import functions_framework
from scripts.flujo_meet_to_jira import flujo_meet_to_jira
import os
<<<<<<< HEAD

@functions_framework.http
def ejecutar_flujo_meet(request):
    usuario = os.getenv("USUARIO_EMAIL", "tecnico@nubemsystems.es")
    proyecto = os.getenv("PROYECTO", "HTX")
    project_key = os.getenv("PROJECT_KEY", "HTX")

    flujo_meet_to_jira(usuario, proyecto, project_key)
    return "✅ Flujo 'reunión → GPT → JIRA' ejecutado correctamente", 200
=======
from flask import Request

@functions_framework.http
def ejecutar_flujo_meet(request: Request):
    """
    Cloud Function: Detecta reuniones → transcribe → GPT → crea tareas en JIRA

    Lee parámetros desde el body JSON:
    {
        "usuario_email": "tecnico@nubemsystems.es",
        "proyecto": "HTX",
        "project_key": "HTX"
    }
    Fallback a variables de entorno si no se pasan.
    """

    data = request.get_json(silent=True) or {}

    usuario = data.get("usuario_email") or os.getenv("USUARIO_EMAIL", "tecnico@nubemsystems.es")
    proyecto = data.get("proyecto") or os.getenv("PROYECTO", "HTX")
    project_key = data.get("project_key") or os.getenv("PROJECT_KEY", "HTX")

    flujo_meet_to_jira(usuario, proyecto, project_key)

    return f"✅ Flujo ejecutado para proyecto: {proyecto}", 200
>>>>>>> 067fa14be1ddbc0bc8296688c42b14c8a9f386c8
