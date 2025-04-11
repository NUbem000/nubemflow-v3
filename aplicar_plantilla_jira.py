import requests
import json
import os
import base64

# === CONFIGURACIÓN ===
JIRA_DOMAIN = "https://nubemsystems.atlassian.net"
import sys

JIRA_EMAIL = os.environ.get("JIRA_EMAIL") or input("📧 JIRA_EMAIL: ").strip()
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN") or input("🔑 JIRA_API_TOKEN: ").strip()

if not JIRA_EMAIL or not JIRA_API_TOKEN:
    print("❌ Faltan credenciales. No se puede continuar.")
    sys.exit(1)



auth_raw = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
auth_encoded = base64.b64encode(auth_raw.encode()).decode()

HEADERS = {
    "Authorization": f"Basic {auth_encoded}",
    "Content-Type": "application/json"
}

# === FUNCIONES ===
def cargar_plantilla(nombre_plantilla):
    path = f"./plantillas_jira/{nombre_plantilla}.json"
    with open(path, "r") as file:
        return json.load(file)

def aplicar_configuracion(project_key, config):
    errores = []

    # Tipos de issue
    for issue_type in config.get("issue_types", []):
        res = requests.post(
            f"{JIRA_DOMAIN}/rest/api/3/issuetype",
            headers=HEADERS,
            json=issue_type
        )
        if res.status_code not in [200, 201]:
            errores.append({"tipo_issue": issue_type, "error": res.text})

    # Campos personalizados
    for field in config.get("custom_fields", []):
        res = requests.post(
            f"{JIRA_DOMAIN}/rest/api/3/field",
            headers=HEADERS,
            json=field
        )
        if res.status_code not in [200, 201]:
            errores.append({"campo": field, "error": res.text})

    return errores

# === FLUJO PRINCIPAL ===
def aplicar_plantilla(project_key, nombre_plantilla):
    print(f"Aplicando plantilla '{nombre_plantilla}' al proyecto '{project_key}'...")
    config = cargar_plantilla(nombre_plantilla)
    errores = aplicar_configuracion(project_key, config)

    if errores:
        print("\n❌ Errores durante la aplicación:")
        for e in errores:
            print(e)
    else:
        print("\n✅ Plantilla aplicada con éxito.")

# === EJECUCIÓN ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python aplicar_plantilla_jira.py <PROJECT_KEY> <NOMBRE_PLANTILLA>")
    else:
        aplicar_plantilla(sys.argv[1], sys.argv[2])
