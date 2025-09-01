def solution(args):
    if not args:
        return ""
​
    res = []
    start = args[0]
    count = 1
​
    for i in range(1, len(args)):
        if args[i] == args[i - 1] + 1:
            count += 1
        else:
            finish = args[i - 1]
            if count >= 3:
                res.append(f"{start}-{finish}")
            elif count == 2:
                res.append(str(start))
                res.append(str(finish))
            else:
                res.append(str(start))
            start = args[i]
            count = 1
​
           
    finish = args[-1]
    if count >= 3:
        res.append(f"{start}-{finish}")
    elif count == 2:
        res.append(str(start))
        res.append(str(finish))
    else:
        res.append(str(start))
​
    return ",".join(res)
            
            
        
        