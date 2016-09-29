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
    private void Tranverse(TreeNode node, IList<int> list)
    {
        if (node == null)
            return;
        list.Add(node.val);
        Tranverse(node.left, list);
        Tranverse(node.right, list);
    }
    public IList<int> PreorderTraversal(TreeNode root)
    {
        IList<int> list = new List<int>();
        Tranverse(root, list);
        return list;
    }
}