function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x10d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x10d) = CONST 
    0xc: JUMPI v9(0x10d), v8

    Begin block 0xd
    prev=[0x0], succ=[0x95, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x6e89e43d) = CONST 
    0x19: v19 = GT v14(0x6e89e43d), v12
    0x1a: v1a(0x95) = CONST 
    0x1d: JUMPI v1a(0x95), v19

    Begin block 0x95
    prev=[0xd], succ=[0xdc, 0xa1]
    =================================
    0x97: v97(0x3a74a767) = CONST 
    0x9c: v9c = GT v97(0x3a74a767), v12
    0x9d: v9d(0xdc) = CONST 
    0xa0: JUMPI v9d(0xdc), v9c

    Begin block 0xdc
    prev=[0x95], succ=[0xc89, 0xe8]
    =================================
    0xde: vde(0x6fdde03) = CONST 
    0xe3: ve3 = EQ vde(0x6fdde03), v12
    0xc7e: vc7e(0xc89) = CONST 
    0xc7f: JUMPI vc7e(0xc89), ve3

    Begin block 0xc89
    prev=[0xdc], succ=[]
    =================================
    0xc8a: vc8a(0x197) = CONST 
    0xc8b: CALLPRIVATE vc8a(0x197)

    Begin block 0xe8
    prev=[0xdc], succ=[0xc8c, 0xf3]
    =================================
    0xe9: ve9(0x8fa2fdf) = CONST 
    0xee: vee = EQ ve9(0x8fa2fdf), v12
    0xc80: vc80(0xc8c) = CONST 
    0xc81: JUMPI vc80(0xc8c), vee

    Begin block 0xc8c
    prev=[0xe8], succ=[]
    =================================
    0xc8d: vc8d(0x221) = CONST 
    0xc8e: CALLPRIVATE vc8d(0x221)

    Begin block 0xf3
    prev=[0xe8], succ=[0xc8f, 0xfe]
    =================================
    0xf4: vf4(0x18160ddd) = CONST 
    0xf9: vf9 = EQ vf4(0x18160ddd), v12
    0xc82: vc82(0xc8f) = CONST 
    0xc83: JUMPI vc82(0xc8f), vf9

    Begin block 0xc8f
    prev=[0xf3], succ=[]
    =================================
    0xc90: vc90(0x278) = CONST 
    0xc91: CALLPRIVATE vc90(0x278)

    Begin block 0xfe
    prev=[0xf3], succ=[0x109, 0xc92]
    =================================
    0xff: vff(0x313ce567) = CONST 
    0x104: v104 = EQ vff(0x313ce567), v12
    0xc84: vc84(0xc92) = CONST 
    0xc85: JUMPI vc84(0xc92), v104

    Begin block 0x109
    prev=[0xfe], succ=[0x114]
    =================================
    0x109: v109(0x114) = CONST 
    0x10c: JUMP v109(0x114)

    Begin block 0x114
    prev=[0x60, 0x91, 0xd8, 0x109, 0x10d], succ=[0x156, 0x177]
    =================================
    0x115: v115(0x2) = CONST 
    0x117: v117 = SLOAD v115(0x2)
    0x118: v118(0x40) = CONST 
    0x11a: v11a = MLOAD v118(0x40)
    0x11b: v11b(0x0) = CONST 
    0x11e: v11e(0x1) = CONST 
    0x120: v120(0x1) = CONST 
    0x122: v122(0xa0) = CONST 
    0x124: v124(0x10000000000000000000000000000000000000000) = SHL v122(0xa0), v120(0x1)
    0x125: v125(0xffffffffffffffffffffffffffffffffffffffff) = SUB v124(0x10000000000000000000000000000000000000000), v11e(0x1)
    0x126: v126 = AND v125(0xffffffffffffffffffffffffffffffffffffffff), v117
    0x12a: v12a = CALLDATASIZE 
    0x132: CALLDATACOPY v11a, v11b(0x0), v12a
    0x133: v133(0x40) = CONST 
    0x135: v135 = MLOAD v133(0x40)
    0x137: v137 = ADD v11a, v12a
    0x13a: v13a(0x0) = CONST 
    0x144: v144 = SUB v137, v135
    0x147: v147 = GAS 
    0x148: v148 = DELEGATECALL v147, v126, v135, v144, v135, v13a(0x0)
    0x14c: v14c = RETURNDATASIZE 
    0x14e: v14e(0x0) = CONST 
    0x151: v151 = EQ v14c, v14e(0x0)
    0x152: v152(0x177) = CONST 
    0x155: JUMPI v152(0x177), v151

    Begin block 0x156
    prev=[0x114], succ=[0x17c]
    =================================
    0x156: v156(0x40) = CONST 
    0x158: v158 = MLOAD v156(0x40)
    0x15b: v15b(0x1f) = CONST 
    0x15d: v15d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v15b(0x1f)
    0x15e: v15e(0x3f) = CONST 
    0x160: v160 = RETURNDATASIZE 
    0x161: v161 = ADD v160, v15e(0x3f)
    0x162: v162 = AND v161, v15d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x164: v164 = ADD v158, v162
    0x165: v165(0x40) = CONST 
    0x167: MSTORE v165(0x40), v164
    0x168: v168 = RETURNDATASIZE 
    0x16a: MSTORE v158, v168
    0x16b: v16b = RETURNDATASIZE 
    0x16c: v16c(0x0) = CONST 
    0x16e: v16e(0x20) = CONST 
    0x171: v171 = ADD v158, v16e(0x20)
    0x172: RETURNDATACOPY v171, v16c(0x0), v16b
    0x173: v173(0x17c) = CONST 
    0x176: JUMP v173(0x17c)

    Begin block 0x17c
    prev=[0x156, 0x177], succ=[0x190, 0x193]
    =================================
    0x181: v181(0x40) = CONST 
    0x183: v183 = MLOAD v181(0x40)
    0x184: v184 = RETURNDATASIZE 
    0x185: v185(0x0) = CONST 
    0x188: RETURNDATACOPY v183, v185(0x0), v184
    0x18b: v18b = ISZERO v148
    0x18c: v18c(0x193) = CONST 
    0x18f: JUMPI v18c(0x193), v18b

    Begin block 0x190
    prev=[0x17c], succ=[]
    =================================
    0x190: v190 = RETURNDATASIZE 
    0x192: RETURN v183, v190

    Begin block 0x193
    prev=[0x17c], succ=[]
    =================================
    0x194: v194 = RETURNDATASIZE 
    0x196: REVERT v183, v194

    Begin block 0x177
    prev=[0x114], succ=[0x17c]
    =================================
    0x178: v178(0x60) = CONST 

    Begin block 0xc92
    prev=[0xfe], succ=[]
    =================================
    0xc93: vc93(0x29f) = CONST 
    0xc94: CALLPRIVATE vc93(0x29f)

    Begin block 0xa1
    prev=[0x95], succ=[0xc95, 0xac]
    =================================
    0xa2: va2(0x3a74a767) = CONST 
    0xa7: va7 = EQ va2(0x3a74a767), v12
    0xc74: vc74(0xc95) = CONST 
    0xc75: JUMPI vc74(0xc95), va7

    Begin block 0xc95
    prev=[0xa1], succ=[]
    =================================
    0xc96: vc96(0x2ca) = CONST 
    0xc97: CALLPRIVATE vc96(0x2ca)

    Begin block 0xac
    prev=[0xa1], succ=[0xc98, 0xb7]
    =================================
    0xad: vad(0x3fc8cef3) = CONST 
    0xb2: vb2 = EQ vad(0x3fc8cef3), v12
    0xc76: vc76(0xc98) = CONST 
    0xc77: JUMPI vc76(0xc98), vb2

    Begin block 0xc98
    prev=[0xac], succ=[]
    =================================
    0xc99: vc99(0x2ff) = CONST 
    0xc9a: CALLPRIVATE vc99(0x2ff)

    Begin block 0xb7
    prev=[0xac], succ=[0xc9b, 0xc2]
    =================================
    0xb8: vb8(0x3fd8b02f) = CONST 
    0xbd: vbd = EQ vb8(0x3fd8b02f), v12
    0xc78: vc78(0xc9b) = CONST 
    0xc79: JUMPI vc78(0xc9b), vbd

    Begin block 0xc9b
    prev=[0xb7], succ=[]
    =================================
    0xc9c: vc9c(0x314) = CONST 
    0xc9d: CALLPRIVATE vc9c(0x314)

    Begin block 0xc2
    prev=[0xb7], succ=[0xc9e, 0xcd]
    =================================
    0xc3: vc3(0x5aa6e675) = CONST 
    0xc8: vc8 = EQ vc3(0x5aa6e675), v12
    0xc7a: vc7a(0xc9e) = CONST 
    0xc7b: JUMPI vc7a(0xc9e), vc8

    Begin block 0xc9e
    prev=[0xc2], succ=[]
    =================================
    0xc9f: vc9f(0x329) = CONST 
    0xca0: CALLPRIVATE vc9f(0x329)

    Begin block 0xcd
    prev=[0xc2], succ=[0xd8, 0xca1]
    =================================
    0xce: vce(0x5c60da1b) = CONST 
    0xd3: vd3 = EQ vce(0x5c60da1b), v12
    0xc7c: vc7c(0xca1) = CONST 
    0xc7d: JUMPI vc7c(0xca1), vd3

    Begin block 0xd8
    prev=[0xcd], succ=[0x114]
    =================================
    0xd8: vd8(0x114) = CONST 
    0xdb: JUMP vd8(0x114)

    Begin block 0xca1
    prev=[0xcd], succ=[]
    =================================
    0xca2: vca2(0x33e) = CONST 
    0xca3: CALLPRIVATE vca2(0x33e)

    Begin block 0x1e
    prev=[0xd], succ=[0x64, 0x29]
    =================================
    0x1f: v1f(0xb052e521) = CONST 
    0x24: v24 = GT v1f(0xb052e521), v12
    0x25: v25(0x64) = CONST 
    0x28: JUMPI v25(0x64), v24

    Begin block 0x64
    prev=[0x1e], succ=[0xca4, 0x70]
    =================================
    0x66: v66(0x6e89e43d) = CONST 
    0x6b: v6b = EQ v66(0x6e89e43d), v12
    0xc6c: vc6c(0xca4) = CONST 
    0xc6d: JUMPI vc6c(0xca4), v6b

    Begin block 0xca4
    prev=[0x64], succ=[]
    =================================
    0xca5: vca5(0x353) = CONST 
    0xca6: CALLPRIVATE vca5(0x353)

    Begin block 0x70
    prev=[0x64], succ=[0xca7, 0x7b]
    =================================
    0x71: v71(0x70a08231) = CONST 
    0x76: v76 = EQ v71(0x70a08231), v12
    0xc6e: vc6e(0xca7) = CONST 
    0xc6f: JUMPI vc6e(0xca7), v76

    Begin block 0xca7
    prev=[0x70], succ=[]
    =================================
    0xca8: vca8(0x386) = CONST 
    0xca9: CALLPRIVATE vca8(0x386)

    Begin block 0x7b
    prev=[0x70], succ=[0xcaa, 0x86]
    =================================
    0x7c: v7c(0x83f81a64) = CONST 
    0x81: v81 = EQ v7c(0x83f81a64), v12
    0xc70: vc70(0xcaa) = CONST 
    0xc71: JUMPI vc70(0xcaa), v81

    Begin block 0xcaa
    prev=[0x7b], succ=[]
    =================================
    0xcab: vcab(0x3b9) = CONST 
    0xcac: CALLPRIVATE vcab(0x3b9)

    Begin block 0x86
    prev=[0x7b], succ=[0x91, 0xcad]
    =================================
    0x87: v87(0x95d89b41) = CONST 
    0x8c: v8c = EQ v87(0x95d89b41), v12
    0xc72: vc72(0xcad) = CONST 
    0xc73: JUMPI vc72(0xcad), v8c

    Begin block 0x91
    prev=[0x86], succ=[0x114]
    =================================
    0x91: v91(0x114) = CONST 
    0x94: JUMP v91(0x114)

    Begin block 0xcad
    prev=[0x86], succ=[]
    =================================
    0xcae: vcae(0x3ce) = CONST 
    0xcaf: CALLPRIVATE vcae(0x3ce)

    Begin block 0x29
    prev=[0x1e], succ=[0xcb0, 0x34]
    =================================
    0x2a: v2a(0xb052e521) = CONST 
    0x2f: v2f = EQ v2a(0xb052e521), v12
    0xc62: vc62(0xcb0) = CONST 
    0xc63: JUMPI vc62(0xcb0), v2f

    Begin block 0xcb0
    prev=[0x29], succ=[]
    =================================
    0xcb1: vcb1(0x3e3) = CONST 
    0xcb2: CALLPRIVATE vcb1(0x3e3)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xcb3]
    =================================
    0x35: v35(0xbb2f30ae) = CONST 
    0x3a: v3a = EQ v35(0xbb2f30ae), v12
    0xc64: vc64(0xcb3) = CONST 
    0xc65: JUMPI vc64(0xcb3), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xcb6, 0x4a]
    =================================
    0x40: v40(0xbb913f41) = CONST 
    0x45: v45 = EQ v40(0xbb913f41), v12
    0xc66: vc66(0xcb6) = CONST 
    0xc67: JUMPI vc66(0xcb6), v45

    Begin block 0xcb6
    prev=[0x3f], succ=[]
    =================================
    0xcb7: vcb7(0x42b) = CONST 
    0xcb8: CALLPRIVATE vcb7(0x42b)

    Begin block 0x4a
    prev=[0x3f], succ=[0xcb9, 0x55]
    =================================
    0x4b: v4b(0xdd62ed3e) = CONST 
    0x50: v50 = EQ v4b(0xdd62ed3e), v12
    0xc68: vc68(0xcb9) = CONST 
    0xc69: JUMPI vc68(0xcb9), v50

    Begin block 0xcb9
    prev=[0x4a], succ=[]
    =================================
    0xcba: vcba(0x45e) = CONST 
    0xcbb: CALLPRIVATE vcba(0x45e)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0xcbc]
    =================================
    0x56: v56(0xf851a440) = CONST 
    0x5b: v5b = EQ v56(0xf851a440), v12
    0xc6a: vc6a(0xcbc) = CONST 
    0xc6b: JUMPI vc6a(0xcbc), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x114]
    =================================
    0x60: v60(0x114) = CONST 
    0x63: JUMP v60(0x114)

    Begin block 0xcbc
    prev=[0x55], succ=[]
    =================================
    0xcbd: vcbd(0x499) = CONST 
    0xcbe: CALLPRIVATE vcbd(0x499)

    Begin block 0xcb3
    prev=[0x34], succ=[]
    =================================
    0xcb4: vcb4(0x3f8) = CONST 
    0xcb5: CALLPRIVATE vcb4(0x3f8)

    Begin block 0x10d
    prev=[0x0], succ=[0xc86, 0x114]
    =================================
    0x10e: v10e = CALLDATASIZE 
    0x10f: v10f(0x114) = CONST 
    0x112: JUMPI v10f(0x114), v10e

    Begin block 0xc86
    prev=[0x10d], succ=[]
    =================================
    0xc86: vc86(0xc88) = CONST 
    0xc87: CALLPRIVATE vc86(0xc88)

}

