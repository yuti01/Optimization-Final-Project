import numpy as np


# Calculating the mass center is really easy!
# Its coordinates are the mean (average) of the points.
# Here is a simple python implementation

def calculate_mass_center(set_of_points) -> tuple:
    """
    Returns the mass center of a given point list (or set/array).
    :param set_of_points: the set/list/array of points.
    :return: the mass center of the given set of points.
    """

    # we distinguish between np.ndarray and other iterable types
    # for faster calculation on large point sets
    if type(set_of_points) == np.ndarray:
        x, y = tuple(np.mean(set_of_points, axis=0))
    else:
        x = np.mean([point[0] for point in set_of_points])
        y = np.mean([point[1] for point in set_of_points])

    return x, y
