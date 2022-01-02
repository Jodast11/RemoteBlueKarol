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

def MeldungAusgeben(meldung=""):
    client.send("{\"commandType\":\"do\",\"command\":\"MeldungAusgeben\",\"meldung\":\""+meldung+"\"}")

def RucksackMaximumSetzen(maximum):
    client.send("{\"commandType\":\"do\",\"command\":\"RucksackMaximumSetzen\",\"maximum\":\""+str(maximum)+"\"}")

def SprunghoeheSetzen(hoehe):
    client.send("{\"commandType\":\"do\",\"command\":\"SprunghoeheSetzen\",\"hoehe\":\""+str(hoehe)+"\"}")

def VerzoegerungSetzen(verzoegerung):
    client.send("{\"commandType\":\"do\",\"command\":\"VerzoegerungSetzen\",\"verzoegerung\":\""+str(verzoegerung)+"\"}")

def Warten(zeit):
    client.send("{\"commandType\":\"do\",\"command\":\"Warten\",\"verzoegerung\":\""+str(zeit)+"\"}")

#roboter functions with return valuese

def IstWand():
    client.send("{\"commandType\":\"get\",\"command\":\"IstWand\"}")
    return True if client.getReturnValue() == "true" else False

def AnzahlZiegelRucksackGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"AnzahlZiegelRucksackGeben\"}")
    return int(client.getReturnValue())

def AnzahlZiegelVorneGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"AnzahlZiegelVorneGeben\"}")
    return int(client.getReturnValue())

def BlickrichtungGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"BlickrichtungGeben\"}")
    return client.getReturnValue()

def HatZiegelImRucksack():
    client.send("{\"commandType\":\"get\",\"command\":\"HatZiegelImRucksack\"}")
    return True if client.getReturnValue() == "true" else False

def IstBlickNorden():
    client.send("{\"commandType\":\"get\",\"command\":\"IstBlickNorden\"}")
    return True if client.getReturnValue() == "true" else False

def IstBlickSueden():
    client.send("{\"commandType\":\"get\",\"command\":\"IstBlickSueden\"}")
    return True if client.getReturnValue() == "true" else False

def IstBlickOsten():
    client.send("{\"commandType\":\"get\",\"command\":\"IstBlickOsten\"}")
    return True if client.getReturnValue() == "true" else False

def IstBlickWesten():
    client.send("{\"commandType\":\"get\",\"command\":\"IstBlickWesten\"}")
    return True if client.getReturnValue() == "true" else False

def IstMarke(farbe=None):
    moeglicheFarben = ["rot","gelb","blau","grün", "schwarz"]
    if farbe not in moeglicheFarben:
        client.send("{\"commandType\":\"get\",\"command\":\"IstMarke\"}")
    else:
        client.send("{\"commandType\":\"get\",\"command\":\"IstMarke\",\"farbe\":\""+farbe+"\"}")
    return True if client.getReturnValue() == "true" else False

def IstRoboter():
    client.send("{\"commandType\":\"get\",\"command\":\"IstRoboter\"}")
    return True if client.getReturnValue() == "true" else False

def IstRoboterInSicht():
    client.send("{\"commandType\":\"get\",\"command\":\"IstRoboterInSicht\"}")
    return True if client.getReturnValue() == "true" else False

def IstRucksackLeer():
    client.send("{\"commandType\":\"get\",\"command\":\"IstRucksackLeer\"}")
    return True if client.getReturnValue() == "true" else False

def IstRucksackVoll():
    client.send("{\"commandType\":\"get\",\"command\":\"IstRucksackVoll\"}")
    return True if client.getReturnValue() == "true" else False

def IstZiegel(farbe=None):
    moeglicheFarben = ["rot","gelb","blau","grün"]
    if farbe not in moeglicheFarben:
        client.send("{\"commandType\":\"get\",\"command\":\"IstZiegel\"}")
    else:
        client.send("{\"commandType\":\"get\",\"command\":\"IstZiegel\",\"farbe\":\""+farbe+"\"}")
    return True if client.getReturnValue() == "true" else False

def IstZiegelLinks():
    client.send("{\"commandType\":\"get\",\"command\":\"IstZiegelLinks\"}")
    return True if client.getReturnValue() == "true" else False

def IstZiegelRechts():
    client.send("{\"commandType\":\"get\",\"command\":\"IstZiegelRechts\"}")
    return True if client.getReturnValue() == "true" else False

def KennungGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"KennungGeben\"}")
    return int(client.getReturnValue())

def PositionXGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"PositionXGeben\"}")
    return int(client.getReturnValue())

def PositionYGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"PositionYGeben\"}")
    return int(client.getReturnValue())

def RoboterVorneKennungGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"RoboterVorneKennungGeben\"}")
    return int(client.getReturnValue())

def RucksackPruefungGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"RucksackPruefungGeben\"}")
    return True if client.getReturnValue() == "true" else False

def SichtbarkeitGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"SichtbarkeitGeben\"}")
    return True if client.getReturnValue() == "true" else False

def SprungshoeheGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"SprungshoeheGeben\"}")
    return int(client.getReturnValue())

def VerzoegerungGeben():
    client.send("{\"commandType\":\"get\",\"command\":\"VerzoegerungGeben\"}")
    return int(client.getReturnValue())