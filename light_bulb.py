class Bulb:
    def __init__(self):
        self.isOn = False

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def isOnFun(self):
        self.isOn = True


c = Bulb()

print(c.turnOn())
