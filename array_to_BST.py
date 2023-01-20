from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    
    def traverse_pre_order(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()


class Solution:
    def balanced_tree_iterative(self, nums : List[int]) -> Optional[TreeNode]:
        if len(nums) < 1: 
            return None
        
        mid_index = len(nums) // 2

        root = TreeNode(nums[mid_index])
        root.left = TreeNode(nums[mid_index - 1]) if 0 < mid_index else None
        root.right = TreeNode(nums[len(nums) -1]) if len(nums) -1 > mid_index else None

        node_left = root.left
        node_right = root.right
        pos_left = 0
        pos_right = len(nums) - 2

        while pos_left < (mid_index - 1):
            node_left.left = TreeNode(nums[pos_left])
            node_left = node_left.left
            pos_left += 1
            
            if pos_right > mid_index:
                node_right.right = TreeNode(nums[pos_right])
                node_right = node_right.right
                pos_right -= 1

        return root


    def balanced_tree_recursive(self, nums : List[int]) -> Optional[TreeNode]:
        if len(nums) < 1: 
            return None

        mid_index = len(nums) // 2

        return TreeNode(nums[mid_index], self.balanced_tree_recursive(nums[:mid_index]), self.balanced_tree_recursive(nums[mid_index + 1:]))

    def print_solution(self, nums):
        print(f'Input: nums = {nums}')
        print('Iterative Output: ',end='')
        root = self.balanced_tree_iterative(nums)
        if root:
            root.traverse_pre_order()
        print()
        print('Recursive Output: ',end='')
        root = self.balanced_tree_recursive(nums)
        if root:
            root.traverse_pre_order()


#TEST 1
print('-Test 1:')
nums = [-10,-3,0,5,9]
solution = Solution()
solution.print_solution(nums)


#TEST 2
print()
print('-Test 2:')
nums = [1,3]
solution = Solution()
solution.print_solution(nums)

#TEST 3
print()
print('-Test 3:')
nums = [1]
solution = Solution()
solution.print_solution(nums)

#TEST 4
print()
print('-Test 4:')
nums = [1,2,3,4]
solution = Solution()
solution.print_solution(nums)

#TEST 5
print()
print('-Test 5:')
nums = []
solution = Solution()
solution.print_solution(nums)

#TEST 6
print()
print('-Test 6:')
nums = [1,2,3]
solution = Solution()
solution.print_solution(nums)