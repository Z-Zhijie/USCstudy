function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xb59]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xb3b: vb3b(0xb59) = CONST 
    0xb3c: JUMPI vb3b(0xb59), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0xb5c]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x13af4035) = CONST 
    0x3b: v3b = EQ v34, v35(0x13af4035)
    0xb3d: vb3d(0xb5c) = CONST 
    0xb3e: JUMPI vb3d(0xb5c), v3b

    Begin block 0x40
    prev=[0xd], succ=[0xb5f, 0x4b]
    =================================
    0x41: v41(0x23aa7e12) = CONST 
    0x46: v46 = EQ v41(0x23aa7e12), v34
    0xb3f: vb3f(0xb5f) = CONST 
    0xb40: JUMPI vb3f(0xb5f), v46

    Begin block 0xb5f
    prev=[0x40], succ=[]
    =================================
    0xb60: vb60(0x154) = CONST 
    0xb61: CALLPRIVATE vb60(0x154)

    Begin block 0x4b
    prev=[0x40], succ=[0xb62, 0x56]
    =================================
    0x4c: v4c(0x3b22f35f) = CONST 
    0x51: v51 = EQ v4c(0x3b22f35f), v34
    0xb41: vb41(0xb62) = CONST 
    0xb42: JUMPI vb41(0xb62), v51

    Begin block 0xb62
    prev=[0x4b], succ=[]
    =================================
    0xb63: vb63(0x185) = CONST 
    0xb64: CALLPRIVATE vb63(0x185)

    Begin block 0x56
    prev=[0x4b], succ=[0xb65, 0x61]
    =================================
    0x57: v57(0x8063ab78) = CONST 
    0x5c: v5c = EQ v57(0x8063ab78), v34
    0xb43: vb43(0xb65) = CONST 
    0xb44: JUMPI vb43(0xb65), v5c

    Begin block 0xb65
    prev=[0x56], succ=[]
    =================================
    0xb66: vb66(0x1af) = CONST 
    0xb67: CALLPRIVATE vb66(0x1af)

    Begin block 0x61
    prev=[0x56], succ=[0xb68, 0x6c]
    =================================
    0x62: v62(0x806ad57e) = CONST 
    0x67: v67 = EQ v62(0x806ad57e), v34
    0xb45: vb45(0xb68) = CONST 
    0xb46: JUMPI vb45(0xb68), v67

    Begin block 0xb68
    prev=[0x61], succ=[]
    =================================
    0xb69: vb69(0x1d0) = CONST 
    0xb6a: CALLPRIVATE vb69(0x1d0)

    Begin block 0x6c
    prev=[0x61], succ=[0xb6b, 0x77]
    =================================
    0x6d: v6d(0x8da5cb5b) = CONST 
    0x72: v72 = EQ v6d(0x8da5cb5b), v34
    0xb47: vb47(0xb6b) = CONST 
    0xb48: JUMPI vb47(0xb6b), v72

    Begin block 0xb6b
    prev=[0x6c], succ=[]
    =================================
    0xb6c: vb6c(0x1f1) = CONST 
    0xb6d: CALLPRIVATE vb6c(0x1f1)

    Begin block 0x77
    prev=[0x6c], succ=[0xb6e, 0x82]
    =================================
    0x78: v78(0xaa156645) = CONST 
    0x7d: v7d = EQ v78(0xaa156645), v34
    0xb49: vb49(0xb6e) = CONST 
    0xb4a: JUMPI vb49(0xb6e), v7d

    Begin block 0xb6e
    prev=[0x77], succ=[]
    =================================
    0xb6f: vb6f(0x206) = CONST 
    0xb70: CALLPRIVATE vb6f(0x206)

    Begin block 0x82
    prev=[0x77], succ=[0xb71, 0x8d]
    =================================
    0x83: v83(0xbc7f3b50) = CONST 
    0x88: v88 = EQ v83(0xbc7f3b50), v34
    0xb4b: vb4b(0xb71) = CONST 
    0xb4c: JUMPI vb4b(0xb71), v88

    Begin block 0xb71
    prev=[0x82], succ=[]
    =================================
    0xb72: vb72(0x227) = CONST 
    0xb73: CALLPRIVATE vb72(0x227)

    Begin block 0x8d
    prev=[0x82], succ=[0xb74, 0x98]
    =================================
    0x8e: v8e(0xc4f987a5) = CONST 
    0x93: v93 = EQ v8e(0xc4f987a5), v34
    0xb4d: vb4d(0xb74) = CONST 
    0xb4e: JUMPI vb4d(0xb74), v93

    Begin block 0xb74
    prev=[0x8d], succ=[]
    =================================
    0xb75: vb75(0x23c) = CONST 
    0xb76: CALLPRIVATE vb75(0x23c)

    Begin block 0x98
    prev=[0x8d], succ=[0xb77, 0xa3]
    =================================
    0x99: v99(0xcb3eef2c) = CONST 
    0x9e: v9e = EQ v99(0xcb3eef2c), v34
    0xb4f: vb4f(0xb77) = CONST 
    0xb50: JUMPI vb4f(0xb77), v9e

    Begin block 0xb77
    prev=[0x98], succ=[]
    =================================
    0xb78: vb78(0x25d) = CONST 
    0xb79: CALLPRIVATE vb78(0x25d)

    Begin block 0xa3
    prev=[0x98], succ=[0xb7a, 0xae]
    =================================
    0xa4: va4(0xd264e05e) = CONST 
    0xa9: va9 = EQ va4(0xd264e05e), v34
    0xb51: vb51(0xb7a) = CONST 
    0xb52: JUMPI vb51(0xb7a), va9

    Begin block 0xb7a
    prev=[0xa3], succ=[]
    =================================
    0xb7b: vb7b(0x2c2) = CONST 
    0xb7c: CALLPRIVATE vb7b(0x2c2)

    Begin block 0xae
    prev=[0xa3], succ=[0xb7d, 0xb9]
    =================================
    0xaf: vaf(0xd273285b) = CONST 
    0xb4: vb4 = EQ vaf(0xd273285b), v34
    0xb53: vb53(0xb7d) = CONST 
    0xb54: JUMPI vb53(0xb7d), vb4

    Begin block 0xb7d
    prev=[0xae], succ=[]
    =================================
    0xb7e: vb7e(0x2d7) = CONST 
    0xb7f: CALLPRIVATE vb7e(0x2d7)

    Begin block 0xb9
    prev=[0xae], succ=[0xb80, 0xc4]
    =================================
    0xba: vba(0xfa34b345) = CONST 
    0xbf: vbf = EQ vba(0xfa34b345), v34
    0xb55: vb55(0xb80) = CONST 
    0xb56: JUMPI vb55(0xb80), vbf

    Begin block 0xb80
    prev=[0xb9], succ=[]
    =================================
    0xb81: vb81(0x2ec) = CONST 
    0xb82: CALLPRIVATE vb81(0x2ec)

    Begin block 0xc4
    prev=[0xb9], succ=[0xb59, 0xb83]
    =================================
    0xc5: vc5(0xffd85b68) = CONST 
    0xca: vca = EQ vc5(0xffd85b68), v34
    0xb57: vb57(0xb83) = CONST 
    0xb58: JUMPI vb57(0xb83), vca

    Begin block 0xb59
    prev=[0x0, 0xc4], succ=[]
    =================================
    0xb5a: vb5a(0xcf) = CONST 
    0xb5b: CALLPRIVATE vb5a(0xcf)

    Begin block 0xb83
    prev=[0xc4], succ=[]
    =================================
    0xb84: vb84(0x301) = CONST 
    0xb85: CALLPRIVATE vb84(0x301)

    Begin block 0xb5c
    prev=[0xd], succ=[]
    =================================
    0xb5d: vb5d(0x11f) = CONST 
    0xb5e: CALLPRIVATE vb5d(0x11f)

}

