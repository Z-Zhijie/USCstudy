function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xca, 0xce]
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
    0xf: vf(0xc) = CONST 
    0x12: v12 = SLOAD vf(0xc)
    0x13: v13(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac50000000000) = CONST 
    0x2d: v2d(0x1) = CONST 
    0x2f: v2f(0x28) = CONST 
    0x31: v31(0x10000000000) = SHL v2f(0x28), v2d(0x1)
    0x32: v32(0x1) = CONST 
    0x34: v34(0xc8) = CONST 
    0x36: v36(0x100000000000000000000000000000000000000000000000000) = SHL v34(0xc8), v32(0x1)
    0x37: v37(0xffffffffffffffffffffffffffffffffffffffff0000000000) = SUB v36(0x100000000000000000000000000000000000000000000000000), v31(0x10000000000)
    0x38: v38(0xffffffffffffff0000000000000000000000000000000000000000ffffffffff) = NOT v37(0xffffffffffffffffffffffffffffffffffffffff0000000000)
    0x3b: v3b = AND v12, v38(0xffffffffffffff0000000000000000000000000000000000000000ffffffffff)
    0x3c: v3c = OR v3b, v13(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac50000000000)
    0x3e: SSTORE vf(0xc), v3c
    0x3f: v3f(0xd) = CONST 
    0x42: v42 = SLOAD v3f(0xd)
    0x43: v43(0x1) = CONST 
    0x45: v45(0x1) = CONST 
    0x47: v47(0xa0) = CONST 
    0x49: v49(0x10000000000000000000000000000000000000000) = SHL v47(0xa0), v45(0x1)
    0x4a: v4a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49(0x10000000000000000000000000000000000000000), v43(0x1)
    0x4b: v4b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4a(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e: v4e = AND v4b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v42
    0x4f: v4f(0x60d70df1c783b1e5489721c443465684e2756555) = CONST 
    0x64: v64 = OR v4f(0x60d70df1c783b1e5489721c443465684e2756555), v4e
    0x67: SSTORE v3f(0xd), v64
    0x68: v68(0xe) = CONST 
    0x6b: v6b = SLOAD v68(0xe)
    0x6d: v6d = AND v4b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6b
    0x6e: v6e(0x868f7622f57b62330db8b282044d7eaf067facfe) = CONST 
    0x83: v83 = OR v6e(0x868f7622f57b62330db8b282044d7eaf067facfe), v6d
    0x85: SSTORE v68(0xe), v83
    0x86: v86(0xf) = CONST 
    0x89: v89 = SLOAD v86(0xf)
    0x8b: v8b = AND v4b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v89
    0x8c: v8c(0xd66a9d2b706e225204f475c9e70a4c09eea62199) = CONST 
    0xa1: va1 = OR v8c(0xd66a9d2b706e225204f475c9e70a4c09eea62199), v8b
    0xa3: SSTORE v86(0xf), va1
    0xa4: va4(0x10) = CONST 
    0xa7: va7 = SLOAD va4(0x10)
    0xaa: vaa = AND v4b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va7
    0xab: vab(0x66bfd3ed6618d9c62dcf1ef706d9aacd5fdbccd6) = CONST 
    0xc0: vc0 = OR vab(0x66bfd3ed6618d9c62dcf1ef706d9aacd5fdbccd6), vaa
    0xc2: SSTORE va4(0x10), vc0
    0xc3: vc3 = CALLVALUE 
    0xc5: vc5 = ISZERO vc3
    0xc6: vc6(0xce) = CONST 
    0xc9: JUMPI vc6(0xce), vc5

    Begin block 0xca
    prev=[0x0], succ=[]
    =================================
    0xca: vca(0x0) = CONST 
    0xcd: REVERT vca(0x0), vca(0x0)

    Begin block 0xce
    prev=[0x0], succ=[]
    =================================
    0xd0: vd0(0x2127) = CONST 
    0xd4: vd4(0xde) = CONST 
    0xd7: vd7(0x0) = CONST 
    0xd9: CODECOPY vd7(0x0), vd4(0xde), vd0(0x2127)
    0xda: vda(0x0) = CONST 
    0xdc: RETURN vda(0x0), vd0(0x2127)

}

