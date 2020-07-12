import sys


class VariableType():
    @classmethod
    def main(cls,args):
        maxInt = 0
        longstart = maxInt + 1
        floatvalue = 0.1
        str = "Hello world!"
        print("Type of maxint", type(maxInt), "value:", maxInt)
        print("Type of longstart", type(longstart), "value:", longstart)
        print("Type of floatvalue", type(floatvalue), "value",floatvalue)
        print("Type of str", type(str), "value", str)



if __name__ == '__main__':
    import sys
VariableType.main(sys.argv)