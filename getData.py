from Tkinter import *
import numpy as np

class Data:
    def __init__(self, objetos, atributos, window):
        self.array = np.empty([objetos, atributos], dtype='a50')
        self.arraySemejanza = np.zeros([objetos, objetos], dtype=np.float)
        self.totalAtributos = atributos
        self.totalObjetos = objetos
        self.obj = 0
        self.atr = 0
        self.textObjeto = StringVar()
        self.textObjeto.set("Objeto: 1")
        self.textAtributo = StringVar()
        self.textAtributo.set("Atributo: 1")
        self.valor = StringVar()
        self.window(window)
    def window(self,window):
        self.root = Toplevel(master=window)
        self.root.resizable(width=False, height=False)
        Label(master=self.root, textvariable=self.textObjeto).grid(row=0, column=0)
        Label(master=self.root, textvariable=self.textAtributo).grid(row=1, column=0)
        Entry(master=self.root, textvariable=self.valor).grid(row=1, column=1, padx=10)
        nextButon = Button(master=self.root, text="Next", command=self.next)
        nextButon.grid(row=2, column=2, padx=10)
        finish = Button(master=self.root, text="Finish", command=self.exit)
        finish.grid(row=2, column=3, padx=10)
        self.root.mainloop()
    def exit(self):
        self.matrizSemejanza()
        print(self.arraySemejanza)
        print(self.array)
        self.root.destroy()
    def next(self):
        flag = False
        if self.atr < self.totalAtributos-1:
            self.atr += 1
        else:
            self.array[self.obj][self.atr] = self.valor.get()
            self.atr = 0
            self.obj += 1
            flag = True
        if self.obj == self.totalObjetos:
            self.exit()
            return
        if flag == False:
            flag = True
            self.array[self.obj][self.atr-1] = self.valor.get()
        self.textAtributo.set("Atributo: "+str(self.atr+1))
        self.textObjeto.set("Objeto: "+str(self.obj+1))
        self.valor.set("")
    def matrizSemejanza(self):
        for i in range(self.totalObjetos):
            j=i
            valor = 0
            for j in range(self.totalObjetos):
                for ii in range(self.totalAtributos):
                    if self.array[i][ii] == self.array[j][ii]:
                        valor += 1
                self.arraySemejanza[j][i] = self.arraySemejanza[i][j] = valor/self.totalAtributos
                print(valor)
                valor = 0