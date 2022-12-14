# TAO CAC CHUC NANG LOP PYTHON
from pythonclass import Python

class Quanlylop:
    listhocvien = []
    
    def create_hoc_vien(self):
        n = int(input("Nhap so hoc vien: "))
        i = 0
        while (i < n):
            i += 1 #Lap vo han
            ten = input("Nhap ten: ")
            tuoi = int(input("Nhap tuoi: "))
            hocvien = Python(ten,tuoi)
            self.listhocvien.append(hocvien)

    def show_hoc_vien(self):
        for i in self.listhocvien:
            print(i.name,i.age,sep=" - ")


    # def update_hoc_vien(self):


    # def delete_hoc_vien(self):



