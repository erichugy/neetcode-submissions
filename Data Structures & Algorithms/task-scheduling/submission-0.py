class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqs = [-x for x in Counter(tasks).values()]
        heap = heapq.heapify(freqs)

        timeout = []

        time = 0
        while freqs or timeout:
            time += 1

            while (timeout and timeout[0][1] <= time):
                heapq.heappush(freqs, timeout.pop(0)[0])

            if freqs:
                val = heapq.heappop(freqs) + 1
                if val:
                    timeout.append((val, time + n + 1))

        return time


