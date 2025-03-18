class Solution:
    def isAnagram(s: str, t: str) -> bool:
        ls = []
        lt = []
        if(len(s)!=len(t)):
            return False
        for i in range(0,len(s)):
            ls.append(s[i])
            lt.append(t[i])
        ls.sort()
        lt.sort()
        if(ls==lt):
            return True
        else:
            return False
        
   
        
        
print(Solution.isAnagram_on("anagram","nagaram"))