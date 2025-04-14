
import os
from datetime import datetime

# === Configuración ===
BASE_DIR = os.path.expanduser("~/NubemFlow_v3.0_CloudDeploy/deploy/subir_tareas_jira")
LOG_FILE = os.path.join(BASE_DIR, "verificacion_log.txt")

archivos_contenido = {
    "main.py": "# Código de la función subir_tareas_jira",
    "requirements.txt": "functions-framework==3.5.0\npython-dotenv\nrequests",
    "deploy.sh": "#!/bin/bash\n# Script de despliegue Cloud Function",
    "test_subida.py": "import requests\n# Script de prueba para invocar subir_tareas_jira"
}

os.makedirs(BASE_DIR, exist_ok=True)

with open(LOG_FILE, "w", encoding="utf-8") as log:
    log.write(f"# Verificación de archivos – {datetime.now().isoformat()}\n\n")

    for nombre, contenido in archivos_contenido.items():
        ruta = os.path.join(BASE_DIR, nombre)
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                actual = f.read()
            if contenido.split("\n")[0] in actual:
                estado = f"✅ {nombre} correcto."
            else:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(contenido)
                estado = f"⚠️ {nombre} existía pero fue actualizado (incompleto)."
        else:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
            estado = f"🆕 {nombre} generado automáticamente."
        log.write(estado + "\n")

print(f"📝 Verificación completa. Revisa el log en: {LOG_FILE}")
