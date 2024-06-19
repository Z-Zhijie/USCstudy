function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xd37]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xcf7: vcf7(0xd37) = CONST 
    0xcf8: JUMPI vcf7(0xd37), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0xd3a]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x55ad42e) = CONST 
    0x3b: v3b = EQ v34, v35(0x55ad42e)
    0xcf9: vcf9(0xd3a) = CONST 
    0xcfa: JUMPI vcf9(0xd3a), v3b

    Begin block 0x40
    prev=[0xd], succ=[0xd3d, 0x4b]
    =================================
    0x41: v41(0xb5f2efd) = CONST 
    0x46: v46 = EQ v41(0xb5f2efd), v34
    0xcfb: vcfb(0xd3d) = CONST 
    0xcfc: JUMPI vcfb(0xd3d), v46

    Begin block 0xd3d
    prev=[0x40], succ=[]
    =================================
    0xd3e: vd3e(0x1cd) = CONST 
    0xd3f: CALLPRIVATE vd3e(0x1cd)

    Begin block 0x4b
    prev=[0x40], succ=[0xd40, 0x56]
    =================================
    0x4c: v4c(0x1e1d696a) = CONST 
    0x51: v51 = EQ v4c(0x1e1d696a), v34
    0xcfd: vcfd(0xd40) = CONST 
    0xcfe: JUMPI vcfd(0xd40), v51

    Begin block 0xd40
    prev=[0x4b], succ=[]
    =================================
    0xd41: vd41(0x1e5) = CONST 
    0xd42: CALLPRIVATE vd41(0x1e5)

    Begin block 0x56
    prev=[0x4b], succ=[0xd43, 0x61]
    =================================
    0x57: v57(0x27f3a72a) = CONST 
    0x5c: v5c = EQ v57(0x27f3a72a), v34
    0xcff: vcff(0xd43) = CONST 
    0xd00: JUMPI vcff(0xd43), v5c

    Begin block 0xd43
    prev=[0x56], succ=[]
    =================================
    0xd44: vd44(0x206) = CONST 
    0xd45: CALLPRIVATE vd44(0x206)

    Begin block 0x61
    prev=[0x56], succ=[0xd46, 0x6c]
    =================================
    0x62: v62(0x29fd50eb) = CONST 
    0x67: v67 = EQ v62(0x29fd50eb), v34
    0xd01: vd01(0xd46) = CONST 
    0xd02: JUMPI vd01(0xd46), v67

    Begin block 0xd46
    prev=[0x61], succ=[]
    =================================
    0xd47: vd47(0x22d) = CONST 
    0xd48: CALLPRIVATE vd47(0x22d)

    Begin block 0x6c
    prev=[0x61], succ=[0xd49, 0x77]
    =================================
    0x6d: v6d(0x38241c16) = CONST 
    0x72: v72 = EQ v6d(0x38241c16), v34
    0xd03: vd03(0xd49) = CONST 
    0xd04: JUMPI vd03(0xd49), v72

    Begin block 0xd49
    prev=[0x6c, 0x82, 0xda], succ=[]
    =================================
    0xd4a: vd4a(0x25e) = CONST 
    0xd4b: CALLPRIVATE vd4a(0x25e)

    Begin block 0x77
    prev=[0x6c], succ=[0xd4c, 0x82]
    =================================
    0x78: v78(0x4774027c) = CONST 
    0x7d: v7d = EQ v78(0x4774027c), v34
    0xd05: vd05(0xd4c) = CONST 
    0xd06: JUMPI vd05(0xd4c), v7d

    Begin block 0xd4c
    prev=[0x77], succ=[]
    =================================
    0xd4d: vd4d(0x28a) = CONST 
    0xd4e: CALLPRIVATE vd4d(0x28a)

    Begin block 0x82
    prev=[0x77], succ=[0xd49, 0x8d]
    =================================
    0x83: v83(0x6b84dfcd) = CONST 
    0x88: v88 = EQ v83(0x6b84dfcd), v34
    0xd07: vd07(0xd49) = CONST 
    0xd08: JUMPI vd07(0xd49), v88

    Begin block 0x8d
    prev=[0x82], succ=[0xd4f, 0x98]
    =================================
    0x8e: v8e(0x7642dc0f) = CONST 
    0x93: v93 = EQ v8e(0x7642dc0f), v34
    0xd09: vd09(0xd4f) = CONST 
    0xd0a: JUMPI vd09(0xd4f), v93

    Begin block 0xd4f
    prev=[0x8d], succ=[]
    =================================
    0xd50: vd50(0x2ab) = CONST 
    0xd51: CALLPRIVATE vd50(0x2ab)

    Begin block 0x98
    prev=[0x8d], succ=[0xd52, 0xa3]
    =================================
    0x99: v99(0x77b74692) = CONST 
    0x9e: v9e = EQ v99(0x77b74692), v34
    0xd0b: vd0b(0xd52) = CONST 
    0xd0c: JUMPI vd0b(0xd52), v9e

    Begin block 0xd52
    prev=[0x98], succ=[]
    =================================
    0xd53: vd53(0x2e7) = CONST 
    0xd54: CALLPRIVATE vd53(0x2e7)

    Begin block 0xa3
    prev=[0x98], succ=[0xd55, 0xae]
    =================================
    0xa4: va4(0x798b18fd) = CONST 
    0xa9: va9 = EQ va4(0x798b18fd), v34
    0xd0d: vd0d(0xd55) = CONST 
    0xd0e: JUMPI vd0d(0xd55), va9

    Begin block 0xd55
    prev=[0xa3], succ=[]
    =================================
    0xd56: vd56(0x2fc) = CONST 
    0xd57: CALLPRIVATE vd56(0x2fc)

    Begin block 0xae
    prev=[0xa3], succ=[0xd58, 0xb9]
    =================================
    0xaf: vaf(0x8da5cb5b) = CONST 
    0xb4: vb4 = EQ vaf(0x8da5cb5b), v34
    0xd0f: vd0f(0xd58) = CONST 
    0xd10: JUMPI vd0f(0xd58), vb4

    Begin block 0xd58
    prev=[0xae], succ=[]
    =================================
    0xd59: vd59(0x311) = CONST 
    0xd5a: CALLPRIVATE vd59(0x311)

    Begin block 0xb9
    prev=[0xae], succ=[0xd5b, 0xc4]
    =================================
    0xba: vba(0x9d3cc187) = CONST 
    0xbf: vbf = EQ vba(0x9d3cc187), v34
    0xd11: vd11(0xd5b) = CONST 
    0xd12: JUMPI vd11(0xd5b), vbf

    Begin block 0xd5b
    prev=[0xb9], succ=[]
    =================================
    0xd5c: vd5c(0x326) = CONST 
    0xd5d: CALLPRIVATE vd5c(0x326)

    Begin block 0xc4
    prev=[0xb9], succ=[0xd5e, 0xcf]
    =================================
    0xc5: vc5(0xa39a45b7) = CONST 
    0xca: vca = EQ vc5(0xa39a45b7), v34
    0xd13: vd13(0xd5e) = CONST 
    0xd14: JUMPI vd13(0xd5e), vca

    Begin block 0xd5e
    prev=[0xc4], succ=[]
    =================================
    0xd5f: vd5f(0x347) = CONST 
    0xd60: CALLPRIVATE vd5f(0x347)

    Begin block 0xcf
    prev=[0xc4], succ=[0xd37, 0xda]
    =================================
    0xd0: vd0(0xa6f2ae3a) = CONST 
    0xd5: vd5 = EQ vd0(0xa6f2ae3a), v34
    0xd15: vd15(0xd37) = CONST 
    0xd16: JUMPI vd15(0xd37), vd5

    Begin block 0xd37
    prev=[0x0, 0xcf, 0x17f], succ=[]
    =================================
    0xd38: vd38(0x18a) = CONST 
    0xd39: CALLPRIVATE vd38(0x18a)

    Begin block 0xda
    prev=[0xcf], succ=[0xd49, 0xe5]
    =================================
    0xdb: vdb(0xad5c1687) = CONST 
    0xe0: ve0 = EQ vdb(0xad5c1687), v34
    0xd17: vd17(0xd49) = CONST 
    0xd18: JUMPI vd17(0xd49), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0xd61, 0xf0]
    =================================
    0xe6: ve6(0xb19f30e2) = CONST 
    0xeb: veb = EQ ve6(0xb19f30e2), v34
    0xd19: vd19(0xd61) = CONST 
    0xd1a: JUMPI vd19(0xd61), veb

    Begin block 0xd61
    prev=[0xe5], succ=[]
    =================================
    0xd62: vd62(0x37c) = CONST 
    0xd63: CALLPRIVATE vd62(0x37c)

    Begin block 0xf0
    prev=[0xe5], succ=[0xd64, 0xfb]
    =================================
    0xf1: vf1(0xb3490bfc) = CONST 
    0xf6: vf6 = EQ vf1(0xb3490bfc), v34
    0xd1b: vd1b(0xd64) = CONST 
    0xd1c: JUMPI vd1b(0xd64), vf6

    Begin block 0xd64
    prev=[0xf0], succ=[]
    =================================
    0xd65: vd65(0x39d) = CONST 
    0xd66: CALLPRIVATE vd65(0x39d)

    Begin block 0xfb
    prev=[0xf0], succ=[0xd67, 0x106]
    =================================
    0xfc: vfc(0xb4d14728) = CONST 
    0x101: v101 = EQ vfc(0xb4d14728), v34
    0xd1d: vd1d(0xd67) = CONST 
    0xd1e: JUMPI vd1d(0xd67), v101

    Begin block 0xd67
    prev=[0xfb], succ=[]
    =================================
    0xd68: vd68(0x3d9) = CONST 
    0xd69: CALLPRIVATE vd68(0x3d9)

    Begin block 0x106
    prev=[0xfb], succ=[0xd6a, 0x111]
    =================================
    0x107: v107(0xb8be73ed) = CONST 
    0x10c: v10c = EQ v107(0xb8be73ed), v34
    0xd1f: vd1f(0xd6a) = CONST 
    0xd20: JUMPI vd1f(0xd6a), v10c

    Begin block 0xd6a
    prev=[0x106], succ=[]
    =================================
    0xd6b: vd6b(0x3ee) = CONST 
    0xd6c: CALLPRIVATE vd6b(0x3ee)

    Begin block 0x111
    prev=[0x106], succ=[0xd6d, 0x11c]
    =================================
    0x112: v112(0xbd3b1046) = CONST 
    0x117: v117 = EQ v112(0xbd3b1046), v34
    0xd21: vd21(0xd6d) = CONST 
    0xd22: JUMPI vd21(0xd6d), v117

    Begin block 0xd6d
    prev=[0x111], succ=[]
    =================================
    0xd6e: vd6e(0x403) = CONST 
    0xd6f: CALLPRIVATE vd6e(0x403)

    Begin block 0x11c
    prev=[0x111], succ=[0xd70, 0x127]
    =================================
    0x11d: v11d(0xc0ab5704) = CONST 
    0x122: v122 = EQ v11d(0xc0ab5704), v34
    0xd23: vd23(0xd70) = CONST 
    0xd24: JUMPI vd23(0xd70), v122

    Begin block 0xd70
    prev=[0x11c], succ=[]
    =================================
    0xd71: vd71(0x424) = CONST 
    0xd72: CALLPRIVATE vd71(0x424)

    Begin block 0x127
    prev=[0x11c], succ=[0xd73, 0x132]
    =================================
    0x128: v128(0xcd3f2910) = CONST 
    0x12d: v12d = EQ v128(0xcd3f2910), v34
    0xd25: vd25(0xd73) = CONST 
    0xd26: JUMPI vd25(0xd73), v12d

    Begin block 0xd73
    prev=[0x127], succ=[]
    =================================
    0xd74: vd74(0x44e) = CONST 
    0xd75: CALLPRIVATE vd74(0x44e)

    Begin block 0x132
    prev=[0x127], succ=[0xd76, 0x13d]
    =================================
    0x133: v133(0xd2d7231f) = CONST 
    0x138: v138 = EQ v133(0xd2d7231f), v34
    0xd27: vd27(0xd76) = CONST 
    0xd28: JUMPI vd27(0xd76), v138

    Begin block 0xd76
    prev=[0x132], succ=[]
    =================================
    0xd77: vd77(0x469) = CONST 
    0xd78: CALLPRIVATE vd77(0x469)

    Begin block 0x13d
    prev=[0x132], succ=[0xd79, 0x148]
    =================================
    0x13e: v13e(0xe16ba8c6) = CONST 
    0x143: v143 = EQ v13e(0xe16ba8c6), v34
    0xd29: vd29(0xd79) = CONST 
    0xd2a: JUMPI vd29(0xd79), v143

    Begin block 0xd79
    prev=[0x13d], succ=[]
    =================================
    0xd7a: vd7a(0x481) = CONST 
    0xd7b: CALLPRIVATE vd7a(0x481)

    Begin block 0x148
    prev=[0x13d], succ=[0xd7c, 0x153]
    =================================
    0x149: v149(0xe388c423) = CONST 
    0x14e: v14e = EQ v149(0xe388c423), v34
    0xd2b: vd2b(0xd7c) = CONST 
    0xd2c: JUMPI vd2b(0xd7c), v14e

    Begin block 0xd7c
    prev=[0x148], succ=[]
    =================================
    0xd7d: vd7d(0x496) = CONST 
    0xd7e: CALLPRIVATE vd7d(0x496)

    Begin block 0x153
    prev=[0x148], succ=[0xd7f, 0x15e]
    =================================
    0x154: v154(0xe696d303) = CONST 
    0x159: v159 = EQ v154(0xe696d303), v34
    0xd2d: vd2d(0xd7f) = CONST 
    0xd2e: JUMPI vd2d(0xd7f), v159

    Begin block 0xd7f
    prev=[0x153], succ=[]
    =================================
    0xd80: vd80(0x4dd) = CONST 
    0xd81: CALLPRIVATE vd80(0x4dd)

    Begin block 0x15e
    prev=[0x153], succ=[0xd82, 0x169]
    =================================
    0x15f: v15f(0xf0cecafc) = CONST 
    0x164: v164 = EQ v15f(0xf0cecafc), v34
    0xd2f: vd2f(0xd82) = CONST 
    0xd30: JUMPI vd2f(0xd82), v164

    Begin block 0xd82
    prev=[0x15e], succ=[]
    =================================
    0xd83: vd83(0x4fe) = CONST 
    0xd84: CALLPRIVATE vd83(0x4fe)

    Begin block 0x169
    prev=[0x15e], succ=[0xd85, 0x174]
    =================================
    0x16a: v16a(0xf9f8bdb7) = CONST 
    0x16f: v16f = EQ v16a(0xf9f8bdb7), v34
    0xd31: vd31(0xd85) = CONST 
    0xd32: JUMPI vd31(0xd85), v16f

    Begin block 0xd85
    prev=[0x169], succ=[]
    =================================
    0xd86: vd86(0x513) = CONST 
    0xd87: CALLPRIVATE vd86(0x513)

    Begin block 0x174
    prev=[0x169], succ=[0xd88, 0x17f]
    =================================
    0x175: v175(0xfc0c546a) = CONST 
    0x17a: v17a = EQ v175(0xfc0c546a), v34
    0xd33: vd33(0xd88) = CONST 
    0xd34: JUMPI vd33(0xd88), v17a

    Begin block 0xd88
    prev=[0x174], succ=[]
    =================================
    0xd89: vd89(0x528) = CONST 
    0xd8a: CALLPRIVATE vd89(0x528)

    Begin block 0x17f
    prev=[0x174], succ=[0xd37, 0xd8b]
    =================================
    0x180: v180(0xfedda89c) = CONST 
    0x185: v185 = EQ v180(0xfedda89c), v34
    0xd35: vd35(0xd8b) = CONST 
    0xd36: JUMPI vd35(0xd8b), v185

    Begin block 0xd8b
    prev=[0x17f], succ=[]
    =================================
    0xd8c: vd8c(0x53d) = CONST 
    0xd8d: CALLPRIVATE vd8c(0x53d)

    Begin block 0xd3a
    prev=[0xd], succ=[]
    =================================
    0xd3b: vd3b(0x194) = CONST 
    0xd3c: CALLPRIVATE vd3b(0x194)

}

