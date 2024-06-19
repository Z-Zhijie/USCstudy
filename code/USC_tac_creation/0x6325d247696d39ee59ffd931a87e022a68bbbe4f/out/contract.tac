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
    prev=[0x0], succ=[0x1f]
    =================================
    0x12: v12(0x1a) = CONST 
    0x15: v15 = CALLER 
    0x16: v16(0x1f) = CONST 
    0x19: JUMP v16(0x1f)

    Begin block 0x1f
    prev=[0x10], succ=[0x1a]
    =================================
    0x20: v20(0x337c729c04082e3bdd94ba7d2b5a8a642f3a138702366a91707825373a2029ba) = CONST 
    0x41: SSTORE v20(0x337c729c04082e3bdd94ba7d2b5a8a642f3a138702366a91707825373a2029ba), v15
    0x42: JUMP v12(0x1a)

    Begin block 0x1a
    prev=[0x1f], succ=[0x43]
    =================================
    0x1b: v1b(0x43) = CONST 
    0x1e: JUMP v1b(0x43)

    Begin block 0x43
    prev=[0x1a], succ=[]
    =================================
    0x44: v44(0x4d3) = CONST 
    0x48: v48(0x52) = CONST 
    0x4b: v4b(0x0) = CONST 
    0x4d: CODECOPY v4b(0x0), v48(0x52), v44(0x4d3)
    0x4e: v4e(0x0) = CONST 
    0x50: RETURN v4e(0x0), v44(0x4d3)

}

