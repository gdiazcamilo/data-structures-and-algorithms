def merge(intervals) :
    """
    Intervals A and B are overlapped when:
    A        [---]
    B    [-------]
    
    1. start of B <= end of A and end of A is <= than end of B
        new interval = start of A, end of B
    2. start of A <= end of B and end of B is <= than end of A
        new interval = start of B, end of A
        
    
    Check each interval.
    Compare each interval with the non-overlapped intervals.
    If the interval is overlapped with one of the non-overlapped intervals, then merge it with the non-overlapped.
    
    """
    
    
    non_overlappeds = []
    for interval_A in intervals:
        
        A_start, A_end = interval_A
        
        is_overlapped = False
        for B_idx, interval_B in enumerate(non_overlappeds):
            # check if they are overlapped
            
            B_start, B_end = interval_B
            
            if A_start <= B_end and B_end <= A_end:
                A_start = min(A_start, B_start)
                A_end = max(A_end, B_end)
                is_overlapped = True
                # modify non_overlapped in index of B
                non_overlappeds[B_idx] = [A_start, A_end]
                
            elif B_start <= A_end and A_end <= B_end:
                A_start = min(A_start, B_start)
                A_end = max(A_end, B_end)
                is_overlapped = True
                # modify non_overlapped in index of B
                non_overlappeds[B_idx] = [A_start, A_end]
            
        if not is_overlapped:
            non_overlappeds.append([A_start, A_end])
        
    result = set()
    for i in non_overlappeds:
        result.add( (i[0], i[1]) )
    return result


print(merge([[1,3],[4,8],[0,18]]))
