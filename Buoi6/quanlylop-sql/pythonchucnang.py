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
    id = 3
    dulieu.execute(sql,(id,))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def get_data_byid_andage(id,age):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s AND age = %s"
    # id = 3
    # age = 22
    dulieu.execute(sql,(id,age))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def create_data():
    sql = "INSERT INTO `Hocvien`(Id,`Name`,Age, Country	, English, Information)VALUES (5, 'Nguyen Van E' , 23, 'Da Nang',  3 , 4 )"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da them thanh cong")

def update_data():
    sql = "UPDATE Quan_ly_hoc_vien.Hocvien SET Age = 25 WHERE Id = 5"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da cap nhat thanh cong")

# get_data2()
# print("-------")
# get_data_byid()
# get_data_byid2()
# get_data_byid_andage(3,22)
# create_data()
update_data()
    





ketnoi.close()