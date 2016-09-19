public class Solution
{
    List<char> mapList = new List<char>{
      '0','1','2','3','4','5','6','7','8','9','#','.','!','@','$','%','*','+','a','b','c','d','e','f','g','h','i',
      'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','A','B','C','D','E','F','G','H','I',
      'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    };
    public bool IsIsomorphic(string s, string t)
    {
        HashSet<char> set = new HashSet<char>();
        for (int i = 0; i < s.Length; ++i)
        {
            if (set.Contains(s[i]))
                continue;
            char sub = mapList.Find(c => !set.Contains(c) && s.IndexOf(c) < 0 && t.IndexOf(c) < 0);
            set.Add(sub);
            s = s.Replace(s[i] + "", sub + "");
            t = t.Replace(t[i] + "", sub + "");
        }
        return s == t;
    }
}