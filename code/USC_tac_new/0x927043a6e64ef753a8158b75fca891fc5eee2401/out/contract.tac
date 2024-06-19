function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x896]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x882: v882(0x896) = CONST 
    0x883: JUMPI v882(0x896), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x899]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x4645a418) = CONST 
    0x3b: v3b = EQ v34, v35(0x4645a418)
    0x884: v884(0x899) = CONST 
    0x885: JUMPI v884(0x899), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x89c, 0x4b]
    =================================
    0x41: v41(0x4e71e0c8) = CONST 
    0x46: v46 = EQ v41(0x4e71e0c8), v34
    0x886: v886(0x89c) = CONST 
    0x887: JUMPI v886(0x89c), v46

    Begin block 0x89c
    prev=[0x40], succ=[]
    =================================
    0x89d: v89d(0xcb) = CONST 
    0x89e: CALLPRIVATE v89d(0xcb)

    Begin block 0x4b
    prev=[0x40], succ=[0x89f, 0x56]
    =================================
    0x4c: v4c(0x715018a6) = CONST 
    0x51: v51 = EQ v4c(0x715018a6), v34
    0x888: v888(0x89f) = CONST 
    0x889: JUMPI v888(0x89f), v51

    Begin block 0x89f
    prev=[0x4b], succ=[]
    =================================
    0x8a0: v8a0(0xe0) = CONST 
    0x8a1: CALLPRIVATE v8a0(0xe0)

    Begin block 0x56
    prev=[0x4b], succ=[0x8a2, 0x61]
    =================================
    0x57: v57(0x83197ef0) = CONST 
    0x5c: v5c = EQ v57(0x83197ef0), v34
    0x88a: v88a(0x8a2) = CONST 
    0x88b: JUMPI v88a(0x8a2), v5c

    Begin block 0x8a2
    prev=[0x56], succ=[]
    =================================
    0x8a3: v8a3(0xf5) = CONST 
    0x8a4: CALLPRIVATE v8a3(0xf5)

    Begin block 0x61
    prev=[0x56], succ=[0x8a5, 0x6c]
    =================================
    0x62: v62(0x86d5c5f9) = CONST 
    0x67: v67 = EQ v62(0x86d5c5f9), v34
    0x88c: v88c(0x8a5) = CONST 
    0x88d: JUMPI v88c(0x8a5), v67

    Begin block 0x8a5
    prev=[0x61], succ=[]
    =================================
    0x8a6: v8a6(0x10a) = CONST 
    0x8a7: CALLPRIVATE v8a6(0x10a)

    Begin block 0x6c
    prev=[0x61], succ=[0x8a8, 0x77]
    =================================
    0x6d: v6d(0x8da5cb5b) = CONST 
    0x72: v72 = EQ v6d(0x8da5cb5b), v34
    0x88e: v88e(0x8a8) = CONST 
    0x88f: JUMPI v88e(0x8a8), v72

    Begin block 0x8a8
    prev=[0x6c], succ=[]
    =================================
    0x8a9: v8a9(0x13b) = CONST 
    0x8aa: CALLPRIVATE v8a9(0x13b)

    Begin block 0x77
    prev=[0x6c], succ=[0x8ab, 0x82]
    =================================
    0x78: v78(0xe30c3978) = CONST 
    0x7d: v7d = EQ v78(0xe30c3978), v34
    0x890: v890(0x8ab) = CONST 
    0x891: JUMPI v890(0x8ab), v7d

    Begin block 0x8ab
    prev=[0x77], succ=[]
    =================================
    0x8ac: v8ac(0x150) = CONST 
    0x8ad: CALLPRIVATE v8ac(0x150)

    Begin block 0x82
    prev=[0x77], succ=[0x8ae, 0x8d]
    =================================
    0x83: v83(0xf2fde38b) = CONST 
    0x88: v88 = EQ v83(0xf2fde38b), v34
    0x892: v892(0x8ae) = CONST 
    0x893: JUMPI v892(0x8ae), v88

    Begin block 0x8ae
    prev=[0x82], succ=[]
    =================================
    0x8af: v8af(0x165) = CONST 
    0x8b0: CALLPRIVATE v8af(0x165)

    Begin block 0x8d
    prev=[0x82], succ=[0x896, 0x8b1]
    =================================
    0x8e: v8e(0xf5074f41) = CONST 
    0x93: v93 = EQ v8e(0xf5074f41), v34
    0x894: v894(0x8b1) = CONST 
    0x895: JUMPI v894(0x8b1), v93

    Begin block 0x896
    prev=[0x0, 0x8d], succ=[]
    =================================
    0x897: v897(0x98) = CONST 
    0x898: CALLPRIVATE v897(0x98)

    Begin block 0x8b1
    prev=[0x8d], succ=[]
    =================================
    0x8b2: v8b2(0x186) = CONST 
    0x8b3: CALLPRIVATE v8b2(0x186)

    Begin block 0x899
    prev=[0xd], succ=[]
    =================================
    0x89a: v89a(0xaa) = CONST 
    0x89b: CALLPRIVATE v89a(0xaa)

}

function getPassportLogicRegistry()() public {
    Begin block 0x10a
    prev=[], succ=[0x112, 0x116]
    =================================
    0x10b: v10b = CALLVALUE 
    0x10d: v10d = ISZERO v10b
    0x10e: v10e(0x116) = CONST 
    0x111: JUMPI v10e(0x116), v10d

    Begin block 0x112
    prev=[0x10a], succ=[]
    =================================
    0x112: v112(0x0) = CONST 
    0x115: REVERT v112(0x0), v112(0x0)

    Begin block 0x116
    prev=[0x10a], succ=[0x3e3B0x116]
    =================================
    0x118: v118(0x6bc) = CONST 
    0x11b: v11b(0x3e3) = CONST 
    0x11e: JUMP v11b(0x3e3)

    Begin block 0x3e3B0x116
    prev=[0x116], succ=[0x453B0x3e3B0x116]
    =================================
    0x3e4S0x116: v3e4V116(0x0) = CONST 
    0x3e6S0x116: v3e6V116(0x813) = CONST 
    0x3e9S0x116: v3e9V116(0x453) = CONST 
    0x3ecS0x116: JUMP v3e9V116(0x453)

    Begin block 0x453B0x3e3B0x116
    prev=[0x3e3B0x116], succ=[0x813B0x116]
    =================================
    0x454S0x3e3S0x116: v454V3e3V116(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a) = CONST 
    0x475S0x3e3S0x116: v475V3e3V116 = SLOAD v454V3e3V116(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a)
    0x477S0x3e3S0x116: JUMP v3e6V116(0x813)

    Begin block 0x813B0x116
    prev=[0x453B0x3e3B0x116], succ=[0x6bc]
    =================================
    0x817S0x116: JUMP v118(0x6bc)

    Begin block 0x6bc
    prev=[0x813B0x116], succ=[]
    =================================
    0x6bd: v6bd(0x40) = CONST 
    0x6c0: v6c0 = MLOAD v6bd(0x40)
    0x6c1: v6c1(0x1) = CONST 
    0x6c3: v6c3(0xa0) = CONST 
    0x6c5: v6c5(0x2) = CONST 
    0x6c7: v6c7(0x10000000000000000000000000000000000000000) = EXP v6c5(0x2), v6c3(0xa0)
    0x6c8: v6c8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c7(0x10000000000000000000000000000000000000000), v6c1(0x1)
    0x6cb: v6cb = AND v475V3e3V116, v6c8(0xffffffffffffffffffffffffffffffffffffffff)
    0x6cd: MSTORE v6c0, v6cb
    0x6ce: v6ce = MLOAD v6bd(0x40)
    0x6d2: v6d2(0x0) = SUB v6c0, v6ce
    0x6d3: v6d3(0x20) = CONST 
    0x6d5: v6d5(0x20) = ADD v6d3(0x20), v6d2(0x0)
    0x6d7: RETURN v6ce, v6d5(0x20)

}

