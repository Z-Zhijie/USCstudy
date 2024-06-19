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
    prev=[0x0], succ=[0x3e]
    =================================
    0x12: v12(0x0) = CONST 
    0x15: v15 = SLOAD v12(0x0)
    0x16: v16(0x1) = CONST 
    0x18: v18(0x1) = CONST 
    0x1a: v1a(0xa0) = CONST 
    0x1c: v1c(0x10000000000000000000000000000000000000000) = SHL v1a(0xa0), v18(0x1)
    0x1d: v1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c(0x10000000000000000000000000000000000000000), v16(0x1)
    0x1e: v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f: v1f = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v15
    0x20: v20 = CALLER 
    0x23: v23 = OR v20, v1f
    0x26: SSTORE v12(0x0), v23
    0x27: v27(0x38) = CONST 
    0x2b: v2b(0x1) = CONST 
    0x2d: v2d(0x1) = CONST 
    0x2f: v2f(0xe0) = CONST 
    0x31: v31(0x100000000000000000000000000000000000000000000000000000000) = SHL v2f(0xe0), v2d(0x1)
    0x32: v32(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v31(0x100000000000000000000000000000000000000000000000000000000), v2b(0x1)
    0x33: v33(0x3e) = CONST 
    0x36: v36(0x3e) = AND v33(0x3e), v32(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x37: JUMP v36(0x3e)

    Begin block 0x3e
    prev=[0x10], succ=[0x38]
    =================================
    0x3f: v3f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x60: SSTORE v3f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v20
    0x61: JUMP v27(0x38)

    Begin block 0x38
    prev=[0x3e], succ=[0x62]
    =================================
    0x3a: v3a(0x62) = CONST 
    0x3d: JUMP v3a(0x62)

    Begin block 0x62
    prev=[0x38], succ=[]
    =================================
    0x63: v63(0x696) = CONST 
    0x67: v67(0x71) = CONST 
    0x6a: v6a(0x0) = CONST 
    0x6c: CODECOPY v6a(0x0), v67(0x71), v63(0x696)
    0x6d: v6d(0x0) = CONST 
    0x6f: RETURN v6d(0x0), v63(0x696)

}

