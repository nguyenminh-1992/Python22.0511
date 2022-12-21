# TAO CAC CHUC NANG LOP PYTHON
from pythonclass import Python

class Quanlylop:
    listhocvien = []

    # [A,C,D,E,F,G]
    
    def create_hoc_vien(self):
        n = int(input("Nhap so hoc vien: "))
        i = 0
        while (i < n):
            i += 1 #Lap vo han
            # id = int(input("Nhap id: "))  #Khong nhap tay, tu dong set (1,2,3,4,...)
            id = self.listhocvien.__len__() + 1
            ten = input("Nhap ten: ")
            tuoi = int(input("Nhap tuoi: "))
            quequan = input("Nhap que quan: ")         
            tienganh = float(input("Nhap diem tieng Anh: "))
            tinhoc = float(input("Nhap diem tin hoc: "))
            hocvien = Python(id,ten,tuoi,quequan,tienganh,tinhoc)
            
            hocvien.diemtrungbinh = float((tienganh + tinhoc)/2)
            if hocvien.diemtrungbinh <4 :
                hocvien.hocluc = "Yeu"      
            elif hocvien.diemtrungbinh < 7:
                hocvien.hocluc = "Kha"
            else:
                hocvien.hocluc = "Gioi"   
                        
            self.listhocvien.append(hocvien)

    def show_hoc_vien(self):
        print("{:<5}{:<15}{:<5}{:<10}{:<10}{:<15}{:<15}{:<10}".format("Id","Ten","Tuoi","Que quan","Diem tin","Diem tieng Anh", "Trung binh", "Hoc luc"))
        for i in self.listhocvien:
            print("{:<5}{:<15}{:<5}{:<10}{:<10}{:<15}{:<15}{:<10}".format(i.id,i.name,i.age,i.country,i.english,i.information,i.diemtrungbinh,i.hocluc,sep=" - "))


    def update_hoc_vien(self,id1):
        for i in self.listhocvien:
            if(i.id == id1):
                name = input("Nhap ten: ")
                tuoi = int(input("Nhap tuoi: "))
                i.name = name
                i.age = tuoi

    def delete_hoc_vien(self,id1):
        for i in self.listhocvien:
            if(i.id == id1):
                self.listhocvien.remove(i)

    def sapxep_hoc_vien(self):
        self.listhocvien.sort(key=lambda x:x.name, reverse=False)
        




# hocvien = Quanlylop()
# hocvien.create_hoc_vien()
# hocvien.show_hoc_vien()







