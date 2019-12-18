import socket
import threading

SIZE = 1024
HOST = input('Enter host name: ')
PORT = int(input('Enter port number: '))


def request(s):
    while True:
        msg = input()
        if msg == 'q' or msg == 'Q':
            s.send(msg.encode())
            s.close()
            return
        s.send(msg.encode('utf-8'))


def response(s):
    while True:
        try:
            data = s.recv(SIZE)
            print(data.decode('utf-8'))
        except OSError:
            s.close()
            return


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(SIZE)
    print(data.decode('utf-8'))
    name = input()
    s.send(name.encode('utf-8'))
    data = s.recv(SIZE)
    print(data.decode('utf-8'))
    print('Enter {name}:{message} for sending message to person;'
          ' {-g} for receiving list with active users;'
          '{q or Q} for exit from chat')
    threading.Thread(target=request, args=(s,)).start()
    threading.Thread(target=response, args=(s,)).start()


