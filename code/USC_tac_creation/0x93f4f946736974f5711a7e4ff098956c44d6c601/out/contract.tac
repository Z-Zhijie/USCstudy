function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x11, 0x15]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x7: v7(0x2) = CONST 
    0x9: SSTORE v7(0x2), v5(0x1)
    0xa: va = CALLVALUE 
    0xc: vc = ISZERO va
    0xd: vd(0x15) = CONST 
    0x10: JUMPI vd(0x15), vc

    Begin block 0x11
    prev=[0x0], succ=[]
    =================================
    0x11: v11(0x0) = CONST 
    0x14: REVERT v11(0x0), v11(0x0)

    Begin block 0x15
    prev=[0x0], succ=[0x73]
    =================================
    0x17: v17(0x0) = CONST 
    0x19: v19(0x20) = CONST 
    0x1c: v1c(0x73) = CONST 
    0x1f: JUMP v1c(0x73)

    Begin block 0x73
    prev=[0x15], succ=[0x20]
    =================================
    0x74: v74 = CALLER 
    0x76: JUMP v19(0x20)

    Begin block 0x20
    prev=[0x73], succ=[0x77]
    =================================
    0x21: v21(0x0) = CONST 
    0x24: v24 = SLOAD v21(0x0)
    0x25: v25(0x1) = CONST 
    0x27: v27(0x1) = CONST 
    0x29: v29(0xa0) = CONST 
    0x2b: v2b(0x10000000000000000000000000000000000000000) = SHL v29(0xa0), v27(0x1)
    0x2c: v2c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b(0x10000000000000000000000000000000000000000), v25(0x1)
    0x2d: v2d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2c(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e: v2e = AND v2d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v24
    0x2f: v2f(0x1) = CONST 
    0x31: v31(0x1) = CONST 
    0x33: v33(0xa0) = CONST 
    0x35: v35(0x10000000000000000000000000000000000000000) = SHL v33(0xa0), v31(0x1)
    0x36: v36(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35(0x10000000000000000000000000000000000000000), v2f(0x1)
    0x38: v38 = AND v74, v36(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b: v3b = OR v38, v2e
    0x3d: SSTORE v21(0x0), v3b
    0x3e: v3e(0x40) = CONST 
    0x40: v40 = MLOAD v3e(0x40)
    0x45: v45(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x69: LOG3 v40, v21(0x0), v45(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v21(0x0), v38
    0x6b: v6b(0x1) = CONST 
    0x6e: SSTORE v6b(0x1), v6b(0x1)
    0x6f: v6f(0x77) = CONST 
    0x72: JUMP v6f(0x77)

    Begin block 0x77
    prev=[0x20], succ=[]
    =================================
    0x78: v78(0x27c7) = CONST 
    0x7c: v7c(0x86) = CONST 
    0x7f: v7f(0x0) = CONST 
    0x81: CODECOPY v7f(0x0), v7c(0x86), v78(0x27c7)
    0x82: v82(0x0) = CONST 
    0x84: RETURN v82(0x0), v78(0x27c7)

}

