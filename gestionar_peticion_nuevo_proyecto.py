import json
import os

def gestionar_peticion_nuevo_proyecto():
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    config_path = os.path.join(base_dir, "config", "plantillas_jira.json")

    if not os.path.exists(config_path):
        print("❌ No se encontró el archivo de configuración de plantillas.")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    print("📦 Tipos de proyecto disponibles:")
    for i, p in enumerate(config["plantillas"], start=1):
        print(f"{i}. {p['nombre']} [{p['tipo']}]")

    opcion = int(input("Selecciona el tipo de proyecto: "))
    seleccion = config["plantillas"][opcion - 1]

    nombre = input("📌 Nombre del proyecto: ").strip()
    objetivo = input("🎯 Objetivo del proyecto: ").strip()
    tecnologias = input("🧰 Tecnologías involucradas (coma separadas): ").split(",")

    # Checkbox I+D e Interno
    interno = input("¿Es un proyecto interno? (s/N): ").lower().startswith("s")
    investigacion = input("¿Es un proyecto de I+D? (s/N): ").lower().startswith("s")

    # Crear contexto completo
    contexto = {
        "nombre_proyecto": nombre,
        "objetivo": objetivo,
        "tipo": seleccion["tipo"],
        "plantilla": seleccion["nombre"],
        "tecnologias": [t.strip() for t in tecnologias],
        "opciones": {
            "interno": interno,
            "i+d": investigacion
        },
        "estructura": {
            "tareas_iniciales": ["Kickoff", "Definición de objetivos", "Asignación de roles"],
            "subcarpetas": ["docs", "scripts", "entregables", "QA"]
        }
    }

    salida_path = os.path.join(base_dir, f"contexto_proyecto_{nombre.replace(' ', '_')}.json")
    with open(salida_path, "w", encoding="utf-8") as f:
        json.dump(contexto, f, indent=2)

    print(f"✅ Proyecto '{nombre}' generado con plantilla '{seleccion['nombre']}' y guardado en:")
    print(f"   {salida_path}")

# Simulación directa
if __name__ == "__main__":
    gestionar_peticion_nuevo_proyecto()
