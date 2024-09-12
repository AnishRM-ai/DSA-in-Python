def merge(intervals):
    intervals.sort(key = lambda interval : interval[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
    return merged

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))
arr = [[1,4],[4,5]]  
print(merge(arr))
#Time : O(n log n)
#Space : O(n)