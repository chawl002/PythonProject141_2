import os
import re
import sys
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")

def BellmanFord(G):
    pathPairs=[]
    # Fill in your Bellman-Ford algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j
    return pathPairs

def FloydWarshall(G):
    pathPairs=[]
    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j
    return pathPairs

def readFile(filename):
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) >= len(vertices) or int(sink) >= len(vertices):
                print("Attempting to insert an edge between "+str(source)+" and "+str(sink)+" in a graph with "+str(len(vertices))+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
    # TODO: Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)

def writeFile(lengthMatrix,filename):
    filename=os.path.splitext(os.path.split(filename)[1])[0]
    outFile=open('output/'+filename+'_output.txt','w')
    for vertex in lengthMatrix:
        for length in vertex:
            outFile.write(str(length)+',')
        outFile.write('\n')


def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    pathLengths=[]
    if algorithm == 'b' or algorithm == 'B':
        pathLengths=BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        pathLengths=FloydWarshall(G)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))
    writeFile(pathLengths,filename)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
