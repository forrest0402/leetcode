/**
 * Definition for binary tree
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator
{
    TreeNode root = null;
    Stack<TreeNode> stack = new Stack<TreeNode>();
    public BSTIterator(TreeNode r)
    {
        root = r;
        while (r != null)
        {
            stack.Push(r);
            r = r.left;
        }
    }

    /** @return whether we have a next smallest number */
    public bool HasNext()
    {
        return stack.Count != 0;
    }

    /** @return the next smallest number */
    public int Next()
    {
        TreeNode t = stack.Pop(), node = t.right;
        while (node != null)
        {
            stack.Push(node);
            if (node.left != null)
                node = node.left;
            else break;
        }
        return t.val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.HasNext()) v[f()] = i.Next();
 */
