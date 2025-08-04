def xo(s):
    x_count = s.lower().count('x')
    o_count = s.lower().count('o')
    
    if x_count == o_count:
        return True
    
    return False