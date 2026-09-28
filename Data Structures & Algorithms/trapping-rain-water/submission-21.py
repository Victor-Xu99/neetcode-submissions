#input: array of integers which represent elevation
#output: total amount of water that can be trapped between bars
#questions: what sort of space and time complexity are we looking for here? would the array be strictly integers? what should be returned for an undefined array? What is the minimum length of the input array? 
#notes: total amount of water trapped b/w bars = difference of indices between bars * height of bars
#straightfoward: Left pointer at a height. Right pointer iterates through array until it encounters a height greater than or equal to first height. If height is lower -> add to in b/w tracker to later subtract from water volume. Once greater or equal to height encountered -> calculate water volume, add to total. left pointer moves to right pointer. Repeat until righter pointer reaches end of array
#optimal: Left pointer at beginning of array. Right pointer at end of array. Track leftmax and rightmax where left pointer and right pointer equal respective maxes initially. Move the pointer that is lesser in value first. Calculate possible water volume: Max - height[pointer]. If encounter value >= to other max. Switch to moving other pointer and change current max. repeat until pointers meet
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        totalWaterTrapped = 0
        leftMax = height[l]
        rightMax = height[r]
        while l != r:
            if leftMax < rightMax:
                l += 1
                currWater = max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                currWater = max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
            totalWaterTrapped += currWater
        return totalWaterTrapped


            
        
                