function owner()() public {
    Begin block 0x13b
    prev=[], succ=[0x143, 0x147]
    =================================
    0x13c: v13c = CALLVALUE 
    0x13e: v13e = ISZERO v13c
    0x13f: v13f(0x147) = CONST 
    0x142: JUMPI v13f(0x147), v13e

    Begin block 0x143
    prev=[0x13b], succ=[]
    =================================
    0x143: v143(0x0) = CONST 
    0x146: REVERT v143(0x0), v143(0x0)

    Begin block 0x147
    prev=[0x13b], succ=[0x3f2B0x147]
    =================================
    0x149: v149(0x6f7) = CONST 
    0x14c: v14c(0x3f2) = CONST 
    0x14f: JUMP v14c(0x3f2)

    Begin block 0x3f2B0x147
    prev=[0x147], succ=[0x478B0x3f2B0x147]
    =================================
    0x3f3S0x147: v3f3V147(0x0) = CONST 
    0x3f5S0x147: v3f5V147(0x837) = CONST 
    0x3f8S0x147: v3f8V147(0x478) = CONST 
    0x3fbS0x147: JUMP v3f8V147(0x478)

    Begin block 0x478B0x3f2B0x147
    prev=[0x3f2B0x147], succ=[0x837B0x147]
    =================================
    0x479S0x3f2S0x147: v479V3f2V147(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x3f2S0x147: v49aV3f2V147 = SLOAD v479V3f2V147(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x3f2S0x147: JUMP v3f5V147(0x837)

    Begin block 0x837B0x147
    prev=[0x478B0x3f2B0x147], succ=[0x6f7]
    =================================
    0x83bS0x147: JUMP v149(0x6f7)

    Begin block 0x6f7
    prev=[0x837B0x147], succ=[]
    =================================
    0x6f8: v6f8(0x40) = CONST 
    0x6fb: v6fb = MLOAD v6f8(0x40)
    0x6fc: v6fc(0x1) = CONST 
    0x6fe: v6fe(0xa0) = CONST 
    0x700: v700(0x2) = CONST 
    0x702: v702(0x10000000000000000000000000000000000000000) = EXP v700(0x2), v6fe(0xa0)
    0x703: v703(0xffffffffffffffffffffffffffffffffffffffff) = SUB v702(0x10000000000000000000000000000000000000000), v6fc(0x1)
    0x706: v706 = AND v49aV3f2V147, v703(0xffffffffffffffffffffffffffffffffffffffff)
    0x708: MSTORE v6fb, v706
    0x709: v709 = MLOAD v6f8(0x40)
    0x70d: v70d(0x0) = SUB v6fb, v709
    0x70e: v70e(0x20) = CONST 
    0x710: v710(0x20) = ADD v70e(0x20), v70d(0x0)
    0x712: RETURN v709, v710(0x20)

}

function pendingOwner()() public {
    Begin block 0x150
    prev=[], succ=[0x158, 0x15c]
    =================================
    0x151: v151 = CALLVALUE 
    0x153: v153 = ISZERO v151
    0x154: v154(0x15c) = CONST 
    0x157: JUMPI v154(0x15c), v153

    Begin block 0x158
    prev=[0x150], succ=[]
    =================================
    0x158: v158(0x0) = CONST 
    0x15b: REVERT v158(0x0), v158(0x0)

    Begin block 0x15c
    prev=[0x150], succ=[0x3fcB0x15c]
    =================================
    0x15e: v15e(0x732) = CONST 
    0x161: v161(0x3fc) = CONST 
    0x164: JUMP v161(0x3fc)

    Begin block 0x3fcB0x15c
    prev=[0x15c], succ=[0x561B0x3fcB0x15c]
    =================================
    0x3fdS0x15c: v3fdV15c(0x0) = CONST 
    0x3ffS0x15c: v3ffV15c(0x85b) = CONST 
    0x402S0x15c: v402V15c(0x561) = CONST 
    0x405S0x15c: JUMP v402V15c(0x561)

    Begin block 0x561B0x3fcB0x15c
    prev=[0x3fcB0x15c], succ=[0x85bB0x15c]
    =================================
    0x562S0x3fcS0x15c: v562V3fcV15c(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x583S0x3fcS0x15c: v583V3fcV15c = SLOAD v562V3fcV15c(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52)
    0x585S0x3fcS0x15c: JUMP v3ffV15c(0x85b)

    Begin block 0x85bB0x15c
    prev=[0x561B0x3fcB0x15c], succ=[0x732]
    =================================
    0x85fS0x15c: JUMP v15e(0x732)

    Begin block 0x732
    prev=[0x85bB0x15c], succ=[]
    =================================
    0x733: v733(0x40) = CONST 
    0x736: v736 = MLOAD v733(0x40)
    0x737: v737(0x1) = CONST 
    0x739: v739(0xa0) = CONST 
    0x73b: v73b(0x2) = CONST 
    0x73d: v73d(0x10000000000000000000000000000000000000000) = EXP v73b(0x2), v739(0xa0)
    0x73e: v73e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v73d(0x10000000000000000000000000000000000000000), v737(0x1)
    0x741: v741 = AND v583V3fcV15c, v73e(0xffffffffffffffffffffffffffffffffffffffff)
    0x743: MSTORE v736, v741
    0x744: v744 = MLOAD v733(0x40)
    0x748: v748(0x0) = SUB v736, v744
    0x749: v749(0x20) = CONST 
    0x74b: v74b(0x20) = ADD v749(0x20), v748(0x0)
    0x74d: RETURN v744, v74b(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x165
    prev=[], succ=[0x16d, 0x171]
    =================================
    0x166: v166 = CALLVALUE 
    0x168: v168 = ISZERO v166
    0x169: v169(0x171) = CONST 
    0x16c: JUMPI v169(0x171), v168

    Begin block 0x16d
    prev=[0x165], succ=[]
    =================================
    0x16d: v16d(0x0) = CONST 
    0x170: REVERT v16d(0x0), v16d(0x0)

    Begin block 0x171
    prev=[0x165], succ=[0x406B0x171]
    =================================
    0x173: v173(0x76d) = CONST 
    0x176: v176(0x1) = CONST 
    0x178: v178(0xa0) = CONST 
    0x17a: v17a(0x2) = CONST 
    0x17c: v17c(0x10000000000000000000000000000000000000000) = EXP v17a(0x2), v178(0xa0)
    0x17d: v17d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17c(0x10000000000000000000000000000000000000000), v176(0x1)
    0x17e: v17e(0x4) = CONST 
    0x180: v180 = CALLDATALOAD v17e(0x4)
    0x181: v181 = AND v180, v17d(0xffffffffffffffffffffffffffffffffffffffff)
    0x182: v182(0x406) = CONST 
    0x185: JUMP v182(0x406), v181, v173(0x76d)

    Begin block 0x406B0x171
    prev=[0x171], succ=[0x478B0x406B0x171]
    =================================
    0x407S0x171: v407V171(0x40e) = CONST 
    0x40aS0x171: v40aV171(0x478) = CONST 
    0x40dS0x171: JUMP v40aV171(0x478)

    Begin block 0x478B0x406B0x171
    prev=[0x406B0x171], succ=[0x40eB0x171]
    =================================
    0x479S0x406S0x171: v479V406V171(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x406S0x171: v49aV406V171 = SLOAD v479V406V171(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x406S0x171: JUMP v407V171(0x40e)

    Begin block 0x40eB0x171
    prev=[0x478B0x406B0x171], succ=[0x41eB0x171, 0x422B0x171]
    =================================
    0x40fS0x171: v40fV171(0x1) = CONST 
    0x411S0x171: v411V171(0xa0) = CONST 
    0x413S0x171: v413V171(0x2) = CONST 
    0x415S0x171: v415V171(0x10000000000000000000000000000000000000000) = EXP v413V171(0x2), v411V171(0xa0)
    0x416S0x171: v416V171(0xffffffffffffffffffffffffffffffffffffffff) = SUB v415V171(0x10000000000000000000000000000000000000000), v40fV171(0x1)
    0x417S0x171: v417V171 = AND v416V171(0xffffffffffffffffffffffffffffffffffffffff), v49aV406V171
    0x418S0x171: v418V171 = CALLER 
    0x419S0x171: v419V171 = EQ v418V171, v417V171
    0x41aS0x171: v41aV171(0x422) = CONST 
    0x41dS0x171: JUMPI v41aV171(0x422), v419V171

    Begin block 0x41eB0x171
    prev=[0x40eB0x171], succ=[]
    =================================
    0x41eS0x171: v41eV171(0x0) = CONST 
    0x421S0x171: REVERT v41eV171(0x0), v41eV171(0x0)

    Begin block 0x422B0x171
    prev=[0x40eB0x171], succ=[0x5aaB0x422B0x171]
    =================================
    0x423S0x171: v423V171(0x87f) = CONST 
    0x427S0x171: v427V171(0x5aa) = CONST 
    0x42aS0x171: JUMP v427V171(0x5aa), v181, v423V171(0x87f)

    Begin block 0x5aaB0x422B0x171
    prev=[0x422B0x171], succ=[0x87fB0x171]
    =================================
    0x5abS0x422S0x171: v5abV422V171(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x5ccS0x422S0x171: SSTORE v5abV422V171(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52), v181
    0x5cdS0x422S0x171: JUMP v423V171(0x87f)

    Begin block 0x87fB0x171
    prev=[0x5aaB0x422B0x171], succ=[0x76d]
    =================================
    0x881S0x171: JUMP v173(0x76d)

    Begin block 0x76d
    prev=[0x87fB0x171], succ=[]
    =================================
    0x76e: STOP 

}

function destroyAndSend(address)() public {
    Begin block 0x186
    prev=[], succ=[0x18e, 0x192]
    =================================
    0x187: v187 = CALLVALUE 
    0x189: v189 = ISZERO v187
    0x18a: v18a(0x192) = CONST 
    0x18d: JUMPI v18a(0x192), v189

    Begin block 0x18e
    prev=[0x186], succ=[]
    =================================
    0x18e: v18e(0x0) = CONST 
    0x191: REVERT v18e(0x0), v18e(0x0)

    Begin block 0x192
    prev=[0x186], succ=[0x42b]
    =================================
    0x194: v194(0x78e) = CONST 
    0x197: v197(0x1) = CONST 
    0x199: v199(0xa0) = CONST 
    0x19b: v19b(0x2) = CONST 
    0x19d: v19d(0x10000000000000000000000000000000000000000) = EXP v19b(0x2), v199(0xa0)
    0x19e: v19e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19d(0x10000000000000000000000000000000000000000), v197(0x1)
    0x19f: v19f(0x4) = CONST 
    0x1a1: v1a1 = CALLDATALOAD v19f(0x4)
    0x1a2: v1a2 = AND v1a1, v19e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a3: v1a3(0x42b) = CONST 
    0x1a6: JUMP v1a3(0x42b)

    Begin block 0x42b
    prev=[0x192], succ=[0x478B0x42b]
    =================================
    0x42c: v42c(0x433) = CONST 
    0x42f: v42f(0x478) = CONST 
    0x432: JUMP v42f(0x478)

    Begin block 0x478B0x42b
    prev=[0x42b], succ=[0x433]
    =================================
    0x479S0x42b: v479V42b(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x42b: v49aV42b = SLOAD v479V42b(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x42b: JUMP v42c(0x433)

    Begin block 0x433
    prev=[0x478B0x42b], succ=[0x443, 0x447]
    =================================
    0x434: v434(0x1) = CONST 
    0x436: v436(0xa0) = CONST 
    0x438: v438(0x2) = CONST 
    0x43a: v43a(0x10000000000000000000000000000000000000000) = EXP v438(0x2), v436(0xa0)
    0x43b: v43b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43a(0x10000000000000000000000000000000000000000), v434(0x1)
    0x43c: v43c = AND v43b(0xffffffffffffffffffffffffffffffffffffffff), v49aV42b
    0x43d: v43d = CALLER 
    0x43e: v43e = EQ v43d, v43c
    0x43f: v43f(0x447) = CONST 
    0x442: JUMPI v43f(0x447), v43e

    Begin block 0x443
    prev=[0x433], succ=[]
    =================================
    0x443: v443(0x0) = CONST 
    0x446: REVERT v443(0x0), v443(0x0)

    Begin block 0x447
    prev=[0x433], succ=[]
    =================================
    0x449: v449(0x1) = CONST 
    0x44b: v44b(0xa0) = CONST 
    0x44d: v44d(0x2) = CONST 
    0x44f: v44f(0x10000000000000000000000000000000000000000) = EXP v44d(0x2), v44b(0xa0)
    0x450: v450(0xffffffffffffffffffffffffffffffffffffffff) = SUB v44f(0x10000000000000000000000000000000000000000), v449(0x1)
    0x451: v451 = AND v450(0xffffffffffffffffffffffffffffffffffffffff), v1a2
    0x452: SELFDESTRUCT v451

}

function fallback()() public {
    Begin block 0x98
    prev=[], succ=[0x1a7]
    =================================
    0x99: v99(0x617) = CONST 
    0x9c: v9c(0xa3) = CONST 
    0x9f: v9f(0x1a7) = CONST 
    0xa2: JUMP v9f(0x1a7)

    Begin block 0x1a7
    prev=[0x98], succ=[0x453B0x1a7]
    =================================
    0x1a8: v1a8(0x0) = CONST 
    0x1aa: v1aa(0x1b1) = CONST 
    0x1ad: v1ad(0x453) = CONST 
    0x1b0: JUMP v1ad(0x453)

    Begin block 0x453B0x1a7
    prev=[0x1a7], succ=[0x1b1]
    =================================
    0x454S0x1a7: v454V1a7(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a) = CONST 
    0x475S0x1a7: v475V1a7 = SLOAD v454V1a7(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a)
    0x477S0x1a7: JUMP v1aa(0x1b1)

    Begin block 0x1b1
    prev=[0x453B0x1a7], succ=[0x203, 0x207]
    =================================
    0x1b2: v1b2(0x1) = CONST 
    0x1b4: v1b4(0xa0) = CONST 
    0x1b6: v1b6(0x2) = CONST 
    0x1b8: v1b8(0x10000000000000000000000000000000000000000) = EXP v1b6(0x2), v1b4(0xa0)
    0x1b9: v1b9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b8(0x10000000000000000000000000000000000000000), v1b2(0x1)
    0x1ba: v1ba = AND v1b9(0xffffffffffffffffffffffffffffffffffffffff), v475V1a7
    0x1bb: v1bb(0x609725ef) = CONST 
    0x1c0: v1c0(0x40) = CONST 
    0x1c2: v1c2 = MLOAD v1c0(0x40)
    0x1c4: v1c4(0xffffffff) = CONST 
    0x1c9: v1c9(0x609725ef) = AND v1c4(0xffffffff), v1bb(0x609725ef)
    0x1ca: v1ca(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e8: v1e8(0x609725ef00000000000000000000000000000000000000000000000000000000) = MUL v1ca(0x100000000000000000000000000000000000000000000000000000000), v1c9(0x609725ef)
    0x1ea: MSTORE v1c2, v1e8(0x609725ef00000000000000000000000000000000000000000000000000000000)
    0x1eb: v1eb(0x4) = CONST 
    0x1ed: v1ed = ADD v1eb(0x4), v1c2
    0x1ee: v1ee(0x20) = CONST 
    0x1f0: v1f0(0x40) = CONST 
    0x1f2: v1f2 = MLOAD v1f0(0x40)
    0x1f5: v1f5(0x4) = SUB v1ed, v1f2
    0x1f7: v1f7(0x0) = CONST 
    0x1fb: v1fb = EXTCODESIZE v1ba
    0x1fc: v1fc = ISZERO v1fb
    0x1fe: v1fe = ISZERO v1fc
    0x1ff: v1ff(0x207) = CONST 
    0x202: JUMPI v1ff(0x207), v1fe

    Begin block 0x203
    prev=[0x1b1], succ=[]
    =================================
    0x203: v203(0x0) = CONST 
    0x206: REVERT v203(0x0), v203(0x0)

    Begin block 0x207
    prev=[0x1b1], succ=[0x212, 0x21b]
    =================================
    0x209: v209 = GAS 
    0x20a: v20a = CALL v209, v1ba, v1f7(0x0), v1f2, v1f5(0x4), v1f2, v1ee(0x20)
    0x20b: v20b = ISZERO v20a
    0x20d: v20d = ISZERO v20b
    0x20e: v20e(0x21b) = CONST 
    0x211: JUMPI v20e(0x21b), v20d

    Begin block 0x212
    prev=[0x207], succ=[]
    =================================
    0x212: v212 = RETURNDATASIZE 
    0x213: v213(0x0) = CONST 
    0x216: RETURNDATACOPY v213(0x0), v213(0x0), v212
    0x217: v217 = RETURNDATASIZE 
    0x218: v218(0x0) = CONST 
    0x21a: REVERT v218(0x0), v217

    Begin block 0x21b
    prev=[0x207], succ=[0x22d, 0x231]
    =================================
    0x220: v220(0x40) = CONST 
    0x222: v222 = MLOAD v220(0x40)
    0x223: v223 = RETURNDATASIZE 
    0x224: v224(0x20) = CONST 
    0x227: v227 = LT v223, v224(0x20)
    0x228: v228 = ISZERO v227
    0x229: v229(0x231) = CONST 
    0x22c: JUMPI v229(0x231), v228

    Begin block 0x22d
    prev=[0x21b], succ=[]
    =================================
    0x22d: v22d(0x0) = CONST 
    0x230: REVERT v22d(0x0), v22d(0x0)

    Begin block 0x231
    prev=[0x21b], succ=[0xa3]
    =================================
    0x233: v233 = MLOAD v222
    0x237: JUMP v9c(0xa3)

    Begin block 0xa3
    prev=[0x231], succ=[0x238]
    =================================
    0xa4: va4(0x238) = CONST 
    0xa7: JUMP va4(0x238)

    Begin block 0x238
    prev=[0xa3], succ=[0x253, 0x257]
    =================================
    0x239: v239 = CALLDATASIZE 
    0x23a: v23a(0x0) = CONST 
    0x23d: CALLDATACOPY v23a(0x0), v23a(0x0), v239
    0x23e: v23e(0x0) = CONST 
    0x241: v241 = CALLDATASIZE 
    0x242: v242(0x0) = CONST 
    0x245: v245 = GAS 
    0x246: v246 = DELEGATECALL v245, v233, v242(0x0), v241, v23e(0x0), v23e(0x0)
    0x247: v247 = RETURNDATASIZE 
    0x248: v248(0x0) = CONST 
    0x24b: RETURNDATACOPY v248(0x0), v248(0x0), v247
    0x24e: v24e = ISZERO v246
    0x24f: v24f(0x257) = CONST 
    0x252: JUMPI v24f(0x257), v24e

    Begin block 0x253
    prev=[0x238], succ=[]
    =================================
    0x253: v253 = RETURNDATASIZE 
    0x254: v254(0x0) = CONST 
    0x256: RETURN v254(0x0), v253

    Begin block 0x257
    prev=[0x238], succ=[]
    =================================
    0x258: v258 = RETURNDATASIZE 
    0x259: v259(0x0) = CONST 
    0x25b: REVERT v259(0x0), v258

}

function changePassportLogicRegistry(address)() public {
    Begin block 0xaa
    prev=[], succ=[0xb2, 0xb6]
    =================================
    0xab: vab = CALLVALUE 
    0xad: vad = ISZERO vab
    0xae: vae(0xb6) = CONST 
    0xb1: JUMPI vae(0xb6), vad

    Begin block 0xb2
    prev=[0xaa], succ=[]
    =================================
    0xb2: vb2(0x0) = CONST 
    0xb5: REVERT vb2(0x0), vb2(0x0)

    Begin block 0xb6
    prev=[0xaa], succ=[0x25cB0xb6]
    =================================
    0xb8: vb8(0x638) = CONST 
    0xbb: vbb(0x1) = CONST 
    0xbd: vbd(0xa0) = CONST 
    0xbf: vbf(0x2) = CONST 
    0xc1: vc1(0x10000000000000000000000000000000000000000) = EXP vbf(0x2), vbd(0xa0)
    0xc2: vc2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc1(0x10000000000000000000000000000000000000000), vbb(0x1)
    0xc3: vc3(0x4) = CONST 
    0xc5: vc5 = CALLDATALOAD vc3(0x4)
    0xc6: vc6 = AND vc5, vc2(0xffffffffffffffffffffffffffffffffffffffff)
    0xc7: vc7(0x25c) = CONST 
    0xca: JUMP vc7(0x25c), vc6, vb8(0x638)

    Begin block 0x25cB0xb6
    prev=[0xb6], succ=[0x478B0x25cB0xb6]
    =================================
    0x25dS0xb6: v25dVb6(0x264) = CONST 
    0x260S0xb6: v260Vb6(0x478) = CONST 
    0x263S0xb6: JUMP v260Vb6(0x478)

    Begin block 0x478B0x25cB0xb6
    prev=[0x25cB0xb6], succ=[0x264B0xb6]
    =================================
    0x479S0x25cS0xb6: v479V25cVb6(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x25cS0xb6: v49aV25cVb6 = SLOAD v479V25cVb6(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x25cS0xb6: JUMP v25dVb6(0x264)

    Begin block 0x264B0xb6
    prev=[0x478B0x25cB0xb6], succ=[0x274B0xb6, 0x278B0xb6]
    =================================
    0x265S0xb6: v265Vb6(0x1) = CONST 
    0x267S0xb6: v267Vb6(0xa0) = CONST 
    0x269S0xb6: v269Vb6(0x2) = CONST 
    0x26bS0xb6: v26bVb6(0x10000000000000000000000000000000000000000) = EXP v269Vb6(0x2), v267Vb6(0xa0)
    0x26cS0xb6: v26cVb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26bVb6(0x10000000000000000000000000000000000000000), v265Vb6(0x1)
    0x26dS0xb6: v26dVb6 = AND v26cVb6(0xffffffffffffffffffffffffffffffffffffffff), v49aV25cVb6
    0x26eS0xb6: v26eVb6 = CALLER 
    0x26fS0xb6: v26fVb6 = EQ v26eVb6, v26dVb6
    0x270S0xb6: v270Vb6(0x278) = CONST 
    0x273S0xb6: JUMPI v270Vb6(0x278), v26fVb6

    Begin block 0x274B0xb6
    prev=[0x264B0xb6], succ=[]
    =================================
    0x274S0xb6: v274Vb6(0x0) = CONST 
    0x277S0xb6: REVERT v274Vb6(0x0), v274Vb6(0x0)

    Begin block 0x278B0xb6
    prev=[0x264B0xb6], succ=[0x453B0x278B0xb6]
    =================================
    0x27aS0xb6: v27aVb6(0x1) = CONST 
    0x27cS0xb6: v27cVb6(0xa0) = CONST 
    0x27eS0xb6: v27eVb6(0x2) = CONST 
    0x280S0xb6: v280Vb6(0x10000000000000000000000000000000000000000) = EXP v27eVb6(0x2), v27cVb6(0xa0)
    0x281S0xb6: v281Vb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v280Vb6(0x10000000000000000000000000000000000000000), v27aVb6(0x1)
    0x282S0xb6: v282Vb6 = AND v281Vb6(0xffffffffffffffffffffffffffffffffffffffff), vc6
    0x283S0xb6: v283Vb6(0x28a) = CONST 
    0x286S0xb6: v286Vb6(0x453) = CONST 
    0x289S0xb6: JUMP v286Vb6(0x453)

    Begin block 0x453B0x278B0xb6
    prev=[0x278B0xb6], succ=[0x28aB0xb6]
    =================================
    0x454S0x278S0xb6: v454V278Vb6(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a) = CONST 
    0x475S0x278S0xb6: v475V278Vb6 = SLOAD v454V278Vb6(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a)
    0x477S0x278S0xb6: JUMP v283Vb6(0x28a)

    Begin block 0x28aB0xb6
    prev=[0x453B0x278B0xb6], succ=[0x49dB0xb6]
    =================================
    0x28bS0xb6: v28bVb6(0x1) = CONST 
    0x28dS0xb6: v28dVb6(0xa0) = CONST 
    0x28fS0xb6: v28fVb6(0x2) = CONST 
    0x291S0xb6: v291Vb6(0x10000000000000000000000000000000000000000) = EXP v28fVb6(0x2), v28dVb6(0xa0)
    0x292S0xb6: v292Vb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v291Vb6(0x10000000000000000000000000000000000000000), v28bVb6(0x1)
    0x293S0xb6: v293Vb6 = AND v292Vb6(0xffffffffffffffffffffffffffffffffffffffff), v475V278Vb6
    0x294S0xb6: v294Vb6(0x5c2abfd67230c0e47d6de28402bfe206c7a57283cba891416ed657fd70a714c2) = CONST 
    0x2b5S0xb6: v2b5Vb6(0x40) = CONST 
    0x2b7S0xb6: v2b7Vb6 = MLOAD v2b5Vb6(0x40)
    0x2b8S0xb6: v2b8Vb6(0x40) = CONST 
    0x2baS0xb6: v2baVb6 = MLOAD v2b8Vb6(0x40)
    0x2bdS0xb6: v2bdVb6(0x0) = SUB v2b7Vb6, v2baVb6
    0x2bfS0xb6: LOG3 v2baVb6, v2bdVb6(0x0), v294Vb6(0x5c2abfd67230c0e47d6de28402bfe206c7a57283cba891416ed657fd70a714c2), v293Vb6, v282Vb6
    0x2c0S0xb6: v2c0Vb6(0x7af) = CONST 
    0x2c4S0xb6: v2c4Vb6(0x49d) = CONST 
    0x2c7S0xb6: JUMP v2c4Vb6(0x49d)

    Begin block 0x49dB0xb6
    prev=[0x28aB0xb6], succ=[0x4b0B0xb6, 0x53cB0xb6]
    =================================
    0x49eS0xb6: v49eVb6(0x0) = CONST 
    0x4a0S0xb6: v4a0Vb6(0x1) = CONST 
    0x4a2S0xb6: v4a2Vb6(0xa0) = CONST 
    0x4a4S0xb6: v4a4Vb6(0x2) = CONST 
    0x4a6S0xb6: v4a6Vb6(0x10000000000000000000000000000000000000000) = EXP v4a4Vb6(0x2), v4a2Vb6(0xa0)
    0x4a7S0xb6: v4a7Vb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a6Vb6(0x10000000000000000000000000000000000000000), v4a0Vb6(0x1)
    0x4a9S0xb6: v4a9Vb6 = AND vc6, v4a7Vb6(0xffffffffffffffffffffffffffffffffffffffff)
    0x4aaS0xb6: v4aaVb6 = ISZERO v4a9Vb6
    0x4abS0xb6: v4abVb6 = ISZERO v4aaVb6
    0x4acS0xb6: v4acVb6(0x53c) = CONST 
    0x4afS0xb6: JUMPI v4acVb6(0x53c), v4abVb6

    Begin block 0x4b0B0xb6
    prev=[0x49dB0xb6], succ=[]
    =================================
    0x4b0S0xb6: v4b0Vb6(0x40) = CONST 
    0x4b3S0xb6: v4b3Vb6 = MLOAD v4b0Vb6(0x40)
    0x4b4S0xb6: v4b4Vb6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4d6S0xb6: MSTORE v4b3Vb6, v4b4Vb6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4d7S0xb6: v4d7Vb6(0x20) = CONST 
    0x4d9S0xb6: v4d9Vb6(0x4) = CONST 
    0x4dcS0xb6: v4dcVb6 = ADD v4b3Vb6, v4d9Vb6(0x4)
    0x4ddS0xb6: MSTORE v4dcVb6, v4d7Vb6(0x20)
    0x4deS0xb6: v4deVb6(0x25) = CONST 
    0x4e0S0xb6: v4e0Vb6(0x24) = CONST 
    0x4e3S0xb6: v4e3Vb6 = ADD v4b3Vb6, v4e0Vb6(0x24)
    0x4e4S0xb6: MSTORE v4e3Vb6, v4deVb6(0x25)
    0x4e5S0xb6: v4e5Vb6(0x43616e6e6f742073657420726567697374727920746f2061207a65726f206164) = CONST 
    0x506S0xb6: v506Vb6(0x44) = CONST 
    0x509S0xb6: v509Vb6 = ADD v4b3Vb6, v506Vb6(0x44)
    0x50aS0xb6: MSTORE v509Vb6, v4e5Vb6(0x43616e6e6f742073657420726567697374727920746f2061207a65726f206164)
    0x50bS0xb6: v50bVb6(0x6472657373000000000000000000000000000000000000000000000000000000) = CONST 
    0x52cS0xb6: v52cVb6(0x64) = CONST 
    0x52fS0xb6: v52fVb6 = ADD v4b3Vb6, v52cVb6(0x64)
    0x530S0xb6: MSTORE v52fVb6, v50bVb6(0x6472657373000000000000000000000000000000000000000000000000000000)
    0x532S0xb6: v532Vb6 = MLOAD v4b0Vb6(0x40)
    0x536S0xb6: v536Vb6(0x0) = SUB v4b3Vb6, v532Vb6
    0x537S0xb6: v537Vb6(0x84) = CONST 
    0x539S0xb6: v539Vb6(0x84) = ADD v537Vb6(0x84), v536Vb6(0x0)
    0x53bS0xb6: REVERT v532Vb6, v539Vb6(0x84)

    Begin block 0x53cB0xb6
    prev=[0x49dB0xb6], succ=[0x7afB0xb6]
    =================================
    0x53eS0xb6: v53eVb6(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a) = CONST 
    0x55fS0xb6: SSTORE v53eVb6(0xa04bab69e45aeb4c94a78ba5bc1be67ef28977c4fdf815a30b829a794eb67a4a), vc6
    0x560S0xb6: JUMP v2c0Vb6(0x7af)

    Begin block 0x7afB0xb6
    prev=[0x53cB0xb6], succ=[0x638]
    =================================
    0x7b1S0xb6: JUMP vb8(0x638)

    Begin block 0x638
    prev=[0x7afB0xb6], succ=[]
    =================================
    0x639: STOP 

}

function claimOwnership()() public {
    Begin block 0xcb
    prev=[], succ=[0xd3, 0xd7]
    =================================
    0xcc: vcc = CALLVALUE 
    0xce: vce = ISZERO vcc
    0xcf: vcf(0xd7) = CONST 
    0xd2: JUMPI vcf(0xd7), vce

    Begin block 0xd3
    prev=[0xcb], succ=[]
    =================================
    0xd3: vd3(0x0) = CONST 
    0xd6: REVERT vd3(0x0), vd3(0x0)

    Begin block 0xd7
    prev=[0xcb], succ=[0x2cbB0xd7]
    =================================
    0xd9: vd9(0x659) = CONST 
    0xdc: vdc(0x2cb) = CONST 
    0xdf: JUMP vdc(0x2cb), vd9(0x659)

    Begin block 0x2cbB0xd7
    prev=[0xd7], succ=[0x561B0x2cbB0xd7]
    =================================
    0x2ccS0xd7: v2ccVd7(0x2d3) = CONST 
    0x2cfS0xd7: v2cfVd7(0x561) = CONST 
    0x2d2S0xd7: JUMP v2cfVd7(0x561)

    Begin block 0x561B0x2cbB0xd7
    prev=[0x2cbB0xd7], succ=[0x2d3B0xd7]
    =================================
    0x562S0x2cbS0xd7: v562V2cbVd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x583S0x2cbS0xd7: v583V2cbVd7 = SLOAD v562V2cbVd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52)
    0x585S0x2cbS0xd7: JUMP v2ccVd7(0x2d3)

    Begin block 0x2d3B0xd7
    prev=[0x561B0x2cbB0xd7], succ=[0x2e3B0xd7, 0x2e7B0xd7]
    =================================
    0x2d4S0xd7: v2d4Vd7(0x1) = CONST 
    0x2d6S0xd7: v2d6Vd7(0xa0) = CONST 
    0x2d8S0xd7: v2d8Vd7(0x2) = CONST 
    0x2daS0xd7: v2daVd7(0x10000000000000000000000000000000000000000) = EXP v2d8Vd7(0x2), v2d6Vd7(0xa0)
    0x2dbS0xd7: v2dbVd7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2daVd7(0x10000000000000000000000000000000000000000), v2d4Vd7(0x1)
    0x2dcS0xd7: v2dcVd7 = AND v2dbVd7(0xffffffffffffffffffffffffffffffffffffffff), v583V2cbVd7
    0x2ddS0xd7: v2ddVd7 = CALLER 
    0x2deS0xd7: v2deVd7 = EQ v2ddVd7, v2dcVd7
    0x2dfS0xd7: v2dfVd7(0x2e7) = CONST 
    0x2e2S0xd7: JUMPI v2dfVd7(0x2e7), v2deVd7

    Begin block 0x2e3B0xd7
    prev=[0x2d3B0xd7], succ=[]
    =================================
    0x2e3S0xd7: v2e3Vd7(0x0) = CONST 
    0x2e6S0xd7: REVERT v2e3Vd7(0x0), v2e3Vd7(0x0)

    Begin block 0x2e7B0xd7
    prev=[0x2d3B0xd7], succ=[0x561B0x2e7B0xd7]
    =================================
    0x2e8S0xd7: v2e8Vd7(0x2ef) = CONST 
    0x2ebS0xd7: v2ebVd7(0x561) = CONST 
    0x2eeS0xd7: JUMP v2ebVd7(0x561)

    Begin block 0x561B0x2e7B0xd7
    prev=[0x2e7B0xd7], succ=[0x2efB0xd7]
    =================================
    0x562S0x2e7S0xd7: v562V2e7Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x583S0x2e7S0xd7: v583V2e7Vd7 = SLOAD v562V2e7Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52)
    0x585S0x2e7S0xd7: JUMP v2e8Vd7(0x2ef)

    Begin block 0x2efB0xd7
    prev=[0x561B0x2e7B0xd7], succ=[0x478B0x2efB0xd7]
    =================================
    0x2f0S0xd7: v2f0Vd7(0x1) = CONST 
    0x2f2S0xd7: v2f2Vd7(0xa0) = CONST 
    0x2f4S0xd7: v2f4Vd7(0x2) = CONST 
    0x2f6S0xd7: v2f6Vd7(0x10000000000000000000000000000000000000000) = EXP v2f4Vd7(0x2), v2f2Vd7(0xa0)
    0x2f7S0xd7: v2f7Vd7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f6Vd7(0x10000000000000000000000000000000000000000), v2f0Vd7(0x1)
    0x2f8S0xd7: v2f8Vd7 = AND v2f7Vd7(0xffffffffffffffffffffffffffffffffffffffff), v583V2e7Vd7
    0x2f9S0xd7: v2f9Vd7(0x300) = CONST 
    0x2fcS0xd7: v2fcVd7(0x478) = CONST 
    0x2ffS0xd7: JUMP v2fcVd7(0x478)

    Begin block 0x478B0x2efB0xd7
    prev=[0x2efB0xd7], succ=[0x300B0xd7]
    =================================
    0x479S0x2efS0xd7: v479V2efVd7(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x2efS0xd7: v49aV2efVd7 = SLOAD v479V2efVd7(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x2efS0xd7: JUMP v2f9Vd7(0x300)

    Begin block 0x300B0xd7
    prev=[0x478B0x2efB0xd7], succ=[0x561B0x300B0xd7]
    =================================
    0x301S0xd7: v301Vd7(0x1) = CONST 
    0x303S0xd7: v303Vd7(0xa0) = CONST 
    0x305S0xd7: v305Vd7(0x2) = CONST 
    0x307S0xd7: v307Vd7(0x10000000000000000000000000000000000000000) = EXP v305Vd7(0x2), v303Vd7(0xa0)
    0x308S0xd7: v308Vd7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v307Vd7(0x10000000000000000000000000000000000000000), v301Vd7(0x1)
    0x309S0xd7: v309Vd7 = AND v308Vd7(0xffffffffffffffffffffffffffffffffffffffff), v49aV2efVd7
    0x30aS0xd7: v30aVd7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x32bS0xd7: v32bVd7(0x40) = CONST 
    0x32dS0xd7: v32dVd7 = MLOAD v32bVd7(0x40)
    0x32eS0xd7: v32eVd7(0x40) = CONST 
    0x330S0xd7: v330Vd7 = MLOAD v32eVd7(0x40)
    0x333S0xd7: v333Vd7(0x0) = SUB v32dVd7, v330Vd7
    0x335S0xd7: LOG3 v330Vd7, v333Vd7(0x0), v30aVd7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v309Vd7, v2f8Vd7
    0x336S0xd7: v336Vd7(0x345) = CONST 
    0x339S0xd7: v339Vd7(0x340) = CONST 
    0x33cS0xd7: v33cVd7(0x561) = CONST 
    0x33fS0xd7: JUMP v33cVd7(0x561)

    Begin block 0x561B0x300B0xd7
    prev=[0x300B0xd7], succ=[0x340B0xd7]
    =================================
    0x562S0x300S0xd7: v562V300Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x583S0x300S0xd7: v583V300Vd7 = SLOAD v562V300Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52)
    0x585S0x300S0xd7: JUMP v339Vd7(0x340)

    Begin block 0x340B0xd7
    prev=[0x561B0x300B0xd7], succ=[0x586B0x340B0xd7]
    =================================
    0x341S0xd7: v341Vd7(0x586) = CONST 
    0x344S0xd7: JUMP v341Vd7(0x586), v583V300Vd7, v336Vd7(0x345)

    Begin block 0x586B0x340B0xd7
    prev=[0x340B0xd7], succ=[0x345B0xd7]
    =================================
    0x587S0x340S0xd7: v587V340Vd7(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x5a8S0x340S0xd7: SSTORE v587V340Vd7(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22), v583V300Vd7
    0x5a9S0x340S0xd7: JUMP v336Vd7(0x345)

    Begin block 0x345B0xd7
    prev=[0x586B0x340B0xd7], succ=[0x5aaB0x345B0xd7]
    =================================
    0x346S0xd7: v346Vd7(0x7d1) = CONST 
    0x349S0xd7: v349Vd7(0x0) = CONST 
    0x34bS0xd7: v34bVd7(0x5aa) = CONST 
    0x34eS0xd7: JUMP v34bVd7(0x5aa), v349Vd7(0x0), v346Vd7(0x7d1)

    Begin block 0x5aaB0x345B0xd7
    prev=[0x345B0xd7], succ=[0x7d1B0xd7]
    =================================
    0x5abS0x345S0xd7: v5abV345Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x5ccS0x345S0xd7: SSTORE v5abV345Vd7(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52), v349Vd7(0x0)
    0x5cdS0x345S0xd7: JUMP v346Vd7(0x7d1)

    Begin block 0x7d1B0xd7
    prev=[0x5aaB0x345B0xd7], succ=[0x659]
    =================================
    0x7d2S0xd7: JUMP vd9(0x659)

    Begin block 0x659
    prev=[0x7d1B0xd7], succ=[]
    =================================
    0x65a: STOP 

}

function renounceOwnership()() public {
    Begin block 0xe0
    prev=[], succ=[0xe8, 0xec]
    =================================
    0xe1: ve1 = CALLVALUE 
    0xe3: ve3 = ISZERO ve1
    0xe4: ve4(0xec) = CONST 
    0xe7: JUMPI ve4(0xec), ve3

    Begin block 0xe8
    prev=[0xe0], succ=[]
    =================================
    0xe8: ve8(0x0) = CONST 
    0xeb: REVERT ve8(0x0), ve8(0x0)

    Begin block 0xec
    prev=[0xe0], succ=[0x351B0xec]
    =================================
    0xee: vee(0x67a) = CONST 
    0xf1: vf1(0x351) = CONST 
    0xf4: JUMP vf1(0x351), vee(0x67a)

    Begin block 0x351B0xec
    prev=[0xec], succ=[0x478B0x351B0xec]
    =================================
    0x352S0xec: v352Vec(0x359) = CONST 
    0x355S0xec: v355Vec(0x478) = CONST 
    0x358S0xec: JUMP v355Vec(0x478)

    Begin block 0x478B0x351B0xec
    prev=[0x351B0xec], succ=[0x359B0xec]
    =================================
    0x479S0x351S0xec: v479V351Vec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x351S0xec: v49aV351Vec = SLOAD v479V351Vec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x351S0xec: JUMP v352Vec(0x359)

    Begin block 0x359B0xec
    prev=[0x478B0x351B0xec], succ=[0x369B0xec, 0x36dB0xec]
    =================================
    0x35aS0xec: v35aVec(0x1) = CONST 
    0x35cS0xec: v35cVec(0xa0) = CONST 
    0x35eS0xec: v35eVec(0x2) = CONST 
    0x360S0xec: v360Vec(0x10000000000000000000000000000000000000000) = EXP v35eVec(0x2), v35cVec(0xa0)
    0x361S0xec: v361Vec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v360Vec(0x10000000000000000000000000000000000000000), v35aVec(0x1)
    0x362S0xec: v362Vec = AND v361Vec(0xffffffffffffffffffffffffffffffffffffffff), v49aV351Vec
    0x363S0xec: v363Vec = CALLER 
    0x364S0xec: v364Vec = EQ v363Vec, v362Vec
    0x365S0xec: v365Vec(0x36d) = CONST 
    0x368S0xec: JUMPI v365Vec(0x36d), v364Vec

    Begin block 0x369B0xec
    prev=[0x359B0xec], succ=[]
    =================================
    0x369S0xec: v369Vec(0x0) = CONST 
    0x36cS0xec: REVERT v369Vec(0x0), v369Vec(0x0)

    Begin block 0x36dB0xec
    prev=[0x359B0xec], succ=[0x478B0x36dB0xec]
    =================================
    0x36eS0xec: v36eVec(0x375) = CONST 
    0x371S0xec: v371Vec(0x478) = CONST 
    0x374S0xec: JUMP v371Vec(0x478)

    Begin block 0x478B0x36dB0xec
    prev=[0x36dB0xec], succ=[0x375B0xec]
    =================================
    0x479S0x36dS0xec: v479V36dVec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x36dS0xec: v49aV36dVec = SLOAD v479V36dVec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x36dS0xec: JUMP v36eVec(0x375)

    Begin block 0x375B0xec
    prev=[0x478B0x36dB0xec], succ=[0x586B0x375B0xec]
    =================================
    0x376S0xec: v376Vec(0x1) = CONST 
    0x378S0xec: v378Vec(0xa0) = CONST 
    0x37aS0xec: v37aVec(0x2) = CONST 
    0x37cS0xec: v37cVec(0x10000000000000000000000000000000000000000) = EXP v37aVec(0x2), v378Vec(0xa0)
    0x37dS0xec: v37dVec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37cVec(0x10000000000000000000000000000000000000000), v376Vec(0x1)
    0x37eS0xec: v37eVec = AND v37dVec(0xffffffffffffffffffffffffffffffffffffffff), v49aV36dVec
    0x37fS0xec: v37fVec(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820) = CONST 
    0x3a0S0xec: v3a0Vec(0x40) = CONST 
    0x3a2S0xec: v3a2Vec = MLOAD v3a0Vec(0x40)
    0x3a3S0xec: v3a3Vec(0x40) = CONST 
    0x3a5S0xec: v3a5Vec = MLOAD v3a3Vec(0x40)
    0x3a8S0xec: v3a8Vec(0x0) = SUB v3a2Vec, v3a5Vec
    0x3aaS0xec: LOG2 v3a5Vec, v3a8Vec(0x0), v37fVec(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820), v37eVec
    0x3abS0xec: v3abVec(0x7f2) = CONST 
    0x3aeS0xec: v3aeVec(0x0) = CONST 
    0x3b0S0xec: v3b0Vec(0x586) = CONST 
    0x3b3S0xec: JUMP v3b0Vec(0x586), v3aeVec(0x0), v3abVec(0x7f2)

    Begin block 0x586B0x375B0xec
    prev=[0x375B0xec], succ=[0x7f2B0xec]
    =================================
    0x587S0x375S0xec: v587V375Vec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x5a8S0x375S0xec: SSTORE v587V375Vec(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22), v3aeVec(0x0)
    0x5a9S0x375S0xec: JUMP v3abVec(0x7f2)

    Begin block 0x7f2B0xec
    prev=[0x586B0x375B0xec], succ=[0x67a]
    =================================
    0x7f3S0xec: JUMP vee(0x67a)

    Begin block 0x67a
    prev=[0x7f2B0xec], succ=[]
    =================================
    0x67b: STOP 

}

function destroy()() public {
    Begin block 0xf5
    prev=[], succ=[0xfd, 0x101]
    =================================
    0xf6: vf6 = CALLVALUE 
    0xf8: vf8 = ISZERO vf6
    0xf9: vf9(0x101) = CONST 
    0xfc: JUMPI vf9(0x101), vf8

    Begin block 0xfd
    prev=[0xf5], succ=[]
    =================================
    0xfd: vfd(0x0) = CONST 
    0x100: REVERT vfd(0x0), vfd(0x0)

    Begin block 0x101
    prev=[0xf5], succ=[0x3b4]
    =================================
    0x103: v103(0x69b) = CONST 
    0x106: v106(0x3b4) = CONST 
    0x109: JUMP v106(0x3b4)

    Begin block 0x3b4
    prev=[0x101], succ=[0x478B0x3b4]
    =================================
    0x3b5: v3b5(0x3bc) = CONST 
    0x3b8: v3b8(0x478) = CONST 
    0x3bb: JUMP v3b8(0x478)

    Begin block 0x478B0x3b4
    prev=[0x3b4], succ=[0x3bc]
    =================================
    0x479S0x3b4: v479V3b4(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x3b4: v49aV3b4 = SLOAD v479V3b4(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x3b4: JUMP v3b5(0x3bc)

    Begin block 0x3bc
    prev=[0x478B0x3b4], succ=[0x3cc, 0x3d0]
    =================================
    0x3bd: v3bd(0x1) = CONST 
    0x3bf: v3bf(0xa0) = CONST 
    0x3c1: v3c1(0x2) = CONST 
    0x3c3: v3c3(0x10000000000000000000000000000000000000000) = EXP v3c1(0x2), v3bf(0xa0)
    0x3c4: v3c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c3(0x10000000000000000000000000000000000000000), v3bd(0x1)
    0x3c5: v3c5 = AND v3c4(0xffffffffffffffffffffffffffffffffffffffff), v49aV3b4
    0x3c6: v3c6 = CALLER 
    0x3c7: v3c7 = EQ v3c6, v3c5
    0x3c8: v3c8(0x3d0) = CONST 
    0x3cb: JUMPI v3c8(0x3d0), v3c7

    Begin block 0x3cc
    prev=[0x3bc], succ=[]
    =================================
    0x3cc: v3cc(0x0) = CONST 
    0x3cf: REVERT v3cc(0x0), v3cc(0x0)

    Begin block 0x3d0
    prev=[0x3bc], succ=[0x478B0x3d0]
    =================================
    0x3d1: v3d1(0x3d8) = CONST 
    0x3d4: v3d4(0x478) = CONST 
    0x3d7: JUMP v3d4(0x478)

    Begin block 0x478B0x3d0
    prev=[0x3d0], succ=[0x3d8]
    =================================
    0x479S0x3d0: v479V3d0(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0x49aS0x3d0: v49aV3d0 = SLOAD v479V3d0(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22)
    0x49cS0x3d0: JUMP v3d1(0x3d8)

    Begin block 0x3d8
    prev=[0x478B0x3d0], succ=[]
    =================================
    0x3d9: v3d9(0x1) = CONST 
    0x3db: v3db(0xa0) = CONST 
    0x3dd: v3dd(0x2) = CONST 
    0x3df: v3df(0x10000000000000000000000000000000000000000) = EXP v3dd(0x2), v3db(0xa0)
    0x3e0: v3e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3df(0x10000000000000000000000000000000000000000), v3d9(0x1)
    0x3e1: v3e1 = AND v3e0(0xffffffffffffffffffffffffffffffffffffffff), v49aV3d0
    0x3e2: SELFDESTRUCT v3e1

}

