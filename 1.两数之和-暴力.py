from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                s = nums[i] + nums[j]
                if s == target and i != j:
                    result.append(i)
                    result.append(j)
        return result


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]


nums = [2,7,11,15]
target = 9
t = Solution2()
print(t.twoSum(nums,target))