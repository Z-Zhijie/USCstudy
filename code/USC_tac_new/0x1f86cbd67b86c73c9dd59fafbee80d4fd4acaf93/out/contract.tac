function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x26a]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x262: v262(0x26a) = CONST 
    0x263: JUMPI v262(0x26a), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x26d]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x51720b41) = CONST 
    0x3b: v3b = EQ v34, v35(0x51720b41)
    0x264: v264(0x26d) = CONST 
    0x265: JUMPI v264(0x26d), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x270, 0x4b]
    =================================
    0x41: v41(0x92eefe9b) = CONST 
    0x46: v46 = EQ v41(0x92eefe9b), v34
    0x266: v266(0x270) = CONST 
    0x267: JUMPI v266(0x270), v46

    Begin block 0x270
    prev=[0x40], succ=[]
    =================================
    0x271: v271(0x14e) = CONST 
    0x272: CALLPRIVATE v271(0x14e)

    Begin block 0x4b
    prev=[0x40], succ=[0x26a, 0x273]
    =================================
    0x4c: v4c(0xf77c4791) = CONST 
    0x51: v51 = EQ v4c(0xf77c4791), v34
    0x268: v268(0x273) = CONST 
    0x269: JUMPI v268(0x273), v51

    Begin block 0x26a
    prev=[0x0, 0x4b], succ=[]
    =================================
    0x26b: v26b(0x56) = CONST 
    0x26c: CALLPRIVATE v26b(0x56)

    Begin block 0x273
    prev=[0x4b], succ=[]
    =================================
    0x274: v274(0x16f) = CONST 
    0x275: CALLPRIVATE v274(0x16f)

    Begin block 0x26d
    prev=[0xd], succ=[]
    =================================
    0x26e: v26e(0x129) = CONST 
    0x26f: CALLPRIVATE v26e(0x129)

}

function targetContractId()() public {
    Begin block 0x129
    prev=[], succ=[0x130, 0x134]
    =================================
    0x12a: v12a = CALLVALUE 
    0x12b: v12b = ISZERO v12a
    0x12c: v12c(0x134) = CONST 
    0x12f: JUMPI v12c(0x134), v12b

    Begin block 0x130
    prev=[0x129], succ=[]
    =================================
    0x130: v130(0x0) = CONST 
    0x133: REVERT v130(0x0), v130(0x0)

    Begin block 0x134
    prev=[0x129], succ=[0x19e]
    =================================
    0x135: v135(0x13c) = CONST 
    0x138: v138(0x19e) = CONST 
    0x13b: JUMP v138(0x19e)

    Begin block 0x19e
    prev=[0x134], succ=[0x13c]
    =================================
    0x19f: v19f(0x1) = CONST 
    0x1a1: v1a1 = SLOAD v19f(0x1)
    0x1a3: JUMP v135(0x13c)

    Begin block 0x13c
    prev=[0x19e], succ=[]
    =================================
    0x13d: v13d(0x40) = CONST 
    0x13f: v13f = MLOAD v13d(0x40)
    0x142: MSTORE v13f, v1a1
    0x143: v143(0x20) = CONST 
    0x145: v145 = ADD v143(0x20), v13f
    0x146: v146(0x40) = CONST 
    0x148: v148 = MLOAD v146(0x40)
    0x14b: v14b(0x20) = SUB v145, v148
    0x14d: RETURN v148, v14b(0x20)

}

