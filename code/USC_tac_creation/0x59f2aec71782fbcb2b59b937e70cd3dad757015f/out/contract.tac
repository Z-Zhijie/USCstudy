function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x16, 0x1a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xd) = CONST 
    0x8: v8 = SLOAD v5(0xd)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9(0xff)
    0xc: vc = AND vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8
    0xe: SSTORE v5(0xd), vc
    0xf: vf = CALLVALUE 
    0x11: v11 = ISZERO vf
    0x12: v12(0x1a) = CONST 
    0x15: JUMPI v12(0x1a), v11

    Begin block 0x16
    prev=[0x0], succ=[]
    =================================
    0x16: v16(0x0) = CONST 
    0x19: REVERT v16(0x0), v16(0x0)

    Begin block 0x1a
    prev=[0x0], succ=[]
    =================================
    0x1c: v1c(0x0) = CONST 
    0x1f: v1f = SLOAD v1c(0x0)
    0x20: v20(0x1) = CONST 
    0x22: v22(0xa0) = CONST 
    0x24: v24(0x2) = CONST 
    0x26: v26(0x10000000000000000000000000000000000000000) = EXP v24(0x2), v22(0xa0)
    0x27: v27(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26(0x10000000000000000000000000000000000000000), v20(0x1)
    0x28: v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27(0xffffffffffffffffffffffffffffffffffffffff)
    0x29: v29 = AND v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f
    0x2a: v2a = CALLER 
    0x2b: v2b = OR v2a, v29
    0x2d: SSTORE v1c(0x0), v2b
    0x2e: v2e(0x1d81) = CONST 
    0x32: v32(0x3c) = CONST 
    0x35: v35(0x0) = CONST 
    0x37: CODECOPY v35(0x0), v32(0x3c), v2e(0x1d81)
    0x38: v38(0x0) = CONST 
    0x3a: RETURN v38(0x0), v2e(0x1d81)

}

