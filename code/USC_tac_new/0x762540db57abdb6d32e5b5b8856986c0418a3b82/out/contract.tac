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
    prev=[0x0], succ=[0x1a, 0x82c]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x81e: v81e(0x82c) = CONST 
    0x81f: JUMPI v81e(0x82c), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x82f, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x5536b682) = CONST 
    0x26: v26 = EQ v21(0x5536b682), v1f
    0x820: v820(0x82f) = CONST 
    0x821: JUMPI v820(0x82f), v26

    Begin block 0x82f
    prev=[0x1a], succ=[]
    =================================
    0x830: v830(0x67) = CONST 
    0x831: CALLPRIVATE v830(0x67)

    Begin block 0x2b
    prev=[0x1a], succ=[0x832, 0x36]
    =================================
    0x2c: v2c(0x6e699d87) = CONST 
    0x31: v31 = EQ v2c(0x6e699d87), v1f
    0x822: v822(0x832) = CONST 
    0x823: JUMPI v822(0x832), v31

    Begin block 0x832
    prev=[0x2b], succ=[]
    =================================
    0x833: v833(0xa7) = CONST 
    0x834: CALLPRIVATE v833(0xa7)

    Begin block 0x36
    prev=[0x2b], succ=[0x835, 0x41]
    =================================
    0x37: v37(0x7b103999) = CONST 
    0x3c: v3c = EQ v37(0x7b103999), v1f
    0x824: v824(0x835) = CONST 
    0x825: JUMPI v824(0x835), v3c

    Begin block 0x835
    prev=[0x36], succ=[]
    =================================
    0x836: v836(0xdf) = CONST 
    0x837: CALLPRIVATE v836(0xdf)

    Begin block 0x41
    prev=[0x36], succ=[0x838, 0x4c]
    =================================
    0x42: v42(0xabf158d5) = CONST 
    0x47: v47 = EQ v42(0xabf158d5), v1f
    0x826: v826(0x838) = CONST 
    0x827: JUMPI v826(0x838), v47

    Begin block 0x838
    prev=[0x41], succ=[]
    =================================
    0x839: v839(0x103) = CONST 
    0x83a: CALLPRIVATE v839(0x103)

    Begin block 0x4c
    prev=[0x41], succ=[0x83b, 0x57]
    =================================
    0x4d: v4d(0xc4d66de8) = CONST 
    0x52: v52 = EQ v4d(0xc4d66de8), v1f
    0x828: v828(0x83b) = CONST 
    0x829: JUMPI v828(0x83b), v52

    Begin block 0x83b
    prev=[0x4c], succ=[]
    =================================
    0x83c: v83c(0x12c) = CONST 
    0x83d: CALLPRIVATE v83c(0x12c)

    Begin block 0x57
    prev=[0x4c], succ=[0x82c, 0x83e]
    =================================
    0x58: v58(0xc98cc002) = CONST 
    0x5d: v5d = EQ v58(0xc98cc002), v1f
    0x82a: v82a(0x83e) = CONST 
    0x82b: JUMPI v82a(0x83e), v5d

    Begin block 0x82c
    prev=[0x10, 0x57], succ=[]
    =================================
    0x82d: v82d(0x62) = CONST 
    0x82e: CALLPRIVATE v82d(0x62)

    Begin block 0x83e
    prev=[0x57], succ=[]
    =================================
    0x83f: v83f(0x152) = CONST 
    0x840: CALLPRIVATE v83f(0x152)

}

