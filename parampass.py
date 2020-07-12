class ParamPass:
    def __init__(self):
        A = [1,2]
        self.Change(A)

    def Change(self,B):
        B.append(3)


class ParameterPass:
    def __init__(self):
        A = 1
        self.Change(A)
        print(A)

    def Change(self,B):
        self.B = B




class ParameterPassTwo:
    def __init__(self):
        A = [1,2]
        self.Change(A)
        print(A)

    def Change(self,B):
        B = [3,4]



d = ParameterPassTwo()































