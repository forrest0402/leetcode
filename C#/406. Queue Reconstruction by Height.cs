public class Solution
{
    public int[,] ReconstructQueue(int[,] people)
    {
        int row = people.GetLength(0);
        for (int i = 0; i < row; ++i)
        {
            int n = i;
            for (int j = i + 1; j < row; ++j)
            {
                if (people[j, 0] < people[n, 0] || (people[j, 0] == people[n, 0] && people[j, 1] < people[n, 1]))
                {
                    n = j;
                }
            }
            if (n != i)
            {
                int temp = people[i, 0];
                people[i, 0] = people[n, 0];
                people[n, 0] = temp;
                temp = people[i, 1];
                people[i, 1] = people[n, 1];
                people[n, 1] = temp;
            }
        }
        for (int i = row - 1; i >= 0; --i)
        {
            int n = 0;
            while (i - n - 1 >= 0 && people[i - n - 1, 0] == people[i, 0])
                ++n;
            if (n != people[i, 1])
            {
                int temph = people[i, 0];
                int tempk = people[i, 1];
                for (int j = 0; j < tempk - n; ++j)
                {
                    people[i + j, 0] = people[i + j + 1, 0];
                    people[i + j, 1] = people[i + j + 1, 1];
                }
                people[i + tempk - n, 0] = temph;
                people[i + tempk - n, 1] = tempk;
            }
        }
        return people;
    }
}