def remov_nb(n):
    # your code
    total_sum = n * (n + 1) // 2
    result = []
    
    for a in range(1, n + 1): 
        if (total_sum + 1) % (a + 1) == 0:
            b = (total_sum + 1) // (a + 1) - 1
            if 1 <= b <= n:
                result.append((a, b))
    
    return result
            