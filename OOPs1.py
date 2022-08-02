# Class   -> Template
# Object  ->Instance of Class
#
# DRY     ->Do not repeat yourshelf


class student:
    pass

harry=student()
larry=student()
harry.name="Lucky"
harry.std="b.tech"
harry.section='B'
larry.subjects=["Hindi", "English", "maths","s.s.t"]
print(harry.name,larry.subjects)
