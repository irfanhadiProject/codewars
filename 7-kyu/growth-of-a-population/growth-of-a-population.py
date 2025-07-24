def nb_year(p0, percent, aug, p):    
    def recurse(current ,years):
        if current >= p:
            return years
        
        new_current = current + current * percent * 0.01 + aug
        return recurse(int(new_current), years + 1)
      
    
    return recurse(p0, 0)
        
    # your code