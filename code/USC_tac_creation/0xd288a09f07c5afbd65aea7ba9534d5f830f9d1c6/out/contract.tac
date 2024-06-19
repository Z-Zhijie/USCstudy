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
    prev=[0x0], succ=[0x2c, 0x24]
    =================================
    0x13: v13(0x0) = CONST 
    0x15: v15 = SLOAD v13(0x0)
    0x16: v16(0x100) = CONST 
    0x1a: v1a = DIV v15, v16(0x100)
    0x1b: v1b(0xff) = CONST 
    0x1d: v1d = AND v1b(0xff), v1a
    0x1f: v1f(0x2c) = CONST 
    0x23: JUMPI v1f(0x2c), v1d

    Begin block 0x2c
    prev=[0x11, 0x24], succ=[0x32, 0x94]
    =================================
    0x2c_0x0: v2c_0 = PHI v1d, v2b
    0x2d: v2d(0x94) = CONST 
    0x31: JUMPI v2d(0x94), v2c_0

    Begin block 0x32
    prev=[0x2c], succ=[]
    =================================
    0x32: v32(0x40) = CONST 
    0x34: v34 = MLOAD v32(0x40)
    0x35: v35(0x461bcd) = CONST 
    0x39: v39(0xe5) = CONST 
    0x3b: v3b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v39(0xe5), v35(0x461bcd)
    0x3d: MSTORE v34, v3b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3e: v3e(0x20) = CONST 
    0x40: v40(0x4) = CONST 
    0x43: v43 = ADD v34, v40(0x4)
    0x44: MSTORE v43, v3e(0x20)
    0x45: v45(0x2e) = CONST 
    0x47: v47(0x24) = CONST 
    0x4a: v4a = ADD v34, v47(0x24)
    0x4b: MSTORE v4a, v45(0x2e)
    0x4c: v4c(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561) = CONST 
    0x6d: v6d(0x44) = CONST 
    0x70: v70 = ADD v34, v6d(0x44)
    0x71: MSTORE v70, v4c(0x496e697469616c697a61626c653a20636f6e747261637420697320616c726561)
    0x72: v72(0x191e481a5b9a5d1a585b1a5e9959) = CONST 
    0x81: v81(0x92) = CONST 
    0x83: v83(0x647920696e697469616c697a6564000000000000000000000000000000000000) = SHL v81(0x92), v72(0x191e481a5b9a5d1a585b1a5e9959)
    0x84: v84(0x64) = CONST 
    0x87: v87 = ADD v34, v84(0x64)
    0x88: MSTORE v87, v83(0x647920696e697469616c697a6564000000000000000000000000000000000000)
    0x89: v89(0x84) = CONST 
    0x8b: v8b = ADD v89(0x84), v34
    0x8c: v8c(0x40) = CONST 
    0x8e: v8e = MLOAD v8c(0x40)
    0x91: v91(0x84) = SUB v8b, v8e
    0x93: REVERT v8e, v91(0x84)

    Begin block 0x94
    prev=[0x2c], succ=[0xa8, 0xb7]
    =================================
    0x95: v95(0x0) = CONST 
    0x97: v97 = SLOAD v95(0x0)
    0x98: v98(0x100) = CONST 
    0x9c: v9c = DIV v97, v98(0x100)
    0x9d: v9d(0xff) = CONST 
    0x9f: v9f = AND v9d(0xff), v9c
    0xa0: va0 = ISZERO v9f
    0xa2: va2 = ISZERO va0
    0xa3: va3(0xb7) = CONST 
    0xa7: JUMPI va3(0xb7), va2

    Begin block 0xa8
    prev=[0x94], succ=[0xb7]
    =================================
    0xa8: va8(0x0) = CONST 
    0xab: vab = SLOAD va8(0x0)
    0xac: vac(0xffff) = CONST 
    0xaf: vaf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT vac(0xffff)
    0xb0: vb0 = AND vaf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000), vab
    0xb1: vb1(0x101) = CONST 
    0xb4: vb4 = OR vb1(0x101), vb0
    0xb6: SSTORE va8(0x0), vb4

    Begin block 0xb7
    prev=[0xa8, 0x94], succ=[0xbf, 0xca]
    =================================
    0xb9: vb9 = ISZERO va0
    0xba: vba(0xca) = CONST 
    0xbe: JUMPI vba(0xca), vb9

    Begin block 0xbf
    prev=[0xb7], succ=[0xca]
    =================================
    0xbf: vbf(0x0) = CONST 
    0xc2: vc2 = SLOAD vbf(0x0)
    0xc3: vc3(0xff00) = CONST 
    0xc6: vc6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT vc3(0xff00)
    0xc7: vc7 = AND vc6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), vc2
    0xc9: SSTORE vbf(0x0), vc7

    Begin block 0xca
    prev=[0xbf, 0xb7], succ=[]
    =================================
    0xcc: vcc(0x2b9c) = CONST 
    0xd0: vd0(0xdb) = CONST 
    0xd4: vd4(0x0) = CONST 
    0xd6: CODECOPY vd4(0x0), vd0(0xdb), vcc(0x2b9c)
    0xd7: vd7(0x0) = CONST 
    0xd9: RETURN vd7(0x0), vcc(0x2b9c)

    Begin block 0x24
    prev=[0x11], succ=[0x2c]
    =================================
    0x25: v25(0x0) = CONST 
    0x27: v27 = SLOAD v25(0x0)
    0x28: v28(0xff) = CONST 
    0x2a: v2a = AND v28(0xff), v27
    0x2b: v2b = ISZERO v2a

}

