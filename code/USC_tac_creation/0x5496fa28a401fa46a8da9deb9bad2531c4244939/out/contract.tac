function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1e, 0x22]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x0) = CONST 
    0x8: v8 = SLOAD v5(0x0)
    0x9: v9(0x100) = CONST 
    0xc: vc(0x1) = CONST 
    0xe: ve(0xa8) = CONST 
    0x10: v10(0x1000000000000000000000000000000000000000000) = SHL ve(0xa8), vc(0x1)
    0x11: v11(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v10(0x1000000000000000000000000000000000000000000), v9(0x100)
    0x12: v12(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v11(0xffffffffffffffffffffffffffffffffffffffff00)
    0x13: v13 = AND v12(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff), v8
    0x15: SSTORE v5(0x0), v13
    0x16: v16 = CALLVALUE 
    0x18: v18 = ISZERO v16
    0x19: v19(0x22) = CONST 
    0x1d: JUMPI v19(0x22), v18

    Begin block 0x1e
    prev=[0x0], succ=[]
    =================================
    0x1e: v1e(0x0) = CONST 
    0x21: REVERT v1e(0x0), v1e(0x0)

    Begin block 0x22
    prev=[0x0], succ=[0x44, 0x48]
    =================================
    0x24: v24(0x40) = CONST 
    0x26: v26 = MLOAD v24(0x40)
    0x27: v27(0x5991) = CONST 
    0x2b: v2b = CODESIZE 
    0x2c: v2c = SUB v2b, v27(0x5991)
    0x2e: v2e(0x5991) = CONST 
    0x33: CODECOPY v26, v2e(0x5991), v2c
    0x36: v36 = ADD v2c, v26
    0x37: v37(0x40) = CONST 
    0x39: MSTORE v37(0x40), v36
    0x3a: v3a(0x20) = CONST 
    0x3d: v3d = LT v2c, v3a(0x20)
    0x3e: v3e = ISZERO v3d
    0x3f: v3f(0x48) = CONST 
    0x43: JUMPI v3f(0x48), v3e

    Begin block 0x44
    prev=[0x22], succ=[]
    =================================
    0x44: v44(0x0) = CONST 
    0x47: REVERT v44(0x0), v44(0x0)

    Begin block 0x48
    prev=[0x22], succ=[]
    =================================
    0x4a: v4a = MLOAD v26
    0x4b: v4b(0x0) = CONST 
    0x4e: v4e = SLOAD v4b(0x0)
    0x4f: v4f(0xff) = CONST 
    0x51: v51(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v4f(0xff)
    0x52: v52(0x1) = CONST 
    0x54: v54(0x1) = CONST 
    0x56: v56(0xa0) = CONST 
    0x58: v58(0x10000000000000000000000000000000000000000) = SHL v56(0xa0), v54(0x1)
    0x59: v59(0xffffffffffffffffffffffffffffffffffffffff) = SUB v58(0x10000000000000000000000000000000000000000), v52(0x1)
    0x5c: v5c = AND v4a, v59(0xffffffffffffffffffffffffffffffffffffffff)
    0x5d: v5d(0x100) = CONST 
    0x60: v60 = MUL v5d(0x100), v5c
    0x61: v61(0x100) = CONST 
    0x64: v64(0x1) = CONST 
    0x66: v66(0xa8) = CONST 
    0x68: v68(0x1000000000000000000000000000000000000000000) = SHL v66(0xa8), v64(0x1)
    0x69: v69(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v68(0x1000000000000000000000000000000000000000000), v61(0x100)
    0x6a: v6a(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v69(0xffffffffffffffffffffffffffffffffffffffff00)
    0x6d: v6d = AND v4e, v6a(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff)
    0x6e: v6e = OR v6d, v60
    0x72: v72 = AND v6e, v51(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x73: v73(0x1) = CONST 
    0x75: v75 = OR v73(0x1), v72
    0x77: SSTORE v4b(0x0), v75
    0x78: v78(0x590a) = CONST 
    0x7c: v7c(0x87) = CONST 
    0x80: v80(0x0) = CONST 
    0x82: CODECOPY v80(0x0), v7c(0x87), v78(0x590a)
    0x83: v83(0x0) = CONST 
    0x85: RETURN v83(0x0), v78(0x590a)

}

