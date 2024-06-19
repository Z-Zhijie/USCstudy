function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x23d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x235: v235(0x23d) = CONST 
    0x236: JUMPI v235(0x23d), v8

    Begin block 0xd
    prev=[0x0], succ=[0x240, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5c60da1b) = CONST 
    0x19: v19 = EQ v14(0x5c60da1b), v12
    0x237: v237(0x240) = CONST 
    0x238: JUMPI v237(0x240), v19

    Begin block 0x240
    prev=[0xd], succ=[]
    =================================
    0x241: v241(0x3e) = CONST 
    0x242: CALLPRIVATE v241(0x3e)

    Begin block 0x1e
    prev=[0xd], succ=[0x243, 0x29]
    =================================
    0x1f: v1f(0xd784d426) = CONST 
    0x24: v24 = EQ v1f(0xd784d426), v12
    0x239: v239(0x243) = CONST 
    0x23a: JUMPI v239(0x243), v24

    Begin block 0x243
    prev=[0x1e], succ=[]
    =================================
    0x244: v244(0x8e) = CONST 
    0x245: CALLPRIVATE v244(0x8e)

    Begin block 0x29
    prev=[0x1e], succ=[0x23d, 0x246]
    =================================
    0x2a: v2a(0xf851a440) = CONST 
    0x2f: v2f = EQ v2a(0xf851a440), v12
    0x23b: v23b(0x246) = CONST 
    0x23c: JUMPI v23b(0x246), v2f

    Begin block 0x23d
    prev=[0x0, 0x29], succ=[]
    =================================
    0x23e: v23e(0x34) = CONST 
    0x23f: CALLPRIVATE v23e(0x34)

    Begin block 0x246
    prev=[0x29], succ=[]
    =================================
    0x247: v247(0xae) = CONST 
    0x248: CALLPRIVATE v247(0xae)

}

function fallback()() public {
    Begin block 0x34
    prev=[], succ=[0xdb]
    =================================
    0x35: v35(0x212) = CONST 
    0x38: v38(0xdb) = CONST 
    0x3b: JUMP v38(0xdb)

    Begin block 0xdb
    prev=[0x34], succ=[0xfd]
    =================================
    0xdc: vdc(0x102) = CONST 
    0xdf: vdf(0xfd) = CONST 
    0xe2: ve2(0x0) = CONST 
    0xe4: ve4 = SLOAD ve2(0x0)
    0xe5: ve5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfa: vfa = AND ve5(0xffffffffffffffffffffffffffffffffffffffff), ve4
    0xfc: JUMP vdf(0xfd)

    Begin block 0xfd
    prev=[0xdb], succ=[0x16f]
    =================================
    0xfe: vfe(0x16f) = CONST 
    0x101: JUMP vfe(0x16f)

    Begin block 0x16f
    prev=[0xfd], succ=[0x18a, 0x18e]
    =================================
    0x170: v170 = CALLDATASIZE 
    0x171: v171(0x0) = CONST 
    0x174: CALLDATACOPY v171(0x0), v171(0x0), v170
    0x175: v175(0x0) = CONST 
    0x178: v178 = CALLDATASIZE 
    0x179: v179(0x0) = CONST 
    0x17c: v17c = GAS 
    0x17d: v17d = DELEGATECALL v17c, vfa, v179(0x0), v178, v175(0x0), v175(0x0)
    0x17e: v17e = RETURNDATASIZE 
    0x17f: v17f(0x0) = CONST 
    0x182: RETURNDATACOPY v17f(0x0), v17f(0x0), v17e
    0x185: v185 = ISZERO v17d
    0x186: v186(0x18e) = CONST 
    0x189: JUMPI v186(0x18e), v185

    Begin block 0x18a
    prev=[0x16f], succ=[]
    =================================
    0x18a: v18a = RETURNDATASIZE 
    0x18b: v18b(0x0) = CONST 
    0x18d: RETURN v18b(0x0), v18a

    Begin block 0x18e
    prev=[0x16f], succ=[]
    =================================
    0x18f: v18f = RETURNDATASIZE 
    0x190: v190(0x0) = CONST 
    0x192: REVERT v190(0x0), v18f

}

