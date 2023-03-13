#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text='soubor')
        self.fileFrame.pack(padx=5, pady=5)
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(anchor='w')
        self.fileBtn = tk.Button(self.fileFrame, text='...')
        self.fileBtn.pack(anchor='e')
        self.dataformatVar = tk.IntVar(value='RADEK')
        self.radkyRBtn = tk.Radiobutton(self.fileFrame, text='data jsou v řádcích', variable = self.dataformatVar, value = 'RADEK')
        self.radkyRBtn.pack(anchor='w')
        self.sloupceRBtn = tk.Radiobutton(self.fileFrame, text='data jsou ve sloupcích', variable = self.dataformatVar, value='SLOUPEC')
        self.sloupceRBtn.pack(anchor='w')


        self.grafFrame = tk.LabelFrame(self, text='Graf')
        self.grafFrame.pack()
        tk.Label(self.grafFrame, text='Titulek').grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0,column=1)

        tk.Label(self.grafFrame, text='Popisek X').grid(row=1, column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1,column=1)
        tk.Label(self.grafFrame, text='Popisek Y').grid(row=2, column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2,column=1)
        tk.Label(self.grafFrame, text='Mřížka').grid(row=3, column=0)
        self.GridChck = tk.Checkbutton(self.grafFrame)
        self.GridChck.grid(row=3,column=1, sticky='w')

        
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()