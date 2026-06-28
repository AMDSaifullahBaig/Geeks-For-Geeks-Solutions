class Solution:
    def getMiddle(self, head):
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow.next.data if fast.next else slow.data