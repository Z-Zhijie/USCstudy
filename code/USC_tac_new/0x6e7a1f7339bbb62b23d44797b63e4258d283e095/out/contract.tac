function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x552]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x548: v548(0x552) = CONST 
    0x549: JUMPI v548(0x552), v8

    Begin block 0xd
    prev=[0x0], succ=[0x555, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x1a31c07c) = CONST 
    0x19: v19 = EQ v14(0x1a31c07c), v12
    0x54a: v54a(0x555) = CONST 
    0x54b: JUMPI v54a(0x555), v19

    Begin block 0x555
    prev=[0xd], succ=[]
    =================================
    0x556: v556(0x49) = CONST 
    0x557: CALLPRIVATE v556(0x49)

    Begin block 0x1e
    prev=[0xd], succ=[0x558, 0x29]
    =================================
    0x1f: v1f(0x3659cfe6) = CONST 
    0x24: v24 = EQ v1f(0x3659cfe6), v12
    0x54c: v54c(0x558) = CONST 
    0x54d: JUMPI v54c(0x558), v24

    Begin block 0x558
    prev=[0x1e], succ=[]
    =================================
    0x559: v559(0x7a) = CONST 
    0x55a: CALLPRIVATE v559(0x7a)

    Begin block 0x29
    prev=[0x1e], succ=[0x55b, 0x34]
    =================================
    0x2a: v2a(0x5c60da1b) = CONST 
    0x2f: v2f = EQ v2a(0x5c60da1b), v12
    0x54e: v54e(0x55b) = CONST 
    0x54f: JUMPI v54e(0x55b), v2f

    Begin block 0x55b
    prev=[0x29], succ=[]
    =================================
    0x55c: v55c(0xad) = CONST 
    0x55d: CALLPRIVATE v55c(0xad)

    Begin block 0x34
    prev=[0x29], succ=[0x552, 0x55e]
    =================================
    0x35: v35(0x91f52f7c) = CONST 
    0x3a: v3a = EQ v35(0x91f52f7c), v12
    0x550: v550(0x55e) = CONST 
    0x551: JUMPI v550(0x55e), v3a

    Begin block 0x552
    prev=[0x0, 0x34], succ=[]
    =================================
    0x553: v553(0x3f) = CONST 
    0x554: CALLPRIVATE v553(0x3f)

    Begin block 0x55e
    prev=[0x34], succ=[]
    =================================
    0x55f: v55f(0xc2) = CONST 
    0x560: CALLPRIVATE v55f(0xc2)

}

function fallback()() public {
    Begin block 0x3f
    prev=[], succ=[0xf5]
    =================================
    0x40: v40(0x44c) = CONST 
    0x43: v43(0xf5) = CONST 
    0x46: JUMP v43(0xf5)

    Begin block 0xf5
    prev=[0x3f], succ=[0x525B0xf5]
    =================================
    0xf6: vf6(0xfd) = CONST 
    0xf9: vf9(0x525) = CONST 
    0xfc: JUMP vf9(0x525), vf6(0xfd)

    Begin block 0x525B0xf5
    prev=[0xf5], succ=[0xfd]
    =================================
    0x526S0xf5: JUMP vf6(0xfd)

    Begin block 0xfd
    prev=[0x525B0xf5], succ=[0x284B0xfd]
    =================================
    0xfe: vfe(0x546) = CONST 
    0x101: v101(0x108) = CONST 
    0x104: v104(0x284) = CONST 
    0x107: JUMP v104(0x284)

    Begin block 0x284B0xfd
    prev=[0xfd], succ=[0x108]
    =================================
    0x285S0xfd: v285Vfd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2a6S0xfd: v2a6Vfd = SLOAD v285Vfd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2a8S0xfd: JUMP v101(0x108)

    Begin block 0x108
    prev=[0x284B0xfd], succ=[0x2a9]
    =================================
    0x109: v109(0x2a9) = CONST 
    0x10c: JUMP v109(0x2a9)

    Begin block 0x2a9
    prev=[0x108], succ=[0x2c4, 0x2c8]
    =================================
    0x2aa: v2aa = CALLDATASIZE 
    0x2ab: v2ab(0x0) = CONST 
    0x2ae: CALLDATACOPY v2ab(0x0), v2ab(0x0), v2aa
    0x2af: v2af(0x0) = CONST 
    0x2b2: v2b2 = CALLDATASIZE 
    0x2b3: v2b3(0x0) = CONST 
    0x2b6: v2b6 = GAS 
    0x2b7: v2b7 = DELEGATECALL v2b6, v2a6Vfd, v2b3(0x0), v2b2, v2af(0x0), v2af(0x0)
    0x2b8: v2b8 = RETURNDATASIZE 
    0x2b9: v2b9(0x0) = CONST 
    0x2bc: RETURNDATACOPY v2b9(0x0), v2b9(0x0), v2b8
    0x2bf: v2bf = ISZERO v2b7
    0x2c0: v2c0(0x2c8) = CONST 
    0x2c3: JUMPI v2c0(0x2c8), v2bf

    Begin block 0x2c4
    prev=[0x2a9], succ=[]
    =================================
    0x2c4: v2c4 = RETURNDATASIZE 
    0x2c5: v2c5(0x0) = CONST 
    0x2c7: RETURN v2c5(0x0), v2c4

    Begin block 0x2c8
    prev=[0x2a9], succ=[]
    =================================
    0x2c9: v2c9 = RETURNDATASIZE 
    0x2ca: v2ca(0x0) = CONST 
    0x2cc: REVERT v2ca(0x0), v2c9

}

