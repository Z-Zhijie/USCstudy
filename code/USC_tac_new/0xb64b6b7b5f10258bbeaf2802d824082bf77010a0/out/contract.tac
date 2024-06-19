function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[0x1a, 0x4700]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x464a: v464a(0x4700) = CONST 
    0x464b: JUMPI v464a(0x4700), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x125, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x9204aac6) = CONST 
    0x26: v26 = GT v21(0x9204aac6), v1f
    0x27: v27(0x125) = CONST 
    0x2a: JUMPI v27(0x125), v26

    Begin block 0x125
    prev=[0x1a], succ=[0x1a8, 0x131]
    =================================
    0x127: v127(0x485cc955) = CONST 
    0x12c: v12c = GT v127(0x485cc955), v1f
    0x12d: v12d(0x1a8) = CONST 
    0x130: JUMPI v12d(0x1a8), v12c

    Begin block 0x1a8
    prev=[0x125], succ=[0x1ef, 0x1b4]
    =================================
    0x1aa: v1aa(0x158ef93e) = CONST 
    0x1af: v1af = GT v1aa(0x158ef93e), v1f
    0x1b0: v1b0(0x1ef) = CONST 
    0x1b3: JUMPI v1b0(0x1ef), v1af

    Begin block 0x1ef
    prev=[0x1a8], succ=[0x4694, 0x1fa]
    =================================
    0x1f1: v1f1(0xfdd58e) = CONST 
    0x1f5: v1f5 = EQ v1f1(0xfdd58e), v1f
    0x468c: v468c(0x4694) = CONST 
    0x468d: JUMPI v468c(0x4694), v1f5

    Begin block 0x4694
    prev=[0x1ef], succ=[]
    =================================
    0x4695: v4695(0x220) = CONST 
    0x4696: CALLPRIVATE v4695(0x220)

    Begin block 0x1fa
    prev=[0x1ef], succ=[0x4697, 0x205]
    =================================
    0x1fb: v1fb(0x1ffc9a7) = CONST 
    0x200: v200 = EQ v1fb(0x1ffc9a7), v1f
    0x468e: v468e(0x4697) = CONST 
    0x468f: JUMPI v468e(0x4697), v200

    Begin block 0x4697
    prev=[0x1fa], succ=[]
    =================================
    0x4698: v4698(0x25e) = CONST 
    0x4699: CALLPRIVATE v4698(0x25e)

    Begin block 0x205
    prev=[0x1fa], succ=[0x469a, 0x210]
    =================================
    0x206: v206(0x2fe5305) = CONST 
    0x20b: v20b = EQ v206(0x2fe5305), v1f
    0x4690: v4690(0x469a) = CONST 
    0x4691: JUMPI v4690(0x469a), v20b

    Begin block 0x469a
    prev=[0x205], succ=[]
    =================================
    0x469b: v469b(0x299) = CONST 
    0x469c: CALLPRIVATE v469b(0x299)

    Begin block 0x210
    prev=[0x205], succ=[0x469d, 0x21b]
    =================================
    0x211: v211(0xe89341c) = CONST 
    0x216: v216 = EQ v211(0xe89341c), v1f
    0x4692: v4692(0x469d) = CONST 
    0x4693: JUMPI v4692(0x469d), v216

    Begin block 0x469d
    prev=[0x210], succ=[]
    =================================
    0x469e: v469e(0x33f) = CONST 
    0x469f: CALLPRIVATE v469e(0x33f)

    Begin block 0x21b
    prev=[0x210], succ=[]
    =================================
    0x21c: v21c(0x0) = CONST 
    0x21f: REVERT v21c(0x0), v21c(0x0)

    Begin block 0x1b4
    prev=[0x1a8], succ=[0x46a0, 0x1bf]
    =================================
    0x1b5: v1b5(0x158ef93e) = CONST 
    0x1ba: v1ba = EQ v1b5(0x158ef93e), v1f
    0x4682: v4682(0x46a0) = CONST 
    0x4683: JUMPI v4682(0x46a0), v1ba

    Begin block 0x46a0
    prev=[0x1b4], succ=[]
    =================================
    0x46a1: v46a1(0x3d1) = CONST 
    0x46a2: CALLPRIVATE v46a1(0x3d1)

    Begin block 0x1bf
    prev=[0x1b4], succ=[0x46a3, 0x1ca]
    =================================
    0x1c0: v1c0(0x2de041f9) = CONST 
    0x1c5: v1c5 = EQ v1c0(0x2de041f9), v1f
    0x4684: v4684(0x46a3) = CONST 
    0x4685: JUMPI v4684(0x46a3), v1c5

    Begin block 0x46a3
    prev=[0x1bf], succ=[]
    =================================
    0x46a4: v46a4(0x3d9) = CONST 
    0x46a5: CALLPRIVATE v46a4(0x3d9)

    Begin block 0x1ca
    prev=[0x1bf], succ=[0x46a6, 0x1d5]
    =================================
    0x1cb: v1cb(0x2eb2c2d6) = CONST 
    0x1d0: v1d0 = EQ v1cb(0x2eb2c2d6), v1f
    0x4686: v4686(0x46a6) = CONST 
    0x4687: JUMPI v4686(0x46a6), v1d0

    Begin block 0x46a6
    prev=[0x1ca], succ=[]
    =================================
    0x46a7: v46a7(0x41b) = CONST 
    0x46a8: CALLPRIVATE v46a7(0x41b)

    Begin block 0x1d5
    prev=[0x1ca], succ=[0x46a9, 0x1e0]
    =================================
    0x1d6: v1d6(0x3092afd5) = CONST 
    0x1db: v1db = EQ v1d6(0x3092afd5), v1f
    0x4688: v4688(0x46a9) = CONST 
    0x4689: JUMPI v4688(0x46a9), v1db

    Begin block 0x46a9
    prev=[0x1d5], succ=[]
    =================================
    0x46aa: v46aa(0x5dc) = CONST 
    0x46ab: CALLPRIVATE v46aa(0x5dc)

    Begin block 0x1e0
    prev=[0x1d5], succ=[0x1eb, 0x46ac]
    =================================
    0x1e1: v1e1(0x40c10f19) = CONST 
    0x1e6: v1e6 = EQ v1e1(0x40c10f19), v1f
    0x468a: v468a(0x46ac) = CONST 
    0x468b: JUMPI v468a(0x46ac), v1e6

    Begin block 0x1eb
    prev=[0x1e0], succ=[0x3d4a]
    =================================
    0x1eb: v1eb(0x3d4a) = CONST 
    0x1ee: JUMP v1eb(0x3d4a)

    Begin block 0x3d4a
    prev=[0x1eb], succ=[]
    =================================
    0x3d4b: v3d4b(0x0) = CONST 
    0x3d4e: REVERT v3d4b(0x0), v3d4b(0x0)

    Begin block 0x46ac
    prev=[0x1e0], succ=[]
    =================================
    0x46ad: v46ad(0x602) = CONST 
    0x46ae: CALLPRIVATE v46ad(0x602)

    Begin block 0x131
    prev=[0x125], succ=[0x177, 0x13c]
    =================================
    0x132: v132(0x6c0360eb) = CONST 
    0x137: v137 = GT v132(0x6c0360eb), v1f
    0x138: v138(0x177) = CONST 
    0x13b: JUMPI v138(0x177), v137

    Begin block 0x177
    prev=[0x131], succ=[0x46af, 0x183]
    =================================
    0x179: v179(0x485cc955) = CONST 
    0x17e: v17e = EQ v179(0x485cc955), v1f
    0x467a: v467a(0x46af) = CONST 
    0x467b: JUMPI v467a(0x46af), v17e

    Begin block 0x46af
    prev=[0x177], succ=[]
    =================================
    0x46b0: v46b0(0x62e) = CONST 
    0x46b1: CALLPRIVATE v46b0(0x62e)

    Begin block 0x183
    prev=[0x177], succ=[0x46b2, 0x18e]
    =================================
    0x184: v184(0x4e1273f4) = CONST 
    0x189: v189 = EQ v184(0x4e1273f4), v1f
    0x467c: v467c(0x46b2) = CONST 
    0x467d: JUMPI v467c(0x46b2), v189

    Begin block 0x46b2
    prev=[0x183], succ=[]
    =================================
    0x46b3: v46b3(0x65c) = CONST 
    0x46b4: CALLPRIVATE v46b3(0x65c)

    Begin block 0x18e
    prev=[0x183], succ=[0x46b5, 0x199]
    =================================
    0x18f: v18f(0x4fb2e45d) = CONST 
    0x194: v194 = EQ v18f(0x4fb2e45d), v1f
    0x467e: v467e(0x46b5) = CONST 
    0x467f: JUMPI v467e(0x46b5), v194

    Begin block 0x46b5
    prev=[0x18e], succ=[]
    =================================
    0x46b6: v46b6(0x7cf) = CONST 
    0x46b7: CALLPRIVATE v46b6(0x7cf)

    Begin block 0x199
    prev=[0x18e], succ=[0x1a4, 0x46b8]
    =================================
    0x19a: v19a(0x540865fe) = CONST 
    0x19f: v19f = EQ v19a(0x540865fe), v1f
    0x4680: v4680(0x46b8) = CONST 
    0x4681: JUMPI v4680(0x46b8), v19f

    Begin block 0x1a4
    prev=[0x199], succ=[0x3d26]
    =================================
    0x1a4: v1a4(0x3d26) = CONST 
    0x1a7: JUMP v1a4(0x3d26)

    Begin block 0x3d26
    prev=[0x1a4], succ=[]
    =================================
    0x3d27: v3d27(0x0) = CONST 
    0x3d2a: REVERT v3d27(0x0), v3d27(0x0)

    Begin block 0x46b8
    prev=[0x199], succ=[]
    =================================
    0x46b9: v46b9(0x7f5) = CONST 
    0x46ba: CALLPRIVATE v46b9(0x7f5)

    Begin block 0x13c
    prev=[0x131], succ=[0x46bb, 0x147]
    =================================
    0x13d: v13d(0x6c0360eb) = CONST 
    0x142: v142 = EQ v13d(0x6c0360eb), v1f
    0x4670: v4670(0x46bb) = CONST 
    0x4671: JUMPI v4670(0x46bb), v142

    Begin block 0x46bb
    prev=[0x13c], succ=[]
    =================================
    0x46bc: v46bc(0x821) = CONST 
    0x46bd: CALLPRIVATE v46bc(0x821)

    Begin block 0x147
    prev=[0x13c], succ=[0x46be, 0x152]
    =================================
    0x148: v148(0x6d70f7ae) = CONST 
    0x14d: v14d = EQ v148(0x6d70f7ae), v1f
    0x4672: v4672(0x46be) = CONST 
    0x4673: JUMPI v4672(0x46be), v14d

    Begin block 0x46be
    prev=[0x147], succ=[]
    =================================
    0x46bf: v46bf(0x829) = CONST 
    0x46c0: CALLPRIVATE v46bf(0x829)

    Begin block 0x152
    prev=[0x147], succ=[0x46c1, 0x15d]
    =================================
    0x153: v153(0x70c2f239) = CONST 
    0x158: v158 = EQ v153(0x70c2f239), v1f
    0x4674: v4674(0x46c1) = CONST 
    0x4675: JUMPI v4674(0x46c1), v158

    Begin block 0x46c1
    prev=[0x152], succ=[]
    =================================
    0x46c2: v46c2(0x84f) = CONST 
    0x46c3: CALLPRIVATE v46c2(0x84f)

    Begin block 0x15d
    prev=[0x152], succ=[0x46c4, 0x168]
    =================================
    0x15e: v15e(0x7a2a4b32) = CONST 
    0x163: v163 = EQ v15e(0x7a2a4b32), v1f
    0x4676: v4676(0x46c4) = CONST 
    0x4677: JUMPI v4676(0x46c4), v163

    Begin block 0x46c4
    prev=[0x15d], succ=[]
    =================================
    0x46c5: v46c5(0x8d2) = CONST 
    0x46c6: CALLPRIVATE v46c5(0x8d2)

    Begin block 0x168
    prev=[0x15d], succ=[0x173, 0x46c7]
    =================================
    0x169: v169(0x8a89bb14) = CONST 
    0x16e: v16e = EQ v169(0x8a89bb14), v1f
    0x4678: v4678(0x46c7) = CONST 
    0x4679: JUMPI v4678(0x46c7), v16e

    Begin block 0x173
    prev=[0x168], succ=[0x3d02]
    =================================
    0x173: v173(0x3d02) = CONST 
    0x176: JUMP v173(0x3d02)

    Begin block 0x3d02
    prev=[0x173], succ=[]
    =================================
    0x3d03: v3d03(0x0) = CONST 
    0x3d06: REVERT v3d03(0x0), v3d03(0x0)

    Begin block 0x46c7
    prev=[0x168], succ=[]
    =================================
    0x46c8: v46c8(0x99f) = CONST 
    0x46c9: CALLPRIVATE v46c8(0x99f)

    Begin block 0x2b
    prev=[0x1a], succ=[0xad, 0x36]
    =================================
    0x2c: v2c(0xac8a584a) = CONST 
    0x31: v31 = GT v2c(0xac8a584a), v1f
    0x32: v32(0xad) = CONST 
    0x35: JUMPI v32(0xad), v31

    Begin block 0xad
    prev=[0x2b], succ=[0xf4, 0xb9]
    =================================
    0xaf: vaf(0xa22cb465) = CONST 
    0xb4: vb4 = GT vaf(0xa22cb465), v1f
    0xb5: vb5(0xf4) = CONST 
    0xb8: JUMPI vb5(0xf4), vb4

    Begin block 0xf4
    prev=[0xad], succ=[0x100, 0x46ca]
    =================================
    0xf6: vf6(0x9204aac6) = CONST 
    0xfb: vfb = EQ vf6(0x9204aac6), v1f
    0x4668: v4668(0x46ca) = CONST 
    0x4669: JUMPI v4668(0x46ca), vfb

    Begin block 0x100
    prev=[0xf4], succ=[0x46cd, 0x10b]
    =================================
    0x101: v101(0x983b2d56) = CONST 
    0x106: v106 = EQ v101(0x983b2d56), v1f
    0x466a: v466a(0x46cd) = CONST 
    0x466b: JUMPI v466a(0x46cd), v106

    Begin block 0x46cd
    prev=[0x100], succ=[]
    =================================
    0x46ce: v46ce(0x9f5) = CONST 
    0x46cf: CALLPRIVATE v46ce(0x9f5)

    Begin block 0x10b
    prev=[0x100], succ=[0x46d0, 0x116]
    =================================
    0x10c: v10c(0x9870d7fe) = CONST 
    0x111: v111 = EQ v10c(0x9870d7fe), v1f
    0x466c: v466c(0x46d0) = CONST 
    0x466d: JUMPI v466c(0x46d0), v111

    Begin block 0x46d0
    prev=[0x10b], succ=[]
    =================================
    0x46d1: v46d1(0xa1b) = CONST 
    0x46d2: CALLPRIVATE v46d1(0xa1b)

    Begin block 0x116
    prev=[0x10b], succ=[0x121, 0x46d3]
    =================================
    0x117: v117(0x9dc29fac) = CONST 
    0x11c: v11c = EQ v117(0x9dc29fac), v1f
    0x466e: v466e(0x46d3) = CONST 
    0x466f: JUMPI v466e(0x46d3), v11c

    Begin block 0x121
    prev=[0x116], succ=[0x3cde]
    =================================
    0x121: v121(0x3cde) = CONST 
    0x124: JUMP v121(0x3cde)

    Begin block 0x3cde
    prev=[0x121], succ=[]
    =================================
    0x3cdf: v3cdf(0x0) = CONST 
    0x3ce2: REVERT v3cdf(0x0), v3cdf(0x0)

    Begin block 0x46d3
    prev=[0x116], succ=[]
    =================================
    0x46d4: v46d4(0xa41) = CONST 
    0x46d5: CALLPRIVATE v46d4(0xa41)

    Begin block 0x46ca
    prev=[0xf4], succ=[]
    =================================
    0x46cb: v46cb(0x9d1) = CONST 
    0x46cc: CALLPRIVATE v46cb(0x9d1)

    Begin block 0xb9
    prev=[0xad], succ=[0x46d6, 0xc4]
    =================================
    0xba: vba(0xa22cb465) = CONST 
    0xbf: vbf = EQ vba(0xa22cb465), v1f
    0x465e: v465e(0x46d6) = CONST 
    0x465f: JUMPI v465e(0x46d6), vbf

    Begin block 0x46d6
    prev=[0xb9], succ=[]
    =================================
    0x46d7: v46d7(0xa6d) = CONST 
    0x46d8: CALLPRIVATE v46d7(0xa6d)

    Begin block 0xc4
    prev=[0xb9], succ=[0x46d9, 0xcf]
    =================================
    0xc5: vc5(0xa36dc62c) = CONST 
    0xca: vca = EQ vc5(0xa36dc62c), v1f
    0x4660: v4660(0x46d9) = CONST 
    0x4661: JUMPI v4660(0x46d9), vca

    Begin block 0x46d9
    prev=[0xc4], succ=[]
    =================================
    0x46da: v46da(0xa9b) = CONST 
    0x46db: CALLPRIVATE v46da(0xa9b)

    Begin block 0xcf
    prev=[0xc4], succ=[0x46dc, 0xda]
    =================================
    0xd0: vd0(0xa4a87571) = CONST 
    0xd5: vd5 = EQ vd0(0xa4a87571), v1f
    0x4662: v4662(0x46dc) = CONST 
    0x4663: JUMPI v4662(0x46dc), vd5

    Begin block 0x46dc
    prev=[0xcf], succ=[]
    =================================
    0x46dd: v46dd(0xb75) = CONST 
    0x46de: CALLPRIVATE v46dd(0xb75)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x46df]
    =================================
    0xdb: vdb(0xaa271e1a) = CONST 
    0xe0: ve0 = EQ vdb(0xaa271e1a), v1f
    0x4664: v4664(0x46df) = CONST 
    0x4665: JUMPI v4664(0x46df), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0xf0, 0x46e2]
    =================================
    0xe6: ve6(0xaa936a0d) = CONST 
    0xeb: veb = EQ ve6(0xaa936a0d), v1f
    0x4666: v4666(0x46e2) = CONST 
    0x4667: JUMPI v4666(0x46e2), veb

    Begin block 0xf0
    prev=[0xe5], succ=[0x3cba]
    =================================
    0xf0: vf0(0x3cba) = CONST 
    0xf3: JUMP vf0(0x3cba)

    Begin block 0x3cba
    prev=[0xf0], succ=[]
    =================================
    0x3cbb: v3cbb(0x0) = CONST 
    0x3cbe: REVERT v3cbb(0x0), v3cbb(0x0)

    Begin block 0x46e2
    prev=[0xe5], succ=[]
    =================================
    0x46e3: v46e3(0xbf0) = CONST 
    0x46e4: CALLPRIVATE v46e3(0xbf0)

    Begin block 0x46df
    prev=[0xda], succ=[]
    =================================
    0x46e0: v46e0(0xbca) = CONST 
    0x46e1: CALLPRIVATE v46e0(0xbca)

    Begin block 0x36
    prev=[0x2b], succ=[0x7c, 0x41]
    =================================
    0x37: v37(0xc46d0771) = CONST 
    0x3c: v3c = GT v37(0xc46d0771), v1f
    0x3d: v3d(0x7c) = CONST 
    0x40: JUMPI v3d(0x7c), v3c

    Begin block 0x7c
    prev=[0x36], succ=[0x46e5, 0x88]
    =================================
    0x7e: v7e(0xac8a584a) = CONST 
    0x83: v83 = EQ v7e(0xac8a584a), v1f
    0x4656: v4656(0x46e5) = CONST 
    0x4657: JUMPI v4656(0x46e5), v83

    Begin block 0x46e5
    prev=[0x7c], succ=[]
    =================================
    0x46e6: v46e6(0xc16) = CONST 
    0x46e7: CALLPRIVATE v46e6(0xc16)

    Begin block 0x88
    prev=[0x7c], succ=[0x46e8, 0x93]
    =================================
    0x89: v89(0xb2dc5dc3) = CONST 
    0x8e: v8e = EQ v89(0xb2dc5dc3), v1f
    0x4658: v4658(0x46e8) = CONST 
    0x4659: JUMPI v4658(0x46e8), v8e

    Begin block 0x46e8
    prev=[0x88], succ=[]
    =================================
    0x46e9: v46e9(0xc3c) = CONST 
    0x46ea: CALLPRIVATE v46e9(0xc3c)

    Begin block 0x93
    prev=[0x88], succ=[0x46eb, 0x9e]
    =================================
    0x94: v94(0xb738592d) = CONST 
    0x99: v99 = EQ v94(0xb738592d), v1f
    0x465a: v465a(0x46eb) = CONST 
    0x465b: JUMPI v465a(0x46eb), v99

    Begin block 0x46eb
    prev=[0x93], succ=[]
    =================================
    0x46ec: v46ec(0xcba) = CONST 
    0x46ed: CALLPRIVATE v46ec(0xcba)

    Begin block 0x9e
    prev=[0x93], succ=[0xa9, 0x46ee]
    =================================
    0x9f: v9f(0xb774b2b1) = CONST 
    0xa4: va4 = EQ v9f(0xb774b2b1), v1f
    0x465c: v465c(0x46ee) = CONST 
    0x465d: JUMPI v465c(0x46ee), va4

    Begin block 0xa9
    prev=[0x9e], succ=[0x3c96]
    =================================
    0xa9: va9(0x3c96) = CONST 
    0xac: JUMP va9(0x3c96)

    Begin block 0x3c96
    prev=[0xa9], succ=[]
    =================================
    0x3c97: v3c97(0x0) = CONST 
    0x3c9a: REVERT v3c97(0x0), v3c97(0x0)

    Begin block 0x46ee
    prev=[0x9e], succ=[]
    =================================
    0x46ef: v46ef(0xcc2) = CONST 
    0x46f0: CALLPRIVATE v46ef(0xcc2)

    Begin block 0x41
    prev=[0x36], succ=[0x46f1, 0x4c]
    =================================
    0x42: v42(0xc46d0771) = CONST 
    0x47: v47 = EQ v42(0xc46d0771), v1f
    0x464c: v464c(0x46f1) = CONST 
    0x464d: JUMPI v464c(0x46f1), v47

    Begin block 0x46f1
    prev=[0x41], succ=[]
    =================================
    0x46f2: v46f2(0xd12) = CONST 
    0x46f3: CALLPRIVATE v46f2(0xd12)

    Begin block 0x4c
    prev=[0x41], succ=[0x46f4, 0x57]
    =================================
    0x4d: v4d(0xc5b8f772) = CONST 
    0x52: v52 = EQ v4d(0xc5b8f772), v1f
    0x464e: v464e(0x46f4) = CONST 
    0x464f: JUMPI v464e(0x46f4), v52

    Begin block 0x46f4
    prev=[0x4c], succ=[]
    =================================
    0x46f5: v46f5(0xd3e) = CONST 
    0x46f6: CALLPRIVATE v46f5(0xd3e)

    Begin block 0x57
    prev=[0x4c], succ=[0x62, 0x46f7]
    =================================
    0x58: v58(0xe985e9c5) = CONST 
    0x5d: v5d = EQ v58(0xe985e9c5), v1f
    0x4650: v4650(0x46f7) = CONST 
    0x4651: JUMPI v4650(0x46f7), v5d

    Begin block 0x62
    prev=[0x57], succ=[0x46fa, 0x6d]
    =================================
    0x63: v63(0xf242432a) = CONST 
    0x68: v68 = EQ v63(0xf242432a), v1f
    0x4652: v4652(0x46fa) = CONST 
    0x4653: JUMPI v4652(0x46fa), v68

    Begin block 0x46fa
    prev=[0x62], succ=[]
    =================================
    0x46fb: v46fb(0xd98) = CONST 
    0x46fc: CALLPRIVATE v46fb(0xd98)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x46fd]
    =================================
    0x6e: v6e(0xf2ebbc3d) = CONST 
    0x73: v73 = EQ v6e(0xf2ebbc3d), v1f
    0x4654: v4654(0x46fd) = CONST 
    0x4655: JUMPI v4654(0x46fd), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x3c72]
    =================================
    0x78: v78(0x3c72) = CONST 
    0x7b: JUMP v78(0x3c72)

    Begin block 0x3c72
    prev=[0x78], succ=[]
    =================================
    0x3c73: v3c73(0x0) = CONST 
    0x3c76: REVERT v3c73(0x0), v3c73(0x0)

    Begin block 0x46fd
    prev=[0x6d], succ=[]
    =================================
    0x46fe: v46fe(0xe61) = CONST 
    0x46ff: CALLPRIVATE v46fe(0xe61)

    Begin block 0x46f7
    prev=[0x57], succ=[]
    =================================
    0x46f8: v46f8(0xd6a) = CONST 
    0x46f9: CALLPRIVATE v46f8(0xd6a)

    Begin block 0x4700
    prev=[0x10], succ=[]
    =================================
    0x4701: v4701(0x3c4e) = CONST 
    0x4702: CALLPRIVATE v4701(0x3c4e)

}

function 0x1857(0x1857arg0x0) private {
    Begin block 0x1857
    prev=[], succ=[0x431a, 0x189a]
    =================================
    0x1858: v1858(0x2) = CONST 
    0x185b: v185b = SLOAD v1858(0x2)
    0x185c: v185c(0x40) = CONST 
    0x185f: v185f = MLOAD v185c(0x40)
    0x1860: v1860(0x20) = CONST 
    0x1862: v1862(0x1f) = CONST 
    0x1864: v1864(0x0) = CONST 
    0x1866: v1866(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1864(0x0)
    0x1867: v1867(0x100) = CONST 
    0x186a: v186a(0x1) = CONST 
    0x186d: v186d = AND v185b, v186a(0x1)
    0x186e: v186e = ISZERO v186d
    0x186f: v186f = MUL v186e, v1867(0x100)
    0x1870: v1870 = ADD v186f, v1866(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1873: v1873 = AND v185b, v1870
    0x1876: v1876 = DIV v1873, v1858(0x2)
    0x1879: v1879 = ADD v1876, v1862(0x1f)
    0x187c: v187c = DIV v1879, v1860(0x20)
    0x187e: v187e = MUL v1860(0x20), v187c
    0x1880: v1880 = ADD v185f, v187e
    0x1882: v1882 = ADD v1860(0x20), v1880
    0x1885: MSTORE v185c(0x40), v1882
    0x1888: MSTORE v185f, v1876
    0x1889: v1889(0x60) = CONST 
    0x1891: v1891 = ADD v185f, v1860(0x20)
    0x1895: v1895 = ISZERO v1876
    0x1896: v1896(0x431a) = CONST 
    0x1899: JUMPI v1896(0x431a), v1895

    Begin block 0x431a
    prev=[0x1857], succ=[]
    =================================
    0x4323: RETURNPRIVATE v1857arg0, v185f

    Begin block 0x189a
    prev=[0x1857], succ=[0x18a2, 0x18b5]
    =================================
    0x189b: v189b(0x1f) = CONST 
    0x189d: v189d = LT v189b(0x1f), v1876
    0x189e: v189e(0x18b5) = CONST 
    0x18a1: JUMPI v189e(0x18b5), v189d

    Begin block 0x18a2
    prev=[0x189a], succ=[0x4343]
    =================================
    0x18a2: v18a2(0x100) = CONST 
    0x18a7: v18a7 = SLOAD v1858(0x2)
    0x18a8: v18a8 = DIV v18a7, v18a2(0x100)
    0x18a9: v18a9 = MUL v18a8, v18a2(0x100)
    0x18ab: MSTORE v1891, v18a9
    0x18ad: v18ad(0x20) = CONST 
    0x18af: v18af = ADD v18ad(0x20), v1891
    0x18b1: v18b1(0x4343) = CONST 
    0x18b4: JUMP v18b1(0x4343)

    Begin block 0x4343
    prev=[0x18a2], succ=[]
    =================================
    0x434c: RETURNPRIVATE v1857arg0, v185f

    Begin block 0x18b5
    prev=[0x189a], succ=[0x18c3]
    =================================
    0x18b7: v18b7 = ADD v1891, v1876
    0x18ba: v18ba(0x0) = CONST 
    0x18bc: MSTORE v18ba(0x0), v1858(0x2)
    0x18bd: v18bd(0x20) = CONST 
    0x18bf: v18bf(0x0) = CONST 
    0x18c1: v18c1 = SHA3 v18bf(0x0), v18bd(0x20)

    Begin block 0x18c3
    prev=[0x18b5, 0x18c3], succ=[0x18c3, 0x18d7]
    =================================
    0x18c3_0x0: v18c3_0 = PHI v1891, v18cf
    0x18c3_0x1: v18c3_1 = PHI v18c1, v18cb
    0x18c5: v18c5 = SLOAD v18c3_1
    0x18c7: MSTORE v18c3_0, v18c5
    0x18c9: v18c9(0x1) = CONST 
    0x18cb: v18cb = ADD v18c9(0x1), v18c3_1
    0x18cd: v18cd(0x20) = CONST 
    0x18cf: v18cf = ADD v18cd(0x20), v18c3_0
    0x18d2: v18d2 = GT v18b7, v18cf
    0x18d3: v18d3(0x18c3) = CONST 
    0x18d6: JUMPI v18d3(0x18c3), v18d2

    Begin block 0x18d7
    prev=[0x18c3], succ=[0x18e0]
    =================================
    0x18d9: v18d9 = SUB v18cf, v18b7
    0x18da: v18da(0x1f) = CONST 
    0x18dc: v18dc = AND v18da(0x1f), v18d9
    0x18de: v18de = ADD v18b7, v18dc

    Begin block 0x18e0
    prev=[0x18d7], succ=[]
    =================================
    0x18e9: RETURNPRIVATE v1857arg0, v185f

}

function balanceOf(address,uint256)() public {
    Begin block 0x220
    prev=[], succ=[0x232, 0x236]
    =================================
    0x221: v221(0x3d6e) = CONST 
    0x224: v224(0x4) = CONST 
    0x227: v227 = CALLDATASIZE 
    0x228: v228 = SUB v227, v224(0x4)
    0x229: v229(0x40) = CONST 
    0x22c: v22c = LT v228, v229(0x40)
    0x22d: v22d = ISZERO v22c
    0x22e: v22e(0x236) = CONST 
    0x231: JUMPI v22e(0x236), v22d

    Begin block 0x232
    prev=[0x220], succ=[]
    =================================
    0x232: v232(0x0) = CONST 
    0x235: REVERT v232(0x0), v232(0x0)

    Begin block 0x236
    prev=[0x220], succ=[0xe690x220]
    =================================
    0x238: v238(0x1) = CONST 
    0x23a: v23a(0x1) = CONST 
    0x23c: v23c(0xa0) = CONST 
    0x23e: v23e(0x10000000000000000000000000000000000000000) = SHL v23c(0xa0), v23a(0x1)
    0x23f: v23f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23e(0x10000000000000000000000000000000000000000), v238(0x1)
    0x241: v241 = CALLDATALOAD v224(0x4)
    0x242: v242 = AND v241, v23f(0xffffffffffffffffffffffffffffffffffffffff)
    0x244: v244(0x20) = CONST 
    0x246: v246(0x24) = ADD v244(0x20), v224(0x4)
    0x247: v247 = CALLDATALOAD v246(0x24)
    0x248: v248(0xe69) = CONST 
    0x24b: JUMP v248(0xe69)

    Begin block 0xe690x220
    prev=[0x236], succ=[0xe750x220]
    =================================
    0xe6a0x220: v220e6a(0x0) = CONST 
    0xe6c0x220: v220e6c(0xe75) = CONST 
    0xe710x220: v220e71(0x2497) = CONST 
    0xe740x220: v220e74_0 = CALLPRIVATE v220e71(0x2497), v247, v242, v220e6c(0xe75)

    Begin block 0xe750x220
    prev=[0xe690x220], succ=[0xe7b0x220, 0xe820x220]
    =================================
    0xe760x220: v220e76 = ISZERO v220e74_0
    0xe770x220: v220e77(0xe82) = CONST 
    0xe7a0x220: JUMPI v220e77(0xe82), v220e76

    Begin block 0xe7b0x220
    prev=[0xe750x220], succ=[0x421b0x220]
    =================================
    0xe7c0x220: v220e7c(0x1) = CONST 
    0xe7e0x220: v220e7e(0x421b) = CONST 
    0xe810x220: JUMP v220e7e(0x421b)

    Begin block 0x421b0x220
    prev=[0xe7b0x220], succ=[0x3d6e]
    =================================
    0x42200x220: JUMP v221(0x3d6e)

    Begin block 0x3d6e
    prev=[0xe860x220, 0x421b0x220], succ=[]
    =================================
    0x3d6e_0x0: v3d6e_0 = PHI v220e84(0x0), v220e7c(0x1)
    0x3d6f: v3d6f(0x40) = CONST 
    0x3d72: v3d72 = MLOAD v3d6f(0x40)
    0x3d75: MSTORE v3d72, v3d6e_0
    0x3d76: v3d76 = MLOAD v3d6f(0x40)
    0x3d7a: v3d7a(0x0) = SUB v3d72, v3d76
    0x3d7b: v3d7b(0x20) = CONST 
    0x3d7d: v3d7d(0x20) = ADD v3d7b(0x20), v3d7a(0x0)
    0x3d7f: RETURN v3d76, v3d7d(0x20)

    Begin block 0xe820x220
    prev=[0xe750x220], succ=[0xe860x220]
    =================================
    0xe840x220: v220e84(0x0) = CONST 

    Begin block 0xe860x220
    prev=[0xe820x220], succ=[0x3d6e]
    =================================
    0xe8b0x220: JUMP v221(0x3d6e)

}

function 0x2497(0x2497arg0x0, 0x2497arg0x1, 0x2497arg0x2) private {
    Begin block 0x2497
    prev=[], succ=[0x24af0x2497, 0x24a80x2497]
    =================================
    0x2498: v2498(0x0) = CONST 
    0x249a: v249a(0x1) = CONST 
    0x249c: v249c(0x1) = CONST 
    0x249e: v249e(0xa0) = CONST 
    0x24a0: v24a0(0x10000000000000000000000000000000000000000) = SHL v249e(0xa0), v249c(0x1)
    0x24a1: v24a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24a0(0x10000000000000000000000000000000000000000), v249a(0x1)
    0x24a3: v24a3 = AND v2497arg1, v24a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x24a4: v24a4(0x24af) = CONST 
    0x24a7: JUMPI v24a4(0x24af), v24a3

    Begin block 0x24af0x2497
    prev=[0x2497], succ=[0x43ff0x2497]
    =================================
    0x24b10x2497: v249724b1(0x0) = CONST 
    0x24b50x2497: MSTORE v249724b1(0x0), v2497arg0
    0x24b60x2497: v249724b6(0x8) = CONST 
    0x24b80x2497: v249724b8(0x20) = CONST 
    0x24ba0x2497: MSTORE v249724b8(0x20), v249724b6(0x8)
    0x24bb0x2497: v249724bb(0x40) = CONST 
    0x24be0x2497: v249724be = SHA3 v249724b1(0x0), v249724bb(0x40)
    0x24bf0x2497: v249724bf = SLOAD v249724be
    0x24c00x2497: v249724c0(0x1) = CONST 
    0x24c20x2497: v249724c2(0x1) = CONST 
    0x24c40x2497: v249724c4(0xa0) = CONST 
    0x24c60x2497: v249724c6(0x10000000000000000000000000000000000000000) = SHL v249724c4(0xa0), v249724c2(0x1)
    0x24c70x2497: v249724c7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v249724c6(0x10000000000000000000000000000000000000000), v249724c0(0x1)
    0x24ca0x2497: v249724ca = AND v249724c7(0xffffffffffffffffffffffffffffffffffffffff), v2497arg1
    0x24cc0x2497: v249724cc = AND v249724bf, v249724c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x24cd0x2497: v249724cd = EQ v249724cc, v249724ca
    0x24ce0x2497: v249724ce(0x43ff) = CONST 
    0x24d10x2497: JUMP v249724ce(0x43ff)

    Begin block 0x43ff0x2497
    prev=[0x24af0x2497], succ=[]
    =================================
    0x44040x2497: RETURNPRIVATE v2497arg2, v249724cd

    Begin block 0x24a80x2497
    prev=[0x2497], succ=[0x43da0x2497]
    =================================
    0x24a90x2497: v249724a9(0x0) = CONST 
    0x24ab0x2497: v249724ab(0x43da) = CONST 
    0x24ae0x2497: JUMP v249724ab(0x43da)

    Begin block 0x43da0x2497
    prev=[0x24a80x2497], succ=[]
    =================================
    0x43df0x2497: RETURNPRIVATE v2497arg2, v249724a9(0x0)

}

function supportsInterface(bytes4)() public {
    Begin block 0x25e
    prev=[], succ=[0x270, 0x274]
    =================================
    0x25f: v25f(0x3d9f) = CONST 
    0x262: v262(0x4) = CONST 
    0x265: v265 = CALLDATASIZE 
    0x266: v266 = SUB v265, v262(0x4)
    0x267: v267(0x20) = CONST 
    0x26a: v26a = LT v266, v267(0x20)
    0x26b: v26b = ISZERO v26a
    0x26c: v26c(0x274) = CONST 
    0x26f: JUMPI v26c(0x274), v26b

    Begin block 0x270
    prev=[0x25e], succ=[]
    =================================
    0x270: v270(0x0) = CONST 
    0x273: REVERT v270(0x0), v270(0x0)

    Begin block 0x274
    prev=[0x25e], succ=[0xe8c]
    =================================
    0x276: v276 = CALLDATALOAD v262(0x4)
    0x277: v277(0x1) = CONST 
    0x279: v279(0x1) = CONST 
    0x27b: v27b(0xe0) = CONST 
    0x27d: v27d(0x100000000000000000000000000000000000000000000000000000000) = SHL v27b(0xe0), v279(0x1)
    0x27e: v27e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v27d(0x100000000000000000000000000000000000000000000000000000000), v277(0x1)
    0x27f: v27f(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v27e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x280: v280 = AND v27f(0xffffffff00000000000000000000000000000000000000000000000000000000), v276
    0x281: v281(0xe8c) = CONST 
    0x284: JUMP v281(0xe8c)

    Begin block 0xe8c
    prev=[0x274], succ=[0xeaa]
    =================================
    0xe8d: ve8d(0x1) = CONST 
    0xe8f: ve8f(0x1) = CONST 
    0xe91: ve91(0xe0) = CONST 
    0xe93: ve93(0x100000000000000000000000000000000000000000000000000000000) = SHL ve91(0xe0), ve8f(0x1)
    0xe94: ve94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB ve93(0x100000000000000000000000000000000000000000000000000000000), ve8d(0x1)
    0xe95: ve95(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT ve94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xe97: ve97 = AND v280, ve95(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0xe98: ve98(0x0) = CONST 
    0xe9c: MSTORE ve98(0x0), ve97
    0xe9d: ve9d(0x20) = CONST 
    0xea1: MSTORE ve9d(0x20), ve98(0x0)
    0xea2: vea2(0x40) = CONST 
    0xea5: vea5 = SHA3 ve98(0x0), vea2(0x40)
    0xea6: vea6 = SLOAD vea5
    0xea7: vea7(0xff) = CONST 
    0xea9: vea9 = AND vea7(0xff), vea6

    Begin block 0xeaa
    prev=[0xe8c], succ=[0x3d9f]
    =================================
    0xeae: JUMP v25f(0x3d9f)

    Begin block 0x3d9f
    prev=[0xeaa], succ=[]
    =================================
    0x3da0: v3da0(0x40) = CONST 
    0x3da3: v3da3 = MLOAD v3da0(0x40)
    0x3da5: v3da5 = ISZERO vea9
    0x3da6: v3da6 = ISZERO v3da5
    0x3da8: MSTORE v3da3, v3da6
    0x3da9: v3da9 = MLOAD v3da0(0x40)
    0x3dad: v3dad(0x0) = SUB v3da3, v3da9
    0x3dae: v3dae(0x20) = CONST 
    0x3db0: v3db0(0x20) = ADD v3dae(0x20), v3dad(0x0)
    0x3db2: RETURN v3da9, v3db0(0x20)

}

function 0x26ae(0x26aearg0x0, 0x26aearg0x1) private {
    Begin block 0x26ae
    prev=[], succ=[0x26d3, 0x26b6]
    =================================
    0x26af: v26af(0x60) = CONST 
    0x26b2: v26b2(0x26d3) = CONST 
    0x26b5: JUMPI v26b2(0x26d3), v26aearg0

    Begin block 0x26d3
    prev=[0x26ae], succ=[0x26d7]
    =================================
    0x26d5: v26d5(0x0) = CONST 

    Begin block 0x26d7
    prev=[0x26de, 0x26d3], succ=[0x26de, 0x26eb]
    =================================
    0x26d7_0x1: v26d7_1 = PHI v26e4, v26aearg0
    0x26d9: v26d9 = ISZERO v26d7_1
    0x26da: v26da(0x26eb) = CONST 
    0x26dd: JUMPI v26da(0x26eb), v26d9

    Begin block 0x26de
    prev=[0x26d7], succ=[0x26d7]
    =================================
    0x26de: v26de(0x1) = CONST 
    0x26de_0x0: v26de_0 = PHI v26d5(0x0), v26e0
    0x26de_0x1: v26de_1 = PHI v26e4, v26aearg0
    0x26e0: v26e0 = ADD v26de(0x1), v26de_0
    0x26e1: v26e1(0xa) = CONST 
    0x26e4: v26e4 = DIV v26de_1, v26e1(0xa)
    0x26e7: v26e7(0x26d7) = CONST 
    0x26ea: JUMP v26e7(0x26d7)

    Begin block 0x26eb
    prev=[0x26d7], succ=[0x2700, 0x2704]
    =================================
    0x26eb_0x0: v26eb_0 = PHI v26d5(0x0), v26e0
    0x26ec: v26ec(0x0) = CONST 
    0x26ef: v26ef(0xffffffffffffffff) = CONST 
    0x26f9: v26f9 = GT v26eb_0, v26ef(0xffffffffffffffff)
    0x26fb: v26fb = ISZERO v26f9
    0x26fc: v26fc(0x2704) = CONST 
    0x26ff: JUMPI v26fc(0x2704), v26fb

    Begin block 0x2700
    prev=[0x26eb], succ=[]
    =================================
    0x2700: v2700(0x0) = CONST 
    0x2703: REVERT v2700(0x0), v2700(0x0)

    Begin block 0x2704
    prev=[0x26eb], succ=[0x2723, 0x272f]
    =================================
    0x2704_0x1: v2704_1 = PHI v26d5(0x0), v26e0
    0x2706: v2706(0x40) = CONST 
    0x2708: v2708 = MLOAD v2706(0x40)
    0x270c: MSTORE v2708, v2704_1
    0x270e: v270e(0x1f) = CONST 
    0x2710: v2710 = ADD v270e(0x1f), v2704_1
    0x2711: v2711(0x1f) = CONST 
    0x2713: v2713(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2711(0x1f)
    0x2714: v2714 = AND v2713(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v2710
    0x2715: v2715(0x20) = CONST 
    0x2717: v2717 = ADD v2715(0x20), v2714
    0x2719: v2719 = ADD v2708, v2717
    0x271a: v271a(0x40) = CONST 
    0x271c: MSTORE v271a(0x40), v2719
    0x271e: v271e = ISZERO v2704_1
    0x271f: v271f(0x272f) = CONST 
    0x2722: JUMPI v271f(0x272f), v271e

    Begin block 0x2723
    prev=[0x2704], succ=[0x272f]
    =================================
    0x2723: v2723(0x20) = CONST 
    0x2723_0x0: v2723_0 = PHI v26d5(0x0), v26e0
    0x2726: v2726 = ADD v2708, v2723(0x20)
    0x2729: v2729 = CALLDATASIZE 
    0x272b: CALLDATACOPY v2726, v2729, v2723_0
    0x272c: v272c = ADD v2723_0, v2726

    Begin block 0x272f
    prev=[0x2723, 0x2704], succ=[0x2734]
    =================================

    Begin block 0x2734
    prev=[0x272f, 0x2763], succ=[0x273b, 0x2787]
    =================================
    0x2734_0x5: v2734_5 = PHI v277e, v26aearg0
    0x2736: v2736 = ISZERO v2734_5
    0x2737: v2737(0x2787) = CONST 
    0x273a: JUMPI v2737(0x2787), v2736

    Begin block 0x273b
    prev=[0x2734], succ=[0x2762, 0x2763]
    =================================
    0x273b: v273b(0x0) = CONST 
    0x273b_0x0: v273b_0 = PHI v26d5(0x0), v26e0, v273e
    0x273b_0x5: v273b_5 = PHI v277e, v26aearg0
    0x273d: v273d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v273b(0x0)
    0x273e: v273e = ADD v273d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v273b_0
    0x273f: v273f(0x0) = CONST 
    0x2741: v2741(0xa) = CONST 
    0x2744: v2744 = DIV v273b_5, v2741(0xa)
    0x2745: v2745(0xa) = CONST 
    0x2747: v2747 = MUL v2745(0xa), v2744
    0x2749: v2749 = SUB v273b_5, v2747
    0x274a: v274a(0x30) = CONST 
    0x274c: v274c = ADD v274a(0x30), v2749
    0x274f: v274f(0x0) = CONST 
    0x2752: v2752(0xf8) = CONST 
    0x2754: v2754 = SHL v2752(0xf8), v274c
    0x275b: v275b = MLOAD v2708
    0x275d: v275d = LT v273e, v275b
    0x275e: v275e(0x2763) = CONST 
    0x2761: JUMPI v275e(0x2763), v275d

    Begin block 0x2762
    prev=[0x273b], succ=[]
    =================================
    0x2762: THROW 

    Begin block 0x2763
    prev=[0x273b], succ=[0x2734]
    =================================
    0x2763_0xa: v2763_a = PHI v277e, v26aearg0
    0x2764: v2764(0x20) = CONST 
    0x2766: v2766 = ADD v2764(0x20), v273e
    0x2767: v2767 = ADD v2766, v2708
    0x2769: v2769(0x1) = CONST 
    0x276b: v276b(0x1) = CONST 
    0x276d: v276d(0xf8) = CONST 
    0x276f: v276f(0x100000000000000000000000000000000000000000000000000000000000000) = SHL v276d(0xf8), v276b(0x1)
    0x2770: v2770(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v276f(0x100000000000000000000000000000000000000000000000000000000000000), v2769(0x1)
    0x2771: v2771(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v2770(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2772: v2772 = AND v2771(0xff00000000000000000000000000000000000000000000000000000000000000), v2754
    0x2775: v2775(0x0) = CONST 
    0x2777: v2777 = BYTE v2775(0x0), v2772
    0x2779: MSTORE8 v2767, v2777
    0x277b: v277b(0xa) = CONST 
    0x277e: v277e = DIV v2763_a, v277b(0xa)
    0x2783: v2783(0x2734) = CONST 
    0x2786: JUMP v2783(0x2734)

    Begin block 0x2787
    prev=[0x2734], succ=[]
    =================================
    0x278f: RETURNPRIVATE v26aearg1, v2708

    Begin block 0x26b6
    prev=[0x26ae], succ=[0x444a]
    =================================
    0x26b7: v26b7(0x40) = CONST 
    0x26ba: v26ba = MLOAD v26b7(0x40)
    0x26bd: v26bd = ADD v26b7(0x40), v26ba
    0x26c0: MSTORE v26b7(0x40), v26bd
    0x26c1: v26c1(0x1) = CONST 
    0x26c4: MSTORE v26ba, v26c1(0x1)
    0x26c5: v26c5(0x3) = CONST 
    0x26c7: v26c7(0xfc) = CONST 
    0x26c9: v26c9(0x3000000000000000000000000000000000000000000000000000000000000000) = SHL v26c7(0xfc), v26c5(0x3)
    0x26ca: v26ca(0x20) = CONST 
    0x26cd: v26cd = ADD v26ba, v26ca(0x20)
    0x26ce: MSTORE v26cd, v26c9(0x3000000000000000000000000000000000000000000000000000000000000000)
    0x26cf: v26cf(0x444a) = CONST 
    0x26d2: JUMP v26cf(0x444a)

    Begin block 0x444a
    prev=[0x26b6], succ=[]
    =================================
    0x444e: RETURNPRIVATE v26aearg1, v26ba

}

function 0x27fd(0x27fdarg0x0, 0x27fdarg0x1, 0x27fdarg0x2, 0x27fdarg0x3, 0x27fdarg0x4, 0x27fdarg0x5, 0x27fdarg0x6) private {
    Begin block 0x27fd
    prev=[], succ=[0x3684B0x27fd]
    =================================
    0x27fe: v27fe(0x280f) = CONST 
    0x2802: v2802(0x1) = CONST 
    0x2804: v2804(0x1) = CONST 
    0x2806: v2806(0xa0) = CONST 
    0x2808: v2808(0x10000000000000000000000000000000000000000) = SHL v2806(0xa0), v2804(0x1)
    0x2809: v2809(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2808(0x10000000000000000000000000000000000000000), v2802(0x1)
    0x280a: v280a = AND v2809(0xffffffffffffffffffffffffffffffffffffffff), v27fdarg3
    0x280b: v280b(0x3684) = CONST 
    0x280e: JUMP v280b(0x3684)

    Begin block 0x3684B0x27fd
    prev=[0x27fd], succ=[0x280f]
    =================================
    0x3685S0x27fd: v3685V27fd = EXTCODESIZE v280a
    0x3686S0x27fd: v3686V27fd = ISZERO v3685V27fd
    0x3687S0x27fd: v3687V27fd = ISZERO v3686V27fd
    0x3689S0x27fd: JUMP v27fe(0x280f)

    Begin block 0x280f
    prev=[0x3684B0x27fd], succ=[0x446e, 0x2815]
    =================================
    0x2810: v2810 = ISZERO v3687V27fd
    0x2811: v2811(0x446e) = CONST 
    0x2814: JUMPI v2811(0x446e), v2810

    Begin block 0x446e
    prev=[0x280f], succ=[]
    =================================
    0x4475: RETURNPRIVATE v27fdarg6

    Begin block 0x2815
    prev=[0x280f], succ=[0x2885]
    =================================
    0x2816: v2816(0x1) = CONST 
    0x2818: v2818(0x1) = CONST 
    0x281a: v281a(0xa0) = CONST 
    0x281c: v281c(0x10000000000000000000000000000000000000000) = SHL v281a(0xa0), v2818(0x1)
    0x281d: v281d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v281c(0x10000000000000000000000000000000000000000), v2816(0x1)
    0x281e: v281e = AND v281d(0xffffffffffffffffffffffffffffffffffffffff), v27fdarg3
    0x281f: v281f(0xbc197c81) = CONST 
    0x2829: v2829(0x40) = CONST 
    0x282b: v282b = MLOAD v2829(0x40)
    0x282d: v282d(0xffffffff) = CONST 
    0x2832: v2832(0xbc197c81) = AND v282d(0xffffffff), v281f(0xbc197c81)
    0x2833: v2833(0xe0) = CONST 
    0x2835: v2835(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v2833(0xe0), v2832(0xbc197c81)
    0x2837: MSTORE v282b, v2835(0xbc197c8100000000000000000000000000000000000000000000000000000000)
    0x2838: v2838(0x4) = CONST 
    0x283a: v283a = ADD v2838(0x4), v282b
    0x283d: v283d(0x1) = CONST 
    0x283f: v283f(0x1) = CONST 
    0x2841: v2841(0xa0) = CONST 
    0x2843: v2843(0x10000000000000000000000000000000000000000) = SHL v2841(0xa0), v283f(0x1)
    0x2844: v2844(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2843(0x10000000000000000000000000000000000000000), v283d(0x1)
    0x2845: v2845 = AND v2844(0xffffffffffffffffffffffffffffffffffffffff), v27fdarg5
    0x2847: MSTORE v283a, v2845
    0x2848: v2848(0x20) = CONST 
    0x284a: v284a = ADD v2848(0x20), v283a
    0x284c: v284c(0x1) = CONST 
    0x284e: v284e(0x1) = CONST 
    0x2850: v2850(0xa0) = CONST 
    0x2852: v2852(0x10000000000000000000000000000000000000000) = SHL v2850(0xa0), v284e(0x1)
    0x2853: v2853(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2852(0x10000000000000000000000000000000000000000), v284c(0x1)
    0x2854: v2854 = AND v2853(0xffffffffffffffffffffffffffffffffffffffff), v27fdarg4
    0x2856: MSTORE v284a, v2854
    0x2857: v2857(0x20) = CONST 
    0x2859: v2859 = ADD v2857(0x20), v284a
    0x285b: v285b(0x20) = CONST 
    0x285d: v285d = ADD v285b(0x20), v2859
    0x285f: v285f(0x20) = CONST 
    0x2861: v2861 = ADD v285f(0x20), v285d
    0x2863: v2863(0x20) = CONST 
    0x2865: v2865 = ADD v2863(0x20), v2861
    0x2868: v2868(0xa0) = SUB v2865, v283a
    0x286a: MSTORE v2859, v2868(0xa0)
    0x286e: v286e = MLOAD v27fdarg2
    0x2870: MSTORE v2865, v286e
    0x2871: v2871(0x20) = CONST 
    0x2873: v2873 = ADD v2871(0x20), v2865
    0x2877: v2877 = MLOAD v27fdarg2
    0x2879: v2879(0x20) = CONST 
    0x287b: v287b = ADD v2879(0x20), v27fdarg2
    0x287d: v287d(0x20) = CONST 
    0x287f: v287f = MUL v287d(0x20), v2877
    0x2883: v2883(0x0) = CONST 

    Begin block 0x2885
    prev=[0x2815, 0x288e], succ=[0x289d, 0x288e]
    =================================
    0x2885_0x0: v2885_0 = PHI v2883(0x0), v2898
    0x2888: v2888 = LT v2885_0, v287f
    0x2889: v2889 = ISZERO v2888
    0x288a: v288a(0x289d) = CONST 
    0x288d: JUMPI v288a(0x289d), v2889

    Begin block 0x289d
    prev=[0x2885], succ=[0x28c4]
    =================================
    0x28a4: v28a4 = ADD v287f, v2873
    0x28a7: v28a7 = SUB v28a4, v283a
    0x28a9: MSTORE v285d, v28a7
    0x28ad: v28ad = MLOAD v27fdarg1
    0x28af: MSTORE v28a4, v28ad
    0x28b0: v28b0(0x20) = CONST 
    0x28b2: v28b2 = ADD v28b0(0x20), v28a4
    0x28b6: v28b6 = MLOAD v27fdarg1
    0x28b8: v28b8(0x20) = CONST 
    0x28ba: v28ba = ADD v28b8(0x20), v27fdarg1
    0x28bc: v28bc(0x20) = CONST 
    0x28be: v28be = MUL v28bc(0x20), v28b6
    0x28c2: v28c2(0x0) = CONST 

    Begin block 0x28c4
    prev=[0x289d, 0x28cd], succ=[0x28dc, 0x28cd]
    =================================
    0x28c4_0x0: v28c4_0 = PHI v28c2(0x0), v28d7
    0x28c7: v28c7 = LT v28c4_0, v28be
    0x28c8: v28c8 = ISZERO v28c7
    0x28c9: v28c9(0x28dc) = CONST 
    0x28cc: JUMPI v28c9(0x28dc), v28c8

    Begin block 0x28dc
    prev=[0x28c4], succ=[0x2900]
    =================================
    0x28e3: v28e3 = ADD v28be, v28b2
    0x28e6: v28e6 = SUB v28e3, v283a
    0x28e8: MSTORE v2861, v28e6
    0x28ec: v28ec = MLOAD v27fdarg0
    0x28ee: MSTORE v28e3, v28ec
    0x28ef: v28ef(0x20) = CONST 
    0x28f1: v28f1 = ADD v28ef(0x20), v28e3
    0x28f5: v28f5 = MLOAD v27fdarg0
    0x28f7: v28f7(0x20) = CONST 
    0x28f9: v28f9 = ADD v28f7(0x20), v27fdarg0
    0x28fe: v28fe(0x0) = CONST 

    Begin block 0x2900
    prev=[0x28dc, 0x2909], succ=[0x2918, 0x2909]
    =================================
    0x2900_0x0: v2900_0 = PHI v28fe(0x0), v2913
    0x2903: v2903 = LT v2900_0, v28f5
    0x2904: v2904 = ISZERO v2903
    0x2905: v2905(0x2918) = CONST 
    0x2908: JUMPI v2905(0x2918), v2904

    Begin block 0x2918
    prev=[0x2900], succ=[0x2945, 0x292c]
    =================================
    0x2921: v2921 = ADD v28f5, v28f1
    0x2923: v2923(0x1f) = CONST 
    0x2925: v2925 = AND v2923(0x1f), v28f5
    0x2927: v2927 = ISZERO v2925
    0x2928: v2928(0x2945) = CONST 
    0x292b: JUMPI v2928(0x2945), v2927

    Begin block 0x2945
    prev=[0x2918, 0x292c], succ=[0x2966, 0x296a]
    =================================
    0x2945_0x1: v2945_1 = PHI v2921, v2942
    0x2951: v2951(0x20) = CONST 
    0x2953: v2953(0x40) = CONST 
    0x2955: v2955 = MLOAD v2953(0x40)
    0x2958: v2958 = SUB v2945_1, v2955
    0x295a: v295a(0x0) = CONST 
    0x295e: v295e = EXTCODESIZE v281e
    0x295f: v295f = ISZERO v295e
    0x2961: v2961 = ISZERO v295f
    0x2962: v2962(0x296a) = CONST 
    0x2965: JUMPI v2962(0x296a), v2961

    Begin block 0x2966
    prev=[0x2945], succ=[]
    =================================
    0x2966: v2966(0x0) = CONST 
    0x2969: REVERT v2966(0x0), v2966(0x0)

    Begin block 0x296a
    prev=[0x2945], succ=[0x298f, 0x2978]
    =================================
    0x296c: v296c = GAS 
    0x296d: v296d = CALL v296c, v281e, v295a(0x0), v2955, v2958, v2955, v2951(0x20)
    0x2973: v2973 = ISZERO v296d
    0x2974: v2974(0x298f) = CONST 
    0x2977: JUMPI v2974(0x298f), v2973

    Begin block 0x298f
    prev=[0x296a, 0x298a], succ=[0x2994, 0x2a62]
    =================================
    0x298f_0x0: v298f_0 = PHI v296d, v298d(0x1)
    0x2990: v2990(0x2a62) = CONST 
    0x2993: JUMPI v2990(0x2a62), v298f_0

    Begin block 0x2994
    prev=[0x298f], succ=[0x299b0x27fd]
    =================================
    0x2994: v2994(0x299b) = CONST 
    0x2997: v2997(0x3969) = CONST 
    0x299a: v299a_0 = CALLPRIVATE v2997(0x3969), v2994(0x299b)

    Begin block 0x299b0x27fd
    prev=[0x2994], succ=[0x29a10x27fd, 0x29a60x27fd]
    =================================
    0x299d0x27fd: v27fd299d(0x29a6) = CONST 
    0x29a00x27fd: JUMPI v27fd299d(0x29a6), v299a_0

    Begin block 0x29a10x27fd
    prev=[0x299b0x27fd], succ=[0x2a2b0x27fd]
    =================================
    0x29a20x27fd: v27fd29a2(0x2a2b) = CONST 
    0x29a50x27fd: JUMP v27fd29a2(0x2a2b)

    Begin block 0x2a2b0x27fd
    prev=[0x29a10x27fd], succ=[]
    =================================
    0x2a2c0x27fd: v27fd2a2c(0x40) = CONST 
    0x2a2e0x27fd: v27fd2a2e = MLOAD v27fd2a2c(0x40)
    0x2a2f0x27fd: v27fd2a2f(0x461bcd) = CONST 
    0x2a330x27fd: v27fd2a33(0xe5) = CONST 
    0x2a350x27fd: v27fd2a35(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v27fd2a33(0xe5), v27fd2a2f(0x461bcd)
    0x2a370x27fd: MSTORE v27fd2a2e, v27fd2a35(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a380x27fd: v27fd2a38(0x4) = CONST 
    0x2a3a0x27fd: v27fd2a3a = ADD v27fd2a38(0x4), v27fd2a2e
    0x2a3d0x27fd: v27fd2a3d(0x20) = CONST 
    0x2a3f0x27fd: v27fd2a3f = ADD v27fd2a3d(0x20), v27fd2a3a
    0x2a420x27fd: v27fd2a42(0x20) = SUB v27fd2a3f, v27fd2a3a
    0x2a440x27fd: MSTORE v27fd2a3a, v27fd2a42(0x20)
    0x2a450x27fd: v27fd2a45(0x2b) = CONST 
    0x2a480x27fd: MSTORE v27fd2a3f, v27fd2a45(0x2b)
    0x2a490x27fd: v27fd2a49(0x20) = CONST 
    0x2a4b0x27fd: v27fd2a4b = ADD v27fd2a49(0x20), v27fd2a3f
    0x2a4d0x27fd: v27fd2a4d(0x3a33) = CONST 
    0x2a500x27fd: v27fd2a50(0x2b) = CONST 
    0x2a530x27fd: CODECOPY v27fd2a4b, v27fd2a4d(0x3a33), v27fd2a50(0x2b)
    0x2a540x27fd: v27fd2a54(0x40) = CONST 
    0x2a560x27fd: v27fd2a56 = ADD v27fd2a54(0x40), v27fd2a4b
    0x2a5a0x27fd: v27fd2a5a(0x40) = CONST 
    0x2a5c0x27fd: v27fd2a5c = MLOAD v27fd2a5a(0x40)
    0x2a5f0x27fd: v27fd2a5f(0x84) = SUB v27fd2a56, v27fd2a5c
    0x2a610x27fd: REVERT v27fd2a5c, v27fd2a5f(0x84)

    Begin block 0x29a60x27fd
    prev=[0x299b0x27fd], succ=[0x29d80x27fd]
    =================================
    0x29a80x27fd: v27fd29a8(0x40) = CONST 
    0x29aa0x27fd: v27fd29aa = MLOAD v27fd29a8(0x40)
    0x29ab0x27fd: v27fd29ab(0x461bcd) = CONST 
    0x29af0x27fd: v27fd29af(0xe5) = CONST 
    0x29b10x27fd: v27fd29b1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v27fd29af(0xe5), v27fd29ab(0x461bcd)
    0x29b30x27fd: MSTORE v27fd29aa, v27fd29b1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29b40x27fd: v27fd29b4(0x4) = CONST 
    0x29b60x27fd: v27fd29b6 = ADD v27fd29b4(0x4), v27fd29aa
    0x29b90x27fd: v27fd29b9(0x20) = CONST 
    0x29bb0x27fd: v27fd29bb = ADD v27fd29b9(0x20), v27fd29b6
    0x29be0x27fd: v27fd29be(0x20) = SUB v27fd29bb, v27fd29b6
    0x29c00x27fd: MSTORE v27fd29b6, v27fd29be(0x20)
    0x29c40x27fd: v27fd29c4 = MLOAD v299a_0
    0x29c60x27fd: MSTORE v27fd29bb, v27fd29c4
    0x29c70x27fd: v27fd29c7(0x20) = CONST 
    0x29c90x27fd: v27fd29c9 = ADD v27fd29c7(0x20), v27fd29bb
    0x29cd0x27fd: v27fd29cd = MLOAD v299a_0
    0x29cf0x27fd: v27fd29cf(0x20) = CONST 
    0x29d10x27fd: v27fd29d1 = ADD v27fd29cf(0x20), v299a_0
    0x29d60x27fd: v27fd29d6(0x0) = CONST 

    Begin block 0x29d80x27fd
    prev=[0x29e10x27fd, 0x29a60x27fd], succ=[0x29f00x27fd, 0x29e10x27fd]
    =================================
    0x29d80x27fd_0x0: v29d827fd_0 = PHI v27fd29eb, v27fd29d6(0x0)
    0x29db0x27fd: v27fd29db = LT v29d827fd_0, v27fd29cd
    0x29dc0x27fd: v27fd29dc = ISZERO v27fd29db
    0x29dd0x27fd: v27fd29dd(0x29f0) = CONST 
    0x29e00x27fd: JUMPI v27fd29dd(0x29f0), v27fd29dc

    Begin block 0x29f00x27fd
    prev=[0x29d80x27fd], succ=[0x2a1d0x27fd, 0x2a040x27fd]
    =================================
    0x29f90x27fd: v27fd29f9 = ADD v27fd29cd, v27fd29c9
    0x29fb0x27fd: v27fd29fb(0x1f) = CONST 
    0x29fd0x27fd: v27fd29fd = AND v27fd29fb(0x1f), v27fd29cd
    0x29ff0x27fd: v27fd29ff = ISZERO v27fd29fd
    0x2a000x27fd: v27fd2a00(0x2a1d) = CONST 
    0x2a030x27fd: JUMPI v27fd2a00(0x2a1d), v27fd29ff

    Begin block 0x2a1d0x27fd
    prev=[0x29f00x27fd, 0x2a040x27fd], succ=[]
    =================================
    0x2a1d0x27fd_0x1: v2a1d27fd_1 = PHI v27fd2a1a, v27fd29f9
    0x2a230x27fd: v27fd2a23(0x40) = CONST 
    0x2a250x27fd: v27fd2a25 = MLOAD v27fd2a23(0x40)
    0x2a280x27fd: v27fd2a28 = SUB v2a1d27fd_1, v27fd2a25
    0x2a2a0x27fd: REVERT v27fd2a25, v27fd2a28

    Begin block 0x2a040x27fd
    prev=[0x29f00x27fd], succ=[0x2a1d0x27fd]
    =================================
    0x2a060x27fd: v27fd2a06 = SUB v27fd29f9, v27fd29fd
    0x2a080x27fd: v27fd2a08 = MLOAD v27fd2a06
    0x2a090x27fd: v27fd2a09(0x1) = CONST 
    0x2a0c0x27fd: v27fd2a0c(0x20) = CONST 
    0x2a0e0x27fd: v27fd2a0e = SUB v27fd2a0c(0x20), v27fd29fd
    0x2a0f0x27fd: v27fd2a0f(0x100) = CONST 
    0x2a120x27fd: v27fd2a12 = EXP v27fd2a0f(0x100), v27fd2a0e
    0x2a130x27fd: v27fd2a13 = SUB v27fd2a12, v27fd2a09(0x1)
    0x2a140x27fd: v27fd2a14 = NOT v27fd2a13
    0x2a150x27fd: v27fd2a15 = AND v27fd2a14, v27fd2a08
    0x2a170x27fd: MSTORE v27fd2a06, v27fd2a15
    0x2a180x27fd: v27fd2a18(0x20) = CONST 
    0x2a1a0x27fd: v27fd2a1a = ADD v27fd2a18(0x20), v27fd2a06

    Begin block 0x29e10x27fd
    prev=[0x29d80x27fd], succ=[0x29d80x27fd]
    =================================
    0x29e10x27fd_0x0: v29e127fd_0 = PHI v27fd29eb, v27fd29d6(0x0)
    0x29e30x27fd: v27fd29e3 = ADD v29e127fd_0, v27fd29d1
    0x29e40x27fd: v27fd29e4 = MLOAD v27fd29e3
    0x29e70x27fd: v27fd29e7 = ADD v29e127fd_0, v27fd29c9
    0x29e80x27fd: MSTORE v27fd29e7, v27fd29e4
    0x29e90x27fd: v27fd29e9(0x20) = CONST 
    0x29eb0x27fd: v27fd29eb = ADD v27fd29e9(0x20), v29e127fd_0
    0x29ec0x27fd: v27fd29ec(0x29d8) = CONST 
    0x29ef0x27fd: JUMP v27fd29ec(0x29d8)

    Begin block 0x2a62
    prev=[0x298f], succ=[0x2a7b, 0x2ac70x27fd]
    =================================
    0x2a62_0x0: v2a62_0 = PHI v298c, v27fdarg0
    0x2a63: v2a63(0x1) = CONST 
    0x2a65: v2a65(0x1) = CONST 
    0x2a67: v2a67(0xe0) = CONST 
    0x2a69: v2a69(0x100000000000000000000000000000000000000000000000000000000) = SHL v2a67(0xe0), v2a65(0x1)
    0x2a6a: v2a6a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2a69(0x100000000000000000000000000000000000000000000000000000000), v2a63(0x1)
    0x2a6b: v2a6b(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2a6a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2a6d: v2a6d = AND v2a62_0, v2a6b(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x2a6e: v2a6e(0xbc197c81) = CONST 
    0x2a73: v2a73(0xe0) = CONST 
    0x2a75: v2a75(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v2a73(0xe0), v2a6e(0xbc197c81)
    0x2a76: v2a76 = EQ v2a75(0xbc197c8100000000000000000000000000000000000000000000000000000000), v2a6d
    0x2a77: v2a77(0x2ac7) = CONST 
    0x2a7a: JUMPI v2a77(0x2ac7), v2a76

    Begin block 0x2a7b
    prev=[0x2a62], succ=[]
    =================================
    0x2a7b: v2a7b(0x40) = CONST 
    0x2a7e: v2a7e = MLOAD v2a7b(0x40)
    0x2a7f: v2a7f(0x461bcd) = CONST 
    0x2a83: v2a83(0xe5) = CONST 
    0x2a85: v2a85(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2a83(0xe5), v2a7f(0x461bcd)
    0x2a87: MSTORE v2a7e, v2a85(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a88: v2a88(0x20) = CONST 
    0x2a8a: v2a8a(0x4) = CONST 
    0x2a8d: v2a8d = ADD v2a7e, v2a8a(0x4)
    0x2a8e: MSTORE v2a8d, v2a88(0x20)
    0x2a8f: v2a8f(0x1f) = CONST 
    0x2a91: v2a91(0x24) = CONST 
    0x2a94: v2a94 = ADD v2a7e, v2a91(0x24)
    0x2a95: MSTORE v2a94, v2a8f(0x1f)
    0x2a96: v2a96(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x2ab7: v2ab7(0x44) = CONST 
    0x2aba: v2aba = ADD v2a7e, v2ab7(0x44)
    0x2abb: MSTORE v2aba, v2a96(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x2abd: v2abd = MLOAD v2a7b(0x40)
    0x2ac1: v2ac1(0x0) = SUB v2a7e, v2abd
    0x2ac2: v2ac2(0x64) = CONST 
    0x2ac4: v2ac4(0x64) = ADD v2ac2(0x64), v2ac1(0x0)
    0x2ac6: REVERT v2abd, v2ac4(0x64)

    Begin block 0x2ac70x27fd
    prev=[0x2a62], succ=[0x2ac90x27fd]
    =================================

    Begin block 0x2ac90x27fd
    prev=[0x2ac70x27fd], succ=[]
    =================================
    0x2ad00x27fd: RETURNPRIVATE v27fdarg6

    Begin block 0x2978
    prev=[0x296a], succ=[0x2986, 0x298a]
    =================================
    0x2979: v2979(0x40) = CONST 
    0x297b: v297b = MLOAD v2979(0x40)
    0x297c: v297c = RETURNDATASIZE 
    0x297d: v297d(0x20) = CONST 
    0x2980: v2980 = LT v297c, v297d(0x20)
    0x2981: v2981 = ISZERO v2980
    0x2982: v2982(0x298a) = CONST 
    0x2985: JUMPI v2982(0x298a), v2981

    Begin block 0x2986
    prev=[0x2978], succ=[]
    =================================
    0x2986: v2986(0x0) = CONST 
    0x2989: REVERT v2986(0x0), v2986(0x0)

    Begin block 0x298a
    prev=[0x2978], succ=[0x298f]
    =================================
    0x298c: v298c = MLOAD v297b
    0x298d: v298d(0x1) = CONST 

    Begin block 0x292c
    prev=[0x2918], succ=[0x2945]
    =================================
    0x292e: v292e = SUB v2921, v2925
    0x2930: v2930 = MLOAD v292e
    0x2931: v2931(0x1) = CONST 
    0x2934: v2934(0x20) = CONST 
    0x2936: v2936 = SUB v2934(0x20), v2925
    0x2937: v2937(0x100) = CONST 
    0x293a: v293a = EXP v2937(0x100), v2936
    0x293b: v293b = SUB v293a, v2931(0x1)
    0x293c: v293c = NOT v293b
    0x293d: v293d = AND v293c, v2930
    0x293f: MSTORE v292e, v293d
    0x2940: v2940(0x20) = CONST 
    0x2942: v2942 = ADD v2940(0x20), v292e

    Begin block 0x2909
    prev=[0x2900], succ=[0x2900]
    =================================
    0x2909_0x0: v2909_0 = PHI v28fe(0x0), v2913
    0x290b: v290b = ADD v2909_0, v28f9
    0x290c: v290c = MLOAD v290b
    0x290f: v290f = ADD v2909_0, v28f1
    0x2910: MSTORE v290f, v290c
    0x2911: v2911(0x20) = CONST 
    0x2913: v2913 = ADD v2911(0x20), v2909_0
    0x2914: v2914(0x2900) = CONST 
    0x2917: JUMP v2914(0x2900)

    Begin block 0x28cd
    prev=[0x28c4], succ=[0x28c4]
    =================================
    0x28cd_0x0: v28cd_0 = PHI v28c2(0x0), v28d7
    0x28cf: v28cf = ADD v28cd_0, v28ba
    0x28d0: v28d0 = MLOAD v28cf
    0x28d3: v28d3 = ADD v28cd_0, v28b2
    0x28d4: MSTORE v28d3, v28d0
    0x28d5: v28d5(0x20) = CONST 
    0x28d7: v28d7 = ADD v28d5(0x20), v28cd_0
    0x28d8: v28d8(0x28c4) = CONST 
    0x28db: JUMP v28d8(0x28c4)

    Begin block 0x288e
    prev=[0x2885], succ=[0x2885]
    =================================
    0x288e_0x0: v288e_0 = PHI v2883(0x0), v2898
    0x2890: v2890 = ADD v288e_0, v287b
    0x2891: v2891 = MLOAD v2890
    0x2894: v2894 = ADD v288e_0, v2873
    0x2895: MSTORE v2894, v2891
    0x2896: v2896(0x20) = CONST 
    0x2898: v2898 = ADD v2896(0x20), v288e_0
    0x2899: v2899(0x2885) = CONST 
    0x289c: JUMP v2899(0x2885)

}

function setURI(string)() public {
    Begin block 0x299
    prev=[], succ=[0x2ab, 0x2af]
    =================================
    0x29a: v29a(0x3dd2) = CONST 
    0x29d: v29d(0x4) = CONST 
    0x2a0: v2a0 = CALLDATASIZE 
    0x2a1: v2a1 = SUB v2a0, v29d(0x4)
    0x2a2: v2a2(0x20) = CONST 
    0x2a5: v2a5 = LT v2a1, v2a2(0x20)
    0x2a6: v2a6 = ISZERO v2a5
    0x2a7: v2a7(0x2af) = CONST 
    0x2aa: JUMPI v2a7(0x2af), v2a6

    Begin block 0x2ab
    prev=[0x299], succ=[]
    =================================
    0x2ab: v2ab(0x0) = CONST 
    0x2ae: REVERT v2ab(0x0), v2ab(0x0)

    Begin block 0x2af
    prev=[0x299], succ=[0x2c5, 0x2c9]
    =================================
    0x2b1: v2b1 = ADD v29d(0x4), v2a1
    0x2b3: v2b3(0x20) = CONST 
    0x2b6: v2b6(0x24) = ADD v29d(0x4), v2b3(0x20)
    0x2b8: v2b8 = CALLDATALOAD v29d(0x4)
    0x2b9: v2b9(0x1) = CONST 
    0x2bb: v2bb(0x20) = CONST 
    0x2bd: v2bd(0x100000000) = SHL v2bb(0x20), v2b9(0x1)
    0x2bf: v2bf = GT v2b8, v2bd(0x100000000)
    0x2c0: v2c0 = ISZERO v2bf
    0x2c1: v2c1(0x2c9) = CONST 
    0x2c4: JUMPI v2c1(0x2c9), v2c0

    Begin block 0x2c5
    prev=[0x2af], succ=[]
    =================================
    0x2c5: v2c5(0x0) = CONST 
    0x2c8: REVERT v2c5(0x0), v2c5(0x0)

    Begin block 0x2c9
    prev=[0x2af], succ=[0x2d7, 0x2db]
    =================================
    0x2cb: v2cb = ADD v29d(0x4), v2b8
    0x2cd: v2cd(0x20) = CONST 
    0x2d0: v2d0 = ADD v2cb, v2cd(0x20)
    0x2d1: v2d1 = GT v2d0, v2b1
    0x2d2: v2d2 = ISZERO v2d1
    0x2d3: v2d3(0x2db) = CONST 
    0x2d6: JUMPI v2d3(0x2db), v2d2

    Begin block 0x2d7
    prev=[0x2c9], succ=[]
    =================================
    0x2d7: v2d7(0x0) = CONST 
    0x2da: REVERT v2d7(0x0), v2d7(0x0)

    Begin block 0x2db
    prev=[0x2c9], succ=[0x2f8, 0x2fc]
    =================================
    0x2dd: v2dd = CALLDATALOAD v2cb
    0x2df: v2df(0x20) = CONST 
    0x2e1: v2e1 = ADD v2df(0x20), v2cb
    0x2e4: v2e4(0x1) = CONST 
    0x2e7: v2e7 = MUL v2dd, v2e4(0x1)
    0x2e9: v2e9 = ADD v2e1, v2e7
    0x2ea: v2ea = GT v2e9, v2b1
    0x2eb: v2eb(0x1) = CONST 
    0x2ed: v2ed(0x20) = CONST 
    0x2ef: v2ef(0x100000000) = SHL v2ed(0x20), v2eb(0x1)
    0x2f1: v2f1 = GT v2dd, v2ef(0x100000000)
    0x2f2: v2f2 = OR v2f1, v2ea
    0x2f3: v2f3 = ISZERO v2f2
    0x2f4: v2f4(0x2fc) = CONST 
    0x2f7: JUMPI v2f4(0x2fc), v2f3

    Begin block 0x2f8
    prev=[0x2db], succ=[]
    =================================
    0x2f8: v2f8(0x0) = CONST 
    0x2fb: REVERT v2f8(0x0), v2f8(0x0)

    Begin block 0x2fc
    prev=[0x2db], succ=[0xeaf]
    =================================
    0x301: v301(0x1f) = CONST 
    0x303: v303 = ADD v301(0x1f), v2dd
    0x304: v304(0x20) = CONST 
    0x308: v308 = DIV v303, v304(0x20)
    0x309: v309 = MUL v308, v304(0x20)
    0x30a: v30a(0x20) = CONST 
    0x30c: v30c = ADD v30a(0x20), v309
    0x30d: v30d(0x40) = CONST 
    0x30f: v30f = MLOAD v30d(0x40)
    0x312: v312 = ADD v30f, v30c
    0x313: v313(0x40) = CONST 
    0x315: MSTORE v313(0x40), v312
    0x31d: MSTORE v30f, v2dd
    0x31e: v31e(0x20) = CONST 
    0x320: v320 = ADD v31e(0x20), v30f
    0x326: CALLDATACOPY v320, v2e1, v2dd
    0x327: v327(0x0) = CONST 
    0x32a: v32a = ADD v320, v2dd
    0x32e: MSTORE v32a, v327(0x0)
    0x333: v333(0xeaf) = CONST 
    0x33c: JUMP v333(0xeaf)

    Begin block 0xeaf
    prev=[0x2fc], succ=[0xec2, 0xf09]
    =================================
    0xeb0: veb0(0x4) = CONST 
    0xeb2: veb2 = SLOAD veb0(0x4)
    0xeb3: veb3(0x1) = CONST 
    0xeb5: veb5(0x1) = CONST 
    0xeb7: veb7(0xa0) = CONST 
    0xeb9: veb9(0x10000000000000000000000000000000000000000) = SHL veb7(0xa0), veb5(0x1)
    0xeba: veba(0xffffffffffffffffffffffffffffffffffffffff) = SUB veb9(0x10000000000000000000000000000000000000000), veb3(0x1)
    0xebb: vebb = AND veba(0xffffffffffffffffffffffffffffffffffffffff), veb2
    0xebc: vebc = CALLER 
    0xebd: vebd = EQ vebc, vebb
    0xebe: vebe(0xf09) = CONST 
    0xec1: JUMPI vebe(0xf09), vebd

    Begin block 0xec2
    prev=[0xeaf], succ=[]
    =================================
    0xec2: vec2(0x40) = CONST 
    0xec5: vec5 = MLOAD vec2(0x40)
    0xec6: vec6(0x461bcd) = CONST 
    0xeca: veca(0xe5) = CONST 
    0xecc: vecc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL veca(0xe5), vec6(0x461bcd)
    0xece: MSTORE vec5, vecc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xecf: vecf(0x20) = CONST 
    0xed1: ved1(0x4) = CONST 
    0xed4: ved4 = ADD vec5, ved1(0x4)
    0xed5: MSTORE ved4, vecf(0x20)
    0xed6: ved6(0x18) = CONST 
    0xed8: ved8(0x24) = CONST 
    0xedb: vedb = ADD vec5, ved8(0x24)
    0xedc: MSTORE vedb, ved6(0x18)
    0xedd: vedd(0x6d7573742062652067616c61787920636f6d6d756e697479) = CONST 
    0xef6: vef6(0x40) = CONST 
    0xef8: vef8(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000) = SHL vef6(0x40), vedd(0x6d7573742062652067616c61787920636f6d6d756e697479)
    0xef9: vef9(0x44) = CONST 
    0xefc: vefc = ADD vec5, vef9(0x44)
    0xefd: MSTORE vefc, vef8(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000)
    0xeff: veff = MLOAD vec2(0x40)
    0xf03: vf03(0x0) = SUB vec5, veff
    0xf04: vf04(0x64) = CONST 
    0xf06: vf06(0x64) = ADD vf04(0x64), vf03(0x0)
    0xf08: REVERT veff, vf06(0x64)

    Begin block 0xf09
    prev=[0xeaf], succ=[0x3813B0xf09]
    =================================
    0xf0b: vf0b = MLOAD v30f
    0xf0c: vf0c(0x4240) = CONST 
    0xf10: vf10(0x2) = CONST 
    0xf13: vf13(0x20) = CONST 
    0xf16: vf16 = ADD v30f, vf13(0x20)
    0xf18: vf18(0x3813) = CONST 
    0xf1b: JUMP vf18(0x3813)

    Begin block 0x3813B0xf09
    prev=[0xf09], succ=[0x3841B0xf09, 0x3849B0xf09]
    =================================
    0x3816S0xf09: v3816Vf09 = SLOAD vf10(0x2)
    0x3817S0xf09: v3817Vf09(0x1) = CONST 
    0x381aS0xf09: v381aVf09(0x1) = CONST 
    0x381cS0xf09: v381cVf09 = AND v381aVf09(0x1), v3816Vf09
    0x381dS0xf09: v381dVf09 = ISZERO v381cVf09
    0x381eS0xf09: v381eVf09(0x100) = CONST 
    0x3821S0xf09: v3821Vf09 = MUL v381eVf09(0x100), v381dVf09
    0x3822S0xf09: v3822Vf09 = SUB v3821Vf09, v3817Vf09(0x1)
    0x3823S0xf09: v3823Vf09 = AND v3822Vf09, v3816Vf09
    0x3824S0xf09: v3824Vf09(0x2) = CONST 
    0x3827S0xf09: v3827Vf09 = DIV v3823Vf09, v3824Vf09(0x2)
    0x3829S0xf09: v3829Vf09(0x0) = CONST 
    0x382bS0xf09: MSTORE v3829Vf09(0x0), vf10(0x2)
    0x382cS0xf09: v382cVf09(0x20) = CONST 
    0x382eS0xf09: v382eVf09(0x0) = CONST 
    0x3830S0xf09: v3830Vf09 = SHA3 v382eVf09(0x0), v382cVf09(0x20)
    0x3832S0xf09: v3832Vf09(0x1f) = CONST 
    0x3834S0xf09: v3834Vf09 = ADD v3832Vf09(0x1f), v3827Vf09
    0x3835S0xf09: v3835Vf09(0x20) = CONST 
    0x3838S0xf09: v3838Vf09 = DIV v3834Vf09, v3835Vf09(0x20)
    0x383aS0xf09: v383aVf09 = ADD v3830Vf09, v3838Vf09
    0x383dS0xf09: v383dVf09(0x3849) = CONST 
    0x3840S0xf09: JUMPI v383dVf09(0x3849), vf0b

    Begin block 0x3841B0xf09
    prev=[0x3813B0xf09], succ=[0x388f0x3813B0xf09]
    =================================
    0x3841S0xf09: v3841Vf09(0x0) = CONST 
    0x3844S0xf09: SSTORE vf10(0x2), v3841Vf09(0x0)
    0x3845S0xf09: v3845Vf09(0x388f) = CONST 
    0x3848S0xf09: JUMP v3845Vf09(0x388f)

    Begin block 0x388f0x3813B0xf09
    prev=[0x3841B0xf09, 0x3862B0xf09, 0x3874B0xf09, 0x3852B0xf09], succ=[0x394eB0x388f0x3813B0xf09]
    =================================
    0x388f0x3813_0x1S0xf09: v388f3813_1Vf09 = PHI v3830Vf09, v3889Vf09
    0x38910x3813S0xf09: v38133891Vf09(0x4579) = CONST 
    0x38970x3813S0xf09: v38133897Vf09(0x394e) = CONST 
    0x389a0x3813S0xf09: JUMP v38133897Vf09(0x394e)

    Begin block 0x394eB0x388f0x3813B0xf09
    prev=[0x388f0x3813B0xf09], succ=[0x394fB0x388f0x3813B0xf09]
    =================================

    Begin block 0x394fB0x388f0x3813B0xf09
    prev=[0x3958B0x388f0x3813B0xf09, 0x394eB0x388f0x3813B0xf09], succ=[0x3958B0x388f0x3813B0xf09, 0x459cB0x388f0x3813B0xf09]
    =================================
    0x394f_0x0S0x388f0x3813S0xf09: v394f_0V388f3813Vf09 = PHI v388f3813_1Vf09, v395eV388f3813Vf09
    0x3952S0x388f0x3813S0xf09: v3952V388f3813Vf09 = GT v383aVf09, v394f_0V388f3813Vf09
    0x3953S0x388f0x3813S0xf09: v3953V388f3813Vf09 = ISZERO v3952V388f3813Vf09
    0x3954S0x388f0x3813S0xf09: v3954V388f3813Vf09(0x459c) = CONST 
    0x3957S0x388f0x3813S0xf09: JUMPI v3954V388f3813Vf09(0x459c), v3953V388f3813Vf09

    Begin block 0x3958B0x388f0x3813B0xf09
    prev=[0x394fB0x388f0x3813B0xf09], succ=[0x394fB0x388f0x3813B0xf09]
    =================================
    0x3958S0x388f0x3813S0xf09: v3958V388f3813Vf09(0x0) = CONST 
    0x3958_0x0S0x388f0x3813S0xf09: v3958_0V388f3813Vf09 = PHI v388f3813_1Vf09, v395eV388f3813Vf09
    0x395bS0x388f0x3813S0xf09: SSTORE v3958_0V388f3813Vf09, v3958V388f3813Vf09(0x0)
    0x395cS0x388f0x3813S0xf09: v395cV388f3813Vf09(0x1) = CONST 
    0x395eS0x388f0x3813S0xf09: v395eV388f3813Vf09 = ADD v395cV388f3813Vf09(0x1), v3958_0V388f3813Vf09
    0x395fS0x388f0x3813S0xf09: v395fV388f3813Vf09(0x394f) = CONST 
    0x3962S0x388f0x3813S0xf09: JUMP v395fV388f3813Vf09(0x394f)

    Begin block 0x459cB0x388f0x3813B0xf09
    prev=[0x394fB0x388f0x3813B0xf09], succ=[0x45790x3813B0xf09]
    =================================
    0x459fS0x388f0x3813S0xf09: JUMP v38133891Vf09(0x4579)

    Begin block 0x45790x3813B0xf09
    prev=[0x459cB0x388f0x3813B0xf09], succ=[0x4240]
    =================================
    0x457c0x3813S0xf09: JUMP vf0c(0x4240)

    Begin block 0x4240
    prev=[0x45790x3813B0xf09], succ=[0x3dd2]
    =================================
    0x4243: JUMP v29a(0x3dd2)

    Begin block 0x3dd2
    prev=[0x4240], succ=[]
    =================================
    0x3dd3: STOP 

    Begin block 0x3849B0xf09
    prev=[0x3813B0xf09], succ=[0x3862B0xf09, 0x3852B0xf09]
    =================================
    0x384bS0xf09: v384bVf09(0x1f) = CONST 
    0x384dS0xf09: v384dVf09 = LT v384bVf09(0x1f), vf0b
    0x384eS0xf09: v384eVf09(0x3862) = CONST 
    0x3851S0xf09: JUMPI v384eVf09(0x3862), v384dVf09

    Begin block 0x3862B0xf09
    prev=[0x3849B0xf09], succ=[0x3871B0xf09, 0x388f0x3813B0xf09]
    =================================
    0x3865S0xf09: v3865Vf09 = ADD vf0b, vf0b
    0x3866S0xf09: v3866Vf09(0x1) = CONST 
    0x3868S0xf09: v3868Vf09 = ADD v3866Vf09(0x1), v3865Vf09
    0x386aS0xf09: SSTORE vf10(0x2), v3868Vf09
    0x386cS0xf09: v386cVf09 = ISZERO vf0b
    0x386dS0xf09: v386dVf09(0x388f) = CONST 
    0x3870S0xf09: JUMPI v386dVf09(0x388f), v386cVf09

    Begin block 0x3871B0xf09
    prev=[0x3862B0xf09], succ=[0x3874B0xf09]
    =================================
    0x3873S0xf09: v3873Vf09 = ADD vf16, vf0b

    Begin block 0x3874B0xf09
    prev=[0x3871B0xf09, 0x387dB0xf09], succ=[0x387dB0xf09, 0x388f0x3813B0xf09]
    =================================
    0x3874_0x2S0xf09: v3874_2Vf09 = PHI vf16, v3884Vf09
    0x3877S0xf09: v3877Vf09 = GT v3873Vf09, v3874_2Vf09
    0x3878S0xf09: v3878Vf09 = ISZERO v3877Vf09
    0x3879S0xf09: v3879Vf09(0x388f) = CONST 
    0x387cS0xf09: JUMPI v3879Vf09(0x388f), v3878Vf09

    Begin block 0x387dB0xf09
    prev=[0x3874B0xf09], succ=[0x3874B0xf09]
    =================================
    0x387d_0x1S0xf09: v387d_1Vf09 = PHI v3830Vf09, v3889Vf09
    0x387d_0x2S0xf09: v387d_2Vf09 = PHI vf16, v3884Vf09
    0x387eS0xf09: v387eVf09 = MLOAD v387d_2Vf09
    0x3880S0xf09: SSTORE v387d_1Vf09, v387eVf09
    0x3882S0xf09: v3882Vf09(0x20) = CONST 
    0x3884S0xf09: v3884Vf09 = ADD v3882Vf09(0x20), v387d_2Vf09
    0x3887S0xf09: v3887Vf09(0x1) = CONST 
    0x3889S0xf09: v3889Vf09 = ADD v3887Vf09(0x1), v387d_1Vf09
    0x388bS0xf09: v388bVf09(0x3874) = CONST 
    0x388eS0xf09: JUMP v388bVf09(0x3874)

    Begin block 0x3852B0xf09
    prev=[0x3849B0xf09], succ=[0x388f0x3813B0xf09]
    =================================
    0x3853S0xf09: v3853Vf09 = MLOAD vf16
    0x3854S0xf09: v3854Vf09(0xff) = CONST 
    0x3856S0xf09: v3856Vf09(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v3854Vf09(0xff)
    0x3857S0xf09: v3857Vf09 = AND v3856Vf09(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v3853Vf09
    0x385aS0xf09: v385aVf09 = ADD vf0b, vf0b
    0x385bS0xf09: v385bVf09 = OR v385aVf09, v3857Vf09
    0x385dS0xf09: SSTORE vf10(0x2), v385bVf09
    0x385eS0xf09: v385eVf09(0x388f) = CONST 
    0x3861S0xf09: JUMP v385eVf09(0x388f)

}

function 0x2ad1(0x2ad1arg0x0, 0x2ad1arg0x1, 0x2ad1arg0x2) private {
    Begin block 0x2ad1
    prev=[], succ=[0x2ae2, 0x2b2e]
    =================================
    0x2ad2: v2ad2(0x0) = CONST 
    0x2ad4: v2ad4(0x1) = CONST 
    0x2ad6: v2ad6(0x1) = CONST 
    0x2ad8: v2ad8(0xa0) = CONST 
    0x2ada: v2ada(0x10000000000000000000000000000000000000000) = SHL v2ad8(0xa0), v2ad6(0x1)
    0x2adb: v2adb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ada(0x10000000000000000000000000000000000000000), v2ad4(0x1)
    0x2add: v2add = AND v2ad1arg1, v2adb(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ade: v2ade(0x2b2e) = CONST 
    0x2ae1: JUMPI v2ade(0x2b2e), v2add

    Begin block 0x2ae2
    prev=[0x2ad1], succ=[]
    =================================
    0x2ae2: v2ae2(0x40) = CONST 
    0x2ae5: v2ae5 = MLOAD v2ae2(0x40)
    0x2ae6: v2ae6(0x461bcd) = CONST 
    0x2aea: v2aea(0xe5) = CONST 
    0x2aec: v2aec(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2aea(0xe5), v2ae6(0x461bcd)
    0x2aee: MSTORE v2ae5, v2aec(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2aef: v2aef(0x20) = CONST 
    0x2af1: v2af1(0x4) = CONST 
    0x2af4: v2af4 = ADD v2ae5, v2af1(0x4)
    0x2af5: MSTORE v2af4, v2aef(0x20)
    0x2af6: v2af6(0x1d) = CONST 
    0x2af8: v2af8(0x24) = CONST 
    0x2afb: v2afb = ADD v2ae5, v2af8(0x24)
    0x2afc: MSTORE v2afb, v2af6(0x1d)
    0x2afd: v2afd(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x2b1e: v2b1e(0x44) = CONST 
    0x2b21: v2b21 = ADD v2ae5, v2b1e(0x44)
    0x2b22: MSTORE v2b21, v2afd(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x2b24: v2b24 = MLOAD v2ae2(0x40)
    0x2b28: v2b28(0x0) = SUB v2ae5, v2b24
    0x2b29: v2b29(0x64) = CONST 
    0x2b2b: v2b2b(0x64) = ADD v2b29(0x64), v2b28(0x0)
    0x2b2d: REVERT v2b24, v2b2b(0x64)

    Begin block 0x2b2e
    prev=[0x2ad1], succ=[0x4495]
    =================================
    0x2b2f: v2b2f(0x7) = CONST 
    0x2b32: v2b32 = SLOAD v2b2f(0x7)
    0x2b33: v2b33(0x1) = CONST 
    0x2b37: v2b37 = ADD v2b33(0x1), v2b32
    0x2b3b: SSTORE v2b2f(0x7), v2b37
    0x2b3c: v2b3c(0x0) = CONST 
    0x2b40: MSTORE v2b3c(0x0), v2b37
    0x2b41: v2b41(0x8) = CONST 
    0x2b43: v2b43(0x20) = CONST 
    0x2b47: MSTORE v2b43(0x20), v2b41(0x8)
    0x2b48: v2b48(0x40) = CONST 
    0x2b4c: v2b4c = SHA3 v2b3c(0x0), v2b48(0x40)
    0x2b4e: v2b4e = SLOAD v2b4c
    0x2b4f: v2b4f(0x1) = CONST 
    0x2b51: v2b51(0x1) = CONST 
    0x2b53: v2b53(0xa0) = CONST 
    0x2b55: v2b55(0x10000000000000000000000000000000000000000) = SHL v2b53(0xa0), v2b51(0x1)
    0x2b56: v2b56(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b55(0x10000000000000000000000000000000000000000), v2b4f(0x1)
    0x2b59: v2b59 = AND v2ad1arg1, v2b56(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b5a: v2b5a(0x1) = CONST 
    0x2b5c: v2b5c(0x1) = CONST 
    0x2b5e: v2b5e(0xa0) = CONST 
    0x2b60: v2b60(0x10000000000000000000000000000000000000000) = SHL v2b5e(0xa0), v2b5c(0x1)
    0x2b61: v2b61(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b60(0x10000000000000000000000000000000000000000), v2b5a(0x1)
    0x2b62: v2b62(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2b61(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b65: v2b65 = AND v2b62(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2b4e
    0x2b67: v2b67 = OR v2b59, v2b65
    0x2b6a: SSTORE v2b4c, v2b67
    0x2b6c: v2b6c = MLOAD v2b48(0x40)
    0x2b6d: v2b6d(0x60) = CONST 
    0x2b70: v2b70 = ADD v2b6c, v2b6d(0x60)
    0x2b72: MSTORE v2b48(0x40), v2b70
    0x2b73: v2b73(0x1) = CONST 
    0x2b75: v2b75(0x1) = CONST 
    0x2b77: v2b77(0x80) = CONST 
    0x2b79: v2b79(0x100000000000000000000000000000000) = SHL v2b77(0x80), v2b75(0x1)
    0x2b7a: v2b7a(0xffffffffffffffffffffffffffffffff) = SUB v2b79(0x100000000000000000000000000000000), v2b73(0x1)
    0x2b7b: v2b7b = NUMBER 
    0x2b7d: v2b7d = AND v2b7a(0xffffffffffffffffffffffffffffffff), v2b7b
    0x2b7f: MSTORE v2b6c, v2b7d
    0x2b82: v2b82 = AND v2b7a(0xffffffffffffffffffffffffffffffff), v2ad1arg0
    0x2b85: v2b85 = ADD v2b43(0x20), v2b6c
    0x2b88: MSTORE v2b85, v2b82
    0x2b8b: v2b8b = ADD v2b48(0x40), v2b6c
    0x2b8e: MSTORE v2b8b, v2b59
    0x2b91: MSTORE v2b3c(0x0), v2b37
    0x2b92: v2b92(0xa) = CONST 
    0x2b95: MSTORE v2b43(0x20), v2b92(0xa)
    0x2b98: v2b98 = SHA3 v2b3c(0x0), v2b48(0x40)
    0x2b9a: v2b9a = MLOAD v2b6c
    0x2b9c: v2b9c = SLOAD v2b98
    0x2b9e: v2b9e = MLOAD v2b85
    0x2ba0: v2ba0 = AND v2b7a(0xffffffffffffffffffffffffffffffff), v2b9e
    0x2ba1: v2ba1(0x1) = CONST 
    0x2ba3: v2ba3(0x80) = CONST 
    0x2ba5: v2ba5(0x100000000000000000000000000000000) = SHL v2ba3(0x80), v2ba1(0x1)
    0x2ba6: v2ba6 = MUL v2ba5(0x100000000000000000000000000000000), v2ba0
    0x2ba9: v2ba9 = AND v2b7a(0xffffffffffffffffffffffffffffffff), v2b9a
    0x2baa: v2baa(0x1) = CONST 
    0x2bac: v2bac(0x1) = CONST 
    0x2bae: v2bae(0x80) = CONST 
    0x2bb0: v2bb0(0x100000000000000000000000000000000) = SHL v2bae(0x80), v2bac(0x1)
    0x2bb1: v2bb1(0xffffffffffffffffffffffffffffffff) = SUB v2bb0(0x100000000000000000000000000000000), v2baa(0x1)
    0x2bb2: v2bb2(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) = NOT v2bb1(0xffffffffffffffffffffffffffffffff)
    0x2bb5: v2bb5 = AND v2b9c, v2bb2(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000)
    0x2bb9: v2bb9 = OR v2bb5, v2ba9
    0x2bbc: v2bbc = AND v2b7a(0xffffffffffffffffffffffffffffffff), v2bb9
    0x2bbd: v2bbd = OR v2bbc, v2ba6
    0x2bbf: SSTORE v2b98, v2bbd
    0x2bc0: v2bc0 = MLOAD v2b8b
    0x2bc3: v2bc3 = ADD v2b33(0x1), v2b98
    0x2bc5: v2bc5 = SLOAD v2bc3
    0x2bc9: v2bc9 = AND v2b56(0xffffffffffffffffffffffffffffffffffffffff), v2bc0
    0x2bcb: v2bcb = AND v2b62(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2bc5
    0x2bcf: v2bcf = OR v2bcb, v2bc9
    0x2bd1: SSTORE v2bc3, v2bcf
    0x2bd3: v2bd3 = MLOAD v2b48(0x40)
    0x2bd6: MSTORE v2bd3, v2b37
    0x2bd9: v2bd9 = ADD v2bd3, v2b43(0x20)
    0x2bdd: MSTORE v2bd9, v2b33(0x1)
    0x2bdf: v2bdf = MLOAD v2b48(0x40)
    0x2be0: v2be0 = CALLER 
    0x2be2: v2be2(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x2c07: v2c07(0x0) = SUB v2bd3, v2bdf
    0x2c08: v2c08(0x40) = ADD v2c07(0x0), v2b48(0x40)
    0x2c0a: LOG4 v2bdf, v2c08(0x40), v2be2(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v2be0, v2b3c(0x0), v2b59
    0x2c0b: v2c0b(0x4495) = CONST 
    0x2c0e: v2c0e = CALLER 
    0x2c0f: v2c0f(0x0) = CONST 
    0x2c13: v2c13(0x1) = CONST 
    0x2c15: v2c15(0x40) = CONST 
    0x2c17: v2c17 = MLOAD v2c15(0x40)
    0x2c19: v2c19(0x20) = CONST 
    0x2c1b: v2c1b = ADD v2c19(0x20), v2c17
    0x2c1c: v2c1c(0x40) = CONST 
    0x2c1e: MSTORE v2c1c(0x40), v2c1b
    0x2c20: v2c20(0x0) = CONST 
    0x2c23: MSTORE v2c17, v2c20(0x0)
    0x2c25: v2c25(0x34fd) = CONST 
    0x2c28: CALLPRIVATE v2c25(0x34fd), v2c17, v2c13(0x1), v2b37, v2ad1arg1, v2c0f(0x0), v2c0e, v2c0b(0x4495)

    Begin block 0x4495
    prev=[0x2b2e], succ=[]
    =================================
    0x449b: RETURNPRIVATE v2ad1arg2, v2b37

}

function uri(uint256)() public {
    Begin block 0x33f
    prev=[], succ=[0x351, 0x355]
    =================================
    0x340: v340(0x35c) = CONST 
    0x343: v343(0x4) = CONST 
    0x346: v346 = CALLDATASIZE 
    0x347: v347 = SUB v346, v343(0x4)
    0x348: v348(0x20) = CONST 
    0x34b: v34b = LT v347, v348(0x20)
    0x34c: v34c = ISZERO v34b
    0x34d: v34d(0x355) = CONST 
    0x350: JUMPI v34d(0x355), v34c

    Begin block 0x351
    prev=[0x33f], succ=[]
    =================================
    0x351: v351(0x0) = CONST 
    0x354: REVERT v351(0x0), v351(0x0)

    Begin block 0x355
    prev=[0x33f], succ=[0xf20]
    =================================
    0x357: v357 = CALLDATALOAD v343(0x4)
    0x358: v358(0xf20) = CONST 
    0x35b: JUMP v358(0xf20)

    Begin block 0xf20
    prev=[0x355], succ=[0xf2d, 0xf79]
    =================================
    0xf21: vf21(0x60) = CONST 
    0xf23: vf23(0x7) = CONST 
    0xf25: vf25 = SLOAD vf23(0x7)
    0xf27: vf27 = GT v357, vf25
    0xf28: vf28 = ISZERO vf27
    0xf29: vf29(0xf79) = CONST 
    0xf2c: JUMPI vf29(0xf79), vf28

    Begin block 0xf2d
    prev=[0xf20], succ=[]
    =================================
    0xf2d: vf2d(0x40) = CONST 
    0xf30: vf30 = MLOAD vf2d(0x40)
    0xf31: vf31(0x461bcd) = CONST 
    0xf35: vf35(0xe5) = CONST 
    0xf37: vf37(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf35(0xe5), vf31(0x461bcd)
    0xf39: MSTORE vf30, vf37(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf3a: vf3a(0x20) = CONST 
    0xf3c: vf3c(0x4) = CONST 
    0xf3f: vf3f = ADD vf30, vf3c(0x4)
    0xf40: MSTORE vf3f, vf3a(0x20)
    0xf41: vf41(0x17) = CONST 
    0xf43: vf43(0x24) = CONST 
    0xf46: vf46 = ADD vf30, vf43(0x24)
    0xf47: MSTORE vf46, vf41(0x17)
    0xf48: vf48(0x53746172206e667420646f6573206e6f74206578697374000000000000000000) = CONST 
    0xf69: vf69(0x44) = CONST 
    0xf6c: vf6c = ADD vf30, vf69(0x44)
    0xf6d: MSTORE vf6c, vf48(0x53746172206e667420646f6573206e6f74206578697374000000000000000000)
    0xf6f: vf6f = MLOAD vf2d(0x40)
    0xf73: vf73(0x0) = SUB vf30, vf6f
    0xf74: vf74(0x64) = CONST 
    0xf76: vf76(0x64) = ADD vf74(0x64), vf73(0x0)
    0xf78: REVERT vf6f, vf76(0x64)

    Begin block 0xf79
    prev=[0xf20], succ=[0xfa5, 0xf91]
    =================================
    0xf7a: vf7a(0x2) = CONST 
    0xf7d: vf7d = SLOAD vf7a(0x2)
    0xf7e: vf7e(0x0) = CONST 
    0xf80: vf80(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vf7e(0x0)
    0xf81: vf81(0x100) = CONST 
    0xf84: vf84(0x1) = CONST 
    0xf87: vf87 = AND vf7d, vf84(0x1)
    0xf88: vf88 = ISZERO vf87
    0xf89: vf89 = MUL vf88, vf81(0x100)
    0xf8a: vf8a = ADD vf89, vf80(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xf8b: vf8b = AND vf8a, vf7d
    0xf8c: vf8c = DIV vf8b, vf7a(0x2)
    0xf8d: vf8d(0xfa5) = CONST 
    0xf90: JUMPI vf8d(0xfa5), vf8c

    Begin block 0xfa5
    prev=[0xf79], succ=[0xfb0]
    =================================
    0xfa6: vfa6(0x2) = CONST 
    0xfa8: vfa8(0xfb0) = CONST 
    0xfac: vfac(0x26ae) = CONST 
    0xfaf: vfaf_0 = CALLPRIVATE vfac(0x26ae), v357, vfa8(0xfb0)

    Begin block 0xfb0
    prev=[0xfa5], succ=[0x100e, 0xfd2]
    =================================
    0xfb1: vfb1(0x40) = CONST 
    0xfb3: vfb3 = MLOAD vfb1(0x40)
    0xfb4: vfb4(0x20) = CONST 
    0xfb6: vfb6 = ADD vfb4(0x20), vfb3
    0xfba: vfba = SLOAD vfa6(0x2)
    0xfbb: vfbb(0x1) = CONST 
    0xfbe: vfbe(0x1) = CONST 
    0xfc0: vfc0 = AND vfbe(0x1), vfba
    0xfc1: vfc1 = ISZERO vfc0
    0xfc2: vfc2(0x100) = CONST 
    0xfc5: vfc5 = MUL vfc2(0x100), vfc1
    0xfc6: vfc6 = SUB vfc5, vfbb(0x1)
    0xfc7: vfc7 = AND vfc6, vfba
    0xfc8: vfc8(0x2) = CONST 
    0xfcb: vfcb = DIV vfc7, vfc8(0x2)
    0xfcd: vfcd = ISZERO vfcb
    0xfce: vfce(0x100e) = CONST 
    0xfd1: JUMPI vfce(0x100e), vfcd

    Begin block 0x100e
    prev=[0xfda, 0xfb0, 0xffa], succ=[0x101b]
    =================================
    0x1012: v1012 = MLOAD vfaf_0
    0x1013: v1013(0x20) = CONST 
    0x1016: v1016 = ADD vfaf_0, v1013(0x20)

    Begin block 0x101b
    prev=[0x100e, 0x1024], succ=[0x103a, 0x1024]
    =================================
    0x101b_0x2: v101b_2 = PHI v1012, v102d
    0x101c: v101c(0x20) = CONST 
    0x101f: v101f = LT v101b_2, v101c(0x20)
    0x1020: v1020(0x103a) = CONST 
    0x1023: JUMPI v1020(0x103a), v101f

    Begin block 0x103a
    prev=[0x101b], succ=[0x4287]
    =================================
    0x103a_0x0: v103a_0 = PHI v1016, v1035
    0x103a_0x1: v103a_1 = PHI vfb6, vfe6, vfee, v1033
    0x103a_0x2: v103a_2 = PHI v1012, v102d
    0x103a_0x5: v103a_5 = PHI vfb6, vfe6, vfee
    0x103b: v103b(0x1) = CONST 
    0x103e: v103e(0x20) = CONST 
    0x1040: v1040 = SUB v103e(0x20), v103a_2
    0x1041: v1041(0x100) = CONST 
    0x1044: v1044 = EXP v1041(0x100), v1040
    0x1045: v1045 = SUB v1044, v103b(0x1)
    0x1047: v1047 = NOT v1045
    0x1049: v1049 = MLOAD v103a_0
    0x104a: v104a = AND v1049, v1047
    0x104d: v104d = MLOAD v103a_1
    0x104e: v104e = AND v104d, v1045
    0x1051: v1051 = OR v104a, v104e
    0x1053: MSTORE v103a_1, v1051
    0x105c: v105c = ADD v1012, v103a_5
    0x105e: v105e(0x173539b7b7) = CONST 
    0x1064: v1064(0xd9) = CONST 
    0x1066: v1066(0x2e6a736f6e000000000000000000000000000000000000000000000000000000) = SHL v1064(0xd9), v105e(0x173539b7b7)
    0x1068: MSTORE v105c, v1066(0x2e6a736f6e000000000000000000000000000000000000000000000000000000)
    0x106a: v106a(0x5) = CONST 
    0x106c: v106c = ADD v106a(0x5), v105c
    0x1071: v1071(0x40) = CONST 
    0x1073: v1073 = MLOAD v1071(0x40)
    0x1074: v1074(0x20) = CONST 
    0x1078: v1078 = SUB v106c, v1073
    0x1079: v1079 = SUB v1078, v1074(0x20)
    0x107b: MSTORE v1073, v1079
    0x107d: v107d(0x40) = CONST 
    0x107f: MSTORE v107d(0x40), v106c
    0x1082: v1082(0x4287) = CONST 
    0x1085: JUMP v1082(0x4287)

    Begin block 0x4287
    prev=[0x103a], succ=[0x35c0x33f]
    =================================
    0x428b: JUMP v340(0x35c)

    Begin block 0x35c0x33f
    prev=[0x4263, 0x4287], succ=[0x37e0x33f]
    =================================
    0x35c0x33f_0x0: v35c33f_0 = PHI vf95, v1073
    0x35d0x33f: v33f35d(0x40) = CONST 
    0x3600x33f: v33f360 = MLOAD v33f35d(0x40)
    0x3610x33f: v33f361(0x20) = CONST 
    0x3650x33f: MSTORE v33f360, v33f361(0x20)
    0x3670x33f: v33f367 = MLOAD v35c33f_0
    0x36a0x33f: v33f36a = ADD v33f360, v33f361(0x20)
    0x36b0x33f: MSTORE v33f36a, v33f367
    0x36d0x33f: v33f36d = MLOAD v35c33f_0
    0x3740x33f: v33f374 = ADD v33f360, v33f35d(0x40)
    0x3770x33f: v33f377 = ADD v35c33f_0, v33f361(0x20)
    0x37c0x33f: v33f37c(0x0) = CONST 

    Begin block 0x37e0x33f
    prev=[0x3870x33f, 0x35c0x33f], succ=[0x3960x33f, 0x3870x33f]
    =================================
    0x37e0x33f_0x0: v37e33f_0 = PHI v33f391, v33f37c(0x0)
    0x3810x33f: v33f381 = LT v37e33f_0, v33f36d
    0x3820x33f: v33f382 = ISZERO v33f381
    0x3830x33f: v33f383(0x396) = CONST 
    0x3860x33f: JUMPI v33f383(0x396), v33f382

    Begin block 0x3960x33f
    prev=[0x37e0x33f], succ=[0x3c30x33f, 0x3aa0x33f]
    =================================
    0x39f0x33f: v33f39f = ADD v33f36d, v33f374
    0x3a10x33f: v33f3a1(0x1f) = CONST 
    0x3a30x33f: v33f3a3 = AND v33f3a1(0x1f), v33f36d
    0x3a50x33f: v33f3a5 = ISZERO v33f3a3
    0x3a60x33f: v33f3a6(0x3c3) = CONST 
    0x3a90x33f: JUMPI v33f3a6(0x3c3), v33f3a5

    Begin block 0x3c30x33f
    prev=[0x3960x33f, 0x3aa0x33f], succ=[]
    =================================
    0x3c30x33f_0x1: v3c333f_1 = PHI v33f3c0, v33f39f
    0x3c90x33f: v33f3c9(0x40) = CONST 
    0x3cb0x33f: v33f3cb = MLOAD v33f3c9(0x40)
    0x3ce0x33f: v33f3ce = SUB v3c333f_1, v33f3cb
    0x3d00x33f: RETURN v33f3cb, v33f3ce

    Begin block 0x3aa0x33f
    prev=[0x3960x33f], succ=[0x3c30x33f]
    =================================
    0x3ac0x33f: v33f3ac = SUB v33f39f, v33f3a3
    0x3ae0x33f: v33f3ae = MLOAD v33f3ac
    0x3af0x33f: v33f3af(0x1) = CONST 
    0x3b20x33f: v33f3b2(0x20) = CONST 
    0x3b40x33f: v33f3b4 = SUB v33f3b2(0x20), v33f3a3
    0x3b50x33f: v33f3b5(0x100) = CONST 
    0x3b80x33f: v33f3b8 = EXP v33f3b5(0x100), v33f3b4
    0x3b90x33f: v33f3b9 = SUB v33f3b8, v33f3af(0x1)
    0x3ba0x33f: v33f3ba = NOT v33f3b9
    0x3bb0x33f: v33f3bb = AND v33f3ba, v33f3ae
    0x3bd0x33f: MSTORE v33f3ac, v33f3bb
    0x3be0x33f: v33f3be(0x20) = CONST 
    0x3c00x33f: v33f3c0 = ADD v33f3be(0x20), v33f3ac

    Begin block 0x3870x33f
    prev=[0x37e0x33f], succ=[0x37e0x33f]
    =================================
    0x3870x33f_0x0: v38733f_0 = PHI v33f391, v33f37c(0x0)
    0x3890x33f: v33f389 = ADD v38733f_0, v33f377
    0x38a0x33f: v33f38a = MLOAD v33f389
    0x38d0x33f: v33f38d = ADD v38733f_0, v33f374
    0x38e0x33f: MSTORE v33f38d, v33f38a
    0x38f0x33f: v33f38f(0x20) = CONST 
    0x3910x33f: v33f391 = ADD v33f38f(0x20), v38733f_0
    0x3920x33f: v33f392(0x37e) = CONST 
    0x3950x33f: JUMP v33f392(0x37e)

    Begin block 0x1024
    prev=[0x101b], succ=[0x101b]
    =================================
    0x1024_0x0: v1024_0 = PHI v1016, v1035
    0x1024_0x1: v1024_1 = PHI vfb6, vfe6, vfee, v1033
    0x1024_0x2: v1024_2 = PHI v1012, v102d
    0x1025: v1025 = MLOAD v1024_0
    0x1027: MSTORE v1024_1, v1025
    0x1028: v1028(0x1f) = CONST 
    0x102a: v102a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1028(0x1f)
    0x102d: v102d = ADD v1024_2, v102a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x102f: v102f(0x20) = CONST 
    0x1033: v1033 = ADD v102f(0x20), v1024_1
    0x1035: v1035 = ADD v102f(0x20), v1024_0
    0x1036: v1036(0x101b) = CONST 
    0x1039: JUMP v1036(0x101b)

    Begin block 0xfd2
    prev=[0xfb0], succ=[0xfda, 0xfec]
    =================================
    0xfd3: vfd3(0x1f) = CONST 
    0xfd5: vfd5 = LT vfd3(0x1f), vfcb
    0xfd6: vfd6(0xfec) = CONST 
    0xfd9: JUMPI vfd6(0xfec), vfd5

    Begin block 0xfda
    prev=[0xfd2], succ=[0x100e]
    =================================
    0xfda: vfda(0x100) = CONST 
    0xfdf: vfdf = SLOAD vfa6(0x2)
    0xfe0: vfe0 = DIV vfdf, vfda(0x100)
    0xfe1: vfe1 = MUL vfe0, vfda(0x100)
    0xfe3: MSTORE vfb6, vfe1
    0xfe6: vfe6 = ADD vfcb, vfb6
    0xfe8: vfe8(0x100e) = CONST 
    0xfeb: JUMP vfe8(0x100e)

    Begin block 0xfec
    prev=[0xfd2], succ=[0xffa]
    =================================
    0xfee: vfee = ADD vfb6, vfcb
    0xff1: vff1(0x0) = CONST 
    0xff3: MSTORE vff1(0x0), vfa6(0x2)
    0xff4: vff4(0x20) = CONST 
    0xff6: vff6(0x0) = CONST 
    0xff8: vff8 = SHA3 vff6(0x0), vff4(0x20)

    Begin block 0xffa
    prev=[0xfec, 0xffa], succ=[0x100e, 0xffa]
    =================================
    0xffa_0x0: vffa_0 = PHI vfb6, v1006
    0xffa_0x1: vffa_1 = PHI vff8, v1002
    0xffc: vffc = SLOAD vffa_1
    0xffe: MSTORE vffa_0, vffc
    0x1000: v1000(0x1) = CONST 
    0x1002: v1002 = ADD v1000(0x1), vffa_1
    0x1004: v1004(0x20) = CONST 
    0x1006: v1006 = ADD v1004(0x20), vffa_0
    0x1009: v1009 = GT vfee, v1006
    0x100a: v100a(0xffa) = CONST 
    0x100d: JUMPI v100a(0xffa), v1009

    Begin block 0xf91
    prev=[0xf79], succ=[0x4263]
    =================================
    0xf92: vf92(0x40) = CONST 
    0xf95: vf95 = MLOAD vf92(0x40)
    0xf96: vf96(0x20) = CONST 
    0xf99: vf99 = ADD vf95, vf96(0x20)
    0xf9c: MSTORE vf92(0x40), vf99
    0xf9d: vf9d(0x0) = CONST 
    0xfa0: MSTORE vf95, vf9d(0x0)
    0xfa1: vfa1(0x4263) = CONST 
    0xfa4: JUMP vfa1(0x4263)

    Begin block 0x4263
    prev=[0xf91], succ=[0x35c0x33f]
    =================================
    0x4267: JUMP v340(0x35c)

}

function 0x34fd(0x34fdarg0x0, 0x34fdarg0x1, 0x34fdarg0x2, 0x34fdarg0x3, 0x34fdarg0x4, 0x34fdarg0x5, 0x34fdarg0x6) private {
    Begin block 0x34fd
    prev=[], succ=[0x3684B0x34fd]
    =================================
    0x34fe: v34fe(0x350f) = CONST 
    0x3502: v3502(0x1) = CONST 
    0x3504: v3504(0x1) = CONST 
    0x3506: v3506(0xa0) = CONST 
    0x3508: v3508(0x10000000000000000000000000000000000000000) = SHL v3506(0xa0), v3504(0x1)
    0x3509: v3509(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3508(0x10000000000000000000000000000000000000000), v3502(0x1)
    0x350a: v350a = AND v3509(0xffffffffffffffffffffffffffffffffffffffff), v34fdarg3
    0x350b: v350b(0x3684) = CONST 
    0x350e: JUMP v350b(0x3684)

    Begin block 0x3684B0x34fd
    prev=[0x34fd], succ=[0x350f]
    =================================
    0x3685S0x34fd: v3685V34fd = EXTCODESIZE v350a
    0x3686S0x34fd: v3686V34fd = ISZERO v3685V34fd
    0x3687S0x34fd: v3687V34fd = ISZERO v3686V34fd
    0x3689S0x34fd: JUMP v34fe(0x350f)

    Begin block 0x350f
    prev=[0x3684B0x34fd], succ=[0x4505, 0x3515]
    =================================
    0x3510: v3510 = ISZERO v3687V34fd
    0x3511: v3511(0x4505) = CONST 
    0x3514: JUMPI v3511(0x4505), v3510

    Begin block 0x4505
    prev=[0x350f], succ=[]
    =================================
    0x450c: RETURNPRIVATE v34fdarg6

    Begin block 0x3515
    prev=[0x350f], succ=[0x3586]
    =================================
    0x3516: v3516(0x1) = CONST 
    0x3518: v3518(0x1) = CONST 
    0x351a: v351a(0xa0) = CONST 
    0x351c: v351c(0x10000000000000000000000000000000000000000) = SHL v351a(0xa0), v3518(0x1)
    0x351d: v351d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v351c(0x10000000000000000000000000000000000000000), v3516(0x1)
    0x351e: v351e = AND v351d(0xffffffffffffffffffffffffffffffffffffffff), v34fdarg3
    0x351f: v351f(0xf23a6e61) = CONST 
    0x3529: v3529(0x40) = CONST 
    0x352b: v352b = MLOAD v3529(0x40)
    0x352d: v352d(0xffffffff) = CONST 
    0x3532: v3532(0xf23a6e61) = AND v352d(0xffffffff), v351f(0xf23a6e61)
    0x3533: v3533(0xe0) = CONST 
    0x3535: v3535(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v3533(0xe0), v3532(0xf23a6e61)
    0x3537: MSTORE v352b, v3535(0xf23a6e6100000000000000000000000000000000000000000000000000000000)
    0x3538: v3538(0x4) = CONST 
    0x353a: v353a = ADD v3538(0x4), v352b
    0x353d: v353d(0x1) = CONST 
    0x353f: v353f(0x1) = CONST 
    0x3541: v3541(0xa0) = CONST 
    0x3543: v3543(0x10000000000000000000000000000000000000000) = SHL v3541(0xa0), v353f(0x1)
    0x3544: v3544(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3543(0x10000000000000000000000000000000000000000), v353d(0x1)
    0x3545: v3545 = AND v3544(0xffffffffffffffffffffffffffffffffffffffff), v34fdarg5
    0x3547: MSTORE v353a, v3545
    0x3548: v3548(0x20) = CONST 
    0x354a: v354a = ADD v3548(0x20), v353a
    0x354c: v354c(0x1) = CONST 
    0x354e: v354e(0x1) = CONST 
    0x3550: v3550(0xa0) = CONST 
    0x3552: v3552(0x10000000000000000000000000000000000000000) = SHL v3550(0xa0), v354e(0x1)
    0x3553: v3553(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3552(0x10000000000000000000000000000000000000000), v354c(0x1)
    0x3554: v3554 = AND v3553(0xffffffffffffffffffffffffffffffffffffffff), v34fdarg4
    0x3556: MSTORE v354a, v3554
    0x3557: v3557(0x20) = CONST 
    0x3559: v3559 = ADD v3557(0x20), v354a
    0x355c: MSTORE v3559, v34fdarg2
    0x355d: v355d(0x20) = CONST 
    0x355f: v355f = ADD v355d(0x20), v3559
    0x3562: MSTORE v355f, v34fdarg1
    0x3563: v3563(0x20) = CONST 
    0x3565: v3565 = ADD v3563(0x20), v355f
    0x3567: v3567(0x20) = CONST 
    0x3569: v3569 = ADD v3567(0x20), v3565
    0x356c: v356c(0xa0) = SUB v3569, v353a
    0x356e: MSTORE v3565, v356c(0xa0)
    0x3572: v3572 = MLOAD v34fdarg0
    0x3574: MSTORE v3569, v3572
    0x3575: v3575(0x20) = CONST 
    0x3577: v3577 = ADD v3575(0x20), v3569
    0x357b: v357b = MLOAD v34fdarg0
    0x357d: v357d(0x20) = CONST 
    0x357f: v357f = ADD v357d(0x20), v34fdarg0
    0x3584: v3584(0x0) = CONST 

    Begin block 0x3586
    prev=[0x3515, 0x358f], succ=[0x359e, 0x358f]
    =================================
    0x3586_0x0: v3586_0 = PHI v3584(0x0), v3599
    0x3589: v3589 = LT v3586_0, v357b
    0x358a: v358a = ISZERO v3589
    0x358b: v358b(0x359e) = CONST 
    0x358e: JUMPI v358b(0x359e), v358a

    Begin block 0x359e
    prev=[0x3586], succ=[0x35cb, 0x35b2]
    =================================
    0x35a7: v35a7 = ADD v357b, v3577
    0x35a9: v35a9(0x1f) = CONST 
    0x35ab: v35ab = AND v35a9(0x1f), v357b
    0x35ad: v35ad = ISZERO v35ab
    0x35ae: v35ae(0x35cb) = CONST 
    0x35b1: JUMPI v35ae(0x35cb), v35ad

    Begin block 0x35cb
    prev=[0x359e, 0x35b2], succ=[0x35ea, 0x35ee]
    =================================
    0x35cb_0x1: v35cb_1 = PHI v35a7, v35c8
    0x35d5: v35d5(0x20) = CONST 
    0x35d7: v35d7(0x40) = CONST 
    0x35d9: v35d9 = MLOAD v35d7(0x40)
    0x35dc: v35dc = SUB v35cb_1, v35d9
    0x35de: v35de(0x0) = CONST 
    0x35e2: v35e2 = EXTCODESIZE v351e
    0x35e3: v35e3 = ISZERO v35e2
    0x35e5: v35e5 = ISZERO v35e3
    0x35e6: v35e6(0x35ee) = CONST 
    0x35e9: JUMPI v35e6(0x35ee), v35e5

    Begin block 0x35ea
    prev=[0x35cb], succ=[]
    =================================
    0x35ea: v35ea(0x0) = CONST 
    0x35ed: REVERT v35ea(0x0), v35ea(0x0)

    Begin block 0x35ee
    prev=[0x35cb], succ=[0x3613, 0x35fc]
    =================================
    0x35f0: v35f0 = GAS 
    0x35f1: v35f1 = CALL v35f0, v351e, v35de(0x0), v35d9, v35dc, v35d9, v35d5(0x20)
    0x35f7: v35f7 = ISZERO v35f1
    0x35f8: v35f8(0x3613) = CONST 
    0x35fb: JUMPI v35f8(0x3613), v35f7

    Begin block 0x3613
    prev=[0x35ee, 0x360e], succ=[0x3618, 0x361f]
    =================================
    0x3613_0x0: v3613_0 = PHI v35f1, v3611(0x1)
    0x3614: v3614(0x361f) = CONST 
    0x3617: JUMPI v3614(0x361f), v3613_0

    Begin block 0x3618
    prev=[0x3613], succ=[0x299b0x34fd]
    =================================
    0x3618: v3618(0x299b) = CONST 
    0x361b: v361b(0x3969) = CONST 
    0x361e: v361e_0 = CALLPRIVATE v361b(0x3969), v3618(0x299b)

    Begin block 0x299b0x34fd
    prev=[0x3618], succ=[0x29a10x34fd, 0x29a60x34fd]
    =================================
    0x299d0x34fd: v34fd299d(0x29a6) = CONST 
    0x29a00x34fd: JUMPI v34fd299d(0x29a6), v361e_0

    Begin block 0x29a10x34fd
    prev=[0x299b0x34fd], succ=[0x2a2b0x34fd]
    =================================
    0x29a20x34fd: v34fd29a2(0x2a2b) = CONST 
    0x29a50x34fd: JUMP v34fd29a2(0x2a2b)

    Begin block 0x2a2b0x34fd
    prev=[0x29a10x34fd], succ=[]
    =================================
    0x2a2c0x34fd: v34fd2a2c(0x40) = CONST 
    0x2a2e0x34fd: v34fd2a2e = MLOAD v34fd2a2c(0x40)
    0x2a2f0x34fd: v34fd2a2f(0x461bcd) = CONST 
    0x2a330x34fd: v34fd2a33(0xe5) = CONST 
    0x2a350x34fd: v34fd2a35(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v34fd2a33(0xe5), v34fd2a2f(0x461bcd)
    0x2a370x34fd: MSTORE v34fd2a2e, v34fd2a35(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a380x34fd: v34fd2a38(0x4) = CONST 
    0x2a3a0x34fd: v34fd2a3a = ADD v34fd2a38(0x4), v34fd2a2e
    0x2a3d0x34fd: v34fd2a3d(0x20) = CONST 
    0x2a3f0x34fd: v34fd2a3f = ADD v34fd2a3d(0x20), v34fd2a3a
    0x2a420x34fd: v34fd2a42(0x20) = SUB v34fd2a3f, v34fd2a3a
    0x2a440x34fd: MSTORE v34fd2a3a, v34fd2a42(0x20)
    0x2a450x34fd: v34fd2a45(0x2b) = CONST 
    0x2a480x34fd: MSTORE v34fd2a3f, v34fd2a45(0x2b)
    0x2a490x34fd: v34fd2a49(0x20) = CONST 
    0x2a4b0x34fd: v34fd2a4b = ADD v34fd2a49(0x20), v34fd2a3f
    0x2a4d0x34fd: v34fd2a4d(0x3a33) = CONST 
    0x2a500x34fd: v34fd2a50(0x2b) = CONST 
    0x2a530x34fd: CODECOPY v34fd2a4b, v34fd2a4d(0x3a33), v34fd2a50(0x2b)
    0x2a540x34fd: v34fd2a54(0x40) = CONST 
    0x2a560x34fd: v34fd2a56 = ADD v34fd2a54(0x40), v34fd2a4b
    0x2a5a0x34fd: v34fd2a5a(0x40) = CONST 
    0x2a5c0x34fd: v34fd2a5c = MLOAD v34fd2a5a(0x40)
    0x2a5f0x34fd: v34fd2a5f(0x84) = SUB v34fd2a56, v34fd2a5c
    0x2a610x34fd: REVERT v34fd2a5c, v34fd2a5f(0x84)

    Begin block 0x29a60x34fd
    prev=[0x299b0x34fd], succ=[0x29d80x34fd]
    =================================
    0x29a80x34fd: v34fd29a8(0x40) = CONST 
    0x29aa0x34fd: v34fd29aa = MLOAD v34fd29a8(0x40)
    0x29ab0x34fd: v34fd29ab(0x461bcd) = CONST 
    0x29af0x34fd: v34fd29af(0xe5) = CONST 
    0x29b10x34fd: v34fd29b1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v34fd29af(0xe5), v34fd29ab(0x461bcd)
    0x29b30x34fd: MSTORE v34fd29aa, v34fd29b1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29b40x34fd: v34fd29b4(0x4) = CONST 
    0x29b60x34fd: v34fd29b6 = ADD v34fd29b4(0x4), v34fd29aa
    0x29b90x34fd: v34fd29b9(0x20) = CONST 
    0x29bb0x34fd: v34fd29bb = ADD v34fd29b9(0x20), v34fd29b6
    0x29be0x34fd: v34fd29be(0x20) = SUB v34fd29bb, v34fd29b6
    0x29c00x34fd: MSTORE v34fd29b6, v34fd29be(0x20)
    0x29c40x34fd: v34fd29c4 = MLOAD v361e_0
    0x29c60x34fd: MSTORE v34fd29bb, v34fd29c4
    0x29c70x34fd: v34fd29c7(0x20) = CONST 
    0x29c90x34fd: v34fd29c9 = ADD v34fd29c7(0x20), v34fd29bb
    0x29cd0x34fd: v34fd29cd = MLOAD v361e_0
    0x29cf0x34fd: v34fd29cf(0x20) = CONST 
    0x29d10x34fd: v34fd29d1 = ADD v34fd29cf(0x20), v361e_0
    0x29d60x34fd: v34fd29d6(0x0) = CONST 

    Begin block 0x29d80x34fd
    prev=[0x29e10x34fd, 0x29a60x34fd], succ=[0x29f00x34fd, 0x29e10x34fd]
    =================================
    0x29d80x34fd_0x0: v29d834fd_0 = PHI v34fd29eb, v34fd29d6(0x0)
    0x29db0x34fd: v34fd29db = LT v29d834fd_0, v34fd29cd
    0x29dc0x34fd: v34fd29dc = ISZERO v34fd29db
    0x29dd0x34fd: v34fd29dd(0x29f0) = CONST 
    0x29e00x34fd: JUMPI v34fd29dd(0x29f0), v34fd29dc

    Begin block 0x29f00x34fd
    prev=[0x29d80x34fd], succ=[0x2a1d0x34fd, 0x2a040x34fd]
    =================================
    0x29f90x34fd: v34fd29f9 = ADD v34fd29cd, v34fd29c9
    0x29fb0x34fd: v34fd29fb(0x1f) = CONST 
    0x29fd0x34fd: v34fd29fd = AND v34fd29fb(0x1f), v34fd29cd
    0x29ff0x34fd: v34fd29ff = ISZERO v34fd29fd
    0x2a000x34fd: v34fd2a00(0x2a1d) = CONST 
    0x2a030x34fd: JUMPI v34fd2a00(0x2a1d), v34fd29ff

    Begin block 0x2a1d0x34fd
    prev=[0x29f00x34fd, 0x2a040x34fd], succ=[]
    =================================
    0x2a1d0x34fd_0x1: v2a1d34fd_1 = PHI v34fd2a1a, v34fd29f9
    0x2a230x34fd: v34fd2a23(0x40) = CONST 
    0x2a250x34fd: v34fd2a25 = MLOAD v34fd2a23(0x40)
    0x2a280x34fd: v34fd2a28 = SUB v2a1d34fd_1, v34fd2a25
    0x2a2a0x34fd: REVERT v34fd2a25, v34fd2a28

    Begin block 0x2a040x34fd
    prev=[0x29f00x34fd], succ=[0x2a1d0x34fd]
    =================================
    0x2a060x34fd: v34fd2a06 = SUB v34fd29f9, v34fd29fd
    0x2a080x34fd: v34fd2a08 = MLOAD v34fd2a06
    0x2a090x34fd: v34fd2a09(0x1) = CONST 
    0x2a0c0x34fd: v34fd2a0c(0x20) = CONST 
    0x2a0e0x34fd: v34fd2a0e = SUB v34fd2a0c(0x20), v34fd29fd
    0x2a0f0x34fd: v34fd2a0f(0x100) = CONST 
    0x2a120x34fd: v34fd2a12 = EXP v34fd2a0f(0x100), v34fd2a0e
    0x2a130x34fd: v34fd2a13 = SUB v34fd2a12, v34fd2a09(0x1)
    0x2a140x34fd: v34fd2a14 = NOT v34fd2a13
    0x2a150x34fd: v34fd2a15 = AND v34fd2a14, v34fd2a08
    0x2a170x34fd: MSTORE v34fd2a06, v34fd2a15
    0x2a180x34fd: v34fd2a18(0x20) = CONST 
    0x2a1a0x34fd: v34fd2a1a = ADD v34fd2a18(0x20), v34fd2a06

    Begin block 0x29e10x34fd
    prev=[0x29d80x34fd], succ=[0x29d80x34fd]
    =================================
    0x29e10x34fd_0x0: v29e134fd_0 = PHI v34fd29eb, v34fd29d6(0x0)
    0x29e30x34fd: v34fd29e3 = ADD v29e134fd_0, v34fd29d1
    0x29e40x34fd: v34fd29e4 = MLOAD v34fd29e3
    0x29e70x34fd: v34fd29e7 = ADD v29e134fd_0, v34fd29c9
    0x29e80x34fd: MSTORE v34fd29e7, v34fd29e4
    0x29e90x34fd: v34fd29e9(0x20) = CONST 
    0x29eb0x34fd: v34fd29eb = ADD v34fd29e9(0x20), v29e134fd_0
    0x29ec0x34fd: v34fd29ec(0x29d8) = CONST 
    0x29ef0x34fd: JUMP v34fd29ec(0x29d8)

    Begin block 0x361f
    prev=[0x3613], succ=[0x3638, 0x2ac70x34fd]
    =================================
    0x361f_0x0: v361f_0 = PHI v3610, v34fdarg0
    0x3620: v3620(0x1) = CONST 
    0x3622: v3622(0x1) = CONST 
    0x3624: v3624(0xe0) = CONST 
    0x3626: v3626(0x100000000000000000000000000000000000000000000000000000000) = SHL v3624(0xe0), v3622(0x1)
    0x3627: v3627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v3626(0x100000000000000000000000000000000000000000000000000000000), v3620(0x1)
    0x3628: v3628(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v3627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x362a: v362a = AND v361f_0, v3628(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x362b: v362b(0xf23a6e61) = CONST 
    0x3630: v3630(0xe0) = CONST 
    0x3632: v3632(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v3630(0xe0), v362b(0xf23a6e61)
    0x3633: v3633 = EQ v3632(0xf23a6e6100000000000000000000000000000000000000000000000000000000), v362a
    0x3634: v3634(0x2ac7) = CONST 
    0x3637: JUMPI v3634(0x2ac7), v3633

    Begin block 0x3638
    prev=[0x361f], succ=[]
    =================================
    0x3638: v3638(0x40) = CONST 
    0x363b: v363b = MLOAD v3638(0x40)
    0x363c: v363c(0x461bcd) = CONST 
    0x3640: v3640(0xe5) = CONST 
    0x3642: v3642(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3640(0xe5), v363c(0x461bcd)
    0x3644: MSTORE v363b, v3642(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3645: v3645(0x20) = CONST 
    0x3647: v3647(0x4) = CONST 
    0x364a: v364a = ADD v363b, v3647(0x4)
    0x364b: MSTORE v364a, v3645(0x20)
    0x364c: v364c(0x1f) = CONST 
    0x364e: v364e(0x24) = CONST 
    0x3651: v3651 = ADD v363b, v364e(0x24)
    0x3652: MSTORE v3651, v364c(0x1f)
    0x3653: v3653(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x3674: v3674(0x44) = CONST 
    0x3677: v3677 = ADD v363b, v3674(0x44)
    0x3678: MSTORE v3677, v3653(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x367a: v367a = MLOAD v3638(0x40)
    0x367e: v367e(0x0) = SUB v363b, v367a
    0x367f: v367f(0x64) = CONST 
    0x3681: v3681(0x64) = ADD v367f(0x64), v367e(0x0)
    0x3683: REVERT v367a, v3681(0x64)

    Begin block 0x2ac70x34fd
    prev=[0x361f], succ=[0x2ac90x34fd]
    =================================

    Begin block 0x2ac90x34fd
    prev=[0x2ac70x34fd], succ=[]
    =================================
    0x2ad00x34fd: RETURNPRIVATE v34fdarg6

    Begin block 0x35fc
    prev=[0x35ee], succ=[0x360a, 0x360e]
    =================================
    0x35fd: v35fd(0x40) = CONST 
    0x35ff: v35ff = MLOAD v35fd(0x40)
    0x3600: v3600 = RETURNDATASIZE 
    0x3601: v3601(0x20) = CONST 
    0x3604: v3604 = LT v3600, v3601(0x20)
    0x3605: v3605 = ISZERO v3604
    0x3606: v3606(0x360e) = CONST 
    0x3609: JUMPI v3606(0x360e), v3605

    Begin block 0x360a
    prev=[0x35fc], succ=[]
    =================================
    0x360a: v360a(0x0) = CONST 
    0x360d: REVERT v360a(0x0), v360a(0x0)

    Begin block 0x360e
    prev=[0x35fc], succ=[0x3613]
    =================================
    0x3610: v3610 = MLOAD v35ff
    0x3611: v3611(0x1) = CONST 

    Begin block 0x35b2
    prev=[0x359e], succ=[0x35cb]
    =================================
    0x35b4: v35b4 = SUB v35a7, v35ab
    0x35b6: v35b6 = MLOAD v35b4
    0x35b7: v35b7(0x1) = CONST 
    0x35ba: v35ba(0x20) = CONST 
    0x35bc: v35bc = SUB v35ba(0x20), v35ab
    0x35bd: v35bd(0x100) = CONST 
    0x35c0: v35c0 = EXP v35bd(0x100), v35bc
    0x35c1: v35c1 = SUB v35c0, v35b7(0x1)
    0x35c2: v35c2 = NOT v35c1
    0x35c3: v35c3 = AND v35c2, v35b6
    0x35c5: MSTORE v35b4, v35c3
    0x35c6: v35c6(0x20) = CONST 
    0x35c8: v35c8 = ADD v35c6(0x20), v35b4

    Begin block 0x358f
    prev=[0x3586], succ=[0x3586]
    =================================
    0x358f_0x0: v358f_0 = PHI v3584(0x0), v3599
    0x3591: v3591 = ADD v358f_0, v357f
    0x3592: v3592 = MLOAD v3591
    0x3595: v3595 = ADD v358f_0, v3577
    0x3596: MSTORE v3595, v3592
    0x3597: v3597(0x20) = CONST 
    0x3599: v3599 = ADD v3597(0x20), v358f_0
    0x359a: v359a(0x3586) = CONST 
    0x359d: JUMP v359a(0x3586)

}

function 0x368a(0x368aarg0x0, 0x368aarg0x1) private {
    Begin block 0x368a
    prev=[], succ=[0x369d]
    =================================
    0x368b: v368b(0x0) = CONST 
    0x368d: v368d(0x369d) = CONST 
    0x3691: v3691(0x1ffc9a7) = CONST 
    0x3696: v3696(0xe0) = CONST 
    0x3698: v3698(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v3696(0xe0), v3691(0x1ffc9a7)
    0x3699: v3699(0x36bd) = CONST 
    0x369c: v369c_0 = CALLPRIVATE v3699(0x36bd), v3698(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v368aarg0, v368d(0x369d)

    Begin block 0x369d
    prev=[0x368a], succ=[0x452c, 0x36a4]
    =================================
    0x369f: v369f = ISZERO v369c_0
    0x36a0: v36a0(0x452c) = CONST 
    0x36a3: JUMPI v36a0(0x452c), v369f

    Begin block 0x452c
    prev=[0x369d], succ=[]
    =================================
    0x4531: RETURNPRIVATE v368aarg1, v369c_0

    Begin block 0x36a4
    prev=[0x369d], succ=[0x36b6]
    =================================
    0x36a5: v36a5(0x36b6) = CONST 
    0x36a9: v36a9(0x1) = CONST 
    0x36ab: v36ab(0x1) = CONST 
    0x36ad: v36ad(0xe0) = CONST 
    0x36af: v36af(0x100000000000000000000000000000000000000000000000000000000) = SHL v36ad(0xe0), v36ab(0x1)
    0x36b0: v36b0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v36af(0x100000000000000000000000000000000000000000000000000000000), v36a9(0x1)
    0x36b1: v36b1(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v36b0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x36b2: v36b2(0x36bd) = CONST 
    0x36b5: v36b5_0 = CALLPRIVATE v36b2(0x36bd), v36b1(0xffffffff00000000000000000000000000000000000000000000000000000000), v368aarg0, v36a5(0x36b6)

    Begin block 0x36b6
    prev=[0x36a4], succ=[]
    =================================
    0x36b7: v36b7 = ISZERO v36b5_0
    0x36bc: RETURNPRIVATE v368aarg1, v36b7

}

function 0x36bd(0x36bdarg0x0, 0x36bdarg0x1, 0x36bdarg0x2) private {
    Begin block 0x36bd
    prev=[], succ=[0x36e0B0x36bd]
    =================================
    0x36be: v36be(0x0) = CONST 
    0x36c1: v36c1(0x0) = CONST 
    0x36c3: v36c3(0x36cc) = CONST 
    0x36c8: v36c8(0x36e0) = CONST 
    0x36cb: JUMP v36c8(0x36e0)

    Begin block 0x36e0B0x36bd
    prev=[0x36bd], succ=[0x3748B0x36bd]
    =================================
    0x36e1S0x36bd: v36e1V36bd(0x40) = CONST 
    0x36e4S0x36bd: v36e4V36bd = MLOAD v36e1V36bd(0x40)
    0x36e5S0x36bd: v36e5V36bd(0x1) = CONST 
    0x36e7S0x36bd: v36e7V36bd(0x1) = CONST 
    0x36e9S0x36bd: v36e9V36bd(0xe0) = CONST 
    0x36ebS0x36bd: v36ebV36bd(0x100000000000000000000000000000000000000000000000000000000) = SHL v36e9V36bd(0xe0), v36e7V36bd(0x1)
    0x36ecS0x36bd: v36ecV36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v36ebV36bd(0x100000000000000000000000000000000000000000000000000000000), v36e5V36bd(0x1)
    0x36edS0x36bd: v36edV36bd(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v36ecV36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x36efS0x36bd: v36efV36bd = AND v36bdarg0, v36edV36bd(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x36f0S0x36bd: v36f0V36bd(0x24) = CONST 
    0x36f4S0x36bd: v36f4V36bd = ADD v36e4V36bd, v36f0V36bd(0x24)
    0x36f8S0x36bd: MSTORE v36f4V36bd, v36efV36bd
    0x36faS0x36bd: v36faV36bd = MLOAD v36e1V36bd(0x40)
    0x36fdS0x36bd: v36fdV36bd(0x0) = SUB v36e4V36bd, v36faV36bd
    0x3700S0x36bd: v3700V36bd(0x24) = ADD v36f0V36bd(0x24), v36fdV36bd(0x0)
    0x3702S0x36bd: MSTORE v36faV36bd, v3700V36bd(0x24)
    0x3703S0x36bd: v3703V36bd(0x44) = CONST 
    0x3707S0x36bd: v3707V36bd = ADD v36e4V36bd, v3703V36bd(0x44)
    0x3709S0x36bd: MSTORE v36e1V36bd(0x40), v3707V36bd
    0x370aS0x36bd: v370aV36bd(0x20) = CONST 
    0x370dS0x36bd: v370dV36bd = ADD v36faV36bd, v370aV36bd(0x20)
    0x370fS0x36bd: v370fV36bd = MLOAD v370dV36bd
    0x3710S0x36bd: v3710V36bd(0x1) = CONST 
    0x3712S0x36bd: v3712V36bd(0x1) = CONST 
    0x3714S0x36bd: v3714V36bd(0xe0) = CONST 
    0x3716S0x36bd: v3716V36bd(0x100000000000000000000000000000000000000000000000000000000) = SHL v3714V36bd(0xe0), v3712V36bd(0x1)
    0x3717S0x36bd: v3717V36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v3716V36bd(0x100000000000000000000000000000000000000000000000000000000), v3710V36bd(0x1)
    0x3718S0x36bd: v3718V36bd = AND v3717V36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v370fV36bd
    0x3719S0x36bd: v3719V36bd(0x1ffc9a7) = CONST 
    0x371eS0x36bd: v371eV36bd(0xe0) = CONST 
    0x3720S0x36bd: v3720V36bd(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v371eV36bd(0xe0), v3719V36bd(0x1ffc9a7)
    0x3721S0x36bd: v3721V36bd = OR v3720V36bd(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v3718V36bd
    0x3723S0x36bd: MSTORE v370dV36bd, v3721V36bd
    0x3725S0x36bd: v3725V36bd = MLOAD v36e1V36bd(0x40)
    0x3727S0x36bd: v3727V36bd(0x24) = MLOAD v36faV36bd
    0x3728S0x36bd: v3728V36bd(0x0) = CONST 
    0x3732S0x36bd: v3732V36bd(0x1) = CONST 
    0x3734S0x36bd: v3734V36bd(0x1) = CONST 
    0x3736S0x36bd: v3736V36bd(0xa0) = CONST 
    0x3738S0x36bd: v3738V36bd(0x10000000000000000000000000000000000000000) = SHL v3736V36bd(0xa0), v3734V36bd(0x1)
    0x3739S0x36bd: v3739V36bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3738V36bd(0x10000000000000000000000000000000000000000), v3732V36bd(0x1)
    0x373bS0x36bd: v373bV36bd = AND v36bdarg1, v3739V36bd(0xffffffffffffffffffffffffffffffffffffffff)
    0x373dS0x36bd: v373dV36bd(0x7530) = CONST 

    Begin block 0x3748B0x36bd
    prev=[0x36e0B0x36bd, 0x3751B0x36bd], succ=[0x3767B0x36bd, 0x3751B0x36bd]
    =================================
    0x3748_0x2S0x36bd: v3748_2V36bd = PHI v3727V36bd(0x24), v375aV36bd
    0x3749S0x36bd: v3749V36bd(0x20) = CONST 
    0x374cS0x36bd: v374cV36bd = LT v3748_2V36bd, v3749V36bd(0x20)
    0x374dS0x36bd: v374dV36bd(0x3767) = CONST 
    0x3750S0x36bd: JUMPI v374dV36bd(0x3767), v374cV36bd

    Begin block 0x3767B0x36bd
    prev=[0x3748B0x36bd], succ=[0x37a7B0x36bd, 0x37c8B0x36bd]
    =================================
    0x3767_0x0S0x36bd: v3767_0V36bd = PHI v370dV36bd, v3762V36bd
    0x3767_0x1S0x36bd: v3767_1V36bd = PHI v3725V36bd, v3760V36bd
    0x3767_0x2S0x36bd: v3767_2V36bd = PHI v3727V36bd(0x24), v375aV36bd
    0x3768S0x36bd: v3768V36bd(0x1) = CONST 
    0x376bS0x36bd: v376bV36bd(0x20) = CONST 
    0x376dS0x36bd: v376dV36bd = SUB v376bV36bd(0x20), v3767_2V36bd
    0x376eS0x36bd: v376eV36bd(0x100) = CONST 
    0x3771S0x36bd: v3771V36bd = EXP v376eV36bd(0x100), v376dV36bd
    0x3772S0x36bd: v3772V36bd = SUB v3771V36bd, v3768V36bd(0x1)
    0x3774S0x36bd: v3774V36bd = NOT v3772V36bd
    0x3776S0x36bd: v3776V36bd = MLOAD v3767_0V36bd
    0x3777S0x36bd: v3777V36bd = AND v3776V36bd, v3774V36bd
    0x377aS0x36bd: v377aV36bd = MLOAD v3767_1V36bd
    0x377bS0x36bd: v377bV36bd = AND v377aV36bd, v3772V36bd
    0x377eS0x36bd: v377eV36bd = OR v3777V36bd, v377bV36bd
    0x3780S0x36bd: MSTORE v3767_1V36bd, v377eV36bd
    0x3789S0x36bd: v3789V36bd = ADD v3727V36bd(0x24), v3725V36bd
    0x378dS0x36bd: v378dV36bd(0x0) = CONST 
    0x378fS0x36bd: v378fV36bd(0x40) = CONST 
    0x3791S0x36bd: v3791V36bd = MLOAD v378fV36bd(0x40)
    0x3794S0x36bd: v3794V36bd(0x24) = SUB v3789V36bd, v3791V36bd
    0x3798S0x36bd: v3798V36bd = STATICCALL v373dV36bd(0x7530), v373bV36bd, v3791V36bd, v3794V36bd(0x24), v3791V36bd, v378dV36bd(0x0)
    0x379dS0x36bd: v379dV36bd = RETURNDATASIZE 
    0x379fS0x36bd: v379fV36bd(0x0) = CONST 
    0x37a2S0x36bd: v37a2V36bd = EQ v379dV36bd, v379fV36bd(0x0)
    0x37a3S0x36bd: v37a3V36bd(0x37c8) = CONST 
    0x37a6S0x36bd: JUMPI v37a3V36bd(0x37c8), v37a2V36bd

    Begin block 0x37a7B0x36bd
    prev=[0x3767B0x36bd], succ=[0x37cdB0x36bd]
    =================================
    0x37a7S0x36bd: v37a7V36bd(0x40) = CONST 
    0x37a9S0x36bd: v37a9V36bd = MLOAD v37a7V36bd(0x40)
    0x37acS0x36bd: v37acV36bd(0x1f) = CONST 
    0x37aeS0x36bd: v37aeV36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v37acV36bd(0x1f)
    0x37afS0x36bd: v37afV36bd(0x3f) = CONST 
    0x37b1S0x36bd: v37b1V36bd = RETURNDATASIZE 
    0x37b2S0x36bd: v37b2V36bd = ADD v37b1V36bd, v37afV36bd(0x3f)
    0x37b3S0x36bd: v37b3V36bd = AND v37b2V36bd, v37aeV36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x37b5S0x36bd: v37b5V36bd = ADD v37a9V36bd, v37b3V36bd
    0x37b6S0x36bd: v37b6V36bd(0x40) = CONST 
    0x37b8S0x36bd: MSTORE v37b6V36bd(0x40), v37b5V36bd
    0x37b9S0x36bd: v37b9V36bd = RETURNDATASIZE 
    0x37bbS0x36bd: MSTORE v37a9V36bd, v37b9V36bd
    0x37bcS0x36bd: v37bcV36bd = RETURNDATASIZE 
    0x37bdS0x36bd: v37bdV36bd(0x0) = CONST 
    0x37bfS0x36bd: v37bfV36bd(0x20) = CONST 
    0x37c2S0x36bd: v37c2V36bd = ADD v37a9V36bd, v37bfV36bd(0x20)
    0x37c3S0x36bd: RETURNDATACOPY v37c2V36bd, v37bdV36bd(0x0), v37bcV36bd
    0x37c4S0x36bd: v37c4V36bd(0x37cd) = CONST 
    0x37c7S0x36bd: JUMP v37c4V36bd(0x37cd)

    Begin block 0x37cdB0x36bd
    prev=[0x37a7B0x36bd, 0x37c8B0x36bd], succ=[0x37ddB0x36bd, 0x37ebB0x36bd]
    =================================
    0x37cd_0x1S0x36bd: v37cd_1V36bd = PHI v37a9V36bd, v37c9V36bd(0x60)
    0x37d3S0x36bd: v37d3V36bd(0x20) = CONST 
    0x37d6S0x36bd: v37d6V36bd = MLOAD v37cd_1V36bd
    0x37d7S0x36bd: v37d7V36bd = LT v37d6V36bd, v37d3V36bd(0x20)
    0x37d8S0x36bd: v37d8V36bd = ISZERO v37d7V36bd
    0x37d9S0x36bd: v37d9V36bd(0x37eb) = CONST 
    0x37dcS0x36bd: JUMPI v37d9V36bd(0x37eb), v37d8V36bd

    Begin block 0x37ddB0x36bd
    prev=[0x37cdB0x36bd], succ=[0x380cB0x36bd]
    =================================
    0x37ddS0x36bd: v37ddV36bd(0x0) = CONST 
    0x37e7S0x36bd: v37e7V36bd(0x380c) = CONST 
    0x37eaS0x36bd: JUMP v37e7V36bd(0x380c)

    Begin block 0x380cB0x36bd
    prev=[0x37ddB0x36bd, 0x3801B0x36bd], succ=[0x36cc]
    =================================
    0x380c_0x0S0x36bd: v380c_0V36bd = PHI v37ddV36bd(0x0), v3803V36bd
    0x380c_0x1S0x36bd: v380c_1V36bd = PHI v37ddV36bd(0x0), v3798V36bd
    0x3812S0x36bd: JUMP v36c3(0x36cc)

    Begin block 0x36cc
    prev=[0x380cB0x36bd], succ=[0x4551, 0x36d8]
    =================================
    0x36d3: v36d3 = ISZERO v380c_1V36bd
    0x36d4: v36d4(0x4551) = CONST 
    0x36d7: JUMPI v36d4(0x4551), v36d3

    Begin block 0x4551
    prev=[0x36cc], succ=[]
    =================================
    0x4559: RETURNPRIVATE v36bdarg2, v380c_1V36bd

    Begin block 0x36d8
    prev=[0x36cc], succ=[]
    =================================
    0x36df: RETURNPRIVATE v36bdarg2, v380c_0V36bd

    Begin block 0x37ebB0x36bd
    prev=[0x37cdB0x36bd], succ=[0x37fdB0x36bd, 0x3801B0x36bd]
    =================================
    0x37eb_0x0S0x36bd: v37eb_0V36bd = PHI v37a9V36bd, v37c9V36bd(0x60)
    0x37efS0x36bd: v37efV36bd(0x20) = CONST 
    0x37f1S0x36bd: v37f1V36bd = ADD v37efV36bd(0x20), v37eb_0V36bd
    0x37f3S0x36bd: v37f3V36bd = MLOAD v37eb_0V36bd
    0x37f4S0x36bd: v37f4V36bd(0x20) = CONST 
    0x37f7S0x36bd: v37f7V36bd = LT v37f3V36bd, v37f4V36bd(0x20)
    0x37f8S0x36bd: v37f8V36bd = ISZERO v37f7V36bd
    0x37f9S0x36bd: v37f9V36bd(0x3801) = CONST 
    0x37fcS0x36bd: JUMPI v37f9V36bd(0x3801), v37f8V36bd

    Begin block 0x37fdB0x36bd
    prev=[0x37ebB0x36bd], succ=[]
    =================================
    0x37fdS0x36bd: v37fdV36bd(0x0) = CONST 
    0x3800S0x36bd: REVERT v37fdV36bd(0x0), v37fdV36bd(0x0)

    Begin block 0x3801B0x36bd
    prev=[0x37ebB0x36bd], succ=[0x380cB0x36bd]
    =================================
    0x3803S0x36bd: v3803V36bd = MLOAD v37f1V36bd

    Begin block 0x37c8B0x36bd
    prev=[0x3767B0x36bd], succ=[0x37cdB0x36bd]
    =================================
    0x37c9S0x36bd: v37c9V36bd(0x60) = CONST 

    Begin block 0x3751B0x36bd
    prev=[0x3748B0x36bd], succ=[0x3748B0x36bd]
    =================================
    0x3751_0x0S0x36bd: v3751_0V36bd = PHI v370dV36bd, v3762V36bd
    0x3751_0x1S0x36bd: v3751_1V36bd = PHI v3725V36bd, v3760V36bd
    0x3751_0x2S0x36bd: v3751_2V36bd = PHI v3727V36bd(0x24), v375aV36bd
    0x3752S0x36bd: v3752V36bd = MLOAD v3751_0V36bd
    0x3754S0x36bd: MSTORE v3751_1V36bd, v3752V36bd
    0x3755S0x36bd: v3755V36bd(0x1f) = CONST 
    0x3757S0x36bd: v3757V36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3755V36bd(0x1f)
    0x375aS0x36bd: v375aV36bd = ADD v3751_2V36bd, v3757V36bd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x375cS0x36bd: v375cV36bd(0x20) = CONST 
    0x3760S0x36bd: v3760V36bd = ADD v375cV36bd(0x20), v3751_1V36bd
    0x3762S0x36bd: v3762V36bd = ADD v375cV36bd(0x20), v3751_0V36bd
    0x3763S0x36bd: v3763V36bd(0x3748) = CONST 
    0x3766S0x36bd: JUMP v3763V36bd(0x3748)

}

function 0x3969(0x3969arg0x0) private {
    Begin block 0x3969
    prev=[], succ=[0x3975, 0x3979]
    =================================
    0x396a: v396a(0x0) = CONST 
    0x396c: v396c(0x44) = CONST 
    0x396e: v396e = RETURNDATASIZE 
    0x396f: v396f = LT v396e, v396c(0x44)
    0x3970: v3970 = ISZERO v396f
    0x3971: v3971(0x3979) = CONST 
    0x3974: JUMPI v3971(0x3979), v3970

    Begin block 0x3975
    prev=[0x3969], succ=[0x45bf]
    =================================
    0x3975: v3975(0x45bf) = CONST 
    0x3978: JUMP v3975(0x45bf)

    Begin block 0x45bf
    prev=[0x3975], succ=[]
    =================================
    0x45c1: RETURNPRIVATE v3969arg0, v396a(0x0)

    Begin block 0x3979
    prev=[0x3969], succ=[0x3963]
    =================================
    0x397a: v397a(0x4) = CONST 
    0x397e: RETURNDATACOPY v396a(0x0), v396a(0x0), v397a(0x4)
    0x397f: v397f(0x8c379a0) = CONST 
    0x3984: v3984(0x398d) = CONST 
    0x3988: v3988 = MLOAD v396a(0x0)
    0x3989: v3989(0x3963) = CONST 
    0x398c: JUMP v3989(0x3963)

    Begin block 0x3963
    prev=[0x3979], succ=[0x398d]
    =================================
    0x3964: v3964(0xe0) = CONST 
    0x3966: v3966 = SHR v3964(0xe0), v3988
    0x3968: JUMP v3984(0x398d)

    Begin block 0x398d
    prev=[0x3963], succ=[0x3993, 0x3997]
    =================================
    0x398e: v398e = EQ v3966, v397f(0x8c379a0)
    0x398f: v398f(0x3997) = CONST 
    0x3992: JUMPI v398f(0x3997), v398e

    Begin block 0x3993
    prev=[0x398d], succ=[0x45e1]
    =================================
    0x3993: v3993(0x45e1) = CONST 
    0x3996: JUMP v3993(0x45e1)

    Begin block 0x45e1
    prev=[0x3993], succ=[]
    =================================
    0x45e3: RETURNPRIVATE v3969arg0, v396a(0x0)

    Begin block 0x3997
    prev=[0x398d], succ=[0x39c7, 0x39bf]
    =================================
    0x3998: v3998(0x40) = CONST 
    0x399a: v399a = MLOAD v3998(0x40)
    0x399b: v399b = RETURNDATASIZE 
    0x399c: v399c(0x3) = CONST 
    0x399e: v399e(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc) = NOT v399c(0x3)
    0x399f: v399f = ADD v399e(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc), v399b
    0x39a0: v39a0(0x4) = CONST 
    0x39a3: RETURNDATACOPY v399a, v39a0(0x4), v399f
    0x39a5: v39a5 = MLOAD v399a
    0x39a6: v39a6 = RETURNDATASIZE 
    0x39a7: v39a7(0xffffffffffffffff) = CONST 
    0x39b1: v39b1(0x24) = CONST 
    0x39b4: v39b4 = ADD v39a5, v39b1(0x24)
    0x39b5: v39b5 = GT v39b4, v39a6
    0x39b8: v39b8 = GT v39a5, v39a7(0xffffffffffffffff)
    0x39b9: v39b9 = OR v39b8, v39b5
    0x39ba: v39ba = ISZERO v39b9
    0x39bb: v39bb(0x39c7) = CONST 
    0x39be: JUMPI v39bb(0x39c7), v39ba

    Begin block 0x39c7
    prev=[0x3997], succ=[0x39e1, 0x39d9]
    =================================
    0x39ca: v39ca = ADD v399a, v39a5
    0x39ce: v39ce = MLOAD v39ca
    0x39d3: v39d3 = GT v39ce, v39a7(0xffffffffffffffff)
    0x39d4: v39d4 = ISZERO v39d3
    0x39d5: v39d5(0x39e1) = CONST 
    0x39d8: JUMPI v39d5(0x39e1), v39d4

    Begin block 0x39e1
    prev=[0x39c7], succ=[0x39f9, 0x39f2]
    =================================
    0x39e3: v39e3 = RETURNDATASIZE 
    0x39e5: v39e5 = ADD v399a, v39e3
    0x39e6: v39e6(0x20) = CONST 
    0x39ea: v39ea = ADD v39ca, v39ce
    0x39eb: v39eb = ADD v39ea, v39e6(0x20)
    0x39ec: v39ec = GT v39eb, v39e5
    0x39ed: v39ed = ISZERO v39ec
    0x39ee: v39ee(0x39f9) = CONST 
    0x39f1: JUMPI v39ee(0x39f9), v39ed

    Begin block 0x39f9
    prev=[0x39e1], succ=[]
    =================================
    0x39fa: v39fa(0x1f) = CONST 
    0x39fc: v39fc = ADD v39fa(0x1f), v39ce
    0x39fd: v39fd(0x1f) = CONST 
    0x39ff: v39ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v39fd(0x1f)
    0x3a00: v3a00 = AND v39ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v39fc
    0x3a02: v3a02 = ADD v39ca, v3a00
    0x3a03: v3a03(0x20) = CONST 
    0x3a05: v3a05 = ADD v3a03(0x20), v3a02
    0x3a06: v3a06(0x40) = CONST 
    0x3a08: MSTORE v3a06(0x40), v3a05
    0x3a0d: RETURNPRIVATE v3969arg0, v39ca

    Begin block 0x39f2
    prev=[0x39e1], succ=[0x4647]
    =================================
    0x39f5: v39f5(0x4647) = CONST 
    0x39f8: JUMP v39f5(0x4647)

    Begin block 0x4647
    prev=[0x39f2], succ=[]
    =================================
    0x4649: RETURNPRIVATE v3969arg0, v396a(0x0)

    Begin block 0x39d9
    prev=[0x39c7], succ=[0x4625]
    =================================
    0x39dd: v39dd(0x4625) = CONST 
    0x39e0: JUMP v39dd(0x4625)

    Begin block 0x4625
    prev=[0x39d9], succ=[]
    =================================
    0x4627: RETURNPRIVATE v3969arg0, v396a(0x0)

    Begin block 0x39bf
    prev=[0x3997], succ=[0x4603]
    =================================
    0x39c3: v39c3(0x4603) = CONST 
    0x39c6: JUMP v39c3(0x4603)

    Begin block 0x4603
    prev=[0x39bf], succ=[]
    =================================
    0x4605: RETURNPRIVATE v3969arg0, v396a(0x0)

}

function fallback()() public {
    Begin block 0x3c4e
    prev=[], succ=[]
    =================================
    0x3c4f: v3c4f(0x0) = CONST 
    0x3c52: REVERT v3c4f(0x0), v3c4f(0x0)

}

function initialized()() public {
    Begin block 0x3d1
    prev=[], succ=[0x1086B0x3d1]
    =================================
    0x3d2: v3d2(0x3df3) = CONST 
    0x3d5: v3d5(0x1086) = CONST 
    0x3d8: JUMP v3d5(0x1086)

    Begin block 0x1086B0x3d1
    prev=[0x3d1], succ=[0x108dB0x3d1]
    =================================
    0x1087S0x3d1: v1087V3d1(0x1) = CONST 
    0x1089S0x3d1: v1089V3d1 = SLOAD v1087V3d1(0x1)
    0x108aS0x3d1: v108aV3d1(0xff) = CONST 
    0x108cS0x3d1: v108cV3d1 = AND v108aV3d1(0xff), v1089V3d1

    Begin block 0x108dB0x3d1
    prev=[0x1086B0x3d1], succ=[0x3df3]
    =================================
    0x108fS0x3d1: JUMP v3d2(0x3df3)

    Begin block 0x3df3
    prev=[0x108dB0x3d1], succ=[]
    =================================
    0x3df4: v3df4(0x40) = CONST 
    0x3df7: v3df7 = MLOAD v3df4(0x40)
    0x3df9: v3df9 = ISZERO v108cV3d1
    0x3dfa: v3dfa = ISZERO v3df9
    0x3dfc: MSTORE v3df7, v3dfa
    0x3dfd: v3dfd = MLOAD v3df4(0x40)
    0x3e01: v3e01(0x0) = SUB v3df7, v3dfd
    0x3e02: v3e02(0x20) = CONST 
    0x3e04: v3e04(0x20) = ADD v3e02(0x20), v3e01(0x0)
    0x3e06: RETURN v3dfd, v3e04(0x20)

}

function mintQuasar(address,uint256,uint256,address,uint256)() public {
    Begin block 0x3d9
    prev=[], succ=[0x3eb, 0x3ef]
    =================================
    0x3da: v3da(0x3e26) = CONST 
    0x3dd: v3dd(0x4) = CONST 
    0x3e0: v3e0 = CALLDATASIZE 
    0x3e1: v3e1 = SUB v3e0, v3dd(0x4)
    0x3e2: v3e2(0xa0) = CONST 
    0x3e5: v3e5 = LT v3e1, v3e2(0xa0)
    0x3e6: v3e6 = ISZERO v3e5
    0x3e7: v3e7(0x3ef) = CONST 
    0x3ea: JUMPI v3e7(0x3ef), v3e6

    Begin block 0x3eb
    prev=[0x3d9], succ=[]
    =================================
    0x3eb: v3eb(0x0) = CONST 
    0x3ee: REVERT v3eb(0x0), v3eb(0x0)

    Begin block 0x3ef
    prev=[0x3d9], succ=[0x1090]
    =================================
    0x3f1: v3f1(0x1) = CONST 
    0x3f3: v3f3(0x1) = CONST 
    0x3f5: v3f5(0xa0) = CONST 
    0x3f7: v3f7(0x10000000000000000000000000000000000000000) = SHL v3f5(0xa0), v3f3(0x1)
    0x3f8: v3f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f7(0x10000000000000000000000000000000000000000), v3f1(0x1)
    0x3fa: v3fa = CALLDATALOAD v3dd(0x4)
    0x3fc: v3fc = AND v3f8(0xffffffffffffffffffffffffffffffffffffffff), v3fa
    0x3fe: v3fe(0x20) = CONST 
    0x401: v401(0x24) = ADD v3dd(0x4), v3fe(0x20)
    0x402: v402 = CALLDATALOAD v401(0x24)
    0x404: v404(0x40) = CONST 
    0x407: v407(0x44) = ADD v3dd(0x4), v404(0x40)
    0x408: v408 = CALLDATALOAD v407(0x44)
    0x40a: v40a(0x60) = CONST 
    0x40d: v40d(0x64) = ADD v3dd(0x4), v40a(0x60)
    0x40e: v40e = CALLDATALOAD v40d(0x64)
    0x411: v411 = AND v3f8(0xffffffffffffffffffffffffffffffffffffffff), v40e
    0x413: v413(0x80) = CONST 
    0x415: v415(0x84) = ADD v413(0x80), v3dd(0x4)
    0x416: v416 = CALLDATALOAD v415(0x84)
    0x417: v417(0x1090) = CONST 
    0x41a: JUMP v417(0x1090)

    Begin block 0x1090
    prev=[0x3ef], succ=[0x10a8, 0x10e5]
    =================================
    0x1091: v1091 = CALLER 
    0x1092: v1092(0x0) = CONST 
    0x1096: MSTORE v1092(0x0), v1091
    0x1097: v1097(0x5) = CONST 
    0x1099: v1099(0x20) = CONST 
    0x109b: MSTORE v1099(0x20), v1097(0x5)
    0x109c: v109c(0x40) = CONST 
    0x109f: v109f = SHA3 v1092(0x0), v109c(0x40)
    0x10a0: v10a0 = SLOAD v109f
    0x10a1: v10a1(0xff) = CONST 
    0x10a3: v10a3 = AND v10a1(0xff), v10a0
    0x10a4: v10a4(0x10e5) = CONST 
    0x10a7: JUMPI v10a4(0x10e5), v10a3

    Begin block 0x10a8
    prev=[0x1090], succ=[]
    =================================
    0x10a8: v10a8(0x40) = CONST 
    0x10ab: v10ab = MLOAD v10a8(0x40)
    0x10ac: v10ac(0x461bcd) = CONST 
    0x10b0: v10b0(0xe5) = CONST 
    0x10b2: v10b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v10b0(0xe5), v10ac(0x461bcd)
    0x10b4: MSTORE v10ab, v10b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10b5: v10b5(0x20) = CONST 
    0x10b7: v10b7(0x4) = CONST 
    0x10ba: v10ba = ADD v10ab, v10b7(0x4)
    0x10bb: MSTORE v10ba, v10b5(0x20)
    0x10bc: v10bc(0xe) = CONST 
    0x10be: v10be(0x24) = CONST 
    0x10c1: v10c1 = ADD v10ab, v10be(0x24)
    0x10c2: MSTORE v10c1, v10bc(0xe)
    0x10c3: v10c3(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x10d2: v10d2(0x91) = CONST 
    0x10d4: v10d4(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v10d2(0x91), v10c3(0x36bab9ba1031329036b4b73a32b9)
    0x10d5: v10d5(0x44) = CONST 
    0x10d8: v10d8 = ADD v10ab, v10d5(0x44)
    0x10d9: MSTORE v10d8, v10d4(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x10db: v10db = MLOAD v10a8(0x40)
    0x10df: v10df(0x0) = SUB v10ab, v10db
    0x10e0: v10e0(0x64) = CONST 
    0x10e2: v10e2(0x64) = ADD v10e0(0x64), v10df(0x0)
    0x10e4: REVERT v10db, v10e2(0x64)

    Begin block 0x10e5
    prev=[0x1090], succ=[0x2790]
    =================================
    0x10e6: v10e6(0x10f2) = CONST 
    0x10ee: v10ee(0x2790) = CONST 
    0x10f1: JUMP v10ee(0x2790)

    Begin block 0x2790
    prev=[0x10e5], succ=[0x279d]
    =================================
    0x2791: v2791(0x0) = CONST 
    0x2794: v2794(0x279d) = CONST 
    0x2799: v2799(0x2ad1) = CONST 
    0x279c: v279c_0 = CALLPRIVATE v2799(0x2ad1), v402, v3fc, v2794(0x279d)

    Begin block 0x279d
    prev=[0x2790], succ=[0x10f2]
    =================================
    0x279e: v279e(0x40) = CONST 
    0x27a1: v27a1 = MLOAD v279e(0x40)
    0x27a2: v27a2(0x60) = CONST 
    0x27a5: v27a5 = ADD v27a1, v27a2(0x60)
    0x27a7: MSTORE v279e(0x40), v27a5
    0x27a8: v27a8(0x1) = CONST 
    0x27aa: v27aa(0x1) = CONST 
    0x27ac: v27ac(0xa0) = CONST 
    0x27ae: v27ae(0x10000000000000000000000000000000000000000) = SHL v27ac(0xa0), v27aa(0x1)
    0x27af: v27af(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27ae(0x10000000000000000000000000000000000000000), v27a8(0x1)
    0x27b2: v27b2 = AND v27af(0xffffffffffffffffffffffffffffffffffffffff), v411
    0x27b4: MSTORE v27a1, v27b2
    0x27b5: v27b5(0x20) = CONST 
    0x27b9: v27b9 = ADD v27a1, v27b5(0x20)
    0x27bc: MSTORE v27b9, v416
    0x27bf: v27bf = ADD v279e(0x40), v27a1
    0x27c2: MSTORE v27bf, v408
    0x27c3: v27c3(0x0) = CONST 
    0x27c7: MSTORE v27c3(0x0), v279c_0
    0x27c8: v27c8(0xb) = CONST 
    0x27cc: MSTORE v27b5(0x20), v27c8(0xb)
    0x27d0: v27d0 = SHA3 v27c3(0x0), v279e(0x40)
    0x27d2: v27d2 = MLOAD v27a1
    0x27d4: v27d4 = SLOAD v27d0
    0x27d5: v27d5(0x1) = CONST 
    0x27d7: v27d7(0x1) = CONST 
    0x27d9: v27d9(0xa0) = CONST 
    0x27db: v27db(0x10000000000000000000000000000000000000000) = SHL v27d9(0xa0), v27d7(0x1)
    0x27dc: v27dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27db(0x10000000000000000000000000000000000000000), v27d5(0x1)
    0x27dd: v27dd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27dc(0xffffffffffffffffffffffffffffffffffffffff)
    0x27de: v27de = AND v27dd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v27d4
    0x27e0: v27e0 = AND v27af(0xffffffffffffffffffffffffffffffffffffffff), v27d2
    0x27e4: v27e4 = OR v27e0, v27de
    0x27e6: SSTORE v27d0, v27e4
    0x27e8: v27e8 = MLOAD v27b9
    0x27e9: v27e9(0x1) = CONST 
    0x27ec: v27ec = ADD v27d0, v27e9(0x1)
    0x27ed: SSTORE v27ec, v27e8
    0x27f1: v27f1 = MLOAD v27bf
    0x27f2: v27f2(0x2) = CONST 
    0x27f6: v27f6 = ADD v27d0, v27f2(0x2)
    0x27f7: SSTORE v27f6, v27f1
    0x27fc: JUMP v10e6(0x10f2)

    Begin block 0x10f2
    prev=[0x279d], succ=[0x3e26]
    =================================
    0x10fb: JUMP v3da(0x3e26)

    Begin block 0x3e26
    prev=[0x10f2], succ=[]
    =================================
    0x3e27: v3e27(0x40) = CONST 
    0x3e2a: v3e2a = MLOAD v3e27(0x40)
    0x3e2d: MSTORE v3e2a, v279c_0
    0x3e2e: v3e2e = MLOAD v3e27(0x40)
    0x3e32: v3e32(0x0) = SUB v3e2a, v3e2e
    0x3e33: v3e33(0x20) = CONST 
    0x3e35: v3e35(0x20) = ADD v3e33(0x20), v3e32(0x0)
    0x3e37: RETURN v3e2e, v3e35(0x20)

}

function safeBatchTransferFrom(address,address,uint256[],uint256[],bytes)() public {
    Begin block 0x41b
    prev=[], succ=[0x42d, 0x431]
    =================================
    0x41c: v41c(0x3e57) = CONST 
    0x41f: v41f(0x4) = CONST 
    0x422: v422 = CALLDATASIZE 
    0x423: v423 = SUB v422, v41f(0x4)
    0x424: v424(0xa0) = CONST 
    0x427: v427 = LT v423, v424(0xa0)
    0x428: v428 = ISZERO v427
    0x429: v429(0x431) = CONST 
    0x42c: JUMPI v429(0x431), v428

    Begin block 0x42d
    prev=[0x41b], succ=[]
    =================================
    0x42d: v42d(0x0) = CONST 
    0x430: REVERT v42d(0x0), v42d(0x0)

    Begin block 0x431
    prev=[0x41b], succ=[0x460, 0x464]
    =================================
    0x432: v432(0x1) = CONST 
    0x434: v434(0x1) = CONST 
    0x436: v436(0xa0) = CONST 
    0x438: v438(0x10000000000000000000000000000000000000000) = SHL v436(0xa0), v434(0x1)
    0x439: v439(0xffffffffffffffffffffffffffffffffffffffff) = SUB v438(0x10000000000000000000000000000000000000000), v432(0x1)
    0x43b: v43b = CALLDATALOAD v41f(0x4)
    0x43d: v43d = AND v439(0xffffffffffffffffffffffffffffffffffffffff), v43b
    0x43f: v43f(0x20) = CONST 
    0x442: v442(0x24) = ADD v41f(0x4), v43f(0x20)
    0x443: v443 = CALLDATALOAD v442(0x24)
    0x446: v446 = AND v439(0xffffffffffffffffffffffffffffffffffffffff), v443
    0x449: v449 = ADD v41f(0x4), v423
    0x44b: v44b(0x60) = CONST 
    0x44e: v44e(0x64) = ADD v41f(0x4), v44b(0x60)
    0x44f: v44f(0x40) = CONST 
    0x452: v452(0x44) = ADD v41f(0x4), v44f(0x40)
    0x453: v453 = CALLDATALOAD v452(0x44)
    0x454: v454(0x1) = CONST 
    0x456: v456(0x20) = CONST 
    0x458: v458(0x100000000) = SHL v456(0x20), v454(0x1)
    0x45a: v45a = GT v453, v458(0x100000000)
    0x45b: v45b = ISZERO v45a
    0x45c: v45c(0x464) = CONST 
    0x45f: JUMPI v45c(0x464), v45b

    Begin block 0x460
    prev=[0x431], succ=[]
    =================================
    0x460: v460(0x0) = CONST 
    0x463: REVERT v460(0x0), v460(0x0)

    Begin block 0x464
    prev=[0x431], succ=[0x472, 0x476]
    =================================
    0x466: v466 = ADD v41f(0x4), v453
    0x468: v468(0x20) = CONST 
    0x46b: v46b = ADD v466, v468(0x20)
    0x46c: v46c = GT v46b, v449
    0x46d: v46d = ISZERO v46c
    0x46e: v46e(0x476) = CONST 
    0x471: JUMPI v46e(0x476), v46d

    Begin block 0x472
    prev=[0x464], succ=[]
    =================================
    0x472: v472(0x0) = CONST 
    0x475: REVERT v472(0x0), v472(0x0)

    Begin block 0x476
    prev=[0x464], succ=[0x493, 0x497]
    =================================
    0x478: v478 = CALLDATALOAD v466
    0x47a: v47a(0x20) = CONST 
    0x47c: v47c = ADD v47a(0x20), v466
    0x47f: v47f(0x20) = CONST 
    0x482: v482 = MUL v478, v47f(0x20)
    0x484: v484 = ADD v47c, v482
    0x485: v485 = GT v484, v449
    0x486: v486(0x1) = CONST 
    0x488: v488(0x20) = CONST 
    0x48a: v48a(0x100000000) = SHL v488(0x20), v486(0x1)
    0x48c: v48c = GT v478, v48a(0x100000000)
    0x48d: v48d = OR v48c, v485
    0x48e: v48e = ISZERO v48d
    0x48f: v48f(0x497) = CONST 
    0x492: JUMPI v48f(0x497), v48e

    Begin block 0x493
    prev=[0x476], succ=[]
    =================================
    0x493: v493(0x0) = CONST 
    0x496: REVERT v493(0x0), v493(0x0)

    Begin block 0x497
    prev=[0x476], succ=[0x4e2, 0x4e6]
    =================================
    0x49c: v49c(0x20) = CONST 
    0x49e: v49e = MUL v49c(0x20), v478
    0x49f: v49f(0x20) = CONST 
    0x4a1: v4a1 = ADD v49f(0x20), v49e
    0x4a2: v4a2(0x40) = CONST 
    0x4a4: v4a4 = MLOAD v4a2(0x40)
    0x4a7: v4a7 = ADD v4a4, v4a1
    0x4a8: v4a8(0x40) = CONST 
    0x4aa: MSTORE v4a8(0x40), v4a7
    0x4b2: MSTORE v4a4, v478
    0x4b3: v4b3(0x20) = CONST 
    0x4b5: v4b5 = ADD v4b3(0x20), v4a4
    0x4b8: v4b8(0x20) = CONST 
    0x4ba: v4ba = MUL v4b8(0x20), v478
    0x4be: CALLDATACOPY v4b5, v47c, v4ba
    0x4bf: v4bf(0x0) = CONST 
    0x4c2: v4c2 = ADD v4b5, v4ba
    0x4c6: MSTORE v4c2, v4bf(0x0)
    0x4cc: v4cc(0x20) = CONST 
    0x4cf: v4cf(0x84) = ADD v44e(0x64), v4cc(0x20)
    0x4d2: v4d2 = CALLDATALOAD v44e(0x64)
    0x4d6: v4d6(0x1) = CONST 
    0x4d8: v4d8(0x20) = CONST 
    0x4da: v4da(0x100000000) = SHL v4d8(0x20), v4d6(0x1)
    0x4dc: v4dc = GT v4d2, v4da(0x100000000)
    0x4dd: v4dd = ISZERO v4dc
    0x4de: v4de(0x4e6) = CONST 
    0x4e1: JUMPI v4de(0x4e6), v4dd

    Begin block 0x4e2
    prev=[0x497], succ=[]
    =================================
    0x4e2: v4e2(0x0) = CONST 
    0x4e5: REVERT v4e2(0x0), v4e2(0x0)

    Begin block 0x4e6
    prev=[0x497], succ=[0x4f4, 0x4f8]
    =================================
    0x4e8: v4e8 = ADD v41f(0x4), v4d2
    0x4ea: v4ea(0x20) = CONST 
    0x4ed: v4ed = ADD v4e8, v4ea(0x20)
    0x4ee: v4ee = GT v4ed, v449
    0x4ef: v4ef = ISZERO v4ee
    0x4f0: v4f0(0x4f8) = CONST 
    0x4f3: JUMPI v4f0(0x4f8), v4ef

    Begin block 0x4f4
    prev=[0x4e6], succ=[]
    =================================
    0x4f4: v4f4(0x0) = CONST 
    0x4f7: REVERT v4f4(0x0), v4f4(0x0)

    Begin block 0x4f8
    prev=[0x4e6], succ=[0x515, 0x519]
    =================================
    0x4fa: v4fa = CALLDATALOAD v4e8
    0x4fc: v4fc(0x20) = CONST 
    0x4fe: v4fe = ADD v4fc(0x20), v4e8
    0x501: v501(0x20) = CONST 
    0x504: v504 = MUL v4fa, v501(0x20)
    0x506: v506 = ADD v4fe, v504
    0x507: v507 = GT v506, v449
    0x508: v508(0x1) = CONST 
    0x50a: v50a(0x20) = CONST 
    0x50c: v50c(0x100000000) = SHL v50a(0x20), v508(0x1)
    0x50e: v50e = GT v4fa, v50c(0x100000000)
    0x50f: v50f = OR v50e, v507
    0x510: v510 = ISZERO v50f
    0x511: v511(0x519) = CONST 
    0x514: JUMPI v511(0x519), v510

    Begin block 0x515
    prev=[0x4f8], succ=[]
    =================================
    0x515: v515(0x0) = CONST 
    0x518: REVERT v515(0x0), v515(0x0)

    Begin block 0x519
    prev=[0x4f8], succ=[0x564, 0x568]
    =================================
    0x51e: v51e(0x20) = CONST 
    0x520: v520 = MUL v51e(0x20), v4fa
    0x521: v521(0x20) = CONST 
    0x523: v523 = ADD v521(0x20), v520
    0x524: v524(0x40) = CONST 
    0x526: v526 = MLOAD v524(0x40)
    0x529: v529 = ADD v526, v523
    0x52a: v52a(0x40) = CONST 
    0x52c: MSTORE v52a(0x40), v529
    0x534: MSTORE v526, v4fa
    0x535: v535(0x20) = CONST 
    0x537: v537 = ADD v535(0x20), v526
    0x53a: v53a(0x20) = CONST 
    0x53c: v53c = MUL v53a(0x20), v4fa
    0x540: CALLDATACOPY v537, v4fe, v53c
    0x541: v541(0x0) = CONST 
    0x544: v544 = ADD v537, v53c
    0x548: MSTORE v544, v541(0x0)
    0x54e: v54e(0x20) = CONST 
    0x551: v551(0xa4) = ADD v4cf(0x84), v54e(0x20)
    0x554: v554 = CALLDATALOAD v4cf(0x84)
    0x558: v558(0x1) = CONST 
    0x55a: v55a(0x20) = CONST 
    0x55c: v55c(0x100000000) = SHL v55a(0x20), v558(0x1)
    0x55e: v55e = GT v554, v55c(0x100000000)
    0x55f: v55f = ISZERO v55e
    0x560: v560(0x568) = CONST 
    0x563: JUMPI v560(0x568), v55f

    Begin block 0x564
    prev=[0x519], succ=[]
    =================================
    0x564: v564(0x0) = CONST 
    0x567: REVERT v564(0x0), v564(0x0)

    Begin block 0x568
    prev=[0x519], succ=[0x576, 0x57a]
    =================================
    0x56a: v56a = ADD v41f(0x4), v554
    0x56c: v56c(0x20) = CONST 
    0x56f: v56f = ADD v56a, v56c(0x20)
    0x570: v570 = GT v56f, v449
    0x571: v571 = ISZERO v570
    0x572: v572(0x57a) = CONST 
    0x575: JUMPI v572(0x57a), v571

    Begin block 0x576
    prev=[0x568], succ=[]
    =================================
    0x576: v576(0x0) = CONST 
    0x579: REVERT v576(0x0), v576(0x0)

    Begin block 0x57a
    prev=[0x568], succ=[0x597, 0x59b]
    =================================
    0x57c: v57c = CALLDATALOAD v56a
    0x57e: v57e(0x20) = CONST 
    0x580: v580 = ADD v57e(0x20), v56a
    0x583: v583(0x1) = CONST 
    0x586: v586 = MUL v57c, v583(0x1)
    0x588: v588 = ADD v580, v586
    0x589: v589 = GT v588, v449
    0x58a: v58a(0x1) = CONST 
    0x58c: v58c(0x20) = CONST 
    0x58e: v58e(0x100000000) = SHL v58c(0x20), v58a(0x1)
    0x590: v590 = GT v57c, v58e(0x100000000)
    0x591: v591 = OR v590, v589
    0x592: v592 = ISZERO v591
    0x593: v593(0x59b) = CONST 
    0x596: JUMPI v593(0x59b), v592

    Begin block 0x597
    prev=[0x57a], succ=[]
    =================================
    0x597: v597(0x0) = CONST 
    0x59a: REVERT v597(0x0), v597(0x0)

    Begin block 0x59b
    prev=[0x57a], succ=[0x10fc]
    =================================
    0x5a0: v5a0(0x1f) = CONST 
    0x5a2: v5a2 = ADD v5a0(0x1f), v57c
    0x5a3: v5a3(0x20) = CONST 
    0x5a7: v5a7 = DIV v5a2, v5a3(0x20)
    0x5a8: v5a8 = MUL v5a7, v5a3(0x20)
    0x5a9: v5a9(0x20) = CONST 
    0x5ab: v5ab = ADD v5a9(0x20), v5a8
    0x5ac: v5ac(0x40) = CONST 
    0x5ae: v5ae = MLOAD v5ac(0x40)
    0x5b1: v5b1 = ADD v5ae, v5ab
    0x5b2: v5b2(0x40) = CONST 
    0x5b4: MSTORE v5b2(0x40), v5b1
    0x5bc: MSTORE v5ae, v57c
    0x5bd: v5bd(0x20) = CONST 
    0x5bf: v5bf = ADD v5bd(0x20), v5ae
    0x5c5: CALLDATACOPY v5bf, v580, v57c
    0x5c6: v5c6(0x0) = CONST 
    0x5c9: v5c9 = ADD v5bf, v57c
    0x5cd: MSTORE v5c9, v5c6(0x0)
    0x5d2: v5d2(0x10fc) = CONST 
    0x5db: JUMP v5d2(0x10fc)

    Begin block 0x10fc
    prev=[0x59b], succ=[0x110b, 0x1141]
    =================================
    0x10fd: v10fd(0x1) = CONST 
    0x10ff: v10ff(0x1) = CONST 
    0x1101: v1101(0xa0) = CONST 
    0x1103: v1103(0x10000000000000000000000000000000000000000) = SHL v1101(0xa0), v10ff(0x1)
    0x1104: v1104(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1103(0x10000000000000000000000000000000000000000), v10fd(0x1)
    0x1106: v1106 = AND v446, v1104(0xffffffffffffffffffffffffffffffffffffffff)
    0x1107: v1107(0x1141) = CONST 
    0x110a: JUMPI v1107(0x1141), v1106

    Begin block 0x110b
    prev=[0x10fc], succ=[]
    =================================
    0x110b: v110b(0x40) = CONST 
    0x110d: v110d = MLOAD v110b(0x40)
    0x110e: v110e(0x461bcd) = CONST 
    0x1112: v1112(0xe5) = CONST 
    0x1114: v1114(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1112(0xe5), v110e(0x461bcd)
    0x1116: MSTORE v110d, v1114(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1117: v1117(0x4) = CONST 
    0x1119: v1119 = ADD v1117(0x4), v110d
    0x111c: v111c(0x20) = CONST 
    0x111e: v111e = ADD v111c(0x20), v1119
    0x1121: v1121(0x20) = SUB v111e, v1119
    0x1123: MSTORE v1119, v1121(0x20)
    0x1124: v1124(0x2a) = CONST 
    0x1127: MSTORE v111e, v1124(0x2a)
    0x1128: v1128(0x20) = CONST 
    0x112a: v112a = ADD v1128(0x20), v111e
    0x112c: v112c(0x3b95) = CONST 
    0x112f: v112f(0x2a) = CONST 
    0x1132: CODECOPY v112a, v112c(0x3b95), v112f(0x2a)
    0x1133: v1133(0x40) = CONST 
    0x1135: v1135 = ADD v1133(0x40), v112a
    0x1139: v1139(0x40) = CONST 
    0x113b: v113b = MLOAD v1139(0x40)
    0x113e: v113e(0x84) = SUB v1135, v113b
    0x1140: REVERT v113b, v113e(0x84)

    Begin block 0x1141
    prev=[0x10fc], succ=[0x114b, 0x1181]
    =================================
    0x1143: v1143 = MLOAD v526
    0x1145: v1145 = MLOAD v4a4
    0x1146: v1146 = EQ v1145, v1143
    0x1147: v1147(0x1181) = CONST 
    0x114a: JUMPI v1147(0x1181), v1146

    Begin block 0x114b
    prev=[0x1141], succ=[]
    =================================
    0x114b: v114b(0x40) = CONST 
    0x114d: v114d = MLOAD v114b(0x40)
    0x114e: v114e(0x461bcd) = CONST 
    0x1152: v1152(0xe5) = CONST 
    0x1154: v1154(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1152(0xe5), v114e(0x461bcd)
    0x1156: MSTORE v114d, v1154(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1157: v1157(0x4) = CONST 
    0x1159: v1159 = ADD v1157(0x4), v114d
    0x115c: v115c(0x20) = CONST 
    0x115e: v115e = ADD v115c(0x20), v1159
    0x1161: v1161(0x20) = SUB v115e, v1159
    0x1163: MSTORE v1159, v1161(0x20)
    0x1164: v1164(0x23) = CONST 
    0x1167: MSTORE v115e, v1164(0x23)
    0x1168: v1168(0x20) = CONST 
    0x116a: v116a = ADD v1168(0x20), v115e
    0x116c: v116c(0x3b4e) = CONST 
    0x116f: v116f(0x23) = CONST 
    0x1172: CODECOPY v116a, v116c(0x3b4e), v116f(0x23)
    0x1173: v1173(0x40) = CONST 
    0x1175: v1175 = ADD v1173(0x40), v116a
    0x1179: v1179(0x40) = CONST 
    0x117b: v117b = MLOAD v1179(0x40)
    0x117e: v117e(0x84) = SUB v1175, v117b
    0x1180: REVERT v117b, v117e(0x84)

    Begin block 0x1181
    prev=[0x1141], succ=[0x119d, 0x1193]
    =================================
    0x1182: v1182(0x1) = CONST 
    0x1184: v1184(0x1) = CONST 
    0x1186: v1186(0xa0) = CONST 
    0x1188: v1188(0x10000000000000000000000000000000000000000) = SHL v1186(0xa0), v1184(0x1)
    0x1189: v1189(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1188(0x10000000000000000000000000000000000000000), v1182(0x1)
    0x118b: v118b = AND v43d, v1189(0xffffffffffffffffffffffffffffffffffffffff)
    0x118c: v118c = CALLER 
    0x118d: v118d = EQ v118c, v118b
    0x118f: v118f(0x119d) = CONST 
    0x1192: JUMPI v118f(0x119d), v118d

    Begin block 0x119d
    prev=[0x1181, 0x24d2B0x1193], succ=[0x11a2, 0x11d8]
    =================================
    0x119d_0x0: v119d_0 = PHI v118d, v24fdV1193
    0x119e: v119e(0x11d8) = CONST 
    0x11a1: JUMPI v119e(0x11d8), v119d_0

    Begin block 0x11a2
    prev=[0x119d], succ=[]
    =================================
    0x11a2: v11a2(0x40) = CONST 
    0x11a4: v11a4 = MLOAD v11a2(0x40)
    0x11a5: v11a5(0x461bcd) = CONST 
    0x11a9: v11a9(0xe5) = CONST 
    0x11ab: v11ab(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v11a9(0xe5), v11a5(0x461bcd)
    0x11ad: MSTORE v11a4, v11ab(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11ae: v11ae(0x4) = CONST 
    0x11b0: v11b0 = ADD v11ae(0x4), v11a4
    0x11b3: v11b3(0x20) = CONST 
    0x11b5: v11b5 = ADD v11b3(0x20), v11b0
    0x11b8: v11b8(0x20) = SUB v11b5, v11b0
    0x11ba: MSTORE v11b0, v11b8(0x20)
    0x11bb: v11bb(0x2d) = CONST 
    0x11be: MSTORE v11b5, v11bb(0x2d)
    0x11bf: v11bf(0x20) = CONST 
    0x11c1: v11c1 = ADD v11bf(0x20), v11b5
    0x11c3: v11c3(0x3ad8) = CONST 
    0x11c6: v11c6(0x2d) = CONST 
    0x11c9: CODECOPY v11c1, v11c3(0x3ad8), v11c6(0x2d)
    0x11ca: v11ca(0x40) = CONST 
    0x11cc: v11cc = ADD v11ca(0x40), v11c1
    0x11d0: v11d0(0x40) = CONST 
    0x11d2: v11d2 = MLOAD v11d0(0x40)
    0x11d5: v11d5(0x84) = SUB v11cc, v11d2
    0x11d7: REVERT v11d2, v11d5(0x84)

    Begin block 0x11d8
    prev=[0x119d], succ=[0x11db]
    =================================
    0x11d9: v11d9(0x0) = CONST 

    Begin block 0x11db
    prev=[0x11d8, 0x1247], succ=[0x11e5, 0x1276]
    =================================
    0x11db_0x0: v11db_0 = PHI v11d9(0x0), v1271
    0x11dd: v11dd = MLOAD v4a4
    0x11df: v11df = LT v11db_0, v11dd
    0x11e0: v11e0 = ISZERO v11df
    0x11e1: v11e1(0x1276) = CONST 
    0x11e4: JUMPI v11e1(0x1276), v11e0

    Begin block 0x11e5
    prev=[0x11db], succ=[0x11f1, 0x11f2]
    =================================
    0x11e5: v11e5(0x0) = CONST 
    0x11e5_0x0: v11e5_0 = PHI v11d9(0x0), v1271
    0x11ea: v11ea = MLOAD v4a4
    0x11ec: v11ec = LT v11e5_0, v11ea
    0x11ed: v11ed(0x11f2) = CONST 
    0x11f0: JUMPI v11ed(0x11f2), v11ec

    Begin block 0x11f1
    prev=[0x11e5], succ=[]
    =================================
    0x11f1: THROW 

    Begin block 0x11f2
    prev=[0x11e5], succ=[0x1206]
    =================================
    0x11f2_0x0: v11f2_0 = PHI v11d9(0x0), v1271
    0x11f3: v11f3(0x20) = CONST 
    0x11f5: v11f5 = MUL v11f3(0x20), v11f2_0
    0x11f6: v11f6(0x20) = CONST 
    0x11f8: v11f8 = ADD v11f6(0x20), v11f5
    0x11f9: v11f9 = ADD v11f8, v4a4
    0x11fa: v11fa = MLOAD v11f9
    0x11fd: v11fd(0x1206) = CONST 
    0x1202: v1202(0x2497) = CONST 
    0x1205: v1205_0 = CALLPRIVATE v1202(0x2497), v11fa, v43d, v11fd(0x1206)

    Begin block 0x1206
    prev=[0x11f2], succ=[0x120b, 0x1247]
    =================================
    0x1207: v1207(0x1247) = CONST 
    0x120a: JUMPI v1207(0x1247), v1205_0

    Begin block 0x120b
    prev=[0x1206], succ=[]
    =================================
    0x120b: v120b(0x40) = CONST 
    0x120e: v120e = MLOAD v120b(0x40)
    0x120f: v120f(0x461bcd) = CONST 
    0x1213: v1213(0xe5) = CONST 
    0x1215: v1215(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1213(0xe5), v120f(0x461bcd)
    0x1217: MSTORE v120e, v1215(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1218: v1218(0x20) = CONST 
    0x121a: v121a(0x4) = CONST 
    0x121d: v121d = ADD v120e, v121a(0x4)
    0x121e: MSTORE v121d, v1218(0x20)
    0x121f: v121f(0xd) = CONST 
    0x1221: v1221(0x24) = CONST 
    0x1224: v1224 = ADD v120e, v1221(0x24)
    0x1225: MSTORE v1224, v121f(0xd)
    0x1226: v1226(0x2737ba103a34329037bbb732b9) = CONST 
    0x1234: v1234(0x99) = CONST 
    0x1236: v1236(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v1234(0x99), v1226(0x2737ba103a34329037bbb732b9)
    0x1237: v1237(0x44) = CONST 
    0x123a: v123a = ADD v120e, v1237(0x44)
    0x123b: MSTORE v123a, v1236(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x123d: v123d = MLOAD v120b(0x40)
    0x1241: v1241(0x0) = SUB v120e, v123d
    0x1242: v1242(0x64) = CONST 
    0x1244: v1244(0x64) = ADD v1242(0x64), v1241(0x0)
    0x1246: REVERT v123d, v1244(0x64)

    Begin block 0x1247
    prev=[0x1206], succ=[0x11db]
    =================================
    0x1247_0x1: v1247_1 = PHI v11d9(0x0), v1271
    0x1248: v1248(0x0) = CONST 
    0x124c: MSTORE v1248(0x0), v11fa
    0x124d: v124d(0x8) = CONST 
    0x124f: v124f(0x20) = CONST 
    0x1251: MSTORE v124f(0x20), v124d(0x8)
    0x1252: v1252(0x40) = CONST 
    0x1255: v1255 = SHA3 v1248(0x0), v1252(0x40)
    0x1257: v1257 = SLOAD v1255
    0x1258: v1258(0x1) = CONST 
    0x125a: v125a(0x1) = CONST 
    0x125c: v125c(0xa0) = CONST 
    0x125e: v125e(0x10000000000000000000000000000000000000000) = SHL v125c(0xa0), v125a(0x1)
    0x125f: v125f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v125e(0x10000000000000000000000000000000000000000), v1258(0x1)
    0x1260: v1260(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v125f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1261: v1261 = AND v1260(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1257
    0x1262: v1262(0x1) = CONST 
    0x1264: v1264(0x1) = CONST 
    0x1266: v1266(0xa0) = CONST 
    0x1268: v1268(0x10000000000000000000000000000000000000000) = SHL v1266(0xa0), v1264(0x1)
    0x1269: v1269(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1268(0x10000000000000000000000000000000000000000), v1262(0x1)
    0x126b: v126b = AND v446, v1269(0xffffffffffffffffffffffffffffffffffffffff)
    0x126c: v126c = OR v126b, v1261
    0x126e: SSTORE v1255, v126c
    0x126f: v126f(0x1) = CONST 
    0x1271: v1271 = ADD v126f(0x1), v1247_1
    0x1272: v1272(0x11db) = CONST 
    0x1275: JUMP v1272(0x11db)

    Begin block 0x1276
    prev=[0x11db], succ=[0x12e4]
    =================================
    0x1279: v1279(0x1) = CONST 
    0x127b: v127b(0x1) = CONST 
    0x127d: v127d(0xa0) = CONST 
    0x127f: v127f(0x10000000000000000000000000000000000000000) = SHL v127d(0xa0), v127b(0x1)
    0x1280: v1280(0xffffffffffffffffffffffffffffffffffffffff) = SUB v127f(0x10000000000000000000000000000000000000000), v1279(0x1)
    0x1281: v1281 = AND v1280(0xffffffffffffffffffffffffffffffffffffffff), v446
    0x1283: v1283(0x1) = CONST 
    0x1285: v1285(0x1) = CONST 
    0x1287: v1287(0xa0) = CONST 
    0x1289: v1289(0x10000000000000000000000000000000000000000) = SHL v1287(0xa0), v1285(0x1)
    0x128a: v128a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1289(0x10000000000000000000000000000000000000000), v1283(0x1)
    0x128b: v128b = AND v128a(0xffffffffffffffffffffffffffffffffffffffff), v43d
    0x128c: v128c = CALLER 
    0x128d: v128d(0x1) = CONST 
    0x128f: v128f(0x1) = CONST 
    0x1291: v1291(0xa0) = CONST 
    0x1293: v1293(0x10000000000000000000000000000000000000000) = SHL v1291(0xa0), v128f(0x1)
    0x1294: v1294(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1293(0x10000000000000000000000000000000000000000), v128d(0x1)
    0x1295: v1295 = AND v1294(0xffffffffffffffffffffffffffffffffffffffff), v128c
    0x1296: v1296(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x12b9: v12b9(0x40) = CONST 
    0x12bb: v12bb = MLOAD v12b9(0x40)
    0x12be: v12be(0x20) = CONST 
    0x12c0: v12c0 = ADD v12be(0x20), v12bb
    0x12c2: v12c2(0x20) = CONST 
    0x12c4: v12c4 = ADD v12c2(0x20), v12c0
    0x12c7: v12c7(0x40) = SUB v12c4, v12bb
    0x12c9: MSTORE v12bb, v12c7(0x40)
    0x12cd: v12cd = MLOAD v4a4
    0x12cf: MSTORE v12c4, v12cd
    0x12d0: v12d0(0x20) = CONST 
    0x12d2: v12d2 = ADD v12d0(0x20), v12c4
    0x12d6: v12d6 = MLOAD v4a4
    0x12d8: v12d8(0x20) = CONST 
    0x12da: v12da = ADD v12d8(0x20), v4a4
    0x12dc: v12dc(0x20) = CONST 
    0x12de: v12de = MUL v12dc(0x20), v12d6
    0x12e2: v12e2(0x0) = CONST 

    Begin block 0x12e4
    prev=[0x1276, 0x12ed], succ=[0x12fc, 0x12ed]
    =================================
    0x12e4_0x0: v12e4_0 = PHI v12e2(0x0), v12f7
    0x12e7: v12e7 = LT v12e4_0, v12de
    0x12e8: v12e8 = ISZERO v12e7
    0x12e9: v12e9(0x12fc) = CONST 
    0x12ec: JUMPI v12e9(0x12fc), v12e8

    Begin block 0x12fc
    prev=[0x12e4], succ=[0x1323]
    =================================
    0x1303: v1303 = ADD v12de, v12d2
    0x1306: v1306 = SUB v1303, v12bb
    0x1308: MSTORE v12c0, v1306
    0x130c: v130c = MLOAD v526
    0x130e: MSTORE v1303, v130c
    0x130f: v130f(0x20) = CONST 
    0x1311: v1311 = ADD v130f(0x20), v1303
    0x1315: v1315 = MLOAD v526
    0x1317: v1317(0x20) = CONST 
    0x1319: v1319 = ADD v1317(0x20), v526
    0x131b: v131b(0x20) = CONST 
    0x131d: v131d = MUL v131b(0x20), v1315
    0x1321: v1321(0x0) = CONST 

    Begin block 0x1323
    prev=[0x12fc, 0x132c], succ=[0x133b, 0x132c]
    =================================
    0x1323_0x0: v1323_0 = PHI v1321(0x0), v1336
    0x1326: v1326 = LT v1323_0, v131d
    0x1327: v1327 = ISZERO v1326
    0x1328: v1328(0x133b) = CONST 
    0x132b: JUMPI v1328(0x133b), v1327

    Begin block 0x133b
    prev=[0x1323], succ=[0x42ab]
    =================================
    0x1342: v1342 = ADD v131d, v1311
    0x1349: v1349(0x40) = CONST 
    0x134b: v134b = MLOAD v1349(0x40)
    0x134e: v134e = SUB v1342, v134b
    0x1350: LOG4 v134b, v134e, v1296(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v1295, v128b, v1281
    0x1351: v1351(0x42ab) = CONST 
    0x1354: v1354 = CALLER 
    0x135a: v135a(0x27fd) = CONST 
    0x135d: CALLPRIVATE v135a(0x27fd), v5ae, v526, v4a4, v446, v43d, v1354, v1351(0x42ab)

    Begin block 0x42ab
    prev=[0x133b], succ=[0x3e57]
    =================================
    0x42b1: JUMP v41c(0x3e57)

    Begin block 0x3e57
    prev=[0x42ab], succ=[]
    =================================
    0x3e58: STOP 

    Begin block 0x132c
    prev=[0x1323], succ=[0x1323]
    =================================
    0x132c_0x0: v132c_0 = PHI v1321(0x0), v1336
    0x132e: v132e = ADD v132c_0, v1319
    0x132f: v132f = MLOAD v132e
    0x1332: v1332 = ADD v132c_0, v1311
    0x1333: MSTORE v1332, v132f
    0x1334: v1334(0x20) = CONST 
    0x1336: v1336 = ADD v1334(0x20), v132c_0
    0x1337: v1337(0x1323) = CONST 
    0x133a: JUMP v1337(0x1323)

    Begin block 0x12ed
    prev=[0x12e4], succ=[0x12e4]
    =================================
    0x12ed_0x0: v12ed_0 = PHI v12e2(0x0), v12f7
    0x12ef: v12ef = ADD v12ed_0, v12da
    0x12f0: v12f0 = MLOAD v12ef
    0x12f3: v12f3 = ADD v12ed_0, v12d2
    0x12f4: MSTORE v12f3, v12f0
    0x12f5: v12f5(0x20) = CONST 
    0x12f7: v12f7 = ADD v12f5(0x20), v12ed_0
    0x12f8: v12f8(0x12e4) = CONST 
    0x12fb: JUMP v12f8(0x12e4)

    Begin block 0x1193
    prev=[0x1181], succ=[0x24d2B0x1193]
    =================================
    0x1194: v1194(0x119d) = CONST 
    0x1198: v1198 = CALLER 
    0x1199: v1199(0x24d2) = CONST 
    0x119c: JUMP v1199(0x24d2)

    Begin block 0x24d2B0x1193
    prev=[0x1193], succ=[0x119d]
    =================================
    0x24d3S0x1193: v24d3V1193(0x1) = CONST 
    0x24d5S0x1193: v24d5V1193(0x1) = CONST 
    0x24d7S0x1193: v24d7V1193(0xa0) = CONST 
    0x24d9S0x1193: v24d9V1193(0x10000000000000000000000000000000000000000) = SHL v24d7V1193(0xa0), v24d5V1193(0x1)
    0x24daS0x1193: v24daV1193(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24d9V1193(0x10000000000000000000000000000000000000000), v24d3V1193(0x1)
    0x24ddS0x1193: v24ddV1193 = AND v24daV1193(0xffffffffffffffffffffffffffffffffffffffff), v43d
    0x24deS0x1193: v24deV1193(0x0) = CONST 
    0x24e2S0x1193: MSTORE v24deV1193(0x0), v24ddV1193
    0x24e3S0x1193: v24e3V1193(0x9) = CONST 
    0x24e5S0x1193: v24e5V1193(0x20) = CONST 
    0x24e9S0x1193: MSTORE v24e5V1193(0x20), v24e3V1193(0x9)
    0x24eaS0x1193: v24eaV1193(0x40) = CONST 
    0x24eeS0x1193: v24eeV1193 = SHA3 v24deV1193(0x0), v24eaV1193(0x40)
    0x24f2S0x1193: v24f2V1193 = AND v24daV1193(0xffffffffffffffffffffffffffffffffffffffff), v1198
    0x24f4S0x1193: MSTORE v24deV1193(0x0), v24f2V1193
    0x24f8S0x1193: MSTORE v24e5V1193(0x20), v24eeV1193
    0x24f9S0x1193: v24f9V1193 = SHA3 v24deV1193(0x0), v24eaV1193(0x40)
    0x24faS0x1193: v24faV1193 = SLOAD v24f9V1193
    0x24fbS0x1193: v24fbV1193(0xff) = CONST 
    0x24fdS0x1193: v24fdV1193 = AND v24fbV1193(0xff), v24faV1193
    0x24ffS0x1193: JUMP v1194(0x119d)

}

function removeMinter(address)() public {
    Begin block 0x5dc
    prev=[], succ=[0x5ee, 0x5f2]
    =================================
    0x5dd: v5dd(0x3e78) = CONST 
    0x5e0: v5e0(0x4) = CONST 
    0x5e3: v5e3 = CALLDATASIZE 
    0x5e4: v5e4 = SUB v5e3, v5e0(0x4)
    0x5e5: v5e5(0x20) = CONST 
    0x5e8: v5e8 = LT v5e4, v5e5(0x20)
    0x5e9: v5e9 = ISZERO v5e8
    0x5ea: v5ea(0x5f2) = CONST 
    0x5ed: JUMPI v5ea(0x5f2), v5e9

    Begin block 0x5ee
    prev=[0x5dc], succ=[]
    =================================
    0x5ee: v5ee(0x0) = CONST 
    0x5f1: REVERT v5ee(0x0), v5ee(0x0)

    Begin block 0x5f2
    prev=[0x5dc], succ=[0x1365]
    =================================
    0x5f4: v5f4 = CALLDATALOAD v5e0(0x4)
    0x5f5: v5f5(0x1) = CONST 
    0x5f7: v5f7(0x1) = CONST 
    0x5f9: v5f9(0xa0) = CONST 
    0x5fb: v5fb(0x10000000000000000000000000000000000000000) = SHL v5f9(0xa0), v5f7(0x1)
    0x5fc: v5fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5fb(0x10000000000000000000000000000000000000000), v5f5(0x1)
    0x5fd: v5fd = AND v5fc(0xffffffffffffffffffffffffffffffffffffffff), v5f4
    0x5fe: v5fe(0x1365) = CONST 
    0x601: JUMP v5fe(0x1365)

    Begin block 0x1365
    prev=[0x5f2], succ=[0x1378, 0x13b4]
    =================================
    0x1366: v1366(0x3) = CONST 
    0x1368: v1368 = SLOAD v1366(0x3)
    0x1369: v1369(0x1) = CONST 
    0x136b: v136b(0x1) = CONST 
    0x136d: v136d(0xa0) = CONST 
    0x136f: v136f(0x10000000000000000000000000000000000000000) = SHL v136d(0xa0), v136b(0x1)
    0x1370: v1370(0xffffffffffffffffffffffffffffffffffffffff) = SUB v136f(0x10000000000000000000000000000000000000000), v1369(0x1)
    0x1371: v1371 = AND v1370(0xffffffffffffffffffffffffffffffffffffffff), v1368
    0x1372: v1372 = CALLER 
    0x1373: v1373 = EQ v1372, v1371
    0x1374: v1374(0x13b4) = CONST 
    0x1377: JUMPI v1374(0x13b4), v1373

    Begin block 0x1378
    prev=[0x1365], succ=[]
    =================================
    0x1378: v1378(0x40) = CONST 
    0x137b: v137b = MLOAD v1378(0x40)
    0x137c: v137c(0x461bcd) = CONST 
    0x1380: v1380(0xe5) = CONST 
    0x1382: v1382(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1380(0xe5), v137c(0x461bcd)
    0x1384: MSTORE v137b, v1382(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1385: v1385(0x20) = CONST 
    0x1387: v1387(0x4) = CONST 
    0x138a: v138a = ADD v137b, v1387(0x4)
    0x138b: MSTORE v138a, v1385(0x20)
    0x138c: v138c(0xd) = CONST 
    0x138e: v138e(0x24) = CONST 
    0x1391: v1391 = ADD v137b, v138e(0x24)
    0x1392: MSTORE v1391, v138c(0xd)
    0x1393: v1393(0x26bab9ba1031329037bbb732b9) = CONST 
    0x13a1: v13a1(0x99) = CONST 
    0x13a3: v13a3(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v13a1(0x99), v1393(0x26bab9ba1031329037bbb732b9)
    0x13a4: v13a4(0x44) = CONST 
    0x13a7: v13a7 = ADD v137b, v13a4(0x44)
    0x13a8: MSTORE v13a7, v13a3(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x13aa: v13aa = MLOAD v1378(0x40)
    0x13ae: v13ae(0x0) = SUB v137b, v13aa
    0x13af: v13af(0x64) = CONST 
    0x13b1: v13b1(0x64) = ADD v13af(0x64), v13ae(0x0)
    0x13b3: REVERT v13aa, v13b1(0x64)

    Begin block 0x13b4
    prev=[0x1365], succ=[0x13d5, 0x1419]
    =================================
    0x13b5: v13b5(0x1) = CONST 
    0x13b7: v13b7(0x1) = CONST 
    0x13b9: v13b9(0xa0) = CONST 
    0x13bb: v13bb(0x10000000000000000000000000000000000000000) = SHL v13b9(0xa0), v13b7(0x1)
    0x13bc: v13bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13bb(0x10000000000000000000000000000000000000000), v13b5(0x1)
    0x13be: v13be = AND v5fd, v13bc(0xffffffffffffffffffffffffffffffffffffffff)
    0x13bf: v13bf(0x0) = CONST 
    0x13c3: MSTORE v13bf(0x0), v13be
    0x13c4: v13c4(0x5) = CONST 
    0x13c6: v13c6(0x20) = CONST 
    0x13c8: MSTORE v13c6(0x20), v13c4(0x5)
    0x13c9: v13c9(0x40) = CONST 
    0x13cc: v13cc = SHA3 v13bf(0x0), v13c9(0x40)
    0x13cd: v13cd = SLOAD v13cc
    0x13ce: v13ce(0xff) = CONST 
    0x13d0: v13d0 = AND v13ce(0xff), v13cd
    0x13d1: v13d1(0x1419) = CONST 
    0x13d4: JUMPI v13d1(0x1419), v13d0

    Begin block 0x13d5
    prev=[0x13b4], succ=[]
    =================================
    0x13d5: v13d5(0x40) = CONST 
    0x13d8: v13d8 = MLOAD v13d5(0x40)
    0x13d9: v13d9(0x461bcd) = CONST 
    0x13dd: v13dd(0xe5) = CONST 
    0x13df: v13df(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13dd(0xe5), v13d9(0x461bcd)
    0x13e1: MSTORE v13d8, v13df(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13e2: v13e2(0x20) = CONST 
    0x13e4: v13e4(0x4) = CONST 
    0x13e7: v13e7 = ADD v13d8, v13e4(0x4)
    0x13e8: MSTORE v13e7, v13e2(0x20)
    0x13e9: v13e9(0x15) = CONST 
    0x13eb: v13eb(0x24) = CONST 
    0x13ee: v13ee = ADD v13d8, v13eb(0x24)
    0x13ef: MSTORE v13ee, v13e9(0x15)
    0x13f0: v13f0(0x135a5b9d195c88191bd95cc81b9bdd08195e1a5cdd) = CONST 
    0x1406: v1406(0x5a) = CONST 
    0x1408: v1408(0x4d696e74657220646f6573206e6f742065786973740000000000000000000000) = SHL v1406(0x5a), v13f0(0x135a5b9d195c88191bd95cc81b9bdd08195e1a5cdd)
    0x1409: v1409(0x44) = CONST 
    0x140c: v140c = ADD v13d8, v1409(0x44)
    0x140d: MSTORE v140c, v1408(0x4d696e74657220646f6573206e6f742065786973740000000000000000000000)
    0x140f: v140f = MLOAD v13d5(0x40)
    0x1413: v1413(0x0) = SUB v13d8, v140f
    0x1414: v1414(0x64) = CONST 
    0x1416: v1416(0x64) = ADD v1414(0x64), v1413(0x0)
    0x1418: REVERT v140f, v1416(0x64)

    Begin block 0x1419
    prev=[0x13b4], succ=[0x3e78]
    =================================
    0x141a: v141a(0x1) = CONST 
    0x141c: v141c(0x1) = CONST 
    0x141e: v141e(0xa0) = CONST 
    0x1420: v1420(0x10000000000000000000000000000000000000000) = SHL v141e(0xa0), v141c(0x1)
    0x1421: v1421(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1420(0x10000000000000000000000000000000000000000), v141a(0x1)
    0x1422: v1422 = AND v1421(0xffffffffffffffffffffffffffffffffffffffff), v5fd
    0x1423: v1423(0x0) = CONST 
    0x1427: MSTORE v1423(0x0), v1422
    0x1428: v1428(0x5) = CONST 
    0x142a: v142a(0x20) = CONST 
    0x142c: MSTORE v142a(0x20), v1428(0x5)
    0x142d: v142d(0x40) = CONST 
    0x1430: v1430 = SHA3 v1423(0x0), v142d(0x40)
    0x1432: v1432 = SLOAD v1430
    0x1433: v1433(0xff) = CONST 
    0x1435: v1435(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1433(0xff)
    0x1436: v1436 = AND v1435(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1432
    0x1438: SSTORE v1430, v1436
    0x1439: JUMP v5dd(0x3e78)

    Begin block 0x3e78
    prev=[0x1419], succ=[]
    =================================
    0x3e79: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x602
    prev=[], succ=[0x614, 0x618]
    =================================
    0x603: v603(0x3e99) = CONST 
    0x606: v606(0x4) = CONST 
    0x609: v609 = CALLDATASIZE 
    0x60a: v60a = SUB v609, v606(0x4)
    0x60b: v60b(0x40) = CONST 
    0x60e: v60e = LT v60a, v60b(0x40)
    0x60f: v60f = ISZERO v60e
    0x610: v610(0x618) = CONST 
    0x613: JUMPI v610(0x618), v60f

    Begin block 0x614
    prev=[0x602], succ=[]
    =================================
    0x614: v614(0x0) = CONST 
    0x617: REVERT v614(0x0), v614(0x0)

    Begin block 0x618
    prev=[0x602], succ=[0x143a]
    =================================
    0x61a: v61a(0x1) = CONST 
    0x61c: v61c(0x1) = CONST 
    0x61e: v61e(0xa0) = CONST 
    0x620: v620(0x10000000000000000000000000000000000000000) = SHL v61e(0xa0), v61c(0x1)
    0x621: v621(0xffffffffffffffffffffffffffffffffffffffff) = SUB v620(0x10000000000000000000000000000000000000000), v61a(0x1)
    0x623: v623 = CALLDATALOAD v606(0x4)
    0x624: v624 = AND v623, v621(0xffffffffffffffffffffffffffffffffffffffff)
    0x626: v626(0x20) = CONST 
    0x628: v628(0x24) = ADD v626(0x20), v606(0x4)
    0x629: v629 = CALLDATALOAD v628(0x24)
    0x62a: v62a(0x143a) = CONST 
    0x62d: JUMP v62a(0x143a)

    Begin block 0x143a
    prev=[0x618], succ=[0x1452, 0x148f]
    =================================
    0x143b: v143b = CALLER 
    0x143c: v143c(0x0) = CONST 
    0x1440: MSTORE v143c(0x0), v143b
    0x1441: v1441(0x5) = CONST 
    0x1443: v1443(0x20) = CONST 
    0x1445: MSTORE v1443(0x20), v1441(0x5)
    0x1446: v1446(0x40) = CONST 
    0x1449: v1449 = SHA3 v143c(0x0), v1446(0x40)
    0x144a: v144a = SLOAD v1449
    0x144b: v144b(0xff) = CONST 
    0x144d: v144d = AND v144b(0xff), v144a
    0x144e: v144e(0x148f) = CONST 
    0x1451: JUMPI v144e(0x148f), v144d

    Begin block 0x1452
    prev=[0x143a], succ=[]
    =================================
    0x1452: v1452(0x40) = CONST 
    0x1455: v1455 = MLOAD v1452(0x40)
    0x1456: v1456(0x461bcd) = CONST 
    0x145a: v145a(0xe5) = CONST 
    0x145c: v145c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v145a(0xe5), v1456(0x461bcd)
    0x145e: MSTORE v1455, v145c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x145f: v145f(0x20) = CONST 
    0x1461: v1461(0x4) = CONST 
    0x1464: v1464 = ADD v1455, v1461(0x4)
    0x1465: MSTORE v1464, v145f(0x20)
    0x1466: v1466(0xe) = CONST 
    0x1468: v1468(0x24) = CONST 
    0x146b: v146b = ADD v1455, v1468(0x24)
    0x146c: MSTORE v146b, v1466(0xe)
    0x146d: v146d(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x147c: v147c(0x91) = CONST 
    0x147e: v147e(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v147c(0x91), v146d(0x36bab9ba1031329036b4b73a32b9)
    0x147f: v147f(0x44) = CONST 
    0x1482: v1482 = ADD v1455, v147f(0x44)
    0x1483: MSTORE v1482, v147e(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x1485: v1485 = MLOAD v1452(0x40)
    0x1489: v1489(0x0) = SUB v1455, v1485
    0x148a: v148a(0x64) = CONST 
    0x148c: v148c(0x64) = ADD v148a(0x64), v1489(0x0)
    0x148e: REVERT v1485, v148c(0x64)

    Begin block 0x148f
    prev=[0x143a], succ=[0x42d1]
    =================================
    0x1490: v1490(0x42d1) = CONST 
    0x1495: v1495(0x2ad1) = CONST 
    0x1498: v1498_0 = CALLPRIVATE v1495(0x2ad1), v629, v624, v1490(0x42d1)

    Begin block 0x42d1
    prev=[0x148f], succ=[0x3e99]
    =================================
    0x42d7: JUMP v603(0x3e99)

    Begin block 0x3e99
    prev=[0x42d1], succ=[]
    =================================
    0x3e9a: v3e9a(0x40) = CONST 
    0x3e9d: v3e9d = MLOAD v3e9a(0x40)
    0x3ea0: MSTORE v3e9d, v1498_0
    0x3ea1: v3ea1 = MLOAD v3e9a(0x40)
    0x3ea5: v3ea5(0x0) = SUB v3e9d, v3ea1
    0x3ea6: v3ea6(0x20) = CONST 
    0x3ea8: v3ea8(0x20) = ADD v3ea6(0x20), v3ea5(0x0)
    0x3eaa: RETURN v3ea1, v3ea8(0x20)

}

function initialize(address,address)() public {
    Begin block 0x62e
    prev=[], succ=[0x640, 0x644]
    =================================
    0x62f: v62f(0x3eca) = CONST 
    0x632: v632(0x4) = CONST 
    0x635: v635 = CALLDATASIZE 
    0x636: v636 = SUB v635, v632(0x4)
    0x637: v637(0x40) = CONST 
    0x63a: v63a = LT v636, v637(0x40)
    0x63b: v63b = ISZERO v63a
    0x63c: v63c(0x644) = CONST 
    0x63f: JUMPI v63c(0x644), v63b

    Begin block 0x640
    prev=[0x62e], succ=[]
    =================================
    0x640: v640(0x0) = CONST 
    0x643: REVERT v640(0x0), v640(0x0)

    Begin block 0x644
    prev=[0x62e], succ=[0x14a0]
    =================================
    0x646: v646(0x1) = CONST 
    0x648: v648(0x1) = CONST 
    0x64a: v64a(0xa0) = CONST 
    0x64c: v64c(0x10000000000000000000000000000000000000000) = SHL v64a(0xa0), v648(0x1)
    0x64d: v64d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64c(0x10000000000000000000000000000000000000000), v646(0x1)
    0x64f: v64f = CALLDATALOAD v632(0x4)
    0x651: v651 = AND v64d(0xffffffffffffffffffffffffffffffffffffffff), v64f
    0x653: v653(0x20) = CONST 
    0x655: v655(0x24) = ADD v653(0x20), v632(0x4)
    0x656: v656 = CALLDATALOAD v655(0x24)
    0x657: v657 = AND v656, v64d(0xffffffffffffffffffffffffffffffffffffffff)
    0x658: v658(0x14a0) = CONST 
    0x65b: JUMP v658(0x14a0)

    Begin block 0x14a0
    prev=[0x644], succ=[0x14ac, 0x14f8]
    =================================
    0x14a1: v14a1(0x1) = CONST 
    0x14a3: v14a3 = SLOAD v14a1(0x1)
    0x14a4: v14a4(0xff) = CONST 
    0x14a6: v14a6 = AND v14a4(0xff), v14a3
    0x14a7: v14a7 = ISZERO v14a6
    0x14a8: v14a8(0x14f8) = CONST 
    0x14ab: JUMPI v14a8(0x14f8), v14a7

    Begin block 0x14ac
    prev=[0x14a0], succ=[]
    =================================
    0x14ac: v14ac(0x40) = CONST 
    0x14af: v14af = MLOAD v14ac(0x40)
    0x14b0: v14b0(0x461bcd) = CONST 
    0x14b4: v14b4(0xe5) = CONST 
    0x14b6: v14b6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v14b4(0xe5), v14b0(0x461bcd)
    0x14b8: MSTORE v14af, v14b6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14b9: v14b9(0x20) = CONST 
    0x14bb: v14bb(0x4) = CONST 
    0x14be: v14be = ADD v14af, v14bb(0x4)
    0x14bf: MSTORE v14be, v14b9(0x20)
    0x14c0: v14c0(0x1c) = CONST 
    0x14c2: v14c2(0x24) = CONST 
    0x14c5: v14c5 = ADD v14af, v14c2(0x24)
    0x14c6: MSTORE v14c5, v14c0(0x1c)
    0x14c7: v14c7(0x436f6e747261637420616c726561647920696e697469616c697a656400000000) = CONST 
    0x14e8: v14e8(0x44) = CONST 
    0x14eb: v14eb = ADD v14af, v14e8(0x44)
    0x14ec: MSTORE v14eb, v14c7(0x436f6e747261637420616c726561647920696e697469616c697a656400000000)
    0x14ee: v14ee = MLOAD v14ac(0x40)
    0x14f2: v14f2(0x0) = SUB v14af, v14ee
    0x14f3: v14f3(0x64) = CONST 
    0x14f5: v14f5(0x64) = ADD v14f3(0x64), v14f2(0x0)
    0x14f7: REVERT v14ee, v14f5(0x64)

    Begin block 0x14f8
    prev=[0x14a0], succ=[0x1507, 0x1553]
    =================================
    0x14f9: v14f9(0x1) = CONST 
    0x14fb: v14fb(0x1) = CONST 
    0x14fd: v14fd(0xa0) = CONST 
    0x14ff: v14ff(0x10000000000000000000000000000000000000000) = SHL v14fd(0xa0), v14fb(0x1)
    0x1500: v1500(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14ff(0x10000000000000000000000000000000000000000), v14f9(0x1)
    0x1502: v1502 = AND v651, v1500(0xffffffffffffffffffffffffffffffffffffffff)
    0x1503: v1503(0x1553) = CONST 
    0x1506: JUMPI v1503(0x1553), v1502

    Begin block 0x1507
    prev=[0x14f8], succ=[]
    =================================
    0x1507: v1507(0x40) = CONST 
    0x150a: v150a = MLOAD v1507(0x40)
    0x150b: v150b(0x461bcd) = CONST 
    0x150f: v150f(0xe5) = CONST 
    0x1511: v1511(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v150f(0xe5), v150b(0x461bcd)
    0x1513: MSTORE v150a, v1511(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1514: v1514(0x20) = CONST 
    0x1516: v1516(0x4) = CONST 
    0x1519: v1519 = ADD v150a, v1516(0x4)
    0x151a: MSTORE v1519, v1514(0x20)
    0x151b: v151b(0x1e) = CONST 
    0x151d: v151d(0x24) = CONST 
    0x1520: v1520 = ADD v150a, v151d(0x24)
    0x1521: MSTORE v1520, v151b(0x1e)
    0x1522: v1522(0x4f776e6572206d757374206e6f74206265206e756c6c20616464726573730000) = CONST 
    0x1543: v1543(0x44) = CONST 
    0x1546: v1546 = ADD v150a, v1543(0x44)
    0x1547: MSTORE v1546, v1522(0x4f776e6572206d757374206e6f74206265206e756c6c20616464726573730000)
    0x1549: v1549 = MLOAD v1507(0x40)
    0x154d: v154d(0x0) = SUB v150a, v1549
    0x154e: v154e(0x64) = CONST 
    0x1550: v1550(0x64) = ADD v154e(0x64), v154d(0x0)
    0x1552: REVERT v1549, v1550(0x64)

    Begin block 0x1553
    prev=[0x14f8], succ=[0x1562, 0x1598]
    =================================
    0x1554: v1554(0x1) = CONST 
    0x1556: v1556(0x1) = CONST 
    0x1558: v1558(0xa0) = CONST 
    0x155a: v155a(0x10000000000000000000000000000000000000000) = SHL v1558(0xa0), v1556(0x1)
    0x155b: v155b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v155a(0x10000000000000000000000000000000000000000), v1554(0x1)
    0x155d: v155d = AND v657, v155b(0xffffffffffffffffffffffffffffffffffffffff)
    0x155e: v155e(0x1598) = CONST 
    0x1561: JUMPI v155e(0x1598), v155d

    Begin block 0x1562
    prev=[0x1553], succ=[]
    =================================
    0x1562: v1562(0x40) = CONST 
    0x1564: v1564 = MLOAD v1562(0x40)
    0x1565: v1565(0x461bcd) = CONST 
    0x1569: v1569(0xe5) = CONST 
    0x156b: v156b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1569(0xe5), v1565(0x461bcd)
    0x156d: MSTORE v1564, v156b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x156e: v156e(0x4) = CONST 
    0x1570: v1570 = ADD v156e(0x4), v1564
    0x1573: v1573(0x20) = CONST 
    0x1575: v1575 = ADD v1573(0x20), v1570
    0x1578: v1578(0x20) = SUB v1575, v1570
    0x157a: MSTORE v1570, v1578(0x20)
    0x157b: v157b(0x28) = CONST 
    0x157e: MSTORE v1575, v157b(0x28)
    0x157f: v157f(0x20) = CONST 
    0x1581: v1581 = ADD v157f(0x20), v1575
    0x1583: v1583(0x3b26) = CONST 
    0x1586: v1586(0x28) = CONST 
    0x1589: CODECOPY v1581, v1583(0x3b26), v1586(0x28)
    0x158a: v158a(0x40) = CONST 
    0x158c: v158c = ADD v158a(0x40), v1581
    0x1590: v1590(0x40) = CONST 
    0x1592: v1592 = MLOAD v1590(0x40)
    0x1595: v1595(0x84) = SUB v158c, v1592
    0x1597: REVERT v1592, v1595(0x84)

    Begin block 0x1598
    prev=[0x1553], succ=[0x3eca]
    =================================
    0x1599: v1599(0x3) = CONST 
    0x159c: v159c = SLOAD v1599(0x3)
    0x159d: v159d(0x1) = CONST 
    0x159f: v159f(0x1) = CONST 
    0x15a1: v15a1(0xa0) = CONST 
    0x15a3: v15a3(0x10000000000000000000000000000000000000000) = SHL v15a1(0xa0), v159f(0x1)
    0x15a4: v15a4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15a3(0x10000000000000000000000000000000000000000), v159d(0x1)
    0x15a7: v15a7 = AND v15a4(0xffffffffffffffffffffffffffffffffffffffff), v651
    0x15a8: v15a8(0x1) = CONST 
    0x15aa: v15aa(0x1) = CONST 
    0x15ac: v15ac(0xa0) = CONST 
    0x15ae: v15ae(0x10000000000000000000000000000000000000000) = SHL v15ac(0xa0), v15aa(0x1)
    0x15af: v15af(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15ae(0x10000000000000000000000000000000000000000), v15a8(0x1)
    0x15b0: v15b0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v15af(0xffffffffffffffffffffffffffffffffffffffff)
    0x15b3: v15b3 = AND v15b0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v159c
    0x15b4: v15b4 = OR v15b3, v15a7
    0x15b7: SSTORE v1599(0x3), v15b4
    0x15b8: v15b8(0x4) = CONST 
    0x15bb: v15bb = SLOAD v15b8(0x4)
    0x15bf: v15bf = AND v15a4(0xffffffffffffffffffffffffffffffffffffffff), v657
    0x15c1: v15c1 = AND v15bb, v15b0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x15c2: v15c2 = OR v15c1, v15bf
    0x15c4: SSTORE v15b8(0x4), v15c2
    0x15c5: v15c5(0x1) = CONST 
    0x15c8: v15c8 = SLOAD v15c5(0x1)
    0x15c9: v15c9(0xff) = CONST 
    0x15cb: v15cb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v15c9(0xff)
    0x15cc: v15cc = AND v15cb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v15c8
    0x15ce: v15ce = OR v15c5(0x1), v15cc
    0x15d0: SSTORE v15c5(0x1), v15ce
    0x15d1: JUMP v62f(0x3eca)

    Begin block 0x3eca
    prev=[0x1598], succ=[]
    =================================
    0x3ecb: STOP 

}

function balanceOfBatch(address[],uint256[])() public {
    Begin block 0x65c
    prev=[], succ=[0x66e, 0x672]
    =================================
    0x65d: v65d(0x77f) = CONST 
    0x660: v660(0x4) = CONST 
    0x663: v663 = CALLDATASIZE 
    0x664: v664 = SUB v663, v660(0x4)
    0x665: v665(0x40) = CONST 
    0x668: v668 = LT v664, v665(0x40)
    0x669: v669 = ISZERO v668
    0x66a: v66a(0x672) = CONST 
    0x66d: JUMPI v66a(0x672), v669

    Begin block 0x66e
    prev=[0x65c], succ=[]
    =================================
    0x66e: v66e(0x0) = CONST 
    0x671: REVERT v66e(0x0), v66e(0x0)

    Begin block 0x672
    prev=[0x65c], succ=[0x688, 0x68c]
    =================================
    0x674: v674 = ADD v660(0x4), v664
    0x676: v676(0x20) = CONST 
    0x679: v679(0x24) = ADD v660(0x4), v676(0x20)
    0x67b: v67b = CALLDATALOAD v660(0x4)
    0x67c: v67c(0x1) = CONST 
    0x67e: v67e(0x20) = CONST 
    0x680: v680(0x100000000) = SHL v67e(0x20), v67c(0x1)
    0x682: v682 = GT v67b, v680(0x100000000)
    0x683: v683 = ISZERO v682
    0x684: v684(0x68c) = CONST 
    0x687: JUMPI v684(0x68c), v683

    Begin block 0x688
    prev=[0x672], succ=[]
    =================================
    0x688: v688(0x0) = CONST 
    0x68b: REVERT v688(0x0), v688(0x0)

    Begin block 0x68c
    prev=[0x672], succ=[0x69a, 0x69e]
    =================================
    0x68e: v68e = ADD v660(0x4), v67b
    0x690: v690(0x20) = CONST 
    0x693: v693 = ADD v68e, v690(0x20)
    0x694: v694 = GT v693, v674
    0x695: v695 = ISZERO v694
    0x696: v696(0x69e) = CONST 
    0x699: JUMPI v696(0x69e), v695

    Begin block 0x69a
    prev=[0x68c], succ=[]
    =================================
    0x69a: v69a(0x0) = CONST 
    0x69d: REVERT v69a(0x0), v69a(0x0)

    Begin block 0x69e
    prev=[0x68c], succ=[0x6bb, 0x6bf]
    =================================
    0x6a0: v6a0 = CALLDATALOAD v68e
    0x6a2: v6a2(0x20) = CONST 
    0x6a4: v6a4 = ADD v6a2(0x20), v68e
    0x6a7: v6a7(0x20) = CONST 
    0x6aa: v6aa = MUL v6a0, v6a7(0x20)
    0x6ac: v6ac = ADD v6a4, v6aa
    0x6ad: v6ad = GT v6ac, v674
    0x6ae: v6ae(0x1) = CONST 
    0x6b0: v6b0(0x20) = CONST 
    0x6b2: v6b2(0x100000000) = SHL v6b0(0x20), v6ae(0x1)
    0x6b4: v6b4 = GT v6a0, v6b2(0x100000000)
    0x6b5: v6b5 = OR v6b4, v6ad
    0x6b6: v6b6 = ISZERO v6b5
    0x6b7: v6b7(0x6bf) = CONST 
    0x6ba: JUMPI v6b7(0x6bf), v6b6

    Begin block 0x6bb
    prev=[0x69e], succ=[]
    =================================
    0x6bb: v6bb(0x0) = CONST 
    0x6be: REVERT v6bb(0x0), v6bb(0x0)

    Begin block 0x6bf
    prev=[0x69e], succ=[0x70a, 0x70e]
    =================================
    0x6c4: v6c4(0x20) = CONST 
    0x6c6: v6c6 = MUL v6c4(0x20), v6a0
    0x6c7: v6c7(0x20) = CONST 
    0x6c9: v6c9 = ADD v6c7(0x20), v6c6
    0x6ca: v6ca(0x40) = CONST 
    0x6cc: v6cc = MLOAD v6ca(0x40)
    0x6cf: v6cf = ADD v6cc, v6c9
    0x6d0: v6d0(0x40) = CONST 
    0x6d2: MSTORE v6d0(0x40), v6cf
    0x6da: MSTORE v6cc, v6a0
    0x6db: v6db(0x20) = CONST 
    0x6dd: v6dd = ADD v6db(0x20), v6cc
    0x6e0: v6e0(0x20) = CONST 
    0x6e2: v6e2 = MUL v6e0(0x20), v6a0
    0x6e6: CALLDATACOPY v6dd, v6a4, v6e2
    0x6e7: v6e7(0x0) = CONST 
    0x6ea: v6ea = ADD v6dd, v6e2
    0x6ee: MSTORE v6ea, v6e7(0x0)
    0x6f4: v6f4(0x20) = CONST 
    0x6f7: v6f7(0x44) = ADD v679(0x24), v6f4(0x20)
    0x6fa: v6fa = CALLDATALOAD v679(0x24)
    0x6fe: v6fe(0x1) = CONST 
    0x700: v700(0x20) = CONST 
    0x702: v702(0x100000000) = SHL v700(0x20), v6fe(0x1)
    0x704: v704 = GT v6fa, v702(0x100000000)
    0x705: v705 = ISZERO v704
    0x706: v706(0x70e) = CONST 
    0x709: JUMPI v706(0x70e), v705

    Begin block 0x70a
    prev=[0x6bf], succ=[]
    =================================
    0x70a: v70a(0x0) = CONST 
    0x70d: REVERT v70a(0x0), v70a(0x0)

    Begin block 0x70e
    prev=[0x6bf], succ=[0x71c, 0x720]
    =================================
    0x710: v710 = ADD v660(0x4), v6fa
    0x712: v712(0x20) = CONST 
    0x715: v715 = ADD v710, v712(0x20)
    0x716: v716 = GT v715, v674
    0x717: v717 = ISZERO v716
    0x718: v718(0x720) = CONST 
    0x71b: JUMPI v718(0x720), v717

    Begin block 0x71c
    prev=[0x70e], succ=[]
    =================================
    0x71c: v71c(0x0) = CONST 
    0x71f: REVERT v71c(0x0), v71c(0x0)

    Begin block 0x720
    prev=[0x70e], succ=[0x73d, 0x741]
    =================================
    0x722: v722 = CALLDATALOAD v710
    0x724: v724(0x20) = CONST 
    0x726: v726 = ADD v724(0x20), v710
    0x729: v729(0x20) = CONST 
    0x72c: v72c = MUL v722, v729(0x20)
    0x72e: v72e = ADD v726, v72c
    0x72f: v72f = GT v72e, v674
    0x730: v730(0x1) = CONST 
    0x732: v732(0x20) = CONST 
    0x734: v734(0x100000000) = SHL v732(0x20), v730(0x1)
    0x736: v736 = GT v722, v734(0x100000000)
    0x737: v737 = OR v736, v72f
    0x738: v738 = ISZERO v737
    0x739: v739(0x741) = CONST 
    0x73c: JUMPI v739(0x741), v738

    Begin block 0x73d
    prev=[0x720], succ=[]
    =================================
    0x73d: v73d(0x0) = CONST 
    0x740: REVERT v73d(0x0), v73d(0x0)

    Begin block 0x741
    prev=[0x720], succ=[0x15d2]
    =================================
    0x746: v746(0x20) = CONST 
    0x748: v748 = MUL v746(0x20), v722
    0x749: v749(0x20) = CONST 
    0x74b: v74b = ADD v749(0x20), v748
    0x74c: v74c(0x40) = CONST 
    0x74e: v74e = MLOAD v74c(0x40)
    0x751: v751 = ADD v74e, v74b
    0x752: v752(0x40) = CONST 
    0x754: MSTORE v752(0x40), v751
    0x75c: MSTORE v74e, v722
    0x75d: v75d(0x20) = CONST 
    0x75f: v75f = ADD v75d(0x20), v74e
    0x762: v762(0x20) = CONST 
    0x764: v764 = MUL v762(0x20), v722
    0x768: CALLDATACOPY v75f, v726, v764
    0x769: v769(0x0) = CONST 
    0x76c: v76c = ADD v75f, v764
    0x770: MSTORE v76c, v769(0x0)
    0x775: v775(0x15d2) = CONST 
    0x77e: JUMP v775(0x15d2)

    Begin block 0x15d2
    prev=[0x741], succ=[0x15de, 0x1614]
    =================================
    0x15d3: v15d3(0x60) = CONST 
    0x15d6: v15d6 = MLOAD v74e
    0x15d8: v15d8 = MLOAD v6cc
    0x15d9: v15d9 = EQ v15d8, v15d6
    0x15da: v15da(0x1614) = CONST 
    0x15dd: JUMPI v15da(0x1614), v15d9

    Begin block 0x15de
    prev=[0x15d2], succ=[]
    =================================
    0x15de: v15de(0x40) = CONST 
    0x15e0: v15e0 = MLOAD v15de(0x40)
    0x15e1: v15e1(0x461bcd) = CONST 
    0x15e5: v15e5(0xe5) = CONST 
    0x15e7: v15e7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15e5(0xe5), v15e1(0x461bcd)
    0x15e9: MSTORE v15e0, v15e7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15ea: v15ea(0x4) = CONST 
    0x15ec: v15ec = ADD v15ea(0x4), v15e0
    0x15ef: v15ef(0x20) = CONST 
    0x15f1: v15f1 = ADD v15ef(0x20), v15ec
    0x15f4: v15f4(0x20) = SUB v15f1, v15ec
    0x15f6: MSTORE v15ec, v15f4(0x20)
    0x15f7: v15f7(0x24) = CONST 
    0x15fa: MSTORE v15f1, v15f7(0x24)
    0x15fb: v15fb(0x20) = CONST 
    0x15fd: v15fd = ADD v15fb(0x20), v15f1
    0x15ff: v15ff(0x3b71) = CONST 
    0x1602: v1602(0x24) = CONST 
    0x1605: CODECOPY v15fd, v15ff(0x3b71), v1602(0x24)
    0x1606: v1606(0x40) = CONST 
    0x1608: v1608 = ADD v1606(0x40), v15fd
    0x160c: v160c(0x40) = CONST 
    0x160e: v160e = MLOAD v160c(0x40)
    0x1611: v1611(0x84) = SUB v1608, v160e
    0x1613: REVERT v160e, v1611(0x84)

    Begin block 0x1614
    prev=[0x15d2], succ=[0x162a, 0x162e]
    =================================
    0x1615: v1615(0x0) = CONST 
    0x1618: v1618 = MLOAD v6cc
    0x1619: v1619(0xffffffffffffffff) = CONST 
    0x1623: v1623 = GT v1618, v1619(0xffffffffffffffff)
    0x1625: v1625 = ISZERO v1623
    0x1626: v1626(0x162e) = CONST 
    0x1629: JUMPI v1626(0x162e), v1625

    Begin block 0x162a
    prev=[0x1614], succ=[]
    =================================
    0x162a: v162a(0x0) = CONST 
    0x162d: REVERT v162a(0x0), v162a(0x0)

    Begin block 0x162e
    prev=[0x1614], succ=[0x1658, 0x1649]
    =================================
    0x1630: v1630(0x40) = CONST 
    0x1632: v1632 = MLOAD v1630(0x40)
    0x1636: MSTORE v1632, v1618
    0x1638: v1638(0x20) = CONST 
    0x163a: v163a = MUL v1638(0x20), v1618
    0x163b: v163b(0x20) = CONST 
    0x163d: v163d = ADD v163b(0x20), v163a
    0x163f: v163f = ADD v1632, v163d
    0x1640: v1640(0x40) = CONST 
    0x1642: MSTORE v1640(0x40), v163f
    0x1644: v1644 = ISZERO v1618
    0x1645: v1645(0x1658) = CONST 
    0x1648: JUMPI v1645(0x1658), v1644

    Begin block 0x1658
    prev=[0x162e, 0x1649], succ=[0x165e]
    =================================
    0x165c: v165c(0x0) = CONST 

    Begin block 0x165e
    prev=[0x1658, 0x16a3], succ=[0x1668, 0x16b6]
    =================================
    0x165e_0x0: v165e_0 = PHI v165c(0x0), v16b1
    0x1660: v1660 = MLOAD v6cc
    0x1662: v1662 = LT v165e_0, v1660
    0x1663: v1663 = ISZERO v1662
    0x1664: v1664(0x16b6) = CONST 
    0x1667: JUMPI v1664(0x16b6), v1663

    Begin block 0x1668
    prev=[0x165e], succ=[0x1675, 0x1676]
    =================================
    0x1668: v1668(0x1697) = CONST 
    0x1668_0x0: v1668_0 = PHI v165c(0x0), v16b1
    0x166e: v166e = MLOAD v6cc
    0x1670: v1670 = LT v1668_0, v166e
    0x1671: v1671(0x1676) = CONST 
    0x1674: JUMPI v1671(0x1676), v1670

    Begin block 0x1675
    prev=[0x1668], succ=[]
    =================================
    0x1675: THROW 

    Begin block 0x1676
    prev=[0x1668], succ=[0x1689, 0x168a]
    =================================
    0x1676_0x0: v1676_0 = PHI v165c(0x0), v16b1
    0x1676_0x3: v1676_3 = PHI v165c(0x0), v16b1
    0x1677: v1677(0x20) = CONST 
    0x1679: v1679 = MUL v1677(0x20), v1676_0
    0x167a: v167a(0x20) = CONST 
    0x167c: v167c = ADD v167a(0x20), v1679
    0x167d: v167d = ADD v167c, v6cc
    0x167e: v167e = MLOAD v167d
    0x1682: v1682 = MLOAD v74e
    0x1684: v1684 = LT v1676_3, v1682
    0x1685: v1685(0x168a) = CONST 
    0x1688: JUMPI v1685(0x168a), v1684

    Begin block 0x1689
    prev=[0x1676], succ=[]
    =================================
    0x1689: THROW 

    Begin block 0x168a
    prev=[0x1676], succ=[0xe690x65c]
    =================================
    0x168a_0x0: v168a_0 = PHI v165c(0x0), v16b1
    0x168b: v168b(0x20) = CONST 
    0x168d: v168d = MUL v168b(0x20), v168a_0
    0x168e: v168e(0x20) = CONST 
    0x1690: v1690 = ADD v168e(0x20), v168d
    0x1691: v1691 = ADD v1690, v74e
    0x1692: v1692 = MLOAD v1691
    0x1693: v1693(0xe69) = CONST 
    0x1696: JUMP v1693(0xe69)

    Begin block 0xe690x65c
    prev=[0x168a], succ=[0xe750x65c]
    =================================
    0xe6a0x65c: v65ce6a(0x0) = CONST 
    0xe6c0x65c: v65ce6c(0xe75) = CONST 
    0xe710x65c: v65ce71(0x2497) = CONST 
    0xe740x65c: v65ce74_0 = CALLPRIVATE v65ce71(0x2497), v1692, v167e, v65ce6c(0xe75)

    Begin block 0xe750x65c
    prev=[0xe690x65c], succ=[0xe7b0x65c, 0xe820x65c]
    =================================
    0xe760x65c: v65ce76 = ISZERO v65ce74_0
    0xe770x65c: v65ce77(0xe82) = CONST 
    0xe7a0x65c: JUMPI v65ce77(0xe82), v65ce76

    Begin block 0xe7b0x65c
    prev=[0xe750x65c], succ=[0x421b0x65c]
    =================================
    0xe7c0x65c: v65ce7c(0x1) = CONST 
    0xe7e0x65c: v65ce7e(0x421b) = CONST 
    0xe810x65c: JUMP v65ce7e(0x421b)

    Begin block 0x421b0x65c
    prev=[0xe7b0x65c], succ=[0x1697]
    =================================
    0x42200x65c: JUMP v1668(0x1697)

    Begin block 0x1697
    prev=[0xe860x65c, 0x421b0x65c], succ=[0x16a2, 0x16a3]
    =================================
    0x1697_0x1: v1697_1 = PHI v165c(0x0), v16b1
    0x169b: v169b = MLOAD v1632
    0x169d: v169d = LT v1697_1, v169b
    0x169e: v169e(0x16a3) = CONST 
    0x16a1: JUMPI v169e(0x16a3), v169d

    Begin block 0x16a2
    prev=[0x1697], succ=[]
    =================================
    0x16a2: THROW 

    Begin block 0x16a3
    prev=[0x1697], succ=[0x165e]
    =================================
    0x16a3_0x0: v16a3_0 = PHI v165c(0x0), v16b1
    0x16a3_0x2: v16a3_2 = PHI v65ce84(0x0), v65ce7c(0x1)
    0x16a3_0x3: v16a3_3 = PHI v165c(0x0), v16b1
    0x16a4: v16a4(0x20) = CONST 
    0x16a8: v16a8 = MUL v16a4(0x20), v16a3_0
    0x16ac: v16ac = ADD v16a8, v1632
    0x16ad: v16ad = ADD v16ac, v16a4(0x20)
    0x16ae: MSTORE v16ad, v16a3_2
    0x16af: v16af(0x1) = CONST 
    0x16b1: v16b1 = ADD v16af(0x1), v16a3_3
    0x16b2: v16b2(0x165e) = CONST 
    0x16b5: JUMP v16b2(0x165e)

    Begin block 0xe820x65c
    prev=[0xe750x65c], succ=[0xe860x65c]
    =================================
    0xe840x65c: v65ce84(0x0) = CONST 

    Begin block 0xe860x65c
    prev=[0xe820x65c], succ=[0x1697]
    =================================
    0xe8b0x65c: JUMP v1668(0x1697)

    Begin block 0x16b6
    prev=[0x165e], succ=[0x77f0x65c]
    =================================
    0x16bd: JUMP v65d(0x77f)

    Begin block 0x77f0x65c
    prev=[0x16b6], succ=[0x7a30x65c]
    =================================
    0x7800x65c: v65c780(0x40) = CONST 
    0x7830x65c: v65c783 = MLOAD v65c780(0x40)
    0x7840x65c: v65c784(0x20) = CONST 
    0x7880x65c: MSTORE v65c783, v65c784(0x20)
    0x78a0x65c: v65c78a = MLOAD v1632
    0x78d0x65c: v65c78d = ADD v65c783, v65c784(0x20)
    0x78e0x65c: MSTORE v65c78d, v65c78a
    0x7900x65c: v65c790 = MLOAD v1632
    0x7970x65c: v65c797 = ADD v65c783, v65c780(0x40)
    0x79b0x65c: v65c79b = ADD v65c784(0x20), v1632
    0x79d0x65c: v65c79d = MUL v65c790, v65c784(0x20)
    0x7a10x65c: v65c7a1(0x0) = CONST 

    Begin block 0x7a30x65c
    prev=[0x7ac0x65c, 0x77f0x65c], succ=[0x7ac0x65c, 0x7bb0x65c]
    =================================
    0x7a30x65c_0x0: v7a365c_0 = PHI v65c7b6, v65c7a1(0x0)
    0x7a60x65c: v65c7a6 = LT v7a365c_0, v65c79d
    0x7a70x65c: v65c7a7 = ISZERO v65c7a6
    0x7a80x65c: v65c7a8(0x7bb) = CONST 
    0x7ab0x65c: JUMPI v65c7a8(0x7bb), v65c7a7

    Begin block 0x7ac0x65c
    prev=[0x7a30x65c], succ=[0x7a30x65c]
    =================================
    0x7ac0x65c_0x0: v7ac65c_0 = PHI v65c7b6, v65c7a1(0x0)
    0x7ae0x65c: v65c7ae = ADD v7ac65c_0, v65c79b
    0x7af0x65c: v65c7af = MLOAD v65c7ae
    0x7b20x65c: v65c7b2 = ADD v7ac65c_0, v65c797
    0x7b30x65c: MSTORE v65c7b2, v65c7af
    0x7b40x65c: v65c7b4(0x20) = CONST 
    0x7b60x65c: v65c7b6 = ADD v65c7b4(0x20), v7ac65c_0
    0x7b70x65c: v65c7b7(0x7a3) = CONST 
    0x7ba0x65c: JUMP v65c7b7(0x7a3)

    Begin block 0x7bb0x65c
    prev=[0x7a30x65c], succ=[]
    =================================
    0x7c20x65c: v65c7c2 = ADD v65c79d, v65c797
    0x7c70x65c: v65c7c7(0x40) = CONST 
    0x7c90x65c: v65c7c9 = MLOAD v65c7c7(0x40)
    0x7cc0x65c: v65c7cc = SUB v65c7c2, v65c7c9
    0x7ce0x65c: RETURN v65c7c9, v65c7cc

    Begin block 0x1649
    prev=[0x162e], succ=[0x1658]
    =================================
    0x164a: v164a(0x20) = CONST 
    0x164c: v164c = ADD v164a(0x20), v1632
    0x164d: v164d(0x20) = CONST 
    0x1650: v1650 = MUL v1618, v164d(0x20)
    0x1652: v1652 = CALLDATASIZE 
    0x1654: CALLDATACOPY v164c, v1652, v1650
    0x1655: v1655 = ADD v1650, v164c

}

function transferOwner(address)() public {
    Begin block 0x7cf
    prev=[], succ=[0x7e1, 0x7e5]
    =================================
    0x7d0: v7d0(0x3eeb) = CONST 
    0x7d3: v7d3(0x4) = CONST 
    0x7d6: v7d6 = CALLDATASIZE 
    0x7d7: v7d7 = SUB v7d6, v7d3(0x4)
    0x7d8: v7d8(0x20) = CONST 
    0x7db: v7db = LT v7d7, v7d8(0x20)
    0x7dc: v7dc = ISZERO v7db
    0x7dd: v7dd(0x7e5) = CONST 
    0x7e0: JUMPI v7dd(0x7e5), v7dc

    Begin block 0x7e1
    prev=[0x7cf], succ=[]
    =================================
    0x7e1: v7e1(0x0) = CONST 
    0x7e4: REVERT v7e1(0x0), v7e1(0x0)

    Begin block 0x7e5
    prev=[0x7cf], succ=[0x16be]
    =================================
    0x7e7: v7e7 = CALLDATALOAD v7d3(0x4)
    0x7e8: v7e8(0x1) = CONST 
    0x7ea: v7ea(0x1) = CONST 
    0x7ec: v7ec(0xa0) = CONST 
    0x7ee: v7ee(0x10000000000000000000000000000000000000000) = SHL v7ec(0xa0), v7ea(0x1)
    0x7ef: v7ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7ee(0x10000000000000000000000000000000000000000), v7e8(0x1)
    0x7f0: v7f0 = AND v7ef(0xffffffffffffffffffffffffffffffffffffffff), v7e7
    0x7f1: v7f1(0x16be) = CONST 
    0x7f4: JUMP v7f1(0x16be)

    Begin block 0x16be
    prev=[0x7e5], succ=[0x16d1, 0x170d]
    =================================
    0x16bf: v16bf(0x3) = CONST 
    0x16c1: v16c1 = SLOAD v16bf(0x3)
    0x16c2: v16c2(0x1) = CONST 
    0x16c4: v16c4(0x1) = CONST 
    0x16c6: v16c6(0xa0) = CONST 
    0x16c8: v16c8(0x10000000000000000000000000000000000000000) = SHL v16c6(0xa0), v16c4(0x1)
    0x16c9: v16c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16c8(0x10000000000000000000000000000000000000000), v16c2(0x1)
    0x16ca: v16ca = AND v16c9(0xffffffffffffffffffffffffffffffffffffffff), v16c1
    0x16cb: v16cb = CALLER 
    0x16cc: v16cc = EQ v16cb, v16ca
    0x16cd: v16cd(0x170d) = CONST 
    0x16d0: JUMPI v16cd(0x170d), v16cc

    Begin block 0x16d1
    prev=[0x16be], succ=[]
    =================================
    0x16d1: v16d1(0x40) = CONST 
    0x16d4: v16d4 = MLOAD v16d1(0x40)
    0x16d5: v16d5(0x461bcd) = CONST 
    0x16d9: v16d9(0xe5) = CONST 
    0x16db: v16db(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v16d9(0xe5), v16d5(0x461bcd)
    0x16dd: MSTORE v16d4, v16db(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x16de: v16de(0x20) = CONST 
    0x16e0: v16e0(0x4) = CONST 
    0x16e3: v16e3 = ADD v16d4, v16e0(0x4)
    0x16e4: MSTORE v16e3, v16de(0x20)
    0x16e5: v16e5(0xd) = CONST 
    0x16e7: v16e7(0x24) = CONST 
    0x16ea: v16ea = ADD v16d4, v16e7(0x24)
    0x16eb: MSTORE v16ea, v16e5(0xd)
    0x16ec: v16ec(0x26bab9ba1031329037bbb732b9) = CONST 
    0x16fa: v16fa(0x99) = CONST 
    0x16fc: v16fc(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v16fa(0x99), v16ec(0x26bab9ba1031329037bbb732b9)
    0x16fd: v16fd(0x44) = CONST 
    0x1700: v1700 = ADD v16d4, v16fd(0x44)
    0x1701: MSTORE v1700, v16fc(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1703: v1703 = MLOAD v16d1(0x40)
    0x1707: v1707(0x0) = SUB v16d4, v1703
    0x1708: v1708(0x64) = CONST 
    0x170a: v170a(0x64) = ADD v1708(0x64), v1707(0x0)
    0x170c: REVERT v1703, v170a(0x64)

    Begin block 0x170d
    prev=[0x16be], succ=[0x171c, 0x1752]
    =================================
    0x170e: v170e(0x1) = CONST 
    0x1710: v1710(0x1) = CONST 
    0x1712: v1712(0xa0) = CONST 
    0x1714: v1714(0x10000000000000000000000000000000000000000) = SHL v1712(0xa0), v1710(0x1)
    0x1715: v1715(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1714(0x10000000000000000000000000000000000000000), v170e(0x1)
    0x1717: v1717 = AND v7f0, v1715(0xffffffffffffffffffffffffffffffffffffffff)
    0x1718: v1718(0x1752) = CONST 
    0x171b: JUMPI v1718(0x1752), v1717

    Begin block 0x171c
    prev=[0x170d], succ=[]
    =================================
    0x171c: v171c(0x40) = CONST 
    0x171e: v171e = MLOAD v171c(0x40)
    0x171f: v171f(0x461bcd) = CONST 
    0x1723: v1723(0xe5) = CONST 
    0x1725: v1725(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1723(0xe5), v171f(0x461bcd)
    0x1727: MSTORE v171e, v1725(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1728: v1728(0x4) = CONST 
    0x172a: v172a = ADD v1728(0x4), v171e
    0x172d: v172d(0x20) = CONST 
    0x172f: v172f = ADD v172d(0x20), v172a
    0x1732: v1732(0x20) = SUB v172f, v172a
    0x1734: MSTORE v172a, v1732(0x20)
    0x1735: v1735(0x22) = CONST 
    0x1738: MSTORE v172f, v1735(0x22)
    0x1739: v1739(0x20) = CONST 
    0x173b: v173b = ADD v1739(0x20), v172f
    0x173d: v173d(0x3bbf) = CONST 
    0x1740: v1740(0x22) = CONST 
    0x1743: CODECOPY v173b, v173d(0x3bbf), v1740(0x22)
    0x1744: v1744(0x40) = CONST 
    0x1746: v1746 = ADD v1744(0x40), v173b
    0x174a: v174a(0x40) = CONST 
    0x174c: v174c = MLOAD v174a(0x40)
    0x174f: v174f(0x84) = SUB v1746, v174c
    0x1751: REVERT v174c, v174f(0x84)

    Begin block 0x1752
    prev=[0x170d], succ=[0x3eeb]
    =================================
    0x1753: v1753(0x3) = CONST 
    0x1755: v1755 = SLOAD v1753(0x3)
    0x1756: v1756(0x40) = CONST 
    0x1758: v1758 = MLOAD v1756(0x40)
    0x1759: v1759(0x1) = CONST 
    0x175b: v175b(0x1) = CONST 
    0x175d: v175d(0xa0) = CONST 
    0x175f: v175f(0x10000000000000000000000000000000000000000) = SHL v175d(0xa0), v175b(0x1)
    0x1760: v1760(0xffffffffffffffffffffffffffffffffffffffff) = SUB v175f(0x10000000000000000000000000000000000000000), v1759(0x1)
    0x1763: v1763 = AND v7f0, v1760(0xffffffffffffffffffffffffffffffffffffffff)
    0x1765: v1765 = AND v1755, v1760(0xffffffffffffffffffffffffffffffffffffffff)
    0x1767: v1767(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1789: v1789(0x0) = CONST 
    0x178c: LOG3 v1758, v1789(0x0), v1767(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1765, v1763
    0x178d: v178d(0x3) = CONST 
    0x1790: v1790 = SLOAD v178d(0x3)
    0x1791: v1791(0x1) = CONST 
    0x1793: v1793(0x1) = CONST 
    0x1795: v1795(0xa0) = CONST 
    0x1797: v1797(0x10000000000000000000000000000000000000000) = SHL v1795(0xa0), v1793(0x1)
    0x1798: v1798(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1797(0x10000000000000000000000000000000000000000), v1791(0x1)
    0x1799: v1799(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1798(0xffffffffffffffffffffffffffffffffffffffff)
    0x179a: v179a = AND v1799(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1790
    0x179b: v179b(0x1) = CONST 
    0x179d: v179d(0x1) = CONST 
    0x179f: v179f(0xa0) = CONST 
    0x17a1: v17a1(0x10000000000000000000000000000000000000000) = SHL v179f(0xa0), v179d(0x1)
    0x17a2: v17a2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17a1(0x10000000000000000000000000000000000000000), v179b(0x1)
    0x17a6: v17a6 = AND v17a2(0xffffffffffffffffffffffffffffffffffffffff), v7f0
    0x17aa: v17aa = OR v17a6, v179a
    0x17ac: SSTORE v178d(0x3), v17aa
    0x17ad: JUMP v7d0(0x3eeb)

    Begin block 0x3eeb
    prev=[0x1752], succ=[]
    =================================
    0x3eec: STOP 

}

function burnQuasar(address,uint256)() public {
    Begin block 0x7f5
    prev=[], succ=[0x807, 0x80b]
    =================================
    0x7f6: v7f6(0x3f0c) = CONST 
    0x7f9: v7f9(0x4) = CONST 
    0x7fc: v7fc = CALLDATASIZE 
    0x7fd: v7fd = SUB v7fc, v7f9(0x4)
    0x7fe: v7fe(0x40) = CONST 
    0x801: v801 = LT v7fd, v7fe(0x40)
    0x802: v802 = ISZERO v801
    0x803: v803(0x80b) = CONST 
    0x806: JUMPI v803(0x80b), v802

    Begin block 0x807
    prev=[0x7f5], succ=[]
    =================================
    0x807: v807(0x0) = CONST 
    0x80a: REVERT v807(0x0), v807(0x0)

    Begin block 0x80b
    prev=[0x7f5], succ=[0x17ae]
    =================================
    0x80d: v80d(0x1) = CONST 
    0x80f: v80f(0x1) = CONST 
    0x811: v811(0xa0) = CONST 
    0x813: v813(0x10000000000000000000000000000000000000000) = SHL v811(0xa0), v80f(0x1)
    0x814: v814(0xffffffffffffffffffffffffffffffffffffffff) = SUB v813(0x10000000000000000000000000000000000000000), v80d(0x1)
    0x816: v816 = CALLDATALOAD v7f9(0x4)
    0x817: v817 = AND v816, v814(0xffffffffffffffffffffffffffffffffffffffff)
    0x819: v819(0x20) = CONST 
    0x81b: v81b(0x24) = ADD v819(0x20), v7f9(0x4)
    0x81c: v81c = CALLDATALOAD v81b(0x24)
    0x81d: v81d(0x17ae) = CONST 
    0x820: JUMP v81d(0x17ae)

    Begin block 0x17ae
    prev=[0x80b], succ=[0x17c6, 0x1803]
    =================================
    0x17af: v17af = CALLER 
    0x17b0: v17b0(0x0) = CONST 
    0x17b4: MSTORE v17b0(0x0), v17af
    0x17b5: v17b5(0x5) = CONST 
    0x17b7: v17b7(0x20) = CONST 
    0x17b9: MSTORE v17b7(0x20), v17b5(0x5)
    0x17ba: v17ba(0x40) = CONST 
    0x17bd: v17bd = SHA3 v17b0(0x0), v17ba(0x40)
    0x17be: v17be = SLOAD v17bd
    0x17bf: v17bf(0xff) = CONST 
    0x17c1: v17c1 = AND v17bf(0xff), v17be
    0x17c2: v17c2(0x1803) = CONST 
    0x17c5: JUMPI v17c2(0x1803), v17c1

    Begin block 0x17c6
    prev=[0x17ae], succ=[]
    =================================
    0x17c6: v17c6(0x40) = CONST 
    0x17c9: v17c9 = MLOAD v17c6(0x40)
    0x17ca: v17ca(0x461bcd) = CONST 
    0x17ce: v17ce(0xe5) = CONST 
    0x17d0: v17d0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17ce(0xe5), v17ca(0x461bcd)
    0x17d2: MSTORE v17c9, v17d0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17d3: v17d3(0x20) = CONST 
    0x17d5: v17d5(0x4) = CONST 
    0x17d8: v17d8 = ADD v17c9, v17d5(0x4)
    0x17d9: MSTORE v17d8, v17d3(0x20)
    0x17da: v17da(0xe) = CONST 
    0x17dc: v17dc(0x24) = CONST 
    0x17df: v17df = ADD v17c9, v17dc(0x24)
    0x17e0: MSTORE v17df, v17da(0xe)
    0x17e1: v17e1(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x17f0: v17f0(0x91) = CONST 
    0x17f2: v17f2(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v17f0(0x91), v17e1(0x36bab9ba1031329036b4b73a32b9)
    0x17f3: v17f3(0x44) = CONST 
    0x17f6: v17f6 = ADD v17c9, v17f3(0x44)
    0x17f7: MSTORE v17f6, v17f2(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x17f9: v17f9 = MLOAD v17c6(0x40)
    0x17fd: v17fd(0x0) = SUB v17c9, v17f9
    0x17fe: v17fe(0x64) = CONST 
    0x1800: v1800(0x64) = ADD v17fe(0x64), v17fd(0x0)
    0x1802: REVERT v17f9, v1800(0x64)

    Begin block 0x1803
    prev=[0x17ae], succ=[0x180d]
    =================================
    0x1804: v1804(0x180d) = CONST 
    0x1809: v1809(0x2497) = CONST 
    0x180c: v180c_0 = CALLPRIVATE v1809(0x2497), v81c, v817, v1804(0x180d)

    Begin block 0x180d
    prev=[0x1803], succ=[0x1812, 0x184e]
    =================================
    0x180e: v180e(0x184e) = CONST 
    0x1811: JUMPI v180e(0x184e), v180c_0

    Begin block 0x1812
    prev=[0x180d], succ=[]
    =================================
    0x1812: v1812(0x40) = CONST 
    0x1815: v1815 = MLOAD v1812(0x40)
    0x1816: v1816(0x461bcd) = CONST 
    0x181a: v181a(0xe5) = CONST 
    0x181c: v181c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v181a(0xe5), v1816(0x461bcd)
    0x181e: MSTORE v1815, v181c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x181f: v181f(0x20) = CONST 
    0x1821: v1821(0x4) = CONST 
    0x1824: v1824 = ADD v1815, v1821(0x4)
    0x1825: MSTORE v1824, v181f(0x20)
    0x1826: v1826(0xd) = CONST 
    0x1828: v1828(0x24) = CONST 
    0x182b: v182b = ADD v1815, v1828(0x24)
    0x182c: MSTORE v182b, v1826(0xd)
    0x182d: v182d(0x2737ba103a34329037bbb732b9) = CONST 
    0x183b: v183b(0x99) = CONST 
    0x183d: v183d(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v183b(0x99), v182d(0x2737ba103a34329037bbb732b9)
    0x183e: v183e(0x44) = CONST 
    0x1841: v1841 = ADD v1815, v183e(0x44)
    0x1842: MSTORE v1841, v183d(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1844: v1844 = MLOAD v1812(0x40)
    0x1848: v1848(0x0) = SUB v1815, v1844
    0x1849: v1849(0x64) = CONST 
    0x184b: v184b(0x64) = ADD v1849(0x64), v1848(0x0)
    0x184d: REVERT v1844, v184b(0x64)

    Begin block 0x184e
    prev=[0x180d], succ=[0x2c29]
    =================================
    0x184f: v184f(0x42f7) = CONST 
    0x1853: v1853(0x2c29) = CONST 
    0x1856: JUMP v1853(0x2c29)

    Begin block 0x2c29
    prev=[0x184e], succ=[0x42f7]
    =================================
    0x2c2a: v2c2a(0x0) = CONST 
    0x2c2e: MSTORE v2c2a(0x0), v81c
    0x2c2f: v2c2f(0xb) = CONST 
    0x2c31: v2c31(0x20) = CONST 
    0x2c33: MSTORE v2c31(0x20), v2c2f(0xb)
    0x2c34: v2c34(0x40) = CONST 
    0x2c38: v2c38 = SHA3 v2c2a(0x0), v2c34(0x40)
    0x2c3a: v2c3a = SLOAD v2c38
    0x2c3b: v2c3b(0x1) = CONST 
    0x2c3d: v2c3d(0x1) = CONST 
    0x2c3f: v2c3f(0xa0) = CONST 
    0x2c41: v2c41(0x10000000000000000000000000000000000000000) = SHL v2c3f(0xa0), v2c3d(0x1)
    0x2c42: v2c42(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c41(0x10000000000000000000000000000000000000000), v2c3b(0x1)
    0x2c43: v2c43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2c42(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c44: v2c44 = AND v2c43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2c3a
    0x2c46: SSTORE v2c38, v2c44
    0x2c47: v2c47(0x1) = CONST 
    0x2c4a: v2c4a = ADD v2c38, v2c47(0x1)
    0x2c4d: SSTORE v2c4a, v2c2a(0x0)
    0x2c4e: v2c4e(0x2) = CONST 
    0x2c50: v2c50 = ADD v2c4e(0x2), v2c38
    0x2c53: SSTORE v2c50, v2c2a(0x0)
    0x2c54: v2c54 = MLOAD v2c34(0x40)
    0x2c57: v2c57(0xbde0a9e22c5839cdde2897048c98e5ac02b30c945ac1c44d3fd76237ab021c) = CONST 
    0x2c78: LOG2 v2c54, v2c2a(0x0), v2c57(0xbde0a9e22c5839cdde2897048c98e5ac02b30c945ac1c44d3fd76237ab021c), v81c
    0x2c7a: JUMP v184f(0x42f7)

    Begin block 0x42f7
    prev=[0x2c29], succ=[0x3f0c]
    =================================
    0x42fa: JUMP v7f6(0x3f0c)

    Begin block 0x3f0c
    prev=[0x42f7], succ=[]
    =================================
    0x3f0d: STOP 

}

function baseURI()() public {
    Begin block 0x821
    prev=[], succ=[0x35c0x821]
    =================================
    0x822: v822(0x35c) = CONST 
    0x825: v825(0x1857) = CONST 
    0x828: v828_0 = CALLPRIVATE v825(0x1857), v822(0x35c)

    Begin block 0x35c0x821
    prev=[0x821], succ=[0x37e0x821]
    =================================
    0x35d0x821: v82135d(0x40) = CONST 
    0x3600x821: v821360 = MLOAD v82135d(0x40)
    0x3610x821: v821361(0x20) = CONST 
    0x3650x821: MSTORE v821360, v821361(0x20)
    0x3670x821: v821367 = MLOAD v828_0
    0x36a0x821: v82136a = ADD v821360, v821361(0x20)
    0x36b0x821: MSTORE v82136a, v821367
    0x36d0x821: v82136d = MLOAD v828_0
    0x3740x821: v821374 = ADD v821360, v82135d(0x40)
    0x3770x821: v821377 = ADD v828_0, v821361(0x20)
    0x37c0x821: v82137c(0x0) = CONST 

    Begin block 0x37e0x821
    prev=[0x3870x821, 0x35c0x821], succ=[0x3960x821, 0x3870x821]
    =================================
    0x37e0x821_0x0: v37e821_0 = PHI v821391, v82137c(0x0)
    0x3810x821: v821381 = LT v37e821_0, v82136d
    0x3820x821: v821382 = ISZERO v821381
    0x3830x821: v821383(0x396) = CONST 
    0x3860x821: JUMPI v821383(0x396), v821382

    Begin block 0x3960x821
    prev=[0x37e0x821], succ=[0x3c30x821, 0x3aa0x821]
    =================================
    0x39f0x821: v82139f = ADD v82136d, v821374
    0x3a10x821: v8213a1(0x1f) = CONST 
    0x3a30x821: v8213a3 = AND v8213a1(0x1f), v82136d
    0x3a50x821: v8213a5 = ISZERO v8213a3
    0x3a60x821: v8213a6(0x3c3) = CONST 
    0x3a90x821: JUMPI v8213a6(0x3c3), v8213a5

    Begin block 0x3c30x821
    prev=[0x3960x821, 0x3aa0x821], succ=[]
    =================================
    0x3c30x821_0x1: v3c3821_1 = PHI v8213c0, v82139f
    0x3c90x821: v8213c9(0x40) = CONST 
    0x3cb0x821: v8213cb = MLOAD v8213c9(0x40)
    0x3ce0x821: v8213ce = SUB v3c3821_1, v8213cb
    0x3d00x821: RETURN v8213cb, v8213ce

    Begin block 0x3aa0x821
    prev=[0x3960x821], succ=[0x3c30x821]
    =================================
    0x3ac0x821: v8213ac = SUB v82139f, v8213a3
    0x3ae0x821: v8213ae = MLOAD v8213ac
    0x3af0x821: v8213af(0x1) = CONST 
    0x3b20x821: v8213b2(0x20) = CONST 
    0x3b40x821: v8213b4 = SUB v8213b2(0x20), v8213a3
    0x3b50x821: v8213b5(0x100) = CONST 
    0x3b80x821: v8213b8 = EXP v8213b5(0x100), v8213b4
    0x3b90x821: v8213b9 = SUB v8213b8, v8213af(0x1)
    0x3ba0x821: v8213ba = NOT v8213b9
    0x3bb0x821: v8213bb = AND v8213ba, v8213ae
    0x3bd0x821: MSTORE v8213ac, v8213bb
    0x3be0x821: v8213be(0x20) = CONST 
    0x3c00x821: v8213c0 = ADD v8213be(0x20), v8213ac

    Begin block 0x3870x821
    prev=[0x37e0x821], succ=[0x37e0x821]
    =================================
    0x3870x821_0x0: v387821_0 = PHI v821391, v82137c(0x0)
    0x3890x821: v821389 = ADD v387821_0, v821377
    0x38a0x821: v82138a = MLOAD v821389
    0x38d0x821: v82138d = ADD v387821_0, v821374
    0x38e0x821: MSTORE v82138d, v82138a
    0x38f0x821: v82138f(0x20) = CONST 
    0x3910x821: v821391 = ADD v82138f(0x20), v387821_0
    0x3920x821: v821392(0x37e) = CONST 
    0x3950x821: JUMP v821392(0x37e)

}

function isOperator(address)() public {
    Begin block 0x829
    prev=[], succ=[0x83b, 0x83f]
    =================================
    0x82a: v82a(0x3f2d) = CONST 
    0x82d: v82d(0x4) = CONST 
    0x830: v830 = CALLDATASIZE 
    0x831: v831 = SUB v830, v82d(0x4)
    0x832: v832(0x20) = CONST 
    0x835: v835 = LT v831, v832(0x20)
    0x836: v836 = ISZERO v835
    0x837: v837(0x83f) = CONST 
    0x83a: JUMPI v837(0x83f), v836

    Begin block 0x83b
    prev=[0x829], succ=[]
    =================================
    0x83b: v83b(0x0) = CONST 
    0x83e: REVERT v83b(0x0), v83b(0x0)

    Begin block 0x83f
    prev=[0x829], succ=[0x18ea]
    =================================
    0x841: v841 = CALLDATALOAD v82d(0x4)
    0x842: v842(0x1) = CONST 
    0x844: v844(0x1) = CONST 
    0x846: v846(0xa0) = CONST 
    0x848: v848(0x10000000000000000000000000000000000000000) = SHL v846(0xa0), v844(0x1)
    0x849: v849(0xffffffffffffffffffffffffffffffffffffffff) = SUB v848(0x10000000000000000000000000000000000000000), v842(0x1)
    0x84a: v84a = AND v849(0xffffffffffffffffffffffffffffffffffffffff), v841
    0x84b: v84b(0x18ea) = CONST 
    0x84e: JUMP v84b(0x18ea)

    Begin block 0x18ea
    prev=[0x83f], succ=[0x3f2d]
    =================================
    0x18eb: v18eb(0x1) = CONST 
    0x18ed: v18ed(0x1) = CONST 
    0x18ef: v18ef(0xa0) = CONST 
    0x18f1: v18f1(0x10000000000000000000000000000000000000000) = SHL v18ef(0xa0), v18ed(0x1)
    0x18f2: v18f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18f1(0x10000000000000000000000000000000000000000), v18eb(0x1)
    0x18f3: v18f3 = AND v18f2(0xffffffffffffffffffffffffffffffffffffffff), v84a
    0x18f4: v18f4(0x0) = CONST 
    0x18f8: MSTORE v18f4(0x0), v18f3
    0x18f9: v18f9(0x6) = CONST 
    0x18fb: v18fb(0x20) = CONST 
    0x18fd: MSTORE v18fb(0x20), v18f9(0x6)
    0x18fe: v18fe(0x40) = CONST 
    0x1901: v1901 = SHA3 v18f4(0x0), v18fe(0x40)
    0x1902: v1902 = SLOAD v1901
    0x1903: v1903(0xff) = CONST 
    0x1905: v1905 = AND v1903(0xff), v1902
    0x1907: JUMP v82a(0x3f2d)

    Begin block 0x3f2d
    prev=[0x18ea], succ=[]
    =================================
    0x3f2e: v3f2e(0x40) = CONST 
    0x3f31: v3f31 = MLOAD v3f2e(0x40)
    0x3f33: v3f33 = ISZERO v1905
    0x3f34: v3f34 = ISZERO v3f33
    0x3f36: MSTORE v3f31, v3f34
    0x3f37: v3f37 = MLOAD v3f2e(0x40)
    0x3f3b: v3f3b(0x0) = SUB v3f31, v3f37
    0x3f3c: v3f3c(0x20) = CONST 
    0x3f3e: v3f3e(0x20) = ADD v3f3c(0x20), v3f3b(0x0)
    0x3f40: RETURN v3f37, v3f3e(0x20)

}

function mintBatch(address,uint256,uint256[])() public {
    Begin block 0x84f
    prev=[], succ=[0x861, 0x865]
    =================================
    0x850: v850(0x77f) = CONST 
    0x853: v853(0x4) = CONST 
    0x856: v856 = CALLDATASIZE 
    0x857: v857 = SUB v856, v853(0x4)
    0x858: v858(0x60) = CONST 
    0x85b: v85b = LT v857, v858(0x60)
    0x85c: v85c = ISZERO v85b
    0x85d: v85d(0x865) = CONST 
    0x860: JUMPI v85d(0x865), v85c

    Begin block 0x861
    prev=[0x84f], succ=[]
    =================================
    0x861: v861(0x0) = CONST 
    0x864: REVERT v861(0x0), v861(0x0)

    Begin block 0x865
    prev=[0x84f], succ=[0x890, 0x894]
    =================================
    0x866: v866(0x1) = CONST 
    0x868: v868(0x1) = CONST 
    0x86a: v86a(0xa0) = CONST 
    0x86c: v86c(0x10000000000000000000000000000000000000000) = SHL v86a(0xa0), v868(0x1)
    0x86d: v86d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86c(0x10000000000000000000000000000000000000000), v866(0x1)
    0x86f: v86f = CALLDATALOAD v853(0x4)
    0x870: v870 = AND v86f, v86d(0xffffffffffffffffffffffffffffffffffffffff)
    0x872: v872(0x20) = CONST 
    0x875: v875(0x24) = ADD v853(0x4), v872(0x20)
    0x876: v876 = CALLDATALOAD v875(0x24)
    0x879: v879 = ADD v853(0x4), v857
    0x87b: v87b(0x60) = CONST 
    0x87e: v87e(0x64) = ADD v853(0x4), v87b(0x60)
    0x87f: v87f(0x40) = CONST 
    0x882: v882(0x44) = ADD v853(0x4), v87f(0x40)
    0x883: v883 = CALLDATALOAD v882(0x44)
    0x884: v884(0x1) = CONST 
    0x886: v886(0x20) = CONST 
    0x888: v888(0x100000000) = SHL v886(0x20), v884(0x1)
    0x88a: v88a = GT v883, v888(0x100000000)
    0x88b: v88b = ISZERO v88a
    0x88c: v88c(0x894) = CONST 
    0x88f: JUMPI v88c(0x894), v88b

    Begin block 0x890
    prev=[0x865], succ=[]
    =================================
    0x890: v890(0x0) = CONST 
    0x893: REVERT v890(0x0), v890(0x0)

    Begin block 0x894
    prev=[0x865], succ=[0x8a2, 0x8a6]
    =================================
    0x896: v896 = ADD v853(0x4), v883
    0x898: v898(0x20) = CONST 
    0x89b: v89b = ADD v896, v898(0x20)
    0x89c: v89c = GT v89b, v879
    0x89d: v89d = ISZERO v89c
    0x89e: v89e(0x8a6) = CONST 
    0x8a1: JUMPI v89e(0x8a6), v89d

    Begin block 0x8a2
    prev=[0x894], succ=[]
    =================================
    0x8a2: v8a2(0x0) = CONST 
    0x8a5: REVERT v8a2(0x0), v8a2(0x0)

    Begin block 0x8a6
    prev=[0x894], succ=[0x8c3, 0x8c7]
    =================================
    0x8a8: v8a8 = CALLDATALOAD v896
    0x8aa: v8aa(0x20) = CONST 
    0x8ac: v8ac = ADD v8aa(0x20), v896
    0x8af: v8af(0x20) = CONST 
    0x8b2: v8b2 = MUL v8a8, v8af(0x20)
    0x8b4: v8b4 = ADD v8ac, v8b2
    0x8b5: v8b5 = GT v8b4, v879
    0x8b6: v8b6(0x1) = CONST 
    0x8b8: v8b8(0x20) = CONST 
    0x8ba: v8ba(0x100000000) = SHL v8b8(0x20), v8b6(0x1)
    0x8bc: v8bc = GT v8a8, v8ba(0x100000000)
    0x8bd: v8bd = OR v8bc, v8b5
    0x8be: v8be = ISZERO v8bd
    0x8bf: v8bf(0x8c7) = CONST 
    0x8c2: JUMPI v8bf(0x8c7), v8be

    Begin block 0x8c3
    prev=[0x8a6], succ=[]
    =================================
    0x8c3: v8c3(0x0) = CONST 
    0x8c6: REVERT v8c3(0x0), v8c3(0x0)

    Begin block 0x8c7
    prev=[0x8a6], succ=[0x1908]
    =================================
    0x8ce: v8ce(0x1908) = CONST 
    0x8d1: JUMP v8ce(0x1908)

    Begin block 0x1908
    prev=[0x8c7], succ=[0x1923, 0x1960]
    =================================
    0x1909: v1909 = CALLER 
    0x190a: v190a(0x0) = CONST 
    0x190e: MSTORE v190a(0x0), v1909
    0x190f: v190f(0x5) = CONST 
    0x1911: v1911(0x20) = CONST 
    0x1913: MSTORE v1911(0x20), v190f(0x5)
    0x1914: v1914(0x40) = CONST 
    0x1917: v1917 = SHA3 v190a(0x0), v1914(0x40)
    0x1918: v1918 = SLOAD v1917
    0x1919: v1919(0x60) = CONST 
    0x191c: v191c(0xff) = CONST 
    0x191e: v191e = AND v191c(0xff), v1918
    0x191f: v191f(0x1960) = CONST 
    0x1922: JUMPI v191f(0x1960), v191e

    Begin block 0x1923
    prev=[0x1908], succ=[]
    =================================
    0x1923: v1923(0x40) = CONST 
    0x1926: v1926 = MLOAD v1923(0x40)
    0x1927: v1927(0x461bcd) = CONST 
    0x192b: v192b(0xe5) = CONST 
    0x192d: v192d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v192b(0xe5), v1927(0x461bcd)
    0x192f: MSTORE v1926, v192d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1930: v1930(0x20) = CONST 
    0x1932: v1932(0x4) = CONST 
    0x1935: v1935 = ADD v1926, v1932(0x4)
    0x1936: MSTORE v1935, v1930(0x20)
    0x1937: v1937(0xe) = CONST 
    0x1939: v1939(0x24) = CONST 
    0x193c: v193c = ADD v1926, v1939(0x24)
    0x193d: MSTORE v193c, v1937(0xe)
    0x193e: v193e(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x194d: v194d(0x91) = CONST 
    0x194f: v194f(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v194d(0x91), v193e(0x36bab9ba1031329036b4b73a32b9)
    0x1950: v1950(0x44) = CONST 
    0x1953: v1953 = ADD v1926, v1950(0x44)
    0x1954: MSTORE v1953, v194f(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x1956: v1956 = MLOAD v1923(0x40)
    0x195a: v195a(0x0) = SUB v1926, v1956
    0x195b: v195b(0x64) = CONST 
    0x195d: v195d(0x64) = ADD v195b(0x64), v195a(0x0)
    0x195f: REVERT v1956, v195d(0x64)

    Begin block 0x1960
    prev=[0x1908], succ=[0x196f, 0x19bb]
    =================================
    0x1961: v1961(0x1) = CONST 
    0x1963: v1963(0x1) = CONST 
    0x1965: v1965(0xa0) = CONST 
    0x1967: v1967(0x10000000000000000000000000000000000000000) = SHL v1965(0xa0), v1963(0x1)
    0x1968: v1968(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1967(0x10000000000000000000000000000000000000000), v1961(0x1)
    0x196a: v196a = AND v870, v1968(0xffffffffffffffffffffffffffffffffffffffff)
    0x196b: v196b(0x19bb) = CONST 
    0x196e: JUMPI v196b(0x19bb), v196a

    Begin block 0x196f
    prev=[0x1960], succ=[]
    =================================
    0x196f: v196f(0x40) = CONST 
    0x1972: v1972 = MLOAD v196f(0x40)
    0x1973: v1973(0x461bcd) = CONST 
    0x1977: v1977(0xe5) = CONST 
    0x1979: v1979(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1977(0xe5), v1973(0x461bcd)
    0x197b: MSTORE v1972, v1979(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x197c: v197c(0x20) = CONST 
    0x197e: v197e(0x4) = CONST 
    0x1981: v1981 = ADD v1972, v197e(0x4)
    0x1982: MSTORE v1981, v197c(0x20)
    0x1983: v1983(0x1d) = CONST 
    0x1985: v1985(0x24) = CONST 
    0x1988: v1988 = ADD v1972, v1985(0x24)
    0x1989: MSTORE v1988, v1983(0x1d)
    0x198a: v198a(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x19ab: v19ab(0x44) = CONST 
    0x19ae: v19ae = ADD v1972, v19ab(0x44)
    0x19af: MSTORE v19ae, v198a(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x19b1: v19b1 = MLOAD v196f(0x40)
    0x19b5: v19b5(0x0) = SUB v1972, v19b1
    0x19b6: v19b6(0x64) = CONST 
    0x19b8: v19b8(0x64) = ADD v19b6(0x64), v19b5(0x0)
    0x19ba: REVERT v19b1, v19b8(0x64)

    Begin block 0x19bb
    prev=[0x1960], succ=[0x19c3, 0x19f9]
    =================================
    0x19be: v19be = EQ v876, v8a8
    0x19bf: v19bf(0x19f9) = CONST 
    0x19c2: JUMPI v19bf(0x19f9), v19be

    Begin block 0x19c3
    prev=[0x19bb], succ=[]
    =================================
    0x19c3: v19c3(0x40) = CONST 
    0x19c5: v19c5 = MLOAD v19c3(0x40)
    0x19c6: v19c6(0x461bcd) = CONST 
    0x19ca: v19ca(0xe5) = CONST 
    0x19cc: v19cc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19ca(0xe5), v19c6(0x461bcd)
    0x19ce: MSTORE v19c5, v19cc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19cf: v19cf(0x4) = CONST 
    0x19d1: v19d1 = ADD v19cf(0x4), v19c5
    0x19d4: v19d4(0x20) = CONST 
    0x19d6: v19d6 = ADD v19d4(0x20), v19d1
    0x19d9: v19d9(0x20) = SUB v19d6, v19d1
    0x19db: MSTORE v19d1, v19d9(0x20)
    0x19dc: v19dc(0x2a) = CONST 
    0x19df: MSTORE v19d6, v19dc(0x2a)
    0x19e0: v19e0(0x20) = CONST 
    0x19e2: v19e2 = ADD v19e0(0x20), v19d6
    0x19e4: v19e4(0x3be1) = CONST 
    0x19e7: v19e7(0x2a) = CONST 
    0x19ea: CODECOPY v19e2, v19e4(0x3be1), v19e7(0x2a)
    0x19eb: v19eb(0x40) = CONST 
    0x19ed: v19ed = ADD v19eb(0x40), v19e2
    0x19f1: v19f1(0x40) = CONST 
    0x19f3: v19f3 = MLOAD v19f1(0x40)
    0x19f6: v19f6(0x84) = SUB v19ed, v19f3
    0x19f8: REVERT v19f3, v19f6(0x84)

    Begin block 0x19f9
    prev=[0x19bb], succ=[0x2c7bB0x19f9]
    =================================
    0x19fa: v19fa(0x436c) = CONST 
    0x1a01: v1a01(0x2c7b) = CONST 
    0x1a04: JUMP v1a01(0x2c7b)

    Begin block 0x2c7bB0x19f9
    prev=[0x19f9], succ=[0x2c92B0x19f9, 0x2c96B0x19f9]
    =================================
    0x2c7cS0x19f9: v2c7cV19f9(0x60) = CONST 
    0x2c7eS0x19f9: v2c7eV19f9(0x0) = CONST 
    0x2c81S0x19f9: v2c81V19f9(0xffffffffffffffff) = CONST 
    0x2c8bS0x19f9: v2c8bV19f9 = GT v876, v2c81V19f9(0xffffffffffffffff)
    0x2c8dS0x19f9: v2c8dV19f9 = ISZERO v2c8bV19f9
    0x2c8eS0x19f9: v2c8eV19f9(0x2c96) = CONST 
    0x2c91S0x19f9: JUMPI v2c8eV19f9(0x2c96), v2c8dV19f9

    Begin block 0x2c92B0x19f9
    prev=[0x2c7bB0x19f9], succ=[]
    =================================
    0x2c92S0x19f9: v2c92V19f9(0x0) = CONST 
    0x2c95S0x19f9: REVERT v2c92V19f9(0x0), v2c92V19f9(0x0)

    Begin block 0x2c96B0x19f9
    prev=[0x2c7bB0x19f9], succ=[0x2cc0B0x19f9, 0x2cb1B0x19f9]
    =================================
    0x2c98S0x19f9: v2c98V19f9(0x40) = CONST 
    0x2c9aS0x19f9: v2c9aV19f9 = MLOAD v2c98V19f9(0x40)
    0x2c9eS0x19f9: MSTORE v2c9aV19f9, v876
    0x2ca0S0x19f9: v2ca0V19f9(0x20) = CONST 
    0x2ca2S0x19f9: v2ca2V19f9 = MUL v2ca0V19f9(0x20), v876
    0x2ca3S0x19f9: v2ca3V19f9(0x20) = CONST 
    0x2ca5S0x19f9: v2ca5V19f9 = ADD v2ca3V19f9(0x20), v2ca2V19f9
    0x2ca7S0x19f9: v2ca7V19f9 = ADD v2c9aV19f9, v2ca5V19f9
    0x2ca8S0x19f9: v2ca8V19f9(0x40) = CONST 
    0x2caaS0x19f9: MSTORE v2ca8V19f9(0x40), v2ca7V19f9
    0x2cacS0x19f9: v2cacV19f9 = ISZERO v876
    0x2cadS0x19f9: v2cadV19f9(0x2cc0) = CONST 
    0x2cb0S0x19f9: JUMPI v2cadV19f9(0x2cc0), v2cacV19f9

    Begin block 0x2cc0B0x19f9
    prev=[0x2c96B0x19f9, 0x2cb1B0x19f9], succ=[0x2cd8B0x19f9, 0x2cdcB0x19f9]
    =================================
    0x2cc4S0x19f9: v2cc4V19f9(0x0) = CONST 
    0x2cc7S0x19f9: v2cc7V19f9(0xffffffffffffffff) = CONST 
    0x2cd1S0x19f9: v2cd1V19f9 = GT v876, v2cc7V19f9(0xffffffffffffffff)
    0x2cd3S0x19f9: v2cd3V19f9 = ISZERO v2cd1V19f9
    0x2cd4S0x19f9: v2cd4V19f9(0x2cdc) = CONST 
    0x2cd7S0x19f9: JUMPI v2cd4V19f9(0x2cdc), v2cd3V19f9

    Begin block 0x2cd8B0x19f9
    prev=[0x2cc0B0x19f9], succ=[]
    =================================
    0x2cd8S0x19f9: v2cd8V19f9(0x0) = CONST 
    0x2cdbS0x19f9: REVERT v2cd8V19f9(0x0), v2cd8V19f9(0x0)

    Begin block 0x2cdcB0x19f9
    prev=[0x2cc0B0x19f9], succ=[0x2d06B0x19f9, 0x2cf7B0x19f9]
    =================================
    0x2cdeS0x19f9: v2cdeV19f9(0x40) = CONST 
    0x2ce0S0x19f9: v2ce0V19f9 = MLOAD v2cdeV19f9(0x40)
    0x2ce4S0x19f9: MSTORE v2ce0V19f9, v876
    0x2ce6S0x19f9: v2ce6V19f9(0x20) = CONST 
    0x2ce8S0x19f9: v2ce8V19f9 = MUL v2ce6V19f9(0x20), v876
    0x2ce9S0x19f9: v2ce9V19f9(0x20) = CONST 
    0x2cebS0x19f9: v2cebV19f9 = ADD v2ce9V19f9(0x20), v2ce8V19f9
    0x2cedS0x19f9: v2cedV19f9 = ADD v2ce0V19f9, v2cebV19f9
    0x2ceeS0x19f9: v2ceeV19f9(0x40) = CONST 
    0x2cf0S0x19f9: MSTORE v2ceeV19f9(0x40), v2cedV19f9
    0x2cf2S0x19f9: v2cf2V19f9 = ISZERO v876
    0x2cf3S0x19f9: v2cf3V19f9(0x2d06) = CONST 
    0x2cf6S0x19f9: JUMPI v2cf3V19f9(0x2d06), v2cf2V19f9

    Begin block 0x2d06B0x19f9
    prev=[0x2cdcB0x19f9, 0x2cf7B0x19f9], succ=[0x2d0cB0x19f9]
    =================================
    0x2d0aS0x19f9: v2d0aV19f9(0x0) = CONST 

    Begin block 0x2d0cB0x19f9
    prev=[0x2d06B0x19f9, 0x2e20B0x19f9], succ=[0x2d16B0x19f9, 0x2e33B0x19f9]
    =================================
    0x2d0c_0x0S0x19f9: v2d0c_0V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2d0eS0x19f9: v2d0eV19f9 = MLOAD v2c9aV19f9
    0x2d10S0x19f9: v2d10V19f9 = LT v2d0c_0V19f9, v2d0eV19f9
    0x2d11S0x19f9: v2d11V19f9 = ISZERO v2d10V19f9
    0x2d12S0x19f9: v2d12V19f9(0x2e33) = CONST 
    0x2d15S0x19f9: JUMPI v2d12V19f9(0x2e33), v2d11V19f9

    Begin block 0x2d16B0x19f9
    prev=[0x2d0cB0x19f9], succ=[0x2d6eB0x19f9, 0x2d6dB0x19f9]
    =================================
    0x2d16S0x19f9: v2d16V19f9(0x7) = CONST 
    0x2d16_0x0S0x19f9: v2d16_0V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2d19S0x19f9: v2d19V19f9 = SLOAD v2d16V19f9(0x7)
    0x2d1aS0x19f9: v2d1aV19f9(0x1) = CONST 
    0x2d1cS0x19f9: v2d1cV19f9 = ADD v2d1aV19f9(0x1), v2d19V19f9
    0x2d20S0x19f9: SSTORE v2d16V19f9(0x7), v2d1cV19f9
    0x2d21S0x19f9: v2d21V19f9(0x0) = CONST 
    0x2d25S0x19f9: MSTORE v2d21V19f9(0x0), v2d1cV19f9
    0x2d26S0x19f9: v2d26V19f9(0x8) = CONST 
    0x2d28S0x19f9: v2d28V19f9(0x20) = CONST 
    0x2d2cS0x19f9: MSTORE v2d28V19f9(0x20), v2d26V19f9(0x8)
    0x2d2dS0x19f9: v2d2dV19f9(0x40) = CONST 
    0x2d32S0x19f9: v2d32V19f9 = SHA3 v2d21V19f9(0x0), v2d2dV19f9(0x40)
    0x2d34S0x19f9: v2d34V19f9 = SLOAD v2d32V19f9
    0x2d35S0x19f9: v2d35V19f9(0x1) = CONST 
    0x2d37S0x19f9: v2d37V19f9(0x1) = CONST 
    0x2d39S0x19f9: v2d39V19f9(0xa0) = CONST 
    0x2d3bS0x19f9: v2d3bV19f9(0x10000000000000000000000000000000000000000) = SHL v2d39V19f9(0xa0), v2d37V19f9(0x1)
    0x2d3cS0x19f9: v2d3cV19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d3bV19f9(0x10000000000000000000000000000000000000000), v2d35V19f9(0x1)
    0x2d3dS0x19f9: v2d3dV19f9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2d3cV19f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d3eS0x19f9: v2d3eV19f9 = AND v2d3dV19f9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2d34V19f9
    0x2d3fS0x19f9: v2d3fV19f9(0x1) = CONST 
    0x2d41S0x19f9: v2d41V19f9(0x1) = CONST 
    0x2d43S0x19f9: v2d43V19f9(0xa0) = CONST 
    0x2d45S0x19f9: v2d45V19f9(0x10000000000000000000000000000000000000000) = SHL v2d43V19f9(0xa0), v2d41V19f9(0x1)
    0x2d46S0x19f9: v2d46V19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d45V19f9(0x10000000000000000000000000000000000000000), v2d3fV19f9(0x1)
    0x2d48S0x19f9: v2d48V19f9 = AND v870, v2d46V19f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d49S0x19f9: v2d49V19f9 = OR v2d48V19f9, v2d3eV19f9
    0x2d4bS0x19f9: SSTORE v2d32V19f9, v2d49V19f9
    0x2d4dS0x19f9: v2d4dV19f9 = MLOAD v2d2dV19f9(0x40)
    0x2d4eS0x19f9: v2d4eV19f9(0x60) = CONST 
    0x2d51S0x19f9: v2d51V19f9 = ADD v2d4dV19f9, v2d4eV19f9(0x60)
    0x2d54S0x19f9: MSTORE v2d2dV19f9(0x40), v2d51V19f9
    0x2d55S0x19f9: v2d55V19f9 = NUMBER 
    0x2d56S0x19f9: v2d56V19f9(0x1) = CONST 
    0x2d58S0x19f9: v2d58V19f9(0x1) = CONST 
    0x2d5aS0x19f9: v2d5aV19f9(0x80) = CONST 
    0x2d5cS0x19f9: v2d5cV19f9(0x100000000000000000000000000000000) = SHL v2d5aV19f9(0x80), v2d58V19f9(0x1)
    0x2d5dS0x19f9: v2d5dV19f9(0xffffffffffffffffffffffffffffffff) = SUB v2d5cV19f9(0x100000000000000000000000000000000), v2d56V19f9(0x1)
    0x2d5eS0x19f9: v2d5eV19f9 = AND v2d5dV19f9(0xffffffffffffffffffffffffffffffff), v2d55V19f9
    0x2d60S0x19f9: MSTORE v2d4dV19f9, v2d5eV19f9
    0x2d62S0x19f9: v2d62V19f9 = ADD v2d4dV19f9, v2d28V19f9(0x20)
    0x2d68S0x19f9: v2d68V19f9 = LT v2d16_0V19f9, v8a8
    0x2d69S0x19f9: v2d69V19f9(0x2d6e) = CONST 
    0x2d6cS0x19f9: JUMPI v2d69V19f9(0x2d6e), v2d68V19f9

    Begin block 0x2d6eB0x19f9
    prev=[0x2d16B0x19f9], succ=[0x2e06B0x19f9, 0x2e05B0x19f9]
    =================================
    0x2d6e_0x0S0x19f9: v2d6e_0V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2d6e_0x5S0x19f9: v2d6e_5V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2d6fS0x19f9: v2d6fV19f9(0x1) = CONST 
    0x2d71S0x19f9: v2d71V19f9(0x1) = CONST 
    0x2d73S0x19f9: v2d73V19f9(0x80) = CONST 
    0x2d75S0x19f9: v2d75V19f9(0x100000000000000000000000000000000) = SHL v2d73V19f9(0x80), v2d71V19f9(0x1)
    0x2d76S0x19f9: v2d76V19f9(0xffffffffffffffffffffffffffffffff) = SUB v2d75V19f9(0x100000000000000000000000000000000), v2d6fV19f9(0x1)
    0x2d77S0x19f9: v2d77V19f9(0x20) = CONST 
    0x2d7bS0x19f9: v2d7bV19f9 = MUL v2d77V19f9(0x20), v2d6e_0V19f9
    0x2d7fS0x19f9: v2d7fV19f9 = ADD v2d7bV19f9, v8ac
    0x2d80S0x19f9: v2d80V19f9 = CALLDATALOAD v2d7fV19f9
    0x2d82S0x19f9: v2d82V19f9 = AND v2d76V19f9(0xffffffffffffffffffffffffffffffff), v2d80V19f9
    0x2d84S0x19f9: MSTORE v2d62V19f9, v2d82V19f9
    0x2d85S0x19f9: v2d85V19f9(0x1) = CONST 
    0x2d87S0x19f9: v2d87V19f9(0x1) = CONST 
    0x2d89S0x19f9: v2d89V19f9(0xa0) = CONST 
    0x2d8bS0x19f9: v2d8bV19f9(0x10000000000000000000000000000000000000000) = SHL v2d89V19f9(0xa0), v2d87V19f9(0x1)
    0x2d8cS0x19f9: v2d8cV19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d8bV19f9(0x10000000000000000000000000000000000000000), v2d85V19f9(0x1)
    0x2d8fS0x19f9: v2d8fV19f9 = AND v870, v2d8cV19f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d92S0x19f9: v2d92V19f9 = ADD v2d77V19f9(0x20), v2d62V19f9
    0x2d96S0x19f9: MSTORE v2d92V19f9, v2d8fV19f9
    0x2d97S0x19f9: v2d97V19f9(0x7) = CONST 
    0x2d9aS0x19f9: v2d9aV19f9 = SLOAD v2d97V19f9(0x7)
    0x2d9bS0x19f9: v2d9bV19f9(0x0) = CONST 
    0x2d9fS0x19f9: MSTORE v2d9bV19f9(0x0), v2d9aV19f9
    0x2da0S0x19f9: v2da0V19f9(0xa) = CONST 
    0x2da3S0x19f9: MSTORE v2d77V19f9(0x20), v2da0V19f9(0xa)
    0x2da4S0x19f9: v2da4V19f9(0x40) = CONST 
    0x2da9S0x19f9: v2da9V19f9 = SHA3 v2d9bV19f9(0x0), v2da4V19f9(0x40)
    0x2dabS0x19f9: v2dabV19f9 = MLOAD v2d4dV19f9
    0x2dadS0x19f9: v2dadV19f9 = SLOAD v2da9V19f9
    0x2db0S0x19f9: v2db0V19f9 = ADD v2d4dV19f9, v2d77V19f9(0x20)
    0x2db1S0x19f9: v2db1V19f9 = MLOAD v2db0V19f9
    0x2db3S0x19f9: v2db3V19f9 = AND v2d76V19f9(0xffffffffffffffffffffffffffffffff), v2db1V19f9
    0x2db4S0x19f9: v2db4V19f9(0x1) = CONST 
    0x2db6S0x19f9: v2db6V19f9(0x80) = CONST 
    0x2db8S0x19f9: v2db8V19f9(0x100000000000000000000000000000000) = SHL v2db6V19f9(0x80), v2db4V19f9(0x1)
    0x2db9S0x19f9: v2db9V19f9 = MUL v2db8V19f9(0x100000000000000000000000000000000), v2db3V19f9
    0x2dbcS0x19f9: v2dbcV19f9 = AND v2d76V19f9(0xffffffffffffffffffffffffffffffff), v2dabV19f9
    0x2dbdS0x19f9: v2dbdV19f9(0x1) = CONST 
    0x2dbfS0x19f9: v2dbfV19f9(0x1) = CONST 
    0x2dc1S0x19f9: v2dc1V19f9(0x80) = CONST 
    0x2dc3S0x19f9: v2dc3V19f9(0x100000000000000000000000000000000) = SHL v2dc1V19f9(0x80), v2dbfV19f9(0x1)
    0x2dc4S0x19f9: v2dc4V19f9(0xffffffffffffffffffffffffffffffff) = SUB v2dc3V19f9(0x100000000000000000000000000000000), v2dbdV19f9(0x1)
    0x2dc5S0x19f9: v2dc5V19f9(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) = NOT v2dc4V19f9(0xffffffffffffffffffffffffffffffff)
    0x2dc8S0x19f9: v2dc8V19f9 = AND v2dadV19f9, v2dc5V19f9(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000)
    0x2dccS0x19f9: v2dccV19f9 = OR v2dc8V19f9, v2dbcV19f9
    0x2dcfS0x19f9: v2dcfV19f9 = AND v2d76V19f9(0xffffffffffffffffffffffffffffffff), v2dccV19f9
    0x2dd3S0x19f9: v2dd3V19f9 = OR v2dcfV19f9, v2db9V19f9
    0x2dd5S0x19f9: SSTORE v2da9V19f9, v2dd3V19f9
    0x2dd7S0x19f9: v2dd7V19f9 = ADD v2d4dV19f9, v2da4V19f9(0x40)
    0x2dd8S0x19f9: v2dd8V19f9 = MLOAD v2dd7V19f9
    0x2dd9S0x19f9: v2dd9V19f9(0x1) = CONST 
    0x2dddS0x19f9: v2dddV19f9 = ADD v2da9V19f9, v2dd9V19f9(0x1)
    0x2ddfS0x19f9: v2ddfV19f9 = SLOAD v2dddV19f9
    0x2de3S0x19f9: v2de3V19f9 = AND v2d8cV19f9(0xffffffffffffffffffffffffffffffffffffffff), v2dd8V19f9
    0x2de4S0x19f9: v2de4V19f9(0x1) = CONST 
    0x2de6S0x19f9: v2de6V19f9(0x1) = CONST 
    0x2de8S0x19f9: v2de8V19f9(0xa0) = CONST 
    0x2deaS0x19f9: v2deaV19f9(0x10000000000000000000000000000000000000000) = SHL v2de8V19f9(0xa0), v2de6V19f9(0x1)
    0x2debS0x19f9: v2debV19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2deaV19f9(0x10000000000000000000000000000000000000000), v2de4V19f9(0x1)
    0x2decS0x19f9: v2decV19f9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2debV19f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2defS0x19f9: v2defV19f9 = AND v2ddfV19f9, v2decV19f9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x2df3S0x19f9: v2df3V19f9 = OR v2defV19f9, v2de3V19f9
    0x2df6S0x19f9: SSTORE v2dddV19f9, v2df3V19f9
    0x2df8S0x19f9: v2df8V19f9 = SLOAD v2d97V19f9(0x7)
    0x2dfaS0x19f9: v2dfaV19f9 = MLOAD v2c9aV19f9
    0x2e00S0x19f9: v2e00V19f9 = LT v2d6e_5V19f9, v2dfaV19f9
    0x2e01S0x19f9: v2e01V19f9(0x2e06) = CONST 
    0x2e04S0x19f9: JUMPI v2e01V19f9(0x2e06), v2e00V19f9

    Begin block 0x2e06B0x19f9
    prev=[0x2d6eB0x19f9], succ=[0x2e20B0x19f9, 0x2e1fB0x19f9]
    =================================
    0x2e06_0x0S0x19f9: v2e06_0V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2e06_0x3S0x19f9: v2e06_3V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2e07S0x19f9: v2e07V19f9(0x20) = CONST 
    0x2e09S0x19f9: v2e09V19f9 = MUL v2e07V19f9(0x20), v2e06_0V19f9
    0x2e0aS0x19f9: v2e0aV19f9(0x20) = CONST 
    0x2e0cS0x19f9: v2e0cV19f9 = ADD v2e0aV19f9(0x20), v2e09V19f9
    0x2e0dS0x19f9: v2e0dV19f9 = ADD v2e0cV19f9, v2c9aV19f9
    0x2e10S0x19f9: MSTORE v2e0dV19f9, v2df8V19f9
    0x2e13S0x19f9: v2e13V19f9(0x1) = CONST 
    0x2e18S0x19f9: v2e18V19f9 = MLOAD v2ce0V19f9
    0x2e1aS0x19f9: v2e1aV19f9 = LT v2e06_3V19f9, v2e18V19f9
    0x2e1bS0x19f9: v2e1bV19f9(0x2e20) = CONST 
    0x2e1eS0x19f9: JUMPI v2e1bV19f9(0x2e20), v2e1aV19f9

    Begin block 0x2e20B0x19f9
    prev=[0x2e06B0x19f9], succ=[0x2d0cB0x19f9]
    =================================
    0x2e20_0x0S0x19f9: v2e20_0V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2e20_0x3S0x19f9: v2e20_3V19f9 = PHI v2d0aV19f9(0x0), v2e2eV19f9
    0x2e21S0x19f9: v2e21V19f9(0x20) = CONST 
    0x2e25S0x19f9: v2e25V19f9 = MUL v2e21V19f9(0x20), v2e20_0V19f9
    0x2e29S0x19f9: v2e29V19f9 = ADD v2e25V19f9, v2ce0V19f9
    0x2e2aS0x19f9: v2e2aV19f9 = ADD v2e29V19f9, v2e21V19f9(0x20)
    0x2e2bS0x19f9: MSTORE v2e2aV19f9, v2e13V19f9(0x1)
    0x2e2cS0x19f9: v2e2cV19f9(0x1) = CONST 
    0x2e2eS0x19f9: v2e2eV19f9 = ADD v2e2cV19f9(0x1), v2e20_3V19f9
    0x2e2fS0x19f9: v2e2fV19f9(0x2d0c) = CONST 
    0x2e32S0x19f9: JUMP v2e2fV19f9(0x2d0c)

    Begin block 0x2e1fB0x19f9
    prev=[0x2e06B0x19f9], succ=[]
    =================================
    0x2e1fS0x19f9: THROW 

    Begin block 0x2e05B0x19f9
    prev=[0x2d6eB0x19f9], succ=[]
    =================================
    0x2e05S0x19f9: THROW 

    Begin block 0x2d6dB0x19f9
    prev=[0x2d16B0x19f9], succ=[]
    =================================
    0x2d6dS0x19f9: THROW 

    Begin block 0x2e33B0x19f9
    prev=[0x2d0cB0x19f9], succ=[0x2ea2B0x19f9]
    =================================
    0x2e36S0x19f9: v2e36V19f9(0x1) = CONST 
    0x2e38S0x19f9: v2e38V19f9(0x1) = CONST 
    0x2e3aS0x19f9: v2e3aV19f9(0xa0) = CONST 
    0x2e3cS0x19f9: v2e3cV19f9(0x10000000000000000000000000000000000000000) = SHL v2e3aV19f9(0xa0), v2e38V19f9(0x1)
    0x2e3dS0x19f9: v2e3dV19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e3cV19f9(0x10000000000000000000000000000000000000000), v2e36V19f9(0x1)
    0x2e3eS0x19f9: v2e3eV19f9 = AND v2e3dV19f9(0xffffffffffffffffffffffffffffffffffffffff), v870
    0x2e3fS0x19f9: v2e3fV19f9(0x0) = CONST 
    0x2e41S0x19f9: v2e41V19f9(0x1) = CONST 
    0x2e43S0x19f9: v2e43V19f9(0x1) = CONST 
    0x2e45S0x19f9: v2e45V19f9(0xa0) = CONST 
    0x2e47S0x19f9: v2e47V19f9(0x10000000000000000000000000000000000000000) = SHL v2e45V19f9(0xa0), v2e43V19f9(0x1)
    0x2e48S0x19f9: v2e48V19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e47V19f9(0x10000000000000000000000000000000000000000), v2e41V19f9(0x1)
    0x2e49S0x19f9: v2e49V19f9(0x0) = AND v2e48V19f9(0xffffffffffffffffffffffffffffffffffffffff), v2e3fV19f9(0x0)
    0x2e4aS0x19f9: v2e4aV19f9 = CALLER 
    0x2e4bS0x19f9: v2e4bV19f9(0x1) = CONST 
    0x2e4dS0x19f9: v2e4dV19f9(0x1) = CONST 
    0x2e4fS0x19f9: v2e4fV19f9(0xa0) = CONST 
    0x2e51S0x19f9: v2e51V19f9(0x10000000000000000000000000000000000000000) = SHL v2e4fV19f9(0xa0), v2e4dV19f9(0x1)
    0x2e52S0x19f9: v2e52V19f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e51V19f9(0x10000000000000000000000000000000000000000), v2e4bV19f9(0x1)
    0x2e53S0x19f9: v2e53V19f9 = AND v2e52V19f9(0xffffffffffffffffffffffffffffffffffffffff), v2e4aV19f9
    0x2e54S0x19f9: v2e54V19f9(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x2e77S0x19f9: v2e77V19f9(0x40) = CONST 
    0x2e79S0x19f9: v2e79V19f9 = MLOAD v2e77V19f9(0x40)
    0x2e7cS0x19f9: v2e7cV19f9(0x20) = CONST 
    0x2e7eS0x19f9: v2e7eV19f9 = ADD v2e7cV19f9(0x20), v2e79V19f9
    0x2e80S0x19f9: v2e80V19f9(0x20) = CONST 
    0x2e82S0x19f9: v2e82V19f9 = ADD v2e80V19f9(0x20), v2e7eV19f9
    0x2e85S0x19f9: v2e85V19f9(0x40) = SUB v2e82V19f9, v2e79V19f9
    0x2e87S0x19f9: MSTORE v2e79V19f9, v2e85V19f9(0x40)
    0x2e8bS0x19f9: v2e8bV19f9 = MLOAD v2c9aV19f9
    0x2e8dS0x19f9: MSTORE v2e82V19f9, v2e8bV19f9
    0x2e8eS0x19f9: v2e8eV19f9(0x20) = CONST 
    0x2e90S0x19f9: v2e90V19f9 = ADD v2e8eV19f9(0x20), v2e82V19f9
    0x2e94S0x19f9: v2e94V19f9 = MLOAD v2c9aV19f9
    0x2e96S0x19f9: v2e96V19f9(0x20) = CONST 
    0x2e98S0x19f9: v2e98V19f9 = ADD v2e96V19f9(0x20), v2c9aV19f9
    0x2e9aS0x19f9: v2e9aV19f9(0x20) = CONST 
    0x2e9cS0x19f9: v2e9cV19f9 = MUL v2e9aV19f9(0x20), v2e94V19f9
    0x2ea0S0x19f9: v2ea0V19f9(0x0) = CONST 

    Begin block 0x2ea2B0x19f9
    prev=[0x2e33B0x19f9, 0x2eabB0x19f9], succ=[0x2ebaB0x19f9, 0x2eabB0x19f9]
    =================================
    0x2ea2_0x0S0x19f9: v2ea2_0V19f9 = PHI v2ea0V19f9(0x0), v2eb5V19f9
    0x2ea5S0x19f9: v2ea5V19f9 = LT v2ea2_0V19f9, v2e9cV19f9
    0x2ea6S0x19f9: v2ea6V19f9 = ISZERO v2ea5V19f9
    0x2ea7S0x19f9: v2ea7V19f9(0x2eba) = CONST 
    0x2eaaS0x19f9: JUMPI v2ea7V19f9(0x2eba), v2ea6V19f9

    Begin block 0x2ebaB0x19f9
    prev=[0x2ea2B0x19f9], succ=[0x2ee1B0x19f9]
    =================================
    0x2ec1S0x19f9: v2ec1V19f9 = ADD v2e9cV19f9, v2e90V19f9
    0x2ec4S0x19f9: v2ec4V19f9 = SUB v2ec1V19f9, v2e79V19f9
    0x2ec6S0x19f9: MSTORE v2e7eV19f9, v2ec4V19f9
    0x2ecaS0x19f9: v2ecaV19f9 = MLOAD v2ce0V19f9
    0x2eccS0x19f9: MSTORE v2ec1V19f9, v2ecaV19f9
    0x2ecdS0x19f9: v2ecdV19f9(0x20) = CONST 
    0x2ecfS0x19f9: v2ecfV19f9 = ADD v2ecdV19f9(0x20), v2ec1V19f9
    0x2ed3S0x19f9: v2ed3V19f9 = MLOAD v2ce0V19f9
    0x2ed5S0x19f9: v2ed5V19f9(0x20) = CONST 
    0x2ed7S0x19f9: v2ed7V19f9 = ADD v2ed5V19f9(0x20), v2ce0V19f9
    0x2ed9S0x19f9: v2ed9V19f9(0x20) = CONST 
    0x2edbS0x19f9: v2edbV19f9 = MUL v2ed9V19f9(0x20), v2ed3V19f9
    0x2edfS0x19f9: v2edfV19f9(0x0) = CONST 

    Begin block 0x2ee1B0x19f9
    prev=[0x2ebaB0x19f9, 0x2eeaB0x19f9], succ=[0x2ef9B0x19f9, 0x2eeaB0x19f9]
    =================================
    0x2ee1_0x0S0x19f9: v2ee1_0V19f9 = PHI v2edfV19f9(0x0), v2ef4V19f9
    0x2ee4S0x19f9: v2ee4V19f9 = LT v2ee1_0V19f9, v2edbV19f9
    0x2ee5S0x19f9: v2ee5V19f9 = ISZERO v2ee4V19f9
    0x2ee6S0x19f9: v2ee6V19f9(0x2ef9) = CONST 
    0x2ee9S0x19f9: JUMPI v2ee6V19f9(0x2ef9), v2ee5V19f9

    Begin block 0x2ef9B0x19f9
    prev=[0x2ee1B0x19f9], succ=[0x2f2cB0x19f9]
    =================================
    0x2f00S0x19f9: v2f00V19f9 = ADD v2edbV19f9, v2ecfV19f9
    0x2f07S0x19f9: v2f07V19f9(0x40) = CONST 
    0x2f09S0x19f9: v2f09V19f9 = MLOAD v2f07V19f9(0x40)
    0x2f0cS0x19f9: v2f0cV19f9 = SUB v2f00V19f9, v2f09V19f9
    0x2f0eS0x19f9: LOG4 v2f09V19f9, v2f0cV19f9, v2e54V19f9(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v2e53V19f9, v2e49V19f9(0x0), v2e3eV19f9
    0x2f0fS0x19f9: v2f0fV19f9(0x2f2c) = CONST 
    0x2f12S0x19f9: v2f12V19f9 = CALLER 
    0x2f13S0x19f9: v2f13V19f9(0x0) = CONST 
    0x2f18S0x19f9: v2f18V19f9(0x40) = CONST 
    0x2f1aS0x19f9: v2f1aV19f9 = MLOAD v2f18V19f9(0x40)
    0x2f1cS0x19f9: v2f1cV19f9(0x20) = CONST 
    0x2f1eS0x19f9: v2f1eV19f9 = ADD v2f1cV19f9(0x20), v2f1aV19f9
    0x2f1fS0x19f9: v2f1fV19f9(0x40) = CONST 
    0x2f21S0x19f9: MSTORE v2f1fV19f9(0x40), v2f1eV19f9
    0x2f23S0x19f9: v2f23V19f9(0x0) = CONST 
    0x2f26S0x19f9: MSTORE v2f1aV19f9, v2f23V19f9(0x0)
    0x2f28S0x19f9: v2f28V19f9(0x27fd) = CONST 
    0x2f2bS0x19f9: CALLPRIVATE v2f28V19f9(0x27fd), v2f1aV19f9, v2ce0V19f9, v2c9aV19f9, v870, v2f13V19f9(0x0), v2f12V19f9, v2f0fV19f9(0x2f2c)

    Begin block 0x2f2cB0x19f9
    prev=[0x2ef9B0x19f9], succ=[0x436c]
    =================================
    0x2f35S0x19f9: JUMP v19fa(0x436c)

    Begin block 0x436c
    prev=[0x2f2cB0x19f9], succ=[0x77f0x84f]
    =================================
    0x4374: JUMP v850(0x77f)

    Begin block 0x77f0x84f
    prev=[0x436c], succ=[0x7a30x84f]
    =================================
    0x7800x84f: v84f780(0x40) = CONST 
    0x7830x84f: v84f783 = MLOAD v84f780(0x40)
    0x7840x84f: v84f784(0x20) = CONST 
    0x7880x84f: MSTORE v84f783, v84f784(0x20)
    0x78a0x84f: v84f78a = MLOAD v2c9aV19f9
    0x78d0x84f: v84f78d = ADD v84f783, v84f784(0x20)
    0x78e0x84f: MSTORE v84f78d, v84f78a
    0x7900x84f: v84f790 = MLOAD v2c9aV19f9
    0x7970x84f: v84f797 = ADD v84f783, v84f780(0x40)
    0x79b0x84f: v84f79b = ADD v84f784(0x20), v2c9aV19f9
    0x79d0x84f: v84f79d = MUL v84f790, v84f784(0x20)
    0x7a10x84f: v84f7a1(0x0) = CONST 

    Begin block 0x7a30x84f
    prev=[0x7ac0x84f, 0x77f0x84f], succ=[0x7ac0x84f, 0x7bb0x84f]
    =================================
    0x7a30x84f_0x0: v7a384f_0 = PHI v84f7b6, v84f7a1(0x0)
    0x7a60x84f: v84f7a6 = LT v7a384f_0, v84f79d
    0x7a70x84f: v84f7a7 = ISZERO v84f7a6
    0x7a80x84f: v84f7a8(0x7bb) = CONST 
    0x7ab0x84f: JUMPI v84f7a8(0x7bb), v84f7a7

    Begin block 0x7ac0x84f
    prev=[0x7a30x84f], succ=[0x7a30x84f]
    =================================
    0x7ac0x84f_0x0: v7ac84f_0 = PHI v84f7b6, v84f7a1(0x0)
    0x7ae0x84f: v84f7ae = ADD v7ac84f_0, v84f79b
    0x7af0x84f: v84f7af = MLOAD v84f7ae
    0x7b20x84f: v84f7b2 = ADD v7ac84f_0, v84f797
    0x7b30x84f: MSTORE v84f7b2, v84f7af
    0x7b40x84f: v84f7b4(0x20) = CONST 
    0x7b60x84f: v84f7b6 = ADD v84f7b4(0x20), v7ac84f_0
    0x7b70x84f: v84f7b7(0x7a3) = CONST 
    0x7ba0x84f: JUMP v84f7b7(0x7a3)

    Begin block 0x7bb0x84f
    prev=[0x7a30x84f], succ=[]
    =================================
    0x7c20x84f: v84f7c2 = ADD v84f79d, v84f797
    0x7c70x84f: v84f7c7(0x40) = CONST 
    0x7c90x84f: v84f7c9 = MLOAD v84f7c7(0x40)
    0x7cc0x84f: v84f7cc = SUB v84f7c2, v84f7c9
    0x7ce0x84f: RETURN v84f7c9, v84f7cc

    Begin block 0x2eeaB0x19f9
    prev=[0x2ee1B0x19f9], succ=[0x2ee1B0x19f9]
    =================================
    0x2eea_0x0S0x19f9: v2eea_0V19f9 = PHI v2edfV19f9(0x0), v2ef4V19f9
    0x2eecS0x19f9: v2eecV19f9 = ADD v2eea_0V19f9, v2ed7V19f9
    0x2eedS0x19f9: v2eedV19f9 = MLOAD v2eecV19f9
    0x2ef0S0x19f9: v2ef0V19f9 = ADD v2eea_0V19f9, v2ecfV19f9
    0x2ef1S0x19f9: MSTORE v2ef0V19f9, v2eedV19f9
    0x2ef2S0x19f9: v2ef2V19f9(0x20) = CONST 
    0x2ef4S0x19f9: v2ef4V19f9 = ADD v2ef2V19f9(0x20), v2eea_0V19f9
    0x2ef5S0x19f9: v2ef5V19f9(0x2ee1) = CONST 
    0x2ef8S0x19f9: JUMP v2ef5V19f9(0x2ee1)

    Begin block 0x2eabB0x19f9
    prev=[0x2ea2B0x19f9], succ=[0x2ea2B0x19f9]
    =================================
    0x2eab_0x0S0x19f9: v2eab_0V19f9 = PHI v2ea0V19f9(0x0), v2eb5V19f9
    0x2eadS0x19f9: v2eadV19f9 = ADD v2eab_0V19f9, v2e98V19f9
    0x2eaeS0x19f9: v2eaeV19f9 = MLOAD v2eadV19f9
    0x2eb1S0x19f9: v2eb1V19f9 = ADD v2eab_0V19f9, v2e90V19f9
    0x2eb2S0x19f9: MSTORE v2eb1V19f9, v2eaeV19f9
    0x2eb3S0x19f9: v2eb3V19f9(0x20) = CONST 
    0x2eb5S0x19f9: v2eb5V19f9 = ADD v2eb3V19f9(0x20), v2eab_0V19f9
    0x2eb6S0x19f9: v2eb6V19f9(0x2ea2) = CONST 
    0x2eb9S0x19f9: JUMP v2eb6V19f9(0x2ea2)

    Begin block 0x2cf7B0x19f9
    prev=[0x2cdcB0x19f9], succ=[0x2d06B0x19f9]
    =================================
    0x2cf8S0x19f9: v2cf8V19f9(0x20) = CONST 
    0x2cfaS0x19f9: v2cfaV19f9 = ADD v2cf8V19f9(0x20), v2ce0V19f9
    0x2cfbS0x19f9: v2cfbV19f9(0x20) = CONST 
    0x2cfeS0x19f9: v2cfeV19f9 = MUL v876, v2cfbV19f9(0x20)
    0x2d00S0x19f9: v2d00V19f9 = CALLDATASIZE 
    0x2d02S0x19f9: CALLDATACOPY v2cfaV19f9, v2d00V19f9, v2cfeV19f9
    0x2d03S0x19f9: v2d03V19f9 = ADD v2cfeV19f9, v2cfaV19f9

    Begin block 0x2cb1B0x19f9
    prev=[0x2c96B0x19f9], succ=[0x2cc0B0x19f9]
    =================================
    0x2cb2S0x19f9: v2cb2V19f9(0x20) = CONST 
    0x2cb4S0x19f9: v2cb4V19f9 = ADD v2cb2V19f9(0x20), v2c9aV19f9
    0x2cb5S0x19f9: v2cb5V19f9(0x20) = CONST 
    0x2cb8S0x19f9: v2cb8V19f9 = MUL v876, v2cb5V19f9(0x20)
    0x2cbaS0x19f9: v2cbaV19f9 = CALLDATASIZE 
    0x2cbcS0x19f9: CALLDATACOPY v2cb4V19f9, v2cbaV19f9, v2cb8V19f9
    0x2cbdS0x19f9: v2cbdV19f9 = ADD v2cb8V19f9, v2cb4V19f9

}

function superInfo(uint256)() public {
    Begin block 0x8d2
    prev=[], succ=[0x8e4, 0x8e8]
    =================================
    0x8d3: v8d3(0x8ef) = CONST 
    0x8d6: v8d6(0x4) = CONST 
    0x8d9: v8d9 = CALLDATASIZE 
    0x8da: v8da = SUB v8d9, v8d6(0x4)
    0x8db: v8db(0x20) = CONST 
    0x8de: v8de = LT v8da, v8db(0x20)
    0x8df: v8df = ISZERO v8de
    0x8e0: v8e0(0x8e8) = CONST 
    0x8e3: JUMPI v8e0(0x8e8), v8df

    Begin block 0x8e4
    prev=[0x8d2], succ=[]
    =================================
    0x8e4: v8e4(0x0) = CONST 
    0x8e7: REVERT v8e4(0x0), v8e4(0x0)

    Begin block 0x8e8
    prev=[0x8d2], succ=[0x1a0e]
    =================================
    0x8ea: v8ea = CALLDATALOAD v8d6(0x4)
    0x8eb: v8eb(0x1a0e) = CONST 
    0x8ee: JUMP v8eb(0x1a0e)

    Begin block 0x1a0e
    prev=[0x8e8], succ=[0x1a5e, 0x1a8c]
    =================================
    0x1a0f: v1a0f(0x0) = CONST 
    0x1a13: MSTORE v1a0f(0x0), v8ea
    0x1a14: v1a14(0xa) = CONST 
    0x1a16: v1a16(0x20) = CONST 
    0x1a1a: MSTORE v1a16(0x20), v1a14(0xa)
    0x1a1b: v1a1b(0x40) = CONST 
    0x1a1f: v1a1f = SHA3 v1a0f(0x0), v1a1b(0x40)
    0x1a20: v1a20 = SLOAD v1a1f
    0x1a21: v1a21(0xc) = CONST 
    0x1a24: MSTORE v1a16(0x20), v1a21(0xc)
    0x1a28: v1a28 = SHA3 v1a0f(0x0), v1a1b(0x40)
    0x1a29: v1a29(0x2) = CONST 
    0x1a2c: v1a2c = ADD v1a28, v1a29(0x2)
    0x1a2d: v1a2d = SLOAD v1a2c
    0x1a2f: v1a2f = SLOAD v1a28
    0x1a31: v1a31 = MLOAD v1a1b(0x40)
    0x1a34: v1a34 = MUL v1a16(0x20), v1a2f
    0x1a36: v1a36 = ADD v1a31, v1a34
    0x1a38: v1a38 = ADD v1a16(0x20), v1a36
    0x1a3b: MSTORE v1a1b(0x40), v1a38
    0x1a3e: MSTORE v1a31, v1a2f
    0x1a3f: v1a3f(0x1) = CONST 
    0x1a41: v1a41(0x1) = CONST 
    0x1a43: v1a43(0x80) = CONST 
    0x1a45: v1a45(0x100000000000000000000000000000000) = SHL v1a43(0x80), v1a41(0x1)
    0x1a46: v1a46(0xffffffffffffffffffffffffffffffff) = SUB v1a45(0x100000000000000000000000000000000), v1a3f(0x1)
    0x1a49: v1a49 = AND v1a20, v1a46(0xffffffffffffffffffffffffffffffff)
    0x1a4b: v1a4b(0x60) = CONST 
    0x1a55: v1a55 = ADD v1a31, v1a16(0x20)
    0x1a59: v1a59 = ISZERO v1a2f
    0x1a5a: v1a5a(0x1a8c) = CONST 
    0x1a5d: JUMPI v1a5a(0x1a8c), v1a59

    Begin block 0x1a5e
    prev=[0x1a0e], succ=[0x1a6e]
    =================================
    0x1a5e: v1a5e(0x20) = CONST 
    0x1a60: v1a60 = MUL v1a5e(0x20), v1a2f
    0x1a62: v1a62 = ADD v1a55, v1a60
    0x1a65: v1a65(0x0) = CONST 
    0x1a67: MSTORE v1a65(0x0), v1a28
    0x1a68: v1a68(0x20) = CONST 
    0x1a6a: v1a6a(0x0) = CONST 
    0x1a6c: v1a6c = SHA3 v1a6a(0x0), v1a68(0x20)

    Begin block 0x1a6e
    prev=[0x1a5e, 0x1a6e], succ=[0x1a8c, 0x1a6e]
    =================================
    0x1a6e_0x0: v1a6e_0 = PHI v1a55, v1a84
    0x1a6e_0x1: v1a6e_1 = PHI v1a6c, v1a80
    0x1a70: v1a70 = SLOAD v1a6e_1
    0x1a71: v1a71(0x1) = CONST 
    0x1a73: v1a73(0x1) = CONST 
    0x1a75: v1a75(0xa0) = CONST 
    0x1a77: v1a77(0x10000000000000000000000000000000000000000) = SHL v1a75(0xa0), v1a73(0x1)
    0x1a78: v1a78(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a77(0x10000000000000000000000000000000000000000), v1a71(0x1)
    0x1a79: v1a79 = AND v1a78(0xffffffffffffffffffffffffffffffffffffffff), v1a70
    0x1a7b: MSTORE v1a6e_0, v1a79
    0x1a7c: v1a7c(0x1) = CONST 
    0x1a80: v1a80 = ADD v1a6e_1, v1a7c(0x1)
    0x1a82: v1a82(0x20) = CONST 
    0x1a84: v1a84 = ADD v1a82(0x20), v1a6e_0
    0x1a87: v1a87 = GT v1a62, v1a84
    0x1a88: v1a88(0x1a6e) = CONST 
    0x1a8b: JUMPI v1a88(0x1a6e), v1a87

    Begin block 0x1a8c
    prev=[0x1a0e, 0x1a6e], succ=[0x1acf, 0x1af3]
    =================================
    0x1a94: v1a94(0xc) = CONST 
    0x1a96: v1a96(0x0) = CONST 
    0x1a9a: MSTORE v1a96(0x0), v8ea
    0x1a9b: v1a9b(0x20) = CONST 
    0x1a9d: v1a9d(0x20) = ADD v1a9b(0x20), v1a96(0x0)
    0x1aa0: MSTORE v1a9d(0x20), v1a94(0xc)
    0x1aa1: v1aa1(0x20) = CONST 
    0x1aa3: v1aa3(0x40) = ADD v1aa1(0x20), v1a9d(0x20)
    0x1aa4: v1aa4(0x0) = CONST 
    0x1aa6: v1aa6 = SHA3 v1aa4(0x0), v1aa3(0x40)
    0x1aa7: v1aa7(0x1) = CONST 
    0x1aa9: v1aa9 = ADD v1aa7(0x1), v1aa6
    0x1aab: v1aab = SLOAD v1aa9
    0x1aad: v1aad(0x20) = CONST 
    0x1aaf: v1aaf = MUL v1aad(0x20), v1aab
    0x1ab0: v1ab0(0x20) = CONST 
    0x1ab2: v1ab2 = ADD v1ab0(0x20), v1aaf
    0x1ab3: v1ab3(0x40) = CONST 
    0x1ab5: v1ab5 = MLOAD v1ab3(0x40)
    0x1ab8: v1ab8 = ADD v1ab5, v1ab2
    0x1ab9: v1ab9(0x40) = CONST 
    0x1abb: MSTORE v1ab9(0x40), v1ab8
    0x1ac2: MSTORE v1ab5, v1aab
    0x1ac3: v1ac3(0x20) = CONST 
    0x1ac5: v1ac5 = ADD v1ac3(0x20), v1ab5
    0x1ac8: v1ac8 = SLOAD v1aa9
    0x1aca: v1aca = ISZERO v1ac8
    0x1acb: v1acb(0x1af3) = CONST 
    0x1ace: JUMPI v1acb(0x1af3), v1aca

    Begin block 0x1acf
    prev=[0x1a8c], succ=[0x1adf]
    =================================
    0x1acf: v1acf(0x20) = CONST 
    0x1ad1: v1ad1 = MUL v1acf(0x20), v1ac8
    0x1ad3: v1ad3 = ADD v1ac5, v1ad1
    0x1ad6: v1ad6(0x0) = CONST 
    0x1ad8: MSTORE v1ad6(0x0), v1aa9
    0x1ad9: v1ad9(0x20) = CONST 
    0x1adb: v1adb(0x0) = CONST 
    0x1add: v1add = SHA3 v1adb(0x0), v1ad9(0x20)

    Begin block 0x1adf
    prev=[0x1acf, 0x1adf], succ=[0x1af3, 0x1adf]
    =================================
    0x1adf_0x0: v1adf_0 = PHI v1ac5, v1ae6
    0x1adf_0x1: v1adf_1 = PHI v1add, v1aea
    0x1ae1: v1ae1 = SLOAD v1adf_1
    0x1ae3: MSTORE v1adf_0, v1ae1
    0x1ae4: v1ae4(0x20) = CONST 
    0x1ae6: v1ae6 = ADD v1ae4(0x20), v1adf_0
    0x1ae8: v1ae8(0x1) = CONST 
    0x1aea: v1aea = ADD v1ae8(0x1), v1adf_1
    0x1aee: v1aee = GT v1ad3, v1ae6
    0x1aef: v1aef(0x1adf) = CONST 
    0x1af2: JUMPI v1aef(0x1adf), v1aee

    Begin block 0x1af3
    prev=[0x1a8c, 0x1adf], succ=[0x8ef]
    =================================
    0x1b00: JUMP v8d3(0x8ef)

    Begin block 0x8ef
    prev=[0x1af3], succ=[0x930]
    =================================
    0x8f0: v8f0(0x40) = CONST 
    0x8f2: v8f2 = MLOAD v8f0(0x40)
    0x8f5: v8f5(0x1) = CONST 
    0x8f7: v8f7(0x1) = CONST 
    0x8f9: v8f9(0x80) = CONST 
    0x8fb: v8fb(0x100000000000000000000000000000000) = SHL v8f9(0x80), v8f7(0x1)
    0x8fc: v8fc(0xffffffffffffffffffffffffffffffff) = SUB v8fb(0x100000000000000000000000000000000), v8f5(0x1)
    0x8fd: v8fd = AND v8fc(0xffffffffffffffffffffffffffffffff), v1a49
    0x8ff: MSTORE v8f2, v8fd
    0x900: v900(0x20) = CONST 
    0x902: v902 = ADD v900(0x20), v8f2
    0x904: v904(0x20) = CONST 
    0x906: v906 = ADD v904(0x20), v902
    0x908: v908(0x20) = CONST 
    0x90a: v90a = ADD v908(0x20), v906
    0x90d: MSTORE v90a, v1a2d
    0x90e: v90e(0x20) = CONST 
    0x910: v910 = ADD v90e(0x20), v90a
    0x913: v913(0x80) = SUB v910, v8f2
    0x915: MSTORE v902, v913(0x80)
    0x919: v919 = MLOAD v1a31
    0x91b: MSTORE v910, v919
    0x91c: v91c(0x20) = CONST 
    0x91e: v91e = ADD v91c(0x20), v910
    0x922: v922 = MLOAD v1a31
    0x924: v924(0x20) = CONST 
    0x926: v926 = ADD v924(0x20), v1a31
    0x928: v928(0x20) = CONST 
    0x92a: v92a = MUL v928(0x20), v922
    0x92e: v92e(0x0) = CONST 

    Begin block 0x930
    prev=[0x8ef, 0x939], succ=[0x948, 0x939]
    =================================
    0x930_0x0: v930_0 = PHI v92e(0x0), v943
    0x933: v933 = LT v930_0, v92a
    0x934: v934 = ISZERO v933
    0x935: v935(0x948) = CONST 
    0x938: JUMPI v935(0x948), v934

    Begin block 0x948
    prev=[0x930], succ=[0x96f]
    =================================
    0x94f: v94f = ADD v92a, v91e
    0x952: v952 = SUB v94f, v8f2
    0x954: MSTORE v906, v952
    0x958: v958 = MLOAD v1ab5
    0x95a: MSTORE v94f, v958
    0x95b: v95b(0x20) = CONST 
    0x95d: v95d = ADD v95b(0x20), v94f
    0x961: v961 = MLOAD v1ab5
    0x963: v963(0x20) = CONST 
    0x965: v965 = ADD v963(0x20), v1ab5
    0x967: v967(0x20) = CONST 
    0x969: v969 = MUL v967(0x20), v961
    0x96d: v96d(0x0) = CONST 

    Begin block 0x96f
    prev=[0x948, 0x978], succ=[0x987, 0x978]
    =================================
    0x96f_0x0: v96f_0 = PHI v96d(0x0), v982
    0x972: v972 = LT v96f_0, v969
    0x973: v973 = ISZERO v972
    0x974: v974(0x987) = CONST 
    0x977: JUMPI v974(0x987), v973

    Begin block 0x987
    prev=[0x96f], succ=[]
    =================================
    0x98e: v98e = ADD v969, v95d
    0x997: v997(0x40) = CONST 
    0x999: v999 = MLOAD v997(0x40)
    0x99c: v99c = SUB v98e, v999
    0x99e: RETURN v999, v99c

    Begin block 0x978
    prev=[0x96f], succ=[0x96f]
    =================================
    0x978_0x0: v978_0 = PHI v96d(0x0), v982
    0x97a: v97a = ADD v978_0, v965
    0x97b: v97b = MLOAD v97a
    0x97e: v97e = ADD v978_0, v95d
    0x97f: MSTORE v97e, v97b
    0x980: v980(0x20) = CONST 
    0x982: v982 = ADD v980(0x20), v978_0
    0x983: v983(0x96f) = CONST 
    0x986: JUMP v983(0x96f)

    Begin block 0x939
    prev=[0x930], succ=[0x930]
    =================================
    0x939_0x0: v939_0 = PHI v92e(0x0), v943
    0x93b: v93b = ADD v939_0, v926
    0x93c: v93c = MLOAD v93b
    0x93f: v93f = ADD v939_0, v91e
    0x940: MSTORE v93f, v93c
    0x941: v941(0x20) = CONST 
    0x943: v943 = ADD v941(0x20), v939_0
    0x944: v944(0x930) = CONST 
    0x947: JUMP v944(0x930)

}

function updatePowah(address,uint256,uint256)() public {
    Begin block 0x99f
    prev=[], succ=[0x9b1, 0x9b5]
    =================================
    0x9a0: v9a0(0x3f60) = CONST 
    0x9a3: v9a3(0x4) = CONST 
    0x9a6: v9a6 = CALLDATASIZE 
    0x9a7: v9a7 = SUB v9a6, v9a3(0x4)
    0x9a8: v9a8(0x60) = CONST 
    0x9ab: v9ab = LT v9a7, v9a8(0x60)
    0x9ac: v9ac = ISZERO v9ab
    0x9ad: v9ad(0x9b5) = CONST 
    0x9b0: JUMPI v9ad(0x9b5), v9ac

    Begin block 0x9b1
    prev=[0x99f], succ=[]
    =================================
    0x9b1: v9b1(0x0) = CONST 
    0x9b4: REVERT v9b1(0x0), v9b1(0x0)

    Begin block 0x9b5
    prev=[0x99f], succ=[0x1b01]
    =================================
    0x9b7: v9b7(0x1) = CONST 
    0x9b9: v9b9(0x1) = CONST 
    0x9bb: v9bb(0xa0) = CONST 
    0x9bd: v9bd(0x10000000000000000000000000000000000000000) = SHL v9bb(0xa0), v9b9(0x1)
    0x9be: v9be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9bd(0x10000000000000000000000000000000000000000), v9b7(0x1)
    0x9c0: v9c0 = CALLDATALOAD v9a3(0x4)
    0x9c1: v9c1 = AND v9c0, v9be(0xffffffffffffffffffffffffffffffffffffffff)
    0x9c3: v9c3(0x20) = CONST 
    0x9c6: v9c6(0x24) = ADD v9a3(0x4), v9c3(0x20)
    0x9c7: v9c7 = CALLDATALOAD v9c6(0x24)
    0x9c9: v9c9(0x40) = CONST 
    0x9cb: v9cb(0x44) = ADD v9c9(0x40), v9a3(0x4)
    0x9cc: v9cc = CALLDATALOAD v9cb(0x44)
    0x9cd: v9cd(0x1b01) = CONST 
    0x9d0: JUMP v9cd(0x1b01)

    Begin block 0x1b01
    prev=[0x9b5], succ=[0x1b19, 0x1b58]
    =================================
    0x1b02: v1b02 = CALLER 
    0x1b03: v1b03(0x0) = CONST 
    0x1b07: MSTORE v1b03(0x0), v1b02
    0x1b08: v1b08(0x6) = CONST 
    0x1b0a: v1b0a(0x20) = CONST 
    0x1b0c: MSTORE v1b0a(0x20), v1b08(0x6)
    0x1b0d: v1b0d(0x40) = CONST 
    0x1b10: v1b10 = SHA3 v1b03(0x0), v1b0d(0x40)
    0x1b11: v1b11 = SLOAD v1b10
    0x1b12: v1b12(0xff) = CONST 
    0x1b14: v1b14 = AND v1b12(0xff), v1b11
    0x1b15: v1b15(0x1b58) = CONST 
    0x1b18: JUMPI v1b15(0x1b58), v1b14

    Begin block 0x1b19
    prev=[0x1b01], succ=[]
    =================================
    0x1b19: v1b19(0x40) = CONST 
    0x1b1c: v1b1c = MLOAD v1b19(0x40)
    0x1b1d: v1b1d(0x461bcd) = CONST 
    0x1b21: v1b21(0xe5) = CONST 
    0x1b23: v1b23(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b21(0xe5), v1b1d(0x461bcd)
    0x1b25: MSTORE v1b1c, v1b23(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b26: v1b26(0x20) = CONST 
    0x1b28: v1b28(0x4) = CONST 
    0x1b2b: v1b2b = ADD v1b1c, v1b28(0x4)
    0x1b2c: MSTORE v1b2b, v1b26(0x20)
    0x1b2d: v1b2d(0x10) = CONST 
    0x1b2f: v1b2f(0x24) = CONST 
    0x1b32: v1b32 = ADD v1b1c, v1b2f(0x24)
    0x1b33: MSTORE v1b32, v1b2d(0x10)
    0x1b34: v1b34(0x36bab9ba1031329037b832b930ba37b9) = CONST 
    0x1b45: v1b45(0x81) = CONST 
    0x1b47: v1b47(0x6d757374206265206f70657261746f7200000000000000000000000000000000) = SHL v1b45(0x81), v1b34(0x36bab9ba1031329037b832b930ba37b9)
    0x1b48: v1b48(0x44) = CONST 
    0x1b4b: v1b4b = ADD v1b1c, v1b48(0x44)
    0x1b4c: MSTORE v1b4b, v1b47(0x6d757374206265206f70657261746f7200000000000000000000000000000000)
    0x1b4e: v1b4e = MLOAD v1b19(0x40)
    0x1b52: v1b52(0x0) = SUB v1b1c, v1b4e
    0x1b53: v1b53(0x64) = CONST 
    0x1b55: v1b55(0x64) = ADD v1b53(0x64), v1b52(0x0)
    0x1b57: REVERT v1b4e, v1b55(0x64)

    Begin block 0x1b58
    prev=[0x1b01], succ=[0x1b62]
    =================================
    0x1b59: v1b59(0x1b62) = CONST 
    0x1b5e: v1b5e(0x2497) = CONST 
    0x1b61: v1b61_0 = CALLPRIVATE v1b5e(0x2497), v9c7, v9c1, v1b59(0x1b62)

    Begin block 0x1b62
    prev=[0x1b58], succ=[0x1b67, 0x1ba3]
    =================================
    0x1b63: v1b63(0x1ba3) = CONST 
    0x1b66: JUMPI v1b63(0x1ba3), v1b61_0

    Begin block 0x1b67
    prev=[0x1b62], succ=[]
    =================================
    0x1b67: v1b67(0x40) = CONST 
    0x1b6a: v1b6a = MLOAD v1b67(0x40)
    0x1b6b: v1b6b(0x461bcd) = CONST 
    0x1b6f: v1b6f(0xe5) = CONST 
    0x1b71: v1b71(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b6f(0xe5), v1b6b(0x461bcd)
    0x1b73: MSTORE v1b6a, v1b71(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b74: v1b74(0x20) = CONST 
    0x1b76: v1b76(0x4) = CONST 
    0x1b79: v1b79 = ADD v1b6a, v1b76(0x4)
    0x1b7a: MSTORE v1b79, v1b74(0x20)
    0x1b7b: v1b7b(0xd) = CONST 
    0x1b7d: v1b7d(0x24) = CONST 
    0x1b80: v1b80 = ADD v1b6a, v1b7d(0x24)
    0x1b81: MSTORE v1b80, v1b7b(0xd)
    0x1b82: v1b82(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1b90: v1b90(0x99) = CONST 
    0x1b92: v1b92(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1b90(0x99), v1b82(0x26bab9ba1031329037bbb732b9)
    0x1b93: v1b93(0x44) = CONST 
    0x1b96: v1b96 = ADD v1b6a, v1b93(0x44)
    0x1b97: MSTORE v1b96, v1b92(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1b99: v1b99 = MLOAD v1b67(0x40)
    0x1b9d: v1b9d(0x0) = SUB v1b6a, v1b99
    0x1b9e: v1b9e(0x64) = CONST 
    0x1ba0: v1ba0(0x64) = ADD v1b9e(0x64), v1b9d(0x0)
    0x1ba2: REVERT v1b99, v1ba0(0x64)

    Begin block 0x1ba3
    prev=[0x1b62], succ=[0x2f36B0x1ba3]
    =================================
    0x1ba4: v1ba4(0x0) = CONST 
    0x1ba8: MSTORE v1ba4(0x0), v9c7
    0x1ba9: v1ba9(0xa) = CONST 
    0x1bab: v1bab(0x20) = CONST 
    0x1bad: MSTORE v1bab(0x20), v1ba9(0xa)
    0x1bae: v1bae(0x40) = CONST 
    0x1bb2: v1bb2 = SHA3 v1ba4(0x0), v1bae(0x40)
    0x1bb3: v1bb3 = SLOAD v1bb2
    0x1bb5: v1bb5 = MLOAD v1bae(0x40)
    0x1bb8: v1bb8(0x1) = CONST 
    0x1bba: v1bba(0x80) = CONST 
    0x1bbc: v1bbc(0x100000000000000000000000000000000) = SHL v1bba(0x80), v1bb8(0x1)
    0x1bbf: v1bbf = DIV v1bb3, v1bbc(0x100000000000000000000000000000000)
    0x1bc0: v1bc0(0x1) = CONST 
    0x1bc2: v1bc2(0x1) = CONST 
    0x1bc4: v1bc4(0x80) = CONST 
    0x1bc6: v1bc6(0x100000000000000000000000000000000) = SHL v1bc4(0x80), v1bc2(0x1)
    0x1bc7: v1bc7(0xffffffffffffffffffffffffffffffff) = SUB v1bc6(0x100000000000000000000000000000000), v1bc0(0x1)
    0x1bc8: v1bc8 = AND v1bc7(0xffffffffffffffffffffffffffffffff), v1bbf
    0x1bcc: v1bcc(0xcfd7d36b449fead22a7599b08c1ce0ae53d225deb29efd38f057f6891485a858) = CONST 
    0x1bef: LOG4 v1bb5, v1ba4(0x0), v1bcc(0xcfd7d36b449fead22a7599b08c1ce0ae53d225deb29efd38f057f6891485a858), v9c7, v1bc8, v9cc
    0x1bf0: v1bf0(0x0) = CONST 
    0x1bf4: MSTORE v1bf0(0x0), v9c7
    0x1bf5: v1bf5(0xa) = CONST 
    0x1bf7: v1bf7(0x20) = CONST 
    0x1bf9: MSTORE v1bf7(0x20), v1bf5(0xa)
    0x1bfa: v1bfa(0x40) = CONST 
    0x1bfd: v1bfd = SHA3 v1bf0(0x0), v1bfa(0x40)
    0x1bfe: v1bfe = SLOAD v1bfd
    0x1bff: v1bff(0x1c1c) = CONST 
    0x1c07: v1c07(0x1) = CONST 
    0x1c09: v1c09(0x80) = CONST 
    0x1c0b: v1c0b(0x100000000000000000000000000000000) = SHL v1c09(0x80), v1c07(0x1)
    0x1c0d: v1c0d = DIV v1bfe, v1c0b(0x100000000000000000000000000000000)
    0x1c0e: v1c0e(0x1) = CONST 
    0x1c10: v1c10(0x1) = CONST 
    0x1c12: v1c12(0x80) = CONST 
    0x1c14: v1c14(0x100000000000000000000000000000000) = SHL v1c12(0x80), v1c10(0x1)
    0x1c15: v1c15(0xffffffffffffffffffffffffffffffff) = SUB v1c14(0x100000000000000000000000000000000), v1c0e(0x1)
    0x1c16: v1c16 = AND v1c15(0xffffffffffffffffffffffffffffffff), v1c0d
    0x1c18: v1c18(0x2f36) = CONST 
    0x1c1b: JUMP v1c18(0x2f36), v9cc, v1c16, v9c7, v9c1, v1bff(0x1c1c)

    Begin block 0x2f36B0x1ba3
    prev=[0x1ba3], succ=[0x3684B0x2f36B0x1ba3]
    =================================
    0x2f37S0x1ba3: v2f37V1ba3(0x2f48) = CONST 
    0x2f3bS0x1ba3: v2f3bV1ba3(0x1) = CONST 
    0x2f3dS0x1ba3: v2f3dV1ba3(0x1) = CONST 
    0x2f3fS0x1ba3: v2f3fV1ba3(0xa0) = CONST 
    0x2f41S0x1ba3: v2f41V1ba3(0x10000000000000000000000000000000000000000) = SHL v2f3fV1ba3(0xa0), v2f3dV1ba3(0x1)
    0x2f42S0x1ba3: v2f42V1ba3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f41V1ba3(0x10000000000000000000000000000000000000000), v2f3bV1ba3(0x1)
    0x2f43S0x1ba3: v2f43V1ba3 = AND v2f42V1ba3(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x2f44S0x1ba3: v2f44V1ba3(0x3684) = CONST 
    0x2f47S0x1ba3: JUMP v2f44V1ba3(0x3684)

    Begin block 0x3684B0x2f36B0x1ba3
    prev=[0x2f36B0x1ba3], succ=[0x2f48B0x1ba3]
    =================================
    0x3685S0x2f36S0x1ba3: v3685V2f36V1ba3 = EXTCODESIZE v2f43V1ba3
    0x3686S0x2f36S0x1ba3: v3686V2f36V1ba3 = ISZERO v3685V2f36V1ba3
    0x3687S0x2f36S0x1ba3: v3687V2f36V1ba3 = ISZERO v3686V2f36V1ba3
    0x3689S0x2f36S0x1ba3: JUMP v2f37V1ba3(0x2f48)

    Begin block 0x2f48B0x1ba3
    prev=[0x3684B0x2f36B0x1ba3], succ=[0x2f61B0x1ba3, 0x2f4fB0x1ba3]
    =================================
    0x2f4aS0x1ba3: v2f4aV1ba3 = ISZERO v3687V2f36V1ba3
    0x2f4bS0x1ba3: v2f4bV1ba3(0x2f61) = CONST 
    0x2f4eS0x1ba3: JUMPI v2f4bV1ba3(0x2f61), v2f4aV1ba3

    Begin block 0x2f61B0x1ba3
    prev=[0x2f48B0x1ba3, 0x2f4fB0x1ba3], succ=[0x2f67B0x1ba3, 0x44bbB0x1ba3]
    =================================
    0x2f61_0x0S0x1ba3: v2f61_0V1ba3 = PHI v2f60_0V1ba3, v3687V2f36V1ba3
    0x2f62S0x1ba3: v2f62V1ba3 = ISZERO v2f61_0V1ba3
    0x2f63S0x1ba3: v2f63V1ba3(0x44bb) = CONST 
    0x2f66S0x1ba3: JUMPI v2f63V1ba3(0x44bb), v2f62V1ba3

    Begin block 0x2f67B0x1ba3
    prev=[0x2f61B0x1ba3], succ=[0x2fafB0x1ba3, 0x2fb3B0x1ba3]
    =================================
    0x2f67S0x1ba3: v2f67V1ba3(0x40) = CONST 
    0x2f6aS0x1ba3: v2f6aV1ba3 = MLOAD v2f67V1ba3(0x40)
    0x2f6bS0x1ba3: v2f6bV1ba3(0x1ffc9a7) = CONST 
    0x2f70S0x1ba3: v2f70V1ba3(0xe0) = CONST 
    0x2f72S0x1ba3: v2f72V1ba3(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v2f70V1ba3(0xe0), v2f6bV1ba3(0x1ffc9a7)
    0x2f74S0x1ba3: MSTORE v2f6aV1ba3, v2f72V1ba3(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x2f75S0x1ba3: v2f75V1ba3(0x50e84861) = CONST 
    0x2f7aS0x1ba3: v2f7aV1ba3(0xe0) = CONST 
    0x2f7cS0x1ba3: v2f7cV1ba3(0x50e8486100000000000000000000000000000000000000000000000000000000) = SHL v2f7aV1ba3(0xe0), v2f75V1ba3(0x50e84861)
    0x2f7dS0x1ba3: v2f7dV1ba3(0x4) = CONST 
    0x2f80S0x1ba3: v2f80V1ba3 = ADD v2f6aV1ba3, v2f7dV1ba3(0x4)
    0x2f81S0x1ba3: MSTORE v2f80V1ba3, v2f7cV1ba3(0x50e8486100000000000000000000000000000000000000000000000000000000)
    0x2f83S0x1ba3: v2f83V1ba3 = MLOAD v2f67V1ba3(0x40)
    0x2f84S0x1ba3: v2f84V1ba3(0x1) = CONST 
    0x2f86S0x1ba3: v2f86V1ba3(0x1) = CONST 
    0x2f88S0x1ba3: v2f88V1ba3(0xa0) = CONST 
    0x2f8aS0x1ba3: v2f8aV1ba3(0x10000000000000000000000000000000000000000) = SHL v2f88V1ba3(0xa0), v2f86V1ba3(0x1)
    0x2f8bS0x1ba3: v2f8bV1ba3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f8aV1ba3(0x10000000000000000000000000000000000000000), v2f84V1ba3(0x1)
    0x2f8dS0x1ba3: v2f8dV1ba3 = AND v9c1, v2f8bV1ba3(0xffffffffffffffffffffffffffffffffffffffff)
    0x2f8fS0x1ba3: v2f8fV1ba3(0x1ffc9a7) = CONST 
    0x2f95S0x1ba3: v2f95V1ba3(0x24) = CONST 
    0x2f99S0x1ba3: v2f99V1ba3 = ADD v2f6aV1ba3, v2f95V1ba3(0x24)
    0x2f9bS0x1ba3: v2f9bV1ba3(0x20) = CONST 
    0x2fa2S0x1ba3: v2fa2V1ba3(0x0) = SUB v2f6aV1ba3, v2f83V1ba3
    0x2fa3S0x1ba3: v2fa3V1ba3(0x24) = ADD v2fa2V1ba3(0x0), v2f95V1ba3(0x24)
    0x2fa7S0x1ba3: v2fa7V1ba3 = EXTCODESIZE v2f8dV1ba3
    0x2fa8S0x1ba3: v2fa8V1ba3 = ISZERO v2fa7V1ba3
    0x2faaS0x1ba3: v2faaV1ba3 = ISZERO v2fa8V1ba3
    0x2fabS0x1ba3: v2fabV1ba3(0x2fb3) = CONST 
    0x2faeS0x1ba3: JUMPI v2fabV1ba3(0x2fb3), v2faaV1ba3

    Begin block 0x2fafB0x1ba3
    prev=[0x2f67B0x1ba3], succ=[]
    =================================
    0x2fafS0x1ba3: v2fafV1ba3(0x0) = CONST 
    0x2fb2S0x1ba3: REVERT v2fafV1ba3(0x0), v2fafV1ba3(0x0)

    Begin block 0x2fb3B0x1ba3
    prev=[0x2f67B0x1ba3], succ=[0x2fbeB0x1ba3, 0x2fc7B0x1ba3]
    =================================
    0x2fb5S0x1ba3: v2fb5V1ba3 = GAS 
    0x2fb6S0x1ba3: v2fb6V1ba3 = STATICCALL v2fb5V1ba3, v2f8dV1ba3, v2f83V1ba3, v2fa3V1ba3(0x24), v2f83V1ba3, v2f9bV1ba3(0x20)
    0x2fb7S0x1ba3: v2fb7V1ba3 = ISZERO v2fb6V1ba3
    0x2fb9S0x1ba3: v2fb9V1ba3 = ISZERO v2fb7V1ba3
    0x2fbaS0x1ba3: v2fbaV1ba3(0x2fc7) = CONST 
    0x2fbdS0x1ba3: JUMPI v2fbaV1ba3(0x2fc7), v2fb9V1ba3

    Begin block 0x2fbeB0x1ba3
    prev=[0x2fb3B0x1ba3], succ=[]
    =================================
    0x2fbeS0x1ba3: v2fbeV1ba3 = RETURNDATASIZE 
    0x2fbfS0x1ba3: v2fbfV1ba3(0x0) = CONST 
    0x2fc2S0x1ba3: RETURNDATACOPY v2fbfV1ba3(0x0), v2fbfV1ba3(0x0), v2fbeV1ba3
    0x2fc3S0x1ba3: v2fc3V1ba3 = RETURNDATASIZE 
    0x2fc4S0x1ba3: v2fc4V1ba3(0x0) = CONST 
    0x2fc6S0x1ba3: REVERT v2fc4V1ba3(0x0), v2fc3V1ba3

    Begin block 0x2fc7B0x1ba3
    prev=[0x2fb3B0x1ba3], succ=[0x2fd9B0x1ba3, 0x2fddB0x1ba3]
    =================================
    0x2fccS0x1ba3: v2fccV1ba3(0x40) = CONST 
    0x2fceS0x1ba3: v2fceV1ba3 = MLOAD v2fccV1ba3(0x40)
    0x2fcfS0x1ba3: v2fcfV1ba3 = RETURNDATASIZE 
    0x2fd0S0x1ba3: v2fd0V1ba3(0x20) = CONST 
    0x2fd3S0x1ba3: v2fd3V1ba3 = LT v2fcfV1ba3, v2fd0V1ba3(0x20)
    0x2fd4S0x1ba3: v2fd4V1ba3 = ISZERO v2fd3V1ba3
    0x2fd5S0x1ba3: v2fd5V1ba3(0x2fdd) = CONST 
    0x2fd8S0x1ba3: JUMPI v2fd5V1ba3(0x2fdd), v2fd4V1ba3

    Begin block 0x2fd9B0x1ba3
    prev=[0x2fc7B0x1ba3], succ=[]
    =================================
    0x2fd9S0x1ba3: v2fd9V1ba3(0x0) = CONST 
    0x2fdcS0x1ba3: REVERT v2fd9V1ba3(0x0), v2fd9V1ba3(0x0)

    Begin block 0x2fddB0x1ba3
    prev=[0x2fc7B0x1ba3], succ=[0x2fe5B0x1ba3, 0x44e0B0x1ba3]
    =================================
    0x2fdfS0x1ba3: v2fdfV1ba3 = MLOAD v2fceV1ba3
    0x2fe0S0x1ba3: v2fe0V1ba3 = ISZERO v2fdfV1ba3
    0x2fe1S0x1ba3: v2fe1V1ba3(0x44e0) = CONST 
    0x2fe4S0x1ba3: JUMPI v2fe1V1ba3(0x44e0), v2fe0V1ba3

    Begin block 0x2fe5B0x1ba3
    prev=[0x2fddB0x1ba3], succ=[0x3036B0x1ba3, 0x303aB0x1ba3]
    =================================
    0x2fe6S0x1ba3: v2fe6V1ba3(0x1) = CONST 
    0x2fe8S0x1ba3: v2fe8V1ba3(0x1) = CONST 
    0x2feaS0x1ba3: v2feaV1ba3(0xa0) = CONST 
    0x2fecS0x1ba3: v2fecV1ba3(0x10000000000000000000000000000000000000000) = SHL v2feaV1ba3(0xa0), v2fe8V1ba3(0x1)
    0x2fedS0x1ba3: v2fedV1ba3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2fecV1ba3(0x10000000000000000000000000000000000000000), v2fe6V1ba3(0x1)
    0x2feeS0x1ba3: v2feeV1ba3 = AND v2fedV1ba3(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x2fefS0x1ba3: v2fefV1ba3(0x50e84861) = CONST 
    0x2ff7S0x1ba3: v2ff7V1ba3(0x40) = CONST 
    0x2ff9S0x1ba3: v2ff9V1ba3 = MLOAD v2ff7V1ba3(0x40)
    0x2ffbS0x1ba3: v2ffbV1ba3(0xffffffff) = CONST 
    0x3000S0x1ba3: v3000V1ba3(0x50e84861) = AND v2ffbV1ba3(0xffffffff), v2fefV1ba3(0x50e84861)
    0x3001S0x1ba3: v3001V1ba3(0xe0) = CONST 
    0x3003S0x1ba3: v3003V1ba3(0x50e8486100000000000000000000000000000000000000000000000000000000) = SHL v3001V1ba3(0xe0), v3000V1ba3(0x50e84861)
    0x3005S0x1ba3: MSTORE v2ff9V1ba3, v3003V1ba3(0x50e8486100000000000000000000000000000000000000000000000000000000)
    0x3006S0x1ba3: v3006V1ba3(0x4) = CONST 
    0x3008S0x1ba3: v3008V1ba3 = ADD v3006V1ba3(0x4), v2ff9V1ba3
    0x300cS0x1ba3: MSTORE v3008V1ba3, v9c7
    0x300dS0x1ba3: v300dV1ba3(0x20) = CONST 
    0x300fS0x1ba3: v300fV1ba3 = ADD v300dV1ba3(0x20), v3008V1ba3
    0x3012S0x1ba3: MSTORE v300fV1ba3, v1c16
    0x3013S0x1ba3: v3013V1ba3(0x20) = CONST 
    0x3015S0x1ba3: v3015V1ba3 = ADD v3013V1ba3(0x20), v300fV1ba3
    0x3018S0x1ba3: MSTORE v3015V1ba3, v9cc
    0x3019S0x1ba3: v3019V1ba3(0x20) = CONST 
    0x301bS0x1ba3: v301bV1ba3 = ADD v3019V1ba3(0x20), v3015V1ba3
    0x3021S0x1ba3: v3021V1ba3(0x0) = CONST 
    0x3023S0x1ba3: v3023V1ba3(0x40) = CONST 
    0x3025S0x1ba3: v3025V1ba3 = MLOAD v3023V1ba3(0x40)
    0x3028S0x1ba3: v3028V1ba3(0x64) = SUB v301bV1ba3, v3025V1ba3
    0x302aS0x1ba3: v302aV1ba3(0x0) = CONST 
    0x302eS0x1ba3: v302eV1ba3 = EXTCODESIZE v2feeV1ba3
    0x302fS0x1ba3: v302fV1ba3 = ISZERO v302eV1ba3
    0x3031S0x1ba3: v3031V1ba3 = ISZERO v302fV1ba3
    0x3032S0x1ba3: v3032V1ba3(0x303a) = CONST 
    0x3035S0x1ba3: JUMPI v3032V1ba3(0x303a), v3031V1ba3

    Begin block 0x3036B0x1ba3
    prev=[0x2fe5B0x1ba3], succ=[]
    =================================
    0x3036S0x1ba3: v3036V1ba3(0x0) = CONST 
    0x3039S0x1ba3: REVERT v3036V1ba3(0x0), v3036V1ba3(0x0)

    Begin block 0x303aB0x1ba3
    prev=[0x2fe5B0x1ba3], succ=[0x3045B0x1ba3, 0x304eB0x1ba3]
    =================================
    0x303cS0x1ba3: v303cV1ba3 = GAS 
    0x303dS0x1ba3: v303dV1ba3 = CALL v303cV1ba3, v2feeV1ba3, v302aV1ba3(0x0), v3025V1ba3, v3028V1ba3(0x64), v3025V1ba3, v3021V1ba3(0x0)
    0x303eS0x1ba3: v303eV1ba3 = ISZERO v303dV1ba3
    0x3040S0x1ba3: v3040V1ba3 = ISZERO v303eV1ba3
    0x3041S0x1ba3: v3041V1ba3(0x304e) = CONST 
    0x3044S0x1ba3: JUMPI v3041V1ba3(0x304e), v3040V1ba3

    Begin block 0x3045B0x1ba3
    prev=[0x303aB0x1ba3], succ=[]
    =================================
    0x3045S0x1ba3: v3045V1ba3 = RETURNDATASIZE 
    0x3046S0x1ba3: v3046V1ba3(0x0) = CONST 
    0x3049S0x1ba3: RETURNDATACOPY v3046V1ba3(0x0), v3046V1ba3(0x0), v3045V1ba3
    0x304aS0x1ba3: v304aV1ba3 = RETURNDATASIZE 
    0x304bS0x1ba3: v304bV1ba3(0x0) = CONST 
    0x304dS0x1ba3: REVERT v304bV1ba3(0x0), v304aV1ba3

    Begin block 0x304eB0x1ba3
    prev=[0x303aB0x1ba3], succ=[0x3053B0x1ba3]
    =================================

    Begin block 0x3053B0x1ba3
    prev=[0x304eB0x1ba3], succ=[0x1c1c]
    =================================
    0x3058S0x1ba3: JUMP v1bff(0x1c1c)

    Begin block 0x1c1c
    prev=[0x44bbB0x1ba3, 0x44e0B0x1ba3, 0x3053B0x1ba3], succ=[0x3f60]
    =================================
    0x1c1d: v1c1d(0x0) = CONST 
    0x1c21: MSTORE v1c1d(0x0), v9c7
    0x1c22: v1c22(0xa) = CONST 
    0x1c24: v1c24(0x20) = CONST 
    0x1c26: MSTORE v1c24(0x20), v1c22(0xa)
    0x1c27: v1c27(0x40) = CONST 
    0x1c2b: v1c2b = SHA3 v1c1d(0x0), v1c27(0x40)
    0x1c2d: v1c2d = SLOAD v1c2b
    0x1c2e: v1c2e(0x1) = CONST 
    0x1c30: v1c30(0x1) = CONST 
    0x1c32: v1c32(0x80) = CONST 
    0x1c34: v1c34(0x100000000000000000000000000000000) = SHL v1c32(0x80), v1c30(0x1)
    0x1c35: v1c35(0xffffffffffffffffffffffffffffffff) = SUB v1c34(0x100000000000000000000000000000000), v1c2e(0x1)
    0x1c38: v1c38 = AND v1c35(0xffffffffffffffffffffffffffffffff), v9cc
    0x1c39: v1c39(0x1) = CONST 
    0x1c3b: v1c3b(0x80) = CONST 
    0x1c3d: v1c3d(0x100000000000000000000000000000000) = SHL v1c3b(0x80), v1c39(0x1)
    0x1c3e: v1c3e = MUL v1c3d(0x100000000000000000000000000000000), v1c38
    0x1c40: v1c40 = AND v1c35(0xffffffffffffffffffffffffffffffff), v1c2d
    0x1c44: v1c44 = OR v1c40, v1c3e
    0x1c46: SSTORE v1c2b, v1c44
    0x1c48: JUMP v9a0(0x3f60)

    Begin block 0x3f60
    prev=[0x1c1c], succ=[]
    =================================
    0x3f61: STOP 

    Begin block 0x44e0B0x1ba3
    prev=[0x2fddB0x1ba3], succ=[0x1c1c]
    =================================
    0x44e5S0x1ba3: JUMP v1bff(0x1c1c)

    Begin block 0x44bbB0x1ba3
    prev=[0x2f61B0x1ba3], succ=[0x1c1c]
    =================================
    0x44c0S0x1ba3: JUMP v1bff(0x1c1c)

    Begin block 0x2f4fB0x1ba3
    prev=[0x2f48B0x1ba3], succ=[0x2f61B0x1ba3]
    =================================
    0x2f50S0x1ba3: v2f50V1ba3(0x2f61) = CONST 
    0x2f54S0x1ba3: v2f54V1ba3(0x1) = CONST 
    0x2f56S0x1ba3: v2f56V1ba3(0x1) = CONST 
    0x2f58S0x1ba3: v2f58V1ba3(0xa0) = CONST 
    0x2f5aS0x1ba3: v2f5aV1ba3(0x10000000000000000000000000000000000000000) = SHL v2f58V1ba3(0xa0), v2f56V1ba3(0x1)
    0x2f5bS0x1ba3: v2f5bV1ba3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f5aV1ba3(0x10000000000000000000000000000000000000000), v2f54V1ba3(0x1)
    0x2f5cS0x1ba3: v2f5cV1ba3 = AND v2f5bV1ba3(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x2f5dS0x1ba3: v2f5dV1ba3(0x368a) = CONST 
    0x2f60S0x1ba3: v2f60_0V1ba3 = CALLPRIVATE v2f5dV1ba3(0x368a), v2f5cV1ba3, v2f50V1ba3(0x2f61)

}

function galaxyCommunity()() public {
    Begin block 0x9d1
    prev=[], succ=[0x1c49]
    =================================
    0x9d2: v9d2(0x3f81) = CONST 
    0x9d5: v9d5(0x1c49) = CONST 
    0x9d8: JUMP v9d5(0x1c49)

    Begin block 0x1c49
    prev=[0x9d1], succ=[0x3f81]
    =================================
    0x1c4a: v1c4a(0x4) = CONST 
    0x1c4c: v1c4c = SLOAD v1c4a(0x4)
    0x1c4d: v1c4d(0x1) = CONST 
    0x1c4f: v1c4f(0x1) = CONST 
    0x1c51: v1c51(0xa0) = CONST 
    0x1c53: v1c53(0x10000000000000000000000000000000000000000) = SHL v1c51(0xa0), v1c4f(0x1)
    0x1c54: v1c54(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c53(0x10000000000000000000000000000000000000000), v1c4d(0x1)
    0x1c55: v1c55 = AND v1c54(0xffffffffffffffffffffffffffffffffffffffff), v1c4c
    0x1c57: JUMP v9d2(0x3f81)

    Begin block 0x3f81
    prev=[0x1c49], succ=[]
    =================================
    0x3f82: v3f82(0x40) = CONST 
    0x3f85: v3f85 = MLOAD v3f82(0x40)
    0x3f86: v3f86(0x1) = CONST 
    0x3f88: v3f88(0x1) = CONST 
    0x3f8a: v3f8a(0xa0) = CONST 
    0x3f8c: v3f8c(0x10000000000000000000000000000000000000000) = SHL v3f8a(0xa0), v3f88(0x1)
    0x3f8d: v3f8d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f8c(0x10000000000000000000000000000000000000000), v3f86(0x1)
    0x3f90: v3f90 = AND v1c55, v3f8d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f92: MSTORE v3f85, v3f90
    0x3f93: v3f93 = MLOAD v3f82(0x40)
    0x3f97: v3f97(0x0) = SUB v3f85, v3f93
    0x3f98: v3f98(0x20) = CONST 
    0x3f9a: v3f9a(0x20) = ADD v3f98(0x20), v3f97(0x0)
    0x3f9c: RETURN v3f93, v3f9a(0x20)

}

function addMinter(address)() public {
    Begin block 0x9f5
    prev=[], succ=[0xa07, 0xa0b]
    =================================
    0x9f6: v9f6(0x3fbc) = CONST 
    0x9f9: v9f9(0x4) = CONST 
    0x9fc: v9fc = CALLDATASIZE 
    0x9fd: v9fd = SUB v9fc, v9f9(0x4)
    0x9fe: v9fe(0x20) = CONST 
    0xa01: va01 = LT v9fd, v9fe(0x20)
    0xa02: va02 = ISZERO va01
    0xa03: va03(0xa0b) = CONST 
    0xa06: JUMPI va03(0xa0b), va02

    Begin block 0xa07
    prev=[0x9f5], succ=[]
    =================================
    0xa07: va07(0x0) = CONST 
    0xa0a: REVERT va07(0x0), va07(0x0)

    Begin block 0xa0b
    prev=[0x9f5], succ=[0x1c58]
    =================================
    0xa0d: va0d = CALLDATALOAD v9f9(0x4)
    0xa0e: va0e(0x1) = CONST 
    0xa10: va10(0x1) = CONST 
    0xa12: va12(0xa0) = CONST 
    0xa14: va14(0x10000000000000000000000000000000000000000) = SHL va12(0xa0), va10(0x1)
    0xa15: va15(0xffffffffffffffffffffffffffffffffffffffff) = SUB va14(0x10000000000000000000000000000000000000000), va0e(0x1)
    0xa16: va16 = AND va15(0xffffffffffffffffffffffffffffffffffffffff), va0d
    0xa17: va17(0x1c58) = CONST 
    0xa1a: JUMP va17(0x1c58)

    Begin block 0x1c58
    prev=[0xa0b], succ=[0x1c6b, 0x1ca7]
    =================================
    0x1c59: v1c59(0x3) = CONST 
    0x1c5b: v1c5b = SLOAD v1c59(0x3)
    0x1c5c: v1c5c(0x1) = CONST 
    0x1c5e: v1c5e(0x1) = CONST 
    0x1c60: v1c60(0xa0) = CONST 
    0x1c62: v1c62(0x10000000000000000000000000000000000000000) = SHL v1c60(0xa0), v1c5e(0x1)
    0x1c63: v1c63(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c62(0x10000000000000000000000000000000000000000), v1c5c(0x1)
    0x1c64: v1c64 = AND v1c63(0xffffffffffffffffffffffffffffffffffffffff), v1c5b
    0x1c65: v1c65 = CALLER 
    0x1c66: v1c66 = EQ v1c65, v1c64
    0x1c67: v1c67(0x1ca7) = CONST 
    0x1c6a: JUMPI v1c67(0x1ca7), v1c66

    Begin block 0x1c6b
    prev=[0x1c58], succ=[]
    =================================
    0x1c6b: v1c6b(0x40) = CONST 
    0x1c6e: v1c6e = MLOAD v1c6b(0x40)
    0x1c6f: v1c6f(0x461bcd) = CONST 
    0x1c73: v1c73(0xe5) = CONST 
    0x1c75: v1c75(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c73(0xe5), v1c6f(0x461bcd)
    0x1c77: MSTORE v1c6e, v1c75(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c78: v1c78(0x20) = CONST 
    0x1c7a: v1c7a(0x4) = CONST 
    0x1c7d: v1c7d = ADD v1c6e, v1c7a(0x4)
    0x1c7e: MSTORE v1c7d, v1c78(0x20)
    0x1c7f: v1c7f(0xd) = CONST 
    0x1c81: v1c81(0x24) = CONST 
    0x1c84: v1c84 = ADD v1c6e, v1c81(0x24)
    0x1c85: MSTORE v1c84, v1c7f(0xd)
    0x1c86: v1c86(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1c94: v1c94(0x99) = CONST 
    0x1c96: v1c96(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1c94(0x99), v1c86(0x26bab9ba1031329037bbb732b9)
    0x1c97: v1c97(0x44) = CONST 
    0x1c9a: v1c9a = ADD v1c6e, v1c97(0x44)
    0x1c9b: MSTORE v1c9a, v1c96(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1c9d: v1c9d = MLOAD v1c6b(0x40)
    0x1ca1: v1ca1(0x0) = SUB v1c6e, v1c9d
    0x1ca2: v1ca2(0x64) = CONST 
    0x1ca4: v1ca4(0x64) = ADD v1ca2(0x64), v1ca1(0x0)
    0x1ca6: REVERT v1c9d, v1ca4(0x64)

    Begin block 0x1ca7
    prev=[0x1c58], succ=[0x1cb6, 0x1d02]
    =================================
    0x1ca8: v1ca8(0x1) = CONST 
    0x1caa: v1caa(0x1) = CONST 
    0x1cac: v1cac(0xa0) = CONST 
    0x1cae: v1cae(0x10000000000000000000000000000000000000000) = SHL v1cac(0xa0), v1caa(0x1)
    0x1caf: v1caf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cae(0x10000000000000000000000000000000000000000), v1ca8(0x1)
    0x1cb1: v1cb1 = AND va16, v1caf(0xffffffffffffffffffffffffffffffffffffffff)
    0x1cb2: v1cb2(0x1d02) = CONST 
    0x1cb5: JUMPI v1cb2(0x1d02), v1cb1

    Begin block 0x1cb6
    prev=[0x1ca7], succ=[]
    =================================
    0x1cb6: v1cb6(0x40) = CONST 
    0x1cb9: v1cb9 = MLOAD v1cb6(0x40)
    0x1cba: v1cba(0x461bcd) = CONST 
    0x1cbe: v1cbe(0xe5) = CONST 
    0x1cc0: v1cc0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1cbe(0xe5), v1cba(0x461bcd)
    0x1cc2: MSTORE v1cb9, v1cc0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cc3: v1cc3(0x20) = CONST 
    0x1cc5: v1cc5(0x4) = CONST 
    0x1cc8: v1cc8 = ADD v1cb9, v1cc5(0x4)
    0x1cc9: MSTORE v1cc8, v1cc3(0x20)
    0x1cca: v1cca(0x1f) = CONST 
    0x1ccc: v1ccc(0x24) = CONST 
    0x1ccf: v1ccf = ADD v1cb9, v1ccc(0x24)
    0x1cd0: MSTORE v1ccf, v1cca(0x1f)
    0x1cd1: v1cd1(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300) = CONST 
    0x1cf2: v1cf2(0x44) = CONST 
    0x1cf5: v1cf5 = ADD v1cb9, v1cf2(0x44)
    0x1cf6: MSTORE v1cf5, v1cd1(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300)
    0x1cf8: v1cf8 = MLOAD v1cb6(0x40)
    0x1cfc: v1cfc(0x0) = SUB v1cb9, v1cf8
    0x1cfd: v1cfd(0x64) = CONST 
    0x1cff: v1cff(0x64) = ADD v1cfd(0x64), v1cfc(0x0)
    0x1d01: REVERT v1cf8, v1cff(0x64)

    Begin block 0x1d02
    prev=[0x1ca7], succ=[0x1d24, 0x1d67]
    =================================
    0x1d03: v1d03(0x1) = CONST 
    0x1d05: v1d05(0x1) = CONST 
    0x1d07: v1d07(0xa0) = CONST 
    0x1d09: v1d09(0x10000000000000000000000000000000000000000) = SHL v1d07(0xa0), v1d05(0x1)
    0x1d0a: v1d0a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d09(0x10000000000000000000000000000000000000000), v1d03(0x1)
    0x1d0c: v1d0c = AND va16, v1d0a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d0d: v1d0d(0x0) = CONST 
    0x1d11: MSTORE v1d0d(0x0), v1d0c
    0x1d12: v1d12(0x5) = CONST 
    0x1d14: v1d14(0x20) = CONST 
    0x1d16: MSTORE v1d14(0x20), v1d12(0x5)
    0x1d17: v1d17(0x40) = CONST 
    0x1d1a: v1d1a = SHA3 v1d0d(0x0), v1d17(0x40)
    0x1d1b: v1d1b = SLOAD v1d1a
    0x1d1c: v1d1c(0xff) = CONST 
    0x1d1e: v1d1e = AND v1d1c(0xff), v1d1b
    0x1d1f: v1d1f = ISZERO v1d1e
    0x1d20: v1d20(0x1d67) = CONST 
    0x1d23: JUMPI v1d20(0x1d67), v1d1f

    Begin block 0x1d24
    prev=[0x1d02], succ=[]
    =================================
    0x1d24: v1d24(0x40) = CONST 
    0x1d27: v1d27 = MLOAD v1d24(0x40)
    0x1d28: v1d28(0x461bcd) = CONST 
    0x1d2c: v1d2c(0xe5) = CONST 
    0x1d2e: v1d2e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1d2c(0xe5), v1d28(0x461bcd)
    0x1d30: MSTORE v1d27, v1d2e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d31: v1d31(0x20) = CONST 
    0x1d33: v1d33(0x4) = CONST 
    0x1d36: v1d36 = ADD v1d27, v1d33(0x4)
    0x1d37: MSTORE v1d36, v1d31(0x20)
    0x1d38: v1d38(0x14) = CONST 
    0x1d3a: v1d3a(0x24) = CONST 
    0x1d3d: v1d3d = ADD v1d27, v1d3a(0x24)
    0x1d3e: MSTORE v1d3d, v1d38(0x14)
    0x1d3f: v1d3f(0x135a5b9d195c88185b1c9958591e481859191959) = CONST 
    0x1d54: v1d54(0x62) = CONST 
    0x1d56: v1d56(0x4d696e74657220616c7265616479206164646564000000000000000000000000) = SHL v1d54(0x62), v1d3f(0x135a5b9d195c88185b1c9958591e481859191959)
    0x1d57: v1d57(0x44) = CONST 
    0x1d5a: v1d5a = ADD v1d27, v1d57(0x44)
    0x1d5b: MSTORE v1d5a, v1d56(0x4d696e74657220616c7265616479206164646564000000000000000000000000)
    0x1d5d: v1d5d = MLOAD v1d24(0x40)
    0x1d61: v1d61(0x0) = SUB v1d27, v1d5d
    0x1d62: v1d62(0x64) = CONST 
    0x1d64: v1d64(0x64) = ADD v1d62(0x64), v1d61(0x0)
    0x1d66: REVERT v1d5d, v1d64(0x64)

    Begin block 0x1d67
    prev=[0x1d02], succ=[0x3fbc]
    =================================
    0x1d68: v1d68(0x1) = CONST 
    0x1d6a: v1d6a(0x1) = CONST 
    0x1d6c: v1d6c(0xa0) = CONST 
    0x1d6e: v1d6e(0x10000000000000000000000000000000000000000) = SHL v1d6c(0xa0), v1d6a(0x1)
    0x1d6f: v1d6f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d6e(0x10000000000000000000000000000000000000000), v1d68(0x1)
    0x1d70: v1d70 = AND v1d6f(0xffffffffffffffffffffffffffffffffffffffff), va16
    0x1d71: v1d71(0x0) = CONST 
    0x1d75: MSTORE v1d71(0x0), v1d70
    0x1d76: v1d76(0x5) = CONST 
    0x1d78: v1d78(0x20) = CONST 
    0x1d7a: MSTORE v1d78(0x20), v1d76(0x5)
    0x1d7b: v1d7b(0x40) = CONST 
    0x1d7e: v1d7e = SHA3 v1d71(0x0), v1d7b(0x40)
    0x1d80: v1d80 = SLOAD v1d7e
    0x1d81: v1d81(0xff) = CONST 
    0x1d83: v1d83(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1d81(0xff)
    0x1d84: v1d84 = AND v1d83(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1d80
    0x1d85: v1d85(0x1) = CONST 
    0x1d87: v1d87 = OR v1d85(0x1), v1d84
    0x1d89: SSTORE v1d7e, v1d87
    0x1d8a: JUMP v9f6(0x3fbc)

    Begin block 0x3fbc
    prev=[0x1d67], succ=[]
    =================================
    0x3fbd: STOP 

}

function addOperator(address)() public {
    Begin block 0xa1b
    prev=[], succ=[0xa2d, 0xa31]
    =================================
    0xa1c: va1c(0x3fdd) = CONST 
    0xa1f: va1f(0x4) = CONST 
    0xa22: va22 = CALLDATASIZE 
    0xa23: va23 = SUB va22, va1f(0x4)
    0xa24: va24(0x20) = CONST 
    0xa27: va27 = LT va23, va24(0x20)
    0xa28: va28 = ISZERO va27
    0xa29: va29(0xa31) = CONST 
    0xa2c: JUMPI va29(0xa31), va28

    Begin block 0xa2d
    prev=[0xa1b], succ=[]
    =================================
    0xa2d: va2d(0x0) = CONST 
    0xa30: REVERT va2d(0x0), va2d(0x0)

    Begin block 0xa31
    prev=[0xa1b], succ=[0x1d8b]
    =================================
    0xa33: va33 = CALLDATALOAD va1f(0x4)
    0xa34: va34(0x1) = CONST 
    0xa36: va36(0x1) = CONST 
    0xa38: va38(0xa0) = CONST 
    0xa3a: va3a(0x10000000000000000000000000000000000000000) = SHL va38(0xa0), va36(0x1)
    0xa3b: va3b(0xffffffffffffffffffffffffffffffffffffffff) = SUB va3a(0x10000000000000000000000000000000000000000), va34(0x1)
    0xa3c: va3c = AND va3b(0xffffffffffffffffffffffffffffffffffffffff), va33
    0xa3d: va3d(0x1d8b) = CONST 
    0xa40: JUMP va3d(0x1d8b)

    Begin block 0x1d8b
    prev=[0xa31], succ=[0x1d9e, 0x1dda]
    =================================
    0x1d8c: v1d8c(0x3) = CONST 
    0x1d8e: v1d8e = SLOAD v1d8c(0x3)
    0x1d8f: v1d8f(0x1) = CONST 
    0x1d91: v1d91(0x1) = CONST 
    0x1d93: v1d93(0xa0) = CONST 
    0x1d95: v1d95(0x10000000000000000000000000000000000000000) = SHL v1d93(0xa0), v1d91(0x1)
    0x1d96: v1d96(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d95(0x10000000000000000000000000000000000000000), v1d8f(0x1)
    0x1d97: v1d97 = AND v1d96(0xffffffffffffffffffffffffffffffffffffffff), v1d8e
    0x1d98: v1d98 = CALLER 
    0x1d99: v1d99 = EQ v1d98, v1d97
    0x1d9a: v1d9a(0x1dda) = CONST 
    0x1d9d: JUMPI v1d9a(0x1dda), v1d99

    Begin block 0x1d9e
    prev=[0x1d8b], succ=[]
    =================================
    0x1d9e: v1d9e(0x40) = CONST 
    0x1da1: v1da1 = MLOAD v1d9e(0x40)
    0x1da2: v1da2(0x461bcd) = CONST 
    0x1da6: v1da6(0xe5) = CONST 
    0x1da8: v1da8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1da6(0xe5), v1da2(0x461bcd)
    0x1daa: MSTORE v1da1, v1da8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1dab: v1dab(0x20) = CONST 
    0x1dad: v1dad(0x4) = CONST 
    0x1db0: v1db0 = ADD v1da1, v1dad(0x4)
    0x1db1: MSTORE v1db0, v1dab(0x20)
    0x1db2: v1db2(0xd) = CONST 
    0x1db4: v1db4(0x24) = CONST 
    0x1db7: v1db7 = ADD v1da1, v1db4(0x24)
    0x1db8: MSTORE v1db7, v1db2(0xd)
    0x1db9: v1db9(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1dc7: v1dc7(0x99) = CONST 
    0x1dc9: v1dc9(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1dc7(0x99), v1db9(0x26bab9ba1031329037bbb732b9)
    0x1dca: v1dca(0x44) = CONST 
    0x1dcd: v1dcd = ADD v1da1, v1dca(0x44)
    0x1dce: MSTORE v1dcd, v1dc9(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1dd0: v1dd0 = MLOAD v1d9e(0x40)
    0x1dd4: v1dd4(0x0) = SUB v1da1, v1dd0
    0x1dd5: v1dd5(0x64) = CONST 
    0x1dd7: v1dd7(0x64) = ADD v1dd5(0x64), v1dd4(0x0)
    0x1dd9: REVERT v1dd0, v1dd7(0x64)

    Begin block 0x1dda
    prev=[0x1d8b], succ=[0x1de9, 0x1e1f]
    =================================
    0x1ddb: v1ddb(0x1) = CONST 
    0x1ddd: v1ddd(0x1) = CONST 
    0x1ddf: v1ddf(0xa0) = CONST 
    0x1de1: v1de1(0x10000000000000000000000000000000000000000) = SHL v1ddf(0xa0), v1ddd(0x1)
    0x1de2: v1de2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1de1(0x10000000000000000000000000000000000000000), v1ddb(0x1)
    0x1de4: v1de4 = AND va3c, v1de2(0xffffffffffffffffffffffffffffffffffffffff)
    0x1de5: v1de5(0x1e1f) = CONST 
    0x1de8: JUMPI v1de5(0x1e1f), v1de4

    Begin block 0x1de9
    prev=[0x1dda], succ=[]
    =================================
    0x1de9: v1de9(0x40) = CONST 
    0x1deb: v1deb = MLOAD v1de9(0x40)
    0x1dec: v1dec(0x461bcd) = CONST 
    0x1df0: v1df0(0xe5) = CONST 
    0x1df2: v1df2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1df0(0xe5), v1dec(0x461bcd)
    0x1df4: MSTORE v1deb, v1df2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1df5: v1df5(0x4) = CONST 
    0x1df7: v1df7 = ADD v1df5(0x4), v1deb
    0x1dfa: v1dfa(0x20) = CONST 
    0x1dfc: v1dfc = ADD v1dfa(0x20), v1df7
    0x1dff: v1dff(0x20) = SUB v1dfc, v1df7
    0x1e01: MSTORE v1df7, v1dff(0x20)
    0x1e02: v1e02(0x21) = CONST 
    0x1e05: MSTORE v1dfc, v1e02(0x21)
    0x1e06: v1e06(0x20) = CONST 
    0x1e08: v1e08 = ADD v1e06(0x20), v1dfc
    0x1e0a: v1e0a(0x3b05) = CONST 
    0x1e0d: v1e0d(0x21) = CONST 
    0x1e10: CODECOPY v1e08, v1e0a(0x3b05), v1e0d(0x21)
    0x1e11: v1e11(0x40) = CONST 
    0x1e13: v1e13 = ADD v1e11(0x40), v1e08
    0x1e17: v1e17(0x40) = CONST 
    0x1e19: v1e19 = MLOAD v1e17(0x40)
    0x1e1c: v1e1c(0x84) = SUB v1e13, v1e19
    0x1e1e: REVERT v1e19, v1e1c(0x84)

    Begin block 0x1e1f
    prev=[0x1dda], succ=[0x1e41, 0x1e86]
    =================================
    0x1e20: v1e20(0x1) = CONST 
    0x1e22: v1e22(0x1) = CONST 
    0x1e24: v1e24(0xa0) = CONST 
    0x1e26: v1e26(0x10000000000000000000000000000000000000000) = SHL v1e24(0xa0), v1e22(0x1)
    0x1e27: v1e27(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e26(0x10000000000000000000000000000000000000000), v1e20(0x1)
    0x1e29: v1e29 = AND va3c, v1e27(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e2a: v1e2a(0x0) = CONST 
    0x1e2e: MSTORE v1e2a(0x0), v1e29
    0x1e2f: v1e2f(0x6) = CONST 
    0x1e31: v1e31(0x20) = CONST 
    0x1e33: MSTORE v1e31(0x20), v1e2f(0x6)
    0x1e34: v1e34(0x40) = CONST 
    0x1e37: v1e37 = SHA3 v1e2a(0x0), v1e34(0x40)
    0x1e38: v1e38 = SLOAD v1e37
    0x1e39: v1e39(0xff) = CONST 
    0x1e3b: v1e3b = AND v1e39(0xff), v1e38
    0x1e3c: v1e3c = ISZERO v1e3b
    0x1e3d: v1e3d(0x1e86) = CONST 
    0x1e40: JUMPI v1e3d(0x1e86), v1e3c

    Begin block 0x1e41
    prev=[0x1e1f], succ=[]
    =================================
    0x1e41: v1e41(0x40) = CONST 
    0x1e44: v1e44 = MLOAD v1e41(0x40)
    0x1e45: v1e45(0x461bcd) = CONST 
    0x1e49: v1e49(0xe5) = CONST 
    0x1e4b: v1e4b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e49(0xe5), v1e45(0x461bcd)
    0x1e4d: MSTORE v1e44, v1e4b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e4e: v1e4e(0x20) = CONST 
    0x1e50: v1e50(0x4) = CONST 
    0x1e53: v1e53 = ADD v1e44, v1e50(0x4)
    0x1e54: MSTORE v1e53, v1e4e(0x20)
    0x1e55: v1e55(0x16) = CONST 
    0x1e57: v1e57(0x24) = CONST 
    0x1e5a: v1e5a = ADD v1e44, v1e57(0x24)
    0x1e5b: MSTORE v1e5a, v1e55(0x16)
    0x1e5c: v1e5c(0x13dc195c985d1bdc88185b1c9958591e481859191959) = CONST 
    0x1e73: v1e73(0x52) = CONST 
    0x1e75: v1e75(0x4f70657261746f7220616c726561647920616464656400000000000000000000) = SHL v1e73(0x52), v1e5c(0x13dc195c985d1bdc88185b1c9958591e481859191959)
    0x1e76: v1e76(0x44) = CONST 
    0x1e79: v1e79 = ADD v1e44, v1e76(0x44)
    0x1e7a: MSTORE v1e79, v1e75(0x4f70657261746f7220616c726561647920616464656400000000000000000000)
    0x1e7c: v1e7c = MLOAD v1e41(0x40)
    0x1e80: v1e80(0x0) = SUB v1e44, v1e7c
    0x1e81: v1e81(0x64) = CONST 
    0x1e83: v1e83(0x64) = ADD v1e81(0x64), v1e80(0x0)
    0x1e85: REVERT v1e7c, v1e83(0x64)

    Begin block 0x1e86
    prev=[0x1e1f], succ=[0x3fdd]
    =================================
    0x1e87: v1e87(0x1) = CONST 
    0x1e89: v1e89(0x1) = CONST 
    0x1e8b: v1e8b(0xa0) = CONST 
    0x1e8d: v1e8d(0x10000000000000000000000000000000000000000) = SHL v1e8b(0xa0), v1e89(0x1)
    0x1e8e: v1e8e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e8d(0x10000000000000000000000000000000000000000), v1e87(0x1)
    0x1e8f: v1e8f = AND v1e8e(0xffffffffffffffffffffffffffffffffffffffff), va3c
    0x1e90: v1e90(0x0) = CONST 
    0x1e94: MSTORE v1e90(0x0), v1e8f
    0x1e95: v1e95(0x6) = CONST 
    0x1e97: v1e97(0x20) = CONST 
    0x1e99: MSTORE v1e97(0x20), v1e95(0x6)
    0x1e9a: v1e9a(0x40) = CONST 
    0x1e9d: v1e9d = SHA3 v1e90(0x0), v1e9a(0x40)
    0x1e9f: v1e9f = SLOAD v1e9d
    0x1ea0: v1ea0(0xff) = CONST 
    0x1ea2: v1ea2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1ea0(0xff)
    0x1ea3: v1ea3 = AND v1ea2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1e9f
    0x1ea4: v1ea4(0x1) = CONST 
    0x1ea6: v1ea6 = OR v1ea4(0x1), v1ea3
    0x1ea8: SSTORE v1e9d, v1ea6
    0x1ea9: JUMP va1c(0x3fdd)

    Begin block 0x3fdd
    prev=[0x1e86], succ=[]
    =================================
    0x3fde: STOP 

}

function burn(address,uint256)() public {
    Begin block 0xa41
    prev=[], succ=[0xa53, 0xa57]
    =================================
    0xa42: va42(0x3ffe) = CONST 
    0xa45: va45(0x4) = CONST 
    0xa48: va48 = CALLDATASIZE 
    0xa49: va49 = SUB va48, va45(0x4)
    0xa4a: va4a(0x40) = CONST 
    0xa4d: va4d = LT va49, va4a(0x40)
    0xa4e: va4e = ISZERO va4d
    0xa4f: va4f(0xa57) = CONST 
    0xa52: JUMPI va4f(0xa57), va4e

    Begin block 0xa53
    prev=[0xa41], succ=[]
    =================================
    0xa53: va53(0x0) = CONST 
    0xa56: REVERT va53(0x0), va53(0x0)

    Begin block 0xa57
    prev=[0xa41], succ=[0x1eaa]
    =================================
    0xa59: va59(0x1) = CONST 
    0xa5b: va5b(0x1) = CONST 
    0xa5d: va5d(0xa0) = CONST 
    0xa5f: va5f(0x10000000000000000000000000000000000000000) = SHL va5d(0xa0), va5b(0x1)
    0xa60: va60(0xffffffffffffffffffffffffffffffffffffffff) = SUB va5f(0x10000000000000000000000000000000000000000), va59(0x1)
    0xa62: va62 = CALLDATALOAD va45(0x4)
    0xa63: va63 = AND va62, va60(0xffffffffffffffffffffffffffffffffffffffff)
    0xa65: va65(0x20) = CONST 
    0xa67: va67(0x24) = ADD va65(0x20), va45(0x4)
    0xa68: va68 = CALLDATALOAD va67(0x24)
    0xa69: va69(0x1eaa) = CONST 
    0xa6c: JUMP va69(0x1eaa)

    Begin block 0x1eaa
    prev=[0xa57], succ=[0x1ec2, 0x1eff]
    =================================
    0x1eab: v1eab = CALLER 
    0x1eac: v1eac(0x0) = CONST 
    0x1eb0: MSTORE v1eac(0x0), v1eab
    0x1eb1: v1eb1(0x5) = CONST 
    0x1eb3: v1eb3(0x20) = CONST 
    0x1eb5: MSTORE v1eb3(0x20), v1eb1(0x5)
    0x1eb6: v1eb6(0x40) = CONST 
    0x1eb9: v1eb9 = SHA3 v1eac(0x0), v1eb6(0x40)
    0x1eba: v1eba = SLOAD v1eb9
    0x1ebb: v1ebb(0xff) = CONST 
    0x1ebd: v1ebd = AND v1ebb(0xff), v1eba
    0x1ebe: v1ebe(0x1eff) = CONST 
    0x1ec1: JUMPI v1ebe(0x1eff), v1ebd

    Begin block 0x1ec2
    prev=[0x1eaa], succ=[]
    =================================
    0x1ec2: v1ec2(0x40) = CONST 
    0x1ec5: v1ec5 = MLOAD v1ec2(0x40)
    0x1ec6: v1ec6(0x461bcd) = CONST 
    0x1eca: v1eca(0xe5) = CONST 
    0x1ecc: v1ecc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1eca(0xe5), v1ec6(0x461bcd)
    0x1ece: MSTORE v1ec5, v1ecc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ecf: v1ecf(0x20) = CONST 
    0x1ed1: v1ed1(0x4) = CONST 
    0x1ed4: v1ed4 = ADD v1ec5, v1ed1(0x4)
    0x1ed5: MSTORE v1ed4, v1ecf(0x20)
    0x1ed6: v1ed6(0xe) = CONST 
    0x1ed8: v1ed8(0x24) = CONST 
    0x1edb: v1edb = ADD v1ec5, v1ed8(0x24)
    0x1edc: MSTORE v1edb, v1ed6(0xe)
    0x1edd: v1edd(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x1eec: v1eec(0x91) = CONST 
    0x1eee: v1eee(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v1eec(0x91), v1edd(0x36bab9ba1031329036b4b73a32b9)
    0x1eef: v1eef(0x44) = CONST 
    0x1ef2: v1ef2 = ADD v1ec5, v1eef(0x44)
    0x1ef3: MSTORE v1ef2, v1eee(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x1ef5: v1ef5 = MLOAD v1ec2(0x40)
    0x1ef9: v1ef9(0x0) = SUB v1ec5, v1ef5
    0x1efa: v1efa(0x64) = CONST 
    0x1efc: v1efc(0x64) = ADD v1efa(0x64), v1ef9(0x0)
    0x1efe: REVERT v1ef5, v1efc(0x64)

    Begin block 0x1eff
    prev=[0x1eaa], succ=[0x1f09]
    =================================
    0x1f00: v1f00(0x1f09) = CONST 
    0x1f05: v1f05(0x2497) = CONST 
    0x1f08: v1f08_0 = CALLPRIVATE v1f05(0x2497), va68, va63, v1f00(0x1f09)

    Begin block 0x1f09
    prev=[0x1eff], succ=[0x1f0e, 0x1f4a]
    =================================
    0x1f0a: v1f0a(0x1f4a) = CONST 
    0x1f0d: JUMPI v1f0a(0x1f4a), v1f08_0

    Begin block 0x1f0e
    prev=[0x1f09], succ=[]
    =================================
    0x1f0e: v1f0e(0x40) = CONST 
    0x1f11: v1f11 = MLOAD v1f0e(0x40)
    0x1f12: v1f12(0x461bcd) = CONST 
    0x1f16: v1f16(0xe5) = CONST 
    0x1f18: v1f18(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f16(0xe5), v1f12(0x461bcd)
    0x1f1a: MSTORE v1f11, v1f18(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f1b: v1f1b(0x20) = CONST 
    0x1f1d: v1f1d(0x4) = CONST 
    0x1f20: v1f20 = ADD v1f11, v1f1d(0x4)
    0x1f21: MSTORE v1f20, v1f1b(0x20)
    0x1f22: v1f22(0xd) = CONST 
    0x1f24: v1f24(0x24) = CONST 
    0x1f27: v1f27 = ADD v1f11, v1f24(0x24)
    0x1f28: MSTORE v1f27, v1f22(0xd)
    0x1f29: v1f29(0x2737ba103a34329037bbb732b9) = CONST 
    0x1f37: v1f37(0x99) = CONST 
    0x1f39: v1f39(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v1f37(0x99), v1f29(0x2737ba103a34329037bbb732b9)
    0x1f3a: v1f3a(0x44) = CONST 
    0x1f3d: v1f3d = ADD v1f11, v1f3a(0x44)
    0x1f3e: MSTORE v1f3d, v1f39(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1f40: v1f40 = MLOAD v1f0e(0x40)
    0x1f44: v1f44(0x0) = SUB v1f11, v1f40
    0x1f45: v1f45(0x64) = CONST 
    0x1f47: v1f47(0x64) = ADD v1f45(0x64), v1f44(0x0)
    0x1f49: REVERT v1f40, v1f47(0x64)

    Begin block 0x1f4a
    prev=[0x1f09], succ=[0x3059]
    =================================
    0x1f4b: v1f4b(0x4394) = CONST 
    0x1f50: v1f50(0x3059) = CONST 
    0x1f53: JUMP v1f50(0x3059)

    Begin block 0x3059
    prev=[0x1f4a], succ=[0x389fB0x3059]
    =================================
    0x305a: v305a(0x0) = CONST 
    0x305e: MSTORE v305a(0x0), va68
    0x305f: v305f(0x8) = CONST 
    0x3061: v3061(0x20) = CONST 
    0x3065: MSTORE v3061(0x20), v305f(0x8)
    0x3066: v3066(0x40) = CONST 
    0x306a: v306a = SHA3 v305a(0x0), v3066(0x40)
    0x306c: v306c = SLOAD v306a
    0x306d: v306d(0x1) = CONST 
    0x306f: v306f(0x1) = CONST 
    0x3071: v3071(0xa0) = CONST 
    0x3073: v3073(0x10000000000000000000000000000000000000000) = SHL v3071(0xa0), v306f(0x1)
    0x3074: v3074(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3073(0x10000000000000000000000000000000000000000), v306d(0x1)
    0x3075: v3075(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3074(0xffffffffffffffffffffffffffffffffffffffff)
    0x3078: v3078 = AND v3075(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v306c
    0x307b: SSTORE v306a, v3078
    0x307c: v307c(0xb) = CONST 
    0x307f: MSTORE v3061(0x20), v307c(0xb)
    0x3082: v3082 = SHA3 v305a(0x0), v3066(0x40)
    0x3084: v3084 = SLOAD v3082
    0x3087: v3087 = AND v3075(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3084
    0x3089: SSTORE v3082, v3087
    0x308a: v308a(0x1) = CONST 
    0x308d: v308d = ADD v3082, v308a(0x1)
    0x3090: SSTORE v308d, v305a(0x0)
    0x3091: v3091(0x2) = CONST 
    0x3093: v3093 = ADD v3091(0x2), v3082
    0x3096: SSTORE v3093, v305a(0x0)
    0x3097: v3097(0xc) = CONST 
    0x309b: MSTORE v3061(0x20), v3097(0xc)
    0x309d: v309d = SHA3 v305a(0x0), v3066(0x40)
    0x309f: v309f(0x30a8) = CONST 
    0x30a4: v30a4(0x389f) = CONST 
    0x30a7: JUMP v30a4(0x389f), v305a(0x0), v309d, v309f(0x30a8)

    Begin block 0x389fB0x3059
    prev=[0x3059], succ=[0x394eB0x389fB0x3059]
    =================================
    0x38a2S0x3059: v38a2V3059 = SLOAD v309d
    0x38a3S0x3059: v38a3V3059(0x0) = CONST 
    0x38a6S0x3059: SSTORE v309d, v38a3V3059(0x0)
    0x38a8S0x3059: v38a8V3059(0x0) = CONST 
    0x38aaS0x3059: MSTORE v38a8V3059(0x0), v309d
    0x38abS0x3059: v38abV3059(0x20) = CONST 
    0x38adS0x3059: v38adV3059(0x0) = CONST 
    0x38afS0x3059: v38afV3059 = SHA3 v38adV3059(0x0), v38abV3059(0x20)
    0x38b2S0x3059: v38b2V3059 = ADD v38afV3059, v38a2V3059
    0x38b4S0x3059: v38b4V3059(0x38bd) = CONST 
    0x38b9S0x3059: v38b9V3059(0x394e) = CONST 
    0x38bcS0x3059: JUMP v38b9V3059(0x394e)

    Begin block 0x394eB0x389fB0x3059
    prev=[0x389fB0x3059], succ=[0x394fB0x389fB0x3059]
    =================================

    Begin block 0x394fB0x389fB0x3059
    prev=[0x3958B0x389fB0x3059, 0x394eB0x389fB0x3059], succ=[0x3958B0x389fB0x3059, 0x459cB0x389fB0x3059]
    =================================
    0x394f_0x0S0x389fS0x3059: v394f_0V389fV3059 = PHI v38afV3059, v395eV389fV3059
    0x3952S0x389fS0x3059: v3952V389fV3059 = GT v38b2V3059, v394f_0V389fV3059
    0x3953S0x389fS0x3059: v3953V389fV3059 = ISZERO v3952V389fV3059
    0x3954S0x389fS0x3059: v3954V389fV3059(0x459c) = CONST 
    0x3957S0x389fS0x3059: JUMPI v3954V389fV3059(0x459c), v3953V389fV3059

    Begin block 0x3958B0x389fB0x3059
    prev=[0x394fB0x389fB0x3059], succ=[0x394fB0x389fB0x3059]
    =================================
    0x3958S0x389fS0x3059: v3958V389fV3059(0x0) = CONST 
    0x3958_0x0S0x389fS0x3059: v3958_0V389fV3059 = PHI v38afV3059, v395eV389fV3059
    0x395bS0x389fS0x3059: SSTORE v3958_0V389fV3059, v3958V389fV3059(0x0)
    0x395cS0x389fS0x3059: v395cV389fV3059(0x1) = CONST 
    0x395eS0x389fS0x3059: v395eV389fV3059 = ADD v395cV389fV3059(0x1), v3958_0V389fV3059
    0x395fS0x389fS0x3059: v395fV389fV3059(0x394f) = CONST 
    0x3962S0x389fS0x3059: JUMP v395fV389fV3059(0x394f)

    Begin block 0x459cB0x389fB0x3059
    prev=[0x394fB0x389fB0x3059], succ=[0x38bdB0x3059]
    =================================
    0x459fS0x389fS0x3059: JUMP v38b4V3059(0x38bd)

    Begin block 0x38bdB0x3059
    prev=[0x459cB0x389fB0x3059], succ=[0x30a8]
    =================================
    0x38bfS0x3059: JUMP v309f(0x30a8)

    Begin block 0x30a8
    prev=[0x38bdB0x3059], succ=[0x389fB0x30a8]
    =================================
    0x30a9: v30a9(0x30b6) = CONST 
    0x30ac: v30ac(0x1) = CONST 
    0x30af: v30af = ADD v309d, v30ac(0x1)
    0x30b0: v30b0(0x0) = CONST 
    0x30b2: v30b2(0x389f) = CONST 
    0x30b5: JUMP v30b2(0x389f), v30b0(0x0), v30af, v30a9(0x30b6)

    Begin block 0x389fB0x30a8
    prev=[0x30a8], succ=[0x394eB0x389fB0x30a8]
    =================================
    0x38a2S0x30a8: v38a2V30a8 = SLOAD v30af
    0x38a3S0x30a8: v38a3V30a8(0x0) = CONST 
    0x38a6S0x30a8: SSTORE v30af, v38a3V30a8(0x0)
    0x38a8S0x30a8: v38a8V30a8(0x0) = CONST 
    0x38aaS0x30a8: MSTORE v38a8V30a8(0x0), v30af
    0x38abS0x30a8: v38abV30a8(0x20) = CONST 
    0x38adS0x30a8: v38adV30a8(0x0) = CONST 
    0x38afS0x30a8: v38afV30a8 = SHA3 v38adV30a8(0x0), v38abV30a8(0x20)
    0x38b2S0x30a8: v38b2V30a8 = ADD v38afV30a8, v38a2V30a8
    0x38b4S0x30a8: v38b4V30a8(0x38bd) = CONST 
    0x38b9S0x30a8: v38b9V30a8(0x394e) = CONST 
    0x38bcS0x30a8: JUMP v38b9V30a8(0x394e)

    Begin block 0x394eB0x389fB0x30a8
    prev=[0x389fB0x30a8], succ=[0x394fB0x389fB0x30a8]
    =================================

    Begin block 0x394fB0x389fB0x30a8
    prev=[0x3958B0x389fB0x30a8, 0x394eB0x389fB0x30a8], succ=[0x3958B0x389fB0x30a8, 0x459cB0x389fB0x30a8]
    =================================
    0x394f_0x0S0x389fS0x30a8: v394f_0V389fV30a8 = PHI v38afV30a8, v395eV389fV30a8
    0x3952S0x389fS0x30a8: v3952V389fV30a8 = GT v38b2V30a8, v394f_0V389fV30a8
    0x3953S0x389fS0x30a8: v3953V389fV30a8 = ISZERO v3952V389fV30a8
    0x3954S0x389fS0x30a8: v3954V389fV30a8(0x459c) = CONST 
    0x3957S0x389fS0x30a8: JUMPI v3954V389fV30a8(0x459c), v3953V389fV30a8

    Begin block 0x3958B0x389fB0x30a8
    prev=[0x394fB0x389fB0x30a8], succ=[0x394fB0x389fB0x30a8]
    =================================
    0x3958S0x389fS0x30a8: v3958V389fV30a8(0x0) = CONST 
    0x3958_0x0S0x389fS0x30a8: v3958_0V389fV30a8 = PHI v38afV30a8, v395eV389fV30a8
    0x395bS0x389fS0x30a8: SSTORE v3958_0V389fV30a8, v3958V389fV30a8(0x0)
    0x395cS0x389fS0x30a8: v395cV389fV30a8(0x1) = CONST 
    0x395eS0x389fS0x30a8: v395eV389fV30a8 = ADD v395cV389fV30a8(0x1), v3958_0V389fV30a8
    0x395fS0x389fS0x30a8: v395fV389fV30a8(0x394f) = CONST 
    0x3962S0x389fS0x30a8: JUMP v395fV389fV30a8(0x394f)

    Begin block 0x459cB0x389fB0x30a8
    prev=[0x394fB0x389fB0x30a8], succ=[0x38bdB0x30a8]
    =================================
    0x459fS0x389fS0x30a8: JUMP v38b4V30a8(0x38bd)

    Begin block 0x38bdB0x30a8
    prev=[0x459cB0x389fB0x30a8], succ=[0x30b6]
    =================================
    0x38bfS0x30a8: JUMP v30a9(0x30b6)

    Begin block 0x30b6
    prev=[0x38bdB0x30a8], succ=[0x4394]
    =================================
    0x30b8: v30b8(0x0) = CONST 
    0x30ba: v30ba(0x2) = CONST 
    0x30bf: v30bf = ADD v30ba(0x2), v309d
    0x30c2: SSTORE v30bf, v30b8(0x0)
    0x30c5: MSTORE v30b8(0x0), va68
    0x30c6: v30c6(0xa) = CONST 
    0x30c8: v30c8(0x20) = CONST 
    0x30cc: MSTORE v30c8(0x20), v30c6(0xa)
    0x30cd: v30cd(0x40) = CONST 
    0x30d1: v30d1 = SHA3 v30b8(0x0), v30cd(0x40)
    0x30d4: SSTORE v30d1, v30b8(0x0)
    0x30d5: v30d5(0x1) = CONST 
    0x30d9: v30d9 = ADD v30d5(0x1), v30d1
    0x30db: v30db = SLOAD v30d9
    0x30dc: v30dc(0x1) = CONST 
    0x30de: v30de(0x1) = CONST 
    0x30e0: v30e0(0xa0) = CONST 
    0x30e2: v30e2(0x10000000000000000000000000000000000000000) = SHL v30e0(0xa0), v30de(0x1)
    0x30e3: v30e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30e2(0x10000000000000000000000000000000000000000), v30dc(0x1)
    0x30e4: v30e4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v30e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x30e5: v30e5 = AND v30e4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v30db
    0x30e7: SSTORE v30d9, v30e5
    0x30e9: v30e9 = MLOAD v30cd(0x40)
    0x30ec: MSTORE v30e9, va68
    0x30ef: v30ef = ADD v30e9, v30c8(0x20)
    0x30f0: MSTORE v30ef, v30d5(0x1)
    0x30f2: v30f2 = MLOAD v30cd(0x40)
    0x30f3: v30f3(0x1) = CONST 
    0x30f5: v30f5(0x1) = CONST 
    0x30f7: v30f7(0xa0) = CONST 
    0x30f9: v30f9(0x10000000000000000000000000000000000000000) = SHL v30f7(0xa0), v30f5(0x1)
    0x30fa: v30fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30f9(0x10000000000000000000000000000000000000000), v30f3(0x1)
    0x30fc: v30fc = AND va63, v30fa(0xffffffffffffffffffffffffffffffffffffffff)
    0x30fe: v30fe = CALLER 
    0x3100: v3100(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x3125: v3125(0x0) = SUB v30e9, v30f2
    0x3126: v3126(0x40) = ADD v3125(0x0), v30cd(0x40)
    0x3128: LOG4 v30f2, v3126(0x40), v3100(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v30fe, v30fc, v30b8(0x0)
    0x312b: JUMP v1f4b(0x4394)

    Begin block 0x4394
    prev=[0x30b6], succ=[0x3ffe]
    =================================
    0x4397: JUMP va42(0x3ffe)

    Begin block 0x3ffe
    prev=[0x4394], succ=[]
    =================================
    0x3fff: STOP 

}

function setApprovalForAll(address,bool)() public {
    Begin block 0xa6d
    prev=[], succ=[0xa7f, 0xa83]
    =================================
    0xa6e: va6e(0x401f) = CONST 
    0xa71: va71(0x4) = CONST 
    0xa74: va74 = CALLDATASIZE 
    0xa75: va75 = SUB va74, va71(0x4)
    0xa76: va76(0x40) = CONST 
    0xa79: va79 = LT va75, va76(0x40)
    0xa7a: va7a = ISZERO va79
    0xa7b: va7b(0xa83) = CONST 
    0xa7e: JUMPI va7b(0xa83), va7a

    Begin block 0xa7f
    prev=[0xa6d], succ=[]
    =================================
    0xa7f: va7f(0x0) = CONST 
    0xa82: REVERT va7f(0x0), va7f(0x0)

    Begin block 0xa83
    prev=[0xa6d], succ=[0x1f54]
    =================================
    0xa85: va85(0x1) = CONST 
    0xa87: va87(0x1) = CONST 
    0xa89: va89(0xa0) = CONST 
    0xa8b: va8b(0x10000000000000000000000000000000000000000) = SHL va89(0xa0), va87(0x1)
    0xa8c: va8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB va8b(0x10000000000000000000000000000000000000000), va85(0x1)
    0xa8e: va8e = CALLDATALOAD va71(0x4)
    0xa8f: va8f = AND va8e, va8c(0xffffffffffffffffffffffffffffffffffffffff)
    0xa91: va91(0x20) = CONST 
    0xa93: va93(0x24) = ADD va91(0x20), va71(0x4)
    0xa94: va94 = CALLDATALOAD va93(0x24)
    0xa95: va95 = ISZERO va94
    0xa96: va96 = ISZERO va95
    0xa97: va97(0x1f54) = CONST 
    0xa9a: JUMP va97(0x1f54)

    Begin block 0x1f54
    prev=[0xa83], succ=[0x1f66, 0x1fb2]
    =================================
    0x1f55: v1f55 = CALLER 
    0x1f56: v1f56(0x1) = CONST 
    0x1f58: v1f58(0x1) = CONST 
    0x1f5a: v1f5a(0xa0) = CONST 
    0x1f5c: v1f5c(0x10000000000000000000000000000000000000000) = SHL v1f5a(0xa0), v1f58(0x1)
    0x1f5d: v1f5d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f5c(0x10000000000000000000000000000000000000000), v1f56(0x1)
    0x1f5f: v1f5f = AND va8f, v1f5d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f60: v1f60 = EQ v1f5f, v1f55
    0x1f61: v1f61 = ISZERO v1f60
    0x1f62: v1f62(0x1fb2) = CONST 
    0x1f65: JUMPI v1f62(0x1fb2), v1f61

    Begin block 0x1f66
    prev=[0x1f54], succ=[]
    =================================
    0x1f66: v1f66(0x40) = CONST 
    0x1f69: v1f69 = MLOAD v1f66(0x40)
    0x1f6a: v1f6a(0x461bcd) = CONST 
    0x1f6e: v1f6e(0xe5) = CONST 
    0x1f70: v1f70(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f6e(0xe5), v1f6a(0x461bcd)
    0x1f72: MSTORE v1f69, v1f70(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f73: v1f73(0x20) = CONST 
    0x1f75: v1f75(0x4) = CONST 
    0x1f78: v1f78 = ADD v1f69, v1f75(0x4)
    0x1f7b: MSTORE v1f78, v1f73(0x20)
    0x1f7c: v1f7c(0x24) = CONST 
    0x1f7f: v1f7f = ADD v1f69, v1f7c(0x24)
    0x1f80: MSTORE v1f7f, v1f73(0x20)
    0x1f81: v1f81(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66) = CONST 
    0x1fa2: v1fa2(0x44) = CONST 
    0x1fa5: v1fa5 = ADD v1f69, v1fa2(0x44)
    0x1fa6: MSTORE v1fa5, v1f81(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66)
    0x1fa8: v1fa8 = MLOAD v1f66(0x40)
    0x1fac: v1fac(0x0) = SUB v1f69, v1fa8
    0x1fad: v1fad(0x64) = CONST 
    0x1faf: v1faf(0x64) = ADD v1fad(0x64), v1fac(0x0)
    0x1fb1: REVERT v1fa8, v1faf(0x64)

    Begin block 0x1fb2
    prev=[0x1f54], succ=[0x401f]
    =================================
    0x1fb3: v1fb3 = CALLER 
    0x1fb4: v1fb4(0x0) = CONST 
    0x1fb8: MSTORE v1fb4(0x0), v1fb3
    0x1fb9: v1fb9(0x9) = CONST 
    0x1fbb: v1fbb(0x20) = CONST 
    0x1fbf: MSTORE v1fbb(0x20), v1fb9(0x9)
    0x1fc0: v1fc0(0x40) = CONST 
    0x1fc4: v1fc4 = SHA3 v1fb4(0x0), v1fc0(0x40)
    0x1fc5: v1fc5(0x1) = CONST 
    0x1fc7: v1fc7(0x1) = CONST 
    0x1fc9: v1fc9(0xa0) = CONST 
    0x1fcb: v1fcb(0x10000000000000000000000000000000000000000) = SHL v1fc9(0xa0), v1fc7(0x1)
    0x1fcc: v1fcc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fcb(0x10000000000000000000000000000000000000000), v1fc5(0x1)
    0x1fce: v1fce = AND va8f, v1fcc(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fd1: MSTORE v1fb4(0x0), v1fce
    0x1fd4: MSTORE v1fbb(0x20), v1fc4
    0x1fd8: v1fd8 = SHA3 v1fb4(0x0), v1fc0(0x40)
    0x1fda: v1fda = SLOAD v1fd8
    0x1fdb: v1fdb(0xff) = CONST 
    0x1fdd: v1fdd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1fdb(0xff)
    0x1fde: v1fde = AND v1fdd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1fda
    0x1fe0: v1fe0 = ISZERO va96
    0x1fe1: v1fe1 = ISZERO v1fe0
    0x1fe4: v1fe4 = OR v1fe1, v1fde
    0x1fe7: SSTORE v1fd8, v1fe4
    0x1fe9: v1fe9 = MLOAD v1fc0(0x40)
    0x1fec: MSTORE v1fe9, v1fe1
    0x1fee: v1fee = MLOAD v1fc0(0x40)
    0x1ff2: v1ff2(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31) = CONST 
    0x2017: v2017(0x0) = SUB v1fe9, v1fee
    0x201a: v201a(0x20) = ADD v1fbb(0x20), v2017(0x0)
    0x201c: LOG3 v1fee, v201a(0x20), v1ff2(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31), v1fb3, v1fce
    0x201f: JUMP va6e(0x401f)

    Begin block 0x401f
    prev=[0x1fb2], succ=[]
    =================================
    0x4020: STOP 

}

function mintSuper(address,uint256,uint256,address[],uint256[])() public {
    Begin block 0xa9b
    prev=[], succ=[0xaad, 0xab1]
    =================================
    0xa9c: va9c(0x4040) = CONST 
    0xa9f: va9f(0x4) = CONST 
    0xaa2: vaa2 = CALLDATASIZE 
    0xaa3: vaa3 = SUB vaa2, va9f(0x4)
    0xaa4: vaa4(0xa0) = CONST 
    0xaa7: vaa7 = LT vaa3, vaa4(0xa0)
    0xaa8: vaa8 = ISZERO vaa7
    0xaa9: vaa9(0xab1) = CONST 
    0xaac: JUMPI vaa9(0xab1), vaa8

    Begin block 0xaad
    prev=[0xa9b], succ=[]
    =================================
    0xaad: vaad(0x0) = CONST 
    0xab0: REVERT vaad(0x0), vaad(0x0)

    Begin block 0xab1
    prev=[0xa9b], succ=[0xae3, 0xae7]
    =================================
    0xab2: vab2(0x1) = CONST 
    0xab4: vab4(0x1) = CONST 
    0xab6: vab6(0xa0) = CONST 
    0xab8: vab8(0x10000000000000000000000000000000000000000) = SHL vab6(0xa0), vab4(0x1)
    0xab9: vab9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vab8(0x10000000000000000000000000000000000000000), vab2(0x1)
    0xabb: vabb = CALLDATALOAD va9f(0x4)
    0xabc: vabc = AND vabb, vab9(0xffffffffffffffffffffffffffffffffffffffff)
    0xabe: vabe(0x20) = CONST 
    0xac1: vac1(0x24) = ADD va9f(0x4), vabe(0x20)
    0xac2: vac2 = CALLDATALOAD vac1(0x24)
    0xac4: vac4(0x40) = CONST 
    0xac7: vac7(0x44) = ADD va9f(0x4), vac4(0x40)
    0xac8: vac8 = CALLDATALOAD vac7(0x44)
    0xacc: vacc = ADD va9f(0x4), vaa3
    0xace: vace(0x80) = CONST 
    0xad1: vad1(0x84) = ADD va9f(0x4), vace(0x80)
    0xad2: vad2(0x60) = CONST 
    0xad5: vad5(0x64) = ADD va9f(0x4), vad2(0x60)
    0xad6: vad6 = CALLDATALOAD vad5(0x64)
    0xad7: vad7(0x1) = CONST 
    0xad9: vad9(0x20) = CONST 
    0xadb: vadb(0x100000000) = SHL vad9(0x20), vad7(0x1)
    0xadd: vadd = GT vad6, vadb(0x100000000)
    0xade: vade = ISZERO vadd
    0xadf: vadf(0xae7) = CONST 
    0xae2: JUMPI vadf(0xae7), vade

    Begin block 0xae3
    prev=[0xab1], succ=[]
    =================================
    0xae3: vae3(0x0) = CONST 
    0xae6: REVERT vae3(0x0), vae3(0x0)

    Begin block 0xae7
    prev=[0xab1], succ=[0xaf5, 0xaf9]
    =================================
    0xae9: vae9 = ADD va9f(0x4), vad6
    0xaeb: vaeb(0x20) = CONST 
    0xaee: vaee = ADD vae9, vaeb(0x20)
    0xaef: vaef = GT vaee, vacc
    0xaf0: vaf0 = ISZERO vaef
    0xaf1: vaf1(0xaf9) = CONST 
    0xaf4: JUMPI vaf1(0xaf9), vaf0

    Begin block 0xaf5
    prev=[0xae7], succ=[]
    =================================
    0xaf5: vaf5(0x0) = CONST 
    0xaf8: REVERT vaf5(0x0), vaf5(0x0)

    Begin block 0xaf9
    prev=[0xae7], succ=[0xb16, 0xb1a]
    =================================
    0xafb: vafb = CALLDATALOAD vae9
    0xafd: vafd(0x20) = CONST 
    0xaff: vaff = ADD vafd(0x20), vae9
    0xb02: vb02(0x20) = CONST 
    0xb05: vb05 = MUL vafb, vb02(0x20)
    0xb07: vb07 = ADD vaff, vb05
    0xb08: vb08 = GT vb07, vacc
    0xb09: vb09(0x1) = CONST 
    0xb0b: vb0b(0x20) = CONST 
    0xb0d: vb0d(0x100000000) = SHL vb0b(0x20), vb09(0x1)
    0xb0f: vb0f = GT vafb, vb0d(0x100000000)
    0xb10: vb10 = OR vb0f, vb08
    0xb11: vb11 = ISZERO vb10
    0xb12: vb12(0xb1a) = CONST 
    0xb15: JUMPI vb12(0xb1a), vb11

    Begin block 0xb16
    prev=[0xaf9], succ=[]
    =================================
    0xb16: vb16(0x0) = CONST 
    0xb19: REVERT vb16(0x0), vb16(0x0)

    Begin block 0xb1a
    prev=[0xaf9], succ=[0xb33, 0xb37]
    =================================
    0xb21: vb21(0x20) = CONST 
    0xb24: vb24(0xa4) = ADD vad1(0x84), vb21(0x20)
    0xb26: vb26 = CALLDATALOAD vad1(0x84)
    0xb27: vb27(0x1) = CONST 
    0xb29: vb29(0x20) = CONST 
    0xb2b: vb2b(0x100000000) = SHL vb29(0x20), vb27(0x1)
    0xb2d: vb2d = GT vb26, vb2b(0x100000000)
    0xb2e: vb2e = ISZERO vb2d
    0xb2f: vb2f(0xb37) = CONST 
    0xb32: JUMPI vb2f(0xb37), vb2e

    Begin block 0xb33
    prev=[0xb1a], succ=[]
    =================================
    0xb33: vb33(0x0) = CONST 
    0xb36: REVERT vb33(0x0), vb33(0x0)

    Begin block 0xb37
    prev=[0xb1a], succ=[0xb45, 0xb49]
    =================================
    0xb39: vb39 = ADD va9f(0x4), vb26
    0xb3b: vb3b(0x20) = CONST 
    0xb3e: vb3e = ADD vb39, vb3b(0x20)
    0xb3f: vb3f = GT vb3e, vacc
    0xb40: vb40 = ISZERO vb3f
    0xb41: vb41(0xb49) = CONST 
    0xb44: JUMPI vb41(0xb49), vb40

    Begin block 0xb45
    prev=[0xb37], succ=[]
    =================================
    0xb45: vb45(0x0) = CONST 
    0xb48: REVERT vb45(0x0), vb45(0x0)

    Begin block 0xb49
    prev=[0xb37], succ=[0xb66, 0xb6a]
    =================================
    0xb4b: vb4b = CALLDATALOAD vb39
    0xb4d: vb4d(0x20) = CONST 
    0xb4f: vb4f = ADD vb4d(0x20), vb39
    0xb52: vb52(0x20) = CONST 
    0xb55: vb55 = MUL vb4b, vb52(0x20)
    0xb57: vb57 = ADD vb4f, vb55
    0xb58: vb58 = GT vb57, vacc
    0xb59: vb59(0x1) = CONST 
    0xb5b: vb5b(0x20) = CONST 
    0xb5d: vb5d(0x100000000) = SHL vb5b(0x20), vb59(0x1)
    0xb5f: vb5f = GT vb4b, vb5d(0x100000000)
    0xb60: vb60 = OR vb5f, vb58
    0xb61: vb61 = ISZERO vb60
    0xb62: vb62(0xb6a) = CONST 
    0xb65: JUMPI vb62(0xb6a), vb61

    Begin block 0xb66
    prev=[0xb49], succ=[]
    =================================
    0xb66: vb66(0x0) = CONST 
    0xb69: REVERT vb66(0x0), vb66(0x0)

    Begin block 0xb6a
    prev=[0xb49], succ=[0x2020]
    =================================
    0xb71: vb71(0x2020) = CONST 
    0xb74: JUMP vb71(0x2020)

    Begin block 0x2020
    prev=[0xb6a], succ=[0x2038, 0x2075]
    =================================
    0x2021: v2021 = CALLER 
    0x2022: v2022(0x0) = CONST 
    0x2026: MSTORE v2022(0x0), v2021
    0x2027: v2027(0x5) = CONST 
    0x2029: v2029(0x20) = CONST 
    0x202b: MSTORE v2029(0x20), v2027(0x5)
    0x202c: v202c(0x40) = CONST 
    0x202f: v202f = SHA3 v2022(0x0), v202c(0x40)
    0x2030: v2030 = SLOAD v202f
    0x2031: v2031(0xff) = CONST 
    0x2033: v2033 = AND v2031(0xff), v2030
    0x2034: v2034(0x2075) = CONST 
    0x2037: JUMPI v2034(0x2075), v2033

    Begin block 0x2038
    prev=[0x2020], succ=[]
    =================================
    0x2038: v2038(0x40) = CONST 
    0x203b: v203b = MLOAD v2038(0x40)
    0x203c: v203c(0x461bcd) = CONST 
    0x2040: v2040(0xe5) = CONST 
    0x2042: v2042(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2040(0xe5), v203c(0x461bcd)
    0x2044: MSTORE v203b, v2042(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2045: v2045(0x20) = CONST 
    0x2047: v2047(0x4) = CONST 
    0x204a: v204a = ADD v203b, v2047(0x4)
    0x204b: MSTORE v204a, v2045(0x20)
    0x204c: v204c(0xe) = CONST 
    0x204e: v204e(0x24) = CONST 
    0x2051: v2051 = ADD v203b, v204e(0x24)
    0x2052: MSTORE v2051, v204c(0xe)
    0x2053: v2053(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x2062: v2062(0x91) = CONST 
    0x2064: v2064(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v2062(0x91), v2053(0x36bab9ba1031329036b4b73a32b9)
    0x2065: v2065(0x44) = CONST 
    0x2068: v2068 = ADD v203b, v2065(0x44)
    0x2069: MSTORE v2068, v2064(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x206b: v206b = MLOAD v2038(0x40)
    0x206f: v206f(0x0) = SUB v203b, v206b
    0x2070: v2070(0x64) = CONST 
    0x2072: v2072(0x64) = ADD v2070(0x64), v206f(0x0)
    0x2074: REVERT v206b, v2072(0x64)

    Begin block 0x2075
    prev=[0x2020], succ=[0x312cB0x2075]
    =================================
    0x2076: v2076(0x2084) = CONST 
    0x2080: v2080(0x312c) = CONST 
    0x2083: JUMP v2080(0x312c)

    Begin block 0x312cB0x2075
    prev=[0x2075], succ=[0x3134B0x2075, 0x316aB0x2075]
    =================================
    0x312dS0x2075: v312dV2075(0x0) = CONST 
    0x3130S0x2075: v3130V2075(0x316a) = CONST 
    0x3133S0x2075: JUMPI v3130V2075(0x316a), vafb

    Begin block 0x3134B0x2075
    prev=[0x312cB0x2075], succ=[]
    =================================
    0x3134S0x2075: v3134V2075(0x40) = CONST 
    0x3136S0x2075: v3136V2075 = MLOAD v3134V2075(0x40)
    0x3137S0x2075: v3137V2075(0x461bcd) = CONST 
    0x313bS0x2075: v313bV2075(0xe5) = CONST 
    0x313dS0x2075: v313dV2075(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v313bV2075(0xe5), v3137V2075(0x461bcd)
    0x313fS0x2075: MSTORE v3136V2075, v313dV2075(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3140S0x2075: v3140V2075(0x4) = CONST 
    0x3142S0x2075: v3142V2075 = ADD v3140V2075(0x4), v3136V2075
    0x3145S0x2075: v3145V2075(0x20) = CONST 
    0x3147S0x2075: v3147V2075 = ADD v3145V2075(0x20), v3142V2075
    0x314aS0x2075: v314aV2075(0x20) = SUB v3147V2075, v3142V2075
    0x314cS0x2075: MSTORE v3142V2075, v314aV2075(0x20)
    0x314dS0x2075: v314dV2075(0x24) = CONST 
    0x3150S0x2075: MSTORE v3147V2075, v314dV2075(0x24)
    0x3151S0x2075: v3151V2075(0x20) = CONST 
    0x3153S0x2075: v3153V2075 = ADD v3151V2075(0x20), v3147V2075
    0x3155S0x2075: v3155V2075(0x3a0f) = CONST 
    0x3158S0x2075: v3158V2075(0x24) = CONST 
    0x315bS0x2075: CODECOPY v3153V2075, v3155V2075(0x3a0f), v3158V2075(0x24)
    0x315cS0x2075: v315cV2075(0x40) = CONST 
    0x315eS0x2075: v315eV2075 = ADD v315cV2075(0x40), v3153V2075
    0x3162S0x2075: v3162V2075(0x40) = CONST 
    0x3164S0x2075: v3164V2075 = MLOAD v3162V2075(0x40)
    0x3167S0x2075: v3167V2075(0x84) = SUB v315eV2075, v3164V2075
    0x3169S0x2075: REVERT v3164V2075, v3167V2075(0x84)

    Begin block 0x316aB0x2075
    prev=[0x312cB0x2075], succ=[0x3172B0x2075, 0x31a8B0x2075]
    =================================
    0x316dS0x2075: v316dV2075 = EQ vb4b, vafb
    0x316eS0x2075: v316eV2075(0x31a8) = CONST 
    0x3171S0x2075: JUMPI v316eV2075(0x31a8), v316dV2075

    Begin block 0x3172B0x2075
    prev=[0x316aB0x2075], succ=[]
    =================================
    0x3172S0x2075: v3172V2075(0x40) = CONST 
    0x3174S0x2075: v3174V2075 = MLOAD v3172V2075(0x40)
    0x3175S0x2075: v3175V2075(0x461bcd) = CONST 
    0x3179S0x2075: v3179V2075(0xe5) = CONST 
    0x317bS0x2075: v317bV2075(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3179V2075(0xe5), v3175V2075(0x461bcd)
    0x317dS0x2075: MSTORE v3174V2075, v317bV2075(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x317eS0x2075: v317eV2075(0x4) = CONST 
    0x3180S0x2075: v3180V2075 = ADD v317eV2075(0x4), v3174V2075
    0x3183S0x2075: v3183V2075(0x20) = CONST 
    0x3185S0x2075: v3185V2075 = ADD v3183V2075(0x20), v3180V2075
    0x3188S0x2075: v3188V2075(0x20) = SUB v3185V2075, v3180V2075
    0x318aS0x2075: MSTORE v3180V2075, v3188V2075(0x20)
    0x318bS0x2075: v318bV2075(0x2b) = CONST 
    0x318eS0x2075: MSTORE v3185V2075, v318bV2075(0x2b)
    0x318fS0x2075: v318fV2075(0x20) = CONST 
    0x3191S0x2075: v3191V2075 = ADD v318fV2075(0x20), v3185V2075
    0x3193S0x2075: v3193V2075(0x3a5e) = CONST 
    0x3196S0x2075: v3196V2075(0x2b) = CONST 
    0x3199S0x2075: CODECOPY v3191V2075, v3193V2075(0x3a5e), v3196V2075(0x2b)
    0x319aS0x2075: v319aV2075(0x40) = CONST 
    0x319cS0x2075: v319cV2075 = ADD v319aV2075(0x40), v3191V2075
    0x31a0S0x2075: v31a0V2075(0x40) = CONST 
    0x31a2S0x2075: v31a2V2075 = MLOAD v31a0V2075(0x40)
    0x31a5S0x2075: v31a5V2075(0x84) = SUB v319cV2075, v31a2V2075
    0x31a7S0x2075: REVERT v31a2V2075, v31a5V2075(0x84)

    Begin block 0x31a8B0x2075
    prev=[0x316aB0x2075], succ=[0x31b4B0x2075]
    =================================
    0x31a9S0x2075: v31a9V2075(0x0) = CONST 
    0x31abS0x2075: v31abV2075(0x31b4) = CONST 
    0x31b0S0x2075: v31b0V2075(0x2ad1) = CONST 
    0x31b3S0x2075: v31b3_0V2075 = CALLPRIVATE v31b0V2075(0x2ad1), vac2, vabc, v31abV2075(0x31b4)

    Begin block 0x31b4B0x2075
    prev=[0x31a8B0x2075], succ=[0x38c0B0x31b4B0x2075]
    =================================
    0x31b5S0x2075: v31b5V2075(0x0) = CONST 
    0x31b9S0x2075: MSTORE v31b5V2075(0x0), v31b3_0V2075
    0x31baS0x2075: v31baV2075(0xc) = CONST 
    0x31bcS0x2075: v31bcV2075(0x20) = CONST 
    0x31beS0x2075: MSTORE v31bcV2075(0x20), v31baV2075(0xc)
    0x31bfS0x2075: v31bfV2075(0x40) = CONST 
    0x31c2S0x2075: v31c2V2075 = SHA3 v31b5V2075(0x0), v31bfV2075(0x40)
    0x31c3S0x2075: v31c3V2075(0x2) = CONST 
    0x31c6S0x2075: v31c6V2075 = ADD v31c2V2075, v31c3V2075(0x2)
    0x31c9S0x2075: SSTORE v31c6V2075, vac8
    0x31cdS0x2075: v31cdV2075(0x31d7) = CONST 
    0x31d3S0x2075: v31d3V2075(0x38c0) = CONST 
    0x31d6S0x2075: JUMP v31d3V2075(0x38c0)

    Begin block 0x38c0B0x31b4B0x2075
    prev=[0x31b4B0x2075], succ=[0x38daB0x31b4B0x2075, 0x388f0x38c0B0x31b4B0x2075]
    =================================
    0x38c3S0x31b4S0x2075: v38c3V31b4V2075 = SLOAD v31c2V2075
    0x38c6S0x31b4S0x2075: SSTORE v31c2V2075, vafb
    0x38c8S0x31b4S0x2075: v38c8V31b4V2075(0x0) = CONST 
    0x38caS0x31b4S0x2075: MSTORE v38c8V31b4V2075(0x0), v31c2V2075
    0x38cbS0x31b4S0x2075: v38cbV31b4V2075(0x20) = CONST 
    0x38cdS0x31b4S0x2075: v38cdV31b4V2075(0x0) = CONST 
    0x38cfS0x31b4S0x2075: v38cfV31b4V2075 = SHA3 v38cdV31b4V2075(0x0), v38cbV31b4V2075(0x20)
    0x38d2S0x31b4S0x2075: v38d2V31b4V2075 = ADD v38cfV31b4V2075, v38c3V31b4V2075
    0x38d5S0x31b4S0x2075: v38d5V31b4V2075 = ISZERO vafb
    0x38d6S0x31b4S0x2075: v38d6V31b4V2075(0x388f) = CONST 
    0x38d9S0x31b4S0x2075: JUMPI v38d6V31b4V2075(0x388f), v38d5V31b4V2075

    Begin block 0x38daB0x31b4B0x2075
    prev=[0x38c0B0x31b4B0x2075], succ=[0x38e0B0x31b4B0x2075]
    =================================
    0x38dbS0x31b4S0x2075: v38dbV31b4V2075(0x20) = CONST 
    0x38ddS0x31b4S0x2075: v38ddV31b4V2075 = MUL v38dbV31b4V2075(0x20), vafb
    0x38dfS0x31b4S0x2075: v38dfV31b4V2075 = ADD vaff, v38ddV31b4V2075

    Begin block 0x38e0B0x31b4B0x2075
    prev=[0x38daB0x31b4B0x2075, 0x38e9B0x31b4B0x2075], succ=[0x38e9B0x31b4B0x2075, 0x388f0x38c0B0x31b4B0x2075]
    =================================
    0x38e0_0x2S0x31b4S0x2075: v38e0_2V31b4V2075 = PHI vaff, v3907V31b4V2075
    0x38e3S0x31b4S0x2075: v38e3V31b4V2075 = GT v38dfV31b4V2075, v38e0_2V31b4V2075
    0x38e4S0x31b4S0x2075: v38e4V31b4V2075 = ISZERO v38e3V31b4V2075
    0x38e5S0x31b4S0x2075: v38e5V31b4V2075(0x388f) = CONST 
    0x38e8S0x31b4S0x2075: JUMPI v38e5V31b4V2075(0x388f), v38e4V31b4V2075

    Begin block 0x38e9B0x31b4B0x2075
    prev=[0x38e0B0x31b4B0x2075], succ=[0x38e0B0x31b4B0x2075]
    =================================
    0x38e9_0x1S0x31b4S0x2075: v38e9_1V31b4V2075 = PHI v38cfV31b4V2075, v390dV31b4V2075
    0x38e9_0x2S0x31b4S0x2075: v38e9_2V31b4V2075 = PHI vaff, v3907V31b4V2075
    0x38eaS0x31b4S0x2075: v38eaV31b4V2075 = SLOAD v38e9_1V31b4V2075
    0x38ebS0x31b4S0x2075: v38ebV31b4V2075(0x1) = CONST 
    0x38edS0x31b4S0x2075: v38edV31b4V2075(0x1) = CONST 
    0x38efS0x31b4S0x2075: v38efV31b4V2075(0xa0) = CONST 
    0x38f1S0x31b4S0x2075: v38f1V31b4V2075(0x10000000000000000000000000000000000000000) = SHL v38efV31b4V2075(0xa0), v38edV31b4V2075(0x1)
    0x38f2S0x31b4S0x2075: v38f2V31b4V2075(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38f1V31b4V2075(0x10000000000000000000000000000000000000000), v38ebV31b4V2075(0x1)
    0x38f3S0x31b4S0x2075: v38f3V31b4V2075(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v38f2V31b4V2075(0xffffffffffffffffffffffffffffffffffffffff)
    0x38f4S0x31b4S0x2075: v38f4V31b4V2075 = AND v38f3V31b4V2075(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v38eaV31b4V2075
    0x38f5S0x31b4S0x2075: v38f5V31b4V2075(0x1) = CONST 
    0x38f7S0x31b4S0x2075: v38f7V31b4V2075(0x1) = CONST 
    0x38f9S0x31b4S0x2075: v38f9V31b4V2075(0xa0) = CONST 
    0x38fbS0x31b4S0x2075: v38fbV31b4V2075(0x10000000000000000000000000000000000000000) = SHL v38f9V31b4V2075(0xa0), v38f7V31b4V2075(0x1)
    0x38fcS0x31b4S0x2075: v38fcV31b4V2075(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38fbV31b4V2075(0x10000000000000000000000000000000000000000), v38f5V31b4V2075(0x1)
    0x38feS0x31b4S0x2075: v38feV31b4V2075 = CALLDATALOAD v38e9_2V31b4V2075
    0x38ffS0x31b4S0x2075: v38ffV31b4V2075 = AND v38feV31b4V2075, v38fcV31b4V2075(0xffffffffffffffffffffffffffffffffffffffff)
    0x3900S0x31b4S0x2075: v3900V31b4V2075 = OR v38ffV31b4V2075, v38f4V31b4V2075
    0x3902S0x31b4S0x2075: SSTORE v38e9_1V31b4V2075, v3900V31b4V2075
    0x3903S0x31b4S0x2075: v3903V31b4V2075(0x20) = CONST 
    0x3907S0x31b4S0x2075: v3907V31b4V2075 = ADD v38e9_2V31b4V2075, v3903V31b4V2075(0x20)
    0x3909S0x31b4S0x2075: v3909V31b4V2075(0x1) = CONST 
    0x390dS0x31b4S0x2075: v390dV31b4V2075 = ADD v38e9_1V31b4V2075, v3909V31b4V2075(0x1)
    0x390fS0x31b4S0x2075: v390fV31b4V2075(0x38e0) = CONST 
    0x3912S0x31b4S0x2075: JUMP v390fV31b4V2075(0x38e0)

    Begin block 0x388f0x38c0B0x31b4B0x2075
    prev=[0x38c0B0x31b4B0x2075, 0x38e0B0x31b4B0x2075], succ=[0x394eB0x388f0x38c0B0x31b4B0x2075]
    =================================
    0x388f0x38c0_0x1S0x31b4S0x2075: v388f38c0_1V31b4V2075 = PHI v38cfV31b4V2075, v390dV31b4V2075
    0x38910x38c0S0x31b4S0x2075: v38c03891V31b4V2075(0x4579) = CONST 
    0x38970x38c0S0x31b4S0x2075: v38c03897V31b4V2075(0x394e) = CONST 
    0x389a0x38c0S0x31b4S0x2075: JUMP v38c03897V31b4V2075(0x394e)

    Begin block 0x394eB0x388f0x38c0B0x31b4B0x2075
    prev=[0x388f0x38c0B0x31b4B0x2075], succ=[0x394fB0x388f0x38c0B0x31b4B0x2075]
    =================================

    Begin block 0x394fB0x388f0x38c0B0x31b4B0x2075
    prev=[0x3958B0x388f0x38c0B0x31b4B0x2075, 0x394eB0x388f0x38c0B0x31b4B0x2075], succ=[0x3958B0x388f0x38c0B0x31b4B0x2075, 0x459cB0x388f0x38c0B0x31b4B0x2075]
    =================================
    0x394f_0x0S0x388f0x38c0S0x31b4S0x2075: v394f_0V388f38c0V31b4V2075 = PHI v388f38c0_1V31b4V2075, v395eV388f38c0V31b4V2075
    0x3952S0x388f0x38c0S0x31b4S0x2075: v3952V388f38c0V31b4V2075 = GT v38d2V31b4V2075, v394f_0V388f38c0V31b4V2075
    0x3953S0x388f0x38c0S0x31b4S0x2075: v3953V388f38c0V31b4V2075 = ISZERO v3952V388f38c0V31b4V2075
    0x3954S0x388f0x38c0S0x31b4S0x2075: v3954V388f38c0V31b4V2075(0x459c) = CONST 
    0x3957S0x388f0x38c0S0x31b4S0x2075: JUMPI v3954V388f38c0V31b4V2075(0x459c), v3953V388f38c0V31b4V2075

    Begin block 0x3958B0x388f0x38c0B0x31b4B0x2075
    prev=[0x394fB0x388f0x38c0B0x31b4B0x2075], succ=[0x394fB0x388f0x38c0B0x31b4B0x2075]
    =================================
    0x3958S0x388f0x38c0S0x31b4S0x2075: v3958V388f38c0V31b4V2075(0x0) = CONST 
    0x3958_0x0S0x388f0x38c0S0x31b4S0x2075: v3958_0V388f38c0V31b4V2075 = PHI v388f38c0_1V31b4V2075, v395eV388f38c0V31b4V2075
    0x395bS0x388f0x38c0S0x31b4S0x2075: SSTORE v3958_0V388f38c0V31b4V2075, v3958V388f38c0V31b4V2075(0x0)
    0x395cS0x388f0x38c0S0x31b4S0x2075: v395cV388f38c0V31b4V2075(0x1) = CONST 
    0x395eS0x388f0x38c0S0x31b4S0x2075: v395eV388f38c0V31b4V2075 = ADD v395cV388f38c0V31b4V2075(0x1), v3958_0V388f38c0V31b4V2075
    0x395fS0x388f0x38c0S0x31b4S0x2075: v395fV388f38c0V31b4V2075(0x394f) = CONST 
    0x3962S0x388f0x38c0S0x31b4S0x2075: JUMP v395fV388f38c0V31b4V2075(0x394f)

    Begin block 0x459cB0x388f0x38c0B0x31b4B0x2075
    prev=[0x394fB0x388f0x38c0B0x31b4B0x2075], succ=[0x45790x38c0B0x31b4B0x2075]
    =================================
    0x459fS0x388f0x38c0S0x31b4S0x2075: JUMP v38c03891V31b4V2075(0x4579)

    Begin block 0x45790x38c0B0x31b4B0x2075
    prev=[0x459cB0x388f0x38c0B0x31b4B0x2075], succ=[0x31d7B0x2075]
    =================================
    0x457c0x38c0S0x31b4S0x2075: JUMP v31cdV2075(0x31d7)

    Begin block 0x31d7B0x2075
    prev=[0x45790x38c0B0x31b4B0x2075], succ=[0x3913B0x31d7B0x2075]
    =================================
    0x31d9S0x2075: v31d9V2075(0x0) = CONST 
    0x31ddS0x2075: MSTORE v31d9V2075(0x0), v31b3_0V2075
    0x31deS0x2075: v31deV2075(0xc) = CONST 
    0x31e0S0x2075: v31e0V2075(0x20) = CONST 
    0x31e2S0x2075: MSTORE v31e0V2075(0x20), v31deV2075(0xc)
    0x31e3S0x2075: v31e3V2075(0x40) = CONST 
    0x31e6S0x2075: v31e6V2075 = SHA3 v31d9V2075(0x0), v31e3V2075(0x40)
    0x31e7S0x2075: v31e7V2075(0x31f4) = CONST 
    0x31ebS0x2075: v31ebV2075(0x1) = CONST 
    0x31edS0x2075: v31edV2075 = ADD v31ebV2075(0x1), v31e6V2075
    0x31f0S0x2075: v31f0V2075(0x3913) = CONST 
    0x31f3S0x2075: JUMP v31f0V2075(0x3913)

    Begin block 0x3913B0x31d7B0x2075
    prev=[0x31d7B0x2075], succ=[0x392dB0x31d7B0x2075, 0x388f0x3913B0x31d7B0x2075]
    =================================
    0x3916S0x31d7S0x2075: v3916V31d7V2075 = SLOAD v31edV2075
    0x3919S0x31d7S0x2075: SSTORE v31edV2075, vb4b
    0x391bS0x31d7S0x2075: v391bV31d7V2075(0x0) = CONST 
    0x391dS0x31d7S0x2075: MSTORE v391bV31d7V2075(0x0), v31edV2075
    0x391eS0x31d7S0x2075: v391eV31d7V2075(0x20) = CONST 
    0x3920S0x31d7S0x2075: v3920V31d7V2075(0x0) = CONST 
    0x3922S0x31d7S0x2075: v3922V31d7V2075 = SHA3 v3920V31d7V2075(0x0), v391eV31d7V2075(0x20)
    0x3925S0x31d7S0x2075: v3925V31d7V2075 = ADD v3922V31d7V2075, v3916V31d7V2075
    0x3928S0x31d7S0x2075: v3928V31d7V2075 = ISZERO vb4b
    0x3929S0x31d7S0x2075: v3929V31d7V2075(0x388f) = CONST 
    0x392cS0x31d7S0x2075: JUMPI v3929V31d7V2075(0x388f), v3928V31d7V2075

    Begin block 0x392dB0x31d7B0x2075
    prev=[0x3913B0x31d7B0x2075], succ=[0x3933B0x31d7B0x2075]
    =================================
    0x392eS0x31d7S0x2075: v392eV31d7V2075(0x20) = CONST 
    0x3930S0x31d7S0x2075: v3930V31d7V2075 = MUL v392eV31d7V2075(0x20), vb4b
    0x3932S0x31d7S0x2075: v3932V31d7V2075 = ADD vb4f, v3930V31d7V2075

    Begin block 0x3933B0x31d7B0x2075
    prev=[0x392dB0x31d7B0x2075, 0x393cB0x31d7B0x2075], succ=[0x393cB0x31d7B0x2075, 0x388f0x3913B0x31d7B0x2075]
    =================================
    0x3933_0x2S0x31d7S0x2075: v3933_2V31d7V2075 = PHI vb4f, v3943V31d7V2075
    0x3936S0x31d7S0x2075: v3936V31d7V2075 = GT v3932V31d7V2075, v3933_2V31d7V2075
    0x3937S0x31d7S0x2075: v3937V31d7V2075 = ISZERO v3936V31d7V2075
    0x3938S0x31d7S0x2075: v3938V31d7V2075(0x388f) = CONST 
    0x393bS0x31d7S0x2075: JUMPI v3938V31d7V2075(0x388f), v3937V31d7V2075

    Begin block 0x393cB0x31d7B0x2075
    prev=[0x3933B0x31d7B0x2075], succ=[0x3933B0x31d7B0x2075]
    =================================
    0x393c_0x1S0x31d7S0x2075: v393c_1V31d7V2075 = PHI v3922V31d7V2075, v3948V31d7V2075
    0x393c_0x2S0x31d7S0x2075: v393c_2V31d7V2075 = PHI vb4f, v3943V31d7V2075
    0x393dS0x31d7S0x2075: v393dV31d7V2075 = CALLDATALOAD v393c_2V31d7V2075
    0x393fS0x31d7S0x2075: SSTORE v393c_1V31d7V2075, v393dV31d7V2075
    0x3941S0x31d7S0x2075: v3941V31d7V2075(0x20) = CONST 
    0x3943S0x31d7S0x2075: v3943V31d7V2075 = ADD v3941V31d7V2075(0x20), v393c_2V31d7V2075
    0x3946S0x31d7S0x2075: v3946V31d7V2075(0x1) = CONST 
    0x3948S0x31d7S0x2075: v3948V31d7V2075 = ADD v3946V31d7V2075(0x1), v393c_1V31d7V2075
    0x394aS0x31d7S0x2075: v394aV31d7V2075(0x3933) = CONST 
    0x394dS0x31d7S0x2075: JUMP v394aV31d7V2075(0x3933)

    Begin block 0x388f0x3913B0x31d7B0x2075
    prev=[0x3913B0x31d7B0x2075, 0x3933B0x31d7B0x2075], succ=[0x394eB0x388f0x3913B0x31d7B0x2075]
    =================================
    0x388f0x3913_0x1S0x31d7S0x2075: v388f3913_1V31d7V2075 = PHI v3922V31d7V2075, v3948V31d7V2075
    0x38910x3913S0x31d7S0x2075: v39133891V31d7V2075(0x4579) = CONST 
    0x38970x3913S0x31d7S0x2075: v39133897V31d7V2075(0x394e) = CONST 
    0x389a0x3913S0x31d7S0x2075: JUMP v39133897V31d7V2075(0x394e)

    Begin block 0x394eB0x388f0x3913B0x31d7B0x2075
    prev=[0x388f0x3913B0x31d7B0x2075], succ=[0x394fB0x388f0x3913B0x31d7B0x2075]
    =================================

    Begin block 0x394fB0x388f0x3913B0x31d7B0x2075
    prev=[0x3958B0x388f0x3913B0x31d7B0x2075, 0x394eB0x388f0x3913B0x31d7B0x2075], succ=[0x3958B0x388f0x3913B0x31d7B0x2075, 0x459cB0x388f0x3913B0x31d7B0x2075]
    =================================
    0x394f_0x0S0x388f0x3913S0x31d7S0x2075: v394f_0V388f3913V31d7V2075 = PHI v388f3913_1V31d7V2075, v395eV388f3913V31d7V2075
    0x3952S0x388f0x3913S0x31d7S0x2075: v3952V388f3913V31d7V2075 = GT v3925V31d7V2075, v394f_0V388f3913V31d7V2075
    0x3953S0x388f0x3913S0x31d7S0x2075: v3953V388f3913V31d7V2075 = ISZERO v3952V388f3913V31d7V2075
    0x3954S0x388f0x3913S0x31d7S0x2075: v3954V388f3913V31d7V2075(0x459c) = CONST 
    0x3957S0x388f0x3913S0x31d7S0x2075: JUMPI v3954V388f3913V31d7V2075(0x459c), v3953V388f3913V31d7V2075

    Begin block 0x3958B0x388f0x3913B0x31d7B0x2075
    prev=[0x394fB0x388f0x3913B0x31d7B0x2075], succ=[0x394fB0x388f0x3913B0x31d7B0x2075]
    =================================
    0x3958S0x388f0x3913S0x31d7S0x2075: v3958V388f3913V31d7V2075(0x0) = CONST 
    0x3958_0x0S0x388f0x3913S0x31d7S0x2075: v3958_0V388f3913V31d7V2075 = PHI v388f3913_1V31d7V2075, v395eV388f3913V31d7V2075
    0x395bS0x388f0x3913S0x31d7S0x2075: SSTORE v3958_0V388f3913V31d7V2075, v3958V388f3913V31d7V2075(0x0)
    0x395cS0x388f0x3913S0x31d7S0x2075: v395cV388f3913V31d7V2075(0x1) = CONST 
    0x395eS0x388f0x3913S0x31d7S0x2075: v395eV388f3913V31d7V2075 = ADD v395cV388f3913V31d7V2075(0x1), v3958_0V388f3913V31d7V2075
    0x395fS0x388f0x3913S0x31d7S0x2075: v395fV388f3913V31d7V2075(0x394f) = CONST 
    0x3962S0x388f0x3913S0x31d7S0x2075: JUMP v395fV388f3913V31d7V2075(0x394f)

    Begin block 0x459cB0x388f0x3913B0x31d7B0x2075
    prev=[0x394fB0x388f0x3913B0x31d7B0x2075], succ=[0x45790x3913B0x31d7B0x2075]
    =================================
    0x459fS0x388f0x3913S0x31d7S0x2075: JUMP v39133891V31d7V2075(0x4579)

    Begin block 0x45790x3913B0x31d7B0x2075
    prev=[0x459cB0x388f0x3913B0x31d7B0x2075], succ=[0x31f4B0x2075]
    =================================
    0x457c0x3913S0x31d7S0x2075: JUMP v31e7V2075(0x31f4)

    Begin block 0x31f4B0x2075
    prev=[0x45790x3913B0x31d7B0x2075], succ=[0x2084]
    =================================
    0x3200S0x2075: JUMP v2076(0x2084)

    Begin block 0x2084
    prev=[0x31f4B0x2075], succ=[0x4040]
    =================================
    0x208f: JUMP va9c(0x4040)

    Begin block 0x4040
    prev=[0x2084], succ=[]
    =================================
    0x4041: v4041(0x40) = CONST 
    0x4044: v4044 = MLOAD v4041(0x40)
    0x4047: MSTORE v4044, v31b3_0V2075
    0x4048: v4048 = MLOAD v4041(0x40)
    0x404c: v404c(0x0) = SUB v4044, v4048
    0x404d: v404d(0x20) = CONST 
    0x404f: v404f(0x20) = ADD v404d(0x20), v404c(0x0)
    0x4051: RETURN v4048, v404f(0x20)

}

function quasarInfo(uint256)() public {
    Begin block 0xb75
    prev=[], succ=[0xb87, 0xb8b]
    =================================
    0xb76: vb76(0xb92) = CONST 
    0xb79: vb79(0x4) = CONST 
    0xb7c: vb7c = CALLDATASIZE 
    0xb7d: vb7d = SUB vb7c, vb79(0x4)
    0xb7e: vb7e(0x20) = CONST 
    0xb81: vb81 = LT vb7d, vb7e(0x20)
    0xb82: vb82 = ISZERO vb81
    0xb83: vb83(0xb8b) = CONST 
    0xb86: JUMPI vb83(0xb8b), vb82

    Begin block 0xb87
    prev=[0xb75], succ=[]
    =================================
    0xb87: vb87(0x0) = CONST 
    0xb8a: REVERT vb87(0x0), vb87(0x0)

    Begin block 0xb8b
    prev=[0xb75], succ=[0x2090]
    =================================
    0xb8d: vb8d = CALLDATALOAD vb79(0x4)
    0xb8e: vb8e(0x2090) = CONST 
    0xb91: JUMP vb8e(0x2090)

    Begin block 0x2090
    prev=[0xb8b], succ=[0xb92]
    =================================
    0x2091: v2091(0x0) = CONST 
    0x2095: MSTORE v2091(0x0), vb8d
    0x2096: v2096(0xa) = CONST 
    0x2098: v2098(0x20) = CONST 
    0x209c: MSTORE v2098(0x20), v2096(0xa)
    0x209d: v209d(0x40) = CONST 
    0x20a1: v20a1 = SHA3 v2091(0x0), v209d(0x40)
    0x20a2: v20a2 = SLOAD v20a1
    0x20a3: v20a3(0xb) = CONST 
    0x20a7: MSTORE v2098(0x20), v20a3(0xb)
    0x20aa: v20aa = SHA3 v2091(0x0), v209d(0x40)
    0x20ac: v20ac = SLOAD v20aa
    0x20ad: v20ad(0x1) = CONST 
    0x20b0: v20b0 = ADD v20aa, v20ad(0x1)
    0x20b1: v20b1 = SLOAD v20b0
    0x20b2: v20b2(0x2) = CONST 
    0x20b6: v20b6 = ADD v20aa, v20b2(0x2)
    0x20b7: v20b7 = SLOAD v20b6
    0x20b8: v20b8(0x1) = CONST 
    0x20ba: v20ba(0x1) = CONST 
    0x20bc: v20bc(0x80) = CONST 
    0x20be: v20be(0x100000000000000000000000000000000) = SHL v20bc(0x80), v20ba(0x1)
    0x20bf: v20bf(0xffffffffffffffffffffffffffffffff) = SUB v20be(0x100000000000000000000000000000000), v20b8(0x1)
    0x20c2: v20c2 = AND v20a2, v20bf(0xffffffffffffffffffffffffffffffff)
    0x20c4: v20c4(0x1) = CONST 
    0x20c6: v20c6(0x1) = CONST 
    0x20c8: v20c8(0xa0) = CONST 
    0x20ca: v20ca(0x10000000000000000000000000000000000000000) = SHL v20c8(0xa0), v20c6(0x1)
    0x20cb: v20cb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20ca(0x10000000000000000000000000000000000000000), v20c4(0x1)
    0x20ce: v20ce = AND v20ac, v20cb(0xffffffffffffffffffffffffffffffffffffffff)
    0x20d1: JUMP vb76(0xb92)

    Begin block 0xb92
    prev=[0x2090], succ=[]
    =================================
    0xb93: vb93(0x40) = CONST 
    0xb96: vb96 = MLOAD vb93(0x40)
    0xb97: vb97(0x1) = CONST 
    0xb99: vb99(0x1) = CONST 
    0xb9b: vb9b(0x80) = CONST 
    0xb9d: vb9d(0x100000000000000000000000000000000) = SHL vb9b(0x80), vb99(0x1)
    0xb9e: vb9e(0xffffffffffffffffffffffffffffffff) = SUB vb9d(0x100000000000000000000000000000000), vb97(0x1)
    0xba1: vba1 = AND v20c2, vb9e(0xffffffffffffffffffffffffffffffff)
    0xba3: MSTORE vb96, vba1
    0xba4: vba4(0x1) = CONST 
    0xba6: vba6(0x1) = CONST 
    0xba8: vba8(0xa0) = CONST 
    0xbaa: vbaa(0x10000000000000000000000000000000000000000) = SHL vba8(0xa0), vba6(0x1)
    0xbab: vbab(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbaa(0x10000000000000000000000000000000000000000), vba4(0x1)
    0xbae: vbae = AND v20ce, vbab(0xffffffffffffffffffffffffffffffffffffffff)
    0xbaf: vbaf(0x20) = CONST 
    0xbb2: vbb2 = ADD vb96, vbaf(0x20)
    0xbb3: MSTORE vbb2, vbae
    0xbb6: vbb6 = ADD vb93(0x40), vb96
    0xbba: MSTORE vbb6, v20b1
    0xbbb: vbbb(0x60) = CONST 
    0xbbe: vbbe = ADD vb96, vbbb(0x60)
    0xbbf: MSTORE vbbe, v20b7
    0xbc0: vbc0 = MLOAD vb93(0x40)
    0xbc4: vbc4(0x0) = SUB vb96, vbc0
    0xbc5: vbc5(0x80) = CONST 
    0xbc7: vbc7(0x80) = ADD vbc5(0x80), vbc4(0x0)
    0xbc9: RETURN vbc0, vbc7(0x80)

}

function isMinter(address)() public {
    Begin block 0xbca
    prev=[], succ=[0xbdc, 0xbe0]
    =================================
    0xbcb: vbcb(0x4071) = CONST 
    0xbce: vbce(0x4) = CONST 
    0xbd1: vbd1 = CALLDATASIZE 
    0xbd2: vbd2 = SUB vbd1, vbce(0x4)
    0xbd3: vbd3(0x20) = CONST 
    0xbd6: vbd6 = LT vbd2, vbd3(0x20)
    0xbd7: vbd7 = ISZERO vbd6
    0xbd8: vbd8(0xbe0) = CONST 
    0xbdb: JUMPI vbd8(0xbe0), vbd7

    Begin block 0xbdc
    prev=[0xbca], succ=[]
    =================================
    0xbdc: vbdc(0x0) = CONST 
    0xbdf: REVERT vbdc(0x0), vbdc(0x0)

    Begin block 0xbe0
    prev=[0xbca], succ=[0x20d2]
    =================================
    0xbe2: vbe2 = CALLDATALOAD vbce(0x4)
    0xbe3: vbe3(0x1) = CONST 
    0xbe5: vbe5(0x1) = CONST 
    0xbe7: vbe7(0xa0) = CONST 
    0xbe9: vbe9(0x10000000000000000000000000000000000000000) = SHL vbe7(0xa0), vbe5(0x1)
    0xbea: vbea(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbe9(0x10000000000000000000000000000000000000000), vbe3(0x1)
    0xbeb: vbeb = AND vbea(0xffffffffffffffffffffffffffffffffffffffff), vbe2
    0xbec: vbec(0x20d2) = CONST 
    0xbef: JUMP vbec(0x20d2)

    Begin block 0x20d2
    prev=[0xbe0], succ=[0x4071]
    =================================
    0x20d3: v20d3(0x1) = CONST 
    0x20d5: v20d5(0x1) = CONST 
    0x20d7: v20d7(0xa0) = CONST 
    0x20d9: v20d9(0x10000000000000000000000000000000000000000) = SHL v20d7(0xa0), v20d5(0x1)
    0x20da: v20da(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20d9(0x10000000000000000000000000000000000000000), v20d3(0x1)
    0x20db: v20db = AND v20da(0xffffffffffffffffffffffffffffffffffffffff), vbeb
    0x20dc: v20dc(0x0) = CONST 
    0x20e0: MSTORE v20dc(0x0), v20db
    0x20e1: v20e1(0x5) = CONST 
    0x20e3: v20e3(0x20) = CONST 
    0x20e5: MSTORE v20e3(0x20), v20e1(0x5)
    0x20e6: v20e6(0x40) = CONST 
    0x20e9: v20e9 = SHA3 v20dc(0x0), v20e6(0x40)
    0x20ea: v20ea = SLOAD v20e9
    0x20eb: v20eb(0xff) = CONST 
    0x20ed: v20ed = AND v20eb(0xff), v20ea
    0x20ef: JUMP vbcb(0x4071)

    Begin block 0x4071
    prev=[0x20d2], succ=[]
    =================================
    0x4072: v4072(0x40) = CONST 
    0x4075: v4075 = MLOAD v4072(0x40)
    0x4077: v4077 = ISZERO v20ed
    0x4078: v4078 = ISZERO v4077
    0x407a: MSTORE v4075, v4078
    0x407b: v407b = MLOAD v4072(0x40)
    0x407f: v407f(0x0) = SUB v4075, v407b
    0x4080: v4080(0x20) = CONST 
    0x4082: v4082(0x20) = ADD v4080(0x20), v407f(0x0)
    0x4084: RETURN v407b, v4082(0x20)

}

function transferGalaxyCommunity(address)() public {
    Begin block 0xbf0
    prev=[], succ=[0xc02, 0xc06]
    =================================
    0xbf1: vbf1(0x40a4) = CONST 
    0xbf4: vbf4(0x4) = CONST 
    0xbf7: vbf7 = CALLDATASIZE 
    0xbf8: vbf8 = SUB vbf7, vbf4(0x4)
    0xbf9: vbf9(0x20) = CONST 
    0xbfc: vbfc = LT vbf8, vbf9(0x20)
    0xbfd: vbfd = ISZERO vbfc
    0xbfe: vbfe(0xc06) = CONST 
    0xc01: JUMPI vbfe(0xc06), vbfd

    Begin block 0xc02
    prev=[0xbf0], succ=[]
    =================================
    0xc02: vc02(0x0) = CONST 
    0xc05: REVERT vc02(0x0), vc02(0x0)

    Begin block 0xc06
    prev=[0xbf0], succ=[0x20f0]
    =================================
    0xc08: vc08 = CALLDATALOAD vbf4(0x4)
    0xc09: vc09(0x1) = CONST 
    0xc0b: vc0b(0x1) = CONST 
    0xc0d: vc0d(0xa0) = CONST 
    0xc0f: vc0f(0x10000000000000000000000000000000000000000) = SHL vc0d(0xa0), vc0b(0x1)
    0xc10: vc10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc0f(0x10000000000000000000000000000000000000000), vc09(0x1)
    0xc11: vc11 = AND vc10(0xffffffffffffffffffffffffffffffffffffffff), vc08
    0xc12: vc12(0x20f0) = CONST 
    0xc15: JUMP vc12(0x20f0)

    Begin block 0x20f0
    prev=[0xc06], succ=[0x2103, 0x214a]
    =================================
    0x20f1: v20f1(0x4) = CONST 
    0x20f3: v20f3 = SLOAD v20f1(0x4)
    0x20f4: v20f4(0x1) = CONST 
    0x20f6: v20f6(0x1) = CONST 
    0x20f8: v20f8(0xa0) = CONST 
    0x20fa: v20fa(0x10000000000000000000000000000000000000000) = SHL v20f8(0xa0), v20f6(0x1)
    0x20fb: v20fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20fa(0x10000000000000000000000000000000000000000), v20f4(0x1)
    0x20fc: v20fc = AND v20fb(0xffffffffffffffffffffffffffffffffffffffff), v20f3
    0x20fd: v20fd = CALLER 
    0x20fe: v20fe = EQ v20fd, v20fc
    0x20ff: v20ff(0x214a) = CONST 
    0x2102: JUMPI v20ff(0x214a), v20fe

    Begin block 0x2103
    prev=[0x20f0], succ=[]
    =================================
    0x2103: v2103(0x40) = CONST 
    0x2106: v2106 = MLOAD v2103(0x40)
    0x2107: v2107(0x461bcd) = CONST 
    0x210b: v210b(0xe5) = CONST 
    0x210d: v210d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v210b(0xe5), v2107(0x461bcd)
    0x210f: MSTORE v2106, v210d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2110: v2110(0x20) = CONST 
    0x2112: v2112(0x4) = CONST 
    0x2115: v2115 = ADD v2106, v2112(0x4)
    0x2116: MSTORE v2115, v2110(0x20)
    0x2117: v2117(0x18) = CONST 
    0x2119: v2119(0x24) = CONST 
    0x211c: v211c = ADD v2106, v2119(0x24)
    0x211d: MSTORE v211c, v2117(0x18)
    0x211e: v211e(0x6d7573742062652067616c61787920636f6d6d756e697479) = CONST 
    0x2137: v2137(0x40) = CONST 
    0x2139: v2139(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000) = SHL v2137(0x40), v211e(0x6d7573742062652067616c61787920636f6d6d756e697479)
    0x213a: v213a(0x44) = CONST 
    0x213d: v213d = ADD v2106, v213a(0x44)
    0x213e: MSTORE v213d, v2139(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000)
    0x2140: v2140 = MLOAD v2103(0x40)
    0x2144: v2144(0x0) = SUB v2106, v2140
    0x2145: v2145(0x64) = CONST 
    0x2147: v2147(0x64) = ADD v2145(0x64), v2144(0x0)
    0x2149: REVERT v2140, v2147(0x64)

    Begin block 0x214a
    prev=[0x20f0], succ=[0x2159, 0x218f]
    =================================
    0x214b: v214b(0x1) = CONST 
    0x214d: v214d(0x1) = CONST 
    0x214f: v214f(0xa0) = CONST 
    0x2151: v2151(0x10000000000000000000000000000000000000000) = SHL v214f(0xa0), v214d(0x1)
    0x2152: v2152(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2151(0x10000000000000000000000000000000000000000), v214b(0x1)
    0x2154: v2154 = AND vc11, v2152(0xffffffffffffffffffffffffffffffffffffffff)
    0x2155: v2155(0x218f) = CONST 
    0x2158: JUMPI v2155(0x218f), v2154

    Begin block 0x2159
    prev=[0x214a], succ=[]
    =================================
    0x2159: v2159(0x40) = CONST 
    0x215b: v215b = MLOAD v2159(0x40)
    0x215c: v215c(0x461bcd) = CONST 
    0x2160: v2160(0xe5) = CONST 
    0x2162: v2162(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2160(0xe5), v215c(0x461bcd)
    0x2164: MSTORE v215b, v2162(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2165: v2165(0x4) = CONST 
    0x2167: v2167 = ADD v2165(0x4), v215b
    0x216a: v216a(0x20) = CONST 
    0x216c: v216c = ADD v216a(0x20), v2167
    0x216f: v216f(0x20) = SUB v216c, v2167
    0x2171: MSTORE v2167, v216f(0x20)
    0x2172: v2172(0x2b) = CONST 
    0x2175: MSTORE v216c, v2172(0x2b)
    0x2176: v2176(0x20) = CONST 
    0x2178: v2178 = ADD v2176(0x20), v216c
    0x217a: v217a(0x3a89) = CONST 
    0x217d: v217d(0x2b) = CONST 
    0x2180: CODECOPY v2178, v217a(0x3a89), v217d(0x2b)
    0x2181: v2181(0x40) = CONST 
    0x2183: v2183 = ADD v2181(0x40), v2178
    0x2187: v2187(0x40) = CONST 
    0x2189: v2189 = MLOAD v2187(0x40)
    0x218c: v218c(0x84) = SUB v2183, v2189
    0x218e: REVERT v2189, v218c(0x84)

    Begin block 0x218f
    prev=[0x214a], succ=[0x40a4]
    =================================
    0x2190: v2190(0x4) = CONST 
    0x2193: v2193 = SLOAD v2190(0x4)
    0x2194: v2194(0x1) = CONST 
    0x2196: v2196(0x1) = CONST 
    0x2198: v2198(0xa0) = CONST 
    0x219a: v219a(0x10000000000000000000000000000000000000000) = SHL v2198(0xa0), v2196(0x1)
    0x219b: v219b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v219a(0x10000000000000000000000000000000000000000), v2194(0x1)
    0x219c: v219c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v219b(0xffffffffffffffffffffffffffffffffffffffff)
    0x219d: v219d = AND v219c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2193
    0x219e: v219e(0x1) = CONST 
    0x21a0: v21a0(0x1) = CONST 
    0x21a2: v21a2(0xa0) = CONST 
    0x21a4: v21a4(0x10000000000000000000000000000000000000000) = SHL v21a2(0xa0), v21a0(0x1)
    0x21a5: v21a5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21a4(0x10000000000000000000000000000000000000000), v219e(0x1)
    0x21a9: v21a9 = AND v21a5(0xffffffffffffffffffffffffffffffffffffffff), vc11
    0x21ad: v21ad = OR v21a9, v219d
    0x21af: SSTORE v2190(0x4), v21ad
    0x21b0: JUMP vbf1(0x40a4)

    Begin block 0x40a4
    prev=[0x218f], succ=[]
    =================================
    0x40a5: STOP 

}

function removeOperator(address)() public {
    Begin block 0xc16
    prev=[], succ=[0xc28, 0xc2c]
    =================================
    0xc17: vc17(0x40c5) = CONST 
    0xc1a: vc1a(0x4) = CONST 
    0xc1d: vc1d = CALLDATASIZE 
    0xc1e: vc1e = SUB vc1d, vc1a(0x4)
    0xc1f: vc1f(0x20) = CONST 
    0xc22: vc22 = LT vc1e, vc1f(0x20)
    0xc23: vc23 = ISZERO vc22
    0xc24: vc24(0xc2c) = CONST 
    0xc27: JUMPI vc24(0xc2c), vc23

    Begin block 0xc28
    prev=[0xc16], succ=[]
    =================================
    0xc28: vc28(0x0) = CONST 
    0xc2b: REVERT vc28(0x0), vc28(0x0)

    Begin block 0xc2c
    prev=[0xc16], succ=[0x21b1]
    =================================
    0xc2e: vc2e = CALLDATALOAD vc1a(0x4)
    0xc2f: vc2f(0x1) = CONST 
    0xc31: vc31(0x1) = CONST 
    0xc33: vc33(0xa0) = CONST 
    0xc35: vc35(0x10000000000000000000000000000000000000000) = SHL vc33(0xa0), vc31(0x1)
    0xc36: vc36(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc35(0x10000000000000000000000000000000000000000), vc2f(0x1)
    0xc37: vc37 = AND vc36(0xffffffffffffffffffffffffffffffffffffffff), vc2e
    0xc38: vc38(0x21b1) = CONST 
    0xc3b: JUMP vc38(0x21b1)

    Begin block 0x21b1
    prev=[0xc2c], succ=[0x21c4, 0x2200]
    =================================
    0x21b2: v21b2(0x3) = CONST 
    0x21b4: v21b4 = SLOAD v21b2(0x3)
    0x21b5: v21b5(0x1) = CONST 
    0x21b7: v21b7(0x1) = CONST 
    0x21b9: v21b9(0xa0) = CONST 
    0x21bb: v21bb(0x10000000000000000000000000000000000000000) = SHL v21b9(0xa0), v21b7(0x1)
    0x21bc: v21bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21bb(0x10000000000000000000000000000000000000000), v21b5(0x1)
    0x21bd: v21bd = AND v21bc(0xffffffffffffffffffffffffffffffffffffffff), v21b4
    0x21be: v21be = CALLER 
    0x21bf: v21bf = EQ v21be, v21bd
    0x21c0: v21c0(0x2200) = CONST 
    0x21c3: JUMPI v21c0(0x2200), v21bf

    Begin block 0x21c4
    prev=[0x21b1], succ=[]
    =================================
    0x21c4: v21c4(0x40) = CONST 
    0x21c7: v21c7 = MLOAD v21c4(0x40)
    0x21c8: v21c8(0x461bcd) = CONST 
    0x21cc: v21cc(0xe5) = CONST 
    0x21ce: v21ce(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v21cc(0xe5), v21c8(0x461bcd)
    0x21d0: MSTORE v21c7, v21ce(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21d1: v21d1(0x20) = CONST 
    0x21d3: v21d3(0x4) = CONST 
    0x21d6: v21d6 = ADD v21c7, v21d3(0x4)
    0x21d7: MSTORE v21d6, v21d1(0x20)
    0x21d8: v21d8(0xd) = CONST 
    0x21da: v21da(0x24) = CONST 
    0x21dd: v21dd = ADD v21c7, v21da(0x24)
    0x21de: MSTORE v21dd, v21d8(0xd)
    0x21df: v21df(0x26bab9ba1031329037bbb732b9) = CONST 
    0x21ed: v21ed(0x99) = CONST 
    0x21ef: v21ef(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v21ed(0x99), v21df(0x26bab9ba1031329037bbb732b9)
    0x21f0: v21f0(0x44) = CONST 
    0x21f3: v21f3 = ADD v21c7, v21f0(0x44)
    0x21f4: MSTORE v21f3, v21ef(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x21f6: v21f6 = MLOAD v21c4(0x40)
    0x21fa: v21fa(0x0) = SUB v21c7, v21f6
    0x21fb: v21fb(0x64) = CONST 
    0x21fd: v21fd(0x64) = ADD v21fb(0x64), v21fa(0x0)
    0x21ff: REVERT v21f6, v21fd(0x64)

    Begin block 0x2200
    prev=[0x21b1], succ=[0x2221, 0x226d]
    =================================
    0x2201: v2201(0x1) = CONST 
    0x2203: v2203(0x1) = CONST 
    0x2205: v2205(0xa0) = CONST 
    0x2207: v2207(0x10000000000000000000000000000000000000000) = SHL v2205(0xa0), v2203(0x1)
    0x2208: v2208(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2207(0x10000000000000000000000000000000000000000), v2201(0x1)
    0x220a: v220a = AND vc37, v2208(0xffffffffffffffffffffffffffffffffffffffff)
    0x220b: v220b(0x0) = CONST 
    0x220f: MSTORE v220b(0x0), v220a
    0x2210: v2210(0x6) = CONST 
    0x2212: v2212(0x20) = CONST 
    0x2214: MSTORE v2212(0x20), v2210(0x6)
    0x2215: v2215(0x40) = CONST 
    0x2218: v2218 = SHA3 v220b(0x0), v2215(0x40)
    0x2219: v2219 = SLOAD v2218
    0x221a: v221a(0xff) = CONST 
    0x221c: v221c = AND v221a(0xff), v2219
    0x221d: v221d(0x226d) = CONST 
    0x2220: JUMPI v221d(0x226d), v221c

    Begin block 0x2221
    prev=[0x2200], succ=[]
    =================================
    0x2221: v2221(0x40) = CONST 
    0x2224: v2224 = MLOAD v2221(0x40)
    0x2225: v2225(0x461bcd) = CONST 
    0x2229: v2229(0xe5) = CONST 
    0x222b: v222b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2229(0xe5), v2225(0x461bcd)
    0x222d: MSTORE v2224, v222b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x222e: v222e(0x20) = CONST 
    0x2230: v2230(0x4) = CONST 
    0x2233: v2233 = ADD v2224, v2230(0x4)
    0x2234: MSTORE v2233, v222e(0x20)
    0x2235: v2235(0x17) = CONST 
    0x2237: v2237(0x24) = CONST 
    0x223a: v223a = ADD v2224, v2237(0x24)
    0x223b: MSTORE v223a, v2235(0x17)
    0x223c: v223c(0x4f70657261746f7220646f6573206e6f74206578697374000000000000000000) = CONST 
    0x225d: v225d(0x44) = CONST 
    0x2260: v2260 = ADD v2224, v225d(0x44)
    0x2261: MSTORE v2260, v223c(0x4f70657261746f7220646f6573206e6f74206578697374000000000000000000)
    0x2263: v2263 = MLOAD v2221(0x40)
    0x2267: v2267(0x0) = SUB v2224, v2263
    0x2268: v2268(0x64) = CONST 
    0x226a: v226a(0x64) = ADD v2268(0x64), v2267(0x0)
    0x226c: REVERT v2263, v226a(0x64)

    Begin block 0x226d
    prev=[0x2200], succ=[0x40c5]
    =================================
    0x226e: v226e(0x1) = CONST 
    0x2270: v2270(0x1) = CONST 
    0x2272: v2272(0xa0) = CONST 
    0x2274: v2274(0x10000000000000000000000000000000000000000) = SHL v2272(0xa0), v2270(0x1)
    0x2275: v2275(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2274(0x10000000000000000000000000000000000000000), v226e(0x1)
    0x2276: v2276 = AND v2275(0xffffffffffffffffffffffffffffffffffffffff), vc37
    0x2277: v2277(0x0) = CONST 
    0x227b: MSTORE v2277(0x0), v2276
    0x227c: v227c(0x6) = CONST 
    0x227e: v227e(0x20) = CONST 
    0x2280: MSTORE v227e(0x20), v227c(0x6)
    0x2281: v2281(0x40) = CONST 
    0x2284: v2284 = SHA3 v2277(0x0), v2281(0x40)
    0x2286: v2286 = SLOAD v2284
    0x2287: v2287(0xff) = CONST 
    0x2289: v2289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2287(0xff)
    0x228a: v228a = AND v2289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2286
    0x228c: SSTORE v2284, v228a
    0x228d: JUMP vc17(0x40c5)

    Begin block 0x40c5
    prev=[0x226d], succ=[]
    =================================
    0x40c6: STOP 

}

function burnBatch(address,uint256[])() public {
    Begin block 0xc3c
    prev=[], succ=[0xc4e, 0xc52]
    =================================
    0xc3d: vc3d(0x40e6) = CONST 
    0xc40: vc40(0x4) = CONST 
    0xc43: vc43 = CALLDATASIZE 
    0xc44: vc44 = SUB vc43, vc40(0x4)
    0xc45: vc45(0x40) = CONST 
    0xc48: vc48 = LT vc44, vc45(0x40)
    0xc49: vc49 = ISZERO vc48
    0xc4a: vc4a(0xc52) = CONST 
    0xc4d: JUMPI vc4a(0xc52), vc49

    Begin block 0xc4e
    prev=[0xc3c], succ=[]
    =================================
    0xc4e: vc4e(0x0) = CONST 
    0xc51: REVERT vc4e(0x0), vc4e(0x0)

    Begin block 0xc52
    prev=[0xc3c], succ=[0xc78, 0xc7c]
    =================================
    0xc53: vc53(0x1) = CONST 
    0xc55: vc55(0x1) = CONST 
    0xc57: vc57(0xa0) = CONST 
    0xc59: vc59(0x10000000000000000000000000000000000000000) = SHL vc57(0xa0), vc55(0x1)
    0xc5a: vc5a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc59(0x10000000000000000000000000000000000000000), vc53(0x1)
    0xc5c: vc5c = CALLDATALOAD vc40(0x4)
    0xc5d: vc5d = AND vc5c, vc5a(0xffffffffffffffffffffffffffffffffffffffff)
    0xc61: vc61 = ADD vc40(0x4), vc44
    0xc63: vc63(0x40) = CONST 
    0xc66: vc66(0x44) = ADD vc40(0x4), vc63(0x40)
    0xc67: vc67(0x20) = CONST 
    0xc6a: vc6a(0x24) = ADD vc40(0x4), vc67(0x20)
    0xc6b: vc6b = CALLDATALOAD vc6a(0x24)
    0xc6c: vc6c(0x1) = CONST 
    0xc6e: vc6e(0x20) = CONST 
    0xc70: vc70(0x100000000) = SHL vc6e(0x20), vc6c(0x1)
    0xc72: vc72 = GT vc6b, vc70(0x100000000)
    0xc73: vc73 = ISZERO vc72
    0xc74: vc74(0xc7c) = CONST 
    0xc77: JUMPI vc74(0xc7c), vc73

    Begin block 0xc78
    prev=[0xc52], succ=[]
    =================================
    0xc78: vc78(0x0) = CONST 
    0xc7b: REVERT vc78(0x0), vc78(0x0)

    Begin block 0xc7c
    prev=[0xc52], succ=[0xc8a, 0xc8e]
    =================================
    0xc7e: vc7e = ADD vc40(0x4), vc6b
    0xc80: vc80(0x20) = CONST 
    0xc83: vc83 = ADD vc7e, vc80(0x20)
    0xc84: vc84 = GT vc83, vc61
    0xc85: vc85 = ISZERO vc84
    0xc86: vc86(0xc8e) = CONST 
    0xc89: JUMPI vc86(0xc8e), vc85

    Begin block 0xc8a
    prev=[0xc7c], succ=[]
    =================================
    0xc8a: vc8a(0x0) = CONST 
    0xc8d: REVERT vc8a(0x0), vc8a(0x0)

    Begin block 0xc8e
    prev=[0xc7c], succ=[0xcab, 0xcaf]
    =================================
    0xc90: vc90 = CALLDATALOAD vc7e
    0xc92: vc92(0x20) = CONST 
    0xc94: vc94 = ADD vc92(0x20), vc7e
    0xc97: vc97(0x20) = CONST 
    0xc9a: vc9a = MUL vc90, vc97(0x20)
    0xc9c: vc9c = ADD vc94, vc9a
    0xc9d: vc9d = GT vc9c, vc61
    0xc9e: vc9e(0x1) = CONST 
    0xca0: vca0(0x20) = CONST 
    0xca2: vca2(0x100000000) = SHL vca0(0x20), vc9e(0x1)
    0xca4: vca4 = GT vc90, vca2(0x100000000)
    0xca5: vca5 = OR vca4, vc9d
    0xca6: vca6 = ISZERO vca5
    0xca7: vca7(0xcaf) = CONST 
    0xcaa: JUMPI vca7(0xcaf), vca6

    Begin block 0xcab
    prev=[0xc8e], succ=[]
    =================================
    0xcab: vcab(0x0) = CONST 
    0xcae: REVERT vcab(0x0), vcab(0x0)

    Begin block 0xcaf
    prev=[0xc8e], succ=[0x228e]
    =================================
    0xcb6: vcb6(0x228e) = CONST 
    0xcb9: JUMP vcb6(0x228e)

    Begin block 0x228e
    prev=[0xcaf], succ=[0x22a6, 0x22e3]
    =================================
    0x228f: v228f = CALLER 
    0x2290: v2290(0x0) = CONST 
    0x2294: MSTORE v2290(0x0), v228f
    0x2295: v2295(0x5) = CONST 
    0x2297: v2297(0x20) = CONST 
    0x2299: MSTORE v2297(0x20), v2295(0x5)
    0x229a: v229a(0x40) = CONST 
    0x229d: v229d = SHA3 v2290(0x0), v229a(0x40)
    0x229e: v229e = SLOAD v229d
    0x229f: v229f(0xff) = CONST 
    0x22a1: v22a1 = AND v229f(0xff), v229e
    0x22a2: v22a2(0x22e3) = CONST 
    0x22a5: JUMPI v22a2(0x22e3), v22a1

    Begin block 0x22a6
    prev=[0x228e], succ=[]
    =================================
    0x22a6: v22a6(0x40) = CONST 
    0x22a9: v22a9 = MLOAD v22a6(0x40)
    0x22aa: v22aa(0x461bcd) = CONST 
    0x22ae: v22ae(0xe5) = CONST 
    0x22b0: v22b0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v22ae(0xe5), v22aa(0x461bcd)
    0x22b2: MSTORE v22a9, v22b0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22b3: v22b3(0x20) = CONST 
    0x22b5: v22b5(0x4) = CONST 
    0x22b8: v22b8 = ADD v22a9, v22b5(0x4)
    0x22b9: MSTORE v22b8, v22b3(0x20)
    0x22ba: v22ba(0xe) = CONST 
    0x22bc: v22bc(0x24) = CONST 
    0x22bf: v22bf = ADD v22a9, v22bc(0x24)
    0x22c0: MSTORE v22bf, v22ba(0xe)
    0x22c1: v22c1(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x22d0: v22d0(0x91) = CONST 
    0x22d2: v22d2(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v22d0(0x91), v22c1(0x36bab9ba1031329036b4b73a32b9)
    0x22d3: v22d3(0x44) = CONST 
    0x22d6: v22d6 = ADD v22a9, v22d3(0x44)
    0x22d7: MSTORE v22d6, v22d2(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x22d9: v22d9 = MLOAD v22a6(0x40)
    0x22dd: v22dd(0x0) = SUB v22a9, v22d9
    0x22de: v22de(0x64) = CONST 
    0x22e0: v22e0(0x64) = ADD v22de(0x64), v22dd(0x0)
    0x22e2: REVERT v22d9, v22e0(0x64)

    Begin block 0x22e3
    prev=[0x228e], succ=[0x22e6]
    =================================
    0x22e4: v22e4(0x0) = CONST 

    Begin block 0x22e6
    prev=[0x22e3, 0x234b], succ=[0x22ef, 0x2353]
    =================================
    0x22e6_0x0: v22e6_0 = PHI v22e4(0x0), v234e
    0x22e9: v22e9 = LT v22e6_0, vc90
    0x22ea: v22ea = ISZERO v22e9
    0x22eb: v22eb(0x2353) = CONST 
    0x22ee: JUMPI v22eb(0x2353), v22ea

    Begin block 0x22ef
    prev=[0x22e6], succ=[0x22fd, 0x22fe]
    =================================
    0x22ef: v22ef(0x230a) = CONST 
    0x22ef_0x0: v22ef_0 = PHI v22e4(0x0), v234e
    0x22f8: v22f8 = LT v22ef_0, vc90
    0x22f9: v22f9(0x22fe) = CONST 
    0x22fc: JUMPI v22f9(0x22fe), v22f8

    Begin block 0x22fd
    prev=[0x22ef], succ=[]
    =================================
    0x22fd: THROW 

    Begin block 0x22fe
    prev=[0x22ef], succ=[0x24970xc3c]
    =================================
    0x22fe_0x0: v22fe_0 = PHI v22e4(0x0), v234e
    0x2301: v2301(0x20) = CONST 
    0x2303: v2303 = MUL v2301(0x20), v22fe_0
    0x2304: v2304 = ADD v2303, vc94
    0x2305: v2305 = CALLDATALOAD v2304
    0x2306: v2306(0x2497) = CONST 
    0x2309: JUMP v2306(0x2497)

    Begin block 0x24970xc3c
    prev=[0x22fe], succ=[0x24af0xc3c, 0x24a80xc3c]
    =================================
    0x24980xc3c: vc3c2498(0x0) = CONST 
    0x249a0xc3c: vc3c249a(0x1) = CONST 
    0x249c0xc3c: vc3c249c(0x1) = CONST 
    0x249e0xc3c: vc3c249e(0xa0) = CONST 
    0x24a00xc3c: vc3c24a0(0x10000000000000000000000000000000000000000) = SHL vc3c249e(0xa0), vc3c249c(0x1)
    0x24a10xc3c: vc3c24a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc3c24a0(0x10000000000000000000000000000000000000000), vc3c249a(0x1)
    0x24a30xc3c: vc3c24a3 = AND vc5d, vc3c24a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x24a40xc3c: vc3c24a4(0x24af) = CONST 
    0x24a70xc3c: JUMPI vc3c24a4(0x24af), vc3c24a3

    Begin block 0x24af0xc3c
    prev=[0x24970xc3c], succ=[0x43ff0xc3c]
    =================================
    0x24b10xc3c: vc3c24b1(0x0) = CONST 
    0x24b50xc3c: MSTORE vc3c24b1(0x0), v2305
    0x24b60xc3c: vc3c24b6(0x8) = CONST 
    0x24b80xc3c: vc3c24b8(0x20) = CONST 
    0x24ba0xc3c: MSTORE vc3c24b8(0x20), vc3c24b6(0x8)
    0x24bb0xc3c: vc3c24bb(0x40) = CONST 
    0x24be0xc3c: vc3c24be = SHA3 vc3c24b1(0x0), vc3c24bb(0x40)
    0x24bf0xc3c: vc3c24bf = SLOAD vc3c24be
    0x24c00xc3c: vc3c24c0(0x1) = CONST 
    0x24c20xc3c: vc3c24c2(0x1) = CONST 
    0x24c40xc3c: vc3c24c4(0xa0) = CONST 
    0x24c60xc3c: vc3c24c6(0x10000000000000000000000000000000000000000) = SHL vc3c24c4(0xa0), vc3c24c2(0x1)
    0x24c70xc3c: vc3c24c7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc3c24c6(0x10000000000000000000000000000000000000000), vc3c24c0(0x1)
    0x24ca0xc3c: vc3c24ca = AND vc3c24c7(0xffffffffffffffffffffffffffffffffffffffff), vc5d
    0x24cc0xc3c: vc3c24cc = AND vc3c24bf, vc3c24c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x24cd0xc3c: vc3c24cd = EQ vc3c24cc, vc3c24ca
    0x24ce0xc3c: vc3c24ce(0x43ff) = CONST 
    0x24d10xc3c: JUMP vc3c24ce(0x43ff)

    Begin block 0x43ff0xc3c
    prev=[0x24af0xc3c], succ=[0x230a]
    =================================
    0x44040xc3c: JUMP v22ef(0x230a)

    Begin block 0x230a
    prev=[0x43da0xc3c, 0x43ff0xc3c], succ=[0x230f, 0x234b]
    =================================
    0x230a_0x0: v230a_0 = PHI vc3c24cd, vc3c24a9(0x0)
    0x230b: v230b(0x234b) = CONST 
    0x230e: JUMPI v230b(0x234b), v230a_0

    Begin block 0x230f
    prev=[0x230a], succ=[]
    =================================
    0x230f: v230f(0x40) = CONST 
    0x2312: v2312 = MLOAD v230f(0x40)
    0x2313: v2313(0x461bcd) = CONST 
    0x2317: v2317(0xe5) = CONST 
    0x2319: v2319(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2317(0xe5), v2313(0x461bcd)
    0x231b: MSTORE v2312, v2319(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x231c: v231c(0x20) = CONST 
    0x231e: v231e(0x4) = CONST 
    0x2321: v2321 = ADD v2312, v231e(0x4)
    0x2322: MSTORE v2321, v231c(0x20)
    0x2323: v2323(0xd) = CONST 
    0x2325: v2325(0x24) = CONST 
    0x2328: v2328 = ADD v2312, v2325(0x24)
    0x2329: MSTORE v2328, v2323(0xd)
    0x232a: v232a(0x2737ba103a34329037bbb732b9) = CONST 
    0x2338: v2338(0x99) = CONST 
    0x233a: v233a(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v2338(0x99), v232a(0x2737ba103a34329037bbb732b9)
    0x233b: v233b(0x44) = CONST 
    0x233e: v233e = ADD v2312, v233b(0x44)
    0x233f: MSTORE v233e, v233a(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x2341: v2341 = MLOAD v230f(0x40)
    0x2345: v2345(0x0) = SUB v2312, v2341
    0x2346: v2346(0x64) = CONST 
    0x2348: v2348(0x64) = ADD v2346(0x64), v2345(0x0)
    0x234a: REVERT v2341, v2348(0x64)

    Begin block 0x234b
    prev=[0x230a], succ=[0x22e6]
    =================================
    0x234b_0x0: v234b_0 = PHI v22e4(0x0), v234e
    0x234c: v234c(0x1) = CONST 
    0x234e: v234e = ADD v234c(0x1), v234b_0
    0x234f: v234f(0x22e6) = CONST 
    0x2352: JUMP v234f(0x22e6)

    Begin block 0x24a80xc3c
    prev=[0x24970xc3c], succ=[0x43da0xc3c]
    =================================
    0x24a90xc3c: vc3c24a9(0x0) = CONST 
    0x24ab0xc3c: vc3c24ab(0x43da) = CONST 
    0x24ae0xc3c: JUMP vc3c24ab(0x43da)

    Begin block 0x43da0xc3c
    prev=[0x24a80xc3c], succ=[0x230a]
    =================================
    0x43df0xc3c: JUMP v22ef(0x230a)

    Begin block 0x2353
    prev=[0x22e6], succ=[0x3201]
    =================================
    0x2355: v2355(0x2391) = CONST 
    0x235d: v235d(0x20) = CONST 
    0x235f: v235f = MUL v235d(0x20), vc90
    0x2360: v2360(0x20) = CONST 
    0x2362: v2362 = ADD v2360(0x20), v235f
    0x2363: v2363(0x40) = CONST 
    0x2365: v2365 = MLOAD v2363(0x40)
    0x2368: v2368 = ADD v2365, v2362
    0x2369: v2369(0x40) = CONST 
    0x236b: MSTORE v2369(0x40), v2368
    0x2373: MSTORE v2365, vc90
    0x2374: v2374(0x20) = CONST 
    0x2376: v2376 = ADD v2374(0x20), v2365
    0x2379: v2379(0x20) = CONST 
    0x237b: v237b = MUL v2379(0x20), vc90
    0x237f: CALLDATACOPY v2376, vc94, v237b
    0x2380: v2380(0x0) = CONST 
    0x2383: v2383 = ADD v2376, v237b
    0x2387: MSTORE v2383, v2380(0x0)
    0x2389: v2389(0x3201) = CONST 
    0x2390: JUMP v2389(0x3201)

    Begin block 0x3201
    prev=[0x2353], succ=[0x3217, 0x321b]
    =================================
    0x3202: v3202(0x0) = CONST 
    0x3205: v3205 = MLOAD v2365
    0x3206: v3206(0xffffffffffffffff) = CONST 
    0x3210: v3210 = GT v3205, v3206(0xffffffffffffffff)
    0x3212: v3212 = ISZERO v3210
    0x3213: v3213(0x321b) = CONST 
    0x3216: JUMPI v3213(0x321b), v3212

    Begin block 0x3217
    prev=[0x3201], succ=[]
    =================================
    0x3217: v3217(0x0) = CONST 
    0x321a: REVERT v3217(0x0), v3217(0x0)

    Begin block 0x321b
    prev=[0x3201], succ=[0x3245, 0x3236]
    =================================
    0x321d: v321d(0x40) = CONST 
    0x321f: v321f = MLOAD v321d(0x40)
    0x3223: MSTORE v321f, v3205
    0x3225: v3225(0x20) = CONST 
    0x3227: v3227 = MUL v3225(0x20), v3205
    0x3228: v3228(0x20) = CONST 
    0x322a: v322a = ADD v3228(0x20), v3227
    0x322c: v322c = ADD v321f, v322a
    0x322d: v322d(0x40) = CONST 
    0x322f: MSTORE v322d(0x40), v322c
    0x3231: v3231 = ISZERO v3205
    0x3232: v3232(0x3245) = CONST 
    0x3235: JUMPI v3232(0x3245), v3231

    Begin block 0x3245
    prev=[0x321b, 0x3236], succ=[0x324b]
    =================================
    0x3249: v3249(0x0) = CONST 

    Begin block 0x324b
    prev=[0x3245, 0x3378], succ=[0x3255, 0x338b]
    =================================
    0x324b_0x0: v324b_0 = PHI v3249(0x0), v3386
    0x324d: v324d = MLOAD v2365
    0x324f: v324f = LT v324b_0, v324d
    0x3250: v3250 = ISZERO v324f
    0x3251: v3251(0x338b) = CONST 
    0x3254: JUMPI v3251(0x338b), v3250

    Begin block 0x3255
    prev=[0x324b], succ=[0x3263, 0x3264]
    =================================
    0x3255: v3255(0x8) = CONST 
    0x3255_0x0: v3255_0 = PHI v3249(0x0), v3386
    0x3257: v3257(0x0) = CONST 
    0x325c: v325c = MLOAD v2365
    0x325e: v325e = LT v3255_0, v325c
    0x325f: v325f(0x3264) = CONST 
    0x3262: JUMPI v325f(0x3264), v325e

    Begin block 0x3263
    prev=[0x3255], succ=[]
    =================================
    0x3263: THROW 

    Begin block 0x3264
    prev=[0x3255], succ=[0x329f, 0x32a0]
    =================================
    0x3264_0x0: v3264_0 = PHI v3249(0x0), v3386
    0x3264_0x4: v3264_4 = PHI v3249(0x0), v3386
    0x3265: v3265(0x20) = CONST 
    0x3267: v3267 = MUL v3265(0x20), v3264_0
    0x3268: v3268(0x20) = CONST 
    0x326a: v326a = ADD v3268(0x20), v3267
    0x326b: v326b = ADD v326a, v2365
    0x326c: v326c = MLOAD v326b
    0x326e: MSTORE v3257(0x0), v326c
    0x326f: v326f(0x20) = CONST 
    0x3271: v3271(0x20) = ADD v326f(0x20), v3257(0x0)
    0x3274: MSTORE v3271(0x20), v3255(0x8)
    0x3275: v3275(0x20) = CONST 
    0x3277: v3277(0x40) = ADD v3275(0x20), v3271(0x20)
    0x3278: v3278(0x0) = CONST 
    0x327a: v327a = SHA3 v3278(0x0), v3277(0x40)
    0x327b: v327b(0x0) = CONST 
    0x327d: v327d(0x100) = CONST 
    0x3280: v3280(0x1) = EXP v327d(0x100), v327b(0x0)
    0x3282: v3282 = SLOAD v327a
    0x3284: v3284(0x1) = CONST 
    0x3286: v3286(0x1) = CONST 
    0x3288: v3288(0xa0) = CONST 
    0x328a: v328a(0x10000000000000000000000000000000000000000) = SHL v3288(0xa0), v3286(0x1)
    0x328b: v328b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v328a(0x10000000000000000000000000000000000000000), v3284(0x1)
    0x328c: v328c(0xffffffffffffffffffffffffffffffffffffffff) = MUL v328b(0xffffffffffffffffffffffffffffffffffffffff), v3280(0x1)
    0x328d: v328d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v328c(0xffffffffffffffffffffffffffffffffffffffff)
    0x328e: v328e = AND v328d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3282
    0x3290: SSTORE v327a, v328e
    0x3291: v3291(0xb) = CONST 
    0x3293: v3293(0x0) = CONST 
    0x3298: v3298 = MLOAD v2365
    0x329a: v329a = LT v3264_4, v3298
    0x329b: v329b(0x32a0) = CONST 
    0x329e: JUMPI v329b(0x32a0), v329a

    Begin block 0x329f
    prev=[0x3264], succ=[]
    =================================
    0x329f: THROW 

    Begin block 0x32a0
    prev=[0x3264], succ=[0x32e8, 0x32e9]
    =================================
    0x32a0_0x0: v32a0_0 = PHI v3249(0x0), v3386
    0x32a0_0x4: v32a0_4 = PHI v3249(0x0), v3386
    0x32a1: v32a1(0x20) = CONST 
    0x32a5: v32a5 = MUL v32a1(0x20), v32a0_0
    0x32a9: v32a9 = ADD v32a5, v2365
    0x32ab: v32ab = ADD v32a1(0x20), v32a9
    0x32ac: v32ac = MLOAD v32ab
    0x32ae: MSTORE v3293(0x0), v32ac
    0x32b0: v32b0(0x20) = ADD v3293(0x0), v32a1(0x20)
    0x32b4: MSTORE v32b0(0x20), v3291(0xb)
    0x32b5: v32b5(0x40) = CONST 
    0x32b7: v32b7(0x40) = ADD v32b5(0x40), v3293(0x0)
    0x32b8: v32b8(0x0) = CONST 
    0x32bc: v32bc = SHA3 v32b8(0x0), v32b7(0x40)
    0x32be: v32be = SLOAD v32bc
    0x32bf: v32bf(0x1) = CONST 
    0x32c1: v32c1(0x1) = CONST 
    0x32c3: v32c3(0xa0) = CONST 
    0x32c5: v32c5(0x10000000000000000000000000000000000000000) = SHL v32c3(0xa0), v32c1(0x1)
    0x32c6: v32c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32c5(0x10000000000000000000000000000000000000000), v32bf(0x1)
    0x32c7: v32c7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v32c6(0xffffffffffffffffffffffffffffffffffffffff)
    0x32c8: v32c8 = AND v32c7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v32be
    0x32ca: SSTORE v32bc, v32c8
    0x32cb: v32cb(0x1) = CONST 
    0x32ce: v32ce = ADD v32bc, v32cb(0x1)
    0x32d1: SSTORE v32ce, v32b8(0x0)
    0x32d2: v32d2(0x2) = CONST 
    0x32d4: v32d4 = ADD v32d2(0x2), v32bc
    0x32d7: SSTORE v32d4, v32b8(0x0)
    0x32d9: v32d9 = MLOAD v2365
    0x32da: v32da(0xc) = CONST 
    0x32e3: v32e3 = LT v32a0_4, v32d9
    0x32e4: v32e4(0x32e9) = CONST 
    0x32e7: JUMPI v32e4(0x32e9), v32e3

    Begin block 0x32e8
    prev=[0x32a0], succ=[]
    =================================
    0x32e8: THROW 

    Begin block 0x32e9
    prev=[0x32a0], succ=[0x389fB0x32e9]
    =================================
    0x32e9_0x0: v32e9_0 = PHI v3249(0x0), v3386
    0x32ea: v32ea(0x20) = CONST 
    0x32ec: v32ec = MUL v32ea(0x20), v32e9_0
    0x32ed: v32ed(0x20) = CONST 
    0x32ef: v32ef = ADD v32ed(0x20), v32ec
    0x32f0: v32f0 = ADD v32ef, v2365
    0x32f1: v32f1 = MLOAD v32f0
    0x32f3: MSTORE v32b8(0x0), v32f1
    0x32f4: v32f4(0x20) = CONST 
    0x32f6: v32f6(0x20) = ADD v32f4(0x20), v32b8(0x0)
    0x32f9: MSTORE v32f6(0x20), v32da(0xc)
    0x32fa: v32fa(0x20) = CONST 
    0x32fc: v32fc(0x40) = ADD v32fa(0x20), v32f6(0x20)
    0x32fd: v32fd(0x0) = CONST 
    0x32ff: v32ff = SHA3 v32fd(0x0), v32fc(0x40)
    0x3300: v3300(0x0) = CONST 
    0x3304: v3304 = ADD v32ff, v3300(0x0)
    0x3305: v3305(0x0) = CONST 
    0x3307: v3307(0x3310) = CONST 
    0x330c: v330c(0x389f) = CONST 
    0x330f: JUMP v330c(0x389f), v3305(0x0), v3304, v3307(0x3310)

    Begin block 0x389fB0x32e9
    prev=[0x32e9], succ=[0x394eB0x389fB0x32e9]
    =================================
    0x38a2S0x32e9: v38a2V32e9 = SLOAD v3304
    0x38a3S0x32e9: v38a3V32e9(0x0) = CONST 
    0x38a6S0x32e9: SSTORE v3304, v38a3V32e9(0x0)
    0x38a8S0x32e9: v38a8V32e9(0x0) = CONST 
    0x38aaS0x32e9: MSTORE v38a8V32e9(0x0), v3304
    0x38abS0x32e9: v38abV32e9(0x20) = CONST 
    0x38adS0x32e9: v38adV32e9(0x0) = CONST 
    0x38afS0x32e9: v38afV32e9 = SHA3 v38adV32e9(0x0), v38abV32e9(0x20)
    0x38b2S0x32e9: v38b2V32e9 = ADD v38afV32e9, v38a2V32e9
    0x38b4S0x32e9: v38b4V32e9(0x38bd) = CONST 
    0x38b9S0x32e9: v38b9V32e9(0x394e) = CONST 
    0x38bcS0x32e9: JUMP v38b9V32e9(0x394e)

    Begin block 0x394eB0x389fB0x32e9
    prev=[0x389fB0x32e9], succ=[0x394fB0x389fB0x32e9]
    =================================

    Begin block 0x394fB0x389fB0x32e9
    prev=[0x3958B0x389fB0x32e9, 0x394eB0x389fB0x32e9], succ=[0x3958B0x389fB0x32e9, 0x459cB0x389fB0x32e9]
    =================================
    0x394f_0x0S0x389fS0x32e9: v394f_0V389fV32e9 = PHI v38afV32e9, v395eV389fV32e9
    0x3952S0x389fS0x32e9: v3952V389fV32e9 = GT v38b2V32e9, v394f_0V389fV32e9
    0x3953S0x389fS0x32e9: v3953V389fV32e9 = ISZERO v3952V389fV32e9
    0x3954S0x389fS0x32e9: v3954V389fV32e9(0x459c) = CONST 
    0x3957S0x389fS0x32e9: JUMPI v3954V389fV32e9(0x459c), v3953V389fV32e9

    Begin block 0x3958B0x389fB0x32e9
    prev=[0x394fB0x389fB0x32e9], succ=[0x394fB0x389fB0x32e9]
    =================================
    0x3958S0x389fS0x32e9: v3958V389fV32e9(0x0) = CONST 
    0x3958_0x0S0x389fS0x32e9: v3958_0V389fV32e9 = PHI v38afV32e9, v395eV389fV32e9
    0x395bS0x389fS0x32e9: SSTORE v3958_0V389fV32e9, v3958V389fV32e9(0x0)
    0x395cS0x389fS0x32e9: v395cV389fV32e9(0x1) = CONST 
    0x395eS0x389fS0x32e9: v395eV389fV32e9 = ADD v395cV389fV32e9(0x1), v3958_0V389fV32e9
    0x395fS0x389fS0x32e9: v395fV389fV32e9(0x394f) = CONST 
    0x3962S0x389fS0x32e9: JUMP v395fV389fV32e9(0x394f)

    Begin block 0x459cB0x389fB0x32e9
    prev=[0x394fB0x389fB0x32e9], succ=[0x38bdB0x32e9]
    =================================
    0x459fS0x389fS0x32e9: JUMP v38b4V32e9(0x38bd)

    Begin block 0x38bdB0x32e9
    prev=[0x459cB0x389fB0x32e9], succ=[0x3310]
    =================================
    0x38bfS0x32e9: JUMP v3307(0x3310)

    Begin block 0x3310
    prev=[0x38bdB0x32e9], succ=[0x389fB0x3310]
    =================================
    0x3311: v3311(0x331e) = CONST 
    0x3314: v3314(0x1) = CONST 
    0x3317: v3317 = ADD v32ff, v3314(0x1)
    0x3318: v3318(0x0) = CONST 
    0x331a: v331a(0x389f) = CONST 
    0x331d: JUMP v331a(0x389f), v3318(0x0), v3317, v3311(0x331e)

    Begin block 0x389fB0x3310
    prev=[0x3310], succ=[0x394eB0x389fB0x3310]
    =================================
    0x38a2S0x3310: v38a2V3310 = SLOAD v3317
    0x38a3S0x3310: v38a3V3310(0x0) = CONST 
    0x38a6S0x3310: SSTORE v3317, v38a3V3310(0x0)
    0x38a8S0x3310: v38a8V3310(0x0) = CONST 
    0x38aaS0x3310: MSTORE v38a8V3310(0x0), v3317
    0x38abS0x3310: v38abV3310(0x20) = CONST 
    0x38adS0x3310: v38adV3310(0x0) = CONST 
    0x38afS0x3310: v38afV3310 = SHA3 v38adV3310(0x0), v38abV3310(0x20)
    0x38b2S0x3310: v38b2V3310 = ADD v38afV3310, v38a2V3310
    0x38b4S0x3310: v38b4V3310(0x38bd) = CONST 
    0x38b9S0x3310: v38b9V3310(0x394e) = CONST 
    0x38bcS0x3310: JUMP v38b9V3310(0x394e)

    Begin block 0x394eB0x389fB0x3310
    prev=[0x389fB0x3310], succ=[0x394fB0x389fB0x3310]
    =================================

    Begin block 0x394fB0x389fB0x3310
    prev=[0x3958B0x389fB0x3310, 0x394eB0x389fB0x3310], succ=[0x3958B0x389fB0x3310, 0x459cB0x389fB0x3310]
    =================================
    0x394f_0x0S0x389fS0x3310: v394f_0V389fV3310 = PHI v38afV3310, v395eV389fV3310
    0x3952S0x389fS0x3310: v3952V389fV3310 = GT v38b2V3310, v394f_0V389fV3310
    0x3953S0x389fS0x3310: v3953V389fV3310 = ISZERO v3952V389fV3310
    0x3954S0x389fS0x3310: v3954V389fV3310(0x459c) = CONST 
    0x3957S0x389fS0x3310: JUMPI v3954V389fV3310(0x459c), v3953V389fV3310

    Begin block 0x3958B0x389fB0x3310
    prev=[0x394fB0x389fB0x3310], succ=[0x394fB0x389fB0x3310]
    =================================
    0x3958S0x389fS0x3310: v3958V389fV3310(0x0) = CONST 
    0x3958_0x0S0x389fS0x3310: v3958_0V389fV3310 = PHI v38afV3310, v395eV389fV3310
    0x395bS0x389fS0x3310: SSTORE v3958_0V389fV3310, v3958V389fV3310(0x0)
    0x395cS0x389fS0x3310: v395cV389fV3310(0x1) = CONST 
    0x395eS0x389fS0x3310: v395eV389fV3310 = ADD v395cV389fV3310(0x1), v3958_0V389fV3310
    0x395fS0x389fS0x3310: v395fV389fV3310(0x394f) = CONST 
    0x3962S0x389fS0x3310: JUMP v395fV389fV3310(0x394f)

    Begin block 0x459cB0x389fB0x3310
    prev=[0x394fB0x389fB0x3310], succ=[0x38bdB0x3310]
    =================================
    0x459fS0x389fS0x3310: JUMP v38b4V3310(0x38bd)

    Begin block 0x38bdB0x3310
    prev=[0x459cB0x389fB0x3310], succ=[0x331e]
    =================================
    0x38bfS0x3310: JUMP v3311(0x331e)

    Begin block 0x331e
    prev=[0x38bdB0x3310], succ=[0x3337, 0x3338]
    =================================
    0x331e_0x2: v331e_2 = PHI v3249(0x0), v3386
    0x331f: v331f(0x2) = CONST 
    0x3322: v3322 = ADD v32ff, v331f(0x2)
    0x3323: v3323(0x0) = CONST 
    0x3326: SSTORE v3322, v3323(0x0)
    0x3329: v3329(0xa) = CONST 
    0x332b: v332b(0x0) = CONST 
    0x3330: v3330 = MLOAD v2365
    0x3332: v3332 = LT v331e_2, v3330
    0x3333: v3333(0x3338) = CONST 
    0x3336: JUMPI v3333(0x3338), v3332

    Begin block 0x3337
    prev=[0x331e], succ=[]
    =================================
    0x3337: THROW 

    Begin block 0x3338
    prev=[0x331e], succ=[0x3377, 0x3378]
    =================================
    0x3338_0x0: v3338_0 = PHI v3249(0x0), v3386
    0x3338_0x4: v3338_4 = PHI v3249(0x0), v3386
    0x3339: v3339(0x20) = CONST 
    0x333d: v333d = MUL v3339(0x20), v3338_0
    0x3341: v3341 = ADD v333d, v2365
    0x3343: v3343 = ADD v3339(0x20), v3341
    0x3344: v3344 = MLOAD v3343
    0x3346: MSTORE v332b(0x0), v3344
    0x3348: v3348(0x20) = ADD v332b(0x0), v3339(0x20)
    0x334c: MSTORE v3348(0x20), v3329(0xa)
    0x334d: v334d(0x40) = CONST 
    0x334f: v334f(0x40) = ADD v334d(0x40), v332b(0x0)
    0x3350: v3350(0x0) = CONST 
    0x3354: v3354 = SHA3 v3350(0x0), v334f(0x40)
    0x3357: SSTORE v3354, v3350(0x0)
    0x3358: v3358(0x1) = CONST 
    0x335c: v335c = ADD v3358(0x1), v3354
    0x335e: v335e = SLOAD v335c
    0x335f: v335f(0x1) = CONST 
    0x3361: v3361(0x1) = CONST 
    0x3363: v3363(0xa0) = CONST 
    0x3365: v3365(0x10000000000000000000000000000000000000000) = SHL v3363(0xa0), v3361(0x1)
    0x3366: v3366(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3365(0x10000000000000000000000000000000000000000), v335f(0x1)
    0x3367: v3367(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3366(0xffffffffffffffffffffffffffffffffffffffff)
    0x3368: v3368 = AND v3367(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v335e
    0x336a: SSTORE v335c, v3368
    0x336c: v336c = MLOAD v321f
    0x3372: v3372 = LT v3338_4, v336c
    0x3373: v3373(0x3378) = CONST 
    0x3376: JUMPI v3373(0x3378), v3372

    Begin block 0x3377
    prev=[0x3338], succ=[]
    =================================
    0x3377: THROW 

    Begin block 0x3378
    prev=[0x3338], succ=[0x324b]
    =================================
    0x3378_0x0: v3378_0 = PHI v3249(0x0), v3386
    0x3378_0x3: v3378_3 = PHI v3249(0x0), v3386
    0x3379: v3379(0x20) = CONST 
    0x337d: v337d = MUL v3379(0x20), v3378_0
    0x3381: v3381 = ADD v337d, v321f
    0x3382: v3382 = ADD v3381, v3379(0x20)
    0x3383: MSTORE v3382, v3358(0x1)
    0x3384: v3384(0x1) = CONST 
    0x3386: v3386 = ADD v3384(0x1), v3378_3
    0x3387: v3387(0x324b) = CONST 
    0x338a: JUMP v3387(0x324b)

    Begin block 0x338b
    prev=[0x324b], succ=[0x33fa]
    =================================
    0x338d: v338d(0x0) = CONST 
    0x338f: v338f(0x1) = CONST 
    0x3391: v3391(0x1) = CONST 
    0x3393: v3393(0xa0) = CONST 
    0x3395: v3395(0x10000000000000000000000000000000000000000) = SHL v3393(0xa0), v3391(0x1)
    0x3396: v3396(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3395(0x10000000000000000000000000000000000000000), v338f(0x1)
    0x3397: v3397(0x0) = AND v3396(0xffffffffffffffffffffffffffffffffffffffff), v338d(0x0)
    0x3399: v3399(0x1) = CONST 
    0x339b: v339b(0x1) = CONST 
    0x339d: v339d(0xa0) = CONST 
    0x339f: v339f(0x10000000000000000000000000000000000000000) = SHL v339d(0xa0), v339b(0x1)
    0x33a0: v33a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v339f(0x10000000000000000000000000000000000000000), v3399(0x1)
    0x33a1: v33a1 = AND v33a0(0xffffffffffffffffffffffffffffffffffffffff), vc5d
    0x33a2: v33a2 = CALLER 
    0x33a3: v33a3(0x1) = CONST 
    0x33a5: v33a5(0x1) = CONST 
    0x33a7: v33a7(0xa0) = CONST 
    0x33a9: v33a9(0x10000000000000000000000000000000000000000) = SHL v33a7(0xa0), v33a5(0x1)
    0x33aa: v33aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v33a9(0x10000000000000000000000000000000000000000), v33a3(0x1)
    0x33ab: v33ab = AND v33aa(0xffffffffffffffffffffffffffffffffffffffff), v33a2
    0x33ac: v33ac(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x33cf: v33cf(0x40) = CONST 
    0x33d1: v33d1 = MLOAD v33cf(0x40)
    0x33d4: v33d4(0x20) = CONST 
    0x33d6: v33d6 = ADD v33d4(0x20), v33d1
    0x33d8: v33d8(0x20) = CONST 
    0x33da: v33da = ADD v33d8(0x20), v33d6
    0x33dd: v33dd(0x40) = SUB v33da, v33d1
    0x33df: MSTORE v33d1, v33dd(0x40)
    0x33e3: v33e3 = MLOAD v2365
    0x33e5: MSTORE v33da, v33e3
    0x33e6: v33e6(0x20) = CONST 
    0x33e8: v33e8 = ADD v33e6(0x20), v33da
    0x33ec: v33ec = MLOAD v2365
    0x33ee: v33ee(0x20) = CONST 
    0x33f0: v33f0 = ADD v33ee(0x20), v2365
    0x33f2: v33f2(0x20) = CONST 
    0x33f4: v33f4 = MUL v33f2(0x20), v33ec
    0x33f8: v33f8(0x0) = CONST 

    Begin block 0x33fa
    prev=[0x338b, 0x3403], succ=[0x3412, 0x3403]
    =================================
    0x33fa_0x0: v33fa_0 = PHI v33f8(0x0), v340d
    0x33fd: v33fd = LT v33fa_0, v33f4
    0x33fe: v33fe = ISZERO v33fd
    0x33ff: v33ff(0x3412) = CONST 
    0x3402: JUMPI v33ff(0x3412), v33fe

    Begin block 0x3412
    prev=[0x33fa], succ=[0x3439]
    =================================
    0x3419: v3419 = ADD v33f4, v33e8
    0x341c: v341c = SUB v3419, v33d1
    0x341e: MSTORE v33d6, v341c
    0x3422: v3422 = MLOAD v321f
    0x3424: MSTORE v3419, v3422
    0x3425: v3425(0x20) = CONST 
    0x3427: v3427 = ADD v3425(0x20), v3419
    0x342b: v342b = MLOAD v321f
    0x342d: v342d(0x20) = CONST 
    0x342f: v342f = ADD v342d(0x20), v321f
    0x3431: v3431(0x20) = CONST 
    0x3433: v3433 = MUL v3431(0x20), v342b
    0x3437: v3437(0x0) = CONST 

    Begin block 0x3439
    prev=[0x3412, 0x3442], succ=[0x3451, 0x3442]
    =================================
    0x3439_0x0: v3439_0 = PHI v3437(0x0), v344c
    0x343c: v343c = LT v3439_0, v3433
    0x343d: v343d = ISZERO v343c
    0x343e: v343e(0x3451) = CONST 
    0x3441: JUMPI v343e(0x3451), v343d

    Begin block 0x3451
    prev=[0x3439], succ=[0x2391]
    =================================
    0x3458: v3458 = ADD v3433, v3427
    0x345f: v345f(0x40) = CONST 
    0x3461: v3461 = MLOAD v345f(0x40)
    0x3464: v3464 = SUB v3458, v3461
    0x3466: LOG4 v3461, v3464, v33ac(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v33ab, v33a1, v3397(0x0)
    0x346a: JUMP v2355(0x2391)

    Begin block 0x2391
    prev=[0x3451], succ=[0x40e6]
    =================================
    0x2395: JUMP vc3d(0x40e6)

    Begin block 0x40e6
    prev=[0x2391], succ=[]
    =================================
    0x40e7: STOP 

    Begin block 0x3442
    prev=[0x3439], succ=[0x3439]
    =================================
    0x3442_0x0: v3442_0 = PHI v3437(0x0), v344c
    0x3444: v3444 = ADD v3442_0, v342f
    0x3445: v3445 = MLOAD v3444
    0x3448: v3448 = ADD v3442_0, v3427
    0x3449: MSTORE v3448, v3445
    0x344a: v344a(0x20) = CONST 
    0x344c: v344c = ADD v344a(0x20), v3442_0
    0x344d: v344d(0x3439) = CONST 
    0x3450: JUMP v344d(0x3439)

    Begin block 0x3403
    prev=[0x33fa], succ=[0x33fa]
    =================================
    0x3403_0x0: v3403_0 = PHI v33f8(0x0), v340d
    0x3405: v3405 = ADD v3403_0, v33f0
    0x3406: v3406 = MLOAD v3405
    0x3409: v3409 = ADD v3403_0, v33e8
    0x340a: MSTORE v3409, v3406
    0x340b: v340b(0x20) = CONST 
    0x340d: v340d = ADD v340b(0x20), v3403_0
    0x340e: v340e(0x33fa) = CONST 
    0x3411: JUMP v340e(0x33fa)

    Begin block 0x3236
    prev=[0x321b], succ=[0x3245]
    =================================
    0x3237: v3237(0x20) = CONST 
    0x3239: v3239 = ADD v3237(0x20), v321f
    0x323a: v323a(0x20) = CONST 
    0x323d: v323d = MUL v3205, v323a(0x20)
    0x323f: v323f = CALLDATASIZE 
    0x3241: CALLDATACOPY v3239, v323f, v323d
    0x3242: v3242 = ADD v323d, v3239

}

function starNFTOwner()() public {
    Begin block 0xcba
    prev=[], succ=[0x2396]
    =================================
    0xcbb: vcbb(0x4107) = CONST 
    0xcbe: vcbe(0x2396) = CONST 
    0xcc1: JUMP vcbe(0x2396)

    Begin block 0x2396
    prev=[0xcba], succ=[0x4107]
    =================================
    0x2397: v2397(0x3) = CONST 
    0x2399: v2399 = SLOAD v2397(0x3)
    0x239a: v239a(0x1) = CONST 
    0x239c: v239c(0x1) = CONST 
    0x239e: v239e(0xa0) = CONST 
    0x23a0: v23a0(0x10000000000000000000000000000000000000000) = SHL v239e(0xa0), v239c(0x1)
    0x23a1: v23a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23a0(0x10000000000000000000000000000000000000000), v239a(0x1)
    0x23a2: v23a2 = AND v23a1(0xffffffffffffffffffffffffffffffffffffffff), v2399
    0x23a4: JUMP vcbb(0x4107)

    Begin block 0x4107
    prev=[0x2396], succ=[]
    =================================
    0x4108: v4108(0x40) = CONST 
    0x410b: v410b = MLOAD v4108(0x40)
    0x410c: v410c(0x1) = CONST 
    0x410e: v410e(0x1) = CONST 
    0x4110: v4110(0xa0) = CONST 
    0x4112: v4112(0x10000000000000000000000000000000000000000) = SHL v4110(0xa0), v410e(0x1)
    0x4113: v4113(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4112(0x10000000000000000000000000000000000000000), v410c(0x1)
    0x4116: v4116 = AND v23a2, v4113(0xffffffffffffffffffffffffffffffffffffffff)
    0x4118: MSTORE v410b, v4116
    0x4119: v4119 = MLOAD v4108(0x40)
    0x411d: v411d(0x0) = SUB v410b, v4119
    0x411e: v411e(0x20) = CONST 
    0x4120: v4120(0x20) = ADD v411e(0x20), v411d(0x0)
    0x4122: RETURN v4119, v4120(0x20)

}

function starInfo(uint256)() public {
    Begin block 0xcc2
    prev=[], succ=[0xcd4, 0xcd8]
    =================================
    0xcc3: vcc3(0xcdf) = CONST 
    0xcc6: vcc6(0x4) = CONST 
    0xcc9: vcc9 = CALLDATASIZE 
    0xcca: vcca = SUB vcc9, vcc6(0x4)
    0xccb: vccb(0x20) = CONST 
    0xcce: vcce = LT vcca, vccb(0x20)
    0xccf: vccf = ISZERO vcce
    0xcd0: vcd0(0xcd8) = CONST 
    0xcd3: JUMPI vcd0(0xcd8), vccf

    Begin block 0xcd4
    prev=[0xcc2], succ=[]
    =================================
    0xcd4: vcd4(0x0) = CONST 
    0xcd7: REVERT vcd4(0x0), vcd4(0x0)

    Begin block 0xcd8
    prev=[0xcc2], succ=[0x23a5]
    =================================
    0xcda: vcda = CALLDATALOAD vcc6(0x4)
    0xcdb: vcdb(0x23a5) = CONST 
    0xcde: JUMP vcdb(0x23a5)

    Begin block 0x23a5
    prev=[0xcd8], succ=[0xcdf]
    =================================
    0x23a6: v23a6(0x0) = CONST 
    0x23aa: MSTORE v23a6(0x0), vcda
    0x23ab: v23ab(0xa) = CONST 
    0x23ad: v23ad(0x20) = CONST 
    0x23af: MSTORE v23ad(0x20), v23ab(0xa)
    0x23b0: v23b0(0x40) = CONST 
    0x23b3: v23b3 = SHA3 v23a6(0x0), v23b0(0x40)
    0x23b5: v23b5 = SLOAD v23b3
    0x23b6: v23b6(0x1) = CONST 
    0x23ba: v23ba = ADD v23b3, v23b6(0x1)
    0x23bb: v23bb = SLOAD v23ba
    0x23bc: v23bc(0x1) = CONST 
    0x23be: v23be(0x1) = CONST 
    0x23c0: v23c0(0x80) = CONST 
    0x23c2: v23c2(0x100000000000000000000000000000000) = SHL v23c0(0x80), v23be(0x1)
    0x23c3: v23c3(0xffffffffffffffffffffffffffffffff) = SUB v23c2(0x100000000000000000000000000000000), v23bc(0x1)
    0x23c4: v23c4(0x1) = CONST 
    0x23c6: v23c6(0x80) = CONST 
    0x23c8: v23c8(0x100000000000000000000000000000000) = SHL v23c6(0x80), v23c4(0x1)
    0x23ca: v23ca = DIV v23b5, v23c8(0x100000000000000000000000000000000)
    0x23cc: v23cc = AND v23c3(0xffffffffffffffffffffffffffffffff), v23ca
    0x23cf: v23cf = AND v23b5, v23c3(0xffffffffffffffffffffffffffffffff)
    0x23d1: v23d1(0x1) = CONST 
    0x23d3: v23d3(0x1) = CONST 
    0x23d5: v23d5(0xa0) = CONST 
    0x23d7: v23d7(0x10000000000000000000000000000000000000000) = SHL v23d5(0xa0), v23d3(0x1)
    0x23d8: v23d8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23d7(0x10000000000000000000000000000000000000000), v23d1(0x1)
    0x23db: v23db = AND v23bb, v23d8(0xffffffffffffffffffffffffffffffffffffffff)
    0x23dd: JUMP vcc3(0xcdf)

    Begin block 0xcdf
    prev=[0x23a5], succ=[]
    =================================
    0xce0: vce0(0x40) = CONST 
    0xce3: vce3 = MLOAD vce0(0x40)
    0xce4: vce4(0x1) = CONST 
    0xce6: vce6(0x1) = CONST 
    0xce8: vce8(0x80) = CONST 
    0xcea: vcea(0x100000000000000000000000000000000) = SHL vce8(0x80), vce6(0x1)
    0xceb: vceb(0xffffffffffffffffffffffffffffffff) = SUB vcea(0x100000000000000000000000000000000), vce4(0x1)
    0xcee: vcee = AND vceb(0xffffffffffffffffffffffffffffffff), v23cc
    0xcf0: MSTORE vce3, vcee
    0xcf4: vcf4 = AND vceb(0xffffffffffffffffffffffffffffffff), v23cf
    0xcf5: vcf5(0x20) = CONST 
    0xcf8: vcf8 = ADD vce3, vcf5(0x20)
    0xcf9: MSTORE vcf8, vcf4
    0xcfa: vcfa(0x1) = CONST 
    0xcfc: vcfc(0x1) = CONST 
    0xcfe: vcfe(0xa0) = CONST 
    0xd00: vd00(0x10000000000000000000000000000000000000000) = SHL vcfe(0xa0), vcfc(0x1)
    0xd01: vd01(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd00(0x10000000000000000000000000000000000000000), vcfa(0x1)
    0xd02: vd02 = AND vd01(0xffffffffffffffffffffffffffffffffffffffff), v23db
    0xd05: vd05 = ADD vce0(0x40), vce3
    0xd06: MSTORE vd05, vd02
    0xd08: vd08 = MLOAD vce0(0x40)
    0xd0c: vd0c(0x0) = SUB vce3, vd08
    0xd0d: vd0d(0x60) = CONST 
    0xd0f: vd0f(0x60) = ADD vd0d(0x60), vd0c(0x0)
    0xd11: RETURN vd08, vd0f(0x60)

}

function burnSuper(address,uint256)() public {
    Begin block 0xd12
    prev=[], succ=[0xd24, 0xd28]
    =================================
    0xd13: vd13(0x4142) = CONST 
    0xd16: vd16(0x4) = CONST 
    0xd19: vd19 = CALLDATASIZE 
    0xd1a: vd1a = SUB vd19, vd16(0x4)
    0xd1b: vd1b(0x40) = CONST 
    0xd1e: vd1e = LT vd1a, vd1b(0x40)
    0xd1f: vd1f = ISZERO vd1e
    0xd20: vd20(0xd28) = CONST 
    0xd23: JUMPI vd20(0xd28), vd1f

    Begin block 0xd24
    prev=[0xd12], succ=[]
    =================================
    0xd24: vd24(0x0) = CONST 
    0xd27: REVERT vd24(0x0), vd24(0x0)

    Begin block 0xd28
    prev=[0xd12], succ=[0x23de]
    =================================
    0xd2a: vd2a(0x1) = CONST 
    0xd2c: vd2c(0x1) = CONST 
    0xd2e: vd2e(0xa0) = CONST 
    0xd30: vd30(0x10000000000000000000000000000000000000000) = SHL vd2e(0xa0), vd2c(0x1)
    0xd31: vd31(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd30(0x10000000000000000000000000000000000000000), vd2a(0x1)
    0xd33: vd33 = CALLDATALOAD vd16(0x4)
    0xd34: vd34 = AND vd33, vd31(0xffffffffffffffffffffffffffffffffffffffff)
    0xd36: vd36(0x20) = CONST 
    0xd38: vd38(0x24) = ADD vd36(0x20), vd16(0x4)
    0xd39: vd39 = CALLDATALOAD vd38(0x24)
    0xd3a: vd3a(0x23de) = CONST 
    0xd3d: JUMP vd3a(0x23de)

    Begin block 0x23de
    prev=[0xd28], succ=[0x23f6, 0x2433]
    =================================
    0x23df: v23df = CALLER 
    0x23e0: v23e0(0x0) = CONST 
    0x23e4: MSTORE v23e0(0x0), v23df
    0x23e5: v23e5(0x5) = CONST 
    0x23e7: v23e7(0x20) = CONST 
    0x23e9: MSTORE v23e7(0x20), v23e5(0x5)
    0x23ea: v23ea(0x40) = CONST 
    0x23ed: v23ed = SHA3 v23e0(0x0), v23ea(0x40)
    0x23ee: v23ee = SLOAD v23ed
    0x23ef: v23ef(0xff) = CONST 
    0x23f1: v23f1 = AND v23ef(0xff), v23ee
    0x23f2: v23f2(0x2433) = CONST 
    0x23f5: JUMPI v23f2(0x2433), v23f1

    Begin block 0x23f6
    prev=[0x23de], succ=[]
    =================================
    0x23f6: v23f6(0x40) = CONST 
    0x23f9: v23f9 = MLOAD v23f6(0x40)
    0x23fa: v23fa(0x461bcd) = CONST 
    0x23fe: v23fe(0xe5) = CONST 
    0x2400: v2400(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v23fe(0xe5), v23fa(0x461bcd)
    0x2402: MSTORE v23f9, v2400(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2403: v2403(0x20) = CONST 
    0x2405: v2405(0x4) = CONST 
    0x2408: v2408 = ADD v23f9, v2405(0x4)
    0x2409: MSTORE v2408, v2403(0x20)
    0x240a: v240a(0xe) = CONST 
    0x240c: v240c(0x24) = CONST 
    0x240f: v240f = ADD v23f9, v240c(0x24)
    0x2410: MSTORE v240f, v240a(0xe)
    0x2411: v2411(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x2420: v2420(0x91) = CONST 
    0x2422: v2422(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v2420(0x91), v2411(0x36bab9ba1031329036b4b73a32b9)
    0x2423: v2423(0x44) = CONST 
    0x2426: v2426 = ADD v23f9, v2423(0x44)
    0x2427: MSTORE v2426, v2422(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x2429: v2429 = MLOAD v23f6(0x40)
    0x242d: v242d(0x0) = SUB v23f9, v2429
    0x242e: v242e(0x64) = CONST 
    0x2430: v2430(0x64) = ADD v242e(0x64), v242d(0x0)
    0x2432: REVERT v2429, v2430(0x64)

    Begin block 0x2433
    prev=[0x23de], succ=[0x243d]
    =================================
    0x2434: v2434(0x243d) = CONST 
    0x2439: v2439(0x2497) = CONST 
    0x243c: v243c_0 = CALLPRIVATE v2439(0x2497), vd39, vd34, v2434(0x243d)

    Begin block 0x243d
    prev=[0x2433], succ=[0x2442, 0x248e]
    =================================
    0x243e: v243e(0x248e) = CONST 
    0x2441: JUMPI v243e(0x248e), v243c_0

    Begin block 0x2442
    prev=[0x243d], succ=[]
    =================================
    0x2442: v2442(0x40) = CONST 
    0x2445: v2445 = MLOAD v2442(0x40)
    0x2446: v2446(0x461bcd) = CONST 
    0x244a: v244a(0xe5) = CONST 
    0x244c: v244c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v244a(0xe5), v2446(0x461bcd)
    0x244e: MSTORE v2445, v244c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x244f: v244f(0x20) = CONST 
    0x2451: v2451(0x4) = CONST 
    0x2454: v2454 = ADD v2445, v2451(0x4)
    0x2455: MSTORE v2454, v244f(0x20)
    0x2456: v2456(0x1f) = CONST 
    0x2458: v2458(0x24) = CONST 
    0x245b: v245b = ADD v2445, v2458(0x24)
    0x245c: MSTORE v245b, v2456(0x1f)
    0x245d: v245d(0x4d757374206265206f776e6572206f662074686973205375706572204e465400) = CONST 
    0x247e: v247e(0x44) = CONST 
    0x2481: v2481 = ADD v2445, v247e(0x44)
    0x2482: MSTORE v2481, v245d(0x4d757374206265206f776e6572206f662074686973205375706572204e465400)
    0x2484: v2484 = MLOAD v2442(0x40)
    0x2488: v2488(0x0) = SUB v2445, v2484
    0x2489: v2489(0x64) = CONST 
    0x248b: v248b(0x64) = ADD v2489(0x64), v2488(0x0)
    0x248d: REVERT v2484, v248b(0x64)

    Begin block 0x248e
    prev=[0x243d], succ=[0x346b]
    =================================
    0x248f: v248f(0x43b7) = CONST 
    0x2493: v2493(0x346b) = CONST 
    0x2496: JUMP v2493(0x346b)

    Begin block 0x346b
    prev=[0x248e], succ=[0x389fB0x346b]
    =================================
    0x346c: v346c(0x0) = CONST 
    0x3470: MSTORE v346c(0x0), vd39
    0x3471: v3471(0xc) = CONST 
    0x3473: v3473(0x20) = CONST 
    0x3475: MSTORE v3473(0x20), v3471(0xc)
    0x3476: v3476(0x40) = CONST 
    0x3479: v3479 = SHA3 v346c(0x0), v3476(0x40)
    0x347a: v347a(0x3482) = CONST 
    0x347e: v347e(0x389f) = CONST 
    0x3481: JUMP v347e(0x389f), v346c(0x0), v3479, v347a(0x3482)

    Begin block 0x389fB0x346b
    prev=[0x346b], succ=[0x394eB0x389fB0x346b]
    =================================
    0x38a2S0x346b: v38a2V346b = SLOAD v3479
    0x38a3S0x346b: v38a3V346b(0x0) = CONST 
    0x38a6S0x346b: SSTORE v3479, v38a3V346b(0x0)
    0x38a8S0x346b: v38a8V346b(0x0) = CONST 
    0x38aaS0x346b: MSTORE v38a8V346b(0x0), v3479
    0x38abS0x346b: v38abV346b(0x20) = CONST 
    0x38adS0x346b: v38adV346b(0x0) = CONST 
    0x38afS0x346b: v38afV346b = SHA3 v38adV346b(0x0), v38abV346b(0x20)
    0x38b2S0x346b: v38b2V346b = ADD v38afV346b, v38a2V346b
    0x38b4S0x346b: v38b4V346b(0x38bd) = CONST 
    0x38b9S0x346b: v38b9V346b(0x394e) = CONST 
    0x38bcS0x346b: JUMP v38b9V346b(0x394e)

    Begin block 0x394eB0x389fB0x346b
    prev=[0x389fB0x346b], succ=[0x394fB0x389fB0x346b]
    =================================

    Begin block 0x394fB0x389fB0x346b
    prev=[0x3958B0x389fB0x346b, 0x394eB0x389fB0x346b], succ=[0x3958B0x389fB0x346b, 0x459cB0x389fB0x346b]
    =================================
    0x394f_0x0S0x389fS0x346b: v394f_0V389fV346b = PHI v38afV346b, v395eV389fV346b
    0x3952S0x389fS0x346b: v3952V389fV346b = GT v38b2V346b, v394f_0V389fV346b
    0x3953S0x389fS0x346b: v3953V389fV346b = ISZERO v3952V389fV346b
    0x3954S0x389fS0x346b: v3954V389fV346b(0x459c) = CONST 
    0x3957S0x389fS0x346b: JUMPI v3954V389fV346b(0x459c), v3953V389fV346b

    Begin block 0x3958B0x389fB0x346b
    prev=[0x394fB0x389fB0x346b], succ=[0x394fB0x389fB0x346b]
    =================================
    0x3958S0x389fS0x346b: v3958V389fV346b(0x0) = CONST 
    0x3958_0x0S0x389fS0x346b: v3958_0V389fV346b = PHI v38afV346b, v395eV389fV346b
    0x395bS0x389fS0x346b: SSTORE v3958_0V389fV346b, v3958V389fV346b(0x0)
    0x395cS0x389fS0x346b: v395cV389fV346b(0x1) = CONST 
    0x395eS0x389fS0x346b: v395eV389fV346b = ADD v395cV389fV346b(0x1), v3958_0V389fV346b
    0x395fS0x389fS0x346b: v395fV389fV346b(0x394f) = CONST 
    0x3962S0x389fS0x346b: JUMP v395fV389fV346b(0x394f)

    Begin block 0x459cB0x389fB0x346b
    prev=[0x394fB0x389fB0x346b], succ=[0x38bdB0x346b]
    =================================
    0x459fS0x389fS0x346b: JUMP v38b4V346b(0x38bd)

    Begin block 0x38bdB0x346b
    prev=[0x459cB0x389fB0x346b], succ=[0x3482]
    =================================
    0x38bfS0x346b: JUMP v347a(0x3482)

    Begin block 0x3482
    prev=[0x38bdB0x346b], succ=[0x389fB0x3482]
    =================================
    0x3483: v3483(0x0) = CONST 
    0x3487: MSTORE v3483(0x0), vd39
    0x3488: v3488(0xc) = CONST 
    0x348a: v348a(0x20) = CONST 
    0x348c: MSTORE v348a(0x20), v3488(0xc)
    0x348d: v348d(0x40) = CONST 
    0x3490: v3490 = SHA3 v3483(0x0), v348d(0x40)
    0x3491: v3491(0x349f) = CONST 
    0x3495: v3495(0x1) = CONST 
    0x3499: v3499 = ADD v3490, v3495(0x1)
    0x349b: v349b(0x389f) = CONST 
    0x349e: JUMP v349b(0x389f), v3483(0x0), v3499, v3491(0x349f)

    Begin block 0x389fB0x3482
    prev=[0x3482], succ=[0x394eB0x389fB0x3482]
    =================================
    0x38a2S0x3482: v38a2V3482 = SLOAD v3499
    0x38a3S0x3482: v38a3V3482(0x0) = CONST 
    0x38a6S0x3482: SSTORE v3499, v38a3V3482(0x0)
    0x38a8S0x3482: v38a8V3482(0x0) = CONST 
    0x38aaS0x3482: MSTORE v38a8V3482(0x0), v3499
    0x38abS0x3482: v38abV3482(0x20) = CONST 
    0x38adS0x3482: v38adV3482(0x0) = CONST 
    0x38afS0x3482: v38afV3482 = SHA3 v38adV3482(0x0), v38abV3482(0x20)
    0x38b2S0x3482: v38b2V3482 = ADD v38afV3482, v38a2V3482
    0x38b4S0x3482: v38b4V3482(0x38bd) = CONST 
    0x38b9S0x3482: v38b9V3482(0x394e) = CONST 
    0x38bcS0x3482: JUMP v38b9V3482(0x394e)

    Begin block 0x394eB0x389fB0x3482
    prev=[0x389fB0x3482], succ=[0x394fB0x389fB0x3482]
    =================================

    Begin block 0x394fB0x389fB0x3482
    prev=[0x3958B0x389fB0x3482, 0x394eB0x389fB0x3482], succ=[0x3958B0x389fB0x3482, 0x459cB0x389fB0x3482]
    =================================
    0x394f_0x0S0x389fS0x3482: v394f_0V389fV3482 = PHI v38afV3482, v395eV389fV3482
    0x3952S0x389fS0x3482: v3952V389fV3482 = GT v38b2V3482, v394f_0V389fV3482
    0x3953S0x389fS0x3482: v3953V389fV3482 = ISZERO v3952V389fV3482
    0x3954S0x389fS0x3482: v3954V389fV3482(0x459c) = CONST 
    0x3957S0x389fS0x3482: JUMPI v3954V389fV3482(0x459c), v3953V389fV3482

    Begin block 0x3958B0x389fB0x3482
    prev=[0x394fB0x389fB0x3482], succ=[0x394fB0x389fB0x3482]
    =================================
    0x3958S0x389fS0x3482: v3958V389fV3482(0x0) = CONST 
    0x3958_0x0S0x389fS0x3482: v3958_0V389fV3482 = PHI v38afV3482, v395eV389fV3482
    0x395bS0x389fS0x3482: SSTORE v3958_0V389fV3482, v3958V389fV3482(0x0)
    0x395cS0x389fS0x3482: v395cV389fV3482(0x1) = CONST 
    0x395eS0x389fS0x3482: v395eV389fV3482 = ADD v395cV389fV3482(0x1), v3958_0V389fV3482
    0x395fS0x389fS0x3482: v395fV389fV3482(0x394f) = CONST 
    0x3962S0x389fS0x3482: JUMP v395fV389fV3482(0x394f)

    Begin block 0x459cB0x389fB0x3482
    prev=[0x394fB0x389fB0x3482], succ=[0x38bdB0x3482]
    =================================
    0x459fS0x389fS0x3482: JUMP v38b4V3482(0x38bd)

    Begin block 0x38bdB0x3482
    prev=[0x459cB0x389fB0x3482], succ=[0x349f]
    =================================
    0x38bfS0x3482: JUMP v3491(0x349f)

    Begin block 0x349f
    prev=[0x38bdB0x3482], succ=[0x389fB0x349f]
    =================================
    0x34a0: v34a0(0x0) = CONST 
    0x34a4: MSTORE v34a0(0x0), vd39
    0x34a5: v34a5(0xc) = CONST 
    0x34a7: v34a7(0x20) = CONST 
    0x34a9: MSTORE v34a7(0x20), v34a5(0xc)
    0x34aa: v34aa(0x40) = CONST 
    0x34ad: v34ad = SHA3 v34a0(0x0), v34aa(0x40)
    0x34af: v34af(0x34b8) = CONST 
    0x34b4: v34b4(0x389f) = CONST 
    0x34b7: JUMP v34b4(0x389f), v34a0(0x0), v34ad, v34af(0x34b8)

    Begin block 0x389fB0x349f
    prev=[0x349f], succ=[0x394eB0x389fB0x349f]
    =================================
    0x38a2S0x349f: v38a2V349f = SLOAD v34ad
    0x38a3S0x349f: v38a3V349f(0x0) = CONST 
    0x38a6S0x349f: SSTORE v34ad, v38a3V349f(0x0)
    0x38a8S0x349f: v38a8V349f(0x0) = CONST 
    0x38aaS0x349f: MSTORE v38a8V349f(0x0), v34ad
    0x38abS0x349f: v38abV349f(0x20) = CONST 
    0x38adS0x349f: v38adV349f(0x0) = CONST 
    0x38afS0x349f: v38afV349f = SHA3 v38adV349f(0x0), v38abV349f(0x20)
    0x38b2S0x349f: v38b2V349f = ADD v38afV349f, v38a2V349f
    0x38b4S0x349f: v38b4V349f(0x38bd) = CONST 
    0x38b9S0x349f: v38b9V349f(0x394e) = CONST 
    0x38bcS0x349f: JUMP v38b9V349f(0x394e)

    Begin block 0x394eB0x389fB0x349f
    prev=[0x389fB0x349f], succ=[0x394fB0x389fB0x349f]
    =================================

    Begin block 0x394fB0x389fB0x349f
    prev=[0x3958B0x389fB0x349f, 0x394eB0x389fB0x349f], succ=[0x3958B0x389fB0x349f, 0x459cB0x389fB0x349f]
    =================================
    0x394f_0x0S0x389fS0x349f: v394f_0V389fV349f = PHI v38afV349f, v395eV389fV349f
    0x3952S0x389fS0x349f: v3952V389fV349f = GT v38b2V349f, v394f_0V389fV349f
    0x3953S0x389fS0x349f: v3953V389fV349f = ISZERO v3952V389fV349f
    0x3954S0x389fS0x349f: v3954V389fV349f(0x459c) = CONST 
    0x3957S0x389fS0x349f: JUMPI v3954V389fV349f(0x459c), v3953V389fV349f

    Begin block 0x3958B0x389fB0x349f
    prev=[0x394fB0x389fB0x349f], succ=[0x394fB0x389fB0x349f]
    =================================
    0x3958S0x389fS0x349f: v3958V389fV349f(0x0) = CONST 
    0x3958_0x0S0x389fS0x349f: v3958_0V389fV349f = PHI v38afV349f, v395eV389fV349f
    0x395bS0x389fS0x349f: SSTORE v3958_0V389fV349f, v3958V389fV349f(0x0)
    0x395cS0x389fS0x349f: v395cV389fV349f(0x1) = CONST 
    0x395eS0x389fS0x349f: v395eV389fV349f = ADD v395cV389fV349f(0x1), v3958_0V389fV349f
    0x395fS0x389fS0x349f: v395fV389fV349f(0x394f) = CONST 
    0x3962S0x389fS0x349f: JUMP v395fV389fV349f(0x394f)

    Begin block 0x459cB0x389fB0x349f
    prev=[0x394fB0x389fB0x349f], succ=[0x38bdB0x349f]
    =================================
    0x459fS0x389fS0x349f: JUMP v38b4V349f(0x38bd)

    Begin block 0x38bdB0x349f
    prev=[0x459cB0x389fB0x349f], succ=[0x34b8]
    =================================
    0x38bfS0x349f: JUMP v34af(0x34b8)

    Begin block 0x34b8
    prev=[0x38bdB0x349f], succ=[0x389fB0x34b8]
    =================================
    0x34b9: v34b9(0x34c6) = CONST 
    0x34bc: v34bc(0x1) = CONST 
    0x34bf: v34bf = ADD v34ad, v34bc(0x1)
    0x34c0: v34c0(0x0) = CONST 
    0x34c2: v34c2(0x389f) = CONST 
    0x34c5: JUMP v34c2(0x389f), v34c0(0x0), v34bf, v34b9(0x34c6)

    Begin block 0x389fB0x34b8
    prev=[0x34b8], succ=[0x394eB0x389fB0x34b8]
    =================================
    0x38a2S0x34b8: v38a2V34b8 = SLOAD v34bf
    0x38a3S0x34b8: v38a3V34b8(0x0) = CONST 
    0x38a6S0x34b8: SSTORE v34bf, v38a3V34b8(0x0)
    0x38a8S0x34b8: v38a8V34b8(0x0) = CONST 
    0x38aaS0x34b8: MSTORE v38a8V34b8(0x0), v34bf
    0x38abS0x34b8: v38abV34b8(0x20) = CONST 
    0x38adS0x34b8: v38adV34b8(0x0) = CONST 
    0x38afS0x34b8: v38afV34b8 = SHA3 v38adV34b8(0x0), v38abV34b8(0x20)
    0x38b2S0x34b8: v38b2V34b8 = ADD v38afV34b8, v38a2V34b8
    0x38b4S0x34b8: v38b4V34b8(0x38bd) = CONST 
    0x38b9S0x34b8: v38b9V34b8(0x394e) = CONST 
    0x38bcS0x34b8: JUMP v38b9V34b8(0x394e)

    Begin block 0x394eB0x389fB0x34b8
    prev=[0x389fB0x34b8], succ=[0x394fB0x389fB0x34b8]
    =================================

    Begin block 0x394fB0x389fB0x34b8
    prev=[0x3958B0x389fB0x34b8, 0x394eB0x389fB0x34b8], succ=[0x3958B0x389fB0x34b8, 0x459cB0x389fB0x34b8]
    =================================
    0x394f_0x0S0x389fS0x34b8: v394f_0V389fV34b8 = PHI v38afV34b8, v395eV389fV34b8
    0x3952S0x389fS0x34b8: v3952V389fV34b8 = GT v38b2V34b8, v394f_0V389fV34b8
    0x3953S0x389fS0x34b8: v3953V389fV34b8 = ISZERO v3952V389fV34b8
    0x3954S0x389fS0x34b8: v3954V389fV34b8(0x459c) = CONST 
    0x3957S0x389fS0x34b8: JUMPI v3954V389fV34b8(0x459c), v3953V389fV34b8

    Begin block 0x3958B0x389fB0x34b8
    prev=[0x394fB0x389fB0x34b8], succ=[0x394fB0x389fB0x34b8]
    =================================
    0x3958S0x389fS0x34b8: v3958V389fV34b8(0x0) = CONST 
    0x3958_0x0S0x389fS0x34b8: v3958_0V389fV34b8 = PHI v38afV34b8, v395eV389fV34b8
    0x395bS0x389fS0x34b8: SSTORE v3958_0V389fV34b8, v3958V389fV34b8(0x0)
    0x395cS0x389fS0x34b8: v395cV389fV34b8(0x1) = CONST 
    0x395eS0x389fS0x34b8: v395eV389fV34b8 = ADD v395cV389fV34b8(0x1), v3958_0V389fV34b8
    0x395fS0x389fS0x34b8: v395fV389fV34b8(0x394f) = CONST 
    0x3962S0x389fS0x34b8: JUMP v395fV389fV34b8(0x394f)

    Begin block 0x459cB0x389fB0x34b8
    prev=[0x394fB0x389fB0x34b8], succ=[0x38bdB0x34b8]
    =================================
    0x459fS0x389fS0x34b8: JUMP v38b4V34b8(0x38bd)

    Begin block 0x38bdB0x34b8
    prev=[0x459cB0x389fB0x34b8], succ=[0x34c6]
    =================================
    0x38bfS0x34b8: JUMP v34b9(0x34c6)

    Begin block 0x34c6
    prev=[0x38bdB0x34b8], succ=[0x43b7]
    =================================
    0x34c8: v34c8(0x0) = CONST 
    0x34ca: v34ca(0x2) = CONST 
    0x34cf: v34cf = ADD v34ca(0x2), v34ad
    0x34d2: SSTORE v34cf, v34c8(0x0)
    0x34d3: v34d3(0x40) = CONST 
    0x34d5: v34d5 = MLOAD v34d3(0x40)
    0x34d8: v34d8(0x4b6e5320f0df4b001291b8e1e2661f0aea72baa9c69260aaf5475b470254deff) = CONST 
    0x34fa: LOG2 v34d5, v34c8(0x0), v34d8(0x4b6e5320f0df4b001291b8e1e2661f0aea72baa9c69260aaf5475b470254deff), vd39
    0x34fc: JUMP v248f(0x43b7)

    Begin block 0x43b7
    prev=[0x34c6], succ=[0x4142]
    =================================
    0x43ba: JUMP vd13(0x4142)

    Begin block 0x4142
    prev=[0x43b7], succ=[]
    =================================
    0x4143: STOP 

}

function isOwnerOf(address,uint256)() public {
    Begin block 0xd3e
    prev=[], succ=[0xd50, 0xd54]
    =================================
    0xd3f: vd3f(0x4163) = CONST 
    0xd42: vd42(0x4) = CONST 
    0xd45: vd45 = CALLDATASIZE 
    0xd46: vd46 = SUB vd45, vd42(0x4)
    0xd47: vd47(0x40) = CONST 
    0xd4a: vd4a = LT vd46, vd47(0x40)
    0xd4b: vd4b = ISZERO vd4a
    0xd4c: vd4c(0xd54) = CONST 
    0xd4f: JUMPI vd4c(0xd54), vd4b

    Begin block 0xd50
    prev=[0xd3e], succ=[]
    =================================
    0xd50: vd50(0x0) = CONST 
    0xd53: REVERT vd50(0x0), vd50(0x0)

    Begin block 0xd54
    prev=[0xd3e], succ=[0x24970xd3e]
    =================================
    0xd56: vd56(0x1) = CONST 
    0xd58: vd58(0x1) = CONST 
    0xd5a: vd5a(0xa0) = CONST 
    0xd5c: vd5c(0x10000000000000000000000000000000000000000) = SHL vd5a(0xa0), vd58(0x1)
    0xd5d: vd5d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd5c(0x10000000000000000000000000000000000000000), vd56(0x1)
    0xd5f: vd5f = CALLDATALOAD vd42(0x4)
    0xd60: vd60 = AND vd5f, vd5d(0xffffffffffffffffffffffffffffffffffffffff)
    0xd62: vd62(0x20) = CONST 
    0xd64: vd64(0x24) = ADD vd62(0x20), vd42(0x4)
    0xd65: vd65 = CALLDATALOAD vd64(0x24)
    0xd66: vd66(0x2497) = CONST 
    0xd69: JUMP vd66(0x2497)

    Begin block 0x24970xd3e
    prev=[0xd54], succ=[0x24af0xd3e, 0x24a80xd3e]
    =================================
    0x24980xd3e: vd3e2498(0x0) = CONST 
    0x249a0xd3e: vd3e249a(0x1) = CONST 
    0x249c0xd3e: vd3e249c(0x1) = CONST 
    0x249e0xd3e: vd3e249e(0xa0) = CONST 
    0x24a00xd3e: vd3e24a0(0x10000000000000000000000000000000000000000) = SHL vd3e249e(0xa0), vd3e249c(0x1)
    0x24a10xd3e: vd3e24a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd3e24a0(0x10000000000000000000000000000000000000000), vd3e249a(0x1)
    0x24a30xd3e: vd3e24a3 = AND vd60, vd3e24a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x24a40xd3e: vd3e24a4(0x24af) = CONST 
    0x24a70xd3e: JUMPI vd3e24a4(0x24af), vd3e24a3

    Begin block 0x24af0xd3e
    prev=[0x24970xd3e], succ=[0x43ff0xd3e]
    =================================
    0x24b10xd3e: vd3e24b1(0x0) = CONST 
    0x24b50xd3e: MSTORE vd3e24b1(0x0), vd65
    0x24b60xd3e: vd3e24b6(0x8) = CONST 
    0x24b80xd3e: vd3e24b8(0x20) = CONST 
    0x24ba0xd3e: MSTORE vd3e24b8(0x20), vd3e24b6(0x8)
    0x24bb0xd3e: vd3e24bb(0x40) = CONST 
    0x24be0xd3e: vd3e24be = SHA3 vd3e24b1(0x0), vd3e24bb(0x40)
    0x24bf0xd3e: vd3e24bf = SLOAD vd3e24be
    0x24c00xd3e: vd3e24c0(0x1) = CONST 
    0x24c20xd3e: vd3e24c2(0x1) = CONST 
    0x24c40xd3e: vd3e24c4(0xa0) = CONST 
    0x24c60xd3e: vd3e24c6(0x10000000000000000000000000000000000000000) = SHL vd3e24c4(0xa0), vd3e24c2(0x1)
    0x24c70xd3e: vd3e24c7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd3e24c6(0x10000000000000000000000000000000000000000), vd3e24c0(0x1)
    0x24ca0xd3e: vd3e24ca = AND vd3e24c7(0xffffffffffffffffffffffffffffffffffffffff), vd60
    0x24cc0xd3e: vd3e24cc = AND vd3e24bf, vd3e24c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x24cd0xd3e: vd3e24cd = EQ vd3e24cc, vd3e24ca
    0x24ce0xd3e: vd3e24ce(0x43ff) = CONST 
    0x24d10xd3e: JUMP vd3e24ce(0x43ff)

    Begin block 0x43ff0xd3e
    prev=[0x24af0xd3e], succ=[0x4163]
    =================================
    0x44040xd3e: JUMP vd3f(0x4163)

    Begin block 0x4163
    prev=[0x43da0xd3e, 0x43ff0xd3e], succ=[]
    =================================
    0x4163_0x0: v4163_0 = PHI vd3e24cd, vd3e24a9(0x0)
    0x4164: v4164(0x40) = CONST 
    0x4167: v4167 = MLOAD v4164(0x40)
    0x4169: v4169 = ISZERO v4163_0
    0x416a: v416a = ISZERO v4169
    0x416c: MSTORE v4167, v416a
    0x416d: v416d = MLOAD v4164(0x40)
    0x4171: v4171(0x0) = SUB v4167, v416d
    0x4172: v4172(0x20) = CONST 
    0x4174: v4174(0x20) = ADD v4172(0x20), v4171(0x0)
    0x4176: RETURN v416d, v4174(0x20)

    Begin block 0x24a80xd3e
    prev=[0x24970xd3e], succ=[0x43da0xd3e]
    =================================
    0x24a90xd3e: vd3e24a9(0x0) = CONST 
    0x24ab0xd3e: vd3e24ab(0x43da) = CONST 
    0x24ae0xd3e: JUMP vd3e24ab(0x43da)

    Begin block 0x43da0xd3e
    prev=[0x24a80xd3e], succ=[0x4163]
    =================================
    0x43df0xd3e: JUMP vd3f(0x4163)

}

function isApprovedForAll(address,address)() public {
    Begin block 0xd6a
    prev=[], succ=[0xd7c, 0xd80]
    =================================
    0xd6b: vd6b(0x4196) = CONST 
    0xd6e: vd6e(0x4) = CONST 
    0xd71: vd71 = CALLDATASIZE 
    0xd72: vd72 = SUB vd71, vd6e(0x4)
    0xd73: vd73(0x40) = CONST 
    0xd76: vd76 = LT vd72, vd73(0x40)
    0xd77: vd77 = ISZERO vd76
    0xd78: vd78(0xd80) = CONST 
    0xd7b: JUMPI vd78(0xd80), vd77

    Begin block 0xd7c
    prev=[0xd6a], succ=[]
    =================================
    0xd7c: vd7c(0x0) = CONST 
    0xd7f: REVERT vd7c(0x0), vd7c(0x0)

    Begin block 0xd80
    prev=[0xd6a], succ=[0x24d20xd6a]
    =================================
    0xd82: vd82(0x1) = CONST 
    0xd84: vd84(0x1) = CONST 
    0xd86: vd86(0xa0) = CONST 
    0xd88: vd88(0x10000000000000000000000000000000000000000) = SHL vd86(0xa0), vd84(0x1)
    0xd89: vd89(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd88(0x10000000000000000000000000000000000000000), vd82(0x1)
    0xd8b: vd8b = CALLDATALOAD vd6e(0x4)
    0xd8d: vd8d = AND vd89(0xffffffffffffffffffffffffffffffffffffffff), vd8b
    0xd8f: vd8f(0x20) = CONST 
    0xd91: vd91(0x24) = ADD vd8f(0x20), vd6e(0x4)
    0xd92: vd92 = CALLDATALOAD vd91(0x24)
    0xd93: vd93 = AND vd92, vd89(0xffffffffffffffffffffffffffffffffffffffff)
    0xd94: vd94(0x24d2) = CONST 
    0xd97: JUMP vd94(0x24d2)

    Begin block 0x24d20xd6a
    prev=[0xd80], succ=[0x4196]
    =================================
    0x24d30xd6a: vd6a24d3(0x1) = CONST 
    0x24d50xd6a: vd6a24d5(0x1) = CONST 
    0x24d70xd6a: vd6a24d7(0xa0) = CONST 
    0x24d90xd6a: vd6a24d9(0x10000000000000000000000000000000000000000) = SHL vd6a24d7(0xa0), vd6a24d5(0x1)
    0x24da0xd6a: vd6a24da(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd6a24d9(0x10000000000000000000000000000000000000000), vd6a24d3(0x1)
    0x24dd0xd6a: vd6a24dd = AND vd6a24da(0xffffffffffffffffffffffffffffffffffffffff), vd8d
    0x24de0xd6a: vd6a24de(0x0) = CONST 
    0x24e20xd6a: MSTORE vd6a24de(0x0), vd6a24dd
    0x24e30xd6a: vd6a24e3(0x9) = CONST 
    0x24e50xd6a: vd6a24e5(0x20) = CONST 
    0x24e90xd6a: MSTORE vd6a24e5(0x20), vd6a24e3(0x9)
    0x24ea0xd6a: vd6a24ea(0x40) = CONST 
    0x24ee0xd6a: vd6a24ee = SHA3 vd6a24de(0x0), vd6a24ea(0x40)
    0x24f20xd6a: vd6a24f2 = AND vd6a24da(0xffffffffffffffffffffffffffffffffffffffff), vd93
    0x24f40xd6a: MSTORE vd6a24de(0x0), vd6a24f2
    0x24f80xd6a: MSTORE vd6a24e5(0x20), vd6a24ee
    0x24f90xd6a: vd6a24f9 = SHA3 vd6a24de(0x0), vd6a24ea(0x40)
    0x24fa0xd6a: vd6a24fa = SLOAD vd6a24f9
    0x24fb0xd6a: vd6a24fb(0xff) = CONST 
    0x24fd0xd6a: vd6a24fd = AND vd6a24fb(0xff), vd6a24fa
    0x24ff0xd6a: JUMP vd6b(0x4196)

    Begin block 0x4196
    prev=[0x24d20xd6a], succ=[]
    =================================
    0x4197: v4197(0x40) = CONST 
    0x419a: v419a = MLOAD v4197(0x40)
    0x419c: v419c = ISZERO vd6a24fd
    0x419d: v419d = ISZERO v419c
    0x419f: MSTORE v419a, v419d
    0x41a0: v41a0 = MLOAD v4197(0x40)
    0x41a4: v41a4(0x0) = SUB v419a, v41a0
    0x41a5: v41a5(0x20) = CONST 
    0x41a7: v41a7(0x20) = ADD v41a5(0x20), v41a4(0x0)
    0x41a9: RETURN v41a0, v41a7(0x20)

}

function safeTransferFrom(address,address,uint256,uint256,bytes)() public {
    Begin block 0xd98
    prev=[], succ=[0xdaa, 0xdae]
    =================================
    0xd99: vd99(0x41c9) = CONST 
    0xd9c: vd9c(0x4) = CONST 
    0xd9f: vd9f = CALLDATASIZE 
    0xda0: vda0 = SUB vd9f, vd9c(0x4)
    0xda1: vda1(0xa0) = CONST 
    0xda4: vda4 = LT vda0, vda1(0xa0)
    0xda5: vda5 = ISZERO vda4
    0xda6: vda6(0xdae) = CONST 
    0xda9: JUMPI vda6(0xdae), vda5

    Begin block 0xdaa
    prev=[0xd98], succ=[]
    =================================
    0xdaa: vdaa(0x0) = CONST 
    0xdad: REVERT vdaa(0x0), vdaa(0x0)

    Begin block 0xdae
    prev=[0xd98], succ=[0xde9, 0xded]
    =================================
    0xdaf: vdaf(0x1) = CONST 
    0xdb1: vdb1(0x1) = CONST 
    0xdb3: vdb3(0xa0) = CONST 
    0xdb5: vdb5(0x10000000000000000000000000000000000000000) = SHL vdb3(0xa0), vdb1(0x1)
    0xdb6: vdb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdb5(0x10000000000000000000000000000000000000000), vdaf(0x1)
    0xdb8: vdb8 = CALLDATALOAD vd9c(0x4)
    0xdba: vdba = AND vdb6(0xffffffffffffffffffffffffffffffffffffffff), vdb8
    0xdbc: vdbc(0x20) = CONST 
    0xdbf: vdbf(0x24) = ADD vd9c(0x4), vdbc(0x20)
    0xdc0: vdc0 = CALLDATALOAD vdbf(0x24)
    0xdc3: vdc3 = AND vdb6(0xffffffffffffffffffffffffffffffffffffffff), vdc0
    0xdc5: vdc5(0x40) = CONST 
    0xdc8: vdc8(0x44) = ADD vd9c(0x4), vdc5(0x40)
    0xdc9: vdc9 = CALLDATALOAD vdc8(0x44)
    0xdcb: vdcb(0x60) = CONST 
    0xdce: vdce(0x64) = ADD vd9c(0x4), vdcb(0x60)
    0xdcf: vdcf = CALLDATALOAD vdce(0x64)
    0xdd2: vdd2 = ADD vd9c(0x4), vda0
    0xdd4: vdd4(0xa0) = CONST 
    0xdd7: vdd7(0xa4) = ADD vd9c(0x4), vdd4(0xa0)
    0xdd8: vdd8(0x80) = CONST 
    0xddb: vddb(0x84) = ADD vd9c(0x4), vdd8(0x80)
    0xddc: vddc = CALLDATALOAD vddb(0x84)
    0xddd: vddd(0x1) = CONST 
    0xddf: vddf(0x20) = CONST 
    0xde1: vde1(0x100000000) = SHL vddf(0x20), vddd(0x1)
    0xde3: vde3 = GT vddc, vde1(0x100000000)
    0xde4: vde4 = ISZERO vde3
    0xde5: vde5(0xded) = CONST 
    0xde8: JUMPI vde5(0xded), vde4

    Begin block 0xde9
    prev=[0xdae], succ=[]
    =================================
    0xde9: vde9(0x0) = CONST 
    0xdec: REVERT vde9(0x0), vde9(0x0)

    Begin block 0xded
    prev=[0xdae], succ=[0xdfb, 0xdff]
    =================================
    0xdef: vdef = ADD vd9c(0x4), vddc
    0xdf1: vdf1(0x20) = CONST 
    0xdf4: vdf4 = ADD vdef, vdf1(0x20)
    0xdf5: vdf5 = GT vdf4, vdd2
    0xdf6: vdf6 = ISZERO vdf5
    0xdf7: vdf7(0xdff) = CONST 
    0xdfa: JUMPI vdf7(0xdff), vdf6

    Begin block 0xdfb
    prev=[0xded], succ=[]
    =================================
    0xdfb: vdfb(0x0) = CONST 
    0xdfe: REVERT vdfb(0x0), vdfb(0x0)

    Begin block 0xdff
    prev=[0xded], succ=[0xe1c, 0xe20]
    =================================
    0xe01: ve01 = CALLDATALOAD vdef
    0xe03: ve03(0x20) = CONST 
    0xe05: ve05 = ADD ve03(0x20), vdef
    0xe08: ve08(0x1) = CONST 
    0xe0b: ve0b = MUL ve01, ve08(0x1)
    0xe0d: ve0d = ADD ve05, ve0b
    0xe0e: ve0e = GT ve0d, vdd2
    0xe0f: ve0f(0x1) = CONST 
    0xe11: ve11(0x20) = CONST 
    0xe13: ve13(0x100000000) = SHL ve11(0x20), ve0f(0x1)
    0xe15: ve15 = GT ve01, ve13(0x100000000)
    0xe16: ve16 = OR ve15, ve0e
    0xe17: ve17 = ISZERO ve16
    0xe18: ve18(0xe20) = CONST 
    0xe1b: JUMPI ve18(0xe20), ve17

    Begin block 0xe1c
    prev=[0xdff], succ=[]
    =================================
    0xe1c: ve1c(0x0) = CONST 
    0xe1f: REVERT ve1c(0x0), ve1c(0x0)

    Begin block 0xe20
    prev=[0xdff], succ=[0x2500]
    =================================
    0xe25: ve25(0x1f) = CONST 
    0xe27: ve27 = ADD ve25(0x1f), ve01
    0xe28: ve28(0x20) = CONST 
    0xe2c: ve2c = DIV ve27, ve28(0x20)
    0xe2d: ve2d = MUL ve2c, ve28(0x20)
    0xe2e: ve2e(0x20) = CONST 
    0xe30: ve30 = ADD ve2e(0x20), ve2d
    0xe31: ve31(0x40) = CONST 
    0xe33: ve33 = MLOAD ve31(0x40)
    0xe36: ve36 = ADD ve33, ve30
    0xe37: ve37(0x40) = CONST 
    0xe39: MSTORE ve37(0x40), ve36
    0xe41: MSTORE ve33, ve01
    0xe42: ve42(0x20) = CONST 
    0xe44: ve44 = ADD ve42(0x20), ve33
    0xe4a: CALLDATACOPY ve44, ve05, ve01
    0xe4b: ve4b(0x0) = CONST 
    0xe4e: ve4e = ADD ve44, ve01
    0xe52: MSTORE ve4e, ve4b(0x0)
    0xe57: ve57(0x2500) = CONST 
    0xe60: JUMP ve57(0x2500)

    Begin block 0x2500
    prev=[0xe20], succ=[0x250f, 0x2545]
    =================================
    0x2501: v2501(0x1) = CONST 
    0x2503: v2503(0x1) = CONST 
    0x2505: v2505(0xa0) = CONST 
    0x2507: v2507(0x10000000000000000000000000000000000000000) = SHL v2505(0xa0), v2503(0x1)
    0x2508: v2508(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2507(0x10000000000000000000000000000000000000000), v2501(0x1)
    0x250a: v250a = AND vdc3, v2508(0xffffffffffffffffffffffffffffffffffffffff)
    0x250b: v250b(0x2545) = CONST 
    0x250e: JUMPI v250b(0x2545), v250a

    Begin block 0x250f
    prev=[0x2500], succ=[]
    =================================
    0x250f: v250f(0x40) = CONST 
    0x2511: v2511 = MLOAD v250f(0x40)
    0x2512: v2512(0x461bcd) = CONST 
    0x2516: v2516(0xe5) = CONST 
    0x2518: v2518(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2516(0xe5), v2512(0x461bcd)
    0x251a: MSTORE v2511, v2518(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x251b: v251b(0x4) = CONST 
    0x251d: v251d = ADD v251b(0x4), v2511
    0x2520: v2520(0x20) = CONST 
    0x2522: v2522 = ADD v2520(0x20), v251d
    0x2525: v2525(0x20) = SUB v2522, v251d
    0x2527: MSTORE v251d, v2525(0x20)
    0x2528: v2528(0x24) = CONST 
    0x252b: MSTORE v2522, v2528(0x24)
    0x252c: v252c(0x20) = CONST 
    0x252e: v252e = ADD v252c(0x20), v2522
    0x2530: v2530(0x3ab4) = CONST 
    0x2533: v2533(0x24) = CONST 
    0x2536: CODECOPY v252e, v2530(0x3ab4), v2533(0x24)
    0x2537: v2537(0x40) = CONST 
    0x2539: v2539 = ADD v2537(0x40), v252e
    0x253d: v253d(0x40) = CONST 
    0x253f: v253f = MLOAD v253d(0x40)
    0x2542: v2542(0x84) = SUB v2539, v253f
    0x2544: REVERT v253f, v2542(0x84)

    Begin block 0x2545
    prev=[0x2500], succ=[0x254e, 0x258b]
    =================================
    0x2547: v2547(0x1) = CONST 
    0x2549: v2549 = EQ v2547(0x1), vdcf
    0x254a: v254a(0x258b) = CONST 
    0x254d: JUMPI v254a(0x258b), v2549

    Begin block 0x254e
    prev=[0x2545], succ=[]
    =================================
    0x254e: v254e(0x40) = CONST 
    0x2551: v2551 = MLOAD v254e(0x40)
    0x2552: v2552(0x461bcd) = CONST 
    0x2556: v2556(0xe5) = CONST 
    0x2558: v2558(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2556(0xe5), v2552(0x461bcd)
    0x255a: MSTORE v2551, v2558(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x255b: v255b(0x20) = CONST 
    0x255d: v255d(0x4) = CONST 
    0x2560: v2560 = ADD v2551, v255d(0x4)
    0x2561: MSTORE v2560, v255b(0x20)
    0x2562: v2562(0xe) = CONST 
    0x2564: v2564(0x24) = CONST 
    0x2567: v2567 = ADD v2551, v2564(0x24)
    0x2568: MSTORE v2567, v2562(0xe)
    0x2569: v2569(0x125b9d985b1a5908185b5bdd5b9d) = CONST 
    0x2578: v2578(0x92) = CONST 
    0x257a: v257a(0x496e76616c696420616d6f756e74000000000000000000000000000000000000) = SHL v2578(0x92), v2569(0x125b9d985b1a5908185b5bdd5b9d)
    0x257b: v257b(0x44) = CONST 
    0x257e: v257e = ADD v2551, v257b(0x44)
    0x257f: MSTORE v257e, v257a(0x496e76616c696420616d6f756e74000000000000000000000000000000000000)
    0x2581: v2581 = MLOAD v254e(0x40)
    0x2585: v2585(0x0) = SUB v2551, v2581
    0x2586: v2586(0x64) = CONST 
    0x2588: v2588(0x64) = ADD v2586(0x64), v2585(0x0)
    0x258a: REVERT v2581, v2588(0x64)

    Begin block 0x258b
    prev=[0x2545], succ=[0x25a7, 0x259d]
    =================================
    0x258c: v258c(0x1) = CONST 
    0x258e: v258e(0x1) = CONST 
    0x2590: v2590(0xa0) = CONST 
    0x2592: v2592(0x10000000000000000000000000000000000000000) = SHL v2590(0xa0), v258e(0x1)
    0x2593: v2593(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2592(0x10000000000000000000000000000000000000000), v258c(0x1)
    0x2595: v2595 = AND vdba, v2593(0xffffffffffffffffffffffffffffffffffffffff)
    0x2596: v2596 = CALLER 
    0x2597: v2597 = EQ v2596, v2595
    0x2599: v2599(0x25a7) = CONST 
    0x259c: JUMPI v2599(0x25a7), v2597

    Begin block 0x25a7
    prev=[0x258b, 0x24d2B0x259d], succ=[0x25ac, 0x25e2]
    =================================
    0x25a7_0x0: v25a7_0 = PHI v2597, v24fdV259d
    0x25a8: v25a8(0x25e2) = CONST 
    0x25ab: JUMPI v25a8(0x25e2), v25a7_0

    Begin block 0x25ac
    prev=[0x25a7], succ=[]
    =================================
    0x25ac: v25ac(0x40) = CONST 
    0x25ae: v25ae = MLOAD v25ac(0x40)
    0x25af: v25af(0x461bcd) = CONST 
    0x25b3: v25b3(0xe5) = CONST 
    0x25b5: v25b5(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v25b3(0xe5), v25af(0x461bcd)
    0x25b7: MSTORE v25ae, v25b5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x25b8: v25b8(0x4) = CONST 
    0x25ba: v25ba = ADD v25b8(0x4), v25ae
    0x25bd: v25bd(0x20) = CONST 
    0x25bf: v25bf = ADD v25bd(0x20), v25ba
    0x25c2: v25c2(0x20) = SUB v25bf, v25ba
    0x25c4: MSTORE v25ba, v25c2(0x20)
    0x25c5: v25c5(0x2d) = CONST 
    0x25c8: MSTORE v25bf, v25c5(0x2d)
    0x25c9: v25c9(0x20) = CONST 
    0x25cb: v25cb = ADD v25c9(0x20), v25bf
    0x25cd: v25cd(0x3ad8) = CONST 
    0x25d0: v25d0(0x2d) = CONST 
    0x25d3: CODECOPY v25cb, v25cd(0x3ad8), v25d0(0x2d)
    0x25d4: v25d4(0x40) = CONST 
    0x25d6: v25d6 = ADD v25d4(0x40), v25cb
    0x25da: v25da(0x40) = CONST 
    0x25dc: v25dc = MLOAD v25da(0x40)
    0x25df: v25df(0x84) = SUB v25d6, v25dc
    0x25e1: REVERT v25dc, v25df(0x84)

    Begin block 0x25e2
    prev=[0x25a7], succ=[0x25ec]
    =================================
    0x25e3: v25e3(0x25ec) = CONST 
    0x25e8: v25e8(0x2497) = CONST 
    0x25eb: v25eb_0 = CALLPRIVATE v25e8(0x2497), vdc9, vdba, v25e3(0x25ec)

    Begin block 0x25ec
    prev=[0x25e2], succ=[0x25f1, 0x262d]
    =================================
    0x25ed: v25ed(0x262d) = CONST 
    0x25f0: JUMPI v25ed(0x262d), v25eb_0

    Begin block 0x25f1
    prev=[0x25ec], succ=[]
    =================================
    0x25f1: v25f1(0x40) = CONST 
    0x25f4: v25f4 = MLOAD v25f1(0x40)
    0x25f5: v25f5(0x461bcd) = CONST 
    0x25f9: v25f9(0xe5) = CONST 
    0x25fb: v25fb(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v25f9(0xe5), v25f5(0x461bcd)
    0x25fd: MSTORE v25f4, v25fb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x25fe: v25fe(0x20) = CONST 
    0x2600: v2600(0x4) = CONST 
    0x2603: v2603 = ADD v25f4, v2600(0x4)
    0x2604: MSTORE v2603, v25fe(0x20)
    0x2605: v2605(0xd) = CONST 
    0x2607: v2607(0x24) = CONST 
    0x260a: v260a = ADD v25f4, v2607(0x24)
    0x260b: MSTORE v260a, v2605(0xd)
    0x260c: v260c(0x2737ba103a34329037bbb732b9) = CONST 
    0x261a: v261a(0x99) = CONST 
    0x261c: v261c(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v261a(0x99), v260c(0x2737ba103a34329037bbb732b9)
    0x261d: v261d(0x44) = CONST 
    0x2620: v2620 = ADD v25f4, v261d(0x44)
    0x2621: MSTORE v2620, v261c(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x2623: v2623 = MLOAD v25f1(0x40)
    0x2627: v2627(0x0) = SUB v25f4, v2623
    0x2628: v2628(0x64) = CONST 
    0x262a: v262a(0x64) = ADD v2628(0x64), v2627(0x0)
    0x262c: REVERT v2623, v262a(0x64)

    Begin block 0x262d
    prev=[0x25ec], succ=[0x4424]
    =================================
    0x262e: v262e(0x0) = CONST 
    0x2632: MSTORE v262e(0x0), vdc9
    0x2633: v2633(0x8) = CONST 
    0x2635: v2635(0x20) = CONST 
    0x2639: MSTORE v2635(0x20), v2633(0x8)
    0x263a: v263a(0x40) = CONST 
    0x263f: v263f = SHA3 v262e(0x0), v263a(0x40)
    0x2641: v2641 = SLOAD v263f
    0x2642: v2642(0x1) = CONST 
    0x2644: v2644(0x1) = CONST 
    0x2646: v2646(0xa0) = CONST 
    0x2648: v2648(0x10000000000000000000000000000000000000000) = SHL v2646(0xa0), v2644(0x1)
    0x2649: v2649(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2648(0x10000000000000000000000000000000000000000), v2642(0x1)
    0x264a: v264a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2649(0xffffffffffffffffffffffffffffffffffffffff)
    0x264b: v264b = AND v264a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2641
    0x264c: v264c(0x1) = CONST 
    0x264e: v264e(0x1) = CONST 
    0x2650: v2650(0xa0) = CONST 
    0x2652: v2652(0x10000000000000000000000000000000000000000) = SHL v2650(0xa0), v264e(0x1)
    0x2653: v2653(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2652(0x10000000000000000000000000000000000000000), v264c(0x1)
    0x2656: v2656 = AND v2653(0xffffffffffffffffffffffffffffffffffffffff), vdc3
    0x2659: v2659 = OR v2656, v264b
    0x265c: SSTORE v263f, v2659
    0x265e: v265e = MLOAD v263a(0x40)
    0x2661: MSTORE v265e, vdc9
    0x2664: v2664 = ADD v265e, v2635(0x20)
    0x2667: MSTORE v2664, vdcf
    0x2669: v2669 = MLOAD v263a(0x40)
    0x266e: v266e = AND vdba, v2653(0xffffffffffffffffffffffffffffffffffffffff)
    0x2670: v2670 = CALLER 
    0x2672: v2672(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x2697: v2697(0x0) = SUB v265e, v2669
    0x2698: v2698(0x40) = ADD v2697(0x0), v263a(0x40)
    0x269a: LOG4 v2669, v2698(0x40), v2672(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v2670, v266e, v2656
    0x269b: v269b(0x4424) = CONST 
    0x269e: v269e = CALLER 
    0x26a4: v26a4(0x34fd) = CONST 
    0x26a7: CALLPRIVATE v26a4(0x34fd), ve33, vdcf, vdc9, vdc3, vdba, v269e, v269b(0x4424)

    Begin block 0x4424
    prev=[0x262d], succ=[0x41c9]
    =================================
    0x442a: JUMP vd99(0x41c9)

    Begin block 0x41c9
    prev=[0x4424], succ=[]
    =================================
    0x41ca: STOP 

    Begin block 0x259d
    prev=[0x258b], succ=[0x24d2B0x259d]
    =================================
    0x259e: v259e(0x25a7) = CONST 
    0x25a2: v25a2 = CALLER 
    0x25a3: v25a3(0x24d2) = CONST 
    0x25a6: JUMP v25a3(0x24d2)

    Begin block 0x24d2B0x259d
    prev=[0x259d], succ=[0x25a7]
    =================================
    0x24d3S0x259d: v24d3V259d(0x1) = CONST 
    0x24d5S0x259d: v24d5V259d(0x1) = CONST 
    0x24d7S0x259d: v24d7V259d(0xa0) = CONST 
    0x24d9S0x259d: v24d9V259d(0x10000000000000000000000000000000000000000) = SHL v24d7V259d(0xa0), v24d5V259d(0x1)
    0x24daS0x259d: v24daV259d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24d9V259d(0x10000000000000000000000000000000000000000), v24d3V259d(0x1)
    0x24ddS0x259d: v24ddV259d = AND v24daV259d(0xffffffffffffffffffffffffffffffffffffffff), vdba
    0x24deS0x259d: v24deV259d(0x0) = CONST 
    0x24e2S0x259d: MSTORE v24deV259d(0x0), v24ddV259d
    0x24e3S0x259d: v24e3V259d(0x9) = CONST 
    0x24e5S0x259d: v24e5V259d(0x20) = CONST 
    0x24e9S0x259d: MSTORE v24e5V259d(0x20), v24e3V259d(0x9)
    0x24eaS0x259d: v24eaV259d(0x40) = CONST 
    0x24eeS0x259d: v24eeV259d = SHA3 v24deV259d(0x0), v24eaV259d(0x40)
    0x24f2S0x259d: v24f2V259d = AND v24daV259d(0xffffffffffffffffffffffffffffffffffffffff), v25a2
    0x24f4S0x259d: MSTORE v24deV259d(0x0), v24f2V259d
    0x24f8S0x259d: MSTORE v24e5V259d(0x20), v24eeV259d
    0x24f9S0x259d: v24f9V259d = SHA3 v24deV259d(0x0), v24eaV259d(0x40)
    0x24faS0x259d: v24faV259d = SLOAD v24f9V259d
    0x24fbS0x259d: v24fbV259d(0xff) = CONST 
    0x24fdS0x259d: v24fdV259d = AND v24fbV259d(0xff), v24faV259d
    0x24ffS0x259d: JUMP v259e(0x25a7)

}

function starNFTCount()() public {
    Begin block 0xe61
    prev=[], succ=[0x26a8]
    =================================
    0xe62: ve62(0x41ea) = CONST 
    0xe65: ve65(0x26a8) = CONST 
    0xe68: JUMP ve65(0x26a8)

    Begin block 0x26a8
    prev=[0xe61], succ=[0x41ea]
    =================================
    0x26a9: v26a9(0x7) = CONST 
    0x26ab: v26ab = SLOAD v26a9(0x7)
    0x26ad: JUMP ve62(0x41ea)

    Begin block 0x41ea
    prev=[0x26a8], succ=[]
    =================================
    0x41eb: v41eb(0x40) = CONST 
    0x41ee: v41ee = MLOAD v41eb(0x40)
    0x41f1: MSTORE v41ee, v26ab
    0x41f2: v41f2 = MLOAD v41eb(0x40)
    0x41f6: v41f6(0x0) = SUB v41ee, v41f2
    0x41f7: v41f7(0x20) = CONST 
    0x41f9: v41f9(0x20) = ADD v41f7(0x20), v41f6(0x0)
    0x41fb: RETURN v41f2, v41f9(0x20)

}

