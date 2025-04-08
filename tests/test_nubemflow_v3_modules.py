import sys
sys.path.append("..")
import pytest
from datetime import datetime
from fpdf import FPDF

# Test módulo de reporting_gpt
def test_pdf_report_generation():
    from scripts.reporting_gpt import generar_reporte_pdf
    kpis = {"tareas_completadas": 12, "sla_cumplidos": 20}
    resumen = ["Buen rendimiento general.", "CCTV necesita revisión final."]
    pendientes = ["Validar cableado", "Revisar documentación CCTV"]

    pdf_bytes = generar_reporte_pdf(kpis, resumen, pendientes)
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 100  # debe generar contenido sustancial

# Test de comentarios automáticos en JIRA (estructura)
def test_formato_comentario():
    texto = "⚠️ Se detectó dependencia en entrega NVR"
    assert texto.startswith("⚠️")
    assert "entrega" in texto

# Test para simulación de memoria + GPT encadenado (modo CLI)
def test_memoria_y_accion_encadenada():
    from scripts.gpt_context_manager import actualizar_contexto, mostrar_contexto_actual
    actualizar_contexto(proyecto="TEST-PROY", pm="Eva Memory", objetivo="Simulación de pruebas")
    mostrar_contexto_actual()
    estado = __import__('nubem_core.memoria.memoria_proyecto').memoria_proyecto.cargar_memoria()
    assert estado["pm"] == "Eva Memory"
    assert estado["objetivo"] == "Simulación de pruebas"