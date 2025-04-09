# 🧠 NubemFlow v3.0 – CloudDeploy Edition

Sistema inteligente de gestión de proyectos IT con automatizaciones GPT, JIRA, Confluence, Google Calendar y Firestore.

---

## 🚀 Funcionalidades Clave

- 📆 Flujo automático desde reuniones Calendar → Tareas JIRA
- 🤖 Memoria activa y decisiones encadenadas con GPT
- ⏱ Imputación horaria automatizada en JIRA
- 📝 Documentación técnica en Confluence
- 💬 Comentarios GPT en incidencias
- 📊 Reporting inteligente con análisis y KPIs
- 🔒 Integración segura con OAuth y Firestore

---

## 📁 Estructura del Proyecto

```
nubemflow-v3/
├── scripts/                 # Flujo funcional y automatizaciones
├── nubem_core/              # Núcleo modular (auth, memoria, GPT, logger, etc.)
├── deploy/                  # Funciones listas para Cloud Functions
│   └── flujo_meet_to_jira/  # Flujo GPT-JIRA como Cloud Function
├── tests/                   # Pruebas automatizadas con pytest
├── jobs/                    # Ejecuciones programables
├── .env                     # Variables sensibles (no subir con claves reales)
├── README.md                # Este archivo
```

---

## 🚀 Despliegue en Google Cloud

1. Crear proyecto Firebase + Firestore
2. Configurar OAuth en Google Cloud Console
3. Desplegar `/deploy/flujo_meet_to_jira` con:
```bash
gcloud functions deploy ejecutar_flujo_meet \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point ejecutar_flujo_meet \
  --region europe-west1 \
  --source ./deploy/flujo_meet_to_jira \
  --set-env-vars USUARIO_EMAIL=...,PROYECTO=...,PROJECT_KEY=...
```

---

## 🧪 Pruebas

```bash
python run_tests.py
```

---

## 🧠 Requisitos

- Python 3.11+
- Git
- Cuenta en Google Cloud (con permisos en Functions y Firestore)
- Cuenta JIRA y Confluence

---

## 📫 Contacto

Este repositorio es parte del ecosistema NubemFlow.  
Para soporte o colaboración, contáctanos vía GitHub o correo.