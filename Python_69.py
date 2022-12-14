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

hindustani_supporter=Employee("Hindustani","Lucky")
#nikhil_raj_pandey=Employee("Nikhil","Raj")
#print(hindustani_supporter.explai())
#print(hindustani_supporter.email)

#hindustani_supporter.fname="US"

#print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"

# print(hindustani_supporter.email)
# print(hindustani_supporter.email)
del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.email)