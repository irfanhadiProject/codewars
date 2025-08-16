def solution(array_a, array_b):
    total_squares = 0
    for i in range(len(array_a)):
        squares = (array_a[i] - array_b[i]) ** 2
        total_squares += squares
    
    return total_squares / len(array_a)
        
        