#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo com as funções auxiliares aos algoritmos de operações nos grafos

from copy import deepcopy
from grafo import Grafo

def isExplorada(exploradas, aresta):
	if [aresta[0],aresta[1]] in exploradas: return True
	if [aresta[1],aresta[0]] in exploradas: return True
	return False


def insertionSort(G):
	Grafo = deepcopy(G)

	arestas = Grafo.getObjectArestas()

	for i in range(1,len(arestas)):
		x = arestas[i]
		j = i-1
		while j>=0 and x.getPeso() < arestas[j].getPeso():
			Grafo.arestas[j+1] = Grafo.arestas[j]
			j=j-1
		Grafo.arestas[j+1] = x

	return Grafo


def removeItens(total, praRemover):
	temp = []

	for element in total:
		temp.append(element)

	for element in temp:
		if element in praRemover:
			del total[total.index(element)]

	return total


def minFranja(Franjas):
	if Franjas != []:
		min = Franjas[0]
		for t in Franjas:
			if t[1] < min[1]:
				min = t
		return min
	else:
		print("Não existem franjas")


def extrairMin(lista, Q):
	for i in lista:
		if i[0] in Q:
			u = i;
			break

	q = []

	for element in lista:
		if element[0] in Q:
			q.append(element[0])
		if element[1] < u[1] and element[0] in Q:
			u = element

	del q[q.index(u[0])]

	return u, q


# lista contém elementos no formato [vertice, distancia, origem]
# lista2 contém somente elementos adjacentes de um dado vertice
# Deve ser retornado os correspondentes da lista na lista2
# Retorna uma lista de vértices adjacentes aos vértices 'lista'
# no formato [vertice, distancia, origem]
def selecionaAdj(lista, lista2):
	retorno = []
	
	for i in lista2:
		for j in lista:
			if i == j[0]:
				retorno.append(j)
				continue
	return retorno;
	

def pesoAresta(lista, aresta):
	for element in lista:
		if aresta == element[0]:
			return element[1]


''' Seja x uma máscara tal que x = [[[A1, B1], p1], [[A2, B2], p2], ..., [[An, Bn], pn]], 
onde Ai, Bi são componentes de uma aresta e pi são os seus respectivos pesos. '''

# Retorna os vertices de uma subárvore da forma x
def vertices(subarvore):
	vertices = []
	for aresta in subarvore:
		if aresta[0][0] not in vertices:
			vertices.append(aresta[0][0])
		if aresta[0][1] not in vertices:
			vertices.append(aresta[0][1])
	return vertices


''' 'subarvore' e 'alcancadas' são listas na forma x. 'subarvore' representa uma subarvore
qualquer e 'alcancadas' representa as arestas de subárvores que já foram alcancadas.'''
def isAlcancada(subarvore, alcancadas):
	# Captura os vértices da subárvore
	v = vertices(subarvore)
	# Verifica se algum dos vértices da subárvore foi alcancado
	for aresta in alcancadas:
		if aresta[0][1] in v:
			return True
	return False


# Unifica uma floresta onde há subárvores adjacentes
def unificar(floresta):
	flora = deepcopy(floresta)
	match = False
	i = 0
	while i < len(flora):
		j = i + 1
		while j < len(flora):
			if areSobrepostas(flora[i], flora[j]):
				match = True
				subway = flora[i]
				subway += flora[j]
				flora.append(subway)
				flora.remove(flora[j])
				flora.remove(flora[i])
				i = 0
				break
			j += 1
		if not match:
			i += 1
		else:
			match = False
	return flora


# Verifica se duas subárvores compartilham um mesmo vértice
def areSobrepostas(subarvore1, subarvore2):
	vert1 = vertices(subarvore1)
	vert2 = vertices(subarvore2)
	for vertice in vert1:
		if vertice in vert2:
			return True
	return False


# Transforma um conjunto de vértices para o formato x
#def setFlorestaInicial(vertices):
def setFlorestaTrivial(vertices):
	floresta = []
	for v in vertices:
		floresta.append([[[v, v], 0]])
	return floresta


#def delFlorestaInicial(subarvore):
def delFlorestaTrivial(subarvore):
	lista = []
	for aresta in subarvore:
		if not aresta[0][0] == aresta[0][1]:
			lista.append(aresta)
	return lista


# Retorna a soma de uma lista de arestas no formato x
def somaPesos(arestas):
	soma = 0
	for a in arestas:
		soma += a[1]
	return soma


# Remove arestas duplicadas em uma lista de arestas no formato x
def removeDuplicadas(arestas):
	lista = []
	for a in arestas:
		if a not in lista:
			copia = deepcopy(a)
			copia[0].reverse()
			if copia not in lista:
				lista.append(a)
	return lista