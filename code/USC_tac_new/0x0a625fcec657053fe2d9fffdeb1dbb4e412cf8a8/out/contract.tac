function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xd46]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xd1a: vd1a(0xd46) = CONST 
    0xd1b: JUMPI vd1a(0xd46), v8

    Begin block 0xd
    prev=[0x0], succ=[0xab, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x797bf385) = CONST 
    0x19: v19 = GT v14(0x797bf385), v12
    0x1a: v1a(0xab) = CONST 
    0x1d: JUMPI v1a(0xab), v19

    Begin block 0xab
    prev=[0xd], succ=[0xf2, 0xb7]
    =================================
    0xad: vad(0x3291c11a) = CONST 
    0xb2: vb2 = GT vad(0x3291c11a), v12
    0xb3: vb3(0xf2) = CONST 
    0xb6: JUMPI vb3(0xf2), vb2

    Begin block 0xf2
    prev=[0xab], succ=[0xd49, 0xfe]
    =================================
    0xf4: vf4(0x6fdde03) = CONST 
    0xf9: vf9 = EQ vf4(0x6fdde03), v12
    0xd3c: vd3c(0xd49) = CONST 
    0xd3d: JUMPI vd3c(0xd49), vf9

    Begin block 0xd49
    prev=[0xf2], succ=[]
    =================================
    0xd4a: vd4a(0x1a6) = CONST 
    0xd4b: CALLPRIVATE vd4a(0x1a6)

    Begin block 0xfe
    prev=[0xf2], succ=[0xd4c, 0x109]
    =================================
    0xff: vff(0x18160ddd) = CONST 
    0x104: v104 = EQ vff(0x18160ddd), v12
    0xd3e: vd3e(0xd4c) = CONST 
    0xd3f: JUMPI vd3e(0xd4c), v104

    Begin block 0xd4c
    prev=[0xfe], succ=[]
    =================================
    0xd4d: vd4d(0x230) = CONST 
    0xd4e: CALLPRIVATE vd4d(0x230)

    Begin block 0x109
    prev=[0xfe], succ=[0xd4f, 0x114]
    =================================
    0x10a: v10a(0x1d0806ae) = CONST 
    0x10f: v10f = EQ v10a(0x1d0806ae), v12
    0xd40: vd40(0xd4f) = CONST 
    0xd41: JUMPI vd40(0xd4f), v10f

    Begin block 0xd4f
    prev=[0x109], succ=[]
    =================================
    0xd50: vd50(0x257) = CONST 
    0xd51: CALLPRIVATE vd50(0x257)

    Begin block 0x114
    prev=[0x109], succ=[0xd52, 0x11f]
    =================================
    0x115: v115(0x1f68f20a) = CONST 
    0x11a: v11a = EQ v115(0x1f68f20a), v12
    0xd42: vd42(0xd52) = CONST 
    0xd43: JUMPI vd42(0xd52), v11a

    Begin block 0xd52
    prev=[0x114], succ=[]
    =================================
    0xd53: vd53(0x26c) = CONST 
    0xd54: CALLPRIVATE vd53(0x26c)

    Begin block 0x11f
    prev=[0x114], succ=[0xd46, 0xd55]
    =================================
    0x120: v120(0x313ce567) = CONST 
    0x125: v125 = EQ v120(0x313ce567), v12
    0xd44: vd44(0xd55) = CONST 
    0xd45: JUMPI vd44(0xd55), v125

    Begin block 0xd46
    prev=[0x0, 0x11f], succ=[]
    =================================
    0xd47: vd47(0x12a) = CONST 
    0xd48: CALLPRIVATE vd47(0x12a)

    Begin block 0xd55
    prev=[0x11f], succ=[]
    =================================
    0xd56: vd56(0x281) = CONST 
    0xd57: CALLPRIVATE vd56(0x281)

    Begin block 0xb7
    prev=[0xab], succ=[0xd58, 0xc2]
    =================================
    0xb8: vb8(0x3291c11a) = CONST 
    0xbd: vbd = EQ vb8(0x3291c11a), v12
    0xd32: vd32(0xd58) = CONST 
    0xd33: JUMPI vd32(0xd58), vbd

    Begin block 0xd58
    prev=[0xb7], succ=[]
    =================================
    0xd59: vd59(0x2ac) = CONST 
    0xd5a: CALLPRIVATE vd59(0x2ac)

    Begin block 0xc2
    prev=[0xb7], succ=[0xd5b, 0xcd]
    =================================
    0xc3: vc3(0x330691ac) = CONST 
    0xc8: vc8 = EQ vc3(0x330691ac), v12
    0xd34: vd34(0xd5b) = CONST 
    0xd35: JUMPI vd34(0xd5b), vc8

    Begin block 0xd5b
    prev=[0xc2], succ=[]
    =================================
    0xd5c: vd5c(0x2d6) = CONST 
    0xd5d: CALLPRIVATE vd5c(0x2d6)

    Begin block 0xcd
    prev=[0xc2], succ=[0xd5e, 0xd8]
    =================================
    0xce: vce(0x56e07d70) = CONST 
    0xd3: vd3 = EQ vce(0x56e07d70), v12
    0xd36: vd36(0xd5e) = CONST 
    0xd37: JUMPI vd36(0xd5e), vd3

    Begin block 0xd5e
    prev=[0xcd], succ=[]
    =================================
    0xd5f: vd5f(0x2eb) = CONST 
    0xd60: CALLPRIVATE vd5f(0x2eb)

    Begin block 0xd8
    prev=[0xcd], succ=[0xd61, 0xe3]
    =================================
    0xd9: vd9(0x70a08231) = CONST 
    0xde: vde = EQ vd9(0x70a08231), v12
    0xd38: vd38(0xd61) = CONST 
    0xd39: JUMPI vd38(0xd61), vde

    Begin block 0xd61
    prev=[0xd8], succ=[]
    =================================
    0xd62: vd62(0x300) = CONST 
    0xd63: CALLPRIVATE vd62(0x300)

    Begin block 0xe3
    prev=[0xd8], succ=[0xee, 0xd64]
    =================================
    0xe4: ve4(0x776d1a01) = CONST 
    0xe9: ve9 = EQ ve4(0x776d1a01), v12
    0xd3a: vd3a(0xd64) = CONST 
    0xd3b: JUMPI vd3a(0xd64), ve9

    Begin block 0xee
    prev=[0xe3], succ=[]
    =================================
    0xee: vee(0x12a) = CONST 
    0xf1: JUMP vee(0x12a)

    Begin block 0xd64
    prev=[0xe3], succ=[]
    =================================
    0xd65: vd65(0x333) = CONST 
    0xd66: CALLPRIVATE vd65(0x333)

    Begin block 0x1e
    prev=[0xd], succ=[0x6f, 0x29]
    =================================
    0x1f: v1f(0x95d89b41) = CONST 
    0x24: v24 = GT v1f(0x95d89b41), v12
    0x25: v25(0x6f) = CONST 
    0x28: JUMPI v25(0x6f), v24

    Begin block 0x6f
    prev=[0x1e], succ=[0xd67, 0x7b]
    =================================
    0x71: v71(0x797bf385) = CONST 
    0x76: v76 = EQ v71(0x797bf385), v12
    0xd28: vd28(0xd67) = CONST 
    0xd29: JUMPI vd28(0xd67), v76

    Begin block 0xd67
    prev=[0x6f], succ=[]
    =================================
    0xd68: vd68(0x366) = CONST 
    0xd69: CALLPRIVATE vd68(0x366)

    Begin block 0x7b
    prev=[0x6f], succ=[0xd6a, 0x86]
    =================================
    0x7c: v7c(0x7b7933b4) = CONST 
    0x81: v81 = EQ v7c(0x7b7933b4), v12
    0xd2a: vd2a(0xd6a) = CONST 
    0xd2b: JUMPI vd2a(0xd6a), v81

    Begin block 0xd6a
    prev=[0x7b], succ=[]
    =================================
    0xd6b: vd6b(0x397) = CONST 
    0xd6c: CALLPRIVATE vd6b(0x397)

    Begin block 0x86
    prev=[0x7b], succ=[0xd6d, 0x91]
    =================================
    0x87: v87(0x7e37c08c) = CONST 
    0x8c: v8c = EQ v87(0x7e37c08c), v12
    0xd2c: vd2c(0xd6d) = CONST 
    0xd2d: JUMPI vd2c(0xd6d), v8c

    Begin block 0xd6d
    prev=[0x86], succ=[]
    =================================
    0xd6e: vd6e(0x3ac) = CONST 
    0xd6f: CALLPRIVATE vd6e(0x3ac)

    Begin block 0x91
    prev=[0x86], succ=[0xd70, 0x9c]
    =================================
    0x92: v92(0x8da5cb5b) = CONST 
    0x97: v97 = EQ v92(0x8da5cb5b), v12
    0xd2e: vd2e(0xd70) = CONST 
    0xd2f: JUMPI vd2e(0xd70), v97

    Begin block 0xd70
    prev=[0x91], succ=[]
    =================================
    0xd71: vd71(0x3c1) = CONST 
    0xd72: CALLPRIVATE vd71(0x3c1)

    Begin block 0x9c
    prev=[0x91], succ=[0xa7, 0xd73]
    =================================
    0x9d: v9d(0x8f32d59b) = CONST 
    0xa2: va2 = EQ v9d(0x8f32d59b), v12
    0xd30: vd30(0xd73) = CONST 
    0xd31: JUMPI vd30(0xd73), va2

    Begin block 0xa7
    prev=[0x9c], succ=[]
    =================================
    0xa7: va7(0x12a) = CONST 
    0xaa: JUMP va7(0x12a)

    Begin block 0xd73
    prev=[0x9c], succ=[]
    =================================
    0xd74: vd74(0x3d6) = CONST 
    0xd75: CALLPRIVATE vd74(0x3d6)

    Begin block 0x29
    prev=[0x1e], succ=[0xd76, 0x34]
    =================================
    0x2a: v2a(0x95d89b41) = CONST 
    0x2f: v2f = EQ v2a(0x95d89b41), v12
    0xd1c: vd1c(0xd76) = CONST 
    0xd1d: JUMPI vd1c(0xd76), v2f

    Begin block 0xd76
    prev=[0x29], succ=[]
    =================================
    0xd77: vd77(0x3ff) = CONST 
    0xd78: CALLPRIVATE vd77(0x3ff)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xd79]
    =================================
    0x35: v35(0xba0e43bf) = CONST 
    0x3a: v3a = EQ v35(0xba0e43bf), v12
    0xd1e: vd1e(0xd79) = CONST 
    0xd1f: JUMPI vd1e(0xd79), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xd7c, 0x4a]
    =================================
    0x40: v40(0xd759dbeb) = CONST 
    0x45: v45 = EQ v40(0xd759dbeb), v12
    0xd20: vd20(0xd7c) = CONST 
    0xd21: JUMPI vd20(0xd7c), v45

    Begin block 0xd7c
    prev=[0x3f], succ=[]
    =================================
    0xd7d: vd7d(0x429) = CONST 
    0xd7e: CALLPRIVATE vd7d(0x429)

    Begin block 0x4a
    prev=[0x3f], succ=[0xd7f, 0x55]
    =================================
    0x4b: v4b(0xdd62ed3e) = CONST 
    0x50: v50 = EQ v4b(0xdd62ed3e), v12
    0xd22: vd22(0xd7f) = CONST 
    0xd23: JUMPI vd22(0xd7f), v50

    Begin block 0xd7f
    prev=[0x4a], succ=[]
    =================================
    0xd80: vd80(0x43e) = CONST 
    0xd81: CALLPRIVATE vd80(0x43e)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0xd82]
    =================================
    0x56: v56(0xef2b0b39) = CONST 
    0x5b: v5b = EQ v56(0xef2b0b39), v12
    0xd24: vd24(0xd82) = CONST 
    0xd25: JUMPI vd24(0xd82), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x6b, 0xd85]
    =================================
    0x61: v61(0xf2fde38b) = CONST 
    0x66: v66 = EQ v61(0xf2fde38b), v12
    0xd26: vd26(0xd85) = CONST 
    0xd27: JUMPI vd26(0xd85), v66

    Begin block 0x6b
    prev=[0x60], succ=[]
    =================================
    0x6b: v6b(0x12a) = CONST 
    0x6e: JUMP v6b(0x12a)

    Begin block 0xd85
    prev=[0x60], succ=[]
    =================================
    0xd86: vd86(0x48e) = CONST 
    0xd87: CALLPRIVATE vd86(0x48e)

    Begin block 0xd82
    prev=[0x55], succ=[]
    =================================
    0xd83: vd83(0x479) = CONST 
    0xd84: CALLPRIVATE vd83(0x479)

    Begin block 0xd79
    prev=[0x34], succ=[]
    =================================
    0xd7a: vd7a(0x414) = CONST 
    0xd7b: CALLPRIVATE vd7a(0x414)

}