function buy()() public {
    Begin block 0x18a
    prev=[], succ=[0x54e0x18a]
    =================================
    0x18b: v18b(0x868) = CONST 
    0x18e: v18e(0x54e) = CONST 
    0x191: JUMP v18e(0x54e)

    Begin block 0x54e0x18a
    prev=[0x18a], succ=[0x5750x18a, 0x8200x18a]
    =================================
    0x54f0x18a: v18a54f(0xd) = CONST 
    0x5510x18a: v18a551 = SLOAD v18a54f(0xd)
    0x5520x18a: v18a552(0x40) = CONST 
    0x5540x18a: v18a554 = MLOAD v18a552(0x40)
    0x5550x18a: v18a555(0x1) = CONST 
    0x5570x18a: v18a557(0xa0) = CONST 
    0x5590x18a: v18a559(0x2) = CONST 
    0x55b0x18a: v18a55b(0x10000000000000000000000000000000000000000) = EXP v18a559(0x2), v18a557(0xa0)
    0x55c0x18a: v18a55c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18a55b(0x10000000000000000000000000000000000000000), v18a555(0x1)
    0x55f0x18a: v18a55f = AND v18a551, v18a55c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x18a: v18a561 = CALLDATASIZE 
    0x5620x18a: v18a562(0x0) = CONST 
    0x5650x18a: CALLDATACOPY v18a554, v18a562(0x0), v18a561
    0x5660x18a: v18a566(0x0) = CONST 
    0x5690x18a: v18a569 = CALLDATASIZE 
    0x56c0x18a: v18a56c = GAS 
    0x56d0x18a: v18a56d = DELEGATECALL v18a56c, v18a55f, v18a554, v18a569, v18a554, v18a566(0x0)
    0x5700x18a: v18a570 = ISZERO v18a56d
    0x5710x18a: v18a571(0x820) = CONST 
    0x5740x18a: JUMPI v18a571(0x820), v18a570

    Begin block 0x5750x18a
    prev=[0x54e0x18a], succ=[]
    =================================
    0x5750x18a: STOP 

    Begin block 0x8200x18a
    prev=[0x54e0x18a], succ=[]
    =================================
    0x8210x18a: v18a821(0x0) = CONST 
    0x8240x18a: REVERT v18a821(0x0), v18a821(0x0)

}

function currentPhase()() public {
    Begin block 0x194
    prev=[], succ=[0x19c, 0x1a0]
    =================================
    0x195: v195 = CALLVALUE 
    0x197: v197 = ISZERO v195
    0x198: v198(0x1a0) = CONST 
    0x19b: JUMPI v198(0x1a0), v197

    Begin block 0x19c
    prev=[0x194], succ=[]
    =================================
    0x19c: v19c(0x0) = CONST 
    0x19f: REVERT v19c(0x0), v19c(0x0)

    Begin block 0x1a0
    prev=[0x194], succ=[0x57b]
    =================================
    0x1a2: v1a2(0x1a9) = CONST 
    0x1a5: v1a5(0x57b) = CONST 
    0x1a8: JUMP v1a5(0x57b)

    Begin block 0x57b
    prev=[0x1a0], succ=[0x1a9]
    =================================
    0x57c: v57c(0x4) = CONST 
    0x57e: v57e = SLOAD v57c(0x4)
    0x57f: v57f(0xff) = CONST 
    0x581: v581 = AND v57f(0xff), v57e
    0x583: JUMP v1a2(0x1a9)

    Begin block 0x1a9
    prev=[0x57b], succ=[0x1b8, 0x1b9]
    =================================
    0x1aa: v1aa(0x40) = CONST 
    0x1ac: v1ac = MLOAD v1aa(0x40)
    0x1af: v1af(0x8) = CONST 
    0x1b2: v1b2 = GT v581, v1af(0x8)
    0x1b3: v1b3 = ISZERO v1b2
    0x1b4: v1b4(0x1b9) = CONST 
    0x1b7: JUMPI v1b4(0x1b9), v1b3

    Begin block 0x1b8
    prev=[0x1a9], succ=[]
    =================================
    0x1b8: THROW 

    Begin block 0x1b9
    prev=[0x1a9], succ=[]
    =================================
    0x1ba: v1ba(0xff) = CONST 
    0x1bc: v1bc = AND v1ba(0xff), v581
    0x1be: MSTORE v1ac, v1bc
    0x1bf: v1bf(0x20) = CONST 
    0x1c1: v1c1 = ADD v1bf(0x20), v1ac
    0x1c5: v1c5(0x40) = CONST 
    0x1c7: v1c7 = MLOAD v1c5(0x40)
    0x1ca: v1ca(0x20) = SUB v1c1, v1c7
    0x1cc: RETURN v1c7, v1ca(0x20)

}

function setCurrentRate(uint256)() public {
    Begin block 0x1cd
    prev=[], succ=[0x1d5, 0x1d9]
    =================================
    0x1ce: v1ce = CALLVALUE 
    0x1d0: v1d0 = ISZERO v1ce
    0x1d1: v1d1(0x1d9) = CONST 
    0x1d4: JUMPI v1d1(0x1d9), v1d0

    Begin block 0x1d5
    prev=[0x1cd], succ=[]
    =================================
    0x1d5: v1d5(0x0) = CONST 
    0x1d8: REVERT v1d5(0x0), v1d5(0x0)

    Begin block 0x1d9
    prev=[0x1cd], succ=[0x54e0x1cd]
    =================================
    0x1db: v1db(0x889) = CONST 
    0x1de: v1de(0x4) = CONST 
    0x1e0: v1e0 = CALLDATALOAD v1de(0x4)
    0x1e1: v1e1(0x54e) = CONST 
    0x1e4: JUMP v1e1(0x54e)

    Begin block 0x54e0x1cd
    prev=[0x1d9], succ=[0x5750x1cd, 0x8200x1cd]
    =================================
    0x54f0x1cd: v1cd54f(0xd) = CONST 
    0x5510x1cd: v1cd551 = SLOAD v1cd54f(0xd)
    0x5520x1cd: v1cd552(0x40) = CONST 
    0x5540x1cd: v1cd554 = MLOAD v1cd552(0x40)
    0x5550x1cd: v1cd555(0x1) = CONST 
    0x5570x1cd: v1cd557(0xa0) = CONST 
    0x5590x1cd: v1cd559(0x2) = CONST 
    0x55b0x1cd: v1cd55b(0x10000000000000000000000000000000000000000) = EXP v1cd559(0x2), v1cd557(0xa0)
    0x55c0x1cd: v1cd55c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cd55b(0x10000000000000000000000000000000000000000), v1cd555(0x1)
    0x55f0x1cd: v1cd55f = AND v1cd551, v1cd55c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x1cd: v1cd561 = CALLDATASIZE 
    0x5620x1cd: v1cd562(0x0) = CONST 
    0x5650x1cd: CALLDATACOPY v1cd554, v1cd562(0x0), v1cd561
    0x5660x1cd: v1cd566(0x0) = CONST 
    0x5690x1cd: v1cd569 = CALLDATASIZE 
    0x56c0x1cd: v1cd56c = GAS 
    0x56d0x1cd: v1cd56d = DELEGATECALL v1cd56c, v1cd55f, v1cd554, v1cd569, v1cd554, v1cd566(0x0)
    0x5700x1cd: v1cd570 = ISZERO v1cd56d
    0x5710x1cd: v1cd571(0x820) = CONST 
    0x5740x1cd: JUMPI v1cd571(0x820), v1cd570

    Begin block 0x5750x1cd
    prev=[0x54e0x1cd], succ=[]
    =================================
    0x5750x1cd: STOP 

    Begin block 0x8200x1cd
    prev=[0x54e0x1cd], succ=[]
    =================================
    0x8210x1cd: v1cd821(0x0) = CONST 
    0x8240x1cd: REVERT v1cd821(0x0), v1cd821(0x0)

}

