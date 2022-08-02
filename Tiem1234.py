# n= int(input("Enter n \n"))
# i=1
# while i<11:
#     i+=1
#     print(n,'x', i, '=', n*i)

import time
initial = time.time()
# print(initial)
k=0
while(k<4):
    print("This is Lucky bhai")
    time.sleep(6)
    k+=1
print("While loop ran in ", time.time() - initial, "Seconds")
initial2 = time.time()
for i in range(4):
    print("This is Lucky bhai")
print("for loop ran in ", time.time() - initial2, "Seconds")

# localtime = time.asctime(time.localtime(time.time()))  # gives actual time going on
# print(localtime)