from datetime import datetime
from nubem_core.google_services.calendar_api import obtener_reuniones_proximas
from nubem_core.google_services.meet_transcription import obtener_transcripcion_meet
from nubem_core.predictive.deteccion_tareas import detectar_tareas_desde_texto
from nubem_core.auth import get_jira_auth_headers
from nubem_core.logger import log_event
import requests
import os

def crear_tarea_jira(project_key, resumen):
    headers = get_jira_auth_headers()
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": resumen,
            "description": "Tarea generada automáticamente desde reunión detectada por NubemFlow.",
            "issuetype": {"name": "Task"}
        }
    }
    res = requests.post("https://nubemsystems.atlassian.net/rest/api/3/issue", headers=headers, json=payload)
    if res.status_code in (200, 201):
        key = res.json().get("key")
        log_event("info", "jira_auto", f"Tarea creada en JIRA: {key} – {resumen}")
        return key
    else:
        log_event("error", "jira_auto", "Error creando tarea en JIRA", {"status": res.status_code, "detalle": res.text})
        return None

def flujo_meet_to_jira(usuario_email, proyecto, project_key):
    log_event("info", "flujo_jira", f"Iniciando flujo reunión → GPT → JIRA para {proyecto}")

    reuniones = obtener_reuniones_proximas(usuario_email, proyecto)

    for reunion in reuniones:
        transcripcion = obtener_transcripcion_meet(reunion['titulo'])
        tareas = detectar_tareas_desde_texto(transcripcion)

        if not tareas:
            log_event("warning", "flujo_jira", f"No se detectaron tareas en la reunión: {reunion['titulo']}")
            continue

        for tarea in tareas:
            crear_tarea_jira(project_key, tarea)

if __name__ == "__main__":
    flujo_meet_to_jira("tecnico@nubemsystems.es", "HTX", "HTX")