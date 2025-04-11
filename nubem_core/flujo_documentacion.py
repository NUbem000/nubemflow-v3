# flujo_documentacion.py

import os
import json
import datetime
from typing import Optional, List

# from nubem_core.memoria.memoria_firestore import guardar_log_version
from nubem_core.google_services.gpt_engine import generar_con_gpt
from nubem_core.google_services.api_confluence import crear_pagina_confluence, actualizar_pagina_confluence
from nubem_core.google_services.envio_email import enviar_correo_con_adjunto
from utils import convertir_html_a_pdf


def generar_documentacion_con_gpt(contexto: dict) -> dict:
    """
    Genera documentación técnica estructurada usando GPT y un contexto detallado.
    Itera hasta 3 veces para mejorar la calidad.
    """
    prompt_base = f"""
    Genera una documentación técnica a partir del siguiente contexto:
    Proyecto: {contexto.get('proyecto')}
    Incidencia relacionada: {contexto.get('incidencia')}
    Resumen: {contexto.get('resumen')}
    Scripts implicados: {contexto.get('scripts')}
    Equipo del proyecto: {json.dumps(contexto.get('equipo', {}), indent=2)}
    El documento debe tener: Introducción, Descripción Técnica, Procedimientos y Conclusiones.
    """

    contenido = ""
    for i in range(3):
        respuesta = generar_con_gpt(prompt_base + contenido)
        contenido = respuesta

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    version = "v1.0"
    return {
        "contenido": contenido,
        "version": version,
        "timestamp": timestamp
    }


def subir_a_confluence(titulo: str, contenido: str, espacio: str, pagina_padre: Optional[str] = None) -> str:
    return crear_pagina_confluence(titulo, contenido, espacio, pagina_padre)


def actualizar_documentacion(id_pagina: str, nuevo_contenido: str):
    actualizar_pagina_confluence(id_pagina, nuevo_contenido)


def guardar_localmente(nombre_archivo: str, contenido: str):
    path_docs = os.path.join("docs", "tmp")
    os.makedirs(path_docs, exist_ok=True)
    ruta = os.path.join(path_docs, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    # guardar_log_version(nombre_archivo, "v1.0")
    return ruta


def convertir_a_pdf_opcional(contenido: str, nombre_pdf: str = "documentacion.pdf") -> str:
    path_pdf = os.path.join("docs", "pdf")
    os.makedirs(path_pdf, exist_ok=True)
    ruta_pdf = os.path.join(path_pdf, nombre_pdf)
    convertir_html_a_pdf(contenido, ruta_pdf)
    return ruta_pdf


def enviar_documento_por_correo(destinatarios: List[str], asunto: str, cuerpo: str, adjunto_path: Optional[str] = None):
    enviar_correo_con_adjunto(destinatarios, asunto, cuerpo, adjunto_path)