function fallback()() public {
    Begin block 0x12a
    prev=[], succ=[0x134, 0x138]
    =================================
    0x12b: v12b(0x8fc) = CONST 
    0x12e: v12e = GAS 
    0x12f: v12f = GT v12e, v12b(0x8fc)
    0x130: v130(0x138) = CONST 
    0x133: JUMPI v130(0x138), v12f

    Begin block 0x134
    prev=[0x12a], succ=[0x903]
    =================================
    0x134: v134(0x903) = CONST 
    0x137: JUMP v134(0x903)

    Begin block 0x903
    prev=[0x134], succ=[]
    =================================
    0x904: STOP 

    Begin block 0x138
    prev=[0x12a], succ=[0x1a0, 0x19d]
    =================================
    0x139: v139(0x14) = CONST 
    0x13b: v13b = SLOAD v139(0x14)
    0x13c: v13c(0x40) = CONST 
    0x13f: v13f = MLOAD v13c(0x40)
    0x140: v140(0x20) = CONST 
    0x142: v142 = CALLDATASIZE 
    0x143: v143(0x1f) = CONST 
    0x146: v146 = ADD v142, v143(0x1f)
    0x149: v149 = DIV v146, v140(0x20)
    0x14b: v14b = MUL v140(0x20), v149
    0x14d: v14d = ADD v13f, v14b
    0x14f: v14f = ADD v140(0x20), v14d
    0x152: MSTORE v13c(0x40), v14f
    0x155: MSTORE v13f, v142
    0x156: v156(0x1) = CONST 
    0x158: v158(0x1) = CONST 
    0x15a: v15a(0xa0) = CONST 
    0x15c: v15c(0x10000000000000000000000000000000000000000) = SHL v15a(0xa0), v158(0x1)
    0x15d: v15d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15c(0x10000000000000000000000000000000000000000), v156(0x1)
    0x160: v160 = AND v13b, v15d(0xffffffffffffffffffffffffffffffffffffffff)
    0x162: v162(0x60) = CONST 
    0x165: v165(0x0) = CONST 
    0x16b: v16b = ADD v13f, v140(0x20)
    0x171: CALLDATACOPY v16b, v165(0x0), v142
    0x172: v172(0x0) = CONST 
    0x175: v175 = ADD v16b, v142
    0x178: MSTORE v175, v172(0x0)
    0x17b: v17b = MLOAD v13f
    0x186: v186(0x20) = CONST 
    0x189: v189 = ADD v13f, v186(0x20)
    0x18b: v18b = GAS 
    0x18c: v18c = DELEGATECALL v18b, v160, v189, v17b, v172(0x0), v172(0x0)
    0x18d: v18d = RETURNDATASIZE 
    0x18e: v18e(0x40) = CONST 
    0x190: v190 = MLOAD v18e(0x40)
    0x192: v192(0x0) = CONST 
    0x195: RETURNDATACOPY v190, v192(0x0), v18d
    0x198: v198 = ISZERO v18c
    0x199: v199(0x1a0) = CONST 
    0x19c: JUMPI v199(0x1a0), v198

    Begin block 0x1a0
    prev=[0x138], succ=[]
    =================================
    0x1a3: REVERT v190, v18d

    Begin block 0x19d
    prev=[0x138], succ=[]
    =================================
    0x19f: RETURN v190, v18d

}

function name()() public {
    Begin block 0x1a6
    prev=[], succ=[0x1ae, 0x1b2]
    =================================
    0x1a7: v1a7 = CALLVALUE 
    0x1a9: v1a9 = ISZERO v1a7
    0x1aa: v1aa(0x1b2) = CONST 
    0x1ad: JUMPI v1aa(0x1b2), v1a9

    Begin block 0x1ae
    prev=[0x1a6], succ=[]
    =================================
    0x1ae: v1ae(0x0) = CONST 
    0x1b1: REVERT v1ae(0x0), v1ae(0x0)

    Begin block 0x1b2
    prev=[0x1a6], succ=[0x1bb0x1a6]
    =================================
    0x1b4: v1b4(0x1bb) = CONST 
    0x1b7: v1b7(0x4c1) = CONST 
    0x1ba: v1ba_0, v1ba_1 = CALLPRIVATE v1b7(0x4c1), v1b4(0x1bb)

    Begin block 0x1bb0x1a6
    prev=[0x1b2], succ=[0x1dd0x1a6]
    =================================
    0x1bc0x1a6: v1a61bc(0x40) = CONST 
    0x1bf0x1a6: v1a61bf = MLOAD v1a61bc(0x40)
    0x1c00x1a6: v1a61c0(0x20) = CONST 
    0x1c40x1a6: MSTORE v1a61bf, v1a61c0(0x20)
    0x1c60x1a6: v1a61c6 = MLOAD v1ba_0
    0x1c90x1a6: v1a61c9 = ADD v1a61bf, v1a61c0(0x20)
    0x1ca0x1a6: MSTORE v1a61c9, v1a61c6
    0x1cc0x1a6: v1a61cc = MLOAD v1ba_0
    0x1d30x1a6: v1a61d3 = ADD v1a61bf, v1a61bc(0x40)
    0x1d60x1a6: v1a61d6 = ADD v1ba_0, v1a61c0(0x20)
    0x1db0x1a6: v1a61db(0x0) = CONST 

    Begin block 0x1dd0x1a6
    prev=[0x1e60x1a6, 0x1bb0x1a6], succ=[0x1f50x1a6, 0x1e60x1a6]
    =================================
    0x1dd0x1a6_0x0: v1dd1a6_0 = PHI v1a61f0, v1a61db(0x0)
    0x1e00x1a6: v1a61e0 = LT v1dd1a6_0, v1a61cc
    0x1e10x1a6: v1a61e1 = ISZERO v1a61e0
    0x1e20x1a6: v1a61e2(0x1f5) = CONST 
    0x1e50x1a6: JUMPI v1a61e2(0x1f5), v1a61e1

    Begin block 0x1f50x1a6
    prev=[0x1dd0x1a6], succ=[0x2220x1a6, 0x2090x1a6]
    =================================
    0x1fe0x1a6: v1a61fe = ADD v1a61cc, v1a61d3
    0x2000x1a6: v1a6200(0x1f) = CONST 
    0x2020x1a6: v1a6202 = AND v1a6200(0x1f), v1a61cc
    0x2040x1a6: v1a6204 = ISZERO v1a6202
    0x2050x1a6: v1a6205(0x222) = CONST 
    0x2080x1a6: JUMPI v1a6205(0x222), v1a6204

    Begin block 0x2220x1a6
    prev=[0x1f50x1a6, 0x2090x1a6], succ=[]
    =================================
    0x2220x1a6_0x1: v2221a6_1 = PHI v1a621f, v1a61fe
    0x2280x1a6: v1a6228(0x40) = CONST 
    0x22a0x1a6: v1a622a = MLOAD v1a6228(0x40)
    0x22d0x1a6: v1a622d = SUB v2221a6_1, v1a622a
    0x22f0x1a6: RETURN v1a622a, v1a622d

    Begin block 0x2090x1a6
    prev=[0x1f50x1a6], succ=[0x2220x1a6]
    =================================
    0x20b0x1a6: v1a620b = SUB v1a61fe, v1a6202
    0x20d0x1a6: v1a620d = MLOAD v1a620b
    0x20e0x1a6: v1a620e(0x1) = CONST 
    0x2110x1a6: v1a6211(0x20) = CONST 
    0x2130x1a6: v1a6213 = SUB v1a6211(0x20), v1a6202
    0x2140x1a6: v1a6214(0x100) = CONST 
    0x2170x1a6: v1a6217 = EXP v1a6214(0x100), v1a6213
    0x2180x1a6: v1a6218 = SUB v1a6217, v1a620e(0x1)
    0x2190x1a6: v1a6219 = NOT v1a6218
    0x21a0x1a6: v1a621a = AND v1a6219, v1a620d
    0x21c0x1a6: MSTORE v1a620b, v1a621a
    0x21d0x1a6: v1a621d(0x20) = CONST 
    0x21f0x1a6: v1a621f = ADD v1a621d(0x20), v1a620b

    Begin block 0x1e60x1a6
    prev=[0x1dd0x1a6], succ=[0x1dd0x1a6]
    =================================
    0x1e60x1a6_0x0: v1e61a6_0 = PHI v1a61f0, v1a61db(0x0)
    0x1e80x1a6: v1a61e8 = ADD v1e61a6_0, v1a61d6
    0x1e90x1a6: v1a61e9 = MLOAD v1a61e8
    0x1ec0x1a6: v1a61ec = ADD v1e61a6_0, v1a61d3
    0x1ed0x1a6: MSTORE v1a61ec, v1a61e9
    0x1ee0x1a6: v1a61ee(0x20) = CONST 
    0x1f00x1a6: v1a61f0 = ADD v1a61ee(0x20), v1e61a6_0
    0x1f10x1a6: v1a61f1(0x1dd) = CONST 
    0x1f40x1a6: JUMP v1a61f1(0x1dd)

}

function totalSupply()() public {
    Begin block 0x230
    prev=[], succ=[0x238, 0x23c]
    =================================
    0x231: v231 = CALLVALUE 
    0x233: v233 = ISZERO v231
    0x234: v234(0x23c) = CONST 
    0x237: JUMPI v234(0x23c), v233

    Begin block 0x238
    prev=[0x230], succ=[]
    =================================
    0x238: v238(0x0) = CONST 
    0x23b: REVERT v238(0x0), v238(0x0)

    Begin block 0x23c
    prev=[0x230], succ=[0x54c]
    =================================
    0x23e: v23e(0x924) = CONST 
    0x241: v241(0x54c) = CONST 
    0x244: JUMP v241(0x54c)

    Begin block 0x54c
    prev=[0x23c], succ=[0x924]
    =================================
    0x54d: v54d(0x13) = CONST 
    0x54f: v54f = SLOAD v54d(0x13)
    0x551: JUMP v23e(0x924)

    Begin block 0x924
    prev=[0x54c], succ=[]
    =================================
    0x925: v925(0x40) = CONST 
    0x928: v928 = MLOAD v925(0x40)
    0x92b: MSTORE v928, v54f
    0x92c: v92c = MLOAD v925(0x40)
    0x930: v930(0x0) = SUB v928, v92c
    0x931: v931(0x20) = CONST 
    0x933: v933(0x20) = ADD v931(0x20), v930(0x0)
    0x935: RETURN v92c, v933(0x20)

}

function initialPrice()() public {
    Begin block 0x257
    prev=[], succ=[0x25f, 0x263]
    =================================
    0x258: v258 = CALLVALUE 
    0x25a: v25a = ISZERO v258
    0x25b: v25b(0x263) = CONST 
    0x25e: JUMPI v25b(0x263), v25a

    Begin block 0x25f
    prev=[0x257], succ=[]
    =================================
    0x25f: v25f(0x0) = CONST 
    0x262: REVERT v25f(0x0), v25f(0x0)

    Begin block 0x263
    prev=[0x257], succ=[0x552]
    =================================
    0x265: v265(0x955) = CONST 
    0x268: v268(0x552) = CONST 
    0x26b: JUMP v268(0x552)

    Begin block 0x552
    prev=[0x263], succ=[0x955]
    =================================
    0x553: v553(0xe) = CONST 
    0x555: v555 = SLOAD v553(0xe)
    0x557: JUMP v265(0x955)

    Begin block 0x955
    prev=[0x552], succ=[]
    =================================
    0x956: v956(0x40) = CONST 
    0x959: v959 = MLOAD v956(0x40)
    0x95c: MSTORE v959, v555
    0x95d: v95d = MLOAD v956(0x40)
    0x961: v961(0x0) = SUB v959, v95d
    0x962: v962(0x20) = CONST 
    0x964: v964(0x20) = ADD v962(0x20), v961(0x0)
    0x966: RETURN v95d, v964(0x20)

}

