#THUC THI CAC CHUC NANG

#MENU

from pythonchucnang import *

# hocvien = Quanlylop()

while(True):
    print("-------------------------------")
    print("1. Them hoc vien")
    print("2. Hien thi hoc vien")
    print("3. Sua thong tin hoc vien")
    print("4. Xoa thong tin hoc vien")
    print("5. Sap xep thong tin hoc vien")
    print("-------------------------------")

    print("Moi ban chon chuc nang")

    nhap = int(input("Chon chuc nang: "))
    if (nhap == 1):
        get_data()
    elif (nhap == 2):
        age = input("Nhap tuoi: ")
        id = input("Nhap id: ")
        update_data(age,id)
    elif (nhap ==3):
        # id1 = int(input("Nhap id muon sua: "))
        update_data()
        print("Da sua thanh cong")
    elif (nhap ==4):
        # id2 = int(input("Nhap id muon xoa: "))
        delete_data()
        print("Da xoa thanh cong")
    elif (nhap ==5):
        print("  ")
        # hocvien.sapxep_hoc_vien()
        # hocvien.show_hoc_vien()
    else:
        break

# elif (nhap == 3):

# elif (nhap == 4):

# else:
#     print("Nhap sai vui long nhap lai")