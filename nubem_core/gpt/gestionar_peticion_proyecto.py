import os
import json
import subprocess

def gestionar_peticion_proyecto(prompt_usuario):
    """
    Detecta intención de crear un nuevo proyecto IT y lanza el flujo correspondiente.
    """
    if "nuevo proyecto" in prompt_usuario.lower() or "crear proyecto" in prompt_usuario.lower():
        print("🛠️ Solicitud detectada para crear un nuevo proyecto IT...")

        # Simular preguntas-respuestas desde GPT (puedes reemplazar por input() o GPT contextual)
        nombre = input("📌 Nombre del proyecto: ").strip()
        objetivo = input("🎯 Objetivo del proyecto: ").strip()
        tecnologias = input("🧰 Tecnologías involucradas (coma separadas): ").strip().split(",")

        contexto = {
            "nombre_proyecto": nombre,
            "objetivo": objetivo,
            "tecnologias": [tech.strip() for tech in tecnologias],
            "estructura": {
                "tareas_iniciales": ["Reunión Kickoff", "Definición de alcance", "Asignación de roles"],
                "subcarpetas": ["docs", "scripts", "tests", "entregables"]
            },
            "equipo": {
                "PM": {
                    "nombre": "Laura",
                    "apellido": "Martínez",
                    "email": "laura.martinez@nubemsystems.es"
                },
                "Responsable Técnico": {
                    "nombre": "David",
                    "apellido": "Anguera",
                    "email": "david.anguera@nubemsystems.es"
                }
            }
        }

        base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
        proyecto_path = os.path.join(base_dir, f"contexto_proyecto_{nombre.replace(' ', '_')}.json")

        with open(proyecto_path, "w", encoding="utf-8") as f:
            json.dump(contexto, f, indent=2)

        print(f"✅ Proyecto '{nombre}' configurado y guardado correctamente.")
        return True

    return False
