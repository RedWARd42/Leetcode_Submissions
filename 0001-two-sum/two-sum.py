class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            compli = target - nums[i]
            if compli in hashmap:
                return [i, hashmap[compli]]
            if compli not in hashmap:
                hashmap[nums[i]] = i

        
        
    