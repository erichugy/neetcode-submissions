# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        # define lt function
        setattr(ListNode, "__lt__", lambda self, other: not self or self.val <= other.val)
        heapq.heapify(lists) 

        while lists:
            node = heapq.heappop(lists)
            if not node:
                continue

            next_node = node.next

            # Append
            curr.next = node
            node.next = None
            curr = curr.next

            # Heappush
            if next_node: 
                heapq.heappush(lists, next_node)
            
        return res.next
