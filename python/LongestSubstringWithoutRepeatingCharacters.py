#Given a string s, find the length of the longest substring without repeating characters.
   
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in char_map and start <= char_map[s[i]]:
                start = char_map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            char_map[s[i]] = i
        
        return max_length