function baseRate()() public {
    Begin block 0x26c
    prev=[], succ=[0x274, 0x278]
    =================================
    0x26d: v26d = CALLVALUE 
    0x26f: v26f = ISZERO v26d
    0x270: v270(0x278) = CONST 
    0x273: JUMPI v270(0x278), v26f

    Begin block 0x274
    prev=[0x26c], succ=[]
    =================================
    0x274: v274(0x0) = CONST 
    0x277: REVERT v274(0x0), v274(0x0)

    Begin block 0x278
    prev=[0x26c], succ=[0x558]
    =================================
    0x27a: v27a(0x986) = CONST 
    0x27d: v27d(0x558) = CONST 
    0x280: JUMP v27d(0x558)

    Begin block 0x558
    prev=[0x278], succ=[0x986]
    =================================
    0x559: v559(0x5) = CONST 
    0x55b: v55b = SLOAD v559(0x5)
    0x55d: JUMP v27a(0x986)

    Begin block 0x986
    prev=[0x558], succ=[]
    =================================
    0x987: v987(0x40) = CONST 
    0x98a: v98a = MLOAD v987(0x40)
    0x98d: MSTORE v98a, v55b
    0x98e: v98e = MLOAD v987(0x40)
    0x992: v992(0x0) = SUB v98a, v98e
    0x993: v993(0x20) = CONST 
    0x995: v995(0x20) = ADD v993(0x20), v992(0x0)
    0x997: RETURN v98e, v995(0x20)

}

function decimals()() public {
    Begin block 0x281
    prev=[], succ=[0x289, 0x28d]
    =================================
    0x282: v282 = CALLVALUE 
    0x284: v284 = ISZERO v282
    0x285: v285(0x28d) = CONST 
    0x288: JUMPI v285(0x28d), v284

    Begin block 0x289
    prev=[0x281], succ=[]
    =================================
    0x289: v289(0x0) = CONST 
    0x28c: REVERT v289(0x0), v289(0x0)

    Begin block 0x28d
    prev=[0x281], succ=[0x55e]
    =================================
    0x28f: v28f(0x296) = CONST 
    0x292: v292(0x55e) = CONST 
    0x295: JUMP v292(0x55e)

    Begin block 0x55e
    prev=[0x28d], succ=[0x296]
    =================================
    0x55f: v55f(0x4) = CONST 
    0x561: v561 = SLOAD v55f(0x4)
    0x562: v562(0xff) = CONST 
    0x564: v564 = AND v562(0xff), v561
    0x566: JUMP v28f(0x296)

    Begin block 0x296
    prev=[0x55e], succ=[]
    =================================
    0x297: v297(0x40) = CONST 
    0x29a: v29a = MLOAD v297(0x40)
    0x29b: v29b(0xff) = CONST 
    0x29f: v29f = AND v564, v29b(0xff)
    0x2a1: MSTORE v29a, v29f
    0x2a2: v2a2 = MLOAD v297(0x40)
    0x2a6: v2a6(0x0) = SUB v29a, v2a2
    0x2a7: v2a7(0x20) = CONST 
    0x2a9: v2a9(0x20) = ADD v2a7(0x20), v2a6(0x0)
    0x2ab: RETURN v2a2, v2a9(0x20)

}

function loanParamsIds(uint256)() public {
    Begin block 0x2ac
    prev=[], succ=[0x2b4, 0x2b8]
    =================================
    0x2ad: v2ad = CALLVALUE 
    0x2af: v2af = ISZERO v2ad
    0x2b0: v2b0(0x2b8) = CONST 
    0x2b3: JUMPI v2b0(0x2b8), v2af

    Begin block 0x2b4
    prev=[0x2ac], succ=[]
    =================================
    0x2b4: v2b4(0x0) = CONST 
    0x2b7: REVERT v2b4(0x0), v2b4(0x0)

    Begin block 0x2b8
    prev=[0x2ac], succ=[0x2cb, 0x2cf]
    =================================
    0x2ba: v2ba(0x9b7) = CONST 
    0x2bd: v2bd(0x4) = CONST 
    0x2c0: v2c0 = CALLDATASIZE 
    0x2c1: v2c1 = SUB v2c0, v2bd(0x4)
    0x2c2: v2c2(0x20) = CONST 
    0x2c5: v2c5 = LT v2c1, v2c2(0x20)
    0x2c6: v2c6 = ISZERO v2c5
    0x2c7: v2c7(0x2cf) = CONST 
    0x2ca: JUMPI v2c7(0x2cf), v2c6

    Begin block 0x2cb
    prev=[0x2b8], succ=[]
    =================================
    0x2cb: v2cb(0x0) = CONST 
    0x2ce: REVERT v2cb(0x0), v2cb(0x0)

    Begin block 0x2cf
    prev=[0x2b8], succ=[0x567]
    =================================
    0x2d1: v2d1 = CALLDATALOAD v2bd(0x4)
    0x2d2: v2d2(0x567) = CONST 
    0x2d5: JUMP v2d2(0x567)

    Begin block 0x567
    prev=[0x2cf], succ=[0x9b7]
    =================================
    0x568: v568(0xf) = CONST 
    0x56a: v56a(0x20) = CONST 
    0x56c: MSTORE v56a(0x20), v568(0xf)
    0x56d: v56d(0x0) = CONST 
    0x571: MSTORE v56d(0x0), v2d1
    0x572: v572(0x40) = CONST 
    0x575: v575 = SHA3 v56d(0x0), v572(0x40)
    0x576: v576 = SLOAD v575
    0x578: JUMP v2ba(0x9b7)

    Begin block 0x9b7
    prev=[0x567], succ=[]
    =================================
    0x9b8: v9b8(0x40) = CONST 
    0x9bb: v9bb = MLOAD v9b8(0x40)
    0x9be: MSTORE v9bb, v576
    0x9bf: v9bf = MLOAD v9b8(0x40)
    0x9c3: v9c3(0x0) = SUB v9bb, v9bf
    0x9c4: v9c4(0x20) = CONST 
    0x9c6: v9c6(0x20) = ADD v9c4(0x20), v9c3(0x0)
    0x9c8: RETURN v9bf, v9c6(0x20)

}

function rateMultiplier()() public {
    Begin block 0x2d6
    prev=[], succ=[0x2de, 0x2e2]
    =================================
    0x2d7: v2d7 = CALLVALUE 
    0x2d9: v2d9 = ISZERO v2d7
    0x2da: v2da(0x2e2) = CONST 
    0x2dd: JUMPI v2da(0x2e2), v2d9

    Begin block 0x2de
    prev=[0x2d6], succ=[]
    =================================
    0x2de: v2de(0x0) = CONST 
    0x2e1: REVERT v2de(0x0), v2de(0x0)

    Begin block 0x2e2
    prev=[0x2d6], succ=[0x579]
    =================================
    0x2e4: v2e4(0x9e8) = CONST 
    0x2e7: v2e7(0x579) = CONST 
    0x2ea: JUMP v2e7(0x579)

    Begin block 0x579
    prev=[0x2e2], succ=[0x9e8]
    =================================
    0x57a: v57a(0x6) = CONST 
    0x57c: v57c = SLOAD v57a(0x6)
    0x57e: JUMP v2e4(0x9e8)

    Begin block 0x9e8
    prev=[0x579], succ=[]
    =================================
    0x9e9: v9e9(0x40) = CONST 
    0x9ec: v9ec = MLOAD v9e9(0x40)
    0x9ef: MSTORE v9ec, v57c
    0x9f0: v9f0 = MLOAD v9e9(0x40)
    0x9f4: v9f4(0x0) = SUB v9ec, v9f0
    0x9f5: v9f5(0x20) = CONST 
    0x9f7: v9f7(0x20) = ADD v9f5(0x20), v9f4(0x0)
    0x9f9: RETURN v9f0, v9f7(0x20)

}

function kinkLevel()() public {
    Begin block 0x2eb
    prev=[], succ=[0x2f3, 0x2f7]
    =================================
    0x2ec: v2ec = CALLVALUE 
    0x2ee: v2ee = ISZERO v2ec
    0x2ef: v2ef(0x2f7) = CONST 
    0x2f2: JUMPI v2ef(0x2f7), v2ee

    Begin block 0x2f3
    prev=[0x2eb], succ=[]
    =================================
    0x2f3: v2f3(0x0) = CONST 
    0x2f6: REVERT v2f3(0x0), v2f3(0x0)

    Begin block 0x2f7
    prev=[0x2eb], succ=[0x57f]
    =================================
    0x2f9: v2f9(0xa19) = CONST 
    0x2fc: v2fc(0x57f) = CONST 
    0x2ff: JUMP v2fc(0x57f)

    Begin block 0x57f
    prev=[0x2f7], succ=[0xa19]
    =================================
    0x580: v580(0xa) = CONST 
    0x582: v582 = SLOAD v580(0xa)
    0x584: JUMP v2f9(0xa19)

    Begin block 0xa19
    prev=[0x57f], succ=[]
    =================================
    0xa1a: va1a(0x40) = CONST 
    0xa1d: va1d = MLOAD va1a(0x40)
    0xa20: MSTORE va1d, v582
    0xa21: va21 = MLOAD va1a(0x40)
    0xa25: va25(0x0) = SUB va1d, va21
    0xa26: va26(0x20) = CONST 
    0xa28: va28(0x20) = ADD va26(0x20), va25(0x0)
    0xa2a: RETURN va21, va28(0x20)

}

function balanceOf(address)() public {
    Begin block 0x300
    prev=[], succ=[0x308, 0x30c]
    =================================
    0x301: v301 = CALLVALUE 
    0x303: v303 = ISZERO v301
    0x304: v304(0x30c) = CONST 
    0x307: JUMPI v304(0x30c), v303

    Begin block 0x308
    prev=[0x300], succ=[]
    =================================
    0x308: v308(0x0) = CONST 
    0x30b: REVERT v308(0x0), v308(0x0)

    Begin block 0x30c
    prev=[0x300], succ=[0x31f, 0x323]
    =================================
    0x30e: v30e(0xa4a) = CONST 
    0x311: v311(0x4) = CONST 
    0x314: v314 = CALLDATASIZE 
    0x315: v315 = SUB v314, v311(0x4)
    0x316: v316(0x20) = CONST 
    0x319: v319 = LT v315, v316(0x20)
    0x31a: v31a = ISZERO v319
    0x31b: v31b(0x323) = CONST 
    0x31e: JUMPI v31b(0x323), v31a

    Begin block 0x31f
    prev=[0x30c], succ=[]
    =================================
    0x31f: v31f(0x0) = CONST 
    0x322: REVERT v31f(0x0), v31f(0x0)

    Begin block 0x323
    prev=[0x30c], succ=[0x585]
    =================================
    0x325: v325 = CALLDATALOAD v311(0x4)
    0x326: v326(0x1) = CONST 
    0x328: v328(0x1) = CONST 
    0x32a: v32a(0xa0) = CONST 
    0x32c: v32c(0x10000000000000000000000000000000000000000) = SHL v32a(0xa0), v328(0x1)
    0x32d: v32d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v32c(0x10000000000000000000000000000000000000000), v326(0x1)
    0x32e: v32e = AND v32d(0xffffffffffffffffffffffffffffffffffffffff), v325
    0x32f: v32f(0x585) = CONST 
    0x332: JUMP v32f(0x585)

    Begin block 0x585
    prev=[0x323], succ=[0xa4a]
    =================================
    0x586: v586(0x1) = CONST 
    0x588: v588(0x1) = CONST 
    0x58a: v58a(0xa0) = CONST 
    0x58c: v58c(0x10000000000000000000000000000000000000000) = SHL v58a(0xa0), v588(0x1)
    0x58d: v58d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v58c(0x10000000000000000000000000000000000000000), v586(0x1)
    0x58e: v58e = AND v58d(0xffffffffffffffffffffffffffffffffffffffff), v32e
    0x58f: v58f(0x0) = CONST 
    0x593: MSTORE v58f(0x0), v58e
    0x594: v594(0x11) = CONST 
    0x596: v596(0x20) = CONST 
    0x598: MSTORE v596(0x20), v594(0x11)
    0x599: v599(0x40) = CONST 
    0x59c: v59c = SHA3 v58f(0x0), v599(0x40)
    0x59d: v59d = SLOAD v59c
    0x59f: JUMP v30e(0xa4a)

    Begin block 0xa4a
    prev=[0x585], succ=[]
    =================================
    0xa4b: va4b(0x40) = CONST 
    0xa4e: va4e = MLOAD va4b(0x40)
    0xa51: MSTORE va4e, v59d
    0xa52: va52 = MLOAD va4b(0x40)
    0xa56: va56(0x0) = SUB va4e, va52
    0xa57: va57(0x20) = CONST 
    0xa59: va59(0x20) = ADD va57(0x20), va56(0x0)
    0xa5b: RETURN va52, va59(0x20)

}

