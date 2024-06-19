function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x62, 0x66]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x44f262622248027f8e2a8fb1090c4cf85072392c) = CONST 
    0x1a: v1a(0x4) = CONST 
    0x1c: v1c(0x0) = CONST 
    0x1e: v1e(0x100) = CONST 
    0x21: v21(0x1) = EXP v1e(0x100), v1c(0x0)
    0x23: v23 = SLOAD v1a(0x4)
    0x25: v25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a: v3a(0xffffffffffffffffffffffffffffffffffffffff) = MUL v25(0xffffffffffffffffffffffffffffffffffffffff), v21(0x1)
    0x3b: v3b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3a(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c: v3c = AND v3b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v23
    0x3f: v3f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x54: v54(0x44f262622248027f8e2a8fb1090c4cf85072392c) = AND v3f(0xffffffffffffffffffffffffffffffffffffffff), v5(0x44f262622248027f8e2a8fb1090c4cf85072392c)
    0x55: v55(0x44f262622248027f8e2a8fb1090c4cf85072392c) = MUL v54(0x44f262622248027f8e2a8fb1090c4cf85072392c), v21(0x1)
    0x56: v56 = OR v55(0x44f262622248027f8e2a8fb1090c4cf85072392c), v3c
    0x58: SSTORE v1a(0x4), v56
    0x5a: v5a = CALLVALUE 
    0x5c: v5c = ISZERO v5a
    0x5d: v5d(0x66) = CONST 
    0x61: JUMPI v5d(0x66), v5c

    Begin block 0x62
    prev=[0x0], succ=[]
    =================================
    0x62: v62(0x0) = CONST 
    0x65: REVERT v62(0x0), v62(0x0)

    Begin block 0x66
    prev=[0x0], succ=[0x85]
    =================================
    0x68: v68(0x78) = CONST 
    0x6c: v6c = CALLER 
    0x6d: v6d(0x85) = CONST 
    0x71: v71(0x20) = CONST 
    0x73: v73(0x8500000000) = SHL v71(0x20), v6d(0x85)
    0x74: v74(0x20) = CONST 
    0x76: v76(0x85) = SHR v74(0x20), v73(0x8500000000)
    0x77: JUMP v76(0x85)

    Begin block 0x85
    prev=[0x66], succ=[0x78]
    =================================
    0x87: v87(0x0) = CONST 
    0x8a: v8a(0x100) = CONST 
    0x8d: v8d(0x1) = EXP v8a(0x100), v87(0x0)
    0x8f: v8f = SLOAD v87(0x0)
    0x91: v91(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa6: va6(0xffffffffffffffffffffffffffffffffffffffff) = MUL v91(0xffffffffffffffffffffffffffffffffffffffff), v8d(0x1)
    0xa7: va7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va6(0xffffffffffffffffffffffffffffffffffffffff)
    0xa8: va8 = AND va7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8f
    0xab: vab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc0: vc0 = AND vab(0xffffffffffffffffffffffffffffffffffffffff), v6c
    0xc1: vc1 = MUL vc0, v8d(0x1)
    0xc2: vc2 = OR vc1, va8
    0xc4: SSTORE v87(0x0), vc2
    0xc7: JUMP v68(0x78)

    Begin block 0x78
    prev=[0x85], succ=[0xc8]
    =================================
    0x79: v79(0x1) = CONST 
    0x7e: SSTORE v79(0x1), v79(0x1)
    0x80: v80(0xc8) = CONST 
    0x84: JUMP v80(0xc8)

    Begin block 0xc8
    prev=[0x78], succ=[]
    =================================
    0xc9: vc9(0x4a67) = CONST 
    0xcd: vcd(0xd8) = CONST 
    0xd1: vd1(0x0) = CONST 
    0xd3: CODECOPY vd1(0x0), vcd(0xd8), vc9(0x4a67)
    0xd4: vd4(0x0) = CONST 
    0xd6: RETURN vd4(0x0), vc9(0x4a67)

}

