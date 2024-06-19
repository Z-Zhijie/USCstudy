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
    prev=[0x0], succ=[0x24]
    =================================
    0x13: v13(0x24) = CONST 
    0x17: v17(0x1ffc9a7) = CONST 
    0x1c: v1c(0xe0) = CONST 
    0x1e: v1e(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v1c(0xe0), v17(0x1ffc9a7)
    0x1f: v1f(0x3c) = CONST 
    0x23: CALLPRIVATE v1f(0x3c), v1e(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v13(0x24)

    Begin block 0x24
    prev=[0x11], succ=[0x36]
    =================================
    0x25: v25(0x36) = CONST 
    0x29: v29(0x2711897) = CONST 
    0x2e: v2e(0xe5) = CONST 
    0x30: v30(0x4e2312e000000000000000000000000000000000000000000000000000000000) = SHL v2e(0xe5), v29(0x2711897)
    0x31: v31(0x3c) = CONST 
    0x35: CALLPRIVATE v31(0x3c), v30(0x4e2312e000000000000000000000000000000000000000000000000000000000), v25(0x36)

    Begin block 0x36
    prev=[0x24], succ=[0xce]
    =================================
    0x37: v37(0xce) = CONST 
    0x3b: JUMP v37(0xce)

    Begin block 0xce
    prev=[0x36], succ=[]
    =================================
    0xcf: vcf(0x59c8) = CONST 
    0xd3: vd3(0xde) = CONST 
    0xd7: vd7(0x0) = CONST 
    0xd9: CODECOPY vd7(0x0), vd3(0xde), vcf(0x59c8)
    0xda: vda(0x0) = CONST 
    0xdc: RETURN vda(0x0), vcf(0x59c8)

}

function 0x3c(0x3carg0x0, 0x3carg0x1) private {
    Begin block 0x3c
    prev=[], succ=[0x50, 0x72]
    =================================
    0x3d: v3d(0x1) = CONST 
    0x3f: v3f(0x1) = CONST 
    0x41: v41(0xe0) = CONST 
    0x43: v43(0x100000000000000000000000000000000000000000000000000000000) = SHL v41(0xe0), v3f(0x1)
    0x44: v44(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v43(0x100000000000000000000000000000000000000000000000000000000), v3d(0x1)
    0x45: v45(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v44(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x48: v48 = AND v3carg0, v45(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x49: v49 = EQ v48, v45(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x4a: v4a = ISZERO v49
    0x4b: v4b(0x72) = CONST 
    0x4f: JUMPI v4b(0x72), v4a

    Begin block 0x50
    prev=[0x3c], succ=[0x97]
    =================================
    0x50: v50(0x40) = CONST 
    0x52: v52 = MLOAD v50(0x40)
    0x53: v53(0x461bcd) = CONST 
    0x57: v57(0xe5) = CONST 
    0x59: v59(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v57(0xe5), v53(0x461bcd)
    0x5b: MSTORE v52, v59(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5c: v5c(0x4) = CONST 
    0x5e: v5e = ADD v5c(0x4), v52
    0x5f: v5f(0x69) = CONST 
    0x64: v64(0x97) = CONST 
    0x68: JUMP v64(0x97)

    Begin block 0x97
    prev=[0x50], succ=[0x69]
    =================================
    0x98: v98(0x20) = CONST 
    0x9c: MSTORE v5e, v98(0x20)
    0x9d: v9d(0x1c) = CONST 
    0xa1: va1 = ADD v5e, v98(0x20)
    0xa2: MSTORE va1, v9d(0x1c)
    0xa3: va3(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0xc4: vc4(0x40) = CONST 
    0xc7: vc7 = ADD v5e, vc4(0x40)
    0xc8: MSTORE vc7, va3(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0xc9: vc9(0x60) = CONST 
    0xcb: vcb = ADD vc9(0x60), v5e
    0xcd: JUMP v5f(0x69)

    Begin block 0x69
    prev=[0x97], succ=[]
    =================================
    0x6a: v6a(0x40) = CONST 
    0x6c: v6c = MLOAD v6a(0x40)
    0x6f: v6f(0x64) = SUB vcb, v6c
    0x71: REVERT v6c, v6f(0x64)

    Begin block 0x72
    prev=[0x3c], succ=[]
    =================================
    0x73: v73(0x1) = CONST 
    0x75: v75(0x1) = CONST 
    0x77: v77(0xe0) = CONST 
    0x79: v79(0x100000000000000000000000000000000000000000000000000000000) = SHL v77(0xe0), v75(0x1)
    0x7a: v7a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v79(0x100000000000000000000000000000000000000000000000000000000), v73(0x1)
    0x7b: v7b(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v7a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x7c: v7c = AND v7b(0xffffffff00000000000000000000000000000000000000000000000000000000), v3carg0
    0x7d: v7d(0x0) = CONST 
    0x81: MSTORE v7d(0x0), v7c
    0x82: v82(0x42) = CONST 
    0x84: v84(0x20) = CONST 
    0x86: MSTORE v84(0x20), v82(0x42)
    0x87: v87(0x40) = CONST 
    0x8a: v8a = SHA3 v7d(0x0), v87(0x40)
    0x8c: v8c = SLOAD v8a
    0x8d: v8d(0xff) = CONST 
    0x8f: v8f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v8d(0xff)
    0x90: v90 = AND v8f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8c
    0x91: v91(0x1) = CONST 
    0x93: v93 = OR v91(0x1), v90
    0x95: SSTORE v8a, v93
    0x96: RETURNPRIVATE v3carg1

}

