function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x1d, 0x21]
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
    0x19: v19(0x21) = CONST 
    0x1c: JUMPI v19(0x21), v18

    Begin block 0x1d
    prev=[0x0], succ=[]
    =================================
    0x1d: v1d(0x0) = CONST 
    0x20: REVERT v1d(0x0), v1d(0x0)

    Begin block 0x21
    prev=[0x0], succ=[0x40, 0x44]
    =================================
    0x23: v23(0x40) = CONST 
    0x25: v25 = MLOAD v23(0x40)
    0x26: v26(0xa5b) = CONST 
    0x29: v29 = CODESIZE 
    0x2a: v2a = SUB v29, v26(0xa5b)
    0x2c: v2c(0xa5b) = CONST 
    0x30: CODECOPY v25, v2c(0xa5b), v2a
    0x33: v33 = ADD v2a, v25
    0x34: v34(0x40) = CONST 
    0x36: MSTORE v34(0x40), v33
    0x37: v37(0x20) = CONST 
    0x3a: v3a = LT v2a, v37(0x20)
    0x3b: v3b = ISZERO v3a
    0x3c: v3c(0x44) = CONST 
    0x3f: JUMPI v3c(0x44), v3b

    Begin block 0x40
    prev=[0x21], succ=[]
    =================================
    0x40: v40(0x0) = CONST 
    0x43: REVERT v40(0x0), v40(0x0)

    Begin block 0x44
    prev=[0x21], succ=[]
    =================================
    0x46: v46 = MLOAD v25
    0x47: v47(0x0) = CONST 
    0x4a: v4a = SLOAD v47(0x0)
    0x4b: v4b(0x100) = CONST 
    0x4e: v4e(0x1) = CONST 
    0x50: v50(0xa8) = CONST 
    0x52: v52(0x1000000000000000000000000000000000000000000) = SHL v50(0xa8), v4e(0x1)
    0x53: v53(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v52(0x1000000000000000000000000000000000000000000), v4b(0x100)
    0x54: v54(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v53(0xffffffffffffffffffffffffffffffffffffffff00)
    0x55: v55 = AND v54(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff), v4a
    0x56: v56(0x100) = CONST 
    0x59: v59(0x1) = CONST 
    0x5b: v5b(0x1) = CONST 
    0x5d: v5d(0xa0) = CONST 
    0x5f: v5f(0x10000000000000000000000000000000000000000) = SHL v5d(0xa0), v5b(0x1)
    0x60: v60(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5f(0x10000000000000000000000000000000000000000), v59(0x1)
    0x62: v62 = AND v46, v60(0xffffffffffffffffffffffffffffffffffffffff)
    0x63: v63 = MUL v62, v56(0x100)
    0x64: v64 = OR v63, v55
    0x66: SSTORE v47(0x0), v64
    0x68: v68(0x0) = CONST 
    0x6b: v6b = SLOAD v68(0x0)
    0x6c: v6c(0xff) = CONST 
    0x6e: v6e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v6c(0xff)
    0x6f: v6f = AND v6e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v6b
    0x70: v70(0x1) = CONST 
    0x72: v72 = OR v70(0x1), v6f
    0x74: SSTORE v68(0x0), v72
    0x75: v75(0x9d8) = CONST 
    0x79: v79(0x83) = CONST 
    0x7c: v7c(0x0) = CONST 
    0x7e: CODECOPY v7c(0x0), v79(0x83), v75(0x9d8)
    0x7f: v7f(0x0) = CONST 
    0x81: RETURN v7f(0x0), v75(0x9d8)

}

