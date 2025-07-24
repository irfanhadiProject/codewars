def dir_reduc(arr):
    stack = []
    for item in arr:
        if stack:
            if item == "NORTH" and stack[-1] == "SOUTH":
                stack.pop()
            elif item == "SOUTH" and stack[-1] == "NORTH":
                stack.pop()
            elif item == "EAST" and stack[-1] == "WEST":
                stack.pop()
            elif item == "WEST" and stack[-1] == "EAST":
                stack.pop()
            else:
                stack.append(item)
        else:
            stack.append(item)
    
    return stack
            
                
            