function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xb5c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xb4c: vb4c(0xb5c) = CONST 
    0xb4d: JUMPI vb4c(0xb5c), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0xb5f]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x26782247) = CONST 
    0x3b: v3b = EQ v34, v35(0x26782247)
    0xb4e: vb4e(0xb5f) = CONST 
    0xb4f: JUMPI vb4e(0xb5f), v3b

    Begin block 0x40
    prev=[0xd], succ=[0xb62, 0x4b]
    =================================
    0x41: v41(0x3659cfe6) = CONST 
    0x46: v46 = EQ v41(0x3659cfe6), v34
    0xb50: vb50(0xb62) = CONST 
    0xb51: JUMPI vb50(0xb62), v46

    Begin block 0xb62
    prev=[0x40], succ=[]
    =================================
    0xb63: vb63(0xbd) = CONST 
    0xb64: CALLPRIVATE vb63(0xbd)

    Begin block 0x4b
    prev=[0x40], succ=[0xb65, 0x56]
    =================================
    0x4c: v4c(0x4f1ef286) = CONST 
    0x51: v51 = EQ v4c(0x4f1ef286), v34
    0xb52: vb52(0xb65) = CONST 
    0xb53: JUMPI vb52(0xb65), v51

    Begin block 0xb65
    prev=[0x4b], succ=[]
    =================================
    0xb66: vb66(0xde) = CONST 
    0xb67: CALLPRIVATE vb66(0xde)

    Begin block 0x56
    prev=[0x4b], succ=[0xb68, 0x61]
    =================================
    0x57: v57(0x5c60da1b) = CONST 
    0x5c: v5c = EQ v57(0x5c60da1b), v34
    0xb54: vb54(0xb68) = CONST 
    0xb55: JUMPI vb54(0xb68), v5c

    Begin block 0xb68
    prev=[0x56], succ=[]
    =================================
    0xb69: vb69(0xfe) = CONST 
    0xb6a: CALLPRIVATE vb69(0xfe)

    Begin block 0x61
    prev=[0x56], succ=[0xb6b, 0x6c]
    =================================
    0x62: v62(0x8f283970) = CONST 
    0x67: v67 = EQ v62(0x8f283970), v34
    0xb56: vb56(0xb6b) = CONST 
    0xb57: JUMPI vb56(0xb6b), v67

    Begin block 0xb6b
    prev=[0x61], succ=[]
    =================================
    0xb6c: vb6c(0x113) = CONST 
    0xb6d: CALLPRIVATE vb6c(0x113)

    Begin block 0x6c
    prev=[0x61], succ=[0xb6e, 0x77]
    =================================
    0x6d: v6d(0xd3b2f598) = CONST 
    0x72: v72 = EQ v6d(0xd3b2f598), v34
    0xb58: vb58(0xb6e) = CONST 
    0xb59: JUMPI vb58(0xb6e), v72

    Begin block 0xb6e
    prev=[0x6c], succ=[]
    =================================
    0xb6f: vb6f(0x134) = CONST 
    0xb70: CALLPRIVATE vb6f(0x134)

    Begin block 0x77
    prev=[0x6c], succ=[0xb5c, 0xb71]
    =================================
    0x78: v78(0xf851a440) = CONST 
    0x7d: v7d = EQ v78(0xf851a440), v34
    0xb5a: vb5a(0xb71) = CONST 
    0xb5b: JUMPI vb5a(0xb71), v7d

    Begin block 0xb5c
    prev=[0x0, 0x77], succ=[]
    =================================
    0xb5d: vb5d(0x82) = CONST 
    0xb5e: CALLPRIVATE vb5d(0x82)

    Begin block 0xb71
    prev=[0x77], succ=[]
    =================================
    0xb72: vb72(0x149) = CONST 
    0xb73: CALLPRIVATE vb72(0x149)

    Begin block 0xb5f
    prev=[0xd], succ=[]
    =================================
    0xb60: vb60(0x8c) = CONST 
    0xb61: CALLPRIVATE vb60(0x8c)

}

