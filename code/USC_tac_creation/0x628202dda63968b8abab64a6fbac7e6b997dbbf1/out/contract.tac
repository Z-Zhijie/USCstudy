function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x66]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x15) = CONST 
    0x8: v8(0x1) = CONST 
    0xa: va(0x1) = CONST 
    0xc: vc(0xe0) = CONST 
    0xe: ve(0x100000000000000000000000000000000000000000000000000000000) = SHL vc(0xe0), va(0x1)
    0xf: vf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB ve(0x100000000000000000000000000000000000000000000000000000000), v8(0x1)
    0x10: v10(0x66) = CONST 
    0x13: v13(0x66) = AND v10(0x66), vf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x14: JUMP v13(0x66)

    Begin block 0x66
    prev=[0x0], succ=[0x15]
    =================================
    0x67: v67 = CALLER 
    0x69: JUMP v5(0x15)

    Begin block 0x15
    prev=[0x66], succ=[0x6a]
    =================================
    0x16: v16(0x33) = CONST 
    0x19: v19 = SLOAD v16(0x33)
    0x1a: v1a(0x1) = CONST 
    0x1c: v1c(0x1) = CONST 
    0x1e: v1e(0xa0) = CONST 
    0x20: v20(0x10000000000000000000000000000000000000000) = SHL v1e(0xa0), v1c(0x1)
    0x21: v21(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20(0x10000000000000000000000000000000000000000), v1a(0x1)
    0x22: v22(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v21(0xffffffffffffffffffffffffffffffffffffffff)
    0x23: v23 = AND v22(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v19
    0x24: v24(0x1) = CONST 
    0x26: v26(0x1) = CONST 
    0x28: v28(0xa0) = CONST 
    0x2a: v2a(0x10000000000000000000000000000000000000000) = SHL v28(0xa0), v26(0x1)
    0x2b: v2b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a(0x10000000000000000000000000000000000000000), v24(0x1)
    0x2e: v2e = AND v2b(0xffffffffffffffffffffffffffffffffffffffff), v67
    0x2f: v2f = OR v2e, v23
    0x33: SSTORE v16(0x33), v2f
    0x34: v34(0x40) = CONST 
    0x36: v36 = MLOAD v34(0x40)
    0x38: v38 = AND v2b(0xffffffffffffffffffffffffffffffffffffffff), v2f
    0x3a: v3a(0x0) = CONST 
    0x3d: v3d(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x61: LOG3 v36, v3a(0x0), v3d(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v3a(0x0), v38
    0x62: v62(0x6a) = CONST 
    0x65: JUMP v62(0x6a)

    Begin block 0x6a
    prev=[0x15], succ=[]
    =================================
    0x6b: v6b(0x1788) = CONST 
    0x6f: v6f(0x79) = CONST 
    0x72: v72(0x0) = CONST 
    0x74: CODECOPY v72(0x0), v6f(0x79), v6b(0x1788)
    0x75: v75(0x0) = CONST 
    0x77: RETURN v75(0x0), v6b(0x1788)

}

