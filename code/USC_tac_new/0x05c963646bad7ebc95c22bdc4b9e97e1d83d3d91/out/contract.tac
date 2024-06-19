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
    prev=[0x0], succ=[0x1a, 0x4733]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x467d: v467d(0x4733) = CONST 
    0x467e: JUMPI v467d(0x4733), v15

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
    prev=[0x1a8], succ=[0x46c7, 0x1fa]
    =================================
    0x1f1: v1f1(0xfdd58e) = CONST 
    0x1f5: v1f5 = EQ v1f1(0xfdd58e), v1f
    0x46bf: v46bf(0x46c7) = CONST 
    0x46c0: JUMPI v46bf(0x46c7), v1f5

    Begin block 0x46c7
    prev=[0x1ef], succ=[]
    =================================
    0x46c8: v46c8(0x220) = CONST 
    0x46c9: CALLPRIVATE v46c8(0x220)

    Begin block 0x1fa
    prev=[0x1ef], succ=[0x46ca, 0x205]
    =================================
    0x1fb: v1fb(0x1ffc9a7) = CONST 
    0x200: v200 = EQ v1fb(0x1ffc9a7), v1f
    0x46c1: v46c1(0x46ca) = CONST 
    0x46c2: JUMPI v46c1(0x46ca), v200

    Begin block 0x46ca
    prev=[0x1fa], succ=[]
    =================================
    0x46cb: v46cb(0x25e) = CONST 
    0x46cc: CALLPRIVATE v46cb(0x25e)

    Begin block 0x205
    prev=[0x1fa], succ=[0x46cd, 0x210]
    =================================
    0x206: v206(0x2fe5305) = CONST 
    0x20b: v20b = EQ v206(0x2fe5305), v1f
    0x46c3: v46c3(0x46cd) = CONST 
    0x46c4: JUMPI v46c3(0x46cd), v20b

    Begin block 0x46cd
    prev=[0x205], succ=[]
    =================================
    0x46ce: v46ce(0x299) = CONST 
    0x46cf: CALLPRIVATE v46ce(0x299)

    Begin block 0x210
    prev=[0x205], succ=[0x46d0, 0x21b]
    =================================
    0x211: v211(0xe89341c) = CONST 
    0x216: v216 = EQ v211(0xe89341c), v1f
    0x46c5: v46c5(0x46d0) = CONST 
    0x46c6: JUMPI v46c5(0x46d0), v216

    Begin block 0x46d0
    prev=[0x210], succ=[]
    =================================
    0x46d1: v46d1(0x33f) = CONST 
    0x46d2: CALLPRIVATE v46d1(0x33f)

    Begin block 0x21b
    prev=[0x210], succ=[]
    =================================
    0x21c: v21c(0x0) = CONST 
    0x21f: REVERT v21c(0x0), v21c(0x0)

    Begin block 0x1b4
    prev=[0x1a8], succ=[0x46d3, 0x1bf]
    =================================
    0x1b5: v1b5(0x158ef93e) = CONST 
    0x1ba: v1ba = EQ v1b5(0x158ef93e), v1f
    0x46b5: v46b5(0x46d3) = CONST 
    0x46b6: JUMPI v46b5(0x46d3), v1ba

    Begin block 0x46d3
    prev=[0x1b4], succ=[]
    =================================
    0x46d4: v46d4(0x3d1) = CONST 
    0x46d5: CALLPRIVATE v46d4(0x3d1)

    Begin block 0x1bf
    prev=[0x1b4], succ=[0x46d6, 0x1ca]
    =================================
    0x1c0: v1c0(0x2de041f9) = CONST 
    0x1c5: v1c5 = EQ v1c0(0x2de041f9), v1f
    0x46b7: v46b7(0x46d6) = CONST 
    0x46b8: JUMPI v46b7(0x46d6), v1c5

    Begin block 0x46d6
    prev=[0x1bf], succ=[]
    =================================
    0x46d7: v46d7(0x3d9) = CONST 
    0x46d8: CALLPRIVATE v46d7(0x3d9)

    Begin block 0x1ca
    prev=[0x1bf], succ=[0x46d9, 0x1d5]
    =================================
    0x1cb: v1cb(0x2eb2c2d6) = CONST 
    0x1d0: v1d0 = EQ v1cb(0x2eb2c2d6), v1f
    0x46b9: v46b9(0x46d9) = CONST 
    0x46ba: JUMPI v46b9(0x46d9), v1d0

    Begin block 0x46d9
    prev=[0x1ca], succ=[]
    =================================
    0x46da: v46da(0x41b) = CONST 
    0x46db: CALLPRIVATE v46da(0x41b)

    Begin block 0x1d5
    prev=[0x1ca], succ=[0x46dc, 0x1e0]
    =================================
    0x1d6: v1d6(0x3092afd5) = CONST 
    0x1db: v1db = EQ v1d6(0x3092afd5), v1f
    0x46bb: v46bb(0x46dc) = CONST 
    0x46bc: JUMPI v46bb(0x46dc), v1db

    Begin block 0x46dc
    prev=[0x1d5], succ=[]
    =================================
    0x46dd: v46dd(0x5dc) = CONST 
    0x46de: CALLPRIVATE v46dd(0x5dc)

    Begin block 0x1e0
    prev=[0x1d5], succ=[0x1eb, 0x46df]
    =================================
    0x1e1: v1e1(0x40c10f19) = CONST 
    0x1e6: v1e6 = EQ v1e1(0x40c10f19), v1f
    0x46bd: v46bd(0x46df) = CONST 
    0x46be: JUMPI v46bd(0x46df), v1e6

    Begin block 0x1eb
    prev=[0x1e0], succ=[0x3d7d]
    =================================
    0x1eb: v1eb(0x3d7d) = CONST 
    0x1ee: JUMP v1eb(0x3d7d)

    Begin block 0x3d7d
    prev=[0x1eb], succ=[]
    =================================
    0x3d7e: v3d7e(0x0) = CONST 
    0x3d81: REVERT v3d7e(0x0), v3d7e(0x0)

    Begin block 0x46df
    prev=[0x1e0], succ=[]
    =================================
    0x46e0: v46e0(0x602) = CONST 
    0x46e1: CALLPRIVATE v46e0(0x602)

    Begin block 0x131
    prev=[0x125], succ=[0x177, 0x13c]
    =================================
    0x132: v132(0x6c0360eb) = CONST 
    0x137: v137 = GT v132(0x6c0360eb), v1f
    0x138: v138(0x177) = CONST 
    0x13b: JUMPI v138(0x177), v137

    Begin block 0x177
    prev=[0x131], succ=[0x46e2, 0x183]
    =================================
    0x179: v179(0x485cc955) = CONST 
    0x17e: v17e = EQ v179(0x485cc955), v1f
    0x46ad: v46ad(0x46e2) = CONST 
    0x46ae: JUMPI v46ad(0x46e2), v17e

    Begin block 0x46e2
    prev=[0x177], succ=[]
    =================================
    0x46e3: v46e3(0x62e) = CONST 
    0x46e4: CALLPRIVATE v46e3(0x62e)

    Begin block 0x183
    prev=[0x177], succ=[0x46e5, 0x18e]
    =================================
    0x184: v184(0x4e1273f4) = CONST 
    0x189: v189 = EQ v184(0x4e1273f4), v1f
    0x46af: v46af(0x46e5) = CONST 
    0x46b0: JUMPI v46af(0x46e5), v189

    Begin block 0x46e5
    prev=[0x183], succ=[]
    =================================
    0x46e6: v46e6(0x65c) = CONST 
    0x46e7: CALLPRIVATE v46e6(0x65c)

    Begin block 0x18e
    prev=[0x183], succ=[0x46e8, 0x199]
    =================================
    0x18f: v18f(0x4fb2e45d) = CONST 
    0x194: v194 = EQ v18f(0x4fb2e45d), v1f
    0x46b1: v46b1(0x46e8) = CONST 
    0x46b2: JUMPI v46b1(0x46e8), v194

    Begin block 0x46e8
    prev=[0x18e], succ=[]
    =================================
    0x46e9: v46e9(0x7cf) = CONST 
    0x46ea: CALLPRIVATE v46e9(0x7cf)

    Begin block 0x199
    prev=[0x18e], succ=[0x1a4, 0x46eb]
    =================================
    0x19a: v19a(0x540865fe) = CONST 
    0x19f: v19f = EQ v19a(0x540865fe), v1f
    0x46b3: v46b3(0x46eb) = CONST 
    0x46b4: JUMPI v46b3(0x46eb), v19f

    Begin block 0x1a4
    prev=[0x199], succ=[0x3d59]
    =================================
    0x1a4: v1a4(0x3d59) = CONST 
    0x1a7: JUMP v1a4(0x3d59)

    Begin block 0x3d59
    prev=[0x1a4], succ=[]
    =================================
    0x3d5a: v3d5a(0x0) = CONST 
    0x3d5d: REVERT v3d5a(0x0), v3d5a(0x0)

    Begin block 0x46eb
    prev=[0x199], succ=[]
    =================================
    0x46ec: v46ec(0x7f5) = CONST 
    0x46ed: CALLPRIVATE v46ec(0x7f5)

    Begin block 0x13c
    prev=[0x131], succ=[0x46ee, 0x147]
    =================================
    0x13d: v13d(0x6c0360eb) = CONST 
    0x142: v142 = EQ v13d(0x6c0360eb), v1f
    0x46a3: v46a3(0x46ee) = CONST 
    0x46a4: JUMPI v46a3(0x46ee), v142

    Begin block 0x46ee
    prev=[0x13c], succ=[]
    =================================
    0x46ef: v46ef(0x821) = CONST 
    0x46f0: CALLPRIVATE v46ef(0x821)

    Begin block 0x147
    prev=[0x13c], succ=[0x46f1, 0x152]
    =================================
    0x148: v148(0x6d70f7ae) = CONST 
    0x14d: v14d = EQ v148(0x6d70f7ae), v1f
    0x46a5: v46a5(0x46f1) = CONST 
    0x46a6: JUMPI v46a5(0x46f1), v14d

    Begin block 0x46f1
    prev=[0x147], succ=[]
    =================================
    0x46f2: v46f2(0x829) = CONST 
    0x46f3: CALLPRIVATE v46f2(0x829)

    Begin block 0x152
    prev=[0x147], succ=[0x46f4, 0x15d]
    =================================
    0x153: v153(0x70c2f239) = CONST 
    0x158: v158 = EQ v153(0x70c2f239), v1f
    0x46a7: v46a7(0x46f4) = CONST 
    0x46a8: JUMPI v46a7(0x46f4), v158

    Begin block 0x46f4
    prev=[0x152], succ=[]
    =================================
    0x46f5: v46f5(0x84f) = CONST 
    0x46f6: CALLPRIVATE v46f5(0x84f)

    Begin block 0x15d
    prev=[0x152], succ=[0x46f7, 0x168]
    =================================
    0x15e: v15e(0x7a2a4b32) = CONST 
    0x163: v163 = EQ v15e(0x7a2a4b32), v1f
    0x46a9: v46a9(0x46f7) = CONST 
    0x46aa: JUMPI v46a9(0x46f7), v163

    Begin block 0x46f7
    prev=[0x15d], succ=[]
    =================================
    0x46f8: v46f8(0x8d2) = CONST 
    0x46f9: CALLPRIVATE v46f8(0x8d2)

    Begin block 0x168
    prev=[0x15d], succ=[0x173, 0x46fa]
    =================================
    0x169: v169(0x8a89bb14) = CONST 
    0x16e: v16e = EQ v169(0x8a89bb14), v1f
    0x46ab: v46ab(0x46fa) = CONST 
    0x46ac: JUMPI v46ab(0x46fa), v16e

    Begin block 0x173
    prev=[0x168], succ=[0x3d35]
    =================================
    0x173: v173(0x3d35) = CONST 
    0x176: JUMP v173(0x3d35)

    Begin block 0x3d35
    prev=[0x173], succ=[]
    =================================
    0x3d36: v3d36(0x0) = CONST 
    0x3d39: REVERT v3d36(0x0), v3d36(0x0)

    Begin block 0x46fa
    prev=[0x168], succ=[]
    =================================
    0x46fb: v46fb(0x99f) = CONST 
    0x46fc: CALLPRIVATE v46fb(0x99f)

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
    prev=[0xad], succ=[0x100, 0x46fd]
    =================================
    0xf6: vf6(0x9204aac6) = CONST 
    0xfb: vfb = EQ vf6(0x9204aac6), v1f
    0x469b: v469b(0x46fd) = CONST 
    0x469c: JUMPI v469b(0x46fd), vfb

    Begin block 0x100
    prev=[0xf4], succ=[0x4700, 0x10b]
    =================================
    0x101: v101(0x983b2d56) = CONST 
    0x106: v106 = EQ v101(0x983b2d56), v1f
    0x469d: v469d(0x4700) = CONST 
    0x469e: JUMPI v469d(0x4700), v106

    Begin block 0x4700
    prev=[0x100], succ=[]
    =================================
    0x4701: v4701(0x9f5) = CONST 
    0x4702: CALLPRIVATE v4701(0x9f5)

    Begin block 0x10b
    prev=[0x100], succ=[0x4703, 0x116]
    =================================
    0x10c: v10c(0x9870d7fe) = CONST 
    0x111: v111 = EQ v10c(0x9870d7fe), v1f
    0x469f: v469f(0x4703) = CONST 
    0x46a0: JUMPI v469f(0x4703), v111

    Begin block 0x4703
    prev=[0x10b], succ=[]
    =================================
    0x4704: v4704(0xa1b) = CONST 
    0x4705: CALLPRIVATE v4704(0xa1b)

    Begin block 0x116
    prev=[0x10b], succ=[0x121, 0x4706]
    =================================
    0x117: v117(0x9dc29fac) = CONST 
    0x11c: v11c = EQ v117(0x9dc29fac), v1f
    0x46a1: v46a1(0x4706) = CONST 
    0x46a2: JUMPI v46a1(0x4706), v11c

    Begin block 0x121
    prev=[0x116], succ=[0x3d11]
    =================================
    0x121: v121(0x3d11) = CONST 
    0x124: JUMP v121(0x3d11)

    Begin block 0x3d11
    prev=[0x121], succ=[]
    =================================
    0x3d12: v3d12(0x0) = CONST 
    0x3d15: REVERT v3d12(0x0), v3d12(0x0)

    Begin block 0x4706
    prev=[0x116], succ=[]
    =================================
    0x4707: v4707(0xa41) = CONST 
    0x4708: CALLPRIVATE v4707(0xa41)

    Begin block 0x46fd
    prev=[0xf4], succ=[]
    =================================
    0x46fe: v46fe(0x9d1) = CONST 
    0x46ff: CALLPRIVATE v46fe(0x9d1)

    Begin block 0xb9
    prev=[0xad], succ=[0x4709, 0xc4]
    =================================
    0xba: vba(0xa22cb465) = CONST 
    0xbf: vbf = EQ vba(0xa22cb465), v1f
    0x4691: v4691(0x4709) = CONST 
    0x4692: JUMPI v4691(0x4709), vbf

    Begin block 0x4709
    prev=[0xb9], succ=[]
    =================================
    0x470a: v470a(0xa6d) = CONST 
    0x470b: CALLPRIVATE v470a(0xa6d)

    Begin block 0xc4
    prev=[0xb9], succ=[0x470c, 0xcf]
    =================================
    0xc5: vc5(0xa36dc62c) = CONST 
    0xca: vca = EQ vc5(0xa36dc62c), v1f
    0x4693: v4693(0x470c) = CONST 
    0x4694: JUMPI v4693(0x470c), vca

    Begin block 0x470c
    prev=[0xc4], succ=[]
    =================================
    0x470d: v470d(0xa9b) = CONST 
    0x470e: CALLPRIVATE v470d(0xa9b)

    Begin block 0xcf
    prev=[0xc4], succ=[0x470f, 0xda]
    =================================
    0xd0: vd0(0xa4a87571) = CONST 
    0xd5: vd5 = EQ vd0(0xa4a87571), v1f
    0x4695: v4695(0x470f) = CONST 
    0x4696: JUMPI v4695(0x470f), vd5

    Begin block 0x470f
    prev=[0xcf], succ=[]
    =================================
    0x4710: v4710(0xb75) = CONST 
    0x4711: CALLPRIVATE v4710(0xb75)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x4712]
    =================================
    0xdb: vdb(0xaa271e1a) = CONST 
    0xe0: ve0 = EQ vdb(0xaa271e1a), v1f
    0x4697: v4697(0x4712) = CONST 
    0x4698: JUMPI v4697(0x4712), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0xf0, 0x4715]
    =================================
    0xe6: ve6(0xaa936a0d) = CONST 
    0xeb: veb = EQ ve6(0xaa936a0d), v1f
    0x4699: v4699(0x4715) = CONST 
    0x469a: JUMPI v4699(0x4715), veb

    Begin block 0xf0
    prev=[0xe5], succ=[0x3ced]
    =================================
    0xf0: vf0(0x3ced) = CONST 
    0xf3: JUMP vf0(0x3ced)

    Begin block 0x3ced
    prev=[0xf0], succ=[]
    =================================
    0x3cee: v3cee(0x0) = CONST 
    0x3cf1: REVERT v3cee(0x0), v3cee(0x0)

    Begin block 0x4715
    prev=[0xe5], succ=[]
    =================================
    0x4716: v4716(0xbf0) = CONST 
    0x4717: CALLPRIVATE v4716(0xbf0)

    Begin block 0x4712
    prev=[0xda], succ=[]
    =================================
    0x4713: v4713(0xbca) = CONST 
    0x4714: CALLPRIVATE v4713(0xbca)

    Begin block 0x36
    prev=[0x2b], succ=[0x7c, 0x41]
    =================================
    0x37: v37(0xc46d0771) = CONST 
    0x3c: v3c = GT v37(0xc46d0771), v1f
    0x3d: v3d(0x7c) = CONST 
    0x40: JUMPI v3d(0x7c), v3c

    Begin block 0x7c
    prev=[0x36], succ=[0x4718, 0x88]
    =================================
    0x7e: v7e(0xac8a584a) = CONST 
    0x83: v83 = EQ v7e(0xac8a584a), v1f
    0x4689: v4689(0x4718) = CONST 
    0x468a: JUMPI v4689(0x4718), v83

    Begin block 0x4718
    prev=[0x7c], succ=[]
    =================================
    0x4719: v4719(0xc16) = CONST 
    0x471a: CALLPRIVATE v4719(0xc16)

    Begin block 0x88
    prev=[0x7c], succ=[0x471b, 0x93]
    =================================
    0x89: v89(0xb2dc5dc3) = CONST 
    0x8e: v8e = EQ v89(0xb2dc5dc3), v1f
    0x468b: v468b(0x471b) = CONST 
    0x468c: JUMPI v468b(0x471b), v8e

    Begin block 0x471b
    prev=[0x88], succ=[]
    =================================
    0x471c: v471c(0xc3c) = CONST 
    0x471d: CALLPRIVATE v471c(0xc3c)

    Begin block 0x93
    prev=[0x88], succ=[0x471e, 0x9e]
    =================================
    0x94: v94(0xb738592d) = CONST 
    0x99: v99 = EQ v94(0xb738592d), v1f
    0x468d: v468d(0x471e) = CONST 
    0x468e: JUMPI v468d(0x471e), v99

    Begin block 0x471e
    prev=[0x93], succ=[]
    =================================
    0x471f: v471f(0xcba) = CONST 
    0x4720: CALLPRIVATE v471f(0xcba)

    Begin block 0x9e
    prev=[0x93], succ=[0xa9, 0x4721]
    =================================
    0x9f: v9f(0xb774b2b1) = CONST 
    0xa4: va4 = EQ v9f(0xb774b2b1), v1f
    0x468f: v468f(0x4721) = CONST 
    0x4690: JUMPI v468f(0x4721), va4

    Begin block 0xa9
    prev=[0x9e], succ=[0x3cc9]
    =================================
    0xa9: va9(0x3cc9) = CONST 
    0xac: JUMP va9(0x3cc9)

    Begin block 0x3cc9
    prev=[0xa9], succ=[]
    =================================
    0x3cca: v3cca(0x0) = CONST 
    0x3ccd: REVERT v3cca(0x0), v3cca(0x0)

    Begin block 0x4721
    prev=[0x9e], succ=[]
    =================================
    0x4722: v4722(0xcc2) = CONST 
    0x4723: CALLPRIVATE v4722(0xcc2)

    Begin block 0x41
    prev=[0x36], succ=[0x4724, 0x4c]
    =================================
    0x42: v42(0xc46d0771) = CONST 
    0x47: v47 = EQ v42(0xc46d0771), v1f
    0x467f: v467f(0x4724) = CONST 
    0x4680: JUMPI v467f(0x4724), v47

    Begin block 0x4724
    prev=[0x41], succ=[]
    =================================
    0x4725: v4725(0xd12) = CONST 
    0x4726: CALLPRIVATE v4725(0xd12)

    Begin block 0x4c
    prev=[0x41], succ=[0x4727, 0x57]
    =================================
    0x4d: v4d(0xc5b8f772) = CONST 
    0x52: v52 = EQ v4d(0xc5b8f772), v1f
    0x4681: v4681(0x4727) = CONST 
    0x4682: JUMPI v4681(0x4727), v52

    Begin block 0x4727
    prev=[0x4c], succ=[]
    =================================
    0x4728: v4728(0xd3e) = CONST 
    0x4729: CALLPRIVATE v4728(0xd3e)

    Begin block 0x57
    prev=[0x4c], succ=[0x62, 0x472a]
    =================================
    0x58: v58(0xe985e9c5) = CONST 
    0x5d: v5d = EQ v58(0xe985e9c5), v1f
    0x4683: v4683(0x472a) = CONST 
    0x4684: JUMPI v4683(0x472a), v5d

    Begin block 0x62
    prev=[0x57], succ=[0x472d, 0x6d]
    =================================
    0x63: v63(0xf242432a) = CONST 
    0x68: v68 = EQ v63(0xf242432a), v1f
    0x4685: v4685(0x472d) = CONST 
    0x4686: JUMPI v4685(0x472d), v68

    Begin block 0x472d
    prev=[0x62], succ=[]
    =================================
    0x472e: v472e(0xd98) = CONST 
    0x472f: CALLPRIVATE v472e(0xd98)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x4730]
    =================================
    0x6e: v6e(0xf2ebbc3d) = CONST 
    0x73: v73 = EQ v6e(0xf2ebbc3d), v1f
    0x4687: v4687(0x4730) = CONST 
    0x4688: JUMPI v4687(0x4730), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x3ca5]
    =================================
    0x78: v78(0x3ca5) = CONST 
    0x7b: JUMP v78(0x3ca5)

    Begin block 0x3ca5
    prev=[0x78], succ=[]
    =================================
    0x3ca6: v3ca6(0x0) = CONST 
    0x3ca9: REVERT v3ca6(0x0), v3ca6(0x0)

    Begin block 0x4730
    prev=[0x6d], succ=[]
    =================================
    0x4731: v4731(0xe61) = CONST 
    0x4732: CALLPRIVATE v4731(0xe61)

    Begin block 0x472a
    prev=[0x57], succ=[]
    =================================
    0x472b: v472b(0xd6a) = CONST 
    0x472c: CALLPRIVATE v472b(0xd6a)

    Begin block 0x4733
    prev=[0x10], succ=[]
    =================================
    0x4734: v4734(0x3c81) = CONST 
    0x4735: CALLPRIVATE v4734(0x3c81)

}

function 0x184b(0x184barg0x0) private {
    Begin block 0x184b
    prev=[], succ=[0x434d, 0x188e]
    =================================
    0x184c: v184c(0x2) = CONST 
    0x184f: v184f = SLOAD v184c(0x2)
    0x1850: v1850(0x40) = CONST 
    0x1853: v1853 = MLOAD v1850(0x40)
    0x1854: v1854(0x20) = CONST 
    0x1856: v1856(0x1f) = CONST 
    0x1858: v1858(0x0) = CONST 
    0x185a: v185a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1858(0x0)
    0x185b: v185b(0x100) = CONST 
    0x185e: v185e(0x1) = CONST 
    0x1861: v1861 = AND v184f, v185e(0x1)
    0x1862: v1862 = ISZERO v1861
    0x1863: v1863 = MUL v1862, v185b(0x100)
    0x1864: v1864 = ADD v1863, v185a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1867: v1867 = AND v184f, v1864
    0x186a: v186a = DIV v1867, v184c(0x2)
    0x186d: v186d = ADD v186a, v1856(0x1f)
    0x1870: v1870 = DIV v186d, v1854(0x20)
    0x1872: v1872 = MUL v1854(0x20), v1870
    0x1874: v1874 = ADD v1853, v1872
    0x1876: v1876 = ADD v1854(0x20), v1874
    0x1879: MSTORE v1850(0x40), v1876
    0x187c: MSTORE v1853, v186a
    0x187d: v187d(0x60) = CONST 
    0x1885: v1885 = ADD v1853, v1854(0x20)
    0x1889: v1889 = ISZERO v186a
    0x188a: v188a(0x434d) = CONST 
    0x188d: JUMPI v188a(0x434d), v1889

    Begin block 0x434d
    prev=[0x184b], succ=[]
    =================================
    0x4356: RETURNPRIVATE v184barg0, v1853

    Begin block 0x188e
    prev=[0x184b], succ=[0x1896, 0x18a9]
    =================================
    0x188f: v188f(0x1f) = CONST 
    0x1891: v1891 = LT v188f(0x1f), v186a
    0x1892: v1892(0x18a9) = CONST 
    0x1895: JUMPI v1892(0x18a9), v1891

    Begin block 0x1896
    prev=[0x188e], succ=[0x4376]
    =================================
    0x1896: v1896(0x100) = CONST 
    0x189b: v189b = SLOAD v184c(0x2)
    0x189c: v189c = DIV v189b, v1896(0x100)
    0x189d: v189d = MUL v189c, v1896(0x100)
    0x189f: MSTORE v1885, v189d
    0x18a1: v18a1(0x20) = CONST 
    0x18a3: v18a3 = ADD v18a1(0x20), v1885
    0x18a5: v18a5(0x4376) = CONST 
    0x18a8: JUMP v18a5(0x4376)

    Begin block 0x4376
    prev=[0x1896], succ=[]
    =================================
    0x437f: RETURNPRIVATE v184barg0, v1853

    Begin block 0x18a9
    prev=[0x188e], succ=[0x18b7]
    =================================
    0x18ab: v18ab = ADD v1885, v186a
    0x18ae: v18ae(0x0) = CONST 
    0x18b0: MSTORE v18ae(0x0), v184c(0x2)
    0x18b1: v18b1(0x20) = CONST 
    0x18b3: v18b3(0x0) = CONST 
    0x18b5: v18b5 = SHA3 v18b3(0x0), v18b1(0x20)

    Begin block 0x18b7
    prev=[0x18a9, 0x18b7], succ=[0x18b7, 0x18cb]
    =================================
    0x18b7_0x0: v18b7_0 = PHI v1885, v18c3
    0x18b7_0x1: v18b7_1 = PHI v18b5, v18bf
    0x18b9: v18b9 = SLOAD v18b7_1
    0x18bb: MSTORE v18b7_0, v18b9
    0x18bd: v18bd(0x1) = CONST 
    0x18bf: v18bf = ADD v18bd(0x1), v18b7_1
    0x18c1: v18c1(0x20) = CONST 
    0x18c3: v18c3 = ADD v18c1(0x20), v18b7_0
    0x18c6: v18c6 = GT v18ab, v18c3
    0x18c7: v18c7(0x18b7) = CONST 
    0x18ca: JUMPI v18c7(0x18b7), v18c6

    Begin block 0x18cb
    prev=[0x18b7], succ=[0x18d4]
    =================================
    0x18cd: v18cd = SUB v18c3, v18ab
    0x18ce: v18ce(0x1f) = CONST 
    0x18d0: v18d0 = AND v18ce(0x1f), v18cd
    0x18d2: v18d2 = ADD v18ab, v18d0

    Begin block 0x18d4
    prev=[0x18cb], succ=[]
    =================================
    0x18dd: RETURNPRIVATE v184barg0, v1853

}

function balanceOf(address,uint256)() public {
    Begin block 0x220
    prev=[], succ=[0x232, 0x236]
    =================================
    0x221: v221(0x3da1) = CONST 
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
    0xe710x220: v220e71(0x24b9) = CONST 
    0xe740x220: v220e74_0 = CALLPRIVATE v220e71(0x24b9), v247, v242, v220e6c(0xe75)

    Begin block 0xe750x220
    prev=[0xe690x220], succ=[0xe7b0x220, 0xe820x220]
    =================================
    0xe760x220: v220e76 = ISZERO v220e74_0
    0xe770x220: v220e77(0xe82) = CONST 
    0xe7a0x220: JUMPI v220e77(0xe82), v220e76

    Begin block 0xe7b0x220
    prev=[0xe750x220], succ=[0x424e0x220]
    =================================
    0xe7c0x220: v220e7c(0x1) = CONST 
    0xe7e0x220: v220e7e(0x424e) = CONST 
    0xe810x220: JUMP v220e7e(0x424e)

    Begin block 0x424e0x220
    prev=[0xe7b0x220], succ=[0x3da1]
    =================================
    0x42530x220: JUMP v221(0x3da1)

    Begin block 0x3da1
    prev=[0xe860x220, 0x424e0x220], succ=[]
    =================================
    0x3da1_0x0: v3da1_0 = PHI v220e84(0x0), v220e7c(0x1)
    0x3da2: v3da2(0x40) = CONST 
    0x3da5: v3da5 = MLOAD v3da2(0x40)
    0x3da8: MSTORE v3da5, v3da1_0
    0x3da9: v3da9 = MLOAD v3da2(0x40)
    0x3dad: v3dad(0x0) = SUB v3da5, v3da9
    0x3dae: v3dae(0x20) = CONST 
    0x3db0: v3db0(0x20) = ADD v3dae(0x20), v3dad(0x0)
    0x3db2: RETURN v3da9, v3db0(0x20)

    Begin block 0xe820x220
    prev=[0xe750x220], succ=[0xe860x220]
    =================================
    0xe840x220: v220e84(0x0) = CONST 

    Begin block 0xe860x220
    prev=[0xe820x220], succ=[0x3da1]
    =================================
    0xe8b0x220: JUMP v221(0x3da1)

}

function 0x24b9(0x24b9arg0x0, 0x24b9arg0x1, 0x24b9arg0x2) private {
    Begin block 0x24b9
    prev=[], succ=[0x24d10x24b9, 0x24ca0x24b9]
    =================================
    0x24ba: v24ba(0x0) = CONST 
    0x24bc: v24bc(0x1) = CONST 
    0x24be: v24be(0x1) = CONST 
    0x24c0: v24c0(0xa0) = CONST 
    0x24c2: v24c2(0x10000000000000000000000000000000000000000) = SHL v24c0(0xa0), v24be(0x1)
    0x24c3: v24c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24c2(0x10000000000000000000000000000000000000000), v24bc(0x1)
    0x24c5: v24c5 = AND v24b9arg1, v24c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x24c6: v24c6(0x24d1) = CONST 
    0x24c9: JUMPI v24c6(0x24d1), v24c5

    Begin block 0x24d10x24b9
    prev=[0x24b9], succ=[0x44320x24b9]
    =================================
    0x24d30x24b9: v24b924d3(0x0) = CONST 
    0x24d70x24b9: MSTORE v24b924d3(0x0), v24b9arg0
    0x24d80x24b9: v24b924d8(0x8) = CONST 
    0x24da0x24b9: v24b924da(0x20) = CONST 
    0x24dc0x24b9: MSTORE v24b924da(0x20), v24b924d8(0x8)
    0x24dd0x24b9: v24b924dd(0x40) = CONST 
    0x24e00x24b9: v24b924e0 = SHA3 v24b924d3(0x0), v24b924dd(0x40)
    0x24e10x24b9: v24b924e1 = SLOAD v24b924e0
    0x24e20x24b9: v24b924e2(0x1) = CONST 
    0x24e40x24b9: v24b924e4(0x1) = CONST 
    0x24e60x24b9: v24b924e6(0xa0) = CONST 
    0x24e80x24b9: v24b924e8(0x10000000000000000000000000000000000000000) = SHL v24b924e6(0xa0), v24b924e4(0x1)
    0x24e90x24b9: v24b924e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24b924e8(0x10000000000000000000000000000000000000000), v24b924e2(0x1)
    0x24ec0x24b9: v24b924ec = AND v24b924e9(0xffffffffffffffffffffffffffffffffffffffff), v24b9arg1
    0x24ee0x24b9: v24b924ee = AND v24b924e1, v24b924e9(0xffffffffffffffffffffffffffffffffffffffff)
    0x24ef0x24b9: v24b924ef = EQ v24b924ee, v24b924ec
    0x24f00x24b9: v24b924f0(0x4432) = CONST 
    0x24f30x24b9: JUMP v24b924f0(0x4432)

    Begin block 0x44320x24b9
    prev=[0x24d10x24b9], succ=[]
    =================================
    0x44370x24b9: RETURNPRIVATE v24b9arg2, v24b924ef

    Begin block 0x24ca0x24b9
    prev=[0x24b9], succ=[0x440d0x24b9]
    =================================
    0x24cb0x24b9: v24b924cb(0x0) = CONST 
    0x24cd0x24b9: v24b924cd(0x440d) = CONST 
    0x24d00x24b9: JUMP v24b924cd(0x440d)

    Begin block 0x440d0x24b9
    prev=[0x24ca0x24b9], succ=[]
    =================================
    0x44120x24b9: RETURNPRIVATE v24b9arg2, v24b924cb(0x0)

}

function supportsInterface(bytes4)() public {
    Begin block 0x25e
    prev=[], succ=[0x270, 0x274]
    =================================
    0x25f: v25f(0x3dd2) = CONST 
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
    prev=[0xe8c], succ=[0x3dd2]
    =================================
    0xeae: JUMP v25f(0x3dd2)

    Begin block 0x3dd2
    prev=[0xeaa], succ=[]
    =================================
    0x3dd3: v3dd3(0x40) = CONST 
    0x3dd6: v3dd6 = MLOAD v3dd3(0x40)
    0x3dd8: v3dd8 = ISZERO vea9
    0x3dd9: v3dd9 = ISZERO v3dd8
    0x3ddb: MSTORE v3dd6, v3dd9
    0x3ddc: v3ddc = MLOAD v3dd3(0x40)
    0x3de0: v3de0(0x0) = SUB v3dd6, v3ddc
    0x3de1: v3de1(0x20) = CONST 
    0x3de3: v3de3(0x20) = ADD v3de1(0x20), v3de0(0x0)
    0x3de5: RETURN v3ddc, v3de3(0x20)

}

function 0x26d0(0x26d0arg0x0, 0x26d0arg0x1) private {
    Begin block 0x26d0
    prev=[], succ=[0x26f5, 0x26d8]
    =================================
    0x26d1: v26d1(0x60) = CONST 
    0x26d4: v26d4(0x26f5) = CONST 
    0x26d7: JUMPI v26d4(0x26f5), v26d0arg0

    Begin block 0x26f5
    prev=[0x26d0], succ=[0x26f9]
    =================================
    0x26f7: v26f7(0x0) = CONST 

    Begin block 0x26f9
    prev=[0x2700, 0x26f5], succ=[0x2700, 0x270d]
    =================================
    0x26f9_0x1: v26f9_1 = PHI v2706, v26d0arg0
    0x26fb: v26fb = ISZERO v26f9_1
    0x26fc: v26fc(0x270d) = CONST 
    0x26ff: JUMPI v26fc(0x270d), v26fb

    Begin block 0x2700
    prev=[0x26f9], succ=[0x26f9]
    =================================
    0x2700: v2700(0x1) = CONST 
    0x2700_0x0: v2700_0 = PHI v26f7(0x0), v2702
    0x2700_0x1: v2700_1 = PHI v2706, v26d0arg0
    0x2702: v2702 = ADD v2700(0x1), v2700_0
    0x2703: v2703(0xa) = CONST 
    0x2706: v2706 = DIV v2700_1, v2703(0xa)
    0x2709: v2709(0x26f9) = CONST 
    0x270c: JUMP v2709(0x26f9)

    Begin block 0x270d
    prev=[0x26f9], succ=[0x2722, 0x2726]
    =================================
    0x270d_0x0: v270d_0 = PHI v26f7(0x0), v2702
    0x270e: v270e(0x0) = CONST 
    0x2711: v2711(0xffffffffffffffff) = CONST 
    0x271b: v271b = GT v270d_0, v2711(0xffffffffffffffff)
    0x271d: v271d = ISZERO v271b
    0x271e: v271e(0x2726) = CONST 
    0x2721: JUMPI v271e(0x2726), v271d

    Begin block 0x2722
    prev=[0x270d], succ=[]
    =================================
    0x2722: v2722(0x0) = CONST 
    0x2725: REVERT v2722(0x0), v2722(0x0)

    Begin block 0x2726
    prev=[0x270d], succ=[0x2745, 0x2751]
    =================================
    0x2726_0x1: v2726_1 = PHI v26f7(0x0), v2702
    0x2728: v2728(0x40) = CONST 
    0x272a: v272a = MLOAD v2728(0x40)
    0x272e: MSTORE v272a, v2726_1
    0x2730: v2730(0x1f) = CONST 
    0x2732: v2732 = ADD v2730(0x1f), v2726_1
    0x2733: v2733(0x1f) = CONST 
    0x2735: v2735(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2733(0x1f)
    0x2736: v2736 = AND v2735(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v2732
    0x2737: v2737(0x20) = CONST 
    0x2739: v2739 = ADD v2737(0x20), v2736
    0x273b: v273b = ADD v272a, v2739
    0x273c: v273c(0x40) = CONST 
    0x273e: MSTORE v273c(0x40), v273b
    0x2740: v2740 = ISZERO v2726_1
    0x2741: v2741(0x2751) = CONST 
    0x2744: JUMPI v2741(0x2751), v2740

    Begin block 0x2745
    prev=[0x2726], succ=[0x2751]
    =================================
    0x2745: v2745(0x20) = CONST 
    0x2745_0x0: v2745_0 = PHI v26f7(0x0), v2702
    0x2748: v2748 = ADD v272a, v2745(0x20)
    0x274b: v274b = CALLDATASIZE 
    0x274d: CALLDATACOPY v2748, v274b, v2745_0
    0x274e: v274e = ADD v2745_0, v2748

    Begin block 0x2751
    prev=[0x2745, 0x2726], succ=[0x2756]
    =================================

    Begin block 0x2756
    prev=[0x2751, 0x2785], succ=[0x275d, 0x27a9]
    =================================
    0x2756_0x5: v2756_5 = PHI v27a0, v26d0arg0
    0x2758: v2758 = ISZERO v2756_5
    0x2759: v2759(0x27a9) = CONST 
    0x275c: JUMPI v2759(0x27a9), v2758

    Begin block 0x275d
    prev=[0x2756], succ=[0x2784, 0x2785]
    =================================
    0x275d: v275d(0x0) = CONST 
    0x275d_0x0: v275d_0 = PHI v26f7(0x0), v2702, v2760
    0x275d_0x5: v275d_5 = PHI v27a0, v26d0arg0
    0x275f: v275f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v275d(0x0)
    0x2760: v2760 = ADD v275f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v275d_0
    0x2761: v2761(0x0) = CONST 
    0x2763: v2763(0xa) = CONST 
    0x2766: v2766 = DIV v275d_5, v2763(0xa)
    0x2767: v2767(0xa) = CONST 
    0x2769: v2769 = MUL v2767(0xa), v2766
    0x276b: v276b = SUB v275d_5, v2769
    0x276c: v276c(0x30) = CONST 
    0x276e: v276e = ADD v276c(0x30), v276b
    0x2771: v2771(0x0) = CONST 
    0x2774: v2774(0xf8) = CONST 
    0x2776: v2776 = SHL v2774(0xf8), v276e
    0x277d: v277d = MLOAD v272a
    0x277f: v277f = LT v2760, v277d
    0x2780: v2780(0x2785) = CONST 
    0x2783: JUMPI v2780(0x2785), v277f

    Begin block 0x2784
    prev=[0x275d], succ=[]
    =================================
    0x2784: THROW 

    Begin block 0x2785
    prev=[0x275d], succ=[0x2756]
    =================================
    0x2785_0xa: v2785_a = PHI v27a0, v26d0arg0
    0x2786: v2786(0x20) = CONST 
    0x2788: v2788 = ADD v2786(0x20), v2760
    0x2789: v2789 = ADD v2788, v272a
    0x278b: v278b(0x1) = CONST 
    0x278d: v278d(0x1) = CONST 
    0x278f: v278f(0xf8) = CONST 
    0x2791: v2791(0x100000000000000000000000000000000000000000000000000000000000000) = SHL v278f(0xf8), v278d(0x1)
    0x2792: v2792(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2791(0x100000000000000000000000000000000000000000000000000000000000000), v278b(0x1)
    0x2793: v2793(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v2792(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2794: v2794 = AND v2793(0xff00000000000000000000000000000000000000000000000000000000000000), v2776
    0x2797: v2797(0x0) = CONST 
    0x2799: v2799 = BYTE v2797(0x0), v2794
    0x279b: MSTORE8 v2789, v2799
    0x279d: v279d(0xa) = CONST 
    0x27a0: v27a0 = DIV v2785_a, v279d(0xa)
    0x27a5: v27a5(0x2756) = CONST 
    0x27a8: JUMP v27a5(0x2756)

    Begin block 0x27a9
    prev=[0x2756], succ=[]
    =================================
    0x27b1: RETURNPRIVATE v26d0arg1, v272a

    Begin block 0x26d8
    prev=[0x26d0], succ=[0x447d]
    =================================
    0x26d9: v26d9(0x40) = CONST 
    0x26dc: v26dc = MLOAD v26d9(0x40)
    0x26df: v26df = ADD v26d9(0x40), v26dc
    0x26e2: MSTORE v26d9(0x40), v26df
    0x26e3: v26e3(0x1) = CONST 
    0x26e6: MSTORE v26dc, v26e3(0x1)
    0x26e7: v26e7(0x3) = CONST 
    0x26e9: v26e9(0xfc) = CONST 
    0x26eb: v26eb(0x3000000000000000000000000000000000000000000000000000000000000000) = SHL v26e9(0xfc), v26e7(0x3)
    0x26ec: v26ec(0x20) = CONST 
    0x26ef: v26ef = ADD v26dc, v26ec(0x20)
    0x26f0: MSTORE v26ef, v26eb(0x3000000000000000000000000000000000000000000000000000000000000000)
    0x26f1: v26f1(0x447d) = CONST 
    0x26f4: JUMP v26f1(0x447d)

    Begin block 0x447d
    prev=[0x26d8], succ=[]
    =================================
    0x4481: RETURNPRIVATE v26d0arg1, v26dc

}

function 0x281f(0x281farg0x0, 0x281farg0x1, 0x281farg0x2, 0x281farg0x3, 0x281farg0x4, 0x281farg0x5, 0x281farg0x6) private {
    Begin block 0x281f
    prev=[], succ=[0x36a6B0x281f]
    =================================
    0x2820: v2820(0x2831) = CONST 
    0x2824: v2824(0x1) = CONST 
    0x2826: v2826(0x1) = CONST 
    0x2828: v2828(0xa0) = CONST 
    0x282a: v282a(0x10000000000000000000000000000000000000000) = SHL v2828(0xa0), v2826(0x1)
    0x282b: v282b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v282a(0x10000000000000000000000000000000000000000), v2824(0x1)
    0x282c: v282c = AND v282b(0xffffffffffffffffffffffffffffffffffffffff), v281farg3
    0x282d: v282d(0x36a6) = CONST 
    0x2830: JUMP v282d(0x36a6)

    Begin block 0x36a6B0x281f
    prev=[0x281f], succ=[0x2831]
    =================================
    0x36a7S0x281f: v36a7V281f = EXTCODESIZE v282c
    0x36a8S0x281f: v36a8V281f = ISZERO v36a7V281f
    0x36a9S0x281f: v36a9V281f = ISZERO v36a8V281f
    0x36abS0x281f: JUMP v2820(0x2831)

    Begin block 0x2831
    prev=[0x36a6B0x281f], succ=[0x44a1, 0x2837]
    =================================
    0x2832: v2832 = ISZERO v36a9V281f
    0x2833: v2833(0x44a1) = CONST 
    0x2836: JUMPI v2833(0x44a1), v2832

    Begin block 0x44a1
    prev=[0x2831], succ=[]
    =================================
    0x44a8: RETURNPRIVATE v281farg6

    Begin block 0x2837
    prev=[0x2831], succ=[0x28a7]
    =================================
    0x2838: v2838(0x1) = CONST 
    0x283a: v283a(0x1) = CONST 
    0x283c: v283c(0xa0) = CONST 
    0x283e: v283e(0x10000000000000000000000000000000000000000) = SHL v283c(0xa0), v283a(0x1)
    0x283f: v283f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v283e(0x10000000000000000000000000000000000000000), v2838(0x1)
    0x2840: v2840 = AND v283f(0xffffffffffffffffffffffffffffffffffffffff), v281farg3
    0x2841: v2841(0xbc197c81) = CONST 
    0x284b: v284b(0x40) = CONST 
    0x284d: v284d = MLOAD v284b(0x40)
    0x284f: v284f(0xffffffff) = CONST 
    0x2854: v2854(0xbc197c81) = AND v284f(0xffffffff), v2841(0xbc197c81)
    0x2855: v2855(0xe0) = CONST 
    0x2857: v2857(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v2855(0xe0), v2854(0xbc197c81)
    0x2859: MSTORE v284d, v2857(0xbc197c8100000000000000000000000000000000000000000000000000000000)
    0x285a: v285a(0x4) = CONST 
    0x285c: v285c = ADD v285a(0x4), v284d
    0x285f: v285f(0x1) = CONST 
    0x2861: v2861(0x1) = CONST 
    0x2863: v2863(0xa0) = CONST 
    0x2865: v2865(0x10000000000000000000000000000000000000000) = SHL v2863(0xa0), v2861(0x1)
    0x2866: v2866(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2865(0x10000000000000000000000000000000000000000), v285f(0x1)
    0x2867: v2867 = AND v2866(0xffffffffffffffffffffffffffffffffffffffff), v281farg5
    0x2869: MSTORE v285c, v2867
    0x286a: v286a(0x20) = CONST 
    0x286c: v286c = ADD v286a(0x20), v285c
    0x286e: v286e(0x1) = CONST 
    0x2870: v2870(0x1) = CONST 
    0x2872: v2872(0xa0) = CONST 
    0x2874: v2874(0x10000000000000000000000000000000000000000) = SHL v2872(0xa0), v2870(0x1)
    0x2875: v2875(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2874(0x10000000000000000000000000000000000000000), v286e(0x1)
    0x2876: v2876 = AND v2875(0xffffffffffffffffffffffffffffffffffffffff), v281farg4
    0x2878: MSTORE v286c, v2876
    0x2879: v2879(0x20) = CONST 
    0x287b: v287b = ADD v2879(0x20), v286c
    0x287d: v287d(0x20) = CONST 
    0x287f: v287f = ADD v287d(0x20), v287b
    0x2881: v2881(0x20) = CONST 
    0x2883: v2883 = ADD v2881(0x20), v287f
    0x2885: v2885(0x20) = CONST 
    0x2887: v2887 = ADD v2885(0x20), v2883
    0x288a: v288a(0xa0) = SUB v2887, v285c
    0x288c: MSTORE v287b, v288a(0xa0)
    0x2890: v2890 = MLOAD v281farg2
    0x2892: MSTORE v2887, v2890
    0x2893: v2893(0x20) = CONST 
    0x2895: v2895 = ADD v2893(0x20), v2887
    0x2899: v2899 = MLOAD v281farg2
    0x289b: v289b(0x20) = CONST 
    0x289d: v289d = ADD v289b(0x20), v281farg2
    0x289f: v289f(0x20) = CONST 
    0x28a1: v28a1 = MUL v289f(0x20), v2899
    0x28a5: v28a5(0x0) = CONST 

    Begin block 0x28a7
    prev=[0x2837, 0x28b0], succ=[0x28bf, 0x28b0]
    =================================
    0x28a7_0x0: v28a7_0 = PHI v28a5(0x0), v28ba
    0x28aa: v28aa = LT v28a7_0, v28a1
    0x28ab: v28ab = ISZERO v28aa
    0x28ac: v28ac(0x28bf) = CONST 
    0x28af: JUMPI v28ac(0x28bf), v28ab

    Begin block 0x28bf
    prev=[0x28a7], succ=[0x28e6]
    =================================
    0x28c6: v28c6 = ADD v28a1, v2895
    0x28c9: v28c9 = SUB v28c6, v285c
    0x28cb: MSTORE v287f, v28c9
    0x28cf: v28cf = MLOAD v281farg1
    0x28d1: MSTORE v28c6, v28cf
    0x28d2: v28d2(0x20) = CONST 
    0x28d4: v28d4 = ADD v28d2(0x20), v28c6
    0x28d8: v28d8 = MLOAD v281farg1
    0x28da: v28da(0x20) = CONST 
    0x28dc: v28dc = ADD v28da(0x20), v281farg1
    0x28de: v28de(0x20) = CONST 
    0x28e0: v28e0 = MUL v28de(0x20), v28d8
    0x28e4: v28e4(0x0) = CONST 

    Begin block 0x28e6
    prev=[0x28bf, 0x28ef], succ=[0x28fe, 0x28ef]
    =================================
    0x28e6_0x0: v28e6_0 = PHI v28e4(0x0), v28f9
    0x28e9: v28e9 = LT v28e6_0, v28e0
    0x28ea: v28ea = ISZERO v28e9
    0x28eb: v28eb(0x28fe) = CONST 
    0x28ee: JUMPI v28eb(0x28fe), v28ea

    Begin block 0x28fe
    prev=[0x28e6], succ=[0x2922]
    =================================
    0x2905: v2905 = ADD v28e0, v28d4
    0x2908: v2908 = SUB v2905, v285c
    0x290a: MSTORE v2883, v2908
    0x290e: v290e = MLOAD v281farg0
    0x2910: MSTORE v2905, v290e
    0x2911: v2911(0x20) = CONST 
    0x2913: v2913 = ADD v2911(0x20), v2905
    0x2917: v2917 = MLOAD v281farg0
    0x2919: v2919(0x20) = CONST 
    0x291b: v291b = ADD v2919(0x20), v281farg0
    0x2920: v2920(0x0) = CONST 

    Begin block 0x2922
    prev=[0x28fe, 0x292b], succ=[0x293a, 0x292b]
    =================================
    0x2922_0x0: v2922_0 = PHI v2920(0x0), v2935
    0x2925: v2925 = LT v2922_0, v2917
    0x2926: v2926 = ISZERO v2925
    0x2927: v2927(0x293a) = CONST 
    0x292a: JUMPI v2927(0x293a), v2926

    Begin block 0x293a
    prev=[0x2922], succ=[0x2967, 0x294e]
    =================================
    0x2943: v2943 = ADD v2917, v2913
    0x2945: v2945(0x1f) = CONST 
    0x2947: v2947 = AND v2945(0x1f), v2917
    0x2949: v2949 = ISZERO v2947
    0x294a: v294a(0x2967) = CONST 
    0x294d: JUMPI v294a(0x2967), v2949

    Begin block 0x2967
    prev=[0x293a, 0x294e], succ=[0x2988, 0x298c]
    =================================
    0x2967_0x1: v2967_1 = PHI v2943, v2964
    0x2973: v2973(0x20) = CONST 
    0x2975: v2975(0x40) = CONST 
    0x2977: v2977 = MLOAD v2975(0x40)
    0x297a: v297a = SUB v2967_1, v2977
    0x297c: v297c(0x0) = CONST 
    0x2980: v2980 = EXTCODESIZE v2840
    0x2981: v2981 = ISZERO v2980
    0x2983: v2983 = ISZERO v2981
    0x2984: v2984(0x298c) = CONST 
    0x2987: JUMPI v2984(0x298c), v2983

    Begin block 0x2988
    prev=[0x2967], succ=[]
    =================================
    0x2988: v2988(0x0) = CONST 
    0x298b: REVERT v2988(0x0), v2988(0x0)

    Begin block 0x298c
    prev=[0x2967], succ=[0x29b1, 0x299a]
    =================================
    0x298e: v298e = GAS 
    0x298f: v298f = CALL v298e, v2840, v297c(0x0), v2977, v297a, v2977, v2973(0x20)
    0x2995: v2995 = ISZERO v298f
    0x2996: v2996(0x29b1) = CONST 
    0x2999: JUMPI v2996(0x29b1), v2995

    Begin block 0x29b1
    prev=[0x298c, 0x29ac], succ=[0x29b6, 0x2a84]
    =================================
    0x29b1_0x0: v29b1_0 = PHI v298f, v29af(0x1)
    0x29b2: v29b2(0x2a84) = CONST 
    0x29b5: JUMPI v29b2(0x2a84), v29b1_0

    Begin block 0x29b6
    prev=[0x29b1], succ=[0x29bd0x281f]
    =================================
    0x29b6: v29b6(0x29bd) = CONST 
    0x29b9: v29b9(0x398b) = CONST 
    0x29bc: v29bc_0 = CALLPRIVATE v29b9(0x398b), v29b6(0x29bd)

    Begin block 0x29bd0x281f
    prev=[0x29b6], succ=[0x29c30x281f, 0x29c80x281f]
    =================================
    0x29bf0x281f: v281f29bf(0x29c8) = CONST 
    0x29c20x281f: JUMPI v281f29bf(0x29c8), v29bc_0

    Begin block 0x29c30x281f
    prev=[0x29bd0x281f], succ=[0x2a4d0x281f]
    =================================
    0x29c40x281f: v281f29c4(0x2a4d) = CONST 
    0x29c70x281f: JUMP v281f29c4(0x2a4d)

    Begin block 0x2a4d0x281f
    prev=[0x29c30x281f], succ=[]
    =================================
    0x2a4e0x281f: v281f2a4e(0x40) = CONST 
    0x2a500x281f: v281f2a50 = MLOAD v281f2a4e(0x40)
    0x2a510x281f: v281f2a51(0x461bcd) = CONST 
    0x2a550x281f: v281f2a55(0xe5) = CONST 
    0x2a570x281f: v281f2a57(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v281f2a55(0xe5), v281f2a51(0x461bcd)
    0x2a590x281f: MSTORE v281f2a50, v281f2a57(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a5a0x281f: v281f2a5a(0x4) = CONST 
    0x2a5c0x281f: v281f2a5c = ADD v281f2a5a(0x4), v281f2a50
    0x2a5f0x281f: v281f2a5f(0x20) = CONST 
    0x2a610x281f: v281f2a61 = ADD v281f2a5f(0x20), v281f2a5c
    0x2a640x281f: v281f2a64(0x20) = SUB v281f2a61, v281f2a5c
    0x2a660x281f: MSTORE v281f2a5c, v281f2a64(0x20)
    0x2a670x281f: v281f2a67(0x2b) = CONST 
    0x2a6a0x281f: MSTORE v281f2a61, v281f2a67(0x2b)
    0x2a6b0x281f: v281f2a6b(0x20) = CONST 
    0x2a6d0x281f: v281f2a6d = ADD v281f2a6b(0x20), v281f2a61
    0x2a6f0x281f: v281f2a6f(0x3a55) = CONST 
    0x2a720x281f: v281f2a72(0x2b) = CONST 
    0x2a750x281f: CODECOPY v281f2a6d, v281f2a6f(0x3a55), v281f2a72(0x2b)
    0x2a760x281f: v281f2a76(0x40) = CONST 
    0x2a780x281f: v281f2a78 = ADD v281f2a76(0x40), v281f2a6d
    0x2a7c0x281f: v281f2a7c(0x40) = CONST 
    0x2a7e0x281f: v281f2a7e = MLOAD v281f2a7c(0x40)
    0x2a810x281f: v281f2a81(0x84) = SUB v281f2a78, v281f2a7e
    0x2a830x281f: REVERT v281f2a7e, v281f2a81(0x84)

    Begin block 0x29c80x281f
    prev=[0x29bd0x281f], succ=[0x29fa0x281f]
    =================================
    0x29ca0x281f: v281f29ca(0x40) = CONST 
    0x29cc0x281f: v281f29cc = MLOAD v281f29ca(0x40)
    0x29cd0x281f: v281f29cd(0x461bcd) = CONST 
    0x29d10x281f: v281f29d1(0xe5) = CONST 
    0x29d30x281f: v281f29d3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v281f29d1(0xe5), v281f29cd(0x461bcd)
    0x29d50x281f: MSTORE v281f29cc, v281f29d3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29d60x281f: v281f29d6(0x4) = CONST 
    0x29d80x281f: v281f29d8 = ADD v281f29d6(0x4), v281f29cc
    0x29db0x281f: v281f29db(0x20) = CONST 
    0x29dd0x281f: v281f29dd = ADD v281f29db(0x20), v281f29d8
    0x29e00x281f: v281f29e0(0x20) = SUB v281f29dd, v281f29d8
    0x29e20x281f: MSTORE v281f29d8, v281f29e0(0x20)
    0x29e60x281f: v281f29e6 = MLOAD v29bc_0
    0x29e80x281f: MSTORE v281f29dd, v281f29e6
    0x29e90x281f: v281f29e9(0x20) = CONST 
    0x29eb0x281f: v281f29eb = ADD v281f29e9(0x20), v281f29dd
    0x29ef0x281f: v281f29ef = MLOAD v29bc_0
    0x29f10x281f: v281f29f1(0x20) = CONST 
    0x29f30x281f: v281f29f3 = ADD v281f29f1(0x20), v29bc_0
    0x29f80x281f: v281f29f8(0x0) = CONST 

    Begin block 0x29fa0x281f
    prev=[0x2a030x281f, 0x29c80x281f], succ=[0x2a120x281f, 0x2a030x281f]
    =================================
    0x29fa0x281f_0x0: v29fa281f_0 = PHI v281f2a0d, v281f29f8(0x0)
    0x29fd0x281f: v281f29fd = LT v29fa281f_0, v281f29ef
    0x29fe0x281f: v281f29fe = ISZERO v281f29fd
    0x29ff0x281f: v281f29ff(0x2a12) = CONST 
    0x2a020x281f: JUMPI v281f29ff(0x2a12), v281f29fe

    Begin block 0x2a120x281f
    prev=[0x29fa0x281f], succ=[0x2a3f0x281f, 0x2a260x281f]
    =================================
    0x2a1b0x281f: v281f2a1b = ADD v281f29ef, v281f29eb
    0x2a1d0x281f: v281f2a1d(0x1f) = CONST 
    0x2a1f0x281f: v281f2a1f = AND v281f2a1d(0x1f), v281f29ef
    0x2a210x281f: v281f2a21 = ISZERO v281f2a1f
    0x2a220x281f: v281f2a22(0x2a3f) = CONST 
    0x2a250x281f: JUMPI v281f2a22(0x2a3f), v281f2a21

    Begin block 0x2a3f0x281f
    prev=[0x2a120x281f, 0x2a260x281f], succ=[]
    =================================
    0x2a3f0x281f_0x1: v2a3f281f_1 = PHI v281f2a3c, v281f2a1b
    0x2a450x281f: v281f2a45(0x40) = CONST 
    0x2a470x281f: v281f2a47 = MLOAD v281f2a45(0x40)
    0x2a4a0x281f: v281f2a4a = SUB v2a3f281f_1, v281f2a47
    0x2a4c0x281f: REVERT v281f2a47, v281f2a4a

    Begin block 0x2a260x281f
    prev=[0x2a120x281f], succ=[0x2a3f0x281f]
    =================================
    0x2a280x281f: v281f2a28 = SUB v281f2a1b, v281f2a1f
    0x2a2a0x281f: v281f2a2a = MLOAD v281f2a28
    0x2a2b0x281f: v281f2a2b(0x1) = CONST 
    0x2a2e0x281f: v281f2a2e(0x20) = CONST 
    0x2a300x281f: v281f2a30 = SUB v281f2a2e(0x20), v281f2a1f
    0x2a310x281f: v281f2a31(0x100) = CONST 
    0x2a340x281f: v281f2a34 = EXP v281f2a31(0x100), v281f2a30
    0x2a350x281f: v281f2a35 = SUB v281f2a34, v281f2a2b(0x1)
    0x2a360x281f: v281f2a36 = NOT v281f2a35
    0x2a370x281f: v281f2a37 = AND v281f2a36, v281f2a2a
    0x2a390x281f: MSTORE v281f2a28, v281f2a37
    0x2a3a0x281f: v281f2a3a(0x20) = CONST 
    0x2a3c0x281f: v281f2a3c = ADD v281f2a3a(0x20), v281f2a28

    Begin block 0x2a030x281f
    prev=[0x29fa0x281f], succ=[0x29fa0x281f]
    =================================
    0x2a030x281f_0x0: v2a03281f_0 = PHI v281f2a0d, v281f29f8(0x0)
    0x2a050x281f: v281f2a05 = ADD v2a03281f_0, v281f29f3
    0x2a060x281f: v281f2a06 = MLOAD v281f2a05
    0x2a090x281f: v281f2a09 = ADD v2a03281f_0, v281f29eb
    0x2a0a0x281f: MSTORE v281f2a09, v281f2a06
    0x2a0b0x281f: v281f2a0b(0x20) = CONST 
    0x2a0d0x281f: v281f2a0d = ADD v281f2a0b(0x20), v2a03281f_0
    0x2a0e0x281f: v281f2a0e(0x29fa) = CONST 
    0x2a110x281f: JUMP v281f2a0e(0x29fa)

    Begin block 0x2a84
    prev=[0x29b1], succ=[0x2a9d, 0x2ae90x281f]
    =================================
    0x2a84_0x0: v2a84_0 = PHI v29ae, v281farg0
    0x2a85: v2a85(0x1) = CONST 
    0x2a87: v2a87(0x1) = CONST 
    0x2a89: v2a89(0xe0) = CONST 
    0x2a8b: v2a8b(0x100000000000000000000000000000000000000000000000000000000) = SHL v2a89(0xe0), v2a87(0x1)
    0x2a8c: v2a8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2a8b(0x100000000000000000000000000000000000000000000000000000000), v2a85(0x1)
    0x2a8d: v2a8d(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2a8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2a8f: v2a8f = AND v2a84_0, v2a8d(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x2a90: v2a90(0xbc197c81) = CONST 
    0x2a95: v2a95(0xe0) = CONST 
    0x2a97: v2a97(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v2a95(0xe0), v2a90(0xbc197c81)
    0x2a98: v2a98 = EQ v2a97(0xbc197c8100000000000000000000000000000000000000000000000000000000), v2a8f
    0x2a99: v2a99(0x2ae9) = CONST 
    0x2a9c: JUMPI v2a99(0x2ae9), v2a98

    Begin block 0x2a9d
    prev=[0x2a84], succ=[]
    =================================
    0x2a9d: v2a9d(0x40) = CONST 
    0x2aa0: v2aa0 = MLOAD v2a9d(0x40)
    0x2aa1: v2aa1(0x461bcd) = CONST 
    0x2aa5: v2aa5(0xe5) = CONST 
    0x2aa7: v2aa7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2aa5(0xe5), v2aa1(0x461bcd)
    0x2aa9: MSTORE v2aa0, v2aa7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2aaa: v2aaa(0x20) = CONST 
    0x2aac: v2aac(0x4) = CONST 
    0x2aaf: v2aaf = ADD v2aa0, v2aac(0x4)
    0x2ab0: MSTORE v2aaf, v2aaa(0x20)
    0x2ab1: v2ab1(0x1f) = CONST 
    0x2ab3: v2ab3(0x24) = CONST 
    0x2ab6: v2ab6 = ADD v2aa0, v2ab3(0x24)
    0x2ab7: MSTORE v2ab6, v2ab1(0x1f)
    0x2ab8: v2ab8(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x2ad9: v2ad9(0x44) = CONST 
    0x2adc: v2adc = ADD v2aa0, v2ad9(0x44)
    0x2add: MSTORE v2adc, v2ab8(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x2adf: v2adf = MLOAD v2a9d(0x40)
    0x2ae3: v2ae3(0x0) = SUB v2aa0, v2adf
    0x2ae4: v2ae4(0x64) = CONST 
    0x2ae6: v2ae6(0x64) = ADD v2ae4(0x64), v2ae3(0x0)
    0x2ae8: REVERT v2adf, v2ae6(0x64)

    Begin block 0x2ae90x281f
    prev=[0x2a84], succ=[0x2aeb0x281f]
    =================================

    Begin block 0x2aeb0x281f
    prev=[0x2ae90x281f], succ=[]
    =================================
    0x2af20x281f: RETURNPRIVATE v281farg6

    Begin block 0x299a
    prev=[0x298c], succ=[0x29a8, 0x29ac]
    =================================
    0x299b: v299b(0x40) = CONST 
    0x299d: v299d = MLOAD v299b(0x40)
    0x299e: v299e = RETURNDATASIZE 
    0x299f: v299f(0x20) = CONST 
    0x29a2: v29a2 = LT v299e, v299f(0x20)
    0x29a3: v29a3 = ISZERO v29a2
    0x29a4: v29a4(0x29ac) = CONST 
    0x29a7: JUMPI v29a4(0x29ac), v29a3

    Begin block 0x29a8
    prev=[0x299a], succ=[]
    =================================
    0x29a8: v29a8(0x0) = CONST 
    0x29ab: REVERT v29a8(0x0), v29a8(0x0)

    Begin block 0x29ac
    prev=[0x299a], succ=[0x29b1]
    =================================
    0x29ae: v29ae = MLOAD v299d
    0x29af: v29af(0x1) = CONST 

    Begin block 0x294e
    prev=[0x293a], succ=[0x2967]
    =================================
    0x2950: v2950 = SUB v2943, v2947
    0x2952: v2952 = MLOAD v2950
    0x2953: v2953(0x1) = CONST 
    0x2956: v2956(0x20) = CONST 
    0x2958: v2958 = SUB v2956(0x20), v2947
    0x2959: v2959(0x100) = CONST 
    0x295c: v295c = EXP v2959(0x100), v2958
    0x295d: v295d = SUB v295c, v2953(0x1)
    0x295e: v295e = NOT v295d
    0x295f: v295f = AND v295e, v2952
    0x2961: MSTORE v2950, v295f
    0x2962: v2962(0x20) = CONST 
    0x2964: v2964 = ADD v2962(0x20), v2950

    Begin block 0x292b
    prev=[0x2922], succ=[0x2922]
    =================================
    0x292b_0x0: v292b_0 = PHI v2920(0x0), v2935
    0x292d: v292d = ADD v292b_0, v291b
    0x292e: v292e = MLOAD v292d
    0x2931: v2931 = ADD v292b_0, v2913
    0x2932: MSTORE v2931, v292e
    0x2933: v2933(0x20) = CONST 
    0x2935: v2935 = ADD v2933(0x20), v292b_0
    0x2936: v2936(0x2922) = CONST 
    0x2939: JUMP v2936(0x2922)

    Begin block 0x28ef
    prev=[0x28e6], succ=[0x28e6]
    =================================
    0x28ef_0x0: v28ef_0 = PHI v28e4(0x0), v28f9
    0x28f1: v28f1 = ADD v28ef_0, v28dc
    0x28f2: v28f2 = MLOAD v28f1
    0x28f5: v28f5 = ADD v28ef_0, v28d4
    0x28f6: MSTORE v28f5, v28f2
    0x28f7: v28f7(0x20) = CONST 
    0x28f9: v28f9 = ADD v28f7(0x20), v28ef_0
    0x28fa: v28fa(0x28e6) = CONST 
    0x28fd: JUMP v28fa(0x28e6)

    Begin block 0x28b0
    prev=[0x28a7], succ=[0x28a7]
    =================================
    0x28b0_0x0: v28b0_0 = PHI v28a5(0x0), v28ba
    0x28b2: v28b2 = ADD v28b0_0, v289d
    0x28b3: v28b3 = MLOAD v28b2
    0x28b6: v28b6 = ADD v28b0_0, v2895
    0x28b7: MSTORE v28b6, v28b3
    0x28b8: v28b8(0x20) = CONST 
    0x28ba: v28ba = ADD v28b8(0x20), v28b0_0
    0x28bb: v28bb(0x28a7) = CONST 
    0x28be: JUMP v28bb(0x28a7)

}

function setURI(string)() public {
    Begin block 0x299
    prev=[], succ=[0x2ab, 0x2af]
    =================================
    0x29a: v29a(0x3e05) = CONST 
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
    prev=[0xeaf], succ=[0x3835B0xf09]
    =================================
    0xf0b: vf0b = MLOAD v30f
    0xf0c: vf0c(0x4273) = CONST 
    0xf10: vf10(0x2) = CONST 
    0xf13: vf13(0x20) = CONST 
    0xf16: vf16 = ADD v30f, vf13(0x20)
    0xf18: vf18(0x3835) = CONST 
    0xf1b: JUMP vf18(0x3835)

    Begin block 0x3835B0xf09
    prev=[0xf09], succ=[0x3863B0xf09, 0x386bB0xf09]
    =================================
    0x3838S0xf09: v3838Vf09 = SLOAD vf10(0x2)
    0x3839S0xf09: v3839Vf09(0x1) = CONST 
    0x383cS0xf09: v383cVf09(0x1) = CONST 
    0x383eS0xf09: v383eVf09 = AND v383cVf09(0x1), v3838Vf09
    0x383fS0xf09: v383fVf09 = ISZERO v383eVf09
    0x3840S0xf09: v3840Vf09(0x100) = CONST 
    0x3843S0xf09: v3843Vf09 = MUL v3840Vf09(0x100), v383fVf09
    0x3844S0xf09: v3844Vf09 = SUB v3843Vf09, v3839Vf09(0x1)
    0x3845S0xf09: v3845Vf09 = AND v3844Vf09, v3838Vf09
    0x3846S0xf09: v3846Vf09(0x2) = CONST 
    0x3849S0xf09: v3849Vf09 = DIV v3845Vf09, v3846Vf09(0x2)
    0x384bS0xf09: v384bVf09(0x0) = CONST 
    0x384dS0xf09: MSTORE v384bVf09(0x0), vf10(0x2)
    0x384eS0xf09: v384eVf09(0x20) = CONST 
    0x3850S0xf09: v3850Vf09(0x0) = CONST 
    0x3852S0xf09: v3852Vf09 = SHA3 v3850Vf09(0x0), v384eVf09(0x20)
    0x3854S0xf09: v3854Vf09(0x1f) = CONST 
    0x3856S0xf09: v3856Vf09 = ADD v3854Vf09(0x1f), v3849Vf09
    0x3857S0xf09: v3857Vf09(0x20) = CONST 
    0x385aS0xf09: v385aVf09 = DIV v3856Vf09, v3857Vf09(0x20)
    0x385cS0xf09: v385cVf09 = ADD v3852Vf09, v385aVf09
    0x385fS0xf09: v385fVf09(0x386b) = CONST 
    0x3862S0xf09: JUMPI v385fVf09(0x386b), vf0b

    Begin block 0x3863B0xf09
    prev=[0x3835B0xf09], succ=[0x38b10x3835B0xf09]
    =================================
    0x3863S0xf09: v3863Vf09(0x0) = CONST 
    0x3866S0xf09: SSTORE vf10(0x2), v3863Vf09(0x0)
    0x3867S0xf09: v3867Vf09(0x38b1) = CONST 
    0x386aS0xf09: JUMP v3867Vf09(0x38b1)

    Begin block 0x38b10x3835B0xf09
    prev=[0x3863B0xf09, 0x3884B0xf09, 0x3896B0xf09, 0x3874B0xf09], succ=[0x3970B0x38b10x3835B0xf09]
    =================================
    0x38b10x3835_0x1S0xf09: v38b13835_1Vf09 = PHI v3852Vf09, v38abVf09
    0x38b30x3835S0xf09: v383538b3Vf09(0x45ac) = CONST 
    0x38b90x3835S0xf09: v383538b9Vf09(0x3970) = CONST 
    0x38bc0x3835S0xf09: JUMP v383538b9Vf09(0x3970)

    Begin block 0x3970B0x38b10x3835B0xf09
    prev=[0x38b10x3835B0xf09], succ=[0x3971B0x38b10x3835B0xf09]
    =================================

    Begin block 0x3971B0x38b10x3835B0xf09
    prev=[0x397aB0x38b10x3835B0xf09, 0x3970B0x38b10x3835B0xf09], succ=[0x397aB0x38b10x3835B0xf09, 0x45cfB0x38b10x3835B0xf09]
    =================================
    0x3971_0x0S0x38b10x3835S0xf09: v3971_0V38b13835Vf09 = PHI v38b13835_1Vf09, v3980V38b13835Vf09
    0x3974S0x38b10x3835S0xf09: v3974V38b13835Vf09 = GT v385cVf09, v3971_0V38b13835Vf09
    0x3975S0x38b10x3835S0xf09: v3975V38b13835Vf09 = ISZERO v3974V38b13835Vf09
    0x3976S0x38b10x3835S0xf09: v3976V38b13835Vf09(0x45cf) = CONST 
    0x3979S0x38b10x3835S0xf09: JUMPI v3976V38b13835Vf09(0x45cf), v3975V38b13835Vf09

    Begin block 0x397aB0x38b10x3835B0xf09
    prev=[0x3971B0x38b10x3835B0xf09], succ=[0x3971B0x38b10x3835B0xf09]
    =================================
    0x397aS0x38b10x3835S0xf09: v397aV38b13835Vf09(0x0) = CONST 
    0x397a_0x0S0x38b10x3835S0xf09: v397a_0V38b13835Vf09 = PHI v38b13835_1Vf09, v3980V38b13835Vf09
    0x397dS0x38b10x3835S0xf09: SSTORE v397a_0V38b13835Vf09, v397aV38b13835Vf09(0x0)
    0x397eS0x38b10x3835S0xf09: v397eV38b13835Vf09(0x1) = CONST 
    0x3980S0x38b10x3835S0xf09: v3980V38b13835Vf09 = ADD v397eV38b13835Vf09(0x1), v397a_0V38b13835Vf09
    0x3981S0x38b10x3835S0xf09: v3981V38b13835Vf09(0x3971) = CONST 
    0x3984S0x38b10x3835S0xf09: JUMP v3981V38b13835Vf09(0x3971)

    Begin block 0x45cfB0x38b10x3835B0xf09
    prev=[0x3971B0x38b10x3835B0xf09], succ=[0x45ac0x3835B0xf09]
    =================================
    0x45d2S0x38b10x3835S0xf09: JUMP v383538b3Vf09(0x45ac)

    Begin block 0x45ac0x3835B0xf09
    prev=[0x45cfB0x38b10x3835B0xf09], succ=[0x4273]
    =================================
    0x45af0x3835S0xf09: JUMP vf0c(0x4273)

    Begin block 0x4273
    prev=[0x45ac0x3835B0xf09], succ=[0x3e05]
    =================================
    0x4276: JUMP v29a(0x3e05)

    Begin block 0x3e05
    prev=[0x4273], succ=[]
    =================================
    0x3e06: STOP 

    Begin block 0x386bB0xf09
    prev=[0x3835B0xf09], succ=[0x3884B0xf09, 0x3874B0xf09]
    =================================
    0x386dS0xf09: v386dVf09(0x1f) = CONST 
    0x386fS0xf09: v386fVf09 = LT v386dVf09(0x1f), vf0b
    0x3870S0xf09: v3870Vf09(0x3884) = CONST 
    0x3873S0xf09: JUMPI v3870Vf09(0x3884), v386fVf09

    Begin block 0x3884B0xf09
    prev=[0x386bB0xf09], succ=[0x3893B0xf09, 0x38b10x3835B0xf09]
    =================================
    0x3887S0xf09: v3887Vf09 = ADD vf0b, vf0b
    0x3888S0xf09: v3888Vf09(0x1) = CONST 
    0x388aS0xf09: v388aVf09 = ADD v3888Vf09(0x1), v3887Vf09
    0x388cS0xf09: SSTORE vf10(0x2), v388aVf09
    0x388eS0xf09: v388eVf09 = ISZERO vf0b
    0x388fS0xf09: v388fVf09(0x38b1) = CONST 
    0x3892S0xf09: JUMPI v388fVf09(0x38b1), v388eVf09

    Begin block 0x3893B0xf09
    prev=[0x3884B0xf09], succ=[0x3896B0xf09]
    =================================
    0x3895S0xf09: v3895Vf09 = ADD vf16, vf0b

    Begin block 0x3896B0xf09
    prev=[0x3893B0xf09, 0x389fB0xf09], succ=[0x389fB0xf09, 0x38b10x3835B0xf09]
    =================================
    0x3896_0x2S0xf09: v3896_2Vf09 = PHI vf16, v38a6Vf09
    0x3899S0xf09: v3899Vf09 = GT v3895Vf09, v3896_2Vf09
    0x389aS0xf09: v389aVf09 = ISZERO v3899Vf09
    0x389bS0xf09: v389bVf09(0x38b1) = CONST 
    0x389eS0xf09: JUMPI v389bVf09(0x38b1), v389aVf09

    Begin block 0x389fB0xf09
    prev=[0x3896B0xf09], succ=[0x3896B0xf09]
    =================================
    0x389f_0x1S0xf09: v389f_1Vf09 = PHI v3852Vf09, v38abVf09
    0x389f_0x2S0xf09: v389f_2Vf09 = PHI vf16, v38a6Vf09
    0x38a0S0xf09: v38a0Vf09 = MLOAD v389f_2Vf09
    0x38a2S0xf09: SSTORE v389f_1Vf09, v38a0Vf09
    0x38a4S0xf09: v38a4Vf09(0x20) = CONST 
    0x38a6S0xf09: v38a6Vf09 = ADD v38a4Vf09(0x20), v389f_2Vf09
    0x38a9S0xf09: v38a9Vf09(0x1) = CONST 
    0x38abS0xf09: v38abVf09 = ADD v38a9Vf09(0x1), v389f_1Vf09
    0x38adS0xf09: v38adVf09(0x3896) = CONST 
    0x38b0S0xf09: JUMP v38adVf09(0x3896)

    Begin block 0x3874B0xf09
    prev=[0x386bB0xf09], succ=[0x38b10x3835B0xf09]
    =================================
    0x3875S0xf09: v3875Vf09 = MLOAD vf16
    0x3876S0xf09: v3876Vf09(0xff) = CONST 
    0x3878S0xf09: v3878Vf09(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v3876Vf09(0xff)
    0x3879S0xf09: v3879Vf09 = AND v3878Vf09(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v3875Vf09
    0x387cS0xf09: v387cVf09 = ADD vf0b, vf0b
    0x387dS0xf09: v387dVf09 = OR v387cVf09, v3879Vf09
    0x387fS0xf09: SSTORE vf10(0x2), v387dVf09
    0x3880S0xf09: v3880Vf09(0x38b1) = CONST 
    0x3883S0xf09: JUMP v3880Vf09(0x38b1)

}

function 0x2af3(0x2af3arg0x0, 0x2af3arg0x1, 0x2af3arg0x2) private {
    Begin block 0x2af3
    prev=[], succ=[0x2b04, 0x2b50]
    =================================
    0x2af4: v2af4(0x0) = CONST 
    0x2af6: v2af6(0x1) = CONST 
    0x2af8: v2af8(0x1) = CONST 
    0x2afa: v2afa(0xa0) = CONST 
    0x2afc: v2afc(0x10000000000000000000000000000000000000000) = SHL v2afa(0xa0), v2af8(0x1)
    0x2afd: v2afd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2afc(0x10000000000000000000000000000000000000000), v2af6(0x1)
    0x2aff: v2aff = AND v2af3arg1, v2afd(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b00: v2b00(0x2b50) = CONST 
    0x2b03: JUMPI v2b00(0x2b50), v2aff

    Begin block 0x2b04
    prev=[0x2af3], succ=[]
    =================================
    0x2b04: v2b04(0x40) = CONST 
    0x2b07: v2b07 = MLOAD v2b04(0x40)
    0x2b08: v2b08(0x461bcd) = CONST 
    0x2b0c: v2b0c(0xe5) = CONST 
    0x2b0e: v2b0e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2b0c(0xe5), v2b08(0x461bcd)
    0x2b10: MSTORE v2b07, v2b0e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2b11: v2b11(0x20) = CONST 
    0x2b13: v2b13(0x4) = CONST 
    0x2b16: v2b16 = ADD v2b07, v2b13(0x4)
    0x2b17: MSTORE v2b16, v2b11(0x20)
    0x2b18: v2b18(0x1d) = CONST 
    0x2b1a: v2b1a(0x24) = CONST 
    0x2b1d: v2b1d = ADD v2b07, v2b1a(0x24)
    0x2b1e: MSTORE v2b1d, v2b18(0x1d)
    0x2b1f: v2b1f(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x2b40: v2b40(0x44) = CONST 
    0x2b43: v2b43 = ADD v2b07, v2b40(0x44)
    0x2b44: MSTORE v2b43, v2b1f(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x2b46: v2b46 = MLOAD v2b04(0x40)
    0x2b4a: v2b4a(0x0) = SUB v2b07, v2b46
    0x2b4b: v2b4b(0x64) = CONST 
    0x2b4d: v2b4d(0x64) = ADD v2b4b(0x64), v2b4a(0x0)
    0x2b4f: REVERT v2b46, v2b4d(0x64)

    Begin block 0x2b50
    prev=[0x2af3], succ=[0x44c8]
    =================================
    0x2b51: v2b51(0x7) = CONST 
    0x2b54: v2b54 = SLOAD v2b51(0x7)
    0x2b55: v2b55(0x1) = CONST 
    0x2b59: v2b59 = ADD v2b55(0x1), v2b54
    0x2b5d: SSTORE v2b51(0x7), v2b59
    0x2b5e: v2b5e(0x0) = CONST 
    0x2b62: MSTORE v2b5e(0x0), v2b59
    0x2b63: v2b63(0x8) = CONST 
    0x2b65: v2b65(0x20) = CONST 
    0x2b69: MSTORE v2b65(0x20), v2b63(0x8)
    0x2b6a: v2b6a(0x40) = CONST 
    0x2b6e: v2b6e = SHA3 v2b5e(0x0), v2b6a(0x40)
    0x2b70: v2b70 = SLOAD v2b6e
    0x2b71: v2b71(0x1) = CONST 
    0x2b73: v2b73(0x1) = CONST 
    0x2b75: v2b75(0xa0) = CONST 
    0x2b77: v2b77(0x10000000000000000000000000000000000000000) = SHL v2b75(0xa0), v2b73(0x1)
    0x2b78: v2b78(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b77(0x10000000000000000000000000000000000000000), v2b71(0x1)
    0x2b7b: v2b7b = AND v2af3arg1, v2b78(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b7c: v2b7c(0x1) = CONST 
    0x2b7e: v2b7e(0x1) = CONST 
    0x2b80: v2b80(0xa0) = CONST 
    0x2b82: v2b82(0x10000000000000000000000000000000000000000) = SHL v2b80(0xa0), v2b7e(0x1)
    0x2b83: v2b83(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b82(0x10000000000000000000000000000000000000000), v2b7c(0x1)
    0x2b84: v2b84(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2b83(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b87: v2b87 = AND v2b84(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2b70
    0x2b89: v2b89 = OR v2b7b, v2b87
    0x2b8c: SSTORE v2b6e, v2b89
    0x2b8e: v2b8e = MLOAD v2b6a(0x40)
    0x2b8f: v2b8f(0x60) = CONST 
    0x2b92: v2b92 = ADD v2b8e, v2b8f(0x60)
    0x2b94: MSTORE v2b6a(0x40), v2b92
    0x2b95: v2b95(0x1) = CONST 
    0x2b97: v2b97(0x1) = CONST 
    0x2b99: v2b99(0x80) = CONST 
    0x2b9b: v2b9b(0x100000000000000000000000000000000) = SHL v2b99(0x80), v2b97(0x1)
    0x2b9c: v2b9c(0xffffffffffffffffffffffffffffffff) = SUB v2b9b(0x100000000000000000000000000000000), v2b95(0x1)
    0x2b9d: v2b9d = NUMBER 
    0x2b9f: v2b9f = AND v2b9c(0xffffffffffffffffffffffffffffffff), v2b9d
    0x2ba1: MSTORE v2b8e, v2b9f
    0x2ba4: v2ba4 = AND v2b9c(0xffffffffffffffffffffffffffffffff), v2af3arg0
    0x2ba7: v2ba7 = ADD v2b65(0x20), v2b8e
    0x2baa: MSTORE v2ba7, v2ba4
    0x2bad: v2bad = ADD v2b6a(0x40), v2b8e
    0x2bb0: MSTORE v2bad, v2b7b
    0x2bb3: MSTORE v2b5e(0x0), v2b59
    0x2bb4: v2bb4(0xa) = CONST 
    0x2bb7: MSTORE v2b65(0x20), v2bb4(0xa)
    0x2bba: v2bba = SHA3 v2b5e(0x0), v2b6a(0x40)
    0x2bbc: v2bbc = MLOAD v2b8e
    0x2bbe: v2bbe = SLOAD v2bba
    0x2bc0: v2bc0 = MLOAD v2ba7
    0x2bc2: v2bc2 = AND v2b9c(0xffffffffffffffffffffffffffffffff), v2bc0
    0x2bc3: v2bc3(0x1) = CONST 
    0x2bc5: v2bc5(0x80) = CONST 
    0x2bc7: v2bc7(0x100000000000000000000000000000000) = SHL v2bc5(0x80), v2bc3(0x1)
    0x2bc8: v2bc8 = MUL v2bc7(0x100000000000000000000000000000000), v2bc2
    0x2bcb: v2bcb = AND v2b9c(0xffffffffffffffffffffffffffffffff), v2bbc
    0x2bcc: v2bcc(0x1) = CONST 
    0x2bce: v2bce(0x1) = CONST 
    0x2bd0: v2bd0(0x80) = CONST 
    0x2bd2: v2bd2(0x100000000000000000000000000000000) = SHL v2bd0(0x80), v2bce(0x1)
    0x2bd3: v2bd3(0xffffffffffffffffffffffffffffffff) = SUB v2bd2(0x100000000000000000000000000000000), v2bcc(0x1)
    0x2bd4: v2bd4(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) = NOT v2bd3(0xffffffffffffffffffffffffffffffff)
    0x2bd7: v2bd7 = AND v2bbe, v2bd4(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000)
    0x2bdb: v2bdb = OR v2bd7, v2bcb
    0x2bde: v2bde = AND v2b9c(0xffffffffffffffffffffffffffffffff), v2bdb
    0x2bdf: v2bdf = OR v2bde, v2bc8
    0x2be1: SSTORE v2bba, v2bdf
    0x2be2: v2be2 = MLOAD v2bad
    0x2be5: v2be5 = ADD v2b55(0x1), v2bba
    0x2be7: v2be7 = SLOAD v2be5
    0x2beb: v2beb = AND v2b78(0xffffffffffffffffffffffffffffffffffffffff), v2be2
    0x2bed: v2bed = AND v2b84(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2be7
    0x2bf1: v2bf1 = OR v2bed, v2beb
    0x2bf3: SSTORE v2be5, v2bf1
    0x2bf5: v2bf5 = MLOAD v2b6a(0x40)
    0x2bf8: MSTORE v2bf5, v2b59
    0x2bfb: v2bfb = ADD v2bf5, v2b65(0x20)
    0x2bff: MSTORE v2bfb, v2b55(0x1)
    0x2c01: v2c01 = MLOAD v2b6a(0x40)
    0x2c02: v2c02 = CALLER 
    0x2c04: v2c04(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x2c29: v2c29(0x0) = SUB v2bf5, v2c01
    0x2c2a: v2c2a(0x40) = ADD v2c29(0x0), v2b6a(0x40)
    0x2c2c: LOG4 v2c01, v2c2a(0x40), v2c04(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v2c02, v2b5e(0x0), v2b7b
    0x2c2d: v2c2d(0x44c8) = CONST 
    0x2c30: v2c30 = CALLER 
    0x2c31: v2c31(0x0) = CONST 
    0x2c35: v2c35(0x1) = CONST 
    0x2c37: v2c37(0x40) = CONST 
    0x2c39: v2c39 = MLOAD v2c37(0x40)
    0x2c3b: v2c3b(0x20) = CONST 
    0x2c3d: v2c3d = ADD v2c3b(0x20), v2c39
    0x2c3e: v2c3e(0x40) = CONST 
    0x2c40: MSTORE v2c3e(0x40), v2c3d
    0x2c42: v2c42(0x0) = CONST 
    0x2c45: MSTORE v2c39, v2c42(0x0)
    0x2c47: v2c47(0x351f) = CONST 
    0x2c4a: CALLPRIVATE v2c47(0x351f), v2c39, v2c35(0x1), v2b59, v2af3arg1, v2c31(0x0), v2c30, v2c2d(0x44c8)

    Begin block 0x44c8
    prev=[0x2b50], succ=[]
    =================================
    0x44ce: RETURNPRIVATE v2af3arg2, v2b59

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
    0xfac: vfac(0x26d0) = CONST 
    0xfaf: vfaf_0 = CALLPRIVATE vfac(0x26d0), v357, vfa8(0xfb0)

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
    prev=[0x101b], succ=[0x42ba]
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
    0x1082: v1082(0x42ba) = CONST 
    0x1085: JUMP v1082(0x42ba)

    Begin block 0x42ba
    prev=[0x103a], succ=[0x35c0x33f]
    =================================
    0x42be: JUMP v340(0x35c)

    Begin block 0x35c0x33f
    prev=[0x4296, 0x42ba], succ=[0x37e0x33f]
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
    prev=[0xf79], succ=[0x4296]
    =================================
    0xf92: vf92(0x40) = CONST 
    0xf95: vf95 = MLOAD vf92(0x40)
    0xf96: vf96(0x20) = CONST 
    0xf99: vf99 = ADD vf95, vf96(0x20)
    0xf9c: MSTORE vf92(0x40), vf99
    0xf9d: vf9d(0x0) = CONST 
    0xfa0: MSTORE vf95, vf9d(0x0)
    0xfa1: vfa1(0x4296) = CONST 
    0xfa4: JUMP vfa1(0x4296)

    Begin block 0x4296
    prev=[0xf91], succ=[0x35c0x33f]
    =================================
    0x429a: JUMP v340(0x35c)

}

function 0x351f(0x351farg0x0, 0x351farg0x1, 0x351farg0x2, 0x351farg0x3, 0x351farg0x4, 0x351farg0x5, 0x351farg0x6) private {
    Begin block 0x351f
    prev=[], succ=[0x36a6B0x351f]
    =================================
    0x3520: v3520(0x3531) = CONST 
    0x3524: v3524(0x1) = CONST 
    0x3526: v3526(0x1) = CONST 
    0x3528: v3528(0xa0) = CONST 
    0x352a: v352a(0x10000000000000000000000000000000000000000) = SHL v3528(0xa0), v3526(0x1)
    0x352b: v352b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v352a(0x10000000000000000000000000000000000000000), v3524(0x1)
    0x352c: v352c = AND v352b(0xffffffffffffffffffffffffffffffffffffffff), v351farg3
    0x352d: v352d(0x36a6) = CONST 
    0x3530: JUMP v352d(0x36a6)

    Begin block 0x36a6B0x351f
    prev=[0x351f], succ=[0x3531]
    =================================
    0x36a7S0x351f: v36a7V351f = EXTCODESIZE v352c
    0x36a8S0x351f: v36a8V351f = ISZERO v36a7V351f
    0x36a9S0x351f: v36a9V351f = ISZERO v36a8V351f
    0x36abS0x351f: JUMP v3520(0x3531)

    Begin block 0x3531
    prev=[0x36a6B0x351f], succ=[0x4538, 0x3537]
    =================================
    0x3532: v3532 = ISZERO v36a9V351f
    0x3533: v3533(0x4538) = CONST 
    0x3536: JUMPI v3533(0x4538), v3532

    Begin block 0x4538
    prev=[0x3531], succ=[]
    =================================
    0x453f: RETURNPRIVATE v351farg6

    Begin block 0x3537
    prev=[0x3531], succ=[0x35a8]
    =================================
    0x3538: v3538(0x1) = CONST 
    0x353a: v353a(0x1) = CONST 
    0x353c: v353c(0xa0) = CONST 
    0x353e: v353e(0x10000000000000000000000000000000000000000) = SHL v353c(0xa0), v353a(0x1)
    0x353f: v353f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v353e(0x10000000000000000000000000000000000000000), v3538(0x1)
    0x3540: v3540 = AND v353f(0xffffffffffffffffffffffffffffffffffffffff), v351farg3
    0x3541: v3541(0xf23a6e61) = CONST 
    0x354b: v354b(0x40) = CONST 
    0x354d: v354d = MLOAD v354b(0x40)
    0x354f: v354f(0xffffffff) = CONST 
    0x3554: v3554(0xf23a6e61) = AND v354f(0xffffffff), v3541(0xf23a6e61)
    0x3555: v3555(0xe0) = CONST 
    0x3557: v3557(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v3555(0xe0), v3554(0xf23a6e61)
    0x3559: MSTORE v354d, v3557(0xf23a6e6100000000000000000000000000000000000000000000000000000000)
    0x355a: v355a(0x4) = CONST 
    0x355c: v355c = ADD v355a(0x4), v354d
    0x355f: v355f(0x1) = CONST 
    0x3561: v3561(0x1) = CONST 
    0x3563: v3563(0xa0) = CONST 
    0x3565: v3565(0x10000000000000000000000000000000000000000) = SHL v3563(0xa0), v3561(0x1)
    0x3566: v3566(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3565(0x10000000000000000000000000000000000000000), v355f(0x1)
    0x3567: v3567 = AND v3566(0xffffffffffffffffffffffffffffffffffffffff), v351farg5
    0x3569: MSTORE v355c, v3567
    0x356a: v356a(0x20) = CONST 
    0x356c: v356c = ADD v356a(0x20), v355c
    0x356e: v356e(0x1) = CONST 
    0x3570: v3570(0x1) = CONST 
    0x3572: v3572(0xa0) = CONST 
    0x3574: v3574(0x10000000000000000000000000000000000000000) = SHL v3572(0xa0), v3570(0x1)
    0x3575: v3575(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3574(0x10000000000000000000000000000000000000000), v356e(0x1)
    0x3576: v3576 = AND v3575(0xffffffffffffffffffffffffffffffffffffffff), v351farg4
    0x3578: MSTORE v356c, v3576
    0x3579: v3579(0x20) = CONST 
    0x357b: v357b = ADD v3579(0x20), v356c
    0x357e: MSTORE v357b, v351farg2
    0x357f: v357f(0x20) = CONST 
    0x3581: v3581 = ADD v357f(0x20), v357b
    0x3584: MSTORE v3581, v351farg1
    0x3585: v3585(0x20) = CONST 
    0x3587: v3587 = ADD v3585(0x20), v3581
    0x3589: v3589(0x20) = CONST 
    0x358b: v358b = ADD v3589(0x20), v3587
    0x358e: v358e(0xa0) = SUB v358b, v355c
    0x3590: MSTORE v3587, v358e(0xa0)
    0x3594: v3594 = MLOAD v351farg0
    0x3596: MSTORE v358b, v3594
    0x3597: v3597(0x20) = CONST 
    0x3599: v3599 = ADD v3597(0x20), v358b
    0x359d: v359d = MLOAD v351farg0
    0x359f: v359f(0x20) = CONST 
    0x35a1: v35a1 = ADD v359f(0x20), v351farg0
    0x35a6: v35a6(0x0) = CONST 

    Begin block 0x35a8
    prev=[0x3537, 0x35b1], succ=[0x35c0, 0x35b1]
    =================================
    0x35a8_0x0: v35a8_0 = PHI v35a6(0x0), v35bb
    0x35ab: v35ab = LT v35a8_0, v359d
    0x35ac: v35ac = ISZERO v35ab
    0x35ad: v35ad(0x35c0) = CONST 
    0x35b0: JUMPI v35ad(0x35c0), v35ac

    Begin block 0x35c0
    prev=[0x35a8], succ=[0x35ed, 0x35d4]
    =================================
    0x35c9: v35c9 = ADD v359d, v3599
    0x35cb: v35cb(0x1f) = CONST 
    0x35cd: v35cd = AND v35cb(0x1f), v359d
    0x35cf: v35cf = ISZERO v35cd
    0x35d0: v35d0(0x35ed) = CONST 
    0x35d3: JUMPI v35d0(0x35ed), v35cf

    Begin block 0x35ed
    prev=[0x35c0, 0x35d4], succ=[0x360c, 0x3610]
    =================================
    0x35ed_0x1: v35ed_1 = PHI v35c9, v35ea
    0x35f7: v35f7(0x20) = CONST 
    0x35f9: v35f9(0x40) = CONST 
    0x35fb: v35fb = MLOAD v35f9(0x40)
    0x35fe: v35fe = SUB v35ed_1, v35fb
    0x3600: v3600(0x0) = CONST 
    0x3604: v3604 = EXTCODESIZE v3540
    0x3605: v3605 = ISZERO v3604
    0x3607: v3607 = ISZERO v3605
    0x3608: v3608(0x3610) = CONST 
    0x360b: JUMPI v3608(0x3610), v3607

    Begin block 0x360c
    prev=[0x35ed], succ=[]
    =================================
    0x360c: v360c(0x0) = CONST 
    0x360f: REVERT v360c(0x0), v360c(0x0)

    Begin block 0x3610
    prev=[0x35ed], succ=[0x3635, 0x361e]
    =================================
    0x3612: v3612 = GAS 
    0x3613: v3613 = CALL v3612, v3540, v3600(0x0), v35fb, v35fe, v35fb, v35f7(0x20)
    0x3619: v3619 = ISZERO v3613
    0x361a: v361a(0x3635) = CONST 
    0x361d: JUMPI v361a(0x3635), v3619

    Begin block 0x3635
    prev=[0x3610, 0x3630], succ=[0x363a, 0x3641]
    =================================
    0x3635_0x0: v3635_0 = PHI v3613, v3633(0x1)
    0x3636: v3636(0x3641) = CONST 
    0x3639: JUMPI v3636(0x3641), v3635_0

    Begin block 0x363a
    prev=[0x3635], succ=[0x29bd0x351f]
    =================================
    0x363a: v363a(0x29bd) = CONST 
    0x363d: v363d(0x398b) = CONST 
    0x3640: v3640_0 = CALLPRIVATE v363d(0x398b), v363a(0x29bd)

    Begin block 0x29bd0x351f
    prev=[0x363a], succ=[0x29c30x351f, 0x29c80x351f]
    =================================
    0x29bf0x351f: v351f29bf(0x29c8) = CONST 
    0x29c20x351f: JUMPI v351f29bf(0x29c8), v3640_0

    Begin block 0x29c30x351f
    prev=[0x29bd0x351f], succ=[0x2a4d0x351f]
    =================================
    0x29c40x351f: v351f29c4(0x2a4d) = CONST 
    0x29c70x351f: JUMP v351f29c4(0x2a4d)

    Begin block 0x2a4d0x351f
    prev=[0x29c30x351f], succ=[]
    =================================
    0x2a4e0x351f: v351f2a4e(0x40) = CONST 
    0x2a500x351f: v351f2a50 = MLOAD v351f2a4e(0x40)
    0x2a510x351f: v351f2a51(0x461bcd) = CONST 
    0x2a550x351f: v351f2a55(0xe5) = CONST 
    0x2a570x351f: v351f2a57(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v351f2a55(0xe5), v351f2a51(0x461bcd)
    0x2a590x351f: MSTORE v351f2a50, v351f2a57(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a5a0x351f: v351f2a5a(0x4) = CONST 
    0x2a5c0x351f: v351f2a5c = ADD v351f2a5a(0x4), v351f2a50
    0x2a5f0x351f: v351f2a5f(0x20) = CONST 
    0x2a610x351f: v351f2a61 = ADD v351f2a5f(0x20), v351f2a5c
    0x2a640x351f: v351f2a64(0x20) = SUB v351f2a61, v351f2a5c
    0x2a660x351f: MSTORE v351f2a5c, v351f2a64(0x20)
    0x2a670x351f: v351f2a67(0x2b) = CONST 
    0x2a6a0x351f: MSTORE v351f2a61, v351f2a67(0x2b)
    0x2a6b0x351f: v351f2a6b(0x20) = CONST 
    0x2a6d0x351f: v351f2a6d = ADD v351f2a6b(0x20), v351f2a61
    0x2a6f0x351f: v351f2a6f(0x3a55) = CONST 
    0x2a720x351f: v351f2a72(0x2b) = CONST 
    0x2a750x351f: CODECOPY v351f2a6d, v351f2a6f(0x3a55), v351f2a72(0x2b)
    0x2a760x351f: v351f2a76(0x40) = CONST 
    0x2a780x351f: v351f2a78 = ADD v351f2a76(0x40), v351f2a6d
    0x2a7c0x351f: v351f2a7c(0x40) = CONST 
    0x2a7e0x351f: v351f2a7e = MLOAD v351f2a7c(0x40)
    0x2a810x351f: v351f2a81(0x84) = SUB v351f2a78, v351f2a7e
    0x2a830x351f: REVERT v351f2a7e, v351f2a81(0x84)

    Begin block 0x29c80x351f
    prev=[0x29bd0x351f], succ=[0x29fa0x351f]
    =================================
    0x29ca0x351f: v351f29ca(0x40) = CONST 
    0x29cc0x351f: v351f29cc = MLOAD v351f29ca(0x40)
    0x29cd0x351f: v351f29cd(0x461bcd) = CONST 
    0x29d10x351f: v351f29d1(0xe5) = CONST 
    0x29d30x351f: v351f29d3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v351f29d1(0xe5), v351f29cd(0x461bcd)
    0x29d50x351f: MSTORE v351f29cc, v351f29d3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29d60x351f: v351f29d6(0x4) = CONST 
    0x29d80x351f: v351f29d8 = ADD v351f29d6(0x4), v351f29cc
    0x29db0x351f: v351f29db(0x20) = CONST 
    0x29dd0x351f: v351f29dd = ADD v351f29db(0x20), v351f29d8
    0x29e00x351f: v351f29e0(0x20) = SUB v351f29dd, v351f29d8
    0x29e20x351f: MSTORE v351f29d8, v351f29e0(0x20)
    0x29e60x351f: v351f29e6 = MLOAD v3640_0
    0x29e80x351f: MSTORE v351f29dd, v351f29e6
    0x29e90x351f: v351f29e9(0x20) = CONST 
    0x29eb0x351f: v351f29eb = ADD v351f29e9(0x20), v351f29dd
    0x29ef0x351f: v351f29ef = MLOAD v3640_0
    0x29f10x351f: v351f29f1(0x20) = CONST 
    0x29f30x351f: v351f29f3 = ADD v351f29f1(0x20), v3640_0
    0x29f80x351f: v351f29f8(0x0) = CONST 

    Begin block 0x29fa0x351f
    prev=[0x2a030x351f, 0x29c80x351f], succ=[0x2a120x351f, 0x2a030x351f]
    =================================
    0x29fa0x351f_0x0: v29fa351f_0 = PHI v351f2a0d, v351f29f8(0x0)
    0x29fd0x351f: v351f29fd = LT v29fa351f_0, v351f29ef
    0x29fe0x351f: v351f29fe = ISZERO v351f29fd
    0x29ff0x351f: v351f29ff(0x2a12) = CONST 
    0x2a020x351f: JUMPI v351f29ff(0x2a12), v351f29fe

    Begin block 0x2a120x351f
    prev=[0x29fa0x351f], succ=[0x2a3f0x351f, 0x2a260x351f]
    =================================
    0x2a1b0x351f: v351f2a1b = ADD v351f29ef, v351f29eb
    0x2a1d0x351f: v351f2a1d(0x1f) = CONST 
    0x2a1f0x351f: v351f2a1f = AND v351f2a1d(0x1f), v351f29ef
    0x2a210x351f: v351f2a21 = ISZERO v351f2a1f
    0x2a220x351f: v351f2a22(0x2a3f) = CONST 
    0x2a250x351f: JUMPI v351f2a22(0x2a3f), v351f2a21

    Begin block 0x2a3f0x351f
    prev=[0x2a120x351f, 0x2a260x351f], succ=[]
    =================================
    0x2a3f0x351f_0x1: v2a3f351f_1 = PHI v351f2a3c, v351f2a1b
    0x2a450x351f: v351f2a45(0x40) = CONST 
    0x2a470x351f: v351f2a47 = MLOAD v351f2a45(0x40)
    0x2a4a0x351f: v351f2a4a = SUB v2a3f351f_1, v351f2a47
    0x2a4c0x351f: REVERT v351f2a47, v351f2a4a

    Begin block 0x2a260x351f
    prev=[0x2a120x351f], succ=[0x2a3f0x351f]
    =================================
    0x2a280x351f: v351f2a28 = SUB v351f2a1b, v351f2a1f
    0x2a2a0x351f: v351f2a2a = MLOAD v351f2a28
    0x2a2b0x351f: v351f2a2b(0x1) = CONST 
    0x2a2e0x351f: v351f2a2e(0x20) = CONST 
    0x2a300x351f: v351f2a30 = SUB v351f2a2e(0x20), v351f2a1f
    0x2a310x351f: v351f2a31(0x100) = CONST 
    0x2a340x351f: v351f2a34 = EXP v351f2a31(0x100), v351f2a30
    0x2a350x351f: v351f2a35 = SUB v351f2a34, v351f2a2b(0x1)
    0x2a360x351f: v351f2a36 = NOT v351f2a35
    0x2a370x351f: v351f2a37 = AND v351f2a36, v351f2a2a
    0x2a390x351f: MSTORE v351f2a28, v351f2a37
    0x2a3a0x351f: v351f2a3a(0x20) = CONST 
    0x2a3c0x351f: v351f2a3c = ADD v351f2a3a(0x20), v351f2a28

    Begin block 0x2a030x351f
    prev=[0x29fa0x351f], succ=[0x29fa0x351f]
    =================================
    0x2a030x351f_0x0: v2a03351f_0 = PHI v351f2a0d, v351f29f8(0x0)
    0x2a050x351f: v351f2a05 = ADD v2a03351f_0, v351f29f3
    0x2a060x351f: v351f2a06 = MLOAD v351f2a05
    0x2a090x351f: v351f2a09 = ADD v2a03351f_0, v351f29eb
    0x2a0a0x351f: MSTORE v351f2a09, v351f2a06
    0x2a0b0x351f: v351f2a0b(0x20) = CONST 
    0x2a0d0x351f: v351f2a0d = ADD v351f2a0b(0x20), v2a03351f_0
    0x2a0e0x351f: v351f2a0e(0x29fa) = CONST 
    0x2a110x351f: JUMP v351f2a0e(0x29fa)

    Begin block 0x3641
    prev=[0x3635], succ=[0x365a, 0x2ae90x351f]
    =================================
    0x3641_0x0: v3641_0 = PHI v3632, v351farg0
    0x3642: v3642(0x1) = CONST 
    0x3644: v3644(0x1) = CONST 
    0x3646: v3646(0xe0) = CONST 
    0x3648: v3648(0x100000000000000000000000000000000000000000000000000000000) = SHL v3646(0xe0), v3644(0x1)
    0x3649: v3649(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v3648(0x100000000000000000000000000000000000000000000000000000000), v3642(0x1)
    0x364a: v364a(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v3649(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x364c: v364c = AND v3641_0, v364a(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x364d: v364d(0xf23a6e61) = CONST 
    0x3652: v3652(0xe0) = CONST 
    0x3654: v3654(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v3652(0xe0), v364d(0xf23a6e61)
    0x3655: v3655 = EQ v3654(0xf23a6e6100000000000000000000000000000000000000000000000000000000), v364c
    0x3656: v3656(0x2ae9) = CONST 
    0x3659: JUMPI v3656(0x2ae9), v3655

    Begin block 0x365a
    prev=[0x3641], succ=[]
    =================================
    0x365a: v365a(0x40) = CONST 
    0x365d: v365d = MLOAD v365a(0x40)
    0x365e: v365e(0x461bcd) = CONST 
    0x3662: v3662(0xe5) = CONST 
    0x3664: v3664(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3662(0xe5), v365e(0x461bcd)
    0x3666: MSTORE v365d, v3664(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3667: v3667(0x20) = CONST 
    0x3669: v3669(0x4) = CONST 
    0x366c: v366c = ADD v365d, v3669(0x4)
    0x366d: MSTORE v366c, v3667(0x20)
    0x366e: v366e(0x1f) = CONST 
    0x3670: v3670(0x24) = CONST 
    0x3673: v3673 = ADD v365d, v3670(0x24)
    0x3674: MSTORE v3673, v366e(0x1f)
    0x3675: v3675(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x3696: v3696(0x44) = CONST 
    0x3699: v3699 = ADD v365d, v3696(0x44)
    0x369a: MSTORE v3699, v3675(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x369c: v369c = MLOAD v365a(0x40)
    0x36a0: v36a0(0x0) = SUB v365d, v369c
    0x36a1: v36a1(0x64) = CONST 
    0x36a3: v36a3(0x64) = ADD v36a1(0x64), v36a0(0x0)
    0x36a5: REVERT v369c, v36a3(0x64)

    Begin block 0x2ae90x351f
    prev=[0x3641], succ=[0x2aeb0x351f]
    =================================

    Begin block 0x2aeb0x351f
    prev=[0x2ae90x351f], succ=[]
    =================================
    0x2af20x351f: RETURNPRIVATE v351farg6

    Begin block 0x361e
    prev=[0x3610], succ=[0x362c, 0x3630]
    =================================
    0x361f: v361f(0x40) = CONST 
    0x3621: v3621 = MLOAD v361f(0x40)
    0x3622: v3622 = RETURNDATASIZE 
    0x3623: v3623(0x20) = CONST 
    0x3626: v3626 = LT v3622, v3623(0x20)
    0x3627: v3627 = ISZERO v3626
    0x3628: v3628(0x3630) = CONST 
    0x362b: JUMPI v3628(0x3630), v3627

    Begin block 0x362c
    prev=[0x361e], succ=[]
    =================================
    0x362c: v362c(0x0) = CONST 
    0x362f: REVERT v362c(0x0), v362c(0x0)

    Begin block 0x3630
    prev=[0x361e], succ=[0x3635]
    =================================
    0x3632: v3632 = MLOAD v3621
    0x3633: v3633(0x1) = CONST 

    Begin block 0x35d4
    prev=[0x35c0], succ=[0x35ed]
    =================================
    0x35d6: v35d6 = SUB v35c9, v35cd
    0x35d8: v35d8 = MLOAD v35d6
    0x35d9: v35d9(0x1) = CONST 
    0x35dc: v35dc(0x20) = CONST 
    0x35de: v35de = SUB v35dc(0x20), v35cd
    0x35df: v35df(0x100) = CONST 
    0x35e2: v35e2 = EXP v35df(0x100), v35de
    0x35e3: v35e3 = SUB v35e2, v35d9(0x1)
    0x35e4: v35e4 = NOT v35e3
    0x35e5: v35e5 = AND v35e4, v35d8
    0x35e7: MSTORE v35d6, v35e5
    0x35e8: v35e8(0x20) = CONST 
    0x35ea: v35ea = ADD v35e8(0x20), v35d6

    Begin block 0x35b1
    prev=[0x35a8], succ=[0x35a8]
    =================================
    0x35b1_0x0: v35b1_0 = PHI v35a6(0x0), v35bb
    0x35b3: v35b3 = ADD v35b1_0, v35a1
    0x35b4: v35b4 = MLOAD v35b3
    0x35b7: v35b7 = ADD v35b1_0, v3599
    0x35b8: MSTORE v35b7, v35b4
    0x35b9: v35b9(0x20) = CONST 
    0x35bb: v35bb = ADD v35b9(0x20), v35b1_0
    0x35bc: v35bc(0x35a8) = CONST 
    0x35bf: JUMP v35bc(0x35a8)

}

function 0x36ac(0x36acarg0x0, 0x36acarg0x1) private {
    Begin block 0x36ac
    prev=[], succ=[0x36bf]
    =================================
    0x36ad: v36ad(0x0) = CONST 
    0x36af: v36af(0x36bf) = CONST 
    0x36b3: v36b3(0x1ffc9a7) = CONST 
    0x36b8: v36b8(0xe0) = CONST 
    0x36ba: v36ba(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v36b8(0xe0), v36b3(0x1ffc9a7)
    0x36bb: v36bb(0x36df) = CONST 
    0x36be: v36be_0 = CALLPRIVATE v36bb(0x36df), v36ba(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v36acarg0, v36af(0x36bf)

    Begin block 0x36bf
    prev=[0x36ac], succ=[0x455f, 0x36c6]
    =================================
    0x36c1: v36c1 = ISZERO v36be_0
    0x36c2: v36c2(0x455f) = CONST 
    0x36c5: JUMPI v36c2(0x455f), v36c1

    Begin block 0x455f
    prev=[0x36bf], succ=[]
    =================================
    0x4564: RETURNPRIVATE v36acarg1, v36be_0

    Begin block 0x36c6
    prev=[0x36bf], succ=[0x36d8]
    =================================
    0x36c7: v36c7(0x36d8) = CONST 
    0x36cb: v36cb(0x1) = CONST 
    0x36cd: v36cd(0x1) = CONST 
    0x36cf: v36cf(0xe0) = CONST 
    0x36d1: v36d1(0x100000000000000000000000000000000000000000000000000000000) = SHL v36cf(0xe0), v36cd(0x1)
    0x36d2: v36d2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v36d1(0x100000000000000000000000000000000000000000000000000000000), v36cb(0x1)
    0x36d3: v36d3(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v36d2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x36d4: v36d4(0x36df) = CONST 
    0x36d7: v36d7_0 = CALLPRIVATE v36d4(0x36df), v36d3(0xffffffff00000000000000000000000000000000000000000000000000000000), v36acarg0, v36c7(0x36d8)

    Begin block 0x36d8
    prev=[0x36c6], succ=[]
    =================================
    0x36d9: v36d9 = ISZERO v36d7_0
    0x36de: RETURNPRIVATE v36acarg1, v36d9

}

function 0x36df(0x36dfarg0x0, 0x36dfarg0x1, 0x36dfarg0x2) private {
    Begin block 0x36df
    prev=[], succ=[0x3702B0x36df]
    =================================
    0x36e0: v36e0(0x0) = CONST 
    0x36e3: v36e3(0x0) = CONST 
    0x36e5: v36e5(0x36ee) = CONST 
    0x36ea: v36ea(0x3702) = CONST 
    0x36ed: JUMP v36ea(0x3702)

    Begin block 0x3702B0x36df
    prev=[0x36df], succ=[0x376aB0x36df]
    =================================
    0x3703S0x36df: v3703V36df(0x40) = CONST 
    0x3706S0x36df: v3706V36df = MLOAD v3703V36df(0x40)
    0x3707S0x36df: v3707V36df(0x1) = CONST 
    0x3709S0x36df: v3709V36df(0x1) = CONST 
    0x370bS0x36df: v370bV36df(0xe0) = CONST 
    0x370dS0x36df: v370dV36df(0x100000000000000000000000000000000000000000000000000000000) = SHL v370bV36df(0xe0), v3709V36df(0x1)
    0x370eS0x36df: v370eV36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v370dV36df(0x100000000000000000000000000000000000000000000000000000000), v3707V36df(0x1)
    0x370fS0x36df: v370fV36df(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v370eV36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x3711S0x36df: v3711V36df = AND v36dfarg0, v370fV36df(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x3712S0x36df: v3712V36df(0x24) = CONST 
    0x3716S0x36df: v3716V36df = ADD v3706V36df, v3712V36df(0x24)
    0x371aS0x36df: MSTORE v3716V36df, v3711V36df
    0x371cS0x36df: v371cV36df = MLOAD v3703V36df(0x40)
    0x371fS0x36df: v371fV36df(0x0) = SUB v3706V36df, v371cV36df
    0x3722S0x36df: v3722V36df(0x24) = ADD v3712V36df(0x24), v371fV36df(0x0)
    0x3724S0x36df: MSTORE v371cV36df, v3722V36df(0x24)
    0x3725S0x36df: v3725V36df(0x44) = CONST 
    0x3729S0x36df: v3729V36df = ADD v3706V36df, v3725V36df(0x44)
    0x372bS0x36df: MSTORE v3703V36df(0x40), v3729V36df
    0x372cS0x36df: v372cV36df(0x20) = CONST 
    0x372fS0x36df: v372fV36df = ADD v371cV36df, v372cV36df(0x20)
    0x3731S0x36df: v3731V36df = MLOAD v372fV36df
    0x3732S0x36df: v3732V36df(0x1) = CONST 
    0x3734S0x36df: v3734V36df(0x1) = CONST 
    0x3736S0x36df: v3736V36df(0xe0) = CONST 
    0x3738S0x36df: v3738V36df(0x100000000000000000000000000000000000000000000000000000000) = SHL v3736V36df(0xe0), v3734V36df(0x1)
    0x3739S0x36df: v3739V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v3738V36df(0x100000000000000000000000000000000000000000000000000000000), v3732V36df(0x1)
    0x373aS0x36df: v373aV36df = AND v3739V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v3731V36df
    0x373bS0x36df: v373bV36df(0x1ffc9a7) = CONST 
    0x3740S0x36df: v3740V36df(0xe0) = CONST 
    0x3742S0x36df: v3742V36df(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v3740V36df(0xe0), v373bV36df(0x1ffc9a7)
    0x3743S0x36df: v3743V36df = OR v3742V36df(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v373aV36df
    0x3745S0x36df: MSTORE v372fV36df, v3743V36df
    0x3747S0x36df: v3747V36df = MLOAD v3703V36df(0x40)
    0x3749S0x36df: v3749V36df(0x24) = MLOAD v371cV36df
    0x374aS0x36df: v374aV36df(0x0) = CONST 
    0x3754S0x36df: v3754V36df(0x1) = CONST 
    0x3756S0x36df: v3756V36df(0x1) = CONST 
    0x3758S0x36df: v3758V36df(0xa0) = CONST 
    0x375aS0x36df: v375aV36df(0x10000000000000000000000000000000000000000) = SHL v3758V36df(0xa0), v3756V36df(0x1)
    0x375bS0x36df: v375bV36df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v375aV36df(0x10000000000000000000000000000000000000000), v3754V36df(0x1)
    0x375dS0x36df: v375dV36df = AND v36dfarg1, v375bV36df(0xffffffffffffffffffffffffffffffffffffffff)
    0x375fS0x36df: v375fV36df(0x7530) = CONST 

    Begin block 0x376aB0x36df
    prev=[0x3702B0x36df, 0x3773B0x36df], succ=[0x3789B0x36df, 0x3773B0x36df]
    =================================
    0x376a_0x2S0x36df: v376a_2V36df = PHI v3749V36df(0x24), v377cV36df
    0x376bS0x36df: v376bV36df(0x20) = CONST 
    0x376eS0x36df: v376eV36df = LT v376a_2V36df, v376bV36df(0x20)
    0x376fS0x36df: v376fV36df(0x3789) = CONST 
    0x3772S0x36df: JUMPI v376fV36df(0x3789), v376eV36df

    Begin block 0x3789B0x36df
    prev=[0x376aB0x36df], succ=[0x37c9B0x36df, 0x37eaB0x36df]
    =================================
    0x3789_0x0S0x36df: v3789_0V36df = PHI v372fV36df, v3784V36df
    0x3789_0x1S0x36df: v3789_1V36df = PHI v3747V36df, v3782V36df
    0x3789_0x2S0x36df: v3789_2V36df = PHI v3749V36df(0x24), v377cV36df
    0x378aS0x36df: v378aV36df(0x1) = CONST 
    0x378dS0x36df: v378dV36df(0x20) = CONST 
    0x378fS0x36df: v378fV36df = SUB v378dV36df(0x20), v3789_2V36df
    0x3790S0x36df: v3790V36df(0x100) = CONST 
    0x3793S0x36df: v3793V36df = EXP v3790V36df(0x100), v378fV36df
    0x3794S0x36df: v3794V36df = SUB v3793V36df, v378aV36df(0x1)
    0x3796S0x36df: v3796V36df = NOT v3794V36df
    0x3798S0x36df: v3798V36df = MLOAD v3789_0V36df
    0x3799S0x36df: v3799V36df = AND v3798V36df, v3796V36df
    0x379cS0x36df: v379cV36df = MLOAD v3789_1V36df
    0x379dS0x36df: v379dV36df = AND v379cV36df, v3794V36df
    0x37a0S0x36df: v37a0V36df = OR v3799V36df, v379dV36df
    0x37a2S0x36df: MSTORE v3789_1V36df, v37a0V36df
    0x37abS0x36df: v37abV36df = ADD v3749V36df(0x24), v3747V36df
    0x37afS0x36df: v37afV36df(0x0) = CONST 
    0x37b1S0x36df: v37b1V36df(0x40) = CONST 
    0x37b3S0x36df: v37b3V36df = MLOAD v37b1V36df(0x40)
    0x37b6S0x36df: v37b6V36df(0x24) = SUB v37abV36df, v37b3V36df
    0x37baS0x36df: v37baV36df = STATICCALL v375fV36df(0x7530), v375dV36df, v37b3V36df, v37b6V36df(0x24), v37b3V36df, v37afV36df(0x0)
    0x37bfS0x36df: v37bfV36df = RETURNDATASIZE 
    0x37c1S0x36df: v37c1V36df(0x0) = CONST 
    0x37c4S0x36df: v37c4V36df = EQ v37bfV36df, v37c1V36df(0x0)
    0x37c5S0x36df: v37c5V36df(0x37ea) = CONST 
    0x37c8S0x36df: JUMPI v37c5V36df(0x37ea), v37c4V36df

    Begin block 0x37c9B0x36df
    prev=[0x3789B0x36df], succ=[0x37efB0x36df]
    =================================
    0x37c9S0x36df: v37c9V36df(0x40) = CONST 
    0x37cbS0x36df: v37cbV36df = MLOAD v37c9V36df(0x40)
    0x37ceS0x36df: v37ceV36df(0x1f) = CONST 
    0x37d0S0x36df: v37d0V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v37ceV36df(0x1f)
    0x37d1S0x36df: v37d1V36df(0x3f) = CONST 
    0x37d3S0x36df: v37d3V36df = RETURNDATASIZE 
    0x37d4S0x36df: v37d4V36df = ADD v37d3V36df, v37d1V36df(0x3f)
    0x37d5S0x36df: v37d5V36df = AND v37d4V36df, v37d0V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x37d7S0x36df: v37d7V36df = ADD v37cbV36df, v37d5V36df
    0x37d8S0x36df: v37d8V36df(0x40) = CONST 
    0x37daS0x36df: MSTORE v37d8V36df(0x40), v37d7V36df
    0x37dbS0x36df: v37dbV36df = RETURNDATASIZE 
    0x37ddS0x36df: MSTORE v37cbV36df, v37dbV36df
    0x37deS0x36df: v37deV36df = RETURNDATASIZE 
    0x37dfS0x36df: v37dfV36df(0x0) = CONST 
    0x37e1S0x36df: v37e1V36df(0x20) = CONST 
    0x37e4S0x36df: v37e4V36df = ADD v37cbV36df, v37e1V36df(0x20)
    0x37e5S0x36df: RETURNDATACOPY v37e4V36df, v37dfV36df(0x0), v37deV36df
    0x37e6S0x36df: v37e6V36df(0x37ef) = CONST 
    0x37e9S0x36df: JUMP v37e6V36df(0x37ef)

    Begin block 0x37efB0x36df
    prev=[0x37c9B0x36df, 0x37eaB0x36df], succ=[0x37ffB0x36df, 0x380dB0x36df]
    =================================
    0x37ef_0x1S0x36df: v37ef_1V36df = PHI v37cbV36df, v37ebV36df(0x60)
    0x37f5S0x36df: v37f5V36df(0x20) = CONST 
    0x37f8S0x36df: v37f8V36df = MLOAD v37ef_1V36df
    0x37f9S0x36df: v37f9V36df = LT v37f8V36df, v37f5V36df(0x20)
    0x37faS0x36df: v37faV36df = ISZERO v37f9V36df
    0x37fbS0x36df: v37fbV36df(0x380d) = CONST 
    0x37feS0x36df: JUMPI v37fbV36df(0x380d), v37faV36df

    Begin block 0x37ffB0x36df
    prev=[0x37efB0x36df], succ=[0x382eB0x36df]
    =================================
    0x37ffS0x36df: v37ffV36df(0x0) = CONST 
    0x3809S0x36df: v3809V36df(0x382e) = CONST 
    0x380cS0x36df: JUMP v3809V36df(0x382e)

    Begin block 0x382eB0x36df
    prev=[0x37ffB0x36df, 0x3823B0x36df], succ=[0x36ee]
    =================================
    0x382e_0x0S0x36df: v382e_0V36df = PHI v37ffV36df(0x0), v3825V36df
    0x382e_0x1S0x36df: v382e_1V36df = PHI v37ffV36df(0x0), v37baV36df
    0x3834S0x36df: JUMP v36e5(0x36ee)

    Begin block 0x36ee
    prev=[0x382eB0x36df], succ=[0x4584, 0x36fa]
    =================================
    0x36f5: v36f5 = ISZERO v382e_1V36df
    0x36f6: v36f6(0x4584) = CONST 
    0x36f9: JUMPI v36f6(0x4584), v36f5

    Begin block 0x4584
    prev=[0x36ee], succ=[]
    =================================
    0x458c: RETURNPRIVATE v36dfarg2, v382e_1V36df

    Begin block 0x36fa
    prev=[0x36ee], succ=[]
    =================================
    0x3701: RETURNPRIVATE v36dfarg2, v382e_0V36df

    Begin block 0x380dB0x36df
    prev=[0x37efB0x36df], succ=[0x381fB0x36df, 0x3823B0x36df]
    =================================
    0x380d_0x0S0x36df: v380d_0V36df = PHI v37cbV36df, v37ebV36df(0x60)
    0x3811S0x36df: v3811V36df(0x20) = CONST 
    0x3813S0x36df: v3813V36df = ADD v3811V36df(0x20), v380d_0V36df
    0x3815S0x36df: v3815V36df = MLOAD v380d_0V36df
    0x3816S0x36df: v3816V36df(0x20) = CONST 
    0x3819S0x36df: v3819V36df = LT v3815V36df, v3816V36df(0x20)
    0x381aS0x36df: v381aV36df = ISZERO v3819V36df
    0x381bS0x36df: v381bV36df(0x3823) = CONST 
    0x381eS0x36df: JUMPI v381bV36df(0x3823), v381aV36df

    Begin block 0x381fB0x36df
    prev=[0x380dB0x36df], succ=[]
    =================================
    0x381fS0x36df: v381fV36df(0x0) = CONST 
    0x3822S0x36df: REVERT v381fV36df(0x0), v381fV36df(0x0)

    Begin block 0x3823B0x36df
    prev=[0x380dB0x36df], succ=[0x382eB0x36df]
    =================================
    0x3825S0x36df: v3825V36df = MLOAD v3813V36df

    Begin block 0x37eaB0x36df
    prev=[0x3789B0x36df], succ=[0x37efB0x36df]
    =================================
    0x37ebS0x36df: v37ebV36df(0x60) = CONST 

    Begin block 0x3773B0x36df
    prev=[0x376aB0x36df], succ=[0x376aB0x36df]
    =================================
    0x3773_0x0S0x36df: v3773_0V36df = PHI v372fV36df, v3784V36df
    0x3773_0x1S0x36df: v3773_1V36df = PHI v3747V36df, v3782V36df
    0x3773_0x2S0x36df: v3773_2V36df = PHI v3749V36df(0x24), v377cV36df
    0x3774S0x36df: v3774V36df = MLOAD v3773_0V36df
    0x3776S0x36df: MSTORE v3773_1V36df, v3774V36df
    0x3777S0x36df: v3777V36df(0x1f) = CONST 
    0x3779S0x36df: v3779V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3777V36df(0x1f)
    0x377cS0x36df: v377cV36df = ADD v3773_2V36df, v3779V36df(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x377eS0x36df: v377eV36df(0x20) = CONST 
    0x3782S0x36df: v3782V36df = ADD v377eV36df(0x20), v3773_1V36df
    0x3784S0x36df: v3784V36df = ADD v377eV36df(0x20), v3773_0V36df
    0x3785S0x36df: v3785V36df(0x376a) = CONST 
    0x3788S0x36df: JUMP v3785V36df(0x376a)

}

function 0x398b(0x398barg0x0) private {
    Begin block 0x398b
    prev=[], succ=[0x3997, 0x399b]
    =================================
    0x398c: v398c(0x0) = CONST 
    0x398e: v398e(0x44) = CONST 
    0x3990: v3990 = RETURNDATASIZE 
    0x3991: v3991 = LT v3990, v398e(0x44)
    0x3992: v3992 = ISZERO v3991
    0x3993: v3993(0x399b) = CONST 
    0x3996: JUMPI v3993(0x399b), v3992

    Begin block 0x3997
    prev=[0x398b], succ=[0x45f2]
    =================================
    0x3997: v3997(0x45f2) = CONST 
    0x399a: JUMP v3997(0x45f2)

    Begin block 0x45f2
    prev=[0x3997], succ=[]
    =================================
    0x45f4: RETURNPRIVATE v398barg0, v398c(0x0)

    Begin block 0x399b
    prev=[0x398b], succ=[0x3985]
    =================================
    0x399c: v399c(0x4) = CONST 
    0x39a0: RETURNDATACOPY v398c(0x0), v398c(0x0), v399c(0x4)
    0x39a1: v39a1(0x8c379a0) = CONST 
    0x39a6: v39a6(0x39af) = CONST 
    0x39aa: v39aa = MLOAD v398c(0x0)
    0x39ab: v39ab(0x3985) = CONST 
    0x39ae: JUMP v39ab(0x3985)

    Begin block 0x3985
    prev=[0x399b], succ=[0x39af]
    =================================
    0x3986: v3986(0xe0) = CONST 
    0x3988: v3988 = SHR v3986(0xe0), v39aa
    0x398a: JUMP v39a6(0x39af)

    Begin block 0x39af
    prev=[0x3985], succ=[0x39b5, 0x39b9]
    =================================
    0x39b0: v39b0 = EQ v3988, v39a1(0x8c379a0)
    0x39b1: v39b1(0x39b9) = CONST 
    0x39b4: JUMPI v39b1(0x39b9), v39b0

    Begin block 0x39b5
    prev=[0x39af], succ=[0x4614]
    =================================
    0x39b5: v39b5(0x4614) = CONST 
    0x39b8: JUMP v39b5(0x4614)

    Begin block 0x4614
    prev=[0x39b5], succ=[]
    =================================
    0x4616: RETURNPRIVATE v398barg0, v398c(0x0)

    Begin block 0x39b9
    prev=[0x39af], succ=[0x39e9, 0x39e1]
    =================================
    0x39ba: v39ba(0x40) = CONST 
    0x39bc: v39bc = MLOAD v39ba(0x40)
    0x39bd: v39bd = RETURNDATASIZE 
    0x39be: v39be(0x3) = CONST 
    0x39c0: v39c0(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc) = NOT v39be(0x3)
    0x39c1: v39c1 = ADD v39c0(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc), v39bd
    0x39c2: v39c2(0x4) = CONST 
    0x39c5: RETURNDATACOPY v39bc, v39c2(0x4), v39c1
    0x39c7: v39c7 = MLOAD v39bc
    0x39c8: v39c8 = RETURNDATASIZE 
    0x39c9: v39c9(0xffffffffffffffff) = CONST 
    0x39d3: v39d3(0x24) = CONST 
    0x39d6: v39d6 = ADD v39c7, v39d3(0x24)
    0x39d7: v39d7 = GT v39d6, v39c8
    0x39da: v39da = GT v39c7, v39c9(0xffffffffffffffff)
    0x39db: v39db = OR v39da, v39d7
    0x39dc: v39dc = ISZERO v39db
    0x39dd: v39dd(0x39e9) = CONST 
    0x39e0: JUMPI v39dd(0x39e9), v39dc

    Begin block 0x39e9
    prev=[0x39b9], succ=[0x3a03, 0x39fb]
    =================================
    0x39ec: v39ec = ADD v39bc, v39c7
    0x39f0: v39f0 = MLOAD v39ec
    0x39f5: v39f5 = GT v39f0, v39c9(0xffffffffffffffff)
    0x39f6: v39f6 = ISZERO v39f5
    0x39f7: v39f7(0x3a03) = CONST 
    0x39fa: JUMPI v39f7(0x3a03), v39f6

    Begin block 0x3a03
    prev=[0x39e9], succ=[0x3a1b, 0x3a14]
    =================================
    0x3a05: v3a05 = RETURNDATASIZE 
    0x3a07: v3a07 = ADD v39bc, v3a05
    0x3a08: v3a08(0x20) = CONST 
    0x3a0c: v3a0c = ADD v39ec, v39f0
    0x3a0d: v3a0d = ADD v3a0c, v3a08(0x20)
    0x3a0e: v3a0e = GT v3a0d, v3a07
    0x3a0f: v3a0f = ISZERO v3a0e
    0x3a10: v3a10(0x3a1b) = CONST 
    0x3a13: JUMPI v3a10(0x3a1b), v3a0f

    Begin block 0x3a1b
    prev=[0x3a03], succ=[]
    =================================
    0x3a1c: v3a1c(0x1f) = CONST 
    0x3a1e: v3a1e = ADD v3a1c(0x1f), v39f0
    0x3a1f: v3a1f(0x1f) = CONST 
    0x3a21: v3a21(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3a1f(0x1f)
    0x3a22: v3a22 = AND v3a21(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v3a1e
    0x3a24: v3a24 = ADD v39ec, v3a22
    0x3a25: v3a25(0x20) = CONST 
    0x3a27: v3a27 = ADD v3a25(0x20), v3a24
    0x3a28: v3a28(0x40) = CONST 
    0x3a2a: MSTORE v3a28(0x40), v3a27
    0x3a2f: RETURNPRIVATE v398barg0, v39ec

    Begin block 0x3a14
    prev=[0x3a03], succ=[0x467a]
    =================================
    0x3a17: v3a17(0x467a) = CONST 
    0x3a1a: JUMP v3a17(0x467a)

    Begin block 0x467a
    prev=[0x3a14], succ=[]
    =================================
    0x467c: RETURNPRIVATE v398barg0, v398c(0x0)

    Begin block 0x39fb
    prev=[0x39e9], succ=[0x4658]
    =================================
    0x39ff: v39ff(0x4658) = CONST 
    0x3a02: JUMP v39ff(0x4658)

    Begin block 0x4658
    prev=[0x39fb], succ=[]
    =================================
    0x465a: RETURNPRIVATE v398barg0, v398c(0x0)

    Begin block 0x39e1
    prev=[0x39b9], succ=[0x4636]
    =================================
    0x39e5: v39e5(0x4636) = CONST 
    0x39e8: JUMP v39e5(0x4636)

    Begin block 0x4636
    prev=[0x39e1], succ=[]
    =================================
    0x4638: RETURNPRIVATE v398barg0, v398c(0x0)

}

function fallback()() public {
    Begin block 0x3c81
    prev=[], succ=[]
    =================================
    0x3c82: v3c82(0x0) = CONST 
    0x3c85: REVERT v3c82(0x0), v3c82(0x0)

}

function initialized()() public {
    Begin block 0x3d1
    prev=[], succ=[0x1086B0x3d1]
    =================================
    0x3d2: v3d2(0x3e26) = CONST 
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
    prev=[0x1086B0x3d1], succ=[0x3e26]
    =================================
    0x108fS0x3d1: JUMP v3d2(0x3e26)

    Begin block 0x3e26
    prev=[0x108dB0x3d1], succ=[]
    =================================
    0x3e27: v3e27(0x40) = CONST 
    0x3e2a: v3e2a = MLOAD v3e27(0x40)
    0x3e2c: v3e2c = ISZERO v108cV3d1
    0x3e2d: v3e2d = ISZERO v3e2c
    0x3e2f: MSTORE v3e2a, v3e2d
    0x3e30: v3e30 = MLOAD v3e27(0x40)
    0x3e34: v3e34(0x0) = SUB v3e2a, v3e30
    0x3e35: v3e35(0x20) = CONST 
    0x3e37: v3e37(0x20) = ADD v3e35(0x20), v3e34(0x0)
    0x3e39: RETURN v3e30, v3e37(0x20)

}

function mintQuasar(address,uint256,uint256,address,uint256)() public {
    Begin block 0x3d9
    prev=[], succ=[0x3eb, 0x3ef]
    =================================
    0x3da: v3da(0x3e59) = CONST 
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
    prev=[0x1090], succ=[0x27b2]
    =================================
    0x10e6: v10e6(0x10f2) = CONST 
    0x10ee: v10ee(0x27b2) = CONST 
    0x10f1: JUMP v10ee(0x27b2)

    Begin block 0x27b2
    prev=[0x10e5], succ=[0x27bf]
    =================================
    0x27b3: v27b3(0x0) = CONST 
    0x27b6: v27b6(0x27bf) = CONST 
    0x27bb: v27bb(0x2af3) = CONST 
    0x27be: v27be_0 = CALLPRIVATE v27bb(0x2af3), v402, v3fc, v27b6(0x27bf)

    Begin block 0x27bf
    prev=[0x27b2], succ=[0x10f2]
    =================================
    0x27c0: v27c0(0x40) = CONST 
    0x27c3: v27c3 = MLOAD v27c0(0x40)
    0x27c4: v27c4(0x60) = CONST 
    0x27c7: v27c7 = ADD v27c3, v27c4(0x60)
    0x27c9: MSTORE v27c0(0x40), v27c7
    0x27ca: v27ca(0x1) = CONST 
    0x27cc: v27cc(0x1) = CONST 
    0x27ce: v27ce(0xa0) = CONST 
    0x27d0: v27d0(0x10000000000000000000000000000000000000000) = SHL v27ce(0xa0), v27cc(0x1)
    0x27d1: v27d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27d0(0x10000000000000000000000000000000000000000), v27ca(0x1)
    0x27d4: v27d4 = AND v27d1(0xffffffffffffffffffffffffffffffffffffffff), v411
    0x27d6: MSTORE v27c3, v27d4
    0x27d7: v27d7(0x20) = CONST 
    0x27db: v27db = ADD v27c3, v27d7(0x20)
    0x27de: MSTORE v27db, v416
    0x27e1: v27e1 = ADD v27c0(0x40), v27c3
    0x27e4: MSTORE v27e1, v408
    0x27e5: v27e5(0x0) = CONST 
    0x27e9: MSTORE v27e5(0x0), v27be_0
    0x27ea: v27ea(0xb) = CONST 
    0x27ee: MSTORE v27d7(0x20), v27ea(0xb)
    0x27f2: v27f2 = SHA3 v27e5(0x0), v27c0(0x40)
    0x27f4: v27f4 = MLOAD v27c3
    0x27f6: v27f6 = SLOAD v27f2
    0x27f7: v27f7(0x1) = CONST 
    0x27f9: v27f9(0x1) = CONST 
    0x27fb: v27fb(0xa0) = CONST 
    0x27fd: v27fd(0x10000000000000000000000000000000000000000) = SHL v27fb(0xa0), v27f9(0x1)
    0x27fe: v27fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27fd(0x10000000000000000000000000000000000000000), v27f7(0x1)
    0x27ff: v27ff(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x2800: v2800 = AND v27ff(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v27f6
    0x2802: v2802 = AND v27d1(0xffffffffffffffffffffffffffffffffffffffff), v27f4
    0x2806: v2806 = OR v2802, v2800
    0x2808: SSTORE v27f2, v2806
    0x280a: v280a = MLOAD v27db
    0x280b: v280b(0x1) = CONST 
    0x280e: v280e = ADD v27f2, v280b(0x1)
    0x280f: SSTORE v280e, v280a
    0x2813: v2813 = MLOAD v27e1
    0x2814: v2814(0x2) = CONST 
    0x2818: v2818 = ADD v27f2, v2814(0x2)
    0x2819: SSTORE v2818, v2813
    0x281e: JUMP v10e6(0x10f2)

    Begin block 0x10f2
    prev=[0x27bf], succ=[0x3e59]
    =================================
    0x10fb: JUMP v3da(0x3e59)

    Begin block 0x3e59
    prev=[0x10f2], succ=[]
    =================================
    0x3e5a: v3e5a(0x40) = CONST 
    0x3e5d: v3e5d = MLOAD v3e5a(0x40)
    0x3e60: MSTORE v3e5d, v27be_0
    0x3e61: v3e61 = MLOAD v3e5a(0x40)
    0x3e65: v3e65(0x0) = SUB v3e5d, v3e61
    0x3e66: v3e66(0x20) = CONST 
    0x3e68: v3e68(0x20) = ADD v3e66(0x20), v3e65(0x0)
    0x3e6a: RETURN v3e61, v3e68(0x20)

}

function safeBatchTransferFrom(address,address,uint256[],uint256[],bytes)() public {
    Begin block 0x41b
    prev=[], succ=[0x42d, 0x431]
    =================================
    0x41c: v41c(0x3e8a) = CONST 
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
    0x112c: v112c(0x3bb7) = CONST 
    0x112f: v112f(0x2a) = CONST 
    0x1132: CODECOPY v112a, v112c(0x3bb7), v112f(0x2a)
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
    0x116c: v116c(0x3b70) = CONST 
    0x116f: v116f(0x23) = CONST 
    0x1172: CODECOPY v116a, v116c(0x3b70), v116f(0x23)
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
    prev=[0x1181, 0x24f4B0x1193], succ=[0x11a2, 0x11d8]
    =================================
    0x119d_0x0: v119d_0 = PHI v118d, v251fV1193
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
    0x11c3: v11c3(0x3afa) = CONST 
    0x11c6: v11c6(0x2d) = CONST 
    0x11c9: CODECOPY v11c1, v11c3(0x3afa), v11c6(0x2d)
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
    0x1202: v1202(0x24b9) = CONST 
    0x1205: v1205_0 = CALLPRIVATE v1202(0x24b9), v11fa, v43d, v11fd(0x1206)

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
    prev=[0x1323], succ=[0x42de]
    =================================
    0x1342: v1342 = ADD v131d, v1311
    0x1349: v1349(0x40) = CONST 
    0x134b: v134b = MLOAD v1349(0x40)
    0x134e: v134e = SUB v1342, v134b
    0x1350: LOG4 v134b, v134e, v1296(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v1295, v128b, v1281
    0x1351: v1351(0x42de) = CONST 
    0x1354: v1354 = CALLER 
    0x135a: v135a(0x281f) = CONST 
    0x135d: CALLPRIVATE v135a(0x281f), v5ae, v526, v4a4, v446, v43d, v1354, v1351(0x42de)

    Begin block 0x42de
    prev=[0x133b], succ=[0x3e8a]
    =================================
    0x42e4: JUMP v41c(0x3e8a)

    Begin block 0x3e8a
    prev=[0x42de], succ=[]
    =================================
    0x3e8b: STOP 

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
    prev=[0x1181], succ=[0x24f4B0x1193]
    =================================
    0x1194: v1194(0x119d) = CONST 
    0x1198: v1198 = CALLER 
    0x1199: v1199(0x24f4) = CONST 
    0x119c: JUMP v1199(0x24f4)

    Begin block 0x24f4B0x1193
    prev=[0x1193], succ=[0x119d]
    =================================
    0x24f5S0x1193: v24f5V1193(0x1) = CONST 
    0x24f7S0x1193: v24f7V1193(0x1) = CONST 
    0x24f9S0x1193: v24f9V1193(0xa0) = CONST 
    0x24fbS0x1193: v24fbV1193(0x10000000000000000000000000000000000000000) = SHL v24f9V1193(0xa0), v24f7V1193(0x1)
    0x24fcS0x1193: v24fcV1193(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24fbV1193(0x10000000000000000000000000000000000000000), v24f5V1193(0x1)
    0x24ffS0x1193: v24ffV1193 = AND v24fcV1193(0xffffffffffffffffffffffffffffffffffffffff), v43d
    0x2500S0x1193: v2500V1193(0x0) = CONST 
    0x2504S0x1193: MSTORE v2500V1193(0x0), v24ffV1193
    0x2505S0x1193: v2505V1193(0x9) = CONST 
    0x2507S0x1193: v2507V1193(0x20) = CONST 
    0x250bS0x1193: MSTORE v2507V1193(0x20), v2505V1193(0x9)
    0x250cS0x1193: v250cV1193(0x40) = CONST 
    0x2510S0x1193: v2510V1193 = SHA3 v2500V1193(0x0), v250cV1193(0x40)
    0x2514S0x1193: v2514V1193 = AND v24fcV1193(0xffffffffffffffffffffffffffffffffffffffff), v1198
    0x2516S0x1193: MSTORE v2500V1193(0x0), v2514V1193
    0x251aS0x1193: MSTORE v2507V1193(0x20), v2510V1193
    0x251bS0x1193: v251bV1193 = SHA3 v2500V1193(0x0), v250cV1193(0x40)
    0x251cS0x1193: v251cV1193 = SLOAD v251bV1193
    0x251dS0x1193: v251dV1193(0xff) = CONST 
    0x251fS0x1193: v251fV1193 = AND v251dV1193(0xff), v251cV1193
    0x2521S0x1193: JUMP v1194(0x119d)

}

function removeMinter(address)() public {
    Begin block 0x5dc
    prev=[], succ=[0x5ee, 0x5f2]
    =================================
    0x5dd: v5dd(0x3eab) = CONST 
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
    prev=[0x13b4], succ=[0x3eab]
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
    0x1439: JUMP v5dd(0x3eab)

    Begin block 0x3eab
    prev=[0x1419], succ=[]
    =================================
    0x3eac: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x602
    prev=[], succ=[0x614, 0x618]
    =================================
    0x603: v603(0x3ecc) = CONST 
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
    prev=[0x143a], succ=[0x4304]
    =================================
    0x1490: v1490(0x4304) = CONST 
    0x1495: v1495(0x2af3) = CONST 
    0x1498: v1498_0 = CALLPRIVATE v1495(0x2af3), v629, v624, v1490(0x4304)

    Begin block 0x4304
    prev=[0x148f], succ=[0x3ecc]
    =================================
    0x430a: JUMP v603(0x3ecc)

    Begin block 0x3ecc
    prev=[0x4304], succ=[]
    =================================
    0x3ecd: v3ecd(0x40) = CONST 
    0x3ed0: v3ed0 = MLOAD v3ecd(0x40)
    0x3ed3: MSTORE v3ed0, v1498_0
    0x3ed4: v3ed4 = MLOAD v3ecd(0x40)
    0x3ed8: v3ed8(0x0) = SUB v3ed0, v3ed4
    0x3ed9: v3ed9(0x20) = CONST 
    0x3edb: v3edb(0x20) = ADD v3ed9(0x20), v3ed8(0x0)
    0x3edd: RETURN v3ed4, v3edb(0x20)

}

function initialize(address,address)() public {
    Begin block 0x62e
    prev=[], succ=[0x640, 0x644]
    =================================
    0x62f: v62f(0x3efd) = CONST 
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
    0x1583: v1583(0x3b48) = CONST 
    0x1586: v1586(0x28) = CONST 
    0x1589: CODECOPY v1581, v1583(0x3b48), v1586(0x28)
    0x158a: v158a(0x40) = CONST 
    0x158c: v158c = ADD v158a(0x40), v1581
    0x1590: v1590(0x40) = CONST 
    0x1592: v1592 = MLOAD v1590(0x40)
    0x1595: v1595(0x84) = SUB v158c, v1592
    0x1597: REVERT v1592, v1595(0x84)

    Begin block 0x1598
    prev=[0x1553], succ=[0x3efd]
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
    0x15d1: JUMP v62f(0x3efd)

    Begin block 0x3efd
    prev=[0x1598], succ=[]
    =================================
    0x3efe: STOP 

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
    0x15ff: v15ff(0x3b93) = CONST 
    0x1602: v1602(0x24) = CONST 
    0x1605: CODECOPY v15fd, v15ff(0x3b93), v1602(0x24)
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
    0xe710x65c: v65ce71(0x24b9) = CONST 
    0xe740x65c: v65ce74_0 = CALLPRIVATE v65ce71(0x24b9), v1692, v167e, v65ce6c(0xe75)

    Begin block 0xe750x65c
    prev=[0xe690x65c], succ=[0xe7b0x65c, 0xe820x65c]
    =================================
    0xe760x65c: v65ce76 = ISZERO v65ce74_0
    0xe770x65c: v65ce77(0xe82) = CONST 
    0xe7a0x65c: JUMPI v65ce77(0xe82), v65ce76

    Begin block 0xe7b0x65c
    prev=[0xe750x65c], succ=[0x424e0x65c]
    =================================
    0xe7c0x65c: v65ce7c(0x1) = CONST 
    0xe7e0x65c: v65ce7e(0x424e) = CONST 
    0xe810x65c: JUMP v65ce7e(0x424e)

    Begin block 0x424e0x65c
    prev=[0xe7b0x65c], succ=[0x1697]
    =================================
    0x42530x65c: JUMP v1668(0x1697)

    Begin block 0x1697
    prev=[0xe860x65c, 0x424e0x65c], succ=[0x16a2, 0x16a3]
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
    0x7d0: v7d0(0x3f1e) = CONST 
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
    0x173d: v173d(0x3be1) = CONST 
    0x1740: v1740(0x22) = CONST 
    0x1743: CODECOPY v173b, v173d(0x3be1), v1740(0x22)
    0x1744: v1744(0x40) = CONST 
    0x1746: v1746 = ADD v1744(0x40), v173b
    0x174a: v174a(0x40) = CONST 
    0x174c: v174c = MLOAD v174a(0x40)
    0x174f: v174f(0x84) = SUB v1746, v174c
    0x1751: REVERT v174c, v174f(0x84)

    Begin block 0x1752
    prev=[0x170d], succ=[0x3f1e]
    =================================
    0x1753: v1753(0x3) = CONST 
    0x1756: v1756 = SLOAD v1753(0x3)
    0x1757: v1757(0x1) = CONST 
    0x1759: v1759(0x1) = CONST 
    0x175b: v175b(0xa0) = CONST 
    0x175d: v175d(0x10000000000000000000000000000000000000000) = SHL v175b(0xa0), v1759(0x1)
    0x175e: v175e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v175d(0x10000000000000000000000000000000000000000), v1757(0x1)
    0x175f: v175f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v175e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1760: v1760 = AND v175f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1756
    0x1761: v1761(0x1) = CONST 
    0x1763: v1763(0x1) = CONST 
    0x1765: v1765(0xa0) = CONST 
    0x1767: v1767(0x10000000000000000000000000000000000000000) = SHL v1765(0xa0), v1763(0x1)
    0x1768: v1768(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1767(0x10000000000000000000000000000000000000000), v1761(0x1)
    0x176b: v176b = AND v1768(0xffffffffffffffffffffffffffffffffffffffff), v7f0
    0x176e: v176e = OR v176b, v1760
    0x1772: SSTORE v1753(0x3), v176e
    0x1773: v1773(0x40) = CONST 
    0x1775: v1775 = MLOAD v1773(0x40)
    0x1778: v1778 = AND v176e, v1768(0xffffffffffffffffffffffffffffffffffffffff)
    0x177a: v177a(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x179c: v179c(0x0) = CONST 
    0x179f: LOG3 v1775, v179c(0x0), v177a(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1778, v176b
    0x17a1: JUMP v7d0(0x3f1e)

    Begin block 0x3f1e
    prev=[0x1752], succ=[]
    =================================
    0x3f1f: STOP 

}

function burnQuasar(address,uint256)() public {
    Begin block 0x7f5
    prev=[], succ=[0x807, 0x80b]
    =================================
    0x7f6: v7f6(0x3f3f) = CONST 
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
    prev=[0x7f5], succ=[0x17a2]
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
    0x81d: v81d(0x17a2) = CONST 
    0x820: JUMP v81d(0x17a2)

    Begin block 0x17a2
    prev=[0x80b], succ=[0x17ba, 0x17f7]
    =================================
    0x17a3: v17a3 = CALLER 
    0x17a4: v17a4(0x0) = CONST 
    0x17a8: MSTORE v17a4(0x0), v17a3
    0x17a9: v17a9(0x5) = CONST 
    0x17ab: v17ab(0x20) = CONST 
    0x17ad: MSTORE v17ab(0x20), v17a9(0x5)
    0x17ae: v17ae(0x40) = CONST 
    0x17b1: v17b1 = SHA3 v17a4(0x0), v17ae(0x40)
    0x17b2: v17b2 = SLOAD v17b1
    0x17b3: v17b3(0xff) = CONST 
    0x17b5: v17b5 = AND v17b3(0xff), v17b2
    0x17b6: v17b6(0x17f7) = CONST 
    0x17b9: JUMPI v17b6(0x17f7), v17b5

    Begin block 0x17ba
    prev=[0x17a2], succ=[]
    =================================
    0x17ba: v17ba(0x40) = CONST 
    0x17bd: v17bd = MLOAD v17ba(0x40)
    0x17be: v17be(0x461bcd) = CONST 
    0x17c2: v17c2(0xe5) = CONST 
    0x17c4: v17c4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17c2(0xe5), v17be(0x461bcd)
    0x17c6: MSTORE v17bd, v17c4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17c7: v17c7(0x20) = CONST 
    0x17c9: v17c9(0x4) = CONST 
    0x17cc: v17cc = ADD v17bd, v17c9(0x4)
    0x17cd: MSTORE v17cc, v17c7(0x20)
    0x17ce: v17ce(0xe) = CONST 
    0x17d0: v17d0(0x24) = CONST 
    0x17d3: v17d3 = ADD v17bd, v17d0(0x24)
    0x17d4: MSTORE v17d3, v17ce(0xe)
    0x17d5: v17d5(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x17e4: v17e4(0x91) = CONST 
    0x17e6: v17e6(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v17e4(0x91), v17d5(0x36bab9ba1031329036b4b73a32b9)
    0x17e7: v17e7(0x44) = CONST 
    0x17ea: v17ea = ADD v17bd, v17e7(0x44)
    0x17eb: MSTORE v17ea, v17e6(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x17ed: v17ed = MLOAD v17ba(0x40)
    0x17f1: v17f1(0x0) = SUB v17bd, v17ed
    0x17f2: v17f2(0x64) = CONST 
    0x17f4: v17f4(0x64) = ADD v17f2(0x64), v17f1(0x0)
    0x17f6: REVERT v17ed, v17f4(0x64)

    Begin block 0x17f7
    prev=[0x17a2], succ=[0x1801]
    =================================
    0x17f8: v17f8(0x1801) = CONST 
    0x17fd: v17fd(0x24b9) = CONST 
    0x1800: v1800_0 = CALLPRIVATE v17fd(0x24b9), v81c, v817, v17f8(0x1801)

    Begin block 0x1801
    prev=[0x17f7], succ=[0x1806, 0x1842]
    =================================
    0x1802: v1802(0x1842) = CONST 
    0x1805: JUMPI v1802(0x1842), v1800_0

    Begin block 0x1806
    prev=[0x1801], succ=[]
    =================================
    0x1806: v1806(0x40) = CONST 
    0x1809: v1809 = MLOAD v1806(0x40)
    0x180a: v180a(0x461bcd) = CONST 
    0x180e: v180e(0xe5) = CONST 
    0x1810: v1810(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v180e(0xe5), v180a(0x461bcd)
    0x1812: MSTORE v1809, v1810(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1813: v1813(0x20) = CONST 
    0x1815: v1815(0x4) = CONST 
    0x1818: v1818 = ADD v1809, v1815(0x4)
    0x1819: MSTORE v1818, v1813(0x20)
    0x181a: v181a(0xd) = CONST 
    0x181c: v181c(0x24) = CONST 
    0x181f: v181f = ADD v1809, v181c(0x24)
    0x1820: MSTORE v181f, v181a(0xd)
    0x1821: v1821(0x2737ba103a34329037bbb732b9) = CONST 
    0x182f: v182f(0x99) = CONST 
    0x1831: v1831(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v182f(0x99), v1821(0x2737ba103a34329037bbb732b9)
    0x1832: v1832(0x44) = CONST 
    0x1835: v1835 = ADD v1809, v1832(0x44)
    0x1836: MSTORE v1835, v1831(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1838: v1838 = MLOAD v1806(0x40)
    0x183c: v183c(0x0) = SUB v1809, v1838
    0x183d: v183d(0x64) = CONST 
    0x183f: v183f(0x64) = ADD v183d(0x64), v183c(0x0)
    0x1841: REVERT v1838, v183f(0x64)

    Begin block 0x1842
    prev=[0x1801], succ=[0x2c4b]
    =================================
    0x1843: v1843(0x432a) = CONST 
    0x1847: v1847(0x2c4b) = CONST 
    0x184a: JUMP v1847(0x2c4b)

    Begin block 0x2c4b
    prev=[0x1842], succ=[0x432a]
    =================================
    0x2c4c: v2c4c(0x0) = CONST 
    0x2c50: MSTORE v2c4c(0x0), v81c
    0x2c51: v2c51(0xb) = CONST 
    0x2c53: v2c53(0x20) = CONST 
    0x2c55: MSTORE v2c53(0x20), v2c51(0xb)
    0x2c56: v2c56(0x40) = CONST 
    0x2c5a: v2c5a = SHA3 v2c4c(0x0), v2c56(0x40)
    0x2c5c: v2c5c = SLOAD v2c5a
    0x2c5d: v2c5d(0x1) = CONST 
    0x2c5f: v2c5f(0x1) = CONST 
    0x2c61: v2c61(0xa0) = CONST 
    0x2c63: v2c63(0x10000000000000000000000000000000000000000) = SHL v2c61(0xa0), v2c5f(0x1)
    0x2c64: v2c64(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c63(0x10000000000000000000000000000000000000000), v2c5d(0x1)
    0x2c65: v2c65(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2c64(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c66: v2c66 = AND v2c65(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2c5c
    0x2c68: SSTORE v2c5a, v2c66
    0x2c69: v2c69(0x1) = CONST 
    0x2c6c: v2c6c = ADD v2c5a, v2c69(0x1)
    0x2c6f: SSTORE v2c6c, v2c4c(0x0)
    0x2c70: v2c70(0x2) = CONST 
    0x2c72: v2c72 = ADD v2c70(0x2), v2c5a
    0x2c75: SSTORE v2c72, v2c4c(0x0)
    0x2c76: v2c76 = MLOAD v2c56(0x40)
    0x2c79: v2c79(0xbde0a9e22c5839cdde2897048c98e5ac02b30c945ac1c44d3fd76237ab021c) = CONST 
    0x2c9a: LOG2 v2c76, v2c4c(0x0), v2c79(0xbde0a9e22c5839cdde2897048c98e5ac02b30c945ac1c44d3fd76237ab021c), v81c
    0x2c9c: JUMP v1843(0x432a)

    Begin block 0x432a
    prev=[0x2c4b], succ=[0x3f3f]
    =================================
    0x432d: JUMP v7f6(0x3f3f)

    Begin block 0x3f3f
    prev=[0x432a], succ=[]
    =================================
    0x3f40: STOP 

}

function baseURI()() public {
    Begin block 0x821
    prev=[], succ=[0x35c0x821]
    =================================
    0x822: v822(0x35c) = CONST 
    0x825: v825(0x184b) = CONST 
    0x828: v828_0 = CALLPRIVATE v825(0x184b), v822(0x35c)

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
    0x82a: v82a(0x3f60) = CONST 
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
    prev=[0x829], succ=[0x18de]
    =================================
    0x841: v841 = CALLDATALOAD v82d(0x4)
    0x842: v842(0x1) = CONST 
    0x844: v844(0x1) = CONST 
    0x846: v846(0xa0) = CONST 
    0x848: v848(0x10000000000000000000000000000000000000000) = SHL v846(0xa0), v844(0x1)
    0x849: v849(0xffffffffffffffffffffffffffffffffffffffff) = SUB v848(0x10000000000000000000000000000000000000000), v842(0x1)
    0x84a: v84a = AND v849(0xffffffffffffffffffffffffffffffffffffffff), v841
    0x84b: v84b(0x18de) = CONST 
    0x84e: JUMP v84b(0x18de)

    Begin block 0x18de
    prev=[0x83f], succ=[0x3f60]
    =================================
    0x18df: v18df(0x1) = CONST 
    0x18e1: v18e1(0x1) = CONST 
    0x18e3: v18e3(0xa0) = CONST 
    0x18e5: v18e5(0x10000000000000000000000000000000000000000) = SHL v18e3(0xa0), v18e1(0x1)
    0x18e6: v18e6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18e5(0x10000000000000000000000000000000000000000), v18df(0x1)
    0x18e7: v18e7 = AND v18e6(0xffffffffffffffffffffffffffffffffffffffff), v84a
    0x18e8: v18e8(0x0) = CONST 
    0x18ec: MSTORE v18e8(0x0), v18e7
    0x18ed: v18ed(0x6) = CONST 
    0x18ef: v18ef(0x20) = CONST 
    0x18f1: MSTORE v18ef(0x20), v18ed(0x6)
    0x18f2: v18f2(0x40) = CONST 
    0x18f5: v18f5 = SHA3 v18e8(0x0), v18f2(0x40)
    0x18f6: v18f6 = SLOAD v18f5
    0x18f7: v18f7(0xff) = CONST 
    0x18f9: v18f9 = AND v18f7(0xff), v18f6
    0x18fb: JUMP v82a(0x3f60)

    Begin block 0x3f60
    prev=[0x18de], succ=[]
    =================================
    0x3f61: v3f61(0x40) = CONST 
    0x3f64: v3f64 = MLOAD v3f61(0x40)
    0x3f66: v3f66 = ISZERO v18f9
    0x3f67: v3f67 = ISZERO v3f66
    0x3f69: MSTORE v3f64, v3f67
    0x3f6a: v3f6a = MLOAD v3f61(0x40)
    0x3f6e: v3f6e(0x0) = SUB v3f64, v3f6a
    0x3f6f: v3f6f(0x20) = CONST 
    0x3f71: v3f71(0x20) = ADD v3f6f(0x20), v3f6e(0x0)
    0x3f73: RETURN v3f6a, v3f71(0x20)

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
    prev=[0x8a6], succ=[0x18fc]
    =================================
    0x8ce: v8ce(0x18fc) = CONST 
    0x8d1: JUMP v8ce(0x18fc)

    Begin block 0x18fc
    prev=[0x8c7], succ=[0x1917, 0x1954]
    =================================
    0x18fd: v18fd = CALLER 
    0x18fe: v18fe(0x0) = CONST 
    0x1902: MSTORE v18fe(0x0), v18fd
    0x1903: v1903(0x5) = CONST 
    0x1905: v1905(0x20) = CONST 
    0x1907: MSTORE v1905(0x20), v1903(0x5)
    0x1908: v1908(0x40) = CONST 
    0x190b: v190b = SHA3 v18fe(0x0), v1908(0x40)
    0x190c: v190c = SLOAD v190b
    0x190d: v190d(0x60) = CONST 
    0x1910: v1910(0xff) = CONST 
    0x1912: v1912 = AND v1910(0xff), v190c
    0x1913: v1913(0x1954) = CONST 
    0x1916: JUMPI v1913(0x1954), v1912

    Begin block 0x1917
    prev=[0x18fc], succ=[]
    =================================
    0x1917: v1917(0x40) = CONST 
    0x191a: v191a = MLOAD v1917(0x40)
    0x191b: v191b(0x461bcd) = CONST 
    0x191f: v191f(0xe5) = CONST 
    0x1921: v1921(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v191f(0xe5), v191b(0x461bcd)
    0x1923: MSTORE v191a, v1921(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1924: v1924(0x20) = CONST 
    0x1926: v1926(0x4) = CONST 
    0x1929: v1929 = ADD v191a, v1926(0x4)
    0x192a: MSTORE v1929, v1924(0x20)
    0x192b: v192b(0xe) = CONST 
    0x192d: v192d(0x24) = CONST 
    0x1930: v1930 = ADD v191a, v192d(0x24)
    0x1931: MSTORE v1930, v192b(0xe)
    0x1932: v1932(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x1941: v1941(0x91) = CONST 
    0x1943: v1943(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v1941(0x91), v1932(0x36bab9ba1031329036b4b73a32b9)
    0x1944: v1944(0x44) = CONST 
    0x1947: v1947 = ADD v191a, v1944(0x44)
    0x1948: MSTORE v1947, v1943(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x194a: v194a = MLOAD v1917(0x40)
    0x194e: v194e(0x0) = SUB v191a, v194a
    0x194f: v194f(0x64) = CONST 
    0x1951: v1951(0x64) = ADD v194f(0x64), v194e(0x0)
    0x1953: REVERT v194a, v1951(0x64)

    Begin block 0x1954
    prev=[0x18fc], succ=[0x1963, 0x19af]
    =================================
    0x1955: v1955(0x1) = CONST 
    0x1957: v1957(0x1) = CONST 
    0x1959: v1959(0xa0) = CONST 
    0x195b: v195b(0x10000000000000000000000000000000000000000) = SHL v1959(0xa0), v1957(0x1)
    0x195c: v195c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v195b(0x10000000000000000000000000000000000000000), v1955(0x1)
    0x195e: v195e = AND v870, v195c(0xffffffffffffffffffffffffffffffffffffffff)
    0x195f: v195f(0x19af) = CONST 
    0x1962: JUMPI v195f(0x19af), v195e

    Begin block 0x1963
    prev=[0x1954], succ=[]
    =================================
    0x1963: v1963(0x40) = CONST 
    0x1966: v1966 = MLOAD v1963(0x40)
    0x1967: v1967(0x461bcd) = CONST 
    0x196b: v196b(0xe5) = CONST 
    0x196d: v196d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v196b(0xe5), v1967(0x461bcd)
    0x196f: MSTORE v1966, v196d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1970: v1970(0x20) = CONST 
    0x1972: v1972(0x4) = CONST 
    0x1975: v1975 = ADD v1966, v1972(0x4)
    0x1976: MSTORE v1975, v1970(0x20)
    0x1977: v1977(0x1d) = CONST 
    0x1979: v1979(0x24) = CONST 
    0x197c: v197c = ADD v1966, v1979(0x24)
    0x197d: MSTORE v197c, v1977(0x1d)
    0x197e: v197e(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x199f: v199f(0x44) = CONST 
    0x19a2: v19a2 = ADD v1966, v199f(0x44)
    0x19a3: MSTORE v19a2, v197e(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x19a5: v19a5 = MLOAD v1963(0x40)
    0x19a9: v19a9(0x0) = SUB v1966, v19a5
    0x19aa: v19aa(0x64) = CONST 
    0x19ac: v19ac(0x64) = ADD v19aa(0x64), v19a9(0x0)
    0x19ae: REVERT v19a5, v19ac(0x64)

    Begin block 0x19af
    prev=[0x1954], succ=[0x19b7, 0x19ed]
    =================================
    0x19b2: v19b2 = EQ v876, v8a8
    0x19b3: v19b3(0x19ed) = CONST 
    0x19b6: JUMPI v19b3(0x19ed), v19b2

    Begin block 0x19b7
    prev=[0x19af], succ=[]
    =================================
    0x19b7: v19b7(0x40) = CONST 
    0x19b9: v19b9 = MLOAD v19b7(0x40)
    0x19ba: v19ba(0x461bcd) = CONST 
    0x19be: v19be(0xe5) = CONST 
    0x19c0: v19c0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19be(0xe5), v19ba(0x461bcd)
    0x19c2: MSTORE v19b9, v19c0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19c3: v19c3(0x4) = CONST 
    0x19c5: v19c5 = ADD v19c3(0x4), v19b9
    0x19c8: v19c8(0x20) = CONST 
    0x19ca: v19ca = ADD v19c8(0x20), v19c5
    0x19cd: v19cd(0x20) = SUB v19ca, v19c5
    0x19cf: MSTORE v19c5, v19cd(0x20)
    0x19d0: v19d0(0x2a) = CONST 
    0x19d3: MSTORE v19ca, v19d0(0x2a)
    0x19d4: v19d4(0x20) = CONST 
    0x19d6: v19d6 = ADD v19d4(0x20), v19ca
    0x19d8: v19d8(0x3c03) = CONST 
    0x19db: v19db(0x2a) = CONST 
    0x19de: CODECOPY v19d6, v19d8(0x3c03), v19db(0x2a)
    0x19df: v19df(0x40) = CONST 
    0x19e1: v19e1 = ADD v19df(0x40), v19d6
    0x19e5: v19e5(0x40) = CONST 
    0x19e7: v19e7 = MLOAD v19e5(0x40)
    0x19ea: v19ea(0x84) = SUB v19e1, v19e7
    0x19ec: REVERT v19e7, v19ea(0x84)

    Begin block 0x19ed
    prev=[0x19af], succ=[0x2c9dB0x19ed]
    =================================
    0x19ee: v19ee(0x439f) = CONST 
    0x19f5: v19f5(0x2c9d) = CONST 
    0x19f8: JUMP v19f5(0x2c9d)

    Begin block 0x2c9dB0x19ed
    prev=[0x19ed], succ=[0x2cb4B0x19ed, 0x2cb8B0x19ed]
    =================================
    0x2c9eS0x19ed: v2c9eV19ed(0x60) = CONST 
    0x2ca0S0x19ed: v2ca0V19ed(0x0) = CONST 
    0x2ca3S0x19ed: v2ca3V19ed(0xffffffffffffffff) = CONST 
    0x2cadS0x19ed: v2cadV19ed = GT v876, v2ca3V19ed(0xffffffffffffffff)
    0x2cafS0x19ed: v2cafV19ed = ISZERO v2cadV19ed
    0x2cb0S0x19ed: v2cb0V19ed(0x2cb8) = CONST 
    0x2cb3S0x19ed: JUMPI v2cb0V19ed(0x2cb8), v2cafV19ed

    Begin block 0x2cb4B0x19ed
    prev=[0x2c9dB0x19ed], succ=[]
    =================================
    0x2cb4S0x19ed: v2cb4V19ed(0x0) = CONST 
    0x2cb7S0x19ed: REVERT v2cb4V19ed(0x0), v2cb4V19ed(0x0)

    Begin block 0x2cb8B0x19ed
    prev=[0x2c9dB0x19ed], succ=[0x2ce2B0x19ed, 0x2cd3B0x19ed]
    =================================
    0x2cbaS0x19ed: v2cbaV19ed(0x40) = CONST 
    0x2cbcS0x19ed: v2cbcV19ed = MLOAD v2cbaV19ed(0x40)
    0x2cc0S0x19ed: MSTORE v2cbcV19ed, v876
    0x2cc2S0x19ed: v2cc2V19ed(0x20) = CONST 
    0x2cc4S0x19ed: v2cc4V19ed = MUL v2cc2V19ed(0x20), v876
    0x2cc5S0x19ed: v2cc5V19ed(0x20) = CONST 
    0x2cc7S0x19ed: v2cc7V19ed = ADD v2cc5V19ed(0x20), v2cc4V19ed
    0x2cc9S0x19ed: v2cc9V19ed = ADD v2cbcV19ed, v2cc7V19ed
    0x2ccaS0x19ed: v2ccaV19ed(0x40) = CONST 
    0x2cccS0x19ed: MSTORE v2ccaV19ed(0x40), v2cc9V19ed
    0x2cceS0x19ed: v2cceV19ed = ISZERO v876
    0x2ccfS0x19ed: v2ccfV19ed(0x2ce2) = CONST 
    0x2cd2S0x19ed: JUMPI v2ccfV19ed(0x2ce2), v2cceV19ed

    Begin block 0x2ce2B0x19ed
    prev=[0x2cb8B0x19ed, 0x2cd3B0x19ed], succ=[0x2cfaB0x19ed, 0x2cfeB0x19ed]
    =================================
    0x2ce6S0x19ed: v2ce6V19ed(0x0) = CONST 
    0x2ce9S0x19ed: v2ce9V19ed(0xffffffffffffffff) = CONST 
    0x2cf3S0x19ed: v2cf3V19ed = GT v876, v2ce9V19ed(0xffffffffffffffff)
    0x2cf5S0x19ed: v2cf5V19ed = ISZERO v2cf3V19ed
    0x2cf6S0x19ed: v2cf6V19ed(0x2cfe) = CONST 
    0x2cf9S0x19ed: JUMPI v2cf6V19ed(0x2cfe), v2cf5V19ed

    Begin block 0x2cfaB0x19ed
    prev=[0x2ce2B0x19ed], succ=[]
    =================================
    0x2cfaS0x19ed: v2cfaV19ed(0x0) = CONST 
    0x2cfdS0x19ed: REVERT v2cfaV19ed(0x0), v2cfaV19ed(0x0)

    Begin block 0x2cfeB0x19ed
    prev=[0x2ce2B0x19ed], succ=[0x2d28B0x19ed, 0x2d19B0x19ed]
    =================================
    0x2d00S0x19ed: v2d00V19ed(0x40) = CONST 
    0x2d02S0x19ed: v2d02V19ed = MLOAD v2d00V19ed(0x40)
    0x2d06S0x19ed: MSTORE v2d02V19ed, v876
    0x2d08S0x19ed: v2d08V19ed(0x20) = CONST 
    0x2d0aS0x19ed: v2d0aV19ed = MUL v2d08V19ed(0x20), v876
    0x2d0bS0x19ed: v2d0bV19ed(0x20) = CONST 
    0x2d0dS0x19ed: v2d0dV19ed = ADD v2d0bV19ed(0x20), v2d0aV19ed
    0x2d0fS0x19ed: v2d0fV19ed = ADD v2d02V19ed, v2d0dV19ed
    0x2d10S0x19ed: v2d10V19ed(0x40) = CONST 
    0x2d12S0x19ed: MSTORE v2d10V19ed(0x40), v2d0fV19ed
    0x2d14S0x19ed: v2d14V19ed = ISZERO v876
    0x2d15S0x19ed: v2d15V19ed(0x2d28) = CONST 
    0x2d18S0x19ed: JUMPI v2d15V19ed(0x2d28), v2d14V19ed

    Begin block 0x2d28B0x19ed
    prev=[0x2cfeB0x19ed, 0x2d19B0x19ed], succ=[0x2d2eB0x19ed]
    =================================
    0x2d2cS0x19ed: v2d2cV19ed(0x0) = CONST 

    Begin block 0x2d2eB0x19ed
    prev=[0x2d28B0x19ed, 0x2e42B0x19ed], succ=[0x2d38B0x19ed, 0x2e55B0x19ed]
    =================================
    0x2d2e_0x0S0x19ed: v2d2e_0V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2d30S0x19ed: v2d30V19ed = MLOAD v2cbcV19ed
    0x2d32S0x19ed: v2d32V19ed = LT v2d2e_0V19ed, v2d30V19ed
    0x2d33S0x19ed: v2d33V19ed = ISZERO v2d32V19ed
    0x2d34S0x19ed: v2d34V19ed(0x2e55) = CONST 
    0x2d37S0x19ed: JUMPI v2d34V19ed(0x2e55), v2d33V19ed

    Begin block 0x2d38B0x19ed
    prev=[0x2d2eB0x19ed], succ=[0x2d90B0x19ed, 0x2d8fB0x19ed]
    =================================
    0x2d38S0x19ed: v2d38V19ed(0x7) = CONST 
    0x2d38_0x0S0x19ed: v2d38_0V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2d3bS0x19ed: v2d3bV19ed = SLOAD v2d38V19ed(0x7)
    0x2d3cS0x19ed: v2d3cV19ed(0x1) = CONST 
    0x2d3eS0x19ed: v2d3eV19ed = ADD v2d3cV19ed(0x1), v2d3bV19ed
    0x2d42S0x19ed: SSTORE v2d38V19ed(0x7), v2d3eV19ed
    0x2d43S0x19ed: v2d43V19ed(0x0) = CONST 
    0x2d47S0x19ed: MSTORE v2d43V19ed(0x0), v2d3eV19ed
    0x2d48S0x19ed: v2d48V19ed(0x8) = CONST 
    0x2d4aS0x19ed: v2d4aV19ed(0x20) = CONST 
    0x2d4eS0x19ed: MSTORE v2d4aV19ed(0x20), v2d48V19ed(0x8)
    0x2d4fS0x19ed: v2d4fV19ed(0x40) = CONST 
    0x2d54S0x19ed: v2d54V19ed = SHA3 v2d43V19ed(0x0), v2d4fV19ed(0x40)
    0x2d56S0x19ed: v2d56V19ed = SLOAD v2d54V19ed
    0x2d57S0x19ed: v2d57V19ed(0x1) = CONST 
    0x2d59S0x19ed: v2d59V19ed(0x1) = CONST 
    0x2d5bS0x19ed: v2d5bV19ed(0xa0) = CONST 
    0x2d5dS0x19ed: v2d5dV19ed(0x10000000000000000000000000000000000000000) = SHL v2d5bV19ed(0xa0), v2d59V19ed(0x1)
    0x2d5eS0x19ed: v2d5eV19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d5dV19ed(0x10000000000000000000000000000000000000000), v2d57V19ed(0x1)
    0x2d5fS0x19ed: v2d5fV19ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2d5eV19ed(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d60S0x19ed: v2d60V19ed = AND v2d5fV19ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2d56V19ed
    0x2d61S0x19ed: v2d61V19ed(0x1) = CONST 
    0x2d63S0x19ed: v2d63V19ed(0x1) = CONST 
    0x2d65S0x19ed: v2d65V19ed(0xa0) = CONST 
    0x2d67S0x19ed: v2d67V19ed(0x10000000000000000000000000000000000000000) = SHL v2d65V19ed(0xa0), v2d63V19ed(0x1)
    0x2d68S0x19ed: v2d68V19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d67V19ed(0x10000000000000000000000000000000000000000), v2d61V19ed(0x1)
    0x2d6aS0x19ed: v2d6aV19ed = AND v870, v2d68V19ed(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d6bS0x19ed: v2d6bV19ed = OR v2d6aV19ed, v2d60V19ed
    0x2d6dS0x19ed: SSTORE v2d54V19ed, v2d6bV19ed
    0x2d6fS0x19ed: v2d6fV19ed = MLOAD v2d4fV19ed(0x40)
    0x2d70S0x19ed: v2d70V19ed(0x60) = CONST 
    0x2d73S0x19ed: v2d73V19ed = ADD v2d6fV19ed, v2d70V19ed(0x60)
    0x2d76S0x19ed: MSTORE v2d4fV19ed(0x40), v2d73V19ed
    0x2d77S0x19ed: v2d77V19ed = NUMBER 
    0x2d78S0x19ed: v2d78V19ed(0x1) = CONST 
    0x2d7aS0x19ed: v2d7aV19ed(0x1) = CONST 
    0x2d7cS0x19ed: v2d7cV19ed(0x80) = CONST 
    0x2d7eS0x19ed: v2d7eV19ed(0x100000000000000000000000000000000) = SHL v2d7cV19ed(0x80), v2d7aV19ed(0x1)
    0x2d7fS0x19ed: v2d7fV19ed(0xffffffffffffffffffffffffffffffff) = SUB v2d7eV19ed(0x100000000000000000000000000000000), v2d78V19ed(0x1)
    0x2d80S0x19ed: v2d80V19ed = AND v2d7fV19ed(0xffffffffffffffffffffffffffffffff), v2d77V19ed
    0x2d82S0x19ed: MSTORE v2d6fV19ed, v2d80V19ed
    0x2d84S0x19ed: v2d84V19ed = ADD v2d6fV19ed, v2d4aV19ed(0x20)
    0x2d8aS0x19ed: v2d8aV19ed = LT v2d38_0V19ed, v8a8
    0x2d8bS0x19ed: v2d8bV19ed(0x2d90) = CONST 
    0x2d8eS0x19ed: JUMPI v2d8bV19ed(0x2d90), v2d8aV19ed

    Begin block 0x2d90B0x19ed
    prev=[0x2d38B0x19ed], succ=[0x2e28B0x19ed, 0x2e27B0x19ed]
    =================================
    0x2d90_0x0S0x19ed: v2d90_0V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2d90_0x5S0x19ed: v2d90_5V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2d91S0x19ed: v2d91V19ed(0x1) = CONST 
    0x2d93S0x19ed: v2d93V19ed(0x1) = CONST 
    0x2d95S0x19ed: v2d95V19ed(0x80) = CONST 
    0x2d97S0x19ed: v2d97V19ed(0x100000000000000000000000000000000) = SHL v2d95V19ed(0x80), v2d93V19ed(0x1)
    0x2d98S0x19ed: v2d98V19ed(0xffffffffffffffffffffffffffffffff) = SUB v2d97V19ed(0x100000000000000000000000000000000), v2d91V19ed(0x1)
    0x2d99S0x19ed: v2d99V19ed(0x20) = CONST 
    0x2d9dS0x19ed: v2d9dV19ed = MUL v2d99V19ed(0x20), v2d90_0V19ed
    0x2da1S0x19ed: v2da1V19ed = ADD v2d9dV19ed, v8ac
    0x2da2S0x19ed: v2da2V19ed = CALLDATALOAD v2da1V19ed
    0x2da4S0x19ed: v2da4V19ed = AND v2d98V19ed(0xffffffffffffffffffffffffffffffff), v2da2V19ed
    0x2da6S0x19ed: MSTORE v2d84V19ed, v2da4V19ed
    0x2da7S0x19ed: v2da7V19ed(0x1) = CONST 
    0x2da9S0x19ed: v2da9V19ed(0x1) = CONST 
    0x2dabS0x19ed: v2dabV19ed(0xa0) = CONST 
    0x2dadS0x19ed: v2dadV19ed(0x10000000000000000000000000000000000000000) = SHL v2dabV19ed(0xa0), v2da9V19ed(0x1)
    0x2daeS0x19ed: v2daeV19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2dadV19ed(0x10000000000000000000000000000000000000000), v2da7V19ed(0x1)
    0x2db1S0x19ed: v2db1V19ed = AND v870, v2daeV19ed(0xffffffffffffffffffffffffffffffffffffffff)
    0x2db4S0x19ed: v2db4V19ed = ADD v2d99V19ed(0x20), v2d84V19ed
    0x2db8S0x19ed: MSTORE v2db4V19ed, v2db1V19ed
    0x2db9S0x19ed: v2db9V19ed(0x7) = CONST 
    0x2dbcS0x19ed: v2dbcV19ed = SLOAD v2db9V19ed(0x7)
    0x2dbdS0x19ed: v2dbdV19ed(0x0) = CONST 
    0x2dc1S0x19ed: MSTORE v2dbdV19ed(0x0), v2dbcV19ed
    0x2dc2S0x19ed: v2dc2V19ed(0xa) = CONST 
    0x2dc5S0x19ed: MSTORE v2d99V19ed(0x20), v2dc2V19ed(0xa)
    0x2dc6S0x19ed: v2dc6V19ed(0x40) = CONST 
    0x2dcbS0x19ed: v2dcbV19ed = SHA3 v2dbdV19ed(0x0), v2dc6V19ed(0x40)
    0x2dcdS0x19ed: v2dcdV19ed = MLOAD v2d6fV19ed
    0x2dcfS0x19ed: v2dcfV19ed = SLOAD v2dcbV19ed
    0x2dd2S0x19ed: v2dd2V19ed = ADD v2d6fV19ed, v2d99V19ed(0x20)
    0x2dd3S0x19ed: v2dd3V19ed = MLOAD v2dd2V19ed
    0x2dd5S0x19ed: v2dd5V19ed = AND v2d98V19ed(0xffffffffffffffffffffffffffffffff), v2dd3V19ed
    0x2dd6S0x19ed: v2dd6V19ed(0x1) = CONST 
    0x2dd8S0x19ed: v2dd8V19ed(0x80) = CONST 
    0x2ddaS0x19ed: v2ddaV19ed(0x100000000000000000000000000000000) = SHL v2dd8V19ed(0x80), v2dd6V19ed(0x1)
    0x2ddbS0x19ed: v2ddbV19ed = MUL v2ddaV19ed(0x100000000000000000000000000000000), v2dd5V19ed
    0x2ddeS0x19ed: v2ddeV19ed = AND v2d98V19ed(0xffffffffffffffffffffffffffffffff), v2dcdV19ed
    0x2ddfS0x19ed: v2ddfV19ed(0x1) = CONST 
    0x2de1S0x19ed: v2de1V19ed(0x1) = CONST 
    0x2de3S0x19ed: v2de3V19ed(0x80) = CONST 
    0x2de5S0x19ed: v2de5V19ed(0x100000000000000000000000000000000) = SHL v2de3V19ed(0x80), v2de1V19ed(0x1)
    0x2de6S0x19ed: v2de6V19ed(0xffffffffffffffffffffffffffffffff) = SUB v2de5V19ed(0x100000000000000000000000000000000), v2ddfV19ed(0x1)
    0x2de7S0x19ed: v2de7V19ed(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) = NOT v2de6V19ed(0xffffffffffffffffffffffffffffffff)
    0x2deaS0x19ed: v2deaV19ed = AND v2dcfV19ed, v2de7V19ed(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000)
    0x2deeS0x19ed: v2deeV19ed = OR v2deaV19ed, v2ddeV19ed
    0x2df1S0x19ed: v2df1V19ed = AND v2d98V19ed(0xffffffffffffffffffffffffffffffff), v2deeV19ed
    0x2df5S0x19ed: v2df5V19ed = OR v2df1V19ed, v2ddbV19ed
    0x2df7S0x19ed: SSTORE v2dcbV19ed, v2df5V19ed
    0x2df9S0x19ed: v2df9V19ed = ADD v2d6fV19ed, v2dc6V19ed(0x40)
    0x2dfaS0x19ed: v2dfaV19ed = MLOAD v2df9V19ed
    0x2dfbS0x19ed: v2dfbV19ed(0x1) = CONST 
    0x2dffS0x19ed: v2dffV19ed = ADD v2dcbV19ed, v2dfbV19ed(0x1)
    0x2e01S0x19ed: v2e01V19ed = SLOAD v2dffV19ed
    0x2e05S0x19ed: v2e05V19ed = AND v2daeV19ed(0xffffffffffffffffffffffffffffffffffffffff), v2dfaV19ed
    0x2e06S0x19ed: v2e06V19ed(0x1) = CONST 
    0x2e08S0x19ed: v2e08V19ed(0x1) = CONST 
    0x2e0aS0x19ed: v2e0aV19ed(0xa0) = CONST 
    0x2e0cS0x19ed: v2e0cV19ed(0x10000000000000000000000000000000000000000) = SHL v2e0aV19ed(0xa0), v2e08V19ed(0x1)
    0x2e0dS0x19ed: v2e0dV19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e0cV19ed(0x10000000000000000000000000000000000000000), v2e06V19ed(0x1)
    0x2e0eS0x19ed: v2e0eV19ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2e0dV19ed(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e11S0x19ed: v2e11V19ed = AND v2e01V19ed, v2e0eV19ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x2e15S0x19ed: v2e15V19ed = OR v2e11V19ed, v2e05V19ed
    0x2e18S0x19ed: SSTORE v2dffV19ed, v2e15V19ed
    0x2e1aS0x19ed: v2e1aV19ed = SLOAD v2db9V19ed(0x7)
    0x2e1cS0x19ed: v2e1cV19ed = MLOAD v2cbcV19ed
    0x2e22S0x19ed: v2e22V19ed = LT v2d90_5V19ed, v2e1cV19ed
    0x2e23S0x19ed: v2e23V19ed(0x2e28) = CONST 
    0x2e26S0x19ed: JUMPI v2e23V19ed(0x2e28), v2e22V19ed

    Begin block 0x2e28B0x19ed
    prev=[0x2d90B0x19ed], succ=[0x2e42B0x19ed, 0x2e41B0x19ed]
    =================================
    0x2e28_0x0S0x19ed: v2e28_0V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2e28_0x3S0x19ed: v2e28_3V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2e29S0x19ed: v2e29V19ed(0x20) = CONST 
    0x2e2bS0x19ed: v2e2bV19ed = MUL v2e29V19ed(0x20), v2e28_0V19ed
    0x2e2cS0x19ed: v2e2cV19ed(0x20) = CONST 
    0x2e2eS0x19ed: v2e2eV19ed = ADD v2e2cV19ed(0x20), v2e2bV19ed
    0x2e2fS0x19ed: v2e2fV19ed = ADD v2e2eV19ed, v2cbcV19ed
    0x2e32S0x19ed: MSTORE v2e2fV19ed, v2e1aV19ed
    0x2e35S0x19ed: v2e35V19ed(0x1) = CONST 
    0x2e3aS0x19ed: v2e3aV19ed = MLOAD v2d02V19ed
    0x2e3cS0x19ed: v2e3cV19ed = LT v2e28_3V19ed, v2e3aV19ed
    0x2e3dS0x19ed: v2e3dV19ed(0x2e42) = CONST 
    0x2e40S0x19ed: JUMPI v2e3dV19ed(0x2e42), v2e3cV19ed

    Begin block 0x2e42B0x19ed
    prev=[0x2e28B0x19ed], succ=[0x2d2eB0x19ed]
    =================================
    0x2e42_0x0S0x19ed: v2e42_0V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2e42_0x3S0x19ed: v2e42_3V19ed = PHI v2d2cV19ed(0x0), v2e50V19ed
    0x2e43S0x19ed: v2e43V19ed(0x20) = CONST 
    0x2e47S0x19ed: v2e47V19ed = MUL v2e43V19ed(0x20), v2e42_0V19ed
    0x2e4bS0x19ed: v2e4bV19ed = ADD v2e47V19ed, v2d02V19ed
    0x2e4cS0x19ed: v2e4cV19ed = ADD v2e4bV19ed, v2e43V19ed(0x20)
    0x2e4dS0x19ed: MSTORE v2e4cV19ed, v2e35V19ed(0x1)
    0x2e4eS0x19ed: v2e4eV19ed(0x1) = CONST 
    0x2e50S0x19ed: v2e50V19ed = ADD v2e4eV19ed(0x1), v2e42_3V19ed
    0x2e51S0x19ed: v2e51V19ed(0x2d2e) = CONST 
    0x2e54S0x19ed: JUMP v2e51V19ed(0x2d2e)

    Begin block 0x2e41B0x19ed
    prev=[0x2e28B0x19ed], succ=[]
    =================================
    0x2e41S0x19ed: THROW 

    Begin block 0x2e27B0x19ed
    prev=[0x2d90B0x19ed], succ=[]
    =================================
    0x2e27S0x19ed: THROW 

    Begin block 0x2d8fB0x19ed
    prev=[0x2d38B0x19ed], succ=[]
    =================================
    0x2d8fS0x19ed: THROW 

    Begin block 0x2e55B0x19ed
    prev=[0x2d2eB0x19ed], succ=[0x2ec4B0x19ed]
    =================================
    0x2e58S0x19ed: v2e58V19ed(0x1) = CONST 
    0x2e5aS0x19ed: v2e5aV19ed(0x1) = CONST 
    0x2e5cS0x19ed: v2e5cV19ed(0xa0) = CONST 
    0x2e5eS0x19ed: v2e5eV19ed(0x10000000000000000000000000000000000000000) = SHL v2e5cV19ed(0xa0), v2e5aV19ed(0x1)
    0x2e5fS0x19ed: v2e5fV19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e5eV19ed(0x10000000000000000000000000000000000000000), v2e58V19ed(0x1)
    0x2e60S0x19ed: v2e60V19ed = AND v2e5fV19ed(0xffffffffffffffffffffffffffffffffffffffff), v870
    0x2e61S0x19ed: v2e61V19ed(0x0) = CONST 
    0x2e63S0x19ed: v2e63V19ed(0x1) = CONST 
    0x2e65S0x19ed: v2e65V19ed(0x1) = CONST 
    0x2e67S0x19ed: v2e67V19ed(0xa0) = CONST 
    0x2e69S0x19ed: v2e69V19ed(0x10000000000000000000000000000000000000000) = SHL v2e67V19ed(0xa0), v2e65V19ed(0x1)
    0x2e6aS0x19ed: v2e6aV19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e69V19ed(0x10000000000000000000000000000000000000000), v2e63V19ed(0x1)
    0x2e6bS0x19ed: v2e6bV19ed(0x0) = AND v2e6aV19ed(0xffffffffffffffffffffffffffffffffffffffff), v2e61V19ed(0x0)
    0x2e6cS0x19ed: v2e6cV19ed = CALLER 
    0x2e6dS0x19ed: v2e6dV19ed(0x1) = CONST 
    0x2e6fS0x19ed: v2e6fV19ed(0x1) = CONST 
    0x2e71S0x19ed: v2e71V19ed(0xa0) = CONST 
    0x2e73S0x19ed: v2e73V19ed(0x10000000000000000000000000000000000000000) = SHL v2e71V19ed(0xa0), v2e6fV19ed(0x1)
    0x2e74S0x19ed: v2e74V19ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e73V19ed(0x10000000000000000000000000000000000000000), v2e6dV19ed(0x1)
    0x2e75S0x19ed: v2e75V19ed = AND v2e74V19ed(0xffffffffffffffffffffffffffffffffffffffff), v2e6cV19ed
    0x2e76S0x19ed: v2e76V19ed(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x2e99S0x19ed: v2e99V19ed(0x40) = CONST 
    0x2e9bS0x19ed: v2e9bV19ed = MLOAD v2e99V19ed(0x40)
    0x2e9eS0x19ed: v2e9eV19ed(0x20) = CONST 
    0x2ea0S0x19ed: v2ea0V19ed = ADD v2e9eV19ed(0x20), v2e9bV19ed
    0x2ea2S0x19ed: v2ea2V19ed(0x20) = CONST 
    0x2ea4S0x19ed: v2ea4V19ed = ADD v2ea2V19ed(0x20), v2ea0V19ed
    0x2ea7S0x19ed: v2ea7V19ed(0x40) = SUB v2ea4V19ed, v2e9bV19ed
    0x2ea9S0x19ed: MSTORE v2e9bV19ed, v2ea7V19ed(0x40)
    0x2eadS0x19ed: v2eadV19ed = MLOAD v2cbcV19ed
    0x2eafS0x19ed: MSTORE v2ea4V19ed, v2eadV19ed
    0x2eb0S0x19ed: v2eb0V19ed(0x20) = CONST 
    0x2eb2S0x19ed: v2eb2V19ed = ADD v2eb0V19ed(0x20), v2ea4V19ed
    0x2eb6S0x19ed: v2eb6V19ed = MLOAD v2cbcV19ed
    0x2eb8S0x19ed: v2eb8V19ed(0x20) = CONST 
    0x2ebaS0x19ed: v2ebaV19ed = ADD v2eb8V19ed(0x20), v2cbcV19ed
    0x2ebcS0x19ed: v2ebcV19ed(0x20) = CONST 
    0x2ebeS0x19ed: v2ebeV19ed = MUL v2ebcV19ed(0x20), v2eb6V19ed
    0x2ec2S0x19ed: v2ec2V19ed(0x0) = CONST 

    Begin block 0x2ec4B0x19ed
    prev=[0x2e55B0x19ed, 0x2ecdB0x19ed], succ=[0x2edcB0x19ed, 0x2ecdB0x19ed]
    =================================
    0x2ec4_0x0S0x19ed: v2ec4_0V19ed = PHI v2ec2V19ed(0x0), v2ed7V19ed
    0x2ec7S0x19ed: v2ec7V19ed = LT v2ec4_0V19ed, v2ebeV19ed
    0x2ec8S0x19ed: v2ec8V19ed = ISZERO v2ec7V19ed
    0x2ec9S0x19ed: v2ec9V19ed(0x2edc) = CONST 
    0x2eccS0x19ed: JUMPI v2ec9V19ed(0x2edc), v2ec8V19ed

    Begin block 0x2edcB0x19ed
    prev=[0x2ec4B0x19ed], succ=[0x2f03B0x19ed]
    =================================
    0x2ee3S0x19ed: v2ee3V19ed = ADD v2ebeV19ed, v2eb2V19ed
    0x2ee6S0x19ed: v2ee6V19ed = SUB v2ee3V19ed, v2e9bV19ed
    0x2ee8S0x19ed: MSTORE v2ea0V19ed, v2ee6V19ed
    0x2eecS0x19ed: v2eecV19ed = MLOAD v2d02V19ed
    0x2eeeS0x19ed: MSTORE v2ee3V19ed, v2eecV19ed
    0x2eefS0x19ed: v2eefV19ed(0x20) = CONST 
    0x2ef1S0x19ed: v2ef1V19ed = ADD v2eefV19ed(0x20), v2ee3V19ed
    0x2ef5S0x19ed: v2ef5V19ed = MLOAD v2d02V19ed
    0x2ef7S0x19ed: v2ef7V19ed(0x20) = CONST 
    0x2ef9S0x19ed: v2ef9V19ed = ADD v2ef7V19ed(0x20), v2d02V19ed
    0x2efbS0x19ed: v2efbV19ed(0x20) = CONST 
    0x2efdS0x19ed: v2efdV19ed = MUL v2efbV19ed(0x20), v2ef5V19ed
    0x2f01S0x19ed: v2f01V19ed(0x0) = CONST 

    Begin block 0x2f03B0x19ed
    prev=[0x2edcB0x19ed, 0x2f0cB0x19ed], succ=[0x2f1bB0x19ed, 0x2f0cB0x19ed]
    =================================
    0x2f03_0x0S0x19ed: v2f03_0V19ed = PHI v2f01V19ed(0x0), v2f16V19ed
    0x2f06S0x19ed: v2f06V19ed = LT v2f03_0V19ed, v2efdV19ed
    0x2f07S0x19ed: v2f07V19ed = ISZERO v2f06V19ed
    0x2f08S0x19ed: v2f08V19ed(0x2f1b) = CONST 
    0x2f0bS0x19ed: JUMPI v2f08V19ed(0x2f1b), v2f07V19ed

    Begin block 0x2f1bB0x19ed
    prev=[0x2f03B0x19ed], succ=[0x2f4eB0x19ed]
    =================================
    0x2f22S0x19ed: v2f22V19ed = ADD v2efdV19ed, v2ef1V19ed
    0x2f29S0x19ed: v2f29V19ed(0x40) = CONST 
    0x2f2bS0x19ed: v2f2bV19ed = MLOAD v2f29V19ed(0x40)
    0x2f2eS0x19ed: v2f2eV19ed = SUB v2f22V19ed, v2f2bV19ed
    0x2f30S0x19ed: LOG4 v2f2bV19ed, v2f2eV19ed, v2e76V19ed(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v2e75V19ed, v2e6bV19ed(0x0), v2e60V19ed
    0x2f31S0x19ed: v2f31V19ed(0x2f4e) = CONST 
    0x2f34S0x19ed: v2f34V19ed = CALLER 
    0x2f35S0x19ed: v2f35V19ed(0x0) = CONST 
    0x2f3aS0x19ed: v2f3aV19ed(0x40) = CONST 
    0x2f3cS0x19ed: v2f3cV19ed = MLOAD v2f3aV19ed(0x40)
    0x2f3eS0x19ed: v2f3eV19ed(0x20) = CONST 
    0x2f40S0x19ed: v2f40V19ed = ADD v2f3eV19ed(0x20), v2f3cV19ed
    0x2f41S0x19ed: v2f41V19ed(0x40) = CONST 
    0x2f43S0x19ed: MSTORE v2f41V19ed(0x40), v2f40V19ed
    0x2f45S0x19ed: v2f45V19ed(0x0) = CONST 
    0x2f48S0x19ed: MSTORE v2f3cV19ed, v2f45V19ed(0x0)
    0x2f4aS0x19ed: v2f4aV19ed(0x281f) = CONST 
    0x2f4dS0x19ed: CALLPRIVATE v2f4aV19ed(0x281f), v2f3cV19ed, v2d02V19ed, v2cbcV19ed, v870, v2f35V19ed(0x0), v2f34V19ed, v2f31V19ed(0x2f4e)

    Begin block 0x2f4eB0x19ed
    prev=[0x2f1bB0x19ed], succ=[0x439f]
    =================================
    0x2f57S0x19ed: JUMP v19ee(0x439f)

    Begin block 0x439f
    prev=[0x2f4eB0x19ed], succ=[0x77f0x84f]
    =================================
    0x43a7: JUMP v850(0x77f)

    Begin block 0x77f0x84f
    prev=[0x439f], succ=[0x7a30x84f]
    =================================
    0x7800x84f: v84f780(0x40) = CONST 
    0x7830x84f: v84f783 = MLOAD v84f780(0x40)
    0x7840x84f: v84f784(0x20) = CONST 
    0x7880x84f: MSTORE v84f783, v84f784(0x20)
    0x78a0x84f: v84f78a = MLOAD v2cbcV19ed
    0x78d0x84f: v84f78d = ADD v84f783, v84f784(0x20)
    0x78e0x84f: MSTORE v84f78d, v84f78a
    0x7900x84f: v84f790 = MLOAD v2cbcV19ed
    0x7970x84f: v84f797 = ADD v84f783, v84f780(0x40)
    0x79b0x84f: v84f79b = ADD v84f784(0x20), v2cbcV19ed
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

    Begin block 0x2f0cB0x19ed
    prev=[0x2f03B0x19ed], succ=[0x2f03B0x19ed]
    =================================
    0x2f0c_0x0S0x19ed: v2f0c_0V19ed = PHI v2f01V19ed(0x0), v2f16V19ed
    0x2f0eS0x19ed: v2f0eV19ed = ADD v2f0c_0V19ed, v2ef9V19ed
    0x2f0fS0x19ed: v2f0fV19ed = MLOAD v2f0eV19ed
    0x2f12S0x19ed: v2f12V19ed = ADD v2f0c_0V19ed, v2ef1V19ed
    0x2f13S0x19ed: MSTORE v2f12V19ed, v2f0fV19ed
    0x2f14S0x19ed: v2f14V19ed(0x20) = CONST 
    0x2f16S0x19ed: v2f16V19ed = ADD v2f14V19ed(0x20), v2f0c_0V19ed
    0x2f17S0x19ed: v2f17V19ed(0x2f03) = CONST 
    0x2f1aS0x19ed: JUMP v2f17V19ed(0x2f03)

    Begin block 0x2ecdB0x19ed
    prev=[0x2ec4B0x19ed], succ=[0x2ec4B0x19ed]
    =================================
    0x2ecd_0x0S0x19ed: v2ecd_0V19ed = PHI v2ec2V19ed(0x0), v2ed7V19ed
    0x2ecfS0x19ed: v2ecfV19ed = ADD v2ecd_0V19ed, v2ebaV19ed
    0x2ed0S0x19ed: v2ed0V19ed = MLOAD v2ecfV19ed
    0x2ed3S0x19ed: v2ed3V19ed = ADD v2ecd_0V19ed, v2eb2V19ed
    0x2ed4S0x19ed: MSTORE v2ed3V19ed, v2ed0V19ed
    0x2ed5S0x19ed: v2ed5V19ed(0x20) = CONST 
    0x2ed7S0x19ed: v2ed7V19ed = ADD v2ed5V19ed(0x20), v2ecd_0V19ed
    0x2ed8S0x19ed: v2ed8V19ed(0x2ec4) = CONST 
    0x2edbS0x19ed: JUMP v2ed8V19ed(0x2ec4)

    Begin block 0x2d19B0x19ed
    prev=[0x2cfeB0x19ed], succ=[0x2d28B0x19ed]
    =================================
    0x2d1aS0x19ed: v2d1aV19ed(0x20) = CONST 
    0x2d1cS0x19ed: v2d1cV19ed = ADD v2d1aV19ed(0x20), v2d02V19ed
    0x2d1dS0x19ed: v2d1dV19ed(0x20) = CONST 
    0x2d20S0x19ed: v2d20V19ed = MUL v876, v2d1dV19ed(0x20)
    0x2d22S0x19ed: v2d22V19ed = CALLDATASIZE 
    0x2d24S0x19ed: CALLDATACOPY v2d1cV19ed, v2d22V19ed, v2d20V19ed
    0x2d25S0x19ed: v2d25V19ed = ADD v2d20V19ed, v2d1cV19ed

    Begin block 0x2cd3B0x19ed
    prev=[0x2cb8B0x19ed], succ=[0x2ce2B0x19ed]
    =================================
    0x2cd4S0x19ed: v2cd4V19ed(0x20) = CONST 
    0x2cd6S0x19ed: v2cd6V19ed = ADD v2cd4V19ed(0x20), v2cbcV19ed
    0x2cd7S0x19ed: v2cd7V19ed(0x20) = CONST 
    0x2cdaS0x19ed: v2cdaV19ed = MUL v876, v2cd7V19ed(0x20)
    0x2cdcS0x19ed: v2cdcV19ed = CALLDATASIZE 
    0x2cdeS0x19ed: CALLDATACOPY v2cd6V19ed, v2cdcV19ed, v2cdaV19ed
    0x2cdfS0x19ed: v2cdfV19ed = ADD v2cdaV19ed, v2cd6V19ed

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
    prev=[0x8d2], succ=[0x1a02]
    =================================
    0x8ea: v8ea = CALLDATALOAD v8d6(0x4)
    0x8eb: v8eb(0x1a02) = CONST 
    0x8ee: JUMP v8eb(0x1a02)

    Begin block 0x1a02
    prev=[0x8e8], succ=[0x1a52, 0x1a80]
    =================================
    0x1a03: v1a03(0x0) = CONST 
    0x1a07: MSTORE v1a03(0x0), v8ea
    0x1a08: v1a08(0xa) = CONST 
    0x1a0a: v1a0a(0x20) = CONST 
    0x1a0e: MSTORE v1a0a(0x20), v1a08(0xa)
    0x1a0f: v1a0f(0x40) = CONST 
    0x1a13: v1a13 = SHA3 v1a03(0x0), v1a0f(0x40)
    0x1a14: v1a14 = SLOAD v1a13
    0x1a15: v1a15(0xc) = CONST 
    0x1a18: MSTORE v1a0a(0x20), v1a15(0xc)
    0x1a1c: v1a1c = SHA3 v1a03(0x0), v1a0f(0x40)
    0x1a1d: v1a1d(0x2) = CONST 
    0x1a20: v1a20 = ADD v1a1c, v1a1d(0x2)
    0x1a21: v1a21 = SLOAD v1a20
    0x1a23: v1a23 = SLOAD v1a1c
    0x1a25: v1a25 = MLOAD v1a0f(0x40)
    0x1a28: v1a28 = MUL v1a0a(0x20), v1a23
    0x1a2a: v1a2a = ADD v1a25, v1a28
    0x1a2c: v1a2c = ADD v1a0a(0x20), v1a2a
    0x1a2f: MSTORE v1a0f(0x40), v1a2c
    0x1a32: MSTORE v1a25, v1a23
    0x1a33: v1a33(0x1) = CONST 
    0x1a35: v1a35(0x1) = CONST 
    0x1a37: v1a37(0x80) = CONST 
    0x1a39: v1a39(0x100000000000000000000000000000000) = SHL v1a37(0x80), v1a35(0x1)
    0x1a3a: v1a3a(0xffffffffffffffffffffffffffffffff) = SUB v1a39(0x100000000000000000000000000000000), v1a33(0x1)
    0x1a3d: v1a3d = AND v1a14, v1a3a(0xffffffffffffffffffffffffffffffff)
    0x1a3f: v1a3f(0x60) = CONST 
    0x1a49: v1a49 = ADD v1a25, v1a0a(0x20)
    0x1a4d: v1a4d = ISZERO v1a23
    0x1a4e: v1a4e(0x1a80) = CONST 
    0x1a51: JUMPI v1a4e(0x1a80), v1a4d

    Begin block 0x1a52
    prev=[0x1a02], succ=[0x1a62]
    =================================
    0x1a52: v1a52(0x20) = CONST 
    0x1a54: v1a54 = MUL v1a52(0x20), v1a23
    0x1a56: v1a56 = ADD v1a49, v1a54
    0x1a59: v1a59(0x0) = CONST 
    0x1a5b: MSTORE v1a59(0x0), v1a1c
    0x1a5c: v1a5c(0x20) = CONST 
    0x1a5e: v1a5e(0x0) = CONST 
    0x1a60: v1a60 = SHA3 v1a5e(0x0), v1a5c(0x20)

    Begin block 0x1a62
    prev=[0x1a52, 0x1a62], succ=[0x1a80, 0x1a62]
    =================================
    0x1a62_0x0: v1a62_0 = PHI v1a49, v1a78
    0x1a62_0x1: v1a62_1 = PHI v1a60, v1a74
    0x1a64: v1a64 = SLOAD v1a62_1
    0x1a65: v1a65(0x1) = CONST 
    0x1a67: v1a67(0x1) = CONST 
    0x1a69: v1a69(0xa0) = CONST 
    0x1a6b: v1a6b(0x10000000000000000000000000000000000000000) = SHL v1a69(0xa0), v1a67(0x1)
    0x1a6c: v1a6c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a6b(0x10000000000000000000000000000000000000000), v1a65(0x1)
    0x1a6d: v1a6d = AND v1a6c(0xffffffffffffffffffffffffffffffffffffffff), v1a64
    0x1a6f: MSTORE v1a62_0, v1a6d
    0x1a70: v1a70(0x1) = CONST 
    0x1a74: v1a74 = ADD v1a62_1, v1a70(0x1)
    0x1a76: v1a76(0x20) = CONST 
    0x1a78: v1a78 = ADD v1a76(0x20), v1a62_0
    0x1a7b: v1a7b = GT v1a56, v1a78
    0x1a7c: v1a7c(0x1a62) = CONST 
    0x1a7f: JUMPI v1a7c(0x1a62), v1a7b

    Begin block 0x1a80
    prev=[0x1a02, 0x1a62], succ=[0x1ac3, 0x1ae7]
    =================================
    0x1a88: v1a88(0xc) = CONST 
    0x1a8a: v1a8a(0x0) = CONST 
    0x1a8e: MSTORE v1a8a(0x0), v8ea
    0x1a8f: v1a8f(0x20) = CONST 
    0x1a91: v1a91(0x20) = ADD v1a8f(0x20), v1a8a(0x0)
    0x1a94: MSTORE v1a91(0x20), v1a88(0xc)
    0x1a95: v1a95(0x20) = CONST 
    0x1a97: v1a97(0x40) = ADD v1a95(0x20), v1a91(0x20)
    0x1a98: v1a98(0x0) = CONST 
    0x1a9a: v1a9a = SHA3 v1a98(0x0), v1a97(0x40)
    0x1a9b: v1a9b(0x1) = CONST 
    0x1a9d: v1a9d = ADD v1a9b(0x1), v1a9a
    0x1a9f: v1a9f = SLOAD v1a9d
    0x1aa1: v1aa1(0x20) = CONST 
    0x1aa3: v1aa3 = MUL v1aa1(0x20), v1a9f
    0x1aa4: v1aa4(0x20) = CONST 
    0x1aa6: v1aa6 = ADD v1aa4(0x20), v1aa3
    0x1aa7: v1aa7(0x40) = CONST 
    0x1aa9: v1aa9 = MLOAD v1aa7(0x40)
    0x1aac: v1aac = ADD v1aa9, v1aa6
    0x1aad: v1aad(0x40) = CONST 
    0x1aaf: MSTORE v1aad(0x40), v1aac
    0x1ab6: MSTORE v1aa9, v1a9f
    0x1ab7: v1ab7(0x20) = CONST 
    0x1ab9: v1ab9 = ADD v1ab7(0x20), v1aa9
    0x1abc: v1abc = SLOAD v1a9d
    0x1abe: v1abe = ISZERO v1abc
    0x1abf: v1abf(0x1ae7) = CONST 
    0x1ac2: JUMPI v1abf(0x1ae7), v1abe

    Begin block 0x1ac3
    prev=[0x1a80], succ=[0x1ad3]
    =================================
    0x1ac3: v1ac3(0x20) = CONST 
    0x1ac5: v1ac5 = MUL v1ac3(0x20), v1abc
    0x1ac7: v1ac7 = ADD v1ab9, v1ac5
    0x1aca: v1aca(0x0) = CONST 
    0x1acc: MSTORE v1aca(0x0), v1a9d
    0x1acd: v1acd(0x20) = CONST 
    0x1acf: v1acf(0x0) = CONST 
    0x1ad1: v1ad1 = SHA3 v1acf(0x0), v1acd(0x20)

    Begin block 0x1ad3
    prev=[0x1ac3, 0x1ad3], succ=[0x1ae7, 0x1ad3]
    =================================
    0x1ad3_0x0: v1ad3_0 = PHI v1ab9, v1ada
    0x1ad3_0x1: v1ad3_1 = PHI v1ad1, v1ade
    0x1ad5: v1ad5 = SLOAD v1ad3_1
    0x1ad7: MSTORE v1ad3_0, v1ad5
    0x1ad8: v1ad8(0x20) = CONST 
    0x1ada: v1ada = ADD v1ad8(0x20), v1ad3_0
    0x1adc: v1adc(0x1) = CONST 
    0x1ade: v1ade = ADD v1adc(0x1), v1ad3_1
    0x1ae2: v1ae2 = GT v1ac7, v1ada
    0x1ae3: v1ae3(0x1ad3) = CONST 
    0x1ae6: JUMPI v1ae3(0x1ad3), v1ae2

    Begin block 0x1ae7
    prev=[0x1a80, 0x1ad3], succ=[0x8ef]
    =================================
    0x1af4: JUMP v8d3(0x8ef)

    Begin block 0x8ef
    prev=[0x1ae7], succ=[0x930]
    =================================
    0x8f0: v8f0(0x40) = CONST 
    0x8f2: v8f2 = MLOAD v8f0(0x40)
    0x8f5: v8f5(0x1) = CONST 
    0x8f7: v8f7(0x1) = CONST 
    0x8f9: v8f9(0x80) = CONST 
    0x8fb: v8fb(0x100000000000000000000000000000000) = SHL v8f9(0x80), v8f7(0x1)
    0x8fc: v8fc(0xffffffffffffffffffffffffffffffff) = SUB v8fb(0x100000000000000000000000000000000), v8f5(0x1)
    0x8fd: v8fd = AND v8fc(0xffffffffffffffffffffffffffffffff), v1a3d
    0x8ff: MSTORE v8f2, v8fd
    0x900: v900(0x20) = CONST 
    0x902: v902 = ADD v900(0x20), v8f2
    0x904: v904(0x20) = CONST 
    0x906: v906 = ADD v904(0x20), v902
    0x908: v908(0x20) = CONST 
    0x90a: v90a = ADD v908(0x20), v906
    0x90d: MSTORE v90a, v1a21
    0x90e: v90e(0x20) = CONST 
    0x910: v910 = ADD v90e(0x20), v90a
    0x913: v913(0x80) = SUB v910, v8f2
    0x915: MSTORE v902, v913(0x80)
    0x919: v919 = MLOAD v1a25
    0x91b: MSTORE v910, v919
    0x91c: v91c(0x20) = CONST 
    0x91e: v91e = ADD v91c(0x20), v910
    0x922: v922 = MLOAD v1a25
    0x924: v924(0x20) = CONST 
    0x926: v926 = ADD v924(0x20), v1a25
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
    0x958: v958 = MLOAD v1aa9
    0x95a: MSTORE v94f, v958
    0x95b: v95b(0x20) = CONST 
    0x95d: v95d = ADD v95b(0x20), v94f
    0x961: v961 = MLOAD v1aa9
    0x963: v963(0x20) = CONST 
    0x965: v965 = ADD v963(0x20), v1aa9
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
    0x9a0: v9a0(0x3f93) = CONST 
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
    prev=[0x99f], succ=[0x1af5]
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
    0x9cd: v9cd(0x1af5) = CONST 
    0x9d0: JUMP v9cd(0x1af5)

    Begin block 0x1af5
    prev=[0x9b5], succ=[0x1b0d, 0x1b4c]
    =================================
    0x1af6: v1af6 = CALLER 
    0x1af7: v1af7(0x0) = CONST 
    0x1afb: MSTORE v1af7(0x0), v1af6
    0x1afc: v1afc(0x6) = CONST 
    0x1afe: v1afe(0x20) = CONST 
    0x1b00: MSTORE v1afe(0x20), v1afc(0x6)
    0x1b01: v1b01(0x40) = CONST 
    0x1b04: v1b04 = SHA3 v1af7(0x0), v1b01(0x40)
    0x1b05: v1b05 = SLOAD v1b04
    0x1b06: v1b06(0xff) = CONST 
    0x1b08: v1b08 = AND v1b06(0xff), v1b05
    0x1b09: v1b09(0x1b4c) = CONST 
    0x1b0c: JUMPI v1b09(0x1b4c), v1b08

    Begin block 0x1b0d
    prev=[0x1af5], succ=[]
    =================================
    0x1b0d: v1b0d(0x40) = CONST 
    0x1b10: v1b10 = MLOAD v1b0d(0x40)
    0x1b11: v1b11(0x461bcd) = CONST 
    0x1b15: v1b15(0xe5) = CONST 
    0x1b17: v1b17(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b15(0xe5), v1b11(0x461bcd)
    0x1b19: MSTORE v1b10, v1b17(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b1a: v1b1a(0x20) = CONST 
    0x1b1c: v1b1c(0x4) = CONST 
    0x1b1f: v1b1f = ADD v1b10, v1b1c(0x4)
    0x1b20: MSTORE v1b1f, v1b1a(0x20)
    0x1b21: v1b21(0x10) = CONST 
    0x1b23: v1b23(0x24) = CONST 
    0x1b26: v1b26 = ADD v1b10, v1b23(0x24)
    0x1b27: MSTORE v1b26, v1b21(0x10)
    0x1b28: v1b28(0x36bab9ba1031329037b832b930ba37b9) = CONST 
    0x1b39: v1b39(0x81) = CONST 
    0x1b3b: v1b3b(0x6d757374206265206f70657261746f7200000000000000000000000000000000) = SHL v1b39(0x81), v1b28(0x36bab9ba1031329037b832b930ba37b9)
    0x1b3c: v1b3c(0x44) = CONST 
    0x1b3f: v1b3f = ADD v1b10, v1b3c(0x44)
    0x1b40: MSTORE v1b3f, v1b3b(0x6d757374206265206f70657261746f7200000000000000000000000000000000)
    0x1b42: v1b42 = MLOAD v1b0d(0x40)
    0x1b46: v1b46(0x0) = SUB v1b10, v1b42
    0x1b47: v1b47(0x64) = CONST 
    0x1b49: v1b49(0x64) = ADD v1b47(0x64), v1b46(0x0)
    0x1b4b: REVERT v1b42, v1b49(0x64)

    Begin block 0x1b4c
    prev=[0x1af5], succ=[0x1b56]
    =================================
    0x1b4d: v1b4d(0x1b56) = CONST 
    0x1b52: v1b52(0x24b9) = CONST 
    0x1b55: v1b55_0 = CALLPRIVATE v1b52(0x24b9), v9c7, v9c1, v1b4d(0x1b56)

    Begin block 0x1b56
    prev=[0x1b4c], succ=[0x1b5b, 0x1b97]
    =================================
    0x1b57: v1b57(0x1b97) = CONST 
    0x1b5a: JUMPI v1b57(0x1b97), v1b55_0

    Begin block 0x1b5b
    prev=[0x1b56], succ=[]
    =================================
    0x1b5b: v1b5b(0x40) = CONST 
    0x1b5e: v1b5e = MLOAD v1b5b(0x40)
    0x1b5f: v1b5f(0x461bcd) = CONST 
    0x1b63: v1b63(0xe5) = CONST 
    0x1b65: v1b65(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b63(0xe5), v1b5f(0x461bcd)
    0x1b67: MSTORE v1b5e, v1b65(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b68: v1b68(0x20) = CONST 
    0x1b6a: v1b6a(0x4) = CONST 
    0x1b6d: v1b6d = ADD v1b5e, v1b6a(0x4)
    0x1b6e: MSTORE v1b6d, v1b68(0x20)
    0x1b6f: v1b6f(0xd) = CONST 
    0x1b71: v1b71(0x24) = CONST 
    0x1b74: v1b74 = ADD v1b5e, v1b71(0x24)
    0x1b75: MSTORE v1b74, v1b6f(0xd)
    0x1b76: v1b76(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1b84: v1b84(0x99) = CONST 
    0x1b86: v1b86(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1b84(0x99), v1b76(0x26bab9ba1031329037bbb732b9)
    0x1b87: v1b87(0x44) = CONST 
    0x1b8a: v1b8a = ADD v1b5e, v1b87(0x44)
    0x1b8b: MSTORE v1b8a, v1b86(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1b8d: v1b8d = MLOAD v1b5b(0x40)
    0x1b91: v1b91(0x0) = SUB v1b5e, v1b8d
    0x1b92: v1b92(0x64) = CONST 
    0x1b94: v1b94(0x64) = ADD v1b92(0x64), v1b91(0x0)
    0x1b96: REVERT v1b8d, v1b94(0x64)

    Begin block 0x1b97
    prev=[0x1b56], succ=[0x2f58B0x1b97]
    =================================
    0x1b98: v1b98(0x0) = CONST 
    0x1b9c: MSTORE v1b98(0x0), v9c7
    0x1b9d: v1b9d(0xa) = CONST 
    0x1b9f: v1b9f(0x20) = CONST 
    0x1ba1: MSTORE v1b9f(0x20), v1b9d(0xa)
    0x1ba2: v1ba2(0x40) = CONST 
    0x1ba6: v1ba6 = SHA3 v1b98(0x0), v1ba2(0x40)
    0x1ba7: v1ba7 = SLOAD v1ba6
    0x1ba9: v1ba9 = MLOAD v1ba2(0x40)
    0x1bac: v1bac(0x1) = CONST 
    0x1bae: v1bae(0x80) = CONST 
    0x1bb0: v1bb0(0x100000000000000000000000000000000) = SHL v1bae(0x80), v1bac(0x1)
    0x1bb3: v1bb3 = DIV v1ba7, v1bb0(0x100000000000000000000000000000000)
    0x1bb4: v1bb4(0x1) = CONST 
    0x1bb6: v1bb6(0x1) = CONST 
    0x1bb8: v1bb8(0x80) = CONST 
    0x1bba: v1bba(0x100000000000000000000000000000000) = SHL v1bb8(0x80), v1bb6(0x1)
    0x1bbb: v1bbb(0xffffffffffffffffffffffffffffffff) = SUB v1bba(0x100000000000000000000000000000000), v1bb4(0x1)
    0x1bbc: v1bbc = AND v1bbb(0xffffffffffffffffffffffffffffffff), v1bb3
    0x1bc0: v1bc0(0xcfd7d36b449fead22a7599b08c1ce0ae53d225deb29efd38f057f6891485a858) = CONST 
    0x1be3: LOG4 v1ba9, v1b98(0x0), v1bc0(0xcfd7d36b449fead22a7599b08c1ce0ae53d225deb29efd38f057f6891485a858), v9c7, v1bbc, v9cc
    0x1be4: v1be4(0x0) = CONST 
    0x1be8: MSTORE v1be4(0x0), v9c7
    0x1be9: v1be9(0xa) = CONST 
    0x1beb: v1beb(0x20) = CONST 
    0x1bed: MSTORE v1beb(0x20), v1be9(0xa)
    0x1bee: v1bee(0x40) = CONST 
    0x1bf1: v1bf1 = SHA3 v1be4(0x0), v1bee(0x40)
    0x1bf2: v1bf2 = SLOAD v1bf1
    0x1bf3: v1bf3(0x1c10) = CONST 
    0x1bfb: v1bfb(0x1) = CONST 
    0x1bfd: v1bfd(0x80) = CONST 
    0x1bff: v1bff(0x100000000000000000000000000000000) = SHL v1bfd(0x80), v1bfb(0x1)
    0x1c01: v1c01 = DIV v1bf2, v1bff(0x100000000000000000000000000000000)
    0x1c02: v1c02(0x1) = CONST 
    0x1c04: v1c04(0x1) = CONST 
    0x1c06: v1c06(0x80) = CONST 
    0x1c08: v1c08(0x100000000000000000000000000000000) = SHL v1c06(0x80), v1c04(0x1)
    0x1c09: v1c09(0xffffffffffffffffffffffffffffffff) = SUB v1c08(0x100000000000000000000000000000000), v1c02(0x1)
    0x1c0a: v1c0a = AND v1c09(0xffffffffffffffffffffffffffffffff), v1c01
    0x1c0c: v1c0c(0x2f58) = CONST 
    0x1c0f: JUMP v1c0c(0x2f58), v9cc, v1c0a, v9c7, v9c1, v1bf3(0x1c10)

    Begin block 0x2f58B0x1b97
    prev=[0x1b97], succ=[0x36a6B0x2f58B0x1b97]
    =================================
    0x2f59S0x1b97: v2f59V1b97(0x2f6a) = CONST 
    0x2f5dS0x1b97: v2f5dV1b97(0x1) = CONST 
    0x2f5fS0x1b97: v2f5fV1b97(0x1) = CONST 
    0x2f61S0x1b97: v2f61V1b97(0xa0) = CONST 
    0x2f63S0x1b97: v2f63V1b97(0x10000000000000000000000000000000000000000) = SHL v2f61V1b97(0xa0), v2f5fV1b97(0x1)
    0x2f64S0x1b97: v2f64V1b97(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f63V1b97(0x10000000000000000000000000000000000000000), v2f5dV1b97(0x1)
    0x2f65S0x1b97: v2f65V1b97 = AND v2f64V1b97(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x2f66S0x1b97: v2f66V1b97(0x36a6) = CONST 
    0x2f69S0x1b97: JUMP v2f66V1b97(0x36a6)

    Begin block 0x36a6B0x2f58B0x1b97
    prev=[0x2f58B0x1b97], succ=[0x2f6aB0x1b97]
    =================================
    0x36a7S0x2f58S0x1b97: v36a7V2f58V1b97 = EXTCODESIZE v2f65V1b97
    0x36a8S0x2f58S0x1b97: v36a8V2f58V1b97 = ISZERO v36a7V2f58V1b97
    0x36a9S0x2f58S0x1b97: v36a9V2f58V1b97 = ISZERO v36a8V2f58V1b97
    0x36abS0x2f58S0x1b97: JUMP v2f59V1b97(0x2f6a)

    Begin block 0x2f6aB0x1b97
    prev=[0x36a6B0x2f58B0x1b97], succ=[0x2f83B0x1b97, 0x2f71B0x1b97]
    =================================
    0x2f6cS0x1b97: v2f6cV1b97 = ISZERO v36a9V2f58V1b97
    0x2f6dS0x1b97: v2f6dV1b97(0x2f83) = CONST 
    0x2f70S0x1b97: JUMPI v2f6dV1b97(0x2f83), v2f6cV1b97

    Begin block 0x2f83B0x1b97
    prev=[0x2f6aB0x1b97, 0x2f71B0x1b97], succ=[0x2f89B0x1b97, 0x44eeB0x1b97]
    =================================
    0x2f83_0x0S0x1b97: v2f83_0V1b97 = PHI v2f82_0V1b97, v36a9V2f58V1b97
    0x2f84S0x1b97: v2f84V1b97 = ISZERO v2f83_0V1b97
    0x2f85S0x1b97: v2f85V1b97(0x44ee) = CONST 
    0x2f88S0x1b97: JUMPI v2f85V1b97(0x44ee), v2f84V1b97

    Begin block 0x2f89B0x1b97
    prev=[0x2f83B0x1b97], succ=[0x2fd1B0x1b97, 0x2fd5B0x1b97]
    =================================
    0x2f89S0x1b97: v2f89V1b97(0x40) = CONST 
    0x2f8cS0x1b97: v2f8cV1b97 = MLOAD v2f89V1b97(0x40)
    0x2f8dS0x1b97: v2f8dV1b97(0x1ffc9a7) = CONST 
    0x2f92S0x1b97: v2f92V1b97(0xe0) = CONST 
    0x2f94S0x1b97: v2f94V1b97(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v2f92V1b97(0xe0), v2f8dV1b97(0x1ffc9a7)
    0x2f96S0x1b97: MSTORE v2f8cV1b97, v2f94V1b97(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x2f97S0x1b97: v2f97V1b97(0x50e84861) = CONST 
    0x2f9cS0x1b97: v2f9cV1b97(0xe0) = CONST 
    0x2f9eS0x1b97: v2f9eV1b97(0x50e8486100000000000000000000000000000000000000000000000000000000) = SHL v2f9cV1b97(0xe0), v2f97V1b97(0x50e84861)
    0x2f9fS0x1b97: v2f9fV1b97(0x4) = CONST 
    0x2fa2S0x1b97: v2fa2V1b97 = ADD v2f8cV1b97, v2f9fV1b97(0x4)
    0x2fa3S0x1b97: MSTORE v2fa2V1b97, v2f9eV1b97(0x50e8486100000000000000000000000000000000000000000000000000000000)
    0x2fa5S0x1b97: v2fa5V1b97 = MLOAD v2f89V1b97(0x40)
    0x2fa6S0x1b97: v2fa6V1b97(0x1) = CONST 
    0x2fa8S0x1b97: v2fa8V1b97(0x1) = CONST 
    0x2faaS0x1b97: v2faaV1b97(0xa0) = CONST 
    0x2facS0x1b97: v2facV1b97(0x10000000000000000000000000000000000000000) = SHL v2faaV1b97(0xa0), v2fa8V1b97(0x1)
    0x2fadS0x1b97: v2fadV1b97(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2facV1b97(0x10000000000000000000000000000000000000000), v2fa6V1b97(0x1)
    0x2fafS0x1b97: v2fafV1b97 = AND v9c1, v2fadV1b97(0xffffffffffffffffffffffffffffffffffffffff)
    0x2fb1S0x1b97: v2fb1V1b97(0x1ffc9a7) = CONST 
    0x2fb7S0x1b97: v2fb7V1b97(0x24) = CONST 
    0x2fbbS0x1b97: v2fbbV1b97 = ADD v2f8cV1b97, v2fb7V1b97(0x24)
    0x2fbdS0x1b97: v2fbdV1b97(0x20) = CONST 
    0x2fc4S0x1b97: v2fc4V1b97(0x0) = SUB v2f8cV1b97, v2fa5V1b97
    0x2fc5S0x1b97: v2fc5V1b97(0x24) = ADD v2fc4V1b97(0x0), v2fb7V1b97(0x24)
    0x2fc9S0x1b97: v2fc9V1b97 = EXTCODESIZE v2fafV1b97
    0x2fcaS0x1b97: v2fcaV1b97 = ISZERO v2fc9V1b97
    0x2fccS0x1b97: v2fccV1b97 = ISZERO v2fcaV1b97
    0x2fcdS0x1b97: v2fcdV1b97(0x2fd5) = CONST 
    0x2fd0S0x1b97: JUMPI v2fcdV1b97(0x2fd5), v2fccV1b97

    Begin block 0x2fd1B0x1b97
    prev=[0x2f89B0x1b97], succ=[]
    =================================
    0x2fd1S0x1b97: v2fd1V1b97(0x0) = CONST 
    0x2fd4S0x1b97: REVERT v2fd1V1b97(0x0), v2fd1V1b97(0x0)

    Begin block 0x2fd5B0x1b97
    prev=[0x2f89B0x1b97], succ=[0x2fe0B0x1b97, 0x2fe9B0x1b97]
    =================================
    0x2fd7S0x1b97: v2fd7V1b97 = GAS 
    0x2fd8S0x1b97: v2fd8V1b97 = STATICCALL v2fd7V1b97, v2fafV1b97, v2fa5V1b97, v2fc5V1b97(0x24), v2fa5V1b97, v2fbdV1b97(0x20)
    0x2fd9S0x1b97: v2fd9V1b97 = ISZERO v2fd8V1b97
    0x2fdbS0x1b97: v2fdbV1b97 = ISZERO v2fd9V1b97
    0x2fdcS0x1b97: v2fdcV1b97(0x2fe9) = CONST 
    0x2fdfS0x1b97: JUMPI v2fdcV1b97(0x2fe9), v2fdbV1b97

    Begin block 0x2fe0B0x1b97
    prev=[0x2fd5B0x1b97], succ=[]
    =================================
    0x2fe0S0x1b97: v2fe0V1b97 = RETURNDATASIZE 
    0x2fe1S0x1b97: v2fe1V1b97(0x0) = CONST 
    0x2fe4S0x1b97: RETURNDATACOPY v2fe1V1b97(0x0), v2fe1V1b97(0x0), v2fe0V1b97
    0x2fe5S0x1b97: v2fe5V1b97 = RETURNDATASIZE 
    0x2fe6S0x1b97: v2fe6V1b97(0x0) = CONST 
    0x2fe8S0x1b97: REVERT v2fe6V1b97(0x0), v2fe5V1b97

    Begin block 0x2fe9B0x1b97
    prev=[0x2fd5B0x1b97], succ=[0x2ffbB0x1b97, 0x2fffB0x1b97]
    =================================
    0x2feeS0x1b97: v2feeV1b97(0x40) = CONST 
    0x2ff0S0x1b97: v2ff0V1b97 = MLOAD v2feeV1b97(0x40)
    0x2ff1S0x1b97: v2ff1V1b97 = RETURNDATASIZE 
    0x2ff2S0x1b97: v2ff2V1b97(0x20) = CONST 
    0x2ff5S0x1b97: v2ff5V1b97 = LT v2ff1V1b97, v2ff2V1b97(0x20)
    0x2ff6S0x1b97: v2ff6V1b97 = ISZERO v2ff5V1b97
    0x2ff7S0x1b97: v2ff7V1b97(0x2fff) = CONST 
    0x2ffaS0x1b97: JUMPI v2ff7V1b97(0x2fff), v2ff6V1b97

    Begin block 0x2ffbB0x1b97
    prev=[0x2fe9B0x1b97], succ=[]
    =================================
    0x2ffbS0x1b97: v2ffbV1b97(0x0) = CONST 
    0x2ffeS0x1b97: REVERT v2ffbV1b97(0x0), v2ffbV1b97(0x0)

    Begin block 0x2fffB0x1b97
    prev=[0x2fe9B0x1b97], succ=[0x3007B0x1b97, 0x4513B0x1b97]
    =================================
    0x3001S0x1b97: v3001V1b97 = MLOAD v2ff0V1b97
    0x3002S0x1b97: v3002V1b97 = ISZERO v3001V1b97
    0x3003S0x1b97: v3003V1b97(0x4513) = CONST 
    0x3006S0x1b97: JUMPI v3003V1b97(0x4513), v3002V1b97

    Begin block 0x3007B0x1b97
    prev=[0x2fffB0x1b97], succ=[0x3058B0x1b97, 0x305cB0x1b97]
    =================================
    0x3008S0x1b97: v3008V1b97(0x1) = CONST 
    0x300aS0x1b97: v300aV1b97(0x1) = CONST 
    0x300cS0x1b97: v300cV1b97(0xa0) = CONST 
    0x300eS0x1b97: v300eV1b97(0x10000000000000000000000000000000000000000) = SHL v300cV1b97(0xa0), v300aV1b97(0x1)
    0x300fS0x1b97: v300fV1b97(0xffffffffffffffffffffffffffffffffffffffff) = SUB v300eV1b97(0x10000000000000000000000000000000000000000), v3008V1b97(0x1)
    0x3010S0x1b97: v3010V1b97 = AND v300fV1b97(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x3011S0x1b97: v3011V1b97(0x50e84861) = CONST 
    0x3019S0x1b97: v3019V1b97(0x40) = CONST 
    0x301bS0x1b97: v301bV1b97 = MLOAD v3019V1b97(0x40)
    0x301dS0x1b97: v301dV1b97(0xffffffff) = CONST 
    0x3022S0x1b97: v3022V1b97(0x50e84861) = AND v301dV1b97(0xffffffff), v3011V1b97(0x50e84861)
    0x3023S0x1b97: v3023V1b97(0xe0) = CONST 
    0x3025S0x1b97: v3025V1b97(0x50e8486100000000000000000000000000000000000000000000000000000000) = SHL v3023V1b97(0xe0), v3022V1b97(0x50e84861)
    0x3027S0x1b97: MSTORE v301bV1b97, v3025V1b97(0x50e8486100000000000000000000000000000000000000000000000000000000)
    0x3028S0x1b97: v3028V1b97(0x4) = CONST 
    0x302aS0x1b97: v302aV1b97 = ADD v3028V1b97(0x4), v301bV1b97
    0x302eS0x1b97: MSTORE v302aV1b97, v9c7
    0x302fS0x1b97: v302fV1b97(0x20) = CONST 
    0x3031S0x1b97: v3031V1b97 = ADD v302fV1b97(0x20), v302aV1b97
    0x3034S0x1b97: MSTORE v3031V1b97, v1c0a
    0x3035S0x1b97: v3035V1b97(0x20) = CONST 
    0x3037S0x1b97: v3037V1b97 = ADD v3035V1b97(0x20), v3031V1b97
    0x303aS0x1b97: MSTORE v3037V1b97, v9cc
    0x303bS0x1b97: v303bV1b97(0x20) = CONST 
    0x303dS0x1b97: v303dV1b97 = ADD v303bV1b97(0x20), v3037V1b97
    0x3043S0x1b97: v3043V1b97(0x0) = CONST 
    0x3045S0x1b97: v3045V1b97(0x40) = CONST 
    0x3047S0x1b97: v3047V1b97 = MLOAD v3045V1b97(0x40)
    0x304aS0x1b97: v304aV1b97(0x64) = SUB v303dV1b97, v3047V1b97
    0x304cS0x1b97: v304cV1b97(0x0) = CONST 
    0x3050S0x1b97: v3050V1b97 = EXTCODESIZE v3010V1b97
    0x3051S0x1b97: v3051V1b97 = ISZERO v3050V1b97
    0x3053S0x1b97: v3053V1b97 = ISZERO v3051V1b97
    0x3054S0x1b97: v3054V1b97(0x305c) = CONST 
    0x3057S0x1b97: JUMPI v3054V1b97(0x305c), v3053V1b97

    Begin block 0x3058B0x1b97
    prev=[0x3007B0x1b97], succ=[]
    =================================
    0x3058S0x1b97: v3058V1b97(0x0) = CONST 
    0x305bS0x1b97: REVERT v3058V1b97(0x0), v3058V1b97(0x0)

    Begin block 0x305cB0x1b97
    prev=[0x3007B0x1b97], succ=[0x3067B0x1b97, 0x3070B0x1b97]
    =================================
    0x305eS0x1b97: v305eV1b97 = GAS 
    0x305fS0x1b97: v305fV1b97 = CALL v305eV1b97, v3010V1b97, v304cV1b97(0x0), v3047V1b97, v304aV1b97(0x64), v3047V1b97, v3043V1b97(0x0)
    0x3060S0x1b97: v3060V1b97 = ISZERO v305fV1b97
    0x3062S0x1b97: v3062V1b97 = ISZERO v3060V1b97
    0x3063S0x1b97: v3063V1b97(0x3070) = CONST 
    0x3066S0x1b97: JUMPI v3063V1b97(0x3070), v3062V1b97

    Begin block 0x3067B0x1b97
    prev=[0x305cB0x1b97], succ=[]
    =================================
    0x3067S0x1b97: v3067V1b97 = RETURNDATASIZE 
    0x3068S0x1b97: v3068V1b97(0x0) = CONST 
    0x306bS0x1b97: RETURNDATACOPY v3068V1b97(0x0), v3068V1b97(0x0), v3067V1b97
    0x306cS0x1b97: v306cV1b97 = RETURNDATASIZE 
    0x306dS0x1b97: v306dV1b97(0x0) = CONST 
    0x306fS0x1b97: REVERT v306dV1b97(0x0), v306cV1b97

    Begin block 0x3070B0x1b97
    prev=[0x305cB0x1b97], succ=[0x3075B0x1b97]
    =================================

    Begin block 0x3075B0x1b97
    prev=[0x3070B0x1b97], succ=[0x1c10]
    =================================
    0x307aS0x1b97: JUMP v1bf3(0x1c10)

    Begin block 0x1c10
    prev=[0x44eeB0x1b97, 0x4513B0x1b97, 0x3075B0x1b97], succ=[0x3f93]
    =================================
    0x1c11: v1c11(0x0) = CONST 
    0x1c15: MSTORE v1c11(0x0), v9c7
    0x1c16: v1c16(0xa) = CONST 
    0x1c18: v1c18(0x20) = CONST 
    0x1c1a: MSTORE v1c18(0x20), v1c16(0xa)
    0x1c1b: v1c1b(0x40) = CONST 
    0x1c1f: v1c1f = SHA3 v1c11(0x0), v1c1b(0x40)
    0x1c21: v1c21 = SLOAD v1c1f
    0x1c22: v1c22(0x1) = CONST 
    0x1c24: v1c24(0x1) = CONST 
    0x1c26: v1c26(0x80) = CONST 
    0x1c28: v1c28(0x100000000000000000000000000000000) = SHL v1c26(0x80), v1c24(0x1)
    0x1c29: v1c29(0xffffffffffffffffffffffffffffffff) = SUB v1c28(0x100000000000000000000000000000000), v1c22(0x1)
    0x1c2c: v1c2c = AND v1c29(0xffffffffffffffffffffffffffffffff), v9cc
    0x1c2d: v1c2d(0x1) = CONST 
    0x1c2f: v1c2f(0x80) = CONST 
    0x1c31: v1c31(0x100000000000000000000000000000000) = SHL v1c2f(0x80), v1c2d(0x1)
    0x1c32: v1c32 = MUL v1c31(0x100000000000000000000000000000000), v1c2c
    0x1c34: v1c34 = AND v1c29(0xffffffffffffffffffffffffffffffff), v1c21
    0x1c38: v1c38 = OR v1c34, v1c32
    0x1c3a: SSTORE v1c1f, v1c38
    0x1c3c: JUMP v9a0(0x3f93)

    Begin block 0x3f93
    prev=[0x1c10], succ=[]
    =================================
    0x3f94: STOP 

    Begin block 0x4513B0x1b97
    prev=[0x2fffB0x1b97], succ=[0x1c10]
    =================================
    0x4518S0x1b97: JUMP v1bf3(0x1c10)

    Begin block 0x44eeB0x1b97
    prev=[0x2f83B0x1b97], succ=[0x1c10]
    =================================
    0x44f3S0x1b97: JUMP v1bf3(0x1c10)

    Begin block 0x2f71B0x1b97
    prev=[0x2f6aB0x1b97], succ=[0x2f83B0x1b97]
    =================================
    0x2f72S0x1b97: v2f72V1b97(0x2f83) = CONST 
    0x2f76S0x1b97: v2f76V1b97(0x1) = CONST 
    0x2f78S0x1b97: v2f78V1b97(0x1) = CONST 
    0x2f7aS0x1b97: v2f7aV1b97(0xa0) = CONST 
    0x2f7cS0x1b97: v2f7cV1b97(0x10000000000000000000000000000000000000000) = SHL v2f7aV1b97(0xa0), v2f78V1b97(0x1)
    0x2f7dS0x1b97: v2f7dV1b97(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f7cV1b97(0x10000000000000000000000000000000000000000), v2f76V1b97(0x1)
    0x2f7eS0x1b97: v2f7eV1b97 = AND v2f7dV1b97(0xffffffffffffffffffffffffffffffffffffffff), v9c1
    0x2f7fS0x1b97: v2f7fV1b97(0x36ac) = CONST 
    0x2f82S0x1b97: v2f82_0V1b97 = CALLPRIVATE v2f7fV1b97(0x36ac), v2f7eV1b97, v2f72V1b97(0x2f83)

}

function galaxyCommunity()() public {
    Begin block 0x9d1
    prev=[], succ=[0x1c3d]
    =================================
    0x9d2: v9d2(0x3fb4) = CONST 
    0x9d5: v9d5(0x1c3d) = CONST 
    0x9d8: JUMP v9d5(0x1c3d)

    Begin block 0x1c3d
    prev=[0x9d1], succ=[0x3fb4]
    =================================
    0x1c3e: v1c3e(0x4) = CONST 
    0x1c40: v1c40 = SLOAD v1c3e(0x4)
    0x1c41: v1c41(0x1) = CONST 
    0x1c43: v1c43(0x1) = CONST 
    0x1c45: v1c45(0xa0) = CONST 
    0x1c47: v1c47(0x10000000000000000000000000000000000000000) = SHL v1c45(0xa0), v1c43(0x1)
    0x1c48: v1c48(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c47(0x10000000000000000000000000000000000000000), v1c41(0x1)
    0x1c49: v1c49 = AND v1c48(0xffffffffffffffffffffffffffffffffffffffff), v1c40
    0x1c4b: JUMP v9d2(0x3fb4)

    Begin block 0x3fb4
    prev=[0x1c3d], succ=[]
    =================================
    0x3fb5: v3fb5(0x40) = CONST 
    0x3fb8: v3fb8 = MLOAD v3fb5(0x40)
    0x3fb9: v3fb9(0x1) = CONST 
    0x3fbb: v3fbb(0x1) = CONST 
    0x3fbd: v3fbd(0xa0) = CONST 
    0x3fbf: v3fbf(0x10000000000000000000000000000000000000000) = SHL v3fbd(0xa0), v3fbb(0x1)
    0x3fc0: v3fc0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fbf(0x10000000000000000000000000000000000000000), v3fb9(0x1)
    0x3fc3: v3fc3 = AND v1c49, v3fc0(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fc5: MSTORE v3fb8, v3fc3
    0x3fc6: v3fc6 = MLOAD v3fb5(0x40)
    0x3fca: v3fca(0x0) = SUB v3fb8, v3fc6
    0x3fcb: v3fcb(0x20) = CONST 
    0x3fcd: v3fcd(0x20) = ADD v3fcb(0x20), v3fca(0x0)
    0x3fcf: RETURN v3fc6, v3fcd(0x20)

}

function addMinter(address)() public {
    Begin block 0x9f5
    prev=[], succ=[0xa07, 0xa0b]
    =================================
    0x9f6: v9f6(0x3fef) = CONST 
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
    prev=[0x9f5], succ=[0x1c4c]
    =================================
    0xa0d: va0d = CALLDATALOAD v9f9(0x4)
    0xa0e: va0e(0x1) = CONST 
    0xa10: va10(0x1) = CONST 
    0xa12: va12(0xa0) = CONST 
    0xa14: va14(0x10000000000000000000000000000000000000000) = SHL va12(0xa0), va10(0x1)
    0xa15: va15(0xffffffffffffffffffffffffffffffffffffffff) = SUB va14(0x10000000000000000000000000000000000000000), va0e(0x1)
    0xa16: va16 = AND va15(0xffffffffffffffffffffffffffffffffffffffff), va0d
    0xa17: va17(0x1c4c) = CONST 
    0xa1a: JUMP va17(0x1c4c)

    Begin block 0x1c4c
    prev=[0xa0b], succ=[0x1c5f, 0x1c9b]
    =================================
    0x1c4d: v1c4d(0x3) = CONST 
    0x1c4f: v1c4f = SLOAD v1c4d(0x3)
    0x1c50: v1c50(0x1) = CONST 
    0x1c52: v1c52(0x1) = CONST 
    0x1c54: v1c54(0xa0) = CONST 
    0x1c56: v1c56(0x10000000000000000000000000000000000000000) = SHL v1c54(0xa0), v1c52(0x1)
    0x1c57: v1c57(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c56(0x10000000000000000000000000000000000000000), v1c50(0x1)
    0x1c58: v1c58 = AND v1c57(0xffffffffffffffffffffffffffffffffffffffff), v1c4f
    0x1c59: v1c59 = CALLER 
    0x1c5a: v1c5a = EQ v1c59, v1c58
    0x1c5b: v1c5b(0x1c9b) = CONST 
    0x1c5e: JUMPI v1c5b(0x1c9b), v1c5a

    Begin block 0x1c5f
    prev=[0x1c4c], succ=[]
    =================================
    0x1c5f: v1c5f(0x40) = CONST 
    0x1c62: v1c62 = MLOAD v1c5f(0x40)
    0x1c63: v1c63(0x461bcd) = CONST 
    0x1c67: v1c67(0xe5) = CONST 
    0x1c69: v1c69(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c67(0xe5), v1c63(0x461bcd)
    0x1c6b: MSTORE v1c62, v1c69(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c6c: v1c6c(0x20) = CONST 
    0x1c6e: v1c6e(0x4) = CONST 
    0x1c71: v1c71 = ADD v1c62, v1c6e(0x4)
    0x1c72: MSTORE v1c71, v1c6c(0x20)
    0x1c73: v1c73(0xd) = CONST 
    0x1c75: v1c75(0x24) = CONST 
    0x1c78: v1c78 = ADD v1c62, v1c75(0x24)
    0x1c79: MSTORE v1c78, v1c73(0xd)
    0x1c7a: v1c7a(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1c88: v1c88(0x99) = CONST 
    0x1c8a: v1c8a(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1c88(0x99), v1c7a(0x26bab9ba1031329037bbb732b9)
    0x1c8b: v1c8b(0x44) = CONST 
    0x1c8e: v1c8e = ADD v1c62, v1c8b(0x44)
    0x1c8f: MSTORE v1c8e, v1c8a(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1c91: v1c91 = MLOAD v1c5f(0x40)
    0x1c95: v1c95(0x0) = SUB v1c62, v1c91
    0x1c96: v1c96(0x64) = CONST 
    0x1c98: v1c98(0x64) = ADD v1c96(0x64), v1c95(0x0)
    0x1c9a: REVERT v1c91, v1c98(0x64)

    Begin block 0x1c9b
    prev=[0x1c4c], succ=[0x1caa, 0x1cf6]
    =================================
    0x1c9c: v1c9c(0x1) = CONST 
    0x1c9e: v1c9e(0x1) = CONST 
    0x1ca0: v1ca0(0xa0) = CONST 
    0x1ca2: v1ca2(0x10000000000000000000000000000000000000000) = SHL v1ca0(0xa0), v1c9e(0x1)
    0x1ca3: v1ca3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ca2(0x10000000000000000000000000000000000000000), v1c9c(0x1)
    0x1ca5: v1ca5 = AND va16, v1ca3(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ca6: v1ca6(0x1cf6) = CONST 
    0x1ca9: JUMPI v1ca6(0x1cf6), v1ca5

    Begin block 0x1caa
    prev=[0x1c9b], succ=[]
    =================================
    0x1caa: v1caa(0x40) = CONST 
    0x1cad: v1cad = MLOAD v1caa(0x40)
    0x1cae: v1cae(0x461bcd) = CONST 
    0x1cb2: v1cb2(0xe5) = CONST 
    0x1cb4: v1cb4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1cb2(0xe5), v1cae(0x461bcd)
    0x1cb6: MSTORE v1cad, v1cb4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cb7: v1cb7(0x20) = CONST 
    0x1cb9: v1cb9(0x4) = CONST 
    0x1cbc: v1cbc = ADD v1cad, v1cb9(0x4)
    0x1cbd: MSTORE v1cbc, v1cb7(0x20)
    0x1cbe: v1cbe(0x1f) = CONST 
    0x1cc0: v1cc0(0x24) = CONST 
    0x1cc3: v1cc3 = ADD v1cad, v1cc0(0x24)
    0x1cc4: MSTORE v1cc3, v1cbe(0x1f)
    0x1cc5: v1cc5(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300) = CONST 
    0x1ce6: v1ce6(0x44) = CONST 
    0x1ce9: v1ce9 = ADD v1cad, v1ce6(0x44)
    0x1cea: MSTORE v1ce9, v1cc5(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300)
    0x1cec: v1cec = MLOAD v1caa(0x40)
    0x1cf0: v1cf0(0x0) = SUB v1cad, v1cec
    0x1cf1: v1cf1(0x64) = CONST 
    0x1cf3: v1cf3(0x64) = ADD v1cf1(0x64), v1cf0(0x0)
    0x1cf5: REVERT v1cec, v1cf3(0x64)

    Begin block 0x1cf6
    prev=[0x1c9b], succ=[0x1d18, 0x1d5b]
    =================================
    0x1cf7: v1cf7(0x1) = CONST 
    0x1cf9: v1cf9(0x1) = CONST 
    0x1cfb: v1cfb(0xa0) = CONST 
    0x1cfd: v1cfd(0x10000000000000000000000000000000000000000) = SHL v1cfb(0xa0), v1cf9(0x1)
    0x1cfe: v1cfe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cfd(0x10000000000000000000000000000000000000000), v1cf7(0x1)
    0x1d00: v1d00 = AND va16, v1cfe(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d01: v1d01(0x0) = CONST 
    0x1d05: MSTORE v1d01(0x0), v1d00
    0x1d06: v1d06(0x5) = CONST 
    0x1d08: v1d08(0x20) = CONST 
    0x1d0a: MSTORE v1d08(0x20), v1d06(0x5)
    0x1d0b: v1d0b(0x40) = CONST 
    0x1d0e: v1d0e = SHA3 v1d01(0x0), v1d0b(0x40)
    0x1d0f: v1d0f = SLOAD v1d0e
    0x1d10: v1d10(0xff) = CONST 
    0x1d12: v1d12 = AND v1d10(0xff), v1d0f
    0x1d13: v1d13 = ISZERO v1d12
    0x1d14: v1d14(0x1d5b) = CONST 
    0x1d17: JUMPI v1d14(0x1d5b), v1d13

    Begin block 0x1d18
    prev=[0x1cf6], succ=[]
    =================================
    0x1d18: v1d18(0x40) = CONST 
    0x1d1b: v1d1b = MLOAD v1d18(0x40)
    0x1d1c: v1d1c(0x461bcd) = CONST 
    0x1d20: v1d20(0xe5) = CONST 
    0x1d22: v1d22(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1d20(0xe5), v1d1c(0x461bcd)
    0x1d24: MSTORE v1d1b, v1d22(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d25: v1d25(0x20) = CONST 
    0x1d27: v1d27(0x4) = CONST 
    0x1d2a: v1d2a = ADD v1d1b, v1d27(0x4)
    0x1d2b: MSTORE v1d2a, v1d25(0x20)
    0x1d2c: v1d2c(0x14) = CONST 
    0x1d2e: v1d2e(0x24) = CONST 
    0x1d31: v1d31 = ADD v1d1b, v1d2e(0x24)
    0x1d32: MSTORE v1d31, v1d2c(0x14)
    0x1d33: v1d33(0x135a5b9d195c88185b1c9958591e481859191959) = CONST 
    0x1d48: v1d48(0x62) = CONST 
    0x1d4a: v1d4a(0x4d696e74657220616c7265616479206164646564000000000000000000000000) = SHL v1d48(0x62), v1d33(0x135a5b9d195c88185b1c9958591e481859191959)
    0x1d4b: v1d4b(0x44) = CONST 
    0x1d4e: v1d4e = ADD v1d1b, v1d4b(0x44)
    0x1d4f: MSTORE v1d4e, v1d4a(0x4d696e74657220616c7265616479206164646564000000000000000000000000)
    0x1d51: v1d51 = MLOAD v1d18(0x40)
    0x1d55: v1d55(0x0) = SUB v1d1b, v1d51
    0x1d56: v1d56(0x64) = CONST 
    0x1d58: v1d58(0x64) = ADD v1d56(0x64), v1d55(0x0)
    0x1d5a: REVERT v1d51, v1d58(0x64)

    Begin block 0x1d5b
    prev=[0x1cf6], succ=[0x3fef]
    =================================
    0x1d5c: v1d5c(0x1) = CONST 
    0x1d5e: v1d5e(0x1) = CONST 
    0x1d60: v1d60(0xa0) = CONST 
    0x1d62: v1d62(0x10000000000000000000000000000000000000000) = SHL v1d60(0xa0), v1d5e(0x1)
    0x1d63: v1d63(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d62(0x10000000000000000000000000000000000000000), v1d5c(0x1)
    0x1d64: v1d64 = AND v1d63(0xffffffffffffffffffffffffffffffffffffffff), va16
    0x1d65: v1d65(0x0) = CONST 
    0x1d69: MSTORE v1d65(0x0), v1d64
    0x1d6a: v1d6a(0x5) = CONST 
    0x1d6c: v1d6c(0x20) = CONST 
    0x1d6e: MSTORE v1d6c(0x20), v1d6a(0x5)
    0x1d6f: v1d6f(0x40) = CONST 
    0x1d72: v1d72 = SHA3 v1d65(0x0), v1d6f(0x40)
    0x1d74: v1d74 = SLOAD v1d72
    0x1d75: v1d75(0xff) = CONST 
    0x1d77: v1d77(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1d75(0xff)
    0x1d78: v1d78 = AND v1d77(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1d74
    0x1d79: v1d79(0x1) = CONST 
    0x1d7b: v1d7b = OR v1d79(0x1), v1d78
    0x1d7d: SSTORE v1d72, v1d7b
    0x1d7e: JUMP v9f6(0x3fef)

    Begin block 0x3fef
    prev=[0x1d5b], succ=[]
    =================================
    0x3ff0: STOP 

}

function addOperator(address)() public {
    Begin block 0xa1b
    prev=[], succ=[0xa2d, 0xa31]
    =================================
    0xa1c: va1c(0x4010) = CONST 
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
    prev=[0xa1b], succ=[0x1d7f]
    =================================
    0xa33: va33 = CALLDATALOAD va1f(0x4)
    0xa34: va34(0x1) = CONST 
    0xa36: va36(0x1) = CONST 
    0xa38: va38(0xa0) = CONST 
    0xa3a: va3a(0x10000000000000000000000000000000000000000) = SHL va38(0xa0), va36(0x1)
    0xa3b: va3b(0xffffffffffffffffffffffffffffffffffffffff) = SUB va3a(0x10000000000000000000000000000000000000000), va34(0x1)
    0xa3c: va3c = AND va3b(0xffffffffffffffffffffffffffffffffffffffff), va33
    0xa3d: va3d(0x1d7f) = CONST 
    0xa40: JUMP va3d(0x1d7f)

    Begin block 0x1d7f
    prev=[0xa31], succ=[0x1d92, 0x1dce]
    =================================
    0x1d80: v1d80(0x3) = CONST 
    0x1d82: v1d82 = SLOAD v1d80(0x3)
    0x1d83: v1d83(0x1) = CONST 
    0x1d85: v1d85(0x1) = CONST 
    0x1d87: v1d87(0xa0) = CONST 
    0x1d89: v1d89(0x10000000000000000000000000000000000000000) = SHL v1d87(0xa0), v1d85(0x1)
    0x1d8a: v1d8a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d89(0x10000000000000000000000000000000000000000), v1d83(0x1)
    0x1d8b: v1d8b = AND v1d8a(0xffffffffffffffffffffffffffffffffffffffff), v1d82
    0x1d8c: v1d8c = CALLER 
    0x1d8d: v1d8d = EQ v1d8c, v1d8b
    0x1d8e: v1d8e(0x1dce) = CONST 
    0x1d91: JUMPI v1d8e(0x1dce), v1d8d

    Begin block 0x1d92
    prev=[0x1d7f], succ=[]
    =================================
    0x1d92: v1d92(0x40) = CONST 
    0x1d95: v1d95 = MLOAD v1d92(0x40)
    0x1d96: v1d96(0x461bcd) = CONST 
    0x1d9a: v1d9a(0xe5) = CONST 
    0x1d9c: v1d9c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1d9a(0xe5), v1d96(0x461bcd)
    0x1d9e: MSTORE v1d95, v1d9c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d9f: v1d9f(0x20) = CONST 
    0x1da1: v1da1(0x4) = CONST 
    0x1da4: v1da4 = ADD v1d95, v1da1(0x4)
    0x1da5: MSTORE v1da4, v1d9f(0x20)
    0x1da6: v1da6(0xd) = CONST 
    0x1da8: v1da8(0x24) = CONST 
    0x1dab: v1dab = ADD v1d95, v1da8(0x24)
    0x1dac: MSTORE v1dab, v1da6(0xd)
    0x1dad: v1dad(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1dbb: v1dbb(0x99) = CONST 
    0x1dbd: v1dbd(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1dbb(0x99), v1dad(0x26bab9ba1031329037bbb732b9)
    0x1dbe: v1dbe(0x44) = CONST 
    0x1dc1: v1dc1 = ADD v1d95, v1dbe(0x44)
    0x1dc2: MSTORE v1dc1, v1dbd(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1dc4: v1dc4 = MLOAD v1d92(0x40)
    0x1dc8: v1dc8(0x0) = SUB v1d95, v1dc4
    0x1dc9: v1dc9(0x64) = CONST 
    0x1dcb: v1dcb(0x64) = ADD v1dc9(0x64), v1dc8(0x0)
    0x1dcd: REVERT v1dc4, v1dcb(0x64)

    Begin block 0x1dce
    prev=[0x1d7f], succ=[0x1ddd, 0x1e13]
    =================================
    0x1dcf: v1dcf(0x1) = CONST 
    0x1dd1: v1dd1(0x1) = CONST 
    0x1dd3: v1dd3(0xa0) = CONST 
    0x1dd5: v1dd5(0x10000000000000000000000000000000000000000) = SHL v1dd3(0xa0), v1dd1(0x1)
    0x1dd6: v1dd6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1dd5(0x10000000000000000000000000000000000000000), v1dcf(0x1)
    0x1dd8: v1dd8 = AND va3c, v1dd6(0xffffffffffffffffffffffffffffffffffffffff)
    0x1dd9: v1dd9(0x1e13) = CONST 
    0x1ddc: JUMPI v1dd9(0x1e13), v1dd8

    Begin block 0x1ddd
    prev=[0x1dce], succ=[]
    =================================
    0x1ddd: v1ddd(0x40) = CONST 
    0x1ddf: v1ddf = MLOAD v1ddd(0x40)
    0x1de0: v1de0(0x461bcd) = CONST 
    0x1de4: v1de4(0xe5) = CONST 
    0x1de6: v1de6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1de4(0xe5), v1de0(0x461bcd)
    0x1de8: MSTORE v1ddf, v1de6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1de9: v1de9(0x4) = CONST 
    0x1deb: v1deb = ADD v1de9(0x4), v1ddf
    0x1dee: v1dee(0x20) = CONST 
    0x1df0: v1df0 = ADD v1dee(0x20), v1deb
    0x1df3: v1df3(0x20) = SUB v1df0, v1deb
    0x1df5: MSTORE v1deb, v1df3(0x20)
    0x1df6: v1df6(0x21) = CONST 
    0x1df9: MSTORE v1df0, v1df6(0x21)
    0x1dfa: v1dfa(0x20) = CONST 
    0x1dfc: v1dfc = ADD v1dfa(0x20), v1df0
    0x1dfe: v1dfe(0x3b27) = CONST 
    0x1e01: v1e01(0x21) = CONST 
    0x1e04: CODECOPY v1dfc, v1dfe(0x3b27), v1e01(0x21)
    0x1e05: v1e05(0x40) = CONST 
    0x1e07: v1e07 = ADD v1e05(0x40), v1dfc
    0x1e0b: v1e0b(0x40) = CONST 
    0x1e0d: v1e0d = MLOAD v1e0b(0x40)
    0x1e10: v1e10(0x84) = SUB v1e07, v1e0d
    0x1e12: REVERT v1e0d, v1e10(0x84)

    Begin block 0x1e13
    prev=[0x1dce], succ=[0x1e35, 0x1e7a]
    =================================
    0x1e14: v1e14(0x1) = CONST 
    0x1e16: v1e16(0x1) = CONST 
    0x1e18: v1e18(0xa0) = CONST 
    0x1e1a: v1e1a(0x10000000000000000000000000000000000000000) = SHL v1e18(0xa0), v1e16(0x1)
    0x1e1b: v1e1b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e1a(0x10000000000000000000000000000000000000000), v1e14(0x1)
    0x1e1d: v1e1d = AND va3c, v1e1b(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e1e: v1e1e(0x0) = CONST 
    0x1e22: MSTORE v1e1e(0x0), v1e1d
    0x1e23: v1e23(0x6) = CONST 
    0x1e25: v1e25(0x20) = CONST 
    0x1e27: MSTORE v1e25(0x20), v1e23(0x6)
    0x1e28: v1e28(0x40) = CONST 
    0x1e2b: v1e2b = SHA3 v1e1e(0x0), v1e28(0x40)
    0x1e2c: v1e2c = SLOAD v1e2b
    0x1e2d: v1e2d(0xff) = CONST 
    0x1e2f: v1e2f = AND v1e2d(0xff), v1e2c
    0x1e30: v1e30 = ISZERO v1e2f
    0x1e31: v1e31(0x1e7a) = CONST 
    0x1e34: JUMPI v1e31(0x1e7a), v1e30

    Begin block 0x1e35
    prev=[0x1e13], succ=[]
    =================================
    0x1e35: v1e35(0x40) = CONST 
    0x1e38: v1e38 = MLOAD v1e35(0x40)
    0x1e39: v1e39(0x461bcd) = CONST 
    0x1e3d: v1e3d(0xe5) = CONST 
    0x1e3f: v1e3f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e3d(0xe5), v1e39(0x461bcd)
    0x1e41: MSTORE v1e38, v1e3f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e42: v1e42(0x20) = CONST 
    0x1e44: v1e44(0x4) = CONST 
    0x1e47: v1e47 = ADD v1e38, v1e44(0x4)
    0x1e48: MSTORE v1e47, v1e42(0x20)
    0x1e49: v1e49(0x16) = CONST 
    0x1e4b: v1e4b(0x24) = CONST 
    0x1e4e: v1e4e = ADD v1e38, v1e4b(0x24)
    0x1e4f: MSTORE v1e4e, v1e49(0x16)
    0x1e50: v1e50(0x13dc195c985d1bdc88185b1c9958591e481859191959) = CONST 
    0x1e67: v1e67(0x52) = CONST 
    0x1e69: v1e69(0x4f70657261746f7220616c726561647920616464656400000000000000000000) = SHL v1e67(0x52), v1e50(0x13dc195c985d1bdc88185b1c9958591e481859191959)
    0x1e6a: v1e6a(0x44) = CONST 
    0x1e6d: v1e6d = ADD v1e38, v1e6a(0x44)
    0x1e6e: MSTORE v1e6d, v1e69(0x4f70657261746f7220616c726561647920616464656400000000000000000000)
    0x1e70: v1e70 = MLOAD v1e35(0x40)
    0x1e74: v1e74(0x0) = SUB v1e38, v1e70
    0x1e75: v1e75(0x64) = CONST 
    0x1e77: v1e77(0x64) = ADD v1e75(0x64), v1e74(0x0)
    0x1e79: REVERT v1e70, v1e77(0x64)

    Begin block 0x1e7a
    prev=[0x1e13], succ=[0x4010]
    =================================
    0x1e7b: v1e7b(0x1) = CONST 
    0x1e7d: v1e7d(0x1) = CONST 
    0x1e7f: v1e7f(0xa0) = CONST 
    0x1e81: v1e81(0x10000000000000000000000000000000000000000) = SHL v1e7f(0xa0), v1e7d(0x1)
    0x1e82: v1e82(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e81(0x10000000000000000000000000000000000000000), v1e7b(0x1)
    0x1e83: v1e83 = AND v1e82(0xffffffffffffffffffffffffffffffffffffffff), va3c
    0x1e84: v1e84(0x0) = CONST 
    0x1e88: MSTORE v1e84(0x0), v1e83
    0x1e89: v1e89(0x6) = CONST 
    0x1e8b: v1e8b(0x20) = CONST 
    0x1e8d: MSTORE v1e8b(0x20), v1e89(0x6)
    0x1e8e: v1e8e(0x40) = CONST 
    0x1e91: v1e91 = SHA3 v1e84(0x0), v1e8e(0x40)
    0x1e93: v1e93 = SLOAD v1e91
    0x1e94: v1e94(0xff) = CONST 
    0x1e96: v1e96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1e94(0xff)
    0x1e97: v1e97 = AND v1e96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1e93
    0x1e98: v1e98(0x1) = CONST 
    0x1e9a: v1e9a = OR v1e98(0x1), v1e97
    0x1e9c: SSTORE v1e91, v1e9a
    0x1e9d: JUMP va1c(0x4010)

    Begin block 0x4010
    prev=[0x1e7a], succ=[]
    =================================
    0x4011: STOP 

}

function burn(address,uint256)() public {
    Begin block 0xa41
    prev=[], succ=[0xa53, 0xa57]
    =================================
    0xa42: va42(0x4031) = CONST 
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
    prev=[0xa41], succ=[0x1e9e]
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
    0xa69: va69(0x1e9e) = CONST 
    0xa6c: JUMP va69(0x1e9e)

    Begin block 0x1e9e
    prev=[0xa57], succ=[0x1eb6, 0x1ef3]
    =================================
    0x1e9f: v1e9f = CALLER 
    0x1ea0: v1ea0(0x0) = CONST 
    0x1ea4: MSTORE v1ea0(0x0), v1e9f
    0x1ea5: v1ea5(0x5) = CONST 
    0x1ea7: v1ea7(0x20) = CONST 
    0x1ea9: MSTORE v1ea7(0x20), v1ea5(0x5)
    0x1eaa: v1eaa(0x40) = CONST 
    0x1ead: v1ead = SHA3 v1ea0(0x0), v1eaa(0x40)
    0x1eae: v1eae = SLOAD v1ead
    0x1eaf: v1eaf(0xff) = CONST 
    0x1eb1: v1eb1 = AND v1eaf(0xff), v1eae
    0x1eb2: v1eb2(0x1ef3) = CONST 
    0x1eb5: JUMPI v1eb2(0x1ef3), v1eb1

    Begin block 0x1eb6
    prev=[0x1e9e], succ=[]
    =================================
    0x1eb6: v1eb6(0x40) = CONST 
    0x1eb9: v1eb9 = MLOAD v1eb6(0x40)
    0x1eba: v1eba(0x461bcd) = CONST 
    0x1ebe: v1ebe(0xe5) = CONST 
    0x1ec0: v1ec0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1ebe(0xe5), v1eba(0x461bcd)
    0x1ec2: MSTORE v1eb9, v1ec0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ec3: v1ec3(0x20) = CONST 
    0x1ec5: v1ec5(0x4) = CONST 
    0x1ec8: v1ec8 = ADD v1eb9, v1ec5(0x4)
    0x1ec9: MSTORE v1ec8, v1ec3(0x20)
    0x1eca: v1eca(0xe) = CONST 
    0x1ecc: v1ecc(0x24) = CONST 
    0x1ecf: v1ecf = ADD v1eb9, v1ecc(0x24)
    0x1ed0: MSTORE v1ecf, v1eca(0xe)
    0x1ed1: v1ed1(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x1ee0: v1ee0(0x91) = CONST 
    0x1ee2: v1ee2(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v1ee0(0x91), v1ed1(0x36bab9ba1031329036b4b73a32b9)
    0x1ee3: v1ee3(0x44) = CONST 
    0x1ee6: v1ee6 = ADD v1eb9, v1ee3(0x44)
    0x1ee7: MSTORE v1ee6, v1ee2(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x1ee9: v1ee9 = MLOAD v1eb6(0x40)
    0x1eed: v1eed(0x0) = SUB v1eb9, v1ee9
    0x1eee: v1eee(0x64) = CONST 
    0x1ef0: v1ef0(0x64) = ADD v1eee(0x64), v1eed(0x0)
    0x1ef2: REVERT v1ee9, v1ef0(0x64)

    Begin block 0x1ef3
    prev=[0x1e9e], succ=[0x1efd]
    =================================
    0x1ef4: v1ef4(0x1efd) = CONST 
    0x1ef9: v1ef9(0x24b9) = CONST 
    0x1efc: v1efc_0 = CALLPRIVATE v1ef9(0x24b9), va68, va63, v1ef4(0x1efd)

    Begin block 0x1efd
    prev=[0x1ef3], succ=[0x1f02, 0x1f3e]
    =================================
    0x1efe: v1efe(0x1f3e) = CONST 
    0x1f01: JUMPI v1efe(0x1f3e), v1efc_0

    Begin block 0x1f02
    prev=[0x1efd], succ=[]
    =================================
    0x1f02: v1f02(0x40) = CONST 
    0x1f05: v1f05 = MLOAD v1f02(0x40)
    0x1f06: v1f06(0x461bcd) = CONST 
    0x1f0a: v1f0a(0xe5) = CONST 
    0x1f0c: v1f0c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f0a(0xe5), v1f06(0x461bcd)
    0x1f0e: MSTORE v1f05, v1f0c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f0f: v1f0f(0x20) = CONST 
    0x1f11: v1f11(0x4) = CONST 
    0x1f14: v1f14 = ADD v1f05, v1f11(0x4)
    0x1f15: MSTORE v1f14, v1f0f(0x20)
    0x1f16: v1f16(0xd) = CONST 
    0x1f18: v1f18(0x24) = CONST 
    0x1f1b: v1f1b = ADD v1f05, v1f18(0x24)
    0x1f1c: MSTORE v1f1b, v1f16(0xd)
    0x1f1d: v1f1d(0x2737ba103a34329037bbb732b9) = CONST 
    0x1f2b: v1f2b(0x99) = CONST 
    0x1f2d: v1f2d(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v1f2b(0x99), v1f1d(0x2737ba103a34329037bbb732b9)
    0x1f2e: v1f2e(0x44) = CONST 
    0x1f31: v1f31 = ADD v1f05, v1f2e(0x44)
    0x1f32: MSTORE v1f31, v1f2d(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1f34: v1f34 = MLOAD v1f02(0x40)
    0x1f38: v1f38(0x0) = SUB v1f05, v1f34
    0x1f39: v1f39(0x64) = CONST 
    0x1f3b: v1f3b(0x64) = ADD v1f39(0x64), v1f38(0x0)
    0x1f3d: REVERT v1f34, v1f3b(0x64)

    Begin block 0x1f3e
    prev=[0x1efd], succ=[0x307b]
    =================================
    0x1f3f: v1f3f(0x43c7) = CONST 
    0x1f44: v1f44(0x307b) = CONST 
    0x1f47: JUMP v1f44(0x307b)

    Begin block 0x307b
    prev=[0x1f3e], succ=[0x38c1B0x307b]
    =================================
    0x307c: v307c(0x0) = CONST 
    0x3080: MSTORE v307c(0x0), va68
    0x3081: v3081(0x8) = CONST 
    0x3083: v3083(0x20) = CONST 
    0x3087: MSTORE v3083(0x20), v3081(0x8)
    0x3088: v3088(0x40) = CONST 
    0x308c: v308c = SHA3 v307c(0x0), v3088(0x40)
    0x308e: v308e = SLOAD v308c
    0x308f: v308f(0x1) = CONST 
    0x3091: v3091(0x1) = CONST 
    0x3093: v3093(0xa0) = CONST 
    0x3095: v3095(0x10000000000000000000000000000000000000000) = SHL v3093(0xa0), v3091(0x1)
    0x3096: v3096(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3095(0x10000000000000000000000000000000000000000), v308f(0x1)
    0x3097: v3097(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3096(0xffffffffffffffffffffffffffffffffffffffff)
    0x309a: v309a = AND v3097(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v308e
    0x309d: SSTORE v308c, v309a
    0x309e: v309e(0xb) = CONST 
    0x30a1: MSTORE v3083(0x20), v309e(0xb)
    0x30a4: v30a4 = SHA3 v307c(0x0), v3088(0x40)
    0x30a6: v30a6 = SLOAD v30a4
    0x30a9: v30a9 = AND v3097(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v30a6
    0x30ab: SSTORE v30a4, v30a9
    0x30ac: v30ac(0x1) = CONST 
    0x30af: v30af = ADD v30a4, v30ac(0x1)
    0x30b2: SSTORE v30af, v307c(0x0)
    0x30b3: v30b3(0x2) = CONST 
    0x30b5: v30b5 = ADD v30b3(0x2), v30a4
    0x30b8: SSTORE v30b5, v307c(0x0)
    0x30b9: v30b9(0xc) = CONST 
    0x30bd: MSTORE v3083(0x20), v30b9(0xc)
    0x30bf: v30bf = SHA3 v307c(0x0), v3088(0x40)
    0x30c1: v30c1(0x30ca) = CONST 
    0x30c6: v30c6(0x38c1) = CONST 
    0x30c9: JUMP v30c6(0x38c1), v307c(0x0), v30bf, v30c1(0x30ca)

    Begin block 0x38c1B0x307b
    prev=[0x307b], succ=[0x3970B0x38c1B0x307b]
    =================================
    0x38c4S0x307b: v38c4V307b = SLOAD v30bf
    0x38c5S0x307b: v38c5V307b(0x0) = CONST 
    0x38c8S0x307b: SSTORE v30bf, v38c5V307b(0x0)
    0x38caS0x307b: v38caV307b(0x0) = CONST 
    0x38ccS0x307b: MSTORE v38caV307b(0x0), v30bf
    0x38cdS0x307b: v38cdV307b(0x20) = CONST 
    0x38cfS0x307b: v38cfV307b(0x0) = CONST 
    0x38d1S0x307b: v38d1V307b = SHA3 v38cfV307b(0x0), v38cdV307b(0x20)
    0x38d4S0x307b: v38d4V307b = ADD v38d1V307b, v38c4V307b
    0x38d6S0x307b: v38d6V307b(0x38df) = CONST 
    0x38dbS0x307b: v38dbV307b(0x3970) = CONST 
    0x38deS0x307b: JUMP v38dbV307b(0x3970)

    Begin block 0x3970B0x38c1B0x307b
    prev=[0x38c1B0x307b], succ=[0x3971B0x38c1B0x307b]
    =================================

    Begin block 0x3971B0x38c1B0x307b
    prev=[0x397aB0x38c1B0x307b, 0x3970B0x38c1B0x307b], succ=[0x397aB0x38c1B0x307b, 0x45cfB0x38c1B0x307b]
    =================================
    0x3971_0x0S0x38c1S0x307b: v3971_0V38c1V307b = PHI v38d1V307b, v3980V38c1V307b
    0x3974S0x38c1S0x307b: v3974V38c1V307b = GT v38d4V307b, v3971_0V38c1V307b
    0x3975S0x38c1S0x307b: v3975V38c1V307b = ISZERO v3974V38c1V307b
    0x3976S0x38c1S0x307b: v3976V38c1V307b(0x45cf) = CONST 
    0x3979S0x38c1S0x307b: JUMPI v3976V38c1V307b(0x45cf), v3975V38c1V307b

    Begin block 0x397aB0x38c1B0x307b
    prev=[0x3971B0x38c1B0x307b], succ=[0x3971B0x38c1B0x307b]
    =================================
    0x397aS0x38c1S0x307b: v397aV38c1V307b(0x0) = CONST 
    0x397a_0x0S0x38c1S0x307b: v397a_0V38c1V307b = PHI v38d1V307b, v3980V38c1V307b
    0x397dS0x38c1S0x307b: SSTORE v397a_0V38c1V307b, v397aV38c1V307b(0x0)
    0x397eS0x38c1S0x307b: v397eV38c1V307b(0x1) = CONST 
    0x3980S0x38c1S0x307b: v3980V38c1V307b = ADD v397eV38c1V307b(0x1), v397a_0V38c1V307b
    0x3981S0x38c1S0x307b: v3981V38c1V307b(0x3971) = CONST 
    0x3984S0x38c1S0x307b: JUMP v3981V38c1V307b(0x3971)

    Begin block 0x45cfB0x38c1B0x307b
    prev=[0x3971B0x38c1B0x307b], succ=[0x38dfB0x307b]
    =================================
    0x45d2S0x38c1S0x307b: JUMP v38d6V307b(0x38df)

    Begin block 0x38dfB0x307b
    prev=[0x45cfB0x38c1B0x307b], succ=[0x30ca]
    =================================
    0x38e1S0x307b: JUMP v30c1(0x30ca)

    Begin block 0x30ca
    prev=[0x38dfB0x307b], succ=[0x38c1B0x30ca]
    =================================
    0x30cb: v30cb(0x30d8) = CONST 
    0x30ce: v30ce(0x1) = CONST 
    0x30d1: v30d1 = ADD v30bf, v30ce(0x1)
    0x30d2: v30d2(0x0) = CONST 
    0x30d4: v30d4(0x38c1) = CONST 
    0x30d7: JUMP v30d4(0x38c1), v30d2(0x0), v30d1, v30cb(0x30d8)

    Begin block 0x38c1B0x30ca
    prev=[0x30ca], succ=[0x3970B0x38c1B0x30ca]
    =================================
    0x38c4S0x30ca: v38c4V30ca = SLOAD v30d1
    0x38c5S0x30ca: v38c5V30ca(0x0) = CONST 
    0x38c8S0x30ca: SSTORE v30d1, v38c5V30ca(0x0)
    0x38caS0x30ca: v38caV30ca(0x0) = CONST 
    0x38ccS0x30ca: MSTORE v38caV30ca(0x0), v30d1
    0x38cdS0x30ca: v38cdV30ca(0x20) = CONST 
    0x38cfS0x30ca: v38cfV30ca(0x0) = CONST 
    0x38d1S0x30ca: v38d1V30ca = SHA3 v38cfV30ca(0x0), v38cdV30ca(0x20)
    0x38d4S0x30ca: v38d4V30ca = ADD v38d1V30ca, v38c4V30ca
    0x38d6S0x30ca: v38d6V30ca(0x38df) = CONST 
    0x38dbS0x30ca: v38dbV30ca(0x3970) = CONST 
    0x38deS0x30ca: JUMP v38dbV30ca(0x3970)

    Begin block 0x3970B0x38c1B0x30ca
    prev=[0x38c1B0x30ca], succ=[0x3971B0x38c1B0x30ca]
    =================================

    Begin block 0x3971B0x38c1B0x30ca
    prev=[0x397aB0x38c1B0x30ca, 0x3970B0x38c1B0x30ca], succ=[0x397aB0x38c1B0x30ca, 0x45cfB0x38c1B0x30ca]
    =================================
    0x3971_0x0S0x38c1S0x30ca: v3971_0V38c1V30ca = PHI v38d1V30ca, v3980V38c1V30ca
    0x3974S0x38c1S0x30ca: v3974V38c1V30ca = GT v38d4V30ca, v3971_0V38c1V30ca
    0x3975S0x38c1S0x30ca: v3975V38c1V30ca = ISZERO v3974V38c1V30ca
    0x3976S0x38c1S0x30ca: v3976V38c1V30ca(0x45cf) = CONST 
    0x3979S0x38c1S0x30ca: JUMPI v3976V38c1V30ca(0x45cf), v3975V38c1V30ca

    Begin block 0x397aB0x38c1B0x30ca
    prev=[0x3971B0x38c1B0x30ca], succ=[0x3971B0x38c1B0x30ca]
    =================================
    0x397aS0x38c1S0x30ca: v397aV38c1V30ca(0x0) = CONST 
    0x397a_0x0S0x38c1S0x30ca: v397a_0V38c1V30ca = PHI v38d1V30ca, v3980V38c1V30ca
    0x397dS0x38c1S0x30ca: SSTORE v397a_0V38c1V30ca, v397aV38c1V30ca(0x0)
    0x397eS0x38c1S0x30ca: v397eV38c1V30ca(0x1) = CONST 
    0x3980S0x38c1S0x30ca: v3980V38c1V30ca = ADD v397eV38c1V30ca(0x1), v397a_0V38c1V30ca
    0x3981S0x38c1S0x30ca: v3981V38c1V30ca(0x3971) = CONST 
    0x3984S0x38c1S0x30ca: JUMP v3981V38c1V30ca(0x3971)

    Begin block 0x45cfB0x38c1B0x30ca
    prev=[0x3971B0x38c1B0x30ca], succ=[0x38dfB0x30ca]
    =================================
    0x45d2S0x38c1S0x30ca: JUMP v38d6V30ca(0x38df)

    Begin block 0x38dfB0x30ca
    prev=[0x45cfB0x38c1B0x30ca], succ=[0x30d8]
    =================================
    0x38e1S0x30ca: JUMP v30cb(0x30d8)

    Begin block 0x30d8
    prev=[0x38dfB0x30ca], succ=[0x43c7]
    =================================
    0x30da: v30da(0x0) = CONST 
    0x30dc: v30dc(0x2) = CONST 
    0x30e1: v30e1 = ADD v30dc(0x2), v30bf
    0x30e4: SSTORE v30e1, v30da(0x0)
    0x30e7: MSTORE v30da(0x0), va68
    0x30e8: v30e8(0xa) = CONST 
    0x30ea: v30ea(0x20) = CONST 
    0x30ee: MSTORE v30ea(0x20), v30e8(0xa)
    0x30ef: v30ef(0x40) = CONST 
    0x30f3: v30f3 = SHA3 v30da(0x0), v30ef(0x40)
    0x30f6: SSTORE v30f3, v30da(0x0)
    0x30f7: v30f7(0x1) = CONST 
    0x30fb: v30fb = ADD v30f7(0x1), v30f3
    0x30fd: v30fd = SLOAD v30fb
    0x30fe: v30fe(0x1) = CONST 
    0x3100: v3100(0x1) = CONST 
    0x3102: v3102(0xa0) = CONST 
    0x3104: v3104(0x10000000000000000000000000000000000000000) = SHL v3102(0xa0), v3100(0x1)
    0x3105: v3105(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3104(0x10000000000000000000000000000000000000000), v30fe(0x1)
    0x3106: v3106(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3105(0xffffffffffffffffffffffffffffffffffffffff)
    0x3107: v3107 = AND v3106(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v30fd
    0x3109: SSTORE v30fb, v3107
    0x310b: v310b = MLOAD v30ef(0x40)
    0x310e: MSTORE v310b, va68
    0x3111: v3111 = ADD v310b, v30ea(0x20)
    0x3112: MSTORE v3111, v30f7(0x1)
    0x3114: v3114 = MLOAD v30ef(0x40)
    0x3115: v3115(0x1) = CONST 
    0x3117: v3117(0x1) = CONST 
    0x3119: v3119(0xa0) = CONST 
    0x311b: v311b(0x10000000000000000000000000000000000000000) = SHL v3119(0xa0), v3117(0x1)
    0x311c: v311c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v311b(0x10000000000000000000000000000000000000000), v3115(0x1)
    0x311e: v311e = AND va63, v311c(0xffffffffffffffffffffffffffffffffffffffff)
    0x3120: v3120 = CALLER 
    0x3122: v3122(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x3147: v3147(0x0) = SUB v310b, v3114
    0x3148: v3148(0x40) = ADD v3147(0x0), v30ef(0x40)
    0x314a: LOG4 v3114, v3148(0x40), v3122(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v3120, v311e, v30da(0x0)
    0x314d: JUMP v1f3f(0x43c7)

    Begin block 0x43c7
    prev=[0x30d8], succ=[0x4031]
    =================================
    0x43ca: JUMP va42(0x4031)

    Begin block 0x4031
    prev=[0x43c7], succ=[]
    =================================
    0x4032: STOP 

}

function setApprovalForAll(address,bool)() public {
    Begin block 0xa6d
    prev=[], succ=[0xa7f, 0xa83]
    =================================
    0xa6e: va6e(0x4052) = CONST 
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
    prev=[0xa6d], succ=[0x1f48]
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
    0xa97: va97(0x1f48) = CONST 
    0xa9a: JUMP va97(0x1f48)

    Begin block 0x1f48
    prev=[0xa83], succ=[0x1f5a, 0x1fa6]
    =================================
    0x1f49: v1f49 = CALLER 
    0x1f4a: v1f4a(0x1) = CONST 
    0x1f4c: v1f4c(0x1) = CONST 
    0x1f4e: v1f4e(0xa0) = CONST 
    0x1f50: v1f50(0x10000000000000000000000000000000000000000) = SHL v1f4e(0xa0), v1f4c(0x1)
    0x1f51: v1f51(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f50(0x10000000000000000000000000000000000000000), v1f4a(0x1)
    0x1f53: v1f53 = AND va8f, v1f51(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f54: v1f54 = EQ v1f53, v1f49
    0x1f55: v1f55 = ISZERO v1f54
    0x1f56: v1f56(0x1fa6) = CONST 
    0x1f59: JUMPI v1f56(0x1fa6), v1f55

    Begin block 0x1f5a
    prev=[0x1f48], succ=[]
    =================================
    0x1f5a: v1f5a(0x40) = CONST 
    0x1f5d: v1f5d = MLOAD v1f5a(0x40)
    0x1f5e: v1f5e(0x461bcd) = CONST 
    0x1f62: v1f62(0xe5) = CONST 
    0x1f64: v1f64(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f62(0xe5), v1f5e(0x461bcd)
    0x1f66: MSTORE v1f5d, v1f64(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f67: v1f67(0x20) = CONST 
    0x1f69: v1f69(0x4) = CONST 
    0x1f6c: v1f6c = ADD v1f5d, v1f69(0x4)
    0x1f6f: MSTORE v1f6c, v1f67(0x20)
    0x1f70: v1f70(0x24) = CONST 
    0x1f73: v1f73 = ADD v1f5d, v1f70(0x24)
    0x1f74: MSTORE v1f73, v1f67(0x20)
    0x1f75: v1f75(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66) = CONST 
    0x1f96: v1f96(0x44) = CONST 
    0x1f99: v1f99 = ADD v1f5d, v1f96(0x44)
    0x1f9a: MSTORE v1f99, v1f75(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66)
    0x1f9c: v1f9c = MLOAD v1f5a(0x40)
    0x1fa0: v1fa0(0x0) = SUB v1f5d, v1f9c
    0x1fa1: v1fa1(0x64) = CONST 
    0x1fa3: v1fa3(0x64) = ADD v1fa1(0x64), v1fa0(0x0)
    0x1fa5: REVERT v1f9c, v1fa3(0x64)

    Begin block 0x1fa6
    prev=[0x1f48], succ=[0x4052]
    =================================
    0x1fa7: v1fa7 = CALLER 
    0x1fa8: v1fa8(0x0) = CONST 
    0x1fac: MSTORE v1fa8(0x0), v1fa7
    0x1fad: v1fad(0x9) = CONST 
    0x1faf: v1faf(0x20) = CONST 
    0x1fb3: MSTORE v1faf(0x20), v1fad(0x9)
    0x1fb4: v1fb4(0x40) = CONST 
    0x1fb8: v1fb8 = SHA3 v1fa8(0x0), v1fb4(0x40)
    0x1fb9: v1fb9(0x1) = CONST 
    0x1fbb: v1fbb(0x1) = CONST 
    0x1fbd: v1fbd(0xa0) = CONST 
    0x1fbf: v1fbf(0x10000000000000000000000000000000000000000) = SHL v1fbd(0xa0), v1fbb(0x1)
    0x1fc0: v1fc0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fbf(0x10000000000000000000000000000000000000000), v1fb9(0x1)
    0x1fc2: v1fc2 = AND va8f, v1fc0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fc5: MSTORE v1fa8(0x0), v1fc2
    0x1fc8: MSTORE v1faf(0x20), v1fb8
    0x1fcc: v1fcc = SHA3 v1fa8(0x0), v1fb4(0x40)
    0x1fce: v1fce = SLOAD v1fcc
    0x1fcf: v1fcf(0xff) = CONST 
    0x1fd1: v1fd1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1fcf(0xff)
    0x1fd2: v1fd2 = AND v1fd1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1fce
    0x1fd4: v1fd4 = ISZERO va96
    0x1fd5: v1fd5 = ISZERO v1fd4
    0x1fd8: v1fd8 = OR v1fd5, v1fd2
    0x1fdb: SSTORE v1fcc, v1fd8
    0x1fdd: v1fdd = MLOAD v1fb4(0x40)
    0x1fe0: MSTORE v1fdd, v1fd5
    0x1fe2: v1fe2 = MLOAD v1fb4(0x40)
    0x1fe6: v1fe6(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31) = CONST 
    0x200b: v200b(0x0) = SUB v1fdd, v1fe2
    0x200e: v200e(0x20) = ADD v1faf(0x20), v200b(0x0)
    0x2010: LOG3 v1fe2, v200e(0x20), v1fe6(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31), v1fa7, v1fc2
    0x2013: JUMP va6e(0x4052)

    Begin block 0x4052
    prev=[0x1fa6], succ=[]
    =================================
    0x4053: STOP 

}

function mintSuper(address,uint256,uint256,address[],uint256[])() public {
    Begin block 0xa9b
    prev=[], succ=[0xaad, 0xab1]
    =================================
    0xa9c: va9c(0x4073) = CONST 
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
    prev=[0xb49], succ=[0x2014]
    =================================
    0xb71: vb71(0x2014) = CONST 
    0xb74: JUMP vb71(0x2014)

    Begin block 0x2014
    prev=[0xb6a], succ=[0x202c, 0x2069]
    =================================
    0x2015: v2015 = CALLER 
    0x2016: v2016(0x0) = CONST 
    0x201a: MSTORE v2016(0x0), v2015
    0x201b: v201b(0x5) = CONST 
    0x201d: v201d(0x20) = CONST 
    0x201f: MSTORE v201d(0x20), v201b(0x5)
    0x2020: v2020(0x40) = CONST 
    0x2023: v2023 = SHA3 v2016(0x0), v2020(0x40)
    0x2024: v2024 = SLOAD v2023
    0x2025: v2025(0xff) = CONST 
    0x2027: v2027 = AND v2025(0xff), v2024
    0x2028: v2028(0x2069) = CONST 
    0x202b: JUMPI v2028(0x2069), v2027

    Begin block 0x202c
    prev=[0x2014], succ=[]
    =================================
    0x202c: v202c(0x40) = CONST 
    0x202f: v202f = MLOAD v202c(0x40)
    0x2030: v2030(0x461bcd) = CONST 
    0x2034: v2034(0xe5) = CONST 
    0x2036: v2036(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2034(0xe5), v2030(0x461bcd)
    0x2038: MSTORE v202f, v2036(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2039: v2039(0x20) = CONST 
    0x203b: v203b(0x4) = CONST 
    0x203e: v203e = ADD v202f, v203b(0x4)
    0x203f: MSTORE v203e, v2039(0x20)
    0x2040: v2040(0xe) = CONST 
    0x2042: v2042(0x24) = CONST 
    0x2045: v2045 = ADD v202f, v2042(0x24)
    0x2046: MSTORE v2045, v2040(0xe)
    0x2047: v2047(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x2056: v2056(0x91) = CONST 
    0x2058: v2058(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v2056(0x91), v2047(0x36bab9ba1031329036b4b73a32b9)
    0x2059: v2059(0x44) = CONST 
    0x205c: v205c = ADD v202f, v2059(0x44)
    0x205d: MSTORE v205c, v2058(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x205f: v205f = MLOAD v202c(0x40)
    0x2063: v2063(0x0) = SUB v202f, v205f
    0x2064: v2064(0x64) = CONST 
    0x2066: v2066(0x64) = ADD v2064(0x64), v2063(0x0)
    0x2068: REVERT v205f, v2066(0x64)

    Begin block 0x2069
    prev=[0x2014], succ=[0x314eB0x2069]
    =================================
    0x206a: v206a(0x2078) = CONST 
    0x2074: v2074(0x314e) = CONST 
    0x2077: JUMP v2074(0x314e)

    Begin block 0x314eB0x2069
    prev=[0x2069], succ=[0x3156B0x2069, 0x318cB0x2069]
    =================================
    0x314fS0x2069: v314fV2069(0x0) = CONST 
    0x3152S0x2069: v3152V2069(0x318c) = CONST 
    0x3155S0x2069: JUMPI v3152V2069(0x318c), vafb

    Begin block 0x3156B0x2069
    prev=[0x314eB0x2069], succ=[]
    =================================
    0x3156S0x2069: v3156V2069(0x40) = CONST 
    0x3158S0x2069: v3158V2069 = MLOAD v3156V2069(0x40)
    0x3159S0x2069: v3159V2069(0x461bcd) = CONST 
    0x315dS0x2069: v315dV2069(0xe5) = CONST 
    0x315fS0x2069: v315fV2069(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v315dV2069(0xe5), v3159V2069(0x461bcd)
    0x3161S0x2069: MSTORE v3158V2069, v315fV2069(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3162S0x2069: v3162V2069(0x4) = CONST 
    0x3164S0x2069: v3164V2069 = ADD v3162V2069(0x4), v3158V2069
    0x3167S0x2069: v3167V2069(0x20) = CONST 
    0x3169S0x2069: v3169V2069 = ADD v3167V2069(0x20), v3164V2069
    0x316cS0x2069: v316cV2069(0x20) = SUB v3169V2069, v3164V2069
    0x316eS0x2069: MSTORE v3164V2069, v316cV2069(0x20)
    0x316fS0x2069: v316fV2069(0x24) = CONST 
    0x3172S0x2069: MSTORE v3169V2069, v316fV2069(0x24)
    0x3173S0x2069: v3173V2069(0x20) = CONST 
    0x3175S0x2069: v3175V2069 = ADD v3173V2069(0x20), v3169V2069
    0x3177S0x2069: v3177V2069(0x3a31) = CONST 
    0x317aS0x2069: v317aV2069(0x24) = CONST 
    0x317dS0x2069: CODECOPY v3175V2069, v3177V2069(0x3a31), v317aV2069(0x24)
    0x317eS0x2069: v317eV2069(0x40) = CONST 
    0x3180S0x2069: v3180V2069 = ADD v317eV2069(0x40), v3175V2069
    0x3184S0x2069: v3184V2069(0x40) = CONST 
    0x3186S0x2069: v3186V2069 = MLOAD v3184V2069(0x40)
    0x3189S0x2069: v3189V2069(0x84) = SUB v3180V2069, v3186V2069
    0x318bS0x2069: REVERT v3186V2069, v3189V2069(0x84)

    Begin block 0x318cB0x2069
    prev=[0x314eB0x2069], succ=[0x3194B0x2069, 0x31caB0x2069]
    =================================
    0x318fS0x2069: v318fV2069 = EQ vb4b, vafb
    0x3190S0x2069: v3190V2069(0x31ca) = CONST 
    0x3193S0x2069: JUMPI v3190V2069(0x31ca), v318fV2069

    Begin block 0x3194B0x2069
    prev=[0x318cB0x2069], succ=[]
    =================================
    0x3194S0x2069: v3194V2069(0x40) = CONST 
    0x3196S0x2069: v3196V2069 = MLOAD v3194V2069(0x40)
    0x3197S0x2069: v3197V2069(0x461bcd) = CONST 
    0x319bS0x2069: v319bV2069(0xe5) = CONST 
    0x319dS0x2069: v319dV2069(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v319bV2069(0xe5), v3197V2069(0x461bcd)
    0x319fS0x2069: MSTORE v3196V2069, v319dV2069(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x31a0S0x2069: v31a0V2069(0x4) = CONST 
    0x31a2S0x2069: v31a2V2069 = ADD v31a0V2069(0x4), v3196V2069
    0x31a5S0x2069: v31a5V2069(0x20) = CONST 
    0x31a7S0x2069: v31a7V2069 = ADD v31a5V2069(0x20), v31a2V2069
    0x31aaS0x2069: v31aaV2069(0x20) = SUB v31a7V2069, v31a2V2069
    0x31acS0x2069: MSTORE v31a2V2069, v31aaV2069(0x20)
    0x31adS0x2069: v31adV2069(0x2b) = CONST 
    0x31b0S0x2069: MSTORE v31a7V2069, v31adV2069(0x2b)
    0x31b1S0x2069: v31b1V2069(0x20) = CONST 
    0x31b3S0x2069: v31b3V2069 = ADD v31b1V2069(0x20), v31a7V2069
    0x31b5S0x2069: v31b5V2069(0x3a80) = CONST 
    0x31b8S0x2069: v31b8V2069(0x2b) = CONST 
    0x31bbS0x2069: CODECOPY v31b3V2069, v31b5V2069(0x3a80), v31b8V2069(0x2b)
    0x31bcS0x2069: v31bcV2069(0x40) = CONST 
    0x31beS0x2069: v31beV2069 = ADD v31bcV2069(0x40), v31b3V2069
    0x31c2S0x2069: v31c2V2069(0x40) = CONST 
    0x31c4S0x2069: v31c4V2069 = MLOAD v31c2V2069(0x40)
    0x31c7S0x2069: v31c7V2069(0x84) = SUB v31beV2069, v31c4V2069
    0x31c9S0x2069: REVERT v31c4V2069, v31c7V2069(0x84)

    Begin block 0x31caB0x2069
    prev=[0x318cB0x2069], succ=[0x31d6B0x2069]
    =================================
    0x31cbS0x2069: v31cbV2069(0x0) = CONST 
    0x31cdS0x2069: v31cdV2069(0x31d6) = CONST 
    0x31d2S0x2069: v31d2V2069(0x2af3) = CONST 
    0x31d5S0x2069: v31d5_0V2069 = CALLPRIVATE v31d2V2069(0x2af3), vac2, vabc, v31cdV2069(0x31d6)

    Begin block 0x31d6B0x2069
    prev=[0x31caB0x2069], succ=[0x38e2B0x31d6B0x2069]
    =================================
    0x31d7S0x2069: v31d7V2069(0x0) = CONST 
    0x31dbS0x2069: MSTORE v31d7V2069(0x0), v31d5_0V2069
    0x31dcS0x2069: v31dcV2069(0xc) = CONST 
    0x31deS0x2069: v31deV2069(0x20) = CONST 
    0x31e0S0x2069: MSTORE v31deV2069(0x20), v31dcV2069(0xc)
    0x31e1S0x2069: v31e1V2069(0x40) = CONST 
    0x31e4S0x2069: v31e4V2069 = SHA3 v31d7V2069(0x0), v31e1V2069(0x40)
    0x31e5S0x2069: v31e5V2069(0x2) = CONST 
    0x31e8S0x2069: v31e8V2069 = ADD v31e4V2069, v31e5V2069(0x2)
    0x31ebS0x2069: SSTORE v31e8V2069, vac8
    0x31efS0x2069: v31efV2069(0x31f9) = CONST 
    0x31f5S0x2069: v31f5V2069(0x38e2) = CONST 
    0x31f8S0x2069: JUMP v31f5V2069(0x38e2)

    Begin block 0x38e2B0x31d6B0x2069
    prev=[0x31d6B0x2069], succ=[0x38fcB0x31d6B0x2069, 0x38b10x38e2B0x31d6B0x2069]
    =================================
    0x38e5S0x31d6S0x2069: v38e5V31d6V2069 = SLOAD v31e4V2069
    0x38e8S0x31d6S0x2069: SSTORE v31e4V2069, vafb
    0x38eaS0x31d6S0x2069: v38eaV31d6V2069(0x0) = CONST 
    0x38ecS0x31d6S0x2069: MSTORE v38eaV31d6V2069(0x0), v31e4V2069
    0x38edS0x31d6S0x2069: v38edV31d6V2069(0x20) = CONST 
    0x38efS0x31d6S0x2069: v38efV31d6V2069(0x0) = CONST 
    0x38f1S0x31d6S0x2069: v38f1V31d6V2069 = SHA3 v38efV31d6V2069(0x0), v38edV31d6V2069(0x20)
    0x38f4S0x31d6S0x2069: v38f4V31d6V2069 = ADD v38f1V31d6V2069, v38e5V31d6V2069
    0x38f7S0x31d6S0x2069: v38f7V31d6V2069 = ISZERO vafb
    0x38f8S0x31d6S0x2069: v38f8V31d6V2069(0x38b1) = CONST 
    0x38fbS0x31d6S0x2069: JUMPI v38f8V31d6V2069(0x38b1), v38f7V31d6V2069

    Begin block 0x38fcB0x31d6B0x2069
    prev=[0x38e2B0x31d6B0x2069], succ=[0x3902B0x31d6B0x2069]
    =================================
    0x38fdS0x31d6S0x2069: v38fdV31d6V2069(0x20) = CONST 
    0x38ffS0x31d6S0x2069: v38ffV31d6V2069 = MUL v38fdV31d6V2069(0x20), vafb
    0x3901S0x31d6S0x2069: v3901V31d6V2069 = ADD vaff, v38ffV31d6V2069

    Begin block 0x3902B0x31d6B0x2069
    prev=[0x38fcB0x31d6B0x2069, 0x390bB0x31d6B0x2069], succ=[0x390bB0x31d6B0x2069, 0x38b10x38e2B0x31d6B0x2069]
    =================================
    0x3902_0x2S0x31d6S0x2069: v3902_2V31d6V2069 = PHI vaff, v3929V31d6V2069
    0x3905S0x31d6S0x2069: v3905V31d6V2069 = GT v3901V31d6V2069, v3902_2V31d6V2069
    0x3906S0x31d6S0x2069: v3906V31d6V2069 = ISZERO v3905V31d6V2069
    0x3907S0x31d6S0x2069: v3907V31d6V2069(0x38b1) = CONST 
    0x390aS0x31d6S0x2069: JUMPI v3907V31d6V2069(0x38b1), v3906V31d6V2069

    Begin block 0x390bB0x31d6B0x2069
    prev=[0x3902B0x31d6B0x2069], succ=[0x3902B0x31d6B0x2069]
    =================================
    0x390b_0x1S0x31d6S0x2069: v390b_1V31d6V2069 = PHI v38f1V31d6V2069, v392fV31d6V2069
    0x390b_0x2S0x31d6S0x2069: v390b_2V31d6V2069 = PHI vaff, v3929V31d6V2069
    0x390cS0x31d6S0x2069: v390cV31d6V2069 = SLOAD v390b_1V31d6V2069
    0x390dS0x31d6S0x2069: v390dV31d6V2069(0x1) = CONST 
    0x390fS0x31d6S0x2069: v390fV31d6V2069(0x1) = CONST 
    0x3911S0x31d6S0x2069: v3911V31d6V2069(0xa0) = CONST 
    0x3913S0x31d6S0x2069: v3913V31d6V2069(0x10000000000000000000000000000000000000000) = SHL v3911V31d6V2069(0xa0), v390fV31d6V2069(0x1)
    0x3914S0x31d6S0x2069: v3914V31d6V2069(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3913V31d6V2069(0x10000000000000000000000000000000000000000), v390dV31d6V2069(0x1)
    0x3915S0x31d6S0x2069: v3915V31d6V2069(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3914V31d6V2069(0xffffffffffffffffffffffffffffffffffffffff)
    0x3916S0x31d6S0x2069: v3916V31d6V2069 = AND v3915V31d6V2069(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v390cV31d6V2069
    0x3917S0x31d6S0x2069: v3917V31d6V2069(0x1) = CONST 
    0x3919S0x31d6S0x2069: v3919V31d6V2069(0x1) = CONST 
    0x391bS0x31d6S0x2069: v391bV31d6V2069(0xa0) = CONST 
    0x391dS0x31d6S0x2069: v391dV31d6V2069(0x10000000000000000000000000000000000000000) = SHL v391bV31d6V2069(0xa0), v3919V31d6V2069(0x1)
    0x391eS0x31d6S0x2069: v391eV31d6V2069(0xffffffffffffffffffffffffffffffffffffffff) = SUB v391dV31d6V2069(0x10000000000000000000000000000000000000000), v3917V31d6V2069(0x1)
    0x3920S0x31d6S0x2069: v3920V31d6V2069 = CALLDATALOAD v390b_2V31d6V2069
    0x3921S0x31d6S0x2069: v3921V31d6V2069 = AND v3920V31d6V2069, v391eV31d6V2069(0xffffffffffffffffffffffffffffffffffffffff)
    0x3922S0x31d6S0x2069: v3922V31d6V2069 = OR v3921V31d6V2069, v3916V31d6V2069
    0x3924S0x31d6S0x2069: SSTORE v390b_1V31d6V2069, v3922V31d6V2069
    0x3925S0x31d6S0x2069: v3925V31d6V2069(0x20) = CONST 
    0x3929S0x31d6S0x2069: v3929V31d6V2069 = ADD v390b_2V31d6V2069, v3925V31d6V2069(0x20)
    0x392bS0x31d6S0x2069: v392bV31d6V2069(0x1) = CONST 
    0x392fS0x31d6S0x2069: v392fV31d6V2069 = ADD v390b_1V31d6V2069, v392bV31d6V2069(0x1)
    0x3931S0x31d6S0x2069: v3931V31d6V2069(0x3902) = CONST 
    0x3934S0x31d6S0x2069: JUMP v3931V31d6V2069(0x3902)

    Begin block 0x38b10x38e2B0x31d6B0x2069
    prev=[0x38e2B0x31d6B0x2069, 0x3902B0x31d6B0x2069], succ=[0x3970B0x38b10x38e2B0x31d6B0x2069]
    =================================
    0x38b10x38e2_0x1S0x31d6S0x2069: v38b138e2_1V31d6V2069 = PHI v38f1V31d6V2069, v392fV31d6V2069
    0x38b30x38e2S0x31d6S0x2069: v38e238b3V31d6V2069(0x45ac) = CONST 
    0x38b90x38e2S0x31d6S0x2069: v38e238b9V31d6V2069(0x3970) = CONST 
    0x38bc0x38e2S0x31d6S0x2069: JUMP v38e238b9V31d6V2069(0x3970)

    Begin block 0x3970B0x38b10x38e2B0x31d6B0x2069
    prev=[0x38b10x38e2B0x31d6B0x2069], succ=[0x3971B0x38b10x38e2B0x31d6B0x2069]
    =================================

    Begin block 0x3971B0x38b10x38e2B0x31d6B0x2069
    prev=[0x397aB0x38b10x38e2B0x31d6B0x2069, 0x3970B0x38b10x38e2B0x31d6B0x2069], succ=[0x397aB0x38b10x38e2B0x31d6B0x2069, 0x45cfB0x38b10x38e2B0x31d6B0x2069]
    =================================
    0x3971_0x0S0x38b10x38e2S0x31d6S0x2069: v3971_0V38b138e2V31d6V2069 = PHI v38b138e2_1V31d6V2069, v3980V38b138e2V31d6V2069
    0x3974S0x38b10x38e2S0x31d6S0x2069: v3974V38b138e2V31d6V2069 = GT v38f4V31d6V2069, v3971_0V38b138e2V31d6V2069
    0x3975S0x38b10x38e2S0x31d6S0x2069: v3975V38b138e2V31d6V2069 = ISZERO v3974V38b138e2V31d6V2069
    0x3976S0x38b10x38e2S0x31d6S0x2069: v3976V38b138e2V31d6V2069(0x45cf) = CONST 
    0x3979S0x38b10x38e2S0x31d6S0x2069: JUMPI v3976V38b138e2V31d6V2069(0x45cf), v3975V38b138e2V31d6V2069

    Begin block 0x397aB0x38b10x38e2B0x31d6B0x2069
    prev=[0x3971B0x38b10x38e2B0x31d6B0x2069], succ=[0x3971B0x38b10x38e2B0x31d6B0x2069]
    =================================
    0x397aS0x38b10x38e2S0x31d6S0x2069: v397aV38b138e2V31d6V2069(0x0) = CONST 
    0x397a_0x0S0x38b10x38e2S0x31d6S0x2069: v397a_0V38b138e2V31d6V2069 = PHI v38b138e2_1V31d6V2069, v3980V38b138e2V31d6V2069
    0x397dS0x38b10x38e2S0x31d6S0x2069: SSTORE v397a_0V38b138e2V31d6V2069, v397aV38b138e2V31d6V2069(0x0)
    0x397eS0x38b10x38e2S0x31d6S0x2069: v397eV38b138e2V31d6V2069(0x1) = CONST 
    0x3980S0x38b10x38e2S0x31d6S0x2069: v3980V38b138e2V31d6V2069 = ADD v397eV38b138e2V31d6V2069(0x1), v397a_0V38b138e2V31d6V2069
    0x3981S0x38b10x38e2S0x31d6S0x2069: v3981V38b138e2V31d6V2069(0x3971) = CONST 
    0x3984S0x38b10x38e2S0x31d6S0x2069: JUMP v3981V38b138e2V31d6V2069(0x3971)

    Begin block 0x45cfB0x38b10x38e2B0x31d6B0x2069
    prev=[0x3971B0x38b10x38e2B0x31d6B0x2069], succ=[0x45ac0x38e2B0x31d6B0x2069]
    =================================
    0x45d2S0x38b10x38e2S0x31d6S0x2069: JUMP v38e238b3V31d6V2069(0x45ac)

    Begin block 0x45ac0x38e2B0x31d6B0x2069
    prev=[0x45cfB0x38b10x38e2B0x31d6B0x2069], succ=[0x31f9B0x2069]
    =================================
    0x45af0x38e2S0x31d6S0x2069: JUMP v31efV2069(0x31f9)

    Begin block 0x31f9B0x2069
    prev=[0x45ac0x38e2B0x31d6B0x2069], succ=[0x3935B0x31f9B0x2069]
    =================================
    0x31fbS0x2069: v31fbV2069(0x0) = CONST 
    0x31ffS0x2069: MSTORE v31fbV2069(0x0), v31d5_0V2069
    0x3200S0x2069: v3200V2069(0xc) = CONST 
    0x3202S0x2069: v3202V2069(0x20) = CONST 
    0x3204S0x2069: MSTORE v3202V2069(0x20), v3200V2069(0xc)
    0x3205S0x2069: v3205V2069(0x40) = CONST 
    0x3208S0x2069: v3208V2069 = SHA3 v31fbV2069(0x0), v3205V2069(0x40)
    0x3209S0x2069: v3209V2069(0x3216) = CONST 
    0x320dS0x2069: v320dV2069(0x1) = CONST 
    0x320fS0x2069: v320fV2069 = ADD v320dV2069(0x1), v3208V2069
    0x3212S0x2069: v3212V2069(0x3935) = CONST 
    0x3215S0x2069: JUMP v3212V2069(0x3935)

    Begin block 0x3935B0x31f9B0x2069
    prev=[0x31f9B0x2069], succ=[0x394fB0x31f9B0x2069, 0x38b10x3935B0x31f9B0x2069]
    =================================
    0x3938S0x31f9S0x2069: v3938V31f9V2069 = SLOAD v320fV2069
    0x393bS0x31f9S0x2069: SSTORE v320fV2069, vb4b
    0x393dS0x31f9S0x2069: v393dV31f9V2069(0x0) = CONST 
    0x393fS0x31f9S0x2069: MSTORE v393dV31f9V2069(0x0), v320fV2069
    0x3940S0x31f9S0x2069: v3940V31f9V2069(0x20) = CONST 
    0x3942S0x31f9S0x2069: v3942V31f9V2069(0x0) = CONST 
    0x3944S0x31f9S0x2069: v3944V31f9V2069 = SHA3 v3942V31f9V2069(0x0), v3940V31f9V2069(0x20)
    0x3947S0x31f9S0x2069: v3947V31f9V2069 = ADD v3944V31f9V2069, v3938V31f9V2069
    0x394aS0x31f9S0x2069: v394aV31f9V2069 = ISZERO vb4b
    0x394bS0x31f9S0x2069: v394bV31f9V2069(0x38b1) = CONST 
    0x394eS0x31f9S0x2069: JUMPI v394bV31f9V2069(0x38b1), v394aV31f9V2069

    Begin block 0x394fB0x31f9B0x2069
    prev=[0x3935B0x31f9B0x2069], succ=[0x3955B0x31f9B0x2069]
    =================================
    0x3950S0x31f9S0x2069: v3950V31f9V2069(0x20) = CONST 
    0x3952S0x31f9S0x2069: v3952V31f9V2069 = MUL v3950V31f9V2069(0x20), vb4b
    0x3954S0x31f9S0x2069: v3954V31f9V2069 = ADD vb4f, v3952V31f9V2069

    Begin block 0x3955B0x31f9B0x2069
    prev=[0x394fB0x31f9B0x2069, 0x395eB0x31f9B0x2069], succ=[0x395eB0x31f9B0x2069, 0x38b10x3935B0x31f9B0x2069]
    =================================
    0x3955_0x2S0x31f9S0x2069: v3955_2V31f9V2069 = PHI vb4f, v3965V31f9V2069
    0x3958S0x31f9S0x2069: v3958V31f9V2069 = GT v3954V31f9V2069, v3955_2V31f9V2069
    0x3959S0x31f9S0x2069: v3959V31f9V2069 = ISZERO v3958V31f9V2069
    0x395aS0x31f9S0x2069: v395aV31f9V2069(0x38b1) = CONST 
    0x395dS0x31f9S0x2069: JUMPI v395aV31f9V2069(0x38b1), v3959V31f9V2069

    Begin block 0x395eB0x31f9B0x2069
    prev=[0x3955B0x31f9B0x2069], succ=[0x3955B0x31f9B0x2069]
    =================================
    0x395e_0x1S0x31f9S0x2069: v395e_1V31f9V2069 = PHI v3944V31f9V2069, v396aV31f9V2069
    0x395e_0x2S0x31f9S0x2069: v395e_2V31f9V2069 = PHI vb4f, v3965V31f9V2069
    0x395fS0x31f9S0x2069: v395fV31f9V2069 = CALLDATALOAD v395e_2V31f9V2069
    0x3961S0x31f9S0x2069: SSTORE v395e_1V31f9V2069, v395fV31f9V2069
    0x3963S0x31f9S0x2069: v3963V31f9V2069(0x20) = CONST 
    0x3965S0x31f9S0x2069: v3965V31f9V2069 = ADD v3963V31f9V2069(0x20), v395e_2V31f9V2069
    0x3968S0x31f9S0x2069: v3968V31f9V2069(0x1) = CONST 
    0x396aS0x31f9S0x2069: v396aV31f9V2069 = ADD v3968V31f9V2069(0x1), v395e_1V31f9V2069
    0x396cS0x31f9S0x2069: v396cV31f9V2069(0x3955) = CONST 
    0x396fS0x31f9S0x2069: JUMP v396cV31f9V2069(0x3955)

    Begin block 0x38b10x3935B0x31f9B0x2069
    prev=[0x3935B0x31f9B0x2069, 0x3955B0x31f9B0x2069], succ=[0x3970B0x38b10x3935B0x31f9B0x2069]
    =================================
    0x38b10x3935_0x1S0x31f9S0x2069: v38b13935_1V31f9V2069 = PHI v3944V31f9V2069, v396aV31f9V2069
    0x38b30x3935S0x31f9S0x2069: v393538b3V31f9V2069(0x45ac) = CONST 
    0x38b90x3935S0x31f9S0x2069: v393538b9V31f9V2069(0x3970) = CONST 
    0x38bc0x3935S0x31f9S0x2069: JUMP v393538b9V31f9V2069(0x3970)

    Begin block 0x3970B0x38b10x3935B0x31f9B0x2069
    prev=[0x38b10x3935B0x31f9B0x2069], succ=[0x3971B0x38b10x3935B0x31f9B0x2069]
    =================================

    Begin block 0x3971B0x38b10x3935B0x31f9B0x2069
    prev=[0x397aB0x38b10x3935B0x31f9B0x2069, 0x3970B0x38b10x3935B0x31f9B0x2069], succ=[0x397aB0x38b10x3935B0x31f9B0x2069, 0x45cfB0x38b10x3935B0x31f9B0x2069]
    =================================
    0x3971_0x0S0x38b10x3935S0x31f9S0x2069: v3971_0V38b13935V31f9V2069 = PHI v38b13935_1V31f9V2069, v3980V38b13935V31f9V2069
    0x3974S0x38b10x3935S0x31f9S0x2069: v3974V38b13935V31f9V2069 = GT v3947V31f9V2069, v3971_0V38b13935V31f9V2069
    0x3975S0x38b10x3935S0x31f9S0x2069: v3975V38b13935V31f9V2069 = ISZERO v3974V38b13935V31f9V2069
    0x3976S0x38b10x3935S0x31f9S0x2069: v3976V38b13935V31f9V2069(0x45cf) = CONST 
    0x3979S0x38b10x3935S0x31f9S0x2069: JUMPI v3976V38b13935V31f9V2069(0x45cf), v3975V38b13935V31f9V2069

    Begin block 0x397aB0x38b10x3935B0x31f9B0x2069
    prev=[0x3971B0x38b10x3935B0x31f9B0x2069], succ=[0x3971B0x38b10x3935B0x31f9B0x2069]
    =================================
    0x397aS0x38b10x3935S0x31f9S0x2069: v397aV38b13935V31f9V2069(0x0) = CONST 
    0x397a_0x0S0x38b10x3935S0x31f9S0x2069: v397a_0V38b13935V31f9V2069 = PHI v38b13935_1V31f9V2069, v3980V38b13935V31f9V2069
    0x397dS0x38b10x3935S0x31f9S0x2069: SSTORE v397a_0V38b13935V31f9V2069, v397aV38b13935V31f9V2069(0x0)
    0x397eS0x38b10x3935S0x31f9S0x2069: v397eV38b13935V31f9V2069(0x1) = CONST 
    0x3980S0x38b10x3935S0x31f9S0x2069: v3980V38b13935V31f9V2069 = ADD v397eV38b13935V31f9V2069(0x1), v397a_0V38b13935V31f9V2069
    0x3981S0x38b10x3935S0x31f9S0x2069: v3981V38b13935V31f9V2069(0x3971) = CONST 
    0x3984S0x38b10x3935S0x31f9S0x2069: JUMP v3981V38b13935V31f9V2069(0x3971)

    Begin block 0x45cfB0x38b10x3935B0x31f9B0x2069
    prev=[0x3971B0x38b10x3935B0x31f9B0x2069], succ=[0x45ac0x3935B0x31f9B0x2069]
    =================================
    0x45d2S0x38b10x3935S0x31f9S0x2069: JUMP v393538b3V31f9V2069(0x45ac)

    Begin block 0x45ac0x3935B0x31f9B0x2069
    prev=[0x45cfB0x38b10x3935B0x31f9B0x2069], succ=[0x3216B0x2069]
    =================================
    0x45af0x3935S0x31f9S0x2069: JUMP v3209V2069(0x3216)

    Begin block 0x3216B0x2069
    prev=[0x45ac0x3935B0x31f9B0x2069], succ=[0x2078]
    =================================
    0x3222S0x2069: JUMP v206a(0x2078)

    Begin block 0x2078
    prev=[0x3216B0x2069], succ=[0x4073]
    =================================
    0x2083: JUMP va9c(0x4073)

    Begin block 0x4073
    prev=[0x2078], succ=[]
    =================================
    0x4074: v4074(0x40) = CONST 
    0x4077: v4077 = MLOAD v4074(0x40)
    0x407a: MSTORE v4077, v31d5_0V2069
    0x407b: v407b = MLOAD v4074(0x40)
    0x407f: v407f(0x0) = SUB v4077, v407b
    0x4080: v4080(0x20) = CONST 
    0x4082: v4082(0x20) = ADD v4080(0x20), v407f(0x0)
    0x4084: RETURN v407b, v4082(0x20)

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
    prev=[0xb75], succ=[0x2084]
    =================================
    0xb8d: vb8d = CALLDATALOAD vb79(0x4)
    0xb8e: vb8e(0x2084) = CONST 
    0xb91: JUMP vb8e(0x2084)

    Begin block 0x2084
    prev=[0xb8b], succ=[0xb92]
    =================================
    0x2085: v2085(0x0) = CONST 
    0x2089: MSTORE v2085(0x0), vb8d
    0x208a: v208a(0xa) = CONST 
    0x208c: v208c(0x20) = CONST 
    0x2090: MSTORE v208c(0x20), v208a(0xa)
    0x2091: v2091(0x40) = CONST 
    0x2095: v2095 = SHA3 v2085(0x0), v2091(0x40)
    0x2096: v2096 = SLOAD v2095
    0x2097: v2097(0xb) = CONST 
    0x209b: MSTORE v208c(0x20), v2097(0xb)
    0x209e: v209e = SHA3 v2085(0x0), v2091(0x40)
    0x20a0: v20a0 = SLOAD v209e
    0x20a1: v20a1(0x1) = CONST 
    0x20a4: v20a4 = ADD v209e, v20a1(0x1)
    0x20a5: v20a5 = SLOAD v20a4
    0x20a6: v20a6(0x2) = CONST 
    0x20aa: v20aa = ADD v209e, v20a6(0x2)
    0x20ab: v20ab = SLOAD v20aa
    0x20ac: v20ac(0x1) = CONST 
    0x20ae: v20ae(0x1) = CONST 
    0x20b0: v20b0(0x80) = CONST 
    0x20b2: v20b2(0x100000000000000000000000000000000) = SHL v20b0(0x80), v20ae(0x1)
    0x20b3: v20b3(0xffffffffffffffffffffffffffffffff) = SUB v20b2(0x100000000000000000000000000000000), v20ac(0x1)
    0x20b6: v20b6 = AND v2096, v20b3(0xffffffffffffffffffffffffffffffff)
    0x20b8: v20b8(0x1) = CONST 
    0x20ba: v20ba(0x1) = CONST 
    0x20bc: v20bc(0xa0) = CONST 
    0x20be: v20be(0x10000000000000000000000000000000000000000) = SHL v20bc(0xa0), v20ba(0x1)
    0x20bf: v20bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20be(0x10000000000000000000000000000000000000000), v20b8(0x1)
    0x20c2: v20c2 = AND v20a0, v20bf(0xffffffffffffffffffffffffffffffffffffffff)
    0x20c5: JUMP vb76(0xb92)

    Begin block 0xb92
    prev=[0x2084], succ=[]
    =================================
    0xb93: vb93(0x40) = CONST 
    0xb96: vb96 = MLOAD vb93(0x40)
    0xb97: vb97(0x1) = CONST 
    0xb99: vb99(0x1) = CONST 
    0xb9b: vb9b(0x80) = CONST 
    0xb9d: vb9d(0x100000000000000000000000000000000) = SHL vb9b(0x80), vb99(0x1)
    0xb9e: vb9e(0xffffffffffffffffffffffffffffffff) = SUB vb9d(0x100000000000000000000000000000000), vb97(0x1)
    0xba1: vba1 = AND v20b6, vb9e(0xffffffffffffffffffffffffffffffff)
    0xba3: MSTORE vb96, vba1
    0xba4: vba4(0x1) = CONST 
    0xba6: vba6(0x1) = CONST 
    0xba8: vba8(0xa0) = CONST 
    0xbaa: vbaa(0x10000000000000000000000000000000000000000) = SHL vba8(0xa0), vba6(0x1)
    0xbab: vbab(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbaa(0x10000000000000000000000000000000000000000), vba4(0x1)
    0xbae: vbae = AND v20c2, vbab(0xffffffffffffffffffffffffffffffffffffffff)
    0xbaf: vbaf(0x20) = CONST 
    0xbb2: vbb2 = ADD vb96, vbaf(0x20)
    0xbb3: MSTORE vbb2, vbae
    0xbb6: vbb6 = ADD vb93(0x40), vb96
    0xbba: MSTORE vbb6, v20a5
    0xbbb: vbbb(0x60) = CONST 
    0xbbe: vbbe = ADD vb96, vbbb(0x60)
    0xbbf: MSTORE vbbe, v20ab
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
    0xbcb: vbcb(0x40a4) = CONST 
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
    prev=[0xbca], succ=[0x20c6]
    =================================
    0xbe2: vbe2 = CALLDATALOAD vbce(0x4)
    0xbe3: vbe3(0x1) = CONST 
    0xbe5: vbe5(0x1) = CONST 
    0xbe7: vbe7(0xa0) = CONST 
    0xbe9: vbe9(0x10000000000000000000000000000000000000000) = SHL vbe7(0xa0), vbe5(0x1)
    0xbea: vbea(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbe9(0x10000000000000000000000000000000000000000), vbe3(0x1)
    0xbeb: vbeb = AND vbea(0xffffffffffffffffffffffffffffffffffffffff), vbe2
    0xbec: vbec(0x20c6) = CONST 
    0xbef: JUMP vbec(0x20c6)

    Begin block 0x20c6
    prev=[0xbe0], succ=[0x40a4]
    =================================
    0x20c7: v20c7(0x1) = CONST 
    0x20c9: v20c9(0x1) = CONST 
    0x20cb: v20cb(0xa0) = CONST 
    0x20cd: v20cd(0x10000000000000000000000000000000000000000) = SHL v20cb(0xa0), v20c9(0x1)
    0x20ce: v20ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20cd(0x10000000000000000000000000000000000000000), v20c7(0x1)
    0x20cf: v20cf = AND v20ce(0xffffffffffffffffffffffffffffffffffffffff), vbeb
    0x20d0: v20d0(0x0) = CONST 
    0x20d4: MSTORE v20d0(0x0), v20cf
    0x20d5: v20d5(0x5) = CONST 
    0x20d7: v20d7(0x20) = CONST 
    0x20d9: MSTORE v20d7(0x20), v20d5(0x5)
    0x20da: v20da(0x40) = CONST 
    0x20dd: v20dd = SHA3 v20d0(0x0), v20da(0x40)
    0x20de: v20de = SLOAD v20dd
    0x20df: v20df(0xff) = CONST 
    0x20e1: v20e1 = AND v20df(0xff), v20de
    0x20e3: JUMP vbcb(0x40a4)

    Begin block 0x40a4
    prev=[0x20c6], succ=[]
    =================================
    0x40a5: v40a5(0x40) = CONST 
    0x40a8: v40a8 = MLOAD v40a5(0x40)
    0x40aa: v40aa = ISZERO v20e1
    0x40ab: v40ab = ISZERO v40aa
    0x40ad: MSTORE v40a8, v40ab
    0x40ae: v40ae = MLOAD v40a5(0x40)
    0x40b2: v40b2(0x0) = SUB v40a8, v40ae
    0x40b3: v40b3(0x20) = CONST 
    0x40b5: v40b5(0x20) = ADD v40b3(0x20), v40b2(0x0)
    0x40b7: RETURN v40ae, v40b5(0x20)

}

function transferGalaxyCommunity(address)() public {
    Begin block 0xbf0
    prev=[], succ=[0xc02, 0xc06]
    =================================
    0xbf1: vbf1(0x40d7) = CONST 
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
    prev=[0xbf0], succ=[0x20e4]
    =================================
    0xc08: vc08 = CALLDATALOAD vbf4(0x4)
    0xc09: vc09(0x1) = CONST 
    0xc0b: vc0b(0x1) = CONST 
    0xc0d: vc0d(0xa0) = CONST 
    0xc0f: vc0f(0x10000000000000000000000000000000000000000) = SHL vc0d(0xa0), vc0b(0x1)
    0xc10: vc10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc0f(0x10000000000000000000000000000000000000000), vc09(0x1)
    0xc11: vc11 = AND vc10(0xffffffffffffffffffffffffffffffffffffffff), vc08
    0xc12: vc12(0x20e4) = CONST 
    0xc15: JUMP vc12(0x20e4)

    Begin block 0x20e4
    prev=[0xc06], succ=[0x20f7, 0x213e]
    =================================
    0x20e5: v20e5(0x4) = CONST 
    0x20e7: v20e7 = SLOAD v20e5(0x4)
    0x20e8: v20e8(0x1) = CONST 
    0x20ea: v20ea(0x1) = CONST 
    0x20ec: v20ec(0xa0) = CONST 
    0x20ee: v20ee(0x10000000000000000000000000000000000000000) = SHL v20ec(0xa0), v20ea(0x1)
    0x20ef: v20ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20ee(0x10000000000000000000000000000000000000000), v20e8(0x1)
    0x20f0: v20f0 = AND v20ef(0xffffffffffffffffffffffffffffffffffffffff), v20e7
    0x20f1: v20f1 = CALLER 
    0x20f2: v20f2 = EQ v20f1, v20f0
    0x20f3: v20f3(0x213e) = CONST 
    0x20f6: JUMPI v20f3(0x213e), v20f2

    Begin block 0x20f7
    prev=[0x20e4], succ=[]
    =================================
    0x20f7: v20f7(0x40) = CONST 
    0x20fa: v20fa = MLOAD v20f7(0x40)
    0x20fb: v20fb(0x461bcd) = CONST 
    0x20ff: v20ff(0xe5) = CONST 
    0x2101: v2101(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v20ff(0xe5), v20fb(0x461bcd)
    0x2103: MSTORE v20fa, v2101(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2104: v2104(0x20) = CONST 
    0x2106: v2106(0x4) = CONST 
    0x2109: v2109 = ADD v20fa, v2106(0x4)
    0x210a: MSTORE v2109, v2104(0x20)
    0x210b: v210b(0x18) = CONST 
    0x210d: v210d(0x24) = CONST 
    0x2110: v2110 = ADD v20fa, v210d(0x24)
    0x2111: MSTORE v2110, v210b(0x18)
    0x2112: v2112(0x6d7573742062652067616c61787920636f6d6d756e697479) = CONST 
    0x212b: v212b(0x40) = CONST 
    0x212d: v212d(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000) = SHL v212b(0x40), v2112(0x6d7573742062652067616c61787920636f6d6d756e697479)
    0x212e: v212e(0x44) = CONST 
    0x2131: v2131 = ADD v20fa, v212e(0x44)
    0x2132: MSTORE v2131, v212d(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000)
    0x2134: v2134 = MLOAD v20f7(0x40)
    0x2138: v2138(0x0) = SUB v20fa, v2134
    0x2139: v2139(0x64) = CONST 
    0x213b: v213b(0x64) = ADD v2139(0x64), v2138(0x0)
    0x213d: REVERT v2134, v213b(0x64)

    Begin block 0x213e
    prev=[0x20e4], succ=[0x214d, 0x2183]
    =================================
    0x213f: v213f(0x1) = CONST 
    0x2141: v2141(0x1) = CONST 
    0x2143: v2143(0xa0) = CONST 
    0x2145: v2145(0x10000000000000000000000000000000000000000) = SHL v2143(0xa0), v2141(0x1)
    0x2146: v2146(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2145(0x10000000000000000000000000000000000000000), v213f(0x1)
    0x2148: v2148 = AND vc11, v2146(0xffffffffffffffffffffffffffffffffffffffff)
    0x2149: v2149(0x2183) = CONST 
    0x214c: JUMPI v2149(0x2183), v2148

    Begin block 0x214d
    prev=[0x213e], succ=[]
    =================================
    0x214d: v214d(0x40) = CONST 
    0x214f: v214f = MLOAD v214d(0x40)
    0x2150: v2150(0x461bcd) = CONST 
    0x2154: v2154(0xe5) = CONST 
    0x2156: v2156(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2154(0xe5), v2150(0x461bcd)
    0x2158: MSTORE v214f, v2156(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2159: v2159(0x4) = CONST 
    0x215b: v215b = ADD v2159(0x4), v214f
    0x215e: v215e(0x20) = CONST 
    0x2160: v2160 = ADD v215e(0x20), v215b
    0x2163: v2163(0x20) = SUB v2160, v215b
    0x2165: MSTORE v215b, v2163(0x20)
    0x2166: v2166(0x2b) = CONST 
    0x2169: MSTORE v2160, v2166(0x2b)
    0x216a: v216a(0x20) = CONST 
    0x216c: v216c = ADD v216a(0x20), v2160
    0x216e: v216e(0x3aab) = CONST 
    0x2171: v2171(0x2b) = CONST 
    0x2174: CODECOPY v216c, v216e(0x3aab), v2171(0x2b)
    0x2175: v2175(0x40) = CONST 
    0x2177: v2177 = ADD v2175(0x40), v216c
    0x217b: v217b(0x40) = CONST 
    0x217d: v217d = MLOAD v217b(0x40)
    0x2180: v2180(0x84) = SUB v2177, v217d
    0x2182: REVERT v217d, v2180(0x84)

    Begin block 0x2183
    prev=[0x213e], succ=[0x40d7]
    =================================
    0x2184: v2184(0x4) = CONST 
    0x2187: v2187 = SLOAD v2184(0x4)
    0x2188: v2188(0x1) = CONST 
    0x218a: v218a(0x1) = CONST 
    0x218c: v218c(0xa0) = CONST 
    0x218e: v218e(0x10000000000000000000000000000000000000000) = SHL v218c(0xa0), v218a(0x1)
    0x218f: v218f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v218e(0x10000000000000000000000000000000000000000), v2188(0x1)
    0x2190: v2190(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v218f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2191: v2191 = AND v2190(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2187
    0x2192: v2192(0x1) = CONST 
    0x2194: v2194(0x1) = CONST 
    0x2196: v2196(0xa0) = CONST 
    0x2198: v2198(0x10000000000000000000000000000000000000000) = SHL v2196(0xa0), v2194(0x1)
    0x2199: v2199(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2198(0x10000000000000000000000000000000000000000), v2192(0x1)
    0x219c: v219c = AND v2199(0xffffffffffffffffffffffffffffffffffffffff), vc11
    0x219f: v219f = OR v219c, v2191
    0x21a3: SSTORE v2184(0x4), v219f
    0x21a4: v21a4(0x40) = CONST 
    0x21a6: v21a6 = MLOAD v21a4(0x40)
    0x21a9: v21a9 = AND v219f, v2199(0xffffffffffffffffffffffffffffffffffffffff)
    0x21ab: v21ab(0x3953a794c970ca1d8613b88541e5759f5a1dc2b77fe412e1edc27a03e5657d11) = CONST 
    0x21cd: v21cd(0x0) = CONST 
    0x21d0: LOG3 v21a6, v21cd(0x0), v21ab(0x3953a794c970ca1d8613b88541e5759f5a1dc2b77fe412e1edc27a03e5657d11), v21a9, v219c
    0x21d2: JUMP vbf1(0x40d7)

    Begin block 0x40d7
    prev=[0x2183], succ=[]
    =================================
    0x40d8: STOP 

}

function removeOperator(address)() public {
    Begin block 0xc16
    prev=[], succ=[0xc28, 0xc2c]
    =================================
    0xc17: vc17(0x40f8) = CONST 
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
    prev=[0xc16], succ=[0x21d3]
    =================================
    0xc2e: vc2e = CALLDATALOAD vc1a(0x4)
    0xc2f: vc2f(0x1) = CONST 
    0xc31: vc31(0x1) = CONST 
    0xc33: vc33(0xa0) = CONST 
    0xc35: vc35(0x10000000000000000000000000000000000000000) = SHL vc33(0xa0), vc31(0x1)
    0xc36: vc36(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc35(0x10000000000000000000000000000000000000000), vc2f(0x1)
    0xc37: vc37 = AND vc36(0xffffffffffffffffffffffffffffffffffffffff), vc2e
    0xc38: vc38(0x21d3) = CONST 
    0xc3b: JUMP vc38(0x21d3)

    Begin block 0x21d3
    prev=[0xc2c], succ=[0x21e6, 0x2222]
    =================================
    0x21d4: v21d4(0x3) = CONST 
    0x21d6: v21d6 = SLOAD v21d4(0x3)
    0x21d7: v21d7(0x1) = CONST 
    0x21d9: v21d9(0x1) = CONST 
    0x21db: v21db(0xa0) = CONST 
    0x21dd: v21dd(0x10000000000000000000000000000000000000000) = SHL v21db(0xa0), v21d9(0x1)
    0x21de: v21de(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21dd(0x10000000000000000000000000000000000000000), v21d7(0x1)
    0x21df: v21df = AND v21de(0xffffffffffffffffffffffffffffffffffffffff), v21d6
    0x21e0: v21e0 = CALLER 
    0x21e1: v21e1 = EQ v21e0, v21df
    0x21e2: v21e2(0x2222) = CONST 
    0x21e5: JUMPI v21e2(0x2222), v21e1

    Begin block 0x21e6
    prev=[0x21d3], succ=[]
    =================================
    0x21e6: v21e6(0x40) = CONST 
    0x21e9: v21e9 = MLOAD v21e6(0x40)
    0x21ea: v21ea(0x461bcd) = CONST 
    0x21ee: v21ee(0xe5) = CONST 
    0x21f0: v21f0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v21ee(0xe5), v21ea(0x461bcd)
    0x21f2: MSTORE v21e9, v21f0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21f3: v21f3(0x20) = CONST 
    0x21f5: v21f5(0x4) = CONST 
    0x21f8: v21f8 = ADD v21e9, v21f5(0x4)
    0x21f9: MSTORE v21f8, v21f3(0x20)
    0x21fa: v21fa(0xd) = CONST 
    0x21fc: v21fc(0x24) = CONST 
    0x21ff: v21ff = ADD v21e9, v21fc(0x24)
    0x2200: MSTORE v21ff, v21fa(0xd)
    0x2201: v2201(0x26bab9ba1031329037bbb732b9) = CONST 
    0x220f: v220f(0x99) = CONST 
    0x2211: v2211(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v220f(0x99), v2201(0x26bab9ba1031329037bbb732b9)
    0x2212: v2212(0x44) = CONST 
    0x2215: v2215 = ADD v21e9, v2212(0x44)
    0x2216: MSTORE v2215, v2211(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x2218: v2218 = MLOAD v21e6(0x40)
    0x221c: v221c(0x0) = SUB v21e9, v2218
    0x221d: v221d(0x64) = CONST 
    0x221f: v221f(0x64) = ADD v221d(0x64), v221c(0x0)
    0x2221: REVERT v2218, v221f(0x64)

    Begin block 0x2222
    prev=[0x21d3], succ=[0x2243, 0x228f]
    =================================
    0x2223: v2223(0x1) = CONST 
    0x2225: v2225(0x1) = CONST 
    0x2227: v2227(0xa0) = CONST 
    0x2229: v2229(0x10000000000000000000000000000000000000000) = SHL v2227(0xa0), v2225(0x1)
    0x222a: v222a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2229(0x10000000000000000000000000000000000000000), v2223(0x1)
    0x222c: v222c = AND vc37, v222a(0xffffffffffffffffffffffffffffffffffffffff)
    0x222d: v222d(0x0) = CONST 
    0x2231: MSTORE v222d(0x0), v222c
    0x2232: v2232(0x6) = CONST 
    0x2234: v2234(0x20) = CONST 
    0x2236: MSTORE v2234(0x20), v2232(0x6)
    0x2237: v2237(0x40) = CONST 
    0x223a: v223a = SHA3 v222d(0x0), v2237(0x40)
    0x223b: v223b = SLOAD v223a
    0x223c: v223c(0xff) = CONST 
    0x223e: v223e = AND v223c(0xff), v223b
    0x223f: v223f(0x228f) = CONST 
    0x2242: JUMPI v223f(0x228f), v223e

    Begin block 0x2243
    prev=[0x2222], succ=[]
    =================================
    0x2243: v2243(0x40) = CONST 
    0x2246: v2246 = MLOAD v2243(0x40)
    0x2247: v2247(0x461bcd) = CONST 
    0x224b: v224b(0xe5) = CONST 
    0x224d: v224d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v224b(0xe5), v2247(0x461bcd)
    0x224f: MSTORE v2246, v224d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2250: v2250(0x20) = CONST 
    0x2252: v2252(0x4) = CONST 
    0x2255: v2255 = ADD v2246, v2252(0x4)
    0x2256: MSTORE v2255, v2250(0x20)
    0x2257: v2257(0x17) = CONST 
    0x2259: v2259(0x24) = CONST 
    0x225c: v225c = ADD v2246, v2259(0x24)
    0x225d: MSTORE v225c, v2257(0x17)
    0x225e: v225e(0x4f70657261746f7220646f6573206e6f74206578697374000000000000000000) = CONST 
    0x227f: v227f(0x44) = CONST 
    0x2282: v2282 = ADD v2246, v227f(0x44)
    0x2283: MSTORE v2282, v225e(0x4f70657261746f7220646f6573206e6f74206578697374000000000000000000)
    0x2285: v2285 = MLOAD v2243(0x40)
    0x2289: v2289(0x0) = SUB v2246, v2285
    0x228a: v228a(0x64) = CONST 
    0x228c: v228c(0x64) = ADD v228a(0x64), v2289(0x0)
    0x228e: REVERT v2285, v228c(0x64)

    Begin block 0x228f
    prev=[0x2222], succ=[0x40f8]
    =================================
    0x2290: v2290(0x1) = CONST 
    0x2292: v2292(0x1) = CONST 
    0x2294: v2294(0xa0) = CONST 
    0x2296: v2296(0x10000000000000000000000000000000000000000) = SHL v2294(0xa0), v2292(0x1)
    0x2297: v2297(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2296(0x10000000000000000000000000000000000000000), v2290(0x1)
    0x2298: v2298 = AND v2297(0xffffffffffffffffffffffffffffffffffffffff), vc37
    0x2299: v2299(0x0) = CONST 
    0x229d: MSTORE v2299(0x0), v2298
    0x229e: v229e(0x6) = CONST 
    0x22a0: v22a0(0x20) = CONST 
    0x22a2: MSTORE v22a0(0x20), v229e(0x6)
    0x22a3: v22a3(0x40) = CONST 
    0x22a6: v22a6 = SHA3 v2299(0x0), v22a3(0x40)
    0x22a8: v22a8 = SLOAD v22a6
    0x22a9: v22a9(0xff) = CONST 
    0x22ab: v22ab(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v22a9(0xff)
    0x22ac: v22ac = AND v22ab(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v22a8
    0x22ae: SSTORE v22a6, v22ac
    0x22af: JUMP vc17(0x40f8)

    Begin block 0x40f8
    prev=[0x228f], succ=[]
    =================================
    0x40f9: STOP 

}

function burnBatch(address,uint256[])() public {
    Begin block 0xc3c
    prev=[], succ=[0xc4e, 0xc52]
    =================================
    0xc3d: vc3d(0x4119) = CONST 
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
    prev=[0xc8e], succ=[0x22b0]
    =================================
    0xcb6: vcb6(0x22b0) = CONST 
    0xcb9: JUMP vcb6(0x22b0)

    Begin block 0x22b0
    prev=[0xcaf], succ=[0x22c8, 0x2305]
    =================================
    0x22b1: v22b1 = CALLER 
    0x22b2: v22b2(0x0) = CONST 
    0x22b6: MSTORE v22b2(0x0), v22b1
    0x22b7: v22b7(0x5) = CONST 
    0x22b9: v22b9(0x20) = CONST 
    0x22bb: MSTORE v22b9(0x20), v22b7(0x5)
    0x22bc: v22bc(0x40) = CONST 
    0x22bf: v22bf = SHA3 v22b2(0x0), v22bc(0x40)
    0x22c0: v22c0 = SLOAD v22bf
    0x22c1: v22c1(0xff) = CONST 
    0x22c3: v22c3 = AND v22c1(0xff), v22c0
    0x22c4: v22c4(0x2305) = CONST 
    0x22c7: JUMPI v22c4(0x2305), v22c3

    Begin block 0x22c8
    prev=[0x22b0], succ=[]
    =================================
    0x22c8: v22c8(0x40) = CONST 
    0x22cb: v22cb = MLOAD v22c8(0x40)
    0x22cc: v22cc(0x461bcd) = CONST 
    0x22d0: v22d0(0xe5) = CONST 
    0x22d2: v22d2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v22d0(0xe5), v22cc(0x461bcd)
    0x22d4: MSTORE v22cb, v22d2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22d5: v22d5(0x20) = CONST 
    0x22d7: v22d7(0x4) = CONST 
    0x22da: v22da = ADD v22cb, v22d7(0x4)
    0x22db: MSTORE v22da, v22d5(0x20)
    0x22dc: v22dc(0xe) = CONST 
    0x22de: v22de(0x24) = CONST 
    0x22e1: v22e1 = ADD v22cb, v22de(0x24)
    0x22e2: MSTORE v22e1, v22dc(0xe)
    0x22e3: v22e3(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x22f2: v22f2(0x91) = CONST 
    0x22f4: v22f4(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v22f2(0x91), v22e3(0x36bab9ba1031329036b4b73a32b9)
    0x22f5: v22f5(0x44) = CONST 
    0x22f8: v22f8 = ADD v22cb, v22f5(0x44)
    0x22f9: MSTORE v22f8, v22f4(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x22fb: v22fb = MLOAD v22c8(0x40)
    0x22ff: v22ff(0x0) = SUB v22cb, v22fb
    0x2300: v2300(0x64) = CONST 
    0x2302: v2302(0x64) = ADD v2300(0x64), v22ff(0x0)
    0x2304: REVERT v22fb, v2302(0x64)

    Begin block 0x2305
    prev=[0x22b0], succ=[0x2308]
    =================================
    0x2306: v2306(0x0) = CONST 

    Begin block 0x2308
    prev=[0x2305, 0x236d], succ=[0x2311, 0x2375]
    =================================
    0x2308_0x0: v2308_0 = PHI v2306(0x0), v2370
    0x230b: v230b = LT v2308_0, vc90
    0x230c: v230c = ISZERO v230b
    0x230d: v230d(0x2375) = CONST 
    0x2310: JUMPI v230d(0x2375), v230c

    Begin block 0x2311
    prev=[0x2308], succ=[0x231f, 0x2320]
    =================================
    0x2311: v2311(0x232c) = CONST 
    0x2311_0x0: v2311_0 = PHI v2306(0x0), v2370
    0x231a: v231a = LT v2311_0, vc90
    0x231b: v231b(0x2320) = CONST 
    0x231e: JUMPI v231b(0x2320), v231a

    Begin block 0x231f
    prev=[0x2311], succ=[]
    =================================
    0x231f: THROW 

    Begin block 0x2320
    prev=[0x2311], succ=[0x24b90xc3c]
    =================================
    0x2320_0x0: v2320_0 = PHI v2306(0x0), v2370
    0x2323: v2323(0x20) = CONST 
    0x2325: v2325 = MUL v2323(0x20), v2320_0
    0x2326: v2326 = ADD v2325, vc94
    0x2327: v2327 = CALLDATALOAD v2326
    0x2328: v2328(0x24b9) = CONST 
    0x232b: JUMP v2328(0x24b9)

    Begin block 0x24b90xc3c
    prev=[0x2320], succ=[0x24d10xc3c, 0x24ca0xc3c]
    =================================
    0x24ba0xc3c: vc3c24ba(0x0) = CONST 
    0x24bc0xc3c: vc3c24bc(0x1) = CONST 
    0x24be0xc3c: vc3c24be(0x1) = CONST 
    0x24c00xc3c: vc3c24c0(0xa0) = CONST 
    0x24c20xc3c: vc3c24c2(0x10000000000000000000000000000000000000000) = SHL vc3c24c0(0xa0), vc3c24be(0x1)
    0x24c30xc3c: vc3c24c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc3c24c2(0x10000000000000000000000000000000000000000), vc3c24bc(0x1)
    0x24c50xc3c: vc3c24c5 = AND vc5d, vc3c24c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x24c60xc3c: vc3c24c6(0x24d1) = CONST 
    0x24c90xc3c: JUMPI vc3c24c6(0x24d1), vc3c24c5

    Begin block 0x24d10xc3c
    prev=[0x24b90xc3c], succ=[0x44320xc3c]
    =================================
    0x24d30xc3c: vc3c24d3(0x0) = CONST 
    0x24d70xc3c: MSTORE vc3c24d3(0x0), v2327
    0x24d80xc3c: vc3c24d8(0x8) = CONST 
    0x24da0xc3c: vc3c24da(0x20) = CONST 
    0x24dc0xc3c: MSTORE vc3c24da(0x20), vc3c24d8(0x8)
    0x24dd0xc3c: vc3c24dd(0x40) = CONST 
    0x24e00xc3c: vc3c24e0 = SHA3 vc3c24d3(0x0), vc3c24dd(0x40)
    0x24e10xc3c: vc3c24e1 = SLOAD vc3c24e0
    0x24e20xc3c: vc3c24e2(0x1) = CONST 
    0x24e40xc3c: vc3c24e4(0x1) = CONST 
    0x24e60xc3c: vc3c24e6(0xa0) = CONST 
    0x24e80xc3c: vc3c24e8(0x10000000000000000000000000000000000000000) = SHL vc3c24e6(0xa0), vc3c24e4(0x1)
    0x24e90xc3c: vc3c24e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc3c24e8(0x10000000000000000000000000000000000000000), vc3c24e2(0x1)
    0x24ec0xc3c: vc3c24ec = AND vc3c24e9(0xffffffffffffffffffffffffffffffffffffffff), vc5d
    0x24ee0xc3c: vc3c24ee = AND vc3c24e1, vc3c24e9(0xffffffffffffffffffffffffffffffffffffffff)
    0x24ef0xc3c: vc3c24ef = EQ vc3c24ee, vc3c24ec
    0x24f00xc3c: vc3c24f0(0x4432) = CONST 
    0x24f30xc3c: JUMP vc3c24f0(0x4432)

    Begin block 0x44320xc3c
    prev=[0x24d10xc3c], succ=[0x232c]
    =================================
    0x44370xc3c: JUMP v2311(0x232c)

    Begin block 0x232c
    prev=[0x440d0xc3c, 0x44320xc3c], succ=[0x2331, 0x236d]
    =================================
    0x232c_0x0: v232c_0 = PHI vc3c24ef, vc3c24cb(0x0)
    0x232d: v232d(0x236d) = CONST 
    0x2330: JUMPI v232d(0x236d), v232c_0

    Begin block 0x2331
    prev=[0x232c], succ=[]
    =================================
    0x2331: v2331(0x40) = CONST 
    0x2334: v2334 = MLOAD v2331(0x40)
    0x2335: v2335(0x461bcd) = CONST 
    0x2339: v2339(0xe5) = CONST 
    0x233b: v233b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2339(0xe5), v2335(0x461bcd)
    0x233d: MSTORE v2334, v233b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x233e: v233e(0x20) = CONST 
    0x2340: v2340(0x4) = CONST 
    0x2343: v2343 = ADD v2334, v2340(0x4)
    0x2344: MSTORE v2343, v233e(0x20)
    0x2345: v2345(0xd) = CONST 
    0x2347: v2347(0x24) = CONST 
    0x234a: v234a = ADD v2334, v2347(0x24)
    0x234b: MSTORE v234a, v2345(0xd)
    0x234c: v234c(0x2737ba103a34329037bbb732b9) = CONST 
    0x235a: v235a(0x99) = CONST 
    0x235c: v235c(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v235a(0x99), v234c(0x2737ba103a34329037bbb732b9)
    0x235d: v235d(0x44) = CONST 
    0x2360: v2360 = ADD v2334, v235d(0x44)
    0x2361: MSTORE v2360, v235c(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x2363: v2363 = MLOAD v2331(0x40)
    0x2367: v2367(0x0) = SUB v2334, v2363
    0x2368: v2368(0x64) = CONST 
    0x236a: v236a(0x64) = ADD v2368(0x64), v2367(0x0)
    0x236c: REVERT v2363, v236a(0x64)

    Begin block 0x236d
    prev=[0x232c], succ=[0x2308]
    =================================
    0x236d_0x0: v236d_0 = PHI v2306(0x0), v2370
    0x236e: v236e(0x1) = CONST 
    0x2370: v2370 = ADD v236e(0x1), v236d_0
    0x2371: v2371(0x2308) = CONST 
    0x2374: JUMP v2371(0x2308)

    Begin block 0x24ca0xc3c
    prev=[0x24b90xc3c], succ=[0x440d0xc3c]
    =================================
    0x24cb0xc3c: vc3c24cb(0x0) = CONST 
    0x24cd0xc3c: vc3c24cd(0x440d) = CONST 
    0x24d00xc3c: JUMP vc3c24cd(0x440d)

    Begin block 0x440d0xc3c
    prev=[0x24ca0xc3c], succ=[0x232c]
    =================================
    0x44120xc3c: JUMP v2311(0x232c)

    Begin block 0x2375
    prev=[0x2308], succ=[0x3223]
    =================================
    0x2377: v2377(0x23b3) = CONST 
    0x237f: v237f(0x20) = CONST 
    0x2381: v2381 = MUL v237f(0x20), vc90
    0x2382: v2382(0x20) = CONST 
    0x2384: v2384 = ADD v2382(0x20), v2381
    0x2385: v2385(0x40) = CONST 
    0x2387: v2387 = MLOAD v2385(0x40)
    0x238a: v238a = ADD v2387, v2384
    0x238b: v238b(0x40) = CONST 
    0x238d: MSTORE v238b(0x40), v238a
    0x2395: MSTORE v2387, vc90
    0x2396: v2396(0x20) = CONST 
    0x2398: v2398 = ADD v2396(0x20), v2387
    0x239b: v239b(0x20) = CONST 
    0x239d: v239d = MUL v239b(0x20), vc90
    0x23a1: CALLDATACOPY v2398, vc94, v239d
    0x23a2: v23a2(0x0) = CONST 
    0x23a5: v23a5 = ADD v2398, v239d
    0x23a9: MSTORE v23a5, v23a2(0x0)
    0x23ab: v23ab(0x3223) = CONST 
    0x23b2: JUMP v23ab(0x3223)

    Begin block 0x3223
    prev=[0x2375], succ=[0x3239, 0x323d]
    =================================
    0x3224: v3224(0x0) = CONST 
    0x3227: v3227 = MLOAD v2387
    0x3228: v3228(0xffffffffffffffff) = CONST 
    0x3232: v3232 = GT v3227, v3228(0xffffffffffffffff)
    0x3234: v3234 = ISZERO v3232
    0x3235: v3235(0x323d) = CONST 
    0x3238: JUMPI v3235(0x323d), v3234

    Begin block 0x3239
    prev=[0x3223], succ=[]
    =================================
    0x3239: v3239(0x0) = CONST 
    0x323c: REVERT v3239(0x0), v3239(0x0)

    Begin block 0x323d
    prev=[0x3223], succ=[0x3267, 0x3258]
    =================================
    0x323f: v323f(0x40) = CONST 
    0x3241: v3241 = MLOAD v323f(0x40)
    0x3245: MSTORE v3241, v3227
    0x3247: v3247(0x20) = CONST 
    0x3249: v3249 = MUL v3247(0x20), v3227
    0x324a: v324a(0x20) = CONST 
    0x324c: v324c = ADD v324a(0x20), v3249
    0x324e: v324e = ADD v3241, v324c
    0x324f: v324f(0x40) = CONST 
    0x3251: MSTORE v324f(0x40), v324e
    0x3253: v3253 = ISZERO v3227
    0x3254: v3254(0x3267) = CONST 
    0x3257: JUMPI v3254(0x3267), v3253

    Begin block 0x3267
    prev=[0x323d, 0x3258], succ=[0x326d]
    =================================
    0x326b: v326b(0x0) = CONST 

    Begin block 0x326d
    prev=[0x3267, 0x339a], succ=[0x3277, 0x33ad]
    =================================
    0x326d_0x0: v326d_0 = PHI v326b(0x0), v33a8
    0x326f: v326f = MLOAD v2387
    0x3271: v3271 = LT v326d_0, v326f
    0x3272: v3272 = ISZERO v3271
    0x3273: v3273(0x33ad) = CONST 
    0x3276: JUMPI v3273(0x33ad), v3272

    Begin block 0x3277
    prev=[0x326d], succ=[0x3285, 0x3286]
    =================================
    0x3277: v3277(0x8) = CONST 
    0x3277_0x0: v3277_0 = PHI v326b(0x0), v33a8
    0x3279: v3279(0x0) = CONST 
    0x327e: v327e = MLOAD v2387
    0x3280: v3280 = LT v3277_0, v327e
    0x3281: v3281(0x3286) = CONST 
    0x3284: JUMPI v3281(0x3286), v3280

    Begin block 0x3285
    prev=[0x3277], succ=[]
    =================================
    0x3285: THROW 

    Begin block 0x3286
    prev=[0x3277], succ=[0x32c1, 0x32c2]
    =================================
    0x3286_0x0: v3286_0 = PHI v326b(0x0), v33a8
    0x3286_0x4: v3286_4 = PHI v326b(0x0), v33a8
    0x3287: v3287(0x20) = CONST 
    0x3289: v3289 = MUL v3287(0x20), v3286_0
    0x328a: v328a(0x20) = CONST 
    0x328c: v328c = ADD v328a(0x20), v3289
    0x328d: v328d = ADD v328c, v2387
    0x328e: v328e = MLOAD v328d
    0x3290: MSTORE v3279(0x0), v328e
    0x3291: v3291(0x20) = CONST 
    0x3293: v3293(0x20) = ADD v3291(0x20), v3279(0x0)
    0x3296: MSTORE v3293(0x20), v3277(0x8)
    0x3297: v3297(0x20) = CONST 
    0x3299: v3299(0x40) = ADD v3297(0x20), v3293(0x20)
    0x329a: v329a(0x0) = CONST 
    0x329c: v329c = SHA3 v329a(0x0), v3299(0x40)
    0x329d: v329d(0x0) = CONST 
    0x329f: v329f(0x100) = CONST 
    0x32a2: v32a2(0x1) = EXP v329f(0x100), v329d(0x0)
    0x32a4: v32a4 = SLOAD v329c
    0x32a6: v32a6(0x1) = CONST 
    0x32a8: v32a8(0x1) = CONST 
    0x32aa: v32aa(0xa0) = CONST 
    0x32ac: v32ac(0x10000000000000000000000000000000000000000) = SHL v32aa(0xa0), v32a8(0x1)
    0x32ad: v32ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32ac(0x10000000000000000000000000000000000000000), v32a6(0x1)
    0x32ae: v32ae(0xffffffffffffffffffffffffffffffffffffffff) = MUL v32ad(0xffffffffffffffffffffffffffffffffffffffff), v32a2(0x1)
    0x32af: v32af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v32ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x32b0: v32b0 = AND v32af(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v32a4
    0x32b2: SSTORE v329c, v32b0
    0x32b3: v32b3(0xb) = CONST 
    0x32b5: v32b5(0x0) = CONST 
    0x32ba: v32ba = MLOAD v2387
    0x32bc: v32bc = LT v3286_4, v32ba
    0x32bd: v32bd(0x32c2) = CONST 
    0x32c0: JUMPI v32bd(0x32c2), v32bc

    Begin block 0x32c1
    prev=[0x3286], succ=[]
    =================================
    0x32c1: THROW 

    Begin block 0x32c2
    prev=[0x3286], succ=[0x330a, 0x330b]
    =================================
    0x32c2_0x0: v32c2_0 = PHI v326b(0x0), v33a8
    0x32c2_0x4: v32c2_4 = PHI v326b(0x0), v33a8
    0x32c3: v32c3(0x20) = CONST 
    0x32c7: v32c7 = MUL v32c3(0x20), v32c2_0
    0x32cb: v32cb = ADD v32c7, v2387
    0x32cd: v32cd = ADD v32c3(0x20), v32cb
    0x32ce: v32ce = MLOAD v32cd
    0x32d0: MSTORE v32b5(0x0), v32ce
    0x32d2: v32d2(0x20) = ADD v32b5(0x0), v32c3(0x20)
    0x32d6: MSTORE v32d2(0x20), v32b3(0xb)
    0x32d7: v32d7(0x40) = CONST 
    0x32d9: v32d9(0x40) = ADD v32d7(0x40), v32b5(0x0)
    0x32da: v32da(0x0) = CONST 
    0x32de: v32de = SHA3 v32da(0x0), v32d9(0x40)
    0x32e0: v32e0 = SLOAD v32de
    0x32e1: v32e1(0x1) = CONST 
    0x32e3: v32e3(0x1) = CONST 
    0x32e5: v32e5(0xa0) = CONST 
    0x32e7: v32e7(0x10000000000000000000000000000000000000000) = SHL v32e5(0xa0), v32e3(0x1)
    0x32e8: v32e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32e7(0x10000000000000000000000000000000000000000), v32e1(0x1)
    0x32e9: v32e9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v32e8(0xffffffffffffffffffffffffffffffffffffffff)
    0x32ea: v32ea = AND v32e9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v32e0
    0x32ec: SSTORE v32de, v32ea
    0x32ed: v32ed(0x1) = CONST 
    0x32f0: v32f0 = ADD v32de, v32ed(0x1)
    0x32f3: SSTORE v32f0, v32da(0x0)
    0x32f4: v32f4(0x2) = CONST 
    0x32f6: v32f6 = ADD v32f4(0x2), v32de
    0x32f9: SSTORE v32f6, v32da(0x0)
    0x32fb: v32fb = MLOAD v2387
    0x32fc: v32fc(0xc) = CONST 
    0x3305: v3305 = LT v32c2_4, v32fb
    0x3306: v3306(0x330b) = CONST 
    0x3309: JUMPI v3306(0x330b), v3305

    Begin block 0x330a
    prev=[0x32c2], succ=[]
    =================================
    0x330a: THROW 

    Begin block 0x330b
    prev=[0x32c2], succ=[0x38c1B0x330b]
    =================================
    0x330b_0x0: v330b_0 = PHI v326b(0x0), v33a8
    0x330c: v330c(0x20) = CONST 
    0x330e: v330e = MUL v330c(0x20), v330b_0
    0x330f: v330f(0x20) = CONST 
    0x3311: v3311 = ADD v330f(0x20), v330e
    0x3312: v3312 = ADD v3311, v2387
    0x3313: v3313 = MLOAD v3312
    0x3315: MSTORE v32da(0x0), v3313
    0x3316: v3316(0x20) = CONST 
    0x3318: v3318(0x20) = ADD v3316(0x20), v32da(0x0)
    0x331b: MSTORE v3318(0x20), v32fc(0xc)
    0x331c: v331c(0x20) = CONST 
    0x331e: v331e(0x40) = ADD v331c(0x20), v3318(0x20)
    0x331f: v331f(0x0) = CONST 
    0x3321: v3321 = SHA3 v331f(0x0), v331e(0x40)
    0x3322: v3322(0x0) = CONST 
    0x3326: v3326 = ADD v3321, v3322(0x0)
    0x3327: v3327(0x0) = CONST 
    0x3329: v3329(0x3332) = CONST 
    0x332e: v332e(0x38c1) = CONST 
    0x3331: JUMP v332e(0x38c1), v3327(0x0), v3326, v3329(0x3332)

    Begin block 0x38c1B0x330b
    prev=[0x330b], succ=[0x3970B0x38c1B0x330b]
    =================================
    0x38c4S0x330b: v38c4V330b = SLOAD v3326
    0x38c5S0x330b: v38c5V330b(0x0) = CONST 
    0x38c8S0x330b: SSTORE v3326, v38c5V330b(0x0)
    0x38caS0x330b: v38caV330b(0x0) = CONST 
    0x38ccS0x330b: MSTORE v38caV330b(0x0), v3326
    0x38cdS0x330b: v38cdV330b(0x20) = CONST 
    0x38cfS0x330b: v38cfV330b(0x0) = CONST 
    0x38d1S0x330b: v38d1V330b = SHA3 v38cfV330b(0x0), v38cdV330b(0x20)
    0x38d4S0x330b: v38d4V330b = ADD v38d1V330b, v38c4V330b
    0x38d6S0x330b: v38d6V330b(0x38df) = CONST 
    0x38dbS0x330b: v38dbV330b(0x3970) = CONST 
    0x38deS0x330b: JUMP v38dbV330b(0x3970)

    Begin block 0x3970B0x38c1B0x330b
    prev=[0x38c1B0x330b], succ=[0x3971B0x38c1B0x330b]
    =================================

    Begin block 0x3971B0x38c1B0x330b
    prev=[0x397aB0x38c1B0x330b, 0x3970B0x38c1B0x330b], succ=[0x397aB0x38c1B0x330b, 0x45cfB0x38c1B0x330b]
    =================================
    0x3971_0x0S0x38c1S0x330b: v3971_0V38c1V330b = PHI v38d1V330b, v3980V38c1V330b
    0x3974S0x38c1S0x330b: v3974V38c1V330b = GT v38d4V330b, v3971_0V38c1V330b
    0x3975S0x38c1S0x330b: v3975V38c1V330b = ISZERO v3974V38c1V330b
    0x3976S0x38c1S0x330b: v3976V38c1V330b(0x45cf) = CONST 
    0x3979S0x38c1S0x330b: JUMPI v3976V38c1V330b(0x45cf), v3975V38c1V330b

    Begin block 0x397aB0x38c1B0x330b
    prev=[0x3971B0x38c1B0x330b], succ=[0x3971B0x38c1B0x330b]
    =================================
    0x397aS0x38c1S0x330b: v397aV38c1V330b(0x0) = CONST 
    0x397a_0x0S0x38c1S0x330b: v397a_0V38c1V330b = PHI v38d1V330b, v3980V38c1V330b
    0x397dS0x38c1S0x330b: SSTORE v397a_0V38c1V330b, v397aV38c1V330b(0x0)
    0x397eS0x38c1S0x330b: v397eV38c1V330b(0x1) = CONST 
    0x3980S0x38c1S0x330b: v3980V38c1V330b = ADD v397eV38c1V330b(0x1), v397a_0V38c1V330b
    0x3981S0x38c1S0x330b: v3981V38c1V330b(0x3971) = CONST 
    0x3984S0x38c1S0x330b: JUMP v3981V38c1V330b(0x3971)

    Begin block 0x45cfB0x38c1B0x330b
    prev=[0x3971B0x38c1B0x330b], succ=[0x38dfB0x330b]
    =================================
    0x45d2S0x38c1S0x330b: JUMP v38d6V330b(0x38df)

    Begin block 0x38dfB0x330b
    prev=[0x45cfB0x38c1B0x330b], succ=[0x3332]
    =================================
    0x38e1S0x330b: JUMP v3329(0x3332)

    Begin block 0x3332
    prev=[0x38dfB0x330b], succ=[0x38c1B0x3332]
    =================================
    0x3333: v3333(0x3340) = CONST 
    0x3336: v3336(0x1) = CONST 
    0x3339: v3339 = ADD v3321, v3336(0x1)
    0x333a: v333a(0x0) = CONST 
    0x333c: v333c(0x38c1) = CONST 
    0x333f: JUMP v333c(0x38c1), v333a(0x0), v3339, v3333(0x3340)

    Begin block 0x38c1B0x3332
    prev=[0x3332], succ=[0x3970B0x38c1B0x3332]
    =================================
    0x38c4S0x3332: v38c4V3332 = SLOAD v3339
    0x38c5S0x3332: v38c5V3332(0x0) = CONST 
    0x38c8S0x3332: SSTORE v3339, v38c5V3332(0x0)
    0x38caS0x3332: v38caV3332(0x0) = CONST 
    0x38ccS0x3332: MSTORE v38caV3332(0x0), v3339
    0x38cdS0x3332: v38cdV3332(0x20) = CONST 
    0x38cfS0x3332: v38cfV3332(0x0) = CONST 
    0x38d1S0x3332: v38d1V3332 = SHA3 v38cfV3332(0x0), v38cdV3332(0x20)
    0x38d4S0x3332: v38d4V3332 = ADD v38d1V3332, v38c4V3332
    0x38d6S0x3332: v38d6V3332(0x38df) = CONST 
    0x38dbS0x3332: v38dbV3332(0x3970) = CONST 
    0x38deS0x3332: JUMP v38dbV3332(0x3970)

    Begin block 0x3970B0x38c1B0x3332
    prev=[0x38c1B0x3332], succ=[0x3971B0x38c1B0x3332]
    =================================

    Begin block 0x3971B0x38c1B0x3332
    prev=[0x397aB0x38c1B0x3332, 0x3970B0x38c1B0x3332], succ=[0x397aB0x38c1B0x3332, 0x45cfB0x38c1B0x3332]
    =================================
    0x3971_0x0S0x38c1S0x3332: v3971_0V38c1V3332 = PHI v38d1V3332, v3980V38c1V3332
    0x3974S0x38c1S0x3332: v3974V38c1V3332 = GT v38d4V3332, v3971_0V38c1V3332
    0x3975S0x38c1S0x3332: v3975V38c1V3332 = ISZERO v3974V38c1V3332
    0x3976S0x38c1S0x3332: v3976V38c1V3332(0x45cf) = CONST 
    0x3979S0x38c1S0x3332: JUMPI v3976V38c1V3332(0x45cf), v3975V38c1V3332

    Begin block 0x397aB0x38c1B0x3332
    prev=[0x3971B0x38c1B0x3332], succ=[0x3971B0x38c1B0x3332]
    =================================
    0x397aS0x38c1S0x3332: v397aV38c1V3332(0x0) = CONST 
    0x397a_0x0S0x38c1S0x3332: v397a_0V38c1V3332 = PHI v38d1V3332, v3980V38c1V3332
    0x397dS0x38c1S0x3332: SSTORE v397a_0V38c1V3332, v397aV38c1V3332(0x0)
    0x397eS0x38c1S0x3332: v397eV38c1V3332(0x1) = CONST 
    0x3980S0x38c1S0x3332: v3980V38c1V3332 = ADD v397eV38c1V3332(0x1), v397a_0V38c1V3332
    0x3981S0x38c1S0x3332: v3981V38c1V3332(0x3971) = CONST 
    0x3984S0x38c1S0x3332: JUMP v3981V38c1V3332(0x3971)

    Begin block 0x45cfB0x38c1B0x3332
    prev=[0x3971B0x38c1B0x3332], succ=[0x38dfB0x3332]
    =================================
    0x45d2S0x38c1S0x3332: JUMP v38d6V3332(0x38df)

    Begin block 0x38dfB0x3332
    prev=[0x45cfB0x38c1B0x3332], succ=[0x3340]
    =================================
    0x38e1S0x3332: JUMP v3333(0x3340)

    Begin block 0x3340
    prev=[0x38dfB0x3332], succ=[0x3359, 0x335a]
    =================================
    0x3340_0x2: v3340_2 = PHI v326b(0x0), v33a8
    0x3341: v3341(0x2) = CONST 
    0x3344: v3344 = ADD v3321, v3341(0x2)
    0x3345: v3345(0x0) = CONST 
    0x3348: SSTORE v3344, v3345(0x0)
    0x334b: v334b(0xa) = CONST 
    0x334d: v334d(0x0) = CONST 
    0x3352: v3352 = MLOAD v2387
    0x3354: v3354 = LT v3340_2, v3352
    0x3355: v3355(0x335a) = CONST 
    0x3358: JUMPI v3355(0x335a), v3354

    Begin block 0x3359
    prev=[0x3340], succ=[]
    =================================
    0x3359: THROW 

    Begin block 0x335a
    prev=[0x3340], succ=[0x3399, 0x339a]
    =================================
    0x335a_0x0: v335a_0 = PHI v326b(0x0), v33a8
    0x335a_0x4: v335a_4 = PHI v326b(0x0), v33a8
    0x335b: v335b(0x20) = CONST 
    0x335f: v335f = MUL v335b(0x20), v335a_0
    0x3363: v3363 = ADD v335f, v2387
    0x3365: v3365 = ADD v335b(0x20), v3363
    0x3366: v3366 = MLOAD v3365
    0x3368: MSTORE v334d(0x0), v3366
    0x336a: v336a(0x20) = ADD v334d(0x0), v335b(0x20)
    0x336e: MSTORE v336a(0x20), v334b(0xa)
    0x336f: v336f(0x40) = CONST 
    0x3371: v3371(0x40) = ADD v336f(0x40), v334d(0x0)
    0x3372: v3372(0x0) = CONST 
    0x3376: v3376 = SHA3 v3372(0x0), v3371(0x40)
    0x3379: SSTORE v3376, v3372(0x0)
    0x337a: v337a(0x1) = CONST 
    0x337e: v337e = ADD v337a(0x1), v3376
    0x3380: v3380 = SLOAD v337e
    0x3381: v3381(0x1) = CONST 
    0x3383: v3383(0x1) = CONST 
    0x3385: v3385(0xa0) = CONST 
    0x3387: v3387(0x10000000000000000000000000000000000000000) = SHL v3385(0xa0), v3383(0x1)
    0x3388: v3388(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3387(0x10000000000000000000000000000000000000000), v3381(0x1)
    0x3389: v3389(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3388(0xffffffffffffffffffffffffffffffffffffffff)
    0x338a: v338a = AND v3389(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3380
    0x338c: SSTORE v337e, v338a
    0x338e: v338e = MLOAD v3241
    0x3394: v3394 = LT v335a_4, v338e
    0x3395: v3395(0x339a) = CONST 
    0x3398: JUMPI v3395(0x339a), v3394

    Begin block 0x3399
    prev=[0x335a], succ=[]
    =================================
    0x3399: THROW 

    Begin block 0x339a
    prev=[0x335a], succ=[0x326d]
    =================================
    0x339a_0x0: v339a_0 = PHI v326b(0x0), v33a8
    0x339a_0x3: v339a_3 = PHI v326b(0x0), v33a8
    0x339b: v339b(0x20) = CONST 
    0x339f: v339f = MUL v339b(0x20), v339a_0
    0x33a3: v33a3 = ADD v339f, v3241
    0x33a4: v33a4 = ADD v33a3, v339b(0x20)
    0x33a5: MSTORE v33a4, v337a(0x1)
    0x33a6: v33a6(0x1) = CONST 
    0x33a8: v33a8 = ADD v33a6(0x1), v339a_3
    0x33a9: v33a9(0x326d) = CONST 
    0x33ac: JUMP v33a9(0x326d)

    Begin block 0x33ad
    prev=[0x326d], succ=[0x341c]
    =================================
    0x33af: v33af(0x0) = CONST 
    0x33b1: v33b1(0x1) = CONST 
    0x33b3: v33b3(0x1) = CONST 
    0x33b5: v33b5(0xa0) = CONST 
    0x33b7: v33b7(0x10000000000000000000000000000000000000000) = SHL v33b5(0xa0), v33b3(0x1)
    0x33b8: v33b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v33b7(0x10000000000000000000000000000000000000000), v33b1(0x1)
    0x33b9: v33b9(0x0) = AND v33b8(0xffffffffffffffffffffffffffffffffffffffff), v33af(0x0)
    0x33bb: v33bb(0x1) = CONST 
    0x33bd: v33bd(0x1) = CONST 
    0x33bf: v33bf(0xa0) = CONST 
    0x33c1: v33c1(0x10000000000000000000000000000000000000000) = SHL v33bf(0xa0), v33bd(0x1)
    0x33c2: v33c2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v33c1(0x10000000000000000000000000000000000000000), v33bb(0x1)
    0x33c3: v33c3 = AND v33c2(0xffffffffffffffffffffffffffffffffffffffff), vc5d
    0x33c4: v33c4 = CALLER 
    0x33c5: v33c5(0x1) = CONST 
    0x33c7: v33c7(0x1) = CONST 
    0x33c9: v33c9(0xa0) = CONST 
    0x33cb: v33cb(0x10000000000000000000000000000000000000000) = SHL v33c9(0xa0), v33c7(0x1)
    0x33cc: v33cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v33cb(0x10000000000000000000000000000000000000000), v33c5(0x1)
    0x33cd: v33cd = AND v33cc(0xffffffffffffffffffffffffffffffffffffffff), v33c4
    0x33ce: v33ce(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x33f1: v33f1(0x40) = CONST 
    0x33f3: v33f3 = MLOAD v33f1(0x40)
    0x33f6: v33f6(0x20) = CONST 
    0x33f8: v33f8 = ADD v33f6(0x20), v33f3
    0x33fa: v33fa(0x20) = CONST 
    0x33fc: v33fc = ADD v33fa(0x20), v33f8
    0x33ff: v33ff(0x40) = SUB v33fc, v33f3
    0x3401: MSTORE v33f3, v33ff(0x40)
    0x3405: v3405 = MLOAD v2387
    0x3407: MSTORE v33fc, v3405
    0x3408: v3408(0x20) = CONST 
    0x340a: v340a = ADD v3408(0x20), v33fc
    0x340e: v340e = MLOAD v2387
    0x3410: v3410(0x20) = CONST 
    0x3412: v3412 = ADD v3410(0x20), v2387
    0x3414: v3414(0x20) = CONST 
    0x3416: v3416 = MUL v3414(0x20), v340e
    0x341a: v341a(0x0) = CONST 

    Begin block 0x341c
    prev=[0x33ad, 0x3425], succ=[0x3434, 0x3425]
    =================================
    0x341c_0x0: v341c_0 = PHI v341a(0x0), v342f
    0x341f: v341f = LT v341c_0, v3416
    0x3420: v3420 = ISZERO v341f
    0x3421: v3421(0x3434) = CONST 
    0x3424: JUMPI v3421(0x3434), v3420

    Begin block 0x3434
    prev=[0x341c], succ=[0x345b]
    =================================
    0x343b: v343b = ADD v3416, v340a
    0x343e: v343e = SUB v343b, v33f3
    0x3440: MSTORE v33f8, v343e
    0x3444: v3444 = MLOAD v3241
    0x3446: MSTORE v343b, v3444
    0x3447: v3447(0x20) = CONST 
    0x3449: v3449 = ADD v3447(0x20), v343b
    0x344d: v344d = MLOAD v3241
    0x344f: v344f(0x20) = CONST 
    0x3451: v3451 = ADD v344f(0x20), v3241
    0x3453: v3453(0x20) = CONST 
    0x3455: v3455 = MUL v3453(0x20), v344d
    0x3459: v3459(0x0) = CONST 

    Begin block 0x345b
    prev=[0x3434, 0x3464], succ=[0x3473, 0x3464]
    =================================
    0x345b_0x0: v345b_0 = PHI v3459(0x0), v346e
    0x345e: v345e = LT v345b_0, v3455
    0x345f: v345f = ISZERO v345e
    0x3460: v3460(0x3473) = CONST 
    0x3463: JUMPI v3460(0x3473), v345f

    Begin block 0x3473
    prev=[0x345b], succ=[0x23b3]
    =================================
    0x347a: v347a = ADD v3455, v3449
    0x3481: v3481(0x40) = CONST 
    0x3483: v3483 = MLOAD v3481(0x40)
    0x3486: v3486 = SUB v347a, v3483
    0x3488: LOG4 v3483, v3486, v33ce(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v33cd, v33c3, v33b9(0x0)
    0x348c: JUMP v2377(0x23b3)

    Begin block 0x23b3
    prev=[0x3473], succ=[0x4119]
    =================================
    0x23b7: JUMP vc3d(0x4119)

    Begin block 0x4119
    prev=[0x23b3], succ=[]
    =================================
    0x411a: STOP 

    Begin block 0x3464
    prev=[0x345b], succ=[0x345b]
    =================================
    0x3464_0x0: v3464_0 = PHI v3459(0x0), v346e
    0x3466: v3466 = ADD v3464_0, v3451
    0x3467: v3467 = MLOAD v3466
    0x346a: v346a = ADD v3464_0, v3449
    0x346b: MSTORE v346a, v3467
    0x346c: v346c(0x20) = CONST 
    0x346e: v346e = ADD v346c(0x20), v3464_0
    0x346f: v346f(0x345b) = CONST 
    0x3472: JUMP v346f(0x345b)

    Begin block 0x3425
    prev=[0x341c], succ=[0x341c]
    =================================
    0x3425_0x0: v3425_0 = PHI v341a(0x0), v342f
    0x3427: v3427 = ADD v3425_0, v3412
    0x3428: v3428 = MLOAD v3427
    0x342b: v342b = ADD v3425_0, v340a
    0x342c: MSTORE v342b, v3428
    0x342d: v342d(0x20) = CONST 
    0x342f: v342f = ADD v342d(0x20), v3425_0
    0x3430: v3430(0x341c) = CONST 
    0x3433: JUMP v3430(0x341c)

    Begin block 0x3258
    prev=[0x323d], succ=[0x3267]
    =================================
    0x3259: v3259(0x20) = CONST 
    0x325b: v325b = ADD v3259(0x20), v3241
    0x325c: v325c(0x20) = CONST 
    0x325f: v325f = MUL v3227, v325c(0x20)
    0x3261: v3261 = CALLDATASIZE 
    0x3263: CALLDATACOPY v325b, v3261, v325f
    0x3264: v3264 = ADD v325f, v325b

}

function starNFTOwner()() public {
    Begin block 0xcba
    prev=[], succ=[0x23b8]
    =================================
    0xcbb: vcbb(0x413a) = CONST 
    0xcbe: vcbe(0x23b8) = CONST 
    0xcc1: JUMP vcbe(0x23b8)

    Begin block 0x23b8
    prev=[0xcba], succ=[0x413a]
    =================================
    0x23b9: v23b9(0x3) = CONST 
    0x23bb: v23bb = SLOAD v23b9(0x3)
    0x23bc: v23bc(0x1) = CONST 
    0x23be: v23be(0x1) = CONST 
    0x23c0: v23c0(0xa0) = CONST 
    0x23c2: v23c2(0x10000000000000000000000000000000000000000) = SHL v23c0(0xa0), v23be(0x1)
    0x23c3: v23c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23c2(0x10000000000000000000000000000000000000000), v23bc(0x1)
    0x23c4: v23c4 = AND v23c3(0xffffffffffffffffffffffffffffffffffffffff), v23bb
    0x23c6: JUMP vcbb(0x413a)

    Begin block 0x413a
    prev=[0x23b8], succ=[]
    =================================
    0x413b: v413b(0x40) = CONST 
    0x413e: v413e = MLOAD v413b(0x40)
    0x413f: v413f(0x1) = CONST 
    0x4141: v4141(0x1) = CONST 
    0x4143: v4143(0xa0) = CONST 
    0x4145: v4145(0x10000000000000000000000000000000000000000) = SHL v4143(0xa0), v4141(0x1)
    0x4146: v4146(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4145(0x10000000000000000000000000000000000000000), v413f(0x1)
    0x4149: v4149 = AND v23c4, v4146(0xffffffffffffffffffffffffffffffffffffffff)
    0x414b: MSTORE v413e, v4149
    0x414c: v414c = MLOAD v413b(0x40)
    0x4150: v4150(0x0) = SUB v413e, v414c
    0x4151: v4151(0x20) = CONST 
    0x4153: v4153(0x20) = ADD v4151(0x20), v4150(0x0)
    0x4155: RETURN v414c, v4153(0x20)

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
    prev=[0xcc2], succ=[0x23c7]
    =================================
    0xcda: vcda = CALLDATALOAD vcc6(0x4)
    0xcdb: vcdb(0x23c7) = CONST 
    0xcde: JUMP vcdb(0x23c7)

    Begin block 0x23c7
    prev=[0xcd8], succ=[0xcdf]
    =================================
    0x23c8: v23c8(0x0) = CONST 
    0x23cc: MSTORE v23c8(0x0), vcda
    0x23cd: v23cd(0xa) = CONST 
    0x23cf: v23cf(0x20) = CONST 
    0x23d1: MSTORE v23cf(0x20), v23cd(0xa)
    0x23d2: v23d2(0x40) = CONST 
    0x23d5: v23d5 = SHA3 v23c8(0x0), v23d2(0x40)
    0x23d7: v23d7 = SLOAD v23d5
    0x23d8: v23d8(0x1) = CONST 
    0x23dc: v23dc = ADD v23d5, v23d8(0x1)
    0x23dd: v23dd = SLOAD v23dc
    0x23de: v23de(0x1) = CONST 
    0x23e0: v23e0(0x1) = CONST 
    0x23e2: v23e2(0x80) = CONST 
    0x23e4: v23e4(0x100000000000000000000000000000000) = SHL v23e2(0x80), v23e0(0x1)
    0x23e5: v23e5(0xffffffffffffffffffffffffffffffff) = SUB v23e4(0x100000000000000000000000000000000), v23de(0x1)
    0x23e6: v23e6(0x1) = CONST 
    0x23e8: v23e8(0x80) = CONST 
    0x23ea: v23ea(0x100000000000000000000000000000000) = SHL v23e8(0x80), v23e6(0x1)
    0x23ec: v23ec = DIV v23d7, v23ea(0x100000000000000000000000000000000)
    0x23ee: v23ee = AND v23e5(0xffffffffffffffffffffffffffffffff), v23ec
    0x23f1: v23f1 = AND v23d7, v23e5(0xffffffffffffffffffffffffffffffff)
    0x23f3: v23f3(0x1) = CONST 
    0x23f5: v23f5(0x1) = CONST 
    0x23f7: v23f7(0xa0) = CONST 
    0x23f9: v23f9(0x10000000000000000000000000000000000000000) = SHL v23f7(0xa0), v23f5(0x1)
    0x23fa: v23fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23f9(0x10000000000000000000000000000000000000000), v23f3(0x1)
    0x23fd: v23fd = AND v23dd, v23fa(0xffffffffffffffffffffffffffffffffffffffff)
    0x23ff: JUMP vcc3(0xcdf)

    Begin block 0xcdf
    prev=[0x23c7], succ=[]
    =================================
    0xce0: vce0(0x40) = CONST 
    0xce3: vce3 = MLOAD vce0(0x40)
    0xce4: vce4(0x1) = CONST 
    0xce6: vce6(0x1) = CONST 
    0xce8: vce8(0x80) = CONST 
    0xcea: vcea(0x100000000000000000000000000000000) = SHL vce8(0x80), vce6(0x1)
    0xceb: vceb(0xffffffffffffffffffffffffffffffff) = SUB vcea(0x100000000000000000000000000000000), vce4(0x1)
    0xcee: vcee = AND vceb(0xffffffffffffffffffffffffffffffff), v23ee
    0xcf0: MSTORE vce3, vcee
    0xcf4: vcf4 = AND vceb(0xffffffffffffffffffffffffffffffff), v23f1
    0xcf5: vcf5(0x20) = CONST 
    0xcf8: vcf8 = ADD vce3, vcf5(0x20)
    0xcf9: MSTORE vcf8, vcf4
    0xcfa: vcfa(0x1) = CONST 
    0xcfc: vcfc(0x1) = CONST 
    0xcfe: vcfe(0xa0) = CONST 
    0xd00: vd00(0x10000000000000000000000000000000000000000) = SHL vcfe(0xa0), vcfc(0x1)
    0xd01: vd01(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd00(0x10000000000000000000000000000000000000000), vcfa(0x1)
    0xd02: vd02 = AND vd01(0xffffffffffffffffffffffffffffffffffffffff), v23fd
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
    0xd13: vd13(0x4175) = CONST 
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
    prev=[0xd12], succ=[0x2400]
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
    0xd3a: vd3a(0x2400) = CONST 
    0xd3d: JUMP vd3a(0x2400)

    Begin block 0x2400
    prev=[0xd28], succ=[0x2418, 0x2455]
    =================================
    0x2401: v2401 = CALLER 
    0x2402: v2402(0x0) = CONST 
    0x2406: MSTORE v2402(0x0), v2401
    0x2407: v2407(0x5) = CONST 
    0x2409: v2409(0x20) = CONST 
    0x240b: MSTORE v2409(0x20), v2407(0x5)
    0x240c: v240c(0x40) = CONST 
    0x240f: v240f = SHA3 v2402(0x0), v240c(0x40)
    0x2410: v2410 = SLOAD v240f
    0x2411: v2411(0xff) = CONST 
    0x2413: v2413 = AND v2411(0xff), v2410
    0x2414: v2414(0x2455) = CONST 
    0x2417: JUMPI v2414(0x2455), v2413

    Begin block 0x2418
    prev=[0x2400], succ=[]
    =================================
    0x2418: v2418(0x40) = CONST 
    0x241b: v241b = MLOAD v2418(0x40)
    0x241c: v241c(0x461bcd) = CONST 
    0x2420: v2420(0xe5) = CONST 
    0x2422: v2422(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2420(0xe5), v241c(0x461bcd)
    0x2424: MSTORE v241b, v2422(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2425: v2425(0x20) = CONST 
    0x2427: v2427(0x4) = CONST 
    0x242a: v242a = ADD v241b, v2427(0x4)
    0x242b: MSTORE v242a, v2425(0x20)
    0x242c: v242c(0xe) = CONST 
    0x242e: v242e(0x24) = CONST 
    0x2431: v2431 = ADD v241b, v242e(0x24)
    0x2432: MSTORE v2431, v242c(0xe)
    0x2433: v2433(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x2442: v2442(0x91) = CONST 
    0x2444: v2444(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v2442(0x91), v2433(0x36bab9ba1031329036b4b73a32b9)
    0x2445: v2445(0x44) = CONST 
    0x2448: v2448 = ADD v241b, v2445(0x44)
    0x2449: MSTORE v2448, v2444(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x244b: v244b = MLOAD v2418(0x40)
    0x244f: v244f(0x0) = SUB v241b, v244b
    0x2450: v2450(0x64) = CONST 
    0x2452: v2452(0x64) = ADD v2450(0x64), v244f(0x0)
    0x2454: REVERT v244b, v2452(0x64)

    Begin block 0x2455
    prev=[0x2400], succ=[0x245f]
    =================================
    0x2456: v2456(0x245f) = CONST 
    0x245b: v245b(0x24b9) = CONST 
    0x245e: v245e_0 = CALLPRIVATE v245b(0x24b9), vd39, vd34, v2456(0x245f)

    Begin block 0x245f
    prev=[0x2455], succ=[0x2464, 0x24b0]
    =================================
    0x2460: v2460(0x24b0) = CONST 
    0x2463: JUMPI v2460(0x24b0), v245e_0

    Begin block 0x2464
    prev=[0x245f], succ=[]
    =================================
    0x2464: v2464(0x40) = CONST 
    0x2467: v2467 = MLOAD v2464(0x40)
    0x2468: v2468(0x461bcd) = CONST 
    0x246c: v246c(0xe5) = CONST 
    0x246e: v246e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v246c(0xe5), v2468(0x461bcd)
    0x2470: MSTORE v2467, v246e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2471: v2471(0x20) = CONST 
    0x2473: v2473(0x4) = CONST 
    0x2476: v2476 = ADD v2467, v2473(0x4)
    0x2477: MSTORE v2476, v2471(0x20)
    0x2478: v2478(0x1f) = CONST 
    0x247a: v247a(0x24) = CONST 
    0x247d: v247d = ADD v2467, v247a(0x24)
    0x247e: MSTORE v247d, v2478(0x1f)
    0x247f: v247f(0x4d757374206265206f776e6572206f662074686973205375706572204e465400) = CONST 
    0x24a0: v24a0(0x44) = CONST 
    0x24a3: v24a3 = ADD v2467, v24a0(0x44)
    0x24a4: MSTORE v24a3, v247f(0x4d757374206265206f776e6572206f662074686973205375706572204e465400)
    0x24a6: v24a6 = MLOAD v2464(0x40)
    0x24aa: v24aa(0x0) = SUB v2467, v24a6
    0x24ab: v24ab(0x64) = CONST 
    0x24ad: v24ad(0x64) = ADD v24ab(0x64), v24aa(0x0)
    0x24af: REVERT v24a6, v24ad(0x64)

    Begin block 0x24b0
    prev=[0x245f], succ=[0x348d]
    =================================
    0x24b1: v24b1(0x43ea) = CONST 
    0x24b5: v24b5(0x348d) = CONST 
    0x24b8: JUMP v24b5(0x348d)

    Begin block 0x348d
    prev=[0x24b0], succ=[0x38c1B0x348d]
    =================================
    0x348e: v348e(0x0) = CONST 
    0x3492: MSTORE v348e(0x0), vd39
    0x3493: v3493(0xc) = CONST 
    0x3495: v3495(0x20) = CONST 
    0x3497: MSTORE v3495(0x20), v3493(0xc)
    0x3498: v3498(0x40) = CONST 
    0x349b: v349b = SHA3 v348e(0x0), v3498(0x40)
    0x349c: v349c(0x34a4) = CONST 
    0x34a0: v34a0(0x38c1) = CONST 
    0x34a3: JUMP v34a0(0x38c1), v348e(0x0), v349b, v349c(0x34a4)

    Begin block 0x38c1B0x348d
    prev=[0x348d], succ=[0x3970B0x38c1B0x348d]
    =================================
    0x38c4S0x348d: v38c4V348d = SLOAD v349b
    0x38c5S0x348d: v38c5V348d(0x0) = CONST 
    0x38c8S0x348d: SSTORE v349b, v38c5V348d(0x0)
    0x38caS0x348d: v38caV348d(0x0) = CONST 
    0x38ccS0x348d: MSTORE v38caV348d(0x0), v349b
    0x38cdS0x348d: v38cdV348d(0x20) = CONST 
    0x38cfS0x348d: v38cfV348d(0x0) = CONST 
    0x38d1S0x348d: v38d1V348d = SHA3 v38cfV348d(0x0), v38cdV348d(0x20)
    0x38d4S0x348d: v38d4V348d = ADD v38d1V348d, v38c4V348d
    0x38d6S0x348d: v38d6V348d(0x38df) = CONST 
    0x38dbS0x348d: v38dbV348d(0x3970) = CONST 
    0x38deS0x348d: JUMP v38dbV348d(0x3970)

    Begin block 0x3970B0x38c1B0x348d
    prev=[0x38c1B0x348d], succ=[0x3971B0x38c1B0x348d]
    =================================

    Begin block 0x3971B0x38c1B0x348d
    prev=[0x397aB0x38c1B0x348d, 0x3970B0x38c1B0x348d], succ=[0x397aB0x38c1B0x348d, 0x45cfB0x38c1B0x348d]
    =================================
    0x3971_0x0S0x38c1S0x348d: v3971_0V38c1V348d = PHI v38d1V348d, v3980V38c1V348d
    0x3974S0x38c1S0x348d: v3974V38c1V348d = GT v38d4V348d, v3971_0V38c1V348d
    0x3975S0x38c1S0x348d: v3975V38c1V348d = ISZERO v3974V38c1V348d
    0x3976S0x38c1S0x348d: v3976V38c1V348d(0x45cf) = CONST 
    0x3979S0x38c1S0x348d: JUMPI v3976V38c1V348d(0x45cf), v3975V38c1V348d

    Begin block 0x397aB0x38c1B0x348d
    prev=[0x3971B0x38c1B0x348d], succ=[0x3971B0x38c1B0x348d]
    =================================
    0x397aS0x38c1S0x348d: v397aV38c1V348d(0x0) = CONST 
    0x397a_0x0S0x38c1S0x348d: v397a_0V38c1V348d = PHI v38d1V348d, v3980V38c1V348d
    0x397dS0x38c1S0x348d: SSTORE v397a_0V38c1V348d, v397aV38c1V348d(0x0)
    0x397eS0x38c1S0x348d: v397eV38c1V348d(0x1) = CONST 
    0x3980S0x38c1S0x348d: v3980V38c1V348d = ADD v397eV38c1V348d(0x1), v397a_0V38c1V348d
    0x3981S0x38c1S0x348d: v3981V38c1V348d(0x3971) = CONST 
    0x3984S0x38c1S0x348d: JUMP v3981V38c1V348d(0x3971)

    Begin block 0x45cfB0x38c1B0x348d
    prev=[0x3971B0x38c1B0x348d], succ=[0x38dfB0x348d]
    =================================
    0x45d2S0x38c1S0x348d: JUMP v38d6V348d(0x38df)

    Begin block 0x38dfB0x348d
    prev=[0x45cfB0x38c1B0x348d], succ=[0x34a4]
    =================================
    0x38e1S0x348d: JUMP v349c(0x34a4)

    Begin block 0x34a4
    prev=[0x38dfB0x348d], succ=[0x38c1B0x34a4]
    =================================
    0x34a5: v34a5(0x0) = CONST 
    0x34a9: MSTORE v34a5(0x0), vd39
    0x34aa: v34aa(0xc) = CONST 
    0x34ac: v34ac(0x20) = CONST 
    0x34ae: MSTORE v34ac(0x20), v34aa(0xc)
    0x34af: v34af(0x40) = CONST 
    0x34b2: v34b2 = SHA3 v34a5(0x0), v34af(0x40)
    0x34b3: v34b3(0x34c1) = CONST 
    0x34b7: v34b7(0x1) = CONST 
    0x34bb: v34bb = ADD v34b2, v34b7(0x1)
    0x34bd: v34bd(0x38c1) = CONST 
    0x34c0: JUMP v34bd(0x38c1), v34a5(0x0), v34bb, v34b3(0x34c1)

    Begin block 0x38c1B0x34a4
    prev=[0x34a4], succ=[0x3970B0x38c1B0x34a4]
    =================================
    0x38c4S0x34a4: v38c4V34a4 = SLOAD v34bb
    0x38c5S0x34a4: v38c5V34a4(0x0) = CONST 
    0x38c8S0x34a4: SSTORE v34bb, v38c5V34a4(0x0)
    0x38caS0x34a4: v38caV34a4(0x0) = CONST 
    0x38ccS0x34a4: MSTORE v38caV34a4(0x0), v34bb
    0x38cdS0x34a4: v38cdV34a4(0x20) = CONST 
    0x38cfS0x34a4: v38cfV34a4(0x0) = CONST 
    0x38d1S0x34a4: v38d1V34a4 = SHA3 v38cfV34a4(0x0), v38cdV34a4(0x20)
    0x38d4S0x34a4: v38d4V34a4 = ADD v38d1V34a4, v38c4V34a4
    0x38d6S0x34a4: v38d6V34a4(0x38df) = CONST 
    0x38dbS0x34a4: v38dbV34a4(0x3970) = CONST 
    0x38deS0x34a4: JUMP v38dbV34a4(0x3970)

    Begin block 0x3970B0x38c1B0x34a4
    prev=[0x38c1B0x34a4], succ=[0x3971B0x38c1B0x34a4]
    =================================

    Begin block 0x3971B0x38c1B0x34a4
    prev=[0x397aB0x38c1B0x34a4, 0x3970B0x38c1B0x34a4], succ=[0x397aB0x38c1B0x34a4, 0x45cfB0x38c1B0x34a4]
    =================================
    0x3971_0x0S0x38c1S0x34a4: v3971_0V38c1V34a4 = PHI v38d1V34a4, v3980V38c1V34a4
    0x3974S0x38c1S0x34a4: v3974V38c1V34a4 = GT v38d4V34a4, v3971_0V38c1V34a4
    0x3975S0x38c1S0x34a4: v3975V38c1V34a4 = ISZERO v3974V38c1V34a4
    0x3976S0x38c1S0x34a4: v3976V38c1V34a4(0x45cf) = CONST 
    0x3979S0x38c1S0x34a4: JUMPI v3976V38c1V34a4(0x45cf), v3975V38c1V34a4

    Begin block 0x397aB0x38c1B0x34a4
    prev=[0x3971B0x38c1B0x34a4], succ=[0x3971B0x38c1B0x34a4]
    =================================
    0x397aS0x38c1S0x34a4: v397aV38c1V34a4(0x0) = CONST 
    0x397a_0x0S0x38c1S0x34a4: v397a_0V38c1V34a4 = PHI v38d1V34a4, v3980V38c1V34a4
    0x397dS0x38c1S0x34a4: SSTORE v397a_0V38c1V34a4, v397aV38c1V34a4(0x0)
    0x397eS0x38c1S0x34a4: v397eV38c1V34a4(0x1) = CONST 
    0x3980S0x38c1S0x34a4: v3980V38c1V34a4 = ADD v397eV38c1V34a4(0x1), v397a_0V38c1V34a4
    0x3981S0x38c1S0x34a4: v3981V38c1V34a4(0x3971) = CONST 
    0x3984S0x38c1S0x34a4: JUMP v3981V38c1V34a4(0x3971)

    Begin block 0x45cfB0x38c1B0x34a4
    prev=[0x3971B0x38c1B0x34a4], succ=[0x38dfB0x34a4]
    =================================
    0x45d2S0x38c1S0x34a4: JUMP v38d6V34a4(0x38df)

    Begin block 0x38dfB0x34a4
    prev=[0x45cfB0x38c1B0x34a4], succ=[0x34c1]
    =================================
    0x38e1S0x34a4: JUMP v34b3(0x34c1)

    Begin block 0x34c1
    prev=[0x38dfB0x34a4], succ=[0x38c1B0x34c1]
    =================================
    0x34c2: v34c2(0x0) = CONST 
    0x34c6: MSTORE v34c2(0x0), vd39
    0x34c7: v34c7(0xc) = CONST 
    0x34c9: v34c9(0x20) = CONST 
    0x34cb: MSTORE v34c9(0x20), v34c7(0xc)
    0x34cc: v34cc(0x40) = CONST 
    0x34cf: v34cf = SHA3 v34c2(0x0), v34cc(0x40)
    0x34d1: v34d1(0x34da) = CONST 
    0x34d6: v34d6(0x38c1) = CONST 
    0x34d9: JUMP v34d6(0x38c1), v34c2(0x0), v34cf, v34d1(0x34da)

    Begin block 0x38c1B0x34c1
    prev=[0x34c1], succ=[0x3970B0x38c1B0x34c1]
    =================================
    0x38c4S0x34c1: v38c4V34c1 = SLOAD v34cf
    0x38c5S0x34c1: v38c5V34c1(0x0) = CONST 
    0x38c8S0x34c1: SSTORE v34cf, v38c5V34c1(0x0)
    0x38caS0x34c1: v38caV34c1(0x0) = CONST 
    0x38ccS0x34c1: MSTORE v38caV34c1(0x0), v34cf
    0x38cdS0x34c1: v38cdV34c1(0x20) = CONST 
    0x38cfS0x34c1: v38cfV34c1(0x0) = CONST 
    0x38d1S0x34c1: v38d1V34c1 = SHA3 v38cfV34c1(0x0), v38cdV34c1(0x20)
    0x38d4S0x34c1: v38d4V34c1 = ADD v38d1V34c1, v38c4V34c1
    0x38d6S0x34c1: v38d6V34c1(0x38df) = CONST 
    0x38dbS0x34c1: v38dbV34c1(0x3970) = CONST 
    0x38deS0x34c1: JUMP v38dbV34c1(0x3970)

    Begin block 0x3970B0x38c1B0x34c1
    prev=[0x38c1B0x34c1], succ=[0x3971B0x38c1B0x34c1]
    =================================

    Begin block 0x3971B0x38c1B0x34c1
    prev=[0x397aB0x38c1B0x34c1, 0x3970B0x38c1B0x34c1], succ=[0x397aB0x38c1B0x34c1, 0x45cfB0x38c1B0x34c1]
    =================================
    0x3971_0x0S0x38c1S0x34c1: v3971_0V38c1V34c1 = PHI v38d1V34c1, v3980V38c1V34c1
    0x3974S0x38c1S0x34c1: v3974V38c1V34c1 = GT v38d4V34c1, v3971_0V38c1V34c1
    0x3975S0x38c1S0x34c1: v3975V38c1V34c1 = ISZERO v3974V38c1V34c1
    0x3976S0x38c1S0x34c1: v3976V38c1V34c1(0x45cf) = CONST 
    0x3979S0x38c1S0x34c1: JUMPI v3976V38c1V34c1(0x45cf), v3975V38c1V34c1

    Begin block 0x397aB0x38c1B0x34c1
    prev=[0x3971B0x38c1B0x34c1], succ=[0x3971B0x38c1B0x34c1]
    =================================
    0x397aS0x38c1S0x34c1: v397aV38c1V34c1(0x0) = CONST 
    0x397a_0x0S0x38c1S0x34c1: v397a_0V38c1V34c1 = PHI v38d1V34c1, v3980V38c1V34c1
    0x397dS0x38c1S0x34c1: SSTORE v397a_0V38c1V34c1, v397aV38c1V34c1(0x0)
    0x397eS0x38c1S0x34c1: v397eV38c1V34c1(0x1) = CONST 
    0x3980S0x38c1S0x34c1: v3980V38c1V34c1 = ADD v397eV38c1V34c1(0x1), v397a_0V38c1V34c1
    0x3981S0x38c1S0x34c1: v3981V38c1V34c1(0x3971) = CONST 
    0x3984S0x38c1S0x34c1: JUMP v3981V38c1V34c1(0x3971)

    Begin block 0x45cfB0x38c1B0x34c1
    prev=[0x3971B0x38c1B0x34c1], succ=[0x38dfB0x34c1]
    =================================
    0x45d2S0x38c1S0x34c1: JUMP v38d6V34c1(0x38df)

    Begin block 0x38dfB0x34c1
    prev=[0x45cfB0x38c1B0x34c1], succ=[0x34da]
    =================================
    0x38e1S0x34c1: JUMP v34d1(0x34da)

    Begin block 0x34da
    prev=[0x38dfB0x34c1], succ=[0x38c1B0x34da]
    =================================
    0x34db: v34db(0x34e8) = CONST 
    0x34de: v34de(0x1) = CONST 
    0x34e1: v34e1 = ADD v34cf, v34de(0x1)
    0x34e2: v34e2(0x0) = CONST 
    0x34e4: v34e4(0x38c1) = CONST 
    0x34e7: JUMP v34e4(0x38c1), v34e2(0x0), v34e1, v34db(0x34e8)

    Begin block 0x38c1B0x34da
    prev=[0x34da], succ=[0x3970B0x38c1B0x34da]
    =================================
    0x38c4S0x34da: v38c4V34da = SLOAD v34e1
    0x38c5S0x34da: v38c5V34da(0x0) = CONST 
    0x38c8S0x34da: SSTORE v34e1, v38c5V34da(0x0)
    0x38caS0x34da: v38caV34da(0x0) = CONST 
    0x38ccS0x34da: MSTORE v38caV34da(0x0), v34e1
    0x38cdS0x34da: v38cdV34da(0x20) = CONST 
    0x38cfS0x34da: v38cfV34da(0x0) = CONST 
    0x38d1S0x34da: v38d1V34da = SHA3 v38cfV34da(0x0), v38cdV34da(0x20)
    0x38d4S0x34da: v38d4V34da = ADD v38d1V34da, v38c4V34da
    0x38d6S0x34da: v38d6V34da(0x38df) = CONST 
    0x38dbS0x34da: v38dbV34da(0x3970) = CONST 
    0x38deS0x34da: JUMP v38dbV34da(0x3970)

    Begin block 0x3970B0x38c1B0x34da
    prev=[0x38c1B0x34da], succ=[0x3971B0x38c1B0x34da]
    =================================

    Begin block 0x3971B0x38c1B0x34da
    prev=[0x397aB0x38c1B0x34da, 0x3970B0x38c1B0x34da], succ=[0x397aB0x38c1B0x34da, 0x45cfB0x38c1B0x34da]
    =================================
    0x3971_0x0S0x38c1S0x34da: v3971_0V38c1V34da = PHI v38d1V34da, v3980V38c1V34da
    0x3974S0x38c1S0x34da: v3974V38c1V34da = GT v38d4V34da, v3971_0V38c1V34da
    0x3975S0x38c1S0x34da: v3975V38c1V34da = ISZERO v3974V38c1V34da
    0x3976S0x38c1S0x34da: v3976V38c1V34da(0x45cf) = CONST 
    0x3979S0x38c1S0x34da: JUMPI v3976V38c1V34da(0x45cf), v3975V38c1V34da

    Begin block 0x397aB0x38c1B0x34da
    prev=[0x3971B0x38c1B0x34da], succ=[0x3971B0x38c1B0x34da]
    =================================
    0x397aS0x38c1S0x34da: v397aV38c1V34da(0x0) = CONST 
    0x397a_0x0S0x38c1S0x34da: v397a_0V38c1V34da = PHI v38d1V34da, v3980V38c1V34da
    0x397dS0x38c1S0x34da: SSTORE v397a_0V38c1V34da, v397aV38c1V34da(0x0)
    0x397eS0x38c1S0x34da: v397eV38c1V34da(0x1) = CONST 
    0x3980S0x38c1S0x34da: v3980V38c1V34da = ADD v397eV38c1V34da(0x1), v397a_0V38c1V34da
    0x3981S0x38c1S0x34da: v3981V38c1V34da(0x3971) = CONST 
    0x3984S0x38c1S0x34da: JUMP v3981V38c1V34da(0x3971)

    Begin block 0x45cfB0x38c1B0x34da
    prev=[0x3971B0x38c1B0x34da], succ=[0x38dfB0x34da]
    =================================
    0x45d2S0x38c1S0x34da: JUMP v38d6V34da(0x38df)

    Begin block 0x38dfB0x34da
    prev=[0x45cfB0x38c1B0x34da], succ=[0x34e8]
    =================================
    0x38e1S0x34da: JUMP v34db(0x34e8)

    Begin block 0x34e8
    prev=[0x38dfB0x34da], succ=[0x43ea]
    =================================
    0x34ea: v34ea(0x0) = CONST 
    0x34ec: v34ec(0x2) = CONST 
    0x34f1: v34f1 = ADD v34ec(0x2), v34cf
    0x34f4: SSTORE v34f1, v34ea(0x0)
    0x34f5: v34f5(0x40) = CONST 
    0x34f7: v34f7 = MLOAD v34f5(0x40)
    0x34fa: v34fa(0x4b6e5320f0df4b001291b8e1e2661f0aea72baa9c69260aaf5475b470254deff) = CONST 
    0x351c: LOG2 v34f7, v34ea(0x0), v34fa(0x4b6e5320f0df4b001291b8e1e2661f0aea72baa9c69260aaf5475b470254deff), vd39
    0x351e: JUMP v24b1(0x43ea)

    Begin block 0x43ea
    prev=[0x34e8], succ=[0x4175]
    =================================
    0x43ed: JUMP vd13(0x4175)

    Begin block 0x4175
    prev=[0x43ea], succ=[]
    =================================
    0x4176: STOP 

}

function isOwnerOf(address,uint256)() public {
    Begin block 0xd3e
    prev=[], succ=[0xd50, 0xd54]
    =================================
    0xd3f: vd3f(0x4196) = CONST 
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
    prev=[0xd3e], succ=[0x24b90xd3e]
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
    0xd66: vd66(0x24b9) = CONST 
    0xd69: JUMP vd66(0x24b9)

    Begin block 0x24b90xd3e
    prev=[0xd54], succ=[0x24d10xd3e, 0x24ca0xd3e]
    =================================
    0x24ba0xd3e: vd3e24ba(0x0) = CONST 
    0x24bc0xd3e: vd3e24bc(0x1) = CONST 
    0x24be0xd3e: vd3e24be(0x1) = CONST 
    0x24c00xd3e: vd3e24c0(0xa0) = CONST 
    0x24c20xd3e: vd3e24c2(0x10000000000000000000000000000000000000000) = SHL vd3e24c0(0xa0), vd3e24be(0x1)
    0x24c30xd3e: vd3e24c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd3e24c2(0x10000000000000000000000000000000000000000), vd3e24bc(0x1)
    0x24c50xd3e: vd3e24c5 = AND vd60, vd3e24c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x24c60xd3e: vd3e24c6(0x24d1) = CONST 
    0x24c90xd3e: JUMPI vd3e24c6(0x24d1), vd3e24c5

    Begin block 0x24d10xd3e
    prev=[0x24b90xd3e], succ=[0x44320xd3e]
    =================================
    0x24d30xd3e: vd3e24d3(0x0) = CONST 
    0x24d70xd3e: MSTORE vd3e24d3(0x0), vd65
    0x24d80xd3e: vd3e24d8(0x8) = CONST 
    0x24da0xd3e: vd3e24da(0x20) = CONST 
    0x24dc0xd3e: MSTORE vd3e24da(0x20), vd3e24d8(0x8)
    0x24dd0xd3e: vd3e24dd(0x40) = CONST 
    0x24e00xd3e: vd3e24e0 = SHA3 vd3e24d3(0x0), vd3e24dd(0x40)
    0x24e10xd3e: vd3e24e1 = SLOAD vd3e24e0
    0x24e20xd3e: vd3e24e2(0x1) = CONST 
    0x24e40xd3e: vd3e24e4(0x1) = CONST 
    0x24e60xd3e: vd3e24e6(0xa0) = CONST 
    0x24e80xd3e: vd3e24e8(0x10000000000000000000000000000000000000000) = SHL vd3e24e6(0xa0), vd3e24e4(0x1)
    0x24e90xd3e: vd3e24e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd3e24e8(0x10000000000000000000000000000000000000000), vd3e24e2(0x1)
    0x24ec0xd3e: vd3e24ec = AND vd3e24e9(0xffffffffffffffffffffffffffffffffffffffff), vd60
    0x24ee0xd3e: vd3e24ee = AND vd3e24e1, vd3e24e9(0xffffffffffffffffffffffffffffffffffffffff)
    0x24ef0xd3e: vd3e24ef = EQ vd3e24ee, vd3e24ec
    0x24f00xd3e: vd3e24f0(0x4432) = CONST 
    0x24f30xd3e: JUMP vd3e24f0(0x4432)

    Begin block 0x44320xd3e
    prev=[0x24d10xd3e], succ=[0x4196]
    =================================
    0x44370xd3e: JUMP vd3f(0x4196)

    Begin block 0x4196
    prev=[0x440d0xd3e, 0x44320xd3e], succ=[]
    =================================
    0x4196_0x0: v4196_0 = PHI vd3e24ef, vd3e24cb(0x0)
    0x4197: v4197(0x40) = CONST 
    0x419a: v419a = MLOAD v4197(0x40)
    0x419c: v419c = ISZERO v4196_0
    0x419d: v419d = ISZERO v419c
    0x419f: MSTORE v419a, v419d
    0x41a0: v41a0 = MLOAD v4197(0x40)
    0x41a4: v41a4(0x0) = SUB v419a, v41a0
    0x41a5: v41a5(0x20) = CONST 
    0x41a7: v41a7(0x20) = ADD v41a5(0x20), v41a4(0x0)
    0x41a9: RETURN v41a0, v41a7(0x20)

    Begin block 0x24ca0xd3e
    prev=[0x24b90xd3e], succ=[0x440d0xd3e]
    =================================
    0x24cb0xd3e: vd3e24cb(0x0) = CONST 
    0x24cd0xd3e: vd3e24cd(0x440d) = CONST 
    0x24d00xd3e: JUMP vd3e24cd(0x440d)

    Begin block 0x440d0xd3e
    prev=[0x24ca0xd3e], succ=[0x4196]
    =================================
    0x44120xd3e: JUMP vd3f(0x4196)

}

function isApprovedForAll(address,address)() public {
    Begin block 0xd6a
    prev=[], succ=[0xd7c, 0xd80]
    =================================
    0xd6b: vd6b(0x41c9) = CONST 
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
    prev=[0xd6a], succ=[0x24f40xd6a]
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
    0xd94: vd94(0x24f4) = CONST 
    0xd97: JUMP vd94(0x24f4)

    Begin block 0x24f40xd6a
    prev=[0xd80], succ=[0x41c9]
    =================================
    0x24f50xd6a: vd6a24f5(0x1) = CONST 
    0x24f70xd6a: vd6a24f7(0x1) = CONST 
    0x24f90xd6a: vd6a24f9(0xa0) = CONST 
    0x24fb0xd6a: vd6a24fb(0x10000000000000000000000000000000000000000) = SHL vd6a24f9(0xa0), vd6a24f7(0x1)
    0x24fc0xd6a: vd6a24fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd6a24fb(0x10000000000000000000000000000000000000000), vd6a24f5(0x1)
    0x24ff0xd6a: vd6a24ff = AND vd6a24fc(0xffffffffffffffffffffffffffffffffffffffff), vd8d
    0x25000xd6a: vd6a2500(0x0) = CONST 
    0x25040xd6a: MSTORE vd6a2500(0x0), vd6a24ff
    0x25050xd6a: vd6a2505(0x9) = CONST 
    0x25070xd6a: vd6a2507(0x20) = CONST 
    0x250b0xd6a: MSTORE vd6a2507(0x20), vd6a2505(0x9)
    0x250c0xd6a: vd6a250c(0x40) = CONST 
    0x25100xd6a: vd6a2510 = SHA3 vd6a2500(0x0), vd6a250c(0x40)
    0x25140xd6a: vd6a2514 = AND vd6a24fc(0xffffffffffffffffffffffffffffffffffffffff), vd93
    0x25160xd6a: MSTORE vd6a2500(0x0), vd6a2514
    0x251a0xd6a: MSTORE vd6a2507(0x20), vd6a2510
    0x251b0xd6a: vd6a251b = SHA3 vd6a2500(0x0), vd6a250c(0x40)
    0x251c0xd6a: vd6a251c = SLOAD vd6a251b
    0x251d0xd6a: vd6a251d(0xff) = CONST 
    0x251f0xd6a: vd6a251f = AND vd6a251d(0xff), vd6a251c
    0x25210xd6a: JUMP vd6b(0x41c9)

    Begin block 0x41c9
    prev=[0x24f40xd6a], succ=[]
    =================================
    0x41ca: v41ca(0x40) = CONST 
    0x41cd: v41cd = MLOAD v41ca(0x40)
    0x41cf: v41cf = ISZERO vd6a251f
    0x41d0: v41d0 = ISZERO v41cf
    0x41d2: MSTORE v41cd, v41d0
    0x41d3: v41d3 = MLOAD v41ca(0x40)
    0x41d7: v41d7(0x0) = SUB v41cd, v41d3
    0x41d8: v41d8(0x20) = CONST 
    0x41da: v41da(0x20) = ADD v41d8(0x20), v41d7(0x0)
    0x41dc: RETURN v41d3, v41da(0x20)

}

function safeTransferFrom(address,address,uint256,uint256,bytes)() public {
    Begin block 0xd98
    prev=[], succ=[0xdaa, 0xdae]
    =================================
    0xd99: vd99(0x41fc) = CONST 
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
    prev=[0xdff], succ=[0x2522]
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
    0xe57: ve57(0x2522) = CONST 
    0xe60: JUMP ve57(0x2522)

    Begin block 0x2522
    prev=[0xe20], succ=[0x2531, 0x2567]
    =================================
    0x2523: v2523(0x1) = CONST 
    0x2525: v2525(0x1) = CONST 
    0x2527: v2527(0xa0) = CONST 
    0x2529: v2529(0x10000000000000000000000000000000000000000) = SHL v2527(0xa0), v2525(0x1)
    0x252a: v252a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2529(0x10000000000000000000000000000000000000000), v2523(0x1)
    0x252c: v252c = AND vdc3, v252a(0xffffffffffffffffffffffffffffffffffffffff)
    0x252d: v252d(0x2567) = CONST 
    0x2530: JUMPI v252d(0x2567), v252c

    Begin block 0x2531
    prev=[0x2522], succ=[]
    =================================
    0x2531: v2531(0x40) = CONST 
    0x2533: v2533 = MLOAD v2531(0x40)
    0x2534: v2534(0x461bcd) = CONST 
    0x2538: v2538(0xe5) = CONST 
    0x253a: v253a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2538(0xe5), v2534(0x461bcd)
    0x253c: MSTORE v2533, v253a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x253d: v253d(0x4) = CONST 
    0x253f: v253f = ADD v253d(0x4), v2533
    0x2542: v2542(0x20) = CONST 
    0x2544: v2544 = ADD v2542(0x20), v253f
    0x2547: v2547(0x20) = SUB v2544, v253f
    0x2549: MSTORE v253f, v2547(0x20)
    0x254a: v254a(0x24) = CONST 
    0x254d: MSTORE v2544, v254a(0x24)
    0x254e: v254e(0x20) = CONST 
    0x2550: v2550 = ADD v254e(0x20), v2544
    0x2552: v2552(0x3ad6) = CONST 
    0x2555: v2555(0x24) = CONST 
    0x2558: CODECOPY v2550, v2552(0x3ad6), v2555(0x24)
    0x2559: v2559(0x40) = CONST 
    0x255b: v255b = ADD v2559(0x40), v2550
    0x255f: v255f(0x40) = CONST 
    0x2561: v2561 = MLOAD v255f(0x40)
    0x2564: v2564(0x84) = SUB v255b, v2561
    0x2566: REVERT v2561, v2564(0x84)

    Begin block 0x2567
    prev=[0x2522], succ=[0x2570, 0x25ad]
    =================================
    0x2569: v2569(0x1) = CONST 
    0x256b: v256b = EQ v2569(0x1), vdcf
    0x256c: v256c(0x25ad) = CONST 
    0x256f: JUMPI v256c(0x25ad), v256b

    Begin block 0x2570
    prev=[0x2567], succ=[]
    =================================
    0x2570: v2570(0x40) = CONST 
    0x2573: v2573 = MLOAD v2570(0x40)
    0x2574: v2574(0x461bcd) = CONST 
    0x2578: v2578(0xe5) = CONST 
    0x257a: v257a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2578(0xe5), v2574(0x461bcd)
    0x257c: MSTORE v2573, v257a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x257d: v257d(0x20) = CONST 
    0x257f: v257f(0x4) = CONST 
    0x2582: v2582 = ADD v2573, v257f(0x4)
    0x2583: MSTORE v2582, v257d(0x20)
    0x2584: v2584(0xe) = CONST 
    0x2586: v2586(0x24) = CONST 
    0x2589: v2589 = ADD v2573, v2586(0x24)
    0x258a: MSTORE v2589, v2584(0xe)
    0x258b: v258b(0x125b9d985b1a5908185b5bdd5b9d) = CONST 
    0x259a: v259a(0x92) = CONST 
    0x259c: v259c(0x496e76616c696420616d6f756e74000000000000000000000000000000000000) = SHL v259a(0x92), v258b(0x125b9d985b1a5908185b5bdd5b9d)
    0x259d: v259d(0x44) = CONST 
    0x25a0: v25a0 = ADD v2573, v259d(0x44)
    0x25a1: MSTORE v25a0, v259c(0x496e76616c696420616d6f756e74000000000000000000000000000000000000)
    0x25a3: v25a3 = MLOAD v2570(0x40)
    0x25a7: v25a7(0x0) = SUB v2573, v25a3
    0x25a8: v25a8(0x64) = CONST 
    0x25aa: v25aa(0x64) = ADD v25a8(0x64), v25a7(0x0)
    0x25ac: REVERT v25a3, v25aa(0x64)

    Begin block 0x25ad
    prev=[0x2567], succ=[0x25c9, 0x25bf]
    =================================
    0x25ae: v25ae(0x1) = CONST 
    0x25b0: v25b0(0x1) = CONST 
    0x25b2: v25b2(0xa0) = CONST 
    0x25b4: v25b4(0x10000000000000000000000000000000000000000) = SHL v25b2(0xa0), v25b0(0x1)
    0x25b5: v25b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25b4(0x10000000000000000000000000000000000000000), v25ae(0x1)
    0x25b7: v25b7 = AND vdba, v25b5(0xffffffffffffffffffffffffffffffffffffffff)
    0x25b8: v25b8 = CALLER 
    0x25b9: v25b9 = EQ v25b8, v25b7
    0x25bb: v25bb(0x25c9) = CONST 
    0x25be: JUMPI v25bb(0x25c9), v25b9

    Begin block 0x25c9
    prev=[0x25ad, 0x24f4B0x25bf], succ=[0x25ce, 0x2604]
    =================================
    0x25c9_0x0: v25c9_0 = PHI v25b9, v251fV25bf
    0x25ca: v25ca(0x2604) = CONST 
    0x25cd: JUMPI v25ca(0x2604), v25c9_0

    Begin block 0x25ce
    prev=[0x25c9], succ=[]
    =================================
    0x25ce: v25ce(0x40) = CONST 
    0x25d0: v25d0 = MLOAD v25ce(0x40)
    0x25d1: v25d1(0x461bcd) = CONST 
    0x25d5: v25d5(0xe5) = CONST 
    0x25d7: v25d7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v25d5(0xe5), v25d1(0x461bcd)
    0x25d9: MSTORE v25d0, v25d7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x25da: v25da(0x4) = CONST 
    0x25dc: v25dc = ADD v25da(0x4), v25d0
    0x25df: v25df(0x20) = CONST 
    0x25e1: v25e1 = ADD v25df(0x20), v25dc
    0x25e4: v25e4(0x20) = SUB v25e1, v25dc
    0x25e6: MSTORE v25dc, v25e4(0x20)
    0x25e7: v25e7(0x2d) = CONST 
    0x25ea: MSTORE v25e1, v25e7(0x2d)
    0x25eb: v25eb(0x20) = CONST 
    0x25ed: v25ed = ADD v25eb(0x20), v25e1
    0x25ef: v25ef(0x3afa) = CONST 
    0x25f2: v25f2(0x2d) = CONST 
    0x25f5: CODECOPY v25ed, v25ef(0x3afa), v25f2(0x2d)
    0x25f6: v25f6(0x40) = CONST 
    0x25f8: v25f8 = ADD v25f6(0x40), v25ed
    0x25fc: v25fc(0x40) = CONST 
    0x25fe: v25fe = MLOAD v25fc(0x40)
    0x2601: v2601(0x84) = SUB v25f8, v25fe
    0x2603: REVERT v25fe, v2601(0x84)

    Begin block 0x2604
    prev=[0x25c9], succ=[0x260e]
    =================================
    0x2605: v2605(0x260e) = CONST 
    0x260a: v260a(0x24b9) = CONST 
    0x260d: v260d_0 = CALLPRIVATE v260a(0x24b9), vdc9, vdba, v2605(0x260e)

    Begin block 0x260e
    prev=[0x2604], succ=[0x2613, 0x264f]
    =================================
    0x260f: v260f(0x264f) = CONST 
    0x2612: JUMPI v260f(0x264f), v260d_0

    Begin block 0x2613
    prev=[0x260e], succ=[]
    =================================
    0x2613: v2613(0x40) = CONST 
    0x2616: v2616 = MLOAD v2613(0x40)
    0x2617: v2617(0x461bcd) = CONST 
    0x261b: v261b(0xe5) = CONST 
    0x261d: v261d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v261b(0xe5), v2617(0x461bcd)
    0x261f: MSTORE v2616, v261d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2620: v2620(0x20) = CONST 
    0x2622: v2622(0x4) = CONST 
    0x2625: v2625 = ADD v2616, v2622(0x4)
    0x2626: MSTORE v2625, v2620(0x20)
    0x2627: v2627(0xd) = CONST 
    0x2629: v2629(0x24) = CONST 
    0x262c: v262c = ADD v2616, v2629(0x24)
    0x262d: MSTORE v262c, v2627(0xd)
    0x262e: v262e(0x2737ba103a34329037bbb732b9) = CONST 
    0x263c: v263c(0x99) = CONST 
    0x263e: v263e(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v263c(0x99), v262e(0x2737ba103a34329037bbb732b9)
    0x263f: v263f(0x44) = CONST 
    0x2642: v2642 = ADD v2616, v263f(0x44)
    0x2643: MSTORE v2642, v263e(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x2645: v2645 = MLOAD v2613(0x40)
    0x2649: v2649(0x0) = SUB v2616, v2645
    0x264a: v264a(0x64) = CONST 
    0x264c: v264c(0x64) = ADD v264a(0x64), v2649(0x0)
    0x264e: REVERT v2645, v264c(0x64)

    Begin block 0x264f
    prev=[0x260e], succ=[0x4457]
    =================================
    0x2650: v2650(0x0) = CONST 
    0x2654: MSTORE v2650(0x0), vdc9
    0x2655: v2655(0x8) = CONST 
    0x2657: v2657(0x20) = CONST 
    0x265b: MSTORE v2657(0x20), v2655(0x8)
    0x265c: v265c(0x40) = CONST 
    0x2661: v2661 = SHA3 v2650(0x0), v265c(0x40)
    0x2663: v2663 = SLOAD v2661
    0x2664: v2664(0x1) = CONST 
    0x2666: v2666(0x1) = CONST 
    0x2668: v2668(0xa0) = CONST 
    0x266a: v266a(0x10000000000000000000000000000000000000000) = SHL v2668(0xa0), v2666(0x1)
    0x266b: v266b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v266a(0x10000000000000000000000000000000000000000), v2664(0x1)
    0x266c: v266c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v266b(0xffffffffffffffffffffffffffffffffffffffff)
    0x266d: v266d = AND v266c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2663
    0x266e: v266e(0x1) = CONST 
    0x2670: v2670(0x1) = CONST 
    0x2672: v2672(0xa0) = CONST 
    0x2674: v2674(0x10000000000000000000000000000000000000000) = SHL v2672(0xa0), v2670(0x1)
    0x2675: v2675(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2674(0x10000000000000000000000000000000000000000), v266e(0x1)
    0x2678: v2678 = AND v2675(0xffffffffffffffffffffffffffffffffffffffff), vdc3
    0x267b: v267b = OR v2678, v266d
    0x267e: SSTORE v2661, v267b
    0x2680: v2680 = MLOAD v265c(0x40)
    0x2683: MSTORE v2680, vdc9
    0x2686: v2686 = ADD v2680, v2657(0x20)
    0x2689: MSTORE v2686, vdcf
    0x268b: v268b = MLOAD v265c(0x40)
    0x2690: v2690 = AND vdba, v2675(0xffffffffffffffffffffffffffffffffffffffff)
    0x2692: v2692 = CALLER 
    0x2694: v2694(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x26b9: v26b9(0x0) = SUB v2680, v268b
    0x26ba: v26ba(0x40) = ADD v26b9(0x0), v265c(0x40)
    0x26bc: LOG4 v268b, v26ba(0x40), v2694(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v2692, v2690, v2678
    0x26bd: v26bd(0x4457) = CONST 
    0x26c0: v26c0 = CALLER 
    0x26c6: v26c6(0x351f) = CONST 
    0x26c9: CALLPRIVATE v26c6(0x351f), ve33, vdcf, vdc9, vdc3, vdba, v26c0, v26bd(0x4457)

    Begin block 0x4457
    prev=[0x264f], succ=[0x41fc]
    =================================
    0x445d: JUMP vd99(0x41fc)

    Begin block 0x41fc
    prev=[0x4457], succ=[]
    =================================
    0x41fd: STOP 

    Begin block 0x25bf
    prev=[0x25ad], succ=[0x24f4B0x25bf]
    =================================
    0x25c0: v25c0(0x25c9) = CONST 
    0x25c4: v25c4 = CALLER 
    0x25c5: v25c5(0x24f4) = CONST 
    0x25c8: JUMP v25c5(0x24f4)

    Begin block 0x24f4B0x25bf
    prev=[0x25bf], succ=[0x25c9]
    =================================
    0x24f5S0x25bf: v24f5V25bf(0x1) = CONST 
    0x24f7S0x25bf: v24f7V25bf(0x1) = CONST 
    0x24f9S0x25bf: v24f9V25bf(0xa0) = CONST 
    0x24fbS0x25bf: v24fbV25bf(0x10000000000000000000000000000000000000000) = SHL v24f9V25bf(0xa0), v24f7V25bf(0x1)
    0x24fcS0x25bf: v24fcV25bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24fbV25bf(0x10000000000000000000000000000000000000000), v24f5V25bf(0x1)
    0x24ffS0x25bf: v24ffV25bf = AND v24fcV25bf(0xffffffffffffffffffffffffffffffffffffffff), vdba
    0x2500S0x25bf: v2500V25bf(0x0) = CONST 
    0x2504S0x25bf: MSTORE v2500V25bf(0x0), v24ffV25bf
    0x2505S0x25bf: v2505V25bf(0x9) = CONST 
    0x2507S0x25bf: v2507V25bf(0x20) = CONST 
    0x250bS0x25bf: MSTORE v2507V25bf(0x20), v2505V25bf(0x9)
    0x250cS0x25bf: v250cV25bf(0x40) = CONST 
    0x2510S0x25bf: v2510V25bf = SHA3 v2500V25bf(0x0), v250cV25bf(0x40)
    0x2514S0x25bf: v2514V25bf = AND v24fcV25bf(0xffffffffffffffffffffffffffffffffffffffff), v25c4
    0x2516S0x25bf: MSTORE v2500V25bf(0x0), v2514V25bf
    0x251aS0x25bf: MSTORE v2507V25bf(0x20), v2510V25bf
    0x251bS0x25bf: v251bV25bf = SHA3 v2500V25bf(0x0), v250cV25bf(0x40)
    0x251cS0x25bf: v251cV25bf = SLOAD v251bV25bf
    0x251dS0x25bf: v251dV25bf(0xff) = CONST 
    0x251fS0x25bf: v251fV25bf = AND v251dV25bf(0xff), v251cV25bf
    0x2521S0x25bf: JUMP v25c0(0x25c9)

}

function starNFTCount()() public {
    Begin block 0xe61
    prev=[], succ=[0x26ca]
    =================================
    0xe62: ve62(0x421d) = CONST 
    0xe65: ve65(0x26ca) = CONST 
    0xe68: JUMP ve65(0x26ca)

    Begin block 0x26ca
    prev=[0xe61], succ=[0x421d]
    =================================
    0x26cb: v26cb(0x7) = CONST 
    0x26cd: v26cd = SLOAD v26cb(0x7)
    0x26cf: JUMP ve62(0x421d)

    Begin block 0x421d
    prev=[0x26ca], succ=[]
    =================================
    0x421e: v421e(0x40) = CONST 
    0x4221: v4221 = MLOAD v421e(0x40)
    0x4224: MSTORE v4221, v26cd
    0x4225: v4225 = MLOAD v421e(0x40)
    0x4229: v4229(0x0) = SUB v4221, v4225
    0x422a: v422a(0x20) = CONST 
    0x422c: v422c(0x20) = ADD v422a(0x20), v4229(0x0)
    0x422e: RETURN v4225, v422c(0x20)

}

