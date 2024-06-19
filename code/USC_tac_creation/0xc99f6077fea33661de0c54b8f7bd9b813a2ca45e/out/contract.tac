function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x41, 0x45]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x12) = CONST 
    0x9: v9(0x0) = CONST 
    0xb: vb(0x100) = CONST 
    0xe: ve(0x1) = EXP vb(0x100), v9(0x0)
    0x10: v10 = SLOAD v7(0x12)
    0x12: v12(0xff) = CONST 
    0x14: v14(0xff) = MUL v12(0xff), ve(0x1)
    0x15: v15(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v14(0xff)
    0x16: v16 = AND v15(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v10
    0x19: v19(0x1) = ISZERO v5(0x0)
    0x1a: v1a(0x0) = ISZERO v19(0x1)
    0x1b: v1b(0x0) = MUL v1a(0x0), ve(0x1)
    0x1c: v1c = OR v1b(0x0), v16
    0x1e: SSTORE v7(0x12), v1c
    0x20: v20(0x0) = CONST 
    0x22: v22(0x12) = CONST 
    0x24: v24(0x1) = CONST 
    0x26: v26(0x100) = CONST 
    0x29: v29(0x100) = EXP v26(0x100), v24(0x1)
    0x2b: v2b = SLOAD v22(0x12)
    0x2d: v2d(0xff) = CONST 
    0x2f: v2f(0xff00) = MUL v2d(0xff), v29(0x100)
    0x30: v30(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v2f(0xff00)
    0x31: v31 = AND v30(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v2b
    0x34: v34(0x1) = ISZERO v20(0x0)
    0x35: v35(0x0) = ISZERO v34(0x1)
    0x36: v36(0x0) = MUL v35(0x0), v29(0x100)
    0x37: v37 = OR v36(0x0), v31
    0x39: SSTORE v22(0x12), v37
    0x3b: v3b = CALLVALUE 
    0x3c: v3c = ISZERO v3b
    0x3d: v3d(0x45) = CONST 
    0x40: JUMPI v3d(0x45), v3c

    Begin block 0x41
    prev=[0x0], succ=[]
    =================================
    0x41: v41(0x0) = CONST 
    0x44: REVERT v41(0x0), v41(0x0)

    Begin block 0x45
    prev=[0x0], succ=[]
    =================================
    0x46: v46(0x40) = CONST 
    0x48: v48 = MLOAD v46(0x40)
    0x49: v49(0x20) = CONST 
    0x4c: v4c(0x2c5e) = CONST 
    0x52: v52 = ADD v2c81(0x3730316565316220000000000000000000000000000000000000000000000000), v48
    0x53: v53(0x40) = CONST 
    0x55: MSTORE v53(0x40), v52
    0x58: v58 = MLOAD v2c81(0x3730316565316220000000000000000000000000000000000000000000000000)
    0x5a: v5a(0x20) = CONST 
    0x5c: v5c(0x3730316565316220000000000000000000000000000000000000000000000020) = ADD v5a(0x20), v2c81(0x3730316565316220000000000000000000000000000000000000000000000000)
    0x62: v62 = CALLER 
    0x63: v63(0x0) = CONST 
    0x66: v66(0x100) = CONST 
    0x69: v69(0x1) = EXP v66(0x100), v63(0x0)
    0x6b: v6b = SLOAD v63(0x0)
    0x6d: v6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x82: v82(0xffffffffffffffffffffffffffffffffffffffff) = MUL v6d(0xffffffffffffffffffffffffffffffffffffffff), v69(0x1)
    0x83: v83(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v82(0xffffffffffffffffffffffffffffffffffffffff)
    0x84: v84 = AND v83(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6b
    0x87: v87(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9c: v9c = AND v87(0xffffffffffffffffffffffffffffffffffffffff), v62
    0x9d: v9d = MUL v9c, v69(0x1)
    0x9e: v9e = OR v9d, v84
    0xa0: SSTORE v63(0x0), v9e
    0xa2: va2 = CALLER 
    0xa3: va3(0x1) = CONST 
    0xa5: va5(0x0) = CONST 
    0xa7: va7(0x100) = CONST 
    0xaa: vaa(0x1) = EXP va7(0x100), va5(0x0)
    0xac: vac = SLOAD va3(0x1)
    0xae: vae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc3: vc3(0xffffffffffffffffffffffffffffffffffffffff) = MUL vae(0xffffffffffffffffffffffffffffffffffffffff), vaa(0x1)
    0xc4: vc4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vc3(0xffffffffffffffffffffffffffffffffffffffff)
    0xc5: vc5 = AND vc4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vac
    0xc8: vc8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdd: vdd = AND vc8(0xffffffffffffffffffffffffffffffffffffffff), va2
    0xde: vde = MUL vdd, vaa(0x1)
    0xdf: vdf = OR vde, vc5
    0xe1: SSTORE va3(0x1), vdf
    0xe4: ve4(0x12) = CONST 
    0xe6: ve6(0x2) = CONST 
    0xe8: ve8(0x100) = CONST 
    0xeb: veb(0x10000) = EXP ve8(0x100), ve6(0x2)
    0xed: ved = SLOAD ve4(0x12)
    0xef: vef(0xffffffffffffffff) = CONST 
    0xf8: vf8(0xffffffffffffffff0000) = MUL vef(0xffffffffffffffff), veb(0x10000)
    0xf9: vf9(0xffffffffffffffffffffffffffffffffffffffffffff0000000000000000ffff) = NOT vf8(0xffffffffffffffff0000)
    0xfa: vfa = AND vf9(0xffffffffffffffffffffffffffffffffffffffffffff0000000000000000ffff), ved
    0xfd: vfd(0x1000000000000000000000000000000000000000000000000) = CONST 
    0x118: v118 = DIV v58, vfd(0x1000000000000000000000000000000000000000000000000)
    0x119: v119 = MUL v118, veb(0x10000)
    0x11a: v11a = OR v119, vfa
    0x11c: SSTORE ve4(0x12), v11a
    0x11f: v11f(0x2b31) = CONST 
    0x123: v123(0x12d) = CONST 
    0x126: v126(0x0) = CONST 
    0x128: CODECOPY v126(0x0), v123(0x12d), v11f(0x2b31)
    0x129: v129(0x0) = CONST 
    0x12b: RETURN v129(0x0), v11f(0x2b31)
    0x2c81: v2c81(0x3730316565316220000000000000000000000000000000000000000000000000) = CONST 

}

