"""
🕒 Job Automático: Revisión de reuniones y creación de tareas en JIRA
Ejecútalo con cron, Airflow, o cualquier scheduler de tu preferencia.
"""

from scripts.flujo_meet_to_jira import flujo_meet_to_jira

# Parámetros configurables (podrían ir en archivo .env)
USUARIO_EMAIL = "tecnico@nubemsystems.es"
PROYECTO = "HTX"
PROJECT_KEY_JIRA = "HTX"

if __name__ == "__main__":
    flujo_meet_to_jira(USUARIO_EMAIL, PROYECTO, PROJECT_KEY_JIRA)