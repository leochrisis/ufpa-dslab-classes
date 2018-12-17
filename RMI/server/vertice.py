#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:04:32 2017

@author: Fernando Junior, Italo Ramon
"""

class Vertice():
	rotulo = ''
	peso = 0

	def __init__(self, rotulo='', peso = 0):
		self.rotulo = rotulo
		self.peso = peso

	def getRotulo(self):
		return self.rotulo

	def getPeso(self):
		return self.peso

	def getVertice(self):
		return {'rotulo': self.rotulo, 'peso': self.peso}

	def setRotulo(self, rotulo):
		self.rotulo = rotulo

	def setPeso(self, peso):
		self.peso = peso

	def print(self):
		print(self.rotulo, end = '')

	def printAll(self):
		print('>> vértice:', self.rotulo, ", peso: ", self.peso)