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
    private bool Tranverse(TreeNode node, int cur, int sum)
    {
        if (node == null)
            return false;
        cur += node.val;
        if (node.left == null && node.right == null)
        {
            return cur == sum;
        }
        return Tranverse(node.left, cur, sum) || Tranverse(node.right, cur, sum);
    }
    public bool HasPathSum(TreeNode root, int sum)
    {
        return Tranverse(root, 0, sum);
    }
}