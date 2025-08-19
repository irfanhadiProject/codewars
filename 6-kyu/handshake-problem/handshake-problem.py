def get_participants(handshakes):
    left = 0
    right = (handshakes * 2) + 1
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid - 1) == handshakes * 2:
            return mid
        elif mid * (mid - 1) < handshakes * 2:
            left = mid + 1
        else:
            right = mid - 1
    
    return left