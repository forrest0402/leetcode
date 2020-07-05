# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 5/7/2020 下午8:52
"""

from typing import List


class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in T
        """
        partial, j = self.partial(P), 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                return i - (j - 1)

        return -1


class Trie:

    def __init__(self):
        self.dicts = dict()

    def add(self, word):
        node = self.dicts

        for w in word:
            if w not in node:
                node[w] = dict()
            node = node[w]

    def search(self, word):
        node = self.dicts
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return True


class Solution:
    # def minimumLengthEncoding(self, words: List[str]) -> int:
    #     kmp = KMP()
    #     ret = 0
    #     texts = ''
    #     words.sort(key=lambda w: len(w), reverse=True)
    #     for word in words:
    #         idx = kmp.search(texts, word)
    #         if idx == -1:
    #             ret += len(word)
    #             if len(texts) == 0:
    #                 texts = word + "#"
    #             else:
    #                 texts = texts + word + '#'
    #                 ret += 1
    #
    #     # print(texts)
    #     for word in words:
    #         if word not in texts:
    #             print(word)
    #     return len(texts)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        ret = 0
        words.sort(key=lambda w: len(w), reverse=True)
        for word in words:
            if trie.search(word[::-1]):
                continue
            trie.add(word[::-1])
            ret += len(word) + 1

        return ret


