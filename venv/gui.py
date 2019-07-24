from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from pathlib import Path
import file1,file2,file3,file4
import os
import cv2


class GetImage:

    def press(self, x):
        self.n = x
        self.display_image.set(self.n)
    def onGo(self):
        self.showOriginalImage(self.n)
    def command1(self):
        file2.rotate(self.n)

    def command2(self):
        file3.rotate(self.n)

    def command3(self):
        file1.rotate(self.n)
    def command4(self):
        file4.rotate(self.n)


    def askForImage(self):
        window = Tk()
        window.title("Image Rotation")
        window.geometry("490x450")
        window.resizable(0, 0)

        back = Frame(master=window, bg='turquoise')
        back.grid(row=0, column=0, )
        back.pack_propagate(0)
        back.pack(fill=BOTH, expand=1)

        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        labelImage = Label(master=back, text="Click on  the name of the Image", bg="turquoise", font=("Arial Bold", 25))
        labelImage.pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        self.display_image = StringVar()
        display = Label(master=back, textvariable=self.display_image, bg="white", font=30, width=15).pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        BtnImage1 = Button(master=back, text="teddybear.jpg", bg="black", fg="white", font=(15), height=1, width=12,
                           command=lambda: self.press("teddybear.jpg")).pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        BtnImage2 = Button(master=back, text="ibesis.jpg", bg="black", fg="white", font=(15), height=1, width=12,
                           command=lambda: self.press("ibesis.jpg")).pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        BtnImage3 = Button(master=back, text="flowers.jpg", bg="black", fg="white", font=(15), height=1, width=12,
                           command=lambda: self.press("flowers.jpg")).pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        BtnImage4 = Button(master=back, text="iphone.jpg", bg="black", fg="white", font=(15), height=1, width=12,
                           command=lambda: self.press("iphone.jpg")).pack()
        labelEmpty = Label(master=back, text=" ", font=10, bg="turquoise")
        labelEmpty.pack()

        BtnGo = Button(master=back, text="Go", bg="green", fg="black", font=(15), height=1, width=6,
                       command=lambda: self.onGo()).pack()
        window.mainloop()
    def showOriginalImage(self,imageName):
        # path = Path(imageName)
        # print(path)
        root = Toplevel()
        root.title("Image Rotation")
        root.geometry("900x900")
        root.resizable(0, 0)

        back = Frame(master=root, bg='turquoise')
        back.grid(row=0,column=0,)
        back.pack_propagate(0)
        back.pack(fill=BOTH, expand=1)

        img=ImageTk.PhotoImage(Image.open(imageName,'r'))
        panel = Label(master=back, image = img ,bg="turquoise")
        panel.pack(side = "top", fill = "both", expand = 1)
        labelEmpty = Label(master=back, text=" ", font=30, bg="turquoise").grid(row=1, column=0)

        labelEmpty = Label(master=back, text=" ", font=30, bg="turquoise").grid(row=2, column=0)
        BtnRotate90=Button(master=back,text="Rotate Anticlockwise", bg="black", fg="white",font=(15),command=lambda :self.command3()).grid(row=2,column=1)
        labelEmpty=Label(master=back,text=" ",font=30,bg="turquoise").grid(row=2,column=2)
        BtnRotate90clock=Button(master=back,text="Rotate Clockwise",  bg="black", fg="white",font=(15),command=lambda :self.command1()).grid(row=2,column=3)
        labelEmpty=Label(master=back,text=" ",font=30,bg="turquoise").grid(row=2,column=4)
        BtnRotate180=Button(master=back,text="Rotate up-side-Down" , bg="black", fg="white",font=(15),command=lambda :self.command2() ).grid(row=2,column=5)
        labelEmpty = Label(master=back, text=" ", font=30, bg="turquoise").grid(row=2, column=6)
        BtnBlackWhite = Button(master=back, text="Black n White", bg="black", fg="white", font=(15),
                              command=lambda: self.command4()).grid(row=2, column=7)

        root.mainloop()

gRef=GetImage()
gRef.askForImage()

