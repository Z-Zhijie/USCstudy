function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1b]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x16) = CONST 
    0x8: v8 = CALLER 
    0x9: v9(0x100000000) = CONST 
    0xf: vf(0x1b) = CONST 
    0x13: v13(0x1b00000000) = MUL v9(0x100000000), vf(0x1b)
    0x14: v14(0x1b) = DIV v13(0x1b00000000), v9(0x100000000)
    0x15: JUMP v14(0x1b)

    Begin block 0x1b
    prev=[0x0], succ=[0x16]
    =================================
    0x1c: v1c(0x6) = CONST 
    0x1f: v1f = SLOAD v1c(0x6)
    0x20: v20(0x1) = CONST 
    0x22: v22(0xa0) = CONST 
    0x24: v24(0x2) = CONST 
    0x26: v26(0x10000000000000000000000000000000000000000) = EXP v24(0x2), v22(0xa0)
    0x27: v27(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26(0x10000000000000000000000000000000000000000), v20(0x1)
    0x28: v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27(0xffffffffffffffffffffffffffffffffffffffff)
    0x29: v29 = AND v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f
    0x2a: v2a(0x1) = CONST 
    0x2c: v2c(0xa0) = CONST 
    0x2e: v2e(0x2) = CONST 
    0x30: v30(0x10000000000000000000000000000000000000000) = EXP v2e(0x2), v2c(0xa0)
    0x31: v31(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30(0x10000000000000000000000000000000000000000), v2a(0x1)
    0x35: v35 = AND v31(0xffffffffffffffffffffffffffffffffffffffff), v8
    0x39: v39 = OR v35, v29
    0x3b: SSTORE v1c(0x6), v39
    0x3c: JUMP v5(0x16)

    Begin block 0x16
    prev=[0x1b], succ=[0x3d]
    =================================
    0x17: v17(0x3d) = CONST 
    0x1a: JUMP v17(0x3d)

    Begin block 0x3d
    prev=[0x16], succ=[]
    =================================
    0x3e: v3e(0x3ad) = CONST 
    0x42: v42(0x4c) = CONST 
    0x45: v45(0x0) = CONST 
    0x47: CODECOPY v45(0x0), v42(0x4c), v3e(0x3ad)
    0x48: v48(0x0) = CONST 
    0x4a: RETURN v48(0x0), v3e(0x3ad)

}

