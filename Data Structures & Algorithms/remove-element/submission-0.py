class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        deleted = 0
        n = len(nums)

        for i in range(n):
            i = i - deleted

            if nums[i] == val:
                deleted += 1
                nums.pop(i)

        return n - deleted 