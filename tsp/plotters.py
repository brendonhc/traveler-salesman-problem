import matplotlib.pyplot as plt
from tsp.tsp import TravelerSalesmanProblem


def plot_digraph(tsp: TravelerSalesmanProblem, way: list):
    x_arr, y_arr = [], []

    nodes = tsp.nodes()

    for i in range(len(nodes)):
        node = nodes[way[i]]

        x_arr.append(node['x'])
        y_arr.append(node['y'])

    fig, ax = plt.subplots()
    ax.plot(x_arr, y_arr, **{'marker': 'o'})
    plt.show()

# NEED FIX A BUG - SECOND PLOT IS PLOTED ABOVE
def plot_2_paths(tsp: TravelerSalesmanProblem, path1: list, path2: list):
    x_arr, y_arr = [], []

    nodes = tsp.nodes()

    fig, (ax1, ax2) = plt.subplots(1, 2)  # 2 plots

    # First plot
    for i in range(len(nodes)):
        node = nodes[path1[i]]

        x_arr.append(node['x'])
        y_arr.append(node['y'])

    ax1.plot(x_arr, y_arr, **{'marker': 'o'})

    # Second plot
    for i in range(len(nodes)):
        node = nodes[path2[i]]

        x_arr.append(node['x'])
        y_arr.append(node['y'])

    ax2.plot(x_arr, y_arr, **{'marker': 'o'})

    plt.show()