function setOwner(address)() public {
    Begin block 0x11f
    prev=[], succ=[0x127, 0x12b]
    =================================
    0x120: v120 = CALLVALUE 
    0x122: v122 = ISZERO v120
    0x123: v123(0x12b) = CONST 
    0x126: JUMPI v123(0x12b), v122

    Begin block 0x127
    prev=[0x11f], succ=[]
    =================================
    0x127: v127(0x0) = CONST 
    0x12a: REVERT v127(0x0), v127(0x0)

    Begin block 0x12b
    prev=[0x11f], succ=[0x34a]
    =================================
    0x12d: v12d(0x811) = CONST 
    0x130: v130(0x1) = CONST 
    0x132: v132(0xa0) = CONST 
    0x134: v134(0x2) = CONST 
    0x136: v136(0x10000000000000000000000000000000000000000) = EXP v134(0x2), v132(0xa0)
    0x137: v137(0xffffffffffffffffffffffffffffffffffffffff) = SUB v136(0x10000000000000000000000000000000000000000), v130(0x1)
    0x138: v138(0x4) = CONST 
    0x13a: v13a = CALLDATALOAD v138(0x4)
    0x13b: v13b = AND v13a, v137(0xffffffffffffffffffffffffffffffffffffffff)
    0x13c: v13c(0x34a) = CONST 
    0x13f: JUMP v13c(0x34a)

    Begin block 0x34a
    prev=[0x12b], succ=[0x364, 0x368]
    =================================
    0x34b: v34b(0x5) = CONST 
    0x34d: v34d = SLOAD v34b(0x5)
    0x34e: v34e(0x0) = CONST 
    0x351: v351 = CALLER 
    0x352: v352(0x1) = CONST 
    0x354: v354(0xa0) = CONST 
    0x356: v356(0x2) = CONST 
    0x358: v358(0x10000000000000000000000000000000000000000) = EXP v356(0x2), v354(0xa0)
    0x359: v359(0xffffffffffffffffffffffffffffffffffffffff) = SUB v358(0x10000000000000000000000000000000000000000), v352(0x1)
    0x35c: v35c = AND v359(0xffffffffffffffffffffffffffffffffffffffff), v351
    0x35e: v35e = AND v34d, v359(0xffffffffffffffffffffffffffffffffffffffff)
    0x35f: v35f = EQ v35e, v35c
    0x360: v360(0x368) = CONST 
    0x363: JUMPI v360(0x368), v35f

    Begin block 0x364
    prev=[0x34a], succ=[]
    =================================
    0x364: v364(0x0) = CONST 
    0x367: REVERT v364(0x0), v364(0x0)

    Begin block 0x368
    prev=[0x34a], succ=[0x379, 0x37d]
    =================================
    0x369: v369(0x1) = CONST 
    0x36b: v36b(0xa0) = CONST 
    0x36d: v36d(0x2) = CONST 
    0x36f: v36f(0x10000000000000000000000000000000000000000) = EXP v36d(0x2), v36b(0xa0)
    0x370: v370(0xffffffffffffffffffffffffffffffffffffffff) = SUB v36f(0x10000000000000000000000000000000000000000), v369(0x1)
    0x372: v372 = AND v13b, v370(0xffffffffffffffffffffffffffffffffffffffff)
    0x373: v373 = ISZERO v372
    0x374: v374 = ISZERO v373
    0x375: v375(0x37d) = CONST 
    0x378: JUMPI v375(0x37d), v374

    Begin block 0x379
    prev=[0x368], succ=[]
    =================================
    0x379: v379(0x0) = CONST 
    0x37c: REVERT v379(0x0), v379(0x0)

    Begin block 0x37d
    prev=[0x368], succ=[0x811]
    =================================
    0x37f: v37f(0x5) = CONST 
    0x382: v382 = SLOAD v37f(0x5)
    0x383: v383(0x1) = CONST 
    0x385: v385(0xa0) = CONST 
    0x387: v387(0x2) = CONST 
    0x389: v389(0x10000000000000000000000000000000000000000) = EXP v387(0x2), v385(0xa0)
    0x38a: v38a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v389(0x10000000000000000000000000000000000000000), v383(0x1)
    0x38c: v38c = AND v13b, v38a(0xffffffffffffffffffffffffffffffffffffffff)
    0x38d: v38d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a2: v3a2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v38d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a5: v3a5 = AND v382, v3a2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3a6: v3a6 = OR v3a5, v38c
    0x3a8: SSTORE v37f(0x5), v3a6
    0x3a9: v3a9(0x1) = CONST 
    0x3ae: JUMP v12d(0x811)

    Begin block 0x811
    prev=[0x37d], succ=[]
    =================================
    0x812: v812(0x40) = CONST 
    0x815: v815 = MLOAD v812(0x40)
    0x817: v817 = ISZERO v3a9(0x1)
    0x818: v818 = ISZERO v817
    0x81a: MSTORE v815, v818
    0x81b: v81b = MLOAD v812(0x40)
    0x81f: v81f(0x0) = SUB v815, v81b
    0x820: v820(0x20) = CONST 
    0x822: v822(0x20) = ADD v820(0x20), v81f(0x0)
    0x824: RETURN v81b, v822(0x20)

}

function controllerDelegate()() public {
    Begin block 0x154
    prev=[], succ=[0x15c, 0x160]
    =================================
    0x155: v155 = CALLVALUE 
    0x157: v157 = ISZERO v155
    0x158: v158(0x160) = CONST 
    0x15b: JUMPI v158(0x160), v157

    Begin block 0x15c
    prev=[0x154], succ=[]
    =================================
    0x15c: v15c(0x0) = CONST 
    0x15f: REVERT v15c(0x0), v15c(0x0)

    Begin block 0x160
    prev=[0x154], succ=[0x3af]
    =================================
    0x162: v162(0x844) = CONST 
    0x165: v165(0x3af) = CONST 
    0x168: JUMP v165(0x3af)

    Begin block 0x3af
    prev=[0x160], succ=[0x844]
    =================================
    0x3b0: v3b0(0x1) = CONST 
    0x3b2: v3b2 = SLOAD v3b0(0x1)
    0x3b3: v3b3(0x1) = CONST 
    0x3b5: v3b5(0xa0) = CONST 
    0x3b7: v3b7(0x2) = CONST 
    0x3b9: v3b9(0x10000000000000000000000000000000000000000) = EXP v3b7(0x2), v3b5(0xa0)
    0x3ba: v3ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b9(0x10000000000000000000000000000000000000000), v3b3(0x1)
    0x3bb: v3bb = AND v3ba(0xffffffffffffffffffffffffffffffffffffffff), v3b2
    0x3bd: JUMP v162(0x844)

    Begin block 0x844
    prev=[0x3af], succ=[]
    =================================
    0x845: v845(0x40) = CONST 
    0x848: v848 = MLOAD v845(0x40)
    0x849: v849(0x1) = CONST 
    0x84b: v84b(0xa0) = CONST 
    0x84d: v84d(0x2) = CONST 
    0x84f: v84f(0x10000000000000000000000000000000000000000) = EXP v84d(0x2), v84b(0xa0)
    0x850: v850(0xffffffffffffffffffffffffffffffffffffffff) = SUB v84f(0x10000000000000000000000000000000000000000), v849(0x1)
    0x853: v853 = AND v3bb, v850(0xffffffffffffffffffffffffffffffffffffffff)
    0x855: MSTORE v848, v853
    0x856: v856 = MLOAD v845(0x40)
    0x85a: v85a(0x0) = SUB v848, v856
    0x85b: v85b(0x20) = CONST 
    0x85d: v85d(0x20) = ADD v85b(0x20), v85a(0x0)
    0x85f: RETURN v856, v85d(0x20)

}

function gStorage(bytes32)() public {
    Begin block 0x185
    prev=[], succ=[0x18d, 0x191]
    =================================
    0x186: v186 = CALLVALUE 
    0x188: v188 = ISZERO v186
    0x189: v189(0x191) = CONST 
    0x18c: JUMPI v189(0x191), v188

    Begin block 0x18d
    prev=[0x185], succ=[]
    =================================
    0x18d: v18d(0x0) = CONST 
    0x190: REVERT v18d(0x0), v18d(0x0)

    Begin block 0x191
    prev=[0x185], succ=[0x3be]
    =================================
    0x193: v193(0x87f) = CONST 
    0x196: v196(0x4) = CONST 
    0x198: v198 = CALLDATALOAD v196(0x4)
    0x199: v199(0x3be) = CONST 
    0x19c: JUMP v199(0x3be)

    Begin block 0x3be
    prev=[0x191], succ=[0x87f]
    =================================
    0x3bf: v3bf(0x4) = CONST 
    0x3c1: v3c1(0x20) = CONST 
    0x3c3: MSTORE v3c1(0x20), v3bf(0x4)
    0x3c4: v3c4(0x0) = CONST 
    0x3c8: MSTORE v3c4(0x0), v198
    0x3c9: v3c9(0x40) = CONST 
    0x3cc: v3cc = SHA3 v3c4(0x0), v3c9(0x40)
    0x3cd: v3cd = SLOAD v3cc
    0x3cf: JUMP v193(0x87f)

    Begin block 0x87f
    prev=[0x3be], succ=[]
    =================================
    0x880: v880(0x40) = CONST 
    0x883: v883 = MLOAD v880(0x40)
    0x886: MSTORE v883, v3cd
    0x887: v887 = MLOAD v880(0x40)
    0x88b: v88b(0x0) = SUB v883, v887
    0x88c: v88c(0x20) = CONST 
    0x88e: v88e(0x20) = ADD v88c(0x20), v88b(0x0)
    0x890: RETURN v887, v88e(0x20)

}

