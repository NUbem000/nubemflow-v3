#!/bin/bash

# Script para automatizar la generación del ZIP de entrega de un proyecto NubemFlow

PROYECTO="Residencia Universitaria UB Campus Bellvitge"
DIR=~/Descargas/NubemFlow_v3.0_CloudDeploy/entregas/$PROYECTO
mkdir -p "$DIR"

# Archivos esperados ya generados por GPT
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/contextos/proyecto_residencia_ub.json "$DIR/proyecto_residencia_bellvitge.json"
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/jobs/tareas_proyecto_residencia_ub.json "$DIR/tareas_proyecto_residencia_bellvitge.json"
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/incidencias/incidencia_test.json "$DIR/incidencia_test.json"

# Informe técnico simulado (si no existe)
if [ ! -f "$DIR/informe_proyecto_bellvitge.txt" ]; then
cat <<EOF > "$DIR/informe_proyecto_bellvitge.txt"
Proyecto: Residencia Universitaria UB Campus Bellvitge
Cliente: Universitat de Barcelona
Ubicación: L'Hospitalet de Llobregat, Barcelona
Objetivo: Construcción sostenible de residencia de 120 habitaciones
Fases: Viabilidad, Anteproyecto, Proyecto Ejecutivo, Ejecución, Entrega, Legalización
Herramientas: Revit, BIM 360, AutoCAD, MS Project, Confluence
Clasificación: Comercial
EOF
fi

# Crear ZIP
ZIP_DEST=~/Descargas/NubemFlow_v3.0_CloudDeploy/entregas/export_residencia_bellvitge.zip
zip -j "$ZIP_DEST" "$DIR"/*.json "$DIR"/*.txt > /dev/null

echo "✅ Pack de entrega generado: $ZIP_DEST"
