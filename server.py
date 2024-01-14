import socket

#creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))
#waiting for client connect
server_socket.listen(1)
print("Waiting for connection...")
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection with {address} was successfull")

    #notification exchange
    while True:
        #waiting for clien nofication
        massage = client_socket.recv(1024).decode()
        if massage.lower() == 'exit':
            break
        print(f"CLient: {massage}")
        response = input("Server: ")
        client_socket.send(response.encode())
    
    print(f"Connection with {address} ended")

    client_socket.close()


# connect to Vitalii's VPS

# import socket
# import threading
# from datetime import datetime
# import json


# def receive_message(client_socket):
#     while True:
#         try:
#             message = json.loads(client_socket.recv(1024).decode('utf-8'))
#             print(f"{datetime.now().strftime('%d.%m.%Y %I:%M:%S')} {message['user']}: {message['message']}")
#         except ConnectionResetError:
#             print("Connection lost to server.")
#             break
#         except OSError:
#             break




# host = '185.65.247.209'
# port = 65432

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((host, port))

# receive_thread = threading.Thread(target=receive_message, args=(client,))
# receive_thread.start()

# print("Connected to the server. You can start sending messages.")

# user = input("Enter your name: ")

# try:
#     while True:
#         message_to_send = json.dumps({
#             "user": user,
#             "date": str(datetime.now()),
#             "message": input("Enter your message: ")
#         })

#         client.send(message_to_send.encode('utf-8'))
# except KeyboardInterrupt:
#     print("You have exited the chat.")
# finally:
#     client.close()