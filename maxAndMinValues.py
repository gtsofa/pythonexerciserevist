# maximum and minimum element in a list.
# eg test0 = [1,3,5,6,8,9]
# [min, max]  = [1,9]
# if min == max ==> [min] or [max]
# eg test1 = [3,3,3] ==> [3]

def findMaxMin(alist):
    # initialize elements using the max and min functions
    min_value = min(alist)
    max_value = max(alist)

    # empty list that will hold the list results.
    result_list = []

    # compare the elements
    if min_value < max_value:
        result_list = [min_value, max_value]
    elif min_value == max_value:
        result_list = [min_value]

    # else:
    #     return False

    return result_list

# test values
test1 = [1,1,1]
test2 = [3,-1,7,2,5]
print(findMaxMin(test1))
print(findMaxMin(test2))

