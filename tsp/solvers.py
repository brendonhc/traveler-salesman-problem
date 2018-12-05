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
        self.__cost = 0

    """ Return a solved way - list of cities sorted by way best cost
    
    Solve the TravelerSalesmanProblem with a simple algorithm
    """

    def solve(self):
        # Visit first city
        self.__visited[0] = True
        self.__way.append(1)  # City id is not equal List id []
        actual_city = 0
        best_city = 0

        while False in self.__visited:
            best_cost = float('Inf')

            for next_city in range(self.__n_nodes):
                if next_city != actual_city and not self.__visited[next_city]:

                    next_city_cost = self.__adjmatrix[actual_city][next_city]

                    if next_city_cost < best_cost:
                        best_cost = next_city_cost
                        best_city = next_city

            self.__visited[best_city] = True  # Mark as visited
            self.__way.append(best_city + 1)  # Put visited city in list
            self.__cost += best_cost  # Add new cost in total cost var

        return {
            'way': self.__way,
            'cost': self.__cost
        }


class TwoOptSolver:
    pass
