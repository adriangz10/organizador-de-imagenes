import os
import shutil
from datetime import datetime

# Directorio de imagenes
path = "D:/Variado"

# Recorrer cada archivo en el directorio
for filename in os.listdir(path):
    # Obtener la fecha de creacion del archivo
    file_path = os.path.join(path, filename)
    creation_time = os.path.getctime(file_path)
    # Convertir la fecha a un objeto datetime
    dt_object = datetime.fromtimestamp(creation_time)
    # Extraer el mes y el año del objeto datetime
    month = dt_object.strftime("%B")
    year = dt_object.strftime("%Y")
    # Crear un directorio con el mes y año si no existe
    new_path = os.path.join(path, year, month)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # Mover el archivo al directorio correspondiente
    shutil.move(file_path, os.path.join(new_path, filename))


