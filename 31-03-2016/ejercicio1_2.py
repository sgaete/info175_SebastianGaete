# -*- coding: utf-8 -*-
class auto(object):
	def __init__(self, kilo, bencina, rendimiento):
		self.kilo = kilo
		self.bencina = bencina
		self.rendimiento = rendimiento
		self.encendido = False

	def encender(self):
		self.encendido = True

	def apagar(self):
		self.encendido = False

	def mover(self):
		if self.bencina >=1/self.rendimiento  and self.encendido:
			print "mover 1k"
			self.bencina = self.bencina-(1/self.rendimiento)
			self.kilo += 1

	def obtener_kilo(self):
		return self.kilo

	def obtener_bencina(self):
		return self.bencina

	def cargar_bencina(self,cantidad):
		if self.encendido:
			self.apagar()
		self.bencina += cantidad

class camion(auto):
	def __init__(self, peso, ruedas):
		self.peso = float(peso)
		self.ruedas = int(ruedas)
		self.acoplados={"ruedas":0,"peso":0.0,"carga":""}

	def agregar_acoplado(self, ruedas, peso, carga):
		self.acoplados["ruedas"]=ruedas
		self.acoplados["peso"]=peso
		self.acoplados["carga"]=carga

	def quitar_acoplado(self):
		self.acoplados["ruedas"]=0
		self.acoplados["peso"]=0.0
		self.acoplados["carga"]=""

	def obtener_acoplado(self):
		return self.acoplados

	def obtener_ruedas(self):
		return self.ruedas

	def obtener_peso(self):
		return self.peso