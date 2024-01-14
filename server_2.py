import socket
import threading

#creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))
#waiting for client connect
server_socket.listen(5)
print("Waiting for connection...")


def handle_client(client_socket, address):
    print(f"Connection with {address} was successfull")
    while True:
        location = client_socket.recv(1024).decode()
        if not location:
            break
        with open("weather_data.txt", 'r') as rfile:
            data = rfile.readlines()
            for loc in data:
                if location in loc:
                    response = loc
            
        client_socket.send(response.encode())
    print(f"Connection with {address} lost")
    client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
