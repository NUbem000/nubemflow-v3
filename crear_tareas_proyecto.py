import os
import json

def crear_tareas_desde_proyecto(nombre_proyecto):
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    contexto_path = os.path.join(base_dir, f"contexto_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    if not os.path.exists(contexto_path):
        print(f"❌ No se encontró el contexto del proyecto '{nombre_proyecto}'.")
        return

    with open(contexto_path, "r", encoding="utf-8") as f:
        contexto = json.load(f)

    tareas_base = contexto.get("estructura", {}).get("tareas_iniciales", [])
    equipo = contexto.get("equipo", {})
    pm = equipo.get("PM", {}).get("nombre", "PM")
    tecnico = equipo.get("Responsable Técnico", {}).get("nombre", "Técnico")

    tareas = []
    for i, tarea in enumerate(tareas_base):
        responsable = pm if i % 2 == 0 else tecnico
        tareas.append({
            "tarea": tarea,
            "estado": "pendiente",
            "responsable": responsable
        })

    salida_path = os.path.join(base_dir, f"tareas_proyecto_{nombre_proyecto.replace(' ', '_')}.json")
    with open(salida_path, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=2)

    print(f"✅ {len(tareas)} tareas creadas y guardadas en '{salida_path}'.")

# Ejecución directa
if __name__ == "__main__":
    nombre = input("🧠 ¿Nombre del proyecto del que quieres generar tareas?: ")
    crear_tareas_desde_proyecto(nombre)
