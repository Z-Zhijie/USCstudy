function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x5498]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x5434: v5434(0x5498) = CONST 
    0x5435: JUMPI v5434(0x5498), v8

    Begin block 0xd
    prev=[0x0], succ=[0x549b, 0x27]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0xe0) = CONST 
    0x14: v14(0x2) = CONST 
    0x16: v16(0x100000000000000000000000000000000000000000000000000000000) = EXP v14(0x2), v12(0xe0)
    0x17: v17(0x0) = CONST 
    0x19: v19 = CALLDATALOAD v17(0x0)
    0x1a: v1a = DIV v19, v16(0x100000000000000000000000000000000000000000000000000000000)
    0x1b: v1b = AND v1a, vd(0xffffffff)
    0x1c: v1c(0x6fdde03) = CONST 
    0x22: v22 = EQ v1b, v1c(0x6fdde03)
    0x5436: v5436(0x549b) = CONST 
    0x5437: JUMPI v5436(0x549b), v22

    Begin block 0x549b
    prev=[0xd, 0x12f], succ=[]
    =================================
    0x549c: v549c(0x23c) = CONST 
    0x549d: CALLPRIVATE v549c(0x23c)

    Begin block 0x27
    prev=[0xd], succ=[0x549e, 0x32]
    =================================
    0x28: v28(0x95ea7b3) = CONST 
    0x2d: v2d = EQ v28(0x95ea7b3), v1b
    0x5438: v5438(0x549e) = CONST 
    0x5439: JUMPI v5438(0x549e), v2d

    Begin block 0x549e
    prev=[0x27], succ=[]
    =================================
    0x549f: v549f(0x2c6) = CONST 
    0x54a0: CALLPRIVATE v549f(0x2c6)

    Begin block 0x32
    prev=[0x27], succ=[0x54a1, 0x3d]
    =================================
    0x33: v33(0xd4b8208) = CONST 
    0x38: v38 = EQ v33(0xd4b8208), v1b
    0x543a: v543a(0x54a1) = CONST 
    0x543b: JUMPI v543a(0x54a1), v38

    Begin block 0x54a1
    prev=[0x32], succ=[]
    =================================
    0x54a2: v54a2(0x2fe) = CONST 
    0x54a3: CALLPRIVATE v54a2(0x2fe)

    Begin block 0x3d
    prev=[0x32], succ=[0x48, 0x54a4]
    =================================
    0x3e: v3e(0x18160ddd) = CONST 
    0x43: v43 = EQ v3e(0x18160ddd), v1b
    0x543c: v543c(0x54a4) = CONST 
    0x543d: JUMPI v543c(0x54a4), v43

    Begin block 0x48
    prev=[0x3d], succ=[0x54a7, 0x53]
    =================================
    0x49: v49(0x1fc1e25f) = CONST 
    0x4e: v4e = EQ v49(0x1fc1e25f), v1b
    0x543e: v543e(0x54a7) = CONST 
    0x543f: JUMPI v543e(0x54a7), v4e

    Begin block 0x54a7
    prev=[0x48], succ=[]
    =================================
    0x54a8: v54a8(0x34b) = CONST 
    0x54a9: CALLPRIVATE v54a8(0x34b)

    Begin block 0x53
    prev=[0x48], succ=[0x54aa, 0x5e]
    =================================
    0x54: v54(0x21bacf28) = CONST 
    0x59: v59 = EQ v54(0x21bacf28), v1b
    0x5440: v5440(0x54aa) = CONST 
    0x5441: JUMPI v5440(0x54aa), v59

    Begin block 0x54aa
    prev=[0x53], succ=[]
    =================================
    0x54ab: v54ab(0x36c) = CONST 
    0x54ac: CALLPRIVATE v54ab(0x36c)

    Begin block 0x5e
    prev=[0x53], succ=[0x54ad, 0x69]
    =================================
    0x5f: v5f(0x23b872dd) = CONST 
    0x64: v64 = EQ v5f(0x23b872dd), v1b
    0x5442: v5442(0x54ad) = CONST 
    0x5443: JUMPI v5442(0x54ad), v64

    Begin block 0x54ad
    prev=[0x5e], succ=[]
    =================================
    0x54ae: v54ae(0x381) = CONST 
    0x54af: CALLPRIVATE v54ae(0x381)

    Begin block 0x69
    prev=[0x5e], succ=[0x74, 0x54b0]
    =================================
    0x6a: v6a(0x313ce567) = CONST 
    0x6f: v6f = EQ v6a(0x313ce567), v1b
    0x5444: v5444(0x54b0) = CONST 
    0x5445: JUMPI v5444(0x54b0), v6f

    Begin block 0x74
    prev=[0x69], succ=[0x54b3, 0x7f]
    =================================
    0x75: v75(0x3af32abf) = CONST 
    0x7a: v7a = EQ v75(0x3af32abf), v1b
    0x5446: v5446(0x54b3) = CONST 
    0x5447: JUMPI v5446(0x54b3), v7a

    Begin block 0x54b3
    prev=[0x74], succ=[]
    =================================
    0x54b4: v54b4(0x3d6) = CONST 
    0x54b5: CALLPRIVATE v54b4(0x3d6)

    Begin block 0x7f
    prev=[0x74], succ=[0x54b6, 0x8a]
    =================================
    0x80: v80(0x3f4ba83a) = CONST 
    0x85: v85 = EQ v80(0x3f4ba83a), v1b
    0x5448: v5448(0x54b6) = CONST 
    0x5449: JUMPI v5448(0x54b6), v85

    Begin block 0x54b6
    prev=[0x7f], succ=[]
    =================================
    0x54b7: v54b7(0x3f7) = CONST 
    0x54b8: CALLPRIVATE v54b7(0x3f7)

    Begin block 0x8a
    prev=[0x7f], succ=[0x54b9, 0x95]
    =================================
    0x8b: v8b(0x40c10f19) = CONST 
    0x90: v90 = EQ v8b(0x40c10f19), v1b
    0x544a: v544a(0x54b9) = CONST 
    0x544b: JUMPI v544a(0x54b9), v90

    Begin block 0x54b9
    prev=[0x8a], succ=[]
    =================================
    0x54ba: v54ba(0x40c) = CONST 
    0x54bb: CALLPRIVATE v54ba(0x40c)

    Begin block 0x95
    prev=[0x8a], succ=[0xa0, 0x54bc]
    =================================
    0x96: v96(0x42966c68) = CONST 
    0x9b: v9b = EQ v96(0x42966c68), v1b
    0x544c: v544c(0x54bc) = CONST 
    0x544d: JUMPI v544c(0x54bc), v9b

    Begin block 0xa0
    prev=[0x95], succ=[0x54bf, 0xab]
    =================================
    0xa1: va1(0x4e71e0c8) = CONST 
    0xa6: va6 = EQ va1(0x4e71e0c8), v1b
    0x544e: v544e(0x54bf) = CONST 
    0x544f: JUMPI v544e(0x54bf), va6

    Begin block 0x54bf
    prev=[0xa0], succ=[]
    =================================
    0x54c0: v54c0(0x448) = CONST 
    0x54c1: CALLPRIVATE v54c0(0x448)

    Begin block 0xab
    prev=[0xa0], succ=[0x54c2, 0xb6]
    =================================
    0xac: vac(0x5bae9ce9) = CONST 
    0xb1: vb1 = EQ vac(0x5bae9ce9), v1b
    0x5450: v5450(0x54c2) = CONST 
    0x5451: JUMPI v5450(0x54c2), vb1

    Begin block 0x54c2
    prev=[0xab], succ=[]
    =================================
    0x54c3: v54c3(0x45d) = CONST 
    0x54c4: CALLPRIVATE v54c3(0x45d)

    Begin block 0xb6
    prev=[0xab], succ=[0x54c5, 0xc1]
    =================================
    0xb7: vb7(0x5c975abb) = CONST 
    0xbc: vbc = EQ vb7(0x5c975abb), v1b
    0x5452: v5452(0x54c5) = CONST 
    0x5453: JUMPI v5452(0x54c5), vbc

    Begin block 0x54c5
    prev=[0xb6], succ=[]
    =================================
    0x54c6: v54c6(0x472) = CONST 
    0x54c7: CALLPRIVATE v54c6(0x472)

    Begin block 0xc1
    prev=[0xb6], succ=[0x54c8, 0xcc]
    =================================
    0xc2: vc2(0x66188463) = CONST 
    0xc7: vc7 = EQ vc2(0x66188463), v1b
    0x5454: v5454(0x54c8) = CONST 
    0x5455: JUMPI v5454(0x54c8), vc7

    Begin block 0x54c8
    prev=[0xc1], succ=[]
    =================================
    0x54c9: v54c9(0x487) = CONST 
    0x54ca: CALLPRIVATE v54c9(0x487)

    Begin block 0xcc
    prev=[0xc1], succ=[0x54cb, 0xd7]
    =================================
    0xcd: vcd(0x662f94c0) = CONST 
    0xd2: vd2 = EQ vcd(0x662f94c0), v1b
    0x5456: v5456(0x54cb) = CONST 
    0x5457: JUMPI v5456(0x54cb), vd2

    Begin block 0x54cb
    prev=[0xcc], succ=[]
    =================================
    0x54cc: v54cc(0x4ab) = CONST 
    0x54cd: CALLPRIVATE v54cc(0x4ab)

    Begin block 0xd7
    prev=[0xcc], succ=[0x54ce, 0xe2]
    =================================
    0xd8: vd8(0x67d407df) = CONST 
    0xdd: vdd = EQ vd8(0x67d407df), v1b
    0x5458: v5458(0x54ce) = CONST 
    0x5459: JUMPI v5458(0x54ce), vdd

    Begin block 0x54ce
    prev=[0xd7], succ=[]
    =================================
    0x54cf: v54cf(0x4cc) = CONST 
    0x54d0: CALLPRIVATE v54cf(0x4cc)

    Begin block 0xe2
    prev=[0xd7], succ=[0x54d1, 0xed]
    =================================
    0xe3: ve3(0x6ad26611) = CONST 
    0xe8: ve8 = EQ ve3(0x6ad26611), v1b
    0x545a: v545a(0x54d1) = CONST 
    0x545b: JUMPI v545a(0x54d1), ve8

    Begin block 0x54d1
    prev=[0xe2], succ=[]
    =================================
    0x54d2: v54d2(0x4ed) = CONST 
    0x54d3: CALLPRIVATE v54d2(0x4ed)

    Begin block 0xed
    prev=[0xe2], succ=[0x54d4, 0xf8]
    =================================
    0xee: vee(0x70a08231) = CONST 
    0xf3: vf3 = EQ vee(0x70a08231), v1b
    0x545c: v545c(0x54d4) = CONST 
    0x545d: JUMPI v545c(0x54d4), vf3

    Begin block 0x54d4
    prev=[0xed], succ=[]
    =================================
    0x54d5: v54d5(0x50e) = CONST 
    0x54d6: CALLPRIVATE v54d5(0x50e)

    Begin block 0xf8
    prev=[0xed], succ=[0x54d7, 0x103]
    =================================
    0xf9: vf9(0x72b7f893) = CONST 
    0xfe: vfe = EQ vf9(0x72b7f893), v1b
    0x545e: v545e(0x54d7) = CONST 
    0x545f: JUMPI v545e(0x54d7), vfe

    Begin block 0x54d7
    prev=[0xf8], succ=[]
    =================================
    0x54d8: v54d8(0x52f) = CONST 
    0x54d9: CALLPRIVATE v54d8(0x52f)

    Begin block 0x103
    prev=[0xf8], succ=[0x54da, 0x10e]
    =================================
    0x104: v104(0x8456cb59) = CONST 
    0x109: v109 = EQ v104(0x8456cb59), v1b
    0x5460: v5460(0x54da) = CONST 
    0x5461: JUMPI v5460(0x54da), v109

    Begin block 0x54da
    prev=[0x103], succ=[]
    =================================
    0x54db: v54db(0x5a1) = CONST 
    0x54dc: CALLPRIVATE v54db(0x5a1)

    Begin block 0x10e
    prev=[0x103], succ=[0x54dd, 0x119]
    =================================
    0x10f: v10f(0x873ab2ce) = CONST 
    0x114: v114 = EQ v10f(0x873ab2ce), v1b
    0x5462: v5462(0x54dd) = CONST 
    0x5463: JUMPI v5462(0x54dd), v114

    Begin block 0x54dd
    prev=[0x10e], succ=[]
    =================================
    0x54de: v54de(0x5b6) = CONST 
    0x54df: CALLPRIVATE v54de(0x5b6)

    Begin block 0x119
    prev=[0x10e], succ=[0x54e0, 0x124]
    =================================
    0x11a: v11a(0x88fa2617) = CONST 
    0x11f: v11f = EQ v11a(0x88fa2617), v1b
    0x5464: v5464(0x54e0) = CONST 
    0x5465: JUMPI v5464(0x54e0), v11f

    Begin block 0x54e0
    prev=[0x119], succ=[]
    =================================
    0x54e1: v54e1(0x5d7) = CONST 
    0x54e2: CALLPRIVATE v54e1(0x5d7)

    Begin block 0x124
    prev=[0x119], succ=[0x54e3, 0x12f]
    =================================
    0x125: v125(0x8da5cb5b) = CONST 
    0x12a: v12a = EQ v125(0x8da5cb5b), v1b
    0x5466: v5466(0x54e3) = CONST 
    0x5467: JUMPI v5466(0x54e3), v12a

    Begin block 0x54e3
    prev=[0x124], succ=[]
    =================================
    0x54e4: v54e4(0x5ec) = CONST 
    0x54e5: CALLPRIVATE v54e4(0x5ec)

    Begin block 0x12f
    prev=[0x124], succ=[0x549b, 0x13a]
    =================================
    0x130: v130(0x95d89b41) = CONST 
    0x135: v135 = EQ v130(0x95d89b41), v1b
    0x5468: v5468(0x549b) = CONST 
    0x5469: JUMPI v5468(0x549b), v135

    Begin block 0x13a
    prev=[0x12f], succ=[0x54e6, 0x145]
    =================================
    0x13b: v13b(0x9d36b5c4) = CONST 
    0x140: v140 = EQ v13b(0x9d36b5c4), v1b
    0x546a: v546a(0x54e6) = CONST 
    0x546b: JUMPI v546a(0x54e6), v140

    Begin block 0x54e6
    prev=[0x13a], succ=[]
    =================================
    0x54e7: v54e7(0x61d) = CONST 
    0x54e8: CALLPRIVATE v54e7(0x61d)

    Begin block 0x145
    prev=[0x13a], succ=[0x54e9, 0x150]
    =================================
    0x146: v146(0x9dec2189) = CONST 
    0x14b: v14b = EQ v146(0x9dec2189), v1b
    0x546c: v546c(0x54e9) = CONST 
    0x546d: JUMPI v546c(0x54e9), v14b

    Begin block 0x54e9
    prev=[0x145], succ=[]
    =================================
    0x54ea: v54ea(0x632) = CONST 
    0x54eb: CALLPRIVATE v54ea(0x632)

    Begin block 0x150
    prev=[0x145], succ=[0x54ec, 0x15b]
    =================================
    0x151: v151(0xa69df4b5) = CONST 
    0x156: v156 = EQ v151(0xa69df4b5), v1b
    0x546e: v546e(0x54ec) = CONST 
    0x546f: JUMPI v546e(0x54ec), v156

    Begin block 0x54ec
    prev=[0x150], succ=[]
    =================================
    0x54ed: v54ed(0x65c) = CONST 
    0x54ee: CALLPRIVATE v54ed(0x65c)

    Begin block 0x15b
    prev=[0x150], succ=[0x54ef, 0x166]
    =================================
    0x15c: v15c(0xa9059cbb) = CONST 
    0x161: v161 = EQ v15c(0xa9059cbb), v1b
    0x5470: v5470(0x54ef) = CONST 
    0x5471: JUMPI v5470(0x54ef), v161

    Begin block 0x54ef
    prev=[0x15b], succ=[]
    =================================
    0x54f0: v54f0(0x671) = CONST 
    0x54f1: CALLPRIVATE v54f0(0x671)

    Begin block 0x166
    prev=[0x15b], succ=[0x54f2, 0x171]
    =================================
    0x167: v167(0xabcb9934) = CONST 
    0x16c: v16c = EQ v167(0xabcb9934), v1b
    0x5472: v5472(0x54f2) = CONST 
    0x5473: JUMPI v5472(0x54f2), v16c

    Begin block 0x54f2
    prev=[0x166], succ=[]
    =================================
    0x54f3: v54f3(0x695) = CONST 
    0x54f4: CALLPRIVATE v54f3(0x695)

    Begin block 0x171
    prev=[0x166], succ=[0x54f5, 0x17c]
    =================================
    0x172: v172(0xb199efb5) = CONST 
    0x177: v177 = EQ v172(0xb199efb5), v1b
    0x5474: v5474(0x54f5) = CONST 
    0x5475: JUMPI v5474(0x54f5), v177

    Begin block 0x54f5
    prev=[0x171], succ=[]
    =================================
    0x54f6: v54f6(0x6b6) = CONST 
    0x54f7: CALLPRIVATE v54f6(0x6b6)

    Begin block 0x17c
    prev=[0x171], succ=[0x54f8, 0x187]
    =================================
    0x17d: v17d(0xb88c9148) = CONST 
    0x182: v182 = EQ v17d(0xb88c9148), v1b
    0x5476: v5476(0x54f8) = CONST 
    0x5477: JUMPI v5476(0x54f8), v182

    Begin block 0x54f8
    prev=[0x17c], succ=[]
    =================================
    0x54f9: v54f9(0x6cb) = CONST 
    0x54fa: CALLPRIVATE v54f9(0x6cb)

    Begin block 0x187
    prev=[0x17c], succ=[0x54fb, 0x192]
    =================================
    0x188: v188(0xba6f4ab0) = CONST 
    0x18d: v18d = EQ v188(0xba6f4ab0), v1b
    0x5478: v5478(0x54fb) = CONST 
    0x5479: JUMPI v5478(0x54fb), v18d

    Begin block 0x54fb
    prev=[0x187], succ=[]
    =================================
    0x54fc: v54fc(0x6ec) = CONST 
    0x54fd: CALLPRIVATE v54fc(0x6ec)

    Begin block 0x192
    prev=[0x187], succ=[0x54fe, 0x19d]
    =================================
    0x193: v193(0xbf4b72e3) = CONST 
    0x198: v198 = EQ v193(0xbf4b72e3), v1b
    0x547a: v547a(0x54fe) = CONST 
    0x547b: JUMPI v547a(0x54fe), v198

    Begin block 0x54fe
    prev=[0x192], succ=[]
    =================================
    0x54ff: v54ff(0x710) = CONST 
    0x5500: CALLPRIVATE v54ff(0x710)

    Begin block 0x19d
    prev=[0x192], succ=[0x5501, 0x1a8]
    =================================
    0x19e: v19e(0xc534ba4b) = CONST 
    0x1a3: v1a3 = EQ v19e(0xc534ba4b), v1b
    0x547c: v547c(0x5501) = CONST 
    0x547d: JUMPI v547c(0x5501), v1a3

    Begin block 0x5501
    prev=[0x19d], succ=[]
    =================================
    0x5502: v5502(0x73a) = CONST 
    0x5503: CALLPRIVATE v5502(0x73a)

    Begin block 0x1a8
    prev=[0x19d], succ=[0x5504, 0x1b3]
    =================================
    0x1a9: v1a9(0xc93a6c84) = CONST 
    0x1ae: v1ae = EQ v1a9(0xc93a6c84), v1b
    0x547e: v547e(0x5504) = CONST 
    0x547f: JUMPI v547e(0x5504), v1ae

    Begin block 0x5504
    prev=[0x1a8], succ=[]
    =================================
    0x5505: v5505(0x75e) = CONST 
    0x5506: CALLPRIVATE v5505(0x75e)

    Begin block 0x1b3
    prev=[0x1a8], succ=[0x5507, 0x1be]
    =================================
    0x1b4: v1b4(0xcde0a4f8) = CONST 
    0x1b9: v1b9 = EQ v1b4(0xcde0a4f8), v1b
    0x5480: v5480(0x5507) = CONST 
    0x5481: JUMPI v5480(0x5507), v1b9

    Begin block 0x5507
    prev=[0x1b3], succ=[]
    =================================
    0x5508: v5508(0x776) = CONST 
    0x5509: CALLPRIVATE v5508(0x776)

    Begin block 0x1be
    prev=[0x1b3], succ=[0x550a, 0x1c9]
    =================================
    0x1bf: v1bf(0xd73dd623) = CONST 
    0x1c4: v1c4 = EQ v1bf(0xd73dd623), v1b
    0x5482: v5482(0x550a) = CONST 
    0x5483: JUMPI v5482(0x550a), v1c4

    Begin block 0x550a
    prev=[0x1be], succ=[]
    =================================
    0x550b: v550b(0x797) = CONST 
    0x550c: CALLPRIVATE v550b(0x797)

    Begin block 0x1c9
    prev=[0x1be], succ=[0x550d, 0x1d4]
    =================================
    0x1ca: v1ca(0xd76f288f) = CONST 
    0x1cf: v1cf = EQ v1ca(0xd76f288f), v1b
    0x5484: v5484(0x550d) = CONST 
    0x5485: JUMPI v5484(0x550d), v1cf

    Begin block 0x550d
    prev=[0x1c9], succ=[]
    =================================
    0x550e: v550e(0x7bb) = CONST 
    0x550f: CALLPRIVATE v550e(0x7bb)

    Begin block 0x1d4
    prev=[0x1c9], succ=[0x5510, 0x1df]
    =================================
    0x1d5: v1d5(0xdd62ed3e) = CONST 
    0x1da: v1da = EQ v1d5(0xdd62ed3e), v1b
    0x5486: v5486(0x5510) = CONST 
    0x5487: JUMPI v5486(0x5510), v1da

    Begin block 0x5510
    prev=[0x1d4], succ=[]
    =================================
    0x5511: v5511(0x7e5) = CONST 
    0x5512: CALLPRIVATE v5511(0x7e5)

    Begin block 0x1df
    prev=[0x1d4], succ=[0x5513, 0x1ea]
    =================================
    0x1e0: v1e0(0xdd8fee14) = CONST 
    0x1e5: v1e5 = EQ v1e0(0xdd8fee14), v1b
    0x5488: v5488(0x5513) = CONST 
    0x5489: JUMPI v5488(0x5513), v1e5

    Begin block 0x5513
    prev=[0x1df], succ=[]
    =================================
    0x5514: v5514(0x80c) = CONST 
    0x5515: CALLPRIVATE v5514(0x80c)

    Begin block 0x1ea
    prev=[0x1df], succ=[0x5516, 0x1f5]
    =================================
    0x1eb: v1eb(0xde08a6d8) = CONST 
    0x1f0: v1f0 = EQ v1eb(0xde08a6d8), v1b
    0x548a: v548a(0x5516) = CONST 
    0x548b: JUMPI v548a(0x5516), v1f0

    Begin block 0x5516
    prev=[0x1ea], succ=[]
    =================================
    0x5517: v5517(0x821) = CONST 
    0x5518: CALLPRIVATE v5517(0x821)

    Begin block 0x1f5
    prev=[0x1ea], succ=[0x5519, 0x200]
    =================================
    0x1f6: v1f6(0xe30c3978) = CONST 
    0x1fb: v1fb = EQ v1f6(0xe30c3978), v1b
    0x548c: v548c(0x5519) = CONST 
    0x548d: JUMPI v548c(0x5519), v1fb

    Begin block 0x5519
    prev=[0x1f5], succ=[]
    =================================
    0x551a: v551a(0x893) = CONST 
    0x551b: CALLPRIVATE v551a(0x893)

    Begin block 0x200
    prev=[0x1f5], succ=[0x551c, 0x20b]
    =================================
    0x201: v201(0xe55156b5) = CONST 
    0x206: v206 = EQ v201(0xe55156b5), v1b
    0x548e: v548e(0x551c) = CONST 
    0x548f: JUMPI v548e(0x551c), v206

    Begin block 0x551c
    prev=[0x200], succ=[]
    =================================
    0x551d: v551d(0x8a8) = CONST 
    0x551e: CALLPRIVATE v551d(0x8a8)

    Begin block 0x20b
    prev=[0x200], succ=[0x551f, 0x216]
    =================================
    0x20c: v20c(0xf0fe3d68) = CONST 
    0x211: v211 = EQ v20c(0xf0fe3d68), v1b
    0x5490: v5490(0x551f) = CONST 
    0x5491: JUMPI v5490(0x551f), v211

    Begin block 0x551f
    prev=[0x20b], succ=[]
    =================================
    0x5520: v5520(0x8cc) = CONST 
    0x5521: CALLPRIVATE v5520(0x8cc)

    Begin block 0x216
    prev=[0x20b], succ=[0x5522, 0x221]
    =================================
    0x217: v217(0xf2fde38b) = CONST 
    0x21c: v21c = EQ v217(0xf2fde38b), v1b
    0x5492: v5492(0x5522) = CONST 
    0x5493: JUMPI v5492(0x5522), v21c

    Begin block 0x5522
    prev=[0x216], succ=[]
    =================================
    0x5523: v5523(0x93e) = CONST 
    0x5524: CALLPRIVATE v5523(0x93e)

    Begin block 0x221
    prev=[0x216], succ=[0x5525, 0x22c]
    =================================
    0x222: v222(0xf7fd3d01) = CONST 
    0x227: v227 = EQ v222(0xf7fd3d01), v1b
    0x5494: v5494(0x5525) = CONST 
    0x5495: JUMPI v5494(0x5525), v227

    Begin block 0x5525
    prev=[0x221], succ=[]
    =================================
    0x5526: v5526(0x95f) = CONST 
    0x5527: CALLPRIVATE v5526(0x95f)

    Begin block 0x22c
    prev=[0x221], succ=[0x5498, 0x5528]
    =================================
    0x22d: v22d(0xf83d08ba) = CONST 
    0x232: v232 = EQ v22d(0xf83d08ba), v1b
    0x5496: v5496(0x5528) = CONST 
    0x5497: JUMPI v5496(0x5528), v232

    Begin block 0x5498
    prev=[0x0, 0x22c], succ=[]
    =================================
    0x5499: v5499(0x237) = CONST 
    0x549a: CALLPRIVATE v5499(0x237)

    Begin block 0x5528
    prev=[0x22c], succ=[]
    =================================
    0x5529: v5529(0x977) = CONST 
    0x552a: CALLPRIVATE v5529(0x977)

    Begin block 0x54bc
    prev=[0x95], succ=[]
    =================================
    0x54bd: v54bd(0x430) = CONST 
    0x54be: CALLPRIVATE v54bd(0x430)

    Begin block 0x54b0
    prev=[0x69], succ=[]
    =================================
    0x54b1: v54b1(0x3ab) = CONST 
    0x54b2: CALLPRIVATE v54b1(0x3ab)

    Begin block 0x54a4
    prev=[0x3d], succ=[]
    =================================
    0x54a5: v54a5(0x324) = CONST 
    0x54a6: CALLPRIVATE v54a5(0x324)

}

function 0x1217(0x1217arg0x0) private {
    Begin block 0x1217
    prev=[], succ=[0x1268, 0x11320x1217]
    =================================
    0x1218: v1218(0x0) = CONST 
    0x121a: v121a(0x4) = CONST 
    0x121c: v121c(0x0) = CONST 
    0x121f: v121f = SLOAD v121a(0x4)
    0x1221: v1221(0x100) = CONST 
    0x1224: v1224(0x1) = EXP v1221(0x100), v121c(0x0)
    0x1226: v1226 = DIV v121f, v1224(0x1)
    0x1227: v1227(0x1) = CONST 
    0x1229: v1229(0xa0) = CONST 
    0x122b: v122b(0x2) = CONST 
    0x122d: v122d(0x10000000000000000000000000000000000000000) = EXP v122b(0x2), v1229(0xa0)
    0x122e: v122e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v122d(0x10000000000000000000000000000000000000000), v1227(0x1)
    0x122f: v122f = AND v122e(0xffffffffffffffffffffffffffffffffffffffff), v1226
    0x1230: v1230(0x1) = CONST 
    0x1232: v1232(0xa0) = CONST 
    0x1234: v1234(0x2) = CONST 
    0x1236: v1236(0x10000000000000000000000000000000000000000) = EXP v1234(0x2), v1232(0xa0)
    0x1237: v1237(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1236(0x10000000000000000000000000000000000000000), v1230(0x1)
    0x1238: v1238 = AND v1237(0xffffffffffffffffffffffffffffffffffffffff), v122f
    0x1239: v1239(0x5a6c72d0) = CONST 
    0x123e: v123e(0x40) = CONST 
    0x1240: v1240 = MLOAD v123e(0x40)
    0x1242: v1242(0xffffffff) = CONST 
    0x1247: v1247(0x5a6c72d0) = AND v1242(0xffffffff), v1239(0x5a6c72d0)
    0x1248: v1248(0xe0) = CONST 
    0x124a: v124a(0x2) = CONST 
    0x124c: v124c(0x100000000000000000000000000000000000000000000000000000000) = EXP v124a(0x2), v1248(0xe0)
    0x124d: v124d(0x5a6c72d000000000000000000000000000000000000000000000000000000000) = MUL v124c(0x100000000000000000000000000000000000000000000000000000000), v1247(0x5a6c72d0)
    0x124f: MSTORE v1240, v124d(0x5a6c72d000000000000000000000000000000000000000000000000000000000)
    0x1250: v1250(0x4) = CONST 
    0x1252: v1252 = ADD v1250(0x4), v1240
    0x1253: v1253(0x20) = CONST 
    0x1255: v1255(0x40) = CONST 
    0x1257: v1257 = MLOAD v1255(0x40)
    0x125a: v125a(0x4) = SUB v1252, v1257
    0x125c: v125c(0x0) = CONST 
    0x1260: v1260 = EXTCODESIZE v1238
    0x1261: v1261 = ISZERO v1260
    0x1263: v1263 = ISZERO v1261
    0x1264: v1264(0x1132) = CONST 
    0x1267: JUMPI v1264(0x1132), v1263

    Begin block 0x1268
    prev=[0x1217], succ=[]
    =================================
    0x1268: v1268(0x0) = CONST 
    0x126b: REVERT v1268(0x0), v1268(0x0)

    Begin block 0x11320x1217
    prev=[0x1217], succ=[0x113d0x1217, 0x11460x1217]
    =================================
    0x11340x1217: v12171134 = GAS 
    0x11350x1217: v12171135 = CALL v12171134, v1238, v125c(0x0), v1257, v125a(0x4), v1257, v1253(0x20)
    0x11360x1217: v12171136 = ISZERO v12171135
    0x11380x1217: v12171138 = ISZERO v12171136
    0x11390x1217: v12171139(0x1146) = CONST 
    0x113c0x1217: JUMPI v12171139(0x1146), v12171138

    Begin block 0x113d0x1217
    prev=[0x11320x1217], succ=[]
    =================================
    0x113d0x1217: v1217113d = RETURNDATASIZE 
    0x113e0x1217: v1217113e(0x0) = CONST 
    0x11410x1217: RETURNDATACOPY v1217113e(0x0), v1217113e(0x0), v1217113d
    0x11420x1217: v12171142 = RETURNDATASIZE 
    0x11430x1217: v12171143(0x0) = CONST 
    0x11450x1217: REVERT v12171143(0x0), v12171142

    Begin block 0x11460x1217
    prev=[0x11320x1217], succ=[0x11580x1217, 0x115c0x1217]
    =================================
    0x114b0x1217: v1217114b(0x40) = CONST 
    0x114d0x1217: v1217114d = MLOAD v1217114b(0x40)
    0x114e0x1217: v1217114e = RETURNDATASIZE 
    0x114f0x1217: v1217114f(0x20) = CONST 
    0x11520x1217: v12171152 = LT v1217114e, v1217114f(0x20)
    0x11530x1217: v12171153 = ISZERO v12171152
    0x11540x1217: v12171154(0x115c) = CONST 
    0x11570x1217: JUMPI v12171154(0x115c), v12171153

    Begin block 0x11580x1217
    prev=[0x11460x1217], succ=[]
    =================================
    0x11580x1217: v12171158(0x0) = CONST 
    0x115b0x1217: REVERT v12171158(0x0), v12171158(0x0)

    Begin block 0x115c0x1217
    prev=[0x11460x1217], succ=[]
    =================================
    0x115e0x1217: v1217115e = MLOAD v1217114d
    0x11620x1217: RETURNPRIVATE v1217arg0, v1217115e

}

function 0x162d(0x162darg0x0, 0x162darg0x1) private {
    Begin block 0x162d
    prev=[], succ=[0x1696, 0x169a0x162d]
    =================================
    0x162e: v162e(0x4) = CONST 
    0x1631: v1631 = SLOAD v162e(0x4)
    0x1632: v1632(0x40) = CONST 
    0x1635: v1635 = MLOAD v1632(0x40)
    0x1636: v1636(0x9b19251a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x1658: MSTORE v1635, v1636(0x9b19251a00000000000000000000000000000000000000000000000000000000)
    0x1659: v1659(0x1) = CONST 
    0x165b: v165b(0xa0) = CONST 
    0x165d: v165d(0x2) = CONST 
    0x165f: v165f(0x10000000000000000000000000000000000000000) = EXP v165d(0x2), v165b(0xa0)
    0x1660: v1660(0xffffffffffffffffffffffffffffffffffffffff) = SUB v165f(0x10000000000000000000000000000000000000000), v1659(0x1)
    0x1663: v1663 = AND v1660(0xffffffffffffffffffffffffffffffffffffffff), v162darg0
    0x1666: v1666 = ADD v1635, v162e(0x4)
    0x166a: MSTORE v1666, v1663
    0x166c: v166c = MLOAD v1632(0x40)
    0x166d: v166d(0x0) = CONST 
    0x1672: v1672 = AND v1631, v1660(0xffffffffffffffffffffffffffffffffffffffff)
    0x1674: v1674(0x9b19251a) = CONST 
    0x167a: v167a(0x24) = CONST 
    0x167e: v167e = ADD v1635, v167a(0x24)
    0x1680: v1680(0x20) = CONST 
    0x1688: v1688(0x0) = SUB v1635, v166c
    0x1689: v1689(0x24) = ADD v1688(0x0), v167a(0x24)
    0x168e: v168e = EXTCODESIZE v1672
    0x168f: v168f = ISZERO v168e
    0x1691: v1691 = ISZERO v168f
    0x1692: v1692(0x169a) = CONST 
    0x1695: JUMPI v1692(0x169a), v1691

    Begin block 0x1696
    prev=[0x162d], succ=[]
    =================================
    0x1696: v1696(0x0) = CONST 
    0x1699: REVERT v1696(0x0), v1696(0x0)

    Begin block 0x169a0x162d
    prev=[0x162d], succ=[0x16a50x162d, 0x16ae0x162d]
    =================================
    0x169c0x162d: v162d169c = GAS 
    0x169d0x162d: v162d169d = CALL v162d169c, v1672, v166d(0x0), v166c, v1689(0x24), v166c, v1680(0x20)
    0x169e0x162d: v162d169e = ISZERO v162d169d
    0x16a00x162d: v162d16a0 = ISZERO v162d169e
    0x16a10x162d: v162d16a1(0x16ae) = CONST 
    0x16a40x162d: JUMPI v162d16a1(0x16ae), v162d16a0

    Begin block 0x16a50x162d
    prev=[0x169a0x162d], succ=[]
    =================================
    0x16a50x162d: v162d16a5 = RETURNDATASIZE 
    0x16a60x162d: v162d16a6(0x0) = CONST 
    0x16a90x162d: RETURNDATACOPY v162d16a6(0x0), v162d16a6(0x0), v162d16a5
    0x16aa0x162d: v162d16aa = RETURNDATASIZE 
    0x16ab0x162d: v162d16ab(0x0) = CONST 
    0x16ad0x162d: REVERT v162d16ab(0x0), v162d16aa

    Begin block 0x16ae0x162d
    prev=[0x169a0x162d], succ=[0x16c00x162d, 0x16c40x162d]
    =================================
    0x16b30x162d: v162d16b3(0x40) = CONST 
    0x16b50x162d: v162d16b5 = MLOAD v162d16b3(0x40)
    0x16b60x162d: v162d16b6 = RETURNDATASIZE 
    0x16b70x162d: v162d16b7(0x20) = CONST 
    0x16ba0x162d: v162d16ba = LT v162d16b6, v162d16b7(0x20)
    0x16bb0x162d: v162d16bb = ISZERO v162d16ba
    0x16bc0x162d: v162d16bc(0x16c4) = CONST 
    0x16bf0x162d: JUMPI v162d16bc(0x16c4), v162d16bb

    Begin block 0x16c00x162d
    prev=[0x16ae0x162d], succ=[]
    =================================
    0x16c00x162d: v162d16c0(0x0) = CONST 
    0x16c30x162d: REVERT v162d16c0(0x0), v162d16c0(0x0)

    Begin block 0x16c40x162d
    prev=[0x16ae0x162d], succ=[0x16c90x162d]
    =================================
    0x16c60x162d: v162d16c6 = MLOAD v162d16b5

    Begin block 0x16c90x162d
    prev=[0x16c40x162d], succ=[]
    =================================
    0x16cd0x162d: RETURNPRIVATE v162darg1, v162d16c6

}

function 0x206a(0x206aarg0x0, 0x206aarg0x1) private {
    Begin block 0x206a
    prev=[], succ=[0x20d1, 0x169a0x206a]
    =================================
    0x206b: v206b(0x2) = CONST 
    0x206d: v206d = SLOAD v206b(0x2)
    0x206e: v206e(0x40) = CONST 
    0x2071: v2071 = MLOAD v206e(0x40)
    0x2072: v2072(0x27e235e300000000000000000000000000000000000000000000000000000000) = CONST 
    0x2094: MSTORE v2071, v2072(0x27e235e300000000000000000000000000000000000000000000000000000000)
    0x2095: v2095(0x1) = CONST 
    0x2097: v2097(0xa0) = CONST 
    0x2099: v2099(0x2) = CONST 
    0x209b: v209b(0x10000000000000000000000000000000000000000) = EXP v2099(0x2), v2097(0xa0)
    0x209c: v209c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v209b(0x10000000000000000000000000000000000000000), v2095(0x1)
    0x209f: v209f = AND v209c(0xffffffffffffffffffffffffffffffffffffffff), v206aarg0
    0x20a0: v20a0(0x4) = CONST 
    0x20a3: v20a3 = ADD v2071, v20a0(0x4)
    0x20a4: MSTORE v20a3, v209f
    0x20a6: v20a6 = MLOAD v206e(0x40)
    0x20a7: v20a7(0x0) = CONST 
    0x20ad: v20ad = AND v206d, v209c(0xffffffffffffffffffffffffffffffffffffffff)
    0x20af: v20af(0x27e235e3) = CONST 
    0x20b5: v20b5(0x24) = CONST 
    0x20b9: v20b9 = ADD v2071, v20b5(0x24)
    0x20bb: v20bb(0x20) = CONST 
    0x20c3: v20c3(0x0) = SUB v2071, v20a6
    0x20c4: v20c4(0x24) = ADD v20c3(0x0), v20b5(0x24)
    0x20c9: v20c9 = EXTCODESIZE v20ad
    0x20ca: v20ca = ISZERO v20c9
    0x20cc: v20cc = ISZERO v20ca
    0x20cd: v20cd(0x169a) = CONST 
    0x20d0: JUMPI v20cd(0x169a), v20cc

    Begin block 0x20d1
    prev=[0x206a], succ=[]
    =================================
    0x20d1: v20d1(0x0) = CONST 
    0x20d4: REVERT v20d1(0x0), v20d1(0x0)

    Begin block 0x169a0x206a
    prev=[0x206a], succ=[0x16a50x206a, 0x16ae0x206a]
    =================================
    0x169c0x206a: v206a169c = GAS 
    0x169d0x206a: v206a169d = CALL v206a169c, v20ad, v20a7(0x0), v20a6, v20c4(0x24), v20a6, v20bb(0x20)
    0x169e0x206a: v206a169e = ISZERO v206a169d
    0x16a00x206a: v206a16a0 = ISZERO v206a169e
    0x16a10x206a: v206a16a1(0x16ae) = CONST 
    0x16a40x206a: JUMPI v206a16a1(0x16ae), v206a16a0

    Begin block 0x16a50x206a
    prev=[0x169a0x206a], succ=[]
    =================================
    0x16a50x206a: v206a16a5 = RETURNDATASIZE 
    0x16a60x206a: v206a16a6(0x0) = CONST 
    0x16a90x206a: RETURNDATACOPY v206a16a6(0x0), v206a16a6(0x0), v206a16a5
    0x16aa0x206a: v206a16aa = RETURNDATASIZE 
    0x16ab0x206a: v206a16ab(0x0) = CONST 
    0x16ad0x206a: REVERT v206a16ab(0x0), v206a16aa

    Begin block 0x16ae0x206a
    prev=[0x169a0x206a], succ=[0x16c00x206a, 0x16c40x206a]
    =================================
    0x16b30x206a: v206a16b3(0x40) = CONST 
    0x16b50x206a: v206a16b5 = MLOAD v206a16b3(0x40)
    0x16b60x206a: v206a16b6 = RETURNDATASIZE 
    0x16b70x206a: v206a16b7(0x20) = CONST 
    0x16ba0x206a: v206a16ba = LT v206a16b6, v206a16b7(0x20)
    0x16bb0x206a: v206a16bb = ISZERO v206a16ba
    0x16bc0x206a: v206a16bc(0x16c4) = CONST 
    0x16bf0x206a: JUMPI v206a16bc(0x16c4), v206a16bb

    Begin block 0x16c00x206a
    prev=[0x16ae0x206a], succ=[]
    =================================
    0x16c00x206a: v206a16c0(0x0) = CONST 
    0x16c30x206a: REVERT v206a16c0(0x0), v206a16c0(0x0)

    Begin block 0x16c40x206a
    prev=[0x16ae0x206a], succ=[0x16c90x206a]
    =================================
    0x16c60x206a: v206a16c6 = MLOAD v206a16b5

    Begin block 0x16c90x206a
    prev=[0x16c40x206a], succ=[]
    =================================
    0x16cd0x206a: RETURNPRIVATE v206aarg1, v206a16c6

}

function fallback()() public {
    Begin block 0x237
    prev=[], succ=[]
    =================================
    0x238: v238(0x0) = CONST 
    0x23b: REVERT v238(0x0), v238(0x0)

}

function symbol()() public {
    Begin block 0x23c
    prev=[], succ=[0x244, 0x248]
    =================================
    0x23d: v23d = CALLVALUE 
    0x23f: v23f = ISZERO v23d
    0x240: v240(0x248) = CONST 
    0x243: JUMPI v240(0x248), v23f

    Begin block 0x244
    prev=[0x23c], succ=[]
    =================================
    0x244: v244(0x0) = CONST 
    0x247: REVERT v244(0x0), v244(0x0)

    Begin block 0x248
    prev=[0x23c], succ=[0x98c]
    =================================
    0x24a: v24a(0x251) = CONST 
    0x24d: v24d(0x98c) = CONST 
    0x250: JUMP v24d(0x98c)

    Begin block 0x98c
    prev=[0x248], succ=[0x251]
    =================================
    0x98d: v98d(0x40) = CONST 
    0x990: v990 = MLOAD v98d(0x40)
    0x993: v993 = ADD v98d(0x40), v990
    0x996: MSTORE v98d(0x40), v993
    0x997: v997(0x4) = CONST 
    0x99a: MSTORE v990, v997(0x4)
    0x99b: v99b(0x4355534400000000000000000000000000000000000000000000000000000000) = CONST 
    0x9bc: v9bc(0x20) = CONST 
    0x9bf: v9bf = ADD v990, v9bc(0x20)
    0x9c0: MSTORE v9bf, v99b(0x4355534400000000000000000000000000000000000000000000000000000000)
    0x9c2: JUMP v24a(0x251)

    Begin block 0x251
    prev=[0x98c], succ=[0x273]
    =================================
    0x252: v252(0x40) = CONST 
    0x255: v255 = MLOAD v252(0x40)
    0x256: v256(0x20) = CONST 
    0x25a: MSTORE v255, v256(0x20)
    0x25c: v25c(0x4) = MLOAD v990
    0x25f: v25f = ADD v255, v256(0x20)
    0x260: MSTORE v25f, v25c(0x4)
    0x262: v262(0x4) = MLOAD v990
    0x269: v269 = ADD v255, v252(0x40)
    0x26c: v26c = ADD v990, v256(0x20)
    0x271: v271(0x0) = CONST 

    Begin block 0x273
    prev=[0x251, 0x27c], succ=[0x28b, 0x27c]
    =================================
    0x273_0x0: v273_0 = PHI v271(0x0), v286
    0x276: v276 = LT v273_0, v262(0x4)
    0x277: v277 = ISZERO v276
    0x278: v278(0x28b) = CONST 
    0x27b: JUMPI v278(0x28b), v277

    Begin block 0x28b
    prev=[0x273], succ=[0x2b8, 0x29f]
    =================================
    0x294: v294 = ADD v262(0x4), v269
    0x296: v296(0x1f) = CONST 
    0x298: v298(0x4) = AND v296(0x1f), v262(0x4)
    0x29a: v29a = ISZERO v298(0x4)
    0x29b: v29b(0x2b8) = CONST 
    0x29e: JUMPI v29b(0x2b8), v29a

    Begin block 0x2b8
    prev=[0x28b, 0x29f], succ=[]
    =================================
    0x2b8_0x1: v2b8_1 = PHI v294, v2b5
    0x2be: v2be(0x40) = CONST 
    0x2c0: v2c0 = MLOAD v2be(0x40)
    0x2c3: v2c3 = SUB v2b8_1, v2c0
    0x2c5: RETURN v2c0, v2c3

    Begin block 0x29f
    prev=[0x28b], succ=[0x2b8]
    =================================
    0x2a1: v2a1 = SUB v294, v298(0x4)
    0x2a3: v2a3 = MLOAD v2a1
    0x2a4: v2a4(0x1) = CONST 
    0x2a7: v2a7(0x20) = CONST 
    0x2a9: v2a9(0x1c) = SUB v2a7(0x20), v298(0x4)
    0x2aa: v2aa(0x100) = CONST 
    0x2ad: v2ad(0x100000000000000000000000000000000000000000000000000000000) = EXP v2aa(0x100), v2a9(0x1c)
    0x2ae: v2ae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2ad(0x100000000000000000000000000000000000000000000000000000000), v2a4(0x1)
    0x2af: v2af = NOT v2ae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2b0: v2b0 = AND v2af, v2a3
    0x2b2: MSTORE v2a1, v2b0
    0x2b3: v2b3(0x20) = CONST 
    0x2b5: v2b5 = ADD v2b3(0x20), v2a1

    Begin block 0x27c
    prev=[0x273], succ=[0x273]
    =================================
    0x27c_0x0: v27c_0 = PHI v271(0x0), v286
    0x27e: v27e = ADD v27c_0, v26c
    0x27f: v27f = MLOAD v27e
    0x282: v282 = ADD v27c_0, v269
    0x283: MSTORE v282, v27f
    0x284: v284(0x20) = CONST 
    0x286: v286 = ADD v284(0x20), v27c_0
    0x287: v287(0x273) = CONST 
    0x28a: JUMP v287(0x273)

}

function 0x24f9(0x24f9arg0x0, 0x24f9arg0x1) private {
    Begin block 0x24f9
    prev=[], succ=[0x2505]
    =================================
    0x24fa: v24fa(0x0) = CONST 
    0x24fd: v24fd(0x2505) = CONST 
    0x2501: v2501(0x2912) = CONST 
    0x2504: v2504_0 = CALLPRIVATE v2501(0x2912), v24f9arg0, v24fd(0x2505)

    Begin block 0x2505
    prev=[0x24f9], succ=[0x250c, 0x251b]
    =================================
    0x2506: v2506 = GT v2504_0, v24fa(0x0)
    0x2507: v2507 = ISZERO v2506
    0x2508: v2508(0x251b) = CONST 
    0x250b: JUMPI v2508(0x251b), v2507

    Begin block 0x250c
    prev=[0x2505], succ=[0x2514]
    =================================
    0x250c: v250c(0x2514) = CONST 
    0x2510: v2510(0x2912) = CONST 
    0x2513: v2513_0 = CALLPRIVATE v2510(0x2912), v24f9arg0, v250c(0x2514)

    Begin block 0x2514
    prev=[0x250c], succ=[0x16c90x24f9]
    =================================
    0x2517: v2517(0x16c9) = CONST 
    0x251a: JUMP v2517(0x16c9)

    Begin block 0x16c90x24f9
    prev=[0x2514], succ=[]
    =================================
    0x16cd0x24f9: RETURNPRIVATE v24f9arg1, v2513_0

    Begin block 0x251b
    prev=[0x2505], succ=[0x2523]
    =================================
    0x251c: v251c(0x2523) = CONST 
    0x251f: v251f(0x1217) = CONST 
    0x2522: v2522_0 = CALLPRIVATE v251f(0x1217), v251c(0x2523)

    Begin block 0x2523
    prev=[0x251b], succ=[]
    =================================
    0x2528: RETURNPRIVATE v24f9arg1, v2522_0

}

function 0x2569(0x2569arg0x0, 0x2569arg0x1, 0x2569arg0x2, 0x2569arg0x3, 0x2569arg0x4) private {
    Begin block 0x2569
    prev=[], succ=[0x25f80x2569]
    =================================
    0x256a: v256a(0x40) = CONST 
    0x256d: v256d = MLOAD v256a(0x40)
    0x256e: v256e(0x1000000000000000000000000) = CONST 
    0x257c: v257c = ADDRESS 
    0x257e: v257e = MUL v256e(0x1000000000000000000000000), v257c
    0x257f: v257f(0x20) = CONST 
    0x2583: v2583 = ADD v256d, v257f(0x20)
    0x2587: MSTORE v2583, v257e
    0x2588: v2588(0x6d657461496e637265617365417070726f76616c000000000000000000000000) = CONST 
    0x25a9: v25a9(0x34) = CONST 
    0x25ac: v25ac = ADD v256d, v25a9(0x34)
    0x25ad: MSTORE v25ac, v2588(0x6d657461496e637265617365417070726f76616c000000000000000000000000)
    0x25ae: v25ae(0x1) = CONST 
    0x25b0: v25b0(0xa0) = CONST 
    0x25b2: v25b2(0x2) = CONST 
    0x25b4: v25b4(0x10000000000000000000000000000000000000000) = EXP v25b2(0x2), v25b0(0xa0)
    0x25b5: v25b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25b4(0x10000000000000000000000000000000000000000), v25ae(0x1)
    0x25b7: v25b7 = AND v2569arg3, v25b5(0xffffffffffffffffffffffffffffffffffffffff)
    0x25ba: v25ba = MUL v256e(0x1000000000000000000000000), v25b7
    0x25bb: v25bb(0x48) = CONST 
    0x25be: v25be = ADD v256d, v25bb(0x48)
    0x25bf: MSTORE v25be, v25ba
    0x25c0: v25c0(0x5c) = CONST 
    0x25c3: v25c3 = ADD v256d, v25c0(0x5c)
    0x25c6: MSTORE v25c3, v2569arg2
    0x25c7: v25c7(0x7c) = CONST 
    0x25ca: v25ca = ADD v256d, v25c7(0x7c)
    0x25cd: MSTORE v25ca, v2569arg1
    0x25ce: v25ce(0x9c) = CONST 
    0x25d2: v25d2 = ADD v256d, v25ce(0x9c)
    0x25d5: MSTORE v25d2, v2569arg0
    0x25d7: v25d7 = MLOAD v256a(0x40)
    0x25da: v25da(0x0) = SUB v256d, v25d7
    0x25dd: v25dd(0x9c) = ADD v25ce(0x9c), v25da(0x0)
    0x25df: MSTORE v25d7, v25dd(0x9c)
    0x25e0: v25e0(0xbc) = CONST 
    0x25e4: v25e4 = ADD v256d, v25e0(0xbc)
    0x25e8: MSTORE v256a(0x40), v25e4
    0x25ea: v25ea(0x9c) = MLOAD v25d7
    0x25eb: v25eb(0x0) = CONST 
    0x25f3: v25f3 = ADD v25d7, v257f(0x20)

    Begin block 0x25f80x2569
    prev=[0x2569, 0x26010x2569], succ=[0x26010x2569, 0x26170x2569]
    =================================
    0x25f80x2569_0x2: v25f82569_2 = PHI v25ea(0x9c), v2569260a
    0x25f90x2569: v256925f9(0x20) = CONST 
    0x25fc0x2569: v256925fc = LT v25f82569_2, v256925f9(0x20)
    0x25fd0x2569: v256925fd(0x2617) = CONST 
    0x26000x2569: JUMPI v256925fd(0x2617), v256925fc

    Begin block 0x26010x2569
    prev=[0x25f80x2569], succ=[0x25f80x2569]
    =================================
    0x26010x2569_0x0: v26012569_0 = PHI v25f3, v25692612
    0x26010x2569_0x1: v26012569_1 = PHI v25e4, v25692610
    0x26010x2569_0x2: v26012569_2 = PHI v25ea(0x9c), v2569260a
    0x26020x2569: v25692602 = MLOAD v26012569_0
    0x26040x2569: MSTORE v26012569_1, v25692602
    0x26050x2569: v25692605(0x1f) = CONST 
    0x26070x2569: v25692607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v25692605(0x1f)
    0x260a0x2569: v2569260a = ADD v26012569_2, v25692607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x260c0x2569: v2569260c(0x20) = CONST 
    0x26100x2569: v25692610 = ADD v2569260c(0x20), v26012569_1
    0x26120x2569: v25692612 = ADD v2569260c(0x20), v26012569_0
    0x26130x2569: v25692613(0x25f8) = CONST 
    0x26160x2569: JUMP v25692613(0x25f8)

    Begin block 0x26170x2569
    prev=[0x25f80x2569], succ=[]
    =================================
    0x26170x2569_0x0: v26172569_0 = PHI v25f3, v25692612
    0x26170x2569_0x1: v26172569_1 = PHI v25e4, v25692610
    0x26170x2569_0x2: v26172569_2 = PHI v25ea(0x9c), v2569260a
    0x26180x2569: v25692618 = MLOAD v26172569_0
    0x261a0x2569: v2569261a = MLOAD v26172569_1
    0x261b0x2569: v2569261b(0x20) = CONST 
    0x26200x2569: v25692620 = SUB v2569261b(0x20), v26172569_2
    0x26210x2569: v25692621(0x100) = CONST 
    0x26240x2569: v25692624 = EXP v25692621(0x100), v25692620
    0x26250x2569: v25692625(0x0) = CONST 
    0x26270x2569: v25692627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v25692625(0x0)
    0x26280x2569: v25692628 = ADD v25692627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v25692624
    0x262a0x2569: v2569262a = NOT v25692628
    0x262d0x2569: v2569262d = AND v25692618, v2569262a
    0x262f0x2569: v2569262f = AND v2569261a, v25692628
    0x26330x2569: v25692633 = OR v2569262f, v2569262d
    0x26350x2569: MSTORE v26172569_1, v25692633
    0x26360x2569: v25692636(0x40) = CONST 
    0x26380x2569: v25692638 = MLOAD v25692636(0x40)
    0x263a0x2569: v2569263a = ADD v25e4, v25ea(0x9c)
    0x263d0x2569: v2569263d = SUB v2569263a, v25692638
    0x26400x2569: v25692640 = SHA3 v25692638, v2569263d
    0x264b0x2569: RETURNPRIVATE v2569arg4, v25692640

}

function 0x2912(0x2912arg0x0, 0x2912arg0x1) private {
    Begin block 0x2912
    prev=[], succ=[0x297b, 0x169a0x2912]
    =================================
    0x2913: v2913(0x4) = CONST 
    0x2916: v2916 = SLOAD v2913(0x4)
    0x2917: v2917(0x40) = CONST 
    0x291a: v291a = MLOAD v2917(0x40)
    0x291b: v291b(0xfaaebd2100000000000000000000000000000000000000000000000000000000) = CONST 
    0x293d: MSTORE v291a, v291b(0xfaaebd2100000000000000000000000000000000000000000000000000000000)
    0x293e: v293e(0x1) = CONST 
    0x2940: v2940(0xa0) = CONST 
    0x2942: v2942(0x2) = CONST 
    0x2944: v2944(0x10000000000000000000000000000000000000000) = EXP v2942(0x2), v2940(0xa0)
    0x2945: v2945(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2944(0x10000000000000000000000000000000000000000), v293e(0x1)
    0x2948: v2948 = AND v2945(0xffffffffffffffffffffffffffffffffffffffff), v2912arg0
    0x294b: v294b = ADD v291a, v2913(0x4)
    0x294f: MSTORE v294b, v2948
    0x2951: v2951 = MLOAD v2917(0x40)
    0x2952: v2952(0x0) = CONST 
    0x2957: v2957 = AND v2916, v2945(0xffffffffffffffffffffffffffffffffffffffff)
    0x2959: v2959(0xfaaebd21) = CONST 
    0x295f: v295f(0x24) = CONST 
    0x2963: v2963 = ADD v291a, v295f(0x24)
    0x2965: v2965(0x20) = CONST 
    0x296d: v296d(0x0) = SUB v291a, v2951
    0x296e: v296e(0x24) = ADD v296d(0x0), v295f(0x24)
    0x2973: v2973 = EXTCODESIZE v2957
    0x2974: v2974 = ISZERO v2973
    0x2976: v2976 = ISZERO v2974
    0x2977: v2977(0x169a) = CONST 
    0x297a: JUMPI v2977(0x169a), v2976

    Begin block 0x297b
    prev=[0x2912], succ=[]
    =================================
    0x297b: v297b(0x0) = CONST 
    0x297e: REVERT v297b(0x0), v297b(0x0)

    Begin block 0x169a0x2912
    prev=[0x2912], succ=[0x16a50x2912, 0x16ae0x2912]
    =================================
    0x169c0x2912: v2912169c = GAS 
    0x169d0x2912: v2912169d = CALL v2912169c, v2957, v2952(0x0), v2951, v296e(0x24), v2951, v2965(0x20)
    0x169e0x2912: v2912169e = ISZERO v2912169d
    0x16a00x2912: v291216a0 = ISZERO v2912169e
    0x16a10x2912: v291216a1(0x16ae) = CONST 
    0x16a40x2912: JUMPI v291216a1(0x16ae), v291216a0

    Begin block 0x16a50x2912
    prev=[0x169a0x2912], succ=[]
    =================================
    0x16a50x2912: v291216a5 = RETURNDATASIZE 
    0x16a60x2912: v291216a6(0x0) = CONST 
    0x16a90x2912: RETURNDATACOPY v291216a6(0x0), v291216a6(0x0), v291216a5
    0x16aa0x2912: v291216aa = RETURNDATASIZE 
    0x16ab0x2912: v291216ab(0x0) = CONST 
    0x16ad0x2912: REVERT v291216ab(0x0), v291216aa

    Begin block 0x16ae0x2912
    prev=[0x169a0x2912], succ=[0x16c00x2912, 0x16c40x2912]
    =================================
    0x16b30x2912: v291216b3(0x40) = CONST 
    0x16b50x2912: v291216b5 = MLOAD v291216b3(0x40)
    0x16b60x2912: v291216b6 = RETURNDATASIZE 
    0x16b70x2912: v291216b7(0x20) = CONST 
    0x16ba0x2912: v291216ba = LT v291216b6, v291216b7(0x20)
    0x16bb0x2912: v291216bb = ISZERO v291216ba
    0x16bc0x2912: v291216bc(0x16c4) = CONST 
    0x16bf0x2912: JUMPI v291216bc(0x16c4), v291216bb

    Begin block 0x16c00x2912
    prev=[0x16ae0x2912], succ=[]
    =================================
    0x16c00x2912: v291216c0(0x0) = CONST 
    0x16c30x2912: REVERT v291216c0(0x0), v291216c0(0x0)

    Begin block 0x16c40x2912
    prev=[0x16ae0x2912], succ=[0x16c90x2912]
    =================================
    0x16c60x2912: v291216c6 = MLOAD v291216b5

    Begin block 0x16c90x2912
    prev=[0x16c40x2912], succ=[]
    =================================
    0x16cd0x2912: RETURNPRIVATE v2912arg1, v291216c6

}

function 0x2a67(0x2a67arg0x0, 0x2a67arg0x1, 0x2a67arg0x2, 0x2a67arg0x3, 0x2a67arg0x4) private {
    Begin block 0x2a67
    prev=[], succ=[0x2afd, 0x26170x2a67]
    =================================
    0x2a68: v2a68(0x40) = CONST 
    0x2a6b: v2a6b = MLOAD v2a68(0x40)
    0x2a6c: v2a6c(0x1000000000000000000000000) = CONST 
    0x2a7a: v2a7a = ADDRESS 
    0x2a7c: v2a7c = MUL v2a6c(0x1000000000000000000000000), v2a7a
    0x2a7d: v2a7d(0x20) = CONST 
    0x2a81: v2a81 = ADD v2a6b, v2a7d(0x20)
    0x2a85: MSTORE v2a81, v2a7c
    0x2a86: v2a86(0x6d6574615472616e736665720000000000000000000000000000000000000000) = CONST 
    0x2aa7: v2aa7(0x34) = CONST 
    0x2aaa: v2aaa = ADD v2a6b, v2aa7(0x34)
    0x2aab: MSTORE v2aaa, v2a86(0x6d6574615472616e736665720000000000000000000000000000000000000000)
    0x2aac: v2aac(0x1) = CONST 
    0x2aae: v2aae(0xa0) = CONST 
    0x2ab0: v2ab0(0x2) = CONST 
    0x2ab2: v2ab2(0x10000000000000000000000000000000000000000) = EXP v2ab0(0x2), v2aae(0xa0)
    0x2ab3: v2ab3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ab2(0x10000000000000000000000000000000000000000), v2aac(0x1)
    0x2ab5: v2ab5 = AND v2a67arg3, v2ab3(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ab8: v2ab8 = MUL v2a6c(0x1000000000000000000000000), v2ab5
    0x2abb: v2abb = ADD v2a68(0x40), v2a6b
    0x2abc: MSTORE v2abb, v2ab8
    0x2abd: v2abd(0x54) = CONST 
    0x2ac0: v2ac0 = ADD v2a6b, v2abd(0x54)
    0x2ac3: MSTORE v2ac0, v2a67arg2
    0x2ac4: v2ac4(0x74) = CONST 
    0x2ac7: v2ac7 = ADD v2a6b, v2ac4(0x74)
    0x2aca: MSTORE v2ac7, v2a67arg1
    0x2acb: v2acb(0x94) = CONST 
    0x2acf: v2acf = ADD v2a6b, v2acb(0x94)
    0x2ad2: MSTORE v2acf, v2a67arg0
    0x2ad4: v2ad4 = MLOAD v2a68(0x40)
    0x2ad7: v2ad7(0x0) = SUB v2a6b, v2ad4
    0x2ada: v2ada(0x94) = ADD v2acb(0x94), v2ad7(0x0)
    0x2adc: MSTORE v2ad4, v2ada(0x94)
    0x2add: v2add(0xb4) = CONST 
    0x2ae1: v2ae1 = ADD v2a6b, v2add(0xb4)
    0x2ae5: MSTORE v2a68(0x40), v2ae1
    0x2ae7: v2ae7(0x94) = MLOAD v2ad4
    0x2ae8: v2ae8(0x0) = CONST 
    0x2af0: v2af0 = ADD v2ad4, v2a7d(0x20)
    0x2af5: v2af5(0x20) = CONST 
    0x2af8: v2af8(0x0) = LT v2ae7(0x94), v2af5(0x20)
    0x2af9: v2af9(0x2617) = CONST 
    0x2afc: JUMPI v2af9(0x2617), v2af8(0x0)

    Begin block 0x2afd
    prev=[0x2a67], succ=[0x25f80x2a67]
    =================================
    0x2afe: v2afe = MLOAD v2af0
    0x2b00: MSTORE v2ae1, v2afe
    0x2b01: v2b01(0x1f) = CONST 
    0x2b03: v2b03(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2b01(0x1f)
    0x2b06: v2b06(0x74) = ADD v2ae7(0x94), v2b03(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2b08: v2b08(0x20) = CONST 
    0x2b0c: v2b0c = ADD v2b08(0x20), v2ae1
    0x2b0e: v2b0e = ADD v2b08(0x20), v2af0
    0x2b0f: v2b0f(0x25f8) = CONST 
    0x2b12: JUMP v2b0f(0x25f8)

    Begin block 0x25f80x2a67
    prev=[0x2afd, 0x26010x2a67], succ=[0x26010x2a67, 0x26170x2a67]
    =================================
    0x25f80x2a67_0x2: v25f82a67_2 = PHI v2b06(0x74), v2a67260a
    0x25f90x2a67: v2a6725f9(0x20) = CONST 
    0x25fc0x2a67: v2a6725fc = LT v25f82a67_2, v2a6725f9(0x20)
    0x25fd0x2a67: v2a6725fd(0x2617) = CONST 
    0x26000x2a67: JUMPI v2a6725fd(0x2617), v2a6725fc

    Begin block 0x26010x2a67
    prev=[0x25f80x2a67], succ=[0x25f80x2a67]
    =================================
    0x26010x2a67_0x0: v26012a67_0 = PHI v2b0e, v2a672612
    0x26010x2a67_0x1: v26012a67_1 = PHI v2b0c, v2a672610
    0x26010x2a67_0x2: v26012a67_2 = PHI v2b06(0x74), v2a67260a
    0x26020x2a67: v2a672602 = MLOAD v26012a67_0
    0x26040x2a67: MSTORE v26012a67_1, v2a672602
    0x26050x2a67: v2a672605(0x1f) = CONST 
    0x26070x2a67: v2a672607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2a672605(0x1f)
    0x260a0x2a67: v2a67260a = ADD v26012a67_2, v2a672607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x260c0x2a67: v2a67260c(0x20) = CONST 
    0x26100x2a67: v2a672610 = ADD v2a67260c(0x20), v26012a67_1
    0x26120x2a67: v2a672612 = ADD v2a67260c(0x20), v26012a67_0
    0x26130x2a67: v2a672613(0x25f8) = CONST 
    0x26160x2a67: JUMP v2a672613(0x25f8)

    Begin block 0x26170x2a67
    prev=[0x2a67, 0x25f80x2a67], succ=[]
    =================================
    0x26170x2a67_0x0: v26172a67_0 = PHI v2af0, v2b0e, v2a672612
    0x26170x2a67_0x1: v26172a67_1 = PHI v2ae1, v2b0c, v2a672610
    0x26170x2a67_0x2: v26172a67_2 = PHI v2ae7(0x94), v2b06(0x74), v2a67260a
    0x26180x2a67: v2a672618 = MLOAD v26172a67_0
    0x261a0x2a67: v2a67261a = MLOAD v26172a67_1
    0x261b0x2a67: v2a67261b(0x20) = CONST 
    0x26200x2a67: v2a672620 = SUB v2a67261b(0x20), v26172a67_2
    0x26210x2a67: v2a672621(0x100) = CONST 
    0x26240x2a67: v2a672624 = EXP v2a672621(0x100), v2a672620
    0x26250x2a67: v2a672625(0x0) = CONST 
    0x26270x2a67: v2a672627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v2a672625(0x0)
    0x26280x2a67: v2a672628 = ADD v2a672627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2a672624
    0x262a0x2a67: v2a67262a = NOT v2a672628
    0x262d0x2a67: v2a67262d = AND v2a672618, v2a67262a
    0x262f0x2a67: v2a67262f = AND v2a67261a, v2a672628
    0x26330x2a67: v2a672633 = OR v2a67262f, v2a67262d
    0x26350x2a67: MSTORE v26172a67_1, v2a672633
    0x26360x2a67: v2a672636(0x40) = CONST 
    0x26380x2a67: v2a672638 = MLOAD v2a672636(0x40)
    0x263a0x2a67: v2a67263a = ADD v2ae1, v2ae7(0x94)
    0x263d0x2a67: v2a67263d = SUB v2a67263a, v2a672638
    0x26400x2a67: v2a672640 = SHA3 v2a672638, v2a67263d
    0x264b0x2a67: RETURNPRIVATE v2a67arg4, v2a672640

}

function approve(address,uint256)() public {
    Begin block 0x2c6
    prev=[], succ=[0x2ce, 0x2d2]
    =================================
    0x2c7: v2c7 = CALLVALUE 
    0x2c9: v2c9 = ISZERO v2c7
    0x2ca: v2ca(0x2d2) = CONST 
    0x2cd: JUMPI v2ca(0x2d2), v2c9

    Begin block 0x2ce
    prev=[0x2c6], succ=[]
    =================================
    0x2ce: v2ce(0x0) = CONST 
    0x2d1: REVERT v2ce(0x0), v2ce(0x0)

    Begin block 0x2d2
    prev=[0x2c6], succ=[0x9c3]
    =================================
    0x2d4: v2d4(0x4af1) = CONST 
    0x2d7: v2d7(0x1) = CONST 
    0x2d9: v2d9(0xa0) = CONST 
    0x2db: v2db(0x2) = CONST 
    0x2dd: v2dd(0x10000000000000000000000000000000000000000) = EXP v2db(0x2), v2d9(0xa0)
    0x2de: v2de(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2dd(0x10000000000000000000000000000000000000000), v2d7(0x1)
    0x2df: v2df(0x4) = CONST 
    0x2e1: v2e1 = CALLDATALOAD v2df(0x4)
    0x2e2: v2e2 = AND v2e1, v2de(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e3: v2e3(0x24) = CONST 
    0x2e5: v2e5 = CALLDATALOAD v2e3(0x24)
    0x2e6: v2e6(0x9c3) = CONST 
    0x2e9: JUMP v2e6(0x9c3)

    Begin block 0x9c3
    prev=[0x2d2], succ=[0xa12, 0xa16]
    =================================
    0x9c4: v9c4(0x3) = CONST 
    0x9c6: v9c6 = SLOAD v9c4(0x3)
    0x9c7: v9c7(0x40) = CONST 
    0x9ca: v9ca = MLOAD v9c7(0x40)
    0x9cb: v9cb(0xe0) = CONST 
    0x9cd: v9cd(0x2) = CONST 
    0x9cf: v9cf(0x100000000000000000000000000000000000000000000000000000000) = EXP v9cd(0x2), v9cb(0xe0)
    0x9d0: v9d0(0x7ccce851) = CONST 
    0x9d5: v9d5(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v9d0(0x7ccce851), v9cf(0x100000000000000000000000000000000000000000000000000000000)
    0x9d7: MSTORE v9ca, v9d5(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x9d8: v9d8(0x1) = CONST 
    0x9da: v9da(0xa0) = CONST 
    0x9dc: v9dc(0x2) = CONST 
    0x9de: v9de(0x10000000000000000000000000000000000000000) = EXP v9dc(0x2), v9da(0xa0)
    0x9df: v9df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9de(0x10000000000000000000000000000000000000000), v9d8(0x1)
    0x9e2: v9e2 = AND v2e2, v9df(0xffffffffffffffffffffffffffffffffffffffff)
    0x9e3: v9e3(0x4) = CONST 
    0x9e6: v9e6 = ADD v9ca, v9e3(0x4)
    0x9e7: MSTORE v9e6, v9e2
    0x9e9: v9e9 = MLOAD v9c7(0x40)
    0x9ea: v9ea(0x0) = CONST 
    0x9ef: v9ef = AND v9df(0xffffffffffffffffffffffffffffffffffffffff), v9c6
    0x9f1: v9f1(0x7ccce851) = CONST 
    0x9f7: v9f7(0x24) = CONST 
    0x9fb: v9fb = ADD v9ca, v9f7(0x24)
    0x9fd: v9fd(0x20) = CONST 
    0xa04: va04(0x0) = SUB v9ca, v9e9
    0xa05: va05(0x24) = ADD va04(0x0), v9f7(0x24)
    0xa0a: va0a = EXTCODESIZE v9ef
    0xa0b: va0b = ISZERO va0a
    0xa0d: va0d = ISZERO va0b
    0xa0e: va0e(0xa16) = CONST 
    0xa11: JUMPI va0e(0xa16), va0d

    Begin block 0xa12
    prev=[0x9c3], succ=[]
    =================================
    0xa12: va12(0x0) = CONST 
    0xa15: REVERT va12(0x0), va12(0x0)

    Begin block 0xa16
    prev=[0x9c3], succ=[0xa21, 0xa2a]
    =================================
    0xa18: va18 = GAS 
    0xa19: va19 = CALL va18, v9ef, v9ea(0x0), v9e9, va05(0x24), v9e9, v9fd(0x20)
    0xa1a: va1a = ISZERO va19
    0xa1c: va1c = ISZERO va1a
    0xa1d: va1d(0xa2a) = CONST 
    0xa20: JUMPI va1d(0xa2a), va1c

    Begin block 0xa21
    prev=[0xa16], succ=[]
    =================================
    0xa21: va21 = RETURNDATASIZE 
    0xa22: va22(0x0) = CONST 
    0xa25: RETURNDATACOPY va22(0x0), va22(0x0), va21
    0xa26: va26 = RETURNDATASIZE 
    0xa27: va27(0x0) = CONST 
    0xa29: REVERT va27(0x0), va26

    Begin block 0xa2a
    prev=[0xa16], succ=[0xa3c, 0xa40]
    =================================
    0xa2f: va2f(0x40) = CONST 
    0xa31: va31 = MLOAD va2f(0x40)
    0xa32: va32 = RETURNDATASIZE 
    0xa33: va33(0x20) = CONST 
    0xa36: va36 = LT va32, va33(0x20)
    0xa37: va37 = ISZERO va36
    0xa38: va38(0xa40) = CONST 
    0xa3b: JUMPI va38(0xa40), va37

    Begin block 0xa3c
    prev=[0xa2a], succ=[]
    =================================
    0xa3c: va3c(0x0) = CONST 
    0xa3f: REVERT va3c(0x0), va3c(0x0)

    Begin block 0xa40
    prev=[0xa2a], succ=[0xa48, 0xa85]
    =================================
    0xa42: va42 = MLOAD va31
    0xa43: va43 = ISZERO va42
    0xa44: va44(0xa85) = CONST 
    0xa47: JUMPI va44(0xa85), va43

    Begin block 0xa48
    prev=[0xa40], succ=[]
    =================================
    0xa48: va48(0x40) = CONST 
    0xa4b: va4b = MLOAD va48(0x40)
    0xa4c: va4c(0xe5) = CONST 
    0xa4e: va4e(0x2) = CONST 
    0xa50: va50(0x2000000000000000000000000000000000000000000000000000000000) = EXP va4e(0x2), va4c(0xe5)
    0xa51: va51(0x461bcd) = CONST 
    0xa55: va55(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL va51(0x461bcd), va50(0x2000000000000000000000000000000000000000000000000000000000)
    0xa57: MSTORE va4b, va55(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa58: va58(0x20) = CONST 
    0xa5a: va5a(0x4) = CONST 
    0xa5d: va5d = ADD va4b, va5a(0x4)
    0xa5e: MSTORE va5d, va58(0x20)
    0xa5f: va5f(0x1c) = CONST 
    0xa61: va61(0x24) = CONST 
    0xa64: va64 = ADD va4b, va61(0x24)
    0xa65: MSTORE va64, va5f(0x1c)
    0xa66: va66(0x0) = CONST 
    0xa69: va69 = MLOAD va66(0x0)
    0xa6a: va6a(0x20) = CONST 
    0xa6c: va6c(0x4a70) = CONST 
    0xa74: MSTORE va66(0x0), va69
    0xa75: va75(0x44) = CONST 
    0xa78: va78 = ADD va4b, va75(0x44)
    0xa79: MSTORE va78, v552f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0xa7b: va7b = MLOAD va48(0x40)
    0xa7f: va7f(0x0) = SUB va4b, va7b
    0xa80: va80(0x64) = CONST 
    0xa82: va82(0x64) = ADD va80(0x64), va7f(0x0)
    0xa84: REVERT va7b, va82(0x64)
    0x552f: v552f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0xa85
    prev=[0xa40], succ=[0xad3, 0xad7]
    =================================
    0xa86: va86(0x3) = CONST 
    0xa88: va88 = SLOAD va86(0x3)
    0xa89: va89(0x40) = CONST 
    0xa8c: va8c = MLOAD va89(0x40)
    0xa8d: va8d(0xe0) = CONST 
    0xa8f: va8f(0x2) = CONST 
    0xa91: va91(0x100000000000000000000000000000000000000000000000000000000) = EXP va8f(0x2), va8d(0xe0)
    0xa92: va92(0x7ccce851) = CONST 
    0xa97: va97(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL va92(0x7ccce851), va91(0x100000000000000000000000000000000000000000000000000000000)
    0xa99: MSTORE va8c, va97(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0xa9a: va9a = CALLER 
    0xa9b: va9b(0x4) = CONST 
    0xa9e: va9e = ADD va8c, va9b(0x4)
    0xaa1: MSTORE va9e, va9a
    0xaa3: vaa3 = MLOAD va89(0x40)
    0xaa6: vaa6(0x1) = CONST 
    0xaa8: vaa8(0xa0) = CONST 
    0xaaa: vaaa(0x2) = CONST 
    0xaac: vaac(0x10000000000000000000000000000000000000000) = EXP vaaa(0x2), vaa8(0xa0)
    0xaad: vaad(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaac(0x10000000000000000000000000000000000000000), vaa6(0x1)
    0xaae: vaae = AND vaad(0xffffffffffffffffffffffffffffffffffffffff), va88
    0xab0: vab0(0x7ccce851) = CONST 
    0xab6: vab6(0x24) = CONST 
    0xaba: vaba = ADD va8c, vab6(0x24)
    0xabc: vabc(0x20) = CONST 
    0xac4: vac4(0x0) = SUB va8c, vaa3
    0xac5: vac5(0x24) = ADD vac4(0x0), vab6(0x24)
    0xac7: vac7(0x0) = CONST 
    0xacb: vacb = EXTCODESIZE vaae
    0xacc: vacc = ISZERO vacb
    0xace: vace = ISZERO vacc
    0xacf: vacf(0xad7) = CONST 
    0xad2: JUMPI vacf(0xad7), vace

    Begin block 0xad3
    prev=[0xa85], succ=[]
    =================================
    0xad3: vad3(0x0) = CONST 
    0xad6: REVERT vad3(0x0), vad3(0x0)

    Begin block 0xad7
    prev=[0xa85], succ=[0xae2, 0xaeb]
    =================================
    0xad9: vad9 = GAS 
    0xada: vada = CALL vad9, vaae, vac7(0x0), vaa3, vac5(0x24), vaa3, vabc(0x20)
    0xadb: vadb = ISZERO vada
    0xadd: vadd = ISZERO vadb
    0xade: vade(0xaeb) = CONST 
    0xae1: JUMPI vade(0xaeb), vadd

    Begin block 0xae2
    prev=[0xad7], succ=[]
    =================================
    0xae2: vae2 = RETURNDATASIZE 
    0xae3: vae3(0x0) = CONST 
    0xae6: RETURNDATACOPY vae3(0x0), vae3(0x0), vae2
    0xae7: vae7 = RETURNDATASIZE 
    0xae8: vae8(0x0) = CONST 
    0xaea: REVERT vae8(0x0), vae7

    Begin block 0xaeb
    prev=[0xad7], succ=[0xafd, 0xb01]
    =================================
    0xaf0: vaf0(0x40) = CONST 
    0xaf2: vaf2 = MLOAD vaf0(0x40)
    0xaf3: vaf3 = RETURNDATASIZE 
    0xaf4: vaf4(0x20) = CONST 
    0xaf7: vaf7 = LT vaf3, vaf4(0x20)
    0xaf8: vaf8 = ISZERO vaf7
    0xaf9: vaf9(0xb01) = CONST 
    0xafc: JUMPI vaf9(0xb01), vaf8

    Begin block 0xafd
    prev=[0xaeb], succ=[]
    =================================
    0xafd: vafd(0x0) = CONST 
    0xb00: REVERT vafd(0x0), vafd(0x0)

    Begin block 0xb01
    prev=[0xaeb], succ=[0xb09, 0xb46]
    =================================
    0xb03: vb03 = MLOAD vaf2
    0xb04: vb04 = ISZERO vb03
    0xb05: vb05(0xb46) = CONST 
    0xb08: JUMPI vb05(0xb46), vb04

    Begin block 0xb09
    prev=[0xb01], succ=[]
    =================================
    0xb09: vb09(0x40) = CONST 
    0xb0c: vb0c = MLOAD vb09(0x40)
    0xb0d: vb0d(0xe5) = CONST 
    0xb0f: vb0f(0x2) = CONST 
    0xb11: vb11(0x2000000000000000000000000000000000000000000000000000000000) = EXP vb0f(0x2), vb0d(0xe5)
    0xb12: vb12(0x461bcd) = CONST 
    0xb16: vb16(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vb12(0x461bcd), vb11(0x2000000000000000000000000000000000000000000000000000000000)
    0xb18: MSTORE vb0c, vb16(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb19: vb19(0x20) = CONST 
    0xb1b: vb1b(0x4) = CONST 
    0xb1e: vb1e = ADD vb0c, vb1b(0x4)
    0xb1f: MSTORE vb1e, vb19(0x20)
    0xb20: vb20(0x1c) = CONST 
    0xb22: vb22(0x24) = CONST 
    0xb25: vb25 = ADD vb0c, vb22(0x24)
    0xb26: MSTORE vb25, vb20(0x1c)
    0xb27: vb27(0x0) = CONST 
    0xb2a: vb2a = MLOAD vb27(0x0)
    0xb2b: vb2b(0x20) = CONST 
    0xb2d: vb2d(0x4a70) = CONST 
    0xb35: MSTORE vb27(0x0), vb2a
    0xb36: vb36(0x44) = CONST 
    0xb39: vb39 = ADD vb0c, vb36(0x44)
    0xb3a: MSTORE vb39, v5534(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0xb3c: vb3c = MLOAD vb09(0x40)
    0xb40: vb40(0x0) = SUB vb0c, vb3c
    0xb41: vb41(0x64) = CONST 
    0xb43: vb43(0x64) = ADD vb41(0x64), vb40(0x0)
    0xb45: REVERT vb3c, vb43(0x64)
    0x5534: v5534(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0xb46
    prev=[0xb01], succ=[0xb59, 0xb5d]
    =================================
    0xb47: vb47(0x1) = CONST 
    0xb49: vb49 = SLOAD vb47(0x1)
    0xb4a: vb4a(0xa0) = CONST 
    0xb4c: vb4c(0x2) = CONST 
    0xb4e: vb4e(0x10000000000000000000000000000000000000000) = EXP vb4c(0x2), vb4a(0xa0)
    0xb50: vb50 = DIV vb49, vb4e(0x10000000000000000000000000000000000000000)
    0xb51: vb51(0xff) = CONST 
    0xb53: vb53 = AND vb51(0xff), vb50
    0xb54: vb54 = ISZERO vb53
    0xb55: vb55(0xb5d) = CONST 
    0xb58: JUMPI vb55(0xb5d), vb54

    Begin block 0xb59
    prev=[0xb46], succ=[]
    =================================
    0xb59: vb59(0x0) = CONST 
    0xb5c: REVERT vb59(0x0), vb59(0x0)

    Begin block 0xb5d
    prev=[0xb46], succ=[0xb83, 0xb87]
    =================================
    0xb5e: vb5e(0x1) = CONST 
    0xb60: vb60 = SLOAD vb5e(0x1)
    0xb61: vb61(0x1000000000000000000000000000000000000000000) = CONST 
    0xb79: vb79 = DIV vb60, vb61(0x1000000000000000000000000000000000000000000)
    0xb7a: vb7a(0xff) = CONST 
    0xb7c: vb7c = AND vb7a(0xff), vb79
    0xb7d: vb7d = ISZERO vb7c
    0xb7e: vb7e = ISZERO vb7d
    0xb7f: vb7f(0xb87) = CONST 
    0xb82: JUMPI vb7f(0xb87), vb7e

    Begin block 0xb83
    prev=[0xb5d], succ=[]
    =================================
    0xb83: vb83(0x0) = CONST 
    0xb86: REVERT vb83(0x0), vb83(0x0)

    Begin block 0xb87
    prev=[0xb5d], succ=[0xbf7, 0xbfb]
    =================================
    0xb88: vb88(0x2) = CONST 
    0xb8a: vb8a = SLOAD vb88(0x2)
    0xb8b: vb8b(0x40) = CONST 
    0xb8e: vb8e = MLOAD vb8b(0x40)
    0xb8f: vb8f(0xda46098c00000000000000000000000000000000000000000000000000000000) = CONST 
    0xbb1: MSTORE vb8e, vb8f(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0xbb2: vbb2 = CALLER 
    0xbb3: vbb3(0x4) = CONST 
    0xbb6: vbb6 = ADD vb8e, vbb3(0x4)
    0xbb7: MSTORE vbb6, vbb2
    0xbb8: vbb8(0x1) = CONST 
    0xbba: vbba(0xa0) = CONST 
    0xbbc: vbbc(0x2) = CONST 
    0xbbe: vbbe(0x10000000000000000000000000000000000000000) = EXP vbbc(0x2), vbba(0xa0)
    0xbbf: vbbf(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbbe(0x10000000000000000000000000000000000000000), vbb8(0x1)
    0xbc2: vbc2 = AND vbbf(0xffffffffffffffffffffffffffffffffffffffff), v2e2
    0xbc3: vbc3(0x24) = CONST 
    0xbc6: vbc6 = ADD vb8e, vbc3(0x24)
    0xbc7: MSTORE vbc6, vbc2
    0xbc8: vbc8(0x44) = CONST 
    0xbcb: vbcb = ADD vb8e, vbc8(0x44)
    0xbce: MSTORE vbcb, v2e5
    0xbd0: vbd0 = MLOAD vb8b(0x40)
    0xbd4: vbd4 = AND vb8a, vbbf(0xffffffffffffffffffffffffffffffffffffffff)
    0xbd6: vbd6(0xda46098c) = CONST 
    0xbdc: vbdc(0x64) = CONST 
    0xbe0: vbe0 = ADD vb8e, vbdc(0x64)
    0xbe2: vbe2(0x0) = CONST 
    0xbe9: vbe9(0x0) = SUB vb8e, vbd0
    0xbea: vbea(0x64) = ADD vbe9(0x0), vbdc(0x64)
    0xbef: vbef = EXTCODESIZE vbd4
    0xbf0: vbf0 = ISZERO vbef
    0xbf2: vbf2 = ISZERO vbf0
    0xbf3: vbf3(0xbfb) = CONST 
    0xbf6: JUMPI vbf3(0xbfb), vbf2

    Begin block 0xbf7
    prev=[0xb87], succ=[]
    =================================
    0xbf7: vbf7(0x0) = CONST 
    0xbfa: REVERT vbf7(0x0), vbf7(0x0)

    Begin block 0xbfb
    prev=[0xb87], succ=[0xc06, 0xc0f]
    =================================
    0xbfd: vbfd = GAS 
    0xbfe: vbfe = CALL vbfd, vbd4, vbe2(0x0), vbd0, vbea(0x64), vbd0, vbe2(0x0)
    0xbff: vbff = ISZERO vbfe
    0xc01: vc01 = ISZERO vbff
    0xc02: vc02(0xc0f) = CONST 
    0xc05: JUMPI vc02(0xc0f), vc01

    Begin block 0xc06
    prev=[0xbfb], succ=[]
    =================================
    0xc06: vc06 = RETURNDATASIZE 
    0xc07: vc07(0x0) = CONST 
    0xc0a: RETURNDATACOPY vc07(0x0), vc07(0x0), vc06
    0xc0b: vc0b = RETURNDATASIZE 
    0xc0c: vc0c(0x0) = CONST 
    0xc0e: REVERT vc0c(0x0), vc0b

    Begin block 0xc0f
    prev=[0xbfb], succ=[0x4af1]
    =================================
    0xc12: vc12(0x40) = CONST 
    0xc15: vc15 = MLOAD vc12(0x40)
    0xc18: MSTORE vc15, v2e5
    0xc1a: vc1a = MLOAD vc12(0x40)
    0xc1b: vc1b(0x1) = CONST 
    0xc1d: vc1d(0xa0) = CONST 
    0xc1f: vc1f(0x2) = CONST 
    0xc21: vc21(0x10000000000000000000000000000000000000000) = EXP vc1f(0x2), vc1d(0xa0)
    0xc22: vc22(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc21(0x10000000000000000000000000000000000000000), vc1b(0x1)
    0xc24: vc24 = AND v2e2, vc22(0xffffffffffffffffffffffffffffffffffffffff)
    0xc27: vc27 = CALLER 
    0xc2a: vc2a(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xc4e: vc4e(0x0) = SUB vc15, vc1a
    0xc4f: vc4f(0x20) = CONST 
    0xc51: vc51(0x20) = ADD vc4f(0x20), vc4e(0x0)
    0xc53: LOG3 vc1a, vc51(0x20), vc2a(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vc27, vc24
    0xc55: vc55(0x1) = CONST 
    0xc5d: JUMP v2d4(0x4af1)

    Begin block 0x4af1
    prev=[0xc0f], succ=[]
    =================================
    0x4af2: v4af2(0x40) = CONST 
    0x4af5: v4af5 = MLOAD v4af2(0x40)
    0x4af7: v4af7 = ISZERO vc55(0x1)
    0x4af8: v4af8 = ISZERO v4af7
    0x4afa: MSTORE v4af5, v4af8
    0x4afb: v4afb = MLOAD v4af2(0x40)
    0x4aff: v4aff(0x0) = SUB v4af5, v4afb
    0x4b00: v4b00(0x20) = CONST 
    0x4b02: v4b02(0x20) = ADD v4b00(0x20), v4aff(0x0)
    0x4b04: RETURN v4afb, v4b02(0x20)

}

function convertCarbonDollar(address,uint256)() public {
    Begin block 0x2fe
    prev=[], succ=[0x306, 0x30a]
    =================================
    0x2ff: v2ff = CALLVALUE 
    0x301: v301 = ISZERO v2ff
    0x302: v302(0x30a) = CONST 
    0x305: JUMPI v302(0x30a), v301

    Begin block 0x306
    prev=[0x2fe], succ=[]
    =================================
    0x306: v306(0x0) = CONST 
    0x309: REVERT v306(0x0), v306(0x0)

    Begin block 0x30a
    prev=[0x2fe], succ=[0xc5e]
    =================================
    0x30c: v30c(0x4b24) = CONST 
    0x30f: v30f(0x1) = CONST 
    0x311: v311(0xa0) = CONST 
    0x313: v313(0x2) = CONST 
    0x315: v315(0x10000000000000000000000000000000000000000) = EXP v313(0x2), v311(0xa0)
    0x316: v316(0xffffffffffffffffffffffffffffffffffffffff) = SUB v315(0x10000000000000000000000000000000000000000), v30f(0x1)
    0x317: v317(0x4) = CONST 
    0x319: v319 = CALLDATALOAD v317(0x4)
    0x31a: v31a = AND v319, v316(0xffffffffffffffffffffffffffffffffffffffff)
    0x31b: v31b(0x24) = CONST 
    0x31d: v31d = CALLDATALOAD v31b(0x24)
    0x31e: v31e(0xc5e) = CONST 
    0x321: JUMP v31e(0xc5e)

    Begin block 0xc5e
    prev=[0x30a], succ=[0xcb4, 0xcb8]
    =================================
    0xc5f: vc5f(0x3) = CONST 
    0xc61: vc61 = SLOAD vc5f(0x3)
    0xc62: vc62(0x40) = CONST 
    0xc65: vc65 = MLOAD vc62(0x40)
    0xc66: vc66(0xe0) = CONST 
    0xc68: vc68(0x2) = CONST 
    0xc6a: vc6a(0x100000000000000000000000000000000000000000000000000000000) = EXP vc68(0x2), vc66(0xe0)
    0xc6b: vc6b(0x7ccce851) = CONST 
    0xc70: vc70(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL vc6b(0x7ccce851), vc6a(0x100000000000000000000000000000000000000000000000000000000)
    0xc72: MSTORE vc65, vc70(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0xc73: vc73 = CALLER 
    0xc74: vc74(0x4) = CONST 
    0xc77: vc77 = ADD vc65, vc74(0x4)
    0xc7a: MSTORE vc77, vc73
    0xc7c: vc7c = MLOAD vc62(0x40)
    0xc7d: vc7d(0x0) = CONST 
    0xc86: vc86(0x1) = CONST 
    0xc88: vc88(0xa0) = CONST 
    0xc8a: vc8a(0x2) = CONST 
    0xc8c: vc8c(0x10000000000000000000000000000000000000000) = EXP vc8a(0x2), vc88(0xa0)
    0xc8d: vc8d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc8c(0x10000000000000000000000000000000000000000), vc86(0x1)
    0xc90: vc90 = AND vc61, vc8d(0xffffffffffffffffffffffffffffffffffffffff)
    0xc92: vc92(0x7ccce851) = CONST 
    0xc98: vc98(0x24) = CONST 
    0xc9c: vc9c = ADD vc65, vc98(0x24)
    0xc9e: vc9e(0x20) = CONST 
    0xca6: vca6(0x0) = SUB vc65, vc7c
    0xca7: vca7(0x24) = ADD vca6(0x0), vc98(0x24)
    0xcac: vcac = EXTCODESIZE vc90
    0xcad: vcad = ISZERO vcac
    0xcaf: vcaf = ISZERO vcad
    0xcb0: vcb0(0xcb8) = CONST 
    0xcb3: JUMPI vcb0(0xcb8), vcaf

    Begin block 0xcb4
    prev=[0xc5e], succ=[]
    =================================
    0xcb4: vcb4(0x0) = CONST 
    0xcb7: REVERT vcb4(0x0), vcb4(0x0)

    Begin block 0xcb8
    prev=[0xc5e], succ=[0xcc3, 0xccc]
    =================================
    0xcba: vcba = GAS 
    0xcbb: vcbb = CALL vcba, vc90, vc7d(0x0), vc7c, vca7(0x24), vc7c, vc9e(0x20)
    0xcbc: vcbc = ISZERO vcbb
    0xcbe: vcbe = ISZERO vcbc
    0xcbf: vcbf(0xccc) = CONST 
    0xcc2: JUMPI vcbf(0xccc), vcbe

    Begin block 0xcc3
    prev=[0xcb8], succ=[]
    =================================
    0xcc3: vcc3 = RETURNDATASIZE 
    0xcc4: vcc4(0x0) = CONST 
    0xcc7: RETURNDATACOPY vcc4(0x0), vcc4(0x0), vcc3
    0xcc8: vcc8 = RETURNDATASIZE 
    0xcc9: vcc9(0x0) = CONST 
    0xccb: REVERT vcc9(0x0), vcc8

    Begin block 0xccc
    prev=[0xcb8], succ=[0xcde, 0xce2]
    =================================
    0xcd1: vcd1(0x40) = CONST 
    0xcd3: vcd3 = MLOAD vcd1(0x40)
    0xcd4: vcd4 = RETURNDATASIZE 
    0xcd5: vcd5(0x20) = CONST 
    0xcd8: vcd8 = LT vcd4, vcd5(0x20)
    0xcd9: vcd9 = ISZERO vcd8
    0xcda: vcda(0xce2) = CONST 
    0xcdd: JUMPI vcda(0xce2), vcd9

    Begin block 0xcde
    prev=[0xccc], succ=[]
    =================================
    0xcde: vcde(0x0) = CONST 
    0xce1: REVERT vcde(0x0), vcde(0x0)

    Begin block 0xce2
    prev=[0xccc], succ=[0xcea, 0xd27]
    =================================
    0xce4: vce4 = MLOAD vcd3
    0xce5: vce5 = ISZERO vce4
    0xce6: vce6(0xd27) = CONST 
    0xce9: JUMPI vce6(0xd27), vce5

    Begin block 0xcea
    prev=[0xce2], succ=[]
    =================================
    0xcea: vcea(0x40) = CONST 
    0xced: vced = MLOAD vcea(0x40)
    0xcee: vcee(0xe5) = CONST 
    0xcf0: vcf0(0x2) = CONST 
    0xcf2: vcf2(0x2000000000000000000000000000000000000000000000000000000000) = EXP vcf0(0x2), vcee(0xe5)
    0xcf3: vcf3(0x461bcd) = CONST 
    0xcf7: vcf7(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vcf3(0x461bcd), vcf2(0x2000000000000000000000000000000000000000000000000000000000)
    0xcf9: MSTORE vced, vcf7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xcfa: vcfa(0x20) = CONST 
    0xcfc: vcfc(0x4) = CONST 
    0xcff: vcff = ADD vced, vcfc(0x4)
    0xd00: MSTORE vcff, vcfa(0x20)
    0xd01: vd01(0x1c) = CONST 
    0xd03: vd03(0x24) = CONST 
    0xd06: vd06 = ADD vced, vd03(0x24)
    0xd07: MSTORE vd06, vd01(0x1c)
    0xd08: vd08(0x0) = CONST 
    0xd0b: vd0b = MLOAD vd08(0x0)
    0xd0c: vd0c(0x20) = CONST 
    0xd0e: vd0e(0x4a70) = CONST 
    0xd16: MSTORE vd08(0x0), vd0b
    0xd17: vd17(0x44) = CONST 
    0xd1a: vd1a = ADD vced, vd17(0x44)
    0xd1b: MSTORE vd1a, v5539(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0xd1d: vd1d = MLOAD vcea(0x40)
    0xd21: vd21(0x0) = SUB vced, vd1d
    0xd22: vd22(0x64) = CONST 
    0xd24: vd24(0x64) = ADD vd22(0x64), vd21(0x0)
    0xd26: REVERT vd1d, vd24(0x64)
    0x5539: v5539(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0xd27
    prev=[0xce2], succ=[0xd3a, 0xd3e]
    =================================
    0xd28: vd28(0x1) = CONST 
    0xd2a: vd2a = SLOAD vd28(0x1)
    0xd2b: vd2b(0xa0) = CONST 
    0xd2d: vd2d(0x2) = CONST 
    0xd2f: vd2f(0x10000000000000000000000000000000000000000) = EXP vd2d(0x2), vd2b(0xa0)
    0xd31: vd31 = DIV vd2a, vd2f(0x10000000000000000000000000000000000000000)
    0xd32: vd32(0xff) = CONST 
    0xd34: vd34 = AND vd32(0xff), vd31
    0xd35: vd35 = ISZERO vd34
    0xd36: vd36(0xd3e) = CONST 
    0xd39: JUMPI vd36(0xd3e), vd35

    Begin block 0xd3a
    prev=[0xd27], succ=[]
    =================================
    0xd3a: vd3a(0x0) = CONST 
    0xd3d: REVERT vd3a(0x0), vd3a(0x0)

    Begin block 0xd3e
    prev=[0xd27], succ=[0xd47]
    =================================
    0xd3f: vd3f(0xd47) = CONST 
    0xd43: vd43(0x162d) = CONST 
    0xd46: vd46_0 = CALLPRIVATE vd43(0x162d), v31a, vd3f(0xd47)

    Begin block 0xd47
    prev=[0xd3e], succ=[0xd4e, 0xdb1]
    =================================
    0xd48: vd48 = ISZERO vd46_0
    0xd49: vd49 = ISZERO vd48
    0xd4a: vd4a(0xdb1) = CONST 
    0xd4d: JUMPI vd4a(0xdb1), vd49

    Begin block 0xd4e
    prev=[0xd47], succ=[]
    =================================
    0xd4e: vd4e(0x40) = CONST 
    0xd51: vd51 = MLOAD vd4e(0x40)
    0xd52: vd52(0xe5) = CONST 
    0xd54: vd54(0x2) = CONST 
    0xd56: vd56(0x2000000000000000000000000000000000000000000000000000000000) = EXP vd54(0x2), vd52(0xe5)
    0xd57: vd57(0x461bcd) = CONST 
    0xd5b: vd5b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vd57(0x461bcd), vd56(0x2000000000000000000000000000000000000000000000000000000000)
    0xd5d: MSTORE vd51, vd5b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd5e: vd5e(0x20) = CONST 
    0xd60: vd60(0x4) = CONST 
    0xd63: vd63 = ADD vd51, vd60(0x4)
    0xd64: MSTORE vd63, vd5e(0x20)
    0xd65: vd65(0x3e) = CONST 
    0xd67: vd67(0x24) = CONST 
    0xd6a: vd6a = ADD vd51, vd67(0x24)
    0xd6b: MSTORE vd6a, vd65(0x3e)
    0xd6c: vd6c(0x0) = CONST 
    0xd6f: vd6f = MLOAD vd6c(0x0)
    0xd70: vd70(0x20) = CONST 
    0xd72: vd72(0x4a50) = CONST 
    0xd7a: MSTORE vd6c(0x0), vd6f
    0xd7b: vd7b(0x44) = CONST 
    0xd7e: vd7e = ADD vd51, vd7b(0x44)
    0xd7f: MSTORE vd7e, v553e(0x537461626c65636f696e206d7573742062652077686974656c69737465642070)
    0xd80: vd80(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000) = CONST 
    0xda1: vda1(0x64) = CONST 
    0xda4: vda4 = ADD vd51, vda1(0x64)
    0xda5: MSTORE vda4, vd80(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000)
    0xda7: vda7 = MLOAD vd4e(0x40)
    0xdab: vdab(0x0) = SUB vd51, vda7
    0xdac: vdac(0x84) = CONST 
    0xdae: vdae(0x84) = ADD vdac(0x84), vdab(0x0)
    0xdb0: REVERT vda7, vdae(0x84)
    0x553e: v553e(0x537461626c65636f696e206d7573742062652077686974656c69737465642070) = CONST 

    Begin block 0xdb1
    prev=[0xd47], succ=[0xe14, 0xe18]
    =================================
    0xdb2: vdb2(0x40) = CONST 
    0xdb5: vdb5 = MLOAD vdb2(0x40)
    0xdb6: vdb6(0x70a0823100000000000000000000000000000000000000000000000000000000) = CONST 
    0xdd8: MSTORE vdb5, vdb6(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0xdd9: vdd9 = ADDRESS 
    0xdda: vdda(0x4) = CONST 
    0xddd: vddd = ADD vdb5, vdda(0x4)
    0xdde: MSTORE vddd, vdd9
    0xde0: vde0 = MLOAD vdb2(0x40)
    0xde6: vde6(0x1) = CONST 
    0xde8: vde8(0xa0) = CONST 
    0xdea: vdea(0x2) = CONST 
    0xdec: vdec(0x10000000000000000000000000000000000000000) = EXP vdea(0x2), vde8(0xa0)
    0xded: vded(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdec(0x10000000000000000000000000000000000000000), vde6(0x1)
    0xdef: vdef = AND v31a, vded(0xffffffffffffffffffffffffffffffffffffffff)
    0xdf1: vdf1(0x70a08231) = CONST 
    0xdf7: vdf7(0x24) = CONST 
    0xdfb: vdfb = ADD vdb5, vdf7(0x24)
    0xdfd: vdfd(0x20) = CONST 
    0xe05: ve05(0x0) = SUB vdb5, vde0
    0xe06: ve06(0x24) = ADD ve05(0x0), vdf7(0x24)
    0xe08: ve08(0x0) = CONST 
    0xe0c: ve0c = EXTCODESIZE vdef
    0xe0d: ve0d = ISZERO ve0c
    0xe0f: ve0f = ISZERO ve0d
    0xe10: ve10(0xe18) = CONST 
    0xe13: JUMPI ve10(0xe18), ve0f

    Begin block 0xe14
    prev=[0xdb1], succ=[]
    =================================
    0xe14: ve14(0x0) = CONST 
    0xe17: REVERT ve14(0x0), ve14(0x0)

    Begin block 0xe18
    prev=[0xdb1], succ=[0xe23, 0xe2c]
    =================================
    0xe1a: ve1a = GAS 
    0xe1b: ve1b = CALL ve1a, vdef, ve08(0x0), vde0, ve06(0x24), vde0, vdfd(0x20)
    0xe1c: ve1c = ISZERO ve1b
    0xe1e: ve1e = ISZERO ve1c
    0xe1f: ve1f(0xe2c) = CONST 
    0xe22: JUMPI ve1f(0xe2c), ve1e

    Begin block 0xe23
    prev=[0xe18], succ=[]
    =================================
    0xe23: ve23 = RETURNDATASIZE 
    0xe24: ve24(0x0) = CONST 
    0xe27: RETURNDATACOPY ve24(0x0), ve24(0x0), ve23
    0xe28: ve28 = RETURNDATASIZE 
    0xe29: ve29(0x0) = CONST 
    0xe2b: REVERT ve29(0x0), ve28

    Begin block 0xe2c
    prev=[0xe18], succ=[0xe3e, 0xe42]
    =================================
    0xe31: ve31(0x40) = CONST 
    0xe33: ve33 = MLOAD ve31(0x40)
    0xe34: ve34 = RETURNDATASIZE 
    0xe35: ve35(0x20) = CONST 
    0xe38: ve38 = LT ve34, ve35(0x20)
    0xe39: ve39 = ISZERO ve38
    0xe3a: ve3a(0xe42) = CONST 
    0xe3d: JUMPI ve3a(0xe42), ve39

    Begin block 0xe3e
    prev=[0xe2c], succ=[]
    =================================
    0xe3e: ve3e(0x0) = CONST 
    0xe41: REVERT ve3e(0x0), ve3e(0x0)

    Begin block 0xe42
    prev=[0xe2c], succ=[0xe4b, 0xee6]
    =================================
    0xe44: ve44 = MLOAD ve33
    0xe45: ve45 = LT ve44, v31d
    0xe46: ve46 = ISZERO ve45
    0xe47: ve47(0xee6) = CONST 
    0xe4a: JUMPI ve47(0xee6), ve46

    Begin block 0xe4b
    prev=[0xe42], succ=[]
    =================================
    0xe4b: ve4b(0x40) = CONST 
    0xe4e: ve4e = MLOAD ve4b(0x40)
    0xe4f: ve4f(0xe5) = CONST 
    0xe51: ve51(0x2) = CONST 
    0xe53: ve53(0x2000000000000000000000000000000000000000000000000000000000) = EXP ve51(0x2), ve4f(0xe5)
    0xe54: ve54(0x461bcd) = CONST 
    0xe58: ve58(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL ve54(0x461bcd), ve53(0x2000000000000000000000000000000000000000000000000000000000)
    0xe5a: MSTORE ve4e, ve58(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe5b: ve5b(0x20) = CONST 
    0xe5d: ve5d(0x4) = CONST 
    0xe60: ve60 = ADD ve4e, ve5d(0x4)
    0xe61: MSTORE ve60, ve5b(0x20)
    0xe62: ve62(0x43) = CONST 
    0xe64: ve64(0x24) = CONST 
    0xe67: ve67 = ADD ve4e, ve64(0x24)
    0xe68: MSTORE ve67, ve62(0x43)
    0xe69: ve69(0x436172626f6e20657363726f77206163636f756e7420696e2057543020646f65) = CONST 
    0xe8a: ve8a(0x44) = CONST 
    0xe8d: ve8d = ADD ve4e, ve8a(0x44)
    0xe8e: MSTORE ve8d, ve69(0x436172626f6e20657363726f77206163636f756e7420696e2057543020646f65)
    0xe8f: ve8f(0x736e2774206861766520656e6f75676820746f6b656e7320666f72206275726e) = CONST 
    0xeb0: veb0(0x64) = CONST 
    0xeb3: veb3 = ADD ve4e, veb0(0x64)
    0xeb4: MSTORE veb3, ve8f(0x736e2774206861766520656e6f75676820746f6b656e7320666f72206275726e)
    0xeb5: veb5(0x696e670000000000000000000000000000000000000000000000000000000000) = CONST 
    0xed6: ved6(0x84) = CONST 
    0xed9: ved9 = ADD ve4e, ved6(0x84)
    0xeda: MSTORE ved9, veb5(0x696e670000000000000000000000000000000000000000000000000000000000)
    0xedc: vedc = MLOAD ve4b(0x40)
    0xee0: vee0(0x0) = SUB ve4e, vedc
    0xee1: vee1(0xa4) = CONST 
    0xee3: vee3(0xa4) = ADD vee1(0xa4), vee0(0x0)
    0xee5: REVERT vedc, vee3(0xa4)

    Begin block 0xee6
    prev=[0xe42], succ=[0xf01]
    =================================
    0xee7: vee7(0x4) = CONST 
    0xee9: vee9 = SLOAD vee7(0x4)
    0xeea: veea(0x1) = CONST 
    0xeec: veec(0xa0) = CONST 
    0xeee: veee(0x2) = CONST 
    0xef0: vef0(0x10000000000000000000000000000000000000000) = EXP veee(0x2), veec(0xa0)
    0xef1: vef1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vef0(0x10000000000000000000000000000000000000000), veea(0x1)
    0xef2: vef2 = AND vef1(0xffffffffffffffffffffffffffffffffffffffff), vee9
    0xef3: vef3(0x2ff284c2) = CONST 
    0xef9: vef9(0xf01) = CONST 
    0xefd: vefd(0x24f9) = CONST 
    0xf00: vf00_0 = CALLPRIVATE vefd(0x24f9), v31a, vef9(0xf01)

    Begin block 0xf01
    prev=[0xee6], succ=[0xf3d, 0xf41]
    =================================
    0xf02: vf02(0x40) = CONST 
    0xf04: vf04 = MLOAD vf02(0x40)
    0xf06: vf06(0xffffffff) = CONST 
    0xf0b: vf0b(0x2ff284c2) = AND vf06(0xffffffff), vef3(0x2ff284c2)
    0xf0c: vf0c(0xe0) = CONST 
    0xf0e: vf0e(0x2) = CONST 
    0xf10: vf10(0x100000000000000000000000000000000000000000000000000000000) = EXP vf0e(0x2), vf0c(0xe0)
    0xf11: vf11(0x2ff284c200000000000000000000000000000000000000000000000000000000) = MUL vf10(0x100000000000000000000000000000000000000000000000000000000), vf0b(0x2ff284c2)
    0xf13: MSTORE vf04, vf11(0x2ff284c200000000000000000000000000000000000000000000000000000000)
    0xf14: vf14(0x4) = CONST 
    0xf16: vf16 = ADD vf14(0x4), vf04
    0xf1a: MSTORE vf16, v31d
    0xf1b: vf1b(0x20) = CONST 
    0xf1d: vf1d = ADD vf1b(0x20), vf16
    0xf20: MSTORE vf1d, vf00_0
    0xf21: vf21(0x20) = CONST 
    0xf23: vf23 = ADD vf21(0x20), vf1d
    0xf28: vf28(0x20) = CONST 
    0xf2a: vf2a(0x40) = CONST 
    0xf2c: vf2c = MLOAD vf2a(0x40)
    0xf2f: vf2f(0x44) = SUB vf23, vf2c
    0xf31: vf31(0x0) = CONST 
    0xf35: vf35 = EXTCODESIZE vef2
    0xf36: vf36 = ISZERO vf35
    0xf38: vf38 = ISZERO vf36
    0xf39: vf39(0xf41) = CONST 
    0xf3c: JUMPI vf39(0xf41), vf38

    Begin block 0xf3d
    prev=[0xf01], succ=[]
    =================================
    0xf3d: vf3d(0x0) = CONST 
    0xf40: REVERT vf3d(0x0), vf3d(0x0)

    Begin block 0xf41
    prev=[0xf01], succ=[0xf4c, 0xf55]
    =================================
    0xf43: vf43 = GAS 
    0xf44: vf44 = CALL vf43, vef2, vf31(0x0), vf2c, vf2f(0x44), vf2c, vf28(0x20)
    0xf45: vf45 = ISZERO vf44
    0xf47: vf47 = ISZERO vf45
    0xf48: vf48(0xf55) = CONST 
    0xf4b: JUMPI vf48(0xf55), vf47

    Begin block 0xf4c
    prev=[0xf41], succ=[]
    =================================
    0xf4c: vf4c = RETURNDATASIZE 
    0xf4d: vf4d(0x0) = CONST 
    0xf50: RETURNDATACOPY vf4d(0x0), vf4d(0x0), vf4c
    0xf51: vf51 = RETURNDATASIZE 
    0xf52: vf52(0x0) = CONST 
    0xf54: REVERT vf52(0x0), vf51

    Begin block 0xf55
    prev=[0xf41], succ=[0xf67, 0xf6b]
    =================================
    0xf5a: vf5a(0x40) = CONST 
    0xf5c: vf5c = MLOAD vf5a(0x40)
    0xf5d: vf5d = RETURNDATASIZE 
    0xf5e: vf5e(0x20) = CONST 
    0xf61: vf61 = LT vf5d, vf5e(0x20)
    0xf62: vf62 = ISZERO vf61
    0xf63: vf63(0xf6b) = CONST 
    0xf66: JUMPI vf63(0xf6b), vf62

    Begin block 0xf67
    prev=[0xf55], succ=[]
    =================================
    0xf67: vf67(0x0) = CONST 
    0xf6a: REVERT vf67(0x0), vf67(0x0)

    Begin block 0xf6b
    prev=[0xf55], succ=[0x3d6eB0xf6b]
    =================================
    0xf6d: vf6d = MLOAD vf5c
    0xf70: vf70(0xf7f) = CONST 
    0xf75: vf75(0xffffffff) = CONST 
    0xf7a: vf7a(0x3d6e) = CONST 
    0xf7d: vf7d(0x3d6e) = AND vf7a(0x3d6e), vf75(0xffffffff)
    0xf7e: JUMP vf7d(0x3d6e)

    Begin block 0x3d6eB0xf6b
    prev=[0xf6b], succ=[0x3d7aB0xf6b, 0x3d79B0xf6b]
    =================================
    0x3d6fS0xf6b: v3d6fVf6b(0x0) = CONST 
    0x3d73S0xf6b: v3d73Vf6b = GT vf6d, v31d
    0x3d74S0xf6b: v3d74Vf6b = ISZERO v3d73Vf6b
    0x3d75S0xf6b: v3d75Vf6b(0x3d7a) = CONST 
    0x3d78S0xf6b: JUMPI v3d75Vf6b(0x3d7a), v3d74Vf6b

    Begin block 0x3d7aB0xf6b
    prev=[0x3d6eB0xf6b], succ=[0xf7f]
    =================================
    0x3d7dS0xf6b: v3d7dVf6b = SUB v31d, vf6d
    0x3d7fS0xf6b: JUMP vf70(0xf7f)

    Begin block 0xf7f
    prev=[0x3d7aB0xf6b], succ=[0xf8b]
    =================================
    0xf82: vf82(0xf8b) = CONST 
    0xf85: vf85 = CALLER 
    0xf87: vf87(0x3d80) = CONST 
    0xf8a: CALLPRIVATE vf87(0x3d80), v31d, vf85, vf82(0xf8b)

    Begin block 0xf8b
    prev=[0xf7f], succ=[0xfef, 0xff3]
    =================================
    0xf8c: vf8c(0x40) = CONST 
    0xf8f: vf8f = MLOAD vf8c(0x40)
    0xf90: vf90(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = CONST 
    0xfb2: MSTORE vf8f, vf90(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0xfb3: vfb3 = CALLER 
    0xfb4: vfb4(0x4) = CONST 
    0xfb7: vfb7 = ADD vf8f, vfb4(0x4)
    0xfb8: MSTORE vfb7, vfb3
    0xfb9: vfb9(0x24) = CONST 
    0xfbc: vfbc = ADD vf8f, vfb9(0x24)
    0xfbf: MSTORE vfbc, v3d7dVf6b
    0xfc1: vfc1 = MLOAD vf8c(0x40)
    0xfc2: vfc2(0x1) = CONST 
    0xfc4: vfc4(0xa0) = CONST 
    0xfc6: vfc6(0x2) = CONST 
    0xfc8: vfc8(0x10000000000000000000000000000000000000000) = EXP vfc6(0x2), vfc4(0xa0)
    0xfc9: vfc9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfc8(0x10000000000000000000000000000000000000000), vfc2(0x1)
    0xfcb: vfcb = AND v31a, vfc9(0xffffffffffffffffffffffffffffffffffffffff)
    0xfcd: vfcd(0xa9059cbb) = CONST 
    0xfd3: vfd3(0x44) = CONST 
    0xfd7: vfd7 = ADD vf8f, vfd3(0x44)
    0xfd9: vfd9(0x20) = CONST 
    0xfe0: vfe0(0x0) = SUB vf8f, vfc1
    0xfe1: vfe1(0x44) = ADD vfe0(0x0), vfd3(0x44)
    0xfe3: vfe3(0x0) = CONST 
    0xfe7: vfe7 = EXTCODESIZE vfcb
    0xfe8: vfe8 = ISZERO vfe7
    0xfea: vfea = ISZERO vfe8
    0xfeb: vfeb(0xff3) = CONST 
    0xfee: JUMPI vfeb(0xff3), vfea

    Begin block 0xfef
    prev=[0xf8b], succ=[]
    =================================
    0xfef: vfef(0x0) = CONST 
    0xff2: REVERT vfef(0x0), vfef(0x0)

    Begin block 0xff3
    prev=[0xf8b], succ=[0xffe, 0x1007]
    =================================
    0xff5: vff5 = GAS 
    0xff6: vff6 = CALL vff5, vfcb, vfe3(0x0), vfc1, vfe1(0x44), vfc1, vfd9(0x20)
    0xff7: vff7 = ISZERO vff6
    0xff9: vff9 = ISZERO vff7
    0xffa: vffa(0x1007) = CONST 
    0xffd: JUMPI vffa(0x1007), vff9

    Begin block 0xffe
    prev=[0xff3], succ=[]
    =================================
    0xffe: vffe = RETURNDATASIZE 
    0xfff: vfff(0x0) = CONST 
    0x1002: RETURNDATACOPY vfff(0x0), vfff(0x0), vffe
    0x1003: v1003 = RETURNDATASIZE 
    0x1004: v1004(0x0) = CONST 
    0x1006: REVERT v1004(0x0), v1003

    Begin block 0x1007
    prev=[0xff3], succ=[0x1019, 0x101d]
    =================================
    0x100c: v100c(0x40) = CONST 
    0x100e: v100e = MLOAD v100c(0x40)
    0x100f: v100f = RETURNDATASIZE 
    0x1010: v1010(0x20) = CONST 
    0x1013: v1013 = LT v100f, v1010(0x20)
    0x1014: v1014 = ISZERO v1013
    0x1015: v1015(0x101d) = CONST 
    0x1018: JUMPI v1015(0x101d), v1014

    Begin block 0x1019
    prev=[0x1007], succ=[]
    =================================
    0x1019: v1019(0x0) = CONST 
    0x101c: REVERT v1019(0x0), v1019(0x0)

    Begin block 0x101d
    prev=[0x1007], succ=[0x1026, 0x102a]
    =================================
    0x101f: v101f = MLOAD v100e
    0x1020: v1020 = ISZERO v101f
    0x1021: v1021 = ISZERO v1020
    0x1022: v1022(0x102a) = CONST 
    0x1025: JUMPI v1022(0x102a), v1021

    Begin block 0x1026
    prev=[0x101d], succ=[]
    =================================
    0x1026: v1026(0x0) = CONST 
    0x1029: REVERT v1026(0x0), v1026(0x0)

    Begin block 0x102a
    prev=[0x101d], succ=[0x106f, 0x1073]
    =================================
    0x102c: v102c(0x1) = CONST 
    0x102e: v102e(0xa0) = CONST 
    0x1030: v1030(0x2) = CONST 
    0x1032: v1032(0x10000000000000000000000000000000000000000) = EXP v1030(0x2), v102e(0xa0)
    0x1033: v1033(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1032(0x10000000000000000000000000000000000000000), v102c(0x1)
    0x1034: v1034 = AND v1033(0xffffffffffffffffffffffffffffffffffffffff), v31a
    0x1035: v1035(0x42966c68) = CONST 
    0x103b: v103b(0x40) = CONST 
    0x103d: v103d = MLOAD v103b(0x40)
    0x103f: v103f(0xffffffff) = CONST 
    0x1044: v1044(0x42966c68) = AND v103f(0xffffffff), v1035(0x42966c68)
    0x1045: v1045(0xe0) = CONST 
    0x1047: v1047(0x2) = CONST 
    0x1049: v1049(0x100000000000000000000000000000000000000000000000000000000) = EXP v1047(0x2), v1045(0xe0)
    0x104a: v104a(0x42966c6800000000000000000000000000000000000000000000000000000000) = MUL v1049(0x100000000000000000000000000000000000000000000000000000000), v1044(0x42966c68)
    0x104c: MSTORE v103d, v104a(0x42966c6800000000000000000000000000000000000000000000000000000000)
    0x104d: v104d(0x4) = CONST 
    0x104f: v104f = ADD v104d(0x4), v103d
    0x1053: MSTORE v104f, vf6d
    0x1054: v1054(0x20) = CONST 
    0x1056: v1056 = ADD v1054(0x20), v104f
    0x105a: v105a(0x0) = CONST 
    0x105c: v105c(0x40) = CONST 
    0x105e: v105e = MLOAD v105c(0x40)
    0x1061: v1061(0x24) = SUB v1056, v105e
    0x1063: v1063(0x0) = CONST 
    0x1067: v1067 = EXTCODESIZE v1034
    0x1068: v1068 = ISZERO v1067
    0x106a: v106a = ISZERO v1068
    0x106b: v106b(0x1073) = CONST 
    0x106e: JUMPI v106b(0x1073), v106a

    Begin block 0x106f
    prev=[0x102a], succ=[]
    =================================
    0x106f: v106f(0x0) = CONST 
    0x1072: REVERT v106f(0x0), v106f(0x0)

    Begin block 0x1073
    prev=[0x102a], succ=[0x107e, 0x1087]
    =================================
    0x1075: v1075 = GAS 
    0x1076: v1076 = CALL v1075, v1034, v1063(0x0), v105e, v1061(0x24), v105e, v105a(0x0)
    0x1077: v1077 = ISZERO v1076
    0x1079: v1079 = ISZERO v1077
    0x107a: v107a(0x1087) = CONST 
    0x107d: JUMPI v107a(0x1087), v1079

    Begin block 0x107e
    prev=[0x1073], succ=[]
    =================================
    0x107e: v107e = RETURNDATASIZE 
    0x107f: v107f(0x0) = CONST 
    0x1082: RETURNDATACOPY v107f(0x0), v107f(0x0), v107e
    0x1083: v1083 = RETURNDATASIZE 
    0x1084: v1084(0x0) = CONST 
    0x1086: REVERT v1084(0x0), v1083

    Begin block 0x1087
    prev=[0x1073], succ=[0x1095]
    =================================
    0x108c: v108c(0x1095) = CONST 
    0x108f: v108f = ADDRESS 
    0x1091: v1091(0x3fa0) = CONST 
    0x1094: CALLPRIVATE v1091(0x3fa0), vf6d, v108f, v108c(0x1095)

    Begin block 0x1095
    prev=[0x1087], succ=[0x4b24]
    =================================
    0x1096: v1096(0x40) = CONST 
    0x1099: v1099 = MLOAD v1096(0x40)
    0x109c: MSTORE v1099, v31d
    0x109e: v109e = MLOAD v1096(0x40)
    0x109f: v109f = CALLER 
    0x10a1: v10a1(0x3a91515f120c05831525e72379609e84b30a70ab21104f3222d0e91411aadc52) = CONST 
    0x10c6: v10c6(0x0) = SUB v1099, v109e
    0x10c7: v10c7(0x20) = CONST 
    0x10c9: v10c9(0x20) = ADD v10c7(0x20), v10c6(0x0)
    0x10cb: LOG2 v109e, v10c9(0x20), v10a1(0x3a91515f120c05831525e72379609e84b30a70ab21104f3222d0e91411aadc52), v109f
    0x10d2: JUMP v30c(0x4b24)

    Begin block 0x4b24
    prev=[0x1095], succ=[]
    =================================
    0x4b25: STOP 

    Begin block 0x3d79B0xf6b
    prev=[0x3d6eB0xf6b], succ=[]
    =================================
    0x3d79S0xf6b: THROW 

}

function 0x3204(0x3204arg0x0, 0x3204arg0x1, 0x3204arg0x2, 0x3204arg0x3, 0x3204arg0x4) private {
    Begin block 0x3204
    prev=[], succ=[0x329b, 0x26170x3204]
    =================================
    0x3205: v3205(0x40) = CONST 
    0x3208: v3208 = MLOAD v3205(0x40)
    0x3209: v3209(0x1000000000000000000000000) = CONST 
    0x3217: v3217 = ADDRESS 
    0x3219: v3219 = MUL v3209(0x1000000000000000000000000), v3217
    0x321a: v321a(0x20) = CONST 
    0x321e: v321e = ADD v3208, v321a(0x20)
    0x3222: MSTORE v321e, v3219
    0x3223: v3223(0x6d6574614275726e436172626f6e446f6c6c6172000000000000000000000000) = CONST 
    0x3244: v3244(0x34) = CONST 
    0x3247: v3247 = ADD v3208, v3244(0x34)
    0x3248: MSTORE v3247, v3223(0x6d6574614275726e436172626f6e446f6c6c6172000000000000000000000000)
    0x3249: v3249(0x1) = CONST 
    0x324b: v324b(0xa0) = CONST 
    0x324d: v324d(0x2) = CONST 
    0x324f: v324f(0x10000000000000000000000000000000000000000) = EXP v324d(0x2), v324b(0xa0)
    0x3250: v3250(0xffffffffffffffffffffffffffffffffffffffff) = SUB v324f(0x10000000000000000000000000000000000000000), v3249(0x1)
    0x3252: v3252 = AND v3204arg3, v3250(0xffffffffffffffffffffffffffffffffffffffff)
    0x3255: v3255 = MUL v3209(0x1000000000000000000000000), v3252
    0x3256: v3256(0x48) = CONST 
    0x3259: v3259 = ADD v3208, v3256(0x48)
    0x325a: MSTORE v3259, v3255
    0x325b: v325b(0x5c) = CONST 
    0x325e: v325e = ADD v3208, v325b(0x5c)
    0x3261: MSTORE v325e, v3204arg2
    0x3262: v3262(0x7c) = CONST 
    0x3265: v3265 = ADD v3208, v3262(0x7c)
    0x3268: MSTORE v3265, v3204arg1
    0x3269: v3269(0x9c) = CONST 
    0x326d: v326d = ADD v3208, v3269(0x9c)
    0x3270: MSTORE v326d, v3204arg0
    0x3272: v3272 = MLOAD v3205(0x40)
    0x3275: v3275(0x0) = SUB v3208, v3272
    0x3278: v3278(0x9c) = ADD v3269(0x9c), v3275(0x0)
    0x327a: MSTORE v3272, v3278(0x9c)
    0x327b: v327b(0xbc) = CONST 
    0x327f: v327f = ADD v3208, v327b(0xbc)
    0x3283: MSTORE v3205(0x40), v327f
    0x3285: v3285(0x9c) = MLOAD v3272
    0x3286: v3286(0x0) = CONST 
    0x328e: v328e = ADD v3272, v321a(0x20)
    0x3293: v3293(0x20) = CONST 
    0x3296: v3296(0x0) = LT v3285(0x9c), v3293(0x20)
    0x3297: v3297(0x2617) = CONST 
    0x329a: JUMPI v3297(0x2617), v3296(0x0)

    Begin block 0x329b
    prev=[0x3204], succ=[0x25f80x3204]
    =================================
    0x329c: v329c = MLOAD v328e
    0x329e: MSTORE v327f, v329c
    0x329f: v329f(0x1f) = CONST 
    0x32a1: v32a1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v329f(0x1f)
    0x32a4: v32a4(0x7c) = ADD v3285(0x9c), v32a1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x32a6: v32a6(0x20) = CONST 
    0x32aa: v32aa = ADD v32a6(0x20), v327f
    0x32ac: v32ac = ADD v32a6(0x20), v328e
    0x32ad: v32ad(0x25f8) = CONST 
    0x32b0: JUMP v32ad(0x25f8)

    Begin block 0x25f80x3204
    prev=[0x329b, 0x26010x3204], succ=[0x26010x3204, 0x26170x3204]
    =================================
    0x25f80x3204_0x2: v25f83204_2 = PHI v32a4(0x7c), v3204260a
    0x25f90x3204: v320425f9(0x20) = CONST 
    0x25fc0x3204: v320425fc = LT v25f83204_2, v320425f9(0x20)
    0x25fd0x3204: v320425fd(0x2617) = CONST 
    0x26000x3204: JUMPI v320425fd(0x2617), v320425fc

    Begin block 0x26010x3204
    prev=[0x25f80x3204], succ=[0x25f80x3204]
    =================================
    0x26010x3204_0x0: v26013204_0 = PHI v32ac, v32042612
    0x26010x3204_0x1: v26013204_1 = PHI v32aa, v32042610
    0x26010x3204_0x2: v26013204_2 = PHI v32a4(0x7c), v3204260a
    0x26020x3204: v32042602 = MLOAD v26013204_0
    0x26040x3204: MSTORE v26013204_1, v32042602
    0x26050x3204: v32042605(0x1f) = CONST 
    0x26070x3204: v32042607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v32042605(0x1f)
    0x260a0x3204: v3204260a = ADD v26013204_2, v32042607(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x260c0x3204: v3204260c(0x20) = CONST 
    0x26100x3204: v32042610 = ADD v3204260c(0x20), v26013204_1
    0x26120x3204: v32042612 = ADD v3204260c(0x20), v26013204_0
    0x26130x3204: v32042613(0x25f8) = CONST 
    0x26160x3204: JUMP v32042613(0x25f8)

    Begin block 0x26170x3204
    prev=[0x3204, 0x25f80x3204], succ=[]
    =================================
    0x26170x3204_0x0: v26173204_0 = PHI v328e, v32ac, v32042612
    0x26170x3204_0x1: v26173204_1 = PHI v327f, v32aa, v32042610
    0x26170x3204_0x2: v26173204_2 = PHI v3285(0x9c), v32a4(0x7c), v3204260a
    0x26180x3204: v32042618 = MLOAD v26173204_0
    0x261a0x3204: v3204261a = MLOAD v26173204_1
    0x261b0x3204: v3204261b(0x20) = CONST 
    0x26200x3204: v32042620 = SUB v3204261b(0x20), v26173204_2
    0x26210x3204: v32042621(0x100) = CONST 
    0x26240x3204: v32042624 = EXP v32042621(0x100), v32042620
    0x26250x3204: v32042625(0x0) = CONST 
    0x26270x3204: v32042627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v32042625(0x0)
    0x26280x3204: v32042628 = ADD v32042627(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v32042624
    0x262a0x3204: v3204262a = NOT v32042628
    0x262d0x3204: v3204262d = AND v32042618, v3204262a
    0x262f0x3204: v3204262f = AND v3204261a, v32042628
    0x26330x3204: v32042633 = OR v3204262f, v3204262d
    0x26350x3204: MSTORE v26173204_1, v32042633
    0x26360x3204: v32042636(0x40) = CONST 
    0x26380x3204: v32042638 = MLOAD v32042636(0x40)
    0x263a0x3204: v3204263a = ADD v327f, v3285(0x9c)
    0x263d0x3204: v3204263d = SUB v3204263a, v32042638
    0x26400x3204: v32042640 = SHA3 v32042638, v3204263d
    0x264b0x3204: RETURNPRIVATE v3204arg4, v32042640

}

function totalSupply()() public {
    Begin block 0x324
    prev=[], succ=[0x32c, 0x330]
    =================================
    0x325: v325 = CALLVALUE 
    0x327: v327 = ISZERO v325
    0x328: v328(0x330) = CONST 
    0x32b: JUMPI v328(0x330), v327

    Begin block 0x32c
    prev=[0x324], succ=[]
    =================================
    0x32c: v32c(0x0) = CONST 
    0x32f: REVERT v32c(0x0), v32c(0x0)

    Begin block 0x330
    prev=[0x324], succ=[0x10d3B0x330]
    =================================
    0x332: v332(0x4b45) = CONST 
    0x335: v335(0x10d3) = CONST 
    0x338: JUMP v335(0x10d3)

    Begin block 0x10d3B0x330
    prev=[0x330], succ=[0x112eB0x330, 0x11320x10d3B0x330]
    =================================
    0x10d4S0x330: v10d4V330(0x2) = CONST 
    0x10d6S0x330: v10d6V330 = SLOAD v10d4V330(0x2)
    0x10d7S0x330: v10d7V330(0x40) = CONST 
    0x10daS0x330: v10daV330 = MLOAD v10d7V330(0x40)
    0x10dbS0x330: v10dbV330(0x18160ddd00000000000000000000000000000000000000000000000000000000) = CONST 
    0x10fdS0x330: MSTORE v10daV330, v10dbV330(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x10ffS0x330: v10ffV330 = MLOAD v10d7V330(0x40)
    0x1100S0x330: v1100V330(0x0) = CONST 
    0x1103S0x330: v1103V330(0x1) = CONST 
    0x1105S0x330: v1105V330(0xa0) = CONST 
    0x1107S0x330: v1107V330(0x2) = CONST 
    0x1109S0x330: v1109V330(0x10000000000000000000000000000000000000000) = EXP v1107V330(0x2), v1105V330(0xa0)
    0x110aS0x330: v110aV330(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1109V330(0x10000000000000000000000000000000000000000), v1103V330(0x1)
    0x110bS0x330: v110bV330 = AND v110aV330(0xffffffffffffffffffffffffffffffffffffffff), v10d6V330
    0x110dS0x330: v110dV330(0x18160ddd) = CONST 
    0x1113S0x330: v1113V330(0x4) = CONST 
    0x1117S0x330: v1117V330 = ADD v10daV330, v1113V330(0x4)
    0x1119S0x330: v1119V330(0x20) = CONST 
    0x1120S0x330: v1120V330(0x0) = SUB v10daV330, v10ffV330
    0x1121S0x330: v1121V330(0x4) = ADD v1120V330(0x0), v1113V330(0x4)
    0x1126S0x330: v1126V330 = EXTCODESIZE v110bV330
    0x1127S0x330: v1127V330 = ISZERO v1126V330
    0x1129S0x330: v1129V330 = ISZERO v1127V330
    0x112aS0x330: v112aV330(0x1132) = CONST 
    0x112dS0x330: JUMPI v112aV330(0x1132), v1129V330

    Begin block 0x112eB0x330
    prev=[0x10d3B0x330], succ=[]
    =================================
    0x112eS0x330: v112eV330(0x0) = CONST 
    0x1131S0x330: REVERT v112eV330(0x0), v112eV330(0x0)

    Begin block 0x11320x10d3B0x330
    prev=[0x10d3B0x330], succ=[0x113d0x10d3B0x330, 0x11460x10d3B0x330]
    =================================
    0x11340x10d3S0x330: v10d31134V330 = GAS 
    0x11350x10d3S0x330: v10d31135V330 = CALL v10d31134V330, v110bV330, v1100V330(0x0), v10ffV330, v1121V330(0x4), v10ffV330, v1119V330(0x20)
    0x11360x10d3S0x330: v10d31136V330 = ISZERO v10d31135V330
    0x11380x10d3S0x330: v10d31138V330 = ISZERO v10d31136V330
    0x11390x10d3S0x330: v10d31139V330(0x1146) = CONST 
    0x113c0x10d3S0x330: JUMPI v10d31139V330(0x1146), v10d31138V330

    Begin block 0x113d0x10d3B0x330
    prev=[0x11320x10d3B0x330], succ=[]
    =================================
    0x113d0x10d3S0x330: v10d3113dV330 = RETURNDATASIZE 
    0x113e0x10d3S0x330: v10d3113eV330(0x0) = CONST 
    0x11410x10d3S0x330: RETURNDATACOPY v10d3113eV330(0x0), v10d3113eV330(0x0), v10d3113dV330
    0x11420x10d3S0x330: v10d31142V330 = RETURNDATASIZE 
    0x11430x10d3S0x330: v10d31143V330(0x0) = CONST 
    0x11450x10d3S0x330: REVERT v10d31143V330(0x0), v10d31142V330

    Begin block 0x11460x10d3B0x330
    prev=[0x11320x10d3B0x330], succ=[0x11580x10d3B0x330, 0x115c0x10d3B0x330]
    =================================
    0x114b0x10d3S0x330: v10d3114bV330(0x40) = CONST 
    0x114d0x10d3S0x330: v10d3114dV330 = MLOAD v10d3114bV330(0x40)
    0x114e0x10d3S0x330: v10d3114eV330 = RETURNDATASIZE 
    0x114f0x10d3S0x330: v10d3114fV330(0x20) = CONST 
    0x11520x10d3S0x330: v10d31152V330 = LT v10d3114eV330, v10d3114fV330(0x20)
    0x11530x10d3S0x330: v10d31153V330 = ISZERO v10d31152V330
    0x11540x10d3S0x330: v10d31154V330(0x115c) = CONST 
    0x11570x10d3S0x330: JUMPI v10d31154V330(0x115c), v10d31153V330

    Begin block 0x11580x10d3B0x330
    prev=[0x11460x10d3B0x330], succ=[]
    =================================
    0x11580x10d3S0x330: v10d31158V330(0x0) = CONST 
    0x115b0x10d3S0x330: REVERT v10d31158V330(0x0), v10d31158V330(0x0)

    Begin block 0x115c0x10d3B0x330
    prev=[0x11460x10d3B0x330], succ=[0x4b45]
    =================================
    0x115e0x10d3S0x330: v10d3115eV330 = MLOAD v10d3114dV330
    0x11620x10d3S0x330: JUMP v332(0x4b45)

    Begin block 0x4b45
    prev=[0x115c0x10d3B0x330], succ=[]
    =================================
    0x4b46: v4b46(0x40) = CONST 
    0x4b49: v4b49 = MLOAD v4b46(0x40)
    0x4b4c: MSTORE v4b49, v10d3115eV330
    0x4b4d: v4b4d = MLOAD v4b46(0x40)
    0x4b51: v4b51(0x0) = SUB v4b49, v4b4d
    0x4b52: v4b52(0x20) = CONST 
    0x4b54: v4b54(0x20) = ADD v4b52(0x20), v4b51(0x0)
    0x4b56: RETURN v4b4d, v4b54(0x20)

}

function 0x32b1(0x32b1arg0x0, 0x32b1arg0x1, 0x32b1arg0x2) private {
    Begin block 0x32b1
    prev=[], succ=[0x3320, 0x3324]
    =================================
    0x32b2: v32b2(0x2) = CONST 
    0x32b4: v32b4 = SLOAD v32b2(0x2)
    0x32b5: v32b5(0x40) = CONST 
    0x32b8: v32b8 = MLOAD v32b5(0x40)
    0x32b9: v32b9(0x55b6ed5c00000000000000000000000000000000000000000000000000000000) = CONST 
    0x32db: MSTORE v32b8, v32b9(0x55b6ed5c00000000000000000000000000000000000000000000000000000000)
    0x32dc: v32dc(0x1) = CONST 
    0x32de: v32de(0xa0) = CONST 
    0x32e0: v32e0(0x2) = CONST 
    0x32e2: v32e2(0x10000000000000000000000000000000000000000) = EXP v32e0(0x2), v32de(0xa0)
    0x32e3: v32e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32e2(0x10000000000000000000000000000000000000000), v32dc(0x1)
    0x32e6: v32e6 = AND v32e3(0xffffffffffffffffffffffffffffffffffffffff), v32b1arg1
    0x32e7: v32e7(0x4) = CONST 
    0x32ea: v32ea = ADD v32b8, v32e7(0x4)
    0x32eb: MSTORE v32ea, v32e6
    0x32ee: v32ee = AND v32e3(0xffffffffffffffffffffffffffffffffffffffff), v32b1arg0
    0x32ef: v32ef(0x24) = CONST 
    0x32f2: v32f2 = ADD v32b8, v32ef(0x24)
    0x32f3: MSTORE v32f2, v32ee
    0x32f5: v32f5 = MLOAD v32b5(0x40)
    0x32f6: v32f6(0x0) = CONST 
    0x32fc: v32fc = AND v32b4, v32e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x32fe: v32fe(0x55b6ed5c) = CONST 
    0x3304: v3304(0x44) = CONST 
    0x3308: v3308 = ADD v32b8, v3304(0x44)
    0x330a: v330a(0x20) = CONST 
    0x3312: v3312(0x0) = SUB v32b8, v32f5
    0x3313: v3313(0x44) = ADD v3312(0x0), v3304(0x44)
    0x3318: v3318 = EXTCODESIZE v32fc
    0x3319: v3319 = ISZERO v3318
    0x331b: v331b = ISZERO v3319
    0x331c: v331c(0x3324) = CONST 
    0x331f: JUMPI v331c(0x3324), v331b

    Begin block 0x3320
    prev=[0x32b1], succ=[]
    =================================
    0x3320: v3320(0x0) = CONST 
    0x3323: REVERT v3320(0x0), v3320(0x0)

    Begin block 0x3324
    prev=[0x32b1], succ=[0x332f, 0x3338]
    =================================
    0x3326: v3326 = GAS 
    0x3327: v3327 = CALL v3326, v32fc, v32f6(0x0), v32f5, v3313(0x44), v32f5, v330a(0x20)
    0x3328: v3328 = ISZERO v3327
    0x332a: v332a = ISZERO v3328
    0x332b: v332b(0x3338) = CONST 
    0x332e: JUMPI v332b(0x3338), v332a

    Begin block 0x332f
    prev=[0x3324], succ=[]
    =================================
    0x332f: v332f = RETURNDATASIZE 
    0x3330: v3330(0x0) = CONST 
    0x3333: RETURNDATACOPY v3330(0x0), v3330(0x0), v332f
    0x3334: v3334 = RETURNDATASIZE 
    0x3335: v3335(0x0) = CONST 
    0x3337: REVERT v3335(0x0), v3334

    Begin block 0x3338
    prev=[0x3324], succ=[0x334a, 0x334e]
    =================================
    0x333d: v333d(0x40) = CONST 
    0x333f: v333f = MLOAD v333d(0x40)
    0x3340: v3340 = RETURNDATASIZE 
    0x3341: v3341(0x20) = CONST 
    0x3344: v3344 = LT v3340, v3341(0x20)
    0x3345: v3345 = ISZERO v3344
    0x3346: v3346(0x334e) = CONST 
    0x3349: JUMPI v3346(0x334e), v3345

    Begin block 0x334a
    prev=[0x3338], succ=[]
    =================================
    0x334a: v334a(0x0) = CONST 
    0x334d: REVERT v334a(0x0), v334a(0x0)

    Begin block 0x334e
    prev=[0x3338], succ=[]
    =================================
    0x3350: v3350 = MLOAD v333f
    0x3356: RETURNPRIVATE v32b1arg2, v3350

}

function listToken(address)() public {
    Begin block 0x34b
    prev=[], succ=[0x353, 0x357]
    =================================
    0x34c: v34c = CALLVALUE 
    0x34e: v34e = ISZERO v34c
    0x34f: v34f(0x357) = CONST 
    0x352: JUMPI v34f(0x357), v34e

    Begin block 0x353
    prev=[0x34b], succ=[]
    =================================
    0x353: v353(0x0) = CONST 
    0x356: REVERT v353(0x0), v353(0x0)

    Begin block 0x357
    prev=[0x34b], succ=[0x1163B0x357]
    =================================
    0x359: v359(0x4b76) = CONST 
    0x35c: v35c(0x1) = CONST 
    0x35e: v35e(0xa0) = CONST 
    0x360: v360(0x2) = CONST 
    0x362: v362(0x10000000000000000000000000000000000000000) = EXP v360(0x2), v35e(0xa0)
    0x363: v363(0xffffffffffffffffffffffffffffffffffffffff) = SUB v362(0x10000000000000000000000000000000000000000), v35c(0x1)
    0x364: v364(0x4) = CONST 
    0x366: v366 = CALLDATALOAD v364(0x4)
    0x367: v367 = AND v366, v363(0xffffffffffffffffffffffffffffffffffffffff)
    0x368: v368(0x1163) = CONST 
    0x36b: JUMP v368(0x1163), v367, v359(0x4b76)

    Begin block 0x1163B0x357
    prev=[0x357], succ=[0x1176B0x357, 0x117aB0x357]
    =================================
    0x1164S0x357: v1164V357(0x0) = CONST 
    0x1166S0x357: v1166V357 = SLOAD v1164V357(0x0)
    0x1167S0x357: v1167V357(0x1) = CONST 
    0x1169S0x357: v1169V357(0xa0) = CONST 
    0x116bS0x357: v116bV357(0x2) = CONST 
    0x116dS0x357: v116dV357(0x10000000000000000000000000000000000000000) = EXP v116bV357(0x2), v1169V357(0xa0)
    0x116eS0x357: v116eV357(0xffffffffffffffffffffffffffffffffffffffff) = SUB v116dV357(0x10000000000000000000000000000000000000000), v1167V357(0x1)
    0x116fS0x357: v116fV357 = AND v116eV357(0xffffffffffffffffffffffffffffffffffffffff), v1166V357
    0x1170S0x357: v1170V357 = CALLER 
    0x1171S0x357: v1171V357 = EQ v1170V357, v116fV357
    0x1172S0x357: v1172V357(0x117a) = CONST 
    0x1175S0x357: JUMPI v1172V357(0x117a), v1171V357

    Begin block 0x1176B0x357
    prev=[0x1163B0x357], succ=[]
    =================================
    0x1176S0x357: v1176V357(0x0) = CONST 
    0x1179S0x357: REVERT v1176V357(0x0), v1176V357(0x0)

    Begin block 0x117aB0x357
    prev=[0x1163B0x357], succ=[0x118dB0x357, 0x1191B0x357]
    =================================
    0x117bS0x357: v117bV357(0x1) = CONST 
    0x117dS0x357: v117dV357 = SLOAD v117bV357(0x1)
    0x117eS0x357: v117eV357(0xa0) = CONST 
    0x1180S0x357: v1180V357(0x2) = CONST 
    0x1182S0x357: v1182V357(0x10000000000000000000000000000000000000000) = EXP v1180V357(0x2), v117eV357(0xa0)
    0x1184S0x357: v1184V357 = DIV v117dV357, v1182V357(0x10000000000000000000000000000000000000000)
    0x1185S0x357: v1185V357(0xff) = CONST 
    0x1187S0x357: v1187V357 = AND v1185V357(0xff), v1184V357
    0x1188S0x357: v1188V357 = ISZERO v1187V357
    0x1189S0x357: v1189V357(0x1191) = CONST 
    0x118cS0x357: JUMPI v1189V357(0x1191), v1188V357

    Begin block 0x118dB0x357
    prev=[0x117aB0x357], succ=[]
    =================================
    0x118dS0x357: v118dV357(0x0) = CONST 
    0x1190S0x357: REVERT v118dV357(0x0), v118dV357(0x0)

    Begin block 0x1191B0x357
    prev=[0x117aB0x357], succ=[0x11f8B0x357, 0x11fc0x1163B0x357]
    =================================
    0x1192S0x357: v1192V357(0x4) = CONST 
    0x1195S0x357: v1195V357 = SLOAD v1192V357(0x4)
    0x1196S0x357: v1196V357(0x40) = CONST 
    0x1199S0x357: v1199V357 = MLOAD v1196V357(0x40)
    0x119aS0x357: v119aV357(0x418945a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x11bcS0x357: MSTORE v1199V357, v119aV357(0x418945a00000000000000000000000000000000000000000000000000000000)
    0x11bdS0x357: v11bdV357(0x1) = CONST 
    0x11bfS0x357: v11bfV357(0xa0) = CONST 
    0x11c1S0x357: v11c1V357(0x2) = CONST 
    0x11c3S0x357: v11c3V357(0x10000000000000000000000000000000000000000) = EXP v11c1V357(0x2), v11bfV357(0xa0)
    0x11c4S0x357: v11c4V357(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11c3V357(0x10000000000000000000000000000000000000000), v11bdV357(0x1)
    0x11c7S0x357: v11c7V357 = AND v11c4V357(0xffffffffffffffffffffffffffffffffffffffff), v367
    0x11caS0x357: v11caV357 = ADD v1199V357, v1192V357(0x4)
    0x11ceS0x357: MSTORE v11caV357, v11c7V357
    0x11d0S0x357: v11d0V357 = MLOAD v1196V357(0x40)
    0x11d4S0x357: v11d4V357 = AND v1195V357, v11c4V357(0xffffffffffffffffffffffffffffffffffffffff)
    0x11d6S0x357: v11d6V357(0x418945a) = CONST 
    0x11dcS0x357: v11dcV357(0x24) = CONST 
    0x11e0S0x357: v11e0V357 = ADD v1199V357, v11dcV357(0x24)
    0x11e2S0x357: v11e2V357(0x0) = CONST 
    0x11eaS0x357: v11eaV357(0x0) = SUB v1199V357, v11d0V357
    0x11ebS0x357: v11ebV357(0x24) = ADD v11eaV357(0x0), v11dcV357(0x24)
    0x11f0S0x357: v11f0V357 = EXTCODESIZE v11d4V357
    0x11f1S0x357: v11f1V357 = ISZERO v11f0V357
    0x11f3S0x357: v11f3V357 = ISZERO v11f1V357
    0x11f4S0x357: v11f4V357(0x11fc) = CONST 
    0x11f7S0x357: JUMPI v11f4V357(0x11fc), v11f3V357

    Begin block 0x11f8B0x357
    prev=[0x1191B0x357], succ=[]
    =================================
    0x11f8S0x357: v11f8V357(0x0) = CONST 
    0x11fbS0x357: REVERT v11f8V357(0x0), v11f8V357(0x0)

    Begin block 0x11fc0x1163B0x357
    prev=[0x1191B0x357], succ=[0x12070x1163B0x357, 0x12100x1163B0x357]
    =================================
    0x11fe0x1163S0x357: v116311feV357 = GAS 
    0x11ff0x1163S0x357: v116311ffV357 = CALL v116311feV357, v11d4V357, v11e2V357(0x0), v11d0V357, v11ebV357(0x24), v11d0V357, v11e2V357(0x0)
    0x12000x1163S0x357: v11631200V357 = ISZERO v116311ffV357
    0x12020x1163S0x357: v11631202V357 = ISZERO v11631200V357
    0x12030x1163S0x357: v11631203V357(0x1210) = CONST 
    0x12060x1163S0x357: JUMPI v11631203V357(0x1210), v11631202V357

    Begin block 0x12070x1163B0x357
    prev=[0x11fc0x1163B0x357], succ=[]
    =================================
    0x12070x1163S0x357: v11631207V357 = RETURNDATASIZE 
    0x12080x1163S0x357: v11631208V357(0x0) = CONST 
    0x120b0x1163S0x357: RETURNDATACOPY v11631208V357(0x0), v11631208V357(0x0), v11631207V357
    0x120c0x1163S0x357: v1163120cV357 = RETURNDATASIZE 
    0x120d0x1163S0x357: v1163120dV357(0x0) = CONST 
    0x120f0x1163S0x357: REVERT v1163120dV357(0x0), v1163120cV357

    Begin block 0x12100x1163B0x357
    prev=[0x11fc0x1163B0x357], succ=[0x4b76]
    =================================
    0x12160x1163S0x357: JUMP v359(0x4b76)

    Begin block 0x4b76
    prev=[0x12100x1163B0x357], succ=[]
    =================================
    0x4b77: STOP 

}

function getDefaultFee()() public {
    Begin block 0x36c
    prev=[], succ=[0x374, 0x378]
    =================================
    0x36d: v36d = CALLVALUE 
    0x36f: v36f = ISZERO v36d
    0x370: v370(0x378) = CONST 
    0x373: JUMPI v370(0x378), v36f

    Begin block 0x374
    prev=[0x36c], succ=[]
    =================================
    0x374: v374(0x0) = CONST 
    0x377: REVERT v374(0x0), v374(0x0)

    Begin block 0x378
    prev=[0x36c], succ=[0x4b97]
    =================================
    0x37a: v37a(0x4b97) = CONST 
    0x37d: v37d(0x1217) = CONST 
    0x380: v380_0 = CALLPRIVATE v37d(0x1217), v37a(0x4b97)

    Begin block 0x4b97
    prev=[0x378], succ=[]
    =================================
    0x4b98: v4b98(0x40) = CONST 
    0x4b9b: v4b9b = MLOAD v4b98(0x40)
    0x4b9e: MSTORE v4b9b, v380_0
    0x4b9f: v4b9f = MLOAD v4b98(0x40)
    0x4ba3: v4ba3(0x0) = SUB v4b9b, v4b9f
    0x4ba4: v4ba4(0x20) = CONST 
    0x4ba6: v4ba6(0x20) = ADD v4ba4(0x20), v4ba3(0x0)
    0x4ba8: RETURN v4b9f, v4ba6(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x381
    prev=[], succ=[0x389, 0x38d]
    =================================
    0x382: v382 = CALLVALUE 
    0x384: v384 = ISZERO v382
    0x385: v385(0x38d) = CONST 
    0x388: JUMPI v385(0x38d), v384

    Begin block 0x389
    prev=[0x381], succ=[]
    =================================
    0x389: v389(0x0) = CONST 
    0x38c: REVERT v389(0x0), v389(0x0)

    Begin block 0x38d
    prev=[0x381], succ=[0x126c]
    =================================
    0x38f: v38f(0x4bc8) = CONST 
    0x392: v392(0x1) = CONST 
    0x394: v394(0xa0) = CONST 
    0x396: v396(0x2) = CONST 
    0x398: v398(0x10000000000000000000000000000000000000000) = EXP v396(0x2), v394(0xa0)
    0x399: v399(0xffffffffffffffffffffffffffffffffffffffff) = SUB v398(0x10000000000000000000000000000000000000000), v392(0x1)
    0x39a: v39a(0x4) = CONST 
    0x39c: v39c = CALLDATALOAD v39a(0x4)
    0x39e: v39e = AND v399(0xffffffffffffffffffffffffffffffffffffffff), v39c
    0x3a0: v3a0(0x24) = CONST 
    0x3a2: v3a2 = CALLDATALOAD v3a0(0x24)
    0x3a3: v3a3 = AND v3a2, v399(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a4: v3a4(0x44) = CONST 
    0x3a6: v3a6 = CALLDATALOAD v3a4(0x44)
    0x3a7: v3a7(0x126c) = CONST 
    0x3aa: JUMP v3a7(0x126c)

    Begin block 0x126c
    prev=[0x38d], succ=[0x1282, 0x1286]
    =================================
    0x126d: v126d(0x1) = CONST 
    0x126f: v126f = SLOAD v126d(0x1)
    0x1270: v1270(0x0) = CONST 
    0x1273: v1273(0xa0) = CONST 
    0x1275: v1275(0x2) = CONST 
    0x1277: v1277(0x10000000000000000000000000000000000000000) = EXP v1275(0x2), v1273(0xa0)
    0x1279: v1279 = DIV v126f, v1277(0x10000000000000000000000000000000000000000)
    0x127a: v127a(0xff) = CONST 
    0x127c: v127c = AND v127a(0xff), v1279
    0x127d: v127d = ISZERO v127c
    0x127e: v127e(0x1286) = CONST 
    0x1281: JUMPI v127e(0x1286), v127d

    Begin block 0x1282
    prev=[0x126c], succ=[]
    =================================
    0x1282: v1282(0x0) = CONST 
    0x1285: REVERT v1282(0x0), v1282(0x0)

    Begin block 0x1286
    prev=[0x126c], succ=[0x12dc, 0x12e0]
    =================================
    0x1287: v1287(0x3) = CONST 
    0x1289: v1289 = SLOAD v1287(0x3)
    0x128a: v128a(0x40) = CONST 
    0x128d: v128d = MLOAD v128a(0x40)
    0x128e: v128e(0xe0) = CONST 
    0x1290: v1290(0x2) = CONST 
    0x1292: v1292(0x100000000000000000000000000000000000000000000000000000000) = EXP v1290(0x2), v128e(0xe0)
    0x1293: v1293(0x7ccce851) = CONST 
    0x1298: v1298(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1293(0x7ccce851), v1292(0x100000000000000000000000000000000000000000000000000000000)
    0x129a: MSTORE v128d, v1298(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x129b: v129b(0x1) = CONST 
    0x129d: v129d(0xa0) = CONST 
    0x129f: v129f(0x2) = CONST 
    0x12a1: v12a1(0x10000000000000000000000000000000000000000) = EXP v129f(0x2), v129d(0xa0)
    0x12a2: v12a2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12a1(0x10000000000000000000000000000000000000000), v129b(0x1)
    0x12a5: v12a5 = AND v3a3, v12a2(0xffffffffffffffffffffffffffffffffffffffff)
    0x12a6: v12a6(0x4) = CONST 
    0x12a9: v12a9 = ADD v128d, v12a6(0x4)
    0x12aa: MSTORE v12a9, v12a5
    0x12ac: v12ac = MLOAD v128a(0x40)
    0x12b1: v12b1(0x0) = CONST 
    0x12b9: v12b9 = AND v1289, v12a2(0xffffffffffffffffffffffffffffffffffffffff)
    0x12bb: v12bb(0x7ccce851) = CONST 
    0x12c1: v12c1(0x24) = CONST 
    0x12c5: v12c5 = ADD v128d, v12c1(0x24)
    0x12c7: v12c7(0x20) = CONST 
    0x12ce: v12ce(0x0) = SUB v128d, v12ac
    0x12cf: v12cf(0x24) = ADD v12ce(0x0), v12c1(0x24)
    0x12d4: v12d4 = EXTCODESIZE v12b9
    0x12d5: v12d5 = ISZERO v12d4
    0x12d7: v12d7 = ISZERO v12d5
    0x12d8: v12d8(0x12e0) = CONST 
    0x12db: JUMPI v12d8(0x12e0), v12d7

    Begin block 0x12dc
    prev=[0x1286], succ=[]
    =================================
    0x12dc: v12dc(0x0) = CONST 
    0x12df: REVERT v12dc(0x0), v12dc(0x0)

    Begin block 0x12e0
    prev=[0x1286], succ=[0x12eb, 0x12f4]
    =================================
    0x12e2: v12e2 = GAS 
    0x12e3: v12e3 = CALL v12e2, v12b9, v12b1(0x0), v12ac, v12cf(0x24), v12ac, v12c7(0x20)
    0x12e4: v12e4 = ISZERO v12e3
    0x12e6: v12e6 = ISZERO v12e4
    0x12e7: v12e7(0x12f4) = CONST 
    0x12ea: JUMPI v12e7(0x12f4), v12e6

    Begin block 0x12eb
    prev=[0x12e0], succ=[]
    =================================
    0x12eb: v12eb = RETURNDATASIZE 
    0x12ec: v12ec(0x0) = CONST 
    0x12ef: RETURNDATACOPY v12ec(0x0), v12ec(0x0), v12eb
    0x12f0: v12f0 = RETURNDATASIZE 
    0x12f1: v12f1(0x0) = CONST 
    0x12f3: REVERT v12f1(0x0), v12f0

    Begin block 0x12f4
    prev=[0x12e0], succ=[0x1306, 0x130a]
    =================================
    0x12f9: v12f9(0x40) = CONST 
    0x12fb: v12fb = MLOAD v12f9(0x40)
    0x12fc: v12fc = RETURNDATASIZE 
    0x12fd: v12fd(0x20) = CONST 
    0x1300: v1300 = LT v12fc, v12fd(0x20)
    0x1301: v1301 = ISZERO v1300
    0x1302: v1302(0x130a) = CONST 
    0x1305: JUMPI v1302(0x130a), v1301

    Begin block 0x1306
    prev=[0x12f4], succ=[]
    =================================
    0x1306: v1306(0x0) = CONST 
    0x1309: REVERT v1306(0x0), v1306(0x0)

    Begin block 0x130a
    prev=[0x12f4], succ=[0x1312, 0x1361]
    =================================
    0x130c: v130c = MLOAD v12fb
    0x130d: v130d = ISZERO v130c
    0x130e: v130e(0x1361) = CONST 
    0x1311: JUMPI v130e(0x1361), v130d

    Begin block 0x1312
    prev=[0x130a], succ=[]
    =================================
    0x1312: v1312(0x40) = CONST 
    0x1315: v1315 = MLOAD v1312(0x40)
    0x1316: v1316(0xe5) = CONST 
    0x1318: v1318(0x2) = CONST 
    0x131a: v131a(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1318(0x2), v1316(0xe5)
    0x131b: v131b(0x461bcd) = CONST 
    0x131f: v131f(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v131b(0x461bcd), v131a(0x2000000000000000000000000000000000000000000000000000000000)
    0x1321: MSTORE v1315, v131f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1322: v1322(0x20) = CONST 
    0x1324: v1324(0x4) = CONST 
    0x1327: v1327 = ADD v1315, v1324(0x4)
    0x1328: MSTORE v1327, v1322(0x20)
    0x1329: v1329(0x1f) = CONST 
    0x132b: v132b(0x24) = CONST 
    0x132e: v132e = ADD v1315, v132b(0x24)
    0x132f: MSTORE v132e, v1329(0x1f)
    0x1330: v1330(0x526563697069656e742063616e6e6f7420626520626c61636b6c697374656400) = CONST 
    0x1351: v1351(0x44) = CONST 
    0x1354: v1354 = ADD v1315, v1351(0x44)
    0x1355: MSTORE v1354, v1330(0x526563697069656e742063616e6e6f7420626520626c61636b6c697374656400)
    0x1357: v1357 = MLOAD v1312(0x40)
    0x135b: v135b(0x0) = SUB v1315, v1357
    0x135c: v135c(0x64) = CONST 
    0x135e: v135e(0x64) = ADD v135c(0x64), v135b(0x0)
    0x1360: REVERT v1357, v135e(0x64)

    Begin block 0x1361
    prev=[0x130a], succ=[0x13af, 0x13b3]
    =================================
    0x1362: v1362(0x3) = CONST 
    0x1364: v1364 = SLOAD v1362(0x3)
    0x1365: v1365(0x40) = CONST 
    0x1368: v1368 = MLOAD v1365(0x40)
    0x1369: v1369(0xe0) = CONST 
    0x136b: v136b(0x2) = CONST 
    0x136d: v136d(0x100000000000000000000000000000000000000000000000000000000) = EXP v136b(0x2), v1369(0xe0)
    0x136e: v136e(0x7ccce851) = CONST 
    0x1373: v1373(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v136e(0x7ccce851), v136d(0x100000000000000000000000000000000000000000000000000000000)
    0x1375: MSTORE v1368, v1373(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1376: v1376(0x1) = CONST 
    0x1378: v1378(0xa0) = CONST 
    0x137a: v137a(0x2) = CONST 
    0x137c: v137c(0x10000000000000000000000000000000000000000) = EXP v137a(0x2), v1378(0xa0)
    0x137d: v137d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v137c(0x10000000000000000000000000000000000000000), v1376(0x1)
    0x1380: v1380 = AND v137d(0xffffffffffffffffffffffffffffffffffffffff), v39e
    0x1381: v1381(0x4) = CONST 
    0x1384: v1384 = ADD v1368, v1381(0x4)
    0x1385: MSTORE v1384, v1380
    0x1387: v1387 = MLOAD v1365(0x40)
    0x138b: v138b = AND v1364, v137d(0xffffffffffffffffffffffffffffffffffffffff)
    0x138d: v138d(0x7ccce851) = CONST 
    0x1393: v1393(0x24) = CONST 
    0x1397: v1397 = ADD v1368, v1393(0x24)
    0x1399: v1399(0x20) = CONST 
    0x13a0: v13a0(0x0) = SUB v1368, v1387
    0x13a1: v13a1(0x24) = ADD v13a0(0x0), v1393(0x24)
    0x13a3: v13a3(0x0) = CONST 
    0x13a7: v13a7 = EXTCODESIZE v138b
    0x13a8: v13a8 = ISZERO v13a7
    0x13aa: v13aa = ISZERO v13a8
    0x13ab: v13ab(0x13b3) = CONST 
    0x13ae: JUMPI v13ab(0x13b3), v13aa

    Begin block 0x13af
    prev=[0x1361], succ=[]
    =================================
    0x13af: v13af(0x0) = CONST 
    0x13b2: REVERT v13af(0x0), v13af(0x0)

    Begin block 0x13b3
    prev=[0x1361], succ=[0x13be, 0x13c7]
    =================================
    0x13b5: v13b5 = GAS 
    0x13b6: v13b6 = CALL v13b5, v138b, v13a3(0x0), v1387, v13a1(0x24), v1387, v1399(0x20)
    0x13b7: v13b7 = ISZERO v13b6
    0x13b9: v13b9 = ISZERO v13b7
    0x13ba: v13ba(0x13c7) = CONST 
    0x13bd: JUMPI v13ba(0x13c7), v13b9

    Begin block 0x13be
    prev=[0x13b3], succ=[]
    =================================
    0x13be: v13be = RETURNDATASIZE 
    0x13bf: v13bf(0x0) = CONST 
    0x13c2: RETURNDATACOPY v13bf(0x0), v13bf(0x0), v13be
    0x13c3: v13c3 = RETURNDATASIZE 
    0x13c4: v13c4(0x0) = CONST 
    0x13c6: REVERT v13c4(0x0), v13c3

    Begin block 0x13c7
    prev=[0x13b3], succ=[0x13d9, 0x13dd]
    =================================
    0x13cc: v13cc(0x40) = CONST 
    0x13ce: v13ce = MLOAD v13cc(0x40)
    0x13cf: v13cf = RETURNDATASIZE 
    0x13d0: v13d0(0x20) = CONST 
    0x13d3: v13d3 = LT v13cf, v13d0(0x20)
    0x13d4: v13d4 = ISZERO v13d3
    0x13d5: v13d5(0x13dd) = CONST 
    0x13d8: JUMPI v13d5(0x13dd), v13d4

    Begin block 0x13d9
    prev=[0x13c7], succ=[]
    =================================
    0x13d9: v13d9(0x0) = CONST 
    0x13dc: REVERT v13d9(0x0), v13d9(0x0)

    Begin block 0x13dd
    prev=[0x13c7], succ=[0x1444, 0x1448]
    =================================
    0x13df: v13df = MLOAD v13ce
    0x13e0: v13e0(0x3) = CONST 
    0x13e2: v13e2 = SLOAD v13e0(0x3)
    0x13e3: v13e3(0x40) = CONST 
    0x13e6: v13e6 = MLOAD v13e3(0x40)
    0x13e7: v13e7(0x91c4529f00000000000000000000000000000000000000000000000000000000) = CONST 
    0x1409: MSTORE v13e6, v13e7(0x91c4529f00000000000000000000000000000000000000000000000000000000)
    0x140a: v140a = CALLER 
    0x140b: v140b(0x4) = CONST 
    0x140e: v140e = ADD v13e6, v140b(0x4)
    0x140f: MSTORE v140e, v140a
    0x1411: v1411 = MLOAD v13e3(0x40)
    0x1415: v1415(0x1) = CONST 
    0x1417: v1417(0xa0) = CONST 
    0x1419: v1419(0x2) = CONST 
    0x141b: v141b(0x10000000000000000000000000000000000000000) = EXP v1419(0x2), v1417(0xa0)
    0x141c: v141c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v141b(0x10000000000000000000000000000000000000000), v1415(0x1)
    0x141f: v141f = AND v13e2, v141c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1421: v1421(0x91c4529f) = CONST 
    0x1427: v1427(0x24) = CONST 
    0x142b: v142b = ADD v13e6, v1427(0x24)
    0x142d: v142d(0x20) = CONST 
    0x1435: v1435(0x0) = SUB v13e6, v1411
    0x1436: v1436(0x24) = ADD v1435(0x0), v1427(0x24)
    0x1438: v1438(0x0) = CONST 
    0x143c: v143c = EXTCODESIZE v141f
    0x143d: v143d = ISZERO v143c
    0x143f: v143f = ISZERO v143d
    0x1440: v1440(0x1448) = CONST 
    0x1443: JUMPI v1440(0x1448), v143f

    Begin block 0x1444
    prev=[0x13dd], succ=[]
    =================================
    0x1444: v1444(0x0) = CONST 
    0x1447: REVERT v1444(0x0), v1444(0x0)

    Begin block 0x1448
    prev=[0x13dd], succ=[0x1453, 0x145c]
    =================================
    0x144a: v144a = GAS 
    0x144b: v144b = CALL v144a, v141f, v1438(0x0), v1411, v1436(0x24), v1411, v142d(0x20)
    0x144c: v144c = ISZERO v144b
    0x144e: v144e = ISZERO v144c
    0x144f: v144f(0x145c) = CONST 
    0x1452: JUMPI v144f(0x145c), v144e

    Begin block 0x1453
    prev=[0x1448], succ=[]
    =================================
    0x1453: v1453 = RETURNDATASIZE 
    0x1454: v1454(0x0) = CONST 
    0x1457: RETURNDATACOPY v1454(0x0), v1454(0x0), v1453
    0x1458: v1458 = RETURNDATASIZE 
    0x1459: v1459(0x0) = CONST 
    0x145b: REVERT v1459(0x0), v1458

    Begin block 0x145c
    prev=[0x1448], succ=[0x146e, 0x1472]
    =================================
    0x1461: v1461(0x40) = CONST 
    0x1463: v1463 = MLOAD v1461(0x40)
    0x1464: v1464 = RETURNDATASIZE 
    0x1465: v1465(0x20) = CONST 
    0x1468: v1468 = LT v1464, v1465(0x20)
    0x1469: v1469 = ISZERO v1468
    0x146a: v146a(0x1472) = CONST 
    0x146d: JUMPI v146a(0x1472), v1469

    Begin block 0x146e
    prev=[0x145c], succ=[]
    =================================
    0x146e: v146e(0x0) = CONST 
    0x1471: REVERT v146e(0x0), v146e(0x0)

    Begin block 0x1472
    prev=[0x145c], succ=[0x1480, 0x147e]
    =================================
    0x1474: v1474 = MLOAD v1463
    0x1478: v1478 = ISZERO v13df
    0x147a: v147a(0x1480) = CONST 
    0x147d: JUMPI v147a(0x1480), v1478

    Begin block 0x1480
    prev=[0x1472, 0x147e], succ=[0x1487, 0x1522]
    =================================
    0x1480_0x0: v1480_0 = PHI v1474, v1478
    0x1481: v1481 = ISZERO v1480_0
    0x1482: v1482 = ISZERO v1481
    0x1483: v1483(0x1522) = CONST 
    0x1486: JUMPI v1483(0x1522), v1482

    Begin block 0x1487
    prev=[0x1480], succ=[]
    =================================
    0x1487: v1487(0x40) = CONST 
    0x148a: v148a = MLOAD v1487(0x40)
    0x148b: v148b(0xe5) = CONST 
    0x148d: v148d(0x2) = CONST 
    0x148f: v148f(0x2000000000000000000000000000000000000000000000000000000000) = EXP v148d(0x2), v148b(0xe5)
    0x1490: v1490(0x461bcd) = CONST 
    0x1494: v1494(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1490(0x461bcd), v148f(0x2000000000000000000000000000000000000000000000000000000000)
    0x1496: MSTORE v148a, v1494(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1497: v1497(0x20) = CONST 
    0x1499: v1499(0x4) = CONST 
    0x149c: v149c = ADD v148a, v1499(0x4)
    0x149d: MSTORE v149c, v1497(0x20)
    0x149e: v149e(0x4c) = CONST 
    0x14a0: v14a0(0x24) = CONST 
    0x14a3: v14a3 = ADD v148a, v14a0(0x24)
    0x14a4: MSTORE v14a3, v149e(0x4c)
    0x14a5: v14a5(0x4f726967696e2063616e6e6f7420626520626c61636b6c697374656420696620) = CONST 
    0x14c6: v14c6(0x44) = CONST 
    0x14c9: v14c9 = ADD v148a, v14c6(0x44)
    0x14ca: MSTORE v14c9, v14a5(0x4f726967696e2063616e6e6f7420626520626c61636b6c697374656420696620)
    0x14cb: v14cb(0x7370656e646572206973206e6f7420616e20617070726f76656420626c61636b) = CONST 
    0x14ec: v14ec(0x64) = CONST 
    0x14ef: v14ef = ADD v148a, v14ec(0x64)
    0x14f0: MSTORE v14ef, v14cb(0x7370656e646572206973206e6f7420616e20617070726f76656420626c61636b)
    0x14f1: v14f1(0x6c697374207370656e6465720000000000000000000000000000000000000000) = CONST 
    0x1512: v1512(0x84) = CONST 
    0x1515: v1515 = ADD v148a, v1512(0x84)
    0x1516: MSTORE v1515, v14f1(0x6c697374207370656e6465720000000000000000000000000000000000000000)
    0x1518: v1518 = MLOAD v1487(0x40)
    0x151c: v151c(0x0) = SUB v148a, v1518
    0x151d: v151d(0xa4) = CONST 
    0x151f: v151f(0xa4) = ADD v151d(0xa4), v151c(0x0)
    0x1521: REVERT v1518, v151f(0xa4)

    Begin block 0x1522
    prev=[0x1480], succ=[0x152c]
    =================================
    0x1523: v1523(0x152c) = CONST 
    0x1527: v1527 = CALLER 
    0x1528: v1528(0x32b1) = CONST 
    0x152b: v152b_0 = CALLPRIVATE v1528(0x32b1), v1527, v39e, v1523(0x152c)

    Begin block 0x152c
    prev=[0x1522], succ=[0x1534, 0x1583]
    =================================
    0x152e: v152e = GT v3a6, v152b_0
    0x152f: v152f = ISZERO v152e
    0x1530: v1530(0x1583) = CONST 
    0x1533: JUMPI v1530(0x1583), v152f

    Begin block 0x1534
    prev=[0x152c], succ=[]
    =================================
    0x1534: v1534(0x40) = CONST 
    0x1537: v1537 = MLOAD v1534(0x40)
    0x1538: v1538(0xe5) = CONST 
    0x153a: v153a(0x2) = CONST 
    0x153c: v153c(0x2000000000000000000000000000000000000000000000000000000000) = EXP v153a(0x2), v1538(0xe5)
    0x153d: v153d(0x461bcd) = CONST 
    0x1541: v1541(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v153d(0x461bcd), v153c(0x2000000000000000000000000000000000000000000000000000000000)
    0x1543: MSTORE v1537, v1541(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1544: v1544(0x20) = CONST 
    0x1546: v1546(0x4) = CONST 
    0x1549: v1549 = ADD v1537, v1546(0x4)
    0x154c: MSTORE v1549, v1544(0x20)
    0x154d: v154d(0x24) = CONST 
    0x1550: v1550 = ADD v1537, v154d(0x24)
    0x1551: MSTORE v1550, v1544(0x20)
    0x1552: v1552(0x6e6f7420656e6f75676820616c6c6f77616e636520746f207472616e73666572) = CONST 
    0x1573: v1573(0x44) = CONST 
    0x1576: v1576 = ADD v1537, v1573(0x44)
    0x1577: MSTORE v1576, v1552(0x6e6f7420656e6f75676820616c6c6f77616e636520746f207472616e73666572)
    0x1579: v1579 = MLOAD v1534(0x40)
    0x157d: v157d(0x0) = SUB v1537, v1579
    0x157e: v157e(0x64) = CONST 
    0x1580: v1580(0x64) = ADD v157e(0x64), v157d(0x0)
    0x1582: REVERT v1579, v1580(0x64)

    Begin block 0x1583
    prev=[0x152c], succ=[0x158e]
    =================================
    0x1584: v1584(0x158e) = CONST 
    0x158a: v158a(0x4176) = CONST 
    0x158d: CALLPRIVATE v158a(0x4176), v3a6, v39e, v3a3, v1584(0x158e)

    Begin block 0x158e
    prev=[0x1583], succ=[0x15fe, 0x1602]
    =================================
    0x158f: v158f(0x2) = CONST 
    0x1591: v1591 = SLOAD v158f(0x2)
    0x1592: v1592(0x40) = CONST 
    0x1595: v1595 = MLOAD v1592(0x40)
    0x1596: v1596(0x97d88cd200000000000000000000000000000000000000000000000000000000) = CONST 
    0x15b8: MSTORE v1595, v1596(0x97d88cd200000000000000000000000000000000000000000000000000000000)
    0x15b9: v15b9(0x1) = CONST 
    0x15bb: v15bb(0xa0) = CONST 
    0x15bd: v15bd(0x2) = CONST 
    0x15bf: v15bf(0x10000000000000000000000000000000000000000) = EXP v15bd(0x2), v15bb(0xa0)
    0x15c0: v15c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15bf(0x10000000000000000000000000000000000000000), v15b9(0x1)
    0x15c3: v15c3 = AND v15c0(0xffffffffffffffffffffffffffffffffffffffff), v39e
    0x15c4: v15c4(0x4) = CONST 
    0x15c7: v15c7 = ADD v1595, v15c4(0x4)
    0x15c8: MSTORE v15c7, v15c3
    0x15c9: v15c9 = CALLER 
    0x15ca: v15ca(0x24) = CONST 
    0x15cd: v15cd = ADD v1595, v15ca(0x24)
    0x15ce: MSTORE v15cd, v15c9
    0x15cf: v15cf(0x44) = CONST 
    0x15d2: v15d2 = ADD v1595, v15cf(0x44)
    0x15d5: MSTORE v15d2, v3a6
    0x15d7: v15d7 = MLOAD v1592(0x40)
    0x15db: v15db = AND v1591, v15c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x15dd: v15dd(0x97d88cd2) = CONST 
    0x15e3: v15e3(0x64) = CONST 
    0x15e7: v15e7 = ADD v1595, v15e3(0x64)
    0x15e9: v15e9(0x0) = CONST 
    0x15f0: v15f0(0x0) = SUB v1595, v15d7
    0x15f1: v15f1(0x64) = ADD v15f0(0x0), v15e3(0x64)
    0x15f6: v15f6 = EXTCODESIZE v15db
    0x15f7: v15f7 = ISZERO v15f6
    0x15f9: v15f9 = ISZERO v15f7
    0x15fa: v15fa(0x1602) = CONST 
    0x15fd: JUMPI v15fa(0x1602), v15f9

    Begin block 0x15fe
    prev=[0x158e], succ=[]
    =================================
    0x15fe: v15fe(0x0) = CONST 
    0x1601: REVERT v15fe(0x0), v15fe(0x0)

    Begin block 0x1602
    prev=[0x158e], succ=[0x160d, 0x1616]
    =================================
    0x1604: v1604 = GAS 
    0x1605: v1605 = CALL v1604, v15db, v15e9(0x0), v15d7, v15f1(0x64), v15d7, v15e9(0x0)
    0x1606: v1606 = ISZERO v1605
    0x1608: v1608 = ISZERO v1606
    0x1609: v1609(0x1616) = CONST 
    0x160c: JUMPI v1609(0x1616), v1608

    Begin block 0x160d
    prev=[0x1602], succ=[]
    =================================
    0x160d: v160d = RETURNDATASIZE 
    0x160e: v160e(0x0) = CONST 
    0x1611: RETURNDATACOPY v160e(0x0), v160e(0x0), v160d
    0x1612: v1612 = RETURNDATASIZE 
    0x1613: v1613(0x0) = CONST 
    0x1615: REVERT v1613(0x0), v1612

    Begin block 0x1616
    prev=[0x1602], succ=[0x4bc8]
    =================================
    0x1618: v1618(0x1) = CONST 
    0x1627: JUMP v38f(0x4bc8)

    Begin block 0x4bc8
    prev=[0x1616], succ=[]
    =================================
    0x4bc9: v4bc9(0x40) = CONST 
    0x4bcc: v4bcc = MLOAD v4bc9(0x40)
    0x4bce: v4bce = ISZERO v1618(0x1)
    0x4bcf: v4bcf = ISZERO v4bce
    0x4bd1: MSTORE v4bcc, v4bcf
    0x4bd2: v4bd2 = MLOAD v4bc9(0x40)
    0x4bd6: v4bd6(0x0) = SUB v4bcc, v4bd2
    0x4bd7: v4bd7(0x20) = CONST 
    0x4bd9: v4bd9(0x20) = ADD v4bd7(0x20), v4bd6(0x0)
    0x4bdb: RETURN v4bd2, v4bd9(0x20)

    Begin block 0x147e
    prev=[0x1472], succ=[0x1480]
    =================================

}

function decimals()() public {
    Begin block 0x3ab
    prev=[], succ=[0x3b3, 0x3b7]
    =================================
    0x3ac: v3ac = CALLVALUE 
    0x3ae: v3ae = ISZERO v3ac
    0x3af: v3af(0x3b7) = CONST 
    0x3b2: JUMPI v3af(0x3b7), v3ae

    Begin block 0x3b3
    prev=[0x3ab], succ=[]
    =================================
    0x3b3: v3b3(0x0) = CONST 
    0x3b6: REVERT v3b3(0x0), v3b3(0x0)

    Begin block 0x3b7
    prev=[0x3ab], succ=[0x1628]
    =================================
    0x3b9: v3b9(0x3c0) = CONST 
    0x3bc: v3bc(0x1628) = CONST 
    0x3bf: JUMP v3bc(0x1628)

    Begin block 0x1628
    prev=[0x3b7], succ=[0x3c0]
    =================================
    0x1629: v1629(0x12) = CONST 
    0x162c: JUMP v3b9(0x3c0)

    Begin block 0x3c0
    prev=[0x1628], succ=[]
    =================================
    0x3c1: v3c1(0x40) = CONST 
    0x3c4: v3c4 = MLOAD v3c1(0x40)
    0x3c5: v3c5(0xff) = CONST 
    0x3c9: v3c9(0x12) = AND v1629(0x12), v3c5(0xff)
    0x3cb: MSTORE v3c4, v3c9(0x12)
    0x3cc: v3cc = MLOAD v3c1(0x40)
    0x3d0: v3d0(0x0) = SUB v3c4, v3cc
    0x3d1: v3d1(0x20) = CONST 
    0x3d3: v3d3(0x20) = ADD v3d1(0x20), v3d0(0x0)
    0x3d5: RETURN v3cc, v3d3(0x20)

}

function isWhitelisted(address)() public {
    Begin block 0x3d6
    prev=[], succ=[0x3de, 0x3e2]
    =================================
    0x3d7: v3d7 = CALLVALUE 
    0x3d9: v3d9 = ISZERO v3d7
    0x3da: v3da(0x3e2) = CONST 
    0x3dd: JUMPI v3da(0x3e2), v3d9

    Begin block 0x3de
    prev=[0x3d6], succ=[]
    =================================
    0x3de: v3de(0x0) = CONST 
    0x3e1: REVERT v3de(0x0), v3de(0x0)

    Begin block 0x3e2
    prev=[0x3d6], succ=[0x4bfb]
    =================================
    0x3e4: v3e4(0x4bfb) = CONST 
    0x3e7: v3e7(0x1) = CONST 
    0x3e9: v3e9(0xa0) = CONST 
    0x3eb: v3eb(0x2) = CONST 
    0x3ed: v3ed(0x10000000000000000000000000000000000000000) = EXP v3eb(0x2), v3e9(0xa0)
    0x3ee: v3ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ed(0x10000000000000000000000000000000000000000), v3e7(0x1)
    0x3ef: v3ef(0x4) = CONST 
    0x3f1: v3f1 = CALLDATALOAD v3ef(0x4)
    0x3f2: v3f2 = AND v3f1, v3ee(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f3: v3f3(0x162d) = CONST 
    0x3f6: v3f6_0 = CALLPRIVATE v3f3(0x162d), v3f2, v3e4(0x4bfb)

    Begin block 0x4bfb
    prev=[0x3e2], succ=[]
    =================================
    0x4bfc: v4bfc(0x40) = CONST 
    0x4bff: v4bff = MLOAD v4bfc(0x40)
    0x4c01: v4c01 = ISZERO v3f6_0
    0x4c02: v4c02 = ISZERO v4c01
    0x4c04: MSTORE v4bff, v4c02
    0x4c05: v4c05 = MLOAD v4bfc(0x40)
    0x4c09: v4c09(0x0) = SUB v4bff, v4c05
    0x4c0a: v4c0a(0x20) = CONST 
    0x4c0c: v4c0c(0x20) = ADD v4c0a(0x20), v4c09(0x0)
    0x4c0e: RETURN v4c05, v4c0c(0x20)

}

function 0x3d80(0x3d80arg0x0, 0x3d80arg0x1, 0x3d80arg0x2) private {
    Begin block 0x3d80
    prev=[], succ=[0x3d91, 0x3de0]
    =================================
    0x3d81: v3d81(0x1) = CONST 
    0x3d83: v3d83(0xa0) = CONST 
    0x3d85: v3d85(0x2) = CONST 
    0x3d87: v3d87(0x10000000000000000000000000000000000000000) = EXP v3d85(0x2), v3d83(0xa0)
    0x3d88: v3d88(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d87(0x10000000000000000000000000000000000000000), v3d81(0x1)
    0x3d8a: v3d8a = AND v3d80arg1, v3d88(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d8b: v3d8b = ISZERO v3d8a
    0x3d8c: v3d8c = ISZERO v3d8b
    0x3d8d: v3d8d(0x3de0) = CONST 
    0x3d90: JUMPI v3d8d(0x3de0), v3d8c

    Begin block 0x3d91
    prev=[0x3d80], succ=[]
    =================================
    0x3d91: v3d91(0x40) = CONST 
    0x3d94: v3d94 = MLOAD v3d91(0x40)
    0x3d95: v3d95(0xe5) = CONST 
    0x3d97: v3d97(0x2) = CONST 
    0x3d99: v3d99(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3d97(0x2), v3d95(0xe5)
    0x3d9a: v3d9a(0x461bcd) = CONST 
    0x3d9e: v3d9e(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3d9a(0x461bcd), v3d99(0x2000000000000000000000000000000000000000000000000000000000)
    0x3da0: MSTORE v3d94, v3d9e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3da1: v3da1(0x20) = CONST 
    0x3da3: v3da3(0x4) = CONST 
    0x3da6: v3da6 = ADD v3d94, v3da3(0x4)
    0x3da7: MSTORE v3da6, v3da1(0x20)
    0x3da8: v3da8(0x1c) = CONST 
    0x3daa: v3daa(0x24) = CONST 
    0x3dad: v3dad = ADD v3d94, v3daa(0x24)
    0x3dae: MSTORE v3dad, v3da8(0x1c)
    0x3daf: v3daf(0x6275726e657220616464726573732063616e6e6f742062652030783000000000) = CONST 
    0x3dd0: v3dd0(0x44) = CONST 
    0x3dd3: v3dd3 = ADD v3d94, v3dd0(0x44)
    0x3dd4: MSTORE v3dd3, v3daf(0x6275726e657220616464726573732063616e6e6f742062652030783000000000)
    0x3dd6: v3dd6 = MLOAD v3d91(0x40)
    0x3dda: v3dda(0x0) = SUB v3d94, v3dd6
    0x3ddb: v3ddb(0x64) = CONST 
    0x3ddd: v3ddd(0x64) = ADD v3ddb(0x64), v3dda(0x0)
    0x3ddf: REVERT v3dd6, v3ddd(0x64)

    Begin block 0x3de0
    prev=[0x3d80], succ=[0x3de9]
    =================================
    0x3de1: v3de1(0x3de9) = CONST 
    0x3de5: v3de5(0x206a) = CONST 
    0x3de8: v3de8_0 = CALLPRIVATE v3de5(0x206a), v3d80arg1, v3de1(0x3de9)

    Begin block 0x3de9
    prev=[0x3de0], succ=[0x3df1, 0x3e40]
    =================================
    0x3deb: v3deb = GT v3d80arg0, v3de8_0
    0x3dec: v3dec = ISZERO v3deb
    0x3ded: v3ded(0x3e40) = CONST 
    0x3df0: JUMPI v3ded(0x3e40), v3dec

    Begin block 0x3df1
    prev=[0x3de9], succ=[]
    =================================
    0x3df1: v3df1(0x40) = CONST 
    0x3df4: v3df4 = MLOAD v3df1(0x40)
    0x3df5: v3df5(0xe5) = CONST 
    0x3df7: v3df7(0x2) = CONST 
    0x3df9: v3df9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3df7(0x2), v3df5(0xe5)
    0x3dfa: v3dfa(0x461bcd) = CONST 
    0x3dfe: v3dfe(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3dfa(0x461bcd), v3df9(0x2000000000000000000000000000000000000000000000000000000000)
    0x3e00: MSTORE v3df4, v3dfe(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3e01: v3e01(0x20) = CONST 
    0x3e03: v3e03(0x4) = CONST 
    0x3e06: v3e06 = ADD v3df4, v3e03(0x4)
    0x3e07: MSTORE v3e06, v3e01(0x20)
    0x3e08: v3e08(0x1a) = CONST 
    0x3e0a: v3e0a(0x24) = CONST 
    0x3e0d: v3e0d = ADD v3df4, v3e0a(0x24)
    0x3e0e: MSTORE v3e0d, v3e08(0x1a)
    0x3e0f: v3e0f(0x6e6f7420656e6f7567682062616c616e636520746f206275726e000000000000) = CONST 
    0x3e30: v3e30(0x44) = CONST 
    0x3e33: v3e33 = ADD v3df4, v3e30(0x44)
    0x3e34: MSTORE v3e33, v3e0f(0x6e6f7420656e6f7567682062616c616e636520746f206275726e000000000000)
    0x3e36: v3e36 = MLOAD v3df1(0x40)
    0x3e3a: v3e3a(0x0) = SUB v3df4, v3e36
    0x3e3b: v3e3b(0x64) = CONST 
    0x3e3d: v3e3d(0x64) = ADD v3e3b(0x64), v3e3a(0x0)
    0x3e3f: REVERT v3e36, v3e3d(0x64)

    Begin block 0x3e40
    prev=[0x3de9], succ=[0x3e94, 0x3e98]
    =================================
    0x3e41: v3e41(0x2) = CONST 
    0x3e43: v3e43 = SLOAD v3e41(0x2)
    0x3e44: v3e44(0x40) = CONST 
    0x3e47: v3e47 = MLOAD v3e44(0x40)
    0x3e48: v3e48(0xe1) = CONST 
    0x3e4a: v3e4a(0x2) = CONST 
    0x3e4c: v3e4c(0x200000000000000000000000000000000000000000000000000000000) = EXP v3e4a(0x2), v3e48(0xe1)
    0x3e4d: v3e4d(0x67c775bf) = CONST 
    0x3e52: v3e52(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = MUL v3e4d(0x67c775bf), v3e4c(0x200000000000000000000000000000000000000000000000000000000)
    0x3e54: MSTORE v3e47, v3e52(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x3e55: v3e55(0x1) = CONST 
    0x3e57: v3e57(0xa0) = CONST 
    0x3e59: v3e59(0x2) = CONST 
    0x3e5b: v3e5b(0x10000000000000000000000000000000000000000) = EXP v3e59(0x2), v3e57(0xa0)
    0x3e5c: v3e5c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3e5b(0x10000000000000000000000000000000000000000), v3e55(0x1)
    0x3e5f: v3e5f = AND v3e5c(0xffffffffffffffffffffffffffffffffffffffff), v3d80arg1
    0x3e60: v3e60(0x4) = CONST 
    0x3e63: v3e63 = ADD v3e47, v3e60(0x4)
    0x3e64: MSTORE v3e63, v3e5f
    0x3e65: v3e65(0x24) = CONST 
    0x3e68: v3e68 = ADD v3e47, v3e65(0x24)
    0x3e6b: MSTORE v3e68, v3d80arg0
    0x3e6d: v3e6d = MLOAD v3e44(0x40)
    0x3e71: v3e71 = AND v3e43, v3e5c(0xffffffffffffffffffffffffffffffffffffffff)
    0x3e73: v3e73(0xcf8eeb7e) = CONST 
    0x3e79: v3e79(0x44) = CONST 
    0x3e7d: v3e7d = ADD v3e47, v3e79(0x44)
    0x3e7f: v3e7f(0x0) = CONST 
    0x3e86: v3e86(0x0) = SUB v3e47, v3e6d
    0x3e87: v3e87(0x44) = ADD v3e86(0x0), v3e79(0x44)
    0x3e8c: v3e8c = EXTCODESIZE v3e71
    0x3e8d: v3e8d = ISZERO v3e8c
    0x3e8f: v3e8f = ISZERO v3e8d
    0x3e90: v3e90(0x3e98) = CONST 
    0x3e93: JUMPI v3e90(0x3e98), v3e8f

    Begin block 0x3e94
    prev=[0x3e40], succ=[]
    =================================
    0x3e94: v3e94(0x0) = CONST 
    0x3e97: REVERT v3e94(0x0), v3e94(0x0)

    Begin block 0x3e98
    prev=[0x3e40], succ=[0x3ea3, 0x3eac]
    =================================
    0x3e9a: v3e9a = GAS 
    0x3e9b: v3e9b = CALL v3e9a, v3e71, v3e7f(0x0), v3e6d, v3e87(0x44), v3e6d, v3e7f(0x0)
    0x3e9c: v3e9c = ISZERO v3e9b
    0x3e9e: v3e9e = ISZERO v3e9c
    0x3e9f: v3e9f(0x3eac) = CONST 
    0x3ea2: JUMPI v3e9f(0x3eac), v3e9e

    Begin block 0x3ea3
    prev=[0x3e98], succ=[]
    =================================
    0x3ea3: v3ea3 = RETURNDATASIZE 
    0x3ea4: v3ea4(0x0) = CONST 
    0x3ea7: RETURNDATACOPY v3ea4(0x0), v3ea4(0x0), v3ea3
    0x3ea8: v3ea8 = RETURNDATASIZE 
    0x3ea9: v3ea9(0x0) = CONST 
    0x3eab: REVERT v3ea9(0x0), v3ea8

    Begin block 0x3eac
    prev=[0x3e98], succ=[0x3f12, 0x3f16]
    =================================
    0x3eaf: v3eaf(0x2) = CONST 
    0x3eb1: v3eb1 = SLOAD v3eaf(0x2)
    0x3eb2: v3eb2(0x40) = CONST 
    0x3eb5: v3eb5 = MLOAD v3eb2(0x40)
    0x3eb6: v3eb6(0x82838c7600000000000000000000000000000000000000000000000000000000) = CONST 
    0x3ed8: MSTORE v3eb5, v3eb6(0x82838c7600000000000000000000000000000000000000000000000000000000)
    0x3ed9: v3ed9(0x4) = CONST 
    0x3edc: v3edc = ADD v3eb5, v3ed9(0x4)
    0x3edf: MSTORE v3edc, v3d80arg0
    0x3ee1: v3ee1 = MLOAD v3eb2(0x40)
    0x3ee2: v3ee2(0x1) = CONST 
    0x3ee4: v3ee4(0xa0) = CONST 
    0x3ee6: v3ee6(0x2) = CONST 
    0x3ee8: v3ee8(0x10000000000000000000000000000000000000000) = EXP v3ee6(0x2), v3ee4(0xa0)
    0x3ee9: v3ee9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ee8(0x10000000000000000000000000000000000000000), v3ee2(0x1)
    0x3eec: v3eec = AND v3eb1, v3ee9(0xffffffffffffffffffffffffffffffffffffffff)
    0x3eef: v3eef(0x82838c76) = CONST 
    0x3ef6: v3ef6(0x24) = CONST 
    0x3efa: v3efa = ADD v3eb5, v3ef6(0x24)
    0x3efc: v3efc(0x0) = CONST 
    0x3f04: v3f04(0x0) = SUB v3eb5, v3ee1
    0x3f05: v3f05(0x24) = ADD v3f04(0x0), v3ef6(0x24)
    0x3f0a: v3f0a = EXTCODESIZE v3eec
    0x3f0b: v3f0b = ISZERO v3f0a
    0x3f0d: v3f0d = ISZERO v3f0b
    0x3f0e: v3f0e(0x3f16) = CONST 
    0x3f11: JUMPI v3f0e(0x3f16), v3f0d

    Begin block 0x3f12
    prev=[0x3eac], succ=[]
    =================================
    0x3f12: v3f12(0x0) = CONST 
    0x3f15: REVERT v3f12(0x0), v3f12(0x0)

    Begin block 0x3f16
    prev=[0x3eac], succ=[0x3f21, 0x3f2a]
    =================================
    0x3f18: v3f18 = GAS 
    0x3f19: v3f19 = CALL v3f18, v3eec, v3efc(0x0), v3ee1, v3f05(0x24), v3ee1, v3efc(0x0)
    0x3f1a: v3f1a = ISZERO v3f19
    0x3f1c: v3f1c = ISZERO v3f1a
    0x3f1d: v3f1d(0x3f2a) = CONST 
    0x3f20: JUMPI v3f1d(0x3f2a), v3f1c

    Begin block 0x3f21
    prev=[0x3f16], succ=[]
    =================================
    0x3f21: v3f21 = RETURNDATASIZE 
    0x3f22: v3f22(0x0) = CONST 
    0x3f25: RETURNDATACOPY v3f22(0x0), v3f22(0x0), v3f21
    0x3f26: v3f26 = RETURNDATASIZE 
    0x3f27: v3f27(0x0) = CONST 
    0x3f29: REVERT v3f27(0x0), v3f26

    Begin block 0x3f2a
    prev=[0x3f16], succ=[]
    =================================
    0x3f2d: v3f2d(0x40) = CONST 
    0x3f30: v3f30 = MLOAD v3f2d(0x40)
    0x3f33: MSTORE v3f30, v3d80arg0
    0x3f35: v3f35 = MLOAD v3f2d(0x40)
    0x3f36: v3f36(0x1) = CONST 
    0x3f38: v3f38(0xa0) = CONST 
    0x3f3a: v3f3a(0x2) = CONST 
    0x3f3c: v3f3c(0x10000000000000000000000000000000000000000) = EXP v3f3a(0x2), v3f38(0xa0)
    0x3f3d: v3f3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f3c(0x10000000000000000000000000000000000000000), v3f36(0x1)
    0x3f3f: v3f3f = AND v3d80arg1, v3f3d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f42: v3f42(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0x3f68: v3f68(0x0) = SUB v3f30, v3f35
    0x3f69: v3f69(0x20) = CONST 
    0x3f6b: v3f6b(0x20) = ADD v3f69(0x20), v3f68(0x0)
    0x3f6d: LOG2 v3f35, v3f6b(0x20), v3f42(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), v3f3f
    0x3f6e: v3f6e(0x40) = CONST 
    0x3f71: v3f71 = MLOAD v3f6e(0x40)
    0x3f74: MSTORE v3f71, v3d80arg0
    0x3f76: v3f76 = MLOAD v3f6e(0x40)
    0x3f77: v3f77(0x0) = CONST 
    0x3f7a: v3f7a(0x1) = CONST 
    0x3f7c: v3f7c(0xa0) = CONST 
    0x3f7e: v3f7e(0x2) = CONST 
    0x3f80: v3f80(0x10000000000000000000000000000000000000000) = EXP v3f7e(0x2), v3f7c(0xa0)
    0x3f81: v3f81(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f80(0x10000000000000000000000000000000000000000), v3f7a(0x1)
    0x3f83: v3f83 = AND v3d80arg1, v3f81(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f85: v3f85(0x0) = CONST 
    0x3f88: v3f88 = MLOAD v3f85(0x0)
    0x3f89: v3f89(0x20) = CONST 
    0x3f8b: v3f8b(0x4a90) = CONST 
    0x3f93: MSTORE v3f85(0x0), v3f88
    0x3f97: v3f97(0x0) = SUB v3f71, v3f76
    0x3f98: v3f98(0x20) = CONST 
    0x3f9a: v3f9a(0x20) = ADD v3f98(0x20), v3f97(0x0)
    0x3f9c: LOG3 v3f76, v3f9a(0x20), v5584(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v3f83, v3f77(0x0)
    0x3f9f: RETURNPRIVATE v3d80arg2
    0x5584: v5584(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 

}

function unpause()() public {
    Begin block 0x3f7
    prev=[], succ=[0x3ff, 0x403]
    =================================
    0x3f8: v3f8 = CALLVALUE 
    0x3fa: v3fa = ISZERO v3f8
    0x3fb: v3fb(0x403) = CONST 
    0x3fe: JUMPI v3fb(0x403), v3fa

    Begin block 0x3ff
    prev=[0x3f7], succ=[]
    =================================
    0x3ff: v3ff(0x0) = CONST 
    0x402: REVERT v3ff(0x0), v3ff(0x0)

    Begin block 0x403
    prev=[0x3f7], succ=[0x16ce]
    =================================
    0x405: v405(0x4c2e) = CONST 
    0x408: v408(0x16ce) = CONST 
    0x40b: JUMP v408(0x16ce)

    Begin block 0x16ce
    prev=[0x403], succ=[0x16e1, 0x16e5]
    =================================
    0x16cf: v16cf(0x0) = CONST 
    0x16d1: v16d1 = SLOAD v16cf(0x0)
    0x16d2: v16d2(0x1) = CONST 
    0x16d4: v16d4(0xa0) = CONST 
    0x16d6: v16d6(0x2) = CONST 
    0x16d8: v16d8(0x10000000000000000000000000000000000000000) = EXP v16d6(0x2), v16d4(0xa0)
    0x16d9: v16d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16d8(0x10000000000000000000000000000000000000000), v16d2(0x1)
    0x16da: v16da = AND v16d9(0xffffffffffffffffffffffffffffffffffffffff), v16d1
    0x16db: v16db = CALLER 
    0x16dc: v16dc = EQ v16db, v16da
    0x16dd: v16dd(0x16e5) = CONST 
    0x16e0: JUMPI v16dd(0x16e5), v16dc

    Begin block 0x16e1
    prev=[0x16ce], succ=[]
    =================================
    0x16e1: v16e1(0x0) = CONST 
    0x16e4: REVERT v16e1(0x0), v16e1(0x0)

    Begin block 0x16e5
    prev=[0x16ce], succ=[0x16f9, 0x16fd]
    =================================
    0x16e6: v16e6(0x1) = CONST 
    0x16e8: v16e8 = SLOAD v16e6(0x1)
    0x16e9: v16e9(0xa0) = CONST 
    0x16eb: v16eb(0x2) = CONST 
    0x16ed: v16ed(0x10000000000000000000000000000000000000000) = EXP v16eb(0x2), v16e9(0xa0)
    0x16ef: v16ef = DIV v16e8, v16ed(0x10000000000000000000000000000000000000000)
    0x16f0: v16f0(0xff) = CONST 
    0x16f2: v16f2 = AND v16f0(0xff), v16ef
    0x16f3: v16f3 = ISZERO v16f2
    0x16f4: v16f4 = ISZERO v16f3
    0x16f5: v16f5(0x16fd) = CONST 
    0x16f8: JUMPI v16f5(0x16fd), v16f4

    Begin block 0x16f9
    prev=[0x16e5], succ=[]
    =================================
    0x16f9: v16f9(0x0) = CONST 
    0x16fc: REVERT v16f9(0x0), v16f9(0x0)

    Begin block 0x16fd
    prev=[0x16e5], succ=[0x4c2e]
    =================================
    0x16fe: v16fe(0x1) = CONST 
    0x1701: v1701 = SLOAD v16fe(0x1)
    0x1702: v1702(0xff0000000000000000000000000000000000000000) = CONST 
    0x1718: v1718(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v1702(0xff0000000000000000000000000000000000000000)
    0x1719: v1719 = AND v1718(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1701
    0x171b: SSTORE v16fe(0x1), v1719
    0x171c: v171c(0x40) = CONST 
    0x171e: v171e = MLOAD v171c(0x40)
    0x171f: v171f(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33) = CONST 
    0x1741: v1741(0x0) = CONST 
    0x1744: LOG1 v171e, v1741(0x0), v171f(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33)
    0x1745: JUMP v405(0x4c2e)

    Begin block 0x4c2e
    prev=[0x16fd], succ=[]
    =================================
    0x4c2f: STOP 

}

function 0x3fa0(0x3fa0arg0x0, 0x3fa0arg0x1, 0x3fa0arg0x2) private {
    Begin block 0x3fa0
    prev=[], succ=[0x3fb1, 0x4000]
    =================================
    0x3fa1: v3fa1(0x1) = CONST 
    0x3fa3: v3fa3(0xa0) = CONST 
    0x3fa5: v3fa5(0x2) = CONST 
    0x3fa7: v3fa7(0x10000000000000000000000000000000000000000) = EXP v3fa5(0x2), v3fa3(0xa0)
    0x3fa8: v3fa8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fa7(0x10000000000000000000000000000000000000000), v3fa1(0x1)
    0x3faa: v3faa = AND v3fa0arg1, v3fa8(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fab: v3fab = ISZERO v3faa
    0x3fac: v3fac = ISZERO v3fab
    0x3fad: v3fad(0x4000) = CONST 
    0x3fb0: JUMPI v3fad(0x4000), v3fac

    Begin block 0x3fb1
    prev=[0x3fa0], succ=[]
    =================================
    0x3fb1: v3fb1(0x40) = CONST 
    0x3fb4: v3fb4 = MLOAD v3fb1(0x40)
    0x3fb5: v3fb5(0xe5) = CONST 
    0x3fb7: v3fb7(0x2) = CONST 
    0x3fb9: v3fb9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3fb7(0x2), v3fb5(0xe5)
    0x3fba: v3fba(0x461bcd) = CONST 
    0x3fbe: v3fbe(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3fba(0x461bcd), v3fb9(0x2000000000000000000000000000000000000000000000000000000000)
    0x3fc0: MSTORE v3fb4, v3fbe(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3fc1: v3fc1(0x20) = CONST 
    0x3fc3: v3fc3(0x4) = CONST 
    0x3fc6: v3fc6 = ADD v3fb4, v3fc3(0x4)
    0x3fc7: MSTORE v3fc6, v3fc1(0x20)
    0x3fc8: v3fc8(0x18) = CONST 
    0x3fca: v3fca(0x24) = CONST 
    0x3fcd: v3fcd = ADD v3fb4, v3fca(0x24)
    0x3fce: MSTORE v3fcd, v3fc8(0x18)
    0x3fcf: v3fcf(0x746f20616464726573732063616e6e6f74206265203078300000000000000000) = CONST 
    0x3ff0: v3ff0(0x44) = CONST 
    0x3ff3: v3ff3 = ADD v3fb4, v3ff0(0x44)
    0x3ff4: MSTORE v3ff3, v3fcf(0x746f20616464726573732063616e6e6f74206265203078300000000000000000)
    0x3ff6: v3ff6 = MLOAD v3fb1(0x40)
    0x3ffa: v3ffa(0x0) = SUB v3fb4, v3ff6
    0x3ffb: v3ffb(0x64) = CONST 
    0x3ffd: v3ffd(0x64) = ADD v3ffb(0x64), v3ffa(0x0)
    0x3fff: REVERT v3ff6, v3ffd(0x64)

    Begin block 0x4000
    prev=[0x3fa0], succ=[0x4062, 0x4066]
    =================================
    0x4001: v4001(0x2) = CONST 
    0x4003: v4003 = SLOAD v4001(0x2)
    0x4004: v4004(0x40) = CONST 
    0x4007: v4007 = MLOAD v4004(0x40)
    0x4008: v4008(0xe468688e00000000000000000000000000000000000000000000000000000000) = CONST 
    0x402a: MSTORE v4007, v4008(0xe468688e00000000000000000000000000000000000000000000000000000000)
    0x402b: v402b(0x4) = CONST 
    0x402e: v402e = ADD v4007, v402b(0x4)
    0x4031: MSTORE v402e, v3fa0arg0
    0x4033: v4033 = MLOAD v4004(0x40)
    0x4034: v4034(0x1) = CONST 
    0x4036: v4036(0xa0) = CONST 
    0x4038: v4038(0x2) = CONST 
    0x403a: v403a(0x10000000000000000000000000000000000000000) = EXP v4038(0x2), v4036(0xa0)
    0x403b: v403b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v403a(0x10000000000000000000000000000000000000000), v4034(0x1)
    0x403e: v403e = AND v4003, v403b(0xffffffffffffffffffffffffffffffffffffffff)
    0x4040: v4040(0xe468688e) = CONST 
    0x4046: v4046(0x24) = CONST 
    0x404a: v404a = ADD v4007, v4046(0x24)
    0x404c: v404c(0x0) = CONST 
    0x4054: v4054(0x0) = SUB v4007, v4033
    0x4055: v4055(0x24) = ADD v4054(0x0), v4046(0x24)
    0x405a: v405a = EXTCODESIZE v403e
    0x405b: v405b = ISZERO v405a
    0x405d: v405d = ISZERO v405b
    0x405e: v405e(0x4066) = CONST 
    0x4061: JUMPI v405e(0x4066), v405d

    Begin block 0x4062
    prev=[0x4000], succ=[]
    =================================
    0x4062: v4062(0x0) = CONST 
    0x4065: REVERT v4062(0x0), v4062(0x0)

    Begin block 0x4066
    prev=[0x4000], succ=[0x4071, 0x407a]
    =================================
    0x4068: v4068 = GAS 
    0x4069: v4069 = CALL v4068, v403e, v404c(0x0), v4033, v4055(0x24), v4033, v404c(0x0)
    0x406a: v406a = ISZERO v4069
    0x406c: v406c = ISZERO v406a
    0x406d: v406d(0x407a) = CONST 
    0x4070: JUMPI v406d(0x407a), v406c

    Begin block 0x4071
    prev=[0x4066], succ=[]
    =================================
    0x4071: v4071 = RETURNDATASIZE 
    0x4072: v4072(0x0) = CONST 
    0x4075: RETURNDATACOPY v4072(0x0), v4072(0x0), v4071
    0x4076: v4076 = RETURNDATASIZE 
    0x4077: v4077(0x0) = CONST 
    0x4079: REVERT v4077(0x0), v4076

    Begin block 0x407a
    prev=[0x4066], succ=[0x40e8, 0x40ec]
    =================================
    0x407d: v407d(0x2) = CONST 
    0x407f: v407f = SLOAD v407d(0x2)
    0x4080: v4080(0x40) = CONST 
    0x4083: v4083 = MLOAD v4080(0x40)
    0x4084: v4084(0x21e5383a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x40a6: MSTORE v4083, v4084(0x21e5383a00000000000000000000000000000000000000000000000000000000)
    0x40a7: v40a7(0x1) = CONST 
    0x40a9: v40a9(0xa0) = CONST 
    0x40ab: v40ab(0x2) = CONST 
    0x40ad: v40ad(0x10000000000000000000000000000000000000000) = EXP v40ab(0x2), v40a9(0xa0)
    0x40ae: v40ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v40ad(0x10000000000000000000000000000000000000000), v40a7(0x1)
    0x40b1: v40b1 = AND v40ae(0xffffffffffffffffffffffffffffffffffffffff), v3fa0arg1
    0x40b2: v40b2(0x4) = CONST 
    0x40b5: v40b5 = ADD v4083, v40b2(0x4)
    0x40b6: MSTORE v40b5, v40b1
    0x40b7: v40b7(0x24) = CONST 
    0x40ba: v40ba = ADD v4083, v40b7(0x24)
    0x40bd: MSTORE v40ba, v3fa0arg0
    0x40bf: v40bf = MLOAD v4080(0x40)
    0x40c3: v40c3 = AND v407f, v40ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x40c6: v40c6(0x21e5383a) = CONST 
    0x40cd: v40cd(0x44) = CONST 
    0x40d1: v40d1 = ADD v4083, v40cd(0x44)
    0x40d3: v40d3(0x0) = CONST 
    0x40da: v40da(0x0) = SUB v4083, v40bf
    0x40db: v40db(0x44) = ADD v40da(0x0), v40cd(0x44)
    0x40e0: v40e0 = EXTCODESIZE v40c3
    0x40e1: v40e1 = ISZERO v40e0
    0x40e3: v40e3 = ISZERO v40e1
    0x40e4: v40e4(0x40ec) = CONST 
    0x40e7: JUMPI v40e4(0x40ec), v40e3

    Begin block 0x40e8
    prev=[0x407a], succ=[]
    =================================
    0x40e8: v40e8(0x0) = CONST 
    0x40eb: REVERT v40e8(0x0), v40e8(0x0)

    Begin block 0x40ec
    prev=[0x407a], succ=[0x40f7, 0x4100]
    =================================
    0x40ee: v40ee = GAS 
    0x40ef: v40ef = CALL v40ee, v40c3, v40d3(0x0), v40bf, v40db(0x44), v40bf, v40d3(0x0)
    0x40f0: v40f0 = ISZERO v40ef
    0x40f2: v40f2 = ISZERO v40f0
    0x40f3: v40f3(0x4100) = CONST 
    0x40f6: JUMPI v40f3(0x4100), v40f2

    Begin block 0x40f7
    prev=[0x40ec], succ=[]
    =================================
    0x40f7: v40f7 = RETURNDATASIZE 
    0x40f8: v40f8(0x0) = CONST 
    0x40fb: RETURNDATACOPY v40f8(0x0), v40f8(0x0), v40f7
    0x40fc: v40fc = RETURNDATASIZE 
    0x40fd: v40fd(0x0) = CONST 
    0x40ff: REVERT v40fd(0x0), v40fc

    Begin block 0x4100
    prev=[0x40ec], succ=[]
    =================================
    0x4103: v4103(0x40) = CONST 
    0x4106: v4106 = MLOAD v4103(0x40)
    0x4109: MSTORE v4106, v3fa0arg0
    0x410b: v410b = MLOAD v4103(0x40)
    0x410c: v410c(0x1) = CONST 
    0x410e: v410e(0xa0) = CONST 
    0x4110: v4110(0x2) = CONST 
    0x4112: v4112(0x10000000000000000000000000000000000000000) = EXP v4110(0x2), v410e(0xa0)
    0x4113: v4113(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4112(0x10000000000000000000000000000000000000000), v410c(0x1)
    0x4115: v4115 = AND v3fa0arg1, v4113(0xffffffffffffffffffffffffffffffffffffffff)
    0x4118: v4118(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0x413e: v413e(0x0) = SUB v4106, v410b
    0x413f: v413f(0x20) = CONST 
    0x4141: v4141(0x20) = ADD v413f(0x20), v413e(0x0)
    0x4143: LOG2 v410b, v4141(0x20), v4118(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), v4115
    0x4144: v4144(0x40) = CONST 
    0x4147: v4147 = MLOAD v4144(0x40)
    0x414a: MSTORE v4147, v3fa0arg0
    0x414c: v414c = MLOAD v4144(0x40)
    0x414d: v414d(0x1) = CONST 
    0x414f: v414f(0xa0) = CONST 
    0x4151: v4151(0x2) = CONST 
    0x4153: v4153(0x10000000000000000000000000000000000000000) = EXP v4151(0x2), v414f(0xa0)
    0x4154: v4154(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4153(0x10000000000000000000000000000000000000000), v414d(0x1)
    0x4156: v4156 = AND v3fa0arg1, v4154(0xffffffffffffffffffffffffffffffffffffffff)
    0x4158: v4158(0x0) = CONST 
    0x415b: v415b(0x0) = CONST 
    0x415e: v415e = MLOAD v415b(0x0)
    0x415f: v415f(0x20) = CONST 
    0x4161: v4161(0x4a90) = CONST 
    0x4169: MSTORE v415b(0x0), v415e
    0x416d: v416d(0x0) = SUB v4147, v414c
    0x416e: v416e(0x20) = CONST 
    0x4170: v4170(0x20) = ADD v416e(0x20), v416d(0x0)
    0x4172: LOG3 v414c, v4170(0x20), v5589(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v4158(0x0), v4156
    0x4175: RETURNPRIVATE v3fa0arg2
    0x5589: v5589(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 

}

function mint(address,uint256)() public {
    Begin block 0x40c
    prev=[], succ=[0x414, 0x418]
    =================================
    0x40d: v40d = CALLVALUE 
    0x40f: v40f = ISZERO v40d
    0x410: v410(0x418) = CONST 
    0x413: JUMPI v410(0x418), v40f

    Begin block 0x414
    prev=[0x40c], succ=[]
    =================================
    0x414: v414(0x0) = CONST 
    0x417: REVERT v414(0x0), v414(0x0)

    Begin block 0x418
    prev=[0x40c], succ=[0x1746B0x418]
    =================================
    0x41a: v41a(0x4c4f) = CONST 
    0x41d: v41d(0x1) = CONST 
    0x41f: v41f(0xa0) = CONST 
    0x421: v421(0x2) = CONST 
    0x423: v423(0x10000000000000000000000000000000000000000) = EXP v421(0x2), v41f(0xa0)
    0x424: v424(0xffffffffffffffffffffffffffffffffffffffff) = SUB v423(0x10000000000000000000000000000000000000000), v41d(0x1)
    0x425: v425(0x4) = CONST 
    0x427: v427 = CALLDATALOAD v425(0x4)
    0x428: v428 = AND v427, v424(0xffffffffffffffffffffffffffffffffffffffff)
    0x429: v429(0x24) = CONST 
    0x42b: v42b = CALLDATALOAD v429(0x24)
    0x42c: v42c(0x1746) = CONST 
    0x42f: JUMP v42c(0x1746), v42b, v428, v41a(0x4c4f)

    Begin block 0x1746B0x418
    prev=[0x418], succ=[0x174fB0x418]
    =================================
    0x1747S0x418: v1747V418(0x174f) = CONST 
    0x174aS0x418: v174aV418 = CALLER 
    0x174bS0x418: v174bV418(0x162d) = CONST 
    0x174eS0x418: v174e_0V418 = CALLPRIVATE v174bV418(0x162d), v174aV418, v1747V418(0x174f)

    Begin block 0x174fB0x418
    prev=[0x1746B0x418], succ=[0x1756B0x418, 0x17cbB0x418]
    =================================
    0x1750S0x418: v1750V418 = ISZERO v174e_0V418
    0x1751S0x418: v1751V418 = ISZERO v1750V418
    0x1752S0x418: v1752V418(0x17cb) = CONST 
    0x1755S0x418: JUMPI v1752V418(0x17cb), v1751V418

    Begin block 0x1756B0x418
    prev=[0x174fB0x418], succ=[]
    =================================
    0x1756S0x418: v1756V418(0x40) = CONST 
    0x1759S0x418: v1759V418 = MLOAD v1756V418(0x40)
    0x175aS0x418: v175aV418(0xe5) = CONST 
    0x175cS0x418: v175cV418(0x2) = CONST 
    0x175eS0x418: v175eV418(0x2000000000000000000000000000000000000000000000000000000000) = EXP v175cV418(0x2), v175aV418(0xe5)
    0x175fS0x418: v175fV418(0x461bcd) = CONST 
    0x1763S0x418: v1763V418(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v175fV418(0x461bcd), v175eV418(0x2000000000000000000000000000000000000000000000000000000000)
    0x1765S0x418: MSTORE v1759V418, v1763V418(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1766S0x418: v1766V418(0x20) = CONST 
    0x1768S0x418: v1768V418(0x4) = CONST 
    0x176bS0x418: v176bV418 = ADD v1759V418, v1768V418(0x4)
    0x176cS0x418: MSTORE v176bV418, v1766V418(0x20)
    0x176dS0x418: v176dV418(0x2b) = CONST 
    0x176fS0x418: v176fV418(0x24) = CONST 
    0x1772S0x418: v1772V418 = ADD v1759V418, v176fV418(0x24)
    0x1773S0x418: MSTORE v1772V418, v176dV418(0x2b)
    0x1774S0x418: v1774V418(0x53656e646572206d75737420626520612077686974656c697374656420746f6b) = CONST 
    0x1795S0x418: v1795V418(0x44) = CONST 
    0x1798S0x418: v1798V418 = ADD v1759V418, v1795V418(0x44)
    0x1799S0x418: MSTORE v1798V418, v1774V418(0x53656e646572206d75737420626520612077686974656c697374656420746f6b)
    0x179aS0x418: v179aV418(0x656e20636f6e7472616374000000000000000000000000000000000000000000) = CONST 
    0x17bbS0x418: v17bbV418(0x64) = CONST 
    0x17beS0x418: v17beV418 = ADD v1759V418, v17bbV418(0x64)
    0x17bfS0x418: MSTORE v17beV418, v179aV418(0x656e20636f6e7472616374000000000000000000000000000000000000000000)
    0x17c1S0x418: v17c1V418 = MLOAD v1756V418(0x40)
    0x17c5S0x418: v17c5V418(0x0) = SUB v1759V418, v17c1V418
    0x17c6S0x418: v17c6V418(0x84) = CONST 
    0x17c8S0x418: v17c8V418(0x84) = ADD v17c6V418(0x84), v17c5V418(0x0)
    0x17caS0x418: REVERT v17c1V418, v17c8V418(0x84)

    Begin block 0x17cbB0x418
    prev=[0x174fB0x418], succ=[0x17deB0x418, 0x17e2B0x418]
    =================================
    0x17ccS0x418: v17ccV418(0x1) = CONST 
    0x17ceS0x418: v17ceV418 = SLOAD v17ccV418(0x1)
    0x17cfS0x418: v17cfV418(0xa0) = CONST 
    0x17d1S0x418: v17d1V418(0x2) = CONST 
    0x17d3S0x418: v17d3V418(0x10000000000000000000000000000000000000000) = EXP v17d1V418(0x2), v17cfV418(0xa0)
    0x17d5S0x418: v17d5V418 = DIV v17ceV418, v17d3V418(0x10000000000000000000000000000000000000000)
    0x17d6S0x418: v17d6V418(0xff) = CONST 
    0x17d8S0x418: v17d8V418 = AND v17d6V418(0xff), v17d5V418
    0x17d9S0x418: v17d9V418 = ISZERO v17d8V418
    0x17daS0x418: v17daV418(0x17e2) = CONST 
    0x17ddS0x418: JUMPI v17daV418(0x17e2), v17d9V418

    Begin block 0x17deB0x418
    prev=[0x17cbB0x418], succ=[]
    =================================
    0x17deS0x418: v17deV418(0x0) = CONST 
    0x17e1S0x418: REVERT v17deV418(0x0), v17deV418(0x0)

    Begin block 0x17e2B0x418
    prev=[0x17cbB0x418], succ=[0x52ebB0x418]
    =================================
    0x17e3S0x418: v17e3V418(0x52eb) = CONST 
    0x17e8S0x418: v17e8V418(0x3fa0) = CONST 
    0x17ebS0x418: CALLPRIVATE v17e8V418(0x3fa0), v42b, v428, v17e3V418(0x52eb)

    Begin block 0x52ebB0x418
    prev=[0x17e2B0x418], succ=[0x4c4f]
    =================================
    0x52eeS0x418: JUMP v41a(0x4c4f)

    Begin block 0x4c4f
    prev=[0x52ebB0x418], succ=[]
    =================================
    0x4c50: STOP 

}

function 0x4176(0x4176arg0x0, 0x4176arg0x1, 0x4176arg0x2, 0x4176arg0x3) private {
    Begin block 0x4176
    prev=[], succ=[0x4187, 0x41d6]
    =================================
    0x4177: v4177(0x1) = CONST 
    0x4179: v4179(0xa0) = CONST 
    0x417b: v417b(0x2) = CONST 
    0x417d: v417d(0x10000000000000000000000000000000000000000) = EXP v417b(0x2), v4179(0xa0)
    0x417e: v417e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v417d(0x10000000000000000000000000000000000000000), v4177(0x1)
    0x4180: v4180 = AND v4176arg2, v417e(0xffffffffffffffffffffffffffffffffffffffff)
    0x4181: v4181 = ISZERO v4180
    0x4182: v4182 = ISZERO v4181
    0x4183: v4183(0x41d6) = CONST 
    0x4186: JUMPI v4183(0x41d6), v4182

    Begin block 0x4187
    prev=[0x4176], succ=[]
    =================================
    0x4187: v4187(0x40) = CONST 
    0x418a: v418a = MLOAD v4187(0x40)
    0x418b: v418b(0xe5) = CONST 
    0x418d: v418d(0x2) = CONST 
    0x418f: v418f(0x2000000000000000000000000000000000000000000000000000000000) = EXP v418d(0x2), v418b(0xe5)
    0x4190: v4190(0x461bcd) = CONST 
    0x4194: v4194(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v4190(0x461bcd), v418f(0x2000000000000000000000000000000000000000000000000000000000)
    0x4196: MSTORE v418a, v4194(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4197: v4197(0x20) = CONST 
    0x4199: v4199(0x4) = CONST 
    0x419c: v419c = ADD v418a, v4199(0x4)
    0x419d: MSTORE v419c, v4197(0x20)
    0x419e: v419e(0x18) = CONST 
    0x41a0: v41a0(0x24) = CONST 
    0x41a3: v41a3 = ADD v418a, v41a0(0x24)
    0x41a4: MSTORE v41a3, v419e(0x18)
    0x41a5: v41a5(0x746f20616464726573732063616e6e6f74206265203078300000000000000000) = CONST 
    0x41c6: v41c6(0x44) = CONST 
    0x41c9: v41c9 = ADD v418a, v41c6(0x44)
    0x41ca: MSTORE v41c9, v41a5(0x746f20616464726573732063616e6e6f74206265203078300000000000000000)
    0x41cc: v41cc = MLOAD v4187(0x40)
    0x41d0: v41d0(0x0) = SUB v418a, v41cc
    0x41d1: v41d1(0x64) = CONST 
    0x41d3: v41d3(0x64) = ADD v41d1(0x64), v41d0(0x0)
    0x41d5: REVERT v41cc, v41d3(0x64)

    Begin block 0x41d6
    prev=[0x4176], succ=[0x41df]
    =================================
    0x41d7: v41d7(0x41df) = CONST 
    0x41db: v41db(0x206a) = CONST 
    0x41de: v41de_0 = CALLPRIVATE v41db(0x206a), v4176arg1, v41d7(0x41df)

    Begin block 0x41df
    prev=[0x41d6], succ=[0x41e7, 0x4236]
    =================================
    0x41e1: v41e1 = GT v4176arg0, v41de_0
    0x41e2: v41e2 = ISZERO v41e1
    0x41e3: v41e3(0x4236) = CONST 
    0x41e6: JUMPI v41e3(0x4236), v41e2

    Begin block 0x41e7
    prev=[0x41df], succ=[]
    =================================
    0x41e7: v41e7(0x40) = CONST 
    0x41ea: v41ea = MLOAD v41e7(0x40)
    0x41eb: v41eb(0xe5) = CONST 
    0x41ed: v41ed(0x2) = CONST 
    0x41ef: v41ef(0x2000000000000000000000000000000000000000000000000000000000) = EXP v41ed(0x2), v41eb(0xe5)
    0x41f0: v41f0(0x461bcd) = CONST 
    0x41f4: v41f4(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v41f0(0x461bcd), v41ef(0x2000000000000000000000000000000000000000000000000000000000)
    0x41f6: MSTORE v41ea, v41f4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x41f7: v41f7(0x20) = CONST 
    0x41f9: v41f9(0x4) = CONST 
    0x41fc: v41fc = ADD v41ea, v41f9(0x4)
    0x41fd: MSTORE v41fc, v41f7(0x20)
    0x41fe: v41fe(0x1e) = CONST 
    0x4200: v4200(0x24) = CONST 
    0x4203: v4203 = ADD v41ea, v4200(0x24)
    0x4204: MSTORE v4203, v41fe(0x1e)
    0x4205: v4205(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000) = CONST 
    0x4226: v4226(0x44) = CONST 
    0x4229: v4229 = ADD v41ea, v4226(0x44)
    0x422a: MSTORE v4229, v4205(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000)
    0x422c: v422c = MLOAD v41e7(0x40)
    0x4230: v4230(0x0) = SUB v41ea, v422c
    0x4231: v4231(0x64) = CONST 
    0x4233: v4233(0x64) = ADD v4231(0x64), v4230(0x0)
    0x4235: REVERT v422c, v4233(0x64)

    Begin block 0x4236
    prev=[0x41df], succ=[0x42a0, 0x42a4]
    =================================
    0x4237: v4237(0x2) = CONST 
    0x4239: v4239 = SLOAD v4237(0x2)
    0x423a: v423a(0x40) = CONST 
    0x423d: v423d = MLOAD v423a(0x40)
    0x423e: v423e(0x21e5383a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x4260: MSTORE v423d, v423e(0x21e5383a00000000000000000000000000000000000000000000000000000000)
    0x4261: v4261(0x1) = CONST 
    0x4263: v4263(0xa0) = CONST 
    0x4265: v4265(0x2) = CONST 
    0x4267: v4267(0x10000000000000000000000000000000000000000) = EXP v4265(0x2), v4263(0xa0)
    0x4268: v4268(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4267(0x10000000000000000000000000000000000000000), v4261(0x1)
    0x426b: v426b = AND v4268(0xffffffffffffffffffffffffffffffffffffffff), v4176arg2
    0x426c: v426c(0x4) = CONST 
    0x426f: v426f = ADD v423d, v426c(0x4)
    0x4270: MSTORE v426f, v426b
    0x4271: v4271(0x24) = CONST 
    0x4274: v4274 = ADD v423d, v4271(0x24)
    0x4277: MSTORE v4274, v4176arg0
    0x4279: v4279 = MLOAD v423a(0x40)
    0x427d: v427d = AND v4239, v4268(0xffffffffffffffffffffffffffffffffffffffff)
    0x427f: v427f(0x21e5383a) = CONST 
    0x4285: v4285(0x44) = CONST 
    0x4289: v4289 = ADD v423d, v4285(0x44)
    0x428b: v428b(0x0) = CONST 
    0x4292: v4292(0x0) = SUB v423d, v4279
    0x4293: v4293(0x44) = ADD v4292(0x0), v4285(0x44)
    0x4298: v4298 = EXTCODESIZE v427d
    0x4299: v4299 = ISZERO v4298
    0x429b: v429b = ISZERO v4299
    0x429c: v429c(0x42a4) = CONST 
    0x429f: JUMPI v429c(0x42a4), v429b

    Begin block 0x42a0
    prev=[0x4236], succ=[]
    =================================
    0x42a0: v42a0(0x0) = CONST 
    0x42a3: REVERT v42a0(0x0), v42a0(0x0)

    Begin block 0x42a4
    prev=[0x4236], succ=[0x42af, 0x42b8]
    =================================
    0x42a6: v42a6 = GAS 
    0x42a7: v42a7 = CALL v42a6, v427d, v428b(0x0), v4279, v4293(0x44), v4279, v428b(0x0)
    0x42a8: v42a8 = ISZERO v42a7
    0x42aa: v42aa = ISZERO v42a8
    0x42ab: v42ab(0x42b8) = CONST 
    0x42ae: JUMPI v42ab(0x42b8), v42aa

    Begin block 0x42af
    prev=[0x42a4], succ=[]
    =================================
    0x42af: v42af = RETURNDATASIZE 
    0x42b0: v42b0(0x0) = CONST 
    0x42b3: RETURNDATACOPY v42b0(0x0), v42b0(0x0), v42af
    0x42b4: v42b4 = RETURNDATASIZE 
    0x42b5: v42b5(0x0) = CONST 
    0x42b7: REVERT v42b5(0x0), v42b4

    Begin block 0x42b8
    prev=[0x42a4], succ=[0x4310, 0x4314]
    =================================
    0x42bb: v42bb(0x2) = CONST 
    0x42bd: v42bd = SLOAD v42bb(0x2)
    0x42be: v42be(0x40) = CONST 
    0x42c1: v42c1 = MLOAD v42be(0x40)
    0x42c2: v42c2(0xe1) = CONST 
    0x42c4: v42c4(0x2) = CONST 
    0x42c6: v42c6(0x200000000000000000000000000000000000000000000000000000000) = EXP v42c4(0x2), v42c2(0xe1)
    0x42c7: v42c7(0x67c775bf) = CONST 
    0x42cc: v42cc(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = MUL v42c7(0x67c775bf), v42c6(0x200000000000000000000000000000000000000000000000000000000)
    0x42ce: MSTORE v42c1, v42cc(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x42cf: v42cf(0x1) = CONST 
    0x42d1: v42d1(0xa0) = CONST 
    0x42d3: v42d3(0x2) = CONST 
    0x42d5: v42d5(0x10000000000000000000000000000000000000000) = EXP v42d3(0x2), v42d1(0xa0)
    0x42d6: v42d6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v42d5(0x10000000000000000000000000000000000000000), v42cf(0x1)
    0x42d9: v42d9 = AND v42d6(0xffffffffffffffffffffffffffffffffffffffff), v4176arg1
    0x42da: v42da(0x4) = CONST 
    0x42dd: v42dd = ADD v42c1, v42da(0x4)
    0x42de: MSTORE v42dd, v42d9
    0x42df: v42df(0x24) = CONST 
    0x42e2: v42e2 = ADD v42c1, v42df(0x24)
    0x42e5: MSTORE v42e2, v4176arg0
    0x42e7: v42e7 = MLOAD v42be(0x40)
    0x42eb: v42eb = AND v42bd, v42d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x42ee: v42ee(0xcf8eeb7e) = CONST 
    0x42f5: v42f5(0x44) = CONST 
    0x42f9: v42f9 = ADD v42c1, v42f5(0x44)
    0x42fb: v42fb(0x0) = CONST 
    0x4302: v4302(0x0) = SUB v42c1, v42e7
    0x4303: v4303(0x44) = ADD v4302(0x0), v42f5(0x44)
    0x4308: v4308 = EXTCODESIZE v42eb
    0x4309: v4309 = ISZERO v4308
    0x430b: v430b = ISZERO v4309
    0x430c: v430c(0x4314) = CONST 
    0x430f: JUMPI v430c(0x4314), v430b

    Begin block 0x4310
    prev=[0x42b8], succ=[]
    =================================
    0x4310: v4310(0x0) = CONST 
    0x4313: REVERT v4310(0x0), v4310(0x0)

    Begin block 0x4314
    prev=[0x42b8], succ=[0x431f, 0x4328]
    =================================
    0x4316: v4316 = GAS 
    0x4317: v4317 = CALL v4316, v42eb, v42fb(0x0), v42e7, v4303(0x44), v42e7, v42fb(0x0)
    0x4318: v4318 = ISZERO v4317
    0x431a: v431a = ISZERO v4318
    0x431b: v431b(0x4328) = CONST 
    0x431e: JUMPI v431b(0x4328), v431a

    Begin block 0x431f
    prev=[0x4314], succ=[]
    =================================
    0x431f: v431f = RETURNDATASIZE 
    0x4320: v4320(0x0) = CONST 
    0x4323: RETURNDATACOPY v4320(0x0), v4320(0x0), v431f
    0x4324: v4324 = RETURNDATASIZE 
    0x4325: v4325(0x0) = CONST 
    0x4327: REVERT v4325(0x0), v4324

    Begin block 0x4328
    prev=[0x4314], succ=[]
    =================================
    0x432b: v432b(0x40) = CONST 
    0x432e: v432e = MLOAD v432b(0x40)
    0x4331: MSTORE v432e, v4176arg0
    0x4333: v4333 = MLOAD v432b(0x40)
    0x4334: v4334(0x1) = CONST 
    0x4336: v4336(0xa0) = CONST 
    0x4338: v4338(0x2) = CONST 
    0x433a: v433a(0x10000000000000000000000000000000000000000) = EXP v4338(0x2), v4336(0xa0)
    0x433b: v433b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v433a(0x10000000000000000000000000000000000000000), v4334(0x1)
    0x433e: v433e = AND v4176arg2, v433b(0xffffffffffffffffffffffffffffffffffffffff)
    0x4342: v4342 = AND v4176arg1, v433b(0xffffffffffffffffffffffffffffffffffffffff)
    0x4345: v4345(0x0) = CONST 
    0x4348: v4348 = MLOAD v4345(0x0)
    0x4349: v4349(0x20) = CONST 
    0x434b: v434b(0x4a90) = CONST 
    0x4353: MSTORE v4345(0x0), v4348
    0x4357: v4357(0x0) = SUB v432e, v4333
    0x4358: v4358(0x20) = CONST 
    0x435a: v435a(0x20) = ADD v4358(0x20), v4357(0x0)
    0x435c: LOG3 v4333, v435a(0x20), v558e(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v4342, v433e
    0x4360: RETURNPRIVATE v4176arg3
    0x558e: v558e(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 

}

function burn(uint256)() public {
    Begin block 0x430
    prev=[], succ=[0x438, 0x43c]
    =================================
    0x431: v431 = CALLVALUE 
    0x433: v433 = ISZERO v431
    0x434: v434(0x43c) = CONST 
    0x437: JUMPI v434(0x43c), v433

    Begin block 0x438
    prev=[0x430], succ=[]
    =================================
    0x438: v438(0x0) = CONST 
    0x43b: REVERT v438(0x0), v438(0x0)

    Begin block 0x43c
    prev=[0x430], succ=[0x17f0B0x43c]
    =================================
    0x43e: v43e(0x4c70) = CONST 
    0x441: v441(0x4) = CONST 
    0x443: v443 = CALLDATALOAD v441(0x4)
    0x444: v444(0x17f0) = CONST 
    0x447: JUMP v444(0x17f0), v443, v43e(0x4c70)

    Begin block 0x17f0B0x43c
    prev=[0x43c], succ=[0x183eB0x43c, 0x1842B0x43c]
    =================================
    0x17f1S0x43c: v17f1V43c(0x3) = CONST 
    0x17f3S0x43c: v17f3V43c = SLOAD v17f1V43c(0x3)
    0x17f4S0x43c: v17f4V43c(0x40) = CONST 
    0x17f7S0x43c: v17f7V43c = MLOAD v17f4V43c(0x40)
    0x17f8S0x43c: v17f8V43c(0xe0) = CONST 
    0x17faS0x43c: v17faV43c(0x2) = CONST 
    0x17fcS0x43c: v17fcV43c(0x100000000000000000000000000000000000000000000000000000000) = EXP v17faV43c(0x2), v17f8V43c(0xe0)
    0x17fdS0x43c: v17fdV43c(0x7ccce851) = CONST 
    0x1802S0x43c: v1802V43c(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v17fdV43c(0x7ccce851), v17fcV43c(0x100000000000000000000000000000000000000000000000000000000)
    0x1804S0x43c: MSTORE v17f7V43c, v1802V43c(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1805S0x43c: v1805V43c = CALLER 
    0x1806S0x43c: v1806V43c(0x4) = CONST 
    0x1809S0x43c: v1809V43c = ADD v17f7V43c, v1806V43c(0x4)
    0x180cS0x43c: MSTORE v1809V43c, v1805V43c
    0x180eS0x43c: v180eV43c = MLOAD v17f4V43c(0x40)
    0x1811S0x43c: v1811V43c(0x1) = CONST 
    0x1813S0x43c: v1813V43c(0xa0) = CONST 
    0x1815S0x43c: v1815V43c(0x2) = CONST 
    0x1817S0x43c: v1817V43c(0x10000000000000000000000000000000000000000) = EXP v1815V43c(0x2), v1813V43c(0xa0)
    0x1818S0x43c: v1818V43c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1817V43c(0x10000000000000000000000000000000000000000), v1811V43c(0x1)
    0x1819S0x43c: v1819V43c = AND v1818V43c(0xffffffffffffffffffffffffffffffffffffffff), v17f3V43c
    0x181bS0x43c: v181bV43c(0x7ccce851) = CONST 
    0x1821S0x43c: v1821V43c(0x24) = CONST 
    0x1825S0x43c: v1825V43c = ADD v17f7V43c, v1821V43c(0x24)
    0x1827S0x43c: v1827V43c(0x20) = CONST 
    0x182fS0x43c: v182fV43c(0x0) = SUB v17f7V43c, v180eV43c
    0x1830S0x43c: v1830V43c(0x24) = ADD v182fV43c(0x0), v1821V43c(0x24)
    0x1832S0x43c: v1832V43c(0x0) = CONST 
    0x1836S0x43c: v1836V43c = EXTCODESIZE v1819V43c
    0x1837S0x43c: v1837V43c = ISZERO v1836V43c
    0x1839S0x43c: v1839V43c = ISZERO v1837V43c
    0x183aS0x43c: v183aV43c(0x1842) = CONST 
    0x183dS0x43c: JUMPI v183aV43c(0x1842), v1839V43c

    Begin block 0x183eB0x43c
    prev=[0x17f0B0x43c], succ=[]
    =================================
    0x183eS0x43c: v183eV43c(0x0) = CONST 
    0x1841S0x43c: REVERT v183eV43c(0x0), v183eV43c(0x0)

    Begin block 0x1842B0x43c
    prev=[0x17f0B0x43c], succ=[0x184dB0x43c, 0x1856B0x43c]
    =================================
    0x1844S0x43c: v1844V43c = GAS 
    0x1845S0x43c: v1845V43c = CALL v1844V43c, v1819V43c, v1832V43c(0x0), v180eV43c, v1830V43c(0x24), v180eV43c, v1827V43c(0x20)
    0x1846S0x43c: v1846V43c = ISZERO v1845V43c
    0x1848S0x43c: v1848V43c = ISZERO v1846V43c
    0x1849S0x43c: v1849V43c(0x1856) = CONST 
    0x184cS0x43c: JUMPI v1849V43c(0x1856), v1848V43c

    Begin block 0x184dB0x43c
    prev=[0x1842B0x43c], succ=[]
    =================================
    0x184dS0x43c: v184dV43c = RETURNDATASIZE 
    0x184eS0x43c: v184eV43c(0x0) = CONST 
    0x1851S0x43c: RETURNDATACOPY v184eV43c(0x0), v184eV43c(0x0), v184dV43c
    0x1852S0x43c: v1852V43c = RETURNDATASIZE 
    0x1853S0x43c: v1853V43c(0x0) = CONST 
    0x1855S0x43c: REVERT v1853V43c(0x0), v1852V43c

    Begin block 0x1856B0x43c
    prev=[0x1842B0x43c], succ=[0x1868B0x43c, 0x186cB0x43c]
    =================================
    0x185bS0x43c: v185bV43c(0x40) = CONST 
    0x185dS0x43c: v185dV43c = MLOAD v185bV43c(0x40)
    0x185eS0x43c: v185eV43c = RETURNDATASIZE 
    0x185fS0x43c: v185fV43c(0x20) = CONST 
    0x1862S0x43c: v1862V43c = LT v185eV43c, v185fV43c(0x20)
    0x1863S0x43c: v1863V43c = ISZERO v1862V43c
    0x1864S0x43c: v1864V43c(0x186c) = CONST 
    0x1867S0x43c: JUMPI v1864V43c(0x186c), v1863V43c

    Begin block 0x1868B0x43c
    prev=[0x1856B0x43c], succ=[]
    =================================
    0x1868S0x43c: v1868V43c(0x0) = CONST 
    0x186bS0x43c: REVERT v1868V43c(0x0), v1868V43c(0x0)

    Begin block 0x186cB0x43c
    prev=[0x1856B0x43c], succ=[0x1874B0x43c, 0x18b1B0x43c]
    =================================
    0x186eS0x43c: v186eV43c = MLOAD v185dV43c
    0x186fS0x43c: v186fV43c = ISZERO v186eV43c
    0x1870S0x43c: v1870V43c(0x18b1) = CONST 
    0x1873S0x43c: JUMPI v1870V43c(0x18b1), v186fV43c

    Begin block 0x1874B0x43c
    prev=[0x186cB0x43c], succ=[]
    =================================
    0x1874S0x43c: v1874V43c(0x40) = CONST 
    0x1877S0x43c: v1877V43c = MLOAD v1874V43c(0x40)
    0x1878S0x43c: v1878V43c(0xe5) = CONST 
    0x187aS0x43c: v187aV43c(0x2) = CONST 
    0x187cS0x43c: v187cV43c(0x2000000000000000000000000000000000000000000000000000000000) = EXP v187aV43c(0x2), v1878V43c(0xe5)
    0x187dS0x43c: v187dV43c(0x461bcd) = CONST 
    0x1881S0x43c: v1881V43c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v187dV43c(0x461bcd), v187cV43c(0x2000000000000000000000000000000000000000000000000000000000)
    0x1883S0x43c: MSTORE v1877V43c, v1881V43c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1884S0x43c: v1884V43c(0x20) = CONST 
    0x1886S0x43c: v1886V43c(0x4) = CONST 
    0x1889S0x43c: v1889V43c = ADD v1877V43c, v1886V43c(0x4)
    0x188aS0x43c: MSTORE v1889V43c, v1884V43c(0x20)
    0x188bS0x43c: v188bV43c(0x1c) = CONST 
    0x188dS0x43c: v188dV43c(0x24) = CONST 
    0x1890S0x43c: v1890V43c = ADD v1877V43c, v188dV43c(0x24)
    0x1891S0x43c: MSTORE v1890V43c, v188bV43c(0x1c)
    0x1892S0x43c: v1892V43c(0x0) = CONST 
    0x1895S0x43c: v1895V43c = MLOAD v1892V43c(0x0)
    0x1896S0x43c: v1896V43c(0x20) = CONST 
    0x1898S0x43c: v1898V43c(0x4a70) = CONST 
    0x18a0S0x43c: MSTORE v1892V43c(0x0), v1895V43c
    0x18a1S0x43c: v18a1V43c(0x44) = CONST 
    0x18a4S0x43c: v18a4V43c = ADD v1877V43c, v18a1V43c(0x44)
    0x18a5S0x43c: MSTORE v18a4V43c, v5543V43c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x18a7S0x43c: v18a7V43c = MLOAD v1874V43c(0x40)
    0x18abS0x43c: v18abV43c(0x0) = SUB v1877V43c, v18a7V43c
    0x18acS0x43c: v18acV43c(0x64) = CONST 
    0x18aeS0x43c: v18aeV43c(0x64) = ADD v18acV43c(0x64), v18abV43c(0x0)
    0x18b0S0x43c: REVERT v18a7V43c, v18aeV43c(0x64)
    0x5543S0x43c: v5543V43c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x18b1B0x43c
    prev=[0x186cB0x43c], succ=[0x18c4B0x43c, 0x18c8B0x43c]
    =================================
    0x18b2S0x43c: v18b2V43c(0x1) = CONST 
    0x18b4S0x43c: v18b4V43c = SLOAD v18b2V43c(0x1)
    0x18b5S0x43c: v18b5V43c(0xa0) = CONST 
    0x18b7S0x43c: v18b7V43c(0x2) = CONST 
    0x18b9S0x43c: v18b9V43c(0x10000000000000000000000000000000000000000) = EXP v18b7V43c(0x2), v18b5V43c(0xa0)
    0x18bbS0x43c: v18bbV43c = DIV v18b4V43c, v18b9V43c(0x10000000000000000000000000000000000000000)
    0x18bcS0x43c: v18bcV43c(0xff) = CONST 
    0x18beS0x43c: v18beV43c = AND v18bcV43c(0xff), v18bbV43c
    0x18bfS0x43c: v18bfV43c = ISZERO v18beV43c
    0x18c0S0x43c: v18c0V43c(0x18c8) = CONST 
    0x18c3S0x43c: JUMPI v18c0V43c(0x18c8), v18bfV43c

    Begin block 0x18c4B0x43c
    prev=[0x18b1B0x43c], succ=[]
    =================================
    0x18c4S0x43c: v18c4V43c(0x0) = CONST 
    0x18c7S0x43c: REVERT v18c4V43c(0x0), v18c4V43c(0x0)

    Begin block 0x18c8B0x43c
    prev=[0x18b1B0x43c], succ=[0x530eB0x43c]
    =================================
    0x18c9S0x43c: v18c9V43c(0x530e) = CONST 
    0x18ccS0x43c: v18ccV43c = CALLER 
    0x18ceS0x43c: v18ceV43c(0x3d80) = CONST 
    0x18d1S0x43c: CALLPRIVATE v18ceV43c(0x3d80), v443, v18ccV43c, v18c9V43c(0x530e)

    Begin block 0x530eB0x43c
    prev=[0x18c8B0x43c], succ=[0x4c70]
    =================================
    0x5311S0x43c: JUMP v43e(0x4c70)

    Begin block 0x4c70
    prev=[0x530eB0x43c], succ=[]
    =================================
    0x4c71: STOP 

}

function claimOwnership()() public {
    Begin block 0x448
    prev=[], succ=[0x450, 0x454]
    =================================
    0x449: v449 = CALLVALUE 
    0x44b: v44b = ISZERO v449
    0x44c: v44c(0x454) = CONST 
    0x44f: JUMPI v44c(0x454), v44b

    Begin block 0x450
    prev=[0x448], succ=[]
    =================================
    0x450: v450(0x0) = CONST 
    0x453: REVERT v450(0x0), v450(0x0)

    Begin block 0x454
    prev=[0x448], succ=[0x18d2]
    =================================
    0x456: v456(0x4c91) = CONST 
    0x459: v459(0x18d2) = CONST 
    0x45c: JUMP v459(0x18d2)

    Begin block 0x18d2
    prev=[0x454], succ=[0x18e5, 0x18e9]
    =================================
    0x18d3: v18d3(0x1) = CONST 
    0x18d5: v18d5 = SLOAD v18d3(0x1)
    0x18d6: v18d6(0x1) = CONST 
    0x18d8: v18d8(0xa0) = CONST 
    0x18da: v18da(0x2) = CONST 
    0x18dc: v18dc(0x10000000000000000000000000000000000000000) = EXP v18da(0x2), v18d8(0xa0)
    0x18dd: v18dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18dc(0x10000000000000000000000000000000000000000), v18d6(0x1)
    0x18de: v18de = AND v18dd(0xffffffffffffffffffffffffffffffffffffffff), v18d5
    0x18df: v18df = CALLER 
    0x18e0: v18e0 = EQ v18df, v18de
    0x18e1: v18e1(0x18e9) = CONST 
    0x18e4: JUMPI v18e1(0x18e9), v18e0

    Begin block 0x18e5
    prev=[0x18d2], succ=[]
    =================================
    0x18e5: v18e5(0x0) = CONST 
    0x18e8: REVERT v18e5(0x0), v18e5(0x0)

    Begin block 0x18e9
    prev=[0x18d2], succ=[0x4c91]
    =================================
    0x18ea: v18ea(0x1) = CONST 
    0x18ec: v18ec = SLOAD v18ea(0x1)
    0x18ed: v18ed(0x0) = CONST 
    0x18f0: v18f0 = SLOAD v18ed(0x0)
    0x18f1: v18f1(0x40) = CONST 
    0x18f3: v18f3 = MLOAD v18f1(0x40)
    0x18f4: v18f4(0x1) = CONST 
    0x18f6: v18f6(0xa0) = CONST 
    0x18f8: v18f8(0x2) = CONST 
    0x18fa: v18fa(0x10000000000000000000000000000000000000000) = EXP v18f8(0x2), v18f6(0xa0)
    0x18fb: v18fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18fa(0x10000000000000000000000000000000000000000), v18f4(0x1)
    0x18fe: v18fe = AND v18fb(0xffffffffffffffffffffffffffffffffffffffff), v18ec
    0x1902: v1902 = AND v18f0, v18fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x1904: v1904(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1926: LOG3 v18f3, v18ed(0x0), v1904(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1902, v18fe
    0x1927: v1927(0x1) = CONST 
    0x192a: v192a = SLOAD v1927(0x1)
    0x192b: v192b(0x0) = CONST 
    0x192e: v192e = SLOAD v192b(0x0)
    0x192f: v192f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1944: v1944(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v192f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1947: v1947 = AND v1944(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v192e
    0x1948: v1948(0x1) = CONST 
    0x194a: v194a(0xa0) = CONST 
    0x194c: v194c(0x2) = CONST 
    0x194e: v194e(0x10000000000000000000000000000000000000000) = EXP v194c(0x2), v194a(0xa0)
    0x194f: v194f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v194e(0x10000000000000000000000000000000000000000), v1948(0x1)
    0x1951: v1951 = AND v192a, v194f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1952: v1952 = OR v1951, v1947
    0x1955: SSTORE v192b(0x0), v1952
    0x1956: v1956 = AND v1944(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v192a
    0x1958: SSTORE v1927(0x1), v1956
    0x1959: JUMP v456(0x4c91)

    Begin block 0x4c91
    prev=[0x18e9], succ=[]
    =================================
    0x4c92: STOP 

}

function 0x44ed(0x44edarg0x0, 0x44edarg0x1, 0x44edarg0x2) private {
    Begin block 0x44ed
    prev=[], succ=[0x44ff, 0x4507]
    =================================
    0x44ee: v44ee(0x0) = CONST 
    0x44f1: v44f1(0x0) = CONST 
    0x44f5: v44f5 = MLOAD v44edarg0
    0x44f6: v44f6(0x41) = CONST 
    0x44f8: v44f8 = EQ v44f6(0x41), v44f5
    0x44f9: v44f9 = ISZERO v44f8
    0x44fa: v44fa = ISZERO v44f9
    0x44fb: v44fb(0x4507) = CONST 
    0x44fe: JUMPI v44fb(0x4507), v44fa

    Begin block 0x44ff
    prev=[0x44ed], succ=[0x5403]
    =================================
    0x44ff: v44ff(0x0) = CONST 
    0x4503: v4503(0x5403) = CONST 
    0x4506: JUMP v4503(0x5403)

    Begin block 0x5403
    prev=[0x44ff], succ=[]
    =================================
    0x540b: RETURNPRIVATE v44edarg2, v44ff(0x0)

    Begin block 0x4507
    prev=[0x44ed], succ=[0x4529, 0x452c]
    =================================
    0x450b: v450b(0x20) = CONST 
    0x450e: v450e = ADD v44edarg0, v450b(0x20)
    0x450f: v450f = MLOAD v450e
    0x4510: v4510(0x40) = CONST 
    0x4513: v4513 = ADD v44edarg0, v4510(0x40)
    0x4514: v4514 = MLOAD v4513
    0x4515: v4515(0x60) = CONST 
    0x4518: v4518 = ADD v44edarg0, v4515(0x60)
    0x4519: v4519 = MLOAD v4518
    0x451a: v451a(0x0) = CONST 
    0x451c: v451c = BYTE v451a(0x0), v4519
    0x451d: v451d(0x1b) = CONST 
    0x451f: v451f(0xff) = CONST 
    0x4522: v4522 = AND v451c, v451f(0xff)
    0x4523: v4523 = LT v4522, v451d(0x1b)
    0x4524: v4524 = ISZERO v4523
    0x4525: v4525(0x452c) = CONST 
    0x4528: JUMPI v4525(0x452c), v4524

    Begin block 0x4529
    prev=[0x4507], succ=[0x452c]
    =================================
    0x4529: v4529(0x1b) = CONST 
    0x452b: v452b = ADD v4529(0x1b), v451c

    Begin block 0x452c
    prev=[0x4529, 0x4507], succ=[0x4544, 0x453b]
    =================================
    0x452c_0x0: v452c_0 = PHI v451c, v452b
    0x452e: v452e(0xff) = CONST 
    0x4530: v4530 = AND v452e(0xff), v452c_0
    0x4531: v4531(0x1b) = CONST 
    0x4533: v4533 = EQ v4531(0x1b), v4530
    0x4534: v4534 = ISZERO v4533
    0x4536: v4536 = ISZERO v4534
    0x4537: v4537(0x4544) = CONST 
    0x453a: JUMPI v4537(0x4544), v4536

    Begin block 0x4544
    prev=[0x452c, 0x453b], succ=[0x454a, 0x4552]
    =================================
    0x4544_0x0: v4544_0 = PHI v4534, v4543
    0x4545: v4545 = ISZERO v4544_0
    0x4546: v4546(0x4552) = CONST 
    0x4549: JUMPI v4546(0x4552), v4545

    Begin block 0x454a
    prev=[0x4544], succ=[0x542b]
    =================================
    0x454a: v454a(0x0) = CONST 
    0x454e: v454e(0x542b) = CONST 
    0x4551: JUMP v454e(0x542b)

    Begin block 0x542b
    prev=[0x454a], succ=[]
    =================================
    0x5433: RETURNPRIVATE v44edarg2, v454a(0x0)

    Begin block 0x4552
    prev=[0x4544], succ=[0x45ab]
    =================================
    0x4553: v4553(0x40) = CONST 
    0x4556: v4556 = MLOAD v4553(0x40)
    0x4557: v4557(0x19457468657265756d205369676e6564204d6573736167653a0a333200000000) = CONST 
    0x4578: v4578(0x20) = CONST 
    0x457c: v457c = ADD v4556, v4578(0x20)
    0x4580: MSTORE v457c, v4557(0x19457468657265756d205369676e6564204d6573736167653a0a333200000000)
    0x4581: v4581(0x3c) = CONST 
    0x4585: v4585 = ADD v4556, v4581(0x3c)
    0x4588: MSTORE v4585, v44edarg1
    0x458a: v458a = MLOAD v4553(0x40)
    0x458d: v458d(0x0) = SUB v4556, v458a
    0x4590: v4590(0x3c) = ADD v4581(0x3c), v458d(0x0)
    0x4592: MSTORE v458a, v4590(0x3c)
    0x4593: v4593(0x5c) = CONST 
    0x4597: v4597 = ADD v4556, v4593(0x5c)
    0x459b: MSTORE v4553(0x40), v4597
    0x459d: v459d(0x3c) = MLOAD v458a
    0x459e: v459e(0x1) = CONST 
    0x45a6: v45a6 = ADD v458a, v4578(0x20)

    Begin block 0x45ab
    prev=[0x4552, 0x45b4], succ=[0x45ca, 0x45b4]
    =================================
    0x45ab_0x2: v45ab_2 = PHI v459d(0x3c), v45bd
    0x45ac: v45ac(0x20) = CONST 
    0x45af: v45af = LT v45ab_2, v45ac(0x20)
    0x45b0: v45b0(0x45ca) = CONST 
    0x45b3: JUMPI v45b0(0x45ca), v45af

    Begin block 0x45ca
    prev=[0x45ab], succ=[0x463d, 0x4646]
    =================================
    0x45ca_0x0: v45ca_0 = PHI v45a6, v45c5
    0x45ca_0x1: v45ca_1 = PHI v4597, v45c3
    0x45ca_0x2: v45ca_2 = PHI v459d(0x3c), v45bd
    0x45ca_0x9: v45ca_9 = PHI v451c, v452b
    0x45cb: v45cb = MLOAD v45ca_0
    0x45cd: v45cd = MLOAD v45ca_1
    0x45ce: v45ce(0x20) = CONST 
    0x45d2: v45d2 = SUB v45ce(0x20), v45ca_2
    0x45d3: v45d3(0x100) = CONST 
    0x45d6: v45d6 = EXP v45d3(0x100), v45d2
    0x45d7: v45d7(0x0) = CONST 
    0x45d9: v45d9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v45d7(0x0)
    0x45da: v45da = ADD v45d9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v45d6
    0x45dc: v45dc = NOT v45da
    0x45df: v45df = AND v45cb, v45dc
    0x45e1: v45e1 = AND v45da, v45cd
    0x45e2: v45e2 = OR v45e1, v45df
    0x45e4: MSTORE v45ca_1, v45e2
    0x45e5: v45e5(0x40) = CONST 
    0x45e8: v45e8 = MLOAD v45e5(0x40)
    0x45ec: v45ec = ADD v4597, v459d(0x3c)
    0x45ef: v45ef = SUB v45ec, v45e8
    0x45f1: v45f1 = SHA3 v45e8, v45ef
    0x45f2: v45f2(0x0) = CONST 
    0x45f6: MSTORE v45e8, v45f2(0x0)
    0x45f9: v45f9 = ADD v45ce(0x20), v45e8
    0x45fc: MSTORE v45e5(0x40), v45f9
    0x4600: MSTORE v45f9, v45f1
    0x4601: v4601(0xff) = CONST 
    0x4604: v4604 = AND v45ca_9, v4601(0xff)
    0x4607: v4607 = ADD v45e5(0x40), v45e8
    0x4608: MSTORE v4607, v4604
    0x4609: v4609(0x60) = CONST 
    0x460c: v460c = ADD v45e8, v4609(0x60)
    0x460f: MSTORE v460c, v450f
    0x4610: v4610(0x80) = CONST 
    0x4613: v4613 = ADD v45e8, v4610(0x80)
    0x4616: MSTORE v4613, v4514
    0x4618: v4618 = MLOAD v45e5(0x40)
    0x4619: v4619(0xa0) = CONST 
    0x461d: v461d = ADD v45e8, v4619(0xa0)
    0x4623: v4623(0x1f) = CONST 
    0x4625: v4625(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v4623(0x1f)
    0x4627: v4627 = ADD v4618, v4625(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x462c: v462c = SUB v45e8, v4618
    0x462f: v462f = ADD v4619(0xa0), v462c
    0x4634: v4634 = GAS 
    0x4635: v4635 = CALL v4634, v459e(0x1), v45f2(0x0), v4618, v462f, v4627, v45ce(0x20)
    0x4636: v4636 = ISZERO v4635
    0x4638: v4638 = ISZERO v4636
    0x4639: v4639(0x4646) = CONST 
    0x463c: JUMPI v4639(0x4646), v4638

    Begin block 0x463d
    prev=[0x45ca], succ=[]
    =================================
    0x463d: v463d = RETURNDATASIZE 
    0x463e: v463e(0x0) = CONST 
    0x4641: RETURNDATACOPY v463e(0x0), v463e(0x0), v463d
    0x4642: v4642 = RETURNDATASIZE 
    0x4643: v4643(0x0) = CONST 
    0x4645: REVERT v4643(0x0), v4642

    Begin block 0x4646
    prev=[0x45ca], succ=[0x4653]
    =================================
    0x464a: v464a(0x20) = CONST 
    0x464c: v464c(0x40) = CONST 
    0x464e: v464e = MLOAD v464c(0x40)
    0x464f: v464f = SUB v464e, v464a(0x20)
    0x4650: v4650 = MLOAD v464f

    Begin block 0x4653
    prev=[0x4646], succ=[]
    =================================
    0x465b: RETURNPRIVATE v44edarg2, v4650

    Begin block 0x45b4
    prev=[0x45ab], succ=[0x45ab]
    =================================
    0x45b4_0x0: v45b4_0 = PHI v45a6, v45c5
    0x45b4_0x1: v45b4_1 = PHI v4597, v45c3
    0x45b4_0x2: v45b4_2 = PHI v459d(0x3c), v45bd
    0x45b5: v45b5 = MLOAD v45b4_0
    0x45b7: MSTORE v45b4_1, v45b5
    0x45b8: v45b8(0x1f) = CONST 
    0x45ba: v45ba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v45b8(0x1f)
    0x45bd: v45bd = ADD v45b4_2, v45ba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x45bf: v45bf(0x20) = CONST 
    0x45c3: v45c3 = ADD v45bf(0x20), v45b4_1
    0x45c5: v45c5 = ADD v45bf(0x20), v45b4_0
    0x45c6: v45c6(0x45ab) = CONST 
    0x45c9: JUMP v45c6(0x45ab)

    Begin block 0x453b
    prev=[0x452c], succ=[0x4544]
    =================================
    0x453b_0x1: v453b_1 = PHI v451c, v452b
    0x453d: v453d(0xff) = CONST 
    0x453f: v453f = AND v453d(0xff), v453b_1
    0x4540: v4540(0x1c) = CONST 
    0x4542: v4542 = EQ v4540(0x1c), v453f
    0x4543: v4543 = ISZERO v4542

}

function blacklisted()() public {
    Begin block 0x45d
    prev=[], succ=[0x465, 0x469]
    =================================
    0x45e: v45e = CALLVALUE 
    0x460: v460 = ISZERO v45e
    0x461: v461(0x469) = CONST 
    0x464: JUMPI v461(0x469), v460

    Begin block 0x465
    prev=[0x45d], succ=[]
    =================================
    0x465: v465(0x0) = CONST 
    0x468: REVERT v465(0x0), v465(0x0)

    Begin block 0x469
    prev=[0x45d], succ=[0x195a]
    =================================
    0x46b: v46b(0x4cb2) = CONST 
    0x46e: v46e(0x195a) = CONST 
    0x471: JUMP v46e(0x195a)

    Begin block 0x195a
    prev=[0x469], succ=[0x19e3, 0x19e7]
    =================================
    0x195b: v195b(0x3) = CONST 
    0x195d: v195d = SLOAD v195b(0x3)
    0x195e: v195e(0x40) = CONST 
    0x1961: v1961 = MLOAD v195e(0x40)
    0x1962: v1962(0x14db6d5800000000000000000000000000000000000000000000000000000000) = CONST 
    0x1984: MSTORE v1961, v1962(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1985: v1985 = CALLER 
    0x1986: v1986(0x4) = CONST 
    0x1989: v1989 = ADD v1961, v1986(0x4)
    0x198a: MSTORE v1989, v1985
    0x198b: v198b(0x0) = CONST 
    0x198e: v198e = CALLDATALOAD v198b(0x0)
    0x198f: v198f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19ac: v19ac(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v198f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x19ad: v19ad = AND v19ac(0xffffffff00000000000000000000000000000000000000000000000000000000), v198e
    0x19ae: v19ae(0x24) = CONST 
    0x19b1: v19b1 = ADD v1961, v19ae(0x24)
    0x19b2: MSTORE v19b1, v19ad
    0x19b4: v19b4 = MLOAD v195e(0x40)
    0x19b7: v19b7(0x1) = CONST 
    0x19b9: v19b9(0xa0) = CONST 
    0x19bb: v19bb(0x2) = CONST 
    0x19bd: v19bd(0x10000000000000000000000000000000000000000) = EXP v19bb(0x2), v19b9(0xa0)
    0x19be: v19be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19bd(0x10000000000000000000000000000000000000000), v19b7(0x1)
    0x19bf: v19bf = AND v19be(0xffffffffffffffffffffffffffffffffffffffff), v195d
    0x19c1: v19c1(0x14db6d58) = CONST 
    0x19c7: v19c7(0x44) = CONST 
    0x19cb: v19cb = ADD v1961, v19c7(0x44)
    0x19cd: v19cd(0x20) = CONST 
    0x19d5: v19d5(0x0) = SUB v1961, v19b4
    0x19d6: v19d6(0x44) = ADD v19d5(0x0), v19c7(0x44)
    0x19db: v19db = EXTCODESIZE v19bf
    0x19dc: v19dc = ISZERO v19db
    0x19de: v19de = ISZERO v19dc
    0x19df: v19df(0x19e7) = CONST 
    0x19e2: JUMPI v19df(0x19e7), v19de

    Begin block 0x19e3
    prev=[0x195a], succ=[]
    =================================
    0x19e3: v19e3(0x0) = CONST 
    0x19e6: REVERT v19e3(0x0), v19e3(0x0)

    Begin block 0x19e7
    prev=[0x195a], succ=[0x19f2, 0x19fb]
    =================================
    0x19e9: v19e9 = GAS 
    0x19ea: v19ea = CALL v19e9, v19bf, v198b(0x0), v19b4, v19d6(0x44), v19b4, v19cd(0x20)
    0x19eb: v19eb = ISZERO v19ea
    0x19ed: v19ed = ISZERO v19eb
    0x19ee: v19ee(0x19fb) = CONST 
    0x19f1: JUMPI v19ee(0x19fb), v19ed

    Begin block 0x19f2
    prev=[0x19e7], succ=[]
    =================================
    0x19f2: v19f2 = RETURNDATASIZE 
    0x19f3: v19f3(0x0) = CONST 
    0x19f6: RETURNDATACOPY v19f3(0x0), v19f3(0x0), v19f2
    0x19f7: v19f7 = RETURNDATASIZE 
    0x19f8: v19f8(0x0) = CONST 
    0x19fa: REVERT v19f8(0x0), v19f7

    Begin block 0x19fb
    prev=[0x19e7], succ=[0x1a0d, 0x1a11]
    =================================
    0x1a00: v1a00(0x40) = CONST 
    0x1a02: v1a02 = MLOAD v1a00(0x40)
    0x1a03: v1a03 = RETURNDATASIZE 
    0x1a04: v1a04(0x20) = CONST 
    0x1a07: v1a07 = LT v1a03, v1a04(0x20)
    0x1a08: v1a08 = ISZERO v1a07
    0x1a09: v1a09(0x1a11) = CONST 
    0x1a0c: JUMPI v1a09(0x1a11), v1a08

    Begin block 0x1a0d
    prev=[0x19fb], succ=[]
    =================================
    0x1a0d: v1a0d(0x0) = CONST 
    0x1a10: REVERT v1a0d(0x0), v1a0d(0x0)

    Begin block 0x1a11
    prev=[0x19fb], succ=[0x1a1a, 0x1a8f]
    =================================
    0x1a13: v1a13 = MLOAD v1a02
    0x1a14: v1a14 = ISZERO v1a13
    0x1a15: v1a15 = ISZERO v1a14
    0x1a16: v1a16(0x1a8f) = CONST 
    0x1a19: JUMPI v1a16(0x1a8f), v1a15

    Begin block 0x1a1a
    prev=[0x1a11], succ=[]
    =================================
    0x1a1a: v1a1a(0x40) = CONST 
    0x1a1d: v1a1d = MLOAD v1a1a(0x40)
    0x1a1e: v1a1e(0xe5) = CONST 
    0x1a20: v1a20(0x2) = CONST 
    0x1a22: v1a22(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1a20(0x2), v1a1e(0xe5)
    0x1a23: v1a23(0x461bcd) = CONST 
    0x1a27: v1a27(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1a23(0x461bcd), v1a22(0x2000000000000000000000000000000000000000000000000000000000)
    0x1a29: MSTORE v1a1d, v1a27(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a2a: v1a2a(0x20) = CONST 
    0x1a2c: v1a2c(0x4) = CONST 
    0x1a2f: v1a2f = ADD v1a1d, v1a2c(0x4)
    0x1a30: MSTORE v1a2f, v1a2a(0x20)
    0x1a31: v1a31(0x31) = CONST 
    0x1a33: v1a33(0x24) = CONST 
    0x1a36: v1a36 = ADD v1a1d, v1a33(0x24)
    0x1a37: MSTORE v1a36, v1a31(0x31)
    0x1a38: v1a38(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x1a59: v1a59(0x44) = CONST 
    0x1a5c: v1a5c = ADD v1a1d, v1a59(0x44)
    0x1a5d: MSTORE v1a5c, v1a38(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x1a5e: v1a5e(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 
    0x1a7f: v1a7f(0x64) = CONST 
    0x1a82: v1a82 = ADD v1a1d, v1a7f(0x64)
    0x1a83: MSTORE v1a82, v1a5e(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x1a85: v1a85 = MLOAD v1a1a(0x40)
    0x1a89: v1a89(0x0) = SUB v1a1d, v1a85
    0x1a8a: v1a8a(0x84) = CONST 
    0x1a8c: v1a8c(0x84) = ADD v1a8a(0x84), v1a89(0x0)
    0x1a8e: REVERT v1a85, v1a8c(0x84)

    Begin block 0x1a8f
    prev=[0x1a11], succ=[0x4cb2]
    =================================
    0x1a91: v1a91(0x1) = CONST 
    0x1a94: JUMP v46b(0x4cb2)

    Begin block 0x4cb2
    prev=[0x1a8f], succ=[]
    =================================
    0x4cb3: v4cb3(0x40) = CONST 
    0x4cb6: v4cb6 = MLOAD v4cb3(0x40)
    0x4cb8: v4cb8 = ISZERO v1a91(0x1)
    0x4cb9: v4cb9 = ISZERO v4cb8
    0x4cbb: MSTORE v4cb6, v4cb9
    0x4cbc: v4cbc = MLOAD v4cb3(0x40)
    0x4cc0: v4cc0(0x0) = SUB v4cb6, v4cbc
    0x4cc1: v4cc1(0x20) = CONST 
    0x4cc3: v4cc3(0x20) = ADD v4cc1(0x20), v4cc0(0x0)
    0x4cc5: RETURN v4cbc, v4cc3(0x20)

}

function 0x465c(0x465carg0x0, 0x465carg0x1, 0x465carg0x2, 0x465carg0x3) private {
    Begin block 0x465c
    prev=[], succ=[0x46ce, 0x46d2]
    =================================
    0x465d: v465d(0x2) = CONST 
    0x465f: v465f = SLOAD v465d(0x2)
    0x4660: v4660(0x40) = CONST 
    0x4663: v4663 = MLOAD v4660(0x40)
    0x4664: v4664(0x5fd72d1600000000000000000000000000000000000000000000000000000000) = CONST 
    0x4686: MSTORE v4663, v4664(0x5fd72d1600000000000000000000000000000000000000000000000000000000)
    0x4687: v4687(0x1) = CONST 
    0x4689: v4689(0xa0) = CONST 
    0x468b: v468b(0x2) = CONST 
    0x468d: v468d(0x10000000000000000000000000000000000000000) = EXP v468b(0x2), v4689(0xa0)
    0x468e: v468e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v468d(0x10000000000000000000000000000000000000000), v4687(0x1)
    0x4691: v4691 = AND v468e(0xffffffffffffffffffffffffffffffffffffffff), v465carg0
    0x4692: v4692(0x4) = CONST 
    0x4695: v4695 = ADD v4663, v4692(0x4)
    0x4696: MSTORE v4695, v4691
    0x4699: v4699 = AND v468e(0xffffffffffffffffffffffffffffffffffffffff), v465carg2
    0x469a: v469a(0x24) = CONST 
    0x469d: v469d = ADD v4663, v469a(0x24)
    0x469e: MSTORE v469d, v4699
    0x469f: v469f(0x44) = CONST 
    0x46a2: v46a2 = ADD v4663, v469f(0x44)
    0x46a5: MSTORE v46a2, v465carg1
    0x46a7: v46a7 = MLOAD v4660(0x40)
    0x46ab: v46ab = AND v465f, v468e(0xffffffffffffffffffffffffffffffffffffffff)
    0x46ad: v46ad(0x5fd72d16) = CONST 
    0x46b3: v46b3(0x64) = CONST 
    0x46b7: v46b7 = ADD v4663, v46b3(0x64)
    0x46b9: v46b9(0x0) = CONST 
    0x46c0: v46c0(0x0) = SUB v4663, v46a7
    0x46c1: v46c1(0x64) = ADD v46c0(0x0), v46b3(0x64)
    0x46c6: v46c6 = EXTCODESIZE v46ab
    0x46c7: v46c7 = ISZERO v46c6
    0x46c9: v46c9 = ISZERO v46c7
    0x46ca: v46ca(0x46d2) = CONST 
    0x46cd: JUMPI v46ca(0x46d2), v46c9

    Begin block 0x46ce
    prev=[0x465c], succ=[]
    =================================
    0x46ce: v46ce(0x0) = CONST 
    0x46d1: REVERT v46ce(0x0), v46ce(0x0)

    Begin block 0x46d2
    prev=[0x465c], succ=[0x46dd, 0x46e6]
    =================================
    0x46d4: v46d4 = GAS 
    0x46d5: v46d5 = CALL v46d4, v46ab, v46b9(0x0), v46a7, v46c1(0x64), v46a7, v46b9(0x0)
    0x46d6: v46d6 = ISZERO v46d5
    0x46d8: v46d8 = ISZERO v46d6
    0x46d9: v46d9(0x46e6) = CONST 
    0x46dc: JUMPI v46d9(0x46e6), v46d8

    Begin block 0x46dd
    prev=[0x46d2], succ=[]
    =================================
    0x46dd: v46dd = RETURNDATASIZE 
    0x46de: v46de(0x0) = CONST 
    0x46e1: RETURNDATACOPY v46de(0x0), v46de(0x0), v46dd
    0x46e2: v46e2 = RETURNDATASIZE 
    0x46e3: v46e3(0x0) = CONST 
    0x46e5: REVERT v46e3(0x0), v46e2

    Begin block 0x46e6
    prev=[0x46d2], succ=[0x4729]
    =================================
    0x46ec: v46ec(0x1) = CONST 
    0x46ee: v46ee(0xa0) = CONST 
    0x46f0: v46f0(0x2) = CONST 
    0x46f2: v46f2(0x10000000000000000000000000000000000000000) = EXP v46f0(0x2), v46ee(0xa0)
    0x46f3: v46f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46f2(0x10000000000000000000000000000000000000000), v46ec(0x1)
    0x46f4: v46f4 = AND v46f3(0xffffffffffffffffffffffffffffffffffffffff), v465carg2
    0x46f6: v46f6(0x1) = CONST 
    0x46f8: v46f8(0xa0) = CONST 
    0x46fa: v46fa(0x2) = CONST 
    0x46fc: v46fc(0x10000000000000000000000000000000000000000) = EXP v46fa(0x2), v46f8(0xa0)
    0x46fd: v46fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46fc(0x10000000000000000000000000000000000000000), v46f6(0x1)
    0x46fe: v46fe = AND v46fd(0xffffffffffffffffffffffffffffffffffffffff), v465carg0
    0x46ff: v46ff(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x4720: v4720(0x4729) = CONST 
    0x4725: v4725(0x32b1) = CONST 
    0x4728: v4728_0 = CALLPRIVATE v4725(0x32b1), v465carg2, v465carg0, v4720(0x4729)

    Begin block 0x4729
    prev=[0x46e6], succ=[]
    =================================
    0x472a: v472a(0x40) = CONST 
    0x472d: v472d = MLOAD v472a(0x40)
    0x4730: MSTORE v472d, v4728_0
    0x4731: v4731 = MLOAD v472a(0x40)
    0x4735: v4735(0x0) = SUB v472d, v4731
    0x4736: v4736(0x20) = CONST 
    0x4738: v4738(0x20) = ADD v4736(0x20), v4735(0x0)
    0x473a: LOG3 v4731, v4738(0x20), v46ff(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v46fe, v46f4
    0x473e: RETURNPRIVATE v465carg3

}

function paused()() public {
    Begin block 0x472
    prev=[], succ=[0x47a, 0x47e]
    =================================
    0x473: v473 = CALLVALUE 
    0x475: v475 = ISZERO v473
    0x476: v476(0x47e) = CONST 
    0x479: JUMPI v476(0x47e), v475

    Begin block 0x47a
    prev=[0x472], succ=[]
    =================================
    0x47a: v47a(0x0) = CONST 
    0x47d: REVERT v47a(0x0), v47a(0x0)

    Begin block 0x47e
    prev=[0x472], succ=[0x1a95]
    =================================
    0x480: v480(0x4ce5) = CONST 
    0x483: v483(0x1a95) = CONST 
    0x486: JUMP v483(0x1a95)

    Begin block 0x1a95
    prev=[0x47e], succ=[0x4ce5]
    =================================
    0x1a96: v1a96(0x1) = CONST 
    0x1a98: v1a98 = SLOAD v1a96(0x1)
    0x1a99: v1a99(0xa0) = CONST 
    0x1a9b: v1a9b(0x2) = CONST 
    0x1a9d: v1a9d(0x10000000000000000000000000000000000000000) = EXP v1a9b(0x2), v1a99(0xa0)
    0x1a9f: v1a9f = DIV v1a98, v1a9d(0x10000000000000000000000000000000000000000)
    0x1aa0: v1aa0(0xff) = CONST 
    0x1aa2: v1aa2 = AND v1aa0(0xff), v1a9f
    0x1aa4: JUMP v480(0x4ce5)

    Begin block 0x4ce5
    prev=[0x1a95], succ=[]
    =================================
    0x4ce6: v4ce6(0x40) = CONST 
    0x4ce9: v4ce9 = MLOAD v4ce6(0x40)
    0x4ceb: v4ceb = ISZERO v1aa2
    0x4cec: v4cec = ISZERO v4ceb
    0x4cee: MSTORE v4ce9, v4cec
    0x4cef: v4cef = MLOAD v4ce6(0x40)
    0x4cf3: v4cf3(0x0) = SUB v4ce9, v4cef
    0x4cf4: v4cf4(0x20) = CONST 
    0x4cf6: v4cf6(0x20) = ADD v4cf4(0x20), v4cf3(0x0)
    0x4cf8: RETURN v4cef, v4cf6(0x20)

}

function 0x473f(0x473farg0x0, 0x473farg0x1, 0x473farg0x2, 0x473farg0x3) private {
    Begin block 0x473f
    prev=[], succ=[0x474d]
    =================================
    0x4740: v4740(0x0) = CONST 
    0x4743: v4743(0x0) = CONST 
    0x4745: v4745(0x474d) = CONST 
    0x4749: v4749(0x162d) = CONST 
    0x474c: v474c_0 = CALLPRIVATE v4749(0x162d), v473farg1, v4745(0x474d)

    Begin block 0x474d
    prev=[0x473f], succ=[0x4754, 0x47b7]
    =================================
    0x474e: v474e = ISZERO v474c_0
    0x474f: v474f = ISZERO v474e
    0x4750: v4750(0x47b7) = CONST 
    0x4753: JUMPI v4750(0x47b7), v474f

    Begin block 0x4754
    prev=[0x474d], succ=[]
    =================================
    0x4754: v4754(0x40) = CONST 
    0x4757: v4757 = MLOAD v4754(0x40)
    0x4758: v4758(0xe5) = CONST 
    0x475a: v475a(0x2) = CONST 
    0x475c: v475c(0x2000000000000000000000000000000000000000000000000000000000) = EXP v475a(0x2), v4758(0xe5)
    0x475d: v475d(0x461bcd) = CONST 
    0x4761: v4761(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v475d(0x461bcd), v475c(0x2000000000000000000000000000000000000000000000000000000000)
    0x4763: MSTORE v4757, v4761(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4764: v4764(0x20) = CONST 
    0x4766: v4766(0x4) = CONST 
    0x4769: v4769 = ADD v4757, v4766(0x4)
    0x476a: MSTORE v4769, v4764(0x20)
    0x476b: v476b(0x2f) = CONST 
    0x476d: v476d(0x24) = CONST 
    0x4770: v4770 = ADD v4757, v476d(0x24)
    0x4771: MSTORE v4770, v476b(0x2f)
    0x4772: v4772(0x0) = CONST 
    0x4775: v4775 = MLOAD v4772(0x0)
    0x4776: v4776(0x20) = CONST 
    0x4778: v4778(0x4a50) = CONST 
    0x4780: MSTORE v4772(0x0), v4775
    0x4781: v4781(0x44) = CONST 
    0x4784: v4784 = ADD v4757, v4781(0x44)
    0x4785: MSTORE v4784, v5593(0x537461626c65636f696e206d7573742062652077686974656c69737465642070)
    0x4786: v4786(0x72696f7220746f206275726e696e670000000000000000000000000000000000) = CONST 
    0x47a7: v47a7(0x64) = CONST 
    0x47aa: v47aa = ADD v4757, v47a7(0x64)
    0x47ab: MSTORE v47aa, v4786(0x72696f7220746f206275726e696e670000000000000000000000000000000000)
    0x47ad: v47ad = MLOAD v4754(0x40)
    0x47b1: v47b1(0x0) = SUB v4757, v47ad
    0x47b2: v47b2(0x84) = CONST 
    0x47b4: v47b4(0x84) = ADD v47b2(0x84), v47b1(0x0)
    0x47b6: REVERT v47ad, v47b4(0x84)
    0x5593: v5593(0x537461626c65636f696e206d7573742062652077686974656c69737465642070) = CONST 

    Begin block 0x47b7
    prev=[0x474d], succ=[0x481a, 0x481e]
    =================================
    0x47b8: v47b8(0x40) = CONST 
    0x47bb: v47bb = MLOAD v47b8(0x40)
    0x47bc: v47bc(0x70a0823100000000000000000000000000000000000000000000000000000000) = CONST 
    0x47de: MSTORE v47bb, v47bc(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x47df: v47df = ADDRESS 
    0x47e0: v47e0(0x4) = CONST 
    0x47e3: v47e3 = ADD v47bb, v47e0(0x4)
    0x47e4: MSTORE v47e3, v47df
    0x47e6: v47e6 = MLOAD v47b8(0x40)
    0x47ec: v47ec(0x1) = CONST 
    0x47ee: v47ee(0xa0) = CONST 
    0x47f0: v47f0(0x2) = CONST 
    0x47f2: v47f2(0x10000000000000000000000000000000000000000) = EXP v47f0(0x2), v47ee(0xa0)
    0x47f3: v47f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v47f2(0x10000000000000000000000000000000000000000), v47ec(0x1)
    0x47f5: v47f5 = AND v473farg1, v47f3(0xffffffffffffffffffffffffffffffffffffffff)
    0x47f7: v47f7(0x70a08231) = CONST 
    0x47fd: v47fd(0x24) = CONST 
    0x4801: v4801 = ADD v47bb, v47fd(0x24)
    0x4803: v4803(0x20) = CONST 
    0x480b: v480b(0x0) = SUB v47bb, v47e6
    0x480c: v480c(0x24) = ADD v480b(0x0), v47fd(0x24)
    0x480e: v480e(0x0) = CONST 
    0x4812: v4812 = EXTCODESIZE v47f5
    0x4813: v4813 = ISZERO v4812
    0x4815: v4815 = ISZERO v4813
    0x4816: v4816(0x481e) = CONST 
    0x4819: JUMPI v4816(0x481e), v4815

    Begin block 0x481a
    prev=[0x47b7], succ=[]
    =================================
    0x481a: v481a(0x0) = CONST 
    0x481d: REVERT v481a(0x0), v481a(0x0)

    Begin block 0x481e
    prev=[0x47b7], succ=[0x4829, 0x4832]
    =================================
    0x4820: v4820 = GAS 
    0x4821: v4821 = CALL v4820, v47f5, v480e(0x0), v47e6, v480c(0x24), v47e6, v4803(0x20)
    0x4822: v4822 = ISZERO v4821
    0x4824: v4824 = ISZERO v4822
    0x4825: v4825(0x4832) = CONST 
    0x4828: JUMPI v4825(0x4832), v4824

    Begin block 0x4829
    prev=[0x481e], succ=[]
    =================================
    0x4829: v4829 = RETURNDATASIZE 
    0x482a: v482a(0x0) = CONST 
    0x482d: RETURNDATACOPY v482a(0x0), v482a(0x0), v4829
    0x482e: v482e = RETURNDATASIZE 
    0x482f: v482f(0x0) = CONST 
    0x4831: REVERT v482f(0x0), v482e

    Begin block 0x4832
    prev=[0x481e], succ=[0x4844, 0x4848]
    =================================
    0x4837: v4837(0x40) = CONST 
    0x4839: v4839 = MLOAD v4837(0x40)
    0x483a: v483a = RETURNDATASIZE 
    0x483b: v483b(0x20) = CONST 
    0x483e: v483e = LT v483a, v483b(0x20)
    0x483f: v483f = ISZERO v483e
    0x4840: v4840(0x4848) = CONST 
    0x4843: JUMPI v4840(0x4848), v483f

    Begin block 0x4844
    prev=[0x4832], succ=[]
    =================================
    0x4844: v4844(0x0) = CONST 
    0x4847: REVERT v4844(0x0), v4844(0x0)

    Begin block 0x4848
    prev=[0x4832], succ=[0x4851, 0x48ec]
    =================================
    0x484a: v484a = MLOAD v4839
    0x484b: v484b = LT v484a, v473farg0
    0x484c: v484c = ISZERO v484b
    0x484d: v484d(0x48ec) = CONST 
    0x4850: JUMPI v484d(0x48ec), v484c

    Begin block 0x4851
    prev=[0x4848], succ=[]
    =================================
    0x4851: v4851(0x40) = CONST 
    0x4854: v4854 = MLOAD v4851(0x40)
    0x4855: v4855(0xe5) = CONST 
    0x4857: v4857(0x2) = CONST 
    0x4859: v4859(0x2000000000000000000000000000000000000000000000000000000000) = EXP v4857(0x2), v4855(0xe5)
    0x485a: v485a(0x461bcd) = CONST 
    0x485e: v485e(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v485a(0x461bcd), v4859(0x2000000000000000000000000000000000000000000000000000000000)
    0x4860: MSTORE v4854, v485e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4861: v4861(0x20) = CONST 
    0x4863: v4863(0x4) = CONST 
    0x4866: v4866 = ADD v4854, v4863(0x4)
    0x4867: MSTORE v4866, v4861(0x20)
    0x4868: v4868(0x43) = CONST 
    0x486a: v486a(0x24) = CONST 
    0x486d: v486d = ADD v4854, v486a(0x24)
    0x486e: MSTORE v486d, v4868(0x43)
    0x486f: v486f(0x436172626f6e20657363726f77206163636f756e7420696e2057543020646f65) = CONST 
    0x4890: v4890(0x44) = CONST 
    0x4893: v4893 = ADD v4854, v4890(0x44)
    0x4894: MSTORE v4893, v486f(0x436172626f6e20657363726f77206163636f756e7420696e2057543020646f65)
    0x4895: v4895(0x736e2774206861766520656e6f75676820746f6b656e7320666f72206275726e) = CONST 
    0x48b6: v48b6(0x64) = CONST 
    0x48b9: v48b9 = ADD v4854, v48b6(0x64)
    0x48ba: MSTORE v48b9, v4895(0x736e2774206861766520656e6f75676820746f6b656e7320666f72206275726e)
    0x48bb: v48bb(0x696e670000000000000000000000000000000000000000000000000000000000) = CONST 
    0x48dc: v48dc(0x84) = CONST 
    0x48df: v48df = ADD v4854, v48dc(0x84)
    0x48e0: MSTORE v48df, v48bb(0x696e670000000000000000000000000000000000000000000000000000000000)
    0x48e2: v48e2 = MLOAD v4851(0x40)
    0x48e6: v48e6(0x0) = SUB v4854, v48e2
    0x48e7: v48e7(0xa4) = CONST 
    0x48e9: v48e9(0xa4) = ADD v48e7(0xa4), v48e6(0x0)
    0x48eb: REVERT v48e2, v48e9(0xa4)

    Begin block 0x48ec
    prev=[0x4848], succ=[0x4907]
    =================================
    0x48ed: v48ed(0x4) = CONST 
    0x48ef: v48ef = SLOAD v48ed(0x4)
    0x48f0: v48f0(0x1) = CONST 
    0x48f2: v48f2(0xa0) = CONST 
    0x48f4: v48f4(0x2) = CONST 
    0x48f6: v48f6(0x10000000000000000000000000000000000000000) = EXP v48f4(0x2), v48f2(0xa0)
    0x48f7: v48f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48f6(0x10000000000000000000000000000000000000000), v48f0(0x1)
    0x48f8: v48f8 = AND v48f7(0xffffffffffffffffffffffffffffffffffffffff), v48ef
    0x48f9: v48f9(0x2ff284c2) = CONST 
    0x48ff: v48ff(0x4907) = CONST 
    0x4903: v4903(0x24f9) = CONST 
    0x4906: v4906_0 = CALLPRIVATE v4903(0x24f9), v473farg1, v48ff(0x4907)

    Begin block 0x4907
    prev=[0x48ec], succ=[0x4943, 0x4947]
    =================================
    0x4908: v4908(0x40) = CONST 
    0x490a: v490a = MLOAD v4908(0x40)
    0x490c: v490c(0xffffffff) = CONST 
    0x4911: v4911(0x2ff284c2) = AND v490c(0xffffffff), v48f9(0x2ff284c2)
    0x4912: v4912(0xe0) = CONST 
    0x4914: v4914(0x2) = CONST 
    0x4916: v4916(0x100000000000000000000000000000000000000000000000000000000) = EXP v4914(0x2), v4912(0xe0)
    0x4917: v4917(0x2ff284c200000000000000000000000000000000000000000000000000000000) = MUL v4916(0x100000000000000000000000000000000000000000000000000000000), v4911(0x2ff284c2)
    0x4919: MSTORE v490a, v4917(0x2ff284c200000000000000000000000000000000000000000000000000000000)
    0x491a: v491a(0x4) = CONST 
    0x491c: v491c = ADD v491a(0x4), v490a
    0x4920: MSTORE v491c, v473farg0
    0x4921: v4921(0x20) = CONST 
    0x4923: v4923 = ADD v4921(0x20), v491c
    0x4926: MSTORE v4923, v4906_0
    0x4927: v4927(0x20) = CONST 
    0x4929: v4929 = ADD v4927(0x20), v4923
    0x492e: v492e(0x20) = CONST 
    0x4930: v4930(0x40) = CONST 
    0x4932: v4932 = MLOAD v4930(0x40)
    0x4935: v4935(0x44) = SUB v4929, v4932
    0x4937: v4937(0x0) = CONST 
    0x493b: v493b = EXTCODESIZE v48f8
    0x493c: v493c = ISZERO v493b
    0x493e: v493e = ISZERO v493c
    0x493f: v493f(0x4947) = CONST 
    0x4942: JUMPI v493f(0x4947), v493e

    Begin block 0x4943
    prev=[0x4907], succ=[]
    =================================
    0x4943: v4943(0x0) = CONST 
    0x4946: REVERT v4943(0x0), v4943(0x0)

    Begin block 0x4947
    prev=[0x4907], succ=[0x4952, 0x495b]
    =================================
    0x4949: v4949 = GAS 
    0x494a: v494a = CALL v4949, v48f8, v4937(0x0), v4932, v4935(0x44), v4932, v492e(0x20)
    0x494b: v494b = ISZERO v494a
    0x494d: v494d = ISZERO v494b
    0x494e: v494e(0x495b) = CONST 
    0x4951: JUMPI v494e(0x495b), v494d

    Begin block 0x4952
    prev=[0x4947], succ=[]
    =================================
    0x4952: v4952 = RETURNDATASIZE 
    0x4953: v4953(0x0) = CONST 
    0x4956: RETURNDATACOPY v4953(0x0), v4953(0x0), v4952
    0x4957: v4957 = RETURNDATASIZE 
    0x4958: v4958(0x0) = CONST 
    0x495a: REVERT v4958(0x0), v4957

    Begin block 0x495b
    prev=[0x4947], succ=[0x496d, 0x4971]
    =================================
    0x4960: v4960(0x40) = CONST 
    0x4962: v4962 = MLOAD v4960(0x40)
    0x4963: v4963 = RETURNDATASIZE 
    0x4964: v4964(0x20) = CONST 
    0x4967: v4967 = LT v4963, v4964(0x20)
    0x4968: v4968 = ISZERO v4967
    0x4969: v4969(0x4971) = CONST 
    0x496c: JUMPI v4969(0x4971), v4968

    Begin block 0x496d
    prev=[0x495b], succ=[]
    =================================
    0x496d: v496d(0x0) = CONST 
    0x4970: REVERT v496d(0x0), v496d(0x0)

    Begin block 0x4971
    prev=[0x495b], succ=[0x3d6eB0x4971]
    =================================
    0x4973: v4973 = MLOAD v4962
    0x4976: v4976(0x4985) = CONST 
    0x497b: v497b(0xffffffff) = CONST 
    0x4980: v4980(0x3d6e) = CONST 
    0x4983: v4983(0x3d6e) = AND v4980(0x3d6e), v497b(0xffffffff)
    0x4984: JUMP v4983(0x3d6e)

    Begin block 0x3d6eB0x4971
    prev=[0x4971], succ=[0x3d7aB0x4971, 0x3d79B0x4971]
    =================================
    0x3d6fS0x4971: v3d6fV4971(0x0) = CONST 
    0x3d73S0x4971: v3d73V4971 = GT v4973, v473farg0
    0x3d74S0x4971: v3d74V4971 = ISZERO v3d73V4971
    0x3d75S0x4971: v3d75V4971(0x3d7a) = CONST 
    0x3d78S0x4971: JUMPI v3d75V4971(0x3d7a), v3d74V4971

    Begin block 0x3d7aB0x4971
    prev=[0x3d6eB0x4971], succ=[0x4985]
    =================================
    0x3d7dS0x4971: v3d7dV4971 = SUB v473farg0, v4973
    0x3d7fS0x4971: JUMP v4976(0x4985)

    Begin block 0x4985
    prev=[0x3d7aB0x4971], succ=[0x4991]
    =================================
    0x4988: v4988(0x4991) = CONST 
    0x498d: v498d(0x3d80) = CONST 
    0x4990: CALLPRIVATE v498d(0x3d80), v473farg0, v473farg2, v4988(0x4991)

    Begin block 0x4991
    prev=[0x4985], succ=[0x49d6, 0x49da]
    =================================
    0x4993: v4993(0x1) = CONST 
    0x4995: v4995(0xa0) = CONST 
    0x4997: v4997(0x2) = CONST 
    0x4999: v4999(0x10000000000000000000000000000000000000000) = EXP v4997(0x2), v4995(0xa0)
    0x499a: v499a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4999(0x10000000000000000000000000000000000000000), v4993(0x1)
    0x499b: v499b = AND v499a(0xffffffffffffffffffffffffffffffffffffffff), v473farg1
    0x499c: v499c(0x42966c68) = CONST 
    0x49a2: v49a2(0x40) = CONST 
    0x49a4: v49a4 = MLOAD v49a2(0x40)
    0x49a6: v49a6(0xffffffff) = CONST 
    0x49ab: v49ab(0x42966c68) = AND v49a6(0xffffffff), v499c(0x42966c68)
    0x49ac: v49ac(0xe0) = CONST 
    0x49ae: v49ae(0x2) = CONST 
    0x49b0: v49b0(0x100000000000000000000000000000000000000000000000000000000) = EXP v49ae(0x2), v49ac(0xe0)
    0x49b1: v49b1(0x42966c6800000000000000000000000000000000000000000000000000000000) = MUL v49b0(0x100000000000000000000000000000000000000000000000000000000), v49ab(0x42966c68)
    0x49b3: MSTORE v49a4, v49b1(0x42966c6800000000000000000000000000000000000000000000000000000000)
    0x49b4: v49b4(0x4) = CONST 
    0x49b6: v49b6 = ADD v49b4(0x4), v49a4
    0x49ba: MSTORE v49b6, v473farg0
    0x49bb: v49bb(0x20) = CONST 
    0x49bd: v49bd = ADD v49bb(0x20), v49b6
    0x49c1: v49c1(0x0) = CONST 
    0x49c3: v49c3(0x40) = CONST 
    0x49c5: v49c5 = MLOAD v49c3(0x40)
    0x49c8: v49c8(0x24) = SUB v49bd, v49c5
    0x49ca: v49ca(0x0) = CONST 
    0x49ce: v49ce = EXTCODESIZE v499b
    0x49cf: v49cf = ISZERO v49ce
    0x49d1: v49d1 = ISZERO v49cf
    0x49d2: v49d2(0x49da) = CONST 
    0x49d5: JUMPI v49d2(0x49da), v49d1

    Begin block 0x49d6
    prev=[0x4991], succ=[]
    =================================
    0x49d6: v49d6(0x0) = CONST 
    0x49d9: REVERT v49d6(0x0), v49d6(0x0)

    Begin block 0x49da
    prev=[0x4991], succ=[0x49e5, 0x49ee]
    =================================
    0x49dc: v49dc = GAS 
    0x49dd: v49dd = CALL v49dc, v499b, v49ca(0x0), v49c5, v49c8(0x24), v49c5, v49c1(0x0)
    0x49de: v49de = ISZERO v49dd
    0x49e0: v49e0 = ISZERO v49de
    0x49e1: v49e1(0x49ee) = CONST 
    0x49e4: JUMPI v49e1(0x49ee), v49e0

    Begin block 0x49e5
    prev=[0x49da], succ=[]
    =================================
    0x49e5: v49e5 = RETURNDATASIZE 
    0x49e6: v49e6(0x0) = CONST 
    0x49e9: RETURNDATACOPY v49e6(0x0), v49e6(0x0), v49e5
    0x49ea: v49ea = RETURNDATASIZE 
    0x49eb: v49eb(0x0) = CONST 
    0x49ed: REVERT v49eb(0x0), v49ea

    Begin block 0x49ee
    prev=[0x49da], succ=[0x49fc]
    =================================
    0x49f3: v49f3(0x49fc) = CONST 
    0x49f6: v49f6 = ADDRESS 
    0x49f8: v49f8(0x3fa0) = CONST 
    0x49fb: CALLPRIVATE v49f8(0x3fa0), v4973, v49f6, v49f3(0x49fc)

    Begin block 0x49fc
    prev=[0x49ee], succ=[]
    =================================
    0x49fd: v49fd(0x40) = CONST 
    0x4a00: v4a00 = MLOAD v49fd(0x40)
    0x4a03: MSTORE v4a00, v3d7dV4971
    0x4a04: v4a04(0x20) = CONST 
    0x4a07: v4a07 = ADD v4a00, v4a04(0x20)
    0x4a0a: MSTORE v4a07, v4973
    0x4a0c: v4a0c = MLOAD v49fd(0x40)
    0x4a0d: v4a0d(0x1) = CONST 
    0x4a0f: v4a0f(0xa0) = CONST 
    0x4a11: v4a11(0x2) = CONST 
    0x4a13: v4a13(0x10000000000000000000000000000000000000000) = EXP v4a11(0x2), v4a0f(0xa0)
    0x4a14: v4a14(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a13(0x10000000000000000000000000000000000000000), v4a0d(0x1)
    0x4a16: v4a16 = AND v473farg2, v4a14(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a18: v4a18(0x8a1387ce462b7423a12c936187028c782512f204b670218701c0d35e92bc0527) = CONST 
    0x4a3c: v4a3c(0x0) = SUB v4a00, v4a0c
    0x4a3d: v4a3d(0x40) = ADD v4a3c(0x0), v49fd(0x40)
    0x4a3f: LOG2 v4a0c, v4a3d(0x40), v4a18(0x8a1387ce462b7423a12c936187028c782512f204b670218701c0d35e92bc0527), v4a16
    0x4a46: RETURNPRIVATE v473farg3

    Begin block 0x3d79B0x4971
    prev=[0x3d6eB0x4971], succ=[]
    =================================
    0x3d79S0x4971: THROW 

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x487
    prev=[], succ=[0x48f, 0x493]
    =================================
    0x488: v488 = CALLVALUE 
    0x48a: v48a = ISZERO v488
    0x48b: v48b(0x493) = CONST 
    0x48e: JUMPI v48b(0x493), v48a

    Begin block 0x48f
    prev=[0x487], succ=[]
    =================================
    0x48f: v48f(0x0) = CONST 
    0x492: REVERT v48f(0x0), v48f(0x0)

    Begin block 0x493
    prev=[0x487], succ=[0x1aa5]
    =================================
    0x495: v495(0x4d18) = CONST 
    0x498: v498(0x1) = CONST 
    0x49a: v49a(0xa0) = CONST 
    0x49c: v49c(0x2) = CONST 
    0x49e: v49e(0x10000000000000000000000000000000000000000) = EXP v49c(0x2), v49a(0xa0)
    0x49f: v49f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49e(0x10000000000000000000000000000000000000000), v498(0x1)
    0x4a0: v4a0(0x4) = CONST 
    0x4a2: v4a2 = CALLDATALOAD v4a0(0x4)
    0x4a3: v4a3 = AND v4a2, v49f(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a4: v4a4(0x24) = CONST 
    0x4a6: v4a6 = CALLDATALOAD v4a4(0x24)
    0x4a7: v4a7(0x1aa5) = CONST 
    0x4aa: JUMP v4a7(0x1aa5)

    Begin block 0x1aa5
    prev=[0x493], succ=[0x1af4, 0x1af8]
    =================================
    0x1aa6: v1aa6(0x3) = CONST 
    0x1aa8: v1aa8 = SLOAD v1aa6(0x3)
    0x1aa9: v1aa9(0x40) = CONST 
    0x1aac: v1aac = MLOAD v1aa9(0x40)
    0x1aad: v1aad(0xe0) = CONST 
    0x1aaf: v1aaf(0x2) = CONST 
    0x1ab1: v1ab1(0x100000000000000000000000000000000000000000000000000000000) = EXP v1aaf(0x2), v1aad(0xe0)
    0x1ab2: v1ab2(0x7ccce851) = CONST 
    0x1ab7: v1ab7(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1ab2(0x7ccce851), v1ab1(0x100000000000000000000000000000000000000000000000000000000)
    0x1ab9: MSTORE v1aac, v1ab7(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1aba: v1aba(0x1) = CONST 
    0x1abc: v1abc(0xa0) = CONST 
    0x1abe: v1abe(0x2) = CONST 
    0x1ac0: v1ac0(0x10000000000000000000000000000000000000000) = EXP v1abe(0x2), v1abc(0xa0)
    0x1ac1: v1ac1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ac0(0x10000000000000000000000000000000000000000), v1aba(0x1)
    0x1ac4: v1ac4 = AND v4a3, v1ac1(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ac5: v1ac5(0x4) = CONST 
    0x1ac8: v1ac8 = ADD v1aac, v1ac5(0x4)
    0x1ac9: MSTORE v1ac8, v1ac4
    0x1acb: v1acb = MLOAD v1aa9(0x40)
    0x1acc: v1acc(0x0) = CONST 
    0x1ad1: v1ad1 = AND v1ac1(0xffffffffffffffffffffffffffffffffffffffff), v1aa8
    0x1ad3: v1ad3(0x7ccce851) = CONST 
    0x1ad9: v1ad9(0x24) = CONST 
    0x1add: v1add = ADD v1aac, v1ad9(0x24)
    0x1adf: v1adf(0x20) = CONST 
    0x1ae6: v1ae6(0x0) = SUB v1aac, v1acb
    0x1ae7: v1ae7(0x24) = ADD v1ae6(0x0), v1ad9(0x24)
    0x1aec: v1aec = EXTCODESIZE v1ad1
    0x1aed: v1aed = ISZERO v1aec
    0x1aef: v1aef = ISZERO v1aed
    0x1af0: v1af0(0x1af8) = CONST 
    0x1af3: JUMPI v1af0(0x1af8), v1aef

    Begin block 0x1af4
    prev=[0x1aa5], succ=[]
    =================================
    0x1af4: v1af4(0x0) = CONST 
    0x1af7: REVERT v1af4(0x0), v1af4(0x0)

    Begin block 0x1af8
    prev=[0x1aa5], succ=[0x1b03, 0x1b0c]
    =================================
    0x1afa: v1afa = GAS 
    0x1afb: v1afb = CALL v1afa, v1ad1, v1acc(0x0), v1acb, v1ae7(0x24), v1acb, v1adf(0x20)
    0x1afc: v1afc = ISZERO v1afb
    0x1afe: v1afe = ISZERO v1afc
    0x1aff: v1aff(0x1b0c) = CONST 
    0x1b02: JUMPI v1aff(0x1b0c), v1afe

    Begin block 0x1b03
    prev=[0x1af8], succ=[]
    =================================
    0x1b03: v1b03 = RETURNDATASIZE 
    0x1b04: v1b04(0x0) = CONST 
    0x1b07: RETURNDATACOPY v1b04(0x0), v1b04(0x0), v1b03
    0x1b08: v1b08 = RETURNDATASIZE 
    0x1b09: v1b09(0x0) = CONST 
    0x1b0b: REVERT v1b09(0x0), v1b08

    Begin block 0x1b0c
    prev=[0x1af8], succ=[0x1b1e, 0x1b22]
    =================================
    0x1b11: v1b11(0x40) = CONST 
    0x1b13: v1b13 = MLOAD v1b11(0x40)
    0x1b14: v1b14 = RETURNDATASIZE 
    0x1b15: v1b15(0x20) = CONST 
    0x1b18: v1b18 = LT v1b14, v1b15(0x20)
    0x1b19: v1b19 = ISZERO v1b18
    0x1b1a: v1b1a(0x1b22) = CONST 
    0x1b1d: JUMPI v1b1a(0x1b22), v1b19

    Begin block 0x1b1e
    prev=[0x1b0c], succ=[]
    =================================
    0x1b1e: v1b1e(0x0) = CONST 
    0x1b21: REVERT v1b1e(0x0), v1b1e(0x0)

    Begin block 0x1b22
    prev=[0x1b0c], succ=[0x1b2a, 0x1b67]
    =================================
    0x1b24: v1b24 = MLOAD v1b13
    0x1b25: v1b25 = ISZERO v1b24
    0x1b26: v1b26(0x1b67) = CONST 
    0x1b29: JUMPI v1b26(0x1b67), v1b25

    Begin block 0x1b2a
    prev=[0x1b22], succ=[]
    =================================
    0x1b2a: v1b2a(0x40) = CONST 
    0x1b2d: v1b2d = MLOAD v1b2a(0x40)
    0x1b2e: v1b2e(0xe5) = CONST 
    0x1b30: v1b30(0x2) = CONST 
    0x1b32: v1b32(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1b30(0x2), v1b2e(0xe5)
    0x1b33: v1b33(0x461bcd) = CONST 
    0x1b37: v1b37(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1b33(0x461bcd), v1b32(0x2000000000000000000000000000000000000000000000000000000000)
    0x1b39: MSTORE v1b2d, v1b37(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b3a: v1b3a(0x20) = CONST 
    0x1b3c: v1b3c(0x4) = CONST 
    0x1b3f: v1b3f = ADD v1b2d, v1b3c(0x4)
    0x1b40: MSTORE v1b3f, v1b3a(0x20)
    0x1b41: v1b41(0x1c) = CONST 
    0x1b43: v1b43(0x24) = CONST 
    0x1b46: v1b46 = ADD v1b2d, v1b43(0x24)
    0x1b47: MSTORE v1b46, v1b41(0x1c)
    0x1b48: v1b48(0x0) = CONST 
    0x1b4b: v1b4b = MLOAD v1b48(0x0)
    0x1b4c: v1b4c(0x20) = CONST 
    0x1b4e: v1b4e(0x4a70) = CONST 
    0x1b56: MSTORE v1b48(0x0), v1b4b
    0x1b57: v1b57(0x44) = CONST 
    0x1b5a: v1b5a = ADD v1b2d, v1b57(0x44)
    0x1b5b: MSTORE v1b5a, v5548(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x1b5d: v1b5d = MLOAD v1b2a(0x40)
    0x1b61: v1b61(0x0) = SUB v1b2d, v1b5d
    0x1b62: v1b62(0x64) = CONST 
    0x1b64: v1b64(0x64) = ADD v1b62(0x64), v1b61(0x0)
    0x1b66: REVERT v1b5d, v1b64(0x64)
    0x5548: v5548(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x1b67
    prev=[0x1b22], succ=[0x1bb5, 0x1bb9]
    =================================
    0x1b68: v1b68(0x3) = CONST 
    0x1b6a: v1b6a = SLOAD v1b68(0x3)
    0x1b6b: v1b6b(0x40) = CONST 
    0x1b6e: v1b6e = MLOAD v1b6b(0x40)
    0x1b6f: v1b6f(0xe0) = CONST 
    0x1b71: v1b71(0x2) = CONST 
    0x1b73: v1b73(0x100000000000000000000000000000000000000000000000000000000) = EXP v1b71(0x2), v1b6f(0xe0)
    0x1b74: v1b74(0x7ccce851) = CONST 
    0x1b79: v1b79(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1b74(0x7ccce851), v1b73(0x100000000000000000000000000000000000000000000000000000000)
    0x1b7b: MSTORE v1b6e, v1b79(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1b7c: v1b7c = CALLER 
    0x1b7d: v1b7d(0x4) = CONST 
    0x1b80: v1b80 = ADD v1b6e, v1b7d(0x4)
    0x1b83: MSTORE v1b80, v1b7c
    0x1b85: v1b85 = MLOAD v1b6b(0x40)
    0x1b88: v1b88(0x1) = CONST 
    0x1b8a: v1b8a(0xa0) = CONST 
    0x1b8c: v1b8c(0x2) = CONST 
    0x1b8e: v1b8e(0x10000000000000000000000000000000000000000) = EXP v1b8c(0x2), v1b8a(0xa0)
    0x1b8f: v1b8f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b8e(0x10000000000000000000000000000000000000000), v1b88(0x1)
    0x1b90: v1b90 = AND v1b8f(0xffffffffffffffffffffffffffffffffffffffff), v1b6a
    0x1b92: v1b92(0x7ccce851) = CONST 
    0x1b98: v1b98(0x24) = CONST 
    0x1b9c: v1b9c = ADD v1b6e, v1b98(0x24)
    0x1b9e: v1b9e(0x20) = CONST 
    0x1ba6: v1ba6(0x0) = SUB v1b6e, v1b85
    0x1ba7: v1ba7(0x24) = ADD v1ba6(0x0), v1b98(0x24)
    0x1ba9: v1ba9(0x0) = CONST 
    0x1bad: v1bad = EXTCODESIZE v1b90
    0x1bae: v1bae = ISZERO v1bad
    0x1bb0: v1bb0 = ISZERO v1bae
    0x1bb1: v1bb1(0x1bb9) = CONST 
    0x1bb4: JUMPI v1bb1(0x1bb9), v1bb0

    Begin block 0x1bb5
    prev=[0x1b67], succ=[]
    =================================
    0x1bb5: v1bb5(0x0) = CONST 
    0x1bb8: REVERT v1bb5(0x0), v1bb5(0x0)

    Begin block 0x1bb9
    prev=[0x1b67], succ=[0x1bc4, 0x1bcd]
    =================================
    0x1bbb: v1bbb = GAS 
    0x1bbc: v1bbc = CALL v1bbb, v1b90, v1ba9(0x0), v1b85, v1ba7(0x24), v1b85, v1b9e(0x20)
    0x1bbd: v1bbd = ISZERO v1bbc
    0x1bbf: v1bbf = ISZERO v1bbd
    0x1bc0: v1bc0(0x1bcd) = CONST 
    0x1bc3: JUMPI v1bc0(0x1bcd), v1bbf

    Begin block 0x1bc4
    prev=[0x1bb9], succ=[]
    =================================
    0x1bc4: v1bc4 = RETURNDATASIZE 
    0x1bc5: v1bc5(0x0) = CONST 
    0x1bc8: RETURNDATACOPY v1bc5(0x0), v1bc5(0x0), v1bc4
    0x1bc9: v1bc9 = RETURNDATASIZE 
    0x1bca: v1bca(0x0) = CONST 
    0x1bcc: REVERT v1bca(0x0), v1bc9

    Begin block 0x1bcd
    prev=[0x1bb9], succ=[0x1bdf, 0x1be3]
    =================================
    0x1bd2: v1bd2(0x40) = CONST 
    0x1bd4: v1bd4 = MLOAD v1bd2(0x40)
    0x1bd5: v1bd5 = RETURNDATASIZE 
    0x1bd6: v1bd6(0x20) = CONST 
    0x1bd9: v1bd9 = LT v1bd5, v1bd6(0x20)
    0x1bda: v1bda = ISZERO v1bd9
    0x1bdb: v1bdb(0x1be3) = CONST 
    0x1bde: JUMPI v1bdb(0x1be3), v1bda

    Begin block 0x1bdf
    prev=[0x1bcd], succ=[]
    =================================
    0x1bdf: v1bdf(0x0) = CONST 
    0x1be2: REVERT v1bdf(0x0), v1bdf(0x0)

    Begin block 0x1be3
    prev=[0x1bcd], succ=[0x1beb, 0x1c28]
    =================================
    0x1be5: v1be5 = MLOAD v1bd4
    0x1be6: v1be6 = ISZERO v1be5
    0x1be7: v1be7(0x1c28) = CONST 
    0x1bea: JUMPI v1be7(0x1c28), v1be6

    Begin block 0x1beb
    prev=[0x1be3], succ=[]
    =================================
    0x1beb: v1beb(0x40) = CONST 
    0x1bee: v1bee = MLOAD v1beb(0x40)
    0x1bef: v1bef(0xe5) = CONST 
    0x1bf1: v1bf1(0x2) = CONST 
    0x1bf3: v1bf3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1bf1(0x2), v1bef(0xe5)
    0x1bf4: v1bf4(0x461bcd) = CONST 
    0x1bf8: v1bf8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1bf4(0x461bcd), v1bf3(0x2000000000000000000000000000000000000000000000000000000000)
    0x1bfa: MSTORE v1bee, v1bf8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1bfb: v1bfb(0x20) = CONST 
    0x1bfd: v1bfd(0x4) = CONST 
    0x1c00: v1c00 = ADD v1bee, v1bfd(0x4)
    0x1c01: MSTORE v1c00, v1bfb(0x20)
    0x1c02: v1c02(0x1c) = CONST 
    0x1c04: v1c04(0x24) = CONST 
    0x1c07: v1c07 = ADD v1bee, v1c04(0x24)
    0x1c08: MSTORE v1c07, v1c02(0x1c)
    0x1c09: v1c09(0x0) = CONST 
    0x1c0c: v1c0c = MLOAD v1c09(0x0)
    0x1c0d: v1c0d(0x20) = CONST 
    0x1c0f: v1c0f(0x4a70) = CONST 
    0x1c17: MSTORE v1c09(0x0), v1c0c
    0x1c18: v1c18(0x44) = CONST 
    0x1c1b: v1c1b = ADD v1bee, v1c18(0x44)
    0x1c1c: MSTORE v1c1b, v554d(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x1c1e: v1c1e = MLOAD v1beb(0x40)
    0x1c22: v1c22(0x0) = SUB v1bee, v1c1e
    0x1c23: v1c23(0x64) = CONST 
    0x1c25: v1c25(0x64) = ADD v1c23(0x64), v1c22(0x0)
    0x1c27: REVERT v1c1e, v1c25(0x64)
    0x554d: v554d(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x1c28
    prev=[0x1be3], succ=[0x1c3b, 0x1c3f]
    =================================
    0x1c29: v1c29(0x1) = CONST 
    0x1c2b: v1c2b = SLOAD v1c29(0x1)
    0x1c2c: v1c2c(0xa0) = CONST 
    0x1c2e: v1c2e(0x2) = CONST 
    0x1c30: v1c30(0x10000000000000000000000000000000000000000) = EXP v1c2e(0x2), v1c2c(0xa0)
    0x1c32: v1c32 = DIV v1c2b, v1c30(0x10000000000000000000000000000000000000000)
    0x1c33: v1c33(0xff) = CONST 
    0x1c35: v1c35 = AND v1c33(0xff), v1c32
    0x1c36: v1c36 = ISZERO v1c35
    0x1c37: v1c37(0x1c3f) = CONST 
    0x1c3a: JUMPI v1c37(0x1c3f), v1c36

    Begin block 0x1c3b
    prev=[0x1c28], succ=[]
    =================================
    0x1c3b: v1c3b(0x0) = CONST 
    0x1c3e: REVERT v1c3b(0x0), v1c3b(0x0)

    Begin block 0x1c3f
    prev=[0x1c28], succ=[0x4361]
    =================================
    0x1c40: v1c40(0x5331) = CONST 
    0x1c45: v1c45 = CALLER 
    0x1c46: v1c46(0x4361) = CONST 
    0x1c49: JUMP v1c46(0x4361)

    Begin block 0x4361
    prev=[0x1c3f], succ=[0x436d]
    =================================
    0x4362: v4362(0x0) = CONST 
    0x4364: v4364(0x436d) = CONST 
    0x4369: v4369(0x32b1) = CONST 
    0x436c: v436c_0 = CALLPRIVATE v4369(0x32b1), v4a3, v1c45, v4364(0x436d)

    Begin block 0x436d
    prev=[0x4361], succ=[0x4378, 0x4408]
    =================================
    0x4372: v4372 = GT v4a6, v436c_0
    0x4373: v4373 = ISZERO v4372
    0x4374: v4374(0x4408) = CONST 
    0x4377: JUMPI v4374(0x4408), v4373

    Begin block 0x4378
    prev=[0x436d], succ=[0x43e7, 0x43eb]
    =================================
    0x4378: v4378(0x2) = CONST 
    0x437a: v437a = SLOAD v4378(0x2)
    0x437b: v437b(0x40) = CONST 
    0x437e: v437e = MLOAD v437b(0x40)
    0x437f: v437f(0xda46098c00000000000000000000000000000000000000000000000000000000) = CONST 
    0x43a1: MSTORE v437e, v437f(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0x43a2: v43a2(0x1) = CONST 
    0x43a4: v43a4(0xa0) = CONST 
    0x43a6: v43a6(0x2) = CONST 
    0x43a8: v43a8(0x10000000000000000000000000000000000000000) = EXP v43a6(0x2), v43a4(0xa0)
    0x43a9: v43a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43a8(0x10000000000000000000000000000000000000000), v43a2(0x1)
    0x43ac: v43ac = AND v43a9(0xffffffffffffffffffffffffffffffffffffffff), v1c45
    0x43ad: v43ad(0x4) = CONST 
    0x43b0: v43b0 = ADD v437e, v43ad(0x4)
    0x43b1: MSTORE v43b0, v43ac
    0x43b4: v43b4 = AND v43a9(0xffffffffffffffffffffffffffffffffffffffff), v4a3
    0x43b5: v43b5(0x24) = CONST 
    0x43b8: v43b8 = ADD v437e, v43b5(0x24)
    0x43b9: MSTORE v43b8, v43b4
    0x43ba: v43ba(0x0) = CONST 
    0x43bc: v43bc(0x44) = CONST 
    0x43bf: v43bf = ADD v437e, v43bc(0x44)
    0x43c2: MSTORE v43bf, v43ba(0x0)
    0x43c4: v43c4 = MLOAD v437b(0x40)
    0x43c6: v43c6 = AND v437a, v43a9(0xffffffffffffffffffffffffffffffffffffffff)
    0x43c8: v43c8(0xda46098c) = CONST 
    0x43ce: v43ce(0x64) = CONST 
    0x43d2: v43d2 = ADD v437e, v43ce(0x64)
    0x43d9: v43d9(0x0) = SUB v437e, v43c4
    0x43da: v43da(0x64) = ADD v43d9(0x0), v43ce(0x64)
    0x43df: v43df = EXTCODESIZE v43c6
    0x43e0: v43e0 = ISZERO v43df
    0x43e2: v43e2 = ISZERO v43e0
    0x43e3: v43e3(0x43eb) = CONST 
    0x43e6: JUMPI v43e3(0x43eb), v43e2

    Begin block 0x43e7
    prev=[0x4378], succ=[]
    =================================
    0x43e7: v43e7(0x0) = CONST 
    0x43ea: REVERT v43e7(0x0), v43e7(0x0)

    Begin block 0x43eb
    prev=[0x4378], succ=[0x43f6, 0x43ff]
    =================================
    0x43ed: v43ed = GAS 
    0x43ee: v43ee = CALL v43ed, v43c6, v43ba(0x0), v43c4, v43da(0x64), v43c4, v43ba(0x0)
    0x43ef: v43ef = ISZERO v43ee
    0x43f1: v43f1 = ISZERO v43ef
    0x43f2: v43f2(0x43ff) = CONST 
    0x43f5: JUMPI v43f2(0x43ff), v43f1

    Begin block 0x43f6
    prev=[0x43eb], succ=[]
    =================================
    0x43f6: v43f6 = RETURNDATASIZE 
    0x43f7: v43f7(0x0) = CONST 
    0x43fa: RETURNDATACOPY v43f7(0x0), v43f7(0x0), v43f6
    0x43fb: v43fb = RETURNDATASIZE 
    0x43fc: v43fc(0x0) = CONST 
    0x43fe: REVERT v43fc(0x0), v43fb

    Begin block 0x43ff
    prev=[0x43eb], succ=[0x4497]
    =================================
    0x4404: v4404(0x4497) = CONST 
    0x4407: JUMP v4404(0x4497)

    Begin block 0x4497
    prev=[0x43ff, 0x4492], succ=[0x44d6]
    =================================
    0x4499: v4499(0x1) = CONST 
    0x449b: v449b(0xa0) = CONST 
    0x449d: v449d(0x2) = CONST 
    0x449f: v449f(0x10000000000000000000000000000000000000000) = EXP v449d(0x2), v449b(0xa0)
    0x44a0: v44a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v449f(0x10000000000000000000000000000000000000000), v4499(0x1)
    0x44a1: v44a1 = AND v44a0(0xffffffffffffffffffffffffffffffffffffffff), v4a3
    0x44a3: v44a3(0x1) = CONST 
    0x44a5: v44a5(0xa0) = CONST 
    0x44a7: v44a7(0x2) = CONST 
    0x44a9: v44a9(0x10000000000000000000000000000000000000000) = EXP v44a7(0x2), v44a5(0xa0)
    0x44aa: v44aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v44a9(0x10000000000000000000000000000000000000000), v44a3(0x1)
    0x44ab: v44ab = AND v44aa(0xffffffffffffffffffffffffffffffffffffffff), v1c45
    0x44ac: v44ac(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x44cd: v44cd(0x44d6) = CONST 
    0x44d2: v44d2(0x32b1) = CONST 
    0x44d5: v44d5_0 = CALLPRIVATE v44d2(0x32b1), v4a3, v1c45, v44cd(0x44d6)

    Begin block 0x44d6
    prev=[0x4497], succ=[0x5331]
    =================================
    0x44d7: v44d7(0x40) = CONST 
    0x44da: v44da = MLOAD v44d7(0x40)
    0x44dd: MSTORE v44da, v44d5_0
    0x44de: v44de = MLOAD v44d7(0x40)
    0x44e2: v44e2(0x0) = SUB v44da, v44de
    0x44e3: v44e3(0x20) = CONST 
    0x44e5: v44e5(0x20) = ADD v44e3(0x20), v44e2(0x0)
    0x44e7: LOG3 v44de, v44e5(0x20), v44ac(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v44ab, v44a1
    0x44ec: JUMP v1c40(0x5331)

    Begin block 0x5331
    prev=[0x44d6], succ=[0x4d18]
    =================================
    0x5333: v5333(0x1) = CONST 
    0x533b: JUMP v495(0x4d18)

    Begin block 0x4d18
    prev=[0x5331], succ=[]
    =================================
    0x4d19: v4d19(0x40) = CONST 
    0x4d1c: v4d1c = MLOAD v4d19(0x40)
    0x4d1e: v4d1e = ISZERO v5333(0x1)
    0x4d1f: v4d1f = ISZERO v4d1e
    0x4d21: MSTORE v4d1c, v4d1f
    0x4d22: v4d22 = MLOAD v4d19(0x40)
    0x4d26: v4d26(0x0) = SUB v4d1c, v4d22
    0x4d27: v4d27(0x20) = CONST 
    0x4d29: v4d29(0x20) = ADD v4d27(0x20), v4d26(0x0)
    0x4d2b: RETURN v4d22, v4d29(0x20)

    Begin block 0x4408
    prev=[0x436d], succ=[0x447a, 0x447e]
    =================================
    0x4409: v4409(0x2) = CONST 
    0x440b: v440b = SLOAD v4409(0x2)
    0x440c: v440c(0x40) = CONST 
    0x440f: v440f = MLOAD v440c(0x40)
    0x4410: v4410(0x97d88cd200000000000000000000000000000000000000000000000000000000) = CONST 
    0x4432: MSTORE v440f, v4410(0x97d88cd200000000000000000000000000000000000000000000000000000000)
    0x4433: v4433(0x1) = CONST 
    0x4435: v4435(0xa0) = CONST 
    0x4437: v4437(0x2) = CONST 
    0x4439: v4439(0x10000000000000000000000000000000000000000) = EXP v4437(0x2), v4435(0xa0)
    0x443a: v443a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4439(0x10000000000000000000000000000000000000000), v4433(0x1)
    0x443d: v443d = AND v443a(0xffffffffffffffffffffffffffffffffffffffff), v1c45
    0x443e: v443e(0x4) = CONST 
    0x4441: v4441 = ADD v440f, v443e(0x4)
    0x4442: MSTORE v4441, v443d
    0x4445: v4445 = AND v443a(0xffffffffffffffffffffffffffffffffffffffff), v4a3
    0x4446: v4446(0x24) = CONST 
    0x4449: v4449 = ADD v440f, v4446(0x24)
    0x444a: MSTORE v4449, v4445
    0x444b: v444b(0x44) = CONST 
    0x444e: v444e = ADD v440f, v444b(0x44)
    0x4451: MSTORE v444e, v4a6
    0x4453: v4453 = MLOAD v440c(0x40)
    0x4457: v4457 = AND v440b, v443a(0xffffffffffffffffffffffffffffffffffffffff)
    0x4459: v4459(0x97d88cd2) = CONST 
    0x445f: v445f(0x64) = CONST 
    0x4463: v4463 = ADD v440f, v445f(0x64)
    0x4465: v4465(0x0) = CONST 
    0x446c: v446c(0x0) = SUB v440f, v4453
    0x446d: v446d(0x64) = ADD v446c(0x0), v445f(0x64)
    0x4472: v4472 = EXTCODESIZE v4457
    0x4473: v4473 = ISZERO v4472
    0x4475: v4475 = ISZERO v4473
    0x4476: v4476(0x447e) = CONST 
    0x4479: JUMPI v4476(0x447e), v4475

    Begin block 0x447a
    prev=[0x4408], succ=[]
    =================================
    0x447a: v447a(0x0) = CONST 
    0x447d: REVERT v447a(0x0), v447a(0x0)

    Begin block 0x447e
    prev=[0x4408], succ=[0x4489, 0x4492]
    =================================
    0x4480: v4480 = GAS 
    0x4481: v4481 = CALL v4480, v4457, v4465(0x0), v4453, v446d(0x64), v4453, v4465(0x0)
    0x4482: v4482 = ISZERO v4481
    0x4484: v4484 = ISZERO v4482
    0x4485: v4485(0x4492) = CONST 
    0x4488: JUMPI v4485(0x4492), v4484

    Begin block 0x4489
    prev=[0x447e], succ=[]
    =================================
    0x4489: v4489 = RETURNDATASIZE 
    0x448a: v448a(0x0) = CONST 
    0x448d: RETURNDATACOPY v448a(0x0), v448a(0x0), v4489
    0x448e: v448e = RETURNDATASIZE 
    0x448f: v448f(0x0) = CONST 
    0x4491: REVERT v448f(0x0), v448e

    Begin block 0x4492
    prev=[0x447e], succ=[0x4497]
    =================================

}

function approveBlacklistedAddressSpender(address)() public {
    Begin block 0x4ab
    prev=[], succ=[0x4b3, 0x4b7]
    =================================
    0x4ac: v4ac = CALLVALUE 
    0x4ae: v4ae = ISZERO v4ac
    0x4af: v4af(0x4b7) = CONST 
    0x4b2: JUMPI v4af(0x4b7), v4ae

    Begin block 0x4b3
    prev=[0x4ab], succ=[]
    =================================
    0x4b3: v4b3(0x0) = CONST 
    0x4b6: REVERT v4b3(0x0), v4b3(0x0)

    Begin block 0x4b7
    prev=[0x4ab], succ=[0x1c55]
    =================================
    0x4b9: v4b9(0x4d4b) = CONST 
    0x4bc: v4bc(0x1) = CONST 
    0x4be: v4be(0xa0) = CONST 
    0x4c0: v4c0(0x2) = CONST 
    0x4c2: v4c2(0x10000000000000000000000000000000000000000) = EXP v4c0(0x2), v4be(0xa0)
    0x4c3: v4c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4c2(0x10000000000000000000000000000000000000000), v4bc(0x1)
    0x4c4: v4c4(0x4) = CONST 
    0x4c6: v4c6 = CALLDATALOAD v4c4(0x4)
    0x4c7: v4c7 = AND v4c6, v4c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x4c8: v4c8(0x1c55) = CONST 
    0x4cb: JUMP v4c8(0x1c55)

    Begin block 0x1c55
    prev=[0x4b7], succ=[0x1ca6, 0x1caa]
    =================================
    0x1c56: v1c56(0x3) = CONST 
    0x1c58: v1c58 = SLOAD v1c56(0x3)
    0x1c59: v1c59(0x40) = CONST 
    0x1c5c: v1c5c = MLOAD v1c59(0x40)
    0x1c5d: v1c5d(0xe0) = CONST 
    0x1c5f: v1c5f(0x2) = CONST 
    0x1c61: v1c61(0x100000000000000000000000000000000000000000000000000000000) = EXP v1c5f(0x2), v1c5d(0xe0)
    0x1c62: v1c62(0x7ccce851) = CONST 
    0x1c67: v1c67(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1c62(0x7ccce851), v1c61(0x100000000000000000000000000000000000000000000000000000000)
    0x1c69: MSTORE v1c5c, v1c67(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1c6a: v1c6a(0x1) = CONST 
    0x1c6c: v1c6c(0xa0) = CONST 
    0x1c6e: v1c6e(0x2) = CONST 
    0x1c70: v1c70(0x10000000000000000000000000000000000000000) = EXP v1c6e(0x2), v1c6c(0xa0)
    0x1c71: v1c71(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c70(0x10000000000000000000000000000000000000000), v1c6a(0x1)
    0x1c74: v1c74 = AND v4c7, v1c71(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c75: v1c75(0x4) = CONST 
    0x1c78: v1c78 = ADD v1c5c, v1c75(0x4)
    0x1c79: MSTORE v1c78, v1c74
    0x1c7b: v1c7b = MLOAD v1c59(0x40)
    0x1c81: v1c81 = AND v1c58, v1c71(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c83: v1c83(0x7ccce851) = CONST 
    0x1c89: v1c89(0x24) = CONST 
    0x1c8d: v1c8d = ADD v1c5c, v1c89(0x24)
    0x1c8f: v1c8f(0x20) = CONST 
    0x1c97: v1c97(0x0) = SUB v1c5c, v1c7b
    0x1c98: v1c98(0x24) = ADD v1c97(0x0), v1c89(0x24)
    0x1c9a: v1c9a(0x0) = CONST 
    0x1c9e: v1c9e = EXTCODESIZE v1c81
    0x1c9f: v1c9f = ISZERO v1c9e
    0x1ca1: v1ca1 = ISZERO v1c9f
    0x1ca2: v1ca2(0x1caa) = CONST 
    0x1ca5: JUMPI v1ca2(0x1caa), v1ca1

    Begin block 0x1ca6
    prev=[0x1c55], succ=[]
    =================================
    0x1ca6: v1ca6(0x0) = CONST 
    0x1ca9: REVERT v1ca6(0x0), v1ca6(0x0)

    Begin block 0x1caa
    prev=[0x1c55], succ=[0x1cb5, 0x1cbe]
    =================================
    0x1cac: v1cac = GAS 
    0x1cad: v1cad = CALL v1cac, v1c81, v1c9a(0x0), v1c7b, v1c98(0x24), v1c7b, v1c8f(0x20)
    0x1cae: v1cae = ISZERO v1cad
    0x1cb0: v1cb0 = ISZERO v1cae
    0x1cb1: v1cb1(0x1cbe) = CONST 
    0x1cb4: JUMPI v1cb1(0x1cbe), v1cb0

    Begin block 0x1cb5
    prev=[0x1caa], succ=[]
    =================================
    0x1cb5: v1cb5 = RETURNDATASIZE 
    0x1cb6: v1cb6(0x0) = CONST 
    0x1cb9: RETURNDATACOPY v1cb6(0x0), v1cb6(0x0), v1cb5
    0x1cba: v1cba = RETURNDATASIZE 
    0x1cbb: v1cbb(0x0) = CONST 
    0x1cbd: REVERT v1cbb(0x0), v1cba

    Begin block 0x1cbe
    prev=[0x1caa], succ=[0x1cd0, 0x1cd4]
    =================================
    0x1cc3: v1cc3(0x40) = CONST 
    0x1cc5: v1cc5 = MLOAD v1cc3(0x40)
    0x1cc6: v1cc6 = RETURNDATASIZE 
    0x1cc7: v1cc7(0x20) = CONST 
    0x1cca: v1cca = LT v1cc6, v1cc7(0x20)
    0x1ccb: v1ccb = ISZERO v1cca
    0x1ccc: v1ccc(0x1cd4) = CONST 
    0x1ccf: JUMPI v1ccc(0x1cd4), v1ccb

    Begin block 0x1cd0
    prev=[0x1cbe], succ=[]
    =================================
    0x1cd0: v1cd0(0x0) = CONST 
    0x1cd3: REVERT v1cd0(0x0), v1cd0(0x0)

    Begin block 0x1cd4
    prev=[0x1cbe], succ=[0x1cdd, 0x1d2c]
    =================================
    0x1cd6: v1cd6 = MLOAD v1cc5
    0x1cd7: v1cd7 = ISZERO v1cd6
    0x1cd8: v1cd8 = ISZERO v1cd7
    0x1cd9: v1cd9(0x1d2c) = CONST 
    0x1cdc: JUMPI v1cd9(0x1d2c), v1cd8

    Begin block 0x1cdd
    prev=[0x1cd4], succ=[]
    =================================
    0x1cdd: v1cdd(0x40) = CONST 
    0x1ce0: v1ce0 = MLOAD v1cdd(0x40)
    0x1ce1: v1ce1(0xe5) = CONST 
    0x1ce3: v1ce3(0x2) = CONST 
    0x1ce5: v1ce5(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1ce3(0x2), v1ce1(0xe5)
    0x1ce6: v1ce6(0x461bcd) = CONST 
    0x1cea: v1cea(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1ce6(0x461bcd), v1ce5(0x2000000000000000000000000000000000000000000000000000000000)
    0x1cec: MSTORE v1ce0, v1cea(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ced: v1ced(0x20) = CONST 
    0x1cef: v1cef(0x4) = CONST 
    0x1cf2: v1cf2 = ADD v1ce0, v1cef(0x4)
    0x1cf3: MSTORE v1cf2, v1ced(0x20)
    0x1cf4: v1cf4(0x18) = CONST 
    0x1cf6: v1cf6(0x24) = CONST 
    0x1cf9: v1cf9 = ADD v1ce0, v1cf6(0x24)
    0x1cfa: MSTORE v1cf9, v1cf4(0x18)
    0x1cfb: v1cfb(0x55736572206d75737420626520626c61636b6c69737465640000000000000000) = CONST 
    0x1d1c: v1d1c(0x44) = CONST 
    0x1d1f: v1d1f = ADD v1ce0, v1d1c(0x44)
    0x1d20: MSTORE v1d1f, v1cfb(0x55736572206d75737420626520626c61636b6c69737465640000000000000000)
    0x1d22: v1d22 = MLOAD v1cdd(0x40)
    0x1d26: v1d26(0x0) = SUB v1ce0, v1d22
    0x1d27: v1d27(0x64) = CONST 
    0x1d29: v1d29(0x64) = ADD v1d27(0x64), v1d26(0x0)
    0x1d2b: REVERT v1d22, v1d29(0x64)

    Begin block 0x1d2c
    prev=[0x1cd4], succ=[0x1d3f, 0x1d43]
    =================================
    0x1d2d: v1d2d(0x1) = CONST 
    0x1d2f: v1d2f = SLOAD v1d2d(0x1)
    0x1d30: v1d30(0xa0) = CONST 
    0x1d32: v1d32(0x2) = CONST 
    0x1d34: v1d34(0x10000000000000000000000000000000000000000) = EXP v1d32(0x2), v1d30(0xa0)
    0x1d36: v1d36 = DIV v1d2f, v1d34(0x10000000000000000000000000000000000000000)
    0x1d37: v1d37(0xff) = CONST 
    0x1d39: v1d39 = AND v1d37(0xff), v1d36
    0x1d3a: v1d3a = ISZERO v1d39
    0x1d3b: v1d3b(0x1d43) = CONST 
    0x1d3e: JUMPI v1d3b(0x1d43), v1d3a

    Begin block 0x1d3f
    prev=[0x1d2c], succ=[]
    =================================
    0x1d3f: v1d3f(0x0) = CONST 
    0x1d42: REVERT v1d3f(0x0), v1d3f(0x0)

    Begin block 0x1d43
    prev=[0x1d2c], succ=[0x1dce, 0x1dd2]
    =================================
    0x1d44: v1d44(0x3) = CONST 
    0x1d46: v1d46 = SLOAD v1d44(0x3)
    0x1d47: v1d47(0x40) = CONST 
    0x1d4a: v1d4a = MLOAD v1d47(0x40)
    0x1d4b: v1d4b(0x14db6d5800000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d6d: MSTORE v1d4a, v1d4b(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1d6e: v1d6e = CALLER 
    0x1d6f: v1d6f(0x4) = CONST 
    0x1d72: v1d72 = ADD v1d4a, v1d6f(0x4)
    0x1d73: MSTORE v1d72, v1d6e
    0x1d74: v1d74(0x0) = CONST 
    0x1d77: v1d77 = CALLDATALOAD v1d74(0x0)
    0x1d78: v1d78(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d95: v1d95(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1d78(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1d96: v1d96 = AND v1d95(0xffffffff00000000000000000000000000000000000000000000000000000000), v1d77
    0x1d97: v1d97(0x24) = CONST 
    0x1d9a: v1d9a = ADD v1d4a, v1d97(0x24)
    0x1d9b: MSTORE v1d9a, v1d96
    0x1d9d: v1d9d = MLOAD v1d47(0x40)
    0x1d9e: v1d9e(0x1) = CONST 
    0x1da0: v1da0(0xa0) = CONST 
    0x1da2: v1da2(0x2) = CONST 
    0x1da4: v1da4(0x10000000000000000000000000000000000000000) = EXP v1da2(0x2), v1da0(0xa0)
    0x1da5: v1da5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1da4(0x10000000000000000000000000000000000000000), v1d9e(0x1)
    0x1da8: v1da8 = AND v1d46, v1da5(0xffffffffffffffffffffffffffffffffffffffff)
    0x1daa: v1daa(0x14db6d58) = CONST 
    0x1db0: v1db0(0x44) = CONST 
    0x1db4: v1db4 = ADD v1d4a, v1db0(0x44)
    0x1db6: v1db6(0x20) = CONST 
    0x1dbd: v1dbd(0x0) = SUB v1d4a, v1d9d
    0x1dc0: v1dc0(0x44) = ADD v1db0(0x44), v1dbd(0x0)
    0x1dc6: v1dc6 = EXTCODESIZE v1da8
    0x1dc7: v1dc7 = ISZERO v1dc6
    0x1dc9: v1dc9 = ISZERO v1dc7
    0x1dca: v1dca(0x1dd2) = CONST 
    0x1dcd: JUMPI v1dca(0x1dd2), v1dc9

    Begin block 0x1dce
    prev=[0x1d43], succ=[]
    =================================
    0x1dce: v1dce(0x0) = CONST 
    0x1dd1: REVERT v1dce(0x0), v1dce(0x0)

    Begin block 0x1dd2
    prev=[0x1d43], succ=[0x1ddd, 0x1de6]
    =================================
    0x1dd4: v1dd4 = GAS 
    0x1dd5: v1dd5 = CALL v1dd4, v1da8, v1d74(0x0), v1d9d, v1dc0(0x44), v1d9d, v1db6(0x20)
    0x1dd6: v1dd6 = ISZERO v1dd5
    0x1dd8: v1dd8 = ISZERO v1dd6
    0x1dd9: v1dd9(0x1de6) = CONST 
    0x1ddc: JUMPI v1dd9(0x1de6), v1dd8

    Begin block 0x1ddd
    prev=[0x1dd2], succ=[]
    =================================
    0x1ddd: v1ddd = RETURNDATASIZE 
    0x1dde: v1dde(0x0) = CONST 
    0x1de1: RETURNDATACOPY v1dde(0x0), v1dde(0x0), v1ddd
    0x1de2: v1de2 = RETURNDATASIZE 
    0x1de3: v1de3(0x0) = CONST 
    0x1de5: REVERT v1de3(0x0), v1de2

    Begin block 0x1de6
    prev=[0x1dd2], succ=[0x1df8, 0x1dfc]
    =================================
    0x1deb: v1deb(0x40) = CONST 
    0x1ded: v1ded = MLOAD v1deb(0x40)
    0x1dee: v1dee = RETURNDATASIZE 
    0x1def: v1def(0x20) = CONST 
    0x1df2: v1df2 = LT v1dee, v1def(0x20)
    0x1df3: v1df3 = ISZERO v1df2
    0x1df4: v1df4(0x1dfc) = CONST 
    0x1df7: JUMPI v1df4(0x1dfc), v1df3

    Begin block 0x1df8
    prev=[0x1de6], succ=[]
    =================================
    0x1df8: v1df8(0x0) = CONST 
    0x1dfb: REVERT v1df8(0x0), v1df8(0x0)

    Begin block 0x1dfc
    prev=[0x1de6], succ=[0x1e05, 0x1e7a]
    =================================
    0x1dfe: v1dfe = MLOAD v1ded
    0x1dff: v1dff = ISZERO v1dfe
    0x1e00: v1e00 = ISZERO v1dff
    0x1e01: v1e01(0x1e7a) = CONST 
    0x1e04: JUMPI v1e01(0x1e7a), v1e00

    Begin block 0x1e05
    prev=[0x1dfc], succ=[]
    =================================
    0x1e05: v1e05(0x40) = CONST 
    0x1e08: v1e08 = MLOAD v1e05(0x40)
    0x1e09: v1e09(0xe5) = CONST 
    0x1e0b: v1e0b(0x2) = CONST 
    0x1e0d: v1e0d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1e0b(0x2), v1e09(0xe5)
    0x1e0e: v1e0e(0x461bcd) = CONST 
    0x1e12: v1e12(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1e0e(0x461bcd), v1e0d(0x2000000000000000000000000000000000000000000000000000000000)
    0x1e14: MSTORE v1e08, v1e12(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e15: v1e15(0x20) = CONST 
    0x1e17: v1e17(0x4) = CONST 
    0x1e1a: v1e1a = ADD v1e08, v1e17(0x4)
    0x1e1b: MSTORE v1e1a, v1e15(0x20)
    0x1e1c: v1e1c(0x31) = CONST 
    0x1e1e: v1e1e(0x24) = CONST 
    0x1e21: v1e21 = ADD v1e08, v1e1e(0x24)
    0x1e22: MSTORE v1e21, v1e1c(0x31)
    0x1e23: v1e23(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x1e44: v1e44(0x44) = CONST 
    0x1e47: v1e47 = ADD v1e08, v1e44(0x44)
    0x1e48: MSTORE v1e47, v1e23(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x1e49: v1e49(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 
    0x1e6a: v1e6a(0x64) = CONST 
    0x1e6d: v1e6d = ADD v1e08, v1e6a(0x64)
    0x1e6e: MSTORE v1e6d, v1e49(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x1e70: v1e70 = MLOAD v1e05(0x40)
    0x1e74: v1e74(0x0) = SUB v1e08, v1e70
    0x1e75: v1e75(0x84) = CONST 
    0x1e77: v1e77(0x84) = ADD v1e75(0x84), v1e74(0x0)
    0x1e79: REVERT v1e70, v1e77(0x84)

    Begin block 0x1e7a
    prev=[0x1dfc], succ=[0x1e96]
    =================================
    0x1e7b: v1e7b(0x2) = CONST 
    0x1e7d: v1e7d = SLOAD v1e7b(0x2)
    0x1e7e: v1e7e(0x1) = CONST 
    0x1e80: v1e80(0xa0) = CONST 
    0x1e82: v1e82(0x2) = CONST 
    0x1e84: v1e84(0x10000000000000000000000000000000000000000) = EXP v1e82(0x2), v1e80(0xa0)
    0x1e85: v1e85(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e84(0x10000000000000000000000000000000000000000), v1e7e(0x1)
    0x1e86: v1e86 = AND v1e85(0xffffffffffffffffffffffffffffffffffffffff), v1e7d
    0x1e87: v1e87(0xda46098c) = CONST 
    0x1e8d: v1e8d = CALLER 
    0x1e8e: v1e8e(0x1e96) = CONST 
    0x1e92: v1e92(0x206a) = CONST 
    0x1e95: v1e95_0 = CALLPRIVATE v1e92(0x206a), v4c7, v1e8e(0x1e96)

    Begin block 0x1e96
    prev=[0x1e7a], succ=[0x1ee5, 0x1ee9]
    =================================
    0x1e97: v1e97(0x40) = CONST 
    0x1e9a: v1e9a = MLOAD v1e97(0x40)
    0x1e9b: v1e9b(0xe0) = CONST 
    0x1e9d: v1e9d(0x2) = CONST 
    0x1e9f: v1e9f(0x100000000000000000000000000000000000000000000000000000000) = EXP v1e9d(0x2), v1e9b(0xe0)
    0x1ea0: v1ea0(0xffffffff) = CONST 
    0x1ea6: v1ea6(0xda46098c) = AND v1e87(0xda46098c), v1ea0(0xffffffff)
    0x1ea7: v1ea7(0xda46098c00000000000000000000000000000000000000000000000000000000) = MUL v1ea6(0xda46098c), v1e9f(0x100000000000000000000000000000000000000000000000000000000)
    0x1ea9: MSTORE v1e9a, v1ea7(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0x1eaa: v1eaa(0x1) = CONST 
    0x1eac: v1eac(0xa0) = CONST 
    0x1eae: v1eae(0x2) = CONST 
    0x1eb0: v1eb0(0x10000000000000000000000000000000000000000) = EXP v1eae(0x2), v1eac(0xa0)
    0x1eb1: v1eb1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1eb0(0x10000000000000000000000000000000000000000), v1eaa(0x1)
    0x1eb4: v1eb4 = AND v1eb1(0xffffffffffffffffffffffffffffffffffffffff), v4c7
    0x1eb5: v1eb5(0x4) = CONST 
    0x1eb8: v1eb8 = ADD v1e9a, v1eb5(0x4)
    0x1eb9: MSTORE v1eb8, v1eb4
    0x1ebd: v1ebd = AND v1eb1(0xffffffffffffffffffffffffffffffffffffffff), v1e8d
    0x1ebe: v1ebe(0x24) = CONST 
    0x1ec1: v1ec1 = ADD v1e9a, v1ebe(0x24)
    0x1ec2: MSTORE v1ec1, v1ebd
    0x1ec3: v1ec3(0x44) = CONST 
    0x1ec6: v1ec6 = ADD v1e9a, v1ec3(0x44)
    0x1ec7: MSTORE v1ec6, v1e95_0
    0x1ec9: v1ec9 = MLOAD v1e97(0x40)
    0x1eca: v1eca(0x64) = CONST 
    0x1ece: v1ece = ADD v1e9a, v1eca(0x64)
    0x1ed0: v1ed0(0x0) = CONST 
    0x1ed7: v1ed7(0x0) = SUB v1e9a, v1ec9
    0x1ed8: v1ed8(0x64) = ADD v1ed7(0x0), v1eca(0x64)
    0x1edd: v1edd = EXTCODESIZE v1e86
    0x1ede: v1ede = ISZERO v1edd
    0x1ee0: v1ee0 = ISZERO v1ede
    0x1ee1: v1ee1(0x1ee9) = CONST 
    0x1ee4: JUMPI v1ee1(0x1ee9), v1ee0

    Begin block 0x1ee5
    prev=[0x1e96], succ=[]
    =================================
    0x1ee5: v1ee5(0x0) = CONST 
    0x1ee8: REVERT v1ee5(0x0), v1ee5(0x0)

    Begin block 0x1ee9
    prev=[0x1e96], succ=[0x1ef4, 0x1efd]
    =================================
    0x1eeb: v1eeb = GAS 
    0x1eec: v1eec = CALL v1eeb, v1e86, v1ed0(0x0), v1ec9, v1ed8(0x64), v1ec9, v1ed0(0x0)
    0x1eed: v1eed = ISZERO v1eec
    0x1eef: v1eef = ISZERO v1eed
    0x1ef0: v1ef0(0x1efd) = CONST 
    0x1ef3: JUMPI v1ef0(0x1efd), v1eef

    Begin block 0x1ef4
    prev=[0x1ee9], succ=[]
    =================================
    0x1ef4: v1ef4 = RETURNDATASIZE 
    0x1ef5: v1ef5(0x0) = CONST 
    0x1ef8: RETURNDATACOPY v1ef5(0x0), v1ef5(0x0), v1ef4
    0x1ef9: v1ef9 = RETURNDATASIZE 
    0x1efa: v1efa(0x0) = CONST 
    0x1efc: REVERT v1efa(0x0), v1ef9

    Begin block 0x1efd
    prev=[0x1ee9], succ=[0x1f37]
    =================================
    0x1eff: v1eff = CALLER 
    0x1f04: v1f04(0x1) = CONST 
    0x1f06: v1f06(0xa0) = CONST 
    0x1f08: v1f08(0x2) = CONST 
    0x1f0a: v1f0a(0x10000000000000000000000000000000000000000) = EXP v1f08(0x2), v1f06(0xa0)
    0x1f0b: v1f0b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f0a(0x10000000000000000000000000000000000000000), v1f04(0x1)
    0x1f0d: v1f0d = AND v4c7, v1f0b(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f0e: v1f0e(0x3b1ffca3903932aa264fbb5b7b381746e2b7b61c9c5a6024bad48d23f958a6c2) = CONST 
    0x1f2f: v1f2f(0x1f37) = CONST 
    0x1f33: v1f33(0x206a) = CONST 
    0x1f36: v1f36_0 = CALLPRIVATE v1f33(0x206a), v4c7, v1f2f(0x1f37)

    Begin block 0x1f37
    prev=[0x1efd], succ=[0x4d4b]
    =================================
    0x1f38: v1f38(0x40) = CONST 
    0x1f3b: v1f3b = MLOAD v1f38(0x40)
    0x1f3e: MSTORE v1f3b, v1f36_0
    0x1f3f: v1f3f = MLOAD v1f38(0x40)
    0x1f43: v1f43(0x0) = SUB v1f3b, v1f3f
    0x1f44: v1f44(0x20) = CONST 
    0x1f46: v1f46(0x20) = ADD v1f44(0x20), v1f43(0x0)
    0x1f48: LOG3 v1f3f, v1f46(0x20), v1f0e(0x3b1ffca3903932aa264fbb5b7b381746e2b7b61c9c5a6024bad48d23f958a6c2), v1f0d, v1eff
    0x1f4b: JUMP v4b9(0x4d4b)

    Begin block 0x4d4b
    prev=[0x1f37], succ=[]
    =================================
    0x4d4c: STOP 

}

function replayNonce(address)() public {
    Begin block 0x4cc
    prev=[], succ=[0x4d4, 0x4d8]
    =================================
    0x4cd: v4cd = CALLVALUE 
    0x4cf: v4cf = ISZERO v4cd
    0x4d0: v4d0(0x4d8) = CONST 
    0x4d3: JUMPI v4d0(0x4d8), v4cf

    Begin block 0x4d4
    prev=[0x4cc], succ=[]
    =================================
    0x4d4: v4d4(0x0) = CONST 
    0x4d7: REVERT v4d4(0x0), v4d4(0x0)

    Begin block 0x4d8
    prev=[0x4cc], succ=[0x1f4c]
    =================================
    0x4da: v4da(0x4d6c) = CONST 
    0x4dd: v4dd(0x1) = CONST 
    0x4df: v4df(0xa0) = CONST 
    0x4e1: v4e1(0x2) = CONST 
    0x4e3: v4e3(0x10000000000000000000000000000000000000000) = EXP v4e1(0x2), v4df(0xa0)
    0x4e4: v4e4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e3(0x10000000000000000000000000000000000000000), v4dd(0x1)
    0x4e5: v4e5(0x4) = CONST 
    0x4e7: v4e7 = CALLDATALOAD v4e5(0x4)
    0x4e8: v4e8 = AND v4e7, v4e4(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e9: v4e9(0x1f4c) = CONST 
    0x4ec: JUMP v4e9(0x1f4c)

    Begin block 0x1f4c
    prev=[0x4d8], succ=[0x4d6c]
    =================================
    0x1f4d: v1f4d(0x5) = CONST 
    0x1f4f: v1f4f(0x20) = CONST 
    0x1f51: MSTORE v1f4f(0x20), v1f4d(0x5)
    0x1f52: v1f52(0x0) = CONST 
    0x1f56: MSTORE v1f52(0x0), v4e8
    0x1f57: v1f57(0x40) = CONST 
    0x1f5a: v1f5a = SHA3 v1f52(0x0), v1f57(0x40)
    0x1f5b: v1f5b = SLOAD v1f5a
    0x1f5d: JUMP v4da(0x4d6c)

    Begin block 0x4d6c
    prev=[0x1f4c], succ=[]
    =================================
    0x4d6d: v4d6d(0x40) = CONST 
    0x4d70: v4d70 = MLOAD v4d6d(0x40)
    0x4d73: MSTORE v4d70, v1f5b
    0x4d74: v4d74 = MLOAD v4d6d(0x40)
    0x4d78: v4d78(0x0) = SUB v4d70, v4d74
    0x4d79: v4d79(0x20) = CONST 
    0x4d7b: v4d7b(0x20) = ADD v4d79(0x20), v4d78(0x0)
    0x4d7d: RETURN v4d74, v4d7b(0x20)

}

function removeFee(address)() public {
    Begin block 0x4ed
    prev=[], succ=[0x4f5, 0x4f9]
    =================================
    0x4ee: v4ee = CALLVALUE 
    0x4f0: v4f0 = ISZERO v4ee
    0x4f1: v4f1(0x4f9) = CONST 
    0x4f4: JUMPI v4f1(0x4f9), v4f0

    Begin block 0x4f5
    prev=[0x4ed], succ=[]
    =================================
    0x4f5: v4f5(0x0) = CONST 
    0x4f8: REVERT v4f5(0x0), v4f5(0x0)

    Begin block 0x4f9
    prev=[0x4ed], succ=[0x1f5eB0x4f9]
    =================================
    0x4fb: v4fb(0x4d9d) = CONST 
    0x4fe: v4fe(0x1) = CONST 
    0x500: v500(0xa0) = CONST 
    0x502: v502(0x2) = CONST 
    0x504: v504(0x10000000000000000000000000000000000000000) = EXP v502(0x2), v500(0xa0)
    0x505: v505(0xffffffffffffffffffffffffffffffffffffffff) = SUB v504(0x10000000000000000000000000000000000000000), v4fe(0x1)
    0x506: v506(0x4) = CONST 
    0x508: v508 = CALLDATALOAD v506(0x4)
    0x509: v509 = AND v508, v505(0xffffffffffffffffffffffffffffffffffffffff)
    0x50a: v50a(0x1f5e) = CONST 
    0x50d: JUMP v50a(0x1f5e), v509, v4fb(0x4d9d)

    Begin block 0x1f5eB0x4f9
    prev=[0x4f9], succ=[0x1f71B0x4f9, 0x1f75B0x4f9]
    =================================
    0x1f5fS0x4f9: v1f5fV4f9(0x0) = CONST 
    0x1f61S0x4f9: v1f61V4f9 = SLOAD v1f5fV4f9(0x0)
    0x1f62S0x4f9: v1f62V4f9(0x1) = CONST 
    0x1f64S0x4f9: v1f64V4f9(0xa0) = CONST 
    0x1f66S0x4f9: v1f66V4f9(0x2) = CONST 
    0x1f68S0x4f9: v1f68V4f9(0x10000000000000000000000000000000000000000) = EXP v1f66V4f9(0x2), v1f64V4f9(0xa0)
    0x1f69S0x4f9: v1f69V4f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f68V4f9(0x10000000000000000000000000000000000000000), v1f62V4f9(0x1)
    0x1f6aS0x4f9: v1f6aV4f9 = AND v1f69V4f9(0xffffffffffffffffffffffffffffffffffffffff), v1f61V4f9
    0x1f6bS0x4f9: v1f6bV4f9 = CALLER 
    0x1f6cS0x4f9: v1f6cV4f9 = EQ v1f6bV4f9, v1f6aV4f9
    0x1f6dS0x4f9: v1f6dV4f9(0x1f75) = CONST 
    0x1f70S0x4f9: JUMPI v1f6dV4f9(0x1f75), v1f6cV4f9

    Begin block 0x1f71B0x4f9
    prev=[0x1f5eB0x4f9], succ=[]
    =================================
    0x1f71S0x4f9: v1f71V4f9(0x0) = CONST 
    0x1f74S0x4f9: REVERT v1f71V4f9(0x0), v1f71V4f9(0x0)

    Begin block 0x1f75B0x4f9
    prev=[0x1f5eB0x4f9], succ=[0x1f88B0x4f9, 0x1f8cB0x4f9]
    =================================
    0x1f76S0x4f9: v1f76V4f9(0x1) = CONST 
    0x1f78S0x4f9: v1f78V4f9 = SLOAD v1f76V4f9(0x1)
    0x1f79S0x4f9: v1f79V4f9(0xa0) = CONST 
    0x1f7bS0x4f9: v1f7bV4f9(0x2) = CONST 
    0x1f7dS0x4f9: v1f7dV4f9(0x10000000000000000000000000000000000000000) = EXP v1f7bV4f9(0x2), v1f79V4f9(0xa0)
    0x1f7fS0x4f9: v1f7fV4f9 = DIV v1f78V4f9, v1f7dV4f9(0x10000000000000000000000000000000000000000)
    0x1f80S0x4f9: v1f80V4f9(0xff) = CONST 
    0x1f82S0x4f9: v1f82V4f9 = AND v1f80V4f9(0xff), v1f7fV4f9
    0x1f83S0x4f9: v1f83V4f9 = ISZERO v1f82V4f9
    0x1f84S0x4f9: v1f84V4f9(0x1f8c) = CONST 
    0x1f87S0x4f9: JUMPI v1f84V4f9(0x1f8c), v1f83V4f9

    Begin block 0x1f88B0x4f9
    prev=[0x1f75B0x4f9], succ=[]
    =================================
    0x1f88S0x4f9: v1f88V4f9(0x0) = CONST 
    0x1f8bS0x4f9: REVERT v1f88V4f9(0x0), v1f88V4f9(0x0)

    Begin block 0x1f8cB0x4f9
    prev=[0x1f75B0x4f9], succ=[0x1f95B0x4f9]
    =================================
    0x1f8dS0x4f9: v1f8dV4f9(0x1f95) = CONST 
    0x1f91S0x4f9: v1f91V4f9(0x162d) = CONST 
    0x1f94S0x4f9: v1f94_0V4f9 = CALLPRIVATE v1f91V4f9(0x162d), v509, v1f8dV4f9(0x1f95)

    Begin block 0x1f95B0x4f9
    prev=[0x1f8cB0x4f9], succ=[0x1f9cB0x4f9, 0x1fffB0x4f9]
    =================================
    0x1f96S0x4f9: v1f96V4f9 = ISZERO v1f94_0V4f9
    0x1f97S0x4f9: v1f97V4f9 = ISZERO v1f96V4f9
    0x1f98S0x4f9: v1f98V4f9(0x1fff) = CONST 
    0x1f9bS0x4f9: JUMPI v1f98V4f9(0x1fff), v1f97V4f9

    Begin block 0x1f9cB0x4f9
    prev=[0x1f95B0x4f9], succ=[]
    =================================
    0x1f9cS0x4f9: v1f9cV4f9(0x40) = CONST 
    0x1f9fS0x4f9: v1f9fV4f9 = MLOAD v1f9cV4f9(0x40)
    0x1fa0S0x4f9: v1fa0V4f9(0xe5) = CONST 
    0x1fa2S0x4f9: v1fa2V4f9(0x2) = CONST 
    0x1fa4S0x4f9: v1fa4V4f9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1fa2V4f9(0x2), v1fa0V4f9(0xe5)
    0x1fa5S0x4f9: v1fa5V4f9(0x461bcd) = CONST 
    0x1fa9S0x4f9: v1fa9V4f9(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1fa5V4f9(0x461bcd), v1fa4V4f9(0x2000000000000000000000000000000000000000000000000000000000)
    0x1fabS0x4f9: MSTORE v1f9fV4f9, v1fa9V4f9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1facS0x4f9: v1facV4f9(0x20) = CONST 
    0x1faeS0x4f9: v1faeV4f9(0x4) = CONST 
    0x1fb1S0x4f9: v1fb1V4f9 = ADD v1f9fV4f9, v1faeV4f9(0x4)
    0x1fb2S0x4f9: MSTORE v1fb1V4f9, v1facV4f9(0x20)
    0x1fb3S0x4f9: v1fb3V4f9(0x3e) = CONST 
    0x1fb5S0x4f9: v1fb5V4f9(0x24) = CONST 
    0x1fb8S0x4f9: v1fb8V4f9 = ADD v1f9fV4f9, v1fb5V4f9(0x24)
    0x1fb9S0x4f9: MSTORE v1fb8V4f9, v1fb3V4f9(0x3e)
    0x1fbaS0x4f9: v1fbaV4f9(0x0) = CONST 
    0x1fbdS0x4f9: v1fbdV4f9 = MLOAD v1fbaV4f9(0x0)
    0x1fbeS0x4f9: v1fbeV4f9(0x20) = CONST 
    0x1fc0S0x4f9: v1fc0V4f9(0x4a50) = CONST 
    0x1fc8S0x4f9: MSTORE v1fbaV4f9(0x0), v1fbdV4f9
    0x1fc9S0x4f9: v1fc9V4f9(0x44) = CONST 
    0x1fccS0x4f9: v1fccV4f9 = ADD v1f9fV4f9, v1fc9V4f9(0x44)
    0x1fcdS0x4f9: MSTORE v1fccV4f9, v5552V4f9(0x537461626c65636f696e206d7573742062652077686974656c69737465642070)
    0x1fceS0x4f9: v1fceV4f9(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000) = CONST 
    0x1fefS0x4f9: v1fefV4f9(0x64) = CONST 
    0x1ff2S0x4f9: v1ff2V4f9 = ADD v1f9fV4f9, v1fefV4f9(0x64)
    0x1ff3S0x4f9: MSTORE v1ff2V4f9, v1fceV4f9(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000)
    0x1ff5S0x4f9: v1ff5V4f9 = MLOAD v1f9cV4f9(0x40)
    0x1ff9S0x4f9: v1ff9V4f9(0x0) = SUB v1f9fV4f9, v1ff5V4f9
    0x1ffaS0x4f9: v1ffaV4f9(0x84) = CONST 
    0x1ffcS0x4f9: v1ffcV4f9(0x84) = ADD v1ffaV4f9(0x84), v1ff9V4f9(0x0)
    0x1ffeS0x4f9: REVERT v1ff5V4f9, v1ffcV4f9(0x84)
    0x5552S0x4f9: v5552V4f9(0x537461626c65636f696e206d7573742062652077686974656c69737465642070) = CONST 

    Begin block 0x1fffB0x4f9
    prev=[0x1f95B0x4f9], succ=[0x2066B0x4f9, 0x11fc0x1f5eB0x4f9]
    =================================
    0x2000S0x4f9: v2000V4f9(0x4) = CONST 
    0x2003S0x4f9: v2003V4f9 = SLOAD v2000V4f9(0x4)
    0x2004S0x4f9: v2004V4f9(0x40) = CONST 
    0x2007S0x4f9: v2007V4f9 = MLOAD v2004V4f9(0x40)
    0x2008S0x4f9: v2008V4f9(0x6ad2661100000000000000000000000000000000000000000000000000000000) = CONST 
    0x202aS0x4f9: MSTORE v2007V4f9, v2008V4f9(0x6ad2661100000000000000000000000000000000000000000000000000000000)
    0x202bS0x4f9: v202bV4f9(0x1) = CONST 
    0x202dS0x4f9: v202dV4f9(0xa0) = CONST 
    0x202fS0x4f9: v202fV4f9(0x2) = CONST 
    0x2031S0x4f9: v2031V4f9(0x10000000000000000000000000000000000000000) = EXP v202fV4f9(0x2), v202dV4f9(0xa0)
    0x2032S0x4f9: v2032V4f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2031V4f9(0x10000000000000000000000000000000000000000), v202bV4f9(0x1)
    0x2035S0x4f9: v2035V4f9 = AND v2032V4f9(0xffffffffffffffffffffffffffffffffffffffff), v509
    0x2038S0x4f9: v2038V4f9 = ADD v2007V4f9, v2000V4f9(0x4)
    0x203cS0x4f9: MSTORE v2038V4f9, v2035V4f9
    0x203eS0x4f9: v203eV4f9 = MLOAD v2004V4f9(0x40)
    0x2042S0x4f9: v2042V4f9 = AND v2003V4f9, v2032V4f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2044S0x4f9: v2044V4f9(0x6ad26611) = CONST 
    0x204aS0x4f9: v204aV4f9(0x24) = CONST 
    0x204eS0x4f9: v204eV4f9 = ADD v2007V4f9, v204aV4f9(0x24)
    0x2050S0x4f9: v2050V4f9(0x0) = CONST 
    0x2058S0x4f9: v2058V4f9(0x0) = SUB v2007V4f9, v203eV4f9
    0x2059S0x4f9: v2059V4f9(0x24) = ADD v2058V4f9(0x0), v204aV4f9(0x24)
    0x205eS0x4f9: v205eV4f9 = EXTCODESIZE v2042V4f9
    0x205fS0x4f9: v205fV4f9 = ISZERO v205eV4f9
    0x2061S0x4f9: v2061V4f9 = ISZERO v205fV4f9
    0x2062S0x4f9: v2062V4f9(0x11fc) = CONST 
    0x2065S0x4f9: JUMPI v2062V4f9(0x11fc), v2061V4f9

    Begin block 0x2066B0x4f9
    prev=[0x1fffB0x4f9], succ=[]
    =================================
    0x2066S0x4f9: v2066V4f9(0x0) = CONST 
    0x2069S0x4f9: REVERT v2066V4f9(0x0), v2066V4f9(0x0)

    Begin block 0x11fc0x1f5eB0x4f9
    prev=[0x1fffB0x4f9], succ=[0x12070x1f5eB0x4f9, 0x12100x1f5eB0x4f9]
    =================================
    0x11fe0x1f5eS0x4f9: v1f5e11feV4f9 = GAS 
    0x11ff0x1f5eS0x4f9: v1f5e11ffV4f9 = CALL v1f5e11feV4f9, v2042V4f9, v2050V4f9(0x0), v203eV4f9, v2059V4f9(0x24), v203eV4f9, v2050V4f9(0x0)
    0x12000x1f5eS0x4f9: v1f5e1200V4f9 = ISZERO v1f5e11ffV4f9
    0x12020x1f5eS0x4f9: v1f5e1202V4f9 = ISZERO v1f5e1200V4f9
    0x12030x1f5eS0x4f9: v1f5e1203V4f9(0x1210) = CONST 
    0x12060x1f5eS0x4f9: JUMPI v1f5e1203V4f9(0x1210), v1f5e1202V4f9

    Begin block 0x12070x1f5eB0x4f9
    prev=[0x11fc0x1f5eB0x4f9], succ=[]
    =================================
    0x12070x1f5eS0x4f9: v1f5e1207V4f9 = RETURNDATASIZE 
    0x12080x1f5eS0x4f9: v1f5e1208V4f9(0x0) = CONST 
    0x120b0x1f5eS0x4f9: RETURNDATACOPY v1f5e1208V4f9(0x0), v1f5e1208V4f9(0x0), v1f5e1207V4f9
    0x120c0x1f5eS0x4f9: v1f5e120cV4f9 = RETURNDATASIZE 
    0x120d0x1f5eS0x4f9: v1f5e120dV4f9(0x0) = CONST 
    0x120f0x1f5eS0x4f9: REVERT v1f5e120dV4f9(0x0), v1f5e120cV4f9

    Begin block 0x12100x1f5eB0x4f9
    prev=[0x11fc0x1f5eB0x4f9], succ=[0x4d9d]
    =================================
    0x12160x1f5eS0x4f9: JUMP v4fb(0x4d9d)

    Begin block 0x4d9d
    prev=[0x12100x1f5eB0x4f9], succ=[]
    =================================
    0x4d9e: STOP 

}

function balanceOf(address)() public {
    Begin block 0x50e
    prev=[], succ=[0x516, 0x51a]
    =================================
    0x50f: v50f = CALLVALUE 
    0x511: v511 = ISZERO v50f
    0x512: v512(0x51a) = CONST 
    0x515: JUMPI v512(0x51a), v511

    Begin block 0x516
    prev=[0x50e], succ=[]
    =================================
    0x516: v516(0x0) = CONST 
    0x519: REVERT v516(0x0), v516(0x0)

    Begin block 0x51a
    prev=[0x50e], succ=[0x4dbe]
    =================================
    0x51c: v51c(0x4dbe) = CONST 
    0x51f: v51f(0x1) = CONST 
    0x521: v521(0xa0) = CONST 
    0x523: v523(0x2) = CONST 
    0x525: v525(0x10000000000000000000000000000000000000000) = EXP v523(0x2), v521(0xa0)
    0x526: v526(0xffffffffffffffffffffffffffffffffffffffff) = SUB v525(0x10000000000000000000000000000000000000000), v51f(0x1)
    0x527: v527(0x4) = CONST 
    0x529: v529 = CALLDATALOAD v527(0x4)
    0x52a: v52a = AND v529, v526(0xffffffffffffffffffffffffffffffffffffffff)
    0x52b: v52b(0x206a) = CONST 
    0x52e: v52e_0 = CALLPRIVATE v52b(0x206a), v52a, v51c(0x4dbe)

    Begin block 0x4dbe
    prev=[0x51a], succ=[]
    =================================
    0x4dbf: v4dbf(0x40) = CONST 
    0x4dc2: v4dc2 = MLOAD v4dbf(0x40)
    0x4dc5: MSTORE v4dc2, v52e_0
    0x4dc6: v4dc6 = MLOAD v4dbf(0x40)
    0x4dca: v4dca(0x0) = SUB v4dc2, v4dc6
    0x4dcb: v4dcb(0x20) = CONST 
    0x4dcd: v4dcd(0x20) = ADD v4dcb(0x20), v4dca(0x0)
    0x4dcf: RETURN v4dc6, v4dcd(0x20)

}

function metaIncreaseApproval(address,uint256,bytes,uint256,uint256)() public {
    Begin block 0x52f
    prev=[], succ=[0x537, 0x53b]
    =================================
    0x530: v530 = CALLVALUE 
    0x532: v532 = ISZERO v530
    0x533: v533(0x53b) = CONST 
    0x536: JUMPI v533(0x53b), v532

    Begin block 0x537
    prev=[0x52f], succ=[]
    =================================
    0x537: v537(0x0) = CONST 
    0x53a: REVERT v537(0x0), v537(0x0)

    Begin block 0x53b
    prev=[0x52f], succ=[0x20d5B0x53b]
    =================================
    0x53d: v53d(0x40) = CONST 
    0x540: v540 = MLOAD v53d(0x40)
    0x541: v541(0x20) = CONST 
    0x543: v543(0x4) = CONST 
    0x545: v545(0x44) = CONST 
    0x547: v547 = CALLDATALOAD v545(0x44)
    0x54a: v54a = ADD v547, v543(0x4)
    0x54b: v54b = CALLDATALOAD v54a
    0x54c: v54c(0x1f) = CONST 
    0x54f: v54f = ADD v54b, v54c(0x1f)
    0x552: v552 = DIV v54f, v541(0x20)
    0x554: v554 = MUL v541(0x20), v552
    0x556: v556 = ADD v540, v554
    0x558: v558 = ADD v541(0x20), v556
    0x55b: MSTORE v53d(0x40), v558
    0x55e: MSTORE v540, v54b
    0x55f: v55f(0x4def) = CONST 
    0x564: v564 = CALLDATALOAD v543(0x4)
    0x565: v565(0x1) = CONST 
    0x567: v567(0xa0) = CONST 
    0x569: v569(0x2) = CONST 
    0x56b: v56b(0x10000000000000000000000000000000000000000) = EXP v569(0x2), v567(0xa0)
    0x56c: v56c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v56b(0x10000000000000000000000000000000000000000), v565(0x1)
    0x56d: v56d = AND v56c(0xffffffffffffffffffffffffffffffffffffffff), v564
    0x56f: v56f(0x24) = CONST 
    0x572: v572 = CALLDATALOAD v56f(0x24)
    0x574: v574 = CALLDATASIZE 
    0x577: v577(0x64) = CONST 
    0x57b: v57b = ADD v56f(0x24), v547
    0x581: v581 = ADD v540, v541(0x20)
    0x587: CALLDATACOPY v581, v57b, v54b
    0x58e: v58e = CALLDATALOAD v577(0x64)
    0x593: v593(0x20) = CONST 
    0x597: v597(0x84) = ADD v577(0x64), v593(0x20)
    0x598: v598 = CALLDATALOAD v597(0x84)
    0x59b: v59b(0x20d5) = CONST 
    0x5a0: JUMP v59b(0x20d5)

    Begin block 0x20d5B0x53b
    prev=[0x53b], succ=[0x212bB0x53b, 0x212fB0x53b]
    =================================
    0x20d6S0x53b: v20d6V53b(0x3) = CONST 
    0x20d8S0x53b: v20d8V53b = SLOAD v20d6V53b(0x3)
    0x20d9S0x53b: v20d9V53b(0x40) = CONST 
    0x20dcS0x53b: v20dcV53b = MLOAD v20d9V53b(0x40)
    0x20ddS0x53b: v20ddV53b(0xe0) = CONST 
    0x20dfS0x53b: v20dfV53b(0x2) = CONST 
    0x20e1S0x53b: v20e1V53b(0x100000000000000000000000000000000000000000000000000000000) = EXP v20dfV53b(0x2), v20ddV53b(0xe0)
    0x20e2S0x53b: v20e2V53b(0x7ccce851) = CONST 
    0x20e7S0x53b: v20e7V53b(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v20e2V53b(0x7ccce851), v20e1V53b(0x100000000000000000000000000000000000000000000000000000000)
    0x20e9S0x53b: MSTORE v20dcV53b, v20e7V53b(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x20eaS0x53b: v20eaV53b(0x1) = CONST 
    0x20ecS0x53b: v20ecV53b(0xa0) = CONST 
    0x20eeS0x53b: v20eeV53b(0x2) = CONST 
    0x20f0S0x53b: v20f0V53b(0x10000000000000000000000000000000000000000) = EXP v20eeV53b(0x2), v20ecV53b(0xa0)
    0x20f1S0x53b: v20f1V53b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20f0V53b(0x10000000000000000000000000000000000000000), v20eaV53b(0x1)
    0x20f4S0x53b: v20f4V53b = AND v56d, v20f1V53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x20f5S0x53b: v20f5V53b(0x4) = CONST 
    0x20f8S0x53b: v20f8V53b = ADD v20dcV53b, v20f5V53b(0x4)
    0x20f9S0x53b: MSTORE v20f8V53b, v20f4V53b
    0x20fbS0x53b: v20fbV53b = MLOAD v20d9V53b(0x40)
    0x20fcS0x53b: v20fcV53b(0x0) = CONST 
    0x2108S0x53b: v2108V53b = AND v20d8V53b, v20f1V53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x210aS0x53b: v210aV53b(0x7ccce851) = CONST 
    0x2110S0x53b: v2110V53b(0x24) = CONST 
    0x2114S0x53b: v2114V53b = ADD v20dcV53b, v2110V53b(0x24)
    0x2116S0x53b: v2116V53b(0x20) = CONST 
    0x211dS0x53b: v211dV53b(0x0) = SUB v20dcV53b, v20fbV53b
    0x211eS0x53b: v211eV53b(0x24) = ADD v211dV53b(0x0), v2110V53b(0x24)
    0x2123S0x53b: v2123V53b = EXTCODESIZE v2108V53b
    0x2124S0x53b: v2124V53b = ISZERO v2123V53b
    0x2126S0x53b: v2126V53b = ISZERO v2124V53b
    0x2127S0x53b: v2127V53b(0x212f) = CONST 
    0x212aS0x53b: JUMPI v2127V53b(0x212f), v2126V53b

    Begin block 0x212bB0x53b
    prev=[0x20d5B0x53b], succ=[]
    =================================
    0x212bS0x53b: v212bV53b(0x0) = CONST 
    0x212eS0x53b: REVERT v212bV53b(0x0), v212bV53b(0x0)

    Begin block 0x212fB0x53b
    prev=[0x20d5B0x53b], succ=[0x213aB0x53b, 0x2143B0x53b]
    =================================
    0x2131S0x53b: v2131V53b = GAS 
    0x2132S0x53b: v2132V53b = CALL v2131V53b, v2108V53b, v20fcV53b(0x0), v20fbV53b, v211eV53b(0x24), v20fbV53b, v2116V53b(0x20)
    0x2133S0x53b: v2133V53b = ISZERO v2132V53b
    0x2135S0x53b: v2135V53b = ISZERO v2133V53b
    0x2136S0x53b: v2136V53b(0x2143) = CONST 
    0x2139S0x53b: JUMPI v2136V53b(0x2143), v2135V53b

    Begin block 0x213aB0x53b
    prev=[0x212fB0x53b], succ=[]
    =================================
    0x213aS0x53b: v213aV53b = RETURNDATASIZE 
    0x213bS0x53b: v213bV53b(0x0) = CONST 
    0x213eS0x53b: RETURNDATACOPY v213bV53b(0x0), v213bV53b(0x0), v213aV53b
    0x213fS0x53b: v213fV53b = RETURNDATASIZE 
    0x2140S0x53b: v2140V53b(0x0) = CONST 
    0x2142S0x53b: REVERT v2140V53b(0x0), v213fV53b

    Begin block 0x2143B0x53b
    prev=[0x212fB0x53b], succ=[0x2155B0x53b, 0x2159B0x53b]
    =================================
    0x2148S0x53b: v2148V53b(0x40) = CONST 
    0x214aS0x53b: v214aV53b = MLOAD v2148V53b(0x40)
    0x214bS0x53b: v214bV53b = RETURNDATASIZE 
    0x214cS0x53b: v214cV53b(0x20) = CONST 
    0x214fS0x53b: v214fV53b = LT v214bV53b, v214cV53b(0x20)
    0x2150S0x53b: v2150V53b = ISZERO v214fV53b
    0x2151S0x53b: v2151V53b(0x2159) = CONST 
    0x2154S0x53b: JUMPI v2151V53b(0x2159), v2150V53b

    Begin block 0x2155B0x53b
    prev=[0x2143B0x53b], succ=[]
    =================================
    0x2155S0x53b: v2155V53b(0x0) = CONST 
    0x2158S0x53b: REVERT v2155V53b(0x0), v2155V53b(0x0)

    Begin block 0x2159B0x53b
    prev=[0x2143B0x53b], succ=[0x2161B0x53b, 0x219eB0x53b]
    =================================
    0x215bS0x53b: v215bV53b = MLOAD v214aV53b
    0x215cS0x53b: v215cV53b = ISZERO v215bV53b
    0x215dS0x53b: v215dV53b(0x219e) = CONST 
    0x2160S0x53b: JUMPI v215dV53b(0x219e), v215cV53b

    Begin block 0x2161B0x53b
    prev=[0x2159B0x53b], succ=[]
    =================================
    0x2161S0x53b: v2161V53b(0x40) = CONST 
    0x2164S0x53b: v2164V53b = MLOAD v2161V53b(0x40)
    0x2165S0x53b: v2165V53b(0xe5) = CONST 
    0x2167S0x53b: v2167V53b(0x2) = CONST 
    0x2169S0x53b: v2169V53b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2167V53b(0x2), v2165V53b(0xe5)
    0x216aS0x53b: v216aV53b(0x461bcd) = CONST 
    0x216eS0x53b: v216eV53b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v216aV53b(0x461bcd), v2169V53b(0x2000000000000000000000000000000000000000000000000000000000)
    0x2170S0x53b: MSTORE v2164V53b, v216eV53b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2171S0x53b: v2171V53b(0x20) = CONST 
    0x2173S0x53b: v2173V53b(0x4) = CONST 
    0x2176S0x53b: v2176V53b = ADD v2164V53b, v2173V53b(0x4)
    0x2177S0x53b: MSTORE v2176V53b, v2171V53b(0x20)
    0x2178S0x53b: v2178V53b(0x1c) = CONST 
    0x217aS0x53b: v217aV53b(0x24) = CONST 
    0x217dS0x53b: v217dV53b = ADD v2164V53b, v217aV53b(0x24)
    0x217eS0x53b: MSTORE v217dV53b, v2178V53b(0x1c)
    0x217fS0x53b: v217fV53b(0x0) = CONST 
    0x2182S0x53b: v2182V53b = MLOAD v217fV53b(0x0)
    0x2183S0x53b: v2183V53b(0x20) = CONST 
    0x2185S0x53b: v2185V53b(0x4a70) = CONST 
    0x218dS0x53b: MSTORE v217fV53b(0x0), v2182V53b
    0x218eS0x53b: v218eV53b(0x44) = CONST 
    0x2191S0x53b: v2191V53b = ADD v2164V53b, v218eV53b(0x44)
    0x2192S0x53b: MSTORE v2191V53b, v5557V53b(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x2194S0x53b: v2194V53b = MLOAD v2161V53b(0x40)
    0x2198S0x53b: v2198V53b(0x0) = SUB v2164V53b, v2194V53b
    0x2199S0x53b: v2199V53b(0x64) = CONST 
    0x219bS0x53b: v219bV53b(0x64) = ADD v2199V53b(0x64), v2198V53b(0x0)
    0x219dS0x53b: REVERT v2194V53b, v219bV53b(0x64)
    0x5557S0x53b: v5557V53b(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x219eB0x53b
    prev=[0x2159B0x53b], succ=[0x21b1B0x53b, 0x21b5B0x53b]
    =================================
    0x219fS0x53b: v219fV53b(0x1) = CONST 
    0x21a1S0x53b: v21a1V53b = SLOAD v219fV53b(0x1)
    0x21a2S0x53b: v21a2V53b(0xa0) = CONST 
    0x21a4S0x53b: v21a4V53b(0x2) = CONST 
    0x21a6S0x53b: v21a6V53b(0x10000000000000000000000000000000000000000) = EXP v21a4V53b(0x2), v21a2V53b(0xa0)
    0x21a8S0x53b: v21a8V53b = DIV v21a1V53b, v21a6V53b(0x10000000000000000000000000000000000000000)
    0x21a9S0x53b: v21a9V53b(0xff) = CONST 
    0x21abS0x53b: v21abV53b = AND v21a9V53b(0xff), v21a8V53b
    0x21acS0x53b: v21acV53b = ISZERO v21abV53b
    0x21adS0x53b: v21adV53b(0x21b5) = CONST 
    0x21b0S0x53b: JUMPI v21adV53b(0x21b5), v21acV53b

    Begin block 0x21b1B0x53b
    prev=[0x219eB0x53b], succ=[]
    =================================
    0x21b1S0x53b: v21b1V53b(0x0) = CONST 
    0x21b4S0x53b: REVERT v21b1V53b(0x0), v21b1V53b(0x0)

    Begin block 0x21b5B0x53b
    prev=[0x219eB0x53b], succ=[0x21c1B0x53b]
    =================================
    0x21b6S0x53b: v21b6V53b(0x21c1) = CONST 
    0x21bdS0x53b: v21bdV53b(0x2569) = CONST 
    0x21c0S0x53b: v21c0_0V53b = CALLPRIVATE v21bdV53b(0x2569), v598, v58e, v572, v56d, v21b6V53b(0x21c1)

    Begin block 0x21c1B0x53b
    prev=[0x21b5B0x53b], succ=[0x21cdB0x53b]
    =================================
    0x21c4S0x53b: v21c4V53b(0x21cd) = CONST 
    0x21c9S0x53b: v21c9V53b(0x44ed) = CONST 
    0x21ccS0x53b: v21cc_0V53b = CALLPRIVATE v21c9V53b(0x44ed), v540, v21c0_0V53b, v21c4V53b(0x21cd)

    Begin block 0x21cdB0x53b
    prev=[0x21c1B0x53b], succ=[0x221dB0x53b, 0x2221B0x53b]
    =================================
    0x21ceS0x53b: v21ceV53b(0x3) = CONST 
    0x21d0S0x53b: v21d0V53b = SLOAD v21ceV53b(0x3)
    0x21d1S0x53b: v21d1V53b(0x40) = CONST 
    0x21d4S0x53b: v21d4V53b = MLOAD v21d1V53b(0x40)
    0x21d5S0x53b: v21d5V53b(0xe0) = CONST 
    0x21d7S0x53b: v21d7V53b(0x2) = CONST 
    0x21d9S0x53b: v21d9V53b(0x100000000000000000000000000000000000000000000000000000000) = EXP v21d7V53b(0x2), v21d5V53b(0xe0)
    0x21daS0x53b: v21daV53b(0x7ccce851) = CONST 
    0x21dfS0x53b: v21dfV53b(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v21daV53b(0x7ccce851), v21d9V53b(0x100000000000000000000000000000000000000000000000000000000)
    0x21e1S0x53b: MSTORE v21d4V53b, v21dfV53b(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x21e2S0x53b: v21e2V53b(0x1) = CONST 
    0x21e4S0x53b: v21e4V53b(0xa0) = CONST 
    0x21e6S0x53b: v21e6V53b(0x2) = CONST 
    0x21e8S0x53b: v21e8V53b(0x10000000000000000000000000000000000000000) = EXP v21e6V53b(0x2), v21e4V53b(0xa0)
    0x21e9S0x53b: v21e9V53b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21e8V53b(0x10000000000000000000000000000000000000000), v21e2V53b(0x1)
    0x21ecS0x53b: v21ecV53b = AND v21cc_0V53b, v21e9V53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x21edS0x53b: v21edV53b(0x4) = CONST 
    0x21f0S0x53b: v21f0V53b = ADD v21d4V53b, v21edV53b(0x4)
    0x21f1S0x53b: MSTORE v21f0V53b, v21ecV53b
    0x21f3S0x53b: v21f3V53b = MLOAD v21d1V53b(0x40)
    0x21f8S0x53b: v21f8V53b = AND v21d0V53b, v21e9V53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x21faS0x53b: v21faV53b(0x7ccce851) = CONST 
    0x2200S0x53b: v2200V53b(0x24) = CONST 
    0x2204S0x53b: v2204V53b = ADD v21d4V53b, v2200V53b(0x24)
    0x2206S0x53b: v2206V53b(0x20) = CONST 
    0x220eS0x53b: v220eV53b(0x0) = SUB v21d4V53b, v21f3V53b
    0x220fS0x53b: v220fV53b(0x24) = ADD v220eV53b(0x0), v2200V53b(0x24)
    0x2211S0x53b: v2211V53b(0x0) = CONST 
    0x2215S0x53b: v2215V53b = EXTCODESIZE v21f8V53b
    0x2216S0x53b: v2216V53b = ISZERO v2215V53b
    0x2218S0x53b: v2218V53b = ISZERO v2216V53b
    0x2219S0x53b: v2219V53b(0x2221) = CONST 
    0x221cS0x53b: JUMPI v2219V53b(0x2221), v2218V53b

    Begin block 0x221dB0x53b
    prev=[0x21cdB0x53b], succ=[]
    =================================
    0x221dS0x53b: v221dV53b(0x0) = CONST 
    0x2220S0x53b: REVERT v221dV53b(0x0), v221dV53b(0x0)

    Begin block 0x2221B0x53b
    prev=[0x21cdB0x53b], succ=[0x222cB0x53b, 0x2235B0x53b]
    =================================
    0x2223S0x53b: v2223V53b = GAS 
    0x2224S0x53b: v2224V53b = CALL v2223V53b, v21f8V53b, v2211V53b(0x0), v21f3V53b, v220fV53b(0x24), v21f3V53b, v2206V53b(0x20)
    0x2225S0x53b: v2225V53b = ISZERO v2224V53b
    0x2227S0x53b: v2227V53b = ISZERO v2225V53b
    0x2228S0x53b: v2228V53b(0x2235) = CONST 
    0x222bS0x53b: JUMPI v2228V53b(0x2235), v2227V53b

    Begin block 0x222cB0x53b
    prev=[0x2221B0x53b], succ=[]
    =================================
    0x222cS0x53b: v222cV53b = RETURNDATASIZE 
    0x222dS0x53b: v222dV53b(0x0) = CONST 
    0x2230S0x53b: RETURNDATACOPY v222dV53b(0x0), v222dV53b(0x0), v222cV53b
    0x2231S0x53b: v2231V53b = RETURNDATASIZE 
    0x2232S0x53b: v2232V53b(0x0) = CONST 
    0x2234S0x53b: REVERT v2232V53b(0x0), v2231V53b

    Begin block 0x2235B0x53b
    prev=[0x2221B0x53b], succ=[0x2247B0x53b, 0x224bB0x53b]
    =================================
    0x223aS0x53b: v223aV53b(0x40) = CONST 
    0x223cS0x53b: v223cV53b = MLOAD v223aV53b(0x40)
    0x223dS0x53b: v223dV53b = RETURNDATASIZE 
    0x223eS0x53b: v223eV53b(0x20) = CONST 
    0x2241S0x53b: v2241V53b = LT v223dV53b, v223eV53b(0x20)
    0x2242S0x53b: v2242V53b = ISZERO v2241V53b
    0x2243S0x53b: v2243V53b(0x224b) = CONST 
    0x2246S0x53b: JUMPI v2243V53b(0x224b), v2242V53b

    Begin block 0x2247B0x53b
    prev=[0x2235B0x53b], succ=[]
    =================================
    0x2247S0x53b: v2247V53b(0x0) = CONST 
    0x224aS0x53b: REVERT v2247V53b(0x0), v2247V53b(0x0)

    Begin block 0x224bB0x53b
    prev=[0x2235B0x53b], succ=[0x2253B0x53b, 0x22a2B0x53b]
    =================================
    0x224dS0x53b: v224dV53b = MLOAD v223cV53b
    0x224eS0x53b: v224eV53b = ISZERO v224dV53b
    0x224fS0x53b: v224fV53b(0x22a2) = CONST 
    0x2252S0x53b: JUMPI v224fV53b(0x22a2), v224eV53b

    Begin block 0x2253B0x53b
    prev=[0x224bB0x53b], succ=[]
    =================================
    0x2253S0x53b: v2253V53b(0x40) = CONST 
    0x2256S0x53b: v2256V53b = MLOAD v2253V53b(0x40)
    0x2257S0x53b: v2257V53b(0xe5) = CONST 
    0x2259S0x53b: v2259V53b(0x2) = CONST 
    0x225bS0x53b: v225bV53b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2259V53b(0x2), v2257V53b(0xe5)
    0x225cS0x53b: v225cV53b(0x461bcd) = CONST 
    0x2260S0x53b: v2260V53b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v225cV53b(0x461bcd), v225bV53b(0x2000000000000000000000000000000000000000000000000000000000)
    0x2262S0x53b: MSTORE v2256V53b, v2260V53b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2263S0x53b: v2263V53b(0x20) = CONST 
    0x2265S0x53b: v2265V53b(0x4) = CONST 
    0x2268S0x53b: v2268V53b = ADD v2256V53b, v2265V53b(0x4)
    0x2269S0x53b: MSTORE v2268V53b, v2263V53b(0x20)
    0x226aS0x53b: v226aV53b(0x15) = CONST 
    0x226cS0x53b: v226cV53b(0x24) = CONST 
    0x226fS0x53b: v226fV53b = ADD v2256V53b, v226cV53b(0x24)
    0x2270S0x53b: MSTORE v226fV53b, v226aV53b(0x15)
    0x2271S0x53b: v2271V53b(0x7369676e657220697320626c61636b6c69737465640000000000000000000000) = CONST 
    0x2292S0x53b: v2292V53b(0x44) = CONST 
    0x2295S0x53b: v2295V53b = ADD v2256V53b, v2292V53b(0x44)
    0x2296S0x53b: MSTORE v2295V53b, v2271V53b(0x7369676e657220697320626c61636b6c69737465640000000000000000000000)
    0x2298S0x53b: v2298V53b = MLOAD v2253V53b(0x40)
    0x229cS0x53b: v229cV53b(0x0) = SUB v2256V53b, v2298V53b
    0x229dS0x53b: v229dV53b(0x64) = CONST 
    0x229fS0x53b: v229fV53b(0x64) = ADD v229dV53b(0x64), v229cV53b(0x0)
    0x22a1S0x53b: REVERT v2298V53b, v229fV53b(0x64)

    Begin block 0x22a2B0x53b
    prev=[0x224bB0x53b], succ=[0x22c2B0x53b, 0x2337B0x53b]
    =================================
    0x22a3S0x53b: v22a3V53b(0x1) = CONST 
    0x22a5S0x53b: v22a5V53b(0xa0) = CONST 
    0x22a7S0x53b: v22a7V53b(0x2) = CONST 
    0x22a9S0x53b: v22a9V53b(0x10000000000000000000000000000000000000000) = EXP v22a7V53b(0x2), v22a5V53b(0xa0)
    0x22aaS0x53b: v22aaV53b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22a9V53b(0x10000000000000000000000000000000000000000), v22a3V53b(0x1)
    0x22acS0x53b: v22acV53b = AND v21cc_0V53b, v22aaV53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x22adS0x53b: v22adV53b(0x0) = CONST 
    0x22b1S0x53b: MSTORE v22adV53b(0x0), v22acV53b
    0x22b2S0x53b: v22b2V53b(0x5) = CONST 
    0x22b4S0x53b: v22b4V53b(0x20) = CONST 
    0x22b6S0x53b: MSTORE v22b4V53b(0x20), v22b2V53b(0x5)
    0x22b7S0x53b: v22b7V53b(0x40) = CONST 
    0x22baS0x53b: v22baV53b = SHA3 v22adV53b(0x0), v22b7V53b(0x40)
    0x22bbS0x53b: v22bbV53b = SLOAD v22baV53b
    0x22bdS0x53b: v22bdV53b = EQ v58e, v22bbV53b
    0x22beS0x53b: v22beV53b(0x2337) = CONST 
    0x22c1S0x53b: JUMPI v22beV53b(0x2337), v22bdV53b

    Begin block 0x22c2B0x53b
    prev=[0x22a2B0x53b], succ=[]
    =================================
    0x22c2S0x53b: v22c2V53b(0x40) = CONST 
    0x22c5S0x53b: v22c5V53b = MLOAD v22c2V53b(0x40)
    0x22c6S0x53b: v22c6V53b(0xe5) = CONST 
    0x22c8S0x53b: v22c8V53b(0x2) = CONST 
    0x22caS0x53b: v22caV53b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v22c8V53b(0x2), v22c6V53b(0xe5)
    0x22cbS0x53b: v22cbV53b(0x461bcd) = CONST 
    0x22cfS0x53b: v22cfV53b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v22cbV53b(0x461bcd), v22caV53b(0x2000000000000000000000000000000000000000000000000000000000)
    0x22d1S0x53b: MSTORE v22c5V53b, v22cfV53b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22d2S0x53b: v22d2V53b(0x20) = CONST 
    0x22d4S0x53b: v22d4V53b(0x4) = CONST 
    0x22d7S0x53b: v22d7V53b = ADD v22c5V53b, v22d4V53b(0x4)
    0x22d8S0x53b: MSTORE v22d7V53b, v22d2V53b(0x20)
    0x22d9S0x53b: v22d9V53b(0x2b) = CONST 
    0x22dbS0x53b: v22dbV53b(0x24) = CONST 
    0x22deS0x53b: v22deV53b = ADD v22c5V53b, v22dbV53b(0x24)
    0x22dfS0x53b: MSTORE v22deV53b, v22d9V53b(0x2b)
    0x22e0S0x53b: v22e0V53b(0x74686973207472616e73616374696f6e2068617320616c726561647920626565) = CONST 
    0x2301S0x53b: v2301V53b(0x44) = CONST 
    0x2304S0x53b: v2304V53b = ADD v22c5V53b, v2301V53b(0x44)
    0x2305S0x53b: MSTORE v2304V53b, v22e0V53b(0x74686973207472616e73616374696f6e2068617320616c726561647920626565)
    0x2306S0x53b: v2306V53b(0x6e2062726f616463617374000000000000000000000000000000000000000000) = CONST 
    0x2327S0x53b: v2327V53b(0x64) = CONST 
    0x232aS0x53b: v232aV53b = ADD v22c5V53b, v2327V53b(0x64)
    0x232bS0x53b: MSTORE v232aV53b, v2306V53b(0x6e2062726f616463617374000000000000000000000000000000000000000000)
    0x232dS0x53b: v232dV53b = MLOAD v22c2V53b(0x40)
    0x2331S0x53b: v2331V53b(0x0) = SUB v22c5V53b, v232dV53b
    0x2332S0x53b: v2332V53b(0x84) = CONST 
    0x2334S0x53b: v2334V53b(0x84) = ADD v2332V53b(0x84), v2331V53b(0x0)
    0x2336S0x53b: REVERT v232dV53b, v2334V53b(0x84)

    Begin block 0x2337B0x53b
    prev=[0x22a2B0x53b], succ=[0x235dB0x53b, 0x23d2B0x53b]
    =================================
    0x2338S0x53b: v2338V53b(0x1) = CONST 
    0x233aS0x53b: v233aV53b(0xa0) = CONST 
    0x233cS0x53b: v233cV53b(0x2) = CONST 
    0x233eS0x53b: v233eV53b(0x10000000000000000000000000000000000000000) = EXP v233cV53b(0x2), v233aV53b(0xa0)
    0x233fS0x53b: v233fV53b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v233eV53b(0x10000000000000000000000000000000000000000), v2338V53b(0x1)
    0x2341S0x53b: v2341V53b = AND v21cc_0V53b, v233fV53b(0xffffffffffffffffffffffffffffffffffffffff)
    0x2342S0x53b: v2342V53b(0x0) = CONST 
    0x2346S0x53b: MSTORE v2342V53b(0x0), v2341V53b
    0x2347S0x53b: v2347V53b(0x5) = CONST 
    0x2349S0x53b: v2349V53b(0x20) = CONST 
    0x234bS0x53b: MSTORE v2349V53b(0x20), v2347V53b(0x5)
    0x234cS0x53b: v234cV53b(0x40) = CONST 
    0x234fS0x53b: v234fV53b = SHA3 v2342V53b(0x0), v234cV53b(0x40)
    0x2351S0x53b: v2351V53b = SLOAD v234fV53b
    0x2352S0x53b: v2352V53b(0x1) = CONST 
    0x2354S0x53b: v2354V53b = ADD v2352V53b(0x1), v2351V53b
    0x2356S0x53b: SSTORE v234fV53b, v2354V53b
    0x2358S0x53b: v2358V53b = GT v598, v2342V53b(0x0)
    0x2359S0x53b: v2359V53b(0x23d2) = CONST 
    0x235cS0x53b: JUMPI v2359V53b(0x23d2), v2358V53b

    Begin block 0x235dB0x53b
    prev=[0x2337B0x53b], succ=[]
    =================================
    0x235dS0x53b: v235dV53b(0x40) = CONST 
    0x2360S0x53b: v2360V53b = MLOAD v235dV53b(0x40)
    0x2361S0x53b: v2361V53b(0xe5) = CONST 
    0x2363S0x53b: v2363V53b(0x2) = CONST 
    0x2365S0x53b: v2365V53b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2363V53b(0x2), v2361V53b(0xe5)
    0x2366S0x53b: v2366V53b(0x461bcd) = CONST 
    0x236aS0x53b: v236aV53b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2366V53b(0x461bcd), v2365V53b(0x2000000000000000000000000000000000000000000000000000000000)
    0x236cS0x53b: MSTORE v2360V53b, v236aV53b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x236dS0x53b: v236dV53b(0x20) = CONST 
    0x236fS0x53b: v236fV53b(0x4) = CONST 
    0x2372S0x53b: v2372V53b = ADD v2360V53b, v236fV53b(0x4)
    0x2373S0x53b: MSTORE v2372V53b, v236dV53b(0x20)
    0x2374S0x53b: v2374V53b(0x2e) = CONST 
    0x2376S0x53b: v2376V53b(0x24) = CONST 
    0x2379S0x53b: v2379V53b = ADD v2360V53b, v2376V53b(0x24)
    0x237aS0x53b: MSTORE v2379V53b, v2374V53b(0x2e)
    0x237bS0x53b: v237bV53b(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75) = CONST 
    0x239cS0x53b: v239cV53b(0x44) = CONST 
    0x239fS0x53b: v239fV53b = ADD v2360V53b, v239cV53b(0x44)
    0x23a0S0x53b: MSTORE v239fV53b, v237bV53b(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75)
    0x23a1S0x53b: v23a1V53b(0x737420626520706f736974697665000000000000000000000000000000000000) = CONST 
    0x23c2S0x53b: v23c2V53b(0x64) = CONST 
    0x23c5S0x53b: v23c5V53b = ADD v2360V53b, v23c2V53b(0x64)
    0x23c6S0x53b: MSTORE v23c5V53b, v23a1V53b(0x737420626520706f736974697665000000000000000000000000000000000000)
    0x23c8S0x53b: v23c8V53b = MLOAD v235dV53b(0x40)
    0x23ccS0x53b: v23ccV53b(0x0) = SUB v2360V53b, v23c8V53b
    0x23cdS0x53b: v23cdV53b(0x84) = CONST 
    0x23cfS0x53b: v23cfV53b(0x84) = ADD v23cdV53b(0x84), v23ccV53b(0x0)
    0x23d1S0x53b: REVERT v23c8V53b, v23cfV53b(0x84)

    Begin block 0x23d2B0x53b
    prev=[0x2337B0x53b], succ=[0x23dbB0x53b]
    =================================
    0x23d3S0x53b: v23d3V53b(0x23db) = CONST 
    0x23d7S0x53b: v23d7V53b(0x206a) = CONST 
    0x23daS0x53b: v23da_0V53b = CALLPRIVATE v23d7V53b(0x206a), v21cc_0V53b, v23d3V53b(0x23db)

    Begin block 0x23dbB0x53b
    prev=[0x23d2B0x53b], succ=[0x23e3B0x53b, 0x2457B0x53b]
    =================================
    0x23ddS0x53b: v23ddV53b = GT v598, v23da_0V53b
    0x23deS0x53b: v23deV53b = ISZERO v23ddV53b
    0x23dfS0x53b: v23dfV53b(0x2457) = CONST 
    0x23e2S0x53b: JUMPI v23dfV53b(0x2457), v23deV53b

    Begin block 0x23e3B0x53b
    prev=[0x23dbB0x53b], succ=[]
    =================================
    0x23e3S0x53b: v23e3V53b(0x40) = CONST 
    0x23e6S0x53b: v23e6V53b = MLOAD v23e3V53b(0x40)
    0x23e7S0x53b: v23e7V53b(0xe5) = CONST 
    0x23e9S0x53b: v23e9V53b(0x2) = CONST 
    0x23ebS0x53b: v23ebV53b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v23e9V53b(0x2), v23e7V53b(0xe5)
    0x23ecS0x53b: v23ecV53b(0x461bcd) = CONST 
    0x23f0S0x53b: v23f0V53b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v23ecV53b(0x461bcd), v23ebV53b(0x2000000000000000000000000000000000000000000000000000000000)
    0x23f2S0x53b: MSTORE v23e6V53b, v23f0V53b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x23f3S0x53b: v23f3V53b(0x20) = CONST 
    0x23f5S0x53b: v23f5V53b(0x4) = CONST 
    0x23f8S0x53b: v23f8V53b = ADD v23e6V53b, v23f5V53b(0x4)
    0x23f9S0x53b: MSTORE v23f8V53b, v23f3V53b(0x20)
    0x23faS0x53b: v23faV53b(0x24) = CONST 
    0x23feS0x53b: v23feV53b = ADD v23e6V53b, v23faV53b(0x24)
    0x23ffS0x53b: MSTORE v23feV53b, v23faV53b(0x24)
    0x2400S0x53b: v2400V53b(0x6e6f7420656e6f7567682062616c616e636520746f207265776172642072656c) = CONST 
    0x2421S0x53b: v2421V53b(0x44) = CONST 
    0x2424S0x53b: v2424V53b = ADD v23e6V53b, v2421V53b(0x44)
    0x2425S0x53b: MSTORE v2424V53b, v2400V53b(0x6e6f7420656e6f7567682062616c616e636520746f207265776172642072656c)
    0x2426S0x53b: v2426V53b(0x6179657200000000000000000000000000000000000000000000000000000000) = CONST 
    0x2447S0x53b: v2447V53b(0x64) = CONST 
    0x244aS0x53b: v244aV53b = ADD v23e6V53b, v2447V53b(0x64)
    0x244bS0x53b: MSTORE v244aV53b, v2426V53b(0x6179657200000000000000000000000000000000000000000000000000000000)
    0x244dS0x53b: v244dV53b = MLOAD v23e3V53b(0x40)
    0x2451S0x53b: v2451V53b(0x0) = SUB v23e6V53b, v244dV53b
    0x2452S0x53b: v2452V53b(0x84) = CONST 
    0x2454S0x53b: v2454V53b(0x84) = ADD v2452V53b(0x84), v2451V53b(0x0)
    0x2456S0x53b: REVERT v244dV53b, v2454V53b(0x84)

    Begin block 0x2457B0x53b
    prev=[0x23dbB0x53b], succ=[0x535bB0x53b]
    =================================
    0x2458S0x53b: v2458V53b(0x535b) = CONST 
    0x245eS0x53b: v245eV53b(0x465c) = CONST 
    0x2461S0x53b: CALLPRIVATE v245eV53b(0x465c), v21cc_0V53b, v572, v56d, v2458V53b(0x535b)

    Begin block 0x535bB0x53b
    prev=[0x2457B0x53b], succ=[0x246d0x20d5B0x53b]
    =================================
    0x535cS0x53b: v535cV53b(0x246d) = CONST 
    0x535fS0x53b: v535fV53b = CALLER 
    0x5362S0x53b: v5362V53b(0x4176) = CONST 
    0x5365S0x53b: CALLPRIVATE v5362V53b(0x4176), v598, v21cc_0V53b, v535fV53b, v535cV53b(0x246d)

    Begin block 0x246d0x20d5B0x53b
    prev=[0x535bB0x53b], succ=[0x4def]
    =================================
    0x246f0x20d5S0x53b: v20d5246fV53b(0x1) = CONST 
    0x247b0x20d5S0x53b: JUMP v55f(0x4def)

    Begin block 0x4def
    prev=[0x246d0x20d5B0x53b], succ=[]
    =================================
    0x4df0: v4df0(0x40) = CONST 
    0x4df3: v4df3 = MLOAD v4df0(0x40)
    0x4df5: v4df5 = ISZERO v20d5246fV53b(0x1)
    0x4df6: v4df6 = ISZERO v4df5
    0x4df8: MSTORE v4df3, v4df6
    0x4df9: v4df9 = MLOAD v4df0(0x40)
    0x4dfd: v4dfd(0x0) = SUB v4df3, v4df9
    0x4dfe: v4dfe(0x20) = CONST 
    0x4e00: v4e00(0x20) = ADD v4dfe(0x20), v4dfd(0x0)
    0x4e02: RETURN v4df9, v4e00(0x20)

}

function pause()() public {
    Begin block 0x5a1
    prev=[], succ=[0x5a9, 0x5ad]
    =================================
    0x5a2: v5a2 = CALLVALUE 
    0x5a4: v5a4 = ISZERO v5a2
    0x5a5: v5a5(0x5ad) = CONST 
    0x5a8: JUMPI v5a5(0x5ad), v5a4

    Begin block 0x5a9
    prev=[0x5a1], succ=[]
    =================================
    0x5a9: v5a9(0x0) = CONST 
    0x5ac: REVERT v5a9(0x0), v5a9(0x0)

    Begin block 0x5ad
    prev=[0x5a1], succ=[0x247c]
    =================================
    0x5af: v5af(0x4e22) = CONST 
    0x5b2: v5b2(0x247c) = CONST 
    0x5b5: JUMP v5b2(0x247c)

    Begin block 0x247c
    prev=[0x5ad], succ=[0x248f, 0x2493]
    =================================
    0x247d: v247d(0x0) = CONST 
    0x247f: v247f = SLOAD v247d(0x0)
    0x2480: v2480(0x1) = CONST 
    0x2482: v2482(0xa0) = CONST 
    0x2484: v2484(0x2) = CONST 
    0x2486: v2486(0x10000000000000000000000000000000000000000) = EXP v2484(0x2), v2482(0xa0)
    0x2487: v2487(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2486(0x10000000000000000000000000000000000000000), v2480(0x1)
    0x2488: v2488 = AND v2487(0xffffffffffffffffffffffffffffffffffffffff), v247f
    0x2489: v2489 = CALLER 
    0x248a: v248a = EQ v2489, v2488
    0x248b: v248b(0x2493) = CONST 
    0x248e: JUMPI v248b(0x2493), v248a

    Begin block 0x248f
    prev=[0x247c], succ=[]
    =================================
    0x248f: v248f(0x0) = CONST 
    0x2492: REVERT v248f(0x0), v248f(0x0)

    Begin block 0x2493
    prev=[0x247c], succ=[0x24a6, 0x24aa]
    =================================
    0x2494: v2494(0x1) = CONST 
    0x2496: v2496 = SLOAD v2494(0x1)
    0x2497: v2497(0xa0) = CONST 
    0x2499: v2499(0x2) = CONST 
    0x249b: v249b(0x10000000000000000000000000000000000000000) = EXP v2499(0x2), v2497(0xa0)
    0x249d: v249d = DIV v2496, v249b(0x10000000000000000000000000000000000000000)
    0x249e: v249e(0xff) = CONST 
    0x24a0: v24a0 = AND v249e(0xff), v249d
    0x24a1: v24a1 = ISZERO v24a0
    0x24a2: v24a2(0x24aa) = CONST 
    0x24a5: JUMPI v24a2(0x24aa), v24a1

    Begin block 0x24a6
    prev=[0x2493], succ=[]
    =================================
    0x24a6: v24a6(0x0) = CONST 
    0x24a9: REVERT v24a6(0x0), v24a6(0x0)

    Begin block 0x24aa
    prev=[0x2493], succ=[0x4e22]
    =================================
    0x24ab: v24ab(0x1) = CONST 
    0x24ae: v24ae = SLOAD v24ab(0x1)
    0x24af: v24af(0xff0000000000000000000000000000000000000000) = CONST 
    0x24c5: v24c5(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v24af(0xff0000000000000000000000000000000000000000)
    0x24c6: v24c6 = AND v24c5(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v24ae
    0x24c7: v24c7(0xa0) = CONST 
    0x24c9: v24c9(0x2) = CONST 
    0x24cb: v24cb(0x10000000000000000000000000000000000000000) = EXP v24c9(0x2), v24c7(0xa0)
    0x24cc: v24cc = OR v24cb(0x10000000000000000000000000000000000000000), v24c6
    0x24ce: SSTORE v24ab(0x1), v24cc
    0x24cf: v24cf(0x40) = CONST 
    0x24d1: v24d1 = MLOAD v24cf(0x40)
    0x24d2: v24d2(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625) = CONST 
    0x24f4: v24f4(0x0) = CONST 
    0x24f7: LOG1 v24d1, v24f4(0x0), v24d2(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625)
    0x24f8: JUMP v5af(0x4e22)

    Begin block 0x4e22
    prev=[0x24aa], succ=[]
    =================================
    0x4e23: STOP 

}

function computeFeeRate(address)() public {
    Begin block 0x5b6
    prev=[], succ=[0x5be, 0x5c2]
    =================================
    0x5b7: v5b7 = CALLVALUE 
    0x5b9: v5b9 = ISZERO v5b7
    0x5ba: v5ba(0x5c2) = CONST 
    0x5bd: JUMPI v5ba(0x5c2), v5b9

    Begin block 0x5be
    prev=[0x5b6], succ=[]
    =================================
    0x5be: v5be(0x0) = CONST 
    0x5c1: REVERT v5be(0x0), v5be(0x0)

    Begin block 0x5c2
    prev=[0x5b6], succ=[0x4e43]
    =================================
    0x5c4: v5c4(0x4e43) = CONST 
    0x5c7: v5c7(0x1) = CONST 
    0x5c9: v5c9(0xa0) = CONST 
    0x5cb: v5cb(0x2) = CONST 
    0x5cd: v5cd(0x10000000000000000000000000000000000000000) = EXP v5cb(0x2), v5c9(0xa0)
    0x5ce: v5ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5cd(0x10000000000000000000000000000000000000000), v5c7(0x1)
    0x5cf: v5cf(0x4) = CONST 
    0x5d1: v5d1 = CALLDATALOAD v5cf(0x4)
    0x5d2: v5d2 = AND v5d1, v5ce(0xffffffffffffffffffffffffffffffffffffffff)
    0x5d3: v5d3(0x24f9) = CONST 
    0x5d6: v5d6_0 = CALLPRIVATE v5d3(0x24f9), v5d2, v5c4(0x4e43)

    Begin block 0x4e43
    prev=[0x5c2], succ=[]
    =================================
    0x4e44: v4e44(0x40) = CONST 
    0x4e47: v4e47 = MLOAD v4e44(0x40)
    0x4e4a: MSTORE v4e47, v5d6_0
    0x4e4b: v4e4b = MLOAD v4e44(0x40)
    0x4e4f: v4e4f(0x0) = SUB v4e47, v4e4b
    0x4e50: v4e50(0x20) = CONST 
    0x4e52: v4e52(0x20) = ADD v4e50(0x20), v4e4f(0x0)
    0x4e54: RETURN v4e4b, v4e52(0x20)

}

function isMethodEnabled()() public {
    Begin block 0x5d7
    prev=[], succ=[0x5df, 0x5e3]
    =================================
    0x5d8: v5d8 = CALLVALUE 
    0x5da: v5da = ISZERO v5d8
    0x5db: v5db(0x5e3) = CONST 
    0x5de: JUMPI v5db(0x5e3), v5da

    Begin block 0x5df
    prev=[0x5d7], succ=[]
    =================================
    0x5df: v5df(0x0) = CONST 
    0x5e2: REVERT v5df(0x0), v5df(0x0)

    Begin block 0x5e3
    prev=[0x5d7], succ=[0x2529]
    =================================
    0x5e5: v5e5(0x4e74) = CONST 
    0x5e8: v5e8(0x2529) = CONST 
    0x5eb: JUMP v5e8(0x2529)

    Begin block 0x2529
    prev=[0x5e3], succ=[0x4e74]
    =================================
    0x252a: v252a(0x1) = CONST 
    0x252c: v252c = SLOAD v252a(0x1)
    0x252d: v252d(0x1000000000000000000000000000000000000000000) = CONST 
    0x2545: v2545 = DIV v252c, v252d(0x1000000000000000000000000000000000000000000)
    0x2546: v2546(0xff) = CONST 
    0x2548: v2548 = AND v2546(0xff), v2545
    0x254a: JUMP v5e5(0x4e74)

    Begin block 0x4e74
    prev=[0x2529], succ=[]
    =================================
    0x4e75: v4e75(0x40) = CONST 
    0x4e78: v4e78 = MLOAD v4e75(0x40)
    0x4e7a: v4e7a = ISZERO v2548
    0x4e7b: v4e7b = ISZERO v4e7a
    0x4e7d: MSTORE v4e78, v4e7b
    0x4e7e: v4e7e = MLOAD v4e75(0x40)
    0x4e82: v4e82(0x0) = SUB v4e78, v4e7e
    0x4e83: v4e83(0x20) = CONST 
    0x4e85: v4e85(0x20) = ADD v4e83(0x20), v4e82(0x0)
    0x4e87: RETURN v4e7e, v4e85(0x20)

}

function owner()() public {
    Begin block 0x5ec
    prev=[], succ=[0x5f4, 0x5f8]
    =================================
    0x5ed: v5ed = CALLVALUE 
    0x5ef: v5ef = ISZERO v5ed
    0x5f0: v5f0(0x5f8) = CONST 
    0x5f3: JUMPI v5f0(0x5f8), v5ef

    Begin block 0x5f4
    prev=[0x5ec], succ=[]
    =================================
    0x5f4: v5f4(0x0) = CONST 
    0x5f7: REVERT v5f4(0x0), v5f4(0x0)

    Begin block 0x5f8
    prev=[0x5ec], succ=[0x254b]
    =================================
    0x5fa: v5fa(0x4ea7) = CONST 
    0x5fd: v5fd(0x254b) = CONST 
    0x600: JUMP v5fd(0x254b)

    Begin block 0x254b
    prev=[0x5f8], succ=[0x4ea7]
    =================================
    0x254c: v254c(0x0) = CONST 
    0x254e: v254e = SLOAD v254c(0x0)
    0x254f: v254f(0x1) = CONST 
    0x2551: v2551(0xa0) = CONST 
    0x2553: v2553(0x2) = CONST 
    0x2555: v2555(0x10000000000000000000000000000000000000000) = EXP v2553(0x2), v2551(0xa0)
    0x2556: v2556(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2555(0x10000000000000000000000000000000000000000), v254f(0x1)
    0x2557: v2557 = AND v2556(0xffffffffffffffffffffffffffffffffffffffff), v254e
    0x2559: JUMP v5fa(0x4ea7)

    Begin block 0x4ea7
    prev=[0x254b], succ=[]
    =================================
    0x4ea8: v4ea8(0x40) = CONST 
    0x4eab: v4eab = MLOAD v4ea8(0x40)
    0x4eac: v4eac(0x1) = CONST 
    0x4eae: v4eae(0xa0) = CONST 
    0x4eb0: v4eb0(0x2) = CONST 
    0x4eb2: v4eb2(0x10000000000000000000000000000000000000000) = EXP v4eb0(0x2), v4eae(0xa0)
    0x4eb3: v4eb3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4eb2(0x10000000000000000000000000000000000000000), v4eac(0x1)
    0x4eb6: v4eb6 = AND v2557, v4eb3(0xffffffffffffffffffffffffffffffffffffffff)
    0x4eb8: MSTORE v4eab, v4eb6
    0x4eb9: v4eb9 = MLOAD v4ea8(0x40)
    0x4ebd: v4ebd(0x0) = SUB v4eab, v4eb9
    0x4ebe: v4ebe(0x20) = CONST 
    0x4ec0: v4ec0(0x20) = ADD v4ebe(0x20), v4ebd(0x0)
    0x4ec2: RETURN v4eb9, v4ec0(0x20)

}

function tokenStorage_CD()() public {
    Begin block 0x61d
    prev=[], succ=[0x625, 0x629]
    =================================
    0x61e: v61e = CALLVALUE 
    0x620: v620 = ISZERO v61e
    0x621: v621(0x629) = CONST 
    0x624: JUMPI v621(0x629), v620

    Begin block 0x625
    prev=[0x61d], succ=[]
    =================================
    0x625: v625(0x0) = CONST 
    0x628: REVERT v625(0x0), v625(0x0)

    Begin block 0x629
    prev=[0x61d], succ=[0x255a]
    =================================
    0x62b: v62b(0x4ee2) = CONST 
    0x62e: v62e(0x255a) = CONST 
    0x631: JUMP v62e(0x255a)

    Begin block 0x255a
    prev=[0x629], succ=[0x4ee2]
    =================================
    0x255b: v255b(0x4) = CONST 
    0x255d: v255d = SLOAD v255b(0x4)
    0x255e: v255e(0x1) = CONST 
    0x2560: v2560(0xa0) = CONST 
    0x2562: v2562(0x2) = CONST 
    0x2564: v2564(0x10000000000000000000000000000000000000000) = EXP v2562(0x2), v2560(0xa0)
    0x2565: v2565(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2564(0x10000000000000000000000000000000000000000), v255e(0x1)
    0x2566: v2566 = AND v2565(0xffffffffffffffffffffffffffffffffffffffff), v255d
    0x2568: JUMP v62b(0x4ee2)

    Begin block 0x4ee2
    prev=[0x255a], succ=[]
    =================================
    0x4ee3: v4ee3(0x40) = CONST 
    0x4ee6: v4ee6 = MLOAD v4ee3(0x40)
    0x4ee7: v4ee7(0x1) = CONST 
    0x4ee9: v4ee9(0xa0) = CONST 
    0x4eeb: v4eeb(0x2) = CONST 
    0x4eed: v4eed(0x10000000000000000000000000000000000000000) = EXP v4eeb(0x2), v4ee9(0xa0)
    0x4eee: v4eee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4eed(0x10000000000000000000000000000000000000000), v4ee7(0x1)
    0x4ef1: v4ef1 = AND v2566, v4eee(0xffffffffffffffffffffffffffffffffffffffff)
    0x4ef3: MSTORE v4ee6, v4ef1
    0x4ef4: v4ef4 = MLOAD v4ee3(0x40)
    0x4ef8: v4ef8(0x0) = SUB v4ee6, v4ef4
    0x4ef9: v4ef9(0x20) = CONST 
    0x4efb: v4efb(0x20) = ADD v4ef9(0x20), v4ef8(0x0)
    0x4efd: RETURN v4ef4, v4efb(0x20)

}

function metaApproveHash(address,uint256,uint256,uint256)() public {
    Begin block 0x632
    prev=[], succ=[0x63a, 0x63e]
    =================================
    0x633: v633 = CALLVALUE 
    0x635: v635 = ISZERO v633
    0x636: v636(0x63e) = CONST 
    0x639: JUMPI v636(0x63e), v635

    Begin block 0x63a
    prev=[0x632], succ=[]
    =================================
    0x63a: v63a(0x0) = CONST 
    0x63d: REVERT v63a(0x0), v63a(0x0)

    Begin block 0x63e
    prev=[0x632], succ=[0x4f1d]
    =================================
    0x640: v640(0x4f1d) = CONST 
    0x643: v643(0x1) = CONST 
    0x645: v645(0xa0) = CONST 
    0x647: v647(0x2) = CONST 
    0x649: v649(0x10000000000000000000000000000000000000000) = EXP v647(0x2), v645(0xa0)
    0x64a: v64a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v649(0x10000000000000000000000000000000000000000), v643(0x1)
    0x64b: v64b(0x4) = CONST 
    0x64d: v64d = CALLDATALOAD v64b(0x4)
    0x64e: v64e = AND v64d, v64a(0xffffffffffffffffffffffffffffffffffffffff)
    0x64f: v64f(0x24) = CONST 
    0x651: v651 = CALLDATALOAD v64f(0x24)
    0x652: v652(0x44) = CONST 
    0x654: v654 = CALLDATALOAD v652(0x44)
    0x655: v655(0x64) = CONST 
    0x657: v657 = CALLDATALOAD v655(0x64)
    0x658: v658(0x2569) = CONST 
    0x65b: v65b_0 = CALLPRIVATE v658(0x2569), v657, v654, v651, v64e, v640(0x4f1d)

    Begin block 0x4f1d
    prev=[0x63e], succ=[]
    =================================
    0x4f1e: v4f1e(0x40) = CONST 
    0x4f21: v4f21 = MLOAD v4f1e(0x40)
    0x4f24: MSTORE v4f21, v65b_0
    0x4f25: v4f25 = MLOAD v4f1e(0x40)
    0x4f29: v4f29(0x0) = SUB v4f21, v4f25
    0x4f2a: v4f2a(0x20) = CONST 
    0x4f2c: v4f2c(0x20) = ADD v4f2a(0x20), v4f29(0x0)
    0x4f2e: RETURN v4f25, v4f2c(0x20)

}

function unlock()() public {
    Begin block 0x65c
    prev=[], succ=[0x664, 0x668]
    =================================
    0x65d: v65d = CALLVALUE 
    0x65f: v65f = ISZERO v65d
    0x660: v660(0x668) = CONST 
    0x663: JUMPI v660(0x668), v65f

    Begin block 0x664
    prev=[0x65c], succ=[]
    =================================
    0x664: v664(0x0) = CONST 
    0x667: REVERT v664(0x0), v664(0x0)

    Begin block 0x668
    prev=[0x65c], succ=[0x264c]
    =================================
    0x66a: v66a(0x4f4e) = CONST 
    0x66d: v66d(0x264c) = CONST 
    0x670: JUMP v66d(0x264c)

    Begin block 0x264c
    prev=[0x668], succ=[0x265f, 0x2663]
    =================================
    0x264d: v264d(0x0) = CONST 
    0x264f: v264f = SLOAD v264d(0x0)
    0x2650: v2650(0x1) = CONST 
    0x2652: v2652(0xa0) = CONST 
    0x2654: v2654(0x2) = CONST 
    0x2656: v2656(0x10000000000000000000000000000000000000000) = EXP v2654(0x2), v2652(0xa0)
    0x2657: v2657(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2656(0x10000000000000000000000000000000000000000), v2650(0x1)
    0x2658: v2658 = AND v2657(0xffffffffffffffffffffffffffffffffffffffff), v264f
    0x2659: v2659 = CALLER 
    0x265a: v265a = EQ v2659, v2658
    0x265b: v265b(0x2663) = CONST 
    0x265e: JUMPI v265b(0x2663), v265a

    Begin block 0x265f
    prev=[0x264c], succ=[]
    =================================
    0x265f: v265f(0x0) = CONST 
    0x2662: REVERT v265f(0x0), v265f(0x0)

    Begin block 0x2663
    prev=[0x264c], succ=[0x4f4e]
    =================================
    0x2664: v2664(0x1) = CONST 
    0x2667: v2667 = SLOAD v2664(0x1)
    0x2668: v2668(0xff000000000000000000000000000000000000000000) = CONST 
    0x267f: v267f(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v2668(0xff000000000000000000000000000000000000000000)
    0x2680: v2680 = AND v267f(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v2667
    0x2681: v2681(0x1000000000000000000000000000000000000000000) = CONST 
    0x2698: v2698 = OR v2681(0x1000000000000000000000000000000000000000000), v2680
    0x269a: SSTORE v2664(0x1), v2698
    0x269b: v269b(0x40) = CONST 
    0x269d: v269d = MLOAD v269b(0x40)
    0x269e: v269e(0x19aad37188a1d3921e29eb3c66acf43d81975e107cb650d58cca878627955fd6) = CONST 
    0x26c0: v26c0(0x0) = CONST 
    0x26c3: LOG1 v269d, v26c0(0x0), v269e(0x19aad37188a1d3921e29eb3c66acf43d81975e107cb650d58cca878627955fd6)
    0x26c4: JUMP v66a(0x4f4e)

    Begin block 0x4f4e
    prev=[0x2663], succ=[]
    =================================
    0x4f4f: STOP 

}

function transfer(address,uint256)() public {
    Begin block 0x671
    prev=[], succ=[0x679, 0x67d]
    =================================
    0x672: v672 = CALLVALUE 
    0x674: v674 = ISZERO v672
    0x675: v675(0x67d) = CONST 
    0x678: JUMPI v675(0x67d), v674

    Begin block 0x679
    prev=[0x671], succ=[]
    =================================
    0x679: v679(0x0) = CONST 
    0x67c: REVERT v679(0x0), v679(0x0)

    Begin block 0x67d
    prev=[0x671], succ=[0x26c5]
    =================================
    0x67f: v67f(0x4f6f) = CONST 
    0x682: v682(0x1) = CONST 
    0x684: v684(0xa0) = CONST 
    0x686: v686(0x2) = CONST 
    0x688: v688(0x10000000000000000000000000000000000000000) = EXP v686(0x2), v684(0xa0)
    0x689: v689(0xffffffffffffffffffffffffffffffffffffffff) = SUB v688(0x10000000000000000000000000000000000000000), v682(0x1)
    0x68a: v68a(0x4) = CONST 
    0x68c: v68c = CALLDATALOAD v68a(0x4)
    0x68d: v68d = AND v68c, v689(0xffffffffffffffffffffffffffffffffffffffff)
    0x68e: v68e(0x24) = CONST 
    0x690: v690 = CALLDATALOAD v68e(0x24)
    0x691: v691(0x26c5) = CONST 
    0x694: JUMP v691(0x26c5)

    Begin block 0x26c5
    prev=[0x67d], succ=[0x2714, 0x2718]
    =================================
    0x26c6: v26c6(0x3) = CONST 
    0x26c8: v26c8 = SLOAD v26c6(0x3)
    0x26c9: v26c9(0x40) = CONST 
    0x26cc: v26cc = MLOAD v26c9(0x40)
    0x26cd: v26cd(0xe0) = CONST 
    0x26cf: v26cf(0x2) = CONST 
    0x26d1: v26d1(0x100000000000000000000000000000000000000000000000000000000) = EXP v26cf(0x2), v26cd(0xe0)
    0x26d2: v26d2(0x7ccce851) = CONST 
    0x26d7: v26d7(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v26d2(0x7ccce851), v26d1(0x100000000000000000000000000000000000000000000000000000000)
    0x26d9: MSTORE v26cc, v26d7(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x26da: v26da(0x1) = CONST 
    0x26dc: v26dc(0xa0) = CONST 
    0x26de: v26de(0x2) = CONST 
    0x26e0: v26e0(0x10000000000000000000000000000000000000000) = EXP v26de(0x2), v26dc(0xa0)
    0x26e1: v26e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26e0(0x10000000000000000000000000000000000000000), v26da(0x1)
    0x26e4: v26e4 = AND v68d, v26e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x26e5: v26e5(0x4) = CONST 
    0x26e8: v26e8 = ADD v26cc, v26e5(0x4)
    0x26e9: MSTORE v26e8, v26e4
    0x26eb: v26eb = MLOAD v26c9(0x40)
    0x26ec: v26ec(0x0) = CONST 
    0x26f1: v26f1 = AND v26e1(0xffffffffffffffffffffffffffffffffffffffff), v26c8
    0x26f3: v26f3(0x7ccce851) = CONST 
    0x26f9: v26f9(0x24) = CONST 
    0x26fd: v26fd = ADD v26cc, v26f9(0x24)
    0x26ff: v26ff(0x20) = CONST 
    0x2706: v2706(0x0) = SUB v26cc, v26eb
    0x2707: v2707(0x24) = ADD v2706(0x0), v26f9(0x24)
    0x270c: v270c = EXTCODESIZE v26f1
    0x270d: v270d = ISZERO v270c
    0x270f: v270f = ISZERO v270d
    0x2710: v2710(0x2718) = CONST 
    0x2713: JUMPI v2710(0x2718), v270f

    Begin block 0x2714
    prev=[0x26c5], succ=[]
    =================================
    0x2714: v2714(0x0) = CONST 
    0x2717: REVERT v2714(0x0), v2714(0x0)

    Begin block 0x2718
    prev=[0x26c5], succ=[0x2723, 0x272c]
    =================================
    0x271a: v271a = GAS 
    0x271b: v271b = CALL v271a, v26f1, v26ec(0x0), v26eb, v2707(0x24), v26eb, v26ff(0x20)
    0x271c: v271c = ISZERO v271b
    0x271e: v271e = ISZERO v271c
    0x271f: v271f(0x272c) = CONST 
    0x2722: JUMPI v271f(0x272c), v271e

    Begin block 0x2723
    prev=[0x2718], succ=[]
    =================================
    0x2723: v2723 = RETURNDATASIZE 
    0x2724: v2724(0x0) = CONST 
    0x2727: RETURNDATACOPY v2724(0x0), v2724(0x0), v2723
    0x2728: v2728 = RETURNDATASIZE 
    0x2729: v2729(0x0) = CONST 
    0x272b: REVERT v2729(0x0), v2728

    Begin block 0x272c
    prev=[0x2718], succ=[0x273e, 0x2742]
    =================================
    0x2731: v2731(0x40) = CONST 
    0x2733: v2733 = MLOAD v2731(0x40)
    0x2734: v2734 = RETURNDATASIZE 
    0x2735: v2735(0x20) = CONST 
    0x2738: v2738 = LT v2734, v2735(0x20)
    0x2739: v2739 = ISZERO v2738
    0x273a: v273a(0x2742) = CONST 
    0x273d: JUMPI v273a(0x2742), v2739

    Begin block 0x273e
    prev=[0x272c], succ=[]
    =================================
    0x273e: v273e(0x0) = CONST 
    0x2741: REVERT v273e(0x0), v273e(0x0)

    Begin block 0x2742
    prev=[0x272c], succ=[0x274a, 0x2787]
    =================================
    0x2744: v2744 = MLOAD v2733
    0x2745: v2745 = ISZERO v2744
    0x2746: v2746(0x2787) = CONST 
    0x2749: JUMPI v2746(0x2787), v2745

    Begin block 0x274a
    prev=[0x2742], succ=[]
    =================================
    0x274a: v274a(0x40) = CONST 
    0x274d: v274d = MLOAD v274a(0x40)
    0x274e: v274e(0xe5) = CONST 
    0x2750: v2750(0x2) = CONST 
    0x2752: v2752(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2750(0x2), v274e(0xe5)
    0x2753: v2753(0x461bcd) = CONST 
    0x2757: v2757(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2753(0x461bcd), v2752(0x2000000000000000000000000000000000000000000000000000000000)
    0x2759: MSTORE v274d, v2757(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x275a: v275a(0x20) = CONST 
    0x275c: v275c(0x4) = CONST 
    0x275f: v275f = ADD v274d, v275c(0x4)
    0x2760: MSTORE v275f, v275a(0x20)
    0x2761: v2761(0x1c) = CONST 
    0x2763: v2763(0x24) = CONST 
    0x2766: v2766 = ADD v274d, v2763(0x24)
    0x2767: MSTORE v2766, v2761(0x1c)
    0x2768: v2768(0x0) = CONST 
    0x276b: v276b = MLOAD v2768(0x0)
    0x276c: v276c(0x20) = CONST 
    0x276e: v276e(0x4a70) = CONST 
    0x2776: MSTORE v2768(0x0), v276b
    0x2777: v2777(0x44) = CONST 
    0x277a: v277a = ADD v274d, v2777(0x44)
    0x277b: MSTORE v277a, v555c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x277d: v277d = MLOAD v274a(0x40)
    0x2781: v2781(0x0) = SUB v274d, v277d
    0x2782: v2782(0x64) = CONST 
    0x2784: v2784(0x64) = ADD v2782(0x64), v2781(0x0)
    0x2786: REVERT v277d, v2784(0x64)
    0x555c: v555c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x2787
    prev=[0x2742], succ=[0x27d5, 0x27d9]
    =================================
    0x2788: v2788(0x3) = CONST 
    0x278a: v278a = SLOAD v2788(0x3)
    0x278b: v278b(0x40) = CONST 
    0x278e: v278e = MLOAD v278b(0x40)
    0x278f: v278f(0xe0) = CONST 
    0x2791: v2791(0x2) = CONST 
    0x2793: v2793(0x100000000000000000000000000000000000000000000000000000000) = EXP v2791(0x2), v278f(0xe0)
    0x2794: v2794(0x7ccce851) = CONST 
    0x2799: v2799(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v2794(0x7ccce851), v2793(0x100000000000000000000000000000000000000000000000000000000)
    0x279b: MSTORE v278e, v2799(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x279c: v279c = CALLER 
    0x279d: v279d(0x4) = CONST 
    0x27a0: v27a0 = ADD v278e, v279d(0x4)
    0x27a3: MSTORE v27a0, v279c
    0x27a5: v27a5 = MLOAD v278b(0x40)
    0x27a8: v27a8(0x1) = CONST 
    0x27aa: v27aa(0xa0) = CONST 
    0x27ac: v27ac(0x2) = CONST 
    0x27ae: v27ae(0x10000000000000000000000000000000000000000) = EXP v27ac(0x2), v27aa(0xa0)
    0x27af: v27af(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27ae(0x10000000000000000000000000000000000000000), v27a8(0x1)
    0x27b0: v27b0 = AND v27af(0xffffffffffffffffffffffffffffffffffffffff), v278a
    0x27b2: v27b2(0x7ccce851) = CONST 
    0x27b8: v27b8(0x24) = CONST 
    0x27bc: v27bc = ADD v278e, v27b8(0x24)
    0x27be: v27be(0x20) = CONST 
    0x27c6: v27c6(0x0) = SUB v278e, v27a5
    0x27c7: v27c7(0x24) = ADD v27c6(0x0), v27b8(0x24)
    0x27c9: v27c9(0x0) = CONST 
    0x27cd: v27cd = EXTCODESIZE v27b0
    0x27ce: v27ce = ISZERO v27cd
    0x27d0: v27d0 = ISZERO v27ce
    0x27d1: v27d1(0x27d9) = CONST 
    0x27d4: JUMPI v27d1(0x27d9), v27d0

    Begin block 0x27d5
    prev=[0x2787], succ=[]
    =================================
    0x27d5: v27d5(0x0) = CONST 
    0x27d8: REVERT v27d5(0x0), v27d5(0x0)

    Begin block 0x27d9
    prev=[0x2787], succ=[0x27e4, 0x27ed]
    =================================
    0x27db: v27db = GAS 
    0x27dc: v27dc = CALL v27db, v27b0, v27c9(0x0), v27a5, v27c7(0x24), v27a5, v27be(0x20)
    0x27dd: v27dd = ISZERO v27dc
    0x27df: v27df = ISZERO v27dd
    0x27e0: v27e0(0x27ed) = CONST 
    0x27e3: JUMPI v27e0(0x27ed), v27df

    Begin block 0x27e4
    prev=[0x27d9], succ=[]
    =================================
    0x27e4: v27e4 = RETURNDATASIZE 
    0x27e5: v27e5(0x0) = CONST 
    0x27e8: RETURNDATACOPY v27e5(0x0), v27e5(0x0), v27e4
    0x27e9: v27e9 = RETURNDATASIZE 
    0x27ea: v27ea(0x0) = CONST 
    0x27ec: REVERT v27ea(0x0), v27e9

    Begin block 0x27ed
    prev=[0x27d9], succ=[0x27ff, 0x2803]
    =================================
    0x27f2: v27f2(0x40) = CONST 
    0x27f4: v27f4 = MLOAD v27f2(0x40)
    0x27f5: v27f5 = RETURNDATASIZE 
    0x27f6: v27f6(0x20) = CONST 
    0x27f9: v27f9 = LT v27f5, v27f6(0x20)
    0x27fa: v27fa = ISZERO v27f9
    0x27fb: v27fb(0x2803) = CONST 
    0x27fe: JUMPI v27fb(0x2803), v27fa

    Begin block 0x27ff
    prev=[0x27ed], succ=[]
    =================================
    0x27ff: v27ff(0x0) = CONST 
    0x2802: REVERT v27ff(0x0), v27ff(0x0)

    Begin block 0x2803
    prev=[0x27ed], succ=[0x280b, 0x2848]
    =================================
    0x2805: v2805 = MLOAD v27f4
    0x2806: v2806 = ISZERO v2805
    0x2807: v2807(0x2848) = CONST 
    0x280a: JUMPI v2807(0x2848), v2806

    Begin block 0x280b
    prev=[0x2803], succ=[]
    =================================
    0x280b: v280b(0x40) = CONST 
    0x280e: v280e = MLOAD v280b(0x40)
    0x280f: v280f(0xe5) = CONST 
    0x2811: v2811(0x2) = CONST 
    0x2813: v2813(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2811(0x2), v280f(0xe5)
    0x2814: v2814(0x461bcd) = CONST 
    0x2818: v2818(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2814(0x461bcd), v2813(0x2000000000000000000000000000000000000000000000000000000000)
    0x281a: MSTORE v280e, v2818(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x281b: v281b(0x20) = CONST 
    0x281d: v281d(0x4) = CONST 
    0x2820: v2820 = ADD v280e, v281d(0x4)
    0x2821: MSTORE v2820, v281b(0x20)
    0x2822: v2822(0x1c) = CONST 
    0x2824: v2824(0x24) = CONST 
    0x2827: v2827 = ADD v280e, v2824(0x24)
    0x2828: MSTORE v2827, v2822(0x1c)
    0x2829: v2829(0x0) = CONST 
    0x282c: v282c = MLOAD v2829(0x0)
    0x282d: v282d(0x20) = CONST 
    0x282f: v282f(0x4a70) = CONST 
    0x2837: MSTORE v2829(0x0), v282c
    0x2838: v2838(0x44) = CONST 
    0x283b: v283b = ADD v280e, v2838(0x44)
    0x283c: MSTORE v283b, v5561(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x283e: v283e = MLOAD v280b(0x40)
    0x2842: v2842(0x0) = SUB v280e, v283e
    0x2843: v2843(0x64) = CONST 
    0x2845: v2845(0x64) = ADD v2843(0x64), v2842(0x0)
    0x2847: REVERT v283e, v2845(0x64)
    0x5561: v5561(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x2848
    prev=[0x2803], succ=[0x285b, 0x285f]
    =================================
    0x2849: v2849(0x1) = CONST 
    0x284b: v284b = SLOAD v2849(0x1)
    0x284c: v284c(0xa0) = CONST 
    0x284e: v284e(0x2) = CONST 
    0x2850: v2850(0x10000000000000000000000000000000000000000) = EXP v284e(0x2), v284c(0xa0)
    0x2852: v2852 = DIV v284b, v2850(0x10000000000000000000000000000000000000000)
    0x2853: v2853(0xff) = CONST 
    0x2855: v2855 = AND v2853(0xff), v2852
    0x2856: v2856 = ISZERO v2855
    0x2857: v2857(0x285f) = CONST 
    0x285a: JUMPI v2857(0x285f), v2856

    Begin block 0x285b
    prev=[0x2848], succ=[]
    =================================
    0x285b: v285b(0x0) = CONST 
    0x285e: REVERT v285b(0x0), v285b(0x0)

    Begin block 0x285f
    prev=[0x2848], succ=[0x5385]
    =================================
    0x2860: v2860(0x5385) = CONST 
    0x2864: v2864 = CALLER 
    0x2866: v2866(0x4176) = CONST 
    0x2869: CALLPRIVATE v2866(0x4176), v690, v2864, v68d, v2860(0x5385)

    Begin block 0x5385
    prev=[0x285f], succ=[0x4f6f]
    =================================
    0x5387: v5387(0x1) = CONST 
    0x538f: JUMP v67f(0x4f6f)

    Begin block 0x4f6f
    prev=[0x5385], succ=[]
    =================================
    0x4f70: v4f70(0x40) = CONST 
    0x4f73: v4f73 = MLOAD v4f70(0x40)
    0x4f75: v4f75 = ISZERO v5387(0x1)
    0x4f76: v4f76 = ISZERO v4f75
    0x4f78: MSTORE v4f73, v4f76
    0x4f79: v4f79 = MLOAD v4f70(0x40)
    0x4f7d: v4f7d(0x0) = SUB v4f73, v4f79
    0x4f7e: v4f7e(0x20) = CONST 
    0x4f80: v4f80(0x20) = ADD v4f7e(0x20), v4f7d(0x0)
    0x4f82: RETURN v4f79, v4f80(0x20)

}

function unlistToken(address)() public {
    Begin block 0x695
    prev=[], succ=[0x69d, 0x6a1]
    =================================
    0x696: v696 = CALLVALUE 
    0x698: v698 = ISZERO v696
    0x699: v699(0x6a1) = CONST 
    0x69c: JUMPI v699(0x6a1), v698

    Begin block 0x69d
    prev=[0x695], succ=[]
    =================================
    0x69d: v69d(0x0) = CONST 
    0x6a0: REVERT v69d(0x0), v69d(0x0)

    Begin block 0x6a1
    prev=[0x695], succ=[0x286aB0x6a1]
    =================================
    0x6a3: v6a3(0x4fa2) = CONST 
    0x6a6: v6a6(0x1) = CONST 
    0x6a8: v6a8(0xa0) = CONST 
    0x6aa: v6aa(0x2) = CONST 
    0x6ac: v6ac(0x10000000000000000000000000000000000000000) = EXP v6aa(0x2), v6a8(0xa0)
    0x6ad: v6ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ac(0x10000000000000000000000000000000000000000), v6a6(0x1)
    0x6ae: v6ae(0x4) = CONST 
    0x6b0: v6b0 = CALLDATALOAD v6ae(0x4)
    0x6b1: v6b1 = AND v6b0, v6ad(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b2: v6b2(0x286a) = CONST 
    0x6b5: JUMP v6b2(0x286a), v6b1, v6a3(0x4fa2)

    Begin block 0x286aB0x6a1
    prev=[0x6a1], succ=[0x287dB0x6a1, 0x2881B0x6a1]
    =================================
    0x286bS0x6a1: v286bV6a1(0x0) = CONST 
    0x286dS0x6a1: v286dV6a1 = SLOAD v286bV6a1(0x0)
    0x286eS0x6a1: v286eV6a1(0x1) = CONST 
    0x2870S0x6a1: v2870V6a1(0xa0) = CONST 
    0x2872S0x6a1: v2872V6a1(0x2) = CONST 
    0x2874S0x6a1: v2874V6a1(0x10000000000000000000000000000000000000000) = EXP v2872V6a1(0x2), v2870V6a1(0xa0)
    0x2875S0x6a1: v2875V6a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2874V6a1(0x10000000000000000000000000000000000000000), v286eV6a1(0x1)
    0x2876S0x6a1: v2876V6a1 = AND v2875V6a1(0xffffffffffffffffffffffffffffffffffffffff), v286dV6a1
    0x2877S0x6a1: v2877V6a1 = CALLER 
    0x2878S0x6a1: v2878V6a1 = EQ v2877V6a1, v2876V6a1
    0x2879S0x6a1: v2879V6a1(0x2881) = CONST 
    0x287cS0x6a1: JUMPI v2879V6a1(0x2881), v2878V6a1

    Begin block 0x287dB0x6a1
    prev=[0x286aB0x6a1], succ=[]
    =================================
    0x287dS0x6a1: v287dV6a1(0x0) = CONST 
    0x2880S0x6a1: REVERT v287dV6a1(0x0), v287dV6a1(0x0)

    Begin block 0x2881B0x6a1
    prev=[0x286aB0x6a1], succ=[0x2894B0x6a1, 0x2898B0x6a1]
    =================================
    0x2882S0x6a1: v2882V6a1(0x1) = CONST 
    0x2884S0x6a1: v2884V6a1 = SLOAD v2882V6a1(0x1)
    0x2885S0x6a1: v2885V6a1(0xa0) = CONST 
    0x2887S0x6a1: v2887V6a1(0x2) = CONST 
    0x2889S0x6a1: v2889V6a1(0x10000000000000000000000000000000000000000) = EXP v2887V6a1(0x2), v2885V6a1(0xa0)
    0x288bS0x6a1: v288bV6a1 = DIV v2884V6a1, v2889V6a1(0x10000000000000000000000000000000000000000)
    0x288cS0x6a1: v288cV6a1(0xff) = CONST 
    0x288eS0x6a1: v288eV6a1 = AND v288cV6a1(0xff), v288bV6a1
    0x288fS0x6a1: v288fV6a1 = ISZERO v288eV6a1
    0x2890S0x6a1: v2890V6a1(0x2898) = CONST 
    0x2893S0x6a1: JUMPI v2890V6a1(0x2898), v288fV6a1

    Begin block 0x2894B0x6a1
    prev=[0x2881B0x6a1], succ=[]
    =================================
    0x2894S0x6a1: v2894V6a1(0x0) = CONST 
    0x2897S0x6a1: REVERT v2894V6a1(0x0), v2894V6a1(0x0)

    Begin block 0x2898B0x6a1
    prev=[0x2881B0x6a1], succ=[0x28ffB0x6a1, 0x11fc0x286aB0x6a1]
    =================================
    0x2899S0x6a1: v2899V6a1(0x4) = CONST 
    0x289cS0x6a1: v289cV6a1 = SLOAD v2899V6a1(0x4)
    0x289dS0x6a1: v289dV6a1(0x40) = CONST 
    0x28a0S0x6a1: v28a0V6a1 = MLOAD v289dV6a1(0x40)
    0x28a1S0x6a1: v28a1V6a1(0x3b947d2b00000000000000000000000000000000000000000000000000000000) = CONST 
    0x28c3S0x6a1: MSTORE v28a0V6a1, v28a1V6a1(0x3b947d2b00000000000000000000000000000000000000000000000000000000)
    0x28c4S0x6a1: v28c4V6a1(0x1) = CONST 
    0x28c6S0x6a1: v28c6V6a1(0xa0) = CONST 
    0x28c8S0x6a1: v28c8V6a1(0x2) = CONST 
    0x28caS0x6a1: v28caV6a1(0x10000000000000000000000000000000000000000) = EXP v28c8V6a1(0x2), v28c6V6a1(0xa0)
    0x28cbS0x6a1: v28cbV6a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v28caV6a1(0x10000000000000000000000000000000000000000), v28c4V6a1(0x1)
    0x28ceS0x6a1: v28ceV6a1 = AND v28cbV6a1(0xffffffffffffffffffffffffffffffffffffffff), v6b1
    0x28d1S0x6a1: v28d1V6a1 = ADD v28a0V6a1, v2899V6a1(0x4)
    0x28d5S0x6a1: MSTORE v28d1V6a1, v28ceV6a1
    0x28d7S0x6a1: v28d7V6a1 = MLOAD v289dV6a1(0x40)
    0x28dbS0x6a1: v28dbV6a1 = AND v289cV6a1, v28cbV6a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x28ddS0x6a1: v28ddV6a1(0x3b947d2b) = CONST 
    0x28e3S0x6a1: v28e3V6a1(0x24) = CONST 
    0x28e7S0x6a1: v28e7V6a1 = ADD v28a0V6a1, v28e3V6a1(0x24)
    0x28e9S0x6a1: v28e9V6a1(0x0) = CONST 
    0x28f1S0x6a1: v28f1V6a1(0x0) = SUB v28a0V6a1, v28d7V6a1
    0x28f2S0x6a1: v28f2V6a1(0x24) = ADD v28f1V6a1(0x0), v28e3V6a1(0x24)
    0x28f7S0x6a1: v28f7V6a1 = EXTCODESIZE v28dbV6a1
    0x28f8S0x6a1: v28f8V6a1 = ISZERO v28f7V6a1
    0x28faS0x6a1: v28faV6a1 = ISZERO v28f8V6a1
    0x28fbS0x6a1: v28fbV6a1(0x11fc) = CONST 
    0x28feS0x6a1: JUMPI v28fbV6a1(0x11fc), v28faV6a1

    Begin block 0x28ffB0x6a1
    prev=[0x2898B0x6a1], succ=[]
    =================================
    0x28ffS0x6a1: v28ffV6a1(0x0) = CONST 
    0x2902S0x6a1: REVERT v28ffV6a1(0x0), v28ffV6a1(0x0)

    Begin block 0x11fc0x286aB0x6a1
    prev=[0x2898B0x6a1], succ=[0x12070x286aB0x6a1, 0x12100x286aB0x6a1]
    =================================
    0x11fe0x286aS0x6a1: v286a11feV6a1 = GAS 
    0x11ff0x286aS0x6a1: v286a11ffV6a1 = CALL v286a11feV6a1, v28dbV6a1, v28e9V6a1(0x0), v28d7V6a1, v28f2V6a1(0x24), v28d7V6a1, v28e9V6a1(0x0)
    0x12000x286aS0x6a1: v286a1200V6a1 = ISZERO v286a11ffV6a1
    0x12020x286aS0x6a1: v286a1202V6a1 = ISZERO v286a1200V6a1
    0x12030x286aS0x6a1: v286a1203V6a1(0x1210) = CONST 
    0x12060x286aS0x6a1: JUMPI v286a1203V6a1(0x1210), v286a1202V6a1

    Begin block 0x12070x286aB0x6a1
    prev=[0x11fc0x286aB0x6a1], succ=[]
    =================================
    0x12070x286aS0x6a1: v286a1207V6a1 = RETURNDATASIZE 
    0x12080x286aS0x6a1: v286a1208V6a1(0x0) = CONST 
    0x120b0x286aS0x6a1: RETURNDATACOPY v286a1208V6a1(0x0), v286a1208V6a1(0x0), v286a1207V6a1
    0x120c0x286aS0x6a1: v286a120cV6a1 = RETURNDATASIZE 
    0x120d0x286aS0x6a1: v286a120dV6a1(0x0) = CONST 
    0x120f0x286aS0x6a1: REVERT v286a120dV6a1(0x0), v286a120cV6a1

    Begin block 0x12100x286aB0x6a1
    prev=[0x11fc0x286aB0x6a1], succ=[0x4fa2]
    =================================
    0x12160x286aS0x6a1: JUMP v6a3(0x4fa2)

    Begin block 0x4fa2
    prev=[0x12100x286aB0x6a1], succ=[]
    =================================
    0x4fa3: STOP 

}

function tokenStorage()() public {
    Begin block 0x6b6
    prev=[], succ=[0x6be, 0x6c2]
    =================================
    0x6b7: v6b7 = CALLVALUE 
    0x6b9: v6b9 = ISZERO v6b7
    0x6ba: v6ba(0x6c2) = CONST 
    0x6bd: JUMPI v6ba(0x6c2), v6b9

    Begin block 0x6be
    prev=[0x6b6], succ=[]
    =================================
    0x6be: v6be(0x0) = CONST 
    0x6c1: REVERT v6be(0x0), v6be(0x0)

    Begin block 0x6c2
    prev=[0x6b6], succ=[0x2903]
    =================================
    0x6c4: v6c4(0x4fc3) = CONST 
    0x6c7: v6c7(0x2903) = CONST 
    0x6ca: JUMP v6c7(0x2903)

    Begin block 0x2903
    prev=[0x6c2], succ=[0x4fc3]
    =================================
    0x2904: v2904(0x2) = CONST 
    0x2906: v2906 = SLOAD v2904(0x2)
    0x2907: v2907(0x1) = CONST 
    0x2909: v2909(0xa0) = CONST 
    0x290b: v290b(0x2) = CONST 
    0x290d: v290d(0x10000000000000000000000000000000000000000) = EXP v290b(0x2), v2909(0xa0)
    0x290e: v290e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v290d(0x10000000000000000000000000000000000000000), v2907(0x1)
    0x290f: v290f = AND v290e(0xffffffffffffffffffffffffffffffffffffffff), v2906
    0x2911: JUMP v6c4(0x4fc3)

    Begin block 0x4fc3
    prev=[0x2903], succ=[]
    =================================
    0x4fc4: v4fc4(0x40) = CONST 
    0x4fc7: v4fc7 = MLOAD v4fc4(0x40)
    0x4fc8: v4fc8(0x1) = CONST 
    0x4fca: v4fca(0xa0) = CONST 
    0x4fcc: v4fcc(0x2) = CONST 
    0x4fce: v4fce(0x10000000000000000000000000000000000000000) = EXP v4fcc(0x2), v4fca(0xa0)
    0x4fcf: v4fcf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4fce(0x10000000000000000000000000000000000000000), v4fc8(0x1)
    0x4fd2: v4fd2 = AND v290f, v4fcf(0xffffffffffffffffffffffffffffffffffffffff)
    0x4fd4: MSTORE v4fc7, v4fd2
    0x4fd5: v4fd5 = MLOAD v4fc4(0x40)
    0x4fd9: v4fd9(0x0) = SUB v4fc7, v4fd5
    0x4fda: v4fda(0x20) = CONST 
    0x4fdc: v4fdc(0x20) = ADD v4fda(0x20), v4fd9(0x0)
    0x4fde: RETURN v4fd5, v4fdc(0x20)

}

function getFee(address)() public {
    Begin block 0x6cb
    prev=[], succ=[0x6d3, 0x6d7]
    =================================
    0x6cc: v6cc = CALLVALUE 
    0x6ce: v6ce = ISZERO v6cc
    0x6cf: v6cf(0x6d7) = CONST 
    0x6d2: JUMPI v6cf(0x6d7), v6ce

    Begin block 0x6d3
    prev=[0x6cb], succ=[]
    =================================
    0x6d3: v6d3(0x0) = CONST 
    0x6d6: REVERT v6d3(0x0), v6d3(0x0)

    Begin block 0x6d7
    prev=[0x6cb], succ=[0x4ffe]
    =================================
    0x6d9: v6d9(0x4ffe) = CONST 
    0x6dc: v6dc(0x1) = CONST 
    0x6de: v6de(0xa0) = CONST 
    0x6e0: v6e0(0x2) = CONST 
    0x6e2: v6e2(0x10000000000000000000000000000000000000000) = EXP v6e0(0x2), v6de(0xa0)
    0x6e3: v6e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e2(0x10000000000000000000000000000000000000000), v6dc(0x1)
    0x6e4: v6e4(0x4) = CONST 
    0x6e6: v6e6 = CALLDATALOAD v6e4(0x4)
    0x6e7: v6e7 = AND v6e6, v6e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x6e8: v6e8(0x2912) = CONST 
    0x6eb: v6eb_0 = CALLPRIVATE v6e8(0x2912), v6e7, v6d9(0x4ffe)

    Begin block 0x4ffe
    prev=[0x6d7], succ=[]
    =================================
    0x4fff: v4fff(0x40) = CONST 
    0x5002: v5002 = MLOAD v4fff(0x40)
    0x5005: MSTORE v5002, v6eb_0
    0x5006: v5006 = MLOAD v4fff(0x40)
    0x500a: v500a(0x0) = SUB v5002, v5006
    0x500b: v500b(0x20) = CONST 
    0x500d: v500d(0x20) = ADD v500b(0x20), v500a(0x0)
    0x500f: RETURN v5006, v500d(0x20)

}

function burnCarbonDollar(address,uint256)() public {
    Begin block 0x6ec
    prev=[], succ=[0x6f4, 0x6f8]
    =================================
    0x6ed: v6ed = CALLVALUE 
    0x6ef: v6ef = ISZERO v6ed
    0x6f0: v6f0(0x6f8) = CONST 
    0x6f3: JUMPI v6f0(0x6f8), v6ef

    Begin block 0x6f4
    prev=[0x6ec], succ=[]
    =================================
    0x6f4: v6f4(0x0) = CONST 
    0x6f7: REVERT v6f4(0x0), v6f4(0x0)

    Begin block 0x6f8
    prev=[0x6ec], succ=[0x297fB0x6f8]
    =================================
    0x6fa: v6fa(0x502f) = CONST 
    0x6fd: v6fd(0x1) = CONST 
    0x6ff: v6ff(0xa0) = CONST 
    0x701: v701(0x2) = CONST 
    0x703: v703(0x10000000000000000000000000000000000000000) = EXP v701(0x2), v6ff(0xa0)
    0x704: v704(0xffffffffffffffffffffffffffffffffffffffff) = SUB v703(0x10000000000000000000000000000000000000000), v6fd(0x1)
    0x705: v705(0x4) = CONST 
    0x707: v707 = CALLDATALOAD v705(0x4)
    0x708: v708 = AND v707, v704(0xffffffffffffffffffffffffffffffffffffffff)
    0x709: v709(0x24) = CONST 
    0x70b: v70b = CALLDATALOAD v709(0x24)
    0x70c: v70c(0x297f) = CONST 
    0x70f: JUMP v70c(0x297f), v70b, v708, v6fa(0x502f)

    Begin block 0x297fB0x6f8
    prev=[0x6f8], succ=[0x29cdB0x6f8, 0x29d1B0x6f8]
    =================================
    0x2980S0x6f8: v2980V6f8(0x3) = CONST 
    0x2982S0x6f8: v2982V6f8 = SLOAD v2980V6f8(0x3)
    0x2983S0x6f8: v2983V6f8(0x40) = CONST 
    0x2986S0x6f8: v2986V6f8 = MLOAD v2983V6f8(0x40)
    0x2987S0x6f8: v2987V6f8(0xe0) = CONST 
    0x2989S0x6f8: v2989V6f8(0x2) = CONST 
    0x298bS0x6f8: v298bV6f8(0x100000000000000000000000000000000000000000000000000000000) = EXP v2989V6f8(0x2), v2987V6f8(0xe0)
    0x298cS0x6f8: v298cV6f8(0x7ccce851) = CONST 
    0x2991S0x6f8: v2991V6f8(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v298cV6f8(0x7ccce851), v298bV6f8(0x100000000000000000000000000000000000000000000000000000000)
    0x2993S0x6f8: MSTORE v2986V6f8, v2991V6f8(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x2994S0x6f8: v2994V6f8 = CALLER 
    0x2995S0x6f8: v2995V6f8(0x4) = CONST 
    0x2998S0x6f8: v2998V6f8 = ADD v2986V6f8, v2995V6f8(0x4)
    0x299bS0x6f8: MSTORE v2998V6f8, v2994V6f8
    0x299dS0x6f8: v299dV6f8 = MLOAD v2983V6f8(0x40)
    0x29a0S0x6f8: v29a0V6f8(0x1) = CONST 
    0x29a2S0x6f8: v29a2V6f8(0xa0) = CONST 
    0x29a4S0x6f8: v29a4V6f8(0x2) = CONST 
    0x29a6S0x6f8: v29a6V6f8(0x10000000000000000000000000000000000000000) = EXP v29a4V6f8(0x2), v29a2V6f8(0xa0)
    0x29a7S0x6f8: v29a7V6f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29a6V6f8(0x10000000000000000000000000000000000000000), v29a0V6f8(0x1)
    0x29a8S0x6f8: v29a8V6f8 = AND v29a7V6f8(0xffffffffffffffffffffffffffffffffffffffff), v2982V6f8
    0x29aaS0x6f8: v29aaV6f8(0x7ccce851) = CONST 
    0x29b0S0x6f8: v29b0V6f8(0x24) = CONST 
    0x29b4S0x6f8: v29b4V6f8 = ADD v2986V6f8, v29b0V6f8(0x24)
    0x29b6S0x6f8: v29b6V6f8(0x20) = CONST 
    0x29beS0x6f8: v29beV6f8(0x0) = SUB v2986V6f8, v299dV6f8
    0x29bfS0x6f8: v29bfV6f8(0x24) = ADD v29beV6f8(0x0), v29b0V6f8(0x24)
    0x29c1S0x6f8: v29c1V6f8(0x0) = CONST 
    0x29c5S0x6f8: v29c5V6f8 = EXTCODESIZE v29a8V6f8
    0x29c6S0x6f8: v29c6V6f8 = ISZERO v29c5V6f8
    0x29c8S0x6f8: v29c8V6f8 = ISZERO v29c6V6f8
    0x29c9S0x6f8: v29c9V6f8(0x29d1) = CONST 
    0x29ccS0x6f8: JUMPI v29c9V6f8(0x29d1), v29c8V6f8

    Begin block 0x29cdB0x6f8
    prev=[0x297fB0x6f8], succ=[]
    =================================
    0x29cdS0x6f8: v29cdV6f8(0x0) = CONST 
    0x29d0S0x6f8: REVERT v29cdV6f8(0x0), v29cdV6f8(0x0)

    Begin block 0x29d1B0x6f8
    prev=[0x297fB0x6f8], succ=[0x29dcB0x6f8, 0x29e5B0x6f8]
    =================================
    0x29d3S0x6f8: v29d3V6f8 = GAS 
    0x29d4S0x6f8: v29d4V6f8 = CALL v29d3V6f8, v29a8V6f8, v29c1V6f8(0x0), v299dV6f8, v29bfV6f8(0x24), v299dV6f8, v29b6V6f8(0x20)
    0x29d5S0x6f8: v29d5V6f8 = ISZERO v29d4V6f8
    0x29d7S0x6f8: v29d7V6f8 = ISZERO v29d5V6f8
    0x29d8S0x6f8: v29d8V6f8(0x29e5) = CONST 
    0x29dbS0x6f8: JUMPI v29d8V6f8(0x29e5), v29d7V6f8

    Begin block 0x29dcB0x6f8
    prev=[0x29d1B0x6f8], succ=[]
    =================================
    0x29dcS0x6f8: v29dcV6f8 = RETURNDATASIZE 
    0x29ddS0x6f8: v29ddV6f8(0x0) = CONST 
    0x29e0S0x6f8: RETURNDATACOPY v29ddV6f8(0x0), v29ddV6f8(0x0), v29dcV6f8
    0x29e1S0x6f8: v29e1V6f8 = RETURNDATASIZE 
    0x29e2S0x6f8: v29e2V6f8(0x0) = CONST 
    0x29e4S0x6f8: REVERT v29e2V6f8(0x0), v29e1V6f8

    Begin block 0x29e5B0x6f8
    prev=[0x29d1B0x6f8], succ=[0x29f7B0x6f8, 0x29fbB0x6f8]
    =================================
    0x29eaS0x6f8: v29eaV6f8(0x40) = CONST 
    0x29ecS0x6f8: v29ecV6f8 = MLOAD v29eaV6f8(0x40)
    0x29edS0x6f8: v29edV6f8 = RETURNDATASIZE 
    0x29eeS0x6f8: v29eeV6f8(0x20) = CONST 
    0x29f1S0x6f8: v29f1V6f8 = LT v29edV6f8, v29eeV6f8(0x20)
    0x29f2S0x6f8: v29f2V6f8 = ISZERO v29f1V6f8
    0x29f3S0x6f8: v29f3V6f8(0x29fb) = CONST 
    0x29f6S0x6f8: JUMPI v29f3V6f8(0x29fb), v29f2V6f8

    Begin block 0x29f7B0x6f8
    prev=[0x29e5B0x6f8], succ=[]
    =================================
    0x29f7S0x6f8: v29f7V6f8(0x0) = CONST 
    0x29faS0x6f8: REVERT v29f7V6f8(0x0), v29f7V6f8(0x0)

    Begin block 0x29fbB0x6f8
    prev=[0x29e5B0x6f8], succ=[0x2a03B0x6f8, 0x2a40B0x6f8]
    =================================
    0x29fdS0x6f8: v29fdV6f8 = MLOAD v29ecV6f8
    0x29feS0x6f8: v29feV6f8 = ISZERO v29fdV6f8
    0x29ffS0x6f8: v29ffV6f8(0x2a40) = CONST 
    0x2a02S0x6f8: JUMPI v29ffV6f8(0x2a40), v29feV6f8

    Begin block 0x2a03B0x6f8
    prev=[0x29fbB0x6f8], succ=[]
    =================================
    0x2a03S0x6f8: v2a03V6f8(0x40) = CONST 
    0x2a06S0x6f8: v2a06V6f8 = MLOAD v2a03V6f8(0x40)
    0x2a07S0x6f8: v2a07V6f8(0xe5) = CONST 
    0x2a09S0x6f8: v2a09V6f8(0x2) = CONST 
    0x2a0bS0x6f8: v2a0bV6f8(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2a09V6f8(0x2), v2a07V6f8(0xe5)
    0x2a0cS0x6f8: v2a0cV6f8(0x461bcd) = CONST 
    0x2a10S0x6f8: v2a10V6f8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2a0cV6f8(0x461bcd), v2a0bV6f8(0x2000000000000000000000000000000000000000000000000000000000)
    0x2a12S0x6f8: MSTORE v2a06V6f8, v2a10V6f8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a13S0x6f8: v2a13V6f8(0x20) = CONST 
    0x2a15S0x6f8: v2a15V6f8(0x4) = CONST 
    0x2a18S0x6f8: v2a18V6f8 = ADD v2a06V6f8, v2a15V6f8(0x4)
    0x2a19S0x6f8: MSTORE v2a18V6f8, v2a13V6f8(0x20)
    0x2a1aS0x6f8: v2a1aV6f8(0x1c) = CONST 
    0x2a1cS0x6f8: v2a1cV6f8(0x24) = CONST 
    0x2a1fS0x6f8: v2a1fV6f8 = ADD v2a06V6f8, v2a1cV6f8(0x24)
    0x2a20S0x6f8: MSTORE v2a1fV6f8, v2a1aV6f8(0x1c)
    0x2a21S0x6f8: v2a21V6f8(0x0) = CONST 
    0x2a24S0x6f8: v2a24V6f8 = MLOAD v2a21V6f8(0x0)
    0x2a25S0x6f8: v2a25V6f8(0x20) = CONST 
    0x2a27S0x6f8: v2a27V6f8(0x4a70) = CONST 
    0x2a2fS0x6f8: MSTORE v2a21V6f8(0x0), v2a24V6f8
    0x2a30S0x6f8: v2a30V6f8(0x44) = CONST 
    0x2a33S0x6f8: v2a33V6f8 = ADD v2a06V6f8, v2a30V6f8(0x44)
    0x2a34S0x6f8: MSTORE v2a33V6f8, v5566V6f8(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x2a36S0x6f8: v2a36V6f8 = MLOAD v2a03V6f8(0x40)
    0x2a3aS0x6f8: v2a3aV6f8(0x0) = SUB v2a06V6f8, v2a36V6f8
    0x2a3bS0x6f8: v2a3bV6f8(0x64) = CONST 
    0x2a3dS0x6f8: v2a3dV6f8(0x64) = ADD v2a3bV6f8(0x64), v2a3aV6f8(0x0)
    0x2a3fS0x6f8: REVERT v2a36V6f8, v2a3dV6f8(0x64)
    0x5566S0x6f8: v5566V6f8(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x2a40B0x6f8
    prev=[0x29fbB0x6f8], succ=[0x2a53B0x6f8, 0x2a57B0x6f8]
    =================================
    0x2a41S0x6f8: v2a41V6f8(0x1) = CONST 
    0x2a43S0x6f8: v2a43V6f8 = SLOAD v2a41V6f8(0x1)
    0x2a44S0x6f8: v2a44V6f8(0xa0) = CONST 
    0x2a46S0x6f8: v2a46V6f8(0x2) = CONST 
    0x2a48S0x6f8: v2a48V6f8(0x10000000000000000000000000000000000000000) = EXP v2a46V6f8(0x2), v2a44V6f8(0xa0)
    0x2a4aS0x6f8: v2a4aV6f8 = DIV v2a43V6f8, v2a48V6f8(0x10000000000000000000000000000000000000000)
    0x2a4bS0x6f8: v2a4bV6f8(0xff) = CONST 
    0x2a4dS0x6f8: v2a4dV6f8 = AND v2a4bV6f8(0xff), v2a4aV6f8
    0x2a4eS0x6f8: v2a4eV6f8 = ISZERO v2a4dV6f8
    0x2a4fS0x6f8: v2a4fV6f8(0x2a57) = CONST 
    0x2a52S0x6f8: JUMPI v2a4fV6f8(0x2a57), v2a4eV6f8

    Begin block 0x2a53B0x6f8
    prev=[0x2a40B0x6f8], succ=[]
    =================================
    0x2a53S0x6f8: v2a53V6f8(0x0) = CONST 
    0x2a56S0x6f8: REVERT v2a53V6f8(0x0), v2a53V6f8(0x0)

    Begin block 0x2a57B0x6f8
    prev=[0x2a40B0x6f8], succ=[0x2a62B0x6f8]
    =================================
    0x2a58S0x6f8: v2a58V6f8(0x2a62) = CONST 
    0x2a5bS0x6f8: v2a5bV6f8 = CALLER 
    0x2a5eS0x6f8: v2a5eV6f8(0x473f) = CONST 
    0x2a61S0x6f8: CALLPRIVATE v2a5eV6f8(0x473f), v70b, v708, v2a5bV6f8, v2a58V6f8(0x2a62)

    Begin block 0x2a62B0x6f8
    prev=[0x2a57B0x6f8], succ=[0x502f]
    =================================
    0x2a66S0x6f8: JUMP v6fa(0x502f)

    Begin block 0x502f
    prev=[0x2a62B0x6f8], succ=[]
    =================================
    0x5030: STOP 

}

function metaTransferHash(address,uint256,uint256,uint256)() public {
    Begin block 0x710
    prev=[], succ=[0x718, 0x71c]
    =================================
    0x711: v711 = CALLVALUE 
    0x713: v713 = ISZERO v711
    0x714: v714(0x71c) = CONST 
    0x717: JUMPI v714(0x71c), v713

    Begin block 0x718
    prev=[0x710], succ=[]
    =================================
    0x718: v718(0x0) = CONST 
    0x71b: REVERT v718(0x0), v718(0x0)

    Begin block 0x71c
    prev=[0x710], succ=[0x5050]
    =================================
    0x71e: v71e(0x5050) = CONST 
    0x721: v721(0x1) = CONST 
    0x723: v723(0xa0) = CONST 
    0x725: v725(0x2) = CONST 
    0x727: v727(0x10000000000000000000000000000000000000000) = EXP v725(0x2), v723(0xa0)
    0x728: v728(0xffffffffffffffffffffffffffffffffffffffff) = SUB v727(0x10000000000000000000000000000000000000000), v721(0x1)
    0x729: v729(0x4) = CONST 
    0x72b: v72b = CALLDATALOAD v729(0x4)
    0x72c: v72c = AND v72b, v728(0xffffffffffffffffffffffffffffffffffffffff)
    0x72d: v72d(0x24) = CONST 
    0x72f: v72f = CALLDATALOAD v72d(0x24)
    0x730: v730(0x44) = CONST 
    0x732: v732 = CALLDATALOAD v730(0x44)
    0x733: v733(0x64) = CONST 
    0x735: v735 = CALLDATALOAD v733(0x64)
    0x736: v736(0x2a67) = CONST 
    0x739: v739_0 = CALLPRIVATE v736(0x2a67), v735, v732, v72f, v72c, v71e(0x5050)

    Begin block 0x5050
    prev=[0x71c], succ=[]
    =================================
    0x5051: v5051(0x40) = CONST 
    0x5054: v5054 = MLOAD v5051(0x40)
    0x5057: MSTORE v5054, v739_0
    0x5058: v5058 = MLOAD v5051(0x40)
    0x505c: v505c(0x0) = SUB v5054, v5058
    0x505d: v505d(0x20) = CONST 
    0x505f: v505f(0x20) = ADD v505d(0x20), v505c(0x0)
    0x5061: RETURN v5058, v505f(0x20)

}

function destroyBlacklistedTokens(address,uint256)() public {
    Begin block 0x73a
    prev=[], succ=[0x742, 0x746]
    =================================
    0x73b: v73b = CALLVALUE 
    0x73d: v73d = ISZERO v73b
    0x73e: v73e(0x746) = CONST 
    0x741: JUMPI v73e(0x746), v73d

    Begin block 0x742
    prev=[0x73a], succ=[]
    =================================
    0x742: v742(0x0) = CONST 
    0x745: REVERT v742(0x0), v742(0x0)

    Begin block 0x746
    prev=[0x73a], succ=[0x2b13]
    =================================
    0x748: v748(0x5081) = CONST 
    0x74b: v74b(0x1) = CONST 
    0x74d: v74d(0xa0) = CONST 
    0x74f: v74f(0x2) = CONST 
    0x751: v751(0x10000000000000000000000000000000000000000) = EXP v74f(0x2), v74d(0xa0)
    0x752: v752(0xffffffffffffffffffffffffffffffffffffffff) = SUB v751(0x10000000000000000000000000000000000000000), v74b(0x1)
    0x753: v753(0x4) = CONST 
    0x755: v755 = CALLDATALOAD v753(0x4)
    0x756: v756 = AND v755, v752(0xffffffffffffffffffffffffffffffffffffffff)
    0x757: v757(0x24) = CONST 
    0x759: v759 = CALLDATALOAD v757(0x24)
    0x75a: v75a(0x2b13) = CONST 
    0x75d: JUMP v75a(0x2b13)

    Begin block 0x2b13
    prev=[0x746], succ=[0x2b64, 0x2b68]
    =================================
    0x2b14: v2b14(0x3) = CONST 
    0x2b16: v2b16 = SLOAD v2b14(0x3)
    0x2b17: v2b17(0x40) = CONST 
    0x2b1a: v2b1a = MLOAD v2b17(0x40)
    0x2b1b: v2b1b(0xe0) = CONST 
    0x2b1d: v2b1d(0x2) = CONST 
    0x2b1f: v2b1f(0x100000000000000000000000000000000000000000000000000000000) = EXP v2b1d(0x2), v2b1b(0xe0)
    0x2b20: v2b20(0x7ccce851) = CONST 
    0x2b25: v2b25(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v2b20(0x7ccce851), v2b1f(0x100000000000000000000000000000000000000000000000000000000)
    0x2b27: MSTORE v2b1a, v2b25(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x2b28: v2b28(0x1) = CONST 
    0x2b2a: v2b2a(0xa0) = CONST 
    0x2b2c: v2b2c(0x2) = CONST 
    0x2b2e: v2b2e(0x10000000000000000000000000000000000000000) = EXP v2b2c(0x2), v2b2a(0xa0)
    0x2b2f: v2b2f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b2e(0x10000000000000000000000000000000000000000), v2b28(0x1)
    0x2b32: v2b32 = AND v756, v2b2f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b33: v2b33(0x4) = CONST 
    0x2b36: v2b36 = ADD v2b1a, v2b33(0x4)
    0x2b37: MSTORE v2b36, v2b32
    0x2b39: v2b39 = MLOAD v2b17(0x40)
    0x2b3f: v2b3f = AND v2b16, v2b2f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b41: v2b41(0x7ccce851) = CONST 
    0x2b47: v2b47(0x24) = CONST 
    0x2b4b: v2b4b = ADD v2b1a, v2b47(0x24)
    0x2b4d: v2b4d(0x20) = CONST 
    0x2b55: v2b55(0x0) = SUB v2b1a, v2b39
    0x2b56: v2b56(0x24) = ADD v2b55(0x0), v2b47(0x24)
    0x2b58: v2b58(0x0) = CONST 
    0x2b5c: v2b5c = EXTCODESIZE v2b3f
    0x2b5d: v2b5d = ISZERO v2b5c
    0x2b5f: v2b5f = ISZERO v2b5d
    0x2b60: v2b60(0x2b68) = CONST 
    0x2b63: JUMPI v2b60(0x2b68), v2b5f

    Begin block 0x2b64
    prev=[0x2b13], succ=[]
    =================================
    0x2b64: v2b64(0x0) = CONST 
    0x2b67: REVERT v2b64(0x0), v2b64(0x0)

    Begin block 0x2b68
    prev=[0x2b13], succ=[0x2b73, 0x2b7c]
    =================================
    0x2b6a: v2b6a = GAS 
    0x2b6b: v2b6b = CALL v2b6a, v2b3f, v2b58(0x0), v2b39, v2b56(0x24), v2b39, v2b4d(0x20)
    0x2b6c: v2b6c = ISZERO v2b6b
    0x2b6e: v2b6e = ISZERO v2b6c
    0x2b6f: v2b6f(0x2b7c) = CONST 
    0x2b72: JUMPI v2b6f(0x2b7c), v2b6e

    Begin block 0x2b73
    prev=[0x2b68], succ=[]
    =================================
    0x2b73: v2b73 = RETURNDATASIZE 
    0x2b74: v2b74(0x0) = CONST 
    0x2b77: RETURNDATACOPY v2b74(0x0), v2b74(0x0), v2b73
    0x2b78: v2b78 = RETURNDATASIZE 
    0x2b79: v2b79(0x0) = CONST 
    0x2b7b: REVERT v2b79(0x0), v2b78

    Begin block 0x2b7c
    prev=[0x2b68], succ=[0x2b8e, 0x2b92]
    =================================
    0x2b81: v2b81(0x40) = CONST 
    0x2b83: v2b83 = MLOAD v2b81(0x40)
    0x2b84: v2b84 = RETURNDATASIZE 
    0x2b85: v2b85(0x20) = CONST 
    0x2b88: v2b88 = LT v2b84, v2b85(0x20)
    0x2b89: v2b89 = ISZERO v2b88
    0x2b8a: v2b8a(0x2b92) = CONST 
    0x2b8d: JUMPI v2b8a(0x2b92), v2b89

    Begin block 0x2b8e
    prev=[0x2b7c], succ=[]
    =================================
    0x2b8e: v2b8e(0x0) = CONST 
    0x2b91: REVERT v2b8e(0x0), v2b8e(0x0)

    Begin block 0x2b92
    prev=[0x2b7c], succ=[0x2b9b, 0x2bea]
    =================================
    0x2b94: v2b94 = MLOAD v2b83
    0x2b95: v2b95 = ISZERO v2b94
    0x2b96: v2b96 = ISZERO v2b95
    0x2b97: v2b97(0x2bea) = CONST 
    0x2b9a: JUMPI v2b97(0x2bea), v2b96

    Begin block 0x2b9b
    prev=[0x2b92], succ=[]
    =================================
    0x2b9b: v2b9b(0x40) = CONST 
    0x2b9e: v2b9e = MLOAD v2b9b(0x40)
    0x2b9f: v2b9f(0xe5) = CONST 
    0x2ba1: v2ba1(0x2) = CONST 
    0x2ba3: v2ba3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2ba1(0x2), v2b9f(0xe5)
    0x2ba4: v2ba4(0x461bcd) = CONST 
    0x2ba8: v2ba8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2ba4(0x461bcd), v2ba3(0x2000000000000000000000000000000000000000000000000000000000)
    0x2baa: MSTORE v2b9e, v2ba8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2bab: v2bab(0x20) = CONST 
    0x2bad: v2bad(0x4) = CONST 
    0x2bb0: v2bb0 = ADD v2b9e, v2bad(0x4)
    0x2bb1: MSTORE v2bb0, v2bab(0x20)
    0x2bb2: v2bb2(0x18) = CONST 
    0x2bb4: v2bb4(0x24) = CONST 
    0x2bb7: v2bb7 = ADD v2b9e, v2bb4(0x24)
    0x2bb8: MSTORE v2bb7, v2bb2(0x18)
    0x2bb9: v2bb9(0x55736572206d75737420626520626c61636b6c69737465640000000000000000) = CONST 
    0x2bda: v2bda(0x44) = CONST 
    0x2bdd: v2bdd = ADD v2b9e, v2bda(0x44)
    0x2bde: MSTORE v2bdd, v2bb9(0x55736572206d75737420626520626c61636b6c69737465640000000000000000)
    0x2be0: v2be0 = MLOAD v2b9b(0x40)
    0x2be4: v2be4(0x0) = SUB v2b9e, v2be0
    0x2be5: v2be5(0x64) = CONST 
    0x2be7: v2be7(0x64) = ADD v2be5(0x64), v2be4(0x0)
    0x2be9: REVERT v2be0, v2be7(0x64)

    Begin block 0x2bea
    prev=[0x2b92], succ=[0x2bfd, 0x2c01]
    =================================
    0x2beb: v2beb(0x1) = CONST 
    0x2bed: v2bed = SLOAD v2beb(0x1)
    0x2bee: v2bee(0xa0) = CONST 
    0x2bf0: v2bf0(0x2) = CONST 
    0x2bf2: v2bf2(0x10000000000000000000000000000000000000000) = EXP v2bf0(0x2), v2bee(0xa0)
    0x2bf4: v2bf4 = DIV v2bed, v2bf2(0x10000000000000000000000000000000000000000)
    0x2bf5: v2bf5(0xff) = CONST 
    0x2bf7: v2bf7 = AND v2bf5(0xff), v2bf4
    0x2bf8: v2bf8 = ISZERO v2bf7
    0x2bf9: v2bf9(0x2c01) = CONST 
    0x2bfc: JUMPI v2bf9(0x2c01), v2bf8

    Begin block 0x2bfd
    prev=[0x2bea], succ=[]
    =================================
    0x2bfd: v2bfd(0x0) = CONST 
    0x2c00: REVERT v2bfd(0x0), v2bfd(0x0)

    Begin block 0x2c01
    prev=[0x2bea], succ=[0x2c8c, 0x2c90]
    =================================
    0x2c02: v2c02(0x3) = CONST 
    0x2c04: v2c04 = SLOAD v2c02(0x3)
    0x2c05: v2c05(0x40) = CONST 
    0x2c08: v2c08 = MLOAD v2c05(0x40)
    0x2c09: v2c09(0x14db6d5800000000000000000000000000000000000000000000000000000000) = CONST 
    0x2c2b: MSTORE v2c08, v2c09(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x2c2c: v2c2c = CALLER 
    0x2c2d: v2c2d(0x4) = CONST 
    0x2c30: v2c30 = ADD v2c08, v2c2d(0x4)
    0x2c31: MSTORE v2c30, v2c2c
    0x2c32: v2c32(0x0) = CONST 
    0x2c35: v2c35 = CALLDATALOAD v2c32(0x0)
    0x2c36: v2c36(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c53: v2c53(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2c36(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2c54: v2c54 = AND v2c53(0xffffffff00000000000000000000000000000000000000000000000000000000), v2c35
    0x2c55: v2c55(0x24) = CONST 
    0x2c58: v2c58 = ADD v2c08, v2c55(0x24)
    0x2c59: MSTORE v2c58, v2c54
    0x2c5b: v2c5b = MLOAD v2c05(0x40)
    0x2c5c: v2c5c(0x1) = CONST 
    0x2c5e: v2c5e(0xa0) = CONST 
    0x2c60: v2c60(0x2) = CONST 
    0x2c62: v2c62(0x10000000000000000000000000000000000000000) = EXP v2c60(0x2), v2c5e(0xa0)
    0x2c63: v2c63(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c62(0x10000000000000000000000000000000000000000), v2c5c(0x1)
    0x2c66: v2c66 = AND v2c04, v2c63(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c68: v2c68(0x14db6d58) = CONST 
    0x2c6e: v2c6e(0x44) = CONST 
    0x2c72: v2c72 = ADD v2c08, v2c6e(0x44)
    0x2c74: v2c74(0x20) = CONST 
    0x2c7b: v2c7b(0x0) = SUB v2c08, v2c5b
    0x2c7e: v2c7e(0x44) = ADD v2c6e(0x44), v2c7b(0x0)
    0x2c84: v2c84 = EXTCODESIZE v2c66
    0x2c85: v2c85 = ISZERO v2c84
    0x2c87: v2c87 = ISZERO v2c85
    0x2c88: v2c88(0x2c90) = CONST 
    0x2c8b: JUMPI v2c88(0x2c90), v2c87

    Begin block 0x2c8c
    prev=[0x2c01], succ=[]
    =================================
    0x2c8c: v2c8c(0x0) = CONST 
    0x2c8f: REVERT v2c8c(0x0), v2c8c(0x0)

    Begin block 0x2c90
    prev=[0x2c01], succ=[0x2c9b, 0x2ca4]
    =================================
    0x2c92: v2c92 = GAS 
    0x2c93: v2c93 = CALL v2c92, v2c66, v2c32(0x0), v2c5b, v2c7e(0x44), v2c5b, v2c74(0x20)
    0x2c94: v2c94 = ISZERO v2c93
    0x2c96: v2c96 = ISZERO v2c94
    0x2c97: v2c97(0x2ca4) = CONST 
    0x2c9a: JUMPI v2c97(0x2ca4), v2c96

    Begin block 0x2c9b
    prev=[0x2c90], succ=[]
    =================================
    0x2c9b: v2c9b = RETURNDATASIZE 
    0x2c9c: v2c9c(0x0) = CONST 
    0x2c9f: RETURNDATACOPY v2c9c(0x0), v2c9c(0x0), v2c9b
    0x2ca0: v2ca0 = RETURNDATASIZE 
    0x2ca1: v2ca1(0x0) = CONST 
    0x2ca3: REVERT v2ca1(0x0), v2ca0

    Begin block 0x2ca4
    prev=[0x2c90], succ=[0x2cb6, 0x2cba]
    =================================
    0x2ca9: v2ca9(0x40) = CONST 
    0x2cab: v2cab = MLOAD v2ca9(0x40)
    0x2cac: v2cac = RETURNDATASIZE 
    0x2cad: v2cad(0x20) = CONST 
    0x2cb0: v2cb0 = LT v2cac, v2cad(0x20)
    0x2cb1: v2cb1 = ISZERO v2cb0
    0x2cb2: v2cb2(0x2cba) = CONST 
    0x2cb5: JUMPI v2cb2(0x2cba), v2cb1

    Begin block 0x2cb6
    prev=[0x2ca4], succ=[]
    =================================
    0x2cb6: v2cb6(0x0) = CONST 
    0x2cb9: REVERT v2cb6(0x0), v2cb6(0x0)

    Begin block 0x2cba
    prev=[0x2ca4], succ=[0x2cc3, 0x2d38]
    =================================
    0x2cbc: v2cbc = MLOAD v2cab
    0x2cbd: v2cbd = ISZERO v2cbc
    0x2cbe: v2cbe = ISZERO v2cbd
    0x2cbf: v2cbf(0x2d38) = CONST 
    0x2cc2: JUMPI v2cbf(0x2d38), v2cbe

    Begin block 0x2cc3
    prev=[0x2cba], succ=[]
    =================================
    0x2cc3: v2cc3(0x40) = CONST 
    0x2cc6: v2cc6 = MLOAD v2cc3(0x40)
    0x2cc7: v2cc7(0xe5) = CONST 
    0x2cc9: v2cc9(0x2) = CONST 
    0x2ccb: v2ccb(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2cc9(0x2), v2cc7(0xe5)
    0x2ccc: v2ccc(0x461bcd) = CONST 
    0x2cd0: v2cd0(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2ccc(0x461bcd), v2ccb(0x2000000000000000000000000000000000000000000000000000000000)
    0x2cd2: MSTORE v2cc6, v2cd0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2cd3: v2cd3(0x20) = CONST 
    0x2cd5: v2cd5(0x4) = CONST 
    0x2cd8: v2cd8 = ADD v2cc6, v2cd5(0x4)
    0x2cd9: MSTORE v2cd8, v2cd3(0x20)
    0x2cda: v2cda(0x31) = CONST 
    0x2cdc: v2cdc(0x24) = CONST 
    0x2cdf: v2cdf = ADD v2cc6, v2cdc(0x24)
    0x2ce0: MSTORE v2cdf, v2cda(0x31)
    0x2ce1: v2ce1(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x2d02: v2d02(0x44) = CONST 
    0x2d05: v2d05 = ADD v2cc6, v2d02(0x44)
    0x2d06: MSTORE v2d05, v2ce1(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x2d07: v2d07(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 
    0x2d28: v2d28(0x64) = CONST 
    0x2d2b: v2d2b = ADD v2cc6, v2d28(0x64)
    0x2d2c: MSTORE v2d2b, v2d07(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x2d2e: v2d2e = MLOAD v2cc3(0x40)
    0x2d32: v2d32(0x0) = SUB v2cc6, v2d2e
    0x2d33: v2d33(0x84) = CONST 
    0x2d35: v2d35(0x84) = ADD v2d33(0x84), v2d32(0x0)
    0x2d37: REVERT v2d2e, v2d35(0x84)

    Begin block 0x2d38
    prev=[0x2cba], succ=[0x2d8c, 0x2d90]
    =================================
    0x2d39: v2d39(0x2) = CONST 
    0x2d3b: v2d3b = SLOAD v2d39(0x2)
    0x2d3c: v2d3c(0x40) = CONST 
    0x2d3f: v2d3f = MLOAD v2d3c(0x40)
    0x2d40: v2d40(0xe1) = CONST 
    0x2d42: v2d42(0x2) = CONST 
    0x2d44: v2d44(0x200000000000000000000000000000000000000000000000000000000) = EXP v2d42(0x2), v2d40(0xe1)
    0x2d45: v2d45(0x67c775bf) = CONST 
    0x2d4a: v2d4a(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = MUL v2d45(0x67c775bf), v2d44(0x200000000000000000000000000000000000000000000000000000000)
    0x2d4c: MSTORE v2d3f, v2d4a(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x2d4d: v2d4d(0x1) = CONST 
    0x2d4f: v2d4f(0xa0) = CONST 
    0x2d51: v2d51(0x2) = CONST 
    0x2d53: v2d53(0x10000000000000000000000000000000000000000) = EXP v2d51(0x2), v2d4f(0xa0)
    0x2d54: v2d54(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d53(0x10000000000000000000000000000000000000000), v2d4d(0x1)
    0x2d57: v2d57 = AND v2d54(0xffffffffffffffffffffffffffffffffffffffff), v756
    0x2d58: v2d58(0x4) = CONST 
    0x2d5b: v2d5b = ADD v2d3f, v2d58(0x4)
    0x2d5c: MSTORE v2d5b, v2d57
    0x2d5d: v2d5d(0x24) = CONST 
    0x2d60: v2d60 = ADD v2d3f, v2d5d(0x24)
    0x2d63: MSTORE v2d60, v759
    0x2d65: v2d65 = MLOAD v2d3c(0x40)
    0x2d69: v2d69 = AND v2d3b, v2d54(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d6b: v2d6b(0xcf8eeb7e) = CONST 
    0x2d71: v2d71(0x44) = CONST 
    0x2d75: v2d75 = ADD v2d3f, v2d71(0x44)
    0x2d77: v2d77(0x0) = CONST 
    0x2d7e: v2d7e(0x0) = SUB v2d3f, v2d65
    0x2d7f: v2d7f(0x44) = ADD v2d7e(0x0), v2d71(0x44)
    0x2d84: v2d84 = EXTCODESIZE v2d69
    0x2d85: v2d85 = ISZERO v2d84
    0x2d87: v2d87 = ISZERO v2d85
    0x2d88: v2d88(0x2d90) = CONST 
    0x2d8b: JUMPI v2d88(0x2d90), v2d87

    Begin block 0x2d8c
    prev=[0x2d38], succ=[]
    =================================
    0x2d8c: v2d8c(0x0) = CONST 
    0x2d8f: REVERT v2d8c(0x0), v2d8c(0x0)

    Begin block 0x2d90
    prev=[0x2d38], succ=[0x2d9b, 0x2da4]
    =================================
    0x2d92: v2d92 = GAS 
    0x2d93: v2d93 = CALL v2d92, v2d69, v2d77(0x0), v2d65, v2d7f(0x44), v2d65, v2d77(0x0)
    0x2d94: v2d94 = ISZERO v2d93
    0x2d96: v2d96 = ISZERO v2d94
    0x2d97: v2d97(0x2da4) = CONST 
    0x2d9a: JUMPI v2d97(0x2da4), v2d96

    Begin block 0x2d9b
    prev=[0x2d90], succ=[]
    =================================
    0x2d9b: v2d9b = RETURNDATASIZE 
    0x2d9c: v2d9c(0x0) = CONST 
    0x2d9f: RETURNDATACOPY v2d9c(0x0), v2d9c(0x0), v2d9b
    0x2da0: v2da0 = RETURNDATASIZE 
    0x2da1: v2da1(0x0) = CONST 
    0x2da3: REVERT v2da1(0x0), v2da0

    Begin block 0x2da4
    prev=[0x2d90], succ=[0x2e0a, 0x2e0e]
    =================================
    0x2da7: v2da7(0x2) = CONST 
    0x2da9: v2da9 = SLOAD v2da7(0x2)
    0x2daa: v2daa(0x40) = CONST 
    0x2dad: v2dad = MLOAD v2daa(0x40)
    0x2dae: v2dae(0x82838c7600000000000000000000000000000000000000000000000000000000) = CONST 
    0x2dd0: MSTORE v2dad, v2dae(0x82838c7600000000000000000000000000000000000000000000000000000000)
    0x2dd1: v2dd1(0x4) = CONST 
    0x2dd4: v2dd4 = ADD v2dad, v2dd1(0x4)
    0x2dd7: MSTORE v2dd4, v759
    0x2dd9: v2dd9 = MLOAD v2daa(0x40)
    0x2dda: v2dda(0x1) = CONST 
    0x2ddc: v2ddc(0xa0) = CONST 
    0x2dde: v2dde(0x2) = CONST 
    0x2de0: v2de0(0x10000000000000000000000000000000000000000) = EXP v2dde(0x2), v2ddc(0xa0)
    0x2de1: v2de1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2de0(0x10000000000000000000000000000000000000000), v2dda(0x1)
    0x2de4: v2de4 = AND v2da9, v2de1(0xffffffffffffffffffffffffffffffffffffffff)
    0x2de7: v2de7(0x82838c76) = CONST 
    0x2dee: v2dee(0x24) = CONST 
    0x2df2: v2df2 = ADD v2dad, v2dee(0x24)
    0x2df4: v2df4(0x0) = CONST 
    0x2dfc: v2dfc(0x0) = SUB v2dad, v2dd9
    0x2dfd: v2dfd(0x24) = ADD v2dfc(0x0), v2dee(0x24)
    0x2e02: v2e02 = EXTCODESIZE v2de4
    0x2e03: v2e03 = ISZERO v2e02
    0x2e05: v2e05 = ISZERO v2e03
    0x2e06: v2e06(0x2e0e) = CONST 
    0x2e09: JUMPI v2e06(0x2e0e), v2e05

    Begin block 0x2e0a
    prev=[0x2da4], succ=[]
    =================================
    0x2e0a: v2e0a(0x0) = CONST 
    0x2e0d: REVERT v2e0a(0x0), v2e0a(0x0)

    Begin block 0x2e0e
    prev=[0x2da4], succ=[0x2e19, 0x2e22]
    =================================
    0x2e10: v2e10 = GAS 
    0x2e11: v2e11 = CALL v2e10, v2de4, v2df4(0x0), v2dd9, v2dfd(0x24), v2dd9, v2df4(0x0)
    0x2e12: v2e12 = ISZERO v2e11
    0x2e14: v2e14 = ISZERO v2e12
    0x2e15: v2e15(0x2e22) = CONST 
    0x2e18: JUMPI v2e15(0x2e22), v2e14

    Begin block 0x2e19
    prev=[0x2e0e], succ=[]
    =================================
    0x2e19: v2e19 = RETURNDATASIZE 
    0x2e1a: v2e1a(0x0) = CONST 
    0x2e1d: RETURNDATACOPY v2e1a(0x0), v2e1a(0x0), v2e19
    0x2e1e: v2e1e = RETURNDATASIZE 
    0x2e1f: v2e1f(0x0) = CONST 
    0x2e21: REVERT v2e1f(0x0), v2e1e

    Begin block 0x2e22
    prev=[0x2e0e], succ=[0x5081]
    =================================
    0x2e25: v2e25(0x40) = CONST 
    0x2e28: v2e28 = MLOAD v2e25(0x40)
    0x2e2b: MSTORE v2e28, v759
    0x2e2d: v2e2d = MLOAD v2e25(0x40)
    0x2e2e: v2e2e(0x1) = CONST 
    0x2e30: v2e30(0xa0) = CONST 
    0x2e32: v2e32(0x2) = CONST 
    0x2e34: v2e34(0x10000000000000000000000000000000000000000) = EXP v2e32(0x2), v2e30(0xa0)
    0x2e35: v2e35(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e34(0x10000000000000000000000000000000000000000), v2e2e(0x1)
    0x2e37: v2e37 = AND v756, v2e35(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e3a: v2e3a(0xb81d1dffb753076892e04e6e1234d137b031f70d859c299876b0486e966424fd) = CONST 
    0x2e60: v2e60(0x0) = SUB v2e28, v2e2d
    0x2e61: v2e61(0x20) = CONST 
    0x2e63: v2e63(0x20) = ADD v2e61(0x20), v2e60(0x0)
    0x2e65: LOG2 v2e2d, v2e63(0x20), v2e3a(0xb81d1dffb753076892e04e6e1234d137b031f70d859c299876b0486e966424fd), v2e37
    0x2e69: JUMP v748(0x5081)

    Begin block 0x5081
    prev=[0x2e22], succ=[]
    =================================
    0x5082: STOP 

}

function setDefaultFee(uint256)() public {
    Begin block 0x75e
    prev=[], succ=[0x766, 0x76a]
    =================================
    0x75f: v75f = CALLVALUE 
    0x761: v761 = ISZERO v75f
    0x762: v762(0x76a) = CONST 
    0x765: JUMPI v762(0x76a), v761

    Begin block 0x766
    prev=[0x75e], succ=[]
    =================================
    0x766: v766(0x0) = CONST 
    0x769: REVERT v766(0x0), v766(0x0)

    Begin block 0x76a
    prev=[0x75e], succ=[0x2e6aB0x76a]
    =================================
    0x76c: v76c(0x50a2) = CONST 
    0x76f: v76f(0x4) = CONST 
    0x771: v771 = CALLDATALOAD v76f(0x4)
    0x772: v772(0x2e6a) = CONST 
    0x775: JUMP v772(0x2e6a), v771, v76c(0x50a2)

    Begin block 0x2e6aB0x76a
    prev=[0x76a], succ=[0x2e7dB0x76a, 0x2e81B0x76a]
    =================================
    0x2e6bS0x76a: v2e6bV76a(0x0) = CONST 
    0x2e6dS0x76a: v2e6dV76a = SLOAD v2e6bV76a(0x0)
    0x2e6eS0x76a: v2e6eV76a(0x1) = CONST 
    0x2e70S0x76a: v2e70V76a(0xa0) = CONST 
    0x2e72S0x76a: v2e72V76a(0x2) = CONST 
    0x2e74S0x76a: v2e74V76a(0x10000000000000000000000000000000000000000) = EXP v2e72V76a(0x2), v2e70V76a(0xa0)
    0x2e75S0x76a: v2e75V76a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e74V76a(0x10000000000000000000000000000000000000000), v2e6eV76a(0x1)
    0x2e76S0x76a: v2e76V76a = AND v2e75V76a(0xffffffffffffffffffffffffffffffffffffffff), v2e6dV76a
    0x2e77S0x76a: v2e77V76a = CALLER 
    0x2e78S0x76a: v2e78V76a = EQ v2e77V76a, v2e76V76a
    0x2e79S0x76a: v2e79V76a(0x2e81) = CONST 
    0x2e7cS0x76a: JUMPI v2e79V76a(0x2e81), v2e78V76a

    Begin block 0x2e7dB0x76a
    prev=[0x2e6aB0x76a], succ=[]
    =================================
    0x2e7dS0x76a: v2e7dV76a(0x0) = CONST 
    0x2e80S0x76a: REVERT v2e7dV76a(0x0), v2e7dV76a(0x0)

    Begin block 0x2e81B0x76a
    prev=[0x2e6aB0x76a], succ=[0x2e94B0x76a, 0x2e98B0x76a]
    =================================
    0x2e82S0x76a: v2e82V76a(0x1) = CONST 
    0x2e84S0x76a: v2e84V76a = SLOAD v2e82V76a(0x1)
    0x2e85S0x76a: v2e85V76a(0xa0) = CONST 
    0x2e87S0x76a: v2e87V76a(0x2) = CONST 
    0x2e89S0x76a: v2e89V76a(0x10000000000000000000000000000000000000000) = EXP v2e87V76a(0x2), v2e85V76a(0xa0)
    0x2e8bS0x76a: v2e8bV76a = DIV v2e84V76a, v2e89V76a(0x10000000000000000000000000000000000000000)
    0x2e8cS0x76a: v2e8cV76a(0xff) = CONST 
    0x2e8eS0x76a: v2e8eV76a = AND v2e8cV76a(0xff), v2e8bV76a
    0x2e8fS0x76a: v2e8fV76a = ISZERO v2e8eV76a
    0x2e90S0x76a: v2e90V76a(0x2e98) = CONST 
    0x2e93S0x76a: JUMPI v2e90V76a(0x2e98), v2e8fV76a

    Begin block 0x2e94B0x76a
    prev=[0x2e81B0x76a], succ=[]
    =================================
    0x2e94S0x76a: v2e94V76a(0x0) = CONST 
    0x2e97S0x76a: REVERT v2e94V76a(0x0), v2e94V76a(0x0)

    Begin block 0x2e98B0x76a
    prev=[0x2e81B0x76a], succ=[0x2ef8B0x76a, 0x11fc0x2e6aB0x76a]
    =================================
    0x2e99S0x76a: v2e99V76a(0x4) = CONST 
    0x2e9cS0x76a: v2e9cV76a = SLOAD v2e99V76a(0x4)
    0x2e9dS0x76a: v2e9dV76a(0x40) = CONST 
    0x2ea0S0x76a: v2ea0V76a = MLOAD v2e9dV76a(0x40)
    0x2ea1S0x76a: v2ea1V76a(0xc93a6c8400000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ec3S0x76a: MSTORE v2ea0V76a, v2ea1V76a(0xc93a6c8400000000000000000000000000000000000000000000000000000000)
    0x2ec6S0x76a: v2ec6V76a = ADD v2ea0V76a, v2e99V76a(0x4)
    0x2ec9S0x76a: MSTORE v2ec6V76a, v771
    0x2ecaS0x76a: v2ecaV76a = MLOAD v2e9dV76a(0x40)
    0x2ecbS0x76a: v2ecbV76a(0x1) = CONST 
    0x2ecdS0x76a: v2ecdV76a(0xa0) = CONST 
    0x2ecfS0x76a: v2ecfV76a(0x2) = CONST 
    0x2ed1S0x76a: v2ed1V76a(0x10000000000000000000000000000000000000000) = EXP v2ecfV76a(0x2), v2ecdV76a(0xa0)
    0x2ed2S0x76a: v2ed2V76a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ed1V76a(0x10000000000000000000000000000000000000000), v2ecbV76a(0x1)
    0x2ed5S0x76a: v2ed5V76a = AND v2e9cV76a, v2ed2V76a(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ed7S0x76a: v2ed7V76a(0xc93a6c84) = CONST 
    0x2eddS0x76a: v2eddV76a(0x24) = CONST 
    0x2ee1S0x76a: v2ee1V76a = ADD v2ea0V76a, v2eddV76a(0x24)
    0x2ee3S0x76a: v2ee3V76a(0x0) = CONST 
    0x2eeaS0x76a: v2eeaV76a(0x0) = SUB v2ea0V76a, v2ecaV76a
    0x2eebS0x76a: v2eebV76a(0x24) = ADD v2eeaV76a(0x0), v2eddV76a(0x24)
    0x2ef0S0x76a: v2ef0V76a = EXTCODESIZE v2ed5V76a
    0x2ef1S0x76a: v2ef1V76a = ISZERO v2ef0V76a
    0x2ef3S0x76a: v2ef3V76a = ISZERO v2ef1V76a
    0x2ef4S0x76a: v2ef4V76a(0x11fc) = CONST 
    0x2ef7S0x76a: JUMPI v2ef4V76a(0x11fc), v2ef3V76a

    Begin block 0x2ef8B0x76a
    prev=[0x2e98B0x76a], succ=[]
    =================================
    0x2ef8S0x76a: v2ef8V76a(0x0) = CONST 
    0x2efbS0x76a: REVERT v2ef8V76a(0x0), v2ef8V76a(0x0)

    Begin block 0x11fc0x2e6aB0x76a
    prev=[0x2e98B0x76a], succ=[0x12070x2e6aB0x76a, 0x12100x2e6aB0x76a]
    =================================
    0x11fe0x2e6aS0x76a: v2e6a11feV76a = GAS 
    0x11ff0x2e6aS0x76a: v2e6a11ffV76a = CALL v2e6a11feV76a, v2ed5V76a, v2ee3V76a(0x0), v2ecaV76a, v2eebV76a(0x24), v2ecaV76a, v2ee3V76a(0x0)
    0x12000x2e6aS0x76a: v2e6a1200V76a = ISZERO v2e6a11ffV76a
    0x12020x2e6aS0x76a: v2e6a1202V76a = ISZERO v2e6a1200V76a
    0x12030x2e6aS0x76a: v2e6a1203V76a(0x1210) = CONST 
    0x12060x2e6aS0x76a: JUMPI v2e6a1203V76a(0x1210), v2e6a1202V76a

    Begin block 0x12070x2e6aB0x76a
    prev=[0x11fc0x2e6aB0x76a], succ=[]
    =================================
    0x12070x2e6aS0x76a: v2e6a1207V76a = RETURNDATASIZE 
    0x12080x2e6aS0x76a: v2e6a1208V76a(0x0) = CONST 
    0x120b0x2e6aS0x76a: RETURNDATACOPY v2e6a1208V76a(0x0), v2e6a1208V76a(0x0), v2e6a1207V76a
    0x120c0x2e6aS0x76a: v2e6a120cV76a = RETURNDATASIZE 
    0x120d0x2e6aS0x76a: v2e6a120dV76a(0x0) = CONST 
    0x120f0x2e6aS0x76a: REVERT v2e6a120dV76a(0x0), v2e6a120cV76a

    Begin block 0x12100x2e6aB0x76a
    prev=[0x11fc0x2e6aB0x76a], succ=[0x50a2]
    =================================
    0x12160x2e6aS0x76a: JUMP v76c(0x50a2)

    Begin block 0x50a2
    prev=[0x12100x2e6aB0x76a], succ=[]
    =================================
    0x50a3: STOP 

}

function setRegulator(address)() public {
    Begin block 0x776
    prev=[], succ=[0x77e, 0x782]
    =================================
    0x777: v777 = CALLVALUE 
    0x779: v779 = ISZERO v777
    0x77a: v77a(0x782) = CONST 
    0x77d: JUMPI v77a(0x782), v779

    Begin block 0x77e
    prev=[0x776], succ=[]
    =================================
    0x77e: v77e(0x0) = CONST 
    0x781: REVERT v77e(0x0), v77e(0x0)

    Begin block 0x782
    prev=[0x776], succ=[0x2efc]
    =================================
    0x784: v784(0x50c3) = CONST 
    0x787: v787(0x1) = CONST 
    0x789: v789(0xa0) = CONST 
    0x78b: v78b(0x2) = CONST 
    0x78d: v78d(0x10000000000000000000000000000000000000000) = EXP v78b(0x2), v789(0xa0)
    0x78e: v78e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v78d(0x10000000000000000000000000000000000000000), v787(0x1)
    0x78f: v78f(0x4) = CONST 
    0x791: v791 = CALLDATALOAD v78f(0x4)
    0x792: v792 = AND v791, v78e(0xffffffffffffffffffffffffffffffffffffffff)
    0x793: v793(0x2efc) = CONST 
    0x796: JUMP v793(0x2efc)

    Begin block 0x2efc
    prev=[0x782], succ=[0x2f10, 0x2f14]
    =================================
    0x2efd: v2efd(0x0) = CONST 
    0x2f00: v2f00 = SLOAD v2efd(0x0)
    0x2f01: v2f01(0x1) = CONST 
    0x2f03: v2f03(0xa0) = CONST 
    0x2f05: v2f05(0x2) = CONST 
    0x2f07: v2f07(0x10000000000000000000000000000000000000000) = EXP v2f05(0x2), v2f03(0xa0)
    0x2f08: v2f08(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f07(0x10000000000000000000000000000000000000000), v2f01(0x1)
    0x2f09: v2f09 = AND v2f08(0xffffffffffffffffffffffffffffffffffffffff), v2f00
    0x2f0a: v2f0a = CALLER 
    0x2f0b: v2f0b = EQ v2f0a, v2f09
    0x2f0c: v2f0c(0x2f14) = CONST 
    0x2f0f: JUMPI v2f0c(0x2f14), v2f0b

    Begin block 0x2f10
    prev=[0x2efc], succ=[]
    =================================
    0x2f10: v2f10(0x0) = CONST 
    0x2f13: REVERT v2f10(0x0), v2f10(0x0)

    Begin block 0x2f14
    prev=[0x2efc], succ=[0x2f2b, 0x2f7a]
    =================================
    0x2f15: v2f15(0x3) = CONST 
    0x2f17: v2f17 = SLOAD v2f15(0x3)
    0x2f18: v2f18(0x1) = CONST 
    0x2f1a: v2f1a(0xa0) = CONST 
    0x2f1c: v2f1c(0x2) = CONST 
    0x2f1e: v2f1e(0x10000000000000000000000000000000000000000) = EXP v2f1c(0x2), v2f1a(0xa0)
    0x2f1f: v2f1f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f1e(0x10000000000000000000000000000000000000000), v2f18(0x1)
    0x2f22: v2f22 = AND v2f1f(0xffffffffffffffffffffffffffffffffffffffff), v792
    0x2f24: v2f24 = AND v2f17, v2f1f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2f25: v2f25 = EQ v2f24, v2f22
    0x2f26: v2f26 = ISZERO v2f25
    0x2f27: v2f27(0x2f7a) = CONST 
    0x2f2a: JUMPI v2f27(0x2f7a), v2f26

    Begin block 0x2f2b
    prev=[0x2f14], succ=[]
    =================================
    0x2f2b: v2f2b(0x40) = CONST 
    0x2f2e: v2f2e = MLOAD v2f2b(0x40)
    0x2f2f: v2f2f(0xe5) = CONST 
    0x2f31: v2f31(0x2) = CONST 
    0x2f33: v2f33(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2f31(0x2), v2f2f(0xe5)
    0x2f34: v2f34(0x461bcd) = CONST 
    0x2f38: v2f38(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2f34(0x461bcd), v2f33(0x2000000000000000000000000000000000000000000000000000000000)
    0x2f3a: MSTORE v2f2e, v2f38(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2f3b: v2f3b(0x20) = CONST 
    0x2f3d: v2f3d(0x4) = CONST 
    0x2f40: v2f40 = ADD v2f2e, v2f3d(0x4)
    0x2f41: MSTORE v2f40, v2f3b(0x20)
    0x2f42: v2f42(0x17) = CONST 
    0x2f44: v2f44(0x24) = CONST 
    0x2f47: v2f47 = ADD v2f2e, v2f44(0x24)
    0x2f48: MSTORE v2f47, v2f42(0x17)
    0x2f49: v2f49(0x4d7573742062652061206e657720726567756c61746f72000000000000000000) = CONST 
    0x2f6a: v2f6a(0x44) = CONST 
    0x2f6d: v2f6d = ADD v2f2e, v2f6a(0x44)
    0x2f6e: MSTORE v2f6d, v2f49(0x4d7573742062652061206e657720726567756c61746f72000000000000000000)
    0x2f70: v2f70 = MLOAD v2f2b(0x40)
    0x2f74: v2f74(0x0) = SUB v2f2e, v2f70
    0x2f75: v2f75(0x64) = CONST 
    0x2f77: v2f77(0x64) = ADD v2f75(0x64), v2f74(0x0)
    0x2f79: REVERT v2f70, v2f77(0x64)

    Begin block 0x2f7a
    prev=[0x2f14], succ=[0x4a47]
    =================================
    0x2f7b: v2f7b(0x2f83) = CONST 
    0x2f7f: v2f7f(0x4a47) = CONST 
    0x2f82: JUMP v2f7f(0x4a47)

    Begin block 0x4a47
    prev=[0x2f7a], succ=[0x2f83]
    =================================
    0x4a48: v4a48(0x0) = CONST 
    0x4a4b: v4a4b = EXTCODESIZE v792
    0x4a4c: v4a4c = GT v4a4b, v4a48(0x0)
    0x4a4e: JUMP v2f7b(0x2f83)

    Begin block 0x2f83
    prev=[0x4a47], succ=[0x2f8a, 0x2fff]
    =================================
    0x2f84: v2f84 = ISZERO v4a4c
    0x2f85: v2f85 = ISZERO v2f84
    0x2f86: v2f86(0x2fff) = CONST 
    0x2f89: JUMPI v2f86(0x2fff), v2f85

    Begin block 0x2f8a
    prev=[0x2f83], succ=[]
    =================================
    0x2f8a: v2f8a(0x40) = CONST 
    0x2f8d: v2f8d = MLOAD v2f8a(0x40)
    0x2f8e: v2f8e(0xe5) = CONST 
    0x2f90: v2f90(0x2) = CONST 
    0x2f92: v2f92(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2f90(0x2), v2f8e(0xe5)
    0x2f93: v2f93(0x461bcd) = CONST 
    0x2f97: v2f97(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2f93(0x461bcd), v2f92(0x2000000000000000000000000000000000000000000000000000000000)
    0x2f99: MSTORE v2f8d, v2f97(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2f9a: v2f9a(0x20) = CONST 
    0x2f9c: v2f9c(0x4) = CONST 
    0x2f9f: v2f9f = ADD v2f8d, v2f9c(0x4)
    0x2fa0: MSTORE v2f9f, v2f9a(0x20)
    0x2fa1: v2fa1(0x38) = CONST 
    0x2fa3: v2fa3(0x24) = CONST 
    0x2fa6: v2fa6 = ADD v2f8d, v2fa3(0x24)
    0x2fa7: MSTORE v2fa6, v2fa1(0x38)
    0x2fa8: v2fa8(0x43616e6e6f7420736574206120726567756c61746f722073746f726167652074) = CONST 
    0x2fc9: v2fc9(0x44) = CONST 
    0x2fcc: v2fcc = ADD v2f8d, v2fc9(0x44)
    0x2fcd: MSTORE v2fcc, v2fa8(0x43616e6e6f7420736574206120726567756c61746f722073746f726167652074)
    0x2fce: v2fce(0x6f2061206e6f6e2d636f6e747261637420616464726573730000000000000000) = CONST 
    0x2fef: v2fef(0x64) = CONST 
    0x2ff2: v2ff2 = ADD v2f8d, v2fef(0x64)
    0x2ff3: MSTORE v2ff2, v2fce(0x6f2061206e6f6e2d636f6e747261637420616464726573730000000000000000)
    0x2ff5: v2ff5 = MLOAD v2f8a(0x40)
    0x2ff9: v2ff9(0x0) = SUB v2f8d, v2ff5
    0x2ffa: v2ffa(0x84) = CONST 
    0x2ffc: v2ffc(0x84) = ADD v2ffa(0x84), v2ff9(0x0)
    0x2ffe: REVERT v2ff5, v2ffc(0x84)

    Begin block 0x2fff
    prev=[0x2f83], succ=[0x50c3]
    =================================
    0x3001: v3001(0x3) = CONST 
    0x3004: v3004 = SLOAD v3001(0x3)
    0x3005: v3005(0x1) = CONST 
    0x3007: v3007(0xa0) = CONST 
    0x3009: v3009(0x2) = CONST 
    0x300b: v300b(0x10000000000000000000000000000000000000000) = EXP v3009(0x2), v3007(0xa0)
    0x300c: v300c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v300b(0x10000000000000000000000000000000000000000), v3005(0x1)
    0x300f: v300f = AND v300c(0xffffffffffffffffffffffffffffffffffffffff), v792
    0x3010: v3010(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3025: v3025(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3010(0xffffffffffffffffffffffffffffffffffffffff)
    0x3027: v3027 = AND v3004, v3025(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3029: v3029 = OR v300f, v3027
    0x302c: SSTORE v3001(0x3), v3029
    0x302d: v302d(0x40) = CONST 
    0x302f: v302f = MLOAD v302d(0x40)
    0x3031: v3031 = AND v3004, v300c(0xffffffffffffffffffffffffffffffffffffffff)
    0x3036: v3036(0x4a59b4b607c6055b37a4716d7813d7d4d2c288e4d0dd8298e365b260a1f262e8) = CONST 
    0x3058: v3058(0x0) = CONST 
    0x305b: LOG3 v302f, v3058(0x0), v3036(0x4a59b4b607c6055b37a4716d7813d7d4d2c288e4d0dd8298e365b260a1f262e8), v3031, v300f
    0x305e: JUMP v784(0x50c3)

    Begin block 0x50c3
    prev=[0x2fff], succ=[]
    =================================
    0x50c4: STOP 

}

function increaseApproval(address,uint256)() public {
    Begin block 0x797
    prev=[], succ=[0x79f, 0x7a3]
    =================================
    0x798: v798 = CALLVALUE 
    0x79a: v79a = ISZERO v798
    0x79b: v79b(0x7a3) = CONST 
    0x79e: JUMPI v79b(0x7a3), v79a

    Begin block 0x79f
    prev=[0x797], succ=[]
    =================================
    0x79f: v79f(0x0) = CONST 
    0x7a2: REVERT v79f(0x0), v79f(0x0)

    Begin block 0x7a3
    prev=[0x797], succ=[0x305f]
    =================================
    0x7a5: v7a5(0x50e4) = CONST 
    0x7a8: v7a8(0x1) = CONST 
    0x7aa: v7aa(0xa0) = CONST 
    0x7ac: v7ac(0x2) = CONST 
    0x7ae: v7ae(0x10000000000000000000000000000000000000000) = EXP v7ac(0x2), v7aa(0xa0)
    0x7af: v7af(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7ae(0x10000000000000000000000000000000000000000), v7a8(0x1)
    0x7b0: v7b0(0x4) = CONST 
    0x7b2: v7b2 = CALLDATALOAD v7b0(0x4)
    0x7b3: v7b3 = AND v7b2, v7af(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b4: v7b4(0x24) = CONST 
    0x7b6: v7b6 = CALLDATALOAD v7b4(0x24)
    0x7b7: v7b7(0x305f) = CONST 
    0x7ba: JUMP v7b7(0x305f)

    Begin block 0x305f
    prev=[0x7a3], succ=[0x30ae, 0x30b2]
    =================================
    0x3060: v3060(0x3) = CONST 
    0x3062: v3062 = SLOAD v3060(0x3)
    0x3063: v3063(0x40) = CONST 
    0x3066: v3066 = MLOAD v3063(0x40)
    0x3067: v3067(0xe0) = CONST 
    0x3069: v3069(0x2) = CONST 
    0x306b: v306b(0x100000000000000000000000000000000000000000000000000000000) = EXP v3069(0x2), v3067(0xe0)
    0x306c: v306c(0x7ccce851) = CONST 
    0x3071: v3071(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v306c(0x7ccce851), v306b(0x100000000000000000000000000000000000000000000000000000000)
    0x3073: MSTORE v3066, v3071(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x3074: v3074(0x1) = CONST 
    0x3076: v3076(0xa0) = CONST 
    0x3078: v3078(0x2) = CONST 
    0x307a: v307a(0x10000000000000000000000000000000000000000) = EXP v3078(0x2), v3076(0xa0)
    0x307b: v307b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v307a(0x10000000000000000000000000000000000000000), v3074(0x1)
    0x307e: v307e = AND v7b3, v307b(0xffffffffffffffffffffffffffffffffffffffff)
    0x307f: v307f(0x4) = CONST 
    0x3082: v3082 = ADD v3066, v307f(0x4)
    0x3083: MSTORE v3082, v307e
    0x3085: v3085 = MLOAD v3063(0x40)
    0x3086: v3086(0x0) = CONST 
    0x308b: v308b = AND v307b(0xffffffffffffffffffffffffffffffffffffffff), v3062
    0x308d: v308d(0x7ccce851) = CONST 
    0x3093: v3093(0x24) = CONST 
    0x3097: v3097 = ADD v3066, v3093(0x24)
    0x3099: v3099(0x20) = CONST 
    0x30a0: v30a0(0x0) = SUB v3066, v3085
    0x30a1: v30a1(0x24) = ADD v30a0(0x0), v3093(0x24)
    0x30a6: v30a6 = EXTCODESIZE v308b
    0x30a7: v30a7 = ISZERO v30a6
    0x30a9: v30a9 = ISZERO v30a7
    0x30aa: v30aa(0x30b2) = CONST 
    0x30ad: JUMPI v30aa(0x30b2), v30a9

    Begin block 0x30ae
    prev=[0x305f], succ=[]
    =================================
    0x30ae: v30ae(0x0) = CONST 
    0x30b1: REVERT v30ae(0x0), v30ae(0x0)

    Begin block 0x30b2
    prev=[0x305f], succ=[0x30bd, 0x30c6]
    =================================
    0x30b4: v30b4 = GAS 
    0x30b5: v30b5 = CALL v30b4, v308b, v3086(0x0), v3085, v30a1(0x24), v3085, v3099(0x20)
    0x30b6: v30b6 = ISZERO v30b5
    0x30b8: v30b8 = ISZERO v30b6
    0x30b9: v30b9(0x30c6) = CONST 
    0x30bc: JUMPI v30b9(0x30c6), v30b8

    Begin block 0x30bd
    prev=[0x30b2], succ=[]
    =================================
    0x30bd: v30bd = RETURNDATASIZE 
    0x30be: v30be(0x0) = CONST 
    0x30c1: RETURNDATACOPY v30be(0x0), v30be(0x0), v30bd
    0x30c2: v30c2 = RETURNDATASIZE 
    0x30c3: v30c3(0x0) = CONST 
    0x30c5: REVERT v30c3(0x0), v30c2

    Begin block 0x30c6
    prev=[0x30b2], succ=[0x30d8, 0x30dc]
    =================================
    0x30cb: v30cb(0x40) = CONST 
    0x30cd: v30cd = MLOAD v30cb(0x40)
    0x30ce: v30ce = RETURNDATASIZE 
    0x30cf: v30cf(0x20) = CONST 
    0x30d2: v30d2 = LT v30ce, v30cf(0x20)
    0x30d3: v30d3 = ISZERO v30d2
    0x30d4: v30d4(0x30dc) = CONST 
    0x30d7: JUMPI v30d4(0x30dc), v30d3

    Begin block 0x30d8
    prev=[0x30c6], succ=[]
    =================================
    0x30d8: v30d8(0x0) = CONST 
    0x30db: REVERT v30d8(0x0), v30d8(0x0)

    Begin block 0x30dc
    prev=[0x30c6], succ=[0x30e4, 0x3121]
    =================================
    0x30de: v30de = MLOAD v30cd
    0x30df: v30df = ISZERO v30de
    0x30e0: v30e0(0x3121) = CONST 
    0x30e3: JUMPI v30e0(0x3121), v30df

    Begin block 0x30e4
    prev=[0x30dc], succ=[]
    =================================
    0x30e4: v30e4(0x40) = CONST 
    0x30e7: v30e7 = MLOAD v30e4(0x40)
    0x30e8: v30e8(0xe5) = CONST 
    0x30ea: v30ea(0x2) = CONST 
    0x30ec: v30ec(0x2000000000000000000000000000000000000000000000000000000000) = EXP v30ea(0x2), v30e8(0xe5)
    0x30ed: v30ed(0x461bcd) = CONST 
    0x30f1: v30f1(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v30ed(0x461bcd), v30ec(0x2000000000000000000000000000000000000000000000000000000000)
    0x30f3: MSTORE v30e7, v30f1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x30f4: v30f4(0x20) = CONST 
    0x30f6: v30f6(0x4) = CONST 
    0x30f9: v30f9 = ADD v30e7, v30f6(0x4)
    0x30fa: MSTORE v30f9, v30f4(0x20)
    0x30fb: v30fb(0x1c) = CONST 
    0x30fd: v30fd(0x24) = CONST 
    0x3100: v3100 = ADD v30e7, v30fd(0x24)
    0x3101: MSTORE v3100, v30fb(0x1c)
    0x3102: v3102(0x0) = CONST 
    0x3105: v3105 = MLOAD v3102(0x0)
    0x3106: v3106(0x20) = CONST 
    0x3108: v3108(0x4a70) = CONST 
    0x3110: MSTORE v3102(0x0), v3105
    0x3111: v3111(0x44) = CONST 
    0x3114: v3114 = ADD v30e7, v3111(0x44)
    0x3115: MSTORE v3114, v556b(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x3117: v3117 = MLOAD v30e4(0x40)
    0x311b: v311b(0x0) = SUB v30e7, v3117
    0x311c: v311c(0x64) = CONST 
    0x311e: v311e(0x64) = ADD v311c(0x64), v311b(0x0)
    0x3120: REVERT v3117, v311e(0x64)
    0x556b: v556b(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x3121
    prev=[0x30dc], succ=[0x316f, 0x3173]
    =================================
    0x3122: v3122(0x3) = CONST 
    0x3124: v3124 = SLOAD v3122(0x3)
    0x3125: v3125(0x40) = CONST 
    0x3128: v3128 = MLOAD v3125(0x40)
    0x3129: v3129(0xe0) = CONST 
    0x312b: v312b(0x2) = CONST 
    0x312d: v312d(0x100000000000000000000000000000000000000000000000000000000) = EXP v312b(0x2), v3129(0xe0)
    0x312e: v312e(0x7ccce851) = CONST 
    0x3133: v3133(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v312e(0x7ccce851), v312d(0x100000000000000000000000000000000000000000000000000000000)
    0x3135: MSTORE v3128, v3133(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x3136: v3136 = CALLER 
    0x3137: v3137(0x4) = CONST 
    0x313a: v313a = ADD v3128, v3137(0x4)
    0x313d: MSTORE v313a, v3136
    0x313f: v313f = MLOAD v3125(0x40)
    0x3142: v3142(0x1) = CONST 
    0x3144: v3144(0xa0) = CONST 
    0x3146: v3146(0x2) = CONST 
    0x3148: v3148(0x10000000000000000000000000000000000000000) = EXP v3146(0x2), v3144(0xa0)
    0x3149: v3149(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3148(0x10000000000000000000000000000000000000000), v3142(0x1)
    0x314a: v314a = AND v3149(0xffffffffffffffffffffffffffffffffffffffff), v3124
    0x314c: v314c(0x7ccce851) = CONST 
    0x3152: v3152(0x24) = CONST 
    0x3156: v3156 = ADD v3128, v3152(0x24)
    0x3158: v3158(0x20) = CONST 
    0x3160: v3160(0x0) = SUB v3128, v313f
    0x3161: v3161(0x24) = ADD v3160(0x0), v3152(0x24)
    0x3163: v3163(0x0) = CONST 
    0x3167: v3167 = EXTCODESIZE v314a
    0x3168: v3168 = ISZERO v3167
    0x316a: v316a = ISZERO v3168
    0x316b: v316b(0x3173) = CONST 
    0x316e: JUMPI v316b(0x3173), v316a

    Begin block 0x316f
    prev=[0x3121], succ=[]
    =================================
    0x316f: v316f(0x0) = CONST 
    0x3172: REVERT v316f(0x0), v316f(0x0)

    Begin block 0x3173
    prev=[0x3121], succ=[0x317e, 0x3187]
    =================================
    0x3175: v3175 = GAS 
    0x3176: v3176 = CALL v3175, v314a, v3163(0x0), v313f, v3161(0x24), v313f, v3158(0x20)
    0x3177: v3177 = ISZERO v3176
    0x3179: v3179 = ISZERO v3177
    0x317a: v317a(0x3187) = CONST 
    0x317d: JUMPI v317a(0x3187), v3179

    Begin block 0x317e
    prev=[0x3173], succ=[]
    =================================
    0x317e: v317e = RETURNDATASIZE 
    0x317f: v317f(0x0) = CONST 
    0x3182: RETURNDATACOPY v317f(0x0), v317f(0x0), v317e
    0x3183: v3183 = RETURNDATASIZE 
    0x3184: v3184(0x0) = CONST 
    0x3186: REVERT v3184(0x0), v3183

    Begin block 0x3187
    prev=[0x3173], succ=[0x3199, 0x319d]
    =================================
    0x318c: v318c(0x40) = CONST 
    0x318e: v318e = MLOAD v318c(0x40)
    0x318f: v318f = RETURNDATASIZE 
    0x3190: v3190(0x20) = CONST 
    0x3193: v3193 = LT v318f, v3190(0x20)
    0x3194: v3194 = ISZERO v3193
    0x3195: v3195(0x319d) = CONST 
    0x3198: JUMPI v3195(0x319d), v3194

    Begin block 0x3199
    prev=[0x3187], succ=[]
    =================================
    0x3199: v3199(0x0) = CONST 
    0x319c: REVERT v3199(0x0), v3199(0x0)

    Begin block 0x319d
    prev=[0x3187], succ=[0x31a5, 0x31e2]
    =================================
    0x319f: v319f = MLOAD v318e
    0x31a0: v31a0 = ISZERO v319f
    0x31a1: v31a1(0x31e2) = CONST 
    0x31a4: JUMPI v31a1(0x31e2), v31a0

    Begin block 0x31a5
    prev=[0x319d], succ=[]
    =================================
    0x31a5: v31a5(0x40) = CONST 
    0x31a8: v31a8 = MLOAD v31a5(0x40)
    0x31a9: v31a9(0xe5) = CONST 
    0x31ab: v31ab(0x2) = CONST 
    0x31ad: v31ad(0x2000000000000000000000000000000000000000000000000000000000) = EXP v31ab(0x2), v31a9(0xe5)
    0x31ae: v31ae(0x461bcd) = CONST 
    0x31b2: v31b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v31ae(0x461bcd), v31ad(0x2000000000000000000000000000000000000000000000000000000000)
    0x31b4: MSTORE v31a8, v31b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x31b5: v31b5(0x20) = CONST 
    0x31b7: v31b7(0x4) = CONST 
    0x31ba: v31ba = ADD v31a8, v31b7(0x4)
    0x31bb: MSTORE v31ba, v31b5(0x20)
    0x31bc: v31bc(0x1c) = CONST 
    0x31be: v31be(0x24) = CONST 
    0x31c1: v31c1 = ADD v31a8, v31be(0x24)
    0x31c2: MSTORE v31c1, v31bc(0x1c)
    0x31c3: v31c3(0x0) = CONST 
    0x31c6: v31c6 = MLOAD v31c3(0x0)
    0x31c7: v31c7(0x20) = CONST 
    0x31c9: v31c9(0x4a70) = CONST 
    0x31d1: MSTORE v31c3(0x0), v31c6
    0x31d2: v31d2(0x44) = CONST 
    0x31d5: v31d5 = ADD v31a8, v31d2(0x44)
    0x31d6: MSTORE v31d5, v5570(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x31d8: v31d8 = MLOAD v31a5(0x40)
    0x31dc: v31dc(0x0) = SUB v31a8, v31d8
    0x31dd: v31dd(0x64) = CONST 
    0x31df: v31df(0x64) = ADD v31dd(0x64), v31dc(0x0)
    0x31e1: REVERT v31d8, v31df(0x64)
    0x5570: v5570(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x31e2
    prev=[0x319d], succ=[0x31f5, 0x31f9]
    =================================
    0x31e3: v31e3(0x1) = CONST 
    0x31e5: v31e5 = SLOAD v31e3(0x1)
    0x31e6: v31e6(0xa0) = CONST 
    0x31e8: v31e8(0x2) = CONST 
    0x31ea: v31ea(0x10000000000000000000000000000000000000000) = EXP v31e8(0x2), v31e6(0xa0)
    0x31ec: v31ec = DIV v31e5, v31ea(0x10000000000000000000000000000000000000000)
    0x31ed: v31ed(0xff) = CONST 
    0x31ef: v31ef = AND v31ed(0xff), v31ec
    0x31f0: v31f0 = ISZERO v31ef
    0x31f1: v31f1(0x31f9) = CONST 
    0x31f4: JUMPI v31f1(0x31f9), v31f0

    Begin block 0x31f5
    prev=[0x31e2], succ=[]
    =================================
    0x31f5: v31f5(0x0) = CONST 
    0x31f8: REVERT v31f5(0x0), v31f5(0x0)

    Begin block 0x31f9
    prev=[0x31e2], succ=[0x53af]
    =================================
    0x31fa: v31fa(0x53af) = CONST 
    0x31ff: v31ff = CALLER 
    0x3200: v3200(0x465c) = CONST 
    0x3203: CALLPRIVATE v3200(0x465c), v31ff, v7b6, v7b3, v31fa(0x53af)

    Begin block 0x53af
    prev=[0x31f9], succ=[0x50e4]
    =================================
    0x53b1: v53b1(0x1) = CONST 
    0x53b9: JUMP v7a5(0x50e4)

    Begin block 0x50e4
    prev=[0x53af], succ=[]
    =================================
    0x50e5: v50e5(0x40) = CONST 
    0x50e8: v50e8 = MLOAD v50e5(0x40)
    0x50ea: v50ea = ISZERO v53b1(0x1)
    0x50eb: v50eb = ISZERO v50ea
    0x50ed: MSTORE v50e8, v50eb
    0x50ee: v50ee = MLOAD v50e5(0x40)
    0x50f2: v50f2(0x0) = SUB v50e8, v50ee
    0x50f3: v50f3(0x20) = CONST 
    0x50f5: v50f5(0x20) = ADD v50f3(0x20), v50f2(0x0)
    0x50f7: RETURN v50ee, v50f5(0x20)

}

function metaBurnHash(address,uint256,uint256,uint256)() public {
    Begin block 0x7bb
    prev=[], succ=[0x7c3, 0x7c7]
    =================================
    0x7bc: v7bc = CALLVALUE 
    0x7be: v7be = ISZERO v7bc
    0x7bf: v7bf(0x7c7) = CONST 
    0x7c2: JUMPI v7bf(0x7c7), v7be

    Begin block 0x7c3
    prev=[0x7bb], succ=[]
    =================================
    0x7c3: v7c3(0x0) = CONST 
    0x7c6: REVERT v7c3(0x0), v7c3(0x0)

    Begin block 0x7c7
    prev=[0x7bb], succ=[0x5117]
    =================================
    0x7c9: v7c9(0x5117) = CONST 
    0x7cc: v7cc(0x1) = CONST 
    0x7ce: v7ce(0xa0) = CONST 
    0x7d0: v7d0(0x2) = CONST 
    0x7d2: v7d2(0x10000000000000000000000000000000000000000) = EXP v7d0(0x2), v7ce(0xa0)
    0x7d3: v7d3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d2(0x10000000000000000000000000000000000000000), v7cc(0x1)
    0x7d4: v7d4(0x4) = CONST 
    0x7d6: v7d6 = CALLDATALOAD v7d4(0x4)
    0x7d7: v7d7 = AND v7d6, v7d3(0xffffffffffffffffffffffffffffffffffffffff)
    0x7d8: v7d8(0x24) = CONST 
    0x7da: v7da = CALLDATALOAD v7d8(0x24)
    0x7db: v7db(0x44) = CONST 
    0x7dd: v7dd = CALLDATALOAD v7db(0x44)
    0x7de: v7de(0x64) = CONST 
    0x7e0: v7e0 = CALLDATALOAD v7de(0x64)
    0x7e1: v7e1(0x3204) = CONST 
    0x7e4: v7e4_0 = CALLPRIVATE v7e1(0x3204), v7e0, v7dd, v7da, v7d7, v7c9(0x5117)

    Begin block 0x5117
    prev=[0x7c7], succ=[]
    =================================
    0x5118: v5118(0x40) = CONST 
    0x511b: v511b = MLOAD v5118(0x40)
    0x511e: MSTORE v511b, v7e4_0
    0x511f: v511f = MLOAD v5118(0x40)
    0x5123: v5123(0x0) = SUB v511b, v511f
    0x5124: v5124(0x20) = CONST 
    0x5126: v5126(0x20) = ADD v5124(0x20), v5123(0x0)
    0x5128: RETURN v511f, v5126(0x20)

}

function allowance(address,address)() public {
    Begin block 0x7e5
    prev=[], succ=[0x7ed, 0x7f1]
    =================================
    0x7e6: v7e6 = CALLVALUE 
    0x7e8: v7e8 = ISZERO v7e6
    0x7e9: v7e9(0x7f1) = CONST 
    0x7ec: JUMPI v7e9(0x7f1), v7e8

    Begin block 0x7ed
    prev=[0x7e5], succ=[]
    =================================
    0x7ed: v7ed(0x0) = CONST 
    0x7f0: REVERT v7ed(0x0), v7ed(0x0)

    Begin block 0x7f1
    prev=[0x7e5], succ=[0x5148]
    =================================
    0x7f3: v7f3(0x5148) = CONST 
    0x7f6: v7f6(0x1) = CONST 
    0x7f8: v7f8(0xa0) = CONST 
    0x7fa: v7fa(0x2) = CONST 
    0x7fc: v7fc(0x10000000000000000000000000000000000000000) = EXP v7fa(0x2), v7f8(0xa0)
    0x7fd: v7fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fc(0x10000000000000000000000000000000000000000), v7f6(0x1)
    0x7fe: v7fe(0x4) = CONST 
    0x800: v800 = CALLDATALOAD v7fe(0x4)
    0x802: v802 = AND v7fd(0xffffffffffffffffffffffffffffffffffffffff), v800
    0x804: v804(0x24) = CONST 
    0x806: v806 = CALLDATALOAD v804(0x24)
    0x807: v807 = AND v806, v7fd(0xffffffffffffffffffffffffffffffffffffffff)
    0x808: v808(0x32b1) = CONST 
    0x80b: v80b_0 = CALLPRIVATE v808(0x32b1), v807, v802, v7f3(0x5148)

    Begin block 0x5148
    prev=[0x7f1], succ=[]
    =================================
    0x5149: v5149(0x40) = CONST 
    0x514c: v514c = MLOAD v5149(0x40)
    0x514f: MSTORE v514c, v80b_0
    0x5150: v5150 = MLOAD v5149(0x40)
    0x5154: v5154(0x0) = SUB v514c, v5150
    0x5155: v5155(0x20) = CONST 
    0x5157: v5157(0x20) = ADD v5155(0x20), v5154(0x0)
    0x5159: RETURN v5150, v5157(0x20)

}

function regulator()() public {
    Begin block 0x80c
    prev=[], succ=[0x814, 0x818]
    =================================
    0x80d: v80d = CALLVALUE 
    0x80f: v80f = ISZERO v80d
    0x810: v810(0x818) = CONST 
    0x813: JUMPI v810(0x818), v80f

    Begin block 0x814
    prev=[0x80c], succ=[]
    =================================
    0x814: v814(0x0) = CONST 
    0x817: REVERT v814(0x0), v814(0x0)

    Begin block 0x818
    prev=[0x80c], succ=[0x3357]
    =================================
    0x81a: v81a(0x5179) = CONST 
    0x81d: v81d(0x3357) = CONST 
    0x820: JUMP v81d(0x3357)

    Begin block 0x3357
    prev=[0x818], succ=[0x5179]
    =================================
    0x3358: v3358(0x3) = CONST 
    0x335a: v335a = SLOAD v3358(0x3)
    0x335b: v335b(0x1) = CONST 
    0x335d: v335d(0xa0) = CONST 
    0x335f: v335f(0x2) = CONST 
    0x3361: v3361(0x10000000000000000000000000000000000000000) = EXP v335f(0x2), v335d(0xa0)
    0x3362: v3362(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3361(0x10000000000000000000000000000000000000000), v335b(0x1)
    0x3363: v3363 = AND v3362(0xffffffffffffffffffffffffffffffffffffffff), v335a
    0x3365: JUMP v81a(0x5179)

    Begin block 0x5179
    prev=[0x3357], succ=[]
    =================================
    0x517a: v517a(0x40) = CONST 
    0x517d: v517d = MLOAD v517a(0x40)
    0x517e: v517e(0x1) = CONST 
    0x5180: v5180(0xa0) = CONST 
    0x5182: v5182(0x2) = CONST 
    0x5184: v5184(0x10000000000000000000000000000000000000000) = EXP v5182(0x2), v5180(0xa0)
    0x5185: v5185(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5184(0x10000000000000000000000000000000000000000), v517e(0x1)
    0x5188: v5188 = AND v3363, v5185(0xffffffffffffffffffffffffffffffffffffffff)
    0x518a: MSTORE v517d, v5188
    0x518b: v518b = MLOAD v517a(0x40)
    0x518f: v518f(0x0) = SUB v517d, v518b
    0x5190: v5190(0x20) = CONST 
    0x5192: v5192(0x20) = ADD v5190(0x20), v518f(0x0)
    0x5194: RETURN v518b, v5192(0x20)

}

function metaTransfer(address,uint256,bytes,uint256,uint256)() public {
    Begin block 0x821
    prev=[], succ=[0x829, 0x82d]
    =================================
    0x822: v822 = CALLVALUE 
    0x824: v824 = ISZERO v822
    0x825: v825(0x82d) = CONST 
    0x828: JUMPI v825(0x82d), v824

    Begin block 0x829
    prev=[0x821], succ=[]
    =================================
    0x829: v829(0x0) = CONST 
    0x82c: REVERT v829(0x0), v829(0x0)

    Begin block 0x82d
    prev=[0x821], succ=[0x3366B0x82d]
    =================================
    0x82f: v82f(0x40) = CONST 
    0x832: v832 = MLOAD v82f(0x40)
    0x833: v833(0x20) = CONST 
    0x835: v835(0x4) = CONST 
    0x837: v837(0x44) = CONST 
    0x839: v839 = CALLDATALOAD v837(0x44)
    0x83c: v83c = ADD v839, v835(0x4)
    0x83d: v83d = CALLDATALOAD v83c
    0x83e: v83e(0x1f) = CONST 
    0x841: v841 = ADD v83d, v83e(0x1f)
    0x844: v844 = DIV v841, v833(0x20)
    0x846: v846 = MUL v833(0x20), v844
    0x848: v848 = ADD v832, v846
    0x84a: v84a = ADD v833(0x20), v848
    0x84d: MSTORE v82f(0x40), v84a
    0x850: MSTORE v832, v83d
    0x851: v851(0x51b4) = CONST 
    0x856: v856 = CALLDATALOAD v835(0x4)
    0x857: v857(0x1) = CONST 
    0x859: v859(0xa0) = CONST 
    0x85b: v85b(0x2) = CONST 
    0x85d: v85d(0x10000000000000000000000000000000000000000) = EXP v85b(0x2), v859(0xa0)
    0x85e: v85e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v85d(0x10000000000000000000000000000000000000000), v857(0x1)
    0x85f: v85f = AND v85e(0xffffffffffffffffffffffffffffffffffffffff), v856
    0x861: v861(0x24) = CONST 
    0x864: v864 = CALLDATALOAD v861(0x24)
    0x866: v866 = CALLDATASIZE 
    0x869: v869(0x64) = CONST 
    0x86d: v86d = ADD v861(0x24), v839
    0x873: v873 = ADD v832, v833(0x20)
    0x879: CALLDATACOPY v873, v86d, v83d
    0x880: v880 = CALLDATALOAD v869(0x64)
    0x885: v885(0x20) = CONST 
    0x889: v889(0x84) = ADD v869(0x64), v885(0x20)
    0x88a: v88a = CALLDATALOAD v889(0x84)
    0x88d: v88d(0x3366) = CONST 
    0x892: JUMP v88d(0x3366)

    Begin block 0x3366B0x82d
    prev=[0x82d], succ=[0x33bcB0x82d, 0x33c0B0x82d]
    =================================
    0x3367S0x82d: v3367V82d(0x3) = CONST 
    0x3369S0x82d: v3369V82d = SLOAD v3367V82d(0x3)
    0x336aS0x82d: v336aV82d(0x40) = CONST 
    0x336dS0x82d: v336dV82d = MLOAD v336aV82d(0x40)
    0x336eS0x82d: v336eV82d(0xe0) = CONST 
    0x3370S0x82d: v3370V82d(0x2) = CONST 
    0x3372S0x82d: v3372V82d(0x100000000000000000000000000000000000000000000000000000000) = EXP v3370V82d(0x2), v336eV82d(0xe0)
    0x3373S0x82d: v3373V82d(0x7ccce851) = CONST 
    0x3378S0x82d: v3378V82d(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v3373V82d(0x7ccce851), v3372V82d(0x100000000000000000000000000000000000000000000000000000000)
    0x337aS0x82d: MSTORE v336dV82d, v3378V82d(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x337bS0x82d: v337bV82d(0x1) = CONST 
    0x337dS0x82d: v337dV82d(0xa0) = CONST 
    0x337fS0x82d: v337fV82d(0x2) = CONST 
    0x3381S0x82d: v3381V82d(0x10000000000000000000000000000000000000000) = EXP v337fV82d(0x2), v337dV82d(0xa0)
    0x3382S0x82d: v3382V82d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3381V82d(0x10000000000000000000000000000000000000000), v337bV82d(0x1)
    0x3385S0x82d: v3385V82d = AND v85f, v3382V82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3386S0x82d: v3386V82d(0x4) = CONST 
    0x3389S0x82d: v3389V82d = ADD v336dV82d, v3386V82d(0x4)
    0x338aS0x82d: MSTORE v3389V82d, v3385V82d
    0x338cS0x82d: v338cV82d = MLOAD v336aV82d(0x40)
    0x338dS0x82d: v338dV82d(0x0) = CONST 
    0x3399S0x82d: v3399V82d = AND v3369V82d, v3382V82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x339bS0x82d: v339bV82d(0x7ccce851) = CONST 
    0x33a1S0x82d: v33a1V82d(0x24) = CONST 
    0x33a5S0x82d: v33a5V82d = ADD v336dV82d, v33a1V82d(0x24)
    0x33a7S0x82d: v33a7V82d(0x20) = CONST 
    0x33aeS0x82d: v33aeV82d(0x0) = SUB v336dV82d, v338cV82d
    0x33afS0x82d: v33afV82d(0x24) = ADD v33aeV82d(0x0), v33a1V82d(0x24)
    0x33b4S0x82d: v33b4V82d = EXTCODESIZE v3399V82d
    0x33b5S0x82d: v33b5V82d = ISZERO v33b4V82d
    0x33b7S0x82d: v33b7V82d = ISZERO v33b5V82d
    0x33b8S0x82d: v33b8V82d(0x33c0) = CONST 
    0x33bbS0x82d: JUMPI v33b8V82d(0x33c0), v33b7V82d

    Begin block 0x33bcB0x82d
    prev=[0x3366B0x82d], succ=[]
    =================================
    0x33bcS0x82d: v33bcV82d(0x0) = CONST 
    0x33bfS0x82d: REVERT v33bcV82d(0x0), v33bcV82d(0x0)

    Begin block 0x33c0B0x82d
    prev=[0x3366B0x82d], succ=[0x33cbB0x82d, 0x33d4B0x82d]
    =================================
    0x33c2S0x82d: v33c2V82d = GAS 
    0x33c3S0x82d: v33c3V82d = CALL v33c2V82d, v3399V82d, v338dV82d(0x0), v338cV82d, v33afV82d(0x24), v338cV82d, v33a7V82d(0x20)
    0x33c4S0x82d: v33c4V82d = ISZERO v33c3V82d
    0x33c6S0x82d: v33c6V82d = ISZERO v33c4V82d
    0x33c7S0x82d: v33c7V82d(0x33d4) = CONST 
    0x33caS0x82d: JUMPI v33c7V82d(0x33d4), v33c6V82d

    Begin block 0x33cbB0x82d
    prev=[0x33c0B0x82d], succ=[]
    =================================
    0x33cbS0x82d: v33cbV82d = RETURNDATASIZE 
    0x33ccS0x82d: v33ccV82d(0x0) = CONST 
    0x33cfS0x82d: RETURNDATACOPY v33ccV82d(0x0), v33ccV82d(0x0), v33cbV82d
    0x33d0S0x82d: v33d0V82d = RETURNDATASIZE 
    0x33d1S0x82d: v33d1V82d(0x0) = CONST 
    0x33d3S0x82d: REVERT v33d1V82d(0x0), v33d0V82d

    Begin block 0x33d4B0x82d
    prev=[0x33c0B0x82d], succ=[0x33e6B0x82d, 0x33eaB0x82d]
    =================================
    0x33d9S0x82d: v33d9V82d(0x40) = CONST 
    0x33dbS0x82d: v33dbV82d = MLOAD v33d9V82d(0x40)
    0x33dcS0x82d: v33dcV82d = RETURNDATASIZE 
    0x33ddS0x82d: v33ddV82d(0x20) = CONST 
    0x33e0S0x82d: v33e0V82d = LT v33dcV82d, v33ddV82d(0x20)
    0x33e1S0x82d: v33e1V82d = ISZERO v33e0V82d
    0x33e2S0x82d: v33e2V82d(0x33ea) = CONST 
    0x33e5S0x82d: JUMPI v33e2V82d(0x33ea), v33e1V82d

    Begin block 0x33e6B0x82d
    prev=[0x33d4B0x82d], succ=[]
    =================================
    0x33e6S0x82d: v33e6V82d(0x0) = CONST 
    0x33e9S0x82d: REVERT v33e6V82d(0x0), v33e6V82d(0x0)

    Begin block 0x33eaB0x82d
    prev=[0x33d4B0x82d], succ=[0x33f2B0x82d, 0x342fB0x82d]
    =================================
    0x33ecS0x82d: v33ecV82d = MLOAD v33dbV82d
    0x33edS0x82d: v33edV82d = ISZERO v33ecV82d
    0x33eeS0x82d: v33eeV82d(0x342f) = CONST 
    0x33f1S0x82d: JUMPI v33eeV82d(0x342f), v33edV82d

    Begin block 0x33f2B0x82d
    prev=[0x33eaB0x82d], succ=[]
    =================================
    0x33f2S0x82d: v33f2V82d(0x40) = CONST 
    0x33f5S0x82d: v33f5V82d = MLOAD v33f2V82d(0x40)
    0x33f6S0x82d: v33f6V82d(0xe5) = CONST 
    0x33f8S0x82d: v33f8V82d(0x2) = CONST 
    0x33faS0x82d: v33faV82d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v33f8V82d(0x2), v33f6V82d(0xe5)
    0x33fbS0x82d: v33fbV82d(0x461bcd) = CONST 
    0x33ffS0x82d: v33ffV82d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v33fbV82d(0x461bcd), v33faV82d(0x2000000000000000000000000000000000000000000000000000000000)
    0x3401S0x82d: MSTORE v33f5V82d, v33ffV82d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3402S0x82d: v3402V82d(0x20) = CONST 
    0x3404S0x82d: v3404V82d(0x4) = CONST 
    0x3407S0x82d: v3407V82d = ADD v33f5V82d, v3404V82d(0x4)
    0x3408S0x82d: MSTORE v3407V82d, v3402V82d(0x20)
    0x3409S0x82d: v3409V82d(0x1c) = CONST 
    0x340bS0x82d: v340bV82d(0x24) = CONST 
    0x340eS0x82d: v340eV82d = ADD v33f5V82d, v340bV82d(0x24)
    0x340fS0x82d: MSTORE v340eV82d, v3409V82d(0x1c)
    0x3410S0x82d: v3410V82d(0x0) = CONST 
    0x3413S0x82d: v3413V82d = MLOAD v3410V82d(0x0)
    0x3414S0x82d: v3414V82d(0x20) = CONST 
    0x3416S0x82d: v3416V82d(0x4a70) = CONST 
    0x341eS0x82d: MSTORE v3410V82d(0x0), v3413V82d
    0x341fS0x82d: v341fV82d(0x44) = CONST 
    0x3422S0x82d: v3422V82d = ADD v33f5V82d, v341fV82d(0x44)
    0x3423S0x82d: MSTORE v3422V82d, v5575V82d(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x3425S0x82d: v3425V82d = MLOAD v33f2V82d(0x40)
    0x3429S0x82d: v3429V82d(0x0) = SUB v33f5V82d, v3425V82d
    0x342aS0x82d: v342aV82d(0x64) = CONST 
    0x342cS0x82d: v342cV82d(0x64) = ADD v342aV82d(0x64), v3429V82d(0x0)
    0x342eS0x82d: REVERT v3425V82d, v342cV82d(0x64)
    0x5575S0x82d: v5575V82d(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x342fB0x82d
    prev=[0x33eaB0x82d], succ=[0x3442B0x82d, 0x3446B0x82d]
    =================================
    0x3430S0x82d: v3430V82d(0x1) = CONST 
    0x3432S0x82d: v3432V82d = SLOAD v3430V82d(0x1)
    0x3433S0x82d: v3433V82d(0xa0) = CONST 
    0x3435S0x82d: v3435V82d(0x2) = CONST 
    0x3437S0x82d: v3437V82d(0x10000000000000000000000000000000000000000) = EXP v3435V82d(0x2), v3433V82d(0xa0)
    0x3439S0x82d: v3439V82d = DIV v3432V82d, v3437V82d(0x10000000000000000000000000000000000000000)
    0x343aS0x82d: v343aV82d(0xff) = CONST 
    0x343cS0x82d: v343cV82d = AND v343aV82d(0xff), v3439V82d
    0x343dS0x82d: v343dV82d = ISZERO v343cV82d
    0x343eS0x82d: v343eV82d(0x3446) = CONST 
    0x3441S0x82d: JUMPI v343eV82d(0x3446), v343dV82d

    Begin block 0x3442B0x82d
    prev=[0x342fB0x82d], succ=[]
    =================================
    0x3442S0x82d: v3442V82d(0x0) = CONST 
    0x3445S0x82d: REVERT v3442V82d(0x0), v3442V82d(0x0)

    Begin block 0x3446B0x82d
    prev=[0x342fB0x82d], succ=[0x3452B0x82d]
    =================================
    0x3447S0x82d: v3447V82d(0x3452) = CONST 
    0x344eS0x82d: v344eV82d(0x2a67) = CONST 
    0x3451S0x82d: v3451_0V82d = CALLPRIVATE v344eV82d(0x2a67), v88a, v880, v864, v85f, v3447V82d(0x3452)

    Begin block 0x3452B0x82d
    prev=[0x3446B0x82d], succ=[0x345eB0x82d]
    =================================
    0x3455S0x82d: v3455V82d(0x345e) = CONST 
    0x345aS0x82d: v345aV82d(0x44ed) = CONST 
    0x345dS0x82d: v345d_0V82d = CALLPRIVATE v345aV82d(0x44ed), v832, v3451_0V82d, v3455V82d(0x345e)

    Begin block 0x345eB0x82d
    prev=[0x3452B0x82d], succ=[0x34aeB0x82d, 0x34b2B0x82d]
    =================================
    0x345fS0x82d: v345fV82d(0x3) = CONST 
    0x3461S0x82d: v3461V82d = SLOAD v345fV82d(0x3)
    0x3462S0x82d: v3462V82d(0x40) = CONST 
    0x3465S0x82d: v3465V82d = MLOAD v3462V82d(0x40)
    0x3466S0x82d: v3466V82d(0xe0) = CONST 
    0x3468S0x82d: v3468V82d(0x2) = CONST 
    0x346aS0x82d: v346aV82d(0x100000000000000000000000000000000000000000000000000000000) = EXP v3468V82d(0x2), v3466V82d(0xe0)
    0x346bS0x82d: v346bV82d(0x7ccce851) = CONST 
    0x3470S0x82d: v3470V82d(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v346bV82d(0x7ccce851), v346aV82d(0x100000000000000000000000000000000000000000000000000000000)
    0x3472S0x82d: MSTORE v3465V82d, v3470V82d(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x3473S0x82d: v3473V82d(0x1) = CONST 
    0x3475S0x82d: v3475V82d(0xa0) = CONST 
    0x3477S0x82d: v3477V82d(0x2) = CONST 
    0x3479S0x82d: v3479V82d(0x10000000000000000000000000000000000000000) = EXP v3477V82d(0x2), v3475V82d(0xa0)
    0x347aS0x82d: v347aV82d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3479V82d(0x10000000000000000000000000000000000000000), v3473V82d(0x1)
    0x347dS0x82d: v347dV82d = AND v345d_0V82d, v347aV82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x347eS0x82d: v347eV82d(0x4) = CONST 
    0x3481S0x82d: v3481V82d = ADD v3465V82d, v347eV82d(0x4)
    0x3482S0x82d: MSTORE v3481V82d, v347dV82d
    0x3484S0x82d: v3484V82d = MLOAD v3462V82d(0x40)
    0x3489S0x82d: v3489V82d = AND v3461V82d, v347aV82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x348bS0x82d: v348bV82d(0x7ccce851) = CONST 
    0x3491S0x82d: v3491V82d(0x24) = CONST 
    0x3495S0x82d: v3495V82d = ADD v3465V82d, v3491V82d(0x24)
    0x3497S0x82d: v3497V82d(0x20) = CONST 
    0x349fS0x82d: v349fV82d(0x0) = SUB v3465V82d, v3484V82d
    0x34a0S0x82d: v34a0V82d(0x24) = ADD v349fV82d(0x0), v3491V82d(0x24)
    0x34a2S0x82d: v34a2V82d(0x0) = CONST 
    0x34a6S0x82d: v34a6V82d = EXTCODESIZE v3489V82d
    0x34a7S0x82d: v34a7V82d = ISZERO v34a6V82d
    0x34a9S0x82d: v34a9V82d = ISZERO v34a7V82d
    0x34aaS0x82d: v34aaV82d(0x34b2) = CONST 
    0x34adS0x82d: JUMPI v34aaV82d(0x34b2), v34a9V82d

    Begin block 0x34aeB0x82d
    prev=[0x345eB0x82d], succ=[]
    =================================
    0x34aeS0x82d: v34aeV82d(0x0) = CONST 
    0x34b1S0x82d: REVERT v34aeV82d(0x0), v34aeV82d(0x0)

    Begin block 0x34b2B0x82d
    prev=[0x345eB0x82d], succ=[0x34bdB0x82d, 0x34c6B0x82d]
    =================================
    0x34b4S0x82d: v34b4V82d = GAS 
    0x34b5S0x82d: v34b5V82d = CALL v34b4V82d, v3489V82d, v34a2V82d(0x0), v3484V82d, v34a0V82d(0x24), v3484V82d, v3497V82d(0x20)
    0x34b6S0x82d: v34b6V82d = ISZERO v34b5V82d
    0x34b8S0x82d: v34b8V82d = ISZERO v34b6V82d
    0x34b9S0x82d: v34b9V82d(0x34c6) = CONST 
    0x34bcS0x82d: JUMPI v34b9V82d(0x34c6), v34b8V82d

    Begin block 0x34bdB0x82d
    prev=[0x34b2B0x82d], succ=[]
    =================================
    0x34bdS0x82d: v34bdV82d = RETURNDATASIZE 
    0x34beS0x82d: v34beV82d(0x0) = CONST 
    0x34c1S0x82d: RETURNDATACOPY v34beV82d(0x0), v34beV82d(0x0), v34bdV82d
    0x34c2S0x82d: v34c2V82d = RETURNDATASIZE 
    0x34c3S0x82d: v34c3V82d(0x0) = CONST 
    0x34c5S0x82d: REVERT v34c3V82d(0x0), v34c2V82d

    Begin block 0x34c6B0x82d
    prev=[0x34b2B0x82d], succ=[0x34d8B0x82d, 0x34dcB0x82d]
    =================================
    0x34cbS0x82d: v34cbV82d(0x40) = CONST 
    0x34cdS0x82d: v34cdV82d = MLOAD v34cbV82d(0x40)
    0x34ceS0x82d: v34ceV82d = RETURNDATASIZE 
    0x34cfS0x82d: v34cfV82d(0x20) = CONST 
    0x34d2S0x82d: v34d2V82d = LT v34ceV82d, v34cfV82d(0x20)
    0x34d3S0x82d: v34d3V82d = ISZERO v34d2V82d
    0x34d4S0x82d: v34d4V82d(0x34dc) = CONST 
    0x34d7S0x82d: JUMPI v34d4V82d(0x34dc), v34d3V82d

    Begin block 0x34d8B0x82d
    prev=[0x34c6B0x82d], succ=[]
    =================================
    0x34d8S0x82d: v34d8V82d(0x0) = CONST 
    0x34dbS0x82d: REVERT v34d8V82d(0x0), v34d8V82d(0x0)

    Begin block 0x34dcB0x82d
    prev=[0x34c6B0x82d], succ=[0x34e4B0x82d, 0x3533B0x82d]
    =================================
    0x34deS0x82d: v34deV82d = MLOAD v34cdV82d
    0x34dfS0x82d: v34dfV82d = ISZERO v34deV82d
    0x34e0S0x82d: v34e0V82d(0x3533) = CONST 
    0x34e3S0x82d: JUMPI v34e0V82d(0x3533), v34dfV82d

    Begin block 0x34e4B0x82d
    prev=[0x34dcB0x82d], succ=[]
    =================================
    0x34e4S0x82d: v34e4V82d(0x40) = CONST 
    0x34e7S0x82d: v34e7V82d = MLOAD v34e4V82d(0x40)
    0x34e8S0x82d: v34e8V82d(0xe5) = CONST 
    0x34eaS0x82d: v34eaV82d(0x2) = CONST 
    0x34ecS0x82d: v34ecV82d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v34eaV82d(0x2), v34e8V82d(0xe5)
    0x34edS0x82d: v34edV82d(0x461bcd) = CONST 
    0x34f1S0x82d: v34f1V82d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v34edV82d(0x461bcd), v34ecV82d(0x2000000000000000000000000000000000000000000000000000000000)
    0x34f3S0x82d: MSTORE v34e7V82d, v34f1V82d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x34f4S0x82d: v34f4V82d(0x20) = CONST 
    0x34f6S0x82d: v34f6V82d(0x4) = CONST 
    0x34f9S0x82d: v34f9V82d = ADD v34e7V82d, v34f6V82d(0x4)
    0x34faS0x82d: MSTORE v34f9V82d, v34f4V82d(0x20)
    0x34fbS0x82d: v34fbV82d(0x15) = CONST 
    0x34fdS0x82d: v34fdV82d(0x24) = CONST 
    0x3500S0x82d: v3500V82d = ADD v34e7V82d, v34fdV82d(0x24)
    0x3501S0x82d: MSTORE v3500V82d, v34fbV82d(0x15)
    0x3502S0x82d: v3502V82d(0x7369676e657220697320626c61636b6c69737465640000000000000000000000) = CONST 
    0x3523S0x82d: v3523V82d(0x44) = CONST 
    0x3526S0x82d: v3526V82d = ADD v34e7V82d, v3523V82d(0x44)
    0x3527S0x82d: MSTORE v3526V82d, v3502V82d(0x7369676e657220697320626c61636b6c69737465640000000000000000000000)
    0x3529S0x82d: v3529V82d = MLOAD v34e4V82d(0x40)
    0x352dS0x82d: v352dV82d(0x0) = SUB v34e7V82d, v3529V82d
    0x352eS0x82d: v352eV82d(0x64) = CONST 
    0x3530S0x82d: v3530V82d(0x64) = ADD v352eV82d(0x64), v352dV82d(0x0)
    0x3532S0x82d: REVERT v3529V82d, v3530V82d(0x64)

    Begin block 0x3533B0x82d
    prev=[0x34dcB0x82d], succ=[0x3553B0x82d, 0x35c8B0x82d]
    =================================
    0x3534S0x82d: v3534V82d(0x1) = CONST 
    0x3536S0x82d: v3536V82d(0xa0) = CONST 
    0x3538S0x82d: v3538V82d(0x2) = CONST 
    0x353aS0x82d: v353aV82d(0x10000000000000000000000000000000000000000) = EXP v3538V82d(0x2), v3536V82d(0xa0)
    0x353bS0x82d: v353bV82d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v353aV82d(0x10000000000000000000000000000000000000000), v3534V82d(0x1)
    0x353dS0x82d: v353dV82d = AND v345d_0V82d, v353bV82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x353eS0x82d: v353eV82d(0x0) = CONST 
    0x3542S0x82d: MSTORE v353eV82d(0x0), v353dV82d
    0x3543S0x82d: v3543V82d(0x5) = CONST 
    0x3545S0x82d: v3545V82d(0x20) = CONST 
    0x3547S0x82d: MSTORE v3545V82d(0x20), v3543V82d(0x5)
    0x3548S0x82d: v3548V82d(0x40) = CONST 
    0x354bS0x82d: v354bV82d = SHA3 v353eV82d(0x0), v3548V82d(0x40)
    0x354cS0x82d: v354cV82d = SLOAD v354bV82d
    0x354eS0x82d: v354eV82d = EQ v880, v354cV82d
    0x354fS0x82d: v354fV82d(0x35c8) = CONST 
    0x3552S0x82d: JUMPI v354fV82d(0x35c8), v354eV82d

    Begin block 0x3553B0x82d
    prev=[0x3533B0x82d], succ=[]
    =================================
    0x3553S0x82d: v3553V82d(0x40) = CONST 
    0x3556S0x82d: v3556V82d = MLOAD v3553V82d(0x40)
    0x3557S0x82d: v3557V82d(0xe5) = CONST 
    0x3559S0x82d: v3559V82d(0x2) = CONST 
    0x355bS0x82d: v355bV82d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3559V82d(0x2), v3557V82d(0xe5)
    0x355cS0x82d: v355cV82d(0x461bcd) = CONST 
    0x3560S0x82d: v3560V82d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v355cV82d(0x461bcd), v355bV82d(0x2000000000000000000000000000000000000000000000000000000000)
    0x3562S0x82d: MSTORE v3556V82d, v3560V82d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3563S0x82d: v3563V82d(0x20) = CONST 
    0x3565S0x82d: v3565V82d(0x4) = CONST 
    0x3568S0x82d: v3568V82d = ADD v3556V82d, v3565V82d(0x4)
    0x3569S0x82d: MSTORE v3568V82d, v3563V82d(0x20)
    0x356aS0x82d: v356aV82d(0x2b) = CONST 
    0x356cS0x82d: v356cV82d(0x24) = CONST 
    0x356fS0x82d: v356fV82d = ADD v3556V82d, v356cV82d(0x24)
    0x3570S0x82d: MSTORE v356fV82d, v356aV82d(0x2b)
    0x3571S0x82d: v3571V82d(0x74686973207472616e73616374696f6e2068617320616c726561647920626565) = CONST 
    0x3592S0x82d: v3592V82d(0x44) = CONST 
    0x3595S0x82d: v3595V82d = ADD v3556V82d, v3592V82d(0x44)
    0x3596S0x82d: MSTORE v3595V82d, v3571V82d(0x74686973207472616e73616374696f6e2068617320616c726561647920626565)
    0x3597S0x82d: v3597V82d(0x6e2062726f616463617374000000000000000000000000000000000000000000) = CONST 
    0x35b8S0x82d: v35b8V82d(0x64) = CONST 
    0x35bbS0x82d: v35bbV82d = ADD v3556V82d, v35b8V82d(0x64)
    0x35bcS0x82d: MSTORE v35bbV82d, v3597V82d(0x6e2062726f616463617374000000000000000000000000000000000000000000)
    0x35beS0x82d: v35beV82d = MLOAD v3553V82d(0x40)
    0x35c2S0x82d: v35c2V82d(0x0) = SUB v3556V82d, v35beV82d
    0x35c3S0x82d: v35c3V82d(0x84) = CONST 
    0x35c5S0x82d: v35c5V82d(0x84) = ADD v35c3V82d(0x84), v35c2V82d(0x0)
    0x35c7S0x82d: REVERT v35beV82d, v35c5V82d(0x84)

    Begin block 0x35c8B0x82d
    prev=[0x3533B0x82d], succ=[0x35eeB0x82d, 0x3663B0x82d]
    =================================
    0x35c9S0x82d: v35c9V82d(0x1) = CONST 
    0x35cbS0x82d: v35cbV82d(0xa0) = CONST 
    0x35cdS0x82d: v35cdV82d(0x2) = CONST 
    0x35cfS0x82d: v35cfV82d(0x10000000000000000000000000000000000000000) = EXP v35cdV82d(0x2), v35cbV82d(0xa0)
    0x35d0S0x82d: v35d0V82d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35cfV82d(0x10000000000000000000000000000000000000000), v35c9V82d(0x1)
    0x35d2S0x82d: v35d2V82d = AND v345d_0V82d, v35d0V82d(0xffffffffffffffffffffffffffffffffffffffff)
    0x35d3S0x82d: v35d3V82d(0x0) = CONST 
    0x35d7S0x82d: MSTORE v35d3V82d(0x0), v35d2V82d
    0x35d8S0x82d: v35d8V82d(0x5) = CONST 
    0x35daS0x82d: v35daV82d(0x20) = CONST 
    0x35dcS0x82d: MSTORE v35daV82d(0x20), v35d8V82d(0x5)
    0x35ddS0x82d: v35ddV82d(0x40) = CONST 
    0x35e0S0x82d: v35e0V82d = SHA3 v35d3V82d(0x0), v35ddV82d(0x40)
    0x35e2S0x82d: v35e2V82d = SLOAD v35e0V82d
    0x35e3S0x82d: v35e3V82d(0x1) = CONST 
    0x35e5S0x82d: v35e5V82d = ADD v35e3V82d(0x1), v35e2V82d
    0x35e7S0x82d: SSTORE v35e0V82d, v35e5V82d
    0x35e9S0x82d: v35e9V82d = GT v88a, v35d3V82d(0x0)
    0x35eaS0x82d: v35eaV82d(0x3663) = CONST 
    0x35edS0x82d: JUMPI v35eaV82d(0x3663), v35e9V82d

    Begin block 0x35eeB0x82d
    prev=[0x35c8B0x82d], succ=[]
    =================================
    0x35eeS0x82d: v35eeV82d(0x40) = CONST 
    0x35f1S0x82d: v35f1V82d = MLOAD v35eeV82d(0x40)
    0x35f2S0x82d: v35f2V82d(0xe5) = CONST 
    0x35f4S0x82d: v35f4V82d(0x2) = CONST 
    0x35f6S0x82d: v35f6V82d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v35f4V82d(0x2), v35f2V82d(0xe5)
    0x35f7S0x82d: v35f7V82d(0x461bcd) = CONST 
    0x35fbS0x82d: v35fbV82d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v35f7V82d(0x461bcd), v35f6V82d(0x2000000000000000000000000000000000000000000000000000000000)
    0x35fdS0x82d: MSTORE v35f1V82d, v35fbV82d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x35feS0x82d: v35feV82d(0x20) = CONST 
    0x3600S0x82d: v3600V82d(0x4) = CONST 
    0x3603S0x82d: v3603V82d = ADD v35f1V82d, v3600V82d(0x4)
    0x3604S0x82d: MSTORE v3603V82d, v35feV82d(0x20)
    0x3605S0x82d: v3605V82d(0x2e) = CONST 
    0x3607S0x82d: v3607V82d(0x24) = CONST 
    0x360aS0x82d: v360aV82d = ADD v35f1V82d, v3607V82d(0x24)
    0x360bS0x82d: MSTORE v360aV82d, v3605V82d(0x2e)
    0x360cS0x82d: v360cV82d(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75) = CONST 
    0x362dS0x82d: v362dV82d(0x44) = CONST 
    0x3630S0x82d: v3630V82d = ADD v35f1V82d, v362dV82d(0x44)
    0x3631S0x82d: MSTORE v3630V82d, v360cV82d(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75)
    0x3632S0x82d: v3632V82d(0x737420626520706f736974697665000000000000000000000000000000000000) = CONST 
    0x3653S0x82d: v3653V82d(0x64) = CONST 
    0x3656S0x82d: v3656V82d = ADD v35f1V82d, v3653V82d(0x64)
    0x3657S0x82d: MSTORE v3656V82d, v3632V82d(0x737420626520706f736974697665000000000000000000000000000000000000)
    0x3659S0x82d: v3659V82d = MLOAD v35eeV82d(0x40)
    0x365dS0x82d: v365dV82d(0x0) = SUB v35f1V82d, v3659V82d
    0x365eS0x82d: v365eV82d(0x84) = CONST 
    0x3660S0x82d: v3660V82d(0x84) = ADD v365eV82d(0x84), v365dV82d(0x0)
    0x3662S0x82d: REVERT v3659V82d, v3660V82d(0x84)

    Begin block 0x3663B0x82d
    prev=[0x35c8B0x82d], succ=[0x366cB0x82d]
    =================================
    0x3664S0x82d: v3664V82d(0x366c) = CONST 
    0x3668S0x82d: v3668V82d(0x206a) = CONST 
    0x366bS0x82d: v366b_0V82d = CALLPRIVATE v3668V82d(0x206a), v345d_0V82d, v3664V82d(0x366c)

    Begin block 0x366cB0x82d
    prev=[0x3663B0x82d], succ=[0x3676B0x82d, 0x36ebB0x82d]
    =================================
    0x366fS0x82d: v366fV82d = ADD v88a, v864
    0x3670S0x82d: v3670V82d = GT v366fV82d, v366b_0V82d
    0x3671S0x82d: v3671V82d = ISZERO v3670V82d
    0x3672S0x82d: v3672V82d(0x36eb) = CONST 
    0x3675S0x82d: JUMPI v3672V82d(0x36eb), v3671V82d

    Begin block 0x3676B0x82d
    prev=[0x366cB0x82d], succ=[]
    =================================
    0x3676S0x82d: v3676V82d(0x40) = CONST 
    0x3679S0x82d: v3679V82d = MLOAD v3676V82d(0x40)
    0x367aS0x82d: v367aV82d(0xe5) = CONST 
    0x367cS0x82d: v367cV82d(0x2) = CONST 
    0x367eS0x82d: v367eV82d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v367cV82d(0x2), v367aV82d(0xe5)
    0x367fS0x82d: v367fV82d(0x461bcd) = CONST 
    0x3683S0x82d: v3683V82d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v367fV82d(0x461bcd), v367eV82d(0x2000000000000000000000000000000000000000000000000000000000)
    0x3685S0x82d: MSTORE v3679V82d, v3683V82d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3686S0x82d: v3686V82d(0x20) = CONST 
    0x3688S0x82d: v3688V82d(0x4) = CONST 
    0x368bS0x82d: v368bV82d = ADD v3679V82d, v3688V82d(0x4)
    0x368cS0x82d: MSTORE v368bV82d, v3686V82d(0x20)
    0x368dS0x82d: v368dV82d(0x31) = CONST 
    0x368fS0x82d: v368fV82d(0x24) = CONST 
    0x3692S0x82d: v3692V82d = ADD v3679V82d, v368fV82d(0x24)
    0x3693S0x82d: MSTORE v3692V82d, v368dV82d(0x31)
    0x3694S0x82d: v3694V82d(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665722061) = CONST 
    0x36b5S0x82d: v36b5V82d(0x44) = CONST 
    0x36b8S0x82d: v36b8V82d = ADD v3679V82d, v36b5V82d(0x44)
    0x36b9S0x82d: MSTORE v36b8V82d, v3694V82d(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665722061)
    0x36baS0x82d: v36baV82d(0x6e64207265776172642072656c61796572000000000000000000000000000000) = CONST 
    0x36dbS0x82d: v36dbV82d(0x64) = CONST 
    0x36deS0x82d: v36deV82d = ADD v3679V82d, v36dbV82d(0x64)
    0x36dfS0x82d: MSTORE v36deV82d, v36baV82d(0x6e64207265776172642072656c61796572000000000000000000000000000000)
    0x36e1S0x82d: v36e1V82d = MLOAD v3676V82d(0x40)
    0x36e5S0x82d: v36e5V82d(0x0) = SUB v3679V82d, v36e1V82d
    0x36e6S0x82d: v36e6V82d(0x84) = CONST 
    0x36e8S0x82d: v36e8V82d(0x84) = ADD v36e6V82d(0x84), v36e5V82d(0x0)
    0x36eaS0x82d: REVERT v36e1V82d, v36e8V82d(0x84)

    Begin block 0x36ebB0x82d
    prev=[0x366cB0x82d], succ=[0x53d9B0x82d]
    =================================
    0x36ecS0x82d: v36ecV82d(0x53d9) = CONST 
    0x36f2S0x82d: v36f2V82d(0x4176) = CONST 
    0x36f5S0x82d: CALLPRIVATE v36f2V82d(0x4176), v864, v345d_0V82d, v85f, v36ecV82d(0x53d9)

    Begin block 0x53d9B0x82d
    prev=[0x36ebB0x82d], succ=[0x246d0x3366B0x82d]
    =================================
    0x53daS0x82d: v53daV82d(0x246d) = CONST 
    0x53ddS0x82d: v53ddV82d = CALLER 
    0x53e0S0x82d: v53e0V82d(0x4176) = CONST 
    0x53e3S0x82d: CALLPRIVATE v53e0V82d(0x4176), v88a, v345d_0V82d, v53ddV82d, v53daV82d(0x246d)

    Begin block 0x246d0x3366B0x82d
    prev=[0x53d9B0x82d], succ=[0x51b4]
    =================================
    0x246f0x3366S0x82d: v3366246fV82d(0x1) = CONST 
    0x247b0x3366S0x82d: JUMP v851(0x51b4)

    Begin block 0x51b4
    prev=[0x246d0x3366B0x82d], succ=[]
    =================================
    0x51b5: v51b5(0x40) = CONST 
    0x51b8: v51b8 = MLOAD v51b5(0x40)
    0x51ba: v51ba = ISZERO v3366246fV82d(0x1)
    0x51bb: v51bb = ISZERO v51ba
    0x51bd: MSTORE v51b8, v51bb
    0x51be: v51be = MLOAD v51b5(0x40)
    0x51c2: v51c2(0x0) = SUB v51b8, v51be
    0x51c3: v51c3(0x20) = CONST 
    0x51c5: v51c5(0x20) = ADD v51c3(0x20), v51c2(0x0)
    0x51c7: RETURN v51be, v51c5(0x20)

}

function pendingOwner()() public {
    Begin block 0x893
    prev=[], succ=[0x89b, 0x89f]
    =================================
    0x894: v894 = CALLVALUE 
    0x896: v896 = ISZERO v894
    0x897: v897(0x89f) = CONST 
    0x89a: JUMPI v897(0x89f), v896

    Begin block 0x89b
    prev=[0x893], succ=[]
    =================================
    0x89b: v89b(0x0) = CONST 
    0x89e: REVERT v89b(0x0), v89b(0x0)

    Begin block 0x89f
    prev=[0x893], succ=[0x36f6]
    =================================
    0x8a1: v8a1(0x51e7) = CONST 
    0x8a4: v8a4(0x36f6) = CONST 
    0x8a7: JUMP v8a4(0x36f6)

    Begin block 0x36f6
    prev=[0x89f], succ=[0x51e7]
    =================================
    0x36f7: v36f7(0x1) = CONST 
    0x36f9: v36f9 = SLOAD v36f7(0x1)
    0x36fa: v36fa(0x1) = CONST 
    0x36fc: v36fc(0xa0) = CONST 
    0x36fe: v36fe(0x2) = CONST 
    0x3700: v3700(0x10000000000000000000000000000000000000000) = EXP v36fe(0x2), v36fc(0xa0)
    0x3701: v3701(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3700(0x10000000000000000000000000000000000000000), v36fa(0x1)
    0x3702: v3702 = AND v3701(0xffffffffffffffffffffffffffffffffffffffff), v36f9
    0x3704: JUMP v8a1(0x51e7)

    Begin block 0x51e7
    prev=[0x36f6], succ=[]
    =================================
    0x51e8: v51e8(0x40) = CONST 
    0x51eb: v51eb = MLOAD v51e8(0x40)
    0x51ec: v51ec(0x1) = CONST 
    0x51ee: v51ee(0xa0) = CONST 
    0x51f0: v51f0(0x2) = CONST 
    0x51f2: v51f2(0x10000000000000000000000000000000000000000) = EXP v51f0(0x2), v51ee(0xa0)
    0x51f3: v51f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51f2(0x10000000000000000000000000000000000000000), v51ec(0x1)
    0x51f6: v51f6 = AND v3702, v51f3(0xffffffffffffffffffffffffffffffffffffffff)
    0x51f8: MSTORE v51eb, v51f6
    0x51f9: v51f9 = MLOAD v51e8(0x40)
    0x51fd: v51fd(0x0) = SUB v51eb, v51f9
    0x51fe: v51fe(0x20) = CONST 
    0x5200: v5200(0x20) = ADD v51fe(0x20), v51fd(0x0)
    0x5202: RETURN v51f9, v5200(0x20)

}

function setFee(address,uint256)() public {
    Begin block 0x8a8
    prev=[], succ=[0x8b0, 0x8b4]
    =================================
    0x8a9: v8a9 = CALLVALUE 
    0x8ab: v8ab = ISZERO v8a9
    0x8ac: v8ac(0x8b4) = CONST 
    0x8af: JUMPI v8ac(0x8b4), v8ab

    Begin block 0x8b0
    prev=[0x8a8], succ=[]
    =================================
    0x8b0: v8b0(0x0) = CONST 
    0x8b3: REVERT v8b0(0x0), v8b0(0x0)

    Begin block 0x8b4
    prev=[0x8a8], succ=[0x3705B0x8b4]
    =================================
    0x8b6: v8b6(0x5222) = CONST 
    0x8b9: v8b9(0x1) = CONST 
    0x8bb: v8bb(0xa0) = CONST 
    0x8bd: v8bd(0x2) = CONST 
    0x8bf: v8bf(0x10000000000000000000000000000000000000000) = EXP v8bd(0x2), v8bb(0xa0)
    0x8c0: v8c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8bf(0x10000000000000000000000000000000000000000), v8b9(0x1)
    0x8c1: v8c1(0x4) = CONST 
    0x8c3: v8c3 = CALLDATALOAD v8c1(0x4)
    0x8c4: v8c4 = AND v8c3, v8c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x8c5: v8c5(0x24) = CONST 
    0x8c7: v8c7 = CALLDATALOAD v8c5(0x24)
    0x8c8: v8c8(0x3705) = CONST 
    0x8cb: JUMP v8c8(0x3705), v8c7, v8c4, v8b6(0x5222)

    Begin block 0x3705B0x8b4
    prev=[0x8b4], succ=[0x3718B0x8b4, 0x371cB0x8b4]
    =================================
    0x3706S0x8b4: v3706V8b4(0x0) = CONST 
    0x3708S0x8b4: v3708V8b4 = SLOAD v3706V8b4(0x0)
    0x3709S0x8b4: v3709V8b4(0x1) = CONST 
    0x370bS0x8b4: v370bV8b4(0xa0) = CONST 
    0x370dS0x8b4: v370dV8b4(0x2) = CONST 
    0x370fS0x8b4: v370fV8b4(0x10000000000000000000000000000000000000000) = EXP v370dV8b4(0x2), v370bV8b4(0xa0)
    0x3710S0x8b4: v3710V8b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v370fV8b4(0x10000000000000000000000000000000000000000), v3709V8b4(0x1)
    0x3711S0x8b4: v3711V8b4 = AND v3710V8b4(0xffffffffffffffffffffffffffffffffffffffff), v3708V8b4
    0x3712S0x8b4: v3712V8b4 = CALLER 
    0x3713S0x8b4: v3713V8b4 = EQ v3712V8b4, v3711V8b4
    0x3714S0x8b4: v3714V8b4(0x371c) = CONST 
    0x3717S0x8b4: JUMPI v3714V8b4(0x371c), v3713V8b4

    Begin block 0x3718B0x8b4
    prev=[0x3705B0x8b4], succ=[]
    =================================
    0x3718S0x8b4: v3718V8b4(0x0) = CONST 
    0x371bS0x8b4: REVERT v3718V8b4(0x0), v3718V8b4(0x0)

    Begin block 0x371cB0x8b4
    prev=[0x3705B0x8b4], succ=[0x372fB0x8b4, 0x3733B0x8b4]
    =================================
    0x371dS0x8b4: v371dV8b4(0x1) = CONST 
    0x371fS0x8b4: v371fV8b4 = SLOAD v371dV8b4(0x1)
    0x3720S0x8b4: v3720V8b4(0xa0) = CONST 
    0x3722S0x8b4: v3722V8b4(0x2) = CONST 
    0x3724S0x8b4: v3724V8b4(0x10000000000000000000000000000000000000000) = EXP v3722V8b4(0x2), v3720V8b4(0xa0)
    0x3726S0x8b4: v3726V8b4 = DIV v371fV8b4, v3724V8b4(0x10000000000000000000000000000000000000000)
    0x3727S0x8b4: v3727V8b4(0xff) = CONST 
    0x3729S0x8b4: v3729V8b4 = AND v3727V8b4(0xff), v3726V8b4
    0x372aS0x8b4: v372aV8b4 = ISZERO v3729V8b4
    0x372bS0x8b4: v372bV8b4(0x3733) = CONST 
    0x372eS0x8b4: JUMPI v372bV8b4(0x3733), v372aV8b4

    Begin block 0x372fB0x8b4
    prev=[0x371cB0x8b4], succ=[]
    =================================
    0x372fS0x8b4: v372fV8b4(0x0) = CONST 
    0x3732S0x8b4: REVERT v372fV8b4(0x0), v372fV8b4(0x0)

    Begin block 0x3733B0x8b4
    prev=[0x371cB0x8b4], succ=[0x373cB0x8b4]
    =================================
    0x3734S0x8b4: v3734V8b4(0x373c) = CONST 
    0x3738S0x8b4: v3738V8b4(0x162d) = CONST 
    0x373bS0x8b4: v373b_0V8b4 = CALLPRIVATE v3738V8b4(0x162d), v8c4, v3734V8b4(0x373c)

    Begin block 0x373cB0x8b4
    prev=[0x3733B0x8b4], succ=[0x3743B0x8b4, 0x37a6B0x8b4]
    =================================
    0x373dS0x8b4: v373dV8b4 = ISZERO v373b_0V8b4
    0x373eS0x8b4: v373eV8b4 = ISZERO v373dV8b4
    0x373fS0x8b4: v373fV8b4(0x37a6) = CONST 
    0x3742S0x8b4: JUMPI v373fV8b4(0x37a6), v373eV8b4

    Begin block 0x3743B0x8b4
    prev=[0x373cB0x8b4], succ=[]
    =================================
    0x3743S0x8b4: v3743V8b4(0x40) = CONST 
    0x3746S0x8b4: v3746V8b4 = MLOAD v3743V8b4(0x40)
    0x3747S0x8b4: v3747V8b4(0xe5) = CONST 
    0x3749S0x8b4: v3749V8b4(0x2) = CONST 
    0x374bS0x8b4: v374bV8b4(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3749V8b4(0x2), v3747V8b4(0xe5)
    0x374cS0x8b4: v374cV8b4(0x461bcd) = CONST 
    0x3750S0x8b4: v3750V8b4(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v374cV8b4(0x461bcd), v374bV8b4(0x2000000000000000000000000000000000000000000000000000000000)
    0x3752S0x8b4: MSTORE v3746V8b4, v3750V8b4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3753S0x8b4: v3753V8b4(0x20) = CONST 
    0x3755S0x8b4: v3755V8b4(0x4) = CONST 
    0x3758S0x8b4: v3758V8b4 = ADD v3746V8b4, v3755V8b4(0x4)
    0x3759S0x8b4: MSTORE v3758V8b4, v3753V8b4(0x20)
    0x375aS0x8b4: v375aV8b4(0x3e) = CONST 
    0x375cS0x8b4: v375cV8b4(0x24) = CONST 
    0x375fS0x8b4: v375fV8b4 = ADD v3746V8b4, v375cV8b4(0x24)
    0x3760S0x8b4: MSTORE v375fV8b4, v375aV8b4(0x3e)
    0x3761S0x8b4: v3761V8b4(0x0) = CONST 
    0x3764S0x8b4: v3764V8b4 = MLOAD v3761V8b4(0x0)
    0x3765S0x8b4: v3765V8b4(0x20) = CONST 
    0x3767S0x8b4: v3767V8b4(0x4a50) = CONST 
    0x376fS0x8b4: MSTORE v3761V8b4(0x0), v3764V8b4
    0x3770S0x8b4: v3770V8b4(0x44) = CONST 
    0x3773S0x8b4: v3773V8b4 = ADD v3746V8b4, v3770V8b4(0x44)
    0x3774S0x8b4: MSTORE v3773V8b4, v557aV8b4(0x537461626c65636f696e206d7573742062652077686974656c69737465642070)
    0x3775S0x8b4: v3775V8b4(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000) = CONST 
    0x3796S0x8b4: v3796V8b4(0x64) = CONST 
    0x3799S0x8b4: v3799V8b4 = ADD v3746V8b4, v3796V8b4(0x64)
    0x379aS0x8b4: MSTORE v3799V8b4, v3775V8b4(0x72696f7220746f2073657474696e6720636f6e76657273696f6e206665650000)
    0x379cS0x8b4: v379cV8b4 = MLOAD v3743V8b4(0x40)
    0x37a0S0x8b4: v37a0V8b4(0x0) = SUB v3746V8b4, v379cV8b4
    0x37a1S0x8b4: v37a1V8b4(0x84) = CONST 
    0x37a3S0x8b4: v37a3V8b4(0x84) = ADD v37a1V8b4(0x84), v37a0V8b4(0x0)
    0x37a5S0x8b4: REVERT v379cV8b4, v37a3V8b4(0x84)
    0x557aS0x8b4: v557aV8b4(0x537461626c65636f696e206d7573742062652077686974656c69737465642070) = CONST 

    Begin block 0x37a6B0x8b4
    prev=[0x373cB0x8b4], succ=[0x3814B0x8b4, 0x3818B0x8b4]
    =================================
    0x37a7S0x8b4: v37a7V8b4(0x4) = CONST 
    0x37aaS0x8b4: v37aaV8b4 = SLOAD v37a7V8b4(0x4)
    0x37abS0x8b4: v37abV8b4(0x40) = CONST 
    0x37aeS0x8b4: v37aeV8b4 = MLOAD v37abV8b4(0x40)
    0x37afS0x8b4: v37afV8b4(0xe55156b500000000000000000000000000000000000000000000000000000000) = CONST 
    0x37d1S0x8b4: MSTORE v37aeV8b4, v37afV8b4(0xe55156b500000000000000000000000000000000000000000000000000000000)
    0x37d2S0x8b4: v37d2V8b4(0x1) = CONST 
    0x37d4S0x8b4: v37d4V8b4(0xa0) = CONST 
    0x37d6S0x8b4: v37d6V8b4(0x2) = CONST 
    0x37d8S0x8b4: v37d8V8b4(0x10000000000000000000000000000000000000000) = EXP v37d6V8b4(0x2), v37d4V8b4(0xa0)
    0x37d9S0x8b4: v37d9V8b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37d8V8b4(0x10000000000000000000000000000000000000000), v37d2V8b4(0x1)
    0x37dcS0x8b4: v37dcV8b4 = AND v37d9V8b4(0xffffffffffffffffffffffffffffffffffffffff), v8c4
    0x37dfS0x8b4: v37dfV8b4 = ADD v37aeV8b4, v37a7V8b4(0x4)
    0x37e3S0x8b4: MSTORE v37dfV8b4, v37dcV8b4
    0x37e4S0x8b4: v37e4V8b4(0x24) = CONST 
    0x37e7S0x8b4: v37e7V8b4 = ADD v37aeV8b4, v37e4V8b4(0x24)
    0x37eaS0x8b4: MSTORE v37e7V8b4, v8c7
    0x37ecS0x8b4: v37ecV8b4 = MLOAD v37abV8b4(0x40)
    0x37f0S0x8b4: v37f0V8b4 = AND v37aaV8b4, v37d9V8b4(0xffffffffffffffffffffffffffffffffffffffff)
    0x37f2S0x8b4: v37f2V8b4(0xe55156b5) = CONST 
    0x37f8S0x8b4: v37f8V8b4(0x44) = CONST 
    0x37fcS0x8b4: v37fcV8b4 = ADD v37aeV8b4, v37f8V8b4(0x44)
    0x37feS0x8b4: v37feV8b4(0x0) = CONST 
    0x3806S0x8b4: v3806V8b4(0x0) = SUB v37aeV8b4, v37ecV8b4
    0x3807S0x8b4: v3807V8b4(0x44) = ADD v3806V8b4(0x0), v37f8V8b4(0x44)
    0x380cS0x8b4: v380cV8b4 = EXTCODESIZE v37f0V8b4
    0x380dS0x8b4: v380dV8b4 = ISZERO v380cV8b4
    0x380fS0x8b4: v380fV8b4 = ISZERO v380dV8b4
    0x3810S0x8b4: v3810V8b4(0x3818) = CONST 
    0x3813S0x8b4: JUMPI v3810V8b4(0x3818), v380fV8b4

    Begin block 0x3814B0x8b4
    prev=[0x37a6B0x8b4], succ=[]
    =================================
    0x3814S0x8b4: v3814V8b4(0x0) = CONST 
    0x3817S0x8b4: REVERT v3814V8b4(0x0), v3814V8b4(0x0)

    Begin block 0x3818B0x8b4
    prev=[0x37a6B0x8b4], succ=[0x3823B0x8b4, 0x382cB0x8b4]
    =================================
    0x381aS0x8b4: v381aV8b4 = GAS 
    0x381bS0x8b4: v381bV8b4 = CALL v381aV8b4, v37f0V8b4, v37feV8b4(0x0), v37ecV8b4, v3807V8b4(0x44), v37ecV8b4, v37feV8b4(0x0)
    0x381cS0x8b4: v381cV8b4 = ISZERO v381bV8b4
    0x381eS0x8b4: v381eV8b4 = ISZERO v381cV8b4
    0x381fS0x8b4: v381fV8b4(0x382c) = CONST 
    0x3822S0x8b4: JUMPI v381fV8b4(0x382c), v381eV8b4

    Begin block 0x3823B0x8b4
    prev=[0x3818B0x8b4], succ=[]
    =================================
    0x3823S0x8b4: v3823V8b4 = RETURNDATASIZE 
    0x3824S0x8b4: v3824V8b4(0x0) = CONST 
    0x3827S0x8b4: RETURNDATACOPY v3824V8b4(0x0), v3824V8b4(0x0), v3823V8b4
    0x3828S0x8b4: v3828V8b4 = RETURNDATASIZE 
    0x3829S0x8b4: v3829V8b4(0x0) = CONST 
    0x382bS0x8b4: REVERT v3829V8b4(0x0), v3828V8b4

    Begin block 0x382cB0x8b4
    prev=[0x3818B0x8b4], succ=[0x5222]
    =================================
    0x3833S0x8b4: JUMP v8b6(0x5222)

    Begin block 0x5222
    prev=[0x382cB0x8b4], succ=[]
    =================================
    0x5223: STOP 

}

function metaBurnCarbonDollar(address,uint256,bytes,uint256,uint256)() public {
    Begin block 0x8cc
    prev=[], succ=[0x8d4, 0x8d8]
    =================================
    0x8cd: v8cd = CALLVALUE 
    0x8cf: v8cf = ISZERO v8cd
    0x8d0: v8d0(0x8d8) = CONST 
    0x8d3: JUMPI v8d0(0x8d8), v8cf

    Begin block 0x8d4
    prev=[0x8cc], succ=[]
    =================================
    0x8d4: v8d4(0x0) = CONST 
    0x8d7: REVERT v8d4(0x0), v8d4(0x0)

    Begin block 0x8d8
    prev=[0x8cc], succ=[0x3834]
    =================================
    0x8da: v8da(0x40) = CONST 
    0x8dd: v8dd = MLOAD v8da(0x40)
    0x8de: v8de(0x20) = CONST 
    0x8e0: v8e0(0x4) = CONST 
    0x8e2: v8e2(0x44) = CONST 
    0x8e4: v8e4 = CALLDATALOAD v8e2(0x44)
    0x8e7: v8e7 = ADD v8e4, v8e0(0x4)
    0x8e8: v8e8 = CALLDATALOAD v8e7
    0x8e9: v8e9(0x1f) = CONST 
    0x8ec: v8ec = ADD v8e8, v8e9(0x1f)
    0x8ef: v8ef = DIV v8ec, v8de(0x20)
    0x8f1: v8f1 = MUL v8de(0x20), v8ef
    0x8f3: v8f3 = ADD v8dd, v8f1
    0x8f5: v8f5 = ADD v8de(0x20), v8f3
    0x8f8: MSTORE v8da(0x40), v8f5
    0x8fb: MSTORE v8dd, v8e8
    0x8fc: v8fc(0x5243) = CONST 
    0x901: v901 = CALLDATALOAD v8e0(0x4)
    0x902: v902(0x1) = CONST 
    0x904: v904(0xa0) = CONST 
    0x906: v906(0x2) = CONST 
    0x908: v908(0x10000000000000000000000000000000000000000) = EXP v906(0x2), v904(0xa0)
    0x909: v909(0xffffffffffffffffffffffffffffffffffffffff) = SUB v908(0x10000000000000000000000000000000000000000), v902(0x1)
    0x90a: v90a = AND v909(0xffffffffffffffffffffffffffffffffffffffff), v901
    0x90c: v90c(0x24) = CONST 
    0x90f: v90f = CALLDATALOAD v90c(0x24)
    0x911: v911 = CALLDATASIZE 
    0x914: v914(0x64) = CONST 
    0x918: v918 = ADD v90c(0x24), v8e4
    0x91e: v91e = ADD v8dd, v8de(0x20)
    0x924: CALLDATACOPY v91e, v918, v8e8
    0x92b: v92b = CALLDATALOAD v914(0x64)
    0x930: v930(0x20) = CONST 
    0x934: v934(0x84) = ADD v914(0x64), v930(0x20)
    0x935: v935 = CALLDATALOAD v934(0x84)
    0x938: v938(0x3834) = CONST 
    0x93d: JUMP v938(0x3834)

    Begin block 0x3834
    prev=[0x8d8], succ=[0x384e, 0x3852]
    =================================
    0x3835: v3835(0x1) = CONST 
    0x3837: v3837 = SLOAD v3835(0x1)
    0x3838: v3838(0x0) = CONST 
    0x383f: v383f(0xa0) = CONST 
    0x3841: v3841(0x2) = CONST 
    0x3843: v3843(0x10000000000000000000000000000000000000000) = EXP v3841(0x2), v383f(0xa0)
    0x3845: v3845 = DIV v3837, v3843(0x10000000000000000000000000000000000000000)
    0x3846: v3846(0xff) = CONST 
    0x3848: v3848 = AND v3846(0xff), v3845
    0x3849: v3849 = ISZERO v3848
    0x384a: v384a(0x3852) = CONST 
    0x384d: JUMPI v384a(0x3852), v3849

    Begin block 0x384e
    prev=[0x3834], succ=[]
    =================================
    0x384e: v384e(0x0) = CONST 
    0x3851: REVERT v384e(0x0), v384e(0x0)

    Begin block 0x3852
    prev=[0x3834], succ=[0x385e]
    =================================
    0x3853: v3853(0x385e) = CONST 
    0x385a: v385a(0x3204) = CONST 
    0x385d: v385d_0 = CALLPRIVATE v385a(0x3204), v935, v92b, v90f, v90a, v3853(0x385e)

    Begin block 0x385e
    prev=[0x3852], succ=[0x386a]
    =================================
    0x3861: v3861(0x386a) = CONST 
    0x3866: v3866(0x44ed) = CONST 
    0x3869: v3869_0 = CALLPRIVATE v3866(0x44ed), v8dd, v385d_0, v3861(0x386a)

    Begin block 0x386a
    prev=[0x385e], succ=[0x38ba, 0x38be]
    =================================
    0x386b: v386b(0x3) = CONST 
    0x386d: v386d = SLOAD v386b(0x3)
    0x386e: v386e(0x40) = CONST 
    0x3871: v3871 = MLOAD v386e(0x40)
    0x3872: v3872(0xe0) = CONST 
    0x3874: v3874(0x2) = CONST 
    0x3876: v3876(0x100000000000000000000000000000000000000000000000000000000) = EXP v3874(0x2), v3872(0xe0)
    0x3877: v3877(0x7ccce851) = CONST 
    0x387c: v387c(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v3877(0x7ccce851), v3876(0x100000000000000000000000000000000000000000000000000000000)
    0x387e: MSTORE v3871, v387c(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x387f: v387f(0x1) = CONST 
    0x3881: v3881(0xa0) = CONST 
    0x3883: v3883(0x2) = CONST 
    0x3885: v3885(0x10000000000000000000000000000000000000000) = EXP v3883(0x2), v3881(0xa0)
    0x3886: v3886(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3885(0x10000000000000000000000000000000000000000), v387f(0x1)
    0x3889: v3889 = AND v3869_0, v3886(0xffffffffffffffffffffffffffffffffffffffff)
    0x388a: v388a(0x4) = CONST 
    0x388d: v388d = ADD v3871, v388a(0x4)
    0x388e: MSTORE v388d, v3889
    0x3890: v3890 = MLOAD v386e(0x40)
    0x3895: v3895 = AND v386d, v3886(0xffffffffffffffffffffffffffffffffffffffff)
    0x3897: v3897(0x7ccce851) = CONST 
    0x389d: v389d(0x24) = CONST 
    0x38a1: v38a1 = ADD v3871, v389d(0x24)
    0x38a3: v38a3(0x20) = CONST 
    0x38ab: v38ab(0x0) = SUB v3871, v3890
    0x38ac: v38ac(0x24) = ADD v38ab(0x0), v389d(0x24)
    0x38ae: v38ae(0x0) = CONST 
    0x38b2: v38b2 = EXTCODESIZE v3895
    0x38b3: v38b3 = ISZERO v38b2
    0x38b5: v38b5 = ISZERO v38b3
    0x38b6: v38b6(0x38be) = CONST 
    0x38b9: JUMPI v38b6(0x38be), v38b5

    Begin block 0x38ba
    prev=[0x386a], succ=[]
    =================================
    0x38ba: v38ba(0x0) = CONST 
    0x38bd: REVERT v38ba(0x0), v38ba(0x0)

    Begin block 0x38be
    prev=[0x386a], succ=[0x38c9, 0x38d2]
    =================================
    0x38c0: v38c0 = GAS 
    0x38c1: v38c1 = CALL v38c0, v3895, v38ae(0x0), v3890, v38ac(0x24), v3890, v38a3(0x20)
    0x38c2: v38c2 = ISZERO v38c1
    0x38c4: v38c4 = ISZERO v38c2
    0x38c5: v38c5(0x38d2) = CONST 
    0x38c8: JUMPI v38c5(0x38d2), v38c4

    Begin block 0x38c9
    prev=[0x38be], succ=[]
    =================================
    0x38c9: v38c9 = RETURNDATASIZE 
    0x38ca: v38ca(0x0) = CONST 
    0x38cd: RETURNDATACOPY v38ca(0x0), v38ca(0x0), v38c9
    0x38ce: v38ce = RETURNDATASIZE 
    0x38cf: v38cf(0x0) = CONST 
    0x38d1: REVERT v38cf(0x0), v38ce

    Begin block 0x38d2
    prev=[0x38be], succ=[0x38e4, 0x38e8]
    =================================
    0x38d7: v38d7(0x40) = CONST 
    0x38d9: v38d9 = MLOAD v38d7(0x40)
    0x38da: v38da = RETURNDATASIZE 
    0x38db: v38db(0x20) = CONST 
    0x38de: v38de = LT v38da, v38db(0x20)
    0x38df: v38df = ISZERO v38de
    0x38e0: v38e0(0x38e8) = CONST 
    0x38e3: JUMPI v38e0(0x38e8), v38df

    Begin block 0x38e4
    prev=[0x38d2], succ=[]
    =================================
    0x38e4: v38e4(0x0) = CONST 
    0x38e7: REVERT v38e4(0x0), v38e4(0x0)

    Begin block 0x38e8
    prev=[0x38d2], succ=[0x38f0, 0x393f]
    =================================
    0x38ea: v38ea = MLOAD v38d9
    0x38eb: v38eb = ISZERO v38ea
    0x38ec: v38ec(0x393f) = CONST 
    0x38ef: JUMPI v38ec(0x393f), v38eb

    Begin block 0x38f0
    prev=[0x38e8], succ=[]
    =================================
    0x38f0: v38f0(0x40) = CONST 
    0x38f3: v38f3 = MLOAD v38f0(0x40)
    0x38f4: v38f4(0xe5) = CONST 
    0x38f6: v38f6(0x2) = CONST 
    0x38f8: v38f8(0x2000000000000000000000000000000000000000000000000000000000) = EXP v38f6(0x2), v38f4(0xe5)
    0x38f9: v38f9(0x461bcd) = CONST 
    0x38fd: v38fd(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v38f9(0x461bcd), v38f8(0x2000000000000000000000000000000000000000000000000000000000)
    0x38ff: MSTORE v38f3, v38fd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3900: v3900(0x20) = CONST 
    0x3902: v3902(0x4) = CONST 
    0x3905: v3905 = ADD v38f3, v3902(0x4)
    0x3906: MSTORE v3905, v3900(0x20)
    0x3907: v3907(0x15) = CONST 
    0x3909: v3909(0x24) = CONST 
    0x390c: v390c = ADD v38f3, v3909(0x24)
    0x390d: MSTORE v390c, v3907(0x15)
    0x390e: v390e(0x7369676e657220697320626c61636b6c69737465640000000000000000000000) = CONST 
    0x392f: v392f(0x44) = CONST 
    0x3932: v3932 = ADD v38f3, v392f(0x44)
    0x3933: MSTORE v3932, v390e(0x7369676e657220697320626c61636b6c69737465640000000000000000000000)
    0x3935: v3935 = MLOAD v38f0(0x40)
    0x3939: v3939(0x0) = SUB v38f3, v3935
    0x393a: v393a(0x64) = CONST 
    0x393c: v393c(0x64) = ADD v393a(0x64), v3939(0x0)
    0x393e: REVERT v3935, v393c(0x64)

    Begin block 0x393f
    prev=[0x38e8], succ=[0x395f, 0x39d4]
    =================================
    0x3940: v3940(0x1) = CONST 
    0x3942: v3942(0xa0) = CONST 
    0x3944: v3944(0x2) = CONST 
    0x3946: v3946(0x10000000000000000000000000000000000000000) = EXP v3944(0x2), v3942(0xa0)
    0x3947: v3947(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3946(0x10000000000000000000000000000000000000000), v3940(0x1)
    0x3949: v3949 = AND v3869_0, v3947(0xffffffffffffffffffffffffffffffffffffffff)
    0x394a: v394a(0x0) = CONST 
    0x394e: MSTORE v394a(0x0), v3949
    0x394f: v394f(0x5) = CONST 
    0x3951: v3951(0x20) = CONST 
    0x3953: MSTORE v3951(0x20), v394f(0x5)
    0x3954: v3954(0x40) = CONST 
    0x3957: v3957 = SHA3 v394a(0x0), v3954(0x40)
    0x3958: v3958 = SLOAD v3957
    0x395a: v395a = EQ v92b, v3958
    0x395b: v395b(0x39d4) = CONST 
    0x395e: JUMPI v395b(0x39d4), v395a

    Begin block 0x395f
    prev=[0x393f], succ=[]
    =================================
    0x395f: v395f(0x40) = CONST 
    0x3962: v3962 = MLOAD v395f(0x40)
    0x3963: v3963(0xe5) = CONST 
    0x3965: v3965(0x2) = CONST 
    0x3967: v3967(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3965(0x2), v3963(0xe5)
    0x3968: v3968(0x461bcd) = CONST 
    0x396c: v396c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3968(0x461bcd), v3967(0x2000000000000000000000000000000000000000000000000000000000)
    0x396e: MSTORE v3962, v396c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x396f: v396f(0x20) = CONST 
    0x3971: v3971(0x4) = CONST 
    0x3974: v3974 = ADD v3962, v3971(0x4)
    0x3975: MSTORE v3974, v396f(0x20)
    0x3976: v3976(0x2b) = CONST 
    0x3978: v3978(0x24) = CONST 
    0x397b: v397b = ADD v3962, v3978(0x24)
    0x397c: MSTORE v397b, v3976(0x2b)
    0x397d: v397d(0x74686973207472616e73616374696f6e2068617320616c726561647920626565) = CONST 
    0x399e: v399e(0x44) = CONST 
    0x39a1: v39a1 = ADD v3962, v399e(0x44)
    0x39a2: MSTORE v39a1, v397d(0x74686973207472616e73616374696f6e2068617320616c726561647920626565)
    0x39a3: v39a3(0x6e2062726f616463617374000000000000000000000000000000000000000000) = CONST 
    0x39c4: v39c4(0x64) = CONST 
    0x39c7: v39c7 = ADD v3962, v39c4(0x64)
    0x39c8: MSTORE v39c7, v39a3(0x6e2062726f616463617374000000000000000000000000000000000000000000)
    0x39ca: v39ca = MLOAD v395f(0x40)
    0x39ce: v39ce(0x0) = SUB v3962, v39ca
    0x39cf: v39cf(0x84) = CONST 
    0x39d1: v39d1(0x84) = ADD v39cf(0x84), v39ce(0x0)
    0x39d3: REVERT v39ca, v39d1(0x84)

    Begin block 0x39d4
    prev=[0x393f], succ=[0x39fa, 0x3a6f]
    =================================
    0x39d5: v39d5(0x1) = CONST 
    0x39d7: v39d7(0xa0) = CONST 
    0x39d9: v39d9(0x2) = CONST 
    0x39db: v39db(0x10000000000000000000000000000000000000000) = EXP v39d9(0x2), v39d7(0xa0)
    0x39dc: v39dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39db(0x10000000000000000000000000000000000000000), v39d5(0x1)
    0x39de: v39de = AND v3869_0, v39dc(0xffffffffffffffffffffffffffffffffffffffff)
    0x39df: v39df(0x0) = CONST 
    0x39e3: MSTORE v39df(0x0), v39de
    0x39e4: v39e4(0x5) = CONST 
    0x39e6: v39e6(0x20) = CONST 
    0x39e8: MSTORE v39e6(0x20), v39e4(0x5)
    0x39e9: v39e9(0x40) = CONST 
    0x39ec: v39ec = SHA3 v39df(0x0), v39e9(0x40)
    0x39ee: v39ee = SLOAD v39ec
    0x39ef: v39ef(0x1) = CONST 
    0x39f1: v39f1 = ADD v39ef(0x1), v39ee
    0x39f3: SSTORE v39ec, v39f1
    0x39f5: v39f5 = GT v935, v39df(0x0)
    0x39f6: v39f6(0x3a6f) = CONST 
    0x39f9: JUMPI v39f6(0x3a6f), v39f5

    Begin block 0x39fa
    prev=[0x39d4], succ=[]
    =================================
    0x39fa: v39fa(0x40) = CONST 
    0x39fd: v39fd = MLOAD v39fa(0x40)
    0x39fe: v39fe(0xe5) = CONST 
    0x3a00: v3a00(0x2) = CONST 
    0x3a02: v3a02(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3a00(0x2), v39fe(0xe5)
    0x3a03: v3a03(0x461bcd) = CONST 
    0x3a07: v3a07(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3a03(0x461bcd), v3a02(0x2000000000000000000000000000000000000000000000000000000000)
    0x3a09: MSTORE v39fd, v3a07(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3a0a: v3a0a(0x20) = CONST 
    0x3a0c: v3a0c(0x4) = CONST 
    0x3a0f: v3a0f = ADD v39fd, v3a0c(0x4)
    0x3a10: MSTORE v3a0f, v3a0a(0x20)
    0x3a11: v3a11(0x2e) = CONST 
    0x3a13: v3a13(0x24) = CONST 
    0x3a16: v3a16 = ADD v39fd, v3a13(0x24)
    0x3a17: MSTORE v3a16, v3a11(0x2e)
    0x3a18: v3a18(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75) = CONST 
    0x3a39: v3a39(0x44) = CONST 
    0x3a3c: v3a3c = ADD v39fd, v3a39(0x44)
    0x3a3d: MSTORE v3a3c, v3a18(0x72657761726420746f20696e63656e746976697a652072656c61796572206d75)
    0x3a3e: v3a3e(0x737420626520706f736974697665000000000000000000000000000000000000) = CONST 
    0x3a5f: v3a5f(0x64) = CONST 
    0x3a62: v3a62 = ADD v39fd, v3a5f(0x64)
    0x3a63: MSTORE v3a62, v3a3e(0x737420626520706f736974697665000000000000000000000000000000000000)
    0x3a65: v3a65 = MLOAD v39fa(0x40)
    0x3a69: v3a69(0x0) = SUB v39fd, v3a65
    0x3a6a: v3a6a(0x84) = CONST 
    0x3a6c: v3a6c(0x84) = ADD v3a6a(0x84), v3a69(0x0)
    0x3a6e: REVERT v3a65, v3a6c(0x84)

    Begin block 0x3a6f
    prev=[0x39d4], succ=[0x3a78]
    =================================
    0x3a70: v3a70(0x3a78) = CONST 
    0x3a74: v3a74(0x206a) = CONST 
    0x3a77: v3a77_0 = CALLPRIVATE v3a74(0x206a), v3869_0, v3a70(0x3a78)

    Begin block 0x3a78
    prev=[0x3a6f], succ=[0x3a82, 0x3af7]
    =================================
    0x3a7b: v3a7b = ADD v935, v90f
    0x3a7c: v3a7c = GT v3a7b, v3a77_0
    0x3a7d: v3a7d = ISZERO v3a7c
    0x3a7e: v3a7e(0x3af7) = CONST 
    0x3a81: JUMPI v3a7e(0x3af7), v3a7d

    Begin block 0x3a82
    prev=[0x3a78], succ=[]
    =================================
    0x3a82: v3a82(0x40) = CONST 
    0x3a85: v3a85 = MLOAD v3a82(0x40)
    0x3a86: v3a86(0xe5) = CONST 
    0x3a88: v3a88(0x2) = CONST 
    0x3a8a: v3a8a(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3a88(0x2), v3a86(0xe5)
    0x3a8b: v3a8b(0x461bcd) = CONST 
    0x3a8f: v3a8f(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3a8b(0x461bcd), v3a8a(0x2000000000000000000000000000000000000000000000000000000000)
    0x3a91: MSTORE v3a85, v3a8f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3a92: v3a92(0x20) = CONST 
    0x3a94: v3a94(0x4) = CONST 
    0x3a97: v3a97 = ADD v3a85, v3a94(0x4)
    0x3a98: MSTORE v3a97, v3a92(0x20)
    0x3a99: v3a99(0x2d) = CONST 
    0x3a9b: v3a9b(0x24) = CONST 
    0x3a9e: v3a9e = ADD v3a85, v3a9b(0x24)
    0x3a9f: MSTORE v3a9e, v3a99(0x2d)
    0x3aa0: v3aa0(0x6e6f7420656e6f7567682062616c616e636520746f206275726e20616e642072) = CONST 
    0x3ac1: v3ac1(0x44) = CONST 
    0x3ac4: v3ac4 = ADD v3a85, v3ac1(0x44)
    0x3ac5: MSTORE v3ac4, v3aa0(0x6e6f7420656e6f7567682062616c616e636520746f206275726e20616e642072)
    0x3ac6: v3ac6(0x65776172642072656c6179657200000000000000000000000000000000000000) = CONST 
    0x3ae7: v3ae7(0x64) = CONST 
    0x3aea: v3aea = ADD v3a85, v3ae7(0x64)
    0x3aeb: MSTORE v3aea, v3ac6(0x65776172642072656c6179657200000000000000000000000000000000000000)
    0x3aed: v3aed = MLOAD v3a82(0x40)
    0x3af1: v3af1(0x0) = SUB v3a85, v3aed
    0x3af2: v3af2(0x84) = CONST 
    0x3af4: v3af4(0x84) = ADD v3af2(0x84), v3af1(0x0)
    0x3af6: REVERT v3aed, v3af4(0x84)

    Begin block 0x3af7
    prev=[0x3a78], succ=[0x3b02]
    =================================
    0x3af8: v3af8(0x3b02) = CONST 
    0x3afe: v3afe(0x473f) = CONST 
    0x3b01: CALLPRIVATE v3afe(0x473f), v90f, v90a, v3869_0, v3af8(0x3b02)

    Begin block 0x3b02
    prev=[0x3af7], succ=[0x3b0d]
    =================================
    0x3b03: v3b03(0x3b0d) = CONST 
    0x3b06: v3b06 = CALLER 
    0x3b09: v3b09(0x4176) = CONST 
    0x3b0c: CALLPRIVATE v3b09(0x4176), v935, v3869_0, v3b06, v3b03(0x3b0d)

    Begin block 0x3b0d
    prev=[0x3b02], succ=[0x5243]
    =================================
    0x3b0f: v3b0f(0x1) = CONST 
    0x3b1a: JUMP v8fc(0x5243)

    Begin block 0x5243
    prev=[0x3b0d], succ=[]
    =================================
    0x5244: v5244(0x40) = CONST 
    0x5247: v5247 = MLOAD v5244(0x40)
    0x5249: v5249 = ISZERO v3b0f(0x1)
    0x524a: v524a = ISZERO v5249
    0x524c: MSTORE v5247, v524a
    0x524d: v524d = MLOAD v5244(0x40)
    0x5251: v5251(0x0) = SUB v5247, v524d
    0x5252: v5252(0x20) = CONST 
    0x5254: v5254(0x20) = ADD v5252(0x20), v5251(0x0)
    0x5256: RETURN v524d, v5254(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x93e
    prev=[], succ=[0x946, 0x94a]
    =================================
    0x93f: v93f = CALLVALUE 
    0x941: v941 = ISZERO v93f
    0x942: v942(0x94a) = CONST 
    0x945: JUMPI v942(0x94a), v941

    Begin block 0x946
    prev=[0x93e], succ=[]
    =================================
    0x946: v946(0x0) = CONST 
    0x949: REVERT v946(0x0), v946(0x0)

    Begin block 0x94a
    prev=[0x93e], succ=[0x3b1b]
    =================================
    0x94c: v94c(0x5276) = CONST 
    0x94f: v94f(0x1) = CONST 
    0x951: v951(0xa0) = CONST 
    0x953: v953(0x2) = CONST 
    0x955: v955(0x10000000000000000000000000000000000000000) = EXP v953(0x2), v951(0xa0)
    0x956: v956(0xffffffffffffffffffffffffffffffffffffffff) = SUB v955(0x10000000000000000000000000000000000000000), v94f(0x1)
    0x957: v957(0x4) = CONST 
    0x959: v959 = CALLDATALOAD v957(0x4)
    0x95a: v95a = AND v959, v956(0xffffffffffffffffffffffffffffffffffffffff)
    0x95b: v95b(0x3b1b) = CONST 
    0x95e: JUMP v95b(0x3b1b)

    Begin block 0x3b1b
    prev=[0x94a], succ=[0x3b2e, 0x3b32]
    =================================
    0x3b1c: v3b1c(0x0) = CONST 
    0x3b1e: v3b1e = SLOAD v3b1c(0x0)
    0x3b1f: v3b1f(0x1) = CONST 
    0x3b21: v3b21(0xa0) = CONST 
    0x3b23: v3b23(0x2) = CONST 
    0x3b25: v3b25(0x10000000000000000000000000000000000000000) = EXP v3b23(0x2), v3b21(0xa0)
    0x3b26: v3b26(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b25(0x10000000000000000000000000000000000000000), v3b1f(0x1)
    0x3b27: v3b27 = AND v3b26(0xffffffffffffffffffffffffffffffffffffffff), v3b1e
    0x3b28: v3b28 = CALLER 
    0x3b29: v3b29 = EQ v3b28, v3b27
    0x3b2a: v3b2a(0x3b32) = CONST 
    0x3b2d: JUMPI v3b2a(0x3b32), v3b29

    Begin block 0x3b2e
    prev=[0x3b1b], succ=[]
    =================================
    0x3b2e: v3b2e(0x0) = CONST 
    0x3b31: REVERT v3b2e(0x0), v3b2e(0x0)

    Begin block 0x3b32
    prev=[0x3b1b], succ=[0x3b43, 0x3b47]
    =================================
    0x3b33: v3b33(0x1) = CONST 
    0x3b35: v3b35(0xa0) = CONST 
    0x3b37: v3b37(0x2) = CONST 
    0x3b39: v3b39(0x10000000000000000000000000000000000000000) = EXP v3b37(0x2), v3b35(0xa0)
    0x3b3a: v3b3a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b39(0x10000000000000000000000000000000000000000), v3b33(0x1)
    0x3b3c: v3b3c = AND v95a, v3b3a(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b3d: v3b3d = ISZERO v3b3c
    0x3b3e: v3b3e = ISZERO v3b3d
    0x3b3f: v3b3f(0x3b47) = CONST 
    0x3b42: JUMPI v3b3f(0x3b47), v3b3e

    Begin block 0x3b43
    prev=[0x3b32], succ=[]
    =================================
    0x3b43: v3b43(0x0) = CONST 
    0x3b46: REVERT v3b43(0x0), v3b43(0x0)

    Begin block 0x3b47
    prev=[0x3b32], succ=[0x5276]
    =================================
    0x3b48: v3b48(0x1) = CONST 
    0x3b4b: v3b4b = SLOAD v3b48(0x1)
    0x3b4c: v3b4c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b61: v3b61(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3b4c(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b62: v3b62 = AND v3b61(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3b4b
    0x3b63: v3b63(0x1) = CONST 
    0x3b65: v3b65(0xa0) = CONST 
    0x3b67: v3b67(0x2) = CONST 
    0x3b69: v3b69(0x10000000000000000000000000000000000000000) = EXP v3b67(0x2), v3b65(0xa0)
    0x3b6a: v3b6a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b69(0x10000000000000000000000000000000000000000), v3b63(0x1)
    0x3b6e: v3b6e = AND v3b6a(0xffffffffffffffffffffffffffffffffffffffff), v95a
    0x3b72: v3b72 = OR v3b6e, v3b62
    0x3b74: SSTORE v3b48(0x1), v3b72
    0x3b75: JUMP v94c(0x5276)

    Begin block 0x5276
    prev=[0x3b47], succ=[]
    =================================
    0x5277: STOP 

}

function releaseCarbonDollar(uint256)() public {
    Begin block 0x95f
    prev=[], succ=[0x967, 0x96b]
    =================================
    0x960: v960 = CALLVALUE 
    0x962: v962 = ISZERO v960
    0x963: v963(0x96b) = CONST 
    0x966: JUMPI v963(0x96b), v962

    Begin block 0x967
    prev=[0x95f], succ=[]
    =================================
    0x967: v967(0x0) = CONST 
    0x96a: REVERT v967(0x0), v967(0x0)

    Begin block 0x96b
    prev=[0x95f], succ=[0x3b76]
    =================================
    0x96d: v96d(0x5297) = CONST 
    0x970: v970(0x4) = CONST 
    0x972: v972 = CALLDATALOAD v970(0x4)
    0x973: v973(0x3b76) = CONST 
    0x976: JUMP v973(0x3b76)

    Begin block 0x3b76
    prev=[0x96b], succ=[0x3b8a, 0x3b8e]
    =================================
    0x3b77: v3b77(0x0) = CONST 
    0x3b7a: v3b7a = SLOAD v3b77(0x0)
    0x3b7b: v3b7b(0x1) = CONST 
    0x3b7d: v3b7d(0xa0) = CONST 
    0x3b7f: v3b7f(0x2) = CONST 
    0x3b81: v3b81(0x10000000000000000000000000000000000000000) = EXP v3b7f(0x2), v3b7d(0xa0)
    0x3b82: v3b82(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b81(0x10000000000000000000000000000000000000000), v3b7b(0x1)
    0x3b83: v3b83 = AND v3b82(0xffffffffffffffffffffffffffffffffffffffff), v3b7a
    0x3b84: v3b84 = CALLER 
    0x3b85: v3b85 = EQ v3b84, v3b83
    0x3b86: v3b86(0x3b8e) = CONST 
    0x3b89: JUMPI v3b86(0x3b8e), v3b85

    Begin block 0x3b8a
    prev=[0x3b76], succ=[]
    =================================
    0x3b8a: v3b8a(0x0) = CONST 
    0x3b8d: REVERT v3b8a(0x0), v3b8a(0x0)

    Begin block 0x3b8e
    prev=[0x3b76], succ=[0x3b97]
    =================================
    0x3b8f: v3b8f(0x3b97) = CONST 
    0x3b92: v3b92 = ADDRESS 
    0x3b93: v3b93(0x206a) = CONST 
    0x3b96: v3b96_0 = CALLPRIVATE v3b93(0x206a), v3b92, v3b8f(0x3b97)

    Begin block 0x3b97
    prev=[0x3b8e], succ=[0x3b9f, 0x3bee]
    =================================
    0x3b99: v3b99 = GT v972, v3b96_0
    0x3b9a: v3b9a = ISZERO v3b99
    0x3b9b: v3b9b(0x3bee) = CONST 
    0x3b9e: JUMPI v3b9b(0x3bee), v3b9a

    Begin block 0x3b9f
    prev=[0x3b97], succ=[]
    =================================
    0x3b9f: v3b9f(0x40) = CONST 
    0x3ba2: v3ba2 = MLOAD v3b9f(0x40)
    0x3ba3: v3ba3(0xe5) = CONST 
    0x3ba5: v3ba5(0x2) = CONST 
    0x3ba7: v3ba7(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3ba5(0x2), v3ba3(0xe5)
    0x3ba8: v3ba8(0x461bcd) = CONST 
    0x3bac: v3bac(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3ba8(0x461bcd), v3ba7(0x2000000000000000000000000000000000000000000000000000000000)
    0x3bae: MSTORE v3ba2, v3bac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3baf: v3baf(0x20) = CONST 
    0x3bb1: v3bb1(0x4) = CONST 
    0x3bb4: v3bb4 = ADD v3ba2, v3bb1(0x4)
    0x3bb5: MSTORE v3bb4, v3baf(0x20)
    0x3bb6: v3bb6(0x1e) = CONST 
    0x3bb8: v3bb8(0x24) = CONST 
    0x3bbb: v3bbb = ADD v3ba2, v3bb8(0x24)
    0x3bbc: MSTORE v3bbb, v3bb6(0x1e)
    0x3bbd: v3bbd(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000) = CONST 
    0x3bde: v3bde(0x44) = CONST 
    0x3be1: v3be1 = ADD v3ba2, v3bde(0x44)
    0x3be2: MSTORE v3be1, v3bbd(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000)
    0x3be4: v3be4 = MLOAD v3b9f(0x40)
    0x3be8: v3be8(0x0) = SUB v3ba2, v3be4
    0x3be9: v3be9(0x64) = CONST 
    0x3beb: v3beb(0x64) = ADD v3be9(0x64), v3be8(0x0)
    0x3bed: REVERT v3be4, v3beb(0x64)

    Begin block 0x3bee
    prev=[0x3b97], succ=[0x3c40, 0x3c44]
    =================================
    0x3bef: v3bef(0x2) = CONST 
    0x3bf1: v3bf1 = SLOAD v3bef(0x2)
    0x3bf2: v3bf2(0x40) = CONST 
    0x3bf5: v3bf5 = MLOAD v3bf2(0x40)
    0x3bf6: v3bf6(0xe1) = CONST 
    0x3bf8: v3bf8(0x2) = CONST 
    0x3bfa: v3bfa(0x200000000000000000000000000000000000000000000000000000000) = EXP v3bf8(0x2), v3bf6(0xe1)
    0x3bfb: v3bfb(0x67c775bf) = CONST 
    0x3c00: v3c00(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = MUL v3bfb(0x67c775bf), v3bfa(0x200000000000000000000000000000000000000000000000000000000)
    0x3c02: MSTORE v3bf5, v3c00(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x3c03: v3c03 = ADDRESS 
    0x3c04: v3c04(0x4) = CONST 
    0x3c07: v3c07 = ADD v3bf5, v3c04(0x4)
    0x3c08: MSTORE v3c07, v3c03
    0x3c09: v3c09(0x24) = CONST 
    0x3c0c: v3c0c = ADD v3bf5, v3c09(0x24)
    0x3c0f: MSTORE v3c0c, v972
    0x3c11: v3c11 = MLOAD v3bf2(0x40)
    0x3c12: v3c12(0x1) = CONST 
    0x3c14: v3c14(0xa0) = CONST 
    0x3c16: v3c16(0x2) = CONST 
    0x3c18: v3c18(0x10000000000000000000000000000000000000000) = EXP v3c16(0x2), v3c14(0xa0)
    0x3c19: v3c19(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c18(0x10000000000000000000000000000000000000000), v3c12(0x1)
    0x3c1c: v3c1c = AND v3bf1, v3c19(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c1e: v3c1e(0xcf8eeb7e) = CONST 
    0x3c24: v3c24(0x44) = CONST 
    0x3c28: v3c28 = ADD v3bf5, v3c24(0x44)
    0x3c2a: v3c2a(0x0) = CONST 
    0x3c32: v3c32(0x0) = SUB v3bf5, v3c11
    0x3c33: v3c33(0x44) = ADD v3c32(0x0), v3c24(0x44)
    0x3c38: v3c38 = EXTCODESIZE v3c1c
    0x3c39: v3c39 = ISZERO v3c38
    0x3c3b: v3c3b = ISZERO v3c39
    0x3c3c: v3c3c(0x3c44) = CONST 
    0x3c3f: JUMPI v3c3c(0x3c44), v3c3b

    Begin block 0x3c40
    prev=[0x3bee], succ=[]
    =================================
    0x3c40: v3c40(0x0) = CONST 
    0x3c43: REVERT v3c40(0x0), v3c40(0x0)

    Begin block 0x3c44
    prev=[0x3bee], succ=[0x3c4f, 0x3c58]
    =================================
    0x3c46: v3c46 = GAS 
    0x3c47: v3c47 = CALL v3c46, v3c1c, v3c2a(0x0), v3c11, v3c33(0x44), v3c11, v3c2a(0x0)
    0x3c48: v3c48 = ISZERO v3c47
    0x3c4a: v3c4a = ISZERO v3c48
    0x3c4b: v3c4b(0x3c58) = CONST 
    0x3c4e: JUMPI v3c4b(0x3c58), v3c4a

    Begin block 0x3c4f
    prev=[0x3c44], succ=[]
    =================================
    0x3c4f: v3c4f = RETURNDATASIZE 
    0x3c50: v3c50(0x0) = CONST 
    0x3c53: RETURNDATACOPY v3c50(0x0), v3c50(0x0), v3c4f
    0x3c54: v3c54 = RETURNDATASIZE 
    0x3c55: v3c55(0x0) = CONST 
    0x3c57: REVERT v3c55(0x0), v3c54

    Begin block 0x3c58
    prev=[0x3c44], succ=[0x3cc4, 0x3cc8]
    =================================
    0x3c5b: v3c5b(0x2) = CONST 
    0x3c5d: v3c5d = SLOAD v3c5b(0x2)
    0x3c5e: v3c5e(0x40) = CONST 
    0x3c61: v3c61 = MLOAD v3c5e(0x40)
    0x3c62: v3c62(0x21e5383a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x3c84: MSTORE v3c61, v3c62(0x21e5383a00000000000000000000000000000000000000000000000000000000)
    0x3c85: v3c85 = CALLER 
    0x3c86: v3c86(0x4) = CONST 
    0x3c89: v3c89 = ADD v3c61, v3c86(0x4)
    0x3c8a: MSTORE v3c89, v3c85
    0x3c8b: v3c8b(0x24) = CONST 
    0x3c8e: v3c8e = ADD v3c61, v3c8b(0x24)
    0x3c91: MSTORE v3c8e, v972
    0x3c93: v3c93 = MLOAD v3c5e(0x40)
    0x3c94: v3c94(0x1) = CONST 
    0x3c96: v3c96(0xa0) = CONST 
    0x3c98: v3c98(0x2) = CONST 
    0x3c9a: v3c9a(0x10000000000000000000000000000000000000000) = EXP v3c98(0x2), v3c96(0xa0)
    0x3c9b: v3c9b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c9a(0x10000000000000000000000000000000000000000), v3c94(0x1)
    0x3c9e: v3c9e = AND v3c5d, v3c9b(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ca1: v3ca1(0x21e5383a) = CONST 
    0x3ca8: v3ca8(0x44) = CONST 
    0x3cac: v3cac = ADD v3c61, v3ca8(0x44)
    0x3cae: v3cae(0x0) = CONST 
    0x3cb6: v3cb6(0x0) = SUB v3c61, v3c93
    0x3cb7: v3cb7(0x44) = ADD v3cb6(0x0), v3ca8(0x44)
    0x3cbc: v3cbc = EXTCODESIZE v3c9e
    0x3cbd: v3cbd = ISZERO v3cbc
    0x3cbf: v3cbf = ISZERO v3cbd
    0x3cc0: v3cc0(0x3cc8) = CONST 
    0x3cc3: JUMPI v3cc0(0x3cc8), v3cbf

    Begin block 0x3cc4
    prev=[0x3c58], succ=[]
    =================================
    0x3cc4: v3cc4(0x0) = CONST 
    0x3cc7: REVERT v3cc4(0x0), v3cc4(0x0)

    Begin block 0x3cc8
    prev=[0x3c58], succ=[0x3cd3, 0x3cdc]
    =================================
    0x3cca: v3cca = GAS 
    0x3ccb: v3ccb = CALL v3cca, v3c9e, v3cae(0x0), v3c93, v3cb7(0x44), v3c93, v3cae(0x0)
    0x3ccc: v3ccc = ISZERO v3ccb
    0x3cce: v3cce = ISZERO v3ccc
    0x3ccf: v3ccf(0x3cdc) = CONST 
    0x3cd2: JUMPI v3ccf(0x3cdc), v3cce

    Begin block 0x3cd3
    prev=[0x3cc8], succ=[]
    =================================
    0x3cd3: v3cd3 = RETURNDATASIZE 
    0x3cd4: v3cd4(0x0) = CONST 
    0x3cd7: RETURNDATACOPY v3cd4(0x0), v3cd4(0x0), v3cd3
    0x3cd8: v3cd8 = RETURNDATASIZE 
    0x3cd9: v3cd9(0x0) = CONST 
    0x3cdb: REVERT v3cd9(0x0), v3cd8

    Begin block 0x3cdc
    prev=[0x3cc8], succ=[0x5297]
    =================================
    0x3cdf: v3cdf(0x40) = CONST 
    0x3ce2: v3ce2 = MLOAD v3cdf(0x40)
    0x3ce5: MSTORE v3ce2, v972
    0x3ce7: v3ce7 = MLOAD v3cdf(0x40)
    0x3ce8: v3ce8 = CALLER 
    0x3ceb: v3ceb = ADDRESS 
    0x3cee: v3cee(0x0) = CONST 
    0x3cf1: v3cf1 = MLOAD v3cee(0x0)
    0x3cf2: v3cf2(0x20) = CONST 
    0x3cf4: v3cf4(0x4a90) = CONST 
    0x3cfc: MSTORE v3cee(0x0), v3cf1
    0x3d00: v3d00(0x0) = SUB v3ce2, v3ce7
    0x3d01: v3d01(0x20) = CONST 
    0x3d03: v3d03(0x20) = ADD v3d01(0x20), v3d00(0x0)
    0x3d05: LOG3 v3ce7, v3d03(0x20), v557f(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v3ceb, v3ce8
    0x3d07: v3d07(0x1) = CONST 
    0x3d0c: JUMP v96d(0x5297)
    0x557f: v557f(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 

    Begin block 0x5297
    prev=[0x3cdc], succ=[]
    =================================
    0x5298: v5298(0x40) = CONST 
    0x529b: v529b = MLOAD v5298(0x40)
    0x529d: v529d = ISZERO v3d07(0x1)
    0x529e: v529e = ISZERO v529d
    0x52a0: MSTORE v529b, v529e
    0x52a1: v52a1 = MLOAD v5298(0x40)
    0x52a5: v52a5(0x0) = SUB v529b, v52a1
    0x52a6: v52a6(0x20) = CONST 
    0x52a8: v52a8(0x20) = ADD v52a6(0x20), v52a5(0x0)
    0x52aa: RETURN v52a1, v52a8(0x20)

}

function lock()() public {
    Begin block 0x977
    prev=[], succ=[0x97f, 0x983]
    =================================
    0x978: v978 = CALLVALUE 
    0x97a: v97a = ISZERO v978
    0x97b: v97b(0x983) = CONST 
    0x97e: JUMPI v97b(0x983), v97a

    Begin block 0x97f
    prev=[0x977], succ=[]
    =================================
    0x97f: v97f(0x0) = CONST 
    0x982: REVERT v97f(0x0), v97f(0x0)

    Begin block 0x983
    prev=[0x977], succ=[0x3d0d]
    =================================
    0x985: v985(0x52ca) = CONST 
    0x988: v988(0x3d0d) = CONST 
    0x98b: JUMP v988(0x3d0d)

    Begin block 0x3d0d
    prev=[0x983], succ=[0x3d20, 0x3d24]
    =================================
    0x3d0e: v3d0e(0x0) = CONST 
    0x3d10: v3d10 = SLOAD v3d0e(0x0)
    0x3d11: v3d11(0x1) = CONST 
    0x3d13: v3d13(0xa0) = CONST 
    0x3d15: v3d15(0x2) = CONST 
    0x3d17: v3d17(0x10000000000000000000000000000000000000000) = EXP v3d15(0x2), v3d13(0xa0)
    0x3d18: v3d18(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d17(0x10000000000000000000000000000000000000000), v3d11(0x1)
    0x3d19: v3d19 = AND v3d18(0xffffffffffffffffffffffffffffffffffffffff), v3d10
    0x3d1a: v3d1a = CALLER 
    0x3d1b: v3d1b = EQ v3d1a, v3d19
    0x3d1c: v3d1c(0x3d24) = CONST 
    0x3d1f: JUMPI v3d1c(0x3d24), v3d1b

    Begin block 0x3d20
    prev=[0x3d0d], succ=[]
    =================================
    0x3d20: v3d20(0x0) = CONST 
    0x3d23: REVERT v3d20(0x0), v3d20(0x0)

    Begin block 0x3d24
    prev=[0x3d0d], succ=[0x52ca]
    =================================
    0x3d25: v3d25(0x1) = CONST 
    0x3d28: v3d28 = SLOAD v3d25(0x1)
    0x3d29: v3d29(0xff000000000000000000000000000000000000000000) = CONST 
    0x3d40: v3d40(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v3d29(0xff000000000000000000000000000000000000000000)
    0x3d41: v3d41 = AND v3d40(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v3d28
    0x3d43: SSTORE v3d25(0x1), v3d41
    0x3d44: v3d44(0x40) = CONST 
    0x3d46: v3d46 = MLOAD v3d44(0x40)
    0x3d47: v3d47(0xf2e5b6c72c6a4491efd919a9f9a409f324ef0708c11ee57d410c2cb06c0992b) = CONST 
    0x3d69: v3d69(0x0) = CONST 
    0x3d6c: LOG1 v3d46, v3d69(0x0), v3d47(0xf2e5b6c72c6a4491efd919a9f9a409f324ef0708c11ee57d410c2cb06c0992b)
    0x3d6d: JUMP v985(0x52ca)

    Begin block 0x52ca
    prev=[0x3d24], succ=[]
    =================================
    0x52cb: STOP 

}

