function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x921]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x907: v907(0x921) = CONST 
    0x908: JUMPI v907(0x921), v8

    Begin block 0xd
    prev=[0x0], succ=[0x64, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0xc1e80334) = CONST 
    0x19: v19 = GT v14(0xc1e80334), v12
    0x1a: v1a(0x64) = CONST 
    0x1d: JUMPI v1a(0x64), v19

    Begin block 0x64
    prev=[0xd], succ=[0x924, 0x70]
    =================================
    0x66: v66(0x26782247) = CONST 
    0x6b: v6b = EQ v66(0x26782247), v12
    0x915: v915(0x924) = CONST 
    0x916: JUMPI v915(0x924), v6b

    Begin block 0x924
    prev=[0x64], succ=[]
    =================================
    0x925: v925(0x12a) = CONST 
    0x926: CALLPRIVATE v925(0x12a)

    Begin block 0x70
    prev=[0x64], succ=[0x927, 0x7b]
    =================================
    0x71: v71(0x2832f611) = CONST 
    0x76: v76 = EQ v71(0x2832f611), v12
    0x917: v917(0x927) = CONST 
    0x918: JUMPI v917(0x927), v76

    Begin block 0x927
    prev=[0x70], succ=[]
    =================================
    0x928: v928(0x15b) = CONST 
    0x929: CALLPRIVATE v928(0x15b)

    Begin block 0x7b
    prev=[0x70], succ=[0x92a, 0x86]
    =================================
    0x7c: v7c(0x32549f5a) = CONST 
    0x81: v81 = EQ v7c(0x32549f5a), v12
    0x919: v919(0x92a) = CONST 
    0x91a: JUMPI v919(0x92a), v81

    Begin block 0x92a
    prev=[0x7b], succ=[]
    =================================
    0x92b: v92b(0x182) = CONST 
    0x92c: CALLPRIVATE v92b(0x182)

    Begin block 0x86
    prev=[0x7b], succ=[0x92d, 0x91]
    =================================
    0x87: v87(0xb71d1a0c) = CONST 
    0x8c: v8c = EQ v87(0xb71d1a0c), v12
    0x91b: v91b(0x92d) = CONST 
    0x91c: JUMPI v91b(0x92d), v8c

    Begin block 0x92d
    prev=[0x86], succ=[]
    =================================
    0x92e: v92e(0x197) = CONST 
    0x92f: CALLPRIVATE v92e(0x197)

    Begin block 0x91
    prev=[0x86], succ=[0x930, 0x9c]
    =================================
    0x92: v92(0xbb5260e4) = CONST 
    0x97: v97 = EQ v92(0xbb5260e4), v12
    0x91d: v91d(0x930) = CONST 
    0x91e: JUMPI v91d(0x930), v97

    Begin block 0x930
    prev=[0x91], succ=[]
    =================================
    0x931: v931(0x1ca) = CONST 
    0x932: CALLPRIVATE v931(0x1ca)

    Begin block 0x9c
    prev=[0x91], succ=[0x921, 0x933]
    =================================
    0x9d: v9d(0xbb82aa5e) = CONST 
    0xa2: va2 = EQ v9d(0xbb82aa5e), v12
    0x91f: v91f(0x933) = CONST 
    0x920: JUMPI v91f(0x933), va2

    Begin block 0x921
    prev=[0x0, 0x9c], succ=[]
    =================================
    0x922: v922(0xa7) = CONST 
    0x923: CALLPRIVATE v922(0xa7)

    Begin block 0x933
    prev=[0x9c], succ=[]
    =================================
    0x934: v934(0x1df) = CONST 
    0x935: CALLPRIVATE v934(0x1df)

    Begin block 0x1e
    prev=[0xd], succ=[0x936, 0x29]
    =================================
    0x1f: v1f(0xc1e80334) = CONST 
    0x24: v24 = EQ v1f(0xc1e80334), v12
    0x909: v909(0x936) = CONST 
    0x90a: JUMPI v909(0x936), v24

    Begin block 0x936
    prev=[0x1e], succ=[]
    =================================
    0x937: v937(0x1f4) = CONST 
    0x938: CALLPRIVATE v937(0x1f4)

    Begin block 0x29
    prev=[0x1e], succ=[0x939, 0x34]
    =================================
    0x2a: v2a(0xdcfbc0c7) = CONST 
    0x2f: v2f = EQ v2a(0xdcfbc0c7), v12
    0x90b: v90b(0x939) = CONST 
    0x90c: JUMPI v90b(0x939), v2f

    Begin block 0x939
    prev=[0x29], succ=[]
    =================================
    0x93a: v93a(0x209) = CONST 
    0x93b: CALLPRIVATE v93a(0x209)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x93c]
    =================================
    0x35: v35(0xdd2d8e3e) = CONST 
    0x3a: v3a = EQ v35(0xdd2d8e3e), v12
    0x90d: v90d(0x93c) = CONST 
    0x90e: JUMPI v90d(0x93c), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x93f, 0x4a]
    =================================
    0x40: v40(0xe992a041) = CONST 
    0x45: v45 = EQ v40(0xe992a041), v12
    0x90f: v90f(0x93f) = CONST 
    0x910: JUMPI v90f(0x93f), v45

    Begin block 0x93f
    prev=[0x3f], succ=[]
    =================================
    0x940: v940(0x233) = CONST 
    0x941: CALLPRIVATE v940(0x233)

    Begin block 0x4a
    prev=[0x3f], succ=[0x942, 0x55]
    =================================
    0x4b: v4b(0xe9c714f2) = CONST 
    0x50: v50 = EQ v4b(0xe9c714f2), v12
    0x911: v911(0x942) = CONST 
    0x912: JUMPI v911(0x942), v50

    Begin block 0x942
    prev=[0x4a], succ=[]
    =================================
    0x943: v943(0x266) = CONST 
    0x944: CALLPRIVATE v943(0x266)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0x945]
    =================================
    0x56: v56(0xf851a440) = CONST 
    0x5b: v5b = EQ v56(0xf851a440), v12
    0x913: v913(0x945) = CONST 
    0x914: JUMPI v913(0x945), v5b

    Begin block 0x60
    prev=[0x55], succ=[]
    =================================
    0x60: v60(0xa7) = CONST 
    0x63: JUMP v60(0xa7)

    Begin block 0x945
    prev=[0x55], succ=[]
    =================================
    0x946: v946(0x27b) = CONST 
    0x947: CALLPRIVATE v946(0x27b)

    Begin block 0x93c
    prev=[0x34], succ=[]
    =================================
    0x93d: v93d(0x21e) = CONST 
    0x93e: CALLPRIVATE v93d(0x21e)

}

