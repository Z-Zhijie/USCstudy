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
    prev=[0x0], succ=[0x2f, 0x33]
    =================================
    0x12: v12(0x40) = CONST 
    0x14: v14 = MLOAD v12(0x40)
    0x15: v15(0x14d) = CONST 
    0x18: v18 = CODESIZE 
    0x19: v19 = SUB v18, v15(0x14d)
    0x1b: v1b(0x14d) = CONST 
    0x1f: CODECOPY v14, v1b(0x14d), v19
    0x22: v22 = ADD v19, v14
    0x23: v23(0x40) = CONST 
    0x25: MSTORE v23(0x40), v22
    0x26: v26(0x20) = CONST 
    0x29: v29 = LT v19, v26(0x20)
    0x2a: v2a = ISZERO v29
    0x2b: v2b(0x33) = CONST 
    0x2e: JUMPI v2b(0x33), v2a

    Begin block 0x2f
    prev=[0x10], succ=[]
    =================================
    0x2f: v2f(0x0) = CONST 
    0x32: REVERT v2f(0x0), v2f(0x0)

    Begin block 0x33
    prev=[0x10], succ=[0x44, 0x7a]
    =================================
    0x35: v35 = MLOAD v14
    0x36: v36(0x1) = CONST 
    0x38: v38(0x1) = CONST 
    0x3a: v3a(0xa0) = CONST 
    0x3c: v3c(0x10000000000000000000000000000000000000000) = SHL v3a(0xa0), v38(0x1)
    0x3d: v3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c(0x10000000000000000000000000000000000000000), v36(0x1)
    0x3f: v3f = AND v35, v3d(0xffffffffffffffffffffffffffffffffffffffff)
    0x40: v40(0x7a) = CONST 
    0x43: JUMPI v40(0x7a), v3f

    Begin block 0x44
    prev=[0x33], succ=[]
    =================================
    0x44: v44(0x40) = CONST 
    0x46: v46 = MLOAD v44(0x40)
    0x47: v47(0x461bcd) = CONST 
    0x4b: v4b(0xe5) = CONST 
    0x4d: v4d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v4b(0xe5), v47(0x461bcd)
    0x4f: MSTORE v46, v4d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x50: v50(0x4) = CONST 
    0x52: v52 = ADD v50(0x4), v46
    0x55: v55(0x20) = CONST 
    0x57: v57 = ADD v55(0x20), v52
    0x5a: v5a(0x20) = SUB v57, v52
    0x5c: MSTORE v52, v5a(0x20)
    0x5d: v5d(0x24) = CONST 
    0x60: MSTORE v57, v5d(0x24)
    0x61: v61(0x20) = CONST 
    0x63: v63 = ADD v61(0x20), v57
    0x65: v65(0x129) = CONST 
    0x68: v68(0x24) = CONST 
    0x6b: CODECOPY v63, v65(0x129), v68(0x24)
    0x6c: v6c(0x40) = CONST 
    0x6e: v6e = ADD v6c(0x40), v63
    0x72: v72(0x40) = CONST 
    0x74: v74 = MLOAD v72(0x40)
    0x77: v77(0x84) = SUB v6e, v74
    0x79: REVERT v74, v77(0x84)

    Begin block 0x7a
    prev=[0x33], succ=[]
    =================================
    0x7b: v7b(0x0) = CONST 
    0x7e: v7e = SLOAD v7b(0x0)
    0x7f: v7f(0x1) = CONST 
    0x81: v81(0x1) = CONST 
    0x83: v83(0xa0) = CONST 
    0x85: v85(0x10000000000000000000000000000000000000000) = SHL v83(0xa0), v81(0x1)
    0x86: v86(0xffffffffffffffffffffffffffffffffffffffff) = SUB v85(0x10000000000000000000000000000000000000000), v7f(0x1)
    0x89: v89 = AND v35, v86(0xffffffffffffffffffffffffffffffffffffffff)
    0x8a: v8a(0x1) = CONST 
    0x8c: v8c(0x1) = CONST 
    0x8e: v8e(0xa0) = CONST 
    0x90: v90(0x10000000000000000000000000000000000000000) = SHL v8e(0xa0), v8c(0x1)
    0x91: v91(0xffffffffffffffffffffffffffffffffffffffff) = SUB v90(0x10000000000000000000000000000000000000000), v8a(0x1)
    0x92: v92(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v91(0xffffffffffffffffffffffffffffffffffffffff)
    0x95: v95 = AND v7e, v92(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x99: v99 = OR v95, v89
    0x9b: SSTORE v7b(0x0), v99
    0x9c: v9c(0x80) = CONST 
    0x9f: v9f(0xa9) = CONST 
    0xa2: va2(0x0) = CONST 
    0xa4: CODECOPY va2(0x0), v9f(0xa9), v9c(0x80)
    0xa5: va5(0x0) = CONST 
    0xa7: RETURN va5(0x0), v9c(0x80)

}

