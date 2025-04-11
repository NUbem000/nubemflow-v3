def sugerir_plantilla_proyecto(nombre, objetivo, descripcion):
    """
    Simula la lógica GPT custom para recomendar una plantilla en función del contexto.
    Incluye detección extendida para construcción, IT hotelero, soporte técnico, etc.
    """

    contexto = f"{nombre} {objetivo} {descripcion}".lower()

    if any(palabra in contexto for palabra in ["helpdesk", "soporte", "ticket", "servicio técnico", "mesa de ayuda", "incidencias", "sla", "atención cliente"]):
        return "ITSM"

    if any(palabra in contexto for palabra in ["desarrollo", "scrum", "sprint", "backlog", "user story", "agile", "equipo técnico"]):
        return "Scrum"

    if any(palabra in contexto for palabra in ["flujo continuo", "procesos en paralelo", "kanban", "workflow simple"]):
        return "Kanban"

    if any(palabra in contexto for palabra in ["obra", "construcción", "infraestructura", "proyecto técnico", "licitación", "seguimiento de obra", "instalación", "hotel", "residencia universitaria", "equipamiento", "instalaciones", "edificio", "bim", "cctv", "wifi", "sai", "control de accesos", "smart tv"]):
        return "Gestión de Proyectos"

    return None
