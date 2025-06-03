class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
    
    def candy_one_pass_optimized(self, ratings):
        n = len(ratings)
        if n <= 1:
            return n
        
        total = 1
        up = 0
        down = 0
        peak = 0
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                up += 1
                down = 0
                peak = up + 1
                total += peak
            elif ratings[i] < ratings[i-1]:
                up = 0
                down += 1
                total += down + (1 if down >= peak else 0)
            else:
                up = down = peak = 0
                total += 1
        
        return total

class DetailedSolution:
    def candy_with_explanation(self, ratings):
        n = len(ratings)
        candies = [1] * n
        
        print(f"初期状態: {candies}")
        print(f"評価: {ratings}")
        
        print("\n=== 左から右へのパス ===")
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                print(f"位置{i}: 評価{ratings[i]} > 評価{ratings[i-1]} → キャンディ{candies[i]}")
        
        print(f"左→右後: {candies}")
        
        print("\n=== 右から左へのパス ===")
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                new_candy = candies[i+1] + 1
                if new_candy > candies[i]:
                    candies[i] = new_candy
                    print(f"位置{i}: 評価{ratings[i]} > 評価{ratings[i+1]} → キャンディ{candies[i]}")
        
        print(f"右←左後: {candies}")
        print(f"合計: {sum(candies)}")
        
        return sum(candies)
