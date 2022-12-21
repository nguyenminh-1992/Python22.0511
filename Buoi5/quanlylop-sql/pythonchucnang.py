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


get_data2()
    





ketnoi.close()