function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x8a) = CONST 
    0xc: JUMPI v9(0x8a), v8

    Begin block 0xd
    prev=[0x0], succ=[0x59, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x715018a6) = CONST 
    0x19: v19 = GT v14(0x715018a6), v12
    0x1a: v1a(0x59) = CONST 
    0x1d: JUMPI v1a(0x59), v19

    Begin block 0x59
    prev=[0xd], succ=[0xc06, 0x65]
    =================================
    0x5b: v5b(0x933c1ed) = CONST 
    0x60: v60 = EQ v5b(0x933c1ed), v12
    0xbfb: vbfb(0xc06) = CONST 
    0xbfc: JUMPI vbfb(0xc06), v60

    Begin block 0xc06
    prev=[0x59], succ=[]
    =================================
    0xc07: vc07(0x114) = CONST 
    0xc08: CALLPRIVATE vc07(0x114)

    Begin block 0x65
    prev=[0x59], succ=[0xc09, 0x70]
    =================================
    0x66: v66(0x3a74a767) = CONST 
    0x6b: v6b = EQ v66(0x3a74a767), v12
    0xbfd: vbfd(0xc09) = CONST 
    0xbfe: JUMPI vbfd(0xc09), v6b

    Begin block 0xc09
    prev=[0x65], succ=[]
    =================================
    0xc0a: vc0a(0x23c) = CONST 
    0xc0b: CALLPRIVATE vc0a(0x23c)

    Begin block 0x70
    prev=[0x65], succ=[0xc0c, 0x7b]
    =================================
    0x71: v71(0x4487152f) = CONST 
    0x76: v76 = EQ v71(0x4487152f), v12
    0xbff: vbff(0xc0c) = CONST 
    0xc00: JUMPI vbff(0xc0c), v76

    Begin block 0xc0c
    prev=[0x70], succ=[]
    =================================
    0xc0d: vc0d(0x271) = CONST 
    0xc0e: CALLPRIVATE vc0d(0x271)

    Begin block 0x7b
    prev=[0x70], succ=[0x86, 0xc0f]
    =================================
    0x7c: v7c(0x5c60da1b) = CONST 
    0x81: v81 = EQ v7c(0x5c60da1b), v12
    0xc01: vc01(0xc0f) = CONST 
    0xc02: JUMPI vc01(0xc0f), v81

    Begin block 0x86
    prev=[0x7b], succ=[0x91]
    =================================
    0x86: v86(0x91) = CONST 
    0x89: JUMP v86(0x91)

    Begin block 0x91
    prev=[0x55, 0x86, 0x8a], succ=[0xd3, 0xf4]
    =================================
    0x92: v92(0x2) = CONST 
    0x94: v94 = SLOAD v92(0x2)
    0x95: v95(0x40) = CONST 
    0x97: v97 = MLOAD v95(0x40)
    0x98: v98(0x0) = CONST 
    0x9b: v9b(0x1) = CONST 
    0x9d: v9d(0x1) = CONST 
    0x9f: v9f(0xa0) = CONST 
    0xa1: va1(0x10000000000000000000000000000000000000000) = SHL v9f(0xa0), v9d(0x1)
    0xa2: va2(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1(0x10000000000000000000000000000000000000000), v9b(0x1)
    0xa3: va3 = AND va2(0xffffffffffffffffffffffffffffffffffffffff), v94
    0xa7: va7 = CALLDATASIZE 
    0xaf: CALLDATACOPY v97, v98(0x0), va7
    0xb0: vb0(0x40) = CONST 
    0xb2: vb2 = MLOAD vb0(0x40)
    0xb4: vb4 = ADD v97, va7
    0xb7: vb7(0x0) = CONST 
    0xc1: vc1 = SUB vb4, vb2
    0xc4: vc4 = GAS 
    0xc5: vc5 = DELEGATECALL vc4, va3, vb2, vc1, vb2, vb7(0x0)
    0xc9: vc9 = RETURNDATASIZE 
    0xcb: vcb(0x0) = CONST 
    0xce: vce = EQ vc9, vcb(0x0)
    0xcf: vcf(0xf4) = CONST 
    0xd2: JUMPI vcf(0xf4), vce

    Begin block 0xd3
    prev=[0x91], succ=[0xf9]
    =================================
    0xd3: vd3(0x40) = CONST 
    0xd5: vd5 = MLOAD vd3(0x40)
    0xd8: vd8(0x1f) = CONST 
    0xda: vda(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vd8(0x1f)
    0xdb: vdb(0x3f) = CONST 
    0xdd: vdd = RETURNDATASIZE 
    0xde: vde = ADD vdd, vdb(0x3f)
    0xdf: vdf = AND vde, vda(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xe1: ve1 = ADD vd5, vdf
    0xe2: ve2(0x40) = CONST 
    0xe4: MSTORE ve2(0x40), ve1
    0xe5: ve5 = RETURNDATASIZE 
    0xe7: MSTORE vd5, ve5
    0xe8: ve8 = RETURNDATASIZE 
    0xe9: ve9(0x0) = CONST 
    0xeb: veb(0x20) = CONST 
    0xee: vee = ADD vd5, veb(0x20)
    0xef: RETURNDATACOPY vee, ve9(0x0), ve8
    0xf0: vf0(0xf9) = CONST 
    0xf3: JUMP vf0(0xf9)

    Begin block 0xf9
    prev=[0xd3, 0xf4], succ=[0x10d, 0x110]
    =================================
    0xfe: vfe(0x40) = CONST 
    0x100: v100 = MLOAD vfe(0x40)
    0x101: v101 = RETURNDATASIZE 
    0x102: v102(0x0) = CONST 
    0x105: RETURNDATACOPY v100, v102(0x0), v101
    0x108: v108 = ISZERO vc5
    0x109: v109(0x110) = CONST 
    0x10c: JUMPI v109(0x110), v108

    Begin block 0x10d
    prev=[0xf9], succ=[]
    =================================
    0x10d: v10d = RETURNDATASIZE 
    0x10f: RETURN v100, v10d

    Begin block 0x110
    prev=[0xf9], succ=[]
    =================================
    0x111: v111 = RETURNDATASIZE 
    0x113: REVERT v100, v111

    Begin block 0xf4
    prev=[0x91], succ=[0xf9]
    =================================
    0xf5: vf5(0x60) = CONST 

    Begin block 0xc0f
    prev=[0x7b], succ=[]
    =================================
    0xc10: vc10(0x324) = CONST 
    0xc11: CALLPRIVATE vc10(0x324)

    Begin block 0x1e
    prev=[0xd], succ=[0xc12, 0x29]
    =================================
    0x1f: v1f(0x715018a6) = CONST 
    0x24: v24 = EQ v1f(0x715018a6), v12
    0xbf1: vbf1(0xc12) = CONST 
    0xbf2: JUMPI vbf1(0xc12), v24

    Begin block 0xc12
    prev=[0x1e], succ=[]
    =================================
    0xc13: vc13(0x355) = CONST 
    0xc14: CALLPRIVATE vc13(0x355)

    Begin block 0x29
    prev=[0x1e], succ=[0xc15, 0x34]
    =================================
    0x2a: v2a(0x8da5cb5b) = CONST 
    0x2f: v2f = EQ v2a(0x8da5cb5b), v12
    0xbf3: vbf3(0xc15) = CONST 
    0xbf4: JUMPI vbf3(0xc15), v2f

    Begin block 0xc15
    prev=[0x29], succ=[]
    =================================
    0xc16: vc16(0x36a) = CONST 
    0xc17: CALLPRIVATE vc16(0x36a)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xc18]
    =================================
    0x35: v35(0xbb913f41) = CONST 
    0x3a: v3a = EQ v35(0xbb913f41), v12
    0xbf5: vbf5(0xc18) = CONST 
    0xbf6: JUMPI vbf5(0xc18), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xc1b, 0x4a]
    =================================
    0x40: v40(0xf2fde38b) = CONST 
    0x45: v45 = EQ v40(0xf2fde38b), v12
    0xbf7: vbf7(0xc1b) = CONST 
    0xbf8: JUMPI vbf7(0xc1b), v45

    Begin block 0xc1b
    prev=[0x3f], succ=[]
    =================================
    0xc1c: vc1c(0x3b2) = CONST 
    0xc1d: CALLPRIVATE vc1c(0x3b2)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0xc1e]
    =================================
    0x4b: v4b(0xf851a440) = CONST 
    0x50: v50 = EQ v4b(0xf851a440), v12
    0xbf9: vbf9(0xc1e) = CONST 
    0xbfa: JUMPI vbf9(0xc1e), v50

    Begin block 0x55
    prev=[0x4a], succ=[0x91]
    =================================
    0x55: v55(0x91) = CONST 
    0x58: JUMP v55(0x91)

    Begin block 0xc1e
    prev=[0x4a], succ=[]
    =================================
    0xc1f: vc1f(0x3e5) = CONST 
    0xc20: CALLPRIVATE vc1f(0x3e5)

    Begin block 0xc18
    prev=[0x34], succ=[]
    =================================
    0xc19: vc19(0x37f) = CONST 
    0xc1a: CALLPRIVATE vc19(0x37f)

    Begin block 0x8a
    prev=[0x0], succ=[0xc03, 0x91]
    =================================
    0x8b: v8b = CALLDATASIZE 
    0x8c: v8c(0x91) = CONST 
    0x8f: JUMPI v8c(0x91), v8b

    Begin block 0xc03
    prev=[0x8a], succ=[]
    =================================
    0xc03: vc03(0xc05) = CONST 
    0xc04: CALLPRIVATE vc03(0xc05)

}

