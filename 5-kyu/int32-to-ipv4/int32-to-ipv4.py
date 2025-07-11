def int32_to_ip(int32):
    # your code here
    return f"{(int32 >> 24) & 0xFF}.{(int32 >> 16) & 0xFF}.{(int32 >> 8) & 0xFF}.{int32 & 0xFF}"