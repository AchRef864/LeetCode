#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_s_list = sorted(list(map(ord, list(s))))
        ascii_t_list = sorted(list(map(ord, list(t))))
        if ascii_s_list != ascii_t_list:
            return False
        return True
