def sort (data, first: int):
    """Sorts a list of strings form smallest to largest bypassing the elements to the left of first.

    Args:
        data (string): list of strings
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variables named i, j
    i = len(data) - first - 1
    j = 0

    # initialize variable named big used to store index of biggest value
    big = 0

    # initialize variable named temp used to swap list values
    temp = 0
    
    while (i > 0):
        # set big equal to first
        big = first

        # set j equal to first + 1
        j = first + 1

        while (j <= first + i):
            # if value in data[big] is less than value in data[j], set big equal to j
            if (len(data[big]) < len(data[j])):
                big = j

            # increment j
            j += 1
        
        # set temp to value in data[first + i]
        temp = data[first + i]

        # set data[first + i] to value in data[big]
        data[first + i] = data[big]

        # set data[big] to value in temp
        data[big] = temp

        # decrement i
        i -= 1