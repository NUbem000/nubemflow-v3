# 🧠 Guía de Redacción de Prompts con Iteración y Foco (2025-04-14)

Esta guía está diseñada para ayudar a cualquier usuario a crear prompts eficaces, reutilizables y centrados, con soporte para iteración automática, modularidad y reencuadre del foco.

---

## 🎯 Objetivo

- Diseñar prompts claros y estructurados.
- Iterar automáticamente hasta alcanzar una versión robusta.
- Evitar dispersión o desvío del objetivo inicial.
- Mantener continuidad incluso después de pausas largas o cambios de contexto.

---

## 📐 Estructura Base Recomendada

```markdown
Contexto: [Describe el sistema, proyecto o problema.]

Objetivo principal: [Qué se busca conseguir.]

Condiciones:
1. [Tecnologías, restricciones o formatos]
2. [Cantidad de iteraciones, reglas de validación]
3. [Compatibilidad con sistemas existentes o integraciones]

Flujo esperado:
- Paso 1: ...
- Paso 2: ...
- ...

Revisión automática:
- Iterar X veces para detectar errores o mejoras
- Validar consistencia, errores y lógica del resultado

Entrega final:
- Resultado funcional, claro y reutilizable
- Comentado o documentado si aplica

Estilo de entrega:
- Preciso, técnico y directo
- En caso de ambigüedad, pedir contexto adicional
```

---

## 🧭 Reencuadre Automático del Foco

Cuando se detecte una desviación del objetivo principal, el asistente debe intervenir con algo como:

> "Parece que estamos derivando hacia otro tema. ¿Quieres volver al punto exacto donde lo dejamos: *[último paso o pregunta relevante]*?"

Y si se retoma una sesión después de una pausa prolongada:

> **Último punto trabajado:** *[X]*  
> **Siguiente paso previsto era:** *[Y]*  
> ¿Deseas retomarlo o redefinir el objetivo?

Este enfoque ayuda a mantener continuidad en proyectos largos, flujos complejos o sesiones con muchas ideas.

---

## 🔁 Plantillas Comunes

### 1. Crear un Script o Flujo
```markdown
Crear un script para [acción específica] que sea compatible con [tecnologías].  
Debe ser modular, registrar errores, y permitir integración futura.  
Iterar X veces y entregar versión final funcional.
```

### 2. Documentación Técnica
```markdown
Documenta el código [X] incluyendo:
- Descripción funcional
- Flujo detallado
- Variables importantes
- Errores comunes y cómo manejarlos
```

### 3. Optimización
```markdown
Revisar y optimizar [X].  
Iterar hasta depurar fallos, redundancias o falta de claridad.  
Entregar versión final y lista de mejoras.
```

---

## 🧠 Uso Sugerido

- Para cualquier proyecto técnico, flujo creativo o integración con herramientas externas.
- Útil en entornos de trabajo complejos, multitarea o cuando se trabaja por fases.
- Ideal como plantilla base para asistentes personalizados, herramientas de IA o documentación interna.
