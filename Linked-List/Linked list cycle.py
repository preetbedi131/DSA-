# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        visited =set()
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False



"""method - 2

. Floyd’s Cycle Detection (Tortoise & Hare) 🐢🐇 → O(1) space ✅

We use two pointers:

slow moves one step at a time.

fast moves two steps at a time.

If there’s a cycle, slow and fast will eventually meet inside the cycle.
If fast reaches None, no cycle exists."""

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:  # fast can jump 2 steps safely
            slow = slow.next       # move 1 step
            fast = fast.next.next  # move 2 steps

            if slow == fast:       # cycle detected
                return True

        return False  # reached end → no cycle