function setController(address)() public {
    Begin block 0x14e
    prev=[], succ=[0x155, 0x159]
    =================================
    0x14f: v14f = CALLVALUE 
    0x150: v150 = ISZERO v14f
    0x151: v151(0x159) = CONST 
    0x154: JUMPI v151(0x159), v150

    Begin block 0x155
    prev=[0x14e], succ=[]
    =================================
    0x155: v155(0x0) = CONST 
    0x158: REVERT v155(0x0), v155(0x0)

    Begin block 0x159
    prev=[0x14e], succ=[0x1a4]
    =================================
    0x15a: v15a(0x16d) = CONST 
    0x15d: v15d(0x1) = CONST 
    0x15f: v15f(0xa0) = CONST 
    0x161: v161(0x2) = CONST 
    0x163: v163(0x10000000000000000000000000000000000000000) = EXP v161(0x2), v15f(0xa0)
    0x164: v164(0xffffffffffffffffffffffffffffffffffffffff) = SUB v163(0x10000000000000000000000000000000000000000), v15d(0x1)
    0x165: v165(0x4) = CONST 
    0x167: v167 = CALLDATALOAD v165(0x4)
    0x168: v168 = AND v167, v164(0xffffffffffffffffffffffffffffffffffffffff)
    0x169: v169(0x1a4) = CONST 
    0x16c: JUMP v169(0x1a4)

    Begin block 0x1a4
    prev=[0x159], succ=[0x1bb, 0x1bf]
    =================================
    0x1a5: v1a5(0x0) = CONST 
    0x1a7: v1a7 = SLOAD v1a5(0x0)
    0x1a8: v1a8 = CALLER 
    0x1a9: v1a9(0x1) = CONST 
    0x1ab: v1ab(0xa0) = CONST 
    0x1ad: v1ad(0x2) = CONST 
    0x1af: v1af(0x10000000000000000000000000000000000000000) = EXP v1ad(0x2), v1ab(0xa0)
    0x1b0: v1b0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1af(0x10000000000000000000000000000000000000000), v1a9(0x1)
    0x1b3: v1b3 = AND v1b0(0xffffffffffffffffffffffffffffffffffffffff), v1a8
    0x1b5: v1b5 = AND v1a7, v1b0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b6: v1b6 = EQ v1b5, v1b3
    0x1b7: v1b7(0x1bf) = CONST 
    0x1ba: JUMPI v1b7(0x1bf), v1b6

    Begin block 0x1bb
    prev=[0x1a4], succ=[]
    =================================
    0x1bb: v1bb(0x0) = CONST 
    0x1be: REVERT v1bb(0x0), v1bb(0x0)

    Begin block 0x1bf
    prev=[0x1a4], succ=[0x16d]
    =================================
    0x1c0: v1c0(0x0) = CONST 
    0x1c3: v1c3 = SLOAD v1c0(0x0)
    0x1c4: v1c4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d9: v1d9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x1da: v1da = AND v1d9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1c3
    0x1db: v1db(0x1) = CONST 
    0x1dd: v1dd(0xa0) = CONST 
    0x1df: v1df(0x2) = CONST 
    0x1e1: v1e1(0x10000000000000000000000000000000000000000) = EXP v1df(0x2), v1dd(0xa0)
    0x1e2: v1e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e1(0x10000000000000000000000000000000000000000), v1db(0x1)
    0x1e4: v1e4 = AND v168, v1e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e5: v1e5 = OR v1e4, v1da
    0x1e7: SSTORE v1c0(0x0), v1e5
    0x1e8: v1e8(0x4ff638452bbf33c012645d18ae6f05515ff5f2d1dfb0cece8cbf018c60903f70) = CONST 
    0x20a: v20a(0x40) = CONST 
    0x20c: v20c = MLOAD v20a(0x40)
    0x20d: v20d(0x1) = CONST 
    0x20f: v20f(0xa0) = CONST 
    0x211: v211(0x2) = CONST 
    0x213: v213(0x10000000000000000000000000000000000000000) = EXP v211(0x2), v20f(0xa0)
    0x214: v214(0xffffffffffffffffffffffffffffffffffffffff) = SUB v213(0x10000000000000000000000000000000000000000), v20d(0x1)
    0x217: v217 = AND v168, v214(0xffffffffffffffffffffffffffffffffffffffff)
    0x219: MSTORE v20c, v217
    0x21a: v21a(0x20) = CONST 
    0x21c: v21c = ADD v21a(0x20), v20c
    0x21d: v21d(0x40) = CONST 
    0x21f: v21f = MLOAD v21d(0x40)
    0x222: v222(0x20) = SUB v21c, v21f
    0x224: LOG1 v21f, v222(0x20), v1e8(0x4ff638452bbf33c012645d18ae6f05515ff5f2d1dfb0cece8cbf018c60903f70)
    0x226: JUMP v15a(0x16d)

    Begin block 0x16d
    prev=[0x1bf], succ=[]
    =================================
    0x16e: STOP 

}

