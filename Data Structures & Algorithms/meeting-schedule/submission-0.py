"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last_end = 0

        intervals = sorted(intervals, key=lambda x: x.end) # earliest end time first

        for interval in intervals:
            if (interval.start < last_end): 
                return False
            last_end = interval.end
        
        return True
        
        