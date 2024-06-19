function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x32, 0x36]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xb) = CONST 
    0x8: v8 = SLOAD v5(0xb)
    0x9: v9(0x1) = CONST 
    0xb: vb(0x1) = CONST 
    0xd: vd(0xa0) = CONST 
    0xf: vf(0x10000000000000000000000000000000000000000) = SHL vd(0xa0), vb(0x1)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf(0x10000000000000000000000000000000000000000), v9(0x1)
    0x11: v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10(0xffffffffffffffffffffffffffffffffffffffff)
    0x12: v12 = AND v11(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8
    0x13: v13(0xfee5f54e1070e7ed31be341e0a5b1e847f6a84ab) = CONST 
    0x28: v28 = OR v13(0xfee5f54e1070e7ed31be341e0a5b1e847f6a84ab), v12
    0x2a: SSTORE v5(0xb), v28
    0x2b: v2b = CALLVALUE 
    0x2d: v2d = ISZERO v2b
    0x2e: v2e(0x36) = CONST 
    0x31: JUMPI v2e(0x36), v2d

    Begin block 0x32
    prev=[0x0], succ=[]
    =================================
    0x32: v32(0x0) = CONST 
    0x35: REVERT v32(0x0), v32(0x0)

    Begin block 0x36
    prev=[0x0], succ=[]
    =================================
    0x38: v38(0x4520) = CONST 
    0x3c: v3c(0x46) = CONST 
    0x3f: v3f(0x0) = CONST 
    0x41: CODECOPY v3f(0x0), v3c(0x46), v38(0x4520)
    0x42: v42(0x0) = CONST 
    0x44: RETURN v42(0x0), v38(0x4520)

}

