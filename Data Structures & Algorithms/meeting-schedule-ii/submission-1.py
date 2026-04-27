"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        counter = 0
        intervals = sorted(intervals, key = lambda x : x.end)
        while True:
            n = len(intervals)
            if not n: break

            counter += 1
            last_avail = 0

            while n:
                interval = intervals.pop(0)
                if last_avail > interval.start:
                    intervals.append(interval)
                else:
                    last_avail = interval.end
                n -= 1
        return counter

