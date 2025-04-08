from datetime import datetime, timedelta

# Placeholder: aquí irá la lógica real usando Google API Client
def obtener_reuniones_proximas(usuario_email, proyecto=None):
    # Simulación de eventos
    reuniones = [
        {"titulo": "Kickoff HTX", "fecha": "2025-04-10T10:00:00", "proyecto": "HTX"},
        {"titulo": "Seguimiento Wi-Fi", "fecha": "2025-04-12T16:00:00", "proyecto": "HTX"},
        {"titulo": "Revisión CCTV", "fecha": "2025-04-13T09:00:00", "proyecto": "CCTV"}
    ]
    if proyecto:
        reuniones = [r for r in reuniones if r["proyecto"] == proyecto]
    return reuniones

def crear_evento_calendario(titulo, descripcion, fecha_inicio, duracion_horas=1):
    fecha_fin = fecha_inicio + timedelta(hours=duracion_horas)
    evento = {
        "summary": titulo,
        "description": descripcion,
        "start": {"dateTime": fecha_inicio.isoformat(), "timeZone": "Europe/Madrid"},
        "end": {"dateTime": fecha_fin.isoformat(), "timeZone": "Europe/Madrid"}
    }
    # Placeholder para llamada real a Google Calendar API
    print(f"📆 Evento creado: {evento['summary']} – {evento['start']['dateTime']}")
    return evento