function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x3) = CONST 
    0x9: v9(0x0) = CONST 
    0xb: vb(0x100) = CONST 
    0xe: ve(0x1) = EXP vb(0x100), v9(0x0)
    0x10: v10 = SLOAD v7(0x3)
    0x12: v12(0xff) = CONST 
    0x14: v14(0xff) = MUL v12(0xff), ve(0x1)
    0x15: v15(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v14(0xff)
    0x16: v16 = AND v15(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v10
    0x19: v19(0x1) = ISZERO v5(0x0)
    0x1a: v1a(0x0) = ISZERO v19(0x1)
    0x1b: v1b(0x0) = MUL v1a(0x0), ve(0x1)
    0x1c: v1c = OR v1b(0x0), v16
    0x1e: SSTORE v7(0x3), v1c
    0x20: v20 = CALLER 
    0x21: v21(0x0) = CONST 
    0x24: v24(0x100) = CONST 
    0x27: v27(0x1) = EXP v24(0x100), v21(0x0)
    0x29: v29 = SLOAD v21(0x0)
    0x2b: v2b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x40: v40(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2b(0xffffffffffffffffffffffffffffffffffffffff), v27(0x1)
    0x41: v41(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v40(0xffffffffffffffffffffffffffffffffffffffff)
    0x42: v42 = AND v41(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v29
    0x45: v45(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5a: v5a = AND v45(0xffffffffffffffffffffffffffffffffffffffff), v20
    0x5b: v5b = MUL v5a, v27(0x1)
    0x5c: v5c = OR v5b, v42
    0x5e: SSTORE v21(0x0), v5c
    0x60: v60(0x1419) = CONST 
    0x64: v64(0x6e) = CONST 
    0x67: v67(0x0) = CONST 
    0x69: CODECOPY v67(0x0), v64(0x6e), v60(0x1419)
    0x6a: v6a(0x0) = CONST 
    0x6c: RETURN v6a(0x0), v60(0x1419)

}