function name()() public {
    Begin block 0x197
    prev=[], succ=[0x19f, 0x1a3]
    =================================
    0x198: v198 = CALLVALUE 
    0x19a: v19a = ISZERO v198
    0x19b: v19b(0x1a3) = CONST 
    0x19e: JUMPI v19b(0x1a3), v19a

    Begin block 0x19f
    prev=[0x197], succ=[]
    =================================
    0x19f: v19f(0x0) = CONST 
    0x1a2: REVERT v19f(0x0), v19f(0x0)

    Begin block 0x1a3
    prev=[0x197], succ=[0x1ac0x197]
    =================================
    0x1a5: v1a5(0x1ac) = CONST 
    0x1a8: v1a8(0x4ae) = CONST 
    0x1ab: v1ab_0, v1ab_1 = CALLPRIVATE v1a8(0x4ae), v1a5(0x1ac)

    Begin block 0x1ac0x197
    prev=[0x1a3], succ=[0x1ce0x197]
    =================================
    0x1ad0x197: v1971ad(0x40) = CONST 
    0x1b00x197: v1971b0 = MLOAD v1971ad(0x40)
    0x1b10x197: v1971b1(0x20) = CONST 
    0x1b50x197: MSTORE v1971b0, v1971b1(0x20)
    0x1b70x197: v1971b7 = MLOAD v1ab_0
    0x1ba0x197: v1971ba = ADD v1971b0, v1971b1(0x20)
    0x1bb0x197: MSTORE v1971ba, v1971b7
    0x1bd0x197: v1971bd = MLOAD v1ab_0
    0x1c40x197: v1971c4 = ADD v1971b0, v1971ad(0x40)
    0x1c70x197: v1971c7 = ADD v1ab_0, v1971b1(0x20)
    0x1cc0x197: v1971cc(0x0) = CONST 

    Begin block 0x1ce0x197
    prev=[0x1d70x197, 0x1ac0x197], succ=[0x1e60x197, 0x1d70x197]
    =================================
    0x1ce0x197_0x0: v1ce197_0 = PHI v1971e1, v1971cc(0x0)
    0x1d10x197: v1971d1 = LT v1ce197_0, v1971bd
    0x1d20x197: v1971d2 = ISZERO v1971d1
    0x1d30x197: v1971d3(0x1e6) = CONST 
    0x1d60x197: JUMPI v1971d3(0x1e6), v1971d2

    Begin block 0x1e60x197
    prev=[0x1ce0x197], succ=[0x2130x197, 0x1fa0x197]
    =================================
    0x1ef0x197: v1971ef = ADD v1971bd, v1971c4
    0x1f10x197: v1971f1(0x1f) = CONST 
    0x1f30x197: v1971f3 = AND v1971f1(0x1f), v1971bd
    0x1f50x197: v1971f5 = ISZERO v1971f3
    0x1f60x197: v1971f6(0x213) = CONST 
    0x1f90x197: JUMPI v1971f6(0x213), v1971f5

    Begin block 0x2130x197
    prev=[0x1e60x197, 0x1fa0x197], succ=[]
    =================================
    0x2130x197_0x1: v213197_1 = PHI v197210, v1971ef
    0x2190x197: v197219(0x40) = CONST 
    0x21b0x197: v19721b = MLOAD v197219(0x40)
    0x21e0x197: v19721e = SUB v213197_1, v19721b
    0x2200x197: RETURN v19721b, v19721e

    Begin block 0x1fa0x197
    prev=[0x1e60x197], succ=[0x2130x197]
    =================================
    0x1fc0x197: v1971fc = SUB v1971ef, v1971f3
    0x1fe0x197: v1971fe = MLOAD v1971fc
    0x1ff0x197: v1971ff(0x1) = CONST 
    0x2020x197: v197202(0x20) = CONST 
    0x2040x197: v197204 = SUB v197202(0x20), v1971f3
    0x2050x197: v197205(0x100) = CONST 
    0x2080x197: v197208 = EXP v197205(0x100), v197204
    0x2090x197: v197209 = SUB v197208, v1971ff(0x1)
    0x20a0x197: v19720a = NOT v197209
    0x20b0x197: v19720b = AND v19720a, v1971fe
    0x20d0x197: MSTORE v1971fc, v19720b
    0x20e0x197: v19720e(0x20) = CONST 
    0x2100x197: v197210 = ADD v19720e(0x20), v1971fc

    Begin block 0x1d70x197
    prev=[0x1ce0x197], succ=[0x1ce0x197]
    =================================
    0x1d70x197_0x0: v1d7197_0 = PHI v1971e1, v1971cc(0x0)
    0x1d90x197: v1971d9 = ADD v1d7197_0, v1971c7
    0x1da0x197: v1971da = MLOAD v1971d9
    0x1dd0x197: v1971dd = ADD v1d7197_0, v1971c4
    0x1de0x197: MSTORE v1971dd, v1971da
    0x1df0x197: v1971df(0x20) = CONST 
    0x1e10x197: v1971e1 = ADD v1971df(0x20), v1d7197_0
    0x1e20x197: v1971e2(0x1ce) = CONST 
    0x1e50x197: JUMP v1971e2(0x1ce)

}

function routerMap(address,address)() public {
    Begin block 0x221
    prev=[], succ=[0x229, 0x22d]
    =================================
    0x222: v222 = CALLVALUE 
    0x224: v224 = ISZERO v222
    0x225: v225(0x22d) = CONST 
    0x228: JUMPI v225(0x22d), v224

    Begin block 0x229
    prev=[0x221], succ=[]
    =================================
    0x229: v229(0x0) = CONST 
    0x22c: REVERT v229(0x0), v229(0x0)

    Begin block 0x22d
    prev=[0x221], succ=[0x240, 0x244]
    =================================
    0x22f: v22f(0x8f0) = CONST 
    0x232: v232(0x4) = CONST 
    0x235: v235 = CALLDATASIZE 
    0x236: v236 = SUB v235, v232(0x4)
    0x237: v237(0x40) = CONST 
    0x23a: v23a = LT v236, v237(0x40)
    0x23b: v23b = ISZERO v23a
    0x23c: v23c(0x244) = CONST 
    0x23f: JUMPI v23c(0x244), v23b

    Begin block 0x240
    prev=[0x22d], succ=[]
    =================================
    0x240: v240(0x0) = CONST 
    0x243: REVERT v240(0x0), v240(0x0)

    Begin block 0x244
    prev=[0x22d], succ=[0x53c]
    =================================
    0x246: v246(0x1) = CONST 
    0x248: v248(0x1) = CONST 
    0x24a: v24a(0xa0) = CONST 
    0x24c: v24c(0x10000000000000000000000000000000000000000) = SHL v24a(0xa0), v248(0x1)
    0x24d: v24d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24c(0x10000000000000000000000000000000000000000), v246(0x1)
    0x24f: v24f = CALLDATALOAD v232(0x4)
    0x251: v251 = AND v24d(0xffffffffffffffffffffffffffffffffffffffff), v24f
    0x253: v253(0x20) = CONST 
    0x255: v255(0x24) = ADD v253(0x20), v232(0x4)
    0x256: v256 = CALLDATALOAD v255(0x24)
    0x257: v257 = AND v256, v24d(0xffffffffffffffffffffffffffffffffffffffff)
    0x258: v258(0x53c) = CONST 
    0x25b: JUMP v258(0x53c)

    Begin block 0x53c
    prev=[0x244], succ=[0x8f0]
    =================================
    0x53d: v53d(0x5) = CONST 
    0x53f: v53f(0x20) = CONST 
    0x543: MSTORE v53f(0x20), v53d(0x5)
    0x544: v544(0x0) = CONST 
    0x548: MSTORE v544(0x0), v251
    0x549: v549(0x40) = CONST 
    0x54d: v54d = SHA3 v544(0x0), v549(0x40)
    0x550: MSTORE v53f(0x20), v54d
    0x553: MSTORE v544(0x0), v257
    0x555: v555 = SHA3 v544(0x0), v549(0x40)
    0x556: v556 = SLOAD v555
    0x557: v557(0x1) = CONST 
    0x559: v559(0x1) = CONST 
    0x55b: v55b(0xa0) = CONST 
    0x55d: v55d(0x10000000000000000000000000000000000000000) = SHL v55b(0xa0), v559(0x1)
    0x55e: v55e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v55d(0x10000000000000000000000000000000000000000), v557(0x1)
    0x55f: v55f = AND v55e(0xffffffffffffffffffffffffffffffffffffffff), v556
    0x561: JUMP v22f(0x8f0)

    Begin block 0x8f0
    prev=[0x53c], succ=[]
    =================================
    0x8f1: v8f1(0x40) = CONST 
    0x8f4: v8f4 = MLOAD v8f1(0x40)
    0x8f5: v8f5(0x1) = CONST 
    0x8f7: v8f7(0x1) = CONST 
    0x8f9: v8f9(0xa0) = CONST 
    0x8fb: v8fb(0x10000000000000000000000000000000000000000) = SHL v8f9(0xa0), v8f7(0x1)
    0x8fc: v8fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8fb(0x10000000000000000000000000000000000000000), v8f5(0x1)
    0x8ff: v8ff = AND v55f, v8fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x901: MSTORE v8f4, v8ff
    0x902: v902 = MLOAD v8f1(0x40)
    0x906: v906(0x0) = SUB v8f4, v902
    0x907: v907(0x20) = CONST 
    0x909: v909(0x20) = ADD v907(0x20), v906(0x0)
    0x90b: RETURN v902, v909(0x20)

}

