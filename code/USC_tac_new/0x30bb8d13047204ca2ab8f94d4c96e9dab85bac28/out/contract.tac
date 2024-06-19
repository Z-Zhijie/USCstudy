function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x1c67]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x1c03: v1c03(0x1c67) = CONST 
    0x1c04: JUMPI v1c03(0x1c67), v8

    Begin block 0xd
    prev=[0x0], succ=[0x175, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x6fc6407c) = CONST 
    0x19: v19 = GT v14(0x6fc6407c), v12
    0x1a: v1a(0x175) = CONST 
    0x1d: JUMPI v1a(0x175), v19

    Begin block 0x175
    prev=[0xd], succ=[0x219, 0x181]
    =================================
    0x177: v177(0x3644e515) = CONST 
    0x17c: v17c = GT v177(0x3644e515), v12
    0x17d: v17d(0x219) = CONST 
    0x180: JUMPI v17d(0x219), v17c

    Begin block 0x219
    prev=[0x175], succ=[0x26b, 0x225]
    =================================
    0x21b: v21b(0x18160ddd) = CONST 
    0x220: v220 = GT v21b(0x18160ddd), v12
    0x221: v221(0x26b) = CONST 
    0x224: JUMPI v221(0x26b), v220

    Begin block 0x26b
    prev=[0x219], succ=[0x1c6a, 0x277]
    =================================
    0x26d: v26d(0x6fdde03) = CONST 
    0x272: v272 = EQ v26d(0x6fdde03), v12
    0x1c5b: v1c5b(0x1c6a) = CONST 
    0x1c5c: JUMPI v1c5b(0x1c6a), v272

    Begin block 0x1c6a
    prev=[0x26b], succ=[]
    =================================
    0x1c6b: v1c6b(0x2f6) = CONST 
    0x1c6c: CALLPRIVATE v1c6b(0x2f6)

    Begin block 0x277
    prev=[0x26b], succ=[0x1c6d, 0x282]
    =================================
    0x278: v278(0x933c1ed) = CONST 
    0x27d: v27d = EQ v278(0x933c1ed), v12
    0x1c5d: v1c5d(0x1c6d) = CONST 
    0x1c5e: JUMPI v1c5d(0x1c6d), v27d

    Begin block 0x1c6d
    prev=[0x277], succ=[]
    =================================
    0x1c6e: v1c6e(0x380) = CONST 
    0x1c6f: CALLPRIVATE v1c6e(0x380)

    Begin block 0x282
    prev=[0x277], succ=[0x1c70, 0x28d]
    =================================
    0x283: v283(0x95ea7b3) = CONST 
    0x288: v288 = EQ v283(0x95ea7b3), v12
    0x1c5f: v1c5f(0x1c70) = CONST 
    0x1c60: JUMPI v1c5f(0x1c70), v288

    Begin block 0x1c70
    prev=[0x95, 0x11f, 0x1de, 0x1f4, 0x282], succ=[]
    =================================
    0x1c71: v1c71(0x431) = CONST 
    0x1c72: CALLPRIVATE v1c71(0x431)

    Begin block 0x28d
    prev=[0x282], succ=[0x1c73, 0x298]
    =================================
    0x28e: v28e(0x11d3e6c4) = CONST 
    0x293: v293 = EQ v28e(0x11d3e6c4), v12
    0x1c61: v1c61(0x1c73) = CONST 
    0x1c62: JUMPI v1c61(0x1c73), v293

    Begin block 0x1c73
    prev=[0x28d], succ=[]
    =================================
    0x1c74: v1c74(0x47e) = CONST 
    0x1c75: CALLPRIVATE v1c74(0x47e)

    Begin block 0x298
    prev=[0x28d], succ=[0x1c76, 0x2a3]
    =================================
    0x299: v299(0x11fd8a83) = CONST 
    0x29e: v29e = EQ v299(0x11fd8a83), v12
    0x1c63: v1c63(0x1c76) = CONST 
    0x1c64: JUMPI v1c63(0x1c76), v29e

    Begin block 0x1c76
    prev=[0x298], succ=[]
    =================================
    0x1c77: v1c77(0x4a5) = CONST 
    0x1c78: CALLPRIVATE v1c77(0x4a5)

    Begin block 0x2a3
    prev=[0x298], succ=[0x1c67, 0x1c79]
    =================================
    0x2a4: v2a4(0x12d43a51) = CONST 
    0x2a9: v2a9 = EQ v2a4(0x12d43a51), v12
    0x1c65: v1c65(0x1c79) = CONST 
    0x1c66: JUMPI v1c65(0x1c79), v2a9

    Begin block 0x1c67
    prev=[0x0, 0x2a3], succ=[]
    =================================
    0x1c68: v1c68(0x2ae) = CONST 
    0x1c69: CALLPRIVATE v1c68(0x2ae)

    Begin block 0x1c79
    prev=[0x2a3], succ=[]
    =================================
    0x1c7a: v1c7a(0x4d6) = CONST 
    0x1c7b: CALLPRIVATE v1c7a(0x4d6)

    Begin block 0x225
    prev=[0x219], succ=[0x1c7c, 0x230]
    =================================
    0x226: v226(0x18160ddd) = CONST 
    0x22b: v22b = EQ v226(0x18160ddd), v12
    0x1c4f: v1c4f(0x1c7c) = CONST 
    0x1c50: JUMPI v1c4f(0x1c7c), v22b

    Begin block 0x1c7c
    prev=[0x225], succ=[]
    =================================
    0x1c7d: v1c7d(0x4eb) = CONST 
    0x1c7e: CALLPRIVATE v1c7d(0x4eb)

    Begin block 0x230
    prev=[0x225], succ=[0x1c7f, 0x23b]
    =================================
    0x231: v231(0x20606b70) = CONST 
    0x236: v236 = EQ v231(0x20606b70), v12
    0x1c51: v1c51(0x1c7f) = CONST 
    0x1c52: JUMPI v1c51(0x1c7f), v236

    Begin block 0x1c7f
    prev=[0x230], succ=[]
    =================================
    0x1c80: v1c80(0x500) = CONST 
    0x1c81: CALLPRIVATE v1c80(0x500)

    Begin block 0x23b
    prev=[0x230], succ=[0x1c82, 0x246]
    =================================
    0x23c: v23c(0x23b872dd) = CONST 
    0x241: v241 = EQ v23c(0x23b872dd), v12
    0x1c53: v1c53(0x1c82) = CONST 
    0x1c54: JUMPI v1c53(0x1c82), v241

    Begin block 0x1c82
    prev=[0xc2, 0x23b], succ=[]
    =================================
    0x1c83: v1c83(0x515) = CONST 
    0x1c84: CALLPRIVATE v1c83(0x515)

    Begin block 0x246
    prev=[0x23b], succ=[0x1c85, 0x251]
    =================================
    0x247: v247(0x25240810) = CONST 
    0x24c: v24c = EQ v247(0x25240810), v12
    0x1c55: v1c55(0x1c85) = CONST 
    0x1c56: JUMPI v1c55(0x1c85), v24c

    Begin block 0x1c85
    prev=[0x246], succ=[]
    =================================
    0x1c86: v1c86(0x558) = CONST 
    0x1c87: CALLPRIVATE v1c86(0x558)

    Begin block 0x251
    prev=[0x246], succ=[0x1c88, 0x25c]
    =================================
    0x252: v252(0x30adf81f) = CONST 
    0x257: v257 = EQ v252(0x30adf81f), v12
    0x1c57: v1c57(0x1c88) = CONST 
    0x1c58: JUMPI v1c57(0x1c88), v257

    Begin block 0x1c88
    prev=[0x251], succ=[]
    =================================
    0x1c89: v1c89(0x56d) = CONST 
    0x1c8a: CALLPRIVATE v1c89(0x56d)

    Begin block 0x25c
    prev=[0x251], succ=[0x267, 0x1c8b]
    =================================
    0x25d: v25d(0x313ce567) = CONST 
    0x262: v262 = EQ v25d(0x313ce567), v12
    0x1c59: v1c59(0x1c8b) = CONST 
    0x1c5a: JUMPI v1c59(0x1c8b), v262

    Begin block 0x267
    prev=[0x25c], succ=[]
    =================================
    0x267: v267(0x2ae) = CONST 
    0x26a: JUMP v267(0x2ae)

    Begin block 0x1c8b
    prev=[0x25c], succ=[]
    =================================
    0x1c8c: v1c8c(0x582) = CONST 
    0x1c8d: CALLPRIVATE v1c8c(0x582)

    Begin block 0x181
    prev=[0x175], succ=[0x1d2, 0x18c]
    =================================
    0x182: v182(0x4bda2e20) = CONST 
    0x187: v187 = GT v182(0x4bda2e20), v12
    0x188: v188(0x1d2) = CONST 
    0x18b: JUMPI v188(0x1d2), v187

    Begin block 0x1d2
    prev=[0x181], succ=[0x1c8e, 0x1de]
    =================================
    0x1d4: v1d4(0x3644e515) = CONST 
    0x1d9: v1d9 = EQ v1d4(0x3644e515), v12
    0x1c43: v1c43(0x1c8e) = CONST 
    0x1c44: JUMPI v1c43(0x1c8e), v1d9

    Begin block 0x1c8e
    prev=[0x1d2], succ=[]
    =================================
    0x1c8f: v1c8f(0x5ad) = CONST 
    0x1c90: CALLPRIVATE v1c8f(0x5ad)

    Begin block 0x1de
    prev=[0x1d2], succ=[0x1c70, 0x1e9]
    =================================
    0x1df: v1df(0x39509351) = CONST 
    0x1e4: v1e4 = EQ v1df(0x39509351), v12
    0x1c45: v1c45(0x1c70) = CONST 
    0x1c46: JUMPI v1c45(0x1c70), v1e4

    Begin block 0x1e9
    prev=[0x1de], succ=[0x1c91, 0x1f4]
    =================================
    0x1ea: v1ea(0x3af9e669) = CONST 
    0x1ef: v1ef = EQ v1ea(0x3af9e669), v12
    0x1c47: v1c47(0x1c91) = CONST 
    0x1c48: JUMPI v1c47(0x1c91), v1ef

    Begin block 0x1c91
    prev=[0xa1, 0x145, 0x1e9], succ=[]
    =================================
    0x1c92: v1c92(0x5c2) = CONST 
    0x1c93: CALLPRIVATE v1c92(0x5c2)

    Begin block 0x1f4
    prev=[0x1e9], succ=[0x1c70, 0x1ff]
    =================================
    0x1f5: v1f5(0x40c10f19) = CONST 
    0x1fa: v1fa = EQ v1f5(0x40c10f19), v12
    0x1c49: v1c49(0x1c70) = CONST 
    0x1c4a: JUMPI v1c49(0x1c70), v1fa

    Begin block 0x1ff
    prev=[0x1f4], succ=[0x1c94, 0x20a]
    =================================
    0x200: v200(0x4487152f) = CONST 
    0x205: v205 = EQ v200(0x4487152f), v12
    0x1c4b: v1c4b(0x1c94) = CONST 
    0x1c4c: JUMPI v1c4b(0x1c94), v205

    Begin block 0x1c94
    prev=[0x1ff], succ=[]
    =================================
    0x1c95: v1c95(0x5f5) = CONST 
    0x1c96: CALLPRIVATE v1c95(0x5f5)

    Begin block 0x20a
    prev=[0x1ff], succ=[0x215, 0x1c97]
    =================================
    0x20b: v20b(0x47dfe70d) = CONST 
    0x210: v210 = EQ v20b(0x47dfe70d), v12
    0x1c4d: v1c4d(0x1c97) = CONST 
    0x1c4e: JUMPI v1c4d(0x1c97), v210

    Begin block 0x215
    prev=[0x20a], succ=[]
    =================================
    0x215: v215(0x2ae) = CONST 
    0x218: JUMP v215(0x2ae)

    Begin block 0x1c97
    prev=[0x60, 0x114, 0x150, 0x1ad, 0x20a], succ=[]
    =================================
    0x1c98: v1c98(0x6a6) = CONST 
    0x1c99: CALLPRIVATE v1c98(0x6a6)

    Begin block 0x18c
    prev=[0x181], succ=[0x1c9a, 0x197]
    =================================
    0x18d: v18d(0x4bda2e20) = CONST 
    0x192: v192 = EQ v18d(0x4bda2e20), v12
    0x1c37: v1c37(0x1c9a) = CONST 
    0x1c38: JUMPI v1c37(0x1c9a), v192

    Begin block 0x1c9a
    prev=[0x18c], succ=[]
    =================================
    0x1c9b: v1c9b(0x6db) = CONST 
    0x1c9c: CALLPRIVATE v1c9b(0x6db)

    Begin block 0x197
    prev=[0x18c], succ=[0x1c9d, 0x1a2]
    =================================
    0x198: v198(0x555bcc40) = CONST 
    0x19d: v19d = EQ v198(0x555bcc40), v12
    0x1c39: v1c39(0x1c9d) = CONST 
    0x1c3a: JUMPI v1c39(0x1c9d), v19d

    Begin block 0x1c9d
    prev=[0x197], succ=[]
    =================================
    0x1c9e: v1c9e(0x6f0) = CONST 
    0x1c9f: CALLPRIVATE v1c9e(0x6f0)

    Begin block 0x1a2
    prev=[0x197], succ=[0x1ca0, 0x1ad]
    =================================
    0x1a3: v1a3(0x587cde1e) = CONST 
    0x1a8: v1a8 = EQ v1a3(0x587cde1e), v12
    0x1c3b: v1c3b(0x1ca0) = CONST 
    0x1c3c: JUMPI v1c3b(0x1ca0), v1a8

    Begin block 0x1ca0
    prev=[0x1a2], succ=[]
    =================================
    0x1ca1: v1ca1(0x7b8) = CONST 
    0x1ca2: CALLPRIVATE v1ca1(0x7b8)

    Begin block 0x1ad
    prev=[0x1a2], succ=[0x1c97, 0x1b8]
    =================================
    0x1ae: v1ae(0x5c19a95c) = CONST 
    0x1b3: v1b3 = EQ v1ae(0x5c19a95c), v12
    0x1c3d: v1c3d(0x1c97) = CONST 
    0x1c3e: JUMPI v1c3d(0x1c97), v1b3

    Begin block 0x1b8
    prev=[0x1ad], succ=[0x1ca3, 0x1c3]
    =================================
    0x1b9: v1b9(0x5c60da1b) = CONST 
    0x1be: v1be = EQ v1b9(0x5c60da1b), v12
    0x1c3f: v1c3f(0x1ca3) = CONST 
    0x1c40: JUMPI v1c3f(0x1ca3), v1be

    Begin block 0x1ca3
    prev=[0x1b8], succ=[]
    =================================
    0x1ca4: v1ca4(0x7db) = CONST 
    0x1ca5: CALLPRIVATE v1ca4(0x7db)

    Begin block 0x1c3
    prev=[0x1b8], succ=[0x1ce, 0x1ca6]
    =================================
    0x1c4: v1c4(0x64dd48f5) = CONST 
    0x1c9: v1c9 = EQ v1c4(0x64dd48f5), v12
    0x1c41: v1c41(0x1ca6) = CONST 
    0x1c42: JUMPI v1c41(0x1ca6), v1c9

    Begin block 0x1ce
    prev=[0x1c3], succ=[]
    =================================
    0x1ce: v1ce(0x2ae) = CONST 
    0x1d1: JUMP v1ce(0x2ae)

    Begin block 0x1ca6
    prev=[0x1c3], succ=[]
    =================================
    0x1ca7: v1ca7(0x7f0) = CONST 
    0x1ca8: CALLPRIVATE v1ca7(0x7f0)

    Begin block 0x1e
    prev=[0xd], succ=[0xdc, 0x29]
    =================================
    0x1f: v1f(0xa9059cbb) = CONST 
    0x24: v24 = GT v1f(0xa9059cbb), v12
    0x25: v25(0xdc) = CONST 
    0x28: JUMPI v25(0xdc), v24

    Begin block 0xdc
    prev=[0x1e], succ=[0x12e, 0xe8]
    =================================
    0xde: vde(0x7cd07e47) = CONST 
    0xe3: ve3 = GT vde(0x7cd07e47), v12
    0xe4: ve4(0x12e) = CONST 
    0xe7: JUMPI ve4(0x12e), ve3

    Begin block 0x12e
    prev=[0xdc], succ=[0x1ca9, 0x13a]
    =================================
    0x130: v130(0x6fc6407c) = CONST 
    0x135: v135 = EQ v130(0x6fc6407c), v12
    0x1c2b: v1c2b(0x1ca9) = CONST 
    0x1c2c: JUMPI v1c2b(0x1ca9), v135

    Begin block 0x1ca9
    prev=[0x12e], succ=[]
    =================================
    0x1caa: v1caa(0x805) = CONST 
    0x1cab: CALLPRIVATE v1caa(0x805)

    Begin block 0x13a
    prev=[0x12e], succ=[0x1cac, 0x145]
    =================================
    0x13b: v13b(0x6fcfff45) = CONST 
    0x140: v140 = EQ v13b(0x6fcfff45), v12
    0x1c2d: v1c2d(0x1cac) = CONST 
    0x1c2e: JUMPI v1c2d(0x1cac), v140

    Begin block 0x1cac
    prev=[0x13a], succ=[]
    =================================
    0x1cad: v1cad(0x81a) = CONST 
    0x1cae: CALLPRIVATE v1cad(0x81a)

    Begin block 0x145
    prev=[0x13a], succ=[0x1c91, 0x150]
    =================================
    0x146: v146(0x70a08231) = CONST 
    0x14b: v14b = EQ v146(0x70a08231), v12
    0x1c2f: v1c2f(0x1c91) = CONST 
    0x1c30: JUMPI v1c2f(0x1c91), v14b

    Begin block 0x150
    prev=[0x145], succ=[0x1c97, 0x15b]
    =================================
    0x151: v151(0x73f03dff) = CONST 
    0x156: v156 = EQ v151(0x73f03dff), v12
    0x1c31: v1c31(0x1c97) = CONST 
    0x1c32: JUMPI v1c31(0x1c97), v156

    Begin block 0x15b
    prev=[0x150], succ=[0x1caf, 0x166]
    =================================
    0x15c: v15c(0x782d6fe1) = CONST 
    0x161: v161 = EQ v15c(0x782d6fe1), v12
    0x1c33: v1c33(0x1caf) = CONST 
    0x1c34: JUMPI v1c33(0x1caf), v161

    Begin block 0x1caf
    prev=[0x15b], succ=[]
    =================================
    0x1cb0: v1cb0(0x866) = CONST 
    0x1cb1: CALLPRIVATE v1cb0(0x866)

    Begin block 0x166
    prev=[0x15b], succ=[0x171, 0x1cb2]
    =================================
    0x167: v167(0x7af548c1) = CONST 
    0x16c: v16c = EQ v167(0x7af548c1), v12
    0x1c35: v1c35(0x1cb2) = CONST 
    0x1c36: JUMPI v1c35(0x1cb2), v16c

    Begin block 0x171
    prev=[0x166], succ=[]
    =================================
    0x171: v171(0x2ae) = CONST 
    0x174: JUMP v171(0x2ae)

    Begin block 0x1cb2
    prev=[0x166], succ=[]
    =================================
    0x1cb3: v1cb3(0x89f) = CONST 
    0x1cb4: CALLPRIVATE v1cb3(0x89f)

    Begin block 0xe8
    prev=[0xdc], succ=[0x1cb5, 0xf3]
    =================================
    0xe9: ve9(0x7cd07e47) = CONST 
    0xee: vee = EQ ve9(0x7cd07e47), v12
    0x1c1f: v1c1f(0x1cb5) = CONST 
    0x1c20: JUMPI v1c1f(0x1cb5), vee

    Begin block 0x1cb5
    prev=[0xe8], succ=[]
    =================================
    0x1cb6: v1cb6(0x8d7) = CONST 
    0x1cb7: CALLPRIVATE v1cb6(0x8d7)

    Begin block 0xf3
    prev=[0xe8], succ=[0x1cb8, 0xfe]
    =================================
    0xf4: vf4(0x7ecebe00) = CONST 
    0xf9: vf9 = EQ vf4(0x7ecebe00), v12
    0x1c21: v1c21(0x1cb8) = CONST 
    0x1c22: JUMPI v1c21(0x1cb8), vf9

    Begin block 0x1cb8
    prev=[0xf3], succ=[]
    =================================
    0x1cb9: v1cb9(0x8ec) = CONST 
    0x1cba: CALLPRIVATE v1cb9(0x8ec)

    Begin block 0xfe
    prev=[0xf3], succ=[0x1cbb, 0x109]
    =================================
    0xff: vff(0x95d89b41) = CONST 
    0x104: v104 = EQ vff(0x95d89b41), v12
    0x1c23: v1c23(0x1cbb) = CONST 
    0x1c24: JUMPI v1c23(0x1cbb), v104

    Begin block 0x1cbb
    prev=[0xfe], succ=[]
    =================================
    0x1cbc: v1cbc(0x91f) = CONST 
    0x1cbd: CALLPRIVATE v1cbc(0x91f)

    Begin block 0x109
    prev=[0xfe], succ=[0x1cbe, 0x114]
    =================================
    0x10a: v10a(0x97d63f93) = CONST 
    0x10f: v10f = EQ v10a(0x97d63f93), v12
    0x1c25: v1c25(0x1cbe) = CONST 
    0x1c26: JUMPI v1c25(0x1cbe), v10f

    Begin block 0x1cbe
    prev=[0x109], succ=[]
    =================================
    0x1cbf: v1cbf(0x934) = CONST 
    0x1cc0: CALLPRIVATE v1cbf(0x934)

    Begin block 0x114
    prev=[0x109], succ=[0x1c97, 0x11f]
    =================================
    0x115: v115(0x98dca210) = CONST 
    0x11a: v11a = EQ v115(0x98dca210), v12
    0x1c27: v1c27(0x1c97) = CONST 
    0x1c28: JUMPI v1c27(0x1c97), v11a

    Begin block 0x11f
    prev=[0x114], succ=[0x12a, 0x1c70]
    =================================
    0x120: v120(0xa457c2d7) = CONST 
    0x125: v125 = EQ v120(0xa457c2d7), v12
    0x1c29: v1c29(0x1c70) = CONST 
    0x1c2a: JUMPI v1c29(0x1c70), v125

    Begin block 0x12a
    prev=[0x11f], succ=[]
    =================================
    0x12a: v12a(0x2ae) = CONST 
    0x12d: JUMP v12a(0x2ae)

    Begin block 0x29
    prev=[0x1e], succ=[0x95, 0x34]
    =================================
    0x2a: v2a(0xdd62ed3e) = CONST 
    0x2f: v2f = GT v2a(0xdd62ed3e), v12
    0x30: v30(0x95) = CONST 
    0x33: JUMPI v30(0x95), v2f

    Begin block 0x95
    prev=[0x29], succ=[0x1c70, 0xa1]
    =================================
    0x97: v97(0xa9059cbb) = CONST 
    0x9c: v9c = EQ v97(0xa9059cbb), v12
    0x1c13: v1c13(0x1c70) = CONST 
    0x1c14: JUMPI v1c13(0x1c70), v9c

    Begin block 0xa1
    prev=[0x95], succ=[0x1c91, 0xac]
    =================================
    0xa2: va2(0xb4b5ea57) = CONST 
    0xa7: va7 = EQ va2(0xb4b5ea57), v12
    0x1c15: v1c15(0x1c91) = CONST 
    0x1c16: JUMPI v1c15(0x1c91), va7

    Begin block 0xac
    prev=[0xa1], succ=[0x1cc1, 0xb7]
    =================================
    0xad: vad(0xbb4490a7) = CONST 
    0xb2: vb2 = EQ vad(0xbb4490a7), v12
    0x1c17: v1c17(0x1cc1) = CONST 
    0x1c18: JUMPI v1c17(0x1cc1), vb2

    Begin block 0x1cc1
    prev=[0x7b, 0xac], succ=[]
    =================================
    0x1cc2: v1cc2(0x949) = CONST 
    0x1cc3: CALLPRIVATE v1cc2(0x949)

    Begin block 0xb7
    prev=[0xac], succ=[0x1cc4, 0xc2]
    =================================
    0xb8: vb8(0xc3cda520) = CONST 
    0xbd: vbd = EQ vb8(0xc3cda520), v12
    0x1c19: v1c19(0x1cc4) = CONST 
    0x1c1a: JUMPI v1c19(0x1cc4), vbd

    Begin block 0x1cc4
    prev=[0xb7], succ=[]
    =================================
    0x1cc5: v1cc5(0x973) = CONST 
    0x1cc6: CALLPRIVATE v1cc5(0x973)

    Begin block 0xc2
    prev=[0xb7], succ=[0x1c82, 0xcd]
    =================================
    0xc3: vc3(0xcea9d26f) = CONST 
    0xc8: vc8 = EQ vc3(0xcea9d26f), v12
    0x1c1b: v1c1b(0x1c82) = CONST 
    0x1c1c: JUMPI v1c1b(0x1c82), vc8

    Begin block 0xcd
    prev=[0xc2], succ=[0xd8, 0x1cc7]
    =================================
    0xce: vce(0xd505accf) = CONST 
    0xd3: vd3 = EQ vce(0xd505accf), v12
    0x1c1d: v1c1d(0x1cc7) = CONST 
    0x1c1e: JUMPI v1c1d(0x1cc7), vd3

    Begin block 0xd8
    prev=[0xcd], succ=[]
    =================================
    0xd8: vd8(0x2ae) = CONST 
    0xdb: JUMP vd8(0x2ae)

    Begin block 0x1cc7
    prev=[0xcd], succ=[]
    =================================
    0x1cc8: v1cc8(0x9c7) = CONST 
    0x1cc9: CALLPRIVATE v1cc8(0x9c7)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x6f]
    =================================
    0x35: v35(0xe9299f40) = CONST 
    0x3a: v3a = GT v35(0xe9299f40), v12
    0x3b: v3b(0x6f) = CONST 
    0x3e: JUMPI v3b(0x6f), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x1cd0, 0x4a]
    =================================
    0x40: v40(0xe9299f40) = CONST 
    0x45: v45 = EQ v40(0xe9299f40), v12
    0x1c05: v1c05(0x1cd0) = CONST 
    0x1c06: JUMPI v1c05(0x1cd0), v45

    Begin block 0x1cd0
    prev=[0x3f], succ=[]
    =================================
    0x1cd1: v1cd1(0xa75) = CONST 
    0x1cd2: CALLPRIVATE v1cd1(0xa75)

    Begin block 0x4a
    prev=[0x3f], succ=[0x1cd3, 0x55]
    =================================
    0x4b: v4b(0xec342ad0) = CONST 
    0x50: v50 = EQ v4b(0xec342ad0), v12
    0x1c07: v1c07(0x1cd3) = CONST 
    0x1c08: JUMPI v1c07(0x1cd3), v50

    Begin block 0x1cd3
    prev=[0x4a], succ=[]
    =================================
    0x1cd4: v1cd4(0xa8a) = CONST 
    0x1cd5: CALLPRIVATE v1cd4(0xa8a)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0x1cd6]
    =================================
    0x56: v56(0xf1127ed8) = CONST 
    0x5b: v5b = EQ v56(0xf1127ed8), v12
    0x1c09: v1c09(0x1cd6) = CONST 
    0x1c0a: JUMPI v1c09(0x1cd6), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x6b, 0x1c97]
    =================================
    0x61: v61(0xfa8f3455) = CONST 
    0x66: v66 = EQ v61(0xfa8f3455), v12
    0x1c0b: v1c0b(0x1c97) = CONST 
    0x1c0c: JUMPI v1c0b(0x1c97), v66

    Begin block 0x6b
    prev=[0x60], succ=[]
    =================================
    0x6b: v6b(0x2ae) = CONST 
    0x6e: JUMP v6b(0x2ae)

    Begin block 0x1cd6
    prev=[0x55], succ=[]
    =================================
    0x1cd7: v1cd7(0xa9f) = CONST 
    0x1cd8: CALLPRIVATE v1cd7(0xa9f)

    Begin block 0x6f
    prev=[0x34], succ=[0x1cca, 0x7b]
    =================================
    0x71: v71(0xdd62ed3e) = CONST 
    0x76: v76 = EQ v71(0xdd62ed3e), v12
    0x1c0d: v1c0d(0x1cca) = CONST 
    0x1c0e: JUMPI v1c0d(0x1cca), v76

    Begin block 0x1cca
    prev=[0x6f], succ=[]
    =================================
    0x1ccb: v1ccb(0xa25) = CONST 
    0x1ccc: CALLPRIVATE v1ccb(0xa25)

    Begin block 0x7b
    prev=[0x6f], succ=[0x1cc1, 0x86]
    =================================
    0x7c: v7c(0xe18120cc) = CONST 
    0x81: v81 = EQ v7c(0xe18120cc), v12
    0x1c0f: v1c0f(0x1cc1) = CONST 
    0x1c10: JUMPI v1c0f(0x1cc1), v81

    Begin block 0x86
    prev=[0x7b], succ=[0x91, 0x1ccd]
    =================================
    0x87: v87(0xe7a324dc) = CONST 
    0x8c: v8c = EQ v87(0xe7a324dc), v12
    0x1c11: v1c11(0x1ccd) = CONST 
    0x1c12: JUMPI v1c11(0x1ccd), v8c

    Begin block 0x91
    prev=[0x86], succ=[]
    =================================
    0x91: v91(0x2ae) = CONST 
    0x94: JUMP v91(0x2ae)

    Begin block 0x1ccd
    prev=[0x86], succ=[]
    =================================
    0x1cce: v1cce(0xa60) = CONST 
    0x1ccf: CALLPRIVATE v1cce(0xa60)

}

