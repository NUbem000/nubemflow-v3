from nubem_core.gpt.gestionar_peticion_documentacion import gestionar_peticion_documentacion

def procesar_prompt_usuario(prompt_usuario):
    print(f"🤖 GPT escuchando: {prompt_usuario}")

    # Verificar si el usuario quiere generar documentación técnica
    if gestionar_peticion_documentacion(prompt_usuario):
        return  # Flujo ejecutado

    # Aquí seguiría el flujo GPT normal si no fue documentación
    print("GPT: Procesando el resto del contexto como prompt habitual...")
    # respuesta = generar_respuesta_gpt(prompt_usuario)
    # return respuesta

# Simulación de entrada
if __name__ == "__main__":
    while True:
        prompt = input("📝 ¿Qué necesitas?: ")
        if prompt.lower() in ["salir", "exit", "q"]:
            break
        procesar_prompt_usuario(prompt)
