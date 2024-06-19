function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xa, 0xb]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLDATASIZE 
    0x6: v6(0xb) = CONST 
    0x9: JUMPI v6(0xb), v5

    Begin block 0xa
    prev=[0x0], succ=[]
    =================================
    0xa: STOP 

    Begin block 0xb
    prev=[0x0], succ=[0x58, 0x78]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: vf = CALLDATALOAD vc(0x0)
    0x10: v10(0x1) = CONST 
    0x12: v12(0x1) = CONST 
    0x14: v14(0xe0) = CONST 
    0x16: v16(0x100000000000000000000000000000000000000000000000000000000) = SHL v14(0xe0), v12(0x1)
    0x17: v17(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v16(0x100000000000000000000000000000000000000000000000000000000), v10(0x1)
    0x18: v18(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v17(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x19: v19 = AND v18(0xffffffff00000000000000000000000000000000000000000000000000000000), vf
    0x1b: MSTORE vc(0x0), v19
    0x1c: v1c(0xc8fcad8db84d3cc18b4c41d551ea0ee66dd599cde068d998e57d5e09332c131c) = CONST 
    0x3d: v3d(0x20) = CONST 
    0x41: MSTORE v3d(0x20), v1c(0xc8fcad8db84d3cc18b4c41d551ea0ee66dd599cde068d998e57d5e09332c131c)
    0x42: v42(0x40) = CONST 
    0x46: v46 = SHA3 vc(0x0), v42(0x40)
    0x47: v47 = SLOAD v46
    0x4a: v4a(0x1) = CONST 
    0x4c: v4c(0x1) = CONST 
    0x4e: v4e(0xa0) = CONST 
    0x50: v50(0x10000000000000000000000000000000000000000) = SHL v4e(0xa0), v4c(0x1)
    0x51: v51(0xffffffffffffffffffffffffffffffffffffffff) = SUB v50(0x10000000000000000000000000000000000000000), v4a(0x1)
    0x52: v52 = AND v51(0xffffffffffffffffffffffffffffffffffffffff), v47
    0x54: v54(0x78) = CONST 
    0x57: JUMPI v54(0x78), v52

    Begin block 0x58
    prev=[0xb], succ=[0xe54]
    =================================
    0x58: v58(0x40) = CONST 
    0x5a: v5a = MLOAD v58(0x40)
    0x5b: v5b(0x461bcd) = CONST 
    0x5f: v5f(0xe5) = CONST 
    0x61: v61(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5f(0xe5), v5b(0x461bcd)
    0x63: MSTORE v5a, v61(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x64: v64(0x4) = CONST 
    0x66: v66 = ADD v64(0x4), v5a
    0x67: v67(0x10d5) = CONST 
    0x6b: v6b(0xe54) = CONST 
    0x6e: JUMP v6b(0xe54)

    Begin block 0xe54
    prev=[0x58], succ=[0x10d5]
    =================================
    0xe55: ve55(0x20) = CONST 
    0xe59: MSTORE v66, ve55(0x20)
    0xe5c: ve5c = ADD ve55(0x20), v66
    0xe5d: MSTORE ve5c, ve55(0x20)
    0xe5e: ve5e(0x4469616d6f6e643a2046756e6374696f6e20646f6573206e6f74206578697374) = CONST 
    0xe7f: ve7f(0x40) = CONST 
    0xe82: ve82 = ADD v66, ve7f(0x40)
    0xe83: MSTORE ve82, ve5e(0x4469616d6f6e643a2046756e6374696f6e20646f6573206e6f74206578697374)
    0xe84: ve84(0x60) = CONST 
    0xe86: ve86 = ADD ve84(0x60), v66
    0xe88: JUMP v67(0x10d5)

    Begin block 0x10d5
    prev=[0xe54], succ=[]
    =================================
    0x10d6: v10d6(0x40) = CONST 
    0x10d8: v10d8 = MLOAD v10d6(0x40)
    0x10db: v10db(0x64) = SUB ve86, v10d8
    0x10dd: REVERT v10d8, v10db(0x64)

    Begin block 0x78
    prev=[0xb], succ=[0x93, 0x97]
    =================================
    0x79: v79 = CALLDATASIZE 
    0x7a: v7a(0x0) = CONST 
    0x7d: CALLDATACOPY v7a(0x0), v7a(0x0), v79
    0x7e: v7e(0x0) = CONST 
    0x81: v81 = CALLDATASIZE 
    0x82: v82(0x0) = CONST 
    0x85: v85 = GAS 
    0x86: v86 = DELEGATECALL v85, v52, v82(0x0), v81, v7e(0x0), v7e(0x0)
    0x87: v87 = RETURNDATASIZE 
    0x88: v88(0x0) = CONST 
    0x8b: RETURNDATACOPY v88(0x0), v88(0x0), v87
    0x8e: v8e = ISZERO v86
    0x8f: v8f(0x97) = CONST 
    0x92: JUMPI v8f(0x97), v8e

    Begin block 0x93
    prev=[0x78], succ=[]
    =================================
    0x93: v93 = RETURNDATASIZE 
    0x94: v94(0x0) = CONST 
    0x96: RETURN v94(0x0), v93

    Begin block 0x97
    prev=[0x78], succ=[]
    =================================
    0x98: v98 = RETURNDATASIZE 
    0x99: v99(0x0) = CONST 
    0x9b: REVERT v99(0x0), v98

}