function controller()() public {
    Begin block 0x16f
    prev=[], succ=[0x176, 0x17a]
    =================================
    0x170: v170 = CALLVALUE 
    0x171: v171 = ISZERO v170
    0x172: v172(0x17a) = CONST 
    0x175: JUMPI v172(0x17a), v171

    Begin block 0x176
    prev=[0x16f], succ=[]
    =================================
    0x176: v176(0x0) = CONST 
    0x179: REVERT v176(0x0), v176(0x0)

    Begin block 0x17a
    prev=[0x16f], succ=[0x227]
    =================================
    0x17b: v17b(0x182) = CONST 
    0x17e: v17e(0x227) = CONST 
    0x181: JUMP v17e(0x227)

    Begin block 0x227
    prev=[0x17a], succ=[0x182]
    =================================
    0x228: v228(0x0) = CONST 
    0x22a: v22a = SLOAD v228(0x0)
    0x22b: v22b(0x1) = CONST 
    0x22d: v22d(0xa0) = CONST 
    0x22f: v22f(0x2) = CONST 
    0x231: v231(0x10000000000000000000000000000000000000000) = EXP v22f(0x2), v22d(0xa0)
    0x232: v232(0xffffffffffffffffffffffffffffffffffffffff) = SUB v231(0x10000000000000000000000000000000000000000), v22b(0x1)
    0x233: v233 = AND v232(0xffffffffffffffffffffffffffffffffffffffff), v22a
    0x235: JUMP v17b(0x182)

    Begin block 0x182
    prev=[0x227], succ=[]
    =================================
    0x183: v183(0x40) = CONST 
    0x185: v185 = MLOAD v183(0x40)
    0x186: v186(0x1) = CONST 
    0x188: v188(0xa0) = CONST 
    0x18a: v18a(0x2) = CONST 
    0x18c: v18c(0x10000000000000000000000000000000000000000) = EXP v18a(0x2), v188(0xa0)
    0x18d: v18d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18c(0x10000000000000000000000000000000000000000), v186(0x1)
    0x190: v190 = AND v233, v18d(0xffffffffffffffffffffffffffffffffffffffff)
    0x192: MSTORE v185, v190
    0x193: v193(0x20) = CONST 
    0x195: v195 = ADD v193(0x20), v185
    0x196: v196(0x40) = CONST 
    0x198: v198 = MLOAD v196(0x40)
    0x19b: v19b(0x20) = SUB v195, v198
    0x19d: RETURN v198, v19b(0x20)

}

