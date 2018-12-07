from tsp.tsp import TravelerSalesmanProblem
from tsp.solvers import NearestNeighborSolver, Improver
import tsp.plotters as view

from datetime import datetime

# paths = ['database/brd14051.tsp']
# paths = ['database/brendon.tsp', 'database/brendon2.tsp']
paths = ['database/brendon.tsp', 'database/a280.tsp', 'database/ali535.tsp',
         'database/att48.tsp', 'database/att532.tsp', 'database/berlin52.tsp',
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

    # Plot
    view.plot_digraph(TSP, result['way'])
    view.plot_digraph(TSP, improved_result['way'])
    view.plot_2_paths(TSP, result['way'], improved_result['way'])

    print('#######################################')
    [print(line) for line in TSP.header()]
    print('#######################################\n')
    print('# Solver Algorithm - Nearest Neighbor #')
    print('Time:', solver_end_time - solver_start_time)
    print('Route:')
    print(result['way'])
    print('Cost:', result['cost'])
    print()
    print('# Improvere Algorithm - 2-Opt #')
    print('Time:', improver_end_time - improver_start_time)
    print('Route:')
    print(improved_result['way'])
    print('Cost:', improved_result['cost'])
    print('\n')
