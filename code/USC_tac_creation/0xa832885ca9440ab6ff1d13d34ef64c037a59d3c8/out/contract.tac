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
    prev=[0x0], succ=[0xdc]
    =================================
    0x24: v24(0x40) = CONST 
    0x26: v26 = MLOAD v24(0x40)
    0x27: v27(0x40) = CONST 
    0x2a: v2a(0x37ca) = CONST 
    0x2f: CODECOPY v26, v2a(0x37ca), v27(0x40)
    0x31: v31 = ADD v26, v27(0x40)
    0x32: v32(0x40) = CONST 
    0x34: MSTORE v32(0x40), v31
    0x36: v36 = MLOAD v26
    0x37: v37(0x20) = CONST 
    0x3b: v3b = ADD v26, v37(0x20)
    0x3c: v3c = MLOAD v3b
    0x3d: v3d(0x0) = CONST 
    0x40: v40 = SLOAD v3d(0x0)
    0x41: v41 = CALLER 
    0x42: v42(0x1) = CONST 
    0x44: v44(0xa0) = CONST 
    0x46: v46(0x2) = CONST 
    0x48: v48(0x10000000000000000000000000000000000000000) = EXP v46(0x2), v44(0xa0)
    0x49: v49(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48(0x10000000000000000000000000000000000000000), v42(0x1)
    0x4a: v4a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v49(0xffffffffffffffffffffffffffffffffffffffff)
    0x4d: v4d = AND v4a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v40
    0x4e: v4e = OR v4d, v41
    0x51: SSTORE v3d(0x0), v4e
    0x52: v52(0x1) = CONST 
    0x55: v55 = SLOAD v52(0x1)
    0x57: v57 = AND v4a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v55
    0x59: SSTORE v52(0x1), v57
    0x5a: v5a(0x3) = CONST 
    0x5d: v5d = SLOAD v5a(0x3)
    0x60: v60 = AND v4a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5d
    0x61: v61(0x1) = CONST 
    0x63: v63(0xa0) = CONST 
    0x65: v65(0x2) = CONST 
    0x67: v67(0x10000000000000000000000000000000000000000) = EXP v65(0x2), v63(0xa0)
    0x68: v68(0xffffffffffffffffffffffffffffffffffffffff) = SUB v67(0x10000000000000000000000000000000000000000), v61(0x1)
    0x6a: v6a = AND v36, v68(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b: v6b = OR v6a, v60
    0x6d: SSTORE v5a(0x3), v6b
    0x6f: v6f(0x78) = CONST 
    0x73: v73(0xdc) = CONST 
    0x77: JUMP v73(0xdc)

    Begin block 0xdc
    prev=[0x22], succ=[0x78]
    =================================
    0xdd: vdd(0x40) = CONST 
    0xdf: vdf = MLOAD vdd(0x40)
    0xe0: ve0(0x718) = CONST 
    0xe4: ve4(0x30b2) = CONST 
    0xe9: CODECOPY vdf, ve4(0x30b2), ve0(0x718)
    0xea: vea = ADD ve0(0x718), vdf
    0xec: JUMP v6f(0x78)

    Begin block 0x78
    prev=[0xdc], succ=[0x8c, 0x95]
    =================================
    0x79: v79(0x40) = CONST 
    0x7b: v7b = MLOAD v79(0x40)
    0x7e: v7e(0x718) = SUB vea, v7b
    0x80: v80(0x0) = CONST 
    0x82: v82 = CREATE v80(0x0), v7b, v7e(0x718)
    0x84: v84 = ISZERO v82
    0x86: v86 = ISZERO v84
    0x87: v87(0x95) = CONST 
    0x8b: JUMPI v87(0x95), v86

    Begin block 0x8c
    prev=[0x78], succ=[]
    =================================
    0x8c: v8c = RETURNDATASIZE 
    0x8d: v8d(0x0) = CONST 
    0x90: RETURNDATACOPY v8d(0x0), v8d(0x0), v8c
    0x91: v91 = RETURNDATASIZE 
    0x92: v92(0x0) = CONST 
    0x94: REVERT v92(0x0), v91

    Begin block 0x95
    prev=[0x78], succ=[0xed]
    =================================
    0x97: v97(0x2) = CONST 
    0x9a: v9a = SLOAD v97(0x2)
    0x9b: v9b(0x1) = CONST 
    0x9d: v9d(0xa0) = CONST 
    0x9f: v9f(0x2) = CONST 
    0xa1: va1(0x10000000000000000000000000000000000000000) = EXP v9f(0x2), v9d(0xa0)
    0xa2: va2(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1(0x10000000000000000000000000000000000000000), v9b(0x1)
    0xa3: va3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va2(0xffffffffffffffffffffffffffffffffffffffff)
    0xa6: va6 = AND va3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v9a
    0xa7: va7(0x1) = CONST 
    0xa9: va9(0xa0) = CONST 
    0xab: vab(0x2) = CONST 
    0xad: vad(0x10000000000000000000000000000000000000000) = EXP vab(0x2), va9(0xa0)
    0xae: vae(0xffffffffffffffffffffffffffffffffffffffff) = SUB vad(0x10000000000000000000000000000000000000000), va7(0x1)
    0xb1: vb1 = AND vae(0xffffffffffffffffffffffffffffffffffffffff), v82
    0xb2: vb2 = OR vb1, va6
    0xb5: SSTORE v97(0x2), vb2
    0xb6: vb6(0x3) = CONST 
    0xb9: vb9 = SLOAD vb6(0x3)
    0xbb: vbb = AND va3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb9
    0xbe: vbe = AND vae(0xffffffffffffffffffffffffffffffffffffffff), v36
    0xc2: vc2 = OR vbe, vbb
    0xc5: SSTORE vb6(0x3), vc2
    0xc6: vc6(0x4) = CONST 
    0xc9: vc9 = SLOAD vc6(0x4)
    0xcc: vcc = AND va3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vc9
    0xce: vce = AND v3c, vae(0xffffffffffffffffffffffffffffffffffffffff)
    0xd2: vd2 = OR vce, vcc
    0xd5: SSTORE vc6(0x4), vd2
    0xd7: vd7(0xed) = CONST 
    0xdb: JUMP vd7(0xed)

    Begin block 0xed
    prev=[0x95], succ=[]
    =================================
    0xee: vee(0x2fb5) = CONST 
    0xf2: vf2(0xfd) = CONST 
    0xf6: vf6(0x0) = CONST 
    0xf8: CODECOPY vf6(0x0), vf2(0xfd), vee(0x2fb5)
    0xf9: vf9(0x0) = CONST 
    0xfb: RETURN vf9(0x0), vee(0x2fb5)

}

