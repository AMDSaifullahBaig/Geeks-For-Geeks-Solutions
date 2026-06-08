class Solution:
    def compute(self,head):
        def reverse(root):
            prev=None
            curr=root
            while curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        reversed=reverse(head)
        curr=reversed
        while curr and curr.next:
            if curr.data>curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return reverse(reversed)