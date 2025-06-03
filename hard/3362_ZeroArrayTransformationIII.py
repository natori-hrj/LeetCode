import heapq

class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        num_total_queries = len(queries)

        queries_starting_at_l = [[] for _ in range(n)]
        for l_orig, r_orig in queries:
            if 0 <= l_orig < n:
                 queries_starting_at_l[l_orig].append((r_orig, l_orig))

        memo_check = {}

        def check(k_queries_to_use: int) -> bool:
            if k_queries_to_use < 0:
                return False
            if k_queries_to_use in memo_check:
                return memo_check[k_queries_to_use]

            queries_used_count = 0
            coverage_effect = [0] * (n + 1) 
            
            active_query_candidates_pq = [] 
            
            current_sum_of_coverage_effects = 0 

            for i in range(n):
                if i < len(queries_starting_at_l):
                    for r_orig, l_orig_from_tuple in queries_starting_at_l[i]:
                        heapq.heappush(active_query_candidates_pq, (-r_orig, l_orig_from_tuple))
                
                current_sum_of_coverage_effects += coverage_effect[i]

                while current_sum_of_coverage_effects < nums[i]:                    
                    while active_query_candidates_pq and -active_query_candidates_pq[0][0] < i:
                         heapq.heappop(active_query_candidates_pq)

                    if not active_query_candidates_pq:
                        memo_check[k_queries_to_use] = False
                        return False 
                    
                    neg_r_chosen, l_chosen = heapq.heappop(active_query_candidates_pq)
                    r_chosen = -neg_r_chosen

                    queries_used_count += 1
                    if queries_used_count > k_queries_to_use:
                        memo_check[k_queries_to_use] = False
                        return False
                    
                    coverage_effect[l_chosen] += 1
                    if r_chosen + 1 <= n: 
                        coverage_effect[r_chosen + 1] -= 1
                    
                    current_sum_of_coverage_effects += 1 
            
            memo_check[k_queries_to_use] = True
            return True

        if not check(num_total_queries):
            return -1

        ans_min_k_needed = num_total_queries 
        low = 0
        high = num_total_queries 

        while low <= high:
            mid_k = low + (high - low) // 2
            if check(mid_k):
                ans_min_k_needed = mid_k
                high = mid_k - 1 
            else:
                low = mid_k + 1
        
        return num_total_queries - ans_min_k_needed