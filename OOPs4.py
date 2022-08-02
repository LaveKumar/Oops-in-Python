class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):

        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod

    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves


harry=Employee("Lucky",4553,"Instructor")
rohan=Employee("Rohan",5000,"Student")

#harry.change_leaves(34)

Employee.no_of_leaves=98  # Because first it will search an instance variable
print(harry.no_of_leaves)