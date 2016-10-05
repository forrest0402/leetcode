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
    private const int NOROB = 0;
    private const int ROB = 1;
    private int[] DP(TreeNode root)
    {
        if (root == null)
            return new int[] { 0, 0 };
        int[] dpLeft = DP(root.left);
        int[] dpRight = DP(root.right);
        int robThis = dpLeft[NOROB] + dpRight[NOROB] + root.val;
        int noRobThis = Math.Max(dpLeft[ROB], dpLeft[NOROB]) +
            Math.Max(dpRight[ROB], dpRight[NOROB]);
        return new int[] { noRobThis, robThis };
    }
    public int Rob(TreeNode root)
    {
        int[] dp = DP(root);
        return Math.Max(dp[NOROB], dp[ROB]);
    }
}