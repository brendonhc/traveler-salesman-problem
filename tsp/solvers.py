"""
    This document contains the Solver classes to TSP - Traveler Salesman
    Problem.

        # class NearestNeighborSolver:
            implementation of the nearest neighbor algorithm

        # class TwoOptSolver:
            implementation of an improved algorithm
"""

from tsp.tsp import TravelerSalesmanProblem


class NearestNeighborSolver:
    def __init__(self, tsp: TravelerSalesmanProblem):
        self.__adjmatrix = tsp.adjacencymatrix()
        self.__n_nodes = tsp.size()
        self.__visited = [False] * tsp.size()
        self.__way = []
        self.__distance = 0

    """ Return a solved way - list of cities sorted by way 
    
    Solve the TravelerSalesmanProblem with a simple algorithm
    """

    def solve(self):
        # Visit first city
        self.__visited[0] = True
        self.__way.append(0)
        actual_city = 0
        best_city = 0

        while False in self.__visited:
            best_dist = float('Inf')

            for next_city in range(self.__n_nodes):
                if next_city != actual_city and not self.__visited[next_city]:

                    next_city_dist = self.__adjmatrix[actual_city][next_city]

                    if next_city_dist < best_dist:
                        best_dist = next_city_dist
                        best_city = next_city

            self.__visited[best_city] = True  # Mark as visited
            self.__way.append(best_city)  # Put visited city in list
            self.__distance += best_dist  # Add new dist in total dist var

        return {
            'way': self.__way,
            'distance': self.__distance
        }


class TwoOptSolver:
    pass
