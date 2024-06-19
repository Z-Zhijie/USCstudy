function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x4e]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x4e) = CONST 
    0xc: JUMPI v9(0x4e), v8

    Begin block 0xd
    prev=[0x0], succ=[0x5c5, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5c60da1b) = CONST 
    0x19: v19 = EQ v14(0x5c60da1b), v12
    0x5b8: v5b8(0x5c5) = CONST 
    0x5b9: JUMPI v5b8(0x5c5), v19

    Begin block 0x5c5
    prev=[0xd], succ=[]
    =================================
    0x5c6: v5c6(0x65) = CONST 
    0x5c7: CALLPRIVATE v5c6(0x65)

    Begin block 0x1e
    prev=[0xd], succ=[0x5c8, 0x29]
    =================================
    0x1f: v1f(0x715018a6) = CONST 
    0x24: v24 = EQ v1f(0x715018a6), v12
    0x5ba: v5ba(0x5c8) = CONST 
    0x5bb: JUMPI v5ba(0x5c8), v24

    Begin block 0x5c8
    prev=[0x1e], succ=[]
    =================================
    0x5c9: v5c9(0x96) = CONST 
    0x5ca: CALLPRIVATE v5c9(0x96)

    Begin block 0x29
    prev=[0x1e], succ=[0x5cb, 0x34]
    =================================
    0x2a: v2a(0x8da5cb5b) = CONST 
    0x2f: v2f = EQ v2a(0x8da5cb5b), v12
    0x5bc: v5bc(0x5cb) = CONST 
    0x5bd: JUMPI v5bc(0x5cb), v2f

    Begin block 0x5cb
    prev=[0x29], succ=[]
    =================================
    0x5cc: v5cc(0xab) = CONST 
    0x5cd: CALLPRIVATE v5cc(0xab)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x5ce]
    =================================
    0x35: v35(0xd69efdc5) = CONST 
    0x3a: v3a = EQ v35(0xd69efdc5), v12
    0x5be: v5be(0x5ce) = CONST 
    0x5bf: JUMPI v5be(0x5ce), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x5d1]
    =================================
    0x40: v40(0xf2fde38b) = CONST 
    0x45: v45 = EQ v40(0xf2fde38b), v12
    0x5c0: v5c0(0x5d1) = CONST 
    0x5c1: JUMPI v5c0(0x5d1), v45

    Begin block 0x4a
    prev=[0x3f], succ=[0x5d]
    =================================
    0x4a: v4a(0x5d) = CONST 
    0x4d: JUMP v4a(0x5d)

    Begin block 0x5d
    prev=[0x4a, 0x4e], succ=[0x126B0x5d]
    =================================
    0x5e: v5e(0x4dd) = CONST 
    0x61: v61(0x126) = CONST 
    0x64: JUMP v61(0x126), v5e(0x4dd)

    Begin block 0x126B0x5d
    prev=[0x5d], succ=[0x130B0x5d, 0x134B0x5d]
    =================================
    0x127S0x5d: v127V5d(0x8fc) = CONST 
    0x12aS0x5d: v12aV5d = GAS 
    0x12bS0x5d: v12bV5d = GT v12aV5d, v127V5d(0x8fc)
    0x12cS0x5d: v12cV5d(0x134) = CONST 
    0x12fS0x5d: JUMPI v12cV5d(0x134), v12bV5d

    Begin block 0x130B0x5d
    prev=[0x126B0x5d], succ=[0x164B0x5d]
    =================================
    0x130S0x5d: v130V5d(0x164) = CONST 
    0x133S0x5d: JUMP v130V5d(0x164)

    Begin block 0x164B0x5d
    prev=[0x130B0x5d], succ=[0x4dd]
    =================================
    0x165S0x5d: JUMP v5e(0x4dd)

    Begin block 0x4dd
    prev=[0x15bB0x5d, 0x164B0x5d], succ=[]
    =================================
    0x4de: STOP 

    Begin block 0x134B0x5d
    prev=[0x126B0x5d], succ=[0x15bB0x5d, 0x15fB0x5d]
    =================================
    0x135S0x5d: v135V5d(0x1) = CONST 
    0x137S0x5d: v137V5d = SLOAD v135V5d(0x1)
    0x138S0x5d: v138V5d(0x1) = CONST 
    0x13aS0x5d: v13aV5d(0x1) = CONST 
    0x13cS0x5d: v13cV5d(0xa0) = CONST 
    0x13eS0x5d: v13eV5d(0x10000000000000000000000000000000000000000) = SHL v13cV5d(0xa0), v13aV5d(0x1)
    0x13fS0x5d: v13fV5d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13eV5d(0x10000000000000000000000000000000000000000), v138V5d(0x1)
    0x140S0x5d: v140V5d = AND v13fV5d(0xffffffffffffffffffffffffffffffffffffffff), v137V5d
    0x141S0x5d: v141V5d = CALLDATASIZE 
    0x142S0x5d: v142V5d(0x0) = CONST 
    0x145S0x5d: CALLDATACOPY v142V5d(0x0), v142V5d(0x0), v141V5d
    0x146S0x5d: v146V5d(0x0) = CONST 
    0x149S0x5d: v149V5d = CALLDATASIZE 
    0x14aS0x5d: v14aV5d(0x0) = CONST 
    0x14dS0x5d: v14dV5d = GAS 
    0x14eS0x5d: v14eV5d = DELEGATECALL v14dV5d, v140V5d, v14aV5d(0x0), v149V5d, v146V5d(0x0), v146V5d(0x0)
    0x14fS0x5d: v14fV5d = RETURNDATASIZE 
    0x150S0x5d: v150V5d(0x0) = CONST 
    0x153S0x5d: RETURNDATACOPY v150V5d(0x0), v150V5d(0x0), v14fV5d
    0x156S0x5d: v156V5d = ISZERO v14eV5d
    0x157S0x5d: v157V5d(0x15f) = CONST 
    0x15aS0x5d: JUMPI v157V5d(0x15f), v156V5d

    Begin block 0x15bB0x5d
    prev=[0x134B0x5d], succ=[0x4dd]
    =================================
    0x15bS0x5d: v15bV5d = RETURNDATASIZE 
    0x15cS0x5d: v15cV5d(0x0) = CONST 
    0x15eS0x5d: RETURN v15cV5d(0x0), v15bV5d

    Begin block 0x15fB0x5d
    prev=[0x134B0x5d], succ=[]
    =================================
    0x160S0x5d: v160V5d = RETURNDATASIZE 
    0x161S0x5d: v161V5d(0x0) = CONST 
    0x163S0x5d: REVERT v161V5d(0x0), v160V5d

    Begin block 0x5d1
    prev=[0x3f], succ=[]
    =================================
    0x5d2: v5d2(0xf3) = CONST 
    0x5d3: CALLPRIVATE v5d2(0xf3)

    Begin block 0x5ce
    prev=[0x34], succ=[]
    =================================
    0x5cf: v5cf(0xc0) = CONST 
    0x5d0: CALLPRIVATE v5cf(0xc0)

    Begin block 0x4e
    prev=[0x0], succ=[0x5c2, 0x5d]
    =================================
    0x4f: v4f = CALLDATASIZE 
    0x50: v50(0x5d) = CONST 
    0x53: JUMPI v50(0x5d), v4f

    Begin block 0x5c2
    prev=[0x4e], succ=[]
    =================================
    0x5c2: v5c2(0x5c4) = CONST 
    0x5c3: CALLPRIVATE v5c2(0x5c4)

}

