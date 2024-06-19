function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xd61]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xd4d: vd4d(0xd61) = CONST 
    0xd4e: JUMPI vd4d(0xd61), v8

    Begin block 0xd
    prev=[0x0], succ=[0x59, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5d36b190) = CONST 
    0x19: v19 = GT v14(0x5d36b190), v12
    0x1a: v1a(0x59) = CONST 
    0x1d: JUMPI v1a(0x59), v19

    Begin block 0x59
    prev=[0xd], succ=[0xd64, 0x65]
    =================================
    0x5b: v5b(0xc340a24) = CONST 
    0x60: v60 = EQ v5b(0xc340a24), v12
    0xd59: vd59(0xd64) = CONST 
    0xd5a: JUMPI vd59(0xd64), v60

    Begin block 0xd64
    prev=[0x59], succ=[]
    =================================
    0xd65: vd65(0x90) = CONST 
    0xd66: CALLPRIVATE vd65(0x90)

    Begin block 0x65
    prev=[0x59], succ=[0xd67, 0x70]
    =================================
    0x66: v66(0x3659cfe6) = CONST 
    0x6b: v6b = EQ v66(0x3659cfe6), v12
    0xd5b: vd5b(0xd67) = CONST 
    0xd5c: JUMPI vd5b(0xd67), v6b

    Begin block 0xd67
    prev=[0x65], succ=[]
    =================================
    0xd68: vd68(0xe7) = CONST 
    0xd69: CALLPRIVATE vd68(0xe7)

    Begin block 0x70
    prev=[0x65], succ=[0xd6a, 0x7b]
    =================================
    0x71: v71(0x4f1ef286) = CONST 
    0x76: v76 = EQ v71(0x4f1ef286), v12
    0xd5d: vd5d(0xd6a) = CONST 
    0xd5e: JUMPI vd5d(0xd6a), v76

    Begin block 0xd6a
    prev=[0x70], succ=[]
    =================================
    0xd6b: vd6b(0x138) = CONST 
    0xd6c: CALLPRIVATE vd6b(0x138)

    Begin block 0x7b
    prev=[0x70], succ=[0xd61, 0xd6d]
    =================================
    0x7c: v7c(0x5c60da1b) = CONST 
    0x81: v81 = EQ v7c(0x5c60da1b), v12
    0xd5f: vd5f(0xd6d) = CONST 
    0xd60: JUMPI vd5f(0xd6d), v81

    Begin block 0xd61
    prev=[0x0, 0x7b], succ=[]
    =================================
    0xd62: vd62(0x86) = CONST 
    0xd63: CALLPRIVATE vd62(0x86)

    Begin block 0xd6d
    prev=[0x7b], succ=[]
    =================================
    0xd6e: vd6e(0x1d1) = CONST 
    0xd6f: CALLPRIVATE vd6e(0x1d1)

    Begin block 0x1e
    prev=[0xd], succ=[0xd70, 0x29]
    =================================
    0x1f: v1f(0x5d36b190) = CONST 
    0x24: v24 = EQ v1f(0x5d36b190), v12
    0xd4f: vd4f(0xd70) = CONST 
    0xd50: JUMPI vd4f(0xd70), v24

    Begin block 0xd70
    prev=[0x1e], succ=[]
    =================================
    0xd71: vd71(0x228) = CONST 
    0xd72: CALLPRIVATE vd71(0x228)

    Begin block 0x29
    prev=[0x1e], succ=[0xd73, 0x34]
    =================================
    0x2a: v2a(0xc7af3352) = CONST 
    0x2f: v2f = EQ v2a(0xc7af3352), v12
    0xd51: vd51(0xd73) = CONST 
    0xd52: JUMPI vd51(0xd73), v2f

    Begin block 0xd73
    prev=[0x29], succ=[]
    =================================
    0xd74: vd74(0x23f) = CONST 
    0xd75: CALLPRIVATE vd74(0x23f)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xd76]
    =================================
    0x35: v35(0xcf7a1d77) = CONST 
    0x3a: v3a = EQ v35(0xcf7a1d77), v12
    0xd53: vd53(0xd76) = CONST 
    0xd54: JUMPI vd53(0xd76), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xd79, 0x4a]
    =================================
    0x40: v40(0xd38bfff4) = CONST 
    0x45: v45 = EQ v40(0xd38bfff4), v12
    0xd55: vd55(0xd79) = CONST 
    0xd56: JUMPI vd55(0xd79), v45

    Begin block 0xd79
    prev=[0x3f], succ=[]
    =================================
    0xd7a: vd7a(0x369) = CONST 
    0xd7b: CALLPRIVATE vd7a(0x369)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0xd7c]
    =================================
    0x4b: v4b(0xf851a440) = CONST 
    0x50: v50 = EQ v4b(0xf851a440), v12
    0xd57: vd57(0xd7c) = CONST 
    0xd58: JUMPI vd57(0xd7c), v50

    Begin block 0x55
    prev=[0x4a], succ=[]
    =================================
    0x55: v55(0x86) = CONST 
    0x58: JUMP v55(0x86)

    Begin block 0xd7c
    prev=[0x4a], succ=[]
    =================================
    0xd7d: vd7d(0x3ba) = CONST 
    0xd7e: CALLPRIVATE vd7d(0x3ba)

    Begin block 0xd76
    prev=[0x34], succ=[]
    =================================
    0xd77: vd77(0x26e) = CONST 
    0xd78: CALLPRIVATE vd77(0x26e)

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0x138
    prev=[], succ=[0x14a, 0x14e]
    =================================
    0x139: v139(0x1cf) = CONST 
    0x13c: v13c(0x4) = CONST 
    0x13f: v13f = CALLDATASIZE 
    0x140: v140 = SUB v13f, v13c(0x4)
    0x141: v141(0x40) = CONST 
    0x144: v144 = LT v140, v141(0x40)
    0x145: v145 = ISZERO v144
    0x146: v146(0x14e) = CONST 
    0x149: JUMPI v146(0x14e), v145

    Begin block 0x14a
    prev=[0x138], succ=[]
    =================================
    0x14a: v14a(0x0) = CONST 
    0x14d: REVERT v14a(0x0), v14a(0x0)

    Begin block 0x14e
    prev=[0x138], succ=[0x187, 0x18b]
    =================================
    0x150: v150 = ADD v13c(0x4), v140
    0x154: v154 = CALLDATALOAD v13c(0x4)
    0x155: v155(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16a: v16a = AND v155(0xffffffffffffffffffffffffffffffffffffffff), v154
    0x16c: v16c(0x20) = CONST 
    0x16e: v16e(0x24) = ADD v16c(0x20), v13c(0x4)
    0x174: v174 = CALLDATALOAD v16e(0x24)
    0x176: v176(0x20) = CONST 
    0x178: v178(0x44) = ADD v176(0x20), v16e(0x24)
    0x17a: v17a(0x100000000) = CONST 
    0x181: v181 = GT v174, v17a(0x100000000)
    0x182: v182 = ISZERO v181
    0x183: v183(0x18b) = CONST 
    0x186: JUMPI v183(0x18b), v182

    Begin block 0x187
    prev=[0x14e], succ=[]
    =================================
    0x187: v187(0x0) = CONST 
    0x18a: REVERT v187(0x0), v187(0x0)

    Begin block 0x18b
    prev=[0x14e], succ=[0x199, 0x19d]
    =================================
    0x18d: v18d = ADD v13c(0x4), v174
    0x18f: v18f(0x20) = CONST 
    0x192: v192 = ADD v18d, v18f(0x20)
    0x193: v193 = GT v192, v150
    0x194: v194 = ISZERO v193
    0x195: v195(0x19d) = CONST 
    0x198: JUMPI v195(0x19d), v194

    Begin block 0x199
    prev=[0x18b], succ=[]
    =================================
    0x199: v199(0x0) = CONST 
    0x19c: REVERT v199(0x0), v199(0x0)

    Begin block 0x19d
    prev=[0x18b], succ=[0x1bb, 0x1bf]
    =================================
    0x19f: v19f = CALLDATALOAD v18d
    0x1a1: v1a1(0x20) = CONST 
    0x1a3: v1a3 = ADD v1a1(0x20), v18d
    0x1a6: v1a6(0x1) = CONST 
    0x1a9: v1a9 = MUL v19f, v1a6(0x1)
    0x1ab: v1ab = ADD v1a3, v1a9
    0x1ac: v1ac = GT v1ab, v150
    0x1ad: v1ad(0x100000000) = CONST 
    0x1b4: v1b4 = GT v19f, v1ad(0x100000000)
    0x1b5: v1b5 = OR v1b4, v1ac
    0x1b6: v1b6 = ISZERO v1b5
    0x1b7: v1b7(0x1bf) = CONST 
    0x1ba: JUMPI v1b7(0x1bf), v1b6

    Begin block 0x1bb
    prev=[0x19d], succ=[]
    =================================
    0x1bb: v1bb(0x0) = CONST 
    0x1be: REVERT v1bb(0x0), v1bb(0x0)

    Begin block 0x1bf
    prev=[0x19d], succ=[0x4c0]
    =================================
    0x1cb: v1cb(0x4c0) = CONST 
    0x1ce: JUMP v1cb(0x4c0)

    Begin block 0x4c0
    prev=[0x1bf], succ=[0x66cB0x4c0]
    =================================
    0x4c1: v4c1(0x4c8) = CONST 
    0x4c4: v4c4(0x66c) = CONST 
    0x4c7: JUMP v4c4(0x66c)

    Begin block 0x66cB0x4c0
    prev=[0x4c0], succ=[0x9ffB0x66cB0x4c0]
    =================================
    0x66dS0x4c0: v66dV4c0(0x0) = CONST 
    0x66fS0x4c0: v66fV4c0(0x676) = CONST 
    0x672S0x4c0: v672V4c0(0x9ff) = CONST 
    0x675S0x4c0: JUMP v672V4c0(0x9ff)

    Begin block 0x9ffB0x66cB0x4c0
    prev=[0x66cB0x4c0], succ=[0x676B0x4c0]
    =================================
    0xa00S0x66cS0x4c0: va00V66cV4c0(0x0) = CONST 
    0xa03S0x66cS0x4c0: va03V66cV4c0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x66cS0x4c0: va24V66cV4c0(0x0) = CONST 
    0xa26S0x66cS0x4c0: va26V66cV4c0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V66cV4c0(0x0), va03V66cV4c0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x66cS0x4c0: va2aV66cV4c0 = SLOAD va26V66cV4c0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x66cS0x4c0: JUMP v66fV4c0(0x676)

    Begin block 0x676B0x4c0
    prev=[0x9ffB0x66cB0x4c0], succ=[0x4c8]
    =================================
    0x677S0x4c0: v677V4c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68cS0x4c0: v68cV4c0 = AND v677V4c0(0xffffffffffffffffffffffffffffffffffffffff), va2aV66cV4c0
    0x68dS0x4c0: v68dV4c0 = CALLER 
    0x68eS0x4c0: v68eV4c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a3S0x4c0: v6a3V4c0 = AND v68eV4c0(0xffffffffffffffffffffffffffffffffffffffff), v68dV4c0
    0x6a4S0x4c0: v6a4V4c0 = EQ v6a3V4c0, v68cV4c0
    0x6a8S0x4c0: JUMP v4c1(0x4c8)

    Begin block 0x4c8
    prev=[0x676B0x4c0], succ=[0x4cd, 0x53a]
    =================================
    0x4c9: v4c9(0x53a) = CONST 
    0x4cc: JUMPI v4c9(0x53a), v6a4V4c0

    Begin block 0x4cd
    prev=[0x4c8], succ=[]
    =================================
    0x4cd: v4cd(0x40) = CONST 
    0x4cf: v4cf = MLOAD v4cd(0x40)
    0x4d0: v4d0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4f2: MSTORE v4cf, v4d0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4f3: v4f3(0x4) = CONST 
    0x4f5: v4f5 = ADD v4f3(0x4), v4cf
    0x4f8: v4f8(0x20) = CONST 
    0x4fa: v4fa = ADD v4f8(0x20), v4f5
    0x4fd: v4fd(0x20) = SUB v4fa, v4f5
    0x4ff: MSTORE v4f5, v4fd(0x20)
    0x500: v500(0x1a) = CONST 
    0x503: MSTORE v4fa, v500(0x1a)
    0x504: v504(0x20) = CONST 
    0x506: v506 = ADD v504(0x20), v4fa
    0x508: v508(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = CONST 
    0x52a: MSTORE v506, v508(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x52c: v52c(0x20) = CONST 
    0x52e: v52e = ADD v52c(0x20), v506
    0x532: v532(0x40) = CONST 
    0x534: v534 = MLOAD v532(0x40)
    0x537: v537(0x64) = SUB v52e, v534
    0x539: REVERT v534, v537(0x64)

    Begin block 0x53a
    prev=[0x4c8], succ=[0xa30B0x53a]
    =================================
    0x53b: v53b(0x543) = CONST 
    0x53f: v53f(0xa30) = CONST 
    0x542: JUMP v53f(0xa30), v16a, v53b(0x543)

    Begin block 0xa30B0x53a
    prev=[0x53a], succ=[0xa39B0x53a]
    =================================
    0xa31S0x53a: va31V53a(0xa39) = CONST 
    0xa35S0x53a: va35V53a(0xbc0) = CONST 
    0xa38S0x53a: CALLPRIVATE va35V53a(0xbc0), v16a, va31V53a(0xa39)

    Begin block 0xa39B0x53a
    prev=[0xa30B0x53a], succ=[0x543]
    =================================
    0xa3bS0x53a: va3bV53a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa50S0x53a: va50V53a = AND va3bV53a(0xffffffffffffffffffffffffffffffffffffffff), v16a
    0xa51S0x53a: va51V53a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0xa72S0x53a: va72V53a(0x40) = CONST 
    0xa74S0x53a: va74V53a = MLOAD va72V53a(0x40)
    0xa75S0x53a: va75V53a(0x40) = CONST 
    0xa77S0x53a: va77V53a = MLOAD va75V53a(0x40)
    0xa7aS0x53a: va7aV53a(0x0) = SUB va74V53a, va77V53a
    0xa7cS0x53a: LOG2 va77V53a, va7aV53a(0x0), va51V53a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), va50V53a
    0xa7eS0x53a: JUMP v53b(0x543)

    Begin block 0x543
    prev=[0xa39B0x53a], succ=[0x58d, 0x5ae]
    =================================
    0x544: v544(0x0) = CONST 
    0x547: v547(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x55c: v55c = AND v547(0xffffffffffffffffffffffffffffffffffffffff), v16a
    0x55f: v55f(0x40) = CONST 
    0x561: v561 = MLOAD v55f(0x40)
    0x568: CALLDATACOPY v561, v1a3, v19f
    0x56b: v56b = ADD v561, v19f
    0x574: v574(0x0) = CONST 
    0x576: v576(0x40) = CONST 
    0x578: v578 = MLOAD v576(0x40)
    0x57b: v57b = SUB v56b, v578
    0x57e: v57e = GAS 
    0x57f: v57f = DELEGATECALL v57e, v55c, v578, v57b, v578, v574(0x0)
    0x583: v583 = RETURNDATASIZE 
    0x585: v585(0x0) = CONST 
    0x588: v588 = EQ v583, v585(0x0)
    0x589: v589(0x5ae) = CONST 
    0x58c: JUMPI v589(0x5ae), v588

    Begin block 0x58d
    prev=[0x543], succ=[0x5b3]
    =================================
    0x58d: v58d(0x40) = CONST 
    0x58f: v58f = MLOAD v58d(0x40)
    0x592: v592(0x1f) = CONST 
    0x594: v594(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v592(0x1f)
    0x595: v595(0x3f) = CONST 
    0x597: v597 = RETURNDATASIZE 
    0x598: v598 = ADD v597, v595(0x3f)
    0x599: v599 = AND v598, v594(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x59b: v59b = ADD v58f, v599
    0x59c: v59c(0x40) = CONST 
    0x59e: MSTORE v59c(0x40), v59b
    0x59f: v59f = RETURNDATASIZE 
    0x5a1: MSTORE v58f, v59f
    0x5a2: v5a2 = RETURNDATASIZE 
    0x5a3: v5a3(0x0) = CONST 
    0x5a5: v5a5(0x20) = CONST 
    0x5a8: v5a8 = ADD v58f, v5a5(0x20)
    0x5a9: RETURNDATACOPY v5a8, v5a3(0x0), v5a2
    0x5aa: v5aa(0x5b3) = CONST 
    0x5ad: JUMP v5aa(0x5b3)

    Begin block 0x5b3
    prev=[0x58d, 0x5ae], succ=[0x5bd, 0x5c1]
    =================================
    0x5b9: v5b9(0x5c1) = CONST 
    0x5bc: JUMPI v5b9(0x5c1), v57f

    Begin block 0x5bd
    prev=[0x5b3], succ=[]
    =================================
    0x5bd: v5bd(0x0) = CONST 
    0x5c0: REVERT v5bd(0x0), v5bd(0x0)

    Begin block 0x5c1
    prev=[0x5b3], succ=[0x1cf]
    =================================
    0x5c6: JUMP v139(0x1cf)

    Begin block 0x1cf
    prev=[0x5c1], succ=[]
    =================================
    0x1d0: STOP 

    Begin block 0x5ae
    prev=[0x543], succ=[0x5b3]
    =================================
    0x5af: v5af(0x60) = CONST 

}

function implementation()() public {
    Begin block 0x1d1
    prev=[], succ=[0x1d9, 0x1dd]
    =================================
    0x1d2: v1d2 = CALLVALUE 
    0x1d4: v1d4 = ISZERO v1d2
    0x1d5: v1d5(0x1dd) = CONST 
    0x1d8: JUMPI v1d5(0x1dd), v1d4

    Begin block 0x1d9
    prev=[0x1d1], succ=[]
    =================================
    0x1d9: v1d9(0x0) = CONST 
    0x1dc: REVERT v1d9(0x0), v1d9(0x0)

    Begin block 0x1dd
    prev=[0x1d1], succ=[0x5c7B0x1dd]
    =================================
    0x1df: v1df(0x1e6) = CONST 
    0x1e2: v1e2(0x5c7) = CONST 
    0x1e5: JUMP v1e2(0x5c7)

    Begin block 0x5c7B0x1dd
    prev=[0x1dd], succ=[0x9a8B0x5c7B0x1dd]
    =================================
    0x5c8S0x1dd: v5c8V1dd(0x0) = CONST 
    0x5caS0x1dd: v5caV1dd(0x5d1) = CONST 
    0x5cdS0x1dd: v5cdV1dd(0x9a8) = CONST 
    0x5d0S0x1dd: JUMP v5cdV1dd(0x9a8)

    Begin block 0x9a8B0x5c7B0x1dd
    prev=[0x5c7B0x1dd], succ=[0x5d1B0x1dd]
    =================================
    0x9a9S0x5c7S0x1dd: v9a9V5c7V1dd(0x0) = CONST 
    0x9acS0x5c7S0x1dd: v9acV5c7V1dd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x9cdS0x5c7S0x1dd: v9cdV5c7V1dd(0x0) = CONST 
    0x9cfS0x5c7S0x1dd: v9cfV5c7V1dd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v9cdV5c7V1dd(0x0), v9acV5c7V1dd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d3S0x5c7S0x1dd: v9d3V5c7V1dd = SLOAD v9cfV5c7V1dd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d8S0x5c7S0x1dd: JUMP v5caV1dd(0x5d1)

    Begin block 0x5d1B0x1dd
    prev=[0x9a8B0x5c7B0x1dd], succ=[0x1e6]
    =================================
    0x5d5S0x1dd: JUMP v1df(0x1e6)

    Begin block 0x1e6
    prev=[0x5d1B0x1dd], succ=[]
    =================================
    0x1e7: v1e7(0x40) = CONST 
    0x1e9: v1e9 = MLOAD v1e7(0x40)
    0x1ec: v1ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x201: v201 = AND v1ec(0xffffffffffffffffffffffffffffffffffffffff), v9d3V5c7V1dd
    0x202: v202(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x217: v217 = AND v202(0xffffffffffffffffffffffffffffffffffffffff), v201
    0x219: MSTORE v1e9, v217
    0x21a: v21a(0x20) = CONST 
    0x21c: v21c = ADD v21a(0x20), v1e9
    0x220: v220(0x40) = CONST 
    0x222: v222 = MLOAD v220(0x40)
    0x225: v225(0x20) = SUB v21c, v222
    0x227: RETURN v222, v225(0x20)

}

function claimGovernance()() public {
    Begin block 0x228
    prev=[], succ=[0x230, 0x234]
    =================================
    0x229: v229 = CALLVALUE 
    0x22b: v22b = ISZERO v229
    0x22c: v22c(0x234) = CONST 
    0x22f: JUMPI v22c(0x234), v22b

    Begin block 0x230
    prev=[0x228], succ=[]
    =================================
    0x230: v230(0x0) = CONST 
    0x233: REVERT v230(0x0), v230(0x0)

    Begin block 0x234
    prev=[0x228], succ=[0x5d6B0x234]
    =================================
    0x236: v236(0x23d) = CONST 
    0x239: v239(0x5d6) = CONST 
    0x23c: JUMP v239(0x5d6), v236(0x23d)

    Begin block 0x5d6B0x234
    prev=[0x234], succ=[0xa7fB0x234]
    =================================
    0x5d7S0x234: v5d7V234(0x5de) = CONST 
    0x5daS0x234: v5daV234(0xa7f) = CONST 
    0x5ddS0x234: JUMP v5daV234(0xa7f)

    Begin block 0xa7fB0x234
    prev=[0x5d6B0x234], succ=[0x5deB0x234]
    =================================
    0xa80S0x234: va80V234(0x0) = CONST 
    0xa83S0x234: va83V234(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = CONST 
    0xaa4S0x234: vaa4V234(0x0) = CONST 
    0xaa6S0x234: vaa6V234(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = SHL vaa4V234(0x0), va83V234(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db)
    0xaaaS0x234: vaaaV234 = SLOAD vaa6V234(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db)
    0xaafS0x234: JUMP v5d7V234(0x5de)

    Begin block 0x5deB0x234
    prev=[0xa7fB0x234], succ=[0x611B0x234, 0x661B0x234]
    =================================
    0x5dfS0x234: v5dfV234(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5f4S0x234: v5f4V234 = AND v5dfV234(0xffffffffffffffffffffffffffffffffffffffff), vaaaV234
    0x5f5S0x234: v5f5V234 = CALLER 
    0x5f6S0x234: v5f6V234(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x60bS0x234: v60bV234 = AND v5f6V234(0xffffffffffffffffffffffffffffffffffffffff), v5f5V234
    0x60cS0x234: v60cV234 = EQ v60bV234, v5f4V234
    0x60dS0x234: v60dV234(0x661) = CONST 
    0x610S0x234: JUMPI v60dV234(0x661), v60cV234

    Begin block 0x611B0x234
    prev=[0x5deB0x234], succ=[]
    =================================
    0x611S0x234: v611V234(0x40) = CONST 
    0x613S0x234: v613V234 = MLOAD v611V234(0x40)
    0x614S0x234: v614V234(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x636S0x234: MSTORE v613V234, v614V234(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x637S0x234: v637V234(0x4) = CONST 
    0x639S0x234: v639V234 = ADD v637V234(0x4), v613V234
    0x63cS0x234: v63cV234(0x20) = CONST 
    0x63eS0x234: v63eV234 = ADD v63cV234(0x20), v639V234
    0x641S0x234: v641V234(0x20) = SUB v63eV234, v639V234
    0x643S0x234: MSTORE v639V234, v641V234(0x20)
    0x644S0x234: v644V234(0x30) = CONST 
    0x647S0x234: MSTORE v63eV234, v644V234(0x30)
    0x648S0x234: v648V234(0x20) = CONST 
    0x64aS0x234: v64aV234 = ADD v648V234(0x20), v63eV234
    0x64cS0x234: v64cV234(0xcfa) = CONST 
    0x64fS0x234: v64fV234(0x30) = CONST 
    0x652S0x234: CODECOPY v64aV234, v64cV234(0xcfa), v64fV234(0x30)
    0x653S0x234: v653V234(0x40) = CONST 
    0x655S0x234: v655V234 = ADD v653V234(0x40), v64aV234
    0x659S0x234: v659V234(0x40) = CONST 
    0x65bS0x234: v65bV234 = MLOAD v659V234(0x40)
    0x65eS0x234: v65eV234(0x84) = SUB v655V234, v65bV234
    0x660S0x234: REVERT v65bV234, v65eV234(0x84)

    Begin block 0x661B0x234
    prev=[0x5deB0x234], succ=[0x66aB0x234]
    =================================
    0x662S0x234: v662V234(0x66a) = CONST 
    0x665S0x234: v665V234 = CALLER 
    0x666S0x234: v666V234(0xab0) = CONST 
    0x669S0x234: CALLPRIVATE v666V234(0xab0), v665V234, v662V234(0x66a)

    Begin block 0x66aB0x234
    prev=[0x661B0x234], succ=[0x23d]
    =================================
    0x66bS0x234: JUMP v236(0x23d)

    Begin block 0x23d
    prev=[0x66aB0x234], succ=[]
    =================================
    0x23e: STOP 

}

function isGovernor()() public {
    Begin block 0x23f
    prev=[], succ=[0x247, 0x24b]
    =================================
    0x240: v240 = CALLVALUE 
    0x242: v242 = ISZERO v240
    0x243: v243(0x24b) = CONST 
    0x246: JUMPI v243(0x24b), v242

    Begin block 0x247
    prev=[0x23f], succ=[]
    =================================
    0x247: v247(0x0) = CONST 
    0x24a: REVERT v247(0x0), v247(0x0)

    Begin block 0x24b
    prev=[0x23f], succ=[0x66cB0x24b]
    =================================
    0x24d: v24d(0x254) = CONST 
    0x250: v250(0x66c) = CONST 
    0x253: JUMP v250(0x66c)

    Begin block 0x66cB0x24b
    prev=[0x24b], succ=[0x9ffB0x66cB0x24b]
    =================================
    0x66dS0x24b: v66dV24b(0x0) = CONST 
    0x66fS0x24b: v66fV24b(0x676) = CONST 
    0x672S0x24b: v672V24b(0x9ff) = CONST 
    0x675S0x24b: JUMP v672V24b(0x9ff)

    Begin block 0x9ffB0x66cB0x24b
    prev=[0x66cB0x24b], succ=[0x676B0x24b]
    =================================
    0xa00S0x66cS0x24b: va00V66cV24b(0x0) = CONST 
    0xa03S0x66cS0x24b: va03V66cV24b(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x66cS0x24b: va24V66cV24b(0x0) = CONST 
    0xa26S0x66cS0x24b: va26V66cV24b(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V66cV24b(0x0), va03V66cV24b(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x66cS0x24b: va2aV66cV24b = SLOAD va26V66cV24b(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x66cS0x24b: JUMP v66fV24b(0x676)

    Begin block 0x676B0x24b
    prev=[0x9ffB0x66cB0x24b], succ=[0x254]
    =================================
    0x677S0x24b: v677V24b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68cS0x24b: v68cV24b = AND v677V24b(0xffffffffffffffffffffffffffffffffffffffff), va2aV66cV24b
    0x68dS0x24b: v68dV24b = CALLER 
    0x68eS0x24b: v68eV24b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a3S0x24b: v6a3V24b = AND v68eV24b(0xffffffffffffffffffffffffffffffffffffffff), v68dV24b
    0x6a4S0x24b: v6a4V24b = EQ v6a3V24b, v68cV24b
    0x6a8S0x24b: JUMP v24d(0x254)

    Begin block 0x254
    prev=[0x676B0x24b], succ=[]
    =================================
    0x255: v255(0x40) = CONST 
    0x257: v257 = MLOAD v255(0x40)
    0x25a: v25a = ISZERO v6a4V24b
    0x25b: v25b = ISZERO v25a
    0x25c: v25c = ISZERO v25b
    0x25d: v25d = ISZERO v25c
    0x25f: MSTORE v257, v25d
    0x260: v260(0x20) = CONST 
    0x262: v262 = ADD v260(0x20), v257
    0x266: v266(0x40) = CONST 
    0x268: v268 = MLOAD v266(0x40)
    0x26b: v26b(0x20) = SUB v262, v268
    0x26d: RETURN v268, v26b(0x20)

}

function initialize(address,address,bytes)() public {
    Begin block 0x26e
    prev=[], succ=[0x280, 0x284]
    =================================
    0x26f: v26f(0x367) = CONST 
    0x272: v272(0x4) = CONST 
    0x275: v275 = CALLDATASIZE 
    0x276: v276 = SUB v275, v272(0x4)
    0x277: v277(0x60) = CONST 
    0x27a: v27a = LT v276, v277(0x60)
    0x27b: v27b = ISZERO v27a
    0x27c: v27c(0x284) = CONST 
    0x27f: JUMPI v27c(0x284), v27b

    Begin block 0x280
    prev=[0x26e], succ=[]
    =================================
    0x280: v280(0x0) = CONST 
    0x283: REVERT v280(0x0), v280(0x0)

    Begin block 0x284
    prev=[0x26e], succ=[0x2dd, 0x2e1]
    =================================
    0x286: v286 = ADD v272(0x4), v276
    0x28a: v28a = CALLDATALOAD v272(0x4)
    0x28b: v28b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a0: v2a0 = AND v28b(0xffffffffffffffffffffffffffffffffffffffff), v28a
    0x2a2: v2a2(0x20) = CONST 
    0x2a4: v2a4(0x24) = ADD v2a2(0x20), v272(0x4)
    0x2aa: v2aa = CALLDATALOAD v2a4(0x24)
    0x2ab: v2ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c0: v2c0 = AND v2ab(0xffffffffffffffffffffffffffffffffffffffff), v2aa
    0x2c2: v2c2(0x20) = CONST 
    0x2c4: v2c4(0x44) = ADD v2c2(0x20), v2a4(0x24)
    0x2ca: v2ca = CALLDATALOAD v2c4(0x44)
    0x2cc: v2cc(0x20) = CONST 
    0x2ce: v2ce(0x64) = ADD v2cc(0x20), v2c4(0x44)
    0x2d0: v2d0(0x100000000) = CONST 
    0x2d7: v2d7 = GT v2ca, v2d0(0x100000000)
    0x2d8: v2d8 = ISZERO v2d7
    0x2d9: v2d9(0x2e1) = CONST 
    0x2dc: JUMPI v2d9(0x2e1), v2d8

    Begin block 0x2dd
    prev=[0x284], succ=[]
    =================================
    0x2dd: v2dd(0x0) = CONST 
    0x2e0: REVERT v2dd(0x0), v2dd(0x0)

    Begin block 0x2e1
    prev=[0x284], succ=[0x2ef, 0x2f3]
    =================================
    0x2e3: v2e3 = ADD v272(0x4), v2ca
    0x2e5: v2e5(0x20) = CONST 
    0x2e8: v2e8 = ADD v2e3, v2e5(0x20)
    0x2e9: v2e9 = GT v2e8, v286
    0x2ea: v2ea = ISZERO v2e9
    0x2eb: v2eb(0x2f3) = CONST 
    0x2ee: JUMPI v2eb(0x2f3), v2ea

    Begin block 0x2ef
    prev=[0x2e1], succ=[]
    =================================
    0x2ef: v2ef(0x0) = CONST 
    0x2f2: REVERT v2ef(0x0), v2ef(0x0)

    Begin block 0x2f3
    prev=[0x2e1], succ=[0x311, 0x315]
    =================================
    0x2f5: v2f5 = CALLDATALOAD v2e3
    0x2f7: v2f7(0x20) = CONST 
    0x2f9: v2f9 = ADD v2f7(0x20), v2e3
    0x2fc: v2fc(0x1) = CONST 
    0x2ff: v2ff = MUL v2f5, v2fc(0x1)
    0x301: v301 = ADD v2f9, v2ff
    0x302: v302 = GT v301, v286
    0x303: v303(0x100000000) = CONST 
    0x30a: v30a = GT v2f5, v303(0x100000000)
    0x30b: v30b = OR v30a, v302
    0x30c: v30c = ISZERO v30b
    0x30d: v30d(0x315) = CONST 
    0x310: JUMPI v30d(0x315), v30c

    Begin block 0x311
    prev=[0x2f3], succ=[]
    =================================
    0x311: v311(0x0) = CONST 
    0x314: REVERT v311(0x0), v311(0x0)

    Begin block 0x315
    prev=[0x2f3], succ=[0x6a9]
    =================================
    0x31a: v31a(0x1f) = CONST 
    0x31c: v31c = ADD v31a(0x1f), v2f5
    0x31d: v31d(0x20) = CONST 
    0x321: v321 = DIV v31c, v31d(0x20)
    0x322: v322 = MUL v321, v31d(0x20)
    0x323: v323(0x20) = CONST 
    0x325: v325 = ADD v323(0x20), v322
    0x326: v326(0x40) = CONST 
    0x328: v328 = MLOAD v326(0x40)
    0x32b: v32b = ADD v328, v325
    0x32c: v32c(0x40) = CONST 
    0x32e: MSTORE v32c(0x40), v32b
    0x336: MSTORE v328, v2f5
    0x337: v337(0x20) = CONST 
    0x339: v339 = ADD v337(0x20), v328
    0x33f: CALLDATACOPY v339, v2f9, v2f5
    0x340: v340(0x0) = CONST 
    0x344: v344 = ADD v339, v2f5
    0x345: MSTORE v344, v340(0x0)
    0x346: v346(0x1f) = CONST 
    0x348: v348(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v346(0x1f)
    0x349: v349(0x1f) = CONST 
    0x34c: v34c = ADD v2f5, v349(0x1f)
    0x34d: v34d = AND v34c, v348(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x352: v352 = ADD v339, v34d
    0x363: v363(0x6a9) = CONST 
    0x366: JUMP v363(0x6a9)

    Begin block 0x6a9
    prev=[0x315], succ=[0x66cB0x6a9]
    =================================
    0x6aa: v6aa(0x6b1) = CONST 
    0x6ad: v6ad(0x66c) = CONST 
    0x6b0: JUMP v6ad(0x66c)

    Begin block 0x66cB0x6a9
    prev=[0x6a9], succ=[0x9ffB0x66cB0x6a9]
    =================================
    0x66dS0x6a9: v66dV6a9(0x0) = CONST 
    0x66fS0x6a9: v66fV6a9(0x676) = CONST 
    0x672S0x6a9: v672V6a9(0x9ff) = CONST 
    0x675S0x6a9: JUMP v672V6a9(0x9ff)

    Begin block 0x9ffB0x66cB0x6a9
    prev=[0x66cB0x6a9], succ=[0x676B0x6a9]
    =================================
    0xa00S0x66cS0x6a9: va00V66cV6a9(0x0) = CONST 
    0xa03S0x66cS0x6a9: va03V66cV6a9(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x66cS0x6a9: va24V66cV6a9(0x0) = CONST 
    0xa26S0x66cS0x6a9: va26V66cV6a9(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V66cV6a9(0x0), va03V66cV6a9(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x66cS0x6a9: va2aV66cV6a9 = SLOAD va26V66cV6a9(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x66cS0x6a9: JUMP v66fV6a9(0x676)

    Begin block 0x676B0x6a9
    prev=[0x9ffB0x66cB0x6a9], succ=[0x6b1]
    =================================
    0x677S0x6a9: v677V6a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68cS0x6a9: v68cV6a9 = AND v677V6a9(0xffffffffffffffffffffffffffffffffffffffff), va2aV66cV6a9
    0x68dS0x6a9: v68dV6a9 = CALLER 
    0x68eS0x6a9: v68eV6a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a3S0x6a9: v6a3V6a9 = AND v68eV6a9(0xffffffffffffffffffffffffffffffffffffffff), v68dV6a9
    0x6a4S0x6a9: v6a4V6a9 = EQ v6a3V6a9, v68cV6a9
    0x6a8S0x6a9: JUMP v6aa(0x6b1)

    Begin block 0x6b1
    prev=[0x676B0x6a9], succ=[0x6b6, 0x723]
    =================================
    0x6b2: v6b2(0x723) = CONST 
    0x6b5: JUMPI v6b2(0x723), v6a4V6a9

    Begin block 0x6b6
    prev=[0x6b1], succ=[]
    =================================
    0x6b6: v6b6(0x40) = CONST 
    0x6b8: v6b8 = MLOAD v6b6(0x40)
    0x6b9: v6b9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x6db: MSTORE v6b8, v6b9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x6dc: v6dc(0x4) = CONST 
    0x6de: v6de = ADD v6dc(0x4), v6b8
    0x6e1: v6e1(0x20) = CONST 
    0x6e3: v6e3 = ADD v6e1(0x20), v6de
    0x6e6: v6e6(0x20) = SUB v6e3, v6de
    0x6e8: MSTORE v6de, v6e6(0x20)
    0x6e9: v6e9(0x1a) = CONST 
    0x6ec: MSTORE v6e3, v6e9(0x1a)
    0x6ed: v6ed(0x20) = CONST 
    0x6ef: v6ef = ADD v6ed(0x20), v6e3
    0x6f1: v6f1(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = CONST 
    0x713: MSTORE v6ef, v6f1(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x715: v715(0x20) = CONST 
    0x717: v717 = ADD v715(0x20), v6ef
    0x71b: v71b(0x40) = CONST 
    0x71d: v71d = MLOAD v71b(0x40)
    0x720: v720(0x64) = SUB v717, v71d
    0x722: REVERT v71d, v720(0x64)

    Begin block 0x723
    prev=[0x6b1], succ=[0x9a8B0x723]
    =================================
    0x724: v724(0x0) = CONST 
    0x726: v726(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x73b: v73b(0x0) = AND v726(0xffffffffffffffffffffffffffffffffffffffff), v724(0x0)
    0x73c: v73c(0x743) = CONST 
    0x73f: v73f(0x9a8) = CONST 
    0x742: JUMP v73f(0x9a8)

    Begin block 0x9a8B0x723
    prev=[0x723], succ=[0x743]
    =================================
    0x9a9S0x723: v9a9V723(0x0) = CONST 
    0x9acS0x723: v9acV723(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x9cdS0x723: v9cdV723(0x0) = CONST 
    0x9cfS0x723: v9cfV723(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v9cdV723(0x0), v9acV723(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d3S0x723: v9d3V723 = SLOAD v9cfV723(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d8S0x723: JUMP v73c(0x743)

    Begin block 0x743
    prev=[0x9a8B0x723], succ=[0x75f, 0x763]
    =================================
    0x744: v744(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x759: v759 = AND v744(0xffffffffffffffffffffffffffffffffffffffff), v9d3V723
    0x75a: v75a = EQ v759, v73b(0x0)
    0x75b: v75b(0x763) = CONST 
    0x75e: JUMPI v75b(0x763), v75a

    Begin block 0x75f
    prev=[0x743], succ=[]
    =================================
    0x75f: v75f(0x0) = CONST 
    0x762: REVERT v75f(0x0), v75f(0x0)

    Begin block 0x763
    prev=[0x743], succ=[0x7cc, 0x7cd]
    =================================
    0x764: v764(0x1) = CONST 
    0x766: v766(0x40) = CONST 
    0x768: v768 = MLOAD v766(0x40)
    0x76b: v76b(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000) = CONST 
    0x78d: MSTORE v768, v76b(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000)
    0x78f: v78f(0x1c) = CONST 
    0x791: v791 = ADD v78f(0x1c), v768
    0x794: v794(0x40) = CONST 
    0x796: v796 = MLOAD v794(0x40)
    0x799: v799(0x1c) = SUB v791, v796
    0x79b: v79b = SHA3 v796, v799(0x1c)
    0x79c: v79c(0x0) = CONST 
    0x79e: v79e = SHR v79c(0x0), v79b
    0x79f: v79f = SUB v79e, v764(0x1)
    0x7a0: v7a0(0x0) = CONST 
    0x7a2: v7a2 = SHL v7a0(0x0), v79f
    0x7a3: v7a3(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x7c4: v7c4(0x0) = CONST 
    0x7c6: v7c6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v7c4(0x0), v7a3(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x7c7: v7c7 = EQ v7c6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v7a2
    0x7c8: v7c8(0x7cd) = CONST 
    0x7cb: JUMPI v7c8(0x7cd), v7c7

    Begin block 0x7cc
    prev=[0x763], succ=[]
    =================================
    0x7cc: THROW 

    Begin block 0x7cd
    prev=[0x763], succ=[0x7d6]
    =================================
    0x7ce: v7ce(0x7d6) = CONST 
    0x7d2: v7d2(0xbc0) = CONST 
    0x7d5: CALLPRIVATE v7d2(0xbc0), v2a0, v7ce(0x7d6)

    Begin block 0x7d6
    prev=[0x7cd], succ=[0x7e1, 0x8a2]
    =================================
    0x7d7: v7d7(0x0) = CONST 
    0x7da: v7da = MLOAD v328
    0x7db: v7db = GT v7da, v7d7(0x0)
    0x7dc: v7dc = ISZERO v7db
    0x7dd: v7dd(0x8a2) = CONST 
    0x7e0: JUMPI v7dd(0x8a2), v7dc

    Begin block 0x7e1
    prev=[0x7d6], succ=[0x80a]
    =================================
    0x7e1: v7e1(0x0) = CONST 
    0x7e4: v7e4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7f9: v7f9 = AND v7e4(0xffffffffffffffffffffffffffffffffffffffff), v2a0
    0x7fb: v7fb(0x40) = CONST 
    0x7fd: v7fd = MLOAD v7fb(0x40)
    0x801: v801 = MLOAD v328
    0x803: v803(0x20) = CONST 
    0x805: v805 = ADD v803(0x20), v328

    Begin block 0x80a
    prev=[0x7e1, 0x813], succ=[0x82d, 0x813]
    =================================
    0x80a_0x2: v80a_2 = PHI v801, v826
    0x80b: v80b(0x20) = CONST 
    0x80e: v80e = LT v80a_2, v80b(0x20)
    0x80f: v80f(0x82d) = CONST 
    0x812: JUMPI v80f(0x82d), v80e

    Begin block 0x82d
    prev=[0x80a], succ=[0x86c, 0x88d]
    =================================
    0x82d_0x0: v82d_0 = PHI v805, v820
    0x82d_0x1: v82d_1 = PHI v7fd, v81a
    0x82d_0x2: v82d_2 = PHI v801, v826
    0x82e: v82e(0x1) = CONST 
    0x831: v831(0x20) = CONST 
    0x833: v833 = SUB v831(0x20), v82d_2
    0x834: v834(0x100) = CONST 
    0x837: v837 = EXP v834(0x100), v833
    0x838: v838 = SUB v837, v82e(0x1)
    0x83a: v83a = NOT v838
    0x83c: v83c = MLOAD v82d_0
    0x83d: v83d = AND v83c, v83a
    0x840: v840 = MLOAD v82d_1
    0x841: v841 = AND v840, v838
    0x844: v844 = OR v83d, v841
    0x846: MSTORE v82d_1, v844
    0x84f: v84f = ADD v801, v7fd
    0x853: v853(0x0) = CONST 
    0x855: v855(0x40) = CONST 
    0x857: v857 = MLOAD v855(0x40)
    0x85a: v85a = SUB v84f, v857
    0x85d: v85d = GAS 
    0x85e: v85e = DELEGATECALL v85d, v7f9, v857, v85a, v857, v853(0x0)
    0x862: v862 = RETURNDATASIZE 
    0x864: v864(0x0) = CONST 
    0x867: v867 = EQ v862, v864(0x0)
    0x868: v868(0x88d) = CONST 
    0x86b: JUMPI v868(0x88d), v867

    Begin block 0x86c
    prev=[0x82d], succ=[0x892]
    =================================
    0x86c: v86c(0x40) = CONST 
    0x86e: v86e = MLOAD v86c(0x40)
    0x871: v871(0x1f) = CONST 
    0x873: v873(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v871(0x1f)
    0x874: v874(0x3f) = CONST 
    0x876: v876 = RETURNDATASIZE 
    0x877: v877 = ADD v876, v874(0x3f)
    0x878: v878 = AND v877, v873(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x87a: v87a = ADD v86e, v878
    0x87b: v87b(0x40) = CONST 
    0x87d: MSTORE v87b(0x40), v87a
    0x87e: v87e = RETURNDATASIZE 
    0x880: MSTORE v86e, v87e
    0x881: v881 = RETURNDATASIZE 
    0x882: v882(0x0) = CONST 
    0x884: v884(0x20) = CONST 
    0x887: v887 = ADD v86e, v884(0x20)
    0x888: RETURNDATACOPY v887, v882(0x0), v881
    0x889: v889(0x892) = CONST 
    0x88c: JUMP v889(0x892)

    Begin block 0x892
    prev=[0x86c, 0x88d], succ=[0x89c, 0x8a0]
    =================================
    0x898: v898(0x8a0) = CONST 
    0x89b: JUMPI v898(0x8a0), v85e

    Begin block 0x89c
    prev=[0x892], succ=[]
    =================================
    0x89c: v89c(0x0) = CONST 
    0x89f: REVERT v89c(0x0), v89c(0x0)

    Begin block 0x8a0
    prev=[0x892], succ=[0x8a2]
    =================================

    Begin block 0x8a2
    prev=[0x7d6, 0x8a0], succ=[0x8ab]
    =================================
    0x8a3: v8a3(0x8ab) = CONST 
    0x8a7: v8a7(0xab0) = CONST 
    0x8aa: CALLPRIVATE v8a7(0xab0), v2c0, v8a3(0x8ab)

    Begin block 0x8ab
    prev=[0x8a2], succ=[0x367]
    =================================
    0x8af: JUMP v26f(0x367)

    Begin block 0x367
    prev=[0x8ab], succ=[]
    =================================
    0x368: STOP 

    Begin block 0x88d
    prev=[0x82d], succ=[0x892]
    =================================
    0x88e: v88e(0x60) = CONST 

    Begin block 0x813
    prev=[0x80a], succ=[0x80a]
    =================================
    0x813_0x0: v813_0 = PHI v805, v820
    0x813_0x1: v813_1 = PHI v7fd, v81a
    0x813_0x2: v813_2 = PHI v801, v826
    0x814: v814 = MLOAD v813_0
    0x816: MSTORE v813_1, v814
    0x817: v817(0x20) = CONST 
    0x81a: v81a = ADD v813_1, v817(0x20)
    0x81d: v81d(0x20) = CONST 
    0x820: v820 = ADD v813_0, v81d(0x20)
    0x823: v823(0x20) = CONST 
    0x826: v826 = SUB v813_2, v823(0x20)
    0x829: v829(0x80a) = CONST 
    0x82c: JUMP v829(0x80a)

}

function transferGovernance(address)() public {
    Begin block 0x369
    prev=[], succ=[0x371, 0x375]
    =================================
    0x36a: v36a = CALLVALUE 
    0x36c: v36c = ISZERO v36a
    0x36d: v36d(0x375) = CONST 
    0x370: JUMPI v36d(0x375), v36c

    Begin block 0x371
    prev=[0x369], succ=[]
    =================================
    0x371: v371(0x0) = CONST 
    0x374: REVERT v371(0x0), v371(0x0)

    Begin block 0x375
    prev=[0x369], succ=[0x388, 0x38c]
    =================================
    0x377: v377(0x3b8) = CONST 
    0x37a: v37a(0x4) = CONST 
    0x37d: v37d = CALLDATASIZE 
    0x37e: v37e = SUB v37d, v37a(0x4)
    0x37f: v37f(0x20) = CONST 
    0x382: v382 = LT v37e, v37f(0x20)
    0x383: v383 = ISZERO v382
    0x384: v384(0x38c) = CONST 
    0x387: JUMPI v384(0x38c), v383

    Begin block 0x388
    prev=[0x375], succ=[]
    =================================
    0x388: v388(0x0) = CONST 
    0x38b: REVERT v388(0x0), v388(0x0)

    Begin block 0x38c
    prev=[0x375], succ=[0x8b0]
    =================================
    0x38e: v38e = ADD v37a(0x4), v37e
    0x392: v392 = CALLDATALOAD v37a(0x4)
    0x393: v393(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a8: v3a8 = AND v393(0xffffffffffffffffffffffffffffffffffffffff), v392
    0x3aa: v3aa(0x20) = CONST 
    0x3ac: v3ac(0x24) = ADD v3aa(0x20), v37a(0x4)
    0x3b4: v3b4(0x8b0) = CONST 
    0x3b7: JUMP v3b4(0x8b0)

    Begin block 0x8b0
    prev=[0x38c], succ=[0x66cB0x8b0]
    =================================
    0x8b1: v8b1(0x8b8) = CONST 
    0x8b4: v8b4(0x66c) = CONST 
    0x8b7: JUMP v8b4(0x66c)

    Begin block 0x66cB0x8b0
    prev=[0x8b0], succ=[0x9ffB0x66cB0x8b0]
    =================================
    0x66dS0x8b0: v66dV8b0(0x0) = CONST 
    0x66fS0x8b0: v66fV8b0(0x676) = CONST 
    0x672S0x8b0: v672V8b0(0x9ff) = CONST 
    0x675S0x8b0: JUMP v672V8b0(0x9ff)

    Begin block 0x9ffB0x66cB0x8b0
    prev=[0x66cB0x8b0], succ=[0x676B0x8b0]
    =================================
    0xa00S0x66cS0x8b0: va00V66cV8b0(0x0) = CONST 
    0xa03S0x66cS0x8b0: va03V66cV8b0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x66cS0x8b0: va24V66cV8b0(0x0) = CONST 
    0xa26S0x66cS0x8b0: va26V66cV8b0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V66cV8b0(0x0), va03V66cV8b0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x66cS0x8b0: va2aV66cV8b0 = SLOAD va26V66cV8b0(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x66cS0x8b0: JUMP v66fV8b0(0x676)

    Begin block 0x676B0x8b0
    prev=[0x9ffB0x66cB0x8b0], succ=[0x8b8]
    =================================
    0x677S0x8b0: v677V8b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68cS0x8b0: v68cV8b0 = AND v677V8b0(0xffffffffffffffffffffffffffffffffffffffff), va2aV66cV8b0
    0x68dS0x8b0: v68dV8b0 = CALLER 
    0x68eS0x8b0: v68eV8b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a3S0x8b0: v6a3V8b0 = AND v68eV8b0(0xffffffffffffffffffffffffffffffffffffffff), v68dV8b0
    0x6a4S0x8b0: v6a4V8b0 = EQ v6a3V8b0, v68cV8b0
    0x6a8S0x8b0: JUMP v8b1(0x8b8)

    Begin block 0x8b8
    prev=[0x676B0x8b0], succ=[0x8bd, 0x92a]
    =================================
    0x8b9: v8b9(0x92a) = CONST 
    0x8bc: JUMPI v8b9(0x92a), v6a4V8b0

    Begin block 0x8bd
    prev=[0x8b8], succ=[]
    =================================
    0x8bd: v8bd(0x40) = CONST 
    0x8bf: v8bf = MLOAD v8bd(0x40)
    0x8c0: v8c0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x8e2: MSTORE v8bf, v8c0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8e3: v8e3(0x4) = CONST 
    0x8e5: v8e5 = ADD v8e3(0x4), v8bf
    0x8e8: v8e8(0x20) = CONST 
    0x8ea: v8ea = ADD v8e8(0x20), v8e5
    0x8ed: v8ed(0x20) = SUB v8ea, v8e5
    0x8ef: MSTORE v8e5, v8ed(0x20)
    0x8f0: v8f0(0x1a) = CONST 
    0x8f3: MSTORE v8ea, v8f0(0x1a)
    0x8f4: v8f4(0x20) = CONST 
    0x8f6: v8f6 = ADD v8f4(0x20), v8ea
    0x8f8: v8f8(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = CONST 
    0x91a: MSTORE v8f6, v8f8(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x91c: v91c(0x20) = CONST 
    0x91e: v91e = ADD v91c(0x20), v8f6
    0x922: v922(0x40) = CONST 
    0x924: v924 = MLOAD v922(0x40)
    0x927: v927(0x64) = SUB v91e, v924
    0x929: REVERT v924, v927(0x64)

    Begin block 0x92a
    prev=[0x8b8], succ=[0xc4d]
    =================================
    0x92b: v92b(0x933) = CONST 
    0x92f: v92f(0xc4d) = CONST 
    0x932: JUMP v92f(0xc4d)

    Begin block 0xc4d
    prev=[0x92a], succ=[0x933]
    =================================
    0xc4e: vc4e(0x0) = CONST 
    0xc50: vc50(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = CONST 
    0xc71: vc71(0x0) = CONST 
    0xc73: vc73(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = SHL vc71(0x0), vc50(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db)
    0xc78: SSTORE vc73(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db), v3a8
    0xc7b: JUMP v92b(0x933)

    Begin block 0x933
    prev=[0xc4d], succ=[0x9ffB0x933]
    =================================
    0x935: v935(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x94a: v94a = AND v935(0xffffffffffffffffffffffffffffffffffffffff), v3a8
    0x94b: v94b(0x952) = CONST 
    0x94e: v94e(0x9ff) = CONST 
    0x951: JUMP v94e(0x9ff)

    Begin block 0x9ffB0x933
    prev=[0x933], succ=[0x952]
    =================================
    0xa00S0x933: va00V933(0x0) = CONST 
    0xa03S0x933: va03V933(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x933: va24V933(0x0) = CONST 
    0xa26S0x933: va26V933(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V933(0x0), va03V933(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x933: va2aV933 = SLOAD va26V933(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x933: JUMP v94b(0x952)

    Begin block 0x952
    prev=[0x9ffB0x933], succ=[0x3b8]
    =================================
    0x953: v953(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x968: v968 = AND v953(0xffffffffffffffffffffffffffffffffffffffff), va2aV933
    0x969: v969(0xa39cc5eb22d0f34d8beaefee8a3f17cc229c1a1d1ef87a5ad47313487b1c4f0d) = CONST 
    0x98a: v98a(0x40) = CONST 
    0x98c: v98c = MLOAD v98a(0x40)
    0x98d: v98d(0x40) = CONST 
    0x98f: v98f = MLOAD v98d(0x40)
    0x992: v992(0x0) = SUB v98c, v98f
    0x994: LOG3 v98f, v992(0x0), v969(0xa39cc5eb22d0f34d8beaefee8a3f17cc229c1a1d1ef87a5ad47313487b1c4f0d), v968, v94a
    0x996: JUMP v377(0x3b8)

    Begin block 0x3b8
    prev=[0x952], succ=[]
    =================================
    0x3b9: STOP 

}

function admin()() public {
    Begin block 0x3ba
    prev=[], succ=[0x3c2, 0x3c6]
    =================================
    0x3bb: v3bb = CALLVALUE 
    0x3bd: v3bd = ISZERO v3bb
    0x3be: v3be(0x3c6) = CONST 
    0x3c1: JUMPI v3be(0x3c6), v3bd

    Begin block 0x3c2
    prev=[0x3ba], succ=[]
    =================================
    0x3c2: v3c2(0x0) = CONST 
    0x3c5: REVERT v3c2(0x0), v3c2(0x0)

    Begin block 0x3c6
    prev=[0x3ba], succ=[0x997B0x3c6]
    =================================
    0x3c8: v3c8(0x3cf) = CONST 
    0x3cb: v3cb(0x997) = CONST 
    0x3ce: JUMP v3cb(0x997)

    Begin block 0x997B0x3c6
    prev=[0x3c6], succ=[0x9ffB0x997B0x3c6]
    =================================
    0x998S0x3c6: v998V3c6(0x0) = CONST 
    0x99aS0x3c6: v99aV3c6(0x9a1) = CONST 
    0x99dS0x3c6: v99dV3c6(0x9ff) = CONST 
    0x9a0S0x3c6: JUMP v99dV3c6(0x9ff)

    Begin block 0x9ffB0x997B0x3c6
    prev=[0x997B0x3c6], succ=[0x9a1B0x3c6]
    =================================
    0xa00S0x997S0x3c6: va00V997V3c6(0x0) = CONST 
    0xa03S0x997S0x3c6: va03V997V3c6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x997S0x3c6: va24V997V3c6(0x0) = CONST 
    0xa26S0x997S0x3c6: va26V997V3c6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V997V3c6(0x0), va03V997V3c6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x997S0x3c6: va2aV997V3c6 = SLOAD va26V997V3c6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x997S0x3c6: JUMP v99aV3c6(0x9a1)

    Begin block 0x9a1B0x3c6
    prev=[0x9ffB0x997B0x3c6], succ=[0x3cf]
    =================================
    0x9a5S0x3c6: JUMP v3c8(0x3cf)

    Begin block 0x3cf
    prev=[0x9a1B0x3c6], succ=[]
    =================================
    0x3d0: v3d0(0x40) = CONST 
    0x3d2: v3d2 = MLOAD v3d0(0x40)
    0x3d5: v3d5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ea: v3ea = AND v3d5(0xffffffffffffffffffffffffffffffffffffffff), va2aV997V3c6
    0x3eb: v3eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x400: v400 = AND v3eb(0xffffffffffffffffffffffffffffffffffffffff), v3ea
    0x402: MSTORE v3d2, v400
    0x403: v403(0x20) = CONST 
    0x405: v405 = ADD v403(0x20), v3d2
    0x409: v409(0x40) = CONST 
    0x40b: v40b = MLOAD v409(0x40)
    0x40e: v40e(0x20) = SUB v405, v40b
    0x410: RETURN v40b, v40e(0x20)

}

function fallback()() public {
    Begin block 0x86
    prev=[], succ=[0x411]
    =================================
    0x87: v87(0x8e) = CONST 
    0x8a: v8a(0x411) = CONST 
    0x8d: JUMP v8a(0x411)

    Begin block 0x411
    prev=[0x86], succ=[0x9a6B0x411]
    =================================
    0x412: v412(0x419) = CONST 
    0x415: v415(0x9a6) = CONST 
    0x418: JUMP v415(0x9a6), v412(0x419)

    Begin block 0x9a6B0x411
    prev=[0x411], succ=[0x419]
    =================================
    0x9a7S0x411: JUMP v412(0x419)

    Begin block 0x419
    prev=[0x9a6B0x411], succ=[0x9a8B0x419]
    =================================
    0x41a: v41a(0x429) = CONST 
    0x41d: v41d(0x424) = CONST 
    0x420: v420(0x9a8) = CONST 
    0x423: JUMP v420(0x9a8)

    Begin block 0x9a8B0x419
    prev=[0x419], succ=[0x424]
    =================================
    0x9a9S0x419: v9a9V419(0x0) = CONST 
    0x9acS0x419: v9acV419(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x9cdS0x419: v9cdV419(0x0) = CONST 
    0x9cfS0x419: v9cfV419(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v9cdV419(0x0), v9acV419(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d3S0x419: v9d3V419 = SLOAD v9cfV419(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9d8S0x419: JUMP v41d(0x424)

    Begin block 0x424
    prev=[0x9a8B0x419], succ=[0x9d9]
    =================================
    0x425: v425(0x9d9) = CONST 
    0x428: JUMP v425(0x9d9)

    Begin block 0x9d9
    prev=[0x424], succ=[0x9f6, 0x9fa]
    =================================
    0x9da: v9da = CALLDATASIZE 
    0x9db: v9db(0x0) = CONST 
    0x9de: CALLDATACOPY v9db(0x0), v9db(0x0), v9da
    0x9df: v9df(0x0) = CONST 
    0x9e2: v9e2 = CALLDATASIZE 
    0x9e3: v9e3(0x0) = CONST 
    0x9e6: v9e6 = GAS 
    0x9e7: v9e7 = DELEGATECALL v9e6, v9d3V419, v9e3(0x0), v9e2, v9df(0x0), v9df(0x0)
    0x9e8: v9e8 = RETURNDATASIZE 
    0x9e9: v9e9(0x0) = CONST 
    0x9ec: RETURNDATACOPY v9e9(0x0), v9e9(0x0), v9e8
    0x9ee: v9ee(0x0) = CONST 
    0x9f1: v9f1 = EQ v9e7, v9ee(0x0)
    0x9f2: v9f2(0x9fa) = CONST 
    0x9f5: JUMPI v9f2(0x9fa), v9f1

    Begin block 0x9f6
    prev=[0x9d9], succ=[]
    =================================
    0x9f6: v9f6 = RETURNDATASIZE 
    0x9f7: v9f7(0x0) = CONST 
    0x9f9: RETURN v9f7(0x0), v9f6

    Begin block 0x9fa
    prev=[0x9d9], succ=[]
    =================================
    0x9fb: v9fb = RETURNDATASIZE 
    0x9fc: v9fc(0x0) = CONST 
    0x9fe: REVERT v9fc(0x0), v9fb

}

function governor()() public {
    Begin block 0x90
    prev=[], succ=[0x98, 0x9c]
    =================================
    0x91: v91 = CALLVALUE 
    0x93: v93 = ISZERO v91
    0x94: v94(0x9c) = CONST 
    0x97: JUMPI v94(0x9c), v93

    Begin block 0x98
    prev=[0x90], succ=[]
    =================================
    0x98: v98(0x0) = CONST 
    0x9b: REVERT v98(0x0), v98(0x0)

    Begin block 0x9c
    prev=[0x90], succ=[0x42bB0x9c]
    =================================
    0x9e: v9e(0xa5) = CONST 
    0xa1: va1(0x42b) = CONST 
    0xa4: JUMP va1(0x42b)

    Begin block 0x42bB0x9c
    prev=[0x9c], succ=[0x9ffB0x42bB0x9c]
    =================================
    0x42cS0x9c: v42cV9c(0x0) = CONST 
    0x42eS0x9c: v42eV9c(0x435) = CONST 
    0x431S0x9c: v431V9c(0x9ff) = CONST 
    0x434S0x9c: JUMP v431V9c(0x9ff)

    Begin block 0x9ffB0x42bB0x9c
    prev=[0x42bB0x9c], succ=[0x435B0x9c]
    =================================
    0xa00S0x42bS0x9c: va00V42bV9c(0x0) = CONST 
    0xa03S0x42bS0x9c: va03V42bV9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x42bS0x9c: va24V42bV9c(0x0) = CONST 
    0xa26S0x42bS0x9c: va26V42bV9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V42bV9c(0x0), va03V42bV9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x42bS0x9c: va2aV42bV9c = SLOAD va26V42bV9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x42bS0x9c: JUMP v42eV9c(0x435)

    Begin block 0x435B0x9c
    prev=[0x9ffB0x42bB0x9c], succ=[0xa5]
    =================================
    0x439S0x9c: JUMP v9e(0xa5)

    Begin block 0xa5
    prev=[0x435B0x9c], succ=[]
    =================================
    0xa6: va6(0x40) = CONST 
    0xa8: va8 = MLOAD va6(0x40)
    0xab: vab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc0: vc0 = AND vab(0xffffffffffffffffffffffffffffffffffffffff), va2aV42bV9c
    0xc1: vc1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd6: vd6 = AND vc1(0xffffffffffffffffffffffffffffffffffffffff), vc0
    0xd8: MSTORE va8, vd6
    0xd9: vd9(0x20) = CONST 
    0xdb: vdb = ADD vd9(0x20), va8
    0xdf: vdf(0x40) = CONST 
    0xe1: ve1 = MLOAD vdf(0x40)
    0xe4: ve4(0x20) = SUB vdb, ve1
    0xe6: RETURN ve1, ve4(0x20)

}

function 0xab0(0xab0arg0x0, 0xab0arg0x1) private {
    Begin block 0xab0
    prev=[], succ=[0xae6, 0xb53]
    =================================
    0xab1: vab1(0x0) = CONST 
    0xab3: vab3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xac8: vac8(0x0) = AND vab3(0xffffffffffffffffffffffffffffffffffffffff), vab1(0x0)
    0xaca: vaca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xadf: vadf = AND vaca(0xffffffffffffffffffffffffffffffffffffffff), vab0arg0
    0xae0: vae0 = EQ vadf, vac8(0x0)
    0xae1: vae1 = ISZERO vae0
    0xae2: vae2(0xb53) = CONST 
    0xae5: JUMPI vae2(0xb53), vae1

    Begin block 0xae6
    prev=[0xab0], succ=[]
    =================================
    0xae6: vae6(0x40) = CONST 
    0xae8: vae8 = MLOAD vae6(0x40)
    0xae9: vae9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xb0b: MSTORE vae8, vae9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb0c: vb0c(0x4) = CONST 
    0xb0e: vb0e = ADD vb0c(0x4), vae8
    0xb11: vb11(0x20) = CONST 
    0xb13: vb13 = ADD vb11(0x20), vb0e
    0xb16: vb16(0x20) = SUB vb13, vb0e
    0xb18: MSTORE vb0e, vb16(0x20)
    0xb19: vb19(0x1a) = CONST 
    0xb1c: MSTORE vb13, vb19(0x1a)
    0xb1d: vb1d(0x20) = CONST 
    0xb1f: vb1f = ADD vb1d(0x20), vb13
    0xb21: vb21(0x4e657720476f7665726e6f722069732061646472657373283029000000000000) = CONST 
    0xb43: MSTORE vb1f, vb21(0x4e657720476f7665726e6f722069732061646472657373283029000000000000)
    0xb45: vb45(0x20) = CONST 
    0xb47: vb47 = ADD vb45(0x20), vb1f
    0xb4b: vb4b(0x40) = CONST 
    0xb4d: vb4d = MLOAD vb4b(0x40)
    0xb50: vb50(0x64) = SUB vb47, vb4d
    0xb52: REVERT vb4d, vb50(0x64)

    Begin block 0xb53
    prev=[0xab0], succ=[0x9ffB0xb53]
    =================================
    0xb55: vb55(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb6a: vb6a = AND vb55(0xffffffffffffffffffffffffffffffffffffffff), vab0arg0
    0xb6b: vb6b(0xb72) = CONST 
    0xb6e: vb6e(0x9ff) = CONST 
    0xb71: JUMP vb6e(0x9ff)

    Begin block 0x9ffB0xb53
    prev=[0xb53], succ=[0xb72]
    =================================
    0xa00S0xb53: va00Vb53(0x0) = CONST 
    0xa03S0xb53: va03Vb53(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0xb53: va24Vb53(0x0) = CONST 
    0xa26S0xb53: va26Vb53(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24Vb53(0x0), va03Vb53(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0xb53: va2aVb53 = SLOAD va26Vb53(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0xb53: JUMP vb6b(0xb72)

    Begin block 0xb72
    prev=[0x9ffB0xb53], succ=[0xc7c]
    =================================
    0xb73: vb73(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb88: vb88 = AND vb73(0xffffffffffffffffffffffffffffffffffffffff), va2aVb53
    0xb89: vb89(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0xbaa: vbaa(0x40) = CONST 
    0xbac: vbac = MLOAD vbaa(0x40)
    0xbad: vbad(0x40) = CONST 
    0xbaf: vbaf = MLOAD vbad(0x40)
    0xbb2: vbb2(0x0) = SUB vbac, vbaf
    0xbb4: LOG3 vbaf, vbb2(0x0), vb89(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), vb88, vb6a
    0xbb5: vbb5(0xbbd) = CONST 
    0xbb9: vbb9(0xc7c) = CONST 
    0xbbc: JUMP vbb9(0xc7c)

    Begin block 0xc7c
    prev=[0xb72], succ=[0xbbd]
    =================================
    0xc7d: vc7d(0x0) = CONST 
    0xc7f: vc7f(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xca0: vca0(0x0) = CONST 
    0xca2: vca2(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL vca0(0x0), vc7f(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xca7: SSTORE vca2(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), vab0arg0
    0xcaa: JUMP vbb5(0xbbd)

    Begin block 0xbbd
    prev=[0xc7c], succ=[]
    =================================
    0xbbf: RETURNPRIVATE vab0arg1

}

function 0xbc0(0xbc0arg0x0, 0xbc0arg0x1) private {
    Begin block 0xbc0
    prev=[], succ=[0xcab]
    =================================
    0xbc1: vbc1(0xbc9) = CONST 
    0xbc5: vbc5(0xcab) = CONST 
    0xbc8: JUMP vbc5(0xcab)

    Begin block 0xcab
    prev=[0xbc0], succ=[0xbc9]
    =================================
    0xcac: vcac(0x0) = CONST 
    0xcb0: vcb0 = EXTCODESIZE vbc0arg0
    0xcb3: vcb3(0x0) = CONST 
    0xcb6: vcb6 = GT vcb0, vcb3(0x0)
    0xcbd: JUMP vbc1(0xbc9)

    Begin block 0xbc9
    prev=[0xcab], succ=[0xbce, 0xc1e]
    =================================
    0xbca: vbca(0xc1e) = CONST 
    0xbcd: JUMPI vbca(0xc1e), vcb6

    Begin block 0xbce
    prev=[0xbc9], succ=[]
    =================================
    0xbce: vbce(0x40) = CONST 
    0xbd0: vbd0 = MLOAD vbce(0x40)
    0xbd1: vbd1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xbf3: MSTORE vbd0, vbd1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xbf4: vbf4(0x4) = CONST 
    0xbf6: vbf6 = ADD vbf4(0x4), vbd0
    0xbf9: vbf9(0x20) = CONST 
    0xbfb: vbfb = ADD vbf9(0x20), vbf6
    0xbfe: vbfe(0x20) = SUB vbfb, vbf6
    0xc00: MSTORE vbf6, vbfe(0x20)
    0xc01: vc01(0x3b) = CONST 
    0xc04: MSTORE vbfb, vc01(0x3b)
    0xc05: vc05(0x20) = CONST 
    0xc07: vc07 = ADD vc05(0x20), vbfb
    0xc09: vc09(0xcbf) = CONST 
    0xc0c: vc0c(0x3b) = CONST 
    0xc0f: CODECOPY vc07, vc09(0xcbf), vc0c(0x3b)
    0xc10: vc10(0x40) = CONST 
    0xc12: vc12 = ADD vc10(0x40), vc07
    0xc16: vc16(0x40) = CONST 
    0xc18: vc18 = MLOAD vc16(0x40)
    0xc1b: vc1b(0x84) = SUB vc12, vc18
    0xc1d: REVERT vc18, vc1b(0x84)

    Begin block 0xc1e
    prev=[0xbc9], succ=[]
    =================================
    0xc1f: vc1f(0x0) = CONST 
    0xc21: vc21(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0xc42: vc42(0x0) = CONST 
    0xc44: vc44(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL vc42(0x0), vc21(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0xc49: SSTORE vc44(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), vbc0arg0
    0xc4c: RETURNPRIVATE vbc0arg1

}

function upgradeTo(address)() public {
    Begin block 0xe7
    prev=[], succ=[0xef, 0xf3]
    =================================
    0xe8: ve8 = CALLVALUE 
    0xea: vea = ISZERO ve8
    0xeb: veb(0xf3) = CONST 
    0xee: JUMPI veb(0xf3), vea

    Begin block 0xef
    prev=[0xe7], succ=[]
    =================================
    0xef: vef(0x0) = CONST 
    0xf2: REVERT vef(0x0), vef(0x0)

    Begin block 0xf3
    prev=[0xe7], succ=[0x106, 0x10a]
    =================================
    0xf5: vf5(0x136) = CONST 
    0xf8: vf8(0x4) = CONST 
    0xfb: vfb = CALLDATASIZE 
    0xfc: vfc = SUB vfb, vf8(0x4)
    0xfd: vfd(0x20) = CONST 
    0x100: v100 = LT vfc, vfd(0x20)
    0x101: v101 = ISZERO v100
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xf3], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xf3], succ=[0x43a]
    =================================
    0x10c: v10c = ADD vf8(0x4), vfc
    0x110: v110 = CALLDATALOAD vf8(0x4)
    0x111: v111(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x126: v126 = AND v111(0xffffffffffffffffffffffffffffffffffffffff), v110
    0x128: v128(0x20) = CONST 
    0x12a: v12a(0x24) = ADD v128(0x20), vf8(0x4)
    0x132: v132(0x43a) = CONST 
    0x135: JUMP v132(0x43a)

    Begin block 0x43a
    prev=[0x10a], succ=[0x66cB0x43a]
    =================================
    0x43b: v43b(0x442) = CONST 
    0x43e: v43e(0x66c) = CONST 
    0x441: JUMP v43e(0x66c)

    Begin block 0x66cB0x43a
    prev=[0x43a], succ=[0x9ffB0x66cB0x43a]
    =================================
    0x66dS0x43a: v66dV43a(0x0) = CONST 
    0x66fS0x43a: v66fV43a(0x676) = CONST 
    0x672S0x43a: v672V43a(0x9ff) = CONST 
    0x675S0x43a: JUMP v672V43a(0x9ff)

    Begin block 0x9ffB0x66cB0x43a
    prev=[0x66cB0x43a], succ=[0x676B0x43a]
    =================================
    0xa00S0x66cS0x43a: va00V66cV43a(0x0) = CONST 
    0xa03S0x66cS0x43a: va03V66cV43a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0xa24S0x66cS0x43a: va24V66cV43a(0x0) = CONST 
    0xa26S0x66cS0x43a: va26V66cV43a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL va24V66cV43a(0x0), va03V66cV43a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2aS0x66cS0x43a: va2aV66cV43a = SLOAD va26V66cV43a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0xa2fS0x66cS0x43a: JUMP v66fV43a(0x676)

    Begin block 0x676B0x43a
    prev=[0x9ffB0x66cB0x43a], succ=[0x442]
    =================================
    0x677S0x43a: v677V43a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68cS0x43a: v68cV43a = AND v677V43a(0xffffffffffffffffffffffffffffffffffffffff), va2aV66cV43a
    0x68dS0x43a: v68dV43a = CALLER 
    0x68eS0x43a: v68eV43a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a3S0x43a: v6a3V43a = AND v68eV43a(0xffffffffffffffffffffffffffffffffffffffff), v68dV43a
    0x6a4S0x43a: v6a4V43a = EQ v6a3V43a, v68cV43a
    0x6a8S0x43a: JUMP v43b(0x442)

    Begin block 0x442
    prev=[0x676B0x43a], succ=[0x447, 0x4b4]
    =================================
    0x443: v443(0x4b4) = CONST 
    0x446: JUMPI v443(0x4b4), v6a4V43a

    Begin block 0x447
    prev=[0x442], succ=[]
    =================================
    0x447: v447(0x40) = CONST 
    0x449: v449 = MLOAD v447(0x40)
    0x44a: v44a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x46c: MSTORE v449, v44a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x46d: v46d(0x4) = CONST 
    0x46f: v46f = ADD v46d(0x4), v449
    0x472: v472(0x20) = CONST 
    0x474: v474 = ADD v472(0x20), v46f
    0x477: v477(0x20) = SUB v474, v46f
    0x479: MSTORE v46f, v477(0x20)
    0x47a: v47a(0x1a) = CONST 
    0x47d: MSTORE v474, v47a(0x1a)
    0x47e: v47e(0x20) = CONST 
    0x480: v480 = ADD v47e(0x20), v474
    0x482: v482(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = CONST 
    0x4a4: MSTORE v480, v482(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x4a6: v4a6(0x20) = CONST 
    0x4a8: v4a8 = ADD v4a6(0x20), v480
    0x4ac: v4ac(0x40) = CONST 
    0x4ae: v4ae = MLOAD v4ac(0x40)
    0x4b1: v4b1(0x64) = SUB v4a8, v4ae
    0x4b3: REVERT v4ae, v4b1(0x64)

    Begin block 0x4b4
    prev=[0x442], succ=[0xa30B0x4b4]
    =================================
    0x4b5: v4b5(0x4bd) = CONST 
    0x4b9: v4b9(0xa30) = CONST 
    0x4bc: JUMP v4b9(0xa30), v126, v4b5(0x4bd)

    Begin block 0xa30B0x4b4
    prev=[0x4b4], succ=[0xa39B0x4b4]
    =================================
    0xa31S0x4b4: va31V4b4(0xa39) = CONST 
    0xa35S0x4b4: va35V4b4(0xbc0) = CONST 
    0xa38S0x4b4: CALLPRIVATE va35V4b4(0xbc0), v126, va31V4b4(0xa39)

    Begin block 0xa39B0x4b4
    prev=[0xa30B0x4b4], succ=[0x4bd]
    =================================
    0xa3bS0x4b4: va3bV4b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa50S0x4b4: va50V4b4 = AND va3bV4b4(0xffffffffffffffffffffffffffffffffffffffff), v126
    0xa51S0x4b4: va51V4b4(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0xa72S0x4b4: va72V4b4(0x40) = CONST 
    0xa74S0x4b4: va74V4b4 = MLOAD va72V4b4(0x40)
    0xa75S0x4b4: va75V4b4(0x40) = CONST 
    0xa77S0x4b4: va77V4b4 = MLOAD va75V4b4(0x40)
    0xa7aS0x4b4: va7aV4b4(0x0) = SUB va74V4b4, va77V4b4
    0xa7cS0x4b4: LOG2 va77V4b4, va7aV4b4(0x0), va51V4b4(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), va50V4b4
    0xa7eS0x4b4: JUMP v4b5(0x4bd)

    Begin block 0x4bd
    prev=[0xa39B0x4b4], succ=[0x136]
    =================================
    0x4bf: JUMP vf5(0x136)

    Begin block 0x136
    prev=[0x4bd], succ=[]
    =================================
    0x137: STOP 

}

