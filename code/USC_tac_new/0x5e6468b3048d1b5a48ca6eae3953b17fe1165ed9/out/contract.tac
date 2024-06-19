function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x877]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x861: v861(0x877) = CONST 
    0x862: JUMPI v861(0x877), v8

    Begin block 0xd
    prev=[0x0], succ=[0x59, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0xc1e80334) = CONST 
    0x19: v19 = GT v14(0xc1e80334), v12
    0x1a: v1a(0x59) = CONST 
    0x1d: JUMPI v1a(0x59), v19

    Begin block 0x59
    prev=[0xd], succ=[0x87a, 0x65]
    =================================
    0x5b: v5b(0x26782247) = CONST 
    0x60: v60 = EQ v5b(0x26782247), v12
    0x86d: v86d(0x87a) = CONST 
    0x86e: JUMPI v86d(0x87a), v60

    Begin block 0x87a
    prev=[0x59], succ=[]
    =================================
    0x87b: v87b(0x114) = CONST 
    0x87c: CALLPRIVATE v87b(0x114)

    Begin block 0x65
    prev=[0x59], succ=[0x70, 0x87d]
    =================================
    0x66: v66(0x396f7b23) = CONST 
    0x6b: v6b = EQ v66(0x396f7b23), v12
    0x86f: v86f(0x87d) = CONST 
    0x870: JUMPI v86f(0x87d), v6b

    Begin block 0x70
    prev=[0x65], succ=[0x880, 0x7b]
    =================================
    0x71: v71(0x52f98dd4) = CONST 
    0x76: v76 = EQ v71(0x52f98dd4), v12
    0x871: v871(0x880) = CONST 
    0x872: JUMPI v871(0x880), v76

    Begin block 0x880
    prev=[0x70], succ=[]
    =================================
    0x881: v881(0x15a) = CONST 
    0x882: CALLPRIVATE v881(0x15a)

    Begin block 0x7b
    prev=[0x70], succ=[0x883, 0x86]
    =================================
    0x7c: v7c(0x5c60da1b) = CONST 
    0x81: v81 = EQ v7c(0x5c60da1b), v12
    0x873: v873(0x883) = CONST 
    0x874: JUMPI v873(0x883), v81

    Begin block 0x883
    prev=[0x7b], succ=[]
    =================================
    0x884: v884(0x16f) = CONST 
    0x885: CALLPRIVATE v884(0x16f)

    Begin block 0x86
    prev=[0x7b], succ=[0x877, 0x886]
    =================================
    0x87: v87(0xb71d1a0c) = CONST 
    0x8c: v8c = EQ v87(0xb71d1a0c), v12
    0x875: v875(0x886) = CONST 
    0x876: JUMPI v875(0x886), v8c

    Begin block 0x877
    prev=[0x0, 0x86], succ=[]
    =================================
    0x878: v878(0x91) = CONST 
    0x879: CALLPRIVATE v878(0x91)

    Begin block 0x886
    prev=[0x86], succ=[]
    =================================
    0x887: v887(0x184) = CONST 
    0x888: CALLPRIVATE v887(0x184)

    Begin block 0x87d
    prev=[0x65], succ=[]
    =================================
    0x87e: v87e(0x145) = CONST 
    0x87f: CALLPRIVATE v87e(0x145)

    Begin block 0x1e
    prev=[0xd], succ=[0x889, 0x29]
    =================================
    0x1f: v1f(0xc1e80334) = CONST 
    0x24: v24 = EQ v1f(0xc1e80334), v12
    0x863: v863(0x889) = CONST 
    0x864: JUMPI v863(0x889), v24

    Begin block 0x889
    prev=[0x1e], succ=[]
    =================================
    0x88a: v88a(0x1b9) = CONST 
    0x88b: CALLPRIVATE v88a(0x1b9)

    Begin block 0x29
    prev=[0x1e], succ=[0x88c, 0x34]
    =================================
    0x2a: v2a(0xe992a041) = CONST 
    0x2f: v2f = EQ v2a(0xe992a041), v12
    0x865: v865(0x88c) = CONST 
    0x866: JUMPI v865(0x88c), v2f

    Begin block 0x88c
    prev=[0x29], succ=[]
    =================================
    0x88d: v88d(0x1ce) = CONST 
    0x88e: CALLPRIVATE v88d(0x1ce)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x88f]
    =================================
    0x35: v35(0xe9c714f2) = CONST 
    0x3a: v3a = EQ v35(0xe9c714f2), v12
    0x867: v867(0x88f) = CONST 
    0x868: JUMPI v867(0x88f), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x892, 0x4a]
    =================================
    0x40: v40(0xf3b04558) = CONST 
    0x45: v45 = EQ v40(0xf3b04558), v12
    0x869: v869(0x892) = CONST 
    0x86a: JUMPI v869(0x892), v45

    Begin block 0x892
    prev=[0x3f], succ=[]
    =================================
    0x893: v893(0x216) = CONST 
    0x894: CALLPRIVATE v893(0x216)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0x895]
    =================================
    0x4b: v4b(0xf851a440) = CONST 
    0x50: v50 = EQ v4b(0xf851a440), v12
    0x86b: v86b(0x895) = CONST 
    0x86c: JUMPI v86b(0x895), v50

    Begin block 0x55
    prev=[0x4a], succ=[]
    =================================
    0x55: v55(0x91) = CONST 
    0x58: JUMP v55(0x91)

    Begin block 0x895
    prev=[0x4a], succ=[]
    =================================
    0x896: v896(0x22b) = CONST 
    0x897: CALLPRIVATE v896(0x22b)

    Begin block 0x88f
    prev=[0x34], succ=[]
    =================================
    0x890: v890(0x201) = CONST 
    0x891: CALLPRIVATE v890(0x201)

}

