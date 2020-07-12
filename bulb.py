class Bulb:
    TotalBulbCount= 0 #Class Variables

    def __init__(self):         #Class Constructor
        Bulb.TotalBulbCount += 1
        self.isOn = False

    @classmethod
    def getBulbCount(cls):          #Class method
        return cls.TotalBulbCount

    def turnOn(self):               #Instance Method
        self.isOn =True

    def turnOff(self):
        self.isOn = False

    def isOnFun(self):
        return  self.isOn

class BulbDemo():
    @classmethod
    def main(cls,args):
        b = Bulb()
        print("Bulb is on return :",b.isOnFun(),b.turnOn())
        print("Bulb is on return",b.isOnFun())
        print(Bulb.getBulbCount())

if __name__ == "__main__":
    import sys
    BulbDemo.main(sys.argv)