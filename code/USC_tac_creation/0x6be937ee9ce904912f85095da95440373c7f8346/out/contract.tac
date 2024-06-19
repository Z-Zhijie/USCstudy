function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x13, 0x17]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x151800) = CONST 
    0x9: v9(0x1) = CONST 
    0xb: SSTORE v9(0x1), v5(0x151800)
    0xc: vc = CALLVALUE 
    0xe: ve = ISZERO vc
    0xf: vf(0x17) = CONST 
    0x12: JUMPI vf(0x17), ve

    Begin block 0x13
    prev=[0x0], succ=[]
    =================================
    0x13: v13(0x0) = CONST 
    0x16: REVERT v13(0x0), v13(0x0)

    Begin block 0x17
    prev=[0x0], succ=[]
    =================================
    0x19: v19(0x0) = CONST 
    0x1c: v1c = SLOAD v19(0x0)
    0x1d: v1d(0x1) = CONST 
    0x1f: v1f(0x1) = CONST 
    0x21: v21(0xa0) = CONST 
    0x23: v23(0x10000000000000000000000000000000000000000) = SHL v21(0xa0), v1f(0x1)
    0x24: v24(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23(0x10000000000000000000000000000000000000000), v1d(0x1)
    0x25: v25(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v24(0xffffffffffffffffffffffffffffffffffffffff)
    0x26: v26 = AND v25(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1c
    0x27: v27 = CALLER 
    0x2a: v2a = OR v27, v26
    0x2c: SSTORE v19(0x0), v2a
    0x2d: v2d(0x40) = CONST 
    0x2f: v2f = MLOAD v2d(0x40)
    0x33: v33(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x57: LOG3 v2f, v19(0x0), v33(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v19(0x0), v27
    0x58: v58(0x2040) = CONST 
    0x5c: v5c(0x66) = CONST 
    0x5f: v5f(0x0) = CONST 
    0x61: CODECOPY v5f(0x0), v5c(0x66), v58(0x2040)
    0x62: v62(0x0) = CONST 
    0x64: RETURN v62(0x0), v58(0x2040)

}

