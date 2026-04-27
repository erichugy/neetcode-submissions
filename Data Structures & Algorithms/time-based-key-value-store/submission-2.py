import collections
class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.hashmap[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if self.hashmap[key][mid][0] > timestamp:
                right = mid - 1
            else:
                res = self.hashmap[key][mid][1]
                left = mid + 1
        return res
        