function 0x1141(0x1141arg0x0) private {
    Begin block 0x1141
    prev=[], succ=[0x1bd4, 0x117e]
    =================================
    0x1142: v1142(0x2) = CONST 
    0x1145: v1145 = SLOAD v1142(0x2)
    0x1146: v1146(0x40) = CONST 
    0x1149: v1149 = MLOAD v1146(0x40)
    0x114a: v114a(0x20) = CONST 
    0x114c: v114c(0x1) = CONST 
    0x114f: v114f = AND v1145, v114c(0x1)
    0x1150: v1150 = ISZERO v114f
    0x1151: v1151(0x100) = CONST 
    0x1154: v1154 = MUL v1151(0x100), v1150
    0x1155: v1155(0x0) = CONST 
    0x1157: v1157(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1155(0x0)
    0x1158: v1158 = ADD v1157(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1154
    0x115b: v115b = AND v1145, v1158
    0x115e: v115e = DIV v115b, v1142(0x2)
    0x115f: v115f(0x1f) = CONST 
    0x1162: v1162 = ADD v115e, v115f(0x1f)
    0x1165: v1165 = DIV v1162, v114a(0x20)
    0x1167: v1167 = MUL v114a(0x20), v1165
    0x1169: v1169 = ADD v1149, v1167
    0x116b: v116b = ADD v114a(0x20), v1169
    0x116e: MSTORE v1146(0x40), v116b
    0x1171: MSTORE v1149, v115e
    0x1175: v1175 = ADD v1149, v114a(0x20)
    0x1179: v1179 = ISZERO v115e
    0x117a: v117a(0x1bd4) = CONST 
    0x117d: JUMPI v117a(0x1bd4), v1179

    Begin block 0x1bd4
    prev=[0x1141], succ=[]
    =================================
    0x1bdb: RETURNPRIVATE v1141arg0, v1149, v1141arg0

    Begin block 0x117e
    prev=[0x1141], succ=[0x1186, 0xbe00x1141]
    =================================
    0x117f: v117f(0x1f) = CONST 
    0x1181: v1181 = LT v117f(0x1f), v115e
    0x1182: v1182(0xbe0) = CONST 
    0x1185: JUMPI v1182(0xbe0), v1181

    Begin block 0x1186
    prev=[0x117e], succ=[0x1bfb]
    =================================
    0x1186: v1186(0x100) = CONST 
    0x118b: v118b = SLOAD v1142(0x2)
    0x118c: v118c = DIV v118b, v1186(0x100)
    0x118d: v118d = MUL v118c, v1186(0x100)
    0x118f: MSTORE v1175, v118d
    0x1191: v1191(0x20) = CONST 
    0x1193: v1193 = ADD v1191(0x20), v1175
    0x1195: v1195(0x1bfb) = CONST 
    0x1198: JUMP v1195(0x1bfb)

    Begin block 0x1bfb
    prev=[0x1186], succ=[]
    =================================
    0x1c02: RETURNPRIVATE v1141arg0, v1149, v1141arg0

    Begin block 0xbe00x1141
    prev=[0x117e], succ=[0xbee0x1141]
    =================================
    0xbe20x1141: v1141be2 = ADD v1175, v115e
    0xbe50x1141: v1141be5(0x0) = CONST 
    0xbe70x1141: MSTORE v1141be5(0x0), v1142(0x2)
    0xbe80x1141: v1141be8(0x20) = CONST 
    0xbea0x1141: v1141bea(0x0) = CONST 
    0xbec0x1141: v1141bec = SHA3 v1141bea(0x0), v1141be8(0x20)

    Begin block 0xbee0x1141
    prev=[0xbee0x1141, 0xbe00x1141], succ=[0xbee0x1141, 0xc020x1141]
    =================================
    0xbee0x1141_0x0: vbee1141_0 = PHI v1175, v1141bfa
    0xbee0x1141_0x1: vbee1141_1 = PHI v1141bf6, v1141bec
    0xbf00x1141: v1141bf0 = SLOAD vbee1141_1
    0xbf20x1141: MSTORE vbee1141_0, v1141bf0
    0xbf40x1141: v1141bf4(0x1) = CONST 
    0xbf60x1141: v1141bf6 = ADD v1141bf4(0x1), vbee1141_1
    0xbf80x1141: v1141bf8(0x20) = CONST 
    0xbfa0x1141: v1141bfa = ADD v1141bf8(0x20), vbee1141_0
    0xbfd0x1141: v1141bfd = GT v1141be2, v1141bfa
    0xbfe0x1141: v1141bfe(0xbee) = CONST 
    0xc010x1141: JUMPI v1141bfe(0xbee), v1141bfd

    Begin block 0xc020x1141
    prev=[0xbee0x1141], succ=[0xc0b0x1141]
    =================================
    0xc040x1141: v1141c04 = SUB v1141bfa, v1141be2
    0xc050x1141: v1141c05(0x1f) = CONST 
    0xc070x1141: v1141c07 = AND v1141c05(0x1f), v1141c04
    0xc090x1141: v1141c09 = ADD v1141be2, v1141c07

    Begin block 0xc0b0x1141
    prev=[0xc020x1141], succ=[]
    =================================
    0xc120x1141: RETURNPRIVATE v1141arg0, v1149, v1141arg0

}

function 0x121c(0x121carg0x0, 0x121carg0x1, 0x121carg0x2) private {
    Begin block 0x121c
    prev=[], succ=[0x123d]
    =================================
    0x121d: v121d(0x60) = CONST 
    0x121f: v121f(0x0) = CONST 
    0x1221: v1221(0x60) = CONST 
    0x1224: v1224(0x1) = CONST 
    0x1226: v1226(0x1) = CONST 
    0x1228: v1228(0xa0) = CONST 
    0x122a: v122a(0x10000000000000000000000000000000000000000) = SHL v1228(0xa0), v1226(0x1)
    0x122b: v122b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v122a(0x10000000000000000000000000000000000000000), v1224(0x1)
    0x122c: v122c = AND v122b(0xffffffffffffffffffffffffffffffffffffffff), v121carg1
    0x122e: v122e(0x40) = CONST 
    0x1230: v1230 = MLOAD v122e(0x40)
    0x1234: v1234 = MLOAD v121carg0
    0x1236: v1236(0x20) = CONST 
    0x1238: v1238 = ADD v1236(0x20), v121carg0

    Begin block 0x123d
    prev=[0x121c, 0x1246], succ=[0x125c, 0x1246]
    =================================
    0x123d_0x2: v123d_2 = PHI v1234, v124f
    0x123e: v123e(0x20) = CONST 
    0x1241: v1241 = LT v123d_2, v123e(0x20)
    0x1242: v1242(0x125c) = CONST 
    0x1245: JUMPI v1242(0x125c), v1241

    Begin block 0x125c
    prev=[0x123d], succ=[0x129b, 0x12bc]
    =================================
    0x125c_0x0: v125c_0 = PHI v1238, v1257
    0x125c_0x1: v125c_1 = PHI v1230, v1255
    0x125c_0x2: v125c_2 = PHI v1234, v124f
    0x125d: v125d(0x1) = CONST 
    0x1260: v1260(0x20) = CONST 
    0x1262: v1262 = SUB v1260(0x20), v125c_2
    0x1263: v1263(0x100) = CONST 
    0x1266: v1266 = EXP v1263(0x100), v1262
    0x1267: v1267 = SUB v1266, v125d(0x1)
    0x1269: v1269 = NOT v1267
    0x126b: v126b = MLOAD v125c_0
    0x126c: v126c = AND v126b, v1269
    0x126f: v126f = MLOAD v125c_1
    0x1270: v1270 = AND v126f, v1267
    0x1273: v1273 = OR v126c, v1270
    0x1275: MSTORE v125c_1, v1273
    0x127e: v127e = ADD v1234, v1230
    0x1282: v1282(0x0) = CONST 
    0x1284: v1284(0x40) = CONST 
    0x1286: v1286 = MLOAD v1284(0x40)
    0x1289: v1289 = SUB v127e, v1286
    0x128c: v128c = GAS 
    0x128d: v128d = DELEGATECALL v128c, v122c, v1286, v1289, v1286, v1282(0x0)
    0x1291: v1291 = RETURNDATASIZE 
    0x1293: v1293(0x0) = CONST 
    0x1296: v1296 = EQ v1291, v1293(0x0)
    0x1297: v1297(0x12bc) = CONST 
    0x129a: JUMPI v1297(0x12bc), v1296

    Begin block 0x129b
    prev=[0x125c], succ=[0x12c1]
    =================================
    0x129b: v129b(0x40) = CONST 
    0x129d: v129d = MLOAD v129b(0x40)
    0x12a0: v12a0(0x1f) = CONST 
    0x12a2: v12a2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v12a0(0x1f)
    0x12a3: v12a3(0x3f) = CONST 
    0x12a5: v12a5 = RETURNDATASIZE 
    0x12a6: v12a6 = ADD v12a5, v12a3(0x3f)
    0x12a7: v12a7 = AND v12a6, v12a2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a9: v12a9 = ADD v129d, v12a7
    0x12aa: v12aa(0x40) = CONST 
    0x12ac: MSTORE v12aa(0x40), v12a9
    0x12ad: v12ad = RETURNDATASIZE 
    0x12af: MSTORE v129d, v12ad
    0x12b0: v12b0 = RETURNDATASIZE 
    0x12b1: v12b1(0x0) = CONST 
    0x12b3: v12b3(0x20) = CONST 
    0x12b6: v12b6 = ADD v129d, v12b3(0x20)
    0x12b7: RETURNDATACOPY v12b6, v12b1(0x0), v12b0
    0x12b8: v12b8(0x12c1) = CONST 
    0x12bb: JUMP v12b8(0x12c1)

    Begin block 0x12c1
    prev=[0x129b, 0x12bc], succ=[0x12d0, 0x12d6]
    =================================
    0x12c7: v12c7(0x0) = CONST 
    0x12ca: v12ca = EQ v128d, v12c7(0x0)
    0x12cb: v12cb = ISZERO v12ca
    0x12cc: v12cc(0x12d6) = CONST 
    0x12cf: JUMPI v12cc(0x12d6), v12cb

    Begin block 0x12d0
    prev=[0x12c1], succ=[]
    =================================
    0x12d0: v12d0 = RETURNDATASIZE 
    0x12d0_0x0: v12d0_0 = PHI v129d, v12bd(0x60)
    0x12d1: v12d1(0x20) = CONST 
    0x12d4: v12d4 = ADD v12d0_0, v12d1(0x20)
    0x12d5: REVERT v12d4, v12d0

    Begin block 0x12d6
    prev=[0x12c1], succ=[]
    =================================
    0x12d6_0x0: v12d6_0 = PHI v129d, v12bd(0x60)
    0x12dd: RETURNPRIVATE v121carg2, v12d6_0

    Begin block 0x12bc
    prev=[0x125c], succ=[0x12c1]
    =================================
    0x12bd: v12bd(0x60) = CONST 

    Begin block 0x1246
    prev=[0x123d], succ=[0x123d]
    =================================
    0x1246_0x0: v1246_0 = PHI v1238, v1257
    0x1246_0x1: v1246_1 = PHI v1230, v1255
    0x1246_0x2: v1246_2 = PHI v1234, v124f
    0x1247: v1247 = MLOAD v1246_0
    0x1249: MSTORE v1246_1, v1247
    0x124a: v124a(0x1f) = CONST 
    0x124c: v124c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v124a(0x1f)
    0x124f: v124f = ADD v1246_2, v124c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x1251: v1251(0x20) = CONST 
    0x1255: v1255 = ADD v1251(0x20), v1246_1
    0x1257: v1257 = ADD v1251(0x20), v1246_0
    0x1258: v1258(0x123d) = CONST 
    0x125b: JUMP v1258(0x123d)

}

function fallback()() public {
    Begin block 0x2ae
    prev=[], succ=[0x2b5, 0x2eb]
    =================================
    0x2af: v2af = CALLVALUE 
    0x2b0: v2b0 = ISZERO v2af
    0x2b1: v2b1(0x2eb) = CONST 
    0x2b4: JUMPI v2b1(0x2eb), v2b0

    Begin block 0x2b5
    prev=[0x2ae], succ=[]
    =================================
    0x2b5: v2b5(0x40) = CONST 
    0x2b7: v2b7 = MLOAD v2b5(0x40)
    0x2b8: v2b8(0x461bcd) = CONST 
    0x2bc: v2bc(0xe5) = CONST 
    0x2be: v2be(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2bc(0xe5), v2b8(0x461bcd)
    0x2c0: MSTORE v2b7, v2be(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2c1: v2c1(0x4) = CONST 
    0x2c3: v2c3 = ADD v2c1(0x4), v2b7
    0x2c6: v2c6(0x20) = CONST 
    0x2c8: v2c8 = ADD v2c6(0x20), v2c3
    0x2cb: v2cb(0x20) = SUB v2c8, v2c3
    0x2cd: MSTORE v2c3, v2cb(0x20)
    0x2ce: v2ce(0x35) = CONST 
    0x2d1: MSTORE v2c8, v2ce(0x35)
    0x2d2: v2d2(0x20) = CONST 
    0x2d4: v2d4 = ADD v2d2(0x20), v2c8
    0x2d6: v2d6(0x147a) = CONST 
    0x2d9: v2d9(0x35) = CONST 
    0x2dc: CODECOPY v2d4, v2d6(0x147a), v2d9(0x35)
    0x2dd: v2dd(0x40) = CONST 
    0x2df: v2df = ADD v2dd(0x40), v2d4
    0x2e3: v2e3(0x40) = CONST 
    0x2e5: v2e5 = MLOAD v2e3(0x40)
    0x2e8: v2e8(0x84) = SUB v2df, v2e5
    0x2ea: REVERT v2e5, v2e8(0x84)

    Begin block 0x2eb
    prev=[0x2ae], succ=[0xafe0x2ae]
    =================================
    0x2ec: v2ec(0x2f3) = CONST 
    0x2ef: v2ef(0xafe) = CONST 
    0x2f2: JUMP v2ef(0xafe)

    Begin block 0xafe0x2ae
    prev=[0x2eb], succ=[0xb450x2ae, 0xb660x2ae]
    =================================
    0xaff0x2ae: v2aeaff(0x12) = CONST 
    0xb010x2ae: v2aeb01 = SLOAD v2aeaff(0x12)
    0xb020x2ae: v2aeb02(0x40) = CONST 
    0xb040x2ae: v2aeb04 = MLOAD v2aeb02(0x40)
    0xb050x2ae: v2aeb05(0x60) = CONST 
    0xb080x2ae: v2aeb08(0x0) = CONST 
    0xb0b0x2ae: v2aeb0b(0x1) = CONST 
    0xb0d0x2ae: v2aeb0d(0x1) = CONST 
    0xb0f0x2ae: v2aeb0f(0xa0) = CONST 
    0xb110x2ae: v2aeb11(0x10000000000000000000000000000000000000000) = SHL v2aeb0f(0xa0), v2aeb0d(0x1)
    0xb120x2ae: v2aeb12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2aeb11(0x10000000000000000000000000000000000000000), v2aeb0b(0x1)
    0xb150x2ae: v2aeb15 = AND v2aeb01, v2aeb12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x2ae: v2aeb19 = CALLDATASIZE 
    0xb210x2ae: CALLDATACOPY v2aeb04, v2aeb08(0x0), v2aeb19
    0xb220x2ae: v2aeb22(0x40) = CONST 
    0xb240x2ae: v2aeb24 = MLOAD v2aeb22(0x40)
    0xb260x2ae: v2aeb26 = ADD v2aeb04, v2aeb19
    0xb290x2ae: v2aeb29(0x0) = CONST 
    0xb330x2ae: v2aeb33 = SUB v2aeb26, v2aeb24
    0xb360x2ae: v2aeb36 = GAS 
    0xb370x2ae: v2aeb37 = DELEGATECALL v2aeb36, v2aeb15, v2aeb24, v2aeb33, v2aeb24, v2aeb29(0x0)
    0xb3b0x2ae: v2aeb3b = RETURNDATASIZE 
    0xb3d0x2ae: v2aeb3d(0x0) = CONST 
    0xb400x2ae: v2aeb40 = EQ v2aeb3b, v2aeb3d(0x0)
    0xb410x2ae: v2aeb41(0xb66) = CONST 
    0xb440x2ae: JUMPI v2aeb41(0xb66), v2aeb40

    Begin block 0xb450x2ae
    prev=[0xafe0x2ae], succ=[0xb6b0x2ae]
    =================================
    0xb450x2ae: v2aeb45(0x40) = CONST 
    0xb470x2ae: v2aeb47 = MLOAD v2aeb45(0x40)
    0xb4a0x2ae: v2aeb4a(0x1f) = CONST 
    0xb4c0x2ae: v2aeb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2aeb4a(0x1f)
    0xb4d0x2ae: v2aeb4d(0x3f) = CONST 
    0xb4f0x2ae: v2aeb4f = RETURNDATASIZE 
    0xb500x2ae: v2aeb50 = ADD v2aeb4f, v2aeb4d(0x3f)
    0xb510x2ae: v2aeb51 = AND v2aeb50, v2aeb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x2ae: v2aeb53 = ADD v2aeb47, v2aeb51
    0xb540x2ae: v2aeb54(0x40) = CONST 
    0xb560x2ae: MSTORE v2aeb54(0x40), v2aeb53
    0xb570x2ae: v2aeb57 = RETURNDATASIZE 
    0xb590x2ae: MSTORE v2aeb47, v2aeb57
    0xb5a0x2ae: v2aeb5a = RETURNDATASIZE 
    0xb5b0x2ae: v2aeb5b(0x0) = CONST 
    0xb5d0x2ae: v2aeb5d(0x20) = CONST 
    0xb600x2ae: v2aeb60 = ADD v2aeb47, v2aeb5d(0x20)
    0xb610x2ae: RETURNDATACOPY v2aeb60, v2aeb5b(0x0), v2aeb5a
    0xb620x2ae: v2aeb62(0xb6b) = CONST 
    0xb650x2ae: JUMP v2aeb62(0xb6b)

    Begin block 0xb6b0x2ae
    prev=[0xb450x2ae, 0xb660x2ae], succ=[0xb7f0x2ae, 0x153c0x2ae]
    =================================
    0xb700x2ae: v2aeb70(0x40) = CONST 
    0xb720x2ae: v2aeb72 = MLOAD v2aeb70(0x40)
    0xb730x2ae: v2aeb73 = RETURNDATASIZE 
    0xb740x2ae: v2aeb74(0x0) = CONST 
    0xb770x2ae: RETURNDATACOPY v2aeb72, v2aeb74(0x0), v2aeb73
    0xb7a0x2ae: v2aeb7a = ISZERO v2aeb37
    0xb7b0x2ae: v2aeb7b(0x153c) = CONST 
    0xb7e0x2ae: JUMPI v2aeb7b(0x153c), v2aeb7a

    Begin block 0xb7f0x2ae
    prev=[0xb6b0x2ae], succ=[]
    =================================
    0xb7f0x2ae: v2aeb7f = RETURNDATASIZE 
    0xb810x2ae: RETURN v2aeb72, v2aeb7f

    Begin block 0x153c0x2ae
    prev=[0xb6b0x2ae], succ=[]
    =================================
    0x153d0x2ae: v2ae153d = RETURNDATASIZE 
    0x153f0x2ae: REVERT v2aeb72, v2ae153d

    Begin block 0xb660x2ae
    prev=[0xafe0x2ae], succ=[0xb6b0x2ae]
    =================================
    0xb670x2ae: v2aeb67(0x60) = CONST 

}

function name()() public {
    Begin block 0x2f6
    prev=[], succ=[0x2fe, 0x302]
    =================================
    0x2f7: v2f7 = CALLVALUE 
    0x2f9: v2f9 = ISZERO v2f7
    0x2fa: v2fa(0x302) = CONST 
    0x2fd: JUMPI v2fa(0x302), v2f9

    Begin block 0x2fe
    prev=[0x2f6], succ=[]
    =================================
    0x2fe: v2fe(0x0) = CONST 
    0x301: REVERT v2fe(0x0), v2fe(0x0)

    Begin block 0x302
    prev=[0x2f6], succ=[0x30b0x2f6]
    =================================
    0x304: v304(0x30b) = CONST 
    0x307: v307(0xb86) = CONST 
    0x30a: v30a_0, v30a_1 = CALLPRIVATE v307(0xb86), v304(0x30b)

    Begin block 0x30b0x2f6
    prev=[0x302], succ=[0x32d0x2f6]
    =================================
    0x30c0x2f6: v2f630c(0x40) = CONST 
    0x30f0x2f6: v2f630f = MLOAD v2f630c(0x40)
    0x3100x2f6: v2f6310(0x20) = CONST 
    0x3140x2f6: MSTORE v2f630f, v2f6310(0x20)
    0x3160x2f6: v2f6316 = MLOAD v30a_0
    0x3190x2f6: v2f6319 = ADD v2f630f, v2f6310(0x20)
    0x31a0x2f6: MSTORE v2f6319, v2f6316
    0x31c0x2f6: v2f631c = MLOAD v30a_0
    0x3230x2f6: v2f6323 = ADD v2f630f, v2f630c(0x40)
    0x3260x2f6: v2f6326 = ADD v30a_0, v2f6310(0x20)
    0x32b0x2f6: v2f632b(0x0) = CONST 

    Begin block 0x32d0x2f6
    prev=[0x3360x2f6, 0x30b0x2f6], succ=[0x3450x2f6, 0x3360x2f6]
    =================================
    0x32d0x2f6_0x0: v32d2f6_0 = PHI v2f6340, v2f632b(0x0)
    0x3300x2f6: v2f6330 = LT v32d2f6_0, v2f631c
    0x3310x2f6: v2f6331 = ISZERO v2f6330
    0x3320x2f6: v2f6332(0x345) = CONST 
    0x3350x2f6: JUMPI v2f6332(0x345), v2f6331

    Begin block 0x3450x2f6
    prev=[0x32d0x2f6], succ=[0x3720x2f6, 0x3590x2f6]
    =================================
    0x34e0x2f6: v2f634e = ADD v2f631c, v2f6323
    0x3500x2f6: v2f6350(0x1f) = CONST 
    0x3520x2f6: v2f6352 = AND v2f6350(0x1f), v2f631c
    0x3540x2f6: v2f6354 = ISZERO v2f6352
    0x3550x2f6: v2f6355(0x372) = CONST 
    0x3580x2f6: JUMPI v2f6355(0x372), v2f6354

    Begin block 0x3720x2f6
    prev=[0x3450x2f6, 0x3590x2f6], succ=[]
    =================================
    0x3720x2f6_0x1: v3722f6_1 = PHI v2f636f, v2f634e
    0x3780x2f6: v2f6378(0x40) = CONST 
    0x37a0x2f6: v2f637a = MLOAD v2f6378(0x40)
    0x37d0x2f6: v2f637d = SUB v3722f6_1, v2f637a
    0x37f0x2f6: RETURN v2f637a, v2f637d

    Begin block 0x3590x2f6
    prev=[0x3450x2f6], succ=[0x3720x2f6]
    =================================
    0x35b0x2f6: v2f635b = SUB v2f634e, v2f6352
    0x35d0x2f6: v2f635d = MLOAD v2f635b
    0x35e0x2f6: v2f635e(0x1) = CONST 
    0x3610x2f6: v2f6361(0x20) = CONST 
    0x3630x2f6: v2f6363 = SUB v2f6361(0x20), v2f6352
    0x3640x2f6: v2f6364(0x100) = CONST 
    0x3670x2f6: v2f6367 = EXP v2f6364(0x100), v2f6363
    0x3680x2f6: v2f6368 = SUB v2f6367, v2f635e(0x1)
    0x3690x2f6: v2f6369 = NOT v2f6368
    0x36a0x2f6: v2f636a = AND v2f6369, v2f635d
    0x36c0x2f6: MSTORE v2f635b, v2f636a
    0x36d0x2f6: v2f636d(0x20) = CONST 
    0x36f0x2f6: v2f636f = ADD v2f636d(0x20), v2f635b

    Begin block 0x3360x2f6
    prev=[0x32d0x2f6], succ=[0x32d0x2f6]
    =================================
    0x3360x2f6_0x0: v3362f6_0 = PHI v2f6340, v2f632b(0x0)
    0x3380x2f6: v2f6338 = ADD v3362f6_0, v2f6326
    0x3390x2f6: v2f6339 = MLOAD v2f6338
    0x33c0x2f6: v2f633c = ADD v3362f6_0, v2f6323
    0x33d0x2f6: MSTORE v2f633c, v2f6339
    0x33e0x2f6: v2f633e(0x20) = CONST 
    0x3400x2f6: v2f6340 = ADD v2f633e(0x20), v3362f6_0
    0x3410x2f6: v2f6341(0x32d) = CONST 
    0x3440x2f6: JUMP v2f6341(0x32d)

}

function delegateToImplementation(bytes)() public {
    Begin block 0x380
    prev=[], succ=[0x388, 0x38c]
    =================================
    0x381: v381 = CALLVALUE 
    0x383: v383 = ISZERO v381
    0x384: v384(0x38c) = CONST 
    0x387: JUMPI v384(0x38c), v383

    Begin block 0x388
    prev=[0x380], succ=[]
    =================================
    0x388: v388(0x0) = CONST 
    0x38b: REVERT v388(0x0), v388(0x0)

    Begin block 0x38c
    prev=[0x380], succ=[0x39f, 0x3a3]
    =================================
    0x38e: v38e(0x30b) = CONST 
    0x391: v391(0x4) = CONST 
    0x394: v394 = CALLDATASIZE 
    0x395: v395 = SUB v394, v391(0x4)
    0x396: v396(0x20) = CONST 
    0x399: v399 = LT v395, v396(0x20)
    0x39a: v39a = ISZERO v399
    0x39b: v39b(0x3a3) = CONST 
    0x39e: JUMPI v39b(0x3a3), v39a

    Begin block 0x39f
    prev=[0x38c], succ=[]
    =================================
    0x39f: v39f(0x0) = CONST 
    0x3a2: REVERT v39f(0x0), v39f(0x0)

    Begin block 0x3a3
    prev=[0x38c], succ=[0x3b9, 0x3bd]
    =================================
    0x3a5: v3a5 = ADD v391(0x4), v395
    0x3a7: v3a7(0x20) = CONST 
    0x3aa: v3aa(0x24) = ADD v391(0x4), v3a7(0x20)
    0x3ac: v3ac = CALLDATALOAD v391(0x4)
    0x3ad: v3ad(0x1) = CONST 
    0x3af: v3af(0x20) = CONST 
    0x3b1: v3b1(0x100000000) = SHL v3af(0x20), v3ad(0x1)
    0x3b3: v3b3 = GT v3ac, v3b1(0x100000000)
    0x3b4: v3b4 = ISZERO v3b3
    0x3b5: v3b5(0x3bd) = CONST 
    0x3b8: JUMPI v3b5(0x3bd), v3b4

    Begin block 0x3b9
    prev=[0x3a3], succ=[]
    =================================
    0x3b9: v3b9(0x0) = CONST 
    0x3bc: REVERT v3b9(0x0), v3b9(0x0)

    Begin block 0x3bd
    prev=[0x3a3], succ=[0x3cb, 0x3cf]
    =================================
    0x3bf: v3bf = ADD v391(0x4), v3ac
    0x3c1: v3c1(0x20) = CONST 
    0x3c4: v3c4 = ADD v3bf, v3c1(0x20)
    0x3c5: v3c5 = GT v3c4, v3a5
    0x3c6: v3c6 = ISZERO v3c5
    0x3c7: v3c7(0x3cf) = CONST 
    0x3ca: JUMPI v3c7(0x3cf), v3c6

    Begin block 0x3cb
    prev=[0x3bd], succ=[]
    =================================
    0x3cb: v3cb(0x0) = CONST 
    0x3ce: REVERT v3cb(0x0), v3cb(0x0)

    Begin block 0x3cf
    prev=[0x3bd], succ=[0x3ec, 0x3f0]
    =================================
    0x3d1: v3d1 = CALLDATALOAD v3bf
    0x3d3: v3d3(0x20) = CONST 
    0x3d5: v3d5 = ADD v3d3(0x20), v3bf
    0x3d8: v3d8(0x1) = CONST 
    0x3db: v3db = MUL v3d1, v3d8(0x1)
    0x3dd: v3dd = ADD v3d5, v3db
    0x3de: v3de = GT v3dd, v3a5
    0x3df: v3df(0x1) = CONST 
    0x3e1: v3e1(0x20) = CONST 
    0x3e3: v3e3(0x100000000) = SHL v3e1(0x20), v3df(0x1)
    0x3e5: v3e5 = GT v3d1, v3e3(0x100000000)
    0x3e6: v3e6 = OR v3e5, v3de
    0x3e7: v3e7 = ISZERO v3e6
    0x3e8: v3e8(0x3f0) = CONST 
    0x3eb: JUMPI v3e8(0x3f0), v3e7

    Begin block 0x3ec
    prev=[0x3cf], succ=[]
    =================================
    0x3ec: v3ec(0x0) = CONST 
    0x3ef: REVERT v3ec(0x0), v3ec(0x0)

    Begin block 0x3f0
    prev=[0x3cf], succ=[0xc130x380]
    =================================
    0x3f5: v3f5(0x1f) = CONST 
    0x3f7: v3f7 = ADD v3f5(0x1f), v3d1
    0x3f8: v3f8(0x20) = CONST 
    0x3fc: v3fc = DIV v3f7, v3f8(0x20)
    0x3fd: v3fd = MUL v3fc, v3f8(0x20)
    0x3fe: v3fe(0x20) = CONST 
    0x400: v400 = ADD v3fe(0x20), v3fd
    0x401: v401(0x40) = CONST 
    0x403: v403 = MLOAD v401(0x40)
    0x406: v406 = ADD v403, v400
    0x407: v407(0x40) = CONST 
    0x409: MSTORE v407(0x40), v406
    0x411: MSTORE v403, v3d1
    0x412: v412(0x20) = CONST 
    0x414: v414 = ADD v412(0x20), v403
    0x41a: CALLDATACOPY v414, v3d5, v3d1
    0x41b: v41b(0x0) = CONST 
    0x41e: v41e = ADD v414, v3d1
    0x422: MSTORE v41e, v41b(0x0)
    0x427: v427(0xc13) = CONST 
    0x430: JUMP v427(0xc13)

    Begin block 0xc130x380
    prev=[0x3f0], succ=[0xc2c0x380]
    =================================
    0xc140x380: v380c14(0x12) = CONST 
    0xc160x380: v380c16 = SLOAD v380c14(0x12)
    0xc170x380: v380c17(0x60) = CONST 
    0xc1a0x380: v380c1a(0xc2c) = CONST 
    0xc1e0x380: v380c1e(0x1) = CONST 
    0xc200x380: v380c20(0x1) = CONST 
    0xc220x380: v380c22(0xa0) = CONST 
    0xc240x380: v380c24(0x10000000000000000000000000000000000000000) = SHL v380c22(0xa0), v380c20(0x1)
    0xc250x380: v380c25(0xffffffffffffffffffffffffffffffffffffffff) = SUB v380c24(0x10000000000000000000000000000000000000000), v380c1e(0x1)
    0xc260x380: v380c26 = AND v380c25(0xffffffffffffffffffffffffffffffffffffffff), v380c16
    0xc280x380: v380c28(0x121c) = CONST 
    0xc2b0x380: v380c2b_0 = CALLPRIVATE v380c28(0x121c), v403, v380c26, v380c1a(0xc2c)

    Begin block 0xc2c0x380
    prev=[0xc130x380], succ=[0x30b0x380]
    =================================
    0xc310x380: JUMP v38e(0x30b)

    Begin block 0x30b0x380
    prev=[0xc2c0x380], succ=[0x32d0x380]
    =================================
    0x30c0x380: v38030c(0x40) = CONST 
    0x30f0x380: v38030f = MLOAD v38030c(0x40)
    0x3100x380: v380310(0x20) = CONST 
    0x3140x380: MSTORE v38030f, v380310(0x20)
    0x3160x380: v380316 = MLOAD v380c2b_0
    0x3190x380: v380319 = ADD v38030f, v380310(0x20)
    0x31a0x380: MSTORE v380319, v380316
    0x31c0x380: v38031c = MLOAD v380c2b_0
    0x3230x380: v380323 = ADD v38030f, v38030c(0x40)
    0x3260x380: v380326 = ADD v380c2b_0, v380310(0x20)
    0x32b0x380: v38032b(0x0) = CONST 

    Begin block 0x32d0x380
    prev=[0x3360x380, 0x30b0x380], succ=[0x3450x380, 0x3360x380]
    =================================
    0x32d0x380_0x0: v32d380_0 = PHI v380340, v38032b(0x0)
    0x3300x380: v380330 = LT v32d380_0, v38031c
    0x3310x380: v380331 = ISZERO v380330
    0x3320x380: v380332(0x345) = CONST 
    0x3350x380: JUMPI v380332(0x345), v380331

    Begin block 0x3450x380
    prev=[0x32d0x380], succ=[0x3720x380, 0x3590x380]
    =================================
    0x34e0x380: v38034e = ADD v38031c, v380323
    0x3500x380: v380350(0x1f) = CONST 
    0x3520x380: v380352 = AND v380350(0x1f), v38031c
    0x3540x380: v380354 = ISZERO v380352
    0x3550x380: v380355(0x372) = CONST 
    0x3580x380: JUMPI v380355(0x372), v380354

    Begin block 0x3720x380
    prev=[0x3450x380, 0x3590x380], succ=[]
    =================================
    0x3720x380_0x1: v372380_1 = PHI v38036f, v38034e
    0x3780x380: v380378(0x40) = CONST 
    0x37a0x380: v38037a = MLOAD v380378(0x40)
    0x37d0x380: v38037d = SUB v372380_1, v38037a
    0x37f0x380: RETURN v38037a, v38037d

    Begin block 0x3590x380
    prev=[0x3450x380], succ=[0x3720x380]
    =================================
    0x35b0x380: v38035b = SUB v38034e, v380352
    0x35d0x380: v38035d = MLOAD v38035b
    0x35e0x380: v38035e(0x1) = CONST 
    0x3610x380: v380361(0x20) = CONST 
    0x3630x380: v380363 = SUB v380361(0x20), v380352
    0x3640x380: v380364(0x100) = CONST 
    0x3670x380: v380367 = EXP v380364(0x100), v380363
    0x3680x380: v380368 = SUB v380367, v38035e(0x1)
    0x3690x380: v380369 = NOT v380368
    0x36a0x380: v38036a = AND v380369, v38035d
    0x36c0x380: MSTORE v38035b, v38036a
    0x36d0x380: v38036d(0x20) = CONST 
    0x36f0x380: v38036f = ADD v38036d(0x20), v38035b

    Begin block 0x3360x380
    prev=[0x32d0x380], succ=[0x32d0x380]
    =================================
    0x3360x380_0x0: v336380_0 = PHI v380340, v38032b(0x0)
    0x3380x380: v380338 = ADD v336380_0, v380326
    0x3390x380: v380339 = MLOAD v380338
    0x33c0x380: v38033c = ADD v336380_0, v380323
    0x33d0x380: MSTORE v38033c, v380339
    0x33e0x380: v38033e(0x20) = CONST 
    0x3400x380: v380340 = ADD v38033e(0x20), v336380_0
    0x3410x380: v380341(0x32d) = CONST 
    0x3440x380: JUMP v380341(0x32d)

}

function transfer(address,uint256)() public {
    Begin block 0x431
    prev=[], succ=[0x439, 0x43d]
    =================================
    0x432: v432 = CALLVALUE 
    0x434: v434 = ISZERO v432
    0x435: v435(0x43d) = CONST 
    0x438: JUMPI v435(0x43d), v434

    Begin block 0x439
    prev=[0x431], succ=[]
    =================================
    0x439: v439(0x0) = CONST 
    0x43c: REVERT v439(0x0), v439(0x0)

    Begin block 0x43d
    prev=[0x431], succ=[0x450, 0x454]
    =================================
    0x43f: v43f(0x1582) = CONST 
    0x442: v442(0x4) = CONST 
    0x445: v445 = CALLDATASIZE 
    0x446: v446 = SUB v445, v442(0x4)
    0x447: v447(0x40) = CONST 
    0x44a: v44a = LT v446, v447(0x40)
    0x44b: v44b = ISZERO v44a
    0x44c: v44c(0x454) = CONST 
    0x44f: JUMPI v44c(0x454), v44b

    Begin block 0x450
    prev=[0x43d], succ=[]
    =================================
    0x450: v450(0x0) = CONST 
    0x453: REVERT v450(0x0), v450(0x0)

    Begin block 0x454
    prev=[0x43d], succ=[0xc32]
    =================================
    0x456: v456(0x1) = CONST 
    0x458: v458(0x1) = CONST 
    0x45a: v45a(0xa0) = CONST 
    0x45c: v45c(0x10000000000000000000000000000000000000000) = SHL v45a(0xa0), v458(0x1)
    0x45d: v45d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45c(0x10000000000000000000000000000000000000000), v456(0x1)
    0x45f: v45f = CALLDATALOAD v442(0x4)
    0x460: v460 = AND v45f, v45d(0xffffffffffffffffffffffffffffffffffffffff)
    0x462: v462(0x20) = CONST 
    0x464: v464(0x24) = ADD v462(0x20), v442(0x4)
    0x465: v465 = CALLDATALOAD v464(0x24)
    0x466: v466(0xc32) = CONST 
    0x469: JUMP v466(0xc32)

    Begin block 0xc32
    prev=[0x454], succ=[0xafe0x431]
    =================================
    0xc33: vc33(0x0) = CONST 
    0xc35: vc35(0x1b88) = CONST 
    0xc38: vc38(0xafe) = CONST 
    0xc3b: JUMP vc38(0xafe)

    Begin block 0xafe0x431
    prev=[0xc32], succ=[0xb450x431, 0xb660x431]
    =================================
    0xaff0x431: v431aff(0x12) = CONST 
    0xb010x431: v431b01 = SLOAD v431aff(0x12)
    0xb020x431: v431b02(0x40) = CONST 
    0xb040x431: v431b04 = MLOAD v431b02(0x40)
    0xb050x431: v431b05(0x60) = CONST 
    0xb080x431: v431b08(0x0) = CONST 
    0xb0b0x431: v431b0b(0x1) = CONST 
    0xb0d0x431: v431b0d(0x1) = CONST 
    0xb0f0x431: v431b0f(0xa0) = CONST 
    0xb110x431: v431b11(0x10000000000000000000000000000000000000000) = SHL v431b0f(0xa0), v431b0d(0x1)
    0xb120x431: v431b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v431b11(0x10000000000000000000000000000000000000000), v431b0b(0x1)
    0xb150x431: v431b15 = AND v431b01, v431b12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x431: v431b19 = CALLDATASIZE 
    0xb210x431: CALLDATACOPY v431b04, v431b08(0x0), v431b19
    0xb220x431: v431b22(0x40) = CONST 
    0xb240x431: v431b24 = MLOAD v431b22(0x40)
    0xb260x431: v431b26 = ADD v431b04, v431b19
    0xb290x431: v431b29(0x0) = CONST 
    0xb330x431: v431b33 = SUB v431b26, v431b24
    0xb360x431: v431b36 = GAS 
    0xb370x431: v431b37 = DELEGATECALL v431b36, v431b15, v431b24, v431b33, v431b24, v431b29(0x0)
    0xb3b0x431: v431b3b = RETURNDATASIZE 
    0xb3d0x431: v431b3d(0x0) = CONST 
    0xb400x431: v431b40 = EQ v431b3b, v431b3d(0x0)
    0xb410x431: v431b41(0xb66) = CONST 
    0xb440x431: JUMPI v431b41(0xb66), v431b40

    Begin block 0xb450x431
    prev=[0xafe0x431], succ=[0xb6b0x431]
    =================================
    0xb450x431: v431b45(0x40) = CONST 
    0xb470x431: v431b47 = MLOAD v431b45(0x40)
    0xb4a0x431: v431b4a(0x1f) = CONST 
    0xb4c0x431: v431b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v431b4a(0x1f)
    0xb4d0x431: v431b4d(0x3f) = CONST 
    0xb4f0x431: v431b4f = RETURNDATASIZE 
    0xb500x431: v431b50 = ADD v431b4f, v431b4d(0x3f)
    0xb510x431: v431b51 = AND v431b50, v431b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x431: v431b53 = ADD v431b47, v431b51
    0xb540x431: v431b54(0x40) = CONST 
    0xb560x431: MSTORE v431b54(0x40), v431b53
    0xb570x431: v431b57 = RETURNDATASIZE 
    0xb590x431: MSTORE v431b47, v431b57
    0xb5a0x431: v431b5a = RETURNDATASIZE 
    0xb5b0x431: v431b5b(0x0) = CONST 
    0xb5d0x431: v431b5d(0x20) = CONST 
    0xb600x431: v431b60 = ADD v431b47, v431b5d(0x20)
    0xb610x431: RETURNDATACOPY v431b60, v431b5b(0x0), v431b5a
    0xb620x431: v431b62(0xb6b) = CONST 
    0xb650x431: JUMP v431b62(0xb6b)

    Begin block 0xb6b0x431
    prev=[0xb450x431, 0xb660x431], succ=[0xb7f0x431, 0x153c0x431]
    =================================
    0xb700x431: v431b70(0x40) = CONST 
    0xb720x431: v431b72 = MLOAD v431b70(0x40)
    0xb730x431: v431b73 = RETURNDATASIZE 
    0xb740x431: v431b74(0x0) = CONST 
    0xb770x431: RETURNDATACOPY v431b72, v431b74(0x0), v431b73
    0xb7a0x431: v431b7a = ISZERO v431b37
    0xb7b0x431: v431b7b(0x153c) = CONST 
    0xb7e0x431: JUMPI v431b7b(0x153c), v431b7a

    Begin block 0xb7f0x431
    prev=[0xb6b0x431], succ=[]
    =================================
    0xb7f0x431: v431b7f = RETURNDATASIZE 
    0xb810x431: RETURN v431b72, v431b7f

    Begin block 0x153c0x431
    prev=[0xb6b0x431], succ=[]
    =================================
    0x153d0x431: v431153d = RETURNDATASIZE 
    0x153f0x431: REVERT v431b72, v431153d

    Begin block 0xb660x431
    prev=[0xafe0x431], succ=[0xb6b0x431]
    =================================
    0xb670x431: v431b67(0x60) = CONST 

}

function maxScalingFactor()() public {
    Begin block 0x47e
    prev=[], succ=[0x486, 0x48a]
    =================================
    0x47f: v47f = CALLVALUE 
    0x481: v481 = ISZERO v47f
    0x482: v482(0x48a) = CONST 
    0x485: JUMPI v482(0x48a), v481

    Begin block 0x486
    prev=[0x47e], succ=[]
    =================================
    0x486: v486(0x0) = CONST 
    0x489: REVERT v486(0x0), v486(0x0)

    Begin block 0x48a
    prev=[0x47e], succ=[0xc43]
    =================================
    0x48c: v48c(0x15b5) = CONST 
    0x48f: v48f(0xc43) = CONST 
    0x492: JUMP v48f(0xc43)

    Begin block 0xc43
    prev=[0x48a], succ=[0x12de0x47e]
    =================================
    0xc44: vc44(0x0) = CONST 
    0xc46: vc46(0xc4d) = CONST 
    0xc49: vc49(0x12de) = CONST 
    0xc4c: JUMP vc49(0x12de)

    Begin block 0x12de0x47e
    prev=[0xc43], succ=[0x13600x47e]
    =================================
    0x12df0x47e: v47e12df(0x60) = CONST 
    0x12e10x47e: v47e12e1(0x0) = CONST 
    0x12e30x47e: v47e12e3 = ADDRESS 
    0x12e40x47e: v47e12e4(0x1) = CONST 
    0x12e60x47e: v47e12e6(0x1) = CONST 
    0x12e80x47e: v47e12e8(0xa0) = CONST 
    0x12ea0x47e: v47e12ea(0x10000000000000000000000000000000000000000) = SHL v47e12e8(0xa0), v47e12e6(0x1)
    0x12eb0x47e: v47e12eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v47e12ea(0x10000000000000000000000000000000000000000), v47e12e4(0x1)
    0x12ec0x47e: v47e12ec = AND v47e12eb(0xffffffffffffffffffffffffffffffffffffffff), v47e12e3
    0x12ed0x47e: v47e12ed(0x0) = CONST 
    0x12ef0x47e: v47e12ef = CALLDATASIZE 
    0x12f00x47e: v47e12f0(0x40) = CONST 
    0x12f20x47e: v47e12f2 = MLOAD v47e12f0(0x40)
    0x12f30x47e: v47e12f3(0x24) = CONST 
    0x12f50x47e: v47e12f5 = ADD v47e12f3(0x24), v47e12f2
    0x12f80x47e: v47e12f8(0x20) = CONST 
    0x12fa0x47e: v47e12fa = ADD v47e12f8(0x20), v47e12f5
    0x12fd0x47e: v47e12fd(0x20) = SUB v47e12fa, v47e12f5
    0x12ff0x47e: MSTORE v47e12f5, v47e12fd(0x20)
    0x13050x47e: MSTORE v47e12fa, v47e12ef
    0x13060x47e: v47e1306(0x20) = CONST 
    0x13080x47e: v47e1308 = ADD v47e1306(0x20), v47e12fa
    0x130e0x47e: CALLDATACOPY v47e1308, v47e12ed(0x0), v47e12ef
    0x130f0x47e: v47e130f(0x0) = CONST 
    0x13130x47e: v47e1313 = ADD v47e12ef, v47e1308
    0x13140x47e: MSTORE v47e1313, v47e130f(0x0)
    0x13150x47e: v47e1315(0x40) = CONST 
    0x13180x47e: v47e1318 = MLOAD v47e1315(0x40)
    0x13190x47e: v47e1319(0x1f) = CONST 
    0x131d0x47e: v47e131d = ADD v47e12ef, v47e1319(0x1f)
    0x131e0x47e: v47e131e(0x1f) = CONST 
    0x13200x47e: v47e1320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v47e131e(0x1f)
    0x13230x47e: v47e1323 = AND v47e1320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v47e131d
    0x13260x47e: v47e1326 = ADD v47e1308, v47e1323
    0x13290x47e: v47e1329 = SUB v47e1326, v47e1318
    0x132c0x47e: v47e132c = ADD v47e1320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v47e1329
    0x132e0x47e: MSTORE v47e1318, v47e132c
    0x13310x47e: MSTORE v47e1315(0x40), v47e1326
    0x13320x47e: v47e1332(0x20) = CONST 
    0x13350x47e: v47e1335 = ADD v47e1318, v47e1332(0x20)
    0x13370x47e: v47e1337 = MLOAD v47e1335
    0x13380x47e: v47e1338(0x1) = CONST 
    0x133a0x47e: v47e133a(0x1) = CONST 
    0x133c0x47e: v47e133c(0xe0) = CONST 
    0x133e0x47e: v47e133e(0x100000000000000000000000000000000000000000000000000000000) = SHL v47e133c(0xe0), v47e133a(0x1)
    0x133f0x47e: v47e133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v47e133e(0x100000000000000000000000000000000000000000000000000000000), v47e1338(0x1)
    0x13400x47e: v47e1340 = AND v47e133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v47e1337
    0x13410x47e: v47e1341(0x933c1ed) = CONST 
    0x13460x47e: v47e1346(0xe0) = CONST 
    0x13480x47e: v47e1348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v47e1346(0xe0), v47e1341(0x933c1ed)
    0x13490x47e: v47e1349 = OR v47e1348(0x933c1ed00000000000000000000000000000000000000000000000000000000), v47e1340
    0x134b0x47e: MSTORE v47e1335, v47e1349
    0x134d0x47e: v47e134d = MLOAD v47e1315(0x40)
    0x134f0x47e: v47e134f = MLOAD v47e1318

    Begin block 0x13600x47e
    prev=[0x13690x47e, 0x12de0x47e], succ=[0x137f0x47e, 0x13690x47e]
    =================================
    0x13600x47e_0x2: v136047e_2 = PHI v47e1372, v47e134f
    0x13610x47e: v47e1361(0x20) = CONST 
    0x13640x47e: v47e1364 = LT v136047e_2, v47e1361(0x20)
    0x13650x47e: v47e1365(0x137f) = CONST 
    0x13680x47e: JUMPI v47e1365(0x137f), v47e1364

    Begin block 0x137f0x47e
    prev=[0x13600x47e], succ=[0x13be0x47e, 0x13df0x47e]
    =================================
    0x137f0x47e_0x0: v137f47e_0 = PHI v47e137a, v47e1335
    0x137f0x47e_0x1: v137f47e_1 = PHI v47e1378, v47e134d
    0x137f0x47e_0x2: v137f47e_2 = PHI v47e1372, v47e134f
    0x13800x47e: v47e1380(0x1) = CONST 
    0x13830x47e: v47e1383(0x20) = CONST 
    0x13850x47e: v47e1385 = SUB v47e1383(0x20), v137f47e_2
    0x13860x47e: v47e1386(0x100) = CONST 
    0x13890x47e: v47e1389 = EXP v47e1386(0x100), v47e1385
    0x138a0x47e: v47e138a = SUB v47e1389, v47e1380(0x1)
    0x138c0x47e: v47e138c = NOT v47e138a
    0x138e0x47e: v47e138e = MLOAD v137f47e_0
    0x138f0x47e: v47e138f = AND v47e138e, v47e138c
    0x13920x47e: v47e1392 = MLOAD v137f47e_1
    0x13930x47e: v47e1393 = AND v47e1392, v47e138a
    0x13960x47e: v47e1396 = OR v47e138f, v47e1393
    0x13980x47e: MSTORE v137f47e_1, v47e1396
    0x13a10x47e: v47e13a1 = ADD v47e134f, v47e134d
    0x13a50x47e: v47e13a5(0x0) = CONST 
    0x13a70x47e: v47e13a7(0x40) = CONST 
    0x13a90x47e: v47e13a9 = MLOAD v47e13a7(0x40)
    0x13ac0x47e: v47e13ac = SUB v47e13a1, v47e13a9
    0x13af0x47e: v47e13af = GAS 
    0x13b00x47e: v47e13b0 = STATICCALL v47e13af, v47e12ec, v47e13a9, v47e13ac, v47e13a9, v47e13a5(0x0)
    0x13b40x47e: v47e13b4 = RETURNDATASIZE 
    0x13b60x47e: v47e13b6(0x0) = CONST 
    0x13b90x47e: v47e13b9 = EQ v47e13b4, v47e13b6(0x0)
    0x13ba0x47e: v47e13ba(0x13df) = CONST 
    0x13bd0x47e: JUMPI v47e13ba(0x13df), v47e13b9

    Begin block 0x13be0x47e
    prev=[0x137f0x47e], succ=[0x13e40x47e]
    =================================
    0x13be0x47e: v47e13be(0x40) = CONST 
    0x13c00x47e: v47e13c0 = MLOAD v47e13be(0x40)
    0x13c30x47e: v47e13c3(0x1f) = CONST 
    0x13c50x47e: v47e13c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v47e13c3(0x1f)
    0x13c60x47e: v47e13c6(0x3f) = CONST 
    0x13c80x47e: v47e13c8 = RETURNDATASIZE 
    0x13c90x47e: v47e13c9 = ADD v47e13c8, v47e13c6(0x3f)
    0x13ca0x47e: v47e13ca = AND v47e13c9, v47e13c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0x47e: v47e13cc = ADD v47e13c0, v47e13ca
    0x13cd0x47e: v47e13cd(0x40) = CONST 
    0x13cf0x47e: MSTORE v47e13cd(0x40), v47e13cc
    0x13d00x47e: v47e13d0 = RETURNDATASIZE 
    0x13d20x47e: MSTORE v47e13c0, v47e13d0
    0x13d30x47e: v47e13d3 = RETURNDATASIZE 
    0x13d40x47e: v47e13d4(0x0) = CONST 
    0x13d60x47e: v47e13d6(0x20) = CONST 
    0x13d90x47e: v47e13d9 = ADD v47e13c0, v47e13d6(0x20)
    0x13da0x47e: RETURNDATACOPY v47e13d9, v47e13d4(0x0), v47e13d3
    0x13db0x47e: v47e13db(0x13e4) = CONST 
    0x13de0x47e: JUMP v47e13db(0x13e4)

    Begin block 0x13e40x47e
    prev=[0x13be0x47e, 0x13df0x47e], succ=[0x13f80x47e, 0x155f0x47e]
    =================================
    0x13e90x47e: v47e13e9(0x40) = CONST 
    0x13eb0x47e: v47e13eb = MLOAD v47e13e9(0x40)
    0x13ec0x47e: v47e13ec = RETURNDATASIZE 
    0x13ed0x47e: v47e13ed(0x0) = CONST 
    0x13f00x47e: RETURNDATACOPY v47e13eb, v47e13ed(0x0), v47e13ec
    0x13f30x47e: v47e13f3 = ISZERO v47e13b0
    0x13f40x47e: v47e13f4(0x155f) = CONST 
    0x13f70x47e: JUMPI v47e13f4(0x155f), v47e13f3

    Begin block 0x13f80x47e
    prev=[0x13e40x47e], succ=[]
    =================================
    0x13f80x47e: v47e13f8(0x40) = CONST 
    0x13fa0x47e: v47e13fa = RETURNDATASIZE 
    0x13fb0x47e: v47e13fb = SUB v47e13fa, v47e13f8(0x40)
    0x13fc0x47e: v47e13fc(0x40) = CONST 
    0x13ff0x47e: v47e13ff = ADD v47e13eb, v47e13fc(0x40)
    0x14000x47e: RETURN v47e13ff, v47e13fb

    Begin block 0x155f0x47e
    prev=[0x13e40x47e], succ=[]
    =================================
    0x15600x47e: v47e1560 = RETURNDATASIZE 
    0x15620x47e: REVERT v47e13eb, v47e1560

    Begin block 0x13df0x47e
    prev=[0x137f0x47e], succ=[0x13e40x47e]
    =================================
    0x13e00x47e: v47e13e0(0x60) = CONST 

    Begin block 0x13690x47e
    prev=[0x13600x47e], succ=[0x13600x47e]
    =================================
    0x13690x47e_0x0: v136947e_0 = PHI v47e137a, v47e1335
    0x13690x47e_0x1: v136947e_1 = PHI v47e1378, v47e134d
    0x13690x47e_0x2: v136947e_2 = PHI v47e1372, v47e134f
    0x136a0x47e: v47e136a = MLOAD v136947e_0
    0x136c0x47e: MSTORE v136947e_1, v47e136a
    0x136d0x47e: v47e136d(0x1f) = CONST 
    0x136f0x47e: v47e136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v47e136d(0x1f)
    0x13720x47e: v47e1372 = ADD v136947e_2, v47e136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740x47e: v47e1374(0x20) = CONST 
    0x13780x47e: v47e1378 = ADD v47e1374(0x20), v136947e_1
    0x137a0x47e: v47e137a = ADD v47e1374(0x20), v136947e_0
    0x137b0x47e: v47e137b(0x1360) = CONST 
    0x137e0x47e: JUMP v47e137b(0x1360)

}

function rebaser()() public {
    Begin block 0x4a5
    prev=[], succ=[0x4ad, 0x4b1]
    =================================
    0x4a6: v4a6 = CALLVALUE 
    0x4a8: v4a8 = ISZERO v4a6
    0x4a9: v4a9(0x4b1) = CONST 
    0x4ac: JUMPI v4a9(0x4b1), v4a8

    Begin block 0x4ad
    prev=[0x4a5], succ=[]
    =================================
    0x4ad: v4ad(0x0) = CONST 
    0x4b0: REVERT v4ad(0x0), v4ad(0x0)

    Begin block 0x4b1
    prev=[0x4a5], succ=[0xc51]
    =================================
    0x4b3: v4b3(0x15e6) = CONST 
    0x4b6: v4b6(0xc51) = CONST 
    0x4b9: JUMP v4b6(0xc51)

    Begin block 0xc51
    prev=[0x4b1], succ=[0x15e6]
    =================================
    0xc52: vc52(0x5) = CONST 
    0xc54: vc54 = SLOAD vc52(0x5)
    0xc55: vc55(0x1) = CONST 
    0xc57: vc57(0x1) = CONST 
    0xc59: vc59(0xa0) = CONST 
    0xc5b: vc5b(0x10000000000000000000000000000000000000000) = SHL vc59(0xa0), vc57(0x1)
    0xc5c: vc5c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc5b(0x10000000000000000000000000000000000000000), vc55(0x1)
    0xc5d: vc5d = AND vc5c(0xffffffffffffffffffffffffffffffffffffffff), vc54
    0xc5f: JUMP v4b3(0x15e6)

    Begin block 0x15e6
    prev=[0xc51], succ=[]
    =================================
    0x15e7: v15e7(0x40) = CONST 
    0x15ea: v15ea = MLOAD v15e7(0x40)
    0x15eb: v15eb(0x1) = CONST 
    0x15ed: v15ed(0x1) = CONST 
    0x15ef: v15ef(0xa0) = CONST 
    0x15f1: v15f1(0x10000000000000000000000000000000000000000) = SHL v15ef(0xa0), v15ed(0x1)
    0x15f2: v15f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15f1(0x10000000000000000000000000000000000000000), v15eb(0x1)
    0x15f5: v15f5 = AND vc5d, v15f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x15f7: MSTORE v15ea, v15f5
    0x15f8: v15f8 = MLOAD v15e7(0x40)
    0x15fc: v15fc(0x0) = SUB v15ea, v15f8
    0x15fd: v15fd(0x20) = CONST 
    0x15ff: v15ff(0x20) = ADD v15fd(0x20), v15fc(0x0)
    0x1601: RETURN v15f8, v15ff(0x20)

}

function gov()() public {
    Begin block 0x4d6
    prev=[], succ=[0x4de, 0x4e2]
    =================================
    0x4d7: v4d7 = CALLVALUE 
    0x4d9: v4d9 = ISZERO v4d7
    0x4da: v4da(0x4e2) = CONST 
    0x4dd: JUMPI v4da(0x4e2), v4d9

    Begin block 0x4de
    prev=[0x4d6], succ=[]
    =================================
    0x4de: v4de(0x0) = CONST 
    0x4e1: REVERT v4de(0x0), v4de(0x0)

    Begin block 0x4e2
    prev=[0x4d6], succ=[0xc60]
    =================================
    0x4e4: v4e4(0x1621) = CONST 
    0x4e7: v4e7(0xc60) = CONST 
    0x4ea: JUMP v4e7(0xc60)

    Begin block 0xc60
    prev=[0x4e2], succ=[0x1621]
    =================================
    0xc61: vc61(0x3) = CONST 
    0xc63: vc63 = SLOAD vc61(0x3)
    0xc64: vc64(0x100) = CONST 
    0xc68: vc68 = DIV vc63, vc64(0x100)
    0xc69: vc69(0x1) = CONST 
    0xc6b: vc6b(0x1) = CONST 
    0xc6d: vc6d(0xa0) = CONST 
    0xc6f: vc6f(0x10000000000000000000000000000000000000000) = SHL vc6d(0xa0), vc6b(0x1)
    0xc70: vc70(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc6f(0x10000000000000000000000000000000000000000), vc69(0x1)
    0xc71: vc71 = AND vc70(0xffffffffffffffffffffffffffffffffffffffff), vc68
    0xc73: JUMP v4e4(0x1621)

    Begin block 0x1621
    prev=[0xc60], succ=[]
    =================================
    0x1622: v1622(0x40) = CONST 
    0x1625: v1625 = MLOAD v1622(0x40)
    0x1626: v1626(0x1) = CONST 
    0x1628: v1628(0x1) = CONST 
    0x162a: v162a(0xa0) = CONST 
    0x162c: v162c(0x10000000000000000000000000000000000000000) = SHL v162a(0xa0), v1628(0x1)
    0x162d: v162d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v162c(0x10000000000000000000000000000000000000000), v1626(0x1)
    0x1630: v1630 = AND vc71, v162d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1632: MSTORE v1625, v1630
    0x1633: v1633 = MLOAD v1622(0x40)
    0x1637: v1637(0x0) = SUB v1625, v1633
    0x1638: v1638(0x20) = CONST 
    0x163a: v163a(0x20) = ADD v1638(0x20), v1637(0x0)
    0x163c: RETURN v1633, v163a(0x20)

}

function totalSupply()() public {
    Begin block 0x4eb
    prev=[], succ=[0x4f3, 0x4f7]
    =================================
    0x4ec: v4ec = CALLVALUE 
    0x4ee: v4ee = ISZERO v4ec
    0x4ef: v4ef(0x4f7) = CONST 
    0x4f2: JUMPI v4ef(0x4f7), v4ee

    Begin block 0x4f3
    prev=[0x4eb], succ=[]
    =================================
    0x4f3: v4f3(0x0) = CONST 
    0x4f6: REVERT v4f3(0x0), v4f3(0x0)

    Begin block 0x4f7
    prev=[0x4eb], succ=[0xc74]
    =================================
    0x4f9: v4f9(0x165c) = CONST 
    0x4fc: v4fc(0xc74) = CONST 
    0x4ff: JUMP v4fc(0xc74)

    Begin block 0xc74
    prev=[0x4f7], succ=[0x165c]
    =================================
    0xc75: vc75(0x8) = CONST 
    0xc77: vc77 = SLOAD vc75(0x8)
    0xc79: JUMP v4f9(0x165c)

    Begin block 0x165c
    prev=[0xc74], succ=[]
    =================================
    0x165d: v165d(0x40) = CONST 
    0x1660: v1660 = MLOAD v165d(0x40)
    0x1663: MSTORE v1660, vc77
    0x1664: v1664 = MLOAD v165d(0x40)
    0x1668: v1668(0x0) = SUB v1660, v1664
    0x1669: v1669(0x20) = CONST 
    0x166b: v166b(0x20) = ADD v1669(0x20), v1668(0x0)
    0x166d: RETURN v1664, v166b(0x20)

}

function DOMAIN_TYPEHASH()() public {
    Begin block 0x500
    prev=[], succ=[0x508, 0x50c]
    =================================
    0x501: v501 = CALLVALUE 
    0x503: v503 = ISZERO v501
    0x504: v504(0x50c) = CONST 
    0x507: JUMPI v504(0x50c), v503

    Begin block 0x508
    prev=[0x500], succ=[]
    =================================
    0x508: v508(0x0) = CONST 
    0x50b: REVERT v508(0x0), v508(0x0)

    Begin block 0x50c
    prev=[0x500], succ=[0xc7a]
    =================================
    0x50e: v50e(0x168d) = CONST 
    0x511: v511(0xc7a) = CONST 
    0x514: JUMP v511(0xc7a)

    Begin block 0xc7a
    prev=[0x50c], succ=[0x168d]
    =================================
    0xc7b: vc7b(0x40) = CONST 
    0xc7d: vc7d = MLOAD vc7b(0x40)
    0xc7f: vc7f(0x43) = CONST 
    0xc81: vc81(0x1402) = CONST 
    0xc85: CODECOPY vc7d, vc81(0x1402), vc7f(0x43)
    0xc86: vc86(0x43) = CONST 
    0xc88: vc88 = ADD vc86(0x43), vc7d
    0xc8b: vc8b(0x40) = CONST 
    0xc8d: vc8d = MLOAD vc8b(0x40)
    0xc90: vc90(0x43) = SUB vc88, vc8d
    0xc92: vc92 = SHA3 vc8d, vc90(0x43)
    0xc94: JUMP v50e(0x168d)

    Begin block 0x168d
    prev=[0xc7a], succ=[]
    =================================
    0x168e: v168e(0x40) = CONST 
    0x1691: v1691 = MLOAD v168e(0x40)
    0x1694: MSTORE v1691, vc92
    0x1695: v1695 = MLOAD v168e(0x40)
    0x1699: v1699(0x0) = SUB v1691, v1695
    0x169a: v169a(0x20) = CONST 
    0x169c: v169c(0x20) = ADD v169a(0x20), v1699(0x0)
    0x169e: RETURN v1695, v169c(0x20)

}

function rescueTokens(address,address,uint256)() public {
    Begin block 0x515
    prev=[], succ=[0x51d, 0x521]
    =================================
    0x516: v516 = CALLVALUE 
    0x518: v518 = ISZERO v516
    0x519: v519(0x521) = CONST 
    0x51c: JUMPI v519(0x521), v518

    Begin block 0x51d
    prev=[0x515], succ=[]
    =================================
    0x51d: v51d(0x0) = CONST 
    0x520: REVERT v51d(0x0), v51d(0x0)

    Begin block 0x521
    prev=[0x515], succ=[0x534, 0x538]
    =================================
    0x523: v523(0x16be) = CONST 
    0x526: v526(0x4) = CONST 
    0x529: v529 = CALLDATASIZE 
    0x52a: v52a = SUB v529, v526(0x4)
    0x52b: v52b(0x60) = CONST 
    0x52e: v52e = LT v52a, v52b(0x60)
    0x52f: v52f = ISZERO v52e
    0x530: v530(0x538) = CONST 
    0x533: JUMPI v530(0x538), v52f

    Begin block 0x534
    prev=[0x521], succ=[]
    =================================
    0x534: v534(0x0) = CONST 
    0x537: REVERT v534(0x0), v534(0x0)

    Begin block 0x538
    prev=[0x521], succ=[0xc950x515]
    =================================
    0x53a: v53a(0x1) = CONST 
    0x53c: v53c(0x1) = CONST 
    0x53e: v53e(0xa0) = CONST 
    0x540: v540(0x10000000000000000000000000000000000000000) = SHL v53e(0xa0), v53c(0x1)
    0x541: v541(0xffffffffffffffffffffffffffffffffffffffff) = SUB v540(0x10000000000000000000000000000000000000000), v53a(0x1)
    0x543: v543 = CALLDATALOAD v526(0x4)
    0x545: v545 = AND v541(0xffffffffffffffffffffffffffffffffffffffff), v543
    0x547: v547(0x20) = CONST 
    0x54a: v54a(0x24) = ADD v526(0x4), v547(0x20)
    0x54b: v54b = CALLDATALOAD v54a(0x24)
    0x54e: v54e = AND v541(0xffffffffffffffffffffffffffffffffffffffff), v54b
    0x550: v550(0x40) = CONST 
    0x552: v552(0x44) = ADD v550(0x40), v526(0x4)
    0x553: v553 = CALLDATALOAD v552(0x44)
    0x554: v554(0xc95) = CONST 
    0x557: JUMP v554(0xc95)

    Begin block 0xc950x515
    prev=[0x538], succ=[0xafe0x515]
    =================================
    0xc960x515: v515c96(0x0) = CONST 
    0xc980x515: v515c98(0xc9f) = CONST 
    0xc9b0x515: v515c9b(0xafe) = CONST 
    0xc9e0x515: JUMP v515c9b(0xafe)

    Begin block 0xafe0x515
    prev=[0xc950x515], succ=[0xb450x515, 0xb660x515]
    =================================
    0xaff0x515: v515aff(0x12) = CONST 
    0xb010x515: v515b01 = SLOAD v515aff(0x12)
    0xb020x515: v515b02(0x40) = CONST 
    0xb040x515: v515b04 = MLOAD v515b02(0x40)
    0xb050x515: v515b05(0x60) = CONST 
    0xb080x515: v515b08(0x0) = CONST 
    0xb0b0x515: v515b0b(0x1) = CONST 
    0xb0d0x515: v515b0d(0x1) = CONST 
    0xb0f0x515: v515b0f(0xa0) = CONST 
    0xb110x515: v515b11(0x10000000000000000000000000000000000000000) = SHL v515b0f(0xa0), v515b0d(0x1)
    0xb120x515: v515b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v515b11(0x10000000000000000000000000000000000000000), v515b0b(0x1)
    0xb150x515: v515b15 = AND v515b01, v515b12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x515: v515b19 = CALLDATASIZE 
    0xb210x515: CALLDATACOPY v515b04, v515b08(0x0), v515b19
    0xb220x515: v515b22(0x40) = CONST 
    0xb240x515: v515b24 = MLOAD v515b22(0x40)
    0xb260x515: v515b26 = ADD v515b04, v515b19
    0xb290x515: v515b29(0x0) = CONST 
    0xb330x515: v515b33 = SUB v515b26, v515b24
    0xb360x515: v515b36 = GAS 
    0xb370x515: v515b37 = DELEGATECALL v515b36, v515b15, v515b24, v515b33, v515b24, v515b29(0x0)
    0xb3b0x515: v515b3b = RETURNDATASIZE 
    0xb3d0x515: v515b3d(0x0) = CONST 
    0xb400x515: v515b40 = EQ v515b3b, v515b3d(0x0)
    0xb410x515: v515b41(0xb66) = CONST 
    0xb440x515: JUMPI v515b41(0xb66), v515b40

    Begin block 0xb450x515
    prev=[0xafe0x515], succ=[0xb6b0x515]
    =================================
    0xb450x515: v515b45(0x40) = CONST 
    0xb470x515: v515b47 = MLOAD v515b45(0x40)
    0xb4a0x515: v515b4a(0x1f) = CONST 
    0xb4c0x515: v515b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v515b4a(0x1f)
    0xb4d0x515: v515b4d(0x3f) = CONST 
    0xb4f0x515: v515b4f = RETURNDATASIZE 
    0xb500x515: v515b50 = ADD v515b4f, v515b4d(0x3f)
    0xb510x515: v515b51 = AND v515b50, v515b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x515: v515b53 = ADD v515b47, v515b51
    0xb540x515: v515b54(0x40) = CONST 
    0xb560x515: MSTORE v515b54(0x40), v515b53
    0xb570x515: v515b57 = RETURNDATASIZE 
    0xb590x515: MSTORE v515b47, v515b57
    0xb5a0x515: v515b5a = RETURNDATASIZE 
    0xb5b0x515: v515b5b(0x0) = CONST 
    0xb5d0x515: v515b5d(0x20) = CONST 
    0xb600x515: v515b60 = ADD v515b47, v515b5d(0x20)
    0xb610x515: RETURNDATACOPY v515b60, v515b5b(0x0), v515b5a
    0xb620x515: v515b62(0xb6b) = CONST 
    0xb650x515: JUMP v515b62(0xb6b)

    Begin block 0xb6b0x515
    prev=[0xb450x515, 0xb660x515], succ=[0xb7f0x515, 0x153c0x515]
    =================================
    0xb700x515: v515b70(0x40) = CONST 
    0xb720x515: v515b72 = MLOAD v515b70(0x40)
    0xb730x515: v515b73 = RETURNDATASIZE 
    0xb740x515: v515b74(0x0) = CONST 
    0xb770x515: RETURNDATACOPY v515b72, v515b74(0x0), v515b73
    0xb7a0x515: v515b7a = ISZERO v515b37
    0xb7b0x515: v515b7b(0x153c) = CONST 
    0xb7e0x515: JUMPI v515b7b(0x153c), v515b7a

    Begin block 0xb7f0x515
    prev=[0xb6b0x515], succ=[]
    =================================
    0xb7f0x515: v515b7f = RETURNDATASIZE 
    0xb810x515: RETURN v515b72, v515b7f

    Begin block 0x153c0x515
    prev=[0xb6b0x515], succ=[]
    =================================
    0x153d0x515: v515153d = RETURNDATASIZE 
    0x153f0x515: REVERT v515b72, v515153d

    Begin block 0xb660x515
    prev=[0xafe0x515], succ=[0xb6b0x515]
    =================================
    0xb670x515: v515b67(0x60) = CONST 

}

function pendingGov()() public {
    Begin block 0x558
    prev=[], succ=[0x560, 0x564]
    =================================
    0x559: v559 = CALLVALUE 
    0x55b: v55b = ISZERO v559
    0x55c: v55c(0x564) = CONST 
    0x55f: JUMPI v55c(0x564), v55b

    Begin block 0x560
    prev=[0x558], succ=[]
    =================================
    0x560: v560(0x0) = CONST 
    0x563: REVERT v560(0x0), v560(0x0)

    Begin block 0x564
    prev=[0x558], succ=[0xca7]
    =================================
    0x566: v566(0x16f1) = CONST 
    0x569: v569(0xca7) = CONST 
    0x56c: JUMP v569(0xca7)

    Begin block 0xca7
    prev=[0x564], succ=[0x16f1]
    =================================
    0xca8: vca8(0x4) = CONST 
    0xcaa: vcaa = SLOAD vca8(0x4)
    0xcab: vcab(0x1) = CONST 
    0xcad: vcad(0x1) = CONST 
    0xcaf: vcaf(0xa0) = CONST 
    0xcb1: vcb1(0x10000000000000000000000000000000000000000) = SHL vcaf(0xa0), vcad(0x1)
    0xcb2: vcb2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcb1(0x10000000000000000000000000000000000000000), vcab(0x1)
    0xcb3: vcb3 = AND vcb2(0xffffffffffffffffffffffffffffffffffffffff), vcaa
    0xcb5: JUMP v566(0x16f1)

    Begin block 0x16f1
    prev=[0xca7], succ=[]
    =================================
    0x16f2: v16f2(0x40) = CONST 
    0x16f5: v16f5 = MLOAD v16f2(0x40)
    0x16f6: v16f6(0x1) = CONST 
    0x16f8: v16f8(0x1) = CONST 
    0x16fa: v16fa(0xa0) = CONST 
    0x16fc: v16fc(0x10000000000000000000000000000000000000000) = SHL v16fa(0xa0), v16f8(0x1)
    0x16fd: v16fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16fc(0x10000000000000000000000000000000000000000), v16f6(0x1)
    0x1700: v1700 = AND vcb3, v16fd(0xffffffffffffffffffffffffffffffffffffffff)
    0x1702: MSTORE v16f5, v1700
    0x1703: v1703 = MLOAD v16f2(0x40)
    0x1707: v1707(0x0) = SUB v16f5, v1703
    0x1708: v1708(0x20) = CONST 
    0x170a: v170a(0x20) = ADD v1708(0x20), v1707(0x0)
    0x170c: RETURN v1703, v170a(0x20)

}

function PERMIT_TYPEHASH()() public {
    Begin block 0x56d
    prev=[], succ=[0x575, 0x579]
    =================================
    0x56e: v56e = CALLVALUE 
    0x570: v570 = ISZERO v56e
    0x571: v571(0x579) = CONST 
    0x574: JUMPI v571(0x579), v570

    Begin block 0x575
    prev=[0x56d], succ=[]
    =================================
    0x575: v575(0x0) = CONST 
    0x578: REVERT v575(0x0), v575(0x0)

    Begin block 0x579
    prev=[0x56d], succ=[0xcb6]
    =================================
    0x57b: v57b(0x172c) = CONST 
    0x57e: v57e(0xcb6) = CONST 
    0x581: JUMP v57e(0xcb6)

    Begin block 0xcb6
    prev=[0x579], succ=[0x172c]
    =================================
    0xcb7: vcb7(0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9) = CONST 
    0xcd9: JUMP v57b(0x172c)

    Begin block 0x172c
    prev=[0xcb6], succ=[]
    =================================
    0x172d: v172d(0x40) = CONST 
    0x1730: v1730 = MLOAD v172d(0x40)
    0x1733: MSTORE v1730, vcb7(0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9)
    0x1734: v1734 = MLOAD v172d(0x40)
    0x1738: v1738(0x0) = SUB v1730, v1734
    0x1739: v1739(0x20) = CONST 
    0x173b: v173b(0x20) = ADD v1739(0x20), v1738(0x0)
    0x173d: RETURN v1734, v173b(0x20)

}

function decimals()() public {
    Begin block 0x582
    prev=[], succ=[0x58a, 0x58e]
    =================================
    0x583: v583 = CALLVALUE 
    0x585: v585 = ISZERO v583
    0x586: v586(0x58e) = CONST 
    0x589: JUMPI v586(0x58e), v585

    Begin block 0x58a
    prev=[0x582], succ=[]
    =================================
    0x58a: v58a(0x0) = CONST 
    0x58d: REVERT v58a(0x0), v58a(0x0)

    Begin block 0x58e
    prev=[0x582], succ=[0xcda]
    =================================
    0x590: v590(0x597) = CONST 
    0x593: v593(0xcda) = CONST 
    0x596: JUMP v593(0xcda)

    Begin block 0xcda
    prev=[0x58e], succ=[0x597]
    =================================
    0xcdb: vcdb(0x3) = CONST 
    0xcdd: vcdd = SLOAD vcdb(0x3)
    0xcde: vcde(0xff) = CONST 
    0xce0: vce0 = AND vcde(0xff), vcdd
    0xce2: JUMP v590(0x597)

    Begin block 0x597
    prev=[0xcda], succ=[]
    =================================
    0x598: v598(0x40) = CONST 
    0x59b: v59b = MLOAD v598(0x40)
    0x59c: v59c(0xff) = CONST 
    0x5a0: v5a0 = AND vce0, v59c(0xff)
    0x5a2: MSTORE v59b, v5a0
    0x5a3: v5a3 = MLOAD v598(0x40)
    0x5a7: v5a7(0x0) = SUB v59b, v5a3
    0x5a8: v5a8(0x20) = CONST 
    0x5aa: v5aa(0x20) = ADD v5a8(0x20), v5a7(0x0)
    0x5ac: RETURN v5a3, v5aa(0x20)

}

function DOMAIN_SEPARATOR()() public {
    Begin block 0x5ad
    prev=[], succ=[0x5b5, 0x5b9]
    =================================
    0x5ae: v5ae = CALLVALUE 
    0x5b0: v5b0 = ISZERO v5ae
    0x5b1: v5b1(0x5b9) = CONST 
    0x5b4: JUMPI v5b1(0x5b9), v5b0

    Begin block 0x5b5
    prev=[0x5ad], succ=[]
    =================================
    0x5b5: v5b5(0x0) = CONST 
    0x5b8: REVERT v5b5(0x0), v5b5(0x0)

    Begin block 0x5b9
    prev=[0x5ad], succ=[0xce3]
    =================================
    0x5bb: v5bb(0x175d) = CONST 
    0x5be: v5be(0xce3) = CONST 
    0x5c1: JUMP v5be(0xce3)

    Begin block 0xce3
    prev=[0x5b9], succ=[0x175d]
    =================================
    0xce4: vce4(0xd) = CONST 
    0xce6: vce6 = SLOAD vce4(0xd)
    0xce8: JUMP v5bb(0x175d)

    Begin block 0x175d
    prev=[0xce3], succ=[]
    =================================
    0x175e: v175e(0x40) = CONST 
    0x1761: v1761 = MLOAD v175e(0x40)
    0x1764: MSTORE v1761, vce6
    0x1765: v1765 = MLOAD v175e(0x40)
    0x1769: v1769(0x0) = SUB v1761, v1765
    0x176a: v176a(0x20) = CONST 
    0x176c: v176c(0x20) = ADD v176a(0x20), v1769(0x0)
    0x176e: RETURN v1765, v176c(0x20)

}

function getCurrentVotes(address)() public {
    Begin block 0x5c2
    prev=[], succ=[0x5ca, 0x5ce]
    =================================
    0x5c3: v5c3 = CALLVALUE 
    0x5c5: v5c5 = ISZERO v5c3
    0x5c6: v5c6(0x5ce) = CONST 
    0x5c9: JUMPI v5c6(0x5ce), v5c5

    Begin block 0x5ca
    prev=[0x5c2], succ=[]
    =================================
    0x5ca: v5ca(0x0) = CONST 
    0x5cd: REVERT v5ca(0x0), v5ca(0x0)

    Begin block 0x5ce
    prev=[0x5c2], succ=[0x5e1, 0x5e50x5c2]
    =================================
    0x5d0: v5d0(0x178e) = CONST 
    0x5d3: v5d3(0x4) = CONST 
    0x5d6: v5d6 = CALLDATASIZE 
    0x5d7: v5d7 = SUB v5d6, v5d3(0x4)
    0x5d8: v5d8(0x20) = CONST 
    0x5db: v5db = LT v5d7, v5d8(0x20)
    0x5dc: v5dc = ISZERO v5db
    0x5dd: v5dd(0x5e5) = CONST 
    0x5e0: JUMPI v5dd(0x5e5), v5dc

    Begin block 0x5e1
    prev=[0x5ce], succ=[]
    =================================
    0x5e1: v5e1(0x0) = CONST 
    0x5e4: REVERT v5e1(0x0), v5e1(0x0)

    Begin block 0x5e50x5c2
    prev=[0x5ce], succ=[0xce90x5c2]
    =================================
    0x5e70x5c2: v5c25e7 = CALLDATALOAD v5d3(0x4)
    0x5e80x5c2: v5c25e8(0x1) = CONST 
    0x5ea0x5c2: v5c25ea(0x1) = CONST 
    0x5ec0x5c2: v5c25ec(0xa0) = CONST 
    0x5ee0x5c2: v5c25ee(0x10000000000000000000000000000000000000000) = SHL v5c25ec(0xa0), v5c25ea(0x1)
    0x5ef0x5c2: v5c25ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c25ee(0x10000000000000000000000000000000000000000), v5c25e8(0x1)
    0x5f00x5c2: v5c25f0 = AND v5c25ef(0xffffffffffffffffffffffffffffffffffffffff), v5c25e7
    0x5f10x5c2: v5c25f1(0xce9) = CONST 
    0x5f40x5c2: JUMP v5c25f1(0xce9)

    Begin block 0xce90x5c2
    prev=[0x5e50x5c2], succ=[0x12de0x5c2]
    =================================
    0xcea0x5c2: v5c2cea(0x0) = CONST 
    0xcec0x5c2: v5c2cec(0xcf3) = CONST 
    0xcef0x5c2: v5c2cef(0x12de) = CONST 
    0xcf20x5c2: JUMP v5c2cef(0x12de)

    Begin block 0x12de0x5c2
    prev=[0xce90x5c2], succ=[0x13600x5c2]
    =================================
    0x12df0x5c2: v5c212df(0x60) = CONST 
    0x12e10x5c2: v5c212e1(0x0) = CONST 
    0x12e30x5c2: v5c212e3 = ADDRESS 
    0x12e40x5c2: v5c212e4(0x1) = CONST 
    0x12e60x5c2: v5c212e6(0x1) = CONST 
    0x12e80x5c2: v5c212e8(0xa0) = CONST 
    0x12ea0x5c2: v5c212ea(0x10000000000000000000000000000000000000000) = SHL v5c212e8(0xa0), v5c212e6(0x1)
    0x12eb0x5c2: v5c212eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c212ea(0x10000000000000000000000000000000000000000), v5c212e4(0x1)
    0x12ec0x5c2: v5c212ec = AND v5c212eb(0xffffffffffffffffffffffffffffffffffffffff), v5c212e3
    0x12ed0x5c2: v5c212ed(0x0) = CONST 
    0x12ef0x5c2: v5c212ef = CALLDATASIZE 
    0x12f00x5c2: v5c212f0(0x40) = CONST 
    0x12f20x5c2: v5c212f2 = MLOAD v5c212f0(0x40)
    0x12f30x5c2: v5c212f3(0x24) = CONST 
    0x12f50x5c2: v5c212f5 = ADD v5c212f3(0x24), v5c212f2
    0x12f80x5c2: v5c212f8(0x20) = CONST 
    0x12fa0x5c2: v5c212fa = ADD v5c212f8(0x20), v5c212f5
    0x12fd0x5c2: v5c212fd(0x20) = SUB v5c212fa, v5c212f5
    0x12ff0x5c2: MSTORE v5c212f5, v5c212fd(0x20)
    0x13050x5c2: MSTORE v5c212fa, v5c212ef
    0x13060x5c2: v5c21306(0x20) = CONST 
    0x13080x5c2: v5c21308 = ADD v5c21306(0x20), v5c212fa
    0x130e0x5c2: CALLDATACOPY v5c21308, v5c212ed(0x0), v5c212ef
    0x130f0x5c2: v5c2130f(0x0) = CONST 
    0x13130x5c2: v5c21313 = ADD v5c212ef, v5c21308
    0x13140x5c2: MSTORE v5c21313, v5c2130f(0x0)
    0x13150x5c2: v5c21315(0x40) = CONST 
    0x13180x5c2: v5c21318 = MLOAD v5c21315(0x40)
    0x13190x5c2: v5c21319(0x1f) = CONST 
    0x131d0x5c2: v5c2131d = ADD v5c212ef, v5c21319(0x1f)
    0x131e0x5c2: v5c2131e(0x1f) = CONST 
    0x13200x5c2: v5c21320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v5c2131e(0x1f)
    0x13230x5c2: v5c21323 = AND v5c21320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v5c2131d
    0x13260x5c2: v5c21326 = ADD v5c21308, v5c21323
    0x13290x5c2: v5c21329 = SUB v5c21326, v5c21318
    0x132c0x5c2: v5c2132c = ADD v5c21320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v5c21329
    0x132e0x5c2: MSTORE v5c21318, v5c2132c
    0x13310x5c2: MSTORE v5c21315(0x40), v5c21326
    0x13320x5c2: v5c21332(0x20) = CONST 
    0x13350x5c2: v5c21335 = ADD v5c21318, v5c21332(0x20)
    0x13370x5c2: v5c21337 = MLOAD v5c21335
    0x13380x5c2: v5c21338(0x1) = CONST 
    0x133a0x5c2: v5c2133a(0x1) = CONST 
    0x133c0x5c2: v5c2133c(0xe0) = CONST 
    0x133e0x5c2: v5c2133e(0x100000000000000000000000000000000000000000000000000000000) = SHL v5c2133c(0xe0), v5c2133a(0x1)
    0x133f0x5c2: v5c2133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v5c2133e(0x100000000000000000000000000000000000000000000000000000000), v5c21338(0x1)
    0x13400x5c2: v5c21340 = AND v5c2133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v5c21337
    0x13410x5c2: v5c21341(0x933c1ed) = CONST 
    0x13460x5c2: v5c21346(0xe0) = CONST 
    0x13480x5c2: v5c21348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v5c21346(0xe0), v5c21341(0x933c1ed)
    0x13490x5c2: v5c21349 = OR v5c21348(0x933c1ed00000000000000000000000000000000000000000000000000000000), v5c21340
    0x134b0x5c2: MSTORE v5c21335, v5c21349
    0x134d0x5c2: v5c2134d = MLOAD v5c21315(0x40)
    0x134f0x5c2: v5c2134f = MLOAD v5c21318

    Begin block 0x13600x5c2
    prev=[0x13690x5c2, 0x12de0x5c2], succ=[0x137f0x5c2, 0x13690x5c2]
    =================================
    0x13600x5c2_0x2: v13605c2_2 = PHI v5c21372, v5c2134f
    0x13610x5c2: v5c21361(0x20) = CONST 
    0x13640x5c2: v5c21364 = LT v13605c2_2, v5c21361(0x20)
    0x13650x5c2: v5c21365(0x137f) = CONST 
    0x13680x5c2: JUMPI v5c21365(0x137f), v5c21364

    Begin block 0x137f0x5c2
    prev=[0x13600x5c2], succ=[0x13be0x5c2, 0x13df0x5c2]
    =================================
    0x137f0x5c2_0x0: v137f5c2_0 = PHI v5c2137a, v5c21335
    0x137f0x5c2_0x1: v137f5c2_1 = PHI v5c21378, v5c2134d
    0x137f0x5c2_0x2: v137f5c2_2 = PHI v5c21372, v5c2134f
    0x13800x5c2: v5c21380(0x1) = CONST 
    0x13830x5c2: v5c21383(0x20) = CONST 
    0x13850x5c2: v5c21385 = SUB v5c21383(0x20), v137f5c2_2
    0x13860x5c2: v5c21386(0x100) = CONST 
    0x13890x5c2: v5c21389 = EXP v5c21386(0x100), v5c21385
    0x138a0x5c2: v5c2138a = SUB v5c21389, v5c21380(0x1)
    0x138c0x5c2: v5c2138c = NOT v5c2138a
    0x138e0x5c2: v5c2138e = MLOAD v137f5c2_0
    0x138f0x5c2: v5c2138f = AND v5c2138e, v5c2138c
    0x13920x5c2: v5c21392 = MLOAD v137f5c2_1
    0x13930x5c2: v5c21393 = AND v5c21392, v5c2138a
    0x13960x5c2: v5c21396 = OR v5c2138f, v5c21393
    0x13980x5c2: MSTORE v137f5c2_1, v5c21396
    0x13a10x5c2: v5c213a1 = ADD v5c2134f, v5c2134d
    0x13a50x5c2: v5c213a5(0x0) = CONST 
    0x13a70x5c2: v5c213a7(0x40) = CONST 
    0x13a90x5c2: v5c213a9 = MLOAD v5c213a7(0x40)
    0x13ac0x5c2: v5c213ac = SUB v5c213a1, v5c213a9
    0x13af0x5c2: v5c213af = GAS 
    0x13b00x5c2: v5c213b0 = STATICCALL v5c213af, v5c212ec, v5c213a9, v5c213ac, v5c213a9, v5c213a5(0x0)
    0x13b40x5c2: v5c213b4 = RETURNDATASIZE 
    0x13b60x5c2: v5c213b6(0x0) = CONST 
    0x13b90x5c2: v5c213b9 = EQ v5c213b4, v5c213b6(0x0)
    0x13ba0x5c2: v5c213ba(0x13df) = CONST 
    0x13bd0x5c2: JUMPI v5c213ba(0x13df), v5c213b9

    Begin block 0x13be0x5c2
    prev=[0x137f0x5c2], succ=[0x13e40x5c2]
    =================================
    0x13be0x5c2: v5c213be(0x40) = CONST 
    0x13c00x5c2: v5c213c0 = MLOAD v5c213be(0x40)
    0x13c30x5c2: v5c213c3(0x1f) = CONST 
    0x13c50x5c2: v5c213c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v5c213c3(0x1f)
    0x13c60x5c2: v5c213c6(0x3f) = CONST 
    0x13c80x5c2: v5c213c8 = RETURNDATASIZE 
    0x13c90x5c2: v5c213c9 = ADD v5c213c8, v5c213c6(0x3f)
    0x13ca0x5c2: v5c213ca = AND v5c213c9, v5c213c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0x5c2: v5c213cc = ADD v5c213c0, v5c213ca
    0x13cd0x5c2: v5c213cd(0x40) = CONST 
    0x13cf0x5c2: MSTORE v5c213cd(0x40), v5c213cc
    0x13d00x5c2: v5c213d0 = RETURNDATASIZE 
    0x13d20x5c2: MSTORE v5c213c0, v5c213d0
    0x13d30x5c2: v5c213d3 = RETURNDATASIZE 
    0x13d40x5c2: v5c213d4(0x0) = CONST 
    0x13d60x5c2: v5c213d6(0x20) = CONST 
    0x13d90x5c2: v5c213d9 = ADD v5c213c0, v5c213d6(0x20)
    0x13da0x5c2: RETURNDATACOPY v5c213d9, v5c213d4(0x0), v5c213d3
    0x13db0x5c2: v5c213db(0x13e4) = CONST 
    0x13de0x5c2: JUMP v5c213db(0x13e4)

    Begin block 0x13e40x5c2
    prev=[0x13be0x5c2, 0x13df0x5c2], succ=[0x13f80x5c2, 0x155f0x5c2]
    =================================
    0x13e90x5c2: v5c213e9(0x40) = CONST 
    0x13eb0x5c2: v5c213eb = MLOAD v5c213e9(0x40)
    0x13ec0x5c2: v5c213ec = RETURNDATASIZE 
    0x13ed0x5c2: v5c213ed(0x0) = CONST 
    0x13f00x5c2: RETURNDATACOPY v5c213eb, v5c213ed(0x0), v5c213ec
    0x13f30x5c2: v5c213f3 = ISZERO v5c213b0
    0x13f40x5c2: v5c213f4(0x155f) = CONST 
    0x13f70x5c2: JUMPI v5c213f4(0x155f), v5c213f3

    Begin block 0x13f80x5c2
    prev=[0x13e40x5c2], succ=[]
    =================================
    0x13f80x5c2: v5c213f8(0x40) = CONST 
    0x13fa0x5c2: v5c213fa = RETURNDATASIZE 
    0x13fb0x5c2: v5c213fb = SUB v5c213fa, v5c213f8(0x40)
    0x13fc0x5c2: v5c213fc(0x40) = CONST 
    0x13ff0x5c2: v5c213ff = ADD v5c213eb, v5c213fc(0x40)
    0x14000x5c2: RETURN v5c213ff, v5c213fb

    Begin block 0x155f0x5c2
    prev=[0x13e40x5c2], succ=[]
    =================================
    0x15600x5c2: v5c21560 = RETURNDATASIZE 
    0x15620x5c2: REVERT v5c213eb, v5c21560

    Begin block 0x13df0x5c2
    prev=[0x137f0x5c2], succ=[0x13e40x5c2]
    =================================
    0x13e00x5c2: v5c213e0(0x60) = CONST 

    Begin block 0x13690x5c2
    prev=[0x13600x5c2], succ=[0x13600x5c2]
    =================================
    0x13690x5c2_0x0: v13695c2_0 = PHI v5c2137a, v5c21335
    0x13690x5c2_0x1: v13695c2_1 = PHI v5c21378, v5c2134d
    0x13690x5c2_0x2: v13695c2_2 = PHI v5c21372, v5c2134f
    0x136a0x5c2: v5c2136a = MLOAD v13695c2_0
    0x136c0x5c2: MSTORE v13695c2_1, v5c2136a
    0x136d0x5c2: v5c2136d(0x1f) = CONST 
    0x136f0x5c2: v5c2136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v5c2136d(0x1f)
    0x13720x5c2: v5c21372 = ADD v13695c2_2, v5c2136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740x5c2: v5c21374(0x20) = CONST 
    0x13780x5c2: v5c21378 = ADD v5c21374(0x20), v13695c2_1
    0x137a0x5c2: v5c2137a = ADD v5c21374(0x20), v13695c2_0
    0x137b0x5c2: v5c2137b(0x1360) = CONST 
    0x137e0x5c2: JUMP v5c2137b(0x1360)

}

function delegateToViewImplementation(bytes)() public {
    Begin block 0x5f5
    prev=[], succ=[0x5fd, 0x601]
    =================================
    0x5f6: v5f6 = CALLVALUE 
    0x5f8: v5f8 = ISZERO v5f6
    0x5f9: v5f9(0x601) = CONST 
    0x5fc: JUMPI v5f9(0x601), v5f8

    Begin block 0x5fd
    prev=[0x5f5], succ=[]
    =================================
    0x5fd: v5fd(0x0) = CONST 
    0x600: REVERT v5fd(0x0), v5fd(0x0)

    Begin block 0x601
    prev=[0x5f5], succ=[0x614, 0x618]
    =================================
    0x603: v603(0x30b) = CONST 
    0x606: v606(0x4) = CONST 
    0x609: v609 = CALLDATASIZE 
    0x60a: v60a = SUB v609, v606(0x4)
    0x60b: v60b(0x20) = CONST 
    0x60e: v60e = LT v60a, v60b(0x20)
    0x60f: v60f = ISZERO v60e
    0x610: v610(0x618) = CONST 
    0x613: JUMPI v610(0x618), v60f

    Begin block 0x614
    prev=[0x601], succ=[]
    =================================
    0x614: v614(0x0) = CONST 
    0x617: REVERT v614(0x0), v614(0x0)

    Begin block 0x618
    prev=[0x601], succ=[0x62e, 0x632]
    =================================
    0x61a: v61a = ADD v606(0x4), v60a
    0x61c: v61c(0x20) = CONST 
    0x61f: v61f(0x24) = ADD v606(0x4), v61c(0x20)
    0x621: v621 = CALLDATALOAD v606(0x4)
    0x622: v622(0x1) = CONST 
    0x624: v624(0x20) = CONST 
    0x626: v626(0x100000000) = SHL v624(0x20), v622(0x1)
    0x628: v628 = GT v621, v626(0x100000000)
    0x629: v629 = ISZERO v628
    0x62a: v62a(0x632) = CONST 
    0x62d: JUMPI v62a(0x632), v629

    Begin block 0x62e
    prev=[0x618], succ=[]
    =================================
    0x62e: v62e(0x0) = CONST 
    0x631: REVERT v62e(0x0), v62e(0x0)

    Begin block 0x632
    prev=[0x618], succ=[0x640, 0x644]
    =================================
    0x634: v634 = ADD v606(0x4), v621
    0x636: v636(0x20) = CONST 
    0x639: v639 = ADD v634, v636(0x20)
    0x63a: v63a = GT v639, v61a
    0x63b: v63b = ISZERO v63a
    0x63c: v63c(0x644) = CONST 
    0x63f: JUMPI v63c(0x644), v63b

    Begin block 0x640
    prev=[0x632], succ=[]
    =================================
    0x640: v640(0x0) = CONST 
    0x643: REVERT v640(0x0), v640(0x0)

    Begin block 0x644
    prev=[0x632], succ=[0x661, 0x665]
    =================================
    0x646: v646 = CALLDATALOAD v634
    0x648: v648(0x20) = CONST 
    0x64a: v64a = ADD v648(0x20), v634
    0x64d: v64d(0x1) = CONST 
    0x650: v650 = MUL v646, v64d(0x1)
    0x652: v652 = ADD v64a, v650
    0x653: v653 = GT v652, v61a
    0x654: v654(0x1) = CONST 
    0x656: v656(0x20) = CONST 
    0x658: v658(0x100000000) = SHL v656(0x20), v654(0x1)
    0x65a: v65a = GT v646, v658(0x100000000)
    0x65b: v65b = OR v65a, v653
    0x65c: v65c = ISZERO v65b
    0x65d: v65d(0x665) = CONST 
    0x660: JUMPI v65d(0x665), v65c

    Begin block 0x661
    prev=[0x644], succ=[]
    =================================
    0x661: v661(0x0) = CONST 
    0x664: REVERT v661(0x0), v661(0x0)

    Begin block 0x665
    prev=[0x644], succ=[0xcf9]
    =================================
    0x66a: v66a(0x1f) = CONST 
    0x66c: v66c = ADD v66a(0x1f), v646
    0x66d: v66d(0x20) = CONST 
    0x671: v671 = DIV v66c, v66d(0x20)
    0x672: v672 = MUL v671, v66d(0x20)
    0x673: v673(0x20) = CONST 
    0x675: v675 = ADD v673(0x20), v672
    0x676: v676(0x40) = CONST 
    0x678: v678 = MLOAD v676(0x40)
    0x67b: v67b = ADD v678, v675
    0x67c: v67c(0x40) = CONST 
    0x67e: MSTORE v67c(0x40), v67b
    0x686: MSTORE v678, v646
    0x687: v687(0x20) = CONST 
    0x689: v689 = ADD v687(0x20), v678
    0x68f: CALLDATACOPY v689, v64a, v646
    0x690: v690(0x0) = CONST 
    0x693: v693 = ADD v689, v646
    0x697: MSTORE v693, v690(0x0)
    0x69c: v69c(0xcf9) = CONST 
    0x6a5: JUMP v69c(0xcf9)

    Begin block 0xcf9
    prev=[0x665], succ=[0xd32]
    =================================
    0xcfa: vcfa(0x60) = CONST 
    0xcfc: vcfc(0x0) = CONST 
    0xcfe: vcfe(0x60) = CONST 
    0xd00: vd00 = ADDRESS 
    0xd01: vd01(0x1) = CONST 
    0xd03: vd03(0x1) = CONST 
    0xd05: vd05(0xa0) = CONST 
    0xd07: vd07(0x10000000000000000000000000000000000000000) = SHL vd05(0xa0), vd03(0x1)
    0xd08: vd08(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd07(0x10000000000000000000000000000000000000000), vd01(0x1)
    0xd09: vd09 = AND vd08(0xffffffffffffffffffffffffffffffffffffffff), vd00
    0xd0b: vd0b(0x40) = CONST 
    0xd0d: vd0d = MLOAD vd0b(0x40)
    0xd0e: vd0e(0x24) = CONST 
    0xd10: vd10 = ADD vd0e(0x24), vd0d
    0xd13: vd13(0x20) = CONST 
    0xd15: vd15 = ADD vd13(0x20), vd10
    0xd18: vd18(0x20) = SUB vd15, vd10
    0xd1a: MSTORE vd10, vd18(0x20)
    0xd1e: vd1e = MLOAD v678
    0xd20: MSTORE vd15, vd1e
    0xd21: vd21(0x20) = CONST 
    0xd23: vd23 = ADD vd21(0x20), vd15
    0xd27: vd27 = MLOAD v678
    0xd29: vd29(0x20) = CONST 
    0xd2b: vd2b = ADD vd29(0x20), v678
    0xd30: vd30(0x0) = CONST 

    Begin block 0xd32
    prev=[0xcf9, 0xd3b], succ=[0xd4a, 0xd3b]
    =================================
    0xd32_0x0: vd32_0 = PHI vd30(0x0), vd45
    0xd35: vd35 = LT vd32_0, vd27
    0xd36: vd36 = ISZERO vd35
    0xd37: vd37(0xd4a) = CONST 
    0xd3a: JUMPI vd37(0xd4a), vd36

    Begin block 0xd4a
    prev=[0xd32], succ=[0xd77, 0xd5e]
    =================================
    0xd53: vd53 = ADD vd27, vd23
    0xd55: vd55(0x1f) = CONST 
    0xd57: vd57 = AND vd55(0x1f), vd27
    0xd59: vd59 = ISZERO vd57
    0xd5a: vd5a(0xd77) = CONST 
    0xd5d: JUMPI vd5a(0xd77), vd59

    Begin block 0xd77
    prev=[0xd4a, 0xd5e], succ=[0xdb3]
    =================================
    0xd77_0x1: vd77_1 = PHI vd53, vd74
    0xd79: vd79(0x40) = CONST 
    0xd7c: vd7c = MLOAD vd79(0x40)
    0xd7d: vd7d(0x1f) = CONST 
    0xd7f: vd7f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vd7d(0x1f)
    0xd82: vd82 = SUB vd77_1, vd7c
    0xd83: vd83 = ADD vd82, vd7f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xd85: MSTORE vd7c, vd83
    0xd88: MSTORE vd79(0x40), vd77_1
    0xd89: vd89(0x20) = CONST 
    0xd8c: vd8c = ADD vd7c, vd89(0x20)
    0xd8e: vd8e = MLOAD vd8c
    0xd8f: vd8f(0x1) = CONST 
    0xd91: vd91(0x1) = CONST 
    0xd93: vd93(0xe0) = CONST 
    0xd95: vd95(0x100000000000000000000000000000000000000000000000000000000) = SHL vd93(0xe0), vd91(0x1)
    0xd96: vd96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vd95(0x100000000000000000000000000000000000000000000000000000000), vd8f(0x1)
    0xd97: vd97 = AND vd96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vd8e
    0xd98: vd98(0x933c1ed) = CONST 
    0xd9d: vd9d(0xe0) = CONST 
    0xd9f: vd9f(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL vd9d(0xe0), vd98(0x933c1ed)
    0xda0: vda0 = OR vd9f(0x933c1ed00000000000000000000000000000000000000000000000000000000), vd97
    0xda2: MSTORE vd8c, vda0
    0xda4: vda4 = MLOAD vd79(0x40)
    0xda6: vda6 = MLOAD vd7c

    Begin block 0xdb3
    prev=[0xd77, 0xdbc], succ=[0xdd2, 0xdbc]
    =================================
    0xdb3_0x2: vdb3_2 = PHI vda6, vdc5
    0xdb4: vdb4(0x20) = CONST 
    0xdb7: vdb7 = LT vdb3_2, vdb4(0x20)
    0xdb8: vdb8(0xdd2) = CONST 
    0xdbb: JUMPI vdb8(0xdd2), vdb7

    Begin block 0xdd2
    prev=[0xdb3], succ=[0xe11, 0xe32]
    =================================
    0xdd2_0x0: vdd2_0 = PHI vd8c, vdcd
    0xdd2_0x1: vdd2_1 = PHI vda4, vdcb
    0xdd2_0x2: vdd2_2 = PHI vda6, vdc5
    0xdd3: vdd3(0x1) = CONST 
    0xdd6: vdd6(0x20) = CONST 
    0xdd8: vdd8 = SUB vdd6(0x20), vdd2_2
    0xdd9: vdd9(0x100) = CONST 
    0xddc: vddc = EXP vdd9(0x100), vdd8
    0xddd: vddd = SUB vddc, vdd3(0x1)
    0xddf: vddf = NOT vddd
    0xde1: vde1 = MLOAD vdd2_0
    0xde2: vde2 = AND vde1, vddf
    0xde5: vde5 = MLOAD vdd2_1
    0xde6: vde6 = AND vde5, vddd
    0xde9: vde9 = OR vde2, vde6
    0xdeb: MSTORE vdd2_1, vde9
    0xdf4: vdf4 = ADD vda6, vda4
    0xdf8: vdf8(0x0) = CONST 
    0xdfa: vdfa(0x40) = CONST 
    0xdfc: vdfc = MLOAD vdfa(0x40)
    0xdff: vdff = SUB vdf4, vdfc
    0xe02: ve02 = GAS 
    0xe03: ve03 = STATICCALL ve02, vd09, vdfc, vdff, vdfc, vdf8(0x0)
    0xe07: ve07 = RETURNDATASIZE 
    0xe09: ve09(0x0) = CONST 
    0xe0c: ve0c = EQ ve07, ve09(0x0)
    0xe0d: ve0d(0xe32) = CONST 
    0xe10: JUMPI ve0d(0xe32), ve0c

    Begin block 0xe11
    prev=[0xdd2], succ=[0xe37]
    =================================
    0xe11: ve11(0x40) = CONST 
    0xe13: ve13 = MLOAD ve11(0x40)
    0xe16: ve16(0x1f) = CONST 
    0xe18: ve18(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT ve16(0x1f)
    0xe19: ve19(0x3f) = CONST 
    0xe1b: ve1b = RETURNDATASIZE 
    0xe1c: ve1c = ADD ve1b, ve19(0x3f)
    0xe1d: ve1d = AND ve1c, ve18(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xe1f: ve1f = ADD ve13, ve1d
    0xe20: ve20(0x40) = CONST 
    0xe22: MSTORE ve20(0x40), ve1f
    0xe23: ve23 = RETURNDATASIZE 
    0xe25: MSTORE ve13, ve23
    0xe26: ve26 = RETURNDATASIZE 
    0xe27: ve27(0x0) = CONST 
    0xe29: ve29(0x20) = CONST 
    0xe2c: ve2c = ADD ve13, ve29(0x20)
    0xe2d: RETURNDATACOPY ve2c, ve27(0x0), ve26
    0xe2e: ve2e(0xe37) = CONST 
    0xe31: JUMP ve2e(0xe37)

    Begin block 0xe37
    prev=[0xe11, 0xe32], succ=[0xe46, 0xe4c]
    =================================
    0xe3d: ve3d(0x0) = CONST 
    0xe40: ve40 = EQ ve03, ve3d(0x0)
    0xe41: ve41 = ISZERO ve40
    0xe42: ve42(0xe4c) = CONST 
    0xe45: JUMPI ve42(0xe4c), ve41

    Begin block 0xe46
    prev=[0xe37], succ=[]
    =================================
    0xe46: ve46 = RETURNDATASIZE 
    0xe46_0x0: ve46_0 = PHI ve13, ve33(0x60)
    0xe47: ve47(0x20) = CONST 
    0xe4a: ve4a = ADD ve46_0, ve47(0x20)
    0xe4b: REVERT ve4a, ve46

    Begin block 0xe4c
    prev=[0xe37], succ=[0xe5d, 0xe61]
    =================================
    0xe4c_0x0: ve4c_0 = PHI ve13, ve33(0x60)
    0xe4f: ve4f(0x20) = CONST 
    0xe51: ve51 = ADD ve4f(0x20), ve4c_0
    0xe53: ve53 = MLOAD ve4c_0
    0xe54: ve54(0x20) = CONST 
    0xe57: ve57 = LT ve53, ve54(0x20)
    0xe58: ve58 = ISZERO ve57
    0xe59: ve59(0xe61) = CONST 
    0xe5c: JUMPI ve59(0xe61), ve58

    Begin block 0xe5d
    prev=[0xe4c], succ=[]
    =================================
    0xe5d: ve5d(0x0) = CONST 
    0xe60: REVERT ve5d(0x0), ve5d(0x0)

    Begin block 0xe61
    prev=[0xe4c], succ=[0xe7c, 0xe80]
    =================================
    0xe63: ve63 = ADD ve51, ve53
    0xe67: ve67 = MLOAD ve51
    0xe68: ve68(0x40) = CONST 
    0xe6a: ve6a = MLOAD ve68(0x40)
    0xe70: ve70(0x1) = CONST 
    0xe72: ve72(0x20) = CONST 
    0xe74: ve74(0x100000000) = SHL ve72(0x20), ve70(0x1)
    0xe76: ve76 = GT ve67, ve74(0x100000000)
    0xe77: ve77 = ISZERO ve76
    0xe78: ve78(0xe80) = CONST 
    0xe7b: JUMPI ve78(0xe80), ve77

    Begin block 0xe7c
    prev=[0xe61], succ=[]
    =================================
    0xe7c: ve7c(0x0) = CONST 
    0xe7f: REVERT ve7c(0x0), ve7c(0x0)

    Begin block 0xe80
    prev=[0xe61], succ=[0xe91, 0xe95]
    =================================
    0xe83: ve83 = ADD ve51, ve67
    0xe85: ve85(0x20) = CONST 
    0xe88: ve88 = ADD ve83, ve85(0x20)
    0xe8b: ve8b = GT ve88, ve63
    0xe8c: ve8c = ISZERO ve8b
    0xe8d: ve8d(0xe95) = CONST 
    0xe90: JUMPI ve8d(0xe95), ve8c

    Begin block 0xe91
    prev=[0xe80], succ=[]
    =================================
    0xe91: ve91(0x0) = CONST 
    0xe94: REVERT ve91(0x0), ve91(0x0)

    Begin block 0xe95
    prev=[0xe80], succ=[0xeaa, 0xeae]
    =================================
    0xe97: ve97 = MLOAD ve83
    0xe98: ve98(0x1) = CONST 
    0xe9a: ve9a(0x20) = CONST 
    0xe9c: ve9c(0x100000000) = SHL ve9a(0x20), ve98(0x1)
    0xe9e: ve9e = GT ve97, ve9c(0x100000000)
    0xea1: vea1 = ADD ve97, ve88
    0xea3: vea3 = LT ve63, vea1
    0xea4: vea4 = OR vea3, ve9e
    0xea5: vea5 = ISZERO vea4
    0xea6: vea6(0xeae) = CONST 
    0xea9: JUMPI vea6(0xeae), vea5

    Begin block 0xeaa
    prev=[0xe95], succ=[]
    =================================
    0xeaa: veaa(0x0) = CONST 
    0xead: REVERT veaa(0x0), veaa(0x0)

    Begin block 0xeae
    prev=[0xe95], succ=[0xec3]
    =================================
    0xeb0: MSTORE ve6a, ve97
    0xeb3: veb3 = MLOAD ve83
    0xeb4: veb4(0x20) = CONST 
    0xeb8: veb8 = ADD veb4(0x20), ve6a
    0xebc: vebc = ADD veb4(0x20), ve83
    0xec1: vec1(0x0) = CONST 

    Begin block 0xec3
    prev=[0xeae, 0xecc], succ=[0xedb, 0xecc]
    =================================
    0xec3_0x0: vec3_0 = PHI vec1(0x0), ved6
    0xec6: vec6 = LT vec3_0, veb3
    0xec7: vec7 = ISZERO vec6
    0xec8: vec8(0xedb) = CONST 
    0xecb: JUMPI vec8(0xedb), vec7

    Begin block 0xedb
    prev=[0xec3], succ=[0xf08, 0xeef]
    =================================
    0xee4: vee4 = ADD veb3, veb8
    0xee6: vee6(0x1f) = CONST 
    0xee8: vee8 = AND vee6(0x1f), veb3
    0xeea: veea = ISZERO vee8
    0xeeb: veeb(0xf08) = CONST 
    0xeee: JUMPI veeb(0xf08), veea

    Begin block 0xf08
    prev=[0xedb, 0xeef], succ=[0x30b0x5f5]
    =================================
    0xf08_0x1: vf08_1 = PHI vee4, vf05
    0xf0a: vf0a(0x40) = CONST 
    0xf0c: MSTORE vf0a(0x40), vf08_1
    0xf17: JUMP v603(0x30b)

    Begin block 0x30b0x5f5
    prev=[0xf08], succ=[0x32d0x5f5]
    =================================
    0x30c0x5f5: v5f530c(0x40) = CONST 
    0x30f0x5f5: v5f530f = MLOAD v5f530c(0x40)
    0x3100x5f5: v5f5310(0x20) = CONST 
    0x3140x5f5: MSTORE v5f530f, v5f5310(0x20)
    0x3160x5f5: v5f5316 = MLOAD ve6a
    0x3190x5f5: v5f5319 = ADD v5f530f, v5f5310(0x20)
    0x31a0x5f5: MSTORE v5f5319, v5f5316
    0x31c0x5f5: v5f531c = MLOAD ve6a
    0x3230x5f5: v5f5323 = ADD v5f530f, v5f530c(0x40)
    0x3260x5f5: v5f5326 = ADD ve6a, v5f5310(0x20)
    0x32b0x5f5: v5f532b(0x0) = CONST 

    Begin block 0x32d0x5f5
    prev=[0x3360x5f5, 0x30b0x5f5], succ=[0x3450x5f5, 0x3360x5f5]
    =================================
    0x32d0x5f5_0x0: v32d5f5_0 = PHI v5f5340, v5f532b(0x0)
    0x3300x5f5: v5f5330 = LT v32d5f5_0, v5f531c
    0x3310x5f5: v5f5331 = ISZERO v5f5330
    0x3320x5f5: v5f5332(0x345) = CONST 
    0x3350x5f5: JUMPI v5f5332(0x345), v5f5331

    Begin block 0x3450x5f5
    prev=[0x32d0x5f5], succ=[0x3720x5f5, 0x3590x5f5]
    =================================
    0x34e0x5f5: v5f534e = ADD v5f531c, v5f5323
    0x3500x5f5: v5f5350(0x1f) = CONST 
    0x3520x5f5: v5f5352 = AND v5f5350(0x1f), v5f531c
    0x3540x5f5: v5f5354 = ISZERO v5f5352
    0x3550x5f5: v5f5355(0x372) = CONST 
    0x3580x5f5: JUMPI v5f5355(0x372), v5f5354

    Begin block 0x3720x5f5
    prev=[0x3450x5f5, 0x3590x5f5], succ=[]
    =================================
    0x3720x5f5_0x1: v3725f5_1 = PHI v5f536f, v5f534e
    0x3780x5f5: v5f5378(0x40) = CONST 
    0x37a0x5f5: v5f537a = MLOAD v5f5378(0x40)
    0x37d0x5f5: v5f537d = SUB v3725f5_1, v5f537a
    0x37f0x5f5: RETURN v5f537a, v5f537d

    Begin block 0x3590x5f5
    prev=[0x3450x5f5], succ=[0x3720x5f5]
    =================================
    0x35b0x5f5: v5f535b = SUB v5f534e, v5f5352
    0x35d0x5f5: v5f535d = MLOAD v5f535b
    0x35e0x5f5: v5f535e(0x1) = CONST 
    0x3610x5f5: v5f5361(0x20) = CONST 
    0x3630x5f5: v5f5363 = SUB v5f5361(0x20), v5f5352
    0x3640x5f5: v5f5364(0x100) = CONST 
    0x3670x5f5: v5f5367 = EXP v5f5364(0x100), v5f5363
    0x3680x5f5: v5f5368 = SUB v5f5367, v5f535e(0x1)
    0x3690x5f5: v5f5369 = NOT v5f5368
    0x36a0x5f5: v5f536a = AND v5f5369, v5f535d
    0x36c0x5f5: MSTORE v5f535b, v5f536a
    0x36d0x5f5: v5f536d(0x20) = CONST 
    0x36f0x5f5: v5f536f = ADD v5f536d(0x20), v5f535b

    Begin block 0x3360x5f5
    prev=[0x32d0x5f5], succ=[0x32d0x5f5]
    =================================
    0x3360x5f5_0x0: v3365f5_0 = PHI v5f5340, v5f532b(0x0)
    0x3380x5f5: v5f5338 = ADD v3365f5_0, v5f5326
    0x3390x5f5: v5f5339 = MLOAD v5f5338
    0x33c0x5f5: v5f533c = ADD v3365f5_0, v5f5323
    0x33d0x5f5: MSTORE v5f533c, v5f5339
    0x33e0x5f5: v5f533e(0x20) = CONST 
    0x3400x5f5: v5f5340 = ADD v5f533e(0x20), v3365f5_0
    0x3410x5f5: v5f5341(0x32d) = CONST 
    0x3440x5f5: JUMP v5f5341(0x32d)

    Begin block 0xeef
    prev=[0xedb], succ=[0xf08]
    =================================
    0xef1: vef1 = SUB vee4, vee8
    0xef3: vef3 = MLOAD vef1
    0xef4: vef4(0x1) = CONST 
    0xef7: vef7(0x20) = CONST 
    0xef9: vef9 = SUB vef7(0x20), vee8
    0xefa: vefa(0x100) = CONST 
    0xefd: vefd = EXP vefa(0x100), vef9
    0xefe: vefe = SUB vefd, vef4(0x1)
    0xeff: veff = NOT vefe
    0xf00: vf00 = AND veff, vef3
    0xf02: MSTORE vef1, vf00
    0xf03: vf03(0x20) = CONST 
    0xf05: vf05 = ADD vf03(0x20), vef1

    Begin block 0xecc
    prev=[0xec3], succ=[0xec3]
    =================================
    0xecc_0x0: vecc_0 = PHI vec1(0x0), ved6
    0xece: vece = ADD vecc_0, vebc
    0xecf: vecf = MLOAD vece
    0xed2: ved2 = ADD vecc_0, veb8
    0xed3: MSTORE ved2, vecf
    0xed4: ved4(0x20) = CONST 
    0xed6: ved6 = ADD ved4(0x20), vecc_0
    0xed7: ved7(0xec3) = CONST 
    0xeda: JUMP ved7(0xec3)

    Begin block 0xe32
    prev=[0xdd2], succ=[0xe37]
    =================================
    0xe33: ve33(0x60) = CONST 

    Begin block 0xdbc
    prev=[0xdb3], succ=[0xdb3]
    =================================
    0xdbc_0x0: vdbc_0 = PHI vd8c, vdcd
    0xdbc_0x1: vdbc_1 = PHI vda4, vdcb
    0xdbc_0x2: vdbc_2 = PHI vda6, vdc5
    0xdbd: vdbd = MLOAD vdbc_0
    0xdbf: MSTORE vdbc_1, vdbd
    0xdc0: vdc0(0x1f) = CONST 
    0xdc2: vdc2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vdc0(0x1f)
    0xdc5: vdc5 = ADD vdbc_2, vdc2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xdc7: vdc7(0x20) = CONST 
    0xdcb: vdcb = ADD vdc7(0x20), vdbc_1
    0xdcd: vdcd = ADD vdc7(0x20), vdbc_0
    0xdce: vdce(0xdb3) = CONST 
    0xdd1: JUMP vdce(0xdb3)

    Begin block 0xd5e
    prev=[0xd4a], succ=[0xd77]
    =================================
    0xd60: vd60 = SUB vd53, vd57
    0xd62: vd62 = MLOAD vd60
    0xd63: vd63(0x1) = CONST 
    0xd66: vd66(0x20) = CONST 
    0xd68: vd68 = SUB vd66(0x20), vd57
    0xd69: vd69(0x100) = CONST 
    0xd6c: vd6c = EXP vd69(0x100), vd68
    0xd6d: vd6d = SUB vd6c, vd63(0x1)
    0xd6e: vd6e = NOT vd6d
    0xd6f: vd6f = AND vd6e, vd62
    0xd71: MSTORE vd60, vd6f
    0xd72: vd72(0x20) = CONST 
    0xd74: vd74 = ADD vd72(0x20), vd60

    Begin block 0xd3b
    prev=[0xd32], succ=[0xd32]
    =================================
    0xd3b_0x0: vd3b_0 = PHI vd30(0x0), vd45
    0xd3d: vd3d = ADD vd3b_0, vd2b
    0xd3e: vd3e = MLOAD vd3d
    0xd41: vd41 = ADD vd3b_0, vd23
    0xd42: MSTORE vd41, vd3e
    0xd43: vd43(0x20) = CONST 
    0xd45: vd45 = ADD vd43(0x20), vd3b_0
    0xd46: vd46(0xd32) = CONST 
    0xd49: JUMP vd46(0xd32)

}

function _setRebaser(address)() public {
    Begin block 0x6a6
    prev=[], succ=[0x6ae, 0x6b2]
    =================================
    0x6a7: v6a7 = CALLVALUE 
    0x6a9: v6a9 = ISZERO v6a7
    0x6aa: v6aa(0x6b2) = CONST 
    0x6ad: JUMPI v6aa(0x6b2), v6a9

    Begin block 0x6ae
    prev=[0x6a6], succ=[]
    =================================
    0x6ae: v6ae(0x0) = CONST 
    0x6b1: REVERT v6ae(0x0), v6ae(0x0)

    Begin block 0x6b2
    prev=[0x6a6], succ=[0x6c5, 0x6c9]
    =================================
    0x6b4: v6b4(0x17bf) = CONST 
    0x6b7: v6b7(0x4) = CONST 
    0x6ba: v6ba = CALLDATASIZE 
    0x6bb: v6bb = SUB v6ba, v6b7(0x4)
    0x6bc: v6bc(0x20) = CONST 
    0x6bf: v6bf = LT v6bb, v6bc(0x20)
    0x6c0: v6c0 = ISZERO v6bf
    0x6c1: v6c1(0x6c9) = CONST 
    0x6c4: JUMPI v6c1(0x6c9), v6c0

    Begin block 0x6c5
    prev=[0x6b2], succ=[]
    =================================
    0x6c5: v6c5(0x0) = CONST 
    0x6c8: REVERT v6c5(0x0), v6c5(0x0)

    Begin block 0x6c9
    prev=[0x6b2], succ=[0xf18]
    =================================
    0x6cb: v6cb = CALLDATALOAD v6b7(0x4)
    0x6cc: v6cc(0x1) = CONST 
    0x6ce: v6ce(0x1) = CONST 
    0x6d0: v6d0(0xa0) = CONST 
    0x6d2: v6d2(0x10000000000000000000000000000000000000000) = SHL v6d0(0xa0), v6ce(0x1)
    0x6d3: v6d3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6d2(0x10000000000000000000000000000000000000000), v6cc(0x1)
    0x6d4: v6d4 = AND v6d3(0xffffffffffffffffffffffffffffffffffffffff), v6cb
    0x6d5: v6d5(0xf18) = CONST 
    0x6d8: JUMP v6d5(0xf18)

    Begin block 0xf18
    prev=[0x6c9], succ=[0xafe0x6a6]
    =================================
    0xf19: vf19(0xf20) = CONST 
    0xf1c: vf1c(0xafe) = CONST 
    0xf1f: JUMP vf1c(0xafe)

    Begin block 0xafe0x6a6
    prev=[0xf18], succ=[0xb450x6a6, 0xb660x6a6]
    =================================
    0xaff0x6a6: v6a6aff(0x12) = CONST 
    0xb010x6a6: v6a6b01 = SLOAD v6a6aff(0x12)
    0xb020x6a6: v6a6b02(0x40) = CONST 
    0xb040x6a6: v6a6b04 = MLOAD v6a6b02(0x40)
    0xb050x6a6: v6a6b05(0x60) = CONST 
    0xb080x6a6: v6a6b08(0x0) = CONST 
    0xb0b0x6a6: v6a6b0b(0x1) = CONST 
    0xb0d0x6a6: v6a6b0d(0x1) = CONST 
    0xb0f0x6a6: v6a6b0f(0xa0) = CONST 
    0xb110x6a6: v6a6b11(0x10000000000000000000000000000000000000000) = SHL v6a6b0f(0xa0), v6a6b0d(0x1)
    0xb120x6a6: v6a6b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6a6b11(0x10000000000000000000000000000000000000000), v6a6b0b(0x1)
    0xb150x6a6: v6a6b15 = AND v6a6b01, v6a6b12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x6a6: v6a6b19 = CALLDATASIZE 
    0xb210x6a6: CALLDATACOPY v6a6b04, v6a6b08(0x0), v6a6b19
    0xb220x6a6: v6a6b22(0x40) = CONST 
    0xb240x6a6: v6a6b24 = MLOAD v6a6b22(0x40)
    0xb260x6a6: v6a6b26 = ADD v6a6b04, v6a6b19
    0xb290x6a6: v6a6b29(0x0) = CONST 
    0xb330x6a6: v6a6b33 = SUB v6a6b26, v6a6b24
    0xb360x6a6: v6a6b36 = GAS 
    0xb370x6a6: v6a6b37 = DELEGATECALL v6a6b36, v6a6b15, v6a6b24, v6a6b33, v6a6b24, v6a6b29(0x0)
    0xb3b0x6a6: v6a6b3b = RETURNDATASIZE 
    0xb3d0x6a6: v6a6b3d(0x0) = CONST 
    0xb400x6a6: v6a6b40 = EQ v6a6b3b, v6a6b3d(0x0)
    0xb410x6a6: v6a6b41(0xb66) = CONST 
    0xb440x6a6: JUMPI v6a6b41(0xb66), v6a6b40

    Begin block 0xb450x6a6
    prev=[0xafe0x6a6], succ=[0xb6b0x6a6]
    =================================
    0xb450x6a6: v6a6b45(0x40) = CONST 
    0xb470x6a6: v6a6b47 = MLOAD v6a6b45(0x40)
    0xb4a0x6a6: v6a6b4a(0x1f) = CONST 
    0xb4c0x6a6: v6a6b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v6a6b4a(0x1f)
    0xb4d0x6a6: v6a6b4d(0x3f) = CONST 
    0xb4f0x6a6: v6a6b4f = RETURNDATASIZE 
    0xb500x6a6: v6a6b50 = ADD v6a6b4f, v6a6b4d(0x3f)
    0xb510x6a6: v6a6b51 = AND v6a6b50, v6a6b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x6a6: v6a6b53 = ADD v6a6b47, v6a6b51
    0xb540x6a6: v6a6b54(0x40) = CONST 
    0xb560x6a6: MSTORE v6a6b54(0x40), v6a6b53
    0xb570x6a6: v6a6b57 = RETURNDATASIZE 
    0xb590x6a6: MSTORE v6a6b47, v6a6b57
    0xb5a0x6a6: v6a6b5a = RETURNDATASIZE 
    0xb5b0x6a6: v6a6b5b(0x0) = CONST 
    0xb5d0x6a6: v6a6b5d(0x20) = CONST 
    0xb600x6a6: v6a6b60 = ADD v6a6b47, v6a6b5d(0x20)
    0xb610x6a6: RETURNDATACOPY v6a6b60, v6a6b5b(0x0), v6a6b5a
    0xb620x6a6: v6a6b62(0xb6b) = CONST 
    0xb650x6a6: JUMP v6a6b62(0xb6b)

    Begin block 0xb6b0x6a6
    prev=[0xb450x6a6, 0xb660x6a6], succ=[0xb7f0x6a6, 0x153c0x6a6]
    =================================
    0xb700x6a6: v6a6b70(0x40) = CONST 
    0xb720x6a6: v6a6b72 = MLOAD v6a6b70(0x40)
    0xb730x6a6: v6a6b73 = RETURNDATASIZE 
    0xb740x6a6: v6a6b74(0x0) = CONST 
    0xb770x6a6: RETURNDATACOPY v6a6b72, v6a6b74(0x0), v6a6b73
    0xb7a0x6a6: v6a6b7a = ISZERO v6a6b37
    0xb7b0x6a6: v6a6b7b(0x153c) = CONST 
    0xb7e0x6a6: JUMPI v6a6b7b(0x153c), v6a6b7a

    Begin block 0xb7f0x6a6
    prev=[0xb6b0x6a6], succ=[]
    =================================
    0xb7f0x6a6: v6a6b7f = RETURNDATASIZE 
    0xb810x6a6: RETURN v6a6b72, v6a6b7f

    Begin block 0x153c0x6a6
    prev=[0xb6b0x6a6], succ=[]
    =================================
    0x153d0x6a6: v6a6153d = RETURNDATASIZE 
    0x153f0x6a6: REVERT v6a6b72, v6a6153d

    Begin block 0xb660x6a6
    prev=[0xafe0x6a6], succ=[0xb6b0x6a6]
    =================================
    0xb670x6a6: v6a6b67(0x60) = CONST 

}

function _acceptGov()() public {
    Begin block 0x6db
    prev=[], succ=[0x6e3, 0x6e7]
    =================================
    0x6dc: v6dc = CALLVALUE 
    0x6de: v6de = ISZERO v6dc
    0x6df: v6df(0x6e7) = CONST 
    0x6e2: JUMPI v6df(0x6e7), v6de

    Begin block 0x6e3
    prev=[0x6db], succ=[]
    =================================
    0x6e3: v6e3(0x0) = CONST 
    0x6e6: REVERT v6e3(0x0), v6e3(0x0)

    Begin block 0x6e7
    prev=[0x6db], succ=[0xf24]
    =================================
    0x6e9: v6e9(0x17e0) = CONST 
    0x6ec: v6ec(0xf24) = CONST 
    0x6ef: JUMP v6ec(0xf24)

    Begin block 0xf24
    prev=[0x6e7], succ=[0xafe0x6db]
    =================================
    0xf25: vf25(0xf2c) = CONST 
    0xf28: vf28(0xafe) = CONST 
    0xf2b: JUMP vf28(0xafe)

    Begin block 0xafe0x6db
    prev=[0xf24], succ=[0xb450x6db, 0xb660x6db]
    =================================
    0xaff0x6db: v6dbaff(0x12) = CONST 
    0xb010x6db: v6dbb01 = SLOAD v6dbaff(0x12)
    0xb020x6db: v6dbb02(0x40) = CONST 
    0xb040x6db: v6dbb04 = MLOAD v6dbb02(0x40)
    0xb050x6db: v6dbb05(0x60) = CONST 
    0xb080x6db: v6dbb08(0x0) = CONST 
    0xb0b0x6db: v6dbb0b(0x1) = CONST 
    0xb0d0x6db: v6dbb0d(0x1) = CONST 
    0xb0f0x6db: v6dbb0f(0xa0) = CONST 
    0xb110x6db: v6dbb11(0x10000000000000000000000000000000000000000) = SHL v6dbb0f(0xa0), v6dbb0d(0x1)
    0xb120x6db: v6dbb12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6dbb11(0x10000000000000000000000000000000000000000), v6dbb0b(0x1)
    0xb150x6db: v6dbb15 = AND v6dbb01, v6dbb12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x6db: v6dbb19 = CALLDATASIZE 
    0xb210x6db: CALLDATACOPY v6dbb04, v6dbb08(0x0), v6dbb19
    0xb220x6db: v6dbb22(0x40) = CONST 
    0xb240x6db: v6dbb24 = MLOAD v6dbb22(0x40)
    0xb260x6db: v6dbb26 = ADD v6dbb04, v6dbb19
    0xb290x6db: v6dbb29(0x0) = CONST 
    0xb330x6db: v6dbb33 = SUB v6dbb26, v6dbb24
    0xb360x6db: v6dbb36 = GAS 
    0xb370x6db: v6dbb37 = DELEGATECALL v6dbb36, v6dbb15, v6dbb24, v6dbb33, v6dbb24, v6dbb29(0x0)
    0xb3b0x6db: v6dbb3b = RETURNDATASIZE 
    0xb3d0x6db: v6dbb3d(0x0) = CONST 
    0xb400x6db: v6dbb40 = EQ v6dbb3b, v6dbb3d(0x0)
    0xb410x6db: v6dbb41(0xb66) = CONST 
    0xb440x6db: JUMPI v6dbb41(0xb66), v6dbb40

    Begin block 0xb450x6db
    prev=[0xafe0x6db], succ=[0xb6b0x6db]
    =================================
    0xb450x6db: v6dbb45(0x40) = CONST 
    0xb470x6db: v6dbb47 = MLOAD v6dbb45(0x40)
    0xb4a0x6db: v6dbb4a(0x1f) = CONST 
    0xb4c0x6db: v6dbb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v6dbb4a(0x1f)
    0xb4d0x6db: v6dbb4d(0x3f) = CONST 
    0xb4f0x6db: v6dbb4f = RETURNDATASIZE 
    0xb500x6db: v6dbb50 = ADD v6dbb4f, v6dbb4d(0x3f)
    0xb510x6db: v6dbb51 = AND v6dbb50, v6dbb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x6db: v6dbb53 = ADD v6dbb47, v6dbb51
    0xb540x6db: v6dbb54(0x40) = CONST 
    0xb560x6db: MSTORE v6dbb54(0x40), v6dbb53
    0xb570x6db: v6dbb57 = RETURNDATASIZE 
    0xb590x6db: MSTORE v6dbb47, v6dbb57
    0xb5a0x6db: v6dbb5a = RETURNDATASIZE 
    0xb5b0x6db: v6dbb5b(0x0) = CONST 
    0xb5d0x6db: v6dbb5d(0x20) = CONST 
    0xb600x6db: v6dbb60 = ADD v6dbb47, v6dbb5d(0x20)
    0xb610x6db: RETURNDATACOPY v6dbb60, v6dbb5b(0x0), v6dbb5a
    0xb620x6db: v6dbb62(0xb6b) = CONST 
    0xb650x6db: JUMP v6dbb62(0xb6b)

    Begin block 0xb6b0x6db
    prev=[0xb450x6db, 0xb660x6db], succ=[0xb7f0x6db, 0x153c0x6db]
    =================================
    0xb700x6db: v6dbb70(0x40) = CONST 
    0xb720x6db: v6dbb72 = MLOAD v6dbb70(0x40)
    0xb730x6db: v6dbb73 = RETURNDATASIZE 
    0xb740x6db: v6dbb74(0x0) = CONST 
    0xb770x6db: RETURNDATACOPY v6dbb72, v6dbb74(0x0), v6dbb73
    0xb7a0x6db: v6dbb7a = ISZERO v6dbb37
    0xb7b0x6db: v6dbb7b(0x153c) = CONST 
    0xb7e0x6db: JUMPI v6dbb7b(0x153c), v6dbb7a

    Begin block 0xb7f0x6db
    prev=[0xb6b0x6db], succ=[]
    =================================
    0xb7f0x6db: v6dbb7f = RETURNDATASIZE 
    0xb810x6db: RETURN v6dbb72, v6dbb7f

    Begin block 0x153c0x6db
    prev=[0xb6b0x6db], succ=[]
    =================================
    0x153d0x6db: v6db153d = RETURNDATASIZE 
    0x153f0x6db: REVERT v6dbb72, v6db153d

    Begin block 0xb660x6db
    prev=[0xafe0x6db], succ=[0xb6b0x6db]
    =================================
    0xb670x6db: v6dbb67(0x60) = CONST 

}

function _setImplementation(address,bool,bytes)() public {
    Begin block 0x6f0
    prev=[], succ=[0x6f8, 0x6fc]
    =================================
    0x6f1: v6f1 = CALLVALUE 
    0x6f3: v6f3 = ISZERO v6f1
    0x6f4: v6f4(0x6fc) = CONST 
    0x6f7: JUMPI v6f4(0x6fc), v6f3

    Begin block 0x6f8
    prev=[0x6f0], succ=[]
    =================================
    0x6f8: v6f8(0x0) = CONST 
    0x6fb: REVERT v6f8(0x0), v6f8(0x0)

    Begin block 0x6fc
    prev=[0x6f0], succ=[0x70f, 0x713]
    =================================
    0x6fe: v6fe(0x1801) = CONST 
    0x701: v701(0x4) = CONST 
    0x704: v704 = CALLDATASIZE 
    0x705: v705 = SUB v704, v701(0x4)
    0x706: v706(0x60) = CONST 
    0x709: v709 = LT v705, v706(0x60)
    0x70a: v70a = ISZERO v709
    0x70b: v70b(0x713) = CONST 
    0x70e: JUMPI v70b(0x713), v70a

    Begin block 0x70f
    prev=[0x6fc], succ=[]
    =================================
    0x70f: v70f(0x0) = CONST 
    0x712: REVERT v70f(0x0), v70f(0x0)

    Begin block 0x713
    prev=[0x6fc], succ=[0x740, 0x744]
    =================================
    0x714: v714(0x1) = CONST 
    0x716: v716(0x1) = CONST 
    0x718: v718(0xa0) = CONST 
    0x71a: v71a(0x10000000000000000000000000000000000000000) = SHL v718(0xa0), v716(0x1)
    0x71b: v71b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71a(0x10000000000000000000000000000000000000000), v714(0x1)
    0x71d: v71d = CALLDATALOAD v701(0x4)
    0x71e: v71e = AND v71d, v71b(0xffffffffffffffffffffffffffffffffffffffff)
    0x720: v720(0x20) = CONST 
    0x723: v723(0x24) = ADD v701(0x4), v720(0x20)
    0x724: v724 = CALLDATALOAD v723(0x24)
    0x725: v725 = ISZERO v724
    0x726: v726 = ISZERO v725
    0x729: v729 = ADD v701(0x4), v705
    0x72b: v72b(0x60) = CONST 
    0x72e: v72e(0x64) = ADD v701(0x4), v72b(0x60)
    0x72f: v72f(0x40) = CONST 
    0x732: v732(0x44) = ADD v701(0x4), v72f(0x40)
    0x733: v733 = CALLDATALOAD v732(0x44)
    0x734: v734(0x1) = CONST 
    0x736: v736(0x20) = CONST 
    0x738: v738(0x100000000) = SHL v736(0x20), v734(0x1)
    0x73a: v73a = GT v733, v738(0x100000000)
    0x73b: v73b = ISZERO v73a
    0x73c: v73c(0x744) = CONST 
    0x73f: JUMPI v73c(0x744), v73b

    Begin block 0x740
    prev=[0x713], succ=[]
    =================================
    0x740: v740(0x0) = CONST 
    0x743: REVERT v740(0x0), v740(0x0)

    Begin block 0x744
    prev=[0x713], succ=[0x752, 0x756]
    =================================
    0x746: v746 = ADD v701(0x4), v733
    0x748: v748(0x20) = CONST 
    0x74b: v74b = ADD v746, v748(0x20)
    0x74c: v74c = GT v74b, v729
    0x74d: v74d = ISZERO v74c
    0x74e: v74e(0x756) = CONST 
    0x751: JUMPI v74e(0x756), v74d

    Begin block 0x752
    prev=[0x744], succ=[]
    =================================
    0x752: v752(0x0) = CONST 
    0x755: REVERT v752(0x0), v752(0x0)

    Begin block 0x756
    prev=[0x744], succ=[0x773, 0x777]
    =================================
    0x758: v758 = CALLDATALOAD v746
    0x75a: v75a(0x20) = CONST 
    0x75c: v75c = ADD v75a(0x20), v746
    0x75f: v75f(0x1) = CONST 
    0x762: v762 = MUL v758, v75f(0x1)
    0x764: v764 = ADD v75c, v762
    0x765: v765 = GT v764, v729
    0x766: v766(0x1) = CONST 
    0x768: v768(0x20) = CONST 
    0x76a: v76a(0x100000000) = SHL v768(0x20), v766(0x1)
    0x76c: v76c = GT v758, v76a(0x100000000)
    0x76d: v76d = OR v76c, v765
    0x76e: v76e = ISZERO v76d
    0x76f: v76f(0x777) = CONST 
    0x772: JUMPI v76f(0x777), v76e

    Begin block 0x773
    prev=[0x756], succ=[]
    =================================
    0x773: v773(0x0) = CONST 
    0x776: REVERT v773(0x0), v773(0x0)

    Begin block 0x777
    prev=[0x756], succ=[0xf2f]
    =================================
    0x77c: v77c(0x1f) = CONST 
    0x77e: v77e = ADD v77c(0x1f), v758
    0x77f: v77f(0x20) = CONST 
    0x783: v783 = DIV v77e, v77f(0x20)
    0x784: v784 = MUL v783, v77f(0x20)
    0x785: v785(0x20) = CONST 
    0x787: v787 = ADD v785(0x20), v784
    0x788: v788(0x40) = CONST 
    0x78a: v78a = MLOAD v788(0x40)
    0x78d: v78d = ADD v78a, v787
    0x78e: v78e(0x40) = CONST 
    0x790: MSTORE v78e(0x40), v78d
    0x798: MSTORE v78a, v758
    0x799: v799(0x20) = CONST 
    0x79b: v79b = ADD v799(0x20), v78a
    0x7a1: CALLDATACOPY v79b, v75c, v758
    0x7a2: v7a2(0x0) = CONST 
    0x7a5: v7a5 = ADD v79b, v758
    0x7a9: MSTORE v7a5, v7a2(0x0)
    0x7ae: v7ae(0xf2f) = CONST 
    0x7b7: JUMP v7ae(0xf2f)

    Begin block 0xf2f
    prev=[0x777], succ=[0xf47, 0xf7d]
    =================================
    0xf30: vf30(0x3) = CONST 
    0xf32: vf32 = SLOAD vf30(0x3)
    0xf33: vf33(0x100) = CONST 
    0xf37: vf37 = DIV vf32, vf33(0x100)
    0xf38: vf38(0x1) = CONST 
    0xf3a: vf3a(0x1) = CONST 
    0xf3c: vf3c(0xa0) = CONST 
    0xf3e: vf3e(0x10000000000000000000000000000000000000000) = SHL vf3c(0xa0), vf3a(0x1)
    0xf3f: vf3f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf3e(0x10000000000000000000000000000000000000000), vf38(0x1)
    0xf40: vf40 = AND vf3f(0xffffffffffffffffffffffffffffffffffffffff), vf37
    0xf41: vf41 = CALLER 
    0xf42: vf42 = EQ vf41, vf40
    0xf43: vf43(0xf7d) = CONST 
    0xf46: JUMPI vf43(0xf7d), vf42

    Begin block 0xf47
    prev=[0xf2f], succ=[]
    =================================
    0xf47: vf47(0x40) = CONST 
    0xf49: vf49 = MLOAD vf47(0x40)
    0xf4a: vf4a(0x461bcd) = CONST 
    0xf4e: vf4e(0xe5) = CONST 
    0xf50: vf50(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf4e(0xe5), vf4a(0x461bcd)
    0xf52: MSTORE vf49, vf50(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf53: vf53(0x4) = CONST 
    0xf55: vf55 = ADD vf53(0x4), vf49
    0xf58: vf58(0x20) = CONST 
    0xf5a: vf5a = ADD vf58(0x20), vf55
    0xf5d: vf5d(0x20) = SUB vf5a, vf55
    0xf5f: MSTORE vf55, vf5d(0x20)
    0xf60: vf60(0x35) = CONST 
    0xf63: MSTORE vf5a, vf60(0x35)
    0xf64: vf64(0x20) = CONST 
    0xf66: vf66 = ADD vf64(0x20), vf5a
    0xf68: vf68(0x1445) = CONST 
    0xf6b: vf6b(0x35) = CONST 
    0xf6e: CODECOPY vf66, vf68(0x1445), vf6b(0x35)
    0xf6f: vf6f(0x40) = CONST 
    0xf71: vf71 = ADD vf6f(0x40), vf66
    0xf75: vf75(0x40) = CONST 
    0xf77: vf77 = MLOAD vf75(0x40)
    0xf7a: vf7a(0x84) = SUB vf71, vf77
    0xf7c: REVERT vf77, vf7a(0x84)

    Begin block 0xf7d
    prev=[0xf2f], succ=[0xf84, 0xfb7]
    =================================
    0xf7f: vf7f = ISZERO v726
    0xf80: vf80(0xfb7) = CONST 
    0xf83: JUMPI vf80(0xfb7), vf7f

    Begin block 0xf84
    prev=[0xf7d], succ=[0xc13B0xf84]
    =================================
    0xf84: vf84(0x40) = CONST 
    0xf87: vf87 = MLOAD vf84(0x40)
    0xf88: vf88(0x4) = CONST 
    0xf8b: MSTORE vf87, vf88(0x4)
    0xf8c: vf8c(0x24) = CONST 
    0xf8f: vf8f = ADD vf87, vf8c(0x24)
    0xf92: MSTORE vf84(0x40), vf8f
    0xf93: vf93(0x20) = CONST 
    0xf96: vf96 = ADD vf87, vf93(0x20)
    0xf98: vf98 = MLOAD vf96
    0xf99: vf99(0x1) = CONST 
    0xf9b: vf9b(0x1) = CONST 
    0xf9d: vf9d(0xe0) = CONST 
    0xf9f: vf9f(0x100000000000000000000000000000000000000000000000000000000) = SHL vf9d(0xe0), vf9b(0x1)
    0xfa0: vfa0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vf9f(0x100000000000000000000000000000000000000000000000000000000), vf99(0x1)
    0xfa1: vfa1 = AND vfa0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vf98
    0xfa2: vfa2(0x153ab505) = CONST 
    0xfa7: vfa7(0xe0) = CONST 
    0xfa9: vfa9(0x153ab50500000000000000000000000000000000000000000000000000000000) = SHL vfa7(0xe0), vfa2(0x153ab505)
    0xfaa: vfaa = OR vfa9(0x153ab50500000000000000000000000000000000000000000000000000000000), vfa1
    0xfac: MSTORE vf96, vfaa
    0xfad: vfad(0xfb5) = CONST 
    0xfb1: vfb1(0xc13) = CONST 
    0xfb4: JUMP vfb1(0xc13)

    Begin block 0xc13B0xf84
    prev=[0xf84], succ=[0xc2c0xc13B0xf84]
    =================================
    0xc14S0xf84: vc14Vf84(0x12) = CONST 
    0xc16S0xf84: vc16Vf84 = SLOAD vc14Vf84(0x12)
    0xc17S0xf84: vc17Vf84(0x60) = CONST 
    0xc1aS0xf84: vc1aVf84(0xc2c) = CONST 
    0xc1eS0xf84: vc1eVf84(0x1) = CONST 
    0xc20S0xf84: vc20Vf84(0x1) = CONST 
    0xc22S0xf84: vc22Vf84(0xa0) = CONST 
    0xc24S0xf84: vc24Vf84(0x10000000000000000000000000000000000000000) = SHL vc22Vf84(0xa0), vc20Vf84(0x1)
    0xc25S0xf84: vc25Vf84(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc24Vf84(0x10000000000000000000000000000000000000000), vc1eVf84(0x1)
    0xc26S0xf84: vc26Vf84 = AND vc25Vf84(0xffffffffffffffffffffffffffffffffffffffff), vc16Vf84
    0xc28S0xf84: vc28Vf84(0x121c) = CONST 
    0xc2bS0xf84: vc2b_0Vf84 = CALLPRIVATE vc28Vf84(0x121c), vf87, vc26Vf84, vc1aVf84(0xc2c)

    Begin block 0xc2c0xc13B0xf84
    prev=[0xc13B0xf84], succ=[0xfb5]
    =================================
    0xc310xc13S0xf84: JUMP vfad(0xfb5)

    Begin block 0xfb5
    prev=[0xc2c0xc13B0xf84], succ=[0xfb7]
    =================================

    Begin block 0xfb7
    prev=[0xf7d, 0xfb5], succ=[0x1009]
    =================================
    0xfb8: vfb8(0x12) = CONST 
    0xfbb: vfbb = SLOAD vfb8(0x12)
    0xfbc: vfbc(0x1) = CONST 
    0xfbe: vfbe(0x1) = CONST 
    0xfc0: vfc0(0xa0) = CONST 
    0xfc2: vfc2(0x10000000000000000000000000000000000000000) = SHL vfc0(0xa0), vfbe(0x1)
    0xfc3: vfc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfc2(0x10000000000000000000000000000000000000000), vfbc(0x1)
    0xfc6: vfc6 = AND vfc3(0xffffffffffffffffffffffffffffffffffffffff), v71e
    0xfc7: vfc7(0x1) = CONST 
    0xfc9: vfc9(0x1) = CONST 
    0xfcb: vfcb(0xa0) = CONST 
    0xfcd: vfcd(0x10000000000000000000000000000000000000000) = SHL vfcb(0xa0), vfc9(0x1)
    0xfce: vfce(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfcd(0x10000000000000000000000000000000000000000), vfc7(0x1)
    0xfcf: vfcf(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vfce(0xffffffffffffffffffffffffffffffffffffffff)
    0xfd1: vfd1 = AND vfbb, vfcf(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0xfd2: vfd2 = OR vfd1, vfc6
    0xfd5: SSTORE vfb8(0x12), vfd2
    0xfd6: vfd6(0x40) = CONST 
    0xfd8: vfd8 = MLOAD vfd6(0x40)
    0xfd9: vfd9(0x20) = CONST 
    0xfdb: vfdb(0x24) = CONST 
    0xfde: vfde = ADD vfd8, vfdb(0x24)
    0xfe1: MSTORE vfde, vfd9(0x20)
    0xfe3: vfe3 = MLOAD v78a
    0xfe4: vfe4(0x44) = CONST 
    0xfe7: vfe7 = ADD vfd8, vfe4(0x44)
    0xfe8: MSTORE vfe7, vfe3
    0xfea: vfea = MLOAD v78a
    0xfee: vfee = AND vfbb, vfc3(0xffffffffffffffffffffffffffffffffffffffff)
    0xff0: vff0(0x1083) = CONST 
    0xffa: vffa(0x64) = CONST 
    0xffe: vffe = ADD vfd8, vffa(0x64)
    0x1002: v1002 = ADD v78a, vfd9(0x20)
    0x1007: v1007(0x0) = CONST 

    Begin block 0x1009
    prev=[0xfb7, 0x1012], succ=[0x1021, 0x1012]
    =================================
    0x1009_0x0: v1009_0 = PHI v1007(0x0), v101c
    0x100c: v100c = LT v1009_0, vfea
    0x100d: v100d = ISZERO v100c
    0x100e: v100e(0x1021) = CONST 
    0x1011: JUMPI v100e(0x1021), v100d

    Begin block 0x1021
    prev=[0x1009], succ=[0x104e, 0x1035]
    =================================
    0x102a: v102a = ADD vfea, vffe
    0x102c: v102c(0x1f) = CONST 
    0x102e: v102e = AND v102c(0x1f), vfea
    0x1030: v1030 = ISZERO v102e
    0x1031: v1031(0x104e) = CONST 
    0x1034: JUMPI v1031(0x104e), v1030

    Begin block 0x104e
    prev=[0x1021, 0x1035], succ=[0xc130x6f0]
    =================================
    0x104e_0x1: v104e_1 = PHI v102a, v104b
    0x1050: v1050(0x40) = CONST 
    0x1053: v1053 = MLOAD v1050(0x40)
    0x1054: v1054(0x1f) = CONST 
    0x1056: v1056(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1054(0x1f)
    0x1059: v1059 = SUB v104e_1, v1053
    0x105a: v105a = ADD v1059, v1056(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x105c: MSTORE v1053, v105a
    0x105f: MSTORE v1050(0x40), v104e_1
    0x1060: v1060(0x20) = CONST 
    0x1063: v1063 = ADD v1053, v1060(0x20)
    0x1065: v1065 = MLOAD v1063
    0x1066: v1066(0x1) = CONST 
    0x1068: v1068(0x1) = CONST 
    0x106a: v106a(0xe0) = CONST 
    0x106c: v106c(0x100000000000000000000000000000000000000000000000000000000) = SHL v106a(0xe0), v1068(0x1)
    0x106d: v106d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v106c(0x100000000000000000000000000000000000000000000000000000000), v1066(0x1)
    0x106e: v106e = AND v106d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1065
    0x106f: v106f(0xadccee5) = CONST 
    0x1074: v1074(0xe3) = CONST 
    0x1076: v1076(0x56e6772800000000000000000000000000000000000000000000000000000000) = SHL v1074(0xe3), v106f(0xadccee5)
    0x1077: v1077 = OR v1076(0x56e6772800000000000000000000000000000000000000000000000000000000), v106e
    0x1079: MSTORE v1063, v1077
    0x107c: v107c(0xc13) = CONST 
    0x1082: JUMP v107c(0xc13)

    Begin block 0xc130x6f0
    prev=[0x104e], succ=[0xc2c0x6f0]
    =================================
    0xc140x6f0: v6f0c14(0x12) = CONST 
    0xc160x6f0: v6f0c16 = SLOAD v6f0c14(0x12)
    0xc170x6f0: v6f0c17(0x60) = CONST 
    0xc1a0x6f0: v6f0c1a(0xc2c) = CONST 
    0xc1e0x6f0: v6f0c1e(0x1) = CONST 
    0xc200x6f0: v6f0c20(0x1) = CONST 
    0xc220x6f0: v6f0c22(0xa0) = CONST 
    0xc240x6f0: v6f0c24(0x10000000000000000000000000000000000000000) = SHL v6f0c22(0xa0), v6f0c20(0x1)
    0xc250x6f0: v6f0c25(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6f0c24(0x10000000000000000000000000000000000000000), v6f0c1e(0x1)
    0xc260x6f0: v6f0c26 = AND v6f0c25(0xffffffffffffffffffffffffffffffffffffffff), v6f0c16
    0xc280x6f0: v6f0c28(0x121c) = CONST 
    0xc2b0x6f0: v6f0c2b_0 = CALLPRIVATE v6f0c28(0x121c), v1053, v6f0c26, v6f0c1a(0xc2c)

    Begin block 0xc2c0x6f0
    prev=[0xc130x6f0], succ=[0x1083]
    =================================
    0xc310x6f0: JUMP vff0(0x1083)

    Begin block 0x1083
    prev=[0xc2c0x6f0], succ=[0x1801]
    =================================
    0x1085: v1085(0x12) = CONST 
    0x1087: v1087 = SLOAD v1085(0x12)
    0x1088: v1088(0x40) = CONST 
    0x108b: v108b = MLOAD v1088(0x40)
    0x108c: v108c(0x1) = CONST 
    0x108e: v108e(0x1) = CONST 
    0x1090: v1090(0xa0) = CONST 
    0x1092: v1092(0x10000000000000000000000000000000000000000) = SHL v1090(0xa0), v108e(0x1)
    0x1093: v1093(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1092(0x10000000000000000000000000000000000000000), v108c(0x1)
    0x1096: v1096 = AND vfee, v1093(0xffffffffffffffffffffffffffffffffffffffff)
    0x1098: MSTORE v108b, v1096
    0x109b: v109b = AND v1087, v1093(0xffffffffffffffffffffffffffffffffffffffff)
    0x109c: v109c(0x20) = CONST 
    0x109f: v109f = ADD v108b, v109c(0x20)
    0x10a0: MSTORE v109f, v109b
    0x10a2: v10a2 = MLOAD v1088(0x40)
    0x10a3: v10a3(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x10c7: v10c7(0x0) = SUB v108b, v10a2
    0x10ca: v10ca(0x40) = ADD v1088(0x40), v10c7(0x0)
    0x10cc: LOG1 v10a2, v10ca(0x40), v10a3(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x10d1: JUMP v6fe(0x1801)

    Begin block 0x1801
    prev=[0x1083], succ=[]
    =================================
    0x1802: STOP 

    Begin block 0x1035
    prev=[0x1021], succ=[0x104e]
    =================================
    0x1037: v1037 = SUB v102a, v102e
    0x1039: v1039 = MLOAD v1037
    0x103a: v103a(0x1) = CONST 
    0x103d: v103d(0x20) = CONST 
    0x103f: v103f = SUB v103d(0x20), v102e
    0x1040: v1040(0x100) = CONST 
    0x1043: v1043 = EXP v1040(0x100), v103f
    0x1044: v1044 = SUB v1043, v103a(0x1)
    0x1045: v1045 = NOT v1044
    0x1046: v1046 = AND v1045, v1039
    0x1048: MSTORE v1037, v1046
    0x1049: v1049(0x20) = CONST 
    0x104b: v104b = ADD v1049(0x20), v1037

    Begin block 0x1012
    prev=[0x1009], succ=[0x1009]
    =================================
    0x1012_0x0: v1012_0 = PHI v1007(0x0), v101c
    0x1014: v1014 = ADD v1012_0, v1002
    0x1015: v1015 = MLOAD v1014
    0x1018: v1018 = ADD v1012_0, vffe
    0x1019: MSTORE v1018, v1015
    0x101a: v101a(0x20) = CONST 
    0x101c: v101c = ADD v101a(0x20), v1012_0
    0x101d: v101d(0x1009) = CONST 
    0x1020: JUMP v101d(0x1009)

}

function delegates(address)() public {
    Begin block 0x7b8
    prev=[], succ=[0x7c0, 0x7c4]
    =================================
    0x7b9: v7b9 = CALLVALUE 
    0x7bb: v7bb = ISZERO v7b9
    0x7bc: v7bc(0x7c4) = CONST 
    0x7bf: JUMPI v7bc(0x7c4), v7bb

    Begin block 0x7c0
    prev=[0x7b8], succ=[]
    =================================
    0x7c0: v7c0(0x0) = CONST 
    0x7c3: REVERT v7c0(0x0), v7c0(0x0)

    Begin block 0x7c4
    prev=[0x7b8], succ=[0x7d7, 0x5e50x7b8]
    =================================
    0x7c6: v7c6(0x1822) = CONST 
    0x7c9: v7c9(0x4) = CONST 
    0x7cc: v7cc = CALLDATASIZE 
    0x7cd: v7cd = SUB v7cc, v7c9(0x4)
    0x7ce: v7ce(0x20) = CONST 
    0x7d1: v7d1 = LT v7cd, v7ce(0x20)
    0x7d2: v7d2 = ISZERO v7d1
    0x7d3: v7d3(0x5e5) = CONST 
    0x7d6: JUMPI v7d3(0x5e5), v7d2

    Begin block 0x7d7
    prev=[0x7c4], succ=[]
    =================================
    0x7d7: v7d7(0x0) = CONST 
    0x7da: REVERT v7d7(0x0), v7d7(0x0)

    Begin block 0x5e50x7b8
    prev=[0x7c4], succ=[0xce90x7b8]
    =================================
    0x5e70x7b8: v7b85e7 = CALLDATALOAD v7c9(0x4)
    0x5e80x7b8: v7b85e8(0x1) = CONST 
    0x5ea0x7b8: v7b85ea(0x1) = CONST 
    0x5ec0x7b8: v7b85ec(0xa0) = CONST 
    0x5ee0x7b8: v7b85ee(0x10000000000000000000000000000000000000000) = SHL v7b85ec(0xa0), v7b85ea(0x1)
    0x5ef0x7b8: v7b85ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b85ee(0x10000000000000000000000000000000000000000), v7b85e8(0x1)
    0x5f00x7b8: v7b85f0 = AND v7b85ef(0xffffffffffffffffffffffffffffffffffffffff), v7b85e7
    0x5f10x7b8: v7b85f1(0xce9) = CONST 
    0x5f40x7b8: JUMP v7b85f1(0xce9)

    Begin block 0xce90x7b8
    prev=[0x5e50x7b8], succ=[0x12de0x7b8]
    =================================
    0xcea0x7b8: v7b8cea(0x0) = CONST 
    0xcec0x7b8: v7b8cec(0xcf3) = CONST 
    0xcef0x7b8: v7b8cef(0x12de) = CONST 
    0xcf20x7b8: JUMP v7b8cef(0x12de)

    Begin block 0x12de0x7b8
    prev=[0xce90x7b8], succ=[0x13600x7b8]
    =================================
    0x12df0x7b8: v7b812df(0x60) = CONST 
    0x12e10x7b8: v7b812e1(0x0) = CONST 
    0x12e30x7b8: v7b812e3 = ADDRESS 
    0x12e40x7b8: v7b812e4(0x1) = CONST 
    0x12e60x7b8: v7b812e6(0x1) = CONST 
    0x12e80x7b8: v7b812e8(0xa0) = CONST 
    0x12ea0x7b8: v7b812ea(0x10000000000000000000000000000000000000000) = SHL v7b812e8(0xa0), v7b812e6(0x1)
    0x12eb0x7b8: v7b812eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b812ea(0x10000000000000000000000000000000000000000), v7b812e4(0x1)
    0x12ec0x7b8: v7b812ec = AND v7b812eb(0xffffffffffffffffffffffffffffffffffffffff), v7b812e3
    0x12ed0x7b8: v7b812ed(0x0) = CONST 
    0x12ef0x7b8: v7b812ef = CALLDATASIZE 
    0x12f00x7b8: v7b812f0(0x40) = CONST 
    0x12f20x7b8: v7b812f2 = MLOAD v7b812f0(0x40)
    0x12f30x7b8: v7b812f3(0x24) = CONST 
    0x12f50x7b8: v7b812f5 = ADD v7b812f3(0x24), v7b812f2
    0x12f80x7b8: v7b812f8(0x20) = CONST 
    0x12fa0x7b8: v7b812fa = ADD v7b812f8(0x20), v7b812f5
    0x12fd0x7b8: v7b812fd(0x20) = SUB v7b812fa, v7b812f5
    0x12ff0x7b8: MSTORE v7b812f5, v7b812fd(0x20)
    0x13050x7b8: MSTORE v7b812fa, v7b812ef
    0x13060x7b8: v7b81306(0x20) = CONST 
    0x13080x7b8: v7b81308 = ADD v7b81306(0x20), v7b812fa
    0x130e0x7b8: CALLDATACOPY v7b81308, v7b812ed(0x0), v7b812ef
    0x130f0x7b8: v7b8130f(0x0) = CONST 
    0x13130x7b8: v7b81313 = ADD v7b812ef, v7b81308
    0x13140x7b8: MSTORE v7b81313, v7b8130f(0x0)
    0x13150x7b8: v7b81315(0x40) = CONST 
    0x13180x7b8: v7b81318 = MLOAD v7b81315(0x40)
    0x13190x7b8: v7b81319(0x1f) = CONST 
    0x131d0x7b8: v7b8131d = ADD v7b812ef, v7b81319(0x1f)
    0x131e0x7b8: v7b8131e(0x1f) = CONST 
    0x13200x7b8: v7b81320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v7b8131e(0x1f)
    0x13230x7b8: v7b81323 = AND v7b81320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v7b8131d
    0x13260x7b8: v7b81326 = ADD v7b81308, v7b81323
    0x13290x7b8: v7b81329 = SUB v7b81326, v7b81318
    0x132c0x7b8: v7b8132c = ADD v7b81320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v7b81329
    0x132e0x7b8: MSTORE v7b81318, v7b8132c
    0x13310x7b8: MSTORE v7b81315(0x40), v7b81326
    0x13320x7b8: v7b81332(0x20) = CONST 
    0x13350x7b8: v7b81335 = ADD v7b81318, v7b81332(0x20)
    0x13370x7b8: v7b81337 = MLOAD v7b81335
    0x13380x7b8: v7b81338(0x1) = CONST 
    0x133a0x7b8: v7b8133a(0x1) = CONST 
    0x133c0x7b8: v7b8133c(0xe0) = CONST 
    0x133e0x7b8: v7b8133e(0x100000000000000000000000000000000000000000000000000000000) = SHL v7b8133c(0xe0), v7b8133a(0x1)
    0x133f0x7b8: v7b8133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v7b8133e(0x100000000000000000000000000000000000000000000000000000000), v7b81338(0x1)
    0x13400x7b8: v7b81340 = AND v7b8133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v7b81337
    0x13410x7b8: v7b81341(0x933c1ed) = CONST 
    0x13460x7b8: v7b81346(0xe0) = CONST 
    0x13480x7b8: v7b81348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v7b81346(0xe0), v7b81341(0x933c1ed)
    0x13490x7b8: v7b81349 = OR v7b81348(0x933c1ed00000000000000000000000000000000000000000000000000000000), v7b81340
    0x134b0x7b8: MSTORE v7b81335, v7b81349
    0x134d0x7b8: v7b8134d = MLOAD v7b81315(0x40)
    0x134f0x7b8: v7b8134f = MLOAD v7b81318

    Begin block 0x13600x7b8
    prev=[0x13690x7b8, 0x12de0x7b8], succ=[0x137f0x7b8, 0x13690x7b8]
    =================================
    0x13600x7b8_0x2: v13607b8_2 = PHI v7b81372, v7b8134f
    0x13610x7b8: v7b81361(0x20) = CONST 
    0x13640x7b8: v7b81364 = LT v13607b8_2, v7b81361(0x20)
    0x13650x7b8: v7b81365(0x137f) = CONST 
    0x13680x7b8: JUMPI v7b81365(0x137f), v7b81364

    Begin block 0x137f0x7b8
    prev=[0x13600x7b8], succ=[0x13be0x7b8, 0x13df0x7b8]
    =================================
    0x137f0x7b8_0x0: v137f7b8_0 = PHI v7b8137a, v7b81335
    0x137f0x7b8_0x1: v137f7b8_1 = PHI v7b81378, v7b8134d
    0x137f0x7b8_0x2: v137f7b8_2 = PHI v7b81372, v7b8134f
    0x13800x7b8: v7b81380(0x1) = CONST 
    0x13830x7b8: v7b81383(0x20) = CONST 
    0x13850x7b8: v7b81385 = SUB v7b81383(0x20), v137f7b8_2
    0x13860x7b8: v7b81386(0x100) = CONST 
    0x13890x7b8: v7b81389 = EXP v7b81386(0x100), v7b81385
    0x138a0x7b8: v7b8138a = SUB v7b81389, v7b81380(0x1)
    0x138c0x7b8: v7b8138c = NOT v7b8138a
    0x138e0x7b8: v7b8138e = MLOAD v137f7b8_0
    0x138f0x7b8: v7b8138f = AND v7b8138e, v7b8138c
    0x13920x7b8: v7b81392 = MLOAD v137f7b8_1
    0x13930x7b8: v7b81393 = AND v7b81392, v7b8138a
    0x13960x7b8: v7b81396 = OR v7b8138f, v7b81393
    0x13980x7b8: MSTORE v137f7b8_1, v7b81396
    0x13a10x7b8: v7b813a1 = ADD v7b8134f, v7b8134d
    0x13a50x7b8: v7b813a5(0x0) = CONST 
    0x13a70x7b8: v7b813a7(0x40) = CONST 
    0x13a90x7b8: v7b813a9 = MLOAD v7b813a7(0x40)
    0x13ac0x7b8: v7b813ac = SUB v7b813a1, v7b813a9
    0x13af0x7b8: v7b813af = GAS 
    0x13b00x7b8: v7b813b0 = STATICCALL v7b813af, v7b812ec, v7b813a9, v7b813ac, v7b813a9, v7b813a5(0x0)
    0x13b40x7b8: v7b813b4 = RETURNDATASIZE 
    0x13b60x7b8: v7b813b6(0x0) = CONST 
    0x13b90x7b8: v7b813b9 = EQ v7b813b4, v7b813b6(0x0)
    0x13ba0x7b8: v7b813ba(0x13df) = CONST 
    0x13bd0x7b8: JUMPI v7b813ba(0x13df), v7b813b9

    Begin block 0x13be0x7b8
    prev=[0x137f0x7b8], succ=[0x13e40x7b8]
    =================================
    0x13be0x7b8: v7b813be(0x40) = CONST 
    0x13c00x7b8: v7b813c0 = MLOAD v7b813be(0x40)
    0x13c30x7b8: v7b813c3(0x1f) = CONST 
    0x13c50x7b8: v7b813c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v7b813c3(0x1f)
    0x13c60x7b8: v7b813c6(0x3f) = CONST 
    0x13c80x7b8: v7b813c8 = RETURNDATASIZE 
    0x13c90x7b8: v7b813c9 = ADD v7b813c8, v7b813c6(0x3f)
    0x13ca0x7b8: v7b813ca = AND v7b813c9, v7b813c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0x7b8: v7b813cc = ADD v7b813c0, v7b813ca
    0x13cd0x7b8: v7b813cd(0x40) = CONST 
    0x13cf0x7b8: MSTORE v7b813cd(0x40), v7b813cc
    0x13d00x7b8: v7b813d0 = RETURNDATASIZE 
    0x13d20x7b8: MSTORE v7b813c0, v7b813d0
    0x13d30x7b8: v7b813d3 = RETURNDATASIZE 
    0x13d40x7b8: v7b813d4(0x0) = CONST 
    0x13d60x7b8: v7b813d6(0x20) = CONST 
    0x13d90x7b8: v7b813d9 = ADD v7b813c0, v7b813d6(0x20)
    0x13da0x7b8: RETURNDATACOPY v7b813d9, v7b813d4(0x0), v7b813d3
    0x13db0x7b8: v7b813db(0x13e4) = CONST 
    0x13de0x7b8: JUMP v7b813db(0x13e4)

    Begin block 0x13e40x7b8
    prev=[0x13be0x7b8, 0x13df0x7b8], succ=[0x13f80x7b8, 0x155f0x7b8]
    =================================
    0x13e90x7b8: v7b813e9(0x40) = CONST 
    0x13eb0x7b8: v7b813eb = MLOAD v7b813e9(0x40)
    0x13ec0x7b8: v7b813ec = RETURNDATASIZE 
    0x13ed0x7b8: v7b813ed(0x0) = CONST 
    0x13f00x7b8: RETURNDATACOPY v7b813eb, v7b813ed(0x0), v7b813ec
    0x13f30x7b8: v7b813f3 = ISZERO v7b813b0
    0x13f40x7b8: v7b813f4(0x155f) = CONST 
    0x13f70x7b8: JUMPI v7b813f4(0x155f), v7b813f3

    Begin block 0x13f80x7b8
    prev=[0x13e40x7b8], succ=[]
    =================================
    0x13f80x7b8: v7b813f8(0x40) = CONST 
    0x13fa0x7b8: v7b813fa = RETURNDATASIZE 
    0x13fb0x7b8: v7b813fb = SUB v7b813fa, v7b813f8(0x40)
    0x13fc0x7b8: v7b813fc(0x40) = CONST 
    0x13ff0x7b8: v7b813ff = ADD v7b813eb, v7b813fc(0x40)
    0x14000x7b8: RETURN v7b813ff, v7b813fb

    Begin block 0x155f0x7b8
    prev=[0x13e40x7b8], succ=[]
    =================================
    0x15600x7b8: v7b81560 = RETURNDATASIZE 
    0x15620x7b8: REVERT v7b813eb, v7b81560

    Begin block 0x13df0x7b8
    prev=[0x137f0x7b8], succ=[0x13e40x7b8]
    =================================
    0x13e00x7b8: v7b813e0(0x60) = CONST 

    Begin block 0x13690x7b8
    prev=[0x13600x7b8], succ=[0x13600x7b8]
    =================================
    0x13690x7b8_0x0: v13697b8_0 = PHI v7b8137a, v7b81335
    0x13690x7b8_0x1: v13697b8_1 = PHI v7b81378, v7b8134d
    0x13690x7b8_0x2: v13697b8_2 = PHI v7b81372, v7b8134f
    0x136a0x7b8: v7b8136a = MLOAD v13697b8_0
    0x136c0x7b8: MSTORE v13697b8_1, v7b8136a
    0x136d0x7b8: v7b8136d(0x1f) = CONST 
    0x136f0x7b8: v7b8136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v7b8136d(0x1f)
    0x13720x7b8: v7b81372 = ADD v13697b8_2, v7b8136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740x7b8: v7b81374(0x20) = CONST 
    0x13780x7b8: v7b81378 = ADD v7b81374(0x20), v13697b8_1
    0x137a0x7b8: v7b8137a = ADD v7b81374(0x20), v13697b8_0
    0x137b0x7b8: v7b8137b(0x1360) = CONST 
    0x137e0x7b8: JUMP v7b8137b(0x1360)

}

function implementation()() public {
    Begin block 0x7db
    prev=[], succ=[0x7e3, 0x7e7]
    =================================
    0x7dc: v7dc = CALLVALUE 
    0x7de: v7de = ISZERO v7dc
    0x7df: v7df(0x7e7) = CONST 
    0x7e2: JUMPI v7df(0x7e7), v7de

    Begin block 0x7e3
    prev=[0x7db], succ=[]
    =================================
    0x7e3: v7e3(0x0) = CONST 
    0x7e6: REVERT v7e3(0x0), v7e3(0x0)

    Begin block 0x7e7
    prev=[0x7db], succ=[0x10d2]
    =================================
    0x7e9: v7e9(0x185d) = CONST 
    0x7ec: v7ec(0x10d2) = CONST 
    0x7ef: JUMP v7ec(0x10d2)

    Begin block 0x10d2
    prev=[0x7e7], succ=[0x185d]
    =================================
    0x10d3: v10d3(0x12) = CONST 
    0x10d5: v10d5 = SLOAD v10d3(0x12)
    0x10d6: v10d6(0x1) = CONST 
    0x10d8: v10d8(0x1) = CONST 
    0x10da: v10da(0xa0) = CONST 
    0x10dc: v10dc(0x10000000000000000000000000000000000000000) = SHL v10da(0xa0), v10d8(0x1)
    0x10dd: v10dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10dc(0x10000000000000000000000000000000000000000), v10d6(0x1)
    0x10de: v10de = AND v10dd(0xffffffffffffffffffffffffffffffffffffffff), v10d5
    0x10e0: JUMP v7e9(0x185d)

    Begin block 0x185d
    prev=[0x10d2], succ=[]
    =================================
    0x185e: v185e(0x40) = CONST 
    0x1861: v1861 = MLOAD v185e(0x40)
    0x1862: v1862(0x1) = CONST 
    0x1864: v1864(0x1) = CONST 
    0x1866: v1866(0xa0) = CONST 
    0x1868: v1868(0x10000000000000000000000000000000000000000) = SHL v1866(0xa0), v1864(0x1)
    0x1869: v1869(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1868(0x10000000000000000000000000000000000000000), v1862(0x1)
    0x186c: v186c = AND v10de, v1869(0xffffffffffffffffffffffffffffffffffffffff)
    0x186e: MSTORE v1861, v186c
    0x186f: v186f = MLOAD v185e(0x40)
    0x1873: v1873(0x0) = SUB v1861, v186f
    0x1874: v1874(0x20) = CONST 
    0x1876: v1876(0x20) = ADD v1874(0x20), v1873(0x0)
    0x1878: RETURN v186f, v1876(0x20)

}

function internalDecimals()() public {
    Begin block 0x7f0
    prev=[], succ=[0x7f8, 0x7fc]
    =================================
    0x7f1: v7f1 = CALLVALUE 
    0x7f3: v7f3 = ISZERO v7f1
    0x7f4: v7f4(0x7fc) = CONST 
    0x7f7: JUMPI v7f4(0x7fc), v7f3

    Begin block 0x7f8
    prev=[0x7f0], succ=[]
    =================================
    0x7f8: v7f8(0x0) = CONST 
    0x7fb: REVERT v7f8(0x0), v7f8(0x0)

    Begin block 0x7fc
    prev=[0x7f0], succ=[0x10e1]
    =================================
    0x7fe: v7fe(0x1898) = CONST 
    0x801: v801(0x10e1) = CONST 
    0x804: JUMP v801(0x10e1)

    Begin block 0x10e1
    prev=[0x7fc], succ=[0x1898]
    =================================
    0x10e2: v10e2(0xd3c21bcecceda1000000) = CONST 
    0x10ee: JUMP v7fe(0x1898)

    Begin block 0x1898
    prev=[0x10e1], succ=[]
    =================================
    0x1899: v1899(0x40) = CONST 
    0x189c: v189c = MLOAD v1899(0x40)
    0x189f: MSTORE v189c, v10e2(0xd3c21bcecceda1000000)
    0x18a0: v18a0 = MLOAD v1899(0x40)
    0x18a4: v18a4(0x0) = SUB v189c, v18a0
    0x18a5: v18a5(0x20) = CONST 
    0x18a7: v18a7(0x20) = ADD v18a5(0x20), v18a4(0x0)
    0x18a9: RETURN v18a0, v18a7(0x20)

}

function incentivizer()() public {
    Begin block 0x805
    prev=[], succ=[0x80d, 0x811]
    =================================
    0x806: v806 = CALLVALUE 
    0x808: v808 = ISZERO v806
    0x809: v809(0x811) = CONST 
    0x80c: JUMPI v809(0x811), v808

    Begin block 0x80d
    prev=[0x805], succ=[]
    =================================
    0x80d: v80d(0x0) = CONST 
    0x810: REVERT v80d(0x0), v80d(0x0)

    Begin block 0x811
    prev=[0x805], succ=[0x10ef]
    =================================
    0x813: v813(0x18c9) = CONST 
    0x816: v816(0x10ef) = CONST 
    0x819: JUMP v816(0x10ef)

    Begin block 0x10ef
    prev=[0x811], succ=[0x18c9]
    =================================
    0x10f0: v10f0(0x7) = CONST 
    0x10f2: v10f2 = SLOAD v10f0(0x7)
    0x10f3: v10f3(0x1) = CONST 
    0x10f5: v10f5(0x1) = CONST 
    0x10f7: v10f7(0xa0) = CONST 
    0x10f9: v10f9(0x10000000000000000000000000000000000000000) = SHL v10f7(0xa0), v10f5(0x1)
    0x10fa: v10fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10f9(0x10000000000000000000000000000000000000000), v10f3(0x1)
    0x10fb: v10fb = AND v10fa(0xffffffffffffffffffffffffffffffffffffffff), v10f2
    0x10fd: JUMP v813(0x18c9)

    Begin block 0x18c9
    prev=[0x10ef], succ=[]
    =================================
    0x18ca: v18ca(0x40) = CONST 
    0x18cd: v18cd = MLOAD v18ca(0x40)
    0x18ce: v18ce(0x1) = CONST 
    0x18d0: v18d0(0x1) = CONST 
    0x18d2: v18d2(0xa0) = CONST 
    0x18d4: v18d4(0x10000000000000000000000000000000000000000) = SHL v18d2(0xa0), v18d0(0x1)
    0x18d5: v18d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18d4(0x10000000000000000000000000000000000000000), v18ce(0x1)
    0x18d8: v18d8 = AND v10fb, v18d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x18da: MSTORE v18cd, v18d8
    0x18db: v18db = MLOAD v18ca(0x40)
    0x18df: v18df(0x0) = SUB v18cd, v18db
    0x18e0: v18e0(0x20) = CONST 
    0x18e2: v18e2(0x20) = ADD v18e0(0x20), v18df(0x0)
    0x18e4: RETURN v18db, v18e2(0x20)

}

function numCheckpoints(address)() public {
    Begin block 0x81a
    prev=[], succ=[0x822, 0x826]
    =================================
    0x81b: v81b = CALLVALUE 
    0x81d: v81d = ISZERO v81b
    0x81e: v81e(0x826) = CONST 
    0x821: JUMPI v81e(0x826), v81d

    Begin block 0x822
    prev=[0x81a], succ=[]
    =================================
    0x822: v822(0x0) = CONST 
    0x825: REVERT v822(0x0), v822(0x0)

    Begin block 0x826
    prev=[0x81a], succ=[0x839, 0x83d]
    =================================
    0x828: v828(0x84d) = CONST 
    0x82b: v82b(0x4) = CONST 
    0x82e: v82e = CALLDATASIZE 
    0x82f: v82f = SUB v82e, v82b(0x4)
    0x830: v830(0x20) = CONST 
    0x833: v833 = LT v82f, v830(0x20)
    0x834: v834 = ISZERO v833
    0x835: v835(0x83d) = CONST 
    0x838: JUMPI v835(0x83d), v834

    Begin block 0x839
    prev=[0x826], succ=[]
    =================================
    0x839: v839(0x0) = CONST 
    0x83c: REVERT v839(0x0), v839(0x0)

    Begin block 0x83d
    prev=[0x826], succ=[0x10fe]
    =================================
    0x83f: v83f = CALLDATALOAD v82b(0x4)
    0x840: v840(0x1) = CONST 
    0x842: v842(0x1) = CONST 
    0x844: v844(0xa0) = CONST 
    0x846: v846(0x10000000000000000000000000000000000000000) = SHL v844(0xa0), v842(0x1)
    0x847: v847(0xffffffffffffffffffffffffffffffffffffffff) = SUB v846(0x10000000000000000000000000000000000000000), v840(0x1)
    0x848: v848 = AND v847(0xffffffffffffffffffffffffffffffffffffffff), v83f
    0x849: v849(0x10fe) = CONST 
    0x84c: JUMP v849(0x10fe)

    Begin block 0x10fe
    prev=[0x83d], succ=[0x84d]
    =================================
    0x10ff: v10ff(0x10) = CONST 
    0x1101: v1101(0x20) = CONST 
    0x1103: MSTORE v1101(0x20), v10ff(0x10)
    0x1104: v1104(0x0) = CONST 
    0x1108: MSTORE v1104(0x0), v848
    0x1109: v1109(0x40) = CONST 
    0x110c: v110c = SHA3 v1104(0x0), v1109(0x40)
    0x110d: v110d = SLOAD v110c
    0x110e: v110e(0xffffffff) = CONST 
    0x1113: v1113 = AND v110e(0xffffffff), v110d
    0x1115: JUMP v828(0x84d)

    Begin block 0x84d
    prev=[0x10fe], succ=[]
    =================================
    0x84e: v84e(0x40) = CONST 
    0x851: v851 = MLOAD v84e(0x40)
    0x852: v852(0xffffffff) = CONST 
    0x859: v859 = AND v1113, v852(0xffffffff)
    0x85b: MSTORE v851, v859
    0x85c: v85c = MLOAD v84e(0x40)
    0x860: v860(0x0) = SUB v851, v85c
    0x861: v861(0x20) = CONST 
    0x863: v863(0x20) = ADD v861(0x20), v860(0x0)
    0x865: RETURN v85c, v863(0x20)

}

function getPriorVotes(address,uint256)() public {
    Begin block 0x866
    prev=[], succ=[0x86e, 0x872]
    =================================
    0x867: v867 = CALLVALUE 
    0x869: v869 = ISZERO v867
    0x86a: v86a(0x872) = CONST 
    0x86d: JUMPI v86a(0x872), v869

    Begin block 0x86e
    prev=[0x866], succ=[]
    =================================
    0x86e: v86e(0x0) = CONST 
    0x871: REVERT v86e(0x0), v86e(0x0)

    Begin block 0x872
    prev=[0x866], succ=[0x885, 0x889]
    =================================
    0x874: v874(0x1904) = CONST 
    0x877: v877(0x4) = CONST 
    0x87a: v87a = CALLDATASIZE 
    0x87b: v87b = SUB v87a, v877(0x4)
    0x87c: v87c(0x40) = CONST 
    0x87f: v87f = LT v87b, v87c(0x40)
    0x880: v880 = ISZERO v87f
    0x881: v881(0x889) = CONST 
    0x884: JUMPI v881(0x889), v880

    Begin block 0x885
    prev=[0x872], succ=[]
    =================================
    0x885: v885(0x0) = CONST 
    0x888: REVERT v885(0x0), v885(0x0)

    Begin block 0x889
    prev=[0x872], succ=[0x11160x866]
    =================================
    0x88b: v88b(0x1) = CONST 
    0x88d: v88d(0x1) = CONST 
    0x88f: v88f(0xa0) = CONST 
    0x891: v891(0x10000000000000000000000000000000000000000) = SHL v88f(0xa0), v88d(0x1)
    0x892: v892(0xffffffffffffffffffffffffffffffffffffffff) = SUB v891(0x10000000000000000000000000000000000000000), v88b(0x1)
    0x894: v894 = CALLDATALOAD v877(0x4)
    0x895: v895 = AND v894, v892(0xffffffffffffffffffffffffffffffffffffffff)
    0x897: v897(0x20) = CONST 
    0x899: v899(0x24) = ADD v897(0x20), v877(0x4)
    0x89a: v89a = CALLDATALOAD v899(0x24)
    0x89b: v89b(0x1116) = CONST 
    0x89e: JUMP v89b(0x1116)

    Begin block 0x11160x866
    prev=[0x889], succ=[0x12de0x866]
    =================================
    0x11170x866: v8661117(0x0) = CONST 
    0x11190x866: v8661119(0x1bae) = CONST 
    0x111c0x866: v866111c(0x12de) = CONST 
    0x111f0x866: JUMP v866111c(0x12de)

    Begin block 0x12de0x866
    prev=[0x11160x866], succ=[0x13600x866]
    =================================
    0x12df0x866: v86612df(0x60) = CONST 
    0x12e10x866: v86612e1(0x0) = CONST 
    0x12e30x866: v86612e3 = ADDRESS 
    0x12e40x866: v86612e4(0x1) = CONST 
    0x12e60x866: v86612e6(0x1) = CONST 
    0x12e80x866: v86612e8(0xa0) = CONST 
    0x12ea0x866: v86612ea(0x10000000000000000000000000000000000000000) = SHL v86612e8(0xa0), v86612e6(0x1)
    0x12eb0x866: v86612eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86612ea(0x10000000000000000000000000000000000000000), v86612e4(0x1)
    0x12ec0x866: v86612ec = AND v86612eb(0xffffffffffffffffffffffffffffffffffffffff), v86612e3
    0x12ed0x866: v86612ed(0x0) = CONST 
    0x12ef0x866: v86612ef = CALLDATASIZE 
    0x12f00x866: v86612f0(0x40) = CONST 
    0x12f20x866: v86612f2 = MLOAD v86612f0(0x40)
    0x12f30x866: v86612f3(0x24) = CONST 
    0x12f50x866: v86612f5 = ADD v86612f3(0x24), v86612f2
    0x12f80x866: v86612f8(0x20) = CONST 
    0x12fa0x866: v86612fa = ADD v86612f8(0x20), v86612f5
    0x12fd0x866: v86612fd(0x20) = SUB v86612fa, v86612f5
    0x12ff0x866: MSTORE v86612f5, v86612fd(0x20)
    0x13050x866: MSTORE v86612fa, v86612ef
    0x13060x866: v8661306(0x20) = CONST 
    0x13080x866: v8661308 = ADD v8661306(0x20), v86612fa
    0x130e0x866: CALLDATACOPY v8661308, v86612ed(0x0), v86612ef
    0x130f0x866: v866130f(0x0) = CONST 
    0x13130x866: v8661313 = ADD v86612ef, v8661308
    0x13140x866: MSTORE v8661313, v866130f(0x0)
    0x13150x866: v8661315(0x40) = CONST 
    0x13180x866: v8661318 = MLOAD v8661315(0x40)
    0x13190x866: v8661319(0x1f) = CONST 
    0x131d0x866: v866131d = ADD v86612ef, v8661319(0x1f)
    0x131e0x866: v866131e(0x1f) = CONST 
    0x13200x866: v8661320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v866131e(0x1f)
    0x13230x866: v8661323 = AND v8661320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v866131d
    0x13260x866: v8661326 = ADD v8661308, v8661323
    0x13290x866: v8661329 = SUB v8661326, v8661318
    0x132c0x866: v866132c = ADD v8661320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v8661329
    0x132e0x866: MSTORE v8661318, v866132c
    0x13310x866: MSTORE v8661315(0x40), v8661326
    0x13320x866: v8661332(0x20) = CONST 
    0x13350x866: v8661335 = ADD v8661318, v8661332(0x20)
    0x13370x866: v8661337 = MLOAD v8661335
    0x13380x866: v8661338(0x1) = CONST 
    0x133a0x866: v866133a(0x1) = CONST 
    0x133c0x866: v866133c(0xe0) = CONST 
    0x133e0x866: v866133e(0x100000000000000000000000000000000000000000000000000000000) = SHL v866133c(0xe0), v866133a(0x1)
    0x133f0x866: v866133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v866133e(0x100000000000000000000000000000000000000000000000000000000), v8661338(0x1)
    0x13400x866: v8661340 = AND v866133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v8661337
    0x13410x866: v8661341(0x933c1ed) = CONST 
    0x13460x866: v8661346(0xe0) = CONST 
    0x13480x866: v8661348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v8661346(0xe0), v8661341(0x933c1ed)
    0x13490x866: v8661349 = OR v8661348(0x933c1ed00000000000000000000000000000000000000000000000000000000), v8661340
    0x134b0x866: MSTORE v8661335, v8661349
    0x134d0x866: v866134d = MLOAD v8661315(0x40)
    0x134f0x866: v866134f = MLOAD v8661318

    Begin block 0x13600x866
    prev=[0x13690x866, 0x12de0x866], succ=[0x137f0x866, 0x13690x866]
    =================================
    0x13600x866_0x2: v1360866_2 = PHI v8661372, v866134f
    0x13610x866: v8661361(0x20) = CONST 
    0x13640x866: v8661364 = LT v1360866_2, v8661361(0x20)
    0x13650x866: v8661365(0x137f) = CONST 
    0x13680x866: JUMPI v8661365(0x137f), v8661364

    Begin block 0x137f0x866
    prev=[0x13600x866], succ=[0x13be0x866, 0x13df0x866]
    =================================
    0x137f0x866_0x0: v137f866_0 = PHI v866137a, v8661335
    0x137f0x866_0x1: v137f866_1 = PHI v8661378, v866134d
    0x137f0x866_0x2: v137f866_2 = PHI v8661372, v866134f
    0x13800x866: v8661380(0x1) = CONST 
    0x13830x866: v8661383(0x20) = CONST 
    0x13850x866: v8661385 = SUB v8661383(0x20), v137f866_2
    0x13860x866: v8661386(0x100) = CONST 
    0x13890x866: v8661389 = EXP v8661386(0x100), v8661385
    0x138a0x866: v866138a = SUB v8661389, v8661380(0x1)
    0x138c0x866: v866138c = NOT v866138a
    0x138e0x866: v866138e = MLOAD v137f866_0
    0x138f0x866: v866138f = AND v866138e, v866138c
    0x13920x866: v8661392 = MLOAD v137f866_1
    0x13930x866: v8661393 = AND v8661392, v866138a
    0x13960x866: v8661396 = OR v866138f, v8661393
    0x13980x866: MSTORE v137f866_1, v8661396
    0x13a10x866: v86613a1 = ADD v866134f, v866134d
    0x13a50x866: v86613a5(0x0) = CONST 
    0x13a70x866: v86613a7(0x40) = CONST 
    0x13a90x866: v86613a9 = MLOAD v86613a7(0x40)
    0x13ac0x866: v86613ac = SUB v86613a1, v86613a9
    0x13af0x866: v86613af = GAS 
    0x13b00x866: v86613b0 = STATICCALL v86613af, v86612ec, v86613a9, v86613ac, v86613a9, v86613a5(0x0)
    0x13b40x866: v86613b4 = RETURNDATASIZE 
    0x13b60x866: v86613b6(0x0) = CONST 
    0x13b90x866: v86613b9 = EQ v86613b4, v86613b6(0x0)
    0x13ba0x866: v86613ba(0x13df) = CONST 
    0x13bd0x866: JUMPI v86613ba(0x13df), v86613b9

    Begin block 0x13be0x866
    prev=[0x137f0x866], succ=[0x13e40x866]
    =================================
    0x13be0x866: v86613be(0x40) = CONST 
    0x13c00x866: v86613c0 = MLOAD v86613be(0x40)
    0x13c30x866: v86613c3(0x1f) = CONST 
    0x13c50x866: v86613c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v86613c3(0x1f)
    0x13c60x866: v86613c6(0x3f) = CONST 
    0x13c80x866: v86613c8 = RETURNDATASIZE 
    0x13c90x866: v86613c9 = ADD v86613c8, v86613c6(0x3f)
    0x13ca0x866: v86613ca = AND v86613c9, v86613c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0x866: v86613cc = ADD v86613c0, v86613ca
    0x13cd0x866: v86613cd(0x40) = CONST 
    0x13cf0x866: MSTORE v86613cd(0x40), v86613cc
    0x13d00x866: v86613d0 = RETURNDATASIZE 
    0x13d20x866: MSTORE v86613c0, v86613d0
    0x13d30x866: v86613d3 = RETURNDATASIZE 
    0x13d40x866: v86613d4(0x0) = CONST 
    0x13d60x866: v86613d6(0x20) = CONST 
    0x13d90x866: v86613d9 = ADD v86613c0, v86613d6(0x20)
    0x13da0x866: RETURNDATACOPY v86613d9, v86613d4(0x0), v86613d3
    0x13db0x866: v86613db(0x13e4) = CONST 
    0x13de0x866: JUMP v86613db(0x13e4)

    Begin block 0x13e40x866
    prev=[0x13be0x866, 0x13df0x866], succ=[0x13f80x866, 0x155f0x866]
    =================================
    0x13e90x866: v86613e9(0x40) = CONST 
    0x13eb0x866: v86613eb = MLOAD v86613e9(0x40)
    0x13ec0x866: v86613ec = RETURNDATASIZE 
    0x13ed0x866: v86613ed(0x0) = CONST 
    0x13f00x866: RETURNDATACOPY v86613eb, v86613ed(0x0), v86613ec
    0x13f30x866: v86613f3 = ISZERO v86613b0
    0x13f40x866: v86613f4(0x155f) = CONST 
    0x13f70x866: JUMPI v86613f4(0x155f), v86613f3

    Begin block 0x13f80x866
    prev=[0x13e40x866], succ=[]
    =================================
    0x13f80x866: v86613f8(0x40) = CONST 
    0x13fa0x866: v86613fa = RETURNDATASIZE 
    0x13fb0x866: v86613fb = SUB v86613fa, v86613f8(0x40)
    0x13fc0x866: v86613fc(0x40) = CONST 
    0x13ff0x866: v86613ff = ADD v86613eb, v86613fc(0x40)
    0x14000x866: RETURN v86613ff, v86613fb

    Begin block 0x155f0x866
    prev=[0x13e40x866], succ=[]
    =================================
    0x15600x866: v8661560 = RETURNDATASIZE 
    0x15620x866: REVERT v86613eb, v8661560

    Begin block 0x13df0x866
    prev=[0x137f0x866], succ=[0x13e40x866]
    =================================
    0x13e00x866: v86613e0(0x60) = CONST 

    Begin block 0x13690x866
    prev=[0x13600x866], succ=[0x13600x866]
    =================================
    0x13690x866_0x0: v1369866_0 = PHI v866137a, v8661335
    0x13690x866_0x1: v1369866_1 = PHI v8661378, v866134d
    0x13690x866_0x2: v1369866_2 = PHI v8661372, v866134f
    0x136a0x866: v866136a = MLOAD v1369866_0
    0x136c0x866: MSTORE v1369866_1, v866136a
    0x136d0x866: v866136d(0x1f) = CONST 
    0x136f0x866: v866136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v866136d(0x1f)
    0x13720x866: v8661372 = ADD v1369866_2, v866136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740x866: v8661374(0x20) = CONST 
    0x13780x866: v8661378 = ADD v8661374(0x20), v1369866_1
    0x137a0x866: v866137a = ADD v8661374(0x20), v1369866_0
    0x137b0x866: v866137b(0x1360) = CONST 
    0x137e0x866: JUMP v866137b(0x1360)

}

function rebase(uint256,uint256,bool)() public {
    Begin block 0x89f
    prev=[], succ=[0x8a7, 0x8ab]
    =================================
    0x8a0: v8a0 = CALLVALUE 
    0x8a2: v8a2 = ISZERO v8a0
    0x8a3: v8a3(0x8ab) = CONST 
    0x8a6: JUMPI v8a3(0x8ab), v8a2

    Begin block 0x8a7
    prev=[0x89f], succ=[]
    =================================
    0x8a7: v8a7(0x0) = CONST 
    0x8aa: REVERT v8a7(0x0), v8a7(0x0)

    Begin block 0x8ab
    prev=[0x89f], succ=[0x8be, 0x8c2]
    =================================
    0x8ad: v8ad(0x1935) = CONST 
    0x8b0: v8b0(0x4) = CONST 
    0x8b3: v8b3 = CALLDATASIZE 
    0x8b4: v8b4 = SUB v8b3, v8b0(0x4)
    0x8b5: v8b5(0x60) = CONST 
    0x8b8: v8b8 = LT v8b4, v8b5(0x60)
    0x8b9: v8b9 = ISZERO v8b8
    0x8ba: v8ba(0x8c2) = CONST 
    0x8bd: JUMPI v8ba(0x8c2), v8b9

    Begin block 0x8be
    prev=[0x8ab], succ=[]
    =================================
    0x8be: v8be(0x0) = CONST 
    0x8c1: REVERT v8be(0x0), v8be(0x0)

    Begin block 0x8c2
    prev=[0x8ab], succ=[0xc950x89f]
    =================================
    0x8c5: v8c5 = CALLDATALOAD v8b0(0x4)
    0x8c7: v8c7(0x20) = CONST 
    0x8ca: v8ca(0x24) = ADD v8b0(0x4), v8c7(0x20)
    0x8cb: v8cb = CALLDATALOAD v8ca(0x24)
    0x8cd: v8cd(0x40) = CONST 
    0x8cf: v8cf(0x44) = ADD v8cd(0x40), v8b0(0x4)
    0x8d0: v8d0 = CALLDATALOAD v8cf(0x44)
    0x8d1: v8d1 = ISZERO v8d0
    0x8d2: v8d2 = ISZERO v8d1
    0x8d3: v8d3(0xc95) = CONST 
    0x8d6: JUMP v8d3(0xc95)

    Begin block 0xc950x89f
    prev=[0x8c2], succ=[0xafe0x89f]
    =================================
    0xc960x89f: v89fc96(0x0) = CONST 
    0xc980x89f: v89fc98(0xc9f) = CONST 
    0xc9b0x89f: v89fc9b(0xafe) = CONST 
    0xc9e0x89f: JUMP v89fc9b(0xafe)

    Begin block 0xafe0x89f
    prev=[0xc950x89f], succ=[0xb450x89f, 0xb660x89f]
    =================================
    0xaff0x89f: v89faff(0x12) = CONST 
    0xb010x89f: v89fb01 = SLOAD v89faff(0x12)
    0xb020x89f: v89fb02(0x40) = CONST 
    0xb040x89f: v89fb04 = MLOAD v89fb02(0x40)
    0xb050x89f: v89fb05(0x60) = CONST 
    0xb080x89f: v89fb08(0x0) = CONST 
    0xb0b0x89f: v89fb0b(0x1) = CONST 
    0xb0d0x89f: v89fb0d(0x1) = CONST 
    0xb0f0x89f: v89fb0f(0xa0) = CONST 
    0xb110x89f: v89fb11(0x10000000000000000000000000000000000000000) = SHL v89fb0f(0xa0), v89fb0d(0x1)
    0xb120x89f: v89fb12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v89fb11(0x10000000000000000000000000000000000000000), v89fb0b(0x1)
    0xb150x89f: v89fb15 = AND v89fb01, v89fb12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x89f: v89fb19 = CALLDATASIZE 
    0xb210x89f: CALLDATACOPY v89fb04, v89fb08(0x0), v89fb19
    0xb220x89f: v89fb22(0x40) = CONST 
    0xb240x89f: v89fb24 = MLOAD v89fb22(0x40)
    0xb260x89f: v89fb26 = ADD v89fb04, v89fb19
    0xb290x89f: v89fb29(0x0) = CONST 
    0xb330x89f: v89fb33 = SUB v89fb26, v89fb24
    0xb360x89f: v89fb36 = GAS 
    0xb370x89f: v89fb37 = DELEGATECALL v89fb36, v89fb15, v89fb24, v89fb33, v89fb24, v89fb29(0x0)
    0xb3b0x89f: v89fb3b = RETURNDATASIZE 
    0xb3d0x89f: v89fb3d(0x0) = CONST 
    0xb400x89f: v89fb40 = EQ v89fb3b, v89fb3d(0x0)
    0xb410x89f: v89fb41(0xb66) = CONST 
    0xb440x89f: JUMPI v89fb41(0xb66), v89fb40

    Begin block 0xb450x89f
    prev=[0xafe0x89f], succ=[0xb6b0x89f]
    =================================
    0xb450x89f: v89fb45(0x40) = CONST 
    0xb470x89f: v89fb47 = MLOAD v89fb45(0x40)
    0xb4a0x89f: v89fb4a(0x1f) = CONST 
    0xb4c0x89f: v89fb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v89fb4a(0x1f)
    0xb4d0x89f: v89fb4d(0x3f) = CONST 
    0xb4f0x89f: v89fb4f = RETURNDATASIZE 
    0xb500x89f: v89fb50 = ADD v89fb4f, v89fb4d(0x3f)
    0xb510x89f: v89fb51 = AND v89fb50, v89fb4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x89f: v89fb53 = ADD v89fb47, v89fb51
    0xb540x89f: v89fb54(0x40) = CONST 
    0xb560x89f: MSTORE v89fb54(0x40), v89fb53
    0xb570x89f: v89fb57 = RETURNDATASIZE 
    0xb590x89f: MSTORE v89fb47, v89fb57
    0xb5a0x89f: v89fb5a = RETURNDATASIZE 
    0xb5b0x89f: v89fb5b(0x0) = CONST 
    0xb5d0x89f: v89fb5d(0x20) = CONST 
    0xb600x89f: v89fb60 = ADD v89fb47, v89fb5d(0x20)
    0xb610x89f: RETURNDATACOPY v89fb60, v89fb5b(0x0), v89fb5a
    0xb620x89f: v89fb62(0xb6b) = CONST 
    0xb650x89f: JUMP v89fb62(0xb6b)

    Begin block 0xb6b0x89f
    prev=[0xb450x89f, 0xb660x89f], succ=[0xb7f0x89f, 0x153c0x89f]
    =================================
    0xb700x89f: v89fb70(0x40) = CONST 
    0xb720x89f: v89fb72 = MLOAD v89fb70(0x40)
    0xb730x89f: v89fb73 = RETURNDATASIZE 
    0xb740x89f: v89fb74(0x0) = CONST 
    0xb770x89f: RETURNDATACOPY v89fb72, v89fb74(0x0), v89fb73
    0xb7a0x89f: v89fb7a = ISZERO v89fb37
    0xb7b0x89f: v89fb7b(0x153c) = CONST 
    0xb7e0x89f: JUMPI v89fb7b(0x153c), v89fb7a

    Begin block 0xb7f0x89f
    prev=[0xb6b0x89f], succ=[]
    =================================
    0xb7f0x89f: v89fb7f = RETURNDATASIZE 
    0xb810x89f: RETURN v89fb72, v89fb7f

    Begin block 0x153c0x89f
    prev=[0xb6b0x89f], succ=[]
    =================================
    0x153d0x89f: v89f153d = RETURNDATASIZE 
    0x153f0x89f: REVERT v89fb72, v89f153d

    Begin block 0xb660x89f
    prev=[0xafe0x89f], succ=[0xb6b0x89f]
    =================================
    0xb670x89f: v89fb67(0x60) = CONST 

}

function migrator()() public {
    Begin block 0x8d7
    prev=[], succ=[0x8df, 0x8e3]
    =================================
    0x8d8: v8d8 = CALLVALUE 
    0x8da: v8da = ISZERO v8d8
    0x8db: v8db(0x8e3) = CONST 
    0x8de: JUMPI v8db(0x8e3), v8da

    Begin block 0x8df
    prev=[0x8d7], succ=[]
    =================================
    0x8df: v8df(0x0) = CONST 
    0x8e2: REVERT v8df(0x0), v8df(0x0)

    Begin block 0x8e3
    prev=[0x8d7], succ=[0x1120]
    =================================
    0x8e5: v8e5(0x1966) = CONST 
    0x8e8: v8e8(0x1120) = CONST 
    0x8eb: JUMP v8e8(0x1120)

    Begin block 0x1120
    prev=[0x8e3], succ=[0x1966]
    =================================
    0x1121: v1121(0x6) = CONST 
    0x1123: v1123 = SLOAD v1121(0x6)
    0x1124: v1124(0x1) = CONST 
    0x1126: v1126(0x1) = CONST 
    0x1128: v1128(0xa0) = CONST 
    0x112a: v112a(0x10000000000000000000000000000000000000000) = SHL v1128(0xa0), v1126(0x1)
    0x112b: v112b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v112a(0x10000000000000000000000000000000000000000), v1124(0x1)
    0x112c: v112c = AND v112b(0xffffffffffffffffffffffffffffffffffffffff), v1123
    0x112e: JUMP v8e5(0x1966)

    Begin block 0x1966
    prev=[0x1120], succ=[]
    =================================
    0x1967: v1967(0x40) = CONST 
    0x196a: v196a = MLOAD v1967(0x40)
    0x196b: v196b(0x1) = CONST 
    0x196d: v196d(0x1) = CONST 
    0x196f: v196f(0xa0) = CONST 
    0x1971: v1971(0x10000000000000000000000000000000000000000) = SHL v196f(0xa0), v196d(0x1)
    0x1972: v1972(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1971(0x10000000000000000000000000000000000000000), v196b(0x1)
    0x1975: v1975 = AND v112c, v1972(0xffffffffffffffffffffffffffffffffffffffff)
    0x1977: MSTORE v196a, v1975
    0x1978: v1978 = MLOAD v1967(0x40)
    0x197c: v197c(0x0) = SUB v196a, v1978
    0x197d: v197d(0x20) = CONST 
    0x197f: v197f(0x20) = ADD v197d(0x20), v197c(0x0)
    0x1981: RETURN v1978, v197f(0x20)

}

function nonces(address)() public {
    Begin block 0x8ec
    prev=[], succ=[0x8f4, 0x8f8]
    =================================
    0x8ed: v8ed = CALLVALUE 
    0x8ef: v8ef = ISZERO v8ed
    0x8f0: v8f0(0x8f8) = CONST 
    0x8f3: JUMPI v8f0(0x8f8), v8ef

    Begin block 0x8f4
    prev=[0x8ec], succ=[]
    =================================
    0x8f4: v8f4(0x0) = CONST 
    0x8f7: REVERT v8f4(0x0), v8f4(0x0)

    Begin block 0x8f8
    prev=[0x8ec], succ=[0x90b, 0x90f]
    =================================
    0x8fa: v8fa(0x19a1) = CONST 
    0x8fd: v8fd(0x4) = CONST 
    0x900: v900 = CALLDATASIZE 
    0x901: v901 = SUB v900, v8fd(0x4)
    0x902: v902(0x20) = CONST 
    0x905: v905 = LT v901, v902(0x20)
    0x906: v906 = ISZERO v905
    0x907: v907(0x90f) = CONST 
    0x90a: JUMPI v907(0x90f), v906

    Begin block 0x90b
    prev=[0x8f8], succ=[]
    =================================
    0x90b: v90b(0x0) = CONST 
    0x90e: REVERT v90b(0x0), v90b(0x0)

    Begin block 0x90f
    prev=[0x8f8], succ=[0x112f]
    =================================
    0x911: v911 = CALLDATALOAD v8fd(0x4)
    0x912: v912(0x1) = CONST 
    0x914: v914(0x1) = CONST 
    0x916: v916(0xa0) = CONST 
    0x918: v918(0x10000000000000000000000000000000000000000) = SHL v916(0xa0), v914(0x1)
    0x919: v919(0xffffffffffffffffffffffffffffffffffffffff) = SUB v918(0x10000000000000000000000000000000000000000), v912(0x1)
    0x91a: v91a = AND v919(0xffffffffffffffffffffffffffffffffffffffff), v911
    0x91b: v91b(0x112f) = CONST 
    0x91e: JUMP v91b(0x112f)

    Begin block 0x112f
    prev=[0x90f], succ=[0x19a1]
    =================================
    0x1130: v1130(0x11) = CONST 
    0x1132: v1132(0x20) = CONST 
    0x1134: MSTORE v1132(0x20), v1130(0x11)
    0x1135: v1135(0x0) = CONST 
    0x1139: MSTORE v1135(0x0), v91a
    0x113a: v113a(0x40) = CONST 
    0x113d: v113d = SHA3 v1135(0x0), v113a(0x40)
    0x113e: v113e = SLOAD v113d
    0x1140: JUMP v8fa(0x19a1)

    Begin block 0x19a1
    prev=[0x112f], succ=[]
    =================================
    0x19a2: v19a2(0x40) = CONST 
    0x19a5: v19a5 = MLOAD v19a2(0x40)
    0x19a8: MSTORE v19a5, v113e
    0x19a9: v19a9 = MLOAD v19a2(0x40)
    0x19ad: v19ad(0x0) = SUB v19a5, v19a9
    0x19ae: v19ae(0x20) = CONST 
    0x19b0: v19b0(0x20) = ADD v19ae(0x20), v19ad(0x0)
    0x19b2: RETURN v19a9, v19b0(0x20)

}

function symbol()() public {
    Begin block 0x91f
    prev=[], succ=[0x927, 0x92b]
    =================================
    0x920: v920 = CALLVALUE 
    0x922: v922 = ISZERO v920
    0x923: v923(0x92b) = CONST 
    0x926: JUMPI v923(0x92b), v922

    Begin block 0x927
    prev=[0x91f], succ=[]
    =================================
    0x927: v927(0x0) = CONST 
    0x92a: REVERT v927(0x0), v927(0x0)

    Begin block 0x92b
    prev=[0x91f], succ=[0x30b0x91f]
    =================================
    0x92d: v92d(0x30b) = CONST 
    0x930: v930(0x1141) = CONST 
    0x933: v933_0, v933_1 = CALLPRIVATE v930(0x1141), v92d(0x30b)

    Begin block 0x30b0x91f
    prev=[0x92b], succ=[0x32d0x91f]
    =================================
    0x30c0x91f: v91f30c(0x40) = CONST 
    0x30f0x91f: v91f30f = MLOAD v91f30c(0x40)
    0x3100x91f: v91f310(0x20) = CONST 
    0x3140x91f: MSTORE v91f30f, v91f310(0x20)
    0x3160x91f: v91f316 = MLOAD v933_0
    0x3190x91f: v91f319 = ADD v91f30f, v91f310(0x20)
    0x31a0x91f: MSTORE v91f319, v91f316
    0x31c0x91f: v91f31c = MLOAD v933_0
    0x3230x91f: v91f323 = ADD v91f30f, v91f30c(0x40)
    0x3260x91f: v91f326 = ADD v933_0, v91f310(0x20)
    0x32b0x91f: v91f32b(0x0) = CONST 

    Begin block 0x32d0x91f
    prev=[0x3360x91f, 0x30b0x91f], succ=[0x3450x91f, 0x3360x91f]
    =================================
    0x32d0x91f_0x0: v32d91f_0 = PHI v91f340, v91f32b(0x0)
    0x3300x91f: v91f330 = LT v32d91f_0, v91f31c
    0x3310x91f: v91f331 = ISZERO v91f330
    0x3320x91f: v91f332(0x345) = CONST 
    0x3350x91f: JUMPI v91f332(0x345), v91f331

    Begin block 0x3450x91f
    prev=[0x32d0x91f], succ=[0x3720x91f, 0x3590x91f]
    =================================
    0x34e0x91f: v91f34e = ADD v91f31c, v91f323
    0x3500x91f: v91f350(0x1f) = CONST 
    0x3520x91f: v91f352 = AND v91f350(0x1f), v91f31c
    0x3540x91f: v91f354 = ISZERO v91f352
    0x3550x91f: v91f355(0x372) = CONST 
    0x3580x91f: JUMPI v91f355(0x372), v91f354

    Begin block 0x3720x91f
    prev=[0x3450x91f, 0x3590x91f], succ=[]
    =================================
    0x3720x91f_0x1: v37291f_1 = PHI v91f36f, v91f34e
    0x3780x91f: v91f378(0x40) = CONST 
    0x37a0x91f: v91f37a = MLOAD v91f378(0x40)
    0x37d0x91f: v91f37d = SUB v37291f_1, v91f37a
    0x37f0x91f: RETURN v91f37a, v91f37d

    Begin block 0x3590x91f
    prev=[0x3450x91f], succ=[0x3720x91f]
    =================================
    0x35b0x91f: v91f35b = SUB v91f34e, v91f352
    0x35d0x91f: v91f35d = MLOAD v91f35b
    0x35e0x91f: v91f35e(0x1) = CONST 
    0x3610x91f: v91f361(0x20) = CONST 
    0x3630x91f: v91f363 = SUB v91f361(0x20), v91f352
    0x3640x91f: v91f364(0x100) = CONST 
    0x3670x91f: v91f367 = EXP v91f364(0x100), v91f363
    0x3680x91f: v91f368 = SUB v91f367, v91f35e(0x1)
    0x3690x91f: v91f369 = NOT v91f368
    0x36a0x91f: v91f36a = AND v91f369, v91f35d
    0x36c0x91f: MSTORE v91f35b, v91f36a
    0x36d0x91f: v91f36d(0x20) = CONST 
    0x36f0x91f: v91f36f = ADD v91f36d(0x20), v91f35b

    Begin block 0x3360x91f
    prev=[0x32d0x91f], succ=[0x32d0x91f]
    =================================
    0x3360x91f_0x0: v33691f_0 = PHI v91f340, v91f32b(0x0)
    0x3380x91f: v91f338 = ADD v33691f_0, v91f326
    0x3390x91f: v91f339 = MLOAD v91f338
    0x33c0x91f: v91f33c = ADD v33691f_0, v91f323
    0x33d0x91f: MSTORE v91f33c, v91f339
    0x33e0x91f: v91f33e(0x20) = CONST 
    0x3400x91f: v91f340 = ADD v91f33e(0x20), v33691f_0
    0x3410x91f: v91f341(0x32d) = CONST 
    0x3440x91f: JUMP v91f341(0x32d)

}

function initSupply()() public {
    Begin block 0x934
    prev=[], succ=[0x93c, 0x940]
    =================================
    0x935: v935 = CALLVALUE 
    0x937: v937 = ISZERO v935
    0x938: v938(0x940) = CONST 
    0x93b: JUMPI v938(0x940), v937

    Begin block 0x93c
    prev=[0x934], succ=[]
    =================================
    0x93c: v93c(0x0) = CONST 
    0x93f: REVERT v93c(0x0), v93c(0x0)

    Begin block 0x940
    prev=[0x934], succ=[0x1199]
    =================================
    0x942: v942(0x19d2) = CONST 
    0x945: v945(0x1199) = CONST 
    0x948: JUMP v945(0x1199)

    Begin block 0x1199
    prev=[0x940], succ=[0x19d2]
    =================================
    0x119a: v119a(0xc) = CONST 
    0x119c: v119c = SLOAD v119a(0xc)
    0x119e: JUMP v942(0x19d2)

    Begin block 0x19d2
    prev=[0x1199], succ=[]
    =================================
    0x19d3: v19d3(0x40) = CONST 
    0x19d6: v19d6 = MLOAD v19d3(0x40)
    0x19d9: MSTORE v19d6, v119c
    0x19da: v19da = MLOAD v19d3(0x40)
    0x19de: v19de(0x0) = SUB v19d6, v19da
    0x19df: v19df(0x20) = CONST 
    0x19e1: v19e1(0x20) = ADD v19df(0x20), v19de(0x0)
    0x19e3: RETURN v19da, v19e1(0x20)

}

function fragmentToYuan(uint256)() public {
    Begin block 0x949
    prev=[], succ=[0x951, 0x955]
    =================================
    0x94a: v94a = CALLVALUE 
    0x94c: v94c = ISZERO v94a
    0x94d: v94d(0x955) = CONST 
    0x950: JUMPI v94d(0x955), v94c

    Begin block 0x951
    prev=[0x949], succ=[]
    =================================
    0x951: v951(0x0) = CONST 
    0x954: REVERT v951(0x0), v951(0x0)

    Begin block 0x955
    prev=[0x949], succ=[0x968, 0x96c]
    =================================
    0x957: v957(0x1a03) = CONST 
    0x95a: v95a(0x4) = CONST 
    0x95d: v95d = CALLDATASIZE 
    0x95e: v95e = SUB v95d, v95a(0x4)
    0x95f: v95f(0x20) = CONST 
    0x962: v962 = LT v95e, v95f(0x20)
    0x963: v963 = ISZERO v962
    0x964: v964(0x96c) = CONST 
    0x967: JUMPI v964(0x96c), v963

    Begin block 0x968
    prev=[0x955], succ=[]
    =================================
    0x968: v968(0x0) = CONST 
    0x96b: REVERT v968(0x0), v968(0x0)

    Begin block 0x96c
    prev=[0x955], succ=[0xce90x949]
    =================================
    0x96e: v96e = CALLDATALOAD v95a(0x4)
    0x96f: v96f(0xce9) = CONST 
    0x972: JUMP v96f(0xce9)

    Begin block 0xce90x949
    prev=[0x96c], succ=[0x12de0x949]
    =================================
    0xcea0x949: v949cea(0x0) = CONST 
    0xcec0x949: v949cec(0xcf3) = CONST 
    0xcef0x949: v949cef(0x12de) = CONST 
    0xcf20x949: JUMP v949cef(0x12de)

    Begin block 0x12de0x949
    prev=[0xce90x949], succ=[0x13600x949]
    =================================
    0x12df0x949: v94912df(0x60) = CONST 
    0x12e10x949: v94912e1(0x0) = CONST 
    0x12e30x949: v94912e3 = ADDRESS 
    0x12e40x949: v94912e4(0x1) = CONST 
    0x12e60x949: v94912e6(0x1) = CONST 
    0x12e80x949: v94912e8(0xa0) = CONST 
    0x12ea0x949: v94912ea(0x10000000000000000000000000000000000000000) = SHL v94912e8(0xa0), v94912e6(0x1)
    0x12eb0x949: v94912eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v94912ea(0x10000000000000000000000000000000000000000), v94912e4(0x1)
    0x12ec0x949: v94912ec = AND v94912eb(0xffffffffffffffffffffffffffffffffffffffff), v94912e3
    0x12ed0x949: v94912ed(0x0) = CONST 
    0x12ef0x949: v94912ef = CALLDATASIZE 
    0x12f00x949: v94912f0(0x40) = CONST 
    0x12f20x949: v94912f2 = MLOAD v94912f0(0x40)
    0x12f30x949: v94912f3(0x24) = CONST 
    0x12f50x949: v94912f5 = ADD v94912f3(0x24), v94912f2
    0x12f80x949: v94912f8(0x20) = CONST 
    0x12fa0x949: v94912fa = ADD v94912f8(0x20), v94912f5
    0x12fd0x949: v94912fd(0x20) = SUB v94912fa, v94912f5
    0x12ff0x949: MSTORE v94912f5, v94912fd(0x20)
    0x13050x949: MSTORE v94912fa, v94912ef
    0x13060x949: v9491306(0x20) = CONST 
    0x13080x949: v9491308 = ADD v9491306(0x20), v94912fa
    0x130e0x949: CALLDATACOPY v9491308, v94912ed(0x0), v94912ef
    0x130f0x949: v949130f(0x0) = CONST 
    0x13130x949: v9491313 = ADD v94912ef, v9491308
    0x13140x949: MSTORE v9491313, v949130f(0x0)
    0x13150x949: v9491315(0x40) = CONST 
    0x13180x949: v9491318 = MLOAD v9491315(0x40)
    0x13190x949: v9491319(0x1f) = CONST 
    0x131d0x949: v949131d = ADD v94912ef, v9491319(0x1f)
    0x131e0x949: v949131e(0x1f) = CONST 
    0x13200x949: v9491320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v949131e(0x1f)
    0x13230x949: v9491323 = AND v9491320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v949131d
    0x13260x949: v9491326 = ADD v9491308, v9491323
    0x13290x949: v9491329 = SUB v9491326, v9491318
    0x132c0x949: v949132c = ADD v9491320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v9491329
    0x132e0x949: MSTORE v9491318, v949132c
    0x13310x949: MSTORE v9491315(0x40), v9491326
    0x13320x949: v9491332(0x20) = CONST 
    0x13350x949: v9491335 = ADD v9491318, v9491332(0x20)
    0x13370x949: v9491337 = MLOAD v9491335
    0x13380x949: v9491338(0x1) = CONST 
    0x133a0x949: v949133a(0x1) = CONST 
    0x133c0x949: v949133c(0xe0) = CONST 
    0x133e0x949: v949133e(0x100000000000000000000000000000000000000000000000000000000) = SHL v949133c(0xe0), v949133a(0x1)
    0x133f0x949: v949133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v949133e(0x100000000000000000000000000000000000000000000000000000000), v9491338(0x1)
    0x13400x949: v9491340 = AND v949133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v9491337
    0x13410x949: v9491341(0x933c1ed) = CONST 
    0x13460x949: v9491346(0xe0) = CONST 
    0x13480x949: v9491348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v9491346(0xe0), v9491341(0x933c1ed)
    0x13490x949: v9491349 = OR v9491348(0x933c1ed00000000000000000000000000000000000000000000000000000000), v9491340
    0x134b0x949: MSTORE v9491335, v9491349
    0x134d0x949: v949134d = MLOAD v9491315(0x40)
    0x134f0x949: v949134f = MLOAD v9491318

    Begin block 0x13600x949
    prev=[0x13690x949, 0x12de0x949], succ=[0x137f0x949, 0x13690x949]
    =================================
    0x13600x949_0x2: v1360949_2 = PHI v9491372, v949134f
    0x13610x949: v9491361(0x20) = CONST 
    0x13640x949: v9491364 = LT v1360949_2, v9491361(0x20)
    0x13650x949: v9491365(0x137f) = CONST 
    0x13680x949: JUMPI v9491365(0x137f), v9491364

    Begin block 0x137f0x949
    prev=[0x13600x949], succ=[0x13be0x949, 0x13df0x949]
    =================================
    0x137f0x949_0x0: v137f949_0 = PHI v949137a, v9491335
    0x137f0x949_0x1: v137f949_1 = PHI v9491378, v949134d
    0x137f0x949_0x2: v137f949_2 = PHI v9491372, v949134f
    0x13800x949: v9491380(0x1) = CONST 
    0x13830x949: v9491383(0x20) = CONST 
    0x13850x949: v9491385 = SUB v9491383(0x20), v137f949_2
    0x13860x949: v9491386(0x100) = CONST 
    0x13890x949: v9491389 = EXP v9491386(0x100), v9491385
    0x138a0x949: v949138a = SUB v9491389, v9491380(0x1)
    0x138c0x949: v949138c = NOT v949138a
    0x138e0x949: v949138e = MLOAD v137f949_0
    0x138f0x949: v949138f = AND v949138e, v949138c
    0x13920x949: v9491392 = MLOAD v137f949_1
    0x13930x949: v9491393 = AND v9491392, v949138a
    0x13960x949: v9491396 = OR v949138f, v9491393
    0x13980x949: MSTORE v137f949_1, v9491396
    0x13a10x949: v94913a1 = ADD v949134f, v949134d
    0x13a50x949: v94913a5(0x0) = CONST 
    0x13a70x949: v94913a7(0x40) = CONST 
    0x13a90x949: v94913a9 = MLOAD v94913a7(0x40)
    0x13ac0x949: v94913ac = SUB v94913a1, v94913a9
    0x13af0x949: v94913af = GAS 
    0x13b00x949: v94913b0 = STATICCALL v94913af, v94912ec, v94913a9, v94913ac, v94913a9, v94913a5(0x0)
    0x13b40x949: v94913b4 = RETURNDATASIZE 
    0x13b60x949: v94913b6(0x0) = CONST 
    0x13b90x949: v94913b9 = EQ v94913b4, v94913b6(0x0)
    0x13ba0x949: v94913ba(0x13df) = CONST 
    0x13bd0x949: JUMPI v94913ba(0x13df), v94913b9

    Begin block 0x13be0x949
    prev=[0x137f0x949], succ=[0x13e40x949]
    =================================
    0x13be0x949: v94913be(0x40) = CONST 
    0x13c00x949: v94913c0 = MLOAD v94913be(0x40)
    0x13c30x949: v94913c3(0x1f) = CONST 
    0x13c50x949: v94913c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v94913c3(0x1f)
    0x13c60x949: v94913c6(0x3f) = CONST 
    0x13c80x949: v94913c8 = RETURNDATASIZE 
    0x13c90x949: v94913c9 = ADD v94913c8, v94913c6(0x3f)
    0x13ca0x949: v94913ca = AND v94913c9, v94913c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0x949: v94913cc = ADD v94913c0, v94913ca
    0x13cd0x949: v94913cd(0x40) = CONST 
    0x13cf0x949: MSTORE v94913cd(0x40), v94913cc
    0x13d00x949: v94913d0 = RETURNDATASIZE 
    0x13d20x949: MSTORE v94913c0, v94913d0
    0x13d30x949: v94913d3 = RETURNDATASIZE 
    0x13d40x949: v94913d4(0x0) = CONST 
    0x13d60x949: v94913d6(0x20) = CONST 
    0x13d90x949: v94913d9 = ADD v94913c0, v94913d6(0x20)
    0x13da0x949: RETURNDATACOPY v94913d9, v94913d4(0x0), v94913d3
    0x13db0x949: v94913db(0x13e4) = CONST 
    0x13de0x949: JUMP v94913db(0x13e4)

    Begin block 0x13e40x949
    prev=[0x13be0x949, 0x13df0x949], succ=[0x13f80x949, 0x155f0x949]
    =================================
    0x13e90x949: v94913e9(0x40) = CONST 
    0x13eb0x949: v94913eb = MLOAD v94913e9(0x40)
    0x13ec0x949: v94913ec = RETURNDATASIZE 
    0x13ed0x949: v94913ed(0x0) = CONST 
    0x13f00x949: RETURNDATACOPY v94913eb, v94913ed(0x0), v94913ec
    0x13f30x949: v94913f3 = ISZERO v94913b0
    0x13f40x949: v94913f4(0x155f) = CONST 
    0x13f70x949: JUMPI v94913f4(0x155f), v94913f3

    Begin block 0x13f80x949
    prev=[0x13e40x949], succ=[]
    =================================
    0x13f80x949: v94913f8(0x40) = CONST 
    0x13fa0x949: v94913fa = RETURNDATASIZE 
    0x13fb0x949: v94913fb = SUB v94913fa, v94913f8(0x40)
    0x13fc0x949: v94913fc(0x40) = CONST 
    0x13ff0x949: v94913ff = ADD v94913eb, v94913fc(0x40)
    0x14000x949: RETURN v94913ff, v94913fb

    Begin block 0x155f0x949
    prev=[0x13e40x949], succ=[]
    =================================
    0x15600x949: v9491560 = RETURNDATASIZE 
    0x15620x949: REVERT v94913eb, v9491560

    Begin block 0x13df0x949
    prev=[0x137f0x949], succ=[0x13e40x949]
    =================================
    0x13e00x949: v94913e0(0x60) = CONST 

    Begin block 0x13690x949
    prev=[0x13600x949], succ=[0x13600x949]
    =================================
    0x13690x949_0x0: v1369949_0 = PHI v949137a, v9491335
    0x13690x949_0x1: v1369949_1 = PHI v9491378, v949134d
    0x13690x949_0x2: v1369949_2 = PHI v9491372, v949134f
    0x136a0x949: v949136a = MLOAD v1369949_0
    0x136c0x949: MSTORE v1369949_1, v949136a
    0x136d0x949: v949136d(0x1f) = CONST 
    0x136f0x949: v949136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v949136d(0x1f)
    0x13720x949: v9491372 = ADD v1369949_2, v949136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740x949: v9491374(0x20) = CONST 
    0x13780x949: v9491378 = ADD v9491374(0x20), v1369949_1
    0x137a0x949: v949137a = ADD v9491374(0x20), v1369949_0
    0x137b0x949: v949137b(0x1360) = CONST 
    0x137e0x949: JUMP v949137b(0x1360)

}

function delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32)() public {
    Begin block 0x973
    prev=[], succ=[0x97b, 0x97f]
    =================================
    0x974: v974 = CALLVALUE 
    0x976: v976 = ISZERO v974
    0x977: v977(0x97f) = CONST 
    0x97a: JUMPI v977(0x97f), v976

    Begin block 0x97b
    prev=[0x973], succ=[]
    =================================
    0x97b: v97b(0x0) = CONST 
    0x97e: REVERT v97b(0x0), v97b(0x0)

    Begin block 0x97f
    prev=[0x973], succ=[0x992, 0x996]
    =================================
    0x981: v981(0x1a34) = CONST 
    0x984: v984(0x4) = CONST 
    0x987: v987 = CALLDATASIZE 
    0x988: v988 = SUB v987, v984(0x4)
    0x989: v989(0xc0) = CONST 
    0x98c: v98c = LT v988, v989(0xc0)
    0x98d: v98d = ISZERO v98c
    0x98e: v98e(0x996) = CONST 
    0x991: JUMPI v98e(0x996), v98d

    Begin block 0x992
    prev=[0x97f], succ=[]
    =================================
    0x992: v992(0x0) = CONST 
    0x995: REVERT v992(0x0), v992(0x0)

    Begin block 0x996
    prev=[0x97f], succ=[0x119f]
    =================================
    0x998: v998(0x1) = CONST 
    0x99a: v99a(0x1) = CONST 
    0x99c: v99c(0xa0) = CONST 
    0x99e: v99e(0x10000000000000000000000000000000000000000) = SHL v99c(0xa0), v99a(0x1)
    0x99f: v99f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v99e(0x10000000000000000000000000000000000000000), v998(0x1)
    0x9a1: v9a1 = CALLDATALOAD v984(0x4)
    0x9a2: v9a2 = AND v9a1, v99f(0xffffffffffffffffffffffffffffffffffffffff)
    0x9a4: v9a4(0x20) = CONST 
    0x9a7: v9a7(0x24) = ADD v984(0x4), v9a4(0x20)
    0x9a8: v9a8 = CALLDATALOAD v9a7(0x24)
    0x9aa: v9aa(0x40) = CONST 
    0x9ad: v9ad(0x44) = ADD v984(0x4), v9aa(0x40)
    0x9ae: v9ae = CALLDATALOAD v9ad(0x44)
    0x9b0: v9b0(0xff) = CONST 
    0x9b2: v9b2(0x60) = CONST 
    0x9b5: v9b5(0x64) = ADD v984(0x4), v9b2(0x60)
    0x9b6: v9b6 = CALLDATALOAD v9b5(0x64)
    0x9b7: v9b7 = AND v9b6, v9b0(0xff)
    0x9b9: v9b9(0x80) = CONST 
    0x9bc: v9bc(0x84) = ADD v984(0x4), v9b9(0x80)
    0x9bd: v9bd = CALLDATALOAD v9bc(0x84)
    0x9bf: v9bf(0xa0) = CONST 
    0x9c1: v9c1(0xa4) = ADD v9bf(0xa0), v984(0x4)
    0x9c2: v9c2 = CALLDATALOAD v9c1(0xa4)
    0x9c3: v9c3(0x119f) = CONST 
    0x9c6: JUMP v9c3(0x119f)

    Begin block 0x119f
    prev=[0x996], succ=[0xafe0x973]
    =================================
    0x11a0: v11a0(0x11a7) = CONST 
    0x11a3: v11a3(0xafe) = CONST 
    0x11a6: JUMP v11a3(0xafe)

    Begin block 0xafe0x973
    prev=[0x119f], succ=[0xb450x973, 0xb660x973]
    =================================
    0xaff0x973: v973aff(0x12) = CONST 
    0xb010x973: v973b01 = SLOAD v973aff(0x12)
    0xb020x973: v973b02(0x40) = CONST 
    0xb040x973: v973b04 = MLOAD v973b02(0x40)
    0xb050x973: v973b05(0x60) = CONST 
    0xb080x973: v973b08(0x0) = CONST 
    0xb0b0x973: v973b0b(0x1) = CONST 
    0xb0d0x973: v973b0d(0x1) = CONST 
    0xb0f0x973: v973b0f(0xa0) = CONST 
    0xb110x973: v973b11(0x10000000000000000000000000000000000000000) = SHL v973b0f(0xa0), v973b0d(0x1)
    0xb120x973: v973b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v973b11(0x10000000000000000000000000000000000000000), v973b0b(0x1)
    0xb150x973: v973b15 = AND v973b01, v973b12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x973: v973b19 = CALLDATASIZE 
    0xb210x973: CALLDATACOPY v973b04, v973b08(0x0), v973b19
    0xb220x973: v973b22(0x40) = CONST 
    0xb240x973: v973b24 = MLOAD v973b22(0x40)
    0xb260x973: v973b26 = ADD v973b04, v973b19
    0xb290x973: v973b29(0x0) = CONST 
    0xb330x973: v973b33 = SUB v973b26, v973b24
    0xb360x973: v973b36 = GAS 
    0xb370x973: v973b37 = DELEGATECALL v973b36, v973b15, v973b24, v973b33, v973b24, v973b29(0x0)
    0xb3b0x973: v973b3b = RETURNDATASIZE 
    0xb3d0x973: v973b3d(0x0) = CONST 
    0xb400x973: v973b40 = EQ v973b3b, v973b3d(0x0)
    0xb410x973: v973b41(0xb66) = CONST 
    0xb440x973: JUMPI v973b41(0xb66), v973b40

    Begin block 0xb450x973
    prev=[0xafe0x973], succ=[0xb6b0x973]
    =================================
    0xb450x973: v973b45(0x40) = CONST 
    0xb470x973: v973b47 = MLOAD v973b45(0x40)
    0xb4a0x973: v973b4a(0x1f) = CONST 
    0xb4c0x973: v973b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v973b4a(0x1f)
    0xb4d0x973: v973b4d(0x3f) = CONST 
    0xb4f0x973: v973b4f = RETURNDATASIZE 
    0xb500x973: v973b50 = ADD v973b4f, v973b4d(0x3f)
    0xb510x973: v973b51 = AND v973b50, v973b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x973: v973b53 = ADD v973b47, v973b51
    0xb540x973: v973b54(0x40) = CONST 
    0xb560x973: MSTORE v973b54(0x40), v973b53
    0xb570x973: v973b57 = RETURNDATASIZE 
    0xb590x973: MSTORE v973b47, v973b57
    0xb5a0x973: v973b5a = RETURNDATASIZE 
    0xb5b0x973: v973b5b(0x0) = CONST 
    0xb5d0x973: v973b5d(0x20) = CONST 
    0xb600x973: v973b60 = ADD v973b47, v973b5d(0x20)
    0xb610x973: RETURNDATACOPY v973b60, v973b5b(0x0), v973b5a
    0xb620x973: v973b62(0xb6b) = CONST 
    0xb650x973: JUMP v973b62(0xb6b)

    Begin block 0xb6b0x973
    prev=[0xb450x973, 0xb660x973], succ=[0xb7f0x973, 0x153c0x973]
    =================================
    0xb700x973: v973b70(0x40) = CONST 
    0xb720x973: v973b72 = MLOAD v973b70(0x40)
    0xb730x973: v973b73 = RETURNDATASIZE 
    0xb740x973: v973b74(0x0) = CONST 
    0xb770x973: RETURNDATACOPY v973b72, v973b74(0x0), v973b73
    0xb7a0x973: v973b7a = ISZERO v973b37
    0xb7b0x973: v973b7b(0x153c) = CONST 
    0xb7e0x973: JUMPI v973b7b(0x153c), v973b7a

    Begin block 0xb7f0x973
    prev=[0xb6b0x973], succ=[]
    =================================
    0xb7f0x973: v973b7f = RETURNDATASIZE 
    0xb810x973: RETURN v973b72, v973b7f

    Begin block 0x153c0x973
    prev=[0xb6b0x973], succ=[]
    =================================
    0x153d0x973: v973153d = RETURNDATASIZE 
    0x153f0x973: REVERT v973b72, v973153d

    Begin block 0xb660x973
    prev=[0xafe0x973], succ=[0xb6b0x973]
    =================================
    0xb670x973: v973b67(0x60) = CONST 

}

function permit(address,address,uint256,uint256,uint8,bytes32,bytes32)() public {
    Begin block 0x9c7
    prev=[], succ=[0x9cf, 0x9d3]
    =================================
    0x9c8: v9c8 = CALLVALUE 
    0x9ca: v9ca = ISZERO v9c8
    0x9cb: v9cb(0x9d3) = CONST 
    0x9ce: JUMPI v9cb(0x9d3), v9ca

    Begin block 0x9cf
    prev=[0x9c7], succ=[]
    =================================
    0x9cf: v9cf(0x0) = CONST 
    0x9d2: REVERT v9cf(0x0), v9cf(0x0)

    Begin block 0x9d3
    prev=[0x9c7], succ=[0x9e6, 0x9ea]
    =================================
    0x9d5: v9d5(0x1a55) = CONST 
    0x9d8: v9d8(0x4) = CONST 
    0x9db: v9db = CALLDATASIZE 
    0x9dc: v9dc = SUB v9db, v9d8(0x4)
    0x9dd: v9dd(0xe0) = CONST 
    0x9e0: v9e0 = LT v9dc, v9dd(0xe0)
    0x9e1: v9e1 = ISZERO v9e0
    0x9e2: v9e2(0x9ea) = CONST 
    0x9e5: JUMPI v9e2(0x9ea), v9e1

    Begin block 0x9e6
    prev=[0x9d3], succ=[]
    =================================
    0x9e6: v9e6(0x0) = CONST 
    0x9e9: REVERT v9e6(0x0), v9e6(0x0)

    Begin block 0x9ea
    prev=[0x9d3], succ=[0x11b0]
    =================================
    0x9ec: v9ec(0x1) = CONST 
    0x9ee: v9ee(0x1) = CONST 
    0x9f0: v9f0(0xa0) = CONST 
    0x9f2: v9f2(0x10000000000000000000000000000000000000000) = SHL v9f0(0xa0), v9ee(0x1)
    0x9f3: v9f3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9f2(0x10000000000000000000000000000000000000000), v9ec(0x1)
    0x9f5: v9f5 = CALLDATALOAD v9d8(0x4)
    0x9f7: v9f7 = AND v9f3(0xffffffffffffffffffffffffffffffffffffffff), v9f5
    0x9f9: v9f9(0x20) = CONST 
    0x9fc: v9fc(0x24) = ADD v9d8(0x4), v9f9(0x20)
    0x9fd: v9fd = CALLDATALOAD v9fc(0x24)
    0xa00: va00 = AND v9f3(0xffffffffffffffffffffffffffffffffffffffff), v9fd
    0xa02: va02(0x40) = CONST 
    0xa05: va05(0x44) = ADD v9d8(0x4), va02(0x40)
    0xa06: va06 = CALLDATALOAD va05(0x44)
    0xa08: va08(0x60) = CONST 
    0xa0b: va0b(0x64) = ADD v9d8(0x4), va08(0x60)
    0xa0c: va0c = CALLDATALOAD va0b(0x64)
    0xa0e: va0e(0xff) = CONST 
    0xa10: va10(0x80) = CONST 
    0xa13: va13(0x84) = ADD v9d8(0x4), va10(0x80)
    0xa14: va14 = CALLDATALOAD va13(0x84)
    0xa15: va15 = AND va14, va0e(0xff)
    0xa17: va17(0xa0) = CONST 
    0xa1a: va1a(0xa4) = ADD v9d8(0x4), va17(0xa0)
    0xa1b: va1b = CALLDATALOAD va1a(0xa4)
    0xa1d: va1d(0xc0) = CONST 
    0xa1f: va1f(0xc4) = ADD va1d(0xc0), v9d8(0x4)
    0xa20: va20 = CALLDATALOAD va1f(0xc4)
    0xa21: va21(0x11b0) = CONST 
    0xa24: JUMP va21(0x11b0)

    Begin block 0x11b0
    prev=[0x9ea], succ=[0xafe0x9c7]
    =================================
    0x11b1: v11b1(0x11b8) = CONST 
    0x11b4: v11b4(0xafe) = CONST 
    0x11b7: JUMP v11b4(0xafe)

    Begin block 0xafe0x9c7
    prev=[0x11b0], succ=[0xb450x9c7, 0xb660x9c7]
    =================================
    0xaff0x9c7: v9c7aff(0x12) = CONST 
    0xb010x9c7: v9c7b01 = SLOAD v9c7aff(0x12)
    0xb020x9c7: v9c7b02(0x40) = CONST 
    0xb040x9c7: v9c7b04 = MLOAD v9c7b02(0x40)
    0xb050x9c7: v9c7b05(0x60) = CONST 
    0xb080x9c7: v9c7b08(0x0) = CONST 
    0xb0b0x9c7: v9c7b0b(0x1) = CONST 
    0xb0d0x9c7: v9c7b0d(0x1) = CONST 
    0xb0f0x9c7: v9c7b0f(0xa0) = CONST 
    0xb110x9c7: v9c7b11(0x10000000000000000000000000000000000000000) = SHL v9c7b0f(0xa0), v9c7b0d(0x1)
    0xb120x9c7: v9c7b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9c7b11(0x10000000000000000000000000000000000000000), v9c7b0b(0x1)
    0xb150x9c7: v9c7b15 = AND v9c7b01, v9c7b12(0xffffffffffffffffffffffffffffffffffffffff)
    0xb190x9c7: v9c7b19 = CALLDATASIZE 
    0xb210x9c7: CALLDATACOPY v9c7b04, v9c7b08(0x0), v9c7b19
    0xb220x9c7: v9c7b22(0x40) = CONST 
    0xb240x9c7: v9c7b24 = MLOAD v9c7b22(0x40)
    0xb260x9c7: v9c7b26 = ADD v9c7b04, v9c7b19
    0xb290x9c7: v9c7b29(0x0) = CONST 
    0xb330x9c7: v9c7b33 = SUB v9c7b26, v9c7b24
    0xb360x9c7: v9c7b36 = GAS 
    0xb370x9c7: v9c7b37 = DELEGATECALL v9c7b36, v9c7b15, v9c7b24, v9c7b33, v9c7b24, v9c7b29(0x0)
    0xb3b0x9c7: v9c7b3b = RETURNDATASIZE 
    0xb3d0x9c7: v9c7b3d(0x0) = CONST 
    0xb400x9c7: v9c7b40 = EQ v9c7b3b, v9c7b3d(0x0)
    0xb410x9c7: v9c7b41(0xb66) = CONST 
    0xb440x9c7: JUMPI v9c7b41(0xb66), v9c7b40

    Begin block 0xb450x9c7
    prev=[0xafe0x9c7], succ=[0xb6b0x9c7]
    =================================
    0xb450x9c7: v9c7b45(0x40) = CONST 
    0xb470x9c7: v9c7b47 = MLOAD v9c7b45(0x40)
    0xb4a0x9c7: v9c7b4a(0x1f) = CONST 
    0xb4c0x9c7: v9c7b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v9c7b4a(0x1f)
    0xb4d0x9c7: v9c7b4d(0x3f) = CONST 
    0xb4f0x9c7: v9c7b4f = RETURNDATASIZE 
    0xb500x9c7: v9c7b50 = ADD v9c7b4f, v9c7b4d(0x3f)
    0xb510x9c7: v9c7b51 = AND v9c7b50, v9c7b4c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xb530x9c7: v9c7b53 = ADD v9c7b47, v9c7b51
    0xb540x9c7: v9c7b54(0x40) = CONST 
    0xb560x9c7: MSTORE v9c7b54(0x40), v9c7b53
    0xb570x9c7: v9c7b57 = RETURNDATASIZE 
    0xb590x9c7: MSTORE v9c7b47, v9c7b57
    0xb5a0x9c7: v9c7b5a = RETURNDATASIZE 
    0xb5b0x9c7: v9c7b5b(0x0) = CONST 
    0xb5d0x9c7: v9c7b5d(0x20) = CONST 
    0xb600x9c7: v9c7b60 = ADD v9c7b47, v9c7b5d(0x20)
    0xb610x9c7: RETURNDATACOPY v9c7b60, v9c7b5b(0x0), v9c7b5a
    0xb620x9c7: v9c7b62(0xb6b) = CONST 
    0xb650x9c7: JUMP v9c7b62(0xb6b)

    Begin block 0xb6b0x9c7
    prev=[0xb450x9c7, 0xb660x9c7], succ=[0xb7f0x9c7, 0x153c0x9c7]
    =================================
    0xb700x9c7: v9c7b70(0x40) = CONST 
    0xb720x9c7: v9c7b72 = MLOAD v9c7b70(0x40)
    0xb730x9c7: v9c7b73 = RETURNDATASIZE 
    0xb740x9c7: v9c7b74(0x0) = CONST 
    0xb770x9c7: RETURNDATACOPY v9c7b72, v9c7b74(0x0), v9c7b73
    0xb7a0x9c7: v9c7b7a = ISZERO v9c7b37
    0xb7b0x9c7: v9c7b7b(0x153c) = CONST 
    0xb7e0x9c7: JUMPI v9c7b7b(0x153c), v9c7b7a

    Begin block 0xb7f0x9c7
    prev=[0xb6b0x9c7], succ=[]
    =================================
    0xb7f0x9c7: v9c7b7f = RETURNDATASIZE 
    0xb810x9c7: RETURN v9c7b72, v9c7b7f

    Begin block 0x153c0x9c7
    prev=[0xb6b0x9c7], succ=[]
    =================================
    0x153d0x9c7: v9c7153d = RETURNDATASIZE 
    0x153f0x9c7: REVERT v9c7b72, v9c7153d

    Begin block 0xb660x9c7
    prev=[0xafe0x9c7], succ=[0xb6b0x9c7]
    =================================
    0xb670x9c7: v9c7b67(0x60) = CONST 

}

function allowance(address,address)() public {
    Begin block 0xa25
    prev=[], succ=[0xa2d, 0xa31]
    =================================
    0xa26: va26 = CALLVALUE 
    0xa28: va28 = ISZERO va26
    0xa29: va29(0xa31) = CONST 
    0xa2c: JUMPI va29(0xa31), va28

    Begin block 0xa2d
    prev=[0xa25], succ=[]
    =================================
    0xa2d: va2d(0x0) = CONST 
    0xa30: REVERT va2d(0x0), va2d(0x0)

    Begin block 0xa31
    prev=[0xa25], succ=[0xa44, 0xa48]
    =================================
    0xa33: va33(0x1a76) = CONST 
    0xa36: va36(0x4) = CONST 
    0xa39: va39 = CALLDATASIZE 
    0xa3a: va3a = SUB va39, va36(0x4)
    0xa3b: va3b(0x40) = CONST 
    0xa3e: va3e = LT va3a, va3b(0x40)
    0xa3f: va3f = ISZERO va3e
    0xa40: va40(0xa48) = CONST 
    0xa43: JUMPI va40(0xa48), va3f

    Begin block 0xa44
    prev=[0xa31], succ=[]
    =================================
    0xa44: va44(0x0) = CONST 
    0xa47: REVERT va44(0x0), va44(0x0)

    Begin block 0xa48
    prev=[0xa31], succ=[0x11160xa25]
    =================================
    0xa4a: va4a(0x1) = CONST 
    0xa4c: va4c(0x1) = CONST 
    0xa4e: va4e(0xa0) = CONST 
    0xa50: va50(0x10000000000000000000000000000000000000000) = SHL va4e(0xa0), va4c(0x1)
    0xa51: va51(0xffffffffffffffffffffffffffffffffffffffff) = SUB va50(0x10000000000000000000000000000000000000000), va4a(0x1)
    0xa53: va53 = CALLDATALOAD va36(0x4)
    0xa55: va55 = AND va51(0xffffffffffffffffffffffffffffffffffffffff), va53
    0xa57: va57(0x20) = CONST 
    0xa59: va59(0x24) = ADD va57(0x20), va36(0x4)
    0xa5a: va5a = CALLDATALOAD va59(0x24)
    0xa5b: va5b = AND va5a, va51(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5c: va5c(0x1116) = CONST 
    0xa5f: JUMP va5c(0x1116)

    Begin block 0x11160xa25
    prev=[0xa48], succ=[0x12de0xa25]
    =================================
    0x11170xa25: va251117(0x0) = CONST 
    0x11190xa25: va251119(0x1bae) = CONST 
    0x111c0xa25: va25111c(0x12de) = CONST 
    0x111f0xa25: JUMP va25111c(0x12de)

    Begin block 0x12de0xa25
    prev=[0x11160xa25], succ=[0x13600xa25]
    =================================
    0x12df0xa25: va2512df(0x60) = CONST 
    0x12e10xa25: va2512e1(0x0) = CONST 
    0x12e30xa25: va2512e3 = ADDRESS 
    0x12e40xa25: va2512e4(0x1) = CONST 
    0x12e60xa25: va2512e6(0x1) = CONST 
    0x12e80xa25: va2512e8(0xa0) = CONST 
    0x12ea0xa25: va2512ea(0x10000000000000000000000000000000000000000) = SHL va2512e8(0xa0), va2512e6(0x1)
    0x12eb0xa25: va2512eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB va2512ea(0x10000000000000000000000000000000000000000), va2512e4(0x1)
    0x12ec0xa25: va2512ec = AND va2512eb(0xffffffffffffffffffffffffffffffffffffffff), va2512e3
    0x12ed0xa25: va2512ed(0x0) = CONST 
    0x12ef0xa25: va2512ef = CALLDATASIZE 
    0x12f00xa25: va2512f0(0x40) = CONST 
    0x12f20xa25: va2512f2 = MLOAD va2512f0(0x40)
    0x12f30xa25: va2512f3(0x24) = CONST 
    0x12f50xa25: va2512f5 = ADD va2512f3(0x24), va2512f2
    0x12f80xa25: va2512f8(0x20) = CONST 
    0x12fa0xa25: va2512fa = ADD va2512f8(0x20), va2512f5
    0x12fd0xa25: va2512fd(0x20) = SUB va2512fa, va2512f5
    0x12ff0xa25: MSTORE va2512f5, va2512fd(0x20)
    0x13050xa25: MSTORE va2512fa, va2512ef
    0x13060xa25: va251306(0x20) = CONST 
    0x13080xa25: va251308 = ADD va251306(0x20), va2512fa
    0x130e0xa25: CALLDATACOPY va251308, va2512ed(0x0), va2512ef
    0x130f0xa25: va25130f(0x0) = CONST 
    0x13130xa25: va251313 = ADD va2512ef, va251308
    0x13140xa25: MSTORE va251313, va25130f(0x0)
    0x13150xa25: va251315(0x40) = CONST 
    0x13180xa25: va251318 = MLOAD va251315(0x40)
    0x13190xa25: va251319(0x1f) = CONST 
    0x131d0xa25: va25131d = ADD va2512ef, va251319(0x1f)
    0x131e0xa25: va25131e(0x1f) = CONST 
    0x13200xa25: va251320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT va25131e(0x1f)
    0x13230xa25: va251323 = AND va251320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), va25131d
    0x13260xa25: va251326 = ADD va251308, va251323
    0x13290xa25: va251329 = SUB va251326, va251318
    0x132c0xa25: va25132c = ADD va251320(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), va251329
    0x132e0xa25: MSTORE va251318, va25132c
    0x13310xa25: MSTORE va251315(0x40), va251326
    0x13320xa25: va251332(0x20) = CONST 
    0x13350xa25: va251335 = ADD va251318, va251332(0x20)
    0x13370xa25: va251337 = MLOAD va251335
    0x13380xa25: va251338(0x1) = CONST 
    0x133a0xa25: va25133a(0x1) = CONST 
    0x133c0xa25: va25133c(0xe0) = CONST 
    0x133e0xa25: va25133e(0x100000000000000000000000000000000000000000000000000000000) = SHL va25133c(0xe0), va25133a(0x1)
    0x133f0xa25: va25133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB va25133e(0x100000000000000000000000000000000000000000000000000000000), va251338(0x1)
    0x13400xa25: va251340 = AND va25133f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), va251337
    0x13410xa25: va251341(0x933c1ed) = CONST 
    0x13460xa25: va251346(0xe0) = CONST 
    0x13480xa25: va251348(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL va251346(0xe0), va251341(0x933c1ed)
    0x13490xa25: va251349 = OR va251348(0x933c1ed00000000000000000000000000000000000000000000000000000000), va251340
    0x134b0xa25: MSTORE va251335, va251349
    0x134d0xa25: va25134d = MLOAD va251315(0x40)
    0x134f0xa25: va25134f = MLOAD va251318

    Begin block 0x13600xa25
    prev=[0x13690xa25, 0x12de0xa25], succ=[0x137f0xa25, 0x13690xa25]
    =================================
    0x13600xa25_0x2: v1360a25_2 = PHI va251372, va25134f
    0x13610xa25: va251361(0x20) = CONST 
    0x13640xa25: va251364 = LT v1360a25_2, va251361(0x20)
    0x13650xa25: va251365(0x137f) = CONST 
    0x13680xa25: JUMPI va251365(0x137f), va251364

    Begin block 0x137f0xa25
    prev=[0x13600xa25], succ=[0x13be0xa25, 0x13df0xa25]
    =================================
    0x137f0xa25_0x0: v137fa25_0 = PHI va25137a, va251335
    0x137f0xa25_0x1: v137fa25_1 = PHI va251378, va25134d
    0x137f0xa25_0x2: v137fa25_2 = PHI va251372, va25134f
    0x13800xa25: va251380(0x1) = CONST 
    0x13830xa25: va251383(0x20) = CONST 
    0x13850xa25: va251385 = SUB va251383(0x20), v137fa25_2
    0x13860xa25: va251386(0x100) = CONST 
    0x13890xa25: va251389 = EXP va251386(0x100), va251385
    0x138a0xa25: va25138a = SUB va251389, va251380(0x1)
    0x138c0xa25: va25138c = NOT va25138a
    0x138e0xa25: va25138e = MLOAD v137fa25_0
    0x138f0xa25: va25138f = AND va25138e, va25138c
    0x13920xa25: va251392 = MLOAD v137fa25_1
    0x13930xa25: va251393 = AND va251392, va25138a
    0x13960xa25: va251396 = OR va25138f, va251393
    0x13980xa25: MSTORE v137fa25_1, va251396
    0x13a10xa25: va2513a1 = ADD va25134f, va25134d
    0x13a50xa25: va2513a5(0x0) = CONST 
    0x13a70xa25: va2513a7(0x40) = CONST 
    0x13a90xa25: va2513a9 = MLOAD va2513a7(0x40)
    0x13ac0xa25: va2513ac = SUB va2513a1, va2513a9
    0x13af0xa25: va2513af = GAS 
    0x13b00xa25: va2513b0 = STATICCALL va2513af, va2512ec, va2513a9, va2513ac, va2513a9, va2513a5(0x0)
    0x13b40xa25: va2513b4 = RETURNDATASIZE 
    0x13b60xa25: va2513b6(0x0) = CONST 
    0x13b90xa25: va2513b9 = EQ va2513b4, va2513b6(0x0)
    0x13ba0xa25: va2513ba(0x13df) = CONST 
    0x13bd0xa25: JUMPI va2513ba(0x13df), va2513b9

    Begin block 0x13be0xa25
    prev=[0x137f0xa25], succ=[0x13e40xa25]
    =================================
    0x13be0xa25: va2513be(0x40) = CONST 
    0x13c00xa25: va2513c0 = MLOAD va2513be(0x40)
    0x13c30xa25: va2513c3(0x1f) = CONST 
    0x13c50xa25: va2513c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT va2513c3(0x1f)
    0x13c60xa25: va2513c6(0x3f) = CONST 
    0x13c80xa25: va2513c8 = RETURNDATASIZE 
    0x13c90xa25: va2513c9 = ADD va2513c8, va2513c6(0x3f)
    0x13ca0xa25: va2513ca = AND va2513c9, va2513c5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13cc0xa25: va2513cc = ADD va2513c0, va2513ca
    0x13cd0xa25: va2513cd(0x40) = CONST 
    0x13cf0xa25: MSTORE va2513cd(0x40), va2513cc
    0x13d00xa25: va2513d0 = RETURNDATASIZE 
    0x13d20xa25: MSTORE va2513c0, va2513d0
    0x13d30xa25: va2513d3 = RETURNDATASIZE 
    0x13d40xa25: va2513d4(0x0) = CONST 
    0x13d60xa25: va2513d6(0x20) = CONST 
    0x13d90xa25: va2513d9 = ADD va2513c0, va2513d6(0x20)
    0x13da0xa25: RETURNDATACOPY va2513d9, va2513d4(0x0), va2513d3
    0x13db0xa25: va2513db(0x13e4) = CONST 
    0x13de0xa25: JUMP va2513db(0x13e4)

    Begin block 0x13e40xa25
    prev=[0x13be0xa25, 0x13df0xa25], succ=[0x13f80xa25, 0x155f0xa25]
    =================================
    0x13e90xa25: va2513e9(0x40) = CONST 
    0x13eb0xa25: va2513eb = MLOAD va2513e9(0x40)
    0x13ec0xa25: va2513ec = RETURNDATASIZE 
    0x13ed0xa25: va2513ed(0x0) = CONST 
    0x13f00xa25: RETURNDATACOPY va2513eb, va2513ed(0x0), va2513ec
    0x13f30xa25: va2513f3 = ISZERO va2513b0
    0x13f40xa25: va2513f4(0x155f) = CONST 
    0x13f70xa25: JUMPI va2513f4(0x155f), va2513f3

    Begin block 0x13f80xa25
    prev=[0x13e40xa25], succ=[]
    =================================
    0x13f80xa25: va2513f8(0x40) = CONST 
    0x13fa0xa25: va2513fa = RETURNDATASIZE 
    0x13fb0xa25: va2513fb = SUB va2513fa, va2513f8(0x40)
    0x13fc0xa25: va2513fc(0x40) = CONST 
    0x13ff0xa25: va2513ff = ADD va2513eb, va2513fc(0x40)
    0x14000xa25: RETURN va2513ff, va2513fb

    Begin block 0x155f0xa25
    prev=[0x13e40xa25], succ=[]
    =================================
    0x15600xa25: va251560 = RETURNDATASIZE 
    0x15620xa25: REVERT va2513eb, va251560

    Begin block 0x13df0xa25
    prev=[0x137f0xa25], succ=[0x13e40xa25]
    =================================
    0x13e00xa25: va2513e0(0x60) = CONST 

    Begin block 0x13690xa25
    prev=[0x13600xa25], succ=[0x13600xa25]
    =================================
    0x13690xa25_0x0: v1369a25_0 = PHI va25137a, va251335
    0x13690xa25_0x1: v1369a25_1 = PHI va251378, va25134d
    0x13690xa25_0x2: v1369a25_2 = PHI va251372, va25134f
    0x136a0xa25: va25136a = MLOAD v1369a25_0
    0x136c0xa25: MSTORE v1369a25_1, va25136a
    0x136d0xa25: va25136d(0x1f) = CONST 
    0x136f0xa25: va25136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT va25136d(0x1f)
    0x13720xa25: va251372 = ADD v1369a25_2, va25136f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x13740xa25: va251374(0x20) = CONST 
    0x13780xa25: va251378 = ADD va251374(0x20), v1369a25_1
    0x137a0xa25: va25137a = ADD va251374(0x20), v1369a25_0
    0x137b0xa25: va25137b(0x1360) = CONST 
    0x137e0xa25: JUMP va25137b(0x1360)

}

function DELEGATION_TYPEHASH()() public {
    Begin block 0xa60
    prev=[], succ=[0xa68, 0xa6c]
    =================================
    0xa61: va61 = CALLVALUE 
    0xa63: va63 = ISZERO va61
    0xa64: va64(0xa6c) = CONST 
    0xa67: JUMPI va64(0xa6c), va63

    Begin block 0xa68
    prev=[0xa60], succ=[]
    =================================
    0xa68: va68(0x0) = CONST 
    0xa6b: REVERT va68(0x0), va68(0x0)

    Begin block 0xa6c
    prev=[0xa60], succ=[0x11c2]
    =================================
    0xa6e: va6e(0x1aa7) = CONST 
    0xa71: va71(0x11c2) = CONST 
    0xa74: JUMP va71(0x11c2)

    Begin block 0x11c2
    prev=[0xa6c], succ=[0x1aa7]
    =================================
    0x11c3: v11c3(0x40) = CONST 
    0x11c5: v11c5 = MLOAD v11c3(0x40)
    0x11c7: v11c7(0x3a) = CONST 
    0x11c9: v11c9(0x14af) = CONST 
    0x11cd: CODECOPY v11c5, v11c9(0x14af), v11c7(0x3a)
    0x11ce: v11ce(0x3a) = CONST 
    0x11d0: v11d0 = ADD v11ce(0x3a), v11c5
    0x11d3: v11d3(0x40) = CONST 
    0x11d5: v11d5 = MLOAD v11d3(0x40)
    0x11d8: v11d8(0x3a) = SUB v11d0, v11d5
    0x11da: v11da = SHA3 v11d5, v11d8(0x3a)
    0x11dc: JUMP va6e(0x1aa7)

    Begin block 0x1aa7
    prev=[0x11c2], succ=[]
    =================================
    0x1aa8: v1aa8(0x40) = CONST 
    0x1aab: v1aab = MLOAD v1aa8(0x40)
    0x1aae: MSTORE v1aab, v11da
    0x1aaf: v1aaf = MLOAD v1aa8(0x40)
    0x1ab3: v1ab3(0x0) = SUB v1aab, v1aaf
    0x1ab4: v1ab4(0x20) = CONST 
    0x1ab6: v1ab6(0x20) = ADD v1ab4(0x20), v1ab3(0x0)
    0x1ab8: RETURN v1aaf, v1ab6(0x20)

}

function yuansScalingFactor()() public {
    Begin block 0xa75
    prev=[], succ=[0xa7d, 0xa81]
    =================================
    0xa76: va76 = CALLVALUE 
    0xa78: va78 = ISZERO va76
    0xa79: va79(0xa81) = CONST 
    0xa7c: JUMPI va79(0xa81), va78

    Begin block 0xa7d
    prev=[0xa75], succ=[]
    =================================
    0xa7d: va7d(0x0) = CONST 
    0xa80: REVERT va7d(0x0), va7d(0x0)

    Begin block 0xa81
    prev=[0xa75], succ=[0x11dd]
    =================================
    0xa83: va83(0x1ad8) = CONST 
    0xa86: va86(0x11dd) = CONST 
    0xa89: JUMP va86(0x11dd)

    Begin block 0x11dd
    prev=[0xa81], succ=[0x1ad8]
    =================================
    0x11de: v11de(0x9) = CONST 
    0x11e0: v11e0 = SLOAD v11de(0x9)
    0x11e2: JUMP va83(0x1ad8)

    Begin block 0x1ad8
    prev=[0x11dd], succ=[]
    =================================
    0x1ad9: v1ad9(0x40) = CONST 
    0x1adc: v1adc = MLOAD v1ad9(0x40)
    0x1adf: MSTORE v1adc, v11e0
    0x1ae0: v1ae0 = MLOAD v1ad9(0x40)
    0x1ae4: v1ae4(0x0) = SUB v1adc, v1ae0
    0x1ae5: v1ae5(0x20) = CONST 
    0x1ae7: v1ae7(0x20) = ADD v1ae5(0x20), v1ae4(0x0)
    0x1ae9: RETURN v1ae0, v1ae7(0x20)

}

function BASE()() public {
    Begin block 0xa8a
    prev=[], succ=[0xa92, 0xa96]
    =================================
    0xa8b: va8b = CALLVALUE 
    0xa8d: va8d = ISZERO va8b
    0xa8e: va8e(0xa96) = CONST 
    0xa91: JUMPI va8e(0xa96), va8d

    Begin block 0xa92
    prev=[0xa8a], succ=[]
    =================================
    0xa92: va92(0x0) = CONST 
    0xa95: REVERT va92(0x0), va92(0x0)

    Begin block 0xa96
    prev=[0xa8a], succ=[0x11e3]
    =================================
    0xa98: va98(0x1b09) = CONST 
    0xa9b: va9b(0x11e3) = CONST 
    0xa9e: JUMP va9b(0x11e3)

    Begin block 0x11e3
    prev=[0xa96], succ=[0x1b09]
    =================================
    0x11e4: v11e4(0xde0b6b3a7640000) = CONST 
    0x11ee: JUMP va98(0x1b09)

    Begin block 0x1b09
    prev=[0x11e3], succ=[]
    =================================
    0x1b0a: v1b0a(0x40) = CONST 
    0x1b0d: v1b0d = MLOAD v1b0a(0x40)
    0x1b10: MSTORE v1b0d, v11e4(0xde0b6b3a7640000)
    0x1b11: v1b11 = MLOAD v1b0a(0x40)
    0x1b15: v1b15(0x0) = SUB v1b0d, v1b11
    0x1b16: v1b16(0x20) = CONST 
    0x1b18: v1b18(0x20) = ADD v1b16(0x20), v1b15(0x0)
    0x1b1a: RETURN v1b11, v1b18(0x20)

}

function checkpoints(address,uint32)() public {
    Begin block 0xa9f
    prev=[], succ=[0xaa7, 0xaab]
    =================================
    0xaa0: vaa0 = CALLVALUE 
    0xaa2: vaa2 = ISZERO vaa0
    0xaa3: vaa3(0xaab) = CONST 
    0xaa6: JUMPI vaa3(0xaab), vaa2

    Begin block 0xaa7
    prev=[0xa9f], succ=[]
    =================================
    0xaa7: vaa7(0x0) = CONST 
    0xaaa: REVERT vaa7(0x0), vaa7(0x0)

    Begin block 0xaab
    prev=[0xa9f], succ=[0xabe, 0xac2]
    =================================
    0xaad: vaad(0xade) = CONST 
    0xab0: vab0(0x4) = CONST 
    0xab3: vab3 = CALLDATASIZE 
    0xab4: vab4 = SUB vab3, vab0(0x4)
    0xab5: vab5(0x40) = CONST 
    0xab8: vab8 = LT vab4, vab5(0x40)
    0xab9: vab9 = ISZERO vab8
    0xaba: vaba(0xac2) = CONST 
    0xabd: JUMPI vaba(0xac2), vab9

    Begin block 0xabe
    prev=[0xaab], succ=[]
    =================================
    0xabe: vabe(0x0) = CONST 
    0xac1: REVERT vabe(0x0), vabe(0x0)

    Begin block 0xac2
    prev=[0xaab], succ=[0x11ef]
    =================================
    0xac5: vac5 = CALLDATALOAD vab0(0x4)
    0xac6: vac6(0x1) = CONST 
    0xac8: vac8(0x1) = CONST 
    0xaca: vaca(0xa0) = CONST 
    0xacc: vacc(0x10000000000000000000000000000000000000000) = SHL vaca(0xa0), vac8(0x1)
    0xacd: vacd(0xffffffffffffffffffffffffffffffffffffffff) = SUB vacc(0x10000000000000000000000000000000000000000), vac6(0x1)
    0xace: vace = AND vacd(0xffffffffffffffffffffffffffffffffffffffff), vac5
    0xad0: vad0(0x20) = CONST 
    0xad2: vad2(0x24) = ADD vad0(0x20), vab0(0x4)
    0xad3: vad3 = CALLDATALOAD vad2(0x24)
    0xad4: vad4(0xffffffff) = CONST 
    0xad9: vad9 = AND vad4(0xffffffff), vad3
    0xada: vada(0x11ef) = CONST 
    0xadd: JUMP vada(0x11ef)

    Begin block 0x11ef
    prev=[0xac2], succ=[0xade]
    =================================
    0x11f0: v11f0(0xf) = CONST 
    0x11f2: v11f2(0x20) = CONST 
    0x11f6: MSTORE v11f2(0x20), v11f0(0xf)
    0x11f7: v11f7(0x0) = CONST 
    0x11fb: MSTORE v11f7(0x0), vace
    0x11fc: v11fc(0x40) = CONST 
    0x1200: v1200 = SHA3 v11f7(0x0), v11fc(0x40)
    0x1203: MSTORE v11f2(0x20), v1200
    0x1206: MSTORE v11f7(0x0), vad9
    0x1208: v1208 = SHA3 v11f7(0x0), v11fc(0x40)
    0x120a: v120a = SLOAD v1208
    0x120b: v120b(0x1) = CONST 
    0x120f: v120f = ADD v1208, v120b(0x1)
    0x1210: v1210 = SLOAD v120f
    0x1211: v1211(0xffffffff) = CONST 
    0x1218: v1218 = AND v120a, v1211(0xffffffff)
    0x121b: JUMP vaad(0xade)

    Begin block 0xade
    prev=[0x11ef], succ=[]
    =================================
    0xadf: vadf(0x40) = CONST 
    0xae2: vae2 = MLOAD vadf(0x40)
    0xae3: vae3(0xffffffff) = CONST 
    0xaea: vaea = AND v1218, vae3(0xffffffff)
    0xaec: MSTORE vae2, vaea
    0xaed: vaed(0x20) = CONST 
    0xaf0: vaf0 = ADD vae2, vaed(0x20)
    0xaf4: MSTORE vaf0, v1210
    0xaf6: vaf6 = MLOAD vadf(0x40)
    0xafa: vafa(0x0) = SUB vae2, vaf6
    0xafb: vafb(0x40) = ADD vafa(0x0), vadf(0x40)
    0xafd: RETURN vaf6, vafb(0x40)

}

function 0xb86(0xb86arg0x0) private {
    Begin block 0xb86
    prev=[], succ=[0x1b3a, 0xbc5]
    =================================
    0xb87: vb87(0x1) = CONST 
    0xb8a: vb8a = SLOAD vb87(0x1)
    0xb8b: vb8b(0x40) = CONST 
    0xb8e: vb8e = MLOAD vb8b(0x40)
    0xb8f: vb8f(0x20) = CONST 
    0xb91: vb91(0x2) = CONST 
    0xb95: vb95 = AND vb87(0x1), vb8a
    0xb96: vb96 = ISZERO vb95
    0xb97: vb97(0x100) = CONST 
    0xb9a: vb9a = MUL vb97(0x100), vb96
    0xb9b: vb9b(0x0) = CONST 
    0xb9d: vb9d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vb9b(0x0)
    0xb9e: vb9e = ADD vb9d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vb9a
    0xba1: vba1 = AND vb8a, vb9e
    0xba5: vba5 = DIV vba1, vb91(0x2)
    0xba6: vba6(0x1f) = CONST 
    0xba9: vba9 = ADD vba5, vba6(0x1f)
    0xbac: vbac = DIV vba9, vb8f(0x20)
    0xbae: vbae = MUL vb8f(0x20), vbac
    0xbb0: vbb0 = ADD vb8e, vbae
    0xbb2: vbb2 = ADD vb8f(0x20), vbb0
    0xbb5: MSTORE vb8b(0x40), vbb2
    0xbb8: MSTORE vb8e, vba5
    0xbbc: vbbc = ADD vb8e, vb8f(0x20)
    0xbc0: vbc0 = ISZERO vba5
    0xbc1: vbc1(0x1b3a) = CONST 
    0xbc4: JUMPI vbc1(0x1b3a), vbc0

    Begin block 0x1b3a
    prev=[0xb86], succ=[]
    =================================
    0x1b41: RETURNPRIVATE vb86arg0, vb8e, vb86arg0

    Begin block 0xbc5
    prev=[0xb86], succ=[0xbcd, 0xbe00xb86]
    =================================
    0xbc6: vbc6(0x1f) = CONST 
    0xbc8: vbc8 = LT vbc6(0x1f), vba5
    0xbc9: vbc9(0xbe0) = CONST 
    0xbcc: JUMPI vbc9(0xbe0), vbc8

    Begin block 0xbcd
    prev=[0xbc5], succ=[0x1b61]
    =================================
    0xbcd: vbcd(0x100) = CONST 
    0xbd2: vbd2 = SLOAD vb87(0x1)
    0xbd3: vbd3 = DIV vbd2, vbcd(0x100)
    0xbd4: vbd4 = MUL vbd3, vbcd(0x100)
    0xbd6: MSTORE vbbc, vbd4
    0xbd8: vbd8(0x20) = CONST 
    0xbda: vbda = ADD vbd8(0x20), vbbc
    0xbdc: vbdc(0x1b61) = CONST 
    0xbdf: JUMP vbdc(0x1b61)

    Begin block 0x1b61
    prev=[0xbcd], succ=[]
    =================================
    0x1b68: RETURNPRIVATE vb86arg0, vb8e, vb86arg0

    Begin block 0xbe00xb86
    prev=[0xbc5], succ=[0xbee0xb86]
    =================================
    0xbe20xb86: vb86be2 = ADD vbbc, vba5
    0xbe50xb86: vb86be5(0x0) = CONST 
    0xbe70xb86: MSTORE vb86be5(0x0), vb87(0x1)
    0xbe80xb86: vb86be8(0x20) = CONST 
    0xbea0xb86: vb86bea(0x0) = CONST 
    0xbec0xb86: vb86bec = SHA3 vb86bea(0x0), vb86be8(0x20)

    Begin block 0xbee0xb86
    prev=[0xbee0xb86, 0xbe00xb86], succ=[0xbee0xb86, 0xc020xb86]
    =================================
    0xbee0xb86_0x0: vbeeb86_0 = PHI vbbc, vb86bfa
    0xbee0xb86_0x1: vbeeb86_1 = PHI vb86bf6, vb86bec
    0xbf00xb86: vb86bf0 = SLOAD vbeeb86_1
    0xbf20xb86: MSTORE vbeeb86_0, vb86bf0
    0xbf40xb86: vb86bf4(0x1) = CONST 
    0xbf60xb86: vb86bf6 = ADD vb86bf4(0x1), vbeeb86_1
    0xbf80xb86: vb86bf8(0x20) = CONST 
    0xbfa0xb86: vb86bfa = ADD vb86bf8(0x20), vbeeb86_0
    0xbfd0xb86: vb86bfd = GT vb86be2, vb86bfa
    0xbfe0xb86: vb86bfe(0xbee) = CONST 
    0xc010xb86: JUMPI vb86bfe(0xbee), vb86bfd

    Begin block 0xc020xb86
    prev=[0xbee0xb86], succ=[0xc0b0xb86]
    =================================
    0xc040xb86: vb86c04 = SUB vb86bfa, vb86be2
    0xc050xb86: vb86c05(0x1f) = CONST 
    0xc070xb86: vb86c07 = AND vb86c05(0x1f), vb86c04
    0xc090xb86: vb86c09 = ADD vb86be2, vb86c07

    Begin block 0xc0b0xb86
    prev=[0xc020xb86], succ=[]
    =================================
    0xc120xb86: RETURNPRIVATE vb86arg0, vb8e, vb86arg0

}

