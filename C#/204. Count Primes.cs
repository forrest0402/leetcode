//SieveOfEratosthenes
public class Solution
{
    bool[] array = new bool[60000000];
    public int CountPrimes(int n)
    {
        --n;
        int count = 0;
        array[0] = array[1] = false;
        array[2] = true;
        for (int i = 3; i < n + 1; i++)
            array[i] = i % 2 == 0 ? false : true;
        int t = (int)Math.Sqrt(n);
        for (int i = 3; i <= t; i++)
            if (array[i])
                for (int j = i * i; j < n + 1; j += 2 * i)
                    array[j] = false;
        for (int i = 2; i <= n; ++i)
            if (array[i])
                ++count;
        return count;
    }
}

//A faster method
public class Solution
{
    bool[] isPrime = new bool[60000001];
    int[] primes = new int[60000001 >> 1];
    public int CountPrimes(int n)
    {
        for (int i = 0; i < n; ++i)
            isPrime[i] = true;
        int index = 0;
        for (int i = 2; i < n; ++i)
        {
            if (isPrime[i])
                primes[index++] = i;
            for (int j = 0; j < index; ++j)
            {
                if (primes[j] * i > n)
                    break;
                isPrime[primes[j] * i] = false;
                if (i % primes[j] == 0)
                    break;
            }
        }
        return index;
    }
}

