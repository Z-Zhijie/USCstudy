function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x43]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x43) = CONST 
    0xc: JUMPI v9(0x43), v8

    Begin block 0xd
    prev=[0x0], succ=[0x878, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x1ffc9a7) = CONST 
    0x19: v19 = EQ v14(0x1ffc9a7), v12
    0x86d: v86d(0x878) = CONST 
    0x86e: JUMPI v86d(0x878), v19

    Begin block 0x878
    prev=[0xd], succ=[]
    =================================
    0x879: v879(0x5a) = CONST 
    0x87a: CALLPRIVATE v879(0x5a)

    Begin block 0x1e
    prev=[0xd], succ=[0x87b, 0x29]
    =================================
    0x1f: v1f(0x31124171) = CONST 
    0x24: v24 = EQ v1f(0x31124171), v12
    0x86f: v86f(0x87b) = CONST 
    0x870: JUMPI v86f(0x87b), v24

    Begin block 0x87b
    prev=[0x1e], succ=[]
    =================================
    0x87c: v87c(0xba) = CONST 
    0x87d: CALLPRIVATE v87c(0xba)

    Begin block 0x29
    prev=[0x1e], succ=[0x87e, 0x34]
    =================================
    0x2a: v2a(0x8da5cb5b) = CONST 
    0x2f: v2f = EQ v2a(0x8da5cb5b), v12
    0x871: v871(0x87e) = CONST 
    0x872: JUMPI v871(0x87e), v2f

    Begin block 0x87e
    prev=[0x29], succ=[]
    =================================
    0x87f: v87f(0x147) = CONST 
    0x880: CALLPRIVATE v87f(0x147)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x881]
    =================================
    0x35: v35(0xf2fde38b) = CONST 
    0x3a: v3a = EQ v35(0xf2fde38b), v12
    0x873: v873(0x881) = CONST 
    0x874: JUMPI v873(0x881), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x52]
    =================================
    0x3f: v3f(0x52) = CONST 
    0x42: JUMP v3f(0x52)

    Begin block 0x52
    prev=[0x3f, 0x43], succ=[0x1ab0x0]
    =================================
    0x53: v53(0x751) = CONST 
    0x56: v56(0x1ab) = CONST 
    0x59: JUMP v56(0x1ab)

    Begin block 0x1ab0x0
    prev=[0x52], succ=[0x1e90x0, 0x1ec0x0]
    =================================
    0x1ac0x0: v01ac(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cd0x0: v01cd = SLOAD v01ac(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1ce0x0: v01ce(0x0) = CONST 
    0x1d00x0: v01d0 = CALLDATASIZE 
    0x1d30x0: CALLDATACOPY v01ce(0x0), v01ce(0x0), v01d0
    0x1d60x0: v01d6 = CALLDATASIZE 
    0x1d90x0: v01d9 = GAS 
    0x1da0x0: v01da = DELEGATECALL v01d9, v01cd, v01ce(0x0), v01d6, v01ce(0x0), v01ce(0x0)
    0x1dd0x0: v01dd = RETURNDATASIZE 
    0x1e10x0: RETURNDATACOPY v01ce(0x0), v01ce(0x0), v01dd
    0x1e40x0: v01e4 = ISZERO v01da
    0x1e50x0: v01e5(0x1ec) = CONST 
    0x1e80x0: JUMPI v01e5(0x1ec), v01e4

    Begin block 0x1e90x0
    prev=[0x1ab0x0], succ=[]
    =================================
    0x1eb0x0: RETURN v01ce(0x0), v01dd

    Begin block 0x1ec0x0
    prev=[0x1ab0x0], succ=[]
    =================================
    0x1ef0x0: REVERT v01ce(0x0), v01dd

    Begin block 0x881
    prev=[0x34], succ=[]
    =================================
    0x882: v882(0x178) = CONST 
    0x883: CALLPRIVATE v882(0x178)

    Begin block 0x43
    prev=[0x0], succ=[0x875, 0x52]
    =================================
    0x44: v44 = CALLDATASIZE 
    0x45: v45(0x52) = CONST 
    0x48: JUMPI v45(0x52), v44

    Begin block 0x875
    prev=[0x43], succ=[]
    =================================
    0x875: v875(0x877) = CONST 
    0x876: CALLPRIVATE v875(0x877)

}

function owner()() public {
    Begin block 0x147
    prev=[], succ=[0x14f, 0x153]
    =================================
    0x148: v148 = CALLVALUE 
    0x14a: v14a = ISZERO v148
    0x14b: v14b(0x153) = CONST 
    0x14e: JUMPI v14b(0x153), v14a

    Begin block 0x14f
    prev=[0x147], succ=[]
    =================================
    0x14f: v14f(0x0) = CONST 
    0x152: REVERT v14f(0x0), v14f(0x0)

    Begin block 0x153
    prev=[0x147], succ=[0x478B0x153]
    =================================
    0x155: v155(0x15c) = CONST 
    0x158: v158(0x478) = CONST 
    0x15b: JUMP v158(0x478)

    Begin block 0x478B0x153
    prev=[0x153], succ=[0x51aB0x478B0x153]
    =================================
    0x479S0x153: v479V153(0x0) = CONST 
    0x47bS0x153: v47bV153(0x482) = CONST 
    0x47eS0x153: v47eV153(0x51a) = CONST 
    0x481S0x153: JUMP v47eV153(0x51a)

    Begin block 0x51aB0x478B0x153
    prev=[0x478B0x153], succ=[0x482B0x153]
    =================================
    0x51bS0x478S0x153: v51bV478V153(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x53cS0x478S0x153: v53cV478V153 = SLOAD v51bV478V153(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x53eS0x478S0x153: JUMP v47bV153(0x482)

    Begin block 0x482B0x153
    prev=[0x51aB0x478B0x153], succ=[0x15c]
    =================================
    0x486S0x153: JUMP v155(0x15c)

    Begin block 0x15c
    prev=[0x482B0x153], succ=[]
    =================================
    0x15d: v15d(0x40) = CONST 
    0x160: v160 = MLOAD v15d(0x40)
    0x161: v161(0x1) = CONST 
    0x163: v163(0x1) = CONST 
    0x165: v165(0xa0) = CONST 
    0x167: v167(0x10000000000000000000000000000000000000000) = SHL v165(0xa0), v163(0x1)
    0x168: v168(0xffffffffffffffffffffffffffffffffffffffff) = SUB v167(0x10000000000000000000000000000000000000000), v161(0x1)
    0x16b: v16b = AND v53cV478V153, v168(0xffffffffffffffffffffffffffffffffffffffff)
    0x16d: MSTORE v160, v16b
    0x16e: v16e = MLOAD v15d(0x40)
    0x172: v172(0x0) = SUB v160, v16e
    0x173: v173(0x20) = CONST 
    0x175: v175(0x20) = ADD v173(0x20), v172(0x0)
    0x177: RETURN v16e, v175(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x178
    prev=[], succ=[0x180, 0x184]
    =================================
    0x179: v179 = CALLVALUE 
    0x17b: v17b = ISZERO v179
    0x17c: v17c(0x184) = CONST 
    0x17f: JUMPI v17c(0x184), v17b

    Begin block 0x180
    prev=[0x178], succ=[]
    =================================
    0x180: v180(0x0) = CONST 
    0x183: REVERT v180(0x0), v180(0x0)

    Begin block 0x184
    prev=[0x178], succ=[0x197, 0x19b]
    =================================
    0x186: v186(0x793) = CONST 
    0x189: v189(0x4) = CONST 
    0x18c: v18c = CALLDATASIZE 
    0x18d: v18d = SUB v18c, v189(0x4)
    0x18e: v18e(0x20) = CONST 
    0x191: v191 = LT v18d, v18e(0x20)
    0x192: v192 = ISZERO v191
    0x193: v193(0x19b) = CONST 
    0x196: JUMPI v193(0x19b), v192

    Begin block 0x197
    prev=[0x184], succ=[]
    =================================
    0x197: v197(0x0) = CONST 
    0x19a: REVERT v197(0x0), v197(0x0)

    Begin block 0x19b
    prev=[0x184], succ=[0x487]
    =================================
    0x19d: v19d = CALLDATALOAD v189(0x4)
    0x19e: v19e(0x1) = CONST 
    0x1a0: v1a0(0x1) = CONST 
    0x1a2: v1a2(0xa0) = CONST 
    0x1a4: v1a4(0x10000000000000000000000000000000000000000) = SHL v1a2(0xa0), v1a0(0x1)
    0x1a5: v1a5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a4(0x10000000000000000000000000000000000000000), v19e(0x1)
    0x1a6: v1a6 = AND v1a5(0xffffffffffffffffffffffffffffffffffffffff), v19d
    0x1a7: v1a7(0x487) = CONST 
    0x1aa: JUMP v1a7(0x487)

    Begin block 0x487
    prev=[0x19b], succ=[0x51aB0x487]
    =================================
    0x488: v488(0x48f) = CONST 
    0x48b: v48b(0x51a) = CONST 
    0x48e: JUMP v48b(0x51a)

    Begin block 0x51aB0x487
    prev=[0x487], succ=[0x48f]
    =================================
    0x51bS0x487: v51bV487(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x53cS0x487: v53cV487 = SLOAD v51bV487(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x53eS0x487: JUMP v488(0x48f)

    Begin block 0x48f
    prev=[0x51aB0x487], succ=[0x4a8, 0x50e]
    =================================
    0x490: v490(0x1) = CONST 
    0x492: v492(0x1) = CONST 
    0x494: v494(0xa0) = CONST 
    0x496: v496(0x10000000000000000000000000000000000000000) = SHL v494(0xa0), v492(0x1)
    0x497: v497(0xffffffffffffffffffffffffffffffffffffffff) = SUB v496(0x10000000000000000000000000000000000000000), v490(0x1)
    0x498: v498 = AND v497(0xffffffffffffffffffffffffffffffffffffffff), v53cV487
    0x499: v499 = CALLER 
    0x49a: v49a(0x1) = CONST 
    0x49c: v49c(0x1) = CONST 
    0x49e: v49e(0xa0) = CONST 
    0x4a0: v4a0(0x10000000000000000000000000000000000000000) = SHL v49e(0xa0), v49c(0x1)
    0x4a1: v4a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a0(0x10000000000000000000000000000000000000000), v49a(0x1)
    0x4a2: v4a2 = AND v4a1(0xffffffffffffffffffffffffffffffffffffffff), v499
    0x4a3: v4a3 = EQ v4a2, v498
    0x4a4: v4a4(0x50e) = CONST 
    0x4a7: JUMPI v4a4(0x50e), v4a3

    Begin block 0x4a8
    prev=[0x48f], succ=[]
    =================================
    0x4a8: v4a8(0x40) = CONST 
    0x4ab: v4ab = MLOAD v4a8(0x40)
    0x4ac: v4ac(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4ce: MSTORE v4ab, v4ac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4cf: v4cf(0x20) = CONST 
    0x4d1: v4d1(0x4) = CONST 
    0x4d4: v4d4 = ADD v4ab, v4d1(0x4)
    0x4d5: MSTORE v4d4, v4cf(0x20)
    0x4d6: v4d6(0xe) = CONST 
    0x4d8: v4d8(0x24) = CONST 
    0x4db: v4db = ADD v4ab, v4d8(0x24)
    0x4dc: MSTORE v4db, v4d6(0xe)
    0x4dd: v4dd(0x4e4f545f415554484f52495a4544000000000000000000000000000000000000) = CONST 
    0x4fe: v4fe(0x44) = CONST 
    0x501: v501 = ADD v4ab, v4fe(0x44)
    0x502: MSTORE v501, v4dd(0x4e4f545f415554484f52495a4544000000000000000000000000000000000000)
    0x504: v504 = MLOAD v4a8(0x40)
    0x508: v508(0x0) = SUB v4ab, v504
    0x509: v509(0x64) = CONST 
    0x50b: v50b(0x64) = ADD v509(0x64), v508(0x0)
    0x50d: REVERT v504, v50b(0x64)

    Begin block 0x50e
    prev=[0x48f], succ=[0x679]
    =================================
    0x50f: v50f(0x517) = CONST 
    0x513: v513(0x679) = CONST 
    0x516: JUMP v513(0x679)

    Begin block 0x679
    prev=[0x50e], succ=[0x51aB0x679]
    =================================
    0x67a: v67a(0x0) = CONST 
    0x67c: v67c(0x683) = CONST 
    0x67f: v67f(0x51a) = CONST 
    0x682: JUMP v67f(0x51a)

    Begin block 0x51aB0x679
    prev=[0x679], succ=[0x683]
    =================================
    0x51bS0x679: v51bV679(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x53cS0x679: v53cV679 = SLOAD v51bV679(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x53eS0x679: JUMP v67c(0x683)

    Begin block 0x683
    prev=[0x51aB0x679], succ=[0x517]
    =================================
    0x687: v687(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6a8: SSTORE v687(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v1a6
    0x6aa: v6aa(0x1) = CONST 
    0x6ac: v6ac(0x1) = CONST 
    0x6ae: v6ae(0xa0) = CONST 
    0x6b0: v6b0(0x10000000000000000000000000000000000000000) = SHL v6ae(0xa0), v6ac(0x1)
    0x6b1: v6b1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b0(0x10000000000000000000000000000000000000000), v6aa(0x1)
    0x6b2: v6b2 = AND v6b1(0xffffffffffffffffffffffffffffffffffffffff), v1a6
    0x6b4: v6b4(0x1) = CONST 
    0x6b6: v6b6(0x1) = CONST 
    0x6b8: v6b8(0xa0) = CONST 
    0x6ba: v6ba(0x10000000000000000000000000000000000000000) = SHL v6b8(0xa0), v6b6(0x1)
    0x6bb: v6bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ba(0x10000000000000000000000000000000000000000), v6b4(0x1)
    0x6bc: v6bc = AND v6bb(0xffffffffffffffffffffffffffffffffffffffff), v53cV679
    0x6bd: v6bd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x6de: v6de(0x40) = CONST 
    0x6e0: v6e0 = MLOAD v6de(0x40)
    0x6e1: v6e1(0x40) = CONST 
    0x6e3: v6e3 = MLOAD v6e1(0x40)
    0x6e6: v6e6(0x0) = SUB v6e0, v6e3
    0x6e8: LOG3 v6e3, v6e6(0x0), v6bd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v6bc, v6b2
    0x6eb: JUMP v50f(0x517)

    Begin block 0x517
    prev=[0x683], succ=[0x793]
    =================================
    0x519: JUMP v186(0x793)

    Begin block 0x793
    prev=[0x517], succ=[]
    =================================
    0x794: STOP 

}

function supportsInterface(bytes4)() public {
    Begin block 0x5a
    prev=[], succ=[0x62, 0x66]
    =================================
    0x5b: v5b = CALLVALUE 
    0x5d: v5d = ISZERO v5b
    0x5e: v5e(0x66) = CONST 
    0x61: JUMPI v5e(0x66), v5d

    Begin block 0x62
    prev=[0x5a], succ=[]
    =================================
    0x62: v62(0x0) = CONST 
    0x65: REVERT v62(0x0), v62(0x0)

    Begin block 0x66
    prev=[0x5a], succ=[0x79, 0x7d]
    =================================
    0x68: v68(0xa6) = CONST 
    0x6b: v6b(0x4) = CONST 
    0x6e: v6e = CALLDATASIZE 
    0x6f: v6f = SUB v6e, v6b(0x4)
    0x70: v70(0x20) = CONST 
    0x73: v73 = LT v6f, v70(0x20)
    0x74: v74 = ISZERO v73
    0x75: v75(0x7d) = CONST 
    0x78: JUMPI v75(0x7d), v74

    Begin block 0x79
    prev=[0x66], succ=[]
    =================================
    0x79: v79(0x0) = CONST 
    0x7c: REVERT v79(0x0), v79(0x0)

    Begin block 0x7d
    prev=[0x66], succ=[0x1f6]
    =================================
    0x7f: v7f = CALLDATALOAD v6b(0x4)
    0x80: v80(0xffffffff00000000000000000000000000000000000000000000000000000000) = CONST 
    0xa1: va1 = AND v80(0xffffffff00000000000000000000000000000000000000000000000000000000), v7f
    0xa2: va2(0x1f6) = CONST 
    0xa5: JUMP va2(0x1f6)

    Begin block 0x1f6
    prev=[0x7d], succ=[0x289, 0x243]
    =================================
    0x1f7: v1f7(0x0) = CONST 
    0x1f9: v1f9(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = CONST 
    0x21a: v21a(0xffffffff00000000000000000000000000000000000000000000000000000000) = CONST 
    0x23c: v23c = AND va1, v21a(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x23d: v23d = EQ v23c, v1f9(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x23f: v23f(0x289) = CONST 
    0x242: JUMPI v23f(0x289), v23d

    Begin block 0x289
    prev=[0x1f6, 0x243], succ=[0x296, 0x28f]
    =================================
    0x289_0x0: v289_0 = PHI v23d, v288
    0x28a: v28a = ISZERO v289_0
    0x28b: v28b(0x296) = CONST 
    0x28e: JUMPI v28b(0x296), v28a

    Begin block 0x296
    prev=[0x289], succ=[0x2c8, 0x2c1]
    =================================
    0x297: v297(0xffffffff00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ba: v2ba = AND va1, v297(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x2bb: v2bb = EQ v2ba, v297(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x2bc: v2bc = ISZERO v2bb
    0x2bd: v2bd(0x2c8) = CONST 
    0x2c0: JUMPI v2bd(0x2c8), v2bc

    Begin block 0x2c8
    prev=[0x296], succ=[0x367, 0x36b]
    =================================
    0x2c9: v2c9(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x2ea: v2ea = SLOAD v2c9(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x2eb: v2eb(0x40) = CONST 
    0x2ee: v2ee = MLOAD v2eb(0x40)
    0x2ef: v2ef(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = CONST 
    0x311: MSTORE v2ee, v2ef(0x1ffc9a700000000000000000000000000000000000000000000000000000000)
    0x312: v312(0xffffffff00000000000000000000000000000000000000000000000000000000) = CONST 
    0x334: v334 = AND va1, v312(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x335: v335(0x4) = CONST 
    0x338: v338 = ADD v2ee, v335(0x4)
    0x339: MSTORE v338, v334
    0x33b: v33b = MLOAD v2eb(0x40)
    0x33c: v33c(0x1) = CONST 
    0x33e: v33e(0x1) = CONST 
    0x340: v340(0xa0) = CONST 
    0x342: v342(0x10000000000000000000000000000000000000000) = SHL v340(0xa0), v33e(0x1)
    0x343: v343(0xffffffffffffffffffffffffffffffffffffffff) = SUB v342(0x10000000000000000000000000000000000000000), v33c(0x1)
    0x345: v345 = AND v2ea, v343(0xffffffffffffffffffffffffffffffffffffffff)
    0x347: v347(0x1ffc9a7) = CONST 
    0x34d: v34d(0x24) = CONST 
    0x351: v351 = ADD v2ee, v34d(0x24)
    0x353: v353(0x20) = CONST 
    0x35a: v35a(0x0) = SUB v2ee, v33b
    0x35b: v35b(0x24) = ADD v35a(0x0), v34d(0x24)
    0x35f: v35f = EXTCODESIZE v345
    0x360: v360 = ISZERO v35f
    0x362: v362 = ISZERO v360
    0x363: v363(0x36b) = CONST 
    0x366: JUMPI v363(0x36b), v362

    Begin block 0x367
    prev=[0x2c8], succ=[]
    =================================
    0x367: v367(0x0) = CONST 
    0x36a: REVERT v367(0x0), v367(0x0)

    Begin block 0x36b
    prev=[0x2c8], succ=[0x390, 0x379]
    =================================
    0x36d: v36d = GAS 
    0x36e: v36e = STATICCALL v36d, v345, v33b, v35b(0x24), v33b, v353(0x20)
    0x374: v374 = ISZERO v36e
    0x375: v375(0x390) = CONST 
    0x378: JUMPI v375(0x390), v374

    Begin block 0x390
    prev=[0x36b, 0x38b], succ=[0x395, 0x39e]
    =================================
    0x390_0x0: v390_0 = PHI v36e, v38e(0x1)
    0x391: v391(0x39e) = CONST 
    0x394: JUMPI v391(0x39e), v390_0

    Begin block 0x395
    prev=[0x390], succ=[0x7fc]
    =================================
    0x395: v395(0x0) = CONST 
    0x39a: v39a(0x7fc) = CONST 
    0x39d: JUMP v39a(0x7fc)

    Begin block 0x7fc
    prev=[0x395], succ=[0xa6]
    =================================
    0x7fc_0x2: v7fc_2 = PHI v68(0xa6), va1
    0x800: JUMP v7fc_2

    Begin block 0xa6
    prev=[0x7b4, 0x7d8, 0x7fc, 0x820], succ=[]
    =================================
    0xa6_0x0: va6_0 = PHI v290(0x1), v2c2(0x0), v2ea, v38d, v395(0x0)
    0xa7: va7(0x40) = CONST 
    0xaa: vaa = MLOAD va7(0x40)
    0xac: vac = ISZERO va6_0
    0xad: vad = ISZERO vac
    0xaf: MSTORE vaa, vad
    0xb0: vb0 = MLOAD va7(0x40)
    0xb4: vb4(0x0) = SUB vaa, vb0
    0xb5: vb5(0x20) = CONST 
    0xb7: vb7(0x20) = ADD vb5(0x20), vb4(0x0)
    0xb9: RETURN vb0, vb7(0x20)

    Begin block 0x39e
    prev=[0x390], succ=[0x820]
    =================================
    0x3a1: v3a1(0x820) = CONST 
    0x3a6: JUMP v3a1(0x820)

    Begin block 0x820
    prev=[0x39e], succ=[0xa6]
    =================================
    0x824: JUMP v68(0xa6)

    Begin block 0x379
    prev=[0x36b], succ=[0x387, 0x38b]
    =================================
    0x37a: v37a(0x40) = CONST 
    0x37c: v37c = MLOAD v37a(0x40)
    0x37d: v37d = RETURNDATASIZE 
    0x37e: v37e(0x20) = CONST 
    0x381: v381 = LT v37d, v37e(0x20)
    0x382: v382 = ISZERO v381
    0x383: v383(0x38b) = CONST 
    0x386: JUMPI v383(0x38b), v382

    Begin block 0x387
    prev=[0x379], succ=[]
    =================================
    0x387: v387(0x0) = CONST 
    0x38a: REVERT v387(0x0), v387(0x0)

    Begin block 0x38b
    prev=[0x379], succ=[0x390]
    =================================
    0x38d: v38d = MLOAD v37c
    0x38e: v38e(0x1) = CONST 

    Begin block 0x2c1
    prev=[0x296], succ=[0x7d8]
    =================================
    0x2c2: v2c2(0x0) = CONST 
    0x2c4: v2c4(0x7d8) = CONST 
    0x2c7: JUMP v2c4(0x7d8)

    Begin block 0x7d8
    prev=[0x2c1], succ=[0xa6]
    =================================
    0x7dc: JUMP v68(0xa6)

    Begin block 0x28f
    prev=[0x289], succ=[0x7b4]
    =================================
    0x290: v290(0x1) = CONST 
    0x292: v292(0x7b4) = CONST 
    0x295: JUMP v292(0x7b4)

    Begin block 0x7b4
    prev=[0x28f], succ=[0xa6]
    =================================
    0x7b8: JUMP v68(0xa6)

    Begin block 0x243
    prev=[0x1f6], succ=[0x289]
    =================================
    0x244: v244(0x7f5828d000000000000000000000000000000000000000000000000000000000) = CONST 
    0x265: v265(0xffffffff00000000000000000000000000000000000000000000000000000000) = CONST 
    0x287: v287 = AND va1, v265(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x288: v288 = EQ v287, v244(0x7f5828d000000000000000000000000000000000000000000000000000000000)

}

function fallback()() public {
    Begin block 0x877
    prev=[], succ=[0x1ab0x877]
    =================================
    0x49: v49(0x730) = CONST 
    0x4c: v4c(0x1ab) = CONST 
    0x4f: JUMP v4c(0x1ab)

    Begin block 0x1ab0x877
    prev=[0x877], succ=[0x1e90x877, 0x1ec0x877]
    =================================
    0x1ac0x877: v8771ac(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cd0x877: v8771cd = SLOAD v8771ac(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1ce0x877: v8771ce(0x0) = CONST 
    0x1d00x877: v8771d0 = CALLDATASIZE 
    0x1d30x877: CALLDATACOPY v8771ce(0x0), v8771ce(0x0), v8771d0
    0x1d60x877: v8771d6 = CALLDATASIZE 
    0x1d90x877: v8771d9 = GAS 
    0x1da0x877: v8771da = DELEGATECALL v8771d9, v8771cd, v8771ce(0x0), v8771d6, v8771ce(0x0), v8771ce(0x0)
    0x1dd0x877: v8771dd = RETURNDATASIZE 
    0x1e10x877: RETURNDATACOPY v8771ce(0x0), v8771ce(0x0), v8771dd
    0x1e40x877: v8771e4 = ISZERO v8771da
    0x1e50x877: v8771e5(0x1ec) = CONST 
    0x1e80x877: JUMPI v8771e5(0x1ec), v8771e4

    Begin block 0x1e90x877
    prev=[0x1ab0x877], succ=[]
    =================================
    0x1eb0x877: RETURN v8771ce(0x0), v8771dd

    Begin block 0x1ec0x877
    prev=[0x1ab0x877], succ=[]
    =================================
    0x1ef0x877: REVERT v8771ce(0x0), v8771dd

}

function changeImplementation(address,bytes)() public {
    Begin block 0xba
    prev=[], succ=[0xc2, 0xc6]
    =================================
    0xbb: vbb = CALLVALUE 
    0xbd: vbd = ISZERO vbb
    0xbe: vbe(0xc6) = CONST 
    0xc1: JUMPI vbe(0xc6), vbd

    Begin block 0xc2
    prev=[0xba], succ=[]
    =================================
    0xc2: vc2(0x0) = CONST 
    0xc5: REVERT vc2(0x0), vc2(0x0)

    Begin block 0xc6
    prev=[0xba], succ=[0xd9, 0xdd]
    =================================
    0xc8: vc8(0x772) = CONST 
    0xcb: vcb(0x4) = CONST 
    0xce: vce = CALLDATASIZE 
    0xcf: vcf = SUB vce, vcb(0x4)
    0xd0: vd0(0x40) = CONST 
    0xd3: vd3 = LT vcf, vd0(0x40)
    0xd4: vd4 = ISZERO vd3
    0xd5: vd5(0xdd) = CONST 
    0xd8: JUMPI vd5(0xdd), vd4

    Begin block 0xd9
    prev=[0xc6], succ=[]
    =================================
    0xd9: vd9(0x0) = CONST 
    0xdc: REVERT vd9(0x0), vd9(0x0)

    Begin block 0xdd
    prev=[0xc6], succ=[0x104, 0x108]
    =================================
    0xde: vde(0x1) = CONST 
    0xe0: ve0(0x1) = CONST 
    0xe2: ve2(0xa0) = CONST 
    0xe4: ve4(0x10000000000000000000000000000000000000000) = SHL ve2(0xa0), ve0(0x1)
    0xe5: ve5(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve4(0x10000000000000000000000000000000000000000), vde(0x1)
    0xe7: ve7 = CALLDATALOAD vcb(0x4)
    0xe8: ve8 = AND ve7, ve5(0xffffffffffffffffffffffffffffffffffffffff)
    0xec: vec = ADD vcb(0x4), vcf
    0xee: vee(0x40) = CONST 
    0xf1: vf1(0x44) = ADD vcb(0x4), vee(0x40)
    0xf2: vf2(0x20) = CONST 
    0xf5: vf5(0x24) = ADD vcb(0x4), vf2(0x20)
    0xf6: vf6 = CALLDATALOAD vf5(0x24)
    0xf7: vf7(0x100000000) = CONST 
    0xfe: vfe = GT vf6, vf7(0x100000000)
    0xff: vff = ISZERO vfe
    0x100: v100(0x108) = CONST 
    0x103: JUMPI v100(0x108), vff

    Begin block 0x104
    prev=[0xdd], succ=[]
    =================================
    0x104: v104(0x0) = CONST 
    0x107: REVERT v104(0x0), v104(0x0)

    Begin block 0x108
    prev=[0xdd], succ=[0x116, 0x11a]
    =================================
    0x10a: v10a = ADD vcb(0x4), vf6
    0x10c: v10c(0x20) = CONST 
    0x10f: v10f = ADD v10a, v10c(0x20)
    0x110: v110 = GT v10f, vec
    0x111: v111 = ISZERO v110
    0x112: v112(0x11a) = CONST 
    0x115: JUMPI v112(0x11a), v111

    Begin block 0x116
    prev=[0x108], succ=[]
    =================================
    0x116: v116(0x0) = CONST 
    0x119: REVERT v116(0x0), v116(0x0)

    Begin block 0x11a
    prev=[0x108], succ=[0x138, 0x13c]
    =================================
    0x11c: v11c = CALLDATALOAD v10a
    0x11e: v11e(0x20) = CONST 
    0x120: v120 = ADD v11e(0x20), v10a
    0x123: v123(0x1) = CONST 
    0x126: v126 = MUL v11c, v123(0x1)
    0x128: v128 = ADD v120, v126
    0x129: v129 = GT v128, vec
    0x12a: v12a(0x100000000) = CONST 
    0x131: v131 = GT v11c, v12a(0x100000000)
    0x132: v132 = OR v131, v129
    0x133: v133 = ISZERO v132
    0x134: v134(0x13c) = CONST 
    0x137: JUMPI v134(0x13c), v133

    Begin block 0x138
    prev=[0x11a], succ=[]
    =================================
    0x138: v138(0x0) = CONST 
    0x13b: REVERT v138(0x0), v138(0x0)

    Begin block 0x13c
    prev=[0x11a], succ=[0x3ac]
    =================================
    0x143: v143(0x3ac) = CONST 
    0x146: JUMP v143(0x3ac)

    Begin block 0x3ac
    prev=[0x13c], succ=[0x51aB0x3ac]
    =================================
    0x3ad: v3ad(0x3b4) = CONST 
    0x3b0: v3b0(0x51a) = CONST 
    0x3b3: JUMP v3b0(0x51a)

    Begin block 0x51aB0x3ac
    prev=[0x3ac], succ=[0x3b4]
    =================================
    0x51bS0x3ac: v51bV3ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x53cS0x3ac: v53cV3ac = SLOAD v51bV3ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x53eS0x3ac: JUMP v3ad(0x3b4)

    Begin block 0x3b4
    prev=[0x51aB0x3ac], succ=[0x3cd, 0x433]
    =================================
    0x3b5: v3b5(0x1) = CONST 
    0x3b7: v3b7(0x1) = CONST 
    0x3b9: v3b9(0xa0) = CONST 
    0x3bb: v3bb(0x10000000000000000000000000000000000000000) = SHL v3b9(0xa0), v3b7(0x1)
    0x3bc: v3bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3bb(0x10000000000000000000000000000000000000000), v3b5(0x1)
    0x3bd: v3bd = AND v3bc(0xffffffffffffffffffffffffffffffffffffffff), v53cV3ac
    0x3be: v3be = CALLER 
    0x3bf: v3bf(0x1) = CONST 
    0x3c1: v3c1(0x1) = CONST 
    0x3c3: v3c3(0xa0) = CONST 
    0x3c5: v3c5(0x10000000000000000000000000000000000000000) = SHL v3c3(0xa0), v3c1(0x1)
    0x3c6: v3c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c5(0x10000000000000000000000000000000000000000), v3bf(0x1)
    0x3c7: v3c7 = AND v3c6(0xffffffffffffffffffffffffffffffffffffffff), v3be
    0x3c8: v3c8 = EQ v3c7, v3bd
    0x3c9: v3c9(0x433) = CONST 
    0x3cc: JUMPI v3c9(0x433), v3c8

    Begin block 0x3cd
    prev=[0x3b4], succ=[]
    =================================
    0x3cd: v3cd(0x40) = CONST 
    0x3d0: v3d0 = MLOAD v3cd(0x40)
    0x3d1: v3d1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3f3: MSTORE v3d0, v3d1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3f4: v3f4(0x20) = CONST 
    0x3f6: v3f6(0x4) = CONST 
    0x3f9: v3f9 = ADD v3d0, v3f6(0x4)
    0x3fa: MSTORE v3f9, v3f4(0x20)
    0x3fb: v3fb(0xe) = CONST 
    0x3fd: v3fd(0x24) = CONST 
    0x400: v400 = ADD v3d0, v3fd(0x24)
    0x401: MSTORE v400, v3fb(0xe)
    0x402: v402(0x4e4f545f415554484f52495a4544000000000000000000000000000000000000) = CONST 
    0x423: v423(0x44) = CONST 
    0x426: v426 = ADD v3d0, v423(0x44)
    0x427: MSTORE v426, v402(0x4e4f545f415554484f52495a4544000000000000000000000000000000000000)
    0x429: v429 = MLOAD v3cd(0x40)
    0x42d: v42d(0x0) = SUB v3d0, v429
    0x42e: v42e(0x64) = CONST 
    0x430: v430(0x64) = ADD v42e(0x64), v42d(0x0)
    0x432: REVERT v429, v430(0x64)

    Begin block 0x433
    prev=[0x3b4], succ=[0x53fB0x433]
    =================================
    0x434: v434(0x844) = CONST 
    0x43c: v43c(0x1f) = CONST 
    0x43e: v43e = ADD v43c(0x1f), v11c
    0x43f: v43f(0x20) = CONST 
    0x443: v443 = DIV v43e, v43f(0x20)
    0x444: v444 = MUL v443, v43f(0x20)
    0x445: v445(0x20) = CONST 
    0x447: v447 = ADD v445(0x20), v444
    0x448: v448(0x40) = CONST 
    0x44a: v44a = MLOAD v448(0x40)
    0x44d: v44d = ADD v44a, v447
    0x44e: v44e(0x40) = CONST 
    0x450: MSTORE v44e(0x40), v44d
    0x458: MSTORE v44a, v11c
    0x459: v459(0x20) = CONST 
    0x45b: v45b = ADD v459(0x20), v44a
    0x461: CALLDATACOPY v45b, v120, v11c
    0x462: v462(0x0) = CONST 
    0x465: v465 = ADD v45b, v11c
    0x469: MSTORE v465, v462(0x0)
    0x46b: v46b(0x53f) = CONST 
    0x472: JUMP v46b(0x53f), v44a, ve8, v434(0x844)

    Begin block 0x53fB0x433
    prev=[0x433], succ=[0x5a7B0x433, 0x868B0x433]
    =================================
    0x540S0x433: v540V433(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x562S0x433: v562V433 = SLOAD v540V433(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x566S0x433: SSTORE v540V433(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), ve8
    0x567S0x433: v567V433(0x40) = CONST 
    0x569S0x433: v569V433 = MLOAD v567V433(0x40)
    0x56aS0x433: v56aV433(0x1) = CONST 
    0x56cS0x433: v56cV433(0x1) = CONST 
    0x56eS0x433: v56eV433(0xa0) = CONST 
    0x570S0x433: v570V433(0x10000000000000000000000000000000000000000) = SHL v56eV433(0xa0), v56cV433(0x1)
    0x571S0x433: v571V433(0xffffffffffffffffffffffffffffffffffffffff) = SUB v570V433(0x10000000000000000000000000000000000000000), v56aV433(0x1)
    0x574S0x433: v574V433 = AND ve8, v571V433(0xffffffffffffffffffffffffffffffffffffffff)
    0x578S0x433: v578V433 = AND v562V433, v571V433(0xffffffffffffffffffffffffffffffffffffffff)
    0x57aS0x433: v57aV433(0x5570d70a002632a7b0b3c9304cc89efb62d8da9eca0dbd7752c83b7379068296) = CONST 
    0x59cS0x433: v59cV433(0x0) = CONST 
    0x59fS0x433: LOG3 v569V433, v59cV433(0x0), v57aV433(0x5570d70a002632a7b0b3c9304cc89efb62d8da9eca0dbd7752c83b7379068296), v578V433, v574V433
    0x5a1S0x433: v5a1V433 = MLOAD v44a
    0x5a2S0x433: v5a2V433 = ISZERO v5a1V433
    0x5a3S0x433: v5a3V433(0x868) = CONST 
    0x5a6S0x433: JUMPI v5a3V433(0x868), v5a2V433

    Begin block 0x5a7B0x433
    prev=[0x53fB0x433], succ=[0x5c3B0x433]
    =================================
    0x5a7S0x433: v5a7V433(0x0) = CONST 
    0x5aaS0x433: v5aaV433(0x1) = CONST 
    0x5acS0x433: v5acV433(0x1) = CONST 
    0x5aeS0x433: v5aeV433(0xa0) = CONST 
    0x5b0S0x433: v5b0V433(0x10000000000000000000000000000000000000000) = SHL v5aeV433(0xa0), v5acV433(0x1)
    0x5b1S0x433: v5b1V433(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5b0V433(0x10000000000000000000000000000000000000000), v5aaV433(0x1)
    0x5b2S0x433: v5b2V433 = AND v5b1V433(0xffffffffffffffffffffffffffffffffffffffff), ve8
    0x5b4S0x433: v5b4V433(0x40) = CONST 
    0x5b6S0x433: v5b6V433 = MLOAD v5b4V433(0x40)
    0x5baS0x433: v5baV433 = MLOAD v44a
    0x5bcS0x433: v5bcV433(0x20) = CONST 
    0x5beS0x433: v5beV433 = ADD v5bcV433(0x20), v44a

    Begin block 0x5c3B0x433
    prev=[0x5a7B0x433, 0x5ccB0x433], succ=[0x600B0x433, 0x5ccB0x433]
    =================================
    0x5c3_0x2S0x433: v5c3_2V433 = PHI v5baV433, v5f3V433
    0x5c4S0x433: v5c4V433(0x20) = CONST 
    0x5c7S0x433: v5c7V433 = LT v5c3_2V433, v5c4V433(0x20)
    0x5c8S0x433: v5c8V433(0x600) = CONST 
    0x5cbS0x433: JUMPI v5c8V433(0x600), v5c7V433

    Begin block 0x600B0x433
    prev=[0x5c3B0x433], succ=[0x63fB0x433, 0x660B0x433]
    =================================
    0x600_0x0S0x433: v600_0V433 = PHI v5beV433, v5fbV433
    0x600_0x1S0x433: v600_1V433 = PHI v5b6V433, v5f9V433
    0x600_0x2S0x433: v600_2V433 = PHI v5baV433, v5f3V433
    0x601S0x433: v601V433(0x1) = CONST 
    0x604S0x433: v604V433(0x20) = CONST 
    0x606S0x433: v606V433 = SUB v604V433(0x20), v600_2V433
    0x607S0x433: v607V433(0x100) = CONST 
    0x60aS0x433: v60aV433 = EXP v607V433(0x100), v606V433
    0x60bS0x433: v60bV433 = SUB v60aV433, v601V433(0x1)
    0x60dS0x433: v60dV433 = NOT v60bV433
    0x60fS0x433: v60fV433 = MLOAD v600_0V433
    0x610S0x433: v610V433 = AND v60fV433, v60dV433
    0x613S0x433: v613V433 = MLOAD v600_1V433
    0x614S0x433: v614V433 = AND v613V433, v60bV433
    0x617S0x433: v617V433 = OR v610V433, v614V433
    0x619S0x433: MSTORE v600_1V433, v617V433
    0x622S0x433: v622V433 = ADD v5baV433, v5b6V433
    0x626S0x433: v626V433(0x0) = CONST 
    0x628S0x433: v628V433(0x40) = CONST 
    0x62aS0x433: v62aV433 = MLOAD v628V433(0x40)
    0x62dS0x433: v62dV433 = SUB v622V433, v62aV433
    0x630S0x433: v630V433 = GAS 
    0x631S0x433: v631V433 = DELEGATECALL v630V433, v5b2V433, v62aV433, v62dV433, v62aV433, v626V433(0x0)
    0x635S0x433: v635V433 = RETURNDATASIZE 
    0x637S0x433: v637V433(0x0) = CONST 
    0x63aS0x433: v63aV433 = EQ v635V433, v637V433(0x0)
    0x63bS0x433: v63bV433(0x660) = CONST 
    0x63eS0x433: JUMPI v63bV433(0x660), v63aV433

    Begin block 0x63fB0x433
    prev=[0x600B0x433], succ=[0x665B0x433]
    =================================
    0x63fS0x433: v63fV433(0x40) = CONST 
    0x641S0x433: v641V433 = MLOAD v63fV433(0x40)
    0x644S0x433: v644V433(0x1f) = CONST 
    0x646S0x433: v646V433(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v644V433(0x1f)
    0x647S0x433: v647V433(0x3f) = CONST 
    0x649S0x433: v649V433 = RETURNDATASIZE 
    0x64aS0x433: v64aV433 = ADD v649V433, v647V433(0x3f)
    0x64bS0x433: v64bV433 = AND v64aV433, v646V433(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x64dS0x433: v64dV433 = ADD v641V433, v64bV433
    0x64eS0x433: v64eV433(0x40) = CONST 
    0x650S0x433: MSTORE v64eV433(0x40), v64dV433
    0x651S0x433: v651V433 = RETURNDATASIZE 
    0x653S0x433: MSTORE v641V433, v651V433
    0x654S0x433: v654V433 = RETURNDATASIZE 
    0x655S0x433: v655V433(0x0) = CONST 
    0x657S0x433: v657V433(0x20) = CONST 
    0x65aS0x433: v65aV433 = ADD v641V433, v657V433(0x20)
    0x65bS0x433: RETURNDATACOPY v65aV433, v655V433(0x0), v654V433
    0x65cS0x433: v65cV433(0x665) = CONST 
    0x65fS0x433: JUMP v65cV433(0x665)

    Begin block 0x665B0x433
    prev=[0x63fB0x433, 0x660B0x433], succ=[0x66fB0x433, 0x1f0B0x433]
    =================================
    0x66bS0x433: v66bV433(0x1f0) = CONST 
    0x66eS0x433: JUMPI v66bV433(0x1f0), v631V433

    Begin block 0x66fB0x433
    prev=[0x665B0x433], succ=[]
    =================================
    0x66fS0x433: v66fV433 = RETURNDATASIZE 
    0x671S0x433: v671V433(0x0) = CONST 
    0x674S0x433: RETURNDATACOPY v671V433(0x0), v671V433(0x0), v66fV433
    0x676S0x433: v676V433(0x0) = CONST 
    0x678S0x433: REVERT v676V433(0x0), v66fV433

    Begin block 0x1f0B0x433
    prev=[0x665B0x433], succ=[0x844]
    =================================
    0x1f5S0x433: JUMP v434(0x844)

    Begin block 0x844
    prev=[0x868B0x433, 0x1f0B0x433], succ=[0x772]
    =================================
    0x848: JUMP vc8(0x772)

    Begin block 0x772
    prev=[0x844], succ=[]
    =================================
    0x773: STOP 

    Begin block 0x660B0x433
    prev=[0x600B0x433], succ=[0x665B0x433]
    =================================
    0x661S0x433: v661V433(0x60) = CONST 

    Begin block 0x5ccB0x433
    prev=[0x5c3B0x433], succ=[0x5c3B0x433]
    =================================
    0x5cc_0x0S0x433: v5cc_0V433 = PHI v5beV433, v5fbV433
    0x5cc_0x1S0x433: v5cc_1V433 = PHI v5b6V433, v5f9V433
    0x5cc_0x2S0x433: v5cc_2V433 = PHI v5baV433, v5f3V433
    0x5cdS0x433: v5cdV433 = MLOAD v5cc_0V433
    0x5cfS0x433: MSTORE v5cc_1V433, v5cdV433
    0x5d0S0x433: v5d0V433(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = CONST 
    0x5f3S0x433: v5f3V433 = ADD v5cc_2V433, v5d0V433(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x5f5S0x433: v5f5V433(0x20) = CONST 
    0x5f9S0x433: v5f9V433 = ADD v5f5V433(0x20), v5cc_1V433
    0x5fbS0x433: v5fbV433 = ADD v5f5V433(0x20), v5cc_0V433
    0x5fcS0x433: v5fcV433(0x5c3) = CONST 
    0x5ffS0x433: JUMP v5fcV433(0x5c3)

    Begin block 0x868B0x433
    prev=[0x53fB0x433], succ=[0x844]
    =================================
    0x86cS0x433: JUMP v434(0x844)

}

