"""
📦 Memoria activa de NubemFlow en Firestore (producción)
"""

from google.cloud import firestore
from datetime import datetime

db = firestore.Client()
COLECCION = "memoria"

def cargar_memoria(proyecto_id):
    doc_ref = db.collection(COLECCION).document(proyecto_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {
            "proyecto": proyecto_id,
            "pm": None,
            "objetivo": None,
            "tareas_criticas": [],
            "reuniones": [],
            "incidencias_abiertas": [],
            "fecha_ultima_actualizacion": None
        }

def guardar_memoria(proyecto_id, datos):
    datos["fecha_ultima_actualizacion"] = datetime.utcnow().isoformat()
    db.collection(COLECCION).document(proyecto_id).set(datos)

def actualizar_memoria(proyecto_id, campo, valor):
    memoria = cargar_memoria(proyecto_id)
    memoria[campo] = valor
    guardar_memoria(proyecto_id, memoria)

def añadir_a_lista(proyecto_id, campo, valor):
    memoria = cargar_memoria(proyecto_id)
    if campo not in memoria or not isinstance(memoria[campo], list):
        memoria[campo] = []
    if valor not in memoria[campo]:
        memoria[campo].append(valor)
    guardar_memoria(proyecto_id, memoria)

def guardar_log_version(nombre_archivo, version):
    print(f'[MOCK] Versión registrada para {nombre_archivo} – {version}')