function totalSupply()() public {
    Begin block 0x278
    prev=[], succ=[0x280, 0x284]
    =================================
    0x279: v279 = CALLVALUE 
    0x27b: v27b = ISZERO v279
    0x27c: v27c(0x284) = CONST 
    0x27f: JUMPI v27c(0x284), v27b

    Begin block 0x280
    prev=[0x278], succ=[]
    =================================
    0x280: v280(0x0) = CONST 
    0x283: REVERT v280(0x0), v280(0x0)

    Begin block 0x284
    prev=[0x278], succ=[0x562]
    =================================
    0x286: v286(0x92b) = CONST 
    0x289: v289(0x562) = CONST 
    0x28c: JUMP v289(0x562)

    Begin block 0x562
    prev=[0x284], succ=[0x92b]
    =================================
    0x563: v563(0xb) = CONST 
    0x565: v565 = SLOAD v563(0xb)
    0x567: JUMP v286(0x92b)

    Begin block 0x92b
    prev=[0x562], succ=[]
    =================================
    0x92c: v92c(0x40) = CONST 
    0x92f: v92f = MLOAD v92c(0x40)
    0x932: MSTORE v92f, v565
    0x933: v933 = MLOAD v92c(0x40)
    0x937: v937(0x0) = SUB v92f, v933
    0x938: v938(0x20) = CONST 
    0x93a: v93a(0x20) = ADD v938(0x20), v937(0x0)
    0x93c: RETURN v933, v93a(0x20)

}

function decimals()() public {
    Begin block 0x29f
    prev=[], succ=[0x2a7, 0x2ab]
    =================================
    0x2a0: v2a0 = CALLVALUE 
    0x2a2: v2a2 = ISZERO v2a0
    0x2a3: v2a3(0x2ab) = CONST 
    0x2a6: JUMPI v2a3(0x2ab), v2a2

    Begin block 0x2a7
    prev=[0x29f], succ=[]
    =================================
    0x2a7: v2a7(0x0) = CONST 
    0x2aa: REVERT v2a7(0x0), v2a7(0x0)

    Begin block 0x2ab
    prev=[0x29f], succ=[0x568]
    =================================
    0x2ad: v2ad(0x2b4) = CONST 
    0x2b0: v2b0(0x568) = CONST 
    0x2b3: JUMP v2b0(0x568)

    Begin block 0x568
    prev=[0x2ab], succ=[0x2b4]
    =================================
    0x569: v569(0x12) = CONST 
    0x56c: JUMP v2ad(0x2b4)

    Begin block 0x2b4
    prev=[0x568], succ=[]
    =================================
    0x2b5: v2b5(0x40) = CONST 
    0x2b8: v2b8 = MLOAD v2b5(0x40)
    0x2b9: v2b9(0xff) = CONST 
    0x2bd: v2bd(0x12) = AND v569(0x12), v2b9(0xff)
    0x2bf: MSTORE v2b8, v2bd(0x12)
    0x2c0: v2c0 = MLOAD v2b5(0x40)
    0x2c4: v2c4(0x0) = SUB v2b8, v2c0
    0x2c5: v2c5(0x20) = CONST 
    0x2c7: v2c7(0x20) = ADD v2c5(0x20), v2c4(0x0)
    0x2c9: RETURN v2c0, v2c7(0x20)

}

