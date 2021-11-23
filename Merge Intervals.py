class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda interval:interval[0]) #T: O(NlogN) S: O(logN)
        end = 0
        for i in range(len(intervals)): #O(N)
            interval = intervals[i]
            if intervals[end][1] >= interval[0]:
                intervals[end][1] = max(intervals[end][1],interval[1])
            else:
                end += 1
                intervals[end] = interval
                    
        return intervals[:end+1]
