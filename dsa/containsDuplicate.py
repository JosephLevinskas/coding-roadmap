# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #Using set since we only need to know if one existed before
        for num in nums: #looping through list
            if num in seen: #See if number was seen already
                return True
            seen.add(num) #populate set
        return False

#Using a set works since we are checking existence instead of frequency otherwise we'd use a dict.
#Time complexity O(N) looping through whole list at most once 
#Space complexity O(N) storing whole list, no duplicates in worst case