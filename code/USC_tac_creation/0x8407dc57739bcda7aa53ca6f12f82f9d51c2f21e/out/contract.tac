function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x6: MSTORE v2(0x40), v0(0x80)
    0x7: v7(0x0) = CONST 
    0xa: va = SLOAD v7(0x0)
    0xb: vb(0x1) = CONST 
    0xd: vd(0x1) = CONST 
    0xf: vf(0xa0) = CONST 
    0x11: v11(0x10000000000000000000000000000000000000000) = SHL vf(0xa0), vd(0x1)
    0x12: v12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11(0x10000000000000000000000000000000000000000), vb(0x1)
    0x13: v13(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v12(0xffffffffffffffffffffffffffffffffffffffff)
    0x14: v14 = AND v13(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va
    0x15: v15 = CALLER 
    0x16: v16 = OR v15, v14
    0x19: SSTORE v7(0x0), v16
    0x1a: v1a(0x1) = CONST 
    0x1c: v1c(0x1) = CONST 
    0x1e: v1e(0xa0) = CONST 
    0x20: v20(0x10000000000000000000000000000000000000000) = SHL v1e(0xa0), v1c(0x1)
    0x21: v21(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20(0x10000000000000000000000000000000000000000), v1a(0x1)
    0x22: v22 = AND v21(0xffffffffffffffffffffffffffffffffffffffff), v16
    0x24: v24(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x48: LOG3 v0(0x80), v7(0x0), v24(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f), v7(0x0), v22
    0x49: v49(0x2c35) = CONST 
    0x4d: v4d(0x57) = CONST 
    0x50: v50(0x0) = CONST 
    0x52: CODECOPY v50(0x0), v4d(0x57), v49(0x2c35)
    0x53: v53(0x0) = CONST 
    0x55: RETURN v53(0x0), v49(0x2c35)

}

