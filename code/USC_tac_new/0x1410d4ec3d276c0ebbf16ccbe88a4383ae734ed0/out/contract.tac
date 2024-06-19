function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x6ca]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x6b6: v6b6(0x6ca) = CONST 
    0x6b7: JUMPI v6b6(0x6ca), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x6cd]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x3659cfe6) = CONST 
    0x3b: v3b = EQ v34, v35(0x3659cfe6)
    0x6b8: v6b8(0x6cd) = CONST 
    0x6b9: JUMPI v6b8(0x6cd), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x6d0, 0x4b]
    =================================
    0x41: v41(0x4e71e0c8) = CONST 
    0x46: v46 = EQ v41(0x4e71e0c8), v34
    0x6ba: v6ba(0x6d0) = CONST 
    0x6bb: JUMPI v6ba(0x6d0), v46

    Begin block 0x6d0
    prev=[0x40], succ=[]
    =================================
    0x6d1: v6d1(0xc3) = CONST 
    0x6d2: CALLPRIVATE v6d1(0xc3)

    Begin block 0x4b
    prev=[0x40], succ=[0x6d3, 0x56]
    =================================
    0x4c: v4c(0x5c60da1b) = CONST 
    0x51: v51 = EQ v4c(0x5c60da1b), v34
    0x6bc: v6bc(0x6d3) = CONST 
    0x6bd: JUMPI v6bc(0x6d3), v51

    Begin block 0x6d3
    prev=[0x4b], succ=[]
    =================================
    0x6d4: v6d4(0xd8) = CONST 
    0x6d5: CALLPRIVATE v6d4(0xd8)

    Begin block 0x56
    prev=[0x4b], succ=[0x6d6, 0x61]
    =================================
    0x57: v57(0x8da5cb5b) = CONST 
    0x5c: v5c = EQ v57(0x8da5cb5b), v34
    0x6be: v6be(0x6d6) = CONST 
    0x6bf: JUMPI v6be(0x6d6), v5c

    Begin block 0x6d6
    prev=[0x56], succ=[]
    =================================
    0x6d7: v6d7(0x109) = CONST 
    0x6d8: CALLPRIVATE v6d7(0x109)

    Begin block 0x61
    prev=[0x56], succ=[0x6d9, 0x6c]
    =================================
    0x62: v62(0x9d36b5c4) = CONST 
    0x67: v67 = EQ v62(0x9d36b5c4), v34
    0x6c0: v6c0(0x6d9) = CONST 
    0x6c1: JUMPI v6c0(0x6d9), v67

    Begin block 0x6d9
    prev=[0x61], succ=[]
    =================================
    0x6da: v6da(0x11e) = CONST 
    0x6db: CALLPRIVATE v6da(0x11e)

    Begin block 0x6c
    prev=[0x61], succ=[0x6dc, 0x77]
    =================================
    0x6d: v6d(0xb199efb5) = CONST 
    0x72: v72 = EQ v6d(0xb199efb5), v34
    0x6c2: v6c2(0x6dc) = CONST 
    0x6c3: JUMPI v6c2(0x6dc), v72

    Begin block 0x6dc
    prev=[0x6c], succ=[]
    =================================
    0x6dd: v6dd(0x133) = CONST 
    0x6de: CALLPRIVATE v6dd(0x133)

    Begin block 0x77
    prev=[0x6c], succ=[0x6df, 0x82]
    =================================
    0x78: v78(0xdd8fee14) = CONST 
    0x7d: v7d = EQ v78(0xdd8fee14), v34
    0x6c4: v6c4(0x6df) = CONST 
    0x6c5: JUMPI v6c4(0x6df), v7d

    Begin block 0x6df
    prev=[0x77], succ=[]
    =================================
    0x6e0: v6e0(0x148) = CONST 
    0x6e1: CALLPRIVATE v6e0(0x148)

    Begin block 0x82
    prev=[0x77], succ=[0x6e2, 0x8d]
    =================================
    0x83: v83(0xe30c3978) = CONST 
    0x88: v88 = EQ v83(0xe30c3978), v34
    0x6c6: v6c6(0x6e2) = CONST 
    0x6c7: JUMPI v6c6(0x6e2), v88

    Begin block 0x6e2
    prev=[0x82], succ=[]
    =================================
    0x6e3: v6e3(0x15d) = CONST 
    0x6e4: CALLPRIVATE v6e3(0x15d)

    Begin block 0x8d
    prev=[0x82], succ=[0x6ca, 0x6e5]
    =================================
    0x8e: v8e(0xf2fde38b) = CONST 
    0x93: v93 = EQ v8e(0xf2fde38b), v34
    0x6c8: v6c8(0x6e5) = CONST 
    0x6c9: JUMPI v6c8(0x6e5), v93

    Begin block 0x6ca
    prev=[0x0, 0x8d], succ=[]
    =================================
    0x6cb: v6cb(0x98) = CONST 
    0x6cc: CALLPRIVATE v6cb(0x98)

    Begin block 0x6e5
    prev=[0x8d], succ=[]
    =================================
    0x6e6: v6e6(0x172) = CONST 
    0x6e7: CALLPRIVATE v6e6(0x172)

    Begin block 0x6cd
    prev=[0xd], succ=[]
    =================================
    0x6ce: v6ce(0xa2) = CONST 
    0x6cf: CALLPRIVATE v6ce(0xa2)

}

