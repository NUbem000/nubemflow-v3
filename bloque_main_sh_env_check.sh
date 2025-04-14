# ----------------------------------------------
# ✅ Carga y verificación automática del archivo .env
# ----------------------------------------------

echo "🔍 Verificando existencia de archivo .env..."

if [ ! -f ".env" ]; then
    echo "⚠️  Archivo .env no encontrado. Ejecutando generador interactivo..."
    python3 utils/generar_env.py
fi

echo "✅ Archivo .env detectado. Comprobando variables obligatorias..."

# Variables esperadas
REQUIRED_VARS=("GIT_USERNAME" "GIT_TOKEN" "GIT_REMOTE_URL" "JIRA_EMAIL" "JIRA_API_TOKEN" "JIRA_URL" "MAIL_SENDER" "MAIL_PASSWORD" "MAIL_SMTP_SERVER" "MAIL_SMTP_PORT")

# Cargar .env en entorno de ejecución actual
set -a
source .env
set +a

# Comprobar variables obligatorias
missing=()
for var in "${REQUIRED_VARS[@]}"
do
  if [ -z "${!var}" ]; then
    missing+=("$var")
  fi
done

if [ ${#missing[@]} -ne 0 ]; then
    echo "❌ Faltan las siguientes variables en el archivo .env:"
    for var in "${missing[@]}"; do
        echo "   - $var"
    done
    echo "🛠️  Por favor, ejecuta 'python3 utils/generar_env.py' y vuelve a intentarlo."
    exit 1
else
    echo "✅ Todas las variables obligatorias están presentes en .env"
fi
