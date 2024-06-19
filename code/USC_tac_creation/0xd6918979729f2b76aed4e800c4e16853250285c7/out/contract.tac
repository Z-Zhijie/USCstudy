function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x114, 0x118]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x0), vf
    0x12: v12(0x2) = CONST 
    0x15: v15 = SLOAD v12(0x2)
    0x16: v16(0x1) = CONST 
    0x18: v18(0x1) = CONST 
    0x1a: v1a(0xa0) = CONST 
    0x1c: v1c(0x10000000000000000000000000000000000000000) = SHL v1a(0xa0), v18(0x1)
    0x1d: v1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c(0x10000000000000000000000000000000000000000), v16(0x1)
    0x1e: v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x21: v21 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v15
    0x22: v22(0x3e0af2916e598fa5ea5cb2da4edfda9aed9fde) = CONST 
    0x36: v36 = OR v22(0x3e0af2916e598fa5ea5cb2da4edfda9aed9fde), v21
    0x39: SSTORE v12(0x2), v36
    0x3a: v3a(0x3) = CONST 
    0x3d: v3d = SLOAD v3a(0x3)
    0x3f: v3f = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3d
    0x40: v40(0x9f48b2f14517770f2d238c787356f3b961a6616f) = CONST 
    0x55: v55 = OR v40(0x9f48b2f14517770f2d238c787356f3b961a6616f), v3f
    0x57: SSTORE v3a(0x3), v55
    0x58: v58(0x4) = CONST 
    0x5b: v5b = SLOAD v58(0x4)
    0x5d: v5d = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5b
    0x5e: v5e(0xe7c9c188138f7d70945d420d75f8ca7d8ab9c700) = CONST 
    0x73: v73 = OR v5e(0xe7c9c188138f7d70945d420d75f8ca7d8ab9c700), v5d
    0x75: SSTORE v58(0x4), v73
    0x76: v76(0x5) = CONST 
    0x79: v79 = SLOAD v76(0x5)
    0x7b: v7b = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v79
    0x7c: v7c(0x6b175474e89094c44da98b954eedeac495271d0f) = CONST 
    0x91: v91 = OR v7c(0x6b175474e89094c44da98b954eedeac495271d0f), v7b
    0x93: SSTORE v76(0x5), v91
    0x94: v94(0x6) = CONST 
    0x97: v97 = SLOAD v94(0x6)
    0x99: v99 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v97
    0x9a: v9a(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48) = CONST 
    0xaf: vaf = OR v9a(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48), v99
    0xb1: SSTORE v94(0x6), vaf
    0xb2: vb2(0x7) = CONST 
    0xb5: vb5 = SLOAD vb2(0x7)
    0xb7: vb7 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb5
    0xb8: vb8(0xb9fb8a22908c570c09a4dbf5f89b87f9d91fbf4a) = CONST 
    0xcd: vcd = OR vb8(0xb9fb8a22908c570c09a4dbf5f89b87f9d91fbf4a), vb7
    0xcf: SSTORE vb2(0x7), vcd
    0xd0: vd0(0x8) = CONST 
    0xd3: vd3 = SLOAD vd0(0x8)
    0xd5: vd5 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd3
    0xd6: vd6(0x90f42043e638094d710bdcf1d1cbe6268aeb22d7) = CONST 
    0xeb: veb = OR vd6(0x90f42043e638094d710bdcf1d1cbe6268aeb22d7), vd5
    0xed: SSTORE vd0(0x8), veb
    0xee: vee(0xd) = CONST 
    0xf1: vf1 = SLOAD vee(0xd)
    0xf4: vf4 = AND v1e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vf1
    0xf5: vf5(0x18d6e366d854d73ca9c5a557ef79ccfaa732ab7b) = CONST 
    0x10a: v10a = OR vf5(0x18d6e366d854d73ca9c5a557ef79ccfaa732ab7b), vf4
    0x10c: SSTORE vee(0xd), v10a
    0x10d: v10d = CALLVALUE 
    0x10f: v10f = ISZERO v10d
    0x110: v110(0x118) = CONST 
    0x113: JUMPI v110(0x118), v10f

    Begin block 0x114
    prev=[0x0], succ=[]
    =================================
    0x114: v114(0x0) = CONST 
    0x117: REVERT v114(0x0), v114(0x0)

    Begin block 0x118
    prev=[0x0], succ=[]
    =================================
    0x11a: v11a(0x41d1) = CONST 
    0x11e: v11e(0x128) = CONST 
    0x121: v121(0x0) = CONST 
    0x123: CODECOPY v121(0x0), v11e(0x128), v11a(0x41d1)
    0x124: v124(0x0) = CONST 
    0x126: RETURN v124(0x0), v11a(0x41d1)

}

