function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x2d) = CONST 
    0xc: JUMPI v9(0x2d), v8

    Begin block 0xd
    prev=[0x0], succ=[0x80f, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x900f010) = CONST 
    0x19: v19 = EQ v14(0x900f010), v12
    0x808: v808(0x80f) = CONST 
    0x809: JUMPI v808(0x80f), v19

    Begin block 0x80f
    prev=[0xd], succ=[]
    =================================
    0x810: v810(0x44) = CONST 
    0x811: CALLPRIVATE v810(0x44)

    Begin block 0x1e
    prev=[0xd], succ=[0x29, 0x812]
    =================================
    0x1f: v1f(0x5c60da1b) = CONST 
    0x24: v24 = EQ v1f(0x5c60da1b), v12
    0x80a: v80a(0x812) = CONST 
    0x80b: JUMPI v80a(0x812), v24

    Begin block 0x29
    prev=[0x1e], succ=[0x3c]
    =================================
    0x29: v29(0x3c) = CONST 
    0x2c: JUMP v29(0x3c)

    Begin block 0x3c
    prev=[0x29, 0x2d], succ=[0xa80x0]
    =================================
    0x3d: v3d(0x757) = CONST 
    0x40: v40(0xa8) = CONST 
    0x43: JUMP v40(0xa8)

    Begin block 0xa80x0
    prev=[0x3c], succ=[0x799B0xa80x0]
    =================================
    0xa90x0: v0a9(0xb0) = CONST 
    0xac0x0: v0ac(0x799) = CONST 
    0xaf0x0: JUMP v0ac(0x799), v0a9(0xb0)

    Begin block 0x799B0xa80x0
    prev=[0xa80x0], succ=[0xb00x0]
    =================================
    0x79aS0xa80x0: JUMP v0a9(0xb0)

    Begin block 0xb00x0
    prev=[0x799B0xa80x0], succ=[0x37eB0xb00x0]
    =================================
    0xb10x0: v0b1(0x7ba) = CONST 
    0xb40x0: v0b4(0xbb) = CONST 
    0xb70x0: v0b7(0x37e) = CONST 
    0xba0x0: JUMP v0b7(0x37e)

    Begin block 0x37eB0xb00x0
    prev=[0xb00x0], succ=[0xbb0x0]
    =================================
    0x37fS0xb00x0: v37fVb00(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x3a0S0xb00x0: v3a0Vb00 = SLOAD v37fVb00(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x3a2S0xb00x0: JUMP v0b4(0xbb)

    Begin block 0xbb0x0
    prev=[0x37eB0xb00x0], succ=[0x3a30x0]
    =================================
    0xbc0x0: v0bc(0x3a3) = CONST 
    0xbf0x0: JUMP v0bc(0x3a3)

    Begin block 0x3a30x0
    prev=[0xbb0x0], succ=[0x3be0x0, 0x3c20x0]
    =================================
    0x3a40x0: v03a4 = CALLDATASIZE 
    0x3a50x0: v03a5(0x0) = CONST 
    0x3a80x0: CALLDATACOPY v03a5(0x0), v03a5(0x0), v03a4
    0x3a90x0: v03a9(0x0) = CONST 
    0x3ac0x0: v03ac = CALLDATASIZE 
    0x3ad0x0: v03ad(0x0) = CONST 
    0x3b00x0: v03b0 = GAS 
    0x3b10x0: v03b1 = DELEGATECALL v03b0, v3a0Vb00, v03ad(0x0), v03ac, v03a9(0x0), v03a9(0x0)
    0x3b20x0: v03b2 = RETURNDATASIZE 
    0x3b30x0: v03b3(0x0) = CONST 
    0x3b60x0: RETURNDATACOPY v03b3(0x0), v03b3(0x0), v03b2
    0x3b90x0: v03b9 = ISZERO v03b1
    0x3ba0x0: v03ba(0x3c2) = CONST 
    0x3bd0x0: JUMPI v03ba(0x3c2), v03b9

    Begin block 0x3be0x0
    prev=[0x3a30x0], succ=[]
    =================================
    0x3be0x0: v03be = RETURNDATASIZE 
    0x3bf0x0: v03bf(0x0) = CONST 
    0x3c10x0: RETURN v03bf(0x0), v03be

    Begin block 0x3c20x0
    prev=[0x3a30x0], succ=[]
    =================================
    0x3c30x0: v03c3 = RETURNDATASIZE 
    0x3c40x0: v03c4(0x0) = CONST 
    0x3c60x0: REVERT v03c4(0x0), v03c3

    Begin block 0x812
    prev=[0x1e], succ=[]
    =================================
    0x813: v813(0x77) = CONST 
    0x814: CALLPRIVATE v813(0x77)

    Begin block 0x2d
    prev=[0x0], succ=[0x80c, 0x3c]
    =================================
    0x2e: v2e = CALLDATASIZE 
    0x2f: v2f(0x3c) = CONST 
    0x32: JUMPI v2f(0x3c), v2e

    Begin block 0x80c
    prev=[0x2d], succ=[]
    =================================
    0x80c: v80c(0x80e) = CONST 
    0x80d: CALLPRIVATE v80c(0x80e)

}

function upgrade(address)() public {
    Begin block 0x44
    prev=[], succ=[0x4c, 0x50]
    =================================
    0x45: v45 = CALLVALUE 
    0x47: v47 = ISZERO v45
    0x48: v48(0x50) = CONST 
    0x4b: JUMPI v48(0x50), v47

    Begin block 0x4c
    prev=[0x44], succ=[]
    =================================
    0x4c: v4c(0x0) = CONST 
    0x4f: REVERT v4c(0x0), v4c(0x0)

    Begin block 0x50
    prev=[0x44], succ=[0x63, 0x67]
    =================================
    0x52: v52(0x778) = CONST 
    0x55: v55(0x4) = CONST 
    0x58: v58 = CALLDATASIZE 
    0x59: v59 = SUB v58, v55(0x4)
    0x5a: v5a(0x20) = CONST 
    0x5d: v5d = LT v59, v5a(0x20)
    0x5e: v5e = ISZERO v5d
    0x5f: v5f(0x67) = CONST 
    0x62: JUMPI v5f(0x67), v5e

    Begin block 0x63
    prev=[0x50], succ=[]
    =================================
    0x63: v63(0x0) = CONST 
    0x66: REVERT v63(0x0), v63(0x0)

    Begin block 0x67
    prev=[0x50], succ=[0xc2]
    =================================
    0x69: v69 = CALLDATALOAD v55(0x4)
    0x6a: v6a(0x1) = CONST 
    0x6c: v6c(0x1) = CONST 
    0x6e: v6e(0xa0) = CONST 
    0x70: v70(0x10000000000000000000000000000000000000000) = SHL v6e(0xa0), v6c(0x1)
    0x71: v71(0xffffffffffffffffffffffffffffffffffffffff) = SUB v70(0x10000000000000000000000000000000000000000), v6a(0x1)
    0x72: v72 = AND v71(0xffffffffffffffffffffffffffffffffffffffff), v69
    0x73: v73(0xc2) = CONST 
    0x76: JUMP v73(0xc2)

    Begin block 0xc2
    prev=[0x67], succ=[0xd1, 0x107]
    =================================
    0xc3: vc3(0x1) = CONST 
    0xc5: vc5(0x1) = CONST 
    0xc7: vc7(0xa0) = CONST 
    0xc9: vc9(0x10000000000000000000000000000000000000000) = SHL vc7(0xa0), vc5(0x1)
    0xca: vca(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc9(0x10000000000000000000000000000000000000000), vc3(0x1)
    0xcc: vcc = AND v72, vca(0xffffffffffffffffffffffffffffffffffffffff)
    0xcd: vcd(0x107) = CONST 
    0xd0: JUMPI vcd(0x107), vcc

    Begin block 0xd1
    prev=[0xc2], succ=[]
    =================================
    0xd1: vd1(0x40) = CONST 
    0xd3: vd3 = MLOAD vd1(0x40)
    0xd4: vd4(0x461bcd) = CONST 
    0xd8: vd8(0xe5) = CONST 
    0xda: vda(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd8(0xe5), vd4(0x461bcd)
    0xdc: MSTORE vd3, vda(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xdd: vdd(0x4) = CONST 
    0xdf: vdf = ADD vdd(0x4), vd3
    0xe2: ve2(0x20) = CONST 
    0xe4: ve4 = ADD ve2(0x20), vdf
    0xe7: ve7(0x20) = SUB ve4, vdf
    0xe9: MSTORE vdf, ve7(0x20)
    0xea: vea(0x27) = CONST 
    0xed: MSTORE ve4, vea(0x27)
    0xee: vee(0x20) = CONST 
    0xf0: vf0 = ADD vee(0x20), ve4
    0xf2: vf2(0x695) = CONST 
    0xf5: vf5(0x27) = CONST 
    0xf8: CODECOPY vf0, vf2(0x695), vf5(0x27)
    0xf9: vf9(0x40) = CONST 
    0xfb: vfb = ADD vf9(0x40), vf0
    0xff: vff(0x40) = CONST 
    0x101: v101 = MLOAD vff(0x40)
    0x104: v104(0x84) = SUB vfb, v101
    0x106: REVERT v101, v104(0x84)

    Begin block 0x107
    prev=[0xc2], succ=[0x13e, 0x142]
    =================================
    0x108: v108(0x0) = CONST 
    0x10b: v10b = ADDRESS 
    0x10c: v10c(0x1) = CONST 
    0x10e: v10e(0x1) = CONST 
    0x110: v110(0xa0) = CONST 
    0x112: v112(0x10000000000000000000000000000000000000000) = SHL v110(0xa0), v10e(0x1)
    0x113: v113(0xffffffffffffffffffffffffffffffffffffffff) = SUB v112(0x10000000000000000000000000000000000000000), v10c(0x1)
    0x114: v114 = AND v113(0xffffffffffffffffffffffffffffffffffffffff), v10b
    0x115: v115(0x9d16acfd) = CONST 
    0x11a: v11a(0x40) = CONST 
    0x11c: v11c = MLOAD v11a(0x40)
    0x11e: v11e(0xffffffff) = CONST 
    0x123: v123(0x9d16acfd) = AND v11e(0xffffffff), v115(0x9d16acfd)
    0x124: v124(0xe0) = CONST 
    0x126: v126(0x9d16acfd00000000000000000000000000000000000000000000000000000000) = SHL v124(0xe0), v123(0x9d16acfd)
    0x128: MSTORE v11c, v126(0x9d16acfd00000000000000000000000000000000000000000000000000000000)
    0x129: v129(0x4) = CONST 
    0x12b: v12b = ADD v129(0x4), v11c
    0x12c: v12c(0x40) = CONST 
    0x12f: v12f = MLOAD v12c(0x40)
    0x132: v132(0x4) = SUB v12b, v12f
    0x136: v136 = EXTCODESIZE v114
    0x137: v137 = ISZERO v136
    0x139: v139 = ISZERO v137
    0x13a: v13a(0x142) = CONST 
    0x13d: JUMPI v13a(0x142), v139

    Begin block 0x13e
    prev=[0x107], succ=[]
    =================================
    0x13e: v13e(0x0) = CONST 
    0x141: REVERT v13e(0x0), v13e(0x0)

    Begin block 0x142
    prev=[0x107], succ=[0x14d, 0x156]
    =================================
    0x144: v144 = GAS 
    0x145: v145 = STATICCALL v144, v114, v12f, v132(0x4), v12f, v12c(0x40)
    0x146: v146 = ISZERO v145
    0x148: v148 = ISZERO v146
    0x149: v149(0x156) = CONST 
    0x14c: JUMPI v149(0x156), v148

    Begin block 0x14d
    prev=[0x142], succ=[]
    =================================
    0x14d: v14d = RETURNDATASIZE 
    0x14e: v14e(0x0) = CONST 
    0x151: RETURNDATACOPY v14e(0x0), v14e(0x0), v14d
    0x152: v152 = RETURNDATASIZE 
    0x153: v153(0x0) = CONST 
    0x155: REVERT v153(0x0), v152

    Begin block 0x156
    prev=[0x142], succ=[0x168, 0x16c]
    =================================
    0x15b: v15b(0x40) = CONST 
    0x15d: v15d = MLOAD v15b(0x40)
    0x15e: v15e = RETURNDATASIZE 
    0x15f: v15f(0x40) = CONST 
    0x162: v162 = LT v15e, v15f(0x40)
    0x163: v163 = ISZERO v162
    0x164: v164(0x16c) = CONST 
    0x167: JUMPI v164(0x16c), v163

    Begin block 0x168
    prev=[0x156], succ=[]
    =================================
    0x168: v168(0x0) = CONST 
    0x16b: REVERT v168(0x0), v168(0x0)

    Begin block 0x16c
    prev=[0x156], succ=[0x180, 0x1c4]
    =================================
    0x16f: v16f = MLOAD v15d
    0x170: v170(0x20) = CONST 
    0x174: v174 = ADD v15d, v170(0x20)
    0x175: v175 = MLOAD v174
    0x17c: v17c(0x1c4) = CONST 
    0x17f: JUMPI v17c(0x1c4), v16f

    Begin block 0x180
    prev=[0x16c], succ=[]
    =================================
    0x180: v180(0x40) = CONST 
    0x183: v183 = MLOAD v180(0x40)
    0x184: v184(0x461bcd) = CONST 
    0x188: v188(0xe5) = CONST 
    0x18a: v18a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v188(0xe5), v184(0x461bcd)
    0x18c: MSTORE v183, v18a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x18d: v18d(0x20) = CONST 
    0x18f: v18f(0x4) = CONST 
    0x192: v192 = ADD v183, v18f(0x4)
    0x193: MSTORE v192, v18d(0x20)
    0x194: v194(0x15) = CONST 
    0x196: v196(0x24) = CONST 
    0x199: v199 = ADD v183, v196(0x24)
    0x19a: MSTORE v199, v194(0x15)
    0x19b: v19b(0x155c19dc985919481b9bdd081cd8da19591d5b1959) = CONST 
    0x1b1: v1b1(0x5a) = CONST 
    0x1b3: v1b3(0x55706772616465206e6f74207363686564756c65640000000000000000000000) = SHL v1b1(0x5a), v19b(0x155c19dc985919481b9bdd081cd8da19591d5b1959)
    0x1b4: v1b4(0x44) = CONST 
    0x1b7: v1b7 = ADD v183, v1b4(0x44)
    0x1b8: MSTORE v1b7, v1b3(0x55706772616465206e6f74207363686564756c65640000000000000000000000)
    0x1ba: v1ba = MLOAD v180(0x40)
    0x1be: v1be(0x0) = SUB v183, v1ba
    0x1bf: v1bf(0x64) = CONST 
    0x1c1: v1c1(0x64) = ADD v1bf(0x64), v1be(0x0)
    0x1c3: REVERT v1ba, v1c1(0x64)

    Begin block 0x1c4
    prev=[0x16c], succ=[0x1de, 0x22a]
    =================================
    0x1c6: v1c6(0x1) = CONST 
    0x1c8: v1c8(0x1) = CONST 
    0x1ca: v1ca(0xa0) = CONST 
    0x1cc: v1cc(0x10000000000000000000000000000000000000000) = SHL v1ca(0xa0), v1c8(0x1)
    0x1cd: v1cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cc(0x10000000000000000000000000000000000000000), v1c6(0x1)
    0x1ce: v1ce = AND v1cd(0xffffffffffffffffffffffffffffffffffffffff), v72
    0x1d0: v1d0(0x1) = CONST 
    0x1d2: v1d2(0x1) = CONST 
    0x1d4: v1d4(0xa0) = CONST 
    0x1d6: v1d6(0x10000000000000000000000000000000000000000) = SHL v1d4(0xa0), v1d2(0x1)
    0x1d7: v1d7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d6(0x10000000000000000000000000000000000000000), v1d0(0x1)
    0x1d8: v1d8 = AND v1d7(0xffffffffffffffffffffffffffffffffffffffff), v175
    0x1d9: v1d9 = EQ v1d8, v1ce
    0x1da: v1da(0x22a) = CONST 
    0x1dd: JUMPI v1da(0x22a), v1d9

    Begin block 0x1de
    prev=[0x1c4], succ=[]
    =================================
    0x1de: v1de(0x40) = CONST 
    0x1e1: v1e1 = MLOAD v1de(0x40)
    0x1e2: v1e2(0x461bcd) = CONST 
    0x1e6: v1e6(0xe5) = CONST 
    0x1e8: v1e8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e6(0xe5), v1e2(0x461bcd)
    0x1ea: MSTORE v1e1, v1e8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1eb: v1eb(0x20) = CONST 
    0x1ed: v1ed(0x4) = CONST 
    0x1f0: v1f0 = ADD v1e1, v1ed(0x4)
    0x1f1: MSTORE v1f0, v1eb(0x20)
    0x1f2: v1f2(0x1d) = CONST 
    0x1f4: v1f4(0x24) = CONST 
    0x1f7: v1f7 = ADD v1e1, v1f4(0x24)
    0x1f8: MSTORE v1f7, v1f2(0x1d)
    0x1f9: v1f9(0x4e6577496d706c656d656e746174696f6e206973206e6f742073616d65000000) = CONST 
    0x21a: v21a(0x44) = CONST 
    0x21d: v21d = ADD v1e1, v21a(0x44)
    0x21e: MSTORE v21d, v1f9(0x4e6577496d706c656d656e746174696f6e206973206e6f742073616d65000000)
    0x220: v220 = MLOAD v1de(0x40)
    0x224: v224(0x0) = SUB v1e1, v220
    0x225: v225(0x64) = CONST 
    0x227: v227(0x64) = ADD v225(0x64), v224(0x0)
    0x229: REVERT v220, v227(0x64)

    Begin block 0x22a
    prev=[0x1c4], succ=[0x3c7]
    =================================
    0x22b: v22b(0x233) = CONST 
    0x22f: v22f(0x3c7) = CONST 
    0x232: JUMP v22f(0x3c7)

    Begin block 0x3c7
    prev=[0x22a], succ=[0x50a]
    =================================
    0x3c8: v3c8(0x3d0) = CONST 
    0x3cc: v3cc(0x50a) = CONST 
    0x3cf: JUMP v3cc(0x50a)

    Begin block 0x50a
    prev=[0x3c7], succ=[0x378]
    =================================
    0x50b: v50b(0x513) = CONST 
    0x50f: v50f(0x378) = CONST 
    0x512: JUMP v50f(0x378)

    Begin block 0x378
    prev=[0x50a], succ=[0x513]
    =================================
    0x379: v379 = EXTCODESIZE v72
    0x37a: v37a = ISZERO v379
    0x37b: v37b = ISZERO v37a
    0x37d: JUMP v50b(0x513)

    Begin block 0x513
    prev=[0x378], succ=[0x518, 0x54e]
    =================================
    0x514: v514(0x54e) = CONST 
    0x517: JUMPI v514(0x54e), v37b

    Begin block 0x518
    prev=[0x513], succ=[]
    =================================
    0x518: v518(0x40) = CONST 
    0x51a: v51a = MLOAD v518(0x40)
    0x51b: v51b(0x461bcd) = CONST 
    0x51f: v51f(0xe5) = CONST 
    0x521: v521(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v51f(0xe5), v51b(0x461bcd)
    0x523: MSTORE v51a, v521(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x524: v524(0x4) = CONST 
    0x526: v526 = ADD v524(0x4), v51a
    0x529: v529(0x20) = CONST 
    0x52b: v52b = ADD v529(0x20), v526
    0x52e: v52e(0x20) = SUB v52b, v526
    0x530: MSTORE v526, v52e(0x20)
    0x531: v531(0x36) = CONST 
    0x534: MSTORE v52b, v531(0x36)
    0x535: v535(0x20) = CONST 
    0x537: v537 = ADD v535(0x20), v52b
    0x539: v539(0x65f) = CONST 
    0x53c: v53c(0x36) = CONST 
    0x53f: CODECOPY v537, v539(0x65f), v53c(0x36)
    0x540: v540(0x40) = CONST 
    0x542: v542 = ADD v540(0x40), v537
    0x546: v546(0x40) = CONST 
    0x548: v548 = MLOAD v546(0x40)
    0x54b: v54b(0x84) = SUB v542, v548
    0x54d: REVERT v548, v54b(0x84)

    Begin block 0x54e
    prev=[0x513], succ=[0x3d0]
    =================================
    0x54f: v54f(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x570: SSTORE v54f(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v72
    0x571: JUMP v3c8(0x3d0)

    Begin block 0x3d0
    prev=[0x54e], succ=[0x233]
    =================================
    0x3d1: v3d1(0x40) = CONST 
    0x3d3: v3d3 = MLOAD v3d1(0x40)
    0x3d4: v3d4(0x1) = CONST 
    0x3d6: v3d6(0x1) = CONST 
    0x3d8: v3d8(0xa0) = CONST 
    0x3da: v3da(0x10000000000000000000000000000000000000000) = SHL v3d8(0xa0), v3d6(0x1)
    0x3db: v3db(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3da(0x10000000000000000000000000000000000000000), v3d4(0x1)
    0x3dd: v3dd = AND v72, v3db(0xffffffffffffffffffffffffffffffffffffffff)
    0x3df: v3df(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x401: v401(0x0) = CONST 
    0x404: LOG2 v3d3, v401(0x0), v3df(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v3dd
    0x406: JUMP v22b(0x233)

    Begin block 0x233
    prev=[0x3d0], succ=[0x271]
    =================================
    0x234: v234(0x40) = CONST 
    0x237: v237 = MLOAD v234(0x40)
    0x238: v238(0x4) = CONST 
    0x23b: MSTORE v237, v238(0x4)
    0x23c: v23c(0x24) = CONST 
    0x23f: v23f = ADD v237, v23c(0x24)
    0x241: MSTORE v234(0x40), v23f
    0x242: v242(0x20) = CONST 
    0x245: v245 = ADD v237, v242(0x20)
    0x247: v247 = MLOAD v245
    0x248: v248(0x1) = CONST 
    0x24a: v24a(0x1) = CONST 
    0x24c: v24c(0xe0) = CONST 
    0x24e: v24e(0x100000000000000000000000000000000000000000000000000000000) = SHL v24c(0xe0), v24a(0x1)
    0x24f: v24f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v24e(0x100000000000000000000000000000000000000000000000000000000), v248(0x1)
    0x250: v250 = AND v24f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v247
    0x251: v251(0x4d284647) = CONST 
    0x256: v256(0xe1) = CONST 
    0x258: v258(0x9a508c8e00000000000000000000000000000000000000000000000000000000) = SHL v256(0xe1), v251(0x4d284647)
    0x259: v259 = OR v258(0x9a508c8e00000000000000000000000000000000000000000000000000000000), v250
    0x25b: MSTORE v245, v259
    0x25d: v25d = MLOAD v234(0x40)
    0x25f: v25f(0x4) = MLOAD v237
    0x260: v260(0x0) = CONST 
    0x263: v263(0x60) = CONST 
    0x266: v266 = ADDRESS 

    Begin block 0x271
    prev=[0x233, 0x27a], succ=[0x290, 0x27a]
    =================================
    0x271_0x2: v271_2 = PHI v25f(0x4), v283
    0x272: v272(0x20) = CONST 
    0x275: v275 = LT v271_2, v272(0x20)
    0x276: v276(0x290) = CONST 
    0x279: JUMPI v276(0x290), v275

    Begin block 0x290
    prev=[0x271], succ=[0x2cf, 0x2f0]
    =================================
    0x290_0x0: v290_0 = PHI v245, v28b
    0x290_0x1: v290_1 = PHI v25d, v289
    0x290_0x2: v290_2 = PHI v25f(0x4), v283
    0x291: v291(0x1) = CONST 
    0x294: v294(0x20) = CONST 
    0x296: v296 = SUB v294(0x20), v290_2
    0x297: v297(0x100) = CONST 
    0x29a: v29a = EXP v297(0x100), v296
    0x29b: v29b = SUB v29a, v291(0x1)
    0x29d: v29d = NOT v29b
    0x29f: v29f = MLOAD v290_0
    0x2a0: v2a0 = AND v29f, v29d
    0x2a3: v2a3 = MLOAD v290_1
    0x2a4: v2a4 = AND v2a3, v29b
    0x2a7: v2a7 = OR v2a0, v2a4
    0x2a9: MSTORE v290_1, v2a7
    0x2b2: v2b2 = ADD v25f(0x4), v25d
    0x2b6: v2b6(0x0) = CONST 
    0x2b8: v2b8(0x40) = CONST 
    0x2ba: v2ba = MLOAD v2b8(0x40)
    0x2bd: v2bd(0x4) = SUB v2b2, v2ba
    0x2c0: v2c0 = GAS 
    0x2c1: v2c1 = DELEGATECALL v2c0, v266, v2ba, v2bd(0x4), v2ba, v2b6(0x0)
    0x2c5: v2c5 = RETURNDATASIZE 
    0x2c7: v2c7(0x0) = CONST 
    0x2ca: v2ca = EQ v2c5, v2c7(0x0)
    0x2cb: v2cb(0x2f0) = CONST 
    0x2ce: JUMPI v2cb(0x2f0), v2ca

    Begin block 0x2cf
    prev=[0x290], succ=[0x2f5]
    =================================
    0x2cf: v2cf(0x40) = CONST 
    0x2d1: v2d1 = MLOAD v2cf(0x40)
    0x2d4: v2d4(0x1f) = CONST 
    0x2d6: v2d6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2d4(0x1f)
    0x2d7: v2d7(0x3f) = CONST 
    0x2d9: v2d9 = RETURNDATASIZE 
    0x2da: v2da = ADD v2d9, v2d7(0x3f)
    0x2db: v2db = AND v2da, v2d6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2dd: v2dd = ADD v2d1, v2db
    0x2de: v2de(0x40) = CONST 
    0x2e0: MSTORE v2de(0x40), v2dd
    0x2e1: v2e1 = RETURNDATASIZE 
    0x2e3: MSTORE v2d1, v2e1
    0x2e4: v2e4 = RETURNDATASIZE 
    0x2e5: v2e5(0x0) = CONST 
    0x2e7: v2e7(0x20) = CONST 
    0x2ea: v2ea = ADD v2d1, v2e7(0x20)
    0x2eb: RETURNDATACOPY v2ea, v2e5(0x0), v2e4
    0x2ec: v2ec(0x2f5) = CONST 
    0x2ef: JUMP v2ec(0x2f5)

    Begin block 0x2f5
    prev=[0x2cf, 0x2f0], succ=[0x300, 0x336]
    =================================
    0x2fc: v2fc(0x336) = CONST 
    0x2ff: JUMPI v2fc(0x336), v2c1

    Begin block 0x300
    prev=[0x2f5], succ=[]
    =================================
    0x300: v300(0x40) = CONST 
    0x302: v302 = MLOAD v300(0x40)
    0x303: v303(0x461bcd) = CONST 
    0x307: v307(0xe5) = CONST 
    0x309: v309(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v307(0xe5), v303(0x461bcd)
    0x30b: MSTORE v302, v309(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x30c: v30c(0x4) = CONST 
    0x30e: v30e = ADD v30c(0x4), v302
    0x311: v311(0x20) = CONST 
    0x313: v313 = ADD v311(0x20), v30e
    0x316: v316(0x20) = SUB v313, v30e
    0x318: MSTORE v30e, v316(0x20)
    0x319: v319(0x21) = CONST 
    0x31c: MSTORE v313, v319(0x21)
    0x31d: v31d(0x20) = CONST 
    0x31f: v31f = ADD v31d(0x20), v313
    0x321: v321(0x617) = CONST 
    0x324: v324(0x21) = CONST 
    0x327: CODECOPY v31f, v321(0x617), v324(0x21)
    0x328: v328(0x40) = CONST 
    0x32a: v32a = ADD v328(0x40), v31f
    0x32e: v32e(0x40) = CONST 
    0x330: v330 = MLOAD v32e(0x40)
    0x333: v333(0x84) = SUB v32a, v330
    0x335: REVERT v330, v333(0x84)

    Begin block 0x336
    prev=[0x2f5], succ=[0x778]
    =================================
    0x33c: JUMP v52(0x778)

    Begin block 0x778
    prev=[0x336], succ=[]
    =================================
    0x779: STOP 

    Begin block 0x2f0
    prev=[0x290], succ=[0x2f5]
    =================================
    0x2f1: v2f1(0x60) = CONST 

    Begin block 0x27a
    prev=[0x271], succ=[0x271]
    =================================
    0x27a_0x0: v27a_0 = PHI v245, v28b
    0x27a_0x1: v27a_1 = PHI v25d, v289
    0x27a_0x2: v27a_2 = PHI v25f(0x4), v283
    0x27b: v27b = MLOAD v27a_0
    0x27d: MSTORE v27a_1, v27b
    0x27e: v27e(0x1f) = CONST 
    0x280: v280(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v27e(0x1f)
    0x283: v283 = ADD v27a_2, v280(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x285: v285(0x20) = CONST 
    0x289: v289 = ADD v285(0x20), v27a_1
    0x28b: v28b = ADD v285(0x20), v27a_0
    0x28c: v28c(0x271) = CONST 
    0x28f: JUMP v28c(0x271)

}

function implementation()() public {
    Begin block 0x77
    prev=[], succ=[0x7f, 0x83]
    =================================
    0x78: v78 = CALLVALUE 
    0x7a: v7a = ISZERO v78
    0x7b: v7b(0x83) = CONST 
    0x7e: JUMPI v7b(0x83), v7a

    Begin block 0x7f
    prev=[0x77], succ=[]
    =================================
    0x7f: v7f(0x0) = CONST 
    0x82: REVERT v7f(0x0), v7f(0x0)

    Begin block 0x83
    prev=[0x77], succ=[0x33dB0x83]
    =================================
    0x85: v85(0x8c) = CONST 
    0x88: v88(0x33d) = CONST 
    0x8b: JUMP v88(0x33d)

    Begin block 0x33dB0x83
    prev=[0x83], succ=[0x37eB0x33dB0x83]
    =================================
    0x33eS0x83: v33eV83(0x0) = CONST 
    0x340S0x83: v340V83(0x347) = CONST 
    0x343S0x83: v343V83(0x37e) = CONST 
    0x346S0x83: JUMP v343V83(0x37e)

    Begin block 0x37eB0x33dB0x83
    prev=[0x33dB0x83], succ=[0x347B0x83]
    =================================
    0x37fS0x33dS0x83: v37fV33dV83(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x3a0S0x33dS0x83: v3a0V33dV83 = SLOAD v37fV33dV83(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x3a2S0x33dS0x83: JUMP v340V83(0x347)

    Begin block 0x347B0x83
    prev=[0x37eB0x33dB0x83], succ=[0x8c]
    =================================
    0x34bS0x83: JUMP v85(0x8c)

    Begin block 0x8c
    prev=[0x347B0x83], succ=[]
    =================================
    0x8d: v8d(0x40) = CONST 
    0x90: v90 = MLOAD v8d(0x40)
    0x91: v91(0x1) = CONST 
    0x93: v93(0x1) = CONST 
    0x95: v95(0xa0) = CONST 
    0x97: v97(0x10000000000000000000000000000000000000000) = SHL v95(0xa0), v93(0x1)
    0x98: v98(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97(0x10000000000000000000000000000000000000000), v91(0x1)
    0x9b: v9b = AND v3a0V33dV83, v98(0xffffffffffffffffffffffffffffffffffffffff)
    0x9d: MSTORE v90, v9b
    0x9e: v9e = MLOAD v8d(0x40)
    0xa2: va2(0x0) = SUB v90, v9e
    0xa3: va3(0x20) = CONST 
    0xa5: va5(0x20) = ADD va3(0x20), va2(0x0)
    0xa7: RETURN v9e, va5(0x20)

}

function fallback()() public {
    Begin block 0x80e
    prev=[], succ=[0xa80x80e]
    =================================
    0x33: v33(0x736) = CONST 
    0x36: v36(0xa8) = CONST 
    0x39: JUMP v36(0xa8)

    Begin block 0xa80x80e
    prev=[0x80e], succ=[0x799B0xa80x80e]
    =================================
    0xa90x80e: v80ea9(0xb0) = CONST 
    0xac0x80e: v80eac(0x799) = CONST 
    0xaf0x80e: JUMP v80eac(0x799), v80ea9(0xb0)

    Begin block 0x799B0xa80x80e
    prev=[0xa80x80e], succ=[0xb00x80e]
    =================================
    0x79aS0xa80x80e: JUMP v80ea9(0xb0)

    Begin block 0xb00x80e
    prev=[0x799B0xa80x80e], succ=[0x37eB0xb00x80e]
    =================================
    0xb10x80e: v80eb1(0x7ba) = CONST 
    0xb40x80e: v80eb4(0xbb) = CONST 
    0xb70x80e: v80eb7(0x37e) = CONST 
    0xba0x80e: JUMP v80eb7(0x37e)

    Begin block 0x37eB0xb00x80e
    prev=[0xb00x80e], succ=[0xbb0x80e]
    =================================
    0x37fS0xb00x80e: v37fVb080e(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x3a0S0xb00x80e: v3a0Vb080e = SLOAD v37fVb080e(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x3a2S0xb00x80e: JUMP v80eb4(0xbb)

    Begin block 0xbb0x80e
    prev=[0x37eB0xb00x80e], succ=[0x3a30x80e]
    =================================
    0xbc0x80e: v80ebc(0x3a3) = CONST 
    0xbf0x80e: JUMP v80ebc(0x3a3)

    Begin block 0x3a30x80e
    prev=[0xbb0x80e], succ=[0x3be0x80e, 0x3c20x80e]
    =================================
    0x3a40x80e: v80e3a4 = CALLDATASIZE 
    0x3a50x80e: v80e3a5(0x0) = CONST 
    0x3a80x80e: CALLDATACOPY v80e3a5(0x0), v80e3a5(0x0), v80e3a4
    0x3a90x80e: v80e3a9(0x0) = CONST 
    0x3ac0x80e: v80e3ac = CALLDATASIZE 
    0x3ad0x80e: v80e3ad(0x0) = CONST 
    0x3b00x80e: v80e3b0 = GAS 
    0x3b10x80e: v80e3b1 = DELEGATECALL v80e3b0, v3a0Vb080e, v80e3ad(0x0), v80e3ac, v80e3a9(0x0), v80e3a9(0x0)
    0x3b20x80e: v80e3b2 = RETURNDATASIZE 
    0x3b30x80e: v80e3b3(0x0) = CONST 
    0x3b60x80e: RETURNDATACOPY v80e3b3(0x0), v80e3b3(0x0), v80e3b2
    0x3b90x80e: v80e3b9 = ISZERO v80e3b1
    0x3ba0x80e: v80e3ba(0x3c2) = CONST 
    0x3bd0x80e: JUMPI v80e3ba(0x3c2), v80e3b9

    Begin block 0x3be0x80e
    prev=[0x3a30x80e], succ=[]
    =================================
    0x3be0x80e: v80e3be = RETURNDATASIZE 
    0x3bf0x80e: v80e3bf(0x0) = CONST 
    0x3c10x80e: RETURN v80e3bf(0x0), v80e3be

    Begin block 0x3c20x80e
    prev=[0x3a30x80e], succ=[]
    =================================
    0x3c30x80e: v80e3c3 = RETURNDATASIZE 
    0x3c40x80e: v80e3c4(0x0) = CONST 
    0x3c60x80e: REVERT v80e3c4(0x0), v80e3c3

}

