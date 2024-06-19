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
    prev=[0x0], succ=[0x27]
    =================================
    0x12: v12(0x27) = CONST 
    0x15: v15 = CALLER 
    0x16: v16(0x0) = CONST 
    0x19: v19 = MLOAD v16(0x0)
    0x1a: v1a(0x20) = CONST 
    0x1c: v1c(0x283c) = CONST 
    0x24: MSTORE v16(0x0), v19
    0x25: SSTORE v285d(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v15
    0x26: JUMP v12(0x27)
    0x285d: v285d(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

    Begin block 0x27
    prev=[0x10], succ=[]
    =================================
    0x28: v28(0x0) = CONST 
    0x2b: v2b = MLOAD v28(0x0)
    0x2c: v2c(0x20) = CONST 
    0x2e: v2e(0x283c) = CONST 
    0x36: MSTORE v28(0x0), v2b
    0x37: v37 = SLOAD v2862(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x38: v38(0x40) = CONST 
    0x3a: v3a = MLOAD v38(0x40)
    0x3b: v3b(0x1) = CONST 
    0x3d: v3d(0x1) = CONST 
    0x3f: v3f(0xa0) = CONST 
    0x41: v41(0x10000000000000000000000000000000000000000) = SHL v3f(0xa0), v3d(0x1)
    0x42: v42(0xffffffffffffffffffffffffffffffffffffffff) = SUB v41(0x10000000000000000000000000000000000000000), v3b(0x1)
    0x45: v45 = AND v37, v42(0xffffffffffffffffffffffffffffffffffffffff)
    0x47: v47(0x0) = CONST 
    0x4a: v4a(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x6e: LOG3 v3a, v47(0x0), v4a(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v47(0x0), v45
    0x6f: v6f(0x27bf) = CONST 
    0x73: v73(0x7d) = CONST 
    0x76: v76(0x0) = CONST 
    0x78: CODECOPY v76(0x0), v73(0x7d), v6f(0x27bf)
    0x79: v79(0x0) = CONST 
    0x7b: RETURN v79(0x0), v6f(0x27bf)
    0x2862: v2862(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

}

