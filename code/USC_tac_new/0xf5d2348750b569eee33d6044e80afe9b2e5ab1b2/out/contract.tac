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
    prev=[0x0], succ=[0x18, 0x102]
    =================================
    0x11: v11(0x4) = CONST 
    0x13: v13 = CALLDATASIZE 
    0x14: v14 = LT v13, v11(0x4)
    0xfc: vfc(0x102) = CONST 
    0xfd: JUMPI vfc(0x102), v14

    Begin block 0x18
    prev=[0xf], succ=[0x105, 0x28]
    =================================
    0x18: v18(0x0) = CONST 
    0x1a: v1a = CALLDATALOAD v18(0x0)
    0x1b: v1b(0xe0) = CONST 
    0x1d: v1d = SHR v1b(0xe0), v1a
    0x1f: v1f(0xdbe671f) = CONST 
    0x24: v24 = EQ v1f(0xdbe671f), v1d
    0xfe: vfe(0x105) = CONST 
    0xff: JUMPI vfe(0x105), v24

    Begin block 0x105
    prev=[0x18], succ=[]
    =================================
    0x106: v106(0x37) = CONST 
    0x107: CALLPRIVATE v106(0x37)

    Begin block 0x28
    prev=[0x18], succ=[0x102, 0x108]
    =================================
    0x29: v29(0x6d4ce63c) = CONST 
    0x2e: v2e = EQ v29(0x6d4ce63c), v1d
    0x100: v100(0x108) = CONST 
    0x101: JUMPI v100(0x108), v2e

    Begin block 0x102
    prev=[0xf, 0x28], succ=[]
    =================================
    0x103: v103(0x32) = CONST 
    0x104: CALLPRIVATE v103(0x32)

    Begin block 0x108
    prev=[0x28], succ=[]
    =================================
    0x109: v109(0x4f) = CONST 
    0x10a: CALLPRIVATE v109(0x4f)

    Begin block 0xb
    prev=[0x0], succ=[]
    =================================
    0xb: vb(0x0) = CONST 
    0xe: REVERT vb(0x0), vb(0x0)

}

function fallback()() public {
    Begin block 0x32
    prev=[], succ=[]
    =================================
    0x33: v33(0x0) = CONST 
    0x36: REVERT v33(0x0), v33(0x0)

}

function a()() public {
    Begin block 0x37
    prev=[], succ=[0x55]
    =================================
    0x38: v38(0xb9) = CONST 
    0x3a: v3a(0x55) = CONST 
    0x3c: JUMP v3a(0x55)

    Begin block 0x55
    prev=[0x37], succ=[0xb9]
    =================================
    0x56: v56(0x0) = CONST 
    0x58: v58 = SLOAD v56(0x0)
    0x5a: JUMP v38(0xb9)

    Begin block 0xb9
    prev=[0x55], succ=[]
    =================================
    0xba: vba(0x40) = CONST 
    0xbd: vbd = MLOAD vba(0x40)
    0xc0: MSTORE vbd, v58
    0xc1: vc1 = MLOAD vba(0x40)
    0xc5: vc5(0x0) = SUB vbd, vc1
    0xc6: vc6(0x20) = CONST 
    0xc8: vc8(0x20) = ADD vc6(0x20), vc5(0x0)
    0xca: RETURN vc1, vc8(0x20)

}

function get()() public {
    Begin block 0x4f
    prev=[], succ=[0x5b]
    =================================
    0x50: v50(0xea) = CONST 
    0x52: v52(0x5b) = CONST 
    0x54: JUMP v52(0x5b)

    Begin block 0x5b
    prev=[0x4f], succ=[0xea]
    =================================
    0x5c: v5c(0x0) = CONST 
    0x5e: v5e = SLOAD v5c(0x0)
    0x5f: v5f(0x1) = CONST 
    0x61: v61 = ADD v5f(0x1), v5e
    0x63: JUMP v50(0xea)

    Begin block 0xea
    prev=[0x5b], succ=[]
    =================================
    0xeb: veb(0x40) = CONST 
    0xee: vee = MLOAD veb(0x40)
    0xf1: MSTORE vee, v61
    0xf2: vf2 = MLOAD veb(0x40)
    0xf6: vf6(0x0) = SUB vee, vf2
    0xf7: vf7(0x20) = CONST 
    0xf9: vf9(0x20) = ADD vf7(0x20), vf6(0x0)
    0xfb: RETURN vf2, vf9(0x20)

}

