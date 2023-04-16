from typing import Optional
from typing import List
from binarytree import build

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

class BinaryTree:
    def generate_graph_list(self, nums : List[int]) -> Optional[int]:
        graph_list = []
        if len(nums) < 1: 
            return graph_list
        
        mid_index = len(nums) // 2
        graph_list.append(nums[mid_index])
        graph_list.append(nums[mid_index -1]) if 0 < mid_index else None
        graph_list.append(nums[len(nums) -1]) if len(nums) -1 > mid_index else None

        pos_left = 0
        pos_right = len(nums) - 2
        num_pos = 0

        while pos_left < (mid_index - 1):
            num_pos += 1
            is_even_pos = (num_pos % 2) == 0
            #left child
            if (is_even_pos) == 0:
                graph_list.append(nums[pos_left])
                graph_list.append(None)
            pos_left += 1

            #right child
            if not pos_right > mid_index:
                continue

            if (is_even_pos) == 0:
                graph_list.append(nums[pos_right])
                graph_list.append(None)
            pos_right -= 1

        return graph_list

    def balanced_tree_iterative(self, nums : List[int]) -> Optional[TreeNode]:
        if len(nums) < 1: 
            return None
        
        mid_index = len(nums) // 2

        #Initialize base tree
        root = TreeNode(nums[mid_index])
        root.left = TreeNode(nums[mid_index - 1]) if 0 < mid_index else None
        root.right = TreeNode(nums[len(nums) -1]) if len(nums) -1 > mid_index else None

        node_left = root.left
        node_right = root.right
        pos_left = 0
        pos_right = len(nums) - 2

        num_pos = 0
        while pos_left < (mid_index - 1):
            num_pos += 1
            is_even_pos = (num_pos % 2) == 0

            #left child
            if (is_even_pos) == 0:
                node_left.right = TreeNode(nums[pos_left])
                node_left = node_left.right
            else:
                node_left.left = TreeNode(nums[pos_left])
                node_left = node_left.left
            pos_left += 1

            #right child
            if not pos_right > mid_index:
                continue

            if (is_even_pos) == 0:
                node_right.right = TreeNode(nums[pos_right])
                node_right = node_right.right
            else:
                node_right.left = TreeNode(nums[pos_right])
                node_right = node_right.left
            pos_right -= 1

        return root

    def balanced_tree_recursive(self, nums : List[int]) -> Optional[TreeNode]:
        if len(nums) < 1: 
            return None

        mid_index = len(nums) // 2

        return TreeNode(nums[mid_index], self.balanced_tree_recursive(nums[:mid_index]), self.balanced_tree_recursive(nums[mid_index + 1:]))

    def print_binary_tree(self, nums):
        print(f'Input: nums = {nums}')
        print('Iterative Output: ',end='')
        root = self.balanced_tree_iterative(nums)
        if root:
            root.traverse_pre_order()
        else:
            print([])

        print('\nRecursive Output: ',end='')
        root = self.balanced_tree_recursive(nums)
        if root:
            root.traverse_pre_order()
        else:
            print([])
            print()

        #Generate Tree Graph for solution
        graph_list = self.generate_graph_list(nums)
        tree = build(graph_list)
        print(tree)