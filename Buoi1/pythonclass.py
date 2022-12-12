#Var
#Array (List, Tuple, Set, Dict)
#Person1 (Doi tuong) - (Thuoc tinh)
#Function
#Class 
# O O P: Object Oriented Programming (Lap trinh huong doi tuong)

class Python0511():
    def __init__(self,name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def eat(self):
        print("An du 3 bua")
    def test(self):
        print("Test tren netacad")


hocvien1 = Python0511("Minh",20,"HN")
hocvien2 = Python0511("Hai",21,"HCM")
hocvien3 = Python0511("Tuan",22,"DN")

print(hocvien1.name)
hocvien1.eat()
hocvien2.eat()
hocvien3.eat()
hocvien1.test()