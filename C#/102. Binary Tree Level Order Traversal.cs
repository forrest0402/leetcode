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
    IList<IList<int>> ans = null;
    public void Tranverse(TreeNode node, int level)
    {
        if (node == null)
            return;
        if (ans.Count - 1 >= level)
        {
            if (node.left != null)
                ans[level].Add(node.left.val);
            if (node.right != null)
                ans[level].Add(node.right.val);
        }
        else
        {
            IList<int> list = new List<int>();
            if (node.left != null)
                list.Add(node.left.val);
            if (node.right != null)
                list.Add(node.right.val);
            if (list.Count > 0)
                ans.Add(list);
        }
        Tranverse(node.left, level + 1);
        Tranverse(node.right, level + 1);
    }
    public IList<IList<int>> LevelOrder(TreeNode root)
    {
        if (root == null)
            return new List<IList<int>>();
        ans = new List<IList<int>>();
        ans.Add(new List<int>() { root.val });
        Tranverse(root, 1);
        return ans;
    }
}