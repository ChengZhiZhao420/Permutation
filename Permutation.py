class Solution(object):
    def permuteUnique(self, nums):
        result = []
        temp = []
        visit = [False] * len(nums)
        nums.sort()
        
        def generator(result, temp, visit, nums):
            if len(nums) == len(temp):
                result.append(temp[:])
                return
            
            for i in range(len(nums)):
                if visit[i] or (i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]):
                    continue
                
                temp.append(nums[i])
                visit[i] = True
                generator(result, temp, visit, nums)
                visit[i] = False
                temp.pop()
                
        generator(result, temp, visit, nums)     
        return result