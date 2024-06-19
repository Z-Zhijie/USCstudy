function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x69]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x69) = CONST 
    0xc: JUMPI v9(0x69), v8

    Begin block 0xd
    prev=[0x0], succ=[0x43, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x8f283970) = CONST 
    0x19: v19 = GT v14(0x8f283970), v12
    0x1a: v1a(0x43) = CONST 
    0x1d: JUMPI v1a(0x43), v19

    Begin block 0x43
    prev=[0xd], succ=[0xc19, 0x4f]
    =================================
    0x45: v45(0x3659cfe6) = CONST 
    0x4a: v4a = EQ v45(0x3659cfe6), v12
    0xc10: vc10(0xc19) = CONST 
    0xc11: JUMPI vc10(0xc19), v4a

    Begin block 0xc19
    prev=[0x43], succ=[]
    =================================
    0xc1a: vc1a(0x8b) = CONST 
    0xc1b: CALLPRIVATE vc1a(0x8b)

    Begin block 0x4f
    prev=[0x43], succ=[0xc1c, 0x5a]
    =================================
    0x50: v50(0x4f1ef286) = CONST 
    0x55: v55 = EQ v50(0x4f1ef286), v12
    0xc12: vc12(0xc1c) = CONST 
    0xc13: JUMPI vc12(0xc1c), v55

    Begin block 0xc1c
    prev=[0x4f], succ=[]
    =================================
    0xc1d: vc1d(0xcb) = CONST 
    0xc1e: CALLPRIVATE vc1d(0xcb)

    Begin block 0x5a
    prev=[0x4f], succ=[0x65, 0xc1f]
    =================================
    0x5b: v5b(0x5c60da1b) = CONST 
    0x60: v60 = EQ v5b(0x5c60da1b), v12
    0xc14: vc14(0xc1f) = CONST 
    0xc15: JUMPI vc14(0xc1f), v60

    Begin block 0x65
    prev=[0x5a], succ=[0x80]
    =================================
    0x65: v65(0x80) = CONST 
    0x68: JUMP v65(0x80)

    Begin block 0x80
    prev=[0x3f, 0x65, 0x69], succ=[0x28eB0x80]
    =================================
    0x81: v81(0x992) = CONST 
    0x84: v84(0x9b3) = CONST 
    0x87: v87(0x28e) = CONST 
    0x8a: JUMP v87(0x28e)

    Begin block 0x28eB0x80
    prev=[0x80], succ=[0x9b3]
    =================================
    0x28fS0x80: v28fV80(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x80: v2b0V80 = SLOAD v28fV80(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x80: JUMP v84(0x9b3)

    Begin block 0x9b3
    prev=[0x28eB0x80], succ=[0x2b30x0]
    =================================
    0x9b4: v9b4(0x2b3) = CONST 
    0x9b7: JUMP v9b4(0x2b3)

    Begin block 0x2b30x0
    prev=[0x9b3], succ=[0x2ce0x0, 0x2d20x0]
    =================================
    0x2b40x0: v02b4 = CALLDATASIZE 
    0x2b50x0: v02b5(0x0) = CONST 
    0x2b80x0: CALLDATACOPY v02b5(0x0), v02b5(0x0), v02b4
    0x2b90x0: v02b9(0x0) = CONST 
    0x2bc0x0: v02bc = CALLDATASIZE 
    0x2bd0x0: v02bd(0x0) = CONST 
    0x2c00x0: v02c0 = GAS 
    0x2c10x0: v02c1 = DELEGATECALL v02c0, v2b0V80, v02bd(0x0), v02bc, v02b9(0x0), v02b9(0x0)
    0x2c20x0: v02c2 = RETURNDATASIZE 
    0x2c30x0: v02c3(0x0) = CONST 
    0x2c60x0: RETURNDATACOPY v02c3(0x0), v02c3(0x0), v02c2
    0x2c90x0: v02c9 = ISZERO v02c1
    0x2ca0x0: v02ca(0x2d2) = CONST 
    0x2cd0x0: JUMPI v02ca(0x2d2), v02c9

    Begin block 0x2ce0x0
    prev=[0x2b30x0], succ=[]
    =================================
    0x2ce0x0: v02ce = RETURNDATASIZE 
    0x2cf0x0: v02cf(0x0) = CONST 
    0x2d10x0: RETURN v02cf(0x0), v02ce

    Begin block 0x2d20x0
    prev=[0x2b30x0], succ=[]
    =================================
    0x2d30x0: v02d3 = RETURNDATASIZE 
    0x2d40x0: v02d4(0x0) = CONST 
    0x2d60x0: REVERT v02d4(0x0), v02d3

    Begin block 0xc1f
    prev=[0x5a], succ=[]
    =================================
    0xc20: vc20(0x158) = CONST 
    0xc21: CALLPRIVATE vc20(0x158)

    Begin block 0x1e
    prev=[0xd], succ=[0xc22, 0x29]
    =================================
    0x1f: v1f(0x8f283970) = CONST 
    0x24: v24 = EQ v1f(0x8f283970), v12
    0xc0a: vc0a(0xc22) = CONST 
    0xc0b: JUMPI vc0a(0xc22), v24

    Begin block 0xc22
    prev=[0x1e], succ=[]
    =================================
    0xc23: vc23(0x196) = CONST 
    0xc24: CALLPRIVATE vc23(0x196)

    Begin block 0x29
    prev=[0x1e], succ=[0xc25, 0x34]
    =================================
    0x2a: v2a(0xcf7a1d77) = CONST 
    0x2f: v2f = EQ v2a(0xcf7a1d77), v12
    0xc0c: vc0c(0xc25) = CONST 
    0xc0d: JUMPI vc0c(0xc25), v2f

    Begin block 0xc25
    prev=[0x29], succ=[]
    =================================
    0xc26: vc26(0x1d6) = CONST 
    0xc27: CALLPRIVATE vc26(0x1d6)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xc28]
    =================================
    0x35: v35(0xf851a440) = CONST 
    0x3a: v3a = EQ v35(0xf851a440), v12
    0xc0e: vc0e(0xc28) = CONST 
    0xc0f: JUMPI vc0e(0xc28), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x80]
    =================================
    0x3f: v3f(0x80) = CONST 
    0x42: JUMP v3f(0x80)

    Begin block 0xc28
    prev=[0x34], succ=[]
    =================================
    0xc29: vc29(0x279) = CONST 
    0xc2a: CALLPRIVATE vc29(0x279)

    Begin block 0x69
    prev=[0x0], succ=[0xc16, 0x80]
    =================================
    0x6a: v6a = CALLDATASIZE 
    0x6b: v6b(0x80) = CONST 
    0x6e: JUMPI v6b(0x80), v6a

    Begin block 0xc16
    prev=[0x69], succ=[]
    =================================
    0xc16: vc16(0xc18) = CONST 
    0xc17: CALLPRIVATE vc16(0xc18)

}

