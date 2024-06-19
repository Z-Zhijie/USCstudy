function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xb4e]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xb3c: vb3c(0xb4e) = CONST 
    0xb3d: JUMPI vb3c(0xb4e), v8

    Begin block 0xd
    prev=[0x0], succ=[0xb51, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x68690113) = CONST 
    0x3c: v3c = EQ v37(0x68690113), v35
    0xb3e: vb3e(0xb51) = CONST 
    0xb3f: JUMPI vb3e(0xb51), v3c

    Begin block 0xb51
    prev=[0xd], succ=[]
    =================================
    0xb52: vb52(0x1e9) = CONST 
    0xb53: CALLPRIVATE vb52(0x1e9)

    Begin block 0x41
    prev=[0xd], succ=[0xb54, 0x4c]
    =================================
    0x42: v42(0x7babfffc) = CONST 
    0x47: v47 = EQ v42(0x7babfffc), v35
    0xb40: vb40(0xb54) = CONST 
    0xb41: JUMPI vb40(0xb54), v47

    Begin block 0xb54
    prev=[0x41], succ=[]
    =================================
    0xb55: vb55(0x240) = CONST 
    0xb56: CALLPRIVATE vb55(0x240)

    Begin block 0x4c
    prev=[0x41], succ=[0xb57, 0x57]
    =================================
    0x4d: v4d(0x8da5cb5b) = CONST 
    0x52: v52 = EQ v4d(0x8da5cb5b), v35
    0xb42: vb42(0xb57) = CONST 
    0xb43: JUMPI vb42(0xb57), v52

    Begin block 0xb57
    prev=[0x4c], succ=[]
    =================================
    0xb58: vb58(0x283) = CONST 
    0xb59: CALLPRIVATE vb58(0x283)

    Begin block 0x57
    prev=[0x4c], succ=[0xb5a, 0x62]
    =================================
    0x58: v58(0x994ebc43) = CONST 
    0x5d: v5d = EQ v58(0x994ebc43), v35
    0xb44: vb44(0xb5a) = CONST 
    0xb45: JUMPI vb44(0xb5a), v5d

    Begin block 0xb5a
    prev=[0x57], succ=[]
    =================================
    0xb5b: vb5b(0x2da) = CONST 
    0xb5c: CALLPRIVATE vb5b(0x2da)

    Begin block 0x62
    prev=[0x57], succ=[0xb5d, 0x6d]
    =================================
    0x63: v63(0xab63424e) = CONST 
    0x68: v68 = EQ v63(0xab63424e), v35
    0xb46: vb46(0xb5d) = CONST 
    0xb47: JUMPI vb46(0xb5d), v68

    Begin block 0xb5d
    prev=[0x62], succ=[]
    =================================
    0xb5e: vb5e(0x331) = CONST 
    0xb5f: CALLPRIVATE vb5e(0x331)

    Begin block 0x6d
    prev=[0x62], succ=[0xb60, 0x78]
    =================================
    0x6e: v6e(0xcd6dc687) = CONST 
    0x73: v73 = EQ v6e(0xcd6dc687), v35
    0xb48: vb48(0xb60) = CONST 
    0xb49: JUMPI vb48(0xb60), v73

    Begin block 0xb60
    prev=[0x6d], succ=[]
    =================================
    0xb61: vb61(0x388) = CONST 
    0xb62: CALLPRIVATE vb61(0x388)

    Begin block 0x78
    prev=[0x6d], succ=[0xb63, 0x83]
    =================================
    0x79: v79(0xdf5cf723) = CONST 
    0x7e: v7e = EQ v79(0xdf5cf723), v35
    0xb4a: vb4a(0xb63) = CONST 
    0xb4b: JUMPI vb4a(0xb63), v7e

    Begin block 0xb63
    prev=[0x78], succ=[]
    =================================
    0xb64: vb64(0x3d5) = CONST 
    0xb65: CALLPRIVATE vb64(0x3d5)

    Begin block 0x83
    prev=[0x78], succ=[0xb4e, 0xb66]
    =================================
    0x84: v84(0xf2fde38b) = CONST 
    0x89: v89 = EQ v84(0xf2fde38b), v35
    0xb4c: vb4c(0xb66) = CONST 
    0xb4d: JUMPI vb4c(0xb66), v89

    Begin block 0xb4e
    prev=[0x0, 0x83], succ=[]
    =================================
    0xb4f: vb4f(0x8e) = CONST 
    0xb50: CALLPRIVATE vb4f(0x8e)

    Begin block 0xb66
    prev=[0x83], succ=[]
    =================================
    0xb67: vb67(0x42c) = CONST 
    0xb68: CALLPRIVATE vb67(0x42c)

}

