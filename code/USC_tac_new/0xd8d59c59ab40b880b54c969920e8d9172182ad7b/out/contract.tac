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
    prev=[0x0], succ=[0x1a, 0x2e65]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x2dc2: v2dc2(0x2e65) = CONST 
    0x2dc3: JUMPI v2dc2(0x2e65), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x12a, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x554249b3) = CONST 
    0x26: v26 = GT v21(0x554249b3), v1f
    0x27: v27(0x12a) = CONST 
    0x2a: JUMPI v27(0x12a), v26

    Begin block 0x12a
    prev=[0x1a], succ=[0x1bd, 0x136]
    =================================
    0x12c: v12c(0x313ce567) = CONST 
    0x131: v131 = GT v12c(0x313ce567), v1f
    0x132: v132(0x1bd) = CONST 
    0x135: JUMPI v132(0x1bd), v131

    Begin block 0x1bd
    prev=[0x12a], succ=[0x1f9, 0x1c9]
    =================================
    0x1bf: v1bf(0x18160ddd) = CONST 
    0x1c4: v1c4 = GT v1bf(0x18160ddd), v1f
    0x1c5: v1c5(0x1f9) = CONST 
    0x1c8: JUMPI v1c5(0x1f9), v1c4

    Begin block 0x1f9
    prev=[0x1bd], succ=[0x2e08, 0x205]
    =================================
    0x1fb: v1fb(0x2d3fdc9) = CONST 
    0x200: v200 = EQ v1fb(0x2d3fdc9), v1f
    0x2e00: v2e00(0x2e08) = CONST 
    0x2e01: JUMPI v2e00(0x2e08), v200

    Begin block 0x2e08
    prev=[0x1f9], succ=[]
    =================================
    0x2e09: v2e09(0x22b) = CONST 
    0x2e0a: CALLPRIVATE v2e09(0x22b)

    Begin block 0x205
    prev=[0x1f9], succ=[0x2e0b, 0x210]
    =================================
    0x206: v206(0x6fdde03) = CONST 
    0x20b: v20b = EQ v206(0x6fdde03), v1f
    0x2e02: v2e02(0x2e0b) = CONST 
    0x2e03: JUMPI v2e02(0x2e0b), v20b

    Begin block 0x2e0b
    prev=[0x205], succ=[]
    =================================
    0x2e0c: v2e0c(0x245) = CONST 
    0x2e0d: CALLPRIVATE v2e0c(0x245)

    Begin block 0x210
    prev=[0x205], succ=[0x2e0e, 0x21b]
    =================================
    0x211: v211(0x95ea7b3) = CONST 
    0x216: v216 = EQ v211(0x95ea7b3), v1f
    0x2e04: v2e04(0x2e0e) = CONST 
    0x2e05: JUMPI v2e04(0x2e0e), v216

    Begin block 0x2e0e
    prev=[0x210], succ=[]
    =================================
    0x2e0f: v2e0f(0x2c2) = CONST 
    0x2e10: CALLPRIVATE v2e0f(0x2c2)

    Begin block 0x21b
    prev=[0x210], succ=[0x2e11, 0x226]
    =================================
    0x21c: v21c(0x9ab8bba) = CONST 
    0x221: v221 = EQ v21c(0x9ab8bba), v1f
    0x2e06: v2e06(0x2e11) = CONST 
    0x2e07: JUMPI v2e06(0x2e11), v221

    Begin block 0x2e11
    prev=[0x21b], succ=[]
    =================================
    0x2e12: v2e12(0x30f) = CONST 
    0x2e13: CALLPRIVATE v2e12(0x30f)

    Begin block 0x226
    prev=[0x21b], succ=[]
    =================================
    0x227: v227(0x0) = CONST 
    0x22a: REVERT v227(0x0), v227(0x0)

    Begin block 0x1c9
    prev=[0x1bd], succ=[0x2e14, 0x1d4]
    =================================
    0x1ca: v1ca(0x18160ddd) = CONST 
    0x1cf: v1cf = EQ v1ca(0x18160ddd), v1f
    0x2df8: v2df8(0x2e14) = CONST 
    0x2df9: JUMPI v2df8(0x2e14), v1cf

    Begin block 0x2e14
    prev=[0x1c9], succ=[]
    =================================
    0x2e15: v2e15(0x34a) = CONST 
    0x2e16: CALLPRIVATE v2e15(0x34a)

    Begin block 0x1d4
    prev=[0x1c9], succ=[0x2e17, 0x1df]
    =================================
    0x1d5: v1d5(0x23b872dd) = CONST 
    0x1da: v1da = EQ v1d5(0x23b872dd), v1f
    0x2dfa: v2dfa(0x2e17) = CONST 
    0x2dfb: JUMPI v2dfa(0x2e17), v1da

    Begin block 0x2e17
    prev=[0x1d4], succ=[]
    =================================
    0x2e18: v2e18(0x352) = CONST 
    0x2e19: CALLPRIVATE v2e18(0x352)

    Begin block 0x1df
    prev=[0x1d4], succ=[0x2e1a, 0x1ea]
    =================================
    0x1e0: v1e0(0x296f4000) = CONST 
    0x1e5: v1e5 = EQ v1e0(0x296f4000), v1f
    0x2dfc: v2dfc(0x2e1a) = CONST 
    0x2dfd: JUMPI v2dfc(0x2e1a), v1e5

    Begin block 0x2e1a
    prev=[0xf9, 0xa3, 0xea, 0x1df], succ=[]
    =================================
    0x2e1b: v2e1b(0x395) = CONST 
    0x2e1c: CALLPRIVATE v2e1b(0x395)

    Begin block 0x1ea
    prev=[0x1df], succ=[0x1f5, 0x2e1d]
    =================================
    0x1eb: v1eb(0x2e440403) = CONST 
    0x1f0: v1f0 = EQ v1eb(0x2e440403), v1f
    0x2dfe: v2dfe(0x2e1d) = CONST 
    0x2dff: JUMPI v2dfe(0x2e1d), v1f0

    Begin block 0x1f5
    prev=[0x1ea], succ=[0x2477]
    =================================
    0x1f5: v1f5(0x2477) = CONST 
    0x1f8: JUMP v1f5(0x2477)

    Begin block 0x2477
    prev=[0x1f5], succ=[]
    =================================
    0x2478: v2478(0x0) = CONST 
    0x247b: REVERT v2478(0x0), v2478(0x0)

    Begin block 0x2e1d
    prev=[0x1ea], succ=[]
    =================================
    0x2e1e: v2e1e(0x3d8) = CONST 
    0x2e1f: CALLPRIVATE v2e1e(0x3d8)

    Begin block 0x136
    prev=[0x12a], succ=[0x18c, 0x141]
    =================================
    0x137: v137(0x42966c68) = CONST 
    0x13c: v13c = GT v137(0x42966c68), v1f
    0x13d: v13d(0x18c) = CONST 
    0x140: JUMPI v13d(0x18c), v13c

    Begin block 0x18c
    prev=[0x136], succ=[0x2e20, 0x198]
    =================================
    0x18e: v18e(0x313ce567) = CONST 
    0x193: v193 = EQ v18e(0x313ce567), v1f
    0x2df0: v2df0(0x2e20) = CONST 
    0x2df1: JUMPI v2df0(0x2e20), v193

    Begin block 0x2e20
    prev=[0x18c], succ=[]
    =================================
    0x2e21: v2e21(0x3f6) = CONST 
    0x2e22: CALLPRIVATE v2e21(0x3f6)

    Begin block 0x198
    prev=[0x18c], succ=[0x2e23, 0x1a3]
    =================================
    0x199: v199(0x3820a686) = CONST 
    0x19e: v19e = EQ v199(0x3820a686), v1f
    0x2df2: v2df2(0x2e23) = CONST 
    0x2df3: JUMPI v2df2(0x2e23), v19e

    Begin block 0x2e23
    prev=[0x198], succ=[]
    =================================
    0x2e24: v2e24(0x3fe) = CONST 
    0x2e25: CALLPRIVATE v2e24(0x3fe)

    Begin block 0x1a3
    prev=[0x198], succ=[0x2e26, 0x1ae]
    =================================
    0x1a4: v1a4(0x39509351) = CONST 
    0x1a9: v1a9 = EQ v1a4(0x39509351), v1f
    0x2df4: v2df4(0x2e26) = CONST 
    0x2df5: JUMPI v2df4(0x2e26), v1a9

    Begin block 0x2e26
    prev=[0x1a3], succ=[]
    =================================
    0x2e27: v2e27(0x431) = CONST 
    0x2e28: CALLPRIVATE v2e27(0x431)

    Begin block 0x1ae
    prev=[0x1a3], succ=[0x1b9, 0x2e29]
    =================================
    0x1af: v1af(0x40c10f19) = CONST 
    0x1b4: v1b4 = EQ v1af(0x40c10f19), v1f
    0x2df6: v2df6(0x2e29) = CONST 
    0x2df7: JUMPI v2df6(0x2e29), v1b4

    Begin block 0x1b9
    prev=[0x1ae], succ=[0x2453]
    =================================
    0x1b9: v1b9(0x2453) = CONST 
    0x1bc: JUMP v1b9(0x2453)

    Begin block 0x2453
    prev=[0x1b9], succ=[]
    =================================
    0x2454: v2454(0x0) = CONST 
    0x2457: REVERT v2454(0x0), v2454(0x0)

    Begin block 0x2e29
    prev=[0x1ae], succ=[]
    =================================
    0x2e2a: v2e2a(0x46a) = CONST 
    0x2e2b: CALLPRIVATE v2e2a(0x46a)

    Begin block 0x141
    prev=[0x136], succ=[0x171, 0x14c]
    =================================
    0x142: v142(0x4df6b45d) = CONST 
    0x147: v147 = GT v142(0x4df6b45d), v1f
    0x148: v148(0x171) = CONST 
    0x14b: JUMPI v148(0x171), v147

    Begin block 0x171
    prev=[0x141], succ=[0x2e2c, 0x17d]
    =================================
    0x173: v173(0x42966c68) = CONST 
    0x178: v178 = EQ v173(0x42966c68), v1f
    0x2dec: v2dec(0x2e2c) = CONST 
    0x2ded: JUMPI v2dec(0x2e2c), v178

    Begin block 0x2e2c
    prev=[0x171], succ=[]
    =================================
    0x2e2d: v2e2d(0x4a5) = CONST 
    0x2e2e: CALLPRIVATE v2e2d(0x4a5)

    Begin block 0x17d
    prev=[0x171], succ=[0x188, 0x2e2f]
    =================================
    0x17e: v17e(0x43a468c8) = CONST 
    0x183: v183 = EQ v17e(0x43a468c8), v1f
    0x2dee: v2dee(0x2e2f) = CONST 
    0x2def: JUMPI v2dee(0x2e2f), v183

    Begin block 0x188
    prev=[0x17d], succ=[0x242f]
    =================================
    0x188: v188(0x242f) = CONST 
    0x18b: JUMP v188(0x242f)

    Begin block 0x242f
    prev=[0x188], succ=[]
    =================================
    0x2430: v2430(0x0) = CONST 
    0x2433: REVERT v2430(0x0), v2430(0x0)

    Begin block 0x2e2f
    prev=[0x17d], succ=[]
    =================================
    0x2e30: v2e30(0x4c2) = CONST 
    0x2e31: CALLPRIVATE v2e30(0x4c2)

    Begin block 0x14c
    prev=[0x141], succ=[0x2e32, 0x157]
    =================================
    0x14d: v14d(0x4df6b45d) = CONST 
    0x152: v152 = EQ v14d(0x4df6b45d), v1f
    0x2de6: v2de6(0x2e32) = CONST 
    0x2de7: JUMPI v2de6(0x2e32), v152

    Begin block 0x2e32
    prev=[0x14c], succ=[]
    =================================
    0x2e33: v2e33(0x4f5) = CONST 
    0x2e34: CALLPRIVATE v2e33(0x4f5)

    Begin block 0x157
    prev=[0x14c], succ=[0x2e35, 0x162]
    =================================
    0x158: v158(0x4e71e0c8) = CONST 
    0x15d: v15d = EQ v158(0x4e71e0c8), v1f
    0x2de8: v2de8(0x2e35) = CONST 
    0x2de9: JUMPI v2de8(0x2e35), v15d

    Begin block 0x2e35
    prev=[0x157], succ=[]
    =================================
    0x2e36: v2e36(0x53e) = CONST 
    0x2e37: CALLPRIVATE v2e36(0x53e)

    Begin block 0x162
    prev=[0x157], succ=[0x16d, 0x2e38]
    =================================
    0x163: v163(0x52006050) = CONST 
    0x168: v168 = EQ v163(0x52006050), v1f
    0x2dea: v2dea(0x2e38) = CONST 
    0x2deb: JUMPI v2dea(0x2e38), v168

    Begin block 0x16d
    prev=[0x162], succ=[0x240b]
    =================================
    0x16d: v16d(0x240b) = CONST 
    0x170: JUMP v16d(0x240b)

    Begin block 0x240b
    prev=[0x16d], succ=[]
    =================================
    0x240c: v240c(0x0) = CONST 
    0x240f: REVERT v240c(0x0), v240c(0x0)

    Begin block 0x2e38
    prev=[0x162], succ=[]
    =================================
    0x2e39: v2e39(0x546) = CONST 
    0x2e3a: CALLPRIVATE v2e39(0x546)

    Begin block 0x2b
    prev=[0x1a], succ=[0xbd, 0x36]
    =================================
    0x2c: v2c(0x95d89b41) = CONST 
    0x31: v31 = GT v2c(0x95d89b41), v1f
    0x32: v32(0xbd) = CONST 
    0x35: JUMPI v32(0xbd), v31

    Begin block 0xbd
    prev=[0x2b], succ=[0xf9, 0xc9]
    =================================
    0xbf: vbf(0x80749656) = CONST 
    0xc4: vc4 = GT vbf(0x80749656), v1f
    0xc5: vc5(0xf9) = CONST 
    0xc8: JUMPI vc5(0xf9), vc4

    Begin block 0xf9
    prev=[0xbd], succ=[0x2e1a, 0x105]
    =================================
    0xfb: vfb(0x554249b3) = CONST 
    0x100: v100 = EQ vfb(0x554249b3), v1f
    0x2dde: v2dde(0x2e1a) = CONST 
    0x2ddf: JUMPI v2dde(0x2e1a), v100

    Begin block 0x105
    prev=[0xf9], succ=[0x2e3b, 0x110]
    =================================
    0x106: v106(0x5c131d70) = CONST 
    0x10b: v10b = EQ v106(0x5c131d70), v1f
    0x2de0: v2de0(0x2e3b) = CONST 
    0x2de1: JUMPI v2de0(0x2e3b), v10b

    Begin block 0x2e3b
    prev=[0x105], succ=[]
    =================================
    0x2e3c: v2e3c(0x569) = CONST 
    0x2e3d: CALLPRIVATE v2e3c(0x569)

    Begin block 0x110
    prev=[0x105], succ=[0x2e3e, 0x11b]
    =================================
    0x111: v111(0x70a08231) = CONST 
    0x116: v116 = EQ v111(0x70a08231), v1f
    0x2de2: v2de2(0x2e3e) = CONST 
    0x2de3: JUMPI v2de2(0x2e3e), v116

    Begin block 0x2e3e
    prev=[0x110], succ=[]
    =================================
    0x2e3f: v2e3f(0x571) = CONST 
    0x2e40: CALLPRIVATE v2e3f(0x571)

    Begin block 0x11b
    prev=[0x110], succ=[0x126, 0x2e41]
    =================================
    0x11c: v11c(0x76e71dd8) = CONST 
    0x121: v121 = EQ v11c(0x76e71dd8), v1f
    0x2de4: v2de4(0x2e41) = CONST 
    0x2de5: JUMPI v2de4(0x2e41), v121

    Begin block 0x126
    prev=[0x11b], succ=[0x23e7]
    =================================
    0x126: v126(0x23e7) = CONST 
    0x129: JUMP v126(0x23e7)

    Begin block 0x23e7
    prev=[0x126], succ=[]
    =================================
    0x23e8: v23e8(0x0) = CONST 
    0x23eb: REVERT v23e8(0x0), v23e8(0x0)

    Begin block 0x2e41
    prev=[0x11b], succ=[]
    =================================
    0x2e42: v2e42(0x5a4) = CONST 
    0x2e43: CALLPRIVATE v2e42(0x5a4)

    Begin block 0xc9
    prev=[0xbd], succ=[0x2e44, 0xd4]
    =================================
    0xca: vca(0x80749656) = CONST 
    0xcf: vcf = EQ vca(0x80749656), v1f
    0x2dd6: v2dd6(0x2e44) = CONST 
    0x2dd7: JUMPI v2dd6(0x2e44), vcf

    Begin block 0x2e44
    prev=[0xc9], succ=[]
    =================================
    0x2e45: v2e45(0x5ac) = CONST 
    0x2e46: CALLPRIVATE v2e45(0x5ac)

    Begin block 0xd4
    prev=[0xc9], succ=[0x2e47, 0xdf]
    =================================
    0xd5: vd5(0x88ee39cc) = CONST 
    0xda: vda = EQ vd5(0x88ee39cc), v1f
    0x2dd8: v2dd8(0x2e47) = CONST 
    0x2dd9: JUMPI v2dd8(0x2e47), vda

    Begin block 0x2e47
    prev=[0xd4], succ=[]
    =================================
    0x2e48: v2e48(0x5e7) = CONST 
    0x2e49: CALLPRIVATE v2e48(0x5e7)

    Begin block 0xdf
    prev=[0xd4], succ=[0x2e4a, 0xea]
    =================================
    0xe0: ve0(0x8da5cb5b) = CONST 
    0xe5: ve5 = EQ ve0(0x8da5cb5b), v1f
    0x2dda: v2dda(0x2e4a) = CONST 
    0x2ddb: JUMPI v2dda(0x2e4a), ve5

    Begin block 0x2e4a
    prev=[0xdf], succ=[]
    =================================
    0x2e4b: v2e4b(0x622) = CONST 
    0x2e4c: CALLPRIVATE v2e4b(0x622)

    Begin block 0xea
    prev=[0xdf], succ=[0xf5, 0x2e1a]
    =================================
    0xeb: veb(0x93d3173a) = CONST 
    0xf0: vf0 = EQ veb(0x93d3173a), v1f
    0x2ddc: v2ddc(0x2e1a) = CONST 
    0x2ddd: JUMPI v2ddc(0x2e1a), vf0

    Begin block 0xf5
    prev=[0xea], succ=[0x23c3]
    =================================
    0xf5: vf5(0x23c3) = CONST 
    0xf8: JUMP vf5(0x23c3)

    Begin block 0x23c3
    prev=[0xf5], succ=[]
    =================================
    0x23c4: v23c4(0x0) = CONST 
    0x23c7: REVERT v23c4(0x0), v23c4(0x0)

    Begin block 0x36
    prev=[0x2b], succ=[0x8c, 0x41]
    =================================
    0x37: v37(0xa9059cbb) = CONST 
    0x3c: v3c = GT v37(0xa9059cbb), v1f
    0x3d: v3d(0x8c) = CONST 
    0x40: JUMPI v3d(0x8c), v3c

    Begin block 0x8c
    prev=[0x36], succ=[0x2e4d, 0x98]
    =================================
    0x8e: v8e(0x95d89b41) = CONST 
    0x93: v93 = EQ v8e(0x95d89b41), v1f
    0x2dce: v2dce(0x2e4d) = CONST 
    0x2dcf: JUMPI v2dce(0x2e4d), v93

    Begin block 0x2e4d
    prev=[0x8c], succ=[]
    =================================
    0x2e4e: v2e4e(0x653) = CONST 
    0x2e4f: CALLPRIVATE v2e4e(0x653)

    Begin block 0x98
    prev=[0x8c], succ=[0x2e50, 0xa3]
    =================================
    0x99: v99(0x9a6a30a4) = CONST 
    0x9e: v9e = EQ v99(0x9a6a30a4), v1f
    0x2dd0: v2dd0(0x2e50) = CONST 
    0x2dd1: JUMPI v2dd0(0x2e50), v9e

    Begin block 0x2e50
    prev=[0x98], succ=[]
    =================================
    0x2e51: v2e51(0x65b) = CONST 
    0x2e52: CALLPRIVATE v2e51(0x65b)

    Begin block 0xa3
    prev=[0x98], succ=[0x2e1a, 0xae]
    =================================
    0xa4: va4(0x9cd1a121) = CONST 
    0xa9: va9 = EQ va4(0x9cd1a121), v1f
    0x2dd2: v2dd2(0x2e1a) = CONST 
    0x2dd3: JUMPI v2dd2(0x2e1a), va9

    Begin block 0xae
    prev=[0xa3], succ=[0xb9, 0x2e53]
    =================================
    0xaf: vaf(0xa457c2d7) = CONST 
    0xb4: vb4 = EQ vaf(0xa457c2d7), v1f
    0x2dd4: v2dd4(0x2e53) = CONST 
    0x2dd5: JUMPI v2dd4(0x2e53), vb4

    Begin block 0xb9
    prev=[0xae], succ=[0x239f]
    =================================
    0xb9: vb9(0x239f) = CONST 
    0xbc: JUMP vb9(0x239f)

    Begin block 0x239f
    prev=[0xb9], succ=[]
    =================================
    0x23a0: v23a0(0x0) = CONST 
    0x23a3: REVERT v23a0(0x0), v23a0(0x0)

    Begin block 0x2e53
    prev=[0xae], succ=[]
    =================================
    0x2e54: v2e54(0x68e) = CONST 
    0x2e55: CALLPRIVATE v2e54(0x68e)

    Begin block 0x41
    prev=[0x36], succ=[0x71, 0x4c]
    =================================
    0x42: v42(0xdd62ed3e) = CONST 
    0x47: v47 = GT v42(0xdd62ed3e), v1f
    0x48: v48(0x71) = CONST 
    0x4b: JUMPI v48(0x71), v47

    Begin block 0x71
    prev=[0x41], succ=[0x2e56, 0x7d]
    =================================
    0x73: v73(0xa9059cbb) = CONST 
    0x78: v78 = EQ v73(0xa9059cbb), v1f
    0x2dca: v2dca(0x2e56) = CONST 
    0x2dcb: JUMPI v2dca(0x2e56), v78

    Begin block 0x2e56
    prev=[0x71], succ=[]
    =================================
    0x2e57: v2e57(0x6c7) = CONST 
    0x2e58: CALLPRIVATE v2e57(0x6c7)

    Begin block 0x7d
    prev=[0x71], succ=[0x88, 0x2e59]
    =================================
    0x7e: v7e(0xd01dd6d2) = CONST 
    0x83: v83 = EQ v7e(0xd01dd6d2), v1f
    0x2dcc: v2dcc(0x2e59) = CONST 
    0x2dcd: JUMPI v2dcc(0x2e59), v83

    Begin block 0x88
    prev=[0x7d], succ=[0x237b]
    =================================
    0x88: v88(0x237b) = CONST 
    0x8b: JUMP v88(0x237b)

    Begin block 0x237b
    prev=[0x88], succ=[]
    =================================
    0x237c: v237c(0x0) = CONST 
    0x237f: REVERT v237c(0x0), v237c(0x0)

    Begin block 0x2e59
    prev=[0x7d], succ=[]
    =================================
    0x2e5a: v2e5a(0x700) = CONST 
    0x2e5b: CALLPRIVATE v2e5a(0x700)

    Begin block 0x4c
    prev=[0x41], succ=[0x2e5c, 0x57]
    =================================
    0x4d: v4d(0xdd62ed3e) = CONST 
    0x52: v52 = EQ v4d(0xdd62ed3e), v1f
    0x2dc4: v2dc4(0x2e5c) = CONST 
    0x2dc5: JUMPI v2dc4(0x2e5c), v52

    Begin block 0x2e5c
    prev=[0x4c], succ=[]
    =================================
    0x2e5d: v2e5d(0x73b) = CONST 
    0x2e5e: CALLPRIVATE v2e5d(0x73b)

    Begin block 0x57
    prev=[0x4c], succ=[0x2e5f, 0x62]
    =================================
    0x58: v58(0xe30c3978) = CONST 
    0x5d: v5d = EQ v58(0xe30c3978), v1f
    0x2dc6: v2dc6(0x2e5f) = CONST 
    0x2dc7: JUMPI v2dc6(0x2e5f), v5d

    Begin block 0x2e5f
    prev=[0x57], succ=[]
    =================================
    0x2e60: v2e60(0x776) = CONST 
    0x2e61: CALLPRIVATE v2e60(0x776)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0x2e62]
    =================================
    0x63: v63(0xf2fde38b) = CONST 
    0x68: v68 = EQ v63(0xf2fde38b), v1f
    0x2dc8: v2dc8(0x2e62) = CONST 
    0x2dc9: JUMPI v2dc8(0x2e62), v68

    Begin block 0x6d
    prev=[0x62], succ=[0x2357]
    =================================
    0x6d: v6d(0x2357) = CONST 
    0x70: JUMP v6d(0x2357)

    Begin block 0x2357
    prev=[0x6d], succ=[]
    =================================
    0x2358: v2358(0x0) = CONST 
    0x235b: REVERT v2358(0x0), v2358(0x0)

    Begin block 0x2e62
    prev=[0x62], succ=[]
    =================================
    0x2e63: v2e63(0x77e) = CONST 
    0x2e64: CALLPRIVATE v2e63(0x77e)

    Begin block 0x2e65
    prev=[0x10], succ=[]
    =================================
    0x2e66: v2e66(0x2333) = CONST 
    0x2e67: CALLPRIVATE v2e66(0x2333)

}