function setTarget(address)() public {
    Begin block 0x333
    prev=[], succ=[0x33b, 0x33f]
    =================================
    0x334: v334 = CALLVALUE 
    0x336: v336 = ISZERO v334
    0x337: v337(0x33f) = CONST 
    0x33a: JUMPI v337(0x33f), v336

    Begin block 0x33b
    prev=[0x333], succ=[]
    =================================
    0x33b: v33b(0x0) = CONST 
    0x33e: REVERT v33b(0x0), v33b(0x0)

    Begin block 0x33f
    prev=[0x333], succ=[0x352, 0x356]
    =================================
    0x341: v341(0xa7b) = CONST 
    0x344: v344(0x4) = CONST 
    0x347: v347 = CALLDATASIZE 
    0x348: v348 = SUB v347, v344(0x4)
    0x349: v349(0x20) = CONST 
    0x34c: v34c = LT v348, v349(0x20)
    0x34d: v34d = ISZERO v34c
    0x34e: v34e(0x356) = CONST 
    0x351: JUMPI v34e(0x356), v34d

    Begin block 0x352
    prev=[0x33f], succ=[]
    =================================
    0x352: v352(0x0) = CONST 
    0x355: REVERT v352(0x0), v352(0x0)

    Begin block 0x356
    prev=[0x33f], succ=[0x5a0]
    =================================
    0x358: v358 = CALLDATALOAD v344(0x4)
    0x359: v359(0x1) = CONST 
    0x35b: v35b(0x1) = CONST 
    0x35d: v35d(0xa0) = CONST 
    0x35f: v35f(0x10000000000000000000000000000000000000000) = SHL v35d(0xa0), v35b(0x1)
    0x360: v360(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35f(0x10000000000000000000000000000000000000000), v359(0x1)
    0x361: v361 = AND v360(0xffffffffffffffffffffffffffffffffffffffff), v358
    0x362: v362(0x5a0) = CONST 
    0x365: JUMP v362(0x5a0)

    Begin block 0x5a0
    prev=[0x356], succ=[0x625B0x5a0]
    =================================
    0x5a1: v5a1(0x5a8) = CONST 
    0x5a4: v5a4(0x625) = CONST 
    0x5a7: JUMP v5a4(0x625)

    Begin block 0x625B0x5a0
    prev=[0x5a0], succ=[0x7a8B0x5a0]
    =================================
    0x626S0x5a0: v626V5a0(0x1) = CONST 
    0x628S0x5a0: v628V5a0 = SLOAD v626V5a0(0x1)
    0x629S0x5a0: v629V5a0(0x0) = CONST 
    0x62cS0x5a0: v62cV5a0(0x1) = CONST 
    0x62eS0x5a0: v62eV5a0(0x1) = CONST 
    0x630S0x5a0: v630V5a0(0xa0) = CONST 
    0x632S0x5a0: v632V5a0(0x10000000000000000000000000000000000000000) = SHL v630V5a0(0xa0), v62eV5a0(0x1)
    0x633S0x5a0: v633V5a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v632V5a0(0x10000000000000000000000000000000000000000), v62cV5a0(0x1)
    0x634S0x5a0: v634V5a0 = AND v633V5a0(0xffffffffffffffffffffffffffffffffffffffff), v628V5a0
    0x635S0x5a0: v635V5a0(0x63c) = CONST 
    0x638S0x5a0: v638V5a0(0x7a8) = CONST 
    0x63bS0x5a0: JUMP v638V5a0(0x7a8)

    Begin block 0x7a8B0x5a0
    prev=[0x625B0x5a0], succ=[0x63cB0x5a0]
    =================================
    0x7a9S0x5a0: v7a9V5a0 = CALLER 
    0x7abS0x5a0: JUMP v635V5a0(0x63c)

    Begin block 0x63cB0x5a0
    prev=[0x7a8B0x5a0], succ=[0x5a8]
    =================================
    0x63dS0x5a0: v63dV5a0(0x1) = CONST 
    0x63fS0x5a0: v63fV5a0(0x1) = CONST 
    0x641S0x5a0: v641V5a0(0xa0) = CONST 
    0x643S0x5a0: v643V5a0(0x10000000000000000000000000000000000000000) = SHL v641V5a0(0xa0), v63fV5a0(0x1)
    0x644S0x5a0: v644V5a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v643V5a0(0x10000000000000000000000000000000000000000), v63dV5a0(0x1)
    0x645S0x5a0: v645V5a0 = AND v644V5a0(0xffffffffffffffffffffffffffffffffffffffff), v7a9V5a0
    0x646S0x5a0: v646V5a0 = EQ v645V5a0, v634V5a0
    0x64aS0x5a0: JUMP v5a1(0x5a8)

    Begin block 0x5a8
    prev=[0x63cB0x5a0], succ=[0x5ad, 0x5e8]
    =================================
    0x5a9: v5a9(0x5e8) = CONST 
    0x5ac: JUMPI v5a9(0x5e8), v646V5a0

    Begin block 0x5ad
    prev=[0x5a8], succ=[]
    =================================
    0x5ad: v5ad(0x40) = CONST 
    0x5b0: v5b0 = MLOAD v5ad(0x40)
    0x5b1: v5b1(0x461bcd) = CONST 
    0x5b5: v5b5(0xe5) = CONST 
    0x5b7: v5b7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5b5(0xe5), v5b1(0x461bcd)
    0x5b9: MSTORE v5b0, v5b7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5ba: v5ba(0x20) = CONST 
    0x5bc: v5bc(0x4) = CONST 
    0x5bf: v5bf = ADD v5b0, v5bc(0x4)
    0x5c0: MSTORE v5bf, v5ba(0x20)
    0x5c1: v5c1(0xc) = CONST 
    0x5c3: v5c3(0x24) = CONST 
    0x5c6: v5c6 = ADD v5b0, v5c3(0x24)
    0x5c7: MSTORE v5c6, v5c1(0xc)
    0x5c8: v5c8(0x1d5b985d5d1a1bdc9a5e9959) = CONST 
    0x5d5: v5d5(0xa2) = CONST 
    0x5d7: v5d7(0x756e617574686f72697a65640000000000000000000000000000000000000000) = SHL v5d5(0xa2), v5c8(0x1d5b985d5d1a1bdc9a5e9959)
    0x5d8: v5d8(0x44) = CONST 
    0x5db: v5db = ADD v5b0, v5d8(0x44)
    0x5dc: MSTORE v5db, v5d7(0x756e617574686f72697a65640000000000000000000000000000000000000000)
    0x5de: v5de = MLOAD v5ad(0x40)
    0x5e2: v5e2(0x0) = SUB v5b0, v5de
    0x5e3: v5e3(0x64) = CONST 
    0x5e5: v5e5(0x64) = ADD v5e3(0x64), v5e2(0x0)
    0x5e7: REVERT v5de, v5e5(0x64)

    Begin block 0x5e8
    prev=[0x5a8], succ=[0x734]
    =================================
    0x5e9: v5e9(0xca7) = CONST 
    0x5ed: v5ed(0x734) = CONST 
    0x5f0: JUMP v5ed(0x734)

    Begin block 0x734
    prev=[0x5e8], succ=[0x84dB0x734]
    =================================
    0x735: v735(0x73d) = CONST 
    0x739: v739(0x84d) = CONST 
    0x73c: JUMP v739(0x84d)

    Begin block 0x84dB0x734
    prev=[0x734], succ=[0x881B0x734, 0x87dB0x734]
    =================================
    0x84eS0x734: v84eV734(0x0) = CONST 
    0x851S0x734: v851V734 = EXTCODEHASH v361
    0x852S0x734: v852V734(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x875S0x734: v875V734 = EQ v852V734(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470), v851V734
    0x877S0x734: v877V734 = ISZERO v875V734
    0x879S0x734: v879V734(0x881) = CONST 
    0x87cS0x734: JUMPI v879V734(0x881), v875V734

    Begin block 0x881B0x734
    prev=[0x84dB0x734, 0x87dB0x734], succ=[0x73d]
    =================================
    0x881_0x0S0x734: v881_0V734 = PHI v877V734, v880V734
    0x888S0x734: JUMP v735(0x73d)

    Begin block 0x73d
    prev=[0x881B0x734], succ=[0x742, 0x786]
    =================================
    0x73e: v73e(0x786) = CONST 
    0x741: JUMPI v73e(0x786), v881_0V734

    Begin block 0x742
    prev=[0x73d], succ=[]
    =================================
    0x742: v742(0x40) = CONST 
    0x745: v745 = MLOAD v742(0x40)
    0x746: v746(0x461bcd) = CONST 
    0x74a: v74a(0xe5) = CONST 
    0x74c: v74c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v74a(0xe5), v746(0x461bcd)
    0x74e: MSTORE v745, v74c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x74f: v74f(0x20) = CONST 
    0x751: v751(0x4) = CONST 
    0x754: v754 = ADD v745, v751(0x4)
    0x755: MSTORE v754, v74f(0x20)
    0x756: v756(0x15) = CONST 
    0x758: v758(0x24) = CONST 
    0x75b: v75b = ADD v745, v758(0x24)
    0x75c: MSTORE v75b, v756(0x15)
    0x75d: v75d(0x1d185c99d95d081b9bdd08184818dbdb9d1c9858dd) = CONST 
    0x773: v773(0x5a) = CONST 
    0x775: v775(0x746172676574206e6f74206120636f6e74726163740000000000000000000000) = SHL v773(0x5a), v75d(0x1d185c99d95d081b9bdd08184818dbdb9d1c9858dd)
    0x776: v776(0x44) = CONST 
    0x779: v779 = ADD v745, v776(0x44)
    0x77a: MSTORE v779, v775(0x746172676574206e6f74206120636f6e74726163740000000000000000000000)
    0x77c: v77c = MLOAD v742(0x40)
    0x780: v780(0x0) = SUB v745, v77c
    0x781: v781(0x64) = CONST 
    0x783: v783(0x64) = ADD v781(0x64), v780(0x0)
    0x785: REVERT v77c, v783(0x64)

    Begin block 0x786
    prev=[0x73d], succ=[0xca7]
    =================================
    0x787: v787(0x14) = CONST 
    0x78a: v78a = SLOAD v787(0x14)
    0x78b: v78b(0x1) = CONST 
    0x78d: v78d(0x1) = CONST 
    0x78f: v78f(0xa0) = CONST 
    0x791: v791(0x10000000000000000000000000000000000000000) = SHL v78f(0xa0), v78d(0x1)
    0x792: v792(0xffffffffffffffffffffffffffffffffffffffff) = SUB v791(0x10000000000000000000000000000000000000000), v78b(0x1)
    0x793: v793(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v792(0xffffffffffffffffffffffffffffffffffffffff)
    0x794: v794 = AND v793(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v78a
    0x795: v795(0x1) = CONST 
    0x797: v797(0x1) = CONST 
    0x799: v799(0xa0) = CONST 
    0x79b: v79b(0x10000000000000000000000000000000000000000) = SHL v799(0xa0), v797(0x1)
    0x79c: v79c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v79b(0x10000000000000000000000000000000000000000), v795(0x1)
    0x7a0: v7a0 = AND v79c(0xffffffffffffffffffffffffffffffffffffffff), v361
    0x7a4: v7a4 = OR v7a0, v794
    0x7a6: SSTORE v787(0x14), v7a4
    0x7a7: JUMP v5e9(0xca7)

    Begin block 0xca7
    prev=[0x786], succ=[0xa7b]
    =================================
    0xca9: JUMP v341(0xa7b)

    Begin block 0xa7b
    prev=[0xca7], succ=[]
    =================================
    0xa7c: STOP 

    Begin block 0x87dB0x734
    prev=[0x84dB0x734], succ=[0x881B0x734]
    =================================
    0x87fS0x734: v87fV734 = ISZERO v851V734
    0x880S0x734: v880V734 = ISZERO v87fV734

}

function loanTokenAddress()() public {
    Begin block 0x366
    prev=[], succ=[0x36e, 0x372]
    =================================
    0x367: v367 = CALLVALUE 
    0x369: v369 = ISZERO v367
    0x36a: v36a(0x372) = CONST 
    0x36d: JUMPI v36a(0x372), v369

    Begin block 0x36e
    prev=[0x366], succ=[]
    =================================
    0x36e: v36e(0x0) = CONST 
    0x371: REVERT v36e(0x0), v36e(0x0)

    Begin block 0x372
    prev=[0x366], succ=[0x5f4]
    =================================
    0x374: v374(0xa9c) = CONST 
    0x377: v377(0x5f4) = CONST 
    0x37a: JUMP v377(0x5f4)

    Begin block 0x5f4
    prev=[0x372], succ=[0xa9c]
    =================================
    0x5f5: v5f5(0x4) = CONST 
    0x5f7: v5f7 = SLOAD v5f5(0x4)
    0x5f8: v5f8(0x1) = CONST 
    0x5fa: v5fa(0x60) = CONST 
    0x5fc: v5fc(0x1000000000000000000000000) = SHL v5fa(0x60), v5f8(0x1)
    0x5fe: v5fe = DIV v5f7, v5fc(0x1000000000000000000000000)
    0x5ff: v5ff(0x1) = CONST 
    0x601: v601(0x1) = CONST 
    0x603: v603(0xa0) = CONST 
    0x605: v605(0x10000000000000000000000000000000000000000) = SHL v603(0xa0), v601(0x1)
    0x606: v606(0xffffffffffffffffffffffffffffffffffffffff) = SUB v605(0x10000000000000000000000000000000000000000), v5ff(0x1)
    0x607: v607 = AND v606(0xffffffffffffffffffffffffffffffffffffffff), v5fe
    0x609: JUMP v374(0xa9c)

    Begin block 0xa9c
    prev=[0x5f4], succ=[]
    =================================
    0xa9d: va9d(0x40) = CONST 
    0xaa0: vaa0 = MLOAD va9d(0x40)
    0xaa1: vaa1(0x1) = CONST 
    0xaa3: vaa3(0x1) = CONST 
    0xaa5: vaa5(0xa0) = CONST 
    0xaa7: vaa7(0x10000000000000000000000000000000000000000) = SHL vaa5(0xa0), vaa3(0x1)
    0xaa8: vaa8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaa7(0x10000000000000000000000000000000000000000), vaa1(0x1)
    0xaab: vaab = AND v607, vaa8(0xffffffffffffffffffffffffffffffffffffffff)
    0xaad: MSTORE vaa0, vaab
    0xaae: vaae = MLOAD va9d(0x40)
    0xab2: vab2(0x0) = SUB vaa0, vaae
    0xab3: vab3(0x20) = CONST 
    0xab5: vab5(0x20) = ADD vab3(0x20), vab2(0x0)
    0xab7: RETURN vaae, vab5(0x20)

}

function checkpointSupply()() public {
    Begin block 0x397
    prev=[], succ=[0x39f, 0x3a3]
    =================================
    0x398: v398 = CALLVALUE 
    0x39a: v39a = ISZERO v398
    0x39b: v39b(0x3a3) = CONST 
    0x39e: JUMPI v39b(0x3a3), v39a

    Begin block 0x39f
    prev=[0x397], succ=[]
    =================================
    0x39f: v39f(0x0) = CONST 
    0x3a2: REVERT v39f(0x0), v39f(0x0)

    Begin block 0x3a3
    prev=[0x397], succ=[0x60a]
    =================================
    0x3a5: v3a5(0xad7) = CONST 
    0x3a8: v3a8(0x60a) = CONST 
    0x3ab: JUMP v3a8(0x60a)

    Begin block 0x60a
    prev=[0x3a3], succ=[0xad7]
    =================================
    0x60b: v60b(0xd) = CONST 
    0x60d: v60d = SLOAD v60b(0xd)
    0x60f: JUMP v3a5(0xad7)

    Begin block 0xad7
    prev=[0x60a], succ=[]
    =================================
    0xad8: vad8(0x40) = CONST 
    0xadb: vadb = MLOAD vad8(0x40)
    0xade: MSTORE vadb, v60d
    0xadf: vadf = MLOAD vad8(0x40)
    0xae3: vae3(0x0) = SUB vadb, vadf
    0xae4: vae4(0x20) = CONST 
    0xae6: vae6(0x20) = ADD vae4(0x20), vae3(0x0)
    0xae8: RETURN vadf, vae6(0x20)

}

function lowUtilRateMultiplier()() public {
    Begin block 0x3ac
    prev=[], succ=[0x3b4, 0x3b8]
    =================================
    0x3ad: v3ad = CALLVALUE 
    0x3af: v3af = ISZERO v3ad
    0x3b0: v3b0(0x3b8) = CONST 
    0x3b3: JUMPI v3b0(0x3b8), v3af

    Begin block 0x3b4
    prev=[0x3ac], succ=[]
    =================================
    0x3b4: v3b4(0x0) = CONST 
    0x3b7: REVERT v3b4(0x0), v3b4(0x0)

    Begin block 0x3b8
    prev=[0x3ac], succ=[0x610]
    =================================
    0x3ba: v3ba(0xb08) = CONST 
    0x3bd: v3bd(0x610) = CONST 
    0x3c0: JUMP v3bd(0x610)

    Begin block 0x610
    prev=[0x3b8], succ=[0xb08]
    =================================
    0x611: v611(0x8) = CONST 
    0x613: v613 = SLOAD v611(0x8)
    0x615: JUMP v3ba(0xb08)

    Begin block 0xb08
    prev=[0x610], succ=[]
    =================================
    0xb09: vb09(0x40) = CONST 
    0xb0c: vb0c = MLOAD vb09(0x40)
    0xb0f: MSTORE vb0c, v613
    0xb10: vb10 = MLOAD vb09(0x40)
    0xb14: vb14(0x0) = SUB vb0c, vb10
    0xb15: vb15(0x20) = CONST 
    0xb17: vb17(0x20) = ADD vb15(0x20), vb14(0x0)
    0xb19: RETURN vb10, vb17(0x20)

}

function owner()() public {
    Begin block 0x3c1
    prev=[], succ=[0x3c9, 0x3cd]
    =================================
    0x3c2: v3c2 = CALLVALUE 
    0x3c4: v3c4 = ISZERO v3c2
    0x3c5: v3c5(0x3cd) = CONST 
    0x3c8: JUMPI v3c5(0x3cd), v3c4

    Begin block 0x3c9
    prev=[0x3c1], succ=[]
    =================================
    0x3c9: v3c9(0x0) = CONST 
    0x3cc: REVERT v3c9(0x0), v3c9(0x0)

    Begin block 0x3cd
    prev=[0x3c1], succ=[0x616]
    =================================
    0x3cf: v3cf(0xb39) = CONST 
    0x3d2: v3d2(0x616) = CONST 
    0x3d5: JUMP v3d2(0x616)

    Begin block 0x616
    prev=[0x3cd], succ=[0xb39]
    =================================
    0x617: v617(0x1) = CONST 
    0x619: v619 = SLOAD v617(0x1)
    0x61a: v61a(0x1) = CONST 
    0x61c: v61c(0x1) = CONST 
    0x61e: v61e(0xa0) = CONST 
    0x620: v620(0x10000000000000000000000000000000000000000) = SHL v61e(0xa0), v61c(0x1)
    0x621: v621(0xffffffffffffffffffffffffffffffffffffffff) = SUB v620(0x10000000000000000000000000000000000000000), v61a(0x1)
    0x622: v622 = AND v621(0xffffffffffffffffffffffffffffffffffffffff), v619
    0x624: JUMP v3cf(0xb39)

    Begin block 0xb39
    prev=[0x616], succ=[]
    =================================
    0xb3a: vb3a(0x40) = CONST 
    0xb3d: vb3d = MLOAD vb3a(0x40)
    0xb3e: vb3e(0x1) = CONST 
    0xb40: vb40(0x1) = CONST 
    0xb42: vb42(0xa0) = CONST 
    0xb44: vb44(0x10000000000000000000000000000000000000000) = SHL vb42(0xa0), vb40(0x1)
    0xb45: vb45(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb44(0x10000000000000000000000000000000000000000), vb3e(0x1)
    0xb48: vb48 = AND v622, vb45(0xffffffffffffffffffffffffffffffffffffffff)
    0xb4a: MSTORE vb3d, vb48
    0xb4b: vb4b = MLOAD vb3a(0x40)
    0xb4f: vb4f(0x0) = SUB vb3d, vb4b
    0xb50: vb50(0x20) = CONST 
    0xb52: vb52(0x20) = ADD vb50(0x20), vb4f(0x0)
    0xb54: RETURN vb4b, vb52(0x20)

}

function isOwner()() public {
    Begin block 0x3d6
    prev=[], succ=[0x3de, 0x3e2]
    =================================
    0x3d7: v3d7 = CALLVALUE 
    0x3d9: v3d9 = ISZERO v3d7
    0x3da: v3da(0x3e2) = CONST 
    0x3dd: JUMPI v3da(0x3e2), v3d9

    Begin block 0x3de
    prev=[0x3d6], succ=[]
    =================================
    0x3de: v3de(0x0) = CONST 
    0x3e1: REVERT v3de(0x0), v3de(0x0)

    Begin block 0x3e2
    prev=[0x3d6], succ=[0x625B0x3e2]
    =================================
    0x3e4: v3e4(0x3eb) = CONST 
    0x3e7: v3e7(0x625) = CONST 
    0x3ea: JUMP v3e7(0x625)

    Begin block 0x625B0x3e2
    prev=[0x3e2], succ=[0x7a8B0x3e2]
    =================================
    0x626S0x3e2: v626V3e2(0x1) = CONST 
    0x628S0x3e2: v628V3e2 = SLOAD v626V3e2(0x1)
    0x629S0x3e2: v629V3e2(0x0) = CONST 
    0x62cS0x3e2: v62cV3e2(0x1) = CONST 
    0x62eS0x3e2: v62eV3e2(0x1) = CONST 
    0x630S0x3e2: v630V3e2(0xa0) = CONST 
    0x632S0x3e2: v632V3e2(0x10000000000000000000000000000000000000000) = SHL v630V3e2(0xa0), v62eV3e2(0x1)
    0x633S0x3e2: v633V3e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v632V3e2(0x10000000000000000000000000000000000000000), v62cV3e2(0x1)
    0x634S0x3e2: v634V3e2 = AND v633V3e2(0xffffffffffffffffffffffffffffffffffffffff), v628V3e2
    0x635S0x3e2: v635V3e2(0x63c) = CONST 
    0x638S0x3e2: v638V3e2(0x7a8) = CONST 
    0x63bS0x3e2: JUMP v638V3e2(0x7a8)

    Begin block 0x7a8B0x3e2
    prev=[0x625B0x3e2], succ=[0x63cB0x3e2]
    =================================
    0x7a9S0x3e2: v7a9V3e2 = CALLER 
    0x7abS0x3e2: JUMP v635V3e2(0x63c)

    Begin block 0x63cB0x3e2
    prev=[0x7a8B0x3e2], succ=[0x3eb]
    =================================
    0x63dS0x3e2: v63dV3e2(0x1) = CONST 
    0x63fS0x3e2: v63fV3e2(0x1) = CONST 
    0x641S0x3e2: v641V3e2(0xa0) = CONST 
    0x643S0x3e2: v643V3e2(0x10000000000000000000000000000000000000000) = SHL v641V3e2(0xa0), v63fV3e2(0x1)
    0x644S0x3e2: v644V3e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v643V3e2(0x10000000000000000000000000000000000000000), v63dV3e2(0x1)
    0x645S0x3e2: v645V3e2 = AND v644V3e2(0xffffffffffffffffffffffffffffffffffffffff), v7a9V3e2
    0x646S0x3e2: v646V3e2 = EQ v645V3e2, v634V3e2
    0x64aS0x3e2: JUMP v3e4(0x3eb)

    Begin block 0x3eb
    prev=[0x63cB0x3e2], succ=[]
    =================================
    0x3ec: v3ec(0x40) = CONST 
    0x3ef: v3ef = MLOAD v3ec(0x40)
    0x3f1: v3f1 = ISZERO v646V3e2
    0x3f2: v3f2 = ISZERO v3f1
    0x3f4: MSTORE v3ef, v3f2
    0x3f5: v3f5 = MLOAD v3ec(0x40)
    0x3f9: v3f9(0x0) = SUB v3ef, v3f5
    0x3fa: v3fa(0x20) = CONST 
    0x3fc: v3fc(0x20) = ADD v3fa(0x20), v3f9(0x0)
    0x3fe: RETURN v3f5, v3fc(0x20)

}

function symbol()() public {
    Begin block 0x3ff
    prev=[], succ=[0x407, 0x40b]
    =================================
    0x400: v400 = CALLVALUE 
    0x402: v402 = ISZERO v400
    0x403: v403(0x40b) = CONST 
    0x406: JUMPI v403(0x40b), v402

    Begin block 0x407
    prev=[0x3ff], succ=[]
    =================================
    0x407: v407(0x0) = CONST 
    0x40a: REVERT v407(0x0), v407(0x0)

    Begin block 0x40b
    prev=[0x3ff], succ=[0x1bb0x3ff]
    =================================
    0x40d: v40d(0x1bb) = CONST 
    0x410: v410(0x64b) = CONST 
    0x413: v413_0, v413_1 = CALLPRIVATE v410(0x64b), v40d(0x1bb)

    Begin block 0x1bb0x3ff
    prev=[0x40b], succ=[0x1dd0x3ff]
    =================================
    0x1bc0x3ff: v3ff1bc(0x40) = CONST 
    0x1bf0x3ff: v3ff1bf = MLOAD v3ff1bc(0x40)
    0x1c00x3ff: v3ff1c0(0x20) = CONST 
    0x1c40x3ff: MSTORE v3ff1bf, v3ff1c0(0x20)
    0x1c60x3ff: v3ff1c6 = MLOAD v413_0
    0x1c90x3ff: v3ff1c9 = ADD v3ff1bf, v3ff1c0(0x20)
    0x1ca0x3ff: MSTORE v3ff1c9, v3ff1c6
    0x1cc0x3ff: v3ff1cc = MLOAD v413_0
    0x1d30x3ff: v3ff1d3 = ADD v3ff1bf, v3ff1bc(0x40)
    0x1d60x3ff: v3ff1d6 = ADD v413_0, v3ff1c0(0x20)
    0x1db0x3ff: v3ff1db(0x0) = CONST 

    Begin block 0x1dd0x3ff
    prev=[0x1e60x3ff, 0x1bb0x3ff], succ=[0x1f50x3ff, 0x1e60x3ff]
    =================================
    0x1dd0x3ff_0x0: v1dd3ff_0 = PHI v3ff1f0, v3ff1db(0x0)
    0x1e00x3ff: v3ff1e0 = LT v1dd3ff_0, v3ff1cc
    0x1e10x3ff: v3ff1e1 = ISZERO v3ff1e0
    0x1e20x3ff: v3ff1e2(0x1f5) = CONST 
    0x1e50x3ff: JUMPI v3ff1e2(0x1f5), v3ff1e1

    Begin block 0x1f50x3ff
    prev=[0x1dd0x3ff], succ=[0x2220x3ff, 0x2090x3ff]
    =================================
    0x1fe0x3ff: v3ff1fe = ADD v3ff1cc, v3ff1d3
    0x2000x3ff: v3ff200(0x1f) = CONST 
    0x2020x3ff: v3ff202 = AND v3ff200(0x1f), v3ff1cc
    0x2040x3ff: v3ff204 = ISZERO v3ff202
    0x2050x3ff: v3ff205(0x222) = CONST 
    0x2080x3ff: JUMPI v3ff205(0x222), v3ff204

    Begin block 0x2220x3ff
    prev=[0x1f50x3ff, 0x2090x3ff], succ=[]
    =================================
    0x2220x3ff_0x1: v2223ff_1 = PHI v3ff21f, v3ff1fe
    0x2280x3ff: v3ff228(0x40) = CONST 
    0x22a0x3ff: v3ff22a = MLOAD v3ff228(0x40)
    0x22d0x3ff: v3ff22d = SUB v2223ff_1, v3ff22a
    0x22f0x3ff: RETURN v3ff22a, v3ff22d

    Begin block 0x2090x3ff
    prev=[0x1f50x3ff], succ=[0x2220x3ff]
    =================================
    0x20b0x3ff: v3ff20b = SUB v3ff1fe, v3ff202
    0x20d0x3ff: v3ff20d = MLOAD v3ff20b
    0x20e0x3ff: v3ff20e(0x1) = CONST 
    0x2110x3ff: v3ff211(0x20) = CONST 
    0x2130x3ff: v3ff213 = SUB v3ff211(0x20), v3ff202
    0x2140x3ff: v3ff214(0x100) = CONST 
    0x2170x3ff: v3ff217 = EXP v3ff214(0x100), v3ff213
    0x2180x3ff: v3ff218 = SUB v3ff217, v3ff20e(0x1)
    0x2190x3ff: v3ff219 = NOT v3ff218
    0x21a0x3ff: v3ff21a = AND v3ff219, v3ff20d
    0x21c0x3ff: MSTORE v3ff20b, v3ff21a
    0x21d0x3ff: v3ff21d(0x20) = CONST 
    0x21f0x3ff: v3ff21f = ADD v3ff21d(0x20), v3ff20b

    Begin block 0x1e60x3ff
    prev=[0x1dd0x3ff], succ=[0x1dd0x3ff]
    =================================
    0x1e60x3ff_0x0: v1e63ff_0 = PHI v3ff1f0, v3ff1db(0x0)
    0x1e80x3ff: v3ff1e8 = ADD v1e63ff_0, v3ff1d6
    0x1e90x3ff: v3ff1e9 = MLOAD v3ff1e8
    0x1ec0x3ff: v3ff1ec = ADD v1e63ff_0, v3ff1d3
    0x1ed0x3ff: MSTORE v3ff1ec, v3ff1e9
    0x1ee0x3ff: v3ff1ee(0x20) = CONST 
    0x1f00x3ff: v3ff1f0 = ADD v3ff1ee(0x20), v1e63ff_0
    0x1f10x3ff: v3ff1f1(0x1dd) = CONST 
    0x1f40x3ff: JUMP v3ff1f1(0x1dd)

}

function targetLevel()() public {
    Begin block 0x414
    prev=[], succ=[0x41c, 0x420]
    =================================
    0x415: v415 = CALLVALUE 
    0x417: v417 = ISZERO v415
    0x418: v418(0x420) = CONST 
    0x41b: JUMPI v418(0x420), v417

    Begin block 0x41c
    prev=[0x414], succ=[]
    =================================
    0x41c: v41c(0x0) = CONST 
    0x41f: REVERT v41c(0x0), v41c(0x0)

    Begin block 0x420
    prev=[0x414], succ=[0x6a6]
    =================================
    0x422: v422(0xb74) = CONST 
    0x425: v425(0x6a6) = CONST 
    0x428: JUMP v425(0x6a6)

    Begin block 0x6a6
    prev=[0x420], succ=[0xb74]
    =================================
    0x6a7: v6a7(0x9) = CONST 
    0x6a9: v6a9 = SLOAD v6a7(0x9)
    0x6ab: JUMP v422(0xb74)

    Begin block 0xb74
    prev=[0x6a6], succ=[]
    =================================
    0xb75: vb75(0x40) = CONST 
    0xb78: vb78 = MLOAD vb75(0x40)
    0xb7b: MSTORE vb78, v6a9
    0xb7c: vb7c = MLOAD vb75(0x40)
    0xb80: vb80(0x0) = SUB vb78, vb7c
    0xb81: vb81(0x20) = CONST 
    0xb83: vb83(0x20) = ADD vb81(0x20), vb80(0x0)
    0xb85: RETURN vb7c, vb83(0x20)

}

function lowUtilBaseRate()() public {
    Begin block 0x429
    prev=[], succ=[0x431, 0x435]
    =================================
    0x42a: v42a = CALLVALUE 
    0x42c: v42c = ISZERO v42a
    0x42d: v42d(0x435) = CONST 
    0x430: JUMPI v42d(0x435), v42c

    Begin block 0x431
    prev=[0x429], succ=[]
    =================================
    0x431: v431(0x0) = CONST 
    0x434: REVERT v431(0x0), v431(0x0)

    Begin block 0x435
    prev=[0x429], succ=[0x6ac]
    =================================
    0x437: v437(0xba5) = CONST 
    0x43a: v43a(0x6ac) = CONST 
    0x43d: JUMP v43a(0x6ac)

    Begin block 0x6ac
    prev=[0x435], succ=[0xba5]
    =================================
    0x6ad: v6ad(0x7) = CONST 
    0x6af: v6af = SLOAD v6ad(0x7)
    0x6b1: JUMP v437(0xba5)

    Begin block 0xba5
    prev=[0x6ac], succ=[]
    =================================
    0xba6: vba6(0x40) = CONST 
    0xba9: vba9 = MLOAD vba6(0x40)
    0xbac: MSTORE vba9, v6af
    0xbad: vbad = MLOAD vba6(0x40)
    0xbb1: vbb1(0x0) = SUB vba9, vbad
    0xbb2: vbb2(0x20) = CONST 
    0xbb4: vbb4(0x20) = ADD vbb2(0x20), vbb1(0x0)
    0xbb6: RETURN vbad, vbb4(0x20)

}

function allowance(address,address)() public {
    Begin block 0x43e
    prev=[], succ=[0x446, 0x44a]
    =================================
    0x43f: v43f = CALLVALUE 
    0x441: v441 = ISZERO v43f
    0x442: v442(0x44a) = CONST 
    0x445: JUMPI v442(0x44a), v441

    Begin block 0x446
    prev=[0x43e], succ=[]
    =================================
    0x446: v446(0x0) = CONST 
    0x449: REVERT v446(0x0), v446(0x0)

    Begin block 0x44a
    prev=[0x43e], succ=[0x45d, 0x461]
    =================================
    0x44c: v44c(0xbd6) = CONST 
    0x44f: v44f(0x4) = CONST 
    0x452: v452 = CALLDATASIZE 
    0x453: v453 = SUB v452, v44f(0x4)
    0x454: v454(0x40) = CONST 
    0x457: v457 = LT v453, v454(0x40)
    0x458: v458 = ISZERO v457
    0x459: v459(0x461) = CONST 
    0x45c: JUMPI v459(0x461), v458

    Begin block 0x45d
    prev=[0x44a], succ=[]
    =================================
    0x45d: v45d(0x0) = CONST 
    0x460: REVERT v45d(0x0), v45d(0x0)

    Begin block 0x461
    prev=[0x44a], succ=[0x6b2]
    =================================
    0x463: v463(0x1) = CONST 
    0x465: v465(0x1) = CONST 
    0x467: v467(0xa0) = CONST 
    0x469: v469(0x10000000000000000000000000000000000000000) = SHL v467(0xa0), v465(0x1)
    0x46a: v46a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v469(0x10000000000000000000000000000000000000000), v463(0x1)
    0x46c: v46c = CALLDATALOAD v44f(0x4)
    0x46e: v46e = AND v46a(0xffffffffffffffffffffffffffffffffffffffff), v46c
    0x470: v470(0x20) = CONST 
    0x472: v472(0x24) = ADD v470(0x20), v44f(0x4)
    0x473: v473 = CALLDATALOAD v472(0x24)
    0x474: v474 = AND v473, v46a(0xffffffffffffffffffffffffffffffffffffffff)
    0x475: v475(0x6b2) = CONST 
    0x478: JUMP v475(0x6b2)

    Begin block 0x6b2
    prev=[0x461], succ=[0xbd6]
    =================================
    0x6b3: v6b3(0x1) = CONST 
    0x6b5: v6b5(0x1) = CONST 
    0x6b7: v6b7(0xa0) = CONST 
    0x6b9: v6b9(0x10000000000000000000000000000000000000000) = SHL v6b7(0xa0), v6b5(0x1)
    0x6ba: v6ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b9(0x10000000000000000000000000000000000000000), v6b3(0x1)
    0x6bd: v6bd = AND v6ba(0xffffffffffffffffffffffffffffffffffffffff), v46e
    0x6be: v6be(0x0) = CONST 
    0x6c2: MSTORE v6be(0x0), v6bd
    0x6c3: v6c3(0x12) = CONST 
    0x6c5: v6c5(0x20) = CONST 
    0x6c9: MSTORE v6c5(0x20), v6c3(0x12)
    0x6ca: v6ca(0x40) = CONST 
    0x6ce: v6ce = SHA3 v6be(0x0), v6ca(0x40)
    0x6d2: v6d2 = AND v6ba(0xffffffffffffffffffffffffffffffffffffffff), v474
    0x6d4: MSTORE v6be(0x0), v6d2
    0x6d8: MSTORE v6c5(0x20), v6ce
    0x6d9: v6d9 = SHA3 v6be(0x0), v6ca(0x40)
    0x6da: v6da = SLOAD v6d9
    0x6dc: JUMP v44c(0xbd6)

    Begin block 0xbd6
    prev=[0x6b2], succ=[]
    =================================
    0xbd7: vbd7(0x40) = CONST 
    0xbda: vbda = MLOAD vbd7(0x40)
    0xbdd: MSTORE vbda, v6da
    0xbde: vbde = MLOAD vbd7(0x40)
    0xbe2: vbe2(0x0) = SUB vbda, vbde
    0xbe3: vbe3(0x20) = CONST 
    0xbe5: vbe5(0x20) = ADD vbe3(0x20), vbe2(0x0)
    0xbe7: RETURN vbde, vbe5(0x20)

}

function maxScaleRate()() public {
    Begin block 0x479
    prev=[], succ=[0x481, 0x485]
    =================================
    0x47a: v47a = CALLVALUE 
    0x47c: v47c = ISZERO v47a
    0x47d: v47d(0x485) = CONST 
    0x480: JUMPI v47d(0x485), v47c

    Begin block 0x481
    prev=[0x479], succ=[]
    =================================
    0x481: v481(0x0) = CONST 
    0x484: REVERT v481(0x0), v481(0x0)

    Begin block 0x485
    prev=[0x479], succ=[0x6dd]
    =================================
    0x487: v487(0xc07) = CONST 
    0x48a: v48a(0x6dd) = CONST 
    0x48d: JUMP v48a(0x6dd)

    Begin block 0x6dd
    prev=[0x485], succ=[0xc07]
    =================================
    0x6de: v6de(0xb) = CONST 
    0x6e0: v6e0 = SLOAD v6de(0xb)
    0x6e2: JUMP v487(0xc07)

    Begin block 0xc07
    prev=[0x6dd], succ=[]
    =================================
    0xc08: vc08(0x40) = CONST 
    0xc0b: vc0b = MLOAD vc08(0x40)
    0xc0e: MSTORE vc0b, v6e0
    0xc0f: vc0f = MLOAD vc08(0x40)
    0xc13: vc13(0x0) = SUB vc0b, vc0f
    0xc14: vc14(0x20) = CONST 
    0xc16: vc16(0x20) = ADD vc14(0x20), vc13(0x0)
    0xc18: RETURN vc0f, vc16(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x48e
    prev=[], succ=[0x496, 0x49a]
    =================================
    0x48f: v48f = CALLVALUE 
    0x491: v491 = ISZERO v48f
    0x492: v492(0x49a) = CONST 
    0x495: JUMPI v492(0x49a), v491

    Begin block 0x496
    prev=[0x48e], succ=[]
    =================================
    0x496: v496(0x0) = CONST 
    0x499: REVERT v496(0x0), v496(0x0)

    Begin block 0x49a
    prev=[0x48e], succ=[0x4ad, 0x4b1]
    =================================
    0x49c: v49c(0xc38) = CONST 
    0x49f: v49f(0x4) = CONST 
    0x4a2: v4a2 = CALLDATASIZE 
    0x4a3: v4a3 = SUB v4a2, v49f(0x4)
    0x4a4: v4a4(0x20) = CONST 
    0x4a7: v4a7 = LT v4a3, v4a4(0x20)
    0x4a8: v4a8 = ISZERO v4a7
    0x4a9: v4a9(0x4b1) = CONST 
    0x4ac: JUMPI v4a9(0x4b1), v4a8

    Begin block 0x4ad
    prev=[0x49a], succ=[]
    =================================
    0x4ad: v4ad(0x0) = CONST 
    0x4b0: REVERT v4ad(0x0), v4ad(0x0)

    Begin block 0x4b1
    prev=[0x49a], succ=[0x6e3]
    =================================
    0x4b3: v4b3 = CALLDATALOAD v49f(0x4)
    0x4b4: v4b4(0x1) = CONST 
    0x4b6: v4b6(0x1) = CONST 
    0x4b8: v4b8(0xa0) = CONST 
    0x4ba: v4ba(0x10000000000000000000000000000000000000000) = SHL v4b8(0xa0), v4b6(0x1)
    0x4bb: v4bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ba(0x10000000000000000000000000000000000000000), v4b4(0x1)
    0x4bc: v4bc = AND v4bb(0xffffffffffffffffffffffffffffffffffffffff), v4b3
    0x4bd: v4bd(0x6e3) = CONST 
    0x4c0: JUMP v4bd(0x6e3)

    Begin block 0x6e3
    prev=[0x4b1], succ=[0x625B0x6e3]
    =================================
    0x6e4: v6e4(0x6eb) = CONST 
    0x6e7: v6e7(0x625) = CONST 
    0x6ea: JUMP v6e7(0x625)

    Begin block 0x625B0x6e3
    prev=[0x6e3], succ=[0x7a8B0x6e3]
    =================================
    0x626S0x6e3: v626V6e3(0x1) = CONST 
    0x628S0x6e3: v628V6e3 = SLOAD v626V6e3(0x1)
    0x629S0x6e3: v629V6e3(0x0) = CONST 
    0x62cS0x6e3: v62cV6e3(0x1) = CONST 
    0x62eS0x6e3: v62eV6e3(0x1) = CONST 
    0x630S0x6e3: v630V6e3(0xa0) = CONST 
    0x632S0x6e3: v632V6e3(0x10000000000000000000000000000000000000000) = SHL v630V6e3(0xa0), v62eV6e3(0x1)
    0x633S0x6e3: v633V6e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v632V6e3(0x10000000000000000000000000000000000000000), v62cV6e3(0x1)
    0x634S0x6e3: v634V6e3 = AND v633V6e3(0xffffffffffffffffffffffffffffffffffffffff), v628V6e3
    0x635S0x6e3: v635V6e3(0x63c) = CONST 
    0x638S0x6e3: v638V6e3(0x7a8) = CONST 
    0x63bS0x6e3: JUMP v638V6e3(0x7a8)

    Begin block 0x7a8B0x6e3
    prev=[0x625B0x6e3], succ=[0x63cB0x6e3]
    =================================
    0x7a9S0x6e3: v7a9V6e3 = CALLER 
    0x7abS0x6e3: JUMP v635V6e3(0x63c)

    Begin block 0x63cB0x6e3
    prev=[0x7a8B0x6e3], succ=[0x6eb]
    =================================
    0x63dS0x6e3: v63dV6e3(0x1) = CONST 
    0x63fS0x6e3: v63fV6e3(0x1) = CONST 
    0x641S0x6e3: v641V6e3(0xa0) = CONST 
    0x643S0x6e3: v643V6e3(0x10000000000000000000000000000000000000000) = SHL v641V6e3(0xa0), v63fV6e3(0x1)
    0x644S0x6e3: v644V6e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v643V6e3(0x10000000000000000000000000000000000000000), v63dV6e3(0x1)
    0x645S0x6e3: v645V6e3 = AND v644V6e3(0xffffffffffffffffffffffffffffffffffffffff), v7a9V6e3
    0x646S0x6e3: v646V6e3 = EQ v645V6e3, v634V6e3
    0x64aS0x6e3: JUMP v6e4(0x6eb)

    Begin block 0x6eb
    prev=[0x63cB0x6e3], succ=[0x6f0, 0x72b]
    =================================
    0x6ec: v6ec(0x72b) = CONST 
    0x6ef: JUMPI v6ec(0x72b), v646V6e3

    Begin block 0x6f0
    prev=[0x6eb], succ=[]
    =================================
    0x6f0: v6f0(0x40) = CONST 
    0x6f3: v6f3 = MLOAD v6f0(0x40)
    0x6f4: v6f4(0x461bcd) = CONST 
    0x6f8: v6f8(0xe5) = CONST 
    0x6fa: v6fa(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v6f8(0xe5), v6f4(0x461bcd)
    0x6fc: MSTORE v6f3, v6fa(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x6fd: v6fd(0x20) = CONST 
    0x6ff: v6ff(0x4) = CONST 
    0x702: v702 = ADD v6f3, v6ff(0x4)
    0x703: MSTORE v702, v6fd(0x20)
    0x704: v704(0xc) = CONST 
    0x706: v706(0x24) = CONST 
    0x709: v709 = ADD v6f3, v706(0x24)
    0x70a: MSTORE v709, v704(0xc)
    0x70b: v70b(0x1d5b985d5d1a1bdc9a5e9959) = CONST 
    0x718: v718(0xa2) = CONST 
    0x71a: v71a(0x756e617574686f72697a65640000000000000000000000000000000000000000) = SHL v718(0xa2), v70b(0x1d5b985d5d1a1bdc9a5e9959)
    0x71b: v71b(0x44) = CONST 
    0x71e: v71e = ADD v6f3, v71b(0x44)
    0x71f: MSTORE v71e, v71a(0x756e617574686f72697a65640000000000000000000000000000000000000000)
    0x721: v721 = MLOAD v6f0(0x40)
    0x725: v725(0x0) = SUB v6f3, v721
    0x726: v726(0x64) = CONST 
    0x728: v728(0x64) = ADD v726(0x64), v725(0x0)
    0x72a: REVERT v721, v728(0x64)

    Begin block 0x72b
    prev=[0x6eb], succ=[0x7ac]
    =================================
    0x72c: v72c(0xd17) = CONST 
    0x730: v730(0x7ac) = CONST 
    0x733: JUMP v730(0x7ac)

    Begin block 0x7ac
    prev=[0x72b], succ=[0x7bb, 0x7f1]
    =================================
    0x7ad: v7ad(0x1) = CONST 
    0x7af: v7af(0x1) = CONST 
    0x7b1: v7b1(0xa0) = CONST 
    0x7b3: v7b3(0x10000000000000000000000000000000000000000) = SHL v7b1(0xa0), v7af(0x1)
    0x7b4: v7b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b3(0x10000000000000000000000000000000000000000), v7ad(0x1)
    0x7b6: v7b6 = AND v4bc, v7b4(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b7: v7b7(0x7f1) = CONST 
    0x7ba: JUMPI v7b7(0x7f1), v7b6

    Begin block 0x7bb
    prev=[0x7ac], succ=[]
    =================================
    0x7bb: v7bb(0x40) = CONST 
    0x7bd: v7bd = MLOAD v7bb(0x40)
    0x7be: v7be(0x461bcd) = CONST 
    0x7c2: v7c2(0xe5) = CONST 
    0x7c4: v7c4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7c2(0xe5), v7be(0x461bcd)
    0x7c6: MSTORE v7bd, v7c4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7c7: v7c7(0x4) = CONST 
    0x7c9: v7c9 = ADD v7c7(0x4), v7bd
    0x7cc: v7cc(0x20) = CONST 
    0x7ce: v7ce = ADD v7cc(0x20), v7c9
    0x7d1: v7d1(0x20) = SUB v7ce, v7c9
    0x7d3: MSTORE v7c9, v7d1(0x20)
    0x7d4: v7d4(0x26) = CONST 
    0x7d7: MSTORE v7ce, v7d4(0x26)
    0x7d8: v7d8(0x20) = CONST 
    0x7da: v7da = ADD v7d8(0x20), v7ce
    0x7dc: v7dc(0x88a) = CONST 
    0x7df: v7df(0x26) = CONST 
    0x7e2: CODECOPY v7da, v7dc(0x88a), v7df(0x26)
    0x7e3: v7e3(0x40) = CONST 
    0x7e5: v7e5 = ADD v7e3(0x40), v7da
    0x7e9: v7e9(0x40) = CONST 
    0x7eb: v7eb = MLOAD v7e9(0x40)
    0x7ee: v7ee(0x84) = SUB v7e5, v7eb
    0x7f0: REVERT v7eb, v7ee(0x84)

    Begin block 0x7f1
    prev=[0x7ac], succ=[0xd17]
    =================================
    0x7f2: v7f2(0x1) = CONST 
    0x7f4: v7f4 = SLOAD v7f2(0x1)
    0x7f5: v7f5(0x40) = CONST 
    0x7f7: v7f7 = MLOAD v7f5(0x40)
    0x7f8: v7f8(0x1) = CONST 
    0x7fa: v7fa(0x1) = CONST 
    0x7fc: v7fc(0xa0) = CONST 
    0x7fe: v7fe(0x10000000000000000000000000000000000000000) = SHL v7fc(0xa0), v7fa(0x1)
    0x7ff: v7ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fe(0x10000000000000000000000000000000000000000), v7f8(0x1)
    0x802: v802 = AND v4bc, v7ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x804: v804 = AND v7f4, v7ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x806: v806(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x828: v828(0x0) = CONST 
    0x82b: LOG3 v7f7, v828(0x0), v806(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v804, v802
    0x82c: v82c(0x1) = CONST 
    0x82f: v82f = SLOAD v82c(0x1)
    0x830: v830(0x1) = CONST 
    0x832: v832(0x1) = CONST 
    0x834: v834(0xa0) = CONST 
    0x836: v836(0x10000000000000000000000000000000000000000) = SHL v834(0xa0), v832(0x1)
    0x837: v837(0xffffffffffffffffffffffffffffffffffffffff) = SUB v836(0x10000000000000000000000000000000000000000), v830(0x1)
    0x838: v838(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v837(0xffffffffffffffffffffffffffffffffffffffff)
    0x839: v839 = AND v838(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v82f
    0x83a: v83a(0x1) = CONST 
    0x83c: v83c(0x1) = CONST 
    0x83e: v83e(0xa0) = CONST 
    0x840: v840(0x10000000000000000000000000000000000000000) = SHL v83e(0xa0), v83c(0x1)
    0x841: v841(0xffffffffffffffffffffffffffffffffffffffff) = SUB v840(0x10000000000000000000000000000000000000000), v83a(0x1)
    0x845: v845 = AND v841(0xffffffffffffffffffffffffffffffffffffffff), v4bc
    0x849: v849 = OR v845, v839
    0x84b: SSTORE v82c(0x1), v849
    0x84c: JUMP v72c(0xd17)

    Begin block 0xd17
    prev=[0x7f1], succ=[0xc38]
    =================================
    0xd19: JUMP v49c(0xc38)

    Begin block 0xc38
    prev=[0xd17], succ=[]
    =================================
    0xc39: STOP 

}

function 0x4c1(0x4c1arg0x0) private {
    Begin block 0x4c1
    prev=[], succ=[0xc59, 0x4fe]
    =================================
    0x4c2: v4c2(0x2) = CONST 
    0x4c5: v4c5 = SLOAD v4c2(0x2)
    0x4c6: v4c6(0x40) = CONST 
    0x4c9: v4c9 = MLOAD v4c6(0x40)
    0x4ca: v4ca(0x20) = CONST 
    0x4cc: v4cc(0x1) = CONST 
    0x4cf: v4cf = AND v4c5, v4cc(0x1)
    0x4d0: v4d0 = ISZERO v4cf
    0x4d1: v4d1(0x100) = CONST 
    0x4d4: v4d4 = MUL v4d1(0x100), v4d0
    0x4d5: v4d5(0x0) = CONST 
    0x4d7: v4d7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v4d5(0x0)
    0x4d8: v4d8 = ADD v4d7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v4d4
    0x4db: v4db = AND v4c5, v4d8
    0x4de: v4de = DIV v4db, v4c2(0x2)
    0x4df: v4df(0x1f) = CONST 
    0x4e2: v4e2 = ADD v4de, v4df(0x1f)
    0x4e5: v4e5 = DIV v4e2, v4ca(0x20)
    0x4e7: v4e7 = MUL v4ca(0x20), v4e5
    0x4e9: v4e9 = ADD v4c9, v4e7
    0x4eb: v4eb = ADD v4ca(0x20), v4e9
    0x4ee: MSTORE v4c6(0x40), v4eb
    0x4f1: MSTORE v4c9, v4de
    0x4f5: v4f5 = ADD v4c9, v4ca(0x20)
    0x4f9: v4f9 = ISZERO v4de
    0x4fa: v4fa(0xc59) = CONST 
    0x4fd: JUMPI v4fa(0xc59), v4f9

    Begin block 0xc59
    prev=[0x4c1], succ=[]
    =================================
    0xc60: RETURNPRIVATE v4c1arg0, v4c9, v4c1arg0

    Begin block 0x4fe
    prev=[0x4c1], succ=[0x506, 0x5190x4c1]
    =================================
    0x4ff: v4ff(0x1f) = CONST 
    0x501: v501 = LT v4ff(0x1f), v4de
    0x502: v502(0x519) = CONST 
    0x505: JUMPI v502(0x519), v501

    Begin block 0x506
    prev=[0x4fe], succ=[0xc80]
    =================================
    0x506: v506(0x100) = CONST 
    0x50b: v50b = SLOAD v4c2(0x2)
    0x50c: v50c = DIV v50b, v506(0x100)
    0x50d: v50d = MUL v50c, v506(0x100)
    0x50f: MSTORE v4f5, v50d
    0x511: v511(0x20) = CONST 
    0x513: v513 = ADD v511(0x20), v4f5
    0x515: v515(0xc80) = CONST 
    0x518: JUMP v515(0xc80)

    Begin block 0xc80
    prev=[0x506], succ=[]
    =================================
    0xc87: RETURNPRIVATE v4c1arg0, v4c9, v4c1arg0

    Begin block 0x5190x4c1
    prev=[0x4fe], succ=[0x5270x4c1]
    =================================
    0x51b0x4c1: v4c151b = ADD v4f5, v4de
    0x51e0x4c1: v4c151e(0x0) = CONST 
    0x5200x4c1: MSTORE v4c151e(0x0), v4c2(0x2)
    0x5210x4c1: v4c1521(0x20) = CONST 
    0x5230x4c1: v4c1523(0x0) = CONST 
    0x5250x4c1: v4c1525 = SHA3 v4c1523(0x0), v4c1521(0x20)

    Begin block 0x5270x4c1
    prev=[0x5270x4c1, 0x5190x4c1], succ=[0x5270x4c1, 0x53b0x4c1]
    =================================
    0x5270x4c1_0x0: v5274c1_0 = PHI v4f5, v4c1533
    0x5270x4c1_0x1: v5274c1_1 = PHI v4c152f, v4c1525
    0x5290x4c1: v4c1529 = SLOAD v5274c1_1
    0x52b0x4c1: MSTORE v5274c1_0, v4c1529
    0x52d0x4c1: v4c152d(0x1) = CONST 
    0x52f0x4c1: v4c152f = ADD v4c152d(0x1), v5274c1_1
    0x5310x4c1: v4c1531(0x20) = CONST 
    0x5330x4c1: v4c1533 = ADD v4c1531(0x20), v5274c1_0
    0x5360x4c1: v4c1536 = GT v4c151b, v4c1533
    0x5370x4c1: v4c1537(0x527) = CONST 
    0x53a0x4c1: JUMPI v4c1537(0x527), v4c1536

    Begin block 0x53b0x4c1
    prev=[0x5270x4c1], succ=[0x5440x4c1]
    =================================
    0x53d0x4c1: v4c153d = SUB v4c1533, v4c151b
    0x53e0x4c1: v4c153e(0x1f) = CONST 
    0x5400x4c1: v4c1540 = AND v4c153e(0x1f), v4c153d
    0x5420x4c1: v4c1542 = ADD v4c151b, v4c1540

    Begin block 0x5440x4c1
    prev=[0x53b0x4c1], succ=[]
    =================================
    0x54b0x4c1: RETURNPRIVATE v4c1arg0, v4c9, v4c1arg0

}

function 0x64b(0x64barg0x0) private {
    Begin block 0x64b
    prev=[], succ=[0xcc9, 0x68b]
    =================================
    0x64c: v64c(0x3) = CONST 
    0x64f: v64f = SLOAD v64c(0x3)
    0x650: v650(0x40) = CONST 
    0x653: v653 = MLOAD v650(0x40)
    0x654: v654(0x20) = CONST 
    0x656: v656(0x2) = CONST 
    0x658: v658(0x1) = CONST 
    0x65b: v65b = AND v64f, v658(0x1)
    0x65c: v65c = ISZERO v65b
    0x65d: v65d(0x100) = CONST 
    0x660: v660 = MUL v65d(0x100), v65c
    0x661: v661(0x0) = CONST 
    0x663: v663(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v661(0x0)
    0x664: v664 = ADD v663(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v660
    0x667: v667 = AND v64f, v664
    0x66b: v66b = DIV v667, v656(0x2)
    0x66c: v66c(0x1f) = CONST 
    0x66f: v66f = ADD v66b, v66c(0x1f)
    0x672: v672 = DIV v66f, v654(0x20)
    0x674: v674 = MUL v654(0x20), v672
    0x676: v676 = ADD v653, v674
    0x678: v678 = ADD v654(0x20), v676
    0x67b: MSTORE v650(0x40), v678
    0x67e: MSTORE v653, v66b
    0x682: v682 = ADD v653, v654(0x20)
    0x686: v686 = ISZERO v66b
    0x687: v687(0xcc9) = CONST 
    0x68a: JUMPI v687(0xcc9), v686

    Begin block 0xcc9
    prev=[0x64b], succ=[]
    =================================
    0xcd0: RETURNPRIVATE v64barg0, v653, v64barg0

    Begin block 0x68b
    prev=[0x64b], succ=[0x693, 0x5190x64b]
    =================================
    0x68c: v68c(0x1f) = CONST 
    0x68e: v68e = LT v68c(0x1f), v66b
    0x68f: v68f(0x519) = CONST 
    0x692: JUMPI v68f(0x519), v68e

    Begin block 0x693
    prev=[0x68b], succ=[0xcf0]
    =================================
    0x693: v693(0x100) = CONST 
    0x698: v698 = SLOAD v64c(0x3)
    0x699: v699 = DIV v698, v693(0x100)
    0x69a: v69a = MUL v699, v693(0x100)
    0x69c: MSTORE v682, v69a
    0x69e: v69e(0x20) = CONST 
    0x6a0: v6a0 = ADD v69e(0x20), v682
    0x6a2: v6a2(0xcf0) = CONST 
    0x6a5: JUMP v6a2(0xcf0)

    Begin block 0xcf0
    prev=[0x693], succ=[]
    =================================
    0xcf7: RETURNPRIVATE v64barg0, v653, v64barg0

    Begin block 0x5190x64b
    prev=[0x68b], succ=[0x5270x64b]
    =================================
    0x51b0x64b: v64b51b = ADD v682, v66b
    0x51e0x64b: v64b51e(0x0) = CONST 
    0x5200x64b: MSTORE v64b51e(0x0), v64c(0x3)
    0x5210x64b: v64b521(0x20) = CONST 
    0x5230x64b: v64b523(0x0) = CONST 
    0x5250x64b: v64b525 = SHA3 v64b523(0x0), v64b521(0x20)

    Begin block 0x5270x64b
    prev=[0x5270x64b, 0x5190x64b], succ=[0x5270x64b, 0x53b0x64b]
    =================================
    0x5270x64b_0x0: v52764b_0 = PHI v682, v64b533
    0x5270x64b_0x1: v52764b_1 = PHI v64b52f, v64b525
    0x5290x64b: v64b529 = SLOAD v52764b_1
    0x52b0x64b: MSTORE v52764b_0, v64b529
    0x52d0x64b: v64b52d(0x1) = CONST 
    0x52f0x64b: v64b52f = ADD v64b52d(0x1), v52764b_1
    0x5310x64b: v64b531(0x20) = CONST 
    0x5330x64b: v64b533 = ADD v64b531(0x20), v52764b_0
    0x5360x64b: v64b536 = GT v64b51b, v64b533
    0x5370x64b: v64b537(0x527) = CONST 
    0x53a0x64b: JUMPI v64b537(0x527), v64b536

    Begin block 0x53b0x64b
    prev=[0x5270x64b], succ=[0x5440x64b]
    =================================
    0x53d0x64b: v64b53d = SUB v64b533, v64b51b
    0x53e0x64b: v64b53e(0x1f) = CONST 
    0x5400x64b: v64b540 = AND v64b53e(0x1f), v64b53d
    0x5420x64b: v64b542 = ADD v64b51b, v64b540

    Begin block 0x5440x64b
    prev=[0x53b0x64b], succ=[]
    =================================
    0x54b0x64b: RETURNPRIVATE v64barg0, v653, v64barg0

}

