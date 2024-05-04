class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first).len(last))):
            if(first[1]!=last[i]):
                return ans
            ans+=first[1]
        return ans