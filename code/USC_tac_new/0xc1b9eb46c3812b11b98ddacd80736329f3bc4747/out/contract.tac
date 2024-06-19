function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x7fe]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x7ec: v7ec(0x7fe) = CONST 
    0x7ed: JUMPI v7ec(0x7fe), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x801]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x25313a2) = CONST 
    0x3b: v3b = EQ v34, v35(0x25313a2)
    0x7ee: v7ee(0x801) = CONST 
    0x7ef: JUMPI v7ee(0x801), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x804, 0x4b]
    =================================
    0x41: v41(0xadd8140) = CONST 
    0x46: v46 = EQ v41(0xadd8140), v34
    0x7f0: v7f0(0x804) = CONST 
    0x7f1: JUMPI v7f0(0x804), v46

    Begin block 0x804
    prev=[0x40], succ=[]
    =================================
    0x805: v805(0xf9) = CONST 
    0x806: CALLPRIVATE v805(0xf9)

    Begin block 0x4b
    prev=[0x40], succ=[0x807, 0x56]
    =================================
    0x4c: v4c(0x3659cfe6) = CONST 
    0x51: v51 = EQ v4c(0x3659cfe6), v34
    0x7f2: v7f2(0x807) = CONST 
    0x7f3: JUMPI v7f2(0x807), v51

    Begin block 0x807
    prev=[0x4b], succ=[]
    =================================
    0x808: v808(0x10e) = CONST 
    0x809: CALLPRIVATE v808(0x10e)

    Begin block 0x56
    prev=[0x4b], succ=[0x80a, 0x61]
    =================================
    0x57: v57(0x5c60da1b) = CONST 
    0x5c: v5c = EQ v57(0x5c60da1b), v34
    0x7f4: v7f4(0x80a) = CONST 
    0x7f5: JUMPI v7f4(0x80a), v5c

    Begin block 0x80a
    prev=[0x56], succ=[]
    =================================
    0x80b: v80b(0x143) = CONST 
    0x80c: CALLPRIVATE v80b(0x143)

    Begin block 0x61
    prev=[0x56], succ=[0x80d, 0x6c]
    =================================
    0x62: v62(0x5e55d96f) = CONST 
    0x67: v67 = EQ v62(0x5e55d96f), v34
    0x7f6: v7f6(0x80d) = CONST 
    0x7f7: JUMPI v7f6(0x80d), v67

    Begin block 0x80d
    prev=[0x61], succ=[]
    =================================
    0x80e: v80e(0x158) = CONST 
    0x80f: CALLPRIVATE v80e(0x158)

    Begin block 0x6c
    prev=[0x61], succ=[0x810, 0x77]
    =================================
    0x6d: v6d(0x8f4a3bcd) = CONST 
    0x72: v72 = EQ v6d(0x8f4a3bcd), v34
    0x7f8: v7f8(0x810) = CONST 
    0x7f9: JUMPI v7f8(0x810), v72

    Begin block 0x810
    prev=[0x6c], succ=[]
    =================================
    0x811: v811(0x18b) = CONST 
    0x812: CALLPRIVATE v811(0x18b)

    Begin block 0x77
    prev=[0x6c], succ=[0x813, 0x82]
    =================================
    0x78: v78(0x9965b3d6) = CONST 
    0x7d: v7d = EQ v78(0x9965b3d6), v34
    0x7fa: v7fa(0x813) = CONST 
    0x7fb: JUMPI v7fa(0x813), v7d

    Begin block 0x813
    prev=[0x77], succ=[]
    =================================
    0x814: v814(0x1b4) = CONST 
    0x815: CALLPRIVATE v814(0x1b4)

    Begin block 0x82
    prev=[0x77], succ=[0x7fe, 0x816]
    =================================
    0x83: v83(0xf1739cae) = CONST 
    0x88: v88 = EQ v83(0xf1739cae), v34
    0x7fc: v7fc(0x816) = CONST 
    0x7fd: JUMPI v7fc(0x816), v88

    Begin block 0x7fe
    prev=[0x0, 0x82], succ=[]
    =================================
    0x7ff: v7ff(0x8d) = CONST 
    0x800: CALLPRIVATE v7ff(0x8d)

    Begin block 0x816
    prev=[0x82], succ=[]
    =================================
    0x817: v817(0x1c9) = CONST 
    0x818: CALLPRIVATE v817(0x1c9)

    Begin block 0x801
    prev=[0xd], succ=[]
    =================================
    0x802: v802(0xc8) = CONST 
    0x803: CALLPRIVATE v802(0xc8)

}