function owner()() public {
    Begin block 0x109
    prev=[], succ=[0x111, 0x115]
    =================================
    0x10a: v10a = CALLVALUE 
    0x10c: v10c = ISZERO v10a
    0x10d: v10d(0x115) = CONST 
    0x110: JUMPI v10d(0x115), v10c

    Begin block 0x111
    prev=[0x109], succ=[]
    =================================
    0x111: v111(0x0) = CONST 
    0x114: REVERT v111(0x0), v111(0x0)

    Begin block 0x115
    prev=[0x109], succ=[0x267]
    =================================
    0x117: v117(0x54b) = CONST 
    0x11a: v11a(0x267) = CONST 
    0x11d: JUMP v11a(0x267)

    Begin block 0x267
    prev=[0x115], succ=[0x54b]
    =================================
    0x268: v268(0x0) = CONST 
    0x26a: v26a = SLOAD v268(0x0)
    0x26b: v26b(0x1) = CONST 
    0x26d: v26d(0xa0) = CONST 
    0x26f: v26f(0x2) = CONST 
    0x271: v271(0x10000000000000000000000000000000000000000) = EXP v26f(0x2), v26d(0xa0)
    0x272: v272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v271(0x10000000000000000000000000000000000000000), v26b(0x1)
    0x273: v273 = AND v272(0xffffffffffffffffffffffffffffffffffffffff), v26a
    0x275: JUMP v117(0x54b)

    Begin block 0x54b
    prev=[0x267], succ=[]
    =================================
    0x54c: v54c(0x40) = CONST 
    0x54f: v54f = MLOAD v54c(0x40)
    0x550: v550(0x1) = CONST 
    0x552: v552(0xa0) = CONST 
    0x554: v554(0x2) = CONST 
    0x556: v556(0x10000000000000000000000000000000000000000) = EXP v554(0x2), v552(0xa0)
    0x557: v557(0xffffffffffffffffffffffffffffffffffffffff) = SUB v556(0x10000000000000000000000000000000000000000), v550(0x1)
    0x55a: v55a = AND v273, v557(0xffffffffffffffffffffffffffffffffffffffff)
    0x55c: MSTORE v54f, v55a
    0x55d: v55d = MLOAD v54c(0x40)
    0x561: v561(0x0) = SUB v54f, v55d
    0x562: v562(0x20) = CONST 
    0x564: v564(0x20) = ADD v562(0x20), v561(0x0)
    0x566: RETURN v55d, v564(0x20)

}

function tokenStorage_CD()() public {
    Begin block 0x11e
    prev=[], succ=[0x126, 0x12a]
    =================================
    0x11f: v11f = CALLVALUE 
    0x121: v121 = ISZERO v11f
    0x122: v122(0x12a) = CONST 
    0x125: JUMPI v122(0x12a), v121

    Begin block 0x126
    prev=[0x11e], succ=[]
    =================================
    0x126: v126(0x0) = CONST 
    0x129: REVERT v126(0x0), v126(0x0)

    Begin block 0x12a
    prev=[0x11e], succ=[0x276]
    =================================
    0x12c: v12c(0x586) = CONST 
    0x12f: v12f(0x276) = CONST 
    0x132: JUMP v12f(0x276)

    Begin block 0x276
    prev=[0x12a], succ=[0x586]
    =================================
    0x277: v277(0x4) = CONST 
    0x279: v279 = SLOAD v277(0x4)
    0x27a: v27a(0x1) = CONST 
    0x27c: v27c(0xa0) = CONST 
    0x27e: v27e(0x2) = CONST 
    0x280: v280(0x10000000000000000000000000000000000000000) = EXP v27e(0x2), v27c(0xa0)
    0x281: v281(0xffffffffffffffffffffffffffffffffffffffff) = SUB v280(0x10000000000000000000000000000000000000000), v27a(0x1)
    0x282: v282 = AND v281(0xffffffffffffffffffffffffffffffffffffffff), v279
    0x284: JUMP v12c(0x586)

    Begin block 0x586
    prev=[0x276], succ=[]
    =================================
    0x587: v587(0x40) = CONST 
    0x58a: v58a = MLOAD v587(0x40)
    0x58b: v58b(0x1) = CONST 
    0x58d: v58d(0xa0) = CONST 
    0x58f: v58f(0x2) = CONST 
    0x591: v591(0x10000000000000000000000000000000000000000) = EXP v58f(0x2), v58d(0xa0)
    0x592: v592(0xffffffffffffffffffffffffffffffffffffffff) = SUB v591(0x10000000000000000000000000000000000000000), v58b(0x1)
    0x595: v595 = AND v282, v592(0xffffffffffffffffffffffffffffffffffffffff)
    0x597: MSTORE v58a, v595
    0x598: v598 = MLOAD v587(0x40)
    0x59c: v59c(0x0) = SUB v58a, v598
    0x59d: v59d(0x20) = CONST 
    0x59f: v59f(0x20) = ADD v59d(0x20), v59c(0x0)
    0x5a1: RETURN v598, v59f(0x20)

}

