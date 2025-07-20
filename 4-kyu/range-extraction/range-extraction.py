def solution(args):
    result = []
​
    while args:
        start = args.pop(0)
        temp = [start]
​
        while args and args[0] == temp[-1] + 1:
            temp.append(args.pop(0))
​
        if len(temp) >= 3:
            result.append(f"{temp[0]}-{temp[-1]}")
        else:
            result.extend(str(x) for x in temp)
​
    return ",".join(result)