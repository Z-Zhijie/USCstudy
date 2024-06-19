function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x26, 0x2a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x5) = CONST 
    0x8: v8 = SLOAD v5(0x5)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9(0xff)
    0xc: vc = AND vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8
    0xe: SSTORE v5(0x5), vc
    0xf: vf(0x0) = CONST 
    0x11: v11(0x6) = CONST 
    0x15: SSTORE v11(0x6), vf(0x0)
    0x16: v16(0x7) = CONST 
    0x18: SSTORE v16(0x7), vf(0x0)
    0x19: v19(0x3e8) = CONST 
    0x1c: v1c(0x15) = CONST 
    0x1e: SSTORE v1c(0x15), v19(0x3e8)
    0x1f: v1f = CALLVALUE 
    0x21: v21 = ISZERO v1f
    0x22: v22(0x2a) = CONST 
    0x25: JUMPI v22(0x2a), v21

    Begin block 0x26
    prev=[0x0], succ=[]
    =================================
    0x26: v26(0x0) = CONST 
    0x29: REVERT v26(0x0), v26(0x0)

    Begin block 0x2a
    prev=[0x0], succ=[]
    =================================
    0x2c: v2c(0x0) = CONST 
    0x2f: v2f = SLOAD v2c(0x0)
    0x30: v30(0x1) = CONST 
    0x32: v32(0x1) = CONST 
    0x34: v34(0xa0) = CONST 
    0x36: v36(0x10000000000000000000000000000000000000000) = SHL v34(0xa0), v32(0x1)
    0x37: v37(0xffffffffffffffffffffffffffffffffffffffff) = SUB v36(0x10000000000000000000000000000000000000000), v30(0x1)
    0x38: v38(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v37(0xffffffffffffffffffffffffffffffffffffffff)
    0x39: v39 = AND v38(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2f
    0x3a: v3a = CALLER 
    0x3b: v3b = OR v3a, v39
    0x3e: SSTORE v2c(0x0), v3b
    0x3f: v3f(0x40) = CONST 
    0x41: v41 = MLOAD v3f(0x40)
    0x42: v42(0x1) = CONST 
    0x44: v44(0x1) = CONST 
    0x46: v46(0xa0) = CONST 
    0x48: v48(0x10000000000000000000000000000000000000000) = SHL v46(0xa0), v44(0x1)
    0x49: v49(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48(0x10000000000000000000000000000000000000000), v42(0x1)
    0x4d: v4d = AND v49(0xffffffffffffffffffffffffffffffffffffffff), v3b
    0x50: v50(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x74: LOG3 v41, v2c(0x0), v50(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v2c(0x0), v4d
    0x75: v75(0x2314) = CONST 
    0x79: v79(0x83) = CONST 
    0x7c: v7c(0x0) = CONST 
    0x7e: CODECOPY v7c(0x0), v79(0x83), v75(0x2314)
    0x7f: v7f(0x0) = CONST 
    0x81: RETURN v7f(0x0), v75(0x2314)

}

