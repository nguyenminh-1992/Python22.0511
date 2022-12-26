import pythonclass

#Ket noi giua MySQL va Python
ketnoi = pythonclass.getConnection()
#print(ketnoi)

#C R U D
dulieu = ketnoi.cursor()

def get_data():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
    
def get_data2():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()

def get_data_byid():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 2")
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def get_data_byid2():
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
    id = int(input("Nhap: "))
    dulieu.execute(sql,(id,))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)


get_data2()
print("-------")
# get_data_byid()
get_data_byid2()
    





ketnoi.close()