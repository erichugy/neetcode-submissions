import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        maxHeap = []

        for n in nums:
            freqs[n] += 1
        print(freqs)
        i = 0
        for key,val in freqs.items():
            # print(f'before ({key}, {val}): {maxHeap}')
            if i < k:
                heapq.heappush(maxHeap, (val, key))
                i += 1
            else: 
                heapq.heappushpop(maxHeap, (val, key))
            # print(f'after {maxHeap}')
        
        return [b for a,b in maxHeap]
        
        
        

