from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(x):
            t = deque(tasks[:x])
            w = workers[-x:]
            pills_left = pills
            i = x - 1

            for j in reversed(range(x)):
                task = t.pop()
                if w[i] >= task:
                    i -= 1
                    continue
                found = False
                for k in range(i + 1):
                    if w[k] + strength >= task:
                        pills_left -= 1
                        if pills_left < 0:
                            return False
                        w.pop(k)
                        i -= 1
                        found = True
                        break
                if not found:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
