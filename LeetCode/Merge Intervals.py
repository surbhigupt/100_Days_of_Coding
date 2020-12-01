class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        L = len(intervals)
        intervals.sort()
        output = [intervals[0]]
        for i in range(1, L): 
            if (intervals[i][0]<=output[-1][1]<=intervals[i][1]) or (output[-1][0]<=intervals[i][0]<=output[-1][1]):
                output[-1][1]=max(output[-1][1], intervals[i][1])
                output[-1][0]=min(output[-1][0], intervals[i][0])
            else:
                output.append(intervals[i])
        
        return output
        