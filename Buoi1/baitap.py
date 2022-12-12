#Viết chương trình nhập thông tin của 1 lớp
#Bước 1: Nhập số học viên 
#Bước 2: Điền thông tin từng học viên (Sử dụng input)
#Bước 3: Hiển thị danh sách sau khi nhập


#Gợi ý: Tạo Class
#Khai báo List
#Dùng For để in ra


class Python:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# hocvien1 = Python("Minh",20)
n = int(input("Nhap so luong hoc vien: "))
j = 1
listhocvien = []
while (j <= n):
    print("Thong tin hoc vien thu" + j)
    name1 = input("Nhap ten: ")
    age1 = int(input("Nhap tuoi: "))
    j += 1
    listhocvien.append(Python(name1,age1))

for i in listhocvien:
    print(i.name,i.age, sep=" - ")