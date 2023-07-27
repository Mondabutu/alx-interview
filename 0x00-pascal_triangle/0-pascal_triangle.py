#!/usr/bin/python3
"""Pascal triangle """


def pascal_triangle(k):
    """Returns a list of lists of integers 
    representing the Pascal’s triangle of n:
    """

    if k <= 0:
        return []

    
    """ initialize an empty resulting array """
    pascal = [[] for idx in range(k)]

    for li in range(k):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ the first column is always set to 1 """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            elif(col == li):
                """ the diagonal is always set to 1 """
                pascal[li].append(1)

    return pascal
