import copy
import numpy as np
import statistics
from collections import defaultdict
 
import sys

#Initializing the Graph Class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance
    def printGraph(self):
        print(self.edges)
        print(self.distances)
 
def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        print(len(nodes))
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path

def main1():
	lines = []
	file = 'input'
	#NCN
	#NBCCN
	#file = 'input_test'
	#file = 'input_test2'
	#file = 'input_test3'
	with open(file) as f:
		lines = f.readlines()
	
	lines_s = []
	for l in lines:
		lines_s.append(l.strip()) 
	
	lt5 = []
	for l_old in lines_s:
		l = copy.copy(l_old)
		s_new = ''
		s_new += l
		for c in range(4):
			l_new = ''
			for s in l:
				i = int(s)
				i += 1
				if i == 10:
					i = 1
				l_new += str(i)
			l = copy.copy(l_new)
			s_new += l_new
		lt5.append(s_new)
	
	lt5d = copy.copy(lt5)
	for c in range(4):
		l_temp = []
		for l in lt5:
			l_new = ''
			for s in l:
				i = int(s)
				i += 1
				if i == 10:
					i = 1
				l_new += str(i)
			lt5d.append(l_new)
			l_temp.append(l_new)
		lt5 = copy.copy(l_temp)

	for l in lt5d:
		print(l)
	
	#print(lt5d)
	x = len(lt5d[0])
	y = len(lt5d)
	#print(x)
	#print(y)
	
	customGraph = Graph()
	for cs in range(y):
		for cl in range(x):
			node = str(cl)+"#"+str(cs)
			customGraph.addNode(node)
			if cl-1 >= 0:
				ntemp = str(cl-1)+"#"+str(cs)
				customGraph.addEdge(node, ntemp, int(lt5d[cs][cl-1]))
			if cs-1 >= 0:
				ntemp = str(cl)+"#"+str(cs-1)
				customGraph.addEdge(node, ntemp, int(lt5d[cs-1][cl]))
			if cl+1 < x:
				ntemp = str(cl+1)+"#"+str(cs)
				customGraph.addEdge(node, ntemp, int(lt5d[cs][cl+1]))
			if cs+1 < y:
				ntemp = str(cl)+"#"+str(cs+1)
				customGraph.addEdge(node, ntemp, int(lt5d[cs+1][cl]))
			cl += 1
		cs += 1
	
	customGraph.printGraph()

	visited, path = dijkstra(customGraph, "0#0")
	print(visited)

if __name__ == '__main__':
	main1()