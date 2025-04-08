"""
📘 Memoria Activa de Proyecto – NubemFlow

Este módulo actúa como una base de memoria temporal o persistente (según configuración),
donde se guarda y consulta el estado del proyecto: PM, tareas críticas, reuniones clave, etc.
Puede ser reemplazado por una base en Firestore o Redis en producción.
"""

import json
from pathlib import Path

MEMORIA_PATH = Path("/mnt/data/memoria_proyecto.json")

def inicializar_memoria_si_no_existe():
    if not MEMORIA_PATH.exists():
        memoria_vacia = {
            "proyecto": None,
            "pm": None,
            "objetivo": None,
            "tareas_criticas": [],
            "reuniones": [],
            "incidencias_abiertas": [],
            "fecha_ultima_actualizacion": None
        }
        guardar_memoria(memoria_vacia)

def cargar_memoria():
    with open(MEMORIA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_memoria(datos):
    with open(MEMORIA_PATH, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

def actualizar_memoria(parte, valor):
    memoria = cargar_memoria()
    memoria[parte] = valor
    guardar_memoria(memoria)

def añadir_a_lista(clave, nuevo_elemento):
    memoria = cargar_memoria()
    if clave not in memoria or not isinstance(memoria[clave], list):
        memoria[clave] = []
    if nuevo_elemento not in memoria[clave]:
        memoria[clave].append(nuevo_elemento)
    guardar_memoria(memoria)

# Inicializar al importar
inicializar_memoria_si_no_existe()

# Ejemplo
if __name__ == "__main__":
    actualizar_memoria("proyecto", "HTX")
    actualizar_memoria("pm", "Ana López")
    añadir_a_lista("tareas_criticas", "Validar cobertura Wi-Fi planta 3")
    print("✅ Memoria actualizada. Estado:")
    print(json.dumps(cargar_memoria(), indent=2, ensure_ascii=False))