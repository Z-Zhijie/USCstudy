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
    prev=[0x0], succ=[0x2a, 0x22]
    =================================
    0x12: v12(0x0) = CONST 
    0x14: v14 = SLOAD v12(0x0)
    0x15: v15(0x100) = CONST 
    0x19: v19 = DIV v14, v15(0x100)
    0x1a: v1a(0xff) = CONST 
    0x1c: v1c = AND v1a(0xff), v19
    0x1e: v1e(0x2a) = CONST 
    0x21: JUMPI v1e(0x2a), v1c

    Begin block 0x2a
    prev=[0x10, 0x22], succ=[0x2f, 0x91]
    =================================
    0x2a_0x0: v2a_0 = PHI v1c, v29
    0x2b: v2b(0x91) = CONST 
    0x2e: JUMPI v2b(0x91), v2a_0

    Begin block 0x2f
    prev=[0x2a], succ=[]
    =================================
    0x2f: v2f(0x40) = CONST 
    0x31: v31 = MLOAD v2f(0x40)
    0x32: v32(0x461bcd) = CONST 
    0x36: v36(0xe5) = CONST 
    0x38: v38(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v36(0xe5), v32(0x461bcd)
    0x3a: MSTORE v31, v38(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3b: v3b(0x20) = CONST 
    0x3d: v3d(0x4) = CONST 
    0x40: v40 = ADD v31, v3d(0x4)
    0x41: MSTORE v40, v3b(0x20)
    0x42: v42(0x2e) = CONST 
    0x44: v44(0x24) = CONST 
    0x47: v47 = ADD v31, v44(0x24)
    0x48: MSTORE v47, v42(0x2e)
    0x49: v49(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561) = CONST 
    0x6a: v6a(0x44) = CONST 
    0x6d: v6d = ADD v31, v6a(0x44)
    0x6e: MSTORE v6d, v49(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561)
    0x6f: v6f(0x191e481a5b9a5d1a585b1a5e9959) = CONST 
    0x7e: v7e(0x92) = CONST 
    0x80: v80(0x647920696e697469616c697a6564000000000000000000000000000000000000) = SHL v7e(0x92), v6f(0x191e481a5b9a5d1a585b1a5e9959)
    0x81: v81(0x64) = CONST 
    0x84: v84 = ADD v31, v81(0x64)
    0x85: MSTORE v84, v80(0x647920696e697469616c697a6564000000000000000000000000000000000000)
    0x86: v86(0x84) = CONST 
    0x88: v88 = ADD v86(0x84), v31
    0x89: v89(0x40) = CONST 
    0x8b: v8b = MLOAD v89(0x40)
    0x8e: v8e(0x84) = SUB v88, v8b
    0x90: REVERT v8b, v8e(0x84)

    Begin block 0x91
    prev=[0x2a], succ=[0xa4, 0xb3]
    =================================
    0x92: v92(0x0) = CONST 
    0x94: v94 = SLOAD v92(0x0)
    0x95: v95(0x100) = CONST 
    0x99: v99 = DIV v94, v95(0x100)
    0x9a: v9a(0xff) = CONST 
    0x9c: v9c = AND v9a(0xff), v99
    0x9d: v9d = ISZERO v9c
    0x9f: v9f = ISZERO v9d
    0xa0: va0(0xb3) = CONST 
    0xa3: JUMPI va0(0xb3), v9f

    Begin block 0xa4
    prev=[0x91], succ=[0xb3]
    =================================
    0xa4: va4(0x0) = CONST 
    0xa7: va7 = SLOAD va4(0x0)
    0xa8: va8(0xffff) = CONST 
    0xab: vab(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT va8(0xffff)
    0xac: vac = AND vab(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000), va7
    0xad: vad(0x101) = CONST 
    0xb0: vb0 = OR vad(0x101), vac
    0xb2: SSTORE va4(0x0), vb0

    Begin block 0xb3
    prev=[0xa4, 0x91], succ=[0xba, 0xc5]
    =================================
    0xb5: vb5 = ISZERO v9d
    0xb6: vb6(0xc5) = CONST 
    0xb9: JUMPI vb6(0xc5), vb5

    Begin block 0xba
    prev=[0xb3], succ=[0xc5]
    =================================
    0xba: vba(0x0) = CONST 
    0xbd: vbd = SLOAD vba(0x0)
    0xbe: vbe(0xff00) = CONST 
    0xc1: vc1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT vbe(0xff00)
    0xc2: vc2 = AND vc1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), vbd
    0xc4: SSTORE vba(0x0), vc2

    Begin block 0xc5
    prev=[0xba, 0xb3], succ=[]
    =================================
    0xc7: vc7(0x99c) = CONST 
    0xcb: vcb(0xd5) = CONST 
    0xce: vce(0x0) = CONST 
    0xd0: CODECOPY vce(0x0), vcb(0xd5), vc7(0x99c)
    0xd1: vd1(0x0) = CONST 
    0xd3: RETURN vd1(0x0), vc7(0x99c)

    Begin block 0x22
    prev=[0x10], succ=[0x2a]
    =================================
    0x23: v23(0x0) = CONST 
    0x25: v25 = SLOAD v23(0x0)
    0x26: v26(0xff) = CONST 
    0x28: v28 = AND v26(0xff), v25
    0x29: v29 = ISZERO v28

}

