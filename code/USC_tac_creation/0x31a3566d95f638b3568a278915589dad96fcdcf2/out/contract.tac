function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x9d, 0xa1]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x8: v8 = SLOAD v5(0x1)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x1), vf
    0x12: v12(0x2) = CONST 
    0x15: v15 = SLOAD v12(0x2)
    0x16: v16(0x1) = CONST 
    0x18: v18(0x1) = CONST 
    0x1a: v1a(0xa0) = CONST 
    0x1c: v1c(0x10000000000000000000000000000000000000000) = SHL v1a(0xa0), v18(0x1)
    0x1d: v1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c(0x10000000000000000000000000000000000000000), v16(0x1)
    0x1e: v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x21: v21 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v15
    0x22: v22(0x3479b0acf875405d7853f44142fe06470a40f6cc) = CONST 
    0x37: v37 = OR v22(0x3479b0acf875405d7853f44142fe06470a40f6cc), v21
    0x3a: SSTORE v12(0x2), v37
    0x3b: v3b(0x3) = CONST 
    0x3e: v3e = SLOAD v3b(0x3)
    0x40: v40 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3e
    0x41: v41(0x71535ad4c7c5925382cdeadc806371cc89a5085d) = CONST 
    0x56: v56 = OR v41(0x71535ad4c7c5925382cdeadc806371cc89a5085d), v40
    0x58: SSTORE v3b(0x3), v56
    0x59: v59(0x4) = CONST 
    0x5c: v5c = SLOAD v59(0x4)
    0x5e: v5e = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5c
    0x5f: v5f(0xa2d385185bbd96f4794ae3504aeaa7825827a297) = CONST 
    0x74: v74 = OR v5f(0xa2d385185bbd96f4794ae3504aeaa7825827a297), v5e
    0x76: SSTORE v59(0x4), v74
    0x77: v77(0x5) = CONST 
    0x7a: v7a = SLOAD v77(0x5)
    0x7d: v7d = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v7a
    0x7e: v7e(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = CONST 
    0x93: v93 = OR v7e(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2), v7d
    0x95: SSTORE v77(0x5), v93
    0x96: v96 = CALLVALUE 
    0x98: v98 = ISZERO v96
    0x99: v99(0xa1) = CONST 
    0x9c: JUMPI v99(0xa1), v98

    Begin block 0x9d
    prev=[0x0], succ=[]
    =================================
    0x9d: v9d(0x0) = CONST 
    0xa0: REVERT v9d(0x0), v9d(0x0)

    Begin block 0xa1
    prev=[0x0], succ=[]
    =================================
    0xa3: va3(0x2d86) = CONST 
    0xa7: va7(0xb1) = CONST 
    0xaa: vaa(0x0) = CONST 
    0xac: CODECOPY vaa(0x0), va7(0xb1), va3(0x2d86)
    0xad: vad(0x0) = CONST 
    0xaf: RETURN vad(0x0), va3(0x2d86)

}

