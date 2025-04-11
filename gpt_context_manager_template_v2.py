from nubem_core.gpt.gestionar_peticion_documentacion import gestionar_peticion_documentacion
from nubem_core.gpt.gestionar_peticion_proyecto import gestionar_peticion_proyecto

def procesar_prompt_usuario(prompt_usuario):
    print(f"🤖 GPT escuchando: {prompt_usuario}")

    # Verificar si es una petición de documentación
    if gestionar_peticion_documentacion(prompt_usuario):
        return

    # Verificar si es una petición de creación de proyecto
    if gestionar_peticion_proyecto(prompt_usuario):
        return

    # Si no coincide con ningún flujo GPT automático
    print("GPT: Procesando el resto del contexto como prompt habitual...")
    # Aquí podrías integrar otros flujos o redirigir a GPT general

# Simulación de entrada
if __name__ == "__main__":
    while True:
        prompt = input("📝 ¿Qué necesitas?: ")
        if prompt.lower() in ["salir", "exit", "q"]:
            break
        procesar_prompt_usuario(prompt)
