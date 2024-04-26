import socket

def main():
    direccion = input("Ingrese direccion IP: ")
    puerto = int(input("Ingrese puerto : "))
    try:
        s = socket.socket()
        s.connect((direccion, puerto))
        s.settimeout(5)
        print(s.recv(1024))
    except :
        print("Error.")


if __name__ == "__main__":
    main()