function fallback()() public {
    Begin block 0x5c4
    prev=[], succ=[0x126B0x5c4]
    =================================
    0x54: v54(0x4bc) = CONST 
    0x57: v57(0x126) = CONST 
    0x5a: JUMP v57(0x126), v54(0x4bc)

    Begin block 0x126B0x5c4
    prev=[0x5c4], succ=[0x130B0x5c4, 0x134B0x5c4]
    =================================
    0x127S0x5c4: v127V5c4(0x8fc) = CONST 
    0x12aS0x5c4: v12aV5c4 = GAS 
    0x12bS0x5c4: v12bV5c4 = GT v12aV5c4, v127V5c4(0x8fc)
    0x12cS0x5c4: v12cV5c4(0x134) = CONST 
    0x12fS0x5c4: JUMPI v12cV5c4(0x134), v12bV5c4

    Begin block 0x130B0x5c4
    prev=[0x126B0x5c4], succ=[0x164B0x5c4]
    =================================
    0x130S0x5c4: v130V5c4(0x164) = CONST 
    0x133S0x5c4: JUMP v130V5c4(0x164)

    Begin block 0x164B0x5c4
    prev=[0x130B0x5c4], succ=[0x4bc]
    =================================
    0x165S0x5c4: JUMP v54(0x4bc)

    Begin block 0x4bc
    prev=[0x15bB0x5c4, 0x164B0x5c4], succ=[]
    =================================
    0x4bd: STOP 

    Begin block 0x134B0x5c4
    prev=[0x126B0x5c4], succ=[0x15bB0x5c4, 0x15fB0x5c4]
    =================================
    0x135S0x5c4: v135V5c4(0x1) = CONST 
    0x137S0x5c4: v137V5c4 = SLOAD v135V5c4(0x1)
    0x138S0x5c4: v138V5c4(0x1) = CONST 
    0x13aS0x5c4: v13aV5c4(0x1) = CONST 
    0x13cS0x5c4: v13cV5c4(0xa0) = CONST 
    0x13eS0x5c4: v13eV5c4(0x10000000000000000000000000000000000000000) = SHL v13cV5c4(0xa0), v13aV5c4(0x1)
    0x13fS0x5c4: v13fV5c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13eV5c4(0x10000000000000000000000000000000000000000), v138V5c4(0x1)
    0x140S0x5c4: v140V5c4 = AND v13fV5c4(0xffffffffffffffffffffffffffffffffffffffff), v137V5c4
    0x141S0x5c4: v141V5c4 = CALLDATASIZE 
    0x142S0x5c4: v142V5c4(0x0) = CONST 
    0x145S0x5c4: CALLDATACOPY v142V5c4(0x0), v142V5c4(0x0), v141V5c4
    0x146S0x5c4: v146V5c4(0x0) = CONST 
    0x149S0x5c4: v149V5c4 = CALLDATASIZE 
    0x14aS0x5c4: v14aV5c4(0x0) = CONST 
    0x14dS0x5c4: v14dV5c4 = GAS 
    0x14eS0x5c4: v14eV5c4 = DELEGATECALL v14dV5c4, v140V5c4, v14aV5c4(0x0), v149V5c4, v146V5c4(0x0), v146V5c4(0x0)
    0x14fS0x5c4: v14fV5c4 = RETURNDATASIZE 
    0x150S0x5c4: v150V5c4(0x0) = CONST 
    0x153S0x5c4: RETURNDATACOPY v150V5c4(0x0), v150V5c4(0x0), v14fV5c4
    0x156S0x5c4: v156V5c4 = ISZERO v14eV5c4
    0x157S0x5c4: v157V5c4(0x15f) = CONST 
    0x15aS0x5c4: JUMPI v157V5c4(0x15f), v156V5c4

    Begin block 0x15bB0x5c4
    prev=[0x134B0x5c4], succ=[0x4bc]
    =================================
    0x15bS0x5c4: v15bV5c4 = RETURNDATASIZE 
    0x15cS0x5c4: v15cV5c4(0x0) = CONST 
    0x15eS0x5c4: RETURN v15cV5c4(0x0), v15bV5c4

    Begin block 0x15fB0x5c4
    prev=[0x134B0x5c4], succ=[]
    =================================
    0x160S0x5c4: v160V5c4 = RETURNDATASIZE 
    0x161S0x5c4: v161V5c4(0x0) = CONST 
    0x163S0x5c4: REVERT v161V5c4(0x0), v160V5c4

}

