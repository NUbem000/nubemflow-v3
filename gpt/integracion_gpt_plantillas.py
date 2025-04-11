
import subprocess
import os

def aplicar_plantilla_desde_gpt(project_key, plantilla_nombre, jira_email, jira_token):
    """
    Aplica una plantilla NubemFlow a un proyecto JIRA existente desde GPT.
    """
    env = os.environ.copy()
    env["JIRA_EMAIL"] = jira_email
    env["JIRA_API_TOKEN"] = jira_token

    comando = [
        "python3",
        "aplicar_plantilla_jira.py",
        project_key,
        plantilla_nombre
    ]

    try:
        print(f"\n🚀 Ejecutando aplicación de plantilla '{plantilla_nombre}' sobre proyecto '{project_key}'...")
        resultado = subprocess.run(comando, capture_output=True, text=True, env=env)

        salida = resultado.stdout
        errores = resultado.stderr

        if resultado.returncode == 0:
            return f"✅ Resultado:\n{salida}"
        else:
            return f"❌ Error durante la ejecución:\nSTDOUT:\n{salida}\nSTDERR:\n{errores}"

    except Exception as e:
        return f"❌ Excepción al ejecutar el script: {str(e)}"


def main():
    try:
        key = os.environ.get("PROJECT_KEY") or input("🔑 Project Key: ").strip()
        plantilla = os.environ.get("PLANTILLA_NOMBRE") or input("📦 Nombre de la plantilla: ").strip()
        email = os.environ.get("JIRA_EMAIL") or input("📧 JIRA Email: ").strip()
        token = os.environ.get("JIRA_API_TOKEN") or input("🔐 JIRA Token: ").strip()

        resultado = aplicar_plantilla_desde_gpt(key, plantilla, email, token)
        print(resultado)
    except OSError as e:
        print(f"❌ Error del sistema: {str(e)}")
    except Exception as e:
        print(f"❌ Excepción inesperada: {str(e)}")

if __name__ == "__main__":
    main()
