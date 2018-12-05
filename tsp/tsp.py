"""
    This document contain the class that design a TSP problem with reader
    and parser methods
"""
from math import sqrt

""" Class TravelerSalesmanProblem  
    
    A instance of this class recives a path to '.tsp' file and parser this 
    file generating a array with cities nodes and a adjacency matrix with 
    the distances for all cities.
    
    This class can be used to prepare a tsp to solver.
"""


class TravelerSalesmanProblem:

    # Init object with path to tsp file
    def __init__(self, tsp_file_path):
        self.__matrix = None

        with open(tsp_file_path, 'r') as tsp_file:  # Read tsp file
            tsp = tsp_file.read().splitlines()

            # First 5 rows
            self.__header = tsp[:5]

            # First tsp row and the Last list element - str
            self.__name = tsp[0].split().pop().strip()

            # Third tsp row and the Last list element - int
            self.__dimension = int(tsp[3].split().pop())

            tsp = tsp[6:-1]  # Nodes lines only (without header and EOF)

            # Coord x and y of each node
            self.__nodes = []

            for line in tsp:
                row = line.split()

                # Each node is a dict with this data
                self.__nodes.append({
                    'id': int(row[0]) - 1,  # 0 to self.dimension-1
                    'x': float(row[1]),
                    'y': float(row[2])
                })

            self.__init_adjacency_matrix()  # Create a adjacency matrix

    # Matrix used to run graph
    def __init_adjacency_matrix(self):

        self.__matrix = []

        # Calc dist of each Vert to all other vertices
        for vert in self.__nodes:

            row = []

            for adj_id in range(self.__dimension):
                adj = self.__nodes[adj_id]

                # Dist between 2 points (2D)
                xa, ya, xb, yb = vert['x'], vert['y'], adj['x'], adj['y']

                dist = sqrt(pow(xa - xb, 2) + pow(ya - yb, 2))

                row.append(dist)  # Fill row with distances

            self.__matrix.append(row)  # Fill matrix with rows

    """ Return number of cities in the tsp
    """
    def size(self):
        return self.__dimension

    """ Return distance between node 'a' to node 'b'
    
        'a' and 'b' variables are matrix coordinates
    """
    def dist(self, a, b):
        return self.__matrix[a][b]

    """ Return adjacency matrix
    """
    def adjacencymatrix(self):
        return self.__matrix

    """ Return name of the problem 
    """
    def name(self):
        return self.__name
