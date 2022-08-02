#  Use of Self .......
# class Employee:
#     no_of_leaves=8
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
# harry=Employee()
# rohan=Employee()
# harry.name="Lucky"
# harry.salary=455
# harry.role="Instructor"
#
# rohan.name="Rohan"
# rohan.salary=5000
# rohan.role="student"
#
# print(rohan.printdetails())



# Use of   Constructors

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):

        self.name=aname
        self.salary=asalary
        self.role=arole

harry=Employee("Lucky",5000,"Student")
print(harry.salary)