def create_phone_number(n):
    template = "({}{}{}) {}{}{}-{}{}{}{}"
    result = template.format(*n)
    
    return result