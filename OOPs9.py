class Dad:
    basketball=1

class Son(Dad):
    dance=2
    basketball = 10
    def isdance(self):
        return f" Yes I can dance {self.dance} no. of times"

class Grandson(Son):
    dance=6
    def isdance(self):
        return f" Jackson Yeah!"\
            f"Yes I dance very awesomely {self.dance} no. of times"


darry=Dad()
larry=Son()
harry=Grandson()
print(harry.basketball)
