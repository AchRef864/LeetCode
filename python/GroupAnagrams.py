#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def frequency_array(s):
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            return freq
        total_list = []
        freq_list = []
        for string in strs:
            freq = frequency_array(string)
            found = False
            for i in range(len(freq_list)):
                if freq == freq_list[i]:
                    total_list[i].append(string)
                    found = True
                    break
            if not found:
                total_list.append([string])
                freq_list.append(freq)
        return total_list
