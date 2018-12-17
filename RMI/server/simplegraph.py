import Pyro4
from grafo import Grafo
from inputer import Inputer
from algoritmos import *

@Pyro4.expose
@Pyro4.behavior(instance_mode = 'single')

class SimpleGraph():
	def __init__(self):
		self.reset_graph()

	def add_vertex(self, vertex):
		self.vertices.append(vertex)

	def add_edge(self, edge):
		if type(edge) == list:
			self.edges.append(edge)

	def get_edges(self):
		return self.edges

	def get_vertices(self):
		return self.vertices

	def get_str(self):
		return self.__str__()

	def reset_graph(self):
		self.vertices = []
		self.edges = []

	def create_graph(self, string):
		self.reset_graph()
		creator = Inputer()
		self.graph = creator.read_from_string(string)
		for vertex in self.graph.getVertices():
			self.add_vertex(vertex)
		for edge in self.graph.getArestas():
			self.add_edge(edge[0])

	def depth_first_search(self, initial):
		if self.graph:
			return buscaProfundidade(self.graph, initial, [], [], [])

	def prim(self, initial):
		if self.graph:
			return prim(self.graph, initial)

	def dijkstra(self, initial):
		if self.graph:
			return dijkstra(self.graph, initial)

	def boruvka(self):
		if self.graph:
			return boruvka(self.graph)

	def __str__(self):
		string = 'vertices: {ver}\n'.format(ver = str(self.vertices))
		string += 'edges:\n'
		for edge in self.edges:
			string += str(edge) + '\n'
		return string

	def show(self):
		print(self)