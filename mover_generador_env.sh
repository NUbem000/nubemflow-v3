#!/bin/bash
# Script auxiliar para mover generar_env.py al lugar correcto

SOURCE_PATH="./generar_env.py"
DEST_PATH="./NubemFlow_v3.0_CloudDeploy/utils"

echo "🚀 Creando carpeta si no existe: $DEST_PATH"
mkdir -p "$DEST_PATH"

echo "📦 Moviendo $SOURCE_PATH a $DEST_PATH/"
mv "$SOURCE_PATH" "$DEST_PATH/"

echo "✅ Script generado y movido correctamente a: $DEST_PATH/generar_env.py"
