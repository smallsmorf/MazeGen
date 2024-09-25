# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.adjacencyList: dict[Coordinates, list[Coordinates]] = {}
        pass 

        
    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if not self.hasVertex(label):
            self.adjacencyList[label] = []
        pass



    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for label in vertLabels:
            self.addVertex(label)
        pass



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.hasVertex(vert1) or not self.hasVertex(vert2):
            return False
        if not addWall:
            if not vert2 in self.adjacencyList[vert1]:
                self.adjacencyList[vert1].append(vert2)
            if not vert1 in self.adjacencyList[vert2]:
                self.adjacencyList[vert2].append(vert1)
        return True
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not vert2.isAdjacent(vert1):
            return False
        # if they are adjacent, and wallStatus is True, check if they are in the adjacency list of one another, if so remove, else return True.
        # if they are adjacent but wallStatus is False, check if they are in the adjacency list of one another, if yes return True, else append
        if wallStatus:
            self.adjacencyList[vert1].remove(vert2)
            self.adjacencyList[vert2].remove(vert1)
        else:
            if not vert2 in self.adjacencyList[vert1]:
                self.adjacencyList[vert1].append(vert2)
            if not vert1 in self.adjacencyList[vert2]:
                self.adjacencyList[vert2].append(vert1)
        return True



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.hasEdge(vert1, vert2):
            return False
        self.adjacencyList[vert1].remove(vert2)
        return True
        pass
        


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.adjacencyList



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return vert2.isAdjacent(vert1)


    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return self.hasEdge(vert1, vert2) and not vert2 in self.adjacencyList[vert1]
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        return [neighbour for neighbour in self.adjacencyList if self.hasEdge(label, neighbour)] 

        