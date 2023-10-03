def insertAndMerge(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example usage:
intervals1 = [[1, 5], [6, 9]]
newInterval1 = [2, 5]
result1 = insertAndMerge(intervals1, newInterval1)
print(result1)

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 9]
result2 = insertAndMerge(intervals2, newInterval2)
print(result2)
