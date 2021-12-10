"""
Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation,
max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy
array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes
and for the flattened matrix.
"""
import numpy as np


def calculate(digits: list) -> dict:
    if len(digits) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(digits, (3, 3))

    return {
        'mean': _calculate_mean(matrix),
        'variance': _calculate_variance(matrix),
        'standard deviation': _calculate_std(matrix),
        'max': _calculate_max(matrix),
        'min': _calclulate_min(matrix),
        'sum': _calculate_sum(matrix),
    }


def _calculate_mean(matrix) -> list:
    return [
        list(np.mean(matrix, axis=0)),
        list(np.mean(matrix, axis=1)),
        np.mean(matrix)
    ]


def _calculate_variance(matrix):
    return [
        list(np.var(matrix, axis=0)),
        list(np.var(matrix, axis=1)),
        np.var(matrix)

    ]


def _calculate_std(matrix):
    return [
        list(np.std(matrix, axis=0)),
        list(np.std(matrix, axis=1)),
        np.std(matrix),
    ]


def _calculate_max(matrix):
    return [
        list(np.max(matrix, axis=0)),
        list(np.max(matrix, axis=1)),
        np.max(matrix),
    ]


def _calclulate_min(matrix):
    return [
        list(np.min(matrix, axis=0)),
        list(np.min(matrix, axis=1)),
        np.min(matrix)
    ]


def _calculate_sum(matrix):
    return [
        list(np.sum(matrix, axis=0)),
        list(np.sum(matrix, axis=1)),
        np.sum(matrix)
    ]
