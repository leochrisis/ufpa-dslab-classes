#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:16:32 2017

@author: Fernando Junior, Italo Ramon
"""

class Aresta():
	rotulo = ''
	peso = 1
	vertices = []

	def __init__(self, vertices = [], peso = 1, rotulo = ''):
		self.vertices = vertices
		self.rotulo = rotulo
		self.peso = peso

	def getVertices(self):
		return self.vertices

	def getRotulo(self):
		return self.rotulo

	def getPeso(self):
		return self.peso

	def getAresta(self):
		return {'vertices': self.vertices,'rotulo': self.rotulo, 'peso': self.peso}

	def setVertices(self, vertices):
		self.vertices = vertices

	def setRotulo(self, rotulo):
		self.rotulo = rotulo

	def setPeso(self, peso):
		self.peso = peso

	def print(self):
		print(self.vertices, end = '')

	def printAll(self):
		print('>> aresta: ',self.vertices, ', peso: ', self.peso, ', rótulo: ', self.rotulo)