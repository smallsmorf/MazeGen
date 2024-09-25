# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        ### Implement me! ###
        # Matrix let outer list be x, inner list by y
        # Matrix let 0 be no connection, 1 be edge, -1 be wall
        self.vertDict: dict[Coordinates, int] = {}
        self.adjacencyMatrix: List[List[int]] = [[0] * 150 for _ in range(150)]
        



    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if label not in self.vertDict:
            # Check if adding the new vertex will exceed the current capacity
            if len(self.vertDict) >= len(self.adjacencyMatrix):
                # create a adjacencyMatrix with two times size
                newMatrixSize = len(self.adjacencyMatrix) * 2 
                newMatrix = [[0] * newMatrixSize for _ in range(newMatrixSize)]
                # Copy existing data to the new matrix
                for i, row in enumerate(self.adjacencyMatrix):
                    for j, val in enumerate(row):
                        newMatrix[i][j] = val
                self.adjacencyMatrix = newMatrix

            # Add the new vertex to the vertex dictionary
            index = len(self.vertDict)
            self.vertDict[label] = index
                    



    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for label in vertLabels:
            self.addVertex(label)
        



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.hasVertex(vert1) or not self.hasVertex(vert2):
            return False
        if self.hasEdge(vert1, vert2):
            return False
        sourceIndex = self.vertDict[vert1]
        targetIndex = self.vertDict[vert2]
        self.adjacencyMatrix[sourceIndex][targetIndex] = -1 if addWall else 1
        self.adjacencyMatrix[targetIndex][sourceIndex] = -1 if addWall else 1
        return True
    


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.hasVertex(vert1) or not self.hasVertex(vert2):
            return False
        if not vert1.isAdjacent(vert2):
            return False
        index1 = self.vertDict[vert1]
        index2 = self.vertDict[vert2]
        self.adjacencyMatrix[index1][index2] = -1 if wallStatus else 1
        self.adjacencyMatrix[index2][index1] = -1 if wallStatus else 1
        return True



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        
        ############## What happens if wallExist ##########################
        if not self.hasEdge(vert1, vert2):
            return False
        sourceIndex = self.vertDict[vert1]
        targetIndex = self.vertDict[vert2]
        self.adjacencyMatrix[sourceIndex][targetIndex] = 0
        return True
        


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.vertDict
        



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        sourceIndex = self.vertDict[vert1]
        targetIndex = self.vertDict[vert2]
        return self.adjacencyMatrix[sourceIndex][targetIndex] != 0
        



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # coordinates valid
        if not self.hasVertex(vert1) or not self.hasVertex(vert2):
            return False
        if not vert1.isAdjacent(vert2):
            return False
        source = self.vertDict[vert1]
        target = self.vertDict[vert2]
        return True if self.adjacencyMatrix[source][target] == -1 else False
        



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        return [neighbour for neighbour in self.vertDict if self.hasEdge(label, neighbour)]    