class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        
        meetings.sort()
        print(meetings)

        merged = [meetings[0]]
        print(merged)

        for curr_start, curr_end in meetings[1:]:
            last_start, last_end = merged[-1]

            if curr_start <= last_end:
                 merged[-1][1] = max(last_end, curr_end)
            else:
                merged.append([curr_start, curr_end])

        
        todal_meetings_days = 0
        for start, end in merged:
            todal_meetings_days += (end - start + 1)


        return days - todal_meetings_days     

        
    

days = 10
meetings = [[5,7],[1,3],[9,10]]

s = Solution()
print(s.countDays(days, meetings))


