import threading
import socket

#Watched a tutorial on how socket works to get a basic understanding so some of the code is taken from here https://youtu.be/3QiPPX-KeSc

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"


#global list, bad practice but couldn't think what else to use

listOfClasses = []

def handle_client(conn, addr):
    print(f"[NEW USER] {addr}")
    connected = True
    while connected:
        msg = conn.recv(HEADER)
        if msg == "!DISCONNECT":
            connected = False
            conn.send("Thank you for using this program!".encode(FORMAT))
        elif msg == "!CREATECHAT":
            conn.send("What name would you like to give to the group chat?".encode(FORMAT))
        elif msg == "!JOINCHAT":
            conn.send("Which chat would you like to join?".encode(FORMAT))
    conn.close()
    return

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(ADDR)
        print(f"[LISTENING] Server is listening on {SERVER}")
        server.listen()
        while True:
            conn, addr = server.accept()
            
            conn.send("Hello new user, welcome to [UNNAMED CHAT]\n".encode(FORMAT))
            conn.send("The commands for this chat program are:\n".encode(FORMAT))
            conn.send("1. !NICKNAME      (Changes your nickname for groups)\n".encode(FORMAT))
            conn.send("2. !CREATECHAT    (Creates a new chatroom)\n".encode(FORMAT))
            conn.send("3. !JOINCHAT      (Join a chat room)\n".encode(FORMAT))
            conn.send("4. !LEAVE         (Leave a chat room)\n".encode(FORMAT))
            conn.send("5. !DISCONNECT    (Disconnects from the server)\n".encode(FORMAT))
            conn.send("What would you like to do?\n".encode(FORMAT))
            
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


start()
