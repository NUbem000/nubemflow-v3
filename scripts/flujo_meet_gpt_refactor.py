from datetime import datetime
from nubem_core.google_services.calendar_api import obtener_reuniones_proximas
from nubem_core.google_services.meet_transcription import obtener_transcripcion_meet
from nubem_core.predictive.deteccion_tareas import detectar_tareas_desde_texto
from nubem_core.logger import log_event

def flujo_reunion_a_tareas(usuario_email, proyecto):
    log_event("info", "flujo_meet", f"Iniciando detección de reuniones para {usuario_email}, proyecto: {proyecto}")

    reuniones = obtener_reuniones_proximas(usuario_email, proyecto)

    for reunion in reuniones:
        log_event("info", "flujo_meet", f"Reunión detectada: {reunion['titulo']} – {reunion['fecha']}")
        
        # Paso 1: Obtener (simulada) transcripción
        transcripcion = obtener_transcripcion_meet(reunion['titulo'])
        log_event("info", "flujo_meet", "Transcripción obtenida", {"resumen": transcripcion[:60] + "..."})

        # Paso 2: Extraer tareas usando GPT
        tareas = detectar_tareas_desde_texto(transcripcion)
        if tareas:
            log_event("info", "flujo_meet", "Tareas detectadas", {"tareas": tareas})
            print(f"📌 Reunión: {reunion['titulo']}")
            for t in tareas:
                print(f"  - {t}")
        else:
            log_event("warning", "flujo_meet", "No se detectaron tareas")

if __name__ == "__main__":
    flujo_reunion_a_tareas("tecnico@nubemsystems.es", "HTX")