import tkinter
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry('500x400')

#Label
label1 = tkinter.Label(giaodien,text="Tinh tong 2 so",fg="black")
label1.grid(column=2,row=0)

label2 = tkinter.Label(giaodien,text="Nhap so thu nhat",fg="black",bg="white")
label2.grid(column=1,row=1)

label3 = tkinter.Label(giaodien,text="Nhap so thu hai",fg="black",bg="white")
label3.grid(column=1,row=2)

label4 = tkinter.Label(giaodien,text="Ket qua",fg="black",bg="white")
label4.grid(column=1,row=3)
#Textbox
textbox1 = tkinter.Entry(giaodien,width=30)
textbox1.grid(column=2,row=1)

textbox2 = tkinter.Entry(giaodien,width=30)
textbox2.grid(column=2,row=2)

textbox3 = tkinter.Entry(giaodien,width=30)
textbox3.grid(column=2,row=3)
#Button
button = tkinter.Button(giaodien,text="Click me",fg="black",bg="white")
button.grid(column=2,row=4)

giaodien.mainloop()


