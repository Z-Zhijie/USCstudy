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
    0x12: v12(0xcf) = CONST 
    0x15: v15 = SLOAD v12(0xcf)
    0x16: v16(0x1) = CONST 
    0x18: v18(0x1) = CONST 
    0x1a: v1a(0xa0) = CONST 
    0x1c: v1c(0x10000000000000000000000000000000000000000) = SHL v1a(0xa0), v18(0x1)
    0x1d: v1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c(0x10000000000000000000000000000000000000000), v16(0x1)
    0x1e: v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f: v1f = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v15
    0x20: v20(0x1) = CONST 
    0x22: v22 = OR v20(0x1), v1f
    0x24: SSTORE v12(0xcf), v22
    0x25: v25(0x5fad) = CONST 
    0x29: v29(0x34) = CONST 
    0x2d: v2d(0x0) = CONST 
    0x2f: CODECOPY v2d(0x0), v29(0x34), v25(0x5fad)
    0x30: v30(0x0) = CONST 
    0x32: RETURN v30(0x0), v25(0x5fad)

}

