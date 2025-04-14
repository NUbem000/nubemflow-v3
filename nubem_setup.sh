#!/bin/bash

# NubemFlow Setup Inicial – Configura alias y entorno de trabajo

echo "🔧 Configurando entorno NubemFlow..."

# Crear carpeta de backups
mkdir -p ~/Descargas/backups_nubemflow

# Alias para ejecutar el despliegue
echo "alias nubem_deploy='bash ~/Descargas/NubemFlow_v3.0_CloudDeploy/deploy_nubemflow.sh'" >> ~/.bashrc

# Alias para activar entorno virtual
echo "alias nubem_venv='source ~/Descargas/NubemFlow_v3.0_CloudDeploy/.venv/bin/activate'" >> ~/.bashrc

# Alias para ver logs de errores
echo "alias nubem_logs='nano ~/Descargas/NubemFlow_v3.0_CloudDeploy/logs/error_log.md'" >> ~/.bashrc

# Alias para abrir el último ATPC generado
echo "alias nubem_atpc='nano ~/Descargas/NubemFlow_v3.0_CloudDeploy/logs/ATPC_$(ls -t ~/Descargas/NubemFlow_v3.0_CloudDeploy/logs/ATPC_*.md | head -n1 | xargs basename)'" >> ~/.bashrc

# Alias para crear nuevo informe ATPC desde plantilla
echo "alias nubem_new_atpc='cp ~/Descargas/NubemFlow_v3.0_CloudDeploy/docs/plantilla_ATPC.md ~/Descargas/NubemFlow_v3.0_CloudDeploy/docs/ATPC_$(date +%Y-%m-%d).md && nano ~/Descargas/NubemFlow_v3.0_CloudDeploy/docs/ATPC_$(date +%Y-%m-%d).md'" >> ~/.bashrc

# Alias para ver estado del repositorio
echo "alias nubem_status='cd ~/Descargas/NubemFlow_v3.0_CloudDeploy && echo 🔍 RUTA: $PWD && git status && echo Último commit: && git log -1 --oneline'" >> ~/.bashrc

# Alias para crear un backup del proyecto
echo "alias nubem_backup='zip -r ~/Descargas/backups_nubemflow/NubemFlow_backup_$(date +%Y-%m-%d_%H-%M-%S).zip ~/Descargas/NubemFlow_v3.0_CloudDeploy'" >> ~/.bashrc

# Alias y función para restaurar un backup
echo '
nubem_restore() {
  cd ~/Descargas/backups_nubemflow || return
  echo "📦 Backups disponibles:"
  select archivo in NubemFlow_backup_*.zip; do
    if [ -n "$archivo" ]; then
      echo "🔁 Restaurando $archivo..."
      rm -rf ~/Descargas/NubemFlow_v3.0_CloudDeploy
      unzip "$archivo" -d ~/Descargas/
      echo "✅ Restauración completada."
      break
    else
      echo "❌ Selección inválida."
    fi
  done
}
' >> ~/.bashrc
echo "alias nubem_restore='nubem_restore'" >> ~/.bashrc

# Aplicar los cambios
source ~/.bashrc
echo "✅ Configuración completada. Puedes usar tus alias NubemFlow desde ya."
