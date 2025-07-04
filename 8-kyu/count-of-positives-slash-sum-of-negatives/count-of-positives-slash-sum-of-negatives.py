def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    positive_count = sum(1 for num in arr if num > 0)
    negative_sum =  sum(num for num in arr if num < 0)
    
    return [positive_count, negative_sum]