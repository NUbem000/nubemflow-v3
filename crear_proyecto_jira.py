import os
import requests
from nubem_core.gpt.gpt_sugerir_plantilla_proyecto import sugerir_plantilla_proyecto

def cargar_credenciales_jira():
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_TOKEN")
    url = os.environ.get("JIRA_URL")
    if not all([email, token, url]):
        print("❌ Faltan variables de entorno.")
        return None, None, None
    return email, token, url

def seleccionar_tipo_equipo():
    opciones = { "1": "software", "2": "service_desk", "3": "business" }
    print("⚙️ Tipo de equipo:")
    print("1. Software")
    print("2. Service Desk (ITSM)")
    print("3. Business (gestión general)")
    return opciones.get(input("Selecciona opción [1-3]: ").strip(), "software")

def seleccionar_plantilla(sugerida=None):
    plantillas = {
        "1": ("Scrum", "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic"),
        "2": ("Kanban", "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic"),
        "3": ("ITSM", "com.atlassian.servicedesk:itil"),
        "4": ("Gestión de Proyectos", "com.atlassian.jira-core-project-templates:project-management")
    }

    print("📐 Plantillas disponibles:")
    for key, (nombre, _) in plantillas.items():
        recomendado = " ← Recomendado" if sugerida and nombre.lower() == sugerida.lower() else ""
        print(f"{key}. {nombre}{recomendado}")

    seleccion = input("Selecciona plantilla [1-4]: ").strip()
    return plantillas.get(seleccion, plantillas["1"])

def seleccionar_acceso():
    accesos = { "1": "open", "2": "limited" }
    print("🔒 Acceso:")
    print("1. open    (Todos los usuarios del sitio pueden ver el proyecto)")
    print("2. limited (Solo los miembros del proyecto asignados manualmente podrán verlo/trabajar)")
    return accesos.get(input("Selecciona opción [1-2]: ").strip(), "open")

def verificar_existencia_proyecto(url, auth, key):
    r = requests.get(f"{url}/rest/api/3/project/{key}", auth=auth)
    return r.status_code == 200

def crear_proyecto_jira():
    email, token, url = cargar_credenciales_jira()
    if not all([email, token, url]):
        return

    nombre = input("📌 Nombre del proyecto: ").strip()
    key = input("🔑 Clave del proyecto (KEY): ").strip().upper()
    objetivo = input("🎯 Objetivo del proyecto: ").strip()
    descripcion = input("🧠 Descripción adicional del proyecto: ").strip()

    tipo_equipo = seleccionar_tipo_equipo()

    sugerida = sugerir_plantilla_proyecto(nombre, objetivo, descripcion)
    if not sugerida:
        print("🤖 No encontré contexto suficiente. ¿Puedes ampliar un poco más?")
        descripcion = input("Descripción extendida: ")
        sugerida = sugerir_plantilla_proyecto(nombre, objetivo, descripcion)

    nombre_plantilla, plantilla_key = seleccionar_plantilla(sugerida)
    acceso = seleccionar_acceso()

    auth = (email, token)

    if verificar_existencia_proyecto(url, auth, key):
        print(f"⚠️ El proyecto con clave '{key}' ya existe.")
        return key

    payload = {
        "key": key,
        "name": nombre,
        "projectTypeKey": tipo_equipo,
        "projectTemplateKey": plantilla_key,
        "description": f"Proyecto generado desde NubemFlow",
        "assigneeType": "PROJECT_LEAD"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{url}/rest/api/3/project", json=payload, auth=auth, headers=headers)

    if response.status_code == 201:
        print(f"✅ Proyecto '{nombre}' creado correctamente con clave '{key}' usando plantilla '{nombre_plantilla}'.")
        return key
    else:
        print("❌ Error al crear el proyecto:", response.status_code)
        print(response.text)
        return None

if __name__ == "__main__":
    crear_proyecto_jira()
