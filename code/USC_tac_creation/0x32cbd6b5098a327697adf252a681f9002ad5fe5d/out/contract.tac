function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x66]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x17) = CONST 
    0xa: va(0x1) = CONST 
    0xc: vc(0x1) = CONST 
    0xe: ve(0xe0) = CONST 
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = SHL ve(0xe0), vc(0x1)
    0x11: v11(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v10(0x100000000000000000000000000000000000000000000000000000000), va(0x1)
    0x12: v12(0x66) = CONST 
    0x15: v15(0x66) = AND v12(0x66), v11(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x16: JUMP v15(0x66)

    Begin block 0x66
    prev=[0x0], succ=[0x17]
    =================================
    0x67: v67 = CALLER 
    0x69: JUMP v7(0x17)

    Begin block 0x17
    prev=[0x66], succ=[0x6a]
    =================================
    0x18: v18(0x0) = CONST 
    0x1b: v1b = SLOAD v18(0x0)
    0x1c: v1c(0x1) = CONST 
    0x1e: v1e(0x1) = CONST 
    0x20: v20(0xa0) = CONST 
    0x22: v22(0x10000000000000000000000000000000000000000) = SHL v20(0xa0), v1e(0x1)
    0x23: v23(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22(0x10000000000000000000000000000000000000000), v1c(0x1)
    0x24: v24(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v23(0xffffffffffffffffffffffffffffffffffffffff)
    0x25: v25 = AND v24(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1b
    0x26: v26(0x1) = CONST 
    0x28: v28(0x1) = CONST 
    0x2a: v2a(0xa0) = CONST 
    0x2c: v2c(0x10000000000000000000000000000000000000000) = SHL v2a(0xa0), v28(0x1)
    0x2d: v2d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c(0x10000000000000000000000000000000000000000), v26(0x1)
    0x2f: v2f = AND v67, v2d(0xffffffffffffffffffffffffffffffffffffffff)
    0x32: v32 = OR v2f, v25
    0x34: SSTORE v18(0x0), v32
    0x35: v35(0x40) = CONST 
    0x37: v37 = MLOAD v35(0x40)
    0x3c: v3c(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x60: LOG3 v37, v18(0x0), v3c(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v18(0x0), v2f
    0x62: v62(0x6a) = CONST 
    0x65: JUMP v62(0x6a)

    Begin block 0x6a
    prev=[0x17], succ=[]
    =================================
    0x6b: v6b(0x12d9) = CONST 
    0x6f: v6f(0x79) = CONST 
    0x72: v72(0x0) = CONST 
    0x74: CODECOPY v72(0x0), v6f(0x79), v6b(0x12d9)
    0x75: v75(0x0) = CONST 
    0x77: RETURN v75(0x0), v6b(0x12d9)

}