function delegateToImplementation(bytes)() public {
    Begin block 0x114
    prev=[], succ=[0x11c, 0x120]
    =================================
    0x115: v115 = CALLVALUE 
    0x117: v117 = ISZERO v115
    0x118: v118(0x120) = CONST 
    0x11b: JUMPI v118(0x120), v117

    Begin block 0x11c
    prev=[0x114], succ=[]
    =================================
    0x11c: v11c(0x0) = CONST 
    0x11f: REVERT v11c(0x0), v11c(0x0)

    Begin block 0x120
    prev=[0x114], succ=[0x133, 0x137]
    =================================
    0x122: v122(0x1c7) = CONST 
    0x125: v125(0x4) = CONST 
    0x128: v128 = CALLDATASIZE 
    0x129: v129 = SUB v128, v125(0x4)
    0x12a: v12a(0x20) = CONST 
    0x12d: v12d = LT v129, v12a(0x20)
    0x12e: v12e = ISZERO v12d
    0x12f: v12f(0x137) = CONST 
    0x132: JUMPI v12f(0x137), v12e

    Begin block 0x133
    prev=[0x120], succ=[]
    =================================
    0x133: v133(0x0) = CONST 
    0x136: REVERT v133(0x0), v133(0x0)

    Begin block 0x137
    prev=[0x120], succ=[0x14e, 0x152]
    =================================
    0x139: v139 = ADD v125(0x4), v129
    0x13b: v13b(0x20) = CONST 
    0x13e: v13e(0x24) = ADD v125(0x4), v13b(0x20)
    0x140: v140 = CALLDATALOAD v125(0x4)
    0x141: v141(0x100000000) = CONST 
    0x148: v148 = GT v140, v141(0x100000000)
    0x149: v149 = ISZERO v148
    0x14a: v14a(0x152) = CONST 
    0x14d: JUMPI v14a(0x152), v149

    Begin block 0x14e
    prev=[0x137], succ=[]
    =================================
    0x14e: v14e(0x0) = CONST 
    0x151: REVERT v14e(0x0), v14e(0x0)

    Begin block 0x152
    prev=[0x137], succ=[0x160, 0x164]
    =================================
    0x154: v154 = ADD v125(0x4), v140
    0x156: v156(0x20) = CONST 
    0x159: v159 = ADD v154, v156(0x20)
    0x15a: v15a = GT v159, v139
    0x15b: v15b = ISZERO v15a
    0x15c: v15c(0x164) = CONST 
    0x15f: JUMPI v15c(0x164), v15b

    Begin block 0x160
    prev=[0x152], succ=[]
    =================================
    0x160: v160(0x0) = CONST 
    0x163: REVERT v160(0x0), v160(0x0)

    Begin block 0x164
    prev=[0x152], succ=[0x182, 0x186]
    =================================
    0x166: v166 = CALLDATALOAD v154
    0x168: v168(0x20) = CONST 
    0x16a: v16a = ADD v168(0x20), v154
    0x16d: v16d(0x1) = CONST 
    0x170: v170 = MUL v166, v16d(0x1)
    0x172: v172 = ADD v16a, v170
    0x173: v173 = GT v172, v139
    0x174: v174(0x100000000) = CONST 
    0x17b: v17b = GT v166, v174(0x100000000)
    0x17c: v17c = OR v17b, v173
    0x17d: v17d = ISZERO v17c
    0x17e: v17e(0x186) = CONST 
    0x181: JUMPI v17e(0x186), v17d

    Begin block 0x182
    prev=[0x164], succ=[]
    =================================
    0x182: v182(0x0) = CONST 
    0x185: REVERT v182(0x0), v182(0x0)

    Begin block 0x186
    prev=[0x164], succ=[0x3fa]
    =================================
    0x18b: v18b(0x1f) = CONST 
    0x18d: v18d = ADD v18b(0x1f), v166
    0x18e: v18e(0x20) = CONST 
    0x192: v192 = DIV v18d, v18e(0x20)
    0x193: v193 = MUL v192, v18e(0x20)
    0x194: v194(0x20) = CONST 
    0x196: v196 = ADD v194(0x20), v193
    0x197: v197(0x40) = CONST 
    0x199: v199 = MLOAD v197(0x40)
    0x19c: v19c = ADD v199, v196
    0x19d: v19d(0x40) = CONST 
    0x19f: MSTORE v19d(0x40), v19c
    0x1a7: MSTORE v199, v166
    0x1a8: v1a8(0x20) = CONST 
    0x1aa: v1aa = ADD v1a8(0x20), v199
    0x1b0: CALLDATACOPY v1aa, v16a, v166
    0x1b1: v1b1(0x0) = CONST 
    0x1b4: v1b4 = ADD v1aa, v166
    0x1b8: MSTORE v1b4, v1b1(0x0)
    0x1bd: v1bd(0x3fa) = CONST 
    0x1c6: JUMP v1bd(0x3fa)

    Begin block 0x3fa
    prev=[0x186], succ=[0x99aB0x3fa]
    =================================
    0x3fb: v3fb(0x2) = CONST 
    0x3fd: v3fd = SLOAD v3fb(0x2)
    0x3fe: v3fe(0x60) = CONST 
    0x401: v401(0x413) = CONST 
    0x405: v405(0x1) = CONST 
    0x407: v407(0x1) = CONST 
    0x409: v409(0xa0) = CONST 
    0x40b: v40b(0x10000000000000000000000000000000000000000) = SHL v409(0xa0), v407(0x1)
    0x40c: v40c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v40b(0x10000000000000000000000000000000000000000), v405(0x1)
    0x40d: v40d = AND v40c(0xffffffffffffffffffffffffffffffffffffffff), v3fd
    0x40f: v40f(0x99a) = CONST 
    0x412: JUMP v40f(0x99a)

    Begin block 0x99aB0x3fa
    prev=[0x3fa], succ=[0x9bbB0x3fa]
    =================================
    0x99bS0x3fa: v99bV3fa(0x60) = CONST 
    0x99dS0x3fa: v99dV3fa(0x0) = CONST 
    0x99fS0x3fa: v99fV3fa(0x60) = CONST 
    0x9a2S0x3fa: v9a2V3fa(0x1) = CONST 
    0x9a4S0x3fa: v9a4V3fa(0x1) = CONST 
    0x9a6S0x3fa: v9a6V3fa(0xa0) = CONST 
    0x9a8S0x3fa: v9a8V3fa(0x10000000000000000000000000000000000000000) = SHL v9a6V3fa(0xa0), v9a4V3fa(0x1)
    0x9a9S0x3fa: v9a9V3fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9a8V3fa(0x10000000000000000000000000000000000000000), v9a2V3fa(0x1)
    0x9aaS0x3fa: v9aaV3fa = AND v9a9V3fa(0xffffffffffffffffffffffffffffffffffffffff), v40d
    0x9acS0x3fa: v9acV3fa(0x40) = CONST 
    0x9aeS0x3fa: v9aeV3fa = MLOAD v9acV3fa(0x40)
    0x9b2S0x3fa: v9b2V3fa = MLOAD v199
    0x9b4S0x3fa: v9b4V3fa(0x20) = CONST 
    0x9b6S0x3fa: v9b6V3fa = ADD v9b4V3fa(0x20), v199

    Begin block 0x9bbB0x3fa
    prev=[0x99aB0x3fa, 0x9c4B0x3fa], succ=[0x9daB0x3fa, 0x9c4B0x3fa]
    =================================
    0x9bb_0x2S0x3fa: v9bb_2V3fa = PHI v9b2V3fa, v9cdV3fa
    0x9bcS0x3fa: v9bcV3fa(0x20) = CONST 
    0x9bfS0x3fa: v9bfV3fa = LT v9bb_2V3fa, v9bcV3fa(0x20)
    0x9c0S0x3fa: v9c0V3fa(0x9da) = CONST 
    0x9c3S0x3fa: JUMPI v9c0V3fa(0x9da), v9bfV3fa

    Begin block 0x9daB0x3fa
    prev=[0x9bbB0x3fa], succ=[0xa19B0x3fa, 0xa3aB0x3fa]
    =================================
    0x9da_0x0S0x3fa: v9da_0V3fa = PHI v9b6V3fa, v9d5V3fa
    0x9da_0x1S0x3fa: v9da_1V3fa = PHI v9aeV3fa, v9d3V3fa
    0x9da_0x2S0x3fa: v9da_2V3fa = PHI v9b2V3fa, v9cdV3fa
    0x9dbS0x3fa: v9dbV3fa(0x1) = CONST 
    0x9deS0x3fa: v9deV3fa(0x20) = CONST 
    0x9e0S0x3fa: v9e0V3fa = SUB v9deV3fa(0x20), v9da_2V3fa
    0x9e1S0x3fa: v9e1V3fa(0x100) = CONST 
    0x9e4S0x3fa: v9e4V3fa = EXP v9e1V3fa(0x100), v9e0V3fa
    0x9e5S0x3fa: v9e5V3fa = SUB v9e4V3fa, v9dbV3fa(0x1)
    0x9e7S0x3fa: v9e7V3fa = NOT v9e5V3fa
    0x9e9S0x3fa: v9e9V3fa = MLOAD v9da_0V3fa
    0x9eaS0x3fa: v9eaV3fa = AND v9e9V3fa, v9e7V3fa
    0x9edS0x3fa: v9edV3fa = MLOAD v9da_1V3fa
    0x9eeS0x3fa: v9eeV3fa = AND v9edV3fa, v9e5V3fa
    0x9f1S0x3fa: v9f1V3fa = OR v9eaV3fa, v9eeV3fa
    0x9f3S0x3fa: MSTORE v9da_1V3fa, v9f1V3fa
    0x9fcS0x3fa: v9fcV3fa = ADD v9b2V3fa, v9aeV3fa
    0xa00S0x3fa: va00V3fa(0x0) = CONST 
    0xa02S0x3fa: va02V3fa(0x40) = CONST 
    0xa04S0x3fa: va04V3fa = MLOAD va02V3fa(0x40)
    0xa07S0x3fa: va07V3fa = SUB v9fcV3fa, va04V3fa
    0xa0aS0x3fa: va0aV3fa = GAS 
    0xa0bS0x3fa: va0bV3fa = DELEGATECALL va0aV3fa, v9aaV3fa, va04V3fa, va07V3fa, va04V3fa, va00V3fa(0x0)
    0xa0fS0x3fa: va0fV3fa = RETURNDATASIZE 
    0xa11S0x3fa: va11V3fa(0x0) = CONST 
    0xa14S0x3fa: va14V3fa = EQ va0fV3fa, va11V3fa(0x0)
    0xa15S0x3fa: va15V3fa(0xa3a) = CONST 
    0xa18S0x3fa: JUMPI va15V3fa(0xa3a), va14V3fa

    Begin block 0xa19B0x3fa
    prev=[0x9daB0x3fa], succ=[0xa3fB0x3fa]
    =================================
    0xa19S0x3fa: va19V3fa(0x40) = CONST 
    0xa1bS0x3fa: va1bV3fa = MLOAD va19V3fa(0x40)
    0xa1eS0x3fa: va1eV3fa(0x1f) = CONST 
    0xa20S0x3fa: va20V3fa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT va1eV3fa(0x1f)
    0xa21S0x3fa: va21V3fa(0x3f) = CONST 
    0xa23S0x3fa: va23V3fa = RETURNDATASIZE 
    0xa24S0x3fa: va24V3fa = ADD va23V3fa, va21V3fa(0x3f)
    0xa25S0x3fa: va25V3fa = AND va24V3fa, va20V3fa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa27S0x3fa: va27V3fa = ADD va1bV3fa, va25V3fa
    0xa28S0x3fa: va28V3fa(0x40) = CONST 
    0xa2aS0x3fa: MSTORE va28V3fa(0x40), va27V3fa
    0xa2bS0x3fa: va2bV3fa = RETURNDATASIZE 
    0xa2dS0x3fa: MSTORE va1bV3fa, va2bV3fa
    0xa2eS0x3fa: va2eV3fa = RETURNDATASIZE 
    0xa2fS0x3fa: va2fV3fa(0x0) = CONST 
    0xa31S0x3fa: va31V3fa(0x20) = CONST 
    0xa34S0x3fa: va34V3fa = ADD va1bV3fa, va31V3fa(0x20)
    0xa35S0x3fa: RETURNDATACOPY va34V3fa, va2fV3fa(0x0), va2eV3fa
    0xa36S0x3fa: va36V3fa(0xa3f) = CONST 
    0xa39S0x3fa: JUMP va36V3fa(0xa3f)

    Begin block 0xa3fB0x3fa
    prev=[0xa19B0x3fa, 0xa3aB0x3fa], succ=[0xa4eB0x3fa, 0xa54B0x3fa]
    =================================
    0xa45S0x3fa: va45V3fa(0x0) = CONST 
    0xa48S0x3fa: va48V3fa = EQ va0bV3fa, va45V3fa(0x0)
    0xa49S0x3fa: va49V3fa = ISZERO va48V3fa
    0xa4aS0x3fa: va4aV3fa(0xa54) = CONST 
    0xa4dS0x3fa: JUMPI va4aV3fa(0xa54), va49V3fa

    Begin block 0xa4eB0x3fa
    prev=[0xa3fB0x3fa], succ=[]
    =================================
    0xa4eS0x3fa: va4eV3fa = RETURNDATASIZE 
    0xa4e_0x0S0x3fa: va4e_0V3fa = PHI va1bV3fa, va3bV3fa(0x60)
    0xa4fS0x3fa: va4fV3fa(0x20) = CONST 
    0xa52S0x3fa: va52V3fa = ADD va4e_0V3fa, va4fV3fa(0x20)
    0xa53S0x3fa: REVERT va52V3fa, va4eV3fa

    Begin block 0xa54B0x3fa
    prev=[0xa3fB0x3fa], succ=[0x413]
    =================================
    0xa54_0x0S0x3fa: va54_0V3fa = PHI va1bV3fa, va3bV3fa(0x60)
    0xa5bS0x3fa: JUMP v401(0x413)

    Begin block 0x413
    prev=[0xa54B0x3fa], succ=[0x1c70x114]
    =================================
    0x418: JUMP v122(0x1c7)

    Begin block 0x1c70x114
    prev=[0x413], succ=[0x1e90x114]
    =================================
    0x1c80x114: v1141c8(0x40) = CONST 
    0x1cb0x114: v1141cb = MLOAD v1141c8(0x40)
    0x1cc0x114: v1141cc(0x20) = CONST 
    0x1d00x114: MSTORE v1141cb, v1141cc(0x20)
    0x1d20x114: v1141d2 = MLOAD va54_0V3fa
    0x1d50x114: v1141d5 = ADD v1141cb, v1141cc(0x20)
    0x1d60x114: MSTORE v1141d5, v1141d2
    0x1d80x114: v1141d8 = MLOAD va54_0V3fa
    0x1df0x114: v1141df = ADD v1141cb, v1141c8(0x40)
    0x1e20x114: v1141e2 = ADD va54_0V3fa, v1141cc(0x20)
    0x1e70x114: v1141e7(0x0) = CONST 

    Begin block 0x1e90x114
    prev=[0x1f20x114, 0x1c70x114], succ=[0x2010x114, 0x1f20x114]
    =================================
    0x1e90x114_0x0: v1e9114_0 = PHI v1141fc, v1141e7(0x0)
    0x1ec0x114: v1141ec = LT v1e9114_0, v1141d8
    0x1ed0x114: v1141ed = ISZERO v1141ec
    0x1ee0x114: v1141ee(0x201) = CONST 
    0x1f10x114: JUMPI v1141ee(0x201), v1141ed

    Begin block 0x2010x114
    prev=[0x1e90x114], succ=[0x22e0x114, 0x2150x114]
    =================================
    0x20a0x114: v11420a = ADD v1141d8, v1141df
    0x20c0x114: v11420c(0x1f) = CONST 
    0x20e0x114: v11420e = AND v11420c(0x1f), v1141d8
    0x2100x114: v114210 = ISZERO v11420e
    0x2110x114: v114211(0x22e) = CONST 
    0x2140x114: JUMPI v114211(0x22e), v114210

    Begin block 0x22e0x114
    prev=[0x2010x114, 0x2150x114], succ=[]
    =================================
    0x22e0x114_0x1: v22e114_1 = PHI v11422b, v11420a
    0x2340x114: v114234(0x40) = CONST 
    0x2360x114: v114236 = MLOAD v114234(0x40)
    0x2390x114: v114239 = SUB v22e114_1, v114236
    0x23b0x114: RETURN v114236, v114239

    Begin block 0x2150x114
    prev=[0x2010x114], succ=[0x22e0x114]
    =================================
    0x2170x114: v114217 = SUB v11420a, v11420e
    0x2190x114: v114219 = MLOAD v114217
    0x21a0x114: v11421a(0x1) = CONST 
    0x21d0x114: v11421d(0x20) = CONST 
    0x21f0x114: v11421f = SUB v11421d(0x20), v11420e
    0x2200x114: v114220(0x100) = CONST 
    0x2230x114: v114223 = EXP v114220(0x100), v11421f
    0x2240x114: v114224 = SUB v114223, v11421a(0x1)
    0x2250x114: v114225 = NOT v114224
    0x2260x114: v114226 = AND v114225, v114219
    0x2280x114: MSTORE v114217, v114226
    0x2290x114: v114229(0x20) = CONST 
    0x22b0x114: v11422b = ADD v114229(0x20), v114217

    Begin block 0x1f20x114
    prev=[0x1e90x114], succ=[0x1e90x114]
    =================================
    0x1f20x114_0x0: v1f2114_0 = PHI v1141fc, v1141e7(0x0)
    0x1f40x114: v1141f4 = ADD v1f2114_0, v1141e2
    0x1f50x114: v1141f5 = MLOAD v1141f4
    0x1f80x114: v1141f8 = ADD v1f2114_0, v1141df
    0x1f90x114: MSTORE v1141f8, v1141f5
    0x1fa0x114: v1141fa(0x20) = CONST 
    0x1fc0x114: v1141fc = ADD v1141fa(0x20), v1f2114_0
    0x1fd0x114: v1141fd(0x1e9) = CONST 
    0x2000x114: JUMP v1141fd(0x1e9)

    Begin block 0xa3aB0x3fa
    prev=[0x9daB0x3fa], succ=[0xa3fB0x3fa]
    =================================
    0xa3bS0x3fa: va3bV3fa(0x60) = CONST 

    Begin block 0x9c4B0x3fa
    prev=[0x9bbB0x3fa], succ=[0x9bbB0x3fa]
    =================================
    0x9c4_0x0S0x3fa: v9c4_0V3fa = PHI v9b6V3fa, v9d5V3fa
    0x9c4_0x1S0x3fa: v9c4_1V3fa = PHI v9aeV3fa, v9d3V3fa
    0x9c4_0x2S0x3fa: v9c4_2V3fa = PHI v9b2V3fa, v9cdV3fa
    0x9c5S0x3fa: v9c5V3fa = MLOAD v9c4_0V3fa
    0x9c7S0x3fa: MSTORE v9c4_1V3fa, v9c5V3fa
    0x9c8S0x3fa: v9c8V3fa(0x1f) = CONST 
    0x9caS0x3fa: v9caV3fa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v9c8V3fa(0x1f)
    0x9cdS0x3fa: v9cdV3fa = ADD v9c4_2V3fa, v9caV3fa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x9cfS0x3fa: v9cfV3fa(0x20) = CONST 
    0x9d3S0x3fa: v9d3V3fa = ADD v9cfV3fa(0x20), v9c4_1V3fa
    0x9d5S0x3fa: v9d5V3fa = ADD v9cfV3fa(0x20), v9c4_0V3fa
    0x9d6S0x3fa: v9d6V3fa(0x9bb) = CONST 
    0x9d9S0x3fa: JUMP v9d6V3fa(0x9bb)

}

