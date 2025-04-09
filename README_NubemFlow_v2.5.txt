# 📘 NubemFlow v2.5 – Sistema Optimizado

Este repositorio contiene la versión optimizada y modular del sistema NubemFlow, lista para su despliegue, mantenimiento y evolución en entornos reales de gestión IT.

---

## 📁 Estructura del Proyecto

```
NubemFlow_Optimizado/
├── nubem_core/
│   ├── auth.py                  # Autenticación segura con JIRA
│   ├── logger.py                # Logging estructurado (JSON)
│   ├── mailer.py                # Envío de correos con adjuntos
│   ├── utils.py                 # Utilidades de carga y validación
│   ├── predictive/
│   │   └── deteccion_tareas.py  # Detección automática de tareas desde texto
│   ├── monitoring/
│   │   └── kpi_monitor.py       # Registro y alertas de KPIs
│   └── google_services/
│       ├── calendar_api.py      # Gestión de eventos en Google Calendar
│       ├── meet_transcription.py# Base para transcripción de Meet
│       └── oauth_setup.py       # Placeholder de OAuth
├── scripts/
│   ├── crear_tareas_jira_refactor.py
│   ├── main_crearEstructuraEnJIRA_refactor.py
│   ├── informe_mensual_refactor.py
│   ├── propuesta_pm_refactor.py
│   └── retrospectiva_semanal_refactor.py
```

---

## 🚀 Requisitos

- Python 3.8+
- Librerías: `requests`, `fpdf`, `flask`, `smtplib`, `email`, `dotenv`
- Acceso a:
  - API de JIRA (token personal)
  - Cuenta Gmail (con contraseña de aplicación)
  - Cuenta de Google con acceso a Calendar (OAuth)

---

## 🔐 Variables de Entorno

Configura las siguientes variables en `.env` o entorno seguro:

```
JIRA_EMAIL=tu_correo@empresa.com
JIRA_API_TOKEN=xxxxxxxxxxxxxxxx
GMAIL_SENDER=noreply@tudominio.com
GMAIL_PASSWORD=clave_app_gmail
```

---

## 🧪 Ejecución de Scripts

- Crear tareas desde JSON:
  ```bash
  python scripts/crear_tareas_jira_refactor.py
  ```

- Enviar informe mensual:
  ```bash
  python scripts/informe_mensual_refactor.py
  ```

- Ejecutar retrospectiva semanal:
  ```bash
  python scripts/retrospectiva_semanal_refactor.py
  ```

- Seleccionar Project Manager automáticamente:
  ```bash
  python scripts/propuesta_pm_refactor.py
  ```

---

## 🧠 Predicción de Tareas con GPT

El archivo `deteccion_tareas.py` incluye un prompt de sistema optimizado para detectar tareas técnicas desde texto libre. Está preparado para integrarse con OpenAI API o modelos locales.

---

## 📊 Seguimiento de KPIs

El script `kpi_monitor.py` permite:
- Registrar métricas por proyecto y fecha.
- Evaluar alertas según umbrales mínimos.
- Guardar datos en JSON (extensible a Firestore o BigQuery).

---

## 📆 Integración Google Calendar y Meet

El módulo `calendar_api.py` simula la lectura y creación de eventos. Puedes ampliar fácilmente la funcionalidad con `google-api-python-client` y OAuth.

---

## 📦 Estado del Sistema

- Scripts y módulos refactorizados ✅
- Núcleo modular reutilizable ✅
- Seguridad mejorada ✅
- UX orientada a roles técnicos ✅
- Listo para despliegue y ampliación ✅

---

© 2025 NubemFlow Systems