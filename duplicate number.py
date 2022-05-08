class Solution:
    def findDuplicate(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i+1 or nums[nums[i]-1] == nums[i]:
                i = i+1
            else:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp

        print(nums[-1])


if __name__ == '__main__':
    arr = [1,1]
    Solution().findDuplicate(arr)