function pendingAdmin()() public {
    Begin block 0x114
    prev=[], succ=[0x11c, 0x120]
    =================================
    0x115: v115 = CALLVALUE 
    0x117: v117 = ISZERO v115
    0x118: v118(0x120) = CONST 
    0x11b: JUMPI v118(0x120), v117

    Begin block 0x11c
    prev=[0x114], succ=[]
    =================================
    0x11c: v11c(0x0) = CONST 
    0x11f: REVERT v11c(0x0), v11c(0x0)

    Begin block 0x120
    prev=[0x114], succ=[0x240]
    =================================
    0x122: v122(0x69a) = CONST 
    0x125: v125(0x240) = CONST 
    0x128: JUMP v125(0x240)

    Begin block 0x240
    prev=[0x120], succ=[0x69a]
    =================================
    0x241: v241(0x3) = CONST 
    0x243: v243 = SLOAD v241(0x3)
    0x244: v244(0x1) = CONST 
    0x246: v246(0x1) = CONST 
    0x248: v248(0xa0) = CONST 
    0x24a: v24a(0x10000000000000000000000000000000000000000) = SHL v248(0xa0), v246(0x1)
    0x24b: v24b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24a(0x10000000000000000000000000000000000000000), v244(0x1)
    0x24c: v24c = AND v24b(0xffffffffffffffffffffffffffffffffffffffff), v243
    0x24e: JUMP v122(0x69a)

    Begin block 0x69a
    prev=[0x240], succ=[]
    =================================
    0x69b: v69b(0x40) = CONST 
    0x69e: v69e = MLOAD v69b(0x40)
    0x69f: v69f(0x1) = CONST 
    0x6a1: v6a1(0x1) = CONST 
    0x6a3: v6a3(0xa0) = CONST 
    0x6a5: v6a5(0x10000000000000000000000000000000000000000) = SHL v6a3(0xa0), v6a1(0x1)
    0x6a6: v6a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6a5(0x10000000000000000000000000000000000000000), v69f(0x1)
    0x6a9: v6a9 = AND v24c, v6a6(0xffffffffffffffffffffffffffffffffffffffff)
    0x6ab: MSTORE v69e, v6a9
    0x6ac: v6ac = MLOAD v69b(0x40)
    0x6b0: v6b0(0x0) = SUB v69e, v6ac
    0x6b1: v6b1(0x20) = CONST 
    0x6b3: v6b3(0x20) = ADD v6b1(0x20), v6b0(0x0)
    0x6b5: RETURN v6ac, v6b3(0x20)

}

function pendingImplementation()() public {
    Begin block 0x145
    prev=[], succ=[0x14d, 0x151]
    =================================
    0x146: v146 = CALLVALUE 
    0x148: v148 = ISZERO v146
    0x149: v149(0x151) = CONST 
    0x14c: JUMPI v149(0x151), v148

    Begin block 0x14d
    prev=[0x145], succ=[]
    =================================
    0x14d: v14d(0x0) = CONST 
    0x150: REVERT v14d(0x0), v14d(0x0)

    Begin block 0x151
    prev=[0x145], succ=[0x24f]
    =================================
    0x153: v153(0x6d5) = CONST 
    0x156: v156(0x24f) = CONST 
    0x159: JUMP v156(0x24f)

    Begin block 0x24f
    prev=[0x151], succ=[0x6d5]
    =================================
    0x250: v250(0x5) = CONST 
    0x252: v252 = SLOAD v250(0x5)
    0x253: v253(0x1) = CONST 
    0x255: v255(0x1) = CONST 
    0x257: v257(0xa0) = CONST 
    0x259: v259(0x10000000000000000000000000000000000000000) = SHL v257(0xa0), v255(0x1)
    0x25a: v25a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v259(0x10000000000000000000000000000000000000000), v253(0x1)
    0x25b: v25b = AND v25a(0xffffffffffffffffffffffffffffffffffffffff), v252
    0x25d: JUMP v153(0x6d5)

    Begin block 0x6d5
    prev=[0x24f], succ=[]
    =================================
    0x6d6: v6d6(0x40) = CONST 
    0x6d9: v6d9 = MLOAD v6d6(0x40)
    0x6da: v6da(0x1) = CONST 
    0x6dc: v6dc(0x1) = CONST 
    0x6de: v6de(0xa0) = CONST 
    0x6e0: v6e0(0x10000000000000000000000000000000000000000) = SHL v6de(0xa0), v6dc(0x1)
    0x6e1: v6e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e0(0x10000000000000000000000000000000000000000), v6da(0x1)
    0x6e4: v6e4 = AND v25b, v6e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x6e6: MSTORE v6d9, v6e4
    0x6e7: v6e7 = MLOAD v6d6(0x40)
    0x6eb: v6eb(0x0) = SUB v6d9, v6e7
    0x6ec: v6ec(0x20) = CONST 
    0x6ee: v6ee(0x20) = ADD v6ec(0x20), v6eb(0x0)
    0x6f0: RETURN v6e7, v6ee(0x20)

}

function efilAddress()() public {
    Begin block 0x15a
    prev=[], succ=[0x162, 0x166]
    =================================
    0x15b: v15b = CALLVALUE 
    0x15d: v15d = ISZERO v15b
    0x15e: v15e(0x166) = CONST 
    0x161: JUMPI v15e(0x166), v15d

    Begin block 0x162
    prev=[0x15a], succ=[]
    =================================
    0x162: v162(0x0) = CONST 
    0x165: REVERT v162(0x0), v162(0x0)

    Begin block 0x166
    prev=[0x15a], succ=[0x25e]
    =================================
    0x168: v168(0x710) = CONST 
    0x16b: v16b(0x25e) = CONST 
    0x16e: JUMP v16b(0x25e)

    Begin block 0x25e
    prev=[0x166], succ=[0x710]
    =================================
    0x25f: v25f(0x1) = CONST 
    0x261: v261 = SLOAD v25f(0x1)
    0x262: v262(0x1) = CONST 
    0x264: v264(0x1) = CONST 
    0x266: v266(0xa0) = CONST 
    0x268: v268(0x10000000000000000000000000000000000000000) = SHL v266(0xa0), v264(0x1)
    0x269: v269(0xffffffffffffffffffffffffffffffffffffffff) = SUB v268(0x10000000000000000000000000000000000000000), v262(0x1)
    0x26a: v26a = AND v269(0xffffffffffffffffffffffffffffffffffffffff), v261
    0x26c: JUMP v168(0x710)

    Begin block 0x710
    prev=[0x25e], succ=[]
    =================================
    0x711: v711(0x40) = CONST 
    0x714: v714 = MLOAD v711(0x40)
    0x715: v715(0x1) = CONST 
    0x717: v717(0x1) = CONST 
    0x719: v719(0xa0) = CONST 
    0x71b: v71b(0x10000000000000000000000000000000000000000) = SHL v719(0xa0), v717(0x1)
    0x71c: v71c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71b(0x10000000000000000000000000000000000000000), v715(0x1)
    0x71f: v71f = AND v26a, v71c(0xffffffffffffffffffffffffffffffffffffffff)
    0x721: MSTORE v714, v71f
    0x722: v722 = MLOAD v711(0x40)
    0x726: v726(0x0) = SUB v714, v722
    0x727: v727(0x20) = CONST 
    0x729: v729(0x20) = ADD v727(0x20), v726(0x0)
    0x72b: RETURN v722, v729(0x20)

}

