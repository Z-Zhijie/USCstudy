function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x5b, 0x5f]
    =================================
    0x0: v0(0xe0) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0xe0)
    0x5: v5(0x2) = CONST 
    0x7: v7(0x80) = CONST 
    0xb: MSTORE v7(0x80), v5(0x2)
    0xc: vc(0x1) = CONST 
    0xe: ve(0xa0) = CONST 
    0x10: MSTORE ve(0xa0), vc(0x1)
    0x11: v11(0x0) = CONST 
    0x13: v13(0xc0) = CONST 
    0x15: MSTORE v13(0xc0), v11(0x0)
    0x16: v16(0x6) = CONST 
    0x19: v19 = SLOAD v16(0x6)
    0x1a: v1a(0x80) = CONST 
    0x1c: v1c(0x2) = CONST 
    0x1e: v1e(0x100000000000000000000000000000000) = EXP v1c(0x2), v1a(0x80)
    0x1f: v1f(0xc0) = CONST 
    0x21: v21(0x2) = CONST 
    0x23: v23(0x1000000000000000000000000000000000000000000000000) = EXP v21(0x2), v1f(0xc0)
    0x24: v24(0xffffffffffffffff00000000000000000000000000000000) = SUB v23(0x1000000000000000000000000000000000000000000000000), v1e(0x100000000000000000000000000000000)
    0x25: v25(0xffffffffffffffff0000000000000000ffffffffffffffffffffffffffffffff) = NOT v24(0xffffffffffffffff00000000000000000000000000000000)
    0x26: v26(0x40) = CONST 
    0x28: v28(0x2) = CONST 
    0x2a: v2a(0x10000000000000000) = EXP v28(0x2), v26(0x40)
    0x2b: v2b(0x80) = CONST 
    0x2d: v2d(0x2) = CONST 
    0x2f: v2f(0x100000000000000000000000000000000) = EXP v2d(0x2), v2b(0x80)
    0x30: v30(0xffffffffffffffff0000000000000000) = SUB v2f(0x100000000000000000000000000000000), v2a(0x10000000000000000)
    0x31: v31(0xffffffffffffffffffffffffffffffff0000000000000000ffffffffffffffff) = NOT v30(0xffffffffffffffff0000000000000000)
    0x32: v32(0xffffffffffffffff) = CONST 
    0x3b: v3b(0xffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000) = NOT v32(0xffffffffffffffff)
    0x3e: v3e = AND v19, v3b(0xffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000)
    0x41: v41 = OR v5(0x2), v3e
    0x42: v42 = AND v41, v31(0xffffffffffffffffffffffffffffffff0000000000000000ffffffffffffffff)
    0x43: v43(0x10000000000000000) = CONST 
    0x4d: v4d = OR v43(0x10000000000000000), v42
    0x51: v51 = AND v4d, v25(0xffffffffffffffff0000000000000000ffffffffffffffffffffffffffffffff)
    0x53: SSTORE v16(0x6), v51
    0x54: v54 = CALLVALUE 
    0x56: v56 = ISZERO v54
    0x57: v57(0x5f) = CONST 
    0x5a: JUMPI v57(0x5f), v56

    Begin block 0x5b
    prev=[0x0], succ=[]
    =================================
    0x5b: v5b(0x0) = CONST 
    0x5e: REVERT v5b(0x0), v5b(0x0)

    Begin block 0x5f
    prev=[0x0], succ=[]
    =================================
    0x61: v61(0x2493) = CONST 
    0x65: v65(0x6f) = CONST 
    0x68: v68(0x0) = CONST 
    0x6a: CODECOPY v68(0x0), v65(0x6f), v61(0x2493)
    0x6b: v6b(0x0) = CONST 
    0x6d: RETURN v6b(0x0), v61(0x2493)

}

