class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        without_duplicates=set(nums)
        if len(nums)!=len(without_duplicates):
            return True
        return False
        