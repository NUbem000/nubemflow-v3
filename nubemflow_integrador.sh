#!/bin/bash

# Script de mejora NubemFlow: HTML + email + pre-push + Docker (opcional)

PROYECTO=~/Descargas/NubemFlow_v3.0_CloudDeploy
LOG_DIR="$PROYECTO/logs"
HTML_DIR="$PROYECTO/reports"
mkdir -p "$HTML_DIR"

# 1. Crear informe HTML visual a partir del último log
ultimo_log=$(ls -t "$LOG_DIR"/test_log_*.log | head -n1)
html_out="$HTML_DIR/report_$(date '+%Y-%m-%d_%H-%M-%S').html"

echo "<html><head><title>Informe NubemFlow</title></head><body><h1>📄 Informe de Test NubemFlow</h1><pre>" > "$html_out"
cat "$ultimo_log" >> "$html_out"
echo "</pre></body></html>" >> "$html_out"

xdg-open "$html_out" > /dev/null 2>&1 || echo "ℹ️ Abre manualmente el informe: $html_out"

# 2. Envío por correo (requiere mailx o mutt configurado)
DESTINO="david.anguera@nubemsystems.es"
asunto="🧪 NubemFlow - Informe de Test $(date '+%Y-%m-%d')"
if command -v mailx > /dev/null; then
  cat "$ultimo_log" | mailx -s "$asunto" "$DESTINO"
  echo "📧 Informe enviado a $DESTINO"
else
  echo "⚠️ mailx no está instalado. Salta envío de correo."
fi

# 3. Añadir hook pre-push de validación a .git
HOOK_PATH="$PROYECTO/.git/hooks/pre-push"
cat <<'EOF' > "$HOOK_PATH"
#!/bin/bash
echo "🔒 Pre-push Hook: Verificando integridad NubemFlow..."
if grep -q "❌" ~/Descargas/NubemFlow_v3.0_CloudDeploy/logs/test_log_*.log; then
  echo "❌ Hay errores en el último test. Corrige antes de hacer push."
  exit 1
fi
echo "✅ Validación correcta. Procediendo con push..."
EOF
chmod +x "$HOOK_PATH"
echo "🪝 Hook pre-push instalado en $HOOK_PATH"

# 4. Opción de creación de Dockerfile (solo base)
DOCKERFILE="$PROYECTO/Dockerfile"
cat <<EOF > "$DOCKERFILE"
# Imagen base para NubemFlow
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install firebase-admin
CMD ["bash", "deploy_nubemflow.sh", "--auto"]
EOF
echo "🐳 Dockerfile base creado."

echo "✅ Script completado. HTML, email, hooks y Docker configurados."
