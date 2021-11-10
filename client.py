import socket as s

client_s = s.socket(s.AF_INET, s.SOCK_STREAM)
client_s.connect((s.gethostname(), 4000))
msg = client_s.recv(2048)
print(msg)

priv_client = s.socket(s.AF_INET, s.SOCK_STREAM)
priv_client.connect((s.gethostname(),7777))

while True:
    command = input('@client/> ')
    priv_client.send(command.encode())
    server_resp = priv_client.recv(2048)
    print(server_resp.decode())
    if server_resp.decode() == 'closing-connection':
        break
        
s.close()
