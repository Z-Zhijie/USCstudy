function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1f, 0x23]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x8: v8 = SLOAD v5(0x1)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xa0) = CONST 
    0xd: vd(0xff0000000000000000000000000000000000000000) = SHL vb(0xa0), v9(0xff)
    0xe: ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vd(0xff0000000000000000000000000000000000000000)
    0xf: vf = AND ve(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v8
    0x11: SSTORE v5(0x1), vf
    0x12: v12(0x0) = CONST 
    0x14: v14(0xb) = CONST 
    0x16: SSTORE v14(0xb), v12(0x0)
    0x17: v17 = CALLVALUE 
    0x19: v19 = ISZERO v17
    0x1a: v1a(0x23) = CONST 
    0x1e: JUMPI v1a(0x23), v19

    Begin block 0x1f
    prev=[0x0], succ=[]
    =================================
    0x1f: v1f(0x0) = CONST 
    0x22: REVERT v1f(0x0), v1f(0x0)

    Begin block 0x23
    prev=[0x0], succ=[0x35]
    =================================
    0x25: v25(0x2f) = CONST 
    0x29: v29 = CALLER 
    0x2a: v2a(0x35) = CONST 
    0x2e: JUMP v2a(0x35)

    Begin block 0x35
    prev=[0x23], succ=[0x2f]
    =================================
    0x36: v36(0x0) = CONST 
    0x39: v39 = SLOAD v36(0x0)
    0x3a: v3a(0x1) = CONST 
    0x3c: v3c(0x1) = CONST 
    0x3e: v3e(0xa0) = CONST 
    0x40: v40(0x10000000000000000000000000000000000000000) = SHL v3e(0xa0), v3c(0x1)
    0x41: v41(0xffffffffffffffffffffffffffffffffffffffff) = SUB v40(0x10000000000000000000000000000000000000000), v3a(0x1)
    0x42: v42(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v41(0xffffffffffffffffffffffffffffffffffffffff)
    0x43: v43 = AND v42(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v39
    0x44: v44(0x1) = CONST 
    0x46: v46(0x1) = CONST 
    0x48: v48(0xa0) = CONST 
    0x4a: v4a(0x10000000000000000000000000000000000000000) = SHL v48(0xa0), v46(0x1)
    0x4b: v4b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a(0x10000000000000000000000000000000000000000), v44(0x1)
    0x4f: v4f = AND v4b(0xffffffffffffffffffffffffffffffffffffffff), v29
    0x53: v53 = OR v4f, v43
    0x55: SSTORE v36(0x0), v53
    0x56: JUMP v25(0x2f)

    Begin block 0x2f
    prev=[0x35], succ=[0x57]
    =================================
    0x30: v30(0x57) = CONST 
    0x34: JUMP v30(0x57)

    Begin block 0x57
    prev=[0x2f], succ=[]
    =================================
    0x58: v58(0x52e5) = CONST 
    0x5c: v5c(0x67) = CONST 
    0x60: v60(0x0) = CONST 
    0x62: CODECOPY v60(0x0), v5c(0x67), v58(0x52e5)
    0x63: v63(0x0) = CONST 
    0x65: RETURN v63(0x0), v58(0x52e5)

}

