import pickle

# cars = ["Audi","BMW","Maruti Suzuki","Farari"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

#pickle.loads=?
