import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 6060))

print("Connected to the server")
while True:
    massage = input("You: ")
    client_socket.send(massage.encode())

    if massage.lower() == 'exit':
            break
    
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

    
print("Connection ended")

client_socket.close()