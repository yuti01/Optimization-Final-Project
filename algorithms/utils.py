from numpy import random
import numpy as np


def generate_random_points(minimum, maximum, number_of_points: int, returned_type='list'):
    """
    Generate random set of points.
    :param minimum: the minimum value of the coordinates
    :param maximum: the maximum value of the coordinates
    :param number_of_points: the number of points to generate.
                             or in other words, the size of the points set.
    :param returned_type: the type of the returned points set.
                          Specify 'list' to get a regular python list.
                          Specify 'set' to get a regular python set (promises unique values).
                          Specify 'array' to get a numpy array.
    :return:
    """
    assert returned_type == 'list' or returned_type == 'set' or returned_type == 'array',\
        'unsupported return type.' \
        '\nsupported types: \'list\' (regular python list), \'set\' (regular python set), ' \
        ' \'array\' (numpy ndarray)'

    assert number_of_points > 0, 'number of point should be a possitive integer'

    if type(maximum) == int or len(maximum) == 1:
        maximum = (maximum, maximum)

    if type(minimum) == int or len(minimum) == 1:
        minimum = (minimum, minimum)

    if minimum[0] > maximum[0] or minimum[1] > maximum[1]:
        raise ValueError('the given minimum is larger than the given maximum.')

    points = set() if returned_type == 'set' else list()

    while len(points) < number_of_points:
        x = minimum[0] + (maximum[0] - minimum[0]) * random.random()
        y = minimum[1] + (maximum[1] - minimum[1]) * random.random()

        if type(points) == set:
            points.add((x, y))
        else:
            points.append((x, y))

    if returned_type == 'array':
        return np.array(points)
    else:
        return points


"""
A point set used in an article
"""
article_data_set = np.array([
    (1, 9, 1),  # 1
    (1, 2, 1),  # 2
    (1, 5, 4),  # 3
    (2, 4, 3),  # 4
    (2, 3, 2),  # 5
    (3, 8, 4),  # 6
    (3, 7, 3),  # 7
    (3, 6, 1),  # 8
    (3, 5, 2),  # 9
    (4, 4, 4),  # 10
    (4, 7, 1),  # 11
    (5, 7, 1),  # 12
    (5, 1, 4),  # 13
    (6, 3, 4),  # 14
    (6, 9, 3),  # 15
    (6, 2, 2),  # 16
    (7, 0, 1),  # 17
    (7, 8, 4),  # 18
    (7, 5, 2),  # 19
    (7, 1, 2),  # 20
    (8, 4, 3),  # 21
    (8, 6, 1),  # 22
    (9, 8, 1),  # 23
    (9, 3, 4),  # 24
    (9, 2, 1),  # 25
    (9, 10, 2),  # 26
    (10, 1, 3),  # 27
    (10, 4, 1),  # 28
    (10, 5, 2),  # 29
    (10, 9, 1)  # 30
])
