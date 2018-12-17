# -*- coding: utf-8 -*-
import Pyro4
from simplegraph import SimpleGraph

# Before all, run it on a other termminal
#python3 -m Pyro4.naming

def main():
	Pyro4.Daemon.serveSimple(
		{
			SimpleGraph: "proxy.graph"
		},
		host = '127.0.0.1',
		port = 46413,
		ns = True)

if __name__=="__main__":
    main()