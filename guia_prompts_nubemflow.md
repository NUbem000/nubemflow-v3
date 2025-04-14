# 🧠 Guía de Redacción de Prompts – NubemFlow (2025-04-14)

Esta guía está diseñada para ayudarte a crear prompts adaptados al estilo de trabajo modular, iterativo y estratégico de NubemFlow. Es compatible con sistemas GPT personalizados, carga de archivos en proyectos, y la sección “Personalizar ChatGPT”.

---

## 🎯 Objetivo

Crear prompts que:
- Organicen ideas dispersas en flujos funcionales.
- Iteren automáticamente hasta alcanzar una solución robusta.
- Generen módulos reutilizables e integrables.
- Permitan trazabilidad, rollback y control de versiones.
- Se integren directamente en JIRA, GitHub, Firestore y Google Cloud.

---

## 📐 Estructura Base de Prompt

```markdown
Contexto: [Explica el sistema, módulo o problema.]

Objetivo principal: [Define el objetivo puntual.]

Condiciones:
1. [Tecnologías y formatos a usar]
2. [Cantidad de iteraciones, condiciones de validación]
3. [Instrucciones sobre scripts o módulos existentes]

Flujo esperado:
- Paso 1: ...
- Paso 2: ...
- ...

Revisión automática:
- Iterar 11 veces internamente
- Validar errores, coherencia, integración y rendimiento

Entrega final:
- Modular, funcional, sin errores
- Comentado o documentado en markdown
- Adaptado a NubemFlow: logs, rollback, control de versiones

Estilo de entrega:
- Claro y técnico
- Si hay ambigüedad, pedir contexto adicional automáticamente
```

---

## 🛠️ Ejemplo: Creación de Script

```markdown
Contexto: Proyecto NubemFlow. Necesito generar épicas en JIRA automáticamente a partir de una descripción.

Objetivo principal: Crear un script `crear_epica_y_tareas.py` que:
- Interprete la descripción de usuario
- Genere una épica
- Cree subtareas en JIRA relacionadas

Condiciones:
1. Proyecto JIRA: Nubemsystems ITSM (NUB)
2. Integrar con gpt_context_manager.py
3. Detectar tipo de actividad y solicitud automáticamente

Flujo esperado:
- Paso 1: Analizar texto
- Paso 2: Generar épica
- Paso 3: Extraer tareas
- Paso 4: Crear en JIRA
- Paso 5: Confirmar en consola y registrar log

Iterar 11 veces internamente para depurar errores lógicos y de integración.

Entrega final: Script funcional, comentado, con logging y control de errores.
```

---

## 🔁 Plantillas Comunes

### 1. Generación de Script
```markdown
Crear un script que [acción] dentro de NubemFlow.  
Condiciones técnicas: [describir].  
Iterar 11 veces.  
Incluir logs, rollback, control de errores y compatibilidad con rutas/nombres del sistema.
```

### 2. Documentación Técnica
```markdown
Documentar el script [X] en markdown con:
- Descripción funcional
- Flujo paso a paso
- Variables y dependencias
- Gestión de errores
```

### 3. Optimización
```markdown
Optimiza el script [X].  
Corrige errores, refactoriza código, adapta al entorno NubemFlow.  
Iterar hasta 11 veces.  
Indicar cambios aplicados al final.
```

### 4. Plantillas de Proyecto
```markdown
Genera una estructura de tareas para el proyecto “[tipo]”.  
Formato JSON.  
Si falta contexto, preguntar antes de generar.  
Incluye fases, tareas, riesgos, KPIs y entregables.
```

---

## 🔐 Reglas Clave para Prompts en NubemFlow

1. Todo prompt debe escalar o integrarse en producción.
2. No se acepta código sin estructura, logs ni control de errores.
3. Se debe preguntar en caso de ambigüedad.
4. Compatible con los 4 núcleos: JIRA, GitHub, Firestore, GCP.
5. Resultado auditable, modular y reutilizable.

---

## 📦 Uso recomendado
- Subir a `/docs/prompts_estructurados.md` en NubemFlow.
- Integrar como plantilla en GPT personalizado.
- Adjuntar en sección “Personalizar ChatGPT” para contexto continuo.

