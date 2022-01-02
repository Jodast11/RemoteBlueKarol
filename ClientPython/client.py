import socket
import base64
import threading
import time
import json
from types import SimpleNamespace

recivedMessages = []
messagesToSend = []

running = True

def b64dec(input):
    return base64.b64decode(input.encode("ascii")).decode("ascii")

def b64enc(input):
    return base64.b64encode(input.encode("ascii")).decode("ascii")

def reciver(s):
    global recivedMessages
    try:
        while running:
            recived = s.recv(4096)
            recivedMessages.append(b64dec(recived[2:].decode("utf-8")))
            time.sleep(0.3)
    except socket.timeout:
        pass
    except :
        s.close()
        print("Reciver crashed")

def sender(s):
    global messagesToSend
    try:
        while running:
            if len(messagesToSend) > 0:
                s.sendall(bytes(b64enc(messagesToSend[0])+"\n","utf-8"))
                messagesToSend = messagesToSend[1:]
            time.sleep(0.3)
    except:
        print("Sender crashed")
        s.close()

def getReturnValue():
    global recivedMessages
    while len(recivedMessages) < 1:
        time.sleep(0.3)
    # value = type(recivedMessages[0])
    value = recivedMessages[0]
    recivedMessages = recivedMessages[1:]
    # return value
    x = json.loads(value, object_hook=lambda d: SimpleNamespace(**d))
    return b64dec(x.data)

def send(message):
    messagesToSend.append(message)

def runClient():
    HOST = 'localhost'
    PORT = 3333

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    s.settimeout(1)

    reciverThread = threading.Thread(target=reciver, args=(s,))
    senderThread = threading.Thread(target=sender, args=(s,))

    reciverThread.start()
    senderThread.start()

def stop():
    global running
    running = False