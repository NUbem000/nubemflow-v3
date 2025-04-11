
import sys

INCIDENCIAS_MENU = {
    "1": "Buscar incidencia existente",
    "2": "Crear nueva incidencia",
    "3": "Ver incidencias por estado",
    "4": "Reasignar / Escalar",
    "5": "Imputar horas",
    "6": "Añadir comentario",
    "0": "Volver al menú principal"
}

def mostrar_menu_incidencias():
    print("\n🛠️  Gestión de Incidencias – Nubemsystems ITSM")
    for key, val in INCIDENCIAS_MENU.items():
        print(f"  {key}. {val}")

def ejecutar_opcion_incidencia(opcion):
    if opcion == "1":
        print("🔍 Buscar incidencia (por clave, resumen o filtros)...")
    elif opcion == "2":
        print("🆕 Crear nueva incidencia...")
    elif opcion == "3":
        print("📊 Ver incidencias por estado...")
    elif opcion == "4":
        print("🔄 Reasignar / Escalar incidencia...")
    elif opcion == "5":
        print("⏱️ Imputar horas...")
    elif opcion == "6":
        print("💬 Añadir comentario...")
    elif opcion == "0":
        print("🔙 Volviendo al menú principal...")
        return False
    else:
        print("❌ Opción no válida.")
    return True

def flujo_gestion_incidencias():
    activo = True
    while activo:
        mostrar_menu_incidencias()
        opcion = input("\n➡️ Selecciona una opción: ").strip()
        activo = ejecutar_opcion_incidencia(opcion)

if __name__ == "__main__":
    flujo_gestion_incidencias()
