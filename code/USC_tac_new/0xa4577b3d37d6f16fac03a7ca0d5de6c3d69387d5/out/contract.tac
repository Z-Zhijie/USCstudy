function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xc, 0x10]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5 = CALLVALUE 
    0x7: v7 = ISZERO v5
    0x8: v8(0x10) = CONST 
    0xb: JUMPI v8(0x10), v7

    Begin block 0xc
    prev=[0x0], succ=[]
    =================================
    0xc: vc(0x0) = CONST 
    0xf: REVERT vc(0x0), vc(0x0)

    Begin block 0x10
    prev=[0x0], succ=[0x1a, 0x3029]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x2faf: v2faf(0x3029) = CONST 
    0x2fb0: JUMPI v2faf(0x3029), v15

    Begin block 0x1a
    prev=[0x10], succ=[0xc3, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x70c2f239) = CONST 
    0x26: v26 = GT v21(0x70c2f239), v1f
    0x27: v27(0xc3) = CONST 
    0x2a: JUMPI v27(0xc3), v26

    Begin block 0xc3
    prev=[0x1a], succ=[0x115, 0xcf]
    =================================
    0xc5: vc5(0x3092afd5) = CONST 
    0xca: vca = GT vc5(0x3092afd5), v1f
    0xcb: vcb(0x115) = CONST 
    0xce: JUMPI vcb(0x115), vca

    Begin block 0x115
    prev=[0xc3], succ=[0x2fe1, 0x120]
    =================================
    0x117: v117(0xfdd58e) = CONST 
    0x11b: v11b = EQ v117(0xfdd58e), v1f
    0x2fd5: v2fd5(0x2fe1) = CONST 
    0x2fd6: JUMPI v2fd5(0x2fe1), v11b

    Begin block 0x2fe1
    prev=[0x115], succ=[]
    =================================
    0x2fe2: v2fe2(0x15c) = CONST 
    0x2fe3: CALLPRIVATE v2fe2(0x15c)

    Begin block 0x120
    prev=[0x115], succ=[0x2fe4, 0x12b]
    =================================
    0x121: v121(0x1ffc9a7) = CONST 
    0x126: v126 = EQ v121(0x1ffc9a7), v1f
    0x2fd7: v2fd7(0x2fe4) = CONST 
    0x2fd8: JUMPI v2fd7(0x2fe4), v126

    Begin block 0x2fe4
    prev=[0x120], succ=[]
    =================================
    0x2fe5: v2fe5(0x19a) = CONST 
    0x2fe6: CALLPRIVATE v2fe5(0x19a)

    Begin block 0x12b
    prev=[0x120], succ=[0x2fe7, 0x136]
    =================================
    0x12c: v12c(0x2fe5305) = CONST 
    0x131: v131 = EQ v12c(0x2fe5305), v1f
    0x2fd9: v2fd9(0x2fe7) = CONST 
    0x2fda: JUMPI v2fd9(0x2fe7), v131

    Begin block 0x2fe7
    prev=[0x12b], succ=[]
    =================================
    0x2fe8: v2fe8(0x1d5) = CONST 
    0x2fe9: CALLPRIVATE v2fe8(0x1d5)

    Begin block 0x136
    prev=[0x12b], succ=[0x2fea, 0x141]
    =================================
    0x137: v137(0xe89341c) = CONST 
    0x13c: v13c = EQ v137(0xe89341c), v1f
    0x2fdb: v2fdb(0x2fea) = CONST 
    0x2fdc: JUMPI v2fdb(0x2fea), v13c

    Begin block 0x2fea
    prev=[0x136], succ=[]
    =================================
    0x2feb: v2feb(0x27b) = CONST 
    0x2fec: CALLPRIVATE v2feb(0x27b)

    Begin block 0x141
    prev=[0x136], succ=[0x2fed, 0x14c]
    =================================
    0x142: v142(0x158ef93e) = CONST 
    0x147: v147 = EQ v142(0x158ef93e), v1f
    0x2fdd: v2fdd(0x2fed) = CONST 
    0x2fde: JUMPI v2fdd(0x2fed), v147

    Begin block 0x2fed
    prev=[0x141], succ=[]
    =================================
    0x2fee: v2fee(0x30d) = CONST 
    0x2fef: CALLPRIVATE v2fee(0x30d)

    Begin block 0x14c
    prev=[0x141], succ=[0x2ff0, 0x157]
    =================================
    0x14d: v14d(0x2eb2c2d6) = CONST 
    0x152: v152 = EQ v14d(0x2eb2c2d6), v1f
    0x2fdf: v2fdf(0x2ff0) = CONST 
    0x2fe0: JUMPI v2fdf(0x2ff0), v152

    Begin block 0x2ff0
    prev=[0x14c], succ=[]
    =================================
    0x2ff1: v2ff1(0x315) = CONST 
    0x2ff2: CALLPRIVATE v2ff1(0x315)

    Begin block 0x157
    prev=[0x14c], succ=[]
    =================================
    0x158: v158(0x0) = CONST 
    0x15b: REVERT v158(0x0), v158(0x0)

    Begin block 0xcf
    prev=[0xc3], succ=[0x2ff3, 0xda]
    =================================
    0xd0: vd0(0x3092afd5) = CONST 
    0xd5: vd5 = EQ vd0(0x3092afd5), v1f
    0x2fc9: v2fc9(0x2ff3) = CONST 
    0x2fca: JUMPI v2fc9(0x2ff3), vd5

    Begin block 0x2ff3
    prev=[0xcf], succ=[]
    =================================
    0x2ff4: v2ff4(0x4d6) = CONST 
    0x2ff5: CALLPRIVATE v2ff4(0x4d6)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x2ff6]
    =================================
    0xdb: vdb(0x40c10f19) = CONST 
    0xe0: ve0 = EQ vdb(0x40c10f19), v1f
    0x2fcb: v2fcb(0x2ff6) = CONST 
    0x2fcc: JUMPI v2fcb(0x2ff6), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0x2ff9, 0xf0]
    =================================
    0xe6: ve6(0x485cc955) = CONST 
    0xeb: veb = EQ ve6(0x485cc955), v1f
    0x2fcd: v2fcd(0x2ff9) = CONST 
    0x2fce: JUMPI v2fcd(0x2ff9), veb

    Begin block 0x2ff9
    prev=[0xe5], succ=[]
    =================================
    0x2ffa: v2ffa(0x528) = CONST 
    0x2ffb: CALLPRIVATE v2ffa(0x528)

    Begin block 0xf0
    prev=[0xe5], succ=[0x2ffc, 0xfb]
    =================================
    0xf1: vf1(0x4e1273f4) = CONST 
    0xf6: vf6 = EQ vf1(0x4e1273f4), v1f
    0x2fcf: v2fcf(0x2ffc) = CONST 
    0x2fd0: JUMPI v2fcf(0x2ffc), vf6

    Begin block 0x2ffc
    prev=[0xf0], succ=[]
    =================================
    0x2ffd: v2ffd(0x556) = CONST 
    0x2ffe: CALLPRIVATE v2ffd(0x556)

    Begin block 0xfb
    prev=[0xf0], succ=[0x2fff, 0x106]
    =================================
    0xfc: vfc(0x4fb2e45d) = CONST 
    0x101: v101 = EQ vfc(0x4fb2e45d), v1f
    0x2fd1: v2fd1(0x2fff) = CONST 
    0x2fd2: JUMPI v2fd1(0x2fff), v101

    Begin block 0x2fff
    prev=[0xfb], succ=[]
    =================================
    0x3000: v3000(0x6c9) = CONST 
    0x3001: CALLPRIVATE v3000(0x6c9)

    Begin block 0x106
    prev=[0xfb], succ=[0x111, 0x3002]
    =================================
    0x107: v107(0x6c0360eb) = CONST 
    0x10c: v10c = EQ v107(0x6c0360eb), v1f
    0x2fd3: v2fd3(0x3002) = CONST 
    0x2fd4: JUMPI v2fd3(0x3002), v10c

    Begin block 0x111
    prev=[0x106], succ=[0x2923]
    =================================
    0x111: v111(0x2923) = CONST 
    0x114: JUMP v111(0x2923)

    Begin block 0x2923
    prev=[0x111], succ=[]
    =================================
    0x2924: v2924(0x0) = CONST 
    0x2927: REVERT v2924(0x0), v2924(0x0)

    Begin block 0x3002
    prev=[0x106], succ=[]
    =================================
    0x3003: v3003(0x6ef) = CONST 
    0x3004: CALLPRIVATE v3003(0x6ef)

    Begin block 0x2ff6
    prev=[0xda], succ=[]
    =================================
    0x2ff7: v2ff7(0x4fc) = CONST 
    0x2ff8: CALLPRIVATE v2ff7(0x4fc)

    Begin block 0x2b
    prev=[0x1a], succ=[0x7c, 0x36]
    =================================
    0x2c: v2c(0xaa936a0d) = CONST 
    0x31: v31 = GT v2c(0xaa936a0d), v1f
    0x32: v32(0x7c) = CONST 
    0x35: JUMPI v32(0x7c), v31

    Begin block 0x7c
    prev=[0x2b], succ=[0x3005, 0x88]
    =================================
    0x7e: v7e(0x70c2f239) = CONST 
    0x83: v83 = EQ v7e(0x70c2f239), v1f
    0x2fbd: v2fbd(0x3005) = CONST 
    0x2fbe: JUMPI v2fbd(0x3005), v83

    Begin block 0x3005
    prev=[0x7c], succ=[]
    =================================
    0x3006: v3006(0x6f7) = CONST 
    0x3007: CALLPRIVATE v3006(0x6f7)

    Begin block 0x88
    prev=[0x7c], succ=[0x3008, 0x93]
    =================================
    0x89: v89(0x8da5cb5b) = CONST 
    0x8e: v8e = EQ v89(0x8da5cb5b), v1f
    0x2fbf: v2fbf(0x3008) = CONST 
    0x2fc0: JUMPI v2fbf(0x3008), v8e

    Begin block 0x3008
    prev=[0x88], succ=[]
    =================================
    0x3009: v3009(0x77a) = CONST 
    0x300a: CALLPRIVATE v3009(0x77a)

    Begin block 0x93
    prev=[0x88], succ=[0x300b, 0x9e]
    =================================
    0x94: v94(0x9204aac6) = CONST 
    0x99: v99 = EQ v94(0x9204aac6), v1f
    0x2fc1: v2fc1(0x300b) = CONST 
    0x2fc2: JUMPI v2fc1(0x300b), v99

    Begin block 0x300b
    prev=[0x93], succ=[]
    =================================
    0x300c: v300c(0x79e) = CONST 
    0x300d: CALLPRIVATE v300c(0x79e)

    Begin block 0x9e
    prev=[0x93], succ=[0x300e, 0xa9]
    =================================
    0x9f: v9f(0x983b2d56) = CONST 
    0xa4: va4 = EQ v9f(0x983b2d56), v1f
    0x2fc3: v2fc3(0x300e) = CONST 
    0x2fc4: JUMPI v2fc3(0x300e), va4

    Begin block 0x300e
    prev=[0x9e], succ=[]
    =================================
    0x300f: v300f(0x7a6) = CONST 
    0x3010: CALLPRIVATE v300f(0x7a6)

    Begin block 0xa9
    prev=[0x9e], succ=[0x3011, 0xb4]
    =================================
    0xaa: vaa(0x9dc29fac) = CONST 
    0xaf: vaf = EQ vaa(0x9dc29fac), v1f
    0x2fc5: v2fc5(0x3011) = CONST 
    0x2fc6: JUMPI v2fc5(0x3011), vaf

    Begin block 0x3011
    prev=[0xa9], succ=[]
    =================================
    0x3012: v3012(0x7cc) = CONST 
    0x3013: CALLPRIVATE v3012(0x7cc)

    Begin block 0xb4
    prev=[0xa9], succ=[0xbf, 0x3014]
    =================================
    0xb5: vb5(0xa22cb465) = CONST 
    0xba: vba = EQ vb5(0xa22cb465), v1f
    0x2fc7: v2fc7(0x3014) = CONST 
    0x2fc8: JUMPI v2fc7(0x3014), vba

    Begin block 0xbf
    prev=[0xb4], succ=[0x28ff]
    =================================
    0xbf: vbf(0x28ff) = CONST 
    0xc2: JUMP vbf(0x28ff)

    Begin block 0x28ff
    prev=[0xbf], succ=[]
    =================================
    0x2900: v2900(0x0) = CONST 
    0x2903: REVERT v2900(0x0), v2900(0x0)

    Begin block 0x3014
    prev=[0xb4], succ=[]
    =================================
    0x3015: v3015(0x7f8) = CONST 
    0x3016: CALLPRIVATE v3015(0x7f8)

    Begin block 0x36
    prev=[0x2b], succ=[0x3017, 0x41]
    =================================
    0x37: v37(0xaa936a0d) = CONST 
    0x3c: v3c = EQ v37(0xaa936a0d), v1f
    0x2fb1: v2fb1(0x3017) = CONST 
    0x2fb2: JUMPI v2fb1(0x3017), v3c

    Begin block 0x3017
    prev=[0x36], succ=[]
    =================================
    0x3018: v3018(0x826) = CONST 
    0x3019: CALLPRIVATE v3018(0x826)

    Begin block 0x41
    prev=[0x36], succ=[0x301a, 0x4c]
    =================================
    0x42: v42(0xb2dc5dc3) = CONST 
    0x47: v47 = EQ v42(0xb2dc5dc3), v1f
    0x2fb3: v2fb3(0x301a) = CONST 
    0x2fb4: JUMPI v2fb3(0x301a), v47

    Begin block 0x301a
    prev=[0x41], succ=[]
    =================================
    0x301b: v301b(0x84c) = CONST 
    0x301c: CALLPRIVATE v301b(0x84c)

    Begin block 0x4c
    prev=[0x41], succ=[0x301d, 0x57]
    =================================
    0x4d: v4d(0xc5b8f772) = CONST 
    0x52: v52 = EQ v4d(0xc5b8f772), v1f
    0x2fb5: v2fb5(0x301d) = CONST 
    0x2fb6: JUMPI v2fb5(0x301d), v52

    Begin block 0x301d
    prev=[0x4c], succ=[]
    =================================
    0x301e: v301e(0x8ca) = CONST 
    0x301f: CALLPRIVATE v301e(0x8ca)

    Begin block 0x57
    prev=[0x4c], succ=[0x62, 0x3020]
    =================================
    0x58: v58(0xe985e9c5) = CONST 
    0x5d: v5d = EQ v58(0xe985e9c5), v1f
    0x2fb7: v2fb7(0x3020) = CONST 
    0x2fb8: JUMPI v2fb7(0x3020), v5d

    Begin block 0x62
    prev=[0x57], succ=[0x3023, 0x6d]
    =================================
    0x63: v63(0xf242432a) = CONST 
    0x68: v68 = EQ v63(0xf242432a), v1f
    0x2fb9: v2fb9(0x3023) = CONST 
    0x2fba: JUMPI v2fb9(0x3023), v68

    Begin block 0x3023
    prev=[0x62], succ=[]
    =================================
    0x3024: v3024(0x924) = CONST 
    0x3025: CALLPRIVATE v3024(0x924)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x3026]
    =================================
    0x6e: v6e(0xf46eccc4) = CONST 
    0x73: v73 = EQ v6e(0xf46eccc4), v1f
    0x2fbb: v2fbb(0x3026) = CONST 
    0x2fbc: JUMPI v2fbb(0x3026), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x28db]
    =================================
    0x78: v78(0x28db) = CONST 
    0x7b: JUMP v78(0x28db)

    Begin block 0x28db
    prev=[0x78], succ=[]
    =================================
    0x28dc: v28dc(0x0) = CONST 
    0x28df: REVERT v28dc(0x0), v28dc(0x0)

    Begin block 0x3026
    prev=[0x6d], succ=[]
    =================================
    0x3027: v3027(0x9ed) = CONST 
    0x3028: CALLPRIVATE v3027(0x9ed)

    Begin block 0x3020
    prev=[0x57], succ=[]
    =================================
    0x3021: v3021(0x8f6) = CONST 
    0x3022: CALLPRIVATE v3021(0x8f6)

    Begin block 0x3029
    prev=[0x10], succ=[]
    =================================
    0x302a: v302a(0x28b7) = CONST 
    0x302b: CALLPRIVATE v302a(0x28b7)

}

function 0x12df(0x12dfarg0x0) private {
    Begin block 0x12df
    prev=[], succ=[0x2d65, 0x131c]
    =================================
    0x12e0: v12e0(0x2) = CONST 
    0x12e3: v12e3 = SLOAD v12e0(0x2)
    0x12e4: v12e4(0x40) = CONST 
    0x12e7: v12e7 = MLOAD v12e4(0x40)
    0x12e8: v12e8(0x20) = CONST 
    0x12ea: v12ea(0x1) = CONST 
    0x12ed: v12ed = AND v12e3, v12ea(0x1)
    0x12ee: v12ee = ISZERO v12ed
    0x12ef: v12ef(0x100) = CONST 
    0x12f2: v12f2 = MUL v12ef(0x100), v12ee
    0x12f3: v12f3(0x0) = CONST 
    0x12f5: v12f5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v12f3(0x0)
    0x12f6: v12f6 = ADD v12f5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v12f2
    0x12f9: v12f9 = AND v12e3, v12f6
    0x12fc: v12fc = DIV v12f9, v12e0(0x2)
    0x12fd: v12fd(0x1f) = CONST 
    0x1300: v1300 = ADD v12fc, v12fd(0x1f)
    0x1303: v1303 = DIV v1300, v12e8(0x20)
    0x1305: v1305 = MUL v12e8(0x20), v1303
    0x1307: v1307 = ADD v12e7, v1305
    0x1309: v1309 = ADD v12e8(0x20), v1307
    0x130c: MSTORE v12e4(0x40), v1309
    0x130f: MSTORE v12e7, v12fc
    0x1313: v1313 = ADD v12e7, v12e8(0x20)
    0x1317: v1317 = ISZERO v12fc
    0x1318: v1318(0x2d65) = CONST 
    0x131b: JUMPI v1318(0x2d65), v1317

    Begin block 0x2d65
    prev=[0x12df], succ=[]
    =================================
    0x2d6c: RETURNPRIVATE v12dfarg0, v12e7, v12dfarg0

    Begin block 0x131c
    prev=[0x12df], succ=[0x1324, 0x1337]
    =================================
    0x131d: v131d(0x1f) = CONST 
    0x131f: v131f = LT v131d(0x1f), v12fc
    0x1320: v1320(0x1337) = CONST 
    0x1323: JUMPI v1320(0x1337), v131f

    Begin block 0x1324
    prev=[0x131c], succ=[0x2d8c]
    =================================
    0x1324: v1324(0x100) = CONST 
    0x1329: v1329 = SLOAD v12e0(0x2)
    0x132a: v132a = DIV v1329, v1324(0x100)
    0x132b: v132b = MUL v132a, v1324(0x100)
    0x132d: MSTORE v1313, v132b
    0x132f: v132f(0x20) = CONST 
    0x1331: v1331 = ADD v132f(0x20), v1313
    0x1333: v1333(0x2d8c) = CONST 
    0x1336: JUMP v1333(0x2d8c)

    Begin block 0x2d8c
    prev=[0x1324], succ=[]
    =================================
    0x2d93: RETURNPRIVATE v12dfarg0, v12e7, v12dfarg0

    Begin block 0x1337
    prev=[0x131c], succ=[0x1345]
    =================================
    0x1339: v1339 = ADD v1313, v12fc
    0x133c: v133c(0x0) = CONST 
    0x133e: MSTORE v133c(0x0), v12e0(0x2)
    0x133f: v133f(0x20) = CONST 
    0x1341: v1341(0x0) = CONST 
    0x1343: v1343 = SHA3 v1341(0x0), v133f(0x20)

    Begin block 0x1345
    prev=[0x1337, 0x1345], succ=[0x1345, 0x1359]
    =================================
    0x1345_0x0: v1345_0 = PHI v1313, v1351
    0x1345_0x1: v1345_1 = PHI v1343, v134d
    0x1347: v1347 = SLOAD v1345_1
    0x1349: MSTORE v1345_0, v1347
    0x134b: v134b(0x1) = CONST 
    0x134d: v134d = ADD v134b(0x1), v1345_1
    0x134f: v134f(0x20) = CONST 
    0x1351: v1351 = ADD v134f(0x20), v1345_0
    0x1354: v1354 = GT v1339, v1351
    0x1355: v1355(0x1345) = CONST 
    0x1358: JUMPI v1355(0x1345), v1354

    Begin block 0x1359
    prev=[0x1345], succ=[0x1362]
    =================================
    0x135b: v135b = SUB v1351, v1339
    0x135c: v135c(0x1f) = CONST 
    0x135e: v135e = AND v135c(0x1f), v135b
    0x1360: v1360 = ADD v1339, v135e

    Begin block 0x1362
    prev=[0x1359], succ=[]
    =================================
    0x1369: RETURNPRIVATE v12dfarg0, v12e7, v12dfarg0

}

function balanceOf(address,uint256)() public {
    Begin block 0x15c
    prev=[], succ=[0x16e, 0x172]
    =================================
    0x15d: v15d(0x2947) = CONST 
    0x160: v160(0x4) = CONST 
    0x163: v163 = CALLDATASIZE 
    0x164: v164 = SUB v163, v160(0x4)
    0x165: v165(0x40) = CONST 
    0x168: v168 = LT v164, v165(0x40)
    0x169: v169 = ISZERO v168
    0x16a: v16a(0x172) = CONST 
    0x16d: JUMPI v16a(0x172), v169

    Begin block 0x16e
    prev=[0x15c], succ=[]
    =================================
    0x16e: v16e(0x0) = CONST 
    0x171: REVERT v16e(0x0), v16e(0x0)

    Begin block 0x172
    prev=[0x15c], succ=[0xa130x15c]
    =================================
    0x174: v174(0x1) = CONST 
    0x176: v176(0x1) = CONST 
    0x178: v178(0xa0) = CONST 
    0x17a: v17a(0x10000000000000000000000000000000000000000) = SHL v178(0xa0), v176(0x1)
    0x17b: v17b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17a(0x10000000000000000000000000000000000000000), v174(0x1)
    0x17d: v17d = CALLDATALOAD v160(0x4)
    0x17e: v17e = AND v17d, v17b(0xffffffffffffffffffffffffffffffffffffffff)
    0x180: v180(0x20) = CONST 
    0x182: v182(0x24) = ADD v180(0x20), v160(0x4)
    0x183: v183 = CALLDATALOAD v182(0x24)
    0x184: v184(0xa13) = CONST 
    0x187: JUMP v184(0xa13)

    Begin block 0xa130x15c
    prev=[0x172], succ=[0xa1f0x15c]
    =================================
    0xa140x15c: v15ca14(0x0) = CONST 
    0xa160x15c: v15ca16(0xa1f) = CONST 
    0xa1b0x15c: v15ca1b(0x192e) = CONST 
    0xa1e0x15c: v15ca1e_0 = CALLPRIVATE v15ca1b(0x192e), v183, v17e, v15ca16(0xa1f)

    Begin block 0xa1f0x15c
    prev=[0xa130x15c], succ=[0xa250x15c, 0xa2c0x15c]
    =================================
    0xa200x15c: v15ca20 = ISZERO v15ca1e_0
    0xa210x15c: v15ca21(0xa2c) = CONST 
    0xa240x15c: JUMPI v15ca21(0xa2c), v15ca20

    Begin block 0xa250x15c
    prev=[0xa1f0x15c], succ=[0x2c890x15c]
    =================================
    0xa260x15c: v15ca26(0x1) = CONST 
    0xa280x15c: v15ca28(0x2c89) = CONST 
    0xa2b0x15c: JUMP v15ca28(0x2c89)

    Begin block 0x2c890x15c
    prev=[0xa250x15c], succ=[0x2947]
    =================================
    0x2c8e0x15c: JUMP v15d(0x2947)

    Begin block 0x2947
    prev=[0xa300x15c, 0x2c890x15c], succ=[]
    =================================
    0x2947_0x0: v2947_0 = PHI v15ca2e(0x0), v15ca26(0x1)
    0x2948: v2948(0x40) = CONST 
    0x294b: v294b = MLOAD v2948(0x40)
    0x294e: MSTORE v294b, v2947_0
    0x294f: v294f = MLOAD v2948(0x40)
    0x2953: v2953(0x0) = SUB v294b, v294f
    0x2954: v2954(0x20) = CONST 
    0x2956: v2956(0x20) = ADD v2954(0x20), v2953(0x0)
    0x2958: RETURN v294f, v2956(0x20)

    Begin block 0xa2c0x15c
    prev=[0xa1f0x15c], succ=[0xa300x15c]
    =================================
    0xa2e0x15c: v15ca2e(0x0) = CONST 

    Begin block 0xa300x15c
    prev=[0xa2c0x15c], succ=[0x2947]
    =================================
    0xa350x15c: JUMP v15d(0x2947)

}

function 0x192e(0x192earg0x0, 0x192earg0x1, 0x192earg0x2) private {
    Begin block 0x192e
    prev=[], succ=[0x19460x192e, 0x193f0x192e]
    =================================
    0x192f: v192f(0x0) = CONST 
    0x1931: v1931(0x1) = CONST 
    0x1933: v1933(0x1) = CONST 
    0x1935: v1935(0xa0) = CONST 
    0x1937: v1937(0x10000000000000000000000000000000000000000) = SHL v1935(0xa0), v1933(0x1)
    0x1938: v1938(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1937(0x10000000000000000000000000000000000000000), v1931(0x1)
    0x193a: v193a = AND v192earg1, v1938(0xffffffffffffffffffffffffffffffffffffffff)
    0x193b: v193b(0x1946) = CONST 
    0x193e: JUMPI v193b(0x1946), v193a

    Begin block 0x19460x192e
    prev=[0x192e], succ=[0x2dfb0x192e]
    =================================
    0x19480x192e: v192e1948(0x0) = CONST 
    0x194c0x192e: MSTORE v192e1948(0x0), v192earg0
    0x194d0x192e: v192e194d(0x7) = CONST 
    0x194f0x192e: v192e194f(0x20) = CONST 
    0x19510x192e: MSTORE v192e194f(0x20), v192e194d(0x7)
    0x19520x192e: v192e1952(0x40) = CONST 
    0x19550x192e: v192e1955 = SHA3 v192e1948(0x0), v192e1952(0x40)
    0x19560x192e: v192e1956 = SLOAD v192e1955
    0x19570x192e: v192e1957(0x1) = CONST 
    0x19590x192e: v192e1959(0x1) = CONST 
    0x195b0x192e: v192e195b(0xa0) = CONST 
    0x195d0x192e: v192e195d(0x10000000000000000000000000000000000000000) = SHL v192e195b(0xa0), v192e1959(0x1)
    0x195e0x192e: v192e195e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v192e195d(0x10000000000000000000000000000000000000000), v192e1957(0x1)
    0x19610x192e: v192e1961 = AND v192e195e(0xffffffffffffffffffffffffffffffffffffffff), v192earg1
    0x19630x192e: v192e1963 = AND v192e1956, v192e195e(0xffffffffffffffffffffffffffffffffffffffff)
    0x19640x192e: v192e1964 = EQ v192e1963, v192e1961
    0x19650x192e: v192e1965(0x2dfb) = CONST 
    0x19680x192e: JUMP v192e1965(0x2dfb)

    Begin block 0x2dfb0x192e
    prev=[0x19460x192e], succ=[]
    =================================
    0x2e000x192e: RETURNPRIVATE v192earg2, v192e1964

    Begin block 0x193f0x192e
    prev=[0x192e], succ=[0x2dd60x192e]
    =================================
    0x19400x192e: v192e1940(0x0) = CONST 
    0x19420x192e: v192e1942(0x2dd6) = CONST 
    0x19450x192e: JUMP v192e1942(0x2dd6)

    Begin block 0x2dd60x192e
    prev=[0x193f0x192e], succ=[]
    =================================
    0x2ddb0x192e: RETURNPRIVATE v192earg2, v192e1940(0x0)

}

function supportsInterface(bytes4)() public {
    Begin block 0x19a
    prev=[], succ=[0x1ac, 0x1b0]
    =================================
    0x19b: v19b(0x2978) = CONST 
    0x19e: v19e(0x4) = CONST 
    0x1a1: v1a1 = CALLDATASIZE 
    0x1a2: v1a2 = SUB v1a1, v19e(0x4)
    0x1a3: v1a3(0x20) = CONST 
    0x1a6: v1a6 = LT v1a2, v1a3(0x20)
    0x1a7: v1a7 = ISZERO v1a6
    0x1a8: v1a8(0x1b0) = CONST 
    0x1ab: JUMPI v1a8(0x1b0), v1a7

    Begin block 0x1ac
    prev=[0x19a], succ=[]
    =================================
    0x1ac: v1ac(0x0) = CONST 
    0x1af: REVERT v1ac(0x0), v1ac(0x0)

    Begin block 0x1b0
    prev=[0x19a], succ=[0xa36]
    =================================
    0x1b2: v1b2 = CALLDATALOAD v19e(0x4)
    0x1b3: v1b3(0x1) = CONST 
    0x1b5: v1b5(0x1) = CONST 
    0x1b7: v1b7(0xe0) = CONST 
    0x1b9: v1b9(0x100000000000000000000000000000000000000000000000000000000) = SHL v1b7(0xe0), v1b5(0x1)
    0x1ba: v1ba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1b9(0x100000000000000000000000000000000000000000000000000000000), v1b3(0x1)
    0x1bb: v1bb(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1ba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1bc: v1bc = AND v1bb(0xffffffff00000000000000000000000000000000000000000000000000000000), v1b2
    0x1bd: v1bd(0xa36) = CONST 
    0x1c0: JUMP v1bd(0xa36)

    Begin block 0xa36
    prev=[0x1b0], succ=[0xa54]
    =================================
    0xa37: va37(0x1) = CONST 
    0xa39: va39(0x1) = CONST 
    0xa3b: va3b(0xe0) = CONST 
    0xa3d: va3d(0x100000000000000000000000000000000000000000000000000000000) = SHL va3b(0xe0), va39(0x1)
    0xa3e: va3e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB va3d(0x100000000000000000000000000000000000000000000000000000000), va37(0x1)
    0xa3f: va3f(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT va3e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xa41: va41 = AND v1bc, va3f(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0xa42: va42(0x0) = CONST 
    0xa46: MSTORE va42(0x0), va41
    0xa47: va47(0x20) = CONST 
    0xa4b: MSTORE va47(0x20), va42(0x0)
    0xa4c: va4c(0x40) = CONST 
    0xa4f: va4f = SHA3 va42(0x0), va4c(0x40)
    0xa50: va50 = SLOAD va4f
    0xa51: va51(0xff) = CONST 
    0xa53: va53 = AND va51(0xff), va50

    Begin block 0xa54
    prev=[0xa36], succ=[0x2978]
    =================================
    0xa58: JUMP v19b(0x2978)

    Begin block 0x2978
    prev=[0xa54], succ=[]
    =================================
    0x2979: v2979(0x40) = CONST 
    0x297c: v297c = MLOAD v2979(0x40)
    0x297e: v297e = ISZERO va53
    0x297f: v297f = ISZERO v297e
    0x2981: MSTORE v297c, v297f
    0x2982: v2982 = MLOAD v2979(0x40)
    0x2986: v2986(0x0) = SUB v297c, v2982
    0x2987: v2987(0x20) = CONST 
    0x2989: v2989(0x20) = ADD v2987(0x20), v2986(0x0)
    0x298b: RETURN v2982, v2989(0x20)

}

function 0x1b54(0x1b54arg0x0, 0x1b54arg0x1) private {
    Begin block 0x1b54
    prev=[], succ=[0x1b79, 0x1b5c]
    =================================
    0x1b55: v1b55(0x60) = CONST 
    0x1b58: v1b58(0x1b79) = CONST 
    0x1b5b: JUMPI v1b58(0x1b79), v1b54arg0

    Begin block 0x1b79
    prev=[0x1b54], succ=[0x1b7d]
    =================================
    0x1b7b: v1b7b(0x0) = CONST 

    Begin block 0x1b7d
    prev=[0x1b84, 0x1b79], succ=[0x1b84, 0x1b91]
    =================================
    0x1b7d_0x1: v1b7d_1 = PHI v1b8a, v1b54arg0
    0x1b7f: v1b7f = ISZERO v1b7d_1
    0x1b80: v1b80(0x1b91) = CONST 
    0x1b83: JUMPI v1b80(0x1b91), v1b7f

    Begin block 0x1b84
    prev=[0x1b7d], succ=[0x1b7d]
    =================================
    0x1b84: v1b84(0x1) = CONST 
    0x1b84_0x0: v1b84_0 = PHI v1b7b(0x0), v1b86
    0x1b84_0x1: v1b84_1 = PHI v1b8a, v1b54arg0
    0x1b86: v1b86 = ADD v1b84(0x1), v1b84_0
    0x1b87: v1b87(0xa) = CONST 
    0x1b8a: v1b8a = DIV v1b84_1, v1b87(0xa)
    0x1b8d: v1b8d(0x1b7d) = CONST 
    0x1b90: JUMP v1b8d(0x1b7d)

    Begin block 0x1b91
    prev=[0x1b7d], succ=[0x1ba6, 0x1baa]
    =================================
    0x1b91_0x0: v1b91_0 = PHI v1b7b(0x0), v1b86
    0x1b92: v1b92(0x0) = CONST 
    0x1b95: v1b95(0xffffffffffffffff) = CONST 
    0x1b9f: v1b9f = GT v1b91_0, v1b95(0xffffffffffffffff)
    0x1ba1: v1ba1 = ISZERO v1b9f
    0x1ba2: v1ba2(0x1baa) = CONST 
    0x1ba5: JUMPI v1ba2(0x1baa), v1ba1

    Begin block 0x1ba6
    prev=[0x1b91], succ=[]
    =================================
    0x1ba6: v1ba6(0x0) = CONST 
    0x1ba9: REVERT v1ba6(0x0), v1ba6(0x0)

    Begin block 0x1baa
    prev=[0x1b91], succ=[0x1bc9, 0x1bd5]
    =================================
    0x1baa_0x1: v1baa_1 = PHI v1b7b(0x0), v1b86
    0x1bac: v1bac(0x40) = CONST 
    0x1bae: v1bae = MLOAD v1bac(0x40)
    0x1bb2: MSTORE v1bae, v1baa_1
    0x1bb4: v1bb4(0x1f) = CONST 
    0x1bb6: v1bb6 = ADD v1bb4(0x1f), v1baa_1
    0x1bb7: v1bb7(0x1f) = CONST 
    0x1bb9: v1bb9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1bb7(0x1f)
    0x1bba: v1bba = AND v1bb9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v1bb6
    0x1bbb: v1bbb(0x20) = CONST 
    0x1bbd: v1bbd = ADD v1bbb(0x20), v1bba
    0x1bbf: v1bbf = ADD v1bae, v1bbd
    0x1bc0: v1bc0(0x40) = CONST 
    0x1bc2: MSTORE v1bc0(0x40), v1bbf
    0x1bc4: v1bc4 = ISZERO v1baa_1
    0x1bc5: v1bc5(0x1bd5) = CONST 
    0x1bc8: JUMPI v1bc5(0x1bd5), v1bc4

    Begin block 0x1bc9
    prev=[0x1baa], succ=[0x1bd5]
    =================================
    0x1bc9: v1bc9(0x20) = CONST 
    0x1bc9_0x0: v1bc9_0 = PHI v1b7b(0x0), v1b86
    0x1bcc: v1bcc = ADD v1bae, v1bc9(0x20)
    0x1bcf: v1bcf = CALLDATASIZE 
    0x1bd1: CALLDATACOPY v1bcc, v1bcf, v1bc9_0
    0x1bd2: v1bd2 = ADD v1bc9_0, v1bcc

    Begin block 0x1bd5
    prev=[0x1bc9, 0x1baa], succ=[0x1bda]
    =================================

    Begin block 0x1bda
    prev=[0x1bd5, 0x1c09], succ=[0x1be1, 0x1c2d]
    =================================
    0x1bda_0x5: v1bda_5 = PHI v1c24, v1b54arg0
    0x1bdc: v1bdc = ISZERO v1bda_5
    0x1bdd: v1bdd(0x1c2d) = CONST 
    0x1be0: JUMPI v1bdd(0x1c2d), v1bdc

    Begin block 0x1be1
    prev=[0x1bda], succ=[0x1c08, 0x1c09]
    =================================
    0x1be1: v1be1(0x0) = CONST 
    0x1be1_0x0: v1be1_0 = PHI v1b7b(0x0), v1b86, v1be4
    0x1be1_0x5: v1be1_5 = PHI v1c24, v1b54arg0
    0x1be3: v1be3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1be1(0x0)
    0x1be4: v1be4 = ADD v1be3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1be1_0
    0x1be5: v1be5(0x0) = CONST 
    0x1be7: v1be7(0xa) = CONST 
    0x1bea: v1bea = DIV v1be1_5, v1be7(0xa)
    0x1beb: v1beb(0xa) = CONST 
    0x1bed: v1bed = MUL v1beb(0xa), v1bea
    0x1bef: v1bef = SUB v1be1_5, v1bed
    0x1bf0: v1bf0(0x30) = CONST 
    0x1bf2: v1bf2 = ADD v1bf0(0x30), v1bef
    0x1bf5: v1bf5(0x0) = CONST 
    0x1bf8: v1bf8(0xf8) = CONST 
    0x1bfa: v1bfa = SHL v1bf8(0xf8), v1bf2
    0x1c01: v1c01 = MLOAD v1bae
    0x1c03: v1c03 = LT v1be4, v1c01
    0x1c04: v1c04(0x1c09) = CONST 
    0x1c07: JUMPI v1c04(0x1c09), v1c03

    Begin block 0x1c08
    prev=[0x1be1], succ=[]
    =================================
    0x1c08: THROW 

    Begin block 0x1c09
    prev=[0x1be1], succ=[0x1bda]
    =================================
    0x1c09_0xa: v1c09_a = PHI v1c24, v1b54arg0
    0x1c0a: v1c0a(0x20) = CONST 
    0x1c0c: v1c0c = ADD v1c0a(0x20), v1be4
    0x1c0d: v1c0d = ADD v1c0c, v1bae
    0x1c0f: v1c0f(0x1) = CONST 
    0x1c11: v1c11(0x1) = CONST 
    0x1c13: v1c13(0xf8) = CONST 
    0x1c15: v1c15(0x100000000000000000000000000000000000000000000000000000000000000) = SHL v1c13(0xf8), v1c11(0x1)
    0x1c16: v1c16(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1c15(0x100000000000000000000000000000000000000000000000000000000000000), v1c0f(0x1)
    0x1c17: v1c17(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1c16(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1c18: v1c18 = AND v1c17(0xff00000000000000000000000000000000000000000000000000000000000000), v1bfa
    0x1c1b: v1c1b(0x0) = CONST 
    0x1c1d: v1c1d = BYTE v1c1b(0x0), v1c18
    0x1c1f: MSTORE8 v1c0d, v1c1d
    0x1c21: v1c21(0xa) = CONST 
    0x1c24: v1c24 = DIV v1c09_a, v1c21(0xa)
    0x1c29: v1c29(0x1bda) = CONST 
    0x1c2c: JUMP v1c29(0x1bda)

    Begin block 0x1c2d
    prev=[0x1bda], succ=[]
    =================================
    0x1c35: RETURNPRIVATE v1b54arg1, v1bae

    Begin block 0x1b5c
    prev=[0x1b54], succ=[0x2e46]
    =================================
    0x1b5d: v1b5d(0x40) = CONST 
    0x1b60: v1b60 = MLOAD v1b5d(0x40)
    0x1b63: v1b63 = ADD v1b5d(0x40), v1b60
    0x1b66: MSTORE v1b5d(0x40), v1b63
    0x1b67: v1b67(0x1) = CONST 
    0x1b6a: MSTORE v1b60, v1b67(0x1)
    0x1b6b: v1b6b(0x3) = CONST 
    0x1b6d: v1b6d(0xfc) = CONST 
    0x1b6f: v1b6f(0x3000000000000000000000000000000000000000000000000000000000000000) = SHL v1b6d(0xfc), v1b6b(0x3)
    0x1b70: v1b70(0x20) = CONST 
    0x1b73: v1b73 = ADD v1b60, v1b70(0x20)
    0x1b74: MSTORE v1b73, v1b6f(0x3000000000000000000000000000000000000000000000000000000000000000)
    0x1b75: v1b75(0x2e46) = CONST 
    0x1b78: JUMP v1b75(0x2e46)

    Begin block 0x2e46
    prev=[0x1b5c], succ=[]
    =================================
    0x2e4a: RETURNPRIVATE v1b54arg1, v1b60

}

function 0x1c36(0x1c36arg0x0, 0x1c36arg0x1, 0x1c36arg0x2, 0x1c36arg0x3, 0x1c36arg0x4, 0x1c36arg0x5, 0x1c36arg0x6) private {
    Begin block 0x1c36
    prev=[], succ=[0x2583B0x1c36]
    =================================
    0x1c37: v1c37(0x1c48) = CONST 
    0x1c3b: v1c3b(0x1) = CONST 
    0x1c3d: v1c3d(0x1) = CONST 
    0x1c3f: v1c3f(0xa0) = CONST 
    0x1c41: v1c41(0x10000000000000000000000000000000000000000) = SHL v1c3f(0xa0), v1c3d(0x1)
    0x1c42: v1c42(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c41(0x10000000000000000000000000000000000000000), v1c3b(0x1)
    0x1c43: v1c43 = AND v1c42(0xffffffffffffffffffffffffffffffffffffffff), v1c36arg3
    0x1c44: v1c44(0x2583) = CONST 
    0x1c47: JUMP v1c44(0x2583)

    Begin block 0x2583B0x1c36
    prev=[0x1c36], succ=[0x1c48]
    =================================
    0x2584S0x1c36: v2584V1c36 = EXTCODESIZE v1c43
    0x2585S0x1c36: v2585V1c36 = ISZERO v2584V1c36
    0x2586S0x1c36: v2586V1c36 = ISZERO v2585V1c36
    0x2588S0x1c36: JUMP v1c37(0x1c48)

    Begin block 0x1c48
    prev=[0x2583B0x1c36], succ=[0x2e6a, 0x1c4e]
    =================================
    0x1c49: v1c49 = ISZERO v2586V1c36
    0x1c4a: v1c4a(0x2e6a) = CONST 
    0x1c4d: JUMPI v1c4a(0x2e6a), v1c49

    Begin block 0x2e6a
    prev=[0x1c48], succ=[]
    =================================
    0x2e71: RETURNPRIVATE v1c36arg6

    Begin block 0x1c4e
    prev=[0x1c48], succ=[0x1cbe]
    =================================
    0x1c4f: v1c4f(0x1) = CONST 
    0x1c51: v1c51(0x1) = CONST 
    0x1c53: v1c53(0xa0) = CONST 
    0x1c55: v1c55(0x10000000000000000000000000000000000000000) = SHL v1c53(0xa0), v1c51(0x1)
    0x1c56: v1c56(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c55(0x10000000000000000000000000000000000000000), v1c4f(0x1)
    0x1c57: v1c57 = AND v1c56(0xffffffffffffffffffffffffffffffffffffffff), v1c36arg3
    0x1c58: v1c58(0xbc197c81) = CONST 
    0x1c62: v1c62(0x40) = CONST 
    0x1c64: v1c64 = MLOAD v1c62(0x40)
    0x1c66: v1c66(0xffffffff) = CONST 
    0x1c6b: v1c6b(0xbc197c81) = AND v1c66(0xffffffff), v1c58(0xbc197c81)
    0x1c6c: v1c6c(0xe0) = CONST 
    0x1c6e: v1c6e(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v1c6c(0xe0), v1c6b(0xbc197c81)
    0x1c70: MSTORE v1c64, v1c6e(0xbc197c8100000000000000000000000000000000000000000000000000000000)
    0x1c71: v1c71(0x4) = CONST 
    0x1c73: v1c73 = ADD v1c71(0x4), v1c64
    0x1c76: v1c76(0x1) = CONST 
    0x1c78: v1c78(0x1) = CONST 
    0x1c7a: v1c7a(0xa0) = CONST 
    0x1c7c: v1c7c(0x10000000000000000000000000000000000000000) = SHL v1c7a(0xa0), v1c78(0x1)
    0x1c7d: v1c7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c7c(0x10000000000000000000000000000000000000000), v1c76(0x1)
    0x1c7e: v1c7e = AND v1c7d(0xffffffffffffffffffffffffffffffffffffffff), v1c36arg5
    0x1c80: MSTORE v1c73, v1c7e
    0x1c81: v1c81(0x20) = CONST 
    0x1c83: v1c83 = ADD v1c81(0x20), v1c73
    0x1c85: v1c85(0x1) = CONST 
    0x1c87: v1c87(0x1) = CONST 
    0x1c89: v1c89(0xa0) = CONST 
    0x1c8b: v1c8b(0x10000000000000000000000000000000000000000) = SHL v1c89(0xa0), v1c87(0x1)
    0x1c8c: v1c8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c8b(0x10000000000000000000000000000000000000000), v1c85(0x1)
    0x1c8d: v1c8d = AND v1c8c(0xffffffffffffffffffffffffffffffffffffffff), v1c36arg4
    0x1c8f: MSTORE v1c83, v1c8d
    0x1c90: v1c90(0x20) = CONST 
    0x1c92: v1c92 = ADD v1c90(0x20), v1c83
    0x1c94: v1c94(0x20) = CONST 
    0x1c96: v1c96 = ADD v1c94(0x20), v1c92
    0x1c98: v1c98(0x20) = CONST 
    0x1c9a: v1c9a = ADD v1c98(0x20), v1c96
    0x1c9c: v1c9c(0x20) = CONST 
    0x1c9e: v1c9e = ADD v1c9c(0x20), v1c9a
    0x1ca1: v1ca1(0xa0) = SUB v1c9e, v1c73
    0x1ca3: MSTORE v1c92, v1ca1(0xa0)
    0x1ca7: v1ca7 = MLOAD v1c36arg2
    0x1ca9: MSTORE v1c9e, v1ca7
    0x1caa: v1caa(0x20) = CONST 
    0x1cac: v1cac = ADD v1caa(0x20), v1c9e
    0x1cb0: v1cb0 = MLOAD v1c36arg2
    0x1cb2: v1cb2(0x20) = CONST 
    0x1cb4: v1cb4 = ADD v1cb2(0x20), v1c36arg2
    0x1cb6: v1cb6(0x20) = CONST 
    0x1cb8: v1cb8 = MUL v1cb6(0x20), v1cb0
    0x1cbc: v1cbc(0x0) = CONST 

    Begin block 0x1cbe
    prev=[0x1c4e, 0x1cc7], succ=[0x1cd6, 0x1cc7]
    =================================
    0x1cbe_0x0: v1cbe_0 = PHI v1cbc(0x0), v1cd1
    0x1cc1: v1cc1 = LT v1cbe_0, v1cb8
    0x1cc2: v1cc2 = ISZERO v1cc1
    0x1cc3: v1cc3(0x1cd6) = CONST 
    0x1cc6: JUMPI v1cc3(0x1cd6), v1cc2

    Begin block 0x1cd6
    prev=[0x1cbe], succ=[0x1cfd]
    =================================
    0x1cdd: v1cdd = ADD v1cb8, v1cac
    0x1ce0: v1ce0 = SUB v1cdd, v1c73
    0x1ce2: MSTORE v1c96, v1ce0
    0x1ce6: v1ce6 = MLOAD v1c36arg1
    0x1ce8: MSTORE v1cdd, v1ce6
    0x1ce9: v1ce9(0x20) = CONST 
    0x1ceb: v1ceb = ADD v1ce9(0x20), v1cdd
    0x1cef: v1cef = MLOAD v1c36arg1
    0x1cf1: v1cf1(0x20) = CONST 
    0x1cf3: v1cf3 = ADD v1cf1(0x20), v1c36arg1
    0x1cf5: v1cf5(0x20) = CONST 
    0x1cf7: v1cf7 = MUL v1cf5(0x20), v1cef
    0x1cfb: v1cfb(0x0) = CONST 

    Begin block 0x1cfd
    prev=[0x1cd6, 0x1d06], succ=[0x1d15, 0x1d06]
    =================================
    0x1cfd_0x0: v1cfd_0 = PHI v1cfb(0x0), v1d10
    0x1d00: v1d00 = LT v1cfd_0, v1cf7
    0x1d01: v1d01 = ISZERO v1d00
    0x1d02: v1d02(0x1d15) = CONST 
    0x1d05: JUMPI v1d02(0x1d15), v1d01

    Begin block 0x1d15
    prev=[0x1cfd], succ=[0x1d39]
    =================================
    0x1d1c: v1d1c = ADD v1cf7, v1ceb
    0x1d1f: v1d1f = SUB v1d1c, v1c73
    0x1d21: MSTORE v1c9a, v1d1f
    0x1d25: v1d25 = MLOAD v1c36arg0
    0x1d27: MSTORE v1d1c, v1d25
    0x1d28: v1d28(0x20) = CONST 
    0x1d2a: v1d2a = ADD v1d28(0x20), v1d1c
    0x1d2e: v1d2e = MLOAD v1c36arg0
    0x1d30: v1d30(0x20) = CONST 
    0x1d32: v1d32 = ADD v1d30(0x20), v1c36arg0
    0x1d37: v1d37(0x0) = CONST 

    Begin block 0x1d39
    prev=[0x1d15, 0x1d42], succ=[0x1d51, 0x1d42]
    =================================
    0x1d39_0x0: v1d39_0 = PHI v1d37(0x0), v1d4c
    0x1d3c: v1d3c = LT v1d39_0, v1d2e
    0x1d3d: v1d3d = ISZERO v1d3c
    0x1d3e: v1d3e(0x1d51) = CONST 
    0x1d41: JUMPI v1d3e(0x1d51), v1d3d

    Begin block 0x1d51
    prev=[0x1d39], succ=[0x1d7e, 0x1d65]
    =================================
    0x1d5a: v1d5a = ADD v1d2e, v1d2a
    0x1d5c: v1d5c(0x1f) = CONST 
    0x1d5e: v1d5e = AND v1d5c(0x1f), v1d2e
    0x1d60: v1d60 = ISZERO v1d5e
    0x1d61: v1d61(0x1d7e) = CONST 
    0x1d64: JUMPI v1d61(0x1d7e), v1d60

    Begin block 0x1d7e
    prev=[0x1d51, 0x1d65], succ=[0x1d9f, 0x1da3]
    =================================
    0x1d7e_0x1: v1d7e_1 = PHI v1d5a, v1d7b
    0x1d8a: v1d8a(0x20) = CONST 
    0x1d8c: v1d8c(0x40) = CONST 
    0x1d8e: v1d8e = MLOAD v1d8c(0x40)
    0x1d91: v1d91 = SUB v1d7e_1, v1d8e
    0x1d93: v1d93(0x0) = CONST 
    0x1d97: v1d97 = EXTCODESIZE v1c57
    0x1d98: v1d98 = ISZERO v1d97
    0x1d9a: v1d9a = ISZERO v1d98
    0x1d9b: v1d9b(0x1da3) = CONST 
    0x1d9e: JUMPI v1d9b(0x1da3), v1d9a

    Begin block 0x1d9f
    prev=[0x1d7e], succ=[]
    =================================
    0x1d9f: v1d9f(0x0) = CONST 
    0x1da2: REVERT v1d9f(0x0), v1d9f(0x0)

    Begin block 0x1da3
    prev=[0x1d7e], succ=[0x1dc8, 0x1db1]
    =================================
    0x1da5: v1da5 = GAS 
    0x1da6: v1da6 = CALL v1da5, v1c57, v1d93(0x0), v1d8e, v1d91, v1d8e, v1d8a(0x20)
    0x1dac: v1dac = ISZERO v1da6
    0x1dad: v1dad(0x1dc8) = CONST 
    0x1db0: JUMPI v1dad(0x1dc8), v1dac

    Begin block 0x1dc8
    prev=[0x1da3, 0x1dc3], succ=[0x1dcd, 0x1e9b]
    =================================
    0x1dc8_0x0: v1dc8_0 = PHI v1da6, v1dc6(0x1)
    0x1dc9: v1dc9(0x1e9b) = CONST 
    0x1dcc: JUMPI v1dc9(0x1e9b), v1dc8_0

    Begin block 0x1dcd
    prev=[0x1dc8], succ=[0x1dd40x1c36]
    =================================
    0x1dcd: v1dcd(0x1dd4) = CONST 
    0x1dd0: v1dd0(0x2630) = CONST 
    0x1dd3: v1dd3_0 = CALLPRIVATE v1dd0(0x2630), v1dcd(0x1dd4)

    Begin block 0x1dd40x1c36
    prev=[0x1dcd], succ=[0x1dda0x1c36, 0x1ddf0x1c36]
    =================================
    0x1dd60x1c36: v1c361dd6(0x1ddf) = CONST 
    0x1dd90x1c36: JUMPI v1c361dd6(0x1ddf), v1dd3_0

    Begin block 0x1dda0x1c36
    prev=[0x1dd40x1c36], succ=[0x1e640x1c36]
    =================================
    0x1ddb0x1c36: v1c361ddb(0x1e64) = CONST 
    0x1dde0x1c36: JUMP v1c361ddb(0x1e64)

    Begin block 0x1e640x1c36
    prev=[0x1dda0x1c36], succ=[]
    =================================
    0x1e650x1c36: v1c361e65(0x40) = CONST 
    0x1e670x1c36: v1c361e67 = MLOAD v1c361e65(0x40)
    0x1e680x1c36: v1c361e68(0x461bcd) = CONST 
    0x1e6c0x1c36: v1c361e6c(0xe5) = CONST 
    0x1e6e0x1c36: v1c361e6e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c361e6c(0xe5), v1c361e68(0x461bcd)
    0x1e700x1c36: MSTORE v1c361e67, v1c361e6e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e710x1c36: v1c361e71(0x4) = CONST 
    0x1e730x1c36: v1c361e73 = ADD v1c361e71(0x4), v1c361e67
    0x1e760x1c36: v1c361e76(0x20) = CONST 
    0x1e780x1c36: v1c361e78 = ADD v1c361e76(0x20), v1c361e73
    0x1e7b0x1c36: v1c361e7b(0x20) = SUB v1c361e78, v1c361e73
    0x1e7d0x1c36: MSTORE v1c361e73, v1c361e7b(0x20)
    0x1e7e0x1c36: v1c361e7e(0x2b) = CONST 
    0x1e810x1c36: MSTORE v1c361e78, v1c361e7e(0x2b)
    0x1e820x1c36: v1c361e82(0x20) = CONST 
    0x1e840x1c36: v1c361e84 = ADD v1c361e82(0x20), v1c361e78
    0x1e860x1c36: v1c361e86(0x26d7) = CONST 
    0x1e890x1c36: v1c361e89(0x2b) = CONST 
    0x1e8c0x1c36: CODECOPY v1c361e84, v1c361e86(0x26d7), v1c361e89(0x2b)
    0x1e8d0x1c36: v1c361e8d(0x40) = CONST 
    0x1e8f0x1c36: v1c361e8f = ADD v1c361e8d(0x40), v1c361e84
    0x1e930x1c36: v1c361e93(0x40) = CONST 
    0x1e950x1c36: v1c361e95 = MLOAD v1c361e93(0x40)
    0x1e980x1c36: v1c361e98(0x84) = SUB v1c361e8f, v1c361e95
    0x1e9a0x1c36: REVERT v1c361e95, v1c361e98(0x84)

    Begin block 0x1ddf0x1c36
    prev=[0x1dd40x1c36], succ=[0x1e110x1c36]
    =================================
    0x1de10x1c36: v1c361de1(0x40) = CONST 
    0x1de30x1c36: v1c361de3 = MLOAD v1c361de1(0x40)
    0x1de40x1c36: v1c361de4(0x461bcd) = CONST 
    0x1de80x1c36: v1c361de8(0xe5) = CONST 
    0x1dea0x1c36: v1c361dea(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c361de8(0xe5), v1c361de4(0x461bcd)
    0x1dec0x1c36: MSTORE v1c361de3, v1c361dea(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ded0x1c36: v1c361ded(0x4) = CONST 
    0x1def0x1c36: v1c361def = ADD v1c361ded(0x4), v1c361de3
    0x1df20x1c36: v1c361df2(0x20) = CONST 
    0x1df40x1c36: v1c361df4 = ADD v1c361df2(0x20), v1c361def
    0x1df70x1c36: v1c361df7(0x20) = SUB v1c361df4, v1c361def
    0x1df90x1c36: MSTORE v1c361def, v1c361df7(0x20)
    0x1dfd0x1c36: v1c361dfd = MLOAD v1dd3_0
    0x1dff0x1c36: MSTORE v1c361df4, v1c361dfd
    0x1e000x1c36: v1c361e00(0x20) = CONST 
    0x1e020x1c36: v1c361e02 = ADD v1c361e00(0x20), v1c361df4
    0x1e060x1c36: v1c361e06 = MLOAD v1dd3_0
    0x1e080x1c36: v1c361e08(0x20) = CONST 
    0x1e0a0x1c36: v1c361e0a = ADD v1c361e08(0x20), v1dd3_0
    0x1e0f0x1c36: v1c361e0f(0x0) = CONST 

    Begin block 0x1e110x1c36
    prev=[0x1e1a0x1c36, 0x1ddf0x1c36], succ=[0x1e290x1c36, 0x1e1a0x1c36]
    =================================
    0x1e110x1c36_0x0: v1e111c36_0 = PHI v1c361e24, v1c361e0f(0x0)
    0x1e140x1c36: v1c361e14 = LT v1e111c36_0, v1c361e06
    0x1e150x1c36: v1c361e15 = ISZERO v1c361e14
    0x1e160x1c36: v1c361e16(0x1e29) = CONST 
    0x1e190x1c36: JUMPI v1c361e16(0x1e29), v1c361e15

    Begin block 0x1e290x1c36
    prev=[0x1e110x1c36], succ=[0x1e560x1c36, 0x1e3d0x1c36]
    =================================
    0x1e320x1c36: v1c361e32 = ADD v1c361e06, v1c361e02
    0x1e340x1c36: v1c361e34(0x1f) = CONST 
    0x1e360x1c36: v1c361e36 = AND v1c361e34(0x1f), v1c361e06
    0x1e380x1c36: v1c361e38 = ISZERO v1c361e36
    0x1e390x1c36: v1c361e39(0x1e56) = CONST 
    0x1e3c0x1c36: JUMPI v1c361e39(0x1e56), v1c361e38

    Begin block 0x1e560x1c36
    prev=[0x1e290x1c36, 0x1e3d0x1c36], succ=[]
    =================================
    0x1e560x1c36_0x1: v1e561c36_1 = PHI v1c361e53, v1c361e32
    0x1e5c0x1c36: v1c361e5c(0x40) = CONST 
    0x1e5e0x1c36: v1c361e5e = MLOAD v1c361e5c(0x40)
    0x1e610x1c36: v1c361e61 = SUB v1e561c36_1, v1c361e5e
    0x1e630x1c36: REVERT v1c361e5e, v1c361e61

    Begin block 0x1e3d0x1c36
    prev=[0x1e290x1c36], succ=[0x1e560x1c36]
    =================================
    0x1e3f0x1c36: v1c361e3f = SUB v1c361e32, v1c361e36
    0x1e410x1c36: v1c361e41 = MLOAD v1c361e3f
    0x1e420x1c36: v1c361e42(0x1) = CONST 
    0x1e450x1c36: v1c361e45(0x20) = CONST 
    0x1e470x1c36: v1c361e47 = SUB v1c361e45(0x20), v1c361e36
    0x1e480x1c36: v1c361e48(0x100) = CONST 
    0x1e4b0x1c36: v1c361e4b = EXP v1c361e48(0x100), v1c361e47
    0x1e4c0x1c36: v1c361e4c = SUB v1c361e4b, v1c361e42(0x1)
    0x1e4d0x1c36: v1c361e4d = NOT v1c361e4c
    0x1e4e0x1c36: v1c361e4e = AND v1c361e4d, v1c361e41
    0x1e500x1c36: MSTORE v1c361e3f, v1c361e4e
    0x1e510x1c36: v1c361e51(0x20) = CONST 
    0x1e530x1c36: v1c361e53 = ADD v1c361e51(0x20), v1c361e3f

    Begin block 0x1e1a0x1c36
    prev=[0x1e110x1c36], succ=[0x1e110x1c36]
    =================================
    0x1e1a0x1c36_0x0: v1e1a1c36_0 = PHI v1c361e24, v1c361e0f(0x0)
    0x1e1c0x1c36: v1c361e1c = ADD v1e1a1c36_0, v1c361e0a
    0x1e1d0x1c36: v1c361e1d = MLOAD v1c361e1c
    0x1e200x1c36: v1c361e20 = ADD v1e1a1c36_0, v1c361e02
    0x1e210x1c36: MSTORE v1c361e20, v1c361e1d
    0x1e220x1c36: v1c361e22(0x20) = CONST 
    0x1e240x1c36: v1c361e24 = ADD v1c361e22(0x20), v1e1a1c36_0
    0x1e250x1c36: v1c361e25(0x1e11) = CONST 
    0x1e280x1c36: JUMP v1c361e25(0x1e11)

    Begin block 0x1e9b
    prev=[0x1dc8], succ=[0x1eb4, 0x1f000x1c36]
    =================================
    0x1e9b_0x0: v1e9b_0 = PHI v1dc5, v1c36arg0
    0x1e9c: v1e9c(0x1) = CONST 
    0x1e9e: v1e9e(0x1) = CONST 
    0x1ea0: v1ea0(0xe0) = CONST 
    0x1ea2: v1ea2(0x100000000000000000000000000000000000000000000000000000000) = SHL v1ea0(0xe0), v1e9e(0x1)
    0x1ea3: v1ea3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1ea2(0x100000000000000000000000000000000000000000000000000000000), v1e9c(0x1)
    0x1ea4: v1ea4(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1ea3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1ea6: v1ea6 = AND v1e9b_0, v1ea4(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x1ea7: v1ea7(0xbc197c81) = CONST 
    0x1eac: v1eac(0xe0) = CONST 
    0x1eae: v1eae(0xbc197c8100000000000000000000000000000000000000000000000000000000) = SHL v1eac(0xe0), v1ea7(0xbc197c81)
    0x1eaf: v1eaf = EQ v1eae(0xbc197c8100000000000000000000000000000000000000000000000000000000), v1ea6
    0x1eb0: v1eb0(0x1f00) = CONST 
    0x1eb3: JUMPI v1eb0(0x1f00), v1eaf

    Begin block 0x1eb4
    prev=[0x1e9b], succ=[]
    =================================
    0x1eb4: v1eb4(0x40) = CONST 
    0x1eb7: v1eb7 = MLOAD v1eb4(0x40)
    0x1eb8: v1eb8(0x461bcd) = CONST 
    0x1ebc: v1ebc(0xe5) = CONST 
    0x1ebe: v1ebe(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1ebc(0xe5), v1eb8(0x461bcd)
    0x1ec0: MSTORE v1eb7, v1ebe(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ec1: v1ec1(0x20) = CONST 
    0x1ec3: v1ec3(0x4) = CONST 
    0x1ec6: v1ec6 = ADD v1eb7, v1ec3(0x4)
    0x1ec7: MSTORE v1ec6, v1ec1(0x20)
    0x1ec8: v1ec8(0x1f) = CONST 
    0x1eca: v1eca(0x24) = CONST 
    0x1ecd: v1ecd = ADD v1eb7, v1eca(0x24)
    0x1ece: MSTORE v1ecd, v1ec8(0x1f)
    0x1ecf: v1ecf(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x1ef0: v1ef0(0x44) = CONST 
    0x1ef3: v1ef3 = ADD v1eb7, v1ef0(0x44)
    0x1ef4: MSTORE v1ef3, v1ecf(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x1ef6: v1ef6 = MLOAD v1eb4(0x40)
    0x1efa: v1efa(0x0) = SUB v1eb7, v1ef6
    0x1efb: v1efb(0x64) = CONST 
    0x1efd: v1efd(0x64) = ADD v1efb(0x64), v1efa(0x0)
    0x1eff: REVERT v1ef6, v1efd(0x64)

    Begin block 0x1f000x1c36
    prev=[0x1e9b], succ=[0x1f020x1c36]
    =================================

    Begin block 0x1f020x1c36
    prev=[0x1f000x1c36], succ=[]
    =================================
    0x1f090x1c36: RETURNPRIVATE v1c36arg6

    Begin block 0x1db1
    prev=[0x1da3], succ=[0x1dbf, 0x1dc3]
    =================================
    0x1db2: v1db2(0x40) = CONST 
    0x1db4: v1db4 = MLOAD v1db2(0x40)
    0x1db5: v1db5 = RETURNDATASIZE 
    0x1db6: v1db6(0x20) = CONST 
    0x1db9: v1db9 = LT v1db5, v1db6(0x20)
    0x1dba: v1dba = ISZERO v1db9
    0x1dbb: v1dbb(0x1dc3) = CONST 
    0x1dbe: JUMPI v1dbb(0x1dc3), v1dba

    Begin block 0x1dbf
    prev=[0x1db1], succ=[]
    =================================
    0x1dbf: v1dbf(0x0) = CONST 
    0x1dc2: REVERT v1dbf(0x0), v1dbf(0x0)

    Begin block 0x1dc3
    prev=[0x1db1], succ=[0x1dc8]
    =================================
    0x1dc5: v1dc5 = MLOAD v1db4
    0x1dc6: v1dc6(0x1) = CONST 

    Begin block 0x1d65
    prev=[0x1d51], succ=[0x1d7e]
    =================================
    0x1d67: v1d67 = SUB v1d5a, v1d5e
    0x1d69: v1d69 = MLOAD v1d67
    0x1d6a: v1d6a(0x1) = CONST 
    0x1d6d: v1d6d(0x20) = CONST 
    0x1d6f: v1d6f = SUB v1d6d(0x20), v1d5e
    0x1d70: v1d70(0x100) = CONST 
    0x1d73: v1d73 = EXP v1d70(0x100), v1d6f
    0x1d74: v1d74 = SUB v1d73, v1d6a(0x1)
    0x1d75: v1d75 = NOT v1d74
    0x1d76: v1d76 = AND v1d75, v1d69
    0x1d78: MSTORE v1d67, v1d76
    0x1d79: v1d79(0x20) = CONST 
    0x1d7b: v1d7b = ADD v1d79(0x20), v1d67

    Begin block 0x1d42
    prev=[0x1d39], succ=[0x1d39]
    =================================
    0x1d42_0x0: v1d42_0 = PHI v1d37(0x0), v1d4c
    0x1d44: v1d44 = ADD v1d42_0, v1d32
    0x1d45: v1d45 = MLOAD v1d44
    0x1d48: v1d48 = ADD v1d42_0, v1d2a
    0x1d49: MSTORE v1d48, v1d45
    0x1d4a: v1d4a(0x20) = CONST 
    0x1d4c: v1d4c = ADD v1d4a(0x20), v1d42_0
    0x1d4d: v1d4d(0x1d39) = CONST 
    0x1d50: JUMP v1d4d(0x1d39)

    Begin block 0x1d06
    prev=[0x1cfd], succ=[0x1cfd]
    =================================
    0x1d06_0x0: v1d06_0 = PHI v1cfb(0x0), v1d10
    0x1d08: v1d08 = ADD v1d06_0, v1cf3
    0x1d09: v1d09 = MLOAD v1d08
    0x1d0c: v1d0c = ADD v1d06_0, v1ceb
    0x1d0d: MSTORE v1d0c, v1d09
    0x1d0e: v1d0e(0x20) = CONST 
    0x1d10: v1d10 = ADD v1d0e(0x20), v1d06_0
    0x1d11: v1d11(0x1cfd) = CONST 
    0x1d14: JUMP v1d11(0x1cfd)

    Begin block 0x1cc7
    prev=[0x1cbe], succ=[0x1cbe]
    =================================
    0x1cc7_0x0: v1cc7_0 = PHI v1cbc(0x0), v1cd1
    0x1cc9: v1cc9 = ADD v1cc7_0, v1cb4
    0x1cca: v1cca = MLOAD v1cc9
    0x1ccd: v1ccd = ADD v1cc7_0, v1cac
    0x1cce: MSTORE v1ccd, v1cca
    0x1ccf: v1ccf(0x20) = CONST 
    0x1cd1: v1cd1 = ADD v1ccf(0x20), v1cc7_0
    0x1cd2: v1cd2(0x1cbe) = CONST 
    0x1cd5: JUMP v1cd2(0x1cbe)

}

function setURI(string)() public {
    Begin block 0x1d5
    prev=[], succ=[0x1e7, 0x1eb]
    =================================
    0x1d6: v1d6(0x29ab) = CONST 
    0x1d9: v1d9(0x4) = CONST 
    0x1dc: v1dc = CALLDATASIZE 
    0x1dd: v1dd = SUB v1dc, v1d9(0x4)
    0x1de: v1de(0x20) = CONST 
    0x1e1: v1e1 = LT v1dd, v1de(0x20)
    0x1e2: v1e2 = ISZERO v1e1
    0x1e3: v1e3(0x1eb) = CONST 
    0x1e6: JUMPI v1e3(0x1eb), v1e2

    Begin block 0x1e7
    prev=[0x1d5], succ=[]
    =================================
    0x1e7: v1e7(0x0) = CONST 
    0x1ea: REVERT v1e7(0x0), v1e7(0x0)

    Begin block 0x1eb
    prev=[0x1d5], succ=[0x201, 0x205]
    =================================
    0x1ed: v1ed = ADD v1d9(0x4), v1dd
    0x1ef: v1ef(0x20) = CONST 
    0x1f2: v1f2(0x24) = ADD v1d9(0x4), v1ef(0x20)
    0x1f4: v1f4 = CALLDATALOAD v1d9(0x4)
    0x1f5: v1f5(0x1) = CONST 
    0x1f7: v1f7(0x20) = CONST 
    0x1f9: v1f9(0x100000000) = SHL v1f7(0x20), v1f5(0x1)
    0x1fb: v1fb = GT v1f4, v1f9(0x100000000)
    0x1fc: v1fc = ISZERO v1fb
    0x1fd: v1fd(0x205) = CONST 
    0x200: JUMPI v1fd(0x205), v1fc

    Begin block 0x201
    prev=[0x1eb], succ=[]
    =================================
    0x201: v201(0x0) = CONST 
    0x204: REVERT v201(0x0), v201(0x0)

    Begin block 0x205
    prev=[0x1eb], succ=[0x213, 0x217]
    =================================
    0x207: v207 = ADD v1d9(0x4), v1f4
    0x209: v209(0x20) = CONST 
    0x20c: v20c = ADD v207, v209(0x20)
    0x20d: v20d = GT v20c, v1ed
    0x20e: v20e = ISZERO v20d
    0x20f: v20f(0x217) = CONST 
    0x212: JUMPI v20f(0x217), v20e

    Begin block 0x213
    prev=[0x205], succ=[]
    =================================
    0x213: v213(0x0) = CONST 
    0x216: REVERT v213(0x0), v213(0x0)

    Begin block 0x217
    prev=[0x205], succ=[0x234, 0x238]
    =================================
    0x219: v219 = CALLDATALOAD v207
    0x21b: v21b(0x20) = CONST 
    0x21d: v21d = ADD v21b(0x20), v207
    0x220: v220(0x1) = CONST 
    0x223: v223 = MUL v219, v220(0x1)
    0x225: v225 = ADD v21d, v223
    0x226: v226 = GT v225, v1ed
    0x227: v227(0x1) = CONST 
    0x229: v229(0x20) = CONST 
    0x22b: v22b(0x100000000) = SHL v229(0x20), v227(0x1)
    0x22d: v22d = GT v219, v22b(0x100000000)
    0x22e: v22e = OR v22d, v226
    0x22f: v22f = ISZERO v22e
    0x230: v230(0x238) = CONST 
    0x233: JUMPI v230(0x238), v22f

    Begin block 0x234
    prev=[0x217], succ=[]
    =================================
    0x234: v234(0x0) = CONST 
    0x237: REVERT v234(0x0), v234(0x0)

    Begin block 0x238
    prev=[0x217], succ=[0xa59]
    =================================
    0x23d: v23d(0x1f) = CONST 
    0x23f: v23f = ADD v23d(0x1f), v219
    0x240: v240(0x20) = CONST 
    0x244: v244 = DIV v23f, v240(0x20)
    0x245: v245 = MUL v244, v240(0x20)
    0x246: v246(0x20) = CONST 
    0x248: v248 = ADD v246(0x20), v245
    0x249: v249(0x40) = CONST 
    0x24b: v24b = MLOAD v249(0x40)
    0x24e: v24e = ADD v24b, v248
    0x24f: v24f(0x40) = CONST 
    0x251: MSTORE v24f(0x40), v24e
    0x259: MSTORE v24b, v219
    0x25a: v25a(0x20) = CONST 
    0x25c: v25c = ADD v25a(0x20), v24b
    0x262: CALLDATACOPY v25c, v21d, v219
    0x263: v263(0x0) = CONST 
    0x266: v266 = ADD v25c, v219
    0x26a: MSTORE v266, v263(0x0)
    0x26f: v26f(0xa59) = CONST 
    0x278: JUMP v26f(0xa59)

    Begin block 0xa59
    prev=[0x238], succ=[0xa6c, 0xab3]
    =================================
    0xa5a: va5a(0x4) = CONST 
    0xa5c: va5c = SLOAD va5a(0x4)
    0xa5d: va5d(0x1) = CONST 
    0xa5f: va5f(0x1) = CONST 
    0xa61: va61(0xa0) = CONST 
    0xa63: va63(0x10000000000000000000000000000000000000000) = SHL va61(0xa0), va5f(0x1)
    0xa64: va64(0xffffffffffffffffffffffffffffffffffffffff) = SUB va63(0x10000000000000000000000000000000000000000), va5d(0x1)
    0xa65: va65 = AND va64(0xffffffffffffffffffffffffffffffffffffffff), va5c
    0xa66: va66 = CALLER 
    0xa67: va67 = EQ va66, va65
    0xa68: va68(0xab3) = CONST 
    0xa6b: JUMPI va68(0xab3), va67

    Begin block 0xa6c
    prev=[0xa59], succ=[]
    =================================
    0xa6c: va6c(0x40) = CONST 
    0xa6f: va6f = MLOAD va6c(0x40)
    0xa70: va70(0x461bcd) = CONST 
    0xa74: va74(0xe5) = CONST 
    0xa76: va76(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL va74(0xe5), va70(0x461bcd)
    0xa78: MSTORE va6f, va76(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa79: va79(0x20) = CONST 
    0xa7b: va7b(0x4) = CONST 
    0xa7e: va7e = ADD va6f, va7b(0x4)
    0xa7f: MSTORE va7e, va79(0x20)
    0xa80: va80(0x18) = CONST 
    0xa82: va82(0x24) = CONST 
    0xa85: va85 = ADD va6f, va82(0x24)
    0xa86: MSTORE va85, va80(0x18)
    0xa87: va87(0x6d7573742062652067616c61787920636f6d6d756e697479) = CONST 
    0xaa0: vaa0(0x40) = CONST 
    0xaa2: vaa2(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000) = SHL vaa0(0x40), va87(0x6d7573742062652067616c61787920636f6d6d756e697479)
    0xaa3: vaa3(0x44) = CONST 
    0xaa6: vaa6 = ADD va6f, vaa3(0x44)
    0xaa7: MSTORE vaa6, vaa2(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000)
    0xaa9: vaa9 = MLOAD va6c(0x40)
    0xaad: vaad(0x0) = SUB va6f, vaa9
    0xaae: vaae(0x64) = CONST 
    0xab0: vab0(0x64) = ADD vaae(0x64), vaad(0x0)
    0xab2: REVERT vaa9, vab0(0x64)

    Begin block 0xab3
    prev=[0xa59], succ=[0x2589B0xab3]
    =================================
    0xab5: vab5 = MLOAD v24b
    0xab6: vab6(0x2cae) = CONST 
    0xaba: vaba(0x2) = CONST 
    0xabd: vabd(0x20) = CONST 
    0xac0: vac0 = ADD v24b, vabd(0x20)
    0xac2: vac2(0x2589) = CONST 
    0xac5: JUMP vac2(0x2589)

    Begin block 0x2589B0xab3
    prev=[0xab3], succ=[0x25b7B0xab3, 0x25bfB0xab3]
    =================================
    0x258cS0xab3: v258cVab3 = SLOAD vaba(0x2)
    0x258dS0xab3: v258dVab3(0x1) = CONST 
    0x2590S0xab3: v2590Vab3(0x1) = CONST 
    0x2592S0xab3: v2592Vab3 = AND v2590Vab3(0x1), v258cVab3
    0x2593S0xab3: v2593Vab3 = ISZERO v2592Vab3
    0x2594S0xab3: v2594Vab3(0x100) = CONST 
    0x2597S0xab3: v2597Vab3 = MUL v2594Vab3(0x100), v2593Vab3
    0x2598S0xab3: v2598Vab3 = SUB v2597Vab3, v258dVab3(0x1)
    0x2599S0xab3: v2599Vab3 = AND v2598Vab3, v258cVab3
    0x259aS0xab3: v259aVab3(0x2) = CONST 
    0x259dS0xab3: v259dVab3 = DIV v2599Vab3, v259aVab3(0x2)
    0x259fS0xab3: v259fVab3(0x0) = CONST 
    0x25a1S0xab3: MSTORE v259fVab3(0x0), vaba(0x2)
    0x25a2S0xab3: v25a2Vab3(0x20) = CONST 
    0x25a4S0xab3: v25a4Vab3(0x0) = CONST 
    0x25a6S0xab3: v25a6Vab3 = SHA3 v25a4Vab3(0x0), v25a2Vab3(0x20)
    0x25a8S0xab3: v25a8Vab3(0x1f) = CONST 
    0x25aaS0xab3: v25aaVab3 = ADD v25a8Vab3(0x1f), v259dVab3
    0x25abS0xab3: v25abVab3(0x20) = CONST 
    0x25aeS0xab3: v25aeVab3 = DIV v25aaVab3, v25abVab3(0x20)
    0x25b0S0xab3: v25b0Vab3 = ADD v25a6Vab3, v25aeVab3
    0x25b3S0xab3: v25b3Vab3(0x25bf) = CONST 
    0x25b6S0xab3: JUMPI v25b3Vab3(0x25bf), vab5

    Begin block 0x25b7B0xab3
    prev=[0x2589B0xab3], succ=[0x2605B0xab3]
    =================================
    0x25b7S0xab3: v25b7Vab3(0x0) = CONST 
    0x25baS0xab3: SSTORE vaba(0x2), v25b7Vab3(0x0)
    0x25bbS0xab3: v25bbVab3(0x2605) = CONST 
    0x25beS0xab3: JUMP v25bbVab3(0x2605)

    Begin block 0x2605B0xab3
    prev=[0x25b7B0xab3, 0x25d8B0xab3, 0x25eaB0xab3, 0x25c8B0xab3], succ=[0x2615B0x2605B0xab3]
    =================================
    0x2605_0x1S0xab3: v2605_1Vab3 = PHI v25a6Vab3, v25ffVab3
    0x2607S0xab3: v2607Vab3(0x2ede) = CONST 
    0x260dS0xab3: v260dVab3(0x2615) = CONST 
    0x2610S0xab3: JUMP v260dVab3(0x2615)

    Begin block 0x2615B0x2605B0xab3
    prev=[0x2605B0xab3], succ=[0x2616B0x2605B0xab3]
    =================================

    Begin block 0x2616B0x2605B0xab3
    prev=[0x261fB0x2605B0xab3, 0x2615B0x2605B0xab3], succ=[0x261fB0x2605B0xab3, 0x2f01B0x2605B0xab3]
    =================================
    0x2616_0x0S0x2605S0xab3: v2616_0V2605Vab3 = PHI v2605_1Vab3, v2625V2605Vab3
    0x2619S0x2605S0xab3: v2619V2605Vab3 = GT v25b0Vab3, v2616_0V2605Vab3
    0x261aS0x2605S0xab3: v261aV2605Vab3 = ISZERO v2619V2605Vab3
    0x261bS0x2605S0xab3: v261bV2605Vab3(0x2f01) = CONST 
    0x261eS0x2605S0xab3: JUMPI v261bV2605Vab3(0x2f01), v261aV2605Vab3

    Begin block 0x261fB0x2605B0xab3
    prev=[0x2616B0x2605B0xab3], succ=[0x2616B0x2605B0xab3]
    =================================
    0x261fS0x2605S0xab3: v261fV2605Vab3(0x0) = CONST 
    0x261f_0x0S0x2605S0xab3: v261f_0V2605Vab3 = PHI v2605_1Vab3, v2625V2605Vab3
    0x2622S0x2605S0xab3: SSTORE v261f_0V2605Vab3, v261fV2605Vab3(0x0)
    0x2623S0x2605S0xab3: v2623V2605Vab3(0x1) = CONST 
    0x2625S0x2605S0xab3: v2625V2605Vab3 = ADD v2623V2605Vab3(0x1), v261f_0V2605Vab3
    0x2626S0x2605S0xab3: v2626V2605Vab3(0x2616) = CONST 
    0x2629S0x2605S0xab3: JUMP v2626V2605Vab3(0x2616)

    Begin block 0x2f01B0x2605B0xab3
    prev=[0x2616B0x2605B0xab3], succ=[0x2edeB0xab3]
    =================================
    0x2f04S0x2605S0xab3: JUMP v2607Vab3(0x2ede)

    Begin block 0x2edeB0xab3
    prev=[0x2f01B0x2605B0xab3], succ=[0x2cae]
    =================================
    0x2ee1S0xab3: JUMP vab6(0x2cae)

    Begin block 0x2cae
    prev=[0x2edeB0xab3], succ=[0x29ab]
    =================================
    0x2cb1: JUMP v1d6(0x29ab)

    Begin block 0x29ab
    prev=[0x2cae], succ=[]
    =================================
    0x29ac: STOP 

    Begin block 0x25bfB0xab3
    prev=[0x2589B0xab3], succ=[0x25d8B0xab3, 0x25c8B0xab3]
    =================================
    0x25c1S0xab3: v25c1Vab3(0x1f) = CONST 
    0x25c3S0xab3: v25c3Vab3 = LT v25c1Vab3(0x1f), vab5
    0x25c4S0xab3: v25c4Vab3(0x25d8) = CONST 
    0x25c7S0xab3: JUMPI v25c4Vab3(0x25d8), v25c3Vab3

    Begin block 0x25d8B0xab3
    prev=[0x25bfB0xab3], succ=[0x2605B0xab3, 0x25e7B0xab3]
    =================================
    0x25dbS0xab3: v25dbVab3 = ADD vab5, vab5
    0x25dcS0xab3: v25dcVab3(0x1) = CONST 
    0x25deS0xab3: v25deVab3 = ADD v25dcVab3(0x1), v25dbVab3
    0x25e0S0xab3: SSTORE vaba(0x2), v25deVab3
    0x25e2S0xab3: v25e2Vab3 = ISZERO vab5
    0x25e3S0xab3: v25e3Vab3(0x2605) = CONST 
    0x25e6S0xab3: JUMPI v25e3Vab3(0x2605), v25e2Vab3

    Begin block 0x25e7B0xab3
    prev=[0x25d8B0xab3], succ=[0x25eaB0xab3]
    =================================
    0x25e9S0xab3: v25e9Vab3 = ADD vac0, vab5

    Begin block 0x25eaB0xab3
    prev=[0x25e7B0xab3, 0x25f3B0xab3], succ=[0x2605B0xab3, 0x25f3B0xab3]
    =================================
    0x25ea_0x2S0xab3: v25ea_2Vab3 = PHI vac0, v25faVab3
    0x25edS0xab3: v25edVab3 = GT v25e9Vab3, v25ea_2Vab3
    0x25eeS0xab3: v25eeVab3 = ISZERO v25edVab3
    0x25efS0xab3: v25efVab3(0x2605) = CONST 
    0x25f2S0xab3: JUMPI v25efVab3(0x2605), v25eeVab3

    Begin block 0x25f3B0xab3
    prev=[0x25eaB0xab3], succ=[0x25eaB0xab3]
    =================================
    0x25f3_0x1S0xab3: v25f3_1Vab3 = PHI v25a6Vab3, v25ffVab3
    0x25f3_0x2S0xab3: v25f3_2Vab3 = PHI vac0, v25faVab3
    0x25f4S0xab3: v25f4Vab3 = MLOAD v25f3_2Vab3
    0x25f6S0xab3: SSTORE v25f3_1Vab3, v25f4Vab3
    0x25f8S0xab3: v25f8Vab3(0x20) = CONST 
    0x25faS0xab3: v25faVab3 = ADD v25f8Vab3(0x20), v25f3_2Vab3
    0x25fdS0xab3: v25fdVab3(0x1) = CONST 
    0x25ffS0xab3: v25ffVab3 = ADD v25fdVab3(0x1), v25f3_1Vab3
    0x2601S0xab3: v2601Vab3(0x25ea) = CONST 
    0x2604S0xab3: JUMP v2601Vab3(0x25ea)

    Begin block 0x25c8B0xab3
    prev=[0x25bfB0xab3], succ=[0x2605B0xab3]
    =================================
    0x25c9S0xab3: v25c9Vab3 = MLOAD vac0
    0x25caS0xab3: v25caVab3(0xff) = CONST 
    0x25ccS0xab3: v25ccVab3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v25caVab3(0xff)
    0x25cdS0xab3: v25cdVab3 = AND v25ccVab3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v25c9Vab3
    0x25d0S0xab3: v25d0Vab3 = ADD vab5, vab5
    0x25d1S0xab3: v25d1Vab3 = OR v25d0Vab3, v25cdVab3
    0x25d3S0xab3: SSTORE vaba(0x2), v25d1Vab3
    0x25d4S0xab3: v25d4Vab3(0x2605) = CONST 
    0x25d7S0xab3: JUMP v25d4Vab3(0x2605)

}

function 0x23fc(0x23fcarg0x0, 0x23fcarg0x1, 0x23fcarg0x2, 0x23fcarg0x3, 0x23fcarg0x4, 0x23fcarg0x5, 0x23fcarg0x6) private {
    Begin block 0x23fc
    prev=[], succ=[0x2583B0x23fc]
    =================================
    0x23fd: v23fd(0x240e) = CONST 
    0x2401: v2401(0x1) = CONST 
    0x2403: v2403(0x1) = CONST 
    0x2405: v2405(0xa0) = CONST 
    0x2407: v2407(0x10000000000000000000000000000000000000000) = SHL v2405(0xa0), v2403(0x1)
    0x2408: v2408(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2407(0x10000000000000000000000000000000000000000), v2401(0x1)
    0x2409: v2409 = AND v2408(0xffffffffffffffffffffffffffffffffffffffff), v23fcarg3
    0x240a: v240a(0x2583) = CONST 
    0x240d: JUMP v240a(0x2583)

    Begin block 0x2583B0x23fc
    prev=[0x23fc], succ=[0x240e]
    =================================
    0x2584S0x23fc: v2584V23fc = EXTCODESIZE v2409
    0x2585S0x23fc: v2585V23fc = ISZERO v2584V23fc
    0x2586S0x23fc: v2586V23fc = ISZERO v2585V23fc
    0x2588S0x23fc: JUMP v23fd(0x240e)

    Begin block 0x240e
    prev=[0x2583B0x23fc], succ=[0x2eb7, 0x2414]
    =================================
    0x240f: v240f = ISZERO v2586V23fc
    0x2410: v2410(0x2eb7) = CONST 
    0x2413: JUMPI v2410(0x2eb7), v240f

    Begin block 0x2eb7
    prev=[0x240e], succ=[]
    =================================
    0x2ebe: RETURNPRIVATE v23fcarg6

    Begin block 0x2414
    prev=[0x240e], succ=[0x2485]
    =================================
    0x2415: v2415(0x1) = CONST 
    0x2417: v2417(0x1) = CONST 
    0x2419: v2419(0xa0) = CONST 
    0x241b: v241b(0x10000000000000000000000000000000000000000) = SHL v2419(0xa0), v2417(0x1)
    0x241c: v241c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v241b(0x10000000000000000000000000000000000000000), v2415(0x1)
    0x241d: v241d = AND v241c(0xffffffffffffffffffffffffffffffffffffffff), v23fcarg3
    0x241e: v241e(0xf23a6e61) = CONST 
    0x2428: v2428(0x40) = CONST 
    0x242a: v242a = MLOAD v2428(0x40)
    0x242c: v242c(0xffffffff) = CONST 
    0x2431: v2431(0xf23a6e61) = AND v242c(0xffffffff), v241e(0xf23a6e61)
    0x2432: v2432(0xe0) = CONST 
    0x2434: v2434(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v2432(0xe0), v2431(0xf23a6e61)
    0x2436: MSTORE v242a, v2434(0xf23a6e6100000000000000000000000000000000000000000000000000000000)
    0x2437: v2437(0x4) = CONST 
    0x2439: v2439 = ADD v2437(0x4), v242a
    0x243c: v243c(0x1) = CONST 
    0x243e: v243e(0x1) = CONST 
    0x2440: v2440(0xa0) = CONST 
    0x2442: v2442(0x10000000000000000000000000000000000000000) = SHL v2440(0xa0), v243e(0x1)
    0x2443: v2443(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2442(0x10000000000000000000000000000000000000000), v243c(0x1)
    0x2444: v2444 = AND v2443(0xffffffffffffffffffffffffffffffffffffffff), v23fcarg5
    0x2446: MSTORE v2439, v2444
    0x2447: v2447(0x20) = CONST 
    0x2449: v2449 = ADD v2447(0x20), v2439
    0x244b: v244b(0x1) = CONST 
    0x244d: v244d(0x1) = CONST 
    0x244f: v244f(0xa0) = CONST 
    0x2451: v2451(0x10000000000000000000000000000000000000000) = SHL v244f(0xa0), v244d(0x1)
    0x2452: v2452(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2451(0x10000000000000000000000000000000000000000), v244b(0x1)
    0x2453: v2453 = AND v2452(0xffffffffffffffffffffffffffffffffffffffff), v23fcarg4
    0x2455: MSTORE v2449, v2453
    0x2456: v2456(0x20) = CONST 
    0x2458: v2458 = ADD v2456(0x20), v2449
    0x245b: MSTORE v2458, v23fcarg2
    0x245c: v245c(0x20) = CONST 
    0x245e: v245e = ADD v245c(0x20), v2458
    0x2461: MSTORE v245e, v23fcarg1
    0x2462: v2462(0x20) = CONST 
    0x2464: v2464 = ADD v2462(0x20), v245e
    0x2466: v2466(0x20) = CONST 
    0x2468: v2468 = ADD v2466(0x20), v2464
    0x246b: v246b(0xa0) = SUB v2468, v2439
    0x246d: MSTORE v2464, v246b(0xa0)
    0x2471: v2471 = MLOAD v23fcarg0
    0x2473: MSTORE v2468, v2471
    0x2474: v2474(0x20) = CONST 
    0x2476: v2476 = ADD v2474(0x20), v2468
    0x247a: v247a = MLOAD v23fcarg0
    0x247c: v247c(0x20) = CONST 
    0x247e: v247e = ADD v247c(0x20), v23fcarg0
    0x2483: v2483(0x0) = CONST 

    Begin block 0x2485
    prev=[0x2414, 0x248e], succ=[0x249d, 0x248e]
    =================================
    0x2485_0x0: v2485_0 = PHI v2483(0x0), v2498
    0x2488: v2488 = LT v2485_0, v247a
    0x2489: v2489 = ISZERO v2488
    0x248a: v248a(0x249d) = CONST 
    0x248d: JUMPI v248a(0x249d), v2489

    Begin block 0x249d
    prev=[0x2485], succ=[0x24ca, 0x24b1]
    =================================
    0x24a6: v24a6 = ADD v247a, v2476
    0x24a8: v24a8(0x1f) = CONST 
    0x24aa: v24aa = AND v24a8(0x1f), v247a
    0x24ac: v24ac = ISZERO v24aa
    0x24ad: v24ad(0x24ca) = CONST 
    0x24b0: JUMPI v24ad(0x24ca), v24ac

    Begin block 0x24ca
    prev=[0x249d, 0x24b1], succ=[0x24e9, 0x24ed]
    =================================
    0x24ca_0x1: v24ca_1 = PHI v24a6, v24c7
    0x24d4: v24d4(0x20) = CONST 
    0x24d6: v24d6(0x40) = CONST 
    0x24d8: v24d8 = MLOAD v24d6(0x40)
    0x24db: v24db = SUB v24ca_1, v24d8
    0x24dd: v24dd(0x0) = CONST 
    0x24e1: v24e1 = EXTCODESIZE v241d
    0x24e2: v24e2 = ISZERO v24e1
    0x24e4: v24e4 = ISZERO v24e2
    0x24e5: v24e5(0x24ed) = CONST 
    0x24e8: JUMPI v24e5(0x24ed), v24e4

    Begin block 0x24e9
    prev=[0x24ca], succ=[]
    =================================
    0x24e9: v24e9(0x0) = CONST 
    0x24ec: REVERT v24e9(0x0), v24e9(0x0)

    Begin block 0x24ed
    prev=[0x24ca], succ=[0x2512, 0x24fb]
    =================================
    0x24ef: v24ef = GAS 
    0x24f0: v24f0 = CALL v24ef, v241d, v24dd(0x0), v24d8, v24db, v24d8, v24d4(0x20)
    0x24f6: v24f6 = ISZERO v24f0
    0x24f7: v24f7(0x2512) = CONST 
    0x24fa: JUMPI v24f7(0x2512), v24f6

    Begin block 0x2512
    prev=[0x24ed, 0x250d], succ=[0x2517, 0x251e]
    =================================
    0x2512_0x0: v2512_0 = PHI v24f0, v2510(0x1)
    0x2513: v2513(0x251e) = CONST 
    0x2516: JUMPI v2513(0x251e), v2512_0

    Begin block 0x2517
    prev=[0x2512], succ=[0x1dd40x23fc]
    =================================
    0x2517: v2517(0x1dd4) = CONST 
    0x251a: v251a(0x2630) = CONST 
    0x251d: v251d_0 = CALLPRIVATE v251a(0x2630), v2517(0x1dd4)

    Begin block 0x1dd40x23fc
    prev=[0x2517], succ=[0x1dda0x23fc, 0x1ddf0x23fc]
    =================================
    0x1dd60x23fc: v23fc1dd6(0x1ddf) = CONST 
    0x1dd90x23fc: JUMPI v23fc1dd6(0x1ddf), v251d_0

    Begin block 0x1dda0x23fc
    prev=[0x1dd40x23fc], succ=[0x1e640x23fc]
    =================================
    0x1ddb0x23fc: v23fc1ddb(0x1e64) = CONST 
    0x1dde0x23fc: JUMP v23fc1ddb(0x1e64)

    Begin block 0x1e640x23fc
    prev=[0x1dda0x23fc], succ=[]
    =================================
    0x1e650x23fc: v23fc1e65(0x40) = CONST 
    0x1e670x23fc: v23fc1e67 = MLOAD v23fc1e65(0x40)
    0x1e680x23fc: v23fc1e68(0x461bcd) = CONST 
    0x1e6c0x23fc: v23fc1e6c(0xe5) = CONST 
    0x1e6e0x23fc: v23fc1e6e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v23fc1e6c(0xe5), v23fc1e68(0x461bcd)
    0x1e700x23fc: MSTORE v23fc1e67, v23fc1e6e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e710x23fc: v23fc1e71(0x4) = CONST 
    0x1e730x23fc: v23fc1e73 = ADD v23fc1e71(0x4), v23fc1e67
    0x1e760x23fc: v23fc1e76(0x20) = CONST 
    0x1e780x23fc: v23fc1e78 = ADD v23fc1e76(0x20), v23fc1e73
    0x1e7b0x23fc: v23fc1e7b(0x20) = SUB v23fc1e78, v23fc1e73
    0x1e7d0x23fc: MSTORE v23fc1e73, v23fc1e7b(0x20)
    0x1e7e0x23fc: v23fc1e7e(0x2b) = CONST 
    0x1e810x23fc: MSTORE v23fc1e78, v23fc1e7e(0x2b)
    0x1e820x23fc: v23fc1e82(0x20) = CONST 
    0x1e840x23fc: v23fc1e84 = ADD v23fc1e82(0x20), v23fc1e78
    0x1e860x23fc: v23fc1e86(0x26d7) = CONST 
    0x1e890x23fc: v23fc1e89(0x2b) = CONST 
    0x1e8c0x23fc: CODECOPY v23fc1e84, v23fc1e86(0x26d7), v23fc1e89(0x2b)
    0x1e8d0x23fc: v23fc1e8d(0x40) = CONST 
    0x1e8f0x23fc: v23fc1e8f = ADD v23fc1e8d(0x40), v23fc1e84
    0x1e930x23fc: v23fc1e93(0x40) = CONST 
    0x1e950x23fc: v23fc1e95 = MLOAD v23fc1e93(0x40)
    0x1e980x23fc: v23fc1e98(0x84) = SUB v23fc1e8f, v23fc1e95
    0x1e9a0x23fc: REVERT v23fc1e95, v23fc1e98(0x84)

    Begin block 0x1ddf0x23fc
    prev=[0x1dd40x23fc], succ=[0x1e110x23fc]
    =================================
    0x1de10x23fc: v23fc1de1(0x40) = CONST 
    0x1de30x23fc: v23fc1de3 = MLOAD v23fc1de1(0x40)
    0x1de40x23fc: v23fc1de4(0x461bcd) = CONST 
    0x1de80x23fc: v23fc1de8(0xe5) = CONST 
    0x1dea0x23fc: v23fc1dea(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v23fc1de8(0xe5), v23fc1de4(0x461bcd)
    0x1dec0x23fc: MSTORE v23fc1de3, v23fc1dea(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ded0x23fc: v23fc1ded(0x4) = CONST 
    0x1def0x23fc: v23fc1def = ADD v23fc1ded(0x4), v23fc1de3
    0x1df20x23fc: v23fc1df2(0x20) = CONST 
    0x1df40x23fc: v23fc1df4 = ADD v23fc1df2(0x20), v23fc1def
    0x1df70x23fc: v23fc1df7(0x20) = SUB v23fc1df4, v23fc1def
    0x1df90x23fc: MSTORE v23fc1def, v23fc1df7(0x20)
    0x1dfd0x23fc: v23fc1dfd = MLOAD v251d_0
    0x1dff0x23fc: MSTORE v23fc1df4, v23fc1dfd
    0x1e000x23fc: v23fc1e00(0x20) = CONST 
    0x1e020x23fc: v23fc1e02 = ADD v23fc1e00(0x20), v23fc1df4
    0x1e060x23fc: v23fc1e06 = MLOAD v251d_0
    0x1e080x23fc: v23fc1e08(0x20) = CONST 
    0x1e0a0x23fc: v23fc1e0a = ADD v23fc1e08(0x20), v251d_0
    0x1e0f0x23fc: v23fc1e0f(0x0) = CONST 

    Begin block 0x1e110x23fc
    prev=[0x1e1a0x23fc, 0x1ddf0x23fc], succ=[0x1e290x23fc, 0x1e1a0x23fc]
    =================================
    0x1e110x23fc_0x0: v1e1123fc_0 = PHI v23fc1e24, v23fc1e0f(0x0)
    0x1e140x23fc: v23fc1e14 = LT v1e1123fc_0, v23fc1e06
    0x1e150x23fc: v23fc1e15 = ISZERO v23fc1e14
    0x1e160x23fc: v23fc1e16(0x1e29) = CONST 
    0x1e190x23fc: JUMPI v23fc1e16(0x1e29), v23fc1e15

    Begin block 0x1e290x23fc
    prev=[0x1e110x23fc], succ=[0x1e560x23fc, 0x1e3d0x23fc]
    =================================
    0x1e320x23fc: v23fc1e32 = ADD v23fc1e06, v23fc1e02
    0x1e340x23fc: v23fc1e34(0x1f) = CONST 
    0x1e360x23fc: v23fc1e36 = AND v23fc1e34(0x1f), v23fc1e06
    0x1e380x23fc: v23fc1e38 = ISZERO v23fc1e36
    0x1e390x23fc: v23fc1e39(0x1e56) = CONST 
    0x1e3c0x23fc: JUMPI v23fc1e39(0x1e56), v23fc1e38

    Begin block 0x1e560x23fc
    prev=[0x1e290x23fc, 0x1e3d0x23fc], succ=[]
    =================================
    0x1e560x23fc_0x1: v1e5623fc_1 = PHI v23fc1e53, v23fc1e32
    0x1e5c0x23fc: v23fc1e5c(0x40) = CONST 
    0x1e5e0x23fc: v23fc1e5e = MLOAD v23fc1e5c(0x40)
    0x1e610x23fc: v23fc1e61 = SUB v1e5623fc_1, v23fc1e5e
    0x1e630x23fc: REVERT v23fc1e5e, v23fc1e61

    Begin block 0x1e3d0x23fc
    prev=[0x1e290x23fc], succ=[0x1e560x23fc]
    =================================
    0x1e3f0x23fc: v23fc1e3f = SUB v23fc1e32, v23fc1e36
    0x1e410x23fc: v23fc1e41 = MLOAD v23fc1e3f
    0x1e420x23fc: v23fc1e42(0x1) = CONST 
    0x1e450x23fc: v23fc1e45(0x20) = CONST 
    0x1e470x23fc: v23fc1e47 = SUB v23fc1e45(0x20), v23fc1e36
    0x1e480x23fc: v23fc1e48(0x100) = CONST 
    0x1e4b0x23fc: v23fc1e4b = EXP v23fc1e48(0x100), v23fc1e47
    0x1e4c0x23fc: v23fc1e4c = SUB v23fc1e4b, v23fc1e42(0x1)
    0x1e4d0x23fc: v23fc1e4d = NOT v23fc1e4c
    0x1e4e0x23fc: v23fc1e4e = AND v23fc1e4d, v23fc1e41
    0x1e500x23fc: MSTORE v23fc1e3f, v23fc1e4e
    0x1e510x23fc: v23fc1e51(0x20) = CONST 
    0x1e530x23fc: v23fc1e53 = ADD v23fc1e51(0x20), v23fc1e3f

    Begin block 0x1e1a0x23fc
    prev=[0x1e110x23fc], succ=[0x1e110x23fc]
    =================================
    0x1e1a0x23fc_0x0: v1e1a23fc_0 = PHI v23fc1e24, v23fc1e0f(0x0)
    0x1e1c0x23fc: v23fc1e1c = ADD v1e1a23fc_0, v23fc1e0a
    0x1e1d0x23fc: v23fc1e1d = MLOAD v23fc1e1c
    0x1e200x23fc: v23fc1e20 = ADD v1e1a23fc_0, v23fc1e02
    0x1e210x23fc: MSTORE v23fc1e20, v23fc1e1d
    0x1e220x23fc: v23fc1e22(0x20) = CONST 
    0x1e240x23fc: v23fc1e24 = ADD v23fc1e22(0x20), v1e1a23fc_0
    0x1e250x23fc: v23fc1e25(0x1e11) = CONST 
    0x1e280x23fc: JUMP v23fc1e25(0x1e11)

    Begin block 0x251e
    prev=[0x2512], succ=[0x2537, 0x1f000x23fc]
    =================================
    0x251e_0x0: v251e_0 = PHI v250f, v23fcarg0
    0x251f: v251f(0x1) = CONST 
    0x2521: v2521(0x1) = CONST 
    0x2523: v2523(0xe0) = CONST 
    0x2525: v2525(0x100000000000000000000000000000000000000000000000000000000) = SHL v2523(0xe0), v2521(0x1)
    0x2526: v2526(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2525(0x100000000000000000000000000000000000000000000000000000000), v251f(0x1)
    0x2527: v2527(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2526(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2529: v2529 = AND v251e_0, v2527(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x252a: v252a(0xf23a6e61) = CONST 
    0x252f: v252f(0xe0) = CONST 
    0x2531: v2531(0xf23a6e6100000000000000000000000000000000000000000000000000000000) = SHL v252f(0xe0), v252a(0xf23a6e61)
    0x2532: v2532 = EQ v2531(0xf23a6e6100000000000000000000000000000000000000000000000000000000), v2529
    0x2533: v2533(0x1f00) = CONST 
    0x2536: JUMPI v2533(0x1f00), v2532

    Begin block 0x2537
    prev=[0x251e], succ=[]
    =================================
    0x2537: v2537(0x40) = CONST 
    0x253a: v253a = MLOAD v2537(0x40)
    0x253b: v253b(0x461bcd) = CONST 
    0x253f: v253f(0xe5) = CONST 
    0x2541: v2541(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v253f(0xe5), v253b(0x461bcd)
    0x2543: MSTORE v253a, v2541(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2544: v2544(0x20) = CONST 
    0x2546: v2546(0x4) = CONST 
    0x2549: v2549 = ADD v253a, v2546(0x4)
    0x254a: MSTORE v2549, v2544(0x20)
    0x254b: v254b(0x1f) = CONST 
    0x254d: v254d(0x24) = CONST 
    0x2550: v2550 = ADD v253a, v254d(0x24)
    0x2551: MSTORE v2550, v254b(0x1f)
    0x2552: v2552(0x4552433131353552656365697665722072656a656374656420746f6b656e7300) = CONST 
    0x2573: v2573(0x44) = CONST 
    0x2576: v2576 = ADD v253a, v2573(0x44)
    0x2577: MSTORE v2576, v2552(0x4552433131353552656365697665722072656a656374656420746f6b656e7300)
    0x2579: v2579 = MLOAD v2537(0x40)
    0x257d: v257d(0x0) = SUB v253a, v2579
    0x257e: v257e(0x64) = CONST 
    0x2580: v2580(0x64) = ADD v257e(0x64), v257d(0x0)
    0x2582: REVERT v2579, v2580(0x64)

    Begin block 0x1f000x23fc
    prev=[0x251e], succ=[0x1f020x23fc]
    =================================

    Begin block 0x1f020x23fc
    prev=[0x1f000x23fc], succ=[]
    =================================
    0x1f090x23fc: RETURNPRIVATE v23fcarg6

    Begin block 0x24fb
    prev=[0x24ed], succ=[0x2509, 0x250d]
    =================================
    0x24fc: v24fc(0x40) = CONST 
    0x24fe: v24fe = MLOAD v24fc(0x40)
    0x24ff: v24ff = RETURNDATASIZE 
    0x2500: v2500(0x20) = CONST 
    0x2503: v2503 = LT v24ff, v2500(0x20)
    0x2504: v2504 = ISZERO v2503
    0x2505: v2505(0x250d) = CONST 
    0x2508: JUMPI v2505(0x250d), v2504

    Begin block 0x2509
    prev=[0x24fb], succ=[]
    =================================
    0x2509: v2509(0x0) = CONST 
    0x250c: REVERT v2509(0x0), v2509(0x0)

    Begin block 0x250d
    prev=[0x24fb], succ=[0x2512]
    =================================
    0x250f: v250f = MLOAD v24fe
    0x2510: v2510(0x1) = CONST 

    Begin block 0x24b1
    prev=[0x249d], succ=[0x24ca]
    =================================
    0x24b3: v24b3 = SUB v24a6, v24aa
    0x24b5: v24b5 = MLOAD v24b3
    0x24b6: v24b6(0x1) = CONST 
    0x24b9: v24b9(0x20) = CONST 
    0x24bb: v24bb = SUB v24b9(0x20), v24aa
    0x24bc: v24bc(0x100) = CONST 
    0x24bf: v24bf = EXP v24bc(0x100), v24bb
    0x24c0: v24c0 = SUB v24bf, v24b6(0x1)
    0x24c1: v24c1 = NOT v24c0
    0x24c2: v24c2 = AND v24c1, v24b5
    0x24c4: MSTORE v24b3, v24c2
    0x24c5: v24c5(0x20) = CONST 
    0x24c7: v24c7 = ADD v24c5(0x20), v24b3

    Begin block 0x248e
    prev=[0x2485], succ=[0x2485]
    =================================
    0x248e_0x0: v248e_0 = PHI v2483(0x0), v2498
    0x2490: v2490 = ADD v248e_0, v247e
    0x2491: v2491 = MLOAD v2490
    0x2494: v2494 = ADD v248e_0, v2476
    0x2495: MSTORE v2494, v2491
    0x2496: v2496(0x20) = CONST 
    0x2498: v2498 = ADD v2496(0x20), v248e_0
    0x2499: v2499(0x2485) = CONST 
    0x249c: JUMP v2499(0x2485)

}

function 0x2630(0x2630arg0x0) private {
    Begin block 0x2630
    prev=[], succ=[0x263c, 0x2640]
    =================================
    0x2631: v2631(0x0) = CONST 
    0x2633: v2633(0x44) = CONST 
    0x2635: v2635 = RETURNDATASIZE 
    0x2636: v2636 = LT v2635, v2633(0x44)
    0x2637: v2637 = ISZERO v2636
    0x2638: v2638(0x2640) = CONST 
    0x263b: JUMPI v2638(0x2640), v2637

    Begin block 0x263c
    prev=[0x2630], succ=[0x2f24]
    =================================
    0x263c: v263c(0x2f24) = CONST 
    0x263f: JUMP v263c(0x2f24)

    Begin block 0x2f24
    prev=[0x263c], succ=[]
    =================================
    0x2f26: RETURNPRIVATE v2630arg0, v2631(0x0)

    Begin block 0x2640
    prev=[0x2630], succ=[0x262a]
    =================================
    0x2641: v2641(0x4) = CONST 
    0x2645: RETURNDATACOPY v2631(0x0), v2631(0x0), v2641(0x4)
    0x2646: v2646(0x8c379a0) = CONST 
    0x264b: v264b(0x2654) = CONST 
    0x264f: v264f = MLOAD v2631(0x0)
    0x2650: v2650(0x262a) = CONST 
    0x2653: JUMP v2650(0x262a)

    Begin block 0x262a
    prev=[0x2640], succ=[0x2654]
    =================================
    0x262b: v262b(0xe0) = CONST 
    0x262d: v262d = SHR v262b(0xe0), v264f
    0x262f: JUMP v264b(0x2654)

    Begin block 0x2654
    prev=[0x262a], succ=[0x265a, 0x265e]
    =================================
    0x2655: v2655 = EQ v262d, v2646(0x8c379a0)
    0x2656: v2656(0x265e) = CONST 
    0x2659: JUMPI v2656(0x265e), v2655

    Begin block 0x265a
    prev=[0x2654], succ=[0x2f46]
    =================================
    0x265a: v265a(0x2f46) = CONST 
    0x265d: JUMP v265a(0x2f46)

    Begin block 0x2f46
    prev=[0x265a], succ=[]
    =================================
    0x2f48: RETURNPRIVATE v2630arg0, v2631(0x0)

    Begin block 0x265e
    prev=[0x2654], succ=[0x268e, 0x2686]
    =================================
    0x265f: v265f(0x40) = CONST 
    0x2661: v2661 = MLOAD v265f(0x40)
    0x2662: v2662 = RETURNDATASIZE 
    0x2663: v2663(0x3) = CONST 
    0x2665: v2665(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc) = NOT v2663(0x3)
    0x2666: v2666 = ADD v2665(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc), v2662
    0x2667: v2667(0x4) = CONST 
    0x266a: RETURNDATACOPY v2661, v2667(0x4), v2666
    0x266c: v266c = MLOAD v2661
    0x266d: v266d = RETURNDATASIZE 
    0x266e: v266e(0xffffffffffffffff) = CONST 
    0x2678: v2678(0x24) = CONST 
    0x267b: v267b = ADD v266c, v2678(0x24)
    0x267c: v267c = GT v267b, v266d
    0x267f: v267f = GT v266c, v266e(0xffffffffffffffff)
    0x2680: v2680 = OR v267f, v267c
    0x2681: v2681 = ISZERO v2680
    0x2682: v2682(0x268e) = CONST 
    0x2685: JUMPI v2682(0x268e), v2681

    Begin block 0x268e
    prev=[0x265e], succ=[0x26a8, 0x26a0]
    =================================
    0x2691: v2691 = ADD v2661, v266c
    0x2695: v2695 = MLOAD v2691
    0x269a: v269a = GT v2695, v266e(0xffffffffffffffff)
    0x269b: v269b = ISZERO v269a
    0x269c: v269c(0x26a8) = CONST 
    0x269f: JUMPI v269c(0x26a8), v269b

    Begin block 0x26a8
    prev=[0x268e], succ=[0x26c0, 0x26b9]
    =================================
    0x26aa: v26aa = RETURNDATASIZE 
    0x26ac: v26ac = ADD v2661, v26aa
    0x26ad: v26ad(0x20) = CONST 
    0x26b1: v26b1 = ADD v2691, v2695
    0x26b2: v26b2 = ADD v26b1, v26ad(0x20)
    0x26b3: v26b3 = GT v26b2, v26ac
    0x26b4: v26b4 = ISZERO v26b3
    0x26b5: v26b5(0x26c0) = CONST 
    0x26b8: JUMPI v26b5(0x26c0), v26b4

    Begin block 0x26c0
    prev=[0x26a8], succ=[0x26d3]
    =================================
    0x26c1: v26c1(0x1f) = CONST 
    0x26c3: v26c3 = ADD v26c1(0x1f), v2695
    0x26c4: v26c4(0x1f) = CONST 
    0x26c6: v26c6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v26c4(0x1f)
    0x26c7: v26c7 = AND v26c6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v26c3
    0x26c9: v26c9 = ADD v2691, v26c7
    0x26ca: v26ca(0x20) = CONST 
    0x26cc: v26cc = ADD v26ca(0x20), v26c9
    0x26cd: v26cd(0x40) = CONST 
    0x26cf: MSTORE v26cd(0x40), v26cc

    Begin block 0x26d3
    prev=[0x26c0], succ=[]
    =================================
    0x26d5: RETURNPRIVATE v2630arg0, v2691

    Begin block 0x26b9
    prev=[0x26a8], succ=[0x2fac]
    =================================
    0x26bc: v26bc(0x2fac) = CONST 
    0x26bf: JUMP v26bc(0x2fac)

    Begin block 0x2fac
    prev=[0x26b9], succ=[]
    =================================
    0x2fae: RETURNPRIVATE v2630arg0, v2631(0x0)

    Begin block 0x26a0
    prev=[0x268e], succ=[0x2f8a]
    =================================
    0x26a4: v26a4(0x2f8a) = CONST 
    0x26a7: JUMP v26a4(0x2f8a)

    Begin block 0x2f8a
    prev=[0x26a0], succ=[]
    =================================
    0x2f8c: RETURNPRIVATE v2630arg0, v2631(0x0)

    Begin block 0x2686
    prev=[0x265e], succ=[0x2f68]
    =================================
    0x268a: v268a(0x2f68) = CONST 
    0x268d: JUMP v268a(0x2f68)

    Begin block 0x2f68
    prev=[0x2686], succ=[]
    =================================
    0x2f6a: RETURNPRIVATE v2630arg0, v2631(0x0)

}

function uri(uint256)() public {
    Begin block 0x27b
    prev=[], succ=[0x28d, 0x291]
    =================================
    0x27c: v27c(0x298) = CONST 
    0x27f: v27f(0x4) = CONST 
    0x282: v282 = CALLDATASIZE 
    0x283: v283 = SUB v282, v27f(0x4)
    0x284: v284(0x20) = CONST 
    0x287: v287 = LT v283, v284(0x20)
    0x288: v288 = ISZERO v287
    0x289: v289(0x291) = CONST 
    0x28c: JUMPI v289(0x291), v288

    Begin block 0x28d
    prev=[0x27b], succ=[]
    =================================
    0x28d: v28d(0x0) = CONST 
    0x290: REVERT v28d(0x0), v28d(0x0)

    Begin block 0x291
    prev=[0x27b], succ=[0xaca]
    =================================
    0x293: v293 = CALLDATALOAD v27f(0x4)
    0x294: v294(0xaca) = CONST 
    0x297: JUMP v294(0xaca)

    Begin block 0xaca
    prev=[0x291], succ=[0xad7, 0xb23]
    =================================
    0xacb: vacb(0x60) = CONST 
    0xacd: vacd(0x6) = CONST 
    0xacf: vacf = SLOAD vacd(0x6)
    0xad1: vad1 = GT v293, vacf
    0xad2: vad2 = ISZERO vad1
    0xad3: vad3(0xb23) = CONST 
    0xad6: JUMPI vad3(0xb23), vad2

    Begin block 0xad7
    prev=[0xaca], succ=[]
    =================================
    0xad7: vad7(0x40) = CONST 
    0xada: vada = MLOAD vad7(0x40)
    0xadb: vadb(0x461bcd) = CONST 
    0xadf: vadf(0xe5) = CONST 
    0xae1: vae1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vadf(0xe5), vadb(0x461bcd)
    0xae3: MSTORE vada, vae1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xae4: vae4(0x20) = CONST 
    0xae6: vae6(0x4) = CONST 
    0xae9: vae9 = ADD vada, vae6(0x4)
    0xaea: MSTORE vae9, vae4(0x20)
    0xaeb: vaeb(0x17) = CONST 
    0xaed: vaed(0x24) = CONST 
    0xaf0: vaf0 = ADD vada, vaed(0x24)
    0xaf1: MSTORE vaf0, vaeb(0x17)
    0xaf2: vaf2(0x53746172206e667420646f6573206e6f74206578697374000000000000000000) = CONST 
    0xb13: vb13(0x44) = CONST 
    0xb16: vb16 = ADD vada, vb13(0x44)
    0xb17: MSTORE vb16, vaf2(0x53746172206e667420646f6573206e6f74206578697374000000000000000000)
    0xb19: vb19 = MLOAD vad7(0x40)
    0xb1d: vb1d(0x0) = SUB vada, vb19
    0xb1e: vb1e(0x64) = CONST 
    0xb20: vb20(0x64) = ADD vb1e(0x64), vb1d(0x0)
    0xb22: REVERT vb19, vb20(0x64)

    Begin block 0xb23
    prev=[0xaca], succ=[0xb4f, 0xb3b]
    =================================
    0xb24: vb24(0x2) = CONST 
    0xb27: vb27 = SLOAD vb24(0x2)
    0xb28: vb28(0x0) = CONST 
    0xb2a: vb2a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vb28(0x0)
    0xb2b: vb2b(0x100) = CONST 
    0xb2e: vb2e(0x1) = CONST 
    0xb31: vb31 = AND vb27, vb2e(0x1)
    0xb32: vb32 = ISZERO vb31
    0xb33: vb33 = MUL vb32, vb2b(0x100)
    0xb34: vb34 = ADD vb33, vb2a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xb35: vb35 = AND vb34, vb27
    0xb36: vb36 = DIV vb35, vb24(0x2)
    0xb37: vb37(0xb4f) = CONST 
    0xb3a: JUMPI vb37(0xb4f), vb36

    Begin block 0xb4f
    prev=[0xb23], succ=[0xb5a]
    =================================
    0xb50: vb50(0x2) = CONST 
    0xb52: vb52(0xb5a) = CONST 
    0xb56: vb56(0x1b54) = CONST 
    0xb59: vb59_0 = CALLPRIVATE vb56(0x1b54), v293, vb52(0xb5a)

    Begin block 0xb5a
    prev=[0xb4f], succ=[0xbb8, 0xb7c]
    =================================
    0xb5b: vb5b(0x40) = CONST 
    0xb5d: vb5d = MLOAD vb5b(0x40)
    0xb5e: vb5e(0x20) = CONST 
    0xb60: vb60 = ADD vb5e(0x20), vb5d
    0xb64: vb64 = SLOAD vb50(0x2)
    0xb65: vb65(0x1) = CONST 
    0xb68: vb68(0x1) = CONST 
    0xb6a: vb6a = AND vb68(0x1), vb64
    0xb6b: vb6b = ISZERO vb6a
    0xb6c: vb6c(0x100) = CONST 
    0xb6f: vb6f = MUL vb6c(0x100), vb6b
    0xb70: vb70 = SUB vb6f, vb65(0x1)
    0xb71: vb71 = AND vb70, vb64
    0xb72: vb72(0x2) = CONST 
    0xb75: vb75 = DIV vb71, vb72(0x2)
    0xb77: vb77 = ISZERO vb75
    0xb78: vb78(0xbb8) = CONST 
    0xb7b: JUMPI vb78(0xbb8), vb77

    Begin block 0xbb8
    prev=[0xb84, 0xb5a, 0xba4], succ=[0xbc5]
    =================================
    0xbbc: vbbc = MLOAD vb59_0
    0xbbd: vbbd(0x20) = CONST 
    0xbc0: vbc0 = ADD vb59_0, vbbd(0x20)

    Begin block 0xbc5
    prev=[0xbb8, 0xbce], succ=[0xbe4, 0xbce]
    =================================
    0xbc5_0x2: vbc5_2 = PHI vbbc, vbd7
    0xbc6: vbc6(0x20) = CONST 
    0xbc9: vbc9 = LT vbc5_2, vbc6(0x20)
    0xbca: vbca(0xbe4) = CONST 
    0xbcd: JUMPI vbca(0xbe4), vbc9

    Begin block 0xbe4
    prev=[0xbc5], succ=[0x2cf5]
    =================================
    0xbe4_0x0: vbe4_0 = PHI vbc0, vbdf
    0xbe4_0x1: vbe4_1 = PHI vb60, vb90, vb98, vbdd
    0xbe4_0x2: vbe4_2 = PHI vbbc, vbd7
    0xbe4_0x5: vbe4_5 = PHI vb60, vb90, vb98
    0xbe5: vbe5(0x1) = CONST 
    0xbe8: vbe8(0x20) = CONST 
    0xbea: vbea = SUB vbe8(0x20), vbe4_2
    0xbeb: vbeb(0x100) = CONST 
    0xbee: vbee = EXP vbeb(0x100), vbea
    0xbef: vbef = SUB vbee, vbe5(0x1)
    0xbf1: vbf1 = NOT vbef
    0xbf3: vbf3 = MLOAD vbe4_0
    0xbf4: vbf4 = AND vbf3, vbf1
    0xbf7: vbf7 = MLOAD vbe4_1
    0xbf8: vbf8 = AND vbf7, vbef
    0xbfb: vbfb = OR vbf4, vbf8
    0xbfd: MSTORE vbe4_1, vbfb
    0xc06: vc06 = ADD vbbc, vbe4_5
    0xc08: vc08(0x173539b7b7) = CONST 
    0xc0e: vc0e(0xd9) = CONST 
    0xc10: vc10(0x2e6a736f6e000000000000000000000000000000000000000000000000000000) = SHL vc0e(0xd9), vc08(0x173539b7b7)
    0xc12: MSTORE vc06, vc10(0x2e6a736f6e000000000000000000000000000000000000000000000000000000)
    0xc14: vc14(0x5) = CONST 
    0xc16: vc16 = ADD vc14(0x5), vc06
    0xc1b: vc1b(0x40) = CONST 
    0xc1d: vc1d = MLOAD vc1b(0x40)
    0xc1e: vc1e(0x20) = CONST 
    0xc22: vc22 = SUB vc16, vc1d
    0xc23: vc23 = SUB vc22, vc1e(0x20)
    0xc25: MSTORE vc1d, vc23
    0xc27: vc27(0x40) = CONST 
    0xc29: MSTORE vc27(0x40), vc16
    0xc2c: vc2c(0x2cf5) = CONST 
    0xc2f: JUMP vc2c(0x2cf5)

    Begin block 0x2cf5
    prev=[0xbe4], succ=[0x2980x27b]
    =================================
    0x2cf9: JUMP v27c(0x298)

    Begin block 0x2980x27b
    prev=[0x2cd1, 0x2cf5], succ=[0x2ba0x27b]
    =================================
    0x2980x27b_0x0: v29827b_0 = PHI vb3f, vc1d
    0x2990x27b: v27b299(0x40) = CONST 
    0x29c0x27b: v27b29c = MLOAD v27b299(0x40)
    0x29d0x27b: v27b29d(0x20) = CONST 
    0x2a10x27b: MSTORE v27b29c, v27b29d(0x20)
    0x2a30x27b: v27b2a3 = MLOAD v29827b_0
    0x2a60x27b: v27b2a6 = ADD v27b29c, v27b29d(0x20)
    0x2a70x27b: MSTORE v27b2a6, v27b2a3
    0x2a90x27b: v27b2a9 = MLOAD v29827b_0
    0x2b00x27b: v27b2b0 = ADD v27b29c, v27b299(0x40)
    0x2b30x27b: v27b2b3 = ADD v29827b_0, v27b29d(0x20)
    0x2b80x27b: v27b2b8(0x0) = CONST 

    Begin block 0x2ba0x27b
    prev=[0x2c30x27b, 0x2980x27b], succ=[0x2d20x27b, 0x2c30x27b]
    =================================
    0x2ba0x27b_0x0: v2ba27b_0 = PHI v27b2cd, v27b2b8(0x0)
    0x2bd0x27b: v27b2bd = LT v2ba27b_0, v27b2a9
    0x2be0x27b: v27b2be = ISZERO v27b2bd
    0x2bf0x27b: v27b2bf(0x2d2) = CONST 
    0x2c20x27b: JUMPI v27b2bf(0x2d2), v27b2be

    Begin block 0x2d20x27b
    prev=[0x2ba0x27b], succ=[0x2ff0x27b, 0x2e60x27b]
    =================================
    0x2db0x27b: v27b2db = ADD v27b2a9, v27b2b0
    0x2dd0x27b: v27b2dd(0x1f) = CONST 
    0x2df0x27b: v27b2df = AND v27b2dd(0x1f), v27b2a9
    0x2e10x27b: v27b2e1 = ISZERO v27b2df
    0x2e20x27b: v27b2e2(0x2ff) = CONST 
    0x2e50x27b: JUMPI v27b2e2(0x2ff), v27b2e1

    Begin block 0x2ff0x27b
    prev=[0x2d20x27b, 0x2e60x27b], succ=[]
    =================================
    0x2ff0x27b_0x1: v2ff27b_1 = PHI v27b2fc, v27b2db
    0x3050x27b: v27b305(0x40) = CONST 
    0x3070x27b: v27b307 = MLOAD v27b305(0x40)
    0x30a0x27b: v27b30a = SUB v2ff27b_1, v27b307
    0x30c0x27b: RETURN v27b307, v27b30a

    Begin block 0x2e60x27b
    prev=[0x2d20x27b], succ=[0x2ff0x27b]
    =================================
    0x2e80x27b: v27b2e8 = SUB v27b2db, v27b2df
    0x2ea0x27b: v27b2ea = MLOAD v27b2e8
    0x2eb0x27b: v27b2eb(0x1) = CONST 
    0x2ee0x27b: v27b2ee(0x20) = CONST 
    0x2f00x27b: v27b2f0 = SUB v27b2ee(0x20), v27b2df
    0x2f10x27b: v27b2f1(0x100) = CONST 
    0x2f40x27b: v27b2f4 = EXP v27b2f1(0x100), v27b2f0
    0x2f50x27b: v27b2f5 = SUB v27b2f4, v27b2eb(0x1)
    0x2f60x27b: v27b2f6 = NOT v27b2f5
    0x2f70x27b: v27b2f7 = AND v27b2f6, v27b2ea
    0x2f90x27b: MSTORE v27b2e8, v27b2f7
    0x2fa0x27b: v27b2fa(0x20) = CONST 
    0x2fc0x27b: v27b2fc = ADD v27b2fa(0x20), v27b2e8

    Begin block 0x2c30x27b
    prev=[0x2ba0x27b], succ=[0x2ba0x27b]
    =================================
    0x2c30x27b_0x0: v2c327b_0 = PHI v27b2cd, v27b2b8(0x0)
    0x2c50x27b: v27b2c5 = ADD v2c327b_0, v27b2b3
    0x2c60x27b: v27b2c6 = MLOAD v27b2c5
    0x2c90x27b: v27b2c9 = ADD v2c327b_0, v27b2b0
    0x2ca0x27b: MSTORE v27b2c9, v27b2c6
    0x2cb0x27b: v27b2cb(0x20) = CONST 
    0x2cd0x27b: v27b2cd = ADD v27b2cb(0x20), v2c327b_0
    0x2ce0x27b: v27b2ce(0x2ba) = CONST 
    0x2d10x27b: JUMP v27b2ce(0x2ba)

    Begin block 0xbce
    prev=[0xbc5], succ=[0xbc5]
    =================================
    0xbce_0x0: vbce_0 = PHI vbc0, vbdf
    0xbce_0x1: vbce_1 = PHI vb60, vb90, vb98, vbdd
    0xbce_0x2: vbce_2 = PHI vbbc, vbd7
    0xbcf: vbcf = MLOAD vbce_0
    0xbd1: MSTORE vbce_1, vbcf
    0xbd2: vbd2(0x1f) = CONST 
    0xbd4: vbd4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vbd2(0x1f)
    0xbd7: vbd7 = ADD vbce_2, vbd4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xbd9: vbd9(0x20) = CONST 
    0xbdd: vbdd = ADD vbd9(0x20), vbce_1
    0xbdf: vbdf = ADD vbd9(0x20), vbce_0
    0xbe0: vbe0(0xbc5) = CONST 
    0xbe3: JUMP vbe0(0xbc5)

    Begin block 0xb7c
    prev=[0xb5a], succ=[0xb84, 0xb96]
    =================================
    0xb7d: vb7d(0x1f) = CONST 
    0xb7f: vb7f = LT vb7d(0x1f), vb75
    0xb80: vb80(0xb96) = CONST 
    0xb83: JUMPI vb80(0xb96), vb7f

    Begin block 0xb84
    prev=[0xb7c], succ=[0xbb8]
    =================================
    0xb84: vb84(0x100) = CONST 
    0xb89: vb89 = SLOAD vb50(0x2)
    0xb8a: vb8a = DIV vb89, vb84(0x100)
    0xb8b: vb8b = MUL vb8a, vb84(0x100)
    0xb8d: MSTORE vb60, vb8b
    0xb90: vb90 = ADD vb75, vb60
    0xb92: vb92(0xbb8) = CONST 
    0xb95: JUMP vb92(0xbb8)

    Begin block 0xb96
    prev=[0xb7c], succ=[0xba4]
    =================================
    0xb98: vb98 = ADD vb60, vb75
    0xb9b: vb9b(0x0) = CONST 
    0xb9d: MSTORE vb9b(0x0), vb50(0x2)
    0xb9e: vb9e(0x20) = CONST 
    0xba0: vba0(0x0) = CONST 
    0xba2: vba2 = SHA3 vba0(0x0), vb9e(0x20)

    Begin block 0xba4
    prev=[0xb96, 0xba4], succ=[0xbb8, 0xba4]
    =================================
    0xba4_0x0: vba4_0 = PHI vb60, vbb0
    0xba4_0x1: vba4_1 = PHI vba2, vbac
    0xba6: vba6 = SLOAD vba4_1
    0xba8: MSTORE vba4_0, vba6
    0xbaa: vbaa(0x1) = CONST 
    0xbac: vbac = ADD vbaa(0x1), vba4_1
    0xbae: vbae(0x20) = CONST 
    0xbb0: vbb0 = ADD vbae(0x20), vba4_0
    0xbb3: vbb3 = GT vb98, vbb0
    0xbb4: vbb4(0xba4) = CONST 
    0xbb7: JUMPI vbb4(0xba4), vbb3

    Begin block 0xb3b
    prev=[0xb23], succ=[0x2cd1]
    =================================
    0xb3c: vb3c(0x40) = CONST 
    0xb3f: vb3f = MLOAD vb3c(0x40)
    0xb40: vb40(0x20) = CONST 
    0xb43: vb43 = ADD vb3f, vb40(0x20)
    0xb46: MSTORE vb3c(0x40), vb43
    0xb47: vb47(0x0) = CONST 
    0xb4a: MSTORE vb3f, vb47(0x0)
    0xb4b: vb4b(0x2cd1) = CONST 
    0xb4e: JUMP vb4b(0x2cd1)

    Begin block 0x2cd1
    prev=[0xb3b], succ=[0x2980x27b]
    =================================
    0x2cd5: JUMP v27c(0x298)

}

function fallback()() public {
    Begin block 0x28b7
    prev=[], succ=[]
    =================================
    0x28b8: v28b8(0x0) = CONST 
    0x28bb: REVERT v28b8(0x0), v28b8(0x0)

}

function initialized()() public {
    Begin block 0x30d
    prev=[], succ=[0xc30]
    =================================
    0x30e: v30e(0x29cc) = CONST 
    0x311: v311(0xc30) = CONST 
    0x314: JUMP v311(0xc30)

    Begin block 0xc30
    prev=[0x30d], succ=[0x29cc]
    =================================
    0xc31: vc31(0x1) = CONST 
    0xc33: vc33 = SLOAD vc31(0x1)
    0xc34: vc34(0xff) = CONST 
    0xc36: vc36 = AND vc34(0xff), vc33
    0xc38: JUMP v30e(0x29cc)

    Begin block 0x29cc
    prev=[0xc30], succ=[]
    =================================
    0x29cd: v29cd(0x40) = CONST 
    0x29d0: v29d0 = MLOAD v29cd(0x40)
    0x29d2: v29d2 = ISZERO vc36
    0x29d3: v29d3 = ISZERO v29d2
    0x29d5: MSTORE v29d0, v29d3
    0x29d6: v29d6 = MLOAD v29cd(0x40)
    0x29da: v29da(0x0) = SUB v29d0, v29d6
    0x29db: v29db(0x20) = CONST 
    0x29dd: v29dd(0x20) = ADD v29db(0x20), v29da(0x0)
    0x29df: RETURN v29d6, v29dd(0x20)

}

function safeBatchTransferFrom(address,address,uint256[],uint256[],bytes)() public {
    Begin block 0x315
    prev=[], succ=[0x327, 0x32b]
    =================================
    0x316: v316(0x29ff) = CONST 
    0x319: v319(0x4) = CONST 
    0x31c: v31c = CALLDATASIZE 
    0x31d: v31d = SUB v31c, v319(0x4)
    0x31e: v31e(0xa0) = CONST 
    0x321: v321 = LT v31d, v31e(0xa0)
    0x322: v322 = ISZERO v321
    0x323: v323(0x32b) = CONST 
    0x326: JUMPI v323(0x32b), v322

    Begin block 0x327
    prev=[0x315], succ=[]
    =================================
    0x327: v327(0x0) = CONST 
    0x32a: REVERT v327(0x0), v327(0x0)

    Begin block 0x32b
    prev=[0x315], succ=[0x35a, 0x35e]
    =================================
    0x32c: v32c(0x1) = CONST 
    0x32e: v32e(0x1) = CONST 
    0x330: v330(0xa0) = CONST 
    0x332: v332(0x10000000000000000000000000000000000000000) = SHL v330(0xa0), v32e(0x1)
    0x333: v333(0xffffffffffffffffffffffffffffffffffffffff) = SUB v332(0x10000000000000000000000000000000000000000), v32c(0x1)
    0x335: v335 = CALLDATALOAD v319(0x4)
    0x337: v337 = AND v333(0xffffffffffffffffffffffffffffffffffffffff), v335
    0x339: v339(0x20) = CONST 
    0x33c: v33c(0x24) = ADD v319(0x4), v339(0x20)
    0x33d: v33d = CALLDATALOAD v33c(0x24)
    0x340: v340 = AND v333(0xffffffffffffffffffffffffffffffffffffffff), v33d
    0x343: v343 = ADD v319(0x4), v31d
    0x345: v345(0x60) = CONST 
    0x348: v348(0x64) = ADD v319(0x4), v345(0x60)
    0x349: v349(0x40) = CONST 
    0x34c: v34c(0x44) = ADD v319(0x4), v349(0x40)
    0x34d: v34d = CALLDATALOAD v34c(0x44)
    0x34e: v34e(0x1) = CONST 
    0x350: v350(0x20) = CONST 
    0x352: v352(0x100000000) = SHL v350(0x20), v34e(0x1)
    0x354: v354 = GT v34d, v352(0x100000000)
    0x355: v355 = ISZERO v354
    0x356: v356(0x35e) = CONST 
    0x359: JUMPI v356(0x35e), v355

    Begin block 0x35a
    prev=[0x32b], succ=[]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35d: REVERT v35a(0x0), v35a(0x0)

    Begin block 0x35e
    prev=[0x32b], succ=[0x36c, 0x370]
    =================================
    0x360: v360 = ADD v319(0x4), v34d
    0x362: v362(0x20) = CONST 
    0x365: v365 = ADD v360, v362(0x20)
    0x366: v366 = GT v365, v343
    0x367: v367 = ISZERO v366
    0x368: v368(0x370) = CONST 
    0x36b: JUMPI v368(0x370), v367

    Begin block 0x36c
    prev=[0x35e], succ=[]
    =================================
    0x36c: v36c(0x0) = CONST 
    0x36f: REVERT v36c(0x0), v36c(0x0)

    Begin block 0x370
    prev=[0x35e], succ=[0x38d, 0x391]
    =================================
    0x372: v372 = CALLDATALOAD v360
    0x374: v374(0x20) = CONST 
    0x376: v376 = ADD v374(0x20), v360
    0x379: v379(0x20) = CONST 
    0x37c: v37c = MUL v372, v379(0x20)
    0x37e: v37e = ADD v376, v37c
    0x37f: v37f = GT v37e, v343
    0x380: v380(0x1) = CONST 
    0x382: v382(0x20) = CONST 
    0x384: v384(0x100000000) = SHL v382(0x20), v380(0x1)
    0x386: v386 = GT v372, v384(0x100000000)
    0x387: v387 = OR v386, v37f
    0x388: v388 = ISZERO v387
    0x389: v389(0x391) = CONST 
    0x38c: JUMPI v389(0x391), v388

    Begin block 0x38d
    prev=[0x370], succ=[]
    =================================
    0x38d: v38d(0x0) = CONST 
    0x390: REVERT v38d(0x0), v38d(0x0)

    Begin block 0x391
    prev=[0x370], succ=[0x3dc, 0x3e0]
    =================================
    0x396: v396(0x20) = CONST 
    0x398: v398 = MUL v396(0x20), v372
    0x399: v399(0x20) = CONST 
    0x39b: v39b = ADD v399(0x20), v398
    0x39c: v39c(0x40) = CONST 
    0x39e: v39e = MLOAD v39c(0x40)
    0x3a1: v3a1 = ADD v39e, v39b
    0x3a2: v3a2(0x40) = CONST 
    0x3a4: MSTORE v3a2(0x40), v3a1
    0x3ac: MSTORE v39e, v372
    0x3ad: v3ad(0x20) = CONST 
    0x3af: v3af = ADD v3ad(0x20), v39e
    0x3b2: v3b2(0x20) = CONST 
    0x3b4: v3b4 = MUL v3b2(0x20), v372
    0x3b8: CALLDATACOPY v3af, v376, v3b4
    0x3b9: v3b9(0x0) = CONST 
    0x3bc: v3bc = ADD v3af, v3b4
    0x3c0: MSTORE v3bc, v3b9(0x0)
    0x3c6: v3c6(0x20) = CONST 
    0x3c9: v3c9(0x84) = ADD v348(0x64), v3c6(0x20)
    0x3cc: v3cc = CALLDATALOAD v348(0x64)
    0x3d0: v3d0(0x1) = CONST 
    0x3d2: v3d2(0x20) = CONST 
    0x3d4: v3d4(0x100000000) = SHL v3d2(0x20), v3d0(0x1)
    0x3d6: v3d6 = GT v3cc, v3d4(0x100000000)
    0x3d7: v3d7 = ISZERO v3d6
    0x3d8: v3d8(0x3e0) = CONST 
    0x3db: JUMPI v3d8(0x3e0), v3d7

    Begin block 0x3dc
    prev=[0x391], succ=[]
    =================================
    0x3dc: v3dc(0x0) = CONST 
    0x3df: REVERT v3dc(0x0), v3dc(0x0)

    Begin block 0x3e0
    prev=[0x391], succ=[0x3ee, 0x3f2]
    =================================
    0x3e2: v3e2 = ADD v319(0x4), v3cc
    0x3e4: v3e4(0x20) = CONST 
    0x3e7: v3e7 = ADD v3e2, v3e4(0x20)
    0x3e8: v3e8 = GT v3e7, v343
    0x3e9: v3e9 = ISZERO v3e8
    0x3ea: v3ea(0x3f2) = CONST 
    0x3ed: JUMPI v3ea(0x3f2), v3e9

    Begin block 0x3ee
    prev=[0x3e0], succ=[]
    =================================
    0x3ee: v3ee(0x0) = CONST 
    0x3f1: REVERT v3ee(0x0), v3ee(0x0)

    Begin block 0x3f2
    prev=[0x3e0], succ=[0x40f, 0x413]
    =================================
    0x3f4: v3f4 = CALLDATALOAD v3e2
    0x3f6: v3f6(0x20) = CONST 
    0x3f8: v3f8 = ADD v3f6(0x20), v3e2
    0x3fb: v3fb(0x20) = CONST 
    0x3fe: v3fe = MUL v3f4, v3fb(0x20)
    0x400: v400 = ADD v3f8, v3fe
    0x401: v401 = GT v400, v343
    0x402: v402(0x1) = CONST 
    0x404: v404(0x20) = CONST 
    0x406: v406(0x100000000) = SHL v404(0x20), v402(0x1)
    0x408: v408 = GT v3f4, v406(0x100000000)
    0x409: v409 = OR v408, v401
    0x40a: v40a = ISZERO v409
    0x40b: v40b(0x413) = CONST 
    0x40e: JUMPI v40b(0x413), v40a

    Begin block 0x40f
    prev=[0x3f2], succ=[]
    =================================
    0x40f: v40f(0x0) = CONST 
    0x412: REVERT v40f(0x0), v40f(0x0)

    Begin block 0x413
    prev=[0x3f2], succ=[0x45e, 0x462]
    =================================
    0x418: v418(0x20) = CONST 
    0x41a: v41a = MUL v418(0x20), v3f4
    0x41b: v41b(0x20) = CONST 
    0x41d: v41d = ADD v41b(0x20), v41a
    0x41e: v41e(0x40) = CONST 
    0x420: v420 = MLOAD v41e(0x40)
    0x423: v423 = ADD v420, v41d
    0x424: v424(0x40) = CONST 
    0x426: MSTORE v424(0x40), v423
    0x42e: MSTORE v420, v3f4
    0x42f: v42f(0x20) = CONST 
    0x431: v431 = ADD v42f(0x20), v420
    0x434: v434(0x20) = CONST 
    0x436: v436 = MUL v434(0x20), v3f4
    0x43a: CALLDATACOPY v431, v3f8, v436
    0x43b: v43b(0x0) = CONST 
    0x43e: v43e = ADD v431, v436
    0x442: MSTORE v43e, v43b(0x0)
    0x448: v448(0x20) = CONST 
    0x44b: v44b(0xa4) = ADD v3c9(0x84), v448(0x20)
    0x44e: v44e = CALLDATALOAD v3c9(0x84)
    0x452: v452(0x1) = CONST 
    0x454: v454(0x20) = CONST 
    0x456: v456(0x100000000) = SHL v454(0x20), v452(0x1)
    0x458: v458 = GT v44e, v456(0x100000000)
    0x459: v459 = ISZERO v458
    0x45a: v45a(0x462) = CONST 
    0x45d: JUMPI v45a(0x462), v459

    Begin block 0x45e
    prev=[0x413], succ=[]
    =================================
    0x45e: v45e(0x0) = CONST 
    0x461: REVERT v45e(0x0), v45e(0x0)

    Begin block 0x462
    prev=[0x413], succ=[0x470, 0x474]
    =================================
    0x464: v464 = ADD v319(0x4), v44e
    0x466: v466(0x20) = CONST 
    0x469: v469 = ADD v464, v466(0x20)
    0x46a: v46a = GT v469, v343
    0x46b: v46b = ISZERO v46a
    0x46c: v46c(0x474) = CONST 
    0x46f: JUMPI v46c(0x474), v46b

    Begin block 0x470
    prev=[0x462], succ=[]
    =================================
    0x470: v470(0x0) = CONST 
    0x473: REVERT v470(0x0), v470(0x0)

    Begin block 0x474
    prev=[0x462], succ=[0x491, 0x495]
    =================================
    0x476: v476 = CALLDATALOAD v464
    0x478: v478(0x20) = CONST 
    0x47a: v47a = ADD v478(0x20), v464
    0x47d: v47d(0x1) = CONST 
    0x480: v480 = MUL v476, v47d(0x1)
    0x482: v482 = ADD v47a, v480
    0x483: v483 = GT v482, v343
    0x484: v484(0x1) = CONST 
    0x486: v486(0x20) = CONST 
    0x488: v488(0x100000000) = SHL v486(0x20), v484(0x1)
    0x48a: v48a = GT v476, v488(0x100000000)
    0x48b: v48b = OR v48a, v483
    0x48c: v48c = ISZERO v48b
    0x48d: v48d(0x495) = CONST 
    0x490: JUMPI v48d(0x495), v48c

    Begin block 0x491
    prev=[0x474], succ=[]
    =================================
    0x491: v491(0x0) = CONST 
    0x494: REVERT v491(0x0), v491(0x0)

    Begin block 0x495
    prev=[0x474], succ=[0xc39]
    =================================
    0x49a: v49a(0x1f) = CONST 
    0x49c: v49c = ADD v49a(0x1f), v476
    0x49d: v49d(0x20) = CONST 
    0x4a1: v4a1 = DIV v49c, v49d(0x20)
    0x4a2: v4a2 = MUL v4a1, v49d(0x20)
    0x4a3: v4a3(0x20) = CONST 
    0x4a5: v4a5 = ADD v4a3(0x20), v4a2
    0x4a6: v4a6(0x40) = CONST 
    0x4a8: v4a8 = MLOAD v4a6(0x40)
    0x4ab: v4ab = ADD v4a8, v4a5
    0x4ac: v4ac(0x40) = CONST 
    0x4ae: MSTORE v4ac(0x40), v4ab
    0x4b6: MSTORE v4a8, v476
    0x4b7: v4b7(0x20) = CONST 
    0x4b9: v4b9 = ADD v4b7(0x20), v4a8
    0x4bf: CALLDATACOPY v4b9, v47a, v476
    0x4c0: v4c0(0x0) = CONST 
    0x4c3: v4c3 = ADD v4b9, v476
    0x4c7: MSTORE v4c3, v4c0(0x0)
    0x4cc: v4cc(0xc39) = CONST 
    0x4d5: JUMP v4cc(0xc39)

    Begin block 0xc39
    prev=[0x495], succ=[0xc48, 0xc7e]
    =================================
    0xc3a: vc3a(0x1) = CONST 
    0xc3c: vc3c(0x1) = CONST 
    0xc3e: vc3e(0xa0) = CONST 
    0xc40: vc40(0x10000000000000000000000000000000000000000) = SHL vc3e(0xa0), vc3c(0x1)
    0xc41: vc41(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc40(0x10000000000000000000000000000000000000000), vc3a(0x1)
    0xc43: vc43 = AND v340, vc41(0xffffffffffffffffffffffffffffffffffffffff)
    0xc44: vc44(0xc7e) = CONST 
    0xc47: JUMPI vc44(0xc7e), vc43

    Begin block 0xc48
    prev=[0xc39], succ=[]
    =================================
    0xc48: vc48(0x40) = CONST 
    0xc4a: vc4a = MLOAD vc48(0x40)
    0xc4b: vc4b(0x461bcd) = CONST 
    0xc4f: vc4f(0xe5) = CONST 
    0xc51: vc51(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc4f(0xe5), vc4b(0x461bcd)
    0xc53: MSTORE vc4a, vc51(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc54: vc54(0x4) = CONST 
    0xc56: vc56 = ADD vc54(0x4), vc4a
    0xc59: vc59(0x20) = CONST 
    0xc5b: vc5b = ADD vc59(0x20), vc56
    0xc5e: vc5e(0x20) = SUB vc5b, vc56
    0xc60: MSTORE vc56, vc5e(0x20)
    0xc61: vc61(0x2a) = CONST 
    0xc64: MSTORE vc5b, vc61(0x2a)
    0xc65: vc65(0x20) = CONST 
    0xc67: vc67 = ADD vc65(0x20), vc5b
    0xc69: vc69(0x27ed) = CONST 
    0xc6c: vc6c(0x2a) = CONST 
    0xc6f: CODECOPY vc67, vc69(0x27ed), vc6c(0x2a)
    0xc70: vc70(0x40) = CONST 
    0xc72: vc72 = ADD vc70(0x40), vc67
    0xc76: vc76(0x40) = CONST 
    0xc78: vc78 = MLOAD vc76(0x40)
    0xc7b: vc7b(0x84) = SUB vc72, vc78
    0xc7d: REVERT vc78, vc7b(0x84)

    Begin block 0xc7e
    prev=[0xc39], succ=[0xc88, 0xcbe]
    =================================
    0xc80: vc80 = MLOAD v420
    0xc82: vc82 = MLOAD v39e
    0xc83: vc83 = EQ vc82, vc80
    0xc84: vc84(0xcbe) = CONST 
    0xc87: JUMPI vc84(0xcbe), vc83

    Begin block 0xc88
    prev=[0xc7e], succ=[]
    =================================
    0xc88: vc88(0x40) = CONST 
    0xc8a: vc8a = MLOAD vc88(0x40)
    0xc8b: vc8b(0x461bcd) = CONST 
    0xc8f: vc8f(0xe5) = CONST 
    0xc91: vc91(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc8f(0xe5), vc8b(0x461bcd)
    0xc93: MSTORE vc8a, vc91(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc94: vc94(0x4) = CONST 
    0xc96: vc96 = ADD vc94(0x4), vc8a
    0xc99: vc99(0x20) = CONST 
    0xc9b: vc9b = ADD vc99(0x20), vc96
    0xc9e: vc9e(0x20) = SUB vc9b, vc96
    0xca0: MSTORE vc96, vc9e(0x20)
    0xca1: vca1(0x23) = CONST 
    0xca4: MSTORE vc9b, vca1(0x23)
    0xca5: vca5(0x20) = CONST 
    0xca7: vca7 = ADD vca5(0x20), vc9b
    0xca9: vca9(0x27a6) = CONST 
    0xcac: vcac(0x23) = CONST 
    0xcaf: CODECOPY vca7, vca9(0x27a6), vcac(0x23)
    0xcb0: vcb0(0x40) = CONST 
    0xcb2: vcb2 = ADD vcb0(0x40), vca7
    0xcb6: vcb6(0x40) = CONST 
    0xcb8: vcb8 = MLOAD vcb6(0x40)
    0xcbb: vcbb(0x84) = SUB vcb2, vcb8
    0xcbd: REVERT vcb8, vcbb(0x84)

    Begin block 0xcbe
    prev=[0xc7e], succ=[0xcda, 0xcd0]
    =================================
    0xcbf: vcbf(0x1) = CONST 
    0xcc1: vcc1(0x1) = CONST 
    0xcc3: vcc3(0xa0) = CONST 
    0xcc5: vcc5(0x10000000000000000000000000000000000000000) = SHL vcc3(0xa0), vcc1(0x1)
    0xcc6: vcc6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcc5(0x10000000000000000000000000000000000000000), vcbf(0x1)
    0xcc8: vcc8 = AND v337, vcc6(0xffffffffffffffffffffffffffffffffffffffff)
    0xcc9: vcc9 = CALLER 
    0xcca: vcca = EQ vcc9, vcc8
    0xccc: vccc(0xcda) = CONST 
    0xccf: JUMPI vccc(0xcda), vcca

    Begin block 0xcda
    prev=[0xcbe, 0x1969B0xcd0], succ=[0xcdf, 0xd15]
    =================================
    0xcda_0x0: vcda_0 = PHI vcca, v1994Vcd0
    0xcdb: vcdb(0xd15) = CONST 
    0xcde: JUMPI vcdb(0xd15), vcda_0

    Begin block 0xcdf
    prev=[0xcda], succ=[]
    =================================
    0xcdf: vcdf(0x40) = CONST 
    0xce1: vce1 = MLOAD vcdf(0x40)
    0xce2: vce2(0x461bcd) = CONST 
    0xce6: vce6(0xe5) = CONST 
    0xce8: vce8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vce6(0xe5), vce2(0x461bcd)
    0xcea: MSTORE vce1, vce8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xceb: vceb(0x4) = CONST 
    0xced: vced = ADD vceb(0x4), vce1
    0xcf0: vcf0(0x20) = CONST 
    0xcf2: vcf2 = ADD vcf0(0x20), vced
    0xcf5: vcf5(0x20) = SUB vcf2, vced
    0xcf7: MSTORE vced, vcf5(0x20)
    0xcf8: vcf8(0x2d) = CONST 
    0xcfb: MSTORE vcf2, vcf8(0x2d)
    0xcfc: vcfc(0x20) = CONST 
    0xcfe: vcfe = ADD vcfc(0x20), vcf2
    0xd00: vd00(0x2751) = CONST 
    0xd03: vd03(0x2d) = CONST 
    0xd06: CODECOPY vcfe, vd00(0x2751), vd03(0x2d)
    0xd07: vd07(0x40) = CONST 
    0xd09: vd09 = ADD vd07(0x40), vcfe
    0xd0d: vd0d(0x40) = CONST 
    0xd0f: vd0f = MLOAD vd0d(0x40)
    0xd12: vd12(0x84) = SUB vd09, vd0f
    0xd14: REVERT vd0f, vd12(0x84)

    Begin block 0xd15
    prev=[0xcda], succ=[0xd18]
    =================================
    0xd16: vd16(0x0) = CONST 

    Begin block 0xd18
    prev=[0xd15, 0xd84], succ=[0xd22, 0xdb3]
    =================================
    0xd18_0x0: vd18_0 = PHI vd16(0x0), vdae
    0xd1a: vd1a = MLOAD v39e
    0xd1c: vd1c = LT vd18_0, vd1a
    0xd1d: vd1d = ISZERO vd1c
    0xd1e: vd1e(0xdb3) = CONST 
    0xd21: JUMPI vd1e(0xdb3), vd1d

    Begin block 0xd22
    prev=[0xd18], succ=[0xd2e, 0xd2f]
    =================================
    0xd22: vd22(0x0) = CONST 
    0xd22_0x0: vd22_0 = PHI vd16(0x0), vdae
    0xd27: vd27 = MLOAD v39e
    0xd29: vd29 = LT vd22_0, vd27
    0xd2a: vd2a(0xd2f) = CONST 
    0xd2d: JUMPI vd2a(0xd2f), vd29

    Begin block 0xd2e
    prev=[0xd22], succ=[]
    =================================
    0xd2e: THROW 

    Begin block 0xd2f
    prev=[0xd22], succ=[0xd43]
    =================================
    0xd2f_0x0: vd2f_0 = PHI vd16(0x0), vdae
    0xd30: vd30(0x20) = CONST 
    0xd32: vd32 = MUL vd30(0x20), vd2f_0
    0xd33: vd33(0x20) = CONST 
    0xd35: vd35 = ADD vd33(0x20), vd32
    0xd36: vd36 = ADD vd35, v39e
    0xd37: vd37 = MLOAD vd36
    0xd3a: vd3a(0xd43) = CONST 
    0xd3f: vd3f(0x192e) = CONST 
    0xd42: vd42_0 = CALLPRIVATE vd3f(0x192e), vd37, v337, vd3a(0xd43)

    Begin block 0xd43
    prev=[0xd2f], succ=[0xd48, 0xd84]
    =================================
    0xd44: vd44(0xd84) = CONST 
    0xd47: JUMPI vd44(0xd84), vd42_0

    Begin block 0xd48
    prev=[0xd43], succ=[]
    =================================
    0xd48: vd48(0x40) = CONST 
    0xd4b: vd4b = MLOAD vd48(0x40)
    0xd4c: vd4c(0x461bcd) = CONST 
    0xd50: vd50(0xe5) = CONST 
    0xd52: vd52(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd50(0xe5), vd4c(0x461bcd)
    0xd54: MSTORE vd4b, vd52(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd55: vd55(0x20) = CONST 
    0xd57: vd57(0x4) = CONST 
    0xd5a: vd5a = ADD vd4b, vd57(0x4)
    0xd5b: MSTORE vd5a, vd55(0x20)
    0xd5c: vd5c(0xd) = CONST 
    0xd5e: vd5e(0x24) = CONST 
    0xd61: vd61 = ADD vd4b, vd5e(0x24)
    0xd62: MSTORE vd61, vd5c(0xd)
    0xd63: vd63(0x2737ba103a34329037bbb732b9) = CONST 
    0xd71: vd71(0x99) = CONST 
    0xd73: vd73(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL vd71(0x99), vd63(0x2737ba103a34329037bbb732b9)
    0xd74: vd74(0x44) = CONST 
    0xd77: vd77 = ADD vd4b, vd74(0x44)
    0xd78: MSTORE vd77, vd73(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0xd7a: vd7a = MLOAD vd48(0x40)
    0xd7e: vd7e(0x0) = SUB vd4b, vd7a
    0xd7f: vd7f(0x64) = CONST 
    0xd81: vd81(0x64) = ADD vd7f(0x64), vd7e(0x0)
    0xd83: REVERT vd7a, vd81(0x64)

    Begin block 0xd84
    prev=[0xd43], succ=[0xd18]
    =================================
    0xd84_0x1: vd84_1 = PHI vd16(0x0), vdae
    0xd85: vd85(0x0) = CONST 
    0xd89: MSTORE vd85(0x0), vd37
    0xd8a: vd8a(0x7) = CONST 
    0xd8c: vd8c(0x20) = CONST 
    0xd8e: MSTORE vd8c(0x20), vd8a(0x7)
    0xd8f: vd8f(0x40) = CONST 
    0xd92: vd92 = SHA3 vd85(0x0), vd8f(0x40)
    0xd94: vd94 = SLOAD vd92
    0xd95: vd95(0x1) = CONST 
    0xd97: vd97(0x1) = CONST 
    0xd99: vd99(0xa0) = CONST 
    0xd9b: vd9b(0x10000000000000000000000000000000000000000) = SHL vd99(0xa0), vd97(0x1)
    0xd9c: vd9c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd9b(0x10000000000000000000000000000000000000000), vd95(0x1)
    0xd9d: vd9d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vd9c(0xffffffffffffffffffffffffffffffffffffffff)
    0xd9e: vd9e = AND vd9d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd94
    0xd9f: vd9f(0x1) = CONST 
    0xda1: vda1(0x1) = CONST 
    0xda3: vda3(0xa0) = CONST 
    0xda5: vda5(0x10000000000000000000000000000000000000000) = SHL vda3(0xa0), vda1(0x1)
    0xda6: vda6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vda5(0x10000000000000000000000000000000000000000), vd9f(0x1)
    0xda8: vda8 = AND v340, vda6(0xffffffffffffffffffffffffffffffffffffffff)
    0xda9: vda9 = OR vda8, vd9e
    0xdab: SSTORE vd92, vda9
    0xdac: vdac(0x1) = CONST 
    0xdae: vdae = ADD vdac(0x1), vd84_1
    0xdaf: vdaf(0xd18) = CONST 
    0xdb2: JUMP vdaf(0xd18)

    Begin block 0xdb3
    prev=[0xd18], succ=[0xe21]
    =================================
    0xdb6: vdb6(0x1) = CONST 
    0xdb8: vdb8(0x1) = CONST 
    0xdba: vdba(0xa0) = CONST 
    0xdbc: vdbc(0x10000000000000000000000000000000000000000) = SHL vdba(0xa0), vdb8(0x1)
    0xdbd: vdbd(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdbc(0x10000000000000000000000000000000000000000), vdb6(0x1)
    0xdbe: vdbe = AND vdbd(0xffffffffffffffffffffffffffffffffffffffff), v340
    0xdc0: vdc0(0x1) = CONST 
    0xdc2: vdc2(0x1) = CONST 
    0xdc4: vdc4(0xa0) = CONST 
    0xdc6: vdc6(0x10000000000000000000000000000000000000000) = SHL vdc4(0xa0), vdc2(0x1)
    0xdc7: vdc7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdc6(0x10000000000000000000000000000000000000000), vdc0(0x1)
    0xdc8: vdc8 = AND vdc7(0xffffffffffffffffffffffffffffffffffffffff), v337
    0xdc9: vdc9 = CALLER 
    0xdca: vdca(0x1) = CONST 
    0xdcc: vdcc(0x1) = CONST 
    0xdce: vdce(0xa0) = CONST 
    0xdd0: vdd0(0x10000000000000000000000000000000000000000) = SHL vdce(0xa0), vdcc(0x1)
    0xdd1: vdd1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdd0(0x10000000000000000000000000000000000000000), vdca(0x1)
    0xdd2: vdd2 = AND vdd1(0xffffffffffffffffffffffffffffffffffffffff), vdc9
    0xdd3: vdd3(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0xdf6: vdf6(0x40) = CONST 
    0xdf8: vdf8 = MLOAD vdf6(0x40)
    0xdfb: vdfb(0x20) = CONST 
    0xdfd: vdfd = ADD vdfb(0x20), vdf8
    0xdff: vdff(0x20) = CONST 
    0xe01: ve01 = ADD vdff(0x20), vdfd
    0xe04: ve04(0x40) = SUB ve01, vdf8
    0xe06: MSTORE vdf8, ve04(0x40)
    0xe0a: ve0a = MLOAD v39e
    0xe0c: MSTORE ve01, ve0a
    0xe0d: ve0d(0x20) = CONST 
    0xe0f: ve0f = ADD ve0d(0x20), ve01
    0xe13: ve13 = MLOAD v39e
    0xe15: ve15(0x20) = CONST 
    0xe17: ve17 = ADD ve15(0x20), v39e
    0xe19: ve19(0x20) = CONST 
    0xe1b: ve1b = MUL ve19(0x20), ve13
    0xe1f: ve1f(0x0) = CONST 

    Begin block 0xe21
    prev=[0xdb3, 0xe2a], succ=[0xe39, 0xe2a]
    =================================
    0xe21_0x0: ve21_0 = PHI ve1f(0x0), ve34
    0xe24: ve24 = LT ve21_0, ve1b
    0xe25: ve25 = ISZERO ve24
    0xe26: ve26(0xe39) = CONST 
    0xe29: JUMPI ve26(0xe39), ve25

    Begin block 0xe39
    prev=[0xe21], succ=[0xe60]
    =================================
    0xe40: ve40 = ADD ve1b, ve0f
    0xe43: ve43 = SUB ve40, vdf8
    0xe45: MSTORE vdfd, ve43
    0xe49: ve49 = MLOAD v420
    0xe4b: MSTORE ve40, ve49
    0xe4c: ve4c(0x20) = CONST 
    0xe4e: ve4e = ADD ve4c(0x20), ve40
    0xe52: ve52 = MLOAD v420
    0xe54: ve54(0x20) = CONST 
    0xe56: ve56 = ADD ve54(0x20), v420
    0xe58: ve58(0x20) = CONST 
    0xe5a: ve5a = MUL ve58(0x20), ve52
    0xe5e: ve5e(0x0) = CONST 

    Begin block 0xe60
    prev=[0xe39, 0xe69], succ=[0xe78, 0xe69]
    =================================
    0xe60_0x0: ve60_0 = PHI ve5e(0x0), ve73
    0xe63: ve63 = LT ve60_0, ve5a
    0xe64: ve64 = ISZERO ve63
    0xe65: ve65(0xe78) = CONST 
    0xe68: JUMPI ve65(0xe78), ve64

    Begin block 0xe78
    prev=[0xe60], succ=[0x2d19]
    =================================
    0xe7f: ve7f = ADD ve5a, ve4e
    0xe86: ve86(0x40) = CONST 
    0xe88: ve88 = MLOAD ve86(0x40)
    0xe8b: ve8b = SUB ve7f, ve88
    0xe8d: LOG4 ve88, ve8b, vdd3(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), vdd2, vdc8, vdbe
    0xe8e: ve8e(0x2d19) = CONST 
    0xe91: ve91 = CALLER 
    0xe97: ve97(0x1c36) = CONST 
    0xe9a: CALLPRIVATE ve97(0x1c36), v4a8, v420, v39e, v340, v337, ve91, ve8e(0x2d19)

    Begin block 0x2d19
    prev=[0xe78], succ=[0x29ff]
    =================================
    0x2d1f: JUMP v316(0x29ff)

    Begin block 0x29ff
    prev=[0x2d19], succ=[]
    =================================
    0x2a00: STOP 

    Begin block 0xe69
    prev=[0xe60], succ=[0xe60]
    =================================
    0xe69_0x0: ve69_0 = PHI ve5e(0x0), ve73
    0xe6b: ve6b = ADD ve69_0, ve56
    0xe6c: ve6c = MLOAD ve6b
    0xe6f: ve6f = ADD ve69_0, ve4e
    0xe70: MSTORE ve6f, ve6c
    0xe71: ve71(0x20) = CONST 
    0xe73: ve73 = ADD ve71(0x20), ve69_0
    0xe74: ve74(0xe60) = CONST 
    0xe77: JUMP ve74(0xe60)

    Begin block 0xe2a
    prev=[0xe21], succ=[0xe21]
    =================================
    0xe2a_0x0: ve2a_0 = PHI ve1f(0x0), ve34
    0xe2c: ve2c = ADD ve2a_0, ve17
    0xe2d: ve2d = MLOAD ve2c
    0xe30: ve30 = ADD ve2a_0, ve0f
    0xe31: MSTORE ve30, ve2d
    0xe32: ve32(0x20) = CONST 
    0xe34: ve34 = ADD ve32(0x20), ve2a_0
    0xe35: ve35(0xe21) = CONST 
    0xe38: JUMP ve35(0xe21)

    Begin block 0xcd0
    prev=[0xcbe], succ=[0x1969B0xcd0]
    =================================
    0xcd1: vcd1(0xcda) = CONST 
    0xcd5: vcd5 = CALLER 
    0xcd6: vcd6(0x1969) = CONST 
    0xcd9: JUMP vcd6(0x1969)

    Begin block 0x1969B0xcd0
    prev=[0xcd0], succ=[0xcda]
    =================================
    0x196aS0xcd0: v196aVcd0(0x1) = CONST 
    0x196cS0xcd0: v196cVcd0(0x1) = CONST 
    0x196eS0xcd0: v196eVcd0(0xa0) = CONST 
    0x1970S0xcd0: v1970Vcd0(0x10000000000000000000000000000000000000000) = SHL v196eVcd0(0xa0), v196cVcd0(0x1)
    0x1971S0xcd0: v1971Vcd0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1970Vcd0(0x10000000000000000000000000000000000000000), v196aVcd0(0x1)
    0x1974S0xcd0: v1974Vcd0 = AND v1971Vcd0(0xffffffffffffffffffffffffffffffffffffffff), v337
    0x1975S0xcd0: v1975Vcd0(0x0) = CONST 
    0x1979S0xcd0: MSTORE v1975Vcd0(0x0), v1974Vcd0
    0x197aS0xcd0: v197aVcd0(0x8) = CONST 
    0x197cS0xcd0: v197cVcd0(0x20) = CONST 
    0x1980S0xcd0: MSTORE v197cVcd0(0x20), v197aVcd0(0x8)
    0x1981S0xcd0: v1981Vcd0(0x40) = CONST 
    0x1985S0xcd0: v1985Vcd0 = SHA3 v1975Vcd0(0x0), v1981Vcd0(0x40)
    0x1989S0xcd0: v1989Vcd0 = AND v1971Vcd0(0xffffffffffffffffffffffffffffffffffffffff), vcd5
    0x198bS0xcd0: MSTORE v1975Vcd0(0x0), v1989Vcd0
    0x198fS0xcd0: MSTORE v197cVcd0(0x20), v1985Vcd0
    0x1990S0xcd0: v1990Vcd0 = SHA3 v1975Vcd0(0x0), v1981Vcd0(0x40)
    0x1991S0xcd0: v1991Vcd0 = SLOAD v1990Vcd0
    0x1992S0xcd0: v1992Vcd0(0xff) = CONST 
    0x1994S0xcd0: v1994Vcd0 = AND v1992Vcd0(0xff), v1991Vcd0
    0x1996S0xcd0: JUMP vcd1(0xcda)

}

function removeMinter(address)() public {
    Begin block 0x4d6
    prev=[], succ=[0x4e8, 0x4ec]
    =================================
    0x4d7: v4d7(0x2a20) = CONST 
    0x4da: v4da(0x4) = CONST 
    0x4dd: v4dd = CALLDATASIZE 
    0x4de: v4de = SUB v4dd, v4da(0x4)
    0x4df: v4df(0x20) = CONST 
    0x4e2: v4e2 = LT v4de, v4df(0x20)
    0x4e3: v4e3 = ISZERO v4e2
    0x4e4: v4e4(0x4ec) = CONST 
    0x4e7: JUMPI v4e4(0x4ec), v4e3

    Begin block 0x4e8
    prev=[0x4d6], succ=[]
    =================================
    0x4e8: v4e8(0x0) = CONST 
    0x4eb: REVERT v4e8(0x0), v4e8(0x0)

    Begin block 0x4ec
    prev=[0x4d6], succ=[0xea2]
    =================================
    0x4ee: v4ee = CALLDATALOAD v4da(0x4)
    0x4ef: v4ef(0x1) = CONST 
    0x4f1: v4f1(0x1) = CONST 
    0x4f3: v4f3(0xa0) = CONST 
    0x4f5: v4f5(0x10000000000000000000000000000000000000000) = SHL v4f3(0xa0), v4f1(0x1)
    0x4f6: v4f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f5(0x10000000000000000000000000000000000000000), v4ef(0x1)
    0x4f7: v4f7 = AND v4f6(0xffffffffffffffffffffffffffffffffffffffff), v4ee
    0x4f8: v4f8(0xea2) = CONST 
    0x4fb: JUMP v4f8(0xea2)

    Begin block 0xea2
    prev=[0x4ec], succ=[0xeb5, 0xef1]
    =================================
    0xea3: vea3(0x3) = CONST 
    0xea5: vea5 = SLOAD vea3(0x3)
    0xea6: vea6(0x1) = CONST 
    0xea8: vea8(0x1) = CONST 
    0xeaa: veaa(0xa0) = CONST 
    0xeac: veac(0x10000000000000000000000000000000000000000) = SHL veaa(0xa0), vea8(0x1)
    0xead: vead(0xffffffffffffffffffffffffffffffffffffffff) = SUB veac(0x10000000000000000000000000000000000000000), vea6(0x1)
    0xeae: veae = AND vead(0xffffffffffffffffffffffffffffffffffffffff), vea5
    0xeaf: veaf = CALLER 
    0xeb0: veb0 = EQ veaf, veae
    0xeb1: veb1(0xef1) = CONST 
    0xeb4: JUMPI veb1(0xef1), veb0

    Begin block 0xeb5
    prev=[0xea2], succ=[]
    =================================
    0xeb5: veb5(0x40) = CONST 
    0xeb8: veb8 = MLOAD veb5(0x40)
    0xeb9: veb9(0x461bcd) = CONST 
    0xebd: vebd(0xe5) = CONST 
    0xebf: vebf(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vebd(0xe5), veb9(0x461bcd)
    0xec1: MSTORE veb8, vebf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xec2: vec2(0x20) = CONST 
    0xec4: vec4(0x4) = CONST 
    0xec7: vec7 = ADD veb8, vec4(0x4)
    0xec8: MSTORE vec7, vec2(0x20)
    0xec9: vec9(0xd) = CONST 
    0xecb: vecb(0x24) = CONST 
    0xece: vece = ADD veb8, vecb(0x24)
    0xecf: MSTORE vece, vec9(0xd)
    0xed0: ved0(0x26bab9ba1031329037bbb732b9) = CONST 
    0xede: vede(0x99) = CONST 
    0xee0: vee0(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL vede(0x99), ved0(0x26bab9ba1031329037bbb732b9)
    0xee1: vee1(0x44) = CONST 
    0xee4: vee4 = ADD veb8, vee1(0x44)
    0xee5: MSTORE vee4, vee0(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0xee7: vee7 = MLOAD veb5(0x40)
    0xeeb: veeb(0x0) = SUB veb8, vee7
    0xeec: veec(0x64) = CONST 
    0xeee: veee(0x64) = ADD veec(0x64), veeb(0x0)
    0xef0: REVERT vee7, veee(0x64)

    Begin block 0xef1
    prev=[0xea2], succ=[0xf12, 0xf56]
    =================================
    0xef2: vef2(0x1) = CONST 
    0xef4: vef4(0x1) = CONST 
    0xef6: vef6(0xa0) = CONST 
    0xef8: vef8(0x10000000000000000000000000000000000000000) = SHL vef6(0xa0), vef4(0x1)
    0xef9: vef9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vef8(0x10000000000000000000000000000000000000000), vef2(0x1)
    0xefb: vefb = AND v4f7, vef9(0xffffffffffffffffffffffffffffffffffffffff)
    0xefc: vefc(0x0) = CONST 
    0xf00: MSTORE vefc(0x0), vefb
    0xf01: vf01(0x5) = CONST 
    0xf03: vf03(0x20) = CONST 
    0xf05: MSTORE vf03(0x20), vf01(0x5)
    0xf06: vf06(0x40) = CONST 
    0xf09: vf09 = SHA3 vefc(0x0), vf06(0x40)
    0xf0a: vf0a = SLOAD vf09
    0xf0b: vf0b(0xff) = CONST 
    0xf0d: vf0d = AND vf0b(0xff), vf0a
    0xf0e: vf0e(0xf56) = CONST 
    0xf11: JUMPI vf0e(0xf56), vf0d

    Begin block 0xf12
    prev=[0xef1], succ=[]
    =================================
    0xf12: vf12(0x40) = CONST 
    0xf15: vf15 = MLOAD vf12(0x40)
    0xf16: vf16(0x461bcd) = CONST 
    0xf1a: vf1a(0xe5) = CONST 
    0xf1c: vf1c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf1a(0xe5), vf16(0x461bcd)
    0xf1e: MSTORE vf15, vf1c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf1f: vf1f(0x20) = CONST 
    0xf21: vf21(0x4) = CONST 
    0xf24: vf24 = ADD vf15, vf21(0x4)
    0xf25: MSTORE vf24, vf1f(0x20)
    0xf26: vf26(0x15) = CONST 
    0xf28: vf28(0x24) = CONST 
    0xf2b: vf2b = ADD vf15, vf28(0x24)
    0xf2c: MSTORE vf2b, vf26(0x15)
    0xf2d: vf2d(0x135a5b9d195c88191bd95cc81b9bdd08195e1a5cdd) = CONST 
    0xf43: vf43(0x5a) = CONST 
    0xf45: vf45(0x4d696e74657220646f6573206e6f742065786973740000000000000000000000) = SHL vf43(0x5a), vf2d(0x135a5b9d195c88191bd95cc81b9bdd08195e1a5cdd)
    0xf46: vf46(0x44) = CONST 
    0xf49: vf49 = ADD vf15, vf46(0x44)
    0xf4a: MSTORE vf49, vf45(0x4d696e74657220646f6573206e6f742065786973740000000000000000000000)
    0xf4c: vf4c = MLOAD vf12(0x40)
    0xf50: vf50(0x0) = SUB vf15, vf4c
    0xf51: vf51(0x64) = CONST 
    0xf53: vf53(0x64) = ADD vf51(0x64), vf50(0x0)
    0xf55: REVERT vf4c, vf53(0x64)

    Begin block 0xf56
    prev=[0xef1], succ=[0x2a20]
    =================================
    0xf57: vf57(0x1) = CONST 
    0xf59: vf59(0x1) = CONST 
    0xf5b: vf5b(0xa0) = CONST 
    0xf5d: vf5d(0x10000000000000000000000000000000000000000) = SHL vf5b(0xa0), vf59(0x1)
    0xf5e: vf5e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf5d(0x10000000000000000000000000000000000000000), vf57(0x1)
    0xf5f: vf5f = AND vf5e(0xffffffffffffffffffffffffffffffffffffffff), v4f7
    0xf60: vf60(0x0) = CONST 
    0xf64: MSTORE vf60(0x0), vf5f
    0xf65: vf65(0x5) = CONST 
    0xf67: vf67(0x20) = CONST 
    0xf69: MSTORE vf67(0x20), vf65(0x5)
    0xf6a: vf6a(0x40) = CONST 
    0xf6d: vf6d = SHA3 vf60(0x0), vf6a(0x40)
    0xf6f: vf6f = SLOAD vf6d
    0xf70: vf70(0xff) = CONST 
    0xf72: vf72(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vf70(0xff)
    0xf73: vf73 = AND vf72(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vf6f
    0xf75: SSTORE vf6d, vf73
    0xf76: JUMP v4d7(0x2a20)

    Begin block 0x2a20
    prev=[0xf56], succ=[]
    =================================
    0x2a21: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x4fc
    prev=[], succ=[0x50e, 0x512]
    =================================
    0x4fd: v4fd(0x2a41) = CONST 
    0x500: v500(0x4) = CONST 
    0x503: v503 = CALLDATASIZE 
    0x504: v504 = SUB v503, v500(0x4)
    0x505: v505(0x40) = CONST 
    0x508: v508 = LT v504, v505(0x40)
    0x509: v509 = ISZERO v508
    0x50a: v50a(0x512) = CONST 
    0x50d: JUMPI v50a(0x512), v509

    Begin block 0x50e
    prev=[0x4fc], succ=[]
    =================================
    0x50e: v50e(0x0) = CONST 
    0x511: REVERT v50e(0x0), v50e(0x0)

    Begin block 0x512
    prev=[0x4fc], succ=[0xf77]
    =================================
    0x514: v514(0x1) = CONST 
    0x516: v516(0x1) = CONST 
    0x518: v518(0xa0) = CONST 
    0x51a: v51a(0x10000000000000000000000000000000000000000) = SHL v518(0xa0), v516(0x1)
    0x51b: v51b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51a(0x10000000000000000000000000000000000000000), v514(0x1)
    0x51d: v51d = CALLDATALOAD v500(0x4)
    0x51e: v51e = AND v51d, v51b(0xffffffffffffffffffffffffffffffffffffffff)
    0x520: v520(0x20) = CONST 
    0x522: v522(0x24) = ADD v520(0x20), v500(0x4)
    0x523: v523 = CALLDATALOAD v522(0x24)
    0x524: v524(0xf77) = CONST 
    0x527: JUMP v524(0xf77)

    Begin block 0xf77
    prev=[0x512], succ=[0xf8f, 0xfcc]
    =================================
    0xf78: vf78 = CALLER 
    0xf79: vf79(0x0) = CONST 
    0xf7d: MSTORE vf79(0x0), vf78
    0xf7e: vf7e(0x5) = CONST 
    0xf80: vf80(0x20) = CONST 
    0xf82: MSTORE vf80(0x20), vf7e(0x5)
    0xf83: vf83(0x40) = CONST 
    0xf86: vf86 = SHA3 vf79(0x0), vf83(0x40)
    0xf87: vf87 = SLOAD vf86
    0xf88: vf88(0xff) = CONST 
    0xf8a: vf8a = AND vf88(0xff), vf87
    0xf8b: vf8b(0xfcc) = CONST 
    0xf8e: JUMPI vf8b(0xfcc), vf8a

    Begin block 0xf8f
    prev=[0xf77], succ=[]
    =================================
    0xf8f: vf8f(0x40) = CONST 
    0xf92: vf92 = MLOAD vf8f(0x40)
    0xf93: vf93(0x461bcd) = CONST 
    0xf97: vf97(0xe5) = CONST 
    0xf99: vf99(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf97(0xe5), vf93(0x461bcd)
    0xf9b: MSTORE vf92, vf99(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf9c: vf9c(0x20) = CONST 
    0xf9e: vf9e(0x4) = CONST 
    0xfa1: vfa1 = ADD vf92, vf9e(0x4)
    0xfa2: MSTORE vfa1, vf9c(0x20)
    0xfa3: vfa3(0xe) = CONST 
    0xfa5: vfa5(0x24) = CONST 
    0xfa8: vfa8 = ADD vf92, vfa5(0x24)
    0xfa9: MSTORE vfa8, vfa3(0xe)
    0xfaa: vfaa(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0xfb9: vfb9(0x91) = CONST 
    0xfbb: vfbb(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL vfb9(0x91), vfaa(0x36bab9ba1031329036b4b73a32b9)
    0xfbc: vfbc(0x44) = CONST 
    0xfbf: vfbf = ADD vf92, vfbc(0x44)
    0xfc0: MSTORE vfbf, vfbb(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0xfc2: vfc2 = MLOAD vf8f(0x40)
    0xfc6: vfc6(0x0) = SUB vf92, vfc2
    0xfc7: vfc7(0x64) = CONST 
    0xfc9: vfc9(0x64) = ADD vfc7(0x64), vfc6(0x0)
    0xfcb: REVERT vfc2, vfc9(0x64)

    Begin block 0xfcc
    prev=[0xf77], succ=[0x1f0aB0xfcc]
    =================================
    0xfcd: vfcd(0x2d3f) = CONST 
    0xfd2: vfd2(0x1f0a) = CONST 
    0xfd5: JUMP vfd2(0x1f0a)

    Begin block 0x1f0aB0xfcc
    prev=[0xfcc], succ=[0x1f1bB0xfcc, 0x1f67B0xfcc]
    =================================
    0x1f0bS0xfcc: v1f0bVfcc(0x0) = CONST 
    0x1f0dS0xfcc: v1f0dVfcc(0x1) = CONST 
    0x1f0fS0xfcc: v1f0fVfcc(0x1) = CONST 
    0x1f11S0xfcc: v1f11Vfcc(0xa0) = CONST 
    0x1f13S0xfcc: v1f13Vfcc(0x10000000000000000000000000000000000000000) = SHL v1f11Vfcc(0xa0), v1f0fVfcc(0x1)
    0x1f14S0xfcc: v1f14Vfcc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f13Vfcc(0x10000000000000000000000000000000000000000), v1f0dVfcc(0x1)
    0x1f16S0xfcc: v1f16Vfcc = AND v51e, v1f14Vfcc(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f17S0xfcc: v1f17Vfcc(0x1f67) = CONST 
    0x1f1aS0xfcc: JUMPI v1f17Vfcc(0x1f67), v1f16Vfcc

    Begin block 0x1f1bB0xfcc
    prev=[0x1f0aB0xfcc], succ=[]
    =================================
    0x1f1bS0xfcc: v1f1bVfcc(0x40) = CONST 
    0x1f1eS0xfcc: v1f1eVfcc = MLOAD v1f1bVfcc(0x40)
    0x1f1fS0xfcc: v1f1fVfcc(0x461bcd) = CONST 
    0x1f23S0xfcc: v1f23Vfcc(0xe5) = CONST 
    0x1f25S0xfcc: v1f25Vfcc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f23Vfcc(0xe5), v1f1fVfcc(0x461bcd)
    0x1f27S0xfcc: MSTORE v1f1eVfcc, v1f25Vfcc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f28S0xfcc: v1f28Vfcc(0x20) = CONST 
    0x1f2aS0xfcc: v1f2aVfcc(0x4) = CONST 
    0x1f2dS0xfcc: v1f2dVfcc = ADD v1f1eVfcc, v1f2aVfcc(0x4)
    0x1f2eS0xfcc: MSTORE v1f2dVfcc, v1f28Vfcc(0x20)
    0x1f2fS0xfcc: v1f2fVfcc(0x1d) = CONST 
    0x1f31S0xfcc: v1f31Vfcc(0x24) = CONST 
    0x1f34S0xfcc: v1f34Vfcc = ADD v1f1eVfcc, v1f31Vfcc(0x24)
    0x1f35S0xfcc: MSTORE v1f34Vfcc, v1f2fVfcc(0x1d)
    0x1f36S0xfcc: v1f36Vfcc(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x1f57S0xfcc: v1f57Vfcc(0x44) = CONST 
    0x1f5aS0xfcc: v1f5aVfcc = ADD v1f1eVfcc, v1f57Vfcc(0x44)
    0x1f5bS0xfcc: MSTORE v1f5aVfcc, v1f36Vfcc(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x1f5dS0xfcc: v1f5dVfcc = MLOAD v1f1bVfcc(0x40)
    0x1f61S0xfcc: v1f61Vfcc(0x0) = SUB v1f1eVfcc, v1f5dVfcc
    0x1f62S0xfcc: v1f62Vfcc(0x64) = CONST 
    0x1f64S0xfcc: v1f64Vfcc(0x64) = ADD v1f62Vfcc(0x64), v1f61Vfcc(0x0)
    0x1f66S0xfcc: REVERT v1f5dVfcc, v1f64Vfcc(0x64)

    Begin block 0x1f67B0xfcc
    prev=[0x1f0aB0xfcc], succ=[0x2e91B0xfcc]
    =================================
    0x1f68S0xfcc: v1f68Vfcc(0x6) = CONST 
    0x1f6bS0xfcc: v1f6bVfcc = SLOAD v1f68Vfcc(0x6)
    0x1f6cS0xfcc: v1f6cVfcc(0x1) = CONST 
    0x1f70S0xfcc: v1f70Vfcc = ADD v1f6cVfcc(0x1), v1f6bVfcc
    0x1f74S0xfcc: SSTORE v1f68Vfcc(0x6), v1f70Vfcc
    0x1f75S0xfcc: v1f75Vfcc(0x0) = CONST 
    0x1f79S0xfcc: MSTORE v1f75Vfcc(0x0), v1f70Vfcc
    0x1f7aS0xfcc: v1f7aVfcc(0x7) = CONST 
    0x1f7cS0xfcc: v1f7cVfcc(0x20) = CONST 
    0x1f80S0xfcc: MSTORE v1f7cVfcc(0x20), v1f7aVfcc(0x7)
    0x1f81S0xfcc: v1f81Vfcc(0x40) = CONST 
    0x1f85S0xfcc: v1f85Vfcc = SHA3 v1f75Vfcc(0x0), v1f81Vfcc(0x40)
    0x1f87S0xfcc: v1f87Vfcc = SLOAD v1f85Vfcc
    0x1f88S0xfcc: v1f88Vfcc(0x1) = CONST 
    0x1f8aS0xfcc: v1f8aVfcc(0x1) = CONST 
    0x1f8cS0xfcc: v1f8cVfcc(0xa0) = CONST 
    0x1f8eS0xfcc: v1f8eVfcc(0x10000000000000000000000000000000000000000) = SHL v1f8cVfcc(0xa0), v1f8aVfcc(0x1)
    0x1f8fS0xfcc: v1f8fVfcc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f8eVfcc(0x10000000000000000000000000000000000000000), v1f88Vfcc(0x1)
    0x1f90S0xfcc: v1f90Vfcc(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1f8fVfcc(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f91S0xfcc: v1f91Vfcc = AND v1f90Vfcc(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f87Vfcc
    0x1f92S0xfcc: v1f92Vfcc(0x1) = CONST 
    0x1f94S0xfcc: v1f94Vfcc(0x1) = CONST 
    0x1f96S0xfcc: v1f96Vfcc(0xa0) = CONST 
    0x1f98S0xfcc: v1f98Vfcc(0x10000000000000000000000000000000000000000) = SHL v1f96Vfcc(0xa0), v1f94Vfcc(0x1)
    0x1f99S0xfcc: v1f99Vfcc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f98Vfcc(0x10000000000000000000000000000000000000000), v1f92Vfcc(0x1)
    0x1f9bS0xfcc: v1f9bVfcc = AND v51e, v1f99Vfcc(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f9eS0xfcc: v1f9eVfcc = OR v1f9bVfcc, v1f91Vfcc
    0x1fa1S0xfcc: SSTORE v1f85Vfcc, v1f9eVfcc
    0x1fa3S0xfcc: v1fa3Vfcc = MLOAD v1f81Vfcc(0x40)
    0x1fa6S0xfcc: MSTORE v1fa3Vfcc, v1f70Vfcc
    0x1fa9S0xfcc: v1fa9Vfcc = ADD v1fa3Vfcc, v1f7cVfcc(0x20)
    0x1fadS0xfcc: MSTORE v1fa9Vfcc, v1f6cVfcc(0x1)
    0x1fafS0xfcc: v1fafVfcc = MLOAD v1f81Vfcc(0x40)
    0x1fb0S0xfcc: v1fb0Vfcc = CALLER 
    0x1fb2S0xfcc: v1fb2Vfcc(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x1fd7S0xfcc: v1fd7Vfcc(0x0) = SUB v1fa3Vfcc, v1fafVfcc
    0x1fd8S0xfcc: v1fd8Vfcc(0x40) = ADD v1fd7Vfcc(0x0), v1f81Vfcc(0x40)
    0x1fdaS0xfcc: LOG4 v1fafVfcc, v1fd8Vfcc(0x40), v1fb2Vfcc(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v1fb0Vfcc, v1f75Vfcc(0x0), v1f9bVfcc
    0x1fdbS0xfcc: v1fdbVfcc(0x2e91) = CONST 
    0x1fdeS0xfcc: v1fdeVfcc = CALLER 
    0x1fdfS0xfcc: v1fdfVfcc(0x0) = CONST 
    0x1fe3S0xfcc: v1fe3Vfcc(0x1) = CONST 
    0x1fe5S0xfcc: v1fe5Vfcc(0x40) = CONST 
    0x1fe7S0xfcc: v1fe7Vfcc = MLOAD v1fe5Vfcc(0x40)
    0x1fe9S0xfcc: v1fe9Vfcc(0x20) = CONST 
    0x1febS0xfcc: v1febVfcc = ADD v1fe9Vfcc(0x20), v1fe7Vfcc
    0x1fecS0xfcc: v1fecVfcc(0x40) = CONST 
    0x1feeS0xfcc: MSTORE v1fecVfcc(0x40), v1febVfcc
    0x1ff0S0xfcc: v1ff0Vfcc(0x0) = CONST 
    0x1ff3S0xfcc: MSTORE v1fe7Vfcc, v1ff0Vfcc(0x0)
    0x1ff5S0xfcc: v1ff5Vfcc(0x23fc) = CONST 
    0x1ff8S0xfcc: CALLPRIVATE v1ff5Vfcc(0x23fc), v1fe7Vfcc, v1fe3Vfcc(0x1), v1f70Vfcc, v51e, v1fdfVfcc(0x0), v1fdeVfcc, v1fdbVfcc(0x2e91)

    Begin block 0x2e91B0xfcc
    prev=[0x1f67B0xfcc], succ=[0x2d3f]
    =================================
    0x2e97S0xfcc: JUMP vfcd(0x2d3f)

    Begin block 0x2d3f
    prev=[0x2e91B0xfcc], succ=[0x2a41]
    =================================
    0x2d45: JUMP v4fd(0x2a41)

    Begin block 0x2a41
    prev=[0x2d3f], succ=[]
    =================================
    0x2a42: v2a42(0x40) = CONST 
    0x2a45: v2a45 = MLOAD v2a42(0x40)
    0x2a48: MSTORE v2a45, v1f70Vfcc
    0x2a49: v2a49 = MLOAD v2a42(0x40)
    0x2a4d: v2a4d(0x0) = SUB v2a45, v2a49
    0x2a4e: v2a4e(0x20) = CONST 
    0x2a50: v2a50(0x20) = ADD v2a4e(0x20), v2a4d(0x0)
    0x2a52: RETURN v2a49, v2a50(0x20)

}

function initialize(address,address)() public {
    Begin block 0x528
    prev=[], succ=[0x53a, 0x53e]
    =================================
    0x529: v529(0x2a72) = CONST 
    0x52c: v52c(0x4) = CONST 
    0x52f: v52f = CALLDATASIZE 
    0x530: v530 = SUB v52f, v52c(0x4)
    0x531: v531(0x40) = CONST 
    0x534: v534 = LT v530, v531(0x40)
    0x535: v535 = ISZERO v534
    0x536: v536(0x53e) = CONST 
    0x539: JUMPI v536(0x53e), v535

    Begin block 0x53a
    prev=[0x528], succ=[]
    =================================
    0x53a: v53a(0x0) = CONST 
    0x53d: REVERT v53a(0x0), v53a(0x0)

    Begin block 0x53e
    prev=[0x528], succ=[0xfdd]
    =================================
    0x540: v540(0x1) = CONST 
    0x542: v542(0x1) = CONST 
    0x544: v544(0xa0) = CONST 
    0x546: v546(0x10000000000000000000000000000000000000000) = SHL v544(0xa0), v542(0x1)
    0x547: v547(0xffffffffffffffffffffffffffffffffffffffff) = SUB v546(0x10000000000000000000000000000000000000000), v540(0x1)
    0x549: v549 = CALLDATALOAD v52c(0x4)
    0x54b: v54b = AND v547(0xffffffffffffffffffffffffffffffffffffffff), v549
    0x54d: v54d(0x20) = CONST 
    0x54f: v54f(0x24) = ADD v54d(0x20), v52c(0x4)
    0x550: v550 = CALLDATALOAD v54f(0x24)
    0x551: v551 = AND v550, v547(0xffffffffffffffffffffffffffffffffffffffff)
    0x552: v552(0xfdd) = CONST 
    0x555: JUMP v552(0xfdd)

    Begin block 0xfdd
    prev=[0x53e], succ=[0xfe9, 0x1035]
    =================================
    0xfde: vfde(0x1) = CONST 
    0xfe0: vfe0 = SLOAD vfde(0x1)
    0xfe1: vfe1(0xff) = CONST 
    0xfe3: vfe3 = AND vfe1(0xff), vfe0
    0xfe4: vfe4 = ISZERO vfe3
    0xfe5: vfe5(0x1035) = CONST 
    0xfe8: JUMPI vfe5(0x1035), vfe4

    Begin block 0xfe9
    prev=[0xfdd], succ=[]
    =================================
    0xfe9: vfe9(0x40) = CONST 
    0xfec: vfec = MLOAD vfe9(0x40)
    0xfed: vfed(0x461bcd) = CONST 
    0xff1: vff1(0xe5) = CONST 
    0xff3: vff3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vff1(0xe5), vfed(0x461bcd)
    0xff5: MSTORE vfec, vff3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xff6: vff6(0x20) = CONST 
    0xff8: vff8(0x4) = CONST 
    0xffb: vffb = ADD vfec, vff8(0x4)
    0xffc: MSTORE vffb, vff6(0x20)
    0xffd: vffd(0x1c) = CONST 
    0xfff: vfff(0x24) = CONST 
    0x1002: v1002 = ADD vfec, vfff(0x24)
    0x1003: MSTORE v1002, vffd(0x1c)
    0x1004: v1004(0x436f6e747261637420616c726561647920696e697469616c697a656400000000) = CONST 
    0x1025: v1025(0x44) = CONST 
    0x1028: v1028 = ADD vfec, v1025(0x44)
    0x1029: MSTORE v1028, v1004(0x436f6e747261637420616c726561647920696e697469616c697a656400000000)
    0x102b: v102b = MLOAD vfe9(0x40)
    0x102f: v102f(0x0) = SUB vfec, v102b
    0x1030: v1030(0x64) = CONST 
    0x1032: v1032(0x64) = ADD v1030(0x64), v102f(0x0)
    0x1034: REVERT v102b, v1032(0x64)

    Begin block 0x1035
    prev=[0xfdd], succ=[0x1044, 0x1090]
    =================================
    0x1036: v1036(0x1) = CONST 
    0x1038: v1038(0x1) = CONST 
    0x103a: v103a(0xa0) = CONST 
    0x103c: v103c(0x10000000000000000000000000000000000000000) = SHL v103a(0xa0), v1038(0x1)
    0x103d: v103d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v103c(0x10000000000000000000000000000000000000000), v1036(0x1)
    0x103f: v103f = AND v54b, v103d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1040: v1040(0x1090) = CONST 
    0x1043: JUMPI v1040(0x1090), v103f

    Begin block 0x1044
    prev=[0x1035], succ=[]
    =================================
    0x1044: v1044(0x40) = CONST 
    0x1047: v1047 = MLOAD v1044(0x40)
    0x1048: v1048(0x461bcd) = CONST 
    0x104c: v104c(0xe5) = CONST 
    0x104e: v104e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v104c(0xe5), v1048(0x461bcd)
    0x1050: MSTORE v1047, v104e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1051: v1051(0x20) = CONST 
    0x1053: v1053(0x4) = CONST 
    0x1056: v1056 = ADD v1047, v1053(0x4)
    0x1057: MSTORE v1056, v1051(0x20)
    0x1058: v1058(0x1e) = CONST 
    0x105a: v105a(0x24) = CONST 
    0x105d: v105d = ADD v1047, v105a(0x24)
    0x105e: MSTORE v105d, v1058(0x1e)
    0x105f: v105f(0x4f776e6572206d757374206e6f74206265206e756c6c20616464726573730000) = CONST 
    0x1080: v1080(0x44) = CONST 
    0x1083: v1083 = ADD v1047, v1080(0x44)
    0x1084: MSTORE v1083, v105f(0x4f776e6572206d757374206e6f74206265206e756c6c20616464726573730000)
    0x1086: v1086 = MLOAD v1044(0x40)
    0x108a: v108a(0x0) = SUB v1047, v1086
    0x108b: v108b(0x64) = CONST 
    0x108d: v108d(0x64) = ADD v108b(0x64), v108a(0x0)
    0x108f: REVERT v1086, v108d(0x64)

    Begin block 0x1090
    prev=[0x1035], succ=[0x109f, 0x10d5]
    =================================
    0x1091: v1091(0x1) = CONST 
    0x1093: v1093(0x1) = CONST 
    0x1095: v1095(0xa0) = CONST 
    0x1097: v1097(0x10000000000000000000000000000000000000000) = SHL v1095(0xa0), v1093(0x1)
    0x1098: v1098(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1097(0x10000000000000000000000000000000000000000), v1091(0x1)
    0x109a: v109a = AND v551, v1098(0xffffffffffffffffffffffffffffffffffffffff)
    0x109b: v109b(0x10d5) = CONST 
    0x109e: JUMPI v109b(0x10d5), v109a

    Begin block 0x109f
    prev=[0x1090], succ=[]
    =================================
    0x109f: v109f(0x40) = CONST 
    0x10a1: v10a1 = MLOAD v109f(0x40)
    0x10a2: v10a2(0x461bcd) = CONST 
    0x10a6: v10a6(0xe5) = CONST 
    0x10a8: v10a8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v10a6(0xe5), v10a2(0x461bcd)
    0x10aa: MSTORE v10a1, v10a8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10ab: v10ab(0x4) = CONST 
    0x10ad: v10ad = ADD v10ab(0x4), v10a1
    0x10b0: v10b0(0x20) = CONST 
    0x10b2: v10b2 = ADD v10b0(0x20), v10ad
    0x10b5: v10b5(0x20) = SUB v10b2, v10ad
    0x10b7: MSTORE v10ad, v10b5(0x20)
    0x10b8: v10b8(0x28) = CONST 
    0x10bb: MSTORE v10b2, v10b8(0x28)
    0x10bc: v10bc(0x20) = CONST 
    0x10be: v10be = ADD v10bc(0x20), v10b2
    0x10c0: v10c0(0x277e) = CONST 
    0x10c3: v10c3(0x28) = CONST 
    0x10c6: CODECOPY v10be, v10c0(0x277e), v10c3(0x28)
    0x10c7: v10c7(0x40) = CONST 
    0x10c9: v10c9 = ADD v10c7(0x40), v10be
    0x10cd: v10cd(0x40) = CONST 
    0x10cf: v10cf = MLOAD v10cd(0x40)
    0x10d2: v10d2(0x84) = SUB v10c9, v10cf
    0x10d4: REVERT v10cf, v10d2(0x84)

    Begin block 0x10d5
    prev=[0x1090], succ=[0x2a72]
    =================================
    0x10d6: v10d6(0x3) = CONST 
    0x10d9: v10d9 = SLOAD v10d6(0x3)
    0x10da: v10da(0x1) = CONST 
    0x10dc: v10dc(0x1) = CONST 
    0x10de: v10de(0xa0) = CONST 
    0x10e0: v10e0(0x10000000000000000000000000000000000000000) = SHL v10de(0xa0), v10dc(0x1)
    0x10e1: v10e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10e0(0x10000000000000000000000000000000000000000), v10da(0x1)
    0x10e4: v10e4 = AND v10e1(0xffffffffffffffffffffffffffffffffffffffff), v54b
    0x10e5: v10e5(0x1) = CONST 
    0x10e7: v10e7(0x1) = CONST 
    0x10e9: v10e9(0xa0) = CONST 
    0x10eb: v10eb(0x10000000000000000000000000000000000000000) = SHL v10e9(0xa0), v10e7(0x1)
    0x10ec: v10ec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10eb(0x10000000000000000000000000000000000000000), v10e5(0x1)
    0x10ed: v10ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10ec(0xffffffffffffffffffffffffffffffffffffffff)
    0x10f0: v10f0 = AND v10ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v10d9
    0x10f1: v10f1 = OR v10f0, v10e4
    0x10f4: SSTORE v10d6(0x3), v10f1
    0x10f5: v10f5(0x4) = CONST 
    0x10f8: v10f8 = SLOAD v10f5(0x4)
    0x10fc: v10fc = AND v10e1(0xffffffffffffffffffffffffffffffffffffffff), v551
    0x10fe: v10fe = AND v10f8, v10ed(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x10ff: v10ff = OR v10fe, v10fc
    0x1101: SSTORE v10f5(0x4), v10ff
    0x1102: v1102(0x1) = CONST 
    0x1105: v1105 = SLOAD v1102(0x1)
    0x1106: v1106(0xff) = CONST 
    0x1108: v1108(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1106(0xff)
    0x1109: v1109 = AND v1108(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1105
    0x110b: v110b = OR v1102(0x1), v1109
    0x110d: SSTORE v1102(0x1), v110b
    0x110e: JUMP v529(0x2a72)

    Begin block 0x2a72
    prev=[0x10d5], succ=[]
    =================================
    0x2a73: STOP 

}

function balanceOfBatch(address[],uint256[])() public {
    Begin block 0x556
    prev=[], succ=[0x568, 0x56c]
    =================================
    0x557: v557(0x679) = CONST 
    0x55a: v55a(0x4) = CONST 
    0x55d: v55d = CALLDATASIZE 
    0x55e: v55e = SUB v55d, v55a(0x4)
    0x55f: v55f(0x40) = CONST 
    0x562: v562 = LT v55e, v55f(0x40)
    0x563: v563 = ISZERO v562
    0x564: v564(0x56c) = CONST 
    0x567: JUMPI v564(0x56c), v563

    Begin block 0x568
    prev=[0x556], succ=[]
    =================================
    0x568: v568(0x0) = CONST 
    0x56b: REVERT v568(0x0), v568(0x0)

    Begin block 0x56c
    prev=[0x556], succ=[0x582, 0x586]
    =================================
    0x56e: v56e = ADD v55a(0x4), v55e
    0x570: v570(0x20) = CONST 
    0x573: v573(0x24) = ADD v55a(0x4), v570(0x20)
    0x575: v575 = CALLDATALOAD v55a(0x4)
    0x576: v576(0x1) = CONST 
    0x578: v578(0x20) = CONST 
    0x57a: v57a(0x100000000) = SHL v578(0x20), v576(0x1)
    0x57c: v57c = GT v575, v57a(0x100000000)
    0x57d: v57d = ISZERO v57c
    0x57e: v57e(0x586) = CONST 
    0x581: JUMPI v57e(0x586), v57d

    Begin block 0x582
    prev=[0x56c], succ=[]
    =================================
    0x582: v582(0x0) = CONST 
    0x585: REVERT v582(0x0), v582(0x0)

    Begin block 0x586
    prev=[0x56c], succ=[0x594, 0x598]
    =================================
    0x588: v588 = ADD v55a(0x4), v575
    0x58a: v58a(0x20) = CONST 
    0x58d: v58d = ADD v588, v58a(0x20)
    0x58e: v58e = GT v58d, v56e
    0x58f: v58f = ISZERO v58e
    0x590: v590(0x598) = CONST 
    0x593: JUMPI v590(0x598), v58f

    Begin block 0x594
    prev=[0x586], succ=[]
    =================================
    0x594: v594(0x0) = CONST 
    0x597: REVERT v594(0x0), v594(0x0)

    Begin block 0x598
    prev=[0x586], succ=[0x5b5, 0x5b9]
    =================================
    0x59a: v59a = CALLDATALOAD v588
    0x59c: v59c(0x20) = CONST 
    0x59e: v59e = ADD v59c(0x20), v588
    0x5a1: v5a1(0x20) = CONST 
    0x5a4: v5a4 = MUL v59a, v5a1(0x20)
    0x5a6: v5a6 = ADD v59e, v5a4
    0x5a7: v5a7 = GT v5a6, v56e
    0x5a8: v5a8(0x1) = CONST 
    0x5aa: v5aa(0x20) = CONST 
    0x5ac: v5ac(0x100000000) = SHL v5aa(0x20), v5a8(0x1)
    0x5ae: v5ae = GT v59a, v5ac(0x100000000)
    0x5af: v5af = OR v5ae, v5a7
    0x5b0: v5b0 = ISZERO v5af
    0x5b1: v5b1(0x5b9) = CONST 
    0x5b4: JUMPI v5b1(0x5b9), v5b0

    Begin block 0x5b5
    prev=[0x598], succ=[]
    =================================
    0x5b5: v5b5(0x0) = CONST 
    0x5b8: REVERT v5b5(0x0), v5b5(0x0)

    Begin block 0x5b9
    prev=[0x598], succ=[0x604, 0x608]
    =================================
    0x5be: v5be(0x20) = CONST 
    0x5c0: v5c0 = MUL v5be(0x20), v59a
    0x5c1: v5c1(0x20) = CONST 
    0x5c3: v5c3 = ADD v5c1(0x20), v5c0
    0x5c4: v5c4(0x40) = CONST 
    0x5c6: v5c6 = MLOAD v5c4(0x40)
    0x5c9: v5c9 = ADD v5c6, v5c3
    0x5ca: v5ca(0x40) = CONST 
    0x5cc: MSTORE v5ca(0x40), v5c9
    0x5d4: MSTORE v5c6, v59a
    0x5d5: v5d5(0x20) = CONST 
    0x5d7: v5d7 = ADD v5d5(0x20), v5c6
    0x5da: v5da(0x20) = CONST 
    0x5dc: v5dc = MUL v5da(0x20), v59a
    0x5e0: CALLDATACOPY v5d7, v59e, v5dc
    0x5e1: v5e1(0x0) = CONST 
    0x5e4: v5e4 = ADD v5d7, v5dc
    0x5e8: MSTORE v5e4, v5e1(0x0)
    0x5ee: v5ee(0x20) = CONST 
    0x5f1: v5f1(0x44) = ADD v573(0x24), v5ee(0x20)
    0x5f4: v5f4 = CALLDATALOAD v573(0x24)
    0x5f8: v5f8(0x1) = CONST 
    0x5fa: v5fa(0x20) = CONST 
    0x5fc: v5fc(0x100000000) = SHL v5fa(0x20), v5f8(0x1)
    0x5fe: v5fe = GT v5f4, v5fc(0x100000000)
    0x5ff: v5ff = ISZERO v5fe
    0x600: v600(0x608) = CONST 
    0x603: JUMPI v600(0x608), v5ff

    Begin block 0x604
    prev=[0x5b9], succ=[]
    =================================
    0x604: v604(0x0) = CONST 
    0x607: REVERT v604(0x0), v604(0x0)

    Begin block 0x608
    prev=[0x5b9], succ=[0x616, 0x61a]
    =================================
    0x60a: v60a = ADD v55a(0x4), v5f4
    0x60c: v60c(0x20) = CONST 
    0x60f: v60f = ADD v60a, v60c(0x20)
    0x610: v610 = GT v60f, v56e
    0x611: v611 = ISZERO v610
    0x612: v612(0x61a) = CONST 
    0x615: JUMPI v612(0x61a), v611

    Begin block 0x616
    prev=[0x608], succ=[]
    =================================
    0x616: v616(0x0) = CONST 
    0x619: REVERT v616(0x0), v616(0x0)

    Begin block 0x61a
    prev=[0x608], succ=[0x637, 0x63b]
    =================================
    0x61c: v61c = CALLDATALOAD v60a
    0x61e: v61e(0x20) = CONST 
    0x620: v620 = ADD v61e(0x20), v60a
    0x623: v623(0x20) = CONST 
    0x626: v626 = MUL v61c, v623(0x20)
    0x628: v628 = ADD v620, v626
    0x629: v629 = GT v628, v56e
    0x62a: v62a(0x1) = CONST 
    0x62c: v62c(0x20) = CONST 
    0x62e: v62e(0x100000000) = SHL v62c(0x20), v62a(0x1)
    0x630: v630 = GT v61c, v62e(0x100000000)
    0x631: v631 = OR v630, v629
    0x632: v632 = ISZERO v631
    0x633: v633(0x63b) = CONST 
    0x636: JUMPI v633(0x63b), v632

    Begin block 0x637
    prev=[0x61a], succ=[]
    =================================
    0x637: v637(0x0) = CONST 
    0x63a: REVERT v637(0x0), v637(0x0)

    Begin block 0x63b
    prev=[0x61a], succ=[0x110f]
    =================================
    0x640: v640(0x20) = CONST 
    0x642: v642 = MUL v640(0x20), v61c
    0x643: v643(0x20) = CONST 
    0x645: v645 = ADD v643(0x20), v642
    0x646: v646(0x40) = CONST 
    0x648: v648 = MLOAD v646(0x40)
    0x64b: v64b = ADD v648, v645
    0x64c: v64c(0x40) = CONST 
    0x64e: MSTORE v64c(0x40), v64b
    0x656: MSTORE v648, v61c
    0x657: v657(0x20) = CONST 
    0x659: v659 = ADD v657(0x20), v648
    0x65c: v65c(0x20) = CONST 
    0x65e: v65e = MUL v65c(0x20), v61c
    0x662: CALLDATACOPY v659, v620, v65e
    0x663: v663(0x0) = CONST 
    0x666: v666 = ADD v659, v65e
    0x66a: MSTORE v666, v663(0x0)
    0x66f: v66f(0x110f) = CONST 
    0x678: JUMP v66f(0x110f)

    Begin block 0x110f
    prev=[0x63b], succ=[0x111b, 0x1151]
    =================================
    0x1110: v1110(0x60) = CONST 
    0x1113: v1113 = MLOAD v648
    0x1115: v1115 = MLOAD v5c6
    0x1116: v1116 = EQ v1115, v1113
    0x1117: v1117(0x1151) = CONST 
    0x111a: JUMPI v1117(0x1151), v1116

    Begin block 0x111b
    prev=[0x110f], succ=[]
    =================================
    0x111b: v111b(0x40) = CONST 
    0x111d: v111d = MLOAD v111b(0x40)
    0x111e: v111e(0x461bcd) = CONST 
    0x1122: v1122(0xe5) = CONST 
    0x1124: v1124(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1122(0xe5), v111e(0x461bcd)
    0x1126: MSTORE v111d, v1124(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1127: v1127(0x4) = CONST 
    0x1129: v1129 = ADD v1127(0x4), v111d
    0x112c: v112c(0x20) = CONST 
    0x112e: v112e = ADD v112c(0x20), v1129
    0x1131: v1131(0x20) = SUB v112e, v1129
    0x1133: MSTORE v1129, v1131(0x20)
    0x1134: v1134(0x24) = CONST 
    0x1137: MSTORE v112e, v1134(0x24)
    0x1138: v1138(0x20) = CONST 
    0x113a: v113a = ADD v1138(0x20), v112e
    0x113c: v113c(0x27c9) = CONST 
    0x113f: v113f(0x24) = CONST 
    0x1142: CODECOPY v113a, v113c(0x27c9), v113f(0x24)
    0x1143: v1143(0x40) = CONST 
    0x1145: v1145 = ADD v1143(0x40), v113a
    0x1149: v1149(0x40) = CONST 
    0x114b: v114b = MLOAD v1149(0x40)
    0x114e: v114e(0x84) = SUB v1145, v114b
    0x1150: REVERT v114b, v114e(0x84)

    Begin block 0x1151
    prev=[0x110f], succ=[0x1167, 0x116b]
    =================================
    0x1152: v1152(0x0) = CONST 
    0x1155: v1155 = MLOAD v5c6
    0x1156: v1156(0xffffffffffffffff) = CONST 
    0x1160: v1160 = GT v1155, v1156(0xffffffffffffffff)
    0x1162: v1162 = ISZERO v1160
    0x1163: v1163(0x116b) = CONST 
    0x1166: JUMPI v1163(0x116b), v1162

    Begin block 0x1167
    prev=[0x1151], succ=[]
    =================================
    0x1167: v1167(0x0) = CONST 
    0x116a: REVERT v1167(0x0), v1167(0x0)

    Begin block 0x116b
    prev=[0x1151], succ=[0x1195, 0x1186]
    =================================
    0x116d: v116d(0x40) = CONST 
    0x116f: v116f = MLOAD v116d(0x40)
    0x1173: MSTORE v116f, v1155
    0x1175: v1175(0x20) = CONST 
    0x1177: v1177 = MUL v1175(0x20), v1155
    0x1178: v1178(0x20) = CONST 
    0x117a: v117a = ADD v1178(0x20), v1177
    0x117c: v117c = ADD v116f, v117a
    0x117d: v117d(0x40) = CONST 
    0x117f: MSTORE v117d(0x40), v117c
    0x1181: v1181 = ISZERO v1155
    0x1182: v1182(0x1195) = CONST 
    0x1185: JUMPI v1182(0x1195), v1181

    Begin block 0x1195
    prev=[0x116b, 0x1186], succ=[0x119b]
    =================================
    0x1199: v1199(0x0) = CONST 

    Begin block 0x119b
    prev=[0x1195, 0x11e0], succ=[0x11a5, 0x11f3]
    =================================
    0x119b_0x0: v119b_0 = PHI v1199(0x0), v11ee
    0x119d: v119d = MLOAD v5c6
    0x119f: v119f = LT v119b_0, v119d
    0x11a0: v11a0 = ISZERO v119f
    0x11a1: v11a1(0x11f3) = CONST 
    0x11a4: JUMPI v11a1(0x11f3), v11a0

    Begin block 0x11a5
    prev=[0x119b], succ=[0x11b2, 0x11b3]
    =================================
    0x11a5: v11a5(0x11d4) = CONST 
    0x11a5_0x0: v11a5_0 = PHI v1199(0x0), v11ee
    0x11ab: v11ab = MLOAD v5c6
    0x11ad: v11ad = LT v11a5_0, v11ab
    0x11ae: v11ae(0x11b3) = CONST 
    0x11b1: JUMPI v11ae(0x11b3), v11ad

    Begin block 0x11b2
    prev=[0x11a5], succ=[]
    =================================
    0x11b2: THROW 

    Begin block 0x11b3
    prev=[0x11a5], succ=[0x11c6, 0x11c7]
    =================================
    0x11b3_0x0: v11b3_0 = PHI v1199(0x0), v11ee
    0x11b3_0x3: v11b3_3 = PHI v1199(0x0), v11ee
    0x11b4: v11b4(0x20) = CONST 
    0x11b6: v11b6 = MUL v11b4(0x20), v11b3_0
    0x11b7: v11b7(0x20) = CONST 
    0x11b9: v11b9 = ADD v11b7(0x20), v11b6
    0x11ba: v11ba = ADD v11b9, v5c6
    0x11bb: v11bb = MLOAD v11ba
    0x11bf: v11bf = MLOAD v648
    0x11c1: v11c1 = LT v11b3_3, v11bf
    0x11c2: v11c2(0x11c7) = CONST 
    0x11c5: JUMPI v11c2(0x11c7), v11c1

    Begin block 0x11c6
    prev=[0x11b3], succ=[]
    =================================
    0x11c6: THROW 

    Begin block 0x11c7
    prev=[0x11b3], succ=[0xa130x556]
    =================================
    0x11c7_0x0: v11c7_0 = PHI v1199(0x0), v11ee
    0x11c8: v11c8(0x20) = CONST 
    0x11ca: v11ca = MUL v11c8(0x20), v11c7_0
    0x11cb: v11cb(0x20) = CONST 
    0x11cd: v11cd = ADD v11cb(0x20), v11ca
    0x11ce: v11ce = ADD v11cd, v648
    0x11cf: v11cf = MLOAD v11ce
    0x11d0: v11d0(0xa13) = CONST 
    0x11d3: JUMP v11d0(0xa13)

    Begin block 0xa130x556
    prev=[0x11c7], succ=[0xa1f0x556]
    =================================
    0xa140x556: v556a14(0x0) = CONST 
    0xa160x556: v556a16(0xa1f) = CONST 
    0xa1b0x556: v556a1b(0x192e) = CONST 
    0xa1e0x556: v556a1e_0 = CALLPRIVATE v556a1b(0x192e), v11cf, v11bb, v556a16(0xa1f)

    Begin block 0xa1f0x556
    prev=[0xa130x556], succ=[0xa250x556, 0xa2c0x556]
    =================================
    0xa200x556: v556a20 = ISZERO v556a1e_0
    0xa210x556: v556a21(0xa2c) = CONST 
    0xa240x556: JUMPI v556a21(0xa2c), v556a20

    Begin block 0xa250x556
    prev=[0xa1f0x556], succ=[0x2c890x556]
    =================================
    0xa260x556: v556a26(0x1) = CONST 
    0xa280x556: v556a28(0x2c89) = CONST 
    0xa2b0x556: JUMP v556a28(0x2c89)

    Begin block 0x2c890x556
    prev=[0xa250x556], succ=[0x11d4]
    =================================
    0x2c8e0x556: JUMP v11a5(0x11d4)

    Begin block 0x11d4
    prev=[0xa300x556, 0x2c890x556], succ=[0x11df, 0x11e0]
    =================================
    0x11d4_0x1: v11d4_1 = PHI v1199(0x0), v11ee
    0x11d8: v11d8 = MLOAD v116f
    0x11da: v11da = LT v11d4_1, v11d8
    0x11db: v11db(0x11e0) = CONST 
    0x11de: JUMPI v11db(0x11e0), v11da

    Begin block 0x11df
    prev=[0x11d4], succ=[]
    =================================
    0x11df: THROW 

    Begin block 0x11e0
    prev=[0x11d4], succ=[0x119b]
    =================================
    0x11e0_0x0: v11e0_0 = PHI v1199(0x0), v11ee
    0x11e0_0x2: v11e0_2 = PHI v556a2e(0x0), v556a26(0x1)
    0x11e0_0x3: v11e0_3 = PHI v1199(0x0), v11ee
    0x11e1: v11e1(0x20) = CONST 
    0x11e5: v11e5 = MUL v11e1(0x20), v11e0_0
    0x11e9: v11e9 = ADD v11e5, v116f
    0x11ea: v11ea = ADD v11e9, v11e1(0x20)
    0x11eb: MSTORE v11ea, v11e0_2
    0x11ec: v11ec(0x1) = CONST 
    0x11ee: v11ee = ADD v11ec(0x1), v11e0_3
    0x11ef: v11ef(0x119b) = CONST 
    0x11f2: JUMP v11ef(0x119b)

    Begin block 0xa2c0x556
    prev=[0xa1f0x556], succ=[0xa300x556]
    =================================
    0xa2e0x556: v556a2e(0x0) = CONST 

    Begin block 0xa300x556
    prev=[0xa2c0x556], succ=[0x11d4]
    =================================
    0xa350x556: JUMP v11a5(0x11d4)

    Begin block 0x11f3
    prev=[0x119b], succ=[0x6790x556]
    =================================
    0x11fa: JUMP v557(0x679)

    Begin block 0x6790x556
    prev=[0x11f3], succ=[0x69d0x556]
    =================================
    0x67a0x556: v55667a(0x40) = CONST 
    0x67d0x556: v55667d = MLOAD v55667a(0x40)
    0x67e0x556: v55667e(0x20) = CONST 
    0x6820x556: MSTORE v55667d, v55667e(0x20)
    0x6840x556: v556684 = MLOAD v116f
    0x6870x556: v556687 = ADD v55667d, v55667e(0x20)
    0x6880x556: MSTORE v556687, v556684
    0x68a0x556: v55668a = MLOAD v116f
    0x6910x556: v556691 = ADD v55667d, v55667a(0x40)
    0x6950x556: v556695 = ADD v55667e(0x20), v116f
    0x6970x556: v556697 = MUL v55668a, v55667e(0x20)
    0x69b0x556: v55669b(0x0) = CONST 

    Begin block 0x69d0x556
    prev=[0x6a60x556, 0x6790x556], succ=[0x6a60x556, 0x6b50x556]
    =================================
    0x69d0x556_0x0: v69d556_0 = PHI v5566b0, v55669b(0x0)
    0x6a00x556: v5566a0 = LT v69d556_0, v556697
    0x6a10x556: v5566a1 = ISZERO v5566a0
    0x6a20x556: v5566a2(0x6b5) = CONST 
    0x6a50x556: JUMPI v5566a2(0x6b5), v5566a1

    Begin block 0x6a60x556
    prev=[0x69d0x556], succ=[0x69d0x556]
    =================================
    0x6a60x556_0x0: v6a6556_0 = PHI v5566b0, v55669b(0x0)
    0x6a80x556: v5566a8 = ADD v6a6556_0, v556695
    0x6a90x556: v5566a9 = MLOAD v5566a8
    0x6ac0x556: v5566ac = ADD v6a6556_0, v556691
    0x6ad0x556: MSTORE v5566ac, v5566a9
    0x6ae0x556: v5566ae(0x20) = CONST 
    0x6b00x556: v5566b0 = ADD v5566ae(0x20), v6a6556_0
    0x6b10x556: v5566b1(0x69d) = CONST 
    0x6b40x556: JUMP v5566b1(0x69d)

    Begin block 0x6b50x556
    prev=[0x69d0x556], succ=[]
    =================================
    0x6bc0x556: v5566bc = ADD v556697, v556691
    0x6c10x556: v5566c1(0x40) = CONST 
    0x6c30x556: v5566c3 = MLOAD v5566c1(0x40)
    0x6c60x556: v5566c6 = SUB v5566bc, v5566c3
    0x6c80x556: RETURN v5566c3, v5566c6

    Begin block 0x1186
    prev=[0x116b], succ=[0x1195]
    =================================
    0x1187: v1187(0x20) = CONST 
    0x1189: v1189 = ADD v1187(0x20), v116f
    0x118a: v118a(0x20) = CONST 
    0x118d: v118d = MUL v1155, v118a(0x20)
    0x118f: v118f = CALLDATASIZE 
    0x1191: CALLDATACOPY v1189, v118f, v118d
    0x1192: v1192 = ADD v118d, v1189

}

function transferOwner(address)() public {
    Begin block 0x6c9
    prev=[], succ=[0x6db, 0x6df]
    =================================
    0x6ca: v6ca(0x2a93) = CONST 
    0x6cd: v6cd(0x4) = CONST 
    0x6d0: v6d0 = CALLDATASIZE 
    0x6d1: v6d1 = SUB v6d0, v6cd(0x4)
    0x6d2: v6d2(0x20) = CONST 
    0x6d5: v6d5 = LT v6d1, v6d2(0x20)
    0x6d6: v6d6 = ISZERO v6d5
    0x6d7: v6d7(0x6df) = CONST 
    0x6da: JUMPI v6d7(0x6df), v6d6

    Begin block 0x6db
    prev=[0x6c9], succ=[]
    =================================
    0x6db: v6db(0x0) = CONST 
    0x6de: REVERT v6db(0x0), v6db(0x0)

    Begin block 0x6df
    prev=[0x6c9], succ=[0x11fb]
    =================================
    0x6e1: v6e1 = CALLDATALOAD v6cd(0x4)
    0x6e2: v6e2(0x1) = CONST 
    0x6e4: v6e4(0x1) = CONST 
    0x6e6: v6e6(0xa0) = CONST 
    0x6e8: v6e8(0x10000000000000000000000000000000000000000) = SHL v6e6(0xa0), v6e4(0x1)
    0x6e9: v6e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6e8(0x10000000000000000000000000000000000000000), v6e2(0x1)
    0x6ea: v6ea = AND v6e9(0xffffffffffffffffffffffffffffffffffffffff), v6e1
    0x6eb: v6eb(0x11fb) = CONST 
    0x6ee: JUMP v6eb(0x11fb)

    Begin block 0x11fb
    prev=[0x6df], succ=[0x120e, 0x124a]
    =================================
    0x11fc: v11fc(0x3) = CONST 
    0x11fe: v11fe = SLOAD v11fc(0x3)
    0x11ff: v11ff(0x1) = CONST 
    0x1201: v1201(0x1) = CONST 
    0x1203: v1203(0xa0) = CONST 
    0x1205: v1205(0x10000000000000000000000000000000000000000) = SHL v1203(0xa0), v1201(0x1)
    0x1206: v1206(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1205(0x10000000000000000000000000000000000000000), v11ff(0x1)
    0x1207: v1207 = AND v1206(0xffffffffffffffffffffffffffffffffffffffff), v11fe
    0x1208: v1208 = CALLER 
    0x1209: v1209 = EQ v1208, v1207
    0x120a: v120a(0x124a) = CONST 
    0x120d: JUMPI v120a(0x124a), v1209

    Begin block 0x120e
    prev=[0x11fb], succ=[]
    =================================
    0x120e: v120e(0x40) = CONST 
    0x1211: v1211 = MLOAD v120e(0x40)
    0x1212: v1212(0x461bcd) = CONST 
    0x1216: v1216(0xe5) = CONST 
    0x1218: v1218(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1216(0xe5), v1212(0x461bcd)
    0x121a: MSTORE v1211, v1218(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x121b: v121b(0x20) = CONST 
    0x121d: v121d(0x4) = CONST 
    0x1220: v1220 = ADD v1211, v121d(0x4)
    0x1221: MSTORE v1220, v121b(0x20)
    0x1222: v1222(0xd) = CONST 
    0x1224: v1224(0x24) = CONST 
    0x1227: v1227 = ADD v1211, v1224(0x24)
    0x1228: MSTORE v1227, v1222(0xd)
    0x1229: v1229(0x26bab9ba1031329037bbb732b9) = CONST 
    0x1237: v1237(0x99) = CONST 
    0x1239: v1239(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v1237(0x99), v1229(0x26bab9ba1031329037bbb732b9)
    0x123a: v123a(0x44) = CONST 
    0x123d: v123d = ADD v1211, v123a(0x44)
    0x123e: MSTORE v123d, v1239(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x1240: v1240 = MLOAD v120e(0x40)
    0x1244: v1244(0x0) = SUB v1211, v1240
    0x1245: v1245(0x64) = CONST 
    0x1247: v1247(0x64) = ADD v1245(0x64), v1244(0x0)
    0x1249: REVERT v1240, v1247(0x64)

    Begin block 0x124a
    prev=[0x11fb], succ=[0x1259, 0x128f]
    =================================
    0x124b: v124b(0x1) = CONST 
    0x124d: v124d(0x1) = CONST 
    0x124f: v124f(0xa0) = CONST 
    0x1251: v1251(0x10000000000000000000000000000000000000000) = SHL v124f(0xa0), v124d(0x1)
    0x1252: v1252(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1251(0x10000000000000000000000000000000000000000), v124b(0x1)
    0x1254: v1254 = AND v6ea, v1252(0xffffffffffffffffffffffffffffffffffffffff)
    0x1255: v1255(0x128f) = CONST 
    0x1258: JUMPI v1255(0x128f), v1254

    Begin block 0x1259
    prev=[0x124a], succ=[]
    =================================
    0x1259: v1259(0x40) = CONST 
    0x125b: v125b = MLOAD v1259(0x40)
    0x125c: v125c(0x461bcd) = CONST 
    0x1260: v1260(0xe5) = CONST 
    0x1262: v1262(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1260(0xe5), v125c(0x461bcd)
    0x1264: MSTORE v125b, v1262(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1265: v1265(0x4) = CONST 
    0x1267: v1267 = ADD v1265(0x4), v125b
    0x126a: v126a(0x20) = CONST 
    0x126c: v126c = ADD v126a(0x20), v1267
    0x126f: v126f(0x20) = SUB v126c, v1267
    0x1271: MSTORE v1267, v126f(0x20)
    0x1272: v1272(0x22) = CONST 
    0x1275: MSTORE v126c, v1272(0x22)
    0x1276: v1276(0x20) = CONST 
    0x1278: v1278 = ADD v1276(0x20), v126c
    0x127a: v127a(0x2817) = CONST 
    0x127d: v127d(0x22) = CONST 
    0x1280: CODECOPY v1278, v127a(0x2817), v127d(0x22)
    0x1281: v1281(0x40) = CONST 
    0x1283: v1283 = ADD v1281(0x40), v1278
    0x1287: v1287(0x40) = CONST 
    0x1289: v1289 = MLOAD v1287(0x40)
    0x128c: v128c(0x84) = SUB v1283, v1289
    0x128e: REVERT v1289, v128c(0x84)

    Begin block 0x128f
    prev=[0x124a], succ=[0x2a93]
    =================================
    0x1290: v1290(0x3) = CONST 
    0x1293: v1293 = SLOAD v1290(0x3)
    0x1294: v1294(0x1) = CONST 
    0x1296: v1296(0x1) = CONST 
    0x1298: v1298(0xa0) = CONST 
    0x129a: v129a(0x10000000000000000000000000000000000000000) = SHL v1298(0xa0), v1296(0x1)
    0x129b: v129b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v129a(0x10000000000000000000000000000000000000000), v1294(0x1)
    0x129c: v129c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v129b(0xffffffffffffffffffffffffffffffffffffffff)
    0x129d: v129d = AND v129c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1293
    0x129e: v129e(0x1) = CONST 
    0x12a0: v12a0(0x1) = CONST 
    0x12a2: v12a2(0xa0) = CONST 
    0x12a4: v12a4(0x10000000000000000000000000000000000000000) = SHL v12a2(0xa0), v12a0(0x1)
    0x12a5: v12a5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12a4(0x10000000000000000000000000000000000000000), v129e(0x1)
    0x12a8: v12a8 = AND v12a5(0xffffffffffffffffffffffffffffffffffffffff), v6ea
    0x12ab: v12ab = OR v12a8, v129d
    0x12af: SSTORE v1290(0x3), v12ab
    0x12b0: v12b0(0x40) = CONST 
    0x12b2: v12b2 = MLOAD v12b0(0x40)
    0x12b5: v12b5 = AND v12ab, v12a5(0xffffffffffffffffffffffffffffffffffffffff)
    0x12b7: v12b7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x12d9: v12d9(0x0) = CONST 
    0x12dc: LOG3 v12b2, v12d9(0x0), v12b7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v12b5, v12a8
    0x12de: JUMP v6ca(0x2a93)

    Begin block 0x2a93
    prev=[0x128f], succ=[]
    =================================
    0x2a94: STOP 

}

function baseURI()() public {
    Begin block 0x6ef
    prev=[], succ=[0x2980x6ef]
    =================================
    0x6f0: v6f0(0x298) = CONST 
    0x6f3: v6f3(0x12df) = CONST 
    0x6f6: v6f6_0, v6f6_1 = CALLPRIVATE v6f3(0x12df), v6f0(0x298)

    Begin block 0x2980x6ef
    prev=[0x6ef], succ=[0x2ba0x6ef]
    =================================
    0x2990x6ef: v6ef299(0x40) = CONST 
    0x29c0x6ef: v6ef29c = MLOAD v6ef299(0x40)
    0x29d0x6ef: v6ef29d(0x20) = CONST 
    0x2a10x6ef: MSTORE v6ef29c, v6ef29d(0x20)
    0x2a30x6ef: v6ef2a3 = MLOAD v6f6_0
    0x2a60x6ef: v6ef2a6 = ADD v6ef29c, v6ef29d(0x20)
    0x2a70x6ef: MSTORE v6ef2a6, v6ef2a3
    0x2a90x6ef: v6ef2a9 = MLOAD v6f6_0
    0x2b00x6ef: v6ef2b0 = ADD v6ef29c, v6ef299(0x40)
    0x2b30x6ef: v6ef2b3 = ADD v6f6_0, v6ef29d(0x20)
    0x2b80x6ef: v6ef2b8(0x0) = CONST 

    Begin block 0x2ba0x6ef
    prev=[0x2c30x6ef, 0x2980x6ef], succ=[0x2d20x6ef, 0x2c30x6ef]
    =================================
    0x2ba0x6ef_0x0: v2ba6ef_0 = PHI v6ef2cd, v6ef2b8(0x0)
    0x2bd0x6ef: v6ef2bd = LT v2ba6ef_0, v6ef2a9
    0x2be0x6ef: v6ef2be = ISZERO v6ef2bd
    0x2bf0x6ef: v6ef2bf(0x2d2) = CONST 
    0x2c20x6ef: JUMPI v6ef2bf(0x2d2), v6ef2be

    Begin block 0x2d20x6ef
    prev=[0x2ba0x6ef], succ=[0x2ff0x6ef, 0x2e60x6ef]
    =================================
    0x2db0x6ef: v6ef2db = ADD v6ef2a9, v6ef2b0
    0x2dd0x6ef: v6ef2dd(0x1f) = CONST 
    0x2df0x6ef: v6ef2df = AND v6ef2dd(0x1f), v6ef2a9
    0x2e10x6ef: v6ef2e1 = ISZERO v6ef2df
    0x2e20x6ef: v6ef2e2(0x2ff) = CONST 
    0x2e50x6ef: JUMPI v6ef2e2(0x2ff), v6ef2e1

    Begin block 0x2ff0x6ef
    prev=[0x2d20x6ef, 0x2e60x6ef], succ=[]
    =================================
    0x2ff0x6ef_0x1: v2ff6ef_1 = PHI v6ef2fc, v6ef2db
    0x3050x6ef: v6ef305(0x40) = CONST 
    0x3070x6ef: v6ef307 = MLOAD v6ef305(0x40)
    0x30a0x6ef: v6ef30a = SUB v2ff6ef_1, v6ef307
    0x30c0x6ef: RETURN v6ef307, v6ef30a

    Begin block 0x2e60x6ef
    prev=[0x2d20x6ef], succ=[0x2ff0x6ef]
    =================================
    0x2e80x6ef: v6ef2e8 = SUB v6ef2db, v6ef2df
    0x2ea0x6ef: v6ef2ea = MLOAD v6ef2e8
    0x2eb0x6ef: v6ef2eb(0x1) = CONST 
    0x2ee0x6ef: v6ef2ee(0x20) = CONST 
    0x2f00x6ef: v6ef2f0 = SUB v6ef2ee(0x20), v6ef2df
    0x2f10x6ef: v6ef2f1(0x100) = CONST 
    0x2f40x6ef: v6ef2f4 = EXP v6ef2f1(0x100), v6ef2f0
    0x2f50x6ef: v6ef2f5 = SUB v6ef2f4, v6ef2eb(0x1)
    0x2f60x6ef: v6ef2f6 = NOT v6ef2f5
    0x2f70x6ef: v6ef2f7 = AND v6ef2f6, v6ef2ea
    0x2f90x6ef: MSTORE v6ef2e8, v6ef2f7
    0x2fa0x6ef: v6ef2fa(0x20) = CONST 
    0x2fc0x6ef: v6ef2fc = ADD v6ef2fa(0x20), v6ef2e8

    Begin block 0x2c30x6ef
    prev=[0x2ba0x6ef], succ=[0x2ba0x6ef]
    =================================
    0x2c30x6ef_0x0: v2c36ef_0 = PHI v6ef2cd, v6ef2b8(0x0)
    0x2c50x6ef: v6ef2c5 = ADD v2c36ef_0, v6ef2b3
    0x2c60x6ef: v6ef2c6 = MLOAD v6ef2c5
    0x2c90x6ef: v6ef2c9 = ADD v2c36ef_0, v6ef2b0
    0x2ca0x6ef: MSTORE v6ef2c9, v6ef2c6
    0x2cb0x6ef: v6ef2cb(0x20) = CONST 
    0x2cd0x6ef: v6ef2cd = ADD v6ef2cb(0x20), v2c36ef_0
    0x2ce0x6ef: v6ef2ce(0x2ba) = CONST 
    0x2d10x6ef: JUMP v6ef2ce(0x2ba)

}

function mintBatch(address,uint256,uint256[])() public {
    Begin block 0x6f7
    prev=[], succ=[0x709, 0x70d]
    =================================
    0x6f8: v6f8(0x679) = CONST 
    0x6fb: v6fb(0x4) = CONST 
    0x6fe: v6fe = CALLDATASIZE 
    0x6ff: v6ff = SUB v6fe, v6fb(0x4)
    0x700: v700(0x60) = CONST 
    0x703: v703 = LT v6ff, v700(0x60)
    0x704: v704 = ISZERO v703
    0x705: v705(0x70d) = CONST 
    0x708: JUMPI v705(0x70d), v704

    Begin block 0x709
    prev=[0x6f7], succ=[]
    =================================
    0x709: v709(0x0) = CONST 
    0x70c: REVERT v709(0x0), v709(0x0)

    Begin block 0x70d
    prev=[0x6f7], succ=[0x738, 0x73c]
    =================================
    0x70e: v70e(0x1) = CONST 
    0x710: v710(0x1) = CONST 
    0x712: v712(0xa0) = CONST 
    0x714: v714(0x10000000000000000000000000000000000000000) = SHL v712(0xa0), v710(0x1)
    0x715: v715(0xffffffffffffffffffffffffffffffffffffffff) = SUB v714(0x10000000000000000000000000000000000000000), v70e(0x1)
    0x717: v717 = CALLDATALOAD v6fb(0x4)
    0x718: v718 = AND v717, v715(0xffffffffffffffffffffffffffffffffffffffff)
    0x71a: v71a(0x20) = CONST 
    0x71d: v71d(0x24) = ADD v6fb(0x4), v71a(0x20)
    0x71e: v71e = CALLDATALOAD v71d(0x24)
    0x721: v721 = ADD v6fb(0x4), v6ff
    0x723: v723(0x60) = CONST 
    0x726: v726(0x64) = ADD v6fb(0x4), v723(0x60)
    0x727: v727(0x40) = CONST 
    0x72a: v72a(0x44) = ADD v6fb(0x4), v727(0x40)
    0x72b: v72b = CALLDATALOAD v72a(0x44)
    0x72c: v72c(0x1) = CONST 
    0x72e: v72e(0x20) = CONST 
    0x730: v730(0x100000000) = SHL v72e(0x20), v72c(0x1)
    0x732: v732 = GT v72b, v730(0x100000000)
    0x733: v733 = ISZERO v732
    0x734: v734(0x73c) = CONST 
    0x737: JUMPI v734(0x73c), v733

    Begin block 0x738
    prev=[0x70d], succ=[]
    =================================
    0x738: v738(0x0) = CONST 
    0x73b: REVERT v738(0x0), v738(0x0)

    Begin block 0x73c
    prev=[0x70d], succ=[0x74a, 0x74e]
    =================================
    0x73e: v73e = ADD v6fb(0x4), v72b
    0x740: v740(0x20) = CONST 
    0x743: v743 = ADD v73e, v740(0x20)
    0x744: v744 = GT v743, v721
    0x745: v745 = ISZERO v744
    0x746: v746(0x74e) = CONST 
    0x749: JUMPI v746(0x74e), v745

    Begin block 0x74a
    prev=[0x73c], succ=[]
    =================================
    0x74a: v74a(0x0) = CONST 
    0x74d: REVERT v74a(0x0), v74a(0x0)

    Begin block 0x74e
    prev=[0x73c], succ=[0x76b, 0x76f]
    =================================
    0x750: v750 = CALLDATALOAD v73e
    0x752: v752(0x20) = CONST 
    0x754: v754 = ADD v752(0x20), v73e
    0x757: v757(0x20) = CONST 
    0x75a: v75a = MUL v750, v757(0x20)
    0x75c: v75c = ADD v754, v75a
    0x75d: v75d = GT v75c, v721
    0x75e: v75e(0x1) = CONST 
    0x760: v760(0x20) = CONST 
    0x762: v762(0x100000000) = SHL v760(0x20), v75e(0x1)
    0x764: v764 = GT v750, v762(0x100000000)
    0x765: v765 = OR v764, v75d
    0x766: v766 = ISZERO v765
    0x767: v767(0x76f) = CONST 
    0x76a: JUMPI v767(0x76f), v766

    Begin block 0x76b
    prev=[0x74e], succ=[]
    =================================
    0x76b: v76b(0x0) = CONST 
    0x76e: REVERT v76b(0x0), v76b(0x0)

    Begin block 0x76f
    prev=[0x74e], succ=[0x136a]
    =================================
    0x776: v776(0x136a) = CONST 
    0x779: JUMP v776(0x136a)

    Begin block 0x136a
    prev=[0x76f], succ=[0x1385, 0x13c2]
    =================================
    0x136b: v136b = CALLER 
    0x136c: v136c(0x0) = CONST 
    0x1370: MSTORE v136c(0x0), v136b
    0x1371: v1371(0x5) = CONST 
    0x1373: v1373(0x20) = CONST 
    0x1375: MSTORE v1373(0x20), v1371(0x5)
    0x1376: v1376(0x40) = CONST 
    0x1379: v1379 = SHA3 v136c(0x0), v1376(0x40)
    0x137a: v137a = SLOAD v1379
    0x137b: v137b(0x60) = CONST 
    0x137e: v137e(0xff) = CONST 
    0x1380: v1380 = AND v137e(0xff), v137a
    0x1381: v1381(0x13c2) = CONST 
    0x1384: JUMPI v1381(0x13c2), v1380

    Begin block 0x1385
    prev=[0x136a], succ=[]
    =================================
    0x1385: v1385(0x40) = CONST 
    0x1388: v1388 = MLOAD v1385(0x40)
    0x1389: v1389(0x461bcd) = CONST 
    0x138d: v138d(0xe5) = CONST 
    0x138f: v138f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v138d(0xe5), v1389(0x461bcd)
    0x1391: MSTORE v1388, v138f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1392: v1392(0x20) = CONST 
    0x1394: v1394(0x4) = CONST 
    0x1397: v1397 = ADD v1388, v1394(0x4)
    0x1398: MSTORE v1397, v1392(0x20)
    0x1399: v1399(0xe) = CONST 
    0x139b: v139b(0x24) = CONST 
    0x139e: v139e = ADD v1388, v139b(0x24)
    0x139f: MSTORE v139e, v1399(0xe)
    0x13a0: v13a0(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x13af: v13af(0x91) = CONST 
    0x13b1: v13b1(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v13af(0x91), v13a0(0x36bab9ba1031329036b4b73a32b9)
    0x13b2: v13b2(0x44) = CONST 
    0x13b5: v13b5 = ADD v1388, v13b2(0x44)
    0x13b6: MSTORE v13b5, v13b1(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x13b8: v13b8 = MLOAD v1385(0x40)
    0x13bc: v13bc(0x0) = SUB v1388, v13b8
    0x13bd: v13bd(0x64) = CONST 
    0x13bf: v13bf(0x64) = ADD v13bd(0x64), v13bc(0x0)
    0x13c1: REVERT v13b8, v13bf(0x64)

    Begin block 0x13c2
    prev=[0x136a], succ=[0x13d1, 0x141d]
    =================================
    0x13c3: v13c3(0x1) = CONST 
    0x13c5: v13c5(0x1) = CONST 
    0x13c7: v13c7(0xa0) = CONST 
    0x13c9: v13c9(0x10000000000000000000000000000000000000000) = SHL v13c7(0xa0), v13c5(0x1)
    0x13ca: v13ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13c9(0x10000000000000000000000000000000000000000), v13c3(0x1)
    0x13cc: v13cc = AND v718, v13ca(0xffffffffffffffffffffffffffffffffffffffff)
    0x13cd: v13cd(0x141d) = CONST 
    0x13d0: JUMPI v13cd(0x141d), v13cc

    Begin block 0x13d1
    prev=[0x13c2], succ=[]
    =================================
    0x13d1: v13d1(0x40) = CONST 
    0x13d4: v13d4 = MLOAD v13d1(0x40)
    0x13d5: v13d5(0x461bcd) = CONST 
    0x13d9: v13d9(0xe5) = CONST 
    0x13db: v13db(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13d9(0xe5), v13d5(0x461bcd)
    0x13dd: MSTORE v13d4, v13db(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13de: v13de(0x20) = CONST 
    0x13e0: v13e0(0x4) = CONST 
    0x13e3: v13e3 = ADD v13d4, v13e0(0x4)
    0x13e4: MSTORE v13e3, v13de(0x20)
    0x13e5: v13e5(0x1d) = CONST 
    0x13e7: v13e7(0x24) = CONST 
    0x13ea: v13ea = ADD v13d4, v13e7(0x24)
    0x13eb: MSTORE v13ea, v13e5(0x1d)
    0x13ec: v13ec(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000) = CONST 
    0x140d: v140d(0x44) = CONST 
    0x1410: v1410 = ADD v13d4, v140d(0x44)
    0x1411: MSTORE v1410, v13ec(0x4d757374206e6f74206d696e7420746f206e756c6c2061646472657373000000)
    0x1413: v1413 = MLOAD v13d1(0x40)
    0x1417: v1417(0x0) = SUB v13d4, v1413
    0x1418: v1418(0x64) = CONST 
    0x141a: v141a(0x64) = ADD v1418(0x64), v1417(0x0)
    0x141c: REVERT v1413, v141a(0x64)

    Begin block 0x141d
    prev=[0x13c2], succ=[0x1425, 0x145b]
    =================================
    0x1420: v1420 = EQ v71e, v750
    0x1421: v1421(0x145b) = CONST 
    0x1424: JUMPI v1421(0x145b), v1420

    Begin block 0x1425
    prev=[0x141d], succ=[]
    =================================
    0x1425: v1425(0x40) = CONST 
    0x1427: v1427 = MLOAD v1425(0x40)
    0x1428: v1428(0x461bcd) = CONST 
    0x142c: v142c(0xe5) = CONST 
    0x142e: v142e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v142c(0xe5), v1428(0x461bcd)
    0x1430: MSTORE v1427, v142e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1431: v1431(0x4) = CONST 
    0x1433: v1433 = ADD v1431(0x4), v1427
    0x1436: v1436(0x20) = CONST 
    0x1438: v1438 = ADD v1436(0x20), v1433
    0x143b: v143b(0x20) = SUB v1438, v1433
    0x143d: MSTORE v1433, v143b(0x20)
    0x143e: v143e(0x2a) = CONST 
    0x1441: MSTORE v1438, v143e(0x2a)
    0x1442: v1442(0x20) = CONST 
    0x1444: v1444 = ADD v1442(0x20), v1438
    0x1446: v1446(0x2839) = CONST 
    0x1449: v1449(0x2a) = CONST 
    0x144c: CODECOPY v1444, v1446(0x2839), v1449(0x2a)
    0x144d: v144d(0x40) = CONST 
    0x144f: v144f = ADD v144d(0x40), v1444
    0x1453: v1453(0x40) = CONST 
    0x1455: v1455 = MLOAD v1453(0x40)
    0x1458: v1458(0x84) = SUB v144f, v1455
    0x145a: REVERT v1455, v1458(0x84)

    Begin block 0x145b
    prev=[0x141d], succ=[0x1ff9B0x145b]
    =================================
    0x145c: v145c(0x1467) = CONST 
    0x1463: v1463(0x1ff9) = CONST 
    0x1466: JUMP v1463(0x1ff9)

    Begin block 0x1ff9B0x145b
    prev=[0x145b], succ=[0x2010B0x145b, 0x2014B0x145b]
    =================================
    0x1ffaS0x145b: v1ffaV145b(0x60) = CONST 
    0x1ffcS0x145b: v1ffcV145b(0x0) = CONST 
    0x1fffS0x145b: v1fffV145b(0xffffffffffffffff) = CONST 
    0x2009S0x145b: v2009V145b = GT v71e, v1fffV145b(0xffffffffffffffff)
    0x200bS0x145b: v200bV145b = ISZERO v2009V145b
    0x200cS0x145b: v200cV145b(0x2014) = CONST 
    0x200fS0x145b: JUMPI v200cV145b(0x2014), v200bV145b

    Begin block 0x2010B0x145b
    prev=[0x1ff9B0x145b], succ=[]
    =================================
    0x2010S0x145b: v2010V145b(0x0) = CONST 
    0x2013S0x145b: REVERT v2010V145b(0x0), v2010V145b(0x0)

    Begin block 0x2014B0x145b
    prev=[0x1ff9B0x145b], succ=[0x203eB0x145b, 0x202fB0x145b]
    =================================
    0x2016S0x145b: v2016V145b(0x40) = CONST 
    0x2018S0x145b: v2018V145b = MLOAD v2016V145b(0x40)
    0x201cS0x145b: MSTORE v2018V145b, v71e
    0x201eS0x145b: v201eV145b(0x20) = CONST 
    0x2020S0x145b: v2020V145b = MUL v201eV145b(0x20), v71e
    0x2021S0x145b: v2021V145b(0x20) = CONST 
    0x2023S0x145b: v2023V145b = ADD v2021V145b(0x20), v2020V145b
    0x2025S0x145b: v2025V145b = ADD v2018V145b, v2023V145b
    0x2026S0x145b: v2026V145b(0x40) = CONST 
    0x2028S0x145b: MSTORE v2026V145b(0x40), v2025V145b
    0x202aS0x145b: v202aV145b = ISZERO v71e
    0x202bS0x145b: v202bV145b(0x203e) = CONST 
    0x202eS0x145b: JUMPI v202bV145b(0x203e), v202aV145b

    Begin block 0x203eB0x145b
    prev=[0x2014B0x145b, 0x202fB0x145b], succ=[0x2056B0x145b, 0x205aB0x145b]
    =================================
    0x2042S0x145b: v2042V145b(0x0) = CONST 
    0x2045S0x145b: v2045V145b(0xffffffffffffffff) = CONST 
    0x204fS0x145b: v204fV145b = GT v71e, v2045V145b(0xffffffffffffffff)
    0x2051S0x145b: v2051V145b = ISZERO v204fV145b
    0x2052S0x145b: v2052V145b(0x205a) = CONST 
    0x2055S0x145b: JUMPI v2052V145b(0x205a), v2051V145b

    Begin block 0x2056B0x145b
    prev=[0x203eB0x145b], succ=[]
    =================================
    0x2056S0x145b: v2056V145b(0x0) = CONST 
    0x2059S0x145b: REVERT v2056V145b(0x0), v2056V145b(0x0)

    Begin block 0x205aB0x145b
    prev=[0x203eB0x145b], succ=[0x2084B0x145b, 0x2075B0x145b]
    =================================
    0x205cS0x145b: v205cV145b(0x40) = CONST 
    0x205eS0x145b: v205eV145b = MLOAD v205cV145b(0x40)
    0x2062S0x145b: MSTORE v205eV145b, v71e
    0x2064S0x145b: v2064V145b(0x20) = CONST 
    0x2066S0x145b: v2066V145b = MUL v2064V145b(0x20), v71e
    0x2067S0x145b: v2067V145b(0x20) = CONST 
    0x2069S0x145b: v2069V145b = ADD v2067V145b(0x20), v2066V145b
    0x206bS0x145b: v206bV145b = ADD v205eV145b, v2069V145b
    0x206cS0x145b: v206cV145b(0x40) = CONST 
    0x206eS0x145b: MSTORE v206cV145b(0x40), v206bV145b
    0x2070S0x145b: v2070V145b = ISZERO v71e
    0x2071S0x145b: v2071V145b(0x2084) = CONST 
    0x2074S0x145b: JUMPI v2071V145b(0x2084), v2070V145b

    Begin block 0x2084B0x145b
    prev=[0x205aB0x145b, 0x2075B0x145b], succ=[0x208aB0x145b]
    =================================
    0x2088S0x145b: v2088V145b(0x0) = CONST 

    Begin block 0x208aB0x145b
    prev=[0x2084B0x145b, 0x20edB0x145b], succ=[0x2094B0x145b, 0x2100B0x145b]
    =================================
    0x208a_0x0S0x145b: v208a_0V145b = PHI v2088V145b(0x0), v20fbV145b
    0x208cS0x145b: v208cV145b = MLOAD v2018V145b
    0x208eS0x145b: v208eV145b = LT v208a_0V145b, v208cV145b
    0x208fS0x145b: v208fV145b = ISZERO v208eV145b
    0x2090S0x145b: v2090V145b(0x2100) = CONST 
    0x2093S0x145b: JUMPI v2090V145b(0x2100), v208fV145b

    Begin block 0x2094B0x145b
    prev=[0x208aB0x145b], succ=[0x20d3B0x145b, 0x20d2B0x145b]
    =================================
    0x2094S0x145b: v2094V145b(0x6) = CONST 
    0x2094_0x0S0x145b: v2094_0V145b = PHI v2088V145b(0x0), v20fbV145b
    0x2097S0x145b: v2097V145b = SLOAD v2094V145b(0x6)
    0x2098S0x145b: v2098V145b(0x1) = CONST 
    0x209aS0x145b: v209aV145b = ADD v2098V145b(0x1), v2097V145b
    0x209dS0x145b: SSTORE v2094V145b(0x6), v209aV145b
    0x209eS0x145b: v209eV145b(0x0) = CONST 
    0x20a2S0x145b: MSTORE v209eV145b(0x0), v209aV145b
    0x20a3S0x145b: v20a3V145b(0x7) = CONST 
    0x20a5S0x145b: v20a5V145b(0x20) = CONST 
    0x20a7S0x145b: MSTORE v20a5V145b(0x20), v20a3V145b(0x7)
    0x20a8S0x145b: v20a8V145b(0x40) = CONST 
    0x20abS0x145b: v20abV145b = SHA3 v209eV145b(0x0), v20a8V145b(0x40)
    0x20adS0x145b: v20adV145b = SLOAD v20abV145b
    0x20aeS0x145b: v20aeV145b(0x1) = CONST 
    0x20b0S0x145b: v20b0V145b(0x1) = CONST 
    0x20b2S0x145b: v20b2V145b(0xa0) = CONST 
    0x20b4S0x145b: v20b4V145b(0x10000000000000000000000000000000000000000) = SHL v20b2V145b(0xa0), v20b0V145b(0x1)
    0x20b5S0x145b: v20b5V145b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20b4V145b(0x10000000000000000000000000000000000000000), v20aeV145b(0x1)
    0x20b6S0x145b: v20b6V145b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v20b5V145b(0xffffffffffffffffffffffffffffffffffffffff)
    0x20b7S0x145b: v20b7V145b = AND v20b6V145b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v20adV145b
    0x20b8S0x145b: v20b8V145b(0x1) = CONST 
    0x20baS0x145b: v20baV145b(0x1) = CONST 
    0x20bcS0x145b: v20bcV145b(0xa0) = CONST 
    0x20beS0x145b: v20beV145b(0x10000000000000000000000000000000000000000) = SHL v20bcV145b(0xa0), v20baV145b(0x1)
    0x20bfS0x145b: v20bfV145b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20beV145b(0x10000000000000000000000000000000000000000), v20b8V145b(0x1)
    0x20c1S0x145b: v20c1V145b = AND v718, v20bfV145b(0xffffffffffffffffffffffffffffffffffffffff)
    0x20c2S0x145b: v20c2V145b = OR v20c1V145b, v20b7V145b
    0x20c4S0x145b: SSTORE v20abV145b, v20c2V145b
    0x20c5S0x145b: v20c5V145b = SLOAD v2094V145b(0x6)
    0x20c7S0x145b: v20c7V145b = MLOAD v2018V145b
    0x20cdS0x145b: v20cdV145b = LT v2094_0V145b, v20c7V145b
    0x20ceS0x145b: v20ceV145b(0x20d3) = CONST 
    0x20d1S0x145b: JUMPI v20ceV145b(0x20d3), v20cdV145b

    Begin block 0x20d3B0x145b
    prev=[0x2094B0x145b], succ=[0x20edB0x145b, 0x20ecB0x145b]
    =================================
    0x20d3_0x0S0x145b: v20d3_0V145b = PHI v2088V145b(0x0), v20fbV145b
    0x20d3_0x3S0x145b: v20d3_3V145b = PHI v2088V145b(0x0), v20fbV145b
    0x20d4S0x145b: v20d4V145b(0x20) = CONST 
    0x20d6S0x145b: v20d6V145b = MUL v20d4V145b(0x20), v20d3_0V145b
    0x20d7S0x145b: v20d7V145b(0x20) = CONST 
    0x20d9S0x145b: v20d9V145b = ADD v20d7V145b(0x20), v20d6V145b
    0x20daS0x145b: v20daV145b = ADD v20d9V145b, v2018V145b
    0x20ddS0x145b: MSTORE v20daV145b, v20c5V145b
    0x20e0S0x145b: v20e0V145b(0x1) = CONST 
    0x20e5S0x145b: v20e5V145b = MLOAD v205eV145b
    0x20e7S0x145b: v20e7V145b = LT v20d3_3V145b, v20e5V145b
    0x20e8S0x145b: v20e8V145b(0x20ed) = CONST 
    0x20ebS0x145b: JUMPI v20e8V145b(0x20ed), v20e7V145b

    Begin block 0x20edB0x145b
    prev=[0x20d3B0x145b], succ=[0x208aB0x145b]
    =================================
    0x20ed_0x0S0x145b: v20ed_0V145b = PHI v2088V145b(0x0), v20fbV145b
    0x20ed_0x3S0x145b: v20ed_3V145b = PHI v2088V145b(0x0), v20fbV145b
    0x20eeS0x145b: v20eeV145b(0x20) = CONST 
    0x20f2S0x145b: v20f2V145b = MUL v20eeV145b(0x20), v20ed_0V145b
    0x20f6S0x145b: v20f6V145b = ADD v20f2V145b, v205eV145b
    0x20f7S0x145b: v20f7V145b = ADD v20f6V145b, v20eeV145b(0x20)
    0x20f8S0x145b: MSTORE v20f7V145b, v20e0V145b(0x1)
    0x20f9S0x145b: v20f9V145b(0x1) = CONST 
    0x20fbS0x145b: v20fbV145b = ADD v20f9V145b(0x1), v20ed_3V145b
    0x20fcS0x145b: v20fcV145b(0x208a) = CONST 
    0x20ffS0x145b: JUMP v20fcV145b(0x208a)

    Begin block 0x20ecB0x145b
    prev=[0x20d3B0x145b], succ=[]
    =================================
    0x20ecS0x145b: THROW 

    Begin block 0x20d2B0x145b
    prev=[0x2094B0x145b], succ=[]
    =================================
    0x20d2S0x145b: THROW 

    Begin block 0x2100B0x145b
    prev=[0x208aB0x145b], succ=[0x216fB0x145b]
    =================================
    0x2103S0x145b: v2103V145b(0x1) = CONST 
    0x2105S0x145b: v2105V145b(0x1) = CONST 
    0x2107S0x145b: v2107V145b(0xa0) = CONST 
    0x2109S0x145b: v2109V145b(0x10000000000000000000000000000000000000000) = SHL v2107V145b(0xa0), v2105V145b(0x1)
    0x210aS0x145b: v210aV145b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2109V145b(0x10000000000000000000000000000000000000000), v2103V145b(0x1)
    0x210bS0x145b: v210bV145b = AND v210aV145b(0xffffffffffffffffffffffffffffffffffffffff), v718
    0x210cS0x145b: v210cV145b(0x0) = CONST 
    0x210eS0x145b: v210eV145b(0x1) = CONST 
    0x2110S0x145b: v2110V145b(0x1) = CONST 
    0x2112S0x145b: v2112V145b(0xa0) = CONST 
    0x2114S0x145b: v2114V145b(0x10000000000000000000000000000000000000000) = SHL v2112V145b(0xa0), v2110V145b(0x1)
    0x2115S0x145b: v2115V145b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2114V145b(0x10000000000000000000000000000000000000000), v210eV145b(0x1)
    0x2116S0x145b: v2116V145b(0x0) = AND v2115V145b(0xffffffffffffffffffffffffffffffffffffffff), v210cV145b(0x0)
    0x2117S0x145b: v2117V145b = CALLER 
    0x2118S0x145b: v2118V145b(0x1) = CONST 
    0x211aS0x145b: v211aV145b(0x1) = CONST 
    0x211cS0x145b: v211cV145b(0xa0) = CONST 
    0x211eS0x145b: v211eV145b(0x10000000000000000000000000000000000000000) = SHL v211cV145b(0xa0), v211aV145b(0x1)
    0x211fS0x145b: v211fV145b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v211eV145b(0x10000000000000000000000000000000000000000), v2118V145b(0x1)
    0x2120S0x145b: v2120V145b = AND v211fV145b(0xffffffffffffffffffffffffffffffffffffffff), v2117V145b
    0x2121S0x145b: v2121V145b(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x2144S0x145b: v2144V145b(0x40) = CONST 
    0x2146S0x145b: v2146V145b = MLOAD v2144V145b(0x40)
    0x2149S0x145b: v2149V145b(0x20) = CONST 
    0x214bS0x145b: v214bV145b = ADD v2149V145b(0x20), v2146V145b
    0x214dS0x145b: v214dV145b(0x20) = CONST 
    0x214fS0x145b: v214fV145b = ADD v214dV145b(0x20), v214bV145b
    0x2152S0x145b: v2152V145b(0x40) = SUB v214fV145b, v2146V145b
    0x2154S0x145b: MSTORE v2146V145b, v2152V145b(0x40)
    0x2158S0x145b: v2158V145b = MLOAD v2018V145b
    0x215aS0x145b: MSTORE v214fV145b, v2158V145b
    0x215bS0x145b: v215bV145b(0x20) = CONST 
    0x215dS0x145b: v215dV145b = ADD v215bV145b(0x20), v214fV145b
    0x2161S0x145b: v2161V145b = MLOAD v2018V145b
    0x2163S0x145b: v2163V145b(0x20) = CONST 
    0x2165S0x145b: v2165V145b = ADD v2163V145b(0x20), v2018V145b
    0x2167S0x145b: v2167V145b(0x20) = CONST 
    0x2169S0x145b: v2169V145b = MUL v2167V145b(0x20), v2161V145b
    0x216dS0x145b: v216dV145b(0x0) = CONST 

    Begin block 0x216fB0x145b
    prev=[0x2100B0x145b, 0x2178B0x145b], succ=[0x2187B0x145b, 0x2178B0x145b]
    =================================
    0x216f_0x0S0x145b: v216f_0V145b = PHI v216dV145b(0x0), v2182V145b
    0x2172S0x145b: v2172V145b = LT v216f_0V145b, v2169V145b
    0x2173S0x145b: v2173V145b = ISZERO v2172V145b
    0x2174S0x145b: v2174V145b(0x2187) = CONST 
    0x2177S0x145b: JUMPI v2174V145b(0x2187), v2173V145b

    Begin block 0x2187B0x145b
    prev=[0x216fB0x145b], succ=[0x21aeB0x145b]
    =================================
    0x218eS0x145b: v218eV145b = ADD v2169V145b, v215dV145b
    0x2191S0x145b: v2191V145b = SUB v218eV145b, v2146V145b
    0x2193S0x145b: MSTORE v214bV145b, v2191V145b
    0x2197S0x145b: v2197V145b = MLOAD v205eV145b
    0x2199S0x145b: MSTORE v218eV145b, v2197V145b
    0x219aS0x145b: v219aV145b(0x20) = CONST 
    0x219cS0x145b: v219cV145b = ADD v219aV145b(0x20), v218eV145b
    0x21a0S0x145b: v21a0V145b = MLOAD v205eV145b
    0x21a2S0x145b: v21a2V145b(0x20) = CONST 
    0x21a4S0x145b: v21a4V145b = ADD v21a2V145b(0x20), v205eV145b
    0x21a6S0x145b: v21a6V145b(0x20) = CONST 
    0x21a8S0x145b: v21a8V145b = MUL v21a6V145b(0x20), v21a0V145b
    0x21acS0x145b: v21acV145b(0x0) = CONST 

    Begin block 0x21aeB0x145b
    prev=[0x2187B0x145b, 0x21b7B0x145b], succ=[0x21c6B0x145b, 0x21b7B0x145b]
    =================================
    0x21ae_0x0S0x145b: v21ae_0V145b = PHI v21acV145b(0x0), v21c1V145b
    0x21b1S0x145b: v21b1V145b = LT v21ae_0V145b, v21a8V145b
    0x21b2S0x145b: v21b2V145b = ISZERO v21b1V145b
    0x21b3S0x145b: v21b3V145b(0x21c6) = CONST 
    0x21b6S0x145b: JUMPI v21b3V145b(0x21c6), v21b2V145b

    Begin block 0x21c6B0x145b
    prev=[0x21aeB0x145b], succ=[0x21f9B0x145b]
    =================================
    0x21cdS0x145b: v21cdV145b = ADD v21a8V145b, v219cV145b
    0x21d4S0x145b: v21d4V145b(0x40) = CONST 
    0x21d6S0x145b: v21d6V145b = MLOAD v21d4V145b(0x40)
    0x21d9S0x145b: v21d9V145b = SUB v21cdV145b, v21d6V145b
    0x21dbS0x145b: LOG4 v21d6V145b, v21d9V145b, v2121V145b(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v2120V145b, v2116V145b(0x0), v210bV145b
    0x21dcS0x145b: v21dcV145b(0x21f9) = CONST 
    0x21dfS0x145b: v21dfV145b = CALLER 
    0x21e0S0x145b: v21e0V145b(0x0) = CONST 
    0x21e5S0x145b: v21e5V145b(0x40) = CONST 
    0x21e7S0x145b: v21e7V145b = MLOAD v21e5V145b(0x40)
    0x21e9S0x145b: v21e9V145b(0x20) = CONST 
    0x21ebS0x145b: v21ebV145b = ADD v21e9V145b(0x20), v21e7V145b
    0x21ecS0x145b: v21ecV145b(0x40) = CONST 
    0x21eeS0x145b: MSTORE v21ecV145b(0x40), v21ebV145b
    0x21f0S0x145b: v21f0V145b(0x0) = CONST 
    0x21f3S0x145b: MSTORE v21e7V145b, v21f0V145b(0x0)
    0x21f5S0x145b: v21f5V145b(0x1c36) = CONST 
    0x21f8S0x145b: CALLPRIVATE v21f5V145b(0x1c36), v21e7V145b, v205eV145b, v2018V145b, v718, v21e0V145b(0x0), v21dfV145b, v21dcV145b(0x21f9)

    Begin block 0x21f9B0x145b
    prev=[0x21c6B0x145b], succ=[0x1467]
    =================================
    0x2202S0x145b: JUMP v145c(0x1467)

    Begin block 0x1467
    prev=[0x21f9B0x145b], succ=[0x6790x6f7]
    =================================
    0x146f: JUMP v6f8(0x679)

    Begin block 0x6790x6f7
    prev=[0x1467], succ=[0x69d0x6f7]
    =================================
    0x67a0x6f7: v6f767a(0x40) = CONST 
    0x67d0x6f7: v6f767d = MLOAD v6f767a(0x40)
    0x67e0x6f7: v6f767e(0x20) = CONST 
    0x6820x6f7: MSTORE v6f767d, v6f767e(0x20)
    0x6840x6f7: v6f7684 = MLOAD v2018V145b
    0x6870x6f7: v6f7687 = ADD v6f767d, v6f767e(0x20)
    0x6880x6f7: MSTORE v6f7687, v6f7684
    0x68a0x6f7: v6f768a = MLOAD v2018V145b
    0x6910x6f7: v6f7691 = ADD v6f767d, v6f767a(0x40)
    0x6950x6f7: v6f7695 = ADD v6f767e(0x20), v2018V145b
    0x6970x6f7: v6f7697 = MUL v6f768a, v6f767e(0x20)
    0x69b0x6f7: v6f769b(0x0) = CONST 

    Begin block 0x69d0x6f7
    prev=[0x6a60x6f7, 0x6790x6f7], succ=[0x6a60x6f7, 0x6b50x6f7]
    =================================
    0x69d0x6f7_0x0: v69d6f7_0 = PHI v6f76b0, v6f769b(0x0)
    0x6a00x6f7: v6f76a0 = LT v69d6f7_0, v6f7697
    0x6a10x6f7: v6f76a1 = ISZERO v6f76a0
    0x6a20x6f7: v6f76a2(0x6b5) = CONST 
    0x6a50x6f7: JUMPI v6f76a2(0x6b5), v6f76a1

    Begin block 0x6a60x6f7
    prev=[0x69d0x6f7], succ=[0x69d0x6f7]
    =================================
    0x6a60x6f7_0x0: v6a66f7_0 = PHI v6f76b0, v6f769b(0x0)
    0x6a80x6f7: v6f76a8 = ADD v6a66f7_0, v6f7695
    0x6a90x6f7: v6f76a9 = MLOAD v6f76a8
    0x6ac0x6f7: v6f76ac = ADD v6a66f7_0, v6f7691
    0x6ad0x6f7: MSTORE v6f76ac, v6f76a9
    0x6ae0x6f7: v6f76ae(0x20) = CONST 
    0x6b00x6f7: v6f76b0 = ADD v6f76ae(0x20), v6a66f7_0
    0x6b10x6f7: v6f76b1(0x69d) = CONST 
    0x6b40x6f7: JUMP v6f76b1(0x69d)

    Begin block 0x6b50x6f7
    prev=[0x69d0x6f7], succ=[]
    =================================
    0x6bc0x6f7: v6f76bc = ADD v6f7697, v6f7691
    0x6c10x6f7: v6f76c1(0x40) = CONST 
    0x6c30x6f7: v6f76c3 = MLOAD v6f76c1(0x40)
    0x6c60x6f7: v6f76c6 = SUB v6f76bc, v6f76c3
    0x6c80x6f7: RETURN v6f76c3, v6f76c6

    Begin block 0x21b7B0x145b
    prev=[0x21aeB0x145b], succ=[0x21aeB0x145b]
    =================================
    0x21b7_0x0S0x145b: v21b7_0V145b = PHI v21acV145b(0x0), v21c1V145b
    0x21b9S0x145b: v21b9V145b = ADD v21b7_0V145b, v21a4V145b
    0x21baS0x145b: v21baV145b = MLOAD v21b9V145b
    0x21bdS0x145b: v21bdV145b = ADD v21b7_0V145b, v219cV145b
    0x21beS0x145b: MSTORE v21bdV145b, v21baV145b
    0x21bfS0x145b: v21bfV145b(0x20) = CONST 
    0x21c1S0x145b: v21c1V145b = ADD v21bfV145b(0x20), v21b7_0V145b
    0x21c2S0x145b: v21c2V145b(0x21ae) = CONST 
    0x21c5S0x145b: JUMP v21c2V145b(0x21ae)

    Begin block 0x2178B0x145b
    prev=[0x216fB0x145b], succ=[0x216fB0x145b]
    =================================
    0x2178_0x0S0x145b: v2178_0V145b = PHI v216dV145b(0x0), v2182V145b
    0x217aS0x145b: v217aV145b = ADD v2178_0V145b, v2165V145b
    0x217bS0x145b: v217bV145b = MLOAD v217aV145b
    0x217eS0x145b: v217eV145b = ADD v2178_0V145b, v215dV145b
    0x217fS0x145b: MSTORE v217eV145b, v217bV145b
    0x2180S0x145b: v2180V145b(0x20) = CONST 
    0x2182S0x145b: v2182V145b = ADD v2180V145b(0x20), v2178_0V145b
    0x2183S0x145b: v2183V145b(0x216f) = CONST 
    0x2186S0x145b: JUMP v2183V145b(0x216f)

    Begin block 0x2075B0x145b
    prev=[0x205aB0x145b], succ=[0x2084B0x145b]
    =================================
    0x2076S0x145b: v2076V145b(0x20) = CONST 
    0x2078S0x145b: v2078V145b = ADD v2076V145b(0x20), v205eV145b
    0x2079S0x145b: v2079V145b(0x20) = CONST 
    0x207cS0x145b: v207cV145b = MUL v71e, v2079V145b(0x20)
    0x207eS0x145b: v207eV145b = CALLDATASIZE 
    0x2080S0x145b: CALLDATACOPY v2078V145b, v207eV145b, v207cV145b
    0x2081S0x145b: v2081V145b = ADD v207cV145b, v2078V145b

    Begin block 0x202fB0x145b
    prev=[0x2014B0x145b], succ=[0x203eB0x145b]
    =================================
    0x2030S0x145b: v2030V145b(0x20) = CONST 
    0x2032S0x145b: v2032V145b = ADD v2030V145b(0x20), v2018V145b
    0x2033S0x145b: v2033V145b(0x20) = CONST 
    0x2036S0x145b: v2036V145b = MUL v71e, v2033V145b(0x20)
    0x2038S0x145b: v2038V145b = CALLDATASIZE 
    0x203aS0x145b: CALLDATACOPY v2032V145b, v2038V145b, v2036V145b
    0x203bS0x145b: v203bV145b = ADD v2036V145b, v2032V145b

}

function owner()() public {
    Begin block 0x77a
    prev=[], succ=[0x1470]
    =================================
    0x77b: v77b(0x2ab4) = CONST 
    0x77e: v77e(0x1470) = CONST 
    0x781: JUMP v77e(0x1470)

    Begin block 0x1470
    prev=[0x77a], succ=[0x2ab4]
    =================================
    0x1471: v1471(0x3) = CONST 
    0x1473: v1473 = SLOAD v1471(0x3)
    0x1474: v1474(0x1) = CONST 
    0x1476: v1476(0x1) = CONST 
    0x1478: v1478(0xa0) = CONST 
    0x147a: v147a(0x10000000000000000000000000000000000000000) = SHL v1478(0xa0), v1476(0x1)
    0x147b: v147b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v147a(0x10000000000000000000000000000000000000000), v1474(0x1)
    0x147c: v147c = AND v147b(0xffffffffffffffffffffffffffffffffffffffff), v1473
    0x147e: JUMP v77b(0x2ab4)

    Begin block 0x2ab4
    prev=[0x1470], succ=[]
    =================================
    0x2ab5: v2ab5(0x40) = CONST 
    0x2ab8: v2ab8 = MLOAD v2ab5(0x40)
    0x2ab9: v2ab9(0x1) = CONST 
    0x2abb: v2abb(0x1) = CONST 
    0x2abd: v2abd(0xa0) = CONST 
    0x2abf: v2abf(0x10000000000000000000000000000000000000000) = SHL v2abd(0xa0), v2abb(0x1)
    0x2ac0: v2ac0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2abf(0x10000000000000000000000000000000000000000), v2ab9(0x1)
    0x2ac3: v2ac3 = AND v147c, v2ac0(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ac5: MSTORE v2ab8, v2ac3
    0x2ac6: v2ac6 = MLOAD v2ab5(0x40)
    0x2aca: v2aca(0x0) = SUB v2ab8, v2ac6
    0x2acb: v2acb(0x20) = CONST 
    0x2acd: v2acd(0x20) = ADD v2acb(0x20), v2aca(0x0)
    0x2acf: RETURN v2ac6, v2acd(0x20)

}

function galaxyCommunity()() public {
    Begin block 0x79e
    prev=[], succ=[0x147f]
    =================================
    0x79f: v79f(0x2aef) = CONST 
    0x7a2: v7a2(0x147f) = CONST 
    0x7a5: JUMP v7a2(0x147f)

    Begin block 0x147f
    prev=[0x79e], succ=[0x2aef]
    =================================
    0x1480: v1480(0x4) = CONST 
    0x1482: v1482 = SLOAD v1480(0x4)
    0x1483: v1483(0x1) = CONST 
    0x1485: v1485(0x1) = CONST 
    0x1487: v1487(0xa0) = CONST 
    0x1489: v1489(0x10000000000000000000000000000000000000000) = SHL v1487(0xa0), v1485(0x1)
    0x148a: v148a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1489(0x10000000000000000000000000000000000000000), v1483(0x1)
    0x148b: v148b = AND v148a(0xffffffffffffffffffffffffffffffffffffffff), v1482
    0x148d: JUMP v79f(0x2aef)

    Begin block 0x2aef
    prev=[0x147f], succ=[]
    =================================
    0x2af0: v2af0(0x40) = CONST 
    0x2af3: v2af3 = MLOAD v2af0(0x40)
    0x2af4: v2af4(0x1) = CONST 
    0x2af6: v2af6(0x1) = CONST 
    0x2af8: v2af8(0xa0) = CONST 
    0x2afa: v2afa(0x10000000000000000000000000000000000000000) = SHL v2af8(0xa0), v2af6(0x1)
    0x2afb: v2afb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2afa(0x10000000000000000000000000000000000000000), v2af4(0x1)
    0x2afe: v2afe = AND v148b, v2afb(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b00: MSTORE v2af3, v2afe
    0x2b01: v2b01 = MLOAD v2af0(0x40)
    0x2b05: v2b05(0x0) = SUB v2af3, v2b01
    0x2b06: v2b06(0x20) = CONST 
    0x2b08: v2b08(0x20) = ADD v2b06(0x20), v2b05(0x0)
    0x2b0a: RETURN v2b01, v2b08(0x20)

}

function addMinter(address)() public {
    Begin block 0x7a6
    prev=[], succ=[0x7b8, 0x7bc]
    =================================
    0x7a7: v7a7(0x2b2a) = CONST 
    0x7aa: v7aa(0x4) = CONST 
    0x7ad: v7ad = CALLDATASIZE 
    0x7ae: v7ae = SUB v7ad, v7aa(0x4)
    0x7af: v7af(0x20) = CONST 
    0x7b2: v7b2 = LT v7ae, v7af(0x20)
    0x7b3: v7b3 = ISZERO v7b2
    0x7b4: v7b4(0x7bc) = CONST 
    0x7b7: JUMPI v7b4(0x7bc), v7b3

    Begin block 0x7b8
    prev=[0x7a6], succ=[]
    =================================
    0x7b8: v7b8(0x0) = CONST 
    0x7bb: REVERT v7b8(0x0), v7b8(0x0)

    Begin block 0x7bc
    prev=[0x7a6], succ=[0x148e]
    =================================
    0x7be: v7be = CALLDATALOAD v7aa(0x4)
    0x7bf: v7bf(0x1) = CONST 
    0x7c1: v7c1(0x1) = CONST 
    0x7c3: v7c3(0xa0) = CONST 
    0x7c5: v7c5(0x10000000000000000000000000000000000000000) = SHL v7c3(0xa0), v7c1(0x1)
    0x7c6: v7c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c5(0x10000000000000000000000000000000000000000), v7bf(0x1)
    0x7c7: v7c7 = AND v7c6(0xffffffffffffffffffffffffffffffffffffffff), v7be
    0x7c8: v7c8(0x148e) = CONST 
    0x7cb: JUMP v7c8(0x148e)

    Begin block 0x148e
    prev=[0x7bc], succ=[0x14a1, 0x14dd]
    =================================
    0x148f: v148f(0x3) = CONST 
    0x1491: v1491 = SLOAD v148f(0x3)
    0x1492: v1492(0x1) = CONST 
    0x1494: v1494(0x1) = CONST 
    0x1496: v1496(0xa0) = CONST 
    0x1498: v1498(0x10000000000000000000000000000000000000000) = SHL v1496(0xa0), v1494(0x1)
    0x1499: v1499(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1498(0x10000000000000000000000000000000000000000), v1492(0x1)
    0x149a: v149a = AND v1499(0xffffffffffffffffffffffffffffffffffffffff), v1491
    0x149b: v149b = CALLER 
    0x149c: v149c = EQ v149b, v149a
    0x149d: v149d(0x14dd) = CONST 
    0x14a0: JUMPI v149d(0x14dd), v149c

    Begin block 0x14a1
    prev=[0x148e], succ=[]
    =================================
    0x14a1: v14a1(0x40) = CONST 
    0x14a4: v14a4 = MLOAD v14a1(0x40)
    0x14a5: v14a5(0x461bcd) = CONST 
    0x14a9: v14a9(0xe5) = CONST 
    0x14ab: v14ab(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v14a9(0xe5), v14a5(0x461bcd)
    0x14ad: MSTORE v14a4, v14ab(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14ae: v14ae(0x20) = CONST 
    0x14b0: v14b0(0x4) = CONST 
    0x14b3: v14b3 = ADD v14a4, v14b0(0x4)
    0x14b4: MSTORE v14b3, v14ae(0x20)
    0x14b5: v14b5(0xd) = CONST 
    0x14b7: v14b7(0x24) = CONST 
    0x14ba: v14ba = ADD v14a4, v14b7(0x24)
    0x14bb: MSTORE v14ba, v14b5(0xd)
    0x14bc: v14bc(0x26bab9ba1031329037bbb732b9) = CONST 
    0x14ca: v14ca(0x99) = CONST 
    0x14cc: v14cc(0x4d757374206265206f776e657200000000000000000000000000000000000000) = SHL v14ca(0x99), v14bc(0x26bab9ba1031329037bbb732b9)
    0x14cd: v14cd(0x44) = CONST 
    0x14d0: v14d0 = ADD v14a4, v14cd(0x44)
    0x14d1: MSTORE v14d0, v14cc(0x4d757374206265206f776e657200000000000000000000000000000000000000)
    0x14d3: v14d3 = MLOAD v14a1(0x40)
    0x14d7: v14d7(0x0) = SUB v14a4, v14d3
    0x14d8: v14d8(0x64) = CONST 
    0x14da: v14da(0x64) = ADD v14d8(0x64), v14d7(0x0)
    0x14dc: REVERT v14d3, v14da(0x64)

    Begin block 0x14dd
    prev=[0x148e], succ=[0x14ec, 0x1538]
    =================================
    0x14de: v14de(0x1) = CONST 
    0x14e0: v14e0(0x1) = CONST 
    0x14e2: v14e2(0xa0) = CONST 
    0x14e4: v14e4(0x10000000000000000000000000000000000000000) = SHL v14e2(0xa0), v14e0(0x1)
    0x14e5: v14e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14e4(0x10000000000000000000000000000000000000000), v14de(0x1)
    0x14e7: v14e7 = AND v7c7, v14e5(0xffffffffffffffffffffffffffffffffffffffff)
    0x14e8: v14e8(0x1538) = CONST 
    0x14eb: JUMPI v14e8(0x1538), v14e7

    Begin block 0x14ec
    prev=[0x14dd], succ=[]
    =================================
    0x14ec: v14ec(0x40) = CONST 
    0x14ef: v14ef = MLOAD v14ec(0x40)
    0x14f0: v14f0(0x461bcd) = CONST 
    0x14f4: v14f4(0xe5) = CONST 
    0x14f6: v14f6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v14f4(0xe5), v14f0(0x461bcd)
    0x14f8: MSTORE v14ef, v14f6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14f9: v14f9(0x20) = CONST 
    0x14fb: v14fb(0x4) = CONST 
    0x14fe: v14fe = ADD v14ef, v14fb(0x4)
    0x14ff: MSTORE v14fe, v14f9(0x20)
    0x1500: v1500(0x1f) = CONST 
    0x1502: v1502(0x24) = CONST 
    0x1505: v1505 = ADD v14ef, v1502(0x24)
    0x1506: MSTORE v1505, v1500(0x1f)
    0x1507: v1507(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300) = CONST 
    0x1528: v1528(0x44) = CONST 
    0x152b: v152b = ADD v14ef, v1528(0x44)
    0x152c: MSTORE v152b, v1507(0x4d696e746572206d757374206e6f74206265206e756c6c206164647265737300)
    0x152e: v152e = MLOAD v14ec(0x40)
    0x1532: v1532(0x0) = SUB v14ef, v152e
    0x1533: v1533(0x64) = CONST 
    0x1535: v1535(0x64) = ADD v1533(0x64), v1532(0x0)
    0x1537: REVERT v152e, v1535(0x64)

    Begin block 0x1538
    prev=[0x14dd], succ=[0x155a, 0x159d]
    =================================
    0x1539: v1539(0x1) = CONST 
    0x153b: v153b(0x1) = CONST 
    0x153d: v153d(0xa0) = CONST 
    0x153f: v153f(0x10000000000000000000000000000000000000000) = SHL v153d(0xa0), v153b(0x1)
    0x1540: v1540(0xffffffffffffffffffffffffffffffffffffffff) = SUB v153f(0x10000000000000000000000000000000000000000), v1539(0x1)
    0x1542: v1542 = AND v7c7, v1540(0xffffffffffffffffffffffffffffffffffffffff)
    0x1543: v1543(0x0) = CONST 
    0x1547: MSTORE v1543(0x0), v1542
    0x1548: v1548(0x5) = CONST 
    0x154a: v154a(0x20) = CONST 
    0x154c: MSTORE v154a(0x20), v1548(0x5)
    0x154d: v154d(0x40) = CONST 
    0x1550: v1550 = SHA3 v1543(0x0), v154d(0x40)
    0x1551: v1551 = SLOAD v1550
    0x1552: v1552(0xff) = CONST 
    0x1554: v1554 = AND v1552(0xff), v1551
    0x1555: v1555 = ISZERO v1554
    0x1556: v1556(0x159d) = CONST 
    0x1559: JUMPI v1556(0x159d), v1555

    Begin block 0x155a
    prev=[0x1538], succ=[]
    =================================
    0x155a: v155a(0x40) = CONST 
    0x155d: v155d = MLOAD v155a(0x40)
    0x155e: v155e(0x461bcd) = CONST 
    0x1562: v1562(0xe5) = CONST 
    0x1564: v1564(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1562(0xe5), v155e(0x461bcd)
    0x1566: MSTORE v155d, v1564(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1567: v1567(0x20) = CONST 
    0x1569: v1569(0x4) = CONST 
    0x156c: v156c = ADD v155d, v1569(0x4)
    0x156d: MSTORE v156c, v1567(0x20)
    0x156e: v156e(0x14) = CONST 
    0x1570: v1570(0x24) = CONST 
    0x1573: v1573 = ADD v155d, v1570(0x24)
    0x1574: MSTORE v1573, v156e(0x14)
    0x1575: v1575(0x135a5b9d195c88185b1c9958591e481859191959) = CONST 
    0x158a: v158a(0x62) = CONST 
    0x158c: v158c(0x4d696e74657220616c7265616479206164646564000000000000000000000000) = SHL v158a(0x62), v1575(0x135a5b9d195c88185b1c9958591e481859191959)
    0x158d: v158d(0x44) = CONST 
    0x1590: v1590 = ADD v155d, v158d(0x44)
    0x1591: MSTORE v1590, v158c(0x4d696e74657220616c7265616479206164646564000000000000000000000000)
    0x1593: v1593 = MLOAD v155a(0x40)
    0x1597: v1597(0x0) = SUB v155d, v1593
    0x1598: v1598(0x64) = CONST 
    0x159a: v159a(0x64) = ADD v1598(0x64), v1597(0x0)
    0x159c: REVERT v1593, v159a(0x64)

    Begin block 0x159d
    prev=[0x1538], succ=[0x2b2a]
    =================================
    0x159e: v159e(0x1) = CONST 
    0x15a0: v15a0(0x1) = CONST 
    0x15a2: v15a2(0xa0) = CONST 
    0x15a4: v15a4(0x10000000000000000000000000000000000000000) = SHL v15a2(0xa0), v15a0(0x1)
    0x15a5: v15a5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15a4(0x10000000000000000000000000000000000000000), v159e(0x1)
    0x15a6: v15a6 = AND v15a5(0xffffffffffffffffffffffffffffffffffffffff), v7c7
    0x15a7: v15a7(0x0) = CONST 
    0x15ab: MSTORE v15a7(0x0), v15a6
    0x15ac: v15ac(0x5) = CONST 
    0x15ae: v15ae(0x20) = CONST 
    0x15b0: MSTORE v15ae(0x20), v15ac(0x5)
    0x15b1: v15b1(0x40) = CONST 
    0x15b4: v15b4 = SHA3 v15a7(0x0), v15b1(0x40)
    0x15b6: v15b6 = SLOAD v15b4
    0x15b7: v15b7(0xff) = CONST 
    0x15b9: v15b9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v15b7(0xff)
    0x15ba: v15ba = AND v15b9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v15b6
    0x15bb: v15bb(0x1) = CONST 
    0x15bd: v15bd = OR v15bb(0x1), v15ba
    0x15bf: SSTORE v15b4, v15bd
    0x15c0: JUMP v7a7(0x2b2a)

    Begin block 0x2b2a
    prev=[0x159d], succ=[]
    =================================
    0x2b2b: STOP 

}

function burn(address,uint256)() public {
    Begin block 0x7cc
    prev=[], succ=[0x7de, 0x7e2]
    =================================
    0x7cd: v7cd(0x2b4b) = CONST 
    0x7d0: v7d0(0x4) = CONST 
    0x7d3: v7d3 = CALLDATASIZE 
    0x7d4: v7d4 = SUB v7d3, v7d0(0x4)
    0x7d5: v7d5(0x40) = CONST 
    0x7d8: v7d8 = LT v7d4, v7d5(0x40)
    0x7d9: v7d9 = ISZERO v7d8
    0x7da: v7da(0x7e2) = CONST 
    0x7dd: JUMPI v7da(0x7e2), v7d9

    Begin block 0x7de
    prev=[0x7cc], succ=[]
    =================================
    0x7de: v7de(0x0) = CONST 
    0x7e1: REVERT v7de(0x0), v7de(0x0)

    Begin block 0x7e2
    prev=[0x7cc], succ=[0x15c1]
    =================================
    0x7e4: v7e4(0x1) = CONST 
    0x7e6: v7e6(0x1) = CONST 
    0x7e8: v7e8(0xa0) = CONST 
    0x7ea: v7ea(0x10000000000000000000000000000000000000000) = SHL v7e8(0xa0), v7e6(0x1)
    0x7eb: v7eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7ea(0x10000000000000000000000000000000000000000), v7e4(0x1)
    0x7ed: v7ed = CALLDATALOAD v7d0(0x4)
    0x7ee: v7ee = AND v7ed, v7eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x7f0: v7f0(0x20) = CONST 
    0x7f2: v7f2(0x24) = ADD v7f0(0x20), v7d0(0x4)
    0x7f3: v7f3 = CALLDATALOAD v7f2(0x24)
    0x7f4: v7f4(0x15c1) = CONST 
    0x7f7: JUMP v7f4(0x15c1)

    Begin block 0x15c1
    prev=[0x7e2], succ=[0x15d9, 0x1616]
    =================================
    0x15c2: v15c2 = CALLER 
    0x15c3: v15c3(0x0) = CONST 
    0x15c7: MSTORE v15c3(0x0), v15c2
    0x15c8: v15c8(0x5) = CONST 
    0x15ca: v15ca(0x20) = CONST 
    0x15cc: MSTORE v15ca(0x20), v15c8(0x5)
    0x15cd: v15cd(0x40) = CONST 
    0x15d0: v15d0 = SHA3 v15c3(0x0), v15cd(0x40)
    0x15d1: v15d1 = SLOAD v15d0
    0x15d2: v15d2(0xff) = CONST 
    0x15d4: v15d4 = AND v15d2(0xff), v15d1
    0x15d5: v15d5(0x1616) = CONST 
    0x15d8: JUMPI v15d5(0x1616), v15d4

    Begin block 0x15d9
    prev=[0x15c1], succ=[]
    =================================
    0x15d9: v15d9(0x40) = CONST 
    0x15dc: v15dc = MLOAD v15d9(0x40)
    0x15dd: v15dd(0x461bcd) = CONST 
    0x15e1: v15e1(0xe5) = CONST 
    0x15e3: v15e3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15e1(0xe5), v15dd(0x461bcd)
    0x15e5: MSTORE v15dc, v15e3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15e6: v15e6(0x20) = CONST 
    0x15e8: v15e8(0x4) = CONST 
    0x15eb: v15eb = ADD v15dc, v15e8(0x4)
    0x15ec: MSTORE v15eb, v15e6(0x20)
    0x15ed: v15ed(0xe) = CONST 
    0x15ef: v15ef(0x24) = CONST 
    0x15f2: v15f2 = ADD v15dc, v15ef(0x24)
    0x15f3: MSTORE v15f2, v15ed(0xe)
    0x15f4: v15f4(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x1603: v1603(0x91) = CONST 
    0x1605: v1605(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v1603(0x91), v15f4(0x36bab9ba1031329036b4b73a32b9)
    0x1606: v1606(0x44) = CONST 
    0x1609: v1609 = ADD v15dc, v1606(0x44)
    0x160a: MSTORE v1609, v1605(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x160c: v160c = MLOAD v15d9(0x40)
    0x1610: v1610(0x0) = SUB v15dc, v160c
    0x1611: v1611(0x64) = CONST 
    0x1613: v1613(0x64) = ADD v1611(0x64), v1610(0x0)
    0x1615: REVERT v160c, v1613(0x64)

    Begin block 0x1616
    prev=[0x15c1], succ=[0x1620]
    =================================
    0x1617: v1617(0x1620) = CONST 
    0x161c: v161c(0x192e) = CONST 
    0x161f: v161f_0 = CALLPRIVATE v161c(0x192e), v7f3, v7ee, v1617(0x1620)

    Begin block 0x1620
    prev=[0x1616], succ=[0x1625, 0x1661]
    =================================
    0x1621: v1621(0x1661) = CONST 
    0x1624: JUMPI v1621(0x1661), v161f_0

    Begin block 0x1625
    prev=[0x1620], succ=[]
    =================================
    0x1625: v1625(0x40) = CONST 
    0x1628: v1628 = MLOAD v1625(0x40)
    0x1629: v1629(0x461bcd) = CONST 
    0x162d: v162d(0xe5) = CONST 
    0x162f: v162f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v162d(0xe5), v1629(0x461bcd)
    0x1631: MSTORE v1628, v162f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1632: v1632(0x20) = CONST 
    0x1634: v1634(0x4) = CONST 
    0x1637: v1637 = ADD v1628, v1634(0x4)
    0x1638: MSTORE v1637, v1632(0x20)
    0x1639: v1639(0xd) = CONST 
    0x163b: v163b(0x24) = CONST 
    0x163e: v163e = ADD v1628, v163b(0x24)
    0x163f: MSTORE v163e, v1639(0xd)
    0x1640: v1640(0x2737ba103a34329037bbb732b9) = CONST 
    0x164e: v164e(0x99) = CONST 
    0x1650: v1650(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v164e(0x99), v1640(0x2737ba103a34329037bbb732b9)
    0x1651: v1651(0x44) = CONST 
    0x1654: v1654 = ADD v1628, v1651(0x44)
    0x1655: MSTORE v1654, v1650(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1657: v1657 = MLOAD v1625(0x40)
    0x165b: v165b(0x0) = SUB v1628, v1657
    0x165c: v165c(0x64) = CONST 
    0x165e: v165e(0x64) = ADD v165c(0x64), v165b(0x0)
    0x1660: REVERT v1657, v165e(0x64)

    Begin block 0x1661
    prev=[0x1620], succ=[0x2203]
    =================================
    0x1662: v1662(0x2db3) = CONST 
    0x1667: v1667(0x2203) = CONST 
    0x166a: JUMP v1667(0x2203)

    Begin block 0x2203
    prev=[0x1661], succ=[0x2db3]
    =================================
    0x2204: v2204(0x0) = CONST 
    0x2208: MSTORE v2204(0x0), v7f3
    0x2209: v2209(0x7) = CONST 
    0x220b: v220b(0x20) = CONST 
    0x220f: MSTORE v220b(0x20), v2209(0x7)
    0x2210: v2210(0x40) = CONST 
    0x2214: v2214 = SHA3 v2204(0x0), v2210(0x40)
    0x2216: v2216 = SLOAD v2214
    0x2217: v2217(0x1) = CONST 
    0x2219: v2219(0x1) = CONST 
    0x221b: v221b(0xa0) = CONST 
    0x221d: v221d(0x10000000000000000000000000000000000000000) = SHL v221b(0xa0), v2219(0x1)
    0x221e: v221e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v221d(0x10000000000000000000000000000000000000000), v2217(0x1)
    0x221f: v221f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v221e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2220: v2220 = AND v221f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2216
    0x2222: SSTORE v2214, v2220
    0x2224: v2224 = MLOAD v2210(0x40)
    0x2227: MSTORE v2224, v7f3
    0x2228: v2228(0x1) = CONST 
    0x222c: v222c = ADD v2224, v220b(0x20)
    0x2230: MSTORE v222c, v2228(0x1)
    0x2232: v2232 = MLOAD v2210(0x40)
    0x2233: v2233(0x1) = CONST 
    0x2235: v2235(0x1) = CONST 
    0x2237: v2237(0xa0) = CONST 
    0x2239: v2239(0x10000000000000000000000000000000000000000) = SHL v2237(0xa0), v2235(0x1)
    0x223a: v223a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2239(0x10000000000000000000000000000000000000000), v2233(0x1)
    0x223c: v223c = AND v7ee, v223a(0xffffffffffffffffffffffffffffffffffffffff)
    0x223e: v223e = CALLER 
    0x2240: v2240(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x2265: v2265(0x0) = SUB v2224, v2232
    0x2266: v2266(0x40) = ADD v2265(0x0), v2210(0x40)
    0x2268: LOG4 v2232, v2266(0x40), v2240(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v223e, v223c, v2204(0x0)
    0x226b: JUMP v1662(0x2db3)

    Begin block 0x2db3
    prev=[0x2203], succ=[0x2b4b]
    =================================
    0x2db6: JUMP v7cd(0x2b4b)

    Begin block 0x2b4b
    prev=[0x2db3], succ=[]
    =================================
    0x2b4c: STOP 

}

function setApprovalForAll(address,bool)() public {
    Begin block 0x7f8
    prev=[], succ=[0x80a, 0x80e]
    =================================
    0x7f9: v7f9(0x2b6c) = CONST 
    0x7fc: v7fc(0x4) = CONST 
    0x7ff: v7ff = CALLDATASIZE 
    0x800: v800 = SUB v7ff, v7fc(0x4)
    0x801: v801(0x40) = CONST 
    0x804: v804 = LT v800, v801(0x40)
    0x805: v805 = ISZERO v804
    0x806: v806(0x80e) = CONST 
    0x809: JUMPI v806(0x80e), v805

    Begin block 0x80a
    prev=[0x7f8], succ=[]
    =================================
    0x80a: v80a(0x0) = CONST 
    0x80d: REVERT v80a(0x0), v80a(0x0)

    Begin block 0x80e
    prev=[0x7f8], succ=[0x166b]
    =================================
    0x810: v810(0x1) = CONST 
    0x812: v812(0x1) = CONST 
    0x814: v814(0xa0) = CONST 
    0x816: v816(0x10000000000000000000000000000000000000000) = SHL v814(0xa0), v812(0x1)
    0x817: v817(0xffffffffffffffffffffffffffffffffffffffff) = SUB v816(0x10000000000000000000000000000000000000000), v810(0x1)
    0x819: v819 = CALLDATALOAD v7fc(0x4)
    0x81a: v81a = AND v819, v817(0xffffffffffffffffffffffffffffffffffffffff)
    0x81c: v81c(0x20) = CONST 
    0x81e: v81e(0x24) = ADD v81c(0x20), v7fc(0x4)
    0x81f: v81f = CALLDATALOAD v81e(0x24)
    0x820: v820 = ISZERO v81f
    0x821: v821 = ISZERO v820
    0x822: v822(0x166b) = CONST 
    0x825: JUMP v822(0x166b)

    Begin block 0x166b
    prev=[0x80e], succ=[0x167d, 0x16c9]
    =================================
    0x166c: v166c = CALLER 
    0x166d: v166d(0x1) = CONST 
    0x166f: v166f(0x1) = CONST 
    0x1671: v1671(0xa0) = CONST 
    0x1673: v1673(0x10000000000000000000000000000000000000000) = SHL v1671(0xa0), v166f(0x1)
    0x1674: v1674(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1673(0x10000000000000000000000000000000000000000), v166d(0x1)
    0x1676: v1676 = AND v81a, v1674(0xffffffffffffffffffffffffffffffffffffffff)
    0x1677: v1677 = EQ v1676, v166c
    0x1678: v1678 = ISZERO v1677
    0x1679: v1679(0x16c9) = CONST 
    0x167c: JUMPI v1679(0x16c9), v1678

    Begin block 0x167d
    prev=[0x166b], succ=[]
    =================================
    0x167d: v167d(0x40) = CONST 
    0x1680: v1680 = MLOAD v167d(0x40)
    0x1681: v1681(0x461bcd) = CONST 
    0x1685: v1685(0xe5) = CONST 
    0x1687: v1687(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1685(0xe5), v1681(0x461bcd)
    0x1689: MSTORE v1680, v1687(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x168a: v168a(0x20) = CONST 
    0x168c: v168c(0x4) = CONST 
    0x168f: v168f = ADD v1680, v168c(0x4)
    0x1692: MSTORE v168f, v168a(0x20)
    0x1693: v1693(0x24) = CONST 
    0x1696: v1696 = ADD v1680, v1693(0x24)
    0x1697: MSTORE v1696, v168a(0x20)
    0x1698: v1698(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66) = CONST 
    0x16b9: v16b9(0x44) = CONST 
    0x16bc: v16bc = ADD v1680, v16b9(0x44)
    0x16bd: MSTORE v16bc, v1698(0x53657474696e6720617070726f76616c2073746174757320666f722073656c66)
    0x16bf: v16bf = MLOAD v167d(0x40)
    0x16c3: v16c3(0x0) = SUB v1680, v16bf
    0x16c4: v16c4(0x64) = CONST 
    0x16c6: v16c6(0x64) = ADD v16c4(0x64), v16c3(0x0)
    0x16c8: REVERT v16bf, v16c6(0x64)

    Begin block 0x16c9
    prev=[0x166b], succ=[0x2b6c]
    =================================
    0x16ca: v16ca = CALLER 
    0x16cb: v16cb(0x0) = CONST 
    0x16cf: MSTORE v16cb(0x0), v16ca
    0x16d0: v16d0(0x8) = CONST 
    0x16d2: v16d2(0x20) = CONST 
    0x16d6: MSTORE v16d2(0x20), v16d0(0x8)
    0x16d7: v16d7(0x40) = CONST 
    0x16db: v16db = SHA3 v16cb(0x0), v16d7(0x40)
    0x16dc: v16dc(0x1) = CONST 
    0x16de: v16de(0x1) = CONST 
    0x16e0: v16e0(0xa0) = CONST 
    0x16e2: v16e2(0x10000000000000000000000000000000000000000) = SHL v16e0(0xa0), v16de(0x1)
    0x16e3: v16e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16e2(0x10000000000000000000000000000000000000000), v16dc(0x1)
    0x16e5: v16e5 = AND v81a, v16e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x16e8: MSTORE v16cb(0x0), v16e5
    0x16eb: MSTORE v16d2(0x20), v16db
    0x16ef: v16ef = SHA3 v16cb(0x0), v16d7(0x40)
    0x16f1: v16f1 = SLOAD v16ef
    0x16f2: v16f2(0xff) = CONST 
    0x16f4: v16f4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v16f2(0xff)
    0x16f5: v16f5 = AND v16f4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v16f1
    0x16f7: v16f7 = ISZERO v821
    0x16f8: v16f8 = ISZERO v16f7
    0x16fb: v16fb = OR v16f8, v16f5
    0x16fe: SSTORE v16ef, v16fb
    0x1700: v1700 = MLOAD v16d7(0x40)
    0x1703: MSTORE v1700, v16f8
    0x1705: v1705 = MLOAD v16d7(0x40)
    0x1709: v1709(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31) = CONST 
    0x172e: v172e(0x0) = SUB v1700, v1705
    0x1731: v1731(0x20) = ADD v16d2(0x20), v172e(0x0)
    0x1733: LOG3 v1705, v1731(0x20), v1709(0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31), v16ca, v16e5
    0x1736: JUMP v7f9(0x2b6c)

    Begin block 0x2b6c
    prev=[0x16c9], succ=[]
    =================================
    0x2b6d: STOP 

}

function transferGalaxyCommunity(address)() public {
    Begin block 0x826
    prev=[], succ=[0x838, 0x83c]
    =================================
    0x827: v827(0x2b8d) = CONST 
    0x82a: v82a(0x4) = CONST 
    0x82d: v82d = CALLDATASIZE 
    0x82e: v82e = SUB v82d, v82a(0x4)
    0x82f: v82f(0x20) = CONST 
    0x832: v832 = LT v82e, v82f(0x20)
    0x833: v833 = ISZERO v832
    0x834: v834(0x83c) = CONST 
    0x837: JUMPI v834(0x83c), v833

    Begin block 0x838
    prev=[0x826], succ=[]
    =================================
    0x838: v838(0x0) = CONST 
    0x83b: REVERT v838(0x0), v838(0x0)

    Begin block 0x83c
    prev=[0x826], succ=[0x1737]
    =================================
    0x83e: v83e = CALLDATALOAD v82a(0x4)
    0x83f: v83f(0x1) = CONST 
    0x841: v841(0x1) = CONST 
    0x843: v843(0xa0) = CONST 
    0x845: v845(0x10000000000000000000000000000000000000000) = SHL v843(0xa0), v841(0x1)
    0x846: v846(0xffffffffffffffffffffffffffffffffffffffff) = SUB v845(0x10000000000000000000000000000000000000000), v83f(0x1)
    0x847: v847 = AND v846(0xffffffffffffffffffffffffffffffffffffffff), v83e
    0x848: v848(0x1737) = CONST 
    0x84b: JUMP v848(0x1737)

    Begin block 0x1737
    prev=[0x83c], succ=[0x174a, 0x1791]
    =================================
    0x1738: v1738(0x4) = CONST 
    0x173a: v173a = SLOAD v1738(0x4)
    0x173b: v173b(0x1) = CONST 
    0x173d: v173d(0x1) = CONST 
    0x173f: v173f(0xa0) = CONST 
    0x1741: v1741(0x10000000000000000000000000000000000000000) = SHL v173f(0xa0), v173d(0x1)
    0x1742: v1742(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1741(0x10000000000000000000000000000000000000000), v173b(0x1)
    0x1743: v1743 = AND v1742(0xffffffffffffffffffffffffffffffffffffffff), v173a
    0x1744: v1744 = CALLER 
    0x1745: v1745 = EQ v1744, v1743
    0x1746: v1746(0x1791) = CONST 
    0x1749: JUMPI v1746(0x1791), v1745

    Begin block 0x174a
    prev=[0x1737], succ=[]
    =================================
    0x174a: v174a(0x40) = CONST 
    0x174d: v174d = MLOAD v174a(0x40)
    0x174e: v174e(0x461bcd) = CONST 
    0x1752: v1752(0xe5) = CONST 
    0x1754: v1754(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1752(0xe5), v174e(0x461bcd)
    0x1756: MSTORE v174d, v1754(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1757: v1757(0x20) = CONST 
    0x1759: v1759(0x4) = CONST 
    0x175c: v175c = ADD v174d, v1759(0x4)
    0x175d: MSTORE v175c, v1757(0x20)
    0x175e: v175e(0x18) = CONST 
    0x1760: v1760(0x24) = CONST 
    0x1763: v1763 = ADD v174d, v1760(0x24)
    0x1764: MSTORE v1763, v175e(0x18)
    0x1765: v1765(0x6d7573742062652067616c61787920636f6d6d756e697479) = CONST 
    0x177e: v177e(0x40) = CONST 
    0x1780: v1780(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000) = SHL v177e(0x40), v1765(0x6d7573742062652067616c61787920636f6d6d756e697479)
    0x1781: v1781(0x44) = CONST 
    0x1784: v1784 = ADD v174d, v1781(0x44)
    0x1785: MSTORE v1784, v1780(0x6d7573742062652067616c61787920636f6d6d756e6974790000000000000000)
    0x1787: v1787 = MLOAD v174a(0x40)
    0x178b: v178b(0x0) = SUB v174d, v1787
    0x178c: v178c(0x64) = CONST 
    0x178e: v178e(0x64) = ADD v178c(0x64), v178b(0x0)
    0x1790: REVERT v1787, v178e(0x64)

    Begin block 0x1791
    prev=[0x1737], succ=[0x17a0, 0x17d6]
    =================================
    0x1792: v1792(0x1) = CONST 
    0x1794: v1794(0x1) = CONST 
    0x1796: v1796(0xa0) = CONST 
    0x1798: v1798(0x10000000000000000000000000000000000000000) = SHL v1796(0xa0), v1794(0x1)
    0x1799: v1799(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1798(0x10000000000000000000000000000000000000000), v1792(0x1)
    0x179b: v179b = AND v847, v1799(0xffffffffffffffffffffffffffffffffffffffff)
    0x179c: v179c(0x17d6) = CONST 
    0x179f: JUMPI v179c(0x17d6), v179b

    Begin block 0x17a0
    prev=[0x1791], succ=[]
    =================================
    0x17a0: v17a0(0x40) = CONST 
    0x17a2: v17a2 = MLOAD v17a0(0x40)
    0x17a3: v17a3(0x461bcd) = CONST 
    0x17a7: v17a7(0xe5) = CONST 
    0x17a9: v17a9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17a7(0xe5), v17a3(0x461bcd)
    0x17ab: MSTORE v17a2, v17a9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17ac: v17ac(0x4) = CONST 
    0x17ae: v17ae = ADD v17ac(0x4), v17a2
    0x17b1: v17b1(0x20) = CONST 
    0x17b3: v17b3 = ADD v17b1(0x20), v17ae
    0x17b6: v17b6(0x20) = SUB v17b3, v17ae
    0x17b8: MSTORE v17ae, v17b6(0x20)
    0x17b9: v17b9(0x2b) = CONST 
    0x17bc: MSTORE v17b3, v17b9(0x2b)
    0x17bd: v17bd(0x20) = CONST 
    0x17bf: v17bf = ADD v17bd(0x20), v17b3
    0x17c1: v17c1(0x2702) = CONST 
    0x17c4: v17c4(0x2b) = CONST 
    0x17c7: CODECOPY v17bf, v17c1(0x2702), v17c4(0x2b)
    0x17c8: v17c8(0x40) = CONST 
    0x17ca: v17ca = ADD v17c8(0x40), v17bf
    0x17ce: v17ce(0x40) = CONST 
    0x17d0: v17d0 = MLOAD v17ce(0x40)
    0x17d3: v17d3(0x84) = SUB v17ca, v17d0
    0x17d5: REVERT v17d0, v17d3(0x84)

    Begin block 0x17d6
    prev=[0x1791], succ=[0x2b8d]
    =================================
    0x17d7: v17d7(0x4) = CONST 
    0x17da: v17da = SLOAD v17d7(0x4)
    0x17db: v17db(0x1) = CONST 
    0x17dd: v17dd(0x1) = CONST 
    0x17df: v17df(0xa0) = CONST 
    0x17e1: v17e1(0x10000000000000000000000000000000000000000) = SHL v17df(0xa0), v17dd(0x1)
    0x17e2: v17e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17e1(0x10000000000000000000000000000000000000000), v17db(0x1)
    0x17e3: v17e3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v17e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x17e4: v17e4 = AND v17e3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v17da
    0x17e5: v17e5(0x1) = CONST 
    0x17e7: v17e7(0x1) = CONST 
    0x17e9: v17e9(0xa0) = CONST 
    0x17eb: v17eb(0x10000000000000000000000000000000000000000) = SHL v17e9(0xa0), v17e7(0x1)
    0x17ec: v17ec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17eb(0x10000000000000000000000000000000000000000), v17e5(0x1)
    0x17ef: v17ef = AND v17ec(0xffffffffffffffffffffffffffffffffffffffff), v847
    0x17f2: v17f2 = OR v17ef, v17e4
    0x17f6: SSTORE v17d7(0x4), v17f2
    0x17f7: v17f7(0x40) = CONST 
    0x17f9: v17f9 = MLOAD v17f7(0x40)
    0x17fc: v17fc = AND v17f2, v17ec(0xffffffffffffffffffffffffffffffffffffffff)
    0x17fe: v17fe(0x3953a794c970ca1d8613b88541e5759f5a1dc2b77fe412e1edc27a03e5657d11) = CONST 
    0x1820: v1820(0x0) = CONST 
    0x1823: LOG3 v17f9, v1820(0x0), v17fe(0x3953a794c970ca1d8613b88541e5759f5a1dc2b77fe412e1edc27a03e5657d11), v17fc, v17ef
    0x1825: JUMP v827(0x2b8d)

    Begin block 0x2b8d
    prev=[0x17d6], succ=[]
    =================================
    0x2b8e: STOP 

}

function burnBatch(address,uint256[])() public {
    Begin block 0x84c
    prev=[], succ=[0x85e, 0x862]
    =================================
    0x84d: v84d(0x2bae) = CONST 
    0x850: v850(0x4) = CONST 
    0x853: v853 = CALLDATASIZE 
    0x854: v854 = SUB v853, v850(0x4)
    0x855: v855(0x40) = CONST 
    0x858: v858 = LT v854, v855(0x40)
    0x859: v859 = ISZERO v858
    0x85a: v85a(0x862) = CONST 
    0x85d: JUMPI v85a(0x862), v859

    Begin block 0x85e
    prev=[0x84c], succ=[]
    =================================
    0x85e: v85e(0x0) = CONST 
    0x861: REVERT v85e(0x0), v85e(0x0)

    Begin block 0x862
    prev=[0x84c], succ=[0x888, 0x88c]
    =================================
    0x863: v863(0x1) = CONST 
    0x865: v865(0x1) = CONST 
    0x867: v867(0xa0) = CONST 
    0x869: v869(0x10000000000000000000000000000000000000000) = SHL v867(0xa0), v865(0x1)
    0x86a: v86a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v869(0x10000000000000000000000000000000000000000), v863(0x1)
    0x86c: v86c = CALLDATALOAD v850(0x4)
    0x86d: v86d = AND v86c, v86a(0xffffffffffffffffffffffffffffffffffffffff)
    0x871: v871 = ADD v850(0x4), v854
    0x873: v873(0x40) = CONST 
    0x876: v876(0x44) = ADD v850(0x4), v873(0x40)
    0x877: v877(0x20) = CONST 
    0x87a: v87a(0x24) = ADD v850(0x4), v877(0x20)
    0x87b: v87b = CALLDATALOAD v87a(0x24)
    0x87c: v87c(0x1) = CONST 
    0x87e: v87e(0x20) = CONST 
    0x880: v880(0x100000000) = SHL v87e(0x20), v87c(0x1)
    0x882: v882 = GT v87b, v880(0x100000000)
    0x883: v883 = ISZERO v882
    0x884: v884(0x88c) = CONST 
    0x887: JUMPI v884(0x88c), v883

    Begin block 0x888
    prev=[0x862], succ=[]
    =================================
    0x888: v888(0x0) = CONST 
    0x88b: REVERT v888(0x0), v888(0x0)

    Begin block 0x88c
    prev=[0x862], succ=[0x89a, 0x89e]
    =================================
    0x88e: v88e = ADD v850(0x4), v87b
    0x890: v890(0x20) = CONST 
    0x893: v893 = ADD v88e, v890(0x20)
    0x894: v894 = GT v893, v871
    0x895: v895 = ISZERO v894
    0x896: v896(0x89e) = CONST 
    0x899: JUMPI v896(0x89e), v895

    Begin block 0x89a
    prev=[0x88c], succ=[]
    =================================
    0x89a: v89a(0x0) = CONST 
    0x89d: REVERT v89a(0x0), v89a(0x0)

    Begin block 0x89e
    prev=[0x88c], succ=[0x8bb, 0x8bf]
    =================================
    0x8a0: v8a0 = CALLDATALOAD v88e
    0x8a2: v8a2(0x20) = CONST 
    0x8a4: v8a4 = ADD v8a2(0x20), v88e
    0x8a7: v8a7(0x20) = CONST 
    0x8aa: v8aa = MUL v8a0, v8a7(0x20)
    0x8ac: v8ac = ADD v8a4, v8aa
    0x8ad: v8ad = GT v8ac, v871
    0x8ae: v8ae(0x1) = CONST 
    0x8b0: v8b0(0x20) = CONST 
    0x8b2: v8b2(0x100000000) = SHL v8b0(0x20), v8ae(0x1)
    0x8b4: v8b4 = GT v8a0, v8b2(0x100000000)
    0x8b5: v8b5 = OR v8b4, v8ad
    0x8b6: v8b6 = ISZERO v8b5
    0x8b7: v8b7(0x8bf) = CONST 
    0x8ba: JUMPI v8b7(0x8bf), v8b6

    Begin block 0x8bb
    prev=[0x89e], succ=[]
    =================================
    0x8bb: v8bb(0x0) = CONST 
    0x8be: REVERT v8bb(0x0), v8bb(0x0)

    Begin block 0x8bf
    prev=[0x89e], succ=[0x1826]
    =================================
    0x8c6: v8c6(0x1826) = CONST 
    0x8c9: JUMP v8c6(0x1826)

    Begin block 0x1826
    prev=[0x8bf], succ=[0x183e, 0x187b]
    =================================
    0x1827: v1827 = CALLER 
    0x1828: v1828(0x0) = CONST 
    0x182c: MSTORE v1828(0x0), v1827
    0x182d: v182d(0x5) = CONST 
    0x182f: v182f(0x20) = CONST 
    0x1831: MSTORE v182f(0x20), v182d(0x5)
    0x1832: v1832(0x40) = CONST 
    0x1835: v1835 = SHA3 v1828(0x0), v1832(0x40)
    0x1836: v1836 = SLOAD v1835
    0x1837: v1837(0xff) = CONST 
    0x1839: v1839 = AND v1837(0xff), v1836
    0x183a: v183a(0x187b) = CONST 
    0x183d: JUMPI v183a(0x187b), v1839

    Begin block 0x183e
    prev=[0x1826], succ=[]
    =================================
    0x183e: v183e(0x40) = CONST 
    0x1841: v1841 = MLOAD v183e(0x40)
    0x1842: v1842(0x461bcd) = CONST 
    0x1846: v1846(0xe5) = CONST 
    0x1848: v1848(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1846(0xe5), v1842(0x461bcd)
    0x184a: MSTORE v1841, v1848(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x184b: v184b(0x20) = CONST 
    0x184d: v184d(0x4) = CONST 
    0x1850: v1850 = ADD v1841, v184d(0x4)
    0x1851: MSTORE v1850, v184b(0x20)
    0x1852: v1852(0xe) = CONST 
    0x1854: v1854(0x24) = CONST 
    0x1857: v1857 = ADD v1841, v1854(0x24)
    0x1858: MSTORE v1857, v1852(0xe)
    0x1859: v1859(0x36bab9ba1031329036b4b73a32b9) = CONST 
    0x1868: v1868(0x91) = CONST 
    0x186a: v186a(0x6d757374206265206d696e746572000000000000000000000000000000000000) = SHL v1868(0x91), v1859(0x36bab9ba1031329036b4b73a32b9)
    0x186b: v186b(0x44) = CONST 
    0x186e: v186e = ADD v1841, v186b(0x44)
    0x186f: MSTORE v186e, v186a(0x6d757374206265206d696e746572000000000000000000000000000000000000)
    0x1871: v1871 = MLOAD v183e(0x40)
    0x1875: v1875(0x0) = SUB v1841, v1871
    0x1876: v1876(0x64) = CONST 
    0x1878: v1878(0x64) = ADD v1876(0x64), v1875(0x0)
    0x187a: REVERT v1871, v1878(0x64)

    Begin block 0x187b
    prev=[0x1826], succ=[0x187e]
    =================================
    0x187c: v187c(0x0) = CONST 

    Begin block 0x187e
    prev=[0x187b, 0x18e3], succ=[0x1887, 0x18eb]
    =================================
    0x187e_0x0: v187e_0 = PHI v187c(0x0), v18e6
    0x1881: v1881 = LT v187e_0, v8a0
    0x1882: v1882 = ISZERO v1881
    0x1883: v1883(0x18eb) = CONST 
    0x1886: JUMPI v1883(0x18eb), v1882

    Begin block 0x1887
    prev=[0x187e], succ=[0x1895, 0x1896]
    =================================
    0x1887: v1887(0x18a2) = CONST 
    0x1887_0x0: v1887_0 = PHI v187c(0x0), v18e6
    0x1890: v1890 = LT v1887_0, v8a0
    0x1891: v1891(0x1896) = CONST 
    0x1894: JUMPI v1891(0x1896), v1890

    Begin block 0x1895
    prev=[0x1887], succ=[]
    =================================
    0x1895: THROW 

    Begin block 0x1896
    prev=[0x1887], succ=[0x192e0x84c]
    =================================
    0x1896_0x0: v1896_0 = PHI v187c(0x0), v18e6
    0x1899: v1899(0x20) = CONST 
    0x189b: v189b = MUL v1899(0x20), v1896_0
    0x189c: v189c = ADD v189b, v8a4
    0x189d: v189d = CALLDATALOAD v189c
    0x189e: v189e(0x192e) = CONST 
    0x18a1: JUMP v189e(0x192e)

    Begin block 0x192e0x84c
    prev=[0x1896], succ=[0x19460x84c, 0x193f0x84c]
    =================================
    0x192f0x84c: v84c192f(0x0) = CONST 
    0x19310x84c: v84c1931(0x1) = CONST 
    0x19330x84c: v84c1933(0x1) = CONST 
    0x19350x84c: v84c1935(0xa0) = CONST 
    0x19370x84c: v84c1937(0x10000000000000000000000000000000000000000) = SHL v84c1935(0xa0), v84c1933(0x1)
    0x19380x84c: v84c1938(0xffffffffffffffffffffffffffffffffffffffff) = SUB v84c1937(0x10000000000000000000000000000000000000000), v84c1931(0x1)
    0x193a0x84c: v84c193a = AND v86d, v84c1938(0xffffffffffffffffffffffffffffffffffffffff)
    0x193b0x84c: v84c193b(0x1946) = CONST 
    0x193e0x84c: JUMPI v84c193b(0x1946), v84c193a

    Begin block 0x19460x84c
    prev=[0x192e0x84c], succ=[0x2dfb0x84c]
    =================================
    0x19480x84c: v84c1948(0x0) = CONST 
    0x194c0x84c: MSTORE v84c1948(0x0), v189d
    0x194d0x84c: v84c194d(0x7) = CONST 
    0x194f0x84c: v84c194f(0x20) = CONST 
    0x19510x84c: MSTORE v84c194f(0x20), v84c194d(0x7)
    0x19520x84c: v84c1952(0x40) = CONST 
    0x19550x84c: v84c1955 = SHA3 v84c1948(0x0), v84c1952(0x40)
    0x19560x84c: v84c1956 = SLOAD v84c1955
    0x19570x84c: v84c1957(0x1) = CONST 
    0x19590x84c: v84c1959(0x1) = CONST 
    0x195b0x84c: v84c195b(0xa0) = CONST 
    0x195d0x84c: v84c195d(0x10000000000000000000000000000000000000000) = SHL v84c195b(0xa0), v84c1959(0x1)
    0x195e0x84c: v84c195e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v84c195d(0x10000000000000000000000000000000000000000), v84c1957(0x1)
    0x19610x84c: v84c1961 = AND v84c195e(0xffffffffffffffffffffffffffffffffffffffff), v86d
    0x19630x84c: v84c1963 = AND v84c1956, v84c195e(0xffffffffffffffffffffffffffffffffffffffff)
    0x19640x84c: v84c1964 = EQ v84c1963, v84c1961
    0x19650x84c: v84c1965(0x2dfb) = CONST 
    0x19680x84c: JUMP v84c1965(0x2dfb)

    Begin block 0x2dfb0x84c
    prev=[0x19460x84c], succ=[0x18a2]
    =================================
    0x2e000x84c: JUMP v1887(0x18a2)

    Begin block 0x18a2
    prev=[0x2dd60x84c, 0x2dfb0x84c], succ=[0x18a7, 0x18e3]
    =================================
    0x18a2_0x0: v18a2_0 = PHI v84c1964, v84c1940(0x0)
    0x18a3: v18a3(0x18e3) = CONST 
    0x18a6: JUMPI v18a3(0x18e3), v18a2_0

    Begin block 0x18a7
    prev=[0x18a2], succ=[]
    =================================
    0x18a7: v18a7(0x40) = CONST 
    0x18aa: v18aa = MLOAD v18a7(0x40)
    0x18ab: v18ab(0x461bcd) = CONST 
    0x18af: v18af(0xe5) = CONST 
    0x18b1: v18b1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v18af(0xe5), v18ab(0x461bcd)
    0x18b3: MSTORE v18aa, v18b1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x18b4: v18b4(0x20) = CONST 
    0x18b6: v18b6(0x4) = CONST 
    0x18b9: v18b9 = ADD v18aa, v18b6(0x4)
    0x18ba: MSTORE v18b9, v18b4(0x20)
    0x18bb: v18bb(0xd) = CONST 
    0x18bd: v18bd(0x24) = CONST 
    0x18c0: v18c0 = ADD v18aa, v18bd(0x24)
    0x18c1: MSTORE v18c0, v18bb(0xd)
    0x18c2: v18c2(0x2737ba103a34329037bbb732b9) = CONST 
    0x18d0: v18d0(0x99) = CONST 
    0x18d2: v18d2(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v18d0(0x99), v18c2(0x2737ba103a34329037bbb732b9)
    0x18d3: v18d3(0x44) = CONST 
    0x18d6: v18d6 = ADD v18aa, v18d3(0x44)
    0x18d7: MSTORE v18d6, v18d2(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x18d9: v18d9 = MLOAD v18a7(0x40)
    0x18dd: v18dd(0x0) = SUB v18aa, v18d9
    0x18de: v18de(0x64) = CONST 
    0x18e0: v18e0(0x64) = ADD v18de(0x64), v18dd(0x0)
    0x18e2: REVERT v18d9, v18e0(0x64)

    Begin block 0x18e3
    prev=[0x18a2], succ=[0x187e]
    =================================
    0x18e3_0x0: v18e3_0 = PHI v187c(0x0), v18e6
    0x18e4: v18e4(0x1) = CONST 
    0x18e6: v18e6 = ADD v18e4(0x1), v18e3_0
    0x18e7: v18e7(0x187e) = CONST 
    0x18ea: JUMP v18e7(0x187e)

    Begin block 0x193f0x84c
    prev=[0x192e0x84c], succ=[0x2dd60x84c]
    =================================
    0x19400x84c: v84c1940(0x0) = CONST 
    0x19420x84c: v84c1942(0x2dd6) = CONST 
    0x19450x84c: JUMP v84c1942(0x2dd6)

    Begin block 0x2dd60x84c
    prev=[0x193f0x84c], succ=[0x18a2]
    =================================
    0x2ddb0x84c: JUMP v1887(0x18a2)

    Begin block 0x18eb
    prev=[0x187e], succ=[0x226c]
    =================================
    0x18ed: v18ed(0x1929) = CONST 
    0x18f5: v18f5(0x20) = CONST 
    0x18f7: v18f7 = MUL v18f5(0x20), v8a0
    0x18f8: v18f8(0x20) = CONST 
    0x18fa: v18fa = ADD v18f8(0x20), v18f7
    0x18fb: v18fb(0x40) = CONST 
    0x18fd: v18fd = MLOAD v18fb(0x40)
    0x1900: v1900 = ADD v18fd, v18fa
    0x1901: v1901(0x40) = CONST 
    0x1903: MSTORE v1901(0x40), v1900
    0x190b: MSTORE v18fd, v8a0
    0x190c: v190c(0x20) = CONST 
    0x190e: v190e = ADD v190c(0x20), v18fd
    0x1911: v1911(0x20) = CONST 
    0x1913: v1913 = MUL v1911(0x20), v8a0
    0x1917: CALLDATACOPY v190e, v8a4, v1913
    0x1918: v1918(0x0) = CONST 
    0x191b: v191b = ADD v190e, v1913
    0x191f: MSTORE v191b, v1918(0x0)
    0x1921: v1921(0x226c) = CONST 
    0x1928: JUMP v1921(0x226c)

    Begin block 0x226c
    prev=[0x18eb], succ=[0x2282, 0x2286]
    =================================
    0x226d: v226d(0x0) = CONST 
    0x2270: v2270 = MLOAD v18fd
    0x2271: v2271(0xffffffffffffffff) = CONST 
    0x227b: v227b = GT v2270, v2271(0xffffffffffffffff)
    0x227d: v227d = ISZERO v227b
    0x227e: v227e(0x2286) = CONST 
    0x2281: JUMPI v227e(0x2286), v227d

    Begin block 0x2282
    prev=[0x226c], succ=[]
    =================================
    0x2282: v2282(0x0) = CONST 
    0x2285: REVERT v2282(0x0), v2282(0x0)

    Begin block 0x2286
    prev=[0x226c], succ=[0x22b0, 0x22a1]
    =================================
    0x2288: v2288(0x40) = CONST 
    0x228a: v228a = MLOAD v2288(0x40)
    0x228e: MSTORE v228a, v2270
    0x2290: v2290(0x20) = CONST 
    0x2292: v2292 = MUL v2290(0x20), v2270
    0x2293: v2293(0x20) = CONST 
    0x2295: v2295 = ADD v2293(0x20), v2292
    0x2297: v2297 = ADD v228a, v2295
    0x2298: v2298(0x40) = CONST 
    0x229a: MSTORE v2298(0x40), v2297
    0x229c: v229c = ISZERO v2270
    0x229d: v229d(0x22b0) = CONST 
    0x22a0: JUMPI v229d(0x22b0), v229c

    Begin block 0x22b0
    prev=[0x2286, 0x22a1], succ=[0x22b6]
    =================================
    0x22b4: v22b4(0x0) = CONST 

    Begin block 0x22b6
    prev=[0x22b0, 0x2309], succ=[0x22c0, 0x231c]
    =================================
    0x22b6_0x0: v22b6_0 = PHI v22b4(0x0), v2317
    0x22b8: v22b8 = MLOAD v18fd
    0x22ba: v22ba = LT v22b6_0, v22b8
    0x22bb: v22bb = ISZERO v22ba
    0x22bc: v22bc(0x231c) = CONST 
    0x22bf: JUMPI v22bc(0x231c), v22bb

    Begin block 0x22c0
    prev=[0x22b6], succ=[0x22ce, 0x22cf]
    =================================
    0x22c0: v22c0(0x7) = CONST 
    0x22c0_0x0: v22c0_0 = PHI v22b4(0x0), v2317
    0x22c2: v22c2(0x0) = CONST 
    0x22c7: v22c7 = MLOAD v18fd
    0x22c9: v22c9 = LT v22c0_0, v22c7
    0x22ca: v22ca(0x22cf) = CONST 
    0x22cd: JUMPI v22ca(0x22cf), v22c9

    Begin block 0x22ce
    prev=[0x22c0], succ=[]
    =================================
    0x22ce: THROW 

    Begin block 0x22cf
    prev=[0x22c0], succ=[0x2308, 0x2309]
    =================================
    0x22cf_0x0: v22cf_0 = PHI v22b4(0x0), v2317
    0x22cf_0x4: v22cf_4 = PHI v22b4(0x0), v2317
    0x22d0: v22d0(0x20) = CONST 
    0x22d2: v22d2 = MUL v22d0(0x20), v22cf_0
    0x22d3: v22d3(0x20) = CONST 
    0x22d5: v22d5 = ADD v22d3(0x20), v22d2
    0x22d6: v22d6 = ADD v22d5, v18fd
    0x22d7: v22d7 = MLOAD v22d6
    0x22d9: MSTORE v22c2(0x0), v22d7
    0x22da: v22da(0x20) = CONST 
    0x22dc: v22dc(0x20) = ADD v22da(0x20), v22c2(0x0)
    0x22df: MSTORE v22dc(0x20), v22c0(0x7)
    0x22e0: v22e0(0x20) = CONST 
    0x22e2: v22e2(0x40) = ADD v22e0(0x20), v22dc(0x20)
    0x22e3: v22e3(0x0) = CONST 
    0x22e5: v22e5 = SHA3 v22e3(0x0), v22e2(0x40)
    0x22e6: v22e6(0x0) = CONST 
    0x22e8: v22e8(0x100) = CONST 
    0x22eb: v22eb(0x1) = EXP v22e8(0x100), v22e6(0x0)
    0x22ed: v22ed = SLOAD v22e5
    0x22ef: v22ef(0x1) = CONST 
    0x22f1: v22f1(0x1) = CONST 
    0x22f3: v22f3(0xa0) = CONST 
    0x22f5: v22f5(0x10000000000000000000000000000000000000000) = SHL v22f3(0xa0), v22f1(0x1)
    0x22f6: v22f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22f5(0x10000000000000000000000000000000000000000), v22ef(0x1)
    0x22f7: v22f7(0xffffffffffffffffffffffffffffffffffffffff) = MUL v22f6(0xffffffffffffffffffffffffffffffffffffffff), v22eb(0x1)
    0x22f8: v22f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v22f7(0xffffffffffffffffffffffffffffffffffffffff)
    0x22f9: v22f9 = AND v22f8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v22ed
    0x22fb: SSTORE v22e5, v22f9
    0x22fc: v22fc(0x1) = CONST 
    0x2301: v2301 = MLOAD v228a
    0x2303: v2303 = LT v22cf_4, v2301
    0x2304: v2304(0x2309) = CONST 
    0x2307: JUMPI v2304(0x2309), v2303

    Begin block 0x2308
    prev=[0x22cf], succ=[]
    =================================
    0x2308: THROW 

    Begin block 0x2309
    prev=[0x22cf], succ=[0x22b6]
    =================================
    0x2309_0x0: v2309_0 = PHI v22b4(0x0), v2317
    0x2309_0x3: v2309_3 = PHI v22b4(0x0), v2317
    0x230a: v230a(0x20) = CONST 
    0x230e: v230e = MUL v230a(0x20), v2309_0
    0x2312: v2312 = ADD v230e, v228a
    0x2313: v2313 = ADD v2312, v230a(0x20)
    0x2314: MSTORE v2313, v22fc(0x1)
    0x2315: v2315(0x1) = CONST 
    0x2317: v2317 = ADD v2315(0x1), v2309_3
    0x2318: v2318(0x22b6) = CONST 
    0x231b: JUMP v2318(0x22b6)

    Begin block 0x231c
    prev=[0x22b6], succ=[0x238b]
    =================================
    0x231e: v231e(0x0) = CONST 
    0x2320: v2320(0x1) = CONST 
    0x2322: v2322(0x1) = CONST 
    0x2324: v2324(0xa0) = CONST 
    0x2326: v2326(0x10000000000000000000000000000000000000000) = SHL v2324(0xa0), v2322(0x1)
    0x2327: v2327(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2326(0x10000000000000000000000000000000000000000), v2320(0x1)
    0x2328: v2328(0x0) = AND v2327(0xffffffffffffffffffffffffffffffffffffffff), v231e(0x0)
    0x232a: v232a(0x1) = CONST 
    0x232c: v232c(0x1) = CONST 
    0x232e: v232e(0xa0) = CONST 
    0x2330: v2330(0x10000000000000000000000000000000000000000) = SHL v232e(0xa0), v232c(0x1)
    0x2331: v2331(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2330(0x10000000000000000000000000000000000000000), v232a(0x1)
    0x2332: v2332 = AND v2331(0xffffffffffffffffffffffffffffffffffffffff), v86d
    0x2333: v2333 = CALLER 
    0x2334: v2334(0x1) = CONST 
    0x2336: v2336(0x1) = CONST 
    0x2338: v2338(0xa0) = CONST 
    0x233a: v233a(0x10000000000000000000000000000000000000000) = SHL v2338(0xa0), v2336(0x1)
    0x233b: v233b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v233a(0x10000000000000000000000000000000000000000), v2334(0x1)
    0x233c: v233c = AND v233b(0xffffffffffffffffffffffffffffffffffffffff), v2333
    0x233d: v233d(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb) = CONST 
    0x2360: v2360(0x40) = CONST 
    0x2362: v2362 = MLOAD v2360(0x40)
    0x2365: v2365(0x20) = CONST 
    0x2367: v2367 = ADD v2365(0x20), v2362
    0x2369: v2369(0x20) = CONST 
    0x236b: v236b = ADD v2369(0x20), v2367
    0x236e: v236e(0x40) = SUB v236b, v2362
    0x2370: MSTORE v2362, v236e(0x40)
    0x2374: v2374 = MLOAD v18fd
    0x2376: MSTORE v236b, v2374
    0x2377: v2377(0x20) = CONST 
    0x2379: v2379 = ADD v2377(0x20), v236b
    0x237d: v237d = MLOAD v18fd
    0x237f: v237f(0x20) = CONST 
    0x2381: v2381 = ADD v237f(0x20), v18fd
    0x2383: v2383(0x20) = CONST 
    0x2385: v2385 = MUL v2383(0x20), v237d
    0x2389: v2389(0x0) = CONST 

    Begin block 0x238b
    prev=[0x231c, 0x2394], succ=[0x23a3, 0x2394]
    =================================
    0x238b_0x0: v238b_0 = PHI v2389(0x0), v239e
    0x238e: v238e = LT v238b_0, v2385
    0x238f: v238f = ISZERO v238e
    0x2390: v2390(0x23a3) = CONST 
    0x2393: JUMPI v2390(0x23a3), v238f

    Begin block 0x23a3
    prev=[0x238b], succ=[0x23ca]
    =================================
    0x23aa: v23aa = ADD v2385, v2379
    0x23ad: v23ad = SUB v23aa, v2362
    0x23af: MSTORE v2367, v23ad
    0x23b3: v23b3 = MLOAD v228a
    0x23b5: MSTORE v23aa, v23b3
    0x23b6: v23b6(0x20) = CONST 
    0x23b8: v23b8 = ADD v23b6(0x20), v23aa
    0x23bc: v23bc = MLOAD v228a
    0x23be: v23be(0x20) = CONST 
    0x23c0: v23c0 = ADD v23be(0x20), v228a
    0x23c2: v23c2(0x20) = CONST 
    0x23c4: v23c4 = MUL v23c2(0x20), v23bc
    0x23c8: v23c8(0x0) = CONST 

    Begin block 0x23ca
    prev=[0x23a3, 0x23d3], succ=[0x23e2, 0x23d3]
    =================================
    0x23ca_0x0: v23ca_0 = PHI v23c8(0x0), v23dd
    0x23cd: v23cd = LT v23ca_0, v23c4
    0x23ce: v23ce = ISZERO v23cd
    0x23cf: v23cf(0x23e2) = CONST 
    0x23d2: JUMPI v23cf(0x23e2), v23ce

    Begin block 0x23e2
    prev=[0x23ca], succ=[0x1929]
    =================================
    0x23e9: v23e9 = ADD v23c4, v23b8
    0x23f0: v23f0(0x40) = CONST 
    0x23f2: v23f2 = MLOAD v23f0(0x40)
    0x23f5: v23f5 = SUB v23e9, v23f2
    0x23f7: LOG4 v23f2, v23f5, v233d(0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb), v233c, v2332, v2328(0x0)
    0x23fb: JUMP v18ed(0x1929)

    Begin block 0x1929
    prev=[0x23e2], succ=[0x2bae]
    =================================
    0x192d: JUMP v84d(0x2bae)

    Begin block 0x2bae
    prev=[0x1929], succ=[]
    =================================
    0x2baf: STOP 

    Begin block 0x23d3
    prev=[0x23ca], succ=[0x23ca]
    =================================
    0x23d3_0x0: v23d3_0 = PHI v23c8(0x0), v23dd
    0x23d5: v23d5 = ADD v23d3_0, v23c0
    0x23d6: v23d6 = MLOAD v23d5
    0x23d9: v23d9 = ADD v23d3_0, v23b8
    0x23da: MSTORE v23d9, v23d6
    0x23db: v23db(0x20) = CONST 
    0x23dd: v23dd = ADD v23db(0x20), v23d3_0
    0x23de: v23de(0x23ca) = CONST 
    0x23e1: JUMP v23de(0x23ca)

    Begin block 0x2394
    prev=[0x238b], succ=[0x238b]
    =================================
    0x2394_0x0: v2394_0 = PHI v2389(0x0), v239e
    0x2396: v2396 = ADD v2394_0, v2381
    0x2397: v2397 = MLOAD v2396
    0x239a: v239a = ADD v2394_0, v2379
    0x239b: MSTORE v239a, v2397
    0x239c: v239c(0x20) = CONST 
    0x239e: v239e = ADD v239c(0x20), v2394_0
    0x239f: v239f(0x238b) = CONST 
    0x23a2: JUMP v239f(0x238b)

    Begin block 0x22a1
    prev=[0x2286], succ=[0x22b0]
    =================================
    0x22a2: v22a2(0x20) = CONST 
    0x22a4: v22a4 = ADD v22a2(0x20), v228a
    0x22a5: v22a5(0x20) = CONST 
    0x22a8: v22a8 = MUL v2270, v22a5(0x20)
    0x22aa: v22aa = CALLDATASIZE 
    0x22ac: CALLDATACOPY v22a4, v22aa, v22a8
    0x22ad: v22ad = ADD v22a8, v22a4

}

function isOwnerOf(address,uint256)() public {
    Begin block 0x8ca
    prev=[], succ=[0x8dc, 0x8e0]
    =================================
    0x8cb: v8cb(0x2bcf) = CONST 
    0x8ce: v8ce(0x4) = CONST 
    0x8d1: v8d1 = CALLDATASIZE 
    0x8d2: v8d2 = SUB v8d1, v8ce(0x4)
    0x8d3: v8d3(0x40) = CONST 
    0x8d6: v8d6 = LT v8d2, v8d3(0x40)
    0x8d7: v8d7 = ISZERO v8d6
    0x8d8: v8d8(0x8e0) = CONST 
    0x8db: JUMPI v8d8(0x8e0), v8d7

    Begin block 0x8dc
    prev=[0x8ca], succ=[]
    =================================
    0x8dc: v8dc(0x0) = CONST 
    0x8df: REVERT v8dc(0x0), v8dc(0x0)

    Begin block 0x8e0
    prev=[0x8ca], succ=[0x192e0x8ca]
    =================================
    0x8e2: v8e2(0x1) = CONST 
    0x8e4: v8e4(0x1) = CONST 
    0x8e6: v8e6(0xa0) = CONST 
    0x8e8: v8e8(0x10000000000000000000000000000000000000000) = SHL v8e6(0xa0), v8e4(0x1)
    0x8e9: v8e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8e8(0x10000000000000000000000000000000000000000), v8e2(0x1)
    0x8eb: v8eb = CALLDATALOAD v8ce(0x4)
    0x8ec: v8ec = AND v8eb, v8e9(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ee: v8ee(0x20) = CONST 
    0x8f0: v8f0(0x24) = ADD v8ee(0x20), v8ce(0x4)
    0x8f1: v8f1 = CALLDATALOAD v8f0(0x24)
    0x8f2: v8f2(0x192e) = CONST 
    0x8f5: JUMP v8f2(0x192e)

    Begin block 0x192e0x8ca
    prev=[0x8e0], succ=[0x19460x8ca, 0x193f0x8ca]
    =================================
    0x192f0x8ca: v8ca192f(0x0) = CONST 
    0x19310x8ca: v8ca1931(0x1) = CONST 
    0x19330x8ca: v8ca1933(0x1) = CONST 
    0x19350x8ca: v8ca1935(0xa0) = CONST 
    0x19370x8ca: v8ca1937(0x10000000000000000000000000000000000000000) = SHL v8ca1935(0xa0), v8ca1933(0x1)
    0x19380x8ca: v8ca1938(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8ca1937(0x10000000000000000000000000000000000000000), v8ca1931(0x1)
    0x193a0x8ca: v8ca193a = AND v8ec, v8ca1938(0xffffffffffffffffffffffffffffffffffffffff)
    0x193b0x8ca: v8ca193b(0x1946) = CONST 
    0x193e0x8ca: JUMPI v8ca193b(0x1946), v8ca193a

    Begin block 0x19460x8ca
    prev=[0x192e0x8ca], succ=[0x2dfb0x8ca]
    =================================
    0x19480x8ca: v8ca1948(0x0) = CONST 
    0x194c0x8ca: MSTORE v8ca1948(0x0), v8f1
    0x194d0x8ca: v8ca194d(0x7) = CONST 
    0x194f0x8ca: v8ca194f(0x20) = CONST 
    0x19510x8ca: MSTORE v8ca194f(0x20), v8ca194d(0x7)
    0x19520x8ca: v8ca1952(0x40) = CONST 
    0x19550x8ca: v8ca1955 = SHA3 v8ca1948(0x0), v8ca1952(0x40)
    0x19560x8ca: v8ca1956 = SLOAD v8ca1955
    0x19570x8ca: v8ca1957(0x1) = CONST 
    0x19590x8ca: v8ca1959(0x1) = CONST 
    0x195b0x8ca: v8ca195b(0xa0) = CONST 
    0x195d0x8ca: v8ca195d(0x10000000000000000000000000000000000000000) = SHL v8ca195b(0xa0), v8ca1959(0x1)
    0x195e0x8ca: v8ca195e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8ca195d(0x10000000000000000000000000000000000000000), v8ca1957(0x1)
    0x19610x8ca: v8ca1961 = AND v8ca195e(0xffffffffffffffffffffffffffffffffffffffff), v8ec
    0x19630x8ca: v8ca1963 = AND v8ca1956, v8ca195e(0xffffffffffffffffffffffffffffffffffffffff)
    0x19640x8ca: v8ca1964 = EQ v8ca1963, v8ca1961
    0x19650x8ca: v8ca1965(0x2dfb) = CONST 
    0x19680x8ca: JUMP v8ca1965(0x2dfb)

    Begin block 0x2dfb0x8ca
    prev=[0x19460x8ca], succ=[0x2bcf]
    =================================
    0x2e000x8ca: JUMP v8cb(0x2bcf)

    Begin block 0x2bcf
    prev=[0x2dd60x8ca, 0x2dfb0x8ca], succ=[]
    =================================
    0x2bcf_0x0: v2bcf_0 = PHI v8ca1964, v8ca1940(0x0)
    0x2bd0: v2bd0(0x40) = CONST 
    0x2bd3: v2bd3 = MLOAD v2bd0(0x40)
    0x2bd5: v2bd5 = ISZERO v2bcf_0
    0x2bd6: v2bd6 = ISZERO v2bd5
    0x2bd8: MSTORE v2bd3, v2bd6
    0x2bd9: v2bd9 = MLOAD v2bd0(0x40)
    0x2bdd: v2bdd(0x0) = SUB v2bd3, v2bd9
    0x2bde: v2bde(0x20) = CONST 
    0x2be0: v2be0(0x20) = ADD v2bde(0x20), v2bdd(0x0)
    0x2be2: RETURN v2bd9, v2be0(0x20)

    Begin block 0x193f0x8ca
    prev=[0x192e0x8ca], succ=[0x2dd60x8ca]
    =================================
    0x19400x8ca: v8ca1940(0x0) = CONST 
    0x19420x8ca: v8ca1942(0x2dd6) = CONST 
    0x19450x8ca: JUMP v8ca1942(0x2dd6)

    Begin block 0x2dd60x8ca
    prev=[0x193f0x8ca], succ=[0x2bcf]
    =================================
    0x2ddb0x8ca: JUMP v8cb(0x2bcf)

}

function isApprovedForAll(address,address)() public {
    Begin block 0x8f6
    prev=[], succ=[0x908, 0x90c]
    =================================
    0x8f7: v8f7(0x2c02) = CONST 
    0x8fa: v8fa(0x4) = CONST 
    0x8fd: v8fd = CALLDATASIZE 
    0x8fe: v8fe = SUB v8fd, v8fa(0x4)
    0x8ff: v8ff(0x40) = CONST 
    0x902: v902 = LT v8fe, v8ff(0x40)
    0x903: v903 = ISZERO v902
    0x904: v904(0x90c) = CONST 
    0x907: JUMPI v904(0x90c), v903

    Begin block 0x908
    prev=[0x8f6], succ=[]
    =================================
    0x908: v908(0x0) = CONST 
    0x90b: REVERT v908(0x0), v908(0x0)

    Begin block 0x90c
    prev=[0x8f6], succ=[0x19690x8f6]
    =================================
    0x90e: v90e(0x1) = CONST 
    0x910: v910(0x1) = CONST 
    0x912: v912(0xa0) = CONST 
    0x914: v914(0x10000000000000000000000000000000000000000) = SHL v912(0xa0), v910(0x1)
    0x915: v915(0xffffffffffffffffffffffffffffffffffffffff) = SUB v914(0x10000000000000000000000000000000000000000), v90e(0x1)
    0x917: v917 = CALLDATALOAD v8fa(0x4)
    0x919: v919 = AND v915(0xffffffffffffffffffffffffffffffffffffffff), v917
    0x91b: v91b(0x20) = CONST 
    0x91d: v91d(0x24) = ADD v91b(0x20), v8fa(0x4)
    0x91e: v91e = CALLDATALOAD v91d(0x24)
    0x91f: v91f = AND v91e, v915(0xffffffffffffffffffffffffffffffffffffffff)
    0x920: v920(0x1969) = CONST 
    0x923: JUMP v920(0x1969)

    Begin block 0x19690x8f6
    prev=[0x90c], succ=[0x2c02]
    =================================
    0x196a0x8f6: v8f6196a(0x1) = CONST 
    0x196c0x8f6: v8f6196c(0x1) = CONST 
    0x196e0x8f6: v8f6196e(0xa0) = CONST 
    0x19700x8f6: v8f61970(0x10000000000000000000000000000000000000000) = SHL v8f6196e(0xa0), v8f6196c(0x1)
    0x19710x8f6: v8f61971(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8f61970(0x10000000000000000000000000000000000000000), v8f6196a(0x1)
    0x19740x8f6: v8f61974 = AND v8f61971(0xffffffffffffffffffffffffffffffffffffffff), v919
    0x19750x8f6: v8f61975(0x0) = CONST 
    0x19790x8f6: MSTORE v8f61975(0x0), v8f61974
    0x197a0x8f6: v8f6197a(0x8) = CONST 
    0x197c0x8f6: v8f6197c(0x20) = CONST 
    0x19800x8f6: MSTORE v8f6197c(0x20), v8f6197a(0x8)
    0x19810x8f6: v8f61981(0x40) = CONST 
    0x19850x8f6: v8f61985 = SHA3 v8f61975(0x0), v8f61981(0x40)
    0x19890x8f6: v8f61989 = AND v8f61971(0xffffffffffffffffffffffffffffffffffffffff), v91f
    0x198b0x8f6: MSTORE v8f61975(0x0), v8f61989
    0x198f0x8f6: MSTORE v8f6197c(0x20), v8f61985
    0x19900x8f6: v8f61990 = SHA3 v8f61975(0x0), v8f61981(0x40)
    0x19910x8f6: v8f61991 = SLOAD v8f61990
    0x19920x8f6: v8f61992(0xff) = CONST 
    0x19940x8f6: v8f61994 = AND v8f61992(0xff), v8f61991
    0x19960x8f6: JUMP v8f7(0x2c02)

    Begin block 0x2c02
    prev=[0x19690x8f6], succ=[]
    =================================
    0x2c03: v2c03(0x40) = CONST 
    0x2c06: v2c06 = MLOAD v2c03(0x40)
    0x2c08: v2c08 = ISZERO v8f61994
    0x2c09: v2c09 = ISZERO v2c08
    0x2c0b: MSTORE v2c06, v2c09
    0x2c0c: v2c0c = MLOAD v2c03(0x40)
    0x2c10: v2c10(0x0) = SUB v2c06, v2c0c
    0x2c11: v2c11(0x20) = CONST 
    0x2c13: v2c13(0x20) = ADD v2c11(0x20), v2c10(0x0)
    0x2c15: RETURN v2c0c, v2c13(0x20)

}

function safeTransferFrom(address,address,uint256,uint256,bytes)() public {
    Begin block 0x924
    prev=[], succ=[0x936, 0x93a]
    =================================
    0x925: v925(0x2c35) = CONST 
    0x928: v928(0x4) = CONST 
    0x92b: v92b = CALLDATASIZE 
    0x92c: v92c = SUB v92b, v928(0x4)
    0x92d: v92d(0xa0) = CONST 
    0x930: v930 = LT v92c, v92d(0xa0)
    0x931: v931 = ISZERO v930
    0x932: v932(0x93a) = CONST 
    0x935: JUMPI v932(0x93a), v931

    Begin block 0x936
    prev=[0x924], succ=[]
    =================================
    0x936: v936(0x0) = CONST 
    0x939: REVERT v936(0x0), v936(0x0)

    Begin block 0x93a
    prev=[0x924], succ=[0x975, 0x979]
    =================================
    0x93b: v93b(0x1) = CONST 
    0x93d: v93d(0x1) = CONST 
    0x93f: v93f(0xa0) = CONST 
    0x941: v941(0x10000000000000000000000000000000000000000) = SHL v93f(0xa0), v93d(0x1)
    0x942: v942(0xffffffffffffffffffffffffffffffffffffffff) = SUB v941(0x10000000000000000000000000000000000000000), v93b(0x1)
    0x944: v944 = CALLDATALOAD v928(0x4)
    0x946: v946 = AND v942(0xffffffffffffffffffffffffffffffffffffffff), v944
    0x948: v948(0x20) = CONST 
    0x94b: v94b(0x24) = ADD v928(0x4), v948(0x20)
    0x94c: v94c = CALLDATALOAD v94b(0x24)
    0x94f: v94f = AND v942(0xffffffffffffffffffffffffffffffffffffffff), v94c
    0x951: v951(0x40) = CONST 
    0x954: v954(0x44) = ADD v928(0x4), v951(0x40)
    0x955: v955 = CALLDATALOAD v954(0x44)
    0x957: v957(0x60) = CONST 
    0x95a: v95a(0x64) = ADD v928(0x4), v957(0x60)
    0x95b: v95b = CALLDATALOAD v95a(0x64)
    0x95e: v95e = ADD v928(0x4), v92c
    0x960: v960(0xa0) = CONST 
    0x963: v963(0xa4) = ADD v928(0x4), v960(0xa0)
    0x964: v964(0x80) = CONST 
    0x967: v967(0x84) = ADD v928(0x4), v964(0x80)
    0x968: v968 = CALLDATALOAD v967(0x84)
    0x969: v969(0x1) = CONST 
    0x96b: v96b(0x20) = CONST 
    0x96d: v96d(0x100000000) = SHL v96b(0x20), v969(0x1)
    0x96f: v96f = GT v968, v96d(0x100000000)
    0x970: v970 = ISZERO v96f
    0x971: v971(0x979) = CONST 
    0x974: JUMPI v971(0x979), v970

    Begin block 0x975
    prev=[0x93a], succ=[]
    =================================
    0x975: v975(0x0) = CONST 
    0x978: REVERT v975(0x0), v975(0x0)

    Begin block 0x979
    prev=[0x93a], succ=[0x987, 0x98b]
    =================================
    0x97b: v97b = ADD v928(0x4), v968
    0x97d: v97d(0x20) = CONST 
    0x980: v980 = ADD v97b, v97d(0x20)
    0x981: v981 = GT v980, v95e
    0x982: v982 = ISZERO v981
    0x983: v983(0x98b) = CONST 
    0x986: JUMPI v983(0x98b), v982

    Begin block 0x987
    prev=[0x979], succ=[]
    =================================
    0x987: v987(0x0) = CONST 
    0x98a: REVERT v987(0x0), v987(0x0)

    Begin block 0x98b
    prev=[0x979], succ=[0x9a8, 0x9ac]
    =================================
    0x98d: v98d = CALLDATALOAD v97b
    0x98f: v98f(0x20) = CONST 
    0x991: v991 = ADD v98f(0x20), v97b
    0x994: v994(0x1) = CONST 
    0x997: v997 = MUL v98d, v994(0x1)
    0x999: v999 = ADD v991, v997
    0x99a: v99a = GT v999, v95e
    0x99b: v99b(0x1) = CONST 
    0x99d: v99d(0x20) = CONST 
    0x99f: v99f(0x100000000) = SHL v99d(0x20), v99b(0x1)
    0x9a1: v9a1 = GT v98d, v99f(0x100000000)
    0x9a2: v9a2 = OR v9a1, v99a
    0x9a3: v9a3 = ISZERO v9a2
    0x9a4: v9a4(0x9ac) = CONST 
    0x9a7: JUMPI v9a4(0x9ac), v9a3

    Begin block 0x9a8
    prev=[0x98b], succ=[]
    =================================
    0x9a8: v9a8(0x0) = CONST 
    0x9ab: REVERT v9a8(0x0), v9a8(0x0)

    Begin block 0x9ac
    prev=[0x98b], succ=[0x1997]
    =================================
    0x9b1: v9b1(0x1f) = CONST 
    0x9b3: v9b3 = ADD v9b1(0x1f), v98d
    0x9b4: v9b4(0x20) = CONST 
    0x9b8: v9b8 = DIV v9b3, v9b4(0x20)
    0x9b9: v9b9 = MUL v9b8, v9b4(0x20)
    0x9ba: v9ba(0x20) = CONST 
    0x9bc: v9bc = ADD v9ba(0x20), v9b9
    0x9bd: v9bd(0x40) = CONST 
    0x9bf: v9bf = MLOAD v9bd(0x40)
    0x9c2: v9c2 = ADD v9bf, v9bc
    0x9c3: v9c3(0x40) = CONST 
    0x9c5: MSTORE v9c3(0x40), v9c2
    0x9cd: MSTORE v9bf, v98d
    0x9ce: v9ce(0x20) = CONST 
    0x9d0: v9d0 = ADD v9ce(0x20), v9bf
    0x9d6: CALLDATACOPY v9d0, v991, v98d
    0x9d7: v9d7(0x0) = CONST 
    0x9da: v9da = ADD v9d0, v98d
    0x9de: MSTORE v9da, v9d7(0x0)
    0x9e3: v9e3(0x1997) = CONST 
    0x9ec: JUMP v9e3(0x1997)

    Begin block 0x1997
    prev=[0x9ac], succ=[0x19a6, 0x19dc]
    =================================
    0x1998: v1998(0x1) = CONST 
    0x199a: v199a(0x1) = CONST 
    0x199c: v199c(0xa0) = CONST 
    0x199e: v199e(0x10000000000000000000000000000000000000000) = SHL v199c(0xa0), v199a(0x1)
    0x199f: v199f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v199e(0x10000000000000000000000000000000000000000), v1998(0x1)
    0x19a1: v19a1 = AND v94f, v199f(0xffffffffffffffffffffffffffffffffffffffff)
    0x19a2: v19a2(0x19dc) = CONST 
    0x19a5: JUMPI v19a2(0x19dc), v19a1

    Begin block 0x19a6
    prev=[0x1997], succ=[]
    =================================
    0x19a6: v19a6(0x40) = CONST 
    0x19a8: v19a8 = MLOAD v19a6(0x40)
    0x19a9: v19a9(0x461bcd) = CONST 
    0x19ad: v19ad(0xe5) = CONST 
    0x19af: v19af(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19ad(0xe5), v19a9(0x461bcd)
    0x19b1: MSTORE v19a8, v19af(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19b2: v19b2(0x4) = CONST 
    0x19b4: v19b4 = ADD v19b2(0x4), v19a8
    0x19b7: v19b7(0x20) = CONST 
    0x19b9: v19b9 = ADD v19b7(0x20), v19b4
    0x19bc: v19bc(0x20) = SUB v19b9, v19b4
    0x19be: MSTORE v19b4, v19bc(0x20)
    0x19bf: v19bf(0x24) = CONST 
    0x19c2: MSTORE v19b9, v19bf(0x24)
    0x19c3: v19c3(0x20) = CONST 
    0x19c5: v19c5 = ADD v19c3(0x20), v19b9
    0x19c7: v19c7(0x272d) = CONST 
    0x19ca: v19ca(0x24) = CONST 
    0x19cd: CODECOPY v19c5, v19c7(0x272d), v19ca(0x24)
    0x19ce: v19ce(0x40) = CONST 
    0x19d0: v19d0 = ADD v19ce(0x40), v19c5
    0x19d4: v19d4(0x40) = CONST 
    0x19d6: v19d6 = MLOAD v19d4(0x40)
    0x19d9: v19d9(0x84) = SUB v19d0, v19d6
    0x19db: REVERT v19d6, v19d9(0x84)

    Begin block 0x19dc
    prev=[0x1997], succ=[0x19e5, 0x1a22]
    =================================
    0x19de: v19de(0x1) = CONST 
    0x19e0: v19e0 = EQ v19de(0x1), v95b
    0x19e1: v19e1(0x1a22) = CONST 
    0x19e4: JUMPI v19e1(0x1a22), v19e0

    Begin block 0x19e5
    prev=[0x19dc], succ=[]
    =================================
    0x19e5: v19e5(0x40) = CONST 
    0x19e8: v19e8 = MLOAD v19e5(0x40)
    0x19e9: v19e9(0x461bcd) = CONST 
    0x19ed: v19ed(0xe5) = CONST 
    0x19ef: v19ef(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19ed(0xe5), v19e9(0x461bcd)
    0x19f1: MSTORE v19e8, v19ef(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19f2: v19f2(0x20) = CONST 
    0x19f4: v19f4(0x4) = CONST 
    0x19f7: v19f7 = ADD v19e8, v19f4(0x4)
    0x19f8: MSTORE v19f7, v19f2(0x20)
    0x19f9: v19f9(0xe) = CONST 
    0x19fb: v19fb(0x24) = CONST 
    0x19fe: v19fe = ADD v19e8, v19fb(0x24)
    0x19ff: MSTORE v19fe, v19f9(0xe)
    0x1a00: v1a00(0x125b9d985b1a5908185b5bdd5b9d) = CONST 
    0x1a0f: v1a0f(0x92) = CONST 
    0x1a11: v1a11(0x496e76616c696420616d6f756e74000000000000000000000000000000000000) = SHL v1a0f(0x92), v1a00(0x125b9d985b1a5908185b5bdd5b9d)
    0x1a12: v1a12(0x44) = CONST 
    0x1a15: v1a15 = ADD v19e8, v1a12(0x44)
    0x1a16: MSTORE v1a15, v1a11(0x496e76616c696420616d6f756e74000000000000000000000000000000000000)
    0x1a18: v1a18 = MLOAD v19e5(0x40)
    0x1a1c: v1a1c(0x0) = SUB v19e8, v1a18
    0x1a1d: v1a1d(0x64) = CONST 
    0x1a1f: v1a1f(0x64) = ADD v1a1d(0x64), v1a1c(0x0)
    0x1a21: REVERT v1a18, v1a1f(0x64)

    Begin block 0x1a22
    prev=[0x19dc], succ=[0x1a3e, 0x1a34]
    =================================
    0x1a23: v1a23(0x1) = CONST 
    0x1a25: v1a25(0x1) = CONST 
    0x1a27: v1a27(0xa0) = CONST 
    0x1a29: v1a29(0x10000000000000000000000000000000000000000) = SHL v1a27(0xa0), v1a25(0x1)
    0x1a2a: v1a2a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a29(0x10000000000000000000000000000000000000000), v1a23(0x1)
    0x1a2c: v1a2c = AND v946, v1a2a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a2d: v1a2d = CALLER 
    0x1a2e: v1a2e = EQ v1a2d, v1a2c
    0x1a30: v1a30(0x1a3e) = CONST 
    0x1a33: JUMPI v1a30(0x1a3e), v1a2e

    Begin block 0x1a3e
    prev=[0x1a22, 0x1969B0x1a34], succ=[0x1a43, 0x1a79]
    =================================
    0x1a3e_0x0: v1a3e_0 = PHI v1a2e, v1994V1a34
    0x1a3f: v1a3f(0x1a79) = CONST 
    0x1a42: JUMPI v1a3f(0x1a79), v1a3e_0

    Begin block 0x1a43
    prev=[0x1a3e], succ=[]
    =================================
    0x1a43: v1a43(0x40) = CONST 
    0x1a45: v1a45 = MLOAD v1a43(0x40)
    0x1a46: v1a46(0x461bcd) = CONST 
    0x1a4a: v1a4a(0xe5) = CONST 
    0x1a4c: v1a4c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1a4a(0xe5), v1a46(0x461bcd)
    0x1a4e: MSTORE v1a45, v1a4c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a4f: v1a4f(0x4) = CONST 
    0x1a51: v1a51 = ADD v1a4f(0x4), v1a45
    0x1a54: v1a54(0x20) = CONST 
    0x1a56: v1a56 = ADD v1a54(0x20), v1a51
    0x1a59: v1a59(0x20) = SUB v1a56, v1a51
    0x1a5b: MSTORE v1a51, v1a59(0x20)
    0x1a5c: v1a5c(0x2d) = CONST 
    0x1a5f: MSTORE v1a56, v1a5c(0x2d)
    0x1a60: v1a60(0x20) = CONST 
    0x1a62: v1a62 = ADD v1a60(0x20), v1a56
    0x1a64: v1a64(0x2751) = CONST 
    0x1a67: v1a67(0x2d) = CONST 
    0x1a6a: CODECOPY v1a62, v1a64(0x2751), v1a67(0x2d)
    0x1a6b: v1a6b(0x40) = CONST 
    0x1a6d: v1a6d = ADD v1a6b(0x40), v1a62
    0x1a71: v1a71(0x40) = CONST 
    0x1a73: v1a73 = MLOAD v1a71(0x40)
    0x1a76: v1a76(0x84) = SUB v1a6d, v1a73
    0x1a78: REVERT v1a73, v1a76(0x84)

    Begin block 0x1a79
    prev=[0x1a3e], succ=[0x1a83]
    =================================
    0x1a7a: v1a7a(0x1a83) = CONST 
    0x1a7f: v1a7f(0x192e) = CONST 
    0x1a82: v1a82_0 = CALLPRIVATE v1a7f(0x192e), v955, v946, v1a7a(0x1a83)

    Begin block 0x1a83
    prev=[0x1a79], succ=[0x1a88, 0x1ac4]
    =================================
    0x1a84: v1a84(0x1ac4) = CONST 
    0x1a87: JUMPI v1a84(0x1ac4), v1a82_0

    Begin block 0x1a88
    prev=[0x1a83], succ=[]
    =================================
    0x1a88: v1a88(0x40) = CONST 
    0x1a8b: v1a8b = MLOAD v1a88(0x40)
    0x1a8c: v1a8c(0x461bcd) = CONST 
    0x1a90: v1a90(0xe5) = CONST 
    0x1a92: v1a92(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1a90(0xe5), v1a8c(0x461bcd)
    0x1a94: MSTORE v1a8b, v1a92(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a95: v1a95(0x20) = CONST 
    0x1a97: v1a97(0x4) = CONST 
    0x1a9a: v1a9a = ADD v1a8b, v1a97(0x4)
    0x1a9b: MSTORE v1a9a, v1a95(0x20)
    0x1a9c: v1a9c(0xd) = CONST 
    0x1a9e: v1a9e(0x24) = CONST 
    0x1aa1: v1aa1 = ADD v1a8b, v1a9e(0x24)
    0x1aa2: MSTORE v1aa1, v1a9c(0xd)
    0x1aa3: v1aa3(0x2737ba103a34329037bbb732b9) = CONST 
    0x1ab1: v1ab1(0x99) = CONST 
    0x1ab3: v1ab3(0x4e6f7420746865206f776e657200000000000000000000000000000000000000) = SHL v1ab1(0x99), v1aa3(0x2737ba103a34329037bbb732b9)
    0x1ab4: v1ab4(0x44) = CONST 
    0x1ab7: v1ab7 = ADD v1a8b, v1ab4(0x44)
    0x1ab8: MSTORE v1ab7, v1ab3(0x4e6f7420746865206f776e657200000000000000000000000000000000000000)
    0x1aba: v1aba = MLOAD v1a88(0x40)
    0x1abe: v1abe(0x0) = SUB v1a8b, v1aba
    0x1abf: v1abf(0x64) = CONST 
    0x1ac1: v1ac1(0x64) = ADD v1abf(0x64), v1abe(0x0)
    0x1ac3: REVERT v1aba, v1ac1(0x64)

    Begin block 0x1ac4
    prev=[0x1a83], succ=[0x2e20]
    =================================
    0x1ac5: v1ac5(0x0) = CONST 
    0x1ac9: MSTORE v1ac5(0x0), v955
    0x1aca: v1aca(0x7) = CONST 
    0x1acc: v1acc(0x20) = CONST 
    0x1ad0: MSTORE v1acc(0x20), v1aca(0x7)
    0x1ad1: v1ad1(0x40) = CONST 
    0x1ad6: v1ad6 = SHA3 v1ac5(0x0), v1ad1(0x40)
    0x1ad8: v1ad8 = SLOAD v1ad6
    0x1ad9: v1ad9(0x1) = CONST 
    0x1adb: v1adb(0x1) = CONST 
    0x1add: v1add(0xa0) = CONST 
    0x1adf: v1adf(0x10000000000000000000000000000000000000000) = SHL v1add(0xa0), v1adb(0x1)
    0x1ae0: v1ae0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1adf(0x10000000000000000000000000000000000000000), v1ad9(0x1)
    0x1ae1: v1ae1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1ae0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ae2: v1ae2 = AND v1ae1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1ad8
    0x1ae3: v1ae3(0x1) = CONST 
    0x1ae5: v1ae5(0x1) = CONST 
    0x1ae7: v1ae7(0xa0) = CONST 
    0x1ae9: v1ae9(0x10000000000000000000000000000000000000000) = SHL v1ae7(0xa0), v1ae5(0x1)
    0x1aea: v1aea(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ae9(0x10000000000000000000000000000000000000000), v1ae3(0x1)
    0x1aed: v1aed = AND v1aea(0xffffffffffffffffffffffffffffffffffffffff), v94f
    0x1af0: v1af0 = OR v1aed, v1ae2
    0x1af3: SSTORE v1ad6, v1af0
    0x1af5: v1af5 = MLOAD v1ad1(0x40)
    0x1af8: MSTORE v1af5, v955
    0x1afb: v1afb = ADD v1af5, v1acc(0x20)
    0x1afe: MSTORE v1afb, v95b
    0x1b00: v1b00 = MLOAD v1ad1(0x40)
    0x1b05: v1b05 = AND v946, v1aea(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b07: v1b07 = CALLER 
    0x1b09: v1b09(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62) = CONST 
    0x1b2e: v1b2e(0x0) = SUB v1af5, v1b00
    0x1b2f: v1b2f(0x40) = ADD v1b2e(0x0), v1ad1(0x40)
    0x1b31: LOG4 v1b00, v1b2f(0x40), v1b09(0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62), v1b07, v1b05, v1aed
    0x1b32: v1b32(0x2e20) = CONST 
    0x1b35: v1b35 = CALLER 
    0x1b3b: v1b3b(0x23fc) = CONST 
    0x1b3e: CALLPRIVATE v1b3b(0x23fc), v9bf, v95b, v955, v94f, v946, v1b35, v1b32(0x2e20)

    Begin block 0x2e20
    prev=[0x1ac4], succ=[0x2c35]
    =================================
    0x2e26: JUMP v925(0x2c35)

    Begin block 0x2c35
    prev=[0x2e20], succ=[]
    =================================
    0x2c36: STOP 

    Begin block 0x1a34
    prev=[0x1a22], succ=[0x1969B0x1a34]
    =================================
    0x1a35: v1a35(0x1a3e) = CONST 
    0x1a39: v1a39 = CALLER 
    0x1a3a: v1a3a(0x1969) = CONST 
    0x1a3d: JUMP v1a3a(0x1969)

    Begin block 0x1969B0x1a34
    prev=[0x1a34], succ=[0x1a3e]
    =================================
    0x196aS0x1a34: v196aV1a34(0x1) = CONST 
    0x196cS0x1a34: v196cV1a34(0x1) = CONST 
    0x196eS0x1a34: v196eV1a34(0xa0) = CONST 
    0x1970S0x1a34: v1970V1a34(0x10000000000000000000000000000000000000000) = SHL v196eV1a34(0xa0), v196cV1a34(0x1)
    0x1971S0x1a34: v1971V1a34(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1970V1a34(0x10000000000000000000000000000000000000000), v196aV1a34(0x1)
    0x1974S0x1a34: v1974V1a34 = AND v1971V1a34(0xffffffffffffffffffffffffffffffffffffffff), v946
    0x1975S0x1a34: v1975V1a34(0x0) = CONST 
    0x1979S0x1a34: MSTORE v1975V1a34(0x0), v1974V1a34
    0x197aS0x1a34: v197aV1a34(0x8) = CONST 
    0x197cS0x1a34: v197cV1a34(0x20) = CONST 
    0x1980S0x1a34: MSTORE v197cV1a34(0x20), v197aV1a34(0x8)
    0x1981S0x1a34: v1981V1a34(0x40) = CONST 
    0x1985S0x1a34: v1985V1a34 = SHA3 v1975V1a34(0x0), v1981V1a34(0x40)
    0x1989S0x1a34: v1989V1a34 = AND v1971V1a34(0xffffffffffffffffffffffffffffffffffffffff), v1a39
    0x198bS0x1a34: MSTORE v1975V1a34(0x0), v1989V1a34
    0x198fS0x1a34: MSTORE v197cV1a34(0x20), v1985V1a34
    0x1990S0x1a34: v1990V1a34 = SHA3 v1975V1a34(0x0), v1981V1a34(0x40)
    0x1991S0x1a34: v1991V1a34 = SLOAD v1990V1a34
    0x1992S0x1a34: v1992V1a34(0xff) = CONST 
    0x1994S0x1a34: v1994V1a34 = AND v1992V1a34(0xff), v1991V1a34
    0x1996S0x1a34: JUMP v1a35(0x1a3e)

}

function minters(address)() public {
    Begin block 0x9ed
    prev=[], succ=[0x9ff, 0xa03]
    =================================
    0x9ee: v9ee(0x2c56) = CONST 
    0x9f1: v9f1(0x4) = CONST 
    0x9f4: v9f4 = CALLDATASIZE 
    0x9f5: v9f5 = SUB v9f4, v9f1(0x4)
    0x9f6: v9f6(0x20) = CONST 
    0x9f9: v9f9 = LT v9f5, v9f6(0x20)
    0x9fa: v9fa = ISZERO v9f9
    0x9fb: v9fb(0xa03) = CONST 
    0x9fe: JUMPI v9fb(0xa03), v9fa

    Begin block 0x9ff
    prev=[0x9ed], succ=[]
    =================================
    0x9ff: v9ff(0x0) = CONST 
    0xa02: REVERT v9ff(0x0), v9ff(0x0)

    Begin block 0xa03
    prev=[0x9ed], succ=[0x1b3f]
    =================================
    0xa05: va05 = CALLDATALOAD v9f1(0x4)
    0xa06: va06(0x1) = CONST 
    0xa08: va08(0x1) = CONST 
    0xa0a: va0a(0xa0) = CONST 
    0xa0c: va0c(0x10000000000000000000000000000000000000000) = SHL va0a(0xa0), va08(0x1)
    0xa0d: va0d(0xffffffffffffffffffffffffffffffffffffffff) = SUB va0c(0x10000000000000000000000000000000000000000), va06(0x1)
    0xa0e: va0e = AND va0d(0xffffffffffffffffffffffffffffffffffffffff), va05
    0xa0f: va0f(0x1b3f) = CONST 
    0xa12: JUMP va0f(0x1b3f)

    Begin block 0x1b3f
    prev=[0xa03], succ=[0x2c56]
    =================================
    0x1b40: v1b40(0x5) = CONST 
    0x1b42: v1b42(0x20) = CONST 
    0x1b44: MSTORE v1b42(0x20), v1b40(0x5)
    0x1b45: v1b45(0x0) = CONST 
    0x1b49: MSTORE v1b45(0x0), va0e
    0x1b4a: v1b4a(0x40) = CONST 
    0x1b4d: v1b4d = SHA3 v1b45(0x0), v1b4a(0x40)
    0x1b4e: v1b4e = SLOAD v1b4d
    0x1b4f: v1b4f(0xff) = CONST 
    0x1b51: v1b51 = AND v1b4f(0xff), v1b4e
    0x1b53: JUMP v9ee(0x2c56)

    Begin block 0x2c56
    prev=[0x1b3f], succ=[]
    =================================
    0x2c57: v2c57(0x40) = CONST 
    0x2c5a: v2c5a = MLOAD v2c57(0x40)
    0x2c5c: v2c5c = ISZERO v1b51
    0x2c5d: v2c5d = ISZERO v2c5c
    0x2c5f: MSTORE v2c5a, v2c5d
    0x2c60: v2c60 = MLOAD v2c57(0x40)
    0x2c64: v2c64(0x0) = SUB v2c5a, v2c60
    0x2c65: v2c65(0x20) = CONST 
    0x2c67: v2c67(0x20) = ADD v2c65(0x20), v2c64(0x0)
    0x2c69: RETURN v2c60, v2c67(0x20)

}

