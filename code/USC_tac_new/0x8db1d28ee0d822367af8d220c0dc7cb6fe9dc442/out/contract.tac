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
    prev=[0x0], succ=[0x876, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x3659cfe6) = CONST 
    0x19: v19 = EQ v14(0x3659cfe6), v12
    0x869: v869(0x876) = CONST 
    0x86a: JUMPI v869(0x876), v19

    Begin block 0x876
    prev=[0xd], succ=[]
    =================================
    0x877: v877(0x70) = CONST 
    0x878: CALLPRIVATE v877(0x70)

    Begin block 0x1e
    prev=[0xd], succ=[0x879, 0x29]
    =================================
    0x1f: v1f(0x4f1ef286) = CONST 
    0x24: v24 = EQ v1f(0x4f1ef286), v12
    0x86b: v86b(0x879) = CONST 
    0x86c: JUMPI v86b(0x879), v24

    Begin block 0x879
    prev=[0x1e], succ=[]
    =================================
    0x87a: v87a(0xa3) = CONST 
    0x87b: CALLPRIVATE v87a(0xa3)

    Begin block 0x29
    prev=[0x1e], succ=[0x87c, 0x34]
    =================================
    0x2a: v2a(0x5c60da1b) = CONST 
    0x2f: v2f = EQ v2a(0x5c60da1b), v12
    0x86d: v86d(0x87c) = CONST 
    0x86e: JUMPI v86d(0x87c), v2f

    Begin block 0x87c
    prev=[0x29], succ=[]
    =================================
    0x87d: v87d(0x123) = CONST 
    0x87e: CALLPRIVATE v87d(0x123)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x87f]
    =================================
    0x35: v35(0x8f283970) = CONST 
    0x3a: v3a = EQ v35(0x8f283970), v12
    0x86f: v86f(0x87f) = CONST 
    0x870: JUMPI v86f(0x87f), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x882]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x871: v871(0x882) = CONST 
    0x872: JUMPI v871(0x882), v45

    Begin block 0x4a
    prev=[0x3f], succ=[0x65]
    =================================
    0x4a: v4a(0x65) = CONST 
    0x4d: JUMP v4a(0x65)

    Begin block 0x65
    prev=[0x4a, 0x4e], succ=[0x19cB0x65]
    =================================
    0x66: v66(0x676) = CONST 
    0x69: v69(0x697) = CONST 
    0x6c: v6c(0x19c) = CONST 
    0x6f: JUMP v6c(0x19c)

    Begin block 0x19cB0x65
    prev=[0x65], succ=[0x697]
    =================================
    0x19dS0x65: v19dV65(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x65: v1beV65 = SLOAD v19dV65(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x65: JUMP v69(0x697)

    Begin block 0x697
    prev=[0x19cB0x65], succ=[0x1c10x0]
    =================================
    0x698: v698(0x1c1) = CONST 
    0x69b: JUMP v698(0x1c1)

    Begin block 0x1c10x0
    prev=[0x697], succ=[0x1dc0x0, 0x1e00x0]
    =================================
    0x1c20x0: v01c2 = CALLDATASIZE 
    0x1c30x0: v01c3(0x0) = CONST 
    0x1c60x0: CALLDATACOPY v01c3(0x0), v01c3(0x0), v01c2
    0x1c70x0: v01c7(0x0) = CONST 
    0x1ca0x0: v01ca = CALLDATASIZE 
    0x1cb0x0: v01cb(0x0) = CONST 
    0x1ce0x0: v01ce = GAS 
    0x1cf0x0: v01cf = DELEGATECALL v01ce, v1beV65, v01cb(0x0), v01ca, v01c7(0x0), v01c7(0x0)
    0x1d00x0: v01d0 = RETURNDATASIZE 
    0x1d10x0: v01d1(0x0) = CONST 
    0x1d40x0: RETURNDATACOPY v01d1(0x0), v01d1(0x0), v01d0
    0x1d70x0: v01d7 = ISZERO v01cf
    0x1d80x0: v01d8(0x1e0) = CONST 
    0x1db0x0: JUMPI v01d8(0x1e0), v01d7

    Begin block 0x1dc0x0
    prev=[0x1c10x0], succ=[]
    =================================
    0x1dc0x0: v01dc = RETURNDATASIZE 
    0x1dd0x0: v01dd(0x0) = CONST 
    0x1df0x0: RETURN v01dd(0x0), v01dc

    Begin block 0x1e00x0
    prev=[0x1c10x0], succ=[]
    =================================
    0x1e10x0: v01e1 = RETURNDATASIZE 
    0x1e20x0: v01e2(0x0) = CONST 
    0x1e40x0: REVERT v01e2(0x0), v01e1

    Begin block 0x882
    prev=[0x3f], succ=[]
    =================================
    0x883: v883(0x187) = CONST 
    0x884: CALLPRIVATE v883(0x187)

    Begin block 0x87f
    prev=[0x34], succ=[]
    =================================
    0x880: v880(0x154) = CONST 
    0x881: CALLPRIVATE v880(0x154)

    Begin block 0x4e
    prev=[0x0], succ=[0x873, 0x65]
    =================================
    0x4f: v4f = CALLDATASIZE 
    0x50: v50(0x65) = CONST 
    0x53: JUMPI v50(0x65), v4f

    Begin block 0x873
    prev=[0x4e], succ=[]
    =================================
    0x873: v873(0x875) = CONST 
    0x874: CALLPRIVATE v873(0x875)

}

function implementation()() public {
    Begin block 0x123
    prev=[], succ=[0x12b, 0x12f]
    =================================
    0x124: v124 = CALLVALUE 
    0x126: v126 = ISZERO v124
    0x127: v127(0x12f) = CONST 
    0x12a: JUMPI v127(0x12f), v126

    Begin block 0x12b
    prev=[0x123], succ=[]
    =================================
    0x12b: v12b(0x0) = CONST 
    0x12e: REVERT v12b(0x0), v12b(0x0)

    Begin block 0x12f
    prev=[0x123], succ=[0x6fd]
    =================================
    0x131: v131(0x6fd) = CONST 
    0x134: v134(0x2cc) = CONST 
    0x137: v137_0 = CALLPRIVATE v134(0x2cc), v131(0x6fd)

    Begin block 0x6fd
    prev=[0x12f], succ=[]
    =================================
    0x6fe: v6fe(0x40) = CONST 
    0x701: v701 = MLOAD v6fe(0x40)
    0x702: v702(0x1) = CONST 
    0x704: v704(0x1) = CONST 
    0x706: v706(0xa0) = CONST 
    0x708: v708(0x10000000000000000000000000000000000000000) = SHL v706(0xa0), v704(0x1)
    0x709: v709(0xffffffffffffffffffffffffffffffffffffffff) = SUB v708(0x10000000000000000000000000000000000000000), v702(0x1)
    0x70c: v70c = AND v137_0, v709(0xffffffffffffffffffffffffffffffffffffffff)
    0x70e: MSTORE v701, v70c
    0x70f: v70f = MLOAD v6fe(0x40)
    0x713: v713(0x0) = SUB v701, v70f
    0x714: v714(0x20) = CONST 
    0x716: v716(0x20) = ADD v714(0x20), v713(0x0)
    0x718: RETURN v70f, v716(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x154
    prev=[], succ=[0x15c, 0x160]
    =================================
    0x155: v155 = CALLVALUE 
    0x157: v157 = ISZERO v155
    0x158: v158(0x160) = CONST 
    0x15b: JUMPI v158(0x160), v157

    Begin block 0x15c
    prev=[0x154], succ=[]
    =================================
    0x15c: v15c(0x0) = CONST 
    0x15f: REVERT v15c(0x0), v15c(0x0)

    Begin block 0x160
    prev=[0x154], succ=[0x173, 0x177]
    =================================
    0x162: v162(0x738) = CONST 
    0x165: v165(0x4) = CONST 
    0x168: v168 = CALLDATASIZE 
    0x169: v169 = SUB v168, v165(0x4)
    0x16a: v16a(0x20) = CONST 
    0x16d: v16d = LT v169, v16a(0x20)
    0x16e: v16e = ISZERO v16d
    0x16f: v16f(0x177) = CONST 
    0x172: JUMPI v16f(0x177), v16e

    Begin block 0x173
    prev=[0x160], succ=[]
    =================================
    0x173: v173(0x0) = CONST 
    0x176: REVERT v173(0x0), v173(0x0)

    Begin block 0x177
    prev=[0x160], succ=[0x309]
    =================================
    0x179: v179 = CALLDATALOAD v165(0x4)
    0x17a: v17a(0x1) = CONST 
    0x17c: v17c(0x1) = CONST 
    0x17e: v17e(0xa0) = CONST 
    0x180: v180(0x10000000000000000000000000000000000000000) = SHL v17e(0xa0), v17c(0x1)
    0x181: v181(0xffffffffffffffffffffffffffffffffffffffff) = SUB v180(0x10000000000000000000000000000000000000000), v17a(0x1)
    0x182: v182 = AND v181(0xffffffffffffffffffffffffffffffffffffffff), v179
    0x183: v183(0x309) = CONST 
    0x186: JUMP v183(0x309)

    Begin block 0x309
    prev=[0x177], succ=[0x3fdB0x309]
    =================================
    0x30a: v30a(0x311) = CONST 
    0x30d: v30d(0x3fd) = CONST 
    0x310: JUMP v30d(0x3fd)

    Begin block 0x3fdB0x309
    prev=[0x309], succ=[0x311]
    =================================
    0x3feS0x309: v3feV309(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x309: v41fV309 = SLOAD v3feV309(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x309: JUMP v30a(0x311)

    Begin block 0x311
    prev=[0x3fdB0x309], succ=[0x32b, 0x2190x154]
    =================================
    0x312: v312(0x1) = CONST 
    0x314: v314(0x1) = CONST 
    0x316: v316(0xa0) = CONST 
    0x318: v318(0x10000000000000000000000000000000000000000) = SHL v316(0xa0), v314(0x1)
    0x319: v319(0xffffffffffffffffffffffffffffffffffffffff) = SUB v318(0x10000000000000000000000000000000000000000), v312(0x1)
    0x31a: v31a = AND v319(0xffffffffffffffffffffffffffffffffffffffff), v41fV309
    0x31b: v31b = CALLER 
    0x31c: v31c(0x1) = CONST 
    0x31e: v31e(0x1) = CONST 
    0x320: v320(0xa0) = CONST 
    0x322: v322(0x10000000000000000000000000000000000000000) = SHL v320(0xa0), v31e(0x1)
    0x323: v323(0xffffffffffffffffffffffffffffffffffffffff) = SUB v322(0x10000000000000000000000000000000000000000), v31c(0x1)
    0x324: v324 = AND v323(0xffffffffffffffffffffffffffffffffffffffff), v31b
    0x325: v325 = EQ v324, v31a
    0x326: v326 = ISZERO v325
    0x327: v327(0x219) = CONST 
    0x32a: JUMPI v327(0x219), v326

    Begin block 0x32b
    prev=[0x311], succ=[0x3fdB0x32b]
    =================================
    0x32b: v32b(0x332) = CONST 
    0x32e: v32e(0x3fd) = CONST 
    0x331: JUMP v32e(0x3fd)

    Begin block 0x3fdB0x32b
    prev=[0x32b], succ=[0x332]
    =================================
    0x3feS0x32b: v3feV32b(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x32b: v41fV32b = SLOAD v3feV32b(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x32b: JUMP v32b(0x332)

    Begin block 0x332
    prev=[0x3fdB0x32b], succ=[0x34c, 0x382]
    =================================
    0x333: v333(0x1) = CONST 
    0x335: v335(0x1) = CONST 
    0x337: v337(0xa0) = CONST 
    0x339: v339(0x10000000000000000000000000000000000000000) = SHL v337(0xa0), v335(0x1)
    0x33a: v33a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v339(0x10000000000000000000000000000000000000000), v333(0x1)
    0x33b: v33b = AND v33a(0xffffffffffffffffffffffffffffffffffffffff), v41fV32b
    0x33d: v33d(0x1) = CONST 
    0x33f: v33f(0x1) = CONST 
    0x341: v341(0xa0) = CONST 
    0x343: v343(0x10000000000000000000000000000000000000000) = SHL v341(0xa0), v33f(0x1)
    0x344: v344(0xffffffffffffffffffffffffffffffffffffffff) = SUB v343(0x10000000000000000000000000000000000000000), v33d(0x1)
    0x345: v345 = AND v344(0xffffffffffffffffffffffffffffffffffffffff), v182
    0x346: v346 = EQ v345, v33b
    0x347: v347 = ISZERO v346
    0x348: v348(0x382) = CONST 
    0x34b: JUMPI v348(0x382), v347

    Begin block 0x34c
    prev=[0x332], succ=[]
    =================================
    0x34c: v34c(0x40) = CONST 
    0x34e: v34e = MLOAD v34c(0x40)
    0x34f: v34f(0x461bcd) = CONST 
    0x353: v353(0xe5) = CONST 
    0x355: v355(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v353(0xe5), v34f(0x461bcd)
    0x357: MSTORE v34e, v355(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x358: v358(0x4) = CONST 
    0x35a: v35a = ADD v358(0x4), v34e
    0x35d: v35d(0x20) = CONST 
    0x35f: v35f = ADD v35d(0x20), v35a
    0x362: v362(0x20) = SUB v35f, v35a
    0x364: MSTORE v35a, v362(0x20)
    0x365: v365(0x23) = CONST 
    0x368: MSTORE v35f, v365(0x23)
    0x369: v369(0x20) = CONST 
    0x36b: v36b = ADD v369(0x20), v35f
    0x36d: v36d(0x582) = CONST 
    0x370: v370(0x23) = CONST 
    0x373: CODECOPY v36b, v36d(0x582), v370(0x23)
    0x374: v374(0x40) = CONST 
    0x376: v376 = ADD v374(0x40), v36b
    0x37a: v37a(0x40) = CONST 
    0x37c: v37c = MLOAD v37a(0x40)
    0x37f: v37f(0x84) = SUB v376, v37c
    0x381: REVERT v37c, v37f(0x84)

    Begin block 0x382
    prev=[0x332], succ=[0x3fdB0x382]
    =================================
    0x383: v383(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x3a4: v3a4(0x3ab) = CONST 
    0x3a7: v3a7(0x3fd) = CONST 
    0x3aa: JUMP v3a7(0x3fd)

    Begin block 0x3fdB0x382
    prev=[0x382], succ=[0x3ab]
    =================================
    0x3feS0x382: v3feV382(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x382: v41fV382 = SLOAD v3feV382(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x382: JUMP v3a4(0x3ab)

    Begin block 0x3ab
    prev=[0x3fdB0x382], succ=[0x46f]
    =================================
    0x3ac: v3ac(0x40) = CONST 
    0x3af: v3af = MLOAD v3ac(0x40)
    0x3b0: v3b0(0x1) = CONST 
    0x3b2: v3b2(0x1) = CONST 
    0x3b4: v3b4(0xa0) = CONST 
    0x3b6: v3b6(0x10000000000000000000000000000000000000000) = SHL v3b4(0xa0), v3b2(0x1)
    0x3b7: v3b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b6(0x10000000000000000000000000000000000000000), v3b0(0x1)
    0x3ba: v3ba = AND v3b7(0xffffffffffffffffffffffffffffffffffffffff), v41fV382
    0x3bc: MSTORE v3af, v3ba
    0x3bf: v3bf = AND v182, v3b7(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c0: v3c0(0x20) = CONST 
    0x3c3: v3c3 = ADD v3af, v3c0(0x20)
    0x3c4: MSTORE v3c3, v3bf
    0x3c6: v3c6 = MLOAD v3ac(0x40)
    0x3ca: v3ca(0x0) = SUB v3af, v3c6
    0x3cb: v3cb(0x40) = ADD v3ca(0x0), v3ac(0x40)
    0x3cd: LOG1 v3c6, v3cb(0x40), v383(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x3ce: v3ce(0x214) = CONST 
    0x3d2: v3d2(0x46f) = CONST 
    0x3d5: JUMP v3d2(0x46f)

    Begin block 0x46f
    prev=[0x3ab], succ=[0x49f, 0x4d5]
    =================================
    0x470: v470(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x491: v491(0x1) = CONST 
    0x493: v493(0x1) = CONST 
    0x495: v495(0xa0) = CONST 
    0x497: v497(0x10000000000000000000000000000000000000000) = SHL v495(0xa0), v493(0x1)
    0x498: v498(0xffffffffffffffffffffffffffffffffffffffff) = SUB v497(0x10000000000000000000000000000000000000000), v491(0x1)
    0x49a: v49a = AND v182, v498(0xffffffffffffffffffffffffffffffffffffffff)
    0x49b: v49b(0x4d5) = CONST 
    0x49e: JUMPI v49b(0x4d5), v49a

    Begin block 0x49f
    prev=[0x46f], succ=[]
    =================================
    0x49f: v49f(0x40) = CONST 
    0x4a1: v4a1 = MLOAD v49f(0x40)
    0x4a2: v4a2(0x461bcd) = CONST 
    0x4a6: v4a6(0xe5) = CONST 
    0x4a8: v4a8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v4a6(0xe5), v4a2(0x461bcd)
    0x4aa: MSTORE v4a1, v4a8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4ab: v4ab(0x4) = CONST 
    0x4ad: v4ad = ADD v4ab(0x4), v4a1
    0x4b0: v4b0(0x20) = CONST 
    0x4b2: v4b2 = ADD v4b0(0x20), v4ad
    0x4b5: v4b5(0x20) = SUB v4b2, v4ad
    0x4b7: MSTORE v4ad, v4b5(0x20)
    0x4b8: v4b8(0x27) = CONST 
    0x4bb: MSTORE v4b2, v4b8(0x27)
    0x4bc: v4bc(0x20) = CONST 
    0x4be: v4be = ADD v4bc(0x20), v4b2
    0x4c0: v4c0(0x55b) = CONST 
    0x4c3: v4c3(0x27) = CONST 
    0x4c6: CODECOPY v4be, v4c0(0x55b), v4c3(0x27)
    0x4c7: v4c7(0x40) = CONST 
    0x4c9: v4c9 = ADD v4c7(0x40), v4be
    0x4cd: v4cd(0x40) = CONST 
    0x4cf: v4cf = MLOAD v4cd(0x40)
    0x4d2: v4d2(0x84) = SUB v4c9, v4cf
    0x4d4: REVERT v4cf, v4d2(0x84)

    Begin block 0x4d5
    prev=[0x46f], succ=[0x2140x154]
    =================================
    0x4d6: SSTORE v470(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v182
    0x4d7: JUMP v3ce(0x214)

    Begin block 0x2140x154
    prev=[0x4d5], succ=[0x7940x154]
    =================================
    0x2150x154: v154215(0x794) = CONST 
    0x2180x154: JUMP v154215(0x794)

    Begin block 0x7940x154
    prev=[0x2140x154], succ=[0x738]
    =================================
    0x7960x154: JUMP v162(0x738)

    Begin block 0x738
    prev=[0x7940x154], succ=[]
    =================================
    0x739: STOP 

    Begin block 0x2190x154
    prev=[0x311], succ=[0x4620x154]
    =================================
    0x21a0x154: v15421a(0x7b6) = CONST 
    0x21d0x154: v15421d(0x462) = CONST 
    0x2200x154: JUMP v15421d(0x462)

    Begin block 0x4620x154
    prev=[0x2190x154], succ=[0x19cB0x4620x154]
    =================================
    0x4630x154: v154463(0x46d) = CONST 
    0x4660x154: v154466(0x864) = CONST 
    0x4690x154: v154469(0x19c) = CONST 
    0x46c0x154: JUMP v154469(0x19c)

    Begin block 0x19cB0x4620x154
    prev=[0x4620x154], succ=[0x8640x154]
    =================================
    0x19dS0x4620x154: v19dV462154(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4620x154: v1beV462154 = SLOAD v19dV462154(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4620x154: JUMP v154466(0x864)

    Begin block 0x8640x154
    prev=[0x19cB0x4620x154], succ=[0x1c10x154]
    =================================
    0x8650x154: v154865(0x1c1) = CONST 
    0x8680x154: JUMP v154865(0x1c1)

    Begin block 0x1c10x154
    prev=[0x8640x154], succ=[0x1dc0x154, 0x1e00x154]
    =================================
    0x1c20x154: v1541c2 = CALLDATASIZE 
    0x1c30x154: v1541c3(0x0) = CONST 
    0x1c60x154: CALLDATACOPY v1541c3(0x0), v1541c3(0x0), v1541c2
    0x1c70x154: v1541c7(0x0) = CONST 
    0x1ca0x154: v1541ca = CALLDATASIZE 
    0x1cb0x154: v1541cb(0x0) = CONST 
    0x1ce0x154: v1541ce = GAS 
    0x1cf0x154: v1541cf = DELEGATECALL v1541ce, v1beV462154, v1541cb(0x0), v1541ca, v1541c7(0x0), v1541c7(0x0)
    0x1d00x154: v1541d0 = RETURNDATASIZE 
    0x1d10x154: v1541d1(0x0) = CONST 
    0x1d40x154: RETURNDATACOPY v1541d1(0x0), v1541d1(0x0), v1541d0
    0x1d70x154: v1541d7 = ISZERO v1541cf
    0x1d80x154: v1541d8(0x1e0) = CONST 
    0x1db0x154: JUMPI v1541d8(0x1e0), v1541d7

    Begin block 0x1dc0x154
    prev=[0x1c10x154], succ=[]
    =================================
    0x1dc0x154: v1541dc = RETURNDATASIZE 
    0x1dd0x154: v1541dd(0x0) = CONST 
    0x1df0x154: RETURN v1541dd(0x0), v1541dc

    Begin block 0x1e00x154
    prev=[0x1c10x154], succ=[]
    =================================
    0x1e10x154: v1541e1 = RETURNDATASIZE 
    0x1e20x154: v1541e2(0x0) = CONST 
    0x1e40x154: REVERT v1541e2(0x0), v1541e1

}

function admin()() public {
    Begin block 0x187
    prev=[], succ=[0x18f, 0x193]
    =================================
    0x188: v188 = CALLVALUE 
    0x18a: v18a = ISZERO v188
    0x18b: v18b(0x193) = CONST 
    0x18e: JUMPI v18b(0x193), v18a

    Begin block 0x18f
    prev=[0x187], succ=[]
    =================================
    0x18f: v18f(0x0) = CONST 
    0x192: REVERT v18f(0x0), v18f(0x0)

    Begin block 0x193
    prev=[0x187], succ=[0x759]
    =================================
    0x195: v195(0x759) = CONST 
    0x198: v198(0x3d6) = CONST 
    0x19b: v19b_0 = CALLPRIVATE v198(0x3d6), v195(0x759)

    Begin block 0x759
    prev=[0x193], succ=[]
    =================================
    0x75a: v75a(0x40) = CONST 
    0x75d: v75d = MLOAD v75a(0x40)
    0x75e: v75e(0x1) = CONST 
    0x760: v760(0x1) = CONST 
    0x762: v762(0xa0) = CONST 
    0x764: v764(0x10000000000000000000000000000000000000000) = SHL v762(0xa0), v760(0x1)
    0x765: v765(0xffffffffffffffffffffffffffffffffffffffff) = SUB v764(0x10000000000000000000000000000000000000000), v75e(0x1)
    0x768: v768 = AND v19b_0, v765(0xffffffffffffffffffffffffffffffffffffffff)
    0x76a: MSTORE v75d, v768
    0x76b: v76b = MLOAD v75a(0x40)
    0x76f: v76f(0x0) = SUB v75d, v76b
    0x770: v770(0x20) = CONST 
    0x772: v772(0x20) = ADD v770(0x20), v76f(0x0)
    0x774: RETURN v76b, v772(0x20)

}

function 0x2cc(0x2ccarg0x0) private {
    Begin block 0x2cc
    prev=[], succ=[0x3fdB0x2cc]
    =================================
    0x2cd: v2cd(0x0) = CONST 
    0x2cf: v2cf(0x2d6) = CONST 
    0x2d2: v2d2(0x3fd) = CONST 
    0x2d5: JUMP v2d2(0x3fd)

    Begin block 0x3fdB0x2cc
    prev=[0x2cc], succ=[0x2d6]
    =================================
    0x3feS0x2cc: v3feV2cc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x2cc: v41fV2cc = SLOAD v3feV2cc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x2cc: JUMP v2cf(0x2d6)

    Begin block 0x2d6
    prev=[0x3fdB0x2cc], succ=[0x2f0, 0x2fe0x2cc]
    =================================
    0x2d7: v2d7(0x1) = CONST 
    0x2d9: v2d9(0x1) = CONST 
    0x2db: v2db(0xa0) = CONST 
    0x2dd: v2dd(0x10000000000000000000000000000000000000000) = SHL v2db(0xa0), v2d9(0x1)
    0x2de: v2de(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2dd(0x10000000000000000000000000000000000000000), v2d7(0x1)
    0x2df: v2df = AND v2de(0xffffffffffffffffffffffffffffffffffffffff), v41fV2cc
    0x2e0: v2e0 = CALLER 
    0x2e1: v2e1(0x1) = CONST 
    0x2e3: v2e3(0x1) = CONST 
    0x2e5: v2e5(0xa0) = CONST 
    0x2e7: v2e7(0x10000000000000000000000000000000000000000) = SHL v2e5(0xa0), v2e3(0x1)
    0x2e8: v2e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e7(0x10000000000000000000000000000000000000000), v2e1(0x1)
    0x2e9: v2e9 = AND v2e8(0xffffffffffffffffffffffffffffffffffffffff), v2e0
    0x2ea: v2ea = EQ v2e9, v2df
    0x2eb: v2eb = ISZERO v2ea
    0x2ec: v2ec(0x2fe) = CONST 
    0x2ef: JUMPI v2ec(0x2fe), v2eb

    Begin block 0x2f0
    prev=[0x2d6], succ=[0x19cB0x2f0]
    =================================
    0x2f0: v2f0(0x2f7) = CONST 
    0x2f3: v2f3(0x19c) = CONST 
    0x2f6: JUMP v2f3(0x19c)

    Begin block 0x19cB0x2f0
    prev=[0x2f0], succ=[0x2f70x2cc]
    =================================
    0x19dS0x2f0: v19dV2f0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x2f0: v1beV2f0 = SLOAD v19dV2f0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x2f0: JUMP v2f0(0x2f7)

    Begin block 0x2f70x2cc
    prev=[0x19cB0x2f0], succ=[0x8200x2cc]
    =================================
    0x2fa0x2cc: v2cc2fa(0x820) = CONST 
    0x2fd0x2cc: JUMP v2cc2fa(0x820)

    Begin block 0x8200x2cc
    prev=[0x2f70x2cc], succ=[]
    =================================
    0x8220x2cc: RETURNPRIVATE v2ccarg0, v1beV2f0

    Begin block 0x2fe0x2cc
    prev=[0x2d6], succ=[0x4620x2cc]
    =================================
    0x2ff0x2cc: v2cc2ff(0x842) = CONST 
    0x3020x2cc: v2cc302(0x462) = CONST 
    0x3050x2cc: JUMP v2cc302(0x462)

    Begin block 0x4620x2cc
    prev=[0x2fe0x2cc], succ=[0x19cB0x4620x2cc]
    =================================
    0x4630x2cc: v2cc463(0x46d) = CONST 
    0x4660x2cc: v2cc466(0x864) = CONST 
    0x4690x2cc: v2cc469(0x19c) = CONST 
    0x46c0x2cc: JUMP v2cc469(0x19c)

    Begin block 0x19cB0x4620x2cc
    prev=[0x4620x2cc], succ=[0x8640x2cc]
    =================================
    0x19dS0x4620x2cc: v19dV4622cc(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4620x2cc: v1beV4622cc = SLOAD v19dV4622cc(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4620x2cc: JUMP v2cc466(0x864)

    Begin block 0x8640x2cc
    prev=[0x19cB0x4620x2cc], succ=[0x1c10x2cc]
    =================================
    0x8650x2cc: v2cc865(0x1c1) = CONST 
    0x8680x2cc: JUMP v2cc865(0x1c1)

    Begin block 0x1c10x2cc
    prev=[0x8640x2cc], succ=[0x1dc0x2cc, 0x1e00x2cc]
    =================================
    0x1c20x2cc: v2cc1c2 = CALLDATASIZE 
    0x1c30x2cc: v2cc1c3(0x0) = CONST 
    0x1c60x2cc: CALLDATACOPY v2cc1c3(0x0), v2cc1c3(0x0), v2cc1c2
    0x1c70x2cc: v2cc1c7(0x0) = CONST 
    0x1ca0x2cc: v2cc1ca = CALLDATASIZE 
    0x1cb0x2cc: v2cc1cb(0x0) = CONST 
    0x1ce0x2cc: v2cc1ce = GAS 
    0x1cf0x2cc: v2cc1cf = DELEGATECALL v2cc1ce, v1beV4622cc, v2cc1cb(0x0), v2cc1ca, v2cc1c7(0x0), v2cc1c7(0x0)
    0x1d00x2cc: v2cc1d0 = RETURNDATASIZE 
    0x1d10x2cc: v2cc1d1(0x0) = CONST 
    0x1d40x2cc: RETURNDATACOPY v2cc1d1(0x0), v2cc1d1(0x0), v2cc1d0
    0x1d70x2cc: v2cc1d7 = ISZERO v2cc1cf
    0x1d80x2cc: v2cc1d8(0x1e0) = CONST 
    0x1db0x2cc: JUMPI v2cc1d8(0x1e0), v2cc1d7

    Begin block 0x1dc0x2cc
    prev=[0x1c10x2cc], succ=[]
    =================================
    0x1dc0x2cc: v2cc1dc = RETURNDATASIZE 
    0x1dd0x2cc: v2cc1dd(0x0) = CONST 
    0x1df0x2cc: RETURN v2cc1dd(0x0), v2cc1dc

    Begin block 0x1e00x2cc
    prev=[0x1c10x2cc], succ=[]
    =================================
    0x1e10x2cc: v2cc1e1 = RETURNDATASIZE 
    0x1e20x2cc: v2cc1e2(0x0) = CONST 
    0x1e40x2cc: REVERT v2cc1e2(0x0), v2cc1e1

}

function 0x3d6(0x3d6arg0x0) private {
    Begin block 0x3d6
    prev=[], succ=[0x3fdB0x3d6]
    =================================
    0x3d7: v3d7(0x0) = CONST 
    0x3d9: v3d9(0x3e0) = CONST 
    0x3dc: v3dc(0x3fd) = CONST 
    0x3df: JUMP v3dc(0x3fd)

    Begin block 0x3fdB0x3d6
    prev=[0x3d6], succ=[0x3e0]
    =================================
    0x3feS0x3d6: v3feV3d6(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x3d6: v41fV3d6 = SLOAD v3feV3d6(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x3d6: JUMP v3d9(0x3e0)

    Begin block 0x3e0
    prev=[0x3fdB0x3d6], succ=[0x3fa, 0x2fe0x3d6]
    =================================
    0x3e1: v3e1(0x1) = CONST 
    0x3e3: v3e3(0x1) = CONST 
    0x3e5: v3e5(0xa0) = CONST 
    0x3e7: v3e7(0x10000000000000000000000000000000000000000) = SHL v3e5(0xa0), v3e3(0x1)
    0x3e8: v3e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3e7(0x10000000000000000000000000000000000000000), v3e1(0x1)
    0x3e9: v3e9 = AND v3e8(0xffffffffffffffffffffffffffffffffffffffff), v41fV3d6
    0x3ea: v3ea = CALLER 
    0x3eb: v3eb(0x1) = CONST 
    0x3ed: v3ed(0x1) = CONST 
    0x3ef: v3ef(0xa0) = CONST 
    0x3f1: v3f1(0x10000000000000000000000000000000000000000) = SHL v3ef(0xa0), v3ed(0x1)
    0x3f2: v3f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f1(0x10000000000000000000000000000000000000000), v3eb(0x1)
    0x3f3: v3f3 = AND v3f2(0xffffffffffffffffffffffffffffffffffffffff), v3ea
    0x3f4: v3f4 = EQ v3f3, v3e9
    0x3f5: v3f5 = ISZERO v3f4
    0x3f6: v3f6(0x2fe) = CONST 
    0x3f9: JUMPI v3f6(0x2fe), v3f5

    Begin block 0x3fa
    prev=[0x3e0], succ=[0x3fd0x3d6]
    =================================
    0x3fa: v3fa(0x2f7) = CONST 

    Begin block 0x3fd0x3d6
    prev=[0x3fa], succ=[0x2f70x3d6]
    =================================
    0x3fe0x3d6: v3d63fe(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41f0x3d6: v3d641f = SLOAD v3d63fe(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x4210x3d6: JUMP v3fa(0x2f7)

    Begin block 0x2f70x3d6
    prev=[0x3fd0x3d6], succ=[0x8200x3d6]
    =================================
    0x2fa0x3d6: v3d62fa(0x820) = CONST 
    0x2fd0x3d6: JUMP v3d62fa(0x820)

    Begin block 0x8200x3d6
    prev=[0x2f70x3d6], succ=[]
    =================================
    0x8220x3d6: RETURNPRIVATE v3d6arg0, v3d641f

    Begin block 0x2fe0x3d6
    prev=[0x3e0], succ=[0x4620x3d6]
    =================================
    0x2ff0x3d6: v3d62ff(0x842) = CONST 
    0x3020x3d6: v3d6302(0x462) = CONST 
    0x3050x3d6: JUMP v3d6302(0x462)

    Begin block 0x4620x3d6
    prev=[0x2fe0x3d6], succ=[0x19cB0x4620x3d6]
    =================================
    0x4630x3d6: v3d6463(0x46d) = CONST 
    0x4660x3d6: v3d6466(0x864) = CONST 
    0x4690x3d6: v3d6469(0x19c) = CONST 
    0x46c0x3d6: JUMP v3d6469(0x19c)

    Begin block 0x19cB0x4620x3d6
    prev=[0x4620x3d6], succ=[0x8640x3d6]
    =================================
    0x19dS0x4620x3d6: v19dV4623d6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4620x3d6: v1beV4623d6 = SLOAD v19dV4623d6(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4620x3d6: JUMP v3d6466(0x864)

    Begin block 0x8640x3d6
    prev=[0x19cB0x4620x3d6], succ=[0x1c10x3d6]
    =================================
    0x8650x3d6: v3d6865(0x1c1) = CONST 
    0x8680x3d6: JUMP v3d6865(0x1c1)

    Begin block 0x1c10x3d6
    prev=[0x8640x3d6], succ=[0x1dc0x3d6, 0x1e00x3d6]
    =================================
    0x1c20x3d6: v3d61c2 = CALLDATASIZE 
    0x1c30x3d6: v3d61c3(0x0) = CONST 
    0x1c60x3d6: CALLDATACOPY v3d61c3(0x0), v3d61c3(0x0), v3d61c2
    0x1c70x3d6: v3d61c7(0x0) = CONST 
    0x1ca0x3d6: v3d61ca = CALLDATASIZE 
    0x1cb0x3d6: v3d61cb(0x0) = CONST 
    0x1ce0x3d6: v3d61ce = GAS 
    0x1cf0x3d6: v3d61cf = DELEGATECALL v3d61ce, v1beV4623d6, v3d61cb(0x0), v3d61ca, v3d61c7(0x0), v3d61c7(0x0)
    0x1d00x3d6: v3d61d0 = RETURNDATASIZE 
    0x1d10x3d6: v3d61d1(0x0) = CONST 
    0x1d40x3d6: RETURNDATACOPY v3d61d1(0x0), v3d61d1(0x0), v3d61d0
    0x1d70x3d6: v3d61d7 = ISZERO v3d61cf
    0x1d80x3d6: v3d61d8(0x1e0) = CONST 
    0x1db0x3d6: JUMPI v3d61d8(0x1e0), v3d61d7

    Begin block 0x1dc0x3d6
    prev=[0x1c10x3d6], succ=[]
    =================================
    0x1dc0x3d6: v3d61dc = RETURNDATASIZE 
    0x1dd0x3d6: v3d61dd(0x0) = CONST 
    0x1df0x3d6: RETURN v3d61dd(0x0), v3d61dc

    Begin block 0x1e00x3d6
    prev=[0x1c10x3d6], succ=[]
    =================================
    0x1e10x3d6: v3d61e1 = RETURNDATASIZE 
    0x1e20x3d6: v3d61e2(0x0) = CONST 
    0x1e40x3d6: REVERT v3d61e2(0x0), v3d61e1

}

function 0x422(0x422arg0x0, 0x422arg0x1) private {
    Begin block 0x422
    prev=[], succ=[0x4d8]
    =================================
    0x423: v423(0x42b) = CONST 
    0x427: v427(0x4d8) = CONST 
    0x42a: JUMP v427(0x4d8)

    Begin block 0x4d8
    prev=[0x422], succ=[0x19cB0x4d8]
    =================================
    0x4d9: v4d9(0x0) = CONST 
    0x4db: v4db(0x4e2) = CONST 
    0x4de: v4de(0x19c) = CONST 
    0x4e1: JUMP v4de(0x19c)

    Begin block 0x19cB0x4d8
    prev=[0x4d8], succ=[0x4e2]
    =================================
    0x19dS0x4d8: v19dV4d8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4d8: v1beV4d8 = SLOAD v19dV4d8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4d8: JUMP v4db(0x4e2)

    Begin block 0x4e2
    prev=[0x19cB0x4d8], succ=[0x4ff, 0x535]
    =================================
    0x4e6: v4e6(0x1) = CONST 
    0x4e8: v4e8(0x1) = CONST 
    0x4ea: v4ea(0xa0) = CONST 
    0x4ec: v4ec(0x10000000000000000000000000000000000000000) = SHL v4ea(0xa0), v4e8(0x1)
    0x4ed: v4ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ec(0x10000000000000000000000000000000000000000), v4e6(0x1)
    0x4ee: v4ee = AND v4ed(0xffffffffffffffffffffffffffffffffffffffff), v422arg0
    0x4f0: v4f0(0x1) = CONST 
    0x4f2: v4f2(0x1) = CONST 
    0x4f4: v4f4(0xa0) = CONST 
    0x4f6: v4f6(0x10000000000000000000000000000000000000000) = SHL v4f4(0xa0), v4f2(0x1)
    0x4f7: v4f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f6(0x10000000000000000000000000000000000000000), v4f0(0x1)
    0x4f8: v4f8 = AND v4f7(0xffffffffffffffffffffffffffffffffffffffff), v1beV4d8
    0x4f9: v4f9 = EQ v4f8, v4ee
    0x4fa: v4fa = ISZERO v4f9
    0x4fb: v4fb(0x535) = CONST 
    0x4fe: JUMPI v4fb(0x535), v4fa

    Begin block 0x4ff
    prev=[0x4e2], succ=[]
    =================================
    0x4ff: v4ff(0x40) = CONST 
    0x501: v501 = MLOAD v4ff(0x40)
    0x502: v502(0x461bcd) = CONST 
    0x506: v506(0xe5) = CONST 
    0x508: v508(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v506(0xe5), v502(0x461bcd)
    0x50a: MSTORE v501, v508(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x50b: v50b(0x4) = CONST 
    0x50d: v50d = ADD v50b(0x4), v501
    0x510: v510(0x20) = CONST 
    0x512: v512 = ADD v510(0x20), v50d
    0x515: v515(0x20) = SUB v512, v50d
    0x517: MSTORE v50d, v515(0x20)
    0x518: v518(0x38) = CONST 
    0x51b: MSTORE v512, v518(0x38)
    0x51c: v51c(0x20) = CONST 
    0x51e: v51e = ADD v51c(0x20), v512
    0x520: v520(0x5a5) = CONST 
    0x523: v523(0x38) = CONST 
    0x526: CODECOPY v51e, v520(0x5a5), v523(0x38)
    0x527: v527(0x40) = CONST 
    0x529: v529 = ADD v527(0x40), v51e
    0x52d: v52d(0x40) = CONST 
    0x52f: v52f = MLOAD v52d(0x40)
    0x532: v532(0x84) = SUB v529, v52f
    0x534: REVERT v52f, v532(0x84)

    Begin block 0x535
    prev=[0x4e2], succ=[0x42b]
    =================================
    0x537: v537(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x558: SSTORE v537(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v422arg0
    0x559: JUMP v423(0x42b)

    Begin block 0x42b
    prev=[0x535], succ=[]
    =================================
    0x42c: v42c(0x40) = CONST 
    0x42e: v42e = MLOAD v42c(0x40)
    0x42f: v42f(0x1) = CONST 
    0x431: v431(0x1) = CONST 
    0x433: v433(0xa0) = CONST 
    0x435: v435(0x10000000000000000000000000000000000000000) = SHL v433(0xa0), v431(0x1)
    0x436: v436(0xffffffffffffffffffffffffffffffffffffffff) = SUB v435(0x10000000000000000000000000000000000000000), v42f(0x1)
    0x438: v438 = AND v422arg0, v436(0xffffffffffffffffffffffffffffffffffffffff)
    0x43a: v43a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x45c: v45c(0x0) = CONST 
    0x45f: LOG2 v42e, v45c(0x0), v43a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v438
    0x461: RETURNPRIVATE v422arg1

}

function upgradeTo(address)() public {
    Begin block 0x70
    prev=[], succ=[0x78, 0x7c]
    =================================
    0x71: v71 = CALLVALUE 
    0x73: v73 = ISZERO v71
    0x74: v74(0x7c) = CONST 
    0x77: JUMPI v74(0x7c), v73

    Begin block 0x78
    prev=[0x70], succ=[]
    =================================
    0x78: v78(0x0) = CONST 
    0x7b: REVERT v78(0x0), v78(0x0)

    Begin block 0x7c
    prev=[0x70], succ=[0x8f, 0x93]
    =================================
    0x7e: v7e(0x6bb) = CONST 
    0x81: v81(0x4) = CONST 
    0x84: v84 = CALLDATASIZE 
    0x85: v85 = SUB v84, v81(0x4)
    0x86: v86(0x20) = CONST 
    0x89: v89 = LT v85, v86(0x20)
    0x8a: v8a = ISZERO v89
    0x8b: v8b(0x93) = CONST 
    0x8e: JUMPI v8b(0x93), v8a

    Begin block 0x8f
    prev=[0x7c], succ=[]
    =================================
    0x8f: v8f(0x0) = CONST 
    0x92: REVERT v8f(0x0), v8f(0x0)

    Begin block 0x93
    prev=[0x7c], succ=[0x1ea]
    =================================
    0x95: v95 = CALLDATALOAD v81(0x4)
    0x96: v96(0x1) = CONST 
    0x98: v98(0x1) = CONST 
    0x9a: v9a(0xa0) = CONST 
    0x9c: v9c(0x10000000000000000000000000000000000000000) = SHL v9a(0xa0), v98(0x1)
    0x9d: v9d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9c(0x10000000000000000000000000000000000000000), v96(0x1)
    0x9e: v9e = AND v9d(0xffffffffffffffffffffffffffffffffffffffff), v95
    0x9f: v9f(0x1ea) = CONST 
    0xa2: JUMP v9f(0x1ea)

    Begin block 0x1ea
    prev=[0x93], succ=[0x3fdB0x1ea]
    =================================
    0x1eb: v1eb(0x1f2) = CONST 
    0x1ee: v1ee(0x3fd) = CONST 
    0x1f1: JUMP v1ee(0x3fd)

    Begin block 0x3fdB0x1ea
    prev=[0x1ea], succ=[0x1f2]
    =================================
    0x3feS0x1ea: v3feV1ea(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x1ea: v41fV1ea = SLOAD v3feV1ea(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x1ea: JUMP v1eb(0x1f2)

    Begin block 0x1f2
    prev=[0x3fdB0x1ea], succ=[0x20c, 0x2190x70]
    =================================
    0x1f3: v1f3(0x1) = CONST 
    0x1f5: v1f5(0x1) = CONST 
    0x1f7: v1f7(0xa0) = CONST 
    0x1f9: v1f9(0x10000000000000000000000000000000000000000) = SHL v1f7(0xa0), v1f5(0x1)
    0x1fa: v1fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f9(0x10000000000000000000000000000000000000000), v1f3(0x1)
    0x1fb: v1fb = AND v1fa(0xffffffffffffffffffffffffffffffffffffffff), v41fV1ea
    0x1fc: v1fc = CALLER 
    0x1fd: v1fd(0x1) = CONST 
    0x1ff: v1ff(0x1) = CONST 
    0x201: v201(0xa0) = CONST 
    0x203: v203(0x10000000000000000000000000000000000000000) = SHL v201(0xa0), v1ff(0x1)
    0x204: v204(0xffffffffffffffffffffffffffffffffffffffff) = SUB v203(0x10000000000000000000000000000000000000000), v1fd(0x1)
    0x205: v205 = AND v204(0xffffffffffffffffffffffffffffffffffffffff), v1fc
    0x206: v206 = EQ v205, v1fb
    0x207: v207 = ISZERO v206
    0x208: v208(0x219) = CONST 
    0x20b: JUMPI v208(0x219), v207

    Begin block 0x20c
    prev=[0x1f2], succ=[0x2140x70]
    =================================
    0x20c: v20c(0x214) = CONST 
    0x210: v210(0x422) = CONST 
    0x213: CALLPRIVATE v210(0x422), v9e, v20c(0x214)

    Begin block 0x2140x70
    prev=[0x20c], succ=[0x7940x70]
    =================================
    0x2150x70: v70215(0x794) = CONST 
    0x2180x70: JUMP v70215(0x794)

    Begin block 0x7940x70
    prev=[0x2140x70], succ=[0x6bb]
    =================================
    0x7960x70: JUMP v7e(0x6bb)

    Begin block 0x6bb
    prev=[0x7940x70], succ=[]
    =================================
    0x6bc: STOP 

    Begin block 0x2190x70
    prev=[0x1f2], succ=[0x4620x70]
    =================================
    0x21a0x70: v7021a(0x7b6) = CONST 
    0x21d0x70: v7021d(0x462) = CONST 
    0x2200x70: JUMP v7021d(0x462)

    Begin block 0x4620x70
    prev=[0x2190x70], succ=[0x19cB0x4620x70]
    =================================
    0x4630x70: v70463(0x46d) = CONST 
    0x4660x70: v70466(0x864) = CONST 
    0x4690x70: v70469(0x19c) = CONST 
    0x46c0x70: JUMP v70469(0x19c)

    Begin block 0x19cB0x4620x70
    prev=[0x4620x70], succ=[0x8640x70]
    =================================
    0x19dS0x4620x70: v19dV46270(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4620x70: v1beV46270 = SLOAD v19dV46270(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4620x70: JUMP v70466(0x864)

    Begin block 0x8640x70
    prev=[0x19cB0x4620x70], succ=[0x1c10x70]
    =================================
    0x8650x70: v70865(0x1c1) = CONST 
    0x8680x70: JUMP v70865(0x1c1)

    Begin block 0x1c10x70
    prev=[0x8640x70], succ=[0x1dc0x70, 0x1e00x70]
    =================================
    0x1c20x70: v701c2 = CALLDATASIZE 
    0x1c30x70: v701c3(0x0) = CONST 
    0x1c60x70: CALLDATACOPY v701c3(0x0), v701c3(0x0), v701c2
    0x1c70x70: v701c7(0x0) = CONST 
    0x1ca0x70: v701ca = CALLDATASIZE 
    0x1cb0x70: v701cb(0x0) = CONST 
    0x1ce0x70: v701ce = GAS 
    0x1cf0x70: v701cf = DELEGATECALL v701ce, v1beV46270, v701cb(0x0), v701ca, v701c7(0x0), v701c7(0x0)
    0x1d00x70: v701d0 = RETURNDATASIZE 
    0x1d10x70: v701d1(0x0) = CONST 
    0x1d40x70: RETURNDATACOPY v701d1(0x0), v701d1(0x0), v701d0
    0x1d70x70: v701d7 = ISZERO v701cf
    0x1d80x70: v701d8(0x1e0) = CONST 
    0x1db0x70: JUMPI v701d8(0x1e0), v701d7

    Begin block 0x1dc0x70
    prev=[0x1c10x70], succ=[]
    =================================
    0x1dc0x70: v701dc = RETURNDATASIZE 
    0x1dd0x70: v701dd(0x0) = CONST 
    0x1df0x70: RETURN v701dd(0x0), v701dc

    Begin block 0x1e00x70
    prev=[0x1c10x70], succ=[]
    =================================
    0x1e10x70: v701e1 = RETURNDATASIZE 
    0x1e20x70: v701e2(0x0) = CONST 
    0x1e40x70: REVERT v701e2(0x0), v701e1

}

function fallback()() public {
    Begin block 0x875
    prev=[], succ=[0x19cB0x875]
    =================================
    0x54: v54(0x631) = CONST 
    0x57: v57(0x652) = CONST 
    0x5a: v5a(0x19c) = CONST 
    0x5d: JUMP v5a(0x19c)

    Begin block 0x19cB0x875
    prev=[0x875], succ=[0x652]
    =================================
    0x19dS0x875: v19dV875(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x875: v1beV875 = SLOAD v19dV875(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x875: JUMP v57(0x652)

    Begin block 0x652
    prev=[0x19cB0x875], succ=[0x1c10x875]
    =================================
    0x653: v653(0x1c1) = CONST 
    0x656: JUMP v653(0x1c1)

    Begin block 0x1c10x875
    prev=[0x652], succ=[0x1dc0x875, 0x1e00x875]
    =================================
    0x1c20x875: v8751c2 = CALLDATASIZE 
    0x1c30x875: v8751c3(0x0) = CONST 
    0x1c60x875: CALLDATACOPY v8751c3(0x0), v8751c3(0x0), v8751c2
    0x1c70x875: v8751c7(0x0) = CONST 
    0x1ca0x875: v8751ca = CALLDATASIZE 
    0x1cb0x875: v8751cb(0x0) = CONST 
    0x1ce0x875: v8751ce = GAS 
    0x1cf0x875: v8751cf = DELEGATECALL v8751ce, v1beV875, v8751cb(0x0), v8751ca, v8751c7(0x0), v8751c7(0x0)
    0x1d00x875: v8751d0 = RETURNDATASIZE 
    0x1d10x875: v8751d1(0x0) = CONST 
    0x1d40x875: RETURNDATACOPY v8751d1(0x0), v8751d1(0x0), v8751d0
    0x1d70x875: v8751d7 = ISZERO v8751cf
    0x1d80x875: v8751d8(0x1e0) = CONST 
    0x1db0x875: JUMPI v8751d8(0x1e0), v8751d7

    Begin block 0x1dc0x875
    prev=[0x1c10x875], succ=[]
    =================================
    0x1dc0x875: v8751dc = RETURNDATASIZE 
    0x1dd0x875: v8751dd(0x0) = CONST 
    0x1df0x875: RETURN v8751dd(0x0), v8751dc

    Begin block 0x1e00x875
    prev=[0x1c10x875], succ=[]
    =================================
    0x1e10x875: v8751e1 = RETURNDATASIZE 
    0x1e20x875: v8751e2(0x0) = CONST 
    0x1e40x875: REVERT v8751e2(0x0), v8751e1

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xa3
    prev=[], succ=[0xb5, 0xb9]
    =================================
    0xa4: va4(0x6dc) = CONST 
    0xa7: va7(0x4) = CONST 
    0xaa: vaa = CALLDATASIZE 
    0xab: vab = SUB vaa, va7(0x4)
    0xac: vac(0x40) = CONST 
    0xaf: vaf = LT vab, vac(0x40)
    0xb0: vb0 = ISZERO vaf
    0xb1: vb1(0xb9) = CONST 
    0xb4: JUMPI vb1(0xb9), vb0

    Begin block 0xb5
    prev=[0xa3], succ=[]
    =================================
    0xb5: vb5(0x0) = CONST 
    0xb8: REVERT vb5(0x0), vb5(0x0)

    Begin block 0xb9
    prev=[0xa3], succ=[0xe0, 0xe4]
    =================================
    0xba: vba(0x1) = CONST 
    0xbc: vbc(0x1) = CONST 
    0xbe: vbe(0xa0) = CONST 
    0xc0: vc0(0x10000000000000000000000000000000000000000) = SHL vbe(0xa0), vbc(0x1)
    0xc1: vc1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc0(0x10000000000000000000000000000000000000000), vba(0x1)
    0xc3: vc3 = CALLDATALOAD va7(0x4)
    0xc4: vc4 = AND vc3, vc1(0xffffffffffffffffffffffffffffffffffffffff)
    0xc8: vc8 = ADD va7(0x4), vab
    0xca: vca(0x40) = CONST 
    0xcd: vcd(0x44) = ADD va7(0x4), vca(0x40)
    0xce: vce(0x20) = CONST 
    0xd1: vd1(0x24) = ADD va7(0x4), vce(0x20)
    0xd2: vd2 = CALLDATALOAD vd1(0x24)
    0xd3: vd3(0x100000000) = CONST 
    0xda: vda = GT vd2, vd3(0x100000000)
    0xdb: vdb = ISZERO vda
    0xdc: vdc(0xe4) = CONST 
    0xdf: JUMPI vdc(0xe4), vdb

    Begin block 0xe0
    prev=[0xb9], succ=[]
    =================================
    0xe0: ve0(0x0) = CONST 
    0xe3: REVERT ve0(0x0), ve0(0x0)

    Begin block 0xe4
    prev=[0xb9], succ=[0xf2, 0xf6]
    =================================
    0xe6: ve6 = ADD va7(0x4), vd2
    0xe8: ve8(0x20) = CONST 
    0xeb: veb = ADD ve6, ve8(0x20)
    0xec: vec = GT veb, vc8
    0xed: ved = ISZERO vec
    0xee: vee(0xf6) = CONST 
    0xf1: JUMPI vee(0xf6), ved

    Begin block 0xf2
    prev=[0xe4], succ=[]
    =================================
    0xf2: vf2(0x0) = CONST 
    0xf5: REVERT vf2(0x0), vf2(0x0)

    Begin block 0xf6
    prev=[0xe4], succ=[0x114, 0x118]
    =================================
    0xf8: vf8 = CALLDATALOAD ve6
    0xfa: vfa(0x20) = CONST 
    0xfc: vfc = ADD vfa(0x20), ve6
    0xff: vff(0x1) = CONST 
    0x102: v102 = MUL vf8, vff(0x1)
    0x104: v104 = ADD vfc, v102
    0x105: v105 = GT v104, vc8
    0x106: v106(0x100000000) = CONST 
    0x10d: v10d = GT vf8, v106(0x100000000)
    0x10e: v10e = OR v10d, v105
    0x10f: v10f = ISZERO v10e
    0x110: v110(0x118) = CONST 
    0x113: JUMPI v110(0x118), v10f

    Begin block 0x114
    prev=[0xf6], succ=[]
    =================================
    0x114: v114(0x0) = CONST 
    0x117: REVERT v114(0x0), v114(0x0)

    Begin block 0x118
    prev=[0xf6], succ=[0x224]
    =================================
    0x11f: v11f(0x224) = CONST 
    0x122: JUMP v11f(0x224)

    Begin block 0x224
    prev=[0x118], succ=[0x3fdB0x224]
    =================================
    0x225: v225(0x22c) = CONST 
    0x228: v228(0x3fd) = CONST 
    0x22b: JUMP v228(0x3fd)

    Begin block 0x3fdB0x224
    prev=[0x224], succ=[0x22c]
    =================================
    0x3feS0x224: v3feV224(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x41fS0x224: v41fV224 = SLOAD v3feV224(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x421S0x224: JUMP v225(0x22c)

    Begin block 0x22c
    prev=[0x3fdB0x224], succ=[0x246, 0x2c4]
    =================================
    0x22d: v22d(0x1) = CONST 
    0x22f: v22f(0x1) = CONST 
    0x231: v231(0xa0) = CONST 
    0x233: v233(0x10000000000000000000000000000000000000000) = SHL v231(0xa0), v22f(0x1)
    0x234: v234(0xffffffffffffffffffffffffffffffffffffffff) = SUB v233(0x10000000000000000000000000000000000000000), v22d(0x1)
    0x235: v235 = AND v234(0xffffffffffffffffffffffffffffffffffffffff), v41fV224
    0x236: v236 = CALLER 
    0x237: v237(0x1) = CONST 
    0x239: v239(0x1) = CONST 
    0x23b: v23b(0xa0) = CONST 
    0x23d: v23d(0x10000000000000000000000000000000000000000) = SHL v23b(0xa0), v239(0x1)
    0x23e: v23e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23d(0x10000000000000000000000000000000000000000), v237(0x1)
    0x23f: v23f = AND v23e(0xffffffffffffffffffffffffffffffffffffffff), v236
    0x240: v240 = EQ v23f, v235
    0x241: v241 = ISZERO v240
    0x242: v242(0x2c4) = CONST 
    0x245: JUMPI v242(0x2c4), v241

    Begin block 0x246
    prev=[0x22c], succ=[0x24e]
    =================================
    0x246: v246(0x24e) = CONST 
    0x24a: v24a(0x422) = CONST 
    0x24d: CALLPRIVATE v24a(0x422), vc4, v246(0x24e)

    Begin block 0x24e
    prev=[0x246], succ=[0x28a, 0x2ab]
    =================================
    0x24f: v24f(0x0) = CONST 
    0x252: v252(0x1) = CONST 
    0x254: v254(0x1) = CONST 
    0x256: v256(0xa0) = CONST 
    0x258: v258(0x10000000000000000000000000000000000000000) = SHL v256(0xa0), v254(0x1)
    0x259: v259(0xffffffffffffffffffffffffffffffffffffffff) = SUB v258(0x10000000000000000000000000000000000000000), v252(0x1)
    0x25a: v25a = AND v259(0xffffffffffffffffffffffffffffffffffffffff), vc4
    0x25d: v25d(0x40) = CONST 
    0x25f: v25f = MLOAD v25d(0x40)
    0x266: CALLDATACOPY v25f, vfc, vf8
    0x267: v267(0x40) = CONST 
    0x269: v269 = MLOAD v267(0x40)
    0x26b: v26b = ADD v25f, vf8
    0x26e: v26e(0x0) = CONST 
    0x278: v278 = SUB v26b, v269
    0x27b: v27b = GAS 
    0x27c: v27c = DELEGATECALL v27b, v25a, v269, v278, v269, v26e(0x0)
    0x280: v280 = RETURNDATASIZE 
    0x282: v282(0x0) = CONST 
    0x285: v285 = EQ v280, v282(0x0)
    0x286: v286(0x2ab) = CONST 
    0x289: JUMPI v286(0x2ab), v285

    Begin block 0x28a
    prev=[0x24e], succ=[0x2b0]
    =================================
    0x28a: v28a(0x40) = CONST 
    0x28c: v28c = MLOAD v28a(0x40)
    0x28f: v28f(0x1f) = CONST 
    0x291: v291(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v28f(0x1f)
    0x292: v292(0x3f) = CONST 
    0x294: v294 = RETURNDATASIZE 
    0x295: v295 = ADD v294, v292(0x3f)
    0x296: v296 = AND v295, v291(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x298: v298 = ADD v28c, v296
    0x299: v299(0x40) = CONST 
    0x29b: MSTORE v299(0x40), v298
    0x29c: v29c = RETURNDATASIZE 
    0x29e: MSTORE v28c, v29c
    0x29f: v29f = RETURNDATASIZE 
    0x2a0: v2a0(0x0) = CONST 
    0x2a2: v2a2(0x20) = CONST 
    0x2a5: v2a5 = ADD v28c, v2a2(0x20)
    0x2a6: RETURNDATACOPY v2a5, v2a0(0x0), v29f
    0x2a7: v2a7(0x2b0) = CONST 
    0x2aa: JUMP v2a7(0x2b0)

    Begin block 0x2b0
    prev=[0x28a, 0x2ab], succ=[0x2ba, 0x2be]
    =================================
    0x2b6: v2b6(0x2be) = CONST 
    0x2b9: JUMPI v2b6(0x2be), v27c

    Begin block 0x2ba
    prev=[0x2b0], succ=[]
    =================================
    0x2ba: v2ba(0x0) = CONST 
    0x2bd: REVERT v2ba(0x0), v2ba(0x0)

    Begin block 0x2be
    prev=[0x2b0], succ=[0x7d8]
    =================================
    0x2c0: v2c0(0x7d8) = CONST 
    0x2c3: JUMP v2c0(0x7d8)

    Begin block 0x7d8
    prev=[0x2be], succ=[0x6dc]
    =================================
    0x7dc: JUMP va4(0x6dc)

    Begin block 0x6dc
    prev=[0x7d8], succ=[]
    =================================
    0x6dd: STOP 

    Begin block 0x2ab
    prev=[0x24e], succ=[0x2b0]
    =================================
    0x2ac: v2ac(0x60) = CONST 

    Begin block 0x2c4
    prev=[0x22c], succ=[0x4620xa3]
    =================================
    0x2c5: v2c5(0x7fc) = CONST 
    0x2c8: v2c8(0x462) = CONST 
    0x2cb: JUMP v2c8(0x462)

    Begin block 0x4620xa3
    prev=[0x2c4], succ=[0x19cB0x4620xa3]
    =================================
    0x4630xa3: va3463(0x46d) = CONST 
    0x4660xa3: va3466(0x864) = CONST 
    0x4690xa3: va3469(0x19c) = CONST 
    0x46c0xa3: JUMP va3469(0x19c)

    Begin block 0x19cB0x4620xa3
    prev=[0x4620xa3], succ=[0x8640xa3]
    =================================
    0x19dS0x4620xa3: v19dV462a3(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1beS0x4620xa3: v1beV462a3 = SLOAD v19dV462a3(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1c0S0x4620xa3: JUMP va3466(0x864)

    Begin block 0x8640xa3
    prev=[0x19cB0x4620xa3], succ=[0x1c10xa3]
    =================================
    0x8650xa3: va3865(0x1c1) = CONST 
    0x8680xa3: JUMP va3865(0x1c1)

    Begin block 0x1c10xa3
    prev=[0x8640xa3], succ=[0x1dc0xa3, 0x1e00xa3]
    =================================
    0x1c20xa3: va31c2 = CALLDATASIZE 
    0x1c30xa3: va31c3(0x0) = CONST 
    0x1c60xa3: CALLDATACOPY va31c3(0x0), va31c3(0x0), va31c2
    0x1c70xa3: va31c7(0x0) = CONST 
    0x1ca0xa3: va31ca = CALLDATASIZE 
    0x1cb0xa3: va31cb(0x0) = CONST 
    0x1ce0xa3: va31ce = GAS 
    0x1cf0xa3: va31cf = DELEGATECALL va31ce, v1beV462a3, va31cb(0x0), va31ca, va31c7(0x0), va31c7(0x0)
    0x1d00xa3: va31d0 = RETURNDATASIZE 
    0x1d10xa3: va31d1(0x0) = CONST 
    0x1d40xa3: RETURNDATACOPY va31d1(0x0), va31d1(0x0), va31d0
    0x1d70xa3: va31d7 = ISZERO va31cf
    0x1d80xa3: va31d8(0x1e0) = CONST 
    0x1db0xa3: JUMPI va31d8(0x1e0), va31d7

    Begin block 0x1dc0xa3
    prev=[0x1c10xa3], succ=[]
    =================================
    0x1dc0xa3: va31dc = RETURNDATASIZE 
    0x1dd0xa3: va31dd(0x0) = CONST 
    0x1df0xa3: RETURN va31dd(0x0), va31dc

    Begin block 0x1e00xa3
    prev=[0x1c10xa3], succ=[]
    =================================
    0x1e10xa3: va31e1 = RETURNDATASIZE 
    0x1e20xa3: va31e2(0x0) = CONST 
    0x1e40xa3: REVERT va31e2(0x0), va31e1

}

