public class Solution
{
    public bool IsValid(string s)
    {
        Stack<char> stack = new Stack<char>();
        foreach (char chs in s)
        {
            if (chs == '(' || chs == '{' || chs == '[')
            {
                stack.Push(chs);
            }
            if (chs == ')')
            {
                if (stack.Count == 0)
                    return false;
                char top = stack.Peek();
                if (top == '(')
                    stack.Pop();
                else return false;
            }
            if (chs == '}')
            {
                if (stack.Count == 0)
                    return false;
                char top = stack.Peek();
                if (top == '{')
                    stack.Pop();
                else return false;
            }
            if (chs == ']')
            {
                if (stack.Count == 0)
                    return false;
                char top = stack.Peek();
                if (top == '[')
                    stack.Pop();
                else return false;
            }
        }
        return stack.Count == 0;
    }
}