class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):

        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good" + string)



    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry=Employee("Lucky",4553,"Instructor")
rohan=Employee("Rohan",5000,"Student")
shubham=Programmer("Shubham",555,"Programmer",["python"])
karan=Programmer("Karan",555,"Programmer",["python","C++"])

print(karan.no_of_holidays)
#print(karan.printdetails())