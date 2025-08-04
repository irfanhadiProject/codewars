def dig_pow(n, p):
    # your code
    digits = [int(num) for num in str(n)]
    total = 0
    for i in range(len(digits)):
        total += digits[i] ** (p + i)
    
    if total % n == 0:
        return total // n
    
    return -1
    