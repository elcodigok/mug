import os
import re
import sys
import vt
from optparse import OptionParser

patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
patron_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
patron_secret = r'(?i)\b(?:password|passwd|secret|key|token|api_key|api_secret|username)\b\s*[:=]\s*[\'"]([^\'"]+)[\'"]'
patron_url = re.compile(
    r'http[s]?://'  # Protocolo http o https
    r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|'  # Dominio
    r'(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # Porcentaje codificado
    r'(?:/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|'  # Ruta
    r'(?:%[0-9a-fA-F][0-9a-fA-F]))*)*'  # Porcentaje codificado en la ruta
)

def main():
    parser = OptionParser()
    parser.add_option("-d", "--directory", dest="directory", help="Ingrese un Directorio de Trabajo.")
    
    (options, args) = parser.parse_args()
    
    if options.directory is None:
        parser.print_help()
        sys.exit()
    else:
        print(options.directory)
        recorrer_directorio(options.directory)
    

def buscar_patrones(arc):
    with open(arc, 'r', encoding='latin-1') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            buscar = re.search(patron_email, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro el correo electronico en la linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
            
            buscar = re.search(patron_ip, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro una IP en la linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
            
            buscar = re.search(patron_secret, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro un Secreto en la linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
            
            buscar = re.search(patron_url, linea)
            if buscar:
                print(f"en el archivo {arc} se encontro una URL en la linea {numero_linea} - {buscar.group()}")
                print("-" * 20)
    

def recorrer_directorio(dire):
    for ruta_directorio, subdirectorios, archivos in os.walk(dire):
        for nombre_archivo in archivos:
            ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
            buscar_patrones(ruta_completa)

if __name__ == '__main__':
    main()
