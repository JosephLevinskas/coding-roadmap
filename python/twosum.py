# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.


def twoSum(self, nums: List[int], target: int) -> List[int]:   # Populate dictionary with opposite number then return indices of both
    seen = {} # dictionary to populate with number and it's index
    for i, num in enumerate(nums): # loop over each element
        remainder = target - num # find the remainder using current value
        if remainder in seen: #look to see if there is a matching pair in the dict we've seen before
            l = [seen[remainder], i] #if there is a matching pair make list with index of both numbers
            return l 
        seen[num] = i # Else place current value in dict. not using the remainder value

#Big(O) 
#Hashmap look up is O(1)
#Single pass at worst is O(N)
#worst case O(N)
#space complexity O(N) for dictionary
