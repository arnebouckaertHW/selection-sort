def sort (data, first: int):
    """Sorts a list of integers form largest to smallest bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variables named i, j
    i = len(data) - first - 1
    j = 0

    # initialize variable named big used to store index of biggest value
    small = 0

    # initialize variable named temp used to swap list values
    temp = 0
    
    while (i > 0):
        # set big equal to first
        small = first

        # set j equal to first + 1
        j = first + 1

        while (j <= first + i):
            # if value in data[big] is less than value in data[j], set big equal to j
            if (data[j] < data[small]):
                small = j

            # increment j
            j += 1
        
        # set temp to value in data[first + i]
        temp = data[first + i]

        # set data[first + i] to value in data[big]
        data[first + i] = data[small]

        # set data[big] to value in temp
        data[small] = temp

        # decrement i
        i -= 1