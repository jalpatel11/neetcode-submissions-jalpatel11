class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s):
            i=0
            j=len(s)-1
            while(i<j):
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if is_pal(sub):
                    path.append(sub)
                    dfs(end, path)
                    path.pop()
        
        dfs(0, [])
        return res
