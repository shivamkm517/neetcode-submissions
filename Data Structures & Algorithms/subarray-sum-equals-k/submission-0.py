class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefixSum = {0:1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            count += prefixSum.get(diff, 0)
            prefixSum[curr_sum] = prefixSum.get(curr_sum, 0) + 1
        
        return count