function _setAdmin(address)() public {
    Begin block 0x23c
    prev=[], succ=[0x244, 0x248]
    =================================
    0x23d: v23d = CALLVALUE 
    0x23f: v23f = ISZERO v23d
    0x240: v240(0x248) = CONST 
    0x243: JUMPI v240(0x248), v23f

    Begin block 0x244
    prev=[0x23c], succ=[]
    =================================
    0x244: v244(0x0) = CONST 
    0x247: REVERT v244(0x0), v244(0x0)

    Begin block 0x248
    prev=[0x23c], succ=[0x25b, 0x25f]
    =================================
    0x24a: v24a(0xadb) = CONST 
    0x24d: v24d(0x4) = CONST 
    0x250: v250 = CALLDATASIZE 
    0x251: v251 = SUB v250, v24d(0x4)
    0x252: v252(0x20) = CONST 
    0x255: v255 = LT v251, v252(0x20)
    0x256: v256 = ISZERO v255
    0x257: v257(0x25f) = CONST 
    0x25a: JUMPI v257(0x25f), v256

    Begin block 0x25b
    prev=[0x248], succ=[]
    =================================
    0x25b: v25b(0x0) = CONST 
    0x25e: REVERT v25b(0x0), v25b(0x0)

    Begin block 0x25f
    prev=[0x248], succ=[0x419]
    =================================
    0x261: v261 = CALLDATALOAD v24d(0x4)
    0x262: v262(0x1) = CONST 
    0x264: v264(0x1) = CONST 
    0x266: v266(0xa0) = CONST 
    0x268: v268(0x10000000000000000000000000000000000000000) = SHL v266(0xa0), v264(0x1)
    0x269: v269(0xffffffffffffffffffffffffffffffffffffffff) = SUB v268(0x10000000000000000000000000000000000000000), v262(0x1)
    0x26a: v26a = AND v269(0xffffffffffffffffffffffffffffffffffffffff), v261
    0x26b: v26b(0x419) = CONST 
    0x26e: JUMP v26b(0x419)

    Begin block 0x419
    prev=[0x25f], succ=[0x42c, 0x467]
    =================================
    0x41a: v41a(0x1) = CONST 
    0x41c: v41c = SLOAD v41a(0x1)
    0x41d: v41d(0x1) = CONST 
    0x41f: v41f(0x1) = CONST 
    0x421: v421(0xa0) = CONST 
    0x423: v423(0x10000000000000000000000000000000000000000) = SHL v421(0xa0), v41f(0x1)
    0x424: v424(0xffffffffffffffffffffffffffffffffffffffff) = SUB v423(0x10000000000000000000000000000000000000000), v41d(0x1)
    0x425: v425 = AND v424(0xffffffffffffffffffffffffffffffffffffffff), v41c
    0x426: v426 = CALLER 
    0x427: v427 = EQ v426, v425
    0x428: v428(0x467) = CONST 
    0x42b: JUMPI v428(0x467), v427

    Begin block 0x42c
    prev=[0x419], succ=[]
    =================================
    0x42c: v42c(0x40) = CONST 
    0x42f: v42f = MLOAD v42c(0x40)
    0x430: v430(0x461bcd) = CONST 
    0x434: v434(0xe5) = CONST 
    0x436: v436(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v434(0xe5), v430(0x461bcd)
    0x438: MSTORE v42f, v436(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x439: v439(0x20) = CONST 
    0x43b: v43b(0x4) = CONST 
    0x43e: v43e = ADD v42f, v43b(0x4)
    0x43f: MSTORE v43e, v439(0x20)
    0x440: v440(0xc) = CONST 
    0x442: v442(0x24) = CONST 
    0x445: v445 = ADD v42f, v442(0x24)
    0x446: MSTORE v445, v440(0xc)
    0x447: v447(0x15539055551213d492569151) = CONST 
    0x454: v454(0xa2) = CONST 
    0x456: v456(0x554e415554484f52495a45440000000000000000000000000000000000000000) = SHL v454(0xa2), v447(0x15539055551213d492569151)
    0x457: v457(0x44) = CONST 
    0x45a: v45a = ADD v42f, v457(0x44)
    0x45b: MSTORE v45a, v456(0x554e415554484f52495a45440000000000000000000000000000000000000000)
    0x45d: v45d = MLOAD v42c(0x40)
    0x461: v461(0x0) = SUB v42f, v45d
    0x462: v462(0x64) = CONST 
    0x464: v464(0x64) = ADD v462(0x64), v461(0x0)
    0x466: REVERT v45d, v464(0x64)

    Begin block 0x467
    prev=[0x419], succ=[0xadb]
    =================================
    0x468: v468(0x1) = CONST 
    0x46b: v46b = SLOAD v468(0x1)
    0x46c: v46c(0x1) = CONST 
    0x46e: v46e(0x1) = CONST 
    0x470: v470(0xa0) = CONST 
    0x472: v472(0x10000000000000000000000000000000000000000) = SHL v470(0xa0), v46e(0x1)
    0x473: v473(0xffffffffffffffffffffffffffffffffffffffff) = SUB v472(0x10000000000000000000000000000000000000000), v46c(0x1)
    0x476: v476 = AND v473(0xffffffffffffffffffffffffffffffffffffffff), v26a
    0x477: v477(0x1) = CONST 
    0x479: v479(0x1) = CONST 
    0x47b: v47b(0xa0) = CONST 
    0x47d: v47d(0x10000000000000000000000000000000000000000) = SHL v47b(0xa0), v479(0x1)
    0x47e: v47e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v47d(0x10000000000000000000000000000000000000000), v477(0x1)
    0x47f: v47f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v47e(0xffffffffffffffffffffffffffffffffffffffff)
    0x481: v481 = AND v46b, v47f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x483: v483 = OR v476, v481
    0x486: SSTORE v468(0x1), v483
    0x487: v487(0x40) = CONST 
    0x48a: v48a = MLOAD v487(0x40)
    0x48e: v48e = AND v46b, v473(0xffffffffffffffffffffffffffffffffffffffff)
    0x491: MSTORE v48a, v48e
    0x492: v492(0x20) = CONST 
    0x495: v495 = ADD v48a, v492(0x20)
    0x499: MSTORE v495, v476
    0x49b: v49b = MLOAD v487(0x40)
    0x49c: v49c(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x4c1: v4c1(0x0) = SUB v48a, v49b
    0x4c4: v4c4(0x40) = ADD v487(0x40), v4c1(0x0)
    0x4c6: LOG1 v49b, v4c4(0x40), v49c(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x4c9: JUMP v24a(0xadb)

    Begin block 0xadb
    prev=[0x467], succ=[]
    =================================
    0xadc: STOP 

}

function delegateToViewImplementation(bytes)() public {
    Begin block 0x271
    prev=[], succ=[0x279, 0x27d]
    =================================
    0x272: v272 = CALLVALUE 
    0x274: v274 = ISZERO v272
    0x275: v275(0x27d) = CONST 
    0x278: JUMPI v275(0x27d), v274

    Begin block 0x279
    prev=[0x271], succ=[]
    =================================
    0x279: v279(0x0) = CONST 
    0x27c: REVERT v279(0x0), v279(0x0)

    Begin block 0x27d
    prev=[0x271], succ=[0x290, 0x294]
    =================================
    0x27f: v27f(0x1c7) = CONST 
    0x282: v282(0x4) = CONST 
    0x285: v285 = CALLDATASIZE 
    0x286: v286 = SUB v285, v282(0x4)
    0x287: v287(0x20) = CONST 
    0x28a: v28a = LT v286, v287(0x20)
    0x28b: v28b = ISZERO v28a
    0x28c: v28c(0x294) = CONST 
    0x28f: JUMPI v28c(0x294), v28b

    Begin block 0x290
    prev=[0x27d], succ=[]
    =================================
    0x290: v290(0x0) = CONST 
    0x293: REVERT v290(0x0), v290(0x0)

    Begin block 0x294
    prev=[0x27d], succ=[0x2ab, 0x2af]
    =================================
    0x296: v296 = ADD v282(0x4), v286
    0x298: v298(0x20) = CONST 
    0x29b: v29b(0x24) = ADD v282(0x4), v298(0x20)
    0x29d: v29d = CALLDATALOAD v282(0x4)
    0x29e: v29e(0x100000000) = CONST 
    0x2a5: v2a5 = GT v29d, v29e(0x100000000)
    0x2a6: v2a6 = ISZERO v2a5
    0x2a7: v2a7(0x2af) = CONST 
    0x2aa: JUMPI v2a7(0x2af), v2a6

    Begin block 0x2ab
    prev=[0x294], succ=[]
    =================================
    0x2ab: v2ab(0x0) = CONST 
    0x2ae: REVERT v2ab(0x0), v2ab(0x0)

    Begin block 0x2af
    prev=[0x294], succ=[0x2bd, 0x2c1]
    =================================
    0x2b1: v2b1 = ADD v282(0x4), v29d
    0x2b3: v2b3(0x20) = CONST 
    0x2b6: v2b6 = ADD v2b1, v2b3(0x20)
    0x2b7: v2b7 = GT v2b6, v296
    0x2b8: v2b8 = ISZERO v2b7
    0x2b9: v2b9(0x2c1) = CONST 
    0x2bc: JUMPI v2b9(0x2c1), v2b8

    Begin block 0x2bd
    prev=[0x2af], succ=[]
    =================================
    0x2bd: v2bd(0x0) = CONST 
    0x2c0: REVERT v2bd(0x0), v2bd(0x0)

    Begin block 0x2c1
    prev=[0x2af], succ=[0x2df, 0x2e3]
    =================================
    0x2c3: v2c3 = CALLDATALOAD v2b1
    0x2c5: v2c5(0x20) = CONST 
    0x2c7: v2c7 = ADD v2c5(0x20), v2b1
    0x2ca: v2ca(0x1) = CONST 
    0x2cd: v2cd = MUL v2c3, v2ca(0x1)
    0x2cf: v2cf = ADD v2c7, v2cd
    0x2d0: v2d0 = GT v2cf, v296
    0x2d1: v2d1(0x100000000) = CONST 
    0x2d8: v2d8 = GT v2c3, v2d1(0x100000000)
    0x2d9: v2d9 = OR v2d8, v2d0
    0x2da: v2da = ISZERO v2d9
    0x2db: v2db(0x2e3) = CONST 
    0x2de: JUMPI v2db(0x2e3), v2da

    Begin block 0x2df
    prev=[0x2c1], succ=[]
    =================================
    0x2df: v2df(0x0) = CONST 
    0x2e2: REVERT v2df(0x0), v2df(0x0)

    Begin block 0x2e3
    prev=[0x2c1], succ=[0x4ca]
    =================================
    0x2e8: v2e8(0x1f) = CONST 
    0x2ea: v2ea = ADD v2e8(0x1f), v2c3
    0x2eb: v2eb(0x20) = CONST 
    0x2ef: v2ef = DIV v2ea, v2eb(0x20)
    0x2f0: v2f0 = MUL v2ef, v2eb(0x20)
    0x2f1: v2f1(0x20) = CONST 
    0x2f3: v2f3 = ADD v2f1(0x20), v2f0
    0x2f4: v2f4(0x40) = CONST 
    0x2f6: v2f6 = MLOAD v2f4(0x40)
    0x2f9: v2f9 = ADD v2f6, v2f3
    0x2fa: v2fa(0x40) = CONST 
    0x2fc: MSTORE v2fa(0x40), v2f9
    0x304: MSTORE v2f6, v2c3
    0x305: v305(0x20) = CONST 
    0x307: v307 = ADD v305(0x20), v2f6
    0x30d: CALLDATACOPY v307, v2c7, v2c3
    0x30e: v30e(0x0) = CONST 
    0x311: v311 = ADD v307, v2c3
    0x315: MSTORE v311, v30e(0x0)
    0x31a: v31a(0x4ca) = CONST 
    0x323: JUMP v31a(0x4ca)

    Begin block 0x4ca
    prev=[0x2e3], succ=[0x503]
    =================================
    0x4cb: v4cb(0x60) = CONST 
    0x4cd: v4cd(0x0) = CONST 
    0x4cf: v4cf(0x60) = CONST 
    0x4d1: v4d1 = ADDRESS 
    0x4d2: v4d2(0x1) = CONST 
    0x4d4: v4d4(0x1) = CONST 
    0x4d6: v4d6(0xa0) = CONST 
    0x4d8: v4d8(0x10000000000000000000000000000000000000000) = SHL v4d6(0xa0), v4d4(0x1)
    0x4d9: v4d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d8(0x10000000000000000000000000000000000000000), v4d2(0x1)
    0x4da: v4da = AND v4d9(0xffffffffffffffffffffffffffffffffffffffff), v4d1
    0x4dc: v4dc(0x40) = CONST 
    0x4de: v4de = MLOAD v4dc(0x40)
    0x4df: v4df(0x24) = CONST 
    0x4e1: v4e1 = ADD v4df(0x24), v4de
    0x4e4: v4e4(0x20) = CONST 
    0x4e6: v4e6 = ADD v4e4(0x20), v4e1
    0x4e9: v4e9(0x20) = SUB v4e6, v4e1
    0x4eb: MSTORE v4e1, v4e9(0x20)
    0x4ef: v4ef = MLOAD v2f6
    0x4f1: MSTORE v4e6, v4ef
    0x4f2: v4f2(0x20) = CONST 
    0x4f4: v4f4 = ADD v4f2(0x20), v4e6
    0x4f8: v4f8 = MLOAD v2f6
    0x4fa: v4fa(0x20) = CONST 
    0x4fc: v4fc = ADD v4fa(0x20), v2f6
    0x501: v501(0x0) = CONST 

    Begin block 0x503
    prev=[0x4ca, 0x50c], succ=[0x51b, 0x50c]
    =================================
    0x503_0x0: v503_0 = PHI v501(0x0), v516
    0x506: v506 = LT v503_0, v4f8
    0x507: v507 = ISZERO v506
    0x508: v508(0x51b) = CONST 
    0x50b: JUMPI v508(0x51b), v507

    Begin block 0x51b
    prev=[0x503], succ=[0x548, 0x52f]
    =================================
    0x524: v524 = ADD v4f8, v4f4
    0x526: v526(0x1f) = CONST 
    0x528: v528 = AND v526(0x1f), v4f8
    0x52a: v52a = ISZERO v528
    0x52b: v52b(0x548) = CONST 
    0x52e: JUMPI v52b(0x548), v52a

    Begin block 0x548
    prev=[0x51b, 0x52f], succ=[0x584]
    =================================
    0x548_0x1: v548_1 = PHI v524, v545
    0x54a: v54a(0x40) = CONST 
    0x54d: v54d = MLOAD v54a(0x40)
    0x54e: v54e(0x1f) = CONST 
    0x550: v550(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v54e(0x1f)
    0x553: v553 = SUB v548_1, v54d
    0x554: v554 = ADD v553, v550(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x556: MSTORE v54d, v554
    0x559: MSTORE v54a(0x40), v548_1
    0x55a: v55a(0x20) = CONST 
    0x55d: v55d = ADD v54d, v55a(0x20)
    0x55f: v55f = MLOAD v55d
    0x560: v560(0x1) = CONST 
    0x562: v562(0x1) = CONST 
    0x564: v564(0xe0) = CONST 
    0x566: v566(0x100000000000000000000000000000000000000000000000000000000) = SHL v564(0xe0), v562(0x1)
    0x567: v567(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v566(0x100000000000000000000000000000000000000000000000000000000), v560(0x1)
    0x568: v568 = AND v567(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v55f
    0x569: v569(0x933c1ed) = CONST 
    0x56e: v56e(0xe0) = CONST 
    0x570: v570(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v56e(0xe0), v569(0x933c1ed)
    0x571: v571 = OR v570(0x933c1ed00000000000000000000000000000000000000000000000000000000), v568
    0x573: MSTORE v55d, v571
    0x575: v575 = MLOAD v54a(0x40)
    0x577: v577 = MLOAD v54d

    Begin block 0x584
    prev=[0x548, 0x58d], succ=[0x5a3, 0x58d]
    =================================
    0x584_0x2: v584_2 = PHI v577, v596
    0x585: v585(0x20) = CONST 
    0x588: v588 = LT v584_2, v585(0x20)
    0x589: v589(0x5a3) = CONST 
    0x58c: JUMPI v589(0x5a3), v588

    Begin block 0x5a3
    prev=[0x584], succ=[0x5e2, 0x603]
    =================================
    0x5a3_0x0: v5a3_0 = PHI v55d, v59e
    0x5a3_0x1: v5a3_1 = PHI v575, v59c
    0x5a3_0x2: v5a3_2 = PHI v577, v596
    0x5a4: v5a4(0x1) = CONST 
    0x5a7: v5a7(0x20) = CONST 
    0x5a9: v5a9 = SUB v5a7(0x20), v5a3_2
    0x5aa: v5aa(0x100) = CONST 
    0x5ad: v5ad = EXP v5aa(0x100), v5a9
    0x5ae: v5ae = SUB v5ad, v5a4(0x1)
    0x5b0: v5b0 = NOT v5ae
    0x5b2: v5b2 = MLOAD v5a3_0
    0x5b3: v5b3 = AND v5b2, v5b0
    0x5b6: v5b6 = MLOAD v5a3_1
    0x5b7: v5b7 = AND v5b6, v5ae
    0x5ba: v5ba = OR v5b3, v5b7
    0x5bc: MSTORE v5a3_1, v5ba
    0x5c5: v5c5 = ADD v577, v575
    0x5c9: v5c9(0x0) = CONST 
    0x5cb: v5cb(0x40) = CONST 
    0x5cd: v5cd = MLOAD v5cb(0x40)
    0x5d0: v5d0 = SUB v5c5, v5cd
    0x5d3: v5d3 = GAS 
    0x5d4: v5d4 = STATICCALL v5d3, v4da, v5cd, v5d0, v5cd, v5c9(0x0)
    0x5d8: v5d8 = RETURNDATASIZE 
    0x5da: v5da(0x0) = CONST 
    0x5dd: v5dd = EQ v5d8, v5da(0x0)
    0x5de: v5de(0x603) = CONST 
    0x5e1: JUMPI v5de(0x603), v5dd

    Begin block 0x5e2
    prev=[0x5a3], succ=[0x608]
    =================================
    0x5e2: v5e2(0x40) = CONST 
    0x5e4: v5e4 = MLOAD v5e2(0x40)
    0x5e7: v5e7(0x1f) = CONST 
    0x5e9: v5e9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v5e7(0x1f)
    0x5ea: v5ea(0x3f) = CONST 
    0x5ec: v5ec = RETURNDATASIZE 
    0x5ed: v5ed = ADD v5ec, v5ea(0x3f)
    0x5ee: v5ee = AND v5ed, v5e9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x5f0: v5f0 = ADD v5e4, v5ee
    0x5f1: v5f1(0x40) = CONST 
    0x5f3: MSTORE v5f1(0x40), v5f0
    0x5f4: v5f4 = RETURNDATASIZE 
    0x5f6: MSTORE v5e4, v5f4
    0x5f7: v5f7 = RETURNDATASIZE 
    0x5f8: v5f8(0x0) = CONST 
    0x5fa: v5fa(0x20) = CONST 
    0x5fd: v5fd = ADD v5e4, v5fa(0x20)
    0x5fe: RETURNDATACOPY v5fd, v5f8(0x0), v5f7
    0x5ff: v5ff(0x608) = CONST 
    0x602: JUMP v5ff(0x608)

    Begin block 0x608
    prev=[0x5e2, 0x603], succ=[0x617, 0x61d]
    =================================
    0x60e: v60e(0x0) = CONST 
    0x611: v611 = EQ v5d4, v60e(0x0)
    0x612: v612 = ISZERO v611
    0x613: v613(0x61d) = CONST 
    0x616: JUMPI v613(0x61d), v612

    Begin block 0x617
    prev=[0x608], succ=[]
    =================================
    0x617: v617 = RETURNDATASIZE 
    0x617_0x0: v617_0 = PHI v5e4, v604(0x60)
    0x618: v618(0x20) = CONST 
    0x61b: v61b = ADD v617_0, v618(0x20)
    0x61c: REVERT v61b, v617

    Begin block 0x61d
    prev=[0x608], succ=[0x62e, 0x632]
    =================================
    0x61d_0x0: v61d_0 = PHI v5e4, v604(0x60)
    0x620: v620(0x20) = CONST 
    0x622: v622 = ADD v620(0x20), v61d_0
    0x624: v624 = MLOAD v61d_0
    0x625: v625(0x20) = CONST 
    0x628: v628 = LT v624, v625(0x20)
    0x629: v629 = ISZERO v628
    0x62a: v62a(0x632) = CONST 
    0x62d: JUMPI v62a(0x632), v629

    Begin block 0x62e
    prev=[0x61d], succ=[]
    =================================
    0x62e: v62e(0x0) = CONST 
    0x631: REVERT v62e(0x0), v62e(0x0)

    Begin block 0x632
    prev=[0x61d], succ=[0x64e, 0x652]
    =================================
    0x634: v634 = ADD v622, v624
    0x638: v638 = MLOAD v622
    0x639: v639(0x40) = CONST 
    0x63b: v63b = MLOAD v639(0x40)
    0x641: v641(0x100000000) = CONST 
    0x648: v648 = GT v638, v641(0x100000000)
    0x649: v649 = ISZERO v648
    0x64a: v64a(0x652) = CONST 
    0x64d: JUMPI v64a(0x652), v649

    Begin block 0x64e
    prev=[0x632], succ=[]
    =================================
    0x64e: v64e(0x0) = CONST 
    0x651: REVERT v64e(0x0), v64e(0x0)

    Begin block 0x652
    prev=[0x632], succ=[0x663, 0x667]
    =================================
    0x655: v655 = ADD v622, v638
    0x657: v657(0x20) = CONST 
    0x65a: v65a = ADD v655, v657(0x20)
    0x65d: v65d = GT v65a, v634
    0x65e: v65e = ISZERO v65d
    0x65f: v65f(0x667) = CONST 
    0x662: JUMPI v65f(0x667), v65e

    Begin block 0x663
    prev=[0x652], succ=[]
    =================================
    0x663: v663(0x0) = CONST 
    0x666: REVERT v663(0x0), v663(0x0)

    Begin block 0x667
    prev=[0x652], succ=[0x67d, 0x681]
    =================================
    0x669: v669 = MLOAD v655
    0x66a: v66a(0x100000000) = CONST 
    0x671: v671 = GT v669, v66a(0x100000000)
    0x674: v674 = ADD v669, v65a
    0x676: v676 = LT v634, v674
    0x677: v677 = OR v676, v671
    0x678: v678 = ISZERO v677
    0x679: v679(0x681) = CONST 
    0x67c: JUMPI v679(0x681), v678

    Begin block 0x67d
    prev=[0x667], succ=[]
    =================================
    0x67d: v67d(0x0) = CONST 
    0x680: REVERT v67d(0x0), v67d(0x0)

    Begin block 0x681
    prev=[0x667], succ=[0x696]
    =================================
    0x683: MSTORE v63b, v669
    0x686: v686 = MLOAD v655
    0x687: v687(0x20) = CONST 
    0x68b: v68b = ADD v687(0x20), v63b
    0x68f: v68f = ADD v687(0x20), v655
    0x694: v694(0x0) = CONST 

    Begin block 0x696
    prev=[0x681, 0x69f], succ=[0x6ae, 0x69f]
    =================================
    0x696_0x0: v696_0 = PHI v694(0x0), v6a9
    0x699: v699 = LT v696_0, v686
    0x69a: v69a = ISZERO v699
    0x69b: v69b(0x6ae) = CONST 
    0x69e: JUMPI v69b(0x6ae), v69a

    Begin block 0x6ae
    prev=[0x696], succ=[0x6db, 0x6c2]
    =================================
    0x6b7: v6b7 = ADD v686, v68b
    0x6b9: v6b9(0x1f) = CONST 
    0x6bb: v6bb = AND v6b9(0x1f), v686
    0x6bd: v6bd = ISZERO v6bb
    0x6be: v6be(0x6db) = CONST 
    0x6c1: JUMPI v6be(0x6db), v6bd

    Begin block 0x6db
    prev=[0x6ae, 0x6c2], succ=[0x1c70x271]
    =================================
    0x6db_0x1: v6db_1 = PHI v6b7, v6d8
    0x6dd: v6dd(0x40) = CONST 
    0x6df: MSTORE v6dd(0x40), v6db_1
    0x6ea: JUMP v27f(0x1c7)

    Begin block 0x1c70x271
    prev=[0x6db], succ=[0x1e90x271]
    =================================
    0x1c80x271: v2711c8(0x40) = CONST 
    0x1cb0x271: v2711cb = MLOAD v2711c8(0x40)
    0x1cc0x271: v2711cc(0x20) = CONST 
    0x1d00x271: MSTORE v2711cb, v2711cc(0x20)
    0x1d20x271: v2711d2 = MLOAD v63b
    0x1d50x271: v2711d5 = ADD v2711cb, v2711cc(0x20)
    0x1d60x271: MSTORE v2711d5, v2711d2
    0x1d80x271: v2711d8 = MLOAD v63b
    0x1df0x271: v2711df = ADD v2711cb, v2711c8(0x40)
    0x1e20x271: v2711e2 = ADD v63b, v2711cc(0x20)
    0x1e70x271: v2711e7(0x0) = CONST 

    Begin block 0x1e90x271
    prev=[0x1f20x271, 0x1c70x271], succ=[0x2010x271, 0x1f20x271]
    =================================
    0x1e90x271_0x0: v1e9271_0 = PHI v2711fc, v2711e7(0x0)
    0x1ec0x271: v2711ec = LT v1e9271_0, v2711d8
    0x1ed0x271: v2711ed = ISZERO v2711ec
    0x1ee0x271: v2711ee(0x201) = CONST 
    0x1f10x271: JUMPI v2711ee(0x201), v2711ed

    Begin block 0x2010x271
    prev=[0x1e90x271], succ=[0x22e0x271, 0x2150x271]
    =================================
    0x20a0x271: v27120a = ADD v2711d8, v2711df
    0x20c0x271: v27120c(0x1f) = CONST 
    0x20e0x271: v27120e = AND v27120c(0x1f), v2711d8
    0x2100x271: v271210 = ISZERO v27120e
    0x2110x271: v271211(0x22e) = CONST 
    0x2140x271: JUMPI v271211(0x22e), v271210

    Begin block 0x22e0x271
    prev=[0x2010x271, 0x2150x271], succ=[]
    =================================
    0x22e0x271_0x1: v22e271_1 = PHI v27122b, v27120a
    0x2340x271: v271234(0x40) = CONST 
    0x2360x271: v271236 = MLOAD v271234(0x40)
    0x2390x271: v271239 = SUB v22e271_1, v271236
    0x23b0x271: RETURN v271236, v271239

    Begin block 0x2150x271
    prev=[0x2010x271], succ=[0x22e0x271]
    =================================
    0x2170x271: v271217 = SUB v27120a, v27120e
    0x2190x271: v271219 = MLOAD v271217
    0x21a0x271: v27121a(0x1) = CONST 
    0x21d0x271: v27121d(0x20) = CONST 
    0x21f0x271: v27121f = SUB v27121d(0x20), v27120e
    0x2200x271: v271220(0x100) = CONST 
    0x2230x271: v271223 = EXP v271220(0x100), v27121f
    0x2240x271: v271224 = SUB v271223, v27121a(0x1)
    0x2250x271: v271225 = NOT v271224
    0x2260x271: v271226 = AND v271225, v271219
    0x2280x271: MSTORE v271217, v271226
    0x2290x271: v271229(0x20) = CONST 
    0x22b0x271: v27122b = ADD v271229(0x20), v271217

    Begin block 0x1f20x271
    prev=[0x1e90x271], succ=[0x1e90x271]
    =================================
    0x1f20x271_0x0: v1f2271_0 = PHI v2711fc, v2711e7(0x0)
    0x1f40x271: v2711f4 = ADD v1f2271_0, v2711e2
    0x1f50x271: v2711f5 = MLOAD v2711f4
    0x1f80x271: v2711f8 = ADD v1f2271_0, v2711df
    0x1f90x271: MSTORE v2711f8, v2711f5
    0x1fa0x271: v2711fa(0x20) = CONST 
    0x1fc0x271: v2711fc = ADD v2711fa(0x20), v1f2271_0
    0x1fd0x271: v2711fd(0x1e9) = CONST 
    0x2000x271: JUMP v2711fd(0x1e9)

    Begin block 0x6c2
    prev=[0x6ae], succ=[0x6db]
    =================================
    0x6c4: v6c4 = SUB v6b7, v6bb
    0x6c6: v6c6 = MLOAD v6c4
    0x6c7: v6c7(0x1) = CONST 
    0x6ca: v6ca(0x20) = CONST 
    0x6cc: v6cc = SUB v6ca(0x20), v6bb
    0x6cd: v6cd(0x100) = CONST 
    0x6d0: v6d0 = EXP v6cd(0x100), v6cc
    0x6d1: v6d1 = SUB v6d0, v6c7(0x1)
    0x6d2: v6d2 = NOT v6d1
    0x6d3: v6d3 = AND v6d2, v6c6
    0x6d5: MSTORE v6c4, v6d3
    0x6d6: v6d6(0x20) = CONST 
    0x6d8: v6d8 = ADD v6d6(0x20), v6c4

    Begin block 0x69f
    prev=[0x696], succ=[0x696]
    =================================
    0x69f_0x0: v69f_0 = PHI v694(0x0), v6a9
    0x6a1: v6a1 = ADD v69f_0, v68f
    0x6a2: v6a2 = MLOAD v6a1
    0x6a5: v6a5 = ADD v69f_0, v68b
    0x6a6: MSTORE v6a5, v6a2
    0x6a7: v6a7(0x20) = CONST 
    0x6a9: v6a9 = ADD v6a7(0x20), v69f_0
    0x6aa: v6aa(0x696) = CONST 
    0x6ad: JUMP v6aa(0x696)

    Begin block 0x603
    prev=[0x5a3], succ=[0x608]
    =================================
    0x604: v604(0x60) = CONST 

    Begin block 0x58d
    prev=[0x584], succ=[0x584]
    =================================
    0x58d_0x0: v58d_0 = PHI v55d, v59e
    0x58d_0x1: v58d_1 = PHI v575, v59c
    0x58d_0x2: v58d_2 = PHI v577, v596
    0x58e: v58e = MLOAD v58d_0
    0x590: MSTORE v58d_1, v58e
    0x591: v591(0x1f) = CONST 
    0x593: v593(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v591(0x1f)
    0x596: v596 = ADD v58d_2, v593(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x598: v598(0x20) = CONST 
    0x59c: v59c = ADD v598(0x20), v58d_1
    0x59e: v59e = ADD v598(0x20), v58d_0
    0x59f: v59f(0x584) = CONST 
    0x5a2: JUMP v59f(0x584)

    Begin block 0x52f
    prev=[0x51b], succ=[0x548]
    =================================
    0x531: v531 = SUB v524, v528
    0x533: v533 = MLOAD v531
    0x534: v534(0x1) = CONST 
    0x537: v537(0x20) = CONST 
    0x539: v539 = SUB v537(0x20), v528
    0x53a: v53a(0x100) = CONST 
    0x53d: v53d = EXP v53a(0x100), v539
    0x53e: v53e = SUB v53d, v534(0x1)
    0x53f: v53f = NOT v53e
    0x540: v540 = AND v53f, v533
    0x542: MSTORE v531, v540
    0x543: v543(0x20) = CONST 
    0x545: v545 = ADD v543(0x20), v531

    Begin block 0x50c
    prev=[0x503], succ=[0x503]
    =================================
    0x50c_0x0: v50c_0 = PHI v501(0x0), v516
    0x50e: v50e = ADD v50c_0, v4fc
    0x50f: v50f = MLOAD v50e
    0x512: v512 = ADD v50c_0, v4f4
    0x513: MSTORE v512, v50f
    0x514: v514(0x20) = CONST 
    0x516: v516 = ADD v514(0x20), v50c_0
    0x517: v517(0x503) = CONST 
    0x51a: JUMP v517(0x503)

}

function implementation()() public {
    Begin block 0x324
    prev=[], succ=[0x32c, 0x330]
    =================================
    0x325: v325 = CALLVALUE 
    0x327: v327 = ISZERO v325
    0x328: v328(0x330) = CONST 
    0x32b: JUMPI v328(0x330), v327

    Begin block 0x32c
    prev=[0x324], succ=[]
    =================================
    0x32c: v32c(0x0) = CONST 
    0x32f: REVERT v32c(0x0), v32c(0x0)

    Begin block 0x330
    prev=[0x324], succ=[0x6eb]
    =================================
    0x332: v332(0xafc) = CONST 
    0x335: v335(0x6eb) = CONST 
    0x338: JUMP v335(0x6eb)

    Begin block 0x6eb
    prev=[0x330], succ=[0xafc]
    =================================
    0x6ec: v6ec(0x2) = CONST 
    0x6ee: v6ee = SLOAD v6ec(0x2)
    0x6ef: v6ef(0x1) = CONST 
    0x6f1: v6f1(0x1) = CONST 
    0x6f3: v6f3(0xa0) = CONST 
    0x6f5: v6f5(0x10000000000000000000000000000000000000000) = SHL v6f3(0xa0), v6f1(0x1)
    0x6f6: v6f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6f5(0x10000000000000000000000000000000000000000), v6ef(0x1)
    0x6f7: v6f7 = AND v6f6(0xffffffffffffffffffffffffffffffffffffffff), v6ee
    0x6f9: JUMP v332(0xafc)

    Begin block 0xafc
    prev=[0x6eb], succ=[]
    =================================
    0xafd: vafd(0x40) = CONST 
    0xb00: vb00 = MLOAD vafd(0x40)
    0xb01: vb01(0x1) = CONST 
    0xb03: vb03(0x1) = CONST 
    0xb05: vb05(0xa0) = CONST 
    0xb07: vb07(0x10000000000000000000000000000000000000000) = SHL vb05(0xa0), vb03(0x1)
    0xb08: vb08(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb07(0x10000000000000000000000000000000000000000), vb01(0x1)
    0xb0b: vb0b = AND v6f7, vb08(0xffffffffffffffffffffffffffffffffffffffff)
    0xb0d: MSTORE vb00, vb0b
    0xb0e: vb0e = MLOAD vafd(0x40)
    0xb12: vb12(0x0) = SUB vb00, vb0e
    0xb13: vb13(0x20) = CONST 
    0xb15: vb15(0x20) = ADD vb13(0x20), vb12(0x0)
    0xb17: RETURN vb0e, vb15(0x20)

}

function renounceOwnership()() public {
    Begin block 0x355
    prev=[], succ=[0x35d, 0x361]
    =================================
    0x356: v356 = CALLVALUE 
    0x358: v358 = ISZERO v356
    0x359: v359(0x361) = CONST 
    0x35c: JUMPI v359(0x361), v358

    Begin block 0x35d
    prev=[0x355], succ=[]
    =================================
    0x35d: v35d(0x0) = CONST 
    0x360: REVERT v35d(0x0), v35d(0x0)

    Begin block 0x361
    prev=[0x355], succ=[0x6fa]
    =================================
    0x363: v363(0xb37) = CONST 
    0x366: v366(0x6fa) = CONST 
    0x369: JUMP v366(0x6fa)

    Begin block 0x6fa
    prev=[0x361], succ=[0xa5cB0x6fa]
    =================================
    0x6fb: v6fb(0x702) = CONST 
    0x6fe: v6fe(0xa5c) = CONST 
    0x701: JUMP v6fe(0xa5c)

    Begin block 0xa5cB0x6fa
    prev=[0x6fa], succ=[0x702]
    =================================
    0xa5dS0x6fa: va5dV6fa = CALLER 
    0xa5fS0x6fa: JUMP v6fb(0x702)

    Begin block 0x702
    prev=[0xa5cB0x6fa], succ=[0x7b8B0x702]
    =================================
    0x703: v703(0x1) = CONST 
    0x705: v705(0x1) = CONST 
    0x707: v707(0xa0) = CONST 
    0x709: v709(0x10000000000000000000000000000000000000000) = SHL v707(0xa0), v705(0x1)
    0x70a: v70a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v709(0x10000000000000000000000000000000000000000), v703(0x1)
    0x70b: v70b = AND v70a(0xffffffffffffffffffffffffffffffffffffffff), va5dV6fa
    0x70c: v70c(0x713) = CONST 
    0x70f: v70f(0x7b8) = CONST 
    0x712: JUMP v70f(0x7b8)

    Begin block 0x7b8B0x702
    prev=[0x702], succ=[0x713]
    =================================
    0x7b9S0x702: v7b9V702(0x0) = CONST 
    0x7bbS0x702: v7bbV702 = SLOAD v7b9V702(0x0)
    0x7bcS0x702: v7bcV702(0x1) = CONST 
    0x7beS0x702: v7beV702(0x1) = CONST 
    0x7c0S0x702: v7c0V702(0xa0) = CONST 
    0x7c2S0x702: v7c2V702(0x10000000000000000000000000000000000000000) = SHL v7c0V702(0xa0), v7beV702(0x1)
    0x7c3S0x702: v7c3V702(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c2V702(0x10000000000000000000000000000000000000000), v7bcV702(0x1)
    0x7c4S0x702: v7c4V702 = AND v7c3V702(0xffffffffffffffffffffffffffffffffffffffff), v7bbV702
    0x7c6S0x702: JUMP v70c(0x713)

    Begin block 0x713
    prev=[0x7b8B0x702], succ=[0x722, 0x76e]
    =================================
    0x714: v714(0x1) = CONST 
    0x716: v716(0x1) = CONST 
    0x718: v718(0xa0) = CONST 
    0x71a: v71a(0x10000000000000000000000000000000000000000) = SHL v718(0xa0), v716(0x1)
    0x71b: v71b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71a(0x10000000000000000000000000000000000000000), v714(0x1)
    0x71c: v71c = AND v71b(0xffffffffffffffffffffffffffffffffffffffff), v7c4V702
    0x71d: v71d = EQ v71c, v70b
    0x71e: v71e(0x76e) = CONST 
    0x721: JUMPI v71e(0x76e), v71d

    Begin block 0x722
    prev=[0x713], succ=[]
    =================================
    0x722: v722(0x40) = CONST 
    0x725: v725 = MLOAD v722(0x40)
    0x726: v726(0x461bcd) = CONST 
    0x72a: v72a(0xe5) = CONST 
    0x72c: v72c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v72a(0xe5), v726(0x461bcd)
    0x72e: MSTORE v725, v72c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x72f: v72f(0x20) = CONST 
    0x731: v731(0x4) = CONST 
    0x734: v734 = ADD v725, v731(0x4)
    0x737: MSTORE v734, v72f(0x20)
    0x738: v738(0x24) = CONST 
    0x73b: v73b = ADD v725, v738(0x24)
    0x73c: MSTORE v73b, v72f(0x20)
    0x73d: v73d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x75e: v75e(0x44) = CONST 
    0x761: v761 = ADD v725, v75e(0x44)
    0x762: MSTORE v761, v73d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x764: v764 = MLOAD v722(0x40)
    0x768: v768(0x0) = SUB v725, v764
    0x769: v769(0x64) = CONST 
    0x76b: v76b(0x64) = ADD v769(0x64), v768(0x0)
    0x76d: REVERT v764, v76b(0x64)

    Begin block 0x76e
    prev=[0x713], succ=[0xb37]
    =================================
    0x76f: v76f(0x0) = CONST 
    0x772: v772 = SLOAD v76f(0x0)
    0x773: v773(0x40) = CONST 
    0x775: v775 = MLOAD v773(0x40)
    0x776: v776(0x1) = CONST 
    0x778: v778(0x1) = CONST 
    0x77a: v77a(0xa0) = CONST 
    0x77c: v77c(0x10000000000000000000000000000000000000000) = SHL v77a(0xa0), v778(0x1)
    0x77d: v77d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v77c(0x10000000000000000000000000000000000000000), v776(0x1)
    0x780: v780 = AND v772, v77d(0xffffffffffffffffffffffffffffffffffffffff)
    0x782: v782(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x7a6: LOG3 v775, v76f(0x0), v782(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v780, v76f(0x0)
    0x7a7: v7a7(0x0) = CONST 
    0x7aa: v7aa = SLOAD v7a7(0x0)
    0x7ab: v7ab(0x1) = CONST 
    0x7ad: v7ad(0x1) = CONST 
    0x7af: v7af(0xa0) = CONST 
    0x7b1: v7b1(0x10000000000000000000000000000000000000000) = SHL v7af(0xa0), v7ad(0x1)
    0x7b2: v7b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b1(0x10000000000000000000000000000000000000000), v7ab(0x1)
    0x7b3: v7b3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v7b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b4: v7b4 = AND v7b3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v7aa
    0x7b6: SSTORE v7a7(0x0), v7b4
    0x7b7: JUMP v363(0xb37)

    Begin block 0xb37
    prev=[0x76e], succ=[]
    =================================
    0xb38: STOP 

}

function owner()() public {
    Begin block 0x36a
    prev=[], succ=[0x372, 0x376]
    =================================
    0x36b: v36b = CALLVALUE 
    0x36d: v36d = ISZERO v36b
    0x36e: v36e(0x376) = CONST 
    0x371: JUMPI v36e(0x376), v36d

    Begin block 0x372
    prev=[0x36a], succ=[]
    =================================
    0x372: v372(0x0) = CONST 
    0x375: REVERT v372(0x0), v372(0x0)

    Begin block 0x376
    prev=[0x36a], succ=[0x7b8B0x376]
    =================================
    0x378: v378(0xb58) = CONST 
    0x37b: v37b(0x7b8) = CONST 
    0x37e: JUMP v37b(0x7b8)

    Begin block 0x7b8B0x376
    prev=[0x376], succ=[0xb58]
    =================================
    0x7b9S0x376: v7b9V376(0x0) = CONST 
    0x7bbS0x376: v7bbV376 = SLOAD v7b9V376(0x0)
    0x7bcS0x376: v7bcV376(0x1) = CONST 
    0x7beS0x376: v7beV376(0x1) = CONST 
    0x7c0S0x376: v7c0V376(0xa0) = CONST 
    0x7c2S0x376: v7c2V376(0x10000000000000000000000000000000000000000) = SHL v7c0V376(0xa0), v7beV376(0x1)
    0x7c3S0x376: v7c3V376(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c2V376(0x10000000000000000000000000000000000000000), v7bcV376(0x1)
    0x7c4S0x376: v7c4V376 = AND v7c3V376(0xffffffffffffffffffffffffffffffffffffffff), v7bbV376
    0x7c6S0x376: JUMP v378(0xb58)

    Begin block 0xb58
    prev=[0x7b8B0x376], succ=[]
    =================================
    0xb59: vb59(0x40) = CONST 
    0xb5c: vb5c = MLOAD vb59(0x40)
    0xb5d: vb5d(0x1) = CONST 
    0xb5f: vb5f(0x1) = CONST 
    0xb61: vb61(0xa0) = CONST 
    0xb63: vb63(0x10000000000000000000000000000000000000000) = SHL vb61(0xa0), vb5f(0x1)
    0xb64: vb64(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb63(0x10000000000000000000000000000000000000000), vb5d(0x1)
    0xb67: vb67 = AND v7c4V376, vb64(0xffffffffffffffffffffffffffffffffffffffff)
    0xb69: MSTORE vb5c, vb67
    0xb6a: vb6a = MLOAD vb59(0x40)
    0xb6e: vb6e(0x0) = SUB vb5c, vb6a
    0xb6f: vb6f(0x20) = CONST 
    0xb71: vb71(0x20) = ADD vb6f(0x20), vb6e(0x0)
    0xb73: RETURN vb6a, vb71(0x20)

}

function _setImplementation(address)() public {
    Begin block 0x37f
    prev=[], succ=[0x387, 0x38b]
    =================================
    0x380: v380 = CALLVALUE 
    0x382: v382 = ISZERO v380
    0x383: v383(0x38b) = CONST 
    0x386: JUMPI v383(0x38b), v382

    Begin block 0x387
    prev=[0x37f], succ=[]
    =================================
    0x387: v387(0x0) = CONST 
    0x38a: REVERT v387(0x0), v387(0x0)

    Begin block 0x38b
    prev=[0x37f], succ=[0x39e, 0x3a2]
    =================================
    0x38d: v38d(0xb93) = CONST 
    0x390: v390(0x4) = CONST 
    0x393: v393 = CALLDATASIZE 
    0x394: v394 = SUB v393, v390(0x4)
    0x395: v395(0x20) = CONST 
    0x398: v398 = LT v394, v395(0x20)
    0x399: v399 = ISZERO v398
    0x39a: v39a(0x3a2) = CONST 
    0x39d: JUMPI v39a(0x3a2), v399

    Begin block 0x39e
    prev=[0x38b], succ=[]
    =================================
    0x39e: v39e(0x0) = CONST 
    0x3a1: REVERT v39e(0x0), v39e(0x0)

    Begin block 0x3a2
    prev=[0x38b], succ=[0x7c7]
    =================================
    0x3a4: v3a4 = CALLDATALOAD v390(0x4)
    0x3a5: v3a5(0x1) = CONST 
    0x3a7: v3a7(0x1) = CONST 
    0x3a9: v3a9(0xa0) = CONST 
    0x3ab: v3ab(0x10000000000000000000000000000000000000000) = SHL v3a9(0xa0), v3a7(0x1)
    0x3ac: v3ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ab(0x10000000000000000000000000000000000000000), v3a5(0x1)
    0x3ad: v3ad = AND v3ac(0xffffffffffffffffffffffffffffffffffffffff), v3a4
    0x3ae: v3ae(0x7c7) = CONST 
    0x3b1: JUMP v3ae(0x7c7)

    Begin block 0x7c7
    prev=[0x3a2], succ=[0x7da, 0x815]
    =================================
    0x7c8: v7c8(0x1) = CONST 
    0x7ca: v7ca = SLOAD v7c8(0x1)
    0x7cb: v7cb(0x1) = CONST 
    0x7cd: v7cd(0x1) = CONST 
    0x7cf: v7cf(0xa0) = CONST 
    0x7d1: v7d1(0x10000000000000000000000000000000000000000) = SHL v7cf(0xa0), v7cd(0x1)
    0x7d2: v7d2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d1(0x10000000000000000000000000000000000000000), v7cb(0x1)
    0x7d3: v7d3 = AND v7d2(0xffffffffffffffffffffffffffffffffffffffff), v7ca
    0x7d4: v7d4 = CALLER 
    0x7d5: v7d5 = EQ v7d4, v7d3
    0x7d6: v7d6(0x815) = CONST 
    0x7d9: JUMPI v7d6(0x815), v7d5

    Begin block 0x7da
    prev=[0x7c7], succ=[]
    =================================
    0x7da: v7da(0x40) = CONST 
    0x7dd: v7dd = MLOAD v7da(0x40)
    0x7de: v7de(0x461bcd) = CONST 
    0x7e2: v7e2(0xe5) = CONST 
    0x7e4: v7e4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7e2(0xe5), v7de(0x461bcd)
    0x7e6: MSTORE v7dd, v7e4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7e7: v7e7(0x20) = CONST 
    0x7e9: v7e9(0x4) = CONST 
    0x7ec: v7ec = ADD v7dd, v7e9(0x4)
    0x7ed: MSTORE v7ec, v7e7(0x20)
    0x7ee: v7ee(0xc) = CONST 
    0x7f0: v7f0(0x24) = CONST 
    0x7f3: v7f3 = ADD v7dd, v7f0(0x24)
    0x7f4: MSTORE v7f3, v7ee(0xc)
    0x7f5: v7f5(0x15539055551213d492569151) = CONST 
    0x802: v802(0xa2) = CONST 
    0x804: v804(0x554e415554484f52495a45440000000000000000000000000000000000000000) = SHL v802(0xa2), v7f5(0x15539055551213d492569151)
    0x805: v805(0x44) = CONST 
    0x808: v808 = ADD v7dd, v805(0x44)
    0x809: MSTORE v808, v804(0x554e415554484f52495a45440000000000000000000000000000000000000000)
    0x80b: v80b = MLOAD v7da(0x40)
    0x80f: v80f(0x0) = SUB v7dd, v80b
    0x810: v810(0x64) = CONST 
    0x812: v812(0x64) = ADD v810(0x64), v80f(0x0)
    0x814: REVERT v80b, v812(0x64)

    Begin block 0x815
    prev=[0x7c7], succ=[0xb93]
    =================================
    0x816: v816(0x2) = CONST 
    0x819: v819 = SLOAD v816(0x2)
    0x81a: v81a(0x1) = CONST 
    0x81c: v81c(0x1) = CONST 
    0x81e: v81e(0xa0) = CONST 
    0x820: v820(0x10000000000000000000000000000000000000000) = SHL v81e(0xa0), v81c(0x1)
    0x821: v821(0xffffffffffffffffffffffffffffffffffffffff) = SUB v820(0x10000000000000000000000000000000000000000), v81a(0x1)
    0x824: v824 = AND v821(0xffffffffffffffffffffffffffffffffffffffff), v3ad
    0x825: v825(0x1) = CONST 
    0x827: v827(0x1) = CONST 
    0x829: v829(0xa0) = CONST 
    0x82b: v82b(0x10000000000000000000000000000000000000000) = SHL v829(0xa0), v827(0x1)
    0x82c: v82c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v82b(0x10000000000000000000000000000000000000000), v825(0x1)
    0x82d: v82d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v82c(0xffffffffffffffffffffffffffffffffffffffff)
    0x82f: v82f = AND v819, v82d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x830: v830 = OR v82f, v824
    0x834: SSTORE v816(0x2), v830
    0x835: v835(0x40) = CONST 
    0x838: v838 = MLOAD v835(0x40)
    0x83b: v83b = AND v821(0xffffffffffffffffffffffffffffffffffffffff), v819
    0x83e: MSTORE v838, v83b
    0x842: v842 = AND v821(0xffffffffffffffffffffffffffffffffffffffff), v830
    0x843: v843(0x20) = CONST 
    0x846: v846 = ADD v838, v843(0x20)
    0x847: MSTORE v846, v842
    0x849: v849 = MLOAD v835(0x40)
    0x84a: v84a(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x86e: v86e(0x0) = SUB v838, v849
    0x871: v871(0x40) = ADD v835(0x40), v86e(0x0)
    0x873: LOG1 v849, v871(0x40), v84a(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x876: JUMP v38d(0xb93)

    Begin block 0xb93
    prev=[0x815], succ=[]
    =================================
    0xb94: STOP 

}

function transferOwnership(address)() public {
    Begin block 0x3b2
    prev=[], succ=[0x3ba, 0x3be]
    =================================
    0x3b3: v3b3 = CALLVALUE 
    0x3b5: v3b5 = ISZERO v3b3
    0x3b6: v3b6(0x3be) = CONST 
    0x3b9: JUMPI v3b6(0x3be), v3b5

    Begin block 0x3ba
    prev=[0x3b2], succ=[]
    =================================
    0x3ba: v3ba(0x0) = CONST 
    0x3bd: REVERT v3ba(0x0), v3ba(0x0)

    Begin block 0x3be
    prev=[0x3b2], succ=[0x3d1, 0x3d5]
    =================================
    0x3c0: v3c0(0xbb4) = CONST 
    0x3c3: v3c3(0x4) = CONST 
    0x3c6: v3c6 = CALLDATASIZE 
    0x3c7: v3c7 = SUB v3c6, v3c3(0x4)
    0x3c8: v3c8(0x20) = CONST 
    0x3cb: v3cb = LT v3c7, v3c8(0x20)
    0x3cc: v3cc = ISZERO v3cb
    0x3cd: v3cd(0x3d5) = CONST 
    0x3d0: JUMPI v3cd(0x3d5), v3cc

    Begin block 0x3d1
    prev=[0x3be], succ=[]
    =================================
    0x3d1: v3d1(0x0) = CONST 
    0x3d4: REVERT v3d1(0x0), v3d1(0x0)

    Begin block 0x3d5
    prev=[0x3be], succ=[0x877]
    =================================
    0x3d7: v3d7 = CALLDATALOAD v3c3(0x4)
    0x3d8: v3d8(0x1) = CONST 
    0x3da: v3da(0x1) = CONST 
    0x3dc: v3dc(0xa0) = CONST 
    0x3de: v3de(0x10000000000000000000000000000000000000000) = SHL v3dc(0xa0), v3da(0x1)
    0x3df: v3df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3de(0x10000000000000000000000000000000000000000), v3d8(0x1)
    0x3e0: v3e0 = AND v3df(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0x3e1: v3e1(0x877) = CONST 
    0x3e4: JUMP v3e1(0x877)

    Begin block 0x877
    prev=[0x3d5], succ=[0xa5cB0x877]
    =================================
    0x878: v878(0x87f) = CONST 
    0x87b: v87b(0xa5c) = CONST 
    0x87e: JUMP v87b(0xa5c)

    Begin block 0xa5cB0x877
    prev=[0x877], succ=[0x87f]
    =================================
    0xa5dS0x877: va5dV877 = CALLER 
    0xa5fS0x877: JUMP v878(0x87f)

    Begin block 0x87f
    prev=[0xa5cB0x877], succ=[0x7b8B0x87f]
    =================================
    0x880: v880(0x1) = CONST 
    0x882: v882(0x1) = CONST 
    0x884: v884(0xa0) = CONST 
    0x886: v886(0x10000000000000000000000000000000000000000) = SHL v884(0xa0), v882(0x1)
    0x887: v887(0xffffffffffffffffffffffffffffffffffffffff) = SUB v886(0x10000000000000000000000000000000000000000), v880(0x1)
    0x888: v888 = AND v887(0xffffffffffffffffffffffffffffffffffffffff), va5dV877
    0x889: v889(0x890) = CONST 
    0x88c: v88c(0x7b8) = CONST 
    0x88f: JUMP v88c(0x7b8)

    Begin block 0x7b8B0x87f
    prev=[0x87f], succ=[0x890]
    =================================
    0x7b9S0x87f: v7b9V87f(0x0) = CONST 
    0x7bbS0x87f: v7bbV87f = SLOAD v7b9V87f(0x0)
    0x7bcS0x87f: v7bcV87f(0x1) = CONST 
    0x7beS0x87f: v7beV87f(0x1) = CONST 
    0x7c0S0x87f: v7c0V87f(0xa0) = CONST 
    0x7c2S0x87f: v7c2V87f(0x10000000000000000000000000000000000000000) = SHL v7c0V87f(0xa0), v7beV87f(0x1)
    0x7c3S0x87f: v7c3V87f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c2V87f(0x10000000000000000000000000000000000000000), v7bcV87f(0x1)
    0x7c4S0x87f: v7c4V87f = AND v7c3V87f(0xffffffffffffffffffffffffffffffffffffffff), v7bbV87f
    0x7c6S0x87f: JUMP v889(0x890)

    Begin block 0x890
    prev=[0x7b8B0x87f], succ=[0x89f, 0x8eb]
    =================================
    0x891: v891(0x1) = CONST 
    0x893: v893(0x1) = CONST 
    0x895: v895(0xa0) = CONST 
    0x897: v897(0x10000000000000000000000000000000000000000) = SHL v895(0xa0), v893(0x1)
    0x898: v898(0xffffffffffffffffffffffffffffffffffffffff) = SUB v897(0x10000000000000000000000000000000000000000), v891(0x1)
    0x899: v899 = AND v898(0xffffffffffffffffffffffffffffffffffffffff), v7c4V87f
    0x89a: v89a = EQ v899, v888
    0x89b: v89b(0x8eb) = CONST 
    0x89e: JUMPI v89b(0x8eb), v89a

    Begin block 0x89f
    prev=[0x890], succ=[]
    =================================
    0x89f: v89f(0x40) = CONST 
    0x8a2: v8a2 = MLOAD v89f(0x40)
    0x8a3: v8a3(0x461bcd) = CONST 
    0x8a7: v8a7(0xe5) = CONST 
    0x8a9: v8a9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v8a7(0xe5), v8a3(0x461bcd)
    0x8ab: MSTORE v8a2, v8a9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8ac: v8ac(0x20) = CONST 
    0x8ae: v8ae(0x4) = CONST 
    0x8b1: v8b1 = ADD v8a2, v8ae(0x4)
    0x8b4: MSTORE v8b1, v8ac(0x20)
    0x8b5: v8b5(0x24) = CONST 
    0x8b8: v8b8 = ADD v8a2, v8b5(0x24)
    0x8b9: MSTORE v8b8, v8ac(0x20)
    0x8ba: v8ba(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x8db: v8db(0x44) = CONST 
    0x8de: v8de = ADD v8a2, v8db(0x44)
    0x8df: MSTORE v8de, v8ba(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x8e1: v8e1 = MLOAD v89f(0x40)
    0x8e5: v8e5(0x0) = SUB v8a2, v8e1
    0x8e6: v8e6(0x64) = CONST 
    0x8e8: v8e8(0x64) = ADD v8e6(0x64), v8e5(0x0)
    0x8ea: REVERT v8e1, v8e8(0x64)

    Begin block 0x8eb
    prev=[0x890], succ=[0x8fa, 0x930]
    =================================
    0x8ec: v8ec(0x1) = CONST 
    0x8ee: v8ee(0x1) = CONST 
    0x8f0: v8f0(0xa0) = CONST 
    0x8f2: v8f2(0x10000000000000000000000000000000000000000) = SHL v8f0(0xa0), v8ee(0x1)
    0x8f3: v8f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8f2(0x10000000000000000000000000000000000000000), v8ec(0x1)
    0x8f5: v8f5 = AND v3e0, v8f3(0xffffffffffffffffffffffffffffffffffffffff)
    0x8f6: v8f6(0x930) = CONST 
    0x8f9: JUMPI v8f6(0x930), v8f5

    Begin block 0x8fa
    prev=[0x8eb], succ=[]
    =================================
    0x8fa: v8fa(0x40) = CONST 
    0x8fc: v8fc = MLOAD v8fa(0x40)
    0x8fd: v8fd(0x461bcd) = CONST 
    0x901: v901(0xe5) = CONST 
    0x903: v903(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v901(0xe5), v8fd(0x461bcd)
    0x905: MSTORE v8fc, v903(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x906: v906(0x4) = CONST 
    0x908: v908 = ADD v906(0x4), v8fc
    0x90b: v90b(0x20) = CONST 
    0x90d: v90d = ADD v90b(0x20), v908
    0x910: v910(0x20) = SUB v90d, v908
    0x912: MSTORE v908, v910(0x20)
    0x913: v913(0x26) = CONST 
    0x916: MSTORE v90d, v913(0x26)
    0x917: v917(0x20) = CONST 
    0x919: v919 = ADD v917(0x20), v90d
    0x91b: v91b(0xa61) = CONST 
    0x91e: v91e(0x26) = CONST 
    0x921: CODECOPY v919, v91b(0xa61), v91e(0x26)
    0x922: v922(0x40) = CONST 
    0x924: v924 = ADD v922(0x40), v919
    0x928: v928(0x40) = CONST 
    0x92a: v92a = MLOAD v928(0x40)
    0x92d: v92d(0x84) = SUB v924, v92a
    0x92f: REVERT v92a, v92d(0x84)

    Begin block 0x930
    prev=[0x8eb], succ=[0xbb4]
    =================================
    0x931: v931(0x0) = CONST 
    0x934: v934 = SLOAD v931(0x0)
    0x935: v935(0x40) = CONST 
    0x937: v937 = MLOAD v935(0x40)
    0x938: v938(0x1) = CONST 
    0x93a: v93a(0x1) = CONST 
    0x93c: v93c(0xa0) = CONST 
    0x93e: v93e(0x10000000000000000000000000000000000000000) = SHL v93c(0xa0), v93a(0x1)
    0x93f: v93f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v93e(0x10000000000000000000000000000000000000000), v938(0x1)
    0x942: v942 = AND v3e0, v93f(0xffffffffffffffffffffffffffffffffffffffff)
    0x945: v945 = AND v934, v93f(0xffffffffffffffffffffffffffffffffffffffff)
    0x947: v947(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x969: LOG3 v937, v931(0x0), v947(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v945, v942
    0x96a: v96a(0x0) = CONST 
    0x96d: v96d = SLOAD v96a(0x0)
    0x96e: v96e(0x1) = CONST 
    0x970: v970(0x1) = CONST 
    0x972: v972(0xa0) = CONST 
    0x974: v974(0x10000000000000000000000000000000000000000) = SHL v972(0xa0), v970(0x1)
    0x975: v975(0xffffffffffffffffffffffffffffffffffffffff) = SUB v974(0x10000000000000000000000000000000000000000), v96e(0x1)
    0x976: v976(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v975(0xffffffffffffffffffffffffffffffffffffffff)
    0x977: v977 = AND v976(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v96d
    0x978: v978(0x1) = CONST 
    0x97a: v97a(0x1) = CONST 
    0x97c: v97c(0xa0) = CONST 
    0x97e: v97e(0x10000000000000000000000000000000000000000) = SHL v97c(0xa0), v97a(0x1)
    0x97f: v97f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97e(0x10000000000000000000000000000000000000000), v978(0x1)
    0x983: v983 = AND v97f(0xffffffffffffffffffffffffffffffffffffffff), v3e0
    0x987: v987 = OR v983, v977
    0x989: SSTORE v96a(0x0), v987
    0x98a: JUMP v3c0(0xbb4)

    Begin block 0xbb4
    prev=[0x930], succ=[]
    =================================
    0xbb5: STOP 

}

function admin()() public {
    Begin block 0x3e5
    prev=[], succ=[0x3ed, 0x3f1]
    =================================
    0x3e6: v3e6 = CALLVALUE 
    0x3e8: v3e8 = ISZERO v3e6
    0x3e9: v3e9(0x3f1) = CONST 
    0x3ec: JUMPI v3e9(0x3f1), v3e8

    Begin block 0x3ed
    prev=[0x3e5], succ=[]
    =================================
    0x3ed: v3ed(0x0) = CONST 
    0x3f0: REVERT v3ed(0x0), v3ed(0x0)

    Begin block 0x3f1
    prev=[0x3e5], succ=[0x98b]
    =================================
    0x3f3: v3f3(0xbd5) = CONST 
    0x3f6: v3f6(0x98b) = CONST 
    0x3f9: JUMP v3f6(0x98b)

    Begin block 0x98b
    prev=[0x3f1], succ=[0xbd5]
    =================================
    0x98c: v98c(0x1) = CONST 
    0x98e: v98e = SLOAD v98c(0x1)
    0x98f: v98f(0x1) = CONST 
    0x991: v991(0x1) = CONST 
    0x993: v993(0xa0) = CONST 
    0x995: v995(0x10000000000000000000000000000000000000000) = SHL v993(0xa0), v991(0x1)
    0x996: v996(0xffffffffffffffffffffffffffffffffffffffff) = SUB v995(0x10000000000000000000000000000000000000000), v98f(0x1)
    0x997: v997 = AND v996(0xffffffffffffffffffffffffffffffffffffffff), v98e
    0x999: JUMP v3f3(0xbd5)

    Begin block 0xbd5
    prev=[0x98b], succ=[]
    =================================
    0xbd6: vbd6(0x40) = CONST 
    0xbd9: vbd9 = MLOAD vbd6(0x40)
    0xbda: vbda(0x1) = CONST 
    0xbdc: vbdc(0x1) = CONST 
    0xbde: vbde(0xa0) = CONST 
    0xbe0: vbe0(0x10000000000000000000000000000000000000000) = SHL vbde(0xa0), vbdc(0x1)
    0xbe1: vbe1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbe0(0x10000000000000000000000000000000000000000), vbda(0x1)
    0xbe4: vbe4 = AND v997, vbe1(0xffffffffffffffffffffffffffffffffffffffff)
    0xbe6: MSTORE vbd9, vbe4
    0xbe7: vbe7 = MLOAD vbd6(0x40)
    0xbeb: vbeb(0x0) = SUB vbd9, vbe7
    0xbec: vbec(0x20) = CONST 
    0xbee: vbee(0x20) = ADD vbec(0x20), vbeb(0x0)
    0xbf0: RETURN vbe7, vbee(0x20)

}

function fallback()() public {
    Begin block 0xc05
    prev=[], succ=[]
    =================================
    0x90: STOP 

}

