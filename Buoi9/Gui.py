import tkinter
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry('500x400')

#Label
label = tkinter.Label(giaodien,text="Xin chao",fg="black",bg="white")
label.grid(column=1,row=0)
#Textbox
textbox = tkinter.Entry(giaodien,width=30)
textbox.grid(column=2,row=0)
#Button
button = tkinter.Button(giaodien,text="Click me",fg="black",bg="white")
button.grid(column=2,row=1)

giaodien.mainloop()


