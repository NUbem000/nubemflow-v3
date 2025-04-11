#!/bin/bash

echo "🔎 Ejecutando test para flujo_documentacion.py..."

# Asegurar que pytest o unittest esté disponible
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado."
    exit 1
fi

# Ejecutar el test
python3 test_flujo_documentacion.py
