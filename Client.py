import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = "86.50.38.13"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    def receive_msg_loop():
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                print(f"{message}")
            except:
                print("An error occured!")
                client.close()
                break
            
    def write():
        while True:
            message = input()
            client.send(message.encode(FORMAT))
            
    def main():
        client.connect(ADDR)
        threading.Thread(target=receive_msg_loop).start()
        threading.Thread(target=write).start()


    print("starting client")
    main()
