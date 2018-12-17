# -*- coding: utf-8 -*-
import Pyro4
import sys
Pyro4.config.DETAILED_TRACEBACK=True;
sys.excepthook = Pyro4.util.excepthook

# Importing the file that contains the graph
file = open('input.in')
string = file.read()

# get a Pyro proxy to the SimpleGraph object
graph = Pyro4.Proxy("PYRONAME:proxy.graph")

print('Input is in <string>')
print('SimpleGraph is in <graph>')