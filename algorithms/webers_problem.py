import numpy as np
import functions as F
from algorithms.mass_center import calculate_mass_center


def solve_webers_problem(set_of_points):
    """
    Solve the Weber's Problem using the Nelder-Mead Simplex algorithm.
    :param set_of_points: The set of points given to the algorithm.
    :return: The solution point.
    """
    pass


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


def _centroid(set_of_points) -> np.ndarray:
    """
    Calculate the centroid of points i.e. the point with the mean (average) coordinates.
    :param set_of_points: The set of points to calculate the centroid of.
    :return: The centroid of points i.e. the point with the mean (average) coordinates.
    """
    # this is actually the same as the mass center so we will use our implementation of it
    return np.array(calculate_mass_center(set_of_points))


def _reflection_points(set_of_points) -> np.ndarray:
    """
    Calculate the reflection points of the set of point given to the function.
    :param set_of_points: The set of points to calculate the reflection of.
    :return: The reflection points of the set of point given to the function.
    """
    return (1 + alpha) * _centroid(set_of_points) - alpha * set_of_points
