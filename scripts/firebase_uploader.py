import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Ruta al archivo de claves (reemplaza por tu archivo real)
CRED_FILE = "/ruta/a/tu/firebase-key.json"

def inicializar_firestore():
    cred = credentials.Certificate(CRED_FILE)
    firebase_admin.initialize_app(cred)
    return firestore.client()

def subir_kpis_y_reuniones(db, proyecto_id, data_kpis, data_reuniones):
    proyecto_ref = db.collection("proyectos").document(proyecto_id)
    proyecto_ref.set({
        "nombre": f"Proyecto {proyecto_id}",
        "pm": "sin_asignar"
    }, merge=True)

    # KPIs
    for fecha, kpis in data_kpis.items():
        db.collection("proyectos").document(proyecto_id)           .collection("kpis").document(fecha).set(kpis)

    # Reuniones
    for key, reunion in data_reuniones.items():
        db.collection("proyectos").document(proyecto_id)           .collection("reuniones").document(key).set(reunion)

    print("✅ Datos subidos correctamente a Firestore.")

if __name__ == "__main__":
    db = inicializar_firestore()

    # Simulación de datos
    kpis = {
        "2025-04-05": {
            "tareas_completadas": 13,
            "sla_cumplidos": 19,
            "tickets_criticos": 3
        }
    }
    reuniones = {
        "kickoff_wifi": {
            "fecha": "2025-04-10T10:00:00",
            "acta_transcripcion": "Se discutió la implementación Wi-Fi.",
            "tareas_sugeridas": [
                "Configurar AP planta baja",
                "Revisar topología de red"
            ]
        }
    }

    subir_kpis_y_reuniones(db, "HTX", kpis, reuniones)