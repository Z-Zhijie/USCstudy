function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x4f0]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x4e4: v4e4(0x4f0) = CONST 
    0x4e5: JUMPI v4e4(0x4f0), v8

    Begin block 0xd
    prev=[0x0], succ=[0x4f3, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5c60da1b) = CONST 
    0x19: v19 = EQ v14(0x5c60da1b), v12
    0x4e6: v4e6(0x4f3) = CONST 
    0x4e7: JUMPI v4e6(0x4f3), v19

    Begin block 0x4f3
    prev=[0xd], succ=[]
    =================================
    0x4f4: v4f4(0xc6) = CONST 
    0x4f5: CALLPRIVATE v4f4(0xc6)

    Begin block 0x1e
    prev=[0xd], succ=[0x4f6, 0x29]
    =================================
    0x1f: v1f(0x8da5cb5b) = CONST 
    0x24: v24 = EQ v1f(0x8da5cb5b), v12
    0x4e8: v4e8(0x4f6) = CONST 
    0x4e9: JUMPI v4e8(0x4f6), v24

    Begin block 0x4f6
    prev=[0x1e], succ=[]
    =================================
    0x4f7: v4f7(0xf7) = CONST 
    0x4f8: CALLPRIVATE v4f7(0xf7)

    Begin block 0x29
    prev=[0x1e], succ=[0x4f9, 0x34]
    =================================
    0x2a: v2a(0x8f32d59b) = CONST 
    0x2f: v2f = EQ v2a(0x8f32d59b), v12
    0x4ea: v4ea(0x4f9) = CONST 
    0x4eb: JUMPI v4ea(0x4f9), v2f

    Begin block 0x4f9
    prev=[0x29], succ=[]
    =================================
    0x4fa: v4fa(0x10c) = CONST 
    0x4fb: CALLPRIVATE v4fa(0x10c)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x4fc]
    =================================
    0x35: v35(0xd69efdc5) = CONST 
    0x3a: v3a = EQ v35(0xd69efdc5), v12
    0x4ec: v4ec(0x4fc) = CONST 
    0x4ed: JUMPI v4ec(0x4fc), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4f0, 0x4ff]
    =================================
    0x40: v40(0xf2fde38b) = CONST 
    0x45: v45 = EQ v40(0xf2fde38b), v12
    0x4ee: v4ee(0x4ff) = CONST 
    0x4ef: JUMPI v4ee(0x4ff), v45

    Begin block 0x4f0
    prev=[0x0, 0x3f], succ=[]
    =================================
    0x4f1: v4f1(0x4a) = CONST 
    0x4f2: CALLPRIVATE v4f1(0x4a)

    Begin block 0x4ff
    prev=[0x3f], succ=[]
    =================================
    0x500: v500(0x168) = CONST 
    0x501: CALLPRIVATE v500(0x168)

    Begin block 0x4fc
    prev=[0x34], succ=[]
    =================================
    0x4fd: v4fd(0x135) = CONST 
    0x4fe: CALLPRIVATE v4fd(0x135)

}

