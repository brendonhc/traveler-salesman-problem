from tsp.tsp import TravelerSalesmanProblem
from tsp.solvers import NearestNeighborSolver

from datetime import datetime

paths = ['database/a280.tsp', 'database/ch130.tsp']


for path in paths:
    # Loading the problem
    TSP = TravelerSalesmanProblem(path)

    # Solving the problem
    start_time = datetime.now()

    Solver = NearestNeighborSolver(TSP)
    result = Solver.solve()

    end_time = datetime.now()

    # Report print
    print('#######################################')
    print('# Solver Algorithm - Nearest Neighbor #')
    print('#######################################')
    print('Problem name:', TSP.name())
    print('Time:', end_time-start_time)
    print('Route:')
    print(result['way'])
    print('Cost:', result['cost'])

    print('\n')
