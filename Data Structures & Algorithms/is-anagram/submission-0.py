class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ans1={}
        ans2={}

        for i in range(len(s)):
            if s[i] not in ans1:
                ans1[s[i]]=1
            else:
                ans1[s[i]]+=1

            if t[i] not in ans2:
                ans2[t[i]]=1
            else:
                ans2[t[i]]+=1

        for i in ans1:
            if i not in ans2 or ans1[i] != ans2[i]:
                return False
        return True