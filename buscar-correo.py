import re

patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

nombre_archivo = 'security.php'

with open(nombre_archivo, 'r') as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        buscar = re.search(patron_email, linea)
        if buscar:
            print(f"en el archivo {nombre_archivo} se encontro el correo electronico en linea {numero_linea} - {buscar.group()}")
