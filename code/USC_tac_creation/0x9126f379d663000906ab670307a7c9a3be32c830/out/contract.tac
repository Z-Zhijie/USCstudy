function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x9a, 0x9e]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9(0xff)
    0xc: vc = AND vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8
    0xe: SSTORE v5(0x0), vc
    0xf: vf(0x5) = CONST 
    0x12: v12 = SLOAD vf(0x5)
    0x13: v13(0x1) = CONST 
    0x15: v15(0x1) = CONST 
    0x17: v17(0xa0) = CONST 
    0x19: v19(0x10000000000000000000000000000000000000000) = SHL v17(0xa0), v15(0x1)
    0x1a: v1a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19(0x10000000000000000000000000000000000000000), v13(0x1)
    0x1b: v1b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e: v1e = AND v1b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12
    0x1f: v1f(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac5) = CONST 
    0x34: v34 = OR v1f(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac5), v1e
    0x37: SSTORE vf(0x5), v34
    0x38: v38(0x6) = CONST 
    0x3b: v3b = SLOAD v38(0x6)
    0x3d: v3d = AND v1b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3b
    0x3e: v3e(0x60d70df1c783b1e5489721c443465684e2756555) = CONST 
    0x53: v53 = OR v3e(0x60d70df1c783b1e5489721c443465684e2756555), v3d
    0x55: SSTORE v38(0x6), v53
    0x56: v56(0x7) = CONST 
    0x59: v59 = SLOAD v56(0x7)
    0x5b: v5b = AND v1b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v59
    0x5c: v5c(0xd66a9d2b706e225204f475c9e70a4c09eea62199) = CONST 
    0x71: v71 = OR v5c(0xd66a9d2b706e225204f475c9e70a4c09eea62199), v5b
    0x73: SSTORE v56(0x7), v71
    0x74: v74(0x8) = CONST 
    0x77: v77 = SLOAD v74(0x8)
    0x7a: v7a = AND v1b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v77
    0x7b: v7b(0x868f7622f57b62330db8b282044d7eaf067facfe) = CONST 
    0x90: v90 = OR v7b(0x868f7622f57b62330db8b282044d7eaf067facfe), v7a
    0x92: SSTORE v74(0x8), v90
    0x93: v93 = CALLVALUE 
    0x95: v95 = ISZERO v93
    0x96: v96(0x9e) = CONST 
    0x99: JUMPI v96(0x9e), v95

    Begin block 0x9a
    prev=[0x0], succ=[]
    =================================
    0x9a: v9a(0x0) = CONST 
    0x9d: REVERT v9a(0x0), v9a(0x0)

    Begin block 0x9e
    prev=[0x0], succ=[]
    =================================
    0xa0: va0(0x1d52) = CONST 
    0xa4: va4(0xae) = CONST 
    0xa7: va7(0x0) = CONST 
    0xa9: CODECOPY va7(0x0), va4(0xae), va0(0x1d52)
    0xaa: vaa(0x0) = CONST 
    0xac: RETURN vaa(0x0), va0(0x1d52)

}

