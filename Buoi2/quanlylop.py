#Viết chương trình nhập thông tin của 1 lớp
#Bước 1: Nhập số học viên 
#Bước 2: Điền thông tin từng học viên (Sử dụng input)
#Bước 3: Hiển thị danh sách sau khi nhập

#Hiển thị danh sách
#Thêm thành viên
#Sửa thành viên
#Xoá thành viên

# C R U D
#Create
#Read
#Update
#Delete

#Class -> hocvien -> (name, age)

class Python:
    def __init__(self,name, age):
        self.name = name
        self.age = age
# #hardcode   
# hocvien1 = Python("Minh",20)
# hocvien2 = Python("Hai",22)

#Handling

#Create
n = int(input("Nhap so hoc vien: "))
i = 0
listhocvien = []
while (i < n):
    i += 1 #Lap vo han
    ten = input("Nhap ten: ")
    tuoi = int(input("Nhap tuoi: "))
    hocvien = Python(ten,tuoi)
    listhocvien.append(hocvien)

#Read
for i in listhocvien:
    print(i.name,i.age,sep=" - ")

#Update




#Delete


#







