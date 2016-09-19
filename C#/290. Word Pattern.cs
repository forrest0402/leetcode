public class Solution
{
    List<char> mapList = new List<char>{
      '0','1','2','3','4','5','6','7','8','9','#','.','!','@','$','%','*','+','a','b','c','d','e','f','g','h','i',
      'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','A','B','C','D','E','F','G','H','I',
      'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    };
    public bool WordPattern(string pattern, string str)
    {
        HashSet<string> set = new HashSet<string>();
        for (int i = 0; i < pattern.Length; ++i)
        {
            if (set.Contains(pattern[i] + ""))
                continue;
            char sub = mapList.Find(c => !set.Contains(c + "") && pattern.IndexOf(c) < 0);
            set.Add(sub + "");
            pattern = pattern.Replace(pattern[i] + "", sub + "");
        }
        set.Clear();
        List<string> patternList = str.Split(' ').ToList();
        for (int i = 0; i < patternList.Count; ++i)
        {
            if (set.Contains(patternList[i]))
                continue;
            char sub = mapList.Find(c => !set.Contains(c + ""));
            set.Add(sub + "");
            string temp = patternList[i];
            for (int j = i; j < patternList.Count; ++j)
                if (patternList[j] == temp)
                    patternList[j] = sub + "";
        }
        string patternStr = "";
        foreach (string s in patternList)
            patternStr += s;
        return patternStr == pattern;
    }
}