function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x9d) = CONST 
    0x8: v8 = SLOAD v5(0x9d)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa8) = CONST 
    0xf: vf(0x1000000000000000000000000000000000000000000) = SHL vd(0xa8), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x1000000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffff000000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffff000000000000000000000000000000000000000000), v8
    0x13: v13(0x100) = CONST 
    0x16: v16 = CALLER 
    0x17: v17 = MUL v16, v13(0x100)
    0x18: v18 = OR v17, v12
    0x1a: SSTORE v5(0x9d), v18
    0x1b: v1b(0x30f4) = CONST 
    0x1f: v1f(0x29) = CONST 
    0x22: v22(0x0) = CONST 
    0x24: CODECOPY v22(0x0), v1f(0x29), v1b(0x30f4)
    0x25: v25(0x0) = CONST 
    0x27: RETURN v25(0x0), v1b(0x30f4)

}

