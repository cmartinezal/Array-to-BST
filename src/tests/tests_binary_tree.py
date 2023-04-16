from typing import Optional
from typing import List
from binarytree import build
from ..binary_tree import BinaryTree

def test_1():
    tree = BinaryTree()
    print('- Test 1:')
    nums = [-10,-3,0,5,9]
    tree.print_binary_tree(nums)

def test_2():
    tree = BinaryTree()
    print('- Test 2:')
    nums = [1,3]
    tree.print_binary_tree(nums)

def test_3():
    tree = BinaryTree()
    print('- Test 3:')
    nums = [1]
    tree.print_binary_tree(nums)

def test_4():
    tree = BinaryTree()
    print('- Test 4:')
    nums = [1,2,3,4,5]
    tree.print_binary_tree(nums)

def test_5():
    tree = BinaryTree()
    print('- Test 5:')
    nums = []
    tree.print_binary_tree(nums)

def test_6():
    tree = BinaryTree()
    print('- Test 6:')
    nums = [1,2,3]
    tree.print_binary_tree(nums)

def run_tests():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
