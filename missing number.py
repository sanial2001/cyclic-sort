class Solution:
    def missingNumber(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == len(nums) or nums[i] == i:
                i = i + 1
            else:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp

        for i, val in enumerate(nums):
            if i != val:
                print(i)
        print(i+1)


if __name__ == '__main__':
    arr = [3, 4, -1, 1]
    Solution().missingNumber(arr)