function tokenStorage()() public {
    Begin block 0x133
    prev=[], succ=[0x13b, 0x13f]
    =================================
    0x134: v134 = CALLVALUE 
    0x136: v136 = ISZERO v134
    0x137: v137(0x13f) = CONST 
    0x13a: JUMPI v137(0x13f), v136

    Begin block 0x13b
    prev=[0x133], succ=[]
    =================================
    0x13b: v13b(0x0) = CONST 
    0x13e: REVERT v13b(0x0), v13b(0x0)

    Begin block 0x13f
    prev=[0x133], succ=[0x285]
    =================================
    0x141: v141(0x5c1) = CONST 
    0x144: v144(0x285) = CONST 
    0x147: JUMP v144(0x285)

    Begin block 0x285
    prev=[0x13f], succ=[0x5c1]
    =================================
    0x286: v286(0x2) = CONST 
    0x288: v288 = SLOAD v286(0x2)
    0x289: v289(0x1) = CONST 
    0x28b: v28b(0xa0) = CONST 
    0x28d: v28d(0x2) = CONST 
    0x28f: v28f(0x10000000000000000000000000000000000000000) = EXP v28d(0x2), v28b(0xa0)
    0x290: v290(0xffffffffffffffffffffffffffffffffffffffff) = SUB v28f(0x10000000000000000000000000000000000000000), v289(0x1)
    0x291: v291 = AND v290(0xffffffffffffffffffffffffffffffffffffffff), v288
    0x293: JUMP v141(0x5c1)

    Begin block 0x5c1
    prev=[0x285], succ=[]
    =================================
    0x5c2: v5c2(0x40) = CONST 
    0x5c5: v5c5 = MLOAD v5c2(0x40)
    0x5c6: v5c6(0x1) = CONST 
    0x5c8: v5c8(0xa0) = CONST 
    0x5ca: v5ca(0x2) = CONST 
    0x5cc: v5cc(0x10000000000000000000000000000000000000000) = EXP v5ca(0x2), v5c8(0xa0)
    0x5cd: v5cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5cc(0x10000000000000000000000000000000000000000), v5c6(0x1)
    0x5d0: v5d0 = AND v291, v5cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x5d2: MSTORE v5c5, v5d0
    0x5d3: v5d3 = MLOAD v5c2(0x40)
    0x5d7: v5d7(0x0) = SUB v5c5, v5d3
    0x5d8: v5d8(0x20) = CONST 
    0x5da: v5da(0x20) = ADD v5d8(0x20), v5d7(0x0)
    0x5dc: RETURN v5d3, v5da(0x20)

}

function regulator()() public {
    Begin block 0x148
    prev=[], succ=[0x150, 0x154]
    =================================
    0x149: v149 = CALLVALUE 
    0x14b: v14b = ISZERO v149
    0x14c: v14c(0x154) = CONST 
    0x14f: JUMPI v14c(0x154), v14b

    Begin block 0x150
    prev=[0x148], succ=[]
    =================================
    0x150: v150(0x0) = CONST 
    0x153: REVERT v150(0x0), v150(0x0)

    Begin block 0x154
    prev=[0x148], succ=[0x294]
    =================================
    0x156: v156(0x5fc) = CONST 
    0x159: v159(0x294) = CONST 
    0x15c: JUMP v159(0x294)

    Begin block 0x294
    prev=[0x154], succ=[0x5fc]
    =================================
    0x295: v295(0x3) = CONST 
    0x297: v297 = SLOAD v295(0x3)
    0x298: v298(0x1) = CONST 
    0x29a: v29a(0xa0) = CONST 
    0x29c: v29c(0x2) = CONST 
    0x29e: v29e(0x10000000000000000000000000000000000000000) = EXP v29c(0x2), v29a(0xa0)
    0x29f: v29f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29e(0x10000000000000000000000000000000000000000), v298(0x1)
    0x2a0: v2a0 = AND v29f(0xffffffffffffffffffffffffffffffffffffffff), v297
    0x2a2: JUMP v156(0x5fc)

    Begin block 0x5fc
    prev=[0x294], succ=[]
    =================================
    0x5fd: v5fd(0x40) = CONST 
    0x600: v600 = MLOAD v5fd(0x40)
    0x601: v601(0x1) = CONST 
    0x603: v603(0xa0) = CONST 
    0x605: v605(0x2) = CONST 
    0x607: v607(0x10000000000000000000000000000000000000000) = EXP v605(0x2), v603(0xa0)
    0x608: v608(0xffffffffffffffffffffffffffffffffffffffff) = SUB v607(0x10000000000000000000000000000000000000000), v601(0x1)
    0x60b: v60b = AND v2a0, v608(0xffffffffffffffffffffffffffffffffffffffff)
    0x60d: MSTORE v600, v60b
    0x60e: v60e = MLOAD v5fd(0x40)
    0x612: v612(0x0) = SUB v600, v60e
    0x613: v613(0x20) = CONST 
    0x615: v615(0x20) = ADD v613(0x20), v612(0x0)
    0x617: RETURN v60e, v615(0x20)

}

