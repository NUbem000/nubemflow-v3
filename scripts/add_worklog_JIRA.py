import os
import requests
from datetime import datetime
from nubem_core.auth import get_jira_auth_headers
from nubem_core.logger import log_event

def imputar_horas(issue_key, tecnico_id, horas, comentario="Registro automático NubemFlow", fecha=None):
    headers = get_jira_auth_headers()
    if fecha is None:
        fecha = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000+0000")

    payload = {
        "comment": comentario,
        "started": fecha,
        "timeSpentSeconds": int(horas * 3600)
    }

    url = f"https://nubemsystems.atlassian.net/rest/api/3/issue/{issue_key}/worklog"

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code in (200, 201):
            log_event("info", "worklog", "Horas imputadas correctamente", {
                "issue": issue_key,
                "horas": horas,
                "usuario": tecnico_id
            })
            print(f"✅ {horas}h imputadas en {issue_key}")
        else:
            log_event("error", "worklog", "Error al imputar horas", {
                "status": res.status_code,
                "detalle": res.text,
                "issue": issue_key
            })
    except Exception as e:
        log_event("critical", "worklog", "Excepción al conectar con JIRA", {"error": str(e)})

# Ejemplo de uso
if __name__ == "__main__":
    imputar_horas("HTX-123", "712020:tecnico01", 2.5, "Trabajo realizado en planta baja")