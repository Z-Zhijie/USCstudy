function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x2d, 0x31]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x1) = CONST 
    0x9: v9(0x14) = CONST 
    0xb: vb(0x100) = CONST 
    0xe: ve(0x10000000000000000000000000000000000000000) = EXP vb(0x100), v9(0x14)
    0x10: v10 = SLOAD v7(0x1)
    0x12: v12(0xff) = CONST 
    0x14: v14(0xff0000000000000000000000000000000000000000) = MUL v12(0xff), ve(0x10000000000000000000000000000000000000000)
    0x15: v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v14(0xff0000000000000000000000000000000000000000)
    0x16: v16 = AND v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v10
    0x19: v19(0x1) = ISZERO v5(0x0)
    0x1a: v1a(0x0) = ISZERO v19(0x1)
    0x1b: v1b(0x0) = MUL v1a(0x0), ve(0x10000000000000000000000000000000000000000)
    0x1c: v1c = OR v1b(0x0), v16
    0x1e: SSTORE v7(0x1), v1c
    0x20: v20(0x0) = CONST 
    0x22: v22(0xb) = CONST 
    0x24: SSTORE v22(0xb), v20(0x0)
    0x25: v25 = CALLVALUE 
    0x27: v27 = ISZERO v25
    0x28: v28(0x31) = CONST 
    0x2c: JUMPI v28(0x31), v27

    Begin block 0x2d
    prev=[0x0], succ=[]
    =================================
    0x2d: v2d(0x0) = CONST 
    0x30: REVERT v2d(0x0), v2d(0x0)

    Begin block 0x31
    prev=[0x0], succ=[0x49]
    =================================
    0x33: v33(0x43) = CONST 
    0x37: v37 = CALLER 
    0x38: v38(0x49) = CONST 
    0x3c: v3c(0x20) = CONST 
    0x3e: v3e(0x4900000000) = SHL v3c(0x20), v38(0x49)
    0x3f: v3f(0x20) = CONST 
    0x41: v41(0x49) = SHR v3f(0x20), v3e(0x4900000000)
    0x42: JUMP v41(0x49)

    Begin block 0x49
    prev=[0x31], succ=[0x43]
    =================================
    0x4b: v4b(0x0) = CONST 
    0x4e: v4e(0x100) = CONST 
    0x51: v51(0x1) = EXP v4e(0x100), v4b(0x0)
    0x53: v53 = SLOAD v4b(0x0)
    0x55: v55(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a: v6a(0xffffffffffffffffffffffffffffffffffffffff) = MUL v55(0xffffffffffffffffffffffffffffffffffffffff), v51(0x1)
    0x6b: v6b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6a(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c: v6c = AND v6b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v53
    0x6f: v6f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x84: v84 = AND v6f(0xffffffffffffffffffffffffffffffffffffffff), v37
    0x85: v85 = MUL v84, v51(0x1)
    0x86: v86 = OR v85, v6c
    0x88: SSTORE v4b(0x0), v86
    0x8b: JUMP v33(0x43)

    Begin block 0x43
    prev=[0x49], succ=[0x8c]
    =================================
    0x44: v44(0x8c) = CONST 
    0x48: JUMP v44(0x8c)

    Begin block 0x8c
    prev=[0x43], succ=[]
    =================================
    0x8d: v8d(0x4af9) = CONST 
    0x91: v91(0x9c) = CONST 
    0x95: v95(0x0) = CONST 
    0x97: CODECOPY v95(0x0), v91(0x9c), v8d(0x4af9)
    0x98: v98(0x0) = CONST 
    0x9a: RETURN v98(0x0), v8d(0x4af9)

}

