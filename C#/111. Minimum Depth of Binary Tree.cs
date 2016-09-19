/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution
{
    int GetDepth(TreeNode root)
    {
        if (root == null)
            return 0;
        if (root.left == null)
            return GetDepth(root.right) + 1;
        if (root.right == null)
            return GetDepth(root.left) + 1;
        return Math.Min(GetDepth(root.left), GetDepth(root.right)) + 1;
    }
    public int MinDepth(TreeNode root)
    {
        return GetDepth(root);
    }
}