# 🚀 NubemFlow v3.0 – CloudDeploy

**NubemFlow** es una plataforma inteligente para la gestión de proyectos IT, soporte técnico, automatización documental y control de KPIs, con integración nativa a JIRA, Google Meet, Calendar, Gmail y Confluence.

---

## 🧠 Funcionalidades principales

- **🎯 Detección de reuniones técnicas** y generación de tareas con GPT
- **📅 Integración Google Calendar & Meet** con transcripción automática
- **💬 Generación de incidencias y comentarios en JIRA**
- **📄 Documentación técnica automatizada en Confluence**
- **📊 Seguimiento de KPIs técnicos con análisis predictivo**
- **🧠 Memoria activa (Firestore o Local) por proyecto**

---

## 🧩 Estructura del proyecto

```
nubemflow-v3/
├── deploy/
│   └── flujo_meet_to_jira/
│       ├── main.py                  # Cloud Function: reuniones → JIRA
│       └── requirements.txt
├── scripts/
│   ├── gpt_context_manager.py       # GPT conversacional con memoria activa
│   ├── add_worklog_JIRA.py
│   ├── add_comment_JIRA.py
│   └── crearDocumentacionConfluence.py
├── nubem_core/
│   ├── google_services/            # Meet, Calendar, OAuth
│   ├── memoria/                    # Firestore vs local
│   └── predictive/                 # Detección de tareas
├── plantillas_jira/                # Plantillas exportables a JIRA
└── run_tests.py                    # Pruebas automáticas
```

---

## ☁️ Despliegue en Google Cloud Functions

1. Activa:
   - Cloud Functions
   - Firestore
   - Gmail API
   - Calendar API

2. Configura variables de entorno:

```
USUARIO_EMAIL=tecnico@nubemsystems.es
PROYECTO=HTX
PROJECT_KEY=HTX
NUBEMFLOW_MODE=cloud
```

3. Despliega con:

```bash
gcloud functions deploy ejecutar_flujo_meet \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point ejecutar_flujo_meet \
  --set-env-vars USUARIO_EMAIL=tecnico@nubemsystems.es,PROYECTO=HTX,PROJECT_KEY=HTX,NUBEMFLOW_MODE=cloud
```

---

## 🔐 Seguridad

- Uso de OAuth2 para Gmail y Calendar.
- Firestore como sistema seguro de memoria activa.
- Cloud Functions con acceso restringido vía token/API Gateway (recomendado).

---

## 🧪 Tests

```bash
python run_tests.py
```

---

## 📞 Contacto

Desarrollado por el equipo de **NubemSystems**  
🔗 www.nubemsystems.es
📧 soporte@nubemsystems.es
