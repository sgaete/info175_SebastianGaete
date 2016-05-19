# -*- coding: utf-8 -*-
lista = []
boolean = True
while(boolean):
	pal = raw_input("Ingrese palabra:  ")
	if (len(pal) == 0):
		boolean = False
	else:
		lista.append(pal)
	for x in range(len(lista)):
		lista[x] = lista[x].upper()	
print(lista)