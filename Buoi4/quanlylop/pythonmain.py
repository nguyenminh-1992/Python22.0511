#THUC THI CAC CHUC NANG

#MENU

from pythonchucnang import *

hocvien = Quanlylop()

while(True):
    print("-------------------------------")
    print("1. Them hoc vien")
    print("2. Hien thi hoc vien")
    print("3. Sua thong tin hoc vien")
    print("4. Xoa thong tin hoc vien")
    print("-------------------------------")

    print("Moi ban chon chuc nang")

    nhap = int(input("Chon chuc nang: "))
    if (nhap == 1):
        hocvien.create_hoc_vien()
    elif (nhap == 2):
        hocvien.show_hoc_vien()
    elif (nhap ==3):
        id1 = int(input("Nhap id muon sua: "))
        hocvien.update_hoc_vien(id1)
        print("Da sua thanh cong")
    elif (nhap ==4):
        id2 = int(input("Nhap id muon xoa: "))
        hocvien.delete_hoc_vien(id2)
        print("Da xoa thanh cong")
    else:
        break

# elif (nhap == 3):

# elif (nhap == 4):

# else:
#     print("Nhap sai vui long nhap lai")