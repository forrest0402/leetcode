public class Solution
{
    public int ComputeArea(int A, int B, int C, int D, int E, int F, int G, int H)
    {
        int sum = (C - A) * (D - B) + (G - E) * (H - F), inter = 0;
        if (A <= E && B <= F && C >= G && D >= H)
            inter = (C - A) * (D - B);
        if (A >= E && B >= F && C <= G && D <= H)
            inter = (G - E) * (H - F);
        if (E >= C || F >= D || A >= G || B >= H)
            inter = 0;
        int a = A < E ? E : A;
        int b = B < F ? F : B;
        int c = C < G ? C : G;
        int d = D < H ? D : H;
        if (c >= a && d >= b)
            inter = (c - a) * (d - b);
        return sum - inter;
    }
}