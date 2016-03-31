# -*- coding: utf-8 -*-
import time
class persona(object):
	def __init__(self, rut, nombre, fechan, genero):
		self.rut = rut
		self.nombre = nombre
		# fecha se toma como(año,mes,dia)
		self.fechan = fechan
		self.genero = genero
	def obtener_edad(self):
		localtime = time.localtime(time.time())
		agno = localtime[0]-self.fechan[0]
		mes = localtime[1]-self.fechan[1]
		dia = localtime[2]-self.fechan[2]
		if mes >= 0 and dia >= 0:
			return agno
		else:
			return agno-1
sebastian = persona(1123412,"sebastian",[1994,01,16],"Male")
print sebastian.obtener_edad()