function upgradeTo(address)() public {
    Begin block 0x10e
    prev=[], succ=[0x116, 0x11a]
    =================================
    0x10f: v10f = CALLVALUE 
    0x111: v111 = ISZERO v10f
    0x112: v112(0x11a) = CONST 
    0x115: JUMPI v112(0x11a), v111

    Begin block 0x116
    prev=[0x10e], succ=[]
    =================================
    0x116: v116(0x0) = CONST 
    0x119: REVERT v116(0x0), v116(0x0)

    Begin block 0x11a
    prev=[0x10e], succ=[0x12d, 0x131]
    =================================
    0x11c: v11c(0x74c) = CONST 
    0x11f: v11f(0x4) = CONST 
    0x122: v122 = CALLDATASIZE 
    0x123: v123 = SUB v122, v11f(0x4)
    0x124: v124(0x20) = CONST 
    0x127: v127 = LT v123, v124(0x20)
    0x128: v128 = ISZERO v127
    0x129: v129(0x131) = CONST 
    0x12c: JUMPI v129(0x131), v128

    Begin block 0x12d
    prev=[0x11a], succ=[]
    =================================
    0x12d: v12d(0x0) = CONST 
    0x130: REVERT v12d(0x0), v12d(0x0)

    Begin block 0x131
    prev=[0x11a], succ=[0x21a]
    =================================
    0x133: v133 = CALLDATALOAD v11f(0x4)
    0x134: v134(0x1) = CONST 
    0x136: v136(0xa0) = CONST 
    0x138: v138(0x2) = CONST 
    0x13a: v13a(0x10000000000000000000000000000000000000000) = EXP v138(0x2), v136(0xa0)
    0x13b: v13b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13a(0x10000000000000000000000000000000000000000), v134(0x1)
    0x13c: v13c = AND v13b(0xffffffffffffffffffffffffffffffffffffffff), v133
    0x13d: v13d(0x21a) = CONST 
    0x140: JUMP v13d(0x21a)

    Begin block 0x21a
    prev=[0x131], succ=[0x45dB0x21a]
    =================================
    0x21b: v21b(0x222) = CONST 
    0x21e: v21e(0x45d) = CONST 
    0x221: JUMP v21e(0x45d)

    Begin block 0x45dB0x21a
    prev=[0x21a], succ=[0x222]
    =================================
    0x45eS0x21a: v45eV21a(0x0) = CONST 
    0x460S0x21a: v460V21a = SLOAD v45eV21a(0x0)
    0x461S0x21a: v461V21a(0x1) = CONST 
    0x463S0x21a: v463V21a(0xa0) = CONST 
    0x465S0x21a: v465V21a(0x2) = CONST 
    0x467S0x21a: v467V21a(0x10000000000000000000000000000000000000000) = EXP v465V21a(0x2), v463V21a(0xa0)
    0x468S0x21a: v468V21a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v467V21a(0x10000000000000000000000000000000000000000), v461V21a(0x1)
    0x469S0x21a: v469V21a = AND v468V21a(0xffffffffffffffffffffffffffffffffffffffff), v460V21a
    0x46aS0x21a: v46aV21a = CALLER 
    0x46bS0x21a: v46bV21a = EQ v46aV21a, v469V21a
    0x46dS0x21a: JUMP v21b(0x222)

    Begin block 0x222
    prev=[0x45dB0x21a], succ=[0x229, 0x278]
    =================================
    0x223: v223 = ISZERO v46bV21a
    0x224: v224 = ISZERO v223
    0x225: v225(0x278) = CONST 
    0x228: JUMPI v225(0x278), v224

    Begin block 0x229
    prev=[0x222], succ=[]
    =================================
    0x229: v229(0x40) = CONST 
    0x22c: v22c = MLOAD v229(0x40)
    0x22d: v22d(0xe5) = CONST 
    0x22f: v22f(0x2) = CONST 
    0x231: v231(0x2000000000000000000000000000000000000000000000000000000000) = EXP v22f(0x2), v22d(0xe5)
    0x232: v232(0x461bcd) = CONST 
    0x236: v236(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v232(0x461bcd), v231(0x2000000000000000000000000000000000000000000000000000000000)
    0x238: MSTORE v22c, v236(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x239: v239(0x20) = CONST 
    0x23b: v23b(0x4) = CONST 
    0x23e: v23e = ADD v22c, v23b(0x4)
    0x241: MSTORE v23e, v239(0x20)
    0x242: v242(0x24) = CONST 
    0x245: v245 = ADD v22c, v242(0x24)
    0x246: MSTORE v245, v239(0x20)
    0x247: v247(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x268: v268(0x44) = CONST 
    0x26b: v26b = ADD v22c, v268(0x44)
    0x26c: MSTORE v26b, v247(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x26e: v26e = MLOAD v229(0x40)
    0x272: v272(0x0) = SUB v22c, v26e
    0x273: v273(0x64) = CONST 
    0x275: v275(0x64) = ADD v273(0x64), v272(0x0)
    0x277: REVERT v26e, v275(0x64)

    Begin block 0x278
    prev=[0x222], succ=[0x28f, 0x304]
    =================================
    0x279: v279(0x2) = CONST 
    0x27b: v27b = SLOAD v279(0x2)
    0x27c: v27c(0x1) = CONST 
    0x27e: v27e(0xa0) = CONST 
    0x280: v280(0x2) = CONST 
    0x282: v282(0x10000000000000000000000000000000000000000) = EXP v280(0x2), v27e(0xa0)
    0x283: v283(0xffffffffffffffffffffffffffffffffffffffff) = SUB v282(0x10000000000000000000000000000000000000000), v27c(0x1)
    0x286: v286 = AND v283(0xffffffffffffffffffffffffffffffffffffffff), v13c
    0x288: v288 = AND v27b, v283(0xffffffffffffffffffffffffffffffffffffffff)
    0x289: v289 = EQ v288, v286
    0x28a: v28a = ISZERO v289
    0x28b: v28b(0x304) = CONST 
    0x28e: JUMPI v28b(0x304), v28a

    Begin block 0x28f
    prev=[0x278], succ=[]
    =================================
    0x28f: v28f(0x40) = CONST 
    0x292: v292 = MLOAD v28f(0x40)
    0x293: v293(0xe5) = CONST 
    0x295: v295(0x2) = CONST 
    0x297: v297(0x2000000000000000000000000000000000000000000000000000000000) = EXP v295(0x2), v293(0xe5)
    0x298: v298(0x461bcd) = CONST 
    0x29c: v29c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v298(0x461bcd), v297(0x2000000000000000000000000000000000000000000000000000000000)
    0x29e: MSTORE v292, v29c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x29f: v29f(0x20) = CONST 
    0x2a1: v2a1(0x4) = CONST 
    0x2a4: v2a4 = ADD v292, v2a1(0x4)
    0x2a5: MSTORE v2a4, v29f(0x20)
    0x2a6: v2a6(0x2c) = CONST 
    0x2a8: v2a8(0x24) = CONST 
    0x2ab: v2ab = ADD v292, v2a8(0x24)
    0x2ac: MSTORE v2ab, v2a6(0x2c)
    0x2ad: v2ad(0x4e657720696d706c656d656e746174696f6e2063616e6e6f7420626520746865) = CONST 
    0x2ce: v2ce(0x44) = CONST 
    0x2d1: v2d1 = ADD v292, v2ce(0x44)
    0x2d2: MSTORE v2d1, v2ad(0x4e657720696d706c656d656e746174696f6e2063616e6e6f7420626520746865)
    0x2d3: v2d3(0x2073616d65206173206f6c640000000000000000000000000000000000000000) = CONST 
    0x2f4: v2f4(0x64) = CONST 
    0x2f7: v2f7 = ADD v292, v2f4(0x64)
    0x2f8: MSTORE v2f7, v2d3(0x2073616d65206173206f6c640000000000000000000000000000000000000000)
    0x2fa: v2fa = MLOAD v28f(0x40)
    0x2fe: v2fe(0x0) = SUB v292, v2fa
    0x2ff: v2ff(0x84) = CONST 
    0x301: v301(0x84) = ADD v2ff(0x84), v2fe(0x0)
    0x303: REVERT v2fa, v301(0x84)

    Begin block 0x304
    prev=[0x278], succ=[0x74c]
    =================================
    0x305: v305(0x2) = CONST 
    0x308: v308 = SLOAD v305(0x2)
    0x309: v309(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x31e: v31e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v309(0xffffffffffffffffffffffffffffffffffffffff)
    0x31f: v31f = AND v31e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v308
    0x320: v320(0x1) = CONST 
    0x322: v322(0xa0) = CONST 
    0x324: v324(0x2) = CONST 
    0x326: v326(0x10000000000000000000000000000000000000000) = EXP v324(0x2), v322(0xa0)
    0x327: v327(0xffffffffffffffffffffffffffffffffffffffff) = SUB v326(0x10000000000000000000000000000000000000000), v320(0x1)
    0x329: v329 = AND v13c, v327(0xffffffffffffffffffffffffffffffffffffffff)
    0x32c: v32c = OR v329, v31f
    0x32f: SSTORE v305(0x2), v32c
    0x330: v330(0x40) = CONST 
    0x332: v332 = MLOAD v330(0x40)
    0x333: v333(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x355: v355(0x0) = CONST 
    0x358: LOG2 v332, v355(0x0), v333(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v329
    0x35a: JUMP v11c(0x74c)

    Begin block 0x74c
    prev=[0x304], succ=[]
    =================================
    0x74d: STOP 

}

function implementation()() public {
    Begin block 0x143
    prev=[], succ=[0x14b, 0x14f]
    =================================
    0x144: v144 = CALLVALUE 
    0x146: v146 = ISZERO v144
    0x147: v147(0x14f) = CONST 
    0x14a: JUMPI v147(0x14f), v146

    Begin block 0x14b
    prev=[0x143], succ=[]
    =================================
    0x14b: v14b(0x0) = CONST 
    0x14e: REVERT v14b(0x0), v14b(0x0)

    Begin block 0x14f
    prev=[0x143], succ=[0x35b]
    =================================
    0x151: v151(0x76d) = CONST 
    0x154: v154(0x35b) = CONST 
    0x157: JUMP v154(0x35b)

    Begin block 0x35b
    prev=[0x14f], succ=[0x76d]
    =================================
    0x35c: v35c(0x2) = CONST 
    0x35e: v35e = SLOAD v35c(0x2)
    0x35f: v35f(0x1) = CONST 
    0x361: v361(0xa0) = CONST 
    0x363: v363(0x2) = CONST 
    0x365: v365(0x10000000000000000000000000000000000000000) = EXP v363(0x2), v361(0xa0)
    0x366: v366(0xffffffffffffffffffffffffffffffffffffffff) = SUB v365(0x10000000000000000000000000000000000000000), v35f(0x1)
    0x367: v367 = AND v366(0xffffffffffffffffffffffffffffffffffffffff), v35e
    0x369: JUMP v151(0x76d)

    Begin block 0x76d
    prev=[0x35b], succ=[]
    =================================
    0x76e: v76e(0x40) = CONST 
    0x771: v771 = MLOAD v76e(0x40)
    0x772: v772(0x1) = CONST 
    0x774: v774(0xa0) = CONST 
    0x776: v776(0x2) = CONST 
    0x778: v778(0x10000000000000000000000000000000000000000) = EXP v776(0x2), v774(0xa0)
    0x779: v779(0xffffffffffffffffffffffffffffffffffffffff) = SUB v778(0x10000000000000000000000000000000000000000), v772(0x1)
    0x77c: v77c = AND v367, v779(0xffffffffffffffffffffffffffffffffffffffff)
    0x77e: MSTORE v771, v77c
    0x77f: v77f = MLOAD v76e(0x40)
    0x783: v783(0x0) = SUB v771, v77f
    0x784: v784(0x20) = CONST 
    0x786: v786(0x20) = ADD v784(0x20), v783(0x0)
    0x788: RETURN v77f, v786(0x20)

}

function initProxyOwnership(address)() public {
    Begin block 0x158
    prev=[], succ=[0x160, 0x164]
    =================================
    0x159: v159 = CALLVALUE 
    0x15b: v15b = ISZERO v159
    0x15c: v15c(0x164) = CONST 
    0x15f: JUMPI v15c(0x164), v15b

    Begin block 0x160
    prev=[0x158], succ=[]
    =================================
    0x160: v160(0x0) = CONST 
    0x163: REVERT v160(0x0), v160(0x0)

    Begin block 0x164
    prev=[0x158], succ=[0x177, 0x17b]
    =================================
    0x166: v166(0x7a8) = CONST 
    0x169: v169(0x4) = CONST 
    0x16c: v16c = CALLDATASIZE 
    0x16d: v16d = SUB v16c, v169(0x4)
    0x16e: v16e(0x20) = CONST 
    0x171: v171 = LT v16d, v16e(0x20)
    0x172: v172 = ISZERO v171
    0x173: v173(0x17b) = CONST 
    0x176: JUMPI v173(0x17b), v172

    Begin block 0x177
    prev=[0x164], succ=[]
    =================================
    0x177: v177(0x0) = CONST 
    0x17a: REVERT v177(0x0), v177(0x0)

    Begin block 0x17b
    prev=[0x164], succ=[0x36a]
    =================================
    0x17d: v17d = CALLDATALOAD v169(0x4)
    0x17e: v17e(0x1) = CONST 
    0x180: v180(0xa0) = CONST 
    0x182: v182(0x2) = CONST 
    0x184: v184(0x10000000000000000000000000000000000000000) = EXP v182(0x2), v180(0xa0)
    0x185: v185(0xffffffffffffffffffffffffffffffffffffffff) = SUB v184(0x10000000000000000000000000000000000000000), v17e(0x1)
    0x186: v186 = AND v185(0xffffffffffffffffffffffffffffffffffffffff), v17d
    0x187: v187(0x36a) = CONST 
    0x18a: JUMP v187(0x36a)

    Begin block 0x36a
    prev=[0x17b], succ=[0x37c, 0x3cb]
    =================================
    0x36b: v36b(0x0) = CONST 
    0x36d: v36d = SLOAD v36b(0x0)
    0x36e: v36e(0x1) = CONST 
    0x370: v370(0xa0) = CONST 
    0x372: v372(0x2) = CONST 
    0x374: v374(0x10000000000000000000000000000000000000000) = EXP v372(0x2), v370(0xa0)
    0x375: v375(0xffffffffffffffffffffffffffffffffffffffff) = SUB v374(0x10000000000000000000000000000000000000000), v36e(0x1)
    0x376: v376 = AND v375(0xffffffffffffffffffffffffffffffffffffffff), v36d
    0x377: v377 = ISZERO v376
    0x378: v378(0x3cb) = CONST 
    0x37b: JUMPI v378(0x3cb), v377

    Begin block 0x37c
    prev=[0x36a], succ=[]
    =================================
    0x37c: v37c(0x40) = CONST 
    0x37f: v37f = MLOAD v37c(0x40)
    0x380: v380(0xe5) = CONST 
    0x382: v382(0x2) = CONST 
    0x384: v384(0x2000000000000000000000000000000000000000000000000000000000) = EXP v382(0x2), v380(0xe5)
    0x385: v385(0x461bcd) = CONST 
    0x389: v389(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v385(0x461bcd), v384(0x2000000000000000000000000000000000000000000000000000000000)
    0x38b: MSTORE v37f, v389(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x38c: v38c(0x20) = CONST 
    0x38e: v38e(0x4) = CONST 
    0x391: v391 = ADD v37f, v38e(0x4)
    0x392: MSTORE v391, v38c(0x20)
    0x393: v393(0x16) = CONST 
    0x395: v395(0x24) = CONST 
    0x398: v398 = ADD v37f, v395(0x24)
    0x399: MSTORE v398, v393(0x16)
    0x39a: v39a(0x4f776e61626c653a20616c7265616479206f776e656400000000000000000000) = CONST 
    0x3bb: v3bb(0x44) = CONST 
    0x3be: v3be = ADD v37f, v3bb(0x44)
    0x3bf: MSTORE v3be, v39a(0x4f776e61626c653a20616c7265616479206f776e656400000000000000000000)
    0x3c1: v3c1 = MLOAD v37c(0x40)
    0x3c5: v3c5(0x0) = SUB v37f, v3c1
    0x3c6: v3c6(0x64) = CONST 
    0x3c8: v3c8(0x64) = ADD v3c6(0x64), v3c5(0x0)
    0x3ca: REVERT v3c1, v3c8(0x64)

    Begin block 0x3cb
    prev=[0x36a], succ=[0x3dc, 0x451]
    =================================
    0x3cc: v3cc(0x1) = CONST 
    0x3ce: v3ce(0xa0) = CONST 
    0x3d0: v3d0(0x2) = CONST 
    0x3d2: v3d2(0x10000000000000000000000000000000000000000) = EXP v3d0(0x2), v3ce(0xa0)
    0x3d3: v3d3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d2(0x10000000000000000000000000000000000000000), v3cc(0x1)
    0x3d5: v3d5 = AND v186, v3d3(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d6: v3d6 = ISZERO v3d5
    0x3d7: v3d7 = ISZERO v3d6
    0x3d8: v3d8(0x451) = CONST 
    0x3db: JUMPI v3d8(0x451), v3d7

    Begin block 0x3dc
    prev=[0x3cb], succ=[]
    =================================
    0x3dc: v3dc(0x40) = CONST 
    0x3df: v3df = MLOAD v3dc(0x40)
    0x3e0: v3e0(0xe5) = CONST 
    0x3e2: v3e2(0x2) = CONST 
    0x3e4: v3e4(0x2000000000000000000000000000000000000000000000000000000000) = EXP v3e2(0x2), v3e0(0xe5)
    0x3e5: v3e5(0x461bcd) = CONST 
    0x3e9: v3e9(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v3e5(0x461bcd), v3e4(0x2000000000000000000000000000000000000000000000000000000000)
    0x3eb: MSTORE v3df, v3e9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3ec: v3ec(0x20) = CONST 
    0x3ee: v3ee(0x4) = CONST 
    0x3f1: v3f1 = ADD v3df, v3ee(0x4)
    0x3f2: MSTORE v3f1, v3ec(0x20)
    0x3f3: v3f3(0x26) = CONST 
    0x3f5: v3f5(0x24) = CONST 
    0x3f8: v3f8 = ADD v3df, v3f5(0x24)
    0x3f9: MSTORE v3f8, v3f3(0x26)
    0x3fa: v3fa(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061) = CONST 
    0x41b: v41b(0x44) = CONST 
    0x41e: v41e = ADD v3df, v41b(0x44)
    0x41f: MSTORE v41e, v3fa(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061)
    0x420: v420(0x6464726573730000000000000000000000000000000000000000000000000000) = CONST 
    0x441: v441(0x64) = CONST 
    0x444: v444 = ADD v3df, v441(0x64)
    0x445: MSTORE v444, v420(0x6464726573730000000000000000000000000000000000000000000000000000)
    0x447: v447 = MLOAD v3dc(0x40)
    0x44b: v44b(0x0) = SUB v3df, v447
    0x44c: v44c(0x84) = CONST 
    0x44e: v44e(0x84) = ADD v44c(0x84), v44b(0x0)
    0x450: REVERT v447, v44e(0x84)

    Begin block 0x451
    prev=[0x3cb], succ=[0x51cB0x451]
    =================================
    0x452: v452(0x45a) = CONST 
    0x456: v456(0x51c) = CONST 
    0x459: JUMP v456(0x51c), v186, v452(0x45a)

    Begin block 0x51cB0x451
    prev=[0x451], succ=[0x52dB0x451, 0x5a2B0x451]
    =================================
    0x51dS0x451: v51dV451(0x1) = CONST 
    0x51fS0x451: v51fV451(0xa0) = CONST 
    0x521S0x451: v521V451(0x2) = CONST 
    0x523S0x451: v523V451(0x10000000000000000000000000000000000000000) = EXP v521V451(0x2), v51fV451(0xa0)
    0x524S0x451: v524V451(0xffffffffffffffffffffffffffffffffffffffff) = SUB v523V451(0x10000000000000000000000000000000000000000), v51dV451(0x1)
    0x526S0x451: v526V451 = AND v186, v524V451(0xffffffffffffffffffffffffffffffffffffffff)
    0x527S0x451: v527V451 = ISZERO v526V451
    0x528S0x451: v528V451 = ISZERO v527V451
    0x529S0x451: v529V451(0x5a2) = CONST 
    0x52cS0x451: JUMPI v529V451(0x5a2), v528V451

    Begin block 0x52dB0x451
    prev=[0x51cB0x451], succ=[]
    =================================
    0x52dS0x451: v52dV451(0x40) = CONST 
    0x530S0x451: v530V451 = MLOAD v52dV451(0x40)
    0x531S0x451: v531V451(0xe5) = CONST 
    0x533S0x451: v533V451(0x2) = CONST 
    0x535S0x451: v535V451(0x2000000000000000000000000000000000000000000000000000000000) = EXP v533V451(0x2), v531V451(0xe5)
    0x536S0x451: v536V451(0x461bcd) = CONST 
    0x53aS0x451: v53aV451(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v536V451(0x461bcd), v535V451(0x2000000000000000000000000000000000000000000000000000000000)
    0x53cS0x451: MSTORE v530V451, v53aV451(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x53dS0x451: v53dV451(0x20) = CONST 
    0x53fS0x451: v53fV451(0x4) = CONST 
    0x542S0x451: v542V451 = ADD v530V451, v53fV451(0x4)
    0x543S0x451: MSTORE v542V451, v53dV451(0x20)
    0x544S0x451: v544V451(0x26) = CONST 
    0x546S0x451: v546V451(0x24) = CONST 
    0x549S0x451: v549V451 = ADD v530V451, v546V451(0x24)
    0x54aS0x451: MSTORE v549V451, v544V451(0x26)
    0x54bS0x451: v54bV451(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061) = CONST 
    0x56cS0x451: v56cV451(0x44) = CONST 
    0x56fS0x451: v56fV451 = ADD v530V451, v56cV451(0x44)
    0x570S0x451: MSTORE v56fV451, v54bV451(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061)
    0x571S0x451: v571V451(0x6464726573730000000000000000000000000000000000000000000000000000) = CONST 
    0x592S0x451: v592V451(0x64) = CONST 
    0x595S0x451: v595V451 = ADD v530V451, v592V451(0x64)
    0x596S0x451: MSTORE v595V451, v571V451(0x6464726573730000000000000000000000000000000000000000000000000000)
    0x598S0x451: v598V451 = MLOAD v52dV451(0x40)
    0x59cS0x451: v59cV451(0x0) = SUB v530V451, v598V451
    0x59dS0x451: v59dV451(0x84) = CONST 
    0x59fS0x451: v59fV451(0x84) = ADD v59dV451(0x84), v59cV451(0x0)
    0x5a1S0x451: REVERT v598V451, v59fV451(0x84)

    Begin block 0x5a2B0x451
    prev=[0x51cB0x451], succ=[0x45a]
    =================================
    0x5a3S0x451: v5a3V451(0x1) = CONST 
    0x5a6S0x451: v5a6V451 = SLOAD v5a3V451(0x1)
    0x5a7S0x451: v5a7V451(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5bcS0x451: v5bcV451(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5a7V451(0xffffffffffffffffffffffffffffffffffffffff)
    0x5bdS0x451: v5bdV451 = AND v5bcV451(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5a6V451
    0x5beS0x451: v5beV451(0x1) = CONST 
    0x5c0S0x451: v5c0V451(0xa0) = CONST 
    0x5c2S0x451: v5c2V451(0x2) = CONST 
    0x5c4S0x451: v5c4V451(0x10000000000000000000000000000000000000000) = EXP v5c2V451(0x2), v5c0V451(0xa0)
    0x5c5S0x451: v5c5V451(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c4V451(0x10000000000000000000000000000000000000000), v5beV451(0x1)
    0x5c9S0x451: v5c9V451 = AND v5c5V451(0xffffffffffffffffffffffffffffffffffffffff), v186
    0x5cdS0x451: v5cdV451 = OR v5c9V451, v5bdV451
    0x5cfS0x451: SSTORE v5a3V451(0x1), v5cdV451
    0x5d0S0x451: JUMP v452(0x45a)

    Begin block 0x45a
    prev=[0x5a2B0x451], succ=[0x7a8]
    =================================
    0x45c: JUMP v166(0x7a8)

    Begin block 0x7a8
    prev=[0x45a], succ=[]
    =================================
    0x7a9: STOP 

}

function isProxyOwner()() public {
    Begin block 0x18b
    prev=[], succ=[0x193, 0x197]
    =================================
    0x18c: v18c = CALLVALUE 
    0x18e: v18e = ISZERO v18c
    0x18f: v18f(0x197) = CONST 
    0x192: JUMPI v18f(0x197), v18e

    Begin block 0x193
    prev=[0x18b], succ=[]
    =================================
    0x193: v193(0x0) = CONST 
    0x196: REVERT v193(0x0), v193(0x0)

    Begin block 0x197
    prev=[0x18b], succ=[0x45dB0x197]
    =================================
    0x199: v199(0x1a0) = CONST 
    0x19c: v19c(0x45d) = CONST 
    0x19f: JUMP v19c(0x45d)

    Begin block 0x45dB0x197
    prev=[0x197], succ=[0x1a0]
    =================================
    0x45eS0x197: v45eV197(0x0) = CONST 
    0x460S0x197: v460V197 = SLOAD v45eV197(0x0)
    0x461S0x197: v461V197(0x1) = CONST 
    0x463S0x197: v463V197(0xa0) = CONST 
    0x465S0x197: v465V197(0x2) = CONST 
    0x467S0x197: v467V197(0x10000000000000000000000000000000000000000) = EXP v465V197(0x2), v463V197(0xa0)
    0x468S0x197: v468V197(0xffffffffffffffffffffffffffffffffffffffff) = SUB v467V197(0x10000000000000000000000000000000000000000), v461V197(0x1)
    0x469S0x197: v469V197 = AND v468V197(0xffffffffffffffffffffffffffffffffffffffff), v460V197
    0x46aS0x197: v46aV197 = CALLER 
    0x46bS0x197: v46bV197 = EQ v46aV197, v469V197
    0x46dS0x197: JUMP v199(0x1a0)

    Begin block 0x1a0
    prev=[0x45dB0x197], succ=[]
    =================================
    0x1a1: v1a1(0x40) = CONST 
    0x1a4: v1a4 = MLOAD v1a1(0x40)
    0x1a6: v1a6 = ISZERO v46bV197
    0x1a7: v1a7 = ISZERO v1a6
    0x1a9: MSTORE v1a4, v1a7
    0x1aa: v1aa = MLOAD v1a1(0x40)
    0x1ae: v1ae(0x0) = SUB v1a4, v1aa
    0x1af: v1af(0x20) = CONST 
    0x1b1: v1b1(0x20) = ADD v1af(0x20), v1ae(0x0)
    0x1b3: RETURN v1aa, v1b1(0x20)

}

function claimProxyOwnership()() public {
    Begin block 0x1b4
    prev=[], succ=[0x1bc, 0x1c0]
    =================================
    0x1b5: v1b5 = CALLVALUE 
    0x1b7: v1b7 = ISZERO v1b5
    0x1b8: v1b8(0x1c0) = CONST 
    0x1bb: JUMPI v1b8(0x1c0), v1b7

    Begin block 0x1bc
    prev=[0x1b4], succ=[]
    =================================
    0x1bc: v1bc(0x0) = CONST 
    0x1bf: REVERT v1bc(0x0), v1bc(0x0)

    Begin block 0x1c0
    prev=[0x1b4], succ=[0x46eB0x1c0]
    =================================
    0x1c2: v1c2(0x7c9) = CONST 
    0x1c5: v1c5(0x46e) = CONST 
    0x1c8: JUMP v1c5(0x46e), v1c2(0x7c9)

    Begin block 0x46eB0x1c0
    prev=[0x1c0], succ=[0x5d1B0x1c0]
    =================================
    0x46fS0x1c0: v46fV1c0(0x477) = CONST 
    0x472S0x1c0: v472V1c0 = CALLER 
    0x473S0x1c0: v473V1c0(0x5d1) = CONST 
    0x476S0x1c0: JUMP v473V1c0(0x5d1)

    Begin block 0x5d1B0x1c0
    prev=[0x46eB0x1c0], succ=[0x5e7B0x1c0, 0x636B0x1c0]
    =================================
    0x5d2S0x1c0: v5d2V1c0(0x1) = CONST 
    0x5d4S0x1c0: v5d4V1c0 = SLOAD v5d2V1c0(0x1)
    0x5d5S0x1c0: v5d5V1c0(0x1) = CONST 
    0x5d7S0x1c0: v5d7V1c0(0xa0) = CONST 
    0x5d9S0x1c0: v5d9V1c0(0x2) = CONST 
    0x5dbS0x1c0: v5dbV1c0(0x10000000000000000000000000000000000000000) = EXP v5d9V1c0(0x2), v5d7V1c0(0xa0)
    0x5dcS0x1c0: v5dcV1c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5dbV1c0(0x10000000000000000000000000000000000000000), v5d5V1c0(0x1)
    0x5dfS0x1c0: v5dfV1c0 = AND v5dcV1c0(0xffffffffffffffffffffffffffffffffffffffff), v472V1c0
    0x5e1S0x1c0: v5e1V1c0 = AND v5d4V1c0, v5dcV1c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x5e2S0x1c0: v5e2V1c0 = EQ v5e1V1c0, v5dfV1c0
    0x5e3S0x1c0: v5e3V1c0(0x636) = CONST 
    0x5e6S0x1c0: JUMPI v5e3V1c0(0x636), v5e2V1c0

    Begin block 0x5e7B0x1c0
    prev=[0x5d1B0x1c0], succ=[]
    =================================
    0x5e7S0x1c0: v5e7V1c0(0x40) = CONST 
    0x5eaS0x1c0: v5eaV1c0 = MLOAD v5e7V1c0(0x40)
    0x5ebS0x1c0: v5ebV1c0(0xe5) = CONST 
    0x5edS0x1c0: v5edV1c0(0x2) = CONST 
    0x5efS0x1c0: v5efV1c0(0x2000000000000000000000000000000000000000000000000000000000) = EXP v5edV1c0(0x2), v5ebV1c0(0xe5)
    0x5f0S0x1c0: v5f0V1c0(0x461bcd) = CONST 
    0x5f4S0x1c0: v5f4V1c0(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v5f0V1c0(0x461bcd), v5efV1c0(0x2000000000000000000000000000000000000000000000000000000000)
    0x5f6S0x1c0: MSTORE v5eaV1c0, v5f4V1c0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5f7S0x1c0: v5f7V1c0(0x20) = CONST 
    0x5f9S0x1c0: v5f9V1c0(0x4) = CONST 
    0x5fcS0x1c0: v5fcV1c0 = ADD v5eaV1c0, v5f9V1c0(0x4)
    0x5fdS0x1c0: MSTORE v5fcV1c0, v5f7V1c0(0x20)
    0x5feS0x1c0: v5feV1c0(0x18) = CONST 
    0x600S0x1c0: v600V1c0(0x24) = CONST 
    0x603S0x1c0: v603V1c0 = ADD v5eaV1c0, v600V1c0(0x24)
    0x604S0x1c0: MSTORE v603V1c0, v5feV1c0(0x18)
    0x605S0x1c0: v605V1c0(0x436c61696d65642062792077726f6e6720616464726573730000000000000000) = CONST 
    0x626S0x1c0: v626V1c0(0x44) = CONST 
    0x629S0x1c0: v629V1c0 = ADD v5eaV1c0, v626V1c0(0x44)
    0x62aS0x1c0: MSTORE v629V1c0, v605V1c0(0x436c61696d65642062792077726f6e6720616464726573730000000000000000)
    0x62cS0x1c0: v62cV1c0 = MLOAD v5e7V1c0(0x40)
    0x630S0x1c0: v630V1c0(0x0) = SUB v5eaV1c0, v62cV1c0
    0x631S0x1c0: v631V1c0(0x64) = CONST 
    0x633S0x1c0: v633V1c0(0x64) = ADD v631V1c0(0x64), v630V1c0(0x0)
    0x635S0x1c0: REVERT v62cV1c0, v633V1c0(0x64)

    Begin block 0x636B0x1c0
    prev=[0x5d1B0x1c0], succ=[0x477B0x1c0]
    =================================
    0x637S0x1c0: v637V1c0(0x0) = CONST 
    0x63aS0x1c0: v63aV1c0 = SLOAD v637V1c0(0x0)
    0x63bS0x1c0: v63bV1c0(0x40) = CONST 
    0x63dS0x1c0: v63dV1c0 = MLOAD v63bV1c0(0x40)
    0x63eS0x1c0: v63eV1c0(0x1) = CONST 
    0x640S0x1c0: v640V1c0(0xa0) = CONST 
    0x642S0x1c0: v642V1c0(0x2) = CONST 
    0x644S0x1c0: v644V1c0(0x10000000000000000000000000000000000000000) = EXP v642V1c0(0x2), v640V1c0(0xa0)
    0x645S0x1c0: v645V1c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v644V1c0(0x10000000000000000000000000000000000000000), v63eV1c0(0x1)
    0x648S0x1c0: v648V1c0 = AND v472V1c0, v645V1c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x64bS0x1c0: v64bV1c0 = AND v63aV1c0, v645V1c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x64dS0x1c0: v64dV1c0(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9) = CONST 
    0x66fS0x1c0: LOG3 v63dV1c0, v637V1c0(0x0), v64dV1c0(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9), v64bV1c0, v648V1c0
    0x670S0x1c0: v670V1c0(0x0) = CONST 
    0x673S0x1c0: v673V1c0 = SLOAD v670V1c0(0x0)
    0x674S0x1c0: v674V1c0(0x1) = CONST 
    0x676S0x1c0: v676V1c0(0xa0) = CONST 
    0x678S0x1c0: v678V1c0(0x2) = CONST 
    0x67aS0x1c0: v67aV1c0(0x10000000000000000000000000000000000000000) = EXP v678V1c0(0x2), v676V1c0(0xa0)
    0x67bS0x1c0: v67bV1c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v67aV1c0(0x10000000000000000000000000000000000000000), v674V1c0(0x1)
    0x67eS0x1c0: v67eV1c0 = AND v472V1c0, v67bV1c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x67fS0x1c0: v67fV1c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x694S0x1c0: v694V1c0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v67fV1c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x697S0x1c0: v697V1c0 = AND v694V1c0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v673V1c0
    0x698S0x1c0: v698V1c0 = OR v697V1c0, v67eV1c0
    0x69aS0x1c0: SSTORE v670V1c0(0x0), v698V1c0
    0x69bS0x1c0: v69bV1c0(0x1) = CONST 
    0x69eS0x1c0: v69eV1c0 = SLOAD v69bV1c0(0x1)
    0x6a1S0x1c0: v6a1V1c0 = AND v694V1c0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v69eV1c0
    0x6a3S0x1c0: SSTORE v69bV1c0(0x1), v6a1V1c0
    0x6a4S0x1c0: JUMP v46fV1c0(0x477)

    Begin block 0x477B0x1c0
    prev=[0x636B0x1c0], succ=[0x7c9]
    =================================
    0x478S0x1c0: JUMP v1c2(0x7c9)

    Begin block 0x7c9
    prev=[0x477B0x1c0], succ=[]
    =================================
    0x7ca: STOP 

}

function transferProxyOwnership(address)() public {
    Begin block 0x1c9
    prev=[], succ=[0x1d1, 0x1d5]
    =================================
    0x1ca: v1ca = CALLVALUE 
    0x1cc: v1cc = ISZERO v1ca
    0x1cd: v1cd(0x1d5) = CONST 
    0x1d0: JUMPI v1cd(0x1d5), v1cc

    Begin block 0x1d1
    prev=[0x1c9], succ=[]
    =================================
    0x1d1: v1d1(0x0) = CONST 
    0x1d4: REVERT v1d1(0x0), v1d1(0x0)

    Begin block 0x1d5
    prev=[0x1c9], succ=[0x1e8, 0x1ec]
    =================================
    0x1d7: v1d7(0x7ea) = CONST 
    0x1da: v1da(0x4) = CONST 
    0x1dd: v1dd = CALLDATASIZE 
    0x1de: v1de = SUB v1dd, v1da(0x4)
    0x1df: v1df(0x20) = CONST 
    0x1e2: v1e2 = LT v1de, v1df(0x20)
    0x1e3: v1e3 = ISZERO v1e2
    0x1e4: v1e4(0x1ec) = CONST 
    0x1e7: JUMPI v1e4(0x1ec), v1e3

    Begin block 0x1e8
    prev=[0x1d5], succ=[]
    =================================
    0x1e8: v1e8(0x0) = CONST 
    0x1eb: REVERT v1e8(0x0), v1e8(0x0)

    Begin block 0x1ec
    prev=[0x1d5], succ=[0x479]
    =================================
    0x1ee: v1ee = CALLDATALOAD v1da(0x4)
    0x1ef: v1ef(0x1) = CONST 
    0x1f1: v1f1(0xa0) = CONST 
    0x1f3: v1f3(0x2) = CONST 
    0x1f5: v1f5(0x10000000000000000000000000000000000000000) = EXP v1f3(0x2), v1f1(0xa0)
    0x1f6: v1f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f5(0x10000000000000000000000000000000000000000), v1ef(0x1)
    0x1f7: v1f7 = AND v1f6(0xffffffffffffffffffffffffffffffffffffffff), v1ee
    0x1f8: v1f8(0x479) = CONST 
    0x1fb: JUMP v1f8(0x479)

    Begin block 0x479
    prev=[0x1ec], succ=[0x45dB0x479]
    =================================
    0x47a: v47a(0x481) = CONST 
    0x47d: v47d(0x45d) = CONST 
    0x480: JUMP v47d(0x45d)

    Begin block 0x45dB0x479
    prev=[0x479], succ=[0x481]
    =================================
    0x45eS0x479: v45eV479(0x0) = CONST 
    0x460S0x479: v460V479 = SLOAD v45eV479(0x0)
    0x461S0x479: v461V479(0x1) = CONST 
    0x463S0x479: v463V479(0xa0) = CONST 
    0x465S0x479: v465V479(0x2) = CONST 
    0x467S0x479: v467V479(0x10000000000000000000000000000000000000000) = EXP v465V479(0x2), v463V479(0xa0)
    0x468S0x479: v468V479(0xffffffffffffffffffffffffffffffffffffffff) = SUB v467V479(0x10000000000000000000000000000000000000000), v461V479(0x1)
    0x469S0x479: v469V479 = AND v468V479(0xffffffffffffffffffffffffffffffffffffffff), v460V479
    0x46aS0x479: v46aV479 = CALLER 
    0x46bS0x479: v46bV479 = EQ v46aV479, v469V479
    0x46dS0x479: JUMP v47a(0x481)

    Begin block 0x481
    prev=[0x45dB0x479], succ=[0x488, 0x4d7]
    =================================
    0x482: v482 = ISZERO v46bV479
    0x483: v483 = ISZERO v482
    0x484: v484(0x4d7) = CONST 
    0x487: JUMPI v484(0x4d7), v483

    Begin block 0x488
    prev=[0x481], succ=[]
    =================================
    0x488: v488(0x40) = CONST 
    0x48b: v48b = MLOAD v488(0x40)
    0x48c: v48c(0xe5) = CONST 
    0x48e: v48e(0x2) = CONST 
    0x490: v490(0x2000000000000000000000000000000000000000000000000000000000) = EXP v48e(0x2), v48c(0xe5)
    0x491: v491(0x461bcd) = CONST 
    0x495: v495(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v491(0x461bcd), v490(0x2000000000000000000000000000000000000000000000000000000000)
    0x497: MSTORE v48b, v495(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x498: v498(0x20) = CONST 
    0x49a: v49a(0x4) = CONST 
    0x49d: v49d = ADD v48b, v49a(0x4)
    0x4a0: MSTORE v49d, v498(0x20)
    0x4a1: v4a1(0x24) = CONST 
    0x4a4: v4a4 = ADD v48b, v4a1(0x24)
    0x4a5: MSTORE v4a4, v498(0x20)
    0x4a6: v4a6(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x4c7: v4c7(0x44) = CONST 
    0x4ca: v4ca = ADD v48b, v4c7(0x44)
    0x4cb: MSTORE v4ca, v4a6(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x4cd: v4cd = MLOAD v488(0x40)
    0x4d1: v4d1(0x0) = SUB v48b, v4cd
    0x4d2: v4d2(0x64) = CONST 
    0x4d4: v4d4(0x64) = ADD v4d2(0x64), v4d1(0x0)
    0x4d6: REVERT v4cd, v4d4(0x64)

    Begin block 0x4d7
    prev=[0x481], succ=[0x51cB0x4d7]
    =================================
    0x4d8: v4d8(0x4e0) = CONST 
    0x4dc: v4dc(0x51c) = CONST 
    0x4df: JUMP v4dc(0x51c), v1f7, v4d8(0x4e0)

    Begin block 0x51cB0x4d7
    prev=[0x4d7], succ=[0x52dB0x4d7, 0x5a2B0x4d7]
    =================================
    0x51dS0x4d7: v51dV4d7(0x1) = CONST 
    0x51fS0x4d7: v51fV4d7(0xa0) = CONST 
    0x521S0x4d7: v521V4d7(0x2) = CONST 
    0x523S0x4d7: v523V4d7(0x10000000000000000000000000000000000000000) = EXP v521V4d7(0x2), v51fV4d7(0xa0)
    0x524S0x4d7: v524V4d7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v523V4d7(0x10000000000000000000000000000000000000000), v51dV4d7(0x1)
    0x526S0x4d7: v526V4d7 = AND v1f7, v524V4d7(0xffffffffffffffffffffffffffffffffffffffff)
    0x527S0x4d7: v527V4d7 = ISZERO v526V4d7
    0x528S0x4d7: v528V4d7 = ISZERO v527V4d7
    0x529S0x4d7: v529V4d7(0x5a2) = CONST 
    0x52cS0x4d7: JUMPI v529V4d7(0x5a2), v528V4d7

    Begin block 0x52dB0x4d7
    prev=[0x51cB0x4d7], succ=[]
    =================================
    0x52dS0x4d7: v52dV4d7(0x40) = CONST 
    0x530S0x4d7: v530V4d7 = MLOAD v52dV4d7(0x40)
    0x531S0x4d7: v531V4d7(0xe5) = CONST 
    0x533S0x4d7: v533V4d7(0x2) = CONST 
    0x535S0x4d7: v535V4d7(0x2000000000000000000000000000000000000000000000000000000000) = EXP v533V4d7(0x2), v531V4d7(0xe5)
    0x536S0x4d7: v536V4d7(0x461bcd) = CONST 
    0x53aS0x4d7: v53aV4d7(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v536V4d7(0x461bcd), v535V4d7(0x2000000000000000000000000000000000000000000000000000000000)
    0x53cS0x4d7: MSTORE v530V4d7, v53aV4d7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x53dS0x4d7: v53dV4d7(0x20) = CONST 
    0x53fS0x4d7: v53fV4d7(0x4) = CONST 
    0x542S0x4d7: v542V4d7 = ADD v530V4d7, v53fV4d7(0x4)
    0x543S0x4d7: MSTORE v542V4d7, v53dV4d7(0x20)
    0x544S0x4d7: v544V4d7(0x26) = CONST 
    0x546S0x4d7: v546V4d7(0x24) = CONST 
    0x549S0x4d7: v549V4d7 = ADD v530V4d7, v546V4d7(0x24)
    0x54aS0x4d7: MSTORE v549V4d7, v544V4d7(0x26)
    0x54bS0x4d7: v54bV4d7(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061) = CONST 
    0x56cS0x4d7: v56cV4d7(0x44) = CONST 
    0x56fS0x4d7: v56fV4d7 = ADD v530V4d7, v56cV4d7(0x44)
    0x570S0x4d7: MSTORE v56fV4d7, v54bV4d7(0x4f776e61626c653a206e6577206f776e657220697320746865207a65726f2061)
    0x571S0x4d7: v571V4d7(0x6464726573730000000000000000000000000000000000000000000000000000) = CONST 
    0x592S0x4d7: v592V4d7(0x64) = CONST 
    0x595S0x4d7: v595V4d7 = ADD v530V4d7, v592V4d7(0x64)
    0x596S0x4d7: MSTORE v595V4d7, v571V4d7(0x6464726573730000000000000000000000000000000000000000000000000000)
    0x598S0x4d7: v598V4d7 = MLOAD v52dV4d7(0x40)
    0x59cS0x4d7: v59cV4d7(0x0) = SUB v530V4d7, v598V4d7
    0x59dS0x4d7: v59dV4d7(0x84) = CONST 
    0x59fS0x4d7: v59fV4d7(0x84) = ADD v59dV4d7(0x84), v59cV4d7(0x0)
    0x5a1S0x4d7: REVERT v598V4d7, v59fV4d7(0x84)

    Begin block 0x5a2B0x4d7
    prev=[0x51cB0x4d7], succ=[0x4e0]
    =================================
    0x5a3S0x4d7: v5a3V4d7(0x1) = CONST 
    0x5a6S0x4d7: v5a6V4d7 = SLOAD v5a3V4d7(0x1)
    0x5a7S0x4d7: v5a7V4d7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5bcS0x4d7: v5bcV4d7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5a7V4d7(0xffffffffffffffffffffffffffffffffffffffff)
    0x5bdS0x4d7: v5bdV4d7 = AND v5bcV4d7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5a6V4d7
    0x5beS0x4d7: v5beV4d7(0x1) = CONST 
    0x5c0S0x4d7: v5c0V4d7(0xa0) = CONST 
    0x5c2S0x4d7: v5c2V4d7(0x2) = CONST 
    0x5c4S0x4d7: v5c4V4d7(0x10000000000000000000000000000000000000000) = EXP v5c2V4d7(0x2), v5c0V4d7(0xa0)
    0x5c5S0x4d7: v5c5V4d7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c4V4d7(0x10000000000000000000000000000000000000000), v5beV4d7(0x1)
    0x5c9S0x4d7: v5c9V4d7 = AND v5c5V4d7(0xffffffffffffffffffffffffffffffffffffffff), v1f7
    0x5cdS0x4d7: v5cdV4d7 = OR v5c9V4d7, v5bdV4d7
    0x5cfS0x4d7: SSTORE v5a3V4d7(0x1), v5cdV4d7
    0x5d0S0x4d7: JUMP v4d8(0x4e0)

    Begin block 0x4e0
    prev=[0x5a2B0x4d7], succ=[0x7ea]
    =================================
    0x4e1: v4e1(0x0) = CONST 
    0x4e4: v4e4 = SLOAD v4e1(0x0)
    0x4e5: v4e5(0x40) = CONST 
    0x4e7: v4e7 = MLOAD v4e5(0x40)
    0x4e8: v4e8(0x1) = CONST 
    0x4ea: v4ea(0xa0) = CONST 
    0x4ec: v4ec(0x2) = CONST 
    0x4ee: v4ee(0x10000000000000000000000000000000000000000) = EXP v4ec(0x2), v4ea(0xa0)
    0x4ef: v4ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ee(0x10000000000000000000000000000000000000000), v4e8(0x1)
    0x4f2: v4f2 = AND v1f7, v4ef(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f5: v4f5 = AND v4e4, v4ef(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f7: v4f7(0xb3d55174552271a4f1aaf36b72f50381e892171636b3fb5447fe00e995e7a37b) = CONST 
    0x519: LOG3 v4e7, v4e1(0x0), v4f7(0xb3d55174552271a4f1aaf36b72f50381e892171636b3fb5447fe00e995e7a37b), v4f5, v4f2
    0x51b: JUMP v1d7(0x7ea)

    Begin block 0x7ea
    prev=[0x4e0], succ=[]
    =================================
    0x7eb: STOP 

}

function fallback()() public {
    Begin block 0x8d
    prev=[], succ=[0xa1, 0xa5]
    =================================
    0x8e: v8e(0x2) = CONST 
    0x90: v90 = SLOAD v8e(0x2)
    0x91: v91(0x1) = CONST 
    0x93: v93(0xa0) = CONST 
    0x95: v95(0x2) = CONST 
    0x97: v97(0x10000000000000000000000000000000000000000) = EXP v95(0x2), v93(0xa0)
    0x98: v98(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97(0x10000000000000000000000000000000000000000), v91(0x1)
    0x99: v99 = AND v98(0xffffffffffffffffffffffffffffffffffffffff), v90
    0x9b: v9b = ISZERO v99
    0x9c: v9c = ISZERO v9b
    0x9d: v9d(0xa5) = CONST 
    0xa0: JUMPI v9d(0xa5), v9c

    Begin block 0xa1
    prev=[0x8d], succ=[]
    =================================
    0xa1: va1(0x0) = CONST 
    0xa4: REVERT va1(0x0), va1(0x0)

    Begin block 0xa5
    prev=[0x8d], succ=[0xc4, 0xc1]
    =================================
    0xa6: va6(0x40) = CONST 
    0xa8: va8 = MLOAD va6(0x40)
    0xa9: va9 = CALLDATASIZE 
    0xaa: vaa = RETURNDATASIZE 
    0xac: CALLDATACOPY va8, vaa, va9
    0xad: vad = RETURNDATASIZE 
    0xae: vae = RETURNDATASIZE 
    0xaf: vaf = CALLDATASIZE 
    0xb2: vb2 = GAS 
    0xb3: vb3 = DELEGATECALL vb2, v99, va8, vaf, vae, vad
    0xb4: vb4 = RETURNDATASIZE 
    0xb6: vb6(0x0) = CONST 
    0xb9: RETURNDATACOPY va8, vb6(0x0), vb4
    0xbc: vbc = ISZERO vb3
    0xbd: vbd(0xc4) = CONST 
    0xc0: JUMPI vbd(0xc4), vbc

    Begin block 0xc4
    prev=[0xa5], succ=[]
    =================================
    0xc7: REVERT va8, vb4

    Begin block 0xc1
    prev=[0xa5], succ=[]
    =================================
    0xc3: RETURN va8, vb4

}

function proxyOwner()() public {
    Begin block 0xc8
    prev=[], succ=[0xd0, 0xd4]
    =================================
    0xc9: vc9 = CALLVALUE 
    0xcb: vcb = ISZERO vc9
    0xcc: vcc(0xd4) = CONST 
    0xcf: JUMPI vcc(0xd4), vcb

    Begin block 0xd0
    prev=[0xc8], succ=[]
    =================================
    0xd0: vd0(0x0) = CONST 
    0xd3: REVERT vd0(0x0), vd0(0x0)

    Begin block 0xd4
    prev=[0xc8], succ=[0x1fc]
    =================================
    0xd6: vd6(0x6d6) = CONST 
    0xd9: vd9(0x1fc) = CONST 
    0xdc: JUMP vd9(0x1fc)

    Begin block 0x1fc
    prev=[0xd4], succ=[0x6d6]
    =================================
    0x1fd: v1fd(0x0) = CONST 
    0x1ff: v1ff = SLOAD v1fd(0x0)
    0x200: v200(0x1) = CONST 
    0x202: v202(0xa0) = CONST 
    0x204: v204(0x2) = CONST 
    0x206: v206(0x10000000000000000000000000000000000000000) = EXP v204(0x2), v202(0xa0)
    0x207: v207(0xffffffffffffffffffffffffffffffffffffffff) = SUB v206(0x10000000000000000000000000000000000000000), v200(0x1)
    0x208: v208 = AND v207(0xffffffffffffffffffffffffffffffffffffffff), v1ff
    0x20a: JUMP vd6(0x6d6)

    Begin block 0x6d6
    prev=[0x1fc], succ=[]
    =================================
    0x6d7: v6d7(0x40) = CONST 
    0x6da: v6da = MLOAD v6d7(0x40)
    0x6db: v6db(0x1) = CONST 
    0x6dd: v6dd(0xa0) = CONST 
    0x6df: v6df(0x2) = CONST 
    0x6e1: v6e1(0x10000000000000000000000000000000000000000) = EXP v6df(0x2), v6dd(0xa0)
    0x6e2: v6e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e1(0x10000000000000000000000000000000000000000), v6db(0x1)
    0x6e5: v6e5 = AND v208, v6e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x6e7: MSTORE v6da, v6e5
    0x6e8: v6e8 = MLOAD v6d7(0x40)
    0x6ec: v6ec(0x0) = SUB v6da, v6e8
    0x6ed: v6ed(0x20) = CONST 
    0x6ef: v6ef(0x20) = ADD v6ed(0x20), v6ec(0x0)
    0x6f1: RETURN v6e8, v6ef(0x20)

}

function pendingProxyOwner()() public {
    Begin block 0xf9
    prev=[], succ=[0x101, 0x105]
    =================================
    0xfa: vfa = CALLVALUE 
    0xfc: vfc = ISZERO vfa
    0xfd: vfd(0x105) = CONST 
    0x100: JUMPI vfd(0x105), vfc

    Begin block 0x101
    prev=[0xf9], succ=[]
    =================================
    0x101: v101(0x0) = CONST 
    0x104: REVERT v101(0x0), v101(0x0)

    Begin block 0x105
    prev=[0xf9], succ=[0x20b]
    =================================
    0x107: v107(0x711) = CONST 
    0x10a: v10a(0x20b) = CONST 
    0x10d: JUMP v10a(0x20b)

    Begin block 0x20b
    prev=[0x105], succ=[0x711]
    =================================
    0x20c: v20c(0x1) = CONST 
    0x20e: v20e = SLOAD v20c(0x1)
    0x20f: v20f(0x1) = CONST 
    0x211: v211(0xa0) = CONST 
    0x213: v213(0x2) = CONST 
    0x215: v215(0x10000000000000000000000000000000000000000) = EXP v213(0x2), v211(0xa0)
    0x216: v216(0xffffffffffffffffffffffffffffffffffffffff) = SUB v215(0x10000000000000000000000000000000000000000), v20f(0x1)
    0x217: v217 = AND v216(0xffffffffffffffffffffffffffffffffffffffff), v20e
    0x219: JUMP v107(0x711)

    Begin block 0x711
    prev=[0x20b], succ=[]
    =================================
    0x712: v712(0x40) = CONST 
    0x715: v715 = MLOAD v712(0x40)
    0x716: v716(0x1) = CONST 
    0x718: v718(0xa0) = CONST 
    0x71a: v71a(0x2) = CONST 
    0x71c: v71c(0x10000000000000000000000000000000000000000) = EXP v71a(0x2), v718(0xa0)
    0x71d: v71d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71c(0x10000000000000000000000000000000000000000), v716(0x1)
    0x720: v720 = AND v217, v71d(0xffffffffffffffffffffffffffffffffffffffff)
    0x722: MSTORE v715, v720
    0x723: v723 = MLOAD v712(0x40)
    0x727: v727(0x0) = SUB v715, v723
    0x728: v728(0x20) = CONST 
    0x72a: v72a(0x20) = ADD v728(0x20), v727(0x0)
    0x72c: RETURN v723, v72a(0x20)

}

