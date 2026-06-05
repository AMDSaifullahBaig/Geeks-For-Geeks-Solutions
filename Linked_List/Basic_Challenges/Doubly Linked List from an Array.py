class Solution:
   def createDLL(self, arr):
     head=Node(arr[0])
     head.prev=None
     if len(arr)==1:
         head.next=None
         return head
     prev=head
     for i in range(1,len(arr)):
        curr=Node(arr[i])
        curr.prev=prev
        prev.next=curr
        prev=curr
     curr.next=None
     return head