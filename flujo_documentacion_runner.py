import json
import os
from datetime import datetime
from nubem_core.flujo_documentacion import (
    generar_documentacion_con_gpt,
    guardar_localmente,
    subir_a_confluence,
    enviar_documento_por_correo
)

# Cargar contexto
BASE_DIR = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
CONTEXT_PATH = os.path.join(BASE_DIR, "contexto_documentacion.json")

with open(CONTEXT_PATH, "r", encoding="utf-8") as f:
    contexto = json.load(f)

# Generar documentación
resultado = generar_documentacion_con_gpt(contexto)
nombre_archivo = f"documentacion_INC-4501_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
ruta_local = guardar_localmente(nombre_archivo, resultado["contenido"])

# Subir a Confluence (mock)
url_confluence = subir_a_confluence("Documentación INC-4501", resultado["contenido"], espacio="NUBEM")

# Enviar por correo (mock)
equipo = contexto.get("equipo", {})
destinatarios = [
    equipo.get("PM", {}).get("email"),
    equipo.get("Técnico", {}).get("email")
]
asunto = "Documentación Técnica – INC-4501"
cuerpo = f"Adjunto encontrarás la documentación generada para el incidente INC-4501. También está disponible en: {url_confluence}"
enviar_documento_por_correo(destinatarios, asunto, cuerpo, ruta_local)

print("✅ Flujo de documentación ejecutado correctamente.")