function implementation()() public {
    Begin block 0x16f
    prev=[], succ=[0x177, 0x17b]
    =================================
    0x170: v170 = CALLVALUE 
    0x172: v172 = ISZERO v170
    0x173: v173(0x17b) = CONST 
    0x176: JUMPI v173(0x17b), v172

    Begin block 0x177
    prev=[0x16f], succ=[]
    =================================
    0x177: v177(0x0) = CONST 
    0x17a: REVERT v177(0x0), v177(0x0)

    Begin block 0x17b
    prev=[0x16f], succ=[0x26d]
    =================================
    0x17d: v17d(0x74b) = CONST 
    0x180: v180(0x26d) = CONST 
    0x183: JUMP v180(0x26d)

    Begin block 0x26d
    prev=[0x17b], succ=[0x74b]
    =================================
    0x26e: v26e(0x4) = CONST 
    0x270: v270 = SLOAD v26e(0x4)
    0x271: v271(0x1) = CONST 
    0x273: v273(0x1) = CONST 
    0x275: v275(0xa0) = CONST 
    0x277: v277(0x10000000000000000000000000000000000000000) = SHL v275(0xa0), v273(0x1)
    0x278: v278(0xffffffffffffffffffffffffffffffffffffffff) = SUB v277(0x10000000000000000000000000000000000000000), v271(0x1)
    0x279: v279 = AND v278(0xffffffffffffffffffffffffffffffffffffffff), v270
    0x27b: JUMP v17d(0x74b)

    Begin block 0x74b
    prev=[0x26d], succ=[]
    =================================
    0x74c: v74c(0x40) = CONST 
    0x74f: v74f = MLOAD v74c(0x40)
    0x750: v750(0x1) = CONST 
    0x752: v752(0x1) = CONST 
    0x754: v754(0xa0) = CONST 
    0x756: v756(0x10000000000000000000000000000000000000000) = SHL v754(0xa0), v752(0x1)
    0x757: v757(0xffffffffffffffffffffffffffffffffffffffff) = SUB v756(0x10000000000000000000000000000000000000000), v750(0x1)
    0x75a: v75a = AND v279, v757(0xffffffffffffffffffffffffffffffffffffffff)
    0x75c: MSTORE v74f, v75a
    0x75d: v75d = MLOAD v74c(0x40)
    0x761: v761(0x0) = SUB v74f, v75d
    0x762: v762(0x20) = CONST 
    0x764: v764(0x20) = ADD v762(0x20), v761(0x0)
    0x766: RETURN v75d, v764(0x20)

}

