import requests
from bs4 import BeautifulSoup

# URL del blog
url = 'https://danielmaldonado.com.ar/blog'

# Realizar la solicitud GET al sitio web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los elementos <h2> que contienen los títulos
    titles = soup.find_all('h2')
    
    # Imprimir los títulos
    for title in titles:
        print(title.text.strip())
else:
    print("Error al obtener el contenido del sitio web.")
