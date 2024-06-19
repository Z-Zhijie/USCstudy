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
    prev=[0x0], succ=[0x26]
    =================================
    0x12: v12(0x21) = CONST 
    0x15: v15(0x1ffc9a7) = CONST 
    0x1a: v1a(0xe0) = CONST 
    0x1c: v1c(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v1a(0xe0), v15(0x1ffc9a7)
    0x1d: v1d(0x26) = CONST 
    0x20: JUMP v1d(0x26)

    Begin block 0x26
    prev=[0x10], succ=[0x39, 0x85]
    =================================
    0x27: v27(0x1) = CONST 
    0x29: v29(0x1) = CONST 
    0x2b: v2b(0xe0) = CONST 
    0x2d: v2d(0x100000000000000000000000000000000000000000000000000000000) = SHL v2b(0xe0), v29(0x1)
    0x2e: v2e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2d(0x100000000000000000000000000000000000000000000000000000000), v27(0x1)
    0x2f: v2f(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x32: v32(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND v1c(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v2f(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x33: v33(0x0) = EQ v32(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v2f(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x34: v34 = ISZERO v33(0x0)
    0x35: v35(0x85) = CONST 
    0x38: JUMPI v35(0x85), v34

    Begin block 0x39
    prev=[0x26], succ=[]
    =================================
    0x39: v39(0x40) = CONST 
    0x3c: v3c = MLOAD v39(0x40)
    0x3d: v3d(0x461bcd) = CONST 
    0x41: v41(0xe5) = CONST 
    0x43: v43(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v41(0xe5), v3d(0x461bcd)
    0x45: MSTORE v3c, v43(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x46: v46(0x20) = CONST 
    0x48: v48(0x4) = CONST 
    0x4b: v4b = ADD v3c, v48(0x4)
    0x4c: MSTORE v4b, v46(0x20)
    0x4d: v4d(0x1c) = CONST 
    0x4f: v4f(0x24) = CONST 
    0x52: v52 = ADD v3c, v4f(0x24)
    0x53: MSTORE v52, v4d(0x1c)
    0x54: v54(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0x75: v75(0x44) = CONST 
    0x78: v78 = ADD v3c, v75(0x44)
    0x79: MSTORE v78, v54(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0x7b: v7b = MLOAD v39(0x40)
    0x7f: v7f(0x0) = SUB v3c, v7b
    0x80: v80(0x64) = CONST 
    0x82: v82(0x64) = ADD v80(0x64), v7f(0x0)
    0x84: REVERT v7b, v82(0x64)

    Begin block 0x85
    prev=[0x26], succ=[0x21]
    =================================
    0x86: v86(0x1) = CONST 
    0x88: v88(0x1) = CONST 
    0x8a: v8a(0xe0) = CONST 
    0x8c: v8c(0x100000000000000000000000000000000000000000000000000000000) = SHL v8a(0xe0), v88(0x1)
    0x8d: v8d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v8c(0x100000000000000000000000000000000000000000000000000000000), v86(0x1)
    0x8e: v8e(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v8d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x8f: v8f(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND v8e(0xffffffff00000000000000000000000000000000000000000000000000000000), v1c(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x90: v90(0x0) = CONST 
    0x94: MSTORE v90(0x0), v8f(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x95: v95(0x20) = CONST 
    0x99: MSTORE v95(0x20), v90(0x0)
    0x9a: v9a(0x40) = CONST 
    0x9d: v9d = SHA3 v90(0x0), v9a(0x40)
    0x9f: v9f = SLOAD v9d
    0xa0: va0(0xff) = CONST 
    0xa2: va2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT va0(0xff)
    0xa3: va3 = AND va2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v9f
    0xa4: va4(0x1) = CONST 
    0xa6: va6 = OR va4(0x1), va3
    0xa8: SSTORE v9d, va6
    0xa9: JUMP v12(0x21)

    Begin block 0x21
    prev=[0x85], succ=[0xaa]
    =================================
    0x22: v22(0xaa) = CONST 
    0x25: JUMP v22(0xaa)

    Begin block 0xaa
    prev=[0x21], succ=[]
    =================================
    0xab: vab(0x2898) = CONST 
    0xaf: vaf(0xba) = CONST 
    0xb3: vb3(0x0) = CONST 
    0xb5: CODECOPY vb3(0x0), vaf(0xba), vab(0x2898)
    0xb6: vb6(0x0) = CONST 
    0xb8: RETURN vb6(0x0), vab(0x2898)

}

