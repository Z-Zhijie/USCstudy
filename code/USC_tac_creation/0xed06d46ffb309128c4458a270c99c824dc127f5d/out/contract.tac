function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x32, 0x36]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x7) = CONST 
    0x8: v8 = SLOAD v5(0x7)
    0x9: v9(0xa0) = CONST 
    0xb: vb(0x2) = CONST 
    0xd: vd(0x10000000000000000000000000000000000000000) = EXP vb(0x2), v9(0xa0)
    0xe: ve(0xff) = CONST 
    0x10: v10(0xff0000000000000000000000000000000000000000) = MUL ve(0xff), vd(0x10000000000000000000000000000000000000000)
    0x11: v11(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v10(0xff0000000000000000000000000000000000000000)
    0x12: v12 = AND v11(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x13: v13(0x10000000000000000000000000000000000000000) = CONST 
    0x29: v29 = OR v13(0x10000000000000000000000000000000000000000), v12
    0x2b: SSTORE v5(0x7), v29
    0x2c: v2c = CALLVALUE 
    0x2d: v2d = ISZERO v2c
    0x2e: v2e(0x36) = CONST 
    0x31: JUMPI v2e(0x36), v2d

    Begin block 0x32
    prev=[0x0], succ=[]
    =================================
    0x32: v32(0x0) = CONST 
    0x35: REVERT v32(0x0), v32(0x0)

    Begin block 0x36
    prev=[0x0], succ=[]
    =================================
    0x37: v37(0x2903) = CONST 
    0x3b: v3b(0x45) = CONST 
    0x3e: v3e(0x0) = CONST 
    0x40: CODECOPY v3e(0x0), v3b(0x45), v37(0x2903)
    0x41: v41(0x0) = CONST 
    0x43: RETURN v41(0x0), v37(0x2903)

}

