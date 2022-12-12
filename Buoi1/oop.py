class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print("Person sleep")
    def eat(self):
        print("Person eat")

class BKCAD():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print("BKACAD study")
    def eat(self):
        print("BKACAD eat")

class Python0511(Person,BKCAD):  #Kế thừa
    def __init__(self,name,age):
        self.name = name
        self.age = age

hocvien1 = Python0511("Minh",20)
hocvien1.sleep()
hocvien1.eat()
    