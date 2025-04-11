import os
import json
import subprocess

def gestionar_peticion_documentacion(prompt_usuario):
    """
    Detecta intención de generar documentación técnica y lanza el flujo si hay datos suficientes.
    """
    if "documentación" in prompt_usuario.lower() or "documentacion" in prompt_usuario.lower():
        # Extraer posibles datos del prompt
        import re
        match_inc = re.search(r"(INC[-_ ]?\d+)", prompt_usuario, re.IGNORECASE)
        num_inc = match_inc.group(1).replace(" ", "").replace("_", "-") if match_inc else "INC-XXXX"

        print(f"📄 Solicitud detectada para generar documentación técnica de la incidencia: {num_inc}")

        # Crear contexto base
        contexto = {
            "proyecto": "Sistema de Monitorización TI",
            "incidencia": num_inc,
            "resumen": "Resumen pendiente de introducir...",
            "scripts": ["script_principal.py"],
            "equipo": {
                "PM": {
                    "nombre": "Laura",
                    "apellido": "Martínez",
                    "telefono": "600123456",
                    "empresa": "NubemSystems",
                    "direccion": "Carrer de la Tecnologia, 12",
                    "email": "laura.martinez@nubemsystems.es"
                },
                "Técnico": {
                    "nombre": "David",
                    "apellido": "Anguera",
                    "telefono": "600654321",
                    "empresa": "NubemSystems",
                    "direccion": "Passeig de Gràcia, 20",
                    "email": "david.anguera@nubemsystems.es"
                }
            }
        }

        base_dir = "/home/david/Descargas/NubemFlow_v3.0_CloudDeploy"
        contexto_path = os.path.join(base_dir, "contexto_documentacion.json")

        with open(contexto_path, "w", encoding="utf-8") as f:
            json.dump(contexto, f, indent=2)

        print("🧠 Contexto generado. Ejecutando flujo automático...")

        subprocess.run([
            os.path.join(base_dir, "venv/bin/python"),
            os.path.join(base_dir, "flujo_documentacion_runner.py")
        ], env={**os.environ, "PYTHONPATH": base_dir})

        print("✅ Documentación generada automáticamente desde conversación.")
        return True

    return False
