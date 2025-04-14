#!/bin/bash

# Script para generar un ZIP de entrega de cualquier proyecto NubemFlow
# Uso: ./generar_zip_proyecto.sh "Nombre del Proyecto"

PROYECTO="$1"

if [ -z "$PROYECTO" ]; then
  echo "❌ Debes indicar el nombre del proyecto como argumento."
  echo "Ejemplo: ./generar_zip_proyecto.sh 'Residencia Universitaria UB Campus Bellvitge'"
  exit 1
fi

BASENAME=$(echo "$PROYECTO" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -d 'áéíóúÁÉÍÓÚñÑ' | tr -cd '[:alnum:]_')
DIR=~/Descargas/NubemFlow_v3.0_CloudDeploy/entregas/$BASENAME
mkdir -p "$DIR"

# Copiar archivos si existen
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/contextos/proyecto_*.json "$DIR/" 2>/dev/null
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/jobs/tareas_proyecto_*.json "$DIR/" 2>/dev/null
cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/incidencias/incidencia_*.json "$DIR/" 2>/dev/null

# Crear informe si no existe
INFORME="$DIR/informe_${BASENAME}.txt"
if [ ! -f "$INFORME" ]; then
cat <<EOF > "$INFORME"
Proyecto: $PROYECTO
Objetivo: [Resumen automático no disponible. Añádelo manualmente si aplica.]
Fases: [Detectadas automáticamente si aplica]
Equipo: [Ver archivo JSON asociado]
Herramientas: [Ver archivo JSON asociado]
Clasificación: [Ver archivo JSON asociado]
EOF
fi

# Crear ZIP
ZIP_DEST=~/Descargas/NubemFlow_v3.0_CloudDeploy/entregas/export_${BASENAME}.zip
zip -j "$ZIP_DEST" "$DIR"/*.json "$DIR"/*.txt > /dev/null

echo "✅ ZIP generado: $ZIP_DEST"
