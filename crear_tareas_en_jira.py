import os
import json
import requests

def cargar_credenciales_jira():
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_TOKEN")
    url = os.environ.get("JIRA_URL")

    if not all([email, token, url]):
        print("❌ Faltan variables de entorno: JIRA_EMAIL, JIRA_TOKEN o JIRA_URL.")
        return None, None, None
    return email, token, url

def seleccionar_proyecto():
    print("Selecciona el proyecto JIRA destino:")
    print("1. Nubemsystems ITSM (NUB) [por defecto]")
    print("2. Introducir otro project_key manualmente")

    opcion = input("Opción [1/2]: ").strip()
    if opcion == "2":
        return input("Introduce el project_key de JIRA (ej: DEV): ").strip().upper()
    return "NUB"

def cargar_tareas(nombre_proyecto):
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    tareas_path = os.path.join(base_dir, f"tareas_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    if not os.path.exists(tareas_path):
        print(f"No se encontró el archivo: {tareas_path}")
        return []
    with open(tareas_path, "r", encoding="utf-8") as f:
        return json.load(f)

def crear_tarea_jira(email, token, url, project_key, tarea):
    headers = {
        "Content-Type": "application/json"
    }
    auth = (email, token)
    data = {
        "fields": {
            "project": {"key": project_key},
            "summary": tarea["tarea"],
            "description": "\n".join([
                "Fase: " + tarea.get("fase", ""),
                "Documentación: " + ", ".join(tarea.get("documentacion", [])),
                "Hitos: " + ", ".join(tarea.get("hitos", []))
            ]),
            "issuetype": {"name": "Task"}
        }
    }

    response = requests.post(f"{url}/rest/api/3/issue", headers=headers, json=data, auth=auth)

    if response.status_code == 201:
        issue_key = response.json().get("key")
        print(f"Tarea creada: {issue_key} – {tarea['tarea']}")
        return issue_key
    else:
        print(f"Error al crear tarea: {tarea['tarea']}")
        print(f"{response.status_code} – {response.text}")
        return None

def ejecutar_creacion_tareas():
    nombre = input("Nombre del proyecto (coincide con el JSON): ").strip()
    email, token, url = cargar_credenciales_jira()
    if not all([email, token, url]):
        return

    project_key = seleccionar_proyecto()
    tareas = cargar_tareas(nombre)
    if not tareas:
        return

    print("Creando {} tareas en el proyecto {}...
".format(len(tareas), project_key))
    for tarea in tareas:
        crear_tarea_jira(email, token, url, project_key, tarea)

if __name__ == "__main__":
    ejecutar_creacion_tareas()
