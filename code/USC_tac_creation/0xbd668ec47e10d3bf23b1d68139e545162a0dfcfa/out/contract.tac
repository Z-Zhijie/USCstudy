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
    prev=[0x0], succ=[]
    =================================
    0x12: v12(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd) = CONST 
    0x27: v27(0x0) = CONST 
    0x2a: v2a(0x100) = CONST 
    0x2d: v2d(0x1) = EXP v2a(0x100), v27(0x0)
    0x2f: v2f = SLOAD v27(0x0)
    0x31: v31(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x46: v46(0xffffffffffffffffffffffffffffffffffffffff) = MUL v31(0xffffffffffffffffffffffffffffffffffffffff), v2d(0x1)
    0x47: v47(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v46(0xffffffffffffffffffffffffffffffffffffffff)
    0x48: v48 = AND v47(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2f
    0x4b: v4b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x60: v60(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd) = AND v4b(0xffffffffffffffffffffffffffffffffffffffff), v12(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd)
    0x61: v61(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd) = MUL v60(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd), v2d(0x1)
    0x62: v62 = OR v61(0x1a678da709f209a94c94bd9ceb63ecdfeadf3cfd), v48
    0x64: SSTORE v27(0x0), v62
    0x66: v66 = CALLER 
    0x67: v67(0x1) = CONST 
    0x69: v69(0x0) = CONST 
    0x6b: v6b(0x100) = CONST 
    0x6e: v6e(0x1) = EXP v6b(0x100), v69(0x0)
    0x70: v70 = SLOAD v67(0x1)
    0x72: v72(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x87: v87(0xffffffffffffffffffffffffffffffffffffffff) = MUL v72(0xffffffffffffffffffffffffffffffffffffffff), v6e(0x1)
    0x88: v88(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v87(0xffffffffffffffffffffffffffffffffffffffff)
    0x89: v89 = AND v88(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v70
    0x8c: v8c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa1: va1 = AND v8c(0xffffffffffffffffffffffffffffffffffffffff), v66
    0xa2: va2 = MUL va1, v6e(0x1)
    0xa3: va3 = OR va2, v89
    0xa5: SSTORE v67(0x1), va3
    0xa7: va7(0x39f) = CONST 
    0xab: vab(0xb5) = CONST 
    0xae: vae(0x0) = CONST 
    0xb0: CODECOPY vae(0x0), vab(0xb5), va7(0x39f)
    0xb1: vb1(0x0) = CONST 
    0xb3: RETURN vb1(0x0), va7(0x39f)

}

