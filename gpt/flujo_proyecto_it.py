
import os
from gpt.integracion_gpt_plantillas import aplicar_plantilla_desde_gpt

PLANTILLAS = [
    "gestion_it_completo",
    "gestion_it_basic",
    "desarrollo_completo",
    "desarrollo_basic"
]

def flujo_crear_o_configurar_proyecto():
    print("\n🧭 Flujo de Configuración de Proyecto IT – NubemFlow")

    # Paso 1: Obtener clave del proyecto
    project_key = input("\n🔑 Introduce la clave del proyecto existente en JIRA (ej: TEST): ").strip()

    # Paso 2: Selección de plantilla
    print("\n📦 Plantillas disponibles para aplicar:")
    for i, plantilla in enumerate(PLANTILLAS, 1):
        print(f"  {i}. {plantilla}")

    try:
        opcion = int(input("\nSelecciona una plantilla (1-4): "))
        plantilla_seleccionada = PLANTILLAS[opcion - 1]
    except (ValueError, IndexError):
        print("❌ Selección inválida. Abortando.")
        return

    # Paso 3: Credenciales
    email = os.environ.get("JIRA_EMAIL") or input("\n📧 JIRA Email: ").strip()
    token = os.environ.get("JIRA_API_TOKEN") or input("🔐 JIRA Token: ").strip()

    # Paso 4: Aplicar plantilla
    resultado = aplicar_plantilla_desde_gpt(project_key, plantilla_seleccionada, email, token)

    # Mostrar resultado
    print("\n📋 Resultado de la aplicación:")
    print(resultado)


if __name__ == "__main__":
    flujo_crear_o_configurar_proyecto()
