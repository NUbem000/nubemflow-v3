#!/bin/bash

# ╔════════════════════════════════════════════════════════╗
# ║        🌐 NubemFlow - Script Principal Avanzado        ║
# ║     🧠 Con Email de Resumen Automático al Finalizar    ║
# ╚════════════════════════════════════════════════════════╝

echo "🔧 Iniciando NubemFlow..."

# ✅ 1. Verificación del .env
if [ ! -f ".env" ]; then
    echo "⚠️  .env no encontrado. Ejecutando generador..."
    python3 utils/generar_env.py
fi

REQUIRED_VARS=("GIT_USERNAME" "GIT_TOKEN" "GIT_REMOTE_URL" "JIRA_EMAIL" "JIRA_API_TOKEN" "JIRA_URL" "MAIL_SENDER" "MAIL_PASSWORD" "MAIL_SMTP_SERVER" "MAIL_SMTP_PORT")
set -a
source .env
set +a

missing=()
for var in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!var}" ]; then missing+=("$var"); fi
done

if [ ${#missing[@]} -ne 0 ]; then
    echo "❌ Variables faltantes:"
    for var in "${missing[@]}"; do echo " - $var"; done
    exit 1
fi

# 📁 2. Inicializar logs si no existen
[ ! -f "eliminados_log.md" ] && echo "# 🗑️ Registro de Archivos Eliminados" > eliminados_log.md
[ ! -f "resumen_ATPC.log" ] && echo "# 📘 Resumen Diario de Automatización (ATPC)" > resumen_ATPC.log

# 🧹 3. Limpieza de ~/Descargas
DOWNLOADS=~/Descargas
VALID_EXT=("sh" "py" "md" "pdf" "txt")
for file in "$DOWNLOADS"/*; do
  if [ -f "$file" ]; then
    ext="${file##*.}"
    if [[ ! " ${VALID_EXT[*]} " =~ " ${ext} " ]]; then
      echo "🗑️  Eliminando: $(basename "$file")"
      echo "[`date '+%Y-%m-%d %H:%M:%S'`] Eliminado: $(basename "$file")" >> eliminados_log.md
      rm "$file"
    fi
  fi
done

# 📦 4. Backup del main.sh
TS=$(date +'%Y%m%d_%H%M%S')
[ -f "main.sh" ] && cp main.sh "main_$TS.sh" && echo "📦 Backup creado: main_$TS.sh"

# 🔁 5. GitHub Sync
if [ ! -d .git ]; then
    git init
    git remote add origin "$GIT_REMOTE_URL"
fi

git add .
git commit -m "Actualización automática: $(date '+%Y-%m-%d %H:%M:%S')"
git pull origin main --rebase
git push origin main

# 📬 6. Enviar resumen diario por correo
echo "✉️ Enviando resumen diario por correo..."

EMAIL_BODY=$(mktemp)
{
  echo "Resumen diario NubemFlow - $(date '+%Y-%m-%d')"
  echo ""
  echo "📝 Log de actividad:"
  tail -n 15 resumen_ATPC.log
  echo ""
  echo "🗑️ Archivos eliminados hoy:"
  tail -n 15 eliminados_log.md
} > "$EMAIL_BODY"

python3 - <<EOF
import smtplib
from email.mime.text import MIMEText
import os

sender = os.getenv("MAIL_SENDER")
password = os.getenv("MAIL_PASSWORD")
smtp_server = os.getenv("MAIL_SMTP_SERVER")
smtp_port = int(os.getenv("MAIL_SMTP_PORT", "587"))

receiver = sender
subject = "📘 NubemFlow – Resumen diario automático"

with open("$EMAIL_BODY", "r") as f:
    body = f.read()

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
    print("✅ Correo enviado correctamente a", receiver)
except Exception as e:
    print("❌ Error al enviar el correo:", e)
EOF

rm "$EMAIL_BODY"

# 📜 7. Registrar ejecución en resumen
echo "[`date '+%Y-%m-%d %H:%M:%S'`] NubemFlow ejecutado correctamente con envío de resumen." >> resumen_ATPC.log
echo "✅ NubemFlow completado con envío de informe diario."
