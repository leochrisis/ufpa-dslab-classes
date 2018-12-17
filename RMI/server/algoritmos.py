#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from grafo import Grafo
from auxiliares import *
infinito = 1e57

def buscaProfundidade(grafo, vertice_inicial, marcados, exploradas, retorno):
	marcados.append(vertice_inicial)
	for item in grafo.getAdjacentes(vertice_inicial):
		if item not in marcados:
			exploradas.append([vertice_inicial,item])
			marcados.append(vertice_inicial)
			marcados, exploradas, retorno = buscaProfundidade(grafo, item, marcados, exploradas, retorno)
		else:
			if not isExplorada(exploradas, [vertice_inicial,item]):
				exploradas.append([vertice_inicial,item])
				retorno.append([vertice_inicial,item])
	return marcados, removeItens(exploradas,retorno), retorno


def buscaLargura(grafo, vertice_inicial):
	marcados = []
	fila = []
	exploradas = []
	retorno = []
	# marcando vertice_inicial
	marcados.append(vertice_inicial)
	# coloca na fila de nohs sendo explorados
	fila.append(vertice_inicial)
	while fila != []:
		v = fila[0]
		del fila[0]
		adjacentes = grafo.getAdjacentes(v) #adjacentes do noh vigente
		for no in adjacentes:
			if no not in marcados:
				exploradas.append([v,no])
				fila.append(no)
				marcados.append(no)
			elif not isExplorada(exploradas, [v,no]):
				exploradas.append([v,no])
				retorno.append([v,no])
	return marcados, removeItens(exploradas,retorno), retorno

	
def prim(g, i):
	grafo = g
	T = [i]
	V = removeItens(grafo.getVertices(), T)
	Arv_Min = []
	
	while V != []:
		K = minFranja(grafo.getFranja(T))
		T += [K[0][1]]
		V = removeItens(V,T)
		Arv_Min.append(K)
		
	return Arv_Min


def kruskal(grafo):
	H = insertionSort(grafo)

	T = Grafo(False)
	T.addVertice(H.getVertices())
	T.addAresta(H.arestas[0].getVertices(), H.arestas[0].getPeso())

	i = 2

	while i < len(H.getArestas()) :
		K = deepcopy(T)
		K.addAresta(H.arestas[i].getVertices())
		_,_,retorno = buscaProfundidade(K,H.arestas[i].getVertices()[0],[],[],[])
		if len(retorno) == 0:
			T.addAresta(H.arestas[i].getVertices(), H.arestas[i].getPeso())
		i += 2

	return removeDuplicadas(T.getArestas())


def dijkstra (grafo, inicial):
	if grafo.hasVertice(inicial):
		
		vertices = []
		arestas = grafo.getArestas()
		
		#criando uma lista dos vertices do grafo, contendo nome do vértice, distancia para chegar nele e a origem
		for i in grafo.vertices:
			if i.getRotulo() == inicial:
				vertices.append([i.getRotulo(), 0, inicial])
			else:
				vertices.append([i.getRotulo(), infinito, ''])

		Q = grafo.getVertices()

		while Q != []:
			
			#funcao que extrai o vertice com menor distância da lista de vértices 
			#e elimina esse elemento da lista
			#a variável u é retornada no formato [vertice, distancia, origem]
			
			u, Q = extrairMin(vertices, Q)
			#a variável v é retornada no formato [vertice, distancia, origem]
			v = selecionaAdj(vertices, grafo.getAdjacentes(u[0]))
					
			for element in v:
				if element[1] > u[1] + pesoAresta(arestas, [u[0],element[0]]):
					element[1] = u[1] + pesoAresta(arestas, [u[0],element[0]])
					element[2] = u[0]
					if element[0] not in Q: 
						Q.append(element[0])      
		return vertices
	else:
		print("Não foi possivel executar a função, pois a aresta dada não está no grafo!")


def bellmanford (grafo, vertice_inicial):
	if grafo.hasVertice(vertice_inicial):
		
		vertices = []
		arestas = grafo.getArestas()
		
		#criando uma lista dos vertices do grafo, contendo nome do vértice, distancia para chegar nele e a origem
		for i in grafo.vertices:
			if i.getRotulo() == vertice_inicial:
				vertices.append([i.getRotulo(), 0, vertice_inicial])
			else:
				vertices.append([i.getRotulo(), infinito, ''])
		
		#É feita n-1 iterações, onde n é o número de vértices.
		for i in range(len(vertices) - 1):
			
			#faz a atualização de valores para cada adjacente de cada vértice
			for u in vertices:
				
				#v é a lista de adjacentes do vértice u
				v = selecionaAdj(vertices, grafo.getAdjacentes(u[0]))
				
				#se a distância até esse vértice for menor que infinito, ele executa
				if u[1] < infinito:
					
					#verifica se deve ser feita a atualização para cada vértice adjacente a u
					for v1 in v:
						if u != v1:
							#print(v)
							if v1[1] > u[1] + pesoAresta(arestas, [u[0],v1[0]]):
								v1[1] = u[1] + pesoAresta(arestas, [u[0],v1[0]])
								v1[2] = u[0]
		
		hasCycle = False
		
		#faz a verificação para saber se tem ciclos
		for u in vertices:
			v = selecionaAdj(vertices, grafo.getAdjacentes(u[0]))
			if u[1] < infinito:
				for v1 in v:
						if u != v1:
							if v1[1] > u[1] + pesoAresta(arestas, [u[0],v1[0]]):
								hasCycle = True
		
		if not hasCycle:
			return vertices
		else:
			return "Sinto muito, mas há ciclos"


def floydWarshall(grafo):
	
	numVertices = grafo.getNumVertices()
	
	matriz = [[infinito for _ in range(numVertices)] for _ in range(numVertices)]
	vertices = grafo.getVertices()
	arestas = grafo.getArestas()
	
	
	for i in range(numVertices):
		for j in range(numVertices):
			if grafo.vertices[i].getRotulo() == grafo.vertices[j].getRotulo():
				matriz[i][j] = 0
			elif grafo.hasAresta([grafo.vertices[i].getRotulo(),grafo.vertices[j].getRotulo()]):
				matriz[i][j] = pesoAresta(arestas, [grafo.vertices[i].getRotulo(),grafo.vertices[j].getRotulo()])
	
	for k in range(numVertices):
		for i in range(numVertices):
			for j in range(numVertices):
				if matriz[i][j] > matriz[i][k] + matriz[k][j]:
					matriz[i][j] = matriz[i][k] + matriz[k][j]
	
	return matriz


def boruvka(grafo):
	floresta = setFlorestaTrivial(grafo.getVertices())
	alcancadas = []
	flora = []
	
	while len(floresta) != 1:
		for subarvore in floresta:
			if not isAlcancada(subarvore, alcancadas):
				menor_aresta = minFranja(grafo.getFranja(vertices(subarvore)))
				#alcancadas.append(subarvore)
				alcancadas += setFlorestaTrivial([menor_aresta[0][1]])
				nova = deepcopy(subarvore)
				nova.append(menor_aresta)
				flora.append(nova)
			else:
				flora.append(subarvore)
		floresta = unificar(flora)
		alcancadas = []
		
	return delFlorestaTrivial(removeDuplicadas(floresta[0]))