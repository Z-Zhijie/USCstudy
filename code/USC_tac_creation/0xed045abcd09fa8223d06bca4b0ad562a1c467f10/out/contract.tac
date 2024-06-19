function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x46, 0x4a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0x1) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0x2) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = EXP vd(0x2), vb(0xa0)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x13: v13 = CALLER 
    0x14: v14 = OR v13, v12
    0x16: SSTORE v5(0x0), v14
    0x17: v17(0x3e8) = CONST 
    0x1a: v1a(0x6) = CONST 
    0x1c: SSTORE v1a(0x6), v17(0x3e8)
    0x1d: v1d(0x8e1bc9bf040000) = CONST 
    0x25: v25(0x7) = CONST 
    0x27: SSTORE v25(0x7), v1d(0x8e1bc9bf040000)
    0x28: v28(0xe35fa931a00000) = CONST 
    0x30: v30(0x8) = CONST 
    0x32: SSTORE v30(0x8), v28(0xe35fa931a00000)
    0x33: v33(0x61b31ab352c0000) = CONST 
    0x3c: v3c(0x9) = CONST 
    0x3e: SSTORE v3c(0x9), v33(0x61b31ab352c0000)
    0x3f: v3f = CALLVALUE 
    0x41: v41 = ISZERO v3f
    0x42: v42(0x4a) = CONST 
    0x45: JUMPI v42(0x4a), v41

    Begin block 0x46
    prev=[0x0], succ=[]
    =================================
    0x46: v46(0x0) = CONST 
    0x49: REVERT v46(0x0), v46(0x0)

    Begin block 0x4a
    prev=[0x0], succ=[0x92, 0x90]
    =================================
    0x4c: v4c(0x40) = CONST 
    0x4e: v4e = MLOAD v4c(0x40)
    0x4f: v4f(0xa0) = CONST 
    0x52: v52(0x17c3) = CONST 
    0x56: CODECOPY v4e, v52(0x17c3), v4f(0xa0)
    0x58: v58 = ADD v4e, v4f(0xa0)
    0x59: v59(0x40) = CONST 
    0x5d: MSTORE v59(0x40), v58
    0x5f: v5f = MLOAD v4e
    0x60: v60(0x20) = CONST 
    0x63: v63 = ADD v4e, v60(0x20)
    0x64: v64 = MLOAD v63
    0x67: v67 = ADD v4e, v59(0x40)
    0x68: v68 = MLOAD v67
    0x69: v69(0x60) = CONST 
    0x6c: v6c = ADD v4e, v69(0x60)
    0x6d: v6d = MLOAD v6c
    0x6e: v6e(0x80) = CONST 
    0x72: v72 = ADD v4e, v6e(0x80)
    0x73: v73 = MLOAD v72
    0x79: v79(0x0) = CONST 
    0x80: v80(0x1) = CONST 
    0x82: v82(0xa0) = CONST 
    0x84: v84(0x2) = CONST 
    0x86: v86(0x10000000000000000000000000000000000000000) = EXP v84(0x2), v82(0xa0)
    0x87: v87(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86(0x10000000000000000000000000000000000000000), v80(0x1)
    0x89: v89 = AND v5f, v87(0xffffffffffffffffffffffffffffffffffffffff)
    0x8a: v8a = ISZERO v89
    0x8b: v8b = ISZERO v8a
    0x8c: v8c(0x92) = CONST 
    0x8f: JUMPI v8c(0x92), v8b

    Begin block 0x92
    prev=[0x4a, 0x90], succ=[]
    =================================
    0x92_0x0: v92_0 = PHI v5f, v91
    0x93: v93(0x0) = CONST 
    0x96: v96 = SLOAD v93(0x0)
    0x97: v97(0x1) = CONST 
    0x99: v99(0xa0) = CONST 
    0x9b: v9b(0x2) = CONST 
    0x9d: v9d(0x10000000000000000000000000000000000000000) = EXP v9b(0x2), v99(0xa0)
    0x9e: v9e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9d(0x10000000000000000000000000000000000000000), v97(0x1)
    0xa1: va1 = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v92_0
    0xa2: va2(0x1) = CONST 
    0xa4: va4(0xa0) = CONST 
    0xa6: va6(0x2) = CONST 
    0xa8: va8(0x10000000000000000000000000000000000000000) = EXP va6(0x2), va4(0xa0)
    0xa9: va9(0xffffffffffffffffffffffffffffffffffffffff) = SUB va8(0x10000000000000000000000000000000000000000), va2(0x1)
    0xaa: vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va9(0xffffffffffffffffffffffffffffffffffffffff)
    0xad: vad = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v96
    0xae: vae = OR vad, va1
    0xb0: SSTORE v93(0x0), vae
    0xb1: vb1(0x4) = CONST 
    0xb4: vb4 = SLOAD vb1(0x4)
    0xb5: vb5(0xff) = CONST 
    0xb7: vb7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vb5(0xff)
    0xb8: vb8 = AND vb7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vb4
    0xba: SSTORE vb1(0x4), vb8
    0xbb: vbb(0xd) = CONST 
    0xbe: vbe = SLOAD vbb(0xd)
    0xc0: vc0 = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbe
    0xc3: vc3(0x0) = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v79(0x0)
    0xc7: vc7 = OR vc3(0x0), vc0
    0xca: SSTORE vbb(0xd), vc7
    0xcb: vcb(0xe) = CONST 
    0xce: vce = SLOAD vcb(0xe)
    0xd0: vd0 = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vce
    0xd3: vd3 = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v64
    0xd7: vd7 = OR vd3, vd0
    0xda: SSTORE vcb(0xe), vd7
    0xdb: vdb(0xa) = CONST 
    0xde: vde = SLOAD vdb(0xa)
    0xe0: ve0 = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vde
    0xe3: ve3 = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v68
    0xe7: ve7 = OR ve3, ve0
    0xea: SSTORE vdb(0xa), ve7
    0xeb: veb(0xb) = CONST 
    0xee: vee = SLOAD veb(0xb)
    0xf0: vf0 = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vee
    0xf3: vf3 = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v6d
    0xf7: vf7 = OR vf3, vf0
    0xfa: SSTORE veb(0xb), vf7
    0xfb: vfb(0xc) = CONST 
    0xfe: vfe = SLOAD vfb(0xc)
    0x101: v101 = AND vaa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vfe
    0x103: v103 = AND v9e(0xffffffffffffffffffffffffffffffffffffffff), v73
    0x104: v104 = OR v103, v101
    0x107: SSTORE vfb(0xc), v104
    0x108: v108(0x16a5) = CONST 
    0x110: v110(0x11e) = CONST 
    0x119: CODECOPY v93(0x0), v110(0x11e), v108(0x16a5)
    0x11a: v11a(0x0) = CONST 
    0x11c: RETURN v11a(0x0), v108(0x16a5)

    Begin block 0x90
    prev=[0x4a], succ=[0x92]
    =================================
    0x91: v91 = CALLER 

}

