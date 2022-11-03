class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      if len(s) < len(p):
        return []
      
      charToCountMap = {}
      no_of_char_matches = 0
      target_char_matches = len(set(p))
      
      res = []
      
      for n in p:
        charToCountMap[n] = charToCountMap.get(n, 0) + 1
        
      l, r = 0, len(p) - 1
      for i in range(l, r+1):
        c = s[i]
        if c in charToCountMap:
          charToCountMap[c] -= 1
          if charToCountMap[c] == 0:
            no_of_char_matches += 1
          if no_of_char_matches == target_char_matches:
            res.append(l)
      
      l += 1
      r += 1
      
      while r < len(s):
        pre = s[l-1]
        post = s[r]
        
        if pre in charToCountMap:
          charToCountMap[pre] += 1
          if charToCountMap[pre] == 1:
            no_of_char_matches -= 1
        if post in charToCountMap:
          charToCountMap[post] -= 1
          if charToCountMap[post] == 0:
            no_of_char_matches += 1
        
        if no_of_char_matches == target_char_matches:
          res.append(l)
        
        l += 1
        r += 1
      
      return res