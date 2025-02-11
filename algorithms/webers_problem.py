import numpy as np
import functions as F
from utils import print_simplex

from algorithms.mass_center import calculate_mass_center


"""
Nelder-Mead Hyper-Parameters:

alpha - coefficients of reflection.
beta - expansion.
gamma - contraction.
delta - shrink.
"""
alpha = 1
beta = 2
gamma = 0.5
delta = 0.5

"""
stopping parameter
"""
epsilon = 1e-10


def solve_webers_problem(set_of_points):
    """
    Solve the Weber's Problem using the Nelder-Mead Simplex algorithm.
    :param set_of_points: The set of points given to the algorithm.
    :return: The solution point.
    """
    # define the target function
    T = lambda x: F.sum_of_distances(set_of_points, x, weighted=True)

    # initialize the simplex
    simplex = _init_simplex(set_of_points)
    print_simplex(simplex, T)

    last_simplex = np.copy(simplex)

    while True:
        # sort the simplex
        simplex = _sort_simplex_points(set_of_points, simplex)

        print_simplex(simplex, T)

        centroid = _centroid(set_of_points, simplex)

        # update the simplex

        # 1. Reflection
        # calculate reflection point
        reflection_point = _reflection_point(simplex[-1], centroid)

        if T(simplex[0]) <= T(reflection_point) <= T(simplex[-2]):
            # replace the worst point with the reflection point
            simplex[-1] = reflection_point

        # 2. Expansion
        elif T(reflection_point) < T(simplex[0]):
            # calculate the expansion point
            expansion_point = _expansion_point(reflection_point, centroid)

            if T(expansion_point) < T(reflection_point):
                # replace the worst point with the expansion point
                simplex[-1] = expansion_point
            else:
                # replace the worst point with the reflection point
                simplex[-1] = reflection_point

        # 4. Outside contraction
        elif T(simplex[-2]) <= T(reflection_point) <= T(simplex[-1]):
            # calculate outside contraction point
            oc_point = _outside_contraction_point(reflection_point, centroid)

            if T(oc_point) < T(reflection_point):
                simplex[-1] = oc_point
            else:
                simplex = _shrink(simplex)

        # 5. Inside contraction
        elif T(reflection_point) >= T(simplex[-1]):
            # calculate inside contraction point
            ic_point = _inside_contraction_point(simplex[-1], centroid)

            if T(ic_point) <= T(simplex[-1]):
                simplex[-1] = ic_point
            else:
                simplex = _shrink(simplex)

        # stopping condition
        if _should_stop(last_simplex, simplex):
            break

        last_simplex = simplex

    return _best_point(simplex, T)


"""def _init_simplex(problem_points):
    simplex_points = list()
    taken_indexes = set()

    dimension = len(problem_points[0]) - 1
    number_of_points = len(problem_points)

    assert dimension + 1 <= number_of_points, "our initialization method assumes that the number of " \
                                              "points given with the problem is larger than the problem's dimension."

    while len(simplex_points) < dimension + 1:
        while True:
            random_index = np.random.randint(low=0, high=number_of_points)

            if random_index not in taken_indexes:
                taken_indexes.add(random_index)
                break

        simplex_points.append(problem_points[random_index][:2])

    return np.array(simplex_points, dtype="float")"""


def _init_simplex(problem_points):
    points = problem_points[:, :2]

    simplex_points = list()

    dimension = len(points[0])
    number_of_points = len(points)

    random_index = np.random.randint(low=0, high=number_of_points)
    random_point = points[random_index]

    simplex_points.append(random_point)

    h = np.array([0.05 if x != 0 else 0.00025 for x in random_point])
    e = np.identity(dimension)

    for j in range(0, dimension):
        point = random_point + h[j]*e[j]
        simplex_points.append(point)

    return np.array(simplex_points, dtype="float")


def _should_stop(prev_simplex, current_simplex):
    stopping_sum = 0.5 * np.sum([(np.linalg.norm(p1 - p2)**2) for p1, p2 in zip(prev_simplex, current_simplex)])

    return stopping_sum < epsilon


def _sort_simplex_points(problem_points, simplex_points):
    """
    Sort the points of the simplex by the value of the target function.
    :param problem_points: The constant set of points given with the problem.
    :param simplex_points: The simplex set of points.
    :return: The simplex set of points sorted by the value of the target function.
    """
    return np.array(sorted(simplex_points, key=lambda point: F.sum_of_distances(problem_points, point)))


def _best_point(simplex_points, target_function):
    best_point_index = np.argmin([target_function(point) for point in simplex_points])

    return simplex_points[best_point_index]


def _centroid(set_of_points, simplex_points) -> np.ndarray:
    """
    Calculate the centroid of points i.e. the point with the mean (average) coordinates.
    :param set_of_points: The set of points to calculate the centroid of.
    :return: The centroid of points i.e. the point with the mean (average) coordinates.
    """
    sorted_points = _sort_simplex_points(set_of_points, simplex_points)[:-1]

    return np.mean(sorted_points, axis=0)


def _reflection_point(point, centroid) -> np.ndarray:
    """
    Calculate the reflection point of a single simplex point.
    :param point: A single point of the simplex.
    :param centroid: The centroid of the simplex points.
    :return: The reflection point of a single simplex point.
    """
    if type(point) != np.ndarray:
        point = np.array(point)

    if type(centroid) != np.ndarray:
        centroid = np.array(centroid)

    return (1 + alpha) * centroid - alpha * point


def _expansion_point(point, centroid) -> np.ndarray:
    """
    Calculate the expansion point of a single simplex point.
    :param point: A single point of the simplex.
    :param centroid: The centroid of the simplex points.
    :return: The expansion point of a single simplex point.
    """
    if type(point) != np.ndarray:
        point = np.array(point)

    if type(centroid) != np.ndarray:
        centroid = np.array(centroid)

    return beta * point - ((1 - beta) * centroid)


def _outside_contraction_point(point, centroid) -> np.ndarray:
    """
    Calculate the outside contraction point of a single simplex point.
    :param point: A single point of the simplex.
    :param centroid: The centroid of the simplex points.
    :return: The outside contraction point of a single simplex point.
    """
    if type(point) != np.ndarray:
        point = np.array(point)

    if type(centroid) != np.ndarray:
        centroid = np.array(centroid)

    return gamma * point + (1 - gamma) * centroid


def _inside_contraction_point(point, centroid) -> np.ndarray:
    """
    Calculate the inside contraction point of a single simplex point.
    :param point: A single point of the simplex.
    :param centroid: The centroid of the simplex points.
    :return: The inside contraction point of a single simplex point.
    """
    if type(point) != np.ndarray:
        point = np.array(point)

    if type(centroid) != np.ndarray:
        centroid = np.array(centroid)

    return (1 + gamma) * centroid - gamma * point


def _shrink(simplex_points):
    """
    Shrink the simplex.
    :param simplex_points: Simplex before shrinking.
    :return: Shrinked simplex.
    """
    for i in range(1, len(simplex_points)):
        simplex_points[i] = _shrink_point(simplex_points[i], simplex_points[0])

    return simplex_points


def _shrink_point(point, best_simplex_point) -> np.ndarray:
    """
    Calculate the shrink point of a single simplex point.
    :param point: A single point of the simplex.
    :param best_simplex_point: The simplex point with the lowest target function value.
    :return: The shrink point of a single simplex point.
    """
    if type(point) != np.ndarray:
        point = np.array(point)

    if type(best_simplex_point) != np.ndarray:
        best_simplex_point = np.array(best_simplex_point)

    return delta * point + (1 - delta) * best_simplex_point
