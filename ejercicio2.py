# -*- coding: utf-8 -*-

if __name__ == "__main__":
	pal = raw_input("ingrese palabras separadas con comas:  ")
	lista = []
	lista = pal.split(",")
	print "Lista desordenada"
	print (lista)
	lista.sort()
	print "Lista ordenada"
	print(lista)