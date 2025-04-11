
import os
import sys
from gpt.flujo_proyecto_it import flujo_crear_o_configurar_proyecto
from gpt.flujo_incidencias import flujo_gestion_incidencias

MENU = {
    "1": "Crear o editar incidencia (JIRA - Nubemsystems ITSM)",
    "2": "Crear o editar proyecto IT",
    "3": "Consultar o editar documentación técnica",
    "4": "Generar reporte inteligente",
    "5": "Procesar acta de reunión",
    "6": "Automatizaciones y flujos programados",
    "0": "Salir"
}

def mostrar_menu():
    print("\n📋 Menú Principal – NubemFlow GPT")
    for key, val in MENU.items():
        print(f"  {key}. {val}")

def ejecutar_opcion(opcion):
    if opcion == "1":
        flujo_gestion_incidencias()
    elif opcion == "2":
        flujo_crear_o_configurar_proyecto()
    else:
        print("⚠️ Opción aún no implementada.")

def main():
    while True:
        mostrar_menu()
        seleccion = input("\n➡️ Selecciona una opción: ").strip()

        if seleccion == "0":
            print("👋 Saliendo de NubemFlow. Hasta luego!")
            sys.exit(0)

        ejecutar_opcion(seleccion)

if __name__ == "__main__":
    main()
