import sys
sys.path.append("..")
import pytest
from nubem_core.memoria import memoria_proyecto
from datetime import datetime

# ---------- TEST MEMORIA DE PROYECTO ----------

def test_memoria_lectura_y_actualizacion():
    memoria_proyecto.actualizar_memoria("proyecto", "TEST-PROYECTO")
    memoria_proyecto.actualizar_memoria("pm", "Carlos Tester")
    estado = memoria_proyecto.cargar_memoria()
    assert estado["proyecto"] == "TEST-PROYECTO"
    assert estado["pm"] == "Carlos Tester"

def test_memoria_lista_dinamica():
    memoria_proyecto.añadir_a_lista("tareas_criticas", "Probar conexión FTP")
    estado = memoria_proyecto.cargar_memoria()
    assert "Probar conexión FTP" in estado["tareas_criticas"]

# ---------- TEST FORMATO DE TIEMPO PARA WORKLOG ----------

def test_formato_fecha_worklog():
    from add_worklog_JIRA import imputar_horas
    fecha = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000+0000")
    assert "T" in fecha
    assert "+" in fecha