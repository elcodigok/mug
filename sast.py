import os
import re

patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
patron_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
patron_secret = r'(?i)\b(?:password|passwd|secret|key|token|api_key|api_secret|username)\b\s*[:=]\s*[\'"]([^\'"]+)[\'"]'

directorio_inicio = '/home/dmaldonado/Herramientas/DVWA/'

def buscar_patrones(arc):
    with open(arc, 'r', encoding='latin-1') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            buscar = re.search(patron_email, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro el correo electronico en linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
            
            buscar = re.search(patron_ip, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro una IP en linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
            
            buscar = re.search(patron_secret, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro un Secreto en linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
    

for ruta_directorio, subdirectorios, archivos in os.walk(directorio_inicio):
    for nombre_archivo in archivos:
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        buscar_patrones(ruta_completa)
