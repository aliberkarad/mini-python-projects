from cProfile import label
from os import stat
import tkinter
from tkinter import *
import gofile
import qrcode
from PIL import Image,ImageTk

windows = tkinter.Tk()
windows.title("Dosya Upload")
windows.geometry("345x100")
windows.resizable(False,False)

LabelMain = Label(windows)
LabelMain.config(text="Dosya Yolunu Belirtiniz",font=("Cascadia Mono","12"))
LabelMain.place(x=15,y=5)

EntryText = Entry(windows)
EntryText.config(bd=1,width=50)
EntryText.place(x=15,y=35)

Label2=Entry(windows)
Label2.config(text="",font=("Cascadia Mono","13"),bd="0",background="green",justify="center",width=27)
Label2.place(x=30,y=100)

def UploadFile():
    global linkt
    file_name = (EntryText.get().replace('\\','/')).replace("\"","")
    o = gofile.uploadFile(file_name)
    linkt = o["downloadPage"]
    windows.geometry(newGeometry="345x150")
    Label2.delete(0,tkinter.END)
    Label2.insert(0,linkt) 
    qrbutton.config(state="active",bd=3)
    
def QR():
    qr = qrcode.make(linkt)
    qr.save("qr.png")    


qrbutton = Button(windows)
qrbutton.config(bd=0,text="QR Code",command=QR,state="disabled")
qrbutton.place(x=75,y=65)

SubmitButton = Button(windows)
SubmitButton.config(bd=2,text="Submit",command=UploadFile)
SubmitButton.place(x=15,y=65)

windows.mainloop()