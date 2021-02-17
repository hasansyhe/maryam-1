from tkinter import *
from tkinter import ttk
import os
from services import images
from ttkthemes import ThemedTk
from tkinter import messagebox

class splash():
    def __init__():
        pass
class select():
    def __init__(self):

        self.meryem = ThemedTk(theme="breeze")
        self.meryem.title("SELECT DEVICE")

        path = os.getcwd()
        image_path = f"{path}/img/b.jpg"
        png_label = images.image_make(path_=image_path, sw_=500, sh_=100)

        title_bar = Label(self.meryem, bg="#fff", image=png_label)
        title_bar.pack(fill=X, expand=True)

        framebody = ttk.Frame(self.meryem)
        framebody.pack(fill=BOTH, expand=True)

        # fileds combox
        labelBox = ttk.LabelFrame(framebody, text="Select Device Model")
        labelBox.pack(fill=X, expand=True, pady=10, padx=10)
        comboxVar = StringVar()
        combox = ttk.Combobox(labelBox, textvariable=comboxVar)
        combox["values"] = ('SM-I8190N')
        combox.pack(fill=X, expand=True, padx=10, pady=10)

        # fileds combox
        labelBox_2 = ttk.LabelFrame(framebody, text="Select Android Version")
        labelBox_2.pack(fill=X, expand=True, pady=10, padx=10)
        comboxVar_2 = StringVar()
        combox_2 = ttk.Combobox(labelBox_2, textvariable=comboxVar_2)
        combox_2["values"] = ('Jelly Bean 4.1','Jelly Bean 4.2','KitKat 4.4','Lolipop 5.0','Marshmallow 6.0','Nougat 7.0','Oreo 8.0')
        combox_2.pack(fill=X, expand=True, padx=10, pady=10)

        butlabel = ttk.Label(framebody)
        butlabel.pack(fill=X, expand=True, pady=10, padx=10)

        but1 = ttk.Button(butlabel, text="Next", width=10)
        but1.pack(side=LEFT, padx=10, pady=10)
        # function
        def exit_():
            msj = messagebox.askyesno("Exit", "Do you want exit")
            if msj == True:
                self.meryem.quit()
            else:
                print ("Cancel Process")
        but2 = ttk.Button(butlabel, text="Exit", width=10, command=exit_)
        but2.pack(side=LEFT, padx=10, pady=10)
        but3 = ttk.Button(butlabel, text="Help", width=10)
        but3.pack(side=LEFT, padx=10, pady=10)

        self.meryem.mainloop()

class sflma():
    def __init__(self):
        self.lara = Tk()
        self.lara.title("MERYEM TOOL")
        self.lara.geometry("500x500")
    def menu(self):
        menubody = Menu(self.lara)
        self.lara.config(menu=menubody)

        open_menu = Menu(menubody)
        menubody.add_cascade(menu=open_menu, label="Open")
        
    def run(self):
        self.lara.mainloop()


if __name__ == '__main__':
    select()