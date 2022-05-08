class Solution:
    def findDisappearedNumbers(self, nums):
        i, ans = 0, []
        while i < len(nums):
            if nums[i] == i+1 or nums[nums[i]-1] == nums[i]:
                i = i+1
            else:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp

        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)

        print(ans)


if __name__ == '__main__':
    arr = [4,3,2,7,8,2,3,1]
    Solution().findDisappearedNumbers(arr)