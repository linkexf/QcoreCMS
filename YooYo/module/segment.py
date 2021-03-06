#coding=utf-8
import urllib
import urllib2
import tornado.escape

class sina:


    isDev = True

    '''
    POSTAG_ID_A = 10 (line 182)
    形容词

    POSTAG_ID_AD = 210 (line 627)
    副形词(直接作状语的形容词)

    POSTAG_ID_AN = 211 (line 632)
    名形词(具有名词功能的形容词)

    POSTAG_ID_B = 20 (line 187)
    区别词

    POSTAG_ID_C = 30 (line 192)
    连词

    POSTAG_ID_C_N = 31 (line 197)
    体词连接

    POSTAG_ID_C_Z = 32 (line 202)
    分句连接

    POSTAG_ID_D = 40 (line 207)
    副词

    POSTAG_ID_D_B = 41 (line 212)
    副词("不")

    POSTAG_ID_D_M = 42 (line 217)
    副词("没")

    POSTAG_ID_E = 50 (line 222)
    叹词

    POSTAG_ID_F = 60 (line 227)
    方位词

    POSTAG_ID_F_N = 62 (line 237)
    方位短语(名词+方位词“地上”)

    POSTAG_ID_F_S = 61 (line 232)
    方位短语(处所词+方位词)

    POSTAG_ID_F_V = 63 (line 242)
    方位短语(动词+方位词“取前”)

    POSTAG_ID_F_Z = 64 (line 247)
    方位短语(动词+方位词“取前”)

    POSTAG_ID_H = 70 (line 252)
    前接成分

    POSTAG_ID_H_M = 71 (line 257)
    数词前缀(“数”---数十)

    POSTAG_ID_H_N = 74 (line 272)
    姓氏

    POSTAG_ID_H_NR = 73 (line 267)
    姓氏

    POSTAG_ID_H_T = 72 (line 262)
    时间词前缀(“公元”“明永乐”)

    POSTAG_ID_K = 80 (line 277)
    后接成分

    POSTAG_ID_K_M = 81 (line 282)
    数词后缀(“来”--,十来个)

    POSTAG_ID_K_N = 83 (line 292)
    名词后缀(“们”)

    POSTAG_ID_K_NS = 87 (line 312)
    状态词后缀(“然”)

    POSTAG_ID_K_NT = 86 (line 307)
    状态词后缀(“然”)

    POSTAG_ID_K_S = 84 (line 297)
    处所词后缀(“苑”“里”)

    POSTAG_ID_K_T = 82 (line 287)
    时间词后缀(“初”“末”“时”)

    POSTAG_ID_K_Z = 85 (line 302)
    状态词后缀(“然”)

    POSTAG_ID_M = 90 (line 317)
    数词

    POSTAG_ID_MQ = 201 (line 617)
    数量短语(“叁个”)

    POSTAG_ID_N = 95 (line 322)
    名词

    POSTAG_ID_NS = 101 (line 352)
    名处词

    POSTAG_ID_NS_Z = 102 (line 357)
    地名(名处词专指：“中国”)

    POSTAG_ID_N_M = 103 (line 362)
    n-m,数词开头的名词(三个学生)

    POSTAG_ID_N_RB = 104 (line 367)
    n-rb,以区别词/代词开头的名词(该学校，该生)

    POSTAG_ID_N_RZ = 96 (line 327)
    人名(“毛泽东”)

    POSTAG_ID_N_T = 97 (line 332)
    机构团体(“团”的声母为t，名词代码n和t并在一起。“公司”)

    POSTAG_ID_N_TA = 98 (line 337)
    POSTAG_ID_N_TZ = 99 (line 342)
    机构团体名("北大")

    POSTAG_ID_N_Z = 100 (line 347)
    其他专名(“专”的声母的第1个字母为z，名词代码n和z并在一起。)

    POSTAG_ID_O = 107 (line 372)
    拟声词

    POSTAG_ID_P = 108 (line 377)
    介词

    POSTAG_ID_Q = 110 (line 382)
    量词

    POSTAG_ID_Q_H = 113 (line 397)
    货币量词(“元”“美元”“英镑”)

    POSTAG_ID_Q_T = 112 (line 392)
    时间量词(“年”“月”“期”)

    POSTAG_ID_Q_V = 111 (line 387)
    动量词(“趟”“遍”)

    POSTAG_ID_R = 120 (line 402)
    代词

    POSTAG_ID_RQ = 202 (line 622)
    代量短语(“这个”)

    POSTAG_ID_R_B = 127 (line 437)
    区别词性代词(“某”“每”)

    POSTAG_ID_R_D = 121 (line 407)
    副词性代词(“怎么”)

    POSTAG_ID_R_M = 122 (line 412)
    数词性代词(“多少”)

    POSTAG_ID_R_N = 123 (line 417)
    名词性代词(“什么”“谁”)

    POSTAG_ID_R_S = 124 (line 422)
    处所词性代词(“哪儿”)

    POSTAG_ID_R_T = 125 (line 427)
    时间词性代词(“何时”)

    POSTAG_ID_R_Z = 126 (line 432)
    谓词性代词(“怎么样”)

    POSTAG_ID_S = 130 (line 442)
    处所词(取英语space的第1个字母。“东部”)

    POSTAG_ID_SP = 200 (line 612)
    不及物谓词(主谓结构“腰酸”“头疼”)

    POSTAG_ID_SPACE = 230 (line 647)
    空格

    POSTAG_ID_S_Z = 131 (line 447)
    处所词(取英语space的第1个字母。“东部”)

    POSTAG_ID_T = 132 (line 452)
    时间词(取英语time的第1个字母)

    POSTAG_ID_T_Z = 133 (line 457)
    时间专指(“唐代”“西周”)

    POSTAG_ID_U = 140 (line 462)
    助词

    POSTAG_ID_UNKNOW = 0 (line 177)
    不知道

    POSTAG_ID_U_C = 143 (line 477)
    补语助词(“得”)

    POSTAG_ID_U_D = 142 (line 472)
    状语助词(“地”)

    POSTAG_ID_U_N = 141 (line 467)
    定语助词(“的”)

    POSTAG_ID_U_S = 145 (line 487)
    体词后助词(“等、等等”)

    POSTAG_ID_U_SO = 146 (line 492)
    助词(“所”)

    POSTAG_ID_U_Z = 144 (line 482)
    谓词后助词(“了、着、过”)

    POSTAG_ID_V = 170 (line 537)
    及物动词(取英语动词verb的第一个字母。)

    POSTAG_ID_VD = 212 (line 637)
    副动词(直接作状语的动词)

    POSTAG_ID_VN = 213 (line 642)
    名动词(指具有名词功能的动词)

    POSTAG_ID_V_A = 176 (line 567)
    助动词(“应该”“能够”)

    POSTAG_ID_V_E = 172 (line 547)
    动补结构动词(“取出”“放到”)

    POSTAG_ID_V_O = 171 (line 542)
    不及物谓词(谓宾结构“剃头”)

    POSTAG_ID_V_Q = 175 (line 562)
    趋向动词(“来”“去”“进来”)

    POSTAG_ID_V_SH = 173 (line 552)
    动词“是”

    POSTAG_ID_V_YO = 174 (line 557)
    动词“有”

    POSTAG_ID_W = 150 (line 497)
    标点符号

    POSTAG_ID_W_D = 151 (line 502)
    顿号(“、”)

    POSTAG_ID_W_H = 156 (line 527)
    中缀型符号

    POSTAG_ID_W_L = 154 (line 517)
    搭配型标点左部

    POSTAG_ID_W_R = 155 (line 522)
    搭配型标点右部(“》”“]”“）”)

    POSTAG_ID_W_S = 153 (line 512)
    分句尾标点(“，”“；”)

    POSTAG_ID_W_SP = 152 (line 507)
    句号(“。”)

    POSTAG_ID_X = 190 (line 577)
    语素字

    POSTAG_ID_X_B = 196 (line 607)
    状态词语素(“伟”“芳”)

    POSTAG_ID_X_N = 191 (line 582)
    名词语素(“琥”)

    POSTAG_ID_X_S = 193 (line 592)
    处所词语素(“中”“日”“美”)

    POSTAG_ID_X_T = 194 (line 597)
    时间词语素(“唐”“宋”“元”)

    POSTAG_ID_X_V = 192 (line 587)
    动词语素(“酹”)

    POSTAG_ID_X_Z = 195 (line 602)
    状态词语素(“伟”“芳”)

    POSTAG_ID_Y = 160 (line 532)
    语气词(取汉字“语”的声母。“吗”“吧”“啦”)

    POSTAG_ID_Z = 180 (line 572)
    状态词(不及物动词,v-o、sp之外的不及物动词)
    '''

    @staticmethod
    def word(text , isDev=None) :
        if None == isDev : isDev = sina.isDev
        if isDev :
            args = urllib.urlencode([('context', text),])
            req = urllib2.Request('http://3.9diary2.sinaapp.com/api/segment?' + args) 
            res = urllib2.urlopen( req ) 
            ret = res.read() 
            res.close() 
        else :
            _SEGMENT_BASE_URL = 'http://segment.sae.sina.com.cn/urlclient.php'
            payload = urllib.urlencode([('context', text),])
            args = urllib.urlencode([('word_tag', 1), ('encoding', 'UTF-8'),])
            url = _SEGMENT_BASE_URL + '?' + args
            ret = urllib2.urlopen(url, payload).read()
        
        return tornado.escape.json_decode(ret)
        