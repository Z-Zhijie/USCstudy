function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xf, 0xb]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5 = CALLVALUE 
    0x6: v6 = ISZERO v5
    0x7: v7(0xf) = CONST 
    0xa: JUMPI v7(0xf), v6

    Begin block 0xf
    prev=[0x0], succ=[]
    =================================
    0x10: v10(0x40) = CONST 
    0x12: v12 = MLOAD v10(0x40)
    0x13: v13(0x20) = CONST 
    0x16: v16(0x47f8) = CONST 
    0x1c: v1c = ADD v481b(0x000000000000000000000000a94e49bdbb0bfdb920ec1e441b1c408ead94c9bc), v12
    0x1d: v1d(0x40) = CONST 
    0x1f: MSTORE v1d(0x40), v1c
    0x22: v22 = MLOAD v481b(0x000000000000000000000000a94e49bdbb0bfdb920ec1e441b1c408ead94c9bc)
    0x23: v23(0x0) = CONST 
    0x26: v26 = SLOAD v23(0x0)
    0x27: v27(0x1) = CONST 
    0x29: v29(0xa0) = CONST 
    0x2b: v2b(0x2) = CONST 
    0x2d: v2d(0x10000000000000000000000000000000000000000) = EXP v2b(0x2), v29(0xa0)
    0x2e: v2e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d(0x10000000000000000000000000000000000000000), v27(0x1)
    0x31: v31 = AND v22, v2e(0xffffffffffffffffffffffffffffffffffffffff)
    0x32: v32(0x1) = CONST 
    0x34: v34(0xa0) = CONST 
    0x36: v36(0x2) = CONST 
    0x38: v38(0x10000000000000000000000000000000000000000) = EXP v36(0x2), v34(0xa0)
    0x39: v39(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38(0x10000000000000000000000000000000000000000), v32(0x1)
    0x3a: v3a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v39(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d: v3d = AND v26, v3a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x41: v41 = OR v3d, v31
    0x43: SSTORE v23(0x0), v41
    0x46: v46(0x47a4) = CONST 
    0x4a: v4a(0x54) = CONST 
    0x4d: v4d(0x0) = CONST 
    0x4f: CODECOPY v4d(0x0), v4a(0x54), v46(0x47a4)
    0x50: v50(0x0) = CONST 
    0x52: RETURN v50(0x0), v46(0x47a4)
    0x481b: v481b(0x000000000000000000000000a94e49bdbb0bfdb920ec1e441b1c408ead94c9bc) = CONST 

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xb: vb(0x0) = CONST 
    0xe: REVERT vb(0x0), vb(0x0)

}

