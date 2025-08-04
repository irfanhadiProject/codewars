def array_diff(a, b):
    if not a or not b:
        return a
    
    return [item for item in a if item not in b]
    