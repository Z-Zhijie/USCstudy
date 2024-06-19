function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x60e]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x600: v600(0x60e) = CONST 
    0x601: JUMPI v600(0x60e), v8

    Begin block 0xd
    prev=[0x0], succ=[0x611, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5c60da1b) = CONST 
    0x19: v19 = EQ v14(0x5c60da1b), v12
    0x602: v602(0x611) = CONST 
    0x603: JUMPI v602(0x611), v19

    Begin block 0x611
    prev=[0xd], succ=[]
    =================================
    0x612: v612(0xd1) = CONST 
    0x613: CALLPRIVATE v612(0xd1)

    Begin block 0x1e
    prev=[0xd], succ=[0x614, 0x29]
    =================================
    0x1f: v1f(0x715018a6) = CONST 
    0x24: v24 = EQ v1f(0x715018a6), v12
    0x604: v604(0x614) = CONST 
    0x605: JUMPI v604(0x614), v24

    Begin block 0x614
    prev=[0x1e], succ=[]
    =================================
    0x615: v615(0x102) = CONST 
    0x616: CALLPRIVATE v615(0x102)

    Begin block 0x29
    prev=[0x1e], succ=[0x617, 0x34]
    =================================
    0x2a: v2a(0x8da5cb5b) = CONST 
    0x2f: v2f = EQ v2a(0x8da5cb5b), v12
    0x606: v606(0x617) = CONST 
    0x607: JUMPI v606(0x617), v2f

    Begin block 0x617
    prev=[0x29], succ=[]
    =================================
    0x618: v618(0x117) = CONST 
    0x619: CALLPRIVATE v618(0x117)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x61a]
    =================================
    0x35: v35(0x8f32d59b) = CONST 
    0x3a: v3a = EQ v35(0x8f32d59b), v12
    0x608: v608(0x61a) = CONST 
    0x609: JUMPI v608(0x61a), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x61d, 0x4a]
    =================================
    0x40: v40(0xd69efdc5) = CONST 
    0x45: v45 = EQ v40(0xd69efdc5), v12
    0x60a: v60a(0x61d) = CONST 
    0x60b: JUMPI v60a(0x61d), v45

    Begin block 0x61d
    prev=[0x3f], succ=[]
    =================================
    0x61e: v61e(0x155) = CONST 
    0x61f: CALLPRIVATE v61e(0x155)

    Begin block 0x4a
    prev=[0x3f], succ=[0x60e, 0x620]
    =================================
    0x4b: v4b(0xf2fde38b) = CONST 
    0x50: v50 = EQ v4b(0xf2fde38b), v12
    0x60c: v60c(0x620) = CONST 
    0x60d: JUMPI v60c(0x620), v50

    Begin block 0x60e
    prev=[0x0, 0x4a], succ=[]
    =================================
    0x60f: v60f(0x55) = CONST 
    0x610: CALLPRIVATE v60f(0x55)

    Begin block 0x620
    prev=[0x4a], succ=[]
    =================================
    0x621: v621(0x188) = CONST 
    0x622: CALLPRIVATE v621(0x188)

    Begin block 0x61a
    prev=[0x34], succ=[]
    =================================
    0x61b: v61b(0x12c) = CONST 
    0x61c: CALLPRIVATE v61b(0x12c)

}

