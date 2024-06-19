function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x11]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x11) = CONST 
    0xc: JUMPI v8(0x11), v7

    Begin block 0xd
    prev=[0x0], succ=[]
    =================================
    0xd: vd(0x0) = CONST 
    0x10: REVERT vd(0x0), vd(0x0)

    Begin block 0x11
    prev=[0x0], succ=[0x2a]
    =================================
    0x13: v13(0x24) = CONST 
    0x17: v17(0x1ffc9a7) = CONST 
    0x1c: v1c(0xe0) = CONST 
    0x1e: v1e(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v1c(0xe0), v17(0x1ffc9a7)
    0x1f: v1f(0x2a) = CONST 
    0x23: JUMP v1f(0x2a)

    Begin block 0x2a
    prev=[0x11], succ=[0x3e, 0x8a]
    =================================
    0x2b: v2b(0x1) = CONST 
    0x2d: v2d(0x1) = CONST 
    0x2f: v2f(0xe0) = CONST 
    0x31: v31(0x100000000000000000000000000000000000000000000000000000000) = SHL v2f(0xe0), v2d(0x1)
    0x32: v32(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v31(0x100000000000000000000000000000000000000000000000000000000), v2b(0x1)
    0x33: v33(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v32(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x36: v36(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND v1e(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v33(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x37: v37(0x0) = EQ v36(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v33(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x38: v38 = ISZERO v37(0x0)
    0x39: v39(0x8a) = CONST 
    0x3d: JUMPI v39(0x8a), v38

    Begin block 0x3e
    prev=[0x2a], succ=[]
    =================================
    0x3e: v3e(0x40) = CONST 
    0x41: v41 = MLOAD v3e(0x40)
    0x42: v42(0x461bcd) = CONST 
    0x46: v46(0xe5) = CONST 
    0x48: v48(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v46(0xe5), v42(0x461bcd)
    0x4a: MSTORE v41, v48(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4b: v4b(0x20) = CONST 
    0x4d: v4d(0x4) = CONST 
    0x50: v50 = ADD v41, v4d(0x4)
    0x51: MSTORE v50, v4b(0x20)
    0x52: v52(0x1c) = CONST 
    0x54: v54(0x24) = CONST 
    0x57: v57 = ADD v41, v54(0x24)
    0x58: MSTORE v57, v52(0x1c)
    0x59: v59(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0x7a: v7a(0x44) = CONST 
    0x7d: v7d = ADD v41, v7a(0x44)
    0x7e: MSTORE v7d, v59(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0x80: v80 = MLOAD v3e(0x40)
    0x84: v84(0x0) = SUB v41, v80
    0x85: v85(0x64) = CONST 
    0x87: v87(0x64) = ADD v85(0x64), v84(0x0)
    0x89: REVERT v80, v87(0x64)

    Begin block 0x8a
    prev=[0x2a], succ=[0x24]
    =================================
    0x8b: v8b(0x1) = CONST 
    0x8d: v8d(0x1) = CONST 
    0x8f: v8f(0xe0) = CONST 
    0x91: v91(0x100000000000000000000000000000000000000000000000000000000) = SHL v8f(0xe0), v8d(0x1)
    0x92: v92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v91(0x100000000000000000000000000000000000000000000000000000000), v8b(0x1)
    0x93: v93(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x94: v94(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND v93(0xffffffff00000000000000000000000000000000000000000000000000000000), v1e(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x95: v95(0x0) = CONST 
    0x99: MSTORE v95(0x0), v94(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x9a: v9a(0x20) = CONST 
    0x9e: MSTORE v9a(0x20), v95(0x0)
    0x9f: v9f(0x40) = CONST 
    0xa2: va2 = SHA3 v95(0x0), v9f(0x40)
    0xa4: va4 = SLOAD va2
    0xa5: va5(0xff) = CONST 
    0xa7: va7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT va5(0xff)
    0xa8: va8 = AND va7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), va4
    0xa9: va9(0x1) = CONST 
    0xab: vab = OR va9(0x1), va8
    0xad: SSTORE va2, vab
    0xae: JUMP v13(0x24)

    Begin block 0x24
    prev=[0x8a], succ=[0xaf]
    =================================
    0x25: v25(0xaf) = CONST 
    0x29: JUMP v25(0xaf)

    Begin block 0xaf
    prev=[0x24], succ=[]
    =================================
    0xb0: vb0(0x3c40) = CONST 
    0xb4: vb4(0xbf) = CONST 
    0xb8: vb8(0x0) = CONST 
    0xba: CODECOPY vb8(0x0), vb4(0xbf), vb0(0x3c40)
    0xbb: vbb(0x0) = CONST 
    0xbd: RETURN vbb(0x0), vb0(0x3c40)

}

