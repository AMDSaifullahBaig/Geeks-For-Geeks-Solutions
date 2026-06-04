class Solution:
    def search(self, arr, x):
        try:
            return arr.index(x)
        except Exception:
            return -1