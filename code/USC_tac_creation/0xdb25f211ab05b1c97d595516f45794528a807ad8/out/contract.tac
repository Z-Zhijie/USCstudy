function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xf, 0xb]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5 = CALLVALUE 
    0x6: v6 = ISZERO v5
    0x7: v7(0xf) = CONST 
    0xa: JUMPI v7(0xf), v6

    Begin block 0xf
    prev=[0x0], succ=[]
    =================================
    0x10: v10(0x40) = CONST 
    0x12: v12 = MLOAD v10(0x40)
    0x13: v13(0x20) = CONST 
    0x16: v16(0x1764) = CONST 
    0x1c: v1c = ADD v1787(0x00000000000000000000000070250fcfef983c9b912c8eefb7021b4b7bae836e), v12
    0x1d: v1d(0x40) = CONST 
    0x1f: MSTORE v1d(0x40), v1c
    0x22: v22 = MLOAD v1787(0x00000000000000000000000070250fcfef983c9b912c8eefb7021b4b7bae836e)
    0x23: v23(0x1f4) = CONST 
    0x26: v26(0x7) = CONST 
    0x28: SSTORE v26(0x7), v23(0x1f4)
    0x29: v29(0x0) = CONST 
    0x2b: v2b(0x8) = CONST 
    0x2f: SSTORE v2b(0x8), v29(0x0)
    0x30: v30(0x9) = CONST 
    0x34: SSTORE v30(0x9), v29(0x0)
    0x35: v35(0xa) = CONST 
    0x37: SSTORE v35(0xa), v29(0x0)
    0x38: v38(0x2) = CONST 
    0x3b: v3b = SLOAD v38(0x2)
    0x3c: v3c(0x1) = CONST 
    0x3e: v3e(0xa0) = CONST 
    0x40: v40(0x2) = CONST 
    0x42: v42(0x10000000000000000000000000000000000000000) = EXP v40(0x2), v3e(0xa0)
    0x43: v43(0xffffffffffffffffffffffffffffffffffffffff) = SUB v42(0x10000000000000000000000000000000000000000), v3c(0x1)
    0x44: v44 = CALLER 
    0x46: v46 = AND v43(0xffffffffffffffffffffffffffffffffffffffff), v44
    0x47: v47(0x1) = CONST 
    0x49: v49(0xa0) = CONST 
    0x4b: v4b(0x2) = CONST 
    0x4d: v4d(0x10000000000000000000000000000000000000000) = EXP v4b(0x2), v49(0xa0)
    0x4e: v4e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d(0x10000000000000000000000000000000000000000), v47(0x1)
    0x4f: v4f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4e(0xffffffffffffffffffffffffffffffffffffffff)
    0x52: v52 = AND v4f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3b
    0x53: v53 = OR v52, v46
    0x56: SSTORE v38(0x2), v53
    0x57: v57(0x3) = CONST 
    0x5a: v5a = SLOAD v57(0x3)
    0x5e: v5e = AND v22, v43(0xffffffffffffffffffffffffffffffffffffffff)
    0x60: v60 = AND v5a, v4f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x61: v61 = OR v60, v5e
    0x63: SSTORE v57(0x3), v61
    0x66: v66(0x16f0) = CONST 
    0x6a: v6a(0x74) = CONST 
    0x6d: v6d(0x0) = CONST 
    0x6f: CODECOPY v6d(0x0), v6a(0x74), v66(0x16f0)
    0x70: v70(0x0) = CONST 
    0x72: RETURN v70(0x0), v66(0x16f0)
    0x1787: v1787(0x00000000000000000000000070250fcfef983c9b912c8eefb7021b4b7bae836e) = CONST 

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xb: vb(0x0) = CONST 
    0xe: REVERT vb(0x0), vb(0x0)

}

