function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[]
    =================================
    0x12: v12(0x5) = CONST 
    0x15: v15 = SLOAD v12(0x5)
    0x16: v16(0xff00) = CONST 
    0x19: v19(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v16(0xff00)
    0x1a: v1a = AND v19(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v15
    0x1b: v1b(0x100) = CONST 
    0x1e: v1e = OR v1b(0x100), v1a
    0x20: SSTORE v12(0x5), v1e
    0x21: v21(0xc58) = CONST 
    0x25: v25(0x2f) = CONST 
    0x28: v28(0x0) = CONST 
    0x2a: CODECOPY v28(0x0), v25(0x2f), v21(0xc58)
    0x2b: v2b(0x0) = CONST 
    0x2d: RETURN v2b(0x0), v21(0xc58)

}

