def row_sum_odd_numbers(n):
    start = n * (n - 1) + 1
    sequence = [ start + 2 * i for i in range(n)]
    
    return sum(sequence)
    #your code here