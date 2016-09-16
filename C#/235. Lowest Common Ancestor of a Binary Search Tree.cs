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
    TreeNode ans = null;
    Dictionary<int, int> dic = new Dictionary<int, int>();
    Dictionary<int, int> dic2 = new Dictionary<int, int>();
    public void CreateDic(TreeNode node)
    {
        if (node == null)
            return;
        if (node.left != null)
        {
            dic.Add(node.left.val, node.val);
            CreateDic(node.left);
        }
        if (node.right != null)
        {
            dic.Add(node.right.val, node.val);
            CreateDic(node.right);
        }
    }
    public void Find(TreeNode node, int value)
    {
        if (node == null)
            return;
        if (node.val == value)
            ans = node;
        else
        {
            Find(node.left, value);
            Find(node.right, value);
        }
    }
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        CreateDic(root);
        int temp = p.val;
        while (dic.ContainsKey(temp))
        {
            dic2.Add(temp, 1);
            temp = dic[temp];
        }
        int temp2 = q.val;
        while (!dic2.ContainsKey(temp2) && temp2 != temp)
        {
            temp2 = dic[temp2];
        }
        Find(root, temp2);
        return ans;
    }
}