class Solution:
    def firstMissingPositive(self, nums):
        i, n = 0, len(nums)
        '''
        while i < n:
            if nums[i] == i+1 or nums[i] < 0 or nums[i] > n:
                i = i + 1
            else:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
        print(nums)
        '''

        for i in range(n):
            if nums[i] != i+1 and 0 < nums[i] <= n:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
                i = i-1
        print(nums)

        for i in range(n):
            if nums[i] != i+1:
                print(i+1)


if __name__ == '__main__':
    arr = [3, 4, -1, 1]
    Solution().firstMissingPositive(arr)
