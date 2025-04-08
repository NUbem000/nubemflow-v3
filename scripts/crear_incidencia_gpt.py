import os
import requests
from datetime import datetime

JIRA_API_URL = "https://nubemsystems.atlassian.net/rest/api/3/issue"
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_API_TOKEN")

def crear_incidencia_jira():
    print("🧠 GPT va a ayudarte a crear una incidencia en JIRA...")

    # Proyecto por defecto
    project_key = "NUB"

    summary = input("📌 Título de la incidencia (Resumen): ").strip()
    descripcion = input("📝 Descripción detallada: ").strip()
    tipo_actividad = input("🧩 Tipo de issue (Task, Bug, Service Request): ").strip().capitalize() or "Task"
    prioridad = input("⚠️ Prioridad (Alta, Media, Baja): ").strip().capitalize() or "Media"
    fecha_limite = input("📅 Fecha límite (opcional, formato YYYY-MM-DD): ").strip()
    etiquetas = input("🏷 Etiquetas (separadas por comas): ").strip().split(",")

    payload = {
        "fields": {
            "project": { "key": project_key },
            "summary": summary,
            "description": descripcion,
            "issuetype": { "name": tipo_actividad },
            "priority": { "name": prioridad },
            "labels": [et.strip() for et in etiquetas if et.strip()]
        }
    }

    if fecha_limite:
        try:
            datetime.strptime(fecha_limite, "%Y-%m-%d")
            payload["fields"]["duedate"] = fecha_limite
        except ValueError:
            print("⚠️ Fecha inválida, se omitirá el campo.")

    print("📡 Enviando incidencia a JIRA...")

    auth = requests.auth.HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)
    headers = { "Content-Type": "application/json" }

    res = requests.post(JIRA_API_URL, json=payload, headers=headers, auth=auth)

    if res.status_code in (200, 201):
        key = res.json().get("key")
        print(f"✅ Incidencia creada con clave: {key}")
    else:
        print("❌ Error al crear incidencia:")
        print(res.status_code, res.text)

# Ejecución directa
if __name__ == "__main__":
    crear_incidencia_jira()