function implementation()() public {
    Begin block 0x158
    prev=[], succ=[0x160, 0x164]
    =================================
    0x159: v159 = CALLVALUE 
    0x15b: v15b = ISZERO v159
    0x15c: v15c(0x164) = CONST 
    0x15f: JUMPI v15c(0x164), v15b

    Begin block 0x160
    prev=[0x158], succ=[]
    =================================
    0x160: v160(0x0) = CONST 
    0x163: REVERT v160(0x0), v160(0x0)

    Begin block 0x164
    prev=[0x158], succ=[0xa19]
    =================================
    0x166: v166(0xa19) = CONST 
    0x169: v169(0x3ff) = CONST 
    0x16c: v16c_0 = CALLPRIVATE v169(0x3ff), v166(0xa19)

    Begin block 0xa19
    prev=[0x164], succ=[]
    =================================
    0xa1a: va1a(0x40) = CONST 
    0xa1d: va1d = MLOAD va1a(0x40)
    0xa1e: va1e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa35: va35 = AND v16c_0, va1e(0xffffffffffffffffffffffffffffffffffffffff)
    0xa37: MSTORE va1d, va35
    0xa38: va38 = MLOAD va1a(0x40)
    0xa3c: va3c(0x0) = SUB va1d, va38
    0xa3d: va3d(0x20) = CONST 
    0xa3f: va3f(0x20) = ADD va3d(0x20), va3c(0x0)
    0xa41: RETURN va38, va3f(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x196
    prev=[], succ=[0x19e, 0x1a2]
    =================================
    0x197: v197 = CALLVALUE 
    0x199: v199 = ISZERO v197
    0x19a: v19a(0x1a2) = CONST 
    0x19d: JUMPI v19a(0x1a2), v199

    Begin block 0x19e
    prev=[0x196], succ=[]
    =================================
    0x19e: v19e(0x0) = CONST 
    0x1a1: REVERT v19e(0x0), v19e(0x0)

    Begin block 0x1a2
    prev=[0x196], succ=[0x1b5, 0x1b9]
    =================================
    0x1a4: v1a4(0xa61) = CONST 
    0x1a7: v1a7(0x4) = CONST 
    0x1aa: v1aa = CALLDATASIZE 
    0x1ab: v1ab = SUB v1aa, v1a7(0x4)
    0x1ac: v1ac(0x20) = CONST 
    0x1af: v1af = LT v1ab, v1ac(0x20)
    0x1b0: v1b0 = ISZERO v1af
    0x1b1: v1b1(0x1b9) = CONST 
    0x1b4: JUMPI v1b1(0x1b9), v1b0

    Begin block 0x1b5
    prev=[0x1a2], succ=[]
    =================================
    0x1b5: v1b5(0x0) = CONST 
    0x1b8: REVERT v1b5(0x0), v1b5(0x0)

    Begin block 0x1b9
    prev=[0x1a2], succ=[0x456]
    =================================
    0x1bb: v1bb = CALLDATALOAD v1a7(0x4)
    0x1bc: v1bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d1: v1d1 = AND v1bc(0xffffffffffffffffffffffffffffffffffffffff), v1bb
    0x1d2: v1d2(0x456) = CONST 
    0x1d5: JUMP v1d2(0x456)

    Begin block 0x456
    prev=[0x1b9], succ=[0x6abB0x456]
    =================================
    0x457: v457(0x45e) = CONST 
    0x45a: v45a(0x6ab) = CONST 
    0x45d: JUMP v45a(0x6ab)

    Begin block 0x6abB0x456
    prev=[0x456], succ=[0x45e]
    =================================
    0x6acS0x456: v6acV456(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x456: v6cdV456 = SLOAD v6acV456(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x456: JUMP v457(0x45e)

    Begin block 0x45e
    prev=[0x6abB0x456], succ=[0x492, 0x3250x196]
    =================================
    0x45f: v45f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x474: v474 = AND v45f(0xffffffffffffffffffffffffffffffffffffffff), v6cdV456
    0x475: v475 = CALLER 
    0x476: v476(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x48b: v48b = AND v476(0xffffffffffffffffffffffffffffffffffffffff), v475
    0x48c: v48c = EQ v48b, v474
    0x48d: v48d = ISZERO v48c
    0x48e: v48e(0x325) = CONST 
    0x491: JUMPI v48e(0x325), v48d

    Begin block 0x492
    prev=[0x45e], succ=[0x6abB0x492]
    =================================
    0x492: v492(0x499) = CONST 
    0x495: v495(0x6ab) = CONST 
    0x498: JUMP v495(0x6ab)

    Begin block 0x6abB0x492
    prev=[0x492], succ=[0x499]
    =================================
    0x6acS0x492: v6acV492(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x492: v6cdV492 = SLOAD v6acV492(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x492: JUMP v492(0x499)

    Begin block 0x499
    prev=[0x6abB0x492], succ=[0x4cd, 0x51d]
    =================================
    0x49a: v49a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4af: v4af = AND v49a(0xffffffffffffffffffffffffffffffffffffffff), v6cdV492
    0x4b1: v4b1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4c6: v4c6 = AND v4b1(0xffffffffffffffffffffffffffffffffffffffff), v1d1
    0x4c7: v4c7 = EQ v4c6, v4af
    0x4c8: v4c8 = ISZERO v4c7
    0x4c9: v4c9(0x51d) = CONST 
    0x4cc: JUMPI v4c9(0x51d), v4c8

    Begin block 0x4cd
    prev=[0x499], succ=[]
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
    0x500: v500(0x25) = CONST 
    0x503: MSTORE v4fa, v500(0x25)
    0x504: v504(0x20) = CONST 
    0x506: v506 = ADD v504(0x20), v4fa
    0x508: v508(0x871) = CONST 
    0x50b: v50b(0x25) = CONST 
    0x50e: CODECOPY v506, v508(0x871), v50b(0x25)
    0x50f: v50f(0x40) = CONST 
    0x511: v511 = ADD v50f(0x40), v506
    0x515: v515(0x40) = CONST 
    0x517: v517 = MLOAD v515(0x40)
    0x51a: v51a(0x84) = SUB v511, v517
    0x51c: REVERT v517, v51a(0x84)

    Begin block 0x51d
    prev=[0x499], succ=[0x6abB0x51d]
    =================================
    0x51e: v51e(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x53f: v53f(0x546) = CONST 
    0x542: v542(0x6ab) = CONST 
    0x545: JUMP v542(0x6ab)

    Begin block 0x6abB0x51d
    prev=[0x51d], succ=[0x546]
    =================================
    0x6acS0x51d: v6acV51d(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x51d: v6cdV51d = SLOAD v6acV51d(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x51d: JUMP v53f(0x546)

    Begin block 0x546
    prev=[0x6abB0x51d], succ=[0x72aB0x546]
    =================================
    0x547: v547(0x40) = CONST 
    0x54a: v54a = MLOAD v547(0x40)
    0x54b: v54b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x562: v562 = AND v54b(0xffffffffffffffffffffffffffffffffffffffff), v6cdV51d
    0x564: MSTORE v54a, v562
    0x567: v567 = AND v1d1, v54b(0xffffffffffffffffffffffffffffffffffffffff)
    0x568: v568(0x20) = CONST 
    0x56b: v56b = ADD v54a, v568(0x20)
    0x56c: MSTORE v56b, v567
    0x56e: v56e = MLOAD v547(0x40)
    0x572: v572(0x0) = SUB v54a, v56e
    0x573: v573(0x40) = ADD v572(0x0), v547(0x40)
    0x575: LOG1 v56e, v573(0x40), v51e(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x576: v576(0x320) = CONST 
    0x57a: v57a(0x72a) = CONST 
    0x57d: JUMP v57a(0x72a), v1d1, v576(0x320)

    Begin block 0x72aB0x546
    prev=[0x546], succ=[0x767B0x546, 0x7b7B0x546]
    =================================
    0x72bS0x546: v72bV546(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x74cS0x546: v74cV546(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x762S0x546: v762V546 = AND v1d1, v74cV546(0xffffffffffffffffffffffffffffffffffffffff)
    0x763S0x546: v763V546(0x7b7) = CONST 
    0x766S0x546: JUMPI v763V546(0x7b7), v762V546

    Begin block 0x767B0x546
    prev=[0x72aB0x546], succ=[]
    =================================
    0x767S0x546: v767V546(0x40) = CONST 
    0x769S0x546: v769V546 = MLOAD v767V546(0x40)
    0x76aS0x546: v76aV546(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x78cS0x546: MSTORE v769V546, v76aV546(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x78dS0x546: v78dV546(0x4) = CONST 
    0x78fS0x546: v78fV546 = ADD v78dV546(0x4), v769V546
    0x792S0x546: v792V546(0x20) = CONST 
    0x794S0x546: v794V546 = ADD v792V546(0x20), v78fV546
    0x797S0x546: v797V546(0x20) = SUB v794V546, v78fV546
    0x799S0x546: MSTORE v78fV546, v797V546(0x20)
    0x79aS0x546: v79aV546(0x29) = CONST 
    0x79dS0x546: MSTORE v794V546, v79aV546(0x29)
    0x79eS0x546: v79eV546(0x20) = CONST 
    0x7a0S0x546: v7a0V546 = ADD v79eV546(0x20), v794V546
    0x7a2S0x546: v7a2V546(0x8d0) = CONST 
    0x7a5S0x546: v7a5V546(0x29) = CONST 
    0x7a8S0x546: CODECOPY v7a0V546, v7a2V546(0x8d0), v7a5V546(0x29)
    0x7a9S0x546: v7a9V546(0x40) = CONST 
    0x7abS0x546: v7abV546 = ADD v7a9V546(0x40), v7a0V546
    0x7afS0x546: v7afV546(0x40) = CONST 
    0x7b1S0x546: v7b1V546 = MLOAD v7afV546(0x40)
    0x7b4S0x546: v7b4V546(0x84) = SUB v7abV546, v7b1V546
    0x7b6S0x546: REVERT v7b1V546, v7b4V546(0x84)

    Begin block 0x7b7B0x546
    prev=[0x72aB0x546], succ=[0x3200x196]
    =================================
    0x7b8S0x546: SSTORE v72bV546(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v1d1
    0x7b9S0x546: JUMP v576(0x320)

    Begin block 0x3200x196
    prev=[0x7b7B0x546], succ=[0xaeb0x196]
    =================================
    0x3210x196: v196321(0xaeb) = CONST 
    0x3240x196: JUMP v196321(0xaeb)

    Begin block 0xaeb0x196
    prev=[0x3200x196], succ=[0xa61]
    =================================
    0xaed0x196: JUMP v1a4(0xa61)

    Begin block 0xa61
    prev=[0xaeb0x196], succ=[]
    =================================
    0xa62: STOP 

    Begin block 0x3250x196
    prev=[0x45e], succ=[0x71d0x196]
    =================================
    0x3260x196: v196326(0xb0d) = CONST 
    0x3290x196: v196329(0x71d) = CONST 
    0x32c0x196: JUMP v196329(0x71d)

    Begin block 0x71d0x196
    prev=[0x3250x196], succ=[0x28eB0x71d0x196]
    =================================
    0x71e0x196: v19671e(0x728) = CONST 
    0x7210x196: v196721(0xc05) = CONST 
    0x7240x196: v196724(0x28e) = CONST 
    0x7270x196: JUMP v196724(0x28e)

    Begin block 0x28eB0x71d0x196
    prev=[0x71d0x196], succ=[0xc050x196]
    =================================
    0x28fS0x71d0x196: v28fV71d196(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0x196: v2b0V71d196 = SLOAD v28fV71d196(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0x196: JUMP v196721(0xc05)

    Begin block 0xc050x196
    prev=[0x28eB0x71d0x196], succ=[0x2b30x196]
    =================================
    0xc060x196: v196c06(0x2b3) = CONST 
    0xc090x196: JUMP v196c06(0x2b3)

    Begin block 0x2b30x196
    prev=[0xc050x196], succ=[0x2ce0x196, 0x2d20x196]
    =================================
    0x2b40x196: v1962b4 = CALLDATASIZE 
    0x2b50x196: v1962b5(0x0) = CONST 
    0x2b80x196: CALLDATACOPY v1962b5(0x0), v1962b5(0x0), v1962b4
    0x2b90x196: v1962b9(0x0) = CONST 
    0x2bc0x196: v1962bc = CALLDATASIZE 
    0x2bd0x196: v1962bd(0x0) = CONST 
    0x2c00x196: v1962c0 = GAS 
    0x2c10x196: v1962c1 = DELEGATECALL v1962c0, v2b0V71d196, v1962bd(0x0), v1962bc, v1962b9(0x0), v1962b9(0x0)
    0x2c20x196: v1962c2 = RETURNDATASIZE 
    0x2c30x196: v1962c3(0x0) = CONST 
    0x2c60x196: RETURNDATACOPY v1962c3(0x0), v1962c3(0x0), v1962c2
    0x2c90x196: v1962c9 = ISZERO v1962c1
    0x2ca0x196: v1962ca(0x2d2) = CONST 
    0x2cd0x196: JUMPI v1962ca(0x2d2), v1962c9

    Begin block 0x2ce0x196
    prev=[0x2b30x196], succ=[]
    =================================
    0x2ce0x196: v1962ce = RETURNDATASIZE 
    0x2cf0x196: v1962cf(0x0) = CONST 
    0x2d10x196: RETURN v1962cf(0x0), v1962ce

    Begin block 0x2d20x196
    prev=[0x2b30x196], succ=[]
    =================================
    0x2d30x196: v1962d3 = RETURNDATASIZE 
    0x2d40x196: v1962d4(0x0) = CONST 
    0x2d60x196: REVERT v1962d4(0x0), v1962d3

}

function initialize(address,address,bytes)() public {
    Begin block 0x1d6
    prev=[], succ=[0x1de, 0x1e2]
    =================================
    0x1d7: v1d7 = CALLVALUE 
    0x1d9: v1d9 = ISZERO v1d7
    0x1da: v1da(0x1e2) = CONST 
    0x1dd: JUMPI v1da(0x1e2), v1d9

    Begin block 0x1de
    prev=[0x1d6], succ=[]
    =================================
    0x1de: v1de(0x0) = CONST 
    0x1e1: REVERT v1de(0x0), v1de(0x0)

    Begin block 0x1e2
    prev=[0x1d6], succ=[0x1f5, 0x1f9]
    =================================
    0x1e4: v1e4(0xa82) = CONST 
    0x1e7: v1e7(0x4) = CONST 
    0x1ea: v1ea = CALLDATASIZE 
    0x1eb: v1eb = SUB v1ea, v1e7(0x4)
    0x1ec: v1ec(0x60) = CONST 
    0x1ef: v1ef = LT v1eb, v1ec(0x60)
    0x1f0: v1f0 = ISZERO v1ef
    0x1f1: v1f1(0x1f9) = CONST 
    0x1f4: JUMPI v1f1(0x1f9), v1f0

    Begin block 0x1f5
    prev=[0x1e2], succ=[]
    =================================
    0x1f5: v1f5(0x0) = CONST 
    0x1f8: REVERT v1f5(0x0), v1f5(0x0)

    Begin block 0x1f9
    prev=[0x1e2], succ=[0x236, 0x23a]
    =================================
    0x1fa: v1fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x210: v210 = CALLDATALOAD v1e7(0x4)
    0x212: v212 = AND v1fa(0xffffffffffffffffffffffffffffffffffffffff), v210
    0x214: v214(0x20) = CONST 
    0x217: v217(0x24) = ADD v1e7(0x4), v214(0x20)
    0x218: v218 = CALLDATALOAD v217(0x24)
    0x21b: v21b = AND v1fa(0xffffffffffffffffffffffffffffffffffffffff), v218
    0x21e: v21e = ADD v1e7(0x4), v1eb
    0x220: v220(0x60) = CONST 
    0x223: v223(0x64) = ADD v1e7(0x4), v220(0x60)
    0x224: v224(0x40) = CONST 
    0x227: v227(0x44) = ADD v1e7(0x4), v224(0x40)
    0x228: v228 = CALLDATALOAD v227(0x44)
    0x229: v229(0x100000000) = CONST 
    0x230: v230 = GT v228, v229(0x100000000)
    0x231: v231 = ISZERO v230
    0x232: v232(0x23a) = CONST 
    0x235: JUMPI v232(0x23a), v231

    Begin block 0x236
    prev=[0x1f9], succ=[]
    =================================
    0x236: v236(0x0) = CONST 
    0x239: REVERT v236(0x0), v236(0x0)

    Begin block 0x23a
    prev=[0x1f9], succ=[0x248, 0x24c]
    =================================
    0x23c: v23c = ADD v1e7(0x4), v228
    0x23e: v23e(0x20) = CONST 
    0x241: v241 = ADD v23c, v23e(0x20)
    0x242: v242 = GT v241, v21e
    0x243: v243 = ISZERO v242
    0x244: v244(0x24c) = CONST 
    0x247: JUMPI v244(0x24c), v243

    Begin block 0x248
    prev=[0x23a], succ=[]
    =================================
    0x248: v248(0x0) = CONST 
    0x24b: REVERT v248(0x0), v248(0x0)

    Begin block 0x24c
    prev=[0x23a], succ=[0x26a, 0x26e]
    =================================
    0x24e: v24e = CALLDATALOAD v23c
    0x250: v250(0x20) = CONST 
    0x252: v252 = ADD v250(0x20), v23c
    0x255: v255(0x1) = CONST 
    0x258: v258 = MUL v24e, v255(0x1)
    0x25a: v25a = ADD v252, v258
    0x25b: v25b = GT v25a, v21e
    0x25c: v25c(0x100000000) = CONST 
    0x263: v263 = GT v24e, v25c(0x100000000)
    0x264: v264 = OR v263, v25b
    0x265: v265 = ISZERO v264
    0x266: v266(0x26e) = CONST 
    0x269: JUMPI v266(0x26e), v265

    Begin block 0x26a
    prev=[0x24c], succ=[]
    =================================
    0x26a: v26a(0x0) = CONST 
    0x26d: REVERT v26a(0x0), v26a(0x0)

    Begin block 0x26e
    prev=[0x24c], succ=[0x57e]
    =================================
    0x275: v275(0x57e) = CONST 
    0x278: JUMP v275(0x57e)

    Begin block 0x57e
    prev=[0x26e], succ=[0x6abB0x57e]
    =================================
    0x57f: v57f(0x586) = CONST 
    0x582: v582(0x6ab) = CONST 
    0x585: JUMP v582(0x6ab)

    Begin block 0x6abB0x57e
    prev=[0x57e], succ=[0x586]
    =================================
    0x6acS0x57e: v6acV57e(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x57e: v6cdV57e = SLOAD v6acV57e(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x57e: JUMP v57f(0x586)

    Begin block 0x586
    prev=[0x6abB0x57e], succ=[0x5ba, 0x65c]
    =================================
    0x587: v587(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x59c: v59c = AND v587(0xffffffffffffffffffffffffffffffffffffffff), v6cdV57e
    0x59d: v59d = CALLER 
    0x59e: v59e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b3: v5b3 = AND v59e(0xffffffffffffffffffffffffffffffffffffffff), v59d
    0x5b4: v5b4 = EQ v5b3, v59c
    0x5b5: v5b5 = ISZERO v5b4
    0x5b6: v5b6(0x65c) = CONST 
    0x5b9: JUMPI v5b6(0x65c), v5b5

    Begin block 0x5ba
    prev=[0x586], succ=[0x5c2]
    =================================
    0x5ba: v5ba(0x5c2) = CONST 
    0x5be: v5be(0x6d0) = CONST 
    0x5c1: CALLPRIVATE v5be(0x6d0), v212, v5ba(0x5c2)

    Begin block 0x5c2
    prev=[0x5ba], succ=[0x72aB0x5c2]
    =================================
    0x5c3: v5c3(0x5cb) = CONST 
    0x5c7: v5c7(0x72a) = CONST 
    0x5ca: JUMP v5c7(0x72a), v21b, v5c3(0x5cb)

    Begin block 0x72aB0x5c2
    prev=[0x5c2], succ=[0x767B0x5c2, 0x7b7B0x5c2]
    =================================
    0x72bS0x5c2: v72bV5c2(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x74cS0x5c2: v74cV5c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x762S0x5c2: v762V5c2 = AND v21b, v74cV5c2(0xffffffffffffffffffffffffffffffffffffffff)
    0x763S0x5c2: v763V5c2(0x7b7) = CONST 
    0x766S0x5c2: JUMPI v763V5c2(0x7b7), v762V5c2

    Begin block 0x767B0x5c2
    prev=[0x72aB0x5c2], succ=[]
    =================================
    0x767S0x5c2: v767V5c2(0x40) = CONST 
    0x769S0x5c2: v769V5c2 = MLOAD v767V5c2(0x40)
    0x76aS0x5c2: v76aV5c2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x78cS0x5c2: MSTORE v769V5c2, v76aV5c2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x78dS0x5c2: v78dV5c2(0x4) = CONST 
    0x78fS0x5c2: v78fV5c2 = ADD v78dV5c2(0x4), v769V5c2
    0x792S0x5c2: v792V5c2(0x20) = CONST 
    0x794S0x5c2: v794V5c2 = ADD v792V5c2(0x20), v78fV5c2
    0x797S0x5c2: v797V5c2(0x20) = SUB v794V5c2, v78fV5c2
    0x799S0x5c2: MSTORE v78fV5c2, v797V5c2(0x20)
    0x79aS0x5c2: v79aV5c2(0x29) = CONST 
    0x79dS0x5c2: MSTORE v794V5c2, v79aV5c2(0x29)
    0x79eS0x5c2: v79eV5c2(0x20) = CONST 
    0x7a0S0x5c2: v7a0V5c2 = ADD v79eV5c2(0x20), v794V5c2
    0x7a2S0x5c2: v7a2V5c2(0x8d0) = CONST 
    0x7a5S0x5c2: v7a5V5c2(0x29) = CONST 
    0x7a8S0x5c2: CODECOPY v7a0V5c2, v7a2V5c2(0x8d0), v7a5V5c2(0x29)
    0x7a9S0x5c2: v7a9V5c2(0x40) = CONST 
    0x7abS0x5c2: v7abV5c2 = ADD v7a9V5c2(0x40), v7a0V5c2
    0x7afS0x5c2: v7afV5c2(0x40) = CONST 
    0x7b1S0x5c2: v7b1V5c2 = MLOAD v7afV5c2(0x40)
    0x7b4S0x5c2: v7b4V5c2(0x84) = SUB v7abV5c2, v7b1V5c2
    0x7b6S0x5c2: REVERT v7b1V5c2, v7b4V5c2(0x84)

    Begin block 0x7b7B0x5c2
    prev=[0x72aB0x5c2], succ=[0x5cb]
    =================================
    0x7b8S0x5c2: SSTORE v72bV5c2(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v21b
    0x7b9S0x5c2: JUMP v5c3(0x5cb)

    Begin block 0x5cb
    prev=[0x7b7B0x5c2], succ=[0x5d2, 0x657]
    =================================
    0x5cd: v5cd = ISZERO v24e
    0x5ce: v5ce(0x657) = CONST 
    0x5d1: JUMPI v5ce(0x657), v5cd

    Begin block 0x5d2
    prev=[0x5cb], succ=[0x28eB0x5d2]
    =================================
    0x5d2: v5d2(0x0) = CONST 
    0x5d4: v5d4(0x5db) = CONST 
    0x5d7: v5d7(0x28e) = CONST 
    0x5da: JUMP v5d7(0x28e)

    Begin block 0x28eB0x5d2
    prev=[0x5d2], succ=[0x5db]
    =================================
    0x28fS0x5d2: v28fV5d2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x5d2: v2b0V5d2 = SLOAD v28fV5d2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x5d2: JUMP v5d4(0x5db)

    Begin block 0x5db
    prev=[0x28eB0x5d2], succ=[0x621, 0x642]
    =================================
    0x5dc: v5dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5f1: v5f1 = AND v5dc(0xffffffffffffffffffffffffffffffffffffffff), v2b0V5d2
    0x5f4: v5f4(0x40) = CONST 
    0x5f6: v5f6 = MLOAD v5f4(0x40)
    0x5fd: CALLDATACOPY v5f6, v252, v24e
    0x5fe: v5fe(0x40) = CONST 
    0x600: v600 = MLOAD v5fe(0x40)
    0x602: v602 = ADD v5f6, v24e
    0x605: v605(0x0) = CONST 
    0x60f: v60f = SUB v602, v600
    0x612: v612 = GAS 
    0x613: v613 = DELEGATECALL v612, v5f1, v600, v60f, v600, v605(0x0)
    0x617: v617 = RETURNDATASIZE 
    0x619: v619(0x0) = CONST 
    0x61c: v61c = EQ v617, v619(0x0)
    0x61d: v61d(0x642) = CONST 
    0x620: JUMPI v61d(0x642), v61c

    Begin block 0x621
    prev=[0x5db], succ=[0x647]
    =================================
    0x621: v621(0x40) = CONST 
    0x623: v623 = MLOAD v621(0x40)
    0x626: v626(0x1f) = CONST 
    0x628: v628(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v626(0x1f)
    0x629: v629(0x3f) = CONST 
    0x62b: v62b = RETURNDATASIZE 
    0x62c: v62c = ADD v62b, v629(0x3f)
    0x62d: v62d = AND v62c, v628(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x62f: v62f = ADD v623, v62d
    0x630: v630(0x40) = CONST 
    0x632: MSTORE v630(0x40), v62f
    0x633: v633 = RETURNDATASIZE 
    0x635: MSTORE v623, v633
    0x636: v636 = RETURNDATASIZE 
    0x637: v637(0x0) = CONST 
    0x639: v639(0x20) = CONST 
    0x63c: v63c = ADD v623, v639(0x20)
    0x63d: RETURNDATACOPY v63c, v637(0x0), v636
    0x63e: v63e(0x647) = CONST 
    0x641: JUMP v63e(0x647)

    Begin block 0x647
    prev=[0x621, 0x642], succ=[0x651, 0x655]
    =================================
    0x64d: v64d(0x655) = CONST 
    0x650: JUMPI v64d(0x655), v613

    Begin block 0x651
    prev=[0x647], succ=[]
    =================================
    0x651: v651(0x0) = CONST 
    0x654: REVERT v651(0x0), v651(0x0)

    Begin block 0x655
    prev=[0x647], succ=[0x657]
    =================================

    Begin block 0x657
    prev=[0x5cb, 0x655], succ=[0xbbb]
    =================================
    0x658: v658(0xbbb) = CONST 
    0x65b: JUMP v658(0xbbb)

    Begin block 0xbbb
    prev=[0x657], succ=[0xa82]
    =================================
    0xbc0: JUMP v1e4(0xa82)

    Begin block 0xa82
    prev=[0xbbb], succ=[]
    =================================
    0xa83: STOP 

    Begin block 0x642
    prev=[0x5db], succ=[0x647]
    =================================
    0x643: v643(0x60) = CONST 

    Begin block 0x65c
    prev=[0x586], succ=[0x71d0x1d6]
    =================================
    0x65d: v65d(0xbe0) = CONST 
    0x660: v660(0x71d) = CONST 
    0x663: JUMP v660(0x71d)

    Begin block 0x71d0x1d6
    prev=[0x65c], succ=[0x28eB0x71d0x1d6]
    =================================
    0x71e0x1d6: v1d671e(0x728) = CONST 
    0x7210x1d6: v1d6721(0xc05) = CONST 
    0x7240x1d6: v1d6724(0x28e) = CONST 
    0x7270x1d6: JUMP v1d6724(0x28e)

    Begin block 0x28eB0x71d0x1d6
    prev=[0x71d0x1d6], succ=[0xc050x1d6]
    =================================
    0x28fS0x71d0x1d6: v28fV71d1d6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0x1d6: v2b0V71d1d6 = SLOAD v28fV71d1d6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0x1d6: JUMP v1d6721(0xc05)

    Begin block 0xc050x1d6
    prev=[0x28eB0x71d0x1d6], succ=[0x2b30x1d6]
    =================================
    0xc060x1d6: v1d6c06(0x2b3) = CONST 
    0xc090x1d6: JUMP v1d6c06(0x2b3)

    Begin block 0x2b30x1d6
    prev=[0xc050x1d6], succ=[0x2ce0x1d6, 0x2d20x1d6]
    =================================
    0x2b40x1d6: v1d62b4 = CALLDATASIZE 
    0x2b50x1d6: v1d62b5(0x0) = CONST 
    0x2b80x1d6: CALLDATACOPY v1d62b5(0x0), v1d62b5(0x0), v1d62b4
    0x2b90x1d6: v1d62b9(0x0) = CONST 
    0x2bc0x1d6: v1d62bc = CALLDATASIZE 
    0x2bd0x1d6: v1d62bd(0x0) = CONST 
    0x2c00x1d6: v1d62c0 = GAS 
    0x2c10x1d6: v1d62c1 = DELEGATECALL v1d62c0, v2b0V71d1d6, v1d62bd(0x0), v1d62bc, v1d62b9(0x0), v1d62b9(0x0)
    0x2c20x1d6: v1d62c2 = RETURNDATASIZE 
    0x2c30x1d6: v1d62c3(0x0) = CONST 
    0x2c60x1d6: RETURNDATACOPY v1d62c3(0x0), v1d62c3(0x0), v1d62c2
    0x2c90x1d6: v1d62c9 = ISZERO v1d62c1
    0x2ca0x1d6: v1d62ca(0x2d2) = CONST 
    0x2cd0x1d6: JUMPI v1d62ca(0x2d2), v1d62c9

    Begin block 0x2ce0x1d6
    prev=[0x2b30x1d6], succ=[]
    =================================
    0x2ce0x1d6: v1d62ce = RETURNDATASIZE 
    0x2cf0x1d6: v1d62cf(0x0) = CONST 
    0x2d10x1d6: RETURN v1d62cf(0x0), v1d62ce

    Begin block 0x2d20x1d6
    prev=[0x2b30x1d6], succ=[]
    =================================
    0x2d30x1d6: v1d62d3 = RETURNDATASIZE 
    0x2d40x1d6: v1d62d4(0x0) = CONST 
    0x2d60x1d6: REVERT v1d62d4(0x0), v1d62d3

}

function admin()() public {
    Begin block 0x279
    prev=[], succ=[0x281, 0x285]
    =================================
    0x27a: v27a = CALLVALUE 
    0x27c: v27c = ISZERO v27a
    0x27d: v27d(0x285) = CONST 
    0x280: JUMPI v27d(0x285), v27c

    Begin block 0x281
    prev=[0x279], succ=[]
    =================================
    0x281: v281(0x0) = CONST 
    0x284: REVERT v281(0x0), v281(0x0)

    Begin block 0x285
    prev=[0x279], succ=[0xaa3]
    =================================
    0x287: v287(0xaa3) = CONST 
    0x28a: v28a(0x66a) = CONST 
    0x28d: v28d_0 = CALLPRIVATE v28a(0x66a), v287(0xaa3)

    Begin block 0xaa3
    prev=[0x285], succ=[]
    =================================
    0xaa4: vaa4(0x40) = CONST 
    0xaa7: vaa7 = MLOAD vaa4(0x40)
    0xaa8: vaa8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xabf: vabf = AND v28d_0, vaa8(0xffffffffffffffffffffffffffffffffffffffff)
    0xac1: MSTORE vaa7, vabf
    0xac2: vac2 = MLOAD vaa4(0x40)
    0xac6: vac6(0x0) = SUB vaa7, vac2
    0xac7: vac7(0x20) = CONST 
    0xac9: vac9(0x20) = ADD vac7(0x20), vac6(0x0)
    0xacb: RETURN vac2, vac9(0x20)

}

function 0x3ff(0x3ffarg0x0) private {
    Begin block 0x3ff
    prev=[], succ=[0x6abB0x3ff]
    =================================
    0x400: v400(0x0) = CONST 
    0x402: v402(0x409) = CONST 
    0x405: v405(0x6ab) = CONST 
    0x408: JUMP v405(0x6ab)

    Begin block 0x6abB0x3ff
    prev=[0x3ff], succ=[0x409]
    =================================
    0x6acS0x3ff: v6acV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x3ff: v6cdV3ff = SLOAD v6acV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x3ff: JUMP v402(0x409)

    Begin block 0x409
    prev=[0x6abB0x3ff], succ=[0x43d, 0x44b0x3ff]
    =================================
    0x40a: v40a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x41f: v41f = AND v40a(0xffffffffffffffffffffffffffffffffffffffff), v6cdV3ff
    0x420: v420 = CALLER 
    0x421: v421(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x436: v436 = AND v421(0xffffffffffffffffffffffffffffffffffffffff), v420
    0x437: v437 = EQ v436, v41f
    0x438: v438 = ISZERO v437
    0x439: v439(0x44b) = CONST 
    0x43c: JUMPI v439(0x44b), v438

    Begin block 0x43d
    prev=[0x409], succ=[0x28eB0x43d]
    =================================
    0x43d: v43d(0x444) = CONST 
    0x440: v440(0x28e) = CONST 
    0x443: JUMP v440(0x28e)

    Begin block 0x28eB0x43d
    prev=[0x43d], succ=[0x4440x3ff]
    =================================
    0x28fS0x43d: v28fV43d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x43d: v2b0V43d = SLOAD v28fV43d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x43d: JUMP v43d(0x444)

    Begin block 0x4440x3ff
    prev=[0x28eB0x43d], succ=[0xb770x3ff]
    =================================
    0x4470x3ff: v3ff447(0xb77) = CONST 
    0x44a0x3ff: JUMP v3ff447(0xb77)

    Begin block 0xb770x3ff
    prev=[0x4440x3ff], succ=[]
    =================================
    0xb790x3ff: RETURNPRIVATE v3ffarg0, v2b0V43d

    Begin block 0x44b0x3ff
    prev=[0x409], succ=[0x71d0x3ff]
    =================================
    0x44c0x3ff: v3ff44c(0xb99) = CONST 
    0x44f0x3ff: v3ff44f(0x71d) = CONST 
    0x4520x3ff: JUMP v3ff44f(0x71d)

    Begin block 0x71d0x3ff
    prev=[0x44b0x3ff], succ=[0x28eB0x71d0x3ff]
    =================================
    0x71e0x3ff: v3ff71e(0x728) = CONST 
    0x7210x3ff: v3ff721(0xc05) = CONST 
    0x7240x3ff: v3ff724(0x28e) = CONST 
    0x7270x3ff: JUMP v3ff724(0x28e)

    Begin block 0x28eB0x71d0x3ff
    prev=[0x71d0x3ff], succ=[0xc050x3ff]
    =================================
    0x28fS0x71d0x3ff: v28fV71d3ff(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0x3ff: v2b0V71d3ff = SLOAD v28fV71d3ff(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0x3ff: JUMP v3ff721(0xc05)

    Begin block 0xc050x3ff
    prev=[0x28eB0x71d0x3ff], succ=[0x2b30x3ff]
    =================================
    0xc060x3ff: v3ffc06(0x2b3) = CONST 
    0xc090x3ff: JUMP v3ffc06(0x2b3)

    Begin block 0x2b30x3ff
    prev=[0xc050x3ff], succ=[0x2ce0x3ff, 0x2d20x3ff]
    =================================
    0x2b40x3ff: v3ff2b4 = CALLDATASIZE 
    0x2b50x3ff: v3ff2b5(0x0) = CONST 
    0x2b80x3ff: CALLDATACOPY v3ff2b5(0x0), v3ff2b5(0x0), v3ff2b4
    0x2b90x3ff: v3ff2b9(0x0) = CONST 
    0x2bc0x3ff: v3ff2bc = CALLDATASIZE 
    0x2bd0x3ff: v3ff2bd(0x0) = CONST 
    0x2c00x3ff: v3ff2c0 = GAS 
    0x2c10x3ff: v3ff2c1 = DELEGATECALL v3ff2c0, v2b0V71d3ff, v3ff2bd(0x0), v3ff2bc, v3ff2b9(0x0), v3ff2b9(0x0)
    0x2c20x3ff: v3ff2c2 = RETURNDATASIZE 
    0x2c30x3ff: v3ff2c3(0x0) = CONST 
    0x2c60x3ff: RETURNDATACOPY v3ff2c3(0x0), v3ff2c3(0x0), v3ff2c2
    0x2c90x3ff: v3ff2c9 = ISZERO v3ff2c1
    0x2ca0x3ff: v3ff2ca(0x2d2) = CONST 
    0x2cd0x3ff: JUMPI v3ff2ca(0x2d2), v3ff2c9

    Begin block 0x2ce0x3ff
    prev=[0x2b30x3ff], succ=[]
    =================================
    0x2ce0x3ff: v3ff2ce = RETURNDATASIZE 
    0x2cf0x3ff: v3ff2cf(0x0) = CONST 
    0x2d10x3ff: RETURN v3ff2cf(0x0), v3ff2ce

    Begin block 0x2d20x3ff
    prev=[0x2b30x3ff], succ=[]
    =================================
    0x2d30x3ff: v3ff2d3 = RETURNDATASIZE 
    0x2d40x3ff: v3ff2d4(0x0) = CONST 
    0x2d60x3ff: REVERT v3ff2d4(0x0), v3ff2d3

}

function 0x66a(0x66aarg0x0) private {
    Begin block 0x66a
    prev=[], succ=[0x6abB0x66a]
    =================================
    0x66b: v66b(0x0) = CONST 
    0x66d: v66d(0x674) = CONST 
    0x670: v670(0x6ab) = CONST 
    0x673: JUMP v670(0x6ab)

    Begin block 0x6abB0x66a
    prev=[0x66a], succ=[0x674]
    =================================
    0x6acS0x66a: v6acV66a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x66a: v6cdV66a = SLOAD v6acV66a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x66a: JUMP v66d(0x674)

    Begin block 0x674
    prev=[0x6abB0x66a], succ=[0x6a8, 0x44b0x66a]
    =================================
    0x675: v675(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x68a: v68a = AND v675(0xffffffffffffffffffffffffffffffffffffffff), v6cdV66a
    0x68b: v68b = CALLER 
    0x68c: v68c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a1: v6a1 = AND v68c(0xffffffffffffffffffffffffffffffffffffffff), v68b
    0x6a2: v6a2 = EQ v6a1, v68a
    0x6a3: v6a3 = ISZERO v6a2
    0x6a4: v6a4(0x44b) = CONST 
    0x6a7: JUMPI v6a4(0x44b), v6a3

    Begin block 0x6a8
    prev=[0x674], succ=[0x6ab0x66a]
    =================================
    0x6a8: v6a8(0x444) = CONST 

    Begin block 0x6ab0x66a
    prev=[0x6a8], succ=[0x4440x66a]
    =================================
    0x6ac0x66a: v66a6ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cd0x66a: v66a6cd = SLOAD v66a6ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cf0x66a: JUMP v6a8(0x444)

    Begin block 0x4440x66a
    prev=[0x6ab0x66a], succ=[0xb770x66a]
    =================================
    0x4470x66a: v66a447(0xb77) = CONST 
    0x44a0x66a: JUMP v66a447(0xb77)

    Begin block 0xb770x66a
    prev=[0x4440x66a], succ=[]
    =================================
    0xb790x66a: RETURNPRIVATE v66aarg0, v66a6cd

    Begin block 0x44b0x66a
    prev=[0x674], succ=[0x71d0x66a]
    =================================
    0x44c0x66a: v66a44c(0xb99) = CONST 
    0x44f0x66a: v66a44f(0x71d) = CONST 
    0x4520x66a: JUMP v66a44f(0x71d)

    Begin block 0x71d0x66a
    prev=[0x44b0x66a], succ=[0x28eB0x71d0x66a]
    =================================
    0x71e0x66a: v66a71e(0x728) = CONST 
    0x7210x66a: v66a721(0xc05) = CONST 
    0x7240x66a: v66a724(0x28e) = CONST 
    0x7270x66a: JUMP v66a724(0x28e)

    Begin block 0x28eB0x71d0x66a
    prev=[0x71d0x66a], succ=[0xc050x66a]
    =================================
    0x28fS0x71d0x66a: v28fV71d66a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0x66a: v2b0V71d66a = SLOAD v28fV71d66a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0x66a: JUMP v66a721(0xc05)

    Begin block 0xc050x66a
    prev=[0x28eB0x71d0x66a], succ=[0x2b30x66a]
    =================================
    0xc060x66a: v66ac06(0x2b3) = CONST 
    0xc090x66a: JUMP v66ac06(0x2b3)

    Begin block 0x2b30x66a
    prev=[0xc050x66a], succ=[0x2ce0x66a, 0x2d20x66a]
    =================================
    0x2b40x66a: v66a2b4 = CALLDATASIZE 
    0x2b50x66a: v66a2b5(0x0) = CONST 
    0x2b80x66a: CALLDATACOPY v66a2b5(0x0), v66a2b5(0x0), v66a2b4
    0x2b90x66a: v66a2b9(0x0) = CONST 
    0x2bc0x66a: v66a2bc = CALLDATASIZE 
    0x2bd0x66a: v66a2bd(0x0) = CONST 
    0x2c00x66a: v66a2c0 = GAS 
    0x2c10x66a: v66a2c1 = DELEGATECALL v66a2c0, v2b0V71d66a, v66a2bd(0x0), v66a2bc, v66a2b9(0x0), v66a2b9(0x0)
    0x2c20x66a: v66a2c2 = RETURNDATASIZE 
    0x2c30x66a: v66a2c3(0x0) = CONST 
    0x2c60x66a: RETURNDATACOPY v66a2c3(0x0), v66a2c3(0x0), v66a2c2
    0x2c90x66a: v66a2c9 = ISZERO v66a2c1
    0x2ca0x66a: v66a2ca(0x2d2) = CONST 
    0x2cd0x66a: JUMPI v66a2ca(0x2d2), v66a2c9

    Begin block 0x2ce0x66a
    prev=[0x2b30x66a], succ=[]
    =================================
    0x2ce0x66a: v66a2ce = RETURNDATASIZE 
    0x2cf0x66a: v66a2cf(0x0) = CONST 
    0x2d10x66a: RETURN v66a2cf(0x0), v66a2ce

    Begin block 0x2d20x66a
    prev=[0x2b30x66a], succ=[]
    =================================
    0x2d30x66a: v66a2d3 = RETURNDATASIZE 
    0x2d40x66a: v66a2d4(0x0) = CONST 
    0x2d60x66a: REVERT v66a2d4(0x0), v66a2d3

}

function 0x6d0(0x6d0arg0x0, 0x6d0arg0x1) private {
    Begin block 0x6d0
    prev=[], succ=[0x7ba]
    =================================
    0x6d1: v6d1(0x6d9) = CONST 
    0x6d5: v6d5(0x7ba) = CONST 
    0x6d8: JUMP v6d5(0x7ba)

    Begin block 0x7ba
    prev=[0x6d0], succ=[0x28eB0x7ba]
    =================================
    0x7bb: v7bb(0x0) = CONST 
    0x7bd: v7bd(0x7c4) = CONST 
    0x7c0: v7c0(0x28e) = CONST 
    0x7c3: JUMP v7c0(0x28e)

    Begin block 0x28eB0x7ba
    prev=[0x7ba], succ=[0x7c4]
    =================================
    0x28fS0x7ba: v28fV7ba(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x7ba: v2b0V7ba = SLOAD v28fV7ba(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x7ba: JUMP v7bd(0x7c4)

    Begin block 0x7c4
    prev=[0x28eB0x7ba], succ=[0x7fb, 0x84b]
    =================================
    0x7c8: v7c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7dd: v7dd = AND v7c8(0xffffffffffffffffffffffffffffffffffffffff), v6d0arg0
    0x7df: v7df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7f4: v7f4 = AND v7df(0xffffffffffffffffffffffffffffffffffffffff), v2b0V7ba
    0x7f5: v7f5 = EQ v7f4, v7dd
    0x7f6: v7f6 = ISZERO v7f5
    0x7f7: v7f7(0x84b) = CONST 
    0x7fa: JUMPI v7f7(0x84b), v7f6

    Begin block 0x7fb
    prev=[0x7c4], succ=[]
    =================================
    0x7fb: v7fb(0x40) = CONST 
    0x7fd: v7fd = MLOAD v7fb(0x40)
    0x7fe: v7fe(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x820: MSTORE v7fd, v7fe(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x821: v821(0x4) = CONST 
    0x823: v823 = ADD v821(0x4), v7fd
    0x826: v826(0x20) = CONST 
    0x828: v828 = ADD v826(0x20), v823
    0x82b: v82b(0x20) = SUB v828, v823
    0x82d: MSTORE v823, v82b(0x20)
    0x82e: v82e(0x3a) = CONST 
    0x831: MSTORE v828, v82e(0x3a)
    0x832: v832(0x20) = CONST 
    0x834: v834 = ADD v832(0x20), v828
    0x836: v836(0x896) = CONST 
    0x839: v839(0x3a) = CONST 
    0x83c: CODECOPY v834, v836(0x896), v839(0x3a)
    0x83d: v83d(0x40) = CONST 
    0x83f: v83f = ADD v83d(0x40), v834
    0x843: v843(0x40) = CONST 
    0x845: v845 = MLOAD v843(0x40)
    0x848: v848(0x84) = SUB v83f, v845
    0x84a: REVERT v845, v848(0x84)

    Begin block 0x84b
    prev=[0x7c4], succ=[0x6d9]
    =================================
    0x84d: v84d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x86e: SSTORE v84d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v6d0arg0
    0x86f: JUMP v6d1(0x6d9)

    Begin block 0x6d9
    prev=[0x84b], succ=[]
    =================================
    0x6da: v6da(0x40) = CONST 
    0x6dc: v6dc = MLOAD v6da(0x40)
    0x6dd: v6dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6f3: v6f3 = AND v6d0arg0, v6dd(0xffffffffffffffffffffffffffffffffffffffff)
    0x6f5: v6f5(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x717: v717(0x0) = CONST 
    0x71a: LOG2 v6dc, v717(0x0), v6f5(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v6f3
    0x71c: RETURNPRIVATE v6d0arg1

}

function upgradeTo(address)() public {
    Begin block 0x8b
    prev=[], succ=[0x93, 0x97]
    =================================
    0x8c: v8c = CALLVALUE 
    0x8e: v8e = ISZERO v8c
    0x8f: v8f(0x97) = CONST 
    0x92: JUMPI v8f(0x97), v8e

    Begin block 0x93
    prev=[0x8b], succ=[]
    =================================
    0x93: v93(0x0) = CONST 
    0x96: REVERT v93(0x0), v93(0x0)

    Begin block 0x97
    prev=[0x8b], succ=[0xaa, 0xae]
    =================================
    0x99: v99(0x9d7) = CONST 
    0x9c: v9c(0x4) = CONST 
    0x9f: v9f = CALLDATASIZE 
    0xa0: va0 = SUB v9f, v9c(0x4)
    0xa1: va1(0x20) = CONST 
    0xa4: va4 = LT va0, va1(0x20)
    0xa5: va5 = ISZERO va4
    0xa6: va6(0xae) = CONST 
    0xa9: JUMPI va6(0xae), va5

    Begin block 0xaa
    prev=[0x97], succ=[]
    =================================
    0xaa: vaa(0x0) = CONST 
    0xad: REVERT vaa(0x0), vaa(0x0)

    Begin block 0xae
    prev=[0x97], succ=[0x2dc]
    =================================
    0xb0: vb0 = CALLDATALOAD v9c(0x4)
    0xb1: vb1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc6: vc6 = AND vb1(0xffffffffffffffffffffffffffffffffffffffff), vb0
    0xc7: vc7(0x2dc) = CONST 
    0xca: JUMP vc7(0x2dc)

    Begin block 0x2dc
    prev=[0xae], succ=[0x6abB0x2dc]
    =================================
    0x2dd: v2dd(0x2e4) = CONST 
    0x2e0: v2e0(0x6ab) = CONST 
    0x2e3: JUMP v2e0(0x6ab)

    Begin block 0x6abB0x2dc
    prev=[0x2dc], succ=[0x2e4]
    =================================
    0x6acS0x2dc: v6acV2dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x2dc: v6cdV2dc = SLOAD v6acV2dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x2dc: JUMP v2dd(0x2e4)

    Begin block 0x2e4
    prev=[0x6abB0x2dc], succ=[0x318, 0x3250x8b]
    =================================
    0x2e5: v2e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fa: v2fa = AND v2e5(0xffffffffffffffffffffffffffffffffffffffff), v6cdV2dc
    0x2fb: v2fb = CALLER 
    0x2fc: v2fc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x311: v311 = AND v2fc(0xffffffffffffffffffffffffffffffffffffffff), v2fb
    0x312: v312 = EQ v311, v2fa
    0x313: v313 = ISZERO v312
    0x314: v314(0x325) = CONST 
    0x317: JUMPI v314(0x325), v313

    Begin block 0x318
    prev=[0x2e4], succ=[0x3200x8b]
    =================================
    0x318: v318(0x320) = CONST 
    0x31c: v31c(0x6d0) = CONST 
    0x31f: CALLPRIVATE v31c(0x6d0), vc6, v318(0x320)

    Begin block 0x3200x8b
    prev=[0x318], succ=[0xaeb0x8b]
    =================================
    0x3210x8b: v8b321(0xaeb) = CONST 
    0x3240x8b: JUMP v8b321(0xaeb)

    Begin block 0xaeb0x8b
    prev=[0x3200x8b], succ=[0x9d7]
    =================================
    0xaed0x8b: JUMP v99(0x9d7)

    Begin block 0x9d7
    prev=[0xaeb0x8b], succ=[]
    =================================
    0x9d8: STOP 

    Begin block 0x3250x8b
    prev=[0x2e4], succ=[0x71d0x8b]
    =================================
    0x3260x8b: v8b326(0xb0d) = CONST 
    0x3290x8b: v8b329(0x71d) = CONST 
    0x32c0x8b: JUMP v8b329(0x71d)

    Begin block 0x71d0x8b
    prev=[0x3250x8b], succ=[0x28eB0x71d0x8b]
    =================================
    0x71e0x8b: v8b71e(0x728) = CONST 
    0x7210x8b: v8b721(0xc05) = CONST 
    0x7240x8b: v8b724(0x28e) = CONST 
    0x7270x8b: JUMP v8b724(0x28e)

    Begin block 0x28eB0x71d0x8b
    prev=[0x71d0x8b], succ=[0xc050x8b]
    =================================
    0x28fS0x71d0x8b: v28fV71d8b(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0x8b: v2b0V71d8b = SLOAD v28fV71d8b(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0x8b: JUMP v8b721(0xc05)

    Begin block 0xc050x8b
    prev=[0x28eB0x71d0x8b], succ=[0x2b30x8b]
    =================================
    0xc060x8b: v8bc06(0x2b3) = CONST 
    0xc090x8b: JUMP v8bc06(0x2b3)

    Begin block 0x2b30x8b
    prev=[0xc050x8b], succ=[0x2ce0x8b, 0x2d20x8b]
    =================================
    0x2b40x8b: v8b2b4 = CALLDATASIZE 
    0x2b50x8b: v8b2b5(0x0) = CONST 
    0x2b80x8b: CALLDATACOPY v8b2b5(0x0), v8b2b5(0x0), v8b2b4
    0x2b90x8b: v8b2b9(0x0) = CONST 
    0x2bc0x8b: v8b2bc = CALLDATASIZE 
    0x2bd0x8b: v8b2bd(0x0) = CONST 
    0x2c00x8b: v8b2c0 = GAS 
    0x2c10x8b: v8b2c1 = DELEGATECALL v8b2c0, v2b0V71d8b, v8b2bd(0x0), v8b2bc, v8b2b9(0x0), v8b2b9(0x0)
    0x2c20x8b: v8b2c2 = RETURNDATASIZE 
    0x2c30x8b: v8b2c3(0x0) = CONST 
    0x2c60x8b: RETURNDATACOPY v8b2c3(0x0), v8b2c3(0x0), v8b2c2
    0x2c90x8b: v8b2c9 = ISZERO v8b2c1
    0x2ca0x8b: v8b2ca(0x2d2) = CONST 
    0x2cd0x8b: JUMPI v8b2ca(0x2d2), v8b2c9

    Begin block 0x2ce0x8b
    prev=[0x2b30x8b], succ=[]
    =================================
    0x2ce0x8b: v8b2ce = RETURNDATASIZE 
    0x2cf0x8b: v8b2cf(0x0) = CONST 
    0x2d10x8b: RETURN v8b2cf(0x0), v8b2ce

    Begin block 0x2d20x8b
    prev=[0x2b30x8b], succ=[]
    =================================
    0x2d30x8b: v8b2d3 = RETURNDATASIZE 
    0x2d40x8b: v8b2d4(0x0) = CONST 
    0x2d60x8b: REVERT v8b2d4(0x0), v8b2d3

}

function fallback()() public {
    Begin block 0xc18
    prev=[], succ=[0x28eB0xc18]
    =================================
    0x6f: v6f(0x94d) = CONST 
    0x72: v72(0x96e) = CONST 
    0x75: v75(0x28e) = CONST 
    0x78: JUMP v75(0x28e)

    Begin block 0x28eB0xc18
    prev=[0xc18], succ=[0x96e]
    =================================
    0x28fS0xc18: v28fVc18(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0xc18: v2b0Vc18 = SLOAD v28fVc18(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0xc18: JUMP v72(0x96e)

    Begin block 0x96e
    prev=[0x28eB0xc18], succ=[0x2b30xc18]
    =================================
    0x96f: v96f(0x2b3) = CONST 
    0x972: JUMP v96f(0x2b3)

    Begin block 0x2b30xc18
    prev=[0x96e], succ=[0x2ce0xc18, 0x2d20xc18]
    =================================
    0x2b40xc18: vc182b4 = CALLDATASIZE 
    0x2b50xc18: vc182b5(0x0) = CONST 
    0x2b80xc18: CALLDATACOPY vc182b5(0x0), vc182b5(0x0), vc182b4
    0x2b90xc18: vc182b9(0x0) = CONST 
    0x2bc0xc18: vc182bc = CALLDATASIZE 
    0x2bd0xc18: vc182bd(0x0) = CONST 
    0x2c00xc18: vc182c0 = GAS 
    0x2c10xc18: vc182c1 = DELEGATECALL vc182c0, v2b0Vc18, vc182bd(0x0), vc182bc, vc182b9(0x0), vc182b9(0x0)
    0x2c20xc18: vc182c2 = RETURNDATASIZE 
    0x2c30xc18: vc182c3(0x0) = CONST 
    0x2c60xc18: RETURNDATACOPY vc182c3(0x0), vc182c3(0x0), vc182c2
    0x2c90xc18: vc182c9 = ISZERO vc182c1
    0x2ca0xc18: vc182ca(0x2d2) = CONST 
    0x2cd0xc18: JUMPI vc182ca(0x2d2), vc182c9

    Begin block 0x2ce0xc18
    prev=[0x2b30xc18], succ=[]
    =================================
    0x2ce0xc18: vc182ce = RETURNDATASIZE 
    0x2cf0xc18: vc182cf(0x0) = CONST 
    0x2d10xc18: RETURN vc182cf(0x0), vc182ce

    Begin block 0x2d20xc18
    prev=[0x2b30xc18], succ=[]
    =================================
    0x2d30xc18: vc182d3 = RETURNDATASIZE 
    0x2d40xc18: vc182d4(0x0) = CONST 
    0x2d60xc18: REVERT vc182d4(0x0), vc182d3

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xcb
    prev=[], succ=[0xdd, 0xe1]
    =================================
    0xcc: vcc(0x9f8) = CONST 
    0xcf: vcf(0x4) = CONST 
    0xd2: vd2 = CALLDATASIZE 
    0xd3: vd3 = SUB vd2, vcf(0x4)
    0xd4: vd4(0x40) = CONST 
    0xd7: vd7 = LT vd3, vd4(0x40)
    0xd8: vd8 = ISZERO vd7
    0xd9: vd9(0xe1) = CONST 
    0xdc: JUMPI vd9(0xe1), vd8

    Begin block 0xdd
    prev=[0xcb], succ=[]
    =================================
    0xdd: vdd(0x0) = CONST 
    0xe0: REVERT vdd(0x0), vdd(0x0)

    Begin block 0xe1
    prev=[0xcb], succ=[0x115, 0x119]
    =================================
    0xe2: ve2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf8: vf8 = CALLDATALOAD vcf(0x4)
    0xf9: vf9 = AND vf8, ve2(0xffffffffffffffffffffffffffffffffffffffff)
    0xfd: vfd = ADD vcf(0x4), vd3
    0xff: vff(0x40) = CONST 
    0x102: v102(0x44) = ADD vcf(0x4), vff(0x40)
    0x103: v103(0x20) = CONST 
    0x106: v106(0x24) = ADD vcf(0x4), v103(0x20)
    0x107: v107 = CALLDATALOAD v106(0x24)
    0x108: v108(0x100000000) = CONST 
    0x10f: v10f = GT v107, v108(0x100000000)
    0x110: v110 = ISZERO v10f
    0x111: v111(0x119) = CONST 
    0x114: JUMPI v111(0x119), v110

    Begin block 0x115
    prev=[0xe1], succ=[]
    =================================
    0x115: v115(0x0) = CONST 
    0x118: REVERT v115(0x0), v115(0x0)

    Begin block 0x119
    prev=[0xe1], succ=[0x127, 0x12b]
    =================================
    0x11b: v11b = ADD vcf(0x4), v107
    0x11d: v11d(0x20) = CONST 
    0x120: v120 = ADD v11b, v11d(0x20)
    0x121: v121 = GT v120, vfd
    0x122: v122 = ISZERO v121
    0x123: v123(0x12b) = CONST 
    0x126: JUMPI v123(0x12b), v122

    Begin block 0x127
    prev=[0x119], succ=[]
    =================================
    0x127: v127(0x0) = CONST 
    0x12a: REVERT v127(0x0), v127(0x0)

    Begin block 0x12b
    prev=[0x119], succ=[0x149, 0x14d]
    =================================
    0x12d: v12d = CALLDATALOAD v11b
    0x12f: v12f(0x20) = CONST 
    0x131: v131 = ADD v12f(0x20), v11b
    0x134: v134(0x1) = CONST 
    0x137: v137 = MUL v12d, v134(0x1)
    0x139: v139 = ADD v131, v137
    0x13a: v13a = GT v139, vfd
    0x13b: v13b(0x100000000) = CONST 
    0x142: v142 = GT v12d, v13b(0x100000000)
    0x143: v143 = OR v142, v13a
    0x144: v144 = ISZERO v143
    0x145: v145(0x14d) = CONST 
    0x148: JUMPI v145(0x14d), v144

    Begin block 0x149
    prev=[0x12b], succ=[]
    =================================
    0x149: v149(0x0) = CONST 
    0x14c: REVERT v149(0x0), v149(0x0)

    Begin block 0x14d
    prev=[0x12b], succ=[0x330]
    =================================
    0x154: v154(0x330) = CONST 
    0x157: JUMP v154(0x330)

    Begin block 0x330
    prev=[0x14d], succ=[0x6abB0x330]
    =================================
    0x331: v331(0x338) = CONST 
    0x334: v334(0x6ab) = CONST 
    0x337: JUMP v334(0x6ab)

    Begin block 0x6abB0x330
    prev=[0x330], succ=[0x338]
    =================================
    0x6acS0x330: v6acV330(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6cdS0x330: v6cdV330 = SLOAD v6acV330(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6cfS0x330: JUMP v331(0x338)

    Begin block 0x338
    prev=[0x6abB0x330], succ=[0x36c, 0x3f7]
    =================================
    0x339: v339(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x34e: v34e = AND v339(0xffffffffffffffffffffffffffffffffffffffff), v6cdV330
    0x34f: v34f = CALLER 
    0x350: v350(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x365: v365 = AND v350(0xffffffffffffffffffffffffffffffffffffffff), v34f
    0x366: v366 = EQ v365, v34e
    0x367: v367 = ISZERO v366
    0x368: v368(0x3f7) = CONST 
    0x36b: JUMPI v368(0x3f7), v367

    Begin block 0x36c
    prev=[0x338], succ=[0x374]
    =================================
    0x36c: v36c(0x374) = CONST 
    0x370: v370(0x6d0) = CONST 
    0x373: CALLPRIVATE v370(0x6d0), vf9, v36c(0x374)

    Begin block 0x374
    prev=[0x36c], succ=[0x3bd, 0x3de]
    =================================
    0x375: v375(0x0) = CONST 
    0x378: v378(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x38d: v38d = AND v378(0xffffffffffffffffffffffffffffffffffffffff), vf9
    0x390: v390(0x40) = CONST 
    0x392: v392 = MLOAD v390(0x40)
    0x399: CALLDATACOPY v392, v131, v12d
    0x39a: v39a(0x40) = CONST 
    0x39c: v39c = MLOAD v39a(0x40)
    0x39e: v39e = ADD v392, v12d
    0x3a1: v3a1(0x0) = CONST 
    0x3ab: v3ab = SUB v39e, v39c
    0x3ae: v3ae = GAS 
    0x3af: v3af = DELEGATECALL v3ae, v38d, v39c, v3ab, v39c, v3a1(0x0)
    0x3b3: v3b3 = RETURNDATASIZE 
    0x3b5: v3b5(0x0) = CONST 
    0x3b8: v3b8 = EQ v3b3, v3b5(0x0)
    0x3b9: v3b9(0x3de) = CONST 
    0x3bc: JUMPI v3b9(0x3de), v3b8

    Begin block 0x3bd
    prev=[0x374], succ=[0x3e3]
    =================================
    0x3bd: v3bd(0x40) = CONST 
    0x3bf: v3bf = MLOAD v3bd(0x40)
    0x3c2: v3c2(0x1f) = CONST 
    0x3c4: v3c4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3c2(0x1f)
    0x3c5: v3c5(0x3f) = CONST 
    0x3c7: v3c7 = RETURNDATASIZE 
    0x3c8: v3c8 = ADD v3c7, v3c5(0x3f)
    0x3c9: v3c9 = AND v3c8, v3c4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x3cb: v3cb = ADD v3bf, v3c9
    0x3cc: v3cc(0x40) = CONST 
    0x3ce: MSTORE v3cc(0x40), v3cb
    0x3cf: v3cf = RETURNDATASIZE 
    0x3d1: MSTORE v3bf, v3cf
    0x3d2: v3d2 = RETURNDATASIZE 
    0x3d3: v3d3(0x0) = CONST 
    0x3d5: v3d5(0x20) = CONST 
    0x3d8: v3d8 = ADD v3bf, v3d5(0x20)
    0x3d9: RETURNDATACOPY v3d8, v3d3(0x0), v3d2
    0x3da: v3da(0x3e3) = CONST 
    0x3dd: JUMP v3da(0x3e3)

    Begin block 0x3e3
    prev=[0x3bd, 0x3de], succ=[0x3ed, 0x3f1]
    =================================
    0x3e9: v3e9(0x3f1) = CONST 
    0x3ec: JUMPI v3e9(0x3f1), v3af

    Begin block 0x3ed
    prev=[0x3e3], succ=[]
    =================================
    0x3ed: v3ed(0x0) = CONST 
    0x3f0: REVERT v3ed(0x0), v3ed(0x0)

    Begin block 0x3f1
    prev=[0x3e3], succ=[0xb2f]
    =================================
    0x3f3: v3f3(0xb2f) = CONST 
    0x3f6: JUMP v3f3(0xb2f)

    Begin block 0xb2f
    prev=[0x3f1], succ=[0x9f8]
    =================================
    0xb33: JUMP vcc(0x9f8)

    Begin block 0x9f8
    prev=[0xb2f], succ=[]
    =================================
    0x9f9: STOP 

    Begin block 0x3de
    prev=[0x374], succ=[0x3e3]
    =================================
    0x3df: v3df(0x60) = CONST 

    Begin block 0x3f7
    prev=[0x338], succ=[0x71d0xcb]
    =================================
    0x3f8: v3f8(0xb53) = CONST 
    0x3fb: v3fb(0x71d) = CONST 
    0x3fe: JUMP v3fb(0x71d)

    Begin block 0x71d0xcb
    prev=[0x3f7], succ=[0x28eB0x71d0xcb]
    =================================
    0x71e0xcb: vcb71e(0x728) = CONST 
    0x7210xcb: vcb721(0xc05) = CONST 
    0x7240xcb: vcb724(0x28e) = CONST 
    0x7270xcb: JUMP vcb724(0x28e)

    Begin block 0x28eB0x71d0xcb
    prev=[0x71d0xcb], succ=[0xc050xcb]
    =================================
    0x28fS0x71d0xcb: v28fV71dcb(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2b0S0x71d0xcb: v2b0V71dcb = SLOAD v28fV71dcb(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2b2S0x71d0xcb: JUMP vcb721(0xc05)

    Begin block 0xc050xcb
    prev=[0x28eB0x71d0xcb], succ=[0x2b30xcb]
    =================================
    0xc060xcb: vcbc06(0x2b3) = CONST 
    0xc090xcb: JUMP vcbc06(0x2b3)

    Begin block 0x2b30xcb
    prev=[0xc050xcb], succ=[0x2ce0xcb, 0x2d20xcb]
    =================================
    0x2b40xcb: vcb2b4 = CALLDATASIZE 
    0x2b50xcb: vcb2b5(0x0) = CONST 
    0x2b80xcb: CALLDATACOPY vcb2b5(0x0), vcb2b5(0x0), vcb2b4
    0x2b90xcb: vcb2b9(0x0) = CONST 
    0x2bc0xcb: vcb2bc = CALLDATASIZE 
    0x2bd0xcb: vcb2bd(0x0) = CONST 
    0x2c00xcb: vcb2c0 = GAS 
    0x2c10xcb: vcb2c1 = DELEGATECALL vcb2c0, v2b0V71dcb, vcb2bd(0x0), vcb2bc, vcb2b9(0x0), vcb2b9(0x0)
    0x2c20xcb: vcb2c2 = RETURNDATASIZE 
    0x2c30xcb: vcb2c3(0x0) = CONST 
    0x2c60xcb: RETURNDATACOPY vcb2c3(0x0), vcb2c3(0x0), vcb2c2
    0x2c90xcb: vcb2c9 = ISZERO vcb2c1
    0x2ca0xcb: vcb2ca(0x2d2) = CONST 
    0x2cd0xcb: JUMPI vcb2ca(0x2d2), vcb2c9

    Begin block 0x2ce0xcb
    prev=[0x2b30xcb], succ=[]
    =================================
    0x2ce0xcb: vcb2ce = RETURNDATASIZE 
    0x2cf0xcb: vcb2cf(0x0) = CONST 
    0x2d10xcb: RETURN vcb2cf(0x0), vcb2ce

    Begin block 0x2d20xcb
    prev=[0x2b30xcb], succ=[]
    =================================
    0x2d30xcb: vcb2d3 = RETURNDATASIZE 
    0x2d40xcb: vcb2d4(0x0) = CONST 
    0x2d60xcb: REVERT vcb2d4(0x0), vcb2d3

}