function changeLibAddress(address)() public {
    Begin block 0x1e5
    prev=[], succ=[0x1ed, 0x1f1]
    =================================
    0x1e6: v1e6 = CALLVALUE 
    0x1e8: v1e8 = ISZERO v1e6
    0x1e9: v1e9(0x1f1) = CONST 
    0x1ec: JUMPI v1e9(0x1f1), v1e8

    Begin block 0x1ed
    prev=[0x1e5], succ=[]
    =================================
    0x1ed: v1ed(0x0) = CONST 
    0x1f0: REVERT v1ed(0x0), v1ed(0x0)

    Begin block 0x1f1
    prev=[0x1e5], succ=[0x584]
    =================================
    0x1f3: v1f3(0x8aa) = CONST 
    0x1f6: v1f6(0x1) = CONST 
    0x1f8: v1f8(0xa0) = CONST 
    0x1fa: v1fa(0x2) = CONST 
    0x1fc: v1fc(0x10000000000000000000000000000000000000000) = EXP v1fa(0x2), v1f8(0xa0)
    0x1fd: v1fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fc(0x10000000000000000000000000000000000000000), v1f6(0x1)
    0x1fe: v1fe(0x4) = CONST 
    0x200: v200 = CALLDATALOAD v1fe(0x4)
    0x201: v201 = AND v200, v1fd(0xffffffffffffffffffffffffffffffffffffffff)
    0x202: v202(0x584) = CONST 
    0x205: JUMP v202(0x584)

    Begin block 0x584
    prev=[0x1f1], succ=[0x7cdB0x584]
    =================================
    0x585: v585(0x58c) = CONST 
    0x588: v588(0x7cd) = CONST 
    0x58b: JUMP v588(0x7cd)

    Begin block 0x7cdB0x584
    prev=[0x584], succ=[0x58c]
    =================================
    0x7ceS0x584: v7ceV584(0x0) = CONST 
    0x7d0S0x584: v7d0V584 = SLOAD v7ceV584(0x0)
    0x7d1S0x584: v7d1V584(0x1) = CONST 
    0x7d3S0x584: v7d3V584(0xa0) = CONST 
    0x7d5S0x584: v7d5V584(0x2) = CONST 
    0x7d7S0x584: v7d7V584(0x10000000000000000000000000000000000000000) = EXP v7d5V584(0x2), v7d3V584(0xa0)
    0x7d8S0x584: v7d8V584(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d7V584(0x10000000000000000000000000000000000000000), v7d1V584(0x1)
    0x7d9S0x584: v7d9V584 = AND v7d8V584(0xffffffffffffffffffffffffffffffffffffffff), v7d0V584
    0x7daS0x584: v7daV584 = CALLER 
    0x7dbS0x584: v7dbV584 = EQ v7daV584, v7d9V584
    0x7ddS0x584: JUMP v585(0x58c)

    Begin block 0x58c
    prev=[0x7cdB0x584], succ=[0x593, 0x597]
    =================================
    0x58d: v58d = ISZERO v7dbV584
    0x58e: v58e = ISZERO v58d
    0x58f: v58f(0x597) = CONST 
    0x592: JUMPI v58f(0x597), v58e

    Begin block 0x593
    prev=[0x58c], succ=[]
    =================================
    0x593: v593(0x0) = CONST 
    0x596: REVERT v593(0x0), v593(0x0)

    Begin block 0x597
    prev=[0x58c], succ=[0x8aa]
    =================================
    0x598: v598(0xd) = CONST 
    0x59b: v59b = SLOAD v598(0xd)
    0x59c: v59c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b1: v5b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v59c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5b2: v5b2 = AND v5b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v59b
    0x5b3: v5b3(0x1) = CONST 
    0x5b5: v5b5(0xa0) = CONST 
    0x5b7: v5b7(0x2) = CONST 
    0x5b9: v5b9(0x10000000000000000000000000000000000000000) = EXP v5b7(0x2), v5b5(0xa0)
    0x5ba: v5ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5b9(0x10000000000000000000000000000000000000000), v5b3(0x1)
    0x5be: v5be = AND v5ba(0xffffffffffffffffffffffffffffffffffffffff), v201
    0x5c2: v5c2 = OR v5be, v5b2
    0x5c4: SSTORE v598(0xd), v5c2
    0x5c5: JUMP v1f3(0x8aa)

    Begin block 0x8aa
    prev=[0x597], succ=[]
    =================================
    0x8ab: STOP 

}

function thisBalance()() public {
    Begin block 0x206
    prev=[], succ=[0x20e, 0x212]
    =================================
    0x207: v207 = CALLVALUE 
    0x209: v209 = ISZERO v207
    0x20a: v20a(0x212) = CONST 
    0x20d: JUMPI v20a(0x212), v209

    Begin block 0x20e
    prev=[0x206], succ=[]
    =================================
    0x20e: v20e(0x0) = CONST 
    0x211: REVERT v20e(0x0), v20e(0x0)

    Begin block 0x212
    prev=[0x206], succ=[0x5c6]
    =================================
    0x214: v214(0x8cb) = CONST 
    0x217: v217(0x5c6) = CONST 
    0x21a: JUMP v217(0x5c6)

    Begin block 0x5c6
    prev=[0x212], succ=[0x8cb]
    =================================
    0x5c7: v5c7(0x9) = CONST 
    0x5c9: v5c9 = SLOAD v5c7(0x9)
    0x5cb: JUMP v214(0x8cb)

    Begin block 0x8cb
    prev=[0x5c6], succ=[]
    =================================
    0x8cc: v8cc(0x40) = CONST 
    0x8cf: v8cf = MLOAD v8cc(0x40)
    0x8d2: MSTORE v8cf, v5c9
    0x8d3: v8d3 = MLOAD v8cc(0x40)
    0x8d7: v8d7(0x0) = SUB v8cf, v8d3
    0x8d8: v8d8(0x20) = CONST 
    0x8da: v8da(0x20) = ADD v8d8(0x20), v8d7(0x0)
    0x8dc: RETURN v8d3, v8da(0x20)

}

function libAddress()() public {
    Begin block 0x22d
    prev=[], succ=[0x235, 0x239]
    =================================
    0x22e: v22e = CALLVALUE 
    0x230: v230 = ISZERO v22e
    0x231: v231(0x239) = CONST 
    0x234: JUMPI v231(0x239), v230

    Begin block 0x235
    prev=[0x22d], succ=[]
    =================================
    0x235: v235(0x0) = CONST 
    0x238: REVERT v235(0x0), v235(0x0)

    Begin block 0x239
    prev=[0x22d], succ=[0x5cc]
    =================================
    0x23b: v23b(0x8fc) = CONST 
    0x23e: v23e(0x5cc) = CONST 
    0x241: JUMP v23e(0x5cc)

    Begin block 0x5cc
    prev=[0x239], succ=[0x8fc]
    =================================
    0x5cd: v5cd(0xd) = CONST 
    0x5cf: v5cf = SLOAD v5cd(0xd)
    0x5d0: v5d0(0x1) = CONST 
    0x5d2: v5d2(0xa0) = CONST 
    0x5d4: v5d4(0x2) = CONST 
    0x5d6: v5d6(0x10000000000000000000000000000000000000000) = EXP v5d4(0x2), v5d2(0xa0)
    0x5d7: v5d7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5d6(0x10000000000000000000000000000000000000000), v5d0(0x1)
    0x5d8: v5d8 = AND v5d7(0xffffffffffffffffffffffffffffffffffffffff), v5cf
    0x5da: JUMP v23b(0x8fc)

    Begin block 0x8fc
    prev=[0x5cc], succ=[]
    =================================
    0x8fd: v8fd(0x40) = CONST 
    0x900: v900 = MLOAD v8fd(0x40)
    0x901: v901(0x1) = CONST 
    0x903: v903(0xa0) = CONST 
    0x905: v905(0x2) = CONST 
    0x907: v907(0x10000000000000000000000000000000000000000) = EXP v905(0x2), v903(0xa0)
    0x908: v908(0xffffffffffffffffffffffffffffffffffffffff) = SUB v907(0x10000000000000000000000000000000000000000), v901(0x1)
    0x90b: v90b = AND v5d8, v908(0xffffffffffffffffffffffffffffffffffffffff)
    0x90d: MSTORE v900, v90b
    0x90e: v90e = MLOAD v8fd(0x40)
    0x912: v912(0x0) = SUB v900, v90e
    0x913: v913(0x20) = CONST 
    0x915: v915(0x20) = ADD v913(0x20), v912(0x0)
    0x917: RETURN v90e, v915(0x20)

}

function offchainUpload(address[],uint256[])() public {
    Begin block 0x25e
    prev=[], succ=[0x266, 0x26a]
    =================================
    0x25f: v25f = CALLVALUE 
    0x261: v261 = ISZERO v25f
    0x262: v262(0x26a) = CONST 
    0x265: JUMPI v262(0x26a), v261

    Begin block 0x266
    prev=[0x25e], succ=[]
    =================================
    0x266: v266(0x0) = CONST 
    0x269: REVERT v266(0x0), v266(0x0)

    Begin block 0x26a
    prev=[0x25e], succ=[0x54e0x25e]
    =================================
    0x26c: v26c(0x937) = CONST 
    0x26f: v26f(0x24) = CONST 
    0x271: v271(0x4) = CONST 
    0x274: v274 = CALLDATALOAD v271(0x4)
    0x277: v277 = ADD v274, v26f(0x24)
    0x27b: v27b = ADD v271(0x4), v274
    0x27c: v27c = CALLDATALOAD v27b
    0x27f: v27f = CALLDATALOAD v26f(0x24)
    0x282: v282 = ADD v27f, v26f(0x24)
    0x284: v284 = ADD v27f, v271(0x4)
    0x285: v285 = CALLDATALOAD v284
    0x286: v286(0x54e) = CONST 
    0x289: JUMP v286(0x54e)

    Begin block 0x54e0x25e
    prev=[0x26a], succ=[0x5750x25e, 0x8200x25e]
    =================================
    0x54f0x25e: v25e54f(0xd) = CONST 
    0x5510x25e: v25e551 = SLOAD v25e54f(0xd)
    0x5520x25e: v25e552(0x40) = CONST 
    0x5540x25e: v25e554 = MLOAD v25e552(0x40)
    0x5550x25e: v25e555(0x1) = CONST 
    0x5570x25e: v25e557(0xa0) = CONST 
    0x5590x25e: v25e559(0x2) = CONST 
    0x55b0x25e: v25e55b(0x10000000000000000000000000000000000000000) = EXP v25e559(0x2), v25e557(0xa0)
    0x55c0x25e: v25e55c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25e55b(0x10000000000000000000000000000000000000000), v25e555(0x1)
    0x55f0x25e: v25e55f = AND v25e551, v25e55c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x25e: v25e561 = CALLDATASIZE 
    0x5620x25e: v25e562(0x0) = CONST 
    0x5650x25e: CALLDATACOPY v25e554, v25e562(0x0), v25e561
    0x5660x25e: v25e566(0x0) = CONST 
    0x5690x25e: v25e569 = CALLDATASIZE 
    0x56c0x25e: v25e56c = GAS 
    0x56d0x25e: v25e56d = DELEGATECALL v25e56c, v25e55f, v25e554, v25e569, v25e554, v25e566(0x0)
    0x5700x25e: v25e570 = ISZERO v25e56d
    0x5710x25e: v25e571(0x820) = CONST 
    0x5740x25e: JUMPI v25e571(0x820), v25e570

    Begin block 0x5750x25e
    prev=[0x54e0x25e], succ=[]
    =================================
    0x5750x25e: STOP 

    Begin block 0x8200x25e
    prev=[0x54e0x25e], succ=[]
    =================================
    0x8210x25e: v25e821(0x0) = CONST 
    0x8240x25e: REVERT v25e821(0x0), v25e821(0x0)

}

function changeOffchainUploaderAddress(address)() public {
    Begin block 0x28a
    prev=[], succ=[0x292, 0x296]
    =================================
    0x28b: v28b = CALLVALUE 
    0x28d: v28d = ISZERO v28b
    0x28e: v28e(0x296) = CONST 
    0x291: JUMPI v28e(0x296), v28d

    Begin block 0x292
    prev=[0x28a], succ=[]
    =================================
    0x292: v292(0x0) = CONST 
    0x295: REVERT v292(0x0), v292(0x0)

    Begin block 0x296
    prev=[0x28a], succ=[0x5db]
    =================================
    0x298: v298(0x958) = CONST 
    0x29b: v29b(0x1) = CONST 
    0x29d: v29d(0xa0) = CONST 
    0x29f: v29f(0x2) = CONST 
    0x2a1: v2a1(0x10000000000000000000000000000000000000000) = EXP v29f(0x2), v29d(0xa0)
    0x2a2: v2a2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a1(0x10000000000000000000000000000000000000000), v29b(0x1)
    0x2a3: v2a3(0x4) = CONST 
    0x2a5: v2a5 = CALLDATALOAD v2a3(0x4)
    0x2a6: v2a6 = AND v2a5, v2a2(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a7: v2a7(0x5db) = CONST 
    0x2aa: JUMP v2a7(0x5db)

    Begin block 0x5db
    prev=[0x296], succ=[0x7cdB0x5db]
    =================================
    0x5dc: v5dc(0x5e3) = CONST 
    0x5df: v5df(0x7cd) = CONST 
    0x5e2: JUMP v5df(0x7cd)

    Begin block 0x7cdB0x5db
    prev=[0x5db], succ=[0x5e3]
    =================================
    0x7ceS0x5db: v7ceV5db(0x0) = CONST 
    0x7d0S0x5db: v7d0V5db = SLOAD v7ceV5db(0x0)
    0x7d1S0x5db: v7d1V5db(0x1) = CONST 
    0x7d3S0x5db: v7d3V5db(0xa0) = CONST 
    0x7d5S0x5db: v7d5V5db(0x2) = CONST 
    0x7d7S0x5db: v7d7V5db(0x10000000000000000000000000000000000000000) = EXP v7d5V5db(0x2), v7d3V5db(0xa0)
    0x7d8S0x5db: v7d8V5db(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d7V5db(0x10000000000000000000000000000000000000000), v7d1V5db(0x1)
    0x7d9S0x5db: v7d9V5db = AND v7d8V5db(0xffffffffffffffffffffffffffffffffffffffff), v7d0V5db
    0x7daS0x5db: v7daV5db = CALLER 
    0x7dbS0x5db: v7dbV5db = EQ v7daV5db, v7d9V5db
    0x7ddS0x5db: JUMP v5dc(0x5e3)

    Begin block 0x5e3
    prev=[0x7cdB0x5db], succ=[0x5ea, 0x5ee]
    =================================
    0x5e4: v5e4 = ISZERO v7dbV5db
    0x5e5: v5e5 = ISZERO v5e4
    0x5e6: v5e6(0x5ee) = CONST 
    0x5e9: JUMPI v5e6(0x5ee), v5e5

    Begin block 0x5ea
    prev=[0x5e3], succ=[]
    =================================
    0x5ea: v5ea(0x0) = CONST 
    0x5ed: REVERT v5ea(0x0), v5ea(0x0)

    Begin block 0x5ee
    prev=[0x5e3], succ=[0x958]
    =================================
    0x5ef: v5ef(0xa) = CONST 
    0x5f2: v5f2 = SLOAD v5ef(0xa)
    0x5f3: v5f3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x608: v608(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5f3(0xffffffffffffffffffffffffffffffffffffffff)
    0x609: v609 = AND v608(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5f2
    0x60a: v60a(0x1) = CONST 
    0x60c: v60c(0xa0) = CONST 
    0x60e: v60e(0x2) = CONST 
    0x610: v610(0x10000000000000000000000000000000000000000) = EXP v60e(0x2), v60c(0xa0)
    0x611: v611(0xffffffffffffffffffffffffffffffffffffffff) = SUB v610(0x10000000000000000000000000000000000000000), v60a(0x1)
    0x615: v615 = AND v611(0xffffffffffffffffffffffffffffffffffffffff), v2a6
    0x619: v619 = OR v615, v609
    0x61b: SSTORE v5ef(0xa), v619
    0x61c: JUMP v298(0x958)

    Begin block 0x958
    prev=[0x5ee], succ=[]
    =================================
    0x959: STOP 

}

function calcVesting(address)() public {
    Begin block 0x2ab
    prev=[], succ=[0x2b3, 0x2b7]
    =================================
    0x2ac: v2ac = CALLVALUE 
    0x2ae: v2ae = ISZERO v2ac
    0x2af: v2af(0x2b7) = CONST 
    0x2b2: JUMPI v2af(0x2b7), v2ae

    Begin block 0x2b3
    prev=[0x2ab], succ=[]
    =================================
    0x2b3: v2b3(0x0) = CONST 
    0x2b6: REVERT v2b3(0x0), v2b3(0x0)

    Begin block 0x2b7
    prev=[0x2ab], succ=[0x61d0x2ab]
    =================================
    0x2b9: v2b9(0x979) = CONST 
    0x2bc: v2bc(0x1) = CONST 
    0x2be: v2be(0xa0) = CONST 
    0x2c0: v2c0(0x2) = CONST 
    0x2c2: v2c2(0x10000000000000000000000000000000000000000) = EXP v2c0(0x2), v2be(0xa0)
    0x2c3: v2c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c2(0x10000000000000000000000000000000000000000), v2bc(0x1)
    0x2c4: v2c4(0x4) = CONST 
    0x2c6: v2c6 = CALLDATALOAD v2c4(0x4)
    0x2c7: v2c7 = AND v2c6, v2c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c8: v2c8(0x61d) = CONST 
    0x2cb: JUMP v2c8(0x61d)

    Begin block 0x61d0x2ab
    prev=[0x2b7], succ=[0x6480x2ab, 0x8440x2ab]
    =================================
    0x61e0x2ab: v2ab61e(0xd) = CONST 
    0x6200x2ab: v2ab620 = SLOAD v2ab61e(0xd)
    0x6210x2ab: v2ab621(0x40) = CONST 
    0x6230x2ab: v2ab623 = MLOAD v2ab621(0x40)
    0x6240x2ab: v2ab624(0x0) = CONST 
    0x6290x2ab: v2ab629(0x1) = CONST 
    0x62b0x2ab: v2ab62b(0xa0) = CONST 
    0x62d0x2ab: v2ab62d(0x2) = CONST 
    0x62f0x2ab: v2ab62f(0x10000000000000000000000000000000000000000) = EXP v2ab62d(0x2), v2ab62b(0xa0)
    0x6300x2ab: v2ab630(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ab62f(0x10000000000000000000000000000000000000000), v2ab629(0x1)
    0x6330x2ab: v2ab633 = AND v2ab620, v2ab630(0xffffffffffffffffffffffffffffffffffffffff)
    0x6350x2ab: v2ab635 = CALLDATASIZE 
    0x6380x2ab: CALLDATACOPY v2ab623, v2ab624(0x0), v2ab635
    0x6390x2ab: v2ab639(0x40) = CONST 
    0x63c0x2ab: v2ab63c = CALLDATASIZE 
    0x63f0x2ab: v2ab63f = GAS 
    0x6400x2ab: v2ab640 = DELEGATECALL v2ab63f, v2ab633, v2ab623, v2ab63c, v2ab623, v2ab639(0x40)
    0x6430x2ab: v2ab643 = ISZERO v2ab640
    0x6440x2ab: v2ab644(0x844) = CONST 
    0x6470x2ab: JUMPI v2ab644(0x844), v2ab643

    Begin block 0x6480x2ab
    prev=[0x61d0x2ab], succ=[]
    =================================
    0x6480x2ab: v2ab648(0x40) = CONST 
    0x64b0x2ab: RETURN v2ab623, v2ab648(0x40)

    Begin block 0x8440x2ab
    prev=[0x61d0x2ab], succ=[]
    =================================
    0x8450x2ab: v2ab845(0x0) = CONST 
    0x8480x2ab: REVERT v2ab845(0x0), v2ab845(0x0)

}

function setKYCAddress()() public {
    Begin block 0x2e7
    prev=[], succ=[0x2ef, 0x2f3]
    =================================
    0x2e8: v2e8 = CALLVALUE 
    0x2ea: v2ea = ISZERO v2e8
    0x2eb: v2eb(0x2f3) = CONST 
    0x2ee: JUMPI v2eb(0x2f3), v2ea

    Begin block 0x2ef
    prev=[0x2e7], succ=[]
    =================================
    0x2ef: v2ef(0x0) = CONST 
    0x2f2: REVERT v2ef(0x0), v2ef(0x0)

    Begin block 0x2f3
    prev=[0x2e7], succ=[0x64c]
    =================================
    0x2f5: v2f5(0x9b3) = CONST 
    0x2f8: v2f8(0x64c) = CONST 
    0x2fb: JUMP v2f8(0x64c)

    Begin block 0x64c
    prev=[0x2f3], succ=[0x9b3]
    =================================
    0x64d: v64d(0xb) = CONST 
    0x64f: v64f = SLOAD v64d(0xb)
    0x650: v650(0x1) = CONST 
    0x652: v652(0xa0) = CONST 
    0x654: v654(0x2) = CONST 
    0x656: v656(0x10000000000000000000000000000000000000000) = EXP v654(0x2), v652(0xa0)
    0x657: v657(0xffffffffffffffffffffffffffffffffffffffff) = SUB v656(0x10000000000000000000000000000000000000000), v650(0x1)
    0x658: v658 = AND v657(0xffffffffffffffffffffffffffffffffffffffff), v64f
    0x65a: JUMP v2f5(0x9b3)

    Begin block 0x9b3
    prev=[0x64c], succ=[]
    =================================
    0x9b4: v9b4(0x40) = CONST 
    0x9b7: v9b7 = MLOAD v9b4(0x40)
    0x9b8: v9b8(0x1) = CONST 
    0x9ba: v9ba(0xa0) = CONST 
    0x9bc: v9bc(0x2) = CONST 
    0x9be: v9be(0x10000000000000000000000000000000000000000) = EXP v9bc(0x2), v9ba(0xa0)
    0x9bf: v9bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9be(0x10000000000000000000000000000000000000000), v9b8(0x1)
    0x9c2: v9c2 = AND v658, v9bf(0xffffffffffffffffffffffffffffffffffffffff)
    0x9c4: MSTORE v9b7, v9c2
    0x9c5: v9c5 = MLOAD v9b4(0x40)
    0x9c9: v9c9(0x0) = SUB v9b7, v9c5
    0x9ca: v9ca(0x20) = CONST 
    0x9cc: v9cc(0x20) = ADD v9ca(0x20), v9c9(0x0)
    0x9ce: RETURN v9c5, v9cc(0x20)

}

function currentRateM()() public {
    Begin block 0x2fc
    prev=[], succ=[0x304, 0x308]
    =================================
    0x2fd: v2fd = CALLVALUE 
    0x2ff: v2ff = ISZERO v2fd
    0x300: v300(0x308) = CONST 
    0x303: JUMPI v300(0x308), v2ff

    Begin block 0x304
    prev=[0x2fc], succ=[]
    =================================
    0x304: v304(0x0) = CONST 
    0x307: REVERT v304(0x0), v304(0x0)

    Begin block 0x308
    prev=[0x2fc], succ=[0x65b]
    =================================
    0x30a: v30a(0x9ee) = CONST 
    0x30d: v30d(0x65b) = CONST 
    0x310: JUMP v30d(0x65b)

    Begin block 0x65b
    prev=[0x308], succ=[0x9ee]
    =================================
    0x65c: v65c(0x6) = CONST 
    0x65e: v65e = SLOAD v65c(0x6)
    0x660: JUMP v30a(0x9ee)

    Begin block 0x9ee
    prev=[0x65b], succ=[]
    =================================
    0x9ef: v9ef(0x40) = CONST 
    0x9f2: v9f2 = MLOAD v9ef(0x40)
    0x9f5: MSTORE v9f2, v65e
    0x9f6: v9f6 = MLOAD v9ef(0x40)
    0x9fa: v9fa(0x0) = SUB v9f2, v9f6
    0x9fb: v9fb(0x20) = CONST 
    0x9fd: v9fd(0x20) = ADD v9fb(0x20), v9fa(0x0)
    0x9ff: RETURN v9f6, v9fd(0x20)

}

function owner()() public {
    Begin block 0x311
    prev=[], succ=[0x319, 0x31d]
    =================================
    0x312: v312 = CALLVALUE 
    0x314: v314 = ISZERO v312
    0x315: v315(0x31d) = CONST 
    0x318: JUMPI v315(0x31d), v314

    Begin block 0x319
    prev=[0x311], succ=[]
    =================================
    0x319: v319(0x0) = CONST 
    0x31c: REVERT v319(0x0), v319(0x0)

    Begin block 0x31d
    prev=[0x311], succ=[0x661]
    =================================
    0x31f: v31f(0xa1f) = CONST 
    0x322: v322(0x661) = CONST 
    0x325: JUMP v322(0x661)

    Begin block 0x661
    prev=[0x31d], succ=[0xa1f]
    =================================
    0x662: v662(0x0) = CONST 
    0x664: v664 = SLOAD v662(0x0)
    0x665: v665(0x1) = CONST 
    0x667: v667(0xa0) = CONST 
    0x669: v669(0x2) = CONST 
    0x66b: v66b(0x10000000000000000000000000000000000000000) = EXP v669(0x2), v667(0xa0)
    0x66c: v66c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v66b(0x10000000000000000000000000000000000000000), v665(0x1)
    0x66d: v66d = AND v66c(0xffffffffffffffffffffffffffffffffffffffff), v664
    0x66f: JUMP v31f(0xa1f)

    Begin block 0xa1f
    prev=[0x661], succ=[]
    =================================
    0xa20: va20(0x40) = CONST 
    0xa23: va23 = MLOAD va20(0x40)
    0xa24: va24(0x1) = CONST 
    0xa26: va26(0xa0) = CONST 
    0xa28: va28(0x2) = CONST 
    0xa2a: va2a(0x10000000000000000000000000000000000000000) = EXP va28(0x2), va26(0xa0)
    0xa2b: va2b(0xffffffffffffffffffffffffffffffffffffffff) = SUB va2a(0x10000000000000000000000000000000000000000), va24(0x1)
    0xa2e: va2e = AND v66d, va2b(0xffffffffffffffffffffffffffffffffffffffff)
    0xa30: MSTORE va23, va2e
    0xa31: va31 = MLOAD va20(0x40)
    0xa35: va35(0x0) = SUB va23, va31
    0xa36: va36(0x20) = CONST 
    0xa38: va38(0x20) = ADD va36(0x20), va35(0x0)
    0xa3a: RETURN va31, va38(0x20)

}

function changeSetRateAddress(address)() public {
    Begin block 0x326
    prev=[], succ=[0x32e, 0x332]
    =================================
    0x327: v327 = CALLVALUE 
    0x329: v329 = ISZERO v327
    0x32a: v32a(0x332) = CONST 
    0x32d: JUMPI v32a(0x332), v329

    Begin block 0x32e
    prev=[0x326], succ=[]
    =================================
    0x32e: v32e(0x0) = CONST 
    0x331: REVERT v32e(0x0), v32e(0x0)

    Begin block 0x332
    prev=[0x326], succ=[0x670]
    =================================
    0x334: v334(0xa5a) = CONST 
    0x337: v337(0x1) = CONST 
    0x339: v339(0xa0) = CONST 
    0x33b: v33b(0x2) = CONST 
    0x33d: v33d(0x10000000000000000000000000000000000000000) = EXP v33b(0x2), v339(0xa0)
    0x33e: v33e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v33d(0x10000000000000000000000000000000000000000), v337(0x1)
    0x33f: v33f(0x4) = CONST 
    0x341: v341 = CALLDATALOAD v33f(0x4)
    0x342: v342 = AND v341, v33e(0xffffffffffffffffffffffffffffffffffffffff)
    0x343: v343(0x670) = CONST 
    0x346: JUMP v343(0x670)

    Begin block 0x670
    prev=[0x332], succ=[0x7cdB0x670]
    =================================
    0x671: v671(0x678) = CONST 
    0x674: v674(0x7cd) = CONST 
    0x677: JUMP v674(0x7cd)

    Begin block 0x7cdB0x670
    prev=[0x670], succ=[0x678]
    =================================
    0x7ceS0x670: v7ceV670(0x0) = CONST 
    0x7d0S0x670: v7d0V670 = SLOAD v7ceV670(0x0)
    0x7d1S0x670: v7d1V670(0x1) = CONST 
    0x7d3S0x670: v7d3V670(0xa0) = CONST 
    0x7d5S0x670: v7d5V670(0x2) = CONST 
    0x7d7S0x670: v7d7V670(0x10000000000000000000000000000000000000000) = EXP v7d5V670(0x2), v7d3V670(0xa0)
    0x7d8S0x670: v7d8V670(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d7V670(0x10000000000000000000000000000000000000000), v7d1V670(0x1)
    0x7d9S0x670: v7d9V670 = AND v7d8V670(0xffffffffffffffffffffffffffffffffffffffff), v7d0V670
    0x7daS0x670: v7daV670 = CALLER 
    0x7dbS0x670: v7dbV670 = EQ v7daV670, v7d9V670
    0x7ddS0x670: JUMP v671(0x678)

    Begin block 0x678
    prev=[0x7cdB0x670], succ=[0x67f, 0x683]
    =================================
    0x679: v679 = ISZERO v7dbV670
    0x67a: v67a = ISZERO v679
    0x67b: v67b(0x683) = CONST 
    0x67e: JUMPI v67b(0x683), v67a

    Begin block 0x67f
    prev=[0x678], succ=[]
    =================================
    0x67f: v67f(0x0) = CONST 
    0x682: REVERT v67f(0x0), v67f(0x0)

    Begin block 0x683
    prev=[0x678], succ=[0xa5a]
    =================================
    0x684: v684(0xc) = CONST 
    0x687: v687 = SLOAD v684(0xc)
    0x688: v688(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x69d: v69d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v688(0xffffffffffffffffffffffffffffffffffffffff)
    0x69e: v69e = AND v69d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v687
    0x69f: v69f(0x1) = CONST 
    0x6a1: v6a1(0xa0) = CONST 
    0x6a3: v6a3(0x2) = CONST 
    0x6a5: v6a5(0x10000000000000000000000000000000000000000) = EXP v6a3(0x2), v6a1(0xa0)
    0x6a6: v6a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6a5(0x10000000000000000000000000000000000000000), v69f(0x1)
    0x6aa: v6aa = AND v6a6(0xffffffffffffffffffffffffffffffffffffffff), v342
    0x6ae: v6ae = OR v6aa, v69e
    0x6b0: SSTORE v684(0xc), v6ae
    0x6b1: JUMP v334(0xa5a)

    Begin block 0xa5a
    prev=[0x683], succ=[]
    =================================
    0xa5b: STOP 

}

function replaceOwner(address)() public {
    Begin block 0x347
    prev=[], succ=[0x34f, 0x353]
    =================================
    0x348: v348 = CALLVALUE 
    0x34a: v34a = ISZERO v348
    0x34b: v34b(0x353) = CONST 
    0x34e: JUMPI v34b(0x353), v34a

    Begin block 0x34f
    prev=[0x347], succ=[]
    =================================
    0x34f: v34f(0x0) = CONST 
    0x352: REVERT v34f(0x0), v34f(0x0)

    Begin block 0x353
    prev=[0x347], succ=[0x6b2]
    =================================
    0x355: v355(0xa7b) = CONST 
    0x358: v358(0x1) = CONST 
    0x35a: v35a(0xa0) = CONST 
    0x35c: v35c(0x2) = CONST 
    0x35e: v35e(0x10000000000000000000000000000000000000000) = EXP v35c(0x2), v35a(0xa0)
    0x35f: v35f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35e(0x10000000000000000000000000000000000000000), v358(0x1)
    0x360: v360(0x4) = CONST 
    0x362: v362 = CALLDATALOAD v360(0x4)
    0x363: v363 = AND v362, v35f(0xffffffffffffffffffffffffffffffffffffffff)
    0x364: v364(0x6b2) = CONST 
    0x367: JUMP v364(0x6b2)

    Begin block 0x6b2
    prev=[0x353], succ=[0x7cdB0x6b2]
    =================================
    0x6b3: v6b3(0x0) = CONST 
    0x6b5: v6b5(0x6bc) = CONST 
    0x6b8: v6b8(0x7cd) = CONST 
    0x6bb: JUMP v6b8(0x7cd)

    Begin block 0x7cdB0x6b2
    prev=[0x6b2], succ=[0x6bc]
    =================================
    0x7ceS0x6b2: v7ceV6b2(0x0) = CONST 
    0x7d0S0x6b2: v7d0V6b2 = SLOAD v7ceV6b2(0x0)
    0x7d1S0x6b2: v7d1V6b2(0x1) = CONST 
    0x7d3S0x6b2: v7d3V6b2(0xa0) = CONST 
    0x7d5S0x6b2: v7d5V6b2(0x2) = CONST 
    0x7d7S0x6b2: v7d7V6b2(0x10000000000000000000000000000000000000000) = EXP v7d5V6b2(0x2), v7d3V6b2(0xa0)
    0x7d8S0x6b2: v7d8V6b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d7V6b2(0x10000000000000000000000000000000000000000), v7d1V6b2(0x1)
    0x7d9S0x6b2: v7d9V6b2 = AND v7d8V6b2(0xffffffffffffffffffffffffffffffffffffffff), v7d0V6b2
    0x7daS0x6b2: v7daV6b2 = CALLER 
    0x7dbS0x6b2: v7dbV6b2 = EQ v7daV6b2, v7d9V6b2
    0x7ddS0x6b2: JUMP v6b5(0x6bc)

    Begin block 0x6bc
    prev=[0x7cdB0x6b2], succ=[0x6c3, 0x6c7]
    =================================
    0x6bd: v6bd = ISZERO v7dbV6b2
    0x6be: v6be = ISZERO v6bd
    0x6bf: v6bf(0x6c7) = CONST 
    0x6c2: JUMPI v6bf(0x6c7), v6be

    Begin block 0x6c3
    prev=[0x6bc], succ=[]
    =================================
    0x6c3: v6c3(0x0) = CONST 
    0x6c6: REVERT v6c3(0x0), v6c3(0x0)

    Begin block 0x6c7
    prev=[0x6bc], succ=[0xa7b]
    =================================
    0x6c9: v6c9(0x0) = CONST 
    0x6cc: v6cc = SLOAD v6c9(0x0)
    0x6cd: v6cd(0x1) = CONST 
    0x6cf: v6cf(0xa0) = CONST 
    0x6d1: v6d1(0x2) = CONST 
    0x6d3: v6d3(0x10000000000000000000000000000000000000000) = EXP v6d1(0x2), v6cf(0xa0)
    0x6d4: v6d4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6d3(0x10000000000000000000000000000000000000000), v6cd(0x1)
    0x6d6: v6d6 = AND v363, v6d4(0xffffffffffffffffffffffffffffffffffffffff)
    0x6d7: v6d7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6ec: v6ec(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6d7(0xffffffffffffffffffffffffffffffffffffffff)
    0x6ef: v6ef = AND v6cc, v6ec(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x6f0: v6f0 = OR v6ef, v6d6
    0x6f2: SSTORE v6c9(0x0), v6f0
    0x6f3: v6f3(0x1) = CONST 
    0x6f8: JUMP v355(0xa7b)

    Begin block 0xa7b
    prev=[0x6c7], succ=[]
    =================================
    0xa7c: va7c(0x40) = CONST 
    0xa7f: va7f = MLOAD va7c(0x40)
    0xa81: va81 = ISZERO v6f3(0x1)
    0xa82: va82 = ISZERO va81
    0xa84: MSTORE va7f, va82
    0xa85: va85 = MLOAD va7c(0x40)
    0xa89: va89(0x0) = SUB va7f, va85
    0xa8a: va8a(0x20) = CONST 
    0xa8c: va8c(0x20) = ADD va8a(0x20), va89(0x0)
    0xa8e: RETURN va85, va8c(0x20)

}

function changeKYCAddress(address)() public {
    Begin block 0x37c
    prev=[], succ=[0x384, 0x388]
    =================================
    0x37d: v37d = CALLVALUE 
    0x37f: v37f = ISZERO v37d
    0x380: v380(0x388) = CONST 
    0x383: JUMPI v380(0x388), v37f

    Begin block 0x384
    prev=[0x37c], succ=[]
    =================================
    0x384: v384(0x0) = CONST 
    0x387: REVERT v384(0x0), v384(0x0)

    Begin block 0x388
    prev=[0x37c], succ=[0x6f9]
    =================================
    0x38a: v38a(0xaae) = CONST 
    0x38d: v38d(0x1) = CONST 
    0x38f: v38f(0xa0) = CONST 
    0x391: v391(0x2) = CONST 
    0x393: v393(0x10000000000000000000000000000000000000000) = EXP v391(0x2), v38f(0xa0)
    0x394: v394(0xffffffffffffffffffffffffffffffffffffffff) = SUB v393(0x10000000000000000000000000000000000000000), v38d(0x1)
    0x395: v395(0x4) = CONST 
    0x397: v397 = CALLDATALOAD v395(0x4)
    0x398: v398 = AND v397, v394(0xffffffffffffffffffffffffffffffffffffffff)
    0x399: v399(0x6f9) = CONST 
    0x39c: JUMP v399(0x6f9)

    Begin block 0x6f9
    prev=[0x388], succ=[0x7cdB0x6f9]
    =================================
    0x6fa: v6fa(0x701) = CONST 
    0x6fd: v6fd(0x7cd) = CONST 
    0x700: JUMP v6fd(0x7cd)

    Begin block 0x7cdB0x6f9
    prev=[0x6f9], succ=[0x701]
    =================================
    0x7ceS0x6f9: v7ceV6f9(0x0) = CONST 
    0x7d0S0x6f9: v7d0V6f9 = SLOAD v7ceV6f9(0x0)
    0x7d1S0x6f9: v7d1V6f9(0x1) = CONST 
    0x7d3S0x6f9: v7d3V6f9(0xa0) = CONST 
    0x7d5S0x6f9: v7d5V6f9(0x2) = CONST 
    0x7d7S0x6f9: v7d7V6f9(0x10000000000000000000000000000000000000000) = EXP v7d5V6f9(0x2), v7d3V6f9(0xa0)
    0x7d8S0x6f9: v7d8V6f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7d7V6f9(0x10000000000000000000000000000000000000000), v7d1V6f9(0x1)
    0x7d9S0x6f9: v7d9V6f9 = AND v7d8V6f9(0xffffffffffffffffffffffffffffffffffffffff), v7d0V6f9
    0x7daS0x6f9: v7daV6f9 = CALLER 
    0x7dbS0x6f9: v7dbV6f9 = EQ v7daV6f9, v7d9V6f9
    0x7ddS0x6f9: JUMP v6fa(0x701)

    Begin block 0x701
    prev=[0x7cdB0x6f9], succ=[0x708, 0x70c]
    =================================
    0x702: v702 = ISZERO v7dbV6f9
    0x703: v703 = ISZERO v702
    0x704: v704(0x70c) = CONST 
    0x707: JUMPI v704(0x70c), v703

    Begin block 0x708
    prev=[0x701], succ=[]
    =================================
    0x708: v708(0x0) = CONST 
    0x70b: REVERT v708(0x0), v708(0x0)

    Begin block 0x70c
    prev=[0x701], succ=[0xaae]
    =================================
    0x70d: v70d(0xb) = CONST 
    0x710: v710 = SLOAD v70d(0xb)
    0x711: v711(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x726: v726(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v711(0xffffffffffffffffffffffffffffffffffffffff)
    0x727: v727 = AND v726(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v710
    0x728: v728(0x1) = CONST 
    0x72a: v72a(0xa0) = CONST 
    0x72c: v72c(0x2) = CONST 
    0x72e: v72e(0x10000000000000000000000000000000000000000) = EXP v72c(0x2), v72a(0xa0)
    0x72f: v72f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v72e(0x10000000000000000000000000000000000000000), v728(0x1)
    0x733: v733 = AND v72f(0xffffffffffffffffffffffffffffffffffffffff), v398
    0x737: v737 = OR v733, v727
    0x739: SSTORE v70d(0xb), v737
    0x73a: JUMP v38a(0xaae)

    Begin block 0xaae
    prev=[0x70c], succ=[]
    =================================
    0xaaf: STOP 

}

function allowTransfer(address)() public {
    Begin block 0x39d
    prev=[], succ=[0x3a5, 0x3a9]
    =================================
    0x39e: v39e = CALLVALUE 
    0x3a0: v3a0 = ISZERO v39e
    0x3a1: v3a1(0x3a9) = CONST 
    0x3a4: JUMPI v3a1(0x3a9), v3a0

    Begin block 0x3a5
    prev=[0x39d], succ=[]
    =================================
    0x3a5: v3a5(0x0) = CONST 
    0x3a8: REVERT v3a5(0x0), v3a5(0x0)

    Begin block 0x3a9
    prev=[0x39d], succ=[0x61d0x39d]
    =================================
    0x3ab: v3ab(0x3be) = CONST 
    0x3ae: v3ae(0x1) = CONST 
    0x3b0: v3b0(0xa0) = CONST 
    0x3b2: v3b2(0x2) = CONST 
    0x3b4: v3b4(0x10000000000000000000000000000000000000000) = EXP v3b2(0x2), v3b0(0xa0)
    0x3b5: v3b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b4(0x10000000000000000000000000000000000000000), v3ae(0x1)
    0x3b6: v3b6(0x4) = CONST 
    0x3b8: v3b8 = CALLDATALOAD v3b6(0x4)
    0x3b9: v3b9 = AND v3b8, v3b5(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ba: v3ba(0x61d) = CONST 
    0x3bd: JUMP v3ba(0x61d)

    Begin block 0x61d0x39d
    prev=[0x3a9], succ=[0x6480x39d, 0x8440x39d]
    =================================
    0x61e0x39d: v39d61e(0xd) = CONST 
    0x6200x39d: v39d620 = SLOAD v39d61e(0xd)
    0x6210x39d: v39d621(0x40) = CONST 
    0x6230x39d: v39d623 = MLOAD v39d621(0x40)
    0x6240x39d: v39d624(0x0) = CONST 
    0x6290x39d: v39d629(0x1) = CONST 
    0x62b0x39d: v39d62b(0xa0) = CONST 
    0x62d0x39d: v39d62d(0x2) = CONST 
    0x62f0x39d: v39d62f(0x10000000000000000000000000000000000000000) = EXP v39d62d(0x2), v39d62b(0xa0)
    0x6300x39d: v39d630(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39d62f(0x10000000000000000000000000000000000000000), v39d629(0x1)
    0x6330x39d: v39d633 = AND v39d620, v39d630(0xffffffffffffffffffffffffffffffffffffffff)
    0x6350x39d: v39d635 = CALLDATASIZE 
    0x6380x39d: CALLDATACOPY v39d623, v39d624(0x0), v39d635
    0x6390x39d: v39d639(0x40) = CONST 
    0x63c0x39d: v39d63c = CALLDATASIZE 
    0x63f0x39d: v39d63f = GAS 
    0x6400x39d: v39d640 = DELEGATECALL v39d63f, v39d633, v39d623, v39d63c, v39d623, v39d639(0x40)
    0x6430x39d: v39d643 = ISZERO v39d640
    0x6440x39d: v39d644(0x844) = CONST 
    0x6470x39d: JUMPI v39d644(0x844), v39d643

    Begin block 0x6480x39d
    prev=[0x61d0x39d], succ=[]
    =================================
    0x6480x39d: v39d648(0x40) = CONST 
    0x64b0x39d: RETURN v39d623, v39d648(0x40)

    Begin block 0x8440x39d
    prev=[0x61d0x39d], succ=[]
    =================================
    0x8450x39d: v39d845(0x0) = CONST 
    0x8480x39d: REVERT v39d845(0x0), v39d845(0x0)

}

function setRateAddress()() public {
    Begin block 0x3d9
    prev=[], succ=[0x3e1, 0x3e5]
    =================================
    0x3da: v3da = CALLVALUE 
    0x3dc: v3dc = ISZERO v3da
    0x3dd: v3dd(0x3e5) = CONST 
    0x3e0: JUMPI v3dd(0x3e5), v3dc

    Begin block 0x3e1
    prev=[0x3d9], succ=[]
    =================================
    0x3e1: v3e1(0x0) = CONST 
    0x3e4: REVERT v3e1(0x0), v3e1(0x0)

    Begin block 0x3e5
    prev=[0x3d9], succ=[0x73b]
    =================================
    0x3e7: v3e7(0xacf) = CONST 
    0x3ea: v3ea(0x73b) = CONST 
    0x3ed: JUMP v3ea(0x73b)

    Begin block 0x73b
    prev=[0x3e5], succ=[0xacf]
    =================================
    0x73c: v73c(0xc) = CONST 
    0x73e: v73e = SLOAD v73c(0xc)
    0x73f: v73f(0x1) = CONST 
    0x741: v741(0xa0) = CONST 
    0x743: v743(0x2) = CONST 
    0x745: v745(0x10000000000000000000000000000000000000000) = EXP v743(0x2), v741(0xa0)
    0x746: v746(0xffffffffffffffffffffffffffffffffffffffff) = SUB v745(0x10000000000000000000000000000000000000000), v73f(0x1)
    0x747: v747 = AND v746(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x749: JUMP v3e7(0xacf)

    Begin block 0xacf
    prev=[0x73b], succ=[]
    =================================
    0xad0: vad0(0x40) = CONST 
    0xad3: vad3 = MLOAD vad0(0x40)
    0xad4: vad4(0x1) = CONST 
    0xad6: vad6(0xa0) = CONST 
    0xad8: vad8(0x2) = CONST 
    0xada: vada(0x10000000000000000000000000000000000000000) = EXP vad8(0x2), vad6(0xa0)
    0xadb: vadb(0xffffffffffffffffffffffffffffffffffffffff) = SUB vada(0x10000000000000000000000000000000000000000), vad4(0x1)
    0xade: vade = AND v747, vadb(0xffffffffffffffffffffffffffffffffffffffff)
    0xae0: MSTORE vad3, vade
    0xae1: vae1 = MLOAD vad0(0x40)
    0xae5: vae5(0x0) = SUB vad3, vae1
    0xae6: vae6(0x20) = CONST 
    0xae8: vae8(0x20) = ADD vae6(0x20), vae5(0x0)
    0xaea: RETURN vae1, vae8(0x20)

}

function offchainUploaderAddress()() public {
    Begin block 0x3ee
    prev=[], succ=[0x3f6, 0x3fa]
    =================================
    0x3ef: v3ef = CALLVALUE 
    0x3f1: v3f1 = ISZERO v3ef
    0x3f2: v3f2(0x3fa) = CONST 
    0x3f5: JUMPI v3f2(0x3fa), v3f1

    Begin block 0x3f6
    prev=[0x3ee], succ=[]
    =================================
    0x3f6: v3f6(0x0) = CONST 
    0x3f9: REVERT v3f6(0x0), v3f6(0x0)

    Begin block 0x3fa
    prev=[0x3ee], succ=[0x74a]
    =================================
    0x3fc: v3fc(0xb0a) = CONST 
    0x3ff: v3ff(0x74a) = CONST 
    0x402: JUMP v3ff(0x74a)

    Begin block 0x74a
    prev=[0x3fa], succ=[0xb0a]
    =================================
    0x74b: v74b(0xa) = CONST 
    0x74d: v74d = SLOAD v74b(0xa)
    0x74e: v74e(0x1) = CONST 
    0x750: v750(0xa0) = CONST 
    0x752: v752(0x2) = CONST 
    0x754: v754(0x10000000000000000000000000000000000000000) = EXP v752(0x2), v750(0xa0)
    0x755: v755(0xffffffffffffffffffffffffffffffffffffffff) = SUB v754(0x10000000000000000000000000000000000000000), v74e(0x1)
    0x756: v756 = AND v755(0xffffffffffffffffffffffffffffffffffffffff), v74d
    0x758: JUMP v3fc(0xb0a)

    Begin block 0xb0a
    prev=[0x74a], succ=[]
    =================================
    0xb0b: vb0b(0x40) = CONST 
    0xb0e: vb0e = MLOAD vb0b(0x40)
    0xb0f: vb0f(0x1) = CONST 
    0xb11: vb11(0xa0) = CONST 
    0xb13: vb13(0x2) = CONST 
    0xb15: vb15(0x10000000000000000000000000000000000000000) = EXP vb13(0x2), vb11(0xa0)
    0xb16: vb16(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb15(0x10000000000000000000000000000000000000000), vb0f(0x1)
    0xb19: vb19 = AND v756, vb16(0xffffffffffffffffffffffffffffffffffffffff)
    0xb1b: MSTORE vb0e, vb19
    0xb1c: vb1c = MLOAD vb0b(0x40)
    0xb20: vb20(0x0) = SUB vb0e, vb1c
    0xb21: vb21(0x20) = CONST 
    0xb23: vb23(0x20) = ADD vb21(0x20), vb20(0x0)
    0xb25: RETURN vb1c, vb23(0x20)

}

function KYC(address)() public {
    Begin block 0x403
    prev=[], succ=[0x40b, 0x40f]
    =================================
    0x404: v404 = CALLVALUE 
    0x406: v406 = ISZERO v404
    0x407: v407(0x40f) = CONST 
    0x40a: JUMPI v407(0x40f), v406

    Begin block 0x40b
    prev=[0x403], succ=[]
    =================================
    0x40b: v40b(0x0) = CONST 
    0x40e: REVERT v40b(0x0), v40b(0x0)

    Begin block 0x40f
    prev=[0x403], succ=[0x759]
    =================================
    0x411: v411(0xb45) = CONST 
    0x414: v414(0x1) = CONST 
    0x416: v416(0xa0) = CONST 
    0x418: v418(0x2) = CONST 
    0x41a: v41a(0x10000000000000000000000000000000000000000) = EXP v418(0x2), v416(0xa0)
    0x41b: v41b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v41a(0x10000000000000000000000000000000000000000), v414(0x1)
    0x41c: v41c(0x4) = CONST 
    0x41e: v41e = CALLDATALOAD v41c(0x4)
    0x41f: v41f = AND v41e, v41b(0xffffffffffffffffffffffffffffffffffffffff)
    0x420: v420(0x759) = CONST 
    0x423: JUMP v420(0x759)

    Begin block 0x759
    prev=[0x40f], succ=[0xb45]
    =================================
    0x75a: v75a(0x1) = CONST 
    0x75c: v75c(0x20) = CONST 
    0x75e: MSTORE v75c(0x20), v75a(0x1)
    0x75f: v75f(0x0) = CONST 
    0x763: MSTORE v75f(0x0), v41f
    0x764: v764(0x40) = CONST 
    0x767: v767 = SHA3 v75f(0x0), v764(0x40)
    0x768: v768 = SLOAD v767
    0x769: v769(0xff) = CONST 
    0x76b: v76b = AND v769(0xff), v768
    0x76d: JUMP v411(0xb45)

    Begin block 0xb45
    prev=[0x759], succ=[]
    =================================
    0xb46: vb46(0x40) = CONST 
    0xb49: vb49 = MLOAD vb46(0x40)
    0xb4b: vb4b = ISZERO v76b
    0xb4c: vb4c = ISZERO vb4b
    0xb4e: MSTORE vb49, vb4c
    0xb4f: vb4f = MLOAD vb46(0x40)
    0xb53: vb53(0x0) = SUB vb49, vb4f
    0xb54: vb54(0x20) = CONST 
    0xb56: vb56(0x20) = ADD vb54(0x20), vb53(0x0)
    0xb58: RETURN vb4f, vb56(0x20)

}

function setVesting(address,uint256,uint256,uint256)() public {
    Begin block 0x424
    prev=[], succ=[0x42c, 0x430]
    =================================
    0x425: v425 = CALLVALUE 
    0x427: v427 = ISZERO v425
    0x428: v428(0x430) = CONST 
    0x42b: JUMPI v428(0x430), v427

    Begin block 0x42c
    prev=[0x424], succ=[]
    =================================
    0x42c: v42c(0x0) = CONST 
    0x42f: REVERT v42c(0x0), v42c(0x0)

    Begin block 0x430
    prev=[0x424], succ=[0x54e0x424]
    =================================
    0x432: v432(0xb78) = CONST 
    0x435: v435(0x1) = CONST 
    0x437: v437(0xa0) = CONST 
    0x439: v439(0x2) = CONST 
    0x43b: v43b(0x10000000000000000000000000000000000000000) = EXP v439(0x2), v437(0xa0)
    0x43c: v43c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43b(0x10000000000000000000000000000000000000000), v435(0x1)
    0x43d: v43d(0x4) = CONST 
    0x43f: v43f = CALLDATALOAD v43d(0x4)
    0x440: v440 = AND v43f, v43c(0xffffffffffffffffffffffffffffffffffffffff)
    0x441: v441(0x24) = CONST 
    0x443: v443 = CALLDATALOAD v441(0x24)
    0x444: v444(0x44) = CONST 
    0x446: v446 = CALLDATALOAD v444(0x44)
    0x447: v447(0x64) = CONST 
    0x449: v449 = CALLDATALOAD v447(0x64)
    0x44a: v44a(0x54e) = CONST 
    0x44d: JUMP v44a(0x54e)

    Begin block 0x54e0x424
    prev=[0x430], succ=[0x5750x424, 0x8200x424]
    =================================
    0x54f0x424: v42454f(0xd) = CONST 
    0x5510x424: v424551 = SLOAD v42454f(0xd)
    0x5520x424: v424552(0x40) = CONST 
    0x5540x424: v424554 = MLOAD v424552(0x40)
    0x5550x424: v424555(0x1) = CONST 
    0x5570x424: v424557(0xa0) = CONST 
    0x5590x424: v424559(0x2) = CONST 
    0x55b0x424: v42455b(0x10000000000000000000000000000000000000000) = EXP v424559(0x2), v424557(0xa0)
    0x55c0x424: v42455c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v42455b(0x10000000000000000000000000000000000000000), v424555(0x1)
    0x55f0x424: v42455f = AND v424551, v42455c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x424: v424561 = CALLDATASIZE 
    0x5620x424: v424562(0x0) = CONST 
    0x5650x424: CALLDATACOPY v424554, v424562(0x0), v424561
    0x5660x424: v424566(0x0) = CONST 
    0x5690x424: v424569 = CALLDATASIZE 
    0x56c0x424: v42456c = GAS 
    0x56d0x424: v42456d = DELEGATECALL v42456c, v42455f, v424554, v424569, v424554, v424566(0x0)
    0x5700x424: v424570 = ISZERO v42456d
    0x5710x424: v424571(0x820) = CONST 
    0x5740x424: JUMPI v424571(0x820), v424570

    Begin block 0x5750x424
    prev=[0x54e0x424], succ=[]
    =================================
    0x5750x424: STOP 

    Begin block 0x8200x424
    prev=[0x54e0x424], succ=[]
    =================================
    0x8210x424: v424821(0x0) = CONST 
    0x8240x424: REVERT v424821(0x0), v424821(0x0)

}

function setCurrentPhase(uint8)() public {
    Begin block 0x44e
    prev=[], succ=[0x456, 0x45a]
    =================================
    0x44f: v44f = CALLVALUE 
    0x451: v451 = ISZERO v44f
    0x452: v452(0x45a) = CONST 
    0x455: JUMPI v452(0x45a), v451

    Begin block 0x456
    prev=[0x44e], succ=[]
    =================================
    0x456: v456(0x0) = CONST 
    0x459: REVERT v456(0x0), v456(0x0)

    Begin block 0x45a
    prev=[0x44e], succ=[0x54e0x44e]
    =================================
    0x45c: v45c(0xb99) = CONST 
    0x45f: v45f(0xff) = CONST 
    0x461: v461(0x4) = CONST 
    0x463: v463 = CALLDATALOAD v461(0x4)
    0x464: v464 = AND v463, v45f(0xff)
    0x465: v465(0x54e) = CONST 
    0x468: JUMP v465(0x54e)

    Begin block 0x54e0x44e
    prev=[0x45a], succ=[0x5750x44e, 0x8200x44e]
    =================================
    0x54f0x44e: v44e54f(0xd) = CONST 
    0x5510x44e: v44e551 = SLOAD v44e54f(0xd)
    0x5520x44e: v44e552(0x40) = CONST 
    0x5540x44e: v44e554 = MLOAD v44e552(0x40)
    0x5550x44e: v44e555(0x1) = CONST 
    0x5570x44e: v44e557(0xa0) = CONST 
    0x5590x44e: v44e559(0x2) = CONST 
    0x55b0x44e: v44e55b(0x10000000000000000000000000000000000000000) = EXP v44e559(0x2), v44e557(0xa0)
    0x55c0x44e: v44e55c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v44e55b(0x10000000000000000000000000000000000000000), v44e555(0x1)
    0x55f0x44e: v44e55f = AND v44e551, v44e55c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x44e: v44e561 = CALLDATASIZE 
    0x5620x44e: v44e562(0x0) = CONST 
    0x5650x44e: CALLDATACOPY v44e554, v44e562(0x0), v44e561
    0x5660x44e: v44e566(0x0) = CONST 
    0x5690x44e: v44e569 = CALLDATASIZE 
    0x56c0x44e: v44e56c = GAS 
    0x56d0x44e: v44e56d = DELEGATECALL v44e56c, v44e55f, v44e554, v44e569, v44e554, v44e566(0x0)
    0x5700x44e: v44e570 = ISZERO v44e56d
    0x5710x44e: v44e571(0x820) = CONST 
    0x5740x44e: JUMPI v44e571(0x820), v44e570

    Begin block 0x5750x44e
    prev=[0x54e0x44e], succ=[]
    =================================
    0x5750x44e: STOP 

    Begin block 0x8200x44e
    prev=[0x54e0x44e], succ=[]
    =================================
    0x8210x44e: v44e821(0x0) = CONST 
    0x8240x44e: REVERT v44e821(0x0), v44e821(0x0)

}

function calculateReward(uint256)() public {
    Begin block 0x469
    prev=[], succ=[0x471, 0x475]
    =================================
    0x46a: v46a = CALLVALUE 
    0x46c: v46c = ISZERO v46a
    0x46d: v46d(0x475) = CONST 
    0x470: JUMPI v46d(0x475), v46c

    Begin block 0x471
    prev=[0x469], succ=[]
    =================================
    0x471: v471(0x0) = CONST 
    0x474: REVERT v471(0x0), v471(0x0)

    Begin block 0x475
    prev=[0x469], succ=[0x61d0x469]
    =================================
    0x477: v477(0xbba) = CONST 
    0x47a: v47a(0x4) = CONST 
    0x47c: v47c = CALLDATALOAD v47a(0x4)
    0x47d: v47d(0x61d) = CONST 
    0x480: JUMP v47d(0x61d)

    Begin block 0x61d0x469
    prev=[0x475], succ=[0x6480x469, 0x8440x469]
    =================================
    0x61e0x469: v46961e(0xd) = CONST 
    0x6200x469: v469620 = SLOAD v46961e(0xd)
    0x6210x469: v469621(0x40) = CONST 
    0x6230x469: v469623 = MLOAD v469621(0x40)
    0x6240x469: v469624(0x0) = CONST 
    0x6290x469: v469629(0x1) = CONST 
    0x62b0x469: v46962b(0xa0) = CONST 
    0x62d0x469: v46962d(0x2) = CONST 
    0x62f0x469: v46962f(0x10000000000000000000000000000000000000000) = EXP v46962d(0x2), v46962b(0xa0)
    0x6300x469: v469630(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46962f(0x10000000000000000000000000000000000000000), v469629(0x1)
    0x6330x469: v469633 = AND v469620, v469630(0xffffffffffffffffffffffffffffffffffffffff)
    0x6350x469: v469635 = CALLDATASIZE 
    0x6380x469: CALLDATACOPY v469623, v469624(0x0), v469635
    0x6390x469: v469639(0x40) = CONST 
    0x63c0x469: v46963c = CALLDATASIZE 
    0x63f0x469: v46963f = GAS 
    0x6400x469: v469640 = DELEGATECALL v46963f, v469633, v469623, v46963c, v469623, v469639(0x40)
    0x6430x469: v469643 = ISZERO v469640
    0x6440x469: v469644(0x844) = CONST 
    0x6470x469: JUMPI v469644(0x844), v469643

    Begin block 0x6480x469
    prev=[0x61d0x469], succ=[]
    =================================
    0x6480x469: v469648(0x40) = CONST 
    0x64b0x469: RETURN v469623, v469648(0x40)

    Begin block 0x8440x469
    prev=[0x61d0x469], succ=[]
    =================================
    0x8450x469: v469845(0x0) = CONST 
    0x8480x469: REVERT v469845(0x0), v469845(0x0)

}

function privateSale1Hardcap()() public {
    Begin block 0x481
    prev=[], succ=[0x489, 0x48d]
    =================================
    0x482: v482 = CALLVALUE 
    0x484: v484 = ISZERO v482
    0x485: v485(0x48d) = CONST 
    0x488: JUMPI v485(0x48d), v484

    Begin block 0x489
    prev=[0x481], succ=[]
    =================================
    0x489: v489(0x0) = CONST 
    0x48c: REVERT v489(0x0), v489(0x0)

    Begin block 0x48d
    prev=[0x481], succ=[0x76e]
    =================================
    0x48f: v48f(0xbf4) = CONST 
    0x492: v492(0x76e) = CONST 
    0x495: JUMP v492(0x76e)

    Begin block 0x76e
    prev=[0x48d], succ=[0xbf4]
    =================================
    0x76f: v76f(0x7) = CONST 
    0x771: v771 = SLOAD v76f(0x7)
    0x773: JUMP v48f(0xbf4)

    Begin block 0xbf4
    prev=[0x76e], succ=[]
    =================================
    0xbf5: vbf5(0x40) = CONST 
    0xbf8: vbf8 = MLOAD vbf5(0x40)
    0xbfb: MSTORE vbf8, v771
    0xbfc: vbfc = MLOAD vbf5(0x40)
    0xc00: vc00(0x0) = SUB vbf8, vbfc
    0xc01: vc01(0x20) = CONST 
    0xc03: vc03(0x20) = ADD vc01(0x20), vc00(0x0)
    0xc05: RETURN vbfc, vc03(0x20)

}

function vesting(address)() public {
    Begin block 0x496
    prev=[], succ=[0x49e, 0x4a2]
    =================================
    0x497: v497 = CALLVALUE 
    0x499: v499 = ISZERO v497
    0x49a: v49a(0x4a2) = CONST 
    0x49d: JUMPI v49a(0x4a2), v499

    Begin block 0x49e
    prev=[0x496], succ=[]
    =================================
    0x49e: v49e(0x0) = CONST 
    0x4a1: REVERT v49e(0x0), v49e(0x0)

    Begin block 0x4a2
    prev=[0x496], succ=[0x774]
    =================================
    0x4a4: v4a4(0x4b7) = CONST 
    0x4a7: v4a7(0x1) = CONST 
    0x4a9: v4a9(0xa0) = CONST 
    0x4ab: v4ab(0x2) = CONST 
    0x4ad: v4ad(0x10000000000000000000000000000000000000000) = EXP v4ab(0x2), v4a9(0xa0)
    0x4ae: v4ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ad(0x10000000000000000000000000000000000000000), v4a7(0x1)
    0x4af: v4af(0x4) = CONST 
    0x4b1: v4b1 = CALLDATALOAD v4af(0x4)
    0x4b2: v4b2 = AND v4b1, v4ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x4b3: v4b3(0x774) = CONST 
    0x4b6: JUMP v4b3(0x774)

    Begin block 0x774
    prev=[0x4a2], succ=[0x4b7]
    =================================
    0x775: v775(0x3) = CONST 
    0x777: v777(0x20) = CONST 
    0x77b: MSTORE v777(0x20), v775(0x3)
    0x77c: v77c(0x0) = CONST 
    0x780: MSTORE v77c(0x0), v4b2
    0x781: v781(0x40) = CONST 
    0x785: v785 = SHA3 v77c(0x0), v781(0x40)
    0x787: v787 = SLOAD v785
    0x788: v788(0x1) = CONST 
    0x78b: v78b = ADD v785, v788(0x1)
    0x78c: v78c = SLOAD v78b
    0x78d: v78d(0x2) = CONST 
    0x790: v790 = ADD v785, v78d(0x2)
    0x791: v791 = SLOAD v790
    0x795: v795 = ADD v775(0x3), v785
    0x796: v796 = SLOAD v795
    0x79c: JUMP v4a4(0x4b7)

    Begin block 0x4b7
    prev=[0x774], succ=[]
    =================================
    0x4b8: v4b8(0x40) = CONST 
    0x4bb: v4bb = MLOAD v4b8(0x40)
    0x4be: MSTORE v4bb, v787
    0x4bf: v4bf(0x20) = CONST 
    0x4c2: v4c2 = ADD v4bb, v4bf(0x20)
    0x4c6: MSTORE v4c2, v78c
    0x4c9: v4c9 = ADD v4b8(0x40), v4bb
    0x4cd: MSTORE v4c9, v791
    0x4ce: v4ce(0x60) = CONST 
    0x4d1: v4d1 = ADD v4bb, v4ce(0x60)
    0x4d2: MSTORE v4d1, v796
    0x4d3: v4d3 = MLOAD v4b8(0x40)
    0x4d7: v4d7(0x0) = SUB v4bb, v4d3
    0x4d8: v4d8(0x80) = CONST 
    0x4da: v4da(0x80) = ADD v4d8(0x80), v4d7(0x0)
    0x4dc: RETURN v4d3, v4da(0x80)

}

function transferRight(address)() public {
    Begin block 0x4dd
    prev=[], succ=[0x4e5, 0x4e9]
    =================================
    0x4de: v4de = CALLVALUE 
    0x4e0: v4e0 = ISZERO v4de
    0x4e1: v4e1(0x4e9) = CONST 
    0x4e4: JUMPI v4e1(0x4e9), v4e0

    Begin block 0x4e5
    prev=[0x4dd], succ=[]
    =================================
    0x4e5: v4e5(0x0) = CONST 
    0x4e8: REVERT v4e5(0x0), v4e5(0x0)

    Begin block 0x4e9
    prev=[0x4dd], succ=[0x79d]
    =================================
    0x4eb: v4eb(0xc25) = CONST 
    0x4ee: v4ee(0x1) = CONST 
    0x4f0: v4f0(0xa0) = CONST 
    0x4f2: v4f2(0x2) = CONST 
    0x4f4: v4f4(0x10000000000000000000000000000000000000000) = EXP v4f2(0x2), v4f0(0xa0)
    0x4f5: v4f5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f4(0x10000000000000000000000000000000000000000), v4ee(0x1)
    0x4f6: v4f6(0x4) = CONST 
    0x4f8: v4f8 = CALLDATALOAD v4f6(0x4)
    0x4f9: v4f9 = AND v4f8, v4f5(0xffffffffffffffffffffffffffffffffffffffff)
    0x4fa: v4fa(0x79d) = CONST 
    0x4fd: JUMP v4fa(0x79d)

    Begin block 0x79d
    prev=[0x4e9], succ=[0xc25]
    =================================
    0x79e: v79e(0x2) = CONST 
    0x7a0: v7a0(0x20) = CONST 
    0x7a2: MSTORE v7a0(0x20), v79e(0x2)
    0x7a3: v7a3(0x0) = CONST 
    0x7a7: MSTORE v7a3(0x0), v4f9
    0x7a8: v7a8(0x40) = CONST 
    0x7ab: v7ab = SHA3 v7a3(0x0), v7a8(0x40)
    0x7ac: v7ac = SLOAD v7ab
    0x7ad: v7ad(0xff) = CONST 
    0x7af: v7af = AND v7ad(0xff), v7ac
    0x7b1: JUMP v4eb(0xc25)

    Begin block 0xc25
    prev=[0x79d], succ=[]
    =================================
    0xc26: vc26(0x40) = CONST 
    0xc29: vc29 = MLOAD vc26(0x40)
    0xc2b: vc2b = ISZERO v7af
    0xc2c: vc2c = ISZERO vc2b
    0xc2e: MSTORE vc29, vc2c
    0xc2f: vc2f = MLOAD vc26(0x40)
    0xc33: vc33(0x0) = SUB vc29, vc2f
    0xc34: vc34(0x20) = CONST 
    0xc36: vc36(0x20) = ADD vc34(0x20), vc33(0x0)
    0xc38: RETURN vc2f, vc36(0x20)

}

function privateSale2Hardcap()() public {
    Begin block 0x4fe
    prev=[], succ=[0x506, 0x50a]
    =================================
    0x4ff: v4ff = CALLVALUE 
    0x501: v501 = ISZERO v4ff
    0x502: v502(0x50a) = CONST 
    0x505: JUMPI v502(0x50a), v501

    Begin block 0x506
    prev=[0x4fe], succ=[]
    =================================
    0x506: v506(0x0) = CONST 
    0x509: REVERT v506(0x0), v506(0x0)

    Begin block 0x50a
    prev=[0x4fe], succ=[0x7b2]
    =================================
    0x50c: v50c(0xc58) = CONST 
    0x50f: v50f(0x7b2) = CONST 
    0x512: JUMP v50f(0x7b2)

    Begin block 0x7b2
    prev=[0x50a], succ=[0xc58]
    =================================
    0x7b3: v7b3(0x8) = CONST 
    0x7b5: v7b5 = SLOAD v7b3(0x8)
    0x7b7: JUMP v50c(0xc58)

    Begin block 0xc58
    prev=[0x7b2], succ=[]
    =================================
    0xc59: vc59(0x40) = CONST 
    0xc5c: vc5c = MLOAD vc59(0x40)
    0xc5f: MSTORE vc5c, v7b5
    0xc60: vc60 = MLOAD vc59(0x40)
    0xc64: vc64(0x0) = SUB vc5c, vc60
    0xc65: vc65(0x20) = CONST 
    0xc67: vc67(0x20) = ADD vc65(0x20), vc64(0x0)
    0xc69: RETURN vc60, vc67(0x20)

}

function currentRate()() public {
    Begin block 0x513
    prev=[], succ=[0x51b, 0x51f]
    =================================
    0x514: v514 = CALLVALUE 
    0x516: v516 = ISZERO v514
    0x517: v517(0x51f) = CONST 
    0x51a: JUMPI v517(0x51f), v516

    Begin block 0x51b
    prev=[0x513], succ=[]
    =================================
    0x51b: v51b(0x0) = CONST 
    0x51e: REVERT v51b(0x0), v51b(0x0)

    Begin block 0x51f
    prev=[0x513], succ=[0x7b8]
    =================================
    0x521: v521(0xc89) = CONST 
    0x524: v524(0x7b8) = CONST 
    0x527: JUMP v524(0x7b8)

    Begin block 0x7b8
    prev=[0x51f], succ=[0xc89]
    =================================
    0x7b9: v7b9(0x5) = CONST 
    0x7bb: v7bb = SLOAD v7b9(0x5)
    0x7bd: JUMP v521(0xc89)

    Begin block 0xc89
    prev=[0x7b8], succ=[]
    =================================
    0xc8a: vc8a(0x40) = CONST 
    0xc8d: vc8d = MLOAD vc8a(0x40)
    0xc90: MSTORE vc8d, v7bb
    0xc91: vc91 = MLOAD vc8a(0x40)
    0xc95: vc95(0x0) = SUB vc8d, vc91
    0xc96: vc96(0x20) = CONST 
    0xc98: vc98(0x20) = ADD vc96(0x20), vc95(0x0)
    0xc9a: RETURN vc91, vc98(0x20)

}

function token()() public {
    Begin block 0x528
    prev=[], succ=[0x530, 0x534]
    =================================
    0x529: v529 = CALLVALUE 
    0x52b: v52b = ISZERO v529
    0x52c: v52c(0x534) = CONST 
    0x52f: JUMPI v52c(0x534), v52b

    Begin block 0x530
    prev=[0x528], succ=[]
    =================================
    0x530: v530(0x0) = CONST 
    0x533: REVERT v530(0x0), v530(0x0)

    Begin block 0x534
    prev=[0x528], succ=[0x7be]
    =================================
    0x536: v536(0xcba) = CONST 
    0x539: v539(0x7be) = CONST 
    0x53c: JUMP v539(0x7be)

    Begin block 0x7be
    prev=[0x534], succ=[0xcba]
    =================================
    0x7bf: v7bf(0xe) = CONST 
    0x7c1: v7c1 = SLOAD v7bf(0xe)
    0x7c2: v7c2(0x1) = CONST 
    0x7c4: v7c4(0xa0) = CONST 
    0x7c6: v7c6(0x2) = CONST 
    0x7c8: v7c8(0x10000000000000000000000000000000000000000) = EXP v7c6(0x2), v7c4(0xa0)
    0x7c9: v7c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c8(0x10000000000000000000000000000000000000000), v7c2(0x1)
    0x7ca: v7ca = AND v7c9(0xffffffffffffffffffffffffffffffffffffffff), v7c1
    0x7cc: JUMP v536(0xcba)

    Begin block 0xcba
    prev=[0x7be], succ=[]
    =================================
    0xcbb: vcbb(0x40) = CONST 
    0xcbe: vcbe = MLOAD vcbb(0x40)
    0xcbf: vcbf(0x1) = CONST 
    0xcc1: vcc1(0xa0) = CONST 
    0xcc3: vcc3(0x2) = CONST 
    0xcc5: vcc5(0x10000000000000000000000000000000000000000) = EXP vcc3(0x2), vcc1(0xa0)
    0xcc6: vcc6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcc5(0x10000000000000000000000000000000000000000), vcbf(0x1)
    0xcc9: vcc9 = AND v7ca, vcc6(0xffffffffffffffffffffffffffffffffffffffff)
    0xccb: MSTORE vcbe, vcc9
    0xccc: vccc = MLOAD vcbb(0x40)
    0xcd0: vcd0(0x0) = SUB vcbe, vccc
    0xcd1: vcd1(0x20) = CONST 
    0xcd3: vcd3(0x20) = ADD vcd1(0x20), vcd0(0x0)
    0xcd5: RETURN vccc, vcd3(0x20)

}

function claimVesting()() public {
    Begin block 0x53d
    prev=[], succ=[0x545, 0x549]
    =================================
    0x53e: v53e = CALLVALUE 
    0x540: v540 = ISZERO v53e
    0x541: v541(0x549) = CONST 
    0x544: JUMPI v541(0x549), v540

    Begin block 0x545
    prev=[0x53d], succ=[]
    =================================
    0x545: v545(0x0) = CONST 
    0x548: REVERT v545(0x0), v545(0x0)

    Begin block 0x549
    prev=[0x53d], succ=[0x54e0x53d]
    =================================
    0x54b: v54b(0xcf5) = CONST 

    Begin block 0x54e0x53d
    prev=[0x549], succ=[0x5750x53d, 0x8200x53d]
    =================================
    0x54f0x53d: v53d54f(0xd) = CONST 
    0x5510x53d: v53d551 = SLOAD v53d54f(0xd)
    0x5520x53d: v53d552(0x40) = CONST 
    0x5540x53d: v53d554 = MLOAD v53d552(0x40)
    0x5550x53d: v53d555(0x1) = CONST 
    0x5570x53d: v53d557(0xa0) = CONST 
    0x5590x53d: v53d559(0x2) = CONST 
    0x55b0x53d: v53d55b(0x10000000000000000000000000000000000000000) = EXP v53d559(0x2), v53d557(0xa0)
    0x55c0x53d: v53d55c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53d55b(0x10000000000000000000000000000000000000000), v53d555(0x1)
    0x55f0x53d: v53d55f = AND v53d551, v53d55c(0xffffffffffffffffffffffffffffffffffffffff)
    0x5610x53d: v53d561 = CALLDATASIZE 
    0x5620x53d: v53d562(0x0) = CONST 
    0x5650x53d: CALLDATACOPY v53d554, v53d562(0x0), v53d561
    0x5660x53d: v53d566(0x0) = CONST 
    0x5690x53d: v53d569 = CALLDATASIZE 
    0x56c0x53d: v53d56c = GAS 
    0x56d0x53d: v53d56d = DELEGATECALL v53d56c, v53d55f, v53d554, v53d569, v53d554, v53d566(0x0)
    0x5700x53d: v53d570 = ISZERO v53d56d
    0x5710x53d: v53d571(0x820) = CONST 
    0x5740x53d: JUMPI v53d571(0x820), v53d570

    Begin block 0x5750x53d
    prev=[0x54e0x53d], succ=[]
    =================================
    0x5750x53d: STOP 

    Begin block 0x8200x53d
    prev=[0x54e0x53d], succ=[]
    =================================
    0x8210x53d: v53d821(0x0) = CONST 
    0x8240x53d: REVERT v53d821(0x0), v53d821(0x0)

}

