function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1e, 0x22]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x13) = CONST 
    0x9: SSTORE v7(0x13), v5(0x0)
    0xa: va(0x9105dba22ed50000) = CONST 
    0x13: v13(0x14) = CONST 
    0x15: SSTORE v13(0x14), va(0x9105dba22ed50000)
    0x16: v16 = CALLVALUE 
    0x18: v18 = ISZERO v16
    0x19: v19(0x22) = CONST 
    0x1d: JUMPI v19(0x22), v18

    Begin block 0x1e
    prev=[0x0], succ=[]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x21: REVERT v1e(0x0), v1e(0x0)

    Begin block 0x22
    prev=[0x0], succ=[0x83]
    =================================
    0x24: v24(0x0) = CONST 
    0x26: v26(0x2f) = CONST 
    0x2a: v2a(0x83) = CONST 
    0x2e: JUMP v2a(0x83)

    Begin block 0x83
    prev=[0x22], succ=[0x2f]
    =================================
    0x84: v84 = CALLER 
    0x86: JUMP v26(0x2f)

    Begin block 0x2f
    prev=[0x83], succ=[0x87]
    =================================
    0x30: v30(0x1) = CONST 
    0x33: v33 = SLOAD v30(0x1)
    0x34: v34(0x1) = CONST 
    0x36: v36(0x1) = CONST 
    0x38: v38(0xa0) = CONST 
    0x3a: v3a(0x10000000000000000000000000000000000000000) = SHL v38(0xa0), v36(0x1)
    0x3b: v3b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a(0x10000000000000000000000000000000000000000), v34(0x1)
    0x3c: v3c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3b(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d: v3d = AND v3c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v33
    0x3e: v3e(0x1) = CONST 
    0x40: v40(0x1) = CONST 
    0x42: v42(0xa0) = CONST 
    0x44: v44(0x10000000000000000000000000000000000000000) = SHL v42(0xa0), v40(0x1)
    0x45: v45(0xffffffffffffffffffffffffffffffffffffffff) = SUB v44(0x10000000000000000000000000000000000000000), v3e(0x1)
    0x47: v47 = AND v84, v45(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a: v4a = OR v47, v3d
    0x4d: SSTORE v30(0x1), v4a
    0x4e: v4e(0x40) = CONST 
    0x50: v50 = MLOAD v4e(0x40)
    0x55: v55(0x0) = CONST 
    0x58: v58(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x7c: LOG3 v50, v55(0x0), v58(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v55(0x0), v47
    0x7e: v7e(0x87) = CONST 
    0x82: JUMP v7e(0x87)

    Begin block 0x87
    prev=[0x2f], succ=[]
    =================================
    0x88: v88(0x3dae) = CONST 
    0x8c: v8c(0x97) = CONST 
    0x90: v90(0x0) = CONST 
    0x92: CODECOPY v90(0x0), v8c(0x97), v88(0x3dae)
    0x93: v93(0x0) = CONST 
    0x95: RETURN v93(0x0), v88(0x3dae)

}

