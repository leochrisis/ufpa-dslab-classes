#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wes Nov 15 14:44:32 2017

@author: Fernando Junior, Italo Ramon
"""

from grafo import Grafo
from vertice import Vertice
from aresta import Aresta
from copy import copy

def bananasplit(string):
	banana = []
	palavra = ''
	for c in string:
		if not c.isalnum() and c not in ['-', '.', '#']:
			if c in [' ', '\n', '\t'] or palavra != '':
				if palavra != '':
					banana.append(palavra)
					palavra = ''
			if c not in [' ', '\n', '\t']:
				banana.append(c)
		else:
			palavra += c
	if palavra != '':
		banana.append(palavra)
	return banana


def read_vertices(string, grafo):
	rotulo = ''
	peso = 0.0
	estado = -1

	for palavra in bananasplit(string):
		if palavra == 'vertices':
			estado = 0
		elif estado == 0:
			if palavra in [',', ';']:
				estado = 1
			elif palavra == '(':
				estado = 2
			else:
				rotulo += palavra + ' '
		elif estado == 1:
			rotulo = rotulo[:-1]
			grafo.addVertice(rotulo, peso)
			rotulo = ''
			peso = 0.0
			estado = 0
			if palavra != ',':
				rotulo += palavra + ' '
		elif estado == 2:
			if palavra == ')':
				estado = 1
			else:
				peso = float(palavra)
		if palavra == 'arestas':
			break

	return grafo


def read_edges(string, grafo):
	nome = ''
	rotulo = ''
	peso = 1.0
	aresta = ['', '']
	estado = -1

	for palavra in bananasplit(string):
		if palavra == 'arestas':
			estado = 0
		elif estado == 0:
			if palavra == ':':
				nome = nome[:-1]
				aresta[0] = nome; nome = ''; estado = 1
			elif palavra == ';':
				break
			elif palavra[0] == '#':
				break;
			else:
				nome += palavra + ' '
		elif estado == 1:
			if palavra == ',':
				nome = nome[:-1]
				aresta[1] = nome
				estado = 2
			elif palavra == ';':
				nome = nome[:-1]
				aresta[1] = nome
				estado = 7
			elif palavra == '(':
				nome = nome[:-1]
				aresta[1] = nome
				estado = 3
			elif palavra == '"':
				nome = nome[:-1]
				aresta[1] = nome
				estado = 5
			else:
				nome += palavra + ' '
		elif estado == 2:
			rotulo = rotulo[:-1]
			grafo.addAresta(copy(aresta), peso, rotulo)
			rotulo = ''; peso = 1.0; estado = 1; nome = ''
			if palavra != ',':
				nome = palavra + ' '
		elif estado == 3:
			if palavra == ')':
				estado = 4
			else:
				peso = float(palavra)
		elif estado == 4:
			if palavra == '"':
				estado = 5
			elif palavra == ';':
				estado = 7
			elif palavra == ',':
				estado = 2
		elif estado == 5:
			if palavra == '"':
				estado = 6
			else:
				rotulo += palavra + ' '
		elif estado == 6:
			if palavra == ';':
				estado = 7
			elif palavra == ',':
				estado = 2
		elif estado == 7:
			rotulo = rotulo[:-1]
			grafo.addAresta(copy(aresta), peso, rotulo)
			rotulo = ''; peso = 1.0; estado = 0; nome = palavra + ' '; aresta = ['', '']
			if palavra[0] == '#':
				break
	else:
		rotulo = rotulo[:-1]
		grafo.addAresta(copy(aresta), peso, rotulo)
	
	return grafo


def read_type(string, grafo):
	cont = 0
	start = 0

	for palavra in bananasplit(string):
		if cont == 1:
			grafo.setTipo(palavra.lower() == 'true')
		if start == 1:
			cont += 1
		if palavra == 'direcionado':
			start = 1

	return grafo


def validate(string):
	estado = 0
	reservados = [',', '(', ')', ';', ':', '"', '=', 'arestas']
	leitura = ''

	for palavra in bananasplit(string):
		if palavra == 'direcionado':
			estado = 1
		elif estado == 1:
			if palavra == '=':
				estado = 2
			else:
				estado = 'invalid'
		elif estado == 2:
			if palavra.lower() in ['true', 'false']:
				estado = 3
			else:
				estado = 'invalid'
		elif estado == 3:
			if palavra == 'vertices':
				estado = 4
			else:
				estado = 'invalid'
		elif estado == 4:
			if palavra not in reservados:
				estado = 5
			else:
				estado = 'invalid'
		elif estado == 5:
			if palavra == ',':
				estado = 6
			elif palavra == '(':
				estado = 17
			elif palavra == ';':
				estado = 20
			elif palavra in reservados:
				estado = 'invalid'
		elif estado == 6:
			if palavra not in reservados:
				estado = 5
			else:
				estado = 'invalid'
		elif estado == 7:
			if palavra == ';':
				estado = 'final1'
			elif palavra not in reservados:
				estado = 8
			else:
				estado = 'invalid'
		elif estado == 8:
			if palavra == ':':
				estado = 16
			elif palavra in reservados:
				estado = 'invalid'
		elif estado == 9:
			if palavra == ';':
				estado = 'final'
			elif palavra == '(':
				estado = 11
			elif palavra == ',':
				estado = 10
			elif palavra == '"':
				estado = 13
			elif palavra in [':', ')', '=']:
				estado = 'invalid'
		elif estado == 10:
			if palavra not in reservados:
				estado = 9
			else:
				estado = 'invalid'
		elif estado == 11:
			if not isreal(palavra):
				estado = 'invalid'
			else:
				estado = 15
		elif estado == 12:
			if palavra == ';':
				estado = 'final'
			elif palavra == ',':
				estado = 9
			elif palavra == '"':
				estado = 13
			else:
				estado = 'invalid'
		elif estado == 13:
			if palavra == '"':
				estado = 14
			elif palavra in reservados:
				estado = 'invalid'
		elif estado == 14:
			if palavra == ';':
				estado = 'final'
			elif palavra == ',':
				estado = 9
			else:
				estado = 'invalid'
		elif estado == 15:
			if palavra == ')':
				estado = 12
			else:
				estado = 'invalid'
		elif estado == 16:
			if palavra not in reservados:
				estado = 9
			else:
				estado = 'invalid'
		elif estado == 17:
			if not isreal(palavra):
				estado = 'invalid'
			else:
				estado = 18
		elif estado == 18:
			if palavra == ')':
				estado = 19
			else:
				estado = 'invalid'
		elif estado == 19:
			if palavra == ',':
				estado = 6
			elif palavra == ';':
				estado = 20
			else:
				estado = 'invalid'
		elif estado == 20:
			if palavra == 'arestas':
				estado = 7
			else:
				estado = 'invalid'
		elif estado == 'final':
			if palavra[0] == '#':
				break
			elif palavra not in reservados:
				estado = 8
			elif palavra == '#':
				estado = 'final'
				break
			else:
				estado = 'invalid'
		elif estado == 'final1':
			if palavra[0] == '#':
				break
			estado = 'invalid'
		if estado == 'invalid':
			break
		leitura += ' ' + palavra
	if estado in ['final', 'final1']:
		return True
	else:
		print('Erro de sintaxe: ', leitura)
		return False


def read_from_file(nome_arquivo):
	grafo = Grafo(True)

	# ler o arquivo de entrada
	arquivo = open(nome_arquivo)
	string = arquivo.read()
	arquivo.close()

	# validar a entrada
	if validate(string):
		# ler os vértices, o tipo e as arestas
		grafo = read_type(string, grafo)
		grafo = read_vertices(string, grafo)
		grafo = read_edges(string, grafo)
		return grafo
	else:
		return None

def read_from_string(string):
	if validate(string):
		grafo = Grafo(True)
		grafo = read_type(string, grafo)
		grafo = read_vertices(string, grafo)
		grafo = read_edges(string, grafo)
		return grafo
	else:
		return None

def isreal(string):
	try:
		float(string)
		return True
	except ValueError:
		return False
