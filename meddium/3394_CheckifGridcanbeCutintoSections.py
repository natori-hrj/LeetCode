class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        def can_cut_along_axis(intervals):
            intervals.sort()
            parts = []
            c_min = intervals[0][0]
            c_max = intervals[0][1]

            for start, end in intervals[1:]:
                if start >= c_max:
                    parts.append((c_min, c_max))
                    c_min = start
                    c_max = end
                else:
                    c_max = max(c_max, end)
            
            parts.append((c_min, c_max))

            return len(parts) >= 3
        
        x_intervals = [[x1, x2] for x1, y1, x2, y2 in rectangles]
        if can_cut_along_axis(x_intervals):
            return True
        
        y_intervals = [[y1, y2] for x1, y1, x2, y2 in rectangles]
        if can_cut_along_axis(y_intervals):
            return True
        
        return False

n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

s = Solution()
print(s.checkValidCuts(n, rectangles))
