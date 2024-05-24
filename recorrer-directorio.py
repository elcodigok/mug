import os

directorio_inicio = '/home/dmaldonado/Herramientas/DVWA/'

for ruta_directorio, subdirectorios, archivos in os.walk(directorio_inicio):
    for nombre_archivo in archivos:
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        print(ruta_completa)
