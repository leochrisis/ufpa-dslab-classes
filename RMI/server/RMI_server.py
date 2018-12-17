# -*- coding: utf-8 -*-
import Pyro4
#from inputer import Inputer
from simplegraph import SimpleGraph

#daemon = Pyro4.Daemon()				# make a Pyro daemon (server)
#uri = daemon.register(Inputer)		# register the inputer class as a Pyro object

#print("Ready.\nObject URI =", uri)	# print the URI so we can use it in the client later
#daemon.requestLoop()				# start the event loop of the server to wait for calls

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