function 0x13aa(0x13aaarg0x0, 0x13aaarg0x1, 0x13aaarg0x2, 0x13aaarg0x3) private {
    Begin block 0x13aa
    prev=[], succ=[0x13d9, 0x140f]
    =================================
    0x13ab: v13ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13c1: v13c1 = AND v13aaarg2, v13ab(0xffffffffffffffffffffffffffffffffffffffff)
    0x13c2: v13c2(0x0) = CONST 
    0x13c6: MSTORE v13c2(0x0), v13c1
    0x13c7: v13c7(0x16) = CONST 
    0x13c9: v13c9(0x20) = CONST 
    0x13cb: MSTORE v13c9(0x20), v13c7(0x16)
    0x13cc: v13cc(0x40) = CONST 
    0x13cf: v13cf = SHA3 v13c2(0x0), v13cc(0x40)
    0x13d0: v13d0 = SLOAD v13cf
    0x13d1: v13d1(0xff) = CONST 
    0x13d3: v13d3 = AND v13d1(0xff), v13d0
    0x13d4: v13d4 = ISZERO v13d3
    0x13d5: v13d5(0x140f) = CONST 
    0x13d8: JUMPI v13d5(0x140f), v13d4

    Begin block 0x13d9
    prev=[0x13aa], succ=[]
    =================================
    0x13d9: v13d9(0x40) = CONST 
    0x13db: v13db = MLOAD v13d9(0x40)
    0x13dc: v13dc(0x461bcd) = CONST 
    0x13e0: v13e0(0xe5) = CONST 
    0x13e2: v13e2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13e0(0xe5), v13dc(0x461bcd)
    0x13e4: MSTORE v13db, v13e2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13e5: v13e5(0x4) = CONST 
    0x13e7: v13e7 = ADD v13e5(0x4), v13db
    0x13ea: v13ea(0x20) = CONST 
    0x13ec: v13ec = ADD v13ea(0x20), v13e7
    0x13ef: v13ef(0x20) = SUB v13ec, v13e7
    0x13f1: MSTORE v13e7, v13ef(0x20)
    0x13f2: v13f2(0x29) = CONST 
    0x13f5: MSTORE v13ec, v13f2(0x29)
    0x13f6: v13f6(0x20) = CONST 
    0x13f8: v13f8 = ADD v13f6(0x20), v13ec
    0x13fa: v13fa(0x20a2) = CONST 
    0x13fd: v13fd(0x29) = CONST 
    0x1400: CODECOPY v13f8, v13fa(0x20a2), v13fd(0x29)
    0x1401: v1401(0x40) = CONST 
    0x1403: v1403 = ADD v1401(0x40), v13f8
    0x1407: v1407(0x40) = CONST 
    0x1409: v1409 = MLOAD v1407(0x40)
    0x140c: v140c(0x84) = SUB v1403, v1409
    0x140e: REVERT v1409, v140c(0x84)

    Begin block 0x140f
    prev=[0x13aa], succ=[0x1442, 0x143f]
    =================================
    0x1410: v1410(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1426: v1426 = AND v13aaarg1, v1410(0xffffffffffffffffffffffffffffffffffffffff)
    0x1427: v1427(0x0) = CONST 
    0x142b: MSTORE v1427(0x0), v1426
    0x142c: v142c(0x16) = CONST 
    0x142e: v142e(0x20) = CONST 
    0x1430: MSTORE v142e(0x20), v142c(0x16)
    0x1431: v1431(0x40) = CONST 
    0x1434: v1434 = SHA3 v1427(0x0), v1431(0x40)
    0x1435: v1435 = SLOAD v1434
    0x1436: v1436(0xff) = CONST 
    0x1438: v1438 = AND v1436(0xff), v1435
    0x1439: v1439 = ISZERO v1438
    0x143b: v143b(0x1442) = CONST 
    0x143e: JUMPI v143b(0x1442), v1439

    Begin block 0x1442
    prev=[0x140f, 0x143f], succ=[0x1447, 0x147d]
    =================================
    0x1442_0x0: v1442_0 = PHI v1439, v1441
    0x1443: v1443(0x147d) = CONST 
    0x1446: JUMPI v1443(0x147d), v1442_0

    Begin block 0x1447
    prev=[0x1442], succ=[]
    =================================
    0x1447: v1447(0x40) = CONST 
    0x1449: v1449 = MLOAD v1447(0x40)
    0x144a: v144a(0x461bcd) = CONST 
    0x144e: v144e(0xe5) = CONST 
    0x1450: v1450(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v144e(0xe5), v144a(0x461bcd)
    0x1452: MSTORE v1449, v1450(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1453: v1453(0x4) = CONST 
    0x1455: v1455 = ADD v1453(0x4), v1449
    0x1458: v1458(0x20) = CONST 
    0x145a: v145a = ADD v1458(0x20), v1455
    0x145d: v145d(0x20) = SUB v145a, v1455
    0x145f: MSTORE v1455, v145d(0x20)
    0x1460: v1460(0x2b) = CONST 
    0x1463: MSTORE v145a, v1460(0x2b)
    0x1464: v1464(0x20) = CONST 
    0x1466: v1466 = ADD v1464(0x20), v145a
    0x1468: v1468(0x1fbc) = CONST 
    0x146b: v146b(0x2b) = CONST 
    0x146e: CODECOPY v1466, v1468(0x1fbc), v146b(0x2b)
    0x146f: v146f(0x40) = CONST 
    0x1471: v1471 = ADD v146f(0x40), v1466
    0x1475: v1475(0x40) = CONST 
    0x1477: v1477 = MLOAD v1475(0x40)
    0x147a: v147a(0x84) = SUB v1471, v1477
    0x147c: REVERT v1477, v147a(0x84)

    Begin block 0x147d
    prev=[0x1442], succ=[0x17d5]
    =================================
    0x147e: v147e(0x2c08) = CONST 
    0x1484: v1484(0x17d5) = CONST 
    0x1487: JUMP v1484(0x17d5)

    Begin block 0x17d5
    prev=[0x147d], succ=[0x17f1, 0x1827]
    =================================
    0x17d6: v17d6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17ec: v17ec = AND v13aaarg2, v17d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x17ed: v17ed(0x1827) = CONST 
    0x17f0: JUMPI v17ed(0x1827), v17ec

    Begin block 0x17f1
    prev=[0x17d5], succ=[]
    =================================
    0x17f1: v17f1(0x40) = CONST 
    0x17f3: v17f3 = MLOAD v17f1(0x40)
    0x17f4: v17f4(0x461bcd) = CONST 
    0x17f8: v17f8(0xe5) = CONST 
    0x17fa: v17fa(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17f8(0xe5), v17f4(0x461bcd)
    0x17fc: MSTORE v17f3, v17fa(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17fd: v17fd(0x4) = CONST 
    0x17ff: v17ff = ADD v17fd(0x4), v17f3
    0x1802: v1802(0x20) = CONST 
    0x1804: v1804 = ADD v1802(0x20), v17ff
    0x1807: v1807(0x20) = SUB v1804, v17ff
    0x1809: MSTORE v17ff, v1807(0x20)
    0x180a: v180a(0x24) = CONST 
    0x180d: MSTORE v1804, v180a(0x24)
    0x180e: v180e(0x20) = CONST 
    0x1810: v1810 = ADD v180e(0x20), v1804
    0x1812: v1812(0x21ed) = CONST 
    0x1815: v1815(0x24) = CONST 
    0x1818: CODECOPY v1810, v1812(0x21ed), v1815(0x24)
    0x1819: v1819(0x40) = CONST 
    0x181b: v181b = ADD v1819(0x40), v1810
    0x181f: v181f(0x40) = CONST 
    0x1821: v1821 = MLOAD v181f(0x40)
    0x1824: v1824(0x84) = SUB v181b, v1821
    0x1826: REVERT v1821, v1824(0x84)

    Begin block 0x1827
    prev=[0x17d5], succ=[0x1843, 0x1879]
    =================================
    0x1828: v1828(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x183e: v183e = AND v13aaarg1, v1828(0xffffffffffffffffffffffffffffffffffffffff)
    0x183f: v183f(0x1879) = CONST 
    0x1842: JUMPI v183f(0x1879), v183e

    Begin block 0x1843
    prev=[0x1827], succ=[]
    =================================
    0x1843: v1843(0x40) = CONST 
    0x1845: v1845 = MLOAD v1843(0x40)
    0x1846: v1846(0x461bcd) = CONST 
    0x184a: v184a(0xe5) = CONST 
    0x184c: v184c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v184a(0xe5), v1846(0x461bcd)
    0x184e: MSTORE v1845, v184c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x184f: v184f(0x4) = CONST 
    0x1851: v1851 = ADD v184f(0x4), v1845
    0x1854: v1854(0x20) = CONST 
    0x1856: v1856 = ADD v1854(0x20), v1851
    0x1859: v1859(0x20) = SUB v1856, v1851
    0x185b: MSTORE v1851, v1859(0x20)
    0x185c: v185c(0x22) = CONST 
    0x185f: MSTORE v1856, v185c(0x22)
    0x1860: v1860(0x20) = CONST 
    0x1862: v1862 = ADD v1860(0x20), v1856
    0x1864: v1864(0x2036) = CONST 
    0x1867: v1867(0x22) = CONST 
    0x186a: CODECOPY v1862, v1864(0x2036), v1867(0x22)
    0x186b: v186b(0x40) = CONST 
    0x186d: v186d = ADD v186b(0x40), v1862
    0x1871: v1871(0x40) = CONST 
    0x1873: v1873 = MLOAD v1871(0x40)
    0x1876: v1876(0x84) = SUB v186d, v1873
    0x1878: REVERT v1873, v1876(0x84)

    Begin block 0x1879
    prev=[0x1827], succ=[0x2c08]
    =================================
    0x187a: v187a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1891: v1891 = AND v13aaarg2, v187a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1892: v1892(0x0) = CONST 
    0x1896: MSTORE v1892(0x0), v1891
    0x1897: v1897(0xf) = CONST 
    0x1899: v1899(0x20) = CONST 
    0x189d: MSTORE v1899(0x20), v1897(0xf)
    0x189e: v189e(0x40) = CONST 
    0x18a2: v18a2 = SHA3 v1892(0x0), v189e(0x40)
    0x18a5: v18a5 = AND v13aaarg1, v187a(0xffffffffffffffffffffffffffffffffffffffff)
    0x18a8: MSTORE v1892(0x0), v18a5
    0x18ab: MSTORE v1899(0x20), v18a2
    0x18af: v18af = SHA3 v1892(0x0), v189e(0x40)
    0x18b2: SSTORE v18af, v13aaarg0
    0x18b4: v18b4 = MLOAD v189e(0x40)
    0x18b7: MSTORE v18b4, v13aaarg0
    0x18b9: v18b9 = MLOAD v189e(0x40)
    0x18ba: v18ba(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x18de: v18de(0x0) = SUB v18b4, v18b9
    0x18e1: v18e1(0x20) = ADD v1899(0x20), v18de(0x0)
    0x18e3: LOG3 v18b9, v18e1(0x20), v18ba(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v1891, v18a5
    0x18e7: JUMP v147e(0x2c08)

    Begin block 0x2c08
    prev=[0x1879], succ=[]
    =================================
    0x2c0c: RETURNPRIVATE v13aaarg3

    Begin block 0x143f
    prev=[0x140f], succ=[0x1442]
    =================================
    0x1441: v1441 = ISZERO v13aaarg0

}

function 0x148d(0x148darg0x0, 0x148darg0x1, 0x148darg0x2, 0x148darg0x3) private {
    Begin block 0x148d
    prev=[], succ=[0x14ab]
    =================================
    0x148e: v148e(0x14ab) = CONST 
    0x1492: v1492(0x33091de8341533468d13a80c5a670f4f47cc649f) = CONST 
    0x14a7: v14a7(0x18e8) = CONST 
    0x14aa: CALLPRIVATE v14a7(0x18e8), v1492(0x33091de8341533468d13a80c5a670f4f47cc649f), v148darg1, v148e(0x14ab)

    Begin block 0x14ab
    prev=[0x148d], succ=[0x14c9]
    =================================
    0x14ac: v14ac(0x14c9) = CONST 
    0x14b0: v14b0(0x50e2719208914764087e68c32bc5aac321f5b04d) = CONST 
    0x14c5: v14c5(0x18e8) = CONST 
    0x14c8: CALLPRIVATE v14c5(0x18e8), v14b0(0x50e2719208914764087e68c32bc5aac321f5b04d), v148darg1, v14ac(0x14c9)

    Begin block 0x14c9
    prev=[0x14ab], succ=[0x14e7]
    =================================
    0x14ca: v14ca(0x14e7) = CONST 
    0x14ce: v14ce(0x71d69e5481a9b7be515e20b38a3f62dab7170d78) = CONST 
    0x14e3: v14e3(0x18e8) = CONST 
    0x14e6: CALLPRIVATE v14e3(0x18e8), v14ce(0x71d69e5481a9b7be515e20b38a3f62dab7170d78), v148darg1, v14ca(0x14e7)

    Begin block 0x14e7
    prev=[0x14c9], succ=[0x1505]
    =================================
    0x14e8: v14e8(0x1505) = CONST 
    0x14ec: v14ec(0x90fdaa85d52db6065d466b86f16bf840d514a488) = CONST 
    0x1501: v1501(0x18e8) = CONST 
    0x1504: CALLPRIVATE v1501(0x18e8), v14ec(0x90fdaa85d52db6065d466b86f16bf840d514a488), v148darg1, v14e8(0x1505)

    Begin block 0x1505
    prev=[0x14e7], succ=[0x19a7B0x1505]
    =================================
    0x1506: v1506(0x2c2c) = CONST 
    0x150c: v150c(0x19a7) = CONST 
    0x150f: JUMP v150c(0x19a7), v148darg0, v148darg1, v148darg2, v1506(0x2c2c)

    Begin block 0x19a7B0x1505
    prev=[0x1505], succ=[0x19d6B0x1505, 0x1a0cB0x1505]
    =================================
    0x19a8S0x1505: v19a8V1505(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19beS0x1505: v19beV1505 = AND v148darg2, v19a8V1505(0xffffffffffffffffffffffffffffffffffffffff)
    0x19bfS0x1505: v19bfV1505(0x0) = CONST 
    0x19c3S0x1505: MSTORE v19bfV1505(0x0), v19beV1505
    0x19c4S0x1505: v19c4V1505(0x16) = CONST 
    0x19c6S0x1505: v19c6V1505(0x20) = CONST 
    0x19c8S0x1505: MSTORE v19c6V1505(0x20), v19c4V1505(0x16)
    0x19c9S0x1505: v19c9V1505(0x40) = CONST 
    0x19ccS0x1505: v19ccV1505 = SHA3 v19bfV1505(0x0), v19c9V1505(0x40)
    0x19cdS0x1505: v19cdV1505 = SLOAD v19ccV1505
    0x19ceS0x1505: v19ceV1505(0xff) = CONST 
    0x19d0S0x1505: v19d0V1505 = AND v19ceV1505(0xff), v19cdV1505
    0x19d1S0x1505: v19d1V1505 = ISZERO v19d0V1505
    0x19d2S0x1505: v19d2V1505(0x1a0c) = CONST 
    0x19d5S0x1505: JUMPI v19d2V1505(0x1a0c), v19d1V1505

    Begin block 0x19d6B0x1505
    prev=[0x19a7B0x1505], succ=[]
    =================================
    0x19d6S0x1505: v19d6V1505(0x40) = CONST 
    0x19d8S0x1505: v19d8V1505 = MLOAD v19d6V1505(0x40)
    0x19d9S0x1505: v19d9V1505(0x461bcd) = CONST 
    0x19ddS0x1505: v19ddV1505(0xe5) = CONST 
    0x19dfS0x1505: v19dfV1505(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19ddV1505(0xe5), v19d9V1505(0x461bcd)
    0x19e1S0x1505: MSTORE v19d8V1505, v19dfV1505(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19e2S0x1505: v19e2V1505(0x4) = CONST 
    0x19e4S0x1505: v19e4V1505 = ADD v19e2V1505(0x4), v19d8V1505
    0x19e7S0x1505: v19e7V1505(0x20) = CONST 
    0x19e9S0x1505: v19e9V1505 = ADD v19e7V1505(0x20), v19e4V1505
    0x19ecS0x1505: v19ecV1505(0x20) = SUB v19e9V1505, v19e4V1505
    0x19eeS0x1505: MSTORE v19e4V1505, v19ecV1505(0x20)
    0x19efS0x1505: v19efV1505(0x23) = CONST 
    0x19f2S0x1505: MSTORE v19e9V1505, v19efV1505(0x23)
    0x19f3S0x1505: v19f3V1505(0x20) = CONST 
    0x19f5S0x1505: v19f5V1505 = ADD v19f3V1505(0x20), v19e9V1505
    0x19f7S0x1505: v19f7V1505(0x2211) = CONST 
    0x19faS0x1505: v19faV1505(0x23) = CONST 
    0x19fdS0x1505: CODECOPY v19f5V1505, v19f7V1505(0x2211), v19faV1505(0x23)
    0x19feS0x1505: v19feV1505(0x40) = CONST 
    0x1a00S0x1505: v1a00V1505 = ADD v19feV1505(0x40), v19f5V1505
    0x1a04S0x1505: v1a04V1505(0x40) = CONST 
    0x1a06S0x1505: v1a06V1505 = MLOAD v1a04V1505(0x40)
    0x1a09S0x1505: v1a09V1505(0x84) = SUB v1a00V1505, v1a06V1505
    0x1a0bS0x1505: REVERT v1a06V1505, v1a09V1505(0x84)

    Begin block 0x1a0cB0x1505
    prev=[0x19a7B0x1505], succ=[0x1a3bB0x1505, 0x1a71B0x1505]
    =================================
    0x1a0dS0x1505: v1a0dV1505(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a23S0x1505: v1a23V1505 = AND v148darg1, v1a0dV1505(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a24S0x1505: v1a24V1505(0x0) = CONST 
    0x1a28S0x1505: MSTORE v1a24V1505(0x0), v1a23V1505
    0x1a29S0x1505: v1a29V1505(0x16) = CONST 
    0x1a2bS0x1505: v1a2bV1505(0x20) = CONST 
    0x1a2dS0x1505: MSTORE v1a2bV1505(0x20), v1a29V1505(0x16)
    0x1a2eS0x1505: v1a2eV1505(0x40) = CONST 
    0x1a31S0x1505: v1a31V1505 = SHA3 v1a24V1505(0x0), v1a2eV1505(0x40)
    0x1a32S0x1505: v1a32V1505 = SLOAD v1a31V1505
    0x1a33S0x1505: v1a33V1505(0xff) = CONST 
    0x1a35S0x1505: v1a35V1505 = AND v1a33V1505(0xff), v1a32V1505
    0x1a36S0x1505: v1a36V1505 = ISZERO v1a35V1505
    0x1a37S0x1505: v1a37V1505(0x1a71) = CONST 
    0x1a3aS0x1505: JUMPI v1a37V1505(0x1a71), v1a36V1505

    Begin block 0x1a3bB0x1505
    prev=[0x1a0cB0x1505], succ=[]
    =================================
    0x1a3bS0x1505: v1a3bV1505(0x40) = CONST 
    0x1a3dS0x1505: v1a3dV1505 = MLOAD v1a3bV1505(0x40)
    0x1a3eS0x1505: v1a3eV1505(0x461bcd) = CONST 
    0x1a42S0x1505: v1a42V1505(0xe5) = CONST 
    0x1a44S0x1505: v1a44V1505(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1a42V1505(0xe5), v1a3eV1505(0x461bcd)
    0x1a46S0x1505: MSTORE v1a3dV1505, v1a44V1505(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a47S0x1505: v1a47V1505(0x4) = CONST 
    0x1a49S0x1505: v1a49V1505 = ADD v1a47V1505(0x4), v1a3dV1505
    0x1a4cS0x1505: v1a4cV1505(0x20) = CONST 
    0x1a4eS0x1505: v1a4eV1505 = ADD v1a4cV1505(0x20), v1a49V1505
    0x1a51S0x1505: v1a51V1505(0x20) = SUB v1a4eV1505, v1a49V1505
    0x1a53S0x1505: MSTORE v1a49V1505, v1a51V1505(0x20)
    0x1a54S0x1505: v1a54V1505(0x26) = CONST 
    0x1a57S0x1505: MSTORE v1a4eV1505, v1a54V1505(0x26)
    0x1a58S0x1505: v1a58V1505(0x20) = CONST 
    0x1a5aS0x1505: v1a5aV1505 = ADD v1a58V1505(0x20), v1a4eV1505
    0x1a5cS0x1505: v1a5cV1505(0x20cb) = CONST 
    0x1a5fS0x1505: v1a5fV1505(0x26) = CONST 
    0x1a62S0x1505: CODECOPY v1a5aV1505, v1a5cV1505(0x20cb), v1a5fV1505(0x26)
    0x1a63S0x1505: v1a63V1505(0x40) = CONST 
    0x1a65S0x1505: v1a65V1505 = ADD v1a63V1505(0x40), v1a5aV1505
    0x1a69S0x1505: v1a69V1505(0x40) = CONST 
    0x1a6bS0x1505: v1a6bV1505 = MLOAD v1a69V1505(0x40)
    0x1a6eS0x1505: v1a6eV1505(0x84) = SUB v1a65V1505, v1a6bV1505
    0x1a70S0x1505: REVERT v1a6bV1505, v1a6eV1505(0x84)

    Begin block 0x1a71B0x1505
    prev=[0x1a0cB0x1505], succ=[0x1a7aB0x1505]
    =================================
    0x1a72S0x1505: v1a72V1505(0x1a7a) = CONST 
    0x1a76S0x1505: v1a76V1505(0x1601) = CONST 
    0x1a79S0x1505: v1a79_0V1505 = CALLPRIVATE v1a76V1505(0x1601), v148darg1, v1a72V1505(0x1a7a)

    Begin block 0x1a7aB0x1505
    prev=[0x1a71B0x1505], succ=[0x1a80B0x1505, 0x1ae5B0x1505]
    =================================
    0x1a7bS0x1505: v1a7bV1505 = ISZERO v1a79_0V1505
    0x1a7cS0x1505: v1a7cV1505(0x1ae5) = CONST 
    0x1a7fS0x1505: JUMPI v1a7cV1505(0x1ae5), v1a7bV1505

    Begin block 0x1a80B0x1505
    prev=[0x1a7aB0x1505], succ=[0x1a9eB0x1505]
    =================================
    0x1a80S0x1505: v1a80V1505(0x1ab0) = CONST 
    0x1a85S0x1505: v1a85V1505(0x1aab) = CONST 
    0x1a88S0x1505: v1a88V1505(0x1a9e) = CONST 
    0x1a8cS0x1505: v1a8cV1505(0x2386f26fc10000) = CONST 
    0x1a94S0x1505: v1a94V1505(0xffffffff) = CONST 
    0x1a99S0x1505: v1a99V1505(0x1bcc) = CONST 
    0x1a9cS0x1505: v1a9cV1505(0x1bcc) = AND v1a99V1505(0x1bcc), v1a94V1505(0xffffffff)
    0x1a9dS0x1505: v1a9d_0V1505 = CALLPRIVATE v1a9cV1505(0x1bcc), v1a8cV1505(0x2386f26fc10000), v148darg0, v1a88V1505(0x1a9e)

    Begin block 0x1a9eB0x1505
    prev=[0x1a80B0x1505], succ=[0x1c0eB0x1a9eB0x1505]
    =================================
    0x1aa1S0x1505: v1aa1V1505(0xffffffff) = CONST 
    0x1aa6S0x1505: v1aa6V1505(0x1c0e) = CONST 
    0x1aa9S0x1505: v1aa9V1505(0x1c0e) = AND v1aa6V1505(0x1c0e), v1aa1V1505(0xffffffff)
    0x1aaaS0x1505: JUMP v1aa9V1505(0x1c0e)

    Begin block 0x1c0eB0x1a9eB0x1505
    prev=[0x1a9eB0x1505], succ=[0x2d73B0x1a9eB0x1505]
    =================================
    0x1c0fS0x1a9eS0x1505: v1c0fV1a9eV1505(0x0) = CONST 
    0x1c11S0x1a9eS0x1505: v1c11V1a9eV1505(0x2d73) = CONST 
    0x1c16S0x1a9eS0x1505: v1c16V1a9eV1505(0x40) = CONST 
    0x1c18S0x1a9eS0x1505: v1c18V1a9eV1505 = MLOAD v1c16V1a9eV1505(0x40)
    0x1c1aS0x1a9eS0x1505: v1c1aV1a9eV1505(0x40) = CONST 
    0x1c1cS0x1a9eS0x1505: v1c1cV1a9eV1505 = ADD v1c1aV1a9eV1505(0x40), v1c18V1a9eV1505
    0x1c1dS0x1a9eS0x1505: v1c1dV1a9eV1505(0x40) = CONST 
    0x1c1fS0x1a9eS0x1505: MSTORE v1c1dV1a9eV1505(0x40), v1c1cV1a9eV1505
    0x1c21S0x1a9eS0x1505: v1c21V1a9eV1505(0x1e) = CONST 
    0x1c24S0x1a9eS0x1505: MSTORE v1c18V1a9eV1505, v1c21V1a9eV1505(0x1e)
    0x1c25S0x1a9eS0x1505: v1c25V1a9eV1505(0x20) = CONST 
    0x1c27S0x1a9eS0x1505: v1c27V1a9eV1505 = ADD v1c25V1a9eV1505(0x20), v1c18V1a9eV1505
    0x1c28S0x1a9eS0x1505: v1c28V1a9eV1505(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x1c4aS0x1a9eS0x1505: MSTORE v1c27V1a9eV1505, v1c28V1a9eV1505(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1c4cS0x1a9eS0x1505: v1c4cV1a9eV1505(0x1510) = CONST 
    0x1c4fS0x1a9eS0x1505: v1c4f_0V1a9eV1505 = CALLPRIVATE v1c4cV1a9eV1505(0x1510), v1c18V1a9eV1505, v1a9d_0V1505, v148darg0, v1c11V1a9eV1505(0x2d73)

    Begin block 0x2d73B0x1a9eB0x1505
    prev=[0x1c0eB0x1a9eB0x1505], succ=[0x1aabB0x1505]
    =================================
    0x2d79S0x1a9eS0x1505: JUMP v1a85V1505(0x1aab)

    Begin block 0x1aabB0x1505
    prev=[0x2d73B0x1a9eB0x1505], succ=[0x1ab0B0x1505]
    =================================
    0x1aacS0x1505: v1aacV1505(0x1c50) = CONST 
    0x1aafS0x1505: CALLPRIVATE v1aacV1505(0x1c50), v1c4f_0V1a9eV1505, v148darg1, v148darg2, v1a80V1505(0x1ab0)

    Begin block 0x1ab0B0x1505
    prev=[0x1aabB0x1505], succ=[0x1aceB0x1505]
    =================================
    0x1ab1S0x1505: v1ab1V1505(0x1ae0) = CONST 
    0x1ab5S0x1505: v1ab5V1505(0x1adb) = CONST 
    0x1ab8S0x1505: v1ab8V1505(0x1ace) = CONST 
    0x1abcS0x1505: v1abcV1505(0x2386f26fc10000) = CONST 
    0x1ac4S0x1505: v1ac4V1505(0xffffffff) = CONST 
    0x1ac9S0x1505: v1ac9V1505(0x1bcc) = CONST 
    0x1accS0x1505: v1accV1505(0x1bcc) = AND v1ac9V1505(0x1bcc), v1ac4V1505(0xffffffff)
    0x1acdS0x1505: v1acd_0V1505 = CALLPRIVATE v1accV1505(0x1bcc), v1abcV1505(0x2386f26fc10000), v148darg0, v1ab8V1505(0x1ace)

    Begin block 0x1aceB0x1505
    prev=[0x1ab0B0x1505], succ=[0x1c0eB0x1aceB0x1505]
    =================================
    0x1ad1S0x1505: v1ad1V1505(0xffffffff) = CONST 
    0x1ad6S0x1505: v1ad6V1505(0x1c0e) = CONST 
    0x1ad9S0x1505: v1ad9V1505(0x1c0e) = AND v1ad6V1505(0x1c0e), v1ad1V1505(0xffffffff)
    0x1adaS0x1505: JUMP v1ad9V1505(0x1c0e)

    Begin block 0x1c0eB0x1aceB0x1505
    prev=[0x1aceB0x1505], succ=[0x2d73B0x1aceB0x1505]
    =================================
    0x1c0fS0x1aceS0x1505: v1c0fV1aceV1505(0x0) = CONST 
    0x1c11S0x1aceS0x1505: v1c11V1aceV1505(0x2d73) = CONST 
    0x1c16S0x1aceS0x1505: v1c16V1aceV1505(0x40) = CONST 
    0x1c18S0x1aceS0x1505: v1c18V1aceV1505 = MLOAD v1c16V1aceV1505(0x40)
    0x1c1aS0x1aceS0x1505: v1c1aV1aceV1505(0x40) = CONST 
    0x1c1cS0x1aceS0x1505: v1c1cV1aceV1505 = ADD v1c1aV1aceV1505(0x40), v1c18V1aceV1505
    0x1c1dS0x1aceS0x1505: v1c1dV1aceV1505(0x40) = CONST 
    0x1c1fS0x1aceS0x1505: MSTORE v1c1dV1aceV1505(0x40), v1c1cV1aceV1505
    0x1c21S0x1aceS0x1505: v1c21V1aceV1505(0x1e) = CONST 
    0x1c24S0x1aceS0x1505: MSTORE v1c18V1aceV1505, v1c21V1aceV1505(0x1e)
    0x1c25S0x1aceS0x1505: v1c25V1aceV1505(0x20) = CONST 
    0x1c27S0x1aceS0x1505: v1c27V1aceV1505 = ADD v1c25V1aceV1505(0x20), v1c18V1aceV1505
    0x1c28S0x1aceS0x1505: v1c28V1aceV1505(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x1c4aS0x1aceS0x1505: MSTORE v1c27V1aceV1505, v1c28V1aceV1505(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1c4cS0x1aceS0x1505: v1c4cV1aceV1505(0x1510) = CONST 
    0x1c4fS0x1aceS0x1505: v1c4f_0V1aceV1505 = CALLPRIVATE v1c4cV1aceV1505(0x1510), v1c18V1aceV1505, v1acd_0V1505, v148darg0, v1c11V1aceV1505(0x2d73)

    Begin block 0x2d73B0x1aceB0x1505
    prev=[0x1c0eB0x1aceB0x1505], succ=[0x1adbB0x1505]
    =================================
    0x2d79S0x1aceS0x1505: JUMP v1ab5V1505(0x1adb)

    Begin block 0x1adbB0x1505
    prev=[0x2d73B0x1aceB0x1505], succ=[0x1ae0B0x1505]
    =================================
    0x1adcS0x1505: v1adcV1505(0x1767) = CONST 
    0x1adfS0x1505: CALLPRIVATE v1adcV1505(0x1767), v1c4f_0V1aceV1505, v148darg1, v1ab1V1505(0x1ae0)

    Begin block 0x1ae0B0x1505
    prev=[0x1adbB0x1505], succ=[0x2d05B0x1505]
    =================================
    0x1ae1S0x1505: v1ae1V1505(0x2d05) = CONST 
    0x1ae4S0x1505: JUMP v1ae1V1505(0x2d05)

    Begin block 0x2d05B0x1505
    prev=[0x1ae0B0x1505], succ=[0x2c2c]
    =================================
    0x2d09S0x1505: JUMP v1506(0x2c2c)

    Begin block 0x2c2c
    prev=[0x2d05B0x1505, 0x2d29B0x1505], succ=[]
    =================================
    0x2c30: RETURNPRIVATE v148darg3

    Begin block 0x1ae5B0x1505
    prev=[0x1a7aB0x1505], succ=[0x2d29B0x1505]
    =================================
    0x1ae6S0x1505: v1ae6V1505(0x2d29) = CONST 
    0x1aecS0x1505: v1aecV1505(0x1c50) = CONST 
    0x1aefS0x1505: CALLPRIVATE v1aecV1505(0x1c50), v148darg0, v148darg1, v148darg2, v1ae6V1505(0x2d29)

    Begin block 0x2d29B0x1505
    prev=[0x1ae5B0x1505], succ=[0x2c2c]
    =================================
    0x2d2dS0x1505: JUMP v1506(0x2c2c)

}

function 0x1510(0x1510arg0x0, 0x1510arg0x1, 0x1510arg0x2, 0x1510arg0x3) private {
    Begin block 0x1510
    prev=[], succ=[0x151c, 0x159f]
    =================================
    0x1511: v1511(0x0) = CONST 
    0x1516: v1516 = GT v1510arg1, v1510arg2
    0x1517: v1517 = ISZERO v1516
    0x1518: v1518(0x159f) = CONST 
    0x151b: JUMPI v1518(0x159f), v1517

    Begin block 0x151c
    prev=[0x1510], succ=[0x154c0x1510]
    =================================
    0x151c: v151c(0x40) = CONST 
    0x151e: v151e = MLOAD v151c(0x40)
    0x151f: v151f(0x461bcd) = CONST 
    0x1523: v1523(0xe5) = CONST 
    0x1525: v1525(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1523(0xe5), v151f(0x461bcd)
    0x1527: MSTORE v151e, v1525(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1528: v1528(0x4) = CONST 
    0x152a: v152a = ADD v1528(0x4), v151e
    0x152d: v152d(0x20) = CONST 
    0x152f: v152f = ADD v152d(0x20), v152a
    0x1532: v1532(0x20) = SUB v152f, v152a
    0x1534: MSTORE v152a, v1532(0x20)
    0x1538: v1538 = MLOAD v1510arg0
    0x153a: MSTORE v152f, v1538
    0x153b: v153b(0x20) = CONST 
    0x153d: v153d = ADD v153b(0x20), v152f
    0x1541: v1541 = MLOAD v1510arg0
    0x1543: v1543(0x20) = CONST 
    0x1545: v1545 = ADD v1543(0x20), v1510arg0
    0x154a: v154a(0x0) = CONST 

    Begin block 0x154c0x1510
    prev=[0x151c, 0x15550x1510], succ=[0x15640x1510, 0x15550x1510]
    =================================
    0x154c0x1510_0x0: v154c1510_0 = PHI v154a(0x0), v1510155f
    0x154f0x1510: v1510154f = LT v154c1510_0, v1541
    0x15500x1510: v15101550 = ISZERO v1510154f
    0x15510x1510: v15101551(0x1564) = CONST 
    0x15540x1510: JUMPI v15101551(0x1564), v15101550

    Begin block 0x15640x1510
    prev=[0x154c0x1510], succ=[0x15910x1510, 0x15780x1510]
    =================================
    0x156d0x1510: v1510156d = ADD v1541, v153d
    0x156f0x1510: v1510156f(0x1f) = CONST 
    0x15710x1510: v15101571 = AND v1510156f(0x1f), v1541
    0x15730x1510: v15101573 = ISZERO v15101571
    0x15740x1510: v15101574(0x1591) = CONST 
    0x15770x1510: JUMPI v15101574(0x1591), v15101573

    Begin block 0x15910x1510
    prev=[0x15640x1510, 0x15780x1510], succ=[]
    =================================
    0x15910x1510_0x1: v15911510_1 = PHI v1510158e, v1510156d
    0x15970x1510: v15101597(0x40) = CONST 
    0x15990x1510: v15101599 = MLOAD v15101597(0x40)
    0x159c0x1510: v1510159c = SUB v15911510_1, v15101599
    0x159e0x1510: REVERT v15101599, v1510159c

    Begin block 0x15780x1510
    prev=[0x15640x1510], succ=[0x15910x1510]
    =================================
    0x157a0x1510: v1510157a = SUB v1510156d, v15101571
    0x157c0x1510: v1510157c = MLOAD v1510157a
    0x157d0x1510: v1510157d(0x1) = CONST 
    0x15800x1510: v15101580(0x20) = CONST 
    0x15820x1510: v15101582 = SUB v15101580(0x20), v15101571
    0x15830x1510: v15101583(0x100) = CONST 
    0x15860x1510: v15101586 = EXP v15101583(0x100), v15101582
    0x15870x1510: v15101587 = SUB v15101586, v1510157d(0x1)
    0x15880x1510: v15101588 = NOT v15101587
    0x15890x1510: v15101589 = AND v15101588, v1510157c
    0x158b0x1510: MSTORE v1510157a, v15101589
    0x158c0x1510: v1510158c(0x20) = CONST 
    0x158e0x1510: v1510158e = ADD v1510158c(0x20), v1510157a

    Begin block 0x15550x1510
    prev=[0x154c0x1510], succ=[0x154c0x1510]
    =================================
    0x15550x1510_0x0: v15551510_0 = PHI v154a(0x0), v1510155f
    0x15570x1510: v15101557 = ADD v15551510_0, v1545
    0x15580x1510: v15101558 = MLOAD v15101557
    0x155b0x1510: v1510155b = ADD v15551510_0, v153d
    0x155c0x1510: MSTORE v1510155b, v15101558
    0x155d0x1510: v1510155d(0x20) = CONST 
    0x155f0x1510: v1510155f = ADD v1510155d(0x20), v15551510_0
    0x15600x1510: v15101560(0x154c) = CONST 
    0x15630x1510: JUMP v15101560(0x154c)

    Begin block 0x159f
    prev=[0x1510], succ=[]
    =================================
    0x15a4: v15a4 = SUB v1510arg2, v1510arg1
    0x15a6: RETURNPRIVATE v1510arg3, v15a4

}

function 0x1601(0x1601arg0x0, 0x1601arg0x1) private {
    Begin block 0x1601
    prev=[], succ=[0x2c76, 0x1626]
    =================================
    0x1602: v1602(0x0) = CONST 
    0x1604: v1604(0x100000) = CONST 
    0x1609: v1609(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x161e: v161e = AND v1609(0xffffffffffffffffffffffffffffffffffffffff), v1601arg0
    0x161f: v161f = LT v161e, v1604(0x100000)
    0x1621: v1621 = ISZERO v161f
    0x1622: v1622(0x2c76) = CONST 
    0x1625: JUMPI v1622(0x2c76), v1621

    Begin block 0x2c76
    prev=[0x1601], succ=[]
    =================================
    0x2c7b: RETURNPRIVATE v1601arg1, v161f

    Begin block 0x1626
    prev=[0x1601], succ=[]
    =================================
    0x1628: v1628(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x163d: v163d = AND v1628(0xffffffffffffffffffffffffffffffffffffffff), v1601arg0
    0x163e: v163e = ISZERO v163d
    0x163f: v163f = ISZERO v163e
    0x1641: RETURNPRIVATE v1601arg1, v163f

}

function 0x1767(0x1767arg0x0, 0x1767arg0x1, 0x1767arg0x2) private {
    Begin block 0x1767
    prev=[], succ=[0x1795, 0x17cb]
    =================================
    0x1768: v1768(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x177e: v177e = AND v1767arg1, v1768(0xffffffffffffffffffffffffffffffffffffffff)
    0x177f: v177f(0x0) = CONST 
    0x1783: MSTORE v177f(0x0), v177e
    0x1784: v1784(0x17) = CONST 
    0x1786: v1786(0x20) = CONST 
    0x1788: MSTORE v1786(0x20), v1784(0x17)
    0x1789: v1789(0x40) = CONST 
    0x178c: v178c = SHA3 v177f(0x0), v1789(0x40)
    0x178d: v178d = SLOAD v178c
    0x178e: v178e(0xff) = CONST 
    0x1790: v1790 = AND v178e(0xff), v178d
    0x1791: v1791(0x17cb) = CONST 
    0x1794: JUMPI v1791(0x17cb), v1790

    Begin block 0x1795
    prev=[0x1767], succ=[]
    =================================
    0x1795: v1795(0x40) = CONST 
    0x1797: v1797 = MLOAD v1795(0x40)
    0x1798: v1798(0x461bcd) = CONST 
    0x179c: v179c(0xe5) = CONST 
    0x179e: v179e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v179c(0xe5), v1798(0x461bcd)
    0x17a0: MSTORE v1797, v179e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17a1: v17a1(0x4) = CONST 
    0x17a3: v17a3 = ADD v17a1(0x4), v1797
    0x17a6: v17a6(0x20) = CONST 
    0x17a8: v17a8 = ADD v17a6(0x20), v17a3
    0x17ab: v17ab(0x20) = SUB v17a8, v17a3
    0x17ad: MSTORE v17a3, v17ab(0x20)
    0x17ae: v17ae(0x2b) = CONST 
    0x17b1: MSTORE v17a8, v17ae(0x2b)
    0x17b2: v17b2(0x20) = CONST 
    0x17b4: v17b4 = ADD v17b2(0x20), v17a8
    0x17b6: v17b6(0x2260) = CONST 
    0x17b9: v17b9(0x2b) = CONST 
    0x17bc: CODECOPY v17b4, v17b6(0x2260), v17b9(0x2b)
    0x17bd: v17bd(0x40) = CONST 
    0x17bf: v17bf = ADD v17bd(0x40), v17b4
    0x17c3: v17c3(0x40) = CONST 
    0x17c5: v17c5 = MLOAD v17c3(0x40)
    0x17c8: v17c8(0x84) = SUB v17bf, v17c5
    0x17ca: REVERT v17c5, v17c8(0x84)

    Begin block 0x17cb
    prev=[0x1767], succ=[0x1af0]
    =================================
    0x17cc: v17cc(0x2cbf) = CONST 
    0x17d1: v17d1(0x1af0) = CONST 
    0x17d4: JUMP v17d1(0x1af0)

    Begin block 0x1af0
    prev=[0x17cb], succ=[0x1afb, 0x1b31]
    =================================
    0x1af1: v1af1(0x6) = CONST 
    0x1af3: v1af3 = SLOAD v1af1(0x6)
    0x1af5: v1af5 = LT v1767arg0, v1af3
    0x1af6: v1af6 = ISZERO v1af5
    0x1af7: v1af7(0x1b31) = CONST 
    0x1afa: JUMPI v1af7(0x1b31), v1af6

    Begin block 0x1afb
    prev=[0x1af0], succ=[]
    =================================
    0x1afb: v1afb(0x40) = CONST 
    0x1afd: v1afd = MLOAD v1afb(0x40)
    0x1afe: v1afe(0x461bcd) = CONST 
    0x1b02: v1b02(0xe5) = CONST 
    0x1b04: v1b04(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b02(0xe5), v1afe(0x461bcd)
    0x1b06: MSTORE v1afd, v1b04(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b07: v1b07(0x4) = CONST 
    0x1b09: v1b09 = ADD v1b07(0x4), v1afd
    0x1b0c: v1b0c(0x20) = CONST 
    0x1b0e: v1b0e = ADD v1b0c(0x20), v1b09
    0x1b11: v1b11(0x20) = SUB v1b0e, v1b09
    0x1b13: MSTORE v1b09, v1b11(0x20)
    0x1b14: v1b14(0x2d) = CONST 
    0x1b17: MSTORE v1b0e, v1b14(0x2d)
    0x1b18: v1b18(0x20) = CONST 
    0x1b1a: v1b1a = ADD v1b18(0x20), v1b0e
    0x1b1c: v1b1c(0x1fe7) = CONST 
    0x1b1f: v1b1f(0x2d) = CONST 
    0x1b22: CODECOPY v1b1a, v1b1c(0x1fe7), v1b1f(0x2d)
    0x1b23: v1b23(0x40) = CONST 
    0x1b25: v1b25 = ADD v1b23(0x40), v1b1a
    0x1b29: v1b29(0x40) = CONST 
    0x1b2b: v1b2b = MLOAD v1b29(0x40)
    0x1b2e: v1b2e(0x84) = SUB v1b25, v1b2b
    0x1b30: REVERT v1b2b, v1b2e(0x84)

    Begin block 0x1b31
    prev=[0x1af0], succ=[0x1b3c, 0x1b72]
    =================================
    0x1b32: v1b32(0x7) = CONST 
    0x1b34: v1b34 = SLOAD v1b32(0x7)
    0x1b36: v1b36 = GT v1767arg0, v1b34
    0x1b37: v1b37 = ISZERO v1b36
    0x1b38: v1b38(0x1b72) = CONST 
    0x1b3b: JUMPI v1b38(0x1b72), v1b37

    Begin block 0x1b3c
    prev=[0x1b31], succ=[]
    =================================
    0x1b3c: v1b3c(0x40) = CONST 
    0x1b3e: v1b3e = MLOAD v1b3c(0x40)
    0x1b3f: v1b3f(0x461bcd) = CONST 
    0x1b43: v1b43(0xe5) = CONST 
    0x1b45: v1b45(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b43(0xe5), v1b3f(0x461bcd)
    0x1b47: MSTORE v1b3e, v1b45(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b48: v1b48(0x4) = CONST 
    0x1b4a: v1b4a = ADD v1b48(0x4), v1b3e
    0x1b4d: v1b4d(0x20) = CONST 
    0x1b4f: v1b4f = ADD v1b4d(0x20), v1b4a
    0x1b52: v1b52(0x20) = SUB v1b4f, v1b4a
    0x1b54: MSTORE v1b4a, v1b52(0x20)
    0x1b55: v1b55(0x2f) = CONST 
    0x1b58: MSTORE v1b4f, v1b55(0x2f)
    0x1b59: v1b59(0x20) = CONST 
    0x1b5b: v1b5b = ADD v1b59(0x20), v1b4f
    0x1b5d: v1b5d(0x22b0) = CONST 
    0x1b60: v1b60(0x2f) = CONST 
    0x1b63: CODECOPY v1b5b, v1b5d(0x22b0), v1b60(0x2f)
    0x1b64: v1b64(0x40) = CONST 
    0x1b66: v1b66 = ADD v1b64(0x40), v1b5b
    0x1b6a: v1b6a(0x40) = CONST 
    0x1b6c: v1b6c = MLOAD v1b6a(0x40)
    0x1b6f: v1b6f(0x84) = SUB v1b66, v1b6c
    0x1b71: REVERT v1b6c, v1b6f(0x84)

    Begin block 0x1b72
    prev=[0x1b31], succ=[0x1dfa]
    =================================
    0x1b73: v1b73(0x1b7c) = CONST 
    0x1b78: v1b78(0x1dfa) = CONST 
    0x1b7b: JUMP v1b78(0x1dfa)

    Begin block 0x1dfa
    prev=[0x1b72], succ=[0x1e16, 0x1e4c]
    =================================
    0x1dfb: v1dfb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e11: v1e11 = AND v1767arg1, v1dfb(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e12: v1e12(0x1e4c) = CONST 
    0x1e15: JUMPI v1e12(0x1e4c), v1e11

    Begin block 0x1e16
    prev=[0x1dfa], succ=[]
    =================================
    0x1e16: v1e16(0x40) = CONST 
    0x1e18: v1e18 = MLOAD v1e16(0x40)
    0x1e19: v1e19(0x461bcd) = CONST 
    0x1e1d: v1e1d(0xe5) = CONST 
    0x1e1f: v1e1f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e1d(0xe5), v1e19(0x461bcd)
    0x1e21: MSTORE v1e18, v1e1f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e22: v1e22(0x4) = CONST 
    0x1e24: v1e24 = ADD v1e22(0x4), v1e18
    0x1e27: v1e27(0x20) = CONST 
    0x1e29: v1e29 = ADD v1e27(0x20), v1e24
    0x1e2c: v1e2c(0x20) = SUB v1e29, v1e24
    0x1e2e: MSTORE v1e24, v1e2c(0x20)
    0x1e2f: v1e2f(0x21) = CONST 
    0x1e32: MSTORE v1e29, v1e2f(0x21)
    0x1e33: v1e33(0x20) = CONST 
    0x1e35: v1e35 = ADD v1e33(0x20), v1e29
    0x1e37: v1e37(0x21a7) = CONST 
    0x1e3a: v1e3a(0x21) = CONST 
    0x1e3d: CODECOPY v1e35, v1e37(0x21a7), v1e3a(0x21)
    0x1e3e: v1e3e(0x40) = CONST 
    0x1e40: v1e40 = ADD v1e3e(0x40), v1e35
    0x1e44: v1e44(0x40) = CONST 
    0x1e46: v1e46 = MLOAD v1e44(0x40)
    0x1e49: v1e49(0x84) = SUB v1e40, v1e46
    0x1e4b: REVERT v1e46, v1e49(0x84)

    Begin block 0x1e4c
    prev=[0x1dfa], succ=[0x2dbdB0x1e4c]
    =================================
    0x1e4d: v1e4d(0x1e58) = CONST 
    0x1e51: v1e51(0x0) = CONST 
    0x1e54: v1e54(0x2dbd) = CONST 
    0x1e57: JUMP v1e54(0x2dbd), v1767arg0, v1e51(0x0), v1767arg1, v1e4d(0x1e58)

    Begin block 0x2dbdB0x1e4c
    prev=[0x1e4c], succ=[0x1e58]
    =================================
    0x2dc1S0x1e4c: JUMP v1e4d(0x1e58)

    Begin block 0x1e58
    prev=[0x2dbdB0x1e4c], succ=[0x1ea8]
    =================================
    0x1e59: v1e59(0x1ea8) = CONST 
    0x1e5d: v1e5d(0x40) = CONST 
    0x1e5f: v1e5f = MLOAD v1e5d(0x40)
    0x1e61: v1e61(0x60) = CONST 
    0x1e63: v1e63 = ADD v1e61(0x60), v1e5f
    0x1e64: v1e64(0x40) = CONST 
    0x1e66: MSTORE v1e64(0x40), v1e63
    0x1e68: v1e68(0x22) = CONST 
    0x1e6b: MSTORE v1e5f, v1e68(0x22)
    0x1e6c: v1e6c(0x20) = CONST 
    0x1e6e: v1e6e = ADD v1e6c(0x20), v1e5f
    0x1e6f: v1e6f(0x2014) = CONST 
    0x1e72: v1e72(0x22) = CONST 
    0x1e75: CODECOPY v1e6e, v1e6f(0x2014), v1e72(0x22)
    0x1e76: v1e76(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e8c: v1e8c = AND v1767arg1, v1e76(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e8d: v1e8d(0x0) = CONST 
    0x1e91: MSTORE v1e8d(0x0), v1e8c
    0x1e92: v1e92(0xe) = CONST 
    0x1e94: v1e94(0x20) = CONST 
    0x1e96: MSTORE v1e94(0x20), v1e92(0xe)
    0x1e97: v1e97(0x40) = CONST 
    0x1e9a: v1e9a = SHA3 v1e8d(0x0), v1e97(0x40)
    0x1e9b: v1e9b = SLOAD v1e9a
    0x1e9e: v1e9e(0xffffffff) = CONST 
    0x1ea3: v1ea3(0x1510) = CONST 
    0x1ea6: v1ea6(0x1510) = AND v1ea3(0x1510), v1e9e(0xffffffff)
    0x1ea7: v1ea7_0 = CALLPRIVATE v1ea6(0x1510), v1e5f, v1767arg0, v1e9b, v1e59(0x1ea8)

    Begin block 0x1ea8
    prev=[0x1e58], succ=[0x1c0eB0x1ea8]
    =================================
    0x1ea9: v1ea9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ebf: v1ebf = AND v1767arg1, v1ea9(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ec0: v1ec0(0x0) = CONST 
    0x1ec4: MSTORE v1ec0(0x0), v1ebf
    0x1ec5: v1ec5(0xe) = CONST 
    0x1ec7: v1ec7(0x20) = CONST 
    0x1ec9: MSTORE v1ec7(0x20), v1ec5(0xe)
    0x1eca: v1eca(0x40) = CONST 
    0x1ecd: v1ecd = SHA3 v1ec0(0x0), v1eca(0x40)
    0x1ece: SSTORE v1ecd, v1ea7_0
    0x1ecf: v1ecf(0x4) = CONST 
    0x1ed1: v1ed1 = SLOAD v1ecf(0x4)
    0x1ed2: v1ed2(0x1ee1) = CONST 
    0x1ed7: v1ed7(0xffffffff) = CONST 
    0x1edc: v1edc(0x1c0e) = CONST 
    0x1edf: v1edf(0x1c0e) = AND v1edc(0x1c0e), v1ed7(0xffffffff)
    0x1ee0: JUMP v1edf(0x1c0e)

    Begin block 0x1c0eB0x1ea8
    prev=[0x1ea8], succ=[0x2d73B0x1ea8]
    =================================
    0x1c0fS0x1ea8: v1c0fV1ea8(0x0) = CONST 
    0x1c11S0x1ea8: v1c11V1ea8(0x2d73) = CONST 
    0x1c16S0x1ea8: v1c16V1ea8(0x40) = CONST 
    0x1c18S0x1ea8: v1c18V1ea8 = MLOAD v1c16V1ea8(0x40)
    0x1c1aS0x1ea8: v1c1aV1ea8(0x40) = CONST 
    0x1c1cS0x1ea8: v1c1cV1ea8 = ADD v1c1aV1ea8(0x40), v1c18V1ea8
    0x1c1dS0x1ea8: v1c1dV1ea8(0x40) = CONST 
    0x1c1fS0x1ea8: MSTORE v1c1dV1ea8(0x40), v1c1cV1ea8
    0x1c21S0x1ea8: v1c21V1ea8(0x1e) = CONST 
    0x1c24S0x1ea8: MSTORE v1c18V1ea8, v1c21V1ea8(0x1e)
    0x1c25S0x1ea8: v1c25V1ea8(0x20) = CONST 
    0x1c27S0x1ea8: v1c27V1ea8 = ADD v1c25V1ea8(0x20), v1c18V1ea8
    0x1c28S0x1ea8: v1c28V1ea8(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x1c4aS0x1ea8: MSTORE v1c27V1ea8, v1c28V1ea8(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1c4cS0x1ea8: v1c4cV1ea8(0x1510) = CONST 
    0x1c4fS0x1ea8: v1c4f_0V1ea8 = CALLPRIVATE v1c4cV1ea8(0x1510), v1c18V1ea8, v1767arg0, v1ed1, v1c11V1ea8(0x2d73)

    Begin block 0x2d73B0x1ea8
    prev=[0x1c0eB0x1ea8], succ=[0x1ee1]
    =================================
    0x2d79S0x1ea8: JUMP v1ed2(0x1ee1)

    Begin block 0x1ee1
    prev=[0x2d73B0x1ea8], succ=[0x1b7c]
    =================================
    0x1ee2: v1ee2(0x4) = CONST 
    0x1ee4: SSTORE v1ee2(0x4), v1c4f_0V1ea8
    0x1ee5: v1ee5(0x40) = CONST 
    0x1ee8: v1ee8 = MLOAD v1ee5(0x40)
    0x1eeb: MSTORE v1ee8, v1767arg0
    0x1eed: v1eed = MLOAD v1ee5(0x40)
    0x1eee: v1eee(0x0) = CONST 
    0x1ef1: v1ef1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f07: v1f07 = AND v1767arg1, v1ef1(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f09: v1f09(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1f2d: v1f2d(0x0) = SUB v1ee8, v1eed
    0x1f2e: v1f2e(0x20) = CONST 
    0x1f30: v1f30(0x20) = ADD v1f2e(0x20), v1f2d(0x0)
    0x1f32: LOG3 v1eed, v1f30(0x20), v1f09(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1f07, v1eee(0x0)
    0x1f35: JUMP v1b73(0x1b7c)

    Begin block 0x1b7c
    prev=[0x1ee1], succ=[0x2cbf]
    =================================
    0x1b7d: v1b7d(0x40) = CONST 
    0x1b80: v1b80 = MLOAD v1b7d(0x40)
    0x1b83: MSTORE v1b80, v1767arg0
    0x1b85: v1b85 = MLOAD v1b7d(0x40)
    0x1b86: v1b86(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b9c: v1b9c = AND v1767arg1, v1b86(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b9e: v1b9e(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0x1bc3: v1bc3(0x0) = SUB v1b80, v1b85
    0x1bc4: v1bc4(0x20) = CONST 
    0x1bc6: v1bc6(0x20) = ADD v1bc4(0x20), v1bc3(0x0)
    0x1bc8: LOG2 v1b85, v1bc6(0x20), v1b9e(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), v1b9c
    0x1bcb: JUMP v17cc(0x2cbf)

    Begin block 0x2cbf
    prev=[0x1b7c], succ=[]
    =================================
    0x2cc2: RETURNPRIVATE v1767arg2

}

function 0x18e8(0x18e8arg0x0, 0x18e8arg0x1, 0x18e8arg0x2) private {
    Begin block 0x18e8
    prev=[], succ=[0x1956, 0x1926]
    =================================
    0x18e9: v18e9(0x14) = CONST 
    0x18ec: v18ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1901: v1901 = AND v18ec(0xffffffffffffffffffffffffffffffffffffffff), v18e8arg0
    0x1903: v1903 = SHR v18e9(0x14), v1901
    0x1904: v1904(0x14) = CONST 
    0x1907: v1907(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x191c: v191c = AND v1907(0xffffffffffffffffffffffffffffffffffffffff), v18e8arg1
    0x191e: v191e = SHR v1904(0x14), v191c
    0x191f: v191f = EQ v191e, v1903
    0x1920: v1920 = ISZERO v191f
    0x1922: v1922(0x1956) = CONST 
    0x1925: JUMPI v1922(0x1956), v1920

    Begin block 0x1956
    prev=[0x18e8, 0x1926], succ=[0x195b, 0x2ce2]
    =================================
    0x1956_0x0: v1956_0 = PHI v1920, v1955
    0x1957: v1957(0x2ce2) = CONST 
    0x195a: JUMPI v1957(0x2ce2), v1956_0

    Begin block 0x195b
    prev=[0x1956], succ=[]
    =================================
    0x195b: v195b(0x40) = CONST 
    0x195e: v195e = MLOAD v195b(0x40)
    0x195f: v195f(0x461bcd) = CONST 
    0x1963: v1963(0xe5) = CONST 
    0x1965: v1965(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1963(0xe5), v195f(0x461bcd)
    0x1967: MSTORE v195e, v1965(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1968: v1968(0x20) = CONST 
    0x196a: v196a(0x4) = CONST 
    0x196d: v196d = ADD v195e, v196a(0x4)
    0x196e: MSTORE v196d, v1968(0x20)
    0x196f: v196f(0x15) = CONST 
    0x1971: v1971(0x24) = CONST 
    0x1974: v1974 = ADD v195e, v1971(0x24)
    0x1975: MSTORE v1974, v196f(0x15)
    0x1976: v1976(0x4175746f73776565702069732064697361626c65640000000000000000000000) = CONST 
    0x1997: v1997(0x44) = CONST 
    0x199a: v199a = ADD v195e, v1997(0x44)
    0x199b: MSTORE v199a, v1976(0x4175746f73776565702069732064697361626c65640000000000000000000000)
    0x199d: v199d = MLOAD v195b(0x40)
    0x19a1: v19a1(0x0) = SUB v195e, v199d
    0x19a2: v19a2(0x64) = CONST 
    0x19a4: v19a4(0x64) = ADD v19a2(0x64), v19a1(0x0)
    0x19a6: REVERT v199d, v19a4(0x64)

    Begin block 0x2ce2
    prev=[0x1956], succ=[]
    =================================
    0x2ce5: RETURNPRIVATE v18e8arg2

    Begin block 0x1926
    prev=[0x18e8], succ=[0x1956]
    =================================
    0x1928: v1928(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x193d: v193d = AND v1928(0xffffffffffffffffffffffffffffffffffffffff), v18e8arg0
    0x193f: v193f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1954: v1954 = AND v193f(0xffffffffffffffffffffffffffffffffffffffff), v18e8arg1
    0x1955: v1955 = EQ v1954, v193d

}

function 0x1bcc(0x1bccarg0x0, 0x1bccarg0x1, 0x1bccarg0x2) private {
    Begin block 0x1bcc
    prev=[], succ=[0x1f36]
    =================================
    0x1bcd: v1bcd(0x0) = CONST 
    0x1bcf: v1bcf(0x2d4d) = CONST 
    0x1bd4: v1bd4(0x40) = CONST 
    0x1bd6: v1bd6 = MLOAD v1bd4(0x40)
    0x1bd8: v1bd8(0x40) = CONST 
    0x1bda: v1bda = ADD v1bd8(0x40), v1bd6
    0x1bdb: v1bdb(0x40) = CONST 
    0x1bdd: MSTORE v1bdb(0x40), v1bda
    0x1bdf: v1bdf(0x18) = CONST 
    0x1be2: MSTORE v1bd6, v1bdf(0x18)
    0x1be3: v1be3(0x20) = CONST 
    0x1be5: v1be5 = ADD v1be3(0x20), v1bd6
    0x1be6: v1be6(0x536166654d6174683a206d6f64756c6f206279207a65726f0000000000000000) = CONST 
    0x1c08: MSTORE v1be5, v1be6(0x536166654d6174683a206d6f64756c6f206279207a65726f0000000000000000)
    0x1c0a: v1c0a(0x1f36) = CONST 
    0x1c0d: JUMP v1c0a(0x1f36)

    Begin block 0x1f36
    prev=[0x1bcc], succ=[0x1f3f, 0x1f85]
    =================================
    0x1f37: v1f37(0x0) = CONST 
    0x1f3b: v1f3b(0x1f85) = CONST 
    0x1f3e: JUMPI v1f3b(0x1f85), v1bccarg0

    Begin block 0x1f3f
    prev=[0x1f36], succ=[0x1f76, 0x15640x1bcc]
    =================================
    0x1f3f: v1f3f(0x40) = CONST 
    0x1f41: v1f41 = MLOAD v1f3f(0x40)
    0x1f42: v1f42(0x461bcd) = CONST 
    0x1f46: v1f46(0xe5) = CONST 
    0x1f48: v1f48(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f46(0xe5), v1f42(0x461bcd)
    0x1f4a: MSTORE v1f41, v1f48(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f4b: v1f4b(0x20) = CONST 
    0x1f4d: v1f4d(0x4) = CONST 
    0x1f50: v1f50 = ADD v1f41, v1f4d(0x4)
    0x1f53: MSTORE v1f50, v1f4b(0x20)
    0x1f55: v1f55(0x18) = MLOAD v1bd6
    0x1f56: v1f56(0x24) = CONST 
    0x1f59: v1f59 = ADD v1f41, v1f56(0x24)
    0x1f5a: MSTORE v1f59, v1f55(0x18)
    0x1f5c: v1f5c(0x18) = MLOAD v1bd6
    0x1f61: v1f61(0x44) = CONST 
    0x1f65: v1f65 = ADD v1f41, v1f61(0x44)
    0x1f69: v1f69 = ADD v1bd6, v1f4b(0x20)
    0x1f6e: v1f6e(0x0) = CONST 
    0x1f71: v1f71 = ISZERO v1f5c(0x18)
    0x1f72: v1f72(0x1564) = CONST 
    0x1f75: JUMPI v1f72(0x1564), v1f71

    Begin block 0x1f76
    prev=[0x1f3f], succ=[0x154c0x1bcc]
    =================================
    0x1f78: v1f78 = ADD v1f6e(0x0), v1f69
    0x1f79: v1f79 = MLOAD v1f78
    0x1f7c: v1f7c = ADD v1f6e(0x0), v1f65
    0x1f7d: MSTORE v1f7c, v1f79
    0x1f7e: v1f7e(0x20) = CONST 
    0x1f80: v1f80(0x20) = ADD v1f7e(0x20), v1f6e(0x0)
    0x1f81: v1f81(0x154c) = CONST 
    0x1f84: JUMP v1f81(0x154c)

    Begin block 0x154c0x1bcc
    prev=[0x1f76, 0x15550x1bcc], succ=[0x15640x1bcc, 0x15550x1bcc]
    =================================
    0x154c0x1bcc_0x0: v154c1bcc_0 = PHI v1f80(0x20), v1bcc155f
    0x154f0x1bcc: v1bcc154f = LT v154c1bcc_0, v1f5c(0x18)
    0x15500x1bcc: v1bcc1550 = ISZERO v1bcc154f
    0x15510x1bcc: v1bcc1551(0x1564) = CONST 
    0x15540x1bcc: JUMPI v1bcc1551(0x1564), v1bcc1550

    Begin block 0x15640x1bcc
    prev=[0x1f3f, 0x154c0x1bcc], succ=[0x15910x1bcc, 0x15780x1bcc]
    =================================
    0x156d0x1bcc: v1bcc156d = ADD v1f5c(0x18), v1f65
    0x156f0x1bcc: v1bcc156f(0x1f) = CONST 
    0x15710x1bcc: v1bcc1571(0x18) = AND v1bcc156f(0x1f), v1f5c(0x18)
    0x15730x1bcc: v1bcc1573 = ISZERO v1bcc1571(0x18)
    0x15740x1bcc: v1bcc1574(0x1591) = CONST 
    0x15770x1bcc: JUMPI v1bcc1574(0x1591), v1bcc1573

    Begin block 0x15910x1bcc
    prev=[0x15640x1bcc, 0x15780x1bcc], succ=[]
    =================================
    0x15910x1bcc_0x1: v15911bcc_1 = PHI v1bcc158e, v1bcc156d
    0x15970x1bcc: v1bcc1597(0x40) = CONST 
    0x15990x1bcc: v1bcc1599 = MLOAD v1bcc1597(0x40)
    0x159c0x1bcc: v1bcc159c = SUB v15911bcc_1, v1bcc1599
    0x159e0x1bcc: REVERT v1bcc1599, v1bcc159c

    Begin block 0x15780x1bcc
    prev=[0x15640x1bcc], succ=[0x15910x1bcc]
    =================================
    0x157a0x1bcc: v1bcc157a = SUB v1bcc156d, v1bcc1571(0x18)
    0x157c0x1bcc: v1bcc157c = MLOAD v1bcc157a
    0x157d0x1bcc: v1bcc157d(0x1) = CONST 
    0x15800x1bcc: v1bcc1580(0x20) = CONST 
    0x15820x1bcc: v1bcc1582(0x8) = SUB v1bcc1580(0x20), v1bcc1571(0x18)
    0x15830x1bcc: v1bcc1583(0x100) = CONST 
    0x15860x1bcc: v1bcc1586(0x10000000000000000) = EXP v1bcc1583(0x100), v1bcc1582(0x8)
    0x15870x1bcc: v1bcc1587(0xffffffffffffffff) = SUB v1bcc1586(0x10000000000000000), v1bcc157d(0x1)
    0x15880x1bcc: v1bcc1588 = NOT v1bcc1587(0xffffffffffffffff)
    0x15890x1bcc: v1bcc1589 = AND v1bcc1588, v1bcc157c
    0x158b0x1bcc: MSTORE v1bcc157a, v1bcc1589
    0x158c0x1bcc: v1bcc158c(0x20) = CONST 
    0x158e0x1bcc: v1bcc158e = ADD v1bcc158c(0x20), v1bcc157a

    Begin block 0x15550x1bcc
    prev=[0x154c0x1bcc], succ=[0x154c0x1bcc]
    =================================
    0x15550x1bcc_0x0: v15551bcc_0 = PHI v1f80(0x20), v1bcc155f
    0x15570x1bcc: v1bcc1557 = ADD v15551bcc_0, v1f69
    0x15580x1bcc: v1bcc1558 = MLOAD v1bcc1557
    0x155b0x1bcc: v1bcc155b = ADD v15551bcc_0, v1f65
    0x155c0x1bcc: MSTORE v1bcc155b, v1bcc1558
    0x155d0x1bcc: v1bcc155d(0x20) = CONST 
    0x155f0x1bcc: v1bcc155f = ADD v1bcc155d(0x20), v15551bcc_0
    0x15600x1bcc: v1bcc1560(0x154c) = CONST 
    0x15630x1bcc: JUMP v1bcc1560(0x154c)

    Begin block 0x1f85
    prev=[0x1f36], succ=[0x1f8e, 0x1f8f]
    =================================
    0x1f8a: v1f8a(0x1f8f) = CONST 
    0x1f8d: JUMPI v1f8a(0x1f8f), v1bccarg0

    Begin block 0x1f8e
    prev=[0x1f85], succ=[]
    =================================
    0x1f8e: THROW 

    Begin block 0x1f8f
    prev=[0x1f85], succ=[0x2d4d]
    =================================
    0x1f90: v1f90 = MOD v1bccarg1, v1bccarg0
    0x1f97: JUMP v1bcf(0x2d4d)

    Begin block 0x2d4d
    prev=[0x1f8f], succ=[]
    =================================
    0x2d53: RETURNPRIVATE v1bccarg2, v1f90

}

function 0x1c50(0x1c50arg0x0, 0x1c50arg0x1, 0x1c50arg0x2, 0x1c50arg0x3) private {
    Begin block 0x1c50
    prev=[], succ=[0x1c6c, 0x1ca2]
    =================================
    0x1c51: v1c51(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c67: v1c67 = AND v1c50arg2, v1c51(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c68: v1c68(0x1ca2) = CONST 
    0x1c6b: JUMPI v1c68(0x1ca2), v1c67

    Begin block 0x1c6c
    prev=[0x1c50], succ=[]
    =================================
    0x1c6c: v1c6c(0x40) = CONST 
    0x1c6e: v1c6e = MLOAD v1c6c(0x40)
    0x1c6f: v1c6f(0x461bcd) = CONST 
    0x1c73: v1c73(0xe5) = CONST 
    0x1c75: v1c75(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c73(0xe5), v1c6f(0x461bcd)
    0x1c77: MSTORE v1c6e, v1c75(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c78: v1c78(0x4) = CONST 
    0x1c7a: v1c7a = ADD v1c78(0x4), v1c6e
    0x1c7d: v1c7d(0x20) = CONST 
    0x1c7f: v1c7f = ADD v1c7d(0x20), v1c7a
    0x1c82: v1c82(0x20) = SUB v1c7f, v1c7a
    0x1c84: MSTORE v1c7a, v1c82(0x20)
    0x1c85: v1c85(0x25) = CONST 
    0x1c88: MSTORE v1c7f, v1c85(0x25)
    0x1c89: v1c89(0x20) = CONST 
    0x1c8b: v1c8b = ADD v1c89(0x20), v1c7f
    0x1c8d: v1c8d(0x21c8) = CONST 
    0x1c90: v1c90(0x25) = CONST 
    0x1c93: CODECOPY v1c8b, v1c8d(0x21c8), v1c90(0x25)
    0x1c94: v1c94(0x40) = CONST 
    0x1c96: v1c96 = ADD v1c94(0x40), v1c8b
    0x1c9a: v1c9a(0x40) = CONST 
    0x1c9c: v1c9c = MLOAD v1c9a(0x40)
    0x1c9f: v1c9f(0x84) = SUB v1c96, v1c9c
    0x1ca1: REVERT v1c9c, v1c9f(0x84)

    Begin block 0x1ca2
    prev=[0x1c50], succ=[0x1cbe, 0x1cf4]
    =================================
    0x1ca3: v1ca3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cb9: v1cb9 = AND v1c50arg1, v1ca3(0xffffffffffffffffffffffffffffffffffffffff)
    0x1cba: v1cba(0x1cf4) = CONST 
    0x1cbd: JUMPI v1cba(0x1cf4), v1cb9

    Begin block 0x1cbe
    prev=[0x1ca2], succ=[]
    =================================
    0x1cbe: v1cbe(0x40) = CONST 
    0x1cc0: v1cc0 = MLOAD v1cbe(0x40)
    0x1cc1: v1cc1(0x461bcd) = CONST 
    0x1cc5: v1cc5(0xe5) = CONST 
    0x1cc7: v1cc7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1cc5(0xe5), v1cc1(0x461bcd)
    0x1cc9: MSTORE v1cc0, v1cc7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cca: v1cca(0x4) = CONST 
    0x1ccc: v1ccc = ADD v1cca(0x4), v1cc0
    0x1ccf: v1ccf(0x20) = CONST 
    0x1cd1: v1cd1 = ADD v1ccf(0x20), v1ccc
    0x1cd4: v1cd4(0x20) = SUB v1cd1, v1ccc
    0x1cd6: MSTORE v1ccc, v1cd4(0x20)
    0x1cd7: v1cd7(0x23) = CONST 
    0x1cda: MSTORE v1cd1, v1cd7(0x23)
    0x1cdb: v1cdb(0x20) = CONST 
    0x1cdd: v1cdd = ADD v1cdb(0x20), v1cd1
    0x1cdf: v1cdf(0x1f99) = CONST 
    0x1ce2: v1ce2(0x23) = CONST 
    0x1ce5: CODECOPY v1cdd, v1cdf(0x1f99), v1ce2(0x23)
    0x1ce6: v1ce6(0x40) = CONST 
    0x1ce8: v1ce8 = ADD v1ce6(0x40), v1cdd
    0x1cec: v1cec(0x40) = CONST 
    0x1cee: v1cee = MLOAD v1cec(0x40)
    0x1cf1: v1cf1(0x84) = SUB v1ce8, v1cee
    0x1cf3: REVERT v1cee, v1cf1(0x84)

    Begin block 0x1cf4
    prev=[0x1ca2], succ=[0x2d99B0x1cf4]
    =================================
    0x1cf5: v1cf5(0x1cff) = CONST 
    0x1cfb: v1cfb(0x2d99) = CONST 
    0x1cfe: JUMP v1cfb(0x2d99), v1c50arg0, v1c50arg1, v1c50arg2, v1cf5(0x1cff)

    Begin block 0x2d99B0x1cf4
    prev=[0x1cf4], succ=[0x1cff]
    =================================
    0x2d9dS0x1cf4: JUMP v1cf5(0x1cff)

    Begin block 0x1cff
    prev=[0x2d99B0x1cf4], succ=[0x1d4f]
    =================================
    0x1d00: v1d00(0x1d4f) = CONST 
    0x1d04: v1d04(0x40) = CONST 
    0x1d06: v1d06 = MLOAD v1d04(0x40)
    0x1d08: v1d08(0x60) = CONST 
    0x1d0a: v1d0a = ADD v1d08(0x60), v1d06
    0x1d0b: v1d0b(0x40) = CONST 
    0x1d0d: MSTORE v1d0b(0x40), v1d0a
    0x1d0f: v1d0f(0x26) = CONST 
    0x1d12: MSTORE v1d06, v1d0f(0x26)
    0x1d13: v1d13(0x20) = CONST 
    0x1d15: v1d15 = ADD v1d13(0x20), v1d06
    0x1d16: v1d16(0x207c) = CONST 
    0x1d19: v1d19(0x26) = CONST 
    0x1d1c: CODECOPY v1d15, v1d16(0x207c), v1d19(0x26)
    0x1d1d: v1d1d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d33: v1d33 = AND v1c50arg2, v1d1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d34: v1d34(0x0) = CONST 
    0x1d38: MSTORE v1d34(0x0), v1d33
    0x1d39: v1d39(0xe) = CONST 
    0x1d3b: v1d3b(0x20) = CONST 
    0x1d3d: MSTORE v1d3b(0x20), v1d39(0xe)
    0x1d3e: v1d3e(0x40) = CONST 
    0x1d41: v1d41 = SHA3 v1d34(0x0), v1d3e(0x40)
    0x1d42: v1d42 = SLOAD v1d41
    0x1d45: v1d45(0xffffffff) = CONST 
    0x1d4a: v1d4a(0x1510) = CONST 
    0x1d4d: v1d4d(0x1510) = AND v1d4a(0x1510), v1d45(0xffffffff)
    0x1d4e: v1d4e_0 = CALLPRIVATE v1d4d(0x1510), v1d06, v1c50arg0, v1d42, v1d00(0x1d4f)

    Begin block 0x1d4f
    prev=[0x1cff], succ=[0x15a7B0x1d4f]
    =================================
    0x1d50: v1d50(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d67: v1d67 = AND v1c50arg2, v1d50(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d68: v1d68(0x0) = CONST 
    0x1d6c: MSTORE v1d68(0x0), v1d67
    0x1d6d: v1d6d(0xe) = CONST 
    0x1d6f: v1d6f(0x20) = CONST 
    0x1d71: MSTORE v1d6f(0x20), v1d6d(0xe)
    0x1d72: v1d72(0x40) = CONST 
    0x1d76: v1d76 = SHA3 v1d68(0x0), v1d72(0x40)
    0x1d7a: SSTORE v1d76, v1d4e_0
    0x1d7d: v1d7d = AND v1c50arg1, v1d50(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d7f: MSTORE v1d68(0x0), v1d7d
    0x1d80: v1d80 = SHA3 v1d68(0x0), v1d72(0x40)
    0x1d81: v1d81 = SLOAD v1d80
    0x1d82: v1d82(0x1d91) = CONST 
    0x1d87: v1d87(0xffffffff) = CONST 
    0x1d8c: v1d8c(0x15a7) = CONST 
    0x1d8f: v1d8f(0x15a7) = AND v1d8c(0x15a7), v1d87(0xffffffff)
    0x1d90: JUMP v1d8f(0x15a7)

    Begin block 0x15a7B0x1d4f
    prev=[0x1d4f], succ=[0x15b5B0x1d4f, 0x2c50B0x1d4f]
    =================================
    0x15a8S0x1d4f: v15a8V1d4f(0x0) = CONST 
    0x15acS0x1d4f: v15acV1d4f = ADD v1c50arg0, v1d81
    0x15afS0x1d4f: v15afV1d4f = LT v15acV1d4f, v1d81
    0x15b0S0x1d4f: v15b0V1d4f = ISZERO v15afV1d4f
    0x15b1S0x1d4f: v15b1V1d4f(0x2c50) = CONST 
    0x15b4S0x1d4f: JUMPI v15b1V1d4f(0x2c50), v15b0V1d4f

    Begin block 0x15b5B0x1d4f
    prev=[0x15a7B0x1d4f], succ=[]
    =================================
    0x15b5S0x1d4f: v15b5V1d4f(0x40) = CONST 
    0x15b8S0x1d4f: v15b8V1d4f = MLOAD v15b5V1d4f(0x40)
    0x15b9S0x1d4f: v15b9V1d4f(0x461bcd) = CONST 
    0x15bdS0x1d4f: v15bdV1d4f(0xe5) = CONST 
    0x15bfS0x1d4f: v15bfV1d4f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15bdV1d4f(0xe5), v15b9V1d4f(0x461bcd)
    0x15c1S0x1d4f: MSTORE v15b8V1d4f, v15bfV1d4f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15c2S0x1d4f: v15c2V1d4f(0x20) = CONST 
    0x15c4S0x1d4f: v15c4V1d4f(0x4) = CONST 
    0x15c7S0x1d4f: v15c7V1d4f = ADD v15b8V1d4f, v15c4V1d4f(0x4)
    0x15c8S0x1d4f: MSTORE v15c7V1d4f, v15c2V1d4f(0x20)
    0x15c9S0x1d4f: v15c9V1d4f(0x1b) = CONST 
    0x15cbS0x1d4f: v15cbV1d4f(0x24) = CONST 
    0x15ceS0x1d4f: v15ceV1d4f = ADD v15b8V1d4f, v15cbV1d4f(0x24)
    0x15cfS0x1d4f: MSTORE v15ceV1d4f, v15c9V1d4f(0x1b)
    0x15d0S0x1d4f: v15d0V1d4f(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x15f1S0x1d4f: v15f1V1d4f(0x44) = CONST 
    0x15f4S0x1d4f: v15f4V1d4f = ADD v15b8V1d4f, v15f1V1d4f(0x44)
    0x15f5S0x1d4f: MSTORE v15f4V1d4f, v15d0V1d4f(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x15f7S0x1d4f: v15f7V1d4f = MLOAD v15b5V1d4f(0x40)
    0x15fbS0x1d4f: v15fbV1d4f(0x0) = SUB v15b8V1d4f, v15f7V1d4f
    0x15fcS0x1d4f: v15fcV1d4f(0x64) = CONST 
    0x15feS0x1d4f: v15feV1d4f(0x64) = ADD v15fcV1d4f(0x64), v15fbV1d4f(0x0)
    0x1600S0x1d4f: REVERT v15f7V1d4f, v15feV1d4f(0x64)

    Begin block 0x2c50B0x1d4f
    prev=[0x15a7B0x1d4f], succ=[0x1d91]
    =================================
    0x2c56S0x1d4f: JUMP v1d82(0x1d91)

    Begin block 0x1d91
    prev=[0x2c50B0x1d4f], succ=[]
    =================================
    0x1d92: v1d92(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1da9: v1da9 = AND v1c50arg1, v1d92(0xffffffffffffffffffffffffffffffffffffffff)
    0x1daa: v1daa(0x0) = CONST 
    0x1dae: MSTORE v1daa(0x0), v1da9
    0x1daf: v1daf(0xe) = CONST 
    0x1db1: v1db1(0x20) = CONST 
    0x1db5: MSTORE v1db1(0x20), v1daf(0xe)
    0x1db6: v1db6(0x40) = CONST 
    0x1dbb: v1dbb = SHA3 v1daa(0x0), v1db6(0x40)
    0x1dbf: SSTORE v1dbb, v15acV1d4f
    0x1dc1: v1dc1 = MLOAD v1db6(0x40)
    0x1dc4: MSTORE v1dc1, v1c50arg0
    0x1dc6: v1dc6 = MLOAD v1db6(0x40)
    0x1dcb: v1dcb = AND v1c50arg2, v1d92(0xffffffffffffffffffffffffffffffffffffffff)
    0x1dcd: v1dcd(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1df2: v1df2(0x0) = SUB v1dc1, v1dc6
    0x1df3: v1df3(0x20) = ADD v1df2(0x0), v1db1(0x20)
    0x1df5: LOG3 v1dc6, v1df3(0x20), v1dcd(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1dcb, v1da9
    0x1df9: RETURNPRIVATE v1c50arg3

}

function burnMin()() public {
    Begin block 0x22b
    prev=[], succ=[0x7b1]
    =================================
    0x22c: v22c(0x254b) = CONST 
    0x22f: v22f(0x7b1) = CONST 
    0x232: JUMP v22f(0x7b1)

    Begin block 0x7b1
    prev=[0x22b], succ=[0x254b]
    =================================
    0x7b2: v7b2(0x6) = CONST 
    0x7b4: v7b4 = SLOAD v7b2(0x6)
    0x7b6: JUMP v22c(0x254b)

    Begin block 0x254b
    prev=[0x7b1], succ=[]
    =================================
    0x254c: v254c(0x40) = CONST 
    0x254f: v254f = MLOAD v254c(0x40)
    0x2552: MSTORE v254f, v7b4
    0x2553: v2553 = MLOAD v254c(0x40)
    0x2557: v2557(0x0) = SUB v254f, v2553
    0x2558: v2558(0x20) = CONST 
    0x255a: v255a(0x20) = ADD v2558(0x20), v2557(0x0)
    0x255c: RETURN v2553, v255a(0x20)

}

function fallback()() public {
    Begin block 0x2333
    prev=[], succ=[]
    =================================
    0x2334: v2334(0x0) = CONST 
    0x2337: REVERT v2334(0x0), v2334(0x0)

}

function name()() public {
    Begin block 0x245
    prev=[], succ=[0x7b7]
    =================================
    0x246: v246(0x24d) = CONST 
    0x249: v249(0x7b7) = CONST 
    0x24c: JUMP v249(0x7b7)

    Begin block 0x7b7
    prev=[0x245], succ=[0x24d0x245]
    =================================
    0x7b8: v7b8(0x40) = CONST 
    0x7bb: v7bb = MLOAD v7b8(0x40)
    0x7be: v7be = ADD v7b8(0x40), v7bb
    0x7c1: MSTORE v7b8(0x40), v7be
    0x7c2: v7c2(0x7) = CONST 
    0x7c5: MSTORE v7bb, v7c2(0x7)
    0x7c6: v7c6(0x5472756555534400000000000000000000000000000000000000000000000000) = CONST 
    0x7e7: v7e7(0x20) = CONST 
    0x7ea: v7ea = ADD v7bb, v7e7(0x20)
    0x7eb: MSTORE v7ea, v7c6(0x5472756555534400000000000000000000000000000000000000000000000000)
    0x7ed: JUMP v246(0x24d)

    Begin block 0x24d0x245
    prev=[0x7b7], succ=[0x26f0x245]
    =================================
    0x24e0x245: v24524e(0x40) = CONST 
    0x2510x245: v245251 = MLOAD v24524e(0x40)
    0x2520x245: v245252(0x20) = CONST 
    0x2560x245: MSTORE v245251, v245252(0x20)
    0x2580x245: v245258(0x7) = MLOAD v7bb
    0x25b0x245: v24525b = ADD v245251, v245252(0x20)
    0x25c0x245: MSTORE v24525b, v245258(0x7)
    0x25e0x245: v24525e(0x7) = MLOAD v7bb
    0x2650x245: v245265 = ADD v245251, v24524e(0x40)
    0x2680x245: v245268 = ADD v7bb, v245252(0x20)
    0x26d0x245: v24526d(0x0) = CONST 

    Begin block 0x26f0x245
    prev=[0x2780x245, 0x24d0x245], succ=[0x2870x245, 0x2780x245]
    =================================
    0x26f0x245_0x0: v26f245_0 = PHI v245282, v24526d(0x0)
    0x2720x245: v245272 = LT v26f245_0, v24525e(0x7)
    0x2730x245: v245273 = ISZERO v245272
    0x2740x245: v245274(0x287) = CONST 
    0x2770x245: JUMPI v245274(0x287), v245273

    Begin block 0x2870x245
    prev=[0x26f0x245], succ=[0x2b40x245, 0x29b0x245]
    =================================
    0x2900x245: v245290 = ADD v24525e(0x7), v245265
    0x2920x245: v245292(0x1f) = CONST 
    0x2940x245: v245294(0x7) = AND v245292(0x1f), v24525e(0x7)
    0x2960x245: v245296 = ISZERO v245294(0x7)
    0x2970x245: v245297(0x2b4) = CONST 
    0x29a0x245: JUMPI v245297(0x2b4), v245296

    Begin block 0x2b40x245
    prev=[0x2870x245, 0x29b0x245], succ=[]
    =================================
    0x2b40x245_0x1: v2b4245_1 = PHI v2452b1, v245290
    0x2ba0x245: v2452ba(0x40) = CONST 
    0x2bc0x245: v2452bc = MLOAD v2452ba(0x40)
    0x2bf0x245: v2452bf = SUB v2b4245_1, v2452bc
    0x2c10x245: RETURN v2452bc, v2452bf

    Begin block 0x29b0x245
    prev=[0x2870x245], succ=[0x2b40x245]
    =================================
    0x29d0x245: v24529d = SUB v245290, v245294(0x7)
    0x29f0x245: v24529f = MLOAD v24529d
    0x2a00x245: v2452a0(0x1) = CONST 
    0x2a30x245: v2452a3(0x20) = CONST 
    0x2a50x245: v2452a5(0x19) = SUB v2452a3(0x20), v245294(0x7)
    0x2a60x245: v2452a6(0x100) = CONST 
    0x2a90x245: v2452a9(0x100000000000000000000000000000000000000000000000000) = EXP v2452a6(0x100), v2452a5(0x19)
    0x2aa0x245: v2452aa(0xffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2452a9(0x100000000000000000000000000000000000000000000000000), v2452a0(0x1)
    0x2ab0x245: v2452ab = NOT v2452aa(0xffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2ac0x245: v2452ac = AND v2452ab, v24529f
    0x2ae0x245: MSTORE v24529d, v2452ac
    0x2af0x245: v2452af(0x20) = CONST 
    0x2b10x245: v2452b1 = ADD v2452af(0x20), v24529d

    Begin block 0x2780x245
    prev=[0x26f0x245], succ=[0x26f0x245]
    =================================
    0x2780x245_0x0: v278245_0 = PHI v245282, v24526d(0x0)
    0x27a0x245: v24527a = ADD v278245_0, v245268
    0x27b0x245: v24527b = MLOAD v24527a
    0x27e0x245: v24527e = ADD v278245_0, v245265
    0x27f0x245: MSTORE v24527e, v24527b
    0x2800x245: v245280(0x20) = CONST 
    0x2820x245: v245282 = ADD v245280(0x20), v278245_0
    0x2830x245: v245283(0x26f) = CONST 
    0x2860x245: JUMP v245283(0x26f)

}

function approve(address,uint256)() public {
    Begin block 0x2c2
    prev=[], succ=[0x2d4, 0x2d8]
    =================================
    0x2c3: v2c3(0x257c) = CONST 
    0x2c6: v2c6(0x4) = CONST 
    0x2c9: v2c9 = CALLDATASIZE 
    0x2ca: v2ca = SUB v2c9, v2c6(0x4)
    0x2cb: v2cb(0x40) = CONST 
    0x2ce: v2ce = LT v2ca, v2cb(0x40)
    0x2cf: v2cf = ISZERO v2ce
    0x2d0: v2d0(0x2d8) = CONST 
    0x2d3: JUMPI v2d0(0x2d8), v2cf

    Begin block 0x2d4
    prev=[0x2c2], succ=[]
    =================================
    0x2d4: v2d4(0x0) = CONST 
    0x2d7: REVERT v2d4(0x0), v2d4(0x0)

    Begin block 0x2d8
    prev=[0x2c2], succ=[0x7ee]
    =================================
    0x2da: v2da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f0: v2f0 = CALLDATALOAD v2c6(0x4)
    0x2f1: v2f1 = AND v2f0, v2da(0xffffffffffffffffffffffffffffffffffffffff)
    0x2f3: v2f3(0x20) = CONST 
    0x2f5: v2f5(0x24) = ADD v2f3(0x20), v2c6(0x4)
    0x2f6: v2f6 = CALLDATALOAD v2f5(0x24)
    0x2f7: v2f7(0x7ee) = CONST 
    0x2fa: JUMP v2f7(0x7ee)

    Begin block 0x7ee
    prev=[0x2d8], succ=[0x13a6B0x7ee]
    =================================
    0x7ef: v7ef(0x0) = CONST 
    0x7f1: v7f1(0x2a8e) = CONST 
    0x7f4: v7f4(0x7fb) = CONST 
    0x7f7: v7f7(0x13a6) = CONST 
    0x7fa: JUMP v7f7(0x13a6)

    Begin block 0x13a6B0x7ee
    prev=[0x7ee], succ=[0x7fb]
    =================================
    0x13a7S0x7ee: v13a7V7ee = CALLER 
    0x13a9S0x7ee: JUMP v7f4(0x7fb)

    Begin block 0x7fb
    prev=[0x13a6B0x7ee], succ=[0x2a8e]
    =================================
    0x7fe: v7fe(0x13aa) = CONST 
    0x801: CALLPRIVATE v7fe(0x13aa), v2f6, v2f1, v13a7V7ee, v7f1(0x2a8e)

    Begin block 0x2a8e
    prev=[0x7fb], succ=[0x257c]
    =================================
    0x2a90: v2a90(0x1) = CONST 
    0x2a96: JUMP v2c3(0x257c)

    Begin block 0x257c
    prev=[0x2a8e], succ=[]
    =================================
    0x257d: v257d(0x40) = CONST 
    0x2580: v2580 = MLOAD v257d(0x40)
    0x2582: v2582 = ISZERO v2a90(0x1)
    0x2583: v2583 = ISZERO v2582
    0x2585: MSTORE v2580, v2583
    0x2586: v2586 = MLOAD v257d(0x40)
    0x258a: v258a(0x0) = SUB v2580, v2586
    0x258b: v258b(0x20) = CONST 
    0x258d: v258d(0x20) = ADD v258b(0x20), v258a(0x0)
    0x258f: RETURN v2586, v258d(0x20)

}

function delegateAllowance(address,address)() public {
    Begin block 0x30f
    prev=[], succ=[0x321, 0x325]
    =================================
    0x310: v310(0x25af) = CONST 
    0x313: v313(0x4) = CONST 
    0x316: v316 = CALLDATASIZE 
    0x317: v317 = SUB v316, v313(0x4)
    0x318: v318(0x40) = CONST 
    0x31b: v31b = LT v317, v318(0x40)
    0x31c: v31c = ISZERO v31b
    0x31d: v31d(0x325) = CONST 
    0x320: JUMPI v31d(0x325), v31c

    Begin block 0x321
    prev=[0x30f], succ=[]
    =================================
    0x321: v321(0x0) = CONST 
    0x324: REVERT v321(0x0), v321(0x0)

    Begin block 0x325
    prev=[0x30f], succ=[0x80b]
    =================================
    0x327: v327(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33d: v33d = CALLDATALOAD v313(0x4)
    0x33f: v33f = AND v327(0xffffffffffffffffffffffffffffffffffffffff), v33d
    0x341: v341(0x20) = CONST 
    0x343: v343(0x24) = ADD v341(0x20), v313(0x4)
    0x344: v344 = CALLDATALOAD v343(0x24)
    0x345: v345 = AND v344, v327(0xffffffffffffffffffffffffffffffffffffffff)
    0x346: v346(0x80b) = CONST 
    0x349: JUMP v346(0x80b)

    Begin block 0x80b
    prev=[0x325], succ=[0x129f0x30f]
    =================================
    0x80c: v80c(0x0) = CONST 
    0x80e: v80e(0x2ab6) = CONST 
    0x813: v813(0x129f) = CONST 
    0x816: JUMP v813(0x129f)

    Begin block 0x129f0x30f
    prev=[0x80b], succ=[0x2ab6]
    =================================
    0x12a00x30f: v30f12a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12b70x30f: v30f12b7 = AND v30f12a0(0xffffffffffffffffffffffffffffffffffffffff), v33f
    0x12b80x30f: v30f12b8(0x0) = CONST 
    0x12bc0x30f: MSTORE v30f12b8(0x0), v30f12b7
    0x12bd0x30f: v30f12bd(0xf) = CONST 
    0x12bf0x30f: v30f12bf(0x20) = CONST 
    0x12c30x30f: MSTORE v30f12bf(0x20), v30f12bd(0xf)
    0x12c40x30f: v30f12c4(0x40) = CONST 
    0x12c80x30f: v30f12c8 = SHA3 v30f12b8(0x0), v30f12c4(0x40)
    0x12cc0x30f: v30f12cc = AND v30f12a0(0xffffffffffffffffffffffffffffffffffffffff), v345
    0x12ce0x30f: MSTORE v30f12b8(0x0), v30f12cc
    0x12d20x30f: MSTORE v30f12bf(0x20), v30f12c8
    0x12d30x30f: v30f12d3 = SHA3 v30f12b8(0x0), v30f12c4(0x40)
    0x12d40x30f: v30f12d4 = SLOAD v30f12d3
    0x12d60x30f: JUMP v80e(0x2ab6)

    Begin block 0x2ab6
    prev=[0x129f0x30f], succ=[0x25af]
    =================================
    0x2abc: JUMP v310(0x25af)

    Begin block 0x25af
    prev=[0x2ab6], succ=[]
    =================================
    0x25b0: v25b0(0x40) = CONST 
    0x25b3: v25b3 = MLOAD v25b0(0x40)
    0x25b6: MSTORE v25b3, v30f12d4
    0x25b7: v25b7 = MLOAD v25b0(0x40)
    0x25bb: v25bb(0x0) = SUB v25b3, v25b7
    0x25bc: v25bc(0x20) = CONST 
    0x25be: v25be(0x20) = ADD v25bc(0x20), v25bb(0x0)
    0x25c0: RETURN v25b7, v25be(0x20)

}

function totalSupply()() public {
    Begin block 0x34a
    prev=[], succ=[0x81eB0x34a]
    =================================
    0x34b: v34b(0x25e0) = CONST 
    0x34e: v34e(0x81e) = CONST 
    0x351: JUMP v34e(0x81e)

    Begin block 0x81eB0x34a
    prev=[0x34a], succ=[0x25e0]
    =================================
    0x81fS0x34a: v81fV34a(0x4) = CONST 
    0x821S0x34a: v821V34a = SLOAD v81fV34a(0x4)
    0x823S0x34a: JUMP v34b(0x25e0)

    Begin block 0x25e0
    prev=[0x81eB0x34a], succ=[]
    =================================
    0x25e1: v25e1(0x40) = CONST 
    0x25e4: v25e4 = MLOAD v25e1(0x40)
    0x25e7: MSTORE v25e4, v821V34a
    0x25e8: v25e8 = MLOAD v25e1(0x40)
    0x25ec: v25ec(0x0) = SUB v25e4, v25e8
    0x25ed: v25ed(0x20) = CONST 
    0x25ef: v25ef(0x20) = ADD v25ed(0x20), v25ec(0x0)
    0x25f1: RETURN v25e8, v25ef(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x352
    prev=[], succ=[0x364, 0x368]
    =================================
    0x353: v353(0x2611) = CONST 
    0x356: v356(0x4) = CONST 
    0x359: v359 = CALLDATASIZE 
    0x35a: v35a = SUB v359, v356(0x4)
    0x35b: v35b(0x60) = CONST 
    0x35e: v35e = LT v35a, v35b(0x60)
    0x35f: v35f = ISZERO v35e
    0x360: v360(0x368) = CONST 
    0x363: JUMPI v360(0x368), v35f

    Begin block 0x364
    prev=[0x352], succ=[]
    =================================
    0x364: v364(0x0) = CONST 
    0x367: REVERT v364(0x0), v364(0x0)

    Begin block 0x368
    prev=[0x352], succ=[0x824]
    =================================
    0x36a: v36a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x380: v380 = CALLDATALOAD v356(0x4)
    0x382: v382 = AND v36a(0xffffffffffffffffffffffffffffffffffffffff), v380
    0x384: v384(0x20) = CONST 
    0x387: v387(0x24) = ADD v356(0x4), v384(0x20)
    0x388: v388 = CALLDATALOAD v387(0x24)
    0x38b: v38b = AND v36a(0xffffffffffffffffffffffffffffffffffffffff), v388
    0x38d: v38d(0x40) = CONST 
    0x38f: v38f(0x44) = ADD v38d(0x40), v356(0x4)
    0x390: v390 = CALLDATALOAD v38f(0x44)
    0x391: v391(0x824) = CONST 
    0x394: JUMP v391(0x824)

    Begin block 0x824
    prev=[0x368], succ=[0x831]
    =================================
    0x825: v825(0x0) = CONST 
    0x827: v827(0x831) = CONST 
    0x82d: v82d(0x148d) = CONST 
    0x830: CALLPRIVATE v82d(0x148d), v390, v38b, v382, v827(0x831)

    Begin block 0x831
    prev=[0x824], succ=[0x13a6B0x831]
    =================================
    0x832: v832(0x8c1) = CONST 
    0x836: v836(0x83d) = CONST 
    0x839: v839(0x13a6) = CONST 
    0x83c: JUMP v839(0x13a6)

    Begin block 0x13a6B0x831
    prev=[0x831], succ=[0x83d]
    =================================
    0x13a7S0x831: v13a7V831 = CALLER 
    0x13a9S0x831: JUMP v836(0x83d)

    Begin block 0x83d
    prev=[0x13a6B0x831], succ=[0x13a6B0x83d]
    =================================
    0x83e: v83e(0x2adc) = CONST 
    0x842: v842(0x40) = CONST 
    0x844: v844 = MLOAD v842(0x40)
    0x846: v846(0x60) = CONST 
    0x848: v848 = ADD v846(0x60), v844
    0x849: v849(0x40) = CONST 
    0x84b: MSTORE v849(0x40), v848
    0x84d: v84d(0x28) = CONST 
    0x850: MSTORE v844, v84d(0x28)
    0x851: v851(0x20) = CONST 
    0x853: v853 = ADD v851(0x20), v844
    0x854: v854(0x2113) = CONST 
    0x857: v857(0x28) = CONST 
    0x85a: CODECOPY v853, v854(0x2113), v857(0x28)
    0x85b: v85b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x871: v871 = AND v382, v85b(0xffffffffffffffffffffffffffffffffffffffff)
    0x872: v872(0x0) = CONST 
    0x876: MSTORE v872(0x0), v871
    0x877: v877(0xf) = CONST 
    0x879: v879(0x20) = CONST 
    0x87b: MSTORE v879(0x20), v877(0xf)
    0x87c: v87c(0x40) = CONST 
    0x87f: v87f = SHA3 v872(0x0), v87c(0x40)
    0x881: v881(0x888) = CONST 
    0x884: v884(0x13a6) = CONST 
    0x887: JUMP v884(0x13a6)

    Begin block 0x13a6B0x83d
    prev=[0x83d], succ=[0x888]
    =================================
    0x13a7S0x83d: v13a7V83d = CALLER 
    0x13a9S0x83d: JUMP v881(0x888)

    Begin block 0x888
    prev=[0x13a6B0x83d], succ=[0x2adc]
    =================================
    0x889: v889(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x89e: v89e = AND v889(0xffffffffffffffffffffffffffffffffffffffff), v13a7V83d
    0x8a0: MSTORE v872(0x0), v89e
    0x8a1: v8a1(0x20) = CONST 
    0x8a4: v8a4(0x20) = ADD v872(0x0), v8a1(0x20)
    0x8a8: MSTORE v8a4(0x20), v87f
    0x8a9: v8a9(0x40) = CONST 
    0x8ab: v8ab(0x40) = ADD v8a9(0x40), v872(0x0)
    0x8ac: v8ac(0x0) = CONST 
    0x8ae: v8ae = SHA3 v8ac(0x0), v8ab(0x40)
    0x8af: v8af = SLOAD v8ae
    0x8b2: v8b2(0xffffffff) = CONST 
    0x8b7: v8b7(0x1510) = CONST 
    0x8ba: v8ba(0x1510) = AND v8b7(0x1510), v8b2(0xffffffff)
    0x8bb: v8bb_0 = CALLPRIVATE v8ba(0x1510), v844, v390, v8af, v83e(0x2adc)

    Begin block 0x2adc
    prev=[0x888], succ=[0x8c1]
    =================================
    0x2add: v2add(0x13aa) = CONST 
    0x2ae0: CALLPRIVATE v2add(0x13aa), v8bb_0, v13a7V831, v382, v832(0x8c1)

    Begin block 0x8c1
    prev=[0x2adc], succ=[0x2611]
    =================================
    0x8c3: v8c3(0x1) = CONST 
    0x8ca: JUMP v353(0x2611)

    Begin block 0x2611
    prev=[0x8c1], succ=[]
    =================================
    0x2612: v2612(0x40) = CONST 
    0x2615: v2615 = MLOAD v2612(0x40)
    0x2617: v2617 = ISZERO v8c3(0x1)
    0x2618: v2618 = ISZERO v2617
    0x261a: MSTORE v2615, v2618
    0x261b: v261b = MLOAD v2612(0x40)
    0x261f: v261f(0x0) = SUB v2615, v261b
    0x2620: v2620(0x20) = CONST 
    0x2622: v2622(0x20) = ADD v2620(0x20), v261f(0x0)
    0x2624: RETURN v261b, v2622(0x20)

}

function delegateTransfer(address,uint256,address)() public {
    Begin block 0x395
    prev=[], succ=[0x3a7, 0x3ab]
    =================================
    0x396: v396(0x2644) = CONST 
    0x399: v399(0x4) = CONST 
    0x39c: v39c = CALLDATASIZE 
    0x39d: v39d = SUB v39c, v399(0x4)
    0x39e: v39e(0x60) = CONST 
    0x3a1: v3a1 = LT v39d, v39e(0x60)
    0x3a2: v3a2 = ISZERO v3a1
    0x3a3: v3a3(0x3ab) = CONST 
    0x3a6: JUMPI v3a3(0x3ab), v3a2

    Begin block 0x3a7
    prev=[0x395], succ=[]
    =================================
    0x3a7: v3a7(0x0) = CONST 
    0x3aa: REVERT v3a7(0x0), v3a7(0x0)

    Begin block 0x3ab
    prev=[0x395], succ=[0x249b]
    =================================
    0x3ad: v3ad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c3: v3c3 = CALLDATALOAD v399(0x4)
    0x3c5: v3c5 = AND v3ad(0xffffffffffffffffffffffffffffffffffffffff), v3c3
    0x3c7: v3c7(0x20) = CONST 
    0x3ca: v3ca(0x24) = ADD v399(0x4), v3c7(0x20)
    0x3cb: v3cb = CALLDATALOAD v3ca(0x24)
    0x3cd: v3cd(0x40) = CONST 
    0x3d1: v3d1(0x44) = ADD v399(0x4), v3cd(0x40)
    0x3d2: v3d2 = CALLDATALOAD v3d1(0x44)
    0x3d3: v3d3 = AND v3d2, v3ad(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d4: v3d4(0x249b) = CONST 
    0x3d7: JUMP v3d4(0x249b)

    Begin block 0x249b
    prev=[0x3ab], succ=[]
    =================================
    0x249c: v249c(0x0) = CONST 
    0x249e: v249e(0x40) = CONST 
    0x24a0: v24a0 = MLOAD v249e(0x40)
    0x24a1: v24a1(0x461bcd) = CONST 
    0x24a5: v24a5(0xe5) = CONST 
    0x24a7: v24a7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v24a5(0xe5), v24a1(0x461bcd)
    0x24a9: MSTORE v24a0, v24a7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x24aa: v24aa(0x4) = CONST 
    0x24ac: v24ac = ADD v24aa(0x4), v24a0
    0x24af: v24af(0x20) = CONST 
    0x24b1: v24b1 = ADD v24af(0x20), v24ac
    0x24b4: v24b4(0x20) = SUB v24b1, v24ac
    0x24b6: MSTORE v24ac, v24b4(0x20)
    0x24b7: v24b7(0x2c) = CONST 
    0x24ba: MSTORE v24b1, v24b7(0x2c)
    0x24bb: v24bb(0x20) = CONST 
    0x24bd: v24bd = ADD v24bb(0x20), v24b1
    0x24bf: v24bf(0x2234) = CONST 
    0x24c2: v24c2(0x2c) = CONST 
    0x24c5: CODECOPY v24bd, v24bf(0x2234), v24c2(0x2c)
    0x24c6: v24c6(0x40) = CONST 
    0x24c8: v24c8 = ADD v24c6(0x40), v24bd
    0x24cc: v24cc(0x40) = CONST 
    0x24ce: v24ce = MLOAD v24cc(0x40)
    0x24d1: v24d1(0x84) = SUB v24c8, v24ce
    0x24d3: REVERT v24ce, v24d1(0x84)

}

function rounding()() public {
    Begin block 0x3d8
    prev=[], succ=[0x904]
    =================================
    0x3d9: v3d9(0x2677) = CONST 
    0x3dc: v3dc(0x904) = CONST 
    0x3df: JUMP v3dc(0x904)

    Begin block 0x904
    prev=[0x3d8], succ=[0x2677]
    =================================
    0x905: v905(0x2) = CONST 
    0x908: JUMP v3d9(0x2677)

    Begin block 0x2677
    prev=[0x904], succ=[]
    =================================
    0x2678: v2678(0x40) = CONST 
    0x267b: v267b = MLOAD v2678(0x40)
    0x267c: v267c(0xff) = CONST 
    0x2680: v2680(0x2) = AND v905(0x2), v267c(0xff)
    0x2682: MSTORE v267b, v2680(0x2)
    0x2683: v2683 = MLOAD v2678(0x40)
    0x2687: v2687(0x0) = SUB v267b, v2683
    0x2688: v2688(0x20) = CONST 
    0x268a: v268a(0x20) = ADD v2688(0x20), v2687(0x0)
    0x268c: RETURN v2683, v268a(0x20)

}

function decimals()() public {
    Begin block 0x3f6
    prev=[], succ=[0x909]
    =================================
    0x3f7: v3f7(0x26ac) = CONST 
    0x3fa: v3fa(0x909) = CONST 
    0x3fd: JUMP v3fa(0x909)

    Begin block 0x909
    prev=[0x3f6], succ=[0x26ac]
    =================================
    0x90a: v90a(0x12) = CONST 
    0x90d: JUMP v3f7(0x26ac)

    Begin block 0x26ac
    prev=[0x909], succ=[]
    =================================
    0x26ad: v26ad(0x40) = CONST 
    0x26b0: v26b0 = MLOAD v26ad(0x40)
    0x26b1: v26b1(0xff) = CONST 
    0x26b5: v26b5(0x12) = AND v90a(0x12), v26b1(0xff)
    0x26b7: MSTORE v26b0, v26b5(0x12)
    0x26b8: v26b8 = MLOAD v26ad(0x40)
    0x26bc: v26bc(0x0) = SUB v26b0, v26b8
    0x26bd: v26bd(0x20) = CONST 
    0x26bf: v26bf(0x20) = ADD v26bd(0x20), v26bc(0x0)
    0x26c1: RETURN v26b8, v26bf(0x20)

}

function canBurn(address)() public {
    Begin block 0x3fe
    prev=[], succ=[0x410, 0x414]
    =================================
    0x3ff: v3ff(0x26e1) = CONST 
    0x402: v402(0x4) = CONST 
    0x405: v405 = CALLDATASIZE 
    0x406: v406 = SUB v405, v402(0x4)
    0x407: v407(0x20) = CONST 
    0x40a: v40a = LT v406, v407(0x20)
    0x40b: v40b = ISZERO v40a
    0x40c: v40c(0x414) = CONST 
    0x40f: JUMPI v40c(0x414), v40b

    Begin block 0x410
    prev=[0x3fe], succ=[]
    =================================
    0x410: v410(0x0) = CONST 
    0x413: REVERT v410(0x0), v410(0x0)

    Begin block 0x414
    prev=[0x3fe], succ=[0x90e]
    =================================
    0x416: v416 = CALLDATALOAD v402(0x4)
    0x417: v417(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42c: v42c = AND v417(0xffffffffffffffffffffffffffffffffffffffff), v416
    0x42d: v42d(0x90e) = CONST 
    0x430: JUMP v42d(0x90e)

    Begin block 0x90e
    prev=[0x414], succ=[0x26e1]
    =================================
    0x90f: v90f(0x17) = CONST 
    0x911: v911(0x20) = CONST 
    0x913: MSTORE v911(0x20), v90f(0x17)
    0x914: v914(0x0) = CONST 
    0x918: MSTORE v914(0x0), v42c
    0x919: v919(0x40) = CONST 
    0x91c: v91c = SHA3 v914(0x0), v919(0x40)
    0x91d: v91d = SLOAD v91c
    0x91e: v91e(0xff) = CONST 
    0x920: v920 = AND v91e(0xff), v91d
    0x922: JUMP v3ff(0x26e1)

    Begin block 0x26e1
    prev=[0x90e], succ=[]
    =================================
    0x26e2: v26e2(0x40) = CONST 
    0x26e5: v26e5 = MLOAD v26e2(0x40)
    0x26e7: v26e7 = ISZERO v920
    0x26e8: v26e8 = ISZERO v26e7
    0x26ea: MSTORE v26e5, v26e8
    0x26eb: v26eb = MLOAD v26e2(0x40)
    0x26ef: v26ef(0x0) = SUB v26e5, v26eb
    0x26f0: v26f0(0x20) = CONST 
    0x26f2: v26f2(0x20) = ADD v26f0(0x20), v26ef(0x0)
    0x26f4: RETURN v26eb, v26f2(0x20)

}

function increaseAllowance(address,uint256)() public {
    Begin block 0x431
    prev=[], succ=[0x443, 0x447]
    =================================
    0x432: v432(0x2714) = CONST 
    0x435: v435(0x4) = CONST 
    0x438: v438 = CALLDATASIZE 
    0x439: v439 = SUB v438, v435(0x4)
    0x43a: v43a(0x40) = CONST 
    0x43d: v43d = LT v439, v43a(0x40)
    0x43e: v43e = ISZERO v43d
    0x43f: v43f(0x447) = CONST 
    0x442: JUMPI v43f(0x447), v43e

    Begin block 0x443
    prev=[0x431], succ=[]
    =================================
    0x443: v443(0x0) = CONST 
    0x446: REVERT v443(0x0), v443(0x0)

    Begin block 0x447
    prev=[0x431], succ=[0x923]
    =================================
    0x449: v449(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x45f: v45f = CALLDATALOAD v435(0x4)
    0x460: v460 = AND v45f, v449(0xffffffffffffffffffffffffffffffffffffffff)
    0x462: v462(0x20) = CONST 
    0x464: v464(0x24) = ADD v462(0x20), v435(0x4)
    0x465: v465 = CALLDATALOAD v464(0x24)
    0x466: v466(0x923) = CONST 
    0x469: JUMP v466(0x923)

    Begin block 0x923
    prev=[0x447], succ=[0x13a6B0x923]
    =================================
    0x924: v924(0x0) = CONST 
    0x926: v926(0x2b00) = CONST 
    0x929: v929(0x930) = CONST 
    0x92c: v92c(0x13a6) = CONST 
    0x92f: JUMP v92c(0x13a6)

    Begin block 0x13a6B0x923
    prev=[0x923], succ=[0x930]
    =================================
    0x13a7S0x923: v13a7V923 = CALLER 
    0x13a9S0x923: JUMP v929(0x930)

    Begin block 0x930
    prev=[0x13a6B0x923], succ=[0x13a6B0x930]
    =================================
    0x932: v932(0x2b28) = CONST 
    0x936: v936(0xf) = CONST 
    0x938: v938(0x0) = CONST 
    0x93a: v93a(0x941) = CONST 
    0x93d: v93d(0x13a6) = CONST 
    0x940: JUMP v93d(0x13a6)

    Begin block 0x13a6B0x930
    prev=[0x930], succ=[0x941]
    =================================
    0x13a7S0x930: v13a7V930 = CALLER 
    0x13a9S0x930: JUMP v93a(0x941)

    Begin block 0x941
    prev=[0x13a6B0x930], succ=[0x15a7B0x941]
    =================================
    0x942: v942(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x959: v959 = AND v942(0xffffffffffffffffffffffffffffffffffffffff), v13a7V930
    0x95b: MSTORE v938(0x0), v959
    0x95c: v95c(0x20) = CONST 
    0x960: v960(0x20) = ADD v938(0x0), v95c(0x20)
    0x964: MSTORE v960(0x20), v936(0xf)
    0x965: v965(0x40) = CONST 
    0x969: v969(0x40) = ADD v965(0x40), v938(0x0)
    0x96a: v96a(0x0) = CONST 
    0x96e: v96e = SHA3 v96a(0x0), v969(0x40)
    0x971: v971 = AND v460, v942(0xffffffffffffffffffffffffffffffffffffffff)
    0x973: MSTORE v96a(0x0), v971
    0x975: MSTORE v95c(0x20), v96e
    0x977: v977 = SHA3 v96a(0x0), v965(0x40)
    0x978: v978 = SLOAD v977
    0x97a: v97a(0xffffffff) = CONST 
    0x97f: v97f(0x15a7) = CONST 
    0x982: v982(0x15a7) = AND v97f(0x15a7), v97a(0xffffffff)
    0x983: JUMP v982(0x15a7)

    Begin block 0x15a7B0x941
    prev=[0x941], succ=[0x15b5B0x941, 0x2c50B0x941]
    =================================
    0x15a8S0x941: v15a8V941(0x0) = CONST 
    0x15acS0x941: v15acV941 = ADD v465, v978
    0x15afS0x941: v15afV941 = LT v15acV941, v978
    0x15b0S0x941: v15b0V941 = ISZERO v15afV941
    0x15b1S0x941: v15b1V941(0x2c50) = CONST 
    0x15b4S0x941: JUMPI v15b1V941(0x2c50), v15b0V941

    Begin block 0x15b5B0x941
    prev=[0x15a7B0x941], succ=[]
    =================================
    0x15b5S0x941: v15b5V941(0x40) = CONST 
    0x15b8S0x941: v15b8V941 = MLOAD v15b5V941(0x40)
    0x15b9S0x941: v15b9V941(0x461bcd) = CONST 
    0x15bdS0x941: v15bdV941(0xe5) = CONST 
    0x15bfS0x941: v15bfV941(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15bdV941(0xe5), v15b9V941(0x461bcd)
    0x15c1S0x941: MSTORE v15b8V941, v15bfV941(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15c2S0x941: v15c2V941(0x20) = CONST 
    0x15c4S0x941: v15c4V941(0x4) = CONST 
    0x15c7S0x941: v15c7V941 = ADD v15b8V941, v15c4V941(0x4)
    0x15c8S0x941: MSTORE v15c7V941, v15c2V941(0x20)
    0x15c9S0x941: v15c9V941(0x1b) = CONST 
    0x15cbS0x941: v15cbV941(0x24) = CONST 
    0x15ceS0x941: v15ceV941 = ADD v15b8V941, v15cbV941(0x24)
    0x15cfS0x941: MSTORE v15ceV941, v15c9V941(0x1b)
    0x15d0S0x941: v15d0V941(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x15f1S0x941: v15f1V941(0x44) = CONST 
    0x15f4S0x941: v15f4V941 = ADD v15b8V941, v15f1V941(0x44)
    0x15f5S0x941: MSTORE v15f4V941, v15d0V941(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x15f7S0x941: v15f7V941 = MLOAD v15b5V941(0x40)
    0x15fbS0x941: v15fbV941(0x0) = SUB v15b8V941, v15f7V941
    0x15fcS0x941: v15fcV941(0x64) = CONST 
    0x15feS0x941: v15feV941(0x64) = ADD v15fcV941(0x64), v15fbV941(0x0)
    0x1600S0x941: REVERT v15f7V941, v15feV941(0x64)

    Begin block 0x2c50B0x941
    prev=[0x15a7B0x941], succ=[0x2b28]
    =================================
    0x2c56S0x941: JUMP v932(0x2b28)

    Begin block 0x2b28
    prev=[0x2c50B0x941], succ=[0x2b00]
    =================================
    0x2b29: v2b29(0x13aa) = CONST 
    0x2b2c: CALLPRIVATE v2b29(0x13aa), v15acV941, v460, v13a7V923, v926(0x2b00)

    Begin block 0x2b00
    prev=[0x2b28], succ=[0x2714]
    =================================
    0x2b02: v2b02(0x1) = CONST 
    0x2b08: JUMP v432(0x2714)

    Begin block 0x2714
    prev=[0x2b00], succ=[]
    =================================
    0x2715: v2715(0x40) = CONST 
    0x2718: v2718 = MLOAD v2715(0x40)
    0x271a: v271a = ISZERO v2b02(0x1)
    0x271b: v271b = ISZERO v271a
    0x271d: MSTORE v2718, v271b
    0x271e: v271e = MLOAD v2715(0x40)
    0x2722: v2722(0x0) = SUB v2718, v271e
    0x2723: v2723(0x20) = CONST 
    0x2725: v2725(0x20) = ADD v2723(0x20), v2722(0x0)
    0x2727: RETURN v271e, v2725(0x20)

}

function mint(address,uint256)() public {
    Begin block 0x46a
    prev=[], succ=[0x47c, 0x480]
    =================================
    0x46b: v46b(0x2747) = CONST 
    0x46e: v46e(0x4) = CONST 
    0x471: v471 = CALLDATASIZE 
    0x472: v472 = SUB v471, v46e(0x4)
    0x473: v473(0x40) = CONST 
    0x476: v476 = LT v472, v473(0x40)
    0x477: v477 = ISZERO v476
    0x478: v478(0x480) = CONST 
    0x47b: JUMPI v478(0x480), v477

    Begin block 0x47c
    prev=[0x46a], succ=[]
    =================================
    0x47c: v47c(0x0) = CONST 
    0x47f: REVERT v47c(0x0), v47c(0x0)

    Begin block 0x480
    prev=[0x46a], succ=[0x984]
    =================================
    0x482: v482(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x498: v498 = CALLDATALOAD v46e(0x4)
    0x499: v499 = AND v498, v482(0xffffffffffffffffffffffffffffffffffffffff)
    0x49b: v49b(0x20) = CONST 
    0x49d: v49d(0x24) = ADD v49b(0x20), v46e(0x4)
    0x49e: v49e = CALLDATALOAD v49d(0x24)
    0x49f: v49f(0x984) = CONST 
    0x4a2: JUMP v49f(0x984)

    Begin block 0x984
    prev=[0x480], succ=[0x9a4, 0x9f0]
    =================================
    0x985: v985(0x0) = CONST 
    0x987: v987 = SLOAD v985(0x0)
    0x988: v988(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x99d: v99d = AND v988(0xffffffffffffffffffffffffffffffffffffffff), v987
    0x99e: v99e = CALLER 
    0x99f: v99f = EQ v99e, v99d
    0x9a0: v9a0(0x9f0) = CONST 
    0x9a3: JUMPI v9a0(0x9f0), v99f

    Begin block 0x9a4
    prev=[0x984], succ=[]
    =================================
    0x9a4: v9a4(0x40) = CONST 
    0x9a7: v9a7 = MLOAD v9a4(0x40)
    0x9a8: v9a8(0x461bcd) = CONST 
    0x9ac: v9ac(0xe5) = CONST 
    0x9ae: v9ae(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v9ac(0xe5), v9a8(0x461bcd)
    0x9b0: MSTORE v9a7, v9ae(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9b1: v9b1(0x20) = CONST 
    0x9b3: v9b3(0x4) = CONST 
    0x9b6: v9b6 = ADD v9a7, v9b3(0x4)
    0x9b7: MSTORE v9b6, v9b1(0x20)
    0x9b8: v9b8(0xa) = CONST 
    0x9ba: v9ba(0x24) = CONST 
    0x9bd: v9bd = ADD v9a7, v9ba(0x24)
    0x9be: MSTORE v9bd, v9b8(0xa)
    0x9bf: v9bf(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0x9e0: v9e0(0x44) = CONST 
    0x9e3: v9e3 = ADD v9a7, v9e0(0x44)
    0x9e4: MSTORE v9e3, v9bf(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0x9e6: v9e6 = MLOAD v9a4(0x40)
    0x9ea: v9ea(0x0) = SUB v9a7, v9e6
    0x9eb: v9eb(0x64) = CONST 
    0x9ed: v9ed(0x64) = ADD v9eb(0x64), v9ea(0x0)
    0x9ef: REVERT v9e6, v9ed(0x64)

    Begin block 0x9f0
    prev=[0x984], succ=[0xa1f, 0xa55]
    =================================
    0x9f1: v9f1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa07: va07 = AND v499, v9f1(0xffffffffffffffffffffffffffffffffffffffff)
    0xa08: va08(0x0) = CONST 
    0xa0c: MSTORE va08(0x0), va07
    0xa0d: va0d(0x16) = CONST 
    0xa0f: va0f(0x20) = CONST 
    0xa11: MSTORE va0f(0x20), va0d(0x16)
    0xa12: va12(0x40) = CONST 
    0xa15: va15 = SHA3 va08(0x0), va12(0x40)
    0xa16: va16 = SLOAD va15
    0xa17: va17(0xff) = CONST 
    0xa19: va19 = AND va17(0xff), va16
    0xa1a: va1a = ISZERO va19
    0xa1b: va1b(0xa55) = CONST 
    0xa1e: JUMPI va1b(0xa55), va1a

    Begin block 0xa1f
    prev=[0x9f0], succ=[]
    =================================
    0xa1f: va1f(0x40) = CONST 
    0xa21: va21 = MLOAD va1f(0x40)
    0xa22: va22(0x461bcd) = CONST 
    0xa26: va26(0xe5) = CONST 
    0xa28: va28(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL va26(0xe5), va22(0x461bcd)
    0xa2a: MSTORE va21, va28(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa2b: va2b(0x4) = CONST 
    0xa2d: va2d = ADD va2b(0x4), va21
    0xa30: va30(0x20) = CONST 
    0xa32: va32 = ADD va30(0x20), va2d
    0xa35: va35(0x20) = SUB va32, va2d
    0xa37: MSTORE va2d, va35(0x20)
    0xa38: va38(0x24) = CONST 
    0xa3b: MSTORE va32, va38(0x24)
    0xa3c: va3c(0x20) = CONST 
    0xa3e: va3e = ADD va3c(0x20), va32
    0xa40: va40(0x2058) = CONST 
    0xa43: va43(0x24) = CONST 
    0xa46: CODECOPY va3e, va40(0x2058), va43(0x24)
    0xa47: va47(0x40) = CONST 
    0xa49: va49 = ADD va47(0x40), va3e
    0xa4d: va4d(0x40) = CONST 
    0xa4f: va4f = MLOAD va4d(0x40)
    0xa52: va52(0x84) = SUB va49, va4f
    0xa54: REVERT va4f, va52(0x84)

    Begin block 0xa55
    prev=[0x9f0], succ=[0xa5e]
    =================================
    0xa56: va56(0xa5e) = CONST 
    0xa5a: va5a(0x1601) = CONST 
    0xa5d: va5d_0 = CALLPRIVATE va5a(0x1601), v499, va56(0xa5e)

    Begin block 0xa5e
    prev=[0xa55], succ=[0xa64, 0xa9a]
    =================================
    0xa5f: va5f = ISZERO va5d_0
    0xa60: va60(0xa9a) = CONST 
    0xa63: JUMPI va60(0xa9a), va5f

    Begin block 0xa64
    prev=[0xa5e], succ=[]
    =================================
    0xa64: va64(0x40) = CONST 
    0xa66: va66 = MLOAD va64(0x40)
    0xa67: va67(0x461bcd) = CONST 
    0xa6b: va6b(0xe5) = CONST 
    0xa6d: va6d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL va6b(0xe5), va67(0x461bcd)
    0xa6f: MSTORE va66, va6d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa70: va70(0x4) = CONST 
    0xa72: va72 = ADD va70(0x4), va66
    0xa75: va75(0x20) = CONST 
    0xa77: va77 = ADD va75(0x20), va72
    0xa7a: va7a(0x20) = SUB va77, va72
    0xa7c: MSTORE va72, va7a(0x20)
    0xa7d: va7d(0x2d) = CONST 
    0xa80: MSTORE va77, va7d(0x2d)
    0xa81: va81(0x20) = CONST 
    0xa83: va83 = ADD va81(0x20), va77
    0xa85: va85(0x213b) = CONST 
    0xa88: va88(0x2d) = CONST 
    0xa8b: CODECOPY va83, va85(0x213b), va88(0x2d)
    0xa8c: va8c(0x40) = CONST 
    0xa8e: va8e = ADD va8c(0x40), va83
    0xa92: va92(0x40) = CONST 
    0xa94: va94 = MLOAD va92(0x40)
    0xa97: va97(0x84) = SUB va8e, va94
    0xa99: REVERT va94, va97(0x84)

    Begin block 0xa9a
    prev=[0xa5e], succ=[0x1642]
    =================================
    0xa9b: va9b(0xaa4) = CONST 
    0xaa0: vaa0(0x1642) = CONST 
    0xaa3: JUMP vaa0(0x1642)

    Begin block 0x1642
    prev=[0xa9a], succ=[0x165e, 0x16aa]
    =================================
    0x1643: v1643(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1659: v1659 = AND v499, v1643(0xffffffffffffffffffffffffffffffffffffffff)
    0x165a: v165a(0x16aa) = CONST 
    0x165d: JUMPI v165a(0x16aa), v1659

    Begin block 0x165e
    prev=[0x1642], succ=[]
    =================================
    0x165e: v165e(0x40) = CONST 
    0x1661: v1661 = MLOAD v165e(0x40)
    0x1662: v1662(0x461bcd) = CONST 
    0x1666: v1666(0xe5) = CONST 
    0x1668: v1668(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1666(0xe5), v1662(0x461bcd)
    0x166a: MSTORE v1661, v1668(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x166b: v166b(0x20) = CONST 
    0x166d: v166d(0x4) = CONST 
    0x1670: v1670 = ADD v1661, v166d(0x4)
    0x1671: MSTORE v1670, v166b(0x20)
    0x1672: v1672(0x1f) = CONST 
    0x1674: v1674(0x24) = CONST 
    0x1677: v1677 = ADD v1661, v1674(0x24)
    0x1678: MSTORE v1677, v1672(0x1f)
    0x1679: v1679(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300) = CONST 
    0x169a: v169a(0x44) = CONST 
    0x169d: v169d = ADD v1661, v169a(0x44)
    0x169e: MSTORE v169d, v1679(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300)
    0x16a0: v16a0 = MLOAD v165e(0x40)
    0x16a4: v16a4(0x0) = SUB v1661, v16a0
    0x16a5: v16a5(0x64) = CONST 
    0x16a7: v16a7(0x64) = ADD v16a5(0x64), v16a4(0x0)
    0x16a9: REVERT v16a0, v16a7(0x64)

    Begin block 0x16aa
    prev=[0x1642], succ=[0x2c9bB0x16aa]
    =================================
    0x16ab: v16ab(0x16b6) = CONST 
    0x16ae: v16ae(0x0) = CONST 
    0x16b2: v16b2(0x2c9b) = CONST 
    0x16b5: JUMP v16b2(0x2c9b), v49e, v499, v16ae(0x0), v16ab(0x16b6)

    Begin block 0x2c9bB0x16aa
    prev=[0x16aa], succ=[0x16b6]
    =================================
    0x2c9fS0x16aa: JUMP v16ab(0x16b6)

    Begin block 0x16b6
    prev=[0x2c9bB0x16aa], succ=[0x15a7B0x16b6]
    =================================
    0x16b7: v16b7(0x4) = CONST 
    0x16b9: v16b9 = SLOAD v16b7(0x4)
    0x16ba: v16ba(0x16c9) = CONST 
    0x16bf: v16bf(0xffffffff) = CONST 
    0x16c4: v16c4(0x15a7) = CONST 
    0x16c7: v16c7(0x15a7) = AND v16c4(0x15a7), v16bf(0xffffffff)
    0x16c8: JUMP v16c7(0x15a7)

    Begin block 0x15a7B0x16b6
    prev=[0x16b6], succ=[0x15b5B0x16b6, 0x2c50B0x16b6]
    =================================
    0x15a8S0x16b6: v15a8V16b6(0x0) = CONST 
    0x15acS0x16b6: v15acV16b6 = ADD v49e, v16b9
    0x15afS0x16b6: v15afV16b6 = LT v15acV16b6, v16b9
    0x15b0S0x16b6: v15b0V16b6 = ISZERO v15afV16b6
    0x15b1S0x16b6: v15b1V16b6(0x2c50) = CONST 
    0x15b4S0x16b6: JUMPI v15b1V16b6(0x2c50), v15b0V16b6

    Begin block 0x15b5B0x16b6
    prev=[0x15a7B0x16b6], succ=[]
    =================================
    0x15b5S0x16b6: v15b5V16b6(0x40) = CONST 
    0x15b8S0x16b6: v15b8V16b6 = MLOAD v15b5V16b6(0x40)
    0x15b9S0x16b6: v15b9V16b6(0x461bcd) = CONST 
    0x15bdS0x16b6: v15bdV16b6(0xe5) = CONST 
    0x15bfS0x16b6: v15bfV16b6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15bdV16b6(0xe5), v15b9V16b6(0x461bcd)
    0x15c1S0x16b6: MSTORE v15b8V16b6, v15bfV16b6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15c2S0x16b6: v15c2V16b6(0x20) = CONST 
    0x15c4S0x16b6: v15c4V16b6(0x4) = CONST 
    0x15c7S0x16b6: v15c7V16b6 = ADD v15b8V16b6, v15c4V16b6(0x4)
    0x15c8S0x16b6: MSTORE v15c7V16b6, v15c2V16b6(0x20)
    0x15c9S0x16b6: v15c9V16b6(0x1b) = CONST 
    0x15cbS0x16b6: v15cbV16b6(0x24) = CONST 
    0x15ceS0x16b6: v15ceV16b6 = ADD v15b8V16b6, v15cbV16b6(0x24)
    0x15cfS0x16b6: MSTORE v15ceV16b6, v15c9V16b6(0x1b)
    0x15d0S0x16b6: v15d0V16b6(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x15f1S0x16b6: v15f1V16b6(0x44) = CONST 
    0x15f4S0x16b6: v15f4V16b6 = ADD v15b8V16b6, v15f1V16b6(0x44)
    0x15f5S0x16b6: MSTORE v15f4V16b6, v15d0V16b6(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x15f7S0x16b6: v15f7V16b6 = MLOAD v15b5V16b6(0x40)
    0x15fbS0x16b6: v15fbV16b6(0x0) = SUB v15b8V16b6, v15f7V16b6
    0x15fcS0x16b6: v15fcV16b6(0x64) = CONST 
    0x15feS0x16b6: v15feV16b6(0x64) = ADD v15fcV16b6(0x64), v15fbV16b6(0x0)
    0x1600S0x16b6: REVERT v15f7V16b6, v15feV16b6(0x64)

    Begin block 0x2c50B0x16b6
    prev=[0x15a7B0x16b6], succ=[0x16c9]
    =================================
    0x2c56S0x16b6: JUMP v16ba(0x16c9)

    Begin block 0x16c9
    prev=[0x2c50B0x16b6], succ=[0x15a7B0x16c9]
    =================================
    0x16ca: v16ca(0x4) = CONST 
    0x16cc: SSTORE v16ca(0x4), v15acV16b6
    0x16cd: v16cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16e3: v16e3 = AND v499, v16cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x16e4: v16e4(0x0) = CONST 
    0x16e8: MSTORE v16e4(0x0), v16e3
    0x16e9: v16e9(0xe) = CONST 
    0x16eb: v16eb(0x20) = CONST 
    0x16ed: MSTORE v16eb(0x20), v16e9(0xe)
    0x16ee: v16ee(0x40) = CONST 
    0x16f1: v16f1 = SHA3 v16e4(0x0), v16ee(0x40)
    0x16f2: v16f2 = SLOAD v16f1
    0x16f3: v16f3(0x1702) = CONST 
    0x16f8: v16f8(0xffffffff) = CONST 
    0x16fd: v16fd(0x15a7) = CONST 
    0x1700: v1700(0x15a7) = AND v16fd(0x15a7), v16f8(0xffffffff)
    0x1701: JUMP v1700(0x15a7)

    Begin block 0x15a7B0x16c9
    prev=[0x16c9], succ=[0x15b5B0x16c9, 0x2c50B0x16c9]
    =================================
    0x15a8S0x16c9: v15a8V16c9(0x0) = CONST 
    0x15acS0x16c9: v15acV16c9 = ADD v49e, v16f2
    0x15afS0x16c9: v15afV16c9 = LT v15acV16c9, v16f2
    0x15b0S0x16c9: v15b0V16c9 = ISZERO v15afV16c9
    0x15b1S0x16c9: v15b1V16c9(0x2c50) = CONST 
    0x15b4S0x16c9: JUMPI v15b1V16c9(0x2c50), v15b0V16c9

    Begin block 0x15b5B0x16c9
    prev=[0x15a7B0x16c9], succ=[]
    =================================
    0x15b5S0x16c9: v15b5V16c9(0x40) = CONST 
    0x15b8S0x16c9: v15b8V16c9 = MLOAD v15b5V16c9(0x40)
    0x15b9S0x16c9: v15b9V16c9(0x461bcd) = CONST 
    0x15bdS0x16c9: v15bdV16c9(0xe5) = CONST 
    0x15bfS0x16c9: v15bfV16c9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15bdV16c9(0xe5), v15b9V16c9(0x461bcd)
    0x15c1S0x16c9: MSTORE v15b8V16c9, v15bfV16c9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15c2S0x16c9: v15c2V16c9(0x20) = CONST 
    0x15c4S0x16c9: v15c4V16c9(0x4) = CONST 
    0x15c7S0x16c9: v15c7V16c9 = ADD v15b8V16c9, v15c4V16c9(0x4)
    0x15c8S0x16c9: MSTORE v15c7V16c9, v15c2V16c9(0x20)
    0x15c9S0x16c9: v15c9V16c9(0x1b) = CONST 
    0x15cbS0x16c9: v15cbV16c9(0x24) = CONST 
    0x15ceS0x16c9: v15ceV16c9 = ADD v15b8V16c9, v15cbV16c9(0x24)
    0x15cfS0x16c9: MSTORE v15ceV16c9, v15c9V16c9(0x1b)
    0x15d0S0x16c9: v15d0V16c9(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x15f1S0x16c9: v15f1V16c9(0x44) = CONST 
    0x15f4S0x16c9: v15f4V16c9 = ADD v15b8V16c9, v15f1V16c9(0x44)
    0x15f5S0x16c9: MSTORE v15f4V16c9, v15d0V16c9(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x15f7S0x16c9: v15f7V16c9 = MLOAD v15b5V16c9(0x40)
    0x15fbS0x16c9: v15fbV16c9(0x0) = SUB v15b8V16c9, v15f7V16c9
    0x15fcS0x16c9: v15fcV16c9(0x64) = CONST 
    0x15feS0x16c9: v15feV16c9(0x64) = ADD v15fcV16c9(0x64), v15fbV16c9(0x0)
    0x1600S0x16c9: REVERT v15f7V16c9, v15feV16c9(0x64)

    Begin block 0x2c50B0x16c9
    prev=[0x15a7B0x16c9], succ=[0x1702]
    =================================
    0x2c56S0x16c9: JUMP v16f3(0x1702)

    Begin block 0x1702
    prev=[0x2c50B0x16c9], succ=[0xaa4]
    =================================
    0x1703: v1703(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1719: v1719 = AND v499, v1703(0xffffffffffffffffffffffffffffffffffffffff)
    0x171a: v171a(0x0) = CONST 
    0x171e: MSTORE v171a(0x0), v1719
    0x171f: v171f(0xe) = CONST 
    0x1721: v1721(0x20) = CONST 
    0x1725: MSTORE v1721(0x20), v171f(0xe)
    0x1726: v1726(0x40) = CONST 
    0x172a: v172a = SHA3 v171a(0x0), v1726(0x40)
    0x172e: SSTORE v172a, v15acV16c9
    0x1730: v1730 = MLOAD v1726(0x40)
    0x1733: MSTORE v1730, v49e
    0x1735: v1735 = MLOAD v1726(0x40)
    0x173a: v173a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x175e: v175e(0x0) = SUB v1730, v1735
    0x1761: v1761(0x20) = ADD v1721(0x20), v175e(0x0)
    0x1763: LOG3 v1735, v1761(0x20), v173a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v171a(0x0), v1719
    0x1766: JUMP va9b(0xaa4)

    Begin block 0xaa4
    prev=[0x1702], succ=[0x2747]
    =================================
    0xaa5: vaa5(0x40) = CONST 
    0xaa8: vaa8 = MLOAD vaa5(0x40)
    0xaab: MSTORE vaa8, v49e
    0xaad: vaad = MLOAD vaa5(0x40)
    0xaae: vaae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xac4: vac4 = AND v499, vaae(0xffffffffffffffffffffffffffffffffffffffff)
    0xac6: vac6(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0xaeb: vaeb(0x0) = SUB vaa8, vaad
    0xaec: vaec(0x20) = CONST 
    0xaee: vaee(0x20) = ADD vaec(0x20), vaeb(0x0)
    0xaf0: LOG2 vaad, vaee(0x20), vac6(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), vac4
    0xaf3: JUMP v46b(0x2747)

    Begin block 0x2747
    prev=[0xaa4], succ=[]
    =================================
    0x2748: STOP 

}

function burn(uint256)() public {
    Begin block 0x4a5
    prev=[], succ=[0x4b7, 0x4bb]
    =================================
    0x4a6: v4a6(0x2768) = CONST 
    0x4a9: v4a9(0x4) = CONST 
    0x4ac: v4ac = CALLDATASIZE 
    0x4ad: v4ad = SUB v4ac, v4a9(0x4)
    0x4ae: v4ae(0x20) = CONST 
    0x4b1: v4b1 = LT v4ad, v4ae(0x20)
    0x4b2: v4b2 = ISZERO v4b1
    0x4b3: v4b3(0x4bb) = CONST 
    0x4b6: JUMPI v4b3(0x4bb), v4b2

    Begin block 0x4b7
    prev=[0x4a5], succ=[]
    =================================
    0x4b7: v4b7(0x0) = CONST 
    0x4ba: REVERT v4b7(0x0), v4b7(0x0)

    Begin block 0x4bb
    prev=[0x4a5], succ=[0xaf4]
    =================================
    0x4bd: v4bd = CALLDATALOAD v4a9(0x4)
    0x4be: v4be(0xaf4) = CONST 
    0x4c1: JUMP v4be(0xaf4)

    Begin block 0xaf4
    prev=[0x4bb], succ=[0xafe]
    =================================
    0xaf5: vaf5(0xafe) = CONST 
    0xaf8: vaf8 = CALLER 
    0xafa: vafa(0x1767) = CONST 
    0xafd: CALLPRIVATE vafa(0x1767), v4bd, vaf8, vaf5(0xafe)

    Begin block 0xafe
    prev=[0xaf4], succ=[0x2768]
    =================================
    0xb00: JUMP v4a6(0x2768)

    Begin block 0x2768
    prev=[0xafe], succ=[]
    =================================
    0x2769: STOP 

}

function delegateBalanceOf(address)() public {
    Begin block 0x4c2
    prev=[], succ=[0x4d4, 0x4d8]
    =================================
    0x4c3: v4c3(0x2789) = CONST 
    0x4c6: v4c6(0x4) = CONST 
    0x4c9: v4c9 = CALLDATASIZE 
    0x4ca: v4ca = SUB v4c9, v4c6(0x4)
    0x4cb: v4cb(0x20) = CONST 
    0x4ce: v4ce = LT v4ca, v4cb(0x20)
    0x4cf: v4cf = ISZERO v4ce
    0x4d0: v4d0(0x4d8) = CONST 
    0x4d3: JUMPI v4d0(0x4d8), v4cf

    Begin block 0x4d4
    prev=[0x4c2], succ=[]
    =================================
    0x4d4: v4d4(0x0) = CONST 
    0x4d7: REVERT v4d4(0x0), v4d4(0x0)

    Begin block 0x4d8
    prev=[0x4c2], succ=[0xb01]
    =================================
    0x4da: v4da = CALLDATALOAD v4c6(0x4)
    0x4db: v4db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4f0: v4f0 = AND v4db(0xffffffffffffffffffffffffffffffffffffffff), v4da
    0x4f1: v4f1(0xb01) = CONST 
    0x4f4: JUMP v4f1(0xb01)

    Begin block 0xb01
    prev=[0x4d8], succ=[0xd0e0x4c2]
    =================================
    0xb02: vb02(0x0) = CONST 
    0xb04: vb04(0x2b4c) = CONST 
    0xb08: vb08(0xd0e) = CONST 
    0xb0b: JUMP vb08(0xd0e)

    Begin block 0xd0e0x4c2
    prev=[0xb01], succ=[0x2b4c]
    =================================
    0xd0f0x4c2: v4c2d0f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd240x4c2: v4c2d24 = AND v4c2d0f(0xffffffffffffffffffffffffffffffffffffffff), v4f0
    0xd250x4c2: v4c2d25(0x0) = CONST 
    0xd290x4c2: MSTORE v4c2d25(0x0), v4c2d24
    0xd2a0x4c2: v4c2d2a(0xe) = CONST 
    0xd2c0x4c2: v4c2d2c(0x20) = CONST 
    0xd2e0x4c2: MSTORE v4c2d2c(0x20), v4c2d2a(0xe)
    0xd2f0x4c2: v4c2d2f(0x40) = CONST 
    0xd320x4c2: v4c2d32 = SHA3 v4c2d25(0x0), v4c2d2f(0x40)
    0xd330x4c2: v4c2d33 = SLOAD v4c2d32
    0xd350x4c2: JUMP vb04(0x2b4c)

    Begin block 0x2b4c
    prev=[0xd0e0x4c2], succ=[0x2789]
    =================================
    0x2b51: JUMP v4c3(0x2789)

    Begin block 0x2789
    prev=[0x2b4c], succ=[]
    =================================
    0x278a: v278a(0x40) = CONST 
    0x278d: v278d = MLOAD v278a(0x40)
    0x2790: MSTORE v278d, v4c2d33
    0x2791: v2791 = MLOAD v278a(0x40)
    0x2795: v2795(0x0) = SUB v278d, v2791
    0x2796: v2796(0x20) = CONST 
    0x2798: v2798(0x20) = ADD v2796(0x20), v2795(0x0)
    0x279a: RETURN v2791, v2798(0x20)

}

function delegateTransferFrom(address,address,uint256,address)() public {
    Begin block 0x4f5
    prev=[], succ=[0x507, 0x50b]
    =================================
    0x4f6: v4f6(0x27ba) = CONST 
    0x4f9: v4f9(0x4) = CONST 
    0x4fc: v4fc = CALLDATASIZE 
    0x4fd: v4fd = SUB v4fc, v4f9(0x4)
    0x4fe: v4fe(0x80) = CONST 
    0x501: v501 = LT v4fd, v4fe(0x80)
    0x502: v502 = ISZERO v501
    0x503: v503(0x50b) = CONST 
    0x506: JUMPI v503(0x50b), v502

    Begin block 0x507
    prev=[0x4f5], succ=[]
    =================================
    0x507: v507(0x0) = CONST 
    0x50a: REVERT v507(0x0), v507(0x0)

    Begin block 0x50b
    prev=[0x4f5], succ=[0x24f3]
    =================================
    0x50d: v50d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x523: v523 = CALLDATALOAD v4f9(0x4)
    0x525: v525 = AND v50d(0xffffffffffffffffffffffffffffffffffffffff), v523
    0x527: v527(0x20) = CONST 
    0x52a: v52a(0x24) = ADD v4f9(0x4), v527(0x20)
    0x52b: v52b = CALLDATALOAD v52a(0x24)
    0x52d: v52d = AND v50d(0xffffffffffffffffffffffffffffffffffffffff), v52b
    0x52f: v52f(0x40) = CONST 
    0x532: v532(0x44) = ADD v4f9(0x4), v52f(0x40)
    0x533: v533 = CALLDATALOAD v532(0x44)
    0x535: v535(0x60) = CONST 
    0x537: v537(0x64) = ADD v535(0x60), v4f9(0x4)
    0x538: v538 = CALLDATALOAD v537(0x64)
    0x539: v539 = AND v538, v50d(0xffffffffffffffffffffffffffffffffffffffff)
    0x53a: v53a(0x24f3) = CONST 
    0x53d: JUMP v53a(0x24f3)

    Begin block 0x24f3
    prev=[0x50b], succ=[]
    =================================
    0x24f4: v24f4(0x0) = CONST 
    0x24f6: v24f6(0x40) = CONST 
    0x24f8: v24f8 = MLOAD v24f6(0x40)
    0x24f9: v24f9(0x461bcd) = CONST 
    0x24fd: v24fd(0xe5) = CONST 
    0x24ff: v24ff(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v24fd(0xe5), v24f9(0x461bcd)
    0x2501: MSTORE v24f8, v24ff(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2502: v2502(0x4) = CONST 
    0x2504: v2504 = ADD v2502(0x4), v24f8
    0x2507: v2507(0x20) = CONST 
    0x2509: v2509 = ADD v2507(0x20), v2504
    0x250c: v250c(0x20) = SUB v2509, v2504
    0x250e: MSTORE v2504, v250c(0x20)
    0x250f: v250f(0x2c) = CONST 
    0x2512: MSTORE v2509, v250f(0x2c)
    0x2513: v2513(0x20) = CONST 
    0x2515: v2515 = ADD v2513(0x20), v2509
    0x2517: v2517(0x2234) = CONST 
    0x251a: v251a(0x2c) = CONST 
    0x251d: CODECOPY v2515, v2517(0x2234), v251a(0x2c)
    0x251e: v251e(0x40) = CONST 
    0x2520: v2520 = ADD v251e(0x40), v2515
    0x2524: v2524(0x40) = CONST 
    0x2526: v2526 = MLOAD v2524(0x40)
    0x2529: v2529(0x84) = SUB v2520, v2526
    0x252b: REVERT v2526, v2529(0x84)

}

function claimOwnership()() public {
    Begin block 0x53e
    prev=[], succ=[0xb12]
    =================================
    0x53f: v53f(0x27ed) = CONST 
    0x542: v542(0xb12) = CONST 
    0x545: JUMP v542(0xb12)

    Begin block 0xb12
    prev=[0x53e], succ=[0xb32, 0xb7e]
    =================================
    0xb13: vb13(0x1) = CONST 
    0xb15: vb15 = SLOAD vb13(0x1)
    0xb16: vb16(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb2b: vb2b = AND vb16(0xffffffffffffffffffffffffffffffffffffffff), vb15
    0xb2c: vb2c = CALLER 
    0xb2d: vb2d = EQ vb2c, vb2b
    0xb2e: vb2e(0xb7e) = CONST 
    0xb31: JUMPI vb2e(0xb7e), vb2d

    Begin block 0xb32
    prev=[0xb12], succ=[]
    =================================
    0xb32: vb32(0x40) = CONST 
    0xb35: vb35 = MLOAD vb32(0x40)
    0xb36: vb36(0x461bcd) = CONST 
    0xb3a: vb3a(0xe5) = CONST 
    0xb3c: vb3c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vb3a(0xe5), vb36(0x461bcd)
    0xb3e: MSTORE vb35, vb3c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb3f: vb3f(0x20) = CONST 
    0xb41: vb41(0x4) = CONST 
    0xb44: vb44 = ADD vb35, vb41(0x4)
    0xb45: MSTORE vb44, vb3f(0x20)
    0xb46: vb46(0x12) = CONST 
    0xb48: vb48(0x24) = CONST 
    0xb4b: vb4b = ADD vb35, vb48(0x24)
    0xb4c: MSTORE vb4b, vb46(0x12)
    0xb4d: vb4d(0x6f6e6c792070656e64696e67206f776e65720000000000000000000000000000) = CONST 
    0xb6e: vb6e(0x44) = CONST 
    0xb71: vb71 = ADD vb35, vb6e(0x44)
    0xb72: MSTORE vb71, vb4d(0x6f6e6c792070656e64696e67206f776e65720000000000000000000000000000)
    0xb74: vb74 = MLOAD vb32(0x40)
    0xb78: vb78(0x0) = SUB vb35, vb74
    0xb79: vb79(0x64) = CONST 
    0xb7b: vb7b(0x64) = ADD vb79(0x64), vb78(0x0)
    0xb7d: REVERT vb74, vb7b(0x64)

    Begin block 0xb7e
    prev=[0xb12], succ=[0x27ed]
    =================================
    0xb7f: vb7f(0x1) = CONST 
    0xb81: vb81 = SLOAD vb7f(0x1)
    0xb82: vb82(0x0) = CONST 
    0xb85: vb85 = SLOAD vb82(0x0)
    0xb86: vb86(0x40) = CONST 
    0xb88: vb88 = MLOAD vb86(0x40)
    0xb89: vb89(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xba0: vba0 = AND vb89(0xffffffffffffffffffffffffffffffffffffffff), vb81
    0xba4: vba4 = AND vb85, vb89(0xffffffffffffffffffffffffffffffffffffffff)
    0xba6: vba6(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xbc8: LOG3 vb88, vb82(0x0), vba6(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vba4, vba0
    0xbc9: vbc9(0x1) = CONST 
    0xbcc: vbcc = SLOAD vbc9(0x1)
    0xbcd: vbcd(0x0) = CONST 
    0xbd0: vbd0 = SLOAD vbcd(0x0)
    0xbd1: vbd1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xbf4: vbf4 = AND vbd1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbd0
    0xbf5: vbf5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc0b: vc0b = AND vbcc, vbf5(0xffffffffffffffffffffffffffffffffffffffff)
    0xc0c: vc0c = OR vc0b, vbf4
    0xc0f: SSTORE vbcd(0x0), vc0c
    0xc10: vc10 = AND vbd1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbcc
    0xc12: SSTORE vbc9(0x1), vc10
    0xc13: JUMP v53f(0x27ed)

    Begin block 0x27ed
    prev=[0xb7e], succ=[]
    =================================
    0x27ee: STOP 

}

function setBurnBounds(uint256,uint256)() public {
    Begin block 0x546
    prev=[], succ=[0x558, 0x55c]
    =================================
    0x547: v547(0x280e) = CONST 
    0x54a: v54a(0x4) = CONST 
    0x54d: v54d = CALLDATASIZE 
    0x54e: v54e = SUB v54d, v54a(0x4)
    0x54f: v54f(0x40) = CONST 
    0x552: v552 = LT v54e, v54f(0x40)
    0x553: v553 = ISZERO v552
    0x554: v554(0x55c) = CONST 
    0x557: JUMPI v554(0x55c), v553

    Begin block 0x558
    prev=[0x546], succ=[]
    =================================
    0x558: v558(0x0) = CONST 
    0x55b: REVERT v558(0x0), v558(0x0)

    Begin block 0x55c
    prev=[0x546], succ=[0xc14]
    =================================
    0x55f: v55f = CALLDATALOAD v54a(0x4)
    0x561: v561(0x20) = CONST 
    0x563: v563(0x24) = ADD v561(0x20), v54a(0x4)
    0x564: v564 = CALLDATALOAD v563(0x24)
    0x565: v565(0xc14) = CONST 
    0x568: JUMP v565(0xc14)

    Begin block 0xc14
    prev=[0x55c], succ=[0xc34, 0xc80]
    =================================
    0xc15: vc15(0x0) = CONST 
    0xc17: vc17 = SLOAD vc15(0x0)
    0xc18: vc18(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc2d: vc2d = AND vc18(0xffffffffffffffffffffffffffffffffffffffff), vc17
    0xc2e: vc2e = CALLER 
    0xc2f: vc2f = EQ vc2e, vc2d
    0xc30: vc30(0xc80) = CONST 
    0xc33: JUMPI vc30(0xc80), vc2f

    Begin block 0xc34
    prev=[0xc14], succ=[]
    =================================
    0xc34: vc34(0x40) = CONST 
    0xc37: vc37 = MLOAD vc34(0x40)
    0xc38: vc38(0x461bcd) = CONST 
    0xc3c: vc3c(0xe5) = CONST 
    0xc3e: vc3e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc3c(0xe5), vc38(0x461bcd)
    0xc40: MSTORE vc37, vc3e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc41: vc41(0x20) = CONST 
    0xc43: vc43(0x4) = CONST 
    0xc46: vc46 = ADD vc37, vc43(0x4)
    0xc47: MSTORE vc46, vc41(0x20)
    0xc48: vc48(0xa) = CONST 
    0xc4a: vc4a(0x24) = CONST 
    0xc4d: vc4d = ADD vc37, vc4a(0x24)
    0xc4e: MSTORE vc4d, vc48(0xa)
    0xc4f: vc4f(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0xc70: vc70(0x44) = CONST 
    0xc73: vc73 = ADD vc37, vc70(0x44)
    0xc74: MSTORE vc73, vc4f(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0xc76: vc76 = MLOAD vc34(0x40)
    0xc7a: vc7a(0x0) = SUB vc37, vc76
    0xc7b: vc7b(0x64) = CONST 
    0xc7d: vc7d(0x64) = ADD vc7b(0x64), vc7a(0x0)
    0xc7f: REVERT vc76, vc7d(0x64)

    Begin block 0xc80
    prev=[0xc14], succ=[0xc89, 0xcbf]
    =================================
    0xc83: vc83 = GT v55f, v564
    0xc84: vc84 = ISZERO vc83
    0xc85: vc85(0xcbf) = CONST 
    0xc88: JUMPI vc85(0xcbf), vc84

    Begin block 0xc89
    prev=[0xc80], succ=[]
    =================================
    0xc89: vc89(0x40) = CONST 
    0xc8b: vc8b = MLOAD vc89(0x40)
    0xc8c: vc8c(0x461bcd) = CONST 
    0xc90: vc90(0xe5) = CONST 
    0xc92: vc92(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc90(0xe5), vc8c(0x461bcd)
    0xc94: MSTORE vc8b, vc92(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc95: vc95(0x4) = CONST 
    0xc97: vc97 = ADD vc95(0x4), vc8b
    0xc9a: vc9a(0x20) = CONST 
    0xc9c: vc9c = ADD vc9a(0x20), vc97
    0xc9f: vc9f(0x20) = SUB vc9c, vc97
    0xca1: MSTORE vc97, vc9f(0x20)
    0xca2: vca2(0x22) = CONST 
    0xca5: MSTORE vc9c, vca2(0x22)
    0xca6: vca6(0x20) = CONST 
    0xca8: vca8 = ADD vca6(0x20), vc9c
    0xcaa: vcaa(0x20f1) = CONST 
    0xcad: vcad(0x22) = CONST 
    0xcb0: CODECOPY vca8, vcaa(0x20f1), vcad(0x22)
    0xcb1: vcb1(0x40) = CONST 
    0xcb3: vcb3 = ADD vcb1(0x40), vca8
    0xcb7: vcb7(0x40) = CONST 
    0xcb9: vcb9 = MLOAD vcb7(0x40)
    0xcbc: vcbc(0x84) = SUB vcb3, vcb9
    0xcbe: REVERT vcb9, vcbc(0x84)

    Begin block 0xcbf
    prev=[0xc80], succ=[0x280e]
    =================================
    0xcc0: vcc0(0x6) = CONST 
    0xcc4: SSTORE vcc0(0x6), v55f
    0xcc5: vcc5(0x7) = CONST 
    0xcc9: SSTORE vcc5(0x7), v564
    0xcca: vcca(0x40) = CONST 
    0xccd: vccd = MLOAD vcca(0x40)
    0xcd0: MSTORE vccd, v55f
    0xcd1: vcd1(0x20) = CONST 
    0xcd4: vcd4 = ADD vccd, vcd1(0x20)
    0xcd7: MSTORE vcd4, v564
    0xcd9: vcd9 = MLOAD vcca(0x40)
    0xcda: vcda(0x21d54a4c1f750b4f93779e3e8b4de89db3f31bab8f203e68569727fee906cc32) = CONST 
    0xcff: vcff(0x0) = SUB vccd, vcd9
    0xd02: vd02(0x40) = ADD vcca(0x40), vcff(0x0)
    0xd04: LOG1 vcd9, vd02(0x40), vcda(0x21d54a4c1f750b4f93779e3e8b4de89db3f31bab8f203e68569727fee906cc32)
    0xd07: JUMP v547(0x280e)

    Begin block 0x280e
    prev=[0xcbf], succ=[]
    =================================
    0x280f: STOP 

}

function burnMax()() public {
    Begin block 0x569
    prev=[], succ=[0xd08]
    =================================
    0x56a: v56a(0x282f) = CONST 
    0x56d: v56d(0xd08) = CONST 
    0x570: JUMP v56d(0xd08)

    Begin block 0xd08
    prev=[0x569], succ=[0x282f]
    =================================
    0xd09: vd09(0x7) = CONST 
    0xd0b: vd0b = SLOAD vd09(0x7)
    0xd0d: JUMP v56a(0x282f)

    Begin block 0x282f
    prev=[0xd08], succ=[]
    =================================
    0x2830: v2830(0x40) = CONST 
    0x2833: v2833 = MLOAD v2830(0x40)
    0x2836: MSTORE v2833, vd0b
    0x2837: v2837 = MLOAD v2830(0x40)
    0x283b: v283b(0x0) = SUB v2833, v2837
    0x283c: v283c(0x20) = CONST 
    0x283e: v283e(0x20) = ADD v283c(0x20), v283b(0x0)
    0x2840: RETURN v2837, v283e(0x20)

}

function balanceOf(address)() public {
    Begin block 0x571
    prev=[], succ=[0x583, 0x587]
    =================================
    0x572: v572(0x2860) = CONST 
    0x575: v575(0x4) = CONST 
    0x578: v578 = CALLDATASIZE 
    0x579: v579 = SUB v578, v575(0x4)
    0x57a: v57a(0x20) = CONST 
    0x57d: v57d = LT v579, v57a(0x20)
    0x57e: v57e = ISZERO v57d
    0x57f: v57f(0x587) = CONST 
    0x582: JUMPI v57f(0x587), v57e

    Begin block 0x583
    prev=[0x571], succ=[]
    =================================
    0x583: v583(0x0) = CONST 
    0x586: REVERT v583(0x0), v583(0x0)

    Begin block 0x587
    prev=[0x571], succ=[0xd0e0x571]
    =================================
    0x589: v589 = CALLDATALOAD v575(0x4)
    0x58a: v58a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x59f: v59f = AND v58a(0xffffffffffffffffffffffffffffffffffffffff), v589
    0x5a0: v5a0(0xd0e) = CONST 
    0x5a3: JUMP v5a0(0xd0e)

    Begin block 0xd0e0x571
    prev=[0x587], succ=[0x2860]
    =================================
    0xd0f0x571: v571d0f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd240x571: v571d24 = AND v571d0f(0xffffffffffffffffffffffffffffffffffffffff), v59f
    0xd250x571: v571d25(0x0) = CONST 
    0xd290x571: MSTORE v571d25(0x0), v571d24
    0xd2a0x571: v571d2a(0xe) = CONST 
    0xd2c0x571: v571d2c(0x20) = CONST 
    0xd2e0x571: MSTORE v571d2c(0x20), v571d2a(0xe)
    0xd2f0x571: v571d2f(0x40) = CONST 
    0xd320x571: v571d32 = SHA3 v571d25(0x0), v571d2f(0x40)
    0xd330x571: v571d33 = SLOAD v571d32
    0xd350x571: JUMP v572(0x2860)

    Begin block 0x2860
    prev=[0xd0e0x571], succ=[]
    =================================
    0x2861: v2861(0x40) = CONST 
    0x2864: v2864 = MLOAD v2861(0x40)
    0x2867: MSTORE v2864, v571d33
    0x2868: v2868 = MLOAD v2861(0x40)
    0x286c: v286c(0x0) = SUB v2864, v2868
    0x286d: v286d(0x20) = CONST 
    0x286f: v286f(0x20) = ADD v286d(0x20), v286c(0x0)
    0x2871: RETURN v2868, v286f(0x20)

}

function delegateTotalSupply()() public {
    Begin block 0x5a4
    prev=[], succ=[0xd36B0x5a4]
    =================================
    0x5a5: v5a5(0x2891) = CONST 
    0x5a8: v5a8(0xd36) = CONST 
    0x5ab: JUMP v5a8(0xd36)

    Begin block 0xd36B0x5a4
    prev=[0x5a4], succ=[0x81eB0xd36B0x5a4]
    =================================
    0xd37S0x5a4: vd37V5a4(0x0) = CONST 
    0xd39S0x5a4: vd39V5a4(0xd40) = CONST 
    0xd3cS0x5a4: vd3cV5a4(0x81e) = CONST 
    0xd3fS0x5a4: JUMP vd3cV5a4(0x81e)

    Begin block 0x81eB0xd36B0x5a4
    prev=[0xd36B0x5a4], succ=[0xd40B0x5a4]
    =================================
    0x81fS0xd36S0x5a4: v81fVd36V5a4(0x4) = CONST 
    0x821S0xd36S0x5a4: v821Vd36V5a4 = SLOAD v81fVd36V5a4(0x4)
    0x823S0xd36S0x5a4: JUMP vd39V5a4(0xd40)

    Begin block 0xd40B0x5a4
    prev=[0x81eB0xd36B0x5a4], succ=[0x2891]
    =================================
    0xd44S0x5a4: JUMP v5a5(0x2891)

    Begin block 0x2891
    prev=[0xd40B0x5a4], succ=[]
    =================================
    0x2892: v2892(0x40) = CONST 
    0x2895: v2895 = MLOAD v2892(0x40)
    0x2898: MSTORE v2895, v821Vd36V5a4
    0x2899: v2899 = MLOAD v2892(0x40)
    0x289d: v289d(0x0) = SUB v2895, v2899
    0x289e: v289e(0x20) = CONST 
    0x28a0: v28a0(0x20) = ADD v289e(0x20), v289d(0x0)
    0x28a2: RETURN v2899, v28a0(0x20)

}

function setCanBurn(address,bool)() public {
    Begin block 0x5ac
    prev=[], succ=[0x5be, 0x5c2]
    =================================
    0x5ad: v5ad(0x28c2) = CONST 
    0x5b0: v5b0(0x4) = CONST 
    0x5b3: v5b3 = CALLDATASIZE 
    0x5b4: v5b4 = SUB v5b3, v5b0(0x4)
    0x5b5: v5b5(0x40) = CONST 
    0x5b8: v5b8 = LT v5b4, v5b5(0x40)
    0x5b9: v5b9 = ISZERO v5b8
    0x5ba: v5ba(0x5c2) = CONST 
    0x5bd: JUMPI v5ba(0x5c2), v5b9

    Begin block 0x5be
    prev=[0x5ac], succ=[]
    =================================
    0x5be: v5be(0x0) = CONST 
    0x5c1: REVERT v5be(0x0), v5be(0x0)

    Begin block 0x5c2
    prev=[0x5ac], succ=[0xd45]
    =================================
    0x5c4: v5c4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5da: v5da = CALLDATALOAD v5b0(0x4)
    0x5db: v5db = AND v5da, v5c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x5dd: v5dd(0x20) = CONST 
    0x5df: v5df(0x24) = ADD v5dd(0x20), v5b0(0x4)
    0x5e0: v5e0 = CALLDATALOAD v5df(0x24)
    0x5e1: v5e1 = ISZERO v5e0
    0x5e2: v5e2 = ISZERO v5e1
    0x5e3: v5e3(0xd45) = CONST 
    0x5e6: JUMP v5e3(0xd45)

    Begin block 0xd45
    prev=[0x5c2], succ=[0xd65, 0xdb1]
    =================================
    0xd46: vd46(0x0) = CONST 
    0xd48: vd48 = SLOAD vd46(0x0)
    0xd49: vd49(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd5e: vd5e = AND vd49(0xffffffffffffffffffffffffffffffffffffffff), vd48
    0xd5f: vd5f = CALLER 
    0xd60: vd60 = EQ vd5f, vd5e
    0xd61: vd61(0xdb1) = CONST 
    0xd64: JUMPI vd61(0xdb1), vd60

    Begin block 0xd65
    prev=[0xd45], succ=[]
    =================================
    0xd65: vd65(0x40) = CONST 
    0xd68: vd68 = MLOAD vd65(0x40)
    0xd69: vd69(0x461bcd) = CONST 
    0xd6d: vd6d(0xe5) = CONST 
    0xd6f: vd6f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd6d(0xe5), vd69(0x461bcd)
    0xd71: MSTORE vd68, vd6f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd72: vd72(0x20) = CONST 
    0xd74: vd74(0x4) = CONST 
    0xd77: vd77 = ADD vd68, vd74(0x4)
    0xd78: MSTORE vd77, vd72(0x20)
    0xd79: vd79(0xa) = CONST 
    0xd7b: vd7b(0x24) = CONST 
    0xd7e: vd7e = ADD vd68, vd7b(0x24)
    0xd7f: MSTORE vd7e, vd79(0xa)
    0xd80: vd80(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0xda1: vda1(0x44) = CONST 
    0xda4: vda4 = ADD vd68, vda1(0x44)
    0xda5: MSTORE vda4, vd80(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0xda7: vda7 = MLOAD vd65(0x40)
    0xdab: vdab(0x0) = SUB vd68, vda7
    0xdac: vdac(0x64) = CONST 
    0xdae: vdae(0x64) = ADD vdac(0x64), vdab(0x0)
    0xdb0: REVERT vda7, vdae(0x64)

    Begin block 0xdb1
    prev=[0xd45], succ=[0x28c2]
    =================================
    0xdb2: vdb2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdca: vdca = AND vdb2(0xffffffffffffffffffffffffffffffffffffffff), v5db
    0xdcb: vdcb(0x0) = CONST 
    0xdcf: MSTORE vdcb(0x0), vdca
    0xdd0: vdd0(0x17) = CONST 
    0xdd2: vdd2(0x20) = CONST 
    0xdd4: MSTORE vdd2(0x20), vdd0(0x17)
    0xdd5: vdd5(0x40) = CONST 
    0xdd8: vdd8 = SHA3 vdcb(0x0), vdd5(0x40)
    0xdda: vdda = SLOAD vdd8
    0xddb: vddb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0xdfc: vdfc = AND vddb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vdda
    0xdfe: vdfe = ISZERO v5e2
    0xdff: vdff = ISZERO vdfe
    0xe03: ve03 = OR vdff, vdfc
    0xe05: SSTORE vdd8, ve03
    0xe06: JUMP v5ad(0x28c2)

    Begin block 0x28c2
    prev=[0xdb1], succ=[]
    =================================
    0x28c3: STOP 

}

function reclaimToken(address,address)() public {
    Begin block 0x5e7
    prev=[], succ=[0x5f9, 0x5fd]
    =================================
    0x5e8: v5e8(0x28e3) = CONST 
    0x5eb: v5eb(0x4) = CONST 
    0x5ee: v5ee = CALLDATASIZE 
    0x5ef: v5ef = SUB v5ee, v5eb(0x4)
    0x5f0: v5f0(0x40) = CONST 
    0x5f3: v5f3 = LT v5ef, v5f0(0x40)
    0x5f4: v5f4 = ISZERO v5f3
    0x5f5: v5f5(0x5fd) = CONST 
    0x5f8: JUMPI v5f5(0x5fd), v5f4

    Begin block 0x5f9
    prev=[0x5e7], succ=[]
    =================================
    0x5f9: v5f9(0x0) = CONST 
    0x5fc: REVERT v5f9(0x0), v5f9(0x0)

    Begin block 0x5fd
    prev=[0x5e7], succ=[0xe07]
    =================================
    0x5ff: v5ff(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x615: v615 = CALLDATALOAD v5eb(0x4)
    0x617: v617 = AND v5ff(0xffffffffffffffffffffffffffffffffffffffff), v615
    0x619: v619(0x20) = CONST 
    0x61b: v61b(0x24) = ADD v619(0x20), v5eb(0x4)
    0x61c: v61c = CALLDATALOAD v61b(0x24)
    0x61d: v61d = AND v61c, v5ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x61e: v61e(0xe07) = CONST 
    0x621: JUMP v61e(0xe07)

    Begin block 0xe07
    prev=[0x5fd], succ=[0xe27, 0xe73]
    =================================
    0xe08: ve08(0x0) = CONST 
    0xe0a: ve0a = SLOAD ve08(0x0)
    0xe0b: ve0b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe20: ve20 = AND ve0b(0xffffffffffffffffffffffffffffffffffffffff), ve0a
    0xe21: ve21 = CALLER 
    0xe22: ve22 = EQ ve21, ve20
    0xe23: ve23(0xe73) = CONST 
    0xe26: JUMPI ve23(0xe73), ve22

    Begin block 0xe27
    prev=[0xe07], succ=[]
    =================================
    0xe27: ve27(0x40) = CONST 
    0xe2a: ve2a = MLOAD ve27(0x40)
    0xe2b: ve2b(0x461bcd) = CONST 
    0xe2f: ve2f(0xe5) = CONST 
    0xe31: ve31(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL ve2f(0xe5), ve2b(0x461bcd)
    0xe33: MSTORE ve2a, ve31(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe34: ve34(0x20) = CONST 
    0xe36: ve36(0x4) = CONST 
    0xe39: ve39 = ADD ve2a, ve36(0x4)
    0xe3a: MSTORE ve39, ve34(0x20)
    0xe3b: ve3b(0xa) = CONST 
    0xe3d: ve3d(0x24) = CONST 
    0xe40: ve40 = ADD ve2a, ve3d(0x24)
    0xe41: MSTORE ve40, ve3b(0xa)
    0xe42: ve42(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0xe63: ve63(0x44) = CONST 
    0xe66: ve66 = ADD ve2a, ve63(0x44)
    0xe67: MSTORE ve66, ve42(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0xe69: ve69 = MLOAD ve27(0x40)
    0xe6d: ve6d(0x0) = SUB ve2a, ve69
    0xe6e: ve6e(0x64) = CONST 
    0xe70: ve70(0x64) = ADD ve6e(0x64), ve6d(0x0)
    0xe72: REVERT ve69, ve70(0x64)

    Begin block 0xe73
    prev=[0xe07], succ=[0xedf, 0xee3]
    =================================
    0xe74: ve74(0x40) = CONST 
    0xe77: ve77 = MLOAD ve74(0x40)
    0xe78: ve78(0x70a0823100000000000000000000000000000000000000000000000000000000) = CONST 
    0xe9a: MSTORE ve77, ve78(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0xe9b: ve9b = ADDRESS 
    0xe9c: ve9c(0x4) = CONST 
    0xe9f: ve9f = ADD ve77, ve9c(0x4)
    0xea0: MSTORE ve9f, ve9b
    0xea2: vea2 = MLOAD ve74(0x40)
    0xea3: vea3(0x0) = CONST 
    0xea6: vea6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xebc: vebc = AND v617, vea6(0xffffffffffffffffffffffffffffffffffffffff)
    0xebe: vebe(0x70a08231) = CONST 
    0xec4: vec4(0x24) = CONST 
    0xec8: vec8 = ADD ve77, vec4(0x24)
    0xeca: veca(0x20) = CONST 
    0xed2: ved2(0x0) = SUB ve77, vea2
    0xed3: ved3(0x24) = ADD ved2(0x0), vec4(0x24)
    0xed7: ved7 = EXTCODESIZE vebc
    0xed8: ved8 = ISZERO ved7
    0xeda: veda = ISZERO ved8
    0xedb: vedb(0xee3) = CONST 
    0xede: JUMPI vedb(0xee3), veda

    Begin block 0xedf
    prev=[0xe73], succ=[]
    =================================
    0xedf: vedf(0x0) = CONST 
    0xee2: REVERT vedf(0x0), vedf(0x0)

    Begin block 0xee3
    prev=[0xe73], succ=[0xeee, 0xef7]
    =================================
    0xee5: vee5 = GAS 
    0xee6: vee6 = STATICCALL vee5, vebc, vea2, ved3(0x24), vea2, veca(0x20)
    0xee7: vee7 = ISZERO vee6
    0xee9: vee9 = ISZERO vee7
    0xeea: veea(0xef7) = CONST 
    0xeed: JUMPI veea(0xef7), vee9

    Begin block 0xeee
    prev=[0xee3], succ=[]
    =================================
    0xeee: veee = RETURNDATASIZE 
    0xeef: veef(0x0) = CONST 
    0xef2: RETURNDATACOPY veef(0x0), veef(0x0), veee
    0xef3: vef3 = RETURNDATASIZE 
    0xef4: vef4(0x0) = CONST 
    0xef6: REVERT vef4(0x0), vef3

    Begin block 0xef7
    prev=[0xee3], succ=[0xf09, 0xf0d]
    =================================
    0xefc: vefc(0x40) = CONST 
    0xefe: vefe = MLOAD vefc(0x40)
    0xeff: veff = RETURNDATASIZE 
    0xf00: vf00(0x20) = CONST 
    0xf03: vf03 = LT veff, vf00(0x20)
    0xf04: vf04 = ISZERO vf03
    0xf05: vf05(0xf0d) = CONST 
    0xf08: JUMPI vf05(0xf0d), vf04

    Begin block 0xf09
    prev=[0xef7], succ=[]
    =================================
    0xf09: vf09(0x0) = CONST 
    0xf0c: REVERT vf09(0x0), vf09(0x0)

    Begin block 0xf0d
    prev=[0xef7], succ=[0xf87, 0xf8b]
    =================================
    0xf0f: vf0f = MLOAD vefe
    0xf10: vf10(0x40) = CONST 
    0xf13: vf13 = MLOAD vf10(0x40)
    0xf14: vf14(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = CONST 
    0xf36: MSTORE vf13, vf14(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0xf37: vf37(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf4e: vf4e = AND vf37(0xffffffffffffffffffffffffffffffffffffffff), v61d
    0xf4f: vf4f(0x4) = CONST 
    0xf52: vf52 = ADD vf13, vf4f(0x4)
    0xf53: MSTORE vf52, vf4e
    0xf54: vf54(0x24) = CONST 
    0xf57: vf57 = ADD vf13, vf54(0x24)
    0xf5a: MSTORE vf57, vf0f
    0xf5c: vf5c = MLOAD vf10(0x40)
    0xf62: vf62 = AND v617, vf37(0xffffffffffffffffffffffffffffffffffffffff)
    0xf64: vf64(0xa9059cbb) = CONST 
    0xf6a: vf6a(0x44) = CONST 
    0xf6e: vf6e = ADD vf13, vf6a(0x44)
    0xf70: vf70(0x20) = CONST 
    0xf78: vf78(0x0) = SUB vf13, vf5c
    0xf79: vf79(0x44) = ADD vf78(0x0), vf6a(0x44)
    0xf7b: vf7b(0x0) = CONST 
    0xf7f: vf7f = EXTCODESIZE vf62
    0xf80: vf80 = ISZERO vf7f
    0xf82: vf82 = ISZERO vf80
    0xf83: vf83(0xf8b) = CONST 
    0xf86: JUMPI vf83(0xf8b), vf82

    Begin block 0xf87
    prev=[0xf0d], succ=[]
    =================================
    0xf87: vf87(0x0) = CONST 
    0xf8a: REVERT vf87(0x0), vf87(0x0)

    Begin block 0xf8b
    prev=[0xf0d], succ=[0xf96, 0xf9f]
    =================================
    0xf8d: vf8d = GAS 
    0xf8e: vf8e = CALL vf8d, vf62, vf7b(0x0), vf5c, vf79(0x44), vf5c, vf70(0x20)
    0xf8f: vf8f = ISZERO vf8e
    0xf91: vf91 = ISZERO vf8f
    0xf92: vf92(0xf9f) = CONST 
    0xf95: JUMPI vf92(0xf9f), vf91

    Begin block 0xf96
    prev=[0xf8b], succ=[]
    =================================
    0xf96: vf96 = RETURNDATASIZE 
    0xf97: vf97(0x0) = CONST 
    0xf9a: RETURNDATACOPY vf97(0x0), vf97(0x0), vf96
    0xf9b: vf9b = RETURNDATASIZE 
    0xf9c: vf9c(0x0) = CONST 
    0xf9e: REVERT vf9c(0x0), vf9b

    Begin block 0xf9f
    prev=[0xf8b], succ=[0xfb1, 0xfb5]
    =================================
    0xfa4: vfa4(0x40) = CONST 
    0xfa6: vfa6 = MLOAD vfa4(0x40)
    0xfa7: vfa7 = RETURNDATASIZE 
    0xfa8: vfa8(0x20) = CONST 
    0xfab: vfab = LT vfa7, vfa8(0x20)
    0xfac: vfac = ISZERO vfab
    0xfad: vfad(0xfb5) = CONST 
    0xfb0: JUMPI vfad(0xfb5), vfac

    Begin block 0xfb1
    prev=[0xf9f], succ=[]
    =================================
    0xfb1: vfb1(0x0) = CONST 
    0xfb4: REVERT vfb1(0x0), vfb1(0x0)

    Begin block 0xfb5
    prev=[0xf9f], succ=[0x28e3]
    =================================
    0xfbb: JUMP v5e8(0x28e3)

    Begin block 0x28e3
    prev=[0xfb5], succ=[]
    =================================
    0x28e4: STOP 

}

function owner()() public {
    Begin block 0x622
    prev=[], succ=[0xfbc]
    =================================
    0x623: v623(0x2904) = CONST 
    0x626: v626(0xfbc) = CONST 
    0x629: JUMP v626(0xfbc)

    Begin block 0xfbc
    prev=[0x622], succ=[0x2904]
    =================================
    0xfbd: vfbd(0x0) = CONST 
    0xfbf: vfbf = SLOAD vfbd(0x0)
    0xfc0: vfc0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfd5: vfd5 = AND vfc0(0xffffffffffffffffffffffffffffffffffffffff), vfbf
    0xfd7: JUMP v623(0x2904)

    Begin block 0x2904
    prev=[0xfbc], succ=[]
    =================================
    0x2905: v2905(0x40) = CONST 
    0x2908: v2908 = MLOAD v2905(0x40)
    0x2909: v2909(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2920: v2920 = AND vfd5, v2909(0xffffffffffffffffffffffffffffffffffffffff)
    0x2922: MSTORE v2908, v2920
    0x2923: v2923 = MLOAD v2905(0x40)
    0x2927: v2927(0x0) = SUB v2908, v2923
    0x2928: v2928(0x20) = CONST 
    0x292a: v292a(0x20) = ADD v2928(0x20), v2927(0x0)
    0x292c: RETURN v2923, v292a(0x20)

}

function symbol()() public {
    Begin block 0x653
    prev=[], succ=[0xfd8]
    =================================
    0x654: v654(0x24d) = CONST 
    0x657: v657(0xfd8) = CONST 
    0x65a: JUMP v657(0xfd8)

    Begin block 0xfd8
    prev=[0x653], succ=[0x24d0x653]
    =================================
    0xfd9: vfd9(0x40) = CONST 
    0xfdc: vfdc = MLOAD vfd9(0x40)
    0xfdf: vfdf = ADD vfd9(0x40), vfdc
    0xfe2: MSTORE vfd9(0x40), vfdf
    0xfe3: vfe3(0x4) = CONST 
    0xfe6: MSTORE vfdc, vfe3(0x4)
    0xfe7: vfe7(0x5455534400000000000000000000000000000000000000000000000000000000) = CONST 
    0x1008: v1008(0x20) = CONST 
    0x100b: v100b = ADD vfdc, v1008(0x20)
    0x100c: MSTORE v100b, vfe7(0x5455534400000000000000000000000000000000000000000000000000000000)
    0x100e: JUMP v654(0x24d)

    Begin block 0x24d0x653
    prev=[0xfd8], succ=[0x26f0x653]
    =================================
    0x24e0x653: v65324e(0x40) = CONST 
    0x2510x653: v653251 = MLOAD v65324e(0x40)
    0x2520x653: v653252(0x20) = CONST 
    0x2560x653: MSTORE v653251, v653252(0x20)
    0x2580x653: v653258(0x4) = MLOAD vfdc
    0x25b0x653: v65325b = ADD v653251, v653252(0x20)
    0x25c0x653: MSTORE v65325b, v653258(0x4)
    0x25e0x653: v65325e(0x4) = MLOAD vfdc
    0x2650x653: v653265 = ADD v653251, v65324e(0x40)
    0x2680x653: v653268 = ADD vfdc, v653252(0x20)
    0x26d0x653: v65326d(0x0) = CONST 

    Begin block 0x26f0x653
    prev=[0x2780x653, 0x24d0x653], succ=[0x2870x653, 0x2780x653]
    =================================
    0x26f0x653_0x0: v26f653_0 = PHI v653282, v65326d(0x0)
    0x2720x653: v653272 = LT v26f653_0, v65325e(0x4)
    0x2730x653: v653273 = ISZERO v653272
    0x2740x653: v653274(0x287) = CONST 
    0x2770x653: JUMPI v653274(0x287), v653273

    Begin block 0x2870x653
    prev=[0x26f0x653], succ=[0x2b40x653, 0x29b0x653]
    =================================
    0x2900x653: v653290 = ADD v65325e(0x4), v653265
    0x2920x653: v653292(0x1f) = CONST 
    0x2940x653: v653294(0x4) = AND v653292(0x1f), v65325e(0x4)
    0x2960x653: v653296 = ISZERO v653294(0x4)
    0x2970x653: v653297(0x2b4) = CONST 
    0x29a0x653: JUMPI v653297(0x2b4), v653296

    Begin block 0x2b40x653
    prev=[0x2870x653, 0x29b0x653], succ=[]
    =================================
    0x2b40x653_0x1: v2b4653_1 = PHI v6532b1, v653290
    0x2ba0x653: v6532ba(0x40) = CONST 
    0x2bc0x653: v6532bc = MLOAD v6532ba(0x40)
    0x2bf0x653: v6532bf = SUB v2b4653_1, v6532bc
    0x2c10x653: RETURN v6532bc, v6532bf

    Begin block 0x29b0x653
    prev=[0x2870x653], succ=[0x2b40x653]
    =================================
    0x29d0x653: v65329d = SUB v653290, v653294(0x4)
    0x29f0x653: v65329f = MLOAD v65329d
    0x2a00x653: v6532a0(0x1) = CONST 
    0x2a30x653: v6532a3(0x20) = CONST 
    0x2a50x653: v6532a5(0x1c) = SUB v6532a3(0x20), v653294(0x4)
    0x2a60x653: v6532a6(0x100) = CONST 
    0x2a90x653: v6532a9(0x100000000000000000000000000000000000000000000000000000000) = EXP v6532a6(0x100), v6532a5(0x1c)
    0x2aa0x653: v6532aa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v6532a9(0x100000000000000000000000000000000000000000000000000000000), v6532a0(0x1)
    0x2ab0x653: v6532ab = NOT v6532aa(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x2ac0x653: v6532ac = AND v6532ab, v65329f
    0x2ae0x653: MSTORE v65329d, v6532ac
    0x2af0x653: v6532af(0x20) = CONST 
    0x2b10x653: v6532b1 = ADD v6532af(0x20), v65329d

    Begin block 0x2780x653
    prev=[0x26f0x653], succ=[0x26f0x653]
    =================================
    0x2780x653_0x0: v278653_0 = PHI v653282, v65326d(0x0)
    0x27a0x653: v65327a = ADD v278653_0, v653268
    0x27b0x653: v65327b = MLOAD v65327a
    0x27e0x653: v65327e = ADD v278653_0, v653265
    0x27f0x653: MSTORE v65327e, v65327b
    0x2800x653: v653280(0x20) = CONST 
    0x2820x653: v653282 = ADD v653280(0x20), v278653_0
    0x2830x653: v653283(0x26f) = CONST 
    0x2860x653: JUMP v653283(0x26f)

}

function reclaimEther(address)() public {
    Begin block 0x65b
    prev=[], succ=[0x66d, 0x671]
    =================================
    0x65c: v65c(0x294c) = CONST 
    0x65f: v65f(0x4) = CONST 
    0x662: v662 = CALLDATASIZE 
    0x663: v663 = SUB v662, v65f(0x4)
    0x664: v664(0x20) = CONST 
    0x667: v667 = LT v663, v664(0x20)
    0x668: v668 = ISZERO v667
    0x669: v669(0x671) = CONST 
    0x66c: JUMPI v669(0x671), v668

    Begin block 0x66d
    prev=[0x65b], succ=[]
    =================================
    0x66d: v66d(0x0) = CONST 
    0x670: REVERT v66d(0x0), v66d(0x0)

    Begin block 0x671
    prev=[0x65b], succ=[0x100f]
    =================================
    0x673: v673 = CALLDATALOAD v65f(0x4)
    0x674: v674(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x689: v689 = AND v674(0xffffffffffffffffffffffffffffffffffffffff), v673
    0x68a: v68a(0x100f) = CONST 
    0x68d: JUMP v68a(0x100f)

    Begin block 0x100f
    prev=[0x671], succ=[0x102f, 0x107b]
    =================================
    0x1010: v1010(0x0) = CONST 
    0x1012: v1012 = SLOAD v1010(0x0)
    0x1013: v1013(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1028: v1028 = AND v1013(0xffffffffffffffffffffffffffffffffffffffff), v1012
    0x1029: v1029 = CALLER 
    0x102a: v102a = EQ v1029, v1028
    0x102b: v102b(0x107b) = CONST 
    0x102e: JUMPI v102b(0x107b), v102a

    Begin block 0x102f
    prev=[0x100f], succ=[]
    =================================
    0x102f: v102f(0x40) = CONST 
    0x1032: v1032 = MLOAD v102f(0x40)
    0x1033: v1033(0x461bcd) = CONST 
    0x1037: v1037(0xe5) = CONST 
    0x1039: v1039(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1037(0xe5), v1033(0x461bcd)
    0x103b: MSTORE v1032, v1039(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x103c: v103c(0x20) = CONST 
    0x103e: v103e(0x4) = CONST 
    0x1041: v1041 = ADD v1032, v103e(0x4)
    0x1042: MSTORE v1041, v103c(0x20)
    0x1043: v1043(0xa) = CONST 
    0x1045: v1045(0x24) = CONST 
    0x1048: v1048 = ADD v1032, v1045(0x24)
    0x1049: MSTORE v1048, v1043(0xa)
    0x104a: v104a(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0x106b: v106b(0x44) = CONST 
    0x106e: v106e = ADD v1032, v106b(0x44)
    0x106f: MSTORE v106e, v104a(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0x1071: v1071 = MLOAD v102f(0x40)
    0x1075: v1075(0x0) = SUB v1032, v1071
    0x1076: v1076(0x64) = CONST 
    0x1078: v1078(0x64) = ADD v1076(0x64), v1075(0x0)
    0x107a: REVERT v1071, v1078(0x64)

    Begin block 0x107b
    prev=[0x100f], succ=[0x10b4, 0x2b71]
    =================================
    0x107c: v107c(0x40) = CONST 
    0x107e: v107e = MLOAD v107c(0x40)
    0x107f: v107f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1095: v1095 = AND v689, v107f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1097: v1097 = SELFBALANCE 
    0x1099: v1099 = ISZERO v1097
    0x109a: v109a(0x8fc) = CONST 
    0x109d: v109d = MUL v109a(0x8fc), v1099
    0x109f: v109f(0x0) = CONST 
    0x10a7: v10a7 = CALL v109d, v1095, v1097, v107e, v109f(0x0), v107e, v109f(0x0)
    0x10ad: v10ad = ISZERO v10a7
    0x10af: v10af = ISZERO v10ad
    0x10b0: v10b0(0x2b71) = CONST 
    0x10b3: JUMPI v10b0(0x2b71), v10af

    Begin block 0x10b4
    prev=[0x107b], succ=[]
    =================================
    0x10b4: v10b4 = RETURNDATASIZE 
    0x10b5: v10b5(0x0) = CONST 
    0x10b8: RETURNDATACOPY v10b5(0x0), v10b5(0x0), v10b4
    0x10b9: v10b9 = RETURNDATASIZE 
    0x10ba: v10ba(0x0) = CONST 
    0x10bc: REVERT v10ba(0x0), v10b9

    Begin block 0x2b71
    prev=[0x107b], succ=[0x294c]
    =================================
    0x2b74: JUMP v65c(0x294c)

    Begin block 0x294c
    prev=[0x2b71], succ=[]
    =================================
    0x294d: STOP 

}

function decreaseAllowance(address,uint256)() public {
    Begin block 0x68e
    prev=[], succ=[0x6a0, 0x6a4]
    =================================
    0x68f: v68f(0x296d) = CONST 
    0x692: v692(0x4) = CONST 
    0x695: v695 = CALLDATASIZE 
    0x696: v696 = SUB v695, v692(0x4)
    0x697: v697(0x40) = CONST 
    0x69a: v69a = LT v696, v697(0x40)
    0x69b: v69b = ISZERO v69a
    0x69c: v69c(0x6a4) = CONST 
    0x69f: JUMPI v69c(0x6a4), v69b

    Begin block 0x6a0
    prev=[0x68e], succ=[]
    =================================
    0x6a0: v6a0(0x0) = CONST 
    0x6a3: REVERT v6a0(0x0), v6a0(0x0)

    Begin block 0x6a4
    prev=[0x68e], succ=[0x10c1]
    =================================
    0x6a6: v6a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6bc: v6bc = CALLDATALOAD v692(0x4)
    0x6bd: v6bd = AND v6bc, v6a6(0xffffffffffffffffffffffffffffffffffffffff)
    0x6bf: v6bf(0x20) = CONST 
    0x6c1: v6c1(0x24) = ADD v6bf(0x20), v692(0x4)
    0x6c2: v6c2 = CALLDATALOAD v6c1(0x24)
    0x6c3: v6c3(0x10c1) = CONST 
    0x6c6: JUMP v6c3(0x10c1)

    Begin block 0x10c1
    prev=[0x6a4], succ=[0x13a6B0x10c1]
    =================================
    0x10c2: v10c2(0x0) = CONST 
    0x10c4: v10c4(0x2b94) = CONST 
    0x10c7: v10c7(0x10ce) = CONST 
    0x10ca: v10ca(0x13a6) = CONST 
    0x10cd: JUMP v10ca(0x13a6)

    Begin block 0x13a6B0x10c1
    prev=[0x10c1], succ=[0x10ce]
    =================================
    0x13a7S0x10c1: v13a7V10c1 = CALLER 
    0x13a9S0x10c1: JUMP v10c7(0x10ce)

    Begin block 0x10ce
    prev=[0x13a6B0x10c1], succ=[0x13a6B0x10ce]
    =================================
    0x10d0: v10d0(0x2bbc) = CONST 
    0x10d4: v10d4(0x40) = CONST 
    0x10d6: v10d6 = MLOAD v10d4(0x40)
    0x10d8: v10d8(0x60) = CONST 
    0x10da: v10da = ADD v10d8(0x60), v10d6
    0x10db: v10db(0x40) = CONST 
    0x10dd: MSTORE v10db(0x40), v10da
    0x10df: v10df(0x25) = CONST 
    0x10e2: MSTORE v10d6, v10df(0x25)
    0x10e3: v10e3(0x20) = CONST 
    0x10e5: v10e5 = ADD v10e3(0x20), v10d6
    0x10e6: v10e6(0x228b) = CONST 
    0x10e9: v10e9(0x25) = CONST 
    0x10ec: CODECOPY v10e5, v10e6(0x228b), v10e9(0x25)
    0x10ed: v10ed(0xf) = CONST 
    0x10ef: v10ef(0x0) = CONST 
    0x10f1: v10f1(0x10f8) = CONST 
    0x10f4: v10f4(0x13a6) = CONST 
    0x10f7: JUMP v10f4(0x13a6)

    Begin block 0x13a6B0x10ce
    prev=[0x10ce], succ=[0x10f8]
    =================================
    0x13a7S0x10ce: v13a7V10ce = CALLER 
    0x13a9S0x10ce: JUMP v10f1(0x10f8)

    Begin block 0x10f8
    prev=[0x13a6B0x10ce], succ=[0x2bbc]
    =================================
    0x10f9: v10f9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1110: v1110 = AND v10f9(0xffffffffffffffffffffffffffffffffffffffff), v13a7V10ce
    0x1112: MSTORE v10ef(0x0), v1110
    0x1113: v1113(0x20) = CONST 
    0x1117: v1117(0x20) = ADD v10ef(0x0), v1113(0x20)
    0x111b: MSTORE v1117(0x20), v10ed(0xf)
    0x111c: v111c(0x40) = CONST 
    0x1120: v1120(0x40) = ADD v111c(0x40), v10ef(0x0)
    0x1121: v1121(0x0) = CONST 
    0x1125: v1125 = SHA3 v1121(0x0), v1120(0x40)
    0x1128: v1128 = AND v6bd, v10f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x112a: MSTORE v1121(0x0), v1128
    0x112c: MSTORE v1113(0x20), v1125
    0x112e: v112e = SHA3 v1121(0x0), v111c(0x40)
    0x112f: v112f = SLOAD v112e
    0x1132: v1132(0xffffffff) = CONST 
    0x1137: v1137(0x1510) = CONST 
    0x113a: v113a(0x1510) = AND v1137(0x1510), v1132(0xffffffff)
    0x113b: v113b_0 = CALLPRIVATE v113a(0x1510), v10d6, v6c2, v112f, v10d0(0x2bbc)

    Begin block 0x2bbc
    prev=[0x10f8], succ=[0x2b94]
    =================================
    0x2bbd: v2bbd(0x13aa) = CONST 
    0x2bc0: CALLPRIVATE v2bbd(0x13aa), v113b_0, v6bd, v13a7V10c1, v10c4(0x2b94)

    Begin block 0x2b94
    prev=[0x2bbc], succ=[0x296d]
    =================================
    0x2b96: v2b96(0x1) = CONST 
    0x2b9c: JUMP v68f(0x296d)

    Begin block 0x296d
    prev=[0x2b94], succ=[]
    =================================
    0x296e: v296e(0x40) = CONST 
    0x2971: v2971 = MLOAD v296e(0x40)
    0x2973: v2973 = ISZERO v2b96(0x1)
    0x2974: v2974 = ISZERO v2973
    0x2976: MSTORE v2971, v2974
    0x2977: v2977 = MLOAD v296e(0x40)
    0x297b: v297b(0x0) = SUB v2971, v2977
    0x297c: v297c(0x20) = CONST 
    0x297e: v297e(0x20) = ADD v297c(0x20), v297b(0x0)
    0x2980: RETURN v2977, v297e(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x6c7
    prev=[], succ=[0x6d9, 0x6dd]
    =================================
    0x6c8: v6c8(0x29a0) = CONST 
    0x6cb: v6cb(0x4) = CONST 
    0x6ce: v6ce = CALLDATASIZE 
    0x6cf: v6cf = SUB v6ce, v6cb(0x4)
    0x6d0: v6d0(0x40) = CONST 
    0x6d3: v6d3 = LT v6cf, v6d0(0x40)
    0x6d4: v6d4 = ISZERO v6d3
    0x6d5: v6d5(0x6dd) = CONST 
    0x6d8: JUMPI v6d5(0x6dd), v6d4

    Begin block 0x6d9
    prev=[0x6c7], succ=[]
    =================================
    0x6d9: v6d9(0x0) = CONST 
    0x6dc: REVERT v6d9(0x0), v6d9(0x0)

    Begin block 0x6dd
    prev=[0x6c7], succ=[0x113c]
    =================================
    0x6df: v6df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6f5: v6f5 = CALLDATALOAD v6cb(0x4)
    0x6f6: v6f6 = AND v6f5, v6df(0xffffffffffffffffffffffffffffffffffffffff)
    0x6f8: v6f8(0x20) = CONST 
    0x6fa: v6fa(0x24) = ADD v6f8(0x20), v6cb(0x4)
    0x6fb: v6fb = CALLDATALOAD v6fa(0x24)
    0x6fc: v6fc(0x113c) = CONST 
    0x6ff: JUMP v6fc(0x113c)

    Begin block 0x113c
    prev=[0x6dd], succ=[0x13a6B0x113c]
    =================================
    0x113d: v113d(0x0) = CONST 
    0x113f: v113f(0x2be0) = CONST 
    0x1142: v1142(0x1149) = CONST 
    0x1145: v1145(0x13a6) = CONST 
    0x1148: JUMP v1145(0x13a6)

    Begin block 0x13a6B0x113c
    prev=[0x113c], succ=[0x1149]
    =================================
    0x13a7S0x113c: v13a7V113c = CALLER 
    0x13a9S0x113c: JUMP v1142(0x1149)

    Begin block 0x1149
    prev=[0x13a6B0x113c], succ=[0x2be0]
    =================================
    0x114c: v114c(0x148d) = CONST 
    0x114f: CALLPRIVATE v114c(0x148d), v6fb, v6f6, v13a7V113c, v113f(0x2be0)

    Begin block 0x2be0
    prev=[0x1149], succ=[0x29a0]
    =================================
    0x2be2: v2be2(0x1) = CONST 
    0x2be8: JUMP v6c8(0x29a0)

    Begin block 0x29a0
    prev=[0x2be0], succ=[]
    =================================
    0x29a1: v29a1(0x40) = CONST 
    0x29a4: v29a4 = MLOAD v29a1(0x40)
    0x29a6: v29a6 = ISZERO v2be2(0x1)
    0x29a7: v29a7 = ISZERO v29a6
    0x29a9: MSTORE v29a4, v29a7
    0x29aa: v29aa = MLOAD v29a1(0x40)
    0x29ae: v29ae(0x0) = SUB v29a4, v29aa
    0x29af: v29af(0x20) = CONST 
    0x29b1: v29b1(0x20) = ADD v29af(0x20), v29ae(0x0)
    0x29b3: RETURN v29aa, v29b1(0x20)

}

function setBlacklisted(address,bool)() public {
    Begin block 0x700
    prev=[], succ=[0x712, 0x716]
    =================================
    0x701: v701(0x29d3) = CONST 
    0x704: v704(0x4) = CONST 
    0x707: v707 = CALLDATASIZE 
    0x708: v708 = SUB v707, v704(0x4)
    0x709: v709(0x40) = CONST 
    0x70c: v70c = LT v708, v709(0x40)
    0x70d: v70d = ISZERO v70c
    0x70e: v70e(0x716) = CONST 
    0x711: JUMPI v70e(0x716), v70d

    Begin block 0x712
    prev=[0x700], succ=[]
    =================================
    0x712: v712(0x0) = CONST 
    0x715: REVERT v712(0x0), v712(0x0)

    Begin block 0x716
    prev=[0x700], succ=[0x1150]
    =================================
    0x718: v718(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x72e: v72e = CALLDATALOAD v704(0x4)
    0x72f: v72f = AND v72e, v718(0xffffffffffffffffffffffffffffffffffffffff)
    0x731: v731(0x20) = CONST 
    0x733: v733(0x24) = ADD v731(0x20), v704(0x4)
    0x734: v734 = CALLDATALOAD v733(0x24)
    0x735: v735 = ISZERO v734
    0x736: v736 = ISZERO v735
    0x737: v737(0x1150) = CONST 
    0x73a: JUMP v737(0x1150)

    Begin block 0x1150
    prev=[0x716], succ=[0x1170, 0x11bc]
    =================================
    0x1151: v1151(0x0) = CONST 
    0x1153: v1153 = SLOAD v1151(0x0)
    0x1154: v1154(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1169: v1169 = AND v1154(0xffffffffffffffffffffffffffffffffffffffff), v1153
    0x116a: v116a = CALLER 
    0x116b: v116b = EQ v116a, v1169
    0x116c: v116c(0x11bc) = CONST 
    0x116f: JUMPI v116c(0x11bc), v116b

    Begin block 0x1170
    prev=[0x1150], succ=[]
    =================================
    0x1170: v1170(0x40) = CONST 
    0x1173: v1173 = MLOAD v1170(0x40)
    0x1174: v1174(0x461bcd) = CONST 
    0x1178: v1178(0xe5) = CONST 
    0x117a: v117a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1178(0xe5), v1174(0x461bcd)
    0x117c: MSTORE v1173, v117a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x117d: v117d(0x20) = CONST 
    0x117f: v117f(0x4) = CONST 
    0x1182: v1182 = ADD v1173, v117f(0x4)
    0x1183: MSTORE v1182, v117d(0x20)
    0x1184: v1184(0xa) = CONST 
    0x1186: v1186(0x24) = CONST 
    0x1189: v1189 = ADD v1173, v1186(0x24)
    0x118a: MSTORE v1189, v1184(0xa)
    0x118b: v118b(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0x11ac: v11ac(0x44) = CONST 
    0x11af: v11af = ADD v1173, v11ac(0x44)
    0x11b0: MSTORE v11af, v118b(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0x11b2: v11b2 = MLOAD v1170(0x40)
    0x11b6: v11b6(0x0) = SUB v1173, v11b2
    0x11b7: v11b7(0x64) = CONST 
    0x11b9: v11b9(0x64) = ADD v11b7(0x64), v11b6(0x0)
    0x11bb: REVERT v11b2, v11b9(0x64)

    Begin block 0x11bc
    prev=[0x1150], succ=[0x11de, 0x1214]
    =================================
    0x11bd: v11bd(0x100000) = CONST 
    0x11c2: v11c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11d7: v11d7 = AND v11c2(0xffffffffffffffffffffffffffffffffffffffff), v72f
    0x11d8: v11d8 = LT v11d7, v11bd(0x100000)
    0x11d9: v11d9 = ISZERO v11d8
    0x11da: v11da(0x1214) = CONST 
    0x11dd: JUMPI v11da(0x1214), v11d9

    Begin block 0x11de
    prev=[0x11bc], succ=[]
    =================================
    0x11de: v11de(0x40) = CONST 
    0x11e0: v11e0 = MLOAD v11de(0x40)
    0x11e1: v11e1(0x461bcd) = CONST 
    0x11e5: v11e5(0xe5) = CONST 
    0x11e7: v11e7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v11e5(0xe5), v11e1(0x461bcd)
    0x11e9: MSTORE v11e0, v11e7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11ea: v11ea(0x4) = CONST 
    0x11ec: v11ec = ADD v11ea(0x4), v11e0
    0x11ef: v11ef(0x20) = CONST 
    0x11f1: v11f1 = ADD v11ef(0x20), v11ec
    0x11f4: v11f4(0x20) = SUB v11f1, v11ec
    0x11f6: MSTORE v11ec, v11f4(0x20)
    0x11f7: v11f7(0x3f) = CONST 
    0x11fa: MSTORE v11f1, v11f7(0x3f)
    0x11fb: v11fb(0x20) = CONST 
    0x11fd: v11fd = ADD v11fb(0x20), v11f1
    0x11ff: v11ff(0x2168) = CONST 
    0x1202: v1202(0x3f) = CONST 
    0x1205: CODECOPY v11fd, v11ff(0x2168), v1202(0x3f)
    0x1206: v1206(0x40) = CONST 
    0x1208: v1208 = ADD v1206(0x40), v11fd
    0x120c: v120c(0x40) = CONST 
    0x120e: v120e = MLOAD v120c(0x40)
    0x1211: v1211(0x84) = SUB v1208, v120e
    0x1213: REVERT v120e, v1211(0x84)

    Begin block 0x1214
    prev=[0x11bc], succ=[0x29d3]
    =================================
    0x1215: v1215(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x122b: v122b = AND v72f, v1215(0xffffffffffffffffffffffffffffffffffffffff)
    0x122c: v122c(0x0) = CONST 
    0x1230: MSTORE v122c(0x0), v122b
    0x1231: v1231(0x16) = CONST 
    0x1233: v1233(0x20) = CONST 
    0x1237: MSTORE v1233(0x20), v1231(0x16)
    0x1238: v1238(0x40) = CONST 
    0x123d: v123d = SHA3 v122c(0x0), v1238(0x40)
    0x123f: v123f = SLOAD v123d
    0x1240: v1240(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x1261: v1261 = AND v1240(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v123f
    0x1263: v1263 = ISZERO v736
    0x1264: v1264 = ISZERO v1263
    0x1267: v1267 = OR v1264, v1261
    0x126a: SSTORE v123d, v1267
    0x126c: v126c = MLOAD v1238(0x40)
    0x126f: MSTORE v126c, v1264
    0x1271: v1271 = MLOAD v1238(0x40)
    0x1272: v1272(0xcf3473b85df1594d47b6958f29a32bea0abff9dd68296f7bf33443646793cfd8) = CONST 
    0x1296: v1296(0x0) = SUB v126c, v1271
    0x1299: v1299(0x20) = ADD v1233(0x20), v1296(0x0)
    0x129b: LOG2 v1271, v1299(0x20), v1272(0xcf3473b85df1594d47b6958f29a32bea0abff9dd68296f7bf33443646793cfd8), v122b
    0x129e: JUMP v701(0x29d3)

    Begin block 0x29d3
    prev=[0x1214], succ=[]
    =================================
    0x29d4: STOP 

}

function allowance(address,address)() public {
    Begin block 0x73b
    prev=[], succ=[0x74d, 0x751]
    =================================
    0x73c: v73c(0x29f4) = CONST 
    0x73f: v73f(0x4) = CONST 
    0x742: v742 = CALLDATASIZE 
    0x743: v743 = SUB v742, v73f(0x4)
    0x744: v744(0x40) = CONST 
    0x747: v747 = LT v743, v744(0x40)
    0x748: v748 = ISZERO v747
    0x749: v749(0x751) = CONST 
    0x74c: JUMPI v749(0x751), v748

    Begin block 0x74d
    prev=[0x73b], succ=[]
    =================================
    0x74d: v74d(0x0) = CONST 
    0x750: REVERT v74d(0x0), v74d(0x0)

    Begin block 0x751
    prev=[0x73b], succ=[0x129f0x73b]
    =================================
    0x753: v753(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x769: v769 = CALLDATALOAD v73f(0x4)
    0x76b: v76b = AND v753(0xffffffffffffffffffffffffffffffffffffffff), v769
    0x76d: v76d(0x20) = CONST 
    0x76f: v76f(0x24) = ADD v76d(0x20), v73f(0x4)
    0x770: v770 = CALLDATALOAD v76f(0x24)
    0x771: v771 = AND v770, v753(0xffffffffffffffffffffffffffffffffffffffff)
    0x772: v772(0x129f) = CONST 
    0x775: JUMP v772(0x129f)

    Begin block 0x129f0x73b
    prev=[0x751], succ=[0x29f4]
    =================================
    0x12a00x73b: v73b12a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12b70x73b: v73b12b7 = AND v73b12a0(0xffffffffffffffffffffffffffffffffffffffff), v76b
    0x12b80x73b: v73b12b8(0x0) = CONST 
    0x12bc0x73b: MSTORE v73b12b8(0x0), v73b12b7
    0x12bd0x73b: v73b12bd(0xf) = CONST 
    0x12bf0x73b: v73b12bf(0x20) = CONST 
    0x12c30x73b: MSTORE v73b12bf(0x20), v73b12bd(0xf)
    0x12c40x73b: v73b12c4(0x40) = CONST 
    0x12c80x73b: v73b12c8 = SHA3 v73b12b8(0x0), v73b12c4(0x40)
    0x12cc0x73b: v73b12cc = AND v73b12a0(0xffffffffffffffffffffffffffffffffffffffff), v771
    0x12ce0x73b: MSTORE v73b12b8(0x0), v73b12cc
    0x12d20x73b: MSTORE v73b12bf(0x20), v73b12c8
    0x12d30x73b: v73b12d3 = SHA3 v73b12b8(0x0), v73b12c4(0x40)
    0x12d40x73b: v73b12d4 = SLOAD v73b12d3
    0x12d60x73b: JUMP v73c(0x29f4)

    Begin block 0x29f4
    prev=[0x129f0x73b], succ=[]
    =================================
    0x29f5: v29f5(0x40) = CONST 
    0x29f8: v29f8 = MLOAD v29f5(0x40)
    0x29fb: MSTORE v29f8, v73b12d4
    0x29fc: v29fc = MLOAD v29f5(0x40)
    0x2a00: v2a00(0x0) = SUB v29f8, v29fc
    0x2a01: v2a01(0x20) = CONST 
    0x2a03: v2a03(0x20) = ADD v2a01(0x20), v2a00(0x0)
    0x2a05: RETURN v29fc, v2a03(0x20)

}

function pendingOwner()() public {
    Begin block 0x776
    prev=[], succ=[0x12d7]
    =================================
    0x777: v777(0x2a25) = CONST 
    0x77a: v77a(0x12d7) = CONST 
    0x77d: JUMP v77a(0x12d7)

    Begin block 0x12d7
    prev=[0x776], succ=[0x2a25]
    =================================
    0x12d8: v12d8(0x1) = CONST 
    0x12da: v12da = SLOAD v12d8(0x1)
    0x12db: v12db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12f0: v12f0 = AND v12db(0xffffffffffffffffffffffffffffffffffffffff), v12da
    0x12f2: JUMP v777(0x2a25)

    Begin block 0x2a25
    prev=[0x12d7], succ=[]
    =================================
    0x2a26: v2a26(0x40) = CONST 
    0x2a29: v2a29 = MLOAD v2a26(0x40)
    0x2a2a: v2a2a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a41: v2a41 = AND v12f0, v2a2a(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a43: MSTORE v2a29, v2a41
    0x2a44: v2a44 = MLOAD v2a26(0x40)
    0x2a48: v2a48(0x0) = SUB v2a29, v2a44
    0x2a49: v2a49(0x20) = CONST 
    0x2a4b: v2a4b(0x20) = ADD v2a49(0x20), v2a48(0x0)
    0x2a4d: RETURN v2a44, v2a4b(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x77e
    prev=[], succ=[0x790, 0x794]
    =================================
    0x77f: v77f(0x2a6d) = CONST 
    0x782: v782(0x4) = CONST 
    0x785: v785 = CALLDATASIZE 
    0x786: v786 = SUB v785, v782(0x4)
    0x787: v787(0x20) = CONST 
    0x78a: v78a = LT v786, v787(0x20)
    0x78b: v78b = ISZERO v78a
    0x78c: v78c(0x794) = CONST 
    0x78f: JUMPI v78c(0x794), v78b

    Begin block 0x790
    prev=[0x77e], succ=[]
    =================================
    0x790: v790(0x0) = CONST 
    0x793: REVERT v790(0x0), v790(0x0)

    Begin block 0x794
    prev=[0x77e], succ=[0x12f3]
    =================================
    0x796: v796 = CALLDATALOAD v782(0x4)
    0x797: v797(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7ac: v7ac = AND v797(0xffffffffffffffffffffffffffffffffffffffff), v796
    0x7ad: v7ad(0x12f3) = CONST 
    0x7b0: JUMP v7ad(0x12f3)

    Begin block 0x12f3
    prev=[0x794], succ=[0x1313, 0x135f]
    =================================
    0x12f4: v12f4(0x0) = CONST 
    0x12f6: v12f6 = SLOAD v12f4(0x0)
    0x12f7: v12f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x130c: v130c = AND v12f7(0xffffffffffffffffffffffffffffffffffffffff), v12f6
    0x130d: v130d = CALLER 
    0x130e: v130e = EQ v130d, v130c
    0x130f: v130f(0x135f) = CONST 
    0x1312: JUMPI v130f(0x135f), v130e

    Begin block 0x1313
    prev=[0x12f3], succ=[]
    =================================
    0x1313: v1313(0x40) = CONST 
    0x1316: v1316 = MLOAD v1313(0x40)
    0x1317: v1317(0x461bcd) = CONST 
    0x131b: v131b(0xe5) = CONST 
    0x131d: v131d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v131b(0xe5), v1317(0x461bcd)
    0x131f: MSTORE v1316, v131d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1320: v1320(0x20) = CONST 
    0x1322: v1322(0x4) = CONST 
    0x1325: v1325 = ADD v1316, v1322(0x4)
    0x1326: MSTORE v1325, v1320(0x20)
    0x1327: v1327(0xa) = CONST 
    0x1329: v1329(0x24) = CONST 
    0x132c: v132c = ADD v1316, v1329(0x24)
    0x132d: MSTORE v132c, v1327(0xa)
    0x132e: v132e(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000) = CONST 
    0x134f: v134f(0x44) = CONST 
    0x1352: v1352 = ADD v1316, v134f(0x44)
    0x1353: MSTORE v1352, v132e(0x6f6e6c79204f776e657200000000000000000000000000000000000000000000)
    0x1355: v1355 = MLOAD v1313(0x40)
    0x1359: v1359(0x0) = SUB v1316, v1355
    0x135a: v135a(0x64) = CONST 
    0x135c: v135c(0x64) = ADD v135a(0x64), v1359(0x0)
    0x135e: REVERT v1355, v135c(0x64)

    Begin block 0x135f
    prev=[0x12f3], succ=[0x2a6d]
    =================================
    0x1360: v1360(0x1) = CONST 
    0x1363: v1363 = SLOAD v1360(0x1)
    0x1364: v1364(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1385: v1385 = AND v1364(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1363
    0x1386: v1386(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x139e: v139e = AND v1386(0xffffffffffffffffffffffffffffffffffffffff), v7ac
    0x13a2: v13a2 = OR v139e, v1385
    0x13a4: SSTORE v1360(0x1), v13a2
    0x13a5: JUMP v77f(0x2a6d)

    Begin block 0x2a6d
    prev=[0x135f], succ=[]
    =================================
    0x2a6e: STOP 

}

