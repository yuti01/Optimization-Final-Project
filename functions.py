"""
Contains The Functions We Are Trying To Minimize.
We Are Actually Searching For The Point That Minimizes The Function (i.e. argmax).
"""
import numpy as np


def sum_of_distances(set_of_points, suggested_solution, weighted: bool = True):
    """
    Get the value of the function we are trying to minimize.
    :param set_of_points: The set of points (weight included)
                          we are trying to solve the problem for.
    :param suggested_solution: The suggested solution point
                               (Note: there is no weight in the solution point).
    :param weighted: A boolean flag.
                     - If set to True (default), we are considering the last coordinate as the weight of the point.
                     This is the function we are minimizing in the Weber's Problem.

                     - If set to False, we are expecting an un-weighted set of points.
                     This is the function we are minimizing in the Geometric Median Problem.

    :return: The value of the function we are trying to minimize in the Weber's / Geometric Median Problem.
    """
    if type(set_of_points) != np.ndarray:
        set_of_points = np.array(set_of_points)

    if weighted:
        # get the weight and the points in a separated arrays
        set_of_points, weights = set_of_points[:, :2], set_of_points[:, -1]

    # initialize the function value to zero
    function_value = 0

    # calculate the value of the function - sum of (weighted distances)
    for idx, point in enumerate(set_of_points):
        dist = np.linalg.norm(point - suggested_solution)

        if weighted:
            dist *= weights[idx]

        function_value += dist

    return function_value
