public class Queue
{
    private Stack<int> stack = new Stack<int>();
    // Push element x to the back of queue.
    public void Push(int x)
    {
        Stack<int> temp = new Stack<int>();
        while (stack.Count > 0)
        {
            temp.Push(stack.Peek());
            stack.Pop();
        }
        stack.Push(x);
        while (temp.Count > 0)
        {
            stack.Push(temp.Peek());
            temp.Pop();
        }
    }

    // Removes the element from front of queue.
    public void Pop()
    {
        stack.Pop();
    }

    // Get the front element.
    public int Peek()
    {
        return stack.Peek();
    }

    // Return whether the queue is empty.
    public bool Empty()
    {
        return stack.Count == 0;
    }
}