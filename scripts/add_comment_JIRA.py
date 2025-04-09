import os
import requests
from nubem_core.auth import get_jira_auth_headers
from nubem_core.logger import log_event

def añadir_comentario(issue_key, texto):
    headers = get_jira_auth_headers()
    url = f"https://nubemsystems.atlassian.net/rest/api/3/issue/{issue_key}/comment"
    payload = {"body": texto}

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code in (200, 201):
            log_event("info", "comentario_jira", "Comentario añadido correctamente", {
                "issue": issue_key,
                "preview": texto[:50]
            })
            print(f"✅ Comentario añadido a {issue_key}")
        else:
            log_event("error", "comentario_jira", "Error al añadir comentario", {
                "status": res.status_code,
                "detalle": res.text
            })
    except Exception as e:
        log_event("critical", "comentario_jira", "Excepción al conectar con JIRA", {"error": str(e)})

# Ejemplo
if __name__ == "__main__":
    texto = "🧠 GPT Detectó que esta tarea depende de la entrega del switch principal. Se recomienda replanificar."
    añadir_comentario("HTX-123", texto)