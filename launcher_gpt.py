import os
import subprocess

PLANTILLAS = [
    "gestion_it_completo",
    "gestion_it_basic",
    "desarrollo_completo",
    "desarrollo_basic"
]

print("\n🚀 NubemFlow – Aplicador de Plantillas JIRA")
print("────────────────────────────────────────────")

# Selección de proyecto
project_key = input("📛 Ingresa el Project Key de JIRA (ej: TEST, DEVX): ").strip()

# Selección de plantilla
print("\n📦 Plantillas disponibles:")
for i, nombre in enumerate(PLANTILLAS, 1):
    print(f"  {i}. {nombre}")

try:
    opcion = int(input("\n🔢 Selecciona una plantilla (1-4): "))
    nombre_plantilla = PLANTILLAS[opcion - 1]
except (ValueError, IndexError):
    print("❌ Opción no válida. Saliendo...")
    exit(1)

# Ejecutar el script principal con las variables interactivas
email = input("\n📧 JIRA_EMAIL: ").strip()
token = input("🔑 JIRA_API_TOKEN: ").strip()

os.environ["JIRA_EMAIL"] = email
os.environ["JIRA_API_TOKEN"] = token

print(f"\n⚙️ Aplicando plantilla '{nombre_plantilla}' al proyecto '{project_key}'...\n")
subprocess.run([
    "python3",
    "aplicar_plantilla_jira.py",
    project_key,
    nombre_plantilla
])
