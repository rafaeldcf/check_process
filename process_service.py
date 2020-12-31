import psutil
import os
import logging
from datetime import datetime

# Cargamos las fechas actuales para ponerlo en los logs
today = datetime.now()
ahora = today.strftime("%Y-%m-%d %H:%M:%S")

# Fichero para guardar los logs
logging.basicConfig(filename='process_service.log', level=logging.DEBUG)

# Proceso que vamos a buscar que este ejecutandose
process_name = "process_name.py"

#Inicializar variable
process_up = False

# Se miran todos los procesos buscando el de interes
for process in psutil.process_iter():
    cmdline = process.cmdline()
    # Si se encuentra, se cambia variable y se guarda info en el LOG 
    if process_name in cmdline:
        process_up = True
        logging.info(ahora+' - Proceso OK')

# Si no se ha encontrado el proceso, se ejecuta el comando para levantarlo
# En este caso se pone en background y se guarda info en el LOG
if process_up == False:
    # Proceso que debe estar ejecutado en background
    os.system('/usr/bin/nohup /usr/bin/python3 process_name.py &')
    logging.info(ahora+' - Proceso Down, levantandolo')
