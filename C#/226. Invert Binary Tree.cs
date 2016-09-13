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
    public TreeNode InvertTree(TreeNode root)
    {
        if (root == null)
            return null;
        TreeNode tempNode = root.left;
        root.left = root.right;
        root.right = tempNode;
        root.left = InvertTree(root.left);
        root.right = InvertTree(root.right);
        return root;
    }
}