function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x397]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x391: v391(0x397) = CONST 
    0x392: JUMPI v391(0x397), v8

    Begin block 0xd
    prev=[0x0], succ=[0x39a, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x22a5ce0e) = CONST 
    0x3c: v3c = EQ v37(0x22a5ce0e), v35
    0x393: v393(0x39a) = CONST 
    0x394: JUMPI v393(0x39a), v3c

    Begin block 0x39a
    prev=[0xd], succ=[]
    =================================
    0x39b: v39b(0x99) = CONST 
    0x39c: CALLPRIVATE v39b(0x99)

    Begin block 0x41
    prev=[0xd], succ=[0x397, 0x39d]
    =================================
    0x42: v42(0xfd8b2370) = CONST 
    0x47: v47 = EQ v42(0xfd8b2370), v35
    0x395: v395(0x39d) = CONST 
    0x396: JUMPI v395(0x39d), v47

    Begin block 0x397
    prev=[0x0, 0x41], succ=[]
    =================================
    0x398: v398(0x4c) = CONST 
    0x399: CALLPRIVATE v398(0x4c)

    Begin block 0x39d
    prev=[0x41], succ=[]
    =================================
    0x39e: v39e(0xf0) = CONST 
    0x39f: CALLPRIVATE v39e(0xf0)

}

function fallback()() public {
    Begin block 0x4c
    prev=[], succ=[0x95, 0x92]
    =================================
    0x4d: v4d(0x0) = CONST 
    0x50: v50(0x0) = CONST 
    0x53: v53 = SLOAD v4d(0x0)
    0x55: v55(0x100) = CONST 
    0x58: v58(0x1) = EXP v55(0x100), v50(0x0)
    0x5a: v5a = DIV v53, v58(0x1)
    0x5b: v5b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x70: v70 = AND v5b(0xffffffffffffffffffffffffffffffffffffffff), v5a
    0x73: v73(0x40) = CONST 
    0x75: v75 = MLOAD v73(0x40)
    0x76: v76 = CALLDATASIZE 
    0x77: v77(0x0) = CONST 
    0x7a: CALLDATACOPY v75, v77(0x0), v76
    0x7b: v7b(0x0) = CONST 
    0x7e: v7e = CALLDATASIZE 
    0x81: v81 = GAS 
    0x82: v82 = DELEGATECALL v81, v70, v75, v7e, v7b(0x0), v7b(0x0)
    0x83: v83 = RETURNDATASIZE 
    0x85: v85(0x0) = CONST 
    0x88: RETURNDATACOPY v75, v85(0x0), v83
    0x8a: v8a(0x0) = CONST 
    0x8d: v8d = EQ v82, v8a(0x0)
    0x8e: v8e(0x95) = CONST 
    0x91: JUMPI v8e(0x95), v8d

    Begin block 0x95
    prev=[0x4c], succ=[]
    =================================
    0x98: REVERT v75, v83

    Begin block 0x92
    prev=[0x4c], succ=[]
    =================================
    0x94: RETURN v75, v83

}

