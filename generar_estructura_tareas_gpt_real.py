import os
import json
from datetime import datetime

def generar_prompt_proyecto(contexto):
    return f"""
Dado el siguiente proyecto:

Nombre: {contexto.get('nombre_proyecto')}
Tipo: {contexto.get('tipo')}
Objetivo: {contexto.get('objetivo')}
Descripción adicional: {contexto.get('descripcion', '')}

Genera un JSON con las siguientes claves:
- fases: lista de fases, y cada fase con:
  - nombre
  - proposito
  - tareas: nombre, documentacion, hitos
- generado_por: GPT
- timestamp: ISO 8601

Utiliza lenguaje claro y estructurado. Adapta la respuesta al tipo de proyecto.
"""

def generar_estructura_desde_contexto(nombre_proyecto):
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    contexto_path = os.path.join(base_dir, f"contexto_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    if not os.path.exists(contexto_path):
        print(f"❌ No se encontró el contexto del proyecto '{nombre_proyecto}'.")
        return

    with open(contexto_path, "r", encoding="utf-8") as f:
        contexto = json.load(f)

    prompt = generar_prompt_proyecto(contexto)

    # Aquí invocarías tu GPT personalizado en producción:
    # response = openai.ChatCompletion.create(...)

    # Simulación de estructura generada (test)
    estructura = {
        "fases": [
            {
                "nombre": "Fase 1 - Análisis inicial",
                "proposito": "Evaluar necesidades del proyecto y definir requerimientos.",
                "tareas": [
                    {
                        "nombre": "Recopilación de necesidades del cliente",
                        "documentacion": ["Resumen de requisitos", "Acta de reunión"],
                        "hitos": ["Validación de requisitos"]
                    }
                ]
            }
        ],
        "generado_por": "GPT - Simulado (modo test)",
        "timestamp": datetime.now().isoformat(),
        "proyecto": contexto.get("nombre_proyecto")
    }

    out_path = os.path.join(base_dir, f"estructura_proyecto_{nombre_proyecto.replace(' ', '_')}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(estructura, f, indent=2)

    print(f"✅ Estructura generada y guardada en: {out_path}")

if __name__ == "__main__":
    nombre = input("📌 Nombre del proyecto: ").strip()
    generar_estructura_desde_contexto(nombre)
