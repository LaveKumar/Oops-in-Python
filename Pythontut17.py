class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname} @codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} { self.lname}"
    @property  # -> decorator
    def email(self):
        if self.fname==None or self.lname==None:
            return " Email is not set. Please set it later"
        return f"{self.fname}.{self.lname} @codewithharry.com"
    @email.setter
    def email(self,string):
        print("Setting now")
        names= string.split("@")[0]
        fname= names.split(".")[1]
        lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
skillf=Employee("skill","F")
# print(skillf.email)
# print(type(skillf))
# print(type("this is a string"))
# print(id("this is a string"))
# print(id("this is a s"))
# o="this is a string"
# print(dir(o))

import inspect
print(inspect.getmembers(skillf))