function changeAdmin(address)() public {
    Begin block 0x113
    prev=[], succ=[0x11b, 0x11f]
    =================================
    0x114: v114 = CALLVALUE 
    0x116: v116 = ISZERO v114
    0x117: v117(0x11f) = CONST 
    0x11a: JUMPI v117(0x11f), v116

    Begin block 0x11b
    prev=[0x113], succ=[]
    =================================
    0x11b: v11b(0x0) = CONST 
    0x11e: REVERT v11b(0x0), v11b(0x0)

    Begin block 0x11f
    prev=[0x113], succ=[0x2bdB0x11f]
    =================================
    0x121: v121(0x975) = CONST 
    0x124: v124(0x1) = CONST 
    0x126: v126(0xa0) = CONST 
    0x128: v128(0x2) = CONST 
    0x12a: v12a(0x10000000000000000000000000000000000000000) = EXP v128(0x2), v126(0xa0)
    0x12b: v12b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12a(0x10000000000000000000000000000000000000000), v124(0x1)
    0x12c: v12c(0x4) = CONST 
    0x12e: v12e = CALLDATALOAD v12c(0x4)
    0x12f: v12f = AND v12e, v12b(0xffffffffffffffffffffffffffffffffffffffff)
    0x130: v130(0x2bd) = CONST 
    0x133: JUMP v130(0x2bd), v12f, v121(0x975)

    Begin block 0x2bdB0x11f
    prev=[0x11f], succ=[0x6c3B0x2bdB0x11f]
    =================================
    0x2beS0x11f: v2beV11f(0x2c5) = CONST 
    0x2c1S0x11f: v2c1V11f(0x6c3) = CONST 
    0x2c4S0x11f: JUMP v2c1V11f(0x6c3)

    Begin block 0x6c3B0x2bdB0x11f
    prev=[0x2bdB0x11f], succ=[0x2c5B0x11f]
    =================================
    0x6c4S0x2bdS0x11f: v6c4V2bdV11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x2bdS0x11f: v6e5V2bdV11f = SLOAD v6c4V2bdV11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x2bdS0x11f: JUMP v2beV11f(0x2c5)

    Begin block 0x2c5B0x11f
    prev=[0x6c3B0x2bdB0x11f], succ=[0x2dfB0x11f, 0xae5B0x11f]
    =================================
    0x2c6S0x11f: v2c6V11f(0x1) = CONST 
    0x2c8S0x11f: v2c8V11f(0xa0) = CONST 
    0x2caS0x11f: v2caV11f(0x2) = CONST 
    0x2ccS0x11f: v2ccV11f(0x10000000000000000000000000000000000000000) = EXP v2caV11f(0x2), v2c8V11f(0xa0)
    0x2cdS0x11f: v2cdV11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ccV11f(0x10000000000000000000000000000000000000000), v2c6V11f(0x1)
    0x2ceS0x11f: v2ceV11f = AND v2cdV11f(0xffffffffffffffffffffffffffffffffffffffff), v6e5V2bdV11f
    0x2cfS0x11f: v2cfV11f = CALLER 
    0x2d0S0x11f: v2d0V11f(0x1) = CONST 
    0x2d2S0x11f: v2d2V11f(0xa0) = CONST 
    0x2d4S0x11f: v2d4V11f(0x2) = CONST 
    0x2d6S0x11f: v2d6V11f(0x10000000000000000000000000000000000000000) = EXP v2d4V11f(0x2), v2d2V11f(0xa0)
    0x2d7S0x11f: v2d7V11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d6V11f(0x10000000000000000000000000000000000000000), v2d0V11f(0x1)
    0x2d8S0x11f: v2d8V11f = AND v2d7V11f(0xffffffffffffffffffffffffffffffffffffffff), v2cfV11f
    0x2d9S0x11f: v2d9V11f = EQ v2d8V11f, v2ceV11f
    0x2daS0x11f: v2daV11f = ISZERO v2d9V11f
    0x2dbS0x11f: v2dbV11f(0xae5) = CONST 
    0x2deS0x11f: JUMPI v2dbV11f(0xae5), v2daV11f

    Begin block 0x2dfB0x11f
    prev=[0x2c5B0x11f], succ=[0x2efB0x11f, 0x364B0x11f]
    =================================
    0x2dfS0x11f: v2dfV11f(0x1) = CONST 
    0x2e1S0x11f: v2e1V11f(0xa0) = CONST 
    0x2e3S0x11f: v2e3V11f(0x2) = CONST 
    0x2e5S0x11f: v2e5V11f(0x10000000000000000000000000000000000000000) = EXP v2e3V11f(0x2), v2e1V11f(0xa0)
    0x2e6S0x11f: v2e6V11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e5V11f(0x10000000000000000000000000000000000000000), v2dfV11f(0x1)
    0x2e8S0x11f: v2e8V11f = AND v12f, v2e6V11f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e9S0x11f: v2e9V11f = ISZERO v2e8V11f
    0x2eaS0x11f: v2eaV11f = ISZERO v2e9V11f
    0x2ebS0x11f: v2ebV11f(0x364) = CONST 
    0x2eeS0x11f: JUMPI v2ebV11f(0x364), v2eaV11f

    Begin block 0x2efB0x11f
    prev=[0x2dfB0x11f], succ=[]
    =================================
    0x2efS0x11f: v2efV11f(0x40) = CONST 
    0x2f2S0x11f: v2f2V11f = MLOAD v2efV11f(0x40)
    0x2f3S0x11f: v2f3V11f(0xe5) = CONST 
    0x2f5S0x11f: v2f5V11f(0x2) = CONST 
    0x2f7S0x11f: v2f7V11f(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2f5V11f(0x2), v2f3V11f(0xe5)
    0x2f8S0x11f: v2f8V11f(0x461bcd) = CONST 
    0x2fcS0x11f: v2fcV11f(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2f8V11f(0x461bcd), v2f7V11f(0x2000000000000000000000000000000000000000000000000000000000)
    0x2feS0x11f: MSTORE v2f2V11f, v2fcV11f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ffS0x11f: v2ffV11f(0x20) = CONST 
    0x301S0x11f: v301V11f(0x4) = CONST 
    0x304S0x11f: v304V11f = ADD v2f2V11f, v301V11f(0x4)
    0x305S0x11f: MSTORE v304V11f, v2ffV11f(0x20)
    0x306S0x11f: v306V11f(0x36) = CONST 
    0x308S0x11f: v308V11f(0x24) = CONST 
    0x30bS0x11f: v30bV11f = ADD v2f2V11f, v308V11f(0x24)
    0x30cS0x11f: MSTORE v30bV11f, v306V11f(0x36)
    0x30dS0x11f: v30dV11f(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f) = CONST 
    0x32eS0x11f: v32eV11f(0x44) = CONST 
    0x331S0x11f: v331V11f = ADD v2f2V11f, v32eV11f(0x44)
    0x332S0x11f: MSTORE v331V11f, v30dV11f(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f)
    0x333S0x11f: v333V11f(0x787920746f20746865207a65726f206164647265737300000000000000000000) = CONST 
    0x354S0x11f: v354V11f(0x64) = CONST 
    0x357S0x11f: v357V11f = ADD v2f2V11f, v354V11f(0x64)
    0x358S0x11f: MSTORE v357V11f, v333V11f(0x787920746f20746865207a65726f206164647265737300000000000000000000)
    0x35aS0x11f: v35aV11f = MLOAD v2efV11f(0x40)
    0x35eS0x11f: v35eV11f(0x0) = SUB v2f2V11f, v35aV11f
    0x35fS0x11f: v35fV11f(0x84) = CONST 
    0x361S0x11f: v361V11f(0x84) = ADD v35fV11f(0x84), v35eV11f(0x0)
    0x363S0x11f: REVERT v35aV11f, v361V11f(0x84)

    Begin block 0x364B0x11f
    prev=[0x2dfB0x11f], succ=[0x6c3B0x364B0x11f]
    =================================
    0x365S0x11f: v365V11f(0x36c) = CONST 
    0x368S0x11f: v368V11f(0x6c3) = CONST 
    0x36bS0x11f: JUMP v368V11f(0x6c3)

    Begin block 0x6c3B0x364B0x11f
    prev=[0x364B0x11f], succ=[0x36cB0x11f]
    =================================
    0x6c4S0x364S0x11f: v6c4V364V11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x364S0x11f: v6e5V364V11f = SLOAD v6c4V364V11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x364S0x11f: JUMP v365V11f(0x36c)

    Begin block 0x36cB0x11f
    prev=[0x6c3B0x364B0x11f], succ=[0x380B0x11f, 0x3f5B0x11f]
    =================================
    0x36dS0x11f: v36dV11f(0x1) = CONST 
    0x36fS0x11f: v36fV11f(0xa0) = CONST 
    0x371S0x11f: v371V11f(0x2) = CONST 
    0x373S0x11f: v373V11f(0x10000000000000000000000000000000000000000) = EXP v371V11f(0x2), v36fV11f(0xa0)
    0x374S0x11f: v374V11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v373V11f(0x10000000000000000000000000000000000000000), v36dV11f(0x1)
    0x377S0x11f: v377V11f = AND v374V11f(0xffffffffffffffffffffffffffffffffffffffff), v12f
    0x379S0x11f: v379V11f = AND v6e5V364V11f, v374V11f(0xffffffffffffffffffffffffffffffffffffffff)
    0x37aS0x11f: v37aV11f = EQ v379V11f, v377V11f
    0x37bS0x11f: v37bV11f = ISZERO v37aV11f
    0x37cS0x11f: v37cV11f(0x3f5) = CONST 
    0x37fS0x11f: JUMPI v37cV11f(0x3f5), v37bV11f

    Begin block 0x380B0x11f
    prev=[0x36cB0x11f], succ=[]
    =================================
    0x380S0x11f: v380V11f(0x40) = CONST 
    0x383S0x11f: v383V11f = MLOAD v380V11f(0x40)
    0x384S0x11f: v384V11f(0xe5) = CONST 
    0x386S0x11f: v386V11f(0x2) = CONST 
    0x388S0x11f: v388V11f(0x2000000000000000000000000000000000000000000000000000000000) = EXP v386V11f(0x2), v384V11f(0xe5)
    0x389S0x11f: v389V11f(0x461bcd) = CONST 
    0x38dS0x11f: v38dV11f(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v389V11f(0x461bcd), v388V11f(0x2000000000000000000000000000000000000000000000000000000000)
    0x38fS0x11f: MSTORE v383V11f, v38dV11f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x390S0x11f: v390V11f(0x20) = CONST 
    0x392S0x11f: v392V11f(0x4) = CONST 
    0x395S0x11f: v395V11f = ADD v383V11f, v392V11f(0x4)
    0x396S0x11f: MSTORE v395V11f, v390V11f(0x20)
    0x397S0x11f: v397V11f(0x2e) = CONST 
    0x399S0x11f: v399V11f(0x24) = CONST 
    0x39cS0x11f: v39cV11f = ADD v383V11f, v399V11f(0x24)
    0x39dS0x11f: MSTORE v39cV11f, v397V11f(0x2e)
    0x39eS0x11f: v39eV11f(0x5468652063757272656e7420616e64206e65772061646d696e2063616e6e6f74) = CONST 
    0x3bfS0x11f: v3bfV11f(0x44) = CONST 
    0x3c2S0x11f: v3c2V11f = ADD v383V11f, v3bfV11f(0x44)
    0x3c3S0x11f: MSTORE v3c2V11f, v39eV11f(0x5468652063757272656e7420616e64206e65772061646d696e2063616e6e6f74)
    0x3c4S0x11f: v3c4V11f(0x206265207468652073616d65202e000000000000000000000000000000000000) = CONST 
    0x3e5S0x11f: v3e5V11f(0x64) = CONST 
    0x3e8S0x11f: v3e8V11f = ADD v383V11f, v3e5V11f(0x64)
    0x3e9S0x11f: MSTORE v3e8V11f, v3c4V11f(0x206265207468652073616d65202e000000000000000000000000000000000000)
    0x3ebS0x11f: v3ebV11f = MLOAD v380V11f(0x40)
    0x3efS0x11f: v3efV11f(0x0) = SUB v383V11f, v3ebV11f
    0x3f0S0x11f: v3f0V11f(0x84) = CONST 
    0x3f2S0x11f: v3f2V11f(0x84) = ADD v3f0V11f(0x84), v3efV11f(0x0)
    0x3f4S0x11f: REVERT v3ebV11f, v3f2V11f(0x84)

    Begin block 0x3f5B0x11f
    prev=[0x36cB0x11f], succ=[0x6e8B0x3f5B0x11f]
    =================================
    0x3f6S0x11f: v3f6V11f(0x3fd) = CONST 
    0x3f9S0x11f: v3f9V11f(0x6e8) = CONST 
    0x3fcS0x11f: JUMP v3f9V11f(0x6e8)

    Begin block 0x6e8B0x3f5B0x11f
    prev=[0x3f5B0x11f], succ=[0x3fdB0x11f]
    =================================
    0x6e9S0x3f5S0x11f: v6e9V3f5V11f(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x70aS0x3f5S0x11f: v70aV3f5V11f = SLOAD v6e9V3f5V11f(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x70cS0x3f5S0x11f: JUMP v3f6V11f(0x3fd)

    Begin block 0x3fdB0x11f
    prev=[0x6e8B0x3f5B0x11f], succ=[0x411B0x11f, 0x486B0x11f]
    =================================
    0x3feS0x11f: v3feV11f(0x1) = CONST 
    0x400S0x11f: v400V11f(0xa0) = CONST 
    0x402S0x11f: v402V11f(0x2) = CONST 
    0x404S0x11f: v404V11f(0x10000000000000000000000000000000000000000) = EXP v402V11f(0x2), v400V11f(0xa0)
    0x405S0x11f: v405V11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v404V11f(0x10000000000000000000000000000000000000000), v3feV11f(0x1)
    0x408S0x11f: v408V11f = AND v405V11f(0xffffffffffffffffffffffffffffffffffffffff), v12f
    0x40aS0x11f: v40aV11f = AND v70aV3f5V11f, v405V11f(0xffffffffffffffffffffffffffffffffffffffff)
    0x40bS0x11f: v40bV11f = EQ v40aV11f, v408V11f
    0x40cS0x11f: v40cV11f = ISZERO v40bV11f
    0x40dS0x11f: v40dV11f(0x486) = CONST 
    0x410S0x11f: JUMPI v40dV11f(0x486), v40cV11f

    Begin block 0x411B0x11f
    prev=[0x3fdB0x11f], succ=[]
    =================================
    0x411S0x11f: v411V11f(0x40) = CONST 
    0x414S0x11f: v414V11f = MLOAD v411V11f(0x40)
    0x415S0x11f: v415V11f(0xe5) = CONST 
    0x417S0x11f: v417V11f(0x2) = CONST 
    0x419S0x11f: v419V11f(0x2000000000000000000000000000000000000000000000000000000000) = EXP v417V11f(0x2), v415V11f(0xe5)
    0x41aS0x11f: v41aV11f(0x461bcd) = CONST 
    0x41eS0x11f: v41eV11f(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v41aV11f(0x461bcd), v419V11f(0x2000000000000000000000000000000000000000000000000000000000)
    0x420S0x11f: MSTORE v414V11f, v41eV11f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x421S0x11f: v421V11f(0x20) = CONST 
    0x423S0x11f: v423V11f(0x4) = CONST 
    0x426S0x11f: v426V11f = ADD v414V11f, v423V11f(0x4)
    0x427S0x11f: MSTORE v426V11f, v421V11f(0x20)
    0x428S0x11f: v428V11f(0x38) = CONST 
    0x42aS0x11f: v42aV11f(0x24) = CONST 
    0x42dS0x11f: v42dV11f = ADD v414V11f, v42aV11f(0x24)
    0x42eS0x11f: MSTORE v42dV11f, v428V11f(0x38)
    0x42fS0x11f: v42fV11f(0x43616e6e6f742073657420746865206e657741646d696e206f6620612070726f) = CONST 
    0x450S0x11f: v450V11f(0x44) = CONST 
    0x453S0x11f: v453V11f = ADD v414V11f, v450V11f(0x44)
    0x454S0x11f: MSTORE v453V11f, v42fV11f(0x43616e6e6f742073657420746865206e657741646d696e206f6620612070726f)
    0x455S0x11f: v455V11f(0x787920746f207468652073616d652061646472657373202e0000000000000000) = CONST 
    0x476S0x11f: v476V11f(0x64) = CONST 
    0x479S0x11f: v479V11f = ADD v414V11f, v476V11f(0x64)
    0x47aS0x11f: MSTORE v479V11f, v455V11f(0x787920746f207468652073616d652061646472657373202e0000000000000000)
    0x47cS0x11f: v47cV11f = MLOAD v411V11f(0x40)
    0x480S0x11f: v480V11f(0x0) = SUB v414V11f, v47cV11f
    0x481S0x11f: v481V11f(0x84) = CONST 
    0x483S0x11f: v483V11f(0x84) = ADD v481V11f(0x84), v480V11f(0x0)
    0x485S0x11f: REVERT v47cV11f, v483V11f(0x84)

    Begin block 0x486B0x11f
    prev=[0x3fdB0x11f], succ=[0x755B0x486B0x11f]
    =================================
    0x487S0x11f: v487V11f(0x48f) = CONST 
    0x48bS0x11f: v48bV11f(0x755) = CONST 
    0x48eS0x11f: JUMP v48bV11f(0x755), v12f, v487V11f(0x48f)

    Begin block 0x755B0x486B0x11f
    prev=[0x486B0x11f], succ=[0x48fB0x11f]
    =================================
    0x756S0x486S0x11f: v756V486V11f(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x777S0x486S0x11f: SSTORE v756V486V11f(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c), v12f
    0x778S0x486S0x11f: JUMP v487V11f(0x48f)

    Begin block 0x48fB0x11f
    prev=[0x755B0x486B0x11f], succ=[0x6c3B0x48fB0x11f]
    =================================
    0x490S0x11f: v490V11f(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x4b1S0x11f: v4b1V11f(0x4b8) = CONST 
    0x4b4S0x11f: v4b4V11f(0x6c3) = CONST 
    0x4b7S0x11f: JUMP v4b4V11f(0x6c3)

    Begin block 0x6c3B0x48fB0x11f
    prev=[0x48fB0x11f], succ=[0x4b8B0x11f]
    =================================
    0x6c4S0x48fS0x11f: v6c4V48fV11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x48fS0x11f: v6e5V48fV11f = SLOAD v6c4V48fV11f(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x48fS0x11f: JUMP v4b1V11f(0x4b8)

    Begin block 0x4b8B0x11f
    prev=[0x6c3B0x48fB0x11f], succ=[0x975]
    =================================
    0x4b9S0x11f: v4b9V11f(0x40) = CONST 
    0x4bcS0x11f: v4bcV11f = MLOAD v4b9V11f(0x40)
    0x4bdS0x11f: v4bdV11f(0x1) = CONST 
    0x4bfS0x11f: v4bfV11f(0xa0) = CONST 
    0x4c1S0x11f: v4c1V11f(0x2) = CONST 
    0x4c3S0x11f: v4c3V11f(0x10000000000000000000000000000000000000000) = EXP v4c1V11f(0x2), v4bfV11f(0xa0)
    0x4c4S0x11f: v4c4V11f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4c3V11f(0x10000000000000000000000000000000000000000), v4bdV11f(0x1)
    0x4c7S0x11f: v4c7V11f = AND v4c4V11f(0xffffffffffffffffffffffffffffffffffffffff), v6e5V48fV11f
    0x4c9S0x11f: MSTORE v4bcV11f, v4c7V11f
    0x4ccS0x11f: v4ccV11f = AND v12f, v4c4V11f(0xffffffffffffffffffffffffffffffffffffffff)
    0x4cdS0x11f: v4cdV11f(0x20) = CONST 
    0x4d0S0x11f: v4d0V11f = ADD v4bcV11f, v4cdV11f(0x20)
    0x4d1S0x11f: MSTORE v4d0V11f, v4ccV11f
    0x4d3S0x11f: v4d3V11f = MLOAD v4b9V11f(0x40)
    0x4d7S0x11f: v4d7V11f(0x0) = SUB v4bcV11f, v4d3V11f
    0x4d8S0x11f: v4d8V11f(0x40) = ADD v4d7V11f(0x0), v4b9V11f(0x40)
    0x4daS0x11f: LOG1 v4d3V11f, v4d8V11f(0x40), v490V11f(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x4dcS0x11f: JUMP v121(0x975)

    Begin block 0x975
    prev=[0x4b8B0x11f, 0xae5B0x11f], succ=[]
    =================================
    0x976: STOP 

    Begin block 0xae5B0x11f
    prev=[0x2c5B0x11f], succ=[0x975]
    =================================
    0xae7S0x11f: JUMP v121(0x975)

}

function updateAdmin()() public {
    Begin block 0x134
    prev=[], succ=[0x13c, 0x140]
    =================================
    0x135: v135 = CALLVALUE 
    0x137: v137 = ISZERO v135
    0x138: v138(0x140) = CONST 
    0x13b: JUMPI v138(0x140), v137

    Begin block 0x13c
    prev=[0x134], succ=[]
    =================================
    0x13c: v13c(0x0) = CONST 
    0x13f: REVERT v13c(0x0), v13c(0x0)

    Begin block 0x140
    prev=[0x134], succ=[0x4dd]
    =================================
    0x142: v142(0x996) = CONST 
    0x145: v145(0x4dd) = CONST 
    0x148: JUMP v145(0x4dd)

    Begin block 0x4dd
    prev=[0x140], succ=[0x6e8B0x4dd]
    =================================
    0x4de: v4de(0x0) = CONST 
    0x4e0: v4e0(0x4e7) = CONST 
    0x4e3: v4e3(0x6e8) = CONST 
    0x4e6: JUMP v4e3(0x6e8)

    Begin block 0x6e8B0x4dd
    prev=[0x4dd], succ=[0x4e7]
    =================================
    0x6e9S0x4dd: v6e9V4dd(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x70aS0x4dd: v70aV4dd = SLOAD v6e9V4dd(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x70cS0x4dd: JUMP v4e0(0x4e7)

    Begin block 0x4e7
    prev=[0x6e8B0x4dd], succ=[0x4fa, 0x56f]
    =================================
    0x4ea: v4ea(0x1) = CONST 
    0x4ec: v4ec(0xa0) = CONST 
    0x4ee: v4ee(0x2) = CONST 
    0x4f0: v4f0(0x10000000000000000000000000000000000000000) = EXP v4ee(0x2), v4ec(0xa0)
    0x4f1: v4f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f0(0x10000000000000000000000000000000000000000), v4ea(0x1)
    0x4f3: v4f3 = AND v70aV4dd, v4f1(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f4: v4f4 = ISZERO v4f3
    0x4f5: v4f5 = ISZERO v4f4
    0x4f6: v4f6(0x56f) = CONST 
    0x4f9: JUMPI v4f6(0x56f), v4f5

    Begin block 0x4fa
    prev=[0x4e7], succ=[]
    =================================
    0x4fa: v4fa(0x40) = CONST 
    0x4fd: v4fd = MLOAD v4fa(0x40)
    0x4fe: v4fe(0xe5) = CONST 
    0x500: v500(0x2) = CONST 
    0x502: v502(0x2000000000000000000000000000000000000000000000000000000000) = EXP v500(0x2), v4fe(0xe5)
    0x503: v503(0x461bcd) = CONST 
    0x507: v507(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v503(0x461bcd), v502(0x2000000000000000000000000000000000000000000000000000000000)
    0x509: MSTORE v4fd, v507(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x50a: v50a(0x20) = CONST 
    0x50c: v50c(0x4) = CONST 
    0x50f: v50f = ADD v4fd, v50c(0x4)
    0x510: MSTORE v50f, v50a(0x20)
    0x511: v511(0x36) = CONST 
    0x513: v513(0x24) = CONST 
    0x516: v516 = ADD v4fd, v513(0x24)
    0x517: MSTORE v516, v511(0x36)
    0x518: v518(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f) = CONST 
    0x539: v539(0x44) = CONST 
    0x53c: v53c = ADD v4fd, v539(0x44)
    0x53d: MSTORE v53c, v518(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f)
    0x53e: v53e(0x787920746f20746865207a65726f206164647265737300000000000000000000) = CONST 
    0x55f: v55f(0x64) = CONST 
    0x562: v562 = ADD v4fd, v55f(0x64)
    0x563: MSTORE v562, v53e(0x787920746f20746865207a65726f206164647265737300000000000000000000)
    0x565: v565 = MLOAD v4fa(0x40)
    0x569: v569(0x0) = SUB v4fd, v565
    0x56a: v56a(0x84) = CONST 
    0x56c: v56c(0x84) = ADD v56a(0x84), v569(0x0)
    0x56e: REVERT v565, v56c(0x84)

    Begin block 0x56f
    prev=[0x4e7], succ=[0x580, 0x5f5]
    =================================
    0x570: v570 = CALLER 
    0x571: v571(0x1) = CONST 
    0x573: v573(0xa0) = CONST 
    0x575: v575(0x2) = CONST 
    0x577: v577(0x10000000000000000000000000000000000000000) = EXP v575(0x2), v573(0xa0)
    0x578: v578(0xffffffffffffffffffffffffffffffffffffffff) = SUB v577(0x10000000000000000000000000000000000000000), v571(0x1)
    0x57a: v57a = AND v70aV4dd, v578(0xffffffffffffffffffffffffffffffffffffffff)
    0x57b: v57b = EQ v57a, v570
    0x57c: v57c(0x5f5) = CONST 
    0x57f: JUMPI v57c(0x5f5), v57b

    Begin block 0x580
    prev=[0x56f], succ=[]
    =================================
    0x580: v580(0x40) = CONST 
    0x583: v583 = MLOAD v580(0x40)
    0x584: v584(0xe5) = CONST 
    0x586: v586(0x2) = CONST 
    0x588: v588(0x2000000000000000000000000000000000000000000000000000000000) = EXP v586(0x2), v584(0xe5)
    0x589: v589(0x461bcd) = CONST 
    0x58d: v58d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v589(0x461bcd), v588(0x2000000000000000000000000000000000000000000000000000000000)
    0x58f: MSTORE v583, v58d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x590: v590(0x20) = CONST 
    0x592: v592(0x4) = CONST 
    0x595: v595 = ADD v583, v592(0x4)
    0x596: MSTORE v595, v590(0x20)
    0x597: v597(0x2a) = CONST 
    0x599: v599(0x24) = CONST 
    0x59c: v59c = ADD v583, v599(0x24)
    0x59d: MSTORE v59c, v597(0x2a)
    0x59e: v59e(0x6d73672e73656e64657220616e64206e657741646d696e206d75737420626520) = CONST 
    0x5bf: v5bf(0x44) = CONST 
    0x5c2: v5c2 = ADD v583, v5bf(0x44)
    0x5c3: MSTORE v5c2, v59e(0x6d73672e73656e64657220616e64206e657741646d696e206d75737420626520)
    0x5c4: v5c4(0x7468652073616d65202e00000000000000000000000000000000000000000000) = CONST 
    0x5e5: v5e5(0x64) = CONST 
    0x5e8: v5e8 = ADD v583, v5e5(0x64)
    0x5e9: MSTORE v5e8, v5c4(0x7468652073616d65202e00000000000000000000000000000000000000000000)
    0x5eb: v5eb = MLOAD v580(0x40)
    0x5ef: v5ef(0x0) = SUB v583, v5eb
    0x5f0: v5f0(0x84) = CONST 
    0x5f2: v5f2(0x84) = ADD v5f0(0x84), v5ef(0x0)
    0x5f4: REVERT v5eb, v5f2(0x84)

    Begin block 0x5f5
    prev=[0x56f], succ=[0x779]
    =================================
    0x5f6: v5f6(0x5fe) = CONST 
    0x5fa: v5fa(0x779) = CONST 
    0x5fd: JUMP v5fa(0x779)

    Begin block 0x779
    prev=[0x5f5], succ=[0x5fe]
    =================================
    0x77a: v77a(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x79b: SSTORE v77a(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b), v70aV4dd
    0x79c: JUMP v5f6(0x5fe)

    Begin block 0x5fe
    prev=[0x779], succ=[0x755B0x5fe]
    =================================
    0x5ff: v5ff(0x608) = CONST 
    0x602: v602(0x0) = CONST 
    0x604: v604(0x755) = CONST 
    0x607: JUMP v604(0x755), v602(0x0), v5ff(0x608)

    Begin block 0x755B0x5fe
    prev=[0x5fe], succ=[0x608]
    =================================
    0x756S0x5fe: v756V5fe(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x777S0x5fe: SSTORE v756V5fe(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c), v602(0x0)
    0x778S0x5fe: JUMP v5ff(0x608)

    Begin block 0x608
    prev=[0x755B0x5fe], succ=[0x996]
    =================================
    0x609: v609(0x40) = CONST 
    0x60c: v60c = MLOAD v609(0x40)
    0x60d: v60d(0x1) = CONST 
    0x60f: v60f(0xa0) = CONST 
    0x611: v611(0x2) = CONST 
    0x613: v613(0x10000000000000000000000000000000000000000) = EXP v611(0x2), v60f(0xa0)
    0x614: v614(0xffffffffffffffffffffffffffffffffffffffff) = SUB v613(0x10000000000000000000000000000000000000000), v60d(0x1)
    0x616: v616 = AND v70aV4dd, v614(0xffffffffffffffffffffffffffffffffffffffff)
    0x618: MSTORE v60c, v616
    0x61a: v61a = MLOAD v609(0x40)
    0x61b: v61b(0x54e4612788f90384e6843298d7854436f3a585b2c3831ab66abf1de63bfa6c2d) = CONST 
    0x63f: v63f(0x0) = SUB v60c, v61a
    0x640: v640(0x20) = CONST 
    0x642: v642(0x20) = ADD v640(0x20), v63f(0x0)
    0x644: LOG1 v61a, v642(0x20), v61b(0x54e4612788f90384e6843298d7854436f3a585b2c3831ab66abf1de63bfa6c2d)
    0x646: JUMP v142(0x996)

    Begin block 0x996
    prev=[0x608], succ=[]
    =================================
    0x997: STOP 

}

function admin()() public {
    Begin block 0x149
    prev=[], succ=[0x151, 0x155]
    =================================
    0x14a: v14a = CALLVALUE 
    0x14c: v14c = ISZERO v14a
    0x14d: v14d(0x155) = CONST 
    0x150: JUMPI v14d(0x155), v14c

    Begin block 0x151
    prev=[0x149], succ=[]
    =================================
    0x151: v151(0x0) = CONST 
    0x154: REVERT v151(0x0), v151(0x0)

    Begin block 0x155
    prev=[0x149], succ=[0x9b7]
    =================================
    0x157: v157(0x9b7) = CONST 
    0x15a: v15a(0x647) = CONST 
    0x15d: v15d_0 = CALLPRIVATE v15a(0x647), v157(0x9b7)

    Begin block 0x9b7
    prev=[0x155], succ=[]
    =================================
    0x9b8: v9b8(0x40) = CONST 
    0x9bb: v9bb = MLOAD v9b8(0x40)
    0x9bc: v9bc(0x1) = CONST 
    0x9be: v9be(0xa0) = CONST 
    0x9c0: v9c0(0x2) = CONST 
    0x9c2: v9c2(0x10000000000000000000000000000000000000000) = EXP v9c0(0x2), v9be(0xa0)
    0x9c3: v9c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9c2(0x10000000000000000000000000000000000000000), v9bc(0x1)
    0x9c6: v9c6 = AND v15d_0, v9c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x9c8: MSTORE v9bb, v9c6
    0x9c9: v9c9 = MLOAD v9b8(0x40)
    0x9cd: v9cd(0x0) = SUB v9bb, v9c9
    0x9ce: v9ce(0x20) = CONST 
    0x9d0: v9d0(0x20) = ADD v9ce(0x20), v9cd(0x0)
    0x9d2: RETURN v9c9, v9d0(0x20)

}

function 0x178(0x178arg0x0) private {
    Begin block 0x178
    prev=[], succ=[0x6c3B0x178]
    =================================
    0x179: v179(0x0) = CONST 
    0x17b: v17b(0x182) = CONST 
    0x17e: v17e(0x6c3) = CONST 
    0x181: JUMP v17e(0x6c3)

    Begin block 0x6c3B0x178
    prev=[0x178], succ=[0x182]
    =================================
    0x6c4S0x178: v6c4V178(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x178: v6e5V178 = SLOAD v6c4V178(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x178: JUMP v17b(0x182)

    Begin block 0x182
    prev=[0x6c3B0x178], succ=[0x19c, 0xa13]
    =================================
    0x183: v183(0x1) = CONST 
    0x185: v185(0xa0) = CONST 
    0x187: v187(0x2) = CONST 
    0x189: v189(0x10000000000000000000000000000000000000000) = EXP v187(0x2), v185(0xa0)
    0x18a: v18a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v189(0x10000000000000000000000000000000000000000), v183(0x1)
    0x18b: v18b = AND v18a(0xffffffffffffffffffffffffffffffffffffffff), v6e5V178
    0x18c: v18c = CALLER 
    0x18d: v18d(0x1) = CONST 
    0x18f: v18f(0xa0) = CONST 
    0x191: v191(0x2) = CONST 
    0x193: v193(0x10000000000000000000000000000000000000000) = EXP v191(0x2), v18f(0xa0)
    0x194: v194(0xffffffffffffffffffffffffffffffffffffffff) = SUB v193(0x10000000000000000000000000000000000000000), v18d(0x1)
    0x195: v195 = AND v194(0xffffffffffffffffffffffffffffffffffffffff), v18c
    0x196: v196 = EQ v195, v18b
    0x197: v197 = ISZERO v196
    0x198: v198(0xa13) = CONST 
    0x19b: JUMPI v198(0xa13), v197

    Begin block 0x19c
    prev=[0x182], succ=[0x6e8B0x19c]
    =================================
    0x19c: v19c(0x1a3) = CONST 
    0x19f: v19f(0x6e8) = CONST 
    0x1a2: JUMP v19f(0x6e8)

    Begin block 0x6e8B0x19c
    prev=[0x19c], succ=[0x1a30x178]
    =================================
    0x6e9S0x19c: v6e9V19c(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x70aS0x19c: v70aV19c = SLOAD v6e9V19c(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x70cS0x19c: JUMP v19c(0x1a3)

    Begin block 0x1a30x178
    prev=[0x6e8B0x19c], succ=[0x1a60x178]
    =================================

    Begin block 0x1a60x178
    prev=[0x1a30x178], succ=[]
    =================================
    0x1a80x178: RETURNPRIVATE v178arg0, v70aV19c

    Begin block 0xa13
    prev=[0x182], succ=[]
    =================================
    0xa15: RETURNPRIVATE v178arg0, v179(0x0)

}

function 0x292(0x292arg0x0) private {
    Begin block 0x292
    prev=[], succ=[0x6c3B0x292]
    =================================
    0x293: v293(0x0) = CONST 
    0x295: v295(0x29c) = CONST 
    0x298: v298(0x6c3) = CONST 
    0x29b: JUMP v298(0x6c3)

    Begin block 0x6c3B0x292
    prev=[0x292], succ=[0x29c]
    =================================
    0x6c4S0x292: v6c4V292(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x292: v6e5V292 = SLOAD v6c4V292(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x292: JUMP v295(0x29c)

    Begin block 0x29c
    prev=[0x6c3B0x292], succ=[0x2b6, 0xac3]
    =================================
    0x29d: v29d(0x1) = CONST 
    0x29f: v29f(0xa0) = CONST 
    0x2a1: v2a1(0x2) = CONST 
    0x2a3: v2a3(0x10000000000000000000000000000000000000000) = EXP v2a1(0x2), v29f(0xa0)
    0x2a4: v2a4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a3(0x10000000000000000000000000000000000000000), v29d(0x1)
    0x2a5: v2a5 = AND v2a4(0xffffffffffffffffffffffffffffffffffffffff), v6e5V292
    0x2a6: v2a6 = CALLER 
    0x2a7: v2a7(0x1) = CONST 
    0x2a9: v2a9(0xa0) = CONST 
    0x2ab: v2ab(0x2) = CONST 
    0x2ad: v2ad(0x10000000000000000000000000000000000000000) = EXP v2ab(0x2), v2a9(0xa0)
    0x2ae: v2ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ad(0x10000000000000000000000000000000000000000), v2a7(0x1)
    0x2af: v2af = AND v2ae(0xffffffffffffffffffffffffffffffffffffffff), v2a6
    0x2b0: v2b0 = EQ v2af, v2a5
    0x2b1: v2b1 = ISZERO v2b0
    0x2b2: v2b2(0xac3) = CONST 
    0x2b5: JUMPI v2b2(0xac3), v2b1

    Begin block 0x2b6
    prev=[0x29c], succ=[0x67aB0x2b6]
    =================================
    0x2b6: v2b6(0x1a3) = CONST 
    0x2b9: v2b9(0x67a) = CONST 
    0x2bc: JUMP v2b9(0x67a)

    Begin block 0x67aB0x2b6
    prev=[0x2b6], succ=[0x1a30x292]
    =================================
    0x67bS0x2b6: v67bV2b6(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x69cS0x2b6: v69cV2b6 = SLOAD v67bV2b6(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x69eS0x2b6: JUMP v2b6(0x1a3)

    Begin block 0x1a30x292
    prev=[0x67aB0x2b6], succ=[0x1a60x292]
    =================================

    Begin block 0x1a60x292
    prev=[0x1a30x292], succ=[]
    =================================
    0x1a80x292: RETURNPRIVATE v292arg0, v69cV2b6

    Begin block 0xac3
    prev=[0x29c], succ=[]
    =================================
    0xac5: RETURNPRIVATE v292arg0, v293(0x0)

}

function 0x647(0x647arg0x0) private {
    Begin block 0x647
    prev=[], succ=[0x6c3B0x647]
    =================================
    0x648: v648(0x0) = CONST 
    0x64a: v64a(0x651) = CONST 
    0x64d: v64d(0x6c3) = CONST 
    0x650: JUMP v64d(0x6c3)

    Begin block 0x6c3B0x647
    prev=[0x647], succ=[0x651]
    =================================
    0x6c4S0x647: v6c4V647(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x647: v6e5V647 = SLOAD v6c4V647(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x647: JUMP v64a(0x651)

    Begin block 0x651
    prev=[0x6c3B0x647], succ=[0x66b, 0xb07]
    =================================
    0x652: v652(0x1) = CONST 
    0x654: v654(0xa0) = CONST 
    0x656: v656(0x2) = CONST 
    0x658: v658(0x10000000000000000000000000000000000000000) = EXP v656(0x2), v654(0xa0)
    0x659: v659(0xffffffffffffffffffffffffffffffffffffffff) = SUB v658(0x10000000000000000000000000000000000000000), v652(0x1)
    0x65a: v65a = AND v659(0xffffffffffffffffffffffffffffffffffffffff), v6e5V647
    0x65b: v65b = CALLER 
    0x65c: v65c(0x1) = CONST 
    0x65e: v65e(0xa0) = CONST 
    0x660: v660(0x2) = CONST 
    0x662: v662(0x10000000000000000000000000000000000000000) = EXP v660(0x2), v65e(0xa0)
    0x663: v663(0xffffffffffffffffffffffffffffffffffffffff) = SUB v662(0x10000000000000000000000000000000000000000), v65c(0x1)
    0x664: v664 = AND v663(0xffffffffffffffffffffffffffffffffffffffff), v65b
    0x665: v665 = EQ v664, v65a
    0x666: v666 = ISZERO v665
    0x667: v667(0xb07) = CONST 
    0x66a: JUMPI v667(0xb07), v666

    Begin block 0x66b
    prev=[0x651], succ=[0x6c3B0x66b]
    =================================
    0x66b: v66b(0x1a3) = CONST 
    0x66e: v66e(0x6c3) = CONST 
    0x671: JUMP v66e(0x6c3)

    Begin block 0x6c3B0x66b
    prev=[0x66b], succ=[0x1a30x647]
    =================================
    0x6c4S0x66b: v6c4V66b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x66b: v6e5V66b = SLOAD v6c4V66b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x66b: JUMP v66b(0x1a3)

    Begin block 0x1a30x647
    prev=[0x6c3B0x66b], succ=[0x1a60x647]
    =================================

    Begin block 0x1a60x647
    prev=[0x1a30x647], succ=[]
    =================================
    0x1a80x647: RETURNPRIVATE v647arg0, v6e5V66b

    Begin block 0xb07
    prev=[0x651], succ=[]
    =================================
    0xb09: RETURNPRIVATE v647arg0, v648(0x0)

}

function 0x70d(0x70darg0x0, 0x70darg0x1) private {
    Begin block 0x70d
    prev=[], succ=[0x79d]
    =================================
    0x70e: v70e(0x716) = CONST 
    0x712: v712(0x79d) = CONST 
    0x715: JUMP v712(0x79d)

    Begin block 0x79d
    prev=[0x70d], succ=[0x849]
    =================================
    0x79e: v79e(0x0) = CONST 
    0x7a0: v7a0(0x7a8) = CONST 
    0x7a4: v7a4(0x849) = CONST 
    0x7a7: JUMP v7a4(0x849)

    Begin block 0x849
    prev=[0x79d], succ=[0x7a8]
    =================================
    0x84a: v84a(0x0) = CONST 
    0x84d: v84d = EXTCODESIZE v70darg0
    0x84e: v84e = GT v84d, v84a(0x0)
    0x850: JUMP v7a0(0x7a8)

    Begin block 0x7a8
    prev=[0x849], succ=[0x7af, 0x824]
    =================================
    0x7a9: v7a9 = ISZERO v84e
    0x7aa: v7aa = ISZERO v7a9
    0x7ab: v7ab(0x824) = CONST 
    0x7ae: JUMPI v7ab(0x824), v7aa

    Begin block 0x7af
    prev=[0x7a8], succ=[]
    =================================
    0x7af: v7af(0x40) = CONST 
    0x7b2: v7b2 = MLOAD v7af(0x40)
    0x7b3: v7b3(0xe5) = CONST 
    0x7b5: v7b5(0x2) = CONST 
    0x7b7: v7b7(0x2000000000000000000000000000000000000000000000000000000000) = EXP v7b5(0x2), v7b3(0xe5)
    0x7b8: v7b8(0x461bcd) = CONST 
    0x7bc: v7bc(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v7b8(0x461bcd), v7b7(0x2000000000000000000000000000000000000000000000000000000000)
    0x7be: MSTORE v7b2, v7bc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7bf: v7bf(0x20) = CONST 
    0x7c1: v7c1(0x4) = CONST 
    0x7c4: v7c4 = ADD v7b2, v7c1(0x4)
    0x7c5: MSTORE v7c4, v7bf(0x20)
    0x7c6: v7c6(0x3b) = CONST 
    0x7c8: v7c8(0x24) = CONST 
    0x7cb: v7cb = ADD v7b2, v7c8(0x24)
    0x7cc: MSTORE v7cb, v7c6(0x3b)
    0x7cd: v7cd(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f) = CONST 
    0x7ee: v7ee(0x44) = CONST 
    0x7f1: v7f1 = ADD v7b2, v7ee(0x44)
    0x7f2: MSTORE v7f1, v7cd(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f)
    0x7f3: v7f3(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000) = CONST 
    0x814: v814(0x64) = CONST 
    0x817: v817 = ADD v7b2, v814(0x64)
    0x818: MSTORE v817, v7f3(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000)
    0x81a: v81a = MLOAD v7af(0x40)
    0x81e: v81e(0x0) = SUB v7b2, v81a
    0x81f: v81f(0x84) = CONST 
    0x821: v821(0x84) = ADD v81f(0x84), v81e(0x0)
    0x823: REVERT v81a, v821(0x84)

    Begin block 0x824
    prev=[0x7a8], succ=[0x716]
    =================================
    0x826: v826(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x847: SSTORE v826(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), v70darg0
    0x848: JUMP v70e(0x716)

    Begin block 0x716
    prev=[0x824], succ=[]
    =================================
    0x717: v717(0x40) = CONST 
    0x71a: v71a = MLOAD v717(0x40)
    0x71b: v71b(0x1) = CONST 
    0x71d: v71d(0xa0) = CONST 
    0x71f: v71f(0x2) = CONST 
    0x721: v721(0x10000000000000000000000000000000000000000) = EXP v71f(0x2), v71d(0xa0)
    0x722: v722(0xffffffffffffffffffffffffffffffffffffffff) = SUB v721(0x10000000000000000000000000000000000000000), v71b(0x1)
    0x724: v724 = AND v70darg0, v722(0xffffffffffffffffffffffffffffffffffffffff)
    0x726: MSTORE v71a, v724
    0x728: v728 = MLOAD v717(0x40)
    0x729: v729(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x74d: v74d(0x0) = SUB v71a, v728
    0x74e: v74e(0x20) = CONST 
    0x750: v750(0x20) = ADD v74e(0x20), v74d(0x0)
    0x752: LOG1 v728, v750(0x20), v729(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b)
    0x754: RETURNPRIVATE v70darg1

}

function fallback()() public {
    Begin block 0x82
    prev=[], succ=[0x15e]
    =================================
    0x83: v83(0x89c) = CONST 
    0x86: v86(0x15e) = CONST 
    0x89: JUMP v86(0x15e)

    Begin block 0x15e
    prev=[0x82], succ=[0x672B0x15e]
    =================================
    0x15f: v15f(0x166) = CONST 
    0x162: v162(0x672) = CONST 
    0x165: JUMP v162(0x672), v15f(0x166)

    Begin block 0x672B0x15e
    prev=[0x15e], succ=[0xb4aB0x672B0x15e]
    =================================
    0x673S0x15e: v673V15e(0xb29) = CONST 
    0x676S0x15e: v676V15e(0xb4a) = CONST 
    0x679S0x15e: JUMP v676V15e(0xb4a), v673V15e(0xb29)

    Begin block 0xb4aB0x672B0x15e
    prev=[0x672B0x15e], succ=[0xb29B0x15e]
    =================================
    0xb4bS0x672S0x15e: JUMP v673V15e(0xb29)

    Begin block 0xb29B0x15e
    prev=[0xb4aB0x672B0x15e], succ=[0x166]
    =================================
    0xb2aS0x15e: JUMP v15f(0x166)

    Begin block 0x166
    prev=[0xb29B0x15e], succ=[0x67aB0x166]
    =================================
    0x167: v167(0x9f2) = CONST 
    0x16a: v16a(0x171) = CONST 
    0x16d: v16d(0x67a) = CONST 
    0x170: JUMP v16d(0x67a)

    Begin block 0x67aB0x166
    prev=[0x166], succ=[0x171]
    =================================
    0x67bS0x166: v67bV166(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x69cS0x166: v69cV166 = SLOAD v67bV166(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x69eS0x166: JUMP v16a(0x171)

    Begin block 0x171
    prev=[0x67aB0x166], succ=[0x69f]
    =================================
    0x172: v172(0x69f) = CONST 
    0x175: JUMP v172(0x69f)

    Begin block 0x69f
    prev=[0x171], succ=[0x6ba, 0x6be]
    =================================
    0x6a0: v6a0 = CALLDATASIZE 
    0x6a1: v6a1(0x0) = CONST 
    0x6a4: CALLDATACOPY v6a1(0x0), v6a1(0x0), v6a0
    0x6a5: v6a5(0x0) = CONST 
    0x6a8: v6a8 = CALLDATASIZE 
    0x6a9: v6a9(0x0) = CONST 
    0x6ac: v6ac = GAS 
    0x6ad: v6ad = DELEGATECALL v6ac, v69cV166, v6a9(0x0), v6a8, v6a5(0x0), v6a5(0x0)
    0x6ae: v6ae = RETURNDATASIZE 
    0x6af: v6af(0x0) = CONST 
    0x6b2: RETURNDATACOPY v6af(0x0), v6af(0x0), v6ae
    0x6b5: v6b5 = ISZERO v6ad
    0x6b6: v6b6(0x6be) = CONST 
    0x6b9: JUMPI v6b6(0x6be), v6b5

    Begin block 0x6ba
    prev=[0x69f], succ=[]
    =================================
    0x6ba: v6ba = RETURNDATASIZE 
    0x6bb: v6bb(0x0) = CONST 
    0x6bd: RETURN v6bb(0x0), v6ba

    Begin block 0x6be
    prev=[0x69f], succ=[]
    =================================
    0x6bf: v6bf = RETURNDATASIZE 
    0x6c0: v6c0(0x0) = CONST 
    0x6c2: REVERT v6c0(0x0), v6bf

}

function pendingAdmin()() public {
    Begin block 0x8c
    prev=[], succ=[0x94, 0x98]
    =================================
    0x8d: v8d = CALLVALUE 
    0x8f: v8f = ISZERO v8d
    0x90: v90(0x98) = CONST 
    0x93: JUMPI v90(0x98), v8f

    Begin block 0x94
    prev=[0x8c], succ=[]
    =================================
    0x94: v94(0x0) = CONST 
    0x97: REVERT v94(0x0), v94(0x0)

    Begin block 0x98
    prev=[0x8c], succ=[0x8bd]
    =================================
    0x9a: v9a(0x8bd) = CONST 
    0x9d: v9d(0x178) = CONST 
    0xa0: va0_0 = CALLPRIVATE v9d(0x178), v9a(0x8bd)

    Begin block 0x8bd
    prev=[0x98], succ=[]
    =================================
    0x8be: v8be(0x40) = CONST 
    0x8c1: v8c1 = MLOAD v8be(0x40)
    0x8c2: v8c2(0x1) = CONST 
    0x8c4: v8c4(0xa0) = CONST 
    0x8c6: v8c6(0x2) = CONST 
    0x8c8: v8c8(0x10000000000000000000000000000000000000000) = EXP v8c6(0x2), v8c4(0xa0)
    0x8c9: v8c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8c8(0x10000000000000000000000000000000000000000), v8c2(0x1)
    0x8cc: v8cc = AND va0_0, v8c9(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ce: MSTORE v8c1, v8cc
    0x8cf: v8cf = MLOAD v8be(0x40)
    0x8d3: v8d3(0x0) = SUB v8c1, v8cf
    0x8d4: v8d4(0x20) = CONST 
    0x8d6: v8d6(0x20) = ADD v8d4(0x20), v8d3(0x0)
    0x8d8: RETURN v8cf, v8d6(0x20)

}

function upgradeTo(address)() public {
    Begin block 0xbd
    prev=[], succ=[0xc5, 0xc9]
    =================================
    0xbe: vbe = CALLVALUE 
    0xc0: vc0 = ISZERO vbe
    0xc1: vc1(0xc9) = CONST 
    0xc4: JUMPI vc1(0xc9), vc0

    Begin block 0xc5
    prev=[0xbd], succ=[]
    =================================
    0xc5: vc5(0x0) = CONST 
    0xc8: REVERT vc5(0x0), vc5(0x0)

    Begin block 0xc9
    prev=[0xbd], succ=[0x1a9B0xc9]
    =================================
    0xcb: vcb(0x8f8) = CONST 
    0xce: vce(0x1) = CONST 
    0xd0: vd0(0xa0) = CONST 
    0xd2: vd2(0x2) = CONST 
    0xd4: vd4(0x10000000000000000000000000000000000000000) = EXP vd2(0x2), vd0(0xa0)
    0xd5: vd5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd4(0x10000000000000000000000000000000000000000), vce(0x1)
    0xd6: vd6(0x4) = CONST 
    0xd8: vd8 = CALLDATALOAD vd6(0x4)
    0xd9: vd9 = AND vd8, vd5(0xffffffffffffffffffffffffffffffffffffffff)
    0xda: vda(0x1a9) = CONST 
    0xdd: JUMP vda(0x1a9), vd9, vcb(0x8f8)

    Begin block 0x1a9B0xc9
    prev=[0xc9], succ=[0x6c3B0x1a9B0xc9]
    =================================
    0x1aaS0xc9: v1aaVc9(0x1b1) = CONST 
    0x1adS0xc9: v1adVc9(0x6c3) = CONST 
    0x1b0S0xc9: JUMP v1adVc9(0x6c3)

    Begin block 0x6c3B0x1a9B0xc9
    prev=[0x1a9B0xc9], succ=[0x1b1B0xc9]
    =================================
    0x6c4S0x1a9S0xc9: v6c4V1a9Vc9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x1a9S0xc9: v6e5V1a9Vc9 = SLOAD v6c4V1a9Vc9(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x1a9S0xc9: JUMP v1aaVc9(0x1b1)

    Begin block 0x1b1B0xc9
    prev=[0x6c3B0x1a9B0xc9], succ=[0x1cbB0xc9, 0xa35B0xc9]
    =================================
    0x1b2S0xc9: v1b2Vc9(0x1) = CONST 
    0x1b4S0xc9: v1b4Vc9(0xa0) = CONST 
    0x1b6S0xc9: v1b6Vc9(0x2) = CONST 
    0x1b8S0xc9: v1b8Vc9(0x10000000000000000000000000000000000000000) = EXP v1b6Vc9(0x2), v1b4Vc9(0xa0)
    0x1b9S0xc9: v1b9Vc9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b8Vc9(0x10000000000000000000000000000000000000000), v1b2Vc9(0x1)
    0x1baS0xc9: v1baVc9 = AND v1b9Vc9(0xffffffffffffffffffffffffffffffffffffffff), v6e5V1a9Vc9
    0x1bbS0xc9: v1bbVc9 = CALLER 
    0x1bcS0xc9: v1bcVc9(0x1) = CONST 
    0x1beS0xc9: v1beVc9(0xa0) = CONST 
    0x1c0S0xc9: v1c0Vc9(0x2) = CONST 
    0x1c2S0xc9: v1c2Vc9(0x10000000000000000000000000000000000000000) = EXP v1c0Vc9(0x2), v1beVc9(0xa0)
    0x1c3S0xc9: v1c3Vc9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c2Vc9(0x10000000000000000000000000000000000000000), v1bcVc9(0x1)
    0x1c4S0xc9: v1c4Vc9 = AND v1c3Vc9(0xffffffffffffffffffffffffffffffffffffffff), v1bbVc9
    0x1c5S0xc9: v1c5Vc9 = EQ v1c4Vc9, v1baVc9
    0x1c6S0xc9: v1c6Vc9 = ISZERO v1c5Vc9
    0x1c7S0xc9: v1c7Vc9(0xa35) = CONST 
    0x1caS0xc9: JUMPI v1c7Vc9(0xa35), v1c6Vc9

    Begin block 0x1cbB0xc9
    prev=[0x1b1B0xc9], succ=[0xa57B0xc9]
    =================================
    0x1cbS0xc9: v1cbVc9(0xa57) = CONST 
    0x1cfS0xc9: v1cfVc9(0x70d) = CONST 
    0x1d2S0xc9: CALLPRIVATE v1cfVc9(0x70d), vd9, v1cbVc9(0xa57)

    Begin block 0xa57B0xc9
    prev=[0x1cbB0xc9], succ=[0x8f8]
    =================================
    0xa59S0xc9: JUMP vcb(0x8f8)

    Begin block 0x8f8
    prev=[0xa35B0xc9, 0xa57B0xc9], succ=[]
    =================================
    0x8f9: STOP 

    Begin block 0xa35B0xc9
    prev=[0x1b1B0xc9], succ=[0x8f8]
    =================================
    0xa37S0xc9: JUMP vcb(0x8f8)

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xde
    prev=[], succ=[0x1d6B0xde]
    =================================
    0xdf: vdf(0x919) = CONST 
    0xe2: ve2(0x4) = CONST 
    0xe5: ve5 = CALLDATALOAD ve2(0x4)
    0xe6: ve6(0x1) = CONST 
    0xe8: ve8(0xa0) = CONST 
    0xea: vea(0x2) = CONST 
    0xec: vec(0x10000000000000000000000000000000000000000) = EXP vea(0x2), ve8(0xa0)
    0xed: ved(0xffffffffffffffffffffffffffffffffffffffff) = SUB vec(0x10000000000000000000000000000000000000000), ve6(0x1)
    0xee: vee = AND ved(0xffffffffffffffffffffffffffffffffffffffff), ve5
    0xf0: vf0(0x24) = CONST 
    0xf3: vf3 = CALLDATALOAD vf0(0x24)
    0xf6: vf6 = ADD vf3, vf0(0x24)
    0xf8: vf8 = ADD ve2(0x4), vf3
    0xf9: vf9 = CALLDATALOAD vf8
    0xfa: vfa(0x1d6) = CONST 
    0xfd: JUMP vfa(0x1d6), vf9, vf6, vee, vdf(0x919)

    Begin block 0x1d6B0xde
    prev=[0xde], succ=[0x6c3B0x1d6B0xde]
    =================================
    0x1d7S0xde: v1d7Vde(0x0) = CONST 
    0x1d9S0xde: v1d9Vde(0x1e0) = CONST 
    0x1dcS0xde: v1dcVde(0x6c3) = CONST 
    0x1dfS0xde: JUMP v1dcVde(0x6c3)

    Begin block 0x6c3B0x1d6B0xde
    prev=[0x1d6B0xde], succ=[0x1e0B0xde]
    =================================
    0x6c4S0x1d6S0xde: v6c4V1d6Vde(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6e5S0x1d6S0xde: v6e5V1d6Vde = SLOAD v6c4V1d6Vde(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6e7S0x1d6S0xde: JUMP v1d9Vde(0x1e0)

    Begin block 0x1e0B0xde
    prev=[0x6c3B0x1d6B0xde], succ=[0x1faB0xde, 0xa79B0xde]
    =================================
    0x1e1S0xde: v1e1Vde(0x1) = CONST 
    0x1e3S0xde: v1e3Vde(0xa0) = CONST 
    0x1e5S0xde: v1e5Vde(0x2) = CONST 
    0x1e7S0xde: v1e7Vde(0x10000000000000000000000000000000000000000) = EXP v1e5Vde(0x2), v1e3Vde(0xa0)
    0x1e8S0xde: v1e8Vde(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e7Vde(0x10000000000000000000000000000000000000000), v1e1Vde(0x1)
    0x1e9S0xde: v1e9Vde = AND v1e8Vde(0xffffffffffffffffffffffffffffffffffffffff), v6e5V1d6Vde
    0x1eaS0xde: v1eaVde = CALLER 
    0x1ebS0xde: v1ebVde(0x1) = CONST 
    0x1edS0xde: v1edVde(0xa0) = CONST 
    0x1efS0xde: v1efVde(0x2) = CONST 
    0x1f1S0xde: v1f1Vde(0x10000000000000000000000000000000000000000) = EXP v1efVde(0x2), v1edVde(0xa0)
    0x1f2S0xde: v1f2Vde(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f1Vde(0x10000000000000000000000000000000000000000), v1ebVde(0x1)
    0x1f3S0xde: v1f3Vde = AND v1f2Vde(0xffffffffffffffffffffffffffffffffffffffff), v1eaVde
    0x1f4S0xde: v1f4Vde = EQ v1f3Vde, v1e9Vde
    0x1f5S0xde: v1f5Vde = ISZERO v1f4Vde
    0x1f6S0xde: v1f6Vde(0xa79) = CONST 
    0x1f9S0xde: JUMPI v1f6Vde(0xa79), v1f5Vde

    Begin block 0x1faB0xde
    prev=[0x1e0B0xde], succ=[0x202B0xde]
    =================================
    0x1faS0xde: v1faVde(0x202) = CONST 
    0x1feS0xde: v1feVde(0x70d) = CONST 
    0x201S0xde: CALLPRIVATE v1feVde(0x70d), vee, v1faVde(0x202)

    Begin block 0x202B0xde
    prev=[0x1faB0xde], succ=[0x23dB0xde, 0xa9eB0xde]
    =================================
    0x203S0xde: v203Vde = ADDRESS 
    0x204S0xde: v204Vde(0x1) = CONST 
    0x206S0xde: v206Vde(0xa0) = CONST 
    0x208S0xde: v208Vde(0x2) = CONST 
    0x20aS0xde: v20aVde(0x10000000000000000000000000000000000000000) = EXP v208Vde(0x2), v206Vde(0xa0)
    0x20bS0xde: v20bVde(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20aVde(0x10000000000000000000000000000000000000000), v204Vde(0x1)
    0x20cS0xde: v20cVde = AND v20bVde(0xffffffffffffffffffffffffffffffffffffffff), v203Vde
    0x20dS0xde: v20dVde = CALLVALUE 
    0x210S0xde: v210Vde(0x40) = CONST 
    0x212S0xde: v212Vde = MLOAD v210Vde(0x40)
    0x219S0xde: CALLDATACOPY v212Vde, vf6, vf9
    0x21bS0xde: v21bVde = ADD v212Vde, vf9
    0x223S0xde: v223Vde(0x0) = CONST 
    0x225S0xde: v225Vde(0x40) = CONST 
    0x227S0xde: v227Vde = MLOAD v225Vde(0x40)
    0x22aS0xde: v22aVde = SUB v21bVde, v227Vde
    0x22eS0xde: v22eVde = GAS 
    0x22fS0xde: v22fVde = CALL v22eVde, v20cVde, v20dVde, v227Vde, v22aVde, v227Vde, v223Vde(0x0)
    0x237S0xde: v237Vde = ISZERO v22fVde
    0x238S0xde: v238Vde = ISZERO v237Vde
    0x239S0xde: v239Vde(0xa9e) = CONST 
    0x23cS0xde: JUMPI v239Vde(0xa9e), v238Vde

    Begin block 0x23dB0xde
    prev=[0x202B0xde], succ=[]
    =================================
    0x23dS0xde: v23dVde(0x40) = CONST 
    0x240S0xde: v240Vde = MLOAD v23dVde(0x40)
    0x241S0xde: v241Vde(0xe5) = CONST 
    0x243S0xde: v243Vde(0x2) = CONST 
    0x245S0xde: v245Vde(0x2000000000000000000000000000000000000000000000000000000000) = EXP v243Vde(0x2), v241Vde(0xe5)
    0x246S0xde: v246Vde(0x461bcd) = CONST 
    0x24aS0xde: v24aVde(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v246Vde(0x461bcd), v245Vde(0x2000000000000000000000000000000000000000000000000000000000)
    0x24cS0xde: MSTORE v240Vde, v24aVde(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x24dS0xde: v24dVde(0x20) = CONST 
    0x24fS0xde: v24fVde(0x4) = CONST 
    0x252S0xde: v252Vde = ADD v240Vde, v24fVde(0x4)
    0x253S0xde: MSTORE v252Vde, v24dVde(0x20)
    0x254S0xde: v254Vde(0x16) = CONST 
    0x256S0xde: v256Vde(0x24) = CONST 
    0x259S0xde: v259Vde = ADD v240Vde, v256Vde(0x24)
    0x25aS0xde: MSTORE v259Vde, v254Vde(0x16)
    0x25bS0xde: v25bVde(0x75706772616465546f416e6443616c6c2d6572726f7200000000000000000000) = CONST 
    0x27cS0xde: v27cVde(0x44) = CONST 
    0x27fS0xde: v27fVde = ADD v240Vde, v27cVde(0x44)
    0x280S0xde: MSTORE v27fVde, v25bVde(0x75706772616465546f416e6443616c6c2d6572726f7200000000000000000000)
    0x282S0xde: v282Vde = MLOAD v23dVde(0x40)
    0x286S0xde: v286Vde(0x0) = SUB v240Vde, v282Vde
    0x287S0xde: v287Vde(0x64) = CONST 
    0x289S0xde: v289Vde(0x64) = ADD v287Vde(0x64), v286Vde(0x0)
    0x28bS0xde: REVERT v282Vde, v289Vde(0x64)

    Begin block 0xa9eB0xde
    prev=[0x202B0xde], succ=[0x919]
    =================================
    0xaa3S0xde: JUMP vdf(0x919)

    Begin block 0x919
    prev=[0xa79B0xde, 0xa9eB0xde], succ=[]
    =================================
    0x91a: STOP 

    Begin block 0xa79B0xde
    prev=[0x1e0B0xde], succ=[0x919]
    =================================
    0xa7eS0xde: JUMP vdf(0x919)

}

function implementation()() public {
    Begin block 0xfe
    prev=[], succ=[0x106, 0x10a]
    =================================
    0xff: vff = CALLVALUE 
    0x101: v101 = ISZERO vff
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xfe], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xfe], succ=[0x93a]
    =================================
    0x10c: v10c(0x93a) = CONST 
    0x10f: v10f(0x292) = CONST 
    0x112: v112_0 = CALLPRIVATE v10f(0x292), v10c(0x93a)

    Begin block 0x93a
    prev=[0x10a], succ=[]
    =================================
    0x93b: v93b(0x40) = CONST 
    0x93e: v93e = MLOAD v93b(0x40)
    0x93f: v93f(0x1) = CONST 
    0x941: v941(0xa0) = CONST 
    0x943: v943(0x2) = CONST 
    0x945: v945(0x10000000000000000000000000000000000000000) = EXP v943(0x2), v941(0xa0)
    0x946: v946(0xffffffffffffffffffffffffffffffffffffffff) = SUB v945(0x10000000000000000000000000000000000000000), v93f(0x1)
    0x949: v949 = AND v112_0, v946(0xffffffffffffffffffffffffffffffffffffffff)
    0x94b: MSTORE v93e, v949
    0x94c: v94c = MLOAD v93b(0x40)
    0x950: v950(0x0) = SUB v93e, v94c
    0x951: v951(0x20) = CONST 
    0x953: v953(0x20) = ADD v951(0x20), v950(0x0)
    0x955: RETURN v94c, v953(0x20)

}

