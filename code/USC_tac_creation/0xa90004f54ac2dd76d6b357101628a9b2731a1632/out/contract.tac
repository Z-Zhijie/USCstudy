function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x55, 0x59]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x8: v8 = SLOAD v5(0x1)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa0) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = SHL vd(0xa0), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x14: v14 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x15: v15(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f) = CONST 
    0x2a: v2a = OR v15(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f), v14
    0x2d: SSTORE v5(0x1), v2a
    0x2e: v2e(0x2) = CONST 
    0x31: v31 = SLOAD v2e(0x2)
    0x34: v34 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v31
    0x35: v35(0x7a250d5630b4cf539739df2c5dacb4c659f2488d) = CONST 
    0x4a: v4a = OR v35(0x7a250d5630b4cf539739df2c5dacb4c659f2488d), v34
    0x4c: SSTORE v2e(0x2), v4a
    0x4d: v4d = CALLVALUE 
    0x4f: v4f = ISZERO v4d
    0x50: v50(0x59) = CONST 
    0x54: JUMPI v50(0x59), v4f

    Begin block 0x55
    prev=[0x0], succ=[]
    =================================
    0x55: v55(0x0) = CONST 
    0x58: REVERT v55(0x0), v55(0x0)

    Begin block 0x59
    prev=[0x0], succ=[0xba]
    =================================
    0x5b: v5b(0x0) = CONST 
    0x5d: v5d(0x66) = CONST 
    0x61: v61(0xba) = CONST 
    0x65: JUMP v61(0xba)

    Begin block 0xba
    prev=[0x59], succ=[0x66]
    =================================
    0xbb: vbb = CALLER 
    0xbd: JUMP v5d(0x66)

    Begin block 0x66
    prev=[0xba], succ=[0xbe]
    =================================
    0x67: v67(0x4) = CONST 
    0x6a: v6a = SLOAD v67(0x4)
    0x6b: v6b(0x1) = CONST 
    0x6d: v6d(0x1) = CONST 
    0x6f: v6f(0xa0) = CONST 
    0x71: v71(0x10000000000000000000000000000000000000000) = SHL v6f(0xa0), v6d(0x1)
    0x72: v72(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71(0x10000000000000000000000000000000000000000), v6b(0x1)
    0x73: v73(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v72(0xffffffffffffffffffffffffffffffffffffffff)
    0x74: v74 = AND v73(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6a
    0x75: v75(0x1) = CONST 
    0x77: v77(0x1) = CONST 
    0x79: v79(0xa0) = CONST 
    0x7b: v7b(0x10000000000000000000000000000000000000000) = SHL v79(0xa0), v77(0x1)
    0x7c: v7c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b(0x10000000000000000000000000000000000000000), v75(0x1)
    0x7e: v7e = AND vbb, v7c(0xffffffffffffffffffffffffffffffffffffffff)
    0x81: v81 = OR v7e, v74
    0x84: SSTORE v67(0x4), v81
    0x85: v85(0x40) = CONST 
    0x87: v87 = MLOAD v85(0x40)
    0x8c: v8c(0x0) = CONST 
    0x8f: v8f(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xb3: LOG3 v87, v8c(0x0), v8f(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v8c(0x0), v7e
    0xb5: vb5(0xbe) = CONST 
    0xb9: JUMP vb5(0xbe)

    Begin block 0xbe
    prev=[0x66], succ=[]
    =================================
    0xbf: vbf(0x3559) = CONST 
    0xc3: vc3(0xce) = CONST 
    0xc7: vc7(0x0) = CONST 
    0xc9: CODECOPY vc7(0x0), vc3(0xce), vbf(0x3559)
    0xca: vca(0x0) = CONST 
    0xcc: RETURN vca(0x0), vbf(0x3559)

}

