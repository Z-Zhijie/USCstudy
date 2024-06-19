function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x3f) = CONST 
    0x8: v8 = SLOAD v5(0x3f)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x3f), vf
    0x12: v12(0x41a8) = CONST 
    0x16: v16(0x20) = CONST 
    0x19: v19(0x0) = CONST 
    0x1b: CODECOPY v19(0x0), v16(0x20), v12(0x41a8)
    0x1c: v1c(0x0) = CONST 
    0x1e: RETURN v1c(0x0), v12(0x41a8)

}