function logRewardParams(uint256,uint256,uint256)() public {
    Begin block 0x103
    prev=[], succ=[0x115, 0x119]
    =================================
    0x104: v104(0x7da) = CONST 
    0x107: v107(0x4) = CONST 
    0x10a: v10a = CALLDATASIZE 
    0x10b: v10b = SUB v10a, v107(0x4)
    0x10c: v10c(0x60) = CONST 
    0x10f: v10f = LT v10b, v10c(0x60)
    0x110: v110 = ISZERO v10f
    0x111: v111(0x119) = CONST 
    0x114: JUMPI v111(0x119), v110

    Begin block 0x115
    prev=[0x103], succ=[]
    =================================
    0x115: v115(0x0) = CONST 
    0x118: REVERT v115(0x0), v115(0x0)

    Begin block 0x119
    prev=[0x103], succ=[0x4bb]
    =================================
    0x11c: v11c = CALLDATALOAD v107(0x4)
    0x11e: v11e(0x20) = CONST 
    0x121: v121(0x24) = ADD v107(0x4), v11e(0x20)
    0x122: v122 = CALLDATALOAD v121(0x24)
    0x124: v124(0x40) = CONST 
    0x126: v126(0x44) = ADD v124(0x40), v107(0x4)
    0x127: v127 = CALLDATALOAD v126(0x44)
    0x128: v128(0x4bb) = CONST 
    0x12b: JUMP v128(0x4bb)

    Begin block 0x4bb
    prev=[0x119], succ=[0x500, 0x504]
    =================================
    0x4bc: v4bc(0x0) = CONST 
    0x4be: v4be = SLOAD v4bc(0x0)
    0x4bf: v4bf(0x40) = CONST 
    0x4c2: v4c2 = MLOAD v4bf(0x40)
    0x4c3: v4c3(0xa1ef8f9) = CONST 
    0x4c8: v4c8(0xe2) = CONST 
    0x4ca: v4ca(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v4c8(0xe2), v4c3(0xa1ef8f9)
    0x4cc: MSTORE v4c2, v4ca(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x4ce: v4ce = MLOAD v4bf(0x40)
    0x4cf: v4cf = CALLER 
    0x4d1: v4d1(0x100) = CONST 
    0x4d5: v4d5 = DIV v4be, v4d1(0x100)
    0x4d6: v4d6(0x1) = CONST 
    0x4d8: v4d8(0x1) = CONST 
    0x4da: v4da(0xa0) = CONST 
    0x4dc: v4dc(0x10000000000000000000000000000000000000000) = SHL v4da(0xa0), v4d8(0x1)
    0x4dd: v4dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4dc(0x10000000000000000000000000000000000000000), v4d6(0x1)
    0x4de: v4de = AND v4dd(0xffffffffffffffffffffffffffffffffffffffff), v4d5
    0x4e0: v4e0(0x287be3e4) = CONST 
    0x4e6: v4e6(0x4) = CONST 
    0x4ea: v4ea = ADD v4c2, v4e6(0x4)
    0x4ec: v4ec(0x20) = CONST 
    0x4f3: v4f3(0x0) = SUB v4c2, v4ce
    0x4f4: v4f4(0x4) = ADD v4f3(0x0), v4e6(0x4)
    0x4f8: v4f8 = EXTCODESIZE v4de
    0x4f9: v4f9 = ISZERO v4f8
    0x4fb: v4fb = ISZERO v4f9
    0x4fc: v4fc(0x504) = CONST 
    0x4ff: JUMPI v4fc(0x504), v4fb

    Begin block 0x500
    prev=[0x4bb], succ=[]
    =================================
    0x500: v500(0x0) = CONST 
    0x503: REVERT v500(0x0), v500(0x0)

    Begin block 0x504
    prev=[0x4bb], succ=[0x50f, 0x518]
    =================================
    0x506: v506 = GAS 
    0x507: v507 = STATICCALL v506, v4de, v4ce, v4f4(0x4), v4ce, v4ec(0x20)
    0x508: v508 = ISZERO v507
    0x50a: v50a = ISZERO v508
    0x50b: v50b(0x518) = CONST 
    0x50e: JUMPI v50b(0x518), v50a

    Begin block 0x50f
    prev=[0x504], succ=[]
    =================================
    0x50f: v50f = RETURNDATASIZE 
    0x510: v510(0x0) = CONST 
    0x513: RETURNDATACOPY v510(0x0), v510(0x0), v50f
    0x514: v514 = RETURNDATASIZE 
    0x515: v515(0x0) = CONST 
    0x517: REVERT v515(0x0), v514

    Begin block 0x518
    prev=[0x504], succ=[0x52a, 0x52e]
    =================================
    0x51d: v51d(0x40) = CONST 
    0x51f: v51f = MLOAD v51d(0x40)
    0x520: v520 = RETURNDATASIZE 
    0x521: v521(0x20) = CONST 
    0x524: v524 = LT v520, v521(0x20)
    0x525: v525 = ISZERO v524
    0x526: v526(0x52e) = CONST 
    0x529: JUMPI v526(0x52e), v525

    Begin block 0x52a
    prev=[0x518], succ=[]
    =================================
    0x52a: v52a(0x0) = CONST 
    0x52d: REVERT v52a(0x0), v52a(0x0)

    Begin block 0x52e
    prev=[0x518], succ=[0x53f, 0x575]
    =================================
    0x530: v530 = MLOAD v51f
    0x531: v531(0x1) = CONST 
    0x533: v533(0x1) = CONST 
    0x535: v535(0xa0) = CONST 
    0x537: v537(0x10000000000000000000000000000000000000000) = SHL v535(0xa0), v533(0x1)
    0x538: v538(0xffffffffffffffffffffffffffffffffffffffff) = SUB v537(0x10000000000000000000000000000000000000000), v531(0x1)
    0x539: v539 = AND v538(0xffffffffffffffffffffffffffffffffffffffff), v530
    0x53a: v53a = EQ v539, v4cf
    0x53b: v53b(0x575) = CONST 
    0x53e: JUMPI v53b(0x575), v53a

    Begin block 0x53f
    prev=[0x52e], succ=[]
    =================================
    0x53f: v53f(0x40) = CONST 
    0x541: v541 = MLOAD v53f(0x40)
    0x542: v542(0x461bcd) = CONST 
    0x546: v546(0xe5) = CONST 
    0x548: v548(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v546(0xe5), v542(0x461bcd)
    0x54a: MSTORE v541, v548(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x54b: v54b(0x4) = CONST 
    0x54d: v54d = ADD v54b(0x4), v541
    0x550: v550(0x20) = CONST 
    0x552: v552 = ADD v550(0x20), v54d
    0x555: v555(0x20) = SUB v552, v54d
    0x557: MSTORE v54d, v555(0x20)
    0x558: v558(0x21) = CONST 
    0x55b: MSTORE v552, v558(0x21)
    0x55c: v55c(0x20) = CONST 
    0x55e: v55e = ADD v55c(0x20), v552
    0x560: v560(0x724) = CONST 
    0x563: v563(0x21) = CONST 
    0x566: CODECOPY v55e, v560(0x724), v563(0x21)
    0x567: v567(0x40) = CONST 
    0x569: v569 = ADD v567(0x40), v55e
    0x56d: v56d(0x40) = CONST 
    0x56f: v56f = MLOAD v56d(0x40)
    0x572: v572(0x84) = SUB v569, v56f
    0x574: REVERT v56f, v572(0x84)

    Begin block 0x575
    prev=[0x52e], succ=[0x7da]
    =================================
    0x576: v576(0x40) = CONST 
    0x579: v579 = MLOAD v576(0x40)
    0x57c: MSTORE v579, v11c
    0x57d: v57d(0x20) = CONST 
    0x580: v580 = ADD v579, v57d(0x20)
    0x583: MSTORE v580, v122
    0x586: v586 = ADD v576(0x40), v579
    0x589: MSTORE v586, v127
    0x58b: v58b = MLOAD v576(0x40)
    0x58c: v58c(0x801c2d11f1d1780f228c2a497cf5eae033694c8eb057d636044683def26e03ec) = CONST 
    0x5b0: v5b0(0x0) = SUB v579, v58b
    0x5b1: v5b1(0x60) = CONST 
    0x5b3: v5b3(0x60) = ADD v5b1(0x60), v5b0(0x0)
    0x5b5: LOG1 v58b, v5b3(0x60), v58c(0x801c2d11f1d1780f228c2a497cf5eae033694c8eb057d636044683def26e03ec)
    0x5b9: JUMP v104(0x7da)

    Begin block 0x7da
    prev=[0x575], succ=[]
    =================================
    0x7db: STOP 

}

function initialize(address)() public {
    Begin block 0x12c
    prev=[], succ=[0x13e, 0x142]
    =================================
    0x12d: v12d(0x7fb) = CONST 
    0x130: v130(0x4) = CONST 
    0x133: v133 = CALLDATASIZE 
    0x134: v134 = SUB v133, v130(0x4)
    0x135: v135(0x20) = CONST 
    0x138: v138 = LT v134, v135(0x20)
    0x139: v139 = ISZERO v138
    0x13a: v13a(0x142) = CONST 
    0x13d: JUMPI v13a(0x142), v139

    Begin block 0x13e
    prev=[0x12c], succ=[]
    =================================
    0x13e: v13e(0x0) = CONST 
    0x141: REVERT v13e(0x0), v13e(0x0)

    Begin block 0x142
    prev=[0x12c], succ=[0x5ba]
    =================================
    0x144: v144 = CALLDATALOAD v130(0x4)
    0x145: v145(0x1) = CONST 
    0x147: v147(0x1) = CONST 
    0x149: v149(0xa0) = CONST 
    0x14b: v14b(0x10000000000000000000000000000000000000000) = SHL v149(0xa0), v147(0x1)
    0x14c: v14c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14b(0x10000000000000000000000000000000000000000), v145(0x1)
    0x14d: v14d = AND v14c(0xffffffffffffffffffffffffffffffffffffffff), v144
    0x14e: v14e(0x5ba) = CONST 
    0x151: JUMP v14e(0x5ba)

    Begin block 0x5ba
    prev=[0x142], succ=[0x5c6, 0x603]
    =================================
    0x5bb: v5bb(0x0) = CONST 
    0x5bd: v5bd = SLOAD v5bb(0x0)
    0x5be: v5be(0xff) = CONST 
    0x5c0: v5c0 = AND v5be(0xff), v5bd
    0x5c1: v5c1 = ISZERO v5c0
    0x5c2: v5c2(0x603) = CONST 
    0x5c5: JUMPI v5c2(0x603), v5c1

    Begin block 0x5c6
    prev=[0x5ba], succ=[]
    =================================
    0x5c6: v5c6(0x40) = CONST 
    0x5c9: v5c9 = MLOAD v5c6(0x40)
    0x5ca: v5ca(0x461bcd) = CONST 
    0x5ce: v5ce(0xe5) = CONST 
    0x5d0: v5d0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5ce(0xe5), v5ca(0x461bcd)
    0x5d2: MSTORE v5c9, v5d0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5d3: v5d3(0x20) = CONST 
    0x5d5: v5d5(0x4) = CONST 
    0x5d8: v5d8 = ADD v5c9, v5d5(0x4)
    0x5d9: MSTORE v5d8, v5d3(0x20)
    0x5da: v5da(0xe) = CONST 
    0x5dc: v5dc(0x24) = CONST 
    0x5df: v5df = ADD v5c9, v5dc(0x24)
    0x5e0: MSTORE v5df, v5da(0xe)
    0x5e1: v5e1(0x185b1c9958591e481a5b9a5d1959) = CONST 
    0x5f0: v5f0(0x92) = CONST 
    0x5f2: v5f2(0x616c726561647920696e69746564000000000000000000000000000000000000) = SHL v5f0(0x92), v5e1(0x185b1c9958591e481a5b9a5d1959)
    0x5f3: v5f3(0x44) = CONST 
    0x5f6: v5f6 = ADD v5c9, v5f3(0x44)
    0x5f7: MSTORE v5f6, v5f2(0x616c726561647920696e69746564000000000000000000000000000000000000)
    0x5f9: v5f9 = MLOAD v5c6(0x40)
    0x5fd: v5fd(0x0) = SUB v5c9, v5f9
    0x5fe: v5fe(0x64) = CONST 
    0x600: v600(0x64) = ADD v5fe(0x64), v5fd(0x0)
    0x602: REVERT v5f9, v600(0x64)

    Begin block 0x603
    prev=[0x5ba], succ=[0x7fb]
    =================================
    0x604: v604(0x0) = CONST 
    0x607: v607 = SLOAD v604(0x0)
    0x608: v608(0x1) = CONST 
    0x60a: v60a(0x1) = CONST 
    0x60c: v60c(0xa0) = CONST 
    0x60e: v60e(0x10000000000000000000000000000000000000000) = SHL v60c(0xa0), v60a(0x1)
    0x60f: v60f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v60e(0x10000000000000000000000000000000000000000), v608(0x1)
    0x612: v612 = AND v14d, v60f(0xffffffffffffffffffffffffffffffffffffffff)
    0x613: v613(0x100) = CONST 
    0x616: v616 = MUL v613(0x100), v612
    0x617: v617(0x100) = CONST 
    0x61a: v61a(0x1) = CONST 
    0x61c: v61c(0xa8) = CONST 
    0x61e: v61e(0x1000000000000000000000000000000000000000000) = SHL v61c(0xa8), v61a(0x1)
    0x61f: v61f(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v61e(0x1000000000000000000000000000000000000000000), v617(0x100)
    0x620: v620(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v61f(0xffffffffffffffffffffffffffffffffffffffff00)
    0x621: v621(0xff) = CONST 
    0x623: v623(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v621(0xff)
    0x626: v626 = AND v607, v623(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x627: v627(0x1) = CONST 
    0x629: v629 = OR v627(0x1), v626
    0x62d: v62d = AND v629, v620(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff)
    0x631: v631 = OR v62d, v616
    0x633: SSTORE v604(0x0), v631
    0x634: JUMP v12d(0x7fb)

    Begin block 0x7fb
    prev=[0x603], succ=[]
    =================================
    0x7fc: STOP 

}

function logUpdateCommissionRate(uint256,uint256,uint256)() public {
    Begin block 0x152
    prev=[], succ=[0x164, 0x168]
    =================================
    0x153: v153(0x81c) = CONST 
    0x156: v156(0x4) = CONST 
    0x159: v159 = CALLDATASIZE 
    0x15a: v15a = SUB v159, v156(0x4)
    0x15b: v15b(0x60) = CONST 
    0x15e: v15e = LT v15a, v15b(0x60)
    0x15f: v15f = ISZERO v15e
    0x160: v160(0x168) = CONST 
    0x163: JUMPI v160(0x168), v15f

    Begin block 0x164
    prev=[0x152], succ=[]
    =================================
    0x164: v164(0x0) = CONST 
    0x167: REVERT v164(0x0), v164(0x0)

    Begin block 0x168
    prev=[0x152], succ=[0x635]
    =================================
    0x16b: v16b = CALLDATALOAD v156(0x4)
    0x16d: v16d(0x20) = CONST 
    0x170: v170(0x24) = ADD v156(0x4), v16d(0x20)
    0x171: v171 = CALLDATALOAD v170(0x24)
    0x173: v173(0x40) = CONST 
    0x175: v175(0x44) = ADD v173(0x40), v156(0x4)
    0x176: v176 = CALLDATALOAD v175(0x44)
    0x177: v177(0x635) = CONST 
    0x17a: JUMP v177(0x635)

    Begin block 0x635
    prev=[0x168], succ=[0x67a, 0x67e]
    =================================
    0x636: v636(0x0) = CONST 
    0x638: v638 = SLOAD v636(0x0)
    0x639: v639(0x40) = CONST 
    0x63c: v63c = MLOAD v639(0x40)
    0x63d: v63d(0xa1ef8f9) = CONST 
    0x642: v642(0xe2) = CONST 
    0x644: v644(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v642(0xe2), v63d(0xa1ef8f9)
    0x646: MSTORE v63c, v644(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x648: v648 = MLOAD v639(0x40)
    0x649: v649 = CALLER 
    0x64b: v64b(0x100) = CONST 
    0x64f: v64f = DIV v638, v64b(0x100)
    0x650: v650(0x1) = CONST 
    0x652: v652(0x1) = CONST 
    0x654: v654(0xa0) = CONST 
    0x656: v656(0x10000000000000000000000000000000000000000) = SHL v654(0xa0), v652(0x1)
    0x657: v657(0xffffffffffffffffffffffffffffffffffffffff) = SUB v656(0x10000000000000000000000000000000000000000), v650(0x1)
    0x658: v658 = AND v657(0xffffffffffffffffffffffffffffffffffffffff), v64f
    0x65a: v65a(0x287be3e4) = CONST 
    0x660: v660(0x4) = CONST 
    0x664: v664 = ADD v63c, v660(0x4)
    0x666: v666(0x20) = CONST 
    0x66d: v66d(0x0) = SUB v63c, v648
    0x66e: v66e(0x4) = ADD v66d(0x0), v660(0x4)
    0x672: v672 = EXTCODESIZE v658
    0x673: v673 = ISZERO v672
    0x675: v675 = ISZERO v673
    0x676: v676(0x67e) = CONST 
    0x679: JUMPI v676(0x67e), v675

    Begin block 0x67a
    prev=[0x635], succ=[]
    =================================
    0x67a: v67a(0x0) = CONST 
    0x67d: REVERT v67a(0x0), v67a(0x0)

    Begin block 0x67e
    prev=[0x635], succ=[0x689, 0x692]
    =================================
    0x680: v680 = GAS 
    0x681: v681 = STATICCALL v680, v658, v648, v66e(0x4), v648, v666(0x20)
    0x682: v682 = ISZERO v681
    0x684: v684 = ISZERO v682
    0x685: v685(0x692) = CONST 
    0x688: JUMPI v685(0x692), v684

    Begin block 0x689
    prev=[0x67e], succ=[]
    =================================
    0x689: v689 = RETURNDATASIZE 
    0x68a: v68a(0x0) = CONST 
    0x68d: RETURNDATACOPY v68a(0x0), v68a(0x0), v689
    0x68e: v68e = RETURNDATASIZE 
    0x68f: v68f(0x0) = CONST 
    0x691: REVERT v68f(0x0), v68e

    Begin block 0x692
    prev=[0x67e], succ=[0x6a4, 0x6a8]
    =================================
    0x697: v697(0x40) = CONST 
    0x699: v699 = MLOAD v697(0x40)
    0x69a: v69a = RETURNDATASIZE 
    0x69b: v69b(0x20) = CONST 
    0x69e: v69e = LT v69a, v69b(0x20)
    0x69f: v69f = ISZERO v69e
    0x6a0: v6a0(0x6a8) = CONST 
    0x6a3: JUMPI v6a0(0x6a8), v69f

    Begin block 0x6a4
    prev=[0x692], succ=[]
    =================================
    0x6a4: v6a4(0x0) = CONST 
    0x6a7: REVERT v6a4(0x0), v6a4(0x0)

    Begin block 0x6a8
    prev=[0x692], succ=[0x6b9, 0x6ef]
    =================================
    0x6aa: v6aa = MLOAD v699
    0x6ab: v6ab(0x1) = CONST 
    0x6ad: v6ad(0x1) = CONST 
    0x6af: v6af(0xa0) = CONST 
    0x6b1: v6b1(0x10000000000000000000000000000000000000000) = SHL v6af(0xa0), v6ad(0x1)
    0x6b2: v6b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b1(0x10000000000000000000000000000000000000000), v6ab(0x1)
    0x6b3: v6b3 = AND v6b2(0xffffffffffffffffffffffffffffffffffffffff), v6aa
    0x6b4: v6b4 = EQ v6b3, v649
    0x6b5: v6b5(0x6ef) = CONST 
    0x6b8: JUMPI v6b5(0x6ef), v6b4

    Begin block 0x6b9
    prev=[0x6a8], succ=[]
    =================================
    0x6b9: v6b9(0x40) = CONST 
    0x6bb: v6bb = MLOAD v6b9(0x40)
    0x6bc: v6bc(0x461bcd) = CONST 
    0x6c0: v6c0(0xe5) = CONST 
    0x6c2: v6c2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v6c0(0xe5), v6bc(0x461bcd)
    0x6c4: MSTORE v6bb, v6c2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x6c5: v6c5(0x4) = CONST 
    0x6c7: v6c7 = ADD v6c5(0x4), v6bb
    0x6ca: v6ca(0x20) = CONST 
    0x6cc: v6cc = ADD v6ca(0x20), v6c7
    0x6cf: v6cf(0x20) = SUB v6cc, v6c7
    0x6d1: MSTORE v6c7, v6cf(0x20)
    0x6d2: v6d2(0x21) = CONST 
    0x6d5: MSTORE v6cc, v6d2(0x21)
    0x6d6: v6d6(0x20) = CONST 
    0x6d8: v6d8 = ADD v6d6(0x20), v6cc
    0x6da: v6da(0x724) = CONST 
    0x6dd: v6dd(0x21) = CONST 
    0x6e0: CODECOPY v6d8, v6da(0x724), v6dd(0x21)
    0x6e1: v6e1(0x40) = CONST 
    0x6e3: v6e3 = ADD v6e1(0x40), v6d8
    0x6e7: v6e7(0x40) = CONST 
    0x6e9: v6e9 = MLOAD v6e7(0x40)
    0x6ec: v6ec(0x84) = SUB v6e3, v6e9
    0x6ee: REVERT v6e9, v6ec(0x84)

    Begin block 0x6ef
    prev=[0x6a8], succ=[0x81c]
    =================================
    0x6f3: v6f3(0x7d5da5ece9d43013d62ab966f4704ca376b92be29ca6fbb958154baf1c0dc17e) = CONST 
    0x714: v714(0x40) = CONST 
    0x716: v716 = MLOAD v714(0x40)
    0x717: v717(0x40) = CONST 
    0x719: v719 = MLOAD v717(0x40)
    0x71c: v71c(0x0) = SUB v716, v719
    0x71e: LOG4 v719, v71c(0x0), v6f3(0x7d5da5ece9d43013d62ab966f4704ca376b92be29ca6fbb958154baf1c0dc17e), v16b, v171, v176
    0x722: JUMP v153(0x81c)

    Begin block 0x81c
    prev=[0x6ef], succ=[]
    =================================
    0x81d: STOP 

}

function fallback()() public {
    Begin block 0x62
    prev=[], succ=[]
    =================================
    0x63: v63(0x0) = CONST 
    0x66: REVERT v63(0x0), v63(0x0)

}

function logShareBurnedWithId(uint256,address,uint256,uint256,uint256)() public {
    Begin block 0x67
    prev=[], succ=[0x79, 0x7d]
    =================================
    0x68: v68(0x798) = CONST 
    0x6b: v6b(0x4) = CONST 
    0x6e: v6e = CALLDATASIZE 
    0x6f: v6f = SUB v6e, v6b(0x4)
    0x70: v70(0xa0) = CONST 
    0x73: v73 = LT v6f, v70(0xa0)
    0x74: v74 = ISZERO v73
    0x75: v75(0x7d) = CONST 
    0x78: JUMPI v75(0x7d), v74

    Begin block 0x79
    prev=[0x67], succ=[]
    =================================
    0x79: v79(0x0) = CONST 
    0x7c: REVERT v79(0x0), v79(0x0)

    Begin block 0x7d
    prev=[0x67], succ=[0x17b]
    =================================
    0x80: v80 = CALLDATALOAD v6b(0x4)
    0x82: v82(0x1) = CONST 
    0x84: v84(0x1) = CONST 
    0x86: v86(0xa0) = CONST 
    0x88: v88(0x10000000000000000000000000000000000000000) = SHL v86(0xa0), v84(0x1)
    0x89: v89(0xffffffffffffffffffffffffffffffffffffffff) = SUB v88(0x10000000000000000000000000000000000000000), v82(0x1)
    0x8a: v8a(0x20) = CONST 
    0x8d: v8d(0x24) = ADD v6b(0x4), v8a(0x20)
    0x8e: v8e = CALLDATALOAD v8d(0x24)
    0x8f: v8f = AND v8e, v89(0xffffffffffffffffffffffffffffffffffffffff)
    0x91: v91(0x40) = CONST 
    0x94: v94(0x44) = ADD v6b(0x4), v91(0x40)
    0x95: v95 = CALLDATALOAD v94(0x44)
    0x97: v97(0x60) = CONST 
    0x9a: v9a(0x64) = ADD v6b(0x4), v97(0x60)
    0x9b: v9b = CALLDATALOAD v9a(0x64)
    0x9d: v9d(0x80) = CONST 
    0x9f: v9f(0x84) = ADD v9d(0x80), v6b(0x4)
    0xa0: va0 = CALLDATALOAD v9f(0x84)
    0xa1: va1(0x17b) = CONST 
    0xa4: JUMP va1(0x17b)

    Begin block 0x17b
    prev=[0x7d], succ=[0x1c7, 0x1cb]
    =================================
    0x17d: v17d(0x0) = CONST 
    0x180: v180(0x1) = CONST 
    0x183: v183 = SLOAD v17d(0x0)
    0x185: v185(0x100) = CONST 
    0x188: v188(0x100) = EXP v185(0x100), v180(0x1)
    0x18a: v18a = DIV v183, v188(0x100)
    0x18b: v18b(0x1) = CONST 
    0x18d: v18d(0x1) = CONST 
    0x18f: v18f(0xa0) = CONST 
    0x191: v191(0x10000000000000000000000000000000000000000) = SHL v18f(0xa0), v18d(0x1)
    0x192: v192(0xffffffffffffffffffffffffffffffffffffffff) = SUB v191(0x10000000000000000000000000000000000000000), v18b(0x1)
    0x193: v193 = AND v192(0xffffffffffffffffffffffffffffffffffffffff), v18a
    0x194: v194(0x1) = CONST 
    0x196: v196(0x1) = CONST 
    0x198: v198(0xa0) = CONST 
    0x19a: v19a(0x10000000000000000000000000000000000000000) = SHL v198(0xa0), v196(0x1)
    0x19b: v19b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19a(0x10000000000000000000000000000000000000000), v194(0x1)
    0x19c: v19c = AND v19b(0xffffffffffffffffffffffffffffffffffffffff), v193
    0x19d: v19d(0x287be3e4) = CONST 
    0x1a2: v1a2(0x40) = CONST 
    0x1a4: v1a4 = MLOAD v1a2(0x40)
    0x1a6: v1a6(0xffffffff) = CONST 
    0x1ab: v1ab(0x287be3e4) = AND v1a6(0xffffffff), v19d(0x287be3e4)
    0x1ac: v1ac(0xe0) = CONST 
    0x1ae: v1ae(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v1ac(0xe0), v1ab(0x287be3e4)
    0x1b0: MSTORE v1a4, v1ae(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x1b1: v1b1(0x4) = CONST 
    0x1b3: v1b3 = ADD v1b1(0x4), v1a4
    0x1b4: v1b4(0x20) = CONST 
    0x1b6: v1b6(0x40) = CONST 
    0x1b8: v1b8 = MLOAD v1b6(0x40)
    0x1bb: v1bb(0x4) = SUB v1b3, v1b8
    0x1bf: v1bf = EXTCODESIZE v19c
    0x1c0: v1c0 = ISZERO v1bf
    0x1c2: v1c2 = ISZERO v1c0
    0x1c3: v1c3(0x1cb) = CONST 
    0x1c6: JUMPI v1c3(0x1cb), v1c2

    Begin block 0x1c7
    prev=[0x17b], succ=[]
    =================================
    0x1c7: v1c7(0x0) = CONST 
    0x1ca: REVERT v1c7(0x0), v1c7(0x0)

    Begin block 0x1cb
    prev=[0x17b], succ=[0x1d6, 0x1df]
    =================================
    0x1cd: v1cd = GAS 
    0x1ce: v1ce = STATICCALL v1cd, v19c, v1b8, v1bb(0x4), v1b8, v1b4(0x20)
    0x1cf: v1cf = ISZERO v1ce
    0x1d1: v1d1 = ISZERO v1cf
    0x1d2: v1d2(0x1df) = CONST 
    0x1d5: JUMPI v1d2(0x1df), v1d1

    Begin block 0x1d6
    prev=[0x1cb], succ=[]
    =================================
    0x1d6: v1d6 = RETURNDATASIZE 
    0x1d7: v1d7(0x0) = CONST 
    0x1da: RETURNDATACOPY v1d7(0x0), v1d7(0x0), v1d6
    0x1db: v1db = RETURNDATASIZE 
    0x1dc: v1dc(0x0) = CONST 
    0x1de: REVERT v1dc(0x0), v1db

    Begin block 0x1df
    prev=[0x1cb], succ=[0x1f1, 0x1f5]
    =================================
    0x1e4: v1e4(0x40) = CONST 
    0x1e6: v1e6 = MLOAD v1e4(0x40)
    0x1e7: v1e7 = RETURNDATASIZE 
    0x1e8: v1e8(0x20) = CONST 
    0x1eb: v1eb = LT v1e7, v1e8(0x20)
    0x1ec: v1ec = ISZERO v1eb
    0x1ed: v1ed(0x1f5) = CONST 
    0x1f0: JUMPI v1ed(0x1f5), v1ec

    Begin block 0x1f1
    prev=[0x1df], succ=[]
    =================================
    0x1f1: v1f1(0x0) = CONST 
    0x1f4: REVERT v1f1(0x0), v1f1(0x0)

    Begin block 0x1f5
    prev=[0x1df], succ=[0x23c, 0x240]
    =================================
    0x1f7: v1f7 = MLOAD v1e6
    0x1f8: v1f8(0x40) = CONST 
    0x1fb: v1fb = MLOAD v1f8(0x40)
    0x1fc: v1fc(0xd6a8b91) = CONST 
    0x201: v201(0xe2) = CONST 
    0x203: v203(0x35aa2e4400000000000000000000000000000000000000000000000000000000) = SHL v201(0xe2), v1fc(0xd6a8b91)
    0x205: MSTORE v1fb, v203(0x35aa2e4400000000000000000000000000000000000000000000000000000000)
    0x206: v206(0x4) = CONST 
    0x209: v209 = ADD v1fb, v206(0x4)
    0x20c: MSTORE v209, v80
    0x20e: v20e = MLOAD v1f8(0x40)
    0x20f: v20f(0x1) = CONST 
    0x211: v211(0x1) = CONST 
    0x213: v213(0xa0) = CONST 
    0x215: v215(0x10000000000000000000000000000000000000000) = SHL v213(0xa0), v211(0x1)
    0x216: v216(0xffffffffffffffffffffffffffffffffffffffff) = SUB v215(0x10000000000000000000000000000000000000000), v20f(0x1)
    0x219: v219 = AND v1f7, v216(0xffffffffffffffffffffffffffffffffffffffff)
    0x21b: v21b(0x35aa2e44) = CONST 
    0x221: v221(0x24) = CONST 
    0x225: v225 = ADD v1fb, v221(0x24)
    0x227: v227(0xe0) = CONST 
    0x22f: v22f(0x0) = SUB v1fb, v20e
    0x230: v230(0x24) = ADD v22f(0x0), v221(0x24)
    0x234: v234 = EXTCODESIZE v219
    0x235: v235 = ISZERO v234
    0x237: v237 = ISZERO v235
    0x238: v238(0x240) = CONST 
    0x23b: JUMPI v238(0x240), v237

    Begin block 0x23c
    prev=[0x1f5], succ=[]
    =================================
    0x23c: v23c(0x0) = CONST 
    0x23f: REVERT v23c(0x0), v23c(0x0)

    Begin block 0x240
    prev=[0x1f5], succ=[0x24b, 0x254]
    =================================
    0x242: v242 = GAS 
    0x243: v243 = STATICCALL v242, v219, v20e, v230(0x24), v20e, v227(0xe0)
    0x244: v244 = ISZERO v243
    0x246: v246 = ISZERO v244
    0x247: v247(0x254) = CONST 
    0x24a: JUMPI v247(0x254), v246

    Begin block 0x24b
    prev=[0x240], succ=[]
    =================================
    0x24b: v24b = RETURNDATASIZE 
    0x24c: v24c(0x0) = CONST 
    0x24f: RETURNDATACOPY v24c(0x0), v24c(0x0), v24b
    0x250: v250 = RETURNDATASIZE 
    0x251: v251(0x0) = CONST 
    0x253: REVERT v251(0x0), v250

    Begin block 0x254
    prev=[0x240], succ=[0x266, 0x26a]
    =================================
    0x259: v259(0x40) = CONST 
    0x25b: v25b = MLOAD v259(0x40)
    0x25c: v25c = RETURNDATASIZE 
    0x25d: v25d(0xe0) = CONST 
    0x260: v260 = LT v25c, v25d(0xe0)
    0x261: v261 = ISZERO v260
    0x262: v262(0x26a) = CONST 
    0x265: JUMPI v262(0x26a), v261

    Begin block 0x266
    prev=[0x254], succ=[]
    =================================
    0x266: v266(0x0) = CONST 
    0x269: REVERT v266(0x0), v266(0x0)

    Begin block 0x26a
    prev=[0x254], succ=[0x282, 0x2be]
    =================================
    0x26c: v26c(0xc0) = CONST 
    0x26e: v26e = ADD v26c(0xc0), v25b
    0x26f: v26f = MLOAD v26e
    0x272: v272(0x1) = CONST 
    0x274: v274(0x1) = CONST 
    0x276: v276(0xa0) = CONST 
    0x278: v278(0x10000000000000000000000000000000000000000) = SHL v276(0xa0), v274(0x1)
    0x279: v279(0xffffffffffffffffffffffffffffffffffffffff) = SUB v278(0x10000000000000000000000000000000000000000), v272(0x1)
    0x27b: v27b = AND v26f, v279(0xffffffffffffffffffffffffffffffffffffffff)
    0x27c: v27c = CALLER 
    0x27d: v27d = EQ v27c, v27b
    0x27e: v27e(0x2be) = CONST 
    0x281: JUMPI v27e(0x2be), v27d

    Begin block 0x282
    prev=[0x26a], succ=[]
    =================================
    0x282: v282(0x40) = CONST 
    0x285: v285 = MLOAD v282(0x40)
    0x286: v286(0x461bcd) = CONST 
    0x28a: v28a(0xe5) = CONST 
    0x28c: v28c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v28a(0xe5), v286(0x461bcd)
    0x28e: MSTORE v285, v28c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x28f: v28f(0x20) = CONST 
    0x291: v291(0x4) = CONST 
    0x294: v294 = ADD v285, v291(0x4)
    0x295: MSTORE v294, v28f(0x20)
    0x296: v296(0xd) = CONST 
    0x298: v298(0x24) = CONST 
    0x29b: v29b = ADD v285, v298(0x24)
    0x29c: MSTORE v29b, v296(0xd)
    0x29d: v29d(0x3737ba103b30b634b230ba37b9) = CONST 
    0x2ab: v2ab(0x99) = CONST 
    0x2ad: v2ad(0x6e6f742076616c696461746f7200000000000000000000000000000000000000) = SHL v2ab(0x99), v29d(0x3737ba103b30b634b230ba37b9)
    0x2ae: v2ae(0x44) = CONST 
    0x2b1: v2b1 = ADD v285, v2ae(0x44)
    0x2b2: MSTORE v2b1, v2ad(0x6e6f742076616c696461746f7200000000000000000000000000000000000000)
    0x2b4: v2b4 = MLOAD v282(0x40)
    0x2b8: v2b8(0x0) = SUB v285, v2b4
    0x2b9: v2b9(0x64) = CONST 
    0x2bb: v2bb(0x64) = ADD v2b9(0x64), v2b8(0x0)
    0x2bd: REVERT v2b4, v2bb(0x64)

    Begin block 0x2be
    prev=[0x26a], succ=[0x798]
    =================================
    0x2c1: v2c1(0x1) = CONST 
    0x2c3: v2c3(0x1) = CONST 
    0x2c5: v2c5(0xa0) = CONST 
    0x2c7: v2c7(0x10000000000000000000000000000000000000000) = SHL v2c5(0xa0), v2c3(0x1)
    0x2c8: v2c8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c7(0x10000000000000000000000000000000000000000), v2c1(0x1)
    0x2c9: v2c9 = AND v2c8(0xffffffffffffffffffffffffffffffffffffffff), v8f
    0x2cb: v2cb(0x502f5a6697a92e602c626b931a4a771fef4360eb9cece7bf906f10c5cec96aaa) = CONST 
    0x2ee: v2ee(0x40) = CONST 
    0x2f0: v2f0 = MLOAD v2ee(0x40)
    0x2f4: MSTORE v2f0, v9b
    0x2f5: v2f5(0x20) = CONST 
    0x2f7: v2f7 = ADD v2f5(0x20), v2f0
    0x2fa: MSTORE v2f7, va0
    0x2fb: v2fb(0x20) = CONST 
    0x2fd: v2fd = ADD v2fb(0x20), v2f7
    0x302: v302(0x40) = CONST 
    0x304: v304 = MLOAD v302(0x40)
    0x307: v307(0x40) = SUB v2fd, v304
    0x309: LOG4 v304, v307(0x40), v2cb(0x502f5a6697a92e602c626b931a4a771fef4360eb9cece7bf906f10c5cec96aaa), v80, v2c9, v95
    0x311: JUMP v68(0x798)

    Begin block 0x798
    prev=[0x2be], succ=[]
    =================================
    0x799: STOP 

}

function logDelegatorUnstakedWithId(uint256,address,uint256,uint256)() public {
    Begin block 0xa7
    prev=[], succ=[0xb9, 0xbd]
    =================================
    0xa8: va8(0x7b9) = CONST 
    0xab: vab(0x4) = CONST 
    0xae: vae = CALLDATASIZE 
    0xaf: vaf = SUB vae, vab(0x4)
    0xb0: vb0(0x80) = CONST 
    0xb3: vb3 = LT vaf, vb0(0x80)
    0xb4: vb4 = ISZERO vb3
    0xb5: vb5(0xbd) = CONST 
    0xb8: JUMPI vb5(0xbd), vb4

    Begin block 0xb9
    prev=[0xa7], succ=[]
    =================================
    0xb9: vb9(0x0) = CONST 
    0xbc: REVERT vb9(0x0), vb9(0x0)

    Begin block 0xbd
    prev=[0xa7], succ=[0x312]
    =================================
    0xc0: vc0 = CALLDATALOAD vab(0x4)
    0xc2: vc2(0x1) = CONST 
    0xc4: vc4(0x1) = CONST 
    0xc6: vc6(0xa0) = CONST 
    0xc8: vc8(0x10000000000000000000000000000000000000000) = SHL vc6(0xa0), vc4(0x1)
    0xc9: vc9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc8(0x10000000000000000000000000000000000000000), vc2(0x1)
    0xca: vca(0x20) = CONST 
    0xcd: vcd(0x24) = ADD vab(0x4), vca(0x20)
    0xce: vce = CALLDATALOAD vcd(0x24)
    0xcf: vcf = AND vce, vc9(0xffffffffffffffffffffffffffffffffffffffff)
    0xd1: vd1(0x40) = CONST 
    0xd4: vd4(0x44) = ADD vab(0x4), vd1(0x40)
    0xd5: vd5 = CALLDATALOAD vd4(0x44)
    0xd7: vd7(0x60) = CONST 
    0xd9: vd9(0x64) = ADD vd7(0x60), vab(0x4)
    0xda: vda = CALLDATALOAD vd9(0x64)
    0xdb: vdb(0x312) = CONST 
    0xde: JUMP vdb(0x312)

    Begin block 0x312
    prev=[0xbd], succ=[0x35e, 0x362]
    =================================
    0x314: v314(0x0) = CONST 
    0x317: v317(0x1) = CONST 
    0x31a: v31a = SLOAD v314(0x0)
    0x31c: v31c(0x100) = CONST 
    0x31f: v31f(0x100) = EXP v31c(0x100), v317(0x1)
    0x321: v321 = DIV v31a, v31f(0x100)
    0x322: v322(0x1) = CONST 
    0x324: v324(0x1) = CONST 
    0x326: v326(0xa0) = CONST 
    0x328: v328(0x10000000000000000000000000000000000000000) = SHL v326(0xa0), v324(0x1)
    0x329: v329(0xffffffffffffffffffffffffffffffffffffffff) = SUB v328(0x10000000000000000000000000000000000000000), v322(0x1)
    0x32a: v32a = AND v329(0xffffffffffffffffffffffffffffffffffffffff), v321
    0x32b: v32b(0x1) = CONST 
    0x32d: v32d(0x1) = CONST 
    0x32f: v32f(0xa0) = CONST 
    0x331: v331(0x10000000000000000000000000000000000000000) = SHL v32f(0xa0), v32d(0x1)
    0x332: v332(0xffffffffffffffffffffffffffffffffffffffff) = SUB v331(0x10000000000000000000000000000000000000000), v32b(0x1)
    0x333: v333 = AND v332(0xffffffffffffffffffffffffffffffffffffffff), v32a
    0x334: v334(0x287be3e4) = CONST 
    0x339: v339(0x40) = CONST 
    0x33b: v33b = MLOAD v339(0x40)
    0x33d: v33d(0xffffffff) = CONST 
    0x342: v342(0x287be3e4) = AND v33d(0xffffffff), v334(0x287be3e4)
    0x343: v343(0xe0) = CONST 
    0x345: v345(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v343(0xe0), v342(0x287be3e4)
    0x347: MSTORE v33b, v345(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x348: v348(0x4) = CONST 
    0x34a: v34a = ADD v348(0x4), v33b
    0x34b: v34b(0x20) = CONST 
    0x34d: v34d(0x40) = CONST 
    0x34f: v34f = MLOAD v34d(0x40)
    0x352: v352(0x4) = SUB v34a, v34f
    0x356: v356 = EXTCODESIZE v333
    0x357: v357 = ISZERO v356
    0x359: v359 = ISZERO v357
    0x35a: v35a(0x362) = CONST 
    0x35d: JUMPI v35a(0x362), v359

    Begin block 0x35e
    prev=[0x312], succ=[]
    =================================
    0x35e: v35e(0x0) = CONST 
    0x361: REVERT v35e(0x0), v35e(0x0)

    Begin block 0x362
    prev=[0x312], succ=[0x36d, 0x376]
    =================================
    0x364: v364 = GAS 
    0x365: v365 = STATICCALL v364, v333, v34f, v352(0x4), v34f, v34b(0x20)
    0x366: v366 = ISZERO v365
    0x368: v368 = ISZERO v366
    0x369: v369(0x376) = CONST 
    0x36c: JUMPI v369(0x376), v368

    Begin block 0x36d
    prev=[0x362], succ=[]
    =================================
    0x36d: v36d = RETURNDATASIZE 
    0x36e: v36e(0x0) = CONST 
    0x371: RETURNDATACOPY v36e(0x0), v36e(0x0), v36d
    0x372: v372 = RETURNDATASIZE 
    0x373: v373(0x0) = CONST 
    0x375: REVERT v373(0x0), v372

    Begin block 0x376
    prev=[0x362], succ=[0x388, 0x38c]
    =================================
    0x37b: v37b(0x40) = CONST 
    0x37d: v37d = MLOAD v37b(0x40)
    0x37e: v37e = RETURNDATASIZE 
    0x37f: v37f(0x20) = CONST 
    0x382: v382 = LT v37e, v37f(0x20)
    0x383: v383 = ISZERO v382
    0x384: v384(0x38c) = CONST 
    0x387: JUMPI v384(0x38c), v383

    Begin block 0x388
    prev=[0x376], succ=[]
    =================================
    0x388: v388(0x0) = CONST 
    0x38b: REVERT v388(0x0), v388(0x0)

    Begin block 0x38c
    prev=[0x376], succ=[0x3d3, 0x3d7]
    =================================
    0x38e: v38e = MLOAD v37d
    0x38f: v38f(0x40) = CONST 
    0x392: v392 = MLOAD v38f(0x40)
    0x393: v393(0xd6a8b91) = CONST 
    0x398: v398(0xe2) = CONST 
    0x39a: v39a(0x35aa2e4400000000000000000000000000000000000000000000000000000000) = SHL v398(0xe2), v393(0xd6a8b91)
    0x39c: MSTORE v392, v39a(0x35aa2e4400000000000000000000000000000000000000000000000000000000)
    0x39d: v39d(0x4) = CONST 
    0x3a0: v3a0 = ADD v392, v39d(0x4)
    0x3a3: MSTORE v3a0, vc0
    0x3a5: v3a5 = MLOAD v38f(0x40)
    0x3a6: v3a6(0x1) = CONST 
    0x3a8: v3a8(0x1) = CONST 
    0x3aa: v3aa(0xa0) = CONST 
    0x3ac: v3ac(0x10000000000000000000000000000000000000000) = SHL v3aa(0xa0), v3a8(0x1)
    0x3ad: v3ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ac(0x10000000000000000000000000000000000000000), v3a6(0x1)
    0x3b0: v3b0 = AND v38e, v3ad(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b2: v3b2(0x35aa2e44) = CONST 
    0x3b8: v3b8(0x24) = CONST 
    0x3bc: v3bc = ADD v392, v3b8(0x24)
    0x3be: v3be(0xe0) = CONST 
    0x3c6: v3c6(0x0) = SUB v392, v3a5
    0x3c7: v3c7(0x24) = ADD v3c6(0x0), v3b8(0x24)
    0x3cb: v3cb = EXTCODESIZE v3b0
    0x3cc: v3cc = ISZERO v3cb
    0x3ce: v3ce = ISZERO v3cc
    0x3cf: v3cf(0x3d7) = CONST 
    0x3d2: JUMPI v3cf(0x3d7), v3ce

    Begin block 0x3d3
    prev=[0x38c], succ=[]
    =================================
    0x3d3: v3d3(0x0) = CONST 
    0x3d6: REVERT v3d3(0x0), v3d3(0x0)

    Begin block 0x3d7
    prev=[0x38c], succ=[0x3e2, 0x3eb]
    =================================
    0x3d9: v3d9 = GAS 
    0x3da: v3da = STATICCALL v3d9, v3b0, v3a5, v3c7(0x24), v3a5, v3be(0xe0)
    0x3db: v3db = ISZERO v3da
    0x3dd: v3dd = ISZERO v3db
    0x3de: v3de(0x3eb) = CONST 
    0x3e1: JUMPI v3de(0x3eb), v3dd

    Begin block 0x3e2
    prev=[0x3d7], succ=[]
    =================================
    0x3e2: v3e2 = RETURNDATASIZE 
    0x3e3: v3e3(0x0) = CONST 
    0x3e6: RETURNDATACOPY v3e3(0x0), v3e3(0x0), v3e2
    0x3e7: v3e7 = RETURNDATASIZE 
    0x3e8: v3e8(0x0) = CONST 
    0x3ea: REVERT v3e8(0x0), v3e7

    Begin block 0x3eb
    prev=[0x3d7], succ=[0x3fd, 0x401]
    =================================
    0x3f0: v3f0(0x40) = CONST 
    0x3f2: v3f2 = MLOAD v3f0(0x40)
    0x3f3: v3f3 = RETURNDATASIZE 
    0x3f4: v3f4(0xe0) = CONST 
    0x3f7: v3f7 = LT v3f3, v3f4(0xe0)
    0x3f8: v3f8 = ISZERO v3f7
    0x3f9: v3f9(0x401) = CONST 
    0x3fc: JUMPI v3f9(0x401), v3f8

    Begin block 0x3fd
    prev=[0x3eb], succ=[]
    =================================
    0x3fd: v3fd(0x0) = CONST 
    0x400: REVERT v3fd(0x0), v3fd(0x0)

    Begin block 0x401
    prev=[0x3eb], succ=[0x419, 0x455]
    =================================
    0x403: v403(0xc0) = CONST 
    0x405: v405 = ADD v403(0xc0), v3f2
    0x406: v406 = MLOAD v405
    0x409: v409(0x1) = CONST 
    0x40b: v40b(0x1) = CONST 
    0x40d: v40d(0xa0) = CONST 
    0x40f: v40f(0x10000000000000000000000000000000000000000) = SHL v40d(0xa0), v40b(0x1)
    0x410: v410(0xffffffffffffffffffffffffffffffffffffffff) = SUB v40f(0x10000000000000000000000000000000000000000), v409(0x1)
    0x412: v412 = AND v406, v410(0xffffffffffffffffffffffffffffffffffffffff)
    0x413: v413 = CALLER 
    0x414: v414 = EQ v413, v412
    0x415: v415(0x455) = CONST 
    0x418: JUMPI v415(0x455), v414

    Begin block 0x419
    prev=[0x401], succ=[]
    =================================
    0x419: v419(0x40) = CONST 
    0x41c: v41c = MLOAD v419(0x40)
    0x41d: v41d(0x461bcd) = CONST 
    0x421: v421(0xe5) = CONST 
    0x423: v423(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v421(0xe5), v41d(0x461bcd)
    0x425: MSTORE v41c, v423(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x426: v426(0x20) = CONST 
    0x428: v428(0x4) = CONST 
    0x42b: v42b = ADD v41c, v428(0x4)
    0x42c: MSTORE v42b, v426(0x20)
    0x42d: v42d(0xd) = CONST 
    0x42f: v42f(0x24) = CONST 
    0x432: v432 = ADD v41c, v42f(0x24)
    0x433: MSTORE v432, v42d(0xd)
    0x434: v434(0x3737ba103b30b634b230ba37b9) = CONST 
    0x442: v442(0x99) = CONST 
    0x444: v444(0x6e6f742076616c696461746f7200000000000000000000000000000000000000) = SHL v442(0x99), v434(0x3737ba103b30b634b230ba37b9)
    0x445: v445(0x44) = CONST 
    0x448: v448 = ADD v41c, v445(0x44)
    0x449: MSTORE v448, v444(0x6e6f742076616c696461746f7200000000000000000000000000000000000000)
    0x44b: v44b = MLOAD v419(0x40)
    0x44f: v44f(0x0) = SUB v41c, v44b
    0x450: v450(0x64) = CONST 
    0x452: v452(0x64) = ADD v450(0x64), v44f(0x0)
    0x454: REVERT v44b, v452(0x64)

    Begin block 0x455
    prev=[0x401], succ=[0x7b9]
    =================================
    0x457: v457(0x1) = CONST 
    0x459: v459(0x1) = CONST 
    0x45b: v45b(0xa0) = CONST 
    0x45d: v45d(0x10000000000000000000000000000000000000000) = SHL v45b(0xa0), v459(0x1)
    0x45e: v45e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45d(0x10000000000000000000000000000000000000000), v457(0x1)
    0x45f: v45f = AND v45e(0xffffffffffffffffffffffffffffffffffffffff), vcf
    0x461: v461(0x7beb9bef91040fcf7607c78d4fc668370a9036788d7e6f202a4a2db5b0c28c80) = CONST 
    0x484: v484(0x40) = CONST 
    0x486: v486 = MLOAD v484(0x40)
    0x48a: MSTORE v486, vd5
    0x48b: v48b(0x20) = CONST 
    0x48d: v48d = ADD v48b(0x20), v486
    0x490: MSTORE v48d, vda
    0x491: v491(0x20) = CONST 
    0x493: v493 = ADD v491(0x20), v48d
    0x498: v498(0x40) = CONST 
    0x49a: v49a = MLOAD v498(0x40)
    0x49d: v49d(0x40) = SUB v493, v49a
    0x49f: LOG3 v49a, v49d(0x40), v461(0x7beb9bef91040fcf7607c78d4fc668370a9036788d7e6f202a4a2db5b0c28c80), vc0, v45f
    0x4a6: JUMP va8(0x7b9)

    Begin block 0x7b9
    prev=[0x455], succ=[]
    =================================
    0x7ba: STOP 

}

function registry()() public {
    Begin block 0xdf
    prev=[], succ=[0x4a7]
    =================================
    0xe0: ve0(0xe7) = CONST 
    0xe3: ve3(0x4a7) = CONST 
    0xe6: JUMP ve3(0x4a7)

    Begin block 0x4a7
    prev=[0xdf], succ=[0xe7]
    =================================
    0x4a8: v4a8(0x0) = CONST 
    0x4aa: v4aa = SLOAD v4a8(0x0)
    0x4ab: v4ab(0x100) = CONST 
    0x4af: v4af = DIV v4aa, v4ab(0x100)
    0x4b0: v4b0(0x1) = CONST 
    0x4b2: v4b2(0x1) = CONST 
    0x4b4: v4b4(0xa0) = CONST 
    0x4b6: v4b6(0x10000000000000000000000000000000000000000) = SHL v4b4(0xa0), v4b2(0x1)
    0x4b7: v4b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b6(0x10000000000000000000000000000000000000000), v4b0(0x1)
    0x4b8: v4b8 = AND v4b7(0xffffffffffffffffffffffffffffffffffffffff), v4af
    0x4ba: JUMP ve0(0xe7)

    Begin block 0xe7
    prev=[0x4a7], succ=[]
    =================================
    0xe8: ve8(0x40) = CONST 
    0xeb: veb = MLOAD ve8(0x40)
    0xec: vec(0x1) = CONST 
    0xee: vee(0x1) = CONST 
    0xf0: vf0(0xa0) = CONST 
    0xf2: vf2(0x10000000000000000000000000000000000000000) = SHL vf0(0xa0), vee(0x1)
    0xf3: vf3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf2(0x10000000000000000000000000000000000000000), vec(0x1)
    0xf6: vf6 = AND v4b8, vf3(0xffffffffffffffffffffffffffffffffffffffff)
    0xf8: MSTORE veb, vf6
    0xf9: vf9 = MLOAD ve8(0x40)
    0xfd: vfd(0x0) = SUB veb, vf9
    0xfe: vfe(0x20) = CONST 
    0x100: v100(0x20) = ADD vfe(0x20), vfd(0x0)
    0x102: RETURN vf9, v100(0x20)

}

