function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x20, 0x1c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x9c) = CONST 
    0x8: v8 = SLOAD v5(0x9c)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa0) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = SHL vd(0xa0), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x14: SSTORE v5(0x9c), v12
    0x15: v15 = CALLVALUE 
    0x17: v17 = ISZERO v15
    0x18: v18(0x20) = CONST 
    0x1b: JUMPI v18(0x20), v17

    Begin block 0x20
    prev=[0x0], succ=[0x37]
    =================================
    0x22: v22(0x37) = CONST 
    0x25: v25 = CALLER 
    0x26: v26(0x0) = CONST 
    0x29: v29 = MLOAD v26(0x0)
    0x2a: v2a(0x20) = CONST 
    0x2c: v2c(0x201b) = CONST 
    0x34: MSTORE v26(0x0), v29
    0x35: SSTORE v203c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v25
    0x36: JUMP v22(0x37)
    0x203c: v203c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

    Begin block 0x37
    prev=[0x20], succ=[]
    =================================
    0x38: v38(0x0) = CONST 
    0x3b: v3b = MLOAD v38(0x0)
    0x3c: v3c(0x20) = CONST 
    0x3e: v3e(0x201b) = CONST 
    0x46: MSTORE v38(0x0), v3b
    0x47: v47 = SLOAD v2041(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x48: v48(0x40) = CONST 
    0x4a: v4a = MLOAD v48(0x40)
    0x4b: v4b(0x1) = CONST 
    0x4d: v4d(0x1) = CONST 
    0x4f: v4f(0xa0) = CONST 
    0x51: v51(0x10000000000000000000000000000000000000000) = SHL v4f(0xa0), v4d(0x1)
    0x52: v52(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51(0x10000000000000000000000000000000000000000), v4b(0x1)
    0x55: v55 = AND v47, v52(0xffffffffffffffffffffffffffffffffffffffff)
    0x57: v57(0x0) = CONST 
    0x5a: v5a(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x7e: LOG3 v4a, v57(0x0), v5a(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v57(0x0), v55
    0x7f: v7f(0x1f8e) = CONST 
    0x83: v83(0x8d) = CONST 
    0x86: v86(0x0) = CONST 
    0x88: CODECOPY v86(0x0), v83(0x8d), v7f(0x1f8e)
    0x89: v89(0x0) = CONST 
    0x8b: RETURN v89(0x0), v7f(0x1f8e)
    0x2041: v2041(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 

    Begin block 0x1c
    prev=[0x0], succ=[]
    =================================
    0x1c: v1c(0x0) = CONST 
    0x1f: REVERT v1c(0x0), v1c(0x0)

}