function _setPendingAdmin(address)() public {
    Begin block 0x184
    prev=[], succ=[0x18c, 0x190]
    =================================
    0x185: v185 = CALLVALUE 
    0x187: v187 = ISZERO v185
    0x188: v188(0x190) = CONST 
    0x18b: JUMPI v188(0x190), v187

    Begin block 0x18c
    prev=[0x184], succ=[]
    =================================
    0x18c: v18c(0x0) = CONST 
    0x18f: REVERT v18c(0x0), v18c(0x0)

    Begin block 0x190
    prev=[0x184], succ=[0x1a3, 0x1a7]
    =================================
    0x192: v192(0x786) = CONST 
    0x195: v195(0x4) = CONST 
    0x198: v198 = CALLDATASIZE 
    0x199: v199 = SUB v198, v195(0x4)
    0x19a: v19a(0x20) = CONST 
    0x19d: v19d = LT v199, v19a(0x20)
    0x19e: v19e = ISZERO v19d
    0x19f: v19f(0x1a7) = CONST 
    0x1a2: JUMPI v19f(0x1a7), v19e

    Begin block 0x1a3
    prev=[0x190], succ=[]
    =================================
    0x1a3: v1a3(0x0) = CONST 
    0x1a6: REVERT v1a3(0x0), v1a3(0x0)

    Begin block 0x1a7
    prev=[0x190], succ=[0x27c]
    =================================
    0x1a9: v1a9 = CALLDATALOAD v195(0x4)
    0x1aa: v1aa(0x1) = CONST 
    0x1ac: v1ac(0x1) = CONST 
    0x1ae: v1ae(0xa0) = CONST 
    0x1b0: v1b0(0x10000000000000000000000000000000000000000) = SHL v1ae(0xa0), v1ac(0x1)
    0x1b1: v1b1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b0(0x10000000000000000000000000000000000000000), v1aa(0x1)
    0x1b2: v1b2 = AND v1b1(0xffffffffffffffffffffffffffffffffffffffff), v1a9
    0x1b3: v1b3(0x27c) = CONST 
    0x1b6: JUMP v1b3(0x27c)

    Begin block 0x27c
    prev=[0x1a7], succ=[0x28f, 0x2c9]
    =================================
    0x27d: v27d(0x2) = CONST 
    0x27f: v27f = SLOAD v27d(0x2)
    0x280: v280(0x1) = CONST 
    0x282: v282(0x1) = CONST 
    0x284: v284(0xa0) = CONST 
    0x286: v286(0x10000000000000000000000000000000000000000) = SHL v284(0xa0), v282(0x1)
    0x287: v287(0xffffffffffffffffffffffffffffffffffffffff) = SUB v286(0x10000000000000000000000000000000000000000), v280(0x1)
    0x288: v288 = AND v287(0xffffffffffffffffffffffffffffffffffffffff), v27f
    0x289: v289 = CALLER 
    0x28a: v28a = EQ v289, v288
    0x28b: v28b(0x2c9) = CONST 
    0x28e: JUMPI v28b(0x2c9), v28a

    Begin block 0x28f
    prev=[0x27c], succ=[]
    =================================
    0x28f: v28f(0x40) = CONST 
    0x292: v292 = MLOAD v28f(0x40)
    0x293: v293(0x461bcd) = CONST 
    0x297: v297(0xe5) = CONST 
    0x299: v299(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v297(0xe5), v293(0x461bcd)
    0x29b: MSTORE v292, v299(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29c: v29c(0x20) = CONST 
    0x29e: v29e(0x4) = CONST 
    0x2a1: v2a1 = ADD v292, v29e(0x4)
    0x2a2: MSTORE v2a1, v29c(0x20)
    0x2a3: v2a3(0xb) = CONST 
    0x2a5: v2a5(0x24) = CONST 
    0x2a8: v2a8 = ADD v292, v2a5(0x24)
    0x2a9: MSTORE v2a8, v2a3(0xb)
    0x2aa: v2aa(0x61646d696e20636865636b) = CONST 
    0x2b6: v2b6(0xa8) = CONST 
    0x2b8: v2b8(0x61646d696e20636865636b000000000000000000000000000000000000000000) = SHL v2b6(0xa8), v2aa(0x61646d696e20636865636b)
    0x2b9: v2b9(0x44) = CONST 
    0x2bc: v2bc = ADD v292, v2b9(0x44)
    0x2bd: MSTORE v2bc, v2b8(0x61646d696e20636865636b000000000000000000000000000000000000000000)
    0x2bf: v2bf = MLOAD v28f(0x40)
    0x2c3: v2c3(0x0) = SUB v292, v2bf
    0x2c4: v2c4(0x64) = CONST 
    0x2c6: v2c6(0x64) = ADD v2c4(0x64), v2c3(0x0)
    0x2c8: REVERT v2bf, v2c6(0x64)

    Begin block 0x2c9
    prev=[0x27c], succ=[0x786]
    =================================
    0x2ca: v2ca(0x3) = CONST 
    0x2cd: v2cd = SLOAD v2ca(0x3)
    0x2ce: v2ce(0x1) = CONST 
    0x2d0: v2d0(0x1) = CONST 
    0x2d2: v2d2(0xa0) = CONST 
    0x2d4: v2d4(0x10000000000000000000000000000000000000000) = SHL v2d2(0xa0), v2d0(0x1)
    0x2d5: v2d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d4(0x10000000000000000000000000000000000000000), v2ce(0x1)
    0x2d8: v2d8 = AND v2d5(0xffffffffffffffffffffffffffffffffffffffff), v1b2
    0x2d9: v2d9(0x1) = CONST 
    0x2db: v2db(0x1) = CONST 
    0x2dd: v2dd(0xa0) = CONST 
    0x2df: v2df(0x10000000000000000000000000000000000000000) = SHL v2dd(0xa0), v2db(0x1)
    0x2e0: v2e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2df(0x10000000000000000000000000000000000000000), v2d9(0x1)
    0x2e1: v2e1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2e0(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e3: v2e3 = AND v2cd, v2e1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x2e5: v2e5 = OR v2d8, v2e3
    0x2e8: SSTORE v2ca(0x3), v2e5
    0x2e9: v2e9(0x40) = CONST 
    0x2ec: v2ec = MLOAD v2e9(0x40)
    0x2f0: v2f0 = AND v2cd, v2d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x2f3: MSTORE v2ec, v2f0
    0x2f4: v2f4(0x20) = CONST 
    0x2f7: v2f7 = ADD v2ec, v2f4(0x20)
    0x2fb: MSTORE v2f7, v2d8
    0x2fd: v2fd = MLOAD v2e9(0x40)
    0x2fe: v2fe(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x323: v323(0x0) = SUB v2ec, v2fd
    0x326: v326(0x40) = ADD v2e9(0x40), v323(0x0)
    0x328: LOG1 v2fd, v326(0x40), v2fe(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x32b: JUMP v192(0x786)

    Begin block 0x786
    prev=[0x2c9], succ=[]
    =================================
    0x787: STOP 

}

function _acceptImplementation()() public {
    Begin block 0x1b9
    prev=[], succ=[0x1c1, 0x1c5]
    =================================
    0x1ba: v1ba = CALLVALUE 
    0x1bc: v1bc = ISZERO v1ba
    0x1bd: v1bd(0x1c5) = CONST 
    0x1c0: JUMPI v1bd(0x1c5), v1bc

    Begin block 0x1c1
    prev=[0x1b9], succ=[]
    =================================
    0x1c1: v1c1(0x0) = CONST 
    0x1c4: REVERT v1c1(0x0), v1c1(0x0)

    Begin block 0x1c5
    prev=[0x1b9], succ=[0x32c]
    =================================
    0x1c7: v1c7(0x7a7) = CONST 
    0x1ca: v1ca(0x32c) = CONST 
    0x1cd: JUMP v1ca(0x32c)

    Begin block 0x32c
    prev=[0x1c5], succ=[0x350, 0x341]
    =================================
    0x32d: v32d(0x5) = CONST 
    0x32f: v32f = SLOAD v32d(0x5)
    0x330: v330(0x1) = CONST 
    0x332: v332(0x1) = CONST 
    0x334: v334(0xa0) = CONST 
    0x336: v336(0x10000000000000000000000000000000000000000) = SHL v334(0xa0), v332(0x1)
    0x337: v337(0xffffffffffffffffffffffffffffffffffffffff) = SUB v336(0x10000000000000000000000000000000000000000), v330(0x1)
    0x338: v338 = AND v337(0xffffffffffffffffffffffffffffffffffffffff), v32f
    0x339: v339 = CALLER 
    0x33a: v33a = EQ v339, v338
    0x33c: v33c = ISZERO v33a
    0x33d: v33d(0x350) = CONST 
    0x340: JUMPI v33d(0x350), v33c

    Begin block 0x350
    prev=[0x32c, 0x341], succ=[0x355, 0x3a1]
    =================================
    0x350_0x0: v350_0 = PHI v33a, v34f
    0x351: v351(0x3a1) = CONST 
    0x354: JUMPI v351(0x3a1), v350_0

    Begin block 0x355
    prev=[0x350], succ=[]
    =================================
    0x355: v355(0x40) = CONST 
    0x358: v358 = MLOAD v355(0x40)
    0x359: v359(0x461bcd) = CONST 
    0x35d: v35d(0xe5) = CONST 
    0x35f: v35f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v35d(0xe5), v359(0x461bcd)
    0x361: MSTORE v358, v35f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x362: v362(0x20) = CONST 
    0x364: v364(0x4) = CONST 
    0x367: v367 = ADD v358, v364(0x4)
    0x368: MSTORE v367, v362(0x20)
    0x369: v369(0x1b) = CONST 
    0x36b: v36b(0x24) = CONST 
    0x36e: v36e = ADD v358, v36b(0x24)
    0x36f: MSTORE v36e, v369(0x1b)
    0x370: v370(0x70656e64696e67496d706c656d656e746174696f6e20636865636b0000000000) = CONST 
    0x391: v391(0x44) = CONST 
    0x394: v394 = ADD v358, v391(0x44)
    0x395: MSTORE v394, v370(0x70656e64696e67496d706c656d656e746174696f6e20636865636b0000000000)
    0x397: v397 = MLOAD v355(0x40)
    0x39b: v39b(0x0) = SUB v358, v397
    0x39c: v39c(0x64) = CONST 
    0x39e: v39e(0x64) = ADD v39c(0x64), v39b(0x0)
    0x3a0: REVERT v397, v39e(0x64)

    Begin block 0x3a1
    prev=[0x350], succ=[0x7a7]
    =================================
    0x3a2: v3a2(0x4) = CONST 
    0x3a5: v3a5 = SLOAD v3a2(0x4)
    0x3a6: v3a6(0x5) = CONST 
    0x3a9: v3a9 = SLOAD v3a6(0x5)
    0x3aa: v3aa(0x1) = CONST 
    0x3ac: v3ac(0x1) = CONST 
    0x3ae: v3ae(0xa0) = CONST 
    0x3b0: v3b0(0x10000000000000000000000000000000000000000) = SHL v3ae(0xa0), v3ac(0x1)
    0x3b1: v3b1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b0(0x10000000000000000000000000000000000000000), v3aa(0x1)
    0x3b4: v3b4 = AND v3a9, v3b1(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b5: v3b5(0x1) = CONST 
    0x3b7: v3b7(0x1) = CONST 
    0x3b9: v3b9(0xa0) = CONST 
    0x3bb: v3bb(0x10000000000000000000000000000000000000000) = SHL v3b9(0xa0), v3b7(0x1)
    0x3bc: v3bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3bb(0x10000000000000000000000000000000000000000), v3b5(0x1)
    0x3bd: v3bd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3bc(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c0: v3c0 = AND v3a5, v3bd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3c2: v3c2 = OR v3b4, v3c0
    0x3c6: SSTORE v3a2(0x4), v3c2
    0x3c9: v3c9 = AND v3a9, v3bd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3cc: SSTORE v3a6(0x5), v3c9
    0x3cd: v3cd(0x40) = CONST 
    0x3d0: v3d0 = MLOAD v3cd(0x40)
    0x3d3: v3d3 = AND v3b1(0xffffffffffffffffffffffffffffffffffffffff), v3a5
    0x3d6: MSTORE v3d0, v3d3
    0x3da: v3da = AND v3b1(0xffffffffffffffffffffffffffffffffffffffff), v3c2
    0x3db: v3db(0x20) = CONST 
    0x3de: v3de = ADD v3d0, v3db(0x20)
    0x3df: MSTORE v3de, v3da
    0x3e1: v3e1 = MLOAD v3cd(0x40)
    0x3e4: v3e4(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x409: v409(0x0) = SUB v3d0, v3e1
    0x40a: v40a(0x40) = ADD v409(0x0), v3cd(0x40)
    0x40c: LOG1 v3e1, v40a(0x40), v3e4(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x40d: v40d(0x5) = CONST 
    0x40f: v40f = SLOAD v40d(0x5)
    0x410: v410(0x40) = CONST 
    0x413: v413 = MLOAD v410(0x40)
    0x414: v414(0x1) = CONST 
    0x416: v416(0x1) = CONST 
    0x418: v418(0xa0) = CONST 
    0x41a: v41a(0x10000000000000000000000000000000000000000) = SHL v418(0xa0), v416(0x1)
    0x41b: v41b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v41a(0x10000000000000000000000000000000000000000), v414(0x1)
    0x41e: v41e = AND v3b4, v41b(0xffffffffffffffffffffffffffffffffffffffff)
    0x420: MSTORE v413, v41e
    0x423: v423 = AND v40f, v41b(0xffffffffffffffffffffffffffffffffffffffff)
    0x424: v424(0x20) = CONST 
    0x427: v427 = ADD v413, v424(0x20)
    0x428: MSTORE v427, v423
    0x42a: v42a = MLOAD v410(0x40)
    0x42b: v42b(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x44f: v44f(0x0) = SUB v413, v42a
    0x452: v452(0x40) = ADD v410(0x40), v44f(0x0)
    0x454: LOG1 v42a, v452(0x40), v42b(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x457: JUMP v1c7(0x7a7)

    Begin block 0x7a7
    prev=[0x3a1], succ=[]
    =================================
    0x7a8: STOP 

    Begin block 0x341
    prev=[0x32c], succ=[0x350]
    =================================
    0x342: v342(0x5) = CONST 
    0x344: v344 = SLOAD v342(0x5)
    0x345: v345(0x1) = CONST 
    0x347: v347(0x1) = CONST 
    0x349: v349(0xa0) = CONST 
    0x34b: v34b(0x10000000000000000000000000000000000000000) = SHL v349(0xa0), v347(0x1)
    0x34c: v34c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v34b(0x10000000000000000000000000000000000000000), v345(0x1)
    0x34d: v34d = AND v34c(0xffffffffffffffffffffffffffffffffffffffff), v344
    0x34e: v34e = ISZERO v34d
    0x34f: v34f = ISZERO v34e

}

function _setPendingImplementation(address)() public {
    Begin block 0x1ce
    prev=[], succ=[0x1d6, 0x1da]
    =================================
    0x1cf: v1cf = CALLVALUE 
    0x1d1: v1d1 = ISZERO v1cf
    0x1d2: v1d2(0x1da) = CONST 
    0x1d5: JUMPI v1d2(0x1da), v1d1

    Begin block 0x1d6
    prev=[0x1ce], succ=[]
    =================================
    0x1d6: v1d6(0x0) = CONST 
    0x1d9: REVERT v1d6(0x0), v1d6(0x0)

    Begin block 0x1da
    prev=[0x1ce], succ=[0x1ed, 0x1f1]
    =================================
    0x1dc: v1dc(0x7c8) = CONST 
    0x1df: v1df(0x4) = CONST 
    0x1e2: v1e2 = CALLDATASIZE 
    0x1e3: v1e3 = SUB v1e2, v1df(0x4)
    0x1e4: v1e4(0x20) = CONST 
    0x1e7: v1e7 = LT v1e3, v1e4(0x20)
    0x1e8: v1e8 = ISZERO v1e7
    0x1e9: v1e9(0x1f1) = CONST 
    0x1ec: JUMPI v1e9(0x1f1), v1e8

    Begin block 0x1ed
    prev=[0x1da], succ=[]
    =================================
    0x1ed: v1ed(0x0) = CONST 
    0x1f0: REVERT v1ed(0x0), v1ed(0x0)

    Begin block 0x1f1
    prev=[0x1da], succ=[0x458]
    =================================
    0x1f3: v1f3 = CALLDATALOAD v1df(0x4)
    0x1f4: v1f4(0x1) = CONST 
    0x1f6: v1f6(0x1) = CONST 
    0x1f8: v1f8(0xa0) = CONST 
    0x1fa: v1fa(0x10000000000000000000000000000000000000000) = SHL v1f8(0xa0), v1f6(0x1)
    0x1fb: v1fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fa(0x10000000000000000000000000000000000000000), v1f4(0x1)
    0x1fc: v1fc = AND v1fb(0xffffffffffffffffffffffffffffffffffffffff), v1f3
    0x1fd: v1fd(0x458) = CONST 
    0x200: JUMP v1fd(0x458)

    Begin block 0x458
    prev=[0x1f1], succ=[0x46b, 0x4a5]
    =================================
    0x459: v459(0x2) = CONST 
    0x45b: v45b = SLOAD v459(0x2)
    0x45c: v45c(0x1) = CONST 
    0x45e: v45e(0x1) = CONST 
    0x460: v460(0xa0) = CONST 
    0x462: v462(0x10000000000000000000000000000000000000000) = SHL v460(0xa0), v45e(0x1)
    0x463: v463(0xffffffffffffffffffffffffffffffffffffffff) = SUB v462(0x10000000000000000000000000000000000000000), v45c(0x1)
    0x464: v464 = AND v463(0xffffffffffffffffffffffffffffffffffffffff), v45b
    0x465: v465 = CALLER 
    0x466: v466 = EQ v465, v464
    0x467: v467(0x4a5) = CONST 
    0x46a: JUMPI v467(0x4a5), v466

    Begin block 0x46b
    prev=[0x458], succ=[]
    =================================
    0x46b: v46b(0x40) = CONST 
    0x46e: v46e = MLOAD v46b(0x40)
    0x46f: v46f(0x461bcd) = CONST 
    0x473: v473(0xe5) = CONST 
    0x475: v475(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v473(0xe5), v46f(0x461bcd)
    0x477: MSTORE v46e, v475(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x478: v478(0x20) = CONST 
    0x47a: v47a(0x4) = CONST 
    0x47d: v47d = ADD v46e, v47a(0x4)
    0x47e: MSTORE v47d, v478(0x20)
    0x47f: v47f(0xb) = CONST 
    0x481: v481(0x24) = CONST 
    0x484: v484 = ADD v46e, v481(0x24)
    0x485: MSTORE v484, v47f(0xb)
    0x486: v486(0x61646d696e20636865636b) = CONST 
    0x492: v492(0xa8) = CONST 
    0x494: v494(0x61646d696e20636865636b000000000000000000000000000000000000000000) = SHL v492(0xa8), v486(0x61646d696e20636865636b)
    0x495: v495(0x44) = CONST 
    0x498: v498 = ADD v46e, v495(0x44)
    0x499: MSTORE v498, v494(0x61646d696e20636865636b000000000000000000000000000000000000000000)
    0x49b: v49b = MLOAD v46b(0x40)
    0x49f: v49f(0x0) = SUB v46e, v49b
    0x4a0: v4a0(0x64) = CONST 
    0x4a2: v4a2(0x64) = ADD v4a0(0x64), v49f(0x0)
    0x4a4: REVERT v49b, v4a2(0x64)

    Begin block 0x4a5
    prev=[0x458], succ=[0x7c8]
    =================================
    0x4a6: v4a6(0x5) = CONST 
    0x4a9: v4a9 = SLOAD v4a6(0x5)
    0x4aa: v4aa(0x1) = CONST 
    0x4ac: v4ac(0x1) = CONST 
    0x4ae: v4ae(0xa0) = CONST 
    0x4b0: v4b0(0x10000000000000000000000000000000000000000) = SHL v4ae(0xa0), v4ac(0x1)
    0x4b1: v4b1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b0(0x10000000000000000000000000000000000000000), v4aa(0x1)
    0x4b4: v4b4 = AND v4b1(0xffffffffffffffffffffffffffffffffffffffff), v1fc
    0x4b5: v4b5(0x1) = CONST 
    0x4b7: v4b7(0x1) = CONST 
    0x4b9: v4b9(0xa0) = CONST 
    0x4bb: v4bb(0x10000000000000000000000000000000000000000) = SHL v4b9(0xa0), v4b7(0x1)
    0x4bc: v4bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4bb(0x10000000000000000000000000000000000000000), v4b5(0x1)
    0x4bd: v4bd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4bc(0xffffffffffffffffffffffffffffffffffffffff)
    0x4bf: v4bf = AND v4a9, v4bd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4c0: v4c0 = OR v4bf, v4b4
    0x4c4: SSTORE v4a6(0x5), v4c0
    0x4c5: v4c5(0x40) = CONST 
    0x4c8: v4c8 = MLOAD v4c5(0x40)
    0x4cb: v4cb = AND v4b1(0xffffffffffffffffffffffffffffffffffffffff), v4a9
    0x4ce: MSTORE v4c8, v4cb
    0x4d2: v4d2 = AND v4b1(0xffffffffffffffffffffffffffffffffffffffff), v4c0
    0x4d3: v4d3(0x20) = CONST 
    0x4d6: v4d6 = ADD v4c8, v4d3(0x20)
    0x4d7: MSTORE v4d6, v4d2
    0x4d9: v4d9 = MLOAD v4c5(0x40)
    0x4da: v4da(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x4fe: v4fe(0x0) = SUB v4c8, v4d9
    0x501: v501(0x40) = ADD v4c5(0x40), v4fe(0x0)
    0x503: LOG1 v4d9, v501(0x40), v4da(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x506: JUMP v1dc(0x7c8)

    Begin block 0x7c8
    prev=[0x4a5], succ=[]
    =================================
    0x7c9: STOP 

}

function _acceptAdmin()() public {
    Begin block 0x201
    prev=[], succ=[0x209, 0x20d]
    =================================
    0x202: v202 = CALLVALUE 
    0x204: v204 = ISZERO v202
    0x205: v205(0x20d) = CONST 
    0x208: JUMPI v205(0x20d), v204

    Begin block 0x209
    prev=[0x201], succ=[]
    =================================
    0x209: v209(0x0) = CONST 
    0x20c: REVERT v209(0x0), v209(0x0)

    Begin block 0x20d
    prev=[0x201], succ=[0x507]
    =================================
    0x20f: v20f(0x7e9) = CONST 
    0x212: v212(0x507) = CONST 
    0x215: JUMP v212(0x507)

    Begin block 0x507
    prev=[0x20d], succ=[0x52b, 0x51c]
    =================================
    0x508: v508(0x3) = CONST 
    0x50a: v50a = SLOAD v508(0x3)
    0x50b: v50b(0x1) = CONST 
    0x50d: v50d(0x1) = CONST 
    0x50f: v50f(0xa0) = CONST 
    0x511: v511(0x10000000000000000000000000000000000000000) = SHL v50f(0xa0), v50d(0x1)
    0x512: v512(0xffffffffffffffffffffffffffffffffffffffff) = SUB v511(0x10000000000000000000000000000000000000000), v50b(0x1)
    0x513: v513 = AND v512(0xffffffffffffffffffffffffffffffffffffffff), v50a
    0x514: v514 = CALLER 
    0x515: v515 = EQ v514, v513
    0x517: v517 = ISZERO v515
    0x518: v518(0x52b) = CONST 
    0x51b: JUMPI v518(0x52b), v517

    Begin block 0x52b
    prev=[0x507, 0x51c], succ=[0x530, 0x571]
    =================================
    0x52b_0x0: v52b_0 = PHI v515, v52a
    0x52c: v52c(0x571) = CONST 
    0x52f: JUMPI v52c(0x571), v52b_0

    Begin block 0x530
    prev=[0x52b], succ=[]
    =================================
    0x530: v530(0x40) = CONST 
    0x533: v533 = MLOAD v530(0x40)
    0x534: v534(0x461bcd) = CONST 
    0x538: v538(0xe5) = CONST 
    0x53a: v53a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v538(0xe5), v534(0x461bcd)
    0x53c: MSTORE v533, v53a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x53d: v53d(0x20) = CONST 
    0x53f: v53f(0x4) = CONST 
    0x542: v542 = ADD v533, v53f(0x4)
    0x543: MSTORE v542, v53d(0x20)
    0x544: v544(0x12) = CONST 
    0x546: v546(0x24) = CONST 
    0x549: v549 = ADD v533, v546(0x24)
    0x54a: MSTORE v549, v544(0x12)
    0x54b: v54b(0x70656e64696e6741646d696e20636865636b) = CONST 
    0x55e: v55e(0x70) = CONST 
    0x560: v560(0x70656e64696e6741646d696e20636865636b0000000000000000000000000000) = SHL v55e(0x70), v54b(0x70656e64696e6741646d696e20636865636b)
    0x561: v561(0x44) = CONST 
    0x564: v564 = ADD v533, v561(0x44)
    0x565: MSTORE v564, v560(0x70656e64696e6741646d696e20636865636b0000000000000000000000000000)
    0x567: v567 = MLOAD v530(0x40)
    0x56b: v56b(0x0) = SUB v533, v567
    0x56c: v56c(0x64) = CONST 
    0x56e: v56e(0x64) = ADD v56c(0x64), v56b(0x0)
    0x570: REVERT v567, v56e(0x64)

    Begin block 0x571
    prev=[0x52b], succ=[0x7e9]
    =================================
    0x572: v572(0x2) = CONST 
    0x575: v575 = SLOAD v572(0x2)
    0x576: v576(0x3) = CONST 
    0x579: v579 = SLOAD v576(0x3)
    0x57a: v57a(0x1) = CONST 
    0x57c: v57c(0x1) = CONST 
    0x57e: v57e(0xa0) = CONST 
    0x580: v580(0x10000000000000000000000000000000000000000) = SHL v57e(0xa0), v57c(0x1)
    0x581: v581(0xffffffffffffffffffffffffffffffffffffffff) = SUB v580(0x10000000000000000000000000000000000000000), v57a(0x1)
    0x584: v584 = AND v579, v581(0xffffffffffffffffffffffffffffffffffffffff)
    0x585: v585(0x1) = CONST 
    0x587: v587(0x1) = CONST 
    0x589: v589(0xa0) = CONST 
    0x58b: v58b(0x10000000000000000000000000000000000000000) = SHL v589(0xa0), v587(0x1)
    0x58c: v58c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v58b(0x10000000000000000000000000000000000000000), v585(0x1)
    0x58d: v58d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v58c(0xffffffffffffffffffffffffffffffffffffffff)
    0x590: v590 = AND v575, v58d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x592: v592 = OR v584, v590
    0x596: SSTORE v572(0x2), v592
    0x599: v599 = AND v579, v58d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x59c: SSTORE v576(0x3), v599
    0x59d: v59d(0x40) = CONST 
    0x5a0: v5a0 = MLOAD v59d(0x40)
    0x5a3: v5a3 = AND v581(0xffffffffffffffffffffffffffffffffffffffff), v575
    0x5a6: MSTORE v5a0, v5a3
    0x5aa: v5aa = AND v581(0xffffffffffffffffffffffffffffffffffffffff), v592
    0x5ab: v5ab(0x20) = CONST 
    0x5ae: v5ae = ADD v5a0, v5ab(0x20)
    0x5af: MSTORE v5ae, v5aa
    0x5b1: v5b1 = MLOAD v59d(0x40)
    0x5b4: v5b4(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x5d9: v5d9(0x0) = SUB v5a0, v5b1
    0x5da: v5da(0x40) = ADD v5d9(0x0), v59d(0x40)
    0x5dc: LOG1 v5b1, v5da(0x40), v5b4(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x5dd: v5dd(0x3) = CONST 
    0x5df: v5df = SLOAD v5dd(0x3)
    0x5e0: v5e0(0x40) = CONST 
    0x5e3: v5e3 = MLOAD v5e0(0x40)
    0x5e4: v5e4(0x1) = CONST 
    0x5e6: v5e6(0x1) = CONST 
    0x5e8: v5e8(0xa0) = CONST 
    0x5ea: v5ea(0x10000000000000000000000000000000000000000) = SHL v5e8(0xa0), v5e6(0x1)
    0x5eb: v5eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5ea(0x10000000000000000000000000000000000000000), v5e4(0x1)
    0x5ee: v5ee = AND v584, v5eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x5f0: MSTORE v5e3, v5ee
    0x5f3: v5f3 = AND v5df, v5eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x5f4: v5f4(0x20) = CONST 
    0x5f7: v5f7 = ADD v5e3, v5f4(0x20)
    0x5f8: MSTORE v5f7, v5f3
    0x5fa: v5fa = MLOAD v5e0(0x40)
    0x5fb: v5fb(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x61f: v61f(0x0) = SUB v5e3, v5fa
    0x622: v622(0x40) = ADD v5e0(0x40), v61f(0x0)
    0x624: LOG1 v5fa, v622(0x40), v5fb(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x627: JUMP v20f(0x7e9)

    Begin block 0x7e9
    prev=[0x571], succ=[]
    =================================
    0x7ea: STOP 

    Begin block 0x51c
    prev=[0x507], succ=[0x52b]
    =================================
    0x51d: v51d(0x3) = CONST 
    0x51f: v51f = SLOAD v51d(0x3)
    0x520: v520(0x1) = CONST 
    0x522: v522(0x1) = CONST 
    0x524: v524(0xa0) = CONST 
    0x526: v526(0x10000000000000000000000000000000000000000) = SHL v524(0xa0), v522(0x1)
    0x527: v527(0xffffffffffffffffffffffffffffffffffffffff) = SUB v526(0x10000000000000000000000000000000000000000), v520(0x1)
    0x528: v528 = AND v527(0xffffffffffffffffffffffffffffffffffffffff), v51f
    0x529: v529 = ISZERO v528
    0x52a: v52a = ISZERO v529

}

function filstAddress()() public {
    Begin block 0x216
    prev=[], succ=[0x21e, 0x222]
    =================================
    0x217: v217 = CALLVALUE 
    0x219: v219 = ISZERO v217
    0x21a: v21a(0x222) = CONST 
    0x21d: JUMPI v21a(0x222), v219

    Begin block 0x21e
    prev=[0x216], succ=[]
    =================================
    0x21e: v21e(0x0) = CONST 
    0x221: REVERT v21e(0x0), v21e(0x0)

    Begin block 0x222
    prev=[0x216], succ=[0x628]
    =================================
    0x224: v224(0x80a) = CONST 
    0x227: v227(0x628) = CONST 
    0x22a: JUMP v227(0x628)

    Begin block 0x628
    prev=[0x222], succ=[0x80a]
    =================================
    0x629: v629(0x0) = CONST 
    0x62b: v62b = SLOAD v629(0x0)
    0x62c: v62c(0x1) = CONST 
    0x62e: v62e(0x1) = CONST 
    0x630: v630(0xa0) = CONST 
    0x632: v632(0x10000000000000000000000000000000000000000) = SHL v630(0xa0), v62e(0x1)
    0x633: v633(0xffffffffffffffffffffffffffffffffffffffff) = SUB v632(0x10000000000000000000000000000000000000000), v62c(0x1)
    0x634: v634 = AND v633(0xffffffffffffffffffffffffffffffffffffffff), v62b
    0x636: JUMP v224(0x80a)

    Begin block 0x80a
    prev=[0x628], succ=[]
    =================================
    0x80b: v80b(0x40) = CONST 
    0x80e: v80e = MLOAD v80b(0x40)
    0x80f: v80f(0x1) = CONST 
    0x811: v811(0x1) = CONST 
    0x813: v813(0xa0) = CONST 
    0x815: v815(0x10000000000000000000000000000000000000000) = SHL v813(0xa0), v811(0x1)
    0x816: v816(0xffffffffffffffffffffffffffffffffffffffff) = SUB v815(0x10000000000000000000000000000000000000000), v80f(0x1)
    0x819: v819 = AND v634, v816(0xffffffffffffffffffffffffffffffffffffffff)
    0x81b: MSTORE v80e, v819
    0x81c: v81c = MLOAD v80b(0x40)
    0x820: v820(0x0) = SUB v80e, v81c
    0x821: v821(0x20) = CONST 
    0x823: v823(0x20) = ADD v821(0x20), v820(0x0)
    0x825: RETURN v81c, v823(0x20)

}

function admin()() public {
    Begin block 0x22b
    prev=[], succ=[0x233, 0x237]
    =================================
    0x22c: v22c = CALLVALUE 
    0x22e: v22e = ISZERO v22c
    0x22f: v22f(0x237) = CONST 
    0x232: JUMPI v22f(0x237), v22e

    Begin block 0x233
    prev=[0x22b], succ=[]
    =================================
    0x233: v233(0x0) = CONST 
    0x236: REVERT v233(0x0), v233(0x0)

    Begin block 0x237
    prev=[0x22b], succ=[0x637]
    =================================
    0x239: v239(0x845) = CONST 
    0x23c: v23c(0x637) = CONST 
    0x23f: JUMP v23c(0x637)

    Begin block 0x637
    prev=[0x237], succ=[0x845]
    =================================
    0x638: v638(0x2) = CONST 
    0x63a: v63a = SLOAD v638(0x2)
    0x63b: v63b(0x1) = CONST 
    0x63d: v63d(0x1) = CONST 
    0x63f: v63f(0xa0) = CONST 
    0x641: v641(0x10000000000000000000000000000000000000000) = SHL v63f(0xa0), v63d(0x1)
    0x642: v642(0xffffffffffffffffffffffffffffffffffffffff) = SUB v641(0x10000000000000000000000000000000000000000), v63b(0x1)
    0x643: v643 = AND v642(0xffffffffffffffffffffffffffffffffffffffff), v63a
    0x645: JUMP v239(0x845)

    Begin block 0x845
    prev=[0x637], succ=[]
    =================================
    0x846: v846(0x40) = CONST 
    0x849: v849 = MLOAD v846(0x40)
    0x84a: v84a(0x1) = CONST 
    0x84c: v84c(0x1) = CONST 
    0x84e: v84e(0xa0) = CONST 
    0x850: v850(0x10000000000000000000000000000000000000000) = SHL v84e(0xa0), v84c(0x1)
    0x851: v851(0xffffffffffffffffffffffffffffffffffffffff) = SUB v850(0x10000000000000000000000000000000000000000), v84a(0x1)
    0x854: v854 = AND v643, v851(0xffffffffffffffffffffffffffffffffffffffff)
    0x856: MSTORE v849, v854
    0x857: v857 = MLOAD v846(0x40)
    0x85b: v85b(0x0) = SUB v849, v857
    0x85c: v85c(0x20) = CONST 
    0x85e: v85e(0x20) = ADD v85c(0x20), v85b(0x0)
    0x860: RETURN v857, v85e(0x20)

}

function fallback()() public {
    Begin block 0x91
    prev=[], succ=[0xd3, 0xf4]
    =================================
    0x92: v92(0x4) = CONST 
    0x94: v94 = SLOAD v92(0x4)
    0x95: v95(0x40) = CONST 
    0x97: v97 = MLOAD v95(0x40)
    0x98: v98(0x0) = CONST 
    0x9b: v9b(0x1) = CONST 
    0x9d: v9d(0x1) = CONST 
    0x9f: v9f(0xa0) = CONST 
    0xa1: va1(0x10000000000000000000000000000000000000000) = SHL v9f(0xa0), v9d(0x1)
    0xa2: va2(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1(0x10000000000000000000000000000000000000000), v9b(0x1)
    0xa3: va3 = AND va2(0xffffffffffffffffffffffffffffffffffffffff), v94
    0xa7: va7 = CALLDATASIZE 
    0xaf: CALLDATACOPY v97, v98(0x0), va7
    0xb0: vb0(0x40) = CONST 
    0xb2: vb2 = MLOAD vb0(0x40)
    0xb4: vb4 = ADD v97, va7
    0xb7: vb7(0x0) = CONST 
    0xc1: vc1 = SUB vb4, vb2
    0xc4: vc4 = GAS 
    0xc5: vc5 = DELEGATECALL vc4, va3, vb2, vc1, vb2, vb7(0x0)
    0xc9: vc9 = RETURNDATASIZE 
    0xcb: vcb(0x0) = CONST 
    0xce: vce = EQ vc9, vcb(0x0)
    0xcf: vcf(0xf4) = CONST 
    0xd2: JUMPI vcf(0xf4), vce

    Begin block 0xd3
    prev=[0x91], succ=[0xf9]
    =================================
    0xd3: vd3(0x40) = CONST 
    0xd5: vd5 = MLOAD vd3(0x40)
    0xd8: vd8(0x1f) = CONST 
    0xda: vda(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vd8(0x1f)
    0xdb: vdb(0x3f) = CONST 
    0xdd: vdd = RETURNDATASIZE 
    0xde: vde = ADD vdd, vdb(0x3f)
    0xdf: vdf = AND vde, vda(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xe1: ve1 = ADD vd5, vdf
    0xe2: ve2(0x40) = CONST 
    0xe4: MSTORE ve2(0x40), ve1
    0xe5: ve5 = RETURNDATASIZE 
    0xe7: MSTORE vd5, ve5
    0xe8: ve8 = RETURNDATASIZE 
    0xe9: ve9(0x0) = CONST 
    0xeb: veb(0x20) = CONST 
    0xee: vee = ADD vd5, veb(0x20)
    0xef: RETURNDATACOPY vee, ve9(0x0), ve8
    0xf0: vf0(0xf9) = CONST 
    0xf3: JUMP vf0(0xf9)

    Begin block 0xf9
    prev=[0xd3, 0xf4], succ=[0x10d, 0x110]
    =================================
    0xfe: vfe(0x40) = CONST 
    0x100: v100 = MLOAD vfe(0x40)
    0x101: v101 = RETURNDATASIZE 
    0x102: v102(0x0) = CONST 
    0x105: RETURNDATACOPY v100, v102(0x0), v101
    0x108: v108 = ISZERO vc5
    0x109: v109(0x110) = CONST 
    0x10c: JUMPI v109(0x110), v108

    Begin block 0x10d
    prev=[0xf9], succ=[]
    =================================
    0x10d: v10d = RETURNDATASIZE 
    0x10f: RETURN v100, v10d

    Begin block 0x110
    prev=[0xf9], succ=[]
    =================================
    0x111: v111 = RETURNDATASIZE 
    0x113: REVERT v100, v111

    Begin block 0xf4
    prev=[0x91], succ=[0xf9]
    =================================
    0xf5: vf5(0x60) = CONST 

}

