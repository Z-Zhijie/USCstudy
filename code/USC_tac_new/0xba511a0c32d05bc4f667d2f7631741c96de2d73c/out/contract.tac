function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xf, 0xb]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0xf) = CONST 
    0xa: JUMPI v8(0xf), v7

    Begin block 0xf
    prev=[0x0], succ=[0x18, 0x71]
    =================================
    0x11: v11(0x4) = CONST 
    0x13: v13 = CALLDATASIZE 
    0x14: v14 = LT v13, v11(0x4)
    0x6d: v6d(0x71) = CONST 
    0x6e: JUMPI v6d(0x71), v14

    Begin block 0x18
    prev=[0xf], succ=[0x71, 0x74]
    =================================
    0x18: v18(0x0) = CONST 
    0x1a: v1a = CALLDATALOAD v18(0x0)
    0x1b: v1b(0xe0) = CONST 
    0x1d: v1d = SHR v1b(0xe0), v1a
    0x1f: v1f(0xe1c7392a) = CONST 
    0x24: v24 = EQ v1f(0xe1c7392a), v1d
    0x6f: v6f(0x74) = CONST 
    0x70: JUMPI v6f(0x74), v24

    Begin block 0x71
    prev=[0xf, 0x18], succ=[]
    =================================
    0x72: v72(0x28) = CONST 
    0x73: CALLPRIVATE v72(0x28)

    Begin block 0x74
    prev=[0x18], succ=[]
    =================================
    0x75: v75(0x2d) = CONST 
    0x76: CALLPRIVATE v75(0x2d)

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xb: vb(0x0) = CONST 
    0xe: REVERT vb(0x0), vb(0x0)

}

function fallback()() public {
    Begin block 0x28
    prev=[], succ=[]
    =================================
    0x29: v29(0x0) = CONST 
    0x2c: REVERT v29(0x0), v29(0x0)

}

function init()() public {
    Begin block 0x2d
    prev=[], succ=[0x35B0x2d]
    =================================
    0x2e: v2e(0x33) = CONST 
    0x30: v30(0x35) = CONST 
    0x32: JUMP v30(0x35), v2e(0x33)

    Begin block 0x35B0x2d
    prev=[0x2d], succ=[0x33]
    =================================
    0x36S0x2d: JUMP v2e(0x33)

    Begin block 0x33
    prev=[0x35B0x2d], succ=[]
    =================================
    0x34: STOP 

}

