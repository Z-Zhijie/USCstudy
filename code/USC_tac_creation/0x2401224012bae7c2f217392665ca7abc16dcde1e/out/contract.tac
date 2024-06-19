function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x6: MSTORE v2(0x40), v0(0x80)
    0x7: v7(0x1) = CONST 
    0xa: va = SLOAD v7(0x1)
    0xb: vb(0x1) = CONST 
    0xd: vd(0x1) = CONST 
    0xf: vf(0xa0) = CONST 
    0x11: v11(0x10000000000000000000000000000000000000000) = SHL vf(0xa0), vd(0x1)
    0x12: v12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11(0x10000000000000000000000000000000000000000), vb(0x1)
    0x13: v13(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v12(0xffffffffffffffffffffffffffffffffffffffff)
    0x14: v14 = AND v13(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va
    0x15: v15 = CALLER 
    0x18: v18 = OR v15, v14
    0x1b: SSTORE v7(0x1), v18
    0x1d: v1d(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94) = CONST 
    0x3f: v3f(0x0) = CONST 
    0x42: LOG2 v0(0x80), v3f(0x0), v1d(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94), v15
    0x43: v43(0x1983) = CONST 
    0x47: v47(0x51) = CONST 
    0x4a: v4a(0x0) = CONST 
    0x4c: CODECOPY v4a(0x0), v47(0x51), v43(0x1983)
    0x4d: v4d(0x0) = CONST 
    0x4f: RETURN v4d(0x0), v43(0x1983)

}

