function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1e, 0x22]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x8: v8 = SLOAD v5(0x1)
    0x9: v9(0xa0) = CONST 
    0xb: vb(0x2) = CONST 
    0xd: vd(0x10000000000000000000000000000000000000000) = EXP vb(0x2), v9(0xa0)
    0xe: ve(0xffff) = CONST 
    0x11: v11(0xffff0000000000000000000000000000000000000000) = MUL ve(0xffff), vd(0x10000000000000000000000000000000000000000)
    0x12: v12(0xffffffffffffffffffff0000ffffffffffffffffffffffffffffffffffffffff) = NOT v11(0xffff0000000000000000000000000000000000000000)
    0x13: v13 = AND v12(0xffffffffffffffffffff0000ffffffffffffffffffffffffffffffffffffffff), v8
    0x15: SSTORE v5(0x1), v13
    0x16: v16 = CALLVALUE 
    0x18: v18 = ISZERO v16
    0x19: v19(0x22) = CONST 
    0x1d: JUMPI v19(0x22), v18

    Begin block 0x1e
    prev=[0x0], succ=[]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x21: REVERT v1e(0x0), v1e(0x0)

    Begin block 0x22
    prev=[0x0], succ=[0x111]
    =================================
    0x24: v24(0x40) = CONST 
    0x26: v26 = MLOAD v24(0x40)
    0x27: v27(0x20) = CONST 
    0x2a: v2a(0x5a35) = CONST 
    0x31: v31 = ADD v5a58(0x0000000000000000000000000000000000000000000000000000000000000000), v26
    0x32: v32(0x40) = CONST 
    0x34: MSTORE v32(0x40), v31
    0x35: v35 = MLOAD v5a58(0x0000000000000000000000000000000000000000000000000000000000000000)
    0x36: v36(0x0) = CONST 
    0x39: v39 = SLOAD v36(0x0)
    0x3a: v3a = CALLER 
    0x3b: v3b(0x1) = CONST 
    0x3d: v3d(0xa0) = CONST 
    0x3f: v3f(0x2) = CONST 
    0x41: v41(0x10000000000000000000000000000000000000000) = EXP v3f(0x2), v3d(0xa0)
    0x42: v42(0xffffffffffffffffffffffffffffffffffffffff) = SUB v41(0x10000000000000000000000000000000000000000), v3b(0x1)
    0x43: v43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v42(0xffffffffffffffffffffffffffffffffffffffff)
    0x46: v46 = AND v43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v39
    0x47: v47 = OR v46, v3a
    0x4a: SSTORE v36(0x0), v47
    0x4b: v4b(0x1) = CONST 
    0x4e: v4e = SLOAD v4b(0x1)
    0x50: v50 = AND v43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v4e
    0x52: SSTORE v4b(0x1), v50
    0x53: v53(0x3) = CONST 
    0x56: v56 = SLOAD v53(0x3)
    0x59: v59 = AND v43(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v56
    0x5a: v5a(0x1) = CONST 
    0x5c: v5c(0xa0) = CONST 
    0x5e: v5e(0x2) = CONST 
    0x60: v60(0x10000000000000000000000000000000000000000) = EXP v5e(0x2), v5c(0xa0)
    0x61: v61(0xffffffffffffffffffffffffffffffffffffffff) = SUB v60(0x10000000000000000000000000000000000000000), v5a(0x1)
    0x63: v63 = AND v35, v61(0xffffffffffffffffffffffffffffffffffffffff)
    0x64: v64 = OR v63, v59
    0x66: SSTORE v53(0x3), v64
    0x69: v69(0x72) = CONST 
    0x6d: v6d(0x111) = CONST 
    0x71: JUMP v6d(0x111)
    0x5a58: v5a58(0x0000000000000000000000000000000000000000000000000000000000000000) = CONST 

    Begin block 0x111
    prev=[0x22], succ=[0x72]
    =================================
    0x112: v112(0x40) = CONST 
    0x114: v114 = MLOAD v112(0x40)
    0x115: v115(0x718) = CONST 
    0x119: v119(0x4c1e) = CONST 
    0x11e: CODECOPY v114, v119(0x4c1e), v115(0x718)
    0x11f: v11f = ADD v115(0x718), v114
    0x121: JUMP v69(0x72)

    Begin block 0x72
    prev=[0x111], succ=[0x86, 0x8f]
    =================================
    0x73: v73(0x40) = CONST 
    0x75: v75 = MLOAD v73(0x40)
    0x78: v78(0x718) = SUB v11f, v75
    0x7a: v7a(0x0) = CONST 
    0x7c: v7c = CREATE v7a(0x0), v75, v78(0x718)
    0x7e: v7e = ISZERO v7c
    0x80: v80 = ISZERO v7e
    0x81: v81(0x8f) = CONST 
    0x85: JUMPI v81(0x8f), v80

    Begin block 0x86
    prev=[0x72], succ=[]
    =================================
    0x86: v86 = RETURNDATASIZE 
    0x87: v87(0x0) = CONST 
    0x8a: RETURNDATACOPY v87(0x0), v87(0x0), v86
    0x8b: v8b = RETURNDATASIZE 
    0x8c: v8c(0x0) = CONST 
    0x8e: REVERT v8c(0x0), v8b

    Begin block 0x8f
    prev=[0x72], succ=[0x122]
    =================================
    0x91: v91(0x2) = CONST 
    0x94: v94 = SLOAD v91(0x2)
    0x95: v95(0x1) = CONST 
    0x97: v97(0xa0) = CONST 
    0x99: v99(0x2) = CONST 
    0x9b: v9b(0x10000000000000000000000000000000000000000) = EXP v99(0x2), v97(0xa0)
    0x9c: v9c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9b(0x10000000000000000000000000000000000000000), v95(0x1)
    0x9d: v9d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v9c(0xffffffffffffffffffffffffffffffffffffffff)
    0xa0: va0 = AND v9d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v94
    0xa1: va1(0x1) = CONST 
    0xa3: va3(0xa0) = CONST 
    0xa5: va5(0x2) = CONST 
    0xa7: va7(0x10000000000000000000000000000000000000000) = EXP va5(0x2), va3(0xa0)
    0xa8: va8(0xffffffffffffffffffffffffffffffffffffffff) = SUB va7(0x10000000000000000000000000000000000000000), va1(0x1)
    0xab: vab = AND va8(0xffffffffffffffffffffffffffffffffffffffff), v7c
    0xac: vac = OR vab, va0
    0xaf: SSTORE v91(0x2), vac
    0xb0: vb0(0x3) = CONST 
    0xb3: vb3 = SLOAD vb0(0x3)
    0xb6: vb6 = AND v9d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb3
    0xb9: vb9 = AND v35, va8(0xffffffffffffffffffffffffffffffffffffffff)
    0xbd: vbd = OR vb9, vb6
    0xbf: SSTORE vb0(0x3), vbd
    0xc1: vc1(0xca) = CONST 
    0xc5: vc5(0x122) = CONST 
    0xc9: JUMP vc5(0x122)

    Begin block 0x122
    prev=[0x8f], succ=[0xca]
    =================================
    0x123: v123(0x40) = CONST 
    0x125: v125 = MLOAD v123(0x40)
    0x126: v126(0x6ff) = CONST 
    0x12a: v12a(0x5336) = CONST 
    0x12f: CODECOPY v125, v12a(0x5336), v126(0x6ff)
    0x130: v130 = ADD v126(0x6ff), v125
    0x132: JUMP vc1(0xca)

    Begin block 0xca
    prev=[0x122], succ=[0xde, 0xe7]
    =================================
    0xcb: vcb(0x40) = CONST 
    0xcd: vcd = MLOAD vcb(0x40)
    0xd0: vd0(0x6ff) = SUB v130, vcd
    0xd2: vd2(0x0) = CONST 
    0xd4: vd4 = CREATE vd2(0x0), vcd, vd0(0x6ff)
    0xd6: vd6 = ISZERO vd4
    0xd8: vd8 = ISZERO vd6
    0xd9: vd9(0xe7) = CONST 
    0xdd: JUMPI vd9(0xe7), vd8

    Begin block 0xde
    prev=[0xca], succ=[]
    =================================
    0xde: vde = RETURNDATASIZE 
    0xdf: vdf(0x0) = CONST 
    0xe2: RETURNDATACOPY vdf(0x0), vdf(0x0), vde
    0xe3: ve3 = RETURNDATASIZE 
    0xe4: ve4(0x0) = CONST 
    0xe6: REVERT ve4(0x0), ve3

    Begin block 0xe7
    prev=[0xca], succ=[0x133]
    =================================
    0xe9: ve9(0x4) = CONST 
    0xec: vec = SLOAD ve9(0x4)
    0xed: ved(0x1) = CONST 
    0xef: vef(0xa0) = CONST 
    0xf1: vf1(0x2) = CONST 
    0xf3: vf3(0x10000000000000000000000000000000000000000) = EXP vf1(0x2), vef(0xa0)
    0xf4: vf4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf3(0x10000000000000000000000000000000000000000), ved(0x1)
    0xf5: vf5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vf4(0xffffffffffffffffffffffffffffffffffffffff)
    0xf6: vf6 = AND vf5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vec
    0xf7: vf7(0x1) = CONST 
    0xf9: vf9(0xa0) = CONST 
    0xfb: vfb(0x2) = CONST 
    0xfd: vfd(0x10000000000000000000000000000000000000000) = EXP vfb(0x2), vf9(0xa0)
    0xfe: vfe(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfd(0x10000000000000000000000000000000000000000), vf7(0x1)
    0x102: v102 = AND vfe(0xffffffffffffffffffffffffffffffffffffffff), vd4
    0x106: v106 = OR v102, vf6
    0x108: SSTORE ve9(0x4), v106
    0x10a: v10a(0x133) = CONST 
    0x110: JUMP v10a(0x133)

    Begin block 0x133
    prev=[0xe7], succ=[]
    =================================
    0x134: v134(0x4adb) = CONST 
    0x138: v138(0x143) = CONST 
    0x13c: v13c(0x0) = CONST 
    0x13e: CODECOPY v13c(0x0), v138(0x143), v134(0x4adb)
    0x13f: v13f(0x0) = CONST 
    0x141: RETURN v13f(0x0), v134(0x4adb)

}