function getAudiusProxyAdminAddress()() public {
    Begin block 0x49
    prev=[], succ=[0x51, 0x55]
    =================================
    0x4a: v4a = CALLVALUE 
    0x4c: v4c = ISZERO v4a
    0x4d: v4d(0x55) = CONST 
    0x50: JUMPI v4d(0x55), v4c

    Begin block 0x51
    prev=[0x49], succ=[]
    =================================
    0x51: v51(0x0) = CONST 
    0x54: REVERT v51(0x0), v51(0x0)

    Begin block 0x55
    prev=[0x49], succ=[0x10f]
    =================================
    0x57: v57(0x46d) = CONST 
    0x5a: v5a(0x10f) = CONST 
    0x5d: JUMP v5a(0x10f)

    Begin block 0x10f
    prev=[0x55], succ=[0x46d]
    =================================
    0x110: v110(0x0) = CONST 
    0x112: v112 = SLOAD v110(0x0)
    0x113: v113(0x1) = CONST 
    0x115: v115(0x1) = CONST 
    0x117: v117(0xa0) = CONST 
    0x119: v119(0x10000000000000000000000000000000000000000) = SHL v117(0xa0), v115(0x1)
    0x11a: v11a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v119(0x10000000000000000000000000000000000000000), v113(0x1)
    0x11b: v11b = AND v11a(0xffffffffffffffffffffffffffffffffffffffff), v112
    0x11d: JUMP v57(0x46d)

    Begin block 0x46d
    prev=[0x10f], succ=[]
    =================================
    0x46e: v46e(0x40) = CONST 
    0x471: v471 = MLOAD v46e(0x40)
    0x472: v472(0x1) = CONST 
    0x474: v474(0x1) = CONST 
    0x476: v476(0xa0) = CONST 
    0x478: v478(0x10000000000000000000000000000000000000000) = SHL v476(0xa0), v474(0x1)
    0x479: v479(0xffffffffffffffffffffffffffffffffffffffff) = SUB v478(0x10000000000000000000000000000000000000000), v472(0x1)
    0x47c: v47c = AND v11b, v479(0xffffffffffffffffffffffffffffffffffffffff)
    0x47e: MSTORE v471, v47c
    0x47f: v47f = MLOAD v46e(0x40)
    0x483: v483(0x0) = SUB v471, v47f
    0x484: v484(0x20) = CONST 
    0x486: v486(0x20) = ADD v484(0x20), v483(0x0)
    0x488: RETURN v47f, v486(0x20)

}

