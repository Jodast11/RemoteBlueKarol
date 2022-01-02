import robot as r

r.createRobot()

r.VerzoegerungSetzen(1)

while True:
    if r.IstWand():
        r.RechtsDrehen()
    else:
        r.Hinlegen()
        r.Schritt()


r.waitForCommands()