function implementation()() public {
    Begin block 0x65
    prev=[], succ=[0x6d, 0x71]
    =================================
    0x66: v66 = CALLVALUE 
    0x68: v68 = ISZERO v66
    0x69: v69(0x71) = CONST 
    0x6c: JUMPI v69(0x71), v68

    Begin block 0x6d
    prev=[0x65], succ=[]
    =================================
    0x6d: v6d(0x0) = CONST 
    0x70: REVERT v6d(0x0), v6d(0x0)

    Begin block 0x71
    prev=[0x65], succ=[0x166]
    =================================
    0x73: v73(0x4fe) = CONST 
    0x76: v76(0x166) = CONST 
    0x79: JUMP v76(0x166)

    Begin block 0x166
    prev=[0x71], succ=[0x4fe]
    =================================
    0x167: v167(0x1) = CONST 
    0x169: v169 = SLOAD v167(0x1)
    0x16a: v16a(0x1) = CONST 
    0x16c: v16c(0x1) = CONST 
    0x16e: v16e(0xa0) = CONST 
    0x170: v170(0x10000000000000000000000000000000000000000) = SHL v16e(0xa0), v16c(0x1)
    0x171: v171(0xffffffffffffffffffffffffffffffffffffffff) = SUB v170(0x10000000000000000000000000000000000000000), v16a(0x1)
    0x172: v172 = AND v171(0xffffffffffffffffffffffffffffffffffffffff), v169
    0x174: JUMP v73(0x4fe)

    Begin block 0x4fe
    prev=[0x166], succ=[]
    =================================
    0x4ff: v4ff(0x40) = CONST 
    0x502: v502 = MLOAD v4ff(0x40)
    0x503: v503(0x1) = CONST 
    0x505: v505(0x1) = CONST 
    0x507: v507(0xa0) = CONST 
    0x509: v509(0x10000000000000000000000000000000000000000) = SHL v507(0xa0), v505(0x1)
    0x50a: v50a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v509(0x10000000000000000000000000000000000000000), v503(0x1)
    0x50d: v50d = AND v172, v50a(0xffffffffffffffffffffffffffffffffffffffff)
    0x50f: MSTORE v502, v50d
    0x510: v510 = MLOAD v4ff(0x40)
    0x514: v514(0x0) = SUB v502, v510
    0x515: v515(0x20) = CONST 
    0x517: v517(0x20) = ADD v515(0x20), v514(0x0)
    0x519: RETURN v510, v517(0x20)

}

