"""
    This document contains the Solver classes to TSP - Traveler Salesman
    Problem.

        # class NearestNeighborSolver:
            implementation of the nearest neighbor algorithm

        # class Improver2Opt:
            implementation of an improver algorithm. From a List nodes with
            a defined route, the Improver2Opt static method 'improve()' can
            minimize costs swapping vertices with 2 Opt algorithm.
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


class Improver:
    @staticmethod
    def improve2opt(tsp: TravelerSalesmanProblem, route: list, cost: float):
        matrix = tsp.adjacencymatrix()
        size = tsp.size()

        # 2-Opt algorithm require minimum 4 vertices
        if size < 4:
            return list

        new_route = route.copy()
        new_total_cost = cost

        for i in range(3, size):
            a, b, c, d = i - 3, i - 2, i - 1, i

            # Actual route                      # Swap like this:
            ab_dist = matrix[a][b]              # a b       a - b
            cd_dist = matrix[c][d]              #  x    =>
            actual_cost = ab_dist + cd_dist     # c d       c - d

            # Possible new route
            ad_dist = matrix[a][d]
            cb_dist = matrix[c][b]
            new_cost = ad_dist + cb_dist

            # Permutation verification
            if new_cost < actual_cost:
                # News costs calc
                new_total_cost -= actual_cost
                new_total_cost += new_cost
                # Swap
                new_route[a], new_route[b] = new_route[b], new_route[a]

        return {
            'way': new_route,
            'cost': new_total_cost
        }
