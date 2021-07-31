# Written by https://www.geeksforgeeks.org/find-two-rectangles-overlap/
# Returns true if two rectangles(l1, r1)
# and (l2, r2) overlap
def doOverlap(l1, r1, l2, r2):
    """
    Takes in the points of two bounding boxes and checks if they overlap
    :param l1: top-left corner coordinate of box 1
    :param r1: bottom-right corner coordinate of box 1
    :param l2: top-left corner coordinate of box 2
    :param r2: bottom-right corner coordinate of box 2
    :return:
    """
    # To check if either rectangle is actually a line
    # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}

    if l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y:
        # the line cannot have positive overlap
        return False

    # If one rectangle is on left side of other
    if l1.x >= r2.x or l2.x >= r1.x:
        return False

    # If one rectangle is above other
    if r1.y >= l2.y or r2.y >= l1.y:
        return False

    return True
