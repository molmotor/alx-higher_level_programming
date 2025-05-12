#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for element in matrix:
        def square(element):
            return element*element
        new_matrix = matrix(map(square, element))
