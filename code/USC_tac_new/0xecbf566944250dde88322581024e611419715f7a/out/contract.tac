function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8d8]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x8cc: v8cc(0x8d8) = CONST 
    0x8cd: JUMPI v8cc(0x8d8), v8

    Begin block 0xd
    prev=[0x0], succ=[0x3b, 0x8db]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x31: v31(0x3659cfe6) = CONST 
    0x36: v36 = EQ v31(0x3659cfe6), v2f
    0x8ce: v8ce(0x8db) = CONST 
    0x8cf: JUMPI v8ce(0x8db), v36

    Begin block 0x3b
    prev=[0xd], succ=[0x8de, 0x46]
    =================================
    0x3c: v3c(0x4f1ef286) = CONST 
    0x41: v41 = EQ v3c(0x4f1ef286), v2f
    0x8d0: v8d0(0x8de) = CONST 
    0x8d1: JUMPI v8d0(0x8de), v41

    Begin block 0x8de
    prev=[0x3b], succ=[]
    =================================
    0x8df: v8df(0xc2) = CONST 
    0x8e0: CALLPRIVATE v8df(0xc2)

    Begin block 0x46
    prev=[0x3b], succ=[0x8e1, 0x51]
    =================================
    0x47: v47(0x5c60da1b) = CONST 
    0x4c: v4c = EQ v47(0x5c60da1b), v2f
    0x8d2: v8d2(0x8e1) = CONST 
    0x8d3: JUMPI v8d2(0x8e1), v4c

    Begin block 0x8e1
    prev=[0x46], succ=[]
    =================================
    0x8e2: v8e2(0x15b) = CONST 
    0x8e3: CALLPRIVATE v8e2(0x15b)

    Begin block 0x51
    prev=[0x46], succ=[0x8e4, 0x5c]
    =================================
    0x52: v52(0x8f283970) = CONST 
    0x57: v57 = EQ v52(0x8f283970), v2f
    0x8d4: v8d4(0x8e4) = CONST 
    0x8d5: JUMPI v8d4(0x8e4), v57

    Begin block 0x8e4
    prev=[0x51], succ=[]
    =================================
    0x8e5: v8e5(0x1b2) = CONST 
    0x8e6: CALLPRIVATE v8e5(0x1b2)

    Begin block 0x5c
    prev=[0x51], succ=[0x8d8, 0x8e7]
    =================================
    0x5d: v5d(0xf851a440) = CONST 
    0x62: v62 = EQ v5d(0xf851a440), v2f
    0x8d6: v8d6(0x8e7) = CONST 
    0x8d7: JUMPI v8d6(0x8e7), v62

    Begin block 0x8d8
    prev=[0x0, 0x5c], succ=[]
    =================================
    0x8d9: v8d9(0x67) = CONST 
    0x8da: CALLPRIVATE v8d9(0x67)

    Begin block 0x8e7
    prev=[0x5c], succ=[]
    =================================
    0x8e8: v8e8(0x203) = CONST 
    0x8e9: CALLPRIVATE v8e8(0x203)

    Begin block 0x8db
    prev=[0xd], succ=[]
    =================================
    0x8dc: v8dc(0x71) = CONST 
    0x8dd: CALLPRIVATE v8dc(0x71)

}

