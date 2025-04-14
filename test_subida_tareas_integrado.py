
import json
import requests
import os
from datetime import datetime
from glob import glob

# === CONFIGURACIÓN ===
PROJECT_NAME = "Test_Smart_Hotel"
BASE_DIR = os.path.expanduser("~/NubemFlow_v3.0_CloudDeploy")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILENAME = f"log_subida_tareas_{PROJECT_NAME}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILENAME)
CLOUD_FUNCTION_URL = "https://europe-west1-nubemflow-prod.cloudfunctions.net/crearEstructuraEnJIRA"

# === CREAR CARPETA DE LOGS SI NO EXISTE ===
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print(f"📁 Carpeta de logs creada en: {LOG_DIR}")

# === BUSCAR JSON MÁS RECIENTE PARA EL PROYECTO ===
json_pattern = os.path.join(BASE_DIR, f"tareas_proyecto_{PROJECT_NAME}*.json")
json_files = sorted(glob(json_pattern), key=os.path.getmtime, reverse=True)

if not json_files:
    with open(LOG_PATH, "w") as log:
        log.write(f"❌ No se encontró ningún archivo que coincida con: tareas_proyecto_{PROJECT_NAME}*.json\n")
    raise SystemExit(f"❌ No se encontró ningún archivo JSON para el proyecto {PROJECT_NAME}.")

JSON_FILENAME = json_files[0]

# === CARGA DE TAREAS ===
try:
    with open(JSON_FILENAME, "r", encoding="utf-8") as f:
        tareas = json.load(f)
except Exception as e:
    with open(LOG_PATH, "w") as log:
        log.write(f"❌ Error cargando archivo: {JSON_FILENAME}\n{str(e)}\n")
    raise SystemExit(f"❌ Error leyendo {JSON_FILENAME}: {str(e)}")

# === ENVÍO A LA FUNCIÓN EN LA NUBE ===
response = requests.post(
    CLOUD_FUNCTION_URL,
    headers={"Content-Type": "application/json"},
    json={"tareas": tareas}
)

# === LOG DEL RESULTADO ===
with open(LOG_PATH, "w", encoding="utf-8") as log:
    log.write(f"Fecha: {datetime.now().isoformat()}\n")
    log.write(f"Archivo: {JSON_FILENAME}\n")
    log.write(f"URL: {CLOUD_FUNCTION_URL}\n")
    log.write(f"Status: {response.status_code}\n\n")
    log.write("Respuesta:\n")
    log.write(response.text)

print(f"✅ Tareas procesadas desde {JSON_FILENAME}. Log generado en: {LOG_PATH}")