function pendingOwner()() public {
    Begin block 0x15d
    prev=[], succ=[0x165, 0x169]
    =================================
    0x15e: v15e = CALLVALUE 
    0x160: v160 = ISZERO v15e
    0x161: v161(0x169) = CONST 
    0x164: JUMPI v161(0x169), v160

    Begin block 0x165
    prev=[0x15d], succ=[]
    =================================
    0x165: v165(0x0) = CONST 
    0x168: REVERT v165(0x0), v165(0x0)

    Begin block 0x169
    prev=[0x15d], succ=[0x2a3]
    =================================
    0x16b: v16b(0x637) = CONST 
    0x16e: v16e(0x2a3) = CONST 
    0x171: JUMP v16e(0x2a3)

    Begin block 0x2a3
    prev=[0x169], succ=[0x637]
    =================================
    0x2a4: v2a4(0x1) = CONST 
    0x2a6: v2a6 = SLOAD v2a4(0x1)
    0x2a7: v2a7(0x1) = CONST 
    0x2a9: v2a9(0xa0) = CONST 
    0x2ab: v2ab(0x2) = CONST 
    0x2ad: v2ad(0x10000000000000000000000000000000000000000) = EXP v2ab(0x2), v2a9(0xa0)
    0x2ae: v2ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ad(0x10000000000000000000000000000000000000000), v2a7(0x1)
    0x2af: v2af = AND v2ae(0xffffffffffffffffffffffffffffffffffffffff), v2a6
    0x2b1: JUMP v16b(0x637)

    Begin block 0x637
    prev=[0x2a3], succ=[]
    =================================
    0x638: v638(0x40) = CONST 
    0x63b: v63b = MLOAD v638(0x40)
    0x63c: v63c(0x1) = CONST 
    0x63e: v63e(0xa0) = CONST 
    0x640: v640(0x2) = CONST 
    0x642: v642(0x10000000000000000000000000000000000000000) = EXP v640(0x2), v63e(0xa0)
    0x643: v643(0xffffffffffffffffffffffffffffffffffffffff) = SUB v642(0x10000000000000000000000000000000000000000), v63c(0x1)
    0x646: v646 = AND v2af, v643(0xffffffffffffffffffffffffffffffffffffffff)
    0x648: MSTORE v63b, v646
    0x649: v649 = MLOAD v638(0x40)
    0x64d: v64d(0x0) = SUB v63b, v649
    0x64e: v64e(0x20) = CONST 
    0x650: v650(0x20) = ADD v64e(0x20), v64d(0x0)
    0x652: RETURN v649, v650(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x172
    prev=[], succ=[0x17a, 0x17e]
    =================================
    0x173: v173 = CALLVALUE 
    0x175: v175 = ISZERO v173
    0x176: v176(0x17e) = CONST 
    0x179: JUMPI v176(0x17e), v175

    Begin block 0x17a
    prev=[0x172], succ=[]
    =================================
    0x17a: v17a(0x0) = CONST 
    0x17d: REVERT v17a(0x0), v17a(0x0)

    Begin block 0x17e
    prev=[0x172], succ=[0x2b2]
    =================================
    0x180: v180(0x672) = CONST 
    0x183: v183(0x1) = CONST 
    0x185: v185(0xa0) = CONST 
    0x187: v187(0x2) = CONST 
    0x189: v189(0x10000000000000000000000000000000000000000) = EXP v187(0x2), v185(0xa0)
    0x18a: v18a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v189(0x10000000000000000000000000000000000000000), v183(0x1)
    0x18b: v18b(0x4) = CONST 
    0x18d: v18d = CALLDATALOAD v18b(0x4)
    0x18e: v18e = AND v18d, v18a(0xffffffffffffffffffffffffffffffffffffffff)
    0x18f: v18f(0x2b2) = CONST 
    0x192: JUMP v18f(0x2b2)

    Begin block 0x2b2
    prev=[0x17e], succ=[0x2c5, 0x2c9]
    =================================
    0x2b3: v2b3(0x0) = CONST 
    0x2b5: v2b5 = SLOAD v2b3(0x0)
    0x2b6: v2b6(0x1) = CONST 
    0x2b8: v2b8(0xa0) = CONST 
    0x2ba: v2ba(0x2) = CONST 
    0x2bc: v2bc(0x10000000000000000000000000000000000000000) = EXP v2ba(0x2), v2b8(0xa0)
    0x2bd: v2bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2bc(0x10000000000000000000000000000000000000000), v2b6(0x1)
    0x2be: v2be = AND v2bd(0xffffffffffffffffffffffffffffffffffffffff), v2b5
    0x2bf: v2bf = CALLER 
    0x2c0: v2c0 = EQ v2bf, v2be
    0x2c1: v2c1(0x2c9) = CONST 
    0x2c4: JUMPI v2c1(0x2c9), v2c0

    Begin block 0x2c5
    prev=[0x2b2], succ=[]
    =================================
    0x2c5: v2c5(0x0) = CONST 
    0x2c8: REVERT v2c5(0x0), v2c5(0x0)

    Begin block 0x2c9
    prev=[0x2b2], succ=[0x2da, 0x2de]
    =================================
    0x2ca: v2ca(0x1) = CONST 
    0x2cc: v2cc(0xa0) = CONST 
    0x2ce: v2ce(0x2) = CONST 
    0x2d0: v2d0(0x10000000000000000000000000000000000000000) = EXP v2ce(0x2), v2cc(0xa0)
    0x2d1: v2d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d0(0x10000000000000000000000000000000000000000), v2ca(0x1)
    0x2d3: v2d3 = AND v18e, v2d1(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d4: v2d4 = ISZERO v2d3
    0x2d5: v2d5 = ISZERO v2d4
    0x2d6: v2d6(0x2de) = CONST 
    0x2d9: JUMPI v2d6(0x2de), v2d5

    Begin block 0x2da
    prev=[0x2c9], succ=[]
    =================================
    0x2da: v2da(0x0) = CONST 
    0x2dd: REVERT v2da(0x0), v2da(0x0)

    Begin block 0x2de
    prev=[0x2c9], succ=[0x672]
    =================================
    0x2df: v2df(0x1) = CONST 
    0x2e2: v2e2 = SLOAD v2df(0x1)
    0x2e3: v2e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f8: v2f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x2f9: v2f9 = AND v2f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2e2
    0x2fa: v2fa(0x1) = CONST 
    0x2fc: v2fc(0xa0) = CONST 
    0x2fe: v2fe(0x2) = CONST 
    0x300: v300(0x10000000000000000000000000000000000000000) = EXP v2fe(0x2), v2fc(0xa0)
    0x301: v301(0xffffffffffffffffffffffffffffffffffffffff) = SUB v300(0x10000000000000000000000000000000000000000), v2fa(0x1)
    0x305: v305 = AND v301(0xffffffffffffffffffffffffffffffffffffffff), v18e
    0x309: v309 = OR v305, v2f9
    0x30b: SSTORE v2df(0x1), v309
    0x30c: JUMP v180(0x672)

    Begin block 0x672
    prev=[0x2de], succ=[]
    =================================
    0x673: STOP 

}

function fallback()() public {
    Begin block 0x98
    prev=[], succ=[0x193]
    =================================
    0x99: v99(0x4ad) = CONST 
    0x9c: v9c(0x193) = CONST 
    0x9f: JUMP v9c(0x193)

    Begin block 0x193
    prev=[0x98], succ=[0x693B0x193]
    =================================
    0x194: v194(0x19b) = CONST 
    0x197: v197(0x693) = CONST 
    0x19a: JUMP v197(0x693), v194(0x19b)

    Begin block 0x693B0x193
    prev=[0x193], succ=[0x19b]
    =================================
    0x694S0x193: JUMP v194(0x19b)

    Begin block 0x19b
    prev=[0x693B0x193], succ=[0x30dB0x19b]
    =================================
    0x19c: v19c(0x6b4) = CONST 
    0x19f: v19f(0x1a6) = CONST 
    0x1a2: v1a2(0x30d) = CONST 
    0x1a5: JUMP v1a2(0x30d)

    Begin block 0x30dB0x19b
    prev=[0x19b], succ=[0x1a6]
    =================================
    0x30eS0x19b: v30eV19b(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x32fS0x19b: v32fV19b = SLOAD v30eV19b(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x331S0x19b: JUMP v19f(0x1a6)

    Begin block 0x1a6
    prev=[0x30dB0x19b], succ=[0x332]
    =================================
    0x1a7: v1a7(0x332) = CONST 
    0x1aa: JUMP v1a7(0x332)

    Begin block 0x332
    prev=[0x1a6], succ=[0x34d, 0x351]
    =================================
    0x333: v333 = CALLDATASIZE 
    0x334: v334(0x0) = CONST 
    0x337: CALLDATACOPY v334(0x0), v334(0x0), v333
    0x338: v338(0x0) = CONST 
    0x33b: v33b = CALLDATASIZE 
    0x33c: v33c(0x0) = CONST 
    0x33f: v33f = GAS 
    0x340: v340 = DELEGATECALL v33f, v32fV19b, v33c(0x0), v33b, v338(0x0), v338(0x0)
    0x341: v341 = RETURNDATASIZE 
    0x342: v342(0x0) = CONST 
    0x345: RETURNDATACOPY v342(0x0), v342(0x0), v341
    0x348: v348 = ISZERO v340
    0x349: v349(0x351) = CONST 
    0x34c: JUMPI v349(0x351), v348

    Begin block 0x34d
    prev=[0x332], succ=[]
    =================================
    0x34d: v34d = RETURNDATASIZE 
    0x34e: v34e(0x0) = CONST 
    0x350: RETURN v34e(0x0), v34d

    Begin block 0x351
    prev=[0x332], succ=[]
    =================================
    0x352: v352 = RETURNDATASIZE 
    0x353: v353(0x0) = CONST 
    0x355: REVERT v353(0x0), v352

}

function upgradeTo(address)() public {
    Begin block 0xa2
    prev=[], succ=[0xaa, 0xae]
    =================================
    0xa3: va3 = CALLVALUE 
    0xa5: va5 = ISZERO va3
    0xa6: va6(0xae) = CONST 
    0xa9: JUMPI va6(0xae), va5

    Begin block 0xaa
    prev=[0xa2], succ=[]
    =================================
    0xaa: vaa(0x0) = CONST 
    0xad: REVERT vaa(0x0), vaa(0x0)

    Begin block 0xae
    prev=[0xa2], succ=[0x1adB0xae]
    =================================
    0xb0: vb0(0x4ce) = CONST 
    0xb3: vb3(0x1) = CONST 
    0xb5: vb5(0xa0) = CONST 
    0xb7: vb7(0x2) = CONST 
    0xb9: vb9(0x10000000000000000000000000000000000000000) = EXP vb7(0x2), vb5(0xa0)
    0xba: vba(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb9(0x10000000000000000000000000000000000000000), vb3(0x1)
    0xbb: vbb(0x4) = CONST 
    0xbd: vbd = CALLDATALOAD vbb(0x4)
    0xbe: vbe = AND vbd, vba(0xffffffffffffffffffffffffffffffffffffffff)
    0xbf: vbf(0x1ad) = CONST 
    0xc2: JUMP vbf(0x1ad), vbe, vb0(0x4ce)

    Begin block 0x1adB0xae
    prev=[0xae], succ=[0x1c0B0xae, 0x1c4B0xae]
    =================================
    0x1aeS0xae: v1aeVae(0x0) = CONST 
    0x1b0S0xae: v1b0Vae = SLOAD v1aeVae(0x0)
    0x1b1S0xae: v1b1Vae(0x1) = CONST 
    0x1b3S0xae: v1b3Vae(0xa0) = CONST 
    0x1b5S0xae: v1b5Vae(0x2) = CONST 
    0x1b7S0xae: v1b7Vae(0x10000000000000000000000000000000000000000) = EXP v1b5Vae(0x2), v1b3Vae(0xa0)
    0x1b8S0xae: v1b8Vae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b7Vae(0x10000000000000000000000000000000000000000), v1b1Vae(0x1)
    0x1b9S0xae: v1b9Vae = AND v1b8Vae(0xffffffffffffffffffffffffffffffffffffffff), v1b0Vae
    0x1baS0xae: v1baVae = CALLER 
    0x1bbS0xae: v1bbVae = EQ v1baVae, v1b9Vae
    0x1bcS0xae: v1bcVae(0x1c4) = CONST 
    0x1bfS0xae: JUMPI v1bcVae(0x1c4), v1bbVae

    Begin block 0x1c0B0xae
    prev=[0x1adB0xae], succ=[]
    =================================
    0x1c0S0xae: v1c0Vae(0x0) = CONST 
    0x1c3S0xae: REVERT v1c0Vae(0x0), v1c0Vae(0x0)

    Begin block 0x1c4B0xae
    prev=[0x1adB0xae], succ=[0x356B0xae]
    =================================
    0x1c5S0xae: v1c5Vae(0x1cd) = CONST 
    0x1c9S0xae: v1c9Vae(0x356) = CONST 
    0x1ccS0xae: JUMP v1c9Vae(0x356)

    Begin block 0x356B0xae
    prev=[0x1c4B0xae], succ=[0x39eB0xae]
    =================================
    0x357S0xae: v357Vae(0x35f) = CONST 
    0x35bS0xae: v35bVae(0x39e) = CONST 
    0x35eS0xae: JUMP v35bVae(0x39e)

    Begin block 0x39eB0xae
    prev=[0x356B0xae], succ=[0x461B0xae]
    =================================
    0x39fS0xae: v39fVae(0x0) = CONST 
    0x3a1S0xae: v3a1Vae(0x3a9) = CONST 
    0x3a5S0xae: v3a5Vae(0x461) = CONST 
    0x3a8S0xae: JUMP v3a5Vae(0x461)

    Begin block 0x461B0xae
    prev=[0x39eB0xae], succ=[0x3a9B0xae]
    =================================
    0x462S0xae: v462Vae(0x0) = CONST 
    0x465S0xae: v465Vae = EXTCODESIZE vbe
    0x466S0xae: v466Vae = GT v465Vae, v462Vae(0x0)
    0x468S0xae: JUMP v3a1Vae(0x3a9)

    Begin block 0x3a9B0xae
    prev=[0x461B0xae], succ=[0x3b0B0xae, 0x43cB0xae]
    =================================
    0x3aaS0xae: v3aaVae = ISZERO v466Vae
    0x3abS0xae: v3abVae = ISZERO v3aaVae
    0x3acS0xae: v3acVae(0x43c) = CONST 
    0x3afS0xae: JUMPI v3acVae(0x43c), v3abVae

    Begin block 0x3b0B0xae
    prev=[0x3a9B0xae], succ=[]
    =================================
    0x3b0S0xae: v3b0Vae(0x40) = CONST 
    0x3b3S0xae: v3b3Vae = MLOAD v3b0Vae(0x40)
    0x3b4S0xae: v3b4Vae(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3d6S0xae: MSTORE v3b3Vae, v3b4Vae(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3d7S0xae: v3d7Vae(0x20) = CONST 
    0x3d9S0xae: v3d9Vae(0x4) = CONST 
    0x3dcS0xae: v3dcVae = ADD v3b3Vae, v3d9Vae(0x4)
    0x3ddS0xae: MSTORE v3dcVae, v3d7Vae(0x20)
    0x3deS0xae: v3deVae(0x3b) = CONST 
    0x3e0S0xae: v3e0Vae(0x24) = CONST 
    0x3e3S0xae: v3e3Vae = ADD v3b3Vae, v3e0Vae(0x24)
    0x3e4S0xae: MSTORE v3e3Vae, v3deVae(0x3b)
    0x3e5S0xae: v3e5Vae(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f) = CONST 
    0x406S0xae: v406Vae(0x44) = CONST 
    0x409S0xae: v409Vae = ADD v3b3Vae, v406Vae(0x44)
    0x40aS0xae: MSTORE v409Vae, v3e5Vae(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f)
    0x40bS0xae: v40bVae(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000) = CONST 
    0x42cS0xae: v42cVae(0x64) = CONST 
    0x42fS0xae: v42fVae = ADD v3b3Vae, v42cVae(0x64)
    0x430S0xae: MSTORE v42fVae, v40bVae(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000)
    0x432S0xae: v432Vae = MLOAD v3b0Vae(0x40)
    0x436S0xae: v436Vae(0x0) = SUB v3b3Vae, v432Vae
    0x437S0xae: v437Vae(0x84) = CONST 
    0x439S0xae: v439Vae(0x84) = ADD v437Vae(0x84), v436Vae(0x0)
    0x43bS0xae: REVERT v432Vae, v439Vae(0x84)

    Begin block 0x43cB0xae
    prev=[0x3a9B0xae], succ=[0x35fB0xae]
    =================================
    0x43eS0xae: v43eVae(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x45fS0xae: SSTORE v43eVae(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), vbe
    0x460S0xae: JUMP v357Vae(0x35f)

    Begin block 0x35fB0xae
    prev=[0x43cB0xae], succ=[0x1cdB0xae]
    =================================
    0x360S0xae: v360Vae(0x40) = CONST 
    0x363S0xae: v363Vae = MLOAD v360Vae(0x40)
    0x364S0xae: v364Vae(0x1) = CONST 
    0x366S0xae: v366Vae(0xa0) = CONST 
    0x368S0xae: v368Vae(0x2) = CONST 
    0x36aS0xae: v36aVae(0x10000000000000000000000000000000000000000) = EXP v368Vae(0x2), v366Vae(0xa0)
    0x36bS0xae: v36bVae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v36aVae(0x10000000000000000000000000000000000000000), v364Vae(0x1)
    0x36dS0xae: v36dVae = AND vbe, v36bVae(0xffffffffffffffffffffffffffffffffffffffff)
    0x36fS0xae: MSTORE v363Vae, v36dVae
    0x371S0xae: v371Vae = MLOAD v360Vae(0x40)
    0x372S0xae: v372Vae(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x396S0xae: v396Vae(0x0) = SUB v363Vae, v371Vae
    0x397S0xae: v397Vae(0x20) = CONST 
    0x399S0xae: v399Vae(0x20) = ADD v397Vae(0x20), v396Vae(0x0)
    0x39bS0xae: LOG1 v371Vae, v399Vae(0x20), v372Vae(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b)
    0x39dS0xae: JUMP v1c5Vae(0x1cd)

    Begin block 0x1cdB0xae
    prev=[0x35fB0xae], succ=[0x4ce]
    =================================
    0x1cfS0xae: JUMP vb0(0x4ce)

    Begin block 0x4ce
    prev=[0x1cdB0xae], succ=[]
    =================================
    0x4cf: STOP 

}

function claimOwnership()() public {
    Begin block 0xc3
    prev=[], succ=[0xcb, 0xcf]
    =================================
    0xc4: vc4 = CALLVALUE 
    0xc6: vc6 = ISZERO vc4
    0xc7: vc7(0xcf) = CONST 
    0xca: JUMPI vc7(0xcf), vc6

    Begin block 0xcb
    prev=[0xc3], succ=[]
    =================================
    0xcb: vcb(0x0) = CONST 
    0xce: REVERT vcb(0x0), vcb(0x0)

    Begin block 0xcf
    prev=[0xc3], succ=[0x1d0]
    =================================
    0xd1: vd1(0x4ef) = CONST 
    0xd4: vd4(0x1d0) = CONST 
    0xd7: JUMP vd4(0x1d0)

    Begin block 0x1d0
    prev=[0xcf], succ=[0x1e3, 0x1e7]
    =================================
    0x1d1: v1d1(0x1) = CONST 
    0x1d3: v1d3 = SLOAD v1d1(0x1)
    0x1d4: v1d4(0x1) = CONST 
    0x1d6: v1d6(0xa0) = CONST 
    0x1d8: v1d8(0x2) = CONST 
    0x1da: v1da(0x10000000000000000000000000000000000000000) = EXP v1d8(0x2), v1d6(0xa0)
    0x1db: v1db(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1da(0x10000000000000000000000000000000000000000), v1d4(0x1)
    0x1dc: v1dc = AND v1db(0xffffffffffffffffffffffffffffffffffffffff), v1d3
    0x1dd: v1dd = CALLER 
    0x1de: v1de = EQ v1dd, v1dc
    0x1df: v1df(0x1e7) = CONST 
    0x1e2: JUMPI v1df(0x1e7), v1de

    Begin block 0x1e3
    prev=[0x1d0], succ=[]
    =================================
    0x1e3: v1e3(0x0) = CONST 
    0x1e6: REVERT v1e3(0x0), v1e3(0x0)

    Begin block 0x1e7
    prev=[0x1d0], succ=[0x4ef]
    =================================
    0x1e8: v1e8(0x1) = CONST 
    0x1ea: v1ea = SLOAD v1e8(0x1)
    0x1eb: v1eb(0x0) = CONST 
    0x1ee: v1ee = SLOAD v1eb(0x0)
    0x1ef: v1ef(0x40) = CONST 
    0x1f1: v1f1 = MLOAD v1ef(0x40)
    0x1f2: v1f2(0x1) = CONST 
    0x1f4: v1f4(0xa0) = CONST 
    0x1f6: v1f6(0x2) = CONST 
    0x1f8: v1f8(0x10000000000000000000000000000000000000000) = EXP v1f6(0x2), v1f4(0xa0)
    0x1f9: v1f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f8(0x10000000000000000000000000000000000000000), v1f2(0x1)
    0x1fc: v1fc = AND v1f9(0xffffffffffffffffffffffffffffffffffffffff), v1ea
    0x200: v200 = AND v1ee, v1f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x202: v202(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x224: LOG3 v1f1, v1eb(0x0), v202(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v200, v1fc
    0x225: v225(0x1) = CONST 
    0x228: v228 = SLOAD v225(0x1)
    0x229: v229(0x0) = CONST 
    0x22c: v22c = SLOAD v229(0x0)
    0x22d: v22d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x242: v242(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v22d(0xffffffffffffffffffffffffffffffffffffffff)
    0x245: v245 = AND v242(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v22c
    0x246: v246(0x1) = CONST 
    0x248: v248(0xa0) = CONST 
    0x24a: v24a(0x2) = CONST 
    0x24c: v24c(0x10000000000000000000000000000000000000000) = EXP v24a(0x2), v248(0xa0)
    0x24d: v24d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24c(0x10000000000000000000000000000000000000000), v246(0x1)
    0x24f: v24f = AND v228, v24d(0xffffffffffffffffffffffffffffffffffffffff)
    0x250: v250 = OR v24f, v245
    0x253: SSTORE v229(0x0), v250
    0x254: v254 = AND v242(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v228
    0x256: SSTORE v225(0x1), v254
    0x257: JUMP vd1(0x4ef)

    Begin block 0x4ef
    prev=[0x1e7], succ=[]
    =================================
    0x4f0: STOP 

}

function implementation()() public {
    Begin block 0xd8
    prev=[], succ=[0xe0, 0xe4]
    =================================
    0xd9: vd9 = CALLVALUE 
    0xdb: vdb = ISZERO vd9
    0xdc: vdc(0xe4) = CONST 
    0xdf: JUMPI vdc(0xe4), vdb

    Begin block 0xe0
    prev=[0xd8], succ=[]
    =================================
    0xe0: ve0(0x0) = CONST 
    0xe3: REVERT ve0(0x0), ve0(0x0)

    Begin block 0xe4
    prev=[0xd8], succ=[0x258B0xe4]
    =================================
    0xe6: ve6(0x510) = CONST 
    0xe9: ve9(0x258) = CONST 
    0xec: JUMP ve9(0x258)

    Begin block 0x258B0xe4
    prev=[0xe4], succ=[0x30dB0x258B0xe4]
    =================================
    0x259S0xe4: v259Ve4(0x0) = CONST 
    0x25bS0xe4: v25bVe4(0x262) = CONST 
    0x25eS0xe4: v25eVe4(0x30d) = CONST 
    0x261S0xe4: JUMP v25eVe4(0x30d)

    Begin block 0x30dB0x258B0xe4
    prev=[0x258B0xe4], succ=[0x262B0xe4]
    =================================
    0x30eS0x258S0xe4: v30eV258Ve4(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x32fS0x258S0xe4: v32fV258Ve4 = SLOAD v30eV258Ve4(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x331S0x258S0xe4: JUMP v25bVe4(0x262)

    Begin block 0x262B0xe4
    prev=[0x30dB0x258B0xe4], succ=[0x510]
    =================================
    0x266S0xe4: JUMP ve6(0x510)

    Begin block 0x510
    prev=[0x262B0xe4], succ=[]
    =================================
    0x511: v511(0x40) = CONST 
    0x514: v514 = MLOAD v511(0x40)
    0x515: v515(0x1) = CONST 
    0x517: v517(0xa0) = CONST 
    0x519: v519(0x2) = CONST 
    0x51b: v51b(0x10000000000000000000000000000000000000000) = EXP v519(0x2), v517(0xa0)
    0x51c: v51c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51b(0x10000000000000000000000000000000000000000), v515(0x1)
    0x51f: v51f = AND v32fV258Ve4, v51c(0xffffffffffffffffffffffffffffffffffffffff)
    0x521: MSTORE v514, v51f
    0x522: v522 = MLOAD v511(0x40)
    0x526: v526(0x0) = SUB v514, v522
    0x527: v527(0x20) = CONST 
    0x529: v529(0x20) = ADD v527(0x20), v526(0x0)
    0x52b: RETURN v522, v529(0x20)

}

