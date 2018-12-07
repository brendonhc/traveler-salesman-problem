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
        self.__way.append(0)  # City id is not equal List id []
        actual_city = 0
        best_city = 0

        # While not visited all cities
        while False in self.__visited:
            best_cost = float('Inf')

            # For each city of the problem, go to nearest
            for next_city in range(self.__n_nodes):
                if next_city != actual_city and not self.__visited[next_city]:

                    next_city_cost = self.__adjmatrix[actual_city][next_city]

                    if next_city_cost < best_cost:
                        best_cost = next_city_cost
                        best_city = next_city

            self.__visited[best_city] = True  # Mark as visited
            self.__way.append(best_city)  # Put visited city in list
            self.__cost += best_cost  # Add new cost in total cost var

        # In the end, add cost of the last city to first become
        self.__cost += \
            self.__adjmatrix[self.__way[self.__n_nodes-1]][self.__way[0]]

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
        best_route = False

        # This statement runs until end possible improvements
        while not best_route:
            improved = False
            for i in range(3, size+3):
                a_id, b_id, c_id, d_id = i - 3, i - 2, i - 1, i

                # To close path
                if i == size:
                    d_id = 0
                elif i == size + 1:
                    c_id, d_id = 0, 1
                elif i == size + 2:
                    b_id, c_id, d_id = 0, 1, 2

                a, b = new_route[a_id], new_route[b_id]
                c, d = new_route[c_id], new_route[d_id]

                # Actual route                      # Swap like this:
                ab_dist = matrix[a][b]              # a b       a - b
                cd_dist = matrix[c][d]              #  x    =>
                actual_cost = ab_dist + cd_dist     # c d       c - d

                # Possible new route
                ac_dist = matrix[a][c]
                bd_dist = matrix[b][d]
                new_cost = ac_dist + bd_dist

                # Permutation verification
                if new_cost < actual_cost:
                    # Swap
                    new_route[b_id], new_route[c_id] = \
                                            new_route[c_id], new_route[b_id]
                    improved = True

            # If without improvements, end, this is best route
            if not improved:
                best_route = True

        # Need re-calc new total cost of route
        new_total_cost = 0
        for i in range(1, tsp.size()):
            city, next_city = new_route[i - 1], new_route[i]
            new_total_cost += matrix[city][next_city]

        new_total_cost += matrix[new_route[i]][new_route[0]]

        return {
            'way': new_route,
            'cost': new_total_cost
        }
