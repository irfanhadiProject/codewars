def in_array(array1, array2):
    # your code
    r = []
    for item1 in array1:
        for item2 in array2:
            if item1 in item2:
                if item1 not in r:
                    r.append(item1)
    r.sort()
    return r