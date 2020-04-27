'''
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)
'''

def pair_sum(arr, sum):
    if len(arr) < 2:
        return ()
    seen = []
    result = []
    for i in arr:
        target = sum - i
        if target in seen:
            # result.append((i, target))
            result.append((min(i, target), max(i, target)))
        else:
            seen.append(i)
    return result