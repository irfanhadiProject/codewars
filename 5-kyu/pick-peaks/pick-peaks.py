def pick_peaks(arr):
    results =  {"pos": [], "peaks": []}
    pos_candidate = None
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            pos_candidate = i
        elif arr[i] < arr[i - 1] and pos_candidate is not None:
            results["pos"].append(pos_candidate)
            results["peaks"].append(arr[pos_candidate])
            pos_candidate = None
    
    return results
                