class Solution:    
    def overlappingIntervals(self, intervals):
        intervals.sort(key=lambda x: x[0])
        my_stack = []
        my_stack.append(intervals[0])
        for i in intervals[1:]:
            if i[0] >= my_stack[-1][0] and i[0] <= my_stack[-1][1]:
                my_stack[-1][1] = max(my_stack[-1][1], i[1])
            else:
                my_stack.append(i)
        return my_stack
