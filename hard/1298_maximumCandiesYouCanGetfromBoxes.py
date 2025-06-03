from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        
        have_keys = set()
        have_boxes = set(initialBoxes)
        opened = set()
        
        queue = deque()
        
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
        
        total_candies = 0
        
        while queue:
            current_box = queue.popleft()
            
            if current_box in opened:
                continue
                
            opened.add(current_box)
            total_candies += candies[current_box]
            
            for key in keys[current_box]:
                have_keys.add(key)
            
            for box in containedBoxes[current_box]:
                have_boxes.add(box)
            
            for key in keys[current_box]:
                if key in have_boxes and key not in opened:
                    queue.append(key)
            
            for box in containedBoxes[current_box]:
                if (status[box] == 1 or box in have_keys) and box not in opened:
                    queue.append(box)
        
        return total_candies
    
    def maxCandies_optimized(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        
        have_keys = set()
        have_boxes = set(initialBoxes)
        opened = [False] * n
        
        queue = deque()
        total_candies = 0
        
        def try_open_boxes():
            nonlocal total_candies
            opened_any = True
            
            while opened_any:
                opened_any = False
                boxes_to_remove = []
                
                for box in list(have_boxes):
                    if not opened[box] and (status[box] == 1 or box in have_keys):
                        opened[box] = True
                        total_candies += candies[box]
                        opened_any = True
                        
                        have_keys.update(keys[box])
                        
                        have_boxes.update(containedBoxes[box])
        
        try_open_boxes()
        return total_candies

class DetailedSolution:
    def maxCandies_with_explanation(self, status, candies, keys, containedBoxes, initialBoxes):
        print(f"初期箱: {initialBoxes}")
        print(f"箱の状態: {status}")
        print(f"キャンディ数: {candies}")
        print(f"鍵: {keys}")
        print(f"含まれる箱: {containedBoxes}")
        print("=" * 50)
        
        have_keys = set()
        have_boxes = set(initialBoxes)
        opened = set()
        queue = deque()
        total_candies = 0
        step = 1
        
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
        
        print(f"初期に開けられる箱: {list(queue)}")
        
        while queue:
            current_box = queue.popleft()
            
            if current_box in opened:
                continue
            
            print(f"\nStep {step}: 箱{current_box}を開ける")
            opened.add(current_box)
            total_candies += candies[current_box]
            print(f"  キャンディ獲得: {candies[current_box]} (合計: {total_candies})")
            
            new_keys = keys[current_box]
            if new_keys:
                have_keys.update(new_keys)
                print(f"  新しい鍵: {new_keys}")
                print(f"  持っている鍵: {have_keys}")
            
            new_boxes = containedBoxes[current_box]
            if new_boxes:
                have_boxes.update(new_boxes)
                print(f"  新しい箱: {new_boxes}")
                print(f"  持っている箱: {have_boxes}")
            
            newly_openable = []
            
            for key in new_keys:
                if key in have_boxes and key not in opened:
                    queue.append(key)
                    newly_openable.append(key)
            
            for box in new_boxes:
                if (status[box] == 1 or box in have_keys) and box not in opened:
                    queue.append(box)
                    newly_openable.append(box)
            
            if newly_openable:
                print(f"  次に開けられる箱: {newly_openable}")
            
            step += 1
        
        print(f"\n最終結果: {total_candies}個のキャンディ")
        return total_candies
