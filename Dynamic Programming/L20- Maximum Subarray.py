class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        n = len(arr)
        temp = arr[0]
        mx = arr[0]
        for i in range(1,n):
            c1 = arr[i]
            c2 = temp+arr[i]
            temp = max(c1,c2)
            mx = max(mx,temp)
        return mx
