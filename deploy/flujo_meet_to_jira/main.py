import functions_framework
from scripts.flujo_meet_to_jira import flujo_meet_to_jira
import os

@functions_framework.http
def ejecutar_flujo_meet(request):
    usuario = os.getenv("USUARIO_EMAIL", "tecnico@nubemsystems.es")
    proyecto = os.getenv("PROYECTO", "HTX")
    project_key = os.getenv("PROJECT_KEY", "HTX")

    flujo_meet_to_jira(usuario, proyecto, project_key)
    return "✅ Flujo 'reunión → GPT → JIRA' ejecutado correctamente", 200