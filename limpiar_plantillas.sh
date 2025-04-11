#!/bin/bash

cd ~/Descargas/NubemFlow_v3.0_CloudDeploy/plantillas_jira || exit 1

echo "📦 Limpiando y renombrando archivos de plantillas..."

# Renombrar plantillas finales limpias
mv -v gestion_it_basic_FINAL_LIMPIO.json gestion_it_basic.json 2>/dev/null
mv -v desarrollo_completo_FINAL_LIMPIO.json desarrollo_completo.json 2>/dev/null
mv -v desarrollo_basic_FINAL_LIMPIO.json desarrollo_basic.json 2>/dev/null

# Eliminar duplicados innecesarios
rm -v *_FINAL_LIMPIO.json 2>/dev/null

echo "✅ Plantillas listas:"
ls -1 *.json
