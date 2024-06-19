function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x2a, 0x21]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x1) = CONST 
    0x7: v7(0x1) = CONST 
    0x9: v9(0xa0) = CONST 
    0xb: vb(0x10000000000000000000000000000000000000000) = SHL v9(0xa0), v7(0x1)
    0xc: vc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb(0x10000000000000000000000000000000000000000), v5(0x1)
    0xd: vd(0x0) = CONST 
    0xf: vf = SLOAD vd(0x0)
    0x10: v10 = AND vf, vc(0xffffffffffffffffffffffffffffffffffffffff)
    0x11: v11(0x530ca437) = CONST 
    0x16: v16(0xe1) = CONST 
    0x18: v18(0xa619486e00000000000000000000000000000000000000000000000000000000) = SHL v16(0xe1), v11(0x530ca437)
    0x19: v19(0x0) = CONST 
    0x1b: v1b = CALLDATALOAD v19(0x0)
    0x1c: v1c = EQ v1b, v18(0xa619486e00000000000000000000000000000000000000000000000000000000)
    0x1d: v1d = ISZERO v1c
    0x1e: v1e(0x2a) = CONST 
    0x20: JUMPI v1e(0x2a), v1d

    Begin block 0x2a
    prev=[0x0], succ=[0x42, 0x46]
    =================================
    0x2b: v2b = CALLDATASIZE 
    0x2c: v2c(0x0) = CONST 
    0x2f: CALLDATACOPY v2c(0x0), v2c(0x0), v2b
    0x30: v30(0x0) = CONST 
    0x33: v33 = CALLDATASIZE 
    0x34: v34(0x0) = CONST 
    0x37: v37 = GAS 
    0x38: v38 = DELEGATECALL v37, v10, v34(0x0), v33, v30(0x0), v30(0x0)
    0x39: v39 = RETURNDATASIZE 
    0x3a: v3a(0x0) = CONST 
    0x3d: RETURNDATACOPY v3a(0x0), v3a(0x0), v39
    0x3f: v3f(0x46) = CONST 
    0x41: JUMPI v3f(0x46), v38

    Begin block 0x42
    prev=[0x2a], succ=[]
    =================================
    0x42: v42 = RETURNDATASIZE 
    0x43: v43(0x0) = CONST 
    0x45: REVERT v43(0x0), v42

    Begin block 0x46
    prev=[0x2a], succ=[]
    =================================
    0x47: v47 = RETURNDATASIZE 
    0x48: v48(0x0) = CONST 
    0x4a: RETURN v48(0x0), v47

    Begin block 0x21
    prev=[0x0], succ=[]
    =================================
    0x22: v22(0x0) = CONST 
    0x24: MSTORE v22(0x0), v10
    0x25: v25(0x20) = CONST 
    0x27: v27(0x0) = CONST 
    0x29: RETURN v27(0x0), v25(0x20)

}