function setWalletsDelegate(address)() public {
    Begin block 0x1af
    prev=[], succ=[0x1b7, 0x1bb]
    =================================
    0x1b0: v1b0 = CALLVALUE 
    0x1b2: v1b2 = ISZERO v1b0
    0x1b3: v1b3(0x1bb) = CONST 
    0x1b6: JUMPI v1b3(0x1bb), v1b2

    Begin block 0x1b7
    prev=[0x1af], succ=[]
    =================================
    0x1b7: v1b7(0x0) = CONST 
    0x1ba: REVERT v1b7(0x0), v1b7(0x0)

    Begin block 0x1bb
    prev=[0x1af], succ=[0x3d0]
    =================================
    0x1bd: v1bd(0x8b0) = CONST 
    0x1c0: v1c0(0x1) = CONST 
    0x1c2: v1c2(0xa0) = CONST 
    0x1c4: v1c4(0x2) = CONST 
    0x1c6: v1c6(0x10000000000000000000000000000000000000000) = EXP v1c4(0x2), v1c2(0xa0)
    0x1c7: v1c7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c6(0x10000000000000000000000000000000000000000), v1c0(0x1)
    0x1c8: v1c8(0x4) = CONST 
    0x1ca: v1ca = CALLDATALOAD v1c8(0x4)
    0x1cb: v1cb = AND v1ca, v1c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x1cc: v1cc(0x3d0) = CONST 
    0x1cf: JUMP v1cc(0x3d0)

    Begin block 0x3d0
    prev=[0x1bb], succ=[0x3ea, 0x3ee]
    =================================
    0x3d1: v3d1(0x5) = CONST 
    0x3d3: v3d3 = SLOAD v3d1(0x5)
    0x3d4: v3d4(0x0) = CONST 
    0x3d7: v3d7 = CALLER 
    0x3d8: v3d8(0x1) = CONST 
    0x3da: v3da(0xa0) = CONST 
    0x3dc: v3dc(0x2) = CONST 
    0x3de: v3de(0x10000000000000000000000000000000000000000) = EXP v3dc(0x2), v3da(0xa0)
    0x3df: v3df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3de(0x10000000000000000000000000000000000000000), v3d8(0x1)
    0x3e2: v3e2 = AND v3df(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0x3e4: v3e4 = AND v3d3, v3df(0xffffffffffffffffffffffffffffffffffffffff)
    0x3e5: v3e5 = EQ v3e4, v3e2
    0x3e6: v3e6(0x3ee) = CONST 
    0x3e9: JUMPI v3e6(0x3ee), v3e5

    Begin block 0x3ea
    prev=[0x3d0], succ=[]
    =================================
    0x3ea: v3ea(0x0) = CONST 
    0x3ed: REVERT v3ea(0x0), v3ea(0x0)

    Begin block 0x3ee
    prev=[0x3d0], succ=[0x8b0]
    =================================
    0x3f0: v3f0(0x0) = CONST 
    0x3f3: v3f3 = SLOAD v3f0(0x0)
    0x3f4: v3f4(0x1) = CONST 
    0x3f6: v3f6(0xa0) = CONST 
    0x3f8: v3f8(0x2) = CONST 
    0x3fa: v3fa(0x10000000000000000000000000000000000000000) = EXP v3f8(0x2), v3f6(0xa0)
    0x3fb: v3fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fa(0x10000000000000000000000000000000000000000), v3f4(0x1)
    0x3fd: v3fd = AND v1cb, v3fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fe: v3fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x413: v413(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x416: v416 = AND v3f3, v413(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x417: v417 = OR v416, v3fd
    0x419: SSTORE v3f0(0x0), v417
    0x41a: v41a(0x1) = CONST 
    0x41f: JUMP v1bd(0x8b0)

    Begin block 0x8b0
    prev=[0x3ee], succ=[]
    =================================
    0x8b1: v8b1(0x40) = CONST 
    0x8b4: v8b4 = MLOAD v8b1(0x40)
    0x8b6: v8b6 = ISZERO v41a(0x1)
    0x8b7: v8b7 = ISZERO v8b6
    0x8b9: MSTORE v8b4, v8b7
    0x8ba: v8ba = MLOAD v8b1(0x40)
    0x8be: v8be(0x0) = SUB v8b4, v8ba
    0x8bf: v8bf(0x20) = CONST 
    0x8c1: v8c1(0x20) = ADD v8bf(0x20), v8be(0x0)
    0x8c3: RETURN v8ba, v8c1(0x20)

}

function addWorker(address)() public {
    Begin block 0x1d0
    prev=[], succ=[0x1d8, 0x1dc]
    =================================
    0x1d1: v1d1 = CALLVALUE 
    0x1d3: v1d3 = ISZERO v1d1
    0x1d4: v1d4(0x1dc) = CONST 
    0x1d7: JUMPI v1d4(0x1dc), v1d3

    Begin block 0x1d8
    prev=[0x1d0], succ=[]
    =================================
    0x1d8: v1d8(0x0) = CONST 
    0x1db: REVERT v1d8(0x0), v1d8(0x0)

    Begin block 0x1dc
    prev=[0x1d0], succ=[0x420]
    =================================
    0x1de: v1de(0x8e3) = CONST 
    0x1e1: v1e1(0x1) = CONST 
    0x1e3: v1e3(0xa0) = CONST 
    0x1e5: v1e5(0x2) = CONST 
    0x1e7: v1e7(0x10000000000000000000000000000000000000000) = EXP v1e5(0x2), v1e3(0xa0)
    0x1e8: v1e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e7(0x10000000000000000000000000000000000000000), v1e1(0x1)
    0x1e9: v1e9(0x4) = CONST 
    0x1eb: v1eb = CALLDATALOAD v1e9(0x4)
    0x1ec: v1ec = AND v1eb, v1e8(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ed: v1ed(0x420) = CONST 
    0x1f0: JUMP v1ed(0x420)

    Begin block 0x420
    prev=[0x1dc], succ=[0x43c, 0x440]
    =================================
    0x421: v421(0x5) = CONST 
    0x423: v423 = SLOAD v421(0x5)
    0x424: v424(0x0) = CONST 
    0x429: v429 = CALLER 
    0x42a: v42a(0x1) = CONST 
    0x42c: v42c(0xa0) = CONST 
    0x42e: v42e(0x2) = CONST 
    0x430: v430(0x10000000000000000000000000000000000000000) = EXP v42e(0x2), v42c(0xa0)
    0x431: v431(0xffffffffffffffffffffffffffffffffffffffff) = SUB v430(0x10000000000000000000000000000000000000000), v42a(0x1)
    0x434: v434 = AND v431(0xffffffffffffffffffffffffffffffffffffffff), v429
    0x436: v436 = AND v423, v431(0xffffffffffffffffffffffffffffffffffffffff)
    0x437: v437 = EQ v436, v434
    0x438: v438(0x440) = CONST 
    0x43b: JUMPI v438(0x440), v437

    Begin block 0x43c
    prev=[0x420], succ=[]
    =================================
    0x43c: v43c(0x0) = CONST 
    0x43f: REVERT v43c(0x0), v43c(0x0)

    Begin block 0x440
    prev=[0x420], succ=[0x509B0x440]
    =================================
    0x441: v441(0x449) = CONST 
    0x445: v445(0x509) = CONST 
    0x448: JUMP v445(0x509)

    Begin block 0x509B0x440
    prev=[0x440], succ=[0x449]
    =================================
    0x50aS0x440: v50aV440(0x1) = CONST 
    0x50cS0x440: v50cV440(0xa0) = CONST 
    0x50eS0x440: v50eV440(0x2) = CONST 
    0x510S0x440: v510V440(0x10000000000000000000000000000000000000000) = EXP v50eV440(0x2), v50cV440(0xa0)
    0x511S0x440: v511V440(0xffffffffffffffffffffffffffffffffffffffff) = SUB v510V440(0x10000000000000000000000000000000000000000), v50aV440(0x1)
    0x512S0x440: v512V440 = AND v511V440(0xffffffffffffffffffffffffffffffffffffffff), v1ec
    0x513S0x440: v513V440(0x0) = CONST 
    0x517S0x440: MSTORE v513V440(0x0), v512V440
    0x518S0x440: v518V440(0x6) = CONST 
    0x51aS0x440: v51aV440(0x20) = CONST 
    0x51cS0x440: MSTORE v51aV440(0x20), v518V440(0x6)
    0x51dS0x440: v51dV440(0x40) = CONST 
    0x520S0x440: v520V440 = SHA3 v513V440(0x0), v51dV440(0x40)
    0x521S0x440: v521V440 = SLOAD v520V440
    0x522S0x440: v522V440 = ISZERO v521V440
    0x523S0x440: v523V440 = ISZERO v522V440
    0x525S0x440: JUMP v441(0x449)

    Begin block 0x449
    prev=[0x509B0x440], succ=[0x44f, 0x453]
    =================================
    0x44a: v44a = ISZERO v523V440
    0x44b: v44b(0x453) = CONST 
    0x44e: JUMPI v44b(0x453), v44a

    Begin block 0x44f
    prev=[0x449], succ=[]
    =================================
    0x44f: v44f(0x0) = CONST 
    0x452: REVERT v44f(0x0), v44f(0x0)

    Begin block 0x453
    prev=[0x449], succ=[0x8e3]
    =================================
    0x455: v455(0x7) = CONST 
    0x458: v458 = SLOAD v455(0x7)
    0x459: v459(0x1) = CONST 
    0x45c: v45c = ADD v458, v459(0x1)
    0x45f: SSTORE v455(0x7), v45c
    0x460: v460(0xa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c688) = CONST 
    0x482: v482 = ADD v458, v460(0xa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c688)
    0x484: v484 = SLOAD v482
    0x485: v485(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x49a: v49a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v485(0xffffffffffffffffffffffffffffffffffffffff)
    0x49b: v49b = AND v49a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v484
    0x49c: v49c(0x1) = CONST 
    0x49e: v49e(0xa0) = CONST 
    0x4a0: v4a0(0x2) = CONST 
    0x4a2: v4a2(0x10000000000000000000000000000000000000000) = EXP v4a0(0x2), v49e(0xa0)
    0x4a3: v4a3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a2(0x10000000000000000000000000000000000000000), v49c(0x1)
    0x4a5: v4a5 = AND v1ec, v4a3(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a8: v4a8 = OR v4a5, v49b
    0x4ab: SSTORE v482, v4a8
    0x4ac: v4ac(0x0) = CONST 
    0x4b0: MSTORE v4ac(0x0), v4a5
    0x4b1: v4b1(0x6) = CONST 
    0x4b3: v4b3(0x20) = CONST 
    0x4b7: MSTORE v4b3(0x20), v4b1(0x6)
    0x4b8: v4b8(0x40) = CONST 
    0x4bd: v4bd = SHA3 v4ac(0x0), v4b8(0x40)
    0x4c0: SSTORE v4bd, v458
    0x4c2: v4c2 = MLOAD v4b8(0x40)
    0x4c5: MSTORE v4c2, v4a5
    0x4c7: v4c7 = MLOAD v4b8(0x40)
    0x4c8: v4c8(0xdecaaccf65fa0157d575425d16efcccc089f3df91ee0abedec8d1def2f12ab39) = CONST 
    0x4ec: v4ec(0x0) = SUB v4c2, v4c7
    0x4ef: v4ef(0x20) = ADD v4b3(0x20), v4ec(0x0)
    0x4f1: LOG1 v4c7, v4ef(0x20), v4c8(0xdecaaccf65fa0157d575425d16efcccc089f3df91ee0abedec8d1def2f12ab39)
    0x4f3: v4f3(0x1) = CONST 
    0x4f9: JUMP v1de(0x8e3)

    Begin block 0x8e3
    prev=[0x453], succ=[]
    =================================
    0x8e4: v8e4(0x40) = CONST 
    0x8e7: v8e7 = MLOAD v8e4(0x40)
    0x8e9: v8e9 = ISZERO v4f3(0x1)
    0x8ea: v8ea = ISZERO v8e9
    0x8ec: MSTORE v8e7, v8ea
    0x8ed: v8ed = MLOAD v8e4(0x40)
    0x8f1: v8f1(0x0) = SUB v8e7, v8ed
    0x8f2: v8f2(0x20) = CONST 
    0x8f4: v8f4(0x20) = ADD v8f2(0x20), v8f1(0x0)
    0x8f6: RETURN v8ed, v8f4(0x20)

}

function owner()() public {
    Begin block 0x1f1
    prev=[], succ=[0x1f9, 0x1fd]
    =================================
    0x1f2: v1f2 = CALLVALUE 
    0x1f4: v1f4 = ISZERO v1f2
    0x1f5: v1f5(0x1fd) = CONST 
    0x1f8: JUMPI v1f5(0x1fd), v1f4

    Begin block 0x1f9
    prev=[0x1f1], succ=[]
    =================================
    0x1f9: v1f9(0x0) = CONST 
    0x1fc: REVERT v1f9(0x0), v1f9(0x0)

    Begin block 0x1fd
    prev=[0x1f1], succ=[0x4fa]
    =================================
    0x1ff: v1ff(0x916) = CONST 
    0x202: v202(0x4fa) = CONST 
    0x205: JUMP v202(0x4fa)

    Begin block 0x4fa
    prev=[0x1fd], succ=[0x916]
    =================================
    0x4fb: v4fb(0x5) = CONST 
    0x4fd: v4fd = SLOAD v4fb(0x5)
    0x4fe: v4fe(0x1) = CONST 
    0x500: v500(0xa0) = CONST 
    0x502: v502(0x2) = CONST 
    0x504: v504(0x10000000000000000000000000000000000000000) = EXP v502(0x2), v500(0xa0)
    0x505: v505(0xffffffffffffffffffffffffffffffffffffffff) = SUB v504(0x10000000000000000000000000000000000000000), v4fe(0x1)
    0x506: v506 = AND v505(0xffffffffffffffffffffffffffffffffffffffff), v4fd
    0x508: JUMP v1ff(0x916)

    Begin block 0x916
    prev=[0x4fa], succ=[]
    =================================
    0x917: v917(0x40) = CONST 
    0x91a: v91a = MLOAD v917(0x40)
    0x91b: v91b(0x1) = CONST 
    0x91d: v91d(0xa0) = CONST 
    0x91f: v91f(0x2) = CONST 
    0x921: v921(0x10000000000000000000000000000000000000000) = EXP v91f(0x2), v91d(0xa0)
    0x922: v922(0xffffffffffffffffffffffffffffffffffffffff) = SUB v921(0x10000000000000000000000000000000000000000), v91b(0x1)
    0x925: v925 = AND v506, v922(0xffffffffffffffffffffffffffffffffffffffff)
    0x927: MSTORE v91a, v925
    0x928: v928 = MLOAD v917(0x40)
    0x92c: v92c(0x0) = SUB v91a, v928
    0x92d: v92d(0x20) = CONST 
    0x92f: v92f(0x20) = ADD v92d(0x20), v92c(0x0)
    0x931: RETURN v928, v92f(0x20)

}

function isWorker(address)() public {
    Begin block 0x206
    prev=[], succ=[0x20e, 0x212]
    =================================
    0x207: v207 = CALLVALUE 
    0x209: v209 = ISZERO v207
    0x20a: v20a(0x212) = CONST 
    0x20d: JUMPI v20a(0x212), v209

    Begin block 0x20e
    prev=[0x206], succ=[]
    =================================
    0x20e: v20e(0x0) = CONST 
    0x211: REVERT v20e(0x0), v20e(0x0)

    Begin block 0x212
    prev=[0x206], succ=[0x509B0x212]
    =================================
    0x214: v214(0x951) = CONST 
    0x217: v217(0x1) = CONST 
    0x219: v219(0xa0) = CONST 
    0x21b: v21b(0x2) = CONST 
    0x21d: v21d(0x10000000000000000000000000000000000000000) = EXP v21b(0x2), v219(0xa0)
    0x21e: v21e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21d(0x10000000000000000000000000000000000000000), v217(0x1)
    0x21f: v21f(0x4) = CONST 
    0x221: v221 = CALLDATALOAD v21f(0x4)
    0x222: v222 = AND v221, v21e(0xffffffffffffffffffffffffffffffffffffffff)
    0x223: v223(0x509) = CONST 
    0x226: JUMP v223(0x509)

    Begin block 0x509B0x212
    prev=[0x212], succ=[0x951]
    =================================
    0x50aS0x212: v50aV212(0x1) = CONST 
    0x50cS0x212: v50cV212(0xa0) = CONST 
    0x50eS0x212: v50eV212(0x2) = CONST 
    0x510S0x212: v510V212(0x10000000000000000000000000000000000000000) = EXP v50eV212(0x2), v50cV212(0xa0)
    0x511S0x212: v511V212(0xffffffffffffffffffffffffffffffffffffffff) = SUB v510V212(0x10000000000000000000000000000000000000000), v50aV212(0x1)
    0x512S0x212: v512V212 = AND v511V212(0xffffffffffffffffffffffffffffffffffffffff), v222
    0x513S0x212: v513V212(0x0) = CONST 
    0x517S0x212: MSTORE v513V212(0x0), v512V212
    0x518S0x212: v518V212(0x6) = CONST 
    0x51aS0x212: v51aV212(0x20) = CONST 
    0x51cS0x212: MSTORE v51aV212(0x20), v518V212(0x6)
    0x51dS0x212: v51dV212(0x40) = CONST 
    0x520S0x212: v520V212 = SHA3 v513V212(0x0), v51dV212(0x40)
    0x521S0x212: v521V212 = SLOAD v520V212
    0x522S0x212: v522V212 = ISZERO v521V212
    0x523S0x212: v523V212 = ISZERO v522V212
    0x525S0x212: JUMP v214(0x951)

    Begin block 0x951
    prev=[0x509B0x212], succ=[]
    =================================
    0x952: v952(0x40) = CONST 
    0x955: v955 = MLOAD v952(0x40)
    0x957: v957 = ISZERO v523V212
    0x958: v958 = ISZERO v957
    0x95a: MSTORE v955, v958
    0x95b: v95b = MLOAD v952(0x40)
    0x95f: v95f(0x0) = SUB v955, v95b
    0x960: v960(0x20) = CONST 
    0x962: v962(0x20) = ADD v960(0x20), v95f(0x0)
    0x964: RETURN v95b, v962(0x20)

}

function getDelegate()() public {
    Begin block 0x227
    prev=[], succ=[0x22f, 0x233]
    =================================
    0x228: v228 = CALLVALUE 
    0x22a: v22a = ISZERO v228
    0x22b: v22b(0x233) = CONST 
    0x22e: JUMPI v22b(0x233), v22a

    Begin block 0x22f
    prev=[0x227], succ=[]
    =================================
    0x22f: v22f(0x0) = CONST 
    0x232: REVERT v22f(0x0), v22f(0x0)

    Begin block 0x233
    prev=[0x227], succ=[0x526]
    =================================
    0x235: v235(0x984) = CONST 
    0x238: v238(0x526) = CONST 
    0x23b: JUMP v238(0x526)

    Begin block 0x526
    prev=[0x233], succ=[0x984]
    =================================
    0x527: v527(0x0) = CONST 
    0x529: v529 = SLOAD v527(0x0)
    0x52a: v52a(0x1) = CONST 
    0x52c: v52c(0xa0) = CONST 
    0x52e: v52e(0x2) = CONST 
    0x530: v530(0x10000000000000000000000000000000000000000) = EXP v52e(0x2), v52c(0xa0)
    0x531: v531(0xffffffffffffffffffffffffffffffffffffffff) = SUB v530(0x10000000000000000000000000000000000000000), v52a(0x1)
    0x532: v532 = AND v531(0xffffffffffffffffffffffffffffffffffffffff), v529
    0x534: JUMP v235(0x984)

    Begin block 0x984
    prev=[0x526], succ=[]
    =================================
    0x985: v985(0x40) = CONST 
    0x988: v988 = MLOAD v985(0x40)
    0x989: v989(0x1) = CONST 
    0x98b: v98b(0xa0) = CONST 
    0x98d: v98d(0x2) = CONST 
    0x98f: v98f(0x10000000000000000000000000000000000000000) = EXP v98d(0x2), v98b(0xa0)
    0x990: v990(0xffffffffffffffffffffffffffffffffffffffff) = SUB v98f(0x10000000000000000000000000000000000000000), v989(0x1)
    0x993: v993 = AND v532, v990(0xffffffffffffffffffffffffffffffffffffffff)
    0x995: MSTORE v988, v993
    0x996: v996 = MLOAD v985(0x40)
    0x99a: v99a(0x0) = SUB v988, v996
    0x99b: v99b(0x20) = CONST 
    0x99d: v99d(0x20) = ADD v99b(0x20), v99a(0x0)
    0x99f: RETURN v996, v99d(0x20)

}

function removeWorker(address)() public {
    Begin block 0x23c
    prev=[], succ=[0x244, 0x248]
    =================================
    0x23d: v23d = CALLVALUE 
    0x23f: v23f = ISZERO v23d
    0x240: v240(0x248) = CONST 
    0x243: JUMPI v240(0x248), v23f

    Begin block 0x244
    prev=[0x23c], succ=[]
    =================================
    0x244: v244(0x0) = CONST 
    0x247: REVERT v244(0x0), v244(0x0)

    Begin block 0x248
    prev=[0x23c], succ=[0x535]
    =================================
    0x24a: v24a(0x9bf) = CONST 
    0x24d: v24d(0x1) = CONST 
    0x24f: v24f(0xa0) = CONST 
    0x251: v251(0x2) = CONST 
    0x253: v253(0x10000000000000000000000000000000000000000) = EXP v251(0x2), v24f(0xa0)
    0x254: v254(0xffffffffffffffffffffffffffffffffffffffff) = SUB v253(0x10000000000000000000000000000000000000000), v24d(0x1)
    0x255: v255(0x4) = CONST 
    0x257: v257 = CALLDATALOAD v255(0x4)
    0x258: v258 = AND v257, v254(0xffffffffffffffffffffffffffffffffffffffff)
    0x259: v259(0x535) = CONST 
    0x25c: JUMP v259(0x535)

    Begin block 0x535
    prev=[0x248], succ=[0x553, 0x557]
    =================================
    0x536: v536(0x5) = CONST 
    0x538: v538 = SLOAD v536(0x5)
    0x539: v539(0x0) = CONST 
    0x540: v540 = CALLER 
    0x541: v541(0x1) = CONST 
    0x543: v543(0xa0) = CONST 
    0x545: v545(0x2) = CONST 
    0x547: v547(0x10000000000000000000000000000000000000000) = EXP v545(0x2), v543(0xa0)
    0x548: v548(0xffffffffffffffffffffffffffffffffffffffff) = SUB v547(0x10000000000000000000000000000000000000000), v541(0x1)
    0x54b: v54b = AND v548(0xffffffffffffffffffffffffffffffffffffffff), v540
    0x54d: v54d = AND v538, v548(0xffffffffffffffffffffffffffffffffffffffff)
    0x54e: v54e = EQ v54d, v54b
    0x54f: v54f(0x557) = CONST 
    0x552: JUMPI v54f(0x557), v54e

    Begin block 0x553
    prev=[0x535], succ=[]
    =================================
    0x553: v553(0x0) = CONST 
    0x556: REVERT v553(0x0), v553(0x0)

    Begin block 0x557
    prev=[0x535], succ=[0x509B0x557]
    =================================
    0x558: v558(0x560) = CONST 
    0x55c: v55c(0x509) = CONST 
    0x55f: JUMP v55c(0x509)

    Begin block 0x509B0x557
    prev=[0x557], succ=[0x560]
    =================================
    0x50aS0x557: v50aV557(0x1) = CONST 
    0x50cS0x557: v50cV557(0xa0) = CONST 
    0x50eS0x557: v50eV557(0x2) = CONST 
    0x510S0x557: v510V557(0x10000000000000000000000000000000000000000) = EXP v50eV557(0x2), v50cV557(0xa0)
    0x511S0x557: v511V557(0xffffffffffffffffffffffffffffffffffffffff) = SUB v510V557(0x10000000000000000000000000000000000000000), v50aV557(0x1)
    0x512S0x557: v512V557 = AND v511V557(0xffffffffffffffffffffffffffffffffffffffff), v258
    0x513S0x557: v513V557(0x0) = CONST 
    0x517S0x557: MSTORE v513V557(0x0), v512V557
    0x518S0x557: v518V557(0x6) = CONST 
    0x51aS0x557: v51aV557(0x20) = CONST 
    0x51cS0x557: MSTORE v51aV557(0x20), v518V557(0x6)
    0x51dS0x557: v51dV557(0x40) = CONST 
    0x520S0x557: v520V557 = SHA3 v513V557(0x0), v51dV557(0x40)
    0x521S0x557: v521V557 = SLOAD v520V557
    0x522S0x557: v522V557 = ISZERO v521V557
    0x523S0x557: v523V557 = ISZERO v522V557
    0x525S0x557: JUMP v558(0x560)

    Begin block 0x560
    prev=[0x509B0x557], succ=[0x567, 0x56b]
    =================================
    0x561: v561 = ISZERO v523V557
    0x562: v562 = ISZERO v561
    0x563: v563(0x56b) = CONST 
    0x566: JUMPI v563(0x56b), v562

    Begin block 0x567
    prev=[0x560], succ=[]
    =================================
    0x567: v567(0x0) = CONST 
    0x56a: REVERT v567(0x0), v567(0x0)

    Begin block 0x56b
    prev=[0x560], succ=[0x599, 0x59a]
    =================================
    0x56c: v56c(0x1) = CONST 
    0x56e: v56e(0xa0) = CONST 
    0x570: v570(0x2) = CONST 
    0x572: v572(0x10000000000000000000000000000000000000000) = EXP v570(0x2), v56e(0xa0)
    0x573: v573(0xffffffffffffffffffffffffffffffffffffffff) = SUB v572(0x10000000000000000000000000000000000000000), v56c(0x1)
    0x575: v575 = AND v258, v573(0xffffffffffffffffffffffffffffffffffffffff)
    0x576: v576(0x0) = CONST 
    0x57a: MSTORE v576(0x0), v575
    0x57b: v57b(0x6) = CONST 
    0x57d: v57d(0x20) = CONST 
    0x57f: MSTORE v57d(0x20), v57b(0x6)
    0x580: v580(0x40) = CONST 
    0x583: v583 = SHA3 v576(0x0), v580(0x40)
    0x584: v584 = SLOAD v583
    0x585: v585(0x7) = CONST 
    0x588: v588 = SLOAD v585(0x7)
    0x58d: v58d(0x0) = CONST 
    0x58f: v58f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v58d(0x0)
    0x591: v591 = ADD v588, v58f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x594: v594 = LT v591, v588
    0x595: v595(0x59a) = CONST 
    0x598: JUMPI v595(0x59a), v594

    Begin block 0x599
    prev=[0x56b], succ=[]
    =================================
    0x599: THROW 

    Begin block 0x59a
    prev=[0x56b], succ=[0x5d3, 0x5d4]
    =================================
    0x59b: v59b(0x0) = CONST 
    0x59f: MSTORE v59b(0x0), v585(0x7)
    0x5a0: v5a0(0x20) = CONST 
    0x5a4: v5a4 = SHA3 v59b(0x0), v5a0(0x20)
    0x5a7: v5a7 = ADD v591, v5a4
    0x5a8: v5a8 = SLOAD v5a7
    0x5a9: v5a9(0x1) = CONST 
    0x5ab: v5ab(0xa0) = CONST 
    0x5ad: v5ad(0x2) = CONST 
    0x5af: v5af(0x10000000000000000000000000000000000000000) = EXP v5ad(0x2), v5ab(0xa0)
    0x5b0: v5b0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5af(0x10000000000000000000000000000000000000000), v5a9(0x1)
    0x5b1: v5b1 = AND v5b0(0xffffffffffffffffffffffffffffffffffffffff), v5a8
    0x5b4: MSTORE v59b(0x0), v5b1
    0x5b5: v5b5(0x6) = CONST 
    0x5b9: MSTORE v5a0(0x20), v5b5(0x6)
    0x5ba: v5ba(0x40) = CONST 
    0x5be: v5be = SHA3 v59b(0x0), v5ba(0x40)
    0x5c1: SSTORE v5be, v584
    0x5c2: v5c2(0x7) = CONST 
    0x5c5: v5c5 = SLOAD v5c2(0x7)
    0x5ce: v5ce = LT v584, v5c5
    0x5cf: v5cf(0x5d4) = CONST 
    0x5d2: JUMPI v5cf(0x5d4), v5ce

    Begin block 0x5d3
    prev=[0x59a], succ=[]
    =================================
    0x5d3: THROW 

    Begin block 0x5d4
    prev=[0x59a], succ=[0x78dB0x5d4]
    =================================
    0x5d5: v5d5(0x0) = CONST 
    0x5d9: MSTORE v5d5(0x0), v5c2(0x7)
    0x5da: v5da(0x20) = CONST 
    0x5de: v5de = SHA3 v5d5(0x0), v5da(0x20)
    0x5df: v5df = ADD v5de, v584
    0x5e1: v5e1 = SLOAD v5df
    0x5e2: v5e2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5f7: v5f7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x5f8: v5f8 = AND v5f7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5e1
    0x5f9: v5f9(0x1) = CONST 
    0x5fb: v5fb(0xa0) = CONST 
    0x5fd: v5fd(0x2) = CONST 
    0x5ff: v5ff(0x10000000000000000000000000000000000000000) = EXP v5fd(0x2), v5fb(0xa0)
    0x600: v600(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5ff(0x10000000000000000000000000000000000000000), v5f9(0x1)
    0x604: v604 = AND v600(0xffffffffffffffffffffffffffffffffffffffff), v5b1
    0x608: v608 = OR v604, v5f8
    0x60a: SSTORE v5df, v608
    0x60b: v60b(0x7) = CONST 
    0x60e: v60e = SLOAD v60b(0x7)
    0x610: v610(0x61d) = CONST 
    0x614: v614(0x0) = CONST 
    0x616: v616(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v614(0x0)
    0x618: v618 = ADD v60e, v616(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x619: v619(0x78d) = CONST 
    0x61c: JUMP v619(0x78d), v618, v60b(0x7), v610(0x61d)

    Begin block 0x78dB0x5d4
    prev=[0x5d4], succ=[0x79bB0x5d4, 0xaefB0x5d4]
    =================================
    0x78fS0x5d4: v78fV5d4 = SLOAD v60b(0x7)
    0x792S0x5d4: SSTORE v60b(0x7), v618
    0x795S0x5d4: v795V5d4 = GT v78fV5d4, v618
    0x796S0x5d4: v796V5d4 = ISZERO v795V5d4
    0x797S0x5d4: v797V5d4(0xaef) = CONST 
    0x79aS0x5d4: JUMPI v797V5d4(0xaef), v796V5d4

    Begin block 0x79bB0x5d4
    prev=[0x78dB0x5d4], succ=[0x7b6B0x79bB0x5d4]
    =================================
    0x79bS0x5d4: v79bV5d4(0x0) = CONST 
    0x79fS0x5d4: MSTORE v79bV5d4(0x0), v60b(0x7)
    0x7a0S0x5d4: v7a0V5d4(0x20) = CONST 
    0x7a3S0x5d4: v7a3V5d4 = SHA3 v79bV5d4(0x0), v7a0V5d4(0x20)
    0x7a4S0x5d4: v7a4V5d4(0xb13) = CONST 
    0x7a9S0x5d4: v7a9V5d4 = ADD v7a3V5d4, v78fV5d4
    0x7acS0x5d4: v7acV5d4 = ADD v618, v7a3V5d4
    0x7adS0x5d4: v7adV5d4(0x7b6) = CONST 
    0x7b0S0x5d4: JUMP v7adV5d4(0x7b6)

    Begin block 0x7b6B0x79bB0x5d4
    prev=[0x79bB0x5d4], succ=[0x7bcB0x79bB0x5d4]
    =================================
    0x7b7S0x79bS0x5d4: v7b7V79bV5d4(0x7d0) = CONST 

    Begin block 0x7bcB0x79bB0x5d4
    prev=[0x7c5B0x79bB0x5d4, 0x7b6B0x79bB0x5d4], succ=[0x7c5B0x79bB0x5d4, 0xb37B0x79bB0x5d4]
    =================================
    0x7bc_0x0S0x79bS0x5d4: v7bc_0V79bV5d4 = PHI v7acV5d4, v7cbV79bV5d4
    0x7bfS0x79bS0x5d4: v7bfV79bV5d4 = GT v7a9V5d4, v7bc_0V79bV5d4
    0x7c0S0x79bS0x5d4: v7c0V79bV5d4 = ISZERO v7bfV79bV5d4
    0x7c1S0x79bS0x5d4: v7c1V79bV5d4(0xb37) = CONST 
    0x7c4S0x79bS0x5d4: JUMPI v7c1V79bV5d4(0xb37), v7c0V79bV5d4

    Begin block 0x7c5B0x79bB0x5d4
    prev=[0x7bcB0x79bB0x5d4], succ=[0x7bcB0x79bB0x5d4]
    =================================
    0x7c5S0x79bS0x5d4: v7c5V79bV5d4(0x0) = CONST 
    0x7c5_0x0S0x79bS0x5d4: v7c5_0V79bV5d4 = PHI v7acV5d4, v7cbV79bV5d4
    0x7c8S0x79bS0x5d4: SSTORE v7c5_0V79bV5d4, v7c5V79bV5d4(0x0)
    0x7c9S0x79bS0x5d4: v7c9V79bV5d4(0x1) = CONST 
    0x7cbS0x79bS0x5d4: v7cbV79bV5d4 = ADD v7c9V79bV5d4(0x1), v7c5_0V79bV5d4
    0x7ccS0x79bS0x5d4: v7ccV79bV5d4(0x7bc) = CONST 
    0x7cfS0x79bS0x5d4: JUMP v7ccV79bV5d4(0x7bc)

    Begin block 0xb37B0x79bB0x5d4
    prev=[0x7bcB0x79bB0x5d4], succ=[0x7d0B0x79bB0x5d4]
    =================================
    0xb3aS0x79bS0x5d4: JUMP v7b7V79bV5d4(0x7d0)

    Begin block 0x7d0B0x79bB0x5d4
    prev=[0xb37B0x79bB0x5d4], succ=[0xb13B0x5d4]
    =================================
    0x7d2S0x79bS0x5d4: JUMP v7a4V5d4(0xb13)

    Begin block 0xb13B0x5d4
    prev=[0x7d0B0x79bB0x5d4], succ=[0x61d]
    =================================
    0xb17S0x5d4: JUMP v610(0x61d)

    Begin block 0x61d
    prev=[0xaefB0x5d4, 0xb13B0x5d4], succ=[0x9bf]
    =================================
    0x61f: v61f(0x1) = CONST 
    0x621: v621(0xa0) = CONST 
    0x623: v623(0x2) = CONST 
    0x625: v625(0x10000000000000000000000000000000000000000) = EXP v623(0x2), v621(0xa0)
    0x626: v626(0xffffffffffffffffffffffffffffffffffffffff) = SUB v625(0x10000000000000000000000000000000000000000), v61f(0x1)
    0x628: v628 = AND v258, v626(0xffffffffffffffffffffffffffffffffffffffff)
    0x629: v629(0x0) = CONST 
    0x62d: MSTORE v629(0x0), v628
    0x62e: v62e(0x6) = CONST 
    0x630: v630(0x20) = CONST 
    0x634: MSTORE v630(0x20), v62e(0x6)
    0x635: v635(0x40) = CONST 
    0x639: v639 = SHA3 v629(0x0), v635(0x40)
    0x63d: SSTORE v639, v629(0x0)
    0x63f: v63f = MLOAD v635(0x40)
    0x642: MSTORE v63f, v628
    0x644: v644 = MLOAD v635(0x40)
    0x645: v645(0x3edc40c0328998eaea1b10228950034eb711623f80702c71897e856964c203c3) = CONST 
    0x669: v669(0x0) = SUB v63f, v644
    0x66c: v66c(0x20) = ADD v630(0x20), v669(0x0)
    0x66e: LOG1 v644, v66c(0x20), v645(0x3edc40c0328998eaea1b10228950034eb711623f80702c71897e856964c203c3)
    0x670: v670(0x1) = CONST 
    0x677: JUMP v24a(0x9bf)

    Begin block 0x9bf
    prev=[0x61d], succ=[]
    =================================
    0x9c0: v9c0(0x40) = CONST 
    0x9c3: v9c3 = MLOAD v9c0(0x40)
    0x9c5: v9c5 = ISZERO v670(0x1)
    0x9c6: v9c6 = ISZERO v9c5
    0x9c8: MSTORE v9c3, v9c6
    0x9c9: v9c9 = MLOAD v9c0(0x40)
    0x9cd: v9cd(0x0) = SUB v9c3, v9c9
    0x9ce: v9ce(0x20) = CONST 
    0x9d0: v9d0(0x20) = ADD v9ce(0x20), v9cd(0x0)
    0x9d2: RETURN v9c9, v9d0(0x20)

    Begin block 0xaefB0x5d4
    prev=[0x78dB0x5d4], succ=[0x61d]
    =================================
    0xaf3S0x5d4: JUMP v610(0x61d)

}

function allWorkers()() public {
    Begin block 0x25d
    prev=[], succ=[0x265, 0x269]
    =================================
    0x25e: v25e = CALLVALUE 
    0x260: v260 = ISZERO v25e
    0x261: v261(0x269) = CONST 
    0x264: JUMPI v261(0x269), v260

    Begin block 0x265
    prev=[0x25d], succ=[]
    =================================
    0x265: v265(0x0) = CONST 
    0x268: REVERT v265(0x0), v265(0x0)

    Begin block 0x269
    prev=[0x25d], succ=[0x678B0x269]
    =================================
    0x26b: v26b(0x272) = CONST 
    0x26e: v26e(0x678) = CONST 
    0x271: JUMP v26e(0x678)

    Begin block 0x678B0x269
    prev=[0x269], succ=[0x6aeB0x269, 0x69fB0x269]
    =================================
    0x679S0x269: v679V269(0x60) = CONST 
    0x67bS0x269: v67bV269(0x0) = CONST 
    0x67dS0x269: v67dV269(0x1) = CONST 
    0x67fS0x269: v67fV269(0x7) = CONST 
    0x682S0x269: v682V269 = SLOAD v67fV269(0x7)
    0x685S0x269: v685V269 = SUB v682V269, v67dV269(0x1)
    0x686S0x269: v686V269(0x40) = CONST 
    0x688S0x269: v688V269 = MLOAD v686V269(0x40)
    0x68cS0x269: MSTORE v688V269, v685V269
    0x68eS0x269: v68eV269(0x20) = CONST 
    0x690S0x269: v690V269 = MUL v68eV269(0x20), v685V269
    0x691S0x269: v691V269(0x20) = CONST 
    0x693S0x269: v693V269 = ADD v691V269(0x20), v690V269
    0x695S0x269: v695V269 = ADD v688V269, v693V269
    0x696S0x269: v696V269(0x40) = CONST 
    0x698S0x269: MSTORE v696V269(0x40), v695V269
    0x69aS0x269: v69aV269 = ISZERO v685V269
    0x69bS0x269: v69bV269(0x6ae) = CONST 
    0x69eS0x269: JUMPI v69bV269(0x6ae), v69aV269

    Begin block 0x6aeB0x269
    prev=[0x678B0x269, 0x69fB0x269], succ=[0x6b6B0x269]
    =================================
    0x6b2S0x269: v6b2V269(0x1) = CONST 

    Begin block 0x6b6B0x269
    prev=[0x6aeB0x269, 0x6f8B0x269], succ=[0x6c1B0x269, 0xaccB0x269]
    =================================
    0x6b6_0x0S0x269: v6b6_0V269 = PHI v6b2V269(0x1), v712V269
    0x6b7S0x269: v6b7V269(0x7) = CONST 
    0x6b9S0x269: v6b9V269 = SLOAD v6b7V269(0x7)
    0x6bbS0x269: v6bbV269 = LT v6b6_0V269, v6b9V269
    0x6bcS0x269: v6bcV269 = ISZERO v6bbV269
    0x6bdS0x269: v6bdV269(0xacc) = CONST 
    0x6c0S0x269: JUMPI v6bdV269(0xacc), v6bcV269

    Begin block 0x6c1B0x269
    prev=[0x6b6B0x269], succ=[0x6ceB0x269, 0x6cdB0x269]
    =================================
    0x6c1S0x269: v6c1V269(0x7) = CONST 
    0x6c1_0x0S0x269: v6c1_0V269 = PHI v6b2V269(0x1), v712V269
    0x6c4S0x269: v6c4V269 = SLOAD v6c1V269(0x7)
    0x6c8S0x269: v6c8V269 = LT v6c1_0V269, v6c4V269
    0x6c9S0x269: v6c9V269(0x6ce) = CONST 
    0x6ccS0x269: JUMPI v6c9V269(0x6ce), v6c8V269

    Begin block 0x6ceB0x269
    prev=[0x6c1B0x269], succ=[0x6f8B0x269, 0x6f7B0x269]
    =================================
    0x6ce_0x0S0x269: v6ce_0V269 = PHI v6b2V269(0x1), v712V269
    0x6ce_0x2S0x269: v6ce_2V269 = PHI v6b2V269(0x1), v712V269
    0x6cfS0x269: v6cfV269(0x0) = CONST 
    0x6d3S0x269: MSTORE v6cfV269(0x0), v6c1V269(0x7)
    0x6d4S0x269: v6d4V269(0x20) = CONST 
    0x6d8S0x269: v6d8V269 = SHA3 v6cfV269(0x0), v6d4V269(0x20)
    0x6d9S0x269: v6d9V269 = ADD v6d8V269, v6ce_0V269
    0x6daS0x269: v6daV269 = SLOAD v6d9V269
    0x6dcS0x269: v6dcV269 = MLOAD v688V269
    0x6ddS0x269: v6ddV269(0x1) = CONST 
    0x6dfS0x269: v6dfV269(0xa0) = CONST 
    0x6e1S0x269: v6e1V269(0x2) = CONST 
    0x6e3S0x269: v6e3V269(0x10000000000000000000000000000000000000000) = EXP v6e1V269(0x2), v6dfV269(0xa0)
    0x6e4S0x269: v6e4V269(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e3V269(0x10000000000000000000000000000000000000000), v6ddV269(0x1)
    0x6e7S0x269: v6e7V269 = AND v6daV269, v6e4V269(0xffffffffffffffffffffffffffffffffffffffff)
    0x6ebS0x269: v6ebV269(0x0) = CONST 
    0x6edS0x269: v6edV269(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v6ebV269(0x0)
    0x6efS0x269: v6efV269 = ADD v6ce_2V269, v6edV269(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x6f2S0x269: v6f2V269 = LT v6efV269, v6dcV269
    0x6f3S0x269: v6f3V269(0x6f8) = CONST 
    0x6f6S0x269: JUMPI v6f3V269(0x6f8), v6f2V269

    Begin block 0x6f8B0x269
    prev=[0x6ceB0x269], succ=[0x6b6B0x269]
    =================================
    0x6f8_0x3S0x269: v6f8_3V269 = PHI v6b2V269(0x1), v712V269
    0x6f9S0x269: v6f9V269(0x1) = CONST 
    0x6fbS0x269: v6fbV269(0xa0) = CONST 
    0x6fdS0x269: v6fdV269(0x2) = CONST 
    0x6ffS0x269: v6ffV269(0x10000000000000000000000000000000000000000) = EXP v6fdV269(0x2), v6fbV269(0xa0)
    0x700S0x269: v700V269(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ffV269(0x10000000000000000000000000000000000000000), v6f9V269(0x1)
    0x703S0x269: v703V269 = AND v6e7V269, v700V269(0xffffffffffffffffffffffffffffffffffffffff)
    0x704S0x269: v704V269(0x20) = CONST 
    0x708S0x269: v708V269 = MUL v704V269(0x20), v6efV269
    0x70bS0x269: v70bV269 = ADD v688V269, v708V269
    0x70eS0x269: v70eV269 = ADD v704V269(0x20), v70bV269
    0x70fS0x269: MSTORE v70eV269, v703V269
    0x710S0x269: v710V269(0x1) = CONST 
    0x712S0x269: v712V269 = ADD v710V269(0x1), v6f8_3V269
    0x713S0x269: v713V269(0x6b6) = CONST 
    0x716S0x269: JUMP v713V269(0x6b6)

    Begin block 0x6f7B0x269
    prev=[0x6ceB0x269], succ=[]
    =================================
    0x6f7S0x269: THROW 

    Begin block 0x6cdB0x269
    prev=[0x6c1B0x269], succ=[]
    =================================
    0x6cdS0x269: THROW 

    Begin block 0xaccB0x269
    prev=[0x6b6B0x269], succ=[0x272]
    =================================
    0xacfS0x269: JUMP v26b(0x272)

    Begin block 0x272
    prev=[0xaccB0x269], succ=[0x296]
    =================================
    0x273: v273(0x40) = CONST 
    0x276: v276 = MLOAD v273(0x40)
    0x277: v277(0x20) = CONST 
    0x27b: MSTORE v276, v277(0x20)
    0x27d: v27d = MLOAD v688V269
    0x280: v280 = ADD v276, v277(0x20)
    0x281: MSTORE v280, v27d
    0x283: v283 = MLOAD v688V269
    0x28a: v28a = ADD v276, v273(0x40)
    0x28e: v28e = ADD v277(0x20), v688V269
    0x290: v290 = MUL v283, v277(0x20)
    0x294: v294(0x0) = CONST 

    Begin block 0x296
    prev=[0x272, 0x29f], succ=[0x2ae, 0x29f]
    =================================
    0x296_0x0: v296_0 = PHI v294(0x0), v2a9
    0x299: v299 = LT v296_0, v290
    0x29a: v29a = ISZERO v299
    0x29b: v29b(0x2ae) = CONST 
    0x29e: JUMPI v29b(0x2ae), v29a

    Begin block 0x2ae
    prev=[0x296], succ=[]
    =================================
    0x2b5: v2b5 = ADD v290, v28a
    0x2ba: v2ba(0x40) = CONST 
    0x2bc: v2bc = MLOAD v2ba(0x40)
    0x2bf: v2bf = SUB v2b5, v2bc
    0x2c1: RETURN v2bc, v2bf

    Begin block 0x29f
    prev=[0x296], succ=[0x296]
    =================================
    0x29f_0x0: v29f_0 = PHI v294(0x0), v2a9
    0x2a1: v2a1 = ADD v29f_0, v28e
    0x2a2: v2a2 = MLOAD v2a1
    0x2a5: v2a5 = ADD v29f_0, v28a
    0x2a6: MSTORE v2a5, v2a2
    0x2a7: v2a7(0x20) = CONST 
    0x2a9: v2a9 = ADD v2a7(0x20), v29f_0
    0x2aa: v2aa(0x296) = CONST 
    0x2ad: JUMP v2aa(0x296)

    Begin block 0x69fB0x269
    prev=[0x678B0x269], succ=[0x6aeB0x269]
    =================================
    0x6a0S0x269: v6a0V269(0x20) = CONST 
    0x6a2S0x269: v6a2V269 = ADD v6a0V269(0x20), v688V269
    0x6a3S0x269: v6a3V269(0x20) = CONST 
    0x6a6S0x269: v6a6V269 = MUL v685V269, v6a3V269(0x20)
    0x6a8S0x269: v6a8V269 = CODESIZE 
    0x6aaS0x269: CODECOPY v6a2V269, v6a8V269, v6a6V269
    0x6abS0x269: v6abV269 = ADD v6a6V269, v6a2V269

}

function forward()() public {
    Begin block 0x2c2
    prev=[], succ=[0x2ca, 0x2ce]
    =================================
    0x2c3: v2c3 = CALLVALUE 
    0x2c5: v2c5 = ISZERO v2c3
    0x2c6: v2c6(0x2ce) = CONST 
    0x2c9: JUMPI v2c6(0x2ce), v2c5

    Begin block 0x2ca
    prev=[0x2c2], succ=[]
    =================================
    0x2ca: v2ca(0x0) = CONST 
    0x2cd: REVERT v2ca(0x0), v2ca(0x0)

    Begin block 0x2ce
    prev=[0x2c2], succ=[0x71b]
    =================================
    0x2d0: v2d0(0x9f2) = CONST 
    0x2d3: v2d3(0x71b) = CONST 
    0x2d6: JUMP v2d3(0x71b)

    Begin block 0x71b
    prev=[0x2ce], succ=[0x9f2]
    =================================
    0x71c: v71c(0x2) = CONST 
    0x71e: v71e = SLOAD v71c(0x2)
    0x71f: v71f(0x1) = CONST 
    0x721: v721(0xa0) = CONST 
    0x723: v723(0x2) = CONST 
    0x725: v725(0x10000000000000000000000000000000000000000) = EXP v723(0x2), v721(0xa0)
    0x726: v726(0xffffffffffffffffffffffffffffffffffffffff) = SUB v725(0x10000000000000000000000000000000000000000), v71f(0x1)
    0x727: v727 = AND v726(0xffffffffffffffffffffffffffffffffffffffff), v71e
    0x729: JUMP v2d0(0x9f2)

    Begin block 0x9f2
    prev=[0x71b], succ=[]
    =================================
    0x9f3: v9f3(0x40) = CONST 
    0x9f6: v9f6 = MLOAD v9f3(0x40)
    0x9f7: v9f7(0x1) = CONST 
    0x9f9: v9f9(0xa0) = CONST 
    0x9fb: v9fb(0x2) = CONST 
    0x9fd: v9fd(0x10000000000000000000000000000000000000000) = EXP v9fb(0x2), v9f9(0xa0)
    0x9fe: v9fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9fd(0x10000000000000000000000000000000000000000), v9f7(0x1)
    0xa01: va01 = AND v727, v9fe(0xffffffffffffffffffffffffffffffffffffffff)
    0xa03: MSTORE v9f6, va01
    0xa04: va04 = MLOAD v9f3(0x40)
    0xa08: va08(0x0) = SUB v9f6, va04
    0xa09: va09(0x20) = CONST 
    0xa0b: va0b(0x20) = ADD va09(0x20), va08(0x0)
    0xa0d: RETURN va04, va0b(0x20)

}

function createdWallets()() public {
    Begin block 0x2d7
    prev=[], succ=[0x2df, 0x2e3]
    =================================
    0x2d8: v2d8 = CALLVALUE 
    0x2da: v2da = ISZERO v2d8
    0x2db: v2db(0x2e3) = CONST 
    0x2de: JUMPI v2db(0x2e3), v2da

    Begin block 0x2df
    prev=[0x2d7], succ=[]
    =================================
    0x2df: v2df(0x0) = CONST 
    0x2e2: REVERT v2df(0x0), v2df(0x0)

    Begin block 0x2e3
    prev=[0x2d7], succ=[0x72a]
    =================================
    0x2e5: v2e5(0xa2d) = CONST 
    0x2e8: v2e8(0x72a) = CONST 
    0x2eb: JUMP v2e8(0x72a)

    Begin block 0x72a
    prev=[0x2e3], succ=[0xa2d]
    =================================
    0x72b: v72b(0x3) = CONST 
    0x72d: v72d = SLOAD v72b(0x3)
    0x72f: JUMP v2e5(0xa2d)

    Begin block 0xa2d
    prev=[0x72a], succ=[]
    =================================
    0xa2e: va2e(0x40) = CONST 
    0xa31: va31 = MLOAD va2e(0x40)
    0xa34: MSTORE va31, v72d
    0xa35: va35 = MLOAD va2e(0x40)
    0xa39: va39(0x0) = SUB va31, va35
    0xa3a: va3a(0x20) = CONST 
    0xa3c: va3c(0x20) = ADD va3a(0x20), va39(0x0)
    0xa3e: RETURN va35, va3c(0x20)

}

function walletsDelegate()() public {
    Begin block 0x2ec
    prev=[], succ=[0x2f4, 0x2f8]
    =================================
    0x2ed: v2ed = CALLVALUE 
    0x2ef: v2ef = ISZERO v2ed
    0x2f0: v2f0(0x2f8) = CONST 
    0x2f3: JUMPI v2f0(0x2f8), v2ef

    Begin block 0x2f4
    prev=[0x2ec], succ=[]
    =================================
    0x2f4: v2f4(0x0) = CONST 
    0x2f7: REVERT v2f4(0x0), v2f4(0x0)

    Begin block 0x2f8
    prev=[0x2ec], succ=[0x730]
    =================================
    0x2fa: v2fa(0xa5e) = CONST 
    0x2fd: v2fd(0x730) = CONST 
    0x300: JUMP v2fd(0x730)

    Begin block 0x730
    prev=[0x2f8], succ=[0xa5e]
    =================================
    0x731: v731(0x0) = CONST 
    0x733: v733 = SLOAD v731(0x0)
    0x734: v734(0x1) = CONST 
    0x736: v736(0xa0) = CONST 
    0x738: v738(0x2) = CONST 
    0x73a: v73a(0x10000000000000000000000000000000000000000) = EXP v738(0x2), v736(0xa0)
    0x73b: v73b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v73a(0x10000000000000000000000000000000000000000), v734(0x1)
    0x73c: v73c = AND v73b(0xffffffffffffffffffffffffffffffffffffffff), v733
    0x73e: JUMP v2fa(0xa5e)

    Begin block 0xa5e
    prev=[0x730], succ=[]
    =================================
    0xa5f: va5f(0x40) = CONST 
    0xa62: va62 = MLOAD va5f(0x40)
    0xa63: va63(0x1) = CONST 
    0xa65: va65(0xa0) = CONST 
    0xa67: va67(0x2) = CONST 
    0xa69: va69(0x10000000000000000000000000000000000000000) = EXP va67(0x2), va65(0xa0)
    0xa6a: va6a(0xffffffffffffffffffffffffffffffffffffffff) = SUB va69(0x10000000000000000000000000000000000000000), va63(0x1)
    0xa6d: va6d = AND v73c, va6a(0xffffffffffffffffffffffffffffffffffffffff)
    0xa6f: MSTORE va62, va6d
    0xa70: va70 = MLOAD va5f(0x40)
    0xa74: va74(0x0) = SUB va62, va70
    0xa75: va75(0x20) = CONST 
    0xa77: va77(0x20) = ADD va75(0x20), va74(0x0)
    0xa79: RETURN va70, va77(0x20)

}

function setControllerDelegate(address)() public {
    Begin block 0x301
    prev=[], succ=[0x309, 0x30d]
    =================================
    0x302: v302 = CALLVALUE 
    0x304: v304 = ISZERO v302
    0x305: v305(0x30d) = CONST 
    0x308: JUMPI v305(0x30d), v304

    Begin block 0x309
    prev=[0x301], succ=[]
    =================================
    0x309: v309(0x0) = CONST 
    0x30c: REVERT v309(0x0), v309(0x0)

    Begin block 0x30d
    prev=[0x301], succ=[0x73f]
    =================================
    0x30f: v30f(0xa99) = CONST 
    0x312: v312(0x1) = CONST 
    0x314: v314(0xa0) = CONST 
    0x316: v316(0x2) = CONST 
    0x318: v318(0x10000000000000000000000000000000000000000) = EXP v316(0x2), v314(0xa0)
    0x319: v319(0xffffffffffffffffffffffffffffffffffffffff) = SUB v318(0x10000000000000000000000000000000000000000), v312(0x1)
    0x31a: v31a(0x4) = CONST 
    0x31c: v31c = CALLDATALOAD v31a(0x4)
    0x31d: v31d = AND v31c, v319(0xffffffffffffffffffffffffffffffffffffffff)
    0x31e: v31e(0x73f) = CONST 
    0x321: JUMP v31e(0x73f)

    Begin block 0x73f
    prev=[0x30d], succ=[0x759, 0x75d]
    =================================
    0x740: v740(0x5) = CONST 
    0x742: v742 = SLOAD v740(0x5)
    0x743: v743(0x0) = CONST 
    0x746: v746 = CALLER 
    0x747: v747(0x1) = CONST 
    0x749: v749(0xa0) = CONST 
    0x74b: v74b(0x2) = CONST 
    0x74d: v74d(0x10000000000000000000000000000000000000000) = EXP v74b(0x2), v749(0xa0)
    0x74e: v74e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v74d(0x10000000000000000000000000000000000000000), v747(0x1)
    0x751: v751 = AND v74e(0xffffffffffffffffffffffffffffffffffffffff), v746
    0x753: v753 = AND v742, v74e(0xffffffffffffffffffffffffffffffffffffffff)
    0x754: v754 = EQ v753, v751
    0x755: v755(0x75d) = CONST 
    0x758: JUMPI v755(0x75d), v754

    Begin block 0x759
    prev=[0x73f], succ=[]
    =================================
    0x759: v759(0x0) = CONST 
    0x75c: REVERT v759(0x0), v759(0x0)

    Begin block 0x75d
    prev=[0x73f], succ=[0xa99]
    =================================
    0x75f: v75f(0x1) = CONST 
    0x762: v762 = SLOAD v75f(0x1)
    0x763: v763(0x1) = CONST 
    0x765: v765(0xa0) = CONST 
    0x767: v767(0x2) = CONST 
    0x769: v769(0x10000000000000000000000000000000000000000) = EXP v767(0x2), v765(0xa0)
    0x76a: v76a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v769(0x10000000000000000000000000000000000000000), v763(0x1)
    0x76c: v76c = AND v31d, v76a(0xffffffffffffffffffffffffffffffffffffffff)
    0x76d: v76d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x782: v782(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v76d(0xffffffffffffffffffffffffffffffffffffffff)
    0x785: v785 = AND v762, v782(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x786: v786 = OR v785, v76c
    0x788: SSTORE v75f(0x1), v786
    0x78c: JUMP v30f(0xa99)

    Begin block 0xa99
    prev=[0x75d], succ=[]
    =================================
    0xa9a: va9a(0x40) = CONST 
    0xa9d: va9d = MLOAD va9a(0x40)
    0xa9f: va9f = ISZERO v75f(0x1)
    0xaa0: vaa0 = ISZERO va9f
    0xaa2: MSTORE va9d, vaa0
    0xaa3: vaa3 = MLOAD va9a(0x40)
    0xaa7: vaa7(0x0) = SUB va9d, vaa3
    0xaa8: vaa8(0x20) = CONST 
    0xaaa: vaaa(0x20) = ADD vaa8(0x20), vaa7(0x0)
    0xaac: RETURN vaa3, vaaa(0x20)

}

function fallback()() public {
    Begin block 0xcf
    prev=[], succ=[0xda, 0x11d]
    =================================
    0xd0: vd0(0x960) = CONST 
    0xd3: vd3 = GAS 
    0xd4: vd4 = GT vd3, vd0(0x960)
    0xd5: vd5 = ISZERO vd4
    0xd6: vd6(0x11d) = CONST 
    0xd9: JUMPI vd6(0x11d), vd5

    Begin block 0xda
    prev=[0xcf], succ=[0x322]
    =================================
    0xda: vda(0x1) = CONST 
    0xdc: vdc = SLOAD vda(0x1)
    0xdd: vdd(0x40) = CONST 
    0xe0: ve0 = MLOAD vdd(0x40)
    0xe1: ve1(0x20) = CONST 
    0xe3: ve3 = CALLDATASIZE 
    0xe4: ve4(0x1f) = CONST 
    0xe7: ve7 = ADD ve3, ve4(0x1f)
    0xea: vea = DIV ve7, ve1(0x20)
    0xec: vec = MUL ve1(0x20), vea
    0xee: vee = ADD ve0, vec
    0xf0: vf0 = ADD ve1(0x20), vee
    0xf3: MSTORE vdd(0x40), vf0
    0xf6: MSTORE ve0, ve3
    0xf7: vf7(0x11d) = CONST 
    0xfb: vfb(0x1) = CONST 
    0xfd: vfd(0xa0) = CONST 
    0xff: vff(0x2) = CONST 
    0x101: v101(0x10000000000000000000000000000000000000000) = EXP vff(0x2), vfd(0xa0)
    0x102: v102(0xffffffffffffffffffffffffffffffffffffffff) = SUB v101(0x10000000000000000000000000000000000000000), vfb(0x1)
    0x103: v103 = AND v102(0xffffffffffffffffffffffffffffffffffffffff), vdc
    0x105: v105(0x0) = CONST 
    0x10b: v10b = ADD ve0, ve1(0x20)
    0x111: CALLDATACOPY v10b, v105(0x0), ve3
    0x113: v113(0x322) = CONST 
    0x11c: JUMP v113(0x322)

    Begin block 0x322
    prev=[0xda], succ=[0x346, 0x343]
    =================================
    0x323: v323(0x0) = CONST 
    0x327: v327 = MLOAD ve0
    0x328: v328(0x20) = CONST 
    0x32b: v32b = ADD ve0, v328(0x20)
    0x32d: v32d(0x2710) = CONST 
    0x330: v330 = GAS 
    0x331: v331 = SUB v330, v32d(0x2710)
    0x332: v332 = DELEGATECALL v331, v103, v32b, v327, v323(0x0), v323(0x0)
    0x333: v333 = RETURNDATASIZE 
    0x334: v334(0x40) = CONST 
    0x336: v336 = MLOAD v334(0x40)
    0x338: v338(0x0) = CONST 
    0x33b: RETURNDATACOPY v336, v338(0x0), v333
    0x33e: v33e = ISZERO v332
    0x33f: v33f(0x346) = CONST 
    0x342: JUMPI v33f(0x346), v33e

    Begin block 0x346
    prev=[0x322], succ=[]
    =================================
    0x349: REVERT v336, v333

    Begin block 0x343
    prev=[0x322], succ=[]
    =================================
    0x345: RETURN v336, v333

    Begin block 0x11d
    prev=[0xcf], succ=[]
    =================================
    0x11e: STOP 

}

