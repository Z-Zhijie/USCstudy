function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x19, 0x1d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x8: v8 = SLOAD v5(0x4)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x4), vf
    0x12: v12 = CALLVALUE 
    0x14: v14 = ISZERO v12
    0x15: v15(0x1d) = CONST 
    0x18: JUMPI v15(0x1d), v14

    Begin block 0x19
    prev=[0x0], succ=[]
    =================================
    0x19: v19(0x0) = CONST 
    0x1c: REVERT v19(0x0), v19(0x0)

    Begin block 0x1d
    prev=[0x0], succ=[]
    =================================
    0x1f: v1f(0x264a) = CONST 
    0x23: v23(0x2d) = CONST 
    0x26: v26(0x0) = CONST 
    0x28: CODECOPY v26(0x0), v23(0x2d), v1f(0x264a)
    0x29: v29(0x0) = CONST 
    0x2b: RETURN v29(0x0), v1f(0x264a)

}

