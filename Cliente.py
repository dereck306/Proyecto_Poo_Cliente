
import socket
import time
import jpysocket
import vlc
from easygui import *



text = "Digite la IP del host"


title = "IP"



output = enterbox(text, title)


host='localhost' 
port=12345    
s1=socket.socket()
s1.connect((host,port)) 
print("Socket Is Connected....")
msgrecv1=s1.recv(1024)
msgrecv1=jpysocket.jpydecode(msgrecv1)
if msgrecv1.startswith('C:'):
    player = vlc.MediaPlayer(msgrecv1)
    player.play()
s1.close() 
print("Connection Closed.")
    
while True:
    s = socket.socket()
    try:
        print('Trying to connect...')
        s.connect(('localhost',12345))
        print('Connected.')
            
        try:
            while True:
                msgrecv=s.recv(1024) 
                msgrecv=jpysocket.jpydecode(msgrecv) 
            
                

                    
                if msgrecv.startswith('pausar'):
                        player.pause()
                if msgrecv.startswith('empezar'):
                        player.play()
                else:
                    if not msgrecv: break      
                        

        finally:
            s.close()
            print('Disconnected.')
    except ConnectionError: 
        time.sleep(1)

