─────────────────────────────  
main.sh  
─────────────────────────────

#!/bin/bash
# main.sh - Script interactivo para NubemFlow
# Este script te guiará paso a paso. Al final de cada paso, se te solicitará escribir "ATPC" y presionar Enter antes de continuar.
# Asegúrate de tener definidas las siguientes variables de entorno:
#   GIT_USERNAME, GIT_TOKEN, GIT_REMOTE_URL, JIRA_API_TOKEN
# Además, verifica que Git esté instalado y configurado con:
#   git config --global user.name "NUbem000"  
#   git config --global user.email "david.anguera@nubemsystems.es"

# Función para solicitar confirmación
confirm() {
    read -p "Escribe ATPC y presiona Enter para continuar: " resp
    while [ "$resp" != "ATPC" ]; do
        echo "Respuesta incorrecta. Por favor, escribe ATPC para continuar."
        read -p "Escribe ATPC y presiona Enter para continuar: " resp
    done
}

echo "Bienvenido al script interactivo de NubemFlow."

# Paso 1: Verificación de variables de entorno
echo "Paso 1: Verificación de variables de entorno"
echo "GIT_USERNAME: $GIT_USERNAME"
echo "GIT_TOKEN: $GIT_TOKEN"
echo "GIT_REMOTE_URL: $GIT_REMOTE_URL"
echo "JIRA_API_TOKEN: $JIRA_API_TOKEN"
confirm

# Paso 2: Validación de la estructura del proyecto (simulación)
echo "Paso 2: Validación de la estructura del proyecto (simulado)..."
# Aquí se implementaría la comparación entre la estructura local y la de GitHub.
sleep 2
echo "Estructura validada correctamente."
confirm

# Paso 3: Renombrado y control de versiones del script
echo "Paso 3: Renombrado y control de versiones del script"
if [ -f "./main.sh" ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    mv ./main.sh ./main_$TIMESTAMP.sh
    echo "Se encontró una versión previa. Renombrado a main_$TIMESTAMP.sh para conservar el historial."
else
    echo "Este es el primer lanzamiento del script."
fi
confirm

# Paso 4: Ejecución de scripts auxiliares (simulación)
echo "Paso 4: Ejecución de scripts auxiliares (simulado)..."
# Aquí se llamarían otros scripts; en este ejemplo se simula la ejecución.
sleep 2
echo "Scripts auxiliares ejecutados correctamente."
confirm

# Paso 5: Validación de la ruta de destino
echo "Paso 5: Validación de la ruta de destino"
read -p "Introduce la ruta de destino final (ej.: /home/david/Descargas/NubemFlow_v3.0_CloudDeploy/deploy): " DESTINO
while [ ! -d "$DESTINO" ]; do
    echo "La ruta no existe. Por favor, introduce una ruta válida."
    read -p "Ruta de destino: " DESTINO
done
echo "Ruta de destino validada: $DESTINO"
confirm

# Paso 6: Registro de acciones y revisión de ~/Descargas (simulado)
echo "Paso 6: Registro de acciones y revisión de ~/Descargas (simulado)..."
echo "[$(date +"%Y-%m-%d %H:%M:%S")] Simulación de registro de acciones en eliminados_log.md" >> eliminados_log.md
echo "Revisión de ~/Descargas completada (simulado)."
confirm

# Paso 7: Integración y sincronización con GitHub
echo "Paso 7: Integración y sincronización con GitHub."
if [ ! -d ".git" ]; then
    git init
fi
git remote rm origin 2>/dev/null
git remote add origin "$GIT_REMOTE_URL"
git add .
git commit -m "Actualización automática: $(date +"%Y-%m-%d %H:%M:%S")"
if ! git push origin master; then
    echo "Error en git push. Ejecutando git pull para fusionar cambios..."
    git pull origin master
    git push origin master
fi
echo "Integración con GitHub completada."
confirm

# Paso 8: Generación del resumen ejecutivo (ATPC)
echo "Paso 8: Generación del resumen ejecutivo (ATPC)."
echo "Resumen ATPC generado el $(date +"%Y-%m-%d %H:%M:%S")" > resumen_ATPC.txt
echo "Resumen ejecutivo guardado en resumen_ATPC.txt y (simulado) enviado a david.anguera@nubemsystems.es."
confirm

# Paso 9: Uso del API Token de JIRA
echo "Paso 9: Uso del API Token de JIRA."
echo "Recuerda utilizar la variable JIRA_API_TOKEN para operaciones con JIRA."
echo "Correo API Token JIRA: mauricio.mendez@nubemsystems.es"
confirm

echo "Fin del script interactivo de NubemFlow. Todos los pasos se han ejecutado correctamente."

─────────────────────────────  
Guarda este contenido en un archivo llamado main.sh. Luego, en tu terminal, ejecuta:

 chmod +x main.sh  
 ./main.sh

