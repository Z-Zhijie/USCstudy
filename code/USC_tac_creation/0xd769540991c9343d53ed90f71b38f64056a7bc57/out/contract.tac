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
    prev=[0x0], succ=[0x39]
    =================================
    0x12: v12(0x39) = CONST 
    0x15: v15 = CALLER 
    0x16: v16(0x17f2f492df265d2a20221741db3d2a0b8fd5b19500149d73967a1a94afc2bf83) = CONST 
    0x37: SSTORE v16(0x17f2f492df265d2a20221741db3d2a0b8fd5b19500149d73967a1a94afc2bf83), v15
    0x38: JUMP v12(0x39)

    Begin block 0x39
    prev=[0x10], succ=[]
    =================================
    0x3a: v3a(0x7c7) = CONST 
    0x3e: v3e(0x48) = CONST 
    0x41: v41(0x0) = CONST 
    0x43: CODECOPY v41(0x0), v3e(0x48), v3a(0x7c7)
    0x44: v44(0x0) = CONST 
    0x46: RETURN v44(0x0), v3a(0x7c7)

}

