function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[0x6a]
    =================================
    0x12: v12(0x0) = CONST 
    0x14: v14(0x1b) = CONST 
    0x17: v17(0x6a) = CONST 
    0x1a: JUMP v17(0x6a)

    Begin block 0x6a
    prev=[0x10], succ=[0x1b]
    =================================
    0x6b: v6b = CALLER 
    0x6d: JUMP v14(0x1b)

    Begin block 0x1b
    prev=[0x6a], succ=[0x6e]
    =================================
    0x1c: v1c(0x0) = CONST 
    0x1f: v1f = SLOAD v1c(0x0)
    0x20: v20(0x1) = CONST 
    0x22: v22(0x1) = CONST 
    0x24: v24(0xa0) = CONST 
    0x26: v26(0x10000000000000000000000000000000000000000) = SHL v24(0xa0), v22(0x1)
    0x27: v27(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26(0x10000000000000000000000000000000000000000), v20(0x1)
    0x28: v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27(0xffffffffffffffffffffffffffffffffffffffff)
    0x29: v29 = AND v28(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f
    0x2a: v2a(0x1) = CONST 
    0x2c: v2c(0x1) = CONST 
    0x2e: v2e(0xa0) = CONST 
    0x30: v30(0x10000000000000000000000000000000000000000) = SHL v2e(0xa0), v2c(0x1)
    0x31: v31(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30(0x10000000000000000000000000000000000000000), v2a(0x1)
    0x33: v33 = AND v6b, v31(0xffffffffffffffffffffffffffffffffffffffff)
    0x36: v36 = OR v33, v29
    0x38: SSTORE v1c(0x0), v36
    0x39: v39(0x40) = CONST 
    0x3b: v3b = MLOAD v39(0x40)
    0x40: v40(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x64: LOG3 v3b, v1c(0x0), v40(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1c(0x0), v33
    0x66: v66(0x6e) = CONST 
    0x69: JUMP v66(0x6e)

    Begin block 0x6e
    prev=[0x1b], succ=[]
    =================================
    0x6f: v6f(0x27d8) = CONST 
    0x73: v73(0x7d) = CONST 
    0x76: v76(0x0) = CONST 
    0x78: CODECOPY v76(0x0), v73(0x7d), v6f(0x27d8)
    0x79: v79(0x0) = CONST 
    0x7b: RETURN v79(0x0), v6f(0x27d8)

}

