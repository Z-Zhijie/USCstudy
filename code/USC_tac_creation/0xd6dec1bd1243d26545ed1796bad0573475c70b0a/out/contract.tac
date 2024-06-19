function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLER 
    0x6: v6(0x0) = CONST 
    0x9: v9(0x100) = CONST 
    0xc: vc(0x1) = EXP v9(0x100), v6(0x0)
    0xe: ve = SLOAD v6(0x0)
    0x10: v10(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25: v25(0xffffffffffffffffffffffffffffffffffffffff) = MUL v10(0xffffffffffffffffffffffffffffffffffffffff), vc(0x1)
    0x26: v26(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v25(0xffffffffffffffffffffffffffffffffffffffff)
    0x27: v27 = AND v26(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), ve
    0x2a: v2a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3f: v3f = AND v2a(0xffffffffffffffffffffffffffffffffffffffff), v5
    0x40: v40 = MUL v3f, vc(0x1)
    0x41: v41 = OR v40, v27
    0x43: SSTORE v6(0x0), v41
    0x45: v45(0x0) = CONST 
    0x49: v49 = SLOAD v45(0x0)
    0x4b: v4b(0x100) = CONST 
    0x4e: v4e(0x1) = EXP v4b(0x100), v45(0x0)
    0x50: v50 = DIV v49, v4e(0x1)
    0x51: v51(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x66: v66 = AND v51(0xffffffffffffffffffffffffffffffffffffffff), v50
    0x67: v67(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7c: v7c = AND v67(0xffffffffffffffffffffffffffffffffffffffff), v66
    0x7d: v7d(0x0) = CONST 
    0x7f: v7f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x94: v94(0x0) = AND v7f(0xffffffffffffffffffffffffffffffffffffffff), v7d(0x0)
    0x95: v95(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xb6: vb6(0x40) = CONST 
    0xb8: vb8 = MLOAD vb6(0x40)
    0xb9: vb9(0x40) = CONST 
    0xbb: vbb = MLOAD vb9(0x40)
    0xbe: vbe(0x0) = SUB vb8, vbb
    0xc0: LOG3 vbb, vbe(0x0), v95(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v94(0x0), v7c
    0xc1: vc1(0xb8d) = CONST 
    0xc5: vc5(0xcf) = CONST 
    0xc8: vc8(0x0) = CONST 
    0xca: CODECOPY vc8(0x0), vc5(0xcf), vc1(0xb8d)
    0xcb: vcb(0x0) = CONST 
    0xcd: RETURN vcb(0x0), vc1(0xb8d)

}