function pendingAdmin()() public {
    Begin block 0x12a
    prev=[], succ=[0x132, 0x136]
    =================================
    0x12b: v12b = CALLVALUE 
    0x12d: v12d = ISZERO v12b
    0x12e: v12e(0x136) = CONST 
    0x131: JUMPI v12e(0x136), v12d

    Begin block 0x132
    prev=[0x12a], succ=[]
    =================================
    0x132: v132(0x0) = CONST 
    0x135: REVERT v132(0x0), v132(0x0)

    Begin block 0x136
    prev=[0x12a], succ=[0x290]
    =================================
    0x138: v138(0x6a8) = CONST 
    0x13b: v13b(0x290) = CONST 
    0x13e: JUMP v13b(0x290)

    Begin block 0x290
    prev=[0x136], succ=[0x6a8]
    =================================
    0x291: v291(0x5) = CONST 
    0x293: v293 = SLOAD v291(0x5)
    0x294: v294(0x1) = CONST 
    0x296: v296(0x1) = CONST 
    0x298: v298(0xa0) = CONST 
    0x29a: v29a(0x10000000000000000000000000000000000000000) = SHL v298(0xa0), v296(0x1)
    0x29b: v29b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29a(0x10000000000000000000000000000000000000000), v294(0x1)
    0x29c: v29c = AND v29b(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x29e: JUMP v138(0x6a8)

    Begin block 0x6a8
    prev=[0x290], succ=[]
    =================================
    0x6a9: v6a9(0x40) = CONST 
    0x6ac: v6ac = MLOAD v6a9(0x40)
    0x6ad: v6ad(0x1) = CONST 
    0x6af: v6af(0x1) = CONST 
    0x6b1: v6b1(0xa0) = CONST 
    0x6b3: v6b3(0x10000000000000000000000000000000000000000) = SHL v6b1(0xa0), v6af(0x1)
    0x6b4: v6b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b3(0x10000000000000000000000000000000000000000), v6ad(0x1)
    0x6b7: v6b7 = AND v29c, v6b4(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b9: MSTORE v6ac, v6b7
    0x6ba: v6ba = MLOAD v6a9(0x40)
    0x6be: v6be(0x0) = SUB v6ac, v6ba
    0x6bf: v6bf(0x20) = CONST 
    0x6c1: v6c1(0x20) = ADD v6bf(0x20), v6be(0x0)
    0x6c3: RETURN v6ba, v6c1(0x20)

}

function dflInitialSpeed()() public {
    Begin block 0x15b
    prev=[], succ=[0x163, 0x167]
    =================================
    0x15c: v15c = CALLVALUE 
    0x15e: v15e = ISZERO v15c
    0x15f: v15f(0x167) = CONST 
    0x162: JUMPI v15f(0x167), v15e

    Begin block 0x163
    prev=[0x15b], succ=[]
    =================================
    0x163: v163(0x0) = CONST 
    0x166: REVERT v163(0x0), v163(0x0)

    Begin block 0x167
    prev=[0x15b], succ=[0x29f]
    =================================
    0x169: v169(0x6e3) = CONST 
    0x16c: v16c(0x29f) = CONST 
    0x16f: JUMP v16c(0x29f)

    Begin block 0x29f
    prev=[0x167], succ=[0x6e3]
    =================================
    0x2a0: v2a0(0x2) = CONST 
    0x2a2: v2a2 = SLOAD v2a0(0x2)
    0x2a4: JUMP v169(0x6e3)

    Begin block 0x6e3
    prev=[0x29f], succ=[]
    =================================
    0x6e4: v6e4(0x40) = CONST 
    0x6e7: v6e7 = MLOAD v6e4(0x40)
    0x6ea: MSTORE v6e7, v2a2
    0x6eb: v6eb = MLOAD v6e4(0x40)
    0x6ef: v6ef(0x0) = SUB v6e7, v6eb
    0x6f0: v6f0(0x20) = CONST 
    0x6f2: v6f2(0x20) = ADD v6f0(0x20), v6ef(0x0)
    0x6f4: RETURN v6eb, v6f2(0x20)

}

function dflStartBlock()() public {
    Begin block 0x182
    prev=[], succ=[0x18a, 0x18e]
    =================================
    0x183: v183 = CALLVALUE 
    0x185: v185 = ISZERO v183
    0x186: v186(0x18e) = CONST 
    0x189: JUMPI v186(0x18e), v185

    Begin block 0x18a
    prev=[0x182], succ=[]
    =================================
    0x18a: v18a(0x0) = CONST 
    0x18d: REVERT v18a(0x0), v18a(0x0)

    Begin block 0x18e
    prev=[0x182], succ=[0x2a5]
    =================================
    0x190: v190(0x714) = CONST 
    0x193: v193(0x2a5) = CONST 
    0x196: JUMP v193(0x2a5)

    Begin block 0x2a5
    prev=[0x18e], succ=[0x714]
    =================================
    0x2a6: v2a6(0x3) = CONST 
    0x2a8: v2a8 = SLOAD v2a6(0x3)
    0x2aa: JUMP v190(0x714)

    Begin block 0x714
    prev=[0x2a5], succ=[]
    =================================
    0x715: v715(0x40) = CONST 
    0x718: v718 = MLOAD v715(0x40)
    0x71b: MSTORE v718, v2a8
    0x71c: v71c = MLOAD v715(0x40)
    0x720: v720(0x0) = SUB v718, v71c
    0x721: v721(0x20) = CONST 
    0x723: v723(0x20) = ADD v721(0x20), v720(0x0)
    0x725: RETURN v71c, v723(0x20)

}

function _setPendingAdmin(address)() public {
    Begin block 0x197
    prev=[], succ=[0x19f, 0x1a3]
    =================================
    0x198: v198 = CALLVALUE 
    0x19a: v19a = ISZERO v198
    0x19b: v19b(0x1a3) = CONST 
    0x19e: JUMPI v19b(0x1a3), v19a

    Begin block 0x19f
    prev=[0x197], succ=[]
    =================================
    0x19f: v19f(0x0) = CONST 
    0x1a2: REVERT v19f(0x0), v19f(0x0)

    Begin block 0x1a3
    prev=[0x197], succ=[0x1b6, 0x1ba]
    =================================
    0x1a5: v1a5(0x745) = CONST 
    0x1a8: v1a8(0x4) = CONST 
    0x1ab: v1ab = CALLDATASIZE 
    0x1ac: v1ac = SUB v1ab, v1a8(0x4)
    0x1ad: v1ad(0x20) = CONST 
    0x1b0: v1b0 = LT v1ac, v1ad(0x20)
    0x1b1: v1b1 = ISZERO v1b0
    0x1b2: v1b2(0x1ba) = CONST 
    0x1b5: JUMPI v1b2(0x1ba), v1b1

    Begin block 0x1b6
    prev=[0x1a3], succ=[]
    =================================
    0x1b6: v1b6(0x0) = CONST 
    0x1b9: REVERT v1b6(0x0), v1b6(0x0)

    Begin block 0x1ba
    prev=[0x1a3], succ=[0x2ab]
    =================================
    0x1bc: v1bc = CALLDATALOAD v1a8(0x4)
    0x1bd: v1bd(0x1) = CONST 
    0x1bf: v1bf(0x1) = CONST 
    0x1c1: v1c1(0xa0) = CONST 
    0x1c3: v1c3(0x10000000000000000000000000000000000000000) = SHL v1c1(0xa0), v1bf(0x1)
    0x1c4: v1c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c3(0x10000000000000000000000000000000000000000), v1bd(0x1)
    0x1c5: v1c5 = AND v1c4(0xffffffffffffffffffffffffffffffffffffffff), v1bc
    0x1c6: v1c6(0x2ab) = CONST 
    0x1c9: JUMP v1c6(0x2ab)

    Begin block 0x2ab
    prev=[0x1ba], succ=[0x2c1, 0x2d3]
    =================================
    0x2ac: v2ac(0x4) = CONST 
    0x2ae: v2ae = SLOAD v2ac(0x4)
    0x2af: v2af(0x0) = CONST 
    0x2b2: v2b2(0x1) = CONST 
    0x2b4: v2b4(0x1) = CONST 
    0x2b6: v2b6(0xa0) = CONST 
    0x2b8: v2b8(0x10000000000000000000000000000000000000000) = SHL v2b6(0xa0), v2b4(0x1)
    0x2b9: v2b9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b8(0x10000000000000000000000000000000000000000), v2b2(0x1)
    0x2ba: v2ba = AND v2b9(0xffffffffffffffffffffffffffffffffffffffff), v2ae
    0x2bb: v2bb = CALLER 
    0x2bc: v2bc = EQ v2bb, v2ba
    0x2bd: v2bd(0x2d3) = CONST 
    0x2c0: JUMPI v2bd(0x2d3), v2bc

    Begin block 0x2c1
    prev=[0x2ab], succ=[0x2cc0x197]
    =================================
    0x2c1: v2c1(0x2cc) = CONST 
    0x2c4: v2c4(0x1) = CONST 
    0x2c6: v2c6(0xd) = CONST 
    0x2c8: v2c8(0x5e7) = CONST 
    0x2cb: v2cb_0 = CALLPRIVATE v2c8(0x5e7), v2c6(0xd), v2c4(0x1), v2c1(0x2cc)

    Begin block 0x2cc0x197
    prev=[0x2c1], succ=[0x3390x197]
    =================================
    0x2cf0x197: v1972cf(0x339) = CONST 
    0x2d20x197: JUMP v1972cf(0x339)

    Begin block 0x3390x197
    prev=[0x2cc0x197, 0x3350x197], succ=[0x745]
    =================================
    0x33d0x197: JUMP v1a5(0x745)

    Begin block 0x745
    prev=[0x3390x197], succ=[]
    =================================
    0x745_0x0: v745_0 = PHI v333(0x0), v2cb_0
    0x746: v746(0x40) = CONST 
    0x749: v749 = MLOAD v746(0x40)
    0x74c: MSTORE v749, v745_0
    0x74d: v74d = MLOAD v746(0x40)
    0x751: v751(0x0) = SUB v749, v74d
    0x752: v752(0x20) = CONST 
    0x754: v754(0x20) = ADD v752(0x20), v751(0x0)
    0x756: RETURN v74d, v754(0x20)

    Begin block 0x2d3
    prev=[0x2ab], succ=[0x3350x197]
    =================================
    0x2d4: v2d4(0x5) = CONST 
    0x2d7: v2d7 = SLOAD v2d4(0x5)
    0x2d8: v2d8(0x1) = CONST 
    0x2da: v2da(0x1) = CONST 
    0x2dc: v2dc(0xa0) = CONST 
    0x2de: v2de(0x10000000000000000000000000000000000000000) = SHL v2dc(0xa0), v2da(0x1)
    0x2df: v2df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2de(0x10000000000000000000000000000000000000000), v2d8(0x1)
    0x2e2: v2e2 = AND v2df(0xffffffffffffffffffffffffffffffffffffffff), v1c5
    0x2e3: v2e3(0x1) = CONST 
    0x2e5: v2e5(0x1) = CONST 
    0x2e7: v2e7(0xa0) = CONST 
    0x2e9: v2e9(0x10000000000000000000000000000000000000000) = SHL v2e7(0xa0), v2e5(0x1)
    0x2ea: v2ea(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e9(0x10000000000000000000000000000000000000000), v2e3(0x1)
    0x2eb: v2eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2ea(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ed: v2ed = AND v2d7, v2eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x2ef: v2ef = OR v2e2, v2ed
    0x2f2: SSTORE v2d4(0x5), v2ef
    0x2f3: v2f3(0x40) = CONST 
    0x2f6: v2f6 = MLOAD v2f3(0x40)
    0x2fa: v2fa = AND v2d7, v2df(0xffffffffffffffffffffffffffffffffffffffff)
    0x2fd: MSTORE v2f6, v2fa
    0x2fe: v2fe(0x20) = CONST 
    0x301: v301 = ADD v2f6, v2fe(0x20)
    0x305: MSTORE v301, v2e2
    0x307: v307 = MLOAD v2f3(0x40)
    0x308: v308(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x32d: v32d(0x0) = SUB v2f6, v307
    0x330: v330(0x40) = ADD v2f3(0x40), v32d(0x0)
    0x332: LOG1 v307, v330(0x40), v308(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x333: v333(0x0) = CONST 

    Begin block 0x3350x197
    prev=[0x2d3], succ=[0x3390x197]
    =================================

}

function dflAddress()() public {
    Begin block 0x1ca
    prev=[], succ=[0x1d2, 0x1d6]
    =================================
    0x1cb: v1cb = CALLVALUE 
    0x1cd: v1cd = ISZERO v1cb
    0x1ce: v1ce(0x1d6) = CONST 
    0x1d1: JUMPI v1ce(0x1d6), v1cd

    Begin block 0x1d2
    prev=[0x1ca], succ=[]
    =================================
    0x1d2: v1d2(0x0) = CONST 
    0x1d5: REVERT v1d2(0x0), v1d2(0x0)

    Begin block 0x1d6
    prev=[0x1ca], succ=[0x33e]
    =================================
    0x1d8: v1d8(0x776) = CONST 
    0x1db: v1db(0x33e) = CONST 
    0x1de: JUMP v1db(0x33e)

    Begin block 0x33e
    prev=[0x1d6], succ=[0x776]
    =================================
    0x33f: v33f(0x0) = CONST 
    0x341: v341 = SLOAD v33f(0x0)
    0x342: v342(0x1) = CONST 
    0x344: v344(0x1) = CONST 
    0x346: v346(0xa0) = CONST 
    0x348: v348(0x10000000000000000000000000000000000000000) = SHL v346(0xa0), v344(0x1)
    0x349: v349(0xffffffffffffffffffffffffffffffffffffffff) = SUB v348(0x10000000000000000000000000000000000000000), v342(0x1)
    0x34a: v34a = AND v349(0xffffffffffffffffffffffffffffffffffffffff), v341
    0x34c: JUMP v1d8(0x776)

    Begin block 0x776
    prev=[0x33e], succ=[]
    =================================
    0x777: v777(0x40) = CONST 
    0x77a: v77a = MLOAD v777(0x40)
    0x77b: v77b(0x1) = CONST 
    0x77d: v77d(0x1) = CONST 
    0x77f: v77f(0xa0) = CONST 
    0x781: v781(0x10000000000000000000000000000000000000000) = SHL v77f(0xa0), v77d(0x1)
    0x782: v782(0xffffffffffffffffffffffffffffffffffffffff) = SUB v781(0x10000000000000000000000000000000000000000), v77b(0x1)
    0x785: v785 = AND v34a, v782(0xffffffffffffffffffffffffffffffffffffffff)
    0x787: MSTORE v77a, v785
    0x788: v788 = MLOAD v777(0x40)
    0x78c: v78c(0x0) = SUB v77a, v788
    0x78d: v78d(0x20) = CONST 
    0x78f: v78f(0x20) = ADD v78d(0x20), v78c(0x0)
    0x791: RETURN v788, v78f(0x20)

}

function comptrollerImplementation()() public {
    Begin block 0x1df
    prev=[], succ=[0x1e7, 0x1eb]
    =================================
    0x1e0: v1e0 = CALLVALUE 
    0x1e2: v1e2 = ISZERO v1e0
    0x1e3: v1e3(0x1eb) = CONST 
    0x1e6: JUMPI v1e3(0x1eb), v1e2

    Begin block 0x1e7
    prev=[0x1df], succ=[]
    =================================
    0x1e7: v1e7(0x0) = CONST 
    0x1ea: REVERT v1e7(0x0), v1e7(0x0)

    Begin block 0x1eb
    prev=[0x1df], succ=[0x34d]
    =================================
    0x1ed: v1ed(0x7b1) = CONST 
    0x1f0: v1f0(0x34d) = CONST 
    0x1f3: JUMP v1f0(0x34d)

    Begin block 0x34d
    prev=[0x1eb], succ=[0x7b1]
    =================================
    0x34e: v34e(0x6) = CONST 
    0x350: v350 = SLOAD v34e(0x6)
    0x351: v351(0x1) = CONST 
    0x353: v353(0x1) = CONST 
    0x355: v355(0xa0) = CONST 
    0x357: v357(0x10000000000000000000000000000000000000000) = SHL v355(0xa0), v353(0x1)
    0x358: v358(0xffffffffffffffffffffffffffffffffffffffff) = SUB v357(0x10000000000000000000000000000000000000000), v351(0x1)
    0x359: v359 = AND v358(0xffffffffffffffffffffffffffffffffffffffff), v350
    0x35b: JUMP v1ed(0x7b1)

    Begin block 0x7b1
    prev=[0x34d], succ=[]
    =================================
    0x7b2: v7b2(0x40) = CONST 
    0x7b5: v7b5 = MLOAD v7b2(0x40)
    0x7b6: v7b6(0x1) = CONST 
    0x7b8: v7b8(0x1) = CONST 
    0x7ba: v7ba(0xa0) = CONST 
    0x7bc: v7bc(0x10000000000000000000000000000000000000000) = SHL v7ba(0xa0), v7b8(0x1)
    0x7bd: v7bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7bc(0x10000000000000000000000000000000000000000), v7b6(0x1)
    0x7c0: v7c0 = AND v359, v7bd(0xffffffffffffffffffffffffffffffffffffffff)
    0x7c2: MSTORE v7b5, v7c0
    0x7c3: v7c3 = MLOAD v7b2(0x40)
    0x7c7: v7c7(0x0) = SUB v7b5, v7c3
    0x7c8: v7c8(0x20) = CONST 
    0x7ca: v7ca(0x20) = ADD v7c8(0x20), v7c7(0x0)
    0x7cc: RETURN v7c3, v7ca(0x20)

}

function _acceptImplementation()() public {
    Begin block 0x1f4
    prev=[], succ=[0x1fc, 0x200]
    =================================
    0x1f5: v1f5 = CALLVALUE 
    0x1f7: v1f7 = ISZERO v1f5
    0x1f8: v1f8(0x200) = CONST 
    0x1fb: JUMPI v1f8(0x200), v1f7

    Begin block 0x1fc
    prev=[0x1f4], succ=[]
    =================================
    0x1fc: v1fc(0x0) = CONST 
    0x1ff: REVERT v1fc(0x0), v1fc(0x0)

    Begin block 0x200
    prev=[0x1f4], succ=[0x35cB0x200]
    =================================
    0x202: v202(0x7ec) = CONST 
    0x205: v205(0x35c) = CONST 
    0x208: JUMP v205(0x35c)

    Begin block 0x35cB0x200
    prev=[0x200], succ=[0x382B0x200, 0x374B0x200]
    =================================
    0x35dS0x200: v35dV200(0x7) = CONST 
    0x35fS0x200: v35fV200 = SLOAD v35dV200(0x7)
    0x360S0x200: v360V200(0x0) = CONST 
    0x363S0x200: v363V200(0x1) = CONST 
    0x365S0x200: v365V200(0x1) = CONST 
    0x367S0x200: v367V200(0xa0) = CONST 
    0x369S0x200: v369V200(0x10000000000000000000000000000000000000000) = SHL v367V200(0xa0), v365V200(0x1)
    0x36aS0x200: v36aV200(0xffffffffffffffffffffffffffffffffffffffff) = SUB v369V200(0x10000000000000000000000000000000000000000), v363V200(0x1)
    0x36bS0x200: v36bV200 = AND v36aV200(0xffffffffffffffffffffffffffffffffffffffff), v35fV200
    0x36cS0x200: v36cV200 = CALLER 
    0x36dS0x200: v36dV200 = EQ v36cV200, v36bV200
    0x36eS0x200: v36eV200 = ISZERO v36dV200
    0x370S0x200: v370V200(0x382) = CONST 
    0x373S0x200: JUMPI v370V200(0x382), v36eV200

    Begin block 0x382B0x200
    prev=[0x35cB0x200, 0x374B0x200], succ=[0x388B0x200, 0x399B0x200]
    =================================
    0x382_0x0S0x200: v382_0V200 = PHI v36eV200, v381V200
    0x383S0x200: v383V200 = ISZERO v382_0V200
    0x384S0x200: v384V200(0x399) = CONST 
    0x387S0x200: JUMPI v384V200(0x399), v383V200

    Begin block 0x388B0x200
    prev=[0x382B0x200], succ=[0x3920x35cB0x200]
    =================================
    0x388S0x200: v388V200(0x392) = CONST 
    0x38bS0x200: v38bV200(0x1) = CONST 
    0x38eS0x200: v38eV200(0x5e7) = CONST 
    0x391S0x200: v391_0V200 = CALLPRIVATE v38eV200(0x5e7), v38bV200(0x1), v38bV200(0x1), v388V200(0x392)

    Begin block 0x3920x35cB0x200
    prev=[0x388B0x200], succ=[0x4540x35cB0x200]
    =================================
    0x3950x35cS0x200: v35c395V200(0x454) = CONST 
    0x3980x35cS0x200: JUMP v35c395V200(0x454)

    Begin block 0x4540x35cB0x200
    prev=[0x3920x35cB0x200, 0x44f0x35cB0x200], succ=[0x7ec]
    =================================
    0x4540x35c_0x0S0x200: v45435c_0V200 = PHI v391_0V200, v44dV200(0x0)
    0x4560x35cS0x200: JUMP v202(0x7ec)

    Begin block 0x7ec
    prev=[0x4540x35cB0x200], succ=[]
    =================================
    0x7ed: v7ed(0x40) = CONST 
    0x7f0: v7f0 = MLOAD v7ed(0x40)
    0x7f3: MSTORE v7f0, v45435c_0V200
    0x7f4: v7f4 = MLOAD v7ed(0x40)
    0x7f8: v7f8(0x0) = SUB v7f0, v7f4
    0x7f9: v7f9(0x20) = CONST 
    0x7fb: v7fb(0x20) = ADD v7f9(0x20), v7f8(0x0)
    0x7fd: RETURN v7f4, v7fb(0x20)

    Begin block 0x399B0x200
    prev=[0x382B0x200], succ=[0x44f0x35cB0x200]
    =================================
    0x39aS0x200: v39aV200(0x6) = CONST 
    0x39dS0x200: v39dV200 = SLOAD v39aV200(0x6)
    0x39eS0x200: v39eV200(0x7) = CONST 
    0x3a1S0x200: v3a1V200 = SLOAD v39eV200(0x7)
    0x3a2S0x200: v3a2V200(0x1) = CONST 
    0x3a4S0x200: v3a4V200(0x1) = CONST 
    0x3a6S0x200: v3a6V200(0xa0) = CONST 
    0x3a8S0x200: v3a8V200(0x10000000000000000000000000000000000000000) = SHL v3a6V200(0xa0), v3a4V200(0x1)
    0x3a9S0x200: v3a9V200(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a8V200(0x10000000000000000000000000000000000000000), v3a2V200(0x1)
    0x3acS0x200: v3acV200 = AND v3a1V200, v3a9V200(0xffffffffffffffffffffffffffffffffffffffff)
    0x3adS0x200: v3adV200(0x1) = CONST 
    0x3afS0x200: v3afV200(0x1) = CONST 
    0x3b1S0x200: v3b1V200(0xa0) = CONST 
    0x3b3S0x200: v3b3V200(0x10000000000000000000000000000000000000000) = SHL v3b1V200(0xa0), v3afV200(0x1)
    0x3b4S0x200: v3b4V200(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b3V200(0x10000000000000000000000000000000000000000), v3adV200(0x1)
    0x3b5S0x200: v3b5V200(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3b4V200(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b8S0x200: v3b8V200 = AND v39dV200, v3b5V200(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3baS0x200: v3baV200 = OR v3acV200, v3b8V200
    0x3beS0x200: SSTORE v39aV200(0x6), v3baV200
    0x3c1S0x200: v3c1V200 = AND v3a1V200, v3b5V200(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x3c4S0x200: SSTORE v39eV200(0x7), v3c1V200
    0x3c5S0x200: v3c5V200(0x40) = CONST 
    0x3c8S0x200: v3c8V200 = MLOAD v3c5V200(0x40)
    0x3cbS0x200: v3cbV200 = AND v3a9V200(0xffffffffffffffffffffffffffffffffffffffff), v39dV200
    0x3ceS0x200: MSTORE v3c8V200, v3cbV200
    0x3d2S0x200: v3d2V200 = AND v3a9V200(0xffffffffffffffffffffffffffffffffffffffff), v3baV200
    0x3d3S0x200: v3d3V200(0x20) = CONST 
    0x3d6S0x200: v3d6V200 = ADD v3c8V200, v3d3V200(0x20)
    0x3d7S0x200: MSTORE v3d6V200, v3d2V200
    0x3d9S0x200: v3d9V200 = MLOAD v3c5V200(0x40)
    0x3dcS0x200: v3dcV200(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x401S0x200: v401V200(0x0) = SUB v3c8V200, v3d9V200
    0x402S0x200: v402V200(0x40) = ADD v401V200(0x0), v3c5V200(0x40)
    0x404S0x200: LOG1 v3d9V200, v402V200(0x40), v3dcV200(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x405S0x200: v405V200(0x7) = CONST 
    0x407S0x200: v407V200 = SLOAD v405V200(0x7)
    0x408S0x200: v408V200(0x40) = CONST 
    0x40bS0x200: v40bV200 = MLOAD v408V200(0x40)
    0x40cS0x200: v40cV200(0x1) = CONST 
    0x40eS0x200: v40eV200(0x1) = CONST 
    0x410S0x200: v410V200(0xa0) = CONST 
    0x412S0x200: v412V200(0x10000000000000000000000000000000000000000) = SHL v410V200(0xa0), v40eV200(0x1)
    0x413S0x200: v413V200(0xffffffffffffffffffffffffffffffffffffffff) = SUB v412V200(0x10000000000000000000000000000000000000000), v40cV200(0x1)
    0x416S0x200: v416V200 = AND v3acV200, v413V200(0xffffffffffffffffffffffffffffffffffffffff)
    0x418S0x200: MSTORE v40bV200, v416V200
    0x41bS0x200: v41bV200 = AND v407V200, v413V200(0xffffffffffffffffffffffffffffffffffffffff)
    0x41cS0x200: v41cV200(0x20) = CONST 
    0x41fS0x200: v41fV200 = ADD v40bV200, v41cV200(0x20)
    0x420S0x200: MSTORE v41fV200, v41bV200
    0x422S0x200: v422V200 = MLOAD v408V200(0x40)
    0x423S0x200: v423V200(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x447S0x200: v447V200(0x0) = SUB v40bV200, v422V200
    0x44aS0x200: v44aV200(0x40) = ADD v408V200(0x40), v447V200(0x0)
    0x44cS0x200: LOG1 v422V200, v44aV200(0x40), v423V200(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x44dS0x200: v44dV200(0x0) = CONST 

    Begin block 0x44f0x35cB0x200
    prev=[0x399B0x200], succ=[0x4540x35cB0x200]
    =================================

    Begin block 0x374B0x200
    prev=[0x35cB0x200], succ=[0x382B0x200]
    =================================
    0x375S0x200: v375V200(0x7) = CONST 
    0x377S0x200: v377V200 = SLOAD v375V200(0x7)
    0x378S0x200: v378V200(0x1) = CONST 
    0x37aS0x200: v37aV200(0x1) = CONST 
    0x37cS0x200: v37cV200(0xa0) = CONST 
    0x37eS0x200: v37eV200(0x10000000000000000000000000000000000000000) = SHL v37cV200(0xa0), v37aV200(0x1)
    0x37fS0x200: v37fV200(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37eV200(0x10000000000000000000000000000000000000000), v378V200(0x1)
    0x380S0x200: v380V200 = AND v37fV200(0xffffffffffffffffffffffffffffffffffffffff), v377V200
    0x381S0x200: v381V200 = ISZERO v380V200

}

function pendingComptrollerImplementation()() public {
    Begin block 0x209
    prev=[], succ=[0x211, 0x215]
    =================================
    0x20a: v20a = CALLVALUE 
    0x20c: v20c = ISZERO v20a
    0x20d: v20d(0x215) = CONST 
    0x210: JUMPI v20d(0x215), v20c

    Begin block 0x211
    prev=[0x209], succ=[]
    =================================
    0x211: v211(0x0) = CONST 
    0x214: REVERT v211(0x0), v211(0x0)

    Begin block 0x215
    prev=[0x209], succ=[0x457]
    =================================
    0x217: v217(0x81d) = CONST 
    0x21a: v21a(0x457) = CONST 
    0x21d: JUMP v21a(0x457)

    Begin block 0x457
    prev=[0x215], succ=[0x81d]
    =================================
    0x458: v458(0x7) = CONST 
    0x45a: v45a = SLOAD v458(0x7)
    0x45b: v45b(0x1) = CONST 
    0x45d: v45d(0x1) = CONST 
    0x45f: v45f(0xa0) = CONST 
    0x461: v461(0x10000000000000000000000000000000000000000) = SHL v45f(0xa0), v45d(0x1)
    0x462: v462(0xffffffffffffffffffffffffffffffffffffffff) = SUB v461(0x10000000000000000000000000000000000000000), v45b(0x1)
    0x463: v463 = AND v462(0xffffffffffffffffffffffffffffffffffffffff), v45a
    0x465: JUMP v217(0x81d)

    Begin block 0x81d
    prev=[0x457], succ=[]
    =================================
    0x81e: v81e(0x40) = CONST 
    0x821: v821 = MLOAD v81e(0x40)
    0x822: v822(0x1) = CONST 
    0x824: v824(0x1) = CONST 
    0x826: v826(0xa0) = CONST 
    0x828: v828(0x10000000000000000000000000000000000000000) = SHL v826(0xa0), v824(0x1)
    0x829: v829(0xffffffffffffffffffffffffffffffffffffffff) = SUB v828(0x10000000000000000000000000000000000000000), v822(0x1)
    0x82c: v82c = AND v463, v829(0xffffffffffffffffffffffffffffffffffffffff)
    0x82e: MSTORE v821, v82c
    0x82f: v82f = MLOAD v81e(0x40)
    0x833: v833(0x0) = SUB v821, v82f
    0x834: v834(0x20) = CONST 
    0x836: v836(0x20) = ADD v834(0x20), v833(0x0)
    0x838: RETURN v82f, v836(0x20)

}

function dflHalvePeriod()() public {
    Begin block 0x21e
    prev=[], succ=[0x226, 0x22a]
    =================================
    0x21f: v21f = CALLVALUE 
    0x221: v221 = ISZERO v21f
    0x222: v222(0x22a) = CONST 
    0x225: JUMPI v222(0x22a), v221

    Begin block 0x226
    prev=[0x21e], succ=[]
    =================================
    0x226: v226(0x0) = CONST 
    0x229: REVERT v226(0x0), v226(0x0)

    Begin block 0x22a
    prev=[0x21e], succ=[0x466]
    =================================
    0x22c: v22c(0x858) = CONST 
    0x22f: v22f(0x466) = CONST 
    0x232: JUMP v22f(0x466)

    Begin block 0x466
    prev=[0x22a], succ=[0x858]
    =================================
    0x467: v467(0x1) = CONST 
    0x469: v469 = SLOAD v467(0x1)
    0x46b: JUMP v22c(0x858)

    Begin block 0x858
    prev=[0x466], succ=[]
    =================================
    0x859: v859(0x40) = CONST 
    0x85c: v85c = MLOAD v859(0x40)
    0x85f: MSTORE v85c, v469
    0x860: v860 = MLOAD v859(0x40)
    0x864: v864(0x0) = SUB v85c, v860
    0x865: v865(0x20) = CONST 
    0x867: v867(0x20) = ADD v865(0x20), v864(0x0)
    0x869: RETURN v860, v867(0x20)

}

function _setPendingImplementation(address)() public {
    Begin block 0x233
    prev=[], succ=[0x23b, 0x23f]
    =================================
    0x234: v234 = CALLVALUE 
    0x236: v236 = ISZERO v234
    0x237: v237(0x23f) = CONST 
    0x23a: JUMPI v237(0x23f), v236

    Begin block 0x23b
    prev=[0x233], succ=[]
    =================================
    0x23b: v23b(0x0) = CONST 
    0x23e: REVERT v23b(0x0), v23b(0x0)

    Begin block 0x23f
    prev=[0x233], succ=[0x252, 0x256]
    =================================
    0x241: v241(0x889) = CONST 
    0x244: v244(0x4) = CONST 
    0x247: v247 = CALLDATASIZE 
    0x248: v248 = SUB v247, v244(0x4)
    0x249: v249(0x20) = CONST 
    0x24c: v24c = LT v248, v249(0x20)
    0x24d: v24d = ISZERO v24c
    0x24e: v24e(0x256) = CONST 
    0x251: JUMPI v24e(0x256), v24d

    Begin block 0x252
    prev=[0x23f], succ=[]
    =================================
    0x252: v252(0x0) = CONST 
    0x255: REVERT v252(0x0), v252(0x0)

    Begin block 0x256
    prev=[0x23f], succ=[0x46c]
    =================================
    0x258: v258 = CALLDATALOAD v244(0x4)
    0x259: v259(0x1) = CONST 
    0x25b: v25b(0x1) = CONST 
    0x25d: v25d(0xa0) = CONST 
    0x25f: v25f(0x10000000000000000000000000000000000000000) = SHL v25d(0xa0), v25b(0x1)
    0x260: v260(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25f(0x10000000000000000000000000000000000000000), v259(0x1)
    0x261: v261 = AND v260(0xffffffffffffffffffffffffffffffffffffffff), v258
    0x262: v262(0x46c) = CONST 
    0x265: JUMP v262(0x46c)

    Begin block 0x46c
    prev=[0x256], succ=[0x482, 0x48d]
    =================================
    0x46d: v46d(0x4) = CONST 
    0x46f: v46f = SLOAD v46d(0x4)
    0x470: v470(0x0) = CONST 
    0x473: v473(0x1) = CONST 
    0x475: v475(0x1) = CONST 
    0x477: v477(0xa0) = CONST 
    0x479: v479(0x10000000000000000000000000000000000000000) = SHL v477(0xa0), v475(0x1)
    0x47a: v47a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v479(0x10000000000000000000000000000000000000000), v473(0x1)
    0x47b: v47b = AND v47a(0xffffffffffffffffffffffffffffffffffffffff), v46f
    0x47c: v47c = CALLER 
    0x47d: v47d = EQ v47c, v47b
    0x47e: v47e(0x48d) = CONST 
    0x481: JUMPI v47e(0x48d), v47d

    Begin block 0x482
    prev=[0x46c], succ=[0x2cc0x233]
    =================================
    0x482: v482(0x2cc) = CONST 
    0x485: v485(0x1) = CONST 
    0x487: v487(0xe) = CONST 
    0x489: v489(0x5e7) = CONST 
    0x48c: v48c_0 = CALLPRIVATE v489(0x5e7), v487(0xe), v485(0x1), v482(0x2cc)

    Begin block 0x2cc0x233
    prev=[0x482], succ=[0x3390x233]
    =================================
    0x2cf0x233: v2332cf(0x339) = CONST 
    0x2d20x233: JUMP v2332cf(0x339)

    Begin block 0x3390x233
    prev=[0x2cc0x233, 0x3350x233], succ=[0x889]
    =================================
    0x33d0x233: JUMP v241(0x889)

    Begin block 0x889
    prev=[0x3390x233], succ=[]
    =================================
    0x889_0x0: v889_0 = PHI v4ec(0x0), v48c_0
    0x88a: v88a(0x40) = CONST 
    0x88d: v88d = MLOAD v88a(0x40)
    0x890: MSTORE v88d, v889_0
    0x891: v891 = MLOAD v88a(0x40)
    0x895: v895(0x0) = SUB v88d, v891
    0x896: v896(0x20) = CONST 
    0x898: v898(0x20) = ADD v896(0x20), v895(0x0)
    0x89a: RETURN v891, v898(0x20)

    Begin block 0x48d
    prev=[0x46c], succ=[0x3350x233]
    =================================
    0x48e: v48e(0x7) = CONST 
    0x491: v491 = SLOAD v48e(0x7)
    0x492: v492(0x1) = CONST 
    0x494: v494(0x1) = CONST 
    0x496: v496(0xa0) = CONST 
    0x498: v498(0x10000000000000000000000000000000000000000) = SHL v496(0xa0), v494(0x1)
    0x499: v499(0xffffffffffffffffffffffffffffffffffffffff) = SUB v498(0x10000000000000000000000000000000000000000), v492(0x1)
    0x49c: v49c = AND v499(0xffffffffffffffffffffffffffffffffffffffff), v261
    0x49d: v49d(0x1) = CONST 
    0x49f: v49f(0x1) = CONST 
    0x4a1: v4a1(0xa0) = CONST 
    0x4a3: v4a3(0x10000000000000000000000000000000000000000) = SHL v4a1(0xa0), v49f(0x1)
    0x4a4: v4a4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a3(0x10000000000000000000000000000000000000000), v49d(0x1)
    0x4a5: v4a5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4a4(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a7: v4a7 = AND v491, v4a5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4a8: v4a8 = OR v4a7, v49c
    0x4ac: SSTORE v48e(0x7), v4a8
    0x4ad: v4ad(0x40) = CONST 
    0x4b0: v4b0 = MLOAD v4ad(0x40)
    0x4b3: v4b3 = AND v499(0xffffffffffffffffffffffffffffffffffffffff), v491
    0x4b6: MSTORE v4b0, v4b3
    0x4ba: v4ba = AND v499(0xffffffffffffffffffffffffffffffffffffffff), v4a8
    0x4bb: v4bb(0x20) = CONST 
    0x4be: v4be = ADD v4b0, v4bb(0x20)
    0x4bf: MSTORE v4be, v4ba
    0x4c1: v4c1 = MLOAD v4ad(0x40)
    0x4c2: v4c2(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x4e6: v4e6(0x0) = SUB v4b0, v4c1
    0x4e9: v4e9(0x40) = ADD v4ad(0x40), v4e6(0x0)
    0x4eb: LOG1 v4c1, v4e9(0x40), v4c2(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x4ec: v4ec(0x0) = CONST 
    0x4ee: v4ee(0x335) = CONST 
    0x4f1: JUMP v4ee(0x335)

    Begin block 0x3350x233
    prev=[0x48d], succ=[0x3390x233]
    =================================

}

function _acceptAdmin()() public {
    Begin block 0x266
    prev=[], succ=[0x26e, 0x272]
    =================================
    0x267: v267 = CALLVALUE 
    0x269: v269 = ISZERO v267
    0x26a: v26a(0x272) = CONST 
    0x26d: JUMPI v26a(0x272), v269

    Begin block 0x26e
    prev=[0x266], succ=[]
    =================================
    0x26e: v26e(0x0) = CONST 
    0x271: REVERT v26e(0x0), v26e(0x0)

    Begin block 0x272
    prev=[0x266], succ=[0x4f2B0x272]
    =================================
    0x274: v274(0x8ba) = CONST 
    0x277: v277(0x4f2) = CONST 
    0x27a: JUMP v277(0x4f2)

    Begin block 0x4f2B0x272
    prev=[0x272], succ=[0x50dB0x272, 0x50aB0x272]
    =================================
    0x4f3S0x272: v4f3V272(0x5) = CONST 
    0x4f5S0x272: v4f5V272 = SLOAD v4f3V272(0x5)
    0x4f6S0x272: v4f6V272(0x0) = CONST 
    0x4f9S0x272: v4f9V272(0x1) = CONST 
    0x4fbS0x272: v4fbV272(0x1) = CONST 
    0x4fdS0x272: v4fdV272(0xa0) = CONST 
    0x4ffS0x272: v4ffV272(0x10000000000000000000000000000000000000000) = SHL v4fdV272(0xa0), v4fbV272(0x1)
    0x500S0x272: v500V272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ffV272(0x10000000000000000000000000000000000000000), v4f9V272(0x1)
    0x501S0x272: v501V272 = AND v500V272(0xffffffffffffffffffffffffffffffffffffffff), v4f5V272
    0x502S0x272: v502V272 = CALLER 
    0x503S0x272: v503V272 = EQ v502V272, v501V272
    0x504S0x272: v504V272 = ISZERO v503V272
    0x506S0x272: v506V272(0x50d) = CONST 
    0x509S0x272: JUMPI v506V272(0x50d), v504V272

    Begin block 0x50dB0x272
    prev=[0x4f2B0x272, 0x50aB0x272], succ=[0x513B0x272, 0x51eB0x272]
    =================================
    0x50d_0x0S0x272: v50d_0V272 = PHI v504V272, v50cV272
    0x50eS0x272: v50eV272 = ISZERO v50d_0V272
    0x50fS0x272: v50fV272(0x51e) = CONST 
    0x512S0x272: JUMPI v50fV272(0x51e), v50eV272

    Begin block 0x513B0x272
    prev=[0x50dB0x272], succ=[0x3920x4f2B0x272]
    =================================
    0x513S0x272: v513V272(0x392) = CONST 
    0x516S0x272: v516V272(0x1) = CONST 
    0x518S0x272: v518V272(0x0) = CONST 
    0x51aS0x272: v51aV272(0x5e7) = CONST 
    0x51dS0x272: v51d_0V272 = CALLPRIVATE v51aV272(0x5e7), v518V272(0x0), v516V272(0x1), v513V272(0x392)

    Begin block 0x3920x4f2B0x272
    prev=[0x513B0x272], succ=[0x4540x4f2B0x272]
    =================================
    0x3950x4f2S0x272: v4f2395V272(0x454) = CONST 
    0x3980x4f2S0x272: JUMP v4f2395V272(0x454)

    Begin block 0x4540x4f2B0x272
    prev=[0x3920x4f2B0x272, 0x44f0x4f2B0x272], succ=[0x8ba]
    =================================
    0x4540x4f2_0x0S0x272: v4544f2_0V272 = PHI v51d_0V272, v5d2V272(0x0)
    0x4560x4f2S0x272: JUMP v274(0x8ba)

    Begin block 0x8ba
    prev=[0x4540x4f2B0x272], succ=[]
    =================================
    0x8bb: v8bb(0x40) = CONST 
    0x8be: v8be = MLOAD v8bb(0x40)
    0x8c1: MSTORE v8be, v4544f2_0V272
    0x8c2: v8c2 = MLOAD v8bb(0x40)
    0x8c6: v8c6(0x0) = SUB v8be, v8c2
    0x8c7: v8c7(0x20) = CONST 
    0x8c9: v8c9(0x20) = ADD v8c7(0x20), v8c6(0x0)
    0x8cb: RETURN v8c2, v8c9(0x20)

    Begin block 0x51eB0x272
    prev=[0x50dB0x272], succ=[0x44f0x4f2B0x272]
    =================================
    0x51fS0x272: v51fV272(0x4) = CONST 
    0x522S0x272: v522V272 = SLOAD v51fV272(0x4)
    0x523S0x272: v523V272(0x5) = CONST 
    0x526S0x272: v526V272 = SLOAD v523V272(0x5)
    0x527S0x272: v527V272(0x1) = CONST 
    0x529S0x272: v529V272(0x1) = CONST 
    0x52bS0x272: v52bV272(0xa0) = CONST 
    0x52dS0x272: v52dV272(0x10000000000000000000000000000000000000000) = SHL v52bV272(0xa0), v529V272(0x1)
    0x52eS0x272: v52eV272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v52dV272(0x10000000000000000000000000000000000000000), v527V272(0x1)
    0x531S0x272: v531V272 = AND v526V272, v52eV272(0xffffffffffffffffffffffffffffffffffffffff)
    0x532S0x272: v532V272(0x1) = CONST 
    0x534S0x272: v534V272(0x1) = CONST 
    0x536S0x272: v536V272(0xa0) = CONST 
    0x538S0x272: v538V272(0x10000000000000000000000000000000000000000) = SHL v536V272(0xa0), v534V272(0x1)
    0x539S0x272: v539V272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v538V272(0x10000000000000000000000000000000000000000), v532V272(0x1)
    0x53aS0x272: v53aV272(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v539V272(0xffffffffffffffffffffffffffffffffffffffff)
    0x53dS0x272: v53dV272 = AND v522V272, v53aV272(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x53fS0x272: v53fV272 = OR v531V272, v53dV272
    0x543S0x272: SSTORE v51fV272(0x4), v53fV272
    0x546S0x272: v546V272 = AND v526V272, v53aV272(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x549S0x272: SSTORE v523V272(0x5), v546V272
    0x54aS0x272: v54aV272(0x40) = CONST 
    0x54dS0x272: v54dV272 = MLOAD v54aV272(0x40)
    0x550S0x272: v550V272 = AND v52eV272(0xffffffffffffffffffffffffffffffffffffffff), v522V272
    0x553S0x272: MSTORE v54dV272, v550V272
    0x557S0x272: v557V272 = AND v52eV272(0xffffffffffffffffffffffffffffffffffffffff), v53fV272
    0x558S0x272: v558V272(0x20) = CONST 
    0x55bS0x272: v55bV272 = ADD v54dV272, v558V272(0x20)
    0x55cS0x272: MSTORE v55bV272, v557V272
    0x55eS0x272: v55eV272 = MLOAD v54aV272(0x40)
    0x561S0x272: v561V272(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x586S0x272: v586V272(0x0) = SUB v54dV272, v55eV272
    0x587S0x272: v587V272(0x40) = ADD v586V272(0x0), v54aV272(0x40)
    0x589S0x272: LOG1 v55eV272, v587V272(0x40), v561V272(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x58aS0x272: v58aV272(0x5) = CONST 
    0x58cS0x272: v58cV272 = SLOAD v58aV272(0x5)
    0x58dS0x272: v58dV272(0x40) = CONST 
    0x590S0x272: v590V272 = MLOAD v58dV272(0x40)
    0x591S0x272: v591V272(0x1) = CONST 
    0x593S0x272: v593V272(0x1) = CONST 
    0x595S0x272: v595V272(0xa0) = CONST 
    0x597S0x272: v597V272(0x10000000000000000000000000000000000000000) = SHL v595V272(0xa0), v593V272(0x1)
    0x598S0x272: v598V272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v597V272(0x10000000000000000000000000000000000000000), v591V272(0x1)
    0x59bS0x272: v59bV272 = AND v531V272, v598V272(0xffffffffffffffffffffffffffffffffffffffff)
    0x59dS0x272: MSTORE v590V272, v59bV272
    0x5a0S0x272: v5a0V272 = AND v58cV272, v598V272(0xffffffffffffffffffffffffffffffffffffffff)
    0x5a1S0x272: v5a1V272(0x20) = CONST 
    0x5a4S0x272: v5a4V272 = ADD v590V272, v5a1V272(0x20)
    0x5a5S0x272: MSTORE v5a4V272, v5a0V272
    0x5a7S0x272: v5a7V272 = MLOAD v58dV272(0x40)
    0x5a8S0x272: v5a8V272(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x5ccS0x272: v5ccV272(0x0) = SUB v590V272, v5a7V272
    0x5cfS0x272: v5cfV272(0x40) = ADD v58dV272(0x40), v5ccV272(0x0)
    0x5d1S0x272: LOG1 v5a7V272, v5cfV272(0x40), v5a8V272(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x5d2S0x272: v5d2V272(0x0) = CONST 
    0x5d4S0x272: v5d4V272(0x44f) = CONST 
    0x5d7S0x272: JUMP v5d4V272(0x44f)

    Begin block 0x44f0x4f2B0x272
    prev=[0x51eB0x272], succ=[0x4540x4f2B0x272]
    =================================

    Begin block 0x50aB0x272
    prev=[0x4f2B0x272], succ=[0x50dB0x272]
    =================================
    0x50bS0x272: v50bV272 = CALLER 
    0x50cS0x272: v50cV272 = ISZERO v50bV272

}

function admin()() public {
    Begin block 0x27b
    prev=[], succ=[0x283, 0x287]
    =================================
    0x27c: v27c = CALLVALUE 
    0x27e: v27e = ISZERO v27c
    0x27f: v27f(0x287) = CONST 
    0x282: JUMPI v27f(0x287), v27e

    Begin block 0x283
    prev=[0x27b], succ=[]
    =================================
    0x283: v283(0x0) = CONST 
    0x286: REVERT v283(0x0), v283(0x0)

    Begin block 0x287
    prev=[0x27b], succ=[0x5d8]
    =================================
    0x289: v289(0x8eb) = CONST 
    0x28c: v28c(0x5d8) = CONST 
    0x28f: JUMP v28c(0x5d8)

    Begin block 0x5d8
    prev=[0x287], succ=[0x8eb]
    =================================
    0x5d9: v5d9(0x4) = CONST 
    0x5db: v5db = SLOAD v5d9(0x4)
    0x5dc: v5dc(0x1) = CONST 
    0x5de: v5de(0x1) = CONST 
    0x5e0: v5e0(0xa0) = CONST 
    0x5e2: v5e2(0x10000000000000000000000000000000000000000) = SHL v5e0(0xa0), v5de(0x1)
    0x5e3: v5e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5e2(0x10000000000000000000000000000000000000000), v5dc(0x1)
    0x5e4: v5e4 = AND v5e3(0xffffffffffffffffffffffffffffffffffffffff), v5db
    0x5e6: JUMP v289(0x8eb)

    Begin block 0x8eb
    prev=[0x5d8], succ=[]
    =================================
    0x8ec: v8ec(0x40) = CONST 
    0x8ef: v8ef = MLOAD v8ec(0x40)
    0x8f0: v8f0(0x1) = CONST 
    0x8f2: v8f2(0x1) = CONST 
    0x8f4: v8f4(0xa0) = CONST 
    0x8f6: v8f6(0x10000000000000000000000000000000000000000) = SHL v8f4(0xa0), v8f2(0x1)
    0x8f7: v8f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8f6(0x10000000000000000000000000000000000000000), v8f0(0x1)
    0x8fa: v8fa = AND v5e4, v8f7(0xffffffffffffffffffffffffffffffffffffffff)
    0x8fc: MSTORE v8ef, v8fa
    0x8fd: v8fd = MLOAD v8ec(0x40)
    0x901: v901(0x0) = SUB v8ef, v8fd
    0x902: v902(0x20) = CONST 
    0x904: v904(0x20) = ADD v902(0x20), v901(0x0)
    0x906: RETURN v8fd, v904(0x20)

}

function 0x5e7(0x5e7arg0x0, 0x5e7arg0x1, 0x5e7arg0x2) private {
    Begin block 0x5e7
    prev=[], succ=[0x615, 0x616]
    =================================
    0x5e8: v5e8(0x0) = CONST 
    0x5ea: v5ea(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0) = CONST 
    0x60c: v60c(0x12) = CONST 
    0x60f: v60f = GT v5e7arg1, v60c(0x12)
    0x610: v610 = ISZERO v60f
    0x611: v611(0x616) = CONST 
    0x614: JUMPI v611(0x616), v610

    Begin block 0x615
    prev=[0x5e7], succ=[]
    =================================
    0x615: THROW 

    Begin block 0x616
    prev=[0x5e7], succ=[0x621, 0x622]
    =================================
    0x618: v618(0x18) = CONST 
    0x61b: v61b = GT v5e7arg0, v618(0x18)
    0x61c: v61c = ISZERO v61b
    0x61d: v61d(0x622) = CONST 
    0x620: JUMPI v61d(0x622), v61c

    Begin block 0x621
    prev=[0x616], succ=[]
    =================================
    0x621: THROW 

    Begin block 0x622
    prev=[0x616], succ=[0x64c, 0x64d]
    =================================
    0x623: v623(0x40) = CONST 
    0x626: v626 = MLOAD v623(0x40)
    0x629: MSTORE v626, v5e7arg1
    0x62a: v62a(0x20) = CONST 
    0x62d: v62d = ADD v626, v62a(0x20)
    0x631: MSTORE v62d, v5e7arg0
    0x632: v632(0x0) = CONST 
    0x636: v636 = ADD v623(0x40), v626
    0x637: MSTORE v636, v632(0x0)
    0x638: v638 = MLOAD v623(0x40)
    0x63c: v63c(0x0) = SUB v626, v638
    0x63d: v63d(0x60) = CONST 
    0x63f: v63f(0x60) = ADD v63d(0x60), v63c(0x0)
    0x641: LOG1 v638, v63f(0x60), v5ea(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0)
    0x643: v643(0x12) = CONST 
    0x646: v646 = GT v5e7arg1, v643(0x12)
    0x647: v647 = ISZERO v646
    0x648: v648(0x64d) = CONST 
    0x64b: JUMPI v648(0x64d), v647

    Begin block 0x64c
    prev=[0x622], succ=[]
    =================================
    0x64c: THROW 

    Begin block 0x64d
    prev=[0x622], succ=[]
    =================================
    0x653: RETURNPRIVATE v5e7arg2, v5e7arg1

}

function fallback()() public {
    Begin block 0xa7
    prev=[], succ=[0xe9, 0x10a]
    =================================
    0xa8: va8(0x6) = CONST 
    0xaa: vaa = SLOAD va8(0x6)
    0xab: vab(0x40) = CONST 
    0xad: vad = MLOAD vab(0x40)
    0xae: vae(0x0) = CONST 
    0xb1: vb1(0x1) = CONST 
    0xb3: vb3(0x1) = CONST 
    0xb5: vb5(0xa0) = CONST 
    0xb7: vb7(0x10000000000000000000000000000000000000000) = SHL vb5(0xa0), vb3(0x1)
    0xb8: vb8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb7(0x10000000000000000000000000000000000000000), vb1(0x1)
    0xb9: vb9 = AND vb8(0xffffffffffffffffffffffffffffffffffffffff), vaa
    0xbd: vbd = CALLDATASIZE 
    0xc5: CALLDATACOPY vad, vae(0x0), vbd
    0xc6: vc6(0x40) = CONST 
    0xc8: vc8 = MLOAD vc6(0x40)
    0xca: vca = ADD vad, vbd
    0xcd: vcd(0x0) = CONST 
    0xd7: vd7 = SUB vca, vc8
    0xda: vda = GAS 
    0xdb: vdb = DELEGATECALL vda, vb9, vc8, vd7, vc8, vcd(0x0)
    0xdf: vdf = RETURNDATASIZE 
    0xe1: ve1(0x0) = CONST 
    0xe4: ve4 = EQ vdf, ve1(0x0)
    0xe5: ve5(0x10a) = CONST 
    0xe8: JUMPI ve5(0x10a), ve4

    Begin block 0xe9
    prev=[0xa7], succ=[0x10f]
    =================================
    0xe9: ve9(0x40) = CONST 
    0xeb: veb = MLOAD ve9(0x40)
    0xee: vee(0x1f) = CONST 
    0xf0: vf0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vee(0x1f)
    0xf1: vf1(0x3f) = CONST 
    0xf3: vf3 = RETURNDATASIZE 
    0xf4: vf4 = ADD vf3, vf1(0x3f)
    0xf5: vf5 = AND vf4, vf0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xf7: vf7 = ADD veb, vf5
    0xf8: vf8(0x40) = CONST 
    0xfa: MSTORE vf8(0x40), vf7
    0xfb: vfb = RETURNDATASIZE 
    0xfd: MSTORE veb, vfb
    0xfe: vfe = RETURNDATASIZE 
    0xff: vff(0x0) = CONST 
    0x101: v101(0x20) = CONST 
    0x104: v104 = ADD veb, v101(0x20)
    0x105: RETURNDATACOPY v104, vff(0x0), vfe
    0x106: v106(0x10f) = CONST 
    0x109: JUMP v106(0x10f)

    Begin block 0x10f
    prev=[0xe9, 0x10a], succ=[0x123, 0x126]
    =================================
    0x114: v114(0x40) = CONST 
    0x116: v116 = MLOAD v114(0x40)
    0x117: v117 = RETURNDATASIZE 
    0x118: v118(0x0) = CONST 
    0x11b: RETURNDATACOPY v116, v118(0x0), v117
    0x11e: v11e = ISZERO vdb
    0x11f: v11f(0x126) = CONST 
    0x122: JUMPI v11f(0x126), v11e

    Begin block 0x123
    prev=[0x10f], succ=[]
    =================================
    0x123: v123 = RETURNDATASIZE 
    0x125: RETURN v116, v123

    Begin block 0x126
    prev=[0x10f], succ=[]
    =================================
    0x127: v127 = RETURNDATASIZE 
    0x129: REVERT v116, v127

    Begin block 0x10a
    prev=[0xa7], succ=[0x10f]
    =================================
    0x10b: v10b(0x60) = CONST 

}

