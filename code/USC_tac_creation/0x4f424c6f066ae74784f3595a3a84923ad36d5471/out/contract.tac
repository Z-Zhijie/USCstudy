function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[0x28]
    =================================
    0x12: v12(0x28) = CONST 
    0x15: v15 = CALLER 
    0x16: v16(0x0) = CONST 
    0x19: v19 = MLOAD v16(0x0)
    0x1a: v1a(0x20) = CONST 
    0x1c: v1c(0x2e35) = CONST 
    0x25: MSTORE v16(0x0), v19
    0x26: SSTORE v2e59(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v15
    0x27: JUMP v12(0x28)
    0x2e59: v2e59(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

    Begin block 0x28
    prev=[0x10], succ=[]
    =================================
    0x29: v29(0x0) = CONST 
    0x2c: v2c = MLOAD v29(0x0)
    0x2d: v2d(0x20) = CONST 
    0x2f: v2f(0x2e35) = CONST 
    0x38: MSTORE v29(0x0), v2c
    0x39: v39 = SLOAD v2e5e(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x3a: v3a(0x40) = CONST 
    0x3c: v3c = MLOAD v3a(0x40)
    0x3d: v3d(0x1) = CONST 
    0x3f: v3f(0x1) = CONST 
    0x41: v41(0xa0) = CONST 
    0x43: v43(0x10000000000000000000000000000000000000000) = SHL v41(0xa0), v3f(0x1)
    0x44: v44(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43(0x10000000000000000000000000000000000000000), v3d(0x1)
    0x47: v47 = AND v39, v44(0xffffffffffffffffffffffffffffffffffffffff)
    0x49: v49(0x0) = CONST 
    0x4c: v4c(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x70: LOG3 v3c, v49(0x0), v4c(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v49(0x0), v47
    0x71: v71(0x2db5) = CONST 
    0x75: v75(0x80) = CONST 
    0x79: v79(0x0) = CONST 
    0x7b: CODECOPY v79(0x0), v75(0x80), v71(0x2db5)
    0x7c: v7c(0x0) = CONST 
    0x7e: RETURN v7c(0x0), v71(0x2db5)
    0x2e5e: v2e5e(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

}

