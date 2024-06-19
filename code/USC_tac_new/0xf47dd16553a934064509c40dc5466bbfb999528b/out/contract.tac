function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x79d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x78b: v78b(0x79d) = CONST 
    0x78c: JUMPI v78b(0x79d), v8

    Begin block 0xd
    prev=[0x0], succ=[0x4e, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0xdcfbc0c7) = CONST 
    0x19: v19 = GT v14(0xdcfbc0c7), v12
    0x1a: v1a(0x4e) = CONST 
    0x1d: JUMPI v1a(0x4e), v19

    Begin block 0x4e
    prev=[0xd], succ=[0x7a0, 0x5a]
    =================================
    0x50: v50(0x26782247) = CONST 
    0x55: v55 = EQ v50(0x26782247), v12
    0x795: v795(0x7a0) = CONST 
    0x796: JUMPI v795(0x7a0), v55

    Begin block 0x7a0
    prev=[0x4e], succ=[]
    =================================
    0x7a1: v7a1(0xfe) = CONST 
    0x7a2: CALLPRIVATE v7a1(0xfe)

    Begin block 0x5a
    prev=[0x4e], succ=[0x7a3, 0x65]
    =================================
    0x5b: v5b(0xb71d1a0c) = CONST 
    0x60: v60 = EQ v5b(0xb71d1a0c), v12
    0x797: v797(0x7a3) = CONST 
    0x798: JUMPI v797(0x7a3), v60

    Begin block 0x7a3
    prev=[0x5a], succ=[]
    =================================
    0x7a4: v7a4(0x12f) = CONST 
    0x7a5: CALLPRIVATE v7a4(0x12f)

    Begin block 0x65
    prev=[0x5a], succ=[0x7a6, 0x70]
    =================================
    0x66: v66(0xbb82aa5e) = CONST 
    0x6b: v6b = EQ v66(0xbb82aa5e), v12
    0x799: v799(0x7a6) = CONST 
    0x79a: JUMPI v799(0x7a6), v6b

    Begin block 0x7a6
    prev=[0x65], succ=[]
    =================================
    0x7a7: v7a7(0x174) = CONST 
    0x7a8: CALLPRIVATE v7a7(0x174)

    Begin block 0x70
    prev=[0x65], succ=[0x79d, 0x7a9]
    =================================
    0x71: v71(0xc1e80334) = CONST 
    0x76: v76 = EQ v71(0xc1e80334), v12
    0x79b: v79b(0x7a9) = CONST 
    0x79c: JUMPI v79b(0x7a9), v76

    Begin block 0x79d
    prev=[0x0, 0x70], succ=[]
    =================================
    0x79e: v79e(0x7b) = CONST 
    0x79f: CALLPRIVATE v79e(0x7b)

    Begin block 0x7a9
    prev=[0x70], succ=[]
    =================================
    0x7aa: v7aa(0x189) = CONST 
    0x7ab: CALLPRIVATE v7aa(0x189)

    Begin block 0x1e
    prev=[0xd], succ=[0x7ac, 0x29]
    =================================
    0x1f: v1f(0xdcfbc0c7) = CONST 
    0x24: v24 = EQ v1f(0xdcfbc0c7), v12
    0x78d: v78d(0x7ac) = CONST 
    0x78e: JUMPI v78d(0x7ac), v24

    Begin block 0x7ac
    prev=[0x1e], succ=[]
    =================================
    0x7ad: v7ad(0x19e) = CONST 
    0x7ae: CALLPRIVATE v7ad(0x19e)

    Begin block 0x29
    prev=[0x1e], succ=[0x7af, 0x34]
    =================================
    0x2a: v2a(0xe992a041) = CONST 
    0x2f: v2f = EQ v2a(0xe992a041), v12
    0x78f: v78f(0x7af) = CONST 
    0x790: JUMPI v78f(0x7af), v2f

    Begin block 0x7af
    prev=[0x29], succ=[]
    =================================
    0x7b0: v7b0(0x1b3) = CONST 
    0x7b1: CALLPRIVATE v7b0(0x1b3)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x7b2]
    =================================
    0x35: v35(0xe9c714f2) = CONST 
    0x3a: v3a = EQ v35(0xe9c714f2), v12
    0x791: v791(0x7b2) = CONST 
    0x792: JUMPI v791(0x7b2), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x7b5]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x793: v793(0x7b5) = CONST 
    0x794: JUMPI v793(0x7b5), v45

    Begin block 0x4a
    prev=[0x3f], succ=[]
    =================================
    0x4a: v4a(0x7b) = CONST 
    0x4d: JUMP v4a(0x7b)

    Begin block 0x7b5
    prev=[0x3f], succ=[]
    =================================
    0x7b6: v7b6(0x1fb) = CONST 
    0x7b7: CALLPRIVATE v7b6(0x1fb)

    Begin block 0x7b2
    prev=[0x34], succ=[]
    =================================
    0x7b3: v7b3(0x1e6) = CONST 
    0x7b4: CALLPRIVATE v7b3(0x1e6)

}

