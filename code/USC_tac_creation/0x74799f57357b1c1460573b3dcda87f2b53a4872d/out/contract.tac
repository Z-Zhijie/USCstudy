function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1e, 0x22]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x3) = CONST 
    0x8: v8 = SLOAD v5(0x3)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa0) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = SHL vd(0xa0), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x13: v13 = CALLER 
    0x14: v14 = OR v13, v12
    0x16: SSTORE v5(0x3), v14
    0x17: v17 = CALLVALUE 
    0x19: v19 = ISZERO v17
    0x1a: v1a(0x22) = CONST 
    0x1d: JUMPI v1a(0x22), v19

    Begin block 0x1e
    prev=[0x0], succ=[]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x21: REVERT v1e(0x0), v1e(0x0)

    Begin block 0x22
    prev=[0x0], succ=[]
    =================================
    0x24: v24(0x1622) = CONST 
    0x28: v28(0x32) = CONST 
    0x2b: v2b(0x0) = CONST 
    0x2d: CODECOPY v2b(0x0), v28(0x32), v24(0x1622)
    0x2e: v2e(0x0) = CONST 
    0x30: RETURN v2e(0x0), v24(0x1622)

}

