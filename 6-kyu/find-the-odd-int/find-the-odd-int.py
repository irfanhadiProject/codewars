def find_it(seq):
    counts = {}
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for key in counts:
        if counts[key] % 2 != 0:
            return key
​