class Employee:
    no_of_leaves=8
    pass

harry=Employee()
rohan=Employee()
harry.name="Lucky"
harry.salary=455
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=5000
rohan.role="student"

print(rohan.no_of_leaves)  # leaves can be accesed by - rohan , harry,Employee
# Employee.no_of_leaves=9
#print(rohan.__dict__)
print(Employee.__dict__)
rohan.no_of_leaves=9  # rohan.no_of_leaves  makes new instanc of variable
print(rohan.__dict__)
print(Employee.no_of_leaves)