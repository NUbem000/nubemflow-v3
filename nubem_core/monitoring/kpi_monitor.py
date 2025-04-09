import json
from datetime import datetime
from nubem_core.logger import log_event

# Simulación de base de datos (local JSON temporal)
db_path = "/mnt/data/kpi_registro.json"

def registrar_kpi(proyecto, kpis):
    fecha = datetime.now().strftime("%Y-%m-%d")
    nuevo_registro = {
        "fecha": fecha,
        "proyecto": proyecto,
        "kpis": kpis
    }

    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(nuevo_registro)

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    log_event("info", "kpi_monitor", "KPIs registrados", nuevo_registro)

def evaluar_alertas(kpis, umbrales):
    alertas = []
    for clave, valor in kpis.items():
        if clave in umbrales and valor < umbrales[clave]:
            alertas.append(f"⚠️ KPI bajo: {clave} = {valor} (mínimo esperado: {umbrales[clave]})")

    if alertas:
        log_event("warning", "kpi_monitor", "Alertas de KPI detectadas", {"alertas": alertas})
    return alertas

# Ejemplo
if __name__ == "__main__":
    kpis = {
        "sla_cumplidos": 18,
        "tareas_completadas": 12,
        "tickets_criticos": 5
    }
    umbrales = {
        "sla_cumplidos": 20,
        "tareas_completadas": 15
    }

    registrar_kpi("HTX", kpis)
    alertas = evaluar_alertas(kpis, umbrales)
    for a in alertas:
        print(a)