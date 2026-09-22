class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sort_by_value = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))

        return list(sort_by_value.keys())[:k]