function _setAdmin(address)() public {
    Begin block 0x2ca
    prev=[], succ=[0x2d2, 0x2d6]
    =================================
    0x2cb: v2cb = CALLVALUE 
    0x2cd: v2cd = ISZERO v2cb
    0x2ce: v2ce(0x2d6) = CONST 
    0x2d1: JUMPI v2ce(0x2d6), v2cd

    Begin block 0x2d2
    prev=[0x2ca], succ=[]
    =================================
    0x2d2: v2d2(0x0) = CONST 
    0x2d5: REVERT v2d2(0x0), v2d2(0x0)

    Begin block 0x2d6
    prev=[0x2ca], succ=[0x2e9, 0x2ed]
    =================================
    0x2d8: v2d8(0x95c) = CONST 
    0x2db: v2db(0x4) = CONST 
    0x2de: v2de = CALLDATASIZE 
    0x2df: v2df = SUB v2de, v2db(0x4)
    0x2e0: v2e0(0x20) = CONST 
    0x2e3: v2e3 = LT v2df, v2e0(0x20)
    0x2e4: v2e4 = ISZERO v2e3
    0x2e5: v2e5(0x2ed) = CONST 
    0x2e8: JUMPI v2e5(0x2ed), v2e4

    Begin block 0x2e9
    prev=[0x2d6], succ=[]
    =================================
    0x2e9: v2e9(0x0) = CONST 
    0x2ec: REVERT v2e9(0x0), v2e9(0x0)

    Begin block 0x2ed
    prev=[0x2d6], succ=[0x56d]
    =================================
    0x2ef: v2ef = CALLDATALOAD v2db(0x4)
    0x2f0: v2f0(0x1) = CONST 
    0x2f2: v2f2(0x1) = CONST 
    0x2f4: v2f4(0xa0) = CONST 
    0x2f6: v2f6(0x10000000000000000000000000000000000000000) = SHL v2f4(0xa0), v2f2(0x1)
    0x2f7: v2f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f6(0x10000000000000000000000000000000000000000), v2f0(0x1)
    0x2f8: v2f8 = AND v2f7(0xffffffffffffffffffffffffffffffffffffffff), v2ef
    0x2f9: v2f9(0x56d) = CONST 
    0x2fc: JUMP v2f9(0x56d)

    Begin block 0x56d
    prev=[0x2ed], succ=[0x580, 0x5bb]
    =================================
    0x56e: v56e(0x0) = CONST 
    0x570: v570 = SLOAD v56e(0x0)
    0x571: v571(0x1) = CONST 
    0x573: v573(0x1) = CONST 
    0x575: v575(0xa0) = CONST 
    0x577: v577(0x10000000000000000000000000000000000000000) = SHL v575(0xa0), v573(0x1)
    0x578: v578(0xffffffffffffffffffffffffffffffffffffffff) = SUB v577(0x10000000000000000000000000000000000000000), v571(0x1)
    0x579: v579 = AND v578(0xffffffffffffffffffffffffffffffffffffffff), v570
    0x57a: v57a = CALLER 
    0x57b: v57b = EQ v57a, v579
    0x57c: v57c(0x5bb) = CONST 
    0x57f: JUMPI v57c(0x5bb), v57b

    Begin block 0x580
    prev=[0x56d], succ=[]
    =================================
    0x580: v580(0x40) = CONST 
    0x583: v583 = MLOAD v580(0x40)
    0x584: v584(0x461bcd) = CONST 
    0x588: v588(0xe5) = CONST 
    0x58a: v58a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v588(0xe5), v584(0x461bcd)
    0x58c: MSTORE v583, v58a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x58d: v58d(0x20) = CONST 
    0x58f: v58f(0x4) = CONST 
    0x592: v592 = ADD v583, v58f(0x4)
    0x593: MSTORE v592, v58d(0x20)
    0x594: v594(0xc) = CONST 
    0x596: v596(0x24) = CONST 
    0x599: v599 = ADD v583, v596(0x24)
    0x59a: MSTORE v599, v594(0xc)
    0x59b: v59b(0x15539055551213d492569151) = CONST 
    0x5a8: v5a8(0xa2) = CONST 
    0x5aa: v5aa(0x554e415554484f52495a45440000000000000000000000000000000000000000) = SHL v5a8(0xa2), v59b(0x15539055551213d492569151)
    0x5ab: v5ab(0x44) = CONST 
    0x5ae: v5ae = ADD v583, v5ab(0x44)
    0x5af: MSTORE v5ae, v5aa(0x554e415554484f52495a45440000000000000000000000000000000000000000)
    0x5b1: v5b1 = MLOAD v580(0x40)
    0x5b5: v5b5(0x0) = SUB v583, v5b1
    0x5b6: v5b6(0x64) = CONST 
    0x5b8: v5b8(0x64) = ADD v5b6(0x64), v5b5(0x0)
    0x5ba: REVERT v5b1, v5b8(0x64)

    Begin block 0x5bb
    prev=[0x56d], succ=[0x95c]
    =================================
    0x5bc: v5bc(0x0) = CONST 
    0x5bf: v5bf = SLOAD v5bc(0x0)
    0x5c0: v5c0(0x1) = CONST 
    0x5c2: v5c2(0x1) = CONST 
    0x5c4: v5c4(0xa0) = CONST 
    0x5c6: v5c6(0x10000000000000000000000000000000000000000) = SHL v5c4(0xa0), v5c2(0x1)
    0x5c7: v5c7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c6(0x10000000000000000000000000000000000000000), v5c0(0x1)
    0x5ca: v5ca = AND v5c7(0xffffffffffffffffffffffffffffffffffffffff), v2f8
    0x5cb: v5cb(0x1) = CONST 
    0x5cd: v5cd(0x1) = CONST 
    0x5cf: v5cf(0xa0) = CONST 
    0x5d1: v5d1(0x10000000000000000000000000000000000000000) = SHL v5cf(0xa0), v5cd(0x1)
    0x5d2: v5d2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5d1(0x10000000000000000000000000000000000000000), v5cb(0x1)
    0x5d3: v5d3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5d2(0xffffffffffffffffffffffffffffffffffffffff)
    0x5d5: v5d5 = AND v5bf, v5d3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x5d7: v5d7 = OR v5ca, v5d5
    0x5da: SSTORE v5bc(0x0), v5d7
    0x5db: v5db(0x40) = CONST 
    0x5de: v5de = MLOAD v5db(0x40)
    0x5e2: v5e2 = AND v5bf, v5c7(0xffffffffffffffffffffffffffffffffffffffff)
    0x5e5: MSTORE v5de, v5e2
    0x5e6: v5e6(0x20) = CONST 
    0x5e9: v5e9 = ADD v5de, v5e6(0x20)
    0x5ed: MSTORE v5e9, v5ca
    0x5ef: v5ef = MLOAD v5db(0x40)
    0x5f0: v5f0(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x615: v615(0x0) = SUB v5de, v5ef
    0x618: v618(0x40) = ADD v5db(0x40), v615(0x0)
    0x61a: LOG1 v5ef, v618(0x40), v5f0(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x61d: JUMP v2d8(0x95c)

    Begin block 0x95c
    prev=[0x5bb], succ=[]
    =================================
    0x95d: STOP 

}

function weth()() public {
    Begin block 0x2ff
    prev=[], succ=[0x307, 0x30b]
    =================================
    0x300: v300 = CALLVALUE 
    0x302: v302 = ISZERO v300
    0x303: v303(0x30b) = CONST 
    0x306: JUMPI v303(0x30b), v302

    Begin block 0x307
    prev=[0x2ff], succ=[]
    =================================
    0x307: v307(0x0) = CONST 
    0x30a: REVERT v307(0x0), v307(0x0)

    Begin block 0x30b
    prev=[0x2ff], succ=[0x61e]
    =================================
    0x30d: v30d(0x97d) = CONST 
    0x310: v310(0x61e) = CONST 
    0x313: JUMP v310(0x61e)

    Begin block 0x61e
    prev=[0x30b], succ=[0x97d]
    =================================
    0x61f: v61f(0x7) = CONST 
    0x621: v621 = SLOAD v61f(0x7)
    0x622: v622(0x1) = CONST 
    0x624: v624(0x1) = CONST 
    0x626: v626(0xa0) = CONST 
    0x628: v628(0x10000000000000000000000000000000000000000) = SHL v626(0xa0), v624(0x1)
    0x629: v629(0xffffffffffffffffffffffffffffffffffffffff) = SUB v628(0x10000000000000000000000000000000000000000), v622(0x1)
    0x62a: v62a = AND v629(0xffffffffffffffffffffffffffffffffffffffff), v621
    0x62c: JUMP v30d(0x97d)

    Begin block 0x97d
    prev=[0x61e], succ=[]
    =================================
    0x97e: v97e(0x40) = CONST 
    0x981: v981 = MLOAD v97e(0x40)
    0x982: v982(0x1) = CONST 
    0x984: v984(0x1) = CONST 
    0x986: v986(0xa0) = CONST 
    0x988: v988(0x10000000000000000000000000000000000000000) = SHL v986(0xa0), v984(0x1)
    0x989: v989(0xffffffffffffffffffffffffffffffffffffffff) = SUB v988(0x10000000000000000000000000000000000000000), v982(0x1)
    0x98c: v98c = AND v62a, v989(0xffffffffffffffffffffffffffffffffffffffff)
    0x98e: MSTORE v981, v98c
    0x98f: v98f = MLOAD v97e(0x40)
    0x993: v993(0x0) = SUB v981, v98f
    0x994: v994(0x20) = CONST 
    0x996: v996(0x20) = ADD v994(0x20), v993(0x0)
    0x998: RETURN v98f, v996(0x20)

}

function lockPeriod()() public {
    Begin block 0x314
    prev=[], succ=[0x31c, 0x320]
    =================================
    0x315: v315 = CALLVALUE 
    0x317: v317 = ISZERO v315
    0x318: v318(0x320) = CONST 
    0x31b: JUMPI v318(0x320), v317

    Begin block 0x31c
    prev=[0x314], succ=[]
    =================================
    0x31c: v31c(0x0) = CONST 
    0x31f: REVERT v31c(0x0), v31c(0x0)

    Begin block 0x320
    prev=[0x314], succ=[0x62d]
    =================================
    0x322: v322(0x9b8) = CONST 
    0x325: v325(0x62d) = CONST 
    0x328: JUMP v325(0x62d)

    Begin block 0x62d
    prev=[0x320], succ=[0x9b8]
    =================================
    0x62e: v62e(0x3) = CONST 
    0x630: v630 = SLOAD v62e(0x3)
    0x632: JUMP v322(0x9b8)

    Begin block 0x9b8
    prev=[0x62d], succ=[]
    =================================
    0x9b9: v9b9(0x40) = CONST 
    0x9bc: v9bc = MLOAD v9b9(0x40)
    0x9bf: MSTORE v9bc, v630
    0x9c0: v9c0 = MLOAD v9b9(0x40)
    0x9c4: v9c4(0x0) = SUB v9bc, v9c0
    0x9c5: v9c5(0x20) = CONST 
    0x9c7: v9c7(0x20) = ADD v9c5(0x20), v9c4(0x0)
    0x9c9: RETURN v9c0, v9c7(0x20)

}

function governance()() public {
    Begin block 0x329
    prev=[], succ=[0x331, 0x335]
    =================================
    0x32a: v32a = CALLVALUE 
    0x32c: v32c = ISZERO v32a
    0x32d: v32d(0x335) = CONST 
    0x330: JUMPI v32d(0x335), v32c

    Begin block 0x331
    prev=[0x329], succ=[]
    =================================
    0x331: v331(0x0) = CONST 
    0x334: REVERT v331(0x0), v331(0x0)

    Begin block 0x335
    prev=[0x329], succ=[0x633]
    =================================
    0x337: v337(0x9e9) = CONST 
    0x33a: v33a(0x633) = CONST 
    0x33d: JUMP v33a(0x633)

    Begin block 0x633
    prev=[0x335], succ=[0x9e9]
    =================================
    0x634: v634(0x1) = CONST 
    0x636: v636 = SLOAD v634(0x1)
    0x637: v637(0x1) = CONST 
    0x639: v639(0x1) = CONST 
    0x63b: v63b(0xa0) = CONST 
    0x63d: v63d(0x10000000000000000000000000000000000000000) = SHL v63b(0xa0), v639(0x1)
    0x63e: v63e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v63d(0x10000000000000000000000000000000000000000), v637(0x1)
    0x63f: v63f = AND v63e(0xffffffffffffffffffffffffffffffffffffffff), v636
    0x641: JUMP v337(0x9e9)

    Begin block 0x9e9
    prev=[0x633], succ=[]
    =================================
    0x9ea: v9ea(0x40) = CONST 
    0x9ed: v9ed = MLOAD v9ea(0x40)
    0x9ee: v9ee(0x1) = CONST 
    0x9f0: v9f0(0x1) = CONST 
    0x9f2: v9f2(0xa0) = CONST 
    0x9f4: v9f4(0x10000000000000000000000000000000000000000) = SHL v9f2(0xa0), v9f0(0x1)
    0x9f5: v9f5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9f4(0x10000000000000000000000000000000000000000), v9ee(0x1)
    0x9f8: v9f8 = AND v63f, v9f5(0xffffffffffffffffffffffffffffffffffffffff)
    0x9fa: MSTORE v9ed, v9f8
    0x9fb: v9fb = MLOAD v9ea(0x40)
    0x9ff: v9ff(0x0) = SUB v9ed, v9fb
    0xa00: va00(0x20) = CONST 
    0xa02: va02(0x20) = ADD va00(0x20), v9ff(0x0)
    0xa04: RETURN v9fb, va02(0x20)

}

function implementation()() public {
    Begin block 0x33e
    prev=[], succ=[0x346, 0x34a]
    =================================
    0x33f: v33f = CALLVALUE 
    0x341: v341 = ISZERO v33f
    0x342: v342(0x34a) = CONST 
    0x345: JUMPI v342(0x34a), v341

    Begin block 0x346
    prev=[0x33e], succ=[]
    =================================
    0x346: v346(0x0) = CONST 
    0x349: REVERT v346(0x0), v346(0x0)

    Begin block 0x34a
    prev=[0x33e], succ=[0x642]
    =================================
    0x34c: v34c(0xa24) = CONST 
    0x34f: v34f(0x642) = CONST 
    0x352: JUMP v34f(0x642)

    Begin block 0x642
    prev=[0x34a], succ=[0xa24]
    =================================
    0x643: v643(0x2) = CONST 
    0x645: v645 = SLOAD v643(0x2)
    0x646: v646(0x1) = CONST 
    0x648: v648(0x1) = CONST 
    0x64a: v64a(0xa0) = CONST 
    0x64c: v64c(0x10000000000000000000000000000000000000000) = SHL v64a(0xa0), v648(0x1)
    0x64d: v64d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64c(0x10000000000000000000000000000000000000000), v646(0x1)
    0x64e: v64e = AND v64d(0xffffffffffffffffffffffffffffffffffffffff), v645
    0x650: JUMP v34c(0xa24)

    Begin block 0xa24
    prev=[0x642], succ=[]
    =================================
    0xa25: va25(0x40) = CONST 
    0xa28: va28 = MLOAD va25(0x40)
    0xa29: va29(0x1) = CONST 
    0xa2b: va2b(0x1) = CONST 
    0xa2d: va2d(0xa0) = CONST 
    0xa2f: va2f(0x10000000000000000000000000000000000000000) = SHL va2d(0xa0), va2b(0x1)
    0xa30: va30(0xffffffffffffffffffffffffffffffffffffffff) = SUB va2f(0x10000000000000000000000000000000000000000), va29(0x1)
    0xa33: va33 = AND v64e, va30(0xffffffffffffffffffffffffffffffffffffffff)
    0xa35: MSTORE va28, va33
    0xa36: va36 = MLOAD va25(0x40)
    0xa3a: va3a(0x0) = SUB va28, va36
    0xa3b: va3b(0x20) = CONST 
    0xa3d: va3d(0x20) = ADD va3b(0x20), va3a(0x0)
    0xa3f: RETURN va36, va3d(0x20)

}

function _setGovernance(address)() public {
    Begin block 0x353
    prev=[], succ=[0x35b, 0x35f]
    =================================
    0x354: v354 = CALLVALUE 
    0x356: v356 = ISZERO v354
    0x357: v357(0x35f) = CONST 
    0x35a: JUMPI v357(0x35f), v356

    Begin block 0x35b
    prev=[0x353], succ=[]
    =================================
    0x35b: v35b(0x0) = CONST 
    0x35e: REVERT v35b(0x0), v35b(0x0)

    Begin block 0x35f
    prev=[0x353], succ=[0x372, 0x376]
    =================================
    0x361: v361(0xa5f) = CONST 
    0x364: v364(0x4) = CONST 
    0x367: v367 = CALLDATASIZE 
    0x368: v368 = SUB v367, v364(0x4)
    0x369: v369(0x20) = CONST 
    0x36c: v36c = LT v368, v369(0x20)
    0x36d: v36d = ISZERO v36c
    0x36e: v36e(0x376) = CONST 
    0x371: JUMPI v36e(0x376), v36d

    Begin block 0x372
    prev=[0x35f], succ=[]
    =================================
    0x372: v372(0x0) = CONST 
    0x375: REVERT v372(0x0), v372(0x0)

    Begin block 0x376
    prev=[0x35f], succ=[0x651]
    =================================
    0x378: v378 = CALLDATALOAD v364(0x4)
    0x379: v379(0x1) = CONST 
    0x37b: v37b(0x1) = CONST 
    0x37d: v37d(0xa0) = CONST 
    0x37f: v37f(0x10000000000000000000000000000000000000000) = SHL v37d(0xa0), v37b(0x1)
    0x380: v380(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37f(0x10000000000000000000000000000000000000000), v379(0x1)
    0x381: v381 = AND v380(0xffffffffffffffffffffffffffffffffffffffff), v378
    0x382: v382(0x651) = CONST 
    0x385: JUMP v382(0x651)

    Begin block 0x651
    prev=[0x376], succ=[0x664, 0x69f]
    =================================
    0x652: v652(0x1) = CONST 
    0x654: v654 = SLOAD v652(0x1)
    0x655: v655(0x1) = CONST 
    0x657: v657(0x1) = CONST 
    0x659: v659(0xa0) = CONST 
    0x65b: v65b(0x10000000000000000000000000000000000000000) = SHL v659(0xa0), v657(0x1)
    0x65c: v65c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v65b(0x10000000000000000000000000000000000000000), v655(0x1)
    0x65d: v65d = AND v65c(0xffffffffffffffffffffffffffffffffffffffff), v654
    0x65e: v65e = CALLER 
    0x65f: v65f = EQ v65e, v65d
    0x660: v660(0x69f) = CONST 
    0x663: JUMPI v660(0x69f), v65f

    Begin block 0x664
    prev=[0x651], succ=[]
    =================================
    0x664: v664(0x40) = CONST 
    0x667: v667 = MLOAD v664(0x40)
    0x668: v668(0x461bcd) = CONST 
    0x66c: v66c(0xe5) = CONST 
    0x66e: v66e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v66c(0xe5), v668(0x461bcd)
    0x670: MSTORE v667, v66e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x671: v671(0x20) = CONST 
    0x673: v673(0x4) = CONST 
    0x676: v676 = ADD v667, v673(0x4)
    0x677: MSTORE v676, v671(0x20)
    0x678: v678(0xc) = CONST 
    0x67a: v67a(0x24) = CONST 
    0x67d: v67d = ADD v667, v67a(0x24)
    0x67e: MSTORE v67d, v678(0xc)
    0x67f: v67f(0x15539055551213d492569151) = CONST 
    0x68c: v68c(0xa2) = CONST 
    0x68e: v68e(0x554e415554484f52495a45440000000000000000000000000000000000000000) = SHL v68c(0xa2), v67f(0x15539055551213d492569151)
    0x68f: v68f(0x44) = CONST 
    0x692: v692 = ADD v667, v68f(0x44)
    0x693: MSTORE v692, v68e(0x554e415554484f52495a45440000000000000000000000000000000000000000)
    0x695: v695 = MLOAD v664(0x40)
    0x699: v699(0x0) = SUB v667, v695
    0x69a: v69a(0x64) = CONST 
    0x69c: v69c(0x64) = ADD v69a(0x64), v699(0x0)
    0x69e: REVERT v695, v69c(0x64)

    Begin block 0x69f
    prev=[0x651], succ=[0xa5f]
    =================================
    0x6a0: v6a0(0x1) = CONST 
    0x6a3: v6a3 = SLOAD v6a0(0x1)
    0x6a4: v6a4(0x1) = CONST 
    0x6a6: v6a6(0x1) = CONST 
    0x6a8: v6a8(0xa0) = CONST 
    0x6aa: v6aa(0x10000000000000000000000000000000000000000) = SHL v6a8(0xa0), v6a6(0x1)
    0x6ab: v6ab(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6aa(0x10000000000000000000000000000000000000000), v6a4(0x1)
    0x6ae: v6ae = AND v6ab(0xffffffffffffffffffffffffffffffffffffffff), v381
    0x6af: v6af(0x1) = CONST 
    0x6b1: v6b1(0x1) = CONST 
    0x6b3: v6b3(0xa0) = CONST 
    0x6b5: v6b5(0x10000000000000000000000000000000000000000) = SHL v6b3(0xa0), v6b1(0x1)
    0x6b6: v6b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b5(0x10000000000000000000000000000000000000000), v6af(0x1)
    0x6b7: v6b7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b9: v6b9 = AND v6a3, v6b7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x6bb: v6bb = OR v6ae, v6b9
    0x6be: SSTORE v6a0(0x1), v6bb
    0x6bf: v6bf(0x40) = CONST 
    0x6c2: v6c2 = MLOAD v6bf(0x40)
    0x6c6: v6c6 = AND v6a3, v6ab(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c9: MSTORE v6c2, v6c6
    0x6ca: v6ca(0x20) = CONST 
    0x6cd: v6cd = ADD v6c2, v6ca(0x20)
    0x6d1: MSTORE v6cd, v6ae
    0x6d3: v6d3 = MLOAD v6bf(0x40)
    0x6d4: v6d4(0x48da34dfe9ebb4198c3f70d8382467788dcee33984c79a74fa850772c4e5e36f) = CONST 
    0x6f9: v6f9(0x0) = SUB v6c2, v6d3
    0x6fc: v6fc(0x40) = ADD v6bf(0x40), v6f9(0x0)
    0x6fe: LOG1 v6d3, v6fc(0x40), v6d4(0x48da34dfe9ebb4198c3f70d8382467788dcee33984c79a74fa850772c4e5e36f)
    0x701: JUMP v361(0xa5f)

    Begin block 0xa5f
    prev=[0x69f], succ=[]
    =================================
    0xa60: STOP 

}

function balanceOf(address)() public {
    Begin block 0x386
    prev=[], succ=[0x38e, 0x392]
    =================================
    0x387: v387 = CALLVALUE 
    0x389: v389 = ISZERO v387
    0x38a: v38a(0x392) = CONST 
    0x38d: JUMPI v38a(0x392), v389

    Begin block 0x38e
    prev=[0x386], succ=[]
    =================================
    0x38e: v38e(0x0) = CONST 
    0x391: REVERT v38e(0x0), v38e(0x0)

    Begin block 0x392
    prev=[0x386], succ=[0x3a5, 0x3a9]
    =================================
    0x394: v394(0xa80) = CONST 
    0x397: v397(0x4) = CONST 
    0x39a: v39a = CALLDATASIZE 
    0x39b: v39b = SUB v39a, v397(0x4)
    0x39c: v39c(0x20) = CONST 
    0x39f: v39f = LT v39b, v39c(0x20)
    0x3a0: v3a0 = ISZERO v39f
    0x3a1: v3a1(0x3a9) = CONST 
    0x3a4: JUMPI v3a1(0x3a9), v3a0

    Begin block 0x3a5
    prev=[0x392], succ=[]
    =================================
    0x3a5: v3a5(0x0) = CONST 
    0x3a8: REVERT v3a5(0x0), v3a5(0x0)

    Begin block 0x3a9
    prev=[0x392], succ=[0x702]
    =================================
    0x3ab: v3ab = CALLDATALOAD v397(0x4)
    0x3ac: v3ac(0x1) = CONST 
    0x3ae: v3ae(0x1) = CONST 
    0x3b0: v3b0(0xa0) = CONST 
    0x3b2: v3b2(0x10000000000000000000000000000000000000000) = SHL v3b0(0xa0), v3ae(0x1)
    0x3b3: v3b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b2(0x10000000000000000000000000000000000000000), v3ac(0x1)
    0x3b4: v3b4 = AND v3b3(0xffffffffffffffffffffffffffffffffffffffff), v3ab
    0x3b5: v3b5(0x702) = CONST 
    0x3b8: JUMP v3b5(0x702)

    Begin block 0x702
    prev=[0x3a9], succ=[0xa80]
    =================================
    0x703: v703(0xc) = CONST 
    0x705: v705(0x20) = CONST 
    0x707: MSTORE v705(0x20), v703(0xc)
    0x708: v708(0x0) = CONST 
    0x70c: MSTORE v708(0x0), v3b4
    0x70d: v70d(0x40) = CONST 
    0x710: v710 = SHA3 v708(0x0), v70d(0x40)
    0x711: v711 = SLOAD v710
    0x713: JUMP v394(0xa80)

    Begin block 0xa80
    prev=[0x702], succ=[]
    =================================
    0xa81: va81(0x40) = CONST 
    0xa84: va84 = MLOAD va81(0x40)
    0xa87: MSTORE va84, v711
    0xa88: va88 = MLOAD va81(0x40)
    0xa8c: va8c(0x0) = SUB va84, va88
    0xa8d: va8d(0x20) = CONST 
    0xa8f: va8f(0x20) = ADD va8d(0x20), va8c(0x0)
    0xa91: RETURN va88, va8f(0x20)

}

function marketRegulator()() public {
    Begin block 0x3b9
    prev=[], succ=[0x3c1, 0x3c5]
    =================================
    0x3ba: v3ba = CALLVALUE 
    0x3bc: v3bc = ISZERO v3ba
    0x3bd: v3bd(0x3c5) = CONST 
    0x3c0: JUMPI v3bd(0x3c5), v3bc

    Begin block 0x3c1
    prev=[0x3b9], succ=[]
    =================================
    0x3c1: v3c1(0x0) = CONST 
    0x3c4: REVERT v3c1(0x0), v3c1(0x0)

    Begin block 0x3c5
    prev=[0x3b9], succ=[0x714]
    =================================
    0x3c7: v3c7(0xab1) = CONST 
    0x3ca: v3ca(0x714) = CONST 
    0x3cd: JUMP v3ca(0x714)

    Begin block 0x714
    prev=[0x3c5], succ=[0xab1]
    =================================
    0x715: v715(0x6) = CONST 
    0x717: v717 = SLOAD v715(0x6)
    0x718: v718(0x1) = CONST 
    0x71a: v71a(0x1) = CONST 
    0x71c: v71c(0xa0) = CONST 
    0x71e: v71e(0x10000000000000000000000000000000000000000) = SHL v71c(0xa0), v71a(0x1)
    0x71f: v71f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71e(0x10000000000000000000000000000000000000000), v718(0x1)
    0x720: v720 = AND v71f(0xffffffffffffffffffffffffffffffffffffffff), v717
    0x722: JUMP v3c7(0xab1)

    Begin block 0xab1
    prev=[0x714], succ=[]
    =================================
    0xab2: vab2(0x40) = CONST 
    0xab5: vab5 = MLOAD vab2(0x40)
    0xab6: vab6(0x1) = CONST 
    0xab8: vab8(0x1) = CONST 
    0xaba: vaba(0xa0) = CONST 
    0xabc: vabc(0x10000000000000000000000000000000000000000) = SHL vaba(0xa0), vab8(0x1)
    0xabd: vabd(0xffffffffffffffffffffffffffffffffffffffff) = SUB vabc(0x10000000000000000000000000000000000000000), vab6(0x1)
    0xac0: vac0 = AND v720, vabd(0xffffffffffffffffffffffffffffffffffffffff)
    0xac2: MSTORE vab5, vac0
    0xac3: vac3 = MLOAD vab2(0x40)
    0xac7: vac7(0x0) = SUB vab5, vac3
    0xac8: vac8(0x20) = CONST 
    0xaca: vaca(0x20) = ADD vac8(0x20), vac7(0x0)
    0xacc: RETURN vac3, vaca(0x20)

}

function symbol()() public {
    Begin block 0x3ce
    prev=[], succ=[0x3d6, 0x3da]
    =================================
    0x3cf: v3cf = CALLVALUE 
    0x3d1: v3d1 = ISZERO v3cf
    0x3d2: v3d2(0x3da) = CONST 
    0x3d5: JUMPI v3d2(0x3da), v3d1

    Begin block 0x3d6
    prev=[0x3ce], succ=[]
    =================================
    0x3d6: v3d6(0x0) = CONST 
    0x3d9: REVERT v3d6(0x0), v3d6(0x0)

    Begin block 0x3da
    prev=[0x3ce], succ=[0x1ac0x3ce]
    =================================
    0x3dc: v3dc(0x1ac) = CONST 
    0x3df: v3df(0x723) = CONST 
    0x3e2: v3e2_0, v3e2_1 = CALLPRIVATE v3df(0x723), v3dc(0x1ac)

    Begin block 0x1ac0x3ce
    prev=[0x3da], succ=[0x1ce0x3ce]
    =================================
    0x1ad0x3ce: v3ce1ad(0x40) = CONST 
    0x1b00x3ce: v3ce1b0 = MLOAD v3ce1ad(0x40)
    0x1b10x3ce: v3ce1b1(0x20) = CONST 
    0x1b50x3ce: MSTORE v3ce1b0, v3ce1b1(0x20)
    0x1b70x3ce: v3ce1b7 = MLOAD v3e2_0
    0x1ba0x3ce: v3ce1ba = ADD v3ce1b0, v3ce1b1(0x20)
    0x1bb0x3ce: MSTORE v3ce1ba, v3ce1b7
    0x1bd0x3ce: v3ce1bd = MLOAD v3e2_0
    0x1c40x3ce: v3ce1c4 = ADD v3ce1b0, v3ce1ad(0x40)
    0x1c70x3ce: v3ce1c7 = ADD v3e2_0, v3ce1b1(0x20)
    0x1cc0x3ce: v3ce1cc(0x0) = CONST 

    Begin block 0x1ce0x3ce
    prev=[0x1d70x3ce, 0x1ac0x3ce], succ=[0x1e60x3ce, 0x1d70x3ce]
    =================================
    0x1ce0x3ce_0x0: v1ce3ce_0 = PHI v3ce1e1, v3ce1cc(0x0)
    0x1d10x3ce: v3ce1d1 = LT v1ce3ce_0, v3ce1bd
    0x1d20x3ce: v3ce1d2 = ISZERO v3ce1d1
    0x1d30x3ce: v3ce1d3(0x1e6) = CONST 
    0x1d60x3ce: JUMPI v3ce1d3(0x1e6), v3ce1d2

    Begin block 0x1e60x3ce
    prev=[0x1ce0x3ce], succ=[0x2130x3ce, 0x1fa0x3ce]
    =================================
    0x1ef0x3ce: v3ce1ef = ADD v3ce1bd, v3ce1c4
    0x1f10x3ce: v3ce1f1(0x1f) = CONST 
    0x1f30x3ce: v3ce1f3 = AND v3ce1f1(0x1f), v3ce1bd
    0x1f50x3ce: v3ce1f5 = ISZERO v3ce1f3
    0x1f60x3ce: v3ce1f6(0x213) = CONST 
    0x1f90x3ce: JUMPI v3ce1f6(0x213), v3ce1f5

    Begin block 0x2130x3ce
    prev=[0x1e60x3ce, 0x1fa0x3ce], succ=[]
    =================================
    0x2130x3ce_0x1: v2133ce_1 = PHI v3ce210, v3ce1ef
    0x2190x3ce: v3ce219(0x40) = CONST 
    0x21b0x3ce: v3ce21b = MLOAD v3ce219(0x40)
    0x21e0x3ce: v3ce21e = SUB v2133ce_1, v3ce21b
    0x2200x3ce: RETURN v3ce21b, v3ce21e

    Begin block 0x1fa0x3ce
    prev=[0x1e60x3ce], succ=[0x2130x3ce]
    =================================
    0x1fc0x3ce: v3ce1fc = SUB v3ce1ef, v3ce1f3
    0x1fe0x3ce: v3ce1fe = MLOAD v3ce1fc
    0x1ff0x3ce: v3ce1ff(0x1) = CONST 
    0x2020x3ce: v3ce202(0x20) = CONST 
    0x2040x3ce: v3ce204 = SUB v3ce202(0x20), v3ce1f3
    0x2050x3ce: v3ce205(0x100) = CONST 
    0x2080x3ce: v3ce208 = EXP v3ce205(0x100), v3ce204
    0x2090x3ce: v3ce209 = SUB v3ce208, v3ce1ff(0x1)
    0x20a0x3ce: v3ce20a = NOT v3ce209
    0x20b0x3ce: v3ce20b = AND v3ce20a, v3ce1fe
    0x20d0x3ce: MSTORE v3ce1fc, v3ce20b
    0x20e0x3ce: v3ce20e(0x20) = CONST 
    0x2100x3ce: v3ce210 = ADD v3ce20e(0x20), v3ce1fc

    Begin block 0x1d70x3ce
    prev=[0x1ce0x3ce], succ=[0x1ce0x3ce]
    =================================
    0x1d70x3ce_0x0: v1d73ce_0 = PHI v3ce1e1, v3ce1cc(0x0)
    0x1d90x3ce: v3ce1d9 = ADD v1d73ce_0, v3ce1c7
    0x1da0x3ce: v3ce1da = MLOAD v3ce1d9
    0x1dd0x3ce: v3ce1dd = ADD v1d73ce_0, v3ce1c4
    0x1de0x3ce: MSTORE v3ce1dd, v3ce1da
    0x1df0x3ce: v3ce1df(0x20) = CONST 
    0x1e10x3ce: v3ce1e1 = ADD v3ce1df(0x20), v1d73ce_0
    0x1e20x3ce: v3ce1e2(0x1ce) = CONST 
    0x1e50x3ce: JUMP v3ce1e2(0x1ce)

}

function SHDToken()() public {
    Begin block 0x3e3
    prev=[], succ=[0x3eb, 0x3ef]
    =================================
    0x3e4: v3e4 = CALLVALUE 
    0x3e6: v3e6 = ISZERO v3e4
    0x3e7: v3e7(0x3ef) = CONST 
    0x3ea: JUMPI v3e7(0x3ef), v3e6

    Begin block 0x3eb
    prev=[0x3e3], succ=[]
    =================================
    0x3eb: v3eb(0x0) = CONST 
    0x3ee: REVERT v3eb(0x0), v3eb(0x0)

    Begin block 0x3ef
    prev=[0x3e3], succ=[0x77e]
    =================================
    0x3f1: v3f1(0xaec) = CONST 
    0x3f4: v3f4(0x77e) = CONST 
    0x3f7: JUMP v3f4(0x77e)

    Begin block 0x77e
    prev=[0x3ef], succ=[0xaec]
    =================================
    0x77f: v77f(0x4) = CONST 
    0x781: v781 = SLOAD v77f(0x4)
    0x782: v782(0x1) = CONST 
    0x784: v784(0x1) = CONST 
    0x786: v786(0xa0) = CONST 
    0x788: v788(0x10000000000000000000000000000000000000000) = SHL v786(0xa0), v784(0x1)
    0x789: v789(0xffffffffffffffffffffffffffffffffffffffff) = SUB v788(0x10000000000000000000000000000000000000000), v782(0x1)
    0x78a: v78a = AND v789(0xffffffffffffffffffffffffffffffffffffffff), v781
    0x78c: JUMP v3f1(0xaec)

    Begin block 0xaec
    prev=[0x77e], succ=[]
    =================================
    0xaed: vaed(0x40) = CONST 
    0xaf0: vaf0 = MLOAD vaed(0x40)
    0xaf1: vaf1(0x1) = CONST 
    0xaf3: vaf3(0x1) = CONST 
    0xaf5: vaf5(0xa0) = CONST 
    0xaf7: vaf7(0x10000000000000000000000000000000000000000) = SHL vaf5(0xa0), vaf3(0x1)
    0xaf8: vaf8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaf7(0x10000000000000000000000000000000000000000), vaf1(0x1)
    0xafb: vafb = AND v78a, vaf8(0xffffffffffffffffffffffffffffffffffffffff)
    0xafd: MSTORE vaf0, vafb
    0xafe: vafe = MLOAD vaed(0x40)
    0xb02: vb02(0x0) = SUB vaf0, vafe
    0xb03: vb03(0x20) = CONST 
    0xb05: vb05(0x20) = ADD vb03(0x20), vb02(0x0)
    0xb07: RETURN vafe, vb05(0x20)

}

function lockDeadline(address)() public {
    Begin block 0x3f8
    prev=[], succ=[0x400, 0x404]
    =================================
    0x3f9: v3f9 = CALLVALUE 
    0x3fb: v3fb = ISZERO v3f9
    0x3fc: v3fc(0x404) = CONST 
    0x3ff: JUMPI v3fc(0x404), v3fb

    Begin block 0x400
    prev=[0x3f8], succ=[]
    =================================
    0x400: v400(0x0) = CONST 
    0x403: REVERT v400(0x0), v400(0x0)

    Begin block 0x404
    prev=[0x3f8], succ=[0x417, 0x41b]
    =================================
    0x406: v406(0xb27) = CONST 
    0x409: v409(0x4) = CONST 
    0x40c: v40c = CALLDATASIZE 
    0x40d: v40d = SUB v40c, v409(0x4)
    0x40e: v40e(0x20) = CONST 
    0x411: v411 = LT v40d, v40e(0x20)
    0x412: v412 = ISZERO v411
    0x413: v413(0x41b) = CONST 
    0x416: JUMPI v413(0x41b), v412

    Begin block 0x417
    prev=[0x404], succ=[]
    =================================
    0x417: v417(0x0) = CONST 
    0x41a: REVERT v417(0x0), v417(0x0)

    Begin block 0x41b
    prev=[0x404], succ=[0x78d]
    =================================
    0x41d: v41d = CALLDATALOAD v409(0x4)
    0x41e: v41e(0x1) = CONST 
    0x420: v420(0x1) = CONST 
    0x422: v422(0xa0) = CONST 
    0x424: v424(0x10000000000000000000000000000000000000000) = SHL v422(0xa0), v420(0x1)
    0x425: v425(0xffffffffffffffffffffffffffffffffffffffff) = SUB v424(0x10000000000000000000000000000000000000000), v41e(0x1)
    0x426: v426 = AND v425(0xffffffffffffffffffffffffffffffffffffffff), v41d
    0x427: v427(0x78d) = CONST 
    0x42a: JUMP v427(0x78d)

    Begin block 0x78d
    prev=[0x41b], succ=[0xb27]
    =================================
    0x78e: v78e(0x8) = CONST 
    0x790: v790(0x20) = CONST 
    0x792: MSTORE v790(0x20), v78e(0x8)
    0x793: v793(0x0) = CONST 
    0x797: MSTORE v793(0x0), v426
    0x798: v798(0x40) = CONST 
    0x79b: v79b = SHA3 v793(0x0), v798(0x40)
    0x79c: v79c = SLOAD v79b
    0x79e: JUMP v406(0xb27)

    Begin block 0xb27
    prev=[0x78d], succ=[]
    =================================
    0xb28: vb28(0x40) = CONST 
    0xb2b: vb2b = MLOAD vb28(0x40)
    0xb2e: MSTORE vb2b, v79c
    0xb2f: vb2f = MLOAD vb28(0x40)
    0xb33: vb33(0x0) = SUB vb2b, vb2f
    0xb34: vb34(0x20) = CONST 
    0xb36: vb36(0x20) = ADD vb34(0x20), vb33(0x0)
    0xb38: RETURN vb2f, vb36(0x20)

}

function _setImplementation(address)() public {
    Begin block 0x42b
    prev=[], succ=[0x433, 0x437]
    =================================
    0x42c: v42c = CALLVALUE 
    0x42e: v42e = ISZERO v42c
    0x42f: v42f(0x437) = CONST 
    0x432: JUMPI v42f(0x437), v42e

    Begin block 0x433
    prev=[0x42b], succ=[]
    =================================
    0x433: v433(0x0) = CONST 
    0x436: REVERT v433(0x0), v433(0x0)

    Begin block 0x437
    prev=[0x42b], succ=[0x44a, 0x44e]
    =================================
    0x439: v439(0xb58) = CONST 
    0x43c: v43c(0x4) = CONST 
    0x43f: v43f = CALLDATASIZE 
    0x440: v440 = SUB v43f, v43c(0x4)
    0x441: v441(0x20) = CONST 
    0x444: v444 = LT v440, v441(0x20)
    0x445: v445 = ISZERO v444
    0x446: v446(0x44e) = CONST 
    0x449: JUMPI v446(0x44e), v445

    Begin block 0x44a
    prev=[0x437], succ=[]
    =================================
    0x44a: v44a(0x0) = CONST 
    0x44d: REVERT v44a(0x0), v44a(0x0)

    Begin block 0x44e
    prev=[0x437], succ=[0x79f]
    =================================
    0x450: v450 = CALLDATALOAD v43c(0x4)
    0x451: v451(0x1) = CONST 
    0x453: v453(0x1) = CONST 
    0x455: v455(0xa0) = CONST 
    0x457: v457(0x10000000000000000000000000000000000000000) = SHL v455(0xa0), v453(0x1)
    0x458: v458(0xffffffffffffffffffffffffffffffffffffffff) = SUB v457(0x10000000000000000000000000000000000000000), v451(0x1)
    0x459: v459 = AND v458(0xffffffffffffffffffffffffffffffffffffffff), v450
    0x45a: v45a(0x79f) = CONST 
    0x45d: JUMP v45a(0x79f)

    Begin block 0x79f
    prev=[0x44e], succ=[0x7b2, 0x7e8]
    =================================
    0x7a0: v7a0(0x1) = CONST 
    0x7a2: v7a2 = SLOAD v7a0(0x1)
    0x7a3: v7a3(0x1) = CONST 
    0x7a5: v7a5(0x1) = CONST 
    0x7a7: v7a7(0xa0) = CONST 
    0x7a9: v7a9(0x10000000000000000000000000000000000000000) = SHL v7a7(0xa0), v7a5(0x1)
    0x7aa: v7aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7a9(0x10000000000000000000000000000000000000000), v7a3(0x1)
    0x7ab: v7ab = AND v7aa(0xffffffffffffffffffffffffffffffffffffffff), v7a2
    0x7ac: v7ac = CALLER 
    0x7ad: v7ad = EQ v7ac, v7ab
    0x7ae: v7ae(0x7e8) = CONST 
    0x7b1: JUMPI v7ae(0x7e8), v7ad

    Begin block 0x7b2
    prev=[0x79f], succ=[]
    =================================
    0x7b2: v7b2(0x40) = CONST 
    0x7b4: v7b4 = MLOAD v7b2(0x40)
    0x7b5: v7b5(0x461bcd) = CONST 
    0x7b9: v7b9(0xe5) = CONST 
    0x7bb: v7bb(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7b9(0xe5), v7b5(0x461bcd)
    0x7bd: MSTORE v7b4, v7bb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7be: v7be(0x4) = CONST 
    0x7c0: v7c0 = ADD v7be(0x4), v7b4
    0x7c3: v7c3(0x20) = CONST 
    0x7c5: v7c5 = ADD v7c3(0x20), v7c0
    0x7c8: v7c8(0x20) = SUB v7c5, v7c0
    0x7ca: MSTORE v7c0, v7c8(0x20)
    0x7cb: v7cb(0x2d) = CONST 
    0x7ce: MSTORE v7c5, v7cb(0x2d)
    0x7cf: v7cf(0x20) = CONST 
    0x7d1: v7d1 = ADD v7cf(0x20), v7c5
    0x7d3: v7d3(0x877) = CONST 
    0x7d6: v7d6(0x2d) = CONST 
    0x7d9: CODECOPY v7d1, v7d3(0x877), v7d6(0x2d)
    0x7da: v7da(0x40) = CONST 
    0x7dc: v7dc = ADD v7da(0x40), v7d1
    0x7e0: v7e0(0x40) = CONST 
    0x7e2: v7e2 = MLOAD v7e0(0x40)
    0x7e5: v7e5(0x84) = SUB v7dc, v7e2
    0x7e7: REVERT v7e2, v7e5(0x84)

    Begin block 0x7e8
    prev=[0x79f], succ=[0xb58]
    =================================
    0x7e9: v7e9(0x2) = CONST 
    0x7ec: v7ec = SLOAD v7e9(0x2)
    0x7ed: v7ed(0x1) = CONST 
    0x7ef: v7ef(0x1) = CONST 
    0x7f1: v7f1(0xa0) = CONST 
    0x7f3: v7f3(0x10000000000000000000000000000000000000000) = SHL v7f1(0xa0), v7ef(0x1)
    0x7f4: v7f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7f3(0x10000000000000000000000000000000000000000), v7ed(0x1)
    0x7f7: v7f7 = AND v7f4(0xffffffffffffffffffffffffffffffffffffffff), v459
    0x7f8: v7f8(0x1) = CONST 
    0x7fa: v7fa(0x1) = CONST 
    0x7fc: v7fc(0xa0) = CONST 
    0x7fe: v7fe(0x10000000000000000000000000000000000000000) = SHL v7fc(0xa0), v7fa(0x1)
    0x7ff: v7ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fe(0x10000000000000000000000000000000000000000), v7f8(0x1)
    0x800: v800(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v7ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x802: v802 = AND v7ec, v800(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x803: v803 = OR v802, v7f7
    0x807: SSTORE v7e9(0x2), v803
    0x808: v808(0x40) = CONST 
    0x80b: v80b = MLOAD v808(0x40)
    0x80e: v80e = AND v7f4(0xffffffffffffffffffffffffffffffffffffffff), v7ec
    0x811: MSTORE v80b, v80e
    0x815: v815 = AND v7f4(0xffffffffffffffffffffffffffffffffffffffff), v803
    0x816: v816(0x20) = CONST 
    0x819: v819 = ADD v80b, v816(0x20)
    0x81a: MSTORE v819, v815
    0x81c: v81c = MLOAD v808(0x40)
    0x81d: v81d(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x841: v841(0x0) = SUB v80b, v81c
    0x844: v844(0x40) = ADD v808(0x40), v841(0x0)
    0x846: LOG1 v81c, v844(0x40), v81d(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x849: JUMP v439(0xb58)

    Begin block 0xb58
    prev=[0x7e8], succ=[]
    =================================
    0xb59: STOP 

}

function allowance(address,address)() public {
    Begin block 0x45e
    prev=[], succ=[0x466, 0x46a]
    =================================
    0x45f: v45f = CALLVALUE 
    0x461: v461 = ISZERO v45f
    0x462: v462(0x46a) = CONST 
    0x465: JUMPI v462(0x46a), v461

    Begin block 0x466
    prev=[0x45e], succ=[]
    =================================
    0x466: v466(0x0) = CONST 
    0x469: REVERT v466(0x0), v466(0x0)

    Begin block 0x46a
    prev=[0x45e], succ=[0x47d, 0x481]
    =================================
    0x46c: v46c(0xb79) = CONST 
    0x46f: v46f(0x4) = CONST 
    0x472: v472 = CALLDATASIZE 
    0x473: v473 = SUB v472, v46f(0x4)
    0x474: v474(0x40) = CONST 
    0x477: v477 = LT v473, v474(0x40)
    0x478: v478 = ISZERO v477
    0x479: v479(0x481) = CONST 
    0x47c: JUMPI v479(0x481), v478

    Begin block 0x47d
    prev=[0x46a], succ=[]
    =================================
    0x47d: v47d(0x0) = CONST 
    0x480: REVERT v47d(0x0), v47d(0x0)

    Begin block 0x481
    prev=[0x46a], succ=[0x84a]
    =================================
    0x483: v483(0x1) = CONST 
    0x485: v485(0x1) = CONST 
    0x487: v487(0xa0) = CONST 
    0x489: v489(0x10000000000000000000000000000000000000000) = SHL v487(0xa0), v485(0x1)
    0x48a: v48a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v489(0x10000000000000000000000000000000000000000), v483(0x1)
    0x48c: v48c = CALLDATALOAD v46f(0x4)
    0x48e: v48e = AND v48a(0xffffffffffffffffffffffffffffffffffffffff), v48c
    0x490: v490(0x20) = CONST 
    0x492: v492(0x24) = ADD v490(0x20), v46f(0x4)
    0x493: v493 = CALLDATALOAD v492(0x24)
    0x494: v494 = AND v493, v48a(0xffffffffffffffffffffffffffffffffffffffff)
    0x495: v495(0x84a) = CONST 
    0x498: JUMP v495(0x84a)

    Begin block 0x84a
    prev=[0x481], succ=[0xb79]
    =================================
    0x84b: v84b(0xd) = CONST 
    0x84d: v84d(0x20) = CONST 
    0x851: MSTORE v84d(0x20), v84b(0xd)
    0x852: v852(0x0) = CONST 
    0x856: MSTORE v852(0x0), v48e
    0x857: v857(0x40) = CONST 
    0x85b: v85b = SHA3 v852(0x0), v857(0x40)
    0x85e: MSTORE v84d(0x20), v85b
    0x861: MSTORE v852(0x0), v494
    0x863: v863 = SHA3 v852(0x0), v857(0x40)
    0x864: v864 = SLOAD v863
    0x866: JUMP v46c(0xb79)

    Begin block 0xb79
    prev=[0x84a], succ=[]
    =================================
    0xb7a: vb7a(0x40) = CONST 
    0xb7d: vb7d = MLOAD vb7a(0x40)
    0xb80: MSTORE vb7d, v864
    0xb81: vb81 = MLOAD vb7a(0x40)
    0xb85: vb85(0x0) = SUB vb7d, vb81
    0xb86: vb86(0x20) = CONST 
    0xb88: vb88(0x20) = ADD vb86(0x20), vb85(0x0)
    0xb8a: RETURN vb81, vb88(0x20)

}

function admin()() public {
    Begin block 0x499
    prev=[], succ=[0x4a1, 0x4a5]
    =================================
    0x49a: v49a = CALLVALUE 
    0x49c: v49c = ISZERO v49a
    0x49d: v49d(0x4a5) = CONST 
    0x4a0: JUMPI v49d(0x4a5), v49c

    Begin block 0x4a1
    prev=[0x499], succ=[]
    =================================
    0x4a1: v4a1(0x0) = CONST 
    0x4a4: REVERT v4a1(0x0), v4a1(0x0)

    Begin block 0x4a5
    prev=[0x499], succ=[0x867]
    =================================
    0x4a7: v4a7(0xbaa) = CONST 
    0x4aa: v4aa(0x867) = CONST 
    0x4ad: JUMP v4aa(0x867)

    Begin block 0x867
    prev=[0x4a5], succ=[0xbaa]
    =================================
    0x868: v868(0x0) = CONST 
    0x86a: v86a = SLOAD v868(0x0)
    0x86b: v86b(0x1) = CONST 
    0x86d: v86d(0x1) = CONST 
    0x86f: v86f(0xa0) = CONST 
    0x871: v871(0x10000000000000000000000000000000000000000) = SHL v86f(0xa0), v86d(0x1)
    0x872: v872(0xffffffffffffffffffffffffffffffffffffffff) = SUB v871(0x10000000000000000000000000000000000000000), v86b(0x1)
    0x873: v873 = AND v872(0xffffffffffffffffffffffffffffffffffffffff), v86a
    0x875: JUMP v4a7(0xbaa)

    Begin block 0xbaa
    prev=[0x867], succ=[]
    =================================
    0xbab: vbab(0x40) = CONST 
    0xbae: vbae = MLOAD vbab(0x40)
    0xbaf: vbaf(0x1) = CONST 
    0xbb1: vbb1(0x1) = CONST 
    0xbb3: vbb3(0xa0) = CONST 
    0xbb5: vbb5(0x10000000000000000000000000000000000000000) = SHL vbb3(0xa0), vbb1(0x1)
    0xbb6: vbb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb5(0x10000000000000000000000000000000000000000), vbaf(0x1)
    0xbb9: vbb9 = AND v873, vbb6(0xffffffffffffffffffffffffffffffffffffffff)
    0xbbb: MSTORE vbae, vbb9
    0xbbc: vbbc = MLOAD vbab(0x40)
    0xbc0: vbc0(0x0) = SUB vbae, vbbc
    0xbc1: vbc1(0x20) = CONST 
    0xbc3: vbc3(0x20) = ADD vbc1(0x20), vbc0(0x0)
    0xbc5: RETURN vbbc, vbc3(0x20)

}

function 0x4ae(0x4aearg0x0) private {
    Begin block 0x4ae
    prev=[], succ=[0xbe5, 0x4ee]
    =================================
    0x4af: v4af(0x9) = CONST 
    0x4b2: v4b2 = SLOAD v4af(0x9)
    0x4b3: v4b3(0x40) = CONST 
    0x4b6: v4b6 = MLOAD v4b3(0x40)
    0x4b7: v4b7(0x20) = CONST 
    0x4b9: v4b9(0x2) = CONST 
    0x4bb: v4bb(0x1) = CONST 
    0x4be: v4be = AND v4b2, v4bb(0x1)
    0x4bf: v4bf = ISZERO v4be
    0x4c0: v4c0(0x100) = CONST 
    0x4c3: v4c3 = MUL v4c0(0x100), v4bf
    0x4c4: v4c4(0x0) = CONST 
    0x4c6: v4c6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v4c4(0x0)
    0x4c7: v4c7 = ADD v4c6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v4c3
    0x4ca: v4ca = AND v4b2, v4c7
    0x4ce: v4ce = DIV v4ca, v4b9(0x2)
    0x4cf: v4cf(0x1f) = CONST 
    0x4d2: v4d2 = ADD v4ce, v4cf(0x1f)
    0x4d5: v4d5 = DIV v4d2, v4b7(0x20)
    0x4d7: v4d7 = MUL v4b7(0x20), v4d5
    0x4d9: v4d9 = ADD v4b6, v4d7
    0x4db: v4db = ADD v4b7(0x20), v4d9
    0x4de: MSTORE v4b3(0x40), v4db
    0x4e1: MSTORE v4b6, v4ce
    0x4e5: v4e5 = ADD v4b6, v4b7(0x20)
    0x4e9: v4e9 = ISZERO v4ce
    0x4ea: v4ea(0xbe5) = CONST 
    0x4ed: JUMPI v4ea(0xbe5), v4e9

    Begin block 0xbe5
    prev=[0x4ae], succ=[]
    =================================
    0xbec: RETURNPRIVATE v4aearg0, v4b6, v4aearg0

    Begin block 0x4ee
    prev=[0x4ae], succ=[0x4f6, 0x5090x4ae]
    =================================
    0x4ef: v4ef(0x1f) = CONST 
    0x4f1: v4f1 = LT v4ef(0x1f), v4ce
    0x4f2: v4f2(0x509) = CONST 
    0x4f5: JUMPI v4f2(0x509), v4f1

    Begin block 0x4f6
    prev=[0x4ee], succ=[0xc0c]
    =================================
    0x4f6: v4f6(0x100) = CONST 
    0x4fb: v4fb = SLOAD v4af(0x9)
    0x4fc: v4fc = DIV v4fb, v4f6(0x100)
    0x4fd: v4fd = MUL v4fc, v4f6(0x100)
    0x4ff: MSTORE v4e5, v4fd
    0x501: v501(0x20) = CONST 
    0x503: v503 = ADD v501(0x20), v4e5
    0x505: v505(0xc0c) = CONST 
    0x508: JUMP v505(0xc0c)

    Begin block 0xc0c
    prev=[0x4f6], succ=[]
    =================================
    0xc13: RETURNPRIVATE v4aearg0, v4b6, v4aearg0

    Begin block 0x5090x4ae
    prev=[0x4ee], succ=[0x5170x4ae]
    =================================
    0x50b0x4ae: v4ae50b = ADD v4e5, v4ce
    0x50e0x4ae: v4ae50e(0x0) = CONST 
    0x5100x4ae: MSTORE v4ae50e(0x0), v4af(0x9)
    0x5110x4ae: v4ae511(0x20) = CONST 
    0x5130x4ae: v4ae513(0x0) = CONST 
    0x5150x4ae: v4ae515 = SHA3 v4ae513(0x0), v4ae511(0x20)

    Begin block 0x5170x4ae
    prev=[0x5170x4ae, 0x5090x4ae], succ=[0x5170x4ae, 0x52b0x4ae]
    =================================
    0x5170x4ae_0x0: v5174ae_0 = PHI v4e5, v4ae523
    0x5170x4ae_0x1: v5174ae_1 = PHI v4ae51f, v4ae515
    0x5190x4ae: v4ae519 = SLOAD v5174ae_1
    0x51b0x4ae: MSTORE v5174ae_0, v4ae519
    0x51d0x4ae: v4ae51d(0x1) = CONST 
    0x51f0x4ae: v4ae51f = ADD v4ae51d(0x1), v5174ae_1
    0x5210x4ae: v4ae521(0x20) = CONST 
    0x5230x4ae: v4ae523 = ADD v4ae521(0x20), v5174ae_0
    0x5260x4ae: v4ae526 = GT v4ae50b, v4ae523
    0x5270x4ae: v4ae527(0x517) = CONST 
    0x52a0x4ae: JUMPI v4ae527(0x517), v4ae526

    Begin block 0x52b0x4ae
    prev=[0x5170x4ae], succ=[0x5340x4ae]
    =================================
    0x52d0x4ae: v4ae52d = SUB v4ae523, v4ae50b
    0x52e0x4ae: v4ae52e(0x1f) = CONST 
    0x5300x4ae: v4ae530 = AND v4ae52e(0x1f), v4ae52d
    0x5320x4ae: v4ae532 = ADD v4ae50b, v4ae530

    Begin block 0x5340x4ae
    prev=[0x52b0x4ae], succ=[]
    =================================
    0x53b0x4ae: RETURNPRIVATE v4aearg0, v4b6, v4aearg0

}

function 0x723(0x723arg0x0) private {
    Begin block 0x723
    prev=[], succ=[0xc33, 0x763]
    =================================
    0x724: v724(0xa) = CONST 
    0x727: v727 = SLOAD v724(0xa)
    0x728: v728(0x40) = CONST 
    0x72b: v72b = MLOAD v728(0x40)
    0x72c: v72c(0x20) = CONST 
    0x72e: v72e(0x2) = CONST 
    0x730: v730(0x1) = CONST 
    0x733: v733 = AND v727, v730(0x1)
    0x734: v734 = ISZERO v733
    0x735: v735(0x100) = CONST 
    0x738: v738 = MUL v735(0x100), v734
    0x739: v739(0x0) = CONST 
    0x73b: v73b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v739(0x0)
    0x73c: v73c = ADD v73b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v738
    0x73f: v73f = AND v727, v73c
    0x743: v743 = DIV v73f, v72e(0x2)
    0x744: v744(0x1f) = CONST 
    0x747: v747 = ADD v743, v744(0x1f)
    0x74a: v74a = DIV v747, v72c(0x20)
    0x74c: v74c = MUL v72c(0x20), v74a
    0x74e: v74e = ADD v72b, v74c
    0x750: v750 = ADD v72c(0x20), v74e
    0x753: MSTORE v728(0x40), v750
    0x756: MSTORE v72b, v743
    0x75a: v75a = ADD v72b, v72c(0x20)
    0x75e: v75e = ISZERO v743
    0x75f: v75f(0xc33) = CONST 
    0x762: JUMPI v75f(0xc33), v75e

    Begin block 0xc33
    prev=[0x723], succ=[]
    =================================
    0xc3a: RETURNPRIVATE v723arg0, v72b, v723arg0

    Begin block 0x763
    prev=[0x723], succ=[0x76b, 0x5090x723]
    =================================
    0x764: v764(0x1f) = CONST 
    0x766: v766 = LT v764(0x1f), v743
    0x767: v767(0x509) = CONST 
    0x76a: JUMPI v767(0x509), v766

    Begin block 0x76b
    prev=[0x763], succ=[0xc5a]
    =================================
    0x76b: v76b(0x100) = CONST 
    0x770: v770 = SLOAD v724(0xa)
    0x771: v771 = DIV v770, v76b(0x100)
    0x772: v772 = MUL v771, v76b(0x100)
    0x774: MSTORE v75a, v772
    0x776: v776(0x20) = CONST 
    0x778: v778 = ADD v776(0x20), v75a
    0x77a: v77a(0xc5a) = CONST 
    0x77d: JUMP v77a(0xc5a)

    Begin block 0xc5a
    prev=[0x76b], succ=[]
    =================================
    0xc61: RETURNPRIVATE v723arg0, v72b, v723arg0

    Begin block 0x5090x723
    prev=[0x763], succ=[0x5170x723]
    =================================
    0x50b0x723: v72350b = ADD v75a, v743
    0x50e0x723: v72350e(0x0) = CONST 
    0x5100x723: MSTORE v72350e(0x0), v724(0xa)
    0x5110x723: v723511(0x20) = CONST 
    0x5130x723: v723513(0x0) = CONST 
    0x5150x723: v723515 = SHA3 v723513(0x0), v723511(0x20)

    Begin block 0x5170x723
    prev=[0x5170x723, 0x5090x723], succ=[0x5170x723, 0x52b0x723]
    =================================
    0x5170x723_0x0: v517723_0 = PHI v75a, v723523
    0x5170x723_0x1: v517723_1 = PHI v72351f, v723515
    0x5190x723: v723519 = SLOAD v517723_1
    0x51b0x723: MSTORE v517723_0, v723519
    0x51d0x723: v72351d(0x1) = CONST 
    0x51f0x723: v72351f = ADD v72351d(0x1), v517723_1
    0x5210x723: v723521(0x20) = CONST 
    0x5230x723: v723523 = ADD v723521(0x20), v517723_0
    0x5260x723: v723526 = GT v72350b, v723523
    0x5270x723: v723527(0x517) = CONST 
    0x52a0x723: JUMPI v723527(0x517), v723526

    Begin block 0x52b0x723
    prev=[0x5170x723], succ=[0x5340x723]
    =================================
    0x52d0x723: v72352d = SUB v723523, v72350b
    0x52e0x723: v72352e(0x1f) = CONST 
    0x5300x723: v723530 = AND v72352e(0x1f), v72352d
    0x5320x723: v723532 = ADD v72350b, v723530

    Begin block 0x5340x723
    prev=[0x52b0x723], succ=[]
    =================================
    0x53b0x723: RETURNPRIVATE v723arg0, v72b, v723arg0

}

function fallback()() public {
    Begin block 0xc88
    prev=[], succ=[]
    =================================
    0x113: STOP 

}

