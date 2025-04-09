from nubem_core.memoria.memoria_proyecto import (
    cargar_memoria,
    actualizar_memoria,
    añadir_a_lista
)

from nubem_core.logger import log_event

def mostrar_contexto_actual():
    memoria = cargar_memoria()
    print("📌 Contexto actual del proyecto:")
    for k, v in memoria.items():
        if isinstance(v, list):
            print(f"- {k.replace('_', ' ').capitalize()}:")
            for item in v:
                print(f"   • {item}")
        else:
            print(f"- {k.replace('_', ' ').capitalize()}: {v}")

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