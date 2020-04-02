"""
One of your coworkers checked in some code before leaving for vacation. 
Unfortunately, they provided no documentation or comments of what the code does. 
Please document the following code to make it more understandable.

Assume:

- You are passed in a list of integers
- The integers are in the range 1..n
- The list has a length of n+1
"""

def find(the_list):
    """Find the mode in the given list of integers. Returns the lower mode in 
    the case of a tie. 
    
    This function counts the frequency of the items in the list by means of 
    windowing. First, it calculates the possible minimum and maximum values 
    of the entire list, and uses those bounds to split the list into lower 
    and upper halves of possible values. For example, a list of 7 integers 
    in the range 1..6 would start with 1 and 6 as its floor and ceiling.
    Based on these floor and ceiling values, the algorithm sets lower and 
    upper ranges (in this case, [1,3] for the lower and [4,6] for the upper).
    Next, it counts the number of items in the list which fall into the lower 
    range. If there are more items within that range than the distinct number 
    of values in that range, then the floor and ceiling values are set to 
    the bounds of the lower range, effectively focusing the window. If not, 
    the window is focused on the upper range instead. This process occurs 
    repeatedly until the floor equals or exceeds the ceiling, at which point 
    the floor is returned. Because the window is adjusted to the range with 
    the most items in it, the floor "traces" the mode of the entire given list.
    
    Parameters:
    the_list (list): A list of integers in the range 1..n with length n+1

    Returns:
    floor (int): The mode of the list
    """
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # set lower/upper range bounds according to the current floor/ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_floor, lower_ceiling = floor, midpoint 
        upper_floor, upper_ceiling = midpoint+1, ceiling 

        # count the number of items in the lower range, inclusively
        items_in_lower_range = 0
        for item in the_list:
            if item >= lower_floor and item <= lower_ceiling:
                items_in_lower_range += 1

        # count the number of distinct possible ints in the lower range
        distinct_possible_integers_in_lower_range = (
            lower_ceiling
            - lower_floor
            + 1
        )

        # adjust the floor and ceiling bounds to the lower or upper range bounds
        # depending on if the list has more items in the lower or upper range, respectively
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            floor, ceiling = lower_floor, lower_ceiling
        else:
            floor, ceiling = upper_floor, upper_ceiling

    # the floor of the last iteration will be the mode of the initial given list
    return floor

print(find([6, 2, 3, 4, 1, 4, 4]))