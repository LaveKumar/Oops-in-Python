class A:
    classvar1="I am a class avriable in class A"
    def __init__(self):
        self.var1="I am inside class A's Instructor"
        self.classvar1="Instance var in class a"
        self.special="Special"

class B(A):

    classvar1="I am in class B"
    def __init__(self):
        super().__init__()
        self.var1="I am inside class A's Instructor"
        self.classvar1="Instance var in class a"
        print(super().classvar1)



a=A()
b=B()
print(b.special,b.var1,b.classvar1)