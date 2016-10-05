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
    private int GetNum(TreeNode node, int k, out bool flag)
    {
        if (node == null)
        {
            flag = false;
            return 0;
        }
        if (k == 1)
        {
            flag = true;
            return node.val;
        }
        int nl = GetNum(node.left, k - 1, out flag);
        if (flag)
            return nl;
        if (nl + 1 == k)
        {
            flag = true;
            return node.val;
        }
        int nr = GetNum(node.right, k - nl - 1, out flag);
        if (flag)
            return nr;
        return nl + nr + 1;
    }
    public int KthSmallest(TreeNode root, int k)
    {
        if (root.left == null && root.right == null)
            return root.val;
        bool flag;
        int n = GetNum(root.left, k, out flag);
        if (flag)
            return n;
        if (k - n - 1 == 0)
            return root.val;
        return KthSmallest(root.right, k - n - 1);
    }
}