function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x20, 0x1c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x9c) = CONST 
    0x8: v8 = SLOAD v5(0x9c)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa0) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = SHL vd(0xa0), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x14: SSTORE v5(0x9c), v12
    0x15: v15 = CALLVALUE 
    0x17: v17 = ISZERO v15
    0x18: v18(0x20) = CONST 
    0x1b: JUMPI v18(0x20), v17

    Begin block 0x20
    prev=[0x0], succ=[]
    =================================
    0x22: v22(0x7f8) = CONST 
    0x26: v26(0x30) = CONST 
    0x29: v29(0x0) = CONST 
    0x2b: CODECOPY v29(0x0), v26(0x30), v22(0x7f8)
    0x2c: v2c(0x0) = CONST 
    0x2e: RETURN v2c(0x0), v22(0x7f8)

    Begin block 0x1c
    prev=[0x0], succ=[]
    =================================
    0x1c: v1c(0x0) = CONST 
    0x1f: REVERT v1c(0x0), v1c(0x0)

}