function upgradeTo(address)() public {
    Begin block 0x7a
    prev=[], succ=[0x82, 0x86]
    =================================
    0x7b: v7b = CALLVALUE 
    0x7d: v7d = ISZERO v7b
    0x7e: v7e(0x86) = CONST 
    0x81: JUMPI v7e(0x86), v7d

    Begin block 0x82
    prev=[0x7a], succ=[]
    =================================
    0x82: v82(0x0) = CONST 
    0x85: REVERT v82(0x0), v82(0x0)

    Begin block 0x86
    prev=[0x7a], succ=[0x99, 0x9d]
    =================================
    0x88: v88(0x4a8) = CONST 
    0x8b: v8b(0x4) = CONST 
    0x8e: v8e = CALLDATASIZE 
    0x8f: v8f = SUB v8e, v8b(0x4)
    0x90: v90(0x20) = CONST 
    0x93: v93 = LT v8f, v90(0x20)
    0x94: v94 = ISZERO v93
    0x95: v95(0x9d) = CONST 
    0x98: JUMPI v95(0x9d), v94

    Begin block 0x99
    prev=[0x86], succ=[]
    =================================
    0x99: v99(0x0) = CONST 
    0x9c: REVERT v99(0x0), v99(0x0)

    Begin block 0x9d
    prev=[0x86], succ=[0x11e]
    =================================
    0x9f: v9f = CALLDATALOAD v8b(0x4)
    0xa0: va0(0x1) = CONST 
    0xa2: va2(0x1) = CONST 
    0xa4: va4(0xa0) = CONST 
    0xa6: va6(0x10000000000000000000000000000000000000000) = SHL va4(0xa0), va2(0x1)
    0xa7: va7(0xffffffffffffffffffffffffffffffffffffffff) = SUB va6(0x10000000000000000000000000000000000000000), va0(0x1)
    0xa8: va8 = AND va7(0xffffffffffffffffffffffffffffffffffffffff), v9f
    0xa9: va9(0x11e) = CONST 
    0xac: JUMP va9(0x11e)

    Begin block 0x11e
    prev=[0x9d], succ=[0x14d, 0x1d0]
    =================================
    0x11f: v11f(0x0) = CONST 
    0x121: v121 = SLOAD v11f(0x0)
    0x122: v122(0x40) = CONST 
    0x125: v125 = MLOAD v122(0x40)
    0x126: v126(0x80) = CONST 
    0x129: v129 = ADD v125, v126(0x80)
    0x12c: MSTORE v122(0x40), v129
    0x12d: v12d(0x42) = CONST 
    0x131: MSTORE v125, v12d(0x42)
    0x132: v132(0x1) = CONST 
    0x134: v134(0x1) = CONST 
    0x136: v136(0xa0) = CONST 
    0x138: v138(0x10000000000000000000000000000000000000000) = SHL v136(0xa0), v134(0x1)
    0x139: v139(0xffffffffffffffffffffffffffffffffffffffff) = SUB v138(0x10000000000000000000000000000000000000000), v132(0x1)
    0x13c: v13c = AND v121, v139(0xffffffffffffffffffffffffffffffffffffffff)
    0x13d: v13d = CALLER 
    0x13e: v13e = EQ v13d, v13c
    0x140: v140(0x3b7) = CONST 
    0x143: v143(0x20) = CONST 
    0x146: v146 = ADD v125, v143(0x20)
    0x147: CODECOPY v146, v140(0x3b7), v12d(0x42)
    0x149: v149(0x1d0) = CONST 
    0x14c: JUMPI v149(0x1d0), v13e

    Begin block 0x14d
    prev=[0x11e], succ=[0x17d0x7a]
    =================================
    0x14d: v14d(0x40) = CONST 
    0x14f: v14f = MLOAD v14d(0x40)
    0x150: v150(0x461bcd) = CONST 
    0x154: v154(0xe5) = CONST 
    0x156: v156(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v154(0xe5), v150(0x461bcd)
    0x158: MSTORE v14f, v156(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x159: v159(0x4) = CONST 
    0x15b: v15b = ADD v159(0x4), v14f
    0x15e: v15e(0x20) = CONST 
    0x160: v160 = ADD v15e(0x20), v15b
    0x163: v163(0x20) = SUB v160, v15b
    0x165: MSTORE v15b, v163(0x20)
    0x169: v169(0x42) = MLOAD v125
    0x16b: MSTORE v160, v169(0x42)
    0x16c: v16c(0x20) = CONST 
    0x16e: v16e = ADD v16c(0x20), v160
    0x172: v172(0x42) = MLOAD v125
    0x174: v174(0x20) = CONST 
    0x176: v176 = ADD v174(0x20), v125
    0x17b: v17b(0x0) = CONST 

    Begin block 0x17d0x7a
    prev=[0x14d, 0x1860x7a], succ=[0x1950x7a, 0x1860x7a]
    =================================
    0x17d0x7a_0x0: v17d7a_0 = PHI v17b(0x0), v7a190
    0x1800x7a: v7a180 = LT v17d7a_0, v172(0x42)
    0x1810x7a: v7a181 = ISZERO v7a180
    0x1820x7a: v7a182(0x195) = CONST 
    0x1850x7a: JUMPI v7a182(0x195), v7a181

    Begin block 0x1950x7a
    prev=[0x17d0x7a], succ=[0x1c20x7a, 0x1a90x7a]
    =================================
    0x19e0x7a: v7a19e = ADD v172(0x42), v16e
    0x1a00x7a: v7a1a0(0x1f) = CONST 
    0x1a20x7a: v7a1a2(0x2) = AND v7a1a0(0x1f), v172(0x42)
    0x1a40x7a: v7a1a4 = ISZERO v7a1a2(0x2)
    0x1a50x7a: v7a1a5(0x1c2) = CONST 
    0x1a80x7a: JUMPI v7a1a5(0x1c2), v7a1a4

    Begin block 0x1c20x7a
    prev=[0x1950x7a, 0x1a90x7a], succ=[]
    =================================
    0x1c20x7a_0x1: v1c27a_1 = PHI v7a1bf, v7a19e
    0x1c80x7a: v7a1c8(0x40) = CONST 
    0x1ca0x7a: v7a1ca = MLOAD v7a1c8(0x40)
    0x1cd0x7a: v7a1cd = SUB v1c27a_1, v7a1ca
    0x1cf0x7a: REVERT v7a1ca, v7a1cd

    Begin block 0x1a90x7a
    prev=[0x1950x7a], succ=[0x1c20x7a]
    =================================
    0x1ab0x7a: v7a1ab = SUB v7a19e, v7a1a2(0x2)
    0x1ad0x7a: v7a1ad = MLOAD v7a1ab
    0x1ae0x7a: v7a1ae(0x1) = CONST 
    0x1b10x7a: v7a1b1(0x20) = CONST 
    0x1b30x7a: v7a1b3(0x1e) = SUB v7a1b1(0x20), v7a1a2(0x2)
    0x1b40x7a: v7a1b4(0x100) = CONST 
    0x1b70x7a: v7a1b7(0x1000000000000000000000000000000000000000000000000000000000000) = EXP v7a1b4(0x100), v7a1b3(0x1e)
    0x1b80x7a: v7a1b8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v7a1b7(0x1000000000000000000000000000000000000000000000000000000000000), v7a1ae(0x1)
    0x1b90x7a: v7a1b9 = NOT v7a1b8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1ba0x7a: v7a1ba = AND v7a1b9, v7a1ad
    0x1bc0x7a: MSTORE v7a1ab, v7a1ba
    0x1bd0x7a: v7a1bd(0x20) = CONST 
    0x1bf0x7a: v7a1bf = ADD v7a1bd(0x20), v7a1ab

    Begin block 0x1860x7a
    prev=[0x17d0x7a], succ=[0x17d0x7a]
    =================================
    0x1860x7a_0x0: v1867a_0 = PHI v17b(0x0), v7a190
    0x1880x7a: v7a188 = ADD v1867a_0, v176
    0x1890x7a: v7a189 = MLOAD v7a188
    0x18c0x7a: v7a18c = ADD v1867a_0, v16e
    0x18d0x7a: MSTORE v7a18c, v7a189
    0x18e0x7a: v7a18e(0x20) = CONST 
    0x1900x7a: v7a190 = ADD v7a18e(0x20), v1867a_0
    0x1910x7a: v7a191(0x17d) = CONST 
    0x1940x7a: JUMP v7a191(0x17d)

    Begin block 0x1d0
    prev=[0x11e], succ=[0x2cd]
    =================================
    0x1d2: v1d2(0x1da) = CONST 
    0x1d6: v1d6(0x2cd) = CONST 
    0x1d9: JUMP v1d6(0x2cd)

    Begin block 0x2cd
    prev=[0x1d0], succ=[0x30d]
    =================================
    0x2ce: v2ce(0x2d6) = CONST 
    0x2d2: v2d2(0x30d) = CONST 
    0x2d5: JUMP v2d2(0x30d)

    Begin block 0x30d
    prev=[0x2cd], succ=[0x375]
    =================================
    0x30e: v30e(0x316) = CONST 
    0x312: v312(0x375) = CONST 
    0x315: JUMP v312(0x375)

    Begin block 0x375
    prev=[0x30d], succ=[0x316]
    =================================
    0x376: v376 = EXTCODESIZE va8
    0x377: v377 = ISZERO v376
    0x378: v378 = ISZERO v377
    0x37a: JUMP v30e(0x316)

    Begin block 0x316
    prev=[0x375], succ=[0x31b, 0x351]
    =================================
    0x317: v317(0x351) = CONST 
    0x31a: JUMPI v317(0x351), v378

    Begin block 0x31b
    prev=[0x316], succ=[]
    =================================
    0x31b: v31b(0x40) = CONST 
    0x31d: v31d = MLOAD v31b(0x40)
    0x31e: v31e(0x461bcd) = CONST 
    0x322: v322(0xe5) = CONST 
    0x324: v324(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v322(0xe5), v31e(0x461bcd)
    0x326: MSTORE v31d, v324(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x327: v327(0x4) = CONST 
    0x329: v329 = ADD v327(0x4), v31d
    0x32c: v32c(0x20) = CONST 
    0x32e: v32e = ADD v32c(0x20), v329
    0x331: v331(0x20) = SUB v32e, v329
    0x333: MSTORE v329, v331(0x20)
    0x334: v334(0x3b) = CONST 
    0x337: MSTORE v32e, v334(0x3b)
    0x338: v338(0x20) = CONST 
    0x33a: v33a = ADD v338(0x20), v32e
    0x33c: v33c(0x37c) = CONST 
    0x33f: v33f(0x3b) = CONST 
    0x342: CODECOPY v33a, v33c(0x37c), v33f(0x3b)
    0x343: v343(0x40) = CONST 
    0x345: v345 = ADD v343(0x40), v33a
    0x349: v349(0x40) = CONST 
    0x34b: v34b = MLOAD v349(0x40)
    0x34e: v34e(0x84) = SUB v345, v34b
    0x350: REVERT v34b, v34e(0x84)

    Begin block 0x351
    prev=[0x316], succ=[0x2d6]
    =================================
    0x352: v352(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x373: SSTORE v352(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), va8
    0x374: JUMP v2ce(0x2d6)

    Begin block 0x2d6
    prev=[0x351], succ=[0x1da]
    =================================
    0x2d7: v2d7(0x40) = CONST 
    0x2d9: v2d9 = MLOAD v2d7(0x40)
    0x2da: v2da(0x1) = CONST 
    0x2dc: v2dc(0x1) = CONST 
    0x2de: v2de(0xa0) = CONST 
    0x2e0: v2e0(0x10000000000000000000000000000000000000000) = SHL v2de(0xa0), v2dc(0x1)
    0x2e1: v2e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e0(0x10000000000000000000000000000000000000000), v2da(0x1)
    0x2e3: v2e3 = AND va8, v2e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e5: v2e5(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x307: v307(0x0) = CONST 
    0x30a: LOG2 v2d9, v307(0x0), v2e5(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v2e3
    0x30c: JUMP v1d2(0x1da)

    Begin block 0x1da
    prev=[0x2d6], succ=[0x4a8]
    =================================
    0x1dc: JUMP v88(0x4a8)

    Begin block 0x4a8
    prev=[0x1da], succ=[]
    =================================
    0x4a9: STOP 

}

function implementation()() public {
    Begin block 0xad
    prev=[], succ=[0xb5, 0xb9]
    =================================
    0xae: vae = CALLVALUE 
    0xb0: vb0 = ISZERO vae
    0xb1: vb1(0xb9) = CONST 
    0xb4: JUMPI vb1(0xb9), vb0

    Begin block 0xb5
    prev=[0xad], succ=[]
    =================================
    0xb5: vb5(0x0) = CONST 
    0xb8: REVERT vb5(0x0), vb5(0x0)

    Begin block 0xb9
    prev=[0xad], succ=[0x1ddB0xb9]
    =================================
    0xbb: vbb(0x4c9) = CONST 
    0xbe: vbe(0x1dd) = CONST 
    0xc1: JUMP vbe(0x1dd)

    Begin block 0x1ddB0xb9
    prev=[0xb9], succ=[0x284B0x1ddB0xb9]
    =================================
    0x1deS0xb9: v1deVb9(0x0) = CONST 
    0x1e0S0xb9: v1e0Vb9(0x1e7) = CONST 
    0x1e3S0xb9: v1e3Vb9(0x284) = CONST 
    0x1e6S0xb9: JUMP v1e3Vb9(0x284)

    Begin block 0x284B0x1ddB0xb9
    prev=[0x1ddB0xb9], succ=[0x1e7B0xb9]
    =================================
    0x285S0x1ddS0xb9: v285V1ddVb9(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2a6S0x1ddS0xb9: v2a6V1ddVb9 = SLOAD v285V1ddVb9(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2a8S0x1ddS0xb9: JUMP v1e0Vb9(0x1e7)

    Begin block 0x1e7B0xb9
    prev=[0x284B0x1ddB0xb9], succ=[0x4c9]
    =================================
    0x1ebS0xb9: JUMP vbb(0x4c9)

    Begin block 0x4c9
    prev=[0x1e7B0xb9], succ=[]
    =================================
    0x4ca: v4ca(0x40) = CONST 
    0x4cd: v4cd = MLOAD v4ca(0x40)
    0x4ce: v4ce(0x1) = CONST 
    0x4d0: v4d0(0x1) = CONST 
    0x4d2: v4d2(0xa0) = CONST 
    0x4d4: v4d4(0x10000000000000000000000000000000000000000) = SHL v4d2(0xa0), v4d0(0x1)
    0x4d5: v4d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d4(0x10000000000000000000000000000000000000000), v4ce(0x1)
    0x4d8: v4d8 = AND v2a6V1ddVb9, v4d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x4da: MSTORE v4cd, v4d8
    0x4db: v4db = MLOAD v4ca(0x40)
    0x4df: v4df(0x0) = SUB v4cd, v4db
    0x4e0: v4e0(0x20) = CONST 
    0x4e2: v4e2(0x20) = ADD v4e0(0x20), v4df(0x0)
    0x4e4: RETURN v4db, v4e2(0x20)

}

function setAudiusProxyAdminAddress(address)() public {
    Begin block 0xc2
    prev=[], succ=[0xca, 0xce]
    =================================
    0xc3: vc3 = CALLVALUE 
    0xc5: vc5 = ISZERO vc3
    0xc6: vc6(0xce) = CONST 
    0xc9: JUMPI vc6(0xce), vc5

    Begin block 0xca
    prev=[0xc2], succ=[]
    =================================
    0xca: vca(0x0) = CONST 
    0xcd: REVERT vca(0x0), vca(0x0)

    Begin block 0xce
    prev=[0xc2], succ=[0xe1, 0xe5]
    =================================
    0xd0: vd0(0x504) = CONST 
    0xd3: vd3(0x4) = CONST 
    0xd6: vd6 = CALLDATASIZE 
    0xd7: vd7 = SUB vd6, vd3(0x4)
    0xd8: vd8(0x20) = CONST 
    0xdb: vdb = LT vd7, vd8(0x20)
    0xdc: vdc = ISZERO vdb
    0xdd: vdd(0xe5) = CONST 
    0xe0: JUMPI vdd(0xe5), vdc

    Begin block 0xe1
    prev=[0xce], succ=[]
    =================================
    0xe1: ve1(0x0) = CONST 
    0xe4: REVERT ve1(0x0), ve1(0x0)

    Begin block 0xe5
    prev=[0xce], succ=[0x1ec]
    =================================
    0xe7: ve7 = CALLDATALOAD vd3(0x4)
    0xe8: ve8(0x1) = CONST 
    0xea: vea(0x1) = CONST 
    0xec: vec(0xa0) = CONST 
    0xee: vee(0x10000000000000000000000000000000000000000) = SHL vec(0xa0), vea(0x1)
    0xef: vef(0xffffffffffffffffffffffffffffffffffffffff) = SUB vee(0x10000000000000000000000000000000000000000), ve8(0x1)
    0xf0: vf0 = AND vef(0xffffffffffffffffffffffffffffffffffffffff), ve7
    0xf1: vf1(0x1ec) = CONST 
    0xf4: JUMP vf1(0x1ec)

    Begin block 0x1ec
    prev=[0xe5], succ=[0x21b, 0x261]
    =================================
    0x1ed: v1ed(0x0) = CONST 
    0x1ef: v1ef = SLOAD v1ed(0x0)
    0x1f0: v1f0(0x40) = CONST 
    0x1f3: v1f3 = MLOAD v1f0(0x40)
    0x1f4: v1f4(0x80) = CONST 
    0x1f7: v1f7 = ADD v1f3, v1f4(0x80)
    0x1fa: MSTORE v1f0(0x40), v1f7
    0x1fb: v1fb(0x42) = CONST 
    0x1ff: MSTORE v1f3, v1fb(0x42)
    0x200: v200(0x1) = CONST 
    0x202: v202(0x1) = CONST 
    0x204: v204(0xa0) = CONST 
    0x206: v206(0x10000000000000000000000000000000000000000) = SHL v204(0xa0), v202(0x1)
    0x207: v207(0xffffffffffffffffffffffffffffffffffffffff) = SUB v206(0x10000000000000000000000000000000000000000), v200(0x1)
    0x20a: v20a = AND v1ef, v207(0xffffffffffffffffffffffffffffffffffffffff)
    0x20b: v20b = CALLER 
    0x20c: v20c = EQ v20b, v20a
    0x20e: v20e(0x3b7) = CONST 
    0x211: v211(0x20) = CONST 
    0x214: v214 = ADD v1f3, v211(0x20)
    0x215: CODECOPY v214, v20e(0x3b7), v1fb(0x42)
    0x217: v217(0x261) = CONST 
    0x21a: JUMPI v217(0x261), v20c

    Begin block 0x21b
    prev=[0x1ec], succ=[0x252, 0x1950xc2]
    =================================
    0x21b: v21b(0x40) = CONST 
    0x21d: v21d = MLOAD v21b(0x40)
    0x21e: v21e(0x461bcd) = CONST 
    0x222: v222(0xe5) = CONST 
    0x224: v224(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v222(0xe5), v21e(0x461bcd)
    0x226: MSTORE v21d, v224(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x227: v227(0x20) = CONST 
    0x229: v229(0x4) = CONST 
    0x22c: v22c = ADD v21d, v229(0x4)
    0x22f: MSTORE v22c, v227(0x20)
    0x231: v231(0x42) = MLOAD v1f3
    0x232: v232(0x24) = CONST 
    0x235: v235 = ADD v21d, v232(0x24)
    0x236: MSTORE v235, v231(0x42)
    0x238: v238(0x42) = MLOAD v1f3
    0x23d: v23d(0x44) = CONST 
    0x241: v241 = ADD v21d, v23d(0x44)
    0x245: v245 = ADD v1f3, v227(0x20)
    0x24a: v24a(0x0) = CONST 
    0x24d: v24d = ISZERO v238(0x42)
    0x24e: v24e(0x195) = CONST 
    0x251: JUMPI v24e(0x195), v24d

    Begin block 0x252
    prev=[0x21b], succ=[0x17d0xc2]
    =================================
    0x254: v254 = ADD v24a(0x0), v245
    0x255: v255 = MLOAD v254
    0x258: v258 = ADD v24a(0x0), v241
    0x259: MSTORE v258, v255
    0x25a: v25a(0x20) = CONST 
    0x25c: v25c(0x20) = ADD v25a(0x20), v24a(0x0)
    0x25d: v25d(0x17d) = CONST 
    0x260: JUMP v25d(0x17d)

    Begin block 0x17d0xc2
    prev=[0x252, 0x1860xc2], succ=[0x1950xc2, 0x1860xc2]
    =================================
    0x17d0xc2_0x0: v17dc2_0 = PHI v25c(0x20), vc2190
    0x1800xc2: vc2180 = LT v17dc2_0, v238(0x42)
    0x1810xc2: vc2181 = ISZERO vc2180
    0x1820xc2: vc2182(0x195) = CONST 
    0x1850xc2: JUMPI vc2182(0x195), vc2181

    Begin block 0x1950xc2
    prev=[0x21b, 0x17d0xc2], succ=[0x1c20xc2, 0x1a90xc2]
    =================================
    0x19e0xc2: vc219e = ADD v238(0x42), v241
    0x1a00xc2: vc21a0(0x1f) = CONST 
    0x1a20xc2: vc21a2(0x2) = AND vc21a0(0x1f), v238(0x42)
    0x1a40xc2: vc21a4 = ISZERO vc21a2(0x2)
    0x1a50xc2: vc21a5(0x1c2) = CONST 
    0x1a80xc2: JUMPI vc21a5(0x1c2), vc21a4

    Begin block 0x1c20xc2
    prev=[0x1950xc2, 0x1a90xc2], succ=[]
    =================================
    0x1c20xc2_0x1: v1c2c2_1 = PHI vc21bf, vc219e
    0x1c80xc2: vc21c8(0x40) = CONST 
    0x1ca0xc2: vc21ca = MLOAD vc21c8(0x40)
    0x1cd0xc2: vc21cd = SUB v1c2c2_1, vc21ca
    0x1cf0xc2: REVERT vc21ca, vc21cd

    Begin block 0x1a90xc2
    prev=[0x1950xc2], succ=[0x1c20xc2]
    =================================
    0x1ab0xc2: vc21ab = SUB vc219e, vc21a2(0x2)
    0x1ad0xc2: vc21ad = MLOAD vc21ab
    0x1ae0xc2: vc21ae(0x1) = CONST 
    0x1b10xc2: vc21b1(0x20) = CONST 
    0x1b30xc2: vc21b3(0x1e) = SUB vc21b1(0x20), vc21a2(0x2)
    0x1b40xc2: vc21b4(0x100) = CONST 
    0x1b70xc2: vc21b7(0x1000000000000000000000000000000000000000000000000000000000000) = EXP vc21b4(0x100), vc21b3(0x1e)
    0x1b80xc2: vc21b8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vc21b7(0x1000000000000000000000000000000000000000000000000000000000000), vc21ae(0x1)
    0x1b90xc2: vc21b9 = NOT vc21b8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1ba0xc2: vc21ba = AND vc21b9, vc21ad
    0x1bc0xc2: MSTORE vc21ab, vc21ba
    0x1bd0xc2: vc21bd(0x20) = CONST 
    0x1bf0xc2: vc21bf = ADD vc21bd(0x20), vc21ab

    Begin block 0x1860xc2
    prev=[0x17d0xc2], succ=[0x17d0xc2]
    =================================
    0x1860xc2_0x0: v186c2_0 = PHI v25c(0x20), vc2190
    0x1880xc2: vc2188 = ADD v186c2_0, v245
    0x1890xc2: vc2189 = MLOAD vc2188
    0x18c0xc2: vc218c = ADD v186c2_0, v241
    0x18d0xc2: MSTORE vc218c, vc2189
    0x18e0xc2: vc218e(0x20) = CONST 
    0x1900xc2: vc2190 = ADD vc218e(0x20), v186c2_0
    0x1910xc2: vc2191(0x17d) = CONST 
    0x1940xc2: JUMP vc2191(0x17d)

    Begin block 0x261
    prev=[0x1ec], succ=[0x504]
    =================================
    0x263: v263(0x0) = CONST 
    0x266: v266 = SLOAD v263(0x0)
    0x267: v267(0x1) = CONST 
    0x269: v269(0x1) = CONST 
    0x26b: v26b(0xa0) = CONST 
    0x26d: v26d(0x10000000000000000000000000000000000000000) = SHL v26b(0xa0), v269(0x1)
    0x26e: v26e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26d(0x10000000000000000000000000000000000000000), v267(0x1)
    0x26f: v26f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v26e(0xffffffffffffffffffffffffffffffffffffffff)
    0x270: v270 = AND v26f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v266
    0x271: v271(0x1) = CONST 
    0x273: v273(0x1) = CONST 
    0x275: v275(0xa0) = CONST 
    0x277: v277(0x10000000000000000000000000000000000000000) = SHL v275(0xa0), v273(0x1)
    0x278: v278(0xffffffffffffffffffffffffffffffffffffffff) = SUB v277(0x10000000000000000000000000000000000000000), v271(0x1)
    0x27c: v27c = AND v278(0xffffffffffffffffffffffffffffffffffffffff), vf0
    0x280: v280 = OR v27c, v270
    0x282: SSTORE v263(0x0), v280
    0x283: JUMP vd0(0x504)

    Begin block 0x504
    prev=[0x261], succ=[]
    =================================
    0x505: STOP 

}

