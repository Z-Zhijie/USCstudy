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
    prev=[0x0], succ=[0x1a, 0xde4]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0xdb0: vdb0(0xde4) = CONST 
    0xdb1: JUMPI vdb0(0xde4), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x66, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x8129fc1c) = CONST 
    0x26: v26 = GT v21(0x8129fc1c), v1f
    0x27: v27(0x66) = CONST 
    0x2a: JUMPI v27(0x66), v26

    Begin block 0x66
    prev=[0x1a], succ=[0xdc6, 0x72]
    =================================
    0x68: v68(0x5a7cdd6) = CONST 
    0x6d: v6d = EQ v68(0x5a7cdd6), v1f
    0xdbc: vdbc(0xdc6) = CONST 
    0xdbd: JUMPI vdbc(0xdc6), v6d

    Begin block 0xdc6
    prev=[0x66], succ=[]
    =================================
    0xdc7: vdc7(0xa3) = CONST 
    0xdc8: CALLPRIVATE vdc7(0xa3)

    Begin block 0x72
    prev=[0x66], succ=[0xdc9, 0x7d]
    =================================
    0x73: v73(0x18f87df0) = CONST 
    0x78: v78 = EQ v73(0x18f87df0), v1f
    0xdbe: vdbe(0xdc9) = CONST 
    0xdbf: JUMPI vdbe(0xdc9), v78

    Begin block 0xdc9
    prev=[0x72], succ=[]
    =================================
    0xdca: vdca(0xc2) = CONST 
    0xdcb: CALLPRIVATE vdca(0xc2)

    Begin block 0x7d
    prev=[0x72], succ=[0xdcc, 0x88]
    =================================
    0x7e: v7e(0x71f2584c) = CONST 
    0x83: v83 = EQ v7e(0x71f2584c), v1f
    0xdc0: vdc0(0xdcc) = CONST 
    0xdc1: JUMPI vdc0(0xdcc), v83

    Begin block 0xdcc
    prev=[0x7d], succ=[]
    =================================
    0xdcd: vdcd(0xe5) = CONST 
    0xdce: CALLPRIVATE vdcd(0xe5)

    Begin block 0x88
    prev=[0x7d], succ=[0xdcf, 0x93]
    =================================
    0x89: v89(0x73252494) = CONST 
    0x8e: v8e = EQ v89(0x73252494), v1f
    0xdc2: vdc2(0xdcf) = CONST 
    0xdc3: JUMPI vdc2(0xdcf), v8e

    Begin block 0xdcf
    prev=[0x88], succ=[]
    =================================
    0xdd0: vdd0(0x109) = CONST 
    0xdd1: CALLPRIVATE vdd0(0x109)

    Begin block 0x93
    prev=[0x88], succ=[0xdd2, 0x9e]
    =================================
    0x94: v94(0x7ce87b43) = CONST 
    0x99: v99 = EQ v94(0x7ce87b43), v1f
    0xdc4: vdc4(0xdd2) = CONST 
    0xdc5: JUMPI vdc4(0xdd2), v99

    Begin block 0xdd2
    prev=[0x93], succ=[]
    =================================
    0xdd3: vdd3(0x111) = CONST 
    0xdd4: CALLPRIVATE vdd3(0x111)

    Begin block 0x9e
    prev=[0x93], succ=[]
    =================================
    0x9f: v9f(0x0) = CONST 
    0xa2: REVERT v9f(0x0), v9f(0x0)

    Begin block 0x2b
    prev=[0x1a], succ=[0x36, 0xdd5]
    =================================
    0x2c: v2c(0x8129fc1c) = CONST 
    0x31: v31 = EQ v2c(0x8129fc1c), v1f
    0xdb2: vdb2(0xdd5) = CONST 
    0xdb3: JUMPI vdb2(0xdd5), v31

    Begin block 0x36
    prev=[0x2b], succ=[0xdd8, 0x41]
    =================================
    0x37: v37(0xa01893bf) = CONST 
    0x3c: v3c = EQ v37(0xa01893bf), v1f
    0xdb4: vdb4(0xdd8) = CONST 
    0xdb5: JUMPI vdb4(0xdd8), v3c

    Begin block 0xdd8
    prev=[0x36], succ=[]
    =================================
    0xdd9: vdd9(0x133) = CONST 
    0xdda: CALLPRIVATE vdd9(0x133)

    Begin block 0x41
    prev=[0x36], succ=[0xddb, 0x4c]
    =================================
    0x42: v42(0xcfc16254) = CONST 
    0x47: v47 = EQ v42(0xcfc16254), v1f
    0xdb6: vdb6(0xddb) = CONST 
    0xdb7: JUMPI vdb6(0xddb), v47

    Begin block 0xddb
    prev=[0x41], succ=[]
    =================================
    0xddc: vddc(0x179) = CONST 
    0xddd: CALLPRIVATE vddc(0x179)

    Begin block 0x4c
    prev=[0x41], succ=[0xdde, 0x57]
    =================================
    0x4d: v4d(0xec8d844f) = CONST 
    0x52: v52 = EQ v4d(0xec8d844f), v1f
    0xdb8: vdb8(0xdde) = CONST 
    0xdb9: JUMPI vdb8(0xdde), v52

    Begin block 0xdde
    prev=[0x4c], succ=[]
    =================================
    0xddf: vddf(0x19f) = CONST 
    0xde0: CALLPRIVATE vddf(0x19f)

    Begin block 0x57
    prev=[0x4c], succ=[0x62, 0xde1]
    =================================
    0x58: v58(0xfc0c546a) = CONST 
    0x5d: v5d = EQ v58(0xfc0c546a), v1f
    0xdba: vdba(0xde1) = CONST 
    0xdbb: JUMPI vdba(0xde1), v5d

    Begin block 0x62
    prev=[0x57], succ=[0xb80]
    =================================
    0x62: v62(0xb80) = CONST 
    0x65: JUMP v62(0xb80)

    Begin block 0xb80
    prev=[0x62], succ=[]
    =================================
    0xb81: vb81(0x0) = CONST 
    0xb84: REVERT vb81(0x0), vb81(0x0)

    Begin block 0xde1
    prev=[0x57], succ=[]
    =================================
    0xde2: vde2(0x1c5) = CONST 
    0xde3: CALLPRIVATE vde2(0x1c5)

    Begin block 0xdd5
    prev=[0x2b], succ=[]
    =================================
    0xdd6: vdd6(0x12b) = CONST 
    0xdd7: CALLPRIVATE vdd6(0x12b)

    Begin block 0xde4
    prev=[0x10], succ=[]
    =================================
    0xde5: vde5(0xb5c) = CONST 
    0xde6: CALLPRIVATE vde5(0xb5c)

}

function getGovernanceAddress()() public {
    Begin block 0x109
    prev=[], succ=[0x454]
    =================================
    0x10a: v10a(0xc21) = CONST 
    0x10d: v10d(0x454) = CONST 
    0x110: JUMP v10d(0x454)

    Begin block 0x454
    prev=[0x109], succ=[0x45e]
    =================================
    0x455: v455(0x0) = CONST 
    0x457: v457(0x45e) = CONST 
    0x45a: v45a(0x87f) = CONST 
    0x45d: CALLPRIVATE v45a(0x87f), v457(0x45e)

    Begin block 0x45e
    prev=[0x454], succ=[0xc21]
    =================================
    0x460: v460(0x33) = CONST 
    0x462: v462 = SLOAD v460(0x33)
    0x463: v463(0x100) = CONST 
    0x467: v467 = DIV v462, v463(0x100)
    0x468: v468(0x1) = CONST 
    0x46a: v46a(0x1) = CONST 
    0x46c: v46c(0xa0) = CONST 
    0x46e: v46e(0x10000000000000000000000000000000000000000) = SHL v46c(0xa0), v46a(0x1)
    0x46f: v46f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46e(0x10000000000000000000000000000000000000000), v468(0x1)
    0x470: v470 = AND v46f(0xffffffffffffffffffffffffffffffffffffffff), v467
    0x472: JUMP v10a(0xc21)

    Begin block 0xc21
    prev=[0x45e], succ=[]
    =================================
    0xc22: vc22(0x40) = CONST 
    0xc25: vc25 = MLOAD vc22(0x40)
    0xc26: vc26(0x1) = CONST 
    0xc28: vc28(0x1) = CONST 
    0xc2a: vc2a(0xa0) = CONST 
    0xc2c: vc2c(0x10000000000000000000000000000000000000000) = SHL vc2a(0xa0), vc28(0x1)
    0xc2d: vc2d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc2c(0x10000000000000000000000000000000000000000), vc26(0x1)
    0xc30: vc30 = AND v470, vc2d(0xffffffffffffffffffffffffffffffffffffffff)
    0xc32: MSTORE vc25, vc30
    0xc33: vc33 = MLOAD vc22(0x40)
    0xc37: vc37(0x0) = SUB vc25, vc33
    0xc38: vc38(0x20) = CONST 
    0xc3a: vc3a(0x20) = ADD vc38(0x20), vc37(0x0)
    0xc3c: RETURN vc33, vc3a(0x20)

}

function getRecipientAddress()() public {
    Begin block 0x111
    prev=[], succ=[0x473]
    =================================
    0x112: v112(0x119) = CONST 
    0x115: v115(0x473) = CONST 
    0x118: JUMP v115(0x473)

    Begin block 0x473
    prev=[0x111], succ=[0x47d]
    =================================
    0x474: v474(0x0) = CONST 
    0x476: v476(0x47d) = CONST 
    0x479: v479(0x87f) = CONST 
    0x47c: CALLPRIVATE v479(0x87f), v476(0x47d)

    Begin block 0x47d
    prev=[0x473], succ=[0x119]
    =================================
    0x47f: v47f(0x36) = CONST 
    0x481: v481 = SLOAD v47f(0x36)
    0x483: JUMP v112(0x119)

    Begin block 0x119
    prev=[0x47d], succ=[]
    =================================
    0x11a: v11a(0x40) = CONST 
    0x11d: v11d = MLOAD v11a(0x40)
    0x120: MSTORE v11d, v481
    0x121: v121 = MLOAD v11a(0x40)
    0x125: v125(0x0) = SUB v11d, v121
    0x126: v126(0x20) = CONST 
    0x128: v128(0x20) = ADD v126(0x20), v125(0x0)
    0x12a: RETURN v121, v128(0x20)

}

function initialize()() public {
    Begin block 0x12b
    prev=[], succ=[0xc5c]
    =================================
    0x12c: v12c(0xc5c) = CONST 
    0x12f: v12f(0x484) = CONST 
    0x132: CALLPRIVATE v12f(0x484), v12c(0xc5c)

    Begin block 0xc5c
    prev=[0x12b], succ=[]
    =================================
    0xc5d: STOP 

}

