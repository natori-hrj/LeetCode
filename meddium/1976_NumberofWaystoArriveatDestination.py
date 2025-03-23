class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        import heapq

        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        
        min_time = [float('inf')] * n
        ways = [0] * n
        min_time[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            curr_time, node = heapq.heappop(pq)

            if curr_time > min_time[node]:
                continue

            for neighbor, t in graph[node]:
                new_time = curr_time + t

                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))

                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
    
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

s = Solution()
print(s.countPaths(n, roads))
