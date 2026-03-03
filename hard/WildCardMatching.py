class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s==p or p=="*":
            return True
        i=0
        j=0

        lm=0
        st=-1
        while i<len(s):
            if j<len(p) and (s[i]==p[j] or p[j]=="?"):
                i+=1
                j+=1
            elif j<len(p) and p[j]=='*':
                lm=i
                st=j
                j+=1
            elif st!=-1:
                j=st+1
                i=lm+1
                lm+=1
            else:
                return False
        while j<len(p) and p[j]=="*":
            j+=1
        return j==len(p)