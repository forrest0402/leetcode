public class Stack
{
    // Push element x onto stack.
    Queue<int> queue = new Queue<int>();
    public void Push(int x)
    {
        Queue<int> temp = new Queue<int>();
        while (queue.Count > 0)
        {
            temp.Enqueue(queue.Peek());
            queue.Dequeue();
        }
        queue.Enqueue(x);
        while (temp.Count > 0)
        {
            queue.Enqueue(temp.Peek());
            temp.Dequeue();
        }
    }

    // Removes the element on top of the stack.
    public void Pop()
    {
        queue.Dequeue();
    }

    // Get the top element.
    public int Top()
    {
        return queue.Peek();
    }

    // Return whether the stack is empty.
    public bool Empty()
    {
        return queue.Count == 0;
    }
}