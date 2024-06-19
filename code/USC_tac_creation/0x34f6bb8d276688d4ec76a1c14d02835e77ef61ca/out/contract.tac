function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x42, 0x46]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x3) = CONST 
    0x9: v9(0x14) = CONST 
    0xb: vb(0x100) = CONST 
    0xe: ve(0x10000000000000000000000000000000000000000) = EXP vb(0x100), v9(0x14)
    0x10: v10 = SLOAD v7(0x3)
    0x12: v12(0xff) = CONST 
    0x14: v14(0xff0000000000000000000000000000000000000000) = MUL v12(0xff), ve(0x10000000000000000000000000000000000000000)
    0x15: v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v14(0xff0000000000000000000000000000000000000000)
    0x16: v16 = AND v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v10
    0x19: v19(0x1) = ISZERO v5(0x0)
    0x1a: v1a(0x0) = ISZERO v19(0x1)
    0x1b: v1b(0x0) = MUL v1a(0x0), ve(0x10000000000000000000000000000000000000000)
    0x1c: v1c = OR v1b(0x0), v16
    0x1e: SSTORE v7(0x3), v1c
    0x20: v20(0x0) = CONST 
    0x22: v22(0x3) = CONST 
    0x24: v24(0x15) = CONST 
    0x26: v26(0x100) = CONST 
    0x29: v29(0x1000000000000000000000000000000000000000000) = EXP v26(0x100), v24(0x15)
    0x2b: v2b = SLOAD v22(0x3)
    0x2d: v2d(0xff) = CONST 
    0x2f: v2f(0xff000000000000000000000000000000000000000000) = MUL v2d(0xff), v29(0x1000000000000000000000000000000000000000000)
    0x30: v30(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v2f(0xff000000000000000000000000000000000000000000)
    0x31: v31 = AND v30(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v2b
    0x34: v34(0x1) = ISZERO v20(0x0)
    0x35: v35(0x0) = ISZERO v34(0x1)
    0x36: v36(0x0) = MUL v35(0x0), v29(0x1000000000000000000000000000000000000000000)
    0x37: v37 = OR v36(0x0), v31
    0x39: SSTORE v22(0x3), v37
    0x3b: v3b = CALLVALUE 
    0x3d: v3d = ISZERO v3b
    0x3e: v3e(0x46) = CONST 
    0x41: JUMPI v3e(0x46), v3d

    Begin block 0x42
    prev=[0x0], succ=[]
    =================================
    0x42: v42(0x0) = CONST 
    0x45: REVERT v42(0x0), v42(0x0)

    Begin block 0x46
    prev=[0x0], succ=[]
    =================================
    0x48: v48 = CALLER 
    0x49: v49(0x3) = CONST 
    0x4b: v4b(0x0) = CONST 
    0x4d: v4d(0x100) = CONST 
    0x50: v50(0x1) = EXP v4d(0x100), v4b(0x0)
    0x52: v52 = SLOAD v49(0x3)
    0x54: v54(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x69: v69(0xffffffffffffffffffffffffffffffffffffffff) = MUL v54(0xffffffffffffffffffffffffffffffffffffffff), v50(0x1)
    0x6a: v6a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v69(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b: v6b = AND v6a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v52
    0x6e: v6e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x83: v83 = AND v6e(0xffffffffffffffffffffffffffffffffffffffff), v48
    0x84: v84 = MUL v83, v50(0x1)
    0x85: v85 = OR v84, v6b
    0x87: SSTORE v49(0x3), v85
    0x89: v89(0x5e8e) = CONST 
    0x8d: v8d(0x98) = CONST 
    0x91: v91(0x0) = CONST 
    0x93: CODECOPY v91(0x0), v8d(0x98), v89(0x5e8e)
    0x94: v94(0x0) = CONST 
    0x96: RETURN v94(0x0), v89(0x5e8e)

}