function implementation()() public {
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
    prev=[0x15b], succ=[0x170]
    =================================
    0x169: v169(0x170) = CONST 
    0x16c: v16c(0x3a1) = CONST 
    0x16f: v16f_0 = CALLPRIVATE v16c(0x3a1), v169(0x170)

    Begin block 0x170
    prev=[0x167], succ=[]
    =================================
    0x171: v171(0x40) = CONST 
    0x173: v173 = MLOAD v171(0x40)
    0x176: v176(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18b: v18b = AND v176(0xffffffffffffffffffffffffffffffffffffffff), v16f_0
    0x18c: v18c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a1: v1a1 = AND v18c(0xffffffffffffffffffffffffffffffffffffffff), v18b
    0x1a3: MSTORE v173, v1a1
    0x1a4: v1a4(0x20) = CONST 
    0x1a6: v1a6 = ADD v1a4(0x20), v173
    0x1aa: v1aa(0x40) = CONST 
    0x1ac: v1ac = MLOAD v1aa(0x40)
    0x1af: v1af(0x20) = SUB v1a6, v1ac
    0x1b1: RETURN v1ac, v1af(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x1b2
    prev=[], succ=[0x1ba, 0x1be]
    =================================
    0x1b3: v1b3 = CALLVALUE 
    0x1b5: v1b5 = ISZERO v1b3
    0x1b6: v1b6(0x1be) = CONST 
    0x1b9: JUMPI v1b6(0x1be), v1b5

    Begin block 0x1ba
    prev=[0x1b2], succ=[]
    =================================
    0x1ba: v1ba(0x0) = CONST 
    0x1bd: REVERT v1ba(0x0), v1ba(0x0)

    Begin block 0x1be
    prev=[0x1b2], succ=[0x1d1, 0x1d5]
    =================================
    0x1c0: v1c0(0x201) = CONST 
    0x1c3: v1c3(0x4) = CONST 
    0x1c6: v1c6 = CALLDATASIZE 
    0x1c7: v1c7 = SUB v1c6, v1c3(0x4)
    0x1c8: v1c8(0x20) = CONST 
    0x1cb: v1cb = LT v1c7, v1c8(0x20)
    0x1cc: v1cc = ISZERO v1cb
    0x1cd: v1cd(0x1d5) = CONST 
    0x1d0: JUMPI v1cd(0x1d5), v1cc

    Begin block 0x1d1
    prev=[0x1be], succ=[]
    =================================
    0x1d1: v1d1(0x0) = CONST 
    0x1d4: REVERT v1d1(0x0), v1d1(0x0)

    Begin block 0x1d5
    prev=[0x1be], succ=[0x3f9]
    =================================
    0x1d7: v1d7 = ADD v1c3(0x4), v1c7
    0x1db: v1db = CALLDATALOAD v1c3(0x4)
    0x1dc: v1dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f1: v1f1 = AND v1dc(0xffffffffffffffffffffffffffffffffffffffff), v1db
    0x1f3: v1f3(0x20) = CONST 
    0x1f5: v1f5(0x24) = ADD v1f3(0x20), v1c3(0x4)
    0x1fd: v1fd(0x3f9) = CONST 
    0x200: JUMP v1fd(0x3f9)

    Begin block 0x3f9
    prev=[0x1d5], succ=[0x6bbB0x3f9]
    =================================
    0x3fa: v3fa(0x401) = CONST 
    0x3fd: v3fd(0x6bb) = CONST 
    0x400: JUMP v3fd(0x6bb)

    Begin block 0x6bbB0x3f9
    prev=[0x3f9], succ=[0x401]
    =================================
    0x6bcS0x3f9: v6bcV3f9(0x0) = CONST 
    0x6bfS0x3f9: v6bfV3f9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x3f9: v6e0V3f9(0x1) = CONST 
    0x6e2S0x3f9: v6e2V3f9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V3f9(0x1), v6bfV3f9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x3f9: v6e6V3f9 = SLOAD v6e2V3f9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x3f9: JUMP v3fa(0x401)

    Begin block 0x401
    prev=[0x6bbB0x3f9], succ=[0x435, 0x568]
    =================================
    0x402: v402(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x417: v417 = AND v402(0xffffffffffffffffffffffffffffffffffffffff), v6e6V3f9
    0x418: v418 = CALLER 
    0x419: v419(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42e: v42e = AND v419(0xffffffffffffffffffffffffffffffffffffffff), v418
    0x42f: v42f = EQ v42e, v417
    0x430: v430 = ISZERO v42f
    0x431: v431(0x568) = CONST 
    0x434: JUMPI v431(0x568), v430

    Begin block 0x435
    prev=[0x401], succ=[0x46c, 0x4bc]
    =================================
    0x435: v435(0x0) = CONST 
    0x437: v437(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x44c: v44c(0x0) = AND v437(0xffffffffffffffffffffffffffffffffffffffff), v435(0x0)
    0x44e: v44e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x463: v463 = AND v44e(0xffffffffffffffffffffffffffffffffffffffff), v1f1
    0x464: v464 = EQ v463, v44c(0x0)
    0x465: v465 = ISZERO v464
    0x466: v466 = ISZERO v465
    0x467: v467 = ISZERO v466
    0x468: v468(0x4bc) = CONST 
    0x46b: JUMPI v468(0x4bc), v467

    Begin block 0x46c
    prev=[0x435], succ=[]
    =================================
    0x46c: v46c(0x40) = CONST 
    0x46e: v46e = MLOAD v46c(0x40)
    0x46f: v46f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x491: MSTORE v46e, v46f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x492: v492(0x4) = CONST 
    0x494: v494 = ADD v492(0x4), v46e
    0x497: v497(0x20) = CONST 
    0x499: v499 = ADD v497(0x20), v494
    0x49c: v49c(0x20) = SUB v499, v494
    0x49e: MSTORE v494, v49c(0x20)
    0x49f: v49f(0x36) = CONST 
    0x4a2: MSTORE v499, v49f(0x36)
    0x4a3: v4a3(0x20) = CONST 
    0x4a5: v4a5 = ADD v4a3(0x20), v499
    0x4a7: v4a7(0x841) = CONST 
    0x4aa: v4aa(0x36) = CONST 
    0x4ad: CODECOPY v4a5, v4a7(0x841), v4aa(0x36)
    0x4ae: v4ae(0x40) = CONST 
    0x4b0: v4b0 = ADD v4ae(0x40), v4a5
    0x4b4: v4b4(0x40) = CONST 
    0x4b6: v4b6 = MLOAD v4b4(0x40)
    0x4b9: v4b9(0x84) = SUB v4b0, v4b6
    0x4bb: REVERT v4b6, v4b9(0x84)

    Begin block 0x4bc
    prev=[0x435], succ=[0x6bbB0x4bc]
    =================================
    0x4bd: v4bd(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x4de: v4de(0x4e5) = CONST 
    0x4e1: v4e1(0x6bb) = CONST 
    0x4e4: JUMP v4e1(0x6bb)

    Begin block 0x6bbB0x4bc
    prev=[0x4bc], succ=[0x4e5]
    =================================
    0x6bcS0x4bc: v6bcV4bc(0x0) = CONST 
    0x6bfS0x4bc: v6bfV4bc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x4bc: v6e0V4bc(0x1) = CONST 
    0x6e2S0x4bc: v6e2V4bc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V4bc(0x1), v6bfV4bc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x4bc: v6e6V4bc = SLOAD v6e2V4bc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x4bc: JUMP v4de(0x4e5)

    Begin block 0x4e5
    prev=[0x6bbB0x4bc], succ=[0x73b]
    =================================
    0x4e7: v4e7(0x40) = CONST 
    0x4e9: v4e9 = MLOAD v4e7(0x40)
    0x4ec: v4ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x501: v501 = AND v4ec(0xffffffffffffffffffffffffffffffffffffffff), v6e6V4bc
    0x502: v502(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x517: v517 = AND v502(0xffffffffffffffffffffffffffffffffffffffff), v501
    0x519: MSTORE v4e9, v517
    0x51a: v51a(0x20) = CONST 
    0x51c: v51c = ADD v51a(0x20), v4e9
    0x51e: v51e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x533: v533 = AND v51e(0xffffffffffffffffffffffffffffffffffffffff), v1f1
    0x534: v534(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x549: v549 = AND v534(0xffffffffffffffffffffffffffffffffffffffff), v533
    0x54b: MSTORE v51c, v549
    0x54c: v54c(0x20) = CONST 
    0x54e: v54e = ADD v54c(0x20), v51c
    0x553: v553(0x40) = CONST 
    0x555: v555 = MLOAD v553(0x40)
    0x558: v558(0x40) = SUB v54e, v555
    0x55a: LOG1 v555, v558(0x40), v4bd(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x55b: v55b(0x563) = CONST 
    0x55f: v55f(0x73b) = CONST 
    0x562: JUMP v55f(0x73b)

    Begin block 0x73b
    prev=[0x4e5], succ=[0x563]
    =================================
    0x73c: v73c(0x0) = CONST 
    0x73e: v73e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x75f: v75f(0x1) = CONST 
    0x761: v761(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v75f(0x1), v73e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x766: SSTORE v761(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b), v1f1
    0x769: JUMP v55b(0x563)

    Begin block 0x563
    prev=[0x73b], succ=[0x571]
    =================================
    0x564: v564(0x571) = CONST 
    0x567: JUMP v564(0x571)

    Begin block 0x571
    prev=[0x563], succ=[0x201]
    =================================
    0x573: JUMP v1c0(0x201)

    Begin block 0x201
    prev=[0x571], succ=[]
    =================================
    0x202: STOP 

    Begin block 0x568
    prev=[0x401], succ=[0x25a0x1b2]
    =================================
    0x569: v569(0x570) = CONST 
    0x56c: v56c(0x25a) = CONST 
    0x56f: JUMP v56c(0x25a)

    Begin block 0x25a0x1b2
    prev=[0x568], succ=[0x2620x1b2]
    =================================
    0x25b0x1b2: v1b225b(0x262) = CONST 
    0x25e0x1b2: v1b225e(0x5cc) = CONST 
    0x2610x1b2: CALLPRIVATE v1b225e(0x5cc), v1b225b(0x262)

    Begin block 0x2620x1b2
    prev=[0x25a0x1b2], succ=[0x664B0x2620x1b2]
    =================================
    0x2630x1b2: v1b2263(0x272) = CONST 
    0x2660x1b2: v1b2266(0x26d) = CONST 
    0x2690x1b2: v1b2269(0x664) = CONST 
    0x26c0x1b2: JUMP v1b2269(0x664)

    Begin block 0x664B0x2620x1b2
    prev=[0x2620x1b2], succ=[0x26d0x1b2]
    =================================
    0x665S0x2620x1b2: v665V2621b2(0x0) = CONST 
    0x668S0x2620x1b2: v668V2621b2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620x1b2: v689V2621b2(0x1) = CONST 
    0x68bS0x2620x1b2: v68bV2621b2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V2621b2(0x1), v668V2621b2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620x1b2: v68fV2621b2 = SLOAD v68bV2621b2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620x1b2: JUMP v1b2266(0x26d)

    Begin block 0x26d0x1b2
    prev=[0x664B0x2620x1b2], succ=[0x6950x1b2]
    =================================
    0x26e0x1b2: v1b226e(0x695) = CONST 
    0x2710x1b2: JUMP v1b226e(0x695)

    Begin block 0x6950x1b2
    prev=[0x26d0x1b2], succ=[0x6b20x1b2, 0x6b60x1b2]
    =================================
    0x6960x1b2: v1b2696 = CALLDATASIZE 
    0x6970x1b2: v1b2697(0x0) = CONST 
    0x69a0x1b2: CALLDATACOPY v1b2697(0x0), v1b2697(0x0), v1b2696
    0x69b0x1b2: v1b269b(0x0) = CONST 
    0x69e0x1b2: v1b269e = CALLDATASIZE 
    0x69f0x1b2: v1b269f(0x0) = CONST 
    0x6a20x1b2: v1b26a2 = GAS 
    0x6a30x1b2: v1b26a3 = DELEGATECALL v1b26a2, v68fV2621b2, v1b269f(0x0), v1b269e, v1b269b(0x0), v1b269b(0x0)
    0x6a40x1b2: v1b26a4 = RETURNDATASIZE 
    0x6a50x1b2: v1b26a5(0x0) = CONST 
    0x6a80x1b2: RETURNDATACOPY v1b26a5(0x0), v1b26a5(0x0), v1b26a4
    0x6aa0x1b2: v1b26aa(0x0) = CONST 
    0x6ad0x1b2: v1b26ad = EQ v1b26a3, v1b26aa(0x0)
    0x6ae0x1b2: v1b26ae(0x6b6) = CONST 
    0x6b10x1b2: JUMPI v1b26ae(0x6b6), v1b26ad

    Begin block 0x6b20x1b2
    prev=[0x6950x1b2], succ=[]
    =================================
    0x6b20x1b2: v1b26b2 = RETURNDATASIZE 
    0x6b30x1b2: v1b26b3(0x0) = CONST 
    0x6b50x1b2: RETURN v1b26b3(0x0), v1b26b2

    Begin block 0x6b60x1b2
    prev=[0x6950x1b2], succ=[]
    =================================
    0x6b70x1b2: v1b26b7 = RETURNDATASIZE 
    0x6b80x1b2: v1b26b8(0x0) = CONST 
    0x6ba0x1b2: REVERT v1b26b8(0x0), v1b26b7

}

function admin()() public {
    Begin block 0x203
    prev=[], succ=[0x20b, 0x20f]
    =================================
    0x204: v204 = CALLVALUE 
    0x206: v206 = ISZERO v204
    0x207: v207(0x20f) = CONST 
    0x20a: JUMPI v207(0x20f), v206

    Begin block 0x20b
    prev=[0x203], succ=[]
    =================================
    0x20b: v20b(0x0) = CONST 
    0x20e: REVERT v20b(0x0), v20b(0x0)

    Begin block 0x20f
    prev=[0x203], succ=[0x218]
    =================================
    0x211: v211(0x218) = CONST 
    0x214: v214(0x574) = CONST 
    0x217: v217_0 = CALLPRIVATE v214(0x574), v211(0x218)

    Begin block 0x218
    prev=[0x20f], succ=[]
    =================================
    0x219: v219(0x40) = CONST 
    0x21b: v21b = MLOAD v219(0x40)
    0x21e: v21e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x233: v233 = AND v21e(0xffffffffffffffffffffffffffffffffffffffff), v217_0
    0x234: v234(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x249: v249 = AND v234(0xffffffffffffffffffffffffffffffffffffffff), v233
    0x24b: MSTORE v21b, v249
    0x24c: v24c(0x20) = CONST 
    0x24e: v24e = ADD v24c(0x20), v21b
    0x252: v252(0x40) = CONST 
    0x254: v254 = MLOAD v252(0x40)
    0x257: v257(0x20) = SUB v24e, v254
    0x259: RETURN v254, v257(0x20)

}

function 0x3a1(0x3a1arg0x0) private {
    Begin block 0x3a1
    prev=[], succ=[0x6bbB0x3a1]
    =================================
    0x3a2: v3a2(0x0) = CONST 
    0x3a4: v3a4(0x3ab) = CONST 
    0x3a7: v3a7(0x6bb) = CONST 
    0x3aa: JUMP v3a7(0x6bb)

    Begin block 0x6bbB0x3a1
    prev=[0x3a1], succ=[0x3ab]
    =================================
    0x6bcS0x3a1: v6bcV3a1(0x0) = CONST 
    0x6bfS0x3a1: v6bfV3a1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x3a1: v6e0V3a1(0x1) = CONST 
    0x6e2S0x3a1: v6e2V3a1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V3a1(0x1), v6bfV3a1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x3a1: v6e6V3a1 = SLOAD v6e2V3a1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x3a1: JUMP v3a4(0x3ab)

    Begin block 0x3ab
    prev=[0x6bbB0x3a1], succ=[0x3df, 0x3ed]
    =================================
    0x3ac: v3ac(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c1: v3c1 = AND v3ac(0xffffffffffffffffffffffffffffffffffffffff), v6e6V3a1
    0x3c2: v3c2 = CALLER 
    0x3c3: v3c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3d8: v3d8 = AND v3c3(0xffffffffffffffffffffffffffffffffffffffff), v3c2
    0x3d9: v3d9 = EQ v3d8, v3c1
    0x3da: v3da = ISZERO v3d9
    0x3db: v3db(0x3ed) = CONST 
    0x3de: JUMPI v3db(0x3ed), v3da

    Begin block 0x3df
    prev=[0x3ab], succ=[0x664B0x3df]
    =================================
    0x3df: v3df(0x3e6) = CONST 
    0x3e2: v3e2(0x664) = CONST 
    0x3e5: JUMP v3e2(0x664)

    Begin block 0x664B0x3df
    prev=[0x3df], succ=[0x3e6]
    =================================
    0x665S0x3df: v665V3df(0x0) = CONST 
    0x668S0x3df: v668V3df(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x3df: v689V3df(0x1) = CONST 
    0x68bS0x3df: v68bV3df(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V3df(0x1), v668V3df(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x3df: v68fV3df = SLOAD v68bV3df(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x3df: JUMP v3df(0x3e6)

    Begin block 0x3e6
    prev=[0x664B0x3df], succ=[0x3f6]
    =================================
    0x3e9: v3e9(0x3f6) = CONST 
    0x3ec: JUMP v3e9(0x3f6)

    Begin block 0x3f6
    prev=[0x3e6], succ=[]
    =================================
    0x3f8: RETURNPRIVATE v3a1arg0, v68fV3df

    Begin block 0x3ed
    prev=[0x3ab], succ=[0x25a0x3a1]
    =================================
    0x3ee: v3ee(0x3f5) = CONST 
    0x3f1: v3f1(0x25a) = CONST 
    0x3f4: JUMP v3f1(0x25a)

    Begin block 0x25a0x3a1
    prev=[0x3ed], succ=[0x2620x3a1]
    =================================
    0x25b0x3a1: v3a125b(0x262) = CONST 
    0x25e0x3a1: v3a125e(0x5cc) = CONST 
    0x2610x3a1: CALLPRIVATE v3a125e(0x5cc), v3a125b(0x262)

    Begin block 0x2620x3a1
    prev=[0x25a0x3a1], succ=[0x664B0x2620x3a1]
    =================================
    0x2630x3a1: v3a1263(0x272) = CONST 
    0x2660x3a1: v3a1266(0x26d) = CONST 
    0x2690x3a1: v3a1269(0x664) = CONST 
    0x26c0x3a1: JUMP v3a1269(0x664)

    Begin block 0x664B0x2620x3a1
    prev=[0x2620x3a1], succ=[0x26d0x3a1]
    =================================
    0x665S0x2620x3a1: v665V2623a1(0x0) = CONST 
    0x668S0x2620x3a1: v668V2623a1(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620x3a1: v689V2623a1(0x1) = CONST 
    0x68bS0x2620x3a1: v68bV2623a1(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V2623a1(0x1), v668V2623a1(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620x3a1: v68fV2623a1 = SLOAD v68bV2623a1(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620x3a1: JUMP v3a1266(0x26d)

    Begin block 0x26d0x3a1
    prev=[0x664B0x2620x3a1], succ=[0x6950x3a1]
    =================================
    0x26e0x3a1: v3a126e(0x695) = CONST 
    0x2710x3a1: JUMP v3a126e(0x695)

    Begin block 0x6950x3a1
    prev=[0x26d0x3a1], succ=[0x6b20x3a1, 0x6b60x3a1]
    =================================
    0x6960x3a1: v3a1696 = CALLDATASIZE 
    0x6970x3a1: v3a1697(0x0) = CONST 
    0x69a0x3a1: CALLDATACOPY v3a1697(0x0), v3a1697(0x0), v3a1696
    0x69b0x3a1: v3a169b(0x0) = CONST 
    0x69e0x3a1: v3a169e = CALLDATASIZE 
    0x69f0x3a1: v3a169f(0x0) = CONST 
    0x6a20x3a1: v3a16a2 = GAS 
    0x6a30x3a1: v3a16a3 = DELEGATECALL v3a16a2, v68fV2623a1, v3a169f(0x0), v3a169e, v3a169b(0x0), v3a169b(0x0)
    0x6a40x3a1: v3a16a4 = RETURNDATASIZE 
    0x6a50x3a1: v3a16a5(0x0) = CONST 
    0x6a80x3a1: RETURNDATACOPY v3a16a5(0x0), v3a16a5(0x0), v3a16a4
    0x6aa0x3a1: v3a16aa(0x0) = CONST 
    0x6ad0x3a1: v3a16ad = EQ v3a16a3, v3a16aa(0x0)
    0x6ae0x3a1: v3a16ae(0x6b6) = CONST 
    0x6b10x3a1: JUMPI v3a16ae(0x6b6), v3a16ad

    Begin block 0x6b20x3a1
    prev=[0x6950x3a1], succ=[]
    =================================
    0x6b20x3a1: v3a16b2 = RETURNDATASIZE 
    0x6b30x3a1: v3a16b3(0x0) = CONST 
    0x6b50x3a1: RETURN v3a16b3(0x0), v3a16b2

    Begin block 0x6b60x3a1
    prev=[0x6950x3a1], succ=[]
    =================================
    0x6b70x3a1: v3a16b7 = RETURNDATASIZE 
    0x6b80x3a1: v3a16b8(0x0) = CONST 
    0x6ba0x3a1: REVERT v3a16b8(0x0), v3a16b7

}

function 0x574(0x574arg0x0) private {
    Begin block 0x574
    prev=[], succ=[0x6bbB0x574]
    =================================
    0x575: v575(0x0) = CONST 
    0x577: v577(0x57e) = CONST 
    0x57a: v57a(0x6bb) = CONST 
    0x57d: JUMP v57a(0x6bb)

    Begin block 0x6bbB0x574
    prev=[0x574], succ=[0x57e]
    =================================
    0x6bcS0x574: v6bcV574(0x0) = CONST 
    0x6bfS0x574: v6bfV574(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x574: v6e0V574(0x1) = CONST 
    0x6e2S0x574: v6e2V574(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V574(0x1), v6bfV574(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x574: v6e6V574 = SLOAD v6e2V574(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x574: JUMP v577(0x57e)

    Begin block 0x57e
    prev=[0x6bbB0x574], succ=[0x5b2, 0x5c0]
    =================================
    0x57f: v57f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x594: v594 = AND v57f(0xffffffffffffffffffffffffffffffffffffffff), v6e6V574
    0x595: v595 = CALLER 
    0x596: v596(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ab: v5ab = AND v596(0xffffffffffffffffffffffffffffffffffffffff), v595
    0x5ac: v5ac = EQ v5ab, v594
    0x5ad: v5ad = ISZERO v5ac
    0x5ae: v5ae(0x5c0) = CONST 
    0x5b1: JUMPI v5ae(0x5c0), v5ad

    Begin block 0x5b2
    prev=[0x57e], succ=[0x6bbB0x5b2]
    =================================
    0x5b2: v5b2(0x5b9) = CONST 
    0x5b5: v5b5(0x6bb) = CONST 
    0x5b8: JUMP v5b5(0x6bb)

    Begin block 0x6bbB0x5b2
    prev=[0x5b2], succ=[0x5b9]
    =================================
    0x6bcS0x5b2: v6bcV5b2(0x0) = CONST 
    0x6bfS0x5b2: v6bfV5b2(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x5b2: v6e0V5b2(0x1) = CONST 
    0x6e2S0x5b2: v6e2V5b2(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V5b2(0x1), v6bfV5b2(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x5b2: v6e6V5b2 = SLOAD v6e2V5b2(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x5b2: JUMP v5b2(0x5b9)

    Begin block 0x5b9
    prev=[0x6bbB0x5b2], succ=[0x5c9]
    =================================
    0x5bc: v5bc(0x5c9) = CONST 
    0x5bf: JUMP v5bc(0x5c9)

    Begin block 0x5c9
    prev=[0x5b9], succ=[]
    =================================
    0x5cb: RETURNPRIVATE v574arg0, v6e6V5b2

    Begin block 0x5c0
    prev=[0x57e], succ=[0x25a0x574]
    =================================
    0x5c1: v5c1(0x5c8) = CONST 
    0x5c4: v5c4(0x25a) = CONST 
    0x5c7: JUMP v5c4(0x25a)

    Begin block 0x25a0x574
    prev=[0x5c0], succ=[0x2620x574]
    =================================
    0x25b0x574: v57425b(0x262) = CONST 
    0x25e0x574: v57425e(0x5cc) = CONST 
    0x2610x574: CALLPRIVATE v57425e(0x5cc), v57425b(0x262)

    Begin block 0x2620x574
    prev=[0x25a0x574], succ=[0x664B0x2620x574]
    =================================
    0x2630x574: v574263(0x272) = CONST 
    0x2660x574: v574266(0x26d) = CONST 
    0x2690x574: v574269(0x664) = CONST 
    0x26c0x574: JUMP v574269(0x664)

    Begin block 0x664B0x2620x574
    prev=[0x2620x574], succ=[0x26d0x574]
    =================================
    0x665S0x2620x574: v665V262574(0x0) = CONST 
    0x668S0x2620x574: v668V262574(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620x574: v689V262574(0x1) = CONST 
    0x68bS0x2620x574: v68bV262574(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V262574(0x1), v668V262574(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620x574: v68fV262574 = SLOAD v68bV262574(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620x574: JUMP v574266(0x26d)

    Begin block 0x26d0x574
    prev=[0x664B0x2620x574], succ=[0x6950x574]
    =================================
    0x26e0x574: v57426e(0x695) = CONST 
    0x2710x574: JUMP v57426e(0x695)

    Begin block 0x6950x574
    prev=[0x26d0x574], succ=[0x6b20x574, 0x6b60x574]
    =================================
    0x6960x574: v574696 = CALLDATASIZE 
    0x6970x574: v574697(0x0) = CONST 
    0x69a0x574: CALLDATACOPY v574697(0x0), v574697(0x0), v574696
    0x69b0x574: v57469b(0x0) = CONST 
    0x69e0x574: v57469e = CALLDATASIZE 
    0x69f0x574: v57469f(0x0) = CONST 
    0x6a20x574: v5746a2 = GAS 
    0x6a30x574: v5746a3 = DELEGATECALL v5746a2, v68fV262574, v57469f(0x0), v57469e, v57469b(0x0), v57469b(0x0)
    0x6a40x574: v5746a4 = RETURNDATASIZE 
    0x6a50x574: v5746a5(0x0) = CONST 
    0x6a80x574: RETURNDATACOPY v5746a5(0x0), v5746a5(0x0), v5746a4
    0x6aa0x574: v5746aa(0x0) = CONST 
    0x6ad0x574: v5746ad = EQ v5746a3, v5746aa(0x0)
    0x6ae0x574: v5746ae(0x6b6) = CONST 
    0x6b10x574: JUMPI v5746ae(0x6b6), v5746ad

    Begin block 0x6b20x574
    prev=[0x6950x574], succ=[]
    =================================
    0x6b20x574: v5746b2 = RETURNDATASIZE 
    0x6b30x574: v5746b3(0x0) = CONST 
    0x6b50x574: RETURN v5746b3(0x0), v5746b2

    Begin block 0x6b60x574
    prev=[0x6950x574], succ=[]
    =================================
    0x6b70x574: v5746b7 = RETURNDATASIZE 
    0x6b80x574: v5746b8(0x0) = CONST 
    0x6ba0x574: REVERT v5746b8(0x0), v5746b7

}

function 0x5cc(0x5ccarg0x0) private {
    Begin block 0x5cc
    prev=[], succ=[0x6bbB0x5cc]
    =================================
    0x5cd: v5cd(0x5d4) = CONST 
    0x5d0: v5d0(0x6bb) = CONST 
    0x5d3: JUMP v5d0(0x6bb)

    Begin block 0x6bbB0x5cc
    prev=[0x5cc], succ=[0x5d4]
    =================================
    0x6bcS0x5cc: v6bcV5cc(0x0) = CONST 
    0x6bfS0x5cc: v6bfV5cc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x5cc: v6e0V5cc(0x1) = CONST 
    0x6e2S0x5cc: v6e2V5cc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V5cc(0x1), v6bfV5cc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x5cc: v6e6V5cc = SLOAD v6e2V5cc(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x5cc: JUMP v5cd(0x5d4)

    Begin block 0x5d4
    prev=[0x6bbB0x5cc], succ=[0x60a, 0x65a]
    =================================
    0x5d5: v5d5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ea: v5ea = AND v5d5(0xffffffffffffffffffffffffffffffffffffffff), v6e6V5cc
    0x5eb: v5eb = CALLER 
    0x5ec: v5ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x601: v601 = AND v5ec(0xffffffffffffffffffffffffffffffffffffffff), v5eb
    0x602: v602 = EQ v601, v5ea
    0x603: v603 = ISZERO v602
    0x604: v604 = ISZERO v603
    0x605: v605 = ISZERO v604
    0x606: v606(0x65a) = CONST 
    0x609: JUMPI v606(0x65a), v605

    Begin block 0x60a
    prev=[0x5d4], succ=[]
    =================================
    0x60a: v60a(0x40) = CONST 
    0x60c: v60c = MLOAD v60a(0x40)
    0x60d: v60d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x62f: MSTORE v60c, v60d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x630: v630(0x4) = CONST 
    0x632: v632 = ADD v630(0x4), v60c
    0x635: v635(0x20) = CONST 
    0x637: v637 = ADD v635(0x20), v632
    0x63a: v63a(0x20) = SUB v637, v632
    0x63c: MSTORE v632, v63a(0x20)
    0x63d: v63d(0x32) = CONST 
    0x640: MSTORE v637, v63d(0x32)
    0x641: v641(0x20) = CONST 
    0x643: v643 = ADD v641(0x20), v637
    0x645: v645(0x80f) = CONST 
    0x648: v648(0x32) = CONST 
    0x64b: CODECOPY v643, v645(0x80f), v648(0x32)
    0x64c: v64c(0x40) = CONST 
    0x64e: v64e = ADD v64c(0x40), v643
    0x652: v652(0x40) = CONST 
    0x654: v654 = MLOAD v652(0x40)
    0x657: v657(0x84) = SUB v64e, v654
    0x659: REVERT v654, v657(0x84)

    Begin block 0x65a
    prev=[0x5d4], succ=[0x76aB0x65a]
    =================================
    0x65b: v65b(0x662) = CONST 
    0x65e: v65e(0x76a) = CONST 
    0x661: JUMP v65e(0x76a), v65b(0x662)

    Begin block 0x76aB0x65a
    prev=[0x65a], succ=[0x662]
    =================================
    0x76bS0x65a: JUMP v65b(0x662)

    Begin block 0x662
    prev=[0x76aB0x65a], succ=[]
    =================================
    0x663: RETURNPRIVATE v5ccarg0

}

function fallback()() public {
    Begin block 0x67
    prev=[], succ=[0x25a0x67]
    =================================
    0x68: v68(0x6f) = CONST 
    0x6b: v6b(0x25a) = CONST 
    0x6e: JUMP v6b(0x25a)

    Begin block 0x25a0x67
    prev=[0x67], succ=[0x2620x67]
    =================================
    0x25b0x67: v6725b(0x262) = CONST 
    0x25e0x67: v6725e(0x5cc) = CONST 
    0x2610x67: CALLPRIVATE v6725e(0x5cc), v6725b(0x262)

    Begin block 0x2620x67
    prev=[0x25a0x67], succ=[0x664B0x2620x67]
    =================================
    0x2630x67: v67263(0x272) = CONST 
    0x2660x67: v67266(0x26d) = CONST 
    0x2690x67: v67269(0x664) = CONST 
    0x26c0x67: JUMP v67269(0x664)

    Begin block 0x664B0x2620x67
    prev=[0x2620x67], succ=[0x26d0x67]
    =================================
    0x665S0x2620x67: v665V26267(0x0) = CONST 
    0x668S0x2620x67: v668V26267(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620x67: v689V26267(0x1) = CONST 
    0x68bS0x2620x67: v68bV26267(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V26267(0x1), v668V26267(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620x67: v68fV26267 = SLOAD v68bV26267(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620x67: JUMP v67266(0x26d)

    Begin block 0x26d0x67
    prev=[0x664B0x2620x67], succ=[0x6950x67]
    =================================
    0x26e0x67: v6726e(0x695) = CONST 
    0x2710x67: JUMP v6726e(0x695)

    Begin block 0x6950x67
    prev=[0x26d0x67], succ=[0x6b20x67, 0x6b60x67]
    =================================
    0x6960x67: v67696 = CALLDATASIZE 
    0x6970x67: v67697(0x0) = CONST 
    0x69a0x67: CALLDATACOPY v67697(0x0), v67697(0x0), v67696
    0x69b0x67: v6769b(0x0) = CONST 
    0x69e0x67: v6769e = CALLDATASIZE 
    0x69f0x67: v6769f(0x0) = CONST 
    0x6a20x67: v676a2 = GAS 
    0x6a30x67: v676a3 = DELEGATECALL v676a2, v68fV26267, v6769f(0x0), v6769e, v6769b(0x0), v6769b(0x0)
    0x6a40x67: v676a4 = RETURNDATASIZE 
    0x6a50x67: v676a5(0x0) = CONST 
    0x6a80x67: RETURNDATACOPY v676a5(0x0), v676a5(0x0), v676a4
    0x6aa0x67: v676aa(0x0) = CONST 
    0x6ad0x67: v676ad = EQ v676a3, v676aa(0x0)
    0x6ae0x67: v676ae(0x6b6) = CONST 
    0x6b10x67: JUMPI v676ae(0x6b6), v676ad

    Begin block 0x6b20x67
    prev=[0x6950x67], succ=[]
    =================================
    0x6b20x67: v676b2 = RETURNDATASIZE 
    0x6b30x67: v676b3(0x0) = CONST 
    0x6b50x67: RETURN v676b3(0x0), v676b2

    Begin block 0x6b60x67
    prev=[0x6950x67], succ=[]
    =================================
    0x6b70x67: v676b7 = RETURNDATASIZE 
    0x6b80x67: v676b8(0x0) = CONST 
    0x6ba0x67: REVERT v676b8(0x0), v676b7

}

function 0x6ec(0x6ecarg0x0, 0x6ecarg0x1) private {
    Begin block 0x6ec
    prev=[], succ=[0x76c]
    =================================
    0x6ed: v6ed(0x6f5) = CONST 
    0x6f1: v6f1(0x76c) = CONST 
    0x6f4: JUMP v6f1(0x76c)

    Begin block 0x76c
    prev=[0x6ec], succ=[0x7fb]
    =================================
    0x76d: v76d(0x775) = CONST 
    0x771: v771(0x7fb) = CONST 
    0x774: JUMP v771(0x7fb)

    Begin block 0x7fb
    prev=[0x76c], succ=[0x775]
    =================================
    0x7fc: v7fc(0x0) = CONST 
    0x800: v800 = EXTCODESIZE v6ecarg0
    0x803: v803(0x0) = CONST 
    0x806: v806 = GT v800, v803(0x0)
    0x80d: JUMP v76d(0x775)

    Begin block 0x775
    prev=[0x7fb], succ=[0x77c, 0x7cc]
    =================================
    0x776: v776 = ISZERO v806
    0x777: v777 = ISZERO v776
    0x778: v778(0x7cc) = CONST 
    0x77b: JUMPI v778(0x7cc), v777

    Begin block 0x77c
    prev=[0x775], succ=[]
    =================================
    0x77c: v77c(0x40) = CONST 
    0x77e: v77e = MLOAD v77c(0x40)
    0x77f: v77f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x7a1: MSTORE v77e, v77f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7a2: v7a2(0x4) = CONST 
    0x7a4: v7a4 = ADD v7a2(0x4), v77e
    0x7a7: v7a7(0x20) = CONST 
    0x7a9: v7a9 = ADD v7a7(0x20), v7a4
    0x7ac: v7ac(0x20) = SUB v7a9, v7a4
    0x7ae: MSTORE v7a4, v7ac(0x20)
    0x7af: v7af(0x3b) = CONST 
    0x7b2: MSTORE v7a9, v7af(0x3b)
    0x7b3: v7b3(0x20) = CONST 
    0x7b5: v7b5 = ADD v7b3(0x20), v7a9
    0x7b7: v7b7(0x877) = CONST 
    0x7ba: v7ba(0x3b) = CONST 
    0x7bd: CODECOPY v7b5, v7b7(0x877), v7ba(0x3b)
    0x7be: v7be(0x40) = CONST 
    0x7c0: v7c0 = ADD v7be(0x40), v7b5
    0x7c4: v7c4(0x40) = CONST 
    0x7c6: v7c6 = MLOAD v7c4(0x40)
    0x7c9: v7c9(0x84) = SUB v7c0, v7c6
    0x7cb: REVERT v7c6, v7c9(0x84)

    Begin block 0x7cc
    prev=[0x775], succ=[0x6f5]
    =================================
    0x7cd: v7cd(0x0) = CONST 
    0x7cf: v7cf(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x7f0: v7f0(0x1) = CONST 
    0x7f2: v7f2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v7f0(0x1), v7cf(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x7f7: SSTORE v7f2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), v6ecarg0
    0x7fa: JUMP v6ed(0x6f5)

    Begin block 0x6f5
    prev=[0x7cc], succ=[]
    =================================
    0x6f7: v6f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x70c: v70c = AND v6f7(0xffffffffffffffffffffffffffffffffffffffff), v6ecarg0
    0x70d: v70d(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x72e: v72e(0x40) = CONST 
    0x730: v730 = MLOAD v72e(0x40)
    0x731: v731(0x40) = CONST 
    0x733: v733 = MLOAD v731(0x40)
    0x736: v736(0x0) = SUB v730, v733
    0x738: LOG2 v733, v736(0x0), v70d(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v70c
    0x73a: RETURNPRIVATE v6ecarg1

}

function upgradeTo(address)() public {
    Begin block 0x71
    prev=[], succ=[0x79, 0x7d]
    =================================
    0x72: v72 = CALLVALUE 
    0x74: v74 = ISZERO v72
    0x75: v75(0x7d) = CONST 
    0x78: JUMPI v75(0x7d), v74

    Begin block 0x79
    prev=[0x71], succ=[]
    =================================
    0x79: v79(0x0) = CONST 
    0x7c: REVERT v79(0x0), v79(0x0)

    Begin block 0x7d
    prev=[0x71], succ=[0x90, 0x94]
    =================================
    0x7f: v7f(0xc0) = CONST 
    0x82: v82(0x4) = CONST 
    0x85: v85 = CALLDATASIZE 
    0x86: v86 = SUB v85, v82(0x4)
    0x87: v87(0x20) = CONST 
    0x8a: v8a = LT v86, v87(0x20)
    0x8b: v8b = ISZERO v8a
    0x8c: v8c(0x94) = CONST 
    0x8f: JUMPI v8c(0x94), v8b

    Begin block 0x90
    prev=[0x7d], succ=[]
    =================================
    0x90: v90(0x0) = CONST 
    0x93: REVERT v90(0x0), v90(0x0)

    Begin block 0x94
    prev=[0x7d], succ=[0x274]
    =================================
    0x96: v96 = ADD v82(0x4), v86
    0x9a: v9a = CALLDATALOAD v82(0x4)
    0x9b: v9b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb0: vb0 = AND v9b(0xffffffffffffffffffffffffffffffffffffffff), v9a
    0xb2: vb2(0x20) = CONST 
    0xb4: vb4(0x24) = ADD vb2(0x20), v82(0x4)
    0xbc: vbc(0x274) = CONST 
    0xbf: JUMP vbc(0x274)

    Begin block 0x274
    prev=[0x94], succ=[0x6bbB0x274]
    =================================
    0x275: v275(0x27c) = CONST 
    0x278: v278(0x6bb) = CONST 
    0x27b: JUMP v278(0x6bb)

    Begin block 0x6bbB0x274
    prev=[0x274], succ=[0x27c]
    =================================
    0x6bcS0x274: v6bcV274(0x0) = CONST 
    0x6bfS0x274: v6bfV274(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x274: v6e0V274(0x1) = CONST 
    0x6e2S0x274: v6e2V274(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V274(0x1), v6bfV274(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x274: v6e6V274 = SLOAD v6e2V274(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x274: JUMP v275(0x27c)

    Begin block 0x27c
    prev=[0x6bbB0x274], succ=[0x2b0, 0x2bd]
    =================================
    0x27d: v27d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x292: v292 = AND v27d(0xffffffffffffffffffffffffffffffffffffffff), v6e6V274
    0x293: v293 = CALLER 
    0x294: v294(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a9: v2a9 = AND v294(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x2aa: v2aa = EQ v2a9, v292
    0x2ab: v2ab = ISZERO v2aa
    0x2ac: v2ac(0x2bd) = CONST 
    0x2af: JUMPI v2ac(0x2bd), v2ab

    Begin block 0x2b0
    prev=[0x27c], succ=[0x2b8]
    =================================
    0x2b0: v2b0(0x2b8) = CONST 
    0x2b4: v2b4(0x6ec) = CONST 
    0x2b7: CALLPRIVATE v2b4(0x6ec), vb0, v2b0(0x2b8)

    Begin block 0x2b8
    prev=[0x2b0], succ=[0x2c6]
    =================================
    0x2b9: v2b9(0x2c6) = CONST 
    0x2bc: JUMP v2b9(0x2c6)

    Begin block 0x2c6
    prev=[0x2b8], succ=[0xc0]
    =================================
    0x2c8: JUMP v7f(0xc0)

    Begin block 0xc0
    prev=[0x2c6], succ=[]
    =================================
    0xc1: STOP 

    Begin block 0x2bd
    prev=[0x27c], succ=[0x25a0x71]
    =================================
    0x2be: v2be(0x2c5) = CONST 
    0x2c1: v2c1(0x25a) = CONST 
    0x2c4: JUMP v2c1(0x25a)

    Begin block 0x25a0x71
    prev=[0x2bd], succ=[0x2620x71]
    =================================
    0x25b0x71: v7125b(0x262) = CONST 
    0x25e0x71: v7125e(0x5cc) = CONST 
    0x2610x71: CALLPRIVATE v7125e(0x5cc), v7125b(0x262)

    Begin block 0x2620x71
    prev=[0x25a0x71], succ=[0x664B0x2620x71]
    =================================
    0x2630x71: v71263(0x272) = CONST 
    0x2660x71: v71266(0x26d) = CONST 
    0x2690x71: v71269(0x664) = CONST 
    0x26c0x71: JUMP v71269(0x664)

    Begin block 0x664B0x2620x71
    prev=[0x2620x71], succ=[0x26d0x71]
    =================================
    0x665S0x2620x71: v665V26271(0x0) = CONST 
    0x668S0x2620x71: v668V26271(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620x71: v689V26271(0x1) = CONST 
    0x68bS0x2620x71: v68bV26271(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V26271(0x1), v668V26271(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620x71: v68fV26271 = SLOAD v68bV26271(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620x71: JUMP v71266(0x26d)

    Begin block 0x26d0x71
    prev=[0x664B0x2620x71], succ=[0x6950x71]
    =================================
    0x26e0x71: v7126e(0x695) = CONST 
    0x2710x71: JUMP v7126e(0x695)

    Begin block 0x6950x71
    prev=[0x26d0x71], succ=[0x6b20x71, 0x6b60x71]
    =================================
    0x6960x71: v71696 = CALLDATASIZE 
    0x6970x71: v71697(0x0) = CONST 
    0x69a0x71: CALLDATACOPY v71697(0x0), v71697(0x0), v71696
    0x69b0x71: v7169b(0x0) = CONST 
    0x69e0x71: v7169e = CALLDATASIZE 
    0x69f0x71: v7169f(0x0) = CONST 
    0x6a20x71: v716a2 = GAS 
    0x6a30x71: v716a3 = DELEGATECALL v716a2, v68fV26271, v7169f(0x0), v7169e, v7169b(0x0), v7169b(0x0)
    0x6a40x71: v716a4 = RETURNDATASIZE 
    0x6a50x71: v716a5(0x0) = CONST 
    0x6a80x71: RETURNDATACOPY v716a5(0x0), v716a5(0x0), v716a4
    0x6aa0x71: v716aa(0x0) = CONST 
    0x6ad0x71: v716ad = EQ v716a3, v716aa(0x0)
    0x6ae0x71: v716ae(0x6b6) = CONST 
    0x6b10x71: JUMPI v716ae(0x6b6), v716ad

    Begin block 0x6b20x71
    prev=[0x6950x71], succ=[]
    =================================
    0x6b20x71: v716b2 = RETURNDATASIZE 
    0x6b30x71: v716b3(0x0) = CONST 
    0x6b50x71: RETURN v716b3(0x0), v716b2

    Begin block 0x6b60x71
    prev=[0x6950x71], succ=[]
    =================================
    0x6b70x71: v716b7 = RETURNDATASIZE 
    0x6b80x71: v716b8(0x0) = CONST 
    0x6ba0x71: REVERT v716b8(0x0), v716b7

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xc2
    prev=[], succ=[0xd4, 0xd8]
    =================================
    0xc3: vc3(0x159) = CONST 
    0xc6: vc6(0x4) = CONST 
    0xc9: vc9 = CALLDATASIZE 
    0xca: vca = SUB vc9, vc6(0x4)
    0xcb: vcb(0x40) = CONST 
    0xce: vce = LT vca, vcb(0x40)
    0xcf: vcf = ISZERO vce
    0xd0: vd0(0xd8) = CONST 
    0xd3: JUMPI vd0(0xd8), vcf

    Begin block 0xd4
    prev=[0xc2], succ=[]
    =================================
    0xd4: vd4(0x0) = CONST 
    0xd7: REVERT vd4(0x0), vd4(0x0)

    Begin block 0xd8
    prev=[0xc2], succ=[0x111, 0x115]
    =================================
    0xda: vda = ADD vc6(0x4), vca
    0xde: vde = CALLDATALOAD vc6(0x4)
    0xdf: vdf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf4: vf4 = AND vdf(0xffffffffffffffffffffffffffffffffffffffff), vde
    0xf6: vf6(0x20) = CONST 
    0xf8: vf8(0x24) = ADD vf6(0x20), vc6(0x4)
    0xfe: vfe = CALLDATALOAD vf8(0x24)
    0x100: v100(0x20) = CONST 
    0x102: v102(0x44) = ADD v100(0x20), vf8(0x24)
    0x104: v104(0x100000000) = CONST 
    0x10b: v10b = GT vfe, v104(0x100000000)
    0x10c: v10c = ISZERO v10b
    0x10d: v10d(0x115) = CONST 
    0x110: JUMPI v10d(0x115), v10c

    Begin block 0x111
    prev=[0xd8], succ=[]
    =================================
    0x111: v111(0x0) = CONST 
    0x114: REVERT v111(0x0), v111(0x0)

    Begin block 0x115
    prev=[0xd8], succ=[0x123, 0x127]
    =================================
    0x117: v117 = ADD vc6(0x4), vfe
    0x119: v119(0x20) = CONST 
    0x11c: v11c = ADD v117, v119(0x20)
    0x11d: v11d = GT v11c, vda
    0x11e: v11e = ISZERO v11d
    0x11f: v11f(0x127) = CONST 
    0x122: JUMPI v11f(0x127), v11e

    Begin block 0x123
    prev=[0x115], succ=[]
    =================================
    0x123: v123(0x0) = CONST 
    0x126: REVERT v123(0x0), v123(0x0)

    Begin block 0x127
    prev=[0x115], succ=[0x145, 0x149]
    =================================
    0x129: v129 = CALLDATALOAD v117
    0x12b: v12b(0x20) = CONST 
    0x12d: v12d = ADD v12b(0x20), v117
    0x130: v130(0x1) = CONST 
    0x133: v133 = MUL v129, v130(0x1)
    0x135: v135 = ADD v12d, v133
    0x136: v136 = GT v135, vda
    0x137: v137(0x100000000) = CONST 
    0x13e: v13e = GT v129, v137(0x100000000)
    0x13f: v13f = OR v13e, v136
    0x140: v140 = ISZERO v13f
    0x141: v141(0x149) = CONST 
    0x144: JUMPI v141(0x149), v140

    Begin block 0x145
    prev=[0x127], succ=[]
    =================================
    0x145: v145(0x0) = CONST 
    0x148: REVERT v145(0x0), v145(0x0)

    Begin block 0x149
    prev=[0x127], succ=[0x2c9]
    =================================
    0x155: v155(0x2c9) = CONST 
    0x158: JUMP v155(0x2c9)

    Begin block 0x2c9
    prev=[0x149], succ=[0x6bbB0x2c9]
    =================================
    0x2ca: v2ca(0x2d1) = CONST 
    0x2cd: v2cd(0x6bb) = CONST 
    0x2d0: JUMP v2cd(0x6bb)

    Begin block 0x6bbB0x2c9
    prev=[0x2c9], succ=[0x2d1]
    =================================
    0x6bcS0x2c9: v6bcV2c9(0x0) = CONST 
    0x6bfS0x2c9: v6bfV2c9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e0S0x2c9: v6e0V2c9(0x1) = CONST 
    0x6e2S0x2c9: v6e2V2c9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = MUL v6e0V2c9(0x1), v6bfV2c9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e6S0x2c9: v6e6V2c9 = SLOAD v6e2V2c9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6ebS0x2c9: JUMP v2ca(0x2d1)

    Begin block 0x2d1
    prev=[0x6bbB0x2c9], succ=[0x305, 0x393]
    =================================
    0x2d2: v2d2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e7: v2e7 = AND v2d2(0xffffffffffffffffffffffffffffffffffffffff), v6e6V2c9
    0x2e8: v2e8 = CALLER 
    0x2e9: v2e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fe: v2fe = AND v2e9(0xffffffffffffffffffffffffffffffffffffffff), v2e8
    0x2ff: v2ff = EQ v2fe, v2e7
    0x300: v300 = ISZERO v2ff
    0x301: v301(0x393) = CONST 
    0x304: JUMPI v301(0x393), v300

    Begin block 0x305
    prev=[0x2d1], succ=[0x30d]
    =================================
    0x305: v305(0x30d) = CONST 
    0x309: v309(0x6ec) = CONST 
    0x30c: CALLPRIVATE v309(0x6ec), vf4, v305(0x30d)

    Begin block 0x30d
    prev=[0x305], succ=[0x357, 0x378]
    =================================
    0x30e: v30e(0x0) = CONST 
    0x311: v311(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x326: v326 = AND v311(0xffffffffffffffffffffffffffffffffffffffff), vf4
    0x329: v329(0x40) = CONST 
    0x32b: v32b = MLOAD v329(0x40)
    0x332: CALLDATACOPY v32b, v12d, v129
    0x335: v335 = ADD v32b, v129
    0x33e: v33e(0x0) = CONST 
    0x340: v340(0x40) = CONST 
    0x342: v342 = MLOAD v340(0x40)
    0x345: v345 = SUB v335, v342
    0x348: v348 = GAS 
    0x349: v349 = DELEGATECALL v348, v326, v342, v345, v342, v33e(0x0)
    0x34d: v34d = RETURNDATASIZE 
    0x34f: v34f(0x0) = CONST 
    0x352: v352 = EQ v34d, v34f(0x0)
    0x353: v353(0x378) = CONST 
    0x356: JUMPI v353(0x378), v352

    Begin block 0x357
    prev=[0x30d], succ=[0x37d]
    =================================
    0x357: v357(0x40) = CONST 
    0x359: v359 = MLOAD v357(0x40)
    0x35c: v35c(0x1f) = CONST 
    0x35e: v35e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v35c(0x1f)
    0x35f: v35f(0x3f) = CONST 
    0x361: v361 = RETURNDATASIZE 
    0x362: v362 = ADD v361, v35f(0x3f)
    0x363: v363 = AND v362, v35e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x365: v365 = ADD v359, v363
    0x366: v366(0x40) = CONST 
    0x368: MSTORE v366(0x40), v365
    0x369: v369 = RETURNDATASIZE 
    0x36b: MSTORE v359, v369
    0x36c: v36c = RETURNDATASIZE 
    0x36d: v36d(0x0) = CONST 
    0x36f: v36f(0x20) = CONST 
    0x372: v372 = ADD v359, v36f(0x20)
    0x373: RETURNDATACOPY v372, v36d(0x0), v36c
    0x374: v374(0x37d) = CONST 
    0x377: JUMP v374(0x37d)

    Begin block 0x37d
    prev=[0x357, 0x378], succ=[0x389, 0x38d]
    =================================
    0x383: v383 = ISZERO v349
    0x384: v384 = ISZERO v383
    0x385: v385(0x38d) = CONST 
    0x388: JUMPI v385(0x38d), v384

    Begin block 0x389
    prev=[0x37d], succ=[]
    =================================
    0x389: v389(0x0) = CONST 
    0x38c: REVERT v389(0x0), v389(0x0)

    Begin block 0x38d
    prev=[0x37d], succ=[0x39c]
    =================================
    0x38f: v38f(0x39c) = CONST 
    0x392: JUMP v38f(0x39c)

    Begin block 0x39c
    prev=[0x38d], succ=[0x159]
    =================================
    0x3a0: JUMP vc3(0x159)

    Begin block 0x159
    prev=[0x39c], succ=[]
    =================================
    0x15a: STOP 

    Begin block 0x378
    prev=[0x30d], succ=[0x37d]
    =================================
    0x379: v379(0x60) = CONST 

    Begin block 0x393
    prev=[0x2d1], succ=[0x25a0xc2]
    =================================
    0x394: v394(0x39b) = CONST 
    0x397: v397(0x25a) = CONST 
    0x39a: JUMP v397(0x25a)

    Begin block 0x25a0xc2
    prev=[0x393], succ=[0x2620xc2]
    =================================
    0x25b0xc2: vc225b(0x262) = CONST 
    0x25e0xc2: vc225e(0x5cc) = CONST 
    0x2610xc2: CALLPRIVATE vc225e(0x5cc), vc225b(0x262)

    Begin block 0x2620xc2
    prev=[0x25a0xc2], succ=[0x664B0x2620xc2]
    =================================
    0x2630xc2: vc2263(0x272) = CONST 
    0x2660xc2: vc2266(0x26d) = CONST 
    0x2690xc2: vc2269(0x664) = CONST 
    0x26c0xc2: JUMP vc2269(0x664)

    Begin block 0x664B0x2620xc2
    prev=[0x2620xc2], succ=[0x26d0xc2]
    =================================
    0x665S0x2620xc2: v665V262c2(0x0) = CONST 
    0x668S0x2620xc2: v668V262c2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x689S0x2620xc2: v689V262c2(0x1) = CONST 
    0x68bS0x2620xc2: v68bV262c2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = MUL v689V262c2(0x1), v668V262c2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x68fS0x2620xc2: v68fV262c2 = SLOAD v68bV262c2(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x694S0x2620xc2: JUMP vc2266(0x26d)

    Begin block 0x26d0xc2
    prev=[0x664B0x2620xc2], succ=[0x6950xc2]
    =================================
    0x26e0xc2: vc226e(0x695) = CONST 
    0x2710xc2: JUMP vc226e(0x695)

    Begin block 0x6950xc2
    prev=[0x26d0xc2], succ=[0x6b20xc2, 0x6b60xc2]
    =================================
    0x6960xc2: vc2696 = CALLDATASIZE 
    0x6970xc2: vc2697(0x0) = CONST 
    0x69a0xc2: CALLDATACOPY vc2697(0x0), vc2697(0x0), vc2696
    0x69b0xc2: vc269b(0x0) = CONST 
    0x69e0xc2: vc269e = CALLDATASIZE 
    0x69f0xc2: vc269f(0x0) = CONST 
    0x6a20xc2: vc26a2 = GAS 
    0x6a30xc2: vc26a3 = DELEGATECALL vc26a2, v68fV262c2, vc269f(0x0), vc269e, vc269b(0x0), vc269b(0x0)
    0x6a40xc2: vc26a4 = RETURNDATASIZE 
    0x6a50xc2: vc26a5(0x0) = CONST 
    0x6a80xc2: RETURNDATACOPY vc26a5(0x0), vc26a5(0x0), vc26a4
    0x6aa0xc2: vc26aa(0x0) = CONST 
    0x6ad0xc2: vc26ad = EQ vc26a3, vc26aa(0x0)
    0x6ae0xc2: vc26ae(0x6b6) = CONST 
    0x6b10xc2: JUMPI vc26ae(0x6b6), vc26ad

    Begin block 0x6b20xc2
    prev=[0x6950xc2], succ=[]
    =================================
    0x6b20xc2: vc26b2 = RETURNDATASIZE 
    0x6b30xc2: vc26b3(0x0) = CONST 
    0x6b50xc2: RETURN vc26b3(0x0), vc26b2

    Begin block 0x6b60xc2
    prev=[0x6950xc2], succ=[]
    =================================
    0x6b70xc2: vc26b7 = RETURNDATASIZE 
    0x6b80xc2: vc26b8(0x0) = CONST 
    0x6ba0xc2: REVERT vc26b8(0x0), vc26b7

}

