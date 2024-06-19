function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x13f]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x7: v7(0x37) = CONST 
    0x9: v9(0x14) = CONST 
    0xb: vb(0x100) = CONST 
    0xe: ve(0x10000000000000000000000000000000000000000) = EXP vb(0x100), v9(0x14)
    0x10: v10 = SLOAD v7(0x37)
    0x12: v12(0xff) = CONST 
    0x14: v14(0xff0000000000000000000000000000000000000000) = MUL v12(0xff), ve(0x10000000000000000000000000000000000000000)
    0x15: v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v14(0xff0000000000000000000000000000000000000000)
    0x16: v16 = AND v15(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v10
    0x19: v19(0x1) = ISZERO v5(0x0)
    0x1a: v1a(0x0) = ISZERO v19(0x1)
    0x1b: v1b(0x0) = MUL v1a(0x0), ve(0x10000000000000000000000000000000000000000)
    0x1c: v1c = OR v1b(0x0), v16
    0x1e: SSTORE v7(0x37), v1c
    0x20: v20(0x1) = CONST 
    0x22: v22(0x37) = CONST 
    0x24: v24(0x15) = CONST 
    0x26: v26(0x100) = CONST 
    0x29: v29(0x1000000000000000000000000000000000000000000) = EXP v26(0x100), v24(0x15)
    0x2b: v2b = SLOAD v22(0x37)
    0x2d: v2d(0xff) = CONST 
    0x2f: v2f(0xff000000000000000000000000000000000000000000) = MUL v2d(0xff), v29(0x1000000000000000000000000000000000000000000)
    0x30: v30(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v2f(0xff000000000000000000000000000000000000000000)
    0x31: v31 = AND v30(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v2b
    0x34: v34(0x0) = ISZERO v20(0x1)
    0x35: v35(0x1) = ISZERO v34(0x0)
    0x36: v36(0x1000000000000000000000000000000000000000000) = MUL v35(0x1), v29(0x1000000000000000000000000000000000000000000)
    0x37: v37 = OR v36(0x1000000000000000000000000000000000000000000), v31
    0x39: SSTORE v22(0x37), v37
    0x3b: v3b(0x0) = CONST 
    0x3d: v3d(0x3d) = CONST 
    0x3f: v3f(0x0) = CONST 
    0x41: v41(0x100) = CONST 
    0x44: v44(0x1) = EXP v41(0x100), v3f(0x0)
    0x46: v46 = SLOAD v3d(0x3d)
    0x48: v48(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5d: v5d(0xffffffffffffffffffffffffffffffffffffffff) = MUL v48(0xffffffffffffffffffffffffffffffffffffffff), v44(0x1)
    0x5e: v5e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5d(0xffffffffffffffffffffffffffffffffffffffff)
    0x5f: v5f = AND v5e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v46
    0x62: v62(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x77: v77(0x0) = AND v62(0xffffffffffffffffffffffffffffffffffffffff), v3b(0x0)
    0x78: v78(0x0) = MUL v77(0x0), v44(0x1)
    0x79: v79 = OR v78(0x0), v5f
    0x7b: SSTORE v3d(0x3d), v79
    0x7d: v7d(0x0) = CONST 
    0x7f: v7f(0x3e) = CONST 
    0x81: v81(0x0) = CONST 
    0x83: v83(0x100) = CONST 
    0x86: v86(0x1) = EXP v83(0x100), v81(0x0)
    0x88: v88 = SLOAD v7f(0x3e)
    0x8a: v8a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9f: v9f(0xffffffffffffffffffffffffffffffffffffffff) = MUL v8a(0xffffffffffffffffffffffffffffffffffffffff), v86(0x1)
    0xa0: va0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v9f(0xffffffffffffffffffffffffffffffffffffffff)
    0xa1: va1 = AND va0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v88
    0xa4: va4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb9: vb9(0x0) = AND va4(0xffffffffffffffffffffffffffffffffffffffff), v7d(0x0)
    0xba: vba(0x0) = MUL vb9(0x0), v86(0x1)
    0xbb: vbb = OR vba(0x0), va1
    0xbd: SSTORE v7f(0x3e), vbb
    0xbf: vbf(0xcf) = CONST 
    0xc3: vc3 = CALLER 
    0xc4: vc4(0x13f) = CONST 
    0xc8: vc8(0x20) = CONST 
    0xca: vca(0x13f00000000) = SHL vc8(0x20), vc4(0x13f)
    0xcb: vcb(0x20) = CONST 
    0xcd: vcd(0x13f) = SHR vcb(0x20), vca(0x13f00000000)
    0xce: JUMP vcd(0x13f)

    Begin block 0x13f
    prev=[0x0], succ=[0xcf]
    =================================
    0x140: v140(0x0) = CONST 
    0x142: v142(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x163: v163(0x0) = CONST 
    0x165: v165(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL v163(0x0), v142(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x16a: SSTORE v165(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), vc3
    0x16d: JUMP vbf(0xcf)

    Begin block 0xcf
    prev=[0x13f], succ=[0x16e]
    =================================
    0xd0: vd0(0xdf) = CONST 
    0xd4: vd4(0x16e) = CONST 
    0xd8: vd8(0x20) = CONST 
    0xda: vda(0x16e00000000) = SHL vd8(0x20), vd4(0x16e)
    0xdb: vdb(0x20) = CONST 
    0xdd: vdd(0x16e) = SHR vdb(0x20), vda(0x16e00000000)
    0xde: JUMP vdd(0x16e)

    Begin block 0x16e
    prev=[0xcf], succ=[0xdf]
    =================================
    0x16f: v16f(0x0) = CONST 
    0x172: v172(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x193: v193(0x0) = CONST 
    0x195: v195(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL v193(0x0), v172(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x199: v199 = SLOAD v195(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x19e: JUMP vd0(0xdf)

    Begin block 0xdf
    prev=[0x16e], succ=[0x19f]
    =================================
    0xe0: ve0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf5: vf5 = AND ve0(0xffffffffffffffffffffffffffffffffffffffff), v199
    0xf6: vf6(0x0) = CONST 
    0xf8: vf8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10d: v10d(0x0) = AND vf8(0xffffffffffffffffffffffffffffffffffffffff), vf6(0x0)
    0x10e: v10e(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x12f: v12f(0x40) = CONST 
    0x131: v131 = MLOAD v12f(0x40)
    0x132: v132(0x40) = CONST 
    0x134: v134 = MLOAD v132(0x40)
    0x137: v137(0x0) = SUB v131, v134
    0x139: LOG3 v134, v137(0x0), v10e(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v10d(0x0), vf5
    0x13a: v13a(0x19f) = CONST 
    0x13e: JUMP v13a(0x19f)

    Begin block 0x19f
    prev=[0xdf], succ=[]
    =================================
    0x1a0: v1a0(0x4b64) = CONST 
    0x1a4: v1a4(0x1af) = CONST 
    0x1a8: v1a8(0x0) = CONST 
    0x1aa: CODECOPY v1a8(0x0), v1a4(0x1af), v1a0(0x4b64)
    0x1ab: v1ab(0x0) = CONST 
    0x1ad: RETURN v1ab(0x0), v1a0(0x4b64)

}

