from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import image


class MyWindow:

    # ctor- window function :
    def __init__(self, window):
        global imgOpen
        imgOpen = False
        self.mycv = ""
        window.title("My Project")
        label = Label(window, text="MY IMAGE :)", font='Script 45 bold italic', bg='light grey', fg='#C22957')
        label.place(x=150, y=40)
        rs = Label(window, text="©  Sara Ben-David & Sari Amor & Dassi Shnaider", font='Script 20 italic',
                   bg='light grey', fg='#C22957')
        rs.place(x=100, y=515)
        self.buttons()
        self.position()
        self.styleWin()

    # buttons function :
    def buttons(self):
        fontText = tkFont.Font(family="Yu Gothic UI Light", size=15, weight="bold", slant="roman")
        self.openImage = Button(win, text='enter picture', activebackground='white', font=fontText,
                                fg='white', bg='#C22957', command=self.chooseImage, height=-1, width=11)
        self.cutImage = Button(win, text='cut picture', activebackground='white', font=fontText,
                               fg='white', bg='#C22957', command=self.cImg, height=-1, width=11)
        self.enterText = Button(win, text='enter text', activebackground='white', font=fontText,
                                fg='white', bg='#C22957', command=self.EnterText, height=-1, width=11)
        self.shape = Button(win, text='choose shapes', activebackground='white', font=fontText,
                            fg='white', bg='#C22957', command=self.chooseShape, height=-1, width=11)
        self.filters = Button(win, text='to designs', activebackground='white', font=fontText,
                              fg='white', bg='#C22957', command=self.chooseDesigns, height=-1, width=11)
        self.save = Button(win, text='to save', activebackground='white', font=fontText, fg='white',
                           bg='#C22957', command=self.toSave, height=-1, width=11)
        self.exit = Button(win, text='to exit', activebackground='white', font=fontText, fg='white',
                           bg='#C22957', command=self.toExit, height=-1, width=11)

    # position function :
    def position(self):
        win.geometry("550x550+850+100")
        self.openImage.place(x=60, y=180)
        self.cutImage.place(x=210, y=180)
        self.enterText.place(x=360, y=180)
        self.shape.place(x=60, y=260)
        self.filters.place(x=210, y=260)
        self.save.place(x=360, y=260)
        self.exit.place(x=210, y=340)

    # style function :

    @staticmethod
    def styleWin():
        ico = Image.open('icon.png')
        photo = ImageTk.PhotoImage(ico)
        win.wm_iconphoto(False, photo)
        win.configure(bg='light grey')

    # to choose image function :
    def chooseImage(self):
        global imgOpen
        imgOpen = True
        root = Tk()
        root.withdraw()
        file_image = askopenfilename()
        self.mycv = image.MyImage(file_image, "imgWin")

    # to choose filters function :
    def chooseDesigns(self):
        self.checkImg()
        top = Tk()
        top.title("option")
        top.configure(bg='light grey')
        top.geometry("300x300+900+200")
        lbl = Label(top, text="DESIGNS ITEMS", bg='light grey', fg='#C22957')
        lbl.pack()
        listBox = Listbox(top)
        listBox.insert(END, "black & colorful")
        listBox.insert(END, "blurry")
        listBox.insert(END, "colorful")
        listBox.insert(END, "black & white")
        listBox.insert(END, "rotate")
        listBox.insert(END, "light colorful")
        listBox.insert(END, "lines")
        listBox.insert(END, "sharp")
        listBox.insert(END, "border")
        btn = Button(top, text="reset", activebackground='white', font='Helvetica 10 bold italic', fg='white',
                     bg='#C22957', height=2, width=9, command=self.noChange)
        listBox.pack()
        btn.place(x=800, y=200)
        btn.pack()

        # help function-select filters & call to function :
        def getList(event):
            index = listBox.curselection()[0]
            seltext = listBox.get(index)
            if seltext == "black & colorful":
                self.mycv.design1()
            elif seltext == "blurry":
                self.mycv.design2()
            elif seltext == "colorful":
                self.mycv.design3()
            elif seltext == "black & white":
                self.mycv.design4()
            elif seltext == "rotate":
                self.mycv.design5()
            elif seltext == "light colorful":
                self.mycv.design6()
            elif seltext == "lines":
                self.mycv.design7()
            elif seltext == "sharp":
                self.mycv.design8()
            else:
                self.mycv.design9()

        listBox.bind('<ButtonRelease-1>', getList)

    # enter text function :
    def EnterText(self):
        self.checkImg()
        global txt, top
        top = Tk()
        top.title("text")
        top.configure(bg='light grey')
        top.geometry("300x300+900+200")
        text = Label(top, text="enter text:", font='Helvetica 12 italic', bg='light grey', fg='#C22957').place(x=100,
                                                                                                               y=40)
        txt = Entry(top)
        txt.place(x=80, y=70)
        btn = Button(top, text="ok", activebackground='white', font='Helvetica 10 bold italic', fg='white',
                     bg='#C22957', height=2, width=9, command=self.addText)
        btn.place(x=100, y=200)

    # call to help function- put text :
    def addText(self):
        self.mycv.funcText(txt.get())
        top.after(1500,lambda : top.destroy())

    # to choose shapes function :
    def chooseShape(self):
        self.checkImg()
        top = Tk()
        top.title("option")
        top.configure(bg='light grey')
        top.geometry("300x300+900+200")
        lbl = Label(top, text="FILTERS ITEMS", bg='light grey', fg='#C22957')
        listBox = Listbox(top)
        listBox.insert(END, "circle")
        listBox.insert(END, "line")
        listBox.insert(END, "rectangle")
        listBox.insert(END, "triangular")
        listBox.insert(END, "ellipse")
        lbl.pack()
        listBox.pack()

        # help function-select shapes & call to function :
        def getList(event):
            index = listBox.curselection()[0]
            seltext = listBox.get(index)
            if seltext == "circle":
                self.mycv.getType("circle")
            elif seltext == "line":
                self.mycv.getType("line")
            elif seltext == "rectangle":
                self.mycv.getType("rectangle")
            elif seltext == "triangular":
                self.mycv.getType("triangular")
            elif seltext == "ellipse":
                self.mycv.getType("ellipse")

        listBox.bind('<ButtonRelease-1>', getList)

    # function check if the user choose image:
    def checkImg(self):
        if imgOpen is False:
            self.errorImg()

    # function error if the user does'nt choose Image:
    def errorImg(self):
        messagebox.showwarning("error", "You need to choose image")
        self.chooseImage()

    # function show original image:
    def noChange(self):
        self.mycv.ImgNoChange()

    # call to cut image function :
    def cImg(self):
        self.checkImg()
        self.mycv.getType("cut")

    # call to save image function :
    def toSave(self):
        self.checkImg()
        self.mycv.saveImg()

    # to exit function :
    def toExit(self):
        if imgOpen is False:
            exit(self)
        if self.mycv.saveChange("exit") is True:
            self.mycv.saveImg()
            exit(self)
        else:
            exit(self)


"""   start   """

win = Tk()
MyWin = MyWindow(win)
win.mainloop()