function getContAdr()() public {
    Begin block 0x99
    prev=[], succ=[0xa1, 0xa5]
    =================================
    0x9a: v9a = CALLVALUE 
    0x9c: v9c = ISZERO v9a
    0x9d: v9d(0xa5) = CONST 
    0xa0: JUMPI v9d(0xa5), v9c

    Begin block 0xa1
    prev=[0x99], succ=[]
    =================================
    0xa1: va1(0x0) = CONST 
    0xa4: REVERT va1(0x0), va1(0x0)

    Begin block 0xa5
    prev=[0x99], succ=[0x141]
    =================================
    0xa7: va7(0xae) = CONST 
    0xaa: vaa(0x141) = CONST 
    0xad: JUMP vaa(0x141)

    Begin block 0x141
    prev=[0xa5], succ=[0x19b, 0x208]
    =================================
    0x142: v142(0x0) = CONST 
    0x144: v144(0x1) = CONST 
    0x146: v146(0x0) = CONST 
    0x149: v149 = SLOAD v144(0x1)
    0x14b: v14b(0x100) = CONST 
    0x14e: v14e(0x1) = EXP v14b(0x100), v146(0x0)
    0x150: v150 = DIV v149, v14e(0x1)
    0x151: v151(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x166: v166 = AND v151(0xffffffffffffffffffffffffffffffffffffffff), v150
    0x167: v167(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17c: v17c = AND v167(0xffffffffffffffffffffffffffffffffffffffff), v166
    0x17d: v17d = CALLER 
    0x17e: v17e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x193: v193 = AND v17e(0xffffffffffffffffffffffffffffffffffffffff), v17d
    0x194: v194 = EQ v193, v17c
    0x195: v195 = ISZERO v194
    0x196: v196 = ISZERO v195
    0x197: v197(0x208) = CONST 
    0x19a: JUMPI v197(0x208), v196

    Begin block 0x19b
    prev=[0x141], succ=[]
    =================================
    0x19b: v19b(0x40) = CONST 
    0x19d: v19d = MLOAD v19b(0x40)
    0x19e: v19e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c0: MSTORE v19d, v19e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c1: v1c1(0x4) = CONST 
    0x1c3: v1c3 = ADD v1c1(0x4), v19d
    0x1c6: v1c6(0x20) = CONST 
    0x1c8: v1c8 = ADD v1c6(0x20), v1c3
    0x1cb: v1cb(0x20) = SUB v1c8, v1c3
    0x1cd: MSTORE v1c3, v1cb(0x20)
    0x1ce: v1ce(0x13) = CONST 
    0x1d1: MSTORE v1c8, v1ce(0x13)
    0x1d2: v1d2(0x20) = CONST 
    0x1d4: v1d4 = ADD v1d2(0x20), v1c8
    0x1d6: v1d6(0x41646d696e206f6e6c792066756e6374696f6e00000000000000000000000000) = CONST 
    0x1f8: MSTORE v1d4, v1d6(0x41646d696e206f6e6c792066756e6374696f6e00000000000000000000000000)
    0x1fa: v1fa(0x20) = CONST 
    0x1fc: v1fc = ADD v1fa(0x20), v1d4
    0x200: v200(0x40) = CONST 
    0x202: v202 = MLOAD v200(0x40)
    0x205: v205(0x64) = SUB v1fc, v202
    0x207: REVERT v202, v205(0x64)

    Begin block 0x208
    prev=[0x141], succ=[0xae]
    =================================
    0x209: v209(0x0) = CONST 
    0x20d: v20d = SLOAD v209(0x0)
    0x20f: v20f(0x100) = CONST 
    0x212: v212(0x1) = EXP v20f(0x100), v209(0x0)
    0x214: v214 = DIV v20d, v212(0x1)
    0x215: v215(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22a: v22a = AND v215(0xffffffffffffffffffffffffffffffffffffffff), v214
    0x22e: JUMP va7(0xae)

    Begin block 0xae
    prev=[0x208], succ=[]
    =================================
    0xaf: vaf(0x40) = CONST 
    0xb1: vb1 = MLOAD vaf(0x40)
    0xb4: vb4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc9: vc9 = AND vb4(0xffffffffffffffffffffffffffffffffffffffff), v22a
    0xca: vca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf: vdf = AND vca(0xffffffffffffffffffffffffffffffffffffffff), vc9
    0xe1: MSTORE vb1, vdf
    0xe2: ve2(0x20) = CONST 
    0xe4: ve4 = ADD ve2(0x20), vb1
    0xe8: ve8(0x40) = CONST 
    0xea: vea = MLOAD ve8(0x40)
    0xed: ved(0x20) = SUB ve4, vea
    0xef: RETURN vea, ved(0x20)

}

function setTargetAddress(address)() public {
    Begin block 0xf0
    prev=[], succ=[0xf8, 0xfc]
    =================================
    0xf1: vf1 = CALLVALUE 
    0xf3: vf3 = ISZERO vf1
    0xf4: vf4(0xfc) = CONST 
    0xf7: JUMPI vf4(0xfc), vf3

    Begin block 0xf8
    prev=[0xf0], succ=[]
    =================================
    0xf8: vf8(0x0) = CONST 
    0xfb: REVERT vf8(0x0), vf8(0x0)

    Begin block 0xfc
    prev=[0xf0], succ=[0x10f, 0x113]
    =================================
    0xfe: vfe(0x13f) = CONST 
    0x101: v101(0x4) = CONST 
    0x104: v104 = CALLDATASIZE 
    0x105: v105 = SUB v104, v101(0x4)
    0x106: v106(0x20) = CONST 
    0x109: v109 = LT v105, v106(0x20)
    0x10a: v10a = ISZERO v109
    0x10b: v10b(0x113) = CONST 
    0x10e: JUMPI v10b(0x113), v10a

    Begin block 0x10f
    prev=[0xfc], succ=[]
    =================================
    0x10f: v10f(0x0) = CONST 
    0x112: REVERT v10f(0x0), v10f(0x0)

    Begin block 0x113
    prev=[0xfc], succ=[0x22f]
    =================================
    0x115: v115 = ADD v101(0x4), v105
    0x119: v119 = CALLDATALOAD v101(0x4)
    0x11a: v11a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12f: v12f = AND v11a(0xffffffffffffffffffffffffffffffffffffffff), v119
    0x131: v131(0x20) = CONST 
    0x133: v133(0x24) = ADD v131(0x20), v101(0x4)
    0x13b: v13b(0x22f) = CONST 
    0x13e: JUMP v13b(0x22f)

    Begin block 0x22f
    prev=[0x113], succ=[0x287, 0x2f4]
    =================================
    0x230: v230(0x1) = CONST 
    0x232: v232(0x0) = CONST 
    0x235: v235 = SLOAD v230(0x1)
    0x237: v237(0x100) = CONST 
    0x23a: v23a(0x1) = EXP v237(0x100), v232(0x0)
    0x23c: v23c = DIV v235, v23a(0x1)
    0x23d: v23d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x252: v252 = AND v23d(0xffffffffffffffffffffffffffffffffffffffff), v23c
    0x253: v253(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x268: v268 = AND v253(0xffffffffffffffffffffffffffffffffffffffff), v252
    0x269: v269 = CALLER 
    0x26a: v26a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27f: v27f = AND v26a(0xffffffffffffffffffffffffffffffffffffffff), v269
    0x280: v280 = EQ v27f, v268
    0x281: v281 = ISZERO v280
    0x282: v282 = ISZERO v281
    0x283: v283(0x2f4) = CONST 
    0x286: JUMPI v283(0x2f4), v282

    Begin block 0x287
    prev=[0x22f], succ=[]
    =================================
    0x287: v287(0x40) = CONST 
    0x289: v289 = MLOAD v287(0x40)
    0x28a: v28a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ac: MSTORE v289, v28a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ad: v2ad(0x4) = CONST 
    0x2af: v2af = ADD v2ad(0x4), v289
    0x2b2: v2b2(0x20) = CONST 
    0x2b4: v2b4 = ADD v2b2(0x20), v2af
    0x2b7: v2b7(0x20) = SUB v2b4, v2af
    0x2b9: MSTORE v2af, v2b7(0x20)
    0x2ba: v2ba(0x13) = CONST 
    0x2bd: MSTORE v2b4, v2ba(0x13)
    0x2be: v2be(0x20) = CONST 
    0x2c0: v2c0 = ADD v2be(0x20), v2b4
    0x2c2: v2c2(0x41646d696e206f6e6c792066756e6374696f6e00000000000000000000000000) = CONST 
    0x2e4: MSTORE v2c0, v2c2(0x41646d696e206f6e6c792066756e6374696f6e00000000000000000000000000)
    0x2e6: v2e6(0x20) = CONST 
    0x2e8: v2e8 = ADD v2e6(0x20), v2c0
    0x2ec: v2ec(0x40) = CONST 
    0x2ee: v2ee = MLOAD v2ec(0x40)
    0x2f1: v2f1(0x64) = SUB v2e8, v2ee
    0x2f3: REVERT v2ee, v2f1(0x64)

    Begin block 0x2f4
    prev=[0x22f], succ=[0x32c, 0x330]
    =================================
    0x2f5: v2f5(0x0) = CONST 
    0x2f7: v2f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30c: v30c(0x0) = AND v2f7(0xffffffffffffffffffffffffffffffffffffffff), v2f5(0x0)
    0x30e: v30e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x323: v323 = AND v30e(0xffffffffffffffffffffffffffffffffffffffff), v12f
    0x324: v324 = EQ v323, v30c(0x0)
    0x325: v325 = ISZERO v324
    0x326: v326 = ISZERO v325
    0x327: v327 = ISZERO v326
    0x328: v328(0x330) = CONST 
    0x32b: JUMPI v328(0x330), v327

    Begin block 0x32c
    prev=[0x2f4], succ=[]
    =================================
    0x32c: v32c(0x0) = CONST 
    0x32f: REVERT v32c(0x0), v32c(0x0)

    Begin block 0x330
    prev=[0x2f4], succ=[0x13f]
    =================================
    0x332: v332(0x0) = CONST 
    0x335: v335(0x100) = CONST 
    0x338: v338(0x1) = EXP v335(0x100), v332(0x0)
    0x33a: v33a = SLOAD v332(0x0)
    0x33c: v33c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x351: v351(0xffffffffffffffffffffffffffffffffffffffff) = MUL v33c(0xffffffffffffffffffffffffffffffffffffffff), v338(0x1)
    0x352: v352(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v351(0xffffffffffffffffffffffffffffffffffffffff)
    0x353: v353 = AND v352(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v33a
    0x356: v356(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36b: v36b = AND v356(0xffffffffffffffffffffffffffffffffffffffff), v12f
    0x36c: v36c = MUL v36b, v338(0x1)
    0x36d: v36d = OR v36c, v353
    0x36f: SSTORE v332(0x0), v36d
    0x372: JUMP vfe(0x13f)

    Begin block 0x13f
    prev=[0x330], succ=[]
    =================================
    0x140: STOP 

}

