class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        i = 0
        j = len(nums)-1

        while i<j and i!=j:
            curr_sum = nums[i] + nums[j]

            if curr_sum == target:
                return [i,j]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
