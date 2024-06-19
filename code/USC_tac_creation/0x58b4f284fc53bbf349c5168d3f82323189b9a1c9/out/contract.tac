function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xb6, 0xba]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f) = CONST 
    0x1a: v1a(0x1) = CONST 
    0x1c: v1c(0x0) = CONST 
    0x1e: v1e(0x100) = CONST 
    0x21: v21(0x1) = EXP v1e(0x100), v1c(0x0)
    0x23: v23 = SLOAD v1a(0x1)
    0x25: v25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a: v3a(0xffffffffffffffffffffffffffffffffffffffff) = MUL v25(0xffffffffffffffffffffffffffffffffffffffff), v21(0x1)
    0x3b: v3b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3a(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c: v3c = AND v3b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v23
    0x3f: v3f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x54: v54(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f) = AND v3f(0xffffffffffffffffffffffffffffffffffffffff), v5(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f)
    0x55: v55(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f) = MUL v54(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f), v21(0x1)
    0x56: v56 = OR v55(0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f), v3c
    0x58: SSTORE v1a(0x1), v56
    0x5a: v5a(0x7a250d5630b4cf539739df2c5dacb4c659f2488d) = CONST 
    0x6f: v6f(0x2) = CONST 
    0x71: v71(0x0) = CONST 
    0x73: v73(0x100) = CONST 
    0x76: v76(0x1) = EXP v73(0x100), v71(0x0)
    0x78: v78 = SLOAD v6f(0x2)
    0x7a: v7a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8f: v8f(0xffffffffffffffffffffffffffffffffffffffff) = MUL v7a(0xffffffffffffffffffffffffffffffffffffffff), v76(0x1)
    0x90: v90(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v8f(0xffffffffffffffffffffffffffffffffffffffff)
    0x91: v91 = AND v90(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v78
    0x94: v94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa9: va9(0x7a250d5630b4cf539739df2c5dacb4c659f2488d) = AND v94(0xffffffffffffffffffffffffffffffffffffffff), v5a(0x7a250d5630b4cf539739df2c5dacb4c659f2488d)
    0xaa: vaa(0x7a250d5630b4cf539739df2c5dacb4c659f2488d) = MUL va9(0x7a250d5630b4cf539739df2c5dacb4c659f2488d), v76(0x1)
    0xab: vab = OR vaa(0x7a250d5630b4cf539739df2c5dacb4c659f2488d), v91
    0xad: SSTORE v6f(0x2), vab
    0xaf: vaf = CALLVALUE 
    0xb1: vb1 = ISZERO vaf
    0xb2: vb2(0xba) = CONST 
    0xb5: JUMPI vb2(0xba), vb1

    Begin block 0xb6
    prev=[0x0], succ=[]
    =================================
    0xb6: vb6(0x0) = CONST 
    0xb9: REVERT vb6(0x0), vb6(0x0)

    Begin block 0xba
    prev=[0x0], succ=[0x16f]
    =================================
    0xbc: vbc(0x0) = CONST 
    0xbe: vbe(0xcb) = CONST 
    0xc1: vc1(0x16f) = CONST 
    0xc4: vc4(0x20) = CONST 
    0xc6: vc6(0x16f00000000) = SHL vc4(0x20), vc1(0x16f)
    0xc7: vc7(0x20) = CONST 
    0xc9: vc9(0x16f) = SHR vc7(0x20), vc6(0x16f00000000)
    0xca: JUMP vc9(0x16f)

    Begin block 0x16f
    prev=[0xba], succ=[0xcb]
    =================================
    0x170: v170(0x0) = CONST 
    0x172: v172 = CALLER 
    0x176: JUMP vbe(0xcb)

    Begin block 0xcb
    prev=[0x16f], succ=[0x177]
    =================================
    0xcf: vcf(0x4) = CONST 
    0xd1: vd1(0x0) = CONST 
    0xd3: vd3(0x100) = CONST 
    0xd6: vd6(0x1) = EXP vd3(0x100), vd1(0x0)
    0xd8: vd8 = SLOAD vcf(0x4)
    0xda: vda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xef: vef(0xffffffffffffffffffffffffffffffffffffffff) = MUL vda(0xffffffffffffffffffffffffffffffffffffffff), vd6(0x1)
    0xf0: vf0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vef(0xffffffffffffffffffffffffffffffffffffffff)
    0xf1: vf1 = AND vf0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd8
    0xf4: vf4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x109: v109 = AND vf4(0xffffffffffffffffffffffffffffffffffffffff), v172
    0x10a: v10a = MUL v109, vd6(0x1)
    0x10b: v10b = OR v10a, vf1
    0x10d: SSTORE vcf(0x4), v10b
    0x110: v110(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x125: v125 = AND v110(0xffffffffffffffffffffffffffffffffffffffff), v172
    0x126: v126(0x0) = CONST 
    0x128: v128(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13d: v13d(0x0) = AND v128(0xffffffffffffffffffffffffffffffffffffffff), v126(0x0)
    0x13e: v13e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x15f: v15f(0x40) = CONST 
    0x161: v161 = MLOAD v15f(0x40)
    0x162: v162(0x40) = CONST 
    0x164: v164 = MLOAD v162(0x40)
    0x167: v167(0x0) = SUB v161, v164
    0x169: LOG3 v164, v167(0x0), v13e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v13d(0x0), v125
    0x16b: v16b(0x177) = CONST 
    0x16e: JUMP v16b(0x177)

    Begin block 0x177
    prev=[0xcb], succ=[]
    =================================
    0x178: v178(0xcc2) = CONST 
    0x17c: v17c(0x186) = CONST 
    0x17f: v17f(0x0) = CONST 
    0x181: CODECOPY v17f(0x0), v17c(0x186), v178(0xcc2)
    0x182: v182(0x0) = CONST 
    0x184: RETURN v182(0x0), v178(0xcc2)

}

