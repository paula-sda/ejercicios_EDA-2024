import socket
import threading


def __recibir_mensajes(client):
    while True:
        try:
            mensaje = client.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
        except:
            print("Error al recibir el mensaje.")
            client.close()
            break

def __enviar_mensajes(client):
    while True:
        mensaje = input("")
        client.sendall(mensaje.encode('utf-8'))

def iniciar_cliente(HOST,PORT):
    
    # Conectar al servidor
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Crear hilos para enviar y recibir mensajes simultáneamente
    thread_recibir = threading.Thread(target=__recibir_mensajes, args=(client,))
    thread_enviar = threading.Thread(target=__enviar_mensajes, args=(client,))

    thread_recibir.start()
    thread_enviar.start()