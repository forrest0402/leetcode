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
    IList<int> TraByLevelOrder = null;
    public void Traverse(TreeNode node, int level)
    {
        if (node == null)
            return;
        if (TraByLevelOrder.Count - 1 >= level)
        {
            if (node.right != null)
                TraByLevelOrder[level] = node.right.val;
            else if (node.left != null)
                TraByLevelOrder[level] = node.left.val;
        }
        else
        {
            if (node.right != null)
                TraByLevelOrder.Add(node.right.val);
            else if (node.left != null)
                TraByLevelOrder.Add(node.left.val);
        }
        Traverse(node.left, level + 1);
        Traverse(node.right, level + 1);
    }
    public IList<int> RightSideView(TreeNode root)
    {
        if (root == null)
            return new List<int>();
        TraByLevelOrder = new List<int>() { root.val };
        Traverse(root, 1);
        return TraByLevelOrder;
    }
}