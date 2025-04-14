#!/bin/bash

# Script de simulación de proyecto: Construcción de residencia universitaria
# y prueba de creación de incidencia

PROYECTO=~/Descargas/NubemFlow_v3.0_CloudDeploy
LOG="$PROYECTO/logs/test_proyecto_$(date '+%Y-%m-%d_%H-%M-%S').log"
echo "🏗️ TEST DE CREACIÓN DE PROYECTO – RESIDENCIA UNIVERSITARIA" > "$LOG"

check() {
  if [ $1 -eq 0 ]; then
    echo "✅ $2" >> "$LOG"
  else
    echo "❌ $2" >> "$LOG"
  fi
}

echo "📋 Simulando proyecto 'Residencia Universitaria UB Campus Bellvitge'" >> "$LOG"

# Simular contexto JSON
mkdir -p "$PROYECTO/contextos"
cat <<EOF > "$PROYECTO/contextos/proyecto_residencia_ub.json"
{
  "nombre_proyecto": "Residencia Universitaria UB Campus Bellvitge",
  "objetivo": "Diseño y construcción de una residencia para estudiantes de la UB con 120 habitaciones, comedor, zonas comunes y espacios sostenibles.",
  "ubicacion": "L'Hospitalet de Llobregat, Barcelona",
  "cliente": "Universitat de Barcelona",
  "equipo_proyecto": [
    {"nombre": "David Anguera", "rol": "PM", "empresa": "NubemSystems"},
    {"nombre": "Maria López", "rol": "Arquitecta", "empresa": "NubemSystems"},
    {"nombre": "Carlos Puig", "rol": "Ingeniero estructural", "empresa": "INGESTEC"}
  ],
  "fases": ["Viabilidad", "Anteproyecto", "Proyecto Ejecutivo", "Ejecución de Obra", "Entrega y Legalización"],
  "tecnologias": ["Revit", "BIM360", "JIRA", "Confluence"],
  "interno": false,
  "tipo": "Construcción"
}
EOF
check $? "Generación de JSON de contexto de proyecto"

# Simular generación de tareas base a partir del contexto
cat <<EOF > "$PROYECTO/jobs/tareas_proyecto_residencia_ub.json"
[
  {"titulo": "Estudio de viabilidad", "fase": "Viabilidad"},
  {"titulo": "Redacción del anteproyecto arquitectónico", "fase": "Anteproyecto"},
  {"titulo": "Coordinación con ingenierías", "fase": "Proyecto Ejecutivo"},
  {"titulo": "Inicio de obra y licitación", "fase": "Ejecución de Obra"},
  {"titulo": "Revisión de normativas locales", "fase": "Entrega y Legalización"}
]
EOF
check $? "Generación de tareas base del proyecto"

# Crear carpeta de incidencias si no existe
mkdir -p "$PROYECTO/incidencias"
cat <<EOF > "$PROYECTO/incidencias/incidencia_test.json"
{
  "titulo": "Test – Problema con planos de instalaciones eléctricas",
  "descripcion": "Se detecta conflicto entre trazado de canalizaciones eléctricas y estructura de forjado en nivel -1. Requiere revisión conjunta entre arquitectura e instalaciones.",
  "tipo_actividad": "Incidencia",
  "proyecto": "Residencia Universitaria UB Campus Bellvitge",
  "prioridad": "Alta",
  "asignado_a": "Carlos Puig",
  "estado": "Abierta"
}
EOF
check $? "Generación de incidencia tipo test"

echo "📄 Log de simulación creado en: $LOG"
cat "$LOG"
