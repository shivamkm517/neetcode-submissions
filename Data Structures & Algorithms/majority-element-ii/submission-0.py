class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, count1 = None, 0
        cand2, count2 = None, 0
        res = []

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -=1
                count2 -=1

        limit = len(nums)//3

        actual_count1 = nums.count(cand1) if count1 > 0 else 0
        actual_count2 = nums.count(cand2) if count2 > 0 else 0

        if actual_count1 > limit:
            res.append(cand1)
        if actual_count2 > limit and cand1 != cand2:
            res.append(cand2)

        return res

             