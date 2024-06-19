function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0xcf]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xcb: vcb(0xcf) = CONST 
    0xcc: JUMPI vcb(0xcf), v8

    Begin block 0xc
    prev=[0x0], succ=[0xcf, 0xd2]
    =================================
    0xc: vc(0x0) = CONST 
    0xe: ve = CALLDATALOAD vc(0x0)
    0xf: vf(0xe0) = CONST 
    0x11: v11 = SHR vf(0xe0), ve
    0x13: v13(0xa619486e) = CONST 
    0x18: v18 = EQ v13(0xa619486e), v11
    0xcd: vcd(0xd2) = CONST 
    0xce: JUMPI vcd(0xd2), v18

    Begin block 0xcf
    prev=[0x0, 0xc], succ=[]
    =================================
    0xd0: vd0(0x1c) = CONST 
    0xd1: CALLPRIVATE vd0(0x1c)

    Begin block 0xd2
    prev=[0xc], succ=[]
    =================================
    0xd3: vd3(0x4c) = CONST 
    0xd4: CALLPRIVATE vd3(0x4c)

}

function fallback()() public {
    Begin block 0x1c
    prev=[], succ=[0x43, 0x47]
    =================================
    0x1d: v1d(0x0) = CONST 
    0x20: v20 = SLOAD v1d(0x0)
    0x21: v21(0x1) = CONST 
    0x23: v23(0x1) = CONST 
    0x25: v25(0xa0) = CONST 
    0x27: v27(0x10000000000000000000000000000000000000000) = SHL v25(0xa0), v23(0x1)
    0x28: v28(0xffffffffffffffffffffffffffffffffffffffff) = SUB v27(0x10000000000000000000000000000000000000000), v21(0x1)
    0x29: v29 = AND v28(0xffffffffffffffffffffffffffffffffffffffff), v20
    0x2b: v2b = CALLDATASIZE 
    0x2e: CALLDATACOPY v1d(0x0), v1d(0x0), v2b
    0x2f: v2f(0x0) = CONST 
    0x32: v32 = CALLDATASIZE 
    0x33: v33(0x0) = CONST 
    0x36: v36 = GAS 
    0x37: v37 = DELEGATECALL v36, v29, v33(0x0), v32, v2f(0x0), v2f(0x0)
    0x38: v38 = RETURNDATASIZE 
    0x39: v39(0x0) = CONST 
    0x3c: RETURNDATACOPY v39(0x0), v39(0x0), v38
    0x3f: v3f = ISZERO v37
    0x40: v40(0x47) = CONST 
    0x42: JUMPI v40(0x47), v3f

    Begin block 0x43
    prev=[0x1c], succ=[]
    =================================
    0x43: v43 = RETURNDATASIZE 
    0x44: v44(0x0) = CONST 
    0x46: RETURN v44(0x0), v43

    Begin block 0x47
    prev=[0x1c], succ=[]
    =================================
    0x48: v48 = RETURNDATASIZE 
    0x49: v49(0x0) = CONST 
    0x4b: REVERT v49(0x0), v48

}

function masterCopy()() public {
    Begin block 0x4c
    prev=[], succ=[0x53, 0x57]
    =================================
    0x4d: v4d = CALLVALUE 
    0x4f: v4f = ISZERO v4d
    0x50: v50(0x57) = CONST 
    0x52: JUMPI v50(0x57), v4f

    Begin block 0x53
    prev=[0x4c], succ=[]
    =================================
    0x53: v53(0x0) = CONST 
    0x56: REVERT v53(0x0), v53(0x0)

    Begin block 0x57
    prev=[0x4c], succ=[0x72]
    =================================
    0x59: v59(0x5e) = CONST 
    0x5b: v5b(0x72) = CONST 
    0x5d: JUMP v5b(0x72)

    Begin block 0x72
    prev=[0x57], succ=[0x5e]
    =================================
    0x73: v73(0x0) = CONST 
    0x75: v75 = SLOAD v73(0x0)
    0x76: v76(0x1) = CONST 
    0x78: v78(0x1) = CONST 
    0x7a: v7a(0xa0) = CONST 
    0x7c: v7c(0x10000000000000000000000000000000000000000) = SHL v7a(0xa0), v78(0x1)
    0x7d: v7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c(0x10000000000000000000000000000000000000000), v76(0x1)
    0x7e: v7e = AND v7d(0xffffffffffffffffffffffffffffffffffffffff), v75
    0x80: JUMP v59(0x5e)

    Begin block 0x5e
    prev=[0x72], succ=[0x81]
    =================================
    0x5f: v5f(0x40) = CONST 
    0x61: v61 = MLOAD v5f(0x40)
    0x62: v62(0x69) = CONST 
    0x66: v66(0x81) = CONST 
    0x68: JUMP v66(0x81)

    Begin block 0x81
    prev=[0x5e], succ=[0x69]
    =================================
    0x82: v82(0x1) = CONST 
    0x84: v84(0x1) = CONST 
    0x86: v86(0xa0) = CONST 
    0x88: v88(0x10000000000000000000000000000000000000000) = SHL v86(0xa0), v84(0x1)
    0x89: v89(0xffffffffffffffffffffffffffffffffffffffff) = SUB v88(0x10000000000000000000000000000000000000000), v82(0x1)
    0x8d: v8d = AND v89(0xffffffffffffffffffffffffffffffffffffffff), v7e
    0x8f: MSTORE v61, v8d
    0x90: v90(0x20) = CONST 
    0x92: v92 = ADD v90(0x20), v61
    0x94: JUMP v62(0x69)

    Begin block 0x69
    prev=[0x81], succ=[]
    =================================
    0x6a: v6a(0x40) = CONST 
    0x6c: v6c = MLOAD v6a(0x40)
    0x6f: v6f(0x20) = SUB v92, v6c
    0x71: RETURN v6c, v6f(0x20)

}

