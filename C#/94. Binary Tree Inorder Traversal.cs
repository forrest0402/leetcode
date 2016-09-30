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
        Tranverse(node.left, list);
        list.Add(node.val);
        Tranverse(node.right, list);
    }
    public IList<int> InorderTraversal(TreeNode root)
    {
        IList<int> list = new List<int>();
        Tranverse(root, list);
        return list;
    }
}