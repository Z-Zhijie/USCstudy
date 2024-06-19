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
    prev=[0x0], succ=[0x1a, 0xe2e]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0xdf5: vdf5(0xe2e) = CONST 
    0xdf6: JUMPI vdf5(0xe2e), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x71, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x96b55f7d) = CONST 
    0x26: v26 = GT v21(0x96b55f7d), v1f
    0x27: v27(0x71) = CONST 
    0x2a: JUMPI v27(0x71), v26

    Begin block 0x71
    prev=[0x1a], succ=[0xe0d, 0x7d]
    =================================
    0x73: v73(0x39af9eb) = CONST 
    0x78: v78 = EQ v73(0x39af9eb), v1f
    0xe03: ve03(0xe0d) = CONST 
    0xe04: JUMPI ve03(0xe0d), v78

    Begin block 0xe0d
    prev=[0x71], succ=[]
    =================================
    0xe0e: ve0e(0xae) = CONST 
    0xe0f: CALLPRIVATE ve0e(0xae)

    Begin block 0x7d
    prev=[0x71], succ=[0xe10, 0x88]
    =================================
    0x7e: v7e(0xc340a24) = CONST 
    0x83: v83 = EQ v7e(0xc340a24), v1f
    0xe05: ve05(0xe10) = CONST 
    0xe06: JUMPI ve05(0xe10), v83

    Begin block 0xe10
    prev=[0x7d], succ=[]
    =================================
    0xe11: ve11(0xdd) = CONST 
    0xe12: CALLPRIVATE ve11(0xdd)

    Begin block 0x88
    prev=[0x7d], succ=[0xe13, 0x93]
    =================================
    0x89: v89(0xce7dc4a) = CONST 
    0x8e: v8e = EQ v89(0xce7dc4a), v1f
    0xe07: ve07(0xe13) = CONST 
    0xe08: JUMPI ve07(0xe13), v8e

    Begin block 0xe13
    prev=[0x88], succ=[]
    =================================
    0xe14: ve14(0x101) = CONST 
    0xe15: CALLPRIVATE ve14(0x101)

    Begin block 0x93
    prev=[0x88], succ=[0xe16, 0x9e]
    =================================
    0x94: v94(0x4cf088d9) = CONST 
    0x99: v99 = EQ v94(0x4cf088d9), v1f
    0xe09: ve09(0xe16) = CONST 
    0xe0a: JUMPI ve09(0xe16), v99

    Begin block 0xe16
    prev=[0x93], succ=[]
    =================================
    0xe17: ve17(0x126) = CONST 
    0xe18: CALLPRIVATE ve17(0x126)

    Begin block 0x9e
    prev=[0x93], succ=[0xe19, 0xa9]
    =================================
    0x9f: v9f(0x8ddb2864) = CONST 
    0xa4: va4 = EQ v9f(0x8ddb2864), v1f
    0xe0b: ve0b(0xe19) = CONST 
    0xe0c: JUMPI ve0b(0xe19), va4

    Begin block 0xe19
    prev=[0x9e], succ=[]
    =================================
    0xe1a: ve1a(0x12e) = CONST 
    0xe1b: CALLPRIVATE ve1a(0x12e)

    Begin block 0xa9
    prev=[0x9e], succ=[]
    =================================
    0xaa: vaa(0x0) = CONST 
    0xad: REVERT vaa(0x0), vaa(0x0)

    Begin block 0x2b
    prev=[0x1a], succ=[0xe1c, 0x36]
    =================================
    0x2c: v2c(0x96b55f7d) = CONST 
    0x31: v31 = EQ v2c(0x96b55f7d), v1f
    0xdf7: vdf7(0xe1c) = CONST 
    0xdf8: JUMPI vdf7(0xe1c), v31

    Begin block 0xe1c
    prev=[0x2b], succ=[]
    =================================
    0xe1d: ve1d(0x154) = CONST 
    0xe1e: CALLPRIVATE ve1d(0x154)

    Begin block 0x36
    prev=[0x2b], succ=[0xe1f, 0x41]
    =================================
    0x37: v37(0xa13a7350) = CONST 
    0x3c: v3c = EQ v37(0xa13a7350), v1f
    0xdf9: vdf9(0xe1f) = CONST 
    0xdfa: JUMPI vdf9(0xe1f), v3c

    Begin block 0xe1f
    prev=[0x36], succ=[]
    =================================
    0xe20: ve20(0x15c) = CONST 
    0xe21: CALLPRIVATE ve20(0x15c)

    Begin block 0x41
    prev=[0x36], succ=[0xe22, 0x4c]
    =================================
    0x42: v42(0xc4d66de8) = CONST 
    0x47: v47 = EQ v42(0xc4d66de8), v1f
    0xdfb: vdfb(0xe22) = CONST 
    0xdfc: JUMPI vdfb(0xe22), v47

    Begin block 0xe22
    prev=[0x41], succ=[]
    =================================
    0xe23: ve23(0x1cc) = CONST 
    0xe24: CALLPRIVATE ve23(0x1cc)

    Begin block 0x4c
    prev=[0x41], succ=[0xe25, 0x57]
    =================================
    0x4d: v4d(0xe3056a34) = CONST 
    0x52: v52 = EQ v4d(0xe3056a34), v1f
    0xdfd: vdfd(0xe25) = CONST 
    0xdfe: JUMPI vdfd(0xe25), v52

    Begin block 0xe25
    prev=[0x4c], succ=[]
    =================================
    0xe26: ve26(0x1f2) = CONST 
    0xe27: CALLPRIVATE ve26(0x1f2)

    Begin block 0x57
    prev=[0x4c], succ=[0xe28, 0x62]
    =================================
    0x58: v58(0xe58bb639) = CONST 
    0x5d: v5d = EQ v58(0xe58bb639), v1f
    0xdff: vdff(0xe28) = CONST 
    0xe00: JUMPI vdff(0xe28), v5d

    Begin block 0xe28
    prev=[0x57], succ=[]
    =================================
    0xe29: ve29(0x1fa) = CONST 
    0xe2a: CALLPRIVATE ve29(0x1fa)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0xe2b]
    =================================
    0x63: v63(0xf235757f) = CONST 
    0x68: v68 = EQ v63(0xf235757f), v1f
    0xe01: ve01(0xe2b) = CONST 
    0xe02: JUMPI ve01(0xe2b), v68

    Begin block 0x6d
    prev=[0x62], succ=[0xc07]
    =================================
    0x6d: v6d(0xc07) = CONST 
    0x70: JUMP v6d(0xc07)

    Begin block 0xc07
    prev=[0x6d], succ=[]
    =================================
    0xc08: vc08(0x0) = CONST 
    0xc0b: REVERT vc08(0x0), vc08(0x0)

    Begin block 0xe2b
    prev=[0x62], succ=[]
    =================================
    0xe2c: ve2c(0x202) = CONST 
    0xe2d: CALLPRIVATE ve2c(0x202)

    Begin block 0xe2e
    prev=[0x10], succ=[]
    =================================
    0xe2f: ve2f(0xbe3) = CONST 
    0xe30: CALLPRIVATE ve2f(0xbe3)

}

