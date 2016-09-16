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
            else ans[level].Add(-1);
            if (node.right != null)
                ans[level].Add(node.right.val);
            else ans[level].Add(-1);
        }
        else
        {
            IList<int> list = new List<int>();
            if (node.left != null)
                list.Add(node.left.val);
            else list.Add(-1);
            if (node.right != null)
                list.Add(node.right.val);
            else list.Add(-1);
            ans.Add(list);
        }
        Tranverse(node.left, level + 1);
        Tranverse(node.right, level + 1);
    }
    public bool IsSymmetric(TreeNode root)
    {
        if (root == null)
            return true;
        ans = new List<IList<int>>();
        IList<int> rootList = new List<int>();
        rootList.Add(root.val);
        ans.Add(rootList);
        Tranverse(root, 1);
        foreach (IList<int> level in ans)
        {
            int lPos = 0, rPos = level.Count - 1;
            while (lPos < rPos)
            {
                if (level[lPos++] != level[rPos--])
                    return false;
            }
        }
        return true;
    }
}