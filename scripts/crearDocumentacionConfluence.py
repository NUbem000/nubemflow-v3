import os
import requests
from nubem_core.logger import log_event
from datetime import datetime

# Requiere variables de entorno:
# CONFLUENCE_USER, CONFLUENCE_TOKEN, CONFLUENCE_BASE_URL, CONFLUENCE_SPACE

def crear_pagina_confluence(titulo, contenido_html, etiquetas=None, padre_id=None):
    user = os.getenv("CONFLUENCE_USER")
    token = os.getenv("CONFLUENCE_TOKEN")
    base_url = os.getenv("CONFLUENCE_BASE_URL")
    space_key = os.getenv("CONFLUENCE_SPACE")

    headers = {
        "Content-Type": "application/json"
    }

    auth = (user, token)

    payload = {
        "type": "page",
        "title": titulo,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": contenido_html,
                "representation": "storage"
            }
        }
    }

    if padre_id:
        payload["ancestors"] = [{"id": padre_id}]

    try:
        res = requests.post(f"{base_url}/rest/api/content", json=payload, headers=headers, auth=auth)
        if res.status_code in (200, 201):
            log_event("info", "confluence", "Página creada correctamente", {
                "titulo": titulo,
                "status": res.status_code
            })
            print(f"✅ Página '{titulo}' publicada en Confluence.")
        else:
            log_event("error", "confluence", "Error al crear página", {
                "status": res.status_code,
                "detalle": res.text
            })
    except Exception as e:
        log_event("critical", "confluence", "Excepción al conectar con Confluence", {"error": str(e)})

# Ejemplo de uso
if __name__ == "__main__":
    html = "<h1>Instalación Wi-Fi – Planta Baja</h1><p>Se configuraron 4 APs y se validó el test de cobertura.</p>"
    crear_pagina_confluence("Informe técnico Wi-Fi – Planta Baja", html)