function implementation()() public {
    Begin block 0x3e
    prev=[], succ=[0x46, 0x4a]
    =================================
    0x3f: v3f = CALLVALUE 
    0x41: v41 = ISZERO v3f
    0x42: v42(0x4a) = CONST 
    0x45: JUMPI v42(0x4a), v41

    Begin block 0x46
    prev=[0x3e], succ=[]
    =================================
    0x46: v46(0x0) = CONST 
    0x49: REVERT v46(0x0), v46(0x0)

    Begin block 0x4a
    prev=[0x3e], succ=[0x650x3e]
    =================================
    0x4c: v4c(0x0) = CONST 
    0x4e: v4e = SLOAD v4c(0x0)
    0x4f: v4f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x64: v64 = AND v4f(0xffffffffffffffffffffffffffffffffffffffff), v4e

    Begin block 0x650x3e
    prev=[0x4a], succ=[]
    =================================
    0x660x3e: v3e66(0x40) = CONST 
    0x680x3e: v3e68 = MLOAD v3e66(0x40)
    0x690x3e: v3e69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x800x3e: v3e80 = AND v64, v3e69(0xffffffffffffffffffffffffffffffffffffffff)
    0x820x3e: MSTORE v3e68, v3e80
    0x830x3e: v3e83(0x20) = CONST 
    0x850x3e: v3e85 = ADD v3e83(0x20), v3e68
    0x860x3e: v3e86(0x40) = CONST 
    0x880x3e: v3e88 = MLOAD v3e86(0x40)
    0x8b0x3e: v3e8b(0x20) = SUB v3e85, v3e88
    0x8d0x3e: RETURN v3e88, v3e8b(0x20)

}

