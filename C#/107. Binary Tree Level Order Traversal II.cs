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
        if (node.left != null)
        {
            if (ans.Count - 1 >= level)
                ans[level].Add(node.left.val);
            else
            {
                IList<int> list = new List<int>() { node.left.val };
                ans.Add(list);
            }
        }
        if (node.right != null)
        {
            if (ans.Count - 1 >= level)
                ans[level].Add(node.right.val);
            else
            {
                IList<int> list = new List<int>() { node.right.val };
                ans.Add(list);
            }
        }
        Tranverse(node.left, level + 1);
        Tranverse(node.right, level + 1);
    }
    public IList<IList<int>> LevelOrderBottom(TreeNode root)
    {
        if (root == null)
            return new List<IList<int>>();
        ans = new List<IList<int>>();
        IList<int> rootList = new List<int>();
        rootList.Add(root.val);
        ans.Add(rootList);
        Tranverse(root, 1);
        return ans.Reverse().ToList();
    }
}