function renounceOwnership()() public {
    Begin block 0x96
    prev=[], succ=[0x9e, 0xa2]
    =================================
    0x97: v97 = CALLVALUE 
    0x99: v99 = ISZERO v97
    0x9a: v9a(0xa2) = CONST 
    0x9d: JUMPI v9a(0xa2), v99

    Begin block 0x9e
    prev=[0x96], succ=[]
    =================================
    0x9e: v9e(0x0) = CONST 
    0xa1: REVERT v9e(0x0), v9e(0x0)

    Begin block 0xa2
    prev=[0x96], succ=[0x175]
    =================================
    0xa4: va4(0x539) = CONST 
    0xa7: va7(0x175) = CONST 
    0xaa: JUMP va7(0x175)

    Begin block 0x175
    prev=[0xa2], succ=[0x43dB0x175]
    =================================
    0x176: v176(0x17d) = CONST 
    0x179: v179(0x43d) = CONST 
    0x17c: JUMP v179(0x43d)

    Begin block 0x43dB0x175
    prev=[0x175], succ=[0x17d]
    =================================
    0x43eS0x175: v43eV175 = CALLER 
    0x440S0x175: JUMP v176(0x17d)

    Begin block 0x17d
    prev=[0x43dB0x175], succ=[0x233B0x17d]
    =================================
    0x17e: v17e(0x1) = CONST 
    0x180: v180(0x1) = CONST 
    0x182: v182(0xa0) = CONST 
    0x184: v184(0x10000000000000000000000000000000000000000) = SHL v182(0xa0), v180(0x1)
    0x185: v185(0xffffffffffffffffffffffffffffffffffffffff) = SUB v184(0x10000000000000000000000000000000000000000), v17e(0x1)
    0x186: v186 = AND v185(0xffffffffffffffffffffffffffffffffffffffff), v43eV175
    0x187: v187(0x18e) = CONST 
    0x18a: v18a(0x233) = CONST 
    0x18d: JUMP v18a(0x233)

    Begin block 0x233B0x17d
    prev=[0x17d], succ=[0x18e]
    =================================
    0x234S0x17d: v234V17d(0x0) = CONST 
    0x236S0x17d: v236V17d = SLOAD v234V17d(0x0)
    0x237S0x17d: v237V17d(0x1) = CONST 
    0x239S0x17d: v239V17d(0x1) = CONST 
    0x23bS0x17d: v23bV17d(0xa0) = CONST 
    0x23dS0x17d: v23dV17d(0x10000000000000000000000000000000000000000) = SHL v23bV17d(0xa0), v239V17d(0x1)
    0x23eS0x17d: v23eV17d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23dV17d(0x10000000000000000000000000000000000000000), v237V17d(0x1)
    0x23fS0x17d: v23fV17d = AND v23eV17d(0xffffffffffffffffffffffffffffffffffffffff), v236V17d
    0x241S0x17d: JUMP v187(0x18e)

    Begin block 0x18e
    prev=[0x233B0x17d], succ=[0x19d, 0x1e9]
    =================================
    0x18f: v18f(0x1) = CONST 
    0x191: v191(0x1) = CONST 
    0x193: v193(0xa0) = CONST 
    0x195: v195(0x10000000000000000000000000000000000000000) = SHL v193(0xa0), v191(0x1)
    0x196: v196(0xffffffffffffffffffffffffffffffffffffffff) = SUB v195(0x10000000000000000000000000000000000000000), v18f(0x1)
    0x197: v197 = AND v196(0xffffffffffffffffffffffffffffffffffffffff), v23fV17d
    0x198: v198 = EQ v197, v186
    0x199: v199(0x1e9) = CONST 
    0x19c: JUMPI v199(0x1e9), v198

    Begin block 0x19d
    prev=[0x18e], succ=[]
    =================================
    0x19d: v19d(0x40) = CONST 
    0x1a0: v1a0 = MLOAD v19d(0x40)
    0x1a1: v1a1(0x461bcd) = CONST 
    0x1a5: v1a5(0xe5) = CONST 
    0x1a7: v1a7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1a5(0xe5), v1a1(0x461bcd)
    0x1a9: MSTORE v1a0, v1a7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1aa: v1aa(0x20) = CONST 
    0x1ac: v1ac(0x4) = CONST 
    0x1af: v1af = ADD v1a0, v1ac(0x4)
    0x1b2: MSTORE v1af, v1aa(0x20)
    0x1b3: v1b3(0x24) = CONST 
    0x1b6: v1b6 = ADD v1a0, v1b3(0x24)
    0x1b7: MSTORE v1b6, v1aa(0x20)
    0x1b8: v1b8(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x1d9: v1d9(0x44) = CONST 
    0x1dc: v1dc = ADD v1a0, v1d9(0x44)
    0x1dd: MSTORE v1dc, v1b8(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1df: v1df = MLOAD v19d(0x40)
    0x1e3: v1e3(0x0) = SUB v1a0, v1df
    0x1e4: v1e4(0x64) = CONST 
    0x1e6: v1e6(0x64) = ADD v1e4(0x64), v1e3(0x0)
    0x1e8: REVERT v1df, v1e6(0x64)

    Begin block 0x1e9
    prev=[0x18e], succ=[0x539]
    =================================
    0x1ea: v1ea(0x0) = CONST 
    0x1ed: v1ed = SLOAD v1ea(0x0)
    0x1ee: v1ee(0x40) = CONST 
    0x1f0: v1f0 = MLOAD v1ee(0x40)
    0x1f1: v1f1(0x1) = CONST 
    0x1f3: v1f3(0x1) = CONST 
    0x1f5: v1f5(0xa0) = CONST 
    0x1f7: v1f7(0x10000000000000000000000000000000000000000) = SHL v1f5(0xa0), v1f3(0x1)
    0x1f8: v1f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f7(0x10000000000000000000000000000000000000000), v1f1(0x1)
    0x1fb: v1fb = AND v1ed, v1f8(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fd: v1fd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x221: LOG3 v1f0, v1ea(0x0), v1fd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1fb, v1ea(0x0)
    0x222: v222(0x0) = CONST 
    0x225: v225 = SLOAD v222(0x0)
    0x226: v226(0x1) = CONST 
    0x228: v228(0x1) = CONST 
    0x22a: v22a(0xa0) = CONST 
    0x22c: v22c(0x10000000000000000000000000000000000000000) = SHL v22a(0xa0), v228(0x1)
    0x22d: v22d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22c(0x10000000000000000000000000000000000000000), v226(0x1)
    0x22e: v22e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v22d(0xffffffffffffffffffffffffffffffffffffffff)
    0x22f: v22f = AND v22e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v225
    0x231: SSTORE v222(0x0), v22f
    0x232: JUMP va4(0x539)

    Begin block 0x539
    prev=[0x1e9], succ=[]
    =================================
    0x53a: STOP 

}

function owner()() public {
    Begin block 0xab
    prev=[], succ=[0xb3, 0xb7]
    =================================
    0xac: vac = CALLVALUE 
    0xae: vae = ISZERO vac
    0xaf: vaf(0xb7) = CONST 
    0xb2: JUMPI vaf(0xb7), vae

    Begin block 0xb3
    prev=[0xab], succ=[]
    =================================
    0xb3: vb3(0x0) = CONST 
    0xb6: REVERT vb3(0x0), vb3(0x0)

    Begin block 0xb7
    prev=[0xab], succ=[0x233B0xb7]
    =================================
    0xb9: vb9(0x55a) = CONST 
    0xbc: vbc(0x233) = CONST 
    0xbf: JUMP vbc(0x233)

    Begin block 0x233B0xb7
    prev=[0xb7], succ=[0x55a]
    =================================
    0x234S0xb7: v234Vb7(0x0) = CONST 
    0x236S0xb7: v236Vb7 = SLOAD v234Vb7(0x0)
    0x237S0xb7: v237Vb7(0x1) = CONST 
    0x239S0xb7: v239Vb7(0x1) = CONST 
    0x23bS0xb7: v23bVb7(0xa0) = CONST 
    0x23dS0xb7: v23dVb7(0x10000000000000000000000000000000000000000) = SHL v23bVb7(0xa0), v239Vb7(0x1)
    0x23eS0xb7: v23eVb7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23dVb7(0x10000000000000000000000000000000000000000), v237Vb7(0x1)
    0x23fS0xb7: v23fVb7 = AND v23eVb7(0xffffffffffffffffffffffffffffffffffffffff), v236Vb7
    0x241S0xb7: JUMP vb9(0x55a)

    Begin block 0x55a
    prev=[0x233B0xb7], succ=[]
    =================================
    0x55b: v55b(0x40) = CONST 
    0x55e: v55e = MLOAD v55b(0x40)
    0x55f: v55f(0x1) = CONST 
    0x561: v561(0x1) = CONST 
    0x563: v563(0xa0) = CONST 
    0x565: v565(0x10000000000000000000000000000000000000000) = SHL v563(0xa0), v561(0x1)
    0x566: v566(0xffffffffffffffffffffffffffffffffffffffff) = SUB v565(0x10000000000000000000000000000000000000000), v55f(0x1)
    0x569: v569 = AND v23fVb7, v566(0xffffffffffffffffffffffffffffffffffffffff)
    0x56b: MSTORE v55e, v569
    0x56c: v56c = MLOAD v55b(0x40)
    0x570: v570(0x0) = SUB v55e, v56c
    0x571: v571(0x20) = CONST 
    0x573: v573(0x20) = ADD v571(0x20), v570(0x0)
    0x575: RETURN v56c, v573(0x20)

}

function replaceImplementation(address)() public {
    Begin block 0xc0
    prev=[], succ=[0xc8, 0xcc]
    =================================
    0xc1: vc1 = CALLVALUE 
    0xc3: vc3 = ISZERO vc1
    0xc4: vc4(0xcc) = CONST 
    0xc7: JUMPI vc4(0xcc), vc3

    Begin block 0xc8
    prev=[0xc0], succ=[]
    =================================
    0xc8: vc8(0x0) = CONST 
    0xcb: REVERT vc8(0x0), vc8(0x0)

    Begin block 0xcc
    prev=[0xc0], succ=[0xdf, 0xe3]
    =================================
    0xce: vce(0x595) = CONST 
    0xd1: vd1(0x4) = CONST 
    0xd4: vd4 = CALLDATASIZE 
    0xd5: vd5 = SUB vd4, vd1(0x4)
    0xd6: vd6(0x20) = CONST 
    0xd9: vd9 = LT vd5, vd6(0x20)
    0xda: vda = ISZERO vd9
    0xdb: vdb(0xe3) = CONST 
    0xde: JUMPI vdb(0xe3), vda

    Begin block 0xdf
    prev=[0xcc], succ=[]
    =================================
    0xdf: vdf(0x0) = CONST 
    0xe2: REVERT vdf(0x0), vdf(0x0)

    Begin block 0xe3
    prev=[0xcc], succ=[0x242]
    =================================
    0xe5: ve5 = CALLDATALOAD vd1(0x4)
    0xe6: ve6(0x1) = CONST 
    0xe8: ve8(0x1) = CONST 
    0xea: vea(0xa0) = CONST 
    0xec: vec(0x10000000000000000000000000000000000000000) = SHL vea(0xa0), ve8(0x1)
    0xed: ved(0xffffffffffffffffffffffffffffffffffffffff) = SUB vec(0x10000000000000000000000000000000000000000), ve6(0x1)
    0xee: vee = AND ved(0xffffffffffffffffffffffffffffffffffffffff), ve5
    0xef: vef(0x242) = CONST 
    0xf2: JUMP vef(0x242)

    Begin block 0x242
    prev=[0xe3], succ=[0x43dB0x242]
    =================================
    0x243: v243(0x24a) = CONST 
    0x246: v246(0x43d) = CONST 
    0x249: JUMP v246(0x43d)

    Begin block 0x43dB0x242
    prev=[0x242], succ=[0x24a]
    =================================
    0x43eS0x242: v43eV242 = CALLER 
    0x440S0x242: JUMP v243(0x24a)

    Begin block 0x24a
    prev=[0x43dB0x242], succ=[0x233B0x24a]
    =================================
    0x24b: v24b(0x1) = CONST 
    0x24d: v24d(0x1) = CONST 
    0x24f: v24f(0xa0) = CONST 
    0x251: v251(0x10000000000000000000000000000000000000000) = SHL v24f(0xa0), v24d(0x1)
    0x252: v252(0xffffffffffffffffffffffffffffffffffffffff) = SUB v251(0x10000000000000000000000000000000000000000), v24b(0x1)
    0x253: v253 = AND v252(0xffffffffffffffffffffffffffffffffffffffff), v43eV242
    0x254: v254(0x25b) = CONST 
    0x257: v257(0x233) = CONST 
    0x25a: JUMP v257(0x233)

    Begin block 0x233B0x24a
    prev=[0x24a], succ=[0x25b]
    =================================
    0x234S0x24a: v234V24a(0x0) = CONST 
    0x236S0x24a: v236V24a = SLOAD v234V24a(0x0)
    0x237S0x24a: v237V24a(0x1) = CONST 
    0x239S0x24a: v239V24a(0x1) = CONST 
    0x23bS0x24a: v23bV24a(0xa0) = CONST 
    0x23dS0x24a: v23dV24a(0x10000000000000000000000000000000000000000) = SHL v23bV24a(0xa0), v239V24a(0x1)
    0x23eS0x24a: v23eV24a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23dV24a(0x10000000000000000000000000000000000000000), v237V24a(0x1)
    0x23fS0x24a: v23fV24a = AND v23eV24a(0xffffffffffffffffffffffffffffffffffffffff), v236V24a
    0x241S0x24a: JUMP v254(0x25b)

    Begin block 0x25b
    prev=[0x233B0x24a], succ=[0x26a, 0x2b6]
    =================================
    0x25c: v25c(0x1) = CONST 
    0x25e: v25e(0x1) = CONST 
    0x260: v260(0xa0) = CONST 
    0x262: v262(0x10000000000000000000000000000000000000000) = SHL v260(0xa0), v25e(0x1)
    0x263: v263(0xffffffffffffffffffffffffffffffffffffffff) = SUB v262(0x10000000000000000000000000000000000000000), v25c(0x1)
    0x264: v264 = AND v263(0xffffffffffffffffffffffffffffffffffffffff), v23fV24a
    0x265: v265 = EQ v264, v253
    0x266: v266(0x2b6) = CONST 
    0x269: JUMPI v266(0x2b6), v265

    Begin block 0x26a
    prev=[0x25b], succ=[]
    =================================
    0x26a: v26a(0x40) = CONST 
    0x26d: v26d = MLOAD v26a(0x40)
    0x26e: v26e(0x461bcd) = CONST 
    0x272: v272(0xe5) = CONST 
    0x274: v274(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v272(0xe5), v26e(0x461bcd)
    0x276: MSTORE v26d, v274(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x277: v277(0x20) = CONST 
    0x279: v279(0x4) = CONST 
    0x27c: v27c = ADD v26d, v279(0x4)
    0x27f: MSTORE v27c, v277(0x20)
    0x280: v280(0x24) = CONST 
    0x283: v283 = ADD v26d, v280(0x24)
    0x284: MSTORE v283, v277(0x20)
    0x285: v285(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x2a6: v2a6(0x44) = CONST 
    0x2a9: v2a9 = ADD v26d, v2a6(0x44)
    0x2aa: MSTORE v2a9, v285(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x2ac: v2ac = MLOAD v26a(0x40)
    0x2b0: v2b0(0x0) = SUB v26d, v2ac
    0x2b1: v2b1(0x64) = CONST 
    0x2b3: v2b3(0x64) = ADD v2b1(0x64), v2b0(0x0)
    0x2b5: REVERT v2ac, v2b3(0x64)

    Begin block 0x2b6
    prev=[0x25b], succ=[0x437]
    =================================
    0x2b7: v2b7(0x2bf) = CONST 
    0x2bb: v2bb(0x437) = CONST 
    0x2be: JUMP v2bb(0x437)

    Begin block 0x437
    prev=[0x2b6], succ=[0x2bf]
    =================================
    0x438: v438 = EXTCODESIZE vee
    0x439: v439 = ISZERO v438
    0x43a: v43a = ISZERO v439
    0x43c: JUMP v2b7(0x2bf)

    Begin block 0x2bf
    prev=[0x437], succ=[0x2c4, 0x301]
    =================================
    0x2c0: v2c0(0x301) = CONST 
    0x2c3: JUMPI v2c0(0x301), v43a

    Begin block 0x2c4
    prev=[0x2bf], succ=[]
    =================================
    0x2c4: v2c4(0x40) = CONST 
    0x2c7: v2c7 = MLOAD v2c4(0x40)
    0x2c8: v2c8(0x461bcd) = CONST 
    0x2cc: v2cc(0xe5) = CONST 
    0x2ce: v2ce(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2cc(0xe5), v2c8(0x461bcd)
    0x2d0: MSTORE v2c7, v2ce(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2d1: v2d1(0x20) = CONST 
    0x2d3: v2d3(0x4) = CONST 
    0x2d6: v2d6 = ADD v2c7, v2d3(0x4)
    0x2d7: MSTORE v2d6, v2d1(0x20)
    0x2d8: v2d8(0xe) = CONST 
    0x2da: v2da(0x24) = CONST 
    0x2dd: v2dd = ADD v2c7, v2da(0x24)
    0x2de: MSTORE v2dd, v2d8(0xe)
    0x2df: v2df(0x1b9bdd08184818dbdb9d1c9858dd) = CONST 
    0x2ee: v2ee(0x92) = CONST 
    0x2f0: v2f0(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000) = SHL v2ee(0x92), v2df(0x1b9bdd08184818dbdb9d1c9858dd)
    0x2f1: v2f1(0x44) = CONST 
    0x2f4: v2f4 = ADD v2c7, v2f1(0x44)
    0x2f5: MSTORE v2f4, v2f0(0x6e6f74206120636f6e7472616374000000000000000000000000000000000000)
    0x2f7: v2f7 = MLOAD v2c4(0x40)
    0x2fb: v2fb(0x0) = SUB v2c7, v2f7
    0x2fc: v2fc(0x64) = CONST 
    0x2fe: v2fe(0x64) = ADD v2fc(0x64), v2fb(0x0)
    0x300: REVERT v2f7, v2fe(0x64)

    Begin block 0x301
    prev=[0x2bf], succ=[0x595]
    =================================
    0x302: v302(0x1) = CONST 
    0x305: v305 = SLOAD v302(0x1)
    0x306: v306(0x1) = CONST 
    0x308: v308(0x1) = CONST 
    0x30a: v30a(0xa0) = CONST 
    0x30c: v30c(0x10000000000000000000000000000000000000000) = SHL v30a(0xa0), v308(0x1)
    0x30d: v30d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30c(0x10000000000000000000000000000000000000000), v306(0x1)
    0x30e: v30e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v30d(0xffffffffffffffffffffffffffffffffffffffff)
    0x30f: v30f = AND v30e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v305
    0x310: v310(0x1) = CONST 
    0x312: v312(0x1) = CONST 
    0x314: v314(0xa0) = CONST 
    0x316: v316(0x10000000000000000000000000000000000000000) = SHL v314(0xa0), v312(0x1)
    0x317: v317(0xffffffffffffffffffffffffffffffffffffffff) = SUB v316(0x10000000000000000000000000000000000000000), v310(0x1)
    0x31b: v31b = AND v317(0xffffffffffffffffffffffffffffffffffffffff), vee
    0x31f: v31f = OR v31b, v30f
    0x321: SSTORE v302(0x1), v31f
    0x322: JUMP vce(0x595)

    Begin block 0x595
    prev=[0x301], succ=[]
    =================================
    0x596: STOP 

}

function transferOwnership(address)() public {
    Begin block 0xf3
    prev=[], succ=[0xfb, 0xff]
    =================================
    0xf4: vf4 = CALLVALUE 
    0xf6: vf6 = ISZERO vf4
    0xf7: vf7(0xff) = CONST 
    0xfa: JUMPI vf7(0xff), vf6

    Begin block 0xfb
    prev=[0xf3], succ=[]
    =================================
    0xfb: vfb(0x0) = CONST 
    0xfe: REVERT vfb(0x0), vfb(0x0)

    Begin block 0xff
    prev=[0xf3], succ=[0x112, 0x116]
    =================================
    0x101: v101(0x5b6) = CONST 
    0x104: v104(0x4) = CONST 
    0x107: v107 = CALLDATASIZE 
    0x108: v108 = SUB v107, v104(0x4)
    0x109: v109(0x20) = CONST 
    0x10c: v10c = LT v108, v109(0x20)
    0x10d: v10d = ISZERO v10c
    0x10e: v10e(0x116) = CONST 
    0x111: JUMPI v10e(0x116), v10d

    Begin block 0x112
    prev=[0xff], succ=[]
    =================================
    0x112: v112(0x0) = CONST 
    0x115: REVERT v112(0x0), v112(0x0)

    Begin block 0x116
    prev=[0xff], succ=[0x323]
    =================================
    0x118: v118 = CALLDATALOAD v104(0x4)
    0x119: v119(0x1) = CONST 
    0x11b: v11b(0x1) = CONST 
    0x11d: v11d(0xa0) = CONST 
    0x11f: v11f(0x10000000000000000000000000000000000000000) = SHL v11d(0xa0), v11b(0x1)
    0x120: v120(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11f(0x10000000000000000000000000000000000000000), v119(0x1)
    0x121: v121 = AND v120(0xffffffffffffffffffffffffffffffffffffffff), v118
    0x122: v122(0x323) = CONST 
    0x125: JUMP v122(0x323)

    Begin block 0x323
    prev=[0x116], succ=[0x43dB0x323]
    =================================
    0x324: v324(0x32b) = CONST 
    0x327: v327(0x43d) = CONST 
    0x32a: JUMP v327(0x43d)

    Begin block 0x43dB0x323
    prev=[0x323], succ=[0x32b]
    =================================
    0x43eS0x323: v43eV323 = CALLER 
    0x440S0x323: JUMP v324(0x32b)

    Begin block 0x32b
    prev=[0x43dB0x323], succ=[0x233B0x32b]
    =================================
    0x32c: v32c(0x1) = CONST 
    0x32e: v32e(0x1) = CONST 
    0x330: v330(0xa0) = CONST 
    0x332: v332(0x10000000000000000000000000000000000000000) = SHL v330(0xa0), v32e(0x1)
    0x333: v333(0xffffffffffffffffffffffffffffffffffffffff) = SUB v332(0x10000000000000000000000000000000000000000), v32c(0x1)
    0x334: v334 = AND v333(0xffffffffffffffffffffffffffffffffffffffff), v43eV323
    0x335: v335(0x33c) = CONST 
    0x338: v338(0x233) = CONST 
    0x33b: JUMP v338(0x233)

    Begin block 0x233B0x32b
    prev=[0x32b], succ=[0x33c]
    =================================
    0x234S0x32b: v234V32b(0x0) = CONST 
    0x236S0x32b: v236V32b = SLOAD v234V32b(0x0)
    0x237S0x32b: v237V32b(0x1) = CONST 
    0x239S0x32b: v239V32b(0x1) = CONST 
    0x23bS0x32b: v23bV32b(0xa0) = CONST 
    0x23dS0x32b: v23dV32b(0x10000000000000000000000000000000000000000) = SHL v23bV32b(0xa0), v239V32b(0x1)
    0x23eS0x32b: v23eV32b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23dV32b(0x10000000000000000000000000000000000000000), v237V32b(0x1)
    0x23fS0x32b: v23fV32b = AND v23eV32b(0xffffffffffffffffffffffffffffffffffffffff), v236V32b
    0x241S0x32b: JUMP v335(0x33c)

    Begin block 0x33c
    prev=[0x233B0x32b], succ=[0x34b, 0x397]
    =================================
    0x33d: v33d(0x1) = CONST 
    0x33f: v33f(0x1) = CONST 
    0x341: v341(0xa0) = CONST 
    0x343: v343(0x10000000000000000000000000000000000000000) = SHL v341(0xa0), v33f(0x1)
    0x344: v344(0xffffffffffffffffffffffffffffffffffffffff) = SUB v343(0x10000000000000000000000000000000000000000), v33d(0x1)
    0x345: v345 = AND v344(0xffffffffffffffffffffffffffffffffffffffff), v23fV32b
    0x346: v346 = EQ v345, v334
    0x347: v347(0x397) = CONST 
    0x34a: JUMPI v347(0x397), v346

    Begin block 0x34b
    prev=[0x33c], succ=[]
    =================================
    0x34b: v34b(0x40) = CONST 
    0x34e: v34e = MLOAD v34b(0x40)
    0x34f: v34f(0x461bcd) = CONST 
    0x353: v353(0xe5) = CONST 
    0x355: v355(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v353(0xe5), v34f(0x461bcd)
    0x357: MSTORE v34e, v355(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x358: v358(0x20) = CONST 
    0x35a: v35a(0x4) = CONST 
    0x35d: v35d = ADD v34e, v35a(0x4)
    0x360: MSTORE v35d, v358(0x20)
    0x361: v361(0x24) = CONST 
    0x364: v364 = ADD v34e, v361(0x24)
    0x365: MSTORE v364, v358(0x20)
    0x366: v366(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x387: v387(0x44) = CONST 
    0x38a: v38a = ADD v34e, v387(0x44)
    0x38b: MSTORE v38a, v366(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x38d: v38d = MLOAD v34b(0x40)
    0x391: v391(0x0) = SUB v34e, v38d
    0x392: v392(0x64) = CONST 
    0x394: v394(0x64) = ADD v392(0x64), v391(0x0)
    0x396: REVERT v38d, v394(0x64)

    Begin block 0x397
    prev=[0x33c], succ=[0x3a6, 0x3dc]
    =================================
    0x398: v398(0x1) = CONST 
    0x39a: v39a(0x1) = CONST 
    0x39c: v39c(0xa0) = CONST 
    0x39e: v39e(0x10000000000000000000000000000000000000000) = SHL v39c(0xa0), v39a(0x1)
    0x39f: v39f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39e(0x10000000000000000000000000000000000000000), v398(0x1)
    0x3a1: v3a1 = AND v121, v39f(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a2: v3a2(0x3dc) = CONST 
    0x3a5: JUMPI v3a2(0x3dc), v3a1

    Begin block 0x3a6
    prev=[0x397], succ=[]
    =================================
    0x3a6: v3a6(0x40) = CONST 
    0x3a8: v3a8 = MLOAD v3a6(0x40)
    0x3a9: v3a9(0x461bcd) = CONST 
    0x3ad: v3ad(0xe5) = CONST 
    0x3af: v3af(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3ad(0xe5), v3a9(0x461bcd)
    0x3b1: MSTORE v3a8, v3af(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3b2: v3b2(0x4) = CONST 
    0x3b4: v3b4 = ADD v3b2(0x4), v3a8
    0x3b7: v3b7(0x20) = CONST 
    0x3b9: v3b9 = ADD v3b7(0x20), v3b4
    0x3bc: v3bc(0x20) = SUB v3b9, v3b4
    0x3be: MSTORE v3b4, v3bc(0x20)
    0x3bf: v3bf(0x26) = CONST 
    0x3c2: MSTORE v3b9, v3bf(0x26)
    0x3c3: v3c3(0x20) = CONST 
    0x3c5: v3c5 = ADD v3c3(0x20), v3b9
    0x3c7: v3c7(0x442) = CONST 
    0x3ca: v3ca(0x26) = CONST 
    0x3cd: CODECOPY v3c5, v3c7(0x442), v3ca(0x26)
    0x3ce: v3ce(0x40) = CONST 
    0x3d0: v3d0 = ADD v3ce(0x40), v3c5
    0x3d4: v3d4(0x40) = CONST 
    0x3d6: v3d6 = MLOAD v3d4(0x40)
    0x3d9: v3d9(0x84) = SUB v3d0, v3d6
    0x3db: REVERT v3d6, v3d9(0x84)

    Begin block 0x3dc
    prev=[0x397], succ=[0x5b6]
    =================================
    0x3dd: v3dd(0x0) = CONST 
    0x3e0: v3e0 = SLOAD v3dd(0x0)
    0x3e1: v3e1(0x40) = CONST 
    0x3e3: v3e3 = MLOAD v3e1(0x40)
    0x3e4: v3e4(0x1) = CONST 
    0x3e6: v3e6(0x1) = CONST 
    0x3e8: v3e8(0xa0) = CONST 
    0x3ea: v3ea(0x10000000000000000000000000000000000000000) = SHL v3e8(0xa0), v3e6(0x1)
    0x3eb: v3eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ea(0x10000000000000000000000000000000000000000), v3e4(0x1)
    0x3ee: v3ee = AND v121, v3eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f1: v3f1 = AND v3e0, v3eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f3: v3f3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x415: LOG3 v3e3, v3dd(0x0), v3f3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v3f1, v3ee
    0x416: v416(0x0) = CONST 
    0x419: v419 = SLOAD v416(0x0)
    0x41a: v41a(0x1) = CONST 
    0x41c: v41c(0x1) = CONST 
    0x41e: v41e(0xa0) = CONST 
    0x420: v420(0x10000000000000000000000000000000000000000) = SHL v41e(0xa0), v41c(0x1)
    0x421: v421(0xffffffffffffffffffffffffffffffffffffffff) = SUB v420(0x10000000000000000000000000000000000000000), v41a(0x1)
    0x422: v422(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v421(0xffffffffffffffffffffffffffffffffffffffff)
    0x423: v423 = AND v422(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v419
    0x424: v424(0x1) = CONST 
    0x426: v426(0x1) = CONST 
    0x428: v428(0xa0) = CONST 
    0x42a: v42a(0x10000000000000000000000000000000000000000) = SHL v428(0xa0), v426(0x1)
    0x42b: v42b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v42a(0x10000000000000000000000000000000000000000), v424(0x1)
    0x42f: v42f = AND v42b(0xffffffffffffffffffffffffffffffffffffffff), v121
    0x433: v433 = OR v42f, v423
    0x435: SSTORE v416(0x0), v433
    0x436: JUMP v101(0x5b6)

    Begin block 0x5b6
    prev=[0x3dc], succ=[]
    =================================
    0x5b7: STOP 

}

