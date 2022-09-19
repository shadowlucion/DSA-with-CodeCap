class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        
        mx = arr[0]
        mn = arr[0]
        ans = arr[0]
        for i in range(1,n):
            el = arr[i]
            c1 = el
            c2 = el*mn
            c3 = el*mx
            mx = max(c1,c2,c3)
            mn = min(c1,c2,c3)
            ans = max(ans,mx)
        return ans
