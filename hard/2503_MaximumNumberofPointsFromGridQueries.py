class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        qlen = len(queries)

        parent = {}
        size = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))

        cells.sort()

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        res = [0] * len(queries)

        seen = [[False] * n for _ in range(m)]
        deirections = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        i = 0
        count = 0

        for q, idx in sorted_queries:
            while i < len(cells) and cells[i][0] < q:
                _, r, c = cells[i]
                i += 1
                key = r * n + c
                parent[key] = key
                size[key] = 1
                seen[r][c] = True
                for dr, dc in deirections:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and seen[nr][nc]:
                        union(key, nr * n + nc)

            if seen[0][0]:
                root = find(0)
                res[idx] = size[root]
            else:
                res[idx] = 0

        return res
    

grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]

s = Solution()
print(s.maxPoints(grid, queries))