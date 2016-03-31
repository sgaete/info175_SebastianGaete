# -*- coding: utf-8 -*-
from Tkinter import *
import string
import encript1
import encript2

class Encrypter():
	def __init__(self, master):
		frame = Frame(master,padx=10,pady=10)
		frame.grid(row=0)
		
		
		self.label01 = Label(frame, font="Times 12 bold" , text="Ingrese el texto a encriptar:")
		self.label01.grid(row=0, column=0)
		
		self.entrada = Text(frame, width= 40,height=6,bd=2)
		self.entrada.grid(row=1,column=0,sticky='EW',pady=10)
		
		self.label02 = Label(frame, font="Times 12 bold" , text=u"Seleccionar el método de encriptación:")
		self.label02.grid(row=2, column=0, sticky='EW')
		
		self.v = IntVar()
		self.v.set(1)
		self.rboton01 = Radiobutton(frame, text=u"Encriptado Cesar", variable=self.v, value=1 )
		self.rboton01.grid(row=3,sticky="W",pady=10)
		self.rboton02 = Radiobutton(frame, text=u"Encriptado Cenit Polar", variable=self.v, value=2)
		self.rboton02.grid(row=3,sticky="E",pady=10)

		self.label03 = Label(frame, text=u"Especifíque el salto para la encriptación cesar:")
		self.label03.grid(row=4, sticky='W')

		self.entrada2 = Entry(frame, bd=2,width=10,justify="right")
		self.entrada2.insert(0,'0')
		self.entrada2.grid(row=4,sticky='E')

		self.label04 = Label(frame, font="Times 12 bold", text=u"Resultado:")
		self.label04.grid(row=5, sticky='W', pady=10)

		self.a = StringVar()

		self.labelres =Label(frame,text=u"",height=6, textvariable=self.a)
		self.labelres.grid(row=6,sticky="EW")

		self.encr = Button(frame,text="Encriptar", command=self.encryptIt)
		self.encr.grid(row=7,sticky="EW",pady=10)

		self.limpia = Button(frame,text="Limpiar",command=self.limpiaCampos)
		self.limpia.grid(row=8,sticky="EW")

	def limpiaCampos(self):
		self.entrada.delete(1.0, END)
		self.entrada2.delete(0,END)
		self.entrada2.insert(0,'0')
		self.a.set("")


	def encryptIt(self):
		if(self.v.get()==1):
			self.labelres.config(text="")
   			frase = self.entrada.get(1.0,END)
	   		salto = int(self.entrada2.get())

	   		frase_cesar = encript1.encryptCesar(frase, salto)
	   		self.a.set(frase_cesar)

	   			
	   	else:
			self.labelres.config(text="")
   			frase = self.entrada.get(1.0,END)

	   		frase_cp = encript2.encryptCP(frase)
	   		self.a.set(frase_cp)	   		



if __name__ == '__main__':
	root = Tk()
	root.title('Vamoh a enccripatrlo')
	root.geometry('370x470')
	root.resizable(width=False,height=False)
	Encrypter(root)
	root.mainloop() 