function setImplementation(address)() public {
    Begin block 0x8e
    prev=[], succ=[0x96, 0x9a]
    =================================
    0x8f: v8f = CALLVALUE 
    0x91: v91 = ISZERO v8f
    0x92: v92(0x9a) = CONST 
    0x95: JUMPI v92(0x9a), v91

    Begin block 0x96
    prev=[0x8e], succ=[]
    =================================
    0x96: v96(0x0) = CONST 
    0x99: REVERT v96(0x0), v96(0x0)

    Begin block 0x9a
    prev=[0x8e], succ=[0x193B0x9a]
    =================================
    0x9c: v9c(0x233) = CONST 
    0x9f: v9f(0xa9) = CONST 
    0xa2: va2 = CALLDATASIZE 
    0xa3: va3(0x4) = CONST 
    0xa5: va5(0x193) = CONST 
    0xa8: JUMP va5(0x193)

    Begin block 0x193B0x9a
    prev=[0x9a], succ=[0x1a1B0x9a, 0x1a5B0x9a]
    =================================
    0x194S0x9a: v194V9a(0x0) = CONST 
    0x196S0x9a: v196V9a(0x20) = CONST 
    0x19aS0x9a: v19aV9a = SUB va2, va3(0x4)
    0x19bS0x9a: v19bV9a = SLT v19aV9a, v196V9a(0x20)
    0x19cS0x9a: v19cV9a = ISZERO v19bV9a
    0x19dS0x9a: v19dV9a(0x1a5) = CONST 
    0x1a0S0x9a: JUMPI v19dV9a(0x1a5), v19cV9a

    Begin block 0x1a1B0x9a
    prev=[0x193B0x9a], succ=[]
    =================================
    0x1a1S0x9a: v1a1V9a(0x0) = CONST 
    0x1a4S0x9a: REVERT v1a1V9a(0x0), v1a1V9a(0x0)

    Begin block 0x1a5B0x9a
    prev=[0x193B0x9a], succ=[0x1c5B0x9a, 0x1c9B0x9a]
    =================================
    0x1a7S0x9a: v1a7V9a = CALLDATALOAD va3(0x4)
    0x1a8S0x9a: v1a8V9a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1beS0x9a: v1beV9a = AND v1a7V9a, v1a8V9a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c0S0x9a: v1c0V9a = EQ v1a7V9a, v1beV9a
    0x1c1S0x9a: v1c1V9a(0x1c9) = CONST 
    0x1c4S0x9a: JUMPI v1c1V9a(0x1c9), v1c0V9a

    Begin block 0x1c5B0x9a
    prev=[0x1a5B0x9a], succ=[]
    =================================
    0x1c5S0x9a: v1c5V9a(0x0) = CONST 
    0x1c8S0x9a: REVERT v1c5V9a(0x0), v1c5V9a(0x0)

    Begin block 0x1c9B0x9a
    prev=[0x1a5B0x9a], succ=[0xa9]
    =================================
    0x1cfS0x9a: JUMP v9f(0xa9)

    Begin block 0xa9
    prev=[0x1c9B0x9a], succ=[0x104]
    =================================
    0xaa: vaa(0x104) = CONST 
    0xad: JUMP vaa(0x104)

    Begin block 0x104
    prev=[0xa9], succ=[0x124, 0x128]
    =================================
    0x105: v105(0x1) = CONST 
    0x107: v107 = SLOAD v105(0x1)
    0x108: v108(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11d: v11d = AND v108(0xffffffffffffffffffffffffffffffffffffffff), v107
    0x11e: v11e = CALLER 
    0x11f: v11f = EQ v11e, v11d
    0x120: v120(0x128) = CONST 
    0x123: JUMPI v120(0x128), v11f

    Begin block 0x124
    prev=[0x104], succ=[]
    =================================
    0x124: v124(0x0) = CONST 
    0x127: REVERT v124(0x0), v124(0x0)

    Begin block 0x128
    prev=[0x104], succ=[0x233]
    =================================
    0x129: v129(0x0) = CONST 
    0x12c: v12c = SLOAD v129(0x0)
    0x12d: v12d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x14e: v14e = AND v12d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12c
    0x14f: v14f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x167: v167 = AND v14f(0xffffffffffffffffffffffffffffffffffffffff), v1a7V9a
    0x16b: v16b = OR v167, v14e
    0x16d: SSTORE v129(0x0), v16b
    0x16e: JUMP v9c(0x233)

    Begin block 0x233
    prev=[0x128], succ=[]
    =================================
    0x234: STOP 

}

function admin()() public {
    Begin block 0xae
    prev=[], succ=[0xb6, 0xba]
    =================================
    0xaf: vaf = CALLVALUE 
    0xb1: vb1 = ISZERO vaf
    0xb2: vb2(0xba) = CONST 
    0xb5: JUMPI vb2(0xba), vb1

    Begin block 0xb6
    prev=[0xae], succ=[]
    =================================
    0xb6: vb6(0x0) = CONST 
    0xb9: REVERT vb6(0x0), vb6(0x0)

    Begin block 0xba
    prev=[0xae], succ=[0x650xae]
    =================================
    0xbc: vbc(0x1) = CONST 
    0xbe: vbe = SLOAD vbc(0x1)
    0xbf: vbf(0x65) = CONST 
    0xc3: vc3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd8: vd8 = AND vc3(0xffffffffffffffffffffffffffffffffffffffff), vbe
    0xda: JUMP vbf(0x65)

    Begin block 0x650xae
    prev=[0xba], succ=[]
    =================================
    0x660xae: vae66(0x40) = CONST 
    0x680xae: vae68 = MLOAD vae66(0x40)
    0x690xae: vae69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x800xae: vae80 = AND vd8, vae69(0xffffffffffffffffffffffffffffffffffffffff)
    0x820xae: MSTORE vae68, vae80
    0x830xae: vae83(0x20) = CONST 
    0x850xae: vae85 = ADD vae83(0x20), vae68
    0x860xae: vae86(0x40) = CONST 
    0x880xae: vae88 = MLOAD vae86(0x40)
    0x8b0xae: vae8b(0x20) = SUB vae85, vae88
    0x8d0xae: RETURN vae88, vae8b(0x20)

}

