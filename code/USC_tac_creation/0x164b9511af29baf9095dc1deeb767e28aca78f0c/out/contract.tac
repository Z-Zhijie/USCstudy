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
    0x12: v12 = CALLER 
    0x13: v13(0x1) = CONST 
    0x15: v15(0x0) = CONST 
    0x17: v17(0x100) = CONST 
    0x1a: v1a(0x1) = EXP v17(0x100), v15(0x0)
    0x1c: v1c = SLOAD v13(0x1)
    0x1e: v1e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33: v33(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1e(0xffffffffffffffffffffffffffffffffffffffff), v1a(0x1)
    0x34: v34(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v33(0xffffffffffffffffffffffffffffffffffffffff)
    0x35: v35 = AND v34(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1c
    0x38: v38(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4d: v4d = AND v38(0xffffffffffffffffffffffffffffffffffffffff), v12
    0x4e: v4e = MUL v4d, v1a(0x1)
    0x4f: v4f = OR v4e, v35
    0x51: SSTORE v13(0x1), v4f
    0x53: v53(0x5dae) = CONST 
    0x57: v57(0x62) = CONST 
    0x5b: v5b(0x0) = CONST 
    0x5d: CODECOPY v5b(0x0), v57(0x62), v53(0x5dae)
    0x5e: v5e(0x0) = CONST 
    0x60: RETURN v5e(0x0), v53(0x5dae)

}

