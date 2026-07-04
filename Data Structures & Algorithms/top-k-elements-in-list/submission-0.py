from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr=Counter(nums)
        common=ctr.most_common(k)
        return [item[0] for item in common]