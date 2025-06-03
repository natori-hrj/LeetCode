class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:        
        def combination(n, k):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            
            return self.stars_and_bars(n, k)
        
        def stars_and_bars(total, groups):
            if total < 0:
                return 0
            
            n = total + groups - 1
            k = groups - 1
            
            if k < 0 or k > n:
                return 0
            
            if k > n - k:
                k = n - k
            
            result = 1
            for i in range(k):
                result = result * (n - i) // (i + 1)
            
            return result
        
        total = stars_and_bars(n, 3)
        
        subtract_one = 3 * stars_and_bars(n - (limit + 1), 3)
        
        add_two = 3 * stars_and_bars(n - 2 * (limit + 1), 3)
        
        subtract_three = stars_and_bars(n - 3 * (limit + 1), 3)
        
        return total - subtract_one + add_two - subtract_three
