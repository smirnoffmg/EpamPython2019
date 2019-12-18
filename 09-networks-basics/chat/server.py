import socket
import threading

HOST = ''
PORT = 22222
SIZE = 1024
users = {}


def parser_data(data, user_name, c):
    if data.find('-g') != -1:
        c.send('Users:\n'.encode('utf-8'))
        for key, value in users.items():
            c.send(f'\t{value}'.encode('utf-8'))
        return
    index = data.find(':')
    if index != -1:
        name = data[:index]
        data = data[index+1:]
        for key, value in users.items():
            if value == name:
                key.send(f'{user_name}: {data}'.encode('utf-8'))
        return
    msg = f'{user_name}: {data}\n'
    send_message(msg, users)


def send_message(msg, clients):
    for c in clients:
        try:
            c.send(msg.encode('utf-8'))
        except OSError:
            c.close()


def handle_client(c):
    user_name = c.recv(SIZE)
    user_name = user_name.decode("utf-8").strip()
    users[c] = user_name
    c.send(f'You are welcome, {user_name}\n'.encode('utf-8'))

    while True:
        data = c.recv(SIZE)
        data = data.decode("utf-8").strip()
        if data == 'q' or data == 'Q':
            send_message(f'{users[c]} leaved chat\n', users)
            c.close()
            del users[c]
            break
        parser_data(data, user_name, c)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        client, address = s.accept()
        print(f'{address} joined chat')
        client.send(b'Enter you name please: ')
        t = threading.Thread(target=handle_client, args=(client,))
        t.start()

    s.close()
