class Solution:
    def maxLevelSum(self, root):
        if not root:return 0
        maximum=root.data
        queue=deque([root])
        while queue:
            add=0
            for i in range(len(queue)):
                e=queue.popleft()
                if e.left:
                    queue.append(e.left)
                    add+=e.left.data
                if e.right:
                    queue.append(e.right)
                    add+=e.right.data
            maximum=max(maximum,add)
        return maximum