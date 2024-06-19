function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLER 
    0x6: v6(0x0) = CONST 
    0x9: v9(0x100) = CONST 
    0xc: vc(0x1) = EXP v9(0x100), v6(0x0)
    0xe: ve = SLOAD v6(0x0)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25: v25(0xffffffffffffffffffffffffffffffffffffffff) = MUL v10(0xffffffffffffffffffffffffffffffffffffffff), vc(0x1)
    0x26: v26(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v25(0xffffffffffffffffffffffffffffffffffffffff)
    0x27: v27 = AND v26(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), ve
    0x2a: v2a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3f: v3f = AND v2a(0xffffffffffffffffffffffffffffffffffffffff), v5
    0x40: v40 = MUL v3f, vc(0x1)
    0x41: v41 = OR v40, v27
    0x43: SSTORE v6(0x0), v41
    0x45: v45(0x67b) = CONST 
    0x49: v49(0x53) = CONST 
    0x4c: v4c(0x0) = CONST 
    0x4e: CODECOPY v4c(0x0), v49(0x53), v45(0x67b)
    0x4f: v4f(0x0) = CONST 
    0x51: RETURN v4f(0x0), v45(0x67b)

}

