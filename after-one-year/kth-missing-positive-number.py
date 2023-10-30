class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        storage = []
        check = set(arr)
        for i in range(1,arr[-1]+1):
            if i not in check:
                storage.append(i)
        if k <= len(storage):
            return storage[k-1]
        # print(len)
        return arr[-1] + (k-len(storage))