from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
     mapping = defaultdict(list)
     output = [] 

     for s in strs:
        sorted_s = tuple(sorted(s))
        mapping[sorted_s].append(s)

     for value in mapping.values():
        output.append(value)

     return output
