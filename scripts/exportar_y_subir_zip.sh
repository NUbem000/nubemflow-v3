#!/bin/bash

API_URL="https://REGION-PROYECTO.cloudfunctions.net/generarZipProyecto"
GIT_USERNAME="${GIT_USERNAME:-NUbem000}"
GIT_EMAIL="${GIT_EMAIL:-david.anguera@nubemsystems.es}"
GIT_REMOTE_URL="${GIT_REMOTE_URL:-https://github.com/NUbem000/nubemflow-actions-gpt.git}"
GIT_TOKEN="${GIT_TOKEN:-YOUR_GITHUB_TOKEN_HERE}"

PROYECTO="$1"
CARPETA_DESTINO="$2"

if [[ -z "$PROYECTO" || -z "$CARPETA_DESTINO" ]]; then
  echo "Uso: ./exportar_y_subir_zip.sh <nombre_proyecto> <carpeta_destino>"
  exit 1
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ZIP_FILE="entrega_${PROYECTO}_${TIMESTAMP}.zip"
TMP_DIR="/tmp/nubem_export"
mkdir -p "$TMP_DIR"

echo "🔄 Generando ZIP para el proyecto: $PROYECTO"
RESPONSE=$(curl -s -X POST "$API_URL"   -H "Content-Type: application/json"   -d "{"proyecto": "$PROYECTO"}")

ZIP_URL=$(echo "$RESPONSE" | jq -r '.zip_url')

if [[ "$ZIP_URL" == "null" || -z "$ZIP_URL" ]]; then
  echo "[ERROR] No se recibió URL válida del ZIP."
  exit 1
fi

echo "⬇️ Descargando ZIP desde: $ZIP_URL"
curl -sL "$ZIP_URL" -o "$TMP_DIR/$ZIP_FILE"

DEST_PATH="./$CARPETA_DESTINO/$ZIP_FILE"
mv "$TMP_DIR/$ZIP_FILE" "$DEST_PATH"

git config --global user.name "$GIT_USERNAME"
git config --global user.email "$GIT_EMAIL"

git add "$DEST_PATH"
git commit -m "Entrega automática del proyecto '$PROYECTO': $TIMESTAMP"
git pull origin main --rebase
git push origin main
