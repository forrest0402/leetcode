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
    List<string> routes = null;
    private void Tranverse(TreeNode node, string route)
    {
        if (node == null)
            return;
        route = route == "" ? node.val + "" : route + "->" + node.val;
        Tranverse(node.left, route);
        Tranverse(node.right, route);
        if (node.left == null && node.right == null)
            routes.Add(route);
    }
    public IList<string> BinaryTreePaths(TreeNode root)
    {
        routes = new List<string>();
        Tranverse(root, "");
        return routes;
    }
}