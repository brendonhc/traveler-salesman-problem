from tsp.tsp import TravelerSalesmanProblem
from tsp.solvers import NearestNeighborSolver

path = 'database/a280.tsp'

TSP = TravelerSalesmanProblem(path)

Solver = NearestNeighborSolver(TSP)
print(Solver.solve())