function renounceOwnership()() public {
    Begin block 0x102
    prev=[], succ=[0x10a, 0x10e]
    =================================
    0x103: v103 = CALLVALUE 
    0x105: v105 = ISZERO v103
    0x106: v106(0x10e) = CONST 
    0x109: JUMPI v106(0x10e), v105

    Begin block 0x10a
    prev=[0x102], succ=[]
    =================================
    0x10a: v10a(0x0) = CONST 
    0x10d: REVERT v10a(0x0), v10a(0x0)

    Begin block 0x10e
    prev=[0x102], succ=[0x1ca]
    =================================
    0x110: v110(0x581) = CONST 
    0x113: v113(0x1ca) = CONST 
    0x116: JUMP v113(0x1ca)

    Begin block 0x1ca
    prev=[0x10e], succ=[0x27cB0x1ca]
    =================================
    0x1cb: v1cb(0x1d2) = CONST 
    0x1ce: v1ce(0x27c) = CONST 
    0x1d1: JUMP v1ce(0x27c)

    Begin block 0x27cB0x1ca
    prev=[0x1ca], succ=[0x3cbB0x1ca]
    =================================
    0x27dS0x1ca: v27dV1ca(0x0) = CONST 
    0x280S0x1ca: v280V1ca = SLOAD v27dV1ca(0x0)
    0x281S0x1ca: v281V1ca(0x1) = CONST 
    0x283S0x1ca: v283V1ca(0x1) = CONST 
    0x285S0x1ca: v285V1ca(0xa0) = CONST 
    0x287S0x1ca: v287V1ca(0x10000000000000000000000000000000000000000) = SHL v285V1ca(0xa0), v283V1ca(0x1)
    0x288S0x1ca: v288V1ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v287V1ca(0x10000000000000000000000000000000000000000), v281V1ca(0x1)
    0x289S0x1ca: v289V1ca = AND v288V1ca(0xffffffffffffffffffffffffffffffffffffffff), v280V1ca
    0x28aS0x1ca: v28aV1ca(0x291) = CONST 
    0x28dS0x1ca: v28dV1ca(0x3cb) = CONST 
    0x290S0x1ca: JUMP v28dV1ca(0x3cb)

    Begin block 0x3cbB0x1ca
    prev=[0x27cB0x1ca], succ=[0x291B0x1ca]
    =================================
    0x3ccS0x1ca: v3ccV1ca = CALLER 
    0x3ceS0x1ca: JUMP v28aV1ca(0x291)

    Begin block 0x291B0x1ca
    prev=[0x3cbB0x1ca], succ=[0x1d2]
    =================================
    0x292S0x1ca: v292V1ca(0x1) = CONST 
    0x294S0x1ca: v294V1ca(0x1) = CONST 
    0x296S0x1ca: v296V1ca(0xa0) = CONST 
    0x298S0x1ca: v298V1ca(0x10000000000000000000000000000000000000000) = SHL v296V1ca(0xa0), v294V1ca(0x1)
    0x299S0x1ca: v299V1ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v298V1ca(0x10000000000000000000000000000000000000000), v292V1ca(0x1)
    0x29aS0x1ca: v29aV1ca = AND v299V1ca(0xffffffffffffffffffffffffffffffffffffffff), v3ccV1ca
    0x29bS0x1ca: v29bV1ca = EQ v29aV1ca, v289V1ca
    0x29fS0x1ca: JUMP v1cb(0x1d2)

    Begin block 0x1d2
    prev=[0x291B0x1ca], succ=[0x1d7, 0x223]
    =================================
    0x1d3: v1d3(0x223) = CONST 
    0x1d6: JUMPI v1d3(0x223), v29bV1ca

    Begin block 0x1d7
    prev=[0x1d2], succ=[]
    =================================
    0x1d7: v1d7(0x40) = CONST 
    0x1da: v1da = MLOAD v1d7(0x40)
    0x1db: v1db(0x461bcd) = CONST 
    0x1df: v1df(0xe5) = CONST 
    0x1e1: v1e1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1df(0xe5), v1db(0x461bcd)
    0x1e3: MSTORE v1da, v1e1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e4: v1e4(0x20) = CONST 
    0x1e6: v1e6(0x4) = CONST 
    0x1e9: v1e9 = ADD v1da, v1e6(0x4)
    0x1ec: MSTORE v1e9, v1e4(0x20)
    0x1ed: v1ed(0x24) = CONST 
    0x1f0: v1f0 = ADD v1da, v1ed(0x24)
    0x1f1: MSTORE v1f0, v1e4(0x20)
    0x1f2: v1f2(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x213: v213(0x44) = CONST 
    0x216: v216 = ADD v1da, v213(0x44)
    0x217: MSTORE v216, v1f2(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x219: v219 = MLOAD v1d7(0x40)
    0x21d: v21d(0x0) = SUB v1da, v219
    0x21e: v21e(0x64) = CONST 
    0x220: v220(0x64) = ADD v21e(0x64), v21d(0x0)
    0x222: REVERT v219, v220(0x64)

    Begin block 0x223
    prev=[0x1d2], succ=[0x581]
    =================================
    0x224: v224(0x0) = CONST 
    0x227: v227 = SLOAD v224(0x0)
    0x228: v228(0x40) = CONST 
    0x22a: v22a = MLOAD v228(0x40)
    0x22b: v22b(0x1) = CONST 
    0x22d: v22d(0x1) = CONST 
    0x22f: v22f(0xa0) = CONST 
    0x231: v231(0x10000000000000000000000000000000000000000) = SHL v22f(0xa0), v22d(0x1)
    0x232: v232(0xffffffffffffffffffffffffffffffffffffffff) = SUB v231(0x10000000000000000000000000000000000000000), v22b(0x1)
    0x235: v235 = AND v227, v232(0xffffffffffffffffffffffffffffffffffffffff)
    0x237: v237(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x25b: LOG3 v22a, v224(0x0), v237(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v235, v224(0x0)
    0x25c: v25c(0x0) = CONST 
    0x25f: v25f = SLOAD v25c(0x0)
    0x260: v260(0x1) = CONST 
    0x262: v262(0x1) = CONST 
    0x264: v264(0xa0) = CONST 
    0x266: v266(0x10000000000000000000000000000000000000000) = SHL v264(0xa0), v262(0x1)
    0x267: v267(0xffffffffffffffffffffffffffffffffffffffff) = SUB v266(0x10000000000000000000000000000000000000000), v260(0x1)
    0x268: v268(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v267(0xffffffffffffffffffffffffffffffffffffffff)
    0x269: v269 = AND v268(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v25f
    0x26b: SSTORE v25c(0x0), v269
    0x26c: JUMP v110(0x581)

    Begin block 0x581
    prev=[0x223], succ=[]
    =================================
    0x582: STOP 

}

function owner()() public {
    Begin block 0x117
    prev=[], succ=[0x11f, 0x123]
    =================================
    0x118: v118 = CALLVALUE 
    0x11a: v11a = ISZERO v118
    0x11b: v11b(0x123) = CONST 
    0x11e: JUMPI v11b(0x123), v11a

    Begin block 0x11f
    prev=[0x117], succ=[]
    =================================
    0x11f: v11f(0x0) = CONST 
    0x122: REVERT v11f(0x0), v11f(0x0)

    Begin block 0x123
    prev=[0x117], succ=[0x26d]
    =================================
    0x125: v125(0x5a2) = CONST 
    0x128: v128(0x26d) = CONST 
    0x12b: JUMP v128(0x26d)

    Begin block 0x26d
    prev=[0x123], succ=[0x5a2]
    =================================
    0x26e: v26e(0x0) = CONST 
    0x270: v270 = SLOAD v26e(0x0)
    0x271: v271(0x1) = CONST 
    0x273: v273(0x1) = CONST 
    0x275: v275(0xa0) = CONST 
    0x277: v277(0x10000000000000000000000000000000000000000) = SHL v275(0xa0), v273(0x1)
    0x278: v278(0xffffffffffffffffffffffffffffffffffffffff) = SUB v277(0x10000000000000000000000000000000000000000), v271(0x1)
    0x279: v279 = AND v278(0xffffffffffffffffffffffffffffffffffffffff), v270
    0x27b: JUMP v125(0x5a2)

    Begin block 0x5a2
    prev=[0x26d], succ=[]
    =================================
    0x5a3: v5a3(0x40) = CONST 
    0x5a6: v5a6 = MLOAD v5a3(0x40)
    0x5a7: v5a7(0x1) = CONST 
    0x5a9: v5a9(0x1) = CONST 
    0x5ab: v5ab(0xa0) = CONST 
    0x5ad: v5ad(0x10000000000000000000000000000000000000000) = SHL v5ab(0xa0), v5a9(0x1)
    0x5ae: v5ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5ad(0x10000000000000000000000000000000000000000), v5a7(0x1)
    0x5b1: v5b1 = AND v279, v5ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x5b3: MSTORE v5a6, v5b1
    0x5b4: v5b4 = MLOAD v5a3(0x40)
    0x5b8: v5b8(0x0) = SUB v5a6, v5b4
    0x5b9: v5b9(0x20) = CONST 
    0x5bb: v5bb(0x20) = ADD v5b9(0x20), v5b8(0x0)
    0x5bd: RETURN v5b4, v5bb(0x20)

}

function isOwner()() public {
    Begin block 0x12c
    prev=[], succ=[0x134, 0x138]
    =================================
    0x12d: v12d = CALLVALUE 
    0x12f: v12f = ISZERO v12d
    0x130: v130(0x138) = CONST 
    0x133: JUMPI v130(0x138), v12f

    Begin block 0x134
    prev=[0x12c], succ=[]
    =================================
    0x134: v134(0x0) = CONST 
    0x137: REVERT v134(0x0), v134(0x0)

    Begin block 0x138
    prev=[0x12c], succ=[0x27cB0x138]
    =================================
    0x13a: v13a(0x141) = CONST 
    0x13d: v13d(0x27c) = CONST 
    0x140: JUMP v13d(0x27c)

    Begin block 0x27cB0x138
    prev=[0x138], succ=[0x3cbB0x138]
    =================================
    0x27dS0x138: v27dV138(0x0) = CONST 
    0x280S0x138: v280V138 = SLOAD v27dV138(0x0)
    0x281S0x138: v281V138(0x1) = CONST 
    0x283S0x138: v283V138(0x1) = CONST 
    0x285S0x138: v285V138(0xa0) = CONST 
    0x287S0x138: v287V138(0x10000000000000000000000000000000000000000) = SHL v285V138(0xa0), v283V138(0x1)
    0x288S0x138: v288V138(0xffffffffffffffffffffffffffffffffffffffff) = SUB v287V138(0x10000000000000000000000000000000000000000), v281V138(0x1)
    0x289S0x138: v289V138 = AND v288V138(0xffffffffffffffffffffffffffffffffffffffff), v280V138
    0x28aS0x138: v28aV138(0x291) = CONST 
    0x28dS0x138: v28dV138(0x3cb) = CONST 
    0x290S0x138: JUMP v28dV138(0x3cb)

    Begin block 0x3cbB0x138
    prev=[0x27cB0x138], succ=[0x291B0x138]
    =================================
    0x3ccS0x138: v3ccV138 = CALLER 
    0x3ceS0x138: JUMP v28aV138(0x291)

    Begin block 0x291B0x138
    prev=[0x3cbB0x138], succ=[0x141]
    =================================
    0x292S0x138: v292V138(0x1) = CONST 
    0x294S0x138: v294V138(0x1) = CONST 
    0x296S0x138: v296V138(0xa0) = CONST 
    0x298S0x138: v298V138(0x10000000000000000000000000000000000000000) = SHL v296V138(0xa0), v294V138(0x1)
    0x299S0x138: v299V138(0xffffffffffffffffffffffffffffffffffffffff) = SUB v298V138(0x10000000000000000000000000000000000000000), v292V138(0x1)
    0x29aS0x138: v29aV138 = AND v299V138(0xffffffffffffffffffffffffffffffffffffffff), v3ccV138
    0x29bS0x138: v29bV138 = EQ v29aV138, v289V138
    0x29fS0x138: JUMP v13a(0x141)

    Begin block 0x141
    prev=[0x291B0x138], succ=[]
    =================================
    0x142: v142(0x40) = CONST 
    0x145: v145 = MLOAD v142(0x40)
    0x147: v147 = ISZERO v29bV138
    0x148: v148 = ISZERO v147
    0x14a: MSTORE v145, v148
    0x14b: v14b = MLOAD v142(0x40)
    0x14f: v14f(0x0) = SUB v145, v14b
    0x150: v150(0x20) = CONST 
    0x152: v152(0x20) = ADD v150(0x20), v14f(0x0)
    0x154: RETURN v14b, v152(0x20)

}

function replaceImplementation(address)() public {
    Begin block 0x155
    prev=[], succ=[0x15d, 0x161]
    =================================
    0x156: v156 = CALLVALUE 
    0x158: v158 = ISZERO v156
    0x159: v159(0x161) = CONST 
    0x15c: JUMPI v159(0x161), v158

    Begin block 0x15d
    prev=[0x155], succ=[]
    =================================
    0x15d: v15d(0x0) = CONST 
    0x160: REVERT v15d(0x0), v15d(0x0)

    Begin block 0x161
    prev=[0x155], succ=[0x174, 0x178]
    =================================
    0x163: v163(0x5dd) = CONST 
    0x166: v166(0x4) = CONST 
    0x169: v169 = CALLDATASIZE 
    0x16a: v16a = SUB v169, v166(0x4)
    0x16b: v16b(0x20) = CONST 
    0x16e: v16e = LT v16a, v16b(0x20)
    0x16f: v16f = ISZERO v16e
    0x170: v170(0x178) = CONST 
    0x173: JUMPI v170(0x178), v16f

    Begin block 0x174
    prev=[0x161], succ=[]
    =================================
    0x174: v174(0x0) = CONST 
    0x177: REVERT v174(0x0), v174(0x0)

    Begin block 0x178
    prev=[0x161], succ=[0x2a0]
    =================================
    0x17a: v17a = CALLDATALOAD v166(0x4)
    0x17b: v17b(0x1) = CONST 
    0x17d: v17d(0x1) = CONST 
    0x17f: v17f(0xa0) = CONST 
    0x181: v181(0x10000000000000000000000000000000000000000) = SHL v17f(0xa0), v17d(0x1)
    0x182: v182(0xffffffffffffffffffffffffffffffffffffffff) = SUB v181(0x10000000000000000000000000000000000000000), v17b(0x1)
    0x183: v183 = AND v182(0xffffffffffffffffffffffffffffffffffffffff), v17a
    0x184: v184(0x2a0) = CONST 
    0x187: JUMP v184(0x2a0)

    Begin block 0x2a0
    prev=[0x178], succ=[0x27cB0x2a0]
    =================================
    0x2a1: v2a1(0x2a8) = CONST 
    0x2a4: v2a4(0x27c) = CONST 
    0x2a7: JUMP v2a4(0x27c)

    Begin block 0x27cB0x2a0
    prev=[0x2a0], succ=[0x3cbB0x2a0]
    =================================
    0x27dS0x2a0: v27dV2a0(0x0) = CONST 
    0x280S0x2a0: v280V2a0 = SLOAD v27dV2a0(0x0)
    0x281S0x2a0: v281V2a0(0x1) = CONST 
    0x283S0x2a0: v283V2a0(0x1) = CONST 
    0x285S0x2a0: v285V2a0(0xa0) = CONST 
    0x287S0x2a0: v287V2a0(0x10000000000000000000000000000000000000000) = SHL v285V2a0(0xa0), v283V2a0(0x1)
    0x288S0x2a0: v288V2a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v287V2a0(0x10000000000000000000000000000000000000000), v281V2a0(0x1)
    0x289S0x2a0: v289V2a0 = AND v288V2a0(0xffffffffffffffffffffffffffffffffffffffff), v280V2a0
    0x28aS0x2a0: v28aV2a0(0x291) = CONST 
    0x28dS0x2a0: v28dV2a0(0x3cb) = CONST 
    0x290S0x2a0: JUMP v28dV2a0(0x3cb)

    Begin block 0x3cbB0x2a0
    prev=[0x27cB0x2a0], succ=[0x291B0x2a0]
    =================================
    0x3ccS0x2a0: v3ccV2a0 = CALLER 
    0x3ceS0x2a0: JUMP v28aV2a0(0x291)

    Begin block 0x291B0x2a0
    prev=[0x3cbB0x2a0], succ=[0x2a8]
    =================================
    0x292S0x2a0: v292V2a0(0x1) = CONST 
    0x294S0x2a0: v294V2a0(0x1) = CONST 
    0x296S0x2a0: v296V2a0(0xa0) = CONST 
    0x298S0x2a0: v298V2a0(0x10000000000000000000000000000000000000000) = SHL v296V2a0(0xa0), v294V2a0(0x1)
    0x299S0x2a0: v299V2a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v298V2a0(0x10000000000000000000000000000000000000000), v292V2a0(0x1)
    0x29aS0x2a0: v29aV2a0 = AND v299V2a0(0xffffffffffffffffffffffffffffffffffffffff), v3ccV2a0
    0x29bS0x2a0: v29bV2a0 = EQ v29aV2a0, v289V2a0
    0x29fS0x2a0: JUMP v2a1(0x2a8)

    Begin block 0x2a8
    prev=[0x291B0x2a0], succ=[0x2ad, 0x2f9]
    =================================
    0x2a9: v2a9(0x2f9) = CONST 
    0x2ac: JUMPI v2a9(0x2f9), v29bV2a0

    Begin block 0x2ad
    prev=[0x2a8], succ=[]
    =================================
    0x2ad: v2ad(0x40) = CONST 
    0x2b0: v2b0 = MLOAD v2ad(0x40)
    0x2b1: v2b1(0x461bcd) = CONST 
    0x2b5: v2b5(0xe5) = CONST 
    0x2b7: v2b7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2b5(0xe5), v2b1(0x461bcd)
    0x2b9: MSTORE v2b0, v2b7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ba: v2ba(0x20) = CONST 
    0x2bc: v2bc(0x4) = CONST 
    0x2bf: v2bf = ADD v2b0, v2bc(0x4)
    0x2c2: MSTORE v2bf, v2ba(0x20)
    0x2c3: v2c3(0x24) = CONST 
    0x2c6: v2c6 = ADD v2b0, v2c3(0x24)
    0x2c7: MSTORE v2c6, v2ba(0x20)
    0x2c8: v2c8(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x2e9: v2e9(0x44) = CONST 
    0x2ec: v2ec = ADD v2b0, v2e9(0x44)
    0x2ed: MSTORE v2ec, v2c8(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x2ef: v2ef = MLOAD v2ad(0x40)
    0x2f3: v2f3(0x0) = SUB v2b0, v2ef
    0x2f4: v2f4(0x64) = CONST 
    0x2f6: v2f6(0x64) = ADD v2f4(0x64), v2f3(0x0)
    0x2f8: REVERT v2ef, v2f6(0x64)

    Begin block 0x2f9
    prev=[0x2a8], succ=[0x3cfB0x2f9]
    =================================
    0x2fa: v2fa(0x302) = CONST 
    0x2fe: v2fe(0x3cf) = CONST 
    0x301: JUMP v2fe(0x3cf)

    Begin block 0x3cfB0x2f9
    prev=[0x2f9], succ=[0x403B0x2f9, 0x3ffB0x2f9]
    =================================
    0x3d0S0x2f9: v3d0V2f9(0x0) = CONST 
    0x3d3S0x2f9: v3d3V2f9 = EXTCODEHASH v183
    0x3d4S0x2f9: v3d4V2f9(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x3f7S0x2f9: v3f7V2f9 = EQ v3d4V2f9(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470), v3d3V2f9
    0x3f9S0x2f9: v3f9V2f9 = ISZERO v3f7V2f9
    0x3fbS0x2f9: v3fbV2f9(0x403) = CONST 
    0x3feS0x2f9: JUMPI v3fbV2f9(0x403), v3f7V2f9

    Begin block 0x403B0x2f9
    prev=[0x3cfB0x2f9, 0x3ffB0x2f9], succ=[0x302]
    =================================
    0x403_0x0S0x2f9: v403_0V2f9 = PHI v3f9V2f9, v402V2f9
    0x40aS0x2f9: JUMP v2fa(0x302)

    Begin block 0x302
    prev=[0x403B0x2f9], succ=[0x307, 0x344]
    =================================
    0x303: v303(0x344) = CONST 
    0x306: JUMPI v303(0x344), v403_0V2f9

    Begin block 0x307
    prev=[0x302], succ=[]
    =================================
    0x307: v307(0x40) = CONST 
    0x30a: v30a = MLOAD v307(0x40)
    0x30b: v30b(0x461bcd) = CONST 
    0x30f: v30f(0xe5) = CONST 
    0x311: v311(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v30f(0xe5), v30b(0x461bcd)
    0x313: MSTORE v30a, v311(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x314: v314(0x20) = CONST 
    0x316: v316(0x4) = CONST 
    0x319: v319 = ADD v30a, v316(0x4)
    0x31a: MSTORE v319, v314(0x20)
    0x31b: v31b(0xe) = CONST 
    0x31d: v31d(0x24) = CONST 
    0x320: v320 = ADD v30a, v31d(0x24)
    0x321: MSTORE v320, v31b(0xe)
    0x322: v322(0x1b9bdd08184818dbdb9d1c9858dd) = CONST 
    0x331: v331(0x92) = CONST 
    0x333: v333(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000) = SHL v331(0x92), v322(0x1b9bdd08184818dbdb9d1c9858dd)
    0x334: v334(0x44) = CONST 
    0x337: v337 = ADD v30a, v334(0x44)
    0x338: MSTORE v337, v333(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000)
    0x33a: v33a = MLOAD v307(0x40)
    0x33e: v33e(0x0) = SUB v30a, v33a
    0x33f: v33f(0x64) = CONST 
    0x341: v341(0x64) = ADD v33f(0x64), v33e(0x0)
    0x343: REVERT v33a, v341(0x64)

    Begin block 0x344
    prev=[0x302], succ=[0x5dd]
    =================================
    0x345: v345(0x1) = CONST 
    0x348: v348 = SLOAD v345(0x1)
    0x349: v349(0x1) = CONST 
    0x34b: v34b(0x1) = CONST 
    0x34d: v34d(0xa0) = CONST 
    0x34f: v34f(0x10000000000000000000000000000000000000000) = SHL v34d(0xa0), v34b(0x1)
    0x350: v350(0xffffffffffffffffffffffffffffffffffffffff) = SUB v34f(0x10000000000000000000000000000000000000000), v349(0x1)
    0x351: v351(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v350(0xffffffffffffffffffffffffffffffffffffffff)
    0x352: v352 = AND v351(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v348
    0x353: v353(0x1) = CONST 
    0x355: v355(0x1) = CONST 
    0x357: v357(0xa0) = CONST 
    0x359: v359(0x10000000000000000000000000000000000000000) = SHL v357(0xa0), v355(0x1)
    0x35a: v35a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v359(0x10000000000000000000000000000000000000000), v353(0x1)
    0x35e: v35e = AND v35a(0xffffffffffffffffffffffffffffffffffffffff), v183
    0x362: v362 = OR v35e, v352
    0x364: SSTORE v345(0x1), v362
    0x365: JUMP v163(0x5dd)

    Begin block 0x5dd
    prev=[0x344], succ=[]
    =================================
    0x5de: STOP 

    Begin block 0x3ffB0x2f9
    prev=[0x3cfB0x2f9], succ=[0x403B0x2f9]
    =================================
    0x401S0x2f9: v401V2f9 = ISZERO v3d3V2f9
    0x402S0x2f9: v402V2f9 = ISZERO v401V2f9

}

function transferOwnership(address)() public {
    Begin block 0x188
    prev=[], succ=[0x190, 0x194]
    =================================
    0x189: v189 = CALLVALUE 
    0x18b: v18b = ISZERO v189
    0x18c: v18c(0x194) = CONST 
    0x18f: JUMPI v18c(0x194), v18b

    Begin block 0x190
    prev=[0x188], succ=[]
    =================================
    0x190: v190(0x0) = CONST 
    0x193: REVERT v190(0x0), v190(0x0)

    Begin block 0x194
    prev=[0x188], succ=[0x1a7, 0x1ab]
    =================================
    0x196: v196(0x5fe) = CONST 
    0x199: v199(0x4) = CONST 
    0x19c: v19c = CALLDATASIZE 
    0x19d: v19d = SUB v19c, v199(0x4)
    0x19e: v19e(0x20) = CONST 
    0x1a1: v1a1 = LT v19d, v19e(0x20)
    0x1a2: v1a2 = ISZERO v1a1
    0x1a3: v1a3(0x1ab) = CONST 
    0x1a6: JUMPI v1a3(0x1ab), v1a2

    Begin block 0x1a7
    prev=[0x194], succ=[]
    =================================
    0x1a7: v1a7(0x0) = CONST 
    0x1aa: REVERT v1a7(0x0), v1a7(0x0)

    Begin block 0x1ab
    prev=[0x194], succ=[0x366]
    =================================
    0x1ad: v1ad = CALLDATALOAD v199(0x4)
    0x1ae: v1ae(0x1) = CONST 
    0x1b0: v1b0(0x1) = CONST 
    0x1b2: v1b2(0xa0) = CONST 
    0x1b4: v1b4(0x10000000000000000000000000000000000000000) = SHL v1b2(0xa0), v1b0(0x1)
    0x1b5: v1b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b4(0x10000000000000000000000000000000000000000), v1ae(0x1)
    0x1b6: v1b6 = AND v1b5(0xffffffffffffffffffffffffffffffffffffffff), v1ad
    0x1b7: v1b7(0x366) = CONST 
    0x1ba: JUMP v1b7(0x366)

    Begin block 0x366
    prev=[0x1ab], succ=[0x27cB0x366]
    =================================
    0x367: v367(0x36e) = CONST 
    0x36a: v36a(0x27c) = CONST 
    0x36d: JUMP v36a(0x27c)

    Begin block 0x27cB0x366
    prev=[0x366], succ=[0x3cbB0x366]
    =================================
    0x27dS0x366: v27dV366(0x0) = CONST 
    0x280S0x366: v280V366 = SLOAD v27dV366(0x0)
    0x281S0x366: v281V366(0x1) = CONST 
    0x283S0x366: v283V366(0x1) = CONST 
    0x285S0x366: v285V366(0xa0) = CONST 
    0x287S0x366: v287V366(0x10000000000000000000000000000000000000000) = SHL v285V366(0xa0), v283V366(0x1)
    0x288S0x366: v288V366(0xffffffffffffffffffffffffffffffffffffffff) = SUB v287V366(0x10000000000000000000000000000000000000000), v281V366(0x1)
    0x289S0x366: v289V366 = AND v288V366(0xffffffffffffffffffffffffffffffffffffffff), v280V366
    0x28aS0x366: v28aV366(0x291) = CONST 
    0x28dS0x366: v28dV366(0x3cb) = CONST 
    0x290S0x366: JUMP v28dV366(0x3cb)

    Begin block 0x3cbB0x366
    prev=[0x27cB0x366], succ=[0x291B0x366]
    =================================
    0x3ccS0x366: v3ccV366 = CALLER 
    0x3ceS0x366: JUMP v28aV366(0x291)

    Begin block 0x291B0x366
    prev=[0x3cbB0x366], succ=[0x36e]
    =================================
    0x292S0x366: v292V366(0x1) = CONST 
    0x294S0x366: v294V366(0x1) = CONST 
    0x296S0x366: v296V366(0xa0) = CONST 
    0x298S0x366: v298V366(0x10000000000000000000000000000000000000000) = SHL v296V366(0xa0), v294V366(0x1)
    0x299S0x366: v299V366(0xffffffffffffffffffffffffffffffffffffffff) = SUB v298V366(0x10000000000000000000000000000000000000000), v292V366(0x1)
    0x29aS0x366: v29aV366 = AND v299V366(0xffffffffffffffffffffffffffffffffffffffff), v3ccV366
    0x29bS0x366: v29bV366 = EQ v29aV366, v289V366
    0x29fS0x366: JUMP v367(0x36e)

    Begin block 0x36e
    prev=[0x291B0x366], succ=[0x373, 0x3bf]
    =================================
    0x36f: v36f(0x3bf) = CONST 
    0x372: JUMPI v36f(0x3bf), v29bV366

    Begin block 0x373
    prev=[0x36e], succ=[]
    =================================
    0x373: v373(0x40) = CONST 
    0x376: v376 = MLOAD v373(0x40)
    0x377: v377(0x461bcd) = CONST 
    0x37b: v37b(0xe5) = CONST 
    0x37d: v37d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v37b(0xe5), v377(0x461bcd)
    0x37f: MSTORE v376, v37d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x380: v380(0x20) = CONST 
    0x382: v382(0x4) = CONST 
    0x385: v385 = ADD v376, v382(0x4)
    0x388: MSTORE v385, v380(0x20)
    0x389: v389(0x24) = CONST 
    0x38c: v38c = ADD v376, v389(0x24)
    0x38d: MSTORE v38c, v380(0x20)
    0x38e: v38e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x3af: v3af(0x44) = CONST 
    0x3b2: v3b2 = ADD v376, v3af(0x44)
    0x3b3: MSTORE v3b2, v38e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x3b5: v3b5 = MLOAD v373(0x40)
    0x3b9: v3b9(0x0) = SUB v376, v3b5
    0x3ba: v3ba(0x64) = CONST 
    0x3bc: v3bc(0x64) = ADD v3ba(0x64), v3b9(0x0)
    0x3be: REVERT v3b5, v3bc(0x64)

    Begin block 0x3bf
    prev=[0x36e], succ=[0x40b]
    =================================
    0x3c0: v3c0(0x3c8) = CONST 
    0x3c4: v3c4(0x40b) = CONST 
    0x3c7: JUMP v3c4(0x40b)

    Begin block 0x40b
    prev=[0x3bf], succ=[0x41a, 0x450]
    =================================
    0x40c: v40c(0x1) = CONST 
    0x40e: v40e(0x1) = CONST 
    0x410: v410(0xa0) = CONST 
    0x412: v412(0x10000000000000000000000000000000000000000) = SHL v410(0xa0), v40e(0x1)
    0x413: v413(0xffffffffffffffffffffffffffffffffffffffff) = SUB v412(0x10000000000000000000000000000000000000000), v40c(0x1)
    0x415: v415 = AND v1b6, v413(0xffffffffffffffffffffffffffffffffffffffff)
    0x416: v416(0x450) = CONST 
    0x419: JUMPI v416(0x450), v415

    Begin block 0x41a
    prev=[0x40b], succ=[]
    =================================
    0x41a: v41a(0x40) = CONST 
    0x41c: v41c = MLOAD v41a(0x40)
    0x41d: v41d(0x461bcd) = CONST 
    0x421: v421(0xe5) = CONST 
    0x423: v423(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v421(0xe5), v41d(0x461bcd)
    0x425: MSTORE v41c, v423(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x426: v426(0x4) = CONST 
    0x428: v428 = ADD v426(0x4), v41c
    0x42b: v42b(0x20) = CONST 
    0x42d: v42d = ADD v42b(0x20), v428
    0x430: v430(0x20) = SUB v42d, v428
    0x432: MSTORE v428, v430(0x20)
    0x433: v433(0x26) = CONST 
    0x436: MSTORE v42d, v433(0x26)
    0x437: v437(0x20) = CONST 
    0x439: v439 = ADD v437(0x20), v42d
    0x43b: v43b(0x4ac) = CONST 
    0x43e: v43e(0x26) = CONST 
    0x441: CODECOPY v439, v43b(0x4ac), v43e(0x26)
    0x442: v442(0x40) = CONST 
    0x444: v444 = ADD v442(0x40), v439
    0x448: v448(0x40) = CONST 
    0x44a: v44a = MLOAD v448(0x40)
    0x44d: v44d(0x84) = SUB v444, v44a
    0x44f: REVERT v44a, v44d(0x84)

    Begin block 0x450
    prev=[0x40b], succ=[0x3c8]
    =================================
    0x451: v451(0x0) = CONST 
    0x454: v454 = SLOAD v451(0x0)
    0x455: v455(0x40) = CONST 
    0x457: v457 = MLOAD v455(0x40)
    0x458: v458(0x1) = CONST 
    0x45a: v45a(0x1) = CONST 
    0x45c: v45c(0xa0) = CONST 
    0x45e: v45e(0x10000000000000000000000000000000000000000) = SHL v45c(0xa0), v45a(0x1)
    0x45f: v45f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45e(0x10000000000000000000000000000000000000000), v458(0x1)
    0x462: v462 = AND v1b6, v45f(0xffffffffffffffffffffffffffffffffffffffff)
    0x465: v465 = AND v454, v45f(0xffffffffffffffffffffffffffffffffffffffff)
    0x467: v467(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x489: LOG3 v457, v451(0x0), v467(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v465, v462
    0x48a: v48a(0x0) = CONST 
    0x48d: v48d = SLOAD v48a(0x0)
    0x48e: v48e(0x1) = CONST 
    0x490: v490(0x1) = CONST 
    0x492: v492(0xa0) = CONST 
    0x494: v494(0x10000000000000000000000000000000000000000) = SHL v492(0xa0), v490(0x1)
    0x495: v495(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494(0x10000000000000000000000000000000000000000), v48e(0x1)
    0x496: v496(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v495(0xffffffffffffffffffffffffffffffffffffffff)
    0x497: v497 = AND v496(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v48d
    0x498: v498(0x1) = CONST 
    0x49a: v49a(0x1) = CONST 
    0x49c: v49c(0xa0) = CONST 
    0x49e: v49e(0x10000000000000000000000000000000000000000) = SHL v49c(0xa0), v49a(0x1)
    0x49f: v49f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49e(0x10000000000000000000000000000000000000000), v498(0x1)
    0x4a3: v4a3 = AND v49f(0xffffffffffffffffffffffffffffffffffffffff), v1b6
    0x4a7: v4a7 = OR v4a3, v497
    0x4a9: SSTORE v48a(0x0), v4a7
    0x4aa: JUMP v3c0(0x3c8)

    Begin block 0x3c8
    prev=[0x450], succ=[0x5fe]
    =================================
    0x3ca: JUMP v196(0x5fe)

    Begin block 0x5fe
    prev=[0x3c8], succ=[]
    =================================
    0x5ff: STOP 

}

function fallback()() public {
    Begin block 0x55
    prev=[], succ=[0x5f, 0x63]
    =================================
    0x56: v56(0x8fc) = CONST 
    0x59: v59 = GAS 
    0x5a: v5a = GT v59, v56(0x8fc)
    0x5b: v5b(0x63) = CONST 
    0x5e: JUMPI v5b(0x63), v5a

    Begin block 0x5f
    prev=[0x55], succ=[0x525]
    =================================
    0x5f: v5f(0x525) = CONST 
    0x62: JUMP v5f(0x525)

    Begin block 0x525
    prev=[0x5f], succ=[]
    =================================
    0x526: STOP 

    Begin block 0x63
    prev=[0x55], succ=[0xcb, 0xc8]
    =================================
    0x64: v64(0x1) = CONST 
    0x66: v66 = SLOAD v64(0x1)
    0x67: v67(0x40) = CONST 
    0x6a: v6a = MLOAD v67(0x40)
    0x6b: v6b(0x20) = CONST 
    0x6d: v6d = CALLDATASIZE 
    0x6e: v6e(0x1f) = CONST 
    0x71: v71 = ADD v6d, v6e(0x1f)
    0x74: v74 = DIV v71, v6b(0x20)
    0x76: v76 = MUL v6b(0x20), v74
    0x78: v78 = ADD v6a, v76
    0x7a: v7a = ADD v6b(0x20), v78
    0x7d: MSTORE v67(0x40), v7a
    0x80: MSTORE v6a, v6d
    0x81: v81(0x1) = CONST 
    0x83: v83(0x1) = CONST 
    0x85: v85(0xa0) = CONST 
    0x87: v87(0x10000000000000000000000000000000000000000) = SHL v85(0xa0), v83(0x1)
    0x88: v88(0xffffffffffffffffffffffffffffffffffffffff) = SUB v87(0x10000000000000000000000000000000000000000), v81(0x1)
    0x8b: v8b = AND v66, v88(0xffffffffffffffffffffffffffffffffffffffff)
    0x8d: v8d(0x60) = CONST 
    0x90: v90(0x0) = CONST 
    0x96: v96 = ADD v6a, v6b(0x20)
    0x9c: CALLDATACOPY v96, v90(0x0), v6d
    0x9d: v9d(0x0) = CONST 
    0xa0: va0 = ADD v96, v6d
    0xa3: MSTORE va0, v9d(0x0)
    0xa6: va6 = MLOAD v6a
    0xb1: vb1(0x20) = CONST 
    0xb4: vb4 = ADD v6a, vb1(0x20)
    0xb6: vb6 = GAS 
    0xb7: vb7 = DELEGATECALL vb6, v8b, vb4, va6, v9d(0x0), v9d(0x0)
    0xb8: vb8 = RETURNDATASIZE 
    0xb9: vb9(0x40) = CONST 
    0xbb: vbb = MLOAD vb9(0x40)
    0xbd: vbd(0x0) = CONST 
    0xc0: RETURNDATACOPY vbb, vbd(0x0), vb8
    0xc3: vc3 = ISZERO vb7
    0xc4: vc4(0xcb) = CONST 
    0xc7: JUMPI vc4(0xcb), vc3

    Begin block 0xcb
    prev=[0x63], succ=[]
    =================================
    0xce: REVERT vbb, vb8

    Begin block 0xc8
    prev=[0x63], succ=[]
    =================================
    0xca: RETURN vbb, vb8

}

function implementation()() public {
    Begin block 0xd1
    prev=[], succ=[0xd9, 0xdd]
    =================================
    0xd2: vd2 = CALLVALUE 
    0xd4: vd4 = ISZERO vd2
    0xd5: vd5(0xdd) = CONST 
    0xd8: JUMPI vd5(0xdd), vd4

    Begin block 0xd9
    prev=[0xd1], succ=[]
    =================================
    0xd9: vd9(0x0) = CONST 
    0xdc: REVERT vd9(0x0), vd9(0x0)

    Begin block 0xdd
    prev=[0xd1], succ=[0x1bb]
    =================================
    0xdf: vdf(0x546) = CONST 
    0xe2: ve2(0x1bb) = CONST 
    0xe5: JUMP ve2(0x1bb)

    Begin block 0x1bb
    prev=[0xdd], succ=[0x546]
    =================================
    0x1bc: v1bc(0x1) = CONST 
    0x1be: v1be = SLOAD v1bc(0x1)
    0x1bf: v1bf(0x1) = CONST 
    0x1c1: v1c1(0x1) = CONST 
    0x1c3: v1c3(0xa0) = CONST 
    0x1c5: v1c5(0x10000000000000000000000000000000000000000) = SHL v1c3(0xa0), v1c1(0x1)
    0x1c6: v1c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c5(0x10000000000000000000000000000000000000000), v1bf(0x1)
    0x1c7: v1c7 = AND v1c6(0xffffffffffffffffffffffffffffffffffffffff), v1be
    0x1c9: JUMP vdf(0x546)

    Begin block 0x546
    prev=[0x1bb], succ=[]
    =================================
    0x547: v547(0x40) = CONST 
    0x54a: v54a = MLOAD v547(0x40)
    0x54b: v54b(0x1) = CONST 
    0x54d: v54d(0x1) = CONST 
    0x54f: v54f(0xa0) = CONST 
    0x551: v551(0x10000000000000000000000000000000000000000) = SHL v54f(0xa0), v54d(0x1)
    0x552: v552(0xffffffffffffffffffffffffffffffffffffffff) = SUB v551(0x10000000000000000000000000000000000000000), v54b(0x1)
    0x555: v555 = AND v1c7, v552(0xffffffffffffffffffffffffffffffffffffffff)
    0x557: MSTORE v54a, v555
    0x558: v558 = MLOAD v547(0x40)
    0x55c: v55c(0x0) = SUB v54a, v558
    0x55d: v55d(0x20) = CONST 
    0x55f: v55f(0x20) = ADD v55d(0x20), v55c(0x0)
    0x561: RETURN v558, v55f(0x20)

}

