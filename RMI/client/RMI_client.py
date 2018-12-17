# -*- coding: utf-8 -*-
import Pyro4
import sys
Pyro4.config.DETAILED_TRACEBACK=True;
sys.excepthook = Pyro4.util.excepthook

# Setting a function to read files
def read_file(file_name):
	file = open(file_name)
	return file.read()

# Importing the file that contains the graph
string = read_file('input.in')

# get a Pyro proxy to the SimpleGraph object
graph = Pyro4.Proxy("PYRONAME:proxy.graph")

print('Input is in <string>')
print('SimpleGraph is in <graph>')