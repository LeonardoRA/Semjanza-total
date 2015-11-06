from Tkinter import *
import getData

class setAtributs:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.numObj = IntVar()
        self.numAtr = IntVar()
        Label(master=self.root, text="Numero de Objetos").grid(row=0, column=0)
        Entry(master=self.root, textvariable=self.numObj).grid(row=0, column=1)
        Label(master=self.root, text="Numero de Atributos").grid(row=1, column=0)
        Entry(master=self.root, textvariable=self.numAtr).grid(row=1, column=1)
        Button(master=self.root, text="OK", command=self.openWindow).grid(row=0, column=2, rowspan=2, padx=10)
        self.root.mainloop()
    def openWindow(self):
        getData.Data(self.numObj.get(), self.numAtr.get(), self.root)
if "__main__" == __name__:
    setAtributs()