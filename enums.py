class Bulb():
    class BulbSize():
        SMALL =u'SMALL'
        MEDIUM = u'MEDIUM'
        LARGE = u'LARGE'

    def __init__(self):
        self.isOn=False
        self.size = Bulb.BulbSize.MEDIUM

    def getBulbSize(self):
        return self.size

    def setBulbSize(self, value):
        self.size = value

class BulbDemo():
    @classmethod
    def main(cls,args):
        b = Bulb()
        print("Bulb Size :"+b.getBulbSize())


if __name__ == "__main__":
    import sys
    BulbDemo.main(sys.argv)

    