// the fastest method
public class Solution
{
    public int CountPrimes(int n)
    {
        --n;
        if (n < 2)
            return 0;
        var gen = new SoA((ulong)n);
        return (int)gen.Count;
    }
}
class SoA : IEnumerable<ulong>
{
    private ushort[] buf = null;
    private long cnt = 0;
    private long opcnt = 0;
    private static byte[] modPRMS = { 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61 };
    private static ushort[] modLUT;
    private static byte[] cntLUT;
    //initialize the private LUT's...
    static SoA()
    {
        modLUT = new ushort[60];
        for (int i = 0, m = 0; i < modLUT.Length; ++i)
        {
            if ((i & 1) != 0 || (i + 7) % 3 == 0 || (i + 7) % 5 == 0) modLUT[i] = 0;
            else modLUT[i] = (ushort)(1 << (m++));
        }
        cntLUT = new byte[65536];
        for (int i = 0; i < cntLUT.Length; ++i)
        {
            var c = 0;
            for (int j = i; j > 0; j >>= 1) c += j & 1;
            cntLUT[i] = (byte)c;
        }
    }
    //initialization and all the work producing the prime bit array done in the constructor...
    public SoA(ulong range)
    {
        this.opcnt = 0;
        if (range < 7)
        {
            if (range > 1)
            {
                cnt = 1;
                if (range > 2) this.cnt += (long)(range - 1) / 2;
            }
            this.buf = new ushort[0];
        }
        else
        {
            this.cnt = 3;
            var nrng = range - 7; var lmtw = nrng / 60;
            //initialize sufficient wheels to non-prime
            this.buf = new ushort[lmtw + 1];

            //Put in candidate primes:
            //for the 4 * x ^ 2 + y ^ 2 quadratic solution toggles - all x odd y...
            ulong n = 6; // equivalent to 13 - 7 = 6...
            for (uint x = 1, y = 3; n <= nrng; n += (x << 3) + 4, ++x, y = 1)
            {
                var cb = n; if (x <= 1) n -= 8; //cancel the effect of skipping the first one...
                for (uint i = 0; i < 15 && cb <= range; cb += (y << 2) + 4, y += 2, ++i)
                {
                    var cbd = cb / 60; var cm = modLUT[cb % 60];
                    if (cm != 0)
                        for (uint c = (uint)cbd, my = y + 15; c < buf.Length; c += my, my += 30)
                        {
                            buf[c] ^= cm; // ++this.opcnt;
                        }
                }
            }
            //for the 3 * x ^ 2 + y ^ 2 quadratic solution toggles - x odd y even...
            n = 0; // equivalent to 7 - 7 = 0...
            for (uint x = 1, y = 2; n <= nrng; n += ((x + x + x) << 2) + 12, x += 2, y = 2)
            {
                var cb = n;
                for (var i = 0; i < 15 && cb <= range; cb += (y << 2) + 4, y += 2, ++i)
                {
                    var cbd = cb / 60; var cm = modLUT[cb % 60];
                    if (cm != 0)
                        for (uint c = (uint)cbd, my = y + 15; c < buf.Length; c += my, my += 30)
                        {
                            buf[c] ^= cm; // ++this.opcnt;
                        }
                }
            }
            //for the 3 * x ^ 2 - y ^ 2 quadratic solution toggles all x and opposite y = x - 1...
            n = 4; // equivalent to 11 - 7 = 4...
            for (uint x = 2, y = x - 1; n <= nrng; n += (ulong)(x << 2) + 4, y = x, ++x)
            {
                var cb = n; int i = 0;
                for (; y > 1 && i < 15 && cb <= nrng; cb += (ulong)(y << 2) - 4, y -= 2, ++i)
                {
                    var cbd = cb / 60; var cm = modLUT[cb % 60];
                    if (cm != 0)
                    {
                        uint c = (uint)cbd, my = y;
                        for (; my >= 30 && c < buf.Length; c += my - 15, my -= 30)
                        {
                            buf[c] ^= cm; // ++this.opcnt;
                        }
                        if (my > 0 && c < buf.Length) { buf[c] ^= cm; /* ++this.opcnt; */ }
                    }
                }
                if (y == 1 && i < 15)
                {
                    var cbd = cb / 60; var cm = modLUT[cb % 60];
                    if ((cm & 0x4822) != 0 && cbd < (ulong)buf.Length) { buf[cbd] ^= cm; /* ++this.opcnt; */ }
                }
            }

            //Eliminate squares of base primes, only for those on the wheel:
            for (uint i = 0, w = 0, pd = 0, pn = 0, msk = 1; w < this.buf.Length; ++i)
            {
                uint p = pd + modPRMS[pn];
                ulong sqr = (ulong)p * (ulong)p; //to handle ranges above UInt32.MaxValue
                if (sqr > range) break;
                if ((this.buf[w] & msk) != 0)
                { //found base prime, square free it...
                    ulong s = sqr - 7;
                    for (int j = 0; s <= nrng && j < modPRMS.Length; s = sqr * modPRMS[j] - 7, ++j)
                    {
                        var cd = s / 60; var cm = (ushort)(modLUT[s % 60] ^ 0xFFFF);
                        //may need ulong loop index for ranges larger than two billion
                        //but buf length only good to about 2^31 * 60 = 120 million anyway,
                        //even with large array setting and half that with 32-bit...
                        for (ulong c = cd; c < (ulong)this.buf.Length; c += sqr)
                        {
                            this.buf[c] &= cm; // ++this.opcnt;
                        }
                    }
                }
                if (msk >= 0x8000) { msk = 1; pn = 0; ++w; pd += 60; }
                else { msk <<= 1; ++pn; }
            }

            //clear any overflow primes in the excess space in the last wheel/word:
            var ndx = nrng % 60; //clear any primes beyond the range
            for (; modLUT[ndx] == 0; --ndx) ;
            this.buf[lmtw] &= (ushort)((modLUT[ndx] << 1) - 1);
        }
    }

    //uses a fast pop count Look Up Table to return the total number of primes...
    public long Count
    {
        get
        {
            long cnt = this.cnt;
            for (int i = 0; i < this.buf.Length; ++i) cnt += cntLUT[this.buf[i]];
            return cnt;
        }
    }

    //returns the number of toggle/cull operations used to sieve the prime bit array...
    public long Ops
    {
        get
        {
            return this.opcnt;
        }
    }

    //generate the enumeration of primes...
    public IEnumerator<ulong> GetEnumerator()
    {
        yield return 2; yield return 3; yield return 5;
        ulong pd = 0;
        for (uint i = 0, w = 0, pn = 0, msk = 1; w < this.buf.Length; ++i)
        {
            if ((this.buf[w] & msk) != 0) //found a prime bit...
                yield return pd + modPRMS[pn]; //add it to the list
            if (msk >= 0x8000) { msk = 1; pn = 0; ++w; pd += 60; }
            else { msk <<= 1; ++pn; }
        }
    }

    //required for the above enumeration...
    IEnumerator IEnumerable.GetEnumerator()
    {
        return this.GetEnumerator();
    }
}