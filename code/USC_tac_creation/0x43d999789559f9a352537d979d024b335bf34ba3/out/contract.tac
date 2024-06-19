function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xf, 0xb]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5 = CALLVALUE 
    0x6: v6 = ISZERO v5
    0x7: v7(0xf) = CONST 
    0xa: JUMPI v7(0xf), v6

    Begin block 0xf
    prev=[0x0], succ=[0x44]
    =================================
    0x10: v10(0x40) = CONST 
    0x12: v12 = MLOAD v10(0x40)
    0x13: v13(0x20) = CONST 
    0x16: v16(0x7c7) = CONST 
    0x1c: v1c = ADD v7e8(0x000000000000000000000000529f23840246d4d520261a0827cb414b4c6463d0), v12
    0x1d: v1d(0x40) = CONST 
    0x1f: MSTORE v1d(0x40), v1c
    0x22: v22 = MLOAD v7e8(0x000000000000000000000000529f23840246d4d520261a0827cb414b4c6463d0)
    0x28: v28(0x3d) = CONST 
    0x2c: v2c(0x100000000) = CONST 
    0x32: v32(0x64d) = CONST 
    0x35: v35(0x44) = CONST 
    0x39: v39(0x4400000000) = MUL v2c(0x100000000), v35(0x44)
    0x3a: v3a(0x440000064d) = OR v39(0x4400000000), v32(0x64d)
    0x3b: v3b(0x44) = DIV v3a(0x440000064d), v2c(0x100000000)
    0x3c: JUMP v3b(0x44)
    0x7e8: v7e8(0x000000000000000000000000529f23840246d4d520261a0827cb414b4c6463d0) = CONST 

    Begin block 0x44
    prev=[0xf], succ=[0x3d]
    =================================
    0x45: v45(0x0) = CONST 
    0x48: v48 = SLOAD v45(0x0)
    0x49: v49(0x1) = CONST 
    0x4b: v4b(0xa0) = CONST 
    0x4d: v4d(0x2) = CONST 
    0x4f: v4f(0x10000000000000000000000000000000000000000) = EXP v4d(0x2), v4b(0xa0)
    0x50: v50(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f(0x10000000000000000000000000000000000000000), v49(0x1)
    0x51: v51(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v50(0xffffffffffffffffffffffffffffffffffffffff)
    0x52: v52 = AND v51(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v48
    0x53: v53(0x1) = CONST 
    0x55: v55(0xa0) = CONST 
    0x57: v57(0x2) = CONST 
    0x59: v59(0x10000000000000000000000000000000000000000) = EXP v57(0x2), v55(0xa0)
    0x5a: v5a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v59(0x10000000000000000000000000000000000000000), v53(0x1)
    0x5e: v5e = AND v5a(0xffffffffffffffffffffffffffffffffffffffff), v22
    0x62: v62 = OR v5e, v52
    0x64: SSTORE v45(0x0), v62
    0x65: JUMP v28(0x3d)

    Begin block 0x3d
    prev=[0x44], succ=[0x66]
    =================================
    0x40: v40(0x66) = CONST 
    0x43: JUMP v40(0x66)

    Begin block 0x66
    prev=[0x3d], succ=[]
    =================================
    0x67: v67(0x752) = CONST 
    0x6b: v6b(0x75) = CONST 
    0x6e: v6e(0x0) = CONST 
    0x70: CODECOPY v6e(0x0), v6b(0x75), v67(0x752)
    0x71: v71(0x0) = CONST 
    0x73: RETURN v71(0x0), v67(0x752)

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xb: vb(0x0) = CONST 
    0xe: REVERT vb(0x0), vb(0x0)

}

