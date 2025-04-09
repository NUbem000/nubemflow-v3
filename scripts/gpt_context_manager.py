<<<<<<< HEAD
from nubem_core.memoria.memoria_proyecto import (
    cargar_memoria,
    actualizar_memoria,
    añadir_a_lista
)

from nubem_core.logger import log_event

def mostrar_contexto_actual():
    memoria = cargar_memoria()
    print("📌 Contexto actual del proyecto:")
=======
import os
import requests

# Detectar si se debe usar Firestore o memoria local
USE_FIRESTORE = os.getenv("NUBEMFLOW_MODE", "local") == "cloud"

if USE_FIRESTORE:
    from nubem_core.memoria.memoria_firestore import (
        cargar_memoria,
        actualizar_memoria,
        añadir_a_lista
    )
else:
    from nubem_core.memoria.memoria_proyecto import (
        cargar_memoria,
        actualizar_memoria,
        añadir_a_lista
    )

# 🔁 Flujo GPT
def mostrar_contexto_actual(proyecto="HTX"):
    memoria = cargar_memoria(proyecto) if USE_FIRESTORE else cargar_memoria()
    print("📌 Contexto actual:")
>>>>>>> 067fa14be1ddbc0bc8296688c42b14c8a9f386c8
    for k, v in memoria.items():
        if isinstance(v, list):
            print(f"- {k.replace('_', ' ').capitalize()}:")
            for item in v:
                print(f"   • {item}")
        else:
            print(f"- {k.replace('_', ' ').capitalize()}: {v}")

<<<<<<< HEAD
def actualizar_contexto(proyecto=None, pm=None, objetivo=None):
    if proyecto:
        actualizar_memoria("proyecto", proyecto)
    if pm:
        actualizar_memoria("pm", pm)
    if objetivo:
        actualizar_memoria("objetivo", objetivo)
    log_event("info", "gpt_memoria", "Contexto actualizado manualmente")

def sugerir_accion_encadenada(tarea_detectada):
    print(f"🤖 GPT sugiere: ¿Quieres imputar horas para '{tarea_detectada}'?")
    respuesta = input("➡️ [sí / no]: ").strip().lower()
    if respuesta == "sí":
        print("⏱ Acción: redirigiendo a imputación horaria...")
        from add_worklog_JIRA import imputar_horas
        imputar_horas("HTX-XXX", "712020:tecnico01", 2, f"Tarea: {tarea_detectada}")
    else:
        print("🧾 Ok. La tarea será registrada como crítica.")
        añadir_a_lista("tareas_criticas", tarea_detectada)

if __name__ == "__main__":
    mostrar_contexto_actual()
    print("
🔄 Simulación de tarea detectada por GPT:")
    sugerir_accion_encadenada("Revisar cableado de planta 2")
=======
def sugerir_imputacion_para_tarea(tarea_detectada, proyecto="HTX"):
    print(f"🤖 GPT detectó la tarea: '{tarea_detectada}'")
    respuesta = input("➡️ ¿Deseas imputar horas por esta tarea? [sí / no]: ").strip().lower()

    if respuesta != "sí":
        añadir_a_lista(proyecto, "tareas_criticas", tarea_detectada) if USE_FIRESTORE else añadir_a_lista("tareas_criticas", tarea_detectada)
        print("📝 Tarea registrada como crítica.")
        return

    issue_key = input("🔑 Clave del issue JIRA (ej: HTX-123): ").strip().upper()
    horas = float(input("⏱ ¿Cuántas horas deseas imputar?: ").strip())
    comentario = input("🗒 Comentario técnico (opcional): ").strip()

    url = "https://europe-west1-hoteltech-gmail-api.cloudfunctions.net/imputar_horas_jira"
    payload = {
        "issue_key": issue_key,
        "horas": horas,
        "comentario": comentario
    }

    print("📡 Enviando imputación...")
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Horas imputadas correctamente en JIRA.")
    else:
        print("❌ Error al imputar horas:", response.text)

# Ejecución manual
if __name__ == "__main__":
    proyecto = "HTX"
    mostrar_contexto_actual(proyecto)
    sugerir_imputacion_para_tarea("Actualizar topología de red planta 2", proyecto)
>>>>>>> 067fa14be1ddbc0bc8296688c42b14c8a9f386c8
