import json
import os

class Empresa():
	"""Clase para el microservicio Noticiario"""
	#Método para inicializar la clase
	def __init__(self):
		self.__noticiai=0
		self.nombre=""
		self.calificacion={}

	def crearEmpresa(self,nombre):
		self.nombre=nombre
		self.calificacion[nombre]={}
		if(nombre):
			return True
		else:
			return False

	def listarCalificaciones(self,nombre):
		for empresa in calificacion:
			for user in empresa:
   				print user, ":", calificacion[empresa][user]
		return True

	def crearCalificacion(self,usuario,nota):
		if(calificacion[empresa][usuario]!=None):
			calificacion[empresa][usuario]=nota
			return True
		return False

	def borrarCalificacion(self,usuario):
		if(calificacion[empresa][usuario]!=None):
			del calificacion[empresa][usuario]
			return True
		return False

	def hacerRanking(self):
		for empresa in calificacion:
			for user in empresa:
   				cali=cali+float(calificacion[empresa][user])
			print empresa,":",cali
		return True