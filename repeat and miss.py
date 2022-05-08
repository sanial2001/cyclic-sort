class Solution:
    def cycle(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[nums[i] - 1] == nums[i]:
                i += 1
            else:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        return nums

    def findErrorNums(self, nums):
        cycle_nums = self.cycle(nums)
        # print(nums)
        n = len(nums)
        res = [-1 for _ in range(2)]

        for i in range(n):
            if cycle_nums[i] != i + 1:
                res[1] = i + 1
                res[0] = cycle_nums[i]
        print(res)


if __name__ == '__main__':
    arr = [1, 3, 4, 4, 2]
    Solution().findErrorNums(arr)