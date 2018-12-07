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
            self.__filename = tsp_file.name
            tsp = tsp_file.read().split('NODE_COORD_SECTION')

            self.__header = tsp[0].splitlines()
            self.__data = tsp[1].splitlines()

            # Coord x and y of each node
            self.__nodes = []
            self.__dimension = 0

            for line in self.__data:
                if len(line) < 6:  # Try ignore blank lines, trash and EOF
                    continue

                row = line.split()

                # Each node is a dict with this data
                self.__nodes.append({
                    'id': int(row[0]) - 1,  # 0 to self.dimension-1
                    'x': float(row[1]),
                    'y': float(row[2])
                })
                self.__dimension += 1

            self.__init_adjacency_matrix()  # Create a adjacency matrix

    # Matrix used to run graph
    def __init_adjacency_matrix(self):

        self.__matrix = []

        # Calc dist of each Vert to all other vertices
        for vert in self.__nodes:

            row = []

            for adj_id in range(self.size()):
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
    def header(self):
        return self.__header

    """ Return all graph nodes
    """
    def nodes(self):
        return self.__nodes

    """ Return tsp filename
    """
    def filename(self):
        return self.__filename
