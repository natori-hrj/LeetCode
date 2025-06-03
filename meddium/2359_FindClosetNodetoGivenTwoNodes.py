from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            distances = {}
            visited = set()
            current = start
            dist = 0
            
            while current != -1 and current not in visited:
                distances[current] = dist
                visited.add(current)
                current = edges[current]
                dist += 1
            
            return distances
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        common_nodes = set(dist1.keys()) & set(dist2.keys())
        
        if not common_nodes:
            return -1
        
        min_max_dist = float('inf')
        result = -1
        
        for node in common_nodes:
            max_dist = max(dist1[node], dist2[node])
            
            if max_dist < min_max_dist or (max_dist == min_max_dist and node < result):
                min_max_dist = max_dist
                result = node
        
        return result