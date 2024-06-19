function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x17, 0x1b]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x3) = CONST 
    0x8: v8 = SLOAD v5(0x3)
    0x9: v9(0xff) = CONST 
    0xb: vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v9(0xff)
    0xc: vc = AND vb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v8
    0xe: SSTORE v5(0x3), vc
    0xf: vf = CALLVALUE 
    0x11: v11 = ISZERO vf
    0x12: v12(0x1b) = CONST 
    0x16: JUMPI v12(0x1b), v11

    Begin block 0x17
    prev=[0x0], succ=[]
    =================================
    0x17: v17(0x0) = CONST 
    0x1a: REVERT v17(0x0), v17(0x0)

    Begin block 0x1b
    prev=[0x0], succ=[0x58B0x1b]
    =================================
    0x1d: v1d(0x37) = CONST 
    0x21: v21(0x1ffc9a7) = CONST 
    0x26: v26(0xe0) = CONST 
    0x28: v28(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v26(0xe0), v21(0x1ffc9a7)
    0x29: v29(0x1) = CONST 
    0x2b: v2b(0x1) = CONST 
    0x2d: v2d(0xe0) = CONST 
    0x2f: v2f(0x100000000000000000000000000000000000000000000000000000000) = SHL v2d(0xe0), v2b(0x1)
    0x30: v30(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2f(0x100000000000000000000000000000000000000000000000000000000), v29(0x1)
    0x31: v31(0x58) = CONST 
    0x35: v35(0x58) = AND v31(0x58), v30(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x36: JUMP v35(0x58), v28(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v1d(0x37)

    Begin block 0x58B0x1b
    prev=[0x1b], succ=[0x6cB0x1b, 0xb8B0x1b]
    =================================
    0x59S0x1b: v59V1b(0x1) = CONST 
    0x5bS0x1b: v5bV1b(0x1) = CONST 
    0x5dS0x1b: v5dV1b(0xe0) = CONST 
    0x5fS0x1b: v5fV1b(0x100000000000000000000000000000000000000000000000000000000) = SHL v5dV1b(0xe0), v5bV1b(0x1)
    0x60S0x1b: v60V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v5fV1b(0x100000000000000000000000000000000000000000000000000000000), v59V1b(0x1)
    0x61S0x1b: v61V1b(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v60V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x64S0x1b: v64V1b(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND v28(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v61V1b(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x65S0x1b: v65V1b(0x0) = EQ v64V1b(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v61V1b(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x66S0x1b: v66V1b = ISZERO v65V1b(0x0)
    0x67S0x1b: v67V1b(0xb8) = CONST 
    0x6bS0x1b: JUMPI v67V1b(0xb8), v66V1b

    Begin block 0x6cB0x1b
    prev=[0x58B0x1b], succ=[]
    =================================
    0x6cS0x1b: v6cV1b(0x40) = CONST 
    0x6fS0x1b: v6fV1b = MLOAD v6cV1b(0x40)
    0x70S0x1b: v70V1b(0x461bcd) = CONST 
    0x74S0x1b: v74V1b(0xe5) = CONST 
    0x76S0x1b: v76V1b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v74V1b(0xe5), v70V1b(0x461bcd)
    0x78S0x1b: MSTORE v6fV1b, v76V1b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x79S0x1b: v79V1b(0x20) = CONST 
    0x7bS0x1b: v7bV1b(0x4) = CONST 
    0x7eS0x1b: v7eV1b = ADD v6fV1b, v7bV1b(0x4)
    0x7fS0x1b: MSTORE v7eV1b, v79V1b(0x20)
    0x80S0x1b: v80V1b(0x1c) = CONST 
    0x82S0x1b: v82V1b(0x24) = CONST 
    0x85S0x1b: v85V1b = ADD v6fV1b, v82V1b(0x24)
    0x86S0x1b: MSTORE v85V1b, v80V1b(0x1c)
    0x87S0x1b: v87V1b(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0xa8S0x1b: va8V1b(0x44) = CONST 
    0xabS0x1b: vabV1b = ADD v6fV1b, va8V1b(0x44)
    0xacS0x1b: MSTORE vabV1b, v87V1b(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0xaeS0x1b: vaeV1b = MLOAD v6cV1b(0x40)
    0xb2S0x1b: vb2V1b(0x0) = SUB v6fV1b, vaeV1b
    0xb3S0x1b: vb3V1b(0x64) = CONST 
    0xb5S0x1b: vb5V1b(0x64) = ADD vb3V1b(0x64), vb2V1b(0x0)
    0xb7S0x1b: REVERT vaeV1b, vb5V1b(0x64)

    Begin block 0xb8B0x1b
    prev=[0x58B0x1b], succ=[0x37]
    =================================
    0xb9S0x1b: vb9V1b(0x1) = CONST 
    0xbbS0x1b: vbbV1b(0x1) = CONST 
    0xbdS0x1b: vbdV1b(0xe0) = CONST 
    0xbfS0x1b: vbfV1b(0x100000000000000000000000000000000000000000000000000000000) = SHL vbdV1b(0xe0), vbbV1b(0x1)
    0xc0S0x1b: vc0V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vbfV1b(0x100000000000000000000000000000000000000000000000000000000), vb9V1b(0x1)
    0xc1S0x1b: vc1V1b(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT vc0V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xc2S0x1b: vc2V1b(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = AND vc1V1b(0xffffffff00000000000000000000000000000000000000000000000000000000), v28(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0xc3S0x1b: vc3V1b(0x0) = CONST 
    0xc7S0x1b: MSTORE vc3V1b(0x0), vc2V1b(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0xc8S0x1b: vc8V1b(0x20) = CONST 
    0xccS0x1b: MSTORE vc8V1b(0x20), vc3V1b(0x0)
    0xcdS0x1b: vcdV1b(0x40) = CONST 
    0xd0S0x1b: vd0V1b = SHA3 vc3V1b(0x0), vcdV1b(0x40)
    0xd2S0x1b: vd2V1b = SLOAD vd0V1b
    0xd3S0x1b: vd3V1b(0xff) = CONST 
    0xd5S0x1b: vd5V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vd3V1b(0xff)
    0xd6S0x1b: vd6V1b = AND vd5V1b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vd2V1b
    0xd7S0x1b: vd7V1b(0x1) = CONST 
    0xd9S0x1b: vd9V1b = OR vd7V1b(0x1), vd6V1b
    0xdbS0x1b: SSTORE vd0V1b, vd9V1b
    0xdcS0x1b: JUMP v1d(0x37)

    Begin block 0x37
    prev=[0xb8B0x1b], succ=[0x58B0x37]
    =================================
    0x38: v38(0x52) = CONST 
    0x3c: v3c(0x2711897) = CONST 
    0x41: v41(0xe5) = CONST 
    0x43: v43(0x4e2312e000000000000000000000000000000000000000000000000000000000) = SHL v41(0xe5), v3c(0x2711897)
    0x44: v44(0x1) = CONST 
    0x46: v46(0x1) = CONST 
    0x48: v48(0xe0) = CONST 
    0x4a: v4a(0x100000000000000000000000000000000000000000000000000000000) = SHL v48(0xe0), v46(0x1)
    0x4b: v4b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v4a(0x100000000000000000000000000000000000000000000000000000000), v44(0x1)
    0x4c: v4c(0x58) = CONST 
    0x50: v50(0x58) = AND v4c(0x58), v4b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x51: JUMP v50(0x58), v43(0x4e2312e000000000000000000000000000000000000000000000000000000000), v38(0x52)

    Begin block 0x58B0x37
    prev=[0x37], succ=[0x6cB0x37, 0xb8B0x37]
    =================================
    0x59S0x37: v59V37(0x1) = CONST 
    0x5bS0x37: v5bV37(0x1) = CONST 
    0x5dS0x37: v5dV37(0xe0) = CONST 
    0x5fS0x37: v5fV37(0x100000000000000000000000000000000000000000000000000000000) = SHL v5dV37(0xe0), v5bV37(0x1)
    0x60S0x37: v60V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v5fV37(0x100000000000000000000000000000000000000000000000000000000), v59V37(0x1)
    0x61S0x37: v61V37(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v60V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x64S0x37: v64V37(0x4e2312e000000000000000000000000000000000000000000000000000000000) = AND v43(0x4e2312e000000000000000000000000000000000000000000000000000000000), v61V37(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x65S0x37: v65V37(0x0) = EQ v64V37(0x4e2312e000000000000000000000000000000000000000000000000000000000), v61V37(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x66S0x37: v66V37 = ISZERO v65V37(0x0)
    0x67S0x37: v67V37(0xb8) = CONST 
    0x6bS0x37: JUMPI v67V37(0xb8), v66V37

    Begin block 0x6cB0x37
    prev=[0x58B0x37], succ=[]
    =================================
    0x6cS0x37: v6cV37(0x40) = CONST 
    0x6fS0x37: v6fV37 = MLOAD v6cV37(0x40)
    0x70S0x37: v70V37(0x461bcd) = CONST 
    0x74S0x37: v74V37(0xe5) = CONST 
    0x76S0x37: v76V37(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v74V37(0xe5), v70V37(0x461bcd)
    0x78S0x37: MSTORE v6fV37, v76V37(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x79S0x37: v79V37(0x20) = CONST 
    0x7bS0x37: v7bV37(0x4) = CONST 
    0x7eS0x37: v7eV37 = ADD v6fV37, v7bV37(0x4)
    0x7fS0x37: MSTORE v7eV37, v79V37(0x20)
    0x80S0x37: v80V37(0x1c) = CONST 
    0x82S0x37: v82V37(0x24) = CONST 
    0x85S0x37: v85V37 = ADD v6fV37, v82V37(0x24)
    0x86S0x37: MSTORE v85V37, v80V37(0x1c)
    0x87S0x37: v87V37(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0xa8S0x37: va8V37(0x44) = CONST 
    0xabS0x37: vabV37 = ADD v6fV37, va8V37(0x44)
    0xacS0x37: MSTORE vabV37, v87V37(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0xaeS0x37: vaeV37 = MLOAD v6cV37(0x40)
    0xb2S0x37: vb2V37(0x0) = SUB v6fV37, vaeV37
    0xb3S0x37: vb3V37(0x64) = CONST 
    0xb5S0x37: vb5V37(0x64) = ADD vb3V37(0x64), vb2V37(0x0)
    0xb7S0x37: REVERT vaeV37, vb5V37(0x64)

    Begin block 0xb8B0x37
    prev=[0x58B0x37], succ=[0x52]
    =================================
    0xb9S0x37: vb9V37(0x1) = CONST 
    0xbbS0x37: vbbV37(0x1) = CONST 
    0xbdS0x37: vbdV37(0xe0) = CONST 
    0xbfS0x37: vbfV37(0x100000000000000000000000000000000000000000000000000000000) = SHL vbdV37(0xe0), vbbV37(0x1)
    0xc0S0x37: vc0V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vbfV37(0x100000000000000000000000000000000000000000000000000000000), vb9V37(0x1)
    0xc1S0x37: vc1V37(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT vc0V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xc2S0x37: vc2V37(0x4e2312e000000000000000000000000000000000000000000000000000000000) = AND vc1V37(0xffffffff00000000000000000000000000000000000000000000000000000000), v43(0x4e2312e000000000000000000000000000000000000000000000000000000000)
    0xc3S0x37: vc3V37(0x0) = CONST 
    0xc7S0x37: MSTORE vc3V37(0x0), vc2V37(0x4e2312e000000000000000000000000000000000000000000000000000000000)
    0xc8S0x37: vc8V37(0x20) = CONST 
    0xccS0x37: MSTORE vc8V37(0x20), vc3V37(0x0)
    0xcdS0x37: vcdV37(0x40) = CONST 
    0xd0S0x37: vd0V37 = SHA3 vc3V37(0x0), vcdV37(0x40)
    0xd2S0x37: vd2V37 = SLOAD vd0V37
    0xd3S0x37: vd3V37(0xff) = CONST 
    0xd5S0x37: vd5V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vd3V37(0xff)
    0xd6S0x37: vd6V37 = AND vd5V37(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vd2V37
    0xd7S0x37: vd7V37(0x1) = CONST 
    0xd9S0x37: vd9V37 = OR vd7V37(0x1), vd6V37
    0xdbS0x37: SSTORE vd0V37, vd9V37
    0xdcS0x37: JUMP v38(0x52)

    Begin block 0x52
    prev=[0xb8B0x37], succ=[0xdd]
    =================================
    0x53: v53(0xdd) = CONST 
    0x57: JUMP v53(0xdd)

    Begin block 0xdd
    prev=[0x52], succ=[]
    =================================
    0xde: vde(0x2537) = CONST 
    0xe2: ve2(0xed) = CONST 
    0xe6: ve6(0x0) = CONST 
    0xe8: CODECOPY ve6(0x0), ve2(0xed), vde(0x2537)
    0xe9: ve9(0x0) = CONST 
    0xeb: RETURN ve9(0x0), vde(0x2537)

}

