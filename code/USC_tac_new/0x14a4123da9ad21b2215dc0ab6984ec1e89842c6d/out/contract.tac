function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x5c3]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x5b7: v5b7(0x5c3) = CONST 
    0x5b8: JUMPI v5b7(0x5c3), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x5c6]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x25313a2) = CONST 
    0x3b: v3b = EQ v34, v35(0x25313a2)
    0x5b9: v5b9(0x5c6) = CONST 
    0x5ba: JUMPI v5b9(0x5c6), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x5c9, 0x4b]
    =================================
    0x41: v41(0x3659cfe6) = CONST 
    0x46: v46 = EQ v41(0x3659cfe6), v34
    0x5bb: v5bb(0x5c9) = CONST 
    0x5bc: JUMPI v5bb(0x5c9), v46

    Begin block 0x5c9
    prev=[0x40], succ=[]
    =================================
    0x5ca: v5ca(0xe3) = CONST 
    0x5cb: CALLPRIVATE v5ca(0xe3)

    Begin block 0x4b
    prev=[0x40], succ=[0x5cc, 0x56]
    =================================
    0x4c: v4c(0x4f1ef286) = CONST 
    0x51: v51 = EQ v4c(0x4f1ef286), v34
    0x5bd: v5bd(0x5cc) = CONST 
    0x5be: JUMPI v5bd(0x5cc), v51

    Begin block 0x5cc
    prev=[0x4b], succ=[]
    =================================
    0x5cd: v5cd(0x106) = CONST 
    0x5ce: CALLPRIVATE v5cd(0x106)

    Begin block 0x56
    prev=[0x4b], succ=[0x5cf, 0x61]
    =================================
    0x57: v57(0x5c60da1b) = CONST 
    0x5c: v5c = EQ v57(0x5c60da1b), v34
    0x5bf: v5bf(0x5cf) = CONST 
    0x5c0: JUMPI v5bf(0x5cf), v5c

    Begin block 0x5cf
    prev=[0x56], succ=[]
    =================================
    0x5d0: v5d0(0x160) = CONST 
    0x5d1: CALLPRIVATE v5d0(0x160)

    Begin block 0x61
    prev=[0x56], succ=[0x5c3, 0x5d2]
    =================================
    0x62: v62(0xf1739cae) = CONST 
    0x67: v67 = EQ v62(0xf1739cae), v34
    0x5c1: v5c1(0x5d2) = CONST 
    0x5c2: JUMPI v5c1(0x5d2), v67

    Begin block 0x5c3
    prev=[0x0, 0x61], succ=[]
    =================================
    0x5c4: v5c4(0x6c) = CONST 
    0x5c5: CALLPRIVATE v5c4(0x6c)

    Begin block 0x5d2
    prev=[0x61], succ=[]
    =================================
    0x5d3: v5d3(0x175) = CONST 
    0x5d4: CALLPRIVATE v5d3(0x175)

    Begin block 0x5c6
    prev=[0xd], succ=[]
    =================================
    0x5c7: v5c7(0xb2) = CONST 
    0x5c8: CALLPRIVATE v5c7(0xb2)

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0x106
    prev=[], succ=[0x250B0x106]
    =================================
    0x107: v107(0x40) = CONST 
    0x10a: v10a = MLOAD v107(0x40)
    0x10b: v10b(0x20) = CONST 
    0x10d: v10d(0x4) = CONST 
    0x10f: v10f(0x24) = CONST 
    0x112: v112 = CALLDATALOAD v10f(0x24)
    0x115: v115 = ADD v112, v10d(0x4)
    0x116: v116 = CALLDATALOAD v115
    0x117: v117(0x1f) = CONST 
    0x11a: v11a = ADD v116, v117(0x1f)
    0x11d: v11d = DIV v11a, v10b(0x20)
    0x11f: v11f = MUL v10b(0x20), v11d
    0x121: v121 = ADD v10a, v11f
    0x123: v123 = ADD v10b(0x20), v121
    0x126: MSTORE v107(0x40), v123
    0x129: MSTORE v10a, v116
    0x12a: v12a(0x515) = CONST 
    0x12f: v12f = CALLDATALOAD v10d(0x4)
    0x130: v130(0x1) = CONST 
    0x132: v132(0xa0) = CONST 
    0x134: v134(0x2) = CONST 
    0x136: v136(0x10000000000000000000000000000000000000000) = EXP v134(0x2), v132(0xa0)
    0x137: v137(0xffffffffffffffffffffffffffffffffffffffff) = SUB v136(0x10000000000000000000000000000000000000000), v130(0x1)
    0x138: v138 = AND v137(0xffffffffffffffffffffffffffffffffffffffff), v12f
    0x13a: v13a = CALLDATASIZE 
    0x13c: v13c(0x44) = CONST 
    0x143: v143 = ADD v10f(0x24), v112
    0x149: v149 = ADD v10a, v10b(0x20)
    0x14f: CALLDATACOPY v149, v143, v116
    0x154: v154(0x250) = CONST 
    0x15f: JUMP v154(0x250), v10a, v138, v12a(0x515)

    Begin block 0x250B0x106
    prev=[0x106], succ=[0x1f2B0x250B0x106]
    =================================
    0x251S0x106: v251V106(0x258) = CONST 
    0x254S0x106: v254V106(0x1f2) = CONST 
    0x257S0x106: JUMP v254V106(0x1f2)

    Begin block 0x1f2B0x250B0x106
    prev=[0x250B0x106], succ=[0x258B0x106]
    =================================
    0x1f3S0x250S0x106: v1f3V250V106(0x40) = CONST 
    0x1f6S0x250S0x106: v1f6V250V106 = MLOAD v1f3V250V106(0x40)
    0x1f7S0x250S0x106: v1f7V250V106(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x219S0x250S0x106: MSTORE v1f6V250V106, v1f7V250V106(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x21bS0x250S0x106: v21bV250V106 = MLOAD v1f3V250V106(0x40)
    0x21fS0x250S0x106: v21fV250V106(0x0) = SUB v1f6V250V106, v21bV250V106
    0x220S0x250S0x106: v220V250V106(0x1a) = CONST 
    0x222S0x250S0x106: v222V250V106(0x1a) = ADD v220V250V106(0x1a), v21fV250V106(0x0)
    0x224S0x250S0x106: v224V250V106 = SHA3 v21bV250V106, v222V250V106(0x1a)
    0x225S0x250S0x106: v225V250V106 = SLOAD v224V250V106
    0x227S0x250S0x106: JUMP v251V106(0x258)

    Begin block 0x258B0x106
    prev=[0x1f2B0x250B0x106], succ=[0x268B0x106, 0x26cB0x106]
    =================================
    0x259S0x106: v259V106(0x1) = CONST 
    0x25bS0x106: v25bV106(0xa0) = CONST 
    0x25dS0x106: v25dV106(0x2) = CONST 
    0x25fS0x106: v25fV106(0x10000000000000000000000000000000000000000) = EXP v25dV106(0x2), v25bV106(0xa0)
    0x260S0x106: v260V106(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25fV106(0x10000000000000000000000000000000000000000), v259V106(0x1)
    0x261S0x106: v261V106 = AND v260V106(0xffffffffffffffffffffffffffffffffffffffff), v225V250V106
    0x262S0x106: v262V106 = CALLER 
    0x263S0x106: v263V106 = EQ v262V106, v261V106
    0x264S0x106: v264V106(0x26c) = CONST 
    0x267S0x106: JUMPI v264V106(0x26c), v263V106

    Begin block 0x268B0x106
    prev=[0x258B0x106], succ=[]
    =================================
    0x268S0x106: v268V106(0x0) = CONST 
    0x26bS0x106: REVERT v268V106(0x0), v268V106(0x0)

    Begin block 0x26cB0x106
    prev=[0x258B0x106], succ=[0x275B0x106]
    =================================
    0x26dS0x106: v26dV106(0x275) = CONST 
    0x271S0x106: v271V106(0x228) = CONST 
    0x274S0x106: CALLPRIVATE v271V106(0x228), v138, v26dV106(0x275)

    Begin block 0x275B0x106
    prev=[0x26cB0x106], succ=[0x293B0x106]
    =================================
    0x276S0x106: v276V106 = ADDRESS 
    0x277S0x106: v277V106(0x1) = CONST 
    0x279S0x106: v279V106(0xa0) = CONST 
    0x27bS0x106: v27bV106(0x2) = CONST 
    0x27dS0x106: v27dV106(0x10000000000000000000000000000000000000000) = EXP v27bV106(0x2), v279V106(0xa0)
    0x27eS0x106: v27eV106(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27dV106(0x10000000000000000000000000000000000000000), v277V106(0x1)
    0x27fS0x106: v27fV106 = AND v27eV106(0xffffffffffffffffffffffffffffffffffffffff), v276V106
    0x280S0x106: v280V106 = CALLVALUE 
    0x282S0x106: v282V106(0x40) = CONST 
    0x284S0x106: v284V106 = MLOAD v282V106(0x40)
    0x288S0x106: v288V106 = MLOAD v10a
    0x28aS0x106: v28aV106(0x20) = CONST 
    0x28cS0x106: v28cV106 = ADD v28aV106(0x20), v10a
    0x291S0x106: v291V106(0x0) = CONST 

    Begin block 0x293B0x106
    prev=[0x275B0x106, 0x29cB0x106], succ=[0x2abB0x106, 0x29cB0x106]
    =================================
    0x293_0x0S0x106: v293_0V106 = PHI v291V106(0x0), v2a6V106
    0x296S0x106: v296V106 = LT v293_0V106, v288V106
    0x297S0x106: v297V106 = ISZERO v296V106
    0x298S0x106: v298V106(0x2ab) = CONST 
    0x29bS0x106: JUMPI v298V106(0x2ab), v297V106

    Begin block 0x2abB0x106
    prev=[0x293B0x106], succ=[0x2d8B0x106, 0x2bfB0x106]
    =================================
    0x2b4S0x106: v2b4V106 = ADD v288V106, v284V106
    0x2b6S0x106: v2b6V106(0x1f) = CONST 
    0x2b8S0x106: v2b8V106 = AND v2b6V106(0x1f), v288V106
    0x2baS0x106: v2baV106 = ISZERO v2b8V106
    0x2bbS0x106: v2bbV106(0x2d8) = CONST 
    0x2beS0x106: JUMPI v2bbV106(0x2d8), v2baV106

    Begin block 0x2d8B0x106
    prev=[0x2abB0x106, 0x2bfB0x106], succ=[0x2f4B0x106, 0x2f8B0x106]
    =================================
    0x2d8_0x1S0x106: v2d8_1V106 = PHI v2b4V106, v2d5V106
    0x2ddS0x106: v2ddV106(0x0) = CONST 
    0x2dfS0x106: v2dfV106(0x40) = CONST 
    0x2e1S0x106: v2e1V106 = MLOAD v2dfV106(0x40)
    0x2e4S0x106: v2e4V106 = SUB v2d8_1V106, v2e1V106
    0x2e8S0x106: v2e8V106 = GAS 
    0x2e9S0x106: v2e9V106 = CALL v2e8V106, v27fV106, v280V106, v2e1V106, v2e4V106, v2e1V106, v2ddV106(0x0)
    0x2eeS0x106: v2eeV106 = ISZERO v2e9V106
    0x2efS0x106: v2efV106 = ISZERO v2eeV106
    0x2f0S0x106: v2f0V106(0x2f8) = CONST 
    0x2f3S0x106: JUMPI v2f0V106(0x2f8), v2efV106

    Begin block 0x2f4B0x106
    prev=[0x2d8B0x106], succ=[]
    =================================
    0x2f4S0x106: v2f4V106(0x0) = CONST 
    0x2f7S0x106: REVERT v2f4V106(0x0), v2f4V106(0x0)

    Begin block 0x2f8B0x106
    prev=[0x2d8B0x106], succ=[0x515]
    =================================
    0x2fbS0x106: JUMP v12a(0x515)

    Begin block 0x515
    prev=[0x2f8B0x106], succ=[]
    =================================
    0x516: STOP 

    Begin block 0x2bfB0x106
    prev=[0x2abB0x106], succ=[0x2d8B0x106]
    =================================
    0x2c1S0x106: v2c1V106 = SUB v2b4V106, v2b8V106
    0x2c3S0x106: v2c3V106 = MLOAD v2c1V106
    0x2c4S0x106: v2c4V106(0x1) = CONST 
    0x2c7S0x106: v2c7V106(0x20) = CONST 
    0x2c9S0x106: v2c9V106 = SUB v2c7V106(0x20), v2b8V106
    0x2caS0x106: v2caV106(0x100) = CONST 
    0x2cdS0x106: v2cdV106 = EXP v2caV106(0x100), v2c9V106
    0x2ceS0x106: v2ceV106 = SUB v2cdV106, v2c4V106(0x1)
    0x2cfS0x106: v2cfV106 = NOT v2ceV106
    0x2d0S0x106: v2d0V106 = AND v2cfV106, v2c3V106
    0x2d2S0x106: MSTORE v2c1V106, v2d0V106
    0x2d3S0x106: v2d3V106(0x20) = CONST 
    0x2d5S0x106: v2d5V106 = ADD v2d3V106(0x20), v2c1V106

    Begin block 0x29cB0x106
    prev=[0x293B0x106], succ=[0x293B0x106]
    =================================
    0x29c_0x0S0x106: v29c_0V106 = PHI v291V106(0x0), v2a6V106
    0x29eS0x106: v29eV106 = ADD v29c_0V106, v28cV106
    0x29fS0x106: v29fV106 = MLOAD v29eV106
    0x2a2S0x106: v2a2V106 = ADD v29c_0V106, v284V106
    0x2a3S0x106: MSTORE v2a2V106, v29fV106
    0x2a4S0x106: v2a4V106(0x20) = CONST 
    0x2a6S0x106: v2a6V106 = ADD v2a4V106(0x20), v29c_0V106
    0x2a7S0x106: v2a7V106(0x293) = CONST 
    0x2aaS0x106: JUMP v2a7V106(0x293)

}

function implementation()() public {
    Begin block 0x160
    prev=[], succ=[0x168, 0x16c]
    =================================
    0x161: v161 = CALLVALUE 
    0x163: v163 = ISZERO v161
    0x164: v164(0x16c) = CONST 
    0x167: JUMPI v164(0x16c), v163

    Begin block 0x168
    prev=[0x160], succ=[]
    =================================
    0x168: v168(0x0) = CONST 
    0x16b: REVERT v168(0x0), v168(0x0)

    Begin block 0x16c
    prev=[0x160], succ=[0x196B0x16c]
    =================================
    0x16e: v16e(0x536) = CONST 
    0x171: v171(0x196) = CONST 
    0x174: JUMP v171(0x196)

    Begin block 0x196B0x16c
    prev=[0x16c], succ=[0x536]
    =================================
    0x197S0x16c: v197V16c(0x40) = CONST 
    0x19aS0x16c: v19aV16c = MLOAD v197V16c(0x40)
    0x19bS0x16c: v19bV16c(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174) = CONST 
    0x1bdS0x16c: MSTORE v19aV16c, v19bV16c(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174)
    0x1beS0x16c: v1beV16c(0x696f6e0000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1dfS0x16c: v1dfV16c(0x20) = CONST 
    0x1e2S0x16c: v1e2V16c = ADD v19aV16c, v1dfV16c(0x20)
    0x1e3S0x16c: MSTORE v1e2V16c, v1beV16c(0x696f6e0000000000000000000000000000000000000000000000000000000000)
    0x1e5S0x16c: v1e5V16c = MLOAD v197V16c(0x40)
    0x1e9S0x16c: v1e9V16c(0x0) = SUB v19aV16c, v1e5V16c
    0x1eaS0x16c: v1eaV16c(0x23) = CONST 
    0x1ecS0x16c: v1ecV16c(0x23) = ADD v1eaV16c(0x23), v1e9V16c(0x0)
    0x1eeS0x16c: v1eeV16c = SHA3 v1e5V16c, v1ecV16c(0x23)
    0x1efS0x16c: v1efV16c = SLOAD v1eeV16c
    0x1f1S0x16c: JUMP v16e(0x536)

    Begin block 0x536
    prev=[0x196B0x16c], succ=[]
    =================================
    0x537: v537(0x40) = CONST 
    0x53a: v53a = MLOAD v537(0x40)
    0x53b: v53b(0x1) = CONST 
    0x53d: v53d(0xa0) = CONST 
    0x53f: v53f(0x2) = CONST 
    0x541: v541(0x10000000000000000000000000000000000000000) = EXP v53f(0x2), v53d(0xa0)
    0x542: v542(0xffffffffffffffffffffffffffffffffffffffff) = SUB v541(0x10000000000000000000000000000000000000000), v53b(0x1)
    0x545: v545 = AND v1efV16c, v542(0xffffffffffffffffffffffffffffffffffffffff)
    0x547: MSTORE v53a, v545
    0x548: v548 = MLOAD v537(0x40)
    0x54c: v54c(0x0) = SUB v53a, v548
    0x54d: v54d(0x20) = CONST 
    0x54f: v54f(0x20) = ADD v54d(0x20), v54c(0x0)
    0x551: RETURN v548, v54f(0x20)

}

function transferProxyOwnership(address)() public {
    Begin block 0x175
    prev=[], succ=[0x17d, 0x181]
    =================================
    0x176: v176 = CALLVALUE 
    0x178: v178 = ISZERO v176
    0x179: v179(0x181) = CONST 
    0x17c: JUMPI v179(0x181), v178

    Begin block 0x17d
    prev=[0x175], succ=[]
    =================================
    0x17d: v17d(0x0) = CONST 
    0x180: REVERT v17d(0x0), v17d(0x0)

    Begin block 0x181
    prev=[0x175], succ=[0x2fcB0x181]
    =================================
    0x183: v183(0x571) = CONST 
    0x186: v186(0x1) = CONST 
    0x188: v188(0xa0) = CONST 
    0x18a: v18a(0x2) = CONST 
    0x18c: v18c(0x10000000000000000000000000000000000000000) = EXP v18a(0x2), v188(0xa0)
    0x18d: v18d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18c(0x10000000000000000000000000000000000000000), v186(0x1)
    0x18e: v18e(0x4) = CONST 
    0x190: v190 = CALLDATALOAD v18e(0x4)
    0x191: v191 = AND v190, v18d(0xffffffffffffffffffffffffffffffffffffffff)
    0x192: v192(0x2fc) = CONST 
    0x195: JUMP v192(0x2fc), v191, v183(0x571)

    Begin block 0x2fcB0x181
    prev=[0x181], succ=[0x1f2B0x2fcB0x181]
    =================================
    0x2fdS0x181: v2fdV181(0x304) = CONST 
    0x300S0x181: v300V181(0x1f2) = CONST 
    0x303S0x181: JUMP v300V181(0x1f2)

    Begin block 0x1f2B0x2fcB0x181
    prev=[0x2fcB0x181], succ=[0x304B0x181]
    =================================
    0x1f3S0x2fcS0x181: v1f3V2fcV181(0x40) = CONST 
    0x1f6S0x2fcS0x181: v1f6V2fcV181 = MLOAD v1f3V2fcV181(0x40)
    0x1f7S0x2fcS0x181: v1f7V2fcV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x219S0x2fcS0x181: MSTORE v1f6V2fcV181, v1f7V2fcV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x21bS0x2fcS0x181: v21bV2fcV181 = MLOAD v1f3V2fcV181(0x40)
    0x21fS0x2fcS0x181: v21fV2fcV181(0x0) = SUB v1f6V2fcV181, v21bV2fcV181
    0x220S0x2fcS0x181: v220V2fcV181(0x1a) = CONST 
    0x222S0x2fcS0x181: v222V2fcV181(0x1a) = ADD v220V2fcV181(0x1a), v21fV2fcV181(0x0)
    0x224S0x2fcS0x181: v224V2fcV181 = SHA3 v21bV2fcV181, v222V2fcV181(0x1a)
    0x225S0x2fcS0x181: v225V2fcV181 = SLOAD v224V2fcV181
    0x227S0x2fcS0x181: JUMP v2fdV181(0x304)

    Begin block 0x304B0x181
    prev=[0x1f2B0x2fcB0x181], succ=[0x314B0x181, 0x318B0x181]
    =================================
    0x305S0x181: v305V181(0x1) = CONST 
    0x307S0x181: v307V181(0xa0) = CONST 
    0x309S0x181: v309V181(0x2) = CONST 
    0x30bS0x181: v30bV181(0x10000000000000000000000000000000000000000) = EXP v309V181(0x2), v307V181(0xa0)
    0x30cS0x181: v30cV181(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30bV181(0x10000000000000000000000000000000000000000), v305V181(0x1)
    0x30dS0x181: v30dV181 = AND v30cV181(0xffffffffffffffffffffffffffffffffffffffff), v225V2fcV181
    0x30eS0x181: v30eV181 = CALLER 
    0x30fS0x181: v30fV181 = EQ v30eV181, v30dV181
    0x310S0x181: v310V181(0x318) = CONST 
    0x313S0x181: JUMPI v310V181(0x318), v30fV181

    Begin block 0x314B0x181
    prev=[0x304B0x181], succ=[]
    =================================
    0x314S0x181: v314V181(0x0) = CONST 
    0x317S0x181: REVERT v314V181(0x0), v314V181(0x0)

    Begin block 0x318B0x181
    prev=[0x304B0x181], succ=[0x329B0x181, 0x32dB0x181]
    =================================
    0x319S0x181: v319V181(0x1) = CONST 
    0x31bS0x181: v31bV181(0xa0) = CONST 
    0x31dS0x181: v31dV181(0x2) = CONST 
    0x31fS0x181: v31fV181(0x10000000000000000000000000000000000000000) = EXP v31dV181(0x2), v31bV181(0xa0)
    0x320S0x181: v320V181(0xffffffffffffffffffffffffffffffffffffffff) = SUB v31fV181(0x10000000000000000000000000000000000000000), v319V181(0x1)
    0x322S0x181: v322V181 = AND v191, v320V181(0xffffffffffffffffffffffffffffffffffffffff)
    0x323S0x181: v323V181 = ISZERO v322V181
    0x324S0x181: v324V181 = ISZERO v323V181
    0x325S0x181: v325V181(0x32d) = CONST 
    0x328S0x181: JUMPI v325V181(0x32d), v324V181

    Begin block 0x329B0x181
    prev=[0x318B0x181], succ=[]
    =================================
    0x329S0x181: v329V181(0x0) = CONST 
    0x32cS0x181: REVERT v329V181(0x0), v329V181(0x0)

    Begin block 0x32dB0x181
    prev=[0x318B0x181], succ=[0x1f2B0x32dB0x181]
    =================================
    0x32eS0x181: v32eV181(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9) = CONST 
    0x34fS0x181: v34fV181(0x356) = CONST 
    0x352S0x181: v352V181(0x1f2) = CONST 
    0x355S0x181: JUMP v352V181(0x1f2)

    Begin block 0x1f2B0x32dB0x181
    prev=[0x32dB0x181], succ=[0x356B0x181]
    =================================
    0x1f3S0x32dS0x181: v1f3V32dV181(0x40) = CONST 
    0x1f6S0x32dS0x181: v1f6V32dV181 = MLOAD v1f3V32dV181(0x40)
    0x1f7S0x32dS0x181: v1f7V32dV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x219S0x32dS0x181: MSTORE v1f6V32dV181, v1f7V32dV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x21bS0x32dS0x181: v21bV32dV181 = MLOAD v1f3V32dV181(0x40)
    0x21fS0x32dS0x181: v21fV32dV181(0x0) = SUB v1f6V32dV181, v21bV32dV181
    0x220S0x32dS0x181: v220V32dV181(0x1a) = CONST 
    0x222S0x32dS0x181: v222V32dV181(0x1a) = ADD v220V32dV181(0x1a), v21fV32dV181(0x0)
    0x224S0x32dS0x181: v224V32dV181 = SHA3 v21bV32dV181, v222V32dV181(0x1a)
    0x225S0x32dS0x181: v225V32dV181 = SLOAD v224V32dV181
    0x227S0x32dS0x181: JUMP v34fV181(0x356)

    Begin block 0x356B0x181
    prev=[0x1f2B0x32dB0x181], succ=[0x3e7B0x181]
    =================================
    0x357S0x181: v357V181(0x40) = CONST 
    0x35aS0x181: v35aV181 = MLOAD v357V181(0x40)
    0x35bS0x181: v35bV181(0x1) = CONST 
    0x35dS0x181: v35dV181(0xa0) = CONST 
    0x35fS0x181: v35fV181(0x2) = CONST 
    0x361S0x181: v361V181(0x10000000000000000000000000000000000000000) = EXP v35fV181(0x2), v35dV181(0xa0)
    0x362S0x181: v362V181(0xffffffffffffffffffffffffffffffffffffffff) = SUB v361V181(0x10000000000000000000000000000000000000000), v35bV181(0x1)
    0x365S0x181: v365V181 = AND v362V181(0xffffffffffffffffffffffffffffffffffffffff), v225V32dV181
    0x367S0x181: MSTORE v35aV181, v365V181
    0x36aS0x181: v36aV181 = AND v191, v362V181(0xffffffffffffffffffffffffffffffffffffffff)
    0x36bS0x181: v36bV181(0x20) = CONST 
    0x36eS0x181: v36eV181 = ADD v35aV181, v36bV181(0x20)
    0x36fS0x181: MSTORE v36eV181, v36aV181
    0x371S0x181: v371V181 = MLOAD v357V181(0x40)
    0x375S0x181: v375V181(0x0) = SUB v35aV181, v371V181
    0x376S0x181: v376V181(0x40) = ADD v375V181(0x0), v357V181(0x40)
    0x378S0x181: LOG1 v371V181, v376V181(0x40), v32eV181(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9)
    0x379S0x181: v379V181(0x5b4) = CONST 
    0x37dS0x181: v37dV181(0x3e7) = CONST 
    0x380S0x181: JUMP v37dV181(0x3e7)

    Begin block 0x3e7B0x181
    prev=[0x356B0x181], succ=[0x5b4B0x181]
    =================================
    0x3e8S0x181: v3e8V181(0x40) = CONST 
    0x3ebS0x181: v3ebV181 = MLOAD v3e8V181(0x40)
    0x3ecS0x181: v3ecV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x40eS0x181: MSTORE v3ebV181, v3ecV181(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x410S0x181: v410V181 = MLOAD v3e8V181(0x40)
    0x414S0x181: v414V181(0x0) = SUB v3ebV181, v410V181
    0x415S0x181: v415V181(0x1a) = CONST 
    0x417S0x181: v417V181(0x1a) = ADD v415V181(0x1a), v414V181(0x0)
    0x419S0x181: v419V181 = SHA3 v410V181, v417V181(0x1a)
    0x41aS0x181: SSTORE v419V181, v191
    0x41bS0x181: JUMP v379V181(0x5b4)

    Begin block 0x5b4B0x181
    prev=[0x3e7B0x181], succ=[0x571]
    =================================
    0x5b6S0x181: JUMP v183(0x571)

    Begin block 0x571
    prev=[0x5b4B0x181], succ=[]
    =================================
    0x572: STOP 

}

function 0x228(0x228arg0x0, 0x228arg0x1) private {
    Begin block 0x228
    prev=[], succ=[0x1f2B0x228]
    =================================
    0x229: v229(0x230) = CONST 
    0x22c: v22c(0x1f2) = CONST 
    0x22f: JUMP v22c(0x1f2)

    Begin block 0x1f2B0x228
    prev=[0x228], succ=[0x230]
    =================================
    0x1f3S0x228: v1f3V228(0x40) = CONST 
    0x1f6S0x228: v1f6V228 = MLOAD v1f3V228(0x40)
    0x1f7S0x228: v1f7V228(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x219S0x228: MSTORE v1f6V228, v1f7V228(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x21bS0x228: v21bV228 = MLOAD v1f3V228(0x40)
    0x21fS0x228: v21fV228(0x0) = SUB v1f6V228, v21bV228
    0x220S0x228: v220V228(0x1a) = CONST 
    0x222S0x228: v222V228(0x1a) = ADD v220V228(0x1a), v21fV228(0x0)
    0x224S0x228: v224V228 = SHA3 v21bV228, v222V228(0x1a)
    0x225S0x228: v225V228 = SLOAD v224V228
    0x227S0x228: JUMP v229(0x230)

    Begin block 0x230
    prev=[0x1f2B0x228], succ=[0x240, 0x244]
    =================================
    0x231: v231(0x1) = CONST 
    0x233: v233(0xa0) = CONST 
    0x235: v235(0x2) = CONST 
    0x237: v237(0x10000000000000000000000000000000000000000) = EXP v235(0x2), v233(0xa0)
    0x238: v238(0xffffffffffffffffffffffffffffffffffffffff) = SUB v237(0x10000000000000000000000000000000000000000), v231(0x1)
    0x239: v239 = AND v238(0xffffffffffffffffffffffffffffffffffffffff), v225V228
    0x23a: v23a = CALLER 
    0x23b: v23b = EQ v23a, v239
    0x23c: v23c(0x244) = CONST 
    0x23f: JUMPI v23c(0x244), v23b

    Begin block 0x240
    prev=[0x230], succ=[]
    =================================
    0x240: v240(0x0) = CONST 
    0x243: REVERT v240(0x0), v240(0x0)

    Begin block 0x244
    prev=[0x230], succ=[0x381]
    =================================
    0x245: v245(0x592) = CONST 
    0x249: v249(0x381) = CONST 
    0x24c: JUMP v249(0x381)

    Begin block 0x381
    prev=[0x244], succ=[0x196B0x381]
    =================================
    0x382: v382(0x0) = CONST 
    0x384: v384(0x38b) = CONST 
    0x387: v387(0x196) = CONST 
    0x38a: JUMP v387(0x196)

    Begin block 0x196B0x381
    prev=[0x381], succ=[0x38b]
    =================================
    0x197S0x381: v197V381(0x40) = CONST 
    0x19aS0x381: v19aV381 = MLOAD v197V381(0x40)
    0x19bS0x381: v19bV381(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174) = CONST 
    0x1bdS0x381: MSTORE v19aV381, v19bV381(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174)
    0x1beS0x381: v1beV381(0x696f6e0000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1dfS0x381: v1dfV381(0x20) = CONST 
    0x1e2S0x381: v1e2V381 = ADD v19aV381, v1dfV381(0x20)
    0x1e3S0x381: MSTORE v1e2V381, v1beV381(0x696f6e0000000000000000000000000000000000000000000000000000000000)
    0x1e5S0x381: v1e5V381 = MLOAD v197V381(0x40)
    0x1e9S0x381: v1e9V381(0x0) = SUB v19aV381, v1e5V381
    0x1eaS0x381: v1eaV381(0x23) = CONST 
    0x1ecS0x381: v1ecV381(0x23) = ADD v1eaV381(0x23), v1e9V381(0x0)
    0x1eeS0x381: v1eeV381 = SHA3 v1e5V381, v1ecV381(0x23)
    0x1efS0x381: v1efV381 = SLOAD v1eeV381
    0x1f1S0x381: JUMP v384(0x38b)

    Begin block 0x38b
    prev=[0x196B0x381], succ=[0x3a2, 0x3a6]
    =================================
    0x38e: v38e(0x1) = CONST 
    0x390: v390(0xa0) = CONST 
    0x392: v392(0x2) = CONST 
    0x394: v394(0x10000000000000000000000000000000000000000) = EXP v392(0x2), v390(0xa0)
    0x395: v395(0xffffffffffffffffffffffffffffffffffffffff) = SUB v394(0x10000000000000000000000000000000000000000), v38e(0x1)
    0x398: v398 = AND v1efV381, v395(0xffffffffffffffffffffffffffffffffffffffff)
    0x39b: v39b = AND v228arg0, v395(0xffffffffffffffffffffffffffffffffffffffff)
    0x39c: v39c = EQ v39b, v398
    0x39d: v39d = ISZERO v39c
    0x39e: v39e(0x3a6) = CONST 
    0x3a1: JUMPI v39e(0x3a6), v39d

    Begin block 0x3a2
    prev=[0x38b], succ=[]
    =================================
    0x3a2: v3a2(0x0) = CONST 
    0x3a5: REVERT v3a2(0x0), v3a2(0x0)

    Begin block 0x3a6
    prev=[0x38b], succ=[0x41c]
    =================================
    0x3a7: v3a7(0x3af) = CONST 
    0x3ab: v3ab(0x41c) = CONST 
    0x3ae: JUMP v3ab(0x41c)

    Begin block 0x41c
    prev=[0x3a6], succ=[0x3af]
    =================================
    0x41d: v41d(0x40) = CONST 
    0x420: v420 = MLOAD v41d(0x40)
    0x421: v421(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174) = CONST 
    0x443: MSTORE v420, v421(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174)
    0x444: v444(0x696f6e0000000000000000000000000000000000000000000000000000000000) = CONST 
    0x465: v465(0x20) = CONST 
    0x468: v468 = ADD v420, v465(0x20)
    0x469: MSTORE v468, v444(0x696f6e0000000000000000000000000000000000000000000000000000000000)
    0x46b: v46b = MLOAD v41d(0x40)
    0x46f: v46f(0x0) = SUB v420, v46b
    0x470: v470(0x23) = CONST 
    0x472: v472(0x23) = ADD v470(0x23), v46f(0x0)
    0x474: v474 = SHA3 v46b, v472(0x23)
    0x475: SSTORE v474, v228arg0
    0x476: JUMP v3a7(0x3af)

    Begin block 0x3af
    prev=[0x41c], succ=[0x592]
    =================================
    0x3b0: v3b0(0x40) = CONST 
    0x3b2: v3b2 = MLOAD v3b0(0x40)
    0x3b3: v3b3(0x1) = CONST 
    0x3b5: v3b5(0xa0) = CONST 
    0x3b7: v3b7(0x2) = CONST 
    0x3b9: v3b9(0x10000000000000000000000000000000000000000) = EXP v3b7(0x2), v3b5(0xa0)
    0x3ba: v3ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b9(0x10000000000000000000000000000000000000000), v3b3(0x1)
    0x3bc: v3bc = AND v228arg0, v3ba(0xffffffffffffffffffffffffffffffffffffffff)
    0x3be: v3be(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x3e0: v3e0(0x0) = CONST 
    0x3e3: LOG2 v3b2, v3e0(0x0), v3be(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v3bc
    0x3e6: JUMP v245(0x592)

    Begin block 0x592
    prev=[0x3af], succ=[]
    =================================
    0x594: RETURNPRIVATE v228arg1

}

function fallback()() public {
    Begin block 0x6c
    prev=[], succ=[0x196B0x6c]
    =================================
    0x6d: v6d(0x0) = CONST 
    0x6f: v6f(0x76) = CONST 
    0x72: v72(0x196) = CONST 
    0x75: JUMP v72(0x196)

    Begin block 0x196B0x6c
    prev=[0x6c], succ=[0x76]
    =================================
    0x197S0x6c: v197V6c(0x40) = CONST 
    0x19aS0x6c: v19aV6c = MLOAD v197V6c(0x40)
    0x19bS0x6c: v19bV6c(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174) = CONST 
    0x1bdS0x6c: MSTORE v19aV6c, v19bV6c(0x6f72672e7a657070656c696e6f732e70726f78792e696d706c656d656e746174)
    0x1beS0x6c: v1beV6c(0x696f6e0000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1dfS0x6c: v1dfV6c(0x20) = CONST 
    0x1e2S0x6c: v1e2V6c = ADD v19aV6c, v1dfV6c(0x20)
    0x1e3S0x6c: MSTORE v1e2V6c, v1beV6c(0x696f6e0000000000000000000000000000000000000000000000000000000000)
    0x1e5S0x6c: v1e5V6c = MLOAD v197V6c(0x40)
    0x1e9S0x6c: v1e9V6c(0x0) = SUB v19aV6c, v1e5V6c
    0x1eaS0x6c: v1eaV6c(0x23) = CONST 
    0x1ecS0x6c: v1ecV6c(0x23) = ADD v1eaV6c(0x23), v1e9V6c(0x0)
    0x1eeS0x6c: v1eeV6c = SHA3 v1e5V6c, v1ecV6c(0x23)
    0x1efS0x6c: v1efV6c = SLOAD v1eeV6c
    0x1f1S0x6c: JUMP v6f(0x76)

    Begin block 0x76
    prev=[0x196B0x6c], succ=[0x89, 0x8d]
    =================================
    0x79: v79(0x1) = CONST 
    0x7b: v7b(0xa0) = CONST 
    0x7d: v7d(0x2) = CONST 
    0x7f: v7f(0x10000000000000000000000000000000000000000) = EXP v7d(0x2), v7b(0xa0)
    0x80: v80(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7f(0x10000000000000000000000000000000000000000), v79(0x1)
    0x82: v82 = AND v1efV6c, v80(0xffffffffffffffffffffffffffffffffffffffff)
    0x83: v83 = ISZERO v82
    0x84: v84 = ISZERO v83
    0x85: v85(0x8d) = CONST 
    0x88: JUMPI v85(0x8d), v84

    Begin block 0x89
    prev=[0x76], succ=[]
    =================================
    0x89: v89(0x0) = CONST 
    0x8c: REVERT v89(0x0), v89(0x0)

    Begin block 0x8d
    prev=[0x76], succ=[0xae, 0xab]
    =================================
    0x8e: v8e(0x40) = CONST 
    0x90: v90 = MLOAD v8e(0x40)
    0x91: v91 = CALLDATASIZE 
    0x92: v92(0x0) = CONST 
    0x95: CALLDATACOPY v90, v92(0x0), v91
    0x96: v96(0x0) = CONST 
    0x99: v99 = CALLDATASIZE 
    0x9c: v9c = GAS 
    0x9d: v9d = DELEGATECALL v9c, v1efV6c, v90, v99, v96(0x0), v96(0x0)
    0x9e: v9e = RETURNDATASIZE 
    0xa0: va0(0x0) = CONST 
    0xa3: RETURNDATACOPY v90, va0(0x0), v9e
    0xa6: va6 = ISZERO v9d
    0xa7: va7(0xae) = CONST 
    0xaa: JUMPI va7(0xae), va6

    Begin block 0xae
    prev=[0x8d], succ=[]
    =================================
    0xb1: REVERT v90, v9e

    Begin block 0xab
    prev=[0x8d], succ=[]
    =================================
    0xad: RETURN v90, v9e

}

function proxyOwner()() public {
    Begin block 0xb2
    prev=[], succ=[0xba, 0xbe]
    =================================
    0xb3: vb3 = CALLVALUE 
    0xb5: vb5 = ISZERO vb3
    0xb6: vb6(0xbe) = CONST 
    0xb9: JUMPI vb6(0xbe), vb5

    Begin block 0xba
    prev=[0xb2], succ=[]
    =================================
    0xba: vba(0x0) = CONST 
    0xbd: REVERT vba(0x0), vba(0x0)

    Begin block 0xbe
    prev=[0xb2], succ=[0x1f2B0xbe]
    =================================
    0xc0: vc0(0x4b9) = CONST 
    0xc3: vc3(0x1f2) = CONST 
    0xc6: JUMP vc3(0x1f2)

    Begin block 0x1f2B0xbe
    prev=[0xbe], succ=[0x4b9]
    =================================
    0x1f3S0xbe: v1f3Vbe(0x40) = CONST 
    0x1f6S0xbe: v1f6Vbe = MLOAD v1f3Vbe(0x40)
    0x1f7S0xbe: v1f7Vbe(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000) = CONST 
    0x219S0xbe: MSTORE v1f6Vbe, v1f7Vbe(0x6f72672e7a657070656c696e6f732e70726f78792e6f776e6572000000000000)
    0x21bS0xbe: v21bVbe = MLOAD v1f3Vbe(0x40)
    0x21fS0xbe: v21fVbe(0x0) = SUB v1f6Vbe, v21bVbe
    0x220S0xbe: v220Vbe(0x1a) = CONST 
    0x222S0xbe: v222Vbe(0x1a) = ADD v220Vbe(0x1a), v21fVbe(0x0)
    0x224S0xbe: v224Vbe = SHA3 v21bVbe, v222Vbe(0x1a)
    0x225S0xbe: v225Vbe = SLOAD v224Vbe
    0x227S0xbe: JUMP vc0(0x4b9)

    Begin block 0x4b9
    prev=[0x1f2B0xbe], succ=[]
    =================================
    0x4ba: v4ba(0x40) = CONST 
    0x4bd: v4bd = MLOAD v4ba(0x40)
    0x4be: v4be(0x1) = CONST 
    0x4c0: v4c0(0xa0) = CONST 
    0x4c2: v4c2(0x2) = CONST 
    0x4c4: v4c4(0x10000000000000000000000000000000000000000) = EXP v4c2(0x2), v4c0(0xa0)
    0x4c5: v4c5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4c4(0x10000000000000000000000000000000000000000), v4be(0x1)
    0x4c8: v4c8 = AND v225Vbe, v4c5(0xffffffffffffffffffffffffffffffffffffffff)
    0x4ca: MSTORE v4bd, v4c8
    0x4cb: v4cb = MLOAD v4ba(0x40)
    0x4cf: v4cf(0x0) = SUB v4bd, v4cb
    0x4d0: v4d0(0x20) = CONST 
    0x4d2: v4d2(0x20) = ADD v4d0(0x20), v4cf(0x0)
    0x4d4: RETURN v4cb, v4d2(0x20)

}

function upgradeTo(address)() public {
    Begin block 0xe3
    prev=[], succ=[0xeb, 0xef]
    =================================
    0xe4: ve4 = CALLVALUE 
    0xe6: ve6 = ISZERO ve4
    0xe7: ve7(0xef) = CONST 
    0xea: JUMPI ve7(0xef), ve6

    Begin block 0xeb
    prev=[0xe3], succ=[]
    =================================
    0xeb: veb(0x0) = CONST 
    0xee: REVERT veb(0x0), veb(0x0)

    Begin block 0xef
    prev=[0xe3], succ=[0x4f4]
    =================================
    0xf1: vf1(0x4f4) = CONST 
    0xf4: vf4(0x1) = CONST 
    0xf6: vf6(0xa0) = CONST 
    0xf8: vf8(0x2) = CONST 
    0xfa: vfa(0x10000000000000000000000000000000000000000) = EXP vf8(0x2), vf6(0xa0)
    0xfb: vfb(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfa(0x10000000000000000000000000000000000000000), vf4(0x1)
    0xfc: vfc(0x4) = CONST 
    0xfe: vfe = CALLDATALOAD vfc(0x4)
    0xff: vff = AND vfe, vfb(0xffffffffffffffffffffffffffffffffffffffff)
    0x100: v100(0x228) = CONST 
    0x103: CALLPRIVATE v100(0x228), vff, vf1(0x4f4)

    Begin block 0x4f4
    prev=[0xef], succ=[]
    =================================
    0x4f5: STOP 

}

