import sqlite3
from datetime import datetime
from nubem_core.logger import log_event

DB_PATH = "/mnt/data/nubemflow_kpis.db"

def inicializar_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS kpis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        proyecto TEXT NOT NULL,
        kpi TEXT NOT NULL,
        valor INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def registrar_kpis(proyecto, kpi_dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d")

    for kpi, valor in kpi_dict.items():
        cur.execute("INSERT INTO kpis (fecha, proyecto, kpi, valor) VALUES (?, ?, ?, ?)",
                    (fecha, proyecto, kpi, valor))
        log_event("info", "kpi_sql", f"KPI registrado: {kpi}={valor}", {"proyecto": proyecto, "fecha": fecha})

    conn.commit()
    conn.close()

def obtener_kpis(proyecto, fecha=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    if fecha:
        cur.execute("SELECT kpi, valor FROM kpis WHERE proyecto=? AND fecha=?", (proyecto, fecha))
    else:
        cur.execute("SELECT kpi, valor FROM kpis WHERE proyecto=?", (proyecto,))
    resultados = cur.fetchall()
    conn.close()
    return resultados

def evaluar_alertas(kpi_dict, umbrales):
    alertas = []
    for kpi, valor in kpi_dict.items():
        if kpi in umbrales and valor < umbrales[kpi]:
            alerta = f"⚠️ {kpi}: {valor} por debajo del umbral ({umbrales[kpi]})"
            alertas.append(alerta)
            log_event("warning", "kpi_sql", "Alerta KPI", {"kpi": kpi, "valor": valor, "esperado": umbrales[kpi]})
    return alertas

if __name__ == "__main__":
    inicializar_db()
    # Ejemplo
    registrar_kpis("HTX", {
        "sla_cumplidos": 18,
        "tareas_completadas": 13,
        "tickets_criticos": 4
    })
    alertas = evaluar_alertas({
        "sla_cumplidos": 18,
        "tareas_completadas": 13
    }, {
        "sla_cumplidos": 20,
        "tareas_completadas": 15
    })
    for alerta in alertas:
        print(alerta)