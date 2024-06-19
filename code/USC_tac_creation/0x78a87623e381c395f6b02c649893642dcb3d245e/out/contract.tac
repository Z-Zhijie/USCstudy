function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0x1) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0x2) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = EXP vd(0x2), vb(0xa0)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x14: v14 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x15: v15 = CALLER 
    0x16: v16 = OR v15, v14
    0x19: SSTORE v5(0x0), v16
    0x1a: v1a(0x1) = CONST 
    0x1d: v1d = SLOAD v1a(0x1)
    0x20: v20 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1d
    0x22: SSTORE v1a(0x1), v20
    0x23: v23(0x2abf) = CONST 
    0x27: v27(0x31) = CONST 
    0x2a: v2a(0x0) = CONST 
    0x2c: CODECOPY v2a(0x0), v27(0x31), v23(0x2abf)
    0x2d: v2d(0x0) = CONST 
    0x2f: RETURN v2d(0x0), v23(0x2abf)

}

