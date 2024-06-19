function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x18, 0x1c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xde0b6b3a7640000) = CONST 
    0xe: ve(0x98) = CONST 
    0x10: SSTORE ve(0x98), v5(0xde0b6b3a7640000)
    0x11: v11 = CALLVALUE 
    0x13: v13 = ISZERO v11
    0x14: v14(0x1c) = CONST 
    0x17: JUMPI v14(0x1c), v13

    Begin block 0x18
    prev=[0x0], succ=[]
    =================================
    0x18: v18(0x0) = CONST 
    0x1b: REVERT v18(0x0), v18(0x0)

    Begin block 0x1c
    prev=[0x0], succ=[0x36, 0x2e]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x20: v20 = SLOAD v1e(0x0)
    0x21: v21(0x100) = CONST 
    0x25: v25 = DIV v20, v21(0x100)
    0x26: v26(0xff) = CONST 
    0x28: v28 = AND v26(0xff), v25
    0x2a: v2a(0x36) = CONST 
    0x2d: JUMPI v2a(0x36), v28

    Begin block 0x36
    prev=[0x1c, 0x2e], succ=[0x3b, 0x9d]
    =================================
    0x36_0x0: v36_0 = PHI v28, v35
    0x37: v37(0x9d) = CONST 
    0x3a: JUMPI v37(0x9d), v36_0

    Begin block 0x3b
    prev=[0x36], succ=[]
    =================================
    0x3b: v3b(0x40) = CONST 
    0x3d: v3d = MLOAD v3b(0x40)
    0x3e: v3e(0x461bcd) = CONST 
    0x42: v42(0xe5) = CONST 
    0x44: v44(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v42(0xe5), v3e(0x461bcd)
    0x46: MSTORE v3d, v44(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x47: v47(0x20) = CONST 
    0x49: v49(0x4) = CONST 
    0x4c: v4c = ADD v3d, v49(0x4)
    0x4d: MSTORE v4c, v47(0x20)
    0x4e: v4e(0x2e) = CONST 
    0x50: v50(0x24) = CONST 
    0x53: v53 = ADD v3d, v50(0x24)
    0x54: MSTORE v53, v4e(0x2e)
    0x55: v55(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561) = CONST 
    0x76: v76(0x44) = CONST 
    0x79: v79 = ADD v3d, v76(0x44)
    0x7a: MSTORE v79, v55(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561)
    0x7b: v7b(0x191e481a5b9a5d1a585b1a5e9959) = CONST 
    0x8a: v8a(0x92) = CONST 
    0x8c: v8c(0x647920696e697469616c697a6564000000000000000000000000000000000000) = SHL v8a(0x92), v7b(0x191e481a5b9a5d1a585b1a5e9959)
    0x8d: v8d(0x64) = CONST 
    0x90: v90 = ADD v3d, v8d(0x64)
    0x91: MSTORE v90, v8c(0x647920696e697469616c697a6564000000000000000000000000000000000000)
    0x92: v92(0x84) = CONST 
    0x94: v94 = ADD v92(0x84), v3d
    0x95: v95(0x40) = CONST 
    0x97: v97 = MLOAD v95(0x40)
    0x9a: v9a(0x84) = SUB v94, v97
    0x9c: REVERT v97, v9a(0x84)

    Begin block 0x9d
    prev=[0x36], succ=[0xb0, 0xbf]
    =================================
    0x9e: v9e(0x0) = CONST 
    0xa0: va0 = SLOAD v9e(0x0)
    0xa1: va1(0x100) = CONST 
    0xa5: va5 = DIV va0, va1(0x100)
    0xa6: va6(0xff) = CONST 
    0xa8: va8 = AND va6(0xff), va5
    0xa9: va9 = ISZERO va8
    0xab: vab = ISZERO va9
    0xac: vac(0xbf) = CONST 
    0xaf: JUMPI vac(0xbf), vab

    Begin block 0xb0
    prev=[0x9d], succ=[0xbf]
    =================================
    0xb0: vb0(0x0) = CONST 
    0xb3: vb3 = SLOAD vb0(0x0)
    0xb4: vb4(0xffff) = CONST 
    0xb7: vb7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT vb4(0xffff)
    0xb8: vb8 = AND vb7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000), vb3
    0xb9: vb9(0x101) = CONST 
    0xbc: vbc = OR vb9(0x101), vb8
    0xbe: SSTORE vb0(0x0), vbc

    Begin block 0xbf
    prev=[0xb0, 0x9d], succ=[0xc6, 0xd1]
    =================================
    0xc1: vc1 = ISZERO va9
    0xc2: vc2(0xd1) = CONST 
    0xc5: JUMPI vc2(0xd1), vc1

    Begin block 0xc6
    prev=[0xbf], succ=[0xd1]
    =================================
    0xc6: vc6(0x0) = CONST 
    0xc9: vc9 = SLOAD vc6(0x0)
    0xca: vca(0xff00) = CONST 
    0xcd: vcd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT vca(0xff00)
    0xce: vce = AND vcd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), vc9
    0xd0: SSTORE vc6(0x0), vce

    Begin block 0xd1
    prev=[0xc6, 0xbf], succ=[]
    =================================
    0xd3: vd3(0x10ab) = CONST 
    0xd7: vd7(0xe1) = CONST 
    0xda: vda(0x0) = CONST 
    0xdc: CODECOPY vda(0x0), vd7(0xe1), vd3(0x10ab)
    0xdd: vdd(0x0) = CONST 
    0xdf: RETURN vdd(0x0), vd3(0x10ab)

    Begin block 0x2e
    prev=[0x1c], succ=[0x36]
    =================================
    0x2f: v2f(0x0) = CONST 
    0x31: v31 = SLOAD v2f(0x0)
    0x32: v32(0xff) = CONST 
    0x34: v34 = AND v32(0xff), v31
    0x35: v35 = ISZERO v34

}

