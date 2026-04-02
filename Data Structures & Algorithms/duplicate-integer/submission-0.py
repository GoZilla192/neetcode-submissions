class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seem_nums = set()

        for num in nums:
            if num in seem_nums:
                return True

            seem_nums.add(num)

        return False