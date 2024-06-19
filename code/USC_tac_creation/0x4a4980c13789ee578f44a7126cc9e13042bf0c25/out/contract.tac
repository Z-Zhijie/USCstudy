function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x16, 0x1a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9(0xff)
    0xc: vc = AND vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8
    0xe: SSTORE v5(0x0), vc
    0xf: vf = CALLVALUE 
    0x11: v11 = ISZERO vf
    0x12: v12(0x1a) = CONST 
    0x15: JUMPI v12(0x1a), v11

    Begin block 0x16
    prev=[0x0], succ=[]
    =================================
    0x16: v16(0x0) = CONST 
    0x19: REVERT v16(0x0), v16(0x0)

    Begin block 0x1a
    prev=[0x0], succ=[]
    =================================
    0x1c: v1c(0x383c) = CONST 
    0x20: v20(0x2a) = CONST 
    0x23: v23(0x0) = CONST 
    0x25: CODECOPY v23(0x0), v20(0x2a), v1c(0x383c)
    0x26: v26(0x0) = CONST 
    0x28: RETURN v26(0x0), v1c(0x383c)

}

