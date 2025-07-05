def square_digits(num):
    # Your code here
    square_nums = [int(digit) ** 2 for digit in str(num)]
    
    return int("".join(str(num) for num in square_nums))