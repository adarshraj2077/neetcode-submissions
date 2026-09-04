class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = i+1

        while i<j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i+1,j+1]
            else:
                i += 1