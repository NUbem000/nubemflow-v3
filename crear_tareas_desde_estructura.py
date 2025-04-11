import os
import json

def crear_tareas_desde_estructura(nombre_proyecto):
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    estructura_path = os.path.join(base_dir, f"estructura_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    if not os.path.exists(estructura_path):
        print(f"❌ No se encontró la estructura del proyecto '{nombre_proyecto}'.")
        return

    with open(estructura_path, "r", encoding="utf-8") as f:
        estructura = json.load(f)

    tareas = []
    fases = estructura.get("fases", [])
    for fase in fases:
        nombre_fase = fase.get("nombre", "Fase sin nombre")
        for t in fase.get("tareas", []):
            nombre_tarea = t.get("nombre", "Tarea sin nombre")
            tareas.append({
                "tarea": f"{nombre_fase} – {nombre_tarea}",
                "estado": "pendiente",
                "fase": nombre_fase,
                "responsable": "Por asignar",
                "documentacion": t.get("documentacion", []),
                "hitos": t.get("hitos", [])
            })

    salida_path = os.path.join(base_dir, f"tareas_proyecto_{nombre_proyecto.replace(' ', '_')}.json")
    with open(salida_path, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=2)

    print(f"✅ Se generaron {len(tareas)} tareas a partir de la estructura y se guardaron en:")
    print(f"   {salida_path}")

if __name__ == "__main__":
    nombre = input("📌 Nombre del proyecto: ").strip()
    crear_tareas_desde_estructura(nombre)
