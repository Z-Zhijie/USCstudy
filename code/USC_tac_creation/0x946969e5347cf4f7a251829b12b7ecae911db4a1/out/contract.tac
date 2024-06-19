function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x12]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xd) = CONST 
    0x8: v8 = CALLER 
    0x9: v9(0x12) = CONST 
    0xc: JUMP v9(0x12)

    Begin block 0x12
    prev=[0x0], succ=[0x42, 0x78]
    =================================
    0x13: v13(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x34: v34(0x1) = CONST 
    0x36: v36(0x1) = CONST 
    0x38: v38(0xa0) = CONST 
    0x3a: v3a(0x10000000000000000000000000000000000000000) = SHL v38(0xa0), v36(0x1)
    0x3b: v3b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a(0x10000000000000000000000000000000000000000), v34(0x1)
    0x3d: v3d = AND v8, v3b(0xffffffffffffffffffffffffffffffffffffffff)
    0x3e: v3e(0x78) = CONST 
    0x41: JUMPI v3e(0x78), v3d

    Begin block 0x42
    prev=[0x12], succ=[]
    =================================
    0x42: v42(0x40) = CONST 
    0x44: v44 = MLOAD v42(0x40)
    0x45: v45(0x461bcd) = CONST 
    0x49: v49(0xe5) = CONST 
    0x4b: v4b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v49(0xe5), v45(0x461bcd)
    0x4d: MSTORE v44, v4b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4e: v4e(0x4) = CONST 
    0x50: v50 = ADD v4e(0x4), v44
    0x53: v53(0x20) = CONST 
    0x55: v55 = ADD v53(0x20), v50
    0x58: v58(0x20) = SUB v55, v50
    0x5a: MSTORE v50, v58(0x20)
    0x5b: v5b(0x29) = CONST 
    0x5e: MSTORE v55, v5b(0x29)
    0x5f: v5f(0x20) = CONST 
    0x61: v61 = ADD v5f(0x20), v55
    0x63: v63(0x9b8) = CONST 
    0x66: v66(0x29) = CONST 
    0x69: CODECOPY v61, v63(0x9b8), v66(0x29)
    0x6a: v6a(0x40) = CONST 
    0x6c: v6c = ADD v6a(0x40), v61
    0x70: v70(0x40) = CONST 
    0x72: v72 = MLOAD v70(0x40)
    0x75: v75(0x84) = SUB v6c, v72
    0x77: REVERT v72, v75(0x84)

    Begin block 0x78
    prev=[0x12], succ=[0xd]
    =================================
    0x79: SSTORE v13(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v8
    0x7a: JUMP v5(0xd)

    Begin block 0xd
    prev=[0x78], succ=[0x7b]
    =================================
    0xe: ve(0x7b) = CONST 
    0x11: JUMP ve(0x7b)

    Begin block 0x7b
    prev=[0xd], succ=[]
    =================================
    0x7c: v7c(0x92e) = CONST 
    0x80: v80(0x8a) = CONST 
    0x83: v83(0x0) = CONST 
    0x85: CODECOPY v83(0x0), v80(0x8a), v7c(0x92e)
    0x86: v86(0x0) = CONST 
    0x88: RETURN v86(0x0), v7c(0x92e)

}

