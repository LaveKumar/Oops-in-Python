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
    def from_str(cls,string):
        return cls(*string.split("-"))
        # paramas=string.split("-")
        # print(paramas)
        # return cls(paramas[0],paramas[1],paramas[2])



harry=Employee("Lucky",4553,"Instructor")
rohan=Employee("Rohan",5000,"Student")
karan=Employee.from_str("Karan-480-Student")

print(karan.salary)