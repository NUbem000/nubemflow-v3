import os
import json
from datetime import datetime
from nubem_core.flujo_documentacion import (
    generar_documentacion_con_gpt,
    guardar_localmente,
    subir_a_confluence,
    enviar_documento_por_correo
)

def generar_documentacion_desde_proyecto(nombre_proyecto):
    base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
    json_path = os.path.join(base_dir, f"contexto_proyecto_{nombre_proyecto.replace(' ', '_')}.json")

    if not os.path.exists(json_path):
        print(f"❌ No se encontró el contexto del proyecto '{nombre_proyecto}'.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        contexto = json.load(f)

    # Adaptar el contexto para el motor de documentación
    contexto_doc = {
        "proyecto": contexto.get("nombre_proyecto"),
        "incidencia": f"DOC-{datetime.now().strftime('%Y%m%d')}",
        "resumen": contexto.get("objetivo"),
        "scripts": ["estructura_proyecto.json"],
        "equipo": contexto.get("equipo", {})
    }

    resultado = generar_documentacion_con_gpt(contexto_doc)
    nombre_archivo = f"documentacion_{nombre_proyecto.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    ruta_local = guardar_localmente(nombre_archivo, resultado["contenido"])

    url_confluence = subir_a_confluence(
        titulo=f"Documentación del Proyecto {nombre_proyecto}",
        contenido=resultado["contenido"],
        espacio="NUBEM"
    )

    destinatarios = [v["email"] for v in contexto_doc["equipo"].values()]
    asunto = f"Documentación del Proyecto {nombre_proyecto}"
    cuerpo = f"Adjunto encontrarás la documentación técnica generada para el proyecto {nombre_proyecto}.\nTambién está disponible en: {url_confluence}"

    enviar_documento_por_correo(destinatarios, asunto, cuerpo, ruta_local)
    print("✅ Documentación generada y enviada correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    nombre = input("🧠 ¿Nombre del proyecto que quieres documentar?: ")
    generar_documentacion_desde_proyecto(nombre)
