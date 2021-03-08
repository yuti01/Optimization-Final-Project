from algorithms.webers_problem import solve_webers_problem
from algorithms.mass_center import calculate_mass_center
from utils import article_data_set

import functions as F

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #article_data_set[:, 2] = 1

    # define the target function
    T = lambda x: F.sum_of_distances(article_data_set, x, weighted=True)

    solution = solve_webers_problem(article_data_set)
    mass_center = np.array(calculate_mass_center(article_data_set[:, :2]))

    print(f"mass center {mass_center}, total cost {T(mass_center)}")
    print(f"nelder mead solution {solution}, total cost {T(solution)}")
    # print(f"nelder mead solution {np.array([5.497, 4.520])}, total cost {T(np.array([5.497, 4.520]))}")

    x = article_data_set[:, 0]
    y = article_data_set[:, 1]

    plt.scatter(x, y, s=40)
    plt.scatter(solution[0], solution[1], s=100, c="purple")
    plt.scatter(mass_center[0], mass_center[1], s=100, c="red")
    plt.show()