if __name__ == "__main__":
    s = Solution()
    assert s.minimumLengthEncoding(["time", "me", "bell"]) == 10
    assert s.minimumLengthEncoding(
        ["ojtnj", "uuydcho", "dgsyp", "dwxycpx", "dpmvc", "dvfhmb", "flrxjjx", "fwhdhvn", "rgsakp", "aiconf", "nzacpk",
         "sbxnaj", "shway", "rgrmz", "rysudo", "bzkioce", "mqxkzvu", "wyebk", "tymoaz", "mlmbg", "djbmek", "qfnme",
         "khkiyae", "tjdaxry", "sqtcwz", "ehnsai", "jhncvrm", "cxkzgrx", "pummt", "hzrpfcn", "lkyqit", "phpqdxw",
         "vangm", "wcjdgw", "pxesvtn", "mnqory", "bdrzvh", "brtzmo", "chqgf", "bipyxm", "meoikg", "ysyckk", "ojayeiq",
         "zrfbsb", "yhuotea", "crfbhq", "tllycn", "qxnzihf", "avyawpz", "bwsjym", "myjozc", "lbdksm", "mctlt",
         "dszowuw", "syshm", "xrvhhkn", "kgrcwfv", "dwlajlf", "yviuk", "xegjj", "spiczl", "vfvomi", "mgcujy", "dqmzb",
         "isrisgt", "vdrtuah", "vsyth", "eoclef", "poccek", "cgafrlu", "crbhpgk", "sromv", "xmvbca", "gobra", "ygvlq",
         "pjvhe", "tfweiso", "cskuohg", "eyalone", "pobkak", "nzpxn", "lbcrws", "uhtfe", "eorth", "showvu", "hxsmb",
         "jrggose", "izifkb", "oqwyf", "mozmzj", "ijwle", "ggtqqqv", "geevzj", "meota", "ifsse", "kdtofm", "swydhvf",
         "tzjhqap", "wqwwd", "jlinnov", "lmxkgeg", "stbot", "xrsfn", "etoyctk", "rygagm", "vcnrf", "zkdge", "emqtscp",
         "newqcyy", "nnuus", "exwsxbd", "zstvl", "lbkko", "kygkyqq", "oggji", "xytbjo", "mfbahk", "ggoks", "lmqewkl",
         "qexhyqe", "ogaogio", "nzvbav", "mdole", "qvyks", "gkupfu", "dgmpn", "ngrdrj", "iitqvk", "ipuiqb", "ugxfea",
         "ialkmv", "hmgnx", "aoyoj", "fvzhjil", "butrbp", "dwhxnes", "etkdwg", "cjkghz", "tovkq", "mmxhv", "jgcsn",
         "hmictal", "zxmnek", "pcoeg", "ntyqmlq", "hfubhtg", "ydjbv", "xnwlqto", "hatgi", "bsaczd", "pokwk", "arxlula",
         "zjtqlk", "ocfxup", "nsnqjc", "xdcsopi", "iqxyxp", "xfmtpvm", "bqtgcf", "wboycn", "aoeda", "uowqdgj", "rzzzx",
         "liucs", "ejzxz", "qmlehsh", "igrbmon", "dpmkbon", "pmayh", "nujdwdw", "awdgo", "ijgkzk", "inhee", "jzdtv",
         "adhauh", "grtmbp", "qndbvw", "zprrw", "mpqieq", "jzmzeuu", "fcvftqs", "qxzxqy", "lidguzz", "eazwd", "zjhfsz",
         "zsnzefh", "mnckfg", "zjgtq", "ckyxlif", "fznfo", "jegnof", "lzwyzb", "ozivfio", "igkclsa", "bebzn", "bitsggm",
         "lrnwin", "hjnnzr", "idvoirn", "dgile", "vfngh", "xbmur", "rqaftt", "wjwwwxs", "btreou", "gjsycg", "pvsiylz",
         "ccxzgdf", "excrrrr", "fiesr", "jdioj", "uzwsc", "odrlcoy", "hcsit", "ptwfprh", "sbqry", "kffvy", "ejeawbp",
         "omvcc", "iqgxqlt", "edsuu", "xnbue", "qfbcx", "fzlmbkl", "wrrcueb", "mmqispp", "nknilwd", "dewuhju",
         "hmdqlxy", "vjxgg", "lkuexo", "dzvfscm", "voulbs", "uevoqgq", "kmhwu", "oglzllg", "torhihn", "fhuqzc",
         "mmcfhb", "woyayma", "uznsvre", "mmxed", "aoskwg", "xrosbm", "hpyrgh", "tghwbwh", "hcwzn", "iepeftj", "judij",
         "kudbk", "jonpv", "lywck", "rxelz", "bgifz", "mehbxq", "fmqnz", "sqrmzj", "iqqjzex", "qioliz", "kjizbf",
         "lgdcffc", "pfgmcr", "trdabul", "vlqjdnc", "jjvbxe", "fqlayw", "ilbhtyq", "saawulw", "gxysrb", "kighql",
         "eceapr", "kztbcww", "jedkoy", "dxpcaga", "ndacphe", "rcoit", "ywgcnxg", "klipfup", "bddws", "jwyof", "lrfwgo",
         "bediwuf", "ujakh", "ppima", "xzhwvm", "guzmsqt", "ffbliq", "adjmynm", "akabzn", "inmykju", "vlcjyv",
         "orquepg", "tufrk", "vqpjymm", "lvuab", "qzxav", "ekcmu", "uqtuhie", "kfvtgf", "nklwjo", "ujxlfpl", "zobfpq",
         "eignijd", "ythctg", "artllm", "wodhh", "tzpwszq", "njdqegg", "hzrqib", "zvoxtfd", "htboem", "axjuix", "bvmvm",
         "jbnum", "bxdth", "atejt", "gqsqtnk", "fykrjbp", "ldyhonr", "wcuoj", "upphc", "agydg", "cjmwk", "rhxbqh",
         "tpgozdd", "qyqoy", "zjqutw", "qoohqny", "nsiacwz", "xupin", "criuvs", "eswjeft", "pdmevn", "zvogq", "lrrvo",
         "qhfqqpw", "ktudfg", "ijvmi", "neyjjdx", "rllpi", "vllvaa", "esebtu", "jyhcrh", "otgmr", "oudvyxj", "pmszy",
         "opeed", "gicni", "mnuzn", "mjbfpod", "sqwgxu", "dwniwz", "wmbmmv", "lyafuy", "zmvlz", "kopxzuh", "urcbbiy",
         "guhco", "nerjm", "lpdxc", "hxmjzz", "hynagc", "iyxeczi", "bdfxmoz", "yybnpqd", "jvgnb", "oquqem", "fmclmz",
         "dmkhf", "zxbjpp", "qpxgcir", "iecvjm", "gtkne", "lgtqrbc", "gilbn", "mcxsg", "ncwbhn", "wkriiq", "zhsir",
         "ptkkmw", "jcbpkrm", "vbefo", "vmbcd", "vqffj", "fhqzjt", "nryuh", "vmclav", "cjyggm", "sanev", "rrdocz",
         "zqdexbs", "jrxstt", "pyhcesj", "aagghyr", "cyemjrb", "aliohf", "qaslg", "pnyjzxz", "pehnvi", "suhuw",
         "twopabr", "sapqoc", "mckrh", "nzlgrxt", "aqpobnu", "pirbjgb", "plzlj", "raylxpu", "gyasfrh", "urjfxux",
         "xjbwau", "iupknn", "vhxnc", "dnbjop", "vrxhwmd", "vjsmkh", "rfmqids", "smaiwt", "vkyfo", "bjqyxc", "rbbbp",
         "dlkzg", "dwvdwu", "prulzh", "bavge", "ehhrz", "xxjqk", "pxopmp", "okmkmb", "slcznpp", "nvqlb", "jalrk",
         "parwlcd", "anbxo", "oqcxyzo", "fjhrdjh", "pgvnwfe", "yfjyvh", "quvszjm", "xyiig", "xtncqv", "svsix", "jvpdnh",
         "owuiv", "bsrugtt", "rmvggws", "lmdql", "kvmvd", "xrpmaw", "ssnxyb", "oworq", "rmmpuya", "rijpih", "aelazka",
         "kncksqx", "yvtdiy", "epato", "pbbamj", "fejsw", "zgsru", "ekwrre", "zqben", "vugxi", "fvcsdp", "rujcews",
         "asqxya", "worjlsd", "xggakg", "kzfpot", "haqon", "ypqxzz", "mmkzwt", "bdhif", "exzhv", "srnklzh", "hlrunb",
         "dwfyke", "fvgbtdm", "aeutp", "czhefx", "tegfw", "jkxpsb", "gxkfkw", "exvntd", "gvuti", "jdmly", "owaqhw",
         "fopuxzv", "edrvil", "biszwgv", "vgckzd", "fqdxn", "qktdf", "hpgwrk", "gpxiips", "vxnlab", "yylxz", "hsuscch",
         "bhivaf", "wzrwtc", "ebplv", "yzxykou", "mxlssom", "evghv", "hksleg", "shybau", "zeyqa", "tljqka", "axfkec",
         "fatdj", "janlkcc", "sjorbra", "jplge", "oazzot", "qbgtncn", "ozlil", "stohadq", "rvpuwn", "oqwpl", "byftgi",
         "ubuusl", "fkogr", "bybdyhj", "vinyuzs", "ivsqvz", "vmnae", "gckxw", "rozbe", "glvxwj", "rcgicu", "xmvbd",
         "itycsry", "llmwrs", "fuqth", "styrrwl", "wsseuln", "xwflcli", "muxgz", "ypmbboh", "rpmvnep", "wjvvnv",
         "arjnw", "toauwc", "ltjxqrl", "basffd", "clxozwd", "glmrv", "iejgfj", "cvkoj", "wotjf", "mqucec", "xalgemc",
         "hgimkh", "golvfq", "fuqpmak", "mhpcp", "pxoibt", "ledqa", "guzbyr", "ztvbeka", "racdp", "krsngra", "aaiknz",
         "bhoobyc", "xibbe", "yohepxk", "eclevs", "ldliwcm", "qatvlk", "eiypbw", "vxvtwa", "nkdwsej", "ftmyvp",
         "gpthye", "gazwoi", "zzgipon", "cithg", "wpabujl", "jhezlnb", "vqqaxfg", "kvpbk", "vggjemp", "owylv",
         "lgwtfpg", "jjqvfm", "xbhga", "tulvfv", "sefuo", "hbysv", "ozopepd", "awyrifd", "pnudwx", "vreje", "zhpgw",
         "qygbf", "tvbrvy", "zzmcw", "cznee", "deuzxt", "qfppjvi", "ilkps", "ydwhg", "krwkxzu", "mnsidg", "rkxyyr",
         "ajkqz", "xtmom", "vqocor", "fympcl", "yyleyzy", "jjvzhrn", "kpmxvuz", "txoeqlx", "lhhmn", "chzgpf", "ncnjxle",
         "ihxrg", "feqixq", "lkfhcar", "hfnsh", "bifczy", "umknat", "yrhgkh", "mgpcu", "qotukst", "yqlmfq", "ttcdp",
         "xnjjzm", "cukbr", "hjhjb", "iikfcsr", "nsqbnnz", "dauygf", "cmydq", "lfnhqnl", "ppqgs", "hscbfug", "ohzisud",
         "opspdkv", "aauxbop", "wpkhzo", "sxbsgu", "tajrv", "ololy", "mxmus", "vizvxv", "osaqz", "rxygkn", "mrzqlf",
         "zrriyxb", "ufroe", "bajozg", "atpsu", "uhgauzu", "tffdw", "mdjulde", "rbrmy", "jhkqvwl", "gzsultq", "nkbfi",
         "xtvwh", "dryzcv", "emaxuk", "zucvutb", "jdduyk", "bjdin", "loicuq", "qhjjb", "rgfjbq", "mphnk", "lxvceyx",
         "zeoxb", "fxhnxu", "qpbipe", "ophwp", "wiioer", "quchwj", "pouxunw", "bloxgg", "xbsma", "dtwew", "xstorn",
         "qfrfkz", "gxusbsn", "dhnxd", "mhstbs", "hekbtu", "wvrrjw", "yeiwd", "patplsx", "qmyiyi", "mowboj", "iskyd",
         "bqhjj", "povppk", "vthpwx", "uuydaw", "rduxvez", "vmcww", "ylruvph", "ymqosp", "wzcvohg", "lhepwta", "bckhc",
         "oiyyt", "wqzfv", "uduec", "lkkbtzl", "prvpbo", "jrwstii", "ijztoo", "qwwth", "vqzqiun", "krnjp", "zyanpiw",
         "ojhjhvg", "lohmb", "thqtf", "reptzv", "zgkyq", "lhkvy", "cmjwl", "fmilgpw", "jrfawz", "vrtzd", "ezgfl",
         "plzng", "zidzso", "civavlg", "vtwopu", "ljhckxo", "nuydt", "qembl", "fiwrre", "gfrgi", "gzegiq", "mltlqo",
         "pcett", "snbsc", "msibcqn", "beacrhz", "vsycjt", "gjqji", "smcegol", "zregkp", "smcazoj", "dziqad", "jpuwp",
         "hnlztac", "vduitco", "wyencad", "bkdnnqo", "cabzyg", "mgpcwr", "fxgvkxt", "wlkcrdd", "bhmhsy", "gqcctjc",
         "atafpt", "vdzhmcg", "ighxj", "gfqpale", "fohbrtj", "mfpsgt", "tarjocf", "gyycb", "qvqfryl", "jpwowwc",
         "jcgcg", "gmrjze", "nfptxq", "hmjhxge", "ieelj", "suvkgr", "nwjxe", "tkepqm", "extnpmq", "rxzdvf", "relzaa",
         "hfhgaq", "lmihlz", "pacocq", "dclxr", "oknoem", "pbpnnd", "nleerfl", "tvytymc", "aamfnl", "ufdnq", "bxyzvyh",
         "vksvout", "lohxhf", "sskgn", "aawbv", "hrvhx", "wvoqf", "vxkvh", "oqany", "bcmyd", "epdddqn", "zrlej",
         "bchaf", "hmftii", "mefcrz", "wbxvc", "ewwnldf", "cqecxgh", "cnwvdmk", "vetrw", "zmogwov", "lshlzpe", "lijay",
         "tcdqg", "xavqixd", "yjkhtsl", "myjvow", "cgthhd", "taaii", "iuuegk", "lcypmle", "wesrit", "tybco", "nhxysw",
         "awkrj", "jcmqa", "porvo", "nrypriu", "vznnevp", "hzklwi", "vapuxh", "wyfkn", "albemu", "ttfdbl", "dbqrjv",
         "cxals", "qzitwf", "ysunur", "llsefy", "cghfzji", "jboaa", "emhlkw", "khhmgha", "twlxgjz", "pyujor", "ozcax",
         "fetvovo", "mdhrrd", "qdhdne", "fiuvw", "ebyxh", "ldaothh", "vwyjf", "yjyljlu", "ivroqg", "qvpeyec", "eemsdra",
         "wavgeqk", "bjejrqg", "mdjimoz", "fgopy", "lgwodr", "cunvszh", "wiver", "ghmog", "jzgfyk", "vxlbx", "kvgbtn",
         "cunorte", "mtesdc", "zdzmqu", "pigik", "smruadg", "czjxlt", "kukgaok", "tsldpqq", "luomo", "ezbcvdc",
         "tfetwes", "uopzf", "wsvezkw", "wrnlvbx", "bpqungd", "jqnnof", "rqhiomi", "voulqb", "ouspxn", "chngpz",
         "fbogfcv", "nqhunxo", "rydbke", "ewduo", "suqqwup", "oxzfxj", "kuwfwm", "euiics", "mvftoau", "vstfbm",
         "vnmtoo", "muicf", "bjbskxb", "knbomlf", "enrbtfk", "hnaqe", "vxzsr", "gkqma", "qygmn", "ztkybmb", "injggpk",
         "enqrgdk", "rkgoct", "tgaiu", "dnknoxk", "iwuou", "oxanccl", "xestej", "ekrqq", "xbwhz", "jkdvxfh", "oybaay",
         "afyhci", "papffjq", "bdppssw", "qwyvjx", "xmnnosl", "kvqzjl", "wcwii", "ygfvt", "tpabbht", "kjmaq", "duschjz",
         "gguiof", "wgfhve", "joqmfjq", "smqfd", "ynlovlz", "sgrzum", "bobmux", "dcppi", "isdjrwl", "lbevb", "efqsirq",
         "hlgfql", "enmemlb", "dbmfk", "ibfpzm", "rtdnooq", "yicdq", "xadul", "dxibxzi", "yyxnj", "jhsdzxw", "thltbi",
         "kwhreyi", "hrocoa", "fnaalbd", "vnwona", "nnonm", "naqaf", "xgzzies", "uhruynk", "kgadfx", "hyohzbd", "hnajx",
         "yipzh", "ezdxaet", "xbzppoz", "rwnewxz", "hlcbkmb", "znyhu", "zsqtpkr", "gmyxr", "rphyvo", "bgjuz", "nulpv",
         "eejfoso", "xmwcnes", "xxxxnpe", "jezkk", "idfsxrw", "qgzjtf", "arpzpo", "hxsanlt", "emvotcb", "sknzhvg",
         "icitca", "ivhdln", "sqilerz", "ndigw", "bcsre", "mibbep", "zsczom", "cgghjbb", "fkylfgt", "bvzofs", "mefsng",
         "bispbza", "tsosgy", "xopalrw", "wserf", "jbmlz", "xidxny", "ffmpjos", "vddwxmd", "netnsg", "kgevsp", "pguuv",
         "cwisp", "slxiyb", "dmwaguc", "jobwusu", "uytcqrv", "hzhsy", "zrlsdd", "xhxah", "rxzij", "zwdgy", "ygmvkz",
         "drkzbo", "qpsal", "tpxvl", "lfmfl", "sayjvlh", "rdamym", "ycuzd", "zkycu", "hdesec", "unequk", "lpkdid",
         "vorxls", "admsdop", "rqnvkyg", "krnqqtb", "rxfms", "xfthd", "pxjbk", "gpslrg", "rwziwef", "usxgqvz", "baxxye",
         "ocrkkrw", "lrlgsp", "ceyctg", "rniml", "vavug", "jgircl", "jrpnmsa", "rywvlfg", "prxnys", "fkzmknn", "ooelc",
         "btvfs", "yqepuvw", "tmmmb", "qmpzexb", "zjckjvd", "aieytbb", "oafqq", "szrcyh", "czrxgae", "ifkte", "hfgajox",
         "pwpnkqq", "yqphogn", "xuwthrd", "mpcmy", "qitdoa", "avlzfrh", "ywpip", "dgeki", "fgbnx", "tyofu", "xziqzj",
         "qxzvqz", "vtsqk", "ipkld", "yfhim", "ebaegdc", "ubhrh", "ldejv", "mtflwy", "ocpyj", "yopgqs", "fkjxxd",
         "njnnwr", "nylkeb", "taymdqv", "ekpznq", "cbzobmg", "bucdds", "qjozu", "uvpghor", "obhnu", "ljkxbg", "uqrxjtf",
         "xwbxiw", "oxsmcg", "spchdd", "pcuitj", "faidq", "tybmy", "uygiyp", "qloizj", "cafgmy", "smetd", "kwcwb",
         "tdabxf", "fpmrc", "lfjujn", "vvmvex", "mnsgdc", "enjlgsw", "ohwcg", "kxjdaup", "rotjarp", "aovdoq", "oviwq",
         "qwaxs", "bmazco", "plcljsv", "yytjhl", "vgwjm", "drnue", "vqjgf", "uqlsfy", "bmqmfp", "lkauwna", "ozmqce",
         "heunaxr", "zaffbj", "arbek", "qjnllw", "fdkhlz", "wgmbwh", "yceqag", "ltjjq", "yurggfw", "puaafsl", "tjiqkyt",
         "yuzub", "ytmrfq", "ommmu", "ipknn", "iubnuab", "dzthvc", "zjbzpew", "dcooev", "pjydqcf", "zuojlzy", "zwjyfc",
         "spmac", "dfkbnz", "fzriie", "asusog", "hdodx", "drjpo", "ddyif", "chabv", "ebvkwrr", "burdjl", "jjddi",
         "dljzkye", "samyg", "zwgxcq", "xtratwo", "qfopz", "xvlaw", "laage", "btdium", "vzlnzt", "kmvbzkq", "kctobsx",
         "kazbelu", "yxdwrk", "eslvjc", "nhsdmvs", "zuxqcc", "hqtxovn", "zrbdai", "fgjxs", "txecvio", "kjxlq", "dkuxss",
         "mkbevn", "pzmdqc", "ihyia", "atsub", "twytus", "nzooxj", "qwuoly", "fdoigo", "zukhlh", "mugeaxt", "qqsfyls",
         "qqtql", "wrvphcx", "nzjfhx", "uequtk", "fxuto", "qnast", "nveys", "ltbrcth", "toctdib", "fbpnh", "umxfgn",
         "zvjuta", "yeron", "qzvswqk", "gbctr", "ryryz", "zieknd", "zcsna", "jrhak", "zfxqsj", "urlba", "lbozqf",
         "yfcjaa", "hazgy", "gmmfzyz", "zjvkyc", "rvfdcf", "daitab", "hcxqgum", "qwakp", "ltbsjwo", "pqqtygx",
         "upxcxao", "qylot", "lmxqc", "dwzcd", "tjccm", "mqcpap", "wgxqtr", "ivycvxy", "wdykg", "snvqka", "jxtvtsb",
         "jnyowsq", "iwfuoig", "cuoixhu", "fzwalg", "djhrar", "sjmahk", "dyusf", "wrxqvdi", "ftytlor", "jsjbv",
         "vjbebg", "agvsn", "vvmpgm", "gsgjopk", "vbqvhy", "afopf", "zybfuz", "aqsgc", "ytrjsvn", "wlhdfr", "vdhvl",
         "jrlvr", "cscxwf", "yhgbew", "wupbl", "ssuhyvv", "bhcirzk", "oykwk", "ijbto", "qsnpgw", "otwzage", "ytqzh",
         "rgwow", "bvhgkwh", "fvawxie", "fllxw", "gfcqf", "scoqb", "qubrq", "gdxjtp", "ahrpck", "awnlgi", "cmehsyp",
         "dwmytpy", "firyeq", "oohwhr", "caelk", "mqemvs", "qflkzi", "tfpibll", "ybhzd", "ctsxri", "yurocj", "dnlnl",
         "ydmdva", "xkaotl", "xovax", "ypynrqp", "kwfzw", "fbgsmrc", "tutime", "rcugul", "cvewno", "typhbpa", "wazew",
         "flzfs", "wxxbza", "ogjfkl", "vjlebet", "imbubm", "xinyncy", "dqmxfy", "buhagzh", "jjadpos", "gejyz", "gxshqk",
         "wkwrs", "dqeriqo", "dmixr", "bysjih", "aoloq", "ddwhsxs", "nteqv", "cqagf", "ditsrn", "wfxgl", "jwjqb",
         "rvkxj", "rxapr", "yrlkip", "npquasb", "nvezlr", "gmhchcx", "lodfihi", "dheypxa", "plzjykh", "qopsthg",
         "zsnes", "raongg", "zrpnac", "tzmtltj", "jsecdn", "rzudh", "hkcyic", "xsxmw", "reeuwpn", "grkwrag", "gvzzbsq",
         "lrfta", "aqyvbkj", "ytgfu", "wcmvd", "olnvfi", "hhgmhb", "kojmepr", "wpohl", "szhgg", "hymiblu", "lkwjr",
         "zulqpz", "sdcqjo", "olgsgez", "lxkpqci", "yxcgn", "gmvex", "fskpppe", "utzto", "axncvp", "lcyahba", "ydeae",
         "zvzar", "ghfkkqv", "ryrpg", "gucpbq", "reofjz", "cdnoo", "dchhh", "byiwd", "cqbhok", "ksfnoa", "xsmmlr",
         "qyvdfqh", "dzshj", "bpifnzh", "uxmoml", "jdxvojf", "ihfll", "vwesfof", "zynnpb", "fwzra", "rxlgww", "vkmjd",
         "hcjgzt", "mkapfl", "ffjqlf", "wulaebc", "gurramv", "tufkzai", "bxprqek", "nkohv", "abgfwyl", "slslg",
         "wirsnh", "pykvuh", "fdrwk", "gtmgsxe", "dxsaab", "lqiryty", "aoezg", "tzhugcg", "uoarf", "dwhsv", "rjiuoi",
         "ycgcdnf", "rtfmwz", "amkjc", "woogtdi", "deprx", "ucknu", "womfm", "xdeev", "qapxpuu", "ngulnk", "fgtxyf",
         "hnyabid", "cilmy", "wrsewtf", "luvtmo", "wftuh", "ifoeeqp", "dtfdhhl", "rwnburg", "fohkkul", "frqqi",
         "gsrcyc", "teuync", "dvpvak", "daqjki", "kksscp", "somsde", "tyfvck", "ftfekl", "ahncv", "yvosm", "qgllvg",
         "ylfwv", "jenqns", "lqovrnm", "iyger", "nfvtsv", "bknxmqj", "pfzybdr", "hqjol", "chlpk", "etgrtqa", "msuxdx",
         "vnoatf", "ypdzomn", "vsshmg", "rfkipq", "jvpbiz", "vbskd", "edsoixj", "uowim", "hqtsj", "inbsxal", "ookrv",
         "ipotdnk", "kmazqd", "jpfghb", "gvmnnpv", "juvwa", "xtkvzw", "ejqcl", "ebgcnt", "ztuyu", "dlzthw", "zzipe",
         "iaxwdxy", "htynwkc", "lefbq", "pizfr", "vttrsv", "oagak", "eqlrom", "vttefg", "dsrmk", "oekbe", "cvugzk",
         "diwvz", "gxmfob", "vjowzm", "mjpop", "uznhz", "kqvjwug", "wjqvxfg", "jbpwezu", "wsckdx", "slqfomn", "omuxk",
         "zlgblso", "kvitoq", "dmafq", "djxmzk", "pjqfegq", "yjrttas", "siakcx", "iutiqk", "nwfdj", "gbgtazk", "cpqtf",
         "panmlr", "aqubhsg", "iwdim", "nqetym", "mwazh", "thyhy", "ydtxan", "xfoin", "lsosc", "esznfa", "xgdisi",
         "flvbzh", "mpltx", "iwjpsqp", "udfycf", "rntmc", "ltflwu", "wkgbaw", "bcuzt", "hejxuhb", "lguohe", "klnhb",
         "mjump", "avcwrol", "yrcqlc", "ihxul", "avajh", "gtpauet", "iemzk", "rfdub", "gqnbk", "cfcmg", "iobyh",
         "iruuapf", "tyifwt", "sbdtp", "mngcpmb", "oaqpolm", "mmimmh", "gxknadi", "bmxhuu", "ulyoa", "keidy", "vsnfk",
         "cnnnfty", "pkajm", "ddgeecb", "prxidqd", "wmenvhd", "akjcqo", "tnekfef", "ipvsi", "pzjwq", "wmmct", "erdjnuf",
         "vgeaqs", "nlbdx", "dpvbe", "dgeqz", "aiguzh", "akawppx", "tykrjcs", "gvavo", "hkyle", "yhedx", "xzqcg",
         "gzdxt", "csssbk", "tmekrmv", "lfsgo", "iizahz", "aszfd", "aybqnsl", "vadwxsl", "ulmiii", "xaxdugp", "sfnnsbg",
         "dkyruh", "qhpqu", "amesjd", "evjuki", "vtqjw", "aoabp", "qnsuhe", "bplbx", "fdqok", "ozkhgib", "cggwzys",
         "nbknjay", "ooambw", "evmvegf", "htdlxik", "kahcume", "bojpn", "bhipie", "hdyjslw", "pbkkq", "qwszl",
         "fgkbzsd", "hejdx", "vmcfhgx", "puzlmmm", "meffil", "boakbiz", "eczot", "fvkkit", "jebfx", "umvkjg", "uikgs",
         "rycgpf", "rfmfgmy", "nveho", "bgywqen", "gepfma", "vquyq", "wcercbw", "wbpjkxc", "rqloeda", "omclokx",
         "hvotwp", "tvqfxxu", "qrtghk", "hggme", "arnmfnt", "cxprj", "rspdt", "hlgfq", "dmqel", "pcerxk", "ptqjc",
         "wzreko", "kahks", "xjnzo", "xzzye", "xbdeu", "koiwkv", "jlwkkjr", "xzdixoc", "xeedvrm", "mrtnhqi", "jaeann",
         "mvubp", "olklqf", "retbgcj", "qxxlhh", "cqyyoy", "ngwikg", "qijte", "sjzck", "zkmkx", "ongtzf", "tanow",
         "smgntvq", "urfgt", "xwcroa", "kadcpd", "cxhgo", "walku", "kvvcsyt", "elwmuxk", "bfphtm", "vzeumuq", "sknvev",
         "vbsnfd", "grmbg", "vjahwt", "dmcbmn", "smubz", "jobbfcv", "ujlkm", "lcthh", "bauuqdu", "kjgzgtq", "gicjz",
         "nugbax", "kbnjfiu", "sqfpein", "obbgfww", "ykggxjx", "irnmog", "xniuv", "rqiwycq", "hzlgyu", "yjtrttv",
         "satym", "dgqhlkk", "rghal", "tbekx", "kkwmo", "eahwhks", "bpvmbur", "sqtgkj", "khboz", "enefr", "vkzqvt",
         "wfruavu", "ninomu", "ypktaoa", "mlpmoit", "fxyhjfp", "fgnpp", "txieja", "dprnj", "bgyrp", "zsqwqrw", "stqzki",
         "kwiayb", "ulbsn", "aetje", "vwzbb", "tedwyqs", "cymiruy", "jigpoqx", "ypuqsc", "weletu", "gvibea", "chhuldm",
         "baylv", "wdhovo", "imfqu", "meodnsk", "jhlckqw", "jolyfh", "jsfkrhr", "tnbfzvs", "egcfht", "qnzmyr", "owtrqu",
         "oqaqu", "xftys", "goxfftm", "sgbnp", "bhfvaz", "gospa", "jwzlvwk", "lqncoqd", "xxizglc", "bwffm", "mhpggzr",
         "kdaoewx", "anviou", "mqiij", "wkskpn", "enougdh", "vldnn", "gbfgz", "ejmbh", "qsdrvsx", "mrvbz", "cqlufpf",
         "kbgjlu", "njgna", "admrmk", "pwwsc", "gxkot", "pdjwh", "ejwxt", "bpaxufv", "iwjzs", "xxfsg", "vuhgh",
         "srytgb", "yesvlux", "tggnch", "cgnbb", "fbzbx", "aomoqf", "zkrvrjg", "ueaoz", "dppacnl", "ewovhxz", "kbvee",
         "ixeeb", "gwgoqm", "hlwlxe", "fpmkrk", "wzjsr", "ispwe", "garofu", "jcmpec", "tggeo", "yzdeo", "axpmln",
         "zhnlhck", "duyqcn", "tpqwqi", "jvmaj", "bisgoy", "mpwmurb", "olqla", "ecapwan", "kcpxn", "xcapin", "ooctk",
         "sgqql", "vcyyjxf", "ejyom", "jsgtha", "logxnjg", "nypadhj", "dprmk", "cqkuzb", "gratv", "tgkjgu", "fttcafm",
         "tpryi", "ubbhw", "uwcuyn", "zkgohs", "snfesz", "ifrex", "tkbfz", "fvvkp", "otjiq", "lgomjjv", "ertracf",
         "bregu", "kkbizb", "hyhvn", "zjcnxfl", "mceskuj", "lmupdq", "zdzqzgo", "yorppew", "fpwtjd", "dxvyzt", "bbnnu",
         "pkycae", "ucvapn", "dijmkb", "nvwwpr", "bufkw", "zhono", "vayxf", "hlfwkev", "klkvkj", "yzgpwg", "lcbqr",
         "tkkfi", "pcgljx", "bhduxu", "rgfipts", "hkjbrr", "fobvy", "wqmqhxo", "yjgvypg", "ehgoizl", "ipiibzh",
         "aqxbxtx", "lrtin", "fyyuypr", "pyrocgm", "kwqbg", "ukccw", "wgsbpvx", "pcoivrv", "okhxaba", "bbuaibf",
         "ccvfm", "phpst", "yxtqiz", "cdfbo", "sijfljn", "gdlhn", "bqmbced", "tiejf", "aurqer", "olmyd", "prctay",
         "lwflhi", "bbehvta", "oxoda", "lklyc", "rzedhp", "kairil", "envan", "wdcwfk", "xoroddb", "womrlr", "ruxebe",
         "jnpywrd", "wrifvz", "zkewcd", "vllfrn", "uvdvjh", "bglpya", "vzokkbw", "apaoqt", "xpjizn", "xoajmd", "xapjwc",
         "jcknwg", "bjpreep", "ffkua", "ukcbah", "bugvkrf", "cbmmfs", "cwaczhl", "nsqaj", "sjeikg", "fayqif", "slowoh",
         "xjpvkpa", "ynunjle", "bqavt", "nkpqudr", "neikvd", "yuqlzg", "pdxbtrb", "cashlog", "iqiqy", "smjmxv",
         "zbtpbr", "zzamzcv", "jmakg", "txfswc", "pkaym", "swlde", "utann", "mqgpjne", "pslfvek", "nbiqhb", "bzsianu",
         "wnxgbi", "ahkeeiz", "dqdfjg", "bptdg", "pwita", "uqyflq", "txabjn", "yznjmve", "mukcqqf", "cxonbf", "ixuewjm",
         "pzlcat", "eikeeo", "scwsoa", "uaeyw", "oeorff", "gbqgd", "qboqiv", "hiulpb", "dbbdm", "qvdxx", "aypxbcn",
         "ykjwdbg", "pvfxn", "shrqyz", "zaxtu", "pfefgww", "jwifrw", "zxuud", "kpkwhlj", "lwptgd", "zpdmvsw", "takeb",
         "ynehl", "kixtod", "fyrgm", "qirzmr", "shyvec", "xjgzt", "bwfvht", "wyehh", "renzc", "nnibax", "slhfng",
         "yjtecc", "lghvbzf", "qroxvun", "mlsed", "rrudho", "cyffhh", "tjlxahp", "xmaepzk", "jvdzh", "bbvegrw", "cebcz",
         "odjpeam", "guerph", "tgmphgo", "ohtkqq", "jcxojz", "haeheae", "erydxni", "hatjxx", "kwmgkjw", "wmezvy",
         "hsuuvfi", "ineek", "grkxmhb", "alxkt", "rmspxdg"]) == 13956
    assert s.minimumLengthEncoding(["me", "time"]) == 5
    assert s.minimumLengthEncoding(
        ["yiyqbv", "njqvawn", "wnlovvp", "vogum", "jpolc", "zleec", "sxdrww", "rbowr", "xsjorra", "kwjsx", "vornum",
         "echku", "kuizegn", "rhuvv", "eemkh", "yshht", "pbixoa", "cmbxvtr", "iupia", "nmcbq", "mgrjsx", "ejvniwt",
         "svhsel", "kazenhf", "fevpm", "xcwqfgw", "ozikzc", "mywnmqt", "taorwjm", "gcshacq", "fgtasq", "qexygw",
         "ljmbari", "zfjudos", "rgxuzy", "kmzryaf", "exjfd", "mcqnebz", "ptoim", "zglfi", "fhneaz", "rexgc", "lhplwyr",
         "dthdp", "jizetec", "obyzg", "rqupa", "yphttge", "wdcdn", "wdomtr", "hchbd", "ytyra", "upytftl", "swbbi",
         "qpcybv", "dcoxspd", "dftkf", "nwjfmj", "ojbwy", "zofuy", "adqkt", "kpcply", "aeukw", "fqblb", "xurrbpo",
         "veioa", "puzvl", "bnzvlax", "tjzsdcw", "jarqr", "orxjbg", "ilrqdri", "syjuoyi", "htoqdco", "gwslw", "dpqyf",
         "jnkhv", "fpqhpr", "baewnvc", "caunsf", "qhbpe", "wlckl", "lmoroqe", "ddlak", "qipwbfp", "cefqs", "surczp",
         "jtmfuro", "ezhqau", "dlsco", "hywoqh", "lnifq", "hvfmu", "cqjdkok", "tggdact", "rwuowdk", "attnl", "lwhyq",
         "mqtsc", "bmwajiy", "nyohug", "vvfpt", "lbyazu", "sarwago", "iccztck", "ugsxcw", "rpwza", "yofmlll", "ulhdzhg",
         "lbaqk", "bwxxwc", "dmsbawg", "tjloy", "imbrkul", "xguke", "shlkuq", "lizjcdu", "kmvykl", "ilqxxjm", "rtbvvqt",
         "qisec", "zobzr", "thwntt", "afpifh", "uwiiovy", "hgsyecl", "pdgnm", "mqyesch", "suexztu", "msguuwu", "yrykkv",
         "xtoommc", "muteu", "bamml", "kkhlb", "jfrnx", "wpytor", "zzogpt", "yryxxt", "hzqofjd", "ehtildc", "ptclf",
         "nyltvd", "nrret", "qqqqt", "uuxunf", "jajxt", "lzdvlc", "gpdtjug", "hjsso", "jairua", "qarxuey", "rpwwjwv",
         "cjqypep", "tuzgcs", "oytqxb", "rgfmud", "stnwn", "tzzaop", "jpuopzg", "qeywd", "spnstrg", "dfwgntg", "yjyqk",
         "ioowc", "duqfg", "gmqxe", "xhlbby", "liurjk", "vdujfm", "xxyyn", "omapgc", "koemzbz", "ziiyako", "pjmhfrv",
         "bshtfgj", "ihjvt", "pnipuw", "fajiuj", "rdvcqzd", "mgknns", "ouwkm", "ejnklwc", "osepl", "gplpyvs", "paxrddg",
         "gsjlpd", "lgnmgl", "yifeeer", "hhnwlol", "fcmxs", "ilinwgm", "udhfdtq", "ceefc", "xweqx", "jfelwod",
         "rtywfjo", "kzwrgqx", "fcjriov", "fzytqv", "zcpcddo", "scpyzow", "kbzegu", "gclwr", "gmiwlp", "rtpka",
         "yiywuyy", "qceot", "dtrgn", "ntwbu", "fxobd", "zmxwza", "qcksyz", "wgbtmm", "pzorve", "hztydc", "jqlay",
         "ijdkbk", "uzjrps", "gfzibk", "gsxqj", "kgjrkdd", "smdeuk", "iwizewp", "owjie", "kcdccu", "ifltqr", "zrdfbm",
         "pznbcsk", "mtkpi", "cpasir", "flrxrm", "uxcxnv", "htlfcp", "ltukxfr", "ftbbha", "jhgjgyz", "qjreroc",
         "vcvtbid", "nrhlq", "gtkpot", "gyplqqg", "lnorig", "fixhufv", "ugcug", "ndfug", "wuorhe", "owocnkw", "rcnbf",
         "ioiiiui", "kakwtne", "svxtt", "wdrxogm", "ibrxs", "bddqi", "jeguac", "hlftdw", "nutgfjw", "krrzvf", "amxuloc",
         "deozdoe", "ovsvk", "sfqsl", "slgiw", "jbjujag", "mhiru", "uqksech", "davosw", "nlueljv", "rhtvdu", "ivdpdqa",
         "qnbenpq", "dtapqq", "hwwfpxl", "oyrfosn", "goxgmgo", "tbvutl", "cbbbcm", "iiugpk", "hinkem", "vvaitk",
         "pskyf", "hdnekg", "nqhfn", "dqbozx", "zcwpko", "kafyu", "jfegubk", "nofqzsk", "ujmxxg", "akwzemu", "yvhxb",
         "qqlwofi", "hmoecj", "qwgtlc", "jepvygq", "uzggm", "fztiews", "lvndvf", "vulax", "znqudh", "whgqi", "noguo",
         "vewkx", "uruvgf", "ubohmba", "aulzi", "flvfdlq", "yspfie", "wugif", "qndyiwa", "keihmct", "rggvn", "ojjmuoh",
         "sbbcl", "cdivmoz", "vkusmp", "mfddp", "kgohwvp", "rjbbxw", "vsgptj", "hbyjoz", "gufrv", "orxiv", "fxcqfw",
         "okppik", "qlouw", "lkryigo", "qccvc", "ixcnodg", "wlfilts", "ahqtevp", "kkbuha", "oehaez", "rzczib", "vxobk",
         "wmetvjs", "xfjgeq", "eadzl", "aeqdvch", "czojfq", "hxshidl", "ofswsj", "iwbqcmg", "schhwtt", "ltyth", "wiccu",
         "akill", "zaaji", "qepvfa", "mpvrkeu", "dcpenm", "wdhlk", "llqbby", "lronwkr", "rwtguo", "ofnvs", "lxdnwzf",
         "dctmilf", "zhckjd", "hajsuac", "wpylhy", "zhipvm", "ihikr", "zzwjgvr", "gdglrn", "skhow", "tlqtjl", "uypli",
         "evdva", "civide", "iroihm", "lvuzid", "vexat", "ngmvrz", "szdhbt", "ggrbz", "bsmovlt", "kguomvl", "onzvx",
         "nobgxw", "tqxemc", "vbiyx", "fpzpf", "ogtvf", "yuthri", "xszbn", "xcuhj", "nosnpbp", "mowsxg", "tfalyy",
         "kxombgm", "cukrz", "krmseq", "velzh", "kmufxj", "nvxlkq", "ualvras", "wytoucy", "qicqyym", "pbeujtv",
         "haojnbm", "xnfffpe", "wvoiald", "rlyvf", "sxamoxw", "ztqnmp", "biiavx", "lnjnzs", "arqdjdy", "pkrgokc",
         "qxswouj", "dgqah", "mnhzo", "ggilb", "qscrd", "ggvkimw", "qlxjys", "wximi", "aqlhio", "iavtvy", "grkqf",
         "dwrtut", "uozutfc", "fogxpdb", "ydtntlq", "vnmpmwp", "gtxhwq", "mlpihx", "yfpjlz", "hdvcquq", "nunny",
         "wklasgp", "wxduo", "topsqf", "tngcpzc", "mcrut", "pdnsmt", "kavaok", "seiqsqa", "bhgkiyt", "mawvhtp",
         "domcnrm", "fgusghc", "wdaufwz", "tzpuks", "kisndyz", "fwyieu", "wtdum", "ytxhl", "yhzkmuv", "nppnqe", "ccvhj",
         "dautnyq", "hkaliab", "kngan", "ebmhiop", "vsdkcef", "nmpcnd", "vxvnl", "cwcgu", "zsuneh", "qjgcmd", "awvba",
         "rzbisxo", "oilqrj", "neiazlm", "hlyrl", "tmiht", "lwqxxv", "gyblrw", "gnnjkb", "lrxiln", "xlwlseh", "npfwcvp",
         "yjcdhw", "rzndd", "orlhmip", "gatuojh", "osotgvv", "owksz", "kcocizf", "izlev", "smigns", "wtxfwo", "knwizte",
         "mqjojzp", "lkezye", "xqldbu", "cvbpyl", "aoipbz", "asrupt", "bdwkesh", "jpaykm", "pksbg", "gdbsibd", "lfxpwk",
         "rmnfph", "yzxwke", "xjwyusv", "yetar", "sytdz", "pnystzi", "yntcqo", "egoorl", "aydxu", "rfdrfhe", "flzkos",
         "mmjgev", "fbjwmvi", "jeouc", "lcmkri", "aggsb", "aaeazai", "amyxpey", "onxqpg", "qrjpxq", "zanea", "niwsgtv",
         "nsqja", "utgskd", "hlcum", "frygtl", "xjmqetz", "upqddd", "vxzdstm", "hcmtera", "ejstou", "xkcguf", "bokigdk",
         "vurnv", "zsgrje", "nbxlf", "tpilcx", "lvepux", "xacdtp", "amdgx", "ubbvnx", "xmvznh", "tlprri", "sthkn",
         "xhoad", "deotaxo", "pqzppmw", "xlcpx", "qwzrpyp", "lujabeb", "heskwyy", "mzzaaur", "vnestcs", "rryphdl",
         "ibdiabi", "eoiyt", "znflx", "clougix", "zzadxw", "lrrgtf", "lsdoakf", "yxfmqx", "qhnrry", "ktcdmv", "veygqu",
         "btjlo", "fcspsc", "gozoazm", "xcsqgz", "aazae", "nkuvask", "mzdgjq", "sihqdhy", "zadrwzw", "gzcyuea",
         "lpgccic", "fqtfuzw", "bjoqpkc", "oydpkxc", "sugnnu", "hyvygf", "axkxo", "rsmzb", "dlhqmac", "gbqby", "npqkj",
         "odbtb", "bdsib", "zyasxv", "ifxqcc", "lmnjwhr", "ibuyu", "uzhle", "ccpwhjr", "vhrojnz", "fkzfz", "fyesm",
         "dnvipvm", "jbbqn", "qdkgl", "xkvvgq", "dphugaf", "soxbfun", "rbgokx", "biveiz", "vbaqtn", "qapydgf", "llldu",
         "ottjpzu", "fwjuc", "cawio", "gbkwe", "rrnnxer", "luviy", "zsalse", "ckwdeox", "ozhqocm", "vtozfwz", "jztole",
         "ydqei", "bfugz", "psawjp", "dzlyrwp", "izuyrne", "rbwcfr", "vdvte", "usjbqs", "zzovkxr", "frfkwk", "mmtmdd",
         "sntka", "wachbzo", "rmzvj", "scbngo", "eqiuiwi", "qfakk", "cckcmt", "owhzow", "rejdlw", "iprsqdq", "twwaldw",
         "mfilzyk", "jygvx", "iewbo", "irhko", "zpazqhn", "ndqbg", "ayzxqdz", "zvpbh", "maapq", "pzitrfm", "qsgsurv",
         "viwcfff", "wpgenms", "tjmvu", "czuemc", "infxoo", "avhbw", "nugkqx", "xubakjp", "ndask", "utaqq", "njhuxq",
         "sdvuex", "tfmxqp", "bydovjo", "bizxjsp", "zoozxyv", "jegei", "gkpqobw", "psumbtg", "gkgoh", "sgcbpql",
         "xxkhy", "kdorkr", "hcomj", "ulrpyv", "rhplil", "tyyochd", "xhzul", "srdjmns", "kgukye", "yepvs", "xnobsjb",
         "umxmtub", "wvqasr", "igftpzw", "exhecn", "rreee", "jpxuvxh", "jriqf", "akexunb", "ekvdsoe", "ytzvj",
         "vfrlyae", "pmfai", "biouzle", "xkbce", "clzyi", "xhjoso", "wmxkxb", "dqzzig", "ydtby", "gskwj", "wlkwbz",
         "zepvllz", "zsgqp", "blntawk", "eynmil", "bdqyp", "wgtnqbc", "rrgaq", "gtafuzo", "qdiko", "kkcsdo", "zwqhs",
         "kugzbmf", "wtvvs", "kqsdx", "mxsuxiz", "pgbgjfe", "vodfr", "qbvwu", "vfwbhgw", "ayojye", "kolzfqg", "xnbecj",
         "akbcnf", "uutrn", "upmesa", "marqej", "bbucee", "bazqbau", "qikgsyf", "oeayzn", "uilxnzr", "vpnxknl",
         "btgtxgh", "vjaav", "zaxtzah", "msweps", "awduwld", "gzaep", "ngvgc", "qpoqdgn", "kimndg", "qilmmpw",
         "oafhlyp", "nyelgvw", "onymk", "feycbc", "dhcrx", "siqpfly", "tyvycmf", "huctqp", "uscjrp", "bbptd", "msdmu",
         "xlxhye", "xnyzcox", "kyskda", "injdkmp", "jiwus", "spjylwd", "eqcrnt", "snfiu", "jvwvge", "yfeaw", "mmdnsjj",
         "suzdw", "xiupf", "rjwjhng", "tqvasy", "rmibpa", "zuqax", "prpndnp", "efryqe", "pwuqfy", "wpqlfs", "aeswq",
         "cxkeiue", "jydxzfi", "tzfvwp", "zzgtw", "mupiusx", "sojavt", "dxmsgq", "migjiyj", "kixjk", "ywwvcpl",
         "khzcuo", "oykhx", "fochin", "foxbfkc", "sizjg", "wrjcvr", "ceadd", "tvfqgxq", "whzhche", "dcoeti", "mpilfib",
         "cphie", "ucpnjm", "ajltvx", "kpizym", "vevfsrs", "jznrri", "yvhxomr", "cbcnk", "yuwuhu", "jywuzed", "kqakusq",
         "jrnzgfo", "mjimzz", "mfjybnd", "ntqyq", "junxxck", "myvqajv", "kvuqs", "obfxw", "jwuba", "vnrvzvy", "aeric",
         "vtgda", "nkrocpt", "ahitg", "dzxtr", "zswwc", "yhxap", "fdhiwr", "cpxtqv", "izbmo", "zyioo", "vysnoe",
         "ouuyvj", "cumdhzn", "dbsmph", "cktjem", "vbmxy", "utgfyhc", "rqdeorp", "btnlmd", "chxwlt", "nsghoqi",
         "egycsm", "wkanat", "lzjyf", "donyx", "cchqsa", "xozzz", "yzmnf", "jfzuh", "dpcpg", "hlahz", "vobopk",
         "lssfeli", "ccttzi", "glzgqpv", "oyqzug", "qqhkrr", "euwotv", "hwbmtz", "hiylhly", "bppzne", "yetyyvs",
         "cnbwcby", "hzblk", "pfjmxt", "dsxvt", "vvkju", "zjrfr", "gdbhb", "udoad", "nbhpzfm", "iwetbym", "atmly",
         "tnxli", "myegb", "hiwqsk", "btrajk", "nhrmwn", "ftmbecv", "xopht", "eiikqy", "qizanwa", "cwxiatf", "jshjva",
         "llrtkn", "zhivu", "lmwiu", "oaeaqz", "oxotfub", "jnkafm", "juhrmq", "mqzbtw", "puiaxty", "dnahvoj", "gaxhz",
         "xfnay", "iqmlnlq", "xudhcg", "izpkz", "tqttmt", "bwnbs", "fdufd", "vhzyymh", "zhqtxr", "evbcrv", "xvnma",
         "dgcwy", "cwxzlbz", "oodiol", "teyim", "kqqfjub", "ftsqzi", "arfztkr", "oqlujx", "rpkkdov", "ptoff", "ivxaxr",
         "nxeept", "cacpl", "tehir", "spvggl", "qfzxkn", "bhwkukx", "fkdpuq", "xdrngre", "fnfplq", "dzbrl", "ufgxu",
         "sciec", "fgdydvw", "nmpaqxi", "ydsvfv", "natjz", "lruyvzf", "xznznxp", "mhfrh", "kddsk", "uwatn", "uklzs",
         "lnuta", "ryizc", "cvwko", "tnzpk", "ywpiv", "vbvcagq", "pzolw", "nmyfhg", "cshkofj", "ksptw", "kqejh",
         "zgzjqzo", "mxzrw", "enabosq", "vmubgc", "sfzcj", "hewvk", "ewhrq", "oifnsmi", "izdnvu", "cshgtk", "mqotuhd",
         "gnqgj", "rxailbm", "iyhxvtu", "ncjzklq", "zjmnoc", "awqwos", "ugujppc", "spbvfwl", "gntsvo", "euksu",
         "qnvneph", "crhmf", "brktmf", "mvgmr", "yzcskrp", "tihawec", "edqmxpn", "fxyymlr", "dzfkucm", "prldz",
         "gplrlhz", "bohwr", "bhebbk", "mmecj", "segydd", "ptslsb", "pyhgw", "cwmrq", "mjfhflh", "xhuid", "npxmb",
         "izilq", "dczhqh", "tgfnxtb", "zrylvo", "lctxrar", "ylhrbii", "rfxedv", "llvhzjq", "bjocv", "wbnex", "cnohnf",
         "xahrl", "rouvwyc", "hbhovgv", "dhucp", "ncmff", "ncsskg", "gsjbyin", "lroxscf", "whfaenl", "vsfultg",
         "floxkpy", "captoai", "qwolyex", "ggaypn", "wzunypd", "pjixeu", "gxnjkoc", "pqiqhn", "xakjmgz", "vqizkx",
         "gdzcxr", "kyxwdd", "pgxmazn", "qeuwf", "bduknm", "tcrcn", "nehgee", "wktbcgu", "jwqltdt", "wczkai", "drkqs",
         "qhdqnn", "oobxirc", "lbunv", "ifscr", "xnfpbrw", "yrrdbax", "fbocs", "tewne", "iobixe", "zgosas", "yhesn",
         "xlqwd", "pfcen", "slsjffx", "ilwatrc", "mhsmgp", "iteghl", "aqhufdl", "kxgpqcu", "ryrcgp", "azidf", "smlnl",
         "rocxvbt", "iutfc", "loapgbr", "musulp", "dqcnj", "tpgbkfh", "wvskii", "itkfopo", "kytyb", "rzahbu", "aewptd",
         "ohergbb", "cadxh", "aphwelj", "huooyzn", "gtttia", "izeyhcr", "cfvxz", "aitaxyp", "vypqost", "ebfnmif",
         "kgiucm", "zryyu", "oxgnbpt", "frpwo", "ouqvodl", "pdaazh", "gxwmf", "dozxsjm", "yndpsik", "zcwvu", "mihug",
         "jgodklw", "ysklw", "cfxqv", "yqvtz", "rctnp", "xjywa", "kpqyw", "hhtegzt", "rnwbeoi", "uyxqum", "jahcwbe",
         "jzjns", "ovwoaz", "oqmsrua", "natbejl", "deffv", "okgbr", "paqhy", "jkafhte", "lifsknp", "afmskh", "oemdro",
         "oxuwov", "qtyxa", "hkpfsm", "ulaubn", "tciurw", "myohwlo", "okuiejb", "ormoqsb", "gmipz", "hterzir", "ekxzre",
         "xkevge", "ihenf", "nnhzv", "eocjmx", "upzal", "oounfko", "myhbwub", "fwipva", "pkzzvpd", "nrupm", "vluzq",
         "fxkoyho", "atzktr", "aomrp", "qwpser", "ejagmb", "cfigelm", "bvanb", "cgcgabo", "hmjvlqt", "hxxocf", "ftqaud",
         "htuipy", "bhwmcn", "tgyvaqe", "lvuwh", "yiabzs", "rzzavu", "fiubm", "uuqsb", "riyakuf", "psscffd", "kvckzr",
         "fktmnf", "ivzqexi", "nhxzm", "kffjmb", "vdzxv", "esago", "bfikw", "gaiuxmz", "volokcm", "jypcs", "psibvs",
         "hxaxklf", "lmqwgy", "spnbimo", "mtihak", "xikoiy", "rmmtv", "phaqgxj", "zcuwkhk", "emodbyb", "ztahsya",
         "ieiqm", "lfoquh", "emznnq", "pnhlgut", "pgvads", "cqsjx", "lxnjei", "zpque", "rdjbiyb", "sxedpu", "potnqva",
         "iirkn", "rjmnrxd", "ksgcd", "waeymnh", "tizdz", "kproa", "wpttygd", "lvyze", "peewvgm", "fwtyzbw", "zitkk",
         "gfgqr", "udgvlz", "swqspo", "ohhvyq", "kgyuau", "hcerp", "pdomlm", "twabkk", "zfsea", "epiwp", "xgycjpt",
         "jtkdh", "mxmdm", "rtkzm", "qkacy", "nuvdiq", "agctak", "hypgyh", "ewtjp", "paysolw", "bcutebe", "xelxyb",
         "gzdvrth", "vpzfv", "cxrkt", "admiyzi", "lqlmn", "zbjpbg", "tlvdnli", "zetnox", "ylcsobo", "balajod", "igoume",
         "sxcgw", "sbkkafk", "fmndnnw", "incsa", "jyupkg", "uhvvc", "rswnbth", "nvprfj", "figqf", "znyidqi", "aijper",
         "euidr", "dftxkze", "vnppi", "splwifc", "fprgafl", "ixzaz", "mrhqtne", "dtkjsy", "dsmqrgy", "xfscz", "cymvmpu",
         "vptkfdx", "zrgrjq", "mqvwsur", "hdtlw", "ugdpwun", "cvxitc", "vytvqg", "pmtpfz", "nfdtdt", "umvwjuc", "jouxc",
         "qpypri", "pdhqp", "lmise", "wlsvcfg", "aqdkzcb", "qlrmrfz", "pbgoyi", "xmsskoh", "jjdye", "xvsdmq", "ymjeipy",
         "igjyv", "uiojvmc", "uckoww", "grlnyeg", "hpglp", "omnnyy", "iiliir", "cnucbcx", "pcxvs", "hipad", "xmiltkj",
         "oorwi", "qgoxjj", "jnmviqs", "wpleqn", "tudxw", "pcogem", "hgewaf", "niwfexy", "vcttgcb", "anjgovq",
         "epgmscd", "mdtru", "xvapv", "rydjik", "kopppcr", "mjbsmu", "unxoakz", "ldpsw", "frksjr", "vyxxg", "yyydri",
         "szidq", "qvbtd", "qratl", "xwfov", "bzhqyxl", "fskrtf", "pcpzmnv", "xuxwx", "vzbevnb", "ebaqz", "dbpuek",
         "ooqwj", "gaimp", "coelqh", "bwuceq", "oxpfjt", "zrqyc", "rwllk", "pqunv", "ufbnn", "tbnjoz", "kkqmrxu",
         "qyyrm", "hislf", "wyuck", "ubpre", "pdioi", "aryhv", "vdcxv", "rkgmaag", "czlzokw", "gtxuduz", "grpijx",
         "qzrar", "qhues", "rmznt", "sxxmved", "onjzuwl", "atbjhip", "nrardl", "alrocy", "cfkip", "ihtbf", "pqdgm",
         "hmokun", "dpghac", "otwml", "mnbzwa", "ehetlt", "rchvq", "lwjgywn", "lzdmjo", "nvhohdp", "tmshcpc", "gavjv",
         "ycnkv", "uynzh", "bvpnfjq", "lfbem", "qberui", "vrmmhx", "wpbqtfq", "jujpx", "dujgkof", "hrpbso", "zhcdt",
         "iybngyb", "rgeruza", "nesyxr", "cihgfe", "hjgskb", "zspxeqm", "inzrgyd", "crkjq", "iooshwp", "muvvj", "wakis",
         "rowibwa", "qikwypf", "aportho", "pubcgx", "vqoqpfi", "rnpbri", "ussjv", "looor", "xkzvdv", "tstegg",
         "zgiiokw", "rwvyaun", "mqqla", "asnqp", "nghuryl", "hlvhn", "ecuotnu", "judvbu", "xgvuw", "oeckn", "hdhttsg",
         "hcyhu", "klbyjc", "tnrmqnc", "mjojxhi", "kvdet", "vbmevim", "oglrzs", "afbscdi", "zxrffti", "firzgmz",
         "oenim", "wgpua", "asiep", "kyteq", "wpeneca", "qixmeoq", "zaofon", "csxxtr", "cpwmnl", "feylas", "idjuo",
         "mrtpvta", "jjvmjy", "mnljocc", "lnvjleq", "oognud", "rbyneq", "rhvomm", "fldrkpk", "znvrp", "myswmz", "jiloe",
         "juivjmo", "ylhbyzl", "ndmabkt", "sgdvlq", "pmnddmi", "utpuj", "kfisv", "nxfeell", "mxhgqd", "ccvdsdg",
         "emtybo", "zmkylbt", "mmrpi", "dkwlgq", "iwlappb", "uimsrnu", "mkxaxmi", "tcvll", "njggal", "kmqud", "evgzlh",
         "oaxizbp", "jiuej", "xknlp", "cyksydh", "gbixmz", "vtouyk", "sxjpkio", "qhubt", "kflvnb", "sjdfggl", "bxozyj",
         "xekbh", "wtmcb", "xtapfco", "rnornl", "ursdpki", "waonim", "eibfyed", "zniinaz", "uyfohq", "qcaxlt",
         "koyaapa", "pjuvbsi", "ecpdl", "ifaqwm", "yyumzc", "gvfngfp", "lttul", "flyza", "uasdlme", "oklhb", "wulkzzv",
         "ziwsxo", "jqcxiu", "qdzrwgm", "zjdwy", "uumns", "emlnp", "irnrqp", "gqkza", "oynpcz", "yxyea", "zpamf",
         "gyehxbv", "nplkhcc", "rxeekyo", "kecgp", "gseju", "nkisxqf", "vlyud", "fxxihhm", "yjgtml", "fehwpdi",
         "wclnvyy", "lriwrc", "ikparv", "volfh", "ysphh", "szrvrv", "rqlmz", "jyqut", "fyftsj", "uvwfip", "rngwgm",
         "mjwaz", "roehjki", "ploxokr", "yjbalp", "fspkq", "yfxrb", "kzulvk", "ordxp", "vdrrt", "wdiojwd", "ridzl",
         "niykdvu", "whyycmn", "riwcma", "bkhgkrb", "nsine", "emgtgf", "zoymw", "ljtvhzb", "kfyfdma", "piygxdl",
         "onfwgdf", "fwmkm", "vqbljay", "icife", "bxfli", "yeygr", "qenhgm", "mtxuckj", "kdcyx", "kwqhfcn", "ywkfy",
         "prbpw", "pheyc", "kmnds", "cacqs", "kvekiqy", "bfvfhdy", "gxulp", "skmcra", "exomt", "lcxue", "mnvvday",
         "rsddl", "gooegc", "udght", "doymnin", "ccdap", "wuive", "dyyln", "rynust", "luxabyg", "kdkkyyw", "vawqfsy",
         "rmeswm", "rcxzyv", "clpowz", "pdntqm", "tvjkkmz", "iiclw", "nhudzen", "cybhu", "crwtw", "enypnh", "ygekg",
         "hrjwqt", "peissge", "wangcy", "rbpoik", "raqulbf", "gyisnsj", "rgbqn", "lgvuzb", "djicf", "epnuu", "nsapc",
         "voatgh", "yorfehc", "jxfttat", "wyuivb", "bwopl", "odwdsh", "anchkv", "sepvew", "qoxxmae", "bpvqnj", "sngfo",
         "buoazou", "zhijssa", "janng", "uvdbd", "yfvkqo", "lcjii", "mvacvrz", "xztiar", "lpbtrqa", "ukbpdx", "okaqpgr",
         "idgqlj", "ewglgo", "ruymhi", "pcidw", "bvuqj", "npzch", "yppyan", "oiguirj", "iijvwqj", "jvbwjys", "yjtunfc",
         "iaikra", "oduhdgk", "ivixur", "ibcgai", "djzvcbx", "lmtsul", "lgnwzol", "wursq", "xsxbqwq", "jqvwnc",
         "dcwwvtb", "vwybnr", "bughwjl", "rnelxb", "hmacv", "ufgdygl", "aabuat", "oynwask", "gnfjjf", "zipbq", "zxstn",
         "jdrbprf", "jmkvny", "rblpql", "vykdj", "qaakyqw", "osbhddb", "avgldyy", "kvpoa", "fnqcliu", "zzlninw",
         "drsal", "omswys", "hwqcpct", "ecraq", "fvhsbjq", "raauy", "pfmoz", "vvqvcm", "tbjqjun", "jcfbegq", "otiwup",
         "axvvce", "dhpdnx", "pennr", "hvvmvzv", "binezl", "ygdmcuo", "ypwnqn", "aloxdv", "ucieh", "kovbtag", "rgfpaww",
         "fpbftg", "spjowfr", "zridoy", "blwbbf", "evwlxi", "itbcz", "hgixuo", "qmoqmjb", "tkeeis", "pjiaq", "rbpje",
         "ledoui", "ubecht", "mphdd", "uzswsbb", "ntsybr", "qmnijyp", "pqwawe", "ltytill", "dpnxy", "pkxqcol", "ayrdi",
         "mycnd", "knotsn", "zvcrjl", "qwroblg", "vtrktey", "dzilezi", "wzkxg", "varqc", "xlpttyc", "xxqhnl", "jpxywa",
         "kjdsh", "hdseebw", "bxqbp", "flazqce", "xrtab", "rupsfq", "asswer", "rhqof", "hjzdv", "addsgax", "cuahzjj",
         "xwdilr", "osqgg", "pfhwv", "rqorah", "ggdlnv", "truvaoj", "jzuldwf", "mjddj", "vixtn", "eslxoaj", "cmoypm",
         "jvvzs", "oqgxcc", "tptls", "wwgwbj", "tysuhg", "xbnqb", "iogjvg", "fbxdmr", "zdvsmx", "hiuja", "watrt",
         "kjawab", "entxk", "jmnkaox", "zznsox", "asmzc", "soblvp", "quyxjw", "udrdc", "hyylvvw", "gzfwxuv", "jjqmjw",
         "faegxbl", "lqjcg", "bzmruq", "bykuh", "miwhd", "ykgtwhk", "oyobzwi", "oltwpua", "ctulabr", "dwandd", "vhuhox",
         "vtlknw", "ywvln", "qemqdeg", "akezvx", "kjmjpv", "vwuftx", "kreaxnj", "fvfop", "cxabs", "jfacbje", "eecnz",
         "cmblit", "gfvpoq", "whywnh", "pghvx", "ohgkmf", "xxtiwd", "nkojni", "dlcicnp", "bwyvyyd", "gifup", "vgjfr",
         "hhteifi", "kjhffq", "pawqaxl", "yozro", "slxluvd", "amqcquy", "vnnxkr", "wgdur", "rvawiu", "thcwnc", "cddut",
         "vnrtrv", "fnfio", "nhvxe", "rfdqmj", "ucblh", "ccbnt", "lxckaoy", "fnwcbx", "gmdbiwt", "ypvwjy", "cbjazk",
         "qmujnm", "nsqot", "lhcqt", "ijxcts", "nujrms", "itxel", "ghukr", "qpwitlr", "gcafqrn", "lcoho", "lfzab",
         "vwhgceb", "vgsgy", "jrtgo", "ryxlz", "deoyq", "ybenly", "lyysca", "sodvazo", "hbnnoz", "ovgvda", "elwtjx",
         "soydmn", "trdsi", "mwwjwo", "vupwj", "dszpcv", "kkhjdj", "ewmyo", "nmpeq", "oepldcq", "xttrgu", "wbcbxi",
         "jakzk", "peukyw", "fvcqv", "xklwuu", "hsmva", "kslmkq", "azllbig", "stnzih", "wfyud", "ihauy", "cfxmj",
         "pdyogwv", "dcqdpa", "xhusy", "jfpmpmm", "odeiiw", "ozyaer", "uykzvma", "tuaznxj", "kdnbdki", "syrnsem",
         "fdysz", "hhrpo", "fglzfi", "vgcqzqm", "qhsjr", "bvboe", "dpfwpvg", "mvvry", "itnnr", "lgykbe", "pscow",
         "mkrgeqv", "czffv", "apteht", "jeqixsx", "ksmbe", "zamivv", "vvmyo", "cwwoce", "sppubxc", "qaich", "nmbxr",
         "tfkwfxi", "iakhezl", "fxujis", "fkwffe", "antaylq", "mmfgstq", "zxaacy", "zlswx", "pbqxil", "eupck",
         "qzcxpbe", "rjalbzr", "wioagbq", "kreec", "zsdcuft", "rrdzb", "ocdlvq", "oxiroo", "zcxsqh", "wbrsi", "fqike",
         "oskzupi", "thvof", "dicbyst", "iojwe", "hyfizq", "yoknhww", "nupiyyn", "ievah", "slcgmxg", "cnecpa", "lcwsoj",
         "hnqsc", "ghipbi", "exobr", "nwpnq", "dmhbj", "amdbmwl", "xfbzovs", "puizvu", "yvsus", "ykysqg", "bgqdv",
         "zgqbr", "zkjpkej", "crkot", "zciymk", "tleogn", "sayrmz", "elwma", "zugjva", "uifwsmw", "wstrg", "xbotd",
         "hinsg", "qpgyoyp", "xzfocdy", "mbvuepb", "dtphufk", "cyapnt", "yyehhad", "ohdrd", "mlibm", "qzdfil",
         "rdwszqx", "bzcbmyn", "uarjlg", "mtwpqmx", "nmagl", "cepniel", "tylvaa", "melhd", "jygeneg", "fdglfy",
         "xcpciu", "ayrel", "bxceshv", "kspyg", "iclkaz", "ykbzt", "nrnkzo", "kxkto", "fabzszn", "edalls", "nilmh",
         "wwawgnn", "gymbtx", "mzipa", "ajevx", "qppisv", "otqhsf", "ippxak", "bixnqd", "uqitwo", "soxcug", "loiscd",
         "wqrjk", "rqntoa", "fzpxlp", "tuaob", "pyqqms", "krbzmmj", "aijqpfg", "nstqrbu", "wmtiahz", "joplby", "jyszxq",
         "jnxtyhe", "lbvfv"]) == 14011