function empty3()() public {
    Begin block 0x1e9
    prev=[], succ=[0x1f1, 0x1f5]
    =================================
    0x1ea: v1ea = CALLVALUE 
    0x1ec: v1ec = ISZERO v1ea
    0x1ed: v1ed(0x1f5) = CONST 
    0x1f0: JUMPI v1ed(0x1f5), v1ec

    Begin block 0x1f1
    prev=[0x1e9], succ=[]
    =================================
    0x1f1: v1f1(0x0) = CONST 
    0x1f4: REVERT v1f1(0x0), v1f1(0x0)

    Begin block 0x1f5
    prev=[0x1e9], succ=[0x499]
    =================================
    0x1f7: v1f7(0x1fe) = CONST 
    0x1fa: v1fa(0x499) = CONST 
    0x1fd: JUMP v1fa(0x499)

    Begin block 0x499
    prev=[0x1f5], succ=[0x1fe]
    =================================
    0x49a: v49a(0x2) = CONST 
    0x49c: v49c(0x0) = CONST 
    0x49f: v49f = SLOAD v49a(0x2)
    0x4a1: v4a1(0x100) = CONST 
    0x4a4: v4a4(0x1) = EXP v4a1(0x100), v49c(0x0)
    0x4a6: v4a6 = DIV v49f, v4a4(0x1)
    0x4a7: v4a7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4bc: v4bc = AND v4a7(0xffffffffffffffffffffffffffffffffffffffff), v4a6
    0x4be: JUMP v1f7(0x1fe)

    Begin block 0x1fe
    prev=[0x499], succ=[]
    =================================
    0x1ff: v1ff(0x40) = CONST 
    0x201: v201 = MLOAD v1ff(0x40)
    0x204: v204(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x219: v219 = AND v204(0xffffffffffffffffffffffffffffffffffffffff), v4bc
    0x21a: v21a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22f: v22f = AND v21a(0xffffffffffffffffffffffffffffffffffffffff), v219
    0x231: MSTORE v201, v22f
    0x232: v232(0x20) = CONST 
    0x234: v234 = ADD v232(0x20), v201
    0x238: v238(0x40) = CONST 
    0x23a: v23a = MLOAD v238(0x40)
    0x23d: v23d(0x20) = SUB v234, v23a
    0x23f: RETURN v23a, v23d(0x20)

}

function transferDelegation(address)() public {
    Begin block 0x240
    prev=[], succ=[0x248, 0x24c]
    =================================
    0x241: v241 = CALLVALUE 
    0x243: v243 = ISZERO v241
    0x244: v244(0x24c) = CONST 
    0x247: JUMPI v244(0x24c), v243

    Begin block 0x248
    prev=[0x240], succ=[]
    =================================
    0x248: v248(0x0) = CONST 
    0x24b: REVERT v248(0x0), v248(0x0)

    Begin block 0x24c
    prev=[0x240], succ=[0x4bf]
    =================================
    0x24e: v24e(0x281) = CONST 
    0x251: v251(0x4) = CONST 
    0x254: v254 = CALLDATASIZE 
    0x255: v255 = SUB v254, v251(0x4)
    0x257: v257 = ADD v251(0x4), v255
    0x25b: v25b = CALLDATALOAD v251(0x4)
    0x25c: v25c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x271: v271 = AND v25c(0xffffffffffffffffffffffffffffffffffffffff), v25b
    0x273: v273(0x20) = CONST 
    0x275: v275(0x24) = ADD v273(0x20), v251(0x4)
    0x27d: v27d(0x4bf) = CONST 
    0x280: JUMP v27d(0x4bf)

    Begin block 0x4bf
    prev=[0x24c], succ=[0x517, 0x584]
    =================================
    0x4c0: v4c0(0x3) = CONST 
    0x4c2: v4c2(0x0) = CONST 
    0x4c5: v4c5 = SLOAD v4c0(0x3)
    0x4c7: v4c7(0x100) = CONST 
    0x4ca: v4ca(0x1) = EXP v4c7(0x100), v4c2(0x0)
    0x4cc: v4cc = DIV v4c5, v4ca(0x1)
    0x4cd: v4cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4e2: v4e2 = AND v4cd(0xffffffffffffffffffffffffffffffffffffffff), v4cc
    0x4e3: v4e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4f8: v4f8 = AND v4e3(0xffffffffffffffffffffffffffffffffffffffff), v4e2
    0x4f9: v4f9 = CALLER 
    0x4fa: v4fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x50f: v50f = AND v4fa(0xffffffffffffffffffffffffffffffffffffffff), v4f9
    0x510: v510 = EQ v50f, v4f8
    0x511: v511 = ISZERO v510
    0x512: v512 = ISZERO v511
    0x513: v513(0x584) = CONST 
    0x516: JUMPI v513(0x584), v512

    Begin block 0x517
    prev=[0x4bf], succ=[]
    =================================
    0x517: v517(0x40) = CONST 
    0x519: v519 = MLOAD v517(0x40)
    0x51a: v51a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x53c: MSTORE v519, v51a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x53d: v53d(0x4) = CONST 
    0x53f: v53f = ADD v53d(0x4), v519
    0x542: v542(0x20) = CONST 
    0x544: v544 = ADD v542(0x20), v53f
    0x547: v547(0x20) = SUB v544, v53f
    0x549: MSTORE v53f, v547(0x20)
    0x54a: v54a(0x17) = CONST 
    0x54d: MSTORE v544, v54a(0x17)
    0x54e: v54e(0x20) = CONST 
    0x550: v550 = ADD v54e(0x20), v544
    0x552: v552(0x53656e646572206973206e6f7420746865206f776e6572000000000000000000) = CONST 
    0x574: MSTORE v550, v552(0x53656e646572206973206e6f7420746865206f776e6572000000000000000000)
    0x576: v576(0x20) = CONST 
    0x578: v578 = ADD v576(0x20), v550
    0x57c: v57c(0x40) = CONST 
    0x57e: v57e = MLOAD v57c(0x40)
    0x581: v581(0x64) = SUB v578, v57e
    0x583: REVERT v57e, v581(0x64)

    Begin block 0x584
    prev=[0x4bf], succ=[0x5bc, 0x629]
    =================================
    0x585: v585(0x0) = CONST 
    0x587: v587(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x59c: v59c(0x0) = AND v587(0xffffffffffffffffffffffffffffffffffffffff), v585(0x0)
    0x59e: v59e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b3: v5b3 = AND v59e(0xffffffffffffffffffffffffffffffffffffffff), v271
    0x5b4: v5b4 = EQ v5b3, v59c(0x0)
    0x5b5: v5b5 = ISZERO v5b4
    0x5b6: v5b6 = ISZERO v5b5
    0x5b7: v5b7 = ISZERO v5b6
    0x5b8: v5b8(0x629) = CONST 
    0x5bb: JUMPI v5b8(0x629), v5b7

    Begin block 0x5bc
    prev=[0x584], succ=[]
    =================================
    0x5bc: v5bc(0x40) = CONST 
    0x5be: v5be = MLOAD v5bc(0x40)
    0x5bf: v5bf(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x5e1: MSTORE v5be, v5bf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5e2: v5e2(0x4) = CONST 
    0x5e4: v5e4 = ADD v5e2(0x4), v5be
    0x5e7: v5e7(0x20) = CONST 
    0x5e9: v5e9 = ADD v5e7(0x20), v5e4
    0x5ec: v5ec(0x20) = SUB v5e9, v5e4
    0x5ee: MSTORE v5e4, v5ec(0x20)
    0x5ef: v5ef(0x1f) = CONST 
    0x5f2: MSTORE v5e9, v5ef(0x1f)
    0x5f3: v5f3(0x20) = CONST 
    0x5f5: v5f5 = ADD v5f3(0x20), v5e9
    0x5f7: v5f7(0x547279696e6720746f207472616e7366657220746f2061646472657373203000) = CONST 
    0x619: MSTORE v5f5, v5f7(0x547279696e6720746f207472616e7366657220746f2061646472657373203000)
    0x61b: v61b(0x20) = CONST 
    0x61d: v61d = ADD v61b(0x20), v5f5
    0x621: v621(0x40) = CONST 
    0x623: v623 = MLOAD v621(0x40)
    0x626: v626(0x64) = SUB v61d, v623
    0x628: REVERT v623, v626(0x64)

    Begin block 0x629
    prev=[0x584], succ=[0x281]
    =================================
    0x62b: v62b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x640: v640 = AND v62b(0xffffffffffffffffffffffffffffffffffffffff), v271
    0x641: v641(0x4) = CONST 
    0x643: v643(0x0) = CONST 
    0x646: v646 = SLOAD v641(0x4)
    0x648: v648(0x100) = CONST 
    0x64b: v64b(0x1) = EXP v648(0x100), v643(0x0)
    0x64d: v64d = DIV v646, v64b(0x1)
    0x64e: v64e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x663: v663 = AND v64e(0xffffffffffffffffffffffffffffffffffffffff), v64d
    0x664: v664(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x679: v679 = AND v664(0xffffffffffffffffffffffffffffffffffffffff), v663
    0x67a: v67a(0xd0f8e6a439689cb66a57cb879faad9da11c6b662caf1ec096fef086d15ea16c7) = CONST 
    0x69b: v69b(0x40) = CONST 
    0x69d: v69d = MLOAD v69b(0x40)
    0x69e: v69e(0x40) = CONST 
    0x6a0: v6a0 = MLOAD v69e(0x40)
    0x6a3: v6a3(0x0) = SUB v69d, v6a0
    0x6a5: LOG3 v6a0, v6a3(0x0), v67a(0xd0f8e6a439689cb66a57cb879faad9da11c6b662caf1ec096fef086d15ea16c7), v679, v640
    0x6a7: v6a7(0x4) = CONST 
    0x6a9: v6a9(0x0) = CONST 
    0x6ab: v6ab(0x100) = CONST 
    0x6ae: v6ae(0x1) = EXP v6ab(0x100), v6a9(0x0)
    0x6b0: v6b0 = SLOAD v6a7(0x4)
    0x6b2: v6b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6c7: v6c7(0xffffffffffffffffffffffffffffffffffffffff) = MUL v6b2(0xffffffffffffffffffffffffffffffffffffffff), v6ae(0x1)
    0x6c8: v6c8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c9: v6c9 = AND v6c8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6b0
    0x6cc: v6cc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6e1: v6e1 = AND v6cc(0xffffffffffffffffffffffffffffffffffffffff), v271
    0x6e2: v6e2 = MUL v6e1, v6ae(0x1)
    0x6e3: v6e3 = OR v6e2, v6c9
    0x6e5: SSTORE v6a7(0x4), v6e3
    0x6e8: JUMP v24e(0x281)

    Begin block 0x281
    prev=[0x629], succ=[]
    =================================
    0x282: STOP 

}

function owner()() public {
    Begin block 0x283
    prev=[], succ=[0x28b, 0x28f]
    =================================
    0x284: v284 = CALLVALUE 
    0x286: v286 = ISZERO v284
    0x287: v287(0x28f) = CONST 
    0x28a: JUMPI v287(0x28f), v286

    Begin block 0x28b
    prev=[0x283], succ=[]
    =================================
    0x28b: v28b(0x0) = CONST 
    0x28e: REVERT v28b(0x0), v28b(0x0)

    Begin block 0x28f
    prev=[0x283], succ=[0x6e9]
    =================================
    0x291: v291(0x298) = CONST 
    0x294: v294(0x6e9) = CONST 
    0x297: JUMP v294(0x6e9)

    Begin block 0x6e9
    prev=[0x28f], succ=[0x298]
    =================================
    0x6ea: v6ea(0x3) = CONST 
    0x6ec: v6ec(0x0) = CONST 
    0x6ef: v6ef = SLOAD v6ea(0x3)
    0x6f1: v6f1(0x100) = CONST 
    0x6f4: v6f4(0x1) = EXP v6f1(0x100), v6ec(0x0)
    0x6f6: v6f6 = DIV v6ef, v6f4(0x1)
    0x6f7: v6f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x70c: v70c = AND v6f7(0xffffffffffffffffffffffffffffffffffffffff), v6f6
    0x70e: JUMP v291(0x298)

    Begin block 0x298
    prev=[0x6e9], succ=[]
    =================================
    0x299: v299(0x40) = CONST 
    0x29b: v29b = MLOAD v299(0x40)
    0x29e: v29e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b3: v2b3 = AND v29e(0xffffffffffffffffffffffffffffffffffffffff), v70c
    0x2b4: v2b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c9: v2c9 = AND v2b4(0xffffffffffffffffffffffffffffffffffffffff), v2b3
    0x2cb: MSTORE v29b, v2c9
    0x2cc: v2cc(0x20) = CONST 
    0x2ce: v2ce = ADD v2cc(0x20), v29b
    0x2d2: v2d2(0x40) = CONST 
    0x2d4: v2d4 = MLOAD v2d2(0x40)
    0x2d7: v2d7(0x20) = SUB v2ce, v2d4
    0x2d9: RETURN v2d4, v2d7(0x20)

}

function empty1()() public {
    Begin block 0x2da
    prev=[], succ=[0x2e2, 0x2e6]
    =================================
    0x2db: v2db = CALLVALUE 
    0x2dd: v2dd = ISZERO v2db
    0x2de: v2de(0x2e6) = CONST 
    0x2e1: JUMPI v2de(0x2e6), v2dd

    Begin block 0x2e2
    prev=[0x2da], succ=[]
    =================================
    0x2e2: v2e2(0x0) = CONST 
    0x2e5: REVERT v2e2(0x0), v2e2(0x0)

    Begin block 0x2e6
    prev=[0x2da], succ=[0x70f]
    =================================
    0x2e8: v2e8(0x2ef) = CONST 
    0x2eb: v2eb(0x70f) = CONST 
    0x2ee: JUMP v2eb(0x70f)

    Begin block 0x70f
    prev=[0x2e6], succ=[0x2ef]
    =================================
    0x710: v710(0x0) = CONST 
    0x714: v714 = SLOAD v710(0x0)
    0x716: v716(0x100) = CONST 
    0x719: v719(0x1) = EXP v716(0x100), v710(0x0)
    0x71b: v71b = DIV v714, v719(0x1)
    0x71c: v71c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x731: v731 = AND v71c(0xffffffffffffffffffffffffffffffffffffffff), v71b
    0x733: JUMP v2e8(0x2ef)

    Begin block 0x2ef
    prev=[0x70f], succ=[]
    =================================
    0x2f0: v2f0(0x40) = CONST 
    0x2f2: v2f2 = MLOAD v2f0(0x40)
    0x2f5: v2f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x30a: v30a = AND v2f5(0xffffffffffffffffffffffffffffffffffffffff), v731
    0x30b: v30b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x320: v320 = AND v30b(0xffffffffffffffffffffffffffffffffffffffff), v30a
    0x322: MSTORE v2f2, v320
    0x323: v323(0x20) = CONST 
    0x325: v325 = ADD v323(0x20), v2f2
    0x329: v329(0x40) = CONST 
    0x32b: v32b = MLOAD v329(0x40)
    0x32e: v32e(0x20) = SUB v325, v32b
    0x330: RETURN v32b, v32e(0x20)

}

function empty2()() public {
    Begin block 0x331
    prev=[], succ=[0x339, 0x33d]
    =================================
    0x332: v332 = CALLVALUE 
    0x334: v334 = ISZERO v332
    0x335: v335(0x33d) = CONST 
    0x338: JUMPI v335(0x33d), v334

    Begin block 0x339
    prev=[0x331], succ=[]
    =================================
    0x339: v339(0x0) = CONST 
    0x33c: REVERT v339(0x0), v339(0x0)

    Begin block 0x33d
    prev=[0x331], succ=[0x734]
    =================================
    0x33f: v33f(0x346) = CONST 
    0x342: v342(0x734) = CONST 
    0x345: JUMP v342(0x734)

    Begin block 0x734
    prev=[0x33d], succ=[0x346]
    =================================
    0x735: v735(0x1) = CONST 
    0x737: v737(0x0) = CONST 
    0x73a: v73a = SLOAD v735(0x1)
    0x73c: v73c(0x100) = CONST 
    0x73f: v73f(0x1) = EXP v73c(0x100), v737(0x0)
    0x741: v741 = DIV v73a, v73f(0x1)
    0x742: v742(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x757: v757 = AND v742(0xffffffffffffffffffffffffffffffffffffffff), v741
    0x759: JUMP v33f(0x346)

    Begin block 0x346
    prev=[0x734], succ=[]
    =================================
    0x347: v347(0x40) = CONST 
    0x349: v349 = MLOAD v347(0x40)
    0x34c: v34c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x361: v361 = AND v34c(0xffffffffffffffffffffffffffffffffffffffff), v757
    0x362: v362(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x377: v377 = AND v362(0xffffffffffffffffffffffffffffffffffffffff), v361
    0x379: MSTORE v349, v377
    0x37a: v37a(0x20) = CONST 
    0x37c: v37c = ADD v37a(0x20), v349
    0x380: v380(0x40) = CONST 
    0x382: v382 = MLOAD v380(0x40)
    0x385: v385(0x20) = SUB v37c, v382
    0x387: RETURN v382, v385(0x20)

}

function initialize(address,uint256)() public {
    Begin block 0x388
    prev=[], succ=[0x390, 0x394]
    =================================
    0x389: v389 = CALLVALUE 
    0x38b: v38b = ISZERO v389
    0x38c: v38c(0x394) = CONST 
    0x38f: JUMPI v38c(0x394), v38b

    Begin block 0x390
    prev=[0x388], succ=[]
    =================================
    0x390: v390(0x0) = CONST 
    0x393: REVERT v390(0x0), v390(0x0)

    Begin block 0x394
    prev=[0x388], succ=[0x75a]
    =================================
    0x396: v396(0x3d3) = CONST 
    0x399: v399(0x4) = CONST 
    0x39c: v39c = CALLDATASIZE 
    0x39d: v39d = SUB v39c, v399(0x4)
    0x39f: v39f = ADD v399(0x4), v39d
    0x3a3: v3a3 = CALLDATALOAD v399(0x4)
    0x3a4: v3a4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b9: v3b9 = AND v3a4(0xffffffffffffffffffffffffffffffffffffffff), v3a3
    0x3bb: v3bb(0x20) = CONST 
    0x3bd: v3bd(0x24) = ADD v3bb(0x20), v399(0x4)
    0x3c3: v3c3 = CALLDATALOAD v3bd(0x24)
    0x3c5: v3c5(0x20) = CONST 
    0x3c7: v3c7(0x44) = ADD v3c5(0x20), v3bd(0x24)
    0x3cf: v3cf(0x75a) = CONST 
    0x3d2: JUMP v3cf(0x75a)

    Begin block 0x75a
    prev=[0x394], succ=[0x79d, 0x80a]
    =================================
    0x75b: v75b(0x0) = CONST 
    0x75d: v75d(0x3) = CONST 
    0x75f: v75f(0x0) = CONST 
    0x762: v762 = SLOAD v75d(0x3)
    0x764: v764(0x100) = CONST 
    0x767: v767(0x1) = EXP v764(0x100), v75f(0x0)
    0x769: v769 = DIV v762, v767(0x1)
    0x76a: v76a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x77f: v77f = AND v76a(0xffffffffffffffffffffffffffffffffffffffff), v769
    0x780: v780(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x795: v795 = AND v780(0xffffffffffffffffffffffffffffffffffffffff), v77f
    0x796: v796 = EQ v795, v75b(0x0)
    0x797: v797 = ISZERO v796
    0x798: v798 = ISZERO v797
    0x799: v799(0x80a) = CONST 
    0x79c: JUMPI v799(0x80a), v798

    Begin block 0x79d
    prev=[0x75a], succ=[]
    =================================
    0x79d: v79d(0x40) = CONST 
    0x79f: v79f = MLOAD v79d(0x40)
    0x7a0: v7a0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x7c2: MSTORE v79f, v7a0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7c3: v7c3(0x4) = CONST 
    0x7c5: v7c5 = ADD v7c3(0x4), v79f
    0x7c8: v7c8(0x20) = CONST 
    0x7ca: v7ca = ADD v7c8(0x20), v7c5
    0x7cd: v7cd(0x20) = SUB v7ca, v7c5
    0x7cf: MSTORE v7c5, v7cd(0x20)
    0x7d0: v7d0(0x13) = CONST 
    0x7d3: MSTORE v7ca, v7d0(0x13)
    0x7d4: v7d4(0x20) = CONST 
    0x7d6: v7d6 = ADD v7d4(0x20), v7ca
    0x7d8: v7d8(0x416c726561647920696e697469616c697a656400000000000000000000000000) = CONST 
    0x7fa: MSTORE v7d6, v7d8(0x416c726561647920696e697469616c697a656400000000000000000000000000)
    0x7fc: v7fc(0x20) = CONST 
    0x7fe: v7fe = ADD v7fc(0x20), v7d6
    0x802: v802(0x40) = CONST 
    0x804: v804 = MLOAD v802(0x40)
    0x807: v807(0x64) = SUB v7fe, v804
    0x809: REVERT v804, v807(0x64)

    Begin block 0x80a
    prev=[0x75a], succ=[0x46f0x388]
    =================================
    0x80b: v80b = CALLER 
    0x80c: v80c(0x3) = CONST 
    0x80e: v80e(0x0) = CONST 
    0x810: v810(0x100) = CONST 
    0x813: v813(0x1) = EXP v810(0x100), v80e(0x0)
    0x815: v815 = SLOAD v80c(0x3)
    0x817: v817(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x82c: v82c(0xffffffffffffffffffffffffffffffffffffffff) = MUL v817(0xffffffffffffffffffffffffffffffffffffffff), v813(0x1)
    0x82d: v82d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v82c(0xffffffffffffffffffffffffffffffffffffffff)
    0x82e: v82e = AND v82d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v815
    0x831: v831(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x846: v846 = AND v831(0xffffffffffffffffffffffffffffffffffffffff), v80b
    0x847: v847 = MUL v846, v813(0x1)
    0x848: v848 = OR v847, v82e
    0x84a: SSTORE v80c(0x3), v848
    0x84d: v84d(0x4) = CONST 
    0x84f: v84f(0x0) = CONST 
    0x851: v851(0x100) = CONST 
    0x854: v854(0x1) = EXP v851(0x100), v84f(0x0)
    0x856: v856 = SLOAD v84d(0x4)
    0x858: v858(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x86d: v86d(0xffffffffffffffffffffffffffffffffffffffff) = MUL v858(0xffffffffffffffffffffffffffffffffffffffff), v854(0x1)
    0x86e: v86e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v86d(0xffffffffffffffffffffffffffffffffffffffff)
    0x86f: v86f = AND v86e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v856
    0x872: v872(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x887: v887 = AND v872(0xffffffffffffffffffffffffffffffffffffffff), v3b9
    0x888: v888 = MUL v887, v854(0x1)
    0x889: v889 = OR v888, v86f
    0x88b: SSTORE v84d(0x4), v889
    0x88d: v88d(0x8c9) = CONST 
    0x891: v891(0x0) = CONST 
    0x893: v893 = CALLDATASIZE 
    0x896: v896(0x1f) = CONST 
    0x898: v898 = ADD v896(0x1f), v893
    0x899: v899(0x20) = CONST 
    0x89d: v89d = DIV v898, v899(0x20)
    0x89e: v89e = MUL v89d, v899(0x20)
    0x89f: v89f(0x20) = CONST 
    0x8a1: v8a1 = ADD v89f(0x20), v89e
    0x8a2: v8a2(0x40) = CONST 
    0x8a4: v8a4 = MLOAD v8a2(0x40)
    0x8a7: v8a7 = ADD v8a4, v8a1
    0x8a8: v8a8(0x40) = CONST 
    0x8aa: MSTORE v8a8(0x40), v8a7
    0x8b2: MSTORE v8a4, v893
    0x8b3: v8b3(0x20) = CONST 
    0x8b5: v8b5 = ADD v8b3(0x20), v8a4
    0x8bb: CALLDATACOPY v8b5, v891(0x0), v893
    0x8bd: v8bd = ADD v8b5, v893
    0x8c5: v8c5(0x46f) = CONST 
    0x8c8: JUMP v8c5(0x46f)

    Begin block 0x46f0x388
    prev=[0x80a], succ=[0x4920x388, 0x4950x388]
    =================================
    0x4700x388: v388470(0x0) = CONST 
    0x4740x388: v388474 = MLOAD v8a4
    0x4750x388: v388475(0x20) = CONST 
    0x4780x388: v388478 = ADD v8a4, v388475(0x20)
    0x47a0x388: v38847a(0x2710) = CONST 
    0x47d0x388: v38847d = GAS 
    0x47e0x388: v38847e = SUB v38847d, v38847a(0x2710)
    0x47f0x388: v38847f = DELEGATECALL v38847e, v3b9, v388478, v388474, v388470(0x0), v388470(0x0)
    0x4800x388: v388480 = RETURNDATASIZE 
    0x4810x388: v388481(0x40) = CONST 
    0x4830x388: v388483 = MLOAD v388481(0x40)
    0x4850x388: v388485(0x0) = CONST 
    0x4880x388: RETURNDATACOPY v388483, v388485(0x0), v388480
    0x48a0x388: v38848a(0x0) = CONST 
    0x48d0x388: v38848d = EQ v38847f, v38848a(0x0)
    0x48e0x388: v38848e(0x495) = CONST 
    0x4910x388: JUMPI v38848e(0x495), v38848d

    Begin block 0x4920x388
    prev=[0x46f0x388], succ=[]
    =================================
    0x4940x388: RETURN v388483, v388480

    Begin block 0x4950x388
    prev=[0x46f0x388], succ=[]
    =================================
    0x4980x388: REVERT v388483, v388480

}

function delegation()() public {
    Begin block 0x3d5
    prev=[], succ=[0x3dd, 0x3e1]
    =================================
    0x3d6: v3d6 = CALLVALUE 
    0x3d8: v3d8 = ISZERO v3d6
    0x3d9: v3d9(0x3e1) = CONST 
    0x3dc: JUMPI v3d9(0x3e1), v3d8

    Begin block 0x3dd
    prev=[0x3d5], succ=[]
    =================================
    0x3dd: v3dd(0x0) = CONST 
    0x3e0: REVERT v3dd(0x0), v3dd(0x0)

    Begin block 0x3e1
    prev=[0x3d5], succ=[0x8cd]
    =================================
    0x3e3: v3e3(0x3ea) = CONST 
    0x3e6: v3e6(0x8cd) = CONST 
    0x3e9: JUMP v3e6(0x8cd)

    Begin block 0x8cd
    prev=[0x3e1], succ=[0x3ea]
    =================================
    0x8ce: v8ce(0x4) = CONST 
    0x8d0: v8d0(0x0) = CONST 
    0x8d3: v8d3 = SLOAD v8ce(0x4)
    0x8d5: v8d5(0x100) = CONST 
    0x8d8: v8d8(0x1) = EXP v8d5(0x100), v8d0(0x0)
    0x8da: v8da = DIV v8d3, v8d8(0x1)
    0x8db: v8db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8f0: v8f0 = AND v8db(0xffffffffffffffffffffffffffffffffffffffff), v8da
    0x8f2: JUMP v3e3(0x3ea)

    Begin block 0x3ea
    prev=[0x8cd], succ=[]
    =================================
    0x3eb: v3eb(0x40) = CONST 
    0x3ed: v3ed = MLOAD v3eb(0x40)
    0x3f0: v3f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x405: v405 = AND v3f0(0xffffffffffffffffffffffffffffffffffffffff), v8f0
    0x406: v406(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x41b: v41b = AND v406(0xffffffffffffffffffffffffffffffffffffffff), v405
    0x41d: MSTORE v3ed, v41b
    0x41e: v41e(0x20) = CONST 
    0x420: v420 = ADD v41e(0x20), v3ed
    0x424: v424(0x40) = CONST 
    0x426: v426 = MLOAD v424(0x40)
    0x429: v429(0x20) = SUB v420, v426
    0x42b: RETURN v426, v429(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x42c
    prev=[], succ=[0x434, 0x438]
    =================================
    0x42d: v42d = CALLVALUE 
    0x42f: v42f = ISZERO v42d
    0x430: v430(0x438) = CONST 
    0x433: JUMPI v430(0x438), v42f

    Begin block 0x434
    prev=[0x42c], succ=[]
    =================================
    0x434: v434(0x0) = CONST 
    0x437: REVERT v434(0x0), v434(0x0)

    Begin block 0x438
    prev=[0x42c], succ=[0x8f3]
    =================================
    0x43a: v43a(0x46d) = CONST 
    0x43d: v43d(0x4) = CONST 
    0x440: v440 = CALLDATASIZE 
    0x441: v441 = SUB v440, v43d(0x4)
    0x443: v443 = ADD v43d(0x4), v441
    0x447: v447 = CALLDATALOAD v43d(0x4)
    0x448: v448(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x45d: v45d = AND v448(0xffffffffffffffffffffffffffffffffffffffff), v447
    0x45f: v45f(0x20) = CONST 
    0x461: v461(0x24) = ADD v45f(0x20), v43d(0x4)
    0x469: v469(0x8f3) = CONST 
    0x46c: JUMP v469(0x8f3)

    Begin block 0x8f3
    prev=[0x438], succ=[0x94b, 0x9b8]
    =================================
    0x8f4: v8f4(0x3) = CONST 
    0x8f6: v8f6(0x0) = CONST 
    0x8f9: v8f9 = SLOAD v8f4(0x3)
    0x8fb: v8fb(0x100) = CONST 
    0x8fe: v8fe(0x1) = EXP v8fb(0x100), v8f6(0x0)
    0x900: v900 = DIV v8f9, v8fe(0x1)
    0x901: v901(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x916: v916 = AND v901(0xffffffffffffffffffffffffffffffffffffffff), v900
    0x917: v917(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x92c: v92c = AND v917(0xffffffffffffffffffffffffffffffffffffffff), v916
    0x92d: v92d = CALLER 
    0x92e: v92e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x943: v943 = AND v92e(0xffffffffffffffffffffffffffffffffffffffff), v92d
    0x944: v944 = EQ v943, v92c
    0x945: v945 = ISZERO v944
    0x946: v946 = ISZERO v945
    0x947: v947(0x9b8) = CONST 
    0x94a: JUMPI v947(0x9b8), v946

    Begin block 0x94b
    prev=[0x8f3], succ=[]
    =================================
    0x94b: v94b(0x40) = CONST 
    0x94d: v94d = MLOAD v94b(0x40)
    0x94e: v94e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x970: MSTORE v94d, v94e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x971: v971(0x4) = CONST 
    0x973: v973 = ADD v971(0x4), v94d
    0x976: v976(0x20) = CONST 
    0x978: v978 = ADD v976(0x20), v973
    0x97b: v97b(0x20) = SUB v978, v973
    0x97d: MSTORE v973, v97b(0x20)
    0x97e: v97e(0x17) = CONST 
    0x981: MSTORE v978, v97e(0x17)
    0x982: v982(0x20) = CONST 
    0x984: v984 = ADD v982(0x20), v978
    0x986: v986(0x53656e646572206973206e6f7420746865206f776e6572000000000000000000) = CONST 
    0x9a8: MSTORE v984, v986(0x53656e646572206973206e6f7420746865206f776e6572000000000000000000)
    0x9aa: v9aa(0x20) = CONST 
    0x9ac: v9ac = ADD v9aa(0x20), v984
    0x9b0: v9b0(0x40) = CONST 
    0x9b2: v9b2 = MLOAD v9b0(0x40)
    0x9b5: v9b5(0x64) = SUB v9ac, v9b2
    0x9b7: REVERT v9b2, v9b5(0x64)

    Begin block 0x9b8
    prev=[0x8f3], succ=[0x9f0, 0xa5d]
    =================================
    0x9b9: v9b9(0x0) = CONST 
    0x9bb: v9bb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9d0: v9d0(0x0) = AND v9bb(0xffffffffffffffffffffffffffffffffffffffff), v9b9(0x0)
    0x9d2: v9d2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9e7: v9e7 = AND v9d2(0xffffffffffffffffffffffffffffffffffffffff), v45d
    0x9e8: v9e8 = EQ v9e7, v9d0(0x0)
    0x9e9: v9e9 = ISZERO v9e8
    0x9ea: v9ea = ISZERO v9e9
    0x9eb: v9eb = ISZERO v9ea
    0x9ec: v9ec(0xa5d) = CONST 
    0x9ef: JUMPI v9ec(0xa5d), v9eb

    Begin block 0x9f0
    prev=[0x9b8], succ=[]
    =================================
    0x9f0: v9f0(0x40) = CONST 
    0x9f2: v9f2 = MLOAD v9f0(0x40)
    0x9f3: v9f3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa15: MSTORE v9f2, v9f3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa16: va16(0x4) = CONST 
    0xa18: va18 = ADD va16(0x4), v9f2
    0xa1b: va1b(0x20) = CONST 
    0xa1d: va1d = ADD va1b(0x20), va18
    0xa20: va20(0x20) = SUB va1d, va18
    0xa22: MSTORE va18, va20(0x20)
    0xa23: va23(0x1f) = CONST 
    0xa26: MSTORE va1d, va23(0x1f)
    0xa27: va27(0x20) = CONST 
    0xa29: va29 = ADD va27(0x20), va1d
    0xa2b: va2b(0x547279696e6720746f207472616e7366657220746f2061646472657373203000) = CONST 
    0xa4d: MSTORE va29, va2b(0x547279696e6720746f207472616e7366657220746f2061646472657373203000)
    0xa4f: va4f(0x20) = CONST 
    0xa51: va51 = ADD va4f(0x20), va29
    0xa55: va55(0x40) = CONST 
    0xa57: va57 = MLOAD va55(0x40)
    0xa5a: va5a(0x64) = SUB va51, va57
    0xa5c: REVERT va57, va5a(0x64)

    Begin block 0xa5d
    prev=[0x9b8], succ=[0x46d]
    =================================
    0xa5f: va5f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa74: va74 = AND va5f(0xffffffffffffffffffffffffffffffffffffffff), v45d
    0xa75: va75(0x3) = CONST 
    0xa77: va77(0x0) = CONST 
    0xa7a: va7a = SLOAD va75(0x3)
    0xa7c: va7c(0x100) = CONST 
    0xa7f: va7f(0x1) = EXP va7c(0x100), va77(0x0)
    0xa81: va81 = DIV va7a, va7f(0x1)
    0xa82: va82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa97: va97 = AND va82(0xffffffffffffffffffffffffffffffffffffffff), va81
    0xa98: va98(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaad: vaad = AND va98(0xffffffffffffffffffffffffffffffffffffffff), va97
    0xaae: vaae(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xacf: vacf(0x40) = CONST 
    0xad1: vad1 = MLOAD vacf(0x40)
    0xad2: vad2(0x40) = CONST 
    0xad4: vad4 = MLOAD vad2(0x40)
    0xad7: vad7(0x0) = SUB vad1, vad4
    0xad9: LOG3 vad4, vad7(0x0), vaae(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vaad, va74
    0xadb: vadb(0x3) = CONST 
    0xadd: vadd(0x0) = CONST 
    0xadf: vadf(0x100) = CONST 
    0xae2: vae2(0x1) = EXP vadf(0x100), vadd(0x0)
    0xae4: vae4 = SLOAD vadb(0x3)
    0xae6: vae6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xafb: vafb(0xffffffffffffffffffffffffffffffffffffffff) = MUL vae6(0xffffffffffffffffffffffffffffffffffffffff), vae2(0x1)
    0xafc: vafc(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vafb(0xffffffffffffffffffffffffffffffffffffffff)
    0xafd: vafd = AND vafc(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vae4
    0xb00: vb00(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb15: vb15 = AND vb00(0xffffffffffffffffffffffffffffffffffffffff), v45d
    0xb16: vb16 = MUL vb15, vae2(0x1)
    0xb17: vb17 = OR vb16, vafd
    0xb19: SSTORE vadb(0x3), vb17
    0xb1c: JUMP v43a(0x46d)

    Begin block 0x46d
    prev=[0xa5d], succ=[]
    =================================
    0x46e: STOP 

}

function fallback()() public {
    Begin block 0x8e
    prev=[], succ=[0x96, 0x9a]
    =================================
    0x8f: v8f = CALLVALUE 
    0x91: v91 = ISZERO v8f
    0x92: v92(0x9a) = CONST 
    0x95: JUMPI v92(0x9a), v91

    Begin block 0x96
    prev=[0x8e], succ=[]
    =================================
    0x96: v96(0x0) = CONST 
    0x99: REVERT v96(0x0), v96(0x0)

    Begin block 0x9a
    prev=[0x8e], succ=[0xf5, 0x188]
    =================================
    0x9c: v9c(0x0) = CONST 
    0x9e: v9e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb3: vb3(0x0) = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v9c(0x0)
    0xb4: vb4(0x4) = CONST 
    0xb6: vb6(0x0) = CONST 
    0xb9: vb9 = SLOAD vb4(0x4)
    0xbb: vbb(0x100) = CONST 
    0xbe: vbe(0x1) = EXP vbb(0x100), vb6(0x0)
    0xc0: vc0 = DIV vb9, vbe(0x1)
    0xc1: vc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd6: vd6 = AND vc1(0xffffffffffffffffffffffffffffffffffffffff), vc0
    0xd7: vd7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec: vec = AND vd7(0xffffffffffffffffffffffffffffffffffffffff), vd6
    0xed: ved = EQ vec, vb3(0x0)
    0xee: vee = ISZERO ved
    0xef: vef = ISZERO vee
    0xf0: vf0 = ISZERO vef
    0xf1: vf1(0x188) = CONST 
    0xf4: JUMPI vf1(0x188), vf0

    Begin block 0xf5
    prev=[0x9a], succ=[]
    =================================
    0xf5: vf5(0x40) = CONST 
    0xf7: vf7 = MLOAD vf5(0x40)
    0xf8: vf8(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11a: MSTORE vf7, vf8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11b: v11b(0x4) = CONST 
    0x11d: v11d = ADD v11b(0x4), vf7
    0x120: v120(0x20) = CONST 
    0x122: v122 = ADD v120(0x20), v11d
    0x125: v125(0x20) = SUB v122, v11d
    0x127: MSTORE v11d, v125(0x20)
    0x128: v128(0x28) = CONST 
    0x12b: MSTORE v122, v128(0x28)
    0x12c: v12c(0x20) = CONST 
    0x12e: v12e = ADD v12c(0x20), v122
    0x130: v130(0x44656c65676174696f6e206973206164647265737320302c206e6f7420696e69) = CONST 
    0x152: MSTORE v12e, v130(0x44656c65676174696f6e206973206164647265737320302c206e6f7420696e69)
    0x153: v153(0x20) = CONST 
    0x155: v155 = ADD v153(0x20), v12e
    0x156: v156(0x7469616c697a6564000000000000000000000000000000000000000000000000) = CONST 
    0x178: MSTORE v155, v156(0x7469616c697a6564000000000000000000000000000000000000000000000000)
    0x17a: v17a(0x40) = CONST 
    0x17c: v17c = ADD v17a(0x40), v12e
    0x180: v180(0x40) = CONST 
    0x182: v182 = MLOAD v180(0x40)
    0x185: v185(0x84) = SUB v17c, v182
    0x187: REVERT v182, v185(0x84)

    Begin block 0x188
    prev=[0x9a], succ=[0x46f0x8e]
    =================================
    0x189: v189(0x1e7) = CONST 
    0x18c: v18c(0x4) = CONST 
    0x18e: v18e(0x0) = CONST 
    0x191: v191 = SLOAD v18c(0x4)
    0x193: v193(0x100) = CONST 
    0x196: v196(0x1) = EXP v193(0x100), v18e(0x0)
    0x198: v198 = DIV v191, v196(0x1)
    0x199: v199(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ae: v1ae = AND v199(0xffffffffffffffffffffffffffffffffffffffff), v198
    0x1af: v1af(0x0) = CONST 
    0x1b1: v1b1 = CALLDATASIZE 
    0x1b4: v1b4(0x1f) = CONST 
    0x1b6: v1b6 = ADD v1b4(0x1f), v1b1
    0x1b7: v1b7(0x20) = CONST 
    0x1bb: v1bb = DIV v1b6, v1b7(0x20)
    0x1bc: v1bc = MUL v1bb, v1b7(0x20)
    0x1bd: v1bd(0x20) = CONST 
    0x1bf: v1bf = ADD v1bd(0x20), v1bc
    0x1c0: v1c0(0x40) = CONST 
    0x1c2: v1c2 = MLOAD v1c0(0x40)
    0x1c5: v1c5 = ADD v1c2, v1bf
    0x1c6: v1c6(0x40) = CONST 
    0x1c8: MSTORE v1c6(0x40), v1c5
    0x1d0: MSTORE v1c2, v1b1
    0x1d1: v1d1(0x20) = CONST 
    0x1d3: v1d3 = ADD v1d1(0x20), v1c2
    0x1d9: CALLDATACOPY v1d3, v1af(0x0), v1b1
    0x1db: v1db = ADD v1d3, v1b1
    0x1e3: v1e3(0x46f) = CONST 
    0x1e6: JUMP v1e3(0x46f)

    Begin block 0x46f0x8e
    prev=[0x188], succ=[0x4920x8e, 0x4950x8e]
    =================================
    0x4700x8e: v8e470(0x0) = CONST 
    0x4740x8e: v8e474 = MLOAD v1c2
    0x4750x8e: v8e475(0x20) = CONST 
    0x4780x8e: v8e478 = ADD v1c2, v8e475(0x20)
    0x47a0x8e: v8e47a(0x2710) = CONST 
    0x47d0x8e: v8e47d = GAS 
    0x47e0x8e: v8e47e = SUB v8e47d, v8e47a(0x2710)
    0x47f0x8e: v8e47f = DELEGATECALL v8e47e, v1ae, v8e478, v8e474, v8e470(0x0), v8e470(0x0)
    0x4800x8e: v8e480 = RETURNDATASIZE 
    0x4810x8e: v8e481(0x40) = CONST 
    0x4830x8e: v8e483 = MLOAD v8e481(0x40)
    0x4850x8e: v8e485(0x0) = CONST 
    0x4880x8e: RETURNDATACOPY v8e483, v8e485(0x0), v8e480
    0x48a0x8e: v8e48a(0x0) = CONST 
    0x48d0x8e: v8e48d = EQ v8e47f, v8e48a(0x0)
    0x48e0x8e: v8e48e(0x495) = CONST 
    0x4910x8e: JUMPI v8e48e(0x495), v8e48d

    Begin block 0x4920x8e
    prev=[0x46f0x8e], succ=[]
    =================================
    0x4940x8e: RETURN v8e483, v8e480

    Begin block 0x4950x8e
    prev=[0x46f0x8e], succ=[]
    =================================
    0x4980x8e: REVERT v8e483, v8e480

}

