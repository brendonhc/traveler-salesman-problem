from tsp.tsp import TravelerSalesmanProblem
from tsp.solvers import NearestNeighborSolver, Improver

from datetime import datetime

paths = ['database/a280.tsp', 'database/ali535.tsp', 'database/att48.tsp',
         'database/att532.tsp', 'database/berlin52.tsp',
         'database/bier127.tsp']


for path in paths:
    # Loading the problem
    TSP = TravelerSalesmanProblem(path)

    # Solving the problem
    solver_start_time = datetime.now()

    Solver = NearestNeighborSolver(TSP)
    result = Solver.solve()

    solver_end_time = datetime.now()

    # Improving the solution
    improver_start_time = datetime.now()

    improved_result = Improver.improve2opt(TSP, result['way'], result['cost'])

    improver_end_time = datetime.now()

    # Report print
    print('#######################################')
    print('# Solver Algorithm - Nearest Neighbor #')
    print('#######################################')
    print('Problem header:', TSP.header())
    print('Time:', solver_end_time-solver_start_time)
    print('Route:')
    print(result['way'])
    print('Cost:', result['cost'])

    print('###############################')
    print('# Improvere Algorithm - 2-Opt #')
    print('###############################')
    print('Time:', improver_end_time-improver_start_time)
    print('Route:')
    print(improved_result['way'])
    print('Cost:', improved_result['cost'])

    print('\n')