function _setPendingAdmin(address)() public {
    Begin block 0x12f
    prev=[], succ=[0x137, 0x13b]
    =================================
    0x130: v130 = CALLVALUE 
    0x132: v132 = ISZERO v130
    0x133: v133(0x13b) = CONST 
    0x136: JUMPI v133(0x13b), v132

    Begin block 0x137
    prev=[0x12f], succ=[]
    =================================
    0x137: v137(0x0) = CONST 
    0x13a: REVERT v137(0x0), v137(0x0)

    Begin block 0x13b
    prev=[0x12f], succ=[0x14e, 0x152]
    =================================
    0x13d: v13d(0x635) = CONST 
    0x140: v140(0x4) = CONST 
    0x143: v143 = CALLDATASIZE 
    0x144: v144 = SUB v143, v140(0x4)
    0x145: v145(0x20) = CONST 
    0x148: v148 = LT v144, v145(0x20)
    0x149: v149 = ISZERO v148
    0x14a: v14a(0x152) = CONST 
    0x14d: JUMPI v14a(0x152), v149

    Begin block 0x14e
    prev=[0x13b], succ=[]
    =================================
    0x14e: v14e(0x0) = CONST 
    0x151: REVERT v14e(0x0), v14e(0x0)

    Begin block 0x152
    prev=[0x13b], succ=[0x21f]
    =================================
    0x154: v154 = CALLDATALOAD v140(0x4)
    0x155: v155(0x1) = CONST 
    0x157: v157(0x1) = CONST 
    0x159: v159(0xa0) = CONST 
    0x15b: v15b(0x10000000000000000000000000000000000000000) = SHL v159(0xa0), v157(0x1)
    0x15c: v15c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15b(0x10000000000000000000000000000000000000000), v155(0x1)
    0x15d: v15d = AND v15c(0xffffffffffffffffffffffffffffffffffffffff), v154
    0x15e: v15e(0x21f) = CONST 
    0x161: JUMP v15e(0x21f)

    Begin block 0x21f
    prev=[0x152], succ=[0x233, 0x245]
    =================================
    0x220: v220(0x0) = CONST 
    0x223: v223 = SLOAD v220(0x0)
    0x224: v224(0x1) = CONST 
    0x226: v226(0x1) = CONST 
    0x228: v228(0xa0) = CONST 
    0x22a: v22a(0x10000000000000000000000000000000000000000) = SHL v228(0xa0), v226(0x1)
    0x22b: v22b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22a(0x10000000000000000000000000000000000000000), v224(0x1)
    0x22c: v22c = AND v22b(0xffffffffffffffffffffffffffffffffffffffff), v223
    0x22d: v22d = CALLER 
    0x22e: v22e = EQ v22d, v22c
    0x22f: v22f(0x245) = CONST 
    0x232: JUMPI v22f(0x245), v22e

    Begin block 0x233
    prev=[0x21f], succ=[0x23e0x12f]
    =================================
    0x233: v233(0x23e) = CONST 
    0x236: v236(0x1) = CONST 
    0x238: v238(0xe) = CONST 
    0x23a: v23a(0x542) = CONST 
    0x23d: v23d_0 = CALLPRIVATE v23a(0x542), v238(0xe), v236(0x1), v233(0x23e)

    Begin block 0x23e0x12f
    prev=[0x233], succ=[0x2ab0x12f]
    =================================
    0x2410x12f: v12f241(0x2ab) = CONST 
    0x2440x12f: JUMP v12f241(0x2ab)

    Begin block 0x2ab0x12f
    prev=[0x23e0x12f, 0x2a70x12f], succ=[0x635]
    =================================
    0x2af0x12f: JUMP v13d(0x635)

    Begin block 0x635
    prev=[0x2ab0x12f], succ=[]
    =================================
    0x635_0x0: v635_0 = PHI v2a5(0x0), v23d_0
    0x636: v636(0x40) = CONST 
    0x639: v639 = MLOAD v636(0x40)
    0x63c: MSTORE v639, v635_0
    0x63d: v63d = MLOAD v636(0x40)
    0x641: v641(0x0) = SUB v639, v63d
    0x642: v642(0x20) = CONST 
    0x644: v644(0x20) = ADD v642(0x20), v641(0x0)
    0x646: RETURN v63d, v644(0x20)

    Begin block 0x245
    prev=[0x21f], succ=[0x2a70x12f]
    =================================
    0x246: v246(0x1) = CONST 
    0x249: v249 = SLOAD v246(0x1)
    0x24a: v24a(0x1) = CONST 
    0x24c: v24c(0x1) = CONST 
    0x24e: v24e(0xa0) = CONST 
    0x250: v250(0x10000000000000000000000000000000000000000) = SHL v24e(0xa0), v24c(0x1)
    0x251: v251(0xffffffffffffffffffffffffffffffffffffffff) = SUB v250(0x10000000000000000000000000000000000000000), v24a(0x1)
    0x254: v254 = AND v251(0xffffffffffffffffffffffffffffffffffffffff), v15d
    0x255: v255(0x1) = CONST 
    0x257: v257(0x1) = CONST 
    0x259: v259(0xa0) = CONST 
    0x25b: v25b(0x10000000000000000000000000000000000000000) = SHL v259(0xa0), v257(0x1)
    0x25c: v25c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25b(0x10000000000000000000000000000000000000000), v255(0x1)
    0x25d: v25d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v25c(0xffffffffffffffffffffffffffffffffffffffff)
    0x25f: v25f = AND v249, v25d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x261: v261 = OR v254, v25f
    0x264: SSTORE v246(0x1), v261
    0x265: v265(0x40) = CONST 
    0x268: v268 = MLOAD v265(0x40)
    0x26c: v26c = AND v249, v251(0xffffffffffffffffffffffffffffffffffffffff)
    0x26f: MSTORE v268, v26c
    0x270: v270(0x20) = CONST 
    0x273: v273 = ADD v268, v270(0x20)
    0x277: MSTORE v273, v254
    0x279: v279 = MLOAD v265(0x40)
    0x27a: v27a(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x29f: v29f(0x0) = SUB v268, v279
    0x2a2: v2a2(0x40) = ADD v265(0x40), v29f(0x0)
    0x2a4: LOG1 v279, v2a2(0x40), v27a(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x2a5: v2a5(0x0) = CONST 

    Begin block 0x2a70x12f
    prev=[0x245], succ=[0x2ab0x12f]
    =================================

}

function comptrollerImplementation()() public {
    Begin block 0x174
    prev=[], succ=[0x17c, 0x180]
    =================================
    0x175: v175 = CALLVALUE 
    0x177: v177 = ISZERO v175
    0x178: v178(0x180) = CONST 
    0x17b: JUMPI v178(0x180), v177

    Begin block 0x17c
    prev=[0x174], succ=[]
    =================================
    0x17c: v17c(0x0) = CONST 
    0x17f: REVERT v17c(0x0), v17c(0x0)

    Begin block 0x180
    prev=[0x174], succ=[0x2b0]
    =================================
    0x182: v182(0x666) = CONST 
    0x185: v185(0x2b0) = CONST 
    0x188: JUMP v185(0x2b0)

    Begin block 0x2b0
    prev=[0x180], succ=[0x666]
    =================================
    0x2b1: v2b1(0x2) = CONST 
    0x2b3: v2b3 = SLOAD v2b1(0x2)
    0x2b4: v2b4(0x1) = CONST 
    0x2b6: v2b6(0x1) = CONST 
    0x2b8: v2b8(0xa0) = CONST 
    0x2ba: v2ba(0x10000000000000000000000000000000000000000) = SHL v2b8(0xa0), v2b6(0x1)
    0x2bb: v2bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ba(0x10000000000000000000000000000000000000000), v2b4(0x1)
    0x2bc: v2bc = AND v2bb(0xffffffffffffffffffffffffffffffffffffffff), v2b3
    0x2be: JUMP v182(0x666)

    Begin block 0x666
    prev=[0x2b0], succ=[]
    =================================
    0x667: v667(0x40) = CONST 
    0x66a: v66a = MLOAD v667(0x40)
    0x66b: v66b(0x1) = CONST 
    0x66d: v66d(0x1) = CONST 
    0x66f: v66f(0xa0) = CONST 
    0x671: v671(0x10000000000000000000000000000000000000000) = SHL v66f(0xa0), v66d(0x1)
    0x672: v672(0xffffffffffffffffffffffffffffffffffffffff) = SUB v671(0x10000000000000000000000000000000000000000), v66b(0x1)
    0x675: v675 = AND v2bc, v672(0xffffffffffffffffffffffffffffffffffffffff)
    0x677: MSTORE v66a, v675
    0x678: v678 = MLOAD v667(0x40)
    0x67c: v67c(0x0) = SUB v66a, v678
    0x67d: v67d(0x20) = CONST 
    0x67f: v67f(0x20) = ADD v67d(0x20), v67c(0x0)
    0x681: RETURN v678, v67f(0x20)

}

function _acceptImplementation()() public {
    Begin block 0x189
    prev=[], succ=[0x191, 0x195]
    =================================
    0x18a: v18a = CALLVALUE 
    0x18c: v18c = ISZERO v18a
    0x18d: v18d(0x195) = CONST 
    0x190: JUMPI v18d(0x195), v18c

    Begin block 0x191
    prev=[0x189], succ=[]
    =================================
    0x191: v191(0x0) = CONST 
    0x194: REVERT v191(0x0), v191(0x0)

    Begin block 0x195
    prev=[0x189], succ=[0x2bfB0x195]
    =================================
    0x197: v197(0x6a1) = CONST 
    0x19a: v19a(0x2bf) = CONST 
    0x19d: JUMP v19a(0x2bf)

    Begin block 0x2bfB0x195
    prev=[0x195], succ=[0x2e5B0x195, 0x2d7B0x195]
    =================================
    0x2c0S0x195: v2c0V195(0x3) = CONST 
    0x2c2S0x195: v2c2V195 = SLOAD v2c0V195(0x3)
    0x2c3S0x195: v2c3V195(0x0) = CONST 
    0x2c6S0x195: v2c6V195(0x1) = CONST 
    0x2c8S0x195: v2c8V195(0x1) = CONST 
    0x2caS0x195: v2caV195(0xa0) = CONST 
    0x2ccS0x195: v2ccV195(0x10000000000000000000000000000000000000000) = SHL v2caV195(0xa0), v2c8V195(0x1)
    0x2cdS0x195: v2cdV195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ccV195(0x10000000000000000000000000000000000000000), v2c6V195(0x1)
    0x2ceS0x195: v2ceV195 = AND v2cdV195(0xffffffffffffffffffffffffffffffffffffffff), v2c2V195
    0x2cfS0x195: v2cfV195 = CALLER 
    0x2d0S0x195: v2d0V195 = EQ v2cfV195, v2ceV195
    0x2d1S0x195: v2d1V195 = ISZERO v2d0V195
    0x2d3S0x195: v2d3V195(0x2e5) = CONST 
    0x2d6S0x195: JUMPI v2d3V195(0x2e5), v2d1V195

    Begin block 0x2e5B0x195
    prev=[0x2bfB0x195, 0x2d7B0x195], succ=[0x2ebB0x195, 0x2fcB0x195]
    =================================
    0x2e5_0x0S0x195: v2e5_0V195 = PHI v2d1V195, v2e4V195
    0x2e6S0x195: v2e6V195 = ISZERO v2e5_0V195
    0x2e7S0x195: v2e7V195(0x2fc) = CONST 
    0x2eaS0x195: JUMPI v2e7V195(0x2fc), v2e6V195

    Begin block 0x2ebB0x195
    prev=[0x2e5B0x195], succ=[0x2f50x2bfB0x195]
    =================================
    0x2ebS0x195: v2ebV195(0x2f5) = CONST 
    0x2eeS0x195: v2eeV195(0x1) = CONST 
    0x2f1S0x195: v2f1V195(0x542) = CONST 
    0x2f4S0x195: v2f4_0V195 = CALLPRIVATE v2f1V195(0x542), v2eeV195(0x1), v2eeV195(0x1), v2ebV195(0x2f5)

    Begin block 0x2f50x2bfB0x195
    prev=[0x2ebB0x195], succ=[0x3b70x2bfB0x195]
    =================================
    0x2f80x2bfS0x195: v2bf2f8V195(0x3b7) = CONST 
    0x2fb0x2bfS0x195: JUMP v2bf2f8V195(0x3b7)

    Begin block 0x3b70x2bfB0x195
    prev=[0x2f50x2bfB0x195, 0x3b20x2bfB0x195], succ=[0x6a1]
    =================================
    0x3b70x2bf_0x0S0x195: v3b72bf_0V195 = PHI v2f4_0V195, v3b0V195(0x0)
    0x3b90x2bfS0x195: JUMP v197(0x6a1)

    Begin block 0x6a1
    prev=[0x3b70x2bfB0x195], succ=[]
    =================================
    0x6a2: v6a2(0x40) = CONST 
    0x6a5: v6a5 = MLOAD v6a2(0x40)
    0x6a8: MSTORE v6a5, v3b72bf_0V195
    0x6a9: v6a9 = MLOAD v6a2(0x40)
    0x6ad: v6ad(0x0) = SUB v6a5, v6a9
    0x6ae: v6ae(0x20) = CONST 
    0x6b0: v6b0(0x20) = ADD v6ae(0x20), v6ad(0x0)
    0x6b2: RETURN v6a9, v6b0(0x20)

    Begin block 0x2fcB0x195
    prev=[0x2e5B0x195], succ=[0x3b20x2bfB0x195]
    =================================
    0x2fdS0x195: v2fdV195(0x2) = CONST 
    0x300S0x195: v300V195 = SLOAD v2fdV195(0x2)
    0x301S0x195: v301V195(0x3) = CONST 
    0x304S0x195: v304V195 = SLOAD v301V195(0x3)
    0x305S0x195: v305V195(0x1) = CONST 
    0x307S0x195: v307V195(0x1) = CONST 
    0x309S0x195: v309V195(0xa0) = CONST 
    0x30bS0x195: v30bV195(0x10000000000000000000000000000000000000000) = SHL v309V195(0xa0), v307V195(0x1)
    0x30cS0x195: v30cV195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30bV195(0x10000000000000000000000000000000000000000), v305V195(0x1)
    0x30fS0x195: v30fV195 = AND v304V195, v30cV195(0xffffffffffffffffffffffffffffffffffffffff)
    0x310S0x195: v310V195(0x1) = CONST 
    0x312S0x195: v312V195(0x1) = CONST 
    0x314S0x195: v314V195(0xa0) = CONST 
    0x316S0x195: v316V195(0x10000000000000000000000000000000000000000) = SHL v314V195(0xa0), v312V195(0x1)
    0x317S0x195: v317V195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v316V195(0x10000000000000000000000000000000000000000), v310V195(0x1)
    0x318S0x195: v318V195(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v317V195(0xffffffffffffffffffffffffffffffffffffffff)
    0x31bS0x195: v31bV195 = AND v300V195, v318V195(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x31dS0x195: v31dV195 = OR v30fV195, v31bV195
    0x321S0x195: SSTORE v2fdV195(0x2), v31dV195
    0x324S0x195: v324V195 = AND v304V195, v318V195(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x327S0x195: SSTORE v301V195(0x3), v324V195
    0x328S0x195: v328V195(0x40) = CONST 
    0x32bS0x195: v32bV195 = MLOAD v328V195(0x40)
    0x32eS0x195: v32eV195 = AND v30cV195(0xffffffffffffffffffffffffffffffffffffffff), v300V195
    0x331S0x195: MSTORE v32bV195, v32eV195
    0x335S0x195: v335V195 = AND v30cV195(0xffffffffffffffffffffffffffffffffffffffff), v31dV195
    0x336S0x195: v336V195(0x20) = CONST 
    0x339S0x195: v339V195 = ADD v32bV195, v336V195(0x20)
    0x33aS0x195: MSTORE v339V195, v335V195
    0x33cS0x195: v33cV195 = MLOAD v328V195(0x40)
    0x33fS0x195: v33fV195(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x364S0x195: v364V195(0x0) = SUB v32bV195, v33cV195
    0x365S0x195: v365V195(0x40) = ADD v364V195(0x0), v328V195(0x40)
    0x367S0x195: LOG1 v33cV195, v365V195(0x40), v33fV195(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x368S0x195: v368V195(0x3) = CONST 
    0x36aS0x195: v36aV195 = SLOAD v368V195(0x3)
    0x36bS0x195: v36bV195(0x40) = CONST 
    0x36eS0x195: v36eV195 = MLOAD v36bV195(0x40)
    0x36fS0x195: v36fV195(0x1) = CONST 
    0x371S0x195: v371V195(0x1) = CONST 
    0x373S0x195: v373V195(0xa0) = CONST 
    0x375S0x195: v375V195(0x10000000000000000000000000000000000000000) = SHL v373V195(0xa0), v371V195(0x1)
    0x376S0x195: v376V195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v375V195(0x10000000000000000000000000000000000000000), v36fV195(0x1)
    0x379S0x195: v379V195 = AND v30fV195, v376V195(0xffffffffffffffffffffffffffffffffffffffff)
    0x37bS0x195: MSTORE v36eV195, v379V195
    0x37eS0x195: v37eV195 = AND v36aV195, v376V195(0xffffffffffffffffffffffffffffffffffffffff)
    0x37fS0x195: v37fV195(0x20) = CONST 
    0x382S0x195: v382V195 = ADD v36eV195, v37fV195(0x20)
    0x383S0x195: MSTORE v382V195, v37eV195
    0x385S0x195: v385V195 = MLOAD v36bV195(0x40)
    0x386S0x195: v386V195(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x3aaS0x195: v3aaV195(0x0) = SUB v36eV195, v385V195
    0x3adS0x195: v3adV195(0x40) = ADD v36bV195(0x40), v3aaV195(0x0)
    0x3afS0x195: LOG1 v385V195, v3adV195(0x40), v386V195(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x3b0S0x195: v3b0V195(0x0) = CONST 

    Begin block 0x3b20x2bfB0x195
    prev=[0x2fcB0x195], succ=[0x3b70x2bfB0x195]
    =================================

    Begin block 0x2d7B0x195
    prev=[0x2bfB0x195], succ=[0x2e5B0x195]
    =================================
    0x2d8S0x195: v2d8V195(0x3) = CONST 
    0x2daS0x195: v2daV195 = SLOAD v2d8V195(0x3)
    0x2dbS0x195: v2dbV195(0x1) = CONST 
    0x2ddS0x195: v2ddV195(0x1) = CONST 
    0x2dfS0x195: v2dfV195(0xa0) = CONST 
    0x2e1S0x195: v2e1V195(0x10000000000000000000000000000000000000000) = SHL v2dfV195(0xa0), v2ddV195(0x1)
    0x2e2S0x195: v2e2V195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e1V195(0x10000000000000000000000000000000000000000), v2dbV195(0x1)
    0x2e3S0x195: v2e3V195 = AND v2e2V195(0xffffffffffffffffffffffffffffffffffffffff), v2daV195
    0x2e4S0x195: v2e4V195 = ISZERO v2e3V195

}

function pendingComptrollerImplementation()() public {
    Begin block 0x19e
    prev=[], succ=[0x1a6, 0x1aa]
    =================================
    0x19f: v19f = CALLVALUE 
    0x1a1: v1a1 = ISZERO v19f
    0x1a2: v1a2(0x1aa) = CONST 
    0x1a5: JUMPI v1a2(0x1aa), v1a1

    Begin block 0x1a6
    prev=[0x19e], succ=[]
    =================================
    0x1a6: v1a6(0x0) = CONST 
    0x1a9: REVERT v1a6(0x0), v1a6(0x0)

    Begin block 0x1aa
    prev=[0x19e], succ=[0x3ba]
    =================================
    0x1ac: v1ac(0x6d2) = CONST 
    0x1af: v1af(0x3ba) = CONST 
    0x1b2: JUMP v1af(0x3ba)

    Begin block 0x3ba
    prev=[0x1aa], succ=[0x6d2]
    =================================
    0x3bb: v3bb(0x3) = CONST 
    0x3bd: v3bd = SLOAD v3bb(0x3)
    0x3be: v3be(0x1) = CONST 
    0x3c0: v3c0(0x1) = CONST 
    0x3c2: v3c2(0xa0) = CONST 
    0x3c4: v3c4(0x10000000000000000000000000000000000000000) = SHL v3c2(0xa0), v3c0(0x1)
    0x3c5: v3c5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c4(0x10000000000000000000000000000000000000000), v3be(0x1)
    0x3c6: v3c6 = AND v3c5(0xffffffffffffffffffffffffffffffffffffffff), v3bd
    0x3c8: JUMP v1ac(0x6d2)

    Begin block 0x6d2
    prev=[0x3ba], succ=[]
    =================================
    0x6d3: v6d3(0x40) = CONST 
    0x6d6: v6d6 = MLOAD v6d3(0x40)
    0x6d7: v6d7(0x1) = CONST 
    0x6d9: v6d9(0x1) = CONST 
    0x6db: v6db(0xa0) = CONST 
    0x6dd: v6dd(0x10000000000000000000000000000000000000000) = SHL v6db(0xa0), v6d9(0x1)
    0x6de: v6de(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6dd(0x10000000000000000000000000000000000000000), v6d7(0x1)
    0x6e1: v6e1 = AND v3c6, v6de(0xffffffffffffffffffffffffffffffffffffffff)
    0x6e3: MSTORE v6d6, v6e1
    0x6e4: v6e4 = MLOAD v6d3(0x40)
    0x6e8: v6e8(0x0) = SUB v6d6, v6e4
    0x6e9: v6e9(0x20) = CONST 
    0x6eb: v6eb(0x20) = ADD v6e9(0x20), v6e8(0x0)
    0x6ed: RETURN v6e4, v6eb(0x20)

}

function _setPendingImplementation(address)() public {
    Begin block 0x1b3
    prev=[], succ=[0x1bb, 0x1bf]
    =================================
    0x1b4: v1b4 = CALLVALUE 
    0x1b6: v1b6 = ISZERO v1b4
    0x1b7: v1b7(0x1bf) = CONST 
    0x1ba: JUMPI v1b7(0x1bf), v1b6

    Begin block 0x1bb
    prev=[0x1b3], succ=[]
    =================================
    0x1bb: v1bb(0x0) = CONST 
    0x1be: REVERT v1bb(0x0), v1bb(0x0)

    Begin block 0x1bf
    prev=[0x1b3], succ=[0x1d2, 0x1d6]
    =================================
    0x1c1: v1c1(0x70d) = CONST 
    0x1c4: v1c4(0x4) = CONST 
    0x1c7: v1c7 = CALLDATASIZE 
    0x1c8: v1c8 = SUB v1c7, v1c4(0x4)
    0x1c9: v1c9(0x20) = CONST 
    0x1cc: v1cc = LT v1c8, v1c9(0x20)
    0x1cd: v1cd = ISZERO v1cc
    0x1ce: v1ce(0x1d6) = CONST 
    0x1d1: JUMPI v1ce(0x1d6), v1cd

    Begin block 0x1d2
    prev=[0x1bf], succ=[]
    =================================
    0x1d2: v1d2(0x0) = CONST 
    0x1d5: REVERT v1d2(0x0), v1d2(0x0)

    Begin block 0x1d6
    prev=[0x1bf], succ=[0x3c9]
    =================================
    0x1d8: v1d8 = CALLDATALOAD v1c4(0x4)
    0x1d9: v1d9(0x1) = CONST 
    0x1db: v1db(0x1) = CONST 
    0x1dd: v1dd(0xa0) = CONST 
    0x1df: v1df(0x10000000000000000000000000000000000000000) = SHL v1dd(0xa0), v1db(0x1)
    0x1e0: v1e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1df(0x10000000000000000000000000000000000000000), v1d9(0x1)
    0x1e1: v1e1 = AND v1e0(0xffffffffffffffffffffffffffffffffffffffff), v1d8
    0x1e2: v1e2(0x3c9) = CONST 
    0x1e5: JUMP v1e2(0x3c9)

    Begin block 0x3c9
    prev=[0x1d6], succ=[0x3dd, 0x3e8]
    =================================
    0x3ca: v3ca(0x0) = CONST 
    0x3cd: v3cd = SLOAD v3ca(0x0)
    0x3ce: v3ce(0x1) = CONST 
    0x3d0: v3d0(0x1) = CONST 
    0x3d2: v3d2(0xa0) = CONST 
    0x3d4: v3d4(0x10000000000000000000000000000000000000000) = SHL v3d2(0xa0), v3d0(0x1)
    0x3d5: v3d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d4(0x10000000000000000000000000000000000000000), v3ce(0x1)
    0x3d6: v3d6 = AND v3d5(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0x3d7: v3d7 = CALLER 
    0x3d8: v3d8 = EQ v3d7, v3d6
    0x3d9: v3d9(0x3e8) = CONST 
    0x3dc: JUMPI v3d9(0x3e8), v3d8

    Begin block 0x3dd
    prev=[0x3c9], succ=[0x23e0x1b3]
    =================================
    0x3dd: v3dd(0x23e) = CONST 
    0x3e0: v3e0(0x1) = CONST 
    0x3e2: v3e2(0xf) = CONST 
    0x3e4: v3e4(0x542) = CONST 
    0x3e7: v3e7_0 = CALLPRIVATE v3e4(0x542), v3e2(0xf), v3e0(0x1), v3dd(0x23e)

    Begin block 0x23e0x1b3
    prev=[0x3dd], succ=[0x2ab0x1b3]
    =================================
    0x2410x1b3: v1b3241(0x2ab) = CONST 
    0x2440x1b3: JUMP v1b3241(0x2ab)

    Begin block 0x2ab0x1b3
    prev=[0x23e0x1b3, 0x2a70x1b3], succ=[0x70d]
    =================================
    0x2af0x1b3: JUMP v1c1(0x70d)

    Begin block 0x70d
    prev=[0x2ab0x1b3], succ=[]
    =================================
    0x70d_0x0: v70d_0 = PHI v447(0x0), v3e7_0
    0x70e: v70e(0x40) = CONST 
    0x711: v711 = MLOAD v70e(0x40)
    0x714: MSTORE v711, v70d_0
    0x715: v715 = MLOAD v70e(0x40)
    0x719: v719(0x0) = SUB v711, v715
    0x71a: v71a(0x20) = CONST 
    0x71c: v71c(0x20) = ADD v71a(0x20), v719(0x0)
    0x71e: RETURN v715, v71c(0x20)

    Begin block 0x3e8
    prev=[0x3c9], succ=[0x2a70x1b3]
    =================================
    0x3e9: v3e9(0x3) = CONST 
    0x3ec: v3ec = SLOAD v3e9(0x3)
    0x3ed: v3ed(0x1) = CONST 
    0x3ef: v3ef(0x1) = CONST 
    0x3f1: v3f1(0xa0) = CONST 
    0x3f3: v3f3(0x10000000000000000000000000000000000000000) = SHL v3f1(0xa0), v3ef(0x1)
    0x3f4: v3f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f3(0x10000000000000000000000000000000000000000), v3ed(0x1)
    0x3f7: v3f7 = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v1e1
    0x3f8: v3f8(0x1) = CONST 
    0x3fa: v3fa(0x1) = CONST 
    0x3fc: v3fc(0xa0) = CONST 
    0x3fe: v3fe(0x10000000000000000000000000000000000000000) = SHL v3fc(0xa0), v3fa(0x1)
    0x3ff: v3ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fe(0x10000000000000000000000000000000000000000), v3f8(0x1)
    0x400: v400(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x402: v402 = AND v3ec, v400(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x403: v403 = OR v402, v3f7
    0x407: SSTORE v3e9(0x3), v403
    0x408: v408(0x40) = CONST 
    0x40b: v40b = MLOAD v408(0x40)
    0x40e: v40e = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v3ec
    0x411: MSTORE v40b, v40e
    0x415: v415 = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v403
    0x416: v416(0x20) = CONST 
    0x419: v419 = ADD v40b, v416(0x20)
    0x41a: MSTORE v419, v415
    0x41c: v41c = MLOAD v408(0x40)
    0x41d: v41d(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x441: v441(0x0) = SUB v40b, v41c
    0x444: v444(0x40) = ADD v408(0x40), v441(0x0)
    0x446: LOG1 v41c, v444(0x40), v41d(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x447: v447(0x0) = CONST 
    0x449: v449(0x2a7) = CONST 
    0x44c: JUMP v449(0x2a7)

    Begin block 0x2a70x1b3
    prev=[0x3e8], succ=[0x2ab0x1b3]
    =================================

}

function _acceptAdmin()() public {
    Begin block 0x1e6
    prev=[], succ=[0x1ee, 0x1f2]
    =================================
    0x1e7: v1e7 = CALLVALUE 
    0x1e9: v1e9 = ISZERO v1e7
    0x1ea: v1ea(0x1f2) = CONST 
    0x1ed: JUMPI v1ea(0x1f2), v1e9

    Begin block 0x1ee
    prev=[0x1e6], succ=[]
    =================================
    0x1ee: v1ee(0x0) = CONST 
    0x1f1: REVERT v1ee(0x0), v1ee(0x0)

    Begin block 0x1f2
    prev=[0x1e6], succ=[0x44dB0x1f2]
    =================================
    0x1f4: v1f4(0x73e) = CONST 
    0x1f7: v1f7(0x44d) = CONST 
    0x1fa: JUMP v1f7(0x44d)

    Begin block 0x44dB0x1f2
    prev=[0x1f2], succ=[0x468B0x1f2, 0x465B0x1f2]
    =================================
    0x44eS0x1f2: v44eV1f2(0x1) = CONST 
    0x450S0x1f2: v450V1f2 = SLOAD v44eV1f2(0x1)
    0x451S0x1f2: v451V1f2(0x0) = CONST 
    0x454S0x1f2: v454V1f2(0x1) = CONST 
    0x456S0x1f2: v456V1f2(0x1) = CONST 
    0x458S0x1f2: v458V1f2(0xa0) = CONST 
    0x45aS0x1f2: v45aV1f2(0x10000000000000000000000000000000000000000) = SHL v458V1f2(0xa0), v456V1f2(0x1)
    0x45bS0x1f2: v45bV1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45aV1f2(0x10000000000000000000000000000000000000000), v454V1f2(0x1)
    0x45cS0x1f2: v45cV1f2 = AND v45bV1f2(0xffffffffffffffffffffffffffffffffffffffff), v450V1f2
    0x45dS0x1f2: v45dV1f2 = CALLER 
    0x45eS0x1f2: v45eV1f2 = EQ v45dV1f2, v45cV1f2
    0x45fS0x1f2: v45fV1f2 = ISZERO v45eV1f2
    0x461S0x1f2: v461V1f2(0x468) = CONST 
    0x464S0x1f2: JUMPI v461V1f2(0x468), v45fV1f2

    Begin block 0x468B0x1f2
    prev=[0x44dB0x1f2, 0x465B0x1f2], succ=[0x46eB0x1f2, 0x479B0x1f2]
    =================================
    0x468_0x0S0x1f2: v468_0V1f2 = PHI v45fV1f2, v467V1f2
    0x469S0x1f2: v469V1f2 = ISZERO v468_0V1f2
    0x46aS0x1f2: v46aV1f2(0x479) = CONST 
    0x46dS0x1f2: JUMPI v46aV1f2(0x479), v469V1f2

    Begin block 0x46eB0x1f2
    prev=[0x468B0x1f2], succ=[0x2f50x44dB0x1f2]
    =================================
    0x46eS0x1f2: v46eV1f2(0x2f5) = CONST 
    0x471S0x1f2: v471V1f2(0x1) = CONST 
    0x473S0x1f2: v473V1f2(0x0) = CONST 
    0x475S0x1f2: v475V1f2(0x542) = CONST 
    0x478S0x1f2: v478_0V1f2 = CALLPRIVATE v475V1f2(0x542), v473V1f2(0x0), v471V1f2(0x1), v46eV1f2(0x2f5)

    Begin block 0x2f50x44dB0x1f2
    prev=[0x46eB0x1f2], succ=[0x3b70x44dB0x1f2]
    =================================
    0x2f80x44dS0x1f2: v44d2f8V1f2(0x3b7) = CONST 
    0x2fb0x44dS0x1f2: JUMP v44d2f8V1f2(0x3b7)

    Begin block 0x3b70x44dB0x1f2
    prev=[0x2f50x44dB0x1f2, 0x3b20x44dB0x1f2], succ=[0x73e]
    =================================
    0x3b70x44d_0x0S0x1f2: v3b744d_0V1f2 = PHI v478_0V1f2, v52dV1f2(0x0)
    0x3b90x44dS0x1f2: JUMP v1f4(0x73e)

    Begin block 0x73e
    prev=[0x3b70x44dB0x1f2], succ=[]
    =================================
    0x73f: v73f(0x40) = CONST 
    0x742: v742 = MLOAD v73f(0x40)
    0x745: MSTORE v742, v3b744d_0V1f2
    0x746: v746 = MLOAD v73f(0x40)
    0x74a: v74a(0x0) = SUB v742, v746
    0x74b: v74b(0x20) = CONST 
    0x74d: v74d(0x20) = ADD v74b(0x20), v74a(0x0)
    0x74f: RETURN v746, v74d(0x20)

    Begin block 0x479B0x1f2
    prev=[0x468B0x1f2], succ=[0x3b20x44dB0x1f2]
    =================================
    0x47aS0x1f2: v47aV1f2(0x0) = CONST 
    0x47dS0x1f2: v47dV1f2 = SLOAD v47aV1f2(0x0)
    0x47eS0x1f2: v47eV1f2(0x1) = CONST 
    0x481S0x1f2: v481V1f2 = SLOAD v47eV1f2(0x1)
    0x482S0x1f2: v482V1f2(0x1) = CONST 
    0x484S0x1f2: v484V1f2(0x1) = CONST 
    0x486S0x1f2: v486V1f2(0xa0) = CONST 
    0x488S0x1f2: v488V1f2(0x10000000000000000000000000000000000000000) = SHL v486V1f2(0xa0), v484V1f2(0x1)
    0x489S0x1f2: v489V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v488V1f2(0x10000000000000000000000000000000000000000), v482V1f2(0x1)
    0x48cS0x1f2: v48cV1f2 = AND v481V1f2, v489V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x48dS0x1f2: v48dV1f2(0x1) = CONST 
    0x48fS0x1f2: v48fV1f2(0x1) = CONST 
    0x491S0x1f2: v491V1f2(0xa0) = CONST 
    0x493S0x1f2: v493V1f2(0x10000000000000000000000000000000000000000) = SHL v491V1f2(0xa0), v48fV1f2(0x1)
    0x494S0x1f2: v494V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v493V1f2(0x10000000000000000000000000000000000000000), v48dV1f2(0x1)
    0x495S0x1f2: v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v494V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x498S0x1f2: v498V1f2 = AND v47dV1f2, v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x49aS0x1f2: v49aV1f2 = OR v48cV1f2, v498V1f2
    0x49eS0x1f2: SSTORE v47aV1f2(0x0), v49aV1f2
    0x4a1S0x1f2: v4a1V1f2 = AND v481V1f2, v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4a4S0x1f2: SSTORE v47eV1f2(0x1), v4a1V1f2
    0x4a5S0x1f2: v4a5V1f2(0x40) = CONST 
    0x4a8S0x1f2: v4a8V1f2 = MLOAD v4a5V1f2(0x40)
    0x4abS0x1f2: v4abV1f2 = AND v489V1f2(0xffffffffffffffffffffffffffffffffffffffff), v47dV1f2
    0x4aeS0x1f2: MSTORE v4a8V1f2, v4abV1f2
    0x4b2S0x1f2: v4b2V1f2 = AND v489V1f2(0xffffffffffffffffffffffffffffffffffffffff), v49aV1f2
    0x4b3S0x1f2: v4b3V1f2(0x20) = CONST 
    0x4b6S0x1f2: v4b6V1f2 = ADD v4a8V1f2, v4b3V1f2(0x20)
    0x4b7S0x1f2: MSTORE v4b6V1f2, v4b2V1f2
    0x4b9S0x1f2: v4b9V1f2 = MLOAD v4a5V1f2(0x40)
    0x4bcS0x1f2: v4bcV1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x4e1S0x1f2: v4e1V1f2(0x0) = SUB v4a8V1f2, v4b9V1f2
    0x4e2S0x1f2: v4e2V1f2(0x40) = ADD v4e1V1f2(0x0), v4a5V1f2(0x40)
    0x4e4S0x1f2: LOG1 v4b9V1f2, v4e2V1f2(0x40), v4bcV1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x4e5S0x1f2: v4e5V1f2(0x1) = CONST 
    0x4e7S0x1f2: v4e7V1f2 = SLOAD v4e5V1f2(0x1)
    0x4e8S0x1f2: v4e8V1f2(0x40) = CONST 
    0x4ebS0x1f2: v4ebV1f2 = MLOAD v4e8V1f2(0x40)
    0x4ecS0x1f2: v4ecV1f2(0x1) = CONST 
    0x4eeS0x1f2: v4eeV1f2(0x1) = CONST 
    0x4f0S0x1f2: v4f0V1f2(0xa0) = CONST 
    0x4f2S0x1f2: v4f2V1f2(0x10000000000000000000000000000000000000000) = SHL v4f0V1f2(0xa0), v4eeV1f2(0x1)
    0x4f3S0x1f2: v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f2V1f2(0x10000000000000000000000000000000000000000), v4ecV1f2(0x1)
    0x4f6S0x1f2: v4f6V1f2 = AND v48cV1f2, v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f8S0x1f2: MSTORE v4ebV1f2, v4f6V1f2
    0x4fbS0x1f2: v4fbV1f2 = AND v4e7V1f2, v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4fcS0x1f2: v4fcV1f2(0x20) = CONST 
    0x4ffS0x1f2: v4ffV1f2 = ADD v4ebV1f2, v4fcV1f2(0x20)
    0x500S0x1f2: MSTORE v4ffV1f2, v4fbV1f2
    0x502S0x1f2: v502V1f2 = MLOAD v4e8V1f2(0x40)
    0x503S0x1f2: v503V1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x527S0x1f2: v527V1f2(0x0) = SUB v4ebV1f2, v502V1f2
    0x52aS0x1f2: v52aV1f2(0x40) = ADD v4e8V1f2(0x40), v527V1f2(0x0)
    0x52cS0x1f2: LOG1 v502V1f2, v52aV1f2(0x40), v503V1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x52dS0x1f2: v52dV1f2(0x0) = CONST 
    0x52fS0x1f2: v52fV1f2(0x3b2) = CONST 
    0x532S0x1f2: JUMP v52fV1f2(0x3b2)

    Begin block 0x3b20x44dB0x1f2
    prev=[0x479B0x1f2], succ=[0x3b70x44dB0x1f2]
    =================================

    Begin block 0x465B0x1f2
    prev=[0x44dB0x1f2], succ=[0x468B0x1f2]
    =================================
    0x466S0x1f2: v466V1f2 = CALLER 
    0x467S0x1f2: v467V1f2 = ISZERO v466V1f2

}

function admin()() public {
    Begin block 0x1fb
    prev=[], succ=[0x203, 0x207]
    =================================
    0x1fc: v1fc = CALLVALUE 
    0x1fe: v1fe = ISZERO v1fc
    0x1ff: v1ff(0x207) = CONST 
    0x202: JUMPI v1ff(0x207), v1fe

    Begin block 0x203
    prev=[0x1fb], succ=[]
    =================================
    0x203: v203(0x0) = CONST 
    0x206: REVERT v203(0x0), v203(0x0)

    Begin block 0x207
    prev=[0x1fb], succ=[0x533]
    =================================
    0x209: v209(0x76f) = CONST 
    0x20c: v20c(0x533) = CONST 
    0x20f: JUMP v20c(0x533)

    Begin block 0x533
    prev=[0x207], succ=[0x76f]
    =================================
    0x534: v534(0x0) = CONST 
    0x536: v536 = SLOAD v534(0x0)
    0x537: v537(0x1) = CONST 
    0x539: v539(0x1) = CONST 
    0x53b: v53b(0xa0) = CONST 
    0x53d: v53d(0x10000000000000000000000000000000000000000) = SHL v53b(0xa0), v539(0x1)
    0x53e: v53e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53d(0x10000000000000000000000000000000000000000), v537(0x1)
    0x53f: v53f = AND v53e(0xffffffffffffffffffffffffffffffffffffffff), v536
    0x541: JUMP v209(0x76f)

    Begin block 0x76f
    prev=[0x533], succ=[]
    =================================
    0x770: v770(0x40) = CONST 
    0x773: v773 = MLOAD v770(0x40)
    0x774: v774(0x1) = CONST 
    0x776: v776(0x1) = CONST 
    0x778: v778(0xa0) = CONST 
    0x77a: v77a(0x10000000000000000000000000000000000000000) = SHL v778(0xa0), v776(0x1)
    0x77b: v77b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v77a(0x10000000000000000000000000000000000000000), v774(0x1)
    0x77e: v77e = AND v53f, v77b(0xffffffffffffffffffffffffffffffffffffffff)
    0x780: MSTORE v773, v77e
    0x781: v781 = MLOAD v770(0x40)
    0x785: v785(0x0) = SUB v773, v781
    0x786: v786(0x20) = CONST 
    0x788: v788(0x20) = ADD v786(0x20), v785(0x0)
    0x78a: RETURN v781, v788(0x20)

}

function 0x542(0x542arg0x0, 0x542arg0x1, 0x542arg0x2) private {
    Begin block 0x542
    prev=[], succ=[0x570, 0x571]
    =================================
    0x543: v543(0x0) = CONST 
    0x545: v545(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0) = CONST 
    0x567: v567(0x11) = CONST 
    0x56a: v56a = GT v542arg1, v567(0x11)
    0x56b: v56b = ISZERO v56a
    0x56c: v56c(0x571) = CONST 
    0x56f: JUMPI v56c(0x571), v56b

    Begin block 0x570
    prev=[0x542], succ=[]
    =================================
    0x570: THROW 

    Begin block 0x571
    prev=[0x542], succ=[0x57c, 0x57d]
    =================================
    0x573: v573(0x13) = CONST 
    0x576: v576 = GT v542arg0, v573(0x13)
    0x577: v577 = ISZERO v576
    0x578: v578(0x57d) = CONST 
    0x57b: JUMPI v578(0x57d), v577

    Begin block 0x57c
    prev=[0x571], succ=[]
    =================================
    0x57c: THROW 

    Begin block 0x57d
    prev=[0x571], succ=[0x5a7, 0x5a8]
    =================================
    0x57e: v57e(0x40) = CONST 
    0x581: v581 = MLOAD v57e(0x40)
    0x584: MSTORE v581, v542arg1
    0x585: v585(0x20) = CONST 
    0x588: v588 = ADD v581, v585(0x20)
    0x58c: MSTORE v588, v542arg0
    0x58d: v58d(0x0) = CONST 
    0x591: v591 = ADD v57e(0x40), v581
    0x592: MSTORE v591, v58d(0x0)
    0x593: v593 = MLOAD v57e(0x40)
    0x597: v597(0x0) = SUB v581, v593
    0x598: v598(0x60) = CONST 
    0x59a: v59a(0x60) = ADD v598(0x60), v597(0x0)
    0x59c: LOG1 v593, v59a(0x60), v545(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0)
    0x59e: v59e(0x11) = CONST 
    0x5a1: v5a1 = GT v542arg1, v59e(0x11)
    0x5a2: v5a2 = ISZERO v5a1
    0x5a3: v5a3(0x5a8) = CONST 
    0x5a6: JUMPI v5a3(0x5a8), v5a2

    Begin block 0x5a7
    prev=[0x57d], succ=[]
    =================================
    0x5a7: THROW 

    Begin block 0x5a8
    prev=[0x57d], succ=[]
    =================================
    0x5ae: RETURNPRIVATE v542arg2, v542arg1

}

function fallback()() public {
    Begin block 0x7b
    prev=[], succ=[0xbd, 0xde]
    =================================
    0x7c: v7c(0x2) = CONST 
    0x7e: v7e = SLOAD v7c(0x2)
    0x7f: v7f(0x40) = CONST 
    0x81: v81 = MLOAD v7f(0x40)
    0x82: v82(0x0) = CONST 
    0x85: v85(0x1) = CONST 
    0x87: v87(0x1) = CONST 
    0x89: v89(0xa0) = CONST 
    0x8b: v8b(0x10000000000000000000000000000000000000000) = SHL v89(0xa0), v87(0x1)
    0x8c: v8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8b(0x10000000000000000000000000000000000000000), v85(0x1)
    0x8d: v8d = AND v8c(0xffffffffffffffffffffffffffffffffffffffff), v7e
    0x91: v91 = CALLDATASIZE 
    0x99: CALLDATACOPY v81, v82(0x0), v91
    0x9a: v9a(0x40) = CONST 
    0x9c: v9c = MLOAD v9a(0x40)
    0x9e: v9e = ADD v81, v91
    0xa1: va1(0x0) = CONST 
    0xab: vab = SUB v9e, v9c
    0xae: vae = GAS 
    0xaf: vaf = DELEGATECALL vae, v8d, v9c, vab, v9c, va1(0x0)
    0xb3: vb3 = RETURNDATASIZE 
    0xb5: vb5(0x0) = CONST 
    0xb8: vb8 = EQ vb3, vb5(0x0)
    0xb9: vb9(0xde) = CONST 
    0xbc: JUMPI vb9(0xde), vb8

    Begin block 0xbd
    prev=[0x7b], succ=[0xe3]
    =================================
    0xbd: vbd(0x40) = CONST 
    0xbf: vbf = MLOAD vbd(0x40)
    0xc2: vc2(0x1f) = CONST 
    0xc4: vc4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vc2(0x1f)
    0xc5: vc5(0x3f) = CONST 
    0xc7: vc7 = RETURNDATASIZE 
    0xc8: vc8 = ADD vc7, vc5(0x3f)
    0xc9: vc9 = AND vc8, vc4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xcb: vcb = ADD vbf, vc9
    0xcc: vcc(0x40) = CONST 
    0xce: MSTORE vcc(0x40), vcb
    0xcf: vcf = RETURNDATASIZE 
    0xd1: MSTORE vbf, vcf
    0xd2: vd2 = RETURNDATASIZE 
    0xd3: vd3(0x0) = CONST 
    0xd5: vd5(0x20) = CONST 
    0xd8: vd8 = ADD vbf, vd5(0x20)
    0xd9: RETURNDATACOPY vd8, vd3(0x0), vd2
    0xda: vda(0xe3) = CONST 
    0xdd: JUMP vda(0xe3)

    Begin block 0xe3
    prev=[0xbd, 0xde], succ=[0xf7, 0xfa]
    =================================
    0xe8: ve8(0x40) = CONST 
    0xea: vea = MLOAD ve8(0x40)
    0xeb: veb = RETURNDATASIZE 
    0xec: vec(0x0) = CONST 
    0xef: RETURNDATACOPY vea, vec(0x0), veb
    0xf2: vf2 = ISZERO vaf
    0xf3: vf3(0xfa) = CONST 
    0xf6: JUMPI vf3(0xfa), vf2

    Begin block 0xf7
    prev=[0xe3], succ=[]
    =================================
    0xf7: vf7 = RETURNDATASIZE 
    0xf9: RETURN vea, vf7

    Begin block 0xfa
    prev=[0xe3], succ=[]
    =================================
    0xfb: vfb = RETURNDATASIZE 
    0xfd: REVERT vea, vfb

    Begin block 0xde
    prev=[0x7b], succ=[0xe3]
    =================================
    0xdf: vdf(0x60) = CONST 

}

function pendingAdmin()() public {
    Begin block 0xfe
    prev=[], succ=[0x106, 0x10a]
    =================================
    0xff: vff = CALLVALUE 
    0x101: v101 = ISZERO vff
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xfe], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xfe], succ=[0x210]
    =================================
    0x10c: v10c(0x5fa) = CONST 
    0x10f: v10f(0x210) = CONST 
    0x112: JUMP v10f(0x210)

    Begin block 0x210
    prev=[0x10a], succ=[0x5fa]
    =================================
    0x211: v211(0x1) = CONST 
    0x213: v213 = SLOAD v211(0x1)
    0x214: v214(0x1) = CONST 
    0x216: v216(0x1) = CONST 
    0x218: v218(0xa0) = CONST 
    0x21a: v21a(0x10000000000000000000000000000000000000000) = SHL v218(0xa0), v216(0x1)
    0x21b: v21b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21a(0x10000000000000000000000000000000000000000), v214(0x1)
    0x21c: v21c = AND v21b(0xffffffffffffffffffffffffffffffffffffffff), v213
    0x21e: JUMP v10c(0x5fa)

    Begin block 0x5fa
    prev=[0x210], succ=[]
    =================================
    0x5fb: v5fb(0x40) = CONST 
    0x5fe: v5fe = MLOAD v5fb(0x40)
    0x5ff: v5ff(0x1) = CONST 
    0x601: v601(0x1) = CONST 
    0x603: v603(0xa0) = CONST 
    0x605: v605(0x10000000000000000000000000000000000000000) = SHL v603(0xa0), v601(0x1)
    0x606: v606(0xffffffffffffffffffffffffffffffffffffffff) = SUB v605(0x10000000000000000000000000000000000000000), v5ff(0x1)
    0x609: v609 = AND v21c, v606(0xffffffffffffffffffffffffffffffffffffffff)
    0x60b: MSTORE v5fe, v609
    0x60c: v60c = MLOAD v5fb(0x40)
    0x610: v610(0x0) = SUB v5fe, v60c
    0x611: v611(0x20) = CONST 
    0x613: v613(0x20) = ADD v611(0x20), v610(0x0)
    0x615: RETURN v60c, v613(0x20)

}

