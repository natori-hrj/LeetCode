import heapq
import math

class Solution:
  def minTimeToReach(self, moveTime: list[list[int]]) -> int:
    return self._dijkstra(
      moveTime,
      start=(0, 0),
      goal=(len(moveTime) - 1, len(moveTime[0]) - 1)
    )

  def _dijkstra(
      self,
      moveTime: list[list[int]],
      start: tuple[int, int],
      goal: tuple[int, int]
  ) -> int:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    rows, cols = len(moveTime), len(moveTime[0])
    dist = [[math.inf] * cols for _ in range(rows)]

    dist[start[0]][start[1]] = 0
    heap = [(0, start)]

    while heap:
      currTime, (i, j) = heapq.heappop(heap)
      if (i, j) == goal:
        return currTime
      if currTime > dist[i][j]:
        continue

      for dx, dy in DIRS:
        x, y = i + dx, j + dy
        if 0 <= x < rows and 0 <= y < cols:
          move_cost = (i + j) % 2 + 1
          arrive_time = max(currTime, moveTime[x][y]) + move_cost
          if arrive_time < dist[x][y]:
            dist[x][y] = arrive_time
            heapq.heappush(heap, (arrive_time, (x, y)))

    return -1
