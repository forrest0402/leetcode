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
    int GetDepth(TreeNode node, int height)
    {
        if (node == null)
            return height;
        return Math.Max(GetDepth(node.left, height + 1), GetDepth(node.right, height + 1));
    }
    bool Tranverse(TreeNode node)
    {
        if (node == null)
            return true;
        if (Math.Abs(GetDepth(node.left, 0) - GetDepth(node.right, 0)) > 1)
            return false;
        return Tranverse(node.left) && Tranverse(node.right);
    }
    public bool IsBalanced(TreeNode root)
    {
        return Tranverse(root);
    }
}