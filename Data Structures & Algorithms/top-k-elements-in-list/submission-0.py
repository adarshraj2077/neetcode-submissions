class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        answer = []

        while len(answer) < k:
            for num, count in dict.items():
                if count == max(dict.values()):
                    answer.append(num)
                    break

            del dict[num]

        return answer