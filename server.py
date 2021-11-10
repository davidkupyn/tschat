import socket as s
from _thread import *

server_s = s.socket(s.AF_INET, s.SOCK_STREAM)
server_s.bind((s.gethostname(), 4000))
server_s.listen(5)

while True:
    client, adress = server_s.accept()
    wlc = adress, "Welcome! <3 \n type 'help' for allowed commands"
    client.send(str(wlc).encode())
    client.close()
    break
server_s.close()
priv_server = s.socket(s.AF_INET, s.SOCK_STREAM)
priv_server.bind((s.gethostname(), 7777))
priv_server.listen(5)

while True:
    priv_client, priv_adress = priv_server.accept()
    while True:
        data = priv_client.recv(1024)
        received_msg = data.decode()
        print(received_msg)
        if not received_msg:
            break
        available_assigments = ['help', 'exit', 'login']
        clients = [['david', '08082005'], ['albert', '1234']]
        if received_msg not in available_assigments:
            priv_client.send(b"Didn't understand the assigment")
        if received_msg == 'help':
            priv_client.send(b'Possible assignments: \n login, exit')
        if received_msg == 'exit':
            priv_client.send(b'closing-connection')
        if received_msg == 'login':
            priv_client.send(b'Enter username: ')
            rcv_username = priv_client.recv(1024)
            username = rcv_username.decode()
            priv_client.send(b'Enter password: ')
            rcv_password = priv_client.recv(1024)
            password = rcv_password.decode()
            if (username == clients[0][0] and password == clients[0][1]) or (username == clients[1][0] and password == clients[1][1]) :
                priv_client.send(b'You successfully logged in')
                break
            else:
                priv_client.send(b'Invalid login or password')
            
    