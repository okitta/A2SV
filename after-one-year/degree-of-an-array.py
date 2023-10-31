class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = max(count.values())
        elements = set()
        for item,value in count.items():
            if value == max_count:
                elements.add(item)
        dic = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in elements:
                dic[nums[i]].append(i)
                
        min_dist = len(nums)

        for value in dic.values():
            min_dist = min(min_dist,(value[-1]-value[0])+1)

        return min_dist