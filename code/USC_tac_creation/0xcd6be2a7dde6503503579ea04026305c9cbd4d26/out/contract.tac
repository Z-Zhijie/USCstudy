function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x21]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1c) = CONST 
    0x8: v8 = CALLER 
    0x9: v9(0x21) = CONST 
    0xc: vc(0x100000000) = CONST 
    0x12: v12(0x2100000000) = MUL vc(0x100000000), v9(0x21)
    0x13: v13(0x100000000) = CONST 
    0x1a: v1a(0x21) = DIV v12(0x2100000000), v13(0x100000000)
    0x1b: JUMP v1a(0x21)

    Begin block 0x21
    prev=[0x0], succ=[0x1c]
    =================================
    0x23: v23(0x6) = CONST 
    0x25: v25(0x0) = CONST 
    0x27: v27(0x100) = CONST 
    0x2a: v2a(0x1) = EXP v27(0x100), v25(0x0)
    0x2c: v2c = SLOAD v23(0x6)
    0x2e: v2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x43: v43(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2e(0xffffffffffffffffffffffffffffffffffffffff), v2a(0x1)
    0x44: v44(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v43(0xffffffffffffffffffffffffffffffffffffffff)
    0x45: v45 = AND v44(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2c
    0x48: v48(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5d: v5d = AND v48(0xffffffffffffffffffffffffffffffffffffffff), v8
    0x5e: v5e = MUL v5d, v2a(0x1)
    0x5f: v5f = OR v5e, v45
    0x61: SSTORE v23(0x6), v5f
    0x64: JUMP v5(0x1c)

    Begin block 0x1c
    prev=[0x21], succ=[0x65]
    =================================
    0x1d: v1d(0x65) = CONST 
    0x20: JUMP v1d(0x65)

    Begin block 0x65
    prev=[0x1c], succ=[]
    =================================
    0x66: v66(0x6b9) = CONST 
    0x6a: v6a(0x74) = CONST 
    0x6d: v6d(0x0) = CONST 
    0x6f: CODECOPY v6d(0x0), v6a(0x74), v66(0x6b9)
    0x70: v70(0x0) = CONST 
    0x72: RETURN v70(0x0), v66(0x6b9)

}