function fallback()() public {
    Begin block 0x56
    prev=[], succ=[0xc2, 0xc6]
    =================================
    0x57: v57(0x0) = CONST 
    0x5a: v5a = SLOAD v57(0x0)
    0x5b: v5b(0x1) = CONST 
    0x5d: v5d = SLOAD v5b(0x1)
    0x5e: v5e(0x1) = CONST 
    0x60: v60(0xa0) = CONST 
    0x62: v62(0x2) = CONST 
    0x64: v64(0x10000000000000000000000000000000000000000) = EXP v62(0x2), v60(0xa0)
    0x65: v65(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64(0x10000000000000000000000000000000000000000), v5e(0x1)
    0x68: v68 = AND v5a, v65(0xffffffffffffffffffffffffffffffffffffffff)
    0x6a: v6a(0xe16c7d98) = CONST 
    0x71: v71(0x40) = CONST 
    0x73: v73 = MLOAD v71(0x40)
    0x74: v74(0x20) = CONST 
    0x76: v76 = ADD v74(0x20), v73
    0x77: MSTORE v76, v57(0x0)
    0x78: v78(0x40) = CONST 
    0x7a: v7a = MLOAD v78(0x40)
    0x7b: v7b(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x99: v99(0xffffffff) = CONST 
    0x9f: v9f(0xe16c7d98) = AND v6a(0xe16c7d98), v99(0xffffffff)
    0xa0: va0(0xe16c7d9800000000000000000000000000000000000000000000000000000000) = MUL v9f(0xe16c7d98), v7b(0x100000000000000000000000000000000000000000000000000000000)
    0xa2: MSTORE v7a, va0(0xe16c7d9800000000000000000000000000000000000000000000000000000000)
    0xa3: va3(0x4) = CONST 
    0xa6: va6 = ADD v7a, va3(0x4)
    0xaa: MSTORE va6, v5d
    0xab: vab(0x24) = CONST 
    0xad: vad = ADD vab(0x24), v7a
    0xae: vae(0x20) = CONST 
    0xb0: vb0(0x40) = CONST 
    0xb2: vb2 = MLOAD vb0(0x40)
    0xb5: vb5(0x24) = SUB vad, vb2
    0xb7: vb7(0x0) = CONST 
    0xbb: vbb = EXTCODESIZE v68
    0xbc: vbc = ISZERO vbb
    0xbd: vbd = ISZERO vbc
    0xbe: vbe(0xc6) = CONST 
    0xc1: JUMPI vbe(0xc6), vbd

    Begin block 0xc2
    prev=[0x56], succ=[]
    =================================
    0xc2: vc2(0x0) = CONST 
    0xc5: REVERT vc2(0x0), vc2(0x0)

    Begin block 0xc6
    prev=[0x56], succ=[0xd3, 0xd7]
    =================================
    0xc7: vc7(0x2c6) = CONST 
    0xca: vca = GAS 
    0xcb: vcb = SUB vca, vc7(0x2c6)
    0xcc: vcc = CALL vcb, v68, vb7(0x0), vb2, vb5(0x24), vb2, vae(0x20)
    0xcd: vcd = ISZERO vcc
    0xce: vce = ISZERO vcd
    0xcf: vcf(0xd7) = CONST 
    0xd2: JUMPI vcf(0xd7), vce

    Begin block 0xd3
    prev=[0xc6], succ=[]
    =================================
    0xd3: vd3(0x0) = CONST 
    0xd6: REVERT vd3(0x0), vd3(0x0)

    Begin block 0xd7
    prev=[0xc6], succ=[0xf4, 0xf8]
    =================================
    0xdb: vdb(0x40) = CONST 
    0xdd: vdd = MLOAD vdb(0x40)
    0xdf: vdf = MLOAD vdd
    0xe3: ve3(0x0) = CONST 
    0xe5: ve5(0x1) = CONST 
    0xe7: ve7(0xa0) = CONST 
    0xe9: ve9(0x2) = CONST 
    0xeb: veb(0x10000000000000000000000000000000000000000) = EXP ve9(0x2), ve7(0xa0)
    0xec: vec(0xffffffffffffffffffffffffffffffffffffffff) = SUB veb(0x10000000000000000000000000000000000000000), ve5(0x1)
    0xee: vee = AND vdf, vec(0xffffffffffffffffffffffffffffffffffffffff)
    0xef: vef = GT vee, ve3(0x0)
    0xf0: vf0(0xf8) = CONST 
    0xf3: JUMPI vf0(0xf8), vef

    Begin block 0xf4
    prev=[0xd7], succ=[]
    =================================
    0xf4: vf4(0x0) = CONST 
    0xf7: REVERT vf4(0x0), vf4(0x0)

    Begin block 0xf8
    prev=[0xd7], succ=[0x122, 0x125]
    =================================
    0xf9: vf9(0x40) = CONST 
    0xfc: vfc = MLOAD vf9(0x40)
    0xfd: vfd = CALLDATASIZE 
    0xff: vff = ADD vfc, vfd
    0x101: MSTORE vf9(0x40), vff
    0x102: v102 = CALLDATASIZE 
    0x103: v103(0x0) = CONST 
    0x106: CALLDATACOPY vfc, v103(0x0), v102
    0x107: v107(0x0) = CONST 
    0x10a: v10a = CALLDATASIZE 
    0x10d: v10d = GAS 
    0x10e: v10e = DELEGATECALL v10d, vdf, vfc, v10a, v107(0x0), v107(0x0)
    0x110: v110 = MLOAD vf9(0x40)
    0x111: v111 = RETURNDATASIZE 
    0x113: v113 = ADD v110, v111
    0x115: MSTORE vf9(0x40), v113
    0x116: v116 = RETURNDATASIZE 
    0x117: v117(0x0) = CONST 
    0x11a: RETURNDATACOPY v110, v117(0x0), v116
    0x11d: v11d = ISZERO v10e
    0x11e: v11e(0x125) = CONST 
    0x121: JUMPI v11e(0x125), v11d

    Begin block 0x122
    prev=[0xf8], succ=[]
    =================================
    0x122: v122 = RETURNDATASIZE 
    0x124: RETURN v110, v122

    Begin block 0x125
    prev=[0xf8], succ=[]
    =================================
    0x126: v126 = RETURNDATASIZE 
    0x128: REVERT v110, v126

}

