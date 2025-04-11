def mostrar_menu_nubemflow():
    print("=== Menú NubemFlow ===")
    print("1. Crear o editar incidencia (JIRA - Nubemsystems ITSM)")
    print("2. Proyecto IT")
    print("3. Consultar tareas activas")
    print("4. Documentación en Confluence")
    print("5. Automatizar imputación de horas")
    print("6. Ajustes y configuración avanzada")
    print("7. Generar documentación técnica (flujo automático)")
    print("0. Salir")

def ejecutar_opcion(opcion):
    if opcion == "7":
        generar_documentacion_tecnica()

def generar_documentacion_tecnica():
    import os
    import subprocess

    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    script_path = os.path.join(base_dir, "flujo_documentacion_runner.py")
    pythonpath = base_dir
    venv_python = os.path.join(base_dir, "venv", "bin", "python")

    print("🚀 Generando documentación técnica...")

    subprocess.run(
        [venv_python, script_path],
        env={**os.environ, "PYTHONPATH": pythonpath}
    )

    print("✅ Documentación generada y enviada correctamente.")

if __name__ == "__main__":
    while True:
        mostrar_menu_nubemflow()
        opcion = input("Selecciona una opción: ")
        if opcion == "0":
            print("👋 Hasta pronto.")
            break
        ejecutar_opcion(opcion)
