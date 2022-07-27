# TC: O(n + max(n)) where n is the len of the array and again iterating through the frequency array of len max(n).

# SC: O(max(n)) because we are creating a freq array of len max(n). 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq_array = [0] * (max(nums) + 1) # include zero
        
        for i in nums:
            freq_array[i] += i
            
        dp = []
        
        dp.append(freq_array[0])
        dp.append(max(freq_array[0], freq_array[1]))
        
        # bottom up (low to high) approach
        for i in range(2, len(freq_array)):
            dp.append(max(freq_array[i] + dp[i-2], dp[i-1]))
        
        return dp[-1]
        
        

        
        