import dns.resolver
import time

def discover_subdominio(dominio):
    f = open("subdomains-top1million-110000.txt", "r")
    contenido = f.readlines()
    f.close()
    lista_subdominios = [
        "www",
        "ftp",
        "aaa",
        "site",
        "cpanel",
        "webmail"
        ]
    
    for elemento in contenido:
        lista_subdominios.append(elemento.strip())
    
    for s in lista_subdominios:
        try:
            answer = dns.resolver.resolve(f"{s}.{dominio}", 'A')
            for ip in answer:
                print(f"[OK]\t{s}.{dominio} - {ip}")
        except dns.resolver.NXDOMAIN:
            print(f"[!]\t{s}.{dominio}")
        except dns.resolver.NoAnswer:
            print(f"[!]\t{s}.{dominio}")
        time.sleep(2)


def main():
    dominio = input("Ingrese el dominio a analizar: ")
    subdominios = discover_subdominio(dominio)

if __name__ == "__main__":
    main()
