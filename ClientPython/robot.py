import client
import time

def createRobot():
    client.runClient()

def stop():
    client.stop()

def waitForCommands():
    while len(client.messagesToSend) > 0:
        time.sleep(0.3)
    stop()

#roboter functions without return values
def Schritt():
    client.send("{\"commandType\":\"do\",\"command\":\"Schritt\"}")

def LinksDrehen():
    client.send("{\"commandType\":\"do\",\"command\":\"LinksDrehen\"}")

def RechtsDrehen():
    client.send("{\"commandType\":\"do\",\"command\":\"RechtsDrehen\"}")

def Aufheben():
    client.send("{\"commandType\":\"do\",\"command\":\"Aufheben\"}")

def MarkeLoeschen():
    client.send("{\"commandType\":\"do\",\"command\":\"MarkeLoeschen\"}")

def TonErzeugen():
    client.send("{\"commandType\":\"do\",\"command\":\"TonErzeugen\"}")

def QuaderAufstellen():
    client.send("{\"commandType\":\"do\",\"command\":\"QuaderAufstellen\"}")

def QuaderEntfernen():
    client.send("{\"commandType\":\"do\",\"command\":\"QuaderEntfernen\"}")

def SichtbarMachen():
    client.send("{\"commandType\":\"do\",\"command\":\"SichtbarMachen\"}")

def UnsichtbarMachen():
    client.send("{\"commandType\":\"do\",\"command\":\"UnsichtbarMachen\"}")

def Hinlegen(farbe=None):
    moeglicheFarben = ["rot","gelb","blau","grün"]
    if farbe not in moeglicheFarben:
        client.send("{\"commandType\":\"do\",\"command\":\"Hinlegen\"}")
    else:
        client.send("{\"commandType\":\"do\",\"command\":\"Hinlegen\",\"farbe\":\""+farbe+"\"}")

def MarkeSetzen(farbe=None):
    moeglicheFarben = ["rot","gelb","blau","grün", "schwarz"]
    if farbe not in moeglicheFarben:
        client.send("{\"commandType\":\"do\",\"command\":\"MarkeSetzen\"}")
    else:
        client.send("{\"commandType\":\"do\",\"command\":\"MarkeSetzen\",\"farbe\":\""+farbe+"\"}")

#roboter functions with return valuese

def IstWand():
    client.send("{\"commandType\":\"get\",\"command\":\"IstWand\"}")
    print(client.getReturnValue(""))