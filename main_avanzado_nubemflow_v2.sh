#!/bin/bash

# ╔════════════════════════════════════════════╗
# ║     🌐 NubemFlow - Script Principal v3.0   ║
# ║         🧠 Versión Completa y Robusta       ║
# ╚════════════════════════════════════════════╝

echo "🔧 Iniciando NubemFlow..."

# ----------------------------------------------
# ✅ 1. Verificar y cargar archivo .env
# ----------------------------------------------
if [ ! -f ".env" ]; then
    echo "⚠️  .env no encontrado. Ejecutando generador interactivo..."
    python3 utils/generar_env.py
fi

REQUIRED_VARS=("GIT_USERNAME" "GIT_TOKEN" "GIT_REMOTE_URL" "JIRA_EMAIL" "JIRA_API_TOKEN" "JIRA_URL" "MAIL_SENDER" "MAIL_PASSWORD" "MAIL_SMTP_SERVER" "MAIL_SMTP_PORT")
set -a
source .env
set +a

missing=()
for var in "${REQUIRED_VARS[@]}"
do
  if [ -z "${!var}" ]; then
    missing+=("$var")
  fi
done

if [ ${#missing[@]} -ne 0 ]; then
    echo "❌ Faltan las siguientes variables:"
    for var in "${missing[@]}"; do echo "   - $var"; done
    exit 1
else
    echo "✅ Variables de entorno cargadas correctamente."
fi

# ----------------------------------------------
# 📂 2. Inicializar logs si no existen
# ----------------------------------------------
if [ ! -f "eliminados_log.md" ]; then
    echo "# 🗑️ Registro de Archivos Eliminados" > eliminados_log.md
fi

if [ ! -f "resumen_ATPC.log" ]; then
    echo "# 📘 Resumen Diario de Automatización (ATPC)" > resumen_ATPC.log
fi

# ----------------------------------------------
# 🧹 3. Limpieza de ~/Descargas
# ----------------------------------------------
echo "🧼 Revisando archivos en ~/Descargas..."
VALID_EXTENSIONS=("sh" "py" "md" "pdf" "txt")
DOWNLOADS=~/Descargas
for file in "$DOWNLOADS"/*; do
  if [ -f "$file" ]; then
    ext="${file##*.}"
    if [[ ! " ${VALID_EXTENSIONS[*]} " =~ " ${ext} " ]]; then
      echo "🗑️  Eliminando archivo no válido: $(basename "$file")"
      echo "[`date '+%Y-%m-%d %H:%M:%S'`] Eliminado: $(basename "$file")" >> eliminados_log.md
      rm "$file"
    fi
  fi
done

# ----------------------------------------------
# 📦 4. Control de versiones
# ----------------------------------------------
SCRIPT="main.sh"
TIMESTAMP=$(date +'%Y%m%d_%H%M%S')
if [ -f "$SCRIPT" ]; then
    cp "$SCRIPT" "main_${TIMESTAMP}.sh"
    echo "📦 Backup creado: main_${TIMESTAMP}.sh"
fi

# ----------------------------------------------
# 🔁 5. Sincronización con GitHub
# ----------------------------------------------
echo "📡 Sincronizando con GitHub..."
if [ ! -d .git ]; then
    git init
    git remote add origin "$GIT_REMOTE_URL"
fi

git add .
git commit -m "Actualización automática: $(date '+%Y-%m-%d %H:%M:%S')"
git pull origin main --rebase
git push origin main

# ----------------------------------------------
# 🧾 6. Resumen Diario
# ----------------------------------------------
echo "[`date '+%Y-%m-%d %H:%M:%S'`] NubemFlow ejecutado correctamente." >> resumen_ATPC.log

echo "✅ Proceso completo de NubemFlow finalizado con éxito."
