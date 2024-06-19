function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x80]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x13) = CONST 
    0x8: v8 = CALLER 
    0x9: v9(0x80) = CONST 
    0xc: vc(0x20) = CONST 
    0xe: ve(0x8000000000) = SHL vc(0x20), v9(0x80)
    0xf: vf(0x20) = CONST 
    0x11: v11(0x80) = SHR vf(0x20), ve(0x8000000000)
    0x12: JUMP v11(0x80)

    Begin block 0x80
    prev=[0x0], succ=[0x13]
    =================================
    0x81: v81(0x0) = CONST 
    0x83: v83(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa4: va4(0x0) = CONST 
    0xa6: va6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va4(0x0), v83(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xab: SSTORE va6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v8
    0xae: JUMP v5(0x13)

    Begin block 0x13
    prev=[0x80], succ=[0xaf]
    =================================
    0x14: v14(0x21) = CONST 
    0x17: v17(0xaf) = CONST 
    0x1a: v1a(0x20) = CONST 
    0x1c: v1c(0xaf00000000) = SHL v1a(0x20), v17(0xaf)
    0x1d: v1d(0x20) = CONST 
    0x1f: v1f(0xaf) = SHR v1d(0x20), v1c(0xaf00000000)
    0x20: JUMP v1f(0xaf)

    Begin block 0xaf
    prev=[0x13], succ=[0x21]
    =================================
    0xb0: vb0(0x0) = CONST 
    0xb3: vb3(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xd4: vd4(0x0) = CONST 
    0xd6: vd6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL vd4(0x0), vb3(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xda: vda = SLOAD vd6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xdf: JUMP v14(0x21)

    Begin block 0x21
    prev=[0xaf], succ=[0xe0]
    =================================
    0x22: v22(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x37: v37 = AND v22(0xffffffffffffffffffffffffffffffffffffffff), vda
    0x38: v38(0x0) = CONST 
    0x3a: v3a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4f: v4f(0x0) = AND v3a(0xffffffffffffffffffffffffffffffffffffffff), v38(0x0)
    0x50: v50(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x71: v71(0x40) = CONST 
    0x73: v73 = MLOAD v71(0x40)
    0x74: v74(0x40) = CONST 
    0x76: v76 = MLOAD v74(0x40)
    0x79: v79(0x0) = SUB v73, v76
    0x7b: LOG3 v76, v79(0x0), v50(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v4f(0x0), v37
    0x7c: v7c(0xe0) = CONST 
    0x7f: JUMP v7c(0xe0)

    Begin block 0xe0
    prev=[0x21], succ=[]
    =================================
    0xe1: ve1(0xd5e) = CONST 
    0xe5: ve5(0xef) = CONST 
    0xe8: ve8(0x0) = CONST 
    0xea: CODECOPY ve8(0x0), ve5(0xef), ve1(0xd5e)
    0xeb: veb(0x0) = CONST 
    0xed: RETURN veb(0x0), ve1(0xd5e)

}

