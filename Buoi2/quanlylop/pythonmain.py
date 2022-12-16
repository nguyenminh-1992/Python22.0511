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
        print("Hello")
        # hocvien.create_hoc_vien()
    elif (nhap == 2):
        print("Hello 2")
        # hocvien.show_hoc_vien()
    else:
        break

# elif (nhap == 3):

# elif (nhap == 4):

# else:
#     print("Nhap sai vui long nhap lai")