function isOwner()() public {
    Begin block 0x10c
    prev=[], succ=[0x114, 0x118]
    =================================
    0x10d: v10d = CALLVALUE 
    0x10f: v10f = ISZERO v10d
    0x110: v110(0x118) = CONST 
    0x113: JUMPI v110(0x118), v10f

    Begin block 0x114
    prev=[0x10c], succ=[]
    =================================
    0x114: v114(0x0) = CONST 
    0x117: REVERT v114(0x0), v114(0x0)

    Begin block 0x118
    prev=[0x10c], succ=[0x1b9B0x118]
    =================================
    0x11a: v11a(0x121) = CONST 
    0x11d: v11d(0x1b9) = CONST 
    0x120: JUMP v11d(0x1b9)

    Begin block 0x1b9B0x118
    prev=[0x118], succ=[0x2e6B0x118]
    =================================
    0x1baS0x118: v1baV118(0x0) = CONST 
    0x1bdS0x118: v1bdV118 = SLOAD v1baV118(0x0)
    0x1beS0x118: v1beV118(0x1) = CONST 
    0x1c0S0x118: v1c0V118(0x1) = CONST 
    0x1c2S0x118: v1c2V118(0xa0) = CONST 
    0x1c4S0x118: v1c4V118(0x10000000000000000000000000000000000000000) = SHL v1c2V118(0xa0), v1c0V118(0x1)
    0x1c5S0x118: v1c5V118(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c4V118(0x10000000000000000000000000000000000000000), v1beV118(0x1)
    0x1c6S0x118: v1c6V118 = AND v1c5V118(0xffffffffffffffffffffffffffffffffffffffff), v1bdV118
    0x1c7S0x118: v1c7V118(0x1ce) = CONST 
    0x1caS0x118: v1caV118(0x2e6) = CONST 
    0x1cdS0x118: JUMP v1caV118(0x2e6)

    Begin block 0x2e6B0x118
    prev=[0x1b9B0x118], succ=[0x1ceB0x118]
    =================================
    0x2e7S0x118: v2e7V118 = CALLER 
    0x2e9S0x118: JUMP v1c7V118(0x1ce)

    Begin block 0x1ceB0x118
    prev=[0x2e6B0x118], succ=[0x121]
    =================================
    0x1cfS0x118: v1cfV118(0x1) = CONST 
    0x1d1S0x118: v1d1V118(0x1) = CONST 
    0x1d3S0x118: v1d3V118(0xa0) = CONST 
    0x1d5S0x118: v1d5V118(0x10000000000000000000000000000000000000000) = SHL v1d3V118(0xa0), v1d1V118(0x1)
    0x1d6S0x118: v1d6V118(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d5V118(0x10000000000000000000000000000000000000000), v1cfV118(0x1)
    0x1d7S0x118: v1d7V118 = AND v1d6V118(0xffffffffffffffffffffffffffffffffffffffff), v2e7V118
    0x1d8S0x118: v1d8V118 = EQ v1d7V118, v1c6V118
    0x1dcS0x118: JUMP v11a(0x121)

    Begin block 0x121
    prev=[0x1ceB0x118], succ=[]
    =================================
    0x122: v122(0x40) = CONST 
    0x125: v125 = MLOAD v122(0x40)
    0x127: v127 = ISZERO v1d8V118
    0x128: v128 = ISZERO v127
    0x12a: MSTORE v125, v128
    0x12b: v12b = MLOAD v122(0x40)
    0x12f: v12f(0x0) = SUB v125, v12b
    0x130: v130(0x20) = CONST 
    0x132: v132(0x20) = ADD v130(0x20), v12f(0x0)
    0x134: RETURN v12b, v132(0x20)

}

function replaceImplementation(address)() public {
    Begin block 0x135
    prev=[], succ=[0x13d, 0x141]
    =================================
    0x136: v136 = CALLVALUE 
    0x138: v138 = ISZERO v136
    0x139: v139(0x141) = CONST 
    0x13c: JUMPI v139(0x141), v138

    Begin block 0x13d
    prev=[0x135], succ=[]
    =================================
    0x13d: v13d(0x0) = CONST 
    0x140: REVERT v13d(0x0), v13d(0x0)

    Begin block 0x141
    prev=[0x135], succ=[0x154, 0x158]
    =================================
    0x143: v143(0x4c1) = CONST 
    0x146: v146(0x4) = CONST 
    0x149: v149 = CALLDATASIZE 
    0x14a: v14a = SUB v149, v146(0x4)
    0x14b: v14b(0x20) = CONST 
    0x14e: v14e = LT v14a, v14b(0x20)
    0x14f: v14f = ISZERO v14e
    0x150: v150(0x158) = CONST 
    0x153: JUMPI v150(0x158), v14f

    Begin block 0x154
    prev=[0x141], succ=[]
    =================================
    0x154: v154(0x0) = CONST 
    0x157: REVERT v154(0x0), v154(0x0)

    Begin block 0x158
    prev=[0x141], succ=[0x1dd]
    =================================
    0x15a: v15a = CALLDATALOAD v146(0x4)
    0x15b: v15b(0x1) = CONST 
    0x15d: v15d(0x1) = CONST 
    0x15f: v15f(0xa0) = CONST 
    0x161: v161(0x10000000000000000000000000000000000000000) = SHL v15f(0xa0), v15d(0x1)
    0x162: v162(0xffffffffffffffffffffffffffffffffffffffff) = SUB v161(0x10000000000000000000000000000000000000000), v15b(0x1)
    0x163: v163 = AND v162(0xffffffffffffffffffffffffffffffffffffffff), v15a
    0x164: v164(0x1dd) = CONST 
    0x167: JUMP v164(0x1dd)

    Begin block 0x1dd
    prev=[0x158], succ=[0x1b9B0x1dd]
    =================================
    0x1de: v1de(0x1e5) = CONST 
    0x1e1: v1e1(0x1b9) = CONST 
    0x1e4: JUMP v1e1(0x1b9)

    Begin block 0x1b9B0x1dd
    prev=[0x1dd], succ=[0x2e6B0x1dd]
    =================================
    0x1baS0x1dd: v1baV1dd(0x0) = CONST 
    0x1bdS0x1dd: v1bdV1dd = SLOAD v1baV1dd(0x0)
    0x1beS0x1dd: v1beV1dd(0x1) = CONST 
    0x1c0S0x1dd: v1c0V1dd(0x1) = CONST 
    0x1c2S0x1dd: v1c2V1dd(0xa0) = CONST 
    0x1c4S0x1dd: v1c4V1dd(0x10000000000000000000000000000000000000000) = SHL v1c2V1dd(0xa0), v1c0V1dd(0x1)
    0x1c5S0x1dd: v1c5V1dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c4V1dd(0x10000000000000000000000000000000000000000), v1beV1dd(0x1)
    0x1c6S0x1dd: v1c6V1dd = AND v1c5V1dd(0xffffffffffffffffffffffffffffffffffffffff), v1bdV1dd
    0x1c7S0x1dd: v1c7V1dd(0x1ce) = CONST 
    0x1caS0x1dd: v1caV1dd(0x2e6) = CONST 
    0x1cdS0x1dd: JUMP v1caV1dd(0x2e6)

    Begin block 0x2e6B0x1dd
    prev=[0x1b9B0x1dd], succ=[0x1ceB0x1dd]
    =================================
    0x2e7S0x1dd: v2e7V1dd = CALLER 
    0x2e9S0x1dd: JUMP v1c7V1dd(0x1ce)

    Begin block 0x1ceB0x1dd
    prev=[0x2e6B0x1dd], succ=[0x1e5]
    =================================
    0x1cfS0x1dd: v1cfV1dd(0x1) = CONST 
    0x1d1S0x1dd: v1d1V1dd(0x1) = CONST 
    0x1d3S0x1dd: v1d3V1dd(0xa0) = CONST 
    0x1d5S0x1dd: v1d5V1dd(0x10000000000000000000000000000000000000000) = SHL v1d3V1dd(0xa0), v1d1V1dd(0x1)
    0x1d6S0x1dd: v1d6V1dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d5V1dd(0x10000000000000000000000000000000000000000), v1cfV1dd(0x1)
    0x1d7S0x1dd: v1d7V1dd = AND v1d6V1dd(0xffffffffffffffffffffffffffffffffffffffff), v2e7V1dd
    0x1d8S0x1dd: v1d8V1dd = EQ v1d7V1dd, v1c6V1dd
    0x1dcS0x1dd: JUMP v1de(0x1e5)

    Begin block 0x1e5
    prev=[0x1ceB0x1dd], succ=[0x1ea, 0x225]
    =================================
    0x1e6: v1e6(0x225) = CONST 
    0x1e9: JUMPI v1e6(0x225), v1d8V1dd

    Begin block 0x1ea
    prev=[0x1e5], succ=[]
    =================================
    0x1ea: v1ea(0x40) = CONST 
    0x1ed: v1ed = MLOAD v1ea(0x40)
    0x1ee: v1ee(0x461bcd) = CONST 
    0x1f2: v1f2(0xe5) = CONST 
    0x1f4: v1f4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f2(0xe5), v1ee(0x461bcd)
    0x1f6: MSTORE v1ed, v1f4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f7: v1f7(0x20) = CONST 
    0x1f9: v1f9(0x4) = CONST 
    0x1fc: v1fc = ADD v1ed, v1f9(0x4)
    0x1fd: MSTORE v1fc, v1f7(0x20)
    0x1fe: v1fe(0xc) = CONST 
    0x200: v200(0x24) = CONST 
    0x203: v203 = ADD v1ed, v200(0x24)
    0x204: MSTORE v203, v1fe(0xc)
    0x205: v205(0x1d5b985d5d1a1bdc9a5e9959) = CONST 
    0x212: v212(0xa2) = CONST 
    0x214: v214(0x756e617574686f72697a65640000000000000000000000000000000000000000) = SHL v212(0xa2), v205(0x1d5b985d5d1a1bdc9a5e9959)
    0x215: v215(0x44) = CONST 
    0x218: v218 = ADD v1ed, v215(0x44)
    0x219: MSTORE v218, v214(0x756e617574686f72697a65640000000000000000000000000000000000000000)
    0x21b: v21b = MLOAD v1ea(0x40)
    0x21f: v21f(0x0) = SUB v1ed, v21b
    0x220: v220(0x64) = CONST 
    0x222: v222(0x64) = ADD v220(0x64), v21f(0x0)
    0x224: REVERT v21b, v222(0x64)

    Begin block 0x225
    prev=[0x1e5], succ=[0x2eaB0x225]
    =================================
    0x226: v226(0x22e) = CONST 
    0x22a: v22a(0x2ea) = CONST 
    0x22d: JUMP v22a(0x2ea)

    Begin block 0x2eaB0x225
    prev=[0x225], succ=[0x31eB0x225, 0x31aB0x225]
    =================================
    0x2ebS0x225: v2ebV225(0x0) = CONST 
    0x2eeS0x225: v2eeV225 = EXTCODEHASH v163
    0x2efS0x225: v2efV225(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x312S0x225: v312V225 = EQ v2efV225(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470), v2eeV225
    0x314S0x225: v314V225 = ISZERO v312V225
    0x316S0x225: v316V225(0x31e) = CONST 
    0x319S0x225: JUMPI v316V225(0x31e), v312V225

    Begin block 0x31eB0x225
    prev=[0x2eaB0x225, 0x31aB0x225], succ=[0x22e]
    =================================
    0x31e_0x0S0x225: v31e_0V225 = PHI v314V225, v31dV225
    0x325S0x225: JUMP v226(0x22e)

    Begin block 0x22e
    prev=[0x31eB0x225], succ=[0x233, 0x270]
    =================================
    0x22f: v22f(0x270) = CONST 
    0x232: JUMPI v22f(0x270), v31e_0V225

    Begin block 0x233
    prev=[0x22e], succ=[]
    =================================
    0x233: v233(0x40) = CONST 
    0x236: v236 = MLOAD v233(0x40)
    0x237: v237(0x461bcd) = CONST 
    0x23b: v23b(0xe5) = CONST 
    0x23d: v23d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v23b(0xe5), v237(0x461bcd)
    0x23f: MSTORE v236, v23d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x240: v240(0x20) = CONST 
    0x242: v242(0x4) = CONST 
    0x245: v245 = ADD v236, v242(0x4)
    0x246: MSTORE v245, v240(0x20)
    0x247: v247(0xe) = CONST 
    0x249: v249(0x24) = CONST 
    0x24c: v24c = ADD v236, v249(0x24)
    0x24d: MSTORE v24c, v247(0xe)
    0x24e: v24e(0x1b9bdd08184818dbdb9d1c9858dd) = CONST 
    0x25d: v25d(0x92) = CONST 
    0x25f: v25f(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000) = SHL v25d(0x92), v24e(0x1b9bdd08184818dbdb9d1c9858dd)
    0x260: v260(0x44) = CONST 
    0x263: v263 = ADD v236, v260(0x44)
    0x264: MSTORE v263, v25f(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000)
    0x266: v266 = MLOAD v233(0x40)
    0x26a: v26a(0x0) = SUB v236, v266
    0x26b: v26b(0x64) = CONST 
    0x26d: v26d(0x64) = ADD v26b(0x64), v26a(0x0)
    0x26f: REVERT v266, v26d(0x64)

    Begin block 0x270
    prev=[0x22e], succ=[0x4c1]
    =================================
    0x271: v271(0x1) = CONST 
    0x274: v274 = SLOAD v271(0x1)
    0x275: v275(0x1) = CONST 
    0x277: v277(0x1) = CONST 
    0x279: v279(0xa0) = CONST 
    0x27b: v27b(0x10000000000000000000000000000000000000000) = SHL v279(0xa0), v277(0x1)
    0x27c: v27c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27b(0x10000000000000000000000000000000000000000), v275(0x1)
    0x27d: v27d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27c(0xffffffffffffffffffffffffffffffffffffffff)
    0x27e: v27e = AND v27d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v274
    0x27f: v27f(0x1) = CONST 
    0x281: v281(0x1) = CONST 
    0x283: v283(0xa0) = CONST 
    0x285: v285(0x10000000000000000000000000000000000000000) = SHL v283(0xa0), v281(0x1)
    0x286: v286(0xffffffffffffffffffffffffffffffffffffffff) = SUB v285(0x10000000000000000000000000000000000000000), v27f(0x1)
    0x28a: v28a = AND v286(0xffffffffffffffffffffffffffffffffffffffff), v163
    0x28e: v28e = OR v28a, v27e
    0x290: SSTORE v271(0x1), v28e
    0x291: JUMP v143(0x4c1)

    Begin block 0x4c1
    prev=[0x270], succ=[]
    =================================
    0x4c2: STOP 

    Begin block 0x31aB0x225
    prev=[0x2eaB0x225], succ=[0x31eB0x225]
    =================================
    0x31cS0x225: v31cV225 = ISZERO v2eeV225
    0x31dS0x225: v31dV225 = ISZERO v31cV225

}

function transferOwnership(address)() public {
    Begin block 0x168
    prev=[], succ=[0x170, 0x174]
    =================================
    0x169: v169 = CALLVALUE 
    0x16b: v16b = ISZERO v169
    0x16c: v16c(0x174) = CONST 
    0x16f: JUMPI v16c(0x174), v16b

    Begin block 0x170
    prev=[0x168], succ=[]
    =================================
    0x170: v170(0x0) = CONST 
    0x173: REVERT v170(0x0), v170(0x0)

    Begin block 0x174
    prev=[0x168], succ=[0x187, 0x18b]
    =================================
    0x176: v176(0x4e2) = CONST 
    0x179: v179(0x4) = CONST 
    0x17c: v17c = CALLDATASIZE 
    0x17d: v17d = SUB v17c, v179(0x4)
    0x17e: v17e(0x20) = CONST 
    0x181: v181 = LT v17d, v17e(0x20)
    0x182: v182 = ISZERO v181
    0x183: v183(0x18b) = CONST 
    0x186: JUMPI v183(0x18b), v182

    Begin block 0x187
    prev=[0x174], succ=[]
    =================================
    0x187: v187(0x0) = CONST 
    0x18a: REVERT v187(0x0), v187(0x0)

    Begin block 0x18b
    prev=[0x174], succ=[0x292]
    =================================
    0x18d: v18d = CALLDATALOAD v179(0x4)
    0x18e: v18e(0x1) = CONST 
    0x190: v190(0x1) = CONST 
    0x192: v192(0xa0) = CONST 
    0x194: v194(0x10000000000000000000000000000000000000000) = SHL v192(0xa0), v190(0x1)
    0x195: v195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v194(0x10000000000000000000000000000000000000000), v18e(0x1)
    0x196: v196 = AND v195(0xffffffffffffffffffffffffffffffffffffffff), v18d
    0x197: v197(0x292) = CONST 
    0x19a: JUMP v197(0x292)

    Begin block 0x292
    prev=[0x18b], succ=[0x1b9B0x292]
    =================================
    0x293: v293(0x29a) = CONST 
    0x296: v296(0x1b9) = CONST 
    0x299: JUMP v296(0x1b9)

    Begin block 0x1b9B0x292
    prev=[0x292], succ=[0x2e6B0x292]
    =================================
    0x1baS0x292: v1baV292(0x0) = CONST 
    0x1bdS0x292: v1bdV292 = SLOAD v1baV292(0x0)
    0x1beS0x292: v1beV292(0x1) = CONST 
    0x1c0S0x292: v1c0V292(0x1) = CONST 
    0x1c2S0x292: v1c2V292(0xa0) = CONST 
    0x1c4S0x292: v1c4V292(0x10000000000000000000000000000000000000000) = SHL v1c2V292(0xa0), v1c0V292(0x1)
    0x1c5S0x292: v1c5V292(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c4V292(0x10000000000000000000000000000000000000000), v1beV292(0x1)
    0x1c6S0x292: v1c6V292 = AND v1c5V292(0xffffffffffffffffffffffffffffffffffffffff), v1bdV292
    0x1c7S0x292: v1c7V292(0x1ce) = CONST 
    0x1caS0x292: v1caV292(0x2e6) = CONST 
    0x1cdS0x292: JUMP v1caV292(0x2e6)

    Begin block 0x2e6B0x292
    prev=[0x1b9B0x292], succ=[0x1ceB0x292]
    =================================
    0x2e7S0x292: v2e7V292 = CALLER 
    0x2e9S0x292: JUMP v1c7V292(0x1ce)

    Begin block 0x1ceB0x292
    prev=[0x2e6B0x292], succ=[0x29a]
    =================================
    0x1cfS0x292: v1cfV292(0x1) = CONST 
    0x1d1S0x292: v1d1V292(0x1) = CONST 
    0x1d3S0x292: v1d3V292(0xa0) = CONST 
    0x1d5S0x292: v1d5V292(0x10000000000000000000000000000000000000000) = SHL v1d3V292(0xa0), v1d1V292(0x1)
    0x1d6S0x292: v1d6V292(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d5V292(0x10000000000000000000000000000000000000000), v1cfV292(0x1)
    0x1d7S0x292: v1d7V292 = AND v1d6V292(0xffffffffffffffffffffffffffffffffffffffff), v2e7V292
    0x1d8S0x292: v1d8V292 = EQ v1d7V292, v1c6V292
    0x1dcS0x292: JUMP v293(0x29a)

    Begin block 0x29a
    prev=[0x1ceB0x292], succ=[0x29f, 0x2da]
    =================================
    0x29b: v29b(0x2da) = CONST 
    0x29e: JUMPI v29b(0x2da), v1d8V292

    Begin block 0x29f
    prev=[0x29a], succ=[]
    =================================
    0x29f: v29f(0x40) = CONST 
    0x2a2: v2a2 = MLOAD v29f(0x40)
    0x2a3: v2a3(0x461bcd) = CONST 
    0x2a7: v2a7(0xe5) = CONST 
    0x2a9: v2a9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2a7(0xe5), v2a3(0x461bcd)
    0x2ab: MSTORE v2a2, v2a9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ac: v2ac(0x20) = CONST 
    0x2ae: v2ae(0x4) = CONST 
    0x2b1: v2b1 = ADD v2a2, v2ae(0x4)
    0x2b2: MSTORE v2b1, v2ac(0x20)
    0x2b3: v2b3(0xc) = CONST 
    0x2b5: v2b5(0x24) = CONST 
    0x2b8: v2b8 = ADD v2a2, v2b5(0x24)
    0x2b9: MSTORE v2b8, v2b3(0xc)
    0x2ba: v2ba(0x1d5b985d5d1a1bdc9a5e9959) = CONST 
    0x2c7: v2c7(0xa2) = CONST 
    0x2c9: v2c9(0x756e617574686f72697a65640000000000000000000000000000000000000000) = SHL v2c7(0xa2), v2ba(0x1d5b985d5d1a1bdc9a5e9959)
    0x2ca: v2ca(0x44) = CONST 
    0x2cd: v2cd = ADD v2a2, v2ca(0x44)
    0x2ce: MSTORE v2cd, v2c9(0x756e617574686f72697a65640000000000000000000000000000000000000000)
    0x2d0: v2d0 = MLOAD v29f(0x40)
    0x2d4: v2d4(0x0) = SUB v2a2, v2d0
    0x2d5: v2d5(0x64) = CONST 
    0x2d7: v2d7(0x64) = ADD v2d5(0x64), v2d4(0x0)
    0x2d9: REVERT v2d0, v2d7(0x64)

    Begin block 0x2da
    prev=[0x29a], succ=[0x326]
    =================================
    0x2db: v2db(0x2e3) = CONST 
    0x2df: v2df(0x326) = CONST 
    0x2e2: JUMP v2df(0x326)

    Begin block 0x326
    prev=[0x2da], succ=[0x335, 0x36b]
    =================================
    0x327: v327(0x1) = CONST 
    0x329: v329(0x1) = CONST 
    0x32b: v32b(0xa0) = CONST 
    0x32d: v32d(0x10000000000000000000000000000000000000000) = SHL v32b(0xa0), v329(0x1)
    0x32e: v32e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32d(0x10000000000000000000000000000000000000000), v327(0x1)
    0x330: v330 = AND v196, v32e(0xffffffffffffffffffffffffffffffffffffffff)
    0x331: v331(0x36b) = CONST 
    0x334: JUMPI v331(0x36b), v330

    Begin block 0x335
    prev=[0x326], succ=[]
    =================================
    0x335: v335(0x40) = CONST 
    0x337: v337 = MLOAD v335(0x40)
    0x338: v338(0x461bcd) = CONST 
    0x33c: v33c(0xe5) = CONST 
    0x33e: v33e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v33c(0xe5), v338(0x461bcd)
    0x340: MSTORE v337, v33e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x341: v341(0x4) = CONST 
    0x343: v343 = ADD v341(0x4), v337
    0x346: v346(0x20) = CONST 
    0x348: v348 = ADD v346(0x20), v343
    0x34b: v34b(0x20) = SUB v348, v343
    0x34d: MSTORE v343, v34b(0x20)
    0x34e: v34e(0x26) = CONST 
    0x351: MSTORE v348, v34e(0x26)
    0x352: v352(0x20) = CONST 
    0x354: v354 = ADD v352(0x20), v348
    0x356: v356(0x3c7) = CONST 
    0x359: v359(0x26) = CONST 
    0x35c: CODECOPY v354, v356(0x3c7), v359(0x26)
    0x35d: v35d(0x40) = CONST 
    0x35f: v35f = ADD v35d(0x40), v354
    0x363: v363(0x40) = CONST 
    0x365: v365 = MLOAD v363(0x40)
    0x368: v368(0x84) = SUB v35f, v365
    0x36a: REVERT v365, v368(0x84)

    Begin block 0x36b
    prev=[0x326], succ=[0x2e3]
    =================================
    0x36c: v36c(0x0) = CONST 
    0x36f: v36f = SLOAD v36c(0x0)
    0x370: v370(0x40) = CONST 
    0x372: v372 = MLOAD v370(0x40)
    0x373: v373(0x1) = CONST 
    0x375: v375(0x1) = CONST 
    0x377: v377(0xa0) = CONST 
    0x379: v379(0x10000000000000000000000000000000000000000) = SHL v377(0xa0), v375(0x1)
    0x37a: v37a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v379(0x10000000000000000000000000000000000000000), v373(0x1)
    0x37d: v37d = AND v196, v37a(0xffffffffffffffffffffffffffffffffffffffff)
    0x380: v380 = AND v36f, v37a(0xffffffffffffffffffffffffffffffffffffffff)
    0x382: v382(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x3a4: LOG3 v372, v36c(0x0), v382(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v380, v37d
    0x3a5: v3a5(0x0) = CONST 
    0x3a8: v3a8 = SLOAD v3a5(0x0)
    0x3a9: v3a9(0x1) = CONST 
    0x3ab: v3ab(0x1) = CONST 
    0x3ad: v3ad(0xa0) = CONST 
    0x3af: v3af(0x10000000000000000000000000000000000000000) = SHL v3ad(0xa0), v3ab(0x1)
    0x3b0: v3b0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3af(0x10000000000000000000000000000000000000000), v3a9(0x1)
    0x3b1: v3b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3b0(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b2: v3b2 = AND v3b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3a8
    0x3b3: v3b3(0x1) = CONST 
    0x3b5: v3b5(0x1) = CONST 
    0x3b7: v3b7(0xa0) = CONST 
    0x3b9: v3b9(0x10000000000000000000000000000000000000000) = SHL v3b7(0xa0), v3b5(0x1)
    0x3ba: v3ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b9(0x10000000000000000000000000000000000000000), v3b3(0x1)
    0x3be: v3be = AND v3ba(0xffffffffffffffffffffffffffffffffffffffff), v196
    0x3c2: v3c2 = OR v3be, v3b2
    0x3c4: SSTORE v3a5(0x0), v3c2
    0x3c5: JUMP v2db(0x2e3)

    Begin block 0x2e3
    prev=[0x36b], succ=[0x4e2]
    =================================
    0x2e5: JUMP v176(0x4e2)

    Begin block 0x4e2
    prev=[0x2e3], succ=[]
    =================================
    0x4e3: STOP 

}

function fallback()() public {
    Begin block 0x4a
    prev=[], succ=[0x54, 0x58]
    =================================
    0x4b: v4b(0x8fc) = CONST 
    0x4e: v4e = GAS 
    0x4f: v4f = GT v4e, v4b(0x8fc)
    0x50: v50(0x58) = CONST 
    0x53: JUMPI v50(0x58), v4f

    Begin block 0x54
    prev=[0x4a], succ=[0x42a]
    =================================
    0x54: v54(0x42a) = CONST 
    0x57: JUMP v54(0x42a)

    Begin block 0x42a
    prev=[0x54], succ=[]
    =================================
    0x42b: STOP 

    Begin block 0x58
    prev=[0x4a], succ=[0xc0, 0xbd]
    =================================
    0x59: v59(0x1) = CONST 
    0x5b: v5b = SLOAD v59(0x1)
    0x5c: v5c(0x40) = CONST 
    0x5f: v5f = MLOAD v5c(0x40)
    0x60: v60(0x20) = CONST 
    0x62: v62 = CALLDATASIZE 
    0x63: v63(0x1f) = CONST 
    0x66: v66 = ADD v62, v63(0x1f)
    0x69: v69 = DIV v66, v60(0x20)
    0x6b: v6b = MUL v60(0x20), v69
    0x6d: v6d = ADD v5f, v6b
    0x6f: v6f = ADD v60(0x20), v6d
    0x72: MSTORE v5c(0x40), v6f
    0x75: MSTORE v5f, v62
    0x76: v76(0x1) = CONST 
    0x78: v78(0x1) = CONST 
    0x7a: v7a(0xa0) = CONST 
    0x7c: v7c(0x10000000000000000000000000000000000000000) = SHL v7a(0xa0), v78(0x1)
    0x7d: v7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c(0x10000000000000000000000000000000000000000), v76(0x1)
    0x80: v80 = AND v5b, v7d(0xffffffffffffffffffffffffffffffffffffffff)
    0x82: v82(0x60) = CONST 
    0x85: v85(0x0) = CONST 
    0x8b: v8b = ADD v5f, v60(0x20)
    0x91: CALLDATACOPY v8b, v85(0x0), v62
    0x92: v92(0x0) = CONST 
    0x95: v95 = ADD v8b, v62
    0x98: MSTORE v95, v92(0x0)
    0x9b: v9b = MLOAD v5f
    0xa6: va6(0x20) = CONST 
    0xa9: va9 = ADD v5f, va6(0x20)
    0xab: vab = GAS 
    0xac: vac = DELEGATECALL vab, v80, va9, v9b, v92(0x0), v92(0x0)
    0xad: vad = RETURNDATASIZE 
    0xae: vae(0x40) = CONST 
    0xb0: vb0 = MLOAD vae(0x40)
    0xb2: vb2(0x0) = CONST 
    0xb5: RETURNDATACOPY vb0, vb2(0x0), vad
    0xb8: vb8 = ISZERO vac
    0xb9: vb9(0xc0) = CONST 
    0xbc: JUMPI vb9(0xc0), vb8

    Begin block 0xc0
    prev=[0x58], succ=[]
    =================================
    0xc3: REVERT vb0, vad

    Begin block 0xbd
    prev=[0x58], succ=[]
    =================================
    0xbf: RETURN vb0, vad

}

function implementation()() public {
    Begin block 0xc6
    prev=[], succ=[0xce, 0xd2]
    =================================
    0xc7: vc7 = CALLVALUE 
    0xc9: vc9 = ISZERO vc7
    0xca: vca(0xd2) = CONST 
    0xcd: JUMPI vca(0xd2), vc9

    Begin block 0xce
    prev=[0xc6], succ=[]
    =================================
    0xce: vce(0x0) = CONST 
    0xd1: REVERT vce(0x0), vce(0x0)

    Begin block 0xd2
    prev=[0xc6], succ=[0x19b]
    =================================
    0xd4: vd4(0x44b) = CONST 
    0xd7: vd7(0x19b) = CONST 
    0xda: JUMP vd7(0x19b)

    Begin block 0x19b
    prev=[0xd2], succ=[0x44b]
    =================================
    0x19c: v19c(0x1) = CONST 
    0x19e: v19e = SLOAD v19c(0x1)
    0x19f: v19f(0x1) = CONST 
    0x1a1: v1a1(0x1) = CONST 
    0x1a3: v1a3(0xa0) = CONST 
    0x1a5: v1a5(0x10000000000000000000000000000000000000000) = SHL v1a3(0xa0), v1a1(0x1)
    0x1a6: v1a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a5(0x10000000000000000000000000000000000000000), v19f(0x1)
    0x1a7: v1a7 = AND v1a6(0xffffffffffffffffffffffffffffffffffffffff), v19e
    0x1a9: JUMP vd4(0x44b)

    Begin block 0x44b
    prev=[0x19b], succ=[]
    =================================
    0x44c: v44c(0x40) = CONST 
    0x44f: v44f = MLOAD v44c(0x40)
    0x450: v450(0x1) = CONST 
    0x452: v452(0x1) = CONST 
    0x454: v454(0xa0) = CONST 
    0x456: v456(0x10000000000000000000000000000000000000000) = SHL v454(0xa0), v452(0x1)
    0x457: v457(0xffffffffffffffffffffffffffffffffffffffff) = SUB v456(0x10000000000000000000000000000000000000000), v450(0x1)
    0x45a: v45a = AND v1a7, v457(0xffffffffffffffffffffffffffffffffffffffff)
    0x45c: MSTORE v44f, v45a
    0x45d: v45d = MLOAD v44c(0x40)
    0x461: v461(0x0) = SUB v44f, v45d
    0x462: v462(0x20) = CONST 
    0x464: v464(0x20) = ADD v462(0x20), v461(0x0)
    0x466: RETURN v45d, v464(0x20)

}

function owner()() public {
    Begin block 0xf7
    prev=[], succ=[0xff, 0x103]
    =================================
    0xf8: vf8 = CALLVALUE 
    0xfa: vfa = ISZERO vf8
    0xfb: vfb(0x103) = CONST 
    0xfe: JUMPI vfb(0x103), vfa

    Begin block 0xff
    prev=[0xf7], succ=[]
    =================================
    0xff: vff(0x0) = CONST 
    0x102: REVERT vff(0x0), vff(0x0)

    Begin block 0x103
    prev=[0xf7], succ=[0x1aa]
    =================================
    0x105: v105(0x486) = CONST 
    0x108: v108(0x1aa) = CONST 
    0x10b: JUMP v108(0x1aa)

    Begin block 0x1aa
    prev=[0x103], succ=[0x486]
    =================================
    0x1ab: v1ab(0x0) = CONST 
    0x1ad: v1ad = SLOAD v1ab(0x0)
    0x1ae: v1ae(0x1) = CONST 
    0x1b0: v1b0(0x1) = CONST 
    0x1b2: v1b2(0xa0) = CONST 
    0x1b4: v1b4(0x10000000000000000000000000000000000000000) = SHL v1b2(0xa0), v1b0(0x1)
    0x1b5: v1b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b4(0x10000000000000000000000000000000000000000), v1ae(0x1)
    0x1b6: v1b6 = AND v1b5(0xffffffffffffffffffffffffffffffffffffffff), v1ad
    0x1b8: JUMP v105(0x486)

    Begin block 0x486
    prev=[0x1aa], succ=[]
    =================================
    0x487: v487(0x40) = CONST 
    0x48a: v48a = MLOAD v487(0x40)
    0x48b: v48b(0x1) = CONST 
    0x48d: v48d(0x1) = CONST 
    0x48f: v48f(0xa0) = CONST 
    0x491: v491(0x10000000000000000000000000000000000000000) = SHL v48f(0xa0), v48d(0x1)
    0x492: v492(0xffffffffffffffffffffffffffffffffffffffff) = SUB v491(0x10000000000000000000000000000000000000000), v48b(0x1)
    0x495: v495 = AND v1b6, v492(0xffffffffffffffffffffffffffffffffffffffff)
    0x497: MSTORE v48a, v495
    0x498: v498 = MLOAD v487(0x40)
    0x49c: v49c(0x0) = SUB v48a, v498
    0x49d: v49d(0x20) = CONST 
    0x49f: v49f(0x20) = ADD v49d(0x20), v49c(0x0)
    0x4a1: RETURN v498, v49f(0x20)

}

