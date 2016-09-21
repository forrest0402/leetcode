public class Solution
{
    public int IntegerReplacement(int n)
    {
        Queue<Op> q = new Queue<Op>();
        q.Enqueue(new Op() { n = n, step = 0 });
        while (q.Count > 0)
        {
            Op op = q.Dequeue();
            if (op.n == 1)
                return op.step;
            if (op.n % 2 == 0)
                q.Enqueue(new Op() { n = op.n / 2, step = op.step + 1 });
            else
            {
                q.Enqueue(new Op() { n = op.n + 1, step = op.step + 1 });
                q.Enqueue(new Op() { n = op.n - 1, step = op.step + 1 });
            }
        }
        return 0;
    }
}
class Op
{
    public long n;
    public int step;
}