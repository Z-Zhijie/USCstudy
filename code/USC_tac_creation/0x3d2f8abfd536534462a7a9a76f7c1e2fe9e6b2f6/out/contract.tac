function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1e, 0x22]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x8: v8 = SLOAD v5(0x1)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x1), vf
    0x12: v12(0x0) = CONST 
    0x14: v14(0xb) = CONST 
    0x16: SSTORE v14(0xb), v12(0x0)
    0x17: v17 = CALLVALUE 
    0x19: v19 = ISZERO v17
    0x1a: v1a(0x22) = CONST 
    0x1d: JUMPI v1a(0x22), v19

    Begin block 0x1e
    prev=[0x0], succ=[]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x21: REVERT v1e(0x0), v1e(0x0)

    Begin block 0x22
    prev=[0x0], succ=[0x31]
    =================================
    0x24: v24(0x2c) = CONST 
    0x27: v27 = CALLER 
    0x28: v28(0x31) = CONST 
    0x2b: JUMP v28(0x31)

    Begin block 0x31
    prev=[0x22], succ=[0x2c]
    =================================
    0x32: v32(0x0) = CONST 
    0x35: v35 = SLOAD v32(0x0)
    0x36: v36(0x1) = CONST 
    0x38: v38(0x1) = CONST 
    0x3a: v3a(0xa0) = CONST 
    0x3c: v3c(0x10000000000000000000000000000000000000000) = SHL v3a(0xa0), v38(0x1)
    0x3d: v3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c(0x10000000000000000000000000000000000000000), v36(0x1)
    0x3e: v3e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f: v3f = AND v3e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v35
    0x40: v40(0x1) = CONST 
    0x42: v42(0x1) = CONST 
    0x44: v44(0xa0) = CONST 
    0x46: v46(0x10000000000000000000000000000000000000000) = SHL v44(0xa0), v42(0x1)
    0x47: v47(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46(0x10000000000000000000000000000000000000000), v40(0x1)
    0x4b: v4b = AND v47(0xffffffffffffffffffffffffffffffffffffffff), v27
    0x4f: v4f = OR v4b, v3f
    0x51: SSTORE v32(0x0), v4f
    0x52: JUMP v24(0x2c)

    Begin block 0x2c
    prev=[0x31], succ=[0x53]
    =================================
    0x2d: v2d(0x53) = CONST 
    0x30: JUMP v2d(0x53)

    Begin block 0x53
    prev=[0x2c], succ=[]
    =================================
    0x54: v54(0x314a) = CONST 
    0x58: v58(0x63) = CONST 
    0x5c: v5c(0x0) = CONST 
    0x5e: CODECOPY v5c(0x0), v58(0x63), v54(0x314a)
    0x5f: v5f(0x0) = CONST 
    0x61: RETURN v5f(0x0), v54(0x314a)

}

