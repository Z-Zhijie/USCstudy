function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1f, 0x1b]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x97) = CONST 
    0x8: v8 = SLOAD v5(0x97)
    0x9: v9(0xffff) = CONST 
    0xc: vc(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT v9(0xffff)
    0xd: vd = AND vc(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000), v8
    0xe: ve(0x2406) = CONST 
    0x11: v11 = OR ve(0x2406), vd
    0x13: SSTORE v5(0x97), v11
    0x14: v14 = CALLVALUE 
    0x16: v16 = ISZERO v14
    0x17: v17(0x1f) = CONST 
    0x1a: JUMPI v17(0x1f), v16

    Begin block 0x1f
    prev=[0x0], succ=[]
    =================================
    0x21: v21(0x99) = CONST 
    0x24: v24 = SLOAD v21(0x99)
    0x25: v25(0x1) = CONST 
    0x27: v27(0x1) = CONST 
    0x29: v29(0xa0) = CONST 
    0x2b: v2b(0x10000000000000000000000000000000000000000) = SHL v29(0xa0), v27(0x1)
    0x2c: v2c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b(0x10000000000000000000000000000000000000000), v25(0x1)
    0x2d: v2d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2c(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e: v2e = AND v2d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v24
    0x2f: v2f(0x1) = CONST 
    0x31: v31 = OR v2f(0x1), v2e
    0x33: SSTORE v21(0x99), v31
    0x34: v34(0x1a7c) = CONST 
    0x38: v38(0x42) = CONST 
    0x3b: v3b(0x0) = CONST 
    0x3d: CODECOPY v3b(0x0), v38(0x42), v34(0x1a7c)
    0x3e: v3e(0x0) = CONST 
    0x40: RETURN v3e(0x0), v34(0x1a7c)

    Begin block 0x1b
    prev=[0x0], succ=[]
    =================================
    0x1b: v1b(0x0) = CONST 
    0x1e: REVERT v1b(0x0), v1b(0x0)

}

