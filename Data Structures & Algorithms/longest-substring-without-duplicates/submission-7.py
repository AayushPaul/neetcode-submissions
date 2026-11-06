class Solution:
    # Time: 10:14 - 11:07
    def lengthOfLongestSubstring(self, s: str) -> int:
        #U: Find the length of the longest substring without duplicate chars 

        #M/P: Hashset to keep track of any duplicates encountered, use the max python function, and two pointers to keep track of the length of current substring/window
        # Hint: sliding window method 

        #I: 
        hashset = set() 
        length = 0 
        left, right = 0, 0 

        for char in s: 
            while char in hashset: 
                hashset.remove(s[left]) 
                left += 1

            hashset.add(char) 
            length = max(length, right - left + 1)
            right += 1
        
        return length

        #R: 
            # s = "abcdec" 
            # hashset/window = {d, e, c}
            # length = 5
            
        #E: Time: O(n), Space: O(n) or O(1) 
            # Another good answer is O(1) for Space Complexity, as number of possible unique characters is strictly bounded (e.g., 128 for standard ASCII or 256 for extended ASCII); the hashset can never grow larger than that constant number, no matter how long the string gets.