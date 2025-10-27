class Solution:
    def secondLargest(self, nums):
        # Remove duplicates using set
        unique_nums = set(nums)
        
        # If there are fewer than 2 unique numbers
        if len(unique_nums) < 2:
            return -1
        
        # Find largest and second largest in one pass
        first = second = float('-inf')
        for num in unique_nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        
        return second


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    
    sol = Solution()
    print(sol.secondLargest(nums))