function initialize(address,address,address,bytes32,address)() public {
    Begin block 0x133
    prev=[], succ=[0x145, 0x149]
    =================================
    0x134: v134(0xc7d) = CONST 
    0x137: v137(0x4) = CONST 
    0x13a: v13a = CALLDATASIZE 
    0x13b: v13b = SUB v13a, v137(0x4)
    0x13c: v13c(0xa0) = CONST 
    0x13f: v13f = LT v13b, v13c(0xa0)
    0x140: v140 = ISZERO v13f
    0x141: v141(0x149) = CONST 
    0x144: JUMPI v141(0x149), v140

    Begin block 0x145
    prev=[0x133], succ=[]
    =================================
    0x145: v145(0x0) = CONST 
    0x148: REVERT v145(0x0), v145(0x0)

    Begin block 0x149
    prev=[0x133], succ=[0x533]
    =================================
    0x14b: v14b(0x1) = CONST 
    0x14d: v14d(0x1) = CONST 
    0x14f: v14f(0xa0) = CONST 
    0x151: v151(0x10000000000000000000000000000000000000000) = SHL v14f(0xa0), v14d(0x1)
    0x152: v152(0xffffffffffffffffffffffffffffffffffffffff) = SUB v151(0x10000000000000000000000000000000000000000), v14b(0x1)
    0x154: v154 = CALLDATALOAD v137(0x4)
    0x156: v156 = AND v152(0xffffffffffffffffffffffffffffffffffffffff), v154
    0x158: v158(0x20) = CONST 
    0x15b: v15b(0x24) = ADD v137(0x4), v158(0x20)
    0x15c: v15c = CALLDATALOAD v15b(0x24)
    0x15e: v15e = AND v152(0xffffffffffffffffffffffffffffffffffffffff), v15c
    0x160: v160(0x40) = CONST 
    0x163: v163(0x44) = ADD v137(0x4), v160(0x40)
    0x164: v164 = CALLDATALOAD v163(0x44)
    0x166: v166 = AND v152(0xffffffffffffffffffffffffffffffffffffffff), v164
    0x168: v168(0x60) = CONST 
    0x16b: v16b(0x64) = ADD v137(0x4), v168(0x60)
    0x16c: v16c = CALLDATALOAD v16b(0x64)
    0x16e: v16e(0x80) = CONST 
    0x172: v172(0x84) = ADD v137(0x4), v16e(0x80)
    0x173: v173 = CALLDATALOAD v172(0x84)
    0x174: v174 = AND v173, v152(0xffffffffffffffffffffffffffffffffffffffff)
    0x175: v175(0x533) = CONST 
    0x178: JUMP v175(0x533)

    Begin block 0x533
    prev=[0x149], succ=[0x54c, 0x544]
    =================================
    0x534: v534(0x0) = CONST 
    0x536: v536 = SLOAD v534(0x0)
    0x537: v537(0x100) = CONST 
    0x53b: v53b = DIV v536, v537(0x100)
    0x53c: v53c(0xff) = CONST 
    0x53e: v53e = AND v53c(0xff), v53b
    0x540: v540(0x54c) = CONST 
    0x543: JUMPI v540(0x54c), v53e

    Begin block 0x54c
    prev=[0x533, 0x90aB0x544], succ=[0x55a, 0x552]
    =================================
    0x54c_0x0: v54c_0 = PHI v53e, v90dV544
    0x54e: v54e(0x55a) = CONST 
    0x551: JUMPI v54e(0x55a), v54c_0

    Begin block 0x55a
    prev=[0x54c, 0x552], succ=[0x55f, 0x595]
    =================================
    0x55a_0x0: v55a_0 = PHI v53e, v559, v90dV544
    0x55b: v55b(0x595) = CONST 
    0x55e: JUMPI v55b(0x595), v55a_0

    Begin block 0x55f
    prev=[0x55a], succ=[]
    =================================
    0x55f: v55f(0x40) = CONST 
    0x561: v561 = MLOAD v55f(0x40)
    0x562: v562(0x461bcd) = CONST 
    0x566: v566(0xe5) = CONST 
    0x568: v568(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v566(0xe5), v562(0x461bcd)
    0x56a: MSTORE v561, v568(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x56b: v56b(0x4) = CONST 
    0x56d: v56d = ADD v56b(0x4), v561
    0x570: v570(0x20) = CONST 
    0x572: v572 = ADD v570(0x20), v56d
    0x575: v575(0x20) = SUB v572, v56d
    0x577: MSTORE v56d, v575(0x20)
    0x578: v578(0x2e) = CONST 
    0x57b: MSTORE v572, v578(0x2e)
    0x57c: v57c(0x20) = CONST 
    0x57e: v57e = ADD v57c(0x20), v572
    0x580: v580(0xa8c) = CONST 
    0x583: v583(0x2e) = CONST 
    0x586: CODECOPY v57e, v580(0xa8c), v583(0x2e)
    0x587: v587(0x40) = CONST 
    0x589: v589 = ADD v587(0x40), v57e
    0x58d: v58d(0x40) = CONST 
    0x58f: v58f = MLOAD v58d(0x40)
    0x592: v592(0x84) = SUB v589, v58f
    0x594: REVERT v58f, v592(0x84)

    Begin block 0x595
    prev=[0x55a], succ=[0x5a8, 0x5c0]
    =================================
    0x596: v596(0x0) = CONST 
    0x598: v598 = SLOAD v596(0x0)
    0x599: v599(0x100) = CONST 
    0x59d: v59d = DIV v598, v599(0x100)
    0x59e: v59e(0xff) = CONST 
    0x5a0: v5a0 = AND v59e(0xff), v59d
    0x5a1: v5a1 = ISZERO v5a0
    0x5a3: v5a3 = ISZERO v5a1
    0x5a4: v5a4(0x5c0) = CONST 
    0x5a7: JUMPI v5a4(0x5c0), v5a3

    Begin block 0x5a8
    prev=[0x595], succ=[0x5c0]
    =================================
    0x5a8: v5a8(0x0) = CONST 
    0x5ab: v5ab = SLOAD v5a8(0x0)
    0x5ac: v5ac(0xff) = CONST 
    0x5ae: v5ae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v5ac(0xff)
    0x5af: v5af(0xff00) = CONST 
    0x5b2: v5b2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v5af(0xff00)
    0x5b5: v5b5 = AND v5ab, v5b2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x5b6: v5b6(0x100) = CONST 
    0x5b9: v5b9 = OR v5b6(0x100), v5b5
    0x5ba: v5ba = AND v5b9, v5ae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x5bb: v5bb(0x1) = CONST 
    0x5bd: v5bd = OR v5bb(0x1), v5ba
    0x5bf: SSTORE v5a8(0x0), v5bd

    Begin block 0x5c0
    prev=[0x5a8, 0x595], succ=[0x910B0x5c0]
    =================================
    0x5c1: v5c1(0x5c9) = CONST 
    0x5c5: v5c5(0x910) = CONST 
    0x5c8: JUMP v5c5(0x910)

    Begin block 0x910B0x5c0
    prev=[0x5c0], succ=[0x944B0x5c0, 0x940B0x5c0]
    =================================
    0x911S0x5c0: v911V5c0(0x0) = CONST 
    0x914S0x5c0: v914V5c0 = EXTCODEHASH v156
    0x915S0x5c0: v915V5c0(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x938S0x5c0: v938V5c0 = EQ v915V5c0(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470), v914V5c0
    0x93aS0x5c0: v93aV5c0 = ISZERO v938V5c0
    0x93cS0x5c0: v93cV5c0(0x944) = CONST 
    0x93fS0x5c0: JUMPI v93cV5c0(0x944), v938V5c0

    Begin block 0x944B0x5c0
    prev=[0x910B0x5c0, 0x940B0x5c0], succ=[0x5c9]
    =================================
    0x944_0x0S0x5c0: v944_0V5c0 = PHI v93aV5c0, v943V5c0
    0x94bS0x5c0: JUMP v5c1(0x5c9)

    Begin block 0x5c9
    prev=[0x944B0x5c0], succ=[0x5e8, 0x62e]
    =================================
    0x5ca: v5ca(0x40) = CONST 
    0x5cc: v5cc = MLOAD v5ca(0x40)
    0x5ce: v5ce(0x60) = CONST 
    0x5d0: v5d0 = ADD v5ce(0x60), v5cc
    0x5d1: v5d1(0x40) = CONST 
    0x5d3: MSTORE v5d1(0x40), v5d0
    0x5d5: v5d5(0x2a) = CONST 
    0x5d8: MSTORE v5cc, v5d5(0x2a)
    0x5d9: v5d9(0x20) = CONST 
    0x5db: v5db = ADD v5d9(0x20), v5cc
    0x5dc: v5dc(0xa62) = CONST 
    0x5df: v5df(0x2a) = CONST 
    0x5e2: CODECOPY v5db, v5dc(0xa62), v5df(0x2a)
    0x5e4: v5e4(0x62e) = CONST 
    0x5e7: JUMPI v5e4(0x62e), v944_0V5c0

    Begin block 0x5e8
    prev=[0x5c9], succ=[0x61f, 0x2660x133]
    =================================
    0x5e8: v5e8(0x40) = CONST 
    0x5ea: v5ea = MLOAD v5e8(0x40)
    0x5eb: v5eb(0x461bcd) = CONST 
    0x5ef: v5ef(0xe5) = CONST 
    0x5f1: v5f1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5ef(0xe5), v5eb(0x461bcd)
    0x5f3: MSTORE v5ea, v5f1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5f4: v5f4(0x20) = CONST 
    0x5f6: v5f6(0x4) = CONST 
    0x5f9: v5f9 = ADD v5ea, v5f6(0x4)
    0x5fc: MSTORE v5f9, v5f4(0x20)
    0x5fe: v5fe(0x2a) = MLOAD v5cc
    0x5ff: v5ff(0x24) = CONST 
    0x602: v602 = ADD v5ea, v5ff(0x24)
    0x603: MSTORE v602, v5fe(0x2a)
    0x605: v605(0x2a) = MLOAD v5cc
    0x60a: v60a(0x44) = CONST 
    0x60e: v60e = ADD v5ea, v60a(0x44)
    0x612: v612 = ADD v5cc, v5f4(0x20)
    0x617: v617(0x0) = CONST 
    0x61a: v61a = ISZERO v605(0x2a)
    0x61b: v61b(0x266) = CONST 
    0x61e: JUMPI v61b(0x266), v61a

    Begin block 0x61f
    prev=[0x5e8], succ=[0x24e0x133]
    =================================
    0x621: v621 = ADD v617(0x0), v612
    0x622: v622 = MLOAD v621
    0x625: v625 = ADD v617(0x0), v60e
    0x626: MSTORE v625, v622
    0x627: v627(0x20) = CONST 
    0x629: v629(0x20) = ADD v627(0x20), v617(0x0)
    0x62a: v62a(0x24e) = CONST 
    0x62d: JUMP v62a(0x24e)

    Begin block 0x24e0x133
    prev=[0x61f, 0x68e, 0x2570x133], succ=[0x2660x133, 0x2570x133]
    =================================
    0x24e0x133_0x0: v24e133_0 = PHI v629(0x20), v698(0x20), v133261
    0x24e0x133_0x3: v24e133_3 = PHI v605(0x2a), v674(0x2d)
    0x2510x133: v133251 = LT v24e133_0, v24e133_3
    0x2520x133: v133252 = ISZERO v133251
    0x2530x133: v133253(0x266) = CONST 
    0x2560x133: JUMPI v133253(0x266), v133252

    Begin block 0x2660x133
    prev=[0x5e8, 0x657, 0x24e0x133], succ=[0x2930x133, 0x27a0x133]
    =================================
    0x2660x133_0x4: v266133_4 = PHI v605(0x2a), v674(0x2d)
    0x2660x133_0x6: v266133_6 = PHI v60e, v67d
    0x26f0x133: v13326f = ADD v266133_4, v266133_6
    0x2710x133: v133271(0x1f) = CONST 
    0x2730x133: v133273 = AND v133271(0x1f), v266133_4
    0x2750x133: v133275 = ISZERO v133273
    0x2760x133: v133276(0x293) = CONST 
    0x2790x133: JUMPI v133276(0x293), v133275

    Begin block 0x2930x133
    prev=[0x2660x133, 0x27a0x133], succ=[]
    =================================
    0x2930x133_0x1: v293133_1 = PHI v133290, v13326f
    0x2990x133: v133299(0x40) = CONST 
    0x29b0x133: v13329b = MLOAD v133299(0x40)
    0x29e0x133: v13329e = SUB v293133_1, v13329b
    0x2a00x133: REVERT v13329b, v13329e

    Begin block 0x27a0x133
    prev=[0x2660x133], succ=[0x2930x133]
    =================================
    0x27c0x133: v13327c = SUB v13326f, v133273
    0x27e0x133: v13327e = MLOAD v13327c
    0x27f0x133: v13327f(0x1) = CONST 
    0x2820x133: v133282(0x20) = CONST 
    0x2840x133: v133284 = SUB v133282(0x20), v133273
    0x2850x133: v133285(0x100) = CONST 
    0x2880x133: v133288 = EXP v133285(0x100), v133284
    0x2890x133: v133289 = SUB v133288, v13327f(0x1)
    0x28a0x133: v13328a = NOT v133289
    0x28b0x133: v13328b = AND v13328a, v13327e
    0x28d0x133: MSTORE v13327c, v13328b
    0x28e0x133: v13328e(0x20) = CONST 
    0x2900x133: v133290 = ADD v13328e(0x20), v13327c

    Begin block 0x2570x133
    prev=[0x24e0x133], succ=[0x24e0x133]
    =================================
    0x2570x133_0x0: v257133_0 = PHI v629(0x20), v698(0x20), v133261
    0x2570x133_0x1: v257133_1 = PHI v612, v681
    0x2570x133_0x2: v257133_2 = PHI v60e, v67d
    0x2590x133: v133259 = ADD v257133_0, v257133_1
    0x25a0x133: v13325a = MLOAD v133259
    0x25d0x133: v13325d = ADD v257133_0, v257133_2
    0x25e0x133: MSTORE v13325d, v13325a
    0x25f0x133: v13325f(0x20) = CONST 
    0x2610x133: v133261 = ADD v13325f(0x20), v257133_0
    0x2620x133: v133262(0x24e) = CONST 
    0x2650x133: JUMP v133262(0x24e)

    Begin block 0x62e
    prev=[0x5c9], succ=[0x910B0x62e]
    =================================
    0x630: v630(0x638) = CONST 
    0x634: v634(0x910) = CONST 
    0x637: JUMP v634(0x910)

    Begin block 0x910B0x62e
    prev=[0x62e], succ=[0x944B0x62e, 0x940B0x62e]
    =================================
    0x911S0x62e: v911V62e(0x0) = CONST 
    0x914S0x62e: v914V62e = EXTCODEHASH v166
    0x915S0x62e: v915V62e(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x938S0x62e: v938V62e = EQ v915V62e(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470), v914V62e
    0x93aS0x62e: v93aV62e = ISZERO v938V62e
    0x93cS0x62e: v93cV62e(0x944) = CONST 
    0x93fS0x62e: JUMPI v93cV62e(0x944), v938V62e

    Begin block 0x944B0x62e
    prev=[0x910B0x62e, 0x940B0x62e], succ=[0x638]
    =================================
    0x944_0x0S0x62e: v944_0V62e = PHI v93aV62e, v943V62e
    0x94bS0x62e: JUMP v630(0x638)

    Begin block 0x638
    prev=[0x944B0x62e], succ=[0x657, 0x69d]
    =================================
    0x639: v639(0x40) = CONST 
    0x63b: v63b = MLOAD v639(0x40)
    0x63d: v63d(0x60) = CONST 
    0x63f: v63f = ADD v63d(0x60), v63b
    0x640: v640(0x40) = CONST 
    0x642: MSTORE v640(0x40), v63f
    0x644: v644(0x2d) = CONST 
    0x647: MSTORE v63b, v644(0x2d)
    0x648: v648(0x20) = CONST 
    0x64a: v64a = ADD v648(0x20), v63b
    0x64b: v64b(0xadc) = CONST 
    0x64e: v64e(0x2d) = CONST 
    0x651: CODECOPY v64a, v64b(0xadc), v64e(0x2d)
    0x653: v653(0x69d) = CONST 
    0x656: JUMPI v653(0x69d), v944_0V62e

    Begin block 0x657
    prev=[0x638], succ=[0x68e, 0x2660x133]
    =================================
    0x657: v657(0x40) = CONST 
    0x659: v659 = MLOAD v657(0x40)
    0x65a: v65a(0x461bcd) = CONST 
    0x65e: v65e(0xe5) = CONST 
    0x660: v660(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v65e(0xe5), v65a(0x461bcd)
    0x662: MSTORE v659, v660(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x663: v663(0x20) = CONST 
    0x665: v665(0x4) = CONST 
    0x668: v668 = ADD v659, v665(0x4)
    0x66b: MSTORE v668, v663(0x20)
    0x66d: v66d(0x2d) = MLOAD v63b
    0x66e: v66e(0x24) = CONST 
    0x671: v671 = ADD v659, v66e(0x24)
    0x672: MSTORE v671, v66d(0x2d)
    0x674: v674(0x2d) = MLOAD v63b
    0x679: v679(0x44) = CONST 
    0x67d: v67d = ADD v659, v679(0x44)
    0x681: v681 = ADD v63b, v663(0x20)
    0x686: v686(0x0) = CONST 
    0x689: v689 = ISZERO v674(0x2d)
    0x68a: v68a(0x266) = CONST 
    0x68d: JUMPI v68a(0x266), v689

    Begin block 0x68e
    prev=[0x657], succ=[0x24e0x133]
    =================================
    0x690: v690 = ADD v686(0x0), v681
    0x691: v691 = MLOAD v690
    0x694: v694 = ADD v686(0x0), v67d
    0x695: MSTORE v694, v691
    0x696: v696(0x20) = CONST 
    0x698: v698(0x20) = ADD v696(0x20), v686(0x0)
    0x699: v699(0x24e) = CONST 
    0x69c: JUMP v699(0x24e)

    Begin block 0x69d
    prev=[0x638], succ=[0x6e9]
    =================================
    0x69f: v69f(0x34) = CONST 
    0x6a2: v6a2 = SLOAD v69f(0x34)
    0x6a3: v6a3(0x1) = CONST 
    0x6a5: v6a5(0x1) = CONST 
    0x6a7: v6a7(0xa0) = CONST 
    0x6a9: v6a9(0x10000000000000000000000000000000000000000) = SHL v6a7(0xa0), v6a5(0x1)
    0x6aa: v6aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6a9(0x10000000000000000000000000000000000000000), v6a3(0x1)
    0x6ad: v6ad = AND v156, v6aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x6ae: v6ae(0x1) = CONST 
    0x6b0: v6b0(0x1) = CONST 
    0x6b2: v6b2(0xa0) = CONST 
    0x6b4: v6b4(0x10000000000000000000000000000000000000000) = SHL v6b2(0xa0), v6b0(0x1)
    0x6b5: v6b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b4(0x10000000000000000000000000000000000000000), v6ae(0x1)
    0x6b6: v6b6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6b5(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b9: v6b9 = AND v6b6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6a2
    0x6ba: v6ba = OR v6b9, v6ad
    0x6bd: SSTORE v69f(0x34), v6ba
    0x6be: v6be(0x35) = CONST 
    0x6c1: v6c1 = SLOAD v6be(0x35)
    0x6c4: v6c4 = AND v6aa(0xffffffffffffffffffffffffffffffffffffffff), v166
    0x6c7: v6c7 = AND v6b6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6c1
    0x6c8: v6c8 = OR v6c7, v6c4
    0x6ca: SSTORE v6be(0x35), v6c8
    0x6cb: v6cb(0x36) = CONST 
    0x6cf: SSTORE v6cb(0x36), v16c
    0x6d0: v6d0(0x37) = CONST 
    0x6d3: v6d3 = SLOAD v6d0(0x37)
    0x6d6: v6d6 = AND v174, v6aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x6da: v6da = AND v6b6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6d3
    0x6de: v6de = OR v6da, v6d6
    0x6e0: SSTORE v6d0(0x37), v6de
    0x6e1: v6e1(0x6e9) = CONST 
    0x6e5: v6e5(0x94c) = CONST 
    0x6e8: CALLPRIVATE v6e5(0x94c), v15e, v6e1(0x6e9)

    Begin block 0x6e9
    prev=[0x69d], succ=[0x6f1]
    =================================
    0x6ea: v6ea(0x6f1) = CONST 
    0x6ed: v6ed(0x484) = CONST 
    0x6f0: CALLPRIVATE v6ed(0x484), v6ea(0x6f1)

    Begin block 0x6f1
    prev=[0x6e9], succ=[0x6f8, 0xd64]
    =================================
    0x6f3: v6f3 = ISZERO v5a1
    0x6f4: v6f4(0xd64) = CONST 
    0x6f7: JUMPI v6f4(0xd64), v6f3

    Begin block 0x6f8
    prev=[0x6f1], succ=[0xc7d]
    =================================
    0x6f8: v6f8(0x0) = CONST 
    0x6fb: v6fb = SLOAD v6f8(0x0)
    0x6fc: v6fc(0xff00) = CONST 
    0x6ff: v6ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v6fc(0xff00)
    0x700: v700 = AND v6ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v6fb
    0x702: SSTORE v6f8(0x0), v700
    0x709: JUMP v134(0xc7d)

    Begin block 0xc7d
    prev=[0x6f8, 0xd64], succ=[]
    =================================
    0xc7e: STOP 

    Begin block 0xd64
    prev=[0x6f1], succ=[0xc7d]
    =================================
    0xd6b: JUMP v134(0xc7d)

    Begin block 0x940B0x62e
    prev=[0x910B0x62e], succ=[0x944B0x62e]
    =================================
    0x942S0x62e: v942V62e = ISZERO v914V62e
    0x943S0x62e: v943V62e = ISZERO v942V62e

    Begin block 0x940B0x5c0
    prev=[0x910B0x5c0], succ=[0x944B0x5c0]
    =================================
    0x942S0x5c0: v942V5c0 = ISZERO v914V5c0
    0x943S0x5c0: v943V5c0 = ISZERO v942V5c0

    Begin block 0x552
    prev=[0x54c], succ=[0x55a]
    =================================
    0x553: v553(0x0) = CONST 
    0x555: v555 = SLOAD v553(0x0)
    0x556: v556(0xff) = CONST 
    0x558: v558 = AND v556(0xff), v555
    0x559: v559 = ISZERO v558

    Begin block 0x544
    prev=[0x533], succ=[0x90aB0x544]
    =================================
    0x545: v545(0x54c) = CONST 
    0x548: v548(0x90a) = CONST 
    0x54b: JUMP v548(0x90a)

    Begin block 0x90aB0x544
    prev=[0x544], succ=[0x54c]
    =================================
    0x90bS0x544: v90bV544 = ADDRESS 
    0x90cS0x544: v90cV544 = EXTCODESIZE v90bV544
    0x90dS0x544: v90dV544 = ISZERO v90cV544
    0x90fS0x544: JUMP v545(0x54c)

}

function setGovernanceAddress(address)() public {
    Begin block 0x179
    prev=[], succ=[0x18b, 0x18f]
    =================================
    0x17a: v17a(0xc9e) = CONST 
    0x17d: v17d(0x4) = CONST 
    0x180: v180 = CALLDATASIZE 
    0x181: v181 = SUB v180, v17d(0x4)
    0x182: v182(0x20) = CONST 
    0x185: v185 = LT v181, v182(0x20)
    0x186: v186 = ISZERO v185
    0x187: v187(0x18f) = CONST 
    0x18a: JUMPI v187(0x18f), v186

    Begin block 0x18b
    prev=[0x179], succ=[]
    =================================
    0x18b: v18b(0x0) = CONST 
    0x18e: REVERT v18b(0x0), v18b(0x0)

    Begin block 0x18f
    prev=[0x179], succ=[0x70a]
    =================================
    0x191: v191 = CALLDATALOAD v17d(0x4)
    0x192: v192(0x1) = CONST 
    0x194: v194(0x1) = CONST 
    0x196: v196(0xa0) = CONST 
    0x198: v198(0x10000000000000000000000000000000000000000) = SHL v196(0xa0), v194(0x1)
    0x199: v199(0xffffffffffffffffffffffffffffffffffffffff) = SUB v198(0x10000000000000000000000000000000000000000), v192(0x1)
    0x19a: v19a = AND v199(0xffffffffffffffffffffffffffffffffffffffff), v191
    0x19b: v19b(0x70a) = CONST 
    0x19e: JUMP v19b(0x70a)

    Begin block 0x70a
    prev=[0x18f], succ=[0x712]
    =================================
    0x70b: v70b(0x712) = CONST 
    0x70e: v70e(0x87f) = CONST 
    0x711: CALLPRIVATE v70e(0x87f), v70b(0x712)

    Begin block 0x712
    prev=[0x70a], succ=[0x75b, 0x7a1]
    =================================
    0x713: v713(0x33) = CONST 
    0x715: v715(0x1) = CONST 
    0x718: v718 = SLOAD v713(0x33)
    0x71a: v71a(0x100) = CONST 
    0x71d: v71d(0x100) = EXP v71a(0x100), v715(0x1)
    0x71f: v71f = DIV v718, v71d(0x100)
    0x720: v720(0x1) = CONST 
    0x722: v722(0x1) = CONST 
    0x724: v724(0xa0) = CONST 
    0x726: v726(0x10000000000000000000000000000000000000000) = SHL v724(0xa0), v722(0x1)
    0x727: v727(0xffffffffffffffffffffffffffffffffffffffff) = SUB v726(0x10000000000000000000000000000000000000000), v720(0x1)
    0x728: v728 = AND v727(0xffffffffffffffffffffffffffffffffffffffff), v71f
    0x729: v729(0x1) = CONST 
    0x72b: v72b(0x1) = CONST 
    0x72d: v72d(0xa0) = CONST 
    0x72f: v72f(0x10000000000000000000000000000000000000000) = SHL v72d(0xa0), v72b(0x1)
    0x730: v730(0xffffffffffffffffffffffffffffffffffffffff) = SUB v72f(0x10000000000000000000000000000000000000000), v729(0x1)
    0x731: v731 = AND v730(0xffffffffffffffffffffffffffffffffffffffff), v728
    0x732: v732 = CALLER 
    0x733: v733(0x1) = CONST 
    0x735: v735(0x1) = CONST 
    0x737: v737(0xa0) = CONST 
    0x739: v739(0x10000000000000000000000000000000000000000) = SHL v737(0xa0), v735(0x1)
    0x73a: v73a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v739(0x10000000000000000000000000000000000000000), v733(0x1)
    0x73b: v73b = AND v73a(0xffffffffffffffffffffffffffffffffffffffff), v732
    0x73c: v73c = EQ v73b, v731
    0x73d: v73d(0x40) = CONST 
    0x73f: v73f = MLOAD v73d(0x40)
    0x741: v741(0x60) = CONST 
    0x743: v743 = ADD v741(0x60), v73f
    0x744: v744(0x40) = CONST 
    0x746: MSTORE v744(0x40), v743
    0x748: v748(0x22) = CONST 
    0x74b: MSTORE v73f, v748(0x22)
    0x74c: v74c(0x20) = CONST 
    0x74e: v74e = ADD v74c(0x20), v73f
    0x74f: v74f(0xaba) = CONST 
    0x752: v752(0x22) = CONST 
    0x755: CODECOPY v74e, v74f(0xaba), v752(0x22)
    0x757: v757(0x7a1) = CONST 
    0x75a: JUMPI v757(0x7a1), v73c

    Begin block 0x75b
    prev=[0x712], succ=[0x792, 0x2660x179]
    =================================
    0x75b: v75b(0x40) = CONST 
    0x75d: v75d = MLOAD v75b(0x40)
    0x75e: v75e(0x461bcd) = CONST 
    0x762: v762(0xe5) = CONST 
    0x764: v764(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v762(0xe5), v75e(0x461bcd)
    0x766: MSTORE v75d, v764(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x767: v767(0x20) = CONST 
    0x769: v769(0x4) = CONST 
    0x76c: v76c = ADD v75d, v769(0x4)
    0x76f: MSTORE v76c, v767(0x20)
    0x771: v771(0x22) = MLOAD v73f
    0x772: v772(0x24) = CONST 
    0x775: v775 = ADD v75d, v772(0x24)
    0x776: MSTORE v775, v771(0x22)
    0x778: v778(0x22) = MLOAD v73f
    0x77d: v77d(0x44) = CONST 
    0x781: v781 = ADD v75d, v77d(0x44)
    0x785: v785 = ADD v73f, v767(0x20)
    0x78a: v78a(0x0) = CONST 
    0x78d: v78d = ISZERO v778(0x22)
    0x78e: v78e(0x266) = CONST 
    0x791: JUMPI v78e(0x266), v78d

    Begin block 0x792
    prev=[0x75b], succ=[0x24e0x179]
    =================================
    0x794: v794 = ADD v78a(0x0), v785
    0x795: v795 = MLOAD v794
    0x798: v798 = ADD v78a(0x0), v781
    0x799: MSTORE v798, v795
    0x79a: v79a(0x20) = CONST 
    0x79c: v79c(0x20) = ADD v79a(0x20), v78a(0x0)
    0x79d: v79d(0x24e) = CONST 
    0x7a0: JUMP v79d(0x24e)

    Begin block 0x24e0x179
    prev=[0x792, 0x2570x179], succ=[0x2660x179, 0x2570x179]
    =================================
    0x24e0x179_0x0: v24e179_0 = PHI v79c(0x20), v179261
    0x2510x179: v179251 = LT v24e179_0, v778(0x22)
    0x2520x179: v179252 = ISZERO v179251
    0x2530x179: v179253(0x266) = CONST 
    0x2560x179: JUMPI v179253(0x266), v179252

    Begin block 0x2660x179
    prev=[0x75b, 0x24e0x179], succ=[0x2930x179, 0x27a0x179]
    =================================
    0x26f0x179: v17926f = ADD v778(0x22), v781
    0x2710x179: v179271(0x1f) = CONST 
    0x2730x179: v179273(0x2) = AND v179271(0x1f), v778(0x22)
    0x2750x179: v179275 = ISZERO v179273(0x2)
    0x2760x179: v179276(0x293) = CONST 
    0x2790x179: JUMPI v179276(0x293), v179275

    Begin block 0x2930x179
    prev=[0x2660x179, 0x27a0x179], succ=[]
    =================================
    0x2930x179_0x1: v293179_1 = PHI v179290, v17926f
    0x2990x179: v179299(0x40) = CONST 
    0x29b0x179: v17929b = MLOAD v179299(0x40)
    0x29e0x179: v17929e = SUB v293179_1, v17929b
    0x2a00x179: REVERT v17929b, v17929e

    Begin block 0x27a0x179
    prev=[0x2660x179], succ=[0x2930x179]
    =================================
    0x27c0x179: v17927c = SUB v17926f, v179273(0x2)
    0x27e0x179: v17927e = MLOAD v17927c
    0x27f0x179: v17927f(0x1) = CONST 
    0x2820x179: v179282(0x20) = CONST 
    0x2840x179: v179284(0x1e) = SUB v179282(0x20), v179273(0x2)
    0x2850x179: v179285(0x100) = CONST 
    0x2880x179: v179288(0x1000000000000000000000000000000000000000000000000000000000000) = EXP v179285(0x100), v179284(0x1e)
    0x2890x179: v179289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v179288(0x1000000000000000000000000000000000000000000000000000000000000), v17927f(0x1)
    0x28a0x179: v17928a = NOT v179289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x28b0x179: v17928b = AND v17928a, v17927e
    0x28d0x179: MSTORE v17927c, v17928b
    0x28e0x179: v17928e(0x20) = CONST 
    0x2900x179: v179290 = ADD v17928e(0x20), v17927c

    Begin block 0x2570x179
    prev=[0x24e0x179], succ=[0x24e0x179]
    =================================
    0x2570x179_0x0: v257179_0 = PHI v79c(0x20), v179261
    0x2590x179: v179259 = ADD v257179_0, v785
    0x25a0x179: v17925a = MLOAD v179259
    0x25d0x179: v17925d = ADD v257179_0, v781
    0x25e0x179: MSTORE v17925d, v17925a
    0x25f0x179: v17925f(0x20) = CONST 
    0x2610x179: v179261 = ADD v17925f(0x20), v257179_0
    0x2620x179: v179262(0x24e) = CONST 
    0x2650x179: JUMP v179262(0x24e)

    Begin block 0x7a1
    prev=[0x712], succ=[0xd8b]
    =================================
    0x7a3: v7a3(0xd8b) = CONST 
    0x7a7: v7a7(0x94c) = CONST 
    0x7aa: CALLPRIVATE v7a7(0x94c), v19a, v7a3(0xd8b)

    Begin block 0xd8b
    prev=[0x7a1], succ=[0xc9e]
    =================================
    0xd8d: JUMP v17a(0xc9e)

    Begin block 0xc9e
    prev=[0xd8b], succ=[]
    =================================
    0xc9f: STOP 

}

function setAntiAbuseOracleAddress(address)() public {
    Begin block 0x19f
    prev=[], succ=[0x1b1, 0x1b5]
    =================================
    0x1a0: v1a0(0xcbf) = CONST 
    0x1a3: v1a3(0x4) = CONST 
    0x1a6: v1a6 = CALLDATASIZE 
    0x1a7: v1a7 = SUB v1a6, v1a3(0x4)
    0x1a8: v1a8(0x20) = CONST 
    0x1ab: v1ab = LT v1a7, v1a8(0x20)
    0x1ac: v1ac = ISZERO v1ab
    0x1ad: v1ad(0x1b5) = CONST 
    0x1b0: JUMPI v1ad(0x1b5), v1ac

    Begin block 0x1b1
    prev=[0x19f], succ=[]
    =================================
    0x1b1: v1b1(0x0) = CONST 
    0x1b4: REVERT v1b1(0x0), v1b1(0x0)

    Begin block 0x1b5
    prev=[0x19f], succ=[0x7ab]
    =================================
    0x1b7: v1b7 = CALLDATALOAD v1a3(0x4)
    0x1b8: v1b8(0x1) = CONST 
    0x1ba: v1ba(0x1) = CONST 
    0x1bc: v1bc(0xa0) = CONST 
    0x1be: v1be(0x10000000000000000000000000000000000000000) = SHL v1bc(0xa0), v1ba(0x1)
    0x1bf: v1bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1be(0x10000000000000000000000000000000000000000), v1b8(0x1)
    0x1c0: v1c0 = AND v1bf(0xffffffffffffffffffffffffffffffffffffffff), v1b7
    0x1c1: v1c1(0x7ab) = CONST 
    0x1c4: JUMP v1c1(0x7ab)

    Begin block 0x7ab
    prev=[0x1b5], succ=[0x7b3]
    =================================
    0x7ac: v7ac(0x7b3) = CONST 
    0x7af: v7af(0x87f) = CONST 
    0x7b2: CALLPRIVATE v7af(0x87f), v7ac(0x7b3)

    Begin block 0x7b3
    prev=[0x7ab], succ=[0x7fc, 0x842]
    =================================
    0x7b4: v7b4(0x33) = CONST 
    0x7b6: v7b6(0x1) = CONST 
    0x7b9: v7b9 = SLOAD v7b4(0x33)
    0x7bb: v7bb(0x100) = CONST 
    0x7be: v7be(0x100) = EXP v7bb(0x100), v7b6(0x1)
    0x7c0: v7c0 = DIV v7b9, v7be(0x100)
    0x7c1: v7c1(0x1) = CONST 
    0x7c3: v7c3(0x1) = CONST 
    0x7c5: v7c5(0xa0) = CONST 
    0x7c7: v7c7(0x10000000000000000000000000000000000000000) = SHL v7c5(0xa0), v7c3(0x1)
    0x7c8: v7c8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c7(0x10000000000000000000000000000000000000000), v7c1(0x1)
    0x7c9: v7c9 = AND v7c8(0xffffffffffffffffffffffffffffffffffffffff), v7c0
    0x7ca: v7ca(0x1) = CONST 
    0x7cc: v7cc(0x1) = CONST 
    0x7ce: v7ce(0xa0) = CONST 
    0x7d0: v7d0(0x10000000000000000000000000000000000000000) = SHL v7ce(0xa0), v7cc(0x1)
    0x7d1: v7d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d0(0x10000000000000000000000000000000000000000), v7ca(0x1)
    0x7d2: v7d2 = AND v7d1(0xffffffffffffffffffffffffffffffffffffffff), v7c9
    0x7d3: v7d3 = CALLER 
    0x7d4: v7d4(0x1) = CONST 
    0x7d6: v7d6(0x1) = CONST 
    0x7d8: v7d8(0xa0) = CONST 
    0x7da: v7da(0x10000000000000000000000000000000000000000) = SHL v7d8(0xa0), v7d6(0x1)
    0x7db: v7db(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7da(0x10000000000000000000000000000000000000000), v7d4(0x1)
    0x7dc: v7dc = AND v7db(0xffffffffffffffffffffffffffffffffffffffff), v7d3
    0x7dd: v7dd = EQ v7dc, v7d2
    0x7de: v7de(0x40) = CONST 
    0x7e0: v7e0 = MLOAD v7de(0x40)
    0x7e2: v7e2(0x60) = CONST 
    0x7e4: v7e4 = ADD v7e2(0x60), v7e0
    0x7e5: v7e5(0x40) = CONST 
    0x7e7: MSTORE v7e5(0x40), v7e4
    0x7e9: v7e9(0x22) = CONST 
    0x7ec: MSTORE v7e0, v7e9(0x22)
    0x7ed: v7ed(0x20) = CONST 
    0x7ef: v7ef = ADD v7ed(0x20), v7e0
    0x7f0: v7f0(0xaba) = CONST 
    0x7f3: v7f3(0x22) = CONST 
    0x7f6: CODECOPY v7ef, v7f0(0xaba), v7f3(0x22)
    0x7f8: v7f8(0x842) = CONST 
    0x7fb: JUMPI v7f8(0x842), v7dd

    Begin block 0x7fc
    prev=[0x7b3], succ=[0x833, 0x2660x19f]
    =================================
    0x7fc: v7fc(0x40) = CONST 
    0x7fe: v7fe = MLOAD v7fc(0x40)
    0x7ff: v7ff(0x461bcd) = CONST 
    0x803: v803(0xe5) = CONST 
    0x805: v805(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v803(0xe5), v7ff(0x461bcd)
    0x807: MSTORE v7fe, v805(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x808: v808(0x20) = CONST 
    0x80a: v80a(0x4) = CONST 
    0x80d: v80d = ADD v7fe, v80a(0x4)
    0x810: MSTORE v80d, v808(0x20)
    0x812: v812(0x22) = MLOAD v7e0
    0x813: v813(0x24) = CONST 
    0x816: v816 = ADD v7fe, v813(0x24)
    0x817: MSTORE v816, v812(0x22)
    0x819: v819(0x22) = MLOAD v7e0
    0x81e: v81e(0x44) = CONST 
    0x822: v822 = ADD v7fe, v81e(0x44)
    0x826: v826 = ADD v7e0, v808(0x20)
    0x82b: v82b(0x0) = CONST 
    0x82e: v82e = ISZERO v819(0x22)
    0x82f: v82f(0x266) = CONST 
    0x832: JUMPI v82f(0x266), v82e

    Begin block 0x833
    prev=[0x7fc], succ=[0x24e0x19f]
    =================================
    0x835: v835 = ADD v82b(0x0), v826
    0x836: v836 = MLOAD v835
    0x839: v839 = ADD v82b(0x0), v822
    0x83a: MSTORE v839, v836
    0x83b: v83b(0x20) = CONST 
    0x83d: v83d(0x20) = ADD v83b(0x20), v82b(0x0)
    0x83e: v83e(0x24e) = CONST 
    0x841: JUMP v83e(0x24e)

    Begin block 0x24e0x19f
    prev=[0x833, 0x2570x19f], succ=[0x2660x19f, 0x2570x19f]
    =================================
    0x24e0x19f_0x0: v24e19f_0 = PHI v83d(0x20), v19f261
    0x2510x19f: v19f251 = LT v24e19f_0, v819(0x22)
    0x2520x19f: v19f252 = ISZERO v19f251
    0x2530x19f: v19f253(0x266) = CONST 
    0x2560x19f: JUMPI v19f253(0x266), v19f252

    Begin block 0x2660x19f
    prev=[0x7fc, 0x24e0x19f], succ=[0x2930x19f, 0x27a0x19f]
    =================================
    0x26f0x19f: v19f26f = ADD v819(0x22), v822
    0x2710x19f: v19f271(0x1f) = CONST 
    0x2730x19f: v19f273(0x2) = AND v19f271(0x1f), v819(0x22)
    0x2750x19f: v19f275 = ISZERO v19f273(0x2)
    0x2760x19f: v19f276(0x293) = CONST 
    0x2790x19f: JUMPI v19f276(0x293), v19f275

    Begin block 0x2930x19f
    prev=[0x2660x19f, 0x27a0x19f], succ=[]
    =================================
    0x2930x19f_0x1: v29319f_1 = PHI v19f290, v19f26f
    0x2990x19f: v19f299(0x40) = CONST 
    0x29b0x19f: v19f29b = MLOAD v19f299(0x40)
    0x29e0x19f: v19f29e = SUB v29319f_1, v19f29b
    0x2a00x19f: REVERT v19f29b, v19f29e

    Begin block 0x27a0x19f
    prev=[0x2660x19f], succ=[0x2930x19f]
    =================================
    0x27c0x19f: v19f27c = SUB v19f26f, v19f273(0x2)
    0x27e0x19f: v19f27e = MLOAD v19f27c
    0x27f0x19f: v19f27f(0x1) = CONST 
    0x2820x19f: v19f282(0x20) = CONST 
    0x2840x19f: v19f284(0x1e) = SUB v19f282(0x20), v19f273(0x2)
    0x2850x19f: v19f285(0x100) = CONST 
    0x2880x19f: v19f288(0x1000000000000000000000000000000000000000000000000000000000000) = EXP v19f285(0x100), v19f284(0x1e)
    0x2890x19f: v19f289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v19f288(0x1000000000000000000000000000000000000000000000000000000000000), v19f27f(0x1)
    0x28a0x19f: v19f28a = NOT v19f289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x28b0x19f: v19f28b = AND v19f28a, v19f27e
    0x28d0x19f: MSTORE v19f27c, v19f28b
    0x28e0x19f: v19f28e(0x20) = CONST 
    0x2900x19f: v19f290 = ADD v19f28e(0x20), v19f27c

    Begin block 0x2570x19f
    prev=[0x24e0x19f], succ=[0x24e0x19f]
    =================================
    0x2570x19f_0x0: v25719f_0 = PHI v83d(0x20), v19f261
    0x2590x19f: v19f259 = ADD v25719f_0, v826
    0x25a0x19f: v19f25a = MLOAD v19f259
    0x25d0x19f: v19f25d = ADD v25719f_0, v822
    0x25e0x19f: MSTORE v19f25d, v19f25a
    0x25f0x19f: v19f25f(0x20) = CONST 
    0x2610x19f: v19f261 = ADD v19f25f(0x20), v25719f_0
    0x2620x19f: v19f262(0x24e) = CONST 
    0x2650x19f: JUMP v19f262(0x24e)

    Begin block 0x842
    prev=[0x7b3], succ=[0xcbf]
    =================================
    0x844: v844(0x37) = CONST 
    0x847: v847 = SLOAD v844(0x37)
    0x848: v848(0x1) = CONST 
    0x84a: v84a(0x1) = CONST 
    0x84c: v84c(0xa0) = CONST 
    0x84e: v84e(0x10000000000000000000000000000000000000000) = SHL v84c(0xa0), v84a(0x1)
    0x84f: v84f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v84e(0x10000000000000000000000000000000000000000), v848(0x1)
    0x850: v850(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v84f(0xffffffffffffffffffffffffffffffffffffffff)
    0x851: v851 = AND v850(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v847
    0x852: v852(0x1) = CONST 
    0x854: v854(0x1) = CONST 
    0x856: v856(0xa0) = CONST 
    0x858: v858(0x10000000000000000000000000000000000000000) = SHL v856(0xa0), v854(0x1)
    0x859: v859(0xffffffffffffffffffffffffffffffffffffffff) = SUB v858(0x10000000000000000000000000000000000000000), v852(0x1)
    0x85d: v85d = AND v859(0xffffffffffffffffffffffffffffffffffffffff), v1c0
    0x861: v861 = OR v85d, v851
    0x863: SSTORE v844(0x37), v861
    0x864: JUMP v1a0(0xcbf)

    Begin block 0xcbf
    prev=[0x842], succ=[]
    =================================
    0xcc0: STOP 

}

function token()() public {
    Begin block 0x1c5
    prev=[], succ=[0x865]
    =================================
    0x1c6: v1c6(0xce0) = CONST 
    0x1c9: v1c9(0x865) = CONST 
    0x1cc: JUMP v1c9(0x865)

    Begin block 0x865
    prev=[0x1c5], succ=[0x86f]
    =================================
    0x866: v866(0x0) = CONST 
    0x868: v868(0x86f) = CONST 
    0x86b: v86b(0x87f) = CONST 
    0x86e: CALLPRIVATE v86b(0x87f), v868(0x86f)

    Begin block 0x86f
    prev=[0x865], succ=[0xce0]
    =================================
    0x871: v871(0x34) = CONST 
    0x873: v873 = SLOAD v871(0x34)
    0x874: v874(0x1) = CONST 
    0x876: v876(0x1) = CONST 
    0x878: v878(0xa0) = CONST 
    0x87a: v87a(0x10000000000000000000000000000000000000000) = SHL v878(0xa0), v876(0x1)
    0x87b: v87b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v87a(0x10000000000000000000000000000000000000000), v874(0x1)
    0x87c: v87c = AND v87b(0xffffffffffffffffffffffffffffffffffffffff), v873
    0x87e: JUMP v1c6(0xce0)

    Begin block 0xce0
    prev=[0x86f], succ=[]
    =================================
    0xce1: vce1(0x40) = CONST 
    0xce4: vce4 = MLOAD vce1(0x40)
    0xce5: vce5(0x1) = CONST 
    0xce7: vce7(0x1) = CONST 
    0xce9: vce9(0xa0) = CONST 
    0xceb: vceb(0x10000000000000000000000000000000000000000) = SHL vce9(0xa0), vce7(0x1)
    0xcec: vcec(0xffffffffffffffffffffffffffffffffffffffff) = SUB vceb(0x10000000000000000000000000000000000000000), vce5(0x1)
    0xcef: vcef = AND v87c, vcec(0xffffffffffffffffffffffffffffffffffffffff)
    0xcf1: MSTORE vce4, vcef
    0xcf2: vcf2 = MLOAD vce1(0x40)
    0xcf6: vcf6(0x0) = SUB vce4, vcf2
    0xcf7: vcf7(0x20) = CONST 
    0xcf9: vcf9(0x20) = ADD vcf7(0x20), vcf6(0x0)
    0xcfb: RETURN vcf2, vcf9(0x20)

}

function 0x484(0x484arg0x0) private {
    Begin block 0x484
    prev=[], succ=[0x49d, 0x495]
    =================================
    0x485: v485(0x0) = CONST 
    0x487: v487 = SLOAD v485(0x0)
    0x488: v488(0x100) = CONST 
    0x48c: v48c = DIV v487, v488(0x100)
    0x48d: v48d(0xff) = CONST 
    0x48f: v48f = AND v48d(0xff), v48c
    0x491: v491(0x49d) = CONST 
    0x494: JUMPI v491(0x49d), v48f

    Begin block 0x49d
    prev=[0x484, 0x90aB0x495], succ=[0x4ab, 0x4a3]
    =================================
    0x49d_0x0: v49d_0 = PHI v48f, v90dV495
    0x49f: v49f(0x4ab) = CONST 
    0x4a2: JUMPI v49f(0x4ab), v49d_0

    Begin block 0x4ab
    prev=[0x49d, 0x4a3], succ=[0x4b0, 0x4e6]
    =================================
    0x4ab_0x0: v4ab_0 = PHI v48f, v4aa, v90dV495
    0x4ac: v4ac(0x4e6) = CONST 
    0x4af: JUMPI v4ac(0x4e6), v4ab_0

    Begin block 0x4b0
    prev=[0x4ab], succ=[]
    =================================
    0x4b0: v4b0(0x40) = CONST 
    0x4b2: v4b2 = MLOAD v4b0(0x40)
    0x4b3: v4b3(0x461bcd) = CONST 
    0x4b7: v4b7(0xe5) = CONST 
    0x4b9: v4b9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v4b7(0xe5), v4b3(0x461bcd)
    0x4bb: MSTORE v4b2, v4b9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4bc: v4bc(0x4) = CONST 
    0x4be: v4be = ADD v4bc(0x4), v4b2
    0x4c1: v4c1(0x20) = CONST 
    0x4c3: v4c3 = ADD v4c1(0x20), v4be
    0x4c6: v4c6(0x20) = SUB v4c3, v4be
    0x4c8: MSTORE v4be, v4c6(0x20)
    0x4c9: v4c9(0x2e) = CONST 
    0x4cc: MSTORE v4c3, v4c9(0x2e)
    0x4cd: v4cd(0x20) = CONST 
    0x4cf: v4cf = ADD v4cd(0x20), v4c3
    0x4d1: v4d1(0xa8c) = CONST 
    0x4d4: v4d4(0x2e) = CONST 
    0x4d7: CODECOPY v4cf, v4d1(0xa8c), v4d4(0x2e)
    0x4d8: v4d8(0x40) = CONST 
    0x4da: v4da = ADD v4d8(0x40), v4cf
    0x4de: v4de(0x40) = CONST 
    0x4e0: v4e0 = MLOAD v4de(0x40)
    0x4e3: v4e3(0x84) = SUB v4da, v4e0
    0x4e5: REVERT v4e0, v4e3(0x84)

    Begin block 0x4e6
    prev=[0x4ab], succ=[0x4f9, 0x511]
    =================================
    0x4e7: v4e7(0x0) = CONST 
    0x4e9: v4e9 = SLOAD v4e7(0x0)
    0x4ea: v4ea(0x100) = CONST 
    0x4ee: v4ee = DIV v4e9, v4ea(0x100)
    0x4ef: v4ef(0xff) = CONST 
    0x4f1: v4f1 = AND v4ef(0xff), v4ee
    0x4f2: v4f2 = ISZERO v4f1
    0x4f4: v4f4 = ISZERO v4f2
    0x4f5: v4f5(0x511) = CONST 
    0x4f8: JUMPI v4f5(0x511), v4f4

    Begin block 0x4f9
    prev=[0x4e6], succ=[0x511]
    =================================
    0x4f9: v4f9(0x0) = CONST 
    0x4fc: v4fc = SLOAD v4f9(0x0)
    0x4fd: v4fd(0xff) = CONST 
    0x4ff: v4ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v4fd(0xff)
    0x500: v500(0xff00) = CONST 
    0x503: v503(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v500(0xff00)
    0x506: v506 = AND v4fc, v503(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x507: v507(0x100) = CONST 
    0x50a: v50a = OR v507(0x100), v506
    0x50b: v50b = AND v50a, v4ff(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x50c: v50c(0x1) = CONST 
    0x50e: v50e = OR v50c(0x1), v50b
    0x510: SSTORE v4f9(0x0), v50e

    Begin block 0x511
    prev=[0x4f9, 0x4e6], succ=[0x525, 0xd42]
    =================================
    0x512: v512(0x33) = CONST 
    0x515: v515 = SLOAD v512(0x33)
    0x516: v516(0xff) = CONST 
    0x518: v518(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v516(0xff)
    0x519: v519 = AND v518(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v515
    0x51a: v51a(0x1) = CONST 
    0x51c: v51c = OR v51a(0x1), v519
    0x51e: SSTORE v512(0x33), v51c
    0x520: v520 = ISZERO v4f2
    0x521: v521(0xd42) = CONST 
    0x524: JUMPI v521(0xd42), v520

    Begin block 0x525
    prev=[0x511], succ=[0x530]
    =================================
    0x525: v525(0x0) = CONST 
    0x528: v528 = SLOAD v525(0x0)
    0x529: v529(0xff00) = CONST 
    0x52c: v52c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v529(0xff00)
    0x52d: v52d = AND v52c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v528
    0x52f: SSTORE v525(0x0), v52d

    Begin block 0x530
    prev=[0x525], succ=[]
    =================================
    0x532: RETURNPRIVATE v484arg0

    Begin block 0xd42
    prev=[0x511], succ=[]
    =================================
    0xd44: RETURNPRIVATE v484arg0

    Begin block 0x4a3
    prev=[0x49d], succ=[0x4ab]
    =================================
    0x4a4: v4a4(0x0) = CONST 
    0x4a6: v4a6 = SLOAD v4a4(0x0)
    0x4a7: v4a7(0xff) = CONST 
    0x4a9: v4a9 = AND v4a7(0xff), v4a6
    0x4aa: v4aa = ISZERO v4a9

    Begin block 0x495
    prev=[0x484], succ=[0x90aB0x495]
    =================================
    0x496: v496(0x49d) = CONST 
    0x499: v499(0x90a) = CONST 
    0x49c: JUMP v499(0x90a)

    Begin block 0x90aB0x495
    prev=[0x495], succ=[0x49d]
    =================================
    0x90bS0x495: v90bV495 = ADDRESS 
    0x90cS0x495: v90cV495 = EXTCODESIZE v90bV495
    0x90dS0x495: v90dV495 = ISZERO v90cV495
    0x90fS0x495: JUMP v496(0x49d)

}

function 0x87f(0x87farg0x0) private {
    Begin block 0x87f
    prev=[], succ=[0x8c4, 0xdad]
    =================================
    0x880: v880(0x33) = CONST 
    0x882: v882 = SLOAD v880(0x33)
    0x883: v883(0x40) = CONST 
    0x886: v886 = MLOAD v883(0x40)
    0x889: v889 = ADD v883(0x40), v886
    0x88c: MSTORE v883(0x40), v889
    0x88d: v88d(0x20) = CONST 
    0x891: MSTORE v886, v88d(0x20)
    0x892: v892(0x496e697469616c697a61626c6556323a204e6f7420696e697469616c697a6564) = CONST 
    0x8b5: v8b5 = ADD v886, v88d(0x20)
    0x8b6: MSTORE v8b5, v892(0x496e697469616c697a61626c6556323a204e6f7420696e697469616c697a6564)
    0x8b8: v8b8(0xff) = CONST 
    0x8ba: v8ba = AND v8b8(0xff), v882
    0x8bb: v8bb = ISZERO v8ba
    0x8bc: v8bc = ISZERO v8bb
    0x8bd: v8bd(0x1) = CONST 
    0x8bf: v8bf = EQ v8bd(0x1), v8bc
    0x8c0: v8c0(0xdad) = CONST 
    0x8c3: JUMPI v8c0(0xdad), v8bf

    Begin block 0x8c4
    prev=[0x87f], succ=[0x8fb, 0x2660x87f]
    =================================
    0x8c4: v8c4(0x40) = CONST 
    0x8c6: v8c6 = MLOAD v8c4(0x40)
    0x8c7: v8c7(0x461bcd) = CONST 
    0x8cb: v8cb(0xe5) = CONST 
    0x8cd: v8cd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v8cb(0xe5), v8c7(0x461bcd)
    0x8cf: MSTORE v8c6, v8cd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8d0: v8d0(0x20) = CONST 
    0x8d2: v8d2(0x4) = CONST 
    0x8d5: v8d5 = ADD v8c6, v8d2(0x4)
    0x8d8: MSTORE v8d5, v8d0(0x20)
    0x8da: v8da(0x20) = MLOAD v886
    0x8db: v8db(0x24) = CONST 
    0x8de: v8de = ADD v8c6, v8db(0x24)
    0x8df: MSTORE v8de, v8da(0x20)
    0x8e1: v8e1(0x20) = MLOAD v886
    0x8e6: v8e6(0x44) = CONST 
    0x8ea: v8ea = ADD v8c6, v8e6(0x44)
    0x8ee: v8ee = ADD v886, v8d0(0x20)
    0x8f3: v8f3(0x0) = CONST 
    0x8f6: v8f6 = ISZERO v8e1(0x20)
    0x8f7: v8f7(0x266) = CONST 
    0x8fa: JUMPI v8f7(0x266), v8f6

    Begin block 0x8fb
    prev=[0x8c4], succ=[0x24e0x87f]
    =================================
    0x8fd: v8fd = ADD v8f3(0x0), v8ee
    0x8fe: v8fe = MLOAD v8fd
    0x901: v901 = ADD v8f3(0x0), v8ea
    0x902: MSTORE v901, v8fe
    0x903: v903(0x20) = CONST 
    0x905: v905(0x20) = ADD v903(0x20), v8f3(0x0)
    0x906: v906(0x24e) = CONST 
    0x909: JUMP v906(0x24e)

    Begin block 0x24e0x87f
    prev=[0x8fb, 0x2570x87f], succ=[0x2660x87f, 0x2570x87f]
    =================================
    0x24e0x87f_0x0: v24e87f_0 = PHI v905(0x20), v87f261
    0x2510x87f: v87f251 = LT v24e87f_0, v8e1(0x20)
    0x2520x87f: v87f252 = ISZERO v87f251
    0x2530x87f: v87f253(0x266) = CONST 
    0x2560x87f: JUMPI v87f253(0x266), v87f252

    Begin block 0x2660x87f
    prev=[0x8c4, 0x24e0x87f], succ=[0x2930x87f, 0x27a0x87f]
    =================================
    0x26f0x87f: v87f26f = ADD v8e1(0x20), v8ea
    0x2710x87f: v87f271(0x1f) = CONST 
    0x2730x87f: v87f273(0x0) = AND v87f271(0x1f), v8e1(0x20)
    0x2750x87f: v87f275 = ISZERO v87f273(0x0)
    0x2760x87f: v87f276(0x293) = CONST 
    0x2790x87f: JUMPI v87f276(0x293), v87f275

    Begin block 0x2930x87f
    prev=[0x2660x87f, 0x27a0x87f], succ=[]
    =================================
    0x2930x87f_0x1: v29387f_1 = PHI v87f290, v87f26f
    0x2990x87f: v87f299(0x40) = CONST 
    0x29b0x87f: v87f29b = MLOAD v87f299(0x40)
    0x29e0x87f: v87f29e = SUB v29387f_1, v87f29b
    0x2a00x87f: REVERT v87f29b, v87f29e

    Begin block 0x27a0x87f
    prev=[0x2660x87f], succ=[0x2930x87f]
    =================================
    0x27c0x87f: v87f27c = SUB v87f26f, v87f273(0x0)
    0x27e0x87f: v87f27e = MLOAD v87f27c
    0x27f0x87f: v87f27f(0x1) = CONST 
    0x2820x87f: v87f282(0x20) = CONST 
    0x2840x87f: v87f284(0x20) = SUB v87f282(0x20), v87f273(0x0)
    0x2850x87f: v87f285(0x100) = CONST 
    0x2880x87f: v87f288(0x1) = EXP v87f285(0x100), v87f284(0x20)
    0x2890x87f: v87f289(0x0) = SUB v87f288(0x1), v87f27f(0x1)
    0x28a0x87f: v87f28a = NOT v87f289(0x0)
    0x28b0x87f: v87f28b = AND v87f28a, v87f27e
    0x28d0x87f: MSTORE v87f27c, v87f28b
    0x28e0x87f: v87f28e(0x20) = CONST 
    0x2900x87f: v87f290 = ADD v87f28e(0x20), v87f27c

    Begin block 0x2570x87f
    prev=[0x24e0x87f], succ=[0x24e0x87f]
    =================================
    0x2570x87f_0x0: v25787f_0 = PHI v905(0x20), v87f261
    0x2590x87f: v87f259 = ADD v25787f_0, v8ee
    0x25a0x87f: v87f25a = MLOAD v87f259
    0x25d0x87f: v87f25d = ADD v25787f_0, v8ea
    0x25e0x87f: MSTORE v87f25d, v87f25a
    0x25f0x87f: v87f25f(0x20) = CONST 
    0x2610x87f: v87f261 = ADD v87f25f(0x20), v25787f_0
    0x2620x87f: v87f262(0x24e) = CONST 
    0x2650x87f: JUMP v87f262(0x24e)

    Begin block 0xdad
    prev=[0x87f], succ=[]
    =================================
    0xdaf: RETURNPRIVATE v87farg0

}

function 0x94c(0x94carg0x0, 0x94carg0x1) private {
    Begin block 0x94c
    prev=[], succ=[0x981, 0x985]
    =================================
    0x94e: v94e(0x1) = CONST 
    0x950: v950(0x1) = CONST 
    0x952: v952(0xa0) = CONST 
    0x954: v954(0x10000000000000000000000000000000000000000) = SHL v952(0xa0), v950(0x1)
    0x955: v955(0xffffffffffffffffffffffffffffffffffffffff) = SUB v954(0x10000000000000000000000000000000000000000), v94e(0x1)
    0x956: v956 = AND v955(0xffffffffffffffffffffffffffffffffffffffff), v94carg0
    0x957: v957(0xea77307) = CONST 
    0x95c: v95c(0x40) = CONST 
    0x95e: v95e = MLOAD v95c(0x40)
    0x960: v960(0xffffffff) = CONST 
    0x965: v965(0xea77307) = AND v960(0xffffffff), v957(0xea77307)
    0x966: v966(0xe0) = CONST 
    0x968: v968(0xea7730700000000000000000000000000000000000000000000000000000000) = SHL v966(0xe0), v965(0xea77307)
    0x96a: MSTORE v95e, v968(0xea7730700000000000000000000000000000000000000000000000000000000)
    0x96b: v96b(0x4) = CONST 
    0x96d: v96d = ADD v96b(0x4), v95e
    0x96e: v96e(0x20) = CONST 
    0x970: v970(0x40) = CONST 
    0x972: v972 = MLOAD v970(0x40)
    0x975: v975(0x4) = SUB v96d, v972
    0x979: v979 = EXTCODESIZE v956
    0x97a: v97a = ISZERO v979
    0x97c: v97c = ISZERO v97a
    0x97d: v97d(0x985) = CONST 
    0x980: JUMPI v97d(0x985), v97c

    Begin block 0x981
    prev=[0x94c], succ=[]
    =================================
    0x981: v981(0x0) = CONST 
    0x984: REVERT v981(0x0), v981(0x0)

    Begin block 0x985
    prev=[0x94c], succ=[0x990, 0x999]
    =================================
    0x987: v987 = GAS 
    0x988: v988 = STATICCALL v987, v956, v972, v975(0x4), v972, v96e(0x20)
    0x989: v989 = ISZERO v988
    0x98b: v98b = ISZERO v989
    0x98c: v98c(0x999) = CONST 
    0x98f: JUMPI v98c(0x999), v98b

    Begin block 0x990
    prev=[0x985], succ=[]
    =================================
    0x990: v990 = RETURNDATASIZE 
    0x991: v991(0x0) = CONST 
    0x994: RETURNDATACOPY v991(0x0), v991(0x0), v990
    0x995: v995 = RETURNDATASIZE 
    0x996: v996(0x0) = CONST 
    0x998: REVERT v996(0x0), v995

    Begin block 0x999
    prev=[0x985], succ=[0x9ab, 0x9af]
    =================================
    0x99e: v99e(0x40) = CONST 
    0x9a0: v9a0 = MLOAD v99e(0x40)
    0x9a1: v9a1 = RETURNDATASIZE 
    0x9a2: v9a2(0x20) = CONST 
    0x9a5: v9a5 = LT v9a1, v9a2(0x20)
    0x9a6: v9a6 = ISZERO v9a5
    0x9a7: v9a7(0x9af) = CONST 
    0x9aa: JUMPI v9a7(0x9af), v9a6

    Begin block 0x9ab
    prev=[0x999], succ=[]
    =================================
    0x9ab: v9ab(0x0) = CONST 
    0x9ae: REVERT v9ab(0x0), v9ab(0x0)

    Begin block 0x9af
    prev=[0x999], succ=[0x9bb, 0x9f1]
    =================================
    0x9b1: v9b1 = MLOAD v9a0
    0x9b2: v9b2 = ISZERO v9b1
    0x9b3: v9b3 = ISZERO v9b2
    0x9b4: v9b4(0x1) = CONST 
    0x9b6: v9b6 = EQ v9b4(0x1), v9b3
    0x9b7: v9b7(0x9f1) = CONST 
    0x9ba: JUMPI v9b7(0x9f1), v9b6

    Begin block 0x9bb
    prev=[0x9af], succ=[]
    =================================
    0x9bb: v9bb(0x40) = CONST 
    0x9bd: v9bd = MLOAD v9bb(0x40)
    0x9be: v9be(0x461bcd) = CONST 
    0x9c2: v9c2(0xe5) = CONST 
    0x9c4: v9c4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v9c2(0xe5), v9be(0x461bcd)
    0x9c6: MSTORE v9bd, v9c4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9c7: v9c7(0x4) = CONST 
    0x9c9: v9c9 = ADD v9c7(0x4), v9bd
    0x9cc: v9cc(0x20) = CONST 
    0x9ce: v9ce = ADD v9cc(0x20), v9c9
    0x9d1: v9d1(0x20) = SUB v9ce, v9c9
    0x9d3: MSTORE v9c9, v9d1(0x20)
    0x9d4: v9d4(0x48) = CONST 
    0x9d7: MSTORE v9ce, v9d4(0x48)
    0x9d8: v9d8(0x20) = CONST 
    0x9da: v9da = ADD v9d8(0x20), v9ce
    0x9dc: v9dc(0xa1a) = CONST 
    0x9df: v9df(0x48) = CONST 
    0x9e2: CODECOPY v9da, v9dc(0xa1a), v9df(0x48)
    0x9e3: v9e3(0x60) = CONST 
    0x9e5: v9e5 = ADD v9e3(0x60), v9da
    0x9e9: v9e9(0x40) = CONST 
    0x9eb: v9eb = MLOAD v9e9(0x40)
    0x9ee: v9ee(0xa4) = SUB v9e5, v9eb
    0x9f0: REVERT v9eb, v9ee(0xa4)

    Begin block 0x9f1
    prev=[0x9af], succ=[]
    =================================
    0x9f2: v9f2(0x33) = CONST 
    0x9f5: v9f5 = SLOAD v9f2(0x33)
    0x9f6: v9f6(0x1) = CONST 
    0x9f8: v9f8(0x1) = CONST 
    0x9fa: v9fa(0xa0) = CONST 
    0x9fc: v9fc(0x10000000000000000000000000000000000000000) = SHL v9fa(0xa0), v9f8(0x1)
    0x9fd: v9fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9fc(0x10000000000000000000000000000000000000000), v9f6(0x1)
    0xa00: va00 = AND v94carg0, v9fd(0xffffffffffffffffffffffffffffffffffffffff)
    0xa01: va01(0x100) = CONST 
    0xa04: va04 = MUL va01(0x100), va00
    0xa05: va05(0x100) = CONST 
    0xa08: va08(0x1) = CONST 
    0xa0a: va0a(0xa8) = CONST 
    0xa0c: va0c(0x1000000000000000000000000000000000000000000) = SHL va0a(0xa8), va08(0x1)
    0xa0d: va0d(0xffffffffffffffffffffffffffffffffffffffff00) = SUB va0c(0x1000000000000000000000000000000000000000000), va05(0x100)
    0xa0e: va0e(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT va0d(0xffffffffffffffffffffffffffffffffffffffff00)
    0xa11: va11 = AND v9f5, va0e(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff)
    0xa15: va15 = OR va11, va04
    0xa17: SSTORE v9f2(0x33), va15
    0xa18: RETURNPRIVATE v94carg1

}

function setRecipientAddress(bytes32)() public {
    Begin block 0xa3
    prev=[], succ=[0xb5, 0xb9]
    =================================
    0xa4: va4(0xba4) = CONST 
    0xa7: va7(0x4) = CONST 
    0xaa: vaa = CALLDATASIZE 
    0xab: vab = SUB vaa, va7(0x4)
    0xac: vac(0x20) = CONST 
    0xaf: vaf = LT vab, vac(0x20)
    0xb0: vb0 = ISZERO vaf
    0xb1: vb1(0xb9) = CONST 
    0xb4: JUMPI vb1(0xb9), vb0

    Begin block 0xb5
    prev=[0xa3], succ=[]
    =================================
    0xb5: vb5(0x0) = CONST 
    0xb8: REVERT vb5(0x0), vb5(0x0)

    Begin block 0xb9
    prev=[0xa3], succ=[0x1cd]
    =================================
    0xbb: vbb = CALLDATALOAD va7(0x4)
    0xbc: vbc(0x1cd) = CONST 
    0xbf: JUMP vbc(0x1cd)

    Begin block 0x1cd
    prev=[0xb9], succ=[0x1d5]
    =================================
    0x1ce: v1ce(0x1d5) = CONST 
    0x1d1: v1d1(0x87f) = CONST 
    0x1d4: CALLPRIVATE v1d1(0x87f), v1ce(0x1d5)

    Begin block 0x1d5
    prev=[0x1cd], succ=[0x21e, 0x2a1]
    =================================
    0x1d6: v1d6(0x33) = CONST 
    0x1d8: v1d8(0x1) = CONST 
    0x1db: v1db = SLOAD v1d6(0x33)
    0x1dd: v1dd(0x100) = CONST 
    0x1e0: v1e0(0x100) = EXP v1dd(0x100), v1d8(0x1)
    0x1e2: v1e2 = DIV v1db, v1e0(0x100)
    0x1e3: v1e3(0x1) = CONST 
    0x1e5: v1e5(0x1) = CONST 
    0x1e7: v1e7(0xa0) = CONST 
    0x1e9: v1e9(0x10000000000000000000000000000000000000000) = SHL v1e7(0xa0), v1e5(0x1)
    0x1ea: v1ea(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e9(0x10000000000000000000000000000000000000000), v1e3(0x1)
    0x1eb: v1eb = AND v1ea(0xffffffffffffffffffffffffffffffffffffffff), v1e2
    0x1ec: v1ec(0x1) = CONST 
    0x1ee: v1ee(0x1) = CONST 
    0x1f0: v1f0(0xa0) = CONST 
    0x1f2: v1f2(0x10000000000000000000000000000000000000000) = SHL v1f0(0xa0), v1ee(0x1)
    0x1f3: v1f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f2(0x10000000000000000000000000000000000000000), v1ec(0x1)
    0x1f4: v1f4 = AND v1f3(0xffffffffffffffffffffffffffffffffffffffff), v1eb
    0x1f5: v1f5 = CALLER 
    0x1f6: v1f6(0x1) = CONST 
    0x1f8: v1f8(0x1) = CONST 
    0x1fa: v1fa(0xa0) = CONST 
    0x1fc: v1fc(0x10000000000000000000000000000000000000000) = SHL v1fa(0xa0), v1f8(0x1)
    0x1fd: v1fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fc(0x10000000000000000000000000000000000000000), v1f6(0x1)
    0x1fe: v1fe = AND v1fd(0xffffffffffffffffffffffffffffffffffffffff), v1f5
    0x1ff: v1ff = EQ v1fe, v1f4
    0x200: v200(0x40) = CONST 
    0x202: v202 = MLOAD v200(0x40)
    0x204: v204(0x60) = CONST 
    0x206: v206 = ADD v204(0x60), v202
    0x207: v207(0x40) = CONST 
    0x209: MSTORE v207(0x40), v206
    0x20b: v20b(0x22) = CONST 
    0x20e: MSTORE v202, v20b(0x22)
    0x20f: v20f(0x20) = CONST 
    0x211: v211 = ADD v20f(0x20), v202
    0x212: v212(0xaba) = CONST 
    0x215: v215(0x22) = CONST 
    0x218: CODECOPY v211, v212(0xaba), v215(0x22)
    0x21a: v21a(0x2a1) = CONST 
    0x21d: JUMPI v21a(0x2a1), v1ff

    Begin block 0x21e
    prev=[0x1d5], succ=[0x24e0xa3]
    =================================
    0x21e: v21e(0x40) = CONST 
    0x220: v220 = MLOAD v21e(0x40)
    0x221: v221(0x461bcd) = CONST 
    0x225: v225(0xe5) = CONST 
    0x227: v227(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v225(0xe5), v221(0x461bcd)
    0x229: MSTORE v220, v227(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22a: v22a(0x4) = CONST 
    0x22c: v22c = ADD v22a(0x4), v220
    0x22f: v22f(0x20) = CONST 
    0x231: v231 = ADD v22f(0x20), v22c
    0x234: v234(0x20) = SUB v231, v22c
    0x236: MSTORE v22c, v234(0x20)
    0x23a: v23a(0x22) = MLOAD v202
    0x23c: MSTORE v231, v23a(0x22)
    0x23d: v23d(0x20) = CONST 
    0x23f: v23f = ADD v23d(0x20), v231
    0x243: v243(0x22) = MLOAD v202
    0x245: v245(0x20) = CONST 
    0x247: v247 = ADD v245(0x20), v202
    0x24c: v24c(0x0) = CONST 

    Begin block 0x24e0xa3
    prev=[0x21e, 0x2570xa3], succ=[0x2660xa3, 0x2570xa3]
    =================================
    0x24e0xa3_0x0: v24ea3_0 = PHI v24c(0x0), va3261
    0x2510xa3: va3251 = LT v24ea3_0, v243(0x22)
    0x2520xa3: va3252 = ISZERO va3251
    0x2530xa3: va3253(0x266) = CONST 
    0x2560xa3: JUMPI va3253(0x266), va3252

    Begin block 0x2660xa3
    prev=[0x24e0xa3], succ=[0x2930xa3, 0x27a0xa3]
    =================================
    0x26f0xa3: va326f = ADD v243(0x22), v23f
    0x2710xa3: va3271(0x1f) = CONST 
    0x2730xa3: va3273(0x2) = AND va3271(0x1f), v243(0x22)
    0x2750xa3: va3275 = ISZERO va3273(0x2)
    0x2760xa3: va3276(0x293) = CONST 
    0x2790xa3: JUMPI va3276(0x293), va3275

    Begin block 0x2930xa3
    prev=[0x2660xa3, 0x27a0xa3], succ=[]
    =================================
    0x2930xa3_0x1: v293a3_1 = PHI va3290, va326f
    0x2990xa3: va3299(0x40) = CONST 
    0x29b0xa3: va329b = MLOAD va3299(0x40)
    0x29e0xa3: va329e = SUB v293a3_1, va329b
    0x2a00xa3: REVERT va329b, va329e

    Begin block 0x27a0xa3
    prev=[0x2660xa3], succ=[0x2930xa3]
    =================================
    0x27c0xa3: va327c = SUB va326f, va3273(0x2)
    0x27e0xa3: va327e = MLOAD va327c
    0x27f0xa3: va327f(0x1) = CONST 
    0x2820xa3: va3282(0x20) = CONST 
    0x2840xa3: va3284(0x1e) = SUB va3282(0x20), va3273(0x2)
    0x2850xa3: va3285(0x100) = CONST 
    0x2880xa3: va3288(0x1000000000000000000000000000000000000000000000000000000000000) = EXP va3285(0x100), va3284(0x1e)
    0x2890xa3: va3289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB va3288(0x1000000000000000000000000000000000000000000000000000000000000), va327f(0x1)
    0x28a0xa3: va328a = NOT va3289(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x28b0xa3: va328b = AND va328a, va327e
    0x28d0xa3: MSTORE va327c, va328b
    0x28e0xa3: va328e(0x20) = CONST 
    0x2900xa3: va3290 = ADD va328e(0x20), va327c

    Begin block 0x2570xa3
    prev=[0x24e0xa3], succ=[0x24e0xa3]
    =================================
    0x2570xa3_0x0: v257a3_0 = PHI v24c(0x0), va3261
    0x2590xa3: va3259 = ADD v257a3_0, v247
    0x25a0xa3: va325a = MLOAD va3259
    0x25d0xa3: va325d = ADD v257a3_0, v23f
    0x25e0xa3: MSTORE va325d, va325a
    0x25f0xa3: va325f(0x20) = CONST 
    0x2610xa3: va3261 = ADD va325f(0x20), v257a3_0
    0x2620xa3: va3262(0x24e) = CONST 
    0x2650xa3: JUMP va3262(0x24e)

    Begin block 0x2a1
    prev=[0x1d5], succ=[0xba4]
    =================================
    0x2a3: v2a3(0x36) = CONST 
    0x2a5: SSTORE v2a3(0x36), vbb
    0x2a6: JUMP va4(0xba4)

    Begin block 0xba4
    prev=[0x2a1], succ=[]
    =================================
    0xba5: STOP 

}

function fallback()() public {
    Begin block 0xb5c
    prev=[], succ=[]
    =================================
    0xb5d: vb5d(0x0) = CONST 
    0xb60: REVERT vb5d(0x0), vb5d(0x0)

}

function transferToSolana(uint32)() public {
    Begin block 0xc2
    prev=[], succ=[0xd4, 0xd8]
    =================================
    0xc3: vc3(0xbc5) = CONST 
    0xc6: vc6(0x4) = CONST 
    0xc9: vc9 = CALLDATASIZE 
    0xca: vca = SUB vc9, vc6(0x4)
    0xcb: vcb(0x20) = CONST 
    0xce: vce = LT vca, vcb(0x20)
    0xcf: vcf = ISZERO vce
    0xd0: vd0(0xd8) = CONST 
    0xd3: JUMPI vd0(0xd8), vcf

    Begin block 0xd4
    prev=[0xc2], succ=[]
    =================================
    0xd4: vd4(0x0) = CONST 
    0xd7: REVERT vd4(0x0), vd4(0x0)

    Begin block 0xd8
    prev=[0xc2], succ=[0x2a7]
    =================================
    0xda: vda = CALLDATALOAD vc6(0x4)
    0xdb: vdb(0xffffffff) = CONST 
    0xe0: ve0 = AND vdb(0xffffffff), vda
    0xe1: ve1(0x2a7) = CONST 
    0xe4: JUMP ve1(0x2a7)

    Begin block 0x2a7
    prev=[0xd8], succ=[0x2af]
    =================================
    0x2a8: v2a8(0x2af) = CONST 
    0x2ab: v2ab(0x87f) = CONST 
    0x2ae: CALLPRIVATE v2ab(0x87f), v2a8(0x2af)

    Begin block 0x2af
    prev=[0x2a7], succ=[0x2f6, 0x2fa]
    =================================
    0x2b0: v2b0(0x34) = CONST 
    0x2b2: v2b2 = SLOAD v2b0(0x34)
    0x2b3: v2b3(0x40) = CONST 
    0x2b6: v2b6 = MLOAD v2b3(0x40)
    0x2b7: v2b7(0x70a08231) = CONST 
    0x2bc: v2bc(0xe0) = CONST 
    0x2be: v2be(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v2bc(0xe0), v2b7(0x70a08231)
    0x2c0: MSTORE v2b6, v2be(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x2c1: v2c1 = ADDRESS 
    0x2c2: v2c2(0x4) = CONST 
    0x2c5: v2c5 = ADD v2b6, v2c2(0x4)
    0x2c6: MSTORE v2c5, v2c1
    0x2c8: v2c8 = MLOAD v2b3(0x40)
    0x2c9: v2c9(0x0) = CONST 
    0x2cc: v2cc(0x1) = CONST 
    0x2ce: v2ce(0x1) = CONST 
    0x2d0: v2d0(0xa0) = CONST 
    0x2d2: v2d2(0x10000000000000000000000000000000000000000) = SHL v2d0(0xa0), v2ce(0x1)
    0x2d3: v2d3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d2(0x10000000000000000000000000000000000000000), v2cc(0x1)
    0x2d4: v2d4 = AND v2d3(0xffffffffffffffffffffffffffffffffffffffff), v2b2
    0x2d6: v2d6(0x70a08231) = CONST 
    0x2dc: v2dc(0x24) = CONST 
    0x2e0: v2e0 = ADD v2b6, v2dc(0x24)
    0x2e2: v2e2(0x20) = CONST 
    0x2e9: v2e9(0x0) = SUB v2b6, v2c8
    0x2ea: v2ea(0x24) = ADD v2e9(0x0), v2dc(0x24)
    0x2ee: v2ee = EXTCODESIZE v2d4
    0x2ef: v2ef = ISZERO v2ee
    0x2f1: v2f1 = ISZERO v2ef
    0x2f2: v2f2(0x2fa) = CONST 
    0x2f5: JUMPI v2f2(0x2fa), v2f1

    Begin block 0x2f6
    prev=[0x2af], succ=[]
    =================================
    0x2f6: v2f6(0x0) = CONST 
    0x2f9: REVERT v2f6(0x0), v2f6(0x0)

    Begin block 0x2fa
    prev=[0x2af], succ=[0x305, 0x30e]
    =================================
    0x2fc: v2fc = GAS 
    0x2fd: v2fd = STATICCALL v2fc, v2d4, v2c8, v2ea(0x24), v2c8, v2e2(0x20)
    0x2fe: v2fe = ISZERO v2fd
    0x300: v300 = ISZERO v2fe
    0x301: v301(0x30e) = CONST 
    0x304: JUMPI v301(0x30e), v300

    Begin block 0x305
    prev=[0x2fa], succ=[]
    =================================
    0x305: v305 = RETURNDATASIZE 
    0x306: v306(0x0) = CONST 
    0x309: RETURNDATACOPY v306(0x0), v306(0x0), v305
    0x30a: v30a = RETURNDATASIZE 
    0x30b: v30b(0x0) = CONST 
    0x30d: REVERT v30b(0x0), v30a

    Begin block 0x30e
    prev=[0x2fa], succ=[0x320, 0x324]
    =================================
    0x313: v313(0x40) = CONST 
    0x315: v315 = MLOAD v313(0x40)
    0x316: v316 = RETURNDATASIZE 
    0x317: v317(0x20) = CONST 
    0x31a: v31a = LT v316, v317(0x20)
    0x31b: v31b = ISZERO v31a
    0x31c: v31c(0x324) = CONST 
    0x31f: JUMPI v31c(0x324), v31b

    Begin block 0x320
    prev=[0x30e], succ=[]
    =================================
    0x320: v320(0x0) = CONST 
    0x323: REVERT v320(0x0), v320(0x0)

    Begin block 0x324
    prev=[0x30e], succ=[0x37d, 0x381]
    =================================
    0x326: v326 = MLOAD v315
    0x327: v327(0x34) = CONST 
    0x329: v329 = SLOAD v327(0x34)
    0x32a: v32a(0x35) = CONST 
    0x32c: v32c = SLOAD v32a(0x35)
    0x32d: v32d(0x40) = CONST 
    0x330: v330 = MLOAD v32d(0x40)
    0x331: v331(0x95ea7b3) = CONST 
    0x336: v336(0xe0) = CONST 
    0x338: v338(0x95ea7b300000000000000000000000000000000000000000000000000000000) = SHL v336(0xe0), v331(0x95ea7b3)
    0x33a: MSTORE v330, v338(0x95ea7b300000000000000000000000000000000000000000000000000000000)
    0x33b: v33b(0x1) = CONST 
    0x33d: v33d(0x1) = CONST 
    0x33f: v33f(0xa0) = CONST 
    0x341: v341(0x10000000000000000000000000000000000000000) = SHL v33f(0xa0), v33d(0x1)
    0x342: v342(0xffffffffffffffffffffffffffffffffffffffff) = SUB v341(0x10000000000000000000000000000000000000000), v33b(0x1)
    0x345: v345 = AND v342(0xffffffffffffffffffffffffffffffffffffffff), v32c
    0x346: v346(0x4) = CONST 
    0x349: v349 = ADD v330, v346(0x4)
    0x34a: MSTORE v349, v345
    0x34b: v34b(0x24) = CONST 
    0x34e: v34e = ADD v330, v34b(0x24)
    0x351: MSTORE v34e, v326
    0x353: v353 = MLOAD v32d(0x40)
    0x358: v358 = AND v329, v342(0xffffffffffffffffffffffffffffffffffffffff)
    0x35a: v35a(0x95ea7b3) = CONST 
    0x360: v360(0x44) = CONST 
    0x364: v364 = ADD v330, v360(0x44)
    0x366: v366(0x20) = CONST 
    0x36e: v36e(0x0) = SUB v330, v353
    0x36f: v36f(0x44) = ADD v36e(0x0), v360(0x44)
    0x371: v371(0x0) = CONST 
    0x375: v375 = EXTCODESIZE v358
    0x376: v376 = ISZERO v375
    0x378: v378 = ISZERO v376
    0x379: v379(0x381) = CONST 
    0x37c: JUMPI v379(0x381), v378

    Begin block 0x37d
    prev=[0x324], succ=[]
    =================================
    0x37d: v37d(0x0) = CONST 
    0x380: REVERT v37d(0x0), v37d(0x0)

    Begin block 0x381
    prev=[0x324], succ=[0x38c, 0x395]
    =================================
    0x383: v383 = GAS 
    0x384: v384 = CALL v383, v358, v371(0x0), v353, v36f(0x44), v353, v366(0x20)
    0x385: v385 = ISZERO v384
    0x387: v387 = ISZERO v385
    0x388: v388(0x395) = CONST 
    0x38b: JUMPI v388(0x395), v387

    Begin block 0x38c
    prev=[0x381], succ=[]
    =================================
    0x38c: v38c = RETURNDATASIZE 
    0x38d: v38d(0x0) = CONST 
    0x390: RETURNDATACOPY v38d(0x0), v38d(0x0), v38c
    0x391: v391 = RETURNDATASIZE 
    0x392: v392(0x0) = CONST 
    0x394: REVERT v392(0x0), v391

    Begin block 0x395
    prev=[0x381], succ=[0x3a7, 0x3ab]
    =================================
    0x39a: v39a(0x40) = CONST 
    0x39c: v39c = MLOAD v39a(0x40)
    0x39d: v39d = RETURNDATASIZE 
    0x39e: v39e(0x20) = CONST 
    0x3a1: v3a1 = LT v39d, v39e(0x20)
    0x3a2: v3a2 = ISZERO v3a1
    0x3a3: v3a3(0x3ab) = CONST 
    0x3a6: JUMPI v3a3(0x3ab), v3a2

    Begin block 0x3a7
    prev=[0x395], succ=[]
    =================================
    0x3a7: v3a7(0x0) = CONST 
    0x3aa: REVERT v3a7(0x0), v3a7(0x0)

    Begin block 0x3ab
    prev=[0x395], succ=[0x425, 0x429]
    =================================
    0x3ae: v3ae(0x35) = CONST 
    0x3b0: v3b0 = SLOAD v3ae(0x35)
    0x3b1: v3b1(0x34) = CONST 
    0x3b3: v3b3 = SLOAD v3b1(0x34)
    0x3b4: v3b4(0x36) = CONST 
    0x3b6: v3b6 = SLOAD v3b4(0x36)
    0x3b7: v3b7(0x40) = CONST 
    0x3ba: v3ba = MLOAD v3b7(0x40)
    0x3bb: v3bb(0x38389cb) = CONST 
    0x3c0: v3c0(0xe5) = CONST 
    0x3c2: v3c2(0x7071396000000000000000000000000000000000000000000000000000000000) = SHL v3c0(0xe5), v3bb(0x38389cb)
    0x3c4: MSTORE v3ba, v3c2(0x7071396000000000000000000000000000000000000000000000000000000000)
    0x3c5: v3c5(0x1) = CONST 
    0x3c7: v3c7(0x1) = CONST 
    0x3c9: v3c9(0xa0) = CONST 
    0x3cb: v3cb(0x10000000000000000000000000000000000000000) = SHL v3c9(0xa0), v3c7(0x1)
    0x3cc: v3cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3cb(0x10000000000000000000000000000000000000000), v3c5(0x1)
    0x3cf: v3cf = AND v3cc(0xffffffffffffffffffffffffffffffffffffffff), v3b3
    0x3d0: v3d0(0x4) = CONST 
    0x3d3: v3d3 = ADD v3ba, v3d0(0x4)
    0x3d4: MSTORE v3d3, v3cf
    0x3d5: v3d5(0x24) = CONST 
    0x3d8: v3d8 = ADD v3ba, v3d5(0x24)
    0x3db: MSTORE v3d8, v326
    0x3dc: v3dc(0x44) = CONST 
    0x3df: v3df = ADD v3ba, v3dc(0x44)
    0x3e3: MSTORE v3df, v3b6
    0x3e4: v3e4(0x1) = CONST 
    0x3e6: v3e6(0x64) = CONST 
    0x3e9: v3e9 = ADD v3ba, v3e6(0x64)
    0x3ec: MSTORE v3e9, v3e4(0x1)
    0x3ed: v3ed(0xffffffff) = CONST 
    0x3f3: v3f3 = AND ve0, v3ed(0xffffffff)
    0x3f4: v3f4(0x84) = CONST 
    0x3f7: v3f7 = ADD v3ba, v3f4(0x84)
    0x3f8: MSTORE v3f7, v3f3
    0x3f9: v3f9(0xa4) = CONST 
    0x3fc: v3fc = ADD v3ba, v3f9(0xa4)
    0x3fd: MSTORE v3fc, v3e4(0x1)
    0x3fe: v3fe = MLOAD v3b7(0x40)
    0x402: v402 = AND v3b0, v3cc(0xffffffffffffffffffffffffffffffffffffffff)
    0x404: v404(0x70713960) = CONST 
    0x40a: v40a(0xc4) = CONST 
    0x40e: v40e = ADD v3ba, v40a(0xc4)
    0x410: v410(0x0) = CONST 
    0x417: v417(0x0) = SUB v3ba, v3fe
    0x418: v418(0xc4) = ADD v417(0x0), v40a(0xc4)
    0x41d: v41d = EXTCODESIZE v402
    0x41e: v41e = ISZERO v41d
    0x420: v420 = ISZERO v41e
    0x421: v421(0x429) = CONST 
    0x424: JUMPI v421(0x429), v420

    Begin block 0x425
    prev=[0x3ab], succ=[]
    =================================
    0x425: v425(0x0) = CONST 
    0x428: REVERT v425(0x0), v425(0x0)

    Begin block 0x429
    prev=[0x3ab], succ=[0x434, 0xd1b]
    =================================
    0x42b: v42b = GAS 
    0x42c: v42c = CALL v42b, v402, v410(0x0), v3fe, v418(0xc4), v3fe, v410(0x0)
    0x42d: v42d = ISZERO v42c
    0x42f: v42f = ISZERO v42d
    0x430: v430(0xd1b) = CONST 
    0x433: JUMPI v430(0xd1b), v42f

    Begin block 0x434
    prev=[0x429], succ=[]
    =================================
    0x434: v434 = RETURNDATASIZE 
    0x435: v435(0x0) = CONST 
    0x438: RETURNDATACOPY v435(0x0), v435(0x0), v434
    0x439: v439 = RETURNDATASIZE 
    0x43a: v43a(0x0) = CONST 
    0x43c: REVERT v43a(0x0), v439

    Begin block 0xd1b
    prev=[0x429], succ=[0xbc5]
    =================================
    0xd22: JUMP vc3(0xbc5)

    Begin block 0xbc5
    prev=[0xd1b], succ=[]
    =================================
    0xbc6: STOP 

}

function antiAbuseOracleAddress()() public {
    Begin block 0xe5
    prev=[], succ=[0x445]
    =================================
    0xe6: ve6(0xbe6) = CONST 
    0xe9: ve9(0x445) = CONST 
    0xec: JUMP ve9(0x445)

    Begin block 0x445
    prev=[0xe5], succ=[0xbe6]
    =================================
    0x446: v446(0x37) = CONST 
    0x448: v448 = SLOAD v446(0x37)
    0x449: v449(0x1) = CONST 
    0x44b: v44b(0x1) = CONST 
    0x44d: v44d(0xa0) = CONST 
    0x44f: v44f(0x10000000000000000000000000000000000000000) = SHL v44d(0xa0), v44b(0x1)
    0x450: v450(0xffffffffffffffffffffffffffffffffffffffff) = SUB v44f(0x10000000000000000000000000000000000000000), v449(0x1)
    0x451: v451 = AND v450(0xffffffffffffffffffffffffffffffffffffffff), v448
    0x453: JUMP ve6(0xbe6)

    Begin block 0xbe6
    prev=[0x445], succ=[]
    =================================
    0xbe7: vbe7(0x40) = CONST 
    0xbea: vbea = MLOAD vbe7(0x40)
    0xbeb: vbeb(0x1) = CONST 
    0xbed: vbed(0x1) = CONST 
    0xbef: vbef(0xa0) = CONST 
    0xbf1: vbf1(0x10000000000000000000000000000000000000000) = SHL vbef(0xa0), vbed(0x1)
    0xbf2: vbf2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbf1(0x10000000000000000000000000000000000000000), vbeb(0x1)
    0xbf5: vbf5 = AND v451, vbf2(0xffffffffffffffffffffffffffffffffffffffff)
    0xbf7: MSTORE vbea, vbf5
    0xbf8: vbf8 = MLOAD vbe7(0x40)
    0xbfc: vbfc(0x0) = SUB vbea, vbf8
    0xbfd: vbfd(0x20) = CONST 
    0xbff: vbff(0x20) = ADD vbfd(0x20), vbfc(0x0)
    0xc01: RETURN vbf8, vbff(0x20)

}

