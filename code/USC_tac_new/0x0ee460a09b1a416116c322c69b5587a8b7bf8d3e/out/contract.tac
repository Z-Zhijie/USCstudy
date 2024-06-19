function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[0x1a, 0x142]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x13e: v13e(0x142) = CONST 
    0x13f: JUMPI v13e(0x142), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x142, 0x145]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0xa9059cbb) = CONST 
    0x26: v26 = EQ v21(0xa9059cbb), v1f
    0x140: v140(0x145) = CONST 
    0x141: JUMPI v140(0x145), v26

    Begin block 0x142
    prev=[0x1a, 0x10], succ=[]
    =================================
    0x143: v143(0x2b) = CONST 
    0x144: CALLPRIVATE v143(0x2b)

    Begin block 0x145
    prev=[0x1a], succ=[]
    =================================
    0x146: v146(0x30) = CONST 
    0x147: CALLPRIVATE v146(0x30)

}

function fallback()() public {
    Begin block 0x2b
    prev=[], succ=[]
    =================================
    0x2c: v2c(0x0) = CONST 
    0x2f: REVERT v2c(0x0), v2c(0x0)

}

function transfer(address,uint256)() public {
    Begin block 0x30
    prev=[], succ=[0x42, 0x46]
    =================================
    0x31: v31(0x7c) = CONST 
    0x34: v34(0x4) = CONST 
    0x37: v37 = CALLDATASIZE 
    0x38: v38 = SUB v37, v34(0x4)
    0x39: v39(0x40) = CONST 
    0x3c: v3c = LT v38, v39(0x40)
    0x3d: v3d = ISZERO v3c
    0x3e: v3e(0x46) = CONST 
    0x41: JUMPI v3e(0x46), v3d

    Begin block 0x42
    prev=[0x30], succ=[]
    =================================
    0x42: v42(0x0) = CONST 
    0x45: REVERT v42(0x0), v42(0x0)

    Begin block 0x46
    prev=[0x30], succ=[0x96]
    =================================
    0x48: v48 = ADD v34(0x4), v38
    0x4c: v4c = CALLDATALOAD v34(0x4)
    0x4d: v4d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x62: v62 = AND v4d(0xffffffffffffffffffffffffffffffffffffffff), v4c
    0x64: v64(0x20) = CONST 
    0x66: v66(0x24) = ADD v64(0x20), v34(0x4)
    0x6c: v6c = CALLDATALOAD v66(0x24)
    0x6e: v6e(0x20) = CONST 
    0x70: v70(0x44) = ADD v6e(0x20), v66(0x24)
    0x78: v78(0x96) = CONST 
    0x7b: JUMP v78(0x96)

    Begin block 0x96
    prev=[0x46], succ=[0x7c]
    =================================
    0x97: v97(0x0) = CONST 
    0x99: v99(0xb1a788d78c7ee87c662101020dc014023c80d738dd509f3ade9e69f463ec497d) = CONST 
    0xbc: vbc(0x40) = CONST 
    0xbe: vbe = MLOAD vbc(0x40)
    0xc1: vc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd6: vd6 = AND vc1(0xffffffffffffffffffffffffffffffffffffffff), v62
    0xd7: vd7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec: vec = AND vd7(0xffffffffffffffffffffffffffffffffffffffff), vd6
    0xee: MSTORE vbe, vec
    0xef: vef(0x20) = CONST 
    0xf1: vf1 = ADD vef(0x20), vbe
    0xf4: MSTORE vf1, v6c
    0xf5: vf5(0x20) = CONST 
    0xf7: vf7 = ADD vf5(0x20), vf1
    0xfc: vfc(0x40) = CONST 
    0xfe: vfe = MLOAD vfc(0x40)
    0x101: v101(0x40) = SUB vf7, vfe
    0x103: LOG1 vfe, v101(0x40), v99(0xb1a788d78c7ee87c662101020dc014023c80d738dd509f3ade9e69f463ec497d)
    0x108: JUMP v31(0x7c)

    Begin block 0x7c
    prev=[0x96], succ=[]
    =================================
    0x7d: v7d(0x40) = CONST 
    0x7f: v7f = MLOAD v7d(0x40)
    0x82: v82 = ISZERO v97(0x0)
    0x83: v83 = ISZERO v82
    0x84: v84 = ISZERO v83
    0x85: v85 = ISZERO v84
    0x87: MSTORE v7f, v85
    0x88: v88(0x20) = CONST 
    0x8a: v8a = ADD v88(0x20), v7f
    0x8e: v8e(0x40) = CONST 
    0x90: v90 = MLOAD v8e(0x40)
    0x93: v93(0x20) = SUB v8a, v90
    0x95: RETURN v90, v93(0x20)

}

