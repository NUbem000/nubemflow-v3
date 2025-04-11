import os
import json
from datetime import datetime

def generar_prompt_estructura(objetivo, tipo_proyecto):
    return f"""Genera un listado integral y documentado para la gestión de un proyecto de tipo {tipo_proyecto}.
El objetivo del proyecto es: {objetivo}

Organiza la salida en seis fases principales. En cada fase incluye:
- Nombre y propósito
- Tareas y subtareas descriptivas
- Documentación asociada
- Hitos clave

Incorpora además:
- Gestión de Riesgos y Contingencias
- Control de Calidad y Aseguramiento
- Integración Digital y Tecnológica
- Gestión de Stakeholders
- Sostenibilidad y Normativas Ambientales
- Ciclos de Retroalimentación y Evaluación Continua

Redacta la salida en formato JSON estructurado para facilitar su posterior uso automatizado.
"""

def generar_estructura_tareas_con_gpt(objetivo, tipo_proyecto, nombre_proyecto):
    # Simular llamada a GPT con prompt
    prompt = generar_prompt_estructura(objetivo, tipo_proyecto)

    # Aquí iría la llamada real a GPT; simulamos respuesta
    estructura_simulada = {
        "fases": [
            {
                "nombre": "Estudio y Viabilidad",
                "proposito": "Analizar viabilidad técnica, económica y ambiental.",
                "tareas": [
                    {
                        "nombre": "Análisis de mercado",
                        "documentacion": ["Informe de mercado", "Benchmarking"],
                        "hitos": ["Aprobación de viabilidad comercial"]
                    }
                ]
            }
        ],
        "generado_por": "GPT",
        "timestamp": datetime.now().isoformat(),
        "tipo_proyecto": tipo_proyecto,
        "objetivo": objetivo
    }

    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    out_path = os.path.join(base_dir, f"estructura_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(estructura_simulada, f, indent=2)

    print(f"✅ Estructura generada automáticamente y guardada en: {out_path}")

if __name__ == "__main__":
    nombre = input("📌 Nombre del proyecto: ").strip()
    tipo = input("🏷️ Tipo de proyecto (ej. Construcción, ITSM, Comercial): ").strip()
    objetivo = input("🎯 Objetivo del proyecto: ").strip()
    generar_estructura_tareas_con_gpt(objetivo, tipo, nombre)
