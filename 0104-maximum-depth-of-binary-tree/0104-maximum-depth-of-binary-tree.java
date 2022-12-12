/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
//         edge case:
        if (root == null) {
        return 0;
    }
//         solving recursively, wil still work in asymetrical tree:
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}