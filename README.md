# organizador-de-imagenes

Este script en Python organiza automáticamente imágenes por mes y año en un directorio especificado.

Cómo funciona
El script comienza leyendo todos los archivos en el directorio especificado.
Para cada archivo, se obtiene la fecha de creación del archivo y se convierte en un objeto datetime.
Se extrae el mes y el año del objeto datetime.
Se crea un directorio con el mes y año si no existe en el directorio especificado.
Se mueve el archivo al directorio correspondiente con el mes y año.
Uso
Descargue o clone este repositorio en su computadora.
Abra el archivo image_organizer.py en un editor de código.
Reemplace "path/to/images" en la primera línea con la ruta correcta del directorio de imágenes en su sistema.
Ejecute el script en su terminal o consola de comandos: python image_organizer.py
Verifica que se hayan organizado las imágenes en los directorios correspondientes.
Nota
Ten en cuenta que el script sobreescribirá cualquier directorio existente con el mismo nombre de mes y año. Asegúrate de tener una copia de seguridad de tus imágenes antes de ejecutar el script.
