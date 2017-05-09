from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    flatten_ls=[]
    for ele in lst:
        if type(ele) == list:
            flatten_ls = flatten_ls + flatten(ele)
        else:
            flatten_ls = flatten_ls + [ele]
    return flatten_ls

# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    len_merge = len(lst1) + len(lst2)
    lst_merge =[]
    x,y = 0,0
    for i in range(len_merge):
        if x == len(lst1):
            lst_merge += [lst2[y]]
            y += 1
        elif y == len(lst2):
            lst_merge += [lst1[x]]
            x += 1
        elif lst1[x]>lst2[y]:
            lst_merge += [lst2[y]]
            y += 1
        else:
            lst_merge += [lst1[x]]
            x += 1
    return lst_merge


