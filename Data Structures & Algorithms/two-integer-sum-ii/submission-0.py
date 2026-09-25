#input: array of numbers in non-decreasing order
#output: indices of 2 numbers that add up to target
#notes: indices returned should be 1-indexed; index1 < index2; index1 != index2
#questions: What do I return with an empty array? What do i return if there is no valid solution? Are duplicate values allowed in the array? Are the integers only positive?
#straighforward solution: go through array, compare each value to every other value until you find target. Violates space complexity requirement.
#optimal solution: Left and right pointer at each end of array. See if their sum equals target; if sum < target: move left pointer; if sum > target: move right pointer. Repeat until equal to target.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target: 
                r -= 1
        return [l + 1, r + 1]
    

                