# TAO CAC CHUC NANG LOP PYTHON
from pythonclass import Python

class Quanlylop:
    listhocvien = []
    
    def create_hoc_vien(self):
        n = int(input("Nhap so hoc vien: "))
        i = 0
        while (i < n):
            i += 1 #Lap vo han
            id = int(input("Nhap id: "))
            ten = input("Nhap ten: ")
            tuoi = int(input("Nhap tuoi: "))
            quequan = input("Nhap que quan: ")
            tienganh = float(input("Nhap diem tieng Anh: "))
            tinhoc = float(input("Nhap diem tin hoc: "))
            hocvien = Python(id,ten,tuoi,quequan,tienganh,tinhoc)
            self.listhocvien.append(hocvien)

    def show_hoc_vien(self):
        for i in self.listhocvien:
            print(i.id,i.name,i.age,sep=" - ")


    # def update_hoc_vien(self):


    # def delete_hoc_vien(self):

hocvien = Quanlylop()
hocvien.create_hoc_vien()
hocvien.show_hoc_vien()







