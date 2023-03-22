class Solution:
		def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
			presum=ans=0
			store={}
			for n in nums:
				if presum in store: store[presum]+=1
				else:store[presum]=1
				presum+=n
				if presum-goal in store:            
					ans+=store[presum-goal]      

			return ans