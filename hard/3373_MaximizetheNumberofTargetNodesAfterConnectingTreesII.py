from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph
        
        def get_bipartite_groups(graph, n):
            if n == 0:
                return [], []
            
            color = [-1] * n
            queue = deque([0])
            color[0] = 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
            
            group0 = []
            group1 = []
            for i in range(n):
                if color[i] == 0:
                    group0.append(i)
                else:
                    group1.append(i)
            
            return group0, group1
        
        def count_targets_for_each_node(graph, n):
            group0, group1 = get_bipartite_groups(graph, n)
            
            targets = [0] * n
            
            for node in group0:
                targets[node] = len(group0)
            
            for node in group1:
                targets[node] = len(group1)
            
            return targets
        
        graph1 = build_graph(edges1)
        graph2 = build_graph(edges2)
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        tree1_targets = count_targets_for_each_node(graph1, n)
        
        group0_tree2, group1_tree2 = get_bipartite_groups(graph2, m)
        
        max_from_tree2 = max(len(group0_tree2), len(group1_tree2))
        
        result = []
        for i in range(n):
            result.append(tree1_targets[i] + max_from_tree2)
        
        return result