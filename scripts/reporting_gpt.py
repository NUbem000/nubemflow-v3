from fpdf import FPDF
from datetime import datetime
from nubem_core.logger import log_event

def generar_reporte_pdf(kpis, resumen_gpt, tareas_pendientes, cliente="Hotel Majestic", proyecto="HTX", periodo=None):
    if not periodo:
        periodo = datetime.today().strftime("%B %Y")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"📊 Informe NubemFlow – {cliente}", ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 10, f"Proyecto: {proyecto} | Periodo: {periodo}", ln=True, align="C")
    pdf.ln(10)

    # KPIs
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Indicadores Clave:", ln=True)
    pdf.set_font("Arial", "", 10)
    for k, v in kpis.items():
        pdf.cell(0, 8, f"- {k.replace('_',' ').capitalize()}: {v}", ln=True)
    pdf.ln(5)

    # Resumen GPT
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Análisis GPT:", ln=True)
    pdf.set_font("Arial", "", 10)
    for linea in resumen_gpt:
        pdf.multi_cell(0, 8, f"- {linea}")
    pdf.ln(5)

    # Tareas pendientes
    if tareas_pendientes:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Tareas pendientes:", ln=True)
        pdf.set_font("Arial", "", 10)
        for tarea in tareas_pendientes:
            pdf.cell(0, 8, f"- {tarea}", ln=True)

    log_event("info", "reporting_gpt", "Informe generado en memoria", {"periodo": periodo})
    return pdf.output(dest="S").encode("latin1")

# Ejemplo de uso
if __name__ == "__main__":
    kpis = {
        "sla_cumplidos": 21,
        "tareas_completadas": 17,
        "tickets_criticos": 2
    }
    resumen = [
        "Este mes se mantuvo un ritmo adecuado de ejecución.",
        "Se recomienda reforzar la cobertura del proyecto CCTV.",
        "El equipo mostró buena coordinación interáreas."
    ]
    pendientes = ["Finalizar entrega Wi-Fi", "Validar cableado cámara 4"]

    pdf_bytes = generar_reporte_pdf(kpis, resumen, pendientes)
    with open("informe_gpt.pdf", "wb") as f:
        f.write(pdf_bytes)
    print("✅ Informe generado como informe_gpt.pdf")