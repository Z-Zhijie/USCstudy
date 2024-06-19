function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x19, 0x1d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x56bc75e2d63100000) = CONST 
    0xf: vf(0xe) = CONST 
    0x11: SSTORE vf(0xe), v5(0x56bc75e2d63100000)
    0x12: v12 = CALLVALUE 
    0x14: v14 = ISZERO v12
    0x15: v15(0x1d) = CONST 
    0x18: JUMPI v15(0x1d), v14

    Begin block 0x19
    prev=[0x0], succ=[]
    =================================
    0x19: v19(0x0) = CONST 
    0x1c: REVERT v19(0x0), v19(0x0)

    Begin block 0x1d
    prev=[0x0], succ=[]
    =================================
    0x1f: v1f(0x0) = CONST 
    0x22: v22 = SLOAD v1f(0x0)
    0x23: v23(0x1) = CONST 
    0x25: v25(0x1) = CONST 
    0x27: v27(0xa0) = CONST 
    0x29: v29(0x10000000000000000000000000000000000000000) = SHL v27(0xa0), v25(0x1)
    0x2a: v2a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29(0x10000000000000000000000000000000000000000), v23(0x1)
    0x2b: v2b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2a(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c: v2c = AND v2b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v22
    0x2d: v2d = CALLER 
    0x2e: v2e = OR v2d, v2c
    0x30: SSTORE v1f(0x0), v2e
    0x31: v31(0x5ce0) = CONST 
    0x35: v35(0x40) = CONST 
    0x39: v39(0x0) = CONST 
    0x3b: CODECOPY v39(0x0), v35(0x40), v31(0x5ce0)
    0x3c: v3c(0x0) = CONST 
    0x3e: RETURN v3c(0x0), v31(0x5ce0)

}

