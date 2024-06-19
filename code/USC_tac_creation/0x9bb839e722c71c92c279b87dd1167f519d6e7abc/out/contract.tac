function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x12, 0x16]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x7: v7(0x2) = CONST 
    0x9: SSTORE v7(0x2), v5(0x1)
    0xa: va = CALLVALUE 
    0xc: vc = ISZERO va
    0xd: vd(0x16) = CONST 
    0x11: JUMPI vd(0x16), vc

    Begin block 0x12
    prev=[0x0], succ=[]
    =================================
    0x12: v12(0x0) = CONST 
    0x15: REVERT v12(0x0), v12(0x0)

    Begin block 0x16
    prev=[0x0], succ=[0x77]
    =================================
    0x18: v18(0x0) = CONST 
    0x1a: v1a(0x23) = CONST 
    0x1e: v1e(0x77) = CONST 
    0x22: JUMP v1e(0x77)

    Begin block 0x77
    prev=[0x16], succ=[0x23]
    =================================
    0x78: v78 = CALLER 
    0x7a: JUMP v1a(0x23)

    Begin block 0x23
    prev=[0x77], succ=[0x7b]
    =================================
    0x24: v24(0x0) = CONST 
    0x27: v27 = SLOAD v24(0x0)
    0x28: v28(0x1) = CONST 
    0x2a: v2a(0x1) = CONST 
    0x2c: v2c(0xa0) = CONST 
    0x2e: v2e(0x10000000000000000000000000000000000000000) = SHL v2c(0xa0), v2a(0x1)
    0x2f: v2f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e(0x10000000000000000000000000000000000000000), v28(0x1)
    0x30: v30(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2f(0xffffffffffffffffffffffffffffffffffffffff)
    0x31: v31 = AND v30(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v27
    0x32: v32(0x1) = CONST 
    0x34: v34(0x1) = CONST 
    0x36: v36(0xa0) = CONST 
    0x38: v38(0x10000000000000000000000000000000000000000) = SHL v36(0xa0), v34(0x1)
    0x39: v39(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38(0x10000000000000000000000000000000000000000), v32(0x1)
    0x3b: v3b = AND v78, v39(0xffffffffffffffffffffffffffffffffffffffff)
    0x3e: v3e = OR v3b, v31
    0x40: SSTORE v24(0x0), v3e
    0x41: v41(0x40) = CONST 
    0x43: v43 = MLOAD v41(0x40)
    0x48: v48(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x6c: LOG3 v43, v24(0x0), v48(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v24(0x0), v3b
    0x6e: v6e(0x1) = CONST 
    0x71: SSTORE v6e(0x1), v6e(0x1)
    0x72: v72(0x7b) = CONST 
    0x76: JUMP v72(0x7b)

    Begin block 0x7b
    prev=[0x23], succ=[]
    =================================
    0x7c: v7c(0x53bf) = CONST 
    0x80: v80(0x8b) = CONST 
    0x84: v84(0x0) = CONST 
    0x86: CODECOPY v84(0x0), v80(0x8b), v7c(0x53bf)
    0x87: v87(0x0) = CONST 
    0x89: RETURN v87(0x0), v7c(0x53bf)

}

