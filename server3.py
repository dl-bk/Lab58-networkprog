# Створіть клієнтсько-серверний додаток, де клієнт
# надсилає рядок тексту або слово на сервер для
# перекладу на іншу мову. Сервер повертає переклад і
# відправляє його клієнту. Наприклад, клієнт надсилає
# рядок "Hello, how are you?" на сервер, а сервер повертає
# переклад цього рядка на вказану мову. Скористайтеся
# бібліотекою googletrans.
from googletrans import Translator
import socket

def translate_text(text, target_language='en'):
    translator = Translator()
    
    src_lang = translator.detect(text).lang
    
    translation = translator.translate(text, src=src_lang, dest=target_language)
    
    return translation.text

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 6060))

server_socket.listen(1)
print("Waiting for connection...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection with {address} was successfull")

    while True:
        massage = client_socket.recv(1024).decode()
        if massage.lower() == 'exit':
            break

        print(f"CLient: {massage}")    
        response = translate_text(massage)
        client_socket.send(response.encode())

    print(f"Connection with {address} ended")

    client_socket.close()

