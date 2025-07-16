def solution(array_a, array_b):
    squares = []
    for i in range(len(array_a)):
        diff = abs(array_a[i] - array_b[i])
        squares.append(diff ** 2)
    
    return sum(squares) / len(array_a)
        
        