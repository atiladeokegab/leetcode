# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # - 🔍 1. Understand the Problem
        # - 🧠 2. Restate the Problem in Your Own Words
        # - 🧪 3. Work Through Examples
        # - 🧱 4. Identify the Core Idea
        # - 🧮 5. Think About the Brute Force Approach
        # - ⚙️ 6. Plan the Solution
        # - 💻 7. Code It Cleanly
        # - ✅ 8. Test Thoroughly
        # - ⏱️ 9. Analyze Time and Space Complexity
        # - 💬 10. Reflect & Optimize
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

# ---------- Helper Functions ----------
def print_tree(root: Optional[TreeNode]):
    """Level order print of tree"""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# ---------- Testing ----------
if __name__ == "__main__":
    # Example usage
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))

    sol = Solution()
    print("Original tree:", print_tree(root))
    inverted = sol.invertTree(root)
    print("Inverted tree:", print_tree(inverted))

    # ---------- Automated Tests ----------
    def test_invert_tree():
        # Test 1: Invert back to original
        root2 = TreeNode(4)
        root2.left = TreeNode(2, TreeNode(1), TreeNode(3))
        root2.right = TreeNode(7, TreeNode(6), TreeNode(9))
        inverted_again = sol.invertTree(inverted)
        try:
            assert print_tree(inverted_again) == print_tree(root2), \
                f"Expected {print_tree(root2)}, got {print_tree(inverted_again)}"
            print("Test 1 passed: Inverting twice returns original tree")
        except AssertionError as e:
            print("Test 1 failed:", e)

        # Test 2: Single node tree
        single = TreeNode(5)
        inverted_single = sol.invertTree(single)
        try:
            assert print_tree(inverted_single) == [5], \
                f"Expected [5], got {print_tree(inverted_single)}"
            print("Test 2 passed: Single node tree remains unchanged")
        except AssertionError as e:
            print("Test 2 failed:", e)

        # Test 3: Empty tree
        empty = None
        inverted_empty = sol.invertTree(empty)
        try:
            assert inverted_empty is None, f"Expected None, got {inverted_empty}"
            print("Test 3 passed: Empty tree returns None")
        except AssertionError as e:
            print("Test 3 failed:", e)

    test_invert_tree()