function updateAlphaTier(uint256,uint256)() public {
    Begin block 0x101
    prev=[], succ=[0x113, 0x117]
    =================================
    0x102: v102(0xc97) = CONST 
    0x105: v105(0x4) = CONST 
    0x108: v108 = CALLDATASIZE 
    0x109: v109 = SUB v108, v105(0x4)
    0x10a: v10a(0x40) = CONST 
    0x10d: v10d = LT v109, v10a(0x40)
    0x10e: v10e = ISZERO v10d
    0x10f: v10f(0x117) = CONST 
    0x112: JUMPI v10f(0x117), v10e

    Begin block 0x113
    prev=[0x101], succ=[]
    =================================
    0x113: v113(0x0) = CONST 
    0x116: REVERT v113(0x0), v113(0x0)

    Begin block 0x117
    prev=[0x101], succ=[0x24f]
    =================================
    0x11a: v11a = CALLDATALOAD v105(0x4)
    0x11c: v11c(0x20) = CONST 
    0x11e: v11e(0x24) = ADD v11c(0x20), v105(0x4)
    0x11f: v11f = CALLDATALOAD v11e(0x24)
    0x120: v120(0x24f) = CONST 
    0x123: JUMP v120(0x24f)

    Begin block 0x24f
    prev=[0x117], succ=[0x268, 0x2a7]
    =================================
    0x250: v250(0x0) = CONST 
    0x252: v252 = SLOAD v250(0x0)
    0x253: v253(0x10000) = CONST 
    0x258: v258 = DIV v252, v253(0x10000)
    0x259: v259(0x1) = CONST 
    0x25b: v25b(0x1) = CONST 
    0x25d: v25d(0xa0) = CONST 
    0x25f: v25f(0x10000000000000000000000000000000000000000) = SHL v25d(0xa0), v25b(0x1)
    0x260: v260(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25f(0x10000000000000000000000000000000000000000), v259(0x1)
    0x261: v261 = AND v260(0xffffffffffffffffffffffffffffffffffffffff), v258
    0x262: v262 = CALLER 
    0x263: v263 = EQ v262, v261
    0x264: v264(0x2a7) = CONST 
    0x267: JUMPI v264(0x2a7), v263

    Begin block 0x268
    prev=[0x24f], succ=[]
    =================================
    0x268: v268(0x40) = CONST 
    0x26b: v26b = MLOAD v268(0x40)
    0x26c: v26c(0x461bcd) = CONST 
    0x270: v270(0xe5) = CONST 
    0x272: v272(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v270(0xe5), v26c(0x461bcd)
    0x274: MSTORE v26b, v272(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x275: v275(0x20) = CONST 
    0x277: v277(0x4) = CONST 
    0x27a: v27a = ADD v26b, v277(0x4)
    0x27b: MSTORE v27a, v275(0x20)
    0x27c: v27c(0x10) = CONST 
    0x27e: v27e(0x24) = CONST 
    0x281: v281 = ADD v26b, v27e(0x24)
    0x282: MSTORE v281, v27c(0x10)
    0x283: v283(0x3737ba103a34329033b7bb32b93737b9) = CONST 
    0x294: v294(0x81) = CONST 
    0x296: v296(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000) = SHL v294(0x81), v283(0x3737ba103a34329033b7bb32b93737b9)
    0x297: v297(0x44) = CONST 
    0x29a: v29a = ADD v26b, v297(0x44)
    0x29b: MSTORE v29a, v296(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000)
    0x29d: v29d = MLOAD v268(0x40)
    0x2a1: v2a1(0x0) = SUB v26b, v29d
    0x2a2: v2a2(0x64) = CONST 
    0x2a4: v2a4(0x64) = ADD v2a2(0x64), v2a1(0x0)
    0x2a6: REVERT v29d, v2a4(0x64)

    Begin block 0x2a7
    prev=[0x24f], succ=[0x2b1, 0x2e7]
    =================================
    0x2a8: v2a8(0x4) = CONST 
    0x2aa: v2aa = SLOAD v2a8(0x4)
    0x2ac: v2ac = LT v11a, v2aa
    0x2ad: v2ad(0x2e7) = CONST 
    0x2b0: JUMPI v2ad(0x2e7), v2ac

    Begin block 0x2b1
    prev=[0x2a7], succ=[]
    =================================
    0x2b1: v2b1(0x40) = CONST 
    0x2b3: v2b3 = MLOAD v2b1(0x40)
    0x2b4: v2b4(0x461bcd) = CONST 
    0x2b8: v2b8(0xe5) = CONST 
    0x2ba: v2ba(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2b8(0xe5), v2b4(0x461bcd)
    0x2bc: MSTORE v2b3, v2ba(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2bd: v2bd(0x4) = CONST 
    0x2bf: v2bf = ADD v2bd(0x4), v2b3
    0x2c2: v2c2(0x20) = CONST 
    0x2c4: v2c4 = ADD v2c2(0x20), v2bf
    0x2c7: v2c7(0x20) = SUB v2c4, v2bf
    0x2c9: MSTORE v2bf, v2c7(0x20)
    0x2ca: v2ca(0x23) = CONST 
    0x2cd: MSTORE v2c4, v2ca(0x23)
    0x2ce: v2ce(0x20) = CONST 
    0x2d0: v2d0 = ADD v2ce(0x20), v2c4
    0x2d2: v2d2(0xa2f) = CONST 
    0x2d5: v2d5(0x23) = CONST 
    0x2d8: CODECOPY v2d0, v2d2(0xa2f), v2d5(0x23)
    0x2d9: v2d9(0x40) = CONST 
    0x2db: v2db = ADD v2d9(0x40), v2d0
    0x2df: v2df(0x40) = CONST 
    0x2e1: v2e1 = MLOAD v2df(0x40)
    0x2e4: v2e4(0x84) = SUB v2db, v2e1
    0x2e6: REVERT v2e1, v2e4(0x84)

    Begin block 0x2e7
    prev=[0x2a7], succ=[0x2ed, 0x323]
    =================================
    0x2e9: v2e9(0x323) = CONST 
    0x2ec: JUMPI v2e9(0x323), v11f

    Begin block 0x2ed
    prev=[0x2e7], succ=[]
    =================================
    0x2ed: v2ed(0x40) = CONST 
    0x2ef: v2ef = MLOAD v2ed(0x40)
    0x2f0: v2f0(0x461bcd) = CONST 
    0x2f4: v2f4(0xe5) = CONST 
    0x2f6: v2f6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2f4(0xe5), v2f0(0x461bcd)
    0x2f8: MSTORE v2ef, v2f6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2f9: v2f9(0x4) = CONST 
    0x2fb: v2fb = ADD v2f9(0x4), v2ef
    0x2fe: v2fe(0x20) = CONST 
    0x300: v300 = ADD v2fe(0x20), v2fb
    0x303: v303(0x20) = SUB v300, v2fb
    0x305: MSTORE v2fb, v303(0x20)
    0x306: v306(0x28) = CONST 
    0x309: MSTORE v300, v306(0x28)
    0x30a: v30a(0x20) = CONST 
    0x30c: v30c = ADD v30a(0x20), v300
    0x30e: v30e(0xb2f) = CONST 
    0x311: v311(0x28) = CONST 
    0x314: CODECOPY v30c, v30e(0xb2f), v311(0x28)
    0x315: v315(0x40) = CONST 
    0x317: v317 = ADD v315(0x40), v30c
    0x31b: v31b(0x40) = CONST 
    0x31d: v31d = MLOAD v31b(0x40)
    0x320: v320(0x84) = SUB v317, v31d
    0x322: REVERT v31d, v320(0x84)

    Begin block 0x323
    prev=[0x2e7], succ=[0x32a, 0x37a]
    =================================
    0x325: v325 = ISZERO v11a
    0x326: v326(0x37a) = CONST 
    0x329: JUMPI v326(0x37a), v325

    Begin block 0x32a
    prev=[0x323], succ=[0x344, 0x37a]
    =================================
    0x32a: v32a(0x0) = CONST 
    0x32c: v32c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v32a(0x0)
    0x32e: v32e = ADD v11a, v32c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x32f: v32f(0x0) = CONST 
    0x333: MSTORE v32f(0x0), v32e
    0x334: v334(0x3) = CONST 
    0x336: v336(0x20) = CONST 
    0x338: MSTORE v336(0x20), v334(0x3)
    0x339: v339(0x40) = CONST 
    0x33c: v33c = SHA3 v32f(0x0), v339(0x40)
    0x33d: v33d = SLOAD v33c
    0x33f: v33f = GT v11f, v33d
    0x340: v340(0x37a) = CONST 
    0x343: JUMPI v340(0x37a), v33f

    Begin block 0x344
    prev=[0x32a], succ=[]
    =================================
    0x344: v344(0x40) = CONST 
    0x346: v346 = MLOAD v344(0x40)
    0x347: v347(0x461bcd) = CONST 
    0x34b: v34b(0xe5) = CONST 
    0x34d: v34d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v34b(0xe5), v347(0x461bcd)
    0x34f: MSTORE v346, v34d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x350: v350(0x4) = CONST 
    0x352: v352 = ADD v350(0x4), v346
    0x355: v355(0x20) = CONST 
    0x357: v357 = ADD v355(0x20), v352
    0x35a: v35a(0x20) = SUB v357, v352
    0x35c: MSTORE v352, v35a(0x20)
    0x35d: v35d(0x44) = CONST 
    0x360: MSTORE v357, v35d(0x44)
    0x361: v361(0x20) = CONST 
    0x363: v363 = ADD v361(0x20), v357
    0x365: v365(0xa52) = CONST 
    0x368: v368(0x44) = CONST 
    0x36b: CODECOPY v363, v365(0xa52), v368(0x44)
    0x36c: v36c(0x60) = CONST 
    0x36e: v36e = ADD v36c(0x60), v363
    0x372: v372(0x40) = CONST 
    0x374: v374 = MLOAD v372(0x40)
    0x377: v377(0xa4) = SUB v36e, v374
    0x379: REVERT v374, v377(0xa4)

    Begin block 0x37a
    prev=[0x32a, 0x323], succ=[0x8efB0x37a]
    =================================
    0x37b: v37b(0x4) = CONST 
    0x37d: v37d = SLOAD v37b(0x4)
    0x37e: v37e(0x388) = CONST 
    0x382: v382(0x1) = CONST 
    0x384: v384(0x8ef) = CONST 
    0x387: JUMP v384(0x8ef)

    Begin block 0x8efB0x37a
    prev=[0x37a], succ=[0x8faB0x37a, 0x946B0x37a]
    =================================
    0x8f0S0x37a: v8f0V37a(0x0) = CONST 
    0x8f4S0x37a: v8f4V37a = GT v382(0x1), v37d
    0x8f5S0x37a: v8f5V37a = ISZERO v8f4V37a
    0x8f6S0x37a: v8f6V37a(0x946) = CONST 
    0x8f9S0x37a: JUMPI v8f6V37a(0x946), v8f5V37a

    Begin block 0x8faB0x37a
    prev=[0x8efB0x37a], succ=[]
    =================================
    0x8faS0x37a: v8faV37a(0x40) = CONST 
    0x8fdS0x37a: v8fdV37a = MLOAD v8faV37a(0x40)
    0x8feS0x37a: v8feV37a(0x461bcd) = CONST 
    0x902S0x37a: v902V37a(0xe5) = CONST 
    0x904S0x37a: v904V37a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v902V37a(0xe5), v8feV37a(0x461bcd)
    0x906S0x37a: MSTORE v8fdV37a, v904V37a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x907S0x37a: v907V37a(0x20) = CONST 
    0x909S0x37a: v909V37a(0x4) = CONST 
    0x90cS0x37a: v90cV37a = ADD v8fdV37a, v909V37a(0x4)
    0x90dS0x37a: MSTORE v90cV37a, v907V37a(0x20)
    0x90eS0x37a: v90eV37a(0x1e) = CONST 
    0x910S0x37a: v910V37a(0x24) = CONST 
    0x913S0x37a: v913V37a = ADD v8fdV37a, v910V37a(0x24)
    0x914S0x37a: MSTORE v913V37a, v90eV37a(0x1e)
    0x915S0x37a: v915V37a(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x936S0x37a: v936V37a(0x44) = CONST 
    0x939S0x37a: v939V37a = ADD v8fdV37a, v936V37a(0x44)
    0x93aS0x37a: MSTORE v939V37a, v915V37a(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x93cS0x37a: v93cV37a = MLOAD v8faV37a(0x40)
    0x940S0x37a: v940V37a(0x0) = SUB v8fdV37a, v93cV37a
    0x941S0x37a: v941V37a(0x64) = CONST 
    0x943S0x37a: v943V37a(0x64) = ADD v941V37a(0x64), v940V37a(0x0)
    0x945S0x37a: REVERT v93cV37a, v943V37a(0x64)

    Begin block 0x946B0x37a
    prev=[0x8efB0x37a], succ=[0x388]
    =================================
    0x949S0x37a: v949V37a = SUB v37d, v382(0x1)
    0x94bS0x37a: JUMP v37e(0x388)

    Begin block 0x388
    prev=[0x946B0x37a], succ=[0x390, 0x3df]
    =================================
    0x38a: v38a = LT v11a, v949V37a
    0x38b: v38b = ISZERO v38a
    0x38c: v38c(0x3df) = CONST 
    0x38f: JUMPI v38c(0x3df), v38b

    Begin block 0x390
    prev=[0x388], succ=[0x3a9, 0x3df]
    =================================
    0x390: v390(0x1) = CONST 
    0x393: v393 = ADD v11a, v390(0x1)
    0x394: v394(0x0) = CONST 
    0x398: MSTORE v394(0x0), v393
    0x399: v399(0x3) = CONST 
    0x39b: v39b(0x20) = CONST 
    0x39d: MSTORE v39b(0x20), v399(0x3)
    0x39e: v39e(0x40) = CONST 
    0x3a1: v3a1 = SHA3 v394(0x0), v39e(0x40)
    0x3a2: v3a2 = SLOAD v3a1
    0x3a4: v3a4 = LT v11f, v3a2
    0x3a5: v3a5(0x3df) = CONST 
    0x3a8: JUMPI v3a5(0x3df), v3a4

    Begin block 0x3a9
    prev=[0x390], succ=[]
    =================================
    0x3a9: v3a9(0x40) = CONST 
    0x3ab: v3ab = MLOAD v3a9(0x40)
    0x3ac: v3ac(0x461bcd) = CONST 
    0x3b0: v3b0(0xe5) = CONST 
    0x3b2: v3b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3b0(0xe5), v3ac(0x461bcd)
    0x3b4: MSTORE v3ab, v3b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3b5: v3b5(0x4) = CONST 
    0x3b7: v3b7 = ADD v3b5(0x4), v3ab
    0x3ba: v3ba(0x20) = CONST 
    0x3bc: v3bc = ADD v3ba(0x20), v3b7
    0x3bf: v3bf(0x20) = SUB v3bc, v3b7
    0x3c1: MSTORE v3b7, v3bf(0x20)
    0x3c2: v3c2(0x40) = CONST 
    0x3c5: MSTORE v3bc, v3c2(0x40)
    0x3c6: v3c6(0x20) = CONST 
    0x3c8: v3c8 = ADD v3c6(0x20), v3bc
    0x3ca: v3ca(0xb57) = CONST 
    0x3cd: v3cd(0x40) = CONST 
    0x3d0: CODECOPY v3c8, v3ca(0xb57), v3cd(0x40)
    0x3d1: v3d1(0x40) = CONST 
    0x3d3: v3d3 = ADD v3d1(0x40), v3c8
    0x3d7: v3d7(0x40) = CONST 
    0x3d9: v3d9 = MLOAD v3d7(0x40)
    0x3dc: v3dc(0x84) = SUB v3d3, v3d9
    0x3de: REVERT v3d9, v3dc(0x84)

    Begin block 0x3df
    prev=[0x390, 0x388], succ=[0xc97]
    =================================
    0x3e0: v3e0(0x0) = CONST 
    0x3e4: MSTORE v3e0(0x0), v11a
    0x3e5: v3e5(0x3) = CONST 
    0x3e7: v3e7(0x20) = CONST 
    0x3eb: MSTORE v3e7(0x20), v3e5(0x3)
    0x3ec: v3ec(0x40) = CONST 
    0x3f1: v3f1 = SHA3 v3e0(0x0), v3ec(0x40)
    0x3f4: SSTORE v3f1, v11f
    0x3f6: v3f6 = MLOAD v3ec(0x40)
    0x3f9: MSTORE v3f6, v11a
    0x3fc: v3fc = ADD v3f6, v3e7(0x20)
    0x3ff: MSTORE v3fc, v11f
    0x401: v401 = MLOAD v3ec(0x40)
    0x402: v402(0x7c0334032b954d80a1d4a83a08ebf0a99d835c40143beec06f14106526167fd0) = CONST 
    0x427: v427(0x0) = SUB v3f6, v401
    0x42a: v42a(0x40) = ADD v3ec(0x40), v427(0x0)
    0x42c: LOG1 v401, v42a(0x40), v402(0x7c0334032b954d80a1d4a83a08ebf0a99d835c40143beec06f14106526167fd0)
    0x42f: JUMP v102(0xc97)

    Begin block 0xc97
    prev=[0x3df], succ=[]
    =================================
    0xc98: STOP 

}

function staking()() public {
    Begin block 0x126
    prev=[], succ=[0x430]
    =================================
    0x127: v127(0xcb8) = CONST 
    0x12a: v12a(0x430) = CONST 
    0x12d: JUMP v12a(0x430)

    Begin block 0x430
    prev=[0x126], succ=[0xcb8]
    =================================
    0x431: v431(0x2) = CONST 
    0x433: v433 = SLOAD v431(0x2)
    0x434: v434(0x1) = CONST 
    0x436: v436(0x1) = CONST 
    0x438: v438(0xa0) = CONST 
    0x43a: v43a(0x10000000000000000000000000000000000000000) = SHL v438(0xa0), v436(0x1)
    0x43b: v43b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43a(0x10000000000000000000000000000000000000000), v434(0x1)
    0x43c: v43c = AND v43b(0xffffffffffffffffffffffffffffffffffffffff), v433
    0x43e: JUMP v127(0xcb8)

    Begin block 0xcb8
    prev=[0x430], succ=[]
    =================================
    0xcb9: vcb9(0x40) = CONST 
    0xcbc: vcbc = MLOAD vcb9(0x40)
    0xcbd: vcbd(0x1) = CONST 
    0xcbf: vcbf(0x1) = CONST 
    0xcc1: vcc1(0xa0) = CONST 
    0xcc3: vcc3(0x10000000000000000000000000000000000000000) = SHL vcc1(0xa0), vcbf(0x1)
    0xcc4: vcc4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcc3(0x10000000000000000000000000000000000000000), vcbd(0x1)
    0xcc7: vcc7 = AND v43c, vcc4(0xffffffffffffffffffffffffffffffffffffffff)
    0xcc9: MSTORE vcbc, vcc7
    0xcca: vcca = MLOAD vcb9(0x40)
    0xcce: vcce(0x0) = SUB vcbc, vcca
    0xccf: vccf(0x20) = CONST 
    0xcd1: vcd1(0x20) = ADD vccf(0x20), vcce(0x0)
    0xcd3: RETURN vcca, vcd1(0x20)

}

function getAlphaTier(address)() public {
    Begin block 0x12e
    prev=[], succ=[0x140, 0x144]
    =================================
    0x12f: v12f(0xcf3) = CONST 
    0x132: v132(0x4) = CONST 
    0x135: v135 = CALLDATASIZE 
    0x136: v136 = SUB v135, v132(0x4)
    0x137: v137(0x20) = CONST 
    0x13a: v13a = LT v136, v137(0x20)
    0x13b: v13b = ISZERO v13a
    0x13c: v13c(0x144) = CONST 
    0x13f: JUMPI v13c(0x144), v13b

    Begin block 0x140
    prev=[0x12e], succ=[]
    =================================
    0x140: v140(0x0) = CONST 
    0x143: REVERT v140(0x0), v140(0x0)

    Begin block 0x144
    prev=[0x12e], succ=[0x43f]
    =================================
    0x146: v146 = CALLDATALOAD v132(0x4)
    0x147: v147(0x1) = CONST 
    0x149: v149(0x1) = CONST 
    0x14b: v14b(0xa0) = CONST 
    0x14d: v14d(0x10000000000000000000000000000000000000000) = SHL v14b(0xa0), v149(0x1)
    0x14e: v14e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14d(0x10000000000000000000000000000000000000000), v147(0x1)
    0x14f: v14f = AND v14e(0xffffffffffffffffffffffffffffffffffffffff), v146
    0x150: v150(0x43f) = CONST 
    0x153: JUMP v150(0x43f)

    Begin block 0x43f
    prev=[0x144], succ=[0x48a, 0x48e]
    =================================
    0x440: v440(0x2) = CONST 
    0x442: v442 = SLOAD v440(0x2)
    0x443: v443(0x40) = CONST 
    0x446: v446 = MLOAD v443(0x40)
    0x447: v447(0x25a008dd) = CONST 
    0x44c: v44c(0xe2) = CONST 
    0x44e: v44e(0x9680237400000000000000000000000000000000000000000000000000000000) = SHL v44c(0xe2), v447(0x25a008dd)
    0x450: MSTORE v446, v44e(0x9680237400000000000000000000000000000000000000000000000000000000)
    0x451: v451(0x1) = CONST 
    0x453: v453(0x1) = CONST 
    0x455: v455(0xa0) = CONST 
    0x457: v457(0x10000000000000000000000000000000000000000) = SHL v455(0xa0), v453(0x1)
    0x458: v458(0xffffffffffffffffffffffffffffffffffffffff) = SUB v457(0x10000000000000000000000000000000000000000), v451(0x1)
    0x45b: v45b = AND v458(0xffffffffffffffffffffffffffffffffffffffff), v14f
    0x45c: v45c(0x4) = CONST 
    0x45f: v45f = ADD v446, v45c(0x4)
    0x460: MSTORE v45f, v45b
    0x462: v462 = MLOAD v443(0x40)
    0x463: v463(0x0) = CONST 
    0x468: v468 = AND v458(0xffffffffffffffffffffffffffffffffffffffff), v442
    0x46a: v46a(0x96802374) = CONST 
    0x470: v470(0x24) = CONST 
    0x474: v474 = ADD v446, v470(0x24)
    0x476: v476(0x20) = CONST 
    0x47d: v47d(0x0) = SUB v446, v462
    0x47e: v47e(0x24) = ADD v47d(0x0), v470(0x24)
    0x482: v482 = EXTCODESIZE v468
    0x483: v483 = ISZERO v482
    0x485: v485 = ISZERO v483
    0x486: v486(0x48e) = CONST 
    0x489: JUMPI v486(0x48e), v485

    Begin block 0x48a
    prev=[0x43f], succ=[]
    =================================
    0x48a: v48a(0x0) = CONST 
    0x48d: REVERT v48a(0x0), v48a(0x0)

    Begin block 0x48e
    prev=[0x43f], succ=[0x499, 0x4a2]
    =================================
    0x490: v490 = GAS 
    0x491: v491 = STATICCALL v490, v468, v462, v47e(0x24), v462, v476(0x20)
    0x492: v492 = ISZERO v491
    0x494: v494 = ISZERO v492
    0x495: v495(0x4a2) = CONST 
    0x498: JUMPI v495(0x4a2), v494

    Begin block 0x499
    prev=[0x48e], succ=[]
    =================================
    0x499: v499 = RETURNDATASIZE 
    0x49a: v49a(0x0) = CONST 
    0x49d: RETURNDATACOPY v49a(0x0), v49a(0x0), v499
    0x49e: v49e = RETURNDATASIZE 
    0x49f: v49f(0x0) = CONST 
    0x4a1: REVERT v49f(0x0), v49e

    Begin block 0x4a2
    prev=[0x48e], succ=[0x4b4, 0x4b8]
    =================================
    0x4a7: v4a7(0x40) = CONST 
    0x4a9: v4a9 = MLOAD v4a7(0x40)
    0x4aa: v4aa = RETURNDATASIZE 
    0x4ab: v4ab(0x20) = CONST 
    0x4ae: v4ae = LT v4aa, v4ab(0x20)
    0x4af: v4af = ISZERO v4ae
    0x4b0: v4b0(0x4b8) = CONST 
    0x4b3: JUMPI v4b0(0x4b8), v4af

    Begin block 0x4b4
    prev=[0x4a2], succ=[]
    =================================
    0x4b4: v4b4(0x0) = CONST 
    0x4b7: REVERT v4b4(0x0), v4b4(0x0)

    Begin block 0x4b8
    prev=[0x4a2], succ=[0x4c3]
    =================================
    0x4ba: v4ba = MLOAD v4a9
    0x4bb: v4bb(0x4) = CONST 
    0x4bd: v4bd = SLOAD v4bb(0x4)
    0x4c1: v4c1(0x0) = CONST 

    Begin block 0x4c3
    prev=[0x4b8, 0x4eb], succ=[0x4cc, 0x4f3]
    =================================
    0x4c3_0x0: v4c3_0 = PHI v4c1(0x0), v4ee
    0x4c6: v4c6 = LT v4c3_0, v4bd
    0x4c7: v4c7 = ISZERO v4c6
    0x4c8: v4c8(0x4f3) = CONST 
    0x4cb: JUMPI v4c8(0x4f3), v4c7

    Begin block 0x4cc
    prev=[0x4c3], succ=[0x4eb, 0x4e2]
    =================================
    0x4cc: v4cc(0x0) = CONST 
    0x4cc_0x0: v4cc_0 = PHI v4c1(0x0), v4ee
    0x4d0: MSTORE v4cc(0x0), v4cc_0
    0x4d1: v4d1(0x3) = CONST 
    0x4d3: v4d3(0x20) = CONST 
    0x4d5: MSTORE v4d3(0x20), v4d1(0x3)
    0x4d6: v4d6(0x40) = CONST 
    0x4d9: v4d9 = SHA3 v4cc(0x0), v4d6(0x40)
    0x4da: v4da = SLOAD v4d9
    0x4dc: v4dc = LT v4ba, v4da
    0x4dd: v4dd = ISZERO v4dc
    0x4de: v4de(0x4eb) = CONST 
    0x4e1: JUMPI v4de(0x4eb), v4dd

    Begin block 0x4eb
    prev=[0x4cc], succ=[0x4c3]
    =================================
    0x4eb_0x0: v4eb_0 = PHI v4c1(0x0), v4ee
    0x4ec: v4ec(0x1) = CONST 
    0x4ee: v4ee = ADD v4ec(0x1), v4eb_0
    0x4ef: v4ef(0x4c3) = CONST 
    0x4f2: JUMP v4ef(0x4c3)

    Begin block 0x4e2
    prev=[0x4cc], succ=[0x504]
    =================================
    0x4e4: v4e4(0x504) = CONST 
    0x4ea: JUMP v4e4(0x504)

    Begin block 0x504
    prev=[0x4ff, 0x4e2], succ=[0xcf3]
    =================================
    0x508: JUMP v12f(0xcf3)

    Begin block 0xcf3
    prev=[0x504], succ=[]
    =================================
    0xcf3_0x0: vcf3_0 = PHI v4c1(0x0), v4ee, v949V4f3
    0xcf4: vcf4(0x40) = CONST 
    0xcf7: vcf7 = MLOAD vcf4(0x40)
    0xcfa: MSTORE vcf7, vcf3_0
    0xcfb: vcfb = MLOAD vcf4(0x40)
    0xcff: vcff(0x0) = SUB vcf7, vcfb
    0xd00: vd00(0x20) = CONST 
    0xd02: vd02(0x20) = ADD vd00(0x20), vcff(0x0)
    0xd04: RETURN vcfb, vd02(0x20)

    Begin block 0x4f3
    prev=[0x4c3], succ=[0x8efB0x4f3]
    =================================
    0x4f5: v4f5(0x4ff) = CONST 
    0x4f9: v4f9(0x1) = CONST 
    0x4fb: v4fb(0x8ef) = CONST 
    0x4fe: JUMP v4fb(0x8ef)

    Begin block 0x8efB0x4f3
    prev=[0x4f3], succ=[0x8faB0x4f3, 0x946B0x4f3]
    =================================
    0x8f0S0x4f3: v8f0V4f3(0x0) = CONST 
    0x8f4S0x4f3: v8f4V4f3 = GT v4f9(0x1), v4bd
    0x8f5S0x4f3: v8f5V4f3 = ISZERO v8f4V4f3
    0x8f6S0x4f3: v8f6V4f3(0x946) = CONST 
    0x8f9S0x4f3: JUMPI v8f6V4f3(0x946), v8f5V4f3

    Begin block 0x8faB0x4f3
    prev=[0x8efB0x4f3], succ=[]
    =================================
    0x8faS0x4f3: v8faV4f3(0x40) = CONST 
    0x8fdS0x4f3: v8fdV4f3 = MLOAD v8faV4f3(0x40)
    0x8feS0x4f3: v8feV4f3(0x461bcd) = CONST 
    0x902S0x4f3: v902V4f3(0xe5) = CONST 
    0x904S0x4f3: v904V4f3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v902V4f3(0xe5), v8feV4f3(0x461bcd)
    0x906S0x4f3: MSTORE v8fdV4f3, v904V4f3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x907S0x4f3: v907V4f3(0x20) = CONST 
    0x909S0x4f3: v909V4f3(0x4) = CONST 
    0x90cS0x4f3: v90cV4f3 = ADD v8fdV4f3, v909V4f3(0x4)
    0x90dS0x4f3: MSTORE v90cV4f3, v907V4f3(0x20)
    0x90eS0x4f3: v90eV4f3(0x1e) = CONST 
    0x910S0x4f3: v910V4f3(0x24) = CONST 
    0x913S0x4f3: v913V4f3 = ADD v8fdV4f3, v910V4f3(0x24)
    0x914S0x4f3: MSTORE v913V4f3, v90eV4f3(0x1e)
    0x915S0x4f3: v915V4f3(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x936S0x4f3: v936V4f3(0x44) = CONST 
    0x939S0x4f3: v939V4f3 = ADD v8fdV4f3, v936V4f3(0x44)
    0x93aS0x4f3: MSTORE v939V4f3, v915V4f3(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x93cS0x4f3: v93cV4f3 = MLOAD v8faV4f3(0x40)
    0x940S0x4f3: v940V4f3(0x0) = SUB v8fdV4f3, v93cV4f3
    0x941S0x4f3: v941V4f3(0x64) = CONST 
    0x943S0x4f3: v943V4f3(0x64) = ADD v941V4f3(0x64), v940V4f3(0x0)
    0x945S0x4f3: REVERT v93cV4f3, v943V4f3(0x64)

    Begin block 0x946B0x4f3
    prev=[0x8efB0x4f3], succ=[0x4ff]
    =================================
    0x949S0x4f3: v949V4f3 = SUB v4bd, v4f9(0x1)
    0x94bS0x4f3: JUMP v4f5(0x4ff)

    Begin block 0x4ff
    prev=[0x946B0x4f3], succ=[0x504]
    =================================

}

function tierCount()() public {
    Begin block 0x154
    prev=[], succ=[0x509]
    =================================
    0x155: v155(0xd24) = CONST 
    0x158: v158(0x509) = CONST 
    0x15b: JUMP v158(0x509)

    Begin block 0x509
    prev=[0x154], succ=[0xd24]
    =================================
    0x50a: v50a(0x4) = CONST 
    0x50c: v50c = SLOAD v50a(0x4)
    0x50e: JUMP v155(0xd24)

    Begin block 0xd24
    prev=[0x509], succ=[]
    =================================
    0xd25: vd25(0x40) = CONST 
    0xd28: vd28 = MLOAD vd25(0x40)
    0xd2b: MSTORE vd28, v50c
    0xd2c: vd2c = MLOAD vd25(0x40)
    0xd30: vd30(0x0) = SUB vd28, vd2c
    0xd31: vd31(0x20) = CONST 
    0xd33: vd33(0x20) = ADD vd31(0x20), vd30(0x0)
    0xd35: RETURN vd2c, vd33(0x20)

}

function setAlphaTiers(uint256[])() public {
    Begin block 0x15c
    prev=[], succ=[0x16e, 0x172]
    =================================
    0x15d: v15d(0xd55) = CONST 
    0x160: v160(0x4) = CONST 
    0x163: v163 = CALLDATASIZE 
    0x164: v164 = SUB v163, v160(0x4)
    0x165: v165(0x20) = CONST 
    0x168: v168 = LT v164, v165(0x20)
    0x169: v169 = ISZERO v168
    0x16a: v16a(0x172) = CONST 
    0x16d: JUMPI v16a(0x172), v169

    Begin block 0x16e
    prev=[0x15c], succ=[]
    =================================
    0x16e: v16e(0x0) = CONST 
    0x171: REVERT v16e(0x0), v16e(0x0)

    Begin block 0x172
    prev=[0x15c], succ=[0x189, 0x18d]
    =================================
    0x174: v174 = ADD v160(0x4), v164
    0x176: v176(0x20) = CONST 
    0x179: v179(0x24) = ADD v160(0x4), v176(0x20)
    0x17b: v17b = CALLDATALOAD v160(0x4)
    0x17c: v17c(0x100000000) = CONST 
    0x183: v183 = GT v17b, v17c(0x100000000)
    0x184: v184 = ISZERO v183
    0x185: v185(0x18d) = CONST 
    0x188: JUMPI v185(0x18d), v184

    Begin block 0x189
    prev=[0x172], succ=[]
    =================================
    0x189: v189(0x0) = CONST 
    0x18c: REVERT v189(0x0), v189(0x0)

    Begin block 0x18d
    prev=[0x172], succ=[0x19b, 0x19f]
    =================================
    0x18f: v18f = ADD v160(0x4), v17b
    0x191: v191(0x20) = CONST 
    0x194: v194 = ADD v18f, v191(0x20)
    0x195: v195 = GT v194, v174
    0x196: v196 = ISZERO v195
    0x197: v197(0x19f) = CONST 
    0x19a: JUMPI v197(0x19f), v196

    Begin block 0x19b
    prev=[0x18d], succ=[]
    =================================
    0x19b: v19b(0x0) = CONST 
    0x19e: REVERT v19b(0x0), v19b(0x0)

    Begin block 0x19f
    prev=[0x18d], succ=[0x1bd, 0x1c1]
    =================================
    0x1a1: v1a1 = CALLDATALOAD v18f
    0x1a3: v1a3(0x20) = CONST 
    0x1a5: v1a5 = ADD v1a3(0x20), v18f
    0x1a8: v1a8(0x20) = CONST 
    0x1ab: v1ab = MUL v1a1, v1a8(0x20)
    0x1ad: v1ad = ADD v1a5, v1ab
    0x1ae: v1ae = GT v1ad, v174
    0x1af: v1af(0x100000000) = CONST 
    0x1b6: v1b6 = GT v1a1, v1af(0x100000000)
    0x1b7: v1b7 = OR v1b6, v1ae
    0x1b8: v1b8 = ISZERO v1b7
    0x1b9: v1b9(0x1c1) = CONST 
    0x1bc: JUMPI v1b9(0x1c1), v1b8

    Begin block 0x1bd
    prev=[0x19f], succ=[]
    =================================
    0x1bd: v1bd(0x0) = CONST 
    0x1c0: REVERT v1bd(0x0), v1bd(0x0)

    Begin block 0x1c1
    prev=[0x19f], succ=[0x50f]
    =================================
    0x1c8: v1c8(0x50f) = CONST 
    0x1cb: JUMP v1c8(0x50f)

    Begin block 0x50f
    prev=[0x1c1], succ=[0x528, 0x567]
    =================================
    0x510: v510(0x0) = CONST 
    0x512: v512 = SLOAD v510(0x0)
    0x513: v513(0x10000) = CONST 
    0x518: v518 = DIV v512, v513(0x10000)
    0x519: v519(0x1) = CONST 
    0x51b: v51b(0x1) = CONST 
    0x51d: v51d(0xa0) = CONST 
    0x51f: v51f(0x10000000000000000000000000000000000000000) = SHL v51d(0xa0), v51b(0x1)
    0x520: v520(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51f(0x10000000000000000000000000000000000000000), v519(0x1)
    0x521: v521 = AND v520(0xffffffffffffffffffffffffffffffffffffffff), v518
    0x522: v522 = CALLER 
    0x523: v523 = EQ v522, v521
    0x524: v524(0x567) = CONST 
    0x527: JUMPI v524(0x567), v523

    Begin block 0x528
    prev=[0x50f], succ=[]
    =================================
    0x528: v528(0x40) = CONST 
    0x52b: v52b = MLOAD v528(0x40)
    0x52c: v52c(0x461bcd) = CONST 
    0x530: v530(0xe5) = CONST 
    0x532: v532(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v530(0xe5), v52c(0x461bcd)
    0x534: MSTORE v52b, v532(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x535: v535(0x20) = CONST 
    0x537: v537(0x4) = CONST 
    0x53a: v53a = ADD v52b, v537(0x4)
    0x53b: MSTORE v53a, v535(0x20)
    0x53c: v53c(0x10) = CONST 
    0x53e: v53e(0x24) = CONST 
    0x541: v541 = ADD v52b, v53e(0x24)
    0x542: MSTORE v541, v53c(0x10)
    0x543: v543(0x3737ba103a34329033b7bb32b93737b9) = CONST 
    0x554: v554(0x81) = CONST 
    0x556: v556(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000) = SHL v554(0x81), v543(0x3737ba103a34329033b7bb32b93737b9)
    0x557: v557(0x44) = CONST 
    0x55a: v55a = ADD v52b, v557(0x44)
    0x55b: MSTORE v55a, v556(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000)
    0x55d: v55d = MLOAD v528(0x40)
    0x561: v561(0x0) = SUB v52b, v55d
    0x562: v562(0x64) = CONST 
    0x564: v564(0x64) = ADD v562(0x64), v561(0x0)
    0x566: REVERT v55d, v564(0x64)

    Begin block 0x567
    prev=[0x50f], succ=[0x56a]
    =================================
    0x568: v568(0x0) = CONST 

    Begin block 0x56a
    prev=[0x567, 0x68b], succ=[0x6b2, 0x573]
    =================================
    0x56a_0x0: v56a_0 = PHI v568(0x0), v6ad
    0x56d: v56d = LT v56a_0, v1a1
    0x56e: v56e = ISZERO v56d
    0x56f: v56f(0x6b2) = CONST 
    0x572: JUMPI v56f(0x6b2), v56e

    Begin block 0x6b2
    prev=[0x56a], succ=[0x6b8]
    =================================
    0x6b4: v6b4(0x4) = CONST 
    0x6b6: v6b6 = SLOAD v6b4(0x4)

    Begin block 0x6b8
    prev=[0x6c1, 0x6b2], succ=[0x6c1, 0x70e]
    =================================
    0x6b8_0x0: v6b8_0 = PHI v1a1, v709
    0x6bb: v6bb = LT v6b8_0, v6b6
    0x6bc: v6bc = ISZERO v6bb
    0x6bd: v6bd(0x70e) = CONST 
    0x6c0: JUMPI v6bd(0x70e), v6bc

    Begin block 0x6c1
    prev=[0x6b8], succ=[0x6b8]
    =================================
    0x6c1: v6c1(0x0) = CONST 
    0x6c1_0x0: v6c1_0 = PHI v1a1, v709
    0x6c5: MSTORE v6c1(0x0), v6c1_0
    0x6c6: v6c6(0x3) = CONST 
    0x6c8: v6c8(0x20) = CONST 
    0x6cc: MSTORE v6c8(0x20), v6c6(0x3)
    0x6cd: v6cd(0x40) = CONST 
    0x6d1: v6d1 = SHA3 v6c1(0x0), v6cd(0x40)
    0x6d5: SSTORE v6d1, v6c1(0x0)
    0x6d7: v6d7 = MLOAD v6cd(0x40)
    0x6da: MSTORE v6d7, v6c1_0
    0x6dc: v6dc = MLOAD v6cd(0x40)
    0x6dd: v6dd(0x5d93be647247f58499480ae6f19f9657c2d03baa86971a0a1aa77f11ab949cab) = CONST 
    0x701: v701(0x0) = SUB v6d7, v6dc
    0x704: v704(0x20) = ADD v6c8(0x20), v701(0x0)
    0x706: LOG1 v6dc, v704(0x20), v6dd(0x5d93be647247f58499480ae6f19f9657c2d03baa86971a0a1aa77f11ab949cab)
    0x707: v707(0x1) = CONST 
    0x709: v709 = ADD v707(0x1), v6c1_0
    0x70a: v70a(0x6b8) = CONST 
    0x70d: JUMP v70a(0x6b8)

    Begin block 0x70e
    prev=[0x6b8], succ=[0xd55]
    =================================
    0x711: v711(0x4) = CONST 
    0x713: SSTORE v711(0x4), v1a1
    0x715: JUMP v15d(0xd55)

    Begin block 0xd55
    prev=[0x70e], succ=[]
    =================================
    0xd56: STOP 

    Begin block 0x573
    prev=[0x56a], succ=[0x5e2, 0x579]
    =================================
    0x573_0x0: v573_0 = PHI v568(0x0), v6ad
    0x574: v574 = ISZERO v573_0
    0x575: v575(0x5e2) = CONST 
    0x578: JUMPI v575(0x5e2), v574

    Begin block 0x5e2
    prev=[0x573], succ=[0x5ef, 0x5f0]
    =================================
    0x5e2_0x0: v5e2_0 = PHI v568(0x0), v6ad
    0x5e3: v5e3(0x0) = CONST 
    0x5ea: v5ea = LT v5e2_0, v1a1
    0x5eb: v5eb(0x5f0) = CONST 
    0x5ee: JUMPI v5eb(0x5f0), v5ea

    Begin block 0x5ef
    prev=[0x5e2], succ=[]
    =================================
    0x5ef: THROW 

    Begin block 0x5f0
    prev=[0x5e2], succ=[0x5fd, 0x633]
    =================================
    0x5f0_0x0: v5f0_0 = PHI v568(0x0), v6ad
    0x5f3: v5f3(0x20) = CONST 
    0x5f5: v5f5 = MUL v5f3(0x20), v5f0_0
    0x5f6: v5f6 = ADD v5f5, v1a5
    0x5f7: v5f7 = CALLDATALOAD v5f6
    0x5f8: v5f8 = GT v5f7, v5e3(0x0)
    0x5f9: v5f9(0x633) = CONST 
    0x5fc: JUMPI v5f9(0x633), v5f8

    Begin block 0x5fd
    prev=[0x5f0], succ=[]
    =================================
    0x5fd: v5fd(0x40) = CONST 
    0x5ff: v5ff = MLOAD v5fd(0x40)
    0x600: v600(0x461bcd) = CONST 
    0x604: v604(0xe5) = CONST 
    0x606: v606(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v604(0xe5), v600(0x461bcd)
    0x608: MSTORE v5ff, v606(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x609: v609(0x4) = CONST 
    0x60b: v60b = ADD v609(0x4), v5ff
    0x60e: v60e(0x20) = CONST 
    0x610: v610 = ADD v60e(0x20), v60b
    0x613: v613(0x20) = SUB v610, v60b
    0x615: MSTORE v60b, v613(0x20)
    0x616: v616(0x33) = CONST 
    0x619: MSTORE v610, v616(0x33)
    0x61a: v61a(0x20) = CONST 
    0x61c: v61c = ADD v61a(0x20), v610
    0x61e: v61e(0xa96) = CONST 
    0x621: v621(0x33) = CONST 
    0x624: CODECOPY v61c, v61e(0xa96), v621(0x33)
    0x625: v625(0x40) = CONST 
    0x627: v627 = ADD v625(0x40), v61c
    0x62b: v62b(0x40) = CONST 
    0x62d: v62d = MLOAD v62b(0x40)
    0x630: v630(0x84) = SUB v627, v62d
    0x632: REVERT v62d, v630(0x84)

    Begin block 0x633
    prev=[0x5dd, 0x5f0], succ=[0x63e, 0x63f]
    =================================
    0x633_0x0: v633_0 = PHI v568(0x0), v6ad
    0x639: v639 = LT v633_0, v1a1
    0x63a: v63a(0x63f) = CONST 
    0x63d: JUMPI v63a(0x63f), v639

    Begin block 0x63e
    prev=[0x633], succ=[]
    =================================
    0x63e: THROW 

    Begin block 0x63f
    prev=[0x633], succ=[0x68a, 0x68b]
    =================================
    0x63f_0x0: v63f_0 = PHI v568(0x0), v6ad
    0x63f_0x3: v63f_3 = PHI v568(0x0), v6ad
    0x642: v642(0x20) = CONST 
    0x644: v644 = MUL v642(0x20), v63f_0
    0x645: v645 = ADD v644, v1a5
    0x646: v646 = CALLDATALOAD v645
    0x647: v647(0x3) = CONST 
    0x649: v649(0x0) = CONST 
    0x64d: MSTORE v649(0x0), v63f_3
    0x64e: v64e(0x20) = CONST 
    0x650: v650(0x20) = ADD v64e(0x20), v649(0x0)
    0x653: MSTORE v650(0x20), v647(0x3)
    0x654: v654(0x20) = CONST 
    0x656: v656(0x40) = ADD v654(0x20), v650(0x20)
    0x657: v657(0x0) = CONST 
    0x659: v659 = SHA3 v657(0x0), v656(0x40)
    0x65c: SSTORE v659, v646
    0x65e: v65e(0x7c0334032b954d80a1d4a83a08ebf0a99d835c40143beec06f14106526167fd0) = CONST 
    0x685: v685 = LT v63f_3, v1a1
    0x686: v686(0x68b) = CONST 
    0x689: JUMPI v686(0x68b), v685

    Begin block 0x68a
    prev=[0x63f], succ=[]
    =================================
    0x68a: THROW 

    Begin block 0x68b
    prev=[0x63f], succ=[0x56a]
    =================================
    0x68b_0x0: v68b_0 = PHI v568(0x0), v6ad
    0x68b_0x3: v68b_3 = PHI v568(0x0), v6ad
    0x68b_0x5: v68b_5 = PHI v568(0x0), v6ad
    0x68c: v68c(0x40) = CONST 
    0x68f: v68f = MLOAD v68c(0x40)
    0x692: MSTORE v68f, v68b_3
    0x693: v693(0x20) = CONST 
    0x697: v697 = MUL v693(0x20), v68b_0
    0x69b: v69b = ADD v697, v1a5
    0x69c: v69c = CALLDATALOAD v69b
    0x69f: v69f = ADD v68f, v693(0x20)
    0x6a0: MSTORE v69f, v69c
    0x6a3: v6a3 = MLOAD v68c(0x40)
    0x6a7: v6a7(0x0) = SUB v68f, v6a3
    0x6a8: v6a8(0x40) = ADD v6a7(0x0), v68c(0x40)
    0x6aa: LOG1 v6a3, v6a8(0x40), v65e(0x7c0334032b954d80a1d4a83a08ebf0a99d835c40143beec06f14106526167fd0)
    0x6ab: v6ab(0x1) = CONST 
    0x6ad: v6ad = ADD v6ab(0x1), v68b_5
    0x6ae: v6ae(0x56a) = CONST 
    0x6b1: JUMP v6ae(0x56a)

    Begin block 0x579
    prev=[0x573], succ=[0x586, 0x587]
    =================================
    0x579_0x0: v579_0 = PHI v568(0x0), v6ad
    0x57b: v57b(0x1) = CONST 
    0x57e: v57e = SUB v579_0, v57b(0x1)
    0x581: v581 = LT v57e, v1a1
    0x582: v582(0x587) = CONST 
    0x585: JUMPI v582(0x587), v581

    Begin block 0x586
    prev=[0x579], succ=[]
    =================================
    0x586: THROW 

    Begin block 0x587
    prev=[0x579], succ=[0x599, 0x59a]
    =================================
    0x587_0x3: v587_3 = PHI v568(0x0), v6ad
    0x58a: v58a(0x20) = CONST 
    0x58c: v58c = MUL v58a(0x20), v57e
    0x58d: v58d = ADD v58c, v1a5
    0x58e: v58e = CALLDATALOAD v58d
    0x594: v594 = LT v587_3, v1a1
    0x595: v595(0x59a) = CONST 
    0x598: JUMPI v595(0x59a), v594

    Begin block 0x599
    prev=[0x587], succ=[]
    =================================
    0x599: THROW 

    Begin block 0x59a
    prev=[0x587], succ=[0x5a7, 0x5dd]
    =================================
    0x59a_0x0: v59a_0 = PHI v568(0x0), v6ad
    0x59d: v59d(0x20) = CONST 
    0x59f: v59f = MUL v59d(0x20), v59a_0
    0x5a0: v5a0 = ADD v59f, v1a5
    0x5a1: v5a1 = CALLDATALOAD v5a0
    0x5a2: v5a2 = GT v5a1, v58e
    0x5a3: v5a3(0x5dd) = CONST 
    0x5a6: JUMPI v5a3(0x5dd), v5a2

    Begin block 0x5a7
    prev=[0x59a], succ=[]
    =================================
    0x5a7: v5a7(0x40) = CONST 
    0x5a9: v5a9 = MLOAD v5a7(0x40)
    0x5aa: v5aa(0x461bcd) = CONST 
    0x5ae: v5ae(0xe5) = CONST 
    0x5b0: v5b0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5ae(0xe5), v5aa(0x461bcd)
    0x5b2: MSTORE v5a9, v5b0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5b3: v5b3(0x4) = CONST 
    0x5b5: v5b5 = ADD v5b3(0x4), v5a9
    0x5b8: v5b8(0x20) = CONST 
    0x5ba: v5ba = ADD v5b8(0x20), v5b5
    0x5bd: v5bd(0x20) = SUB v5ba, v5b5
    0x5bf: MSTORE v5b5, v5bd(0x20)
    0x5c0: v5c0(0x38) = CONST 
    0x5c3: MSTORE v5ba, v5c0(0x38)
    0x5c4: v5c4(0x20) = CONST 
    0x5c6: v5c6 = ADD v5c4(0x20), v5ba
    0x5c8: v5c8(0xaf7) = CONST 
    0x5cb: v5cb(0x38) = CONST 
    0x5ce: CODECOPY v5c6, v5c8(0xaf7), v5cb(0x38)
    0x5cf: v5cf(0x40) = CONST 
    0x5d1: v5d1 = ADD v5cf(0x40), v5c6
    0x5d5: v5d5(0x40) = CONST 
    0x5d7: v5d7 = MLOAD v5d5(0x40)
    0x5da: v5da(0x84) = SUB v5d1, v5d7
    0x5dc: REVERT v5d7, v5da(0x84)

    Begin block 0x5dd
    prev=[0x59a], succ=[0x633]
    =================================
    0x5de: v5de(0x633) = CONST 
    0x5e1: JUMP v5de(0x633)

}

function initialize(address)() public {
    Begin block 0x1cc
    prev=[], succ=[0x1de, 0x1e2]
    =================================
    0x1cd: v1cd(0xd76) = CONST 
    0x1d0: v1d0(0x4) = CONST 
    0x1d3: v1d3 = CALLDATASIZE 
    0x1d4: v1d4 = SUB v1d3, v1d0(0x4)
    0x1d5: v1d5(0x20) = CONST 
    0x1d8: v1d8 = LT v1d4, v1d5(0x20)
    0x1d9: v1d9 = ISZERO v1d8
    0x1da: v1da(0x1e2) = CONST 
    0x1dd: JUMPI v1da(0x1e2), v1d9

    Begin block 0x1de
    prev=[0x1cc], succ=[]
    =================================
    0x1de: v1de(0x0) = CONST 
    0x1e1: REVERT v1de(0x0), v1de(0x0)

    Begin block 0x1e2
    prev=[0x1cc], succ=[0x716]
    =================================
    0x1e4: v1e4 = CALLDATALOAD v1d0(0x4)
    0x1e5: v1e5(0x1) = CONST 
    0x1e7: v1e7(0x1) = CONST 
    0x1e9: v1e9(0xa0) = CONST 
    0x1eb: v1eb(0x10000000000000000000000000000000000000000) = SHL v1e9(0xa0), v1e7(0x1)
    0x1ec: v1ec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1eb(0x10000000000000000000000000000000000000000), v1e5(0x1)
    0x1ed: v1ed = AND v1ec(0xffffffffffffffffffffffffffffffffffffffff), v1e4
    0x1ee: v1ee(0x716) = CONST 
    0x1f1: JUMP v1ee(0x716)

    Begin block 0x716
    prev=[0x1e2], succ=[0x72f, 0x727]
    =================================
    0x717: v717(0x0) = CONST 
    0x719: v719 = SLOAD v717(0x0)
    0x71a: v71a(0x100) = CONST 
    0x71e: v71e = DIV v719, v71a(0x100)
    0x71f: v71f(0xff) = CONST 
    0x721: v721 = AND v71f(0xff), v71e
    0x723: v723(0x72f) = CONST 
    0x726: JUMPI v723(0x72f), v721

    Begin block 0x72f
    prev=[0x716, 0x957B0x727], succ=[0x73d, 0x735]
    =================================
    0x72f_0x0: v72f_0 = PHI v721, v958V727
    0x731: v731(0x73d) = CONST 
    0x734: JUMPI v731(0x73d), v72f_0

    Begin block 0x73d
    prev=[0x72f, 0x735], succ=[0x742, 0x778]
    =================================
    0x73d_0x0: v73d_0 = PHI v721, v73c, v958V727
    0x73e: v73e(0x778) = CONST 
    0x741: JUMPI v73e(0x778), v73d_0

    Begin block 0x742
    prev=[0x73d], succ=[]
    =================================
    0x742: v742(0x40) = CONST 
    0x744: v744 = MLOAD v742(0x40)
    0x745: v745(0x461bcd) = CONST 
    0x749: v749(0xe5) = CONST 
    0x74b: v74b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v749(0xe5), v745(0x461bcd)
    0x74d: MSTORE v744, v74b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x74e: v74e(0x4) = CONST 
    0x750: v750 = ADD v74e(0x4), v744
    0x753: v753(0x20) = CONST 
    0x755: v755 = ADD v753(0x20), v750
    0x758: v758(0x20) = SUB v755, v750
    0x75a: MSTORE v750, v758(0x20)
    0x75b: v75b(0x2e) = CONST 
    0x75e: MSTORE v755, v75b(0x2e)
    0x75f: v75f(0x20) = CONST 
    0x761: v761 = ADD v75f(0x20), v755
    0x763: v763(0xac9) = CONST 
    0x766: v766(0x2e) = CONST 
    0x769: CODECOPY v761, v763(0xac9), v766(0x2e)
    0x76a: v76a(0x40) = CONST 
    0x76c: v76c = ADD v76a(0x40), v761
    0x770: v770(0x40) = CONST 
    0x772: v772 = MLOAD v770(0x40)
    0x775: v775(0x84) = SUB v76c, v772
    0x777: REVERT v772, v775(0x84)

    Begin block 0x778
    prev=[0x73d], succ=[0x78b, 0x7a3]
    =================================
    0x779: v779(0x0) = CONST 
    0x77b: v77b = SLOAD v779(0x0)
    0x77c: v77c(0x100) = CONST 
    0x780: v780 = DIV v77b, v77c(0x100)
    0x781: v781(0xff) = CONST 
    0x783: v783 = AND v781(0xff), v780
    0x784: v784 = ISZERO v783
    0x786: v786 = ISZERO v784
    0x787: v787(0x7a3) = CONST 
    0x78a: JUMPI v787(0x7a3), v786

    Begin block 0x78b
    prev=[0x778], succ=[0x7a3]
    =================================
    0x78b: v78b(0x0) = CONST 
    0x78e: v78e = SLOAD v78b(0x0)
    0x78f: v78f(0xff) = CONST 
    0x791: v791(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v78f(0xff)
    0x792: v792(0xff00) = CONST 
    0x795: v795(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v792(0xff00)
    0x798: v798 = AND v78e, v795(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x799: v799(0x100) = CONST 
    0x79c: v79c = OR v799(0x100), v798
    0x79d: v79d = AND v79c, v791(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x79e: v79e(0x1) = CONST 
    0x7a0: v7a0 = OR v79e(0x1), v79d
    0x7a2: SSTORE v78b(0x0), v7a0

    Begin block 0x7a3
    prev=[0x78b, 0x778], succ=[0x95dB0x7a3]
    =================================
    0x7a4: v7a4(0x7ab) = CONST 
    0x7a7: v7a7(0x95d) = CONST 
    0x7aa: JUMP v7a7(0x95d), v7a4(0x7ab)

    Begin block 0x95dB0x7a3
    prev=[0x7a3], succ=[0x976B0x7a3, 0x96eB0x7a3]
    =================================
    0x95eS0x7a3: v95eV7a3(0x0) = CONST 
    0x960S0x7a3: v960V7a3 = SLOAD v95eV7a3(0x0)
    0x961S0x7a3: v961V7a3(0x100) = CONST 
    0x965S0x7a3: v965V7a3 = DIV v960V7a3, v961V7a3(0x100)
    0x966S0x7a3: v966V7a3(0xff) = CONST 
    0x968S0x7a3: v968V7a3 = AND v966V7a3(0xff), v965V7a3
    0x96aS0x7a3: v96aV7a3(0x976) = CONST 
    0x96dS0x7a3: JUMPI v96aV7a3(0x976), v968V7a3

    Begin block 0x976B0x7a3
    prev=[0x95dB0x7a3, 0x957B0x96eB0x7a3], succ=[0x984B0x7a3, 0x97cB0x7a3]
    =================================
    0x976_0x0S0x7a3: v976_0V7a3 = PHI v968V7a3, v958V96eV7a3
    0x978S0x7a3: v978V7a3(0x984) = CONST 
    0x97bS0x7a3: JUMPI v978V7a3(0x984), v976_0V7a3

    Begin block 0x984B0x7a3
    prev=[0x976B0x7a3, 0x97cB0x7a3], succ=[0x989B0x7a3, 0x9bfB0x7a3]
    =================================
    0x984_0x0S0x7a3: v984_0V7a3 = PHI v968V7a3, v983V7a3, v958V96eV7a3
    0x985S0x7a3: v985V7a3(0x9bf) = CONST 
    0x988S0x7a3: JUMPI v985V7a3(0x9bf), v984_0V7a3

    Begin block 0x989B0x7a3
    prev=[0x984B0x7a3], succ=[]
    =================================
    0x989S0x7a3: v989V7a3(0x40) = CONST 
    0x98bS0x7a3: v98bV7a3 = MLOAD v989V7a3(0x40)
    0x98cS0x7a3: v98cV7a3(0x461bcd) = CONST 
    0x990S0x7a3: v990V7a3(0xe5) = CONST 
    0x992S0x7a3: v992V7a3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v990V7a3(0xe5), v98cV7a3(0x461bcd)
    0x994S0x7a3: MSTORE v98bV7a3, v992V7a3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x995S0x7a3: v995V7a3(0x4) = CONST 
    0x997S0x7a3: v997V7a3 = ADD v995V7a3(0x4), v98bV7a3
    0x99aS0x7a3: v99aV7a3(0x20) = CONST 
    0x99cS0x7a3: v99cV7a3 = ADD v99aV7a3(0x20), v997V7a3
    0x99fS0x7a3: v99fV7a3(0x20) = SUB v99cV7a3, v997V7a3
    0x9a1S0x7a3: MSTORE v997V7a3, v99fV7a3(0x20)
    0x9a2S0x7a3: v9a2V7a3(0x2e) = CONST 
    0x9a5S0x7a3: MSTORE v99cV7a3, v9a2V7a3(0x2e)
    0x9a6S0x7a3: v9a6V7a3(0x20) = CONST 
    0x9a8S0x7a3: v9a8V7a3 = ADD v9a6V7a3(0x20), v99cV7a3
    0x9aaS0x7a3: v9aaV7a3(0xac9) = CONST 
    0x9adS0x7a3: v9adV7a3(0x2e) = CONST 
    0x9b0S0x7a3: CODECOPY v9a8V7a3, v9aaV7a3(0xac9), v9adV7a3(0x2e)
    0x9b1S0x7a3: v9b1V7a3(0x40) = CONST 
    0x9b3S0x7a3: v9b3V7a3 = ADD v9b1V7a3(0x40), v9a8V7a3
    0x9b7S0x7a3: v9b7V7a3(0x40) = CONST 
    0x9b9S0x7a3: v9b9V7a3 = MLOAD v9b7V7a3(0x40)
    0x9bcS0x7a3: v9bcV7a3(0x84) = SUB v9b3V7a3, v9b9V7a3
    0x9beS0x7a3: REVERT v9b9V7a3, v9bcV7a3(0x84)

    Begin block 0x9bfB0x7a3
    prev=[0x984B0x7a3], succ=[0x9d2B0x7a3, 0x9eaB0x7a3]
    =================================
    0x9c0S0x7a3: v9c0V7a3(0x0) = CONST 
    0x9c2S0x7a3: v9c2V7a3 = SLOAD v9c0V7a3(0x0)
    0x9c3S0x7a3: v9c3V7a3(0x100) = CONST 
    0x9c7S0x7a3: v9c7V7a3 = DIV v9c2V7a3, v9c3V7a3(0x100)
    0x9c8S0x7a3: v9c8V7a3(0xff) = CONST 
    0x9caS0x7a3: v9caV7a3 = AND v9c8V7a3(0xff), v9c7V7a3
    0x9cbS0x7a3: v9cbV7a3 = ISZERO v9caV7a3
    0x9cdS0x7a3: v9cdV7a3 = ISZERO v9cbV7a3
    0x9ceS0x7a3: v9ceV7a3(0x9ea) = CONST 
    0x9d1S0x7a3: JUMPI v9ceV7a3(0x9ea), v9cdV7a3

    Begin block 0x9d2B0x7a3
    prev=[0x9bfB0x7a3], succ=[0x9eaB0x7a3]
    =================================
    0x9d2S0x7a3: v9d2V7a3(0x0) = CONST 
    0x9d5S0x7a3: v9d5V7a3 = SLOAD v9d2V7a3(0x0)
    0x9d6S0x7a3: v9d6V7a3(0xff) = CONST 
    0x9d8S0x7a3: v9d8V7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9d6V7a3(0xff)
    0x9d9S0x7a3: v9d9V7a3(0xff00) = CONST 
    0x9dcS0x7a3: v9dcV7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v9d9V7a3(0xff00)
    0x9dfS0x7a3: v9dfV7a3 = AND v9d5V7a3, v9dcV7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x9e0S0x7a3: v9e0V7a3(0x100) = CONST 
    0x9e3S0x7a3: v9e3V7a3 = OR v9e0V7a3(0x100), v9dfV7a3
    0x9e4S0x7a3: v9e4V7a3 = AND v9e3V7a3, v9d8V7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x9e5S0x7a3: v9e5V7a3(0x1) = CONST 
    0x9e7S0x7a3: v9e7V7a3 = OR v9e5V7a3(0x1), v9e4V7a3
    0x9e9S0x7a3: SSTORE v9d2V7a3(0x0), v9e7V7a3

    Begin block 0x9eaB0x7a3
    prev=[0x9d2B0x7a3, 0x9bfB0x7a3], succ=[0xa1aB0x7a3, 0xa25B0x7a3]
    =================================
    0x9ebS0x7a3: v9ebV7a3(0x0) = CONST 
    0x9eeS0x7a3: v9eeV7a3 = SLOAD v9ebV7a3(0x0)
    0x9efS0x7a3: v9efV7a3(0x10000) = CONST 
    0x9f3S0x7a3: v9f3V7a3(0x1) = CONST 
    0x9f5S0x7a3: v9f5V7a3(0xb0) = CONST 
    0x9f7S0x7a3: v9f7V7a3(0x100000000000000000000000000000000000000000000) = SHL v9f5V7a3(0xb0), v9f3V7a3(0x1)
    0x9f8S0x7a3: v9f8V7a3(0xffffffffffffffffffffffffffffffffffffffff0000) = SUB v9f7V7a3(0x100000000000000000000000000000000000000000000), v9efV7a3(0x10000)
    0x9f9S0x7a3: v9f9V7a3(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT v9f8V7a3(0xffffffffffffffffffffffffffffffffffffffff0000)
    0x9faS0x7a3: v9faV7a3 = AND v9f9V7a3(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff), v9eeV7a3
    0x9fbS0x7a3: v9fbV7a3 = CALLER 
    0x9fcS0x7a3: v9fcV7a3(0x10000) = CONST 
    0xa00S0x7a3: va00V7a3 = MUL v9fcV7a3(0x10000), v9fbV7a3
    0xa01S0x7a3: va01V7a3 = OR va00V7a3, v9faV7a3
    0xa03S0x7a3: SSTORE v9ebV7a3(0x0), va01V7a3
    0xa04S0x7a3: va04V7a3(0x1) = CONST 
    0xa07S0x7a3: va07V7a3 = SLOAD va04V7a3(0x1)
    0xa08S0x7a3: va08V7a3(0x1) = CONST 
    0xa0aS0x7a3: va0aV7a3(0x1) = CONST 
    0xa0cS0x7a3: va0cV7a3(0xa0) = CONST 
    0xa0eS0x7a3: va0eV7a3(0x10000000000000000000000000000000000000000) = SHL va0cV7a3(0xa0), va0aV7a3(0x1)
    0xa0fS0x7a3: va0fV7a3(0xffffffffffffffffffffffffffffffffffffffff) = SUB va0eV7a3(0x10000000000000000000000000000000000000000), va08V7a3(0x1)
    0xa10S0x7a3: va10V7a3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va0fV7a3(0xffffffffffffffffffffffffffffffffffffffff)
    0xa11S0x7a3: va11V7a3 = AND va10V7a3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va07V7a3
    0xa13S0x7a3: SSTORE va04V7a3(0x1), va11V7a3
    0xa15S0x7a3: va15V7a3 = ISZERO v9cbV7a3
    0xa16S0x7a3: va16V7a3(0xa25) = CONST 
    0xa19S0x7a3: JUMPI va16V7a3(0xa25), va15V7a3

    Begin block 0xa1aB0x7a3
    prev=[0x9eaB0x7a3], succ=[0xa25B0x7a3]
    =================================
    0xa1aS0x7a3: va1aV7a3(0x0) = CONST 
    0xa1dS0x7a3: va1dV7a3 = SLOAD va1aV7a3(0x0)
    0xa1eS0x7a3: va1eV7a3(0xff00) = CONST 
    0xa21S0x7a3: va21V7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT va1eV7a3(0xff00)
    0xa22S0x7a3: va22V7a3 = AND va21V7a3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), va1dV7a3
    0xa24S0x7a3: SSTORE va1aV7a3(0x0), va22V7a3

    Begin block 0xa25B0x7a3
    prev=[0xa1aB0x7a3, 0x9eaB0x7a3], succ=[0x7ab]
    =================================
    0xa27S0x7a3: JUMP v7a4(0x7ab)

    Begin block 0x7ab
    prev=[0xa25B0x7a3], succ=[0x7cd, 0x7d8]
    =================================
    0x7ac: v7ac(0x2) = CONST 
    0x7af: v7af = SLOAD v7ac(0x2)
    0x7b0: v7b0(0x1) = CONST 
    0x7b2: v7b2(0x1) = CONST 
    0x7b4: v7b4(0xa0) = CONST 
    0x7b6: v7b6(0x10000000000000000000000000000000000000000) = SHL v7b4(0xa0), v7b2(0x1)
    0x7b7: v7b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b6(0x10000000000000000000000000000000000000000), v7b0(0x1)
    0x7b8: v7b8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v7b7(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b9: v7b9 = AND v7b8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v7af
    0x7ba: v7ba(0x1) = CONST 
    0x7bc: v7bc(0x1) = CONST 
    0x7be: v7be(0xa0) = CONST 
    0x7c0: v7c0(0x10000000000000000000000000000000000000000) = SHL v7be(0xa0), v7bc(0x1)
    0x7c1: v7c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c0(0x10000000000000000000000000000000000000000), v7ba(0x1)
    0x7c3: v7c3 = AND v1ed, v7c1(0xffffffffffffffffffffffffffffffffffffffff)
    0x7c4: v7c4 = OR v7c3, v7b9
    0x7c6: SSTORE v7ac(0x2), v7c4
    0x7c8: v7c8 = ISZERO v784
    0x7c9: v7c9(0x7d8) = CONST 
    0x7cc: JUMPI v7c9(0x7d8), v7c8

    Begin block 0x7cd
    prev=[0x7ab], succ=[0x7d8]
    =================================
    0x7cd: v7cd(0x0) = CONST 
    0x7d0: v7d0 = SLOAD v7cd(0x0)
    0x7d1: v7d1(0xff00) = CONST 
    0x7d4: v7d4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v7d1(0xff00)
    0x7d5: v7d5 = AND v7d4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v7d0
    0x7d7: SSTORE v7cd(0x0), v7d5

    Begin block 0x7d8
    prev=[0x7cd, 0x7ab], succ=[0xd76]
    =================================
    0x7db: JUMP v1cd(0xd76)

    Begin block 0xd76
    prev=[0x7d8], succ=[]
    =================================
    0xd77: STOP 

    Begin block 0x97cB0x7a3
    prev=[0x976B0x7a3], succ=[0x984B0x7a3]
    =================================
    0x97dS0x7a3: v97dV7a3(0x0) = CONST 
    0x97fS0x7a3: v97fV7a3 = SLOAD v97dV7a3(0x0)
    0x980S0x7a3: v980V7a3(0xff) = CONST 
    0x982S0x7a3: v982V7a3 = AND v980V7a3(0xff), v97fV7a3
    0x983S0x7a3: v983V7a3 = ISZERO v982V7a3

    Begin block 0x96eB0x7a3
    prev=[0x95dB0x7a3], succ=[0x94cB0x96eB0x7a3]
    =================================
    0x96fS0x7a3: v96fV7a3(0x976) = CONST 
    0x972S0x7a3: v972V7a3(0x94c) = CONST 
    0x975S0x7a3: JUMP v972V7a3(0x94c)

    Begin block 0x94cB0x96eB0x7a3
    prev=[0x96eB0x7a3], succ=[0xa28B0x96eB0x7a3]
    =================================
    0x94dS0x96eS0x7a3: v94dV96eV7a3(0x0) = CONST 
    0x94fS0x96eS0x7a3: v94fV96eV7a3(0x957) = CONST 
    0x952S0x96eS0x7a3: v952V96eV7a3 = ADDRESS 
    0x953S0x96eS0x7a3: v953V96eV7a3(0xa28) = CONST 
    0x956S0x96eS0x7a3: JUMP v953V96eV7a3(0xa28)

    Begin block 0xa28B0x96eB0x7a3
    prev=[0x94cB0x96eB0x7a3], succ=[0x957B0x96eB0x7a3]
    =================================
    0xa29S0x96eS0x7a3: va29V96eV7a3 = EXTCODESIZE v952V96eV7a3
    0xa2aS0x96eS0x7a3: va2aV96eV7a3 = ISZERO va29V96eV7a3
    0xa2bS0x96eS0x7a3: va2bV96eV7a3 = ISZERO va2aV96eV7a3
    0xa2dS0x96eS0x7a3: JUMP v94fV96eV7a3(0x957)

    Begin block 0x957B0x96eB0x7a3
    prev=[0xa28B0x96eB0x7a3], succ=[0x976B0x7a3]
    =================================
    0x958S0x96eS0x7a3: v958V96eV7a3 = ISZERO va2bV96eV7a3
    0x95cS0x96eS0x7a3: JUMP v96fV7a3(0x976)

    Begin block 0x735
    prev=[0x72f], succ=[0x73d]
    =================================
    0x736: v736(0x0) = CONST 
    0x738: v738 = SLOAD v736(0x0)
    0x739: v739(0xff) = CONST 
    0x73b: v73b = AND v739(0xff), v738
    0x73c: v73c = ISZERO v73b

    Begin block 0x727
    prev=[0x716], succ=[0x94cB0x727]
    =================================
    0x728: v728(0x72f) = CONST 
    0x72b: v72b(0x94c) = CONST 
    0x72e: JUMP v72b(0x94c)

    Begin block 0x94cB0x727
    prev=[0x727], succ=[0xa28B0x727]
    =================================
    0x94dS0x727: v94dV727(0x0) = CONST 
    0x94fS0x727: v94fV727(0x957) = CONST 
    0x952S0x727: v952V727 = ADDRESS 
    0x953S0x727: v953V727(0xa28) = CONST 
    0x956S0x727: JUMP v953V727(0xa28)

    Begin block 0xa28B0x727
    prev=[0x94cB0x727], succ=[0x957B0x727]
    =================================
    0xa29S0x727: va29V727 = EXTCODESIZE v952V727
    0xa2aS0x727: va2aV727 = ISZERO va29V727
    0xa2bS0x727: va2bV727 = ISZERO va2aV727
    0xa2dS0x727: JUMP v94fV727(0x957)

    Begin block 0x957B0x727
    prev=[0xa28B0x727], succ=[0x72f]
    =================================
    0x958S0x727: v958V727 = ISZERO va2bV727
    0x95cS0x727: JUMP v728(0x72f)

}

function pendingGovernor()() public {
    Begin block 0x1f2
    prev=[], succ=[0x7dc]
    =================================
    0x1f3: v1f3(0xd97) = CONST 
    0x1f6: v1f6(0x7dc) = CONST 
    0x1f9: JUMP v1f6(0x7dc)

    Begin block 0x7dc
    prev=[0x1f2], succ=[0xd97]
    =================================
    0x7dd: v7dd(0x1) = CONST 
    0x7df: v7df = SLOAD v7dd(0x1)
    0x7e0: v7e0(0x1) = CONST 
    0x7e2: v7e2(0x1) = CONST 
    0x7e4: v7e4(0xa0) = CONST 
    0x7e6: v7e6(0x10000000000000000000000000000000000000000) = SHL v7e4(0xa0), v7e2(0x1)
    0x7e7: v7e7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7e6(0x10000000000000000000000000000000000000000), v7e0(0x1)
    0x7e8: v7e8 = AND v7e7(0xffffffffffffffffffffffffffffffffffffffff), v7df
    0x7ea: JUMP v1f3(0xd97)

    Begin block 0xd97
    prev=[0x7dc], succ=[]
    =================================
    0xd98: vd98(0x40) = CONST 
    0xd9b: vd9b = MLOAD vd98(0x40)
    0xd9c: vd9c(0x1) = CONST 
    0xd9e: vd9e(0x1) = CONST 
    0xda0: vda0(0xa0) = CONST 
    0xda2: vda2(0x10000000000000000000000000000000000000000) = SHL vda0(0xa0), vd9e(0x1)
    0xda3: vda3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vda2(0x10000000000000000000000000000000000000000), vd9c(0x1)
    0xda6: vda6 = AND v7e8, vda3(0xffffffffffffffffffffffffffffffffffffffff)
    0xda8: MSTORE vd9b, vda6
    0xda9: vda9 = MLOAD vd98(0x40)
    0xdad: vdad(0x0) = SUB vd9b, vda9
    0xdae: vdae(0x20) = CONST 
    0xdb0: vdb0(0x20) = ADD vdae(0x20), vdad(0x0)
    0xdb2: RETURN vda9, vdb0(0x20)

}

function acceptGovernor()() public {
    Begin block 0x1fa
    prev=[], succ=[0x7eb]
    =================================
    0x1fb: v1fb(0xdd2) = CONST 
    0x1fe: v1fe(0x7eb) = CONST 
    0x201: JUMP v1fe(0x7eb)

    Begin block 0x7eb
    prev=[0x1fa], succ=[0x7fe, 0x84a]
    =================================
    0x7ec: v7ec(0x1) = CONST 
    0x7ee: v7ee = SLOAD v7ec(0x1)
    0x7ef: v7ef(0x1) = CONST 
    0x7f1: v7f1(0x1) = CONST 
    0x7f3: v7f3(0xa0) = CONST 
    0x7f5: v7f5(0x10000000000000000000000000000000000000000) = SHL v7f3(0xa0), v7f1(0x1)
    0x7f6: v7f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7f5(0x10000000000000000000000000000000000000000), v7ef(0x1)
    0x7f7: v7f7 = AND v7f6(0xffffffffffffffffffffffffffffffffffffffff), v7ee
    0x7f8: v7f8 = CALLER 
    0x7f9: v7f9 = EQ v7f8, v7f7
    0x7fa: v7fa(0x84a) = CONST 
    0x7fd: JUMPI v7fa(0x84a), v7f9

    Begin block 0x7fe
    prev=[0x7eb], succ=[]
    =================================
    0x7fe: v7fe(0x40) = CONST 
    0x801: v801 = MLOAD v7fe(0x40)
    0x802: v802(0x461bcd) = CONST 
    0x806: v806(0xe5) = CONST 
    0x808: v808(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v806(0xe5), v802(0x461bcd)
    0x80a: MSTORE v801, v808(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x80b: v80b(0x20) = CONST 
    0x80d: v80d(0x4) = CONST 
    0x810: v810 = ADD v801, v80d(0x4)
    0x811: MSTORE v810, v80b(0x20)
    0x812: v812(0x18) = CONST 
    0x814: v814(0x24) = CONST 
    0x817: v817 = ADD v801, v814(0x24)
    0x818: MSTORE v817, v812(0x18)
    0x819: v819(0x6e6f74207468652070656e64696e6720676f7665726e6f720000000000000000) = CONST 
    0x83a: v83a(0x44) = CONST 
    0x83d: v83d = ADD v801, v83a(0x44)
    0x83e: MSTORE v83d, v819(0x6e6f74207468652070656e64696e6720676f7665726e6f720000000000000000)
    0x840: v840 = MLOAD v7fe(0x40)
    0x844: v844(0x0) = SUB v801, v840
    0x845: v845(0x64) = CONST 
    0x847: v847(0x64) = ADD v845(0x64), v844(0x0)
    0x849: REVERT v840, v847(0x64)

    Begin block 0x84a
    prev=[0x7eb], succ=[0xdd2]
    =================================
    0x84b: v84b(0x1) = CONST 
    0x84e: v84e = SLOAD v84b(0x1)
    0x84f: v84f(0x1) = CONST 
    0x851: v851(0x1) = CONST 
    0x853: v853(0xa0) = CONST 
    0x855: v855(0x10000000000000000000000000000000000000000) = SHL v853(0xa0), v851(0x1)
    0x856: v856(0xffffffffffffffffffffffffffffffffffffffff) = SUB v855(0x10000000000000000000000000000000000000000), v84f(0x1)
    0x857: v857(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v856(0xffffffffffffffffffffffffffffffffffffffff)
    0x858: v858 = AND v857(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v84e
    0x85a: SSTORE v84b(0x1), v858
    0x85b: v85b(0x0) = CONST 
    0x85e: v85e = SLOAD v85b(0x0)
    0x85f: v85f(0x10000) = CONST 
    0x863: v863(0x1) = CONST 
    0x865: v865(0xb0) = CONST 
    0x867: v867(0x100000000000000000000000000000000000000000000) = SHL v865(0xb0), v863(0x1)
    0x868: v868(0xffffffffffffffffffffffffffffffffffffffff0000) = SUB v867(0x100000000000000000000000000000000000000000000), v85f(0x10000)
    0x869: v869(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT v868(0xffffffffffffffffffffffffffffffffffffffff0000)
    0x86a: v86a = AND v869(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff), v85e
    0x86b: v86b = CALLER 
    0x86c: v86c(0x10000) = CONST 
    0x870: v870 = MUL v86c(0x10000), v86b
    0x871: v871 = OR v870, v86a
    0x873: SSTORE v85b(0x0), v871
    0x874: JUMP v1fb(0xdd2)

    Begin block 0xdd2
    prev=[0x84a], succ=[]
    =================================
    0xdd3: STOP 

}

function setPendingGovernor(address)() public {
    Begin block 0x202
    prev=[], succ=[0x214, 0x218]
    =================================
    0x203: v203(0xdf3) = CONST 
    0x206: v206(0x4) = CONST 
    0x209: v209 = CALLDATASIZE 
    0x20a: v20a = SUB v209, v206(0x4)
    0x20b: v20b(0x20) = CONST 
    0x20e: v20e = LT v20a, v20b(0x20)
    0x20f: v20f = ISZERO v20e
    0x210: v210(0x218) = CONST 
    0x213: JUMPI v210(0x218), v20f

    Begin block 0x214
    prev=[0x202], succ=[]
    =================================
    0x214: v214(0x0) = CONST 
    0x217: REVERT v214(0x0), v214(0x0)

    Begin block 0x218
    prev=[0x202], succ=[0x875]
    =================================
    0x21a: v21a = CALLDATALOAD v206(0x4)
    0x21b: v21b(0x1) = CONST 
    0x21d: v21d(0x1) = CONST 
    0x21f: v21f(0xa0) = CONST 
    0x221: v221(0x10000000000000000000000000000000000000000) = SHL v21f(0xa0), v21d(0x1)
    0x222: v222(0xffffffffffffffffffffffffffffffffffffffff) = SUB v221(0x10000000000000000000000000000000000000000), v21b(0x1)
    0x223: v223 = AND v222(0xffffffffffffffffffffffffffffffffffffffff), v21a
    0x224: v224(0x875) = CONST 
    0x227: JUMP v224(0x875)

    Begin block 0x875
    prev=[0x218], succ=[0x88e, 0x8cd]
    =================================
    0x876: v876(0x0) = CONST 
    0x878: v878 = SLOAD v876(0x0)
    0x879: v879(0x10000) = CONST 
    0x87e: v87e = DIV v878, v879(0x10000)
    0x87f: v87f(0x1) = CONST 
    0x881: v881(0x1) = CONST 
    0x883: v883(0xa0) = CONST 
    0x885: v885(0x10000000000000000000000000000000000000000) = SHL v883(0xa0), v881(0x1)
    0x886: v886(0xffffffffffffffffffffffffffffffffffffffff) = SUB v885(0x10000000000000000000000000000000000000000), v87f(0x1)
    0x887: v887 = AND v886(0xffffffffffffffffffffffffffffffffffffffff), v87e
    0x888: v888 = CALLER 
    0x889: v889 = EQ v888, v887
    0x88a: v88a(0x8cd) = CONST 
    0x88d: JUMPI v88a(0x8cd), v889

    Begin block 0x88e
    prev=[0x875], succ=[]
    =================================
    0x88e: v88e(0x40) = CONST 
    0x891: v891 = MLOAD v88e(0x40)
    0x892: v892(0x461bcd) = CONST 
    0x896: v896(0xe5) = CONST 
    0x898: v898(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v896(0xe5), v892(0x461bcd)
    0x89a: MSTORE v891, v898(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x89b: v89b(0x20) = CONST 
    0x89d: v89d(0x4) = CONST 
    0x8a0: v8a0 = ADD v891, v89d(0x4)
    0x8a1: MSTORE v8a0, v89b(0x20)
    0x8a2: v8a2(0x10) = CONST 
    0x8a4: v8a4(0x24) = CONST 
    0x8a7: v8a7 = ADD v891, v8a4(0x24)
    0x8a8: MSTORE v8a7, v8a2(0x10)
    0x8a9: v8a9(0x3737ba103a34329033b7bb32b93737b9) = CONST 
    0x8ba: v8ba(0x81) = CONST 
    0x8bc: v8bc(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000) = SHL v8ba(0x81), v8a9(0x3737ba103a34329033b7bb32b93737b9)
    0x8bd: v8bd(0x44) = CONST 
    0x8c0: v8c0 = ADD v891, v8bd(0x44)
    0x8c1: MSTORE v8c0, v8bc(0x6e6f742074686520676f7665726e6f7200000000000000000000000000000000)
    0x8c3: v8c3 = MLOAD v88e(0x40)
    0x8c7: v8c7(0x0) = SUB v891, v8c3
    0x8c8: v8c8(0x64) = CONST 
    0x8ca: v8ca(0x64) = ADD v8c8(0x64), v8c7(0x0)
    0x8cc: REVERT v8c3, v8ca(0x64)

    Begin block 0x8cd
    prev=[0x875], succ=[0xdf3]
    =================================
    0x8ce: v8ce(0x1) = CONST 
    0x8d1: v8d1 = SLOAD v8ce(0x1)
    0x8d2: v8d2(0x1) = CONST 
    0x8d4: v8d4(0x1) = CONST 
    0x8d6: v8d6(0xa0) = CONST 
    0x8d8: v8d8(0x10000000000000000000000000000000000000000) = SHL v8d6(0xa0), v8d4(0x1)
    0x8d9: v8d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8d8(0x10000000000000000000000000000000000000000), v8d2(0x1)
    0x8da: v8da(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v8d9(0xffffffffffffffffffffffffffffffffffffffff)
    0x8db: v8db = AND v8da(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8d1
    0x8dc: v8dc(0x1) = CONST 
    0x8de: v8de(0x1) = CONST 
    0x8e0: v8e0(0xa0) = CONST 
    0x8e2: v8e2(0x10000000000000000000000000000000000000000) = SHL v8e0(0xa0), v8de(0x1)
    0x8e3: v8e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8e2(0x10000000000000000000000000000000000000000), v8dc(0x1)
    0x8e7: v8e7 = AND v8e3(0xffffffffffffffffffffffffffffffffffffffff), v223
    0x8eb: v8eb = OR v8e7, v8db
    0x8ed: SSTORE v8ce(0x1), v8eb
    0x8ee: JUMP v203(0xdf3)

    Begin block 0xdf3
    prev=[0x8cd], succ=[]
    =================================
    0xdf4: STOP 

}

function tiers(uint256)() public {
    Begin block 0xae
    prev=[], succ=[0xc0, 0xc4]
    =================================
    0xaf: vaf(0xc2b) = CONST 
    0xb2: vb2(0x4) = CONST 
    0xb5: vb5 = CALLDATASIZE 
    0xb6: vb6 = SUB vb5, vb2(0x4)
    0xb7: vb7(0x20) = CONST 
    0xba: vba = LT vb6, vb7(0x20)
    0xbb: vbb = ISZERO vba
    0xbc: vbc(0xc4) = CONST 
    0xbf: JUMPI vbc(0xc4), vbb

    Begin block 0xc0
    prev=[0xae], succ=[]
    =================================
    0xc0: vc0(0x0) = CONST 
    0xc3: REVERT vc0(0x0), vc0(0x0)

    Begin block 0xc4
    prev=[0xae], succ=[0x228]
    =================================
    0xc6: vc6 = CALLDATALOAD vb2(0x4)
    0xc7: vc7(0x228) = CONST 
    0xca: JUMP vc7(0x228)

    Begin block 0x228
    prev=[0xc4], succ=[0xc2b]
    =================================
    0x229: v229(0x3) = CONST 
    0x22b: v22b(0x20) = CONST 
    0x22d: MSTORE v22b(0x20), v229(0x3)
    0x22e: v22e(0x0) = CONST 
    0x232: MSTORE v22e(0x0), vc6
    0x233: v233(0x40) = CONST 
    0x236: v236 = SHA3 v22e(0x0), v233(0x40)
    0x237: v237 = SLOAD v236
    0x239: JUMP vaf(0xc2b)

    Begin block 0xc2b
    prev=[0x228], succ=[]
    =================================
    0xc2c: vc2c(0x40) = CONST 
    0xc2f: vc2f = MLOAD vc2c(0x40)
    0xc32: MSTORE vc2f, v237
    0xc33: vc33 = MLOAD vc2c(0x40)
    0xc37: vc37(0x0) = SUB vc2f, vc33
    0xc38: vc38(0x20) = CONST 
    0xc3a: vc3a(0x20) = ADD vc38(0x20), vc37(0x0)
    0xc3c: RETURN vc33, vc3a(0x20)

}

function fallback()() public {
    Begin block 0xbe3
    prev=[], succ=[]
    =================================
    0xbe4: vbe4(0x0) = CONST 
    0xbe7: REVERT vbe4(0x0), vbe4(0x0)

}

function governor()() public {
    Begin block 0xdd
    prev=[], succ=[0x23a]
    =================================
    0xde: vde(0xc5c) = CONST 
    0xe1: ve1(0x23a) = CONST 
    0xe4: JUMP ve1(0x23a)

    Begin block 0x23a
    prev=[0xdd], succ=[0xc5c]
    =================================
    0x23b: v23b(0x0) = CONST 
    0x23d: v23d = SLOAD v23b(0x0)
    0x23e: v23e(0x10000) = CONST 
    0x243: v243 = DIV v23d, v23e(0x10000)
    0x244: v244(0x1) = CONST 
    0x246: v246(0x1) = CONST 
    0x248: v248(0xa0) = CONST 
    0x24a: v24a(0x10000000000000000000000000000000000000000) = SHL v248(0xa0), v246(0x1)
    0x24b: v24b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24a(0x10000000000000000000000000000000000000000), v244(0x1)
    0x24c: v24c = AND v24b(0xffffffffffffffffffffffffffffffffffffffff), v243
    0x24e: JUMP vde(0xc5c)

    Begin block 0xc5c
    prev=[0x23a], succ=[]
    =================================
    0xc5d: vc5d(0x40) = CONST 
    0xc60: vc60 = MLOAD vc5d(0x40)
    0xc61: vc61(0x1) = CONST 
    0xc63: vc63(0x1) = CONST 
    0xc65: vc65(0xa0) = CONST 
    0xc67: vc67(0x10000000000000000000000000000000000000000) = SHL vc65(0xa0), vc63(0x1)
    0xc68: vc68(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc67(0x10000000000000000000000000000000000000000), vc61(0x1)
    0xc6b: vc6b = AND v24c, vc68(0xffffffffffffffffffffffffffffffffffffffff)
    0xc6d: MSTORE vc60, vc6b
    0xc6e: vc6e = MLOAD vc5d(0x40)
    0xc72: vc72(0x0) = SUB vc60, vc6e
    0xc73: vc73(0x20) = CONST 
    0xc75: vc75(0x20) = ADD vc73(0x20), vc72(0x0)
    0xc77: RETURN vc6e, vc75(0x20)

}

