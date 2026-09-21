class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, l, r):
        result = []

        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1

        result.extend(l[i:])
        result.extend(r[j:])

        return result