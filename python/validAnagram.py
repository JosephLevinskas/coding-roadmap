
#Given two strings s and t, return true if t is an of s, and false otherwise.


def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #always check length first easy to get false right away
            return False

        freq = {} #build on frequency dictionary then cancel it out

        for char in s: #Build the dict using string 1
            freq[char] = freq.get(char, 0) + 1

        for char in t: #Compare string 2 to dict of string 1
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]

        return len(freq) == 0 #see if everything got cancelled out

#Space complexity O(N) because we build one dict. of size N-string
#Time complexity O(N + M) which is essentially O(N) since we loop through 2 strings fo size N + M