import requests
import argparse
import time

parser = argparse.ArgumentParser(description="Script de Fizzing.")
parser.add_argument("url", help="URL base.")
parser.add_argument("diccionario", help="Diccionario de Fuzzing.")

args = parser.parse_args()

#print(args.url)
#print(args.diccionario)

with open(args.diccionario) as file:
    wordlist = file.read().splitlines()


for linea in wordlist:
    url_completa = args.url + linea
    respuesta = requests.get(url_completa)
    if respuesta.status_code == 200:
        print(f"{url_completa}")
    else:
        pass
    time.sleep(1)
