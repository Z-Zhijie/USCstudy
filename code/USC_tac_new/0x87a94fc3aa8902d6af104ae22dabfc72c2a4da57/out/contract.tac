function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x1b27]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x1acd: v1acd(0x1b27) = CONST 
    0x1ace: JUMPI v1acd(0x1b27), v8

    Begin block 0xd
    prev=[0x0], succ=[0x144, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5c60da1b) = CONST 
    0x19: v19 = GT v14(0x5c60da1b), v12
    0x1a: v1a(0x144) = CONST 
    0x1d: JUMPI v1a(0x144), v19

    Begin block 0x144
    prev=[0xd], succ=[0x1dd, 0x150]
    =================================
    0x146: v146(0x313ce567) = CONST 
    0x14b: v14b = GT v146(0x313ce567), v12
    0x14c: v14c(0x1dd) = CONST 
    0x14f: JUMPI v14c(0x1dd), v14b

    Begin block 0x1dd
    prev=[0x144], succ=[0x22f, 0x1e9]
    =================================
    0x1df: v1df(0x12d43a51) = CONST 
    0x1e4: v1e4 = GT v1df(0x12d43a51), v12
    0x1e5: v1e5(0x22f) = CONST 
    0x1e8: JUMPI v1e5(0x22f), v1e4

    Begin block 0x22f
    prev=[0x1dd], succ=[0x1b2a, 0x23b]
    =================================
    0x231: v231(0x6fdde03) = CONST 
    0x236: v236 = EQ v231(0x6fdde03), v12
    0x1b1d: v1b1d(0x1b2a) = CONST 
    0x1b1e: JUMPI v1b1d(0x1b2a), v236

    Begin block 0x1b2a
    prev=[0x22f], succ=[]
    =================================
    0x1b2b: v1b2b(0x2af) = CONST 
    0x1b2c: CALLPRIVATE v1b2b(0x2af)

    Begin block 0x23b
    prev=[0x22f], succ=[0x1b2d, 0x246]
    =================================
    0x23c: v23c(0x933c1ed) = CONST 
    0x241: v241 = EQ v23c(0x933c1ed), v12
    0x1b1f: v1b1f(0x1b2d) = CONST 
    0x1b20: JUMPI v1b1f(0x1b2d), v241

    Begin block 0x1b2d
    prev=[0x23b], succ=[]
    =================================
    0x1b2e: v1b2e(0x339) = CONST 
    0x1b2f: CALLPRIVATE v1b2e(0x339)

    Begin block 0x246
    prev=[0x23b], succ=[0x1b30, 0x251]
    =================================
    0x247: v247(0x95ea7b3) = CONST 
    0x24c: v24c = EQ v247(0x95ea7b3), v12
    0x1b21: v1b21(0x1b30) = CONST 
    0x1b22: JUMPI v1b21(0x1b30), v24c

    Begin block 0x1b30
    prev=[0x86, 0x91, 0x1b8, 0x1ce, 0x246], succ=[]
    =================================
    0x1b31: v1b31(0x3ea) = CONST 
    0x1b32: CALLPRIVATE v1b31(0x3ea)

    Begin block 0x251
    prev=[0x246], succ=[0x1b33, 0x25c]
    =================================
    0x252: v252(0x11d3e6c4) = CONST 
    0x257: v257 = EQ v252(0x11d3e6c4), v12
    0x1b23: v1b23(0x1b33) = CONST 
    0x1b24: JUMPI v1b23(0x1b33), v257

    Begin block 0x1b33
    prev=[0x251], succ=[]
    =================================
    0x1b34: v1b34(0x437) = CONST 
    0x1b35: CALLPRIVATE v1b34(0x437)

    Begin block 0x25c
    prev=[0x251], succ=[0x1b27, 0x1b36]
    =================================
    0x25d: v25d(0x11fd8a83) = CONST 
    0x262: v262 = EQ v25d(0x11fd8a83), v12
    0x1b25: v1b25(0x1b36) = CONST 
    0x1b26: JUMPI v1b25(0x1b36), v262

    Begin block 0x1b27
    prev=[0x0, 0x25c], succ=[]
    =================================
    0x1b28: v1b28(0x267) = CONST 
    0x1b29: CALLPRIVATE v1b28(0x267)

    Begin block 0x1b36
    prev=[0x25c], succ=[]
    =================================
    0x1b37: v1b37(0x45e) = CONST 
    0x1b38: CALLPRIVATE v1b37(0x45e)

    Begin block 0x1e9
    prev=[0x1dd], succ=[0x1b39, 0x1f4]
    =================================
    0x1ea: v1ea(0x12d43a51) = CONST 
    0x1ef: v1ef = EQ v1ea(0x12d43a51), v12
    0x1b11: v1b11(0x1b39) = CONST 
    0x1b12: JUMPI v1b11(0x1b39), v1ef

    Begin block 0x1b39
    prev=[0x1e9], succ=[]
    =================================
    0x1b3a: v1b3a(0x48f) = CONST 
    0x1b3b: CALLPRIVATE v1b3a(0x48f)

    Begin block 0x1f4
    prev=[0x1e9], succ=[0x1b3c, 0x1ff]
    =================================
    0x1f5: v1f5(0x18160ddd) = CONST 
    0x1fa: v1fa = EQ v1f5(0x18160ddd), v12
    0x1b13: v1b13(0x1b3c) = CONST 
    0x1b14: JUMPI v1b13(0x1b3c), v1fa

    Begin block 0x1b3c
    prev=[0x1f4], succ=[]
    =================================
    0x1b3d: v1b3d(0x4a4) = CONST 
    0x1b3e: CALLPRIVATE v1b3d(0x4a4)

    Begin block 0x1ff
    prev=[0x1f4], succ=[0x1b3f, 0x20a]
    =================================
    0x200: v200(0x1e7f9f36) = CONST 
    0x205: v205 = EQ v200(0x1e7f9f36), v12
    0x1b15: v1b15(0x1b3f) = CONST 
    0x1b16: JUMPI v1b15(0x1b3f), v205

    Begin block 0x1b3f
    prev=[0x1ff], succ=[]
    =================================
    0x1b40: v1b40(0x4b9) = CONST 
    0x1b41: CALLPRIVATE v1b40(0x4b9)

    Begin block 0x20a
    prev=[0x1ff], succ=[0x1b42, 0x215]
    =================================
    0x20b: v20b(0x20606b70) = CONST 
    0x210: v210 = EQ v20b(0x20606b70), v12
    0x1b17: v1b17(0x1b42) = CONST 
    0x1b18: JUMPI v1b17(0x1b42), v210

    Begin block 0x1b42
    prev=[0x20a], succ=[]
    =================================
    0x1b43: v1b43(0x4e3) = CONST 
    0x1b44: CALLPRIVATE v1b43(0x4e3)

    Begin block 0x215
    prev=[0x20a], succ=[0x1b45, 0x220]
    =================================
    0x216: v216(0x23b872dd) = CONST 
    0x21b: v21b = EQ v216(0x23b872dd), v12
    0x1b19: v1b19(0x1b45) = CONST 
    0x1b1a: JUMPI v1b19(0x1b45), v21b

    Begin block 0x1b45
    prev=[0x215], succ=[]
    =================================
    0x1b46: v1b46(0x4f8) = CONST 
    0x1b47: CALLPRIVATE v1b46(0x4f8)

    Begin block 0x220
    prev=[0x215], succ=[0x22b, 0x1b48]
    =================================
    0x221: v221(0x25240810) = CONST 
    0x226: v226 = EQ v221(0x25240810), v12
    0x1b1b: v1b1b(0x1b48) = CONST 
    0x1b1c: JUMPI v1b1b(0x1b48), v226

    Begin block 0x22b
    prev=[0x220], succ=[]
    =================================
    0x22b: v22b(0x267) = CONST 
    0x22e: JUMP v22b(0x267)

    Begin block 0x1b48
    prev=[0x220], succ=[]
    =================================
    0x1b49: v1b49(0x53b) = CONST 
    0x1b4a: CALLPRIVATE v1b49(0x53b)

    Begin block 0x150
    prev=[0x144], succ=[0x1a1, 0x15b]
    =================================
    0x151: v151(0x4487152f) = CONST 
    0x156: v156 = GT v151(0x4487152f), v12
    0x157: v157(0x1a1) = CONST 
    0x15a: JUMPI v157(0x1a1), v156

    Begin block 0x1a1
    prev=[0x150], succ=[0x1b4b, 0x1ad]
    =================================
    0x1a3: v1a3(0x313ce567) = CONST 
    0x1a8: v1a8 = EQ v1a3(0x313ce567), v12
    0x1b07: v1b07(0x1b4b) = CONST 
    0x1b08: JUMPI v1b07(0x1b4b), v1a8

    Begin block 0x1b4b
    prev=[0x1a1], succ=[]
    =================================
    0x1b4c: v1b4c(0x550) = CONST 
    0x1b4d: CALLPRIVATE v1b4c(0x550)

    Begin block 0x1ad
    prev=[0x1a1], succ=[0x1b4e, 0x1b8]
    =================================
    0x1ae: v1ae(0x3218b99d) = CONST 
    0x1b3: v1b3 = EQ v1ae(0x3218b99d), v12
    0x1b09: v1b09(0x1b4e) = CONST 
    0x1b0a: JUMPI v1b09(0x1b4e), v1b3

    Begin block 0x1b4e
    prev=[0x1ad], succ=[]
    =================================
    0x1b4f: v1b4f(0x57b) = CONST 
    0x1b50: CALLPRIVATE v1b4f(0x57b)

    Begin block 0x1b8
    prev=[0x1ad], succ=[0x1b30, 0x1c3]
    =================================
    0x1b9: v1b9(0x39509351) = CONST 
    0x1be: v1be = EQ v1b9(0x39509351), v12
    0x1b0b: v1b0b(0x1b30) = CONST 
    0x1b0c: JUMPI v1b0b(0x1b30), v1be

    Begin block 0x1c3
    prev=[0x1b8], succ=[0x1b51, 0x1ce]
    =================================
    0x1c4: v1c4(0x3af9e669) = CONST 
    0x1c9: v1c9 = EQ v1c4(0x3af9e669), v12
    0x1b0d: v1b0d(0x1b51) = CONST 
    0x1b0e: JUMPI v1b0d(0x1b51), v1c9

    Begin block 0x1b51
    prev=[0x9c, 0x135, 0x1c3], succ=[]
    =================================
    0x1b52: v1b52(0x590) = CONST 
    0x1b53: CALLPRIVATE v1b52(0x590)

    Begin block 0x1ce
    prev=[0x1c3], succ=[0x1d9, 0x1b30]
    =================================
    0x1cf: v1cf(0x40c10f19) = CONST 
    0x1d4: v1d4 = EQ v1cf(0x40c10f19), v12
    0x1b0f: v1b0f(0x1b30) = CONST 
    0x1b10: JUMPI v1b0f(0x1b30), v1d4

    Begin block 0x1d9
    prev=[0x1ce], succ=[]
    =================================
    0x1d9: v1d9(0x267) = CONST 
    0x1dc: JUMP v1d9(0x267)

    Begin block 0x15b
    prev=[0x150], succ=[0x1b54, 0x166]
    =================================
    0x15c: v15c(0x4487152f) = CONST 
    0x161: v161 = EQ v15c(0x4487152f), v12
    0x1afb: v1afb(0x1b54) = CONST 
    0x1afc: JUMPI v1afb(0x1b54), v161

    Begin block 0x1b54
    prev=[0x15b], succ=[]
    =================================
    0x1b55: v1b55(0x5c3) = CONST 
    0x1b56: CALLPRIVATE v1b55(0x5c3)

    Begin block 0x166
    prev=[0x15b], succ=[0x1b57, 0x171]
    =================================
    0x167: v167(0x4bda2e20) = CONST 
    0x16c: v16c = EQ v167(0x4bda2e20), v12
    0x1afd: v1afd(0x1b57) = CONST 
    0x1afe: JUMPI v1afd(0x1b57), v16c

    Begin block 0x1b57
    prev=[0x166], succ=[]
    =================================
    0x1b58: v1b58(0x674) = CONST 
    0x1b59: CALLPRIVATE v1b58(0x674)

    Begin block 0x171
    prev=[0x166], succ=[0x1b5a, 0x17c]
    =================================
    0x172: v172(0x555bcc40) = CONST 
    0x177: v177 = EQ v172(0x555bcc40), v12
    0x1aff: v1aff(0x1b5a) = CONST 
    0x1b00: JUMPI v1aff(0x1b5a), v177

    Begin block 0x1b5a
    prev=[0x171], succ=[]
    =================================
    0x1b5b: v1b5b(0x68b) = CONST 
    0x1b5c: CALLPRIVATE v1b5b(0x68b)

    Begin block 0x17c
    prev=[0x171], succ=[0x1b5d, 0x187]
    =================================
    0x17d: v17d(0x56a9fb88) = CONST 
    0x182: v182 = EQ v17d(0x56a9fb88), v12
    0x1b01: v1b01(0x1b5d) = CONST 
    0x1b02: JUMPI v1b01(0x1b5d), v182

    Begin block 0x1b5d
    prev=[0x17c], succ=[]
    =================================
    0x1b5e: v1b5e(0x753) = CONST 
    0x1b5f: CALLPRIVATE v1b5e(0x753)

    Begin block 0x187
    prev=[0x17c], succ=[0x1b60, 0x192]
    =================================
    0x188: v188(0x587cde1e) = CONST 
    0x18d: v18d = EQ v188(0x587cde1e), v12
    0x1b03: v1b03(0x1b60) = CONST 
    0x1b04: JUMPI v1b03(0x1b60), v18d

    Begin block 0x1b60
    prev=[0x187], succ=[]
    =================================
    0x1b61: v1b61(0x768) = CONST 
    0x1b62: CALLPRIVATE v1b61(0x768)

    Begin block 0x192
    prev=[0x187], succ=[0x19d, 0x1b63]
    =================================
    0x193: v193(0x5c19a95c) = CONST 
    0x198: v198 = EQ v193(0x5c19a95c), v12
    0x1b05: v1b05(0x1b63) = CONST 
    0x1b06: JUMPI v1b05(0x1b63), v198

    Begin block 0x19d
    prev=[0x192], succ=[]
    =================================
    0x19d: v19d(0x267) = CONST 
    0x1a0: JUMP v19d(0x267)

    Begin block 0x1b63
    prev=[0x7a, 0x6b, 0xc2, 0x192], succ=[]
    =================================
    0x1b64: v1b64(0x78b) = CONST 
    0x1b65: CALLPRIVATE v1b64(0x78b)

    Begin block 0x1e
    prev=[0xd], succ=[0xb6, 0x29]
    =================================
    0x1f: v1f(0x98dca210) = CONST 
    0x24: v24 = GT v1f(0x98dca210), v12
    0x25: v25(0xb6) = CONST 
    0x28: JUMPI v25(0xb6), v24

    Begin block 0xb6
    prev=[0x1e], succ=[0x108, 0xc2]
    =================================
    0xb8: vb8(0x73f03dff) = CONST 
    0xbd: vbd = GT vb8(0x73f03dff), v12
    0xbe: vbe(0x108) = CONST 
    0xc1: JUMPI vbe(0x108), vbd

    Begin block 0x108
    prev=[0xb6], succ=[0x1b66, 0x114]
    =================================
    0x10a: v10a(0x5c60da1b) = CONST 
    0x10f: v10f = EQ v10a(0x5c60da1b), v12
    0x1af1: v1af1(0x1b66) = CONST 
    0x1af2: JUMPI v1af1(0x1b66), v10f

    Begin block 0x1b66
    prev=[0x108], succ=[]
    =================================
    0x1b67: v1b67(0x7be) = CONST 
    0x1b68: CALLPRIVATE v1b67(0x7be)

    Begin block 0x114
    prev=[0x108], succ=[0x1b69, 0x11f]
    =================================
    0x115: v115(0x64dd48f5) = CONST 
    0x11a: v11a = EQ v115(0x64dd48f5), v12
    0x1af3: v1af3(0x1b69) = CONST 
    0x1af4: JUMPI v1af3(0x1b69), v11a

    Begin block 0x1b69
    prev=[0x114], succ=[]
    =================================
    0x1b6a: v1b6a(0x7d3) = CONST 
    0x1b6b: CALLPRIVATE v1b6a(0x7d3)

    Begin block 0x11f
    prev=[0x114], succ=[0x1b6c, 0x12a]
    =================================
    0x120: v120(0x6fc6407c) = CONST 
    0x125: v125 = EQ v120(0x6fc6407c), v12
    0x1af5: v1af5(0x1b6c) = CONST 
    0x1af6: JUMPI v1af5(0x1b6c), v125

    Begin block 0x1b6c
    prev=[0x11f], succ=[]
    =================================
    0x1b6d: v1b6d(0x7e8) = CONST 
    0x1b6e: CALLPRIVATE v1b6d(0x7e8)

    Begin block 0x12a
    prev=[0x11f], succ=[0x1b6f, 0x135]
    =================================
    0x12b: v12b(0x6fcfff45) = CONST 
    0x130: v130 = EQ v12b(0x6fcfff45), v12
    0x1af7: v1af7(0x1b6f) = CONST 
    0x1af8: JUMPI v1af7(0x1b6f), v130

    Begin block 0x1b6f
    prev=[0x12a], succ=[]
    =================================
    0x1b70: v1b70(0x7fd) = CONST 
    0x1b71: CALLPRIVATE v1b70(0x7fd)

    Begin block 0x135
    prev=[0x12a], succ=[0x140, 0x1b51]
    =================================
    0x136: v136(0x70a08231) = CONST 
    0x13b: v13b = EQ v136(0x70a08231), v12
    0x1af9: v1af9(0x1b51) = CONST 
    0x1afa: JUMPI v1af9(0x1b51), v13b

    Begin block 0x140
    prev=[0x135], succ=[]
    =================================
    0x140: v140(0x267) = CONST 
    0x143: JUMP v140(0x267)

    Begin block 0xc2
    prev=[0xb6], succ=[0x1b63, 0xcd]
    =================================
    0xc3: vc3(0x73f03dff) = CONST 
    0xc8: vc8 = EQ vc3(0x73f03dff), v12
    0x1ae5: v1ae5(0x1b63) = CONST 
    0x1ae6: JUMPI v1ae5(0x1b63), vc8

    Begin block 0xcd
    prev=[0xc2], succ=[0x1b72, 0xd8]
    =================================
    0xce: vce(0x782d6fe1) = CONST 
    0xd3: vd3 = EQ vce(0x782d6fe1), v12
    0x1ae7: v1ae7(0x1b72) = CONST 
    0x1ae8: JUMPI v1ae7(0x1b72), vd3

    Begin block 0x1b72
    prev=[0xcd], succ=[]
    =================================
    0x1b73: v1b73(0x849) = CONST 
    0x1b74: CALLPRIVATE v1b73(0x849)

    Begin block 0xd8
    prev=[0xcd], succ=[0xe3, 0x1b75]
    =================================
    0xd9: vd9(0x7af548c1) = CONST 
    0xde: vde = EQ vd9(0x7af548c1), v12
    0x1ae9: v1ae9(0x1b75) = CONST 
    0x1aea: JUMPI v1ae9(0x1b75), vde

    Begin block 0xe3
    prev=[0xd8], succ=[0x1b78, 0xee]
    =================================
    0xe4: ve4(0x7ecebe00) = CONST 
    0xe9: ve9 = EQ ve4(0x7ecebe00), v12
    0x1aeb: v1aeb(0x1b78) = CONST 
    0x1aec: JUMPI v1aeb(0x1b78), ve9

    Begin block 0x1b78
    prev=[0xe3], succ=[]
    =================================
    0x1b79: v1b79(0x8ba) = CONST 
    0x1b7a: CALLPRIVATE v1b79(0x8ba)

    Begin block 0xee
    prev=[0xe3], succ=[0x1b7b, 0xf9]
    =================================
    0xef: vef(0x95d89b41) = CONST 
    0xf4: vf4 = EQ vef(0x95d89b41), v12
    0x1aed: v1aed(0x1b7b) = CONST 
    0x1aee: JUMPI v1aed(0x1b7b), vf4

    Begin block 0x1b7b
    prev=[0xee], succ=[]
    =================================
    0x1b7c: v1b7c(0x8ed) = CONST 
    0x1b7d: CALLPRIVATE v1b7c(0x8ed)

    Begin block 0xf9
    prev=[0xee], succ=[0x104, 0x1b7e]
    =================================
    0xfa: vfa(0x97d63f93) = CONST 
    0xff: vff = EQ vfa(0x97d63f93), v12
    0x1aef: v1aef(0x1b7e) = CONST 
    0x1af0: JUMPI v1aef(0x1b7e), vff

    Begin block 0x104
    prev=[0xf9], succ=[]
    =================================
    0x104: v104(0x267) = CONST 
    0x107: JUMP v104(0x267)

    Begin block 0x1b7e
    prev=[0xf9], succ=[]
    =================================
    0x1b7f: v1b7f(0x902) = CONST 
    0x1b80: CALLPRIVATE v1b7f(0x902)

    Begin block 0x1b75
    prev=[0xd8], succ=[]
    =================================
    0x1b76: v1b76(0x882) = CONST 
    0x1b77: CALLPRIVATE v1b76(0x882)

    Begin block 0x29
    prev=[0x1e], succ=[0x7a, 0x34]
    =================================
    0x2a: v2a(0xc3cda520) = CONST 
    0x2f: v2f = GT v2a(0xc3cda520), v12
    0x30: v30(0x7a) = CONST 
    0x33: JUMPI v30(0x7a), v2f

    Begin block 0x7a
    prev=[0x29], succ=[0x1b63, 0x86]
    =================================
    0x7c: v7c(0x98dca210) = CONST 
    0x81: v81 = EQ v7c(0x98dca210), v12
    0x1adb: v1adb(0x1b63) = CONST 
    0x1adc: JUMPI v1adb(0x1b63), v81

    Begin block 0x86
    prev=[0x7a], succ=[0x1b30, 0x91]
    =================================
    0x87: v87(0xa457c2d7) = CONST 
    0x8c: v8c = EQ v87(0xa457c2d7), v12
    0x1add: v1add(0x1b30) = CONST 
    0x1ade: JUMPI v1add(0x1b30), v8c

    Begin block 0x91
    prev=[0x86], succ=[0x1b30, 0x9c]
    =================================
    0x92: v92(0xa9059cbb) = CONST 
    0x97: v97 = EQ v92(0xa9059cbb), v12
    0x1adf: v1adf(0x1b30) = CONST 
    0x1ae0: JUMPI v1adf(0x1b30), v97

    Begin block 0x9c
    prev=[0x91], succ=[0x1b51, 0xa7]
    =================================
    0x9d: v9d(0xb4b5ea57) = CONST 
    0xa2: va2 = EQ v9d(0xb4b5ea57), v12
    0x1ae1: v1ae1(0x1b51) = CONST 
    0x1ae2: JUMPI v1ae1(0x1b51), va2

    Begin block 0xa7
    prev=[0x9c], succ=[0xb2, 0x1b81]
    =================================
    0xa8: va8(0xb6fa8576) = CONST 
    0xad: vad = EQ va8(0xb6fa8576), v12
    0x1ae3: v1ae3(0x1b81) = CONST 
    0x1ae4: JUMPI v1ae3(0x1b81), vad

    Begin block 0xb2
    prev=[0xa7], succ=[]
    =================================
    0xb2: vb2(0x267) = CONST 
    0xb5: JUMP vb2(0x267)

    Begin block 0x1b81
    prev=[0xa7], succ=[]
    =================================
    0x1b82: v1b82(0x917) = CONST 
    0x1b83: CALLPRIVATE v1b82(0x917)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x1b84]
    =================================
    0x35: v35(0xc3cda520) = CONST 
    0x3a: v3a = EQ v35(0xc3cda520), v12
    0x1acf: v1acf(0x1b84) = CONST 
    0x1ad0: JUMPI v1acf(0x1b84), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x1b87, 0x4a]
    =================================
    0x40: v40(0xdd62ed3e) = CONST 
    0x45: v45 = EQ v40(0xdd62ed3e), v12
    0x1ad1: v1ad1(0x1b87) = CONST 
    0x1ad2: JUMPI v1ad1(0x1b87), v45

    Begin block 0x1b87
    prev=[0x3f], succ=[]
    =================================
    0x1b88: v1b88(0x980) = CONST 
    0x1b89: CALLPRIVATE v1b88(0x980)

    Begin block 0x4a
    prev=[0x3f], succ=[0x1b8a, 0x55]
    =================================
    0x4b: v4b(0xe7a324dc) = CONST 
    0x50: v50 = EQ v4b(0xe7a324dc), v12
    0x1ad3: v1ad3(0x1b8a) = CONST 
    0x1ad4: JUMPI v1ad3(0x1b8a), v50

    Begin block 0x1b8a
    prev=[0x4a], succ=[]
    =================================
    0x1b8b: v1b8b(0x9bb) = CONST 
    0x1b8c: CALLPRIVATE v1b8b(0x9bb)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0x1b8d]
    =================================
    0x56: v56(0xec342ad0) = CONST 
    0x5b: v5b = EQ v56(0xec342ad0), v12
    0x1ad5: v1ad5(0x1b8d) = CONST 
    0x1ad6: JUMPI v1ad5(0x1b8d), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x1b90, 0x6b]
    =================================
    0x61: v61(0xf1127ed8) = CONST 
    0x66: v66 = EQ v61(0xf1127ed8), v12
    0x1ad7: v1ad7(0x1b90) = CONST 
    0x1ad8: JUMPI v1ad7(0x1b90), v66

    Begin block 0x1b90
    prev=[0x60], succ=[]
    =================================
    0x1b91: v1b91(0x9e5) = CONST 
    0x1b92: CALLPRIVATE v1b91(0x9e5)

    Begin block 0x6b
    prev=[0x60], succ=[0x76, 0x1b63]
    =================================
    0x6c: v6c(0xfa8f3455) = CONST 
    0x71: v71 = EQ v6c(0xfa8f3455), v12
    0x1ad9: v1ad9(0x1b63) = CONST 
    0x1ada: JUMPI v1ad9(0x1b63), v71

    Begin block 0x76
    prev=[0x6b], succ=[]
    =================================
    0x76: v76(0x267) = CONST 
    0x79: JUMP v76(0x267)

    Begin block 0x1b8d
    prev=[0x55], succ=[]
    =================================
    0x1b8e: v1b8e(0x9d0) = CONST 
    0x1b8f: CALLPRIVATE v1b8e(0x9d0)

    Begin block 0x1b84
    prev=[0x34], succ=[]
    =================================
    0x1b85: v1b85(0x92c) = CONST 
    0x1b86: CALLPRIVATE v1b85(0x92c)

}

function 0x1084(0x1084arg0x0) private {
    Begin block 0x1084
    prev=[], succ=[0x1a9e, 0x10c1]
    =================================
    0x1085: v1085(0x2) = CONST 
    0x1088: v1088 = SLOAD v1085(0x2)
    0x1089: v1089(0x40) = CONST 
    0x108c: v108c = MLOAD v1089(0x40)
    0x108d: v108d(0x20) = CONST 
    0x108f: v108f(0x1) = CONST 
    0x1092: v1092 = AND v1088, v108f(0x1)
    0x1093: v1093 = ISZERO v1092
    0x1094: v1094(0x100) = CONST 
    0x1097: v1097 = MUL v1094(0x100), v1093
    0x1098: v1098(0x0) = CONST 
    0x109a: v109a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1098(0x0)
    0x109b: v109b = ADD v109a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1097
    0x109e: v109e = AND v1088, v109b
    0x10a1: v10a1 = DIV v109e, v1085(0x2)
    0x10a2: v10a2(0x1f) = CONST 
    0x10a5: v10a5 = ADD v10a1, v10a2(0x1f)
    0x10a8: v10a8 = DIV v10a5, v108d(0x20)
    0x10aa: v10aa = MUL v108d(0x20), v10a8
    0x10ac: v10ac = ADD v108c, v10aa
    0x10ae: v10ae = ADD v108d(0x20), v10ac
    0x10b1: MSTORE v1089(0x40), v10ae
    0x10b4: MSTORE v108c, v10a1
    0x10b8: v10b8 = ADD v108c, v108d(0x20)
    0x10bc: v10bc = ISZERO v10a1
    0x10bd: v10bd(0x1a9e) = CONST 
    0x10c0: JUMPI v10bd(0x1a9e), v10bc

    Begin block 0x1a9e
    prev=[0x1084], succ=[]
    =================================
    0x1aa5: RETURNPRIVATE v1084arg0, v108c, v1084arg0

    Begin block 0x10c1
    prev=[0x1084], succ=[0x10c9, 0xb260x1084]
    =================================
    0x10c2: v10c2(0x1f) = CONST 
    0x10c4: v10c4 = LT v10c2(0x1f), v10a1
    0x10c5: v10c5(0xb26) = CONST 
    0x10c8: JUMPI v10c5(0xb26), v10c4

    Begin block 0x10c9
    prev=[0x10c1], succ=[0x1ac5]
    =================================
    0x10c9: v10c9(0x100) = CONST 
    0x10ce: v10ce = SLOAD v1085(0x2)
    0x10cf: v10cf = DIV v10ce, v10c9(0x100)
    0x10d0: v10d0 = MUL v10cf, v10c9(0x100)
    0x10d2: MSTORE v10b8, v10d0
    0x10d4: v10d4(0x20) = CONST 
    0x10d6: v10d6 = ADD v10d4(0x20), v10b8
    0x10d8: v10d8(0x1ac5) = CONST 
    0x10db: JUMP v10d8(0x1ac5)

    Begin block 0x1ac5
    prev=[0x10c9], succ=[]
    =================================
    0x1acc: RETURNPRIVATE v1084arg0, v108c, v1084arg0

    Begin block 0xb260x1084
    prev=[0x10c1], succ=[0xb340x1084]
    =================================
    0xb280x1084: v1084b28 = ADD v10b8, v10a1
    0xb2b0x1084: v1084b2b(0x0) = CONST 
    0xb2d0x1084: MSTORE v1084b2b(0x0), v1085(0x2)
    0xb2e0x1084: v1084b2e(0x20) = CONST 
    0xb300x1084: v1084b30(0x0) = CONST 
    0xb320x1084: v1084b32 = SHA3 v1084b30(0x0), v1084b2e(0x20)

    Begin block 0xb340x1084
    prev=[0xb340x1084, 0xb260x1084], succ=[0xb340x1084, 0xb480x1084]
    =================================
    0xb340x1084_0x0: vb341084_0 = PHI v10b8, v1084b40
    0xb340x1084_0x1: vb341084_1 = PHI v1084b3c, v1084b32
    0xb360x1084: v1084b36 = SLOAD vb341084_1
    0xb380x1084: MSTORE vb341084_0, v1084b36
    0xb3a0x1084: v1084b3a(0x1) = CONST 
    0xb3c0x1084: v1084b3c = ADD v1084b3a(0x1), vb341084_1
    0xb3e0x1084: v1084b3e(0x20) = CONST 
    0xb400x1084: v1084b40 = ADD v1084b3e(0x20), vb341084_0
    0xb430x1084: v1084b43 = GT v1084b28, v1084b40
    0xb440x1084: v1084b44(0xb34) = CONST 
    0xb470x1084: JUMPI v1084b44(0xb34), v1084b43

    Begin block 0xb480x1084
    prev=[0xb340x1084], succ=[0xb510x1084]
    =================================
    0xb4a0x1084: v1084b4a = SUB v1084b40, v1084b28
    0xb4b0x1084: v1084b4b(0x1f) = CONST 
    0xb4d0x1084: v1084b4d = AND v1084b4b(0x1f), v1084b4a
    0xb4f0x1084: v1084b4f = ADD v1084b28, v1084b4d

    Begin block 0xb510x1084
    prev=[0xb480x1084], succ=[]
    =================================
    0xb580x1084: RETURNPRIVATE v1084arg0, v108c, v1084arg0

}

function 0x114d(0x114darg0x0, 0x114darg0x1, 0x114darg0x2) private {
    Begin block 0x114d
    prev=[], succ=[0x116e]
    =================================
    0x114e: v114e(0x60) = CONST 
    0x1150: v1150(0x0) = CONST 
    0x1152: v1152(0x60) = CONST 
    0x1155: v1155(0x1) = CONST 
    0x1157: v1157(0x1) = CONST 
    0x1159: v1159(0xa0) = CONST 
    0x115b: v115b(0x10000000000000000000000000000000000000000) = SHL v1159(0xa0), v1157(0x1)
    0x115c: v115c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v115b(0x10000000000000000000000000000000000000000), v1155(0x1)
    0x115d: v115d = AND v115c(0xffffffffffffffffffffffffffffffffffffffff), v114darg1
    0x115f: v115f(0x40) = CONST 
    0x1161: v1161 = MLOAD v115f(0x40)
    0x1165: v1165 = MLOAD v114darg0
    0x1167: v1167(0x20) = CONST 
    0x1169: v1169 = ADD v1167(0x20), v114darg0

    Begin block 0x116e
    prev=[0x114d, 0x1177], succ=[0x118d, 0x1177]
    =================================
    0x116e_0x2: v116e_2 = PHI v1165, v1180
    0x116f: v116f(0x20) = CONST 
    0x1172: v1172 = LT v116e_2, v116f(0x20)
    0x1173: v1173(0x118d) = CONST 
    0x1176: JUMPI v1173(0x118d), v1172

    Begin block 0x118d
    prev=[0x116e], succ=[0x11cc, 0x11ed]
    =================================
    0x118d_0x0: v118d_0 = PHI v1169, v1188
    0x118d_0x1: v118d_1 = PHI v1161, v1186
    0x118d_0x2: v118d_2 = PHI v1165, v1180
    0x118e: v118e(0x1) = CONST 
    0x1191: v1191(0x20) = CONST 
    0x1193: v1193 = SUB v1191(0x20), v118d_2
    0x1194: v1194(0x100) = CONST 
    0x1197: v1197 = EXP v1194(0x100), v1193
    0x1198: v1198 = SUB v1197, v118e(0x1)
    0x119a: v119a = NOT v1198
    0x119c: v119c = MLOAD v118d_0
    0x119d: v119d = AND v119c, v119a
    0x11a0: v11a0 = MLOAD v118d_1
    0x11a1: v11a1 = AND v11a0, v1198
    0x11a4: v11a4 = OR v119d, v11a1
    0x11a6: MSTORE v118d_1, v11a4
    0x11af: v11af = ADD v1165, v1161
    0x11b3: v11b3(0x0) = CONST 
    0x11b5: v11b5(0x40) = CONST 
    0x11b7: v11b7 = MLOAD v11b5(0x40)
    0x11ba: v11ba = SUB v11af, v11b7
    0x11bd: v11bd = GAS 
    0x11be: v11be = DELEGATECALL v11bd, v115d, v11b7, v11ba, v11b7, v11b3(0x0)
    0x11c2: v11c2 = RETURNDATASIZE 
    0x11c4: v11c4(0x0) = CONST 
    0x11c7: v11c7 = EQ v11c2, v11c4(0x0)
    0x11c8: v11c8(0x11ed) = CONST 
    0x11cb: JUMPI v11c8(0x11ed), v11c7

    Begin block 0x11cc
    prev=[0x118d], succ=[0x11f2]
    =================================
    0x11cc: v11cc(0x40) = CONST 
    0x11ce: v11ce = MLOAD v11cc(0x40)
    0x11d1: v11d1(0x1f) = CONST 
    0x11d3: v11d3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v11d1(0x1f)
    0x11d4: v11d4(0x3f) = CONST 
    0x11d6: v11d6 = RETURNDATASIZE 
    0x11d7: v11d7 = ADD v11d6, v11d4(0x3f)
    0x11d8: v11d8 = AND v11d7, v11d3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x11da: v11da = ADD v11ce, v11d8
    0x11db: v11db(0x40) = CONST 
    0x11dd: MSTORE v11db(0x40), v11da
    0x11de: v11de = RETURNDATASIZE 
    0x11e0: MSTORE v11ce, v11de
    0x11e1: v11e1 = RETURNDATASIZE 
    0x11e2: v11e2(0x0) = CONST 
    0x11e4: v11e4(0x20) = CONST 
    0x11e7: v11e7 = ADD v11ce, v11e4(0x20)
    0x11e8: RETURNDATACOPY v11e7, v11e2(0x0), v11e1
    0x11e9: v11e9(0x11f2) = CONST 
    0x11ec: JUMP v11e9(0x11f2)

    Begin block 0x11f2
    prev=[0x11cc, 0x11ed], succ=[0x1201, 0x1207]
    =================================
    0x11f8: v11f8(0x0) = CONST 
    0x11fb: v11fb = EQ v11be, v11f8(0x0)
    0x11fc: v11fc = ISZERO v11fb
    0x11fd: v11fd(0x1207) = CONST 
    0x1200: JUMPI v11fd(0x1207), v11fc

    Begin block 0x1201
    prev=[0x11f2], succ=[]
    =================================
    0x1201: v1201 = RETURNDATASIZE 
    0x1201_0x0: v1201_0 = PHI v11ce, v11ee(0x60)
    0x1202: v1202(0x20) = CONST 
    0x1205: v1205 = ADD v1201_0, v1202(0x20)
    0x1206: REVERT v1205, v1201

    Begin block 0x1207
    prev=[0x11f2], succ=[]
    =================================
    0x1207_0x0: v1207_0 = PHI v11ce, v11ee(0x60)
    0x120e: RETURNPRIVATE v114darg2, v1207_0

    Begin block 0x11ed
    prev=[0x118d], succ=[0x11f2]
    =================================
    0x11ee: v11ee(0x60) = CONST 

    Begin block 0x1177
    prev=[0x116e], succ=[0x116e]
    =================================
    0x1177_0x0: v1177_0 = PHI v1169, v1188
    0x1177_0x1: v1177_1 = PHI v1161, v1186
    0x1177_0x2: v1177_2 = PHI v1165, v1180
    0x1178: v1178 = MLOAD v1177_0
    0x117a: MSTORE v1177_1, v1178
    0x117b: v117b(0x1f) = CONST 
    0x117d: v117d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v117b(0x1f)
    0x1180: v1180 = ADD v1177_2, v117d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x1182: v1182(0x20) = CONST 
    0x1186: v1186 = ADD v1182(0x20), v1177_1
    0x1188: v1188 = ADD v1182(0x20), v1177_0
    0x1189: v1189(0x116e) = CONST 
    0x118c: JUMP v1189(0x116e)

}

function fallback()() public {
    Begin block 0x267
    prev=[], succ=[0x26e, 0x2a4]
    =================================
    0x268: v268 = CALLVALUE 
    0x269: v269 = ISZERO v268
    0x26a: v26a(0x2a4) = CONST 
    0x26d: JUMPI v26a(0x2a4), v269

    Begin block 0x26e
    prev=[0x267], succ=[]
    =================================
    0x26e: v26e(0x40) = CONST 
    0x270: v270 = MLOAD v26e(0x40)
    0x271: v271(0x461bcd) = CONST 
    0x275: v275(0xe5) = CONST 
    0x277: v277(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v275(0xe5), v271(0x461bcd)
    0x279: MSTORE v270, v277(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x27a: v27a(0x4) = CONST 
    0x27c: v27c = ADD v27a(0x4), v270
    0x27f: v27f(0x20) = CONST 
    0x281: v281 = ADD v27f(0x20), v27c
    0x284: v284(0x20) = SUB v281, v27c
    0x286: MSTORE v27c, v284(0x20)
    0x287: v287(0x34) = CONST 
    0x28a: MSTORE v281, v287(0x34)
    0x28b: v28b(0x20) = CONST 
    0x28d: v28d = ADD v28b(0x20), v281
    0x28f: v28f(0x1364) = CONST 
    0x292: v292(0x34) = CONST 
    0x295: CODECOPY v28d, v28f(0x1364), v292(0x34)
    0x296: v296(0x40) = CONST 
    0x298: v298 = ADD v296(0x40), v28d
    0x29c: v29c(0x40) = CONST 
    0x29e: v29e = MLOAD v29c(0x40)
    0x2a1: v2a1(0x84) = SUB v298, v29e
    0x2a3: REVERT v29e, v2a1(0x84)

    Begin block 0x2a4
    prev=[0x267], succ=[0xa440x267]
    =================================
    0x2a5: v2a5(0x2ac) = CONST 
    0x2a8: v2a8(0xa44) = CONST 
    0x2ab: JUMP v2a8(0xa44)

    Begin block 0xa440x267
    prev=[0x2a4], succ=[0xa8b0x267, 0xaac0x267]
    =================================
    0xa450x267: v267a45(0x13) = CONST 
    0xa470x267: v267a47 = SLOAD v267a45(0x13)
    0xa480x267: v267a48(0x40) = CONST 
    0xa4a0x267: v267a4a = MLOAD v267a48(0x40)
    0xa4b0x267: v267a4b(0x60) = CONST 
    0xa4e0x267: v267a4e(0x0) = CONST 
    0xa510x267: v267a51(0x1) = CONST 
    0xa530x267: v267a53(0x1) = CONST 
    0xa550x267: v267a55(0xa0) = CONST 
    0xa570x267: v267a57(0x10000000000000000000000000000000000000000) = SHL v267a55(0xa0), v267a53(0x1)
    0xa580x267: v267a58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v267a57(0x10000000000000000000000000000000000000000), v267a51(0x1)
    0xa5b0x267: v267a5b = AND v267a47, v267a58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x267: v267a5f = CALLDATASIZE 
    0xa670x267: CALLDATACOPY v267a4a, v267a4e(0x0), v267a5f
    0xa680x267: v267a68(0x40) = CONST 
    0xa6a0x267: v267a6a = MLOAD v267a68(0x40)
    0xa6c0x267: v267a6c = ADD v267a4a, v267a5f
    0xa6f0x267: v267a6f(0x0) = CONST 
    0xa790x267: v267a79 = SUB v267a6c, v267a6a
    0xa7c0x267: v267a7c = GAS 
    0xa7d0x267: v267a7d = DELEGATECALL v267a7c, v267a5b, v267a6a, v267a79, v267a6a, v267a6f(0x0)
    0xa810x267: v267a81 = RETURNDATASIZE 
    0xa830x267: v267a83(0x0) = CONST 
    0xa860x267: v267a86 = EQ v267a81, v267a83(0x0)
    0xa870x267: v267a87(0xaac) = CONST 
    0xa8a0x267: JUMPI v267a87(0xaac), v267a86

    Begin block 0xa8b0x267
    prev=[0xa440x267], succ=[0xab10x267]
    =================================
    0xa8b0x267: v267a8b(0x40) = CONST 
    0xa8d0x267: v267a8d = MLOAD v267a8b(0x40)
    0xa900x267: v267a90(0x1f) = CONST 
    0xa920x267: v267a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v267a90(0x1f)
    0xa930x267: v267a93(0x3f) = CONST 
    0xa950x267: v267a95 = RETURNDATASIZE 
    0xa960x267: v267a96 = ADD v267a95, v267a93(0x3f)
    0xa970x267: v267a97 = AND v267a96, v267a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x267: v267a99 = ADD v267a8d, v267a97
    0xa9a0x267: v267a9a(0x40) = CONST 
    0xa9c0x267: MSTORE v267a9a(0x40), v267a99
    0xa9d0x267: v267a9d = RETURNDATASIZE 
    0xa9f0x267: MSTORE v267a8d, v267a9d
    0xaa00x267: v267aa0 = RETURNDATASIZE 
    0xaa10x267: v267aa1(0x0) = CONST 
    0xaa30x267: v267aa3(0x20) = CONST 
    0xaa60x267: v267aa6 = ADD v267a8d, v267aa3(0x20)
    0xaa70x267: RETURNDATACOPY v267aa6, v267aa1(0x0), v267aa0
    0xaa80x267: v267aa8(0xab1) = CONST 
    0xaab0x267: JUMP v267aa8(0xab1)

    Begin block 0xab10x267
    prev=[0xa8b0x267, 0xaac0x267], succ=[0xac50x267, 0x14560x267]
    =================================
    0xab60x267: v267ab6(0x40) = CONST 
    0xab80x267: v267ab8 = MLOAD v267ab6(0x40)
    0xab90x267: v267ab9 = RETURNDATASIZE 
    0xaba0x267: v267aba(0x0) = CONST 
    0xabd0x267: RETURNDATACOPY v267ab8, v267aba(0x0), v267ab9
    0xac00x267: v267ac0 = ISZERO v267a7d
    0xac10x267: v267ac1(0x1456) = CONST 
    0xac40x267: JUMPI v267ac1(0x1456), v267ac0

    Begin block 0xac50x267
    prev=[0xab10x267], succ=[]
    =================================
    0xac50x267: v267ac5 = RETURNDATASIZE 
    0xac70x267: RETURN v267ab8, v267ac5

    Begin block 0x14560x267
    prev=[0xab10x267], succ=[]
    =================================
    0x14570x267: v2671457 = RETURNDATASIZE 
    0x14590x267: REVERT v267ab8, v2671457

    Begin block 0xaac0x267
    prev=[0xa440x267], succ=[0xab10x267]
    =================================
    0xaad0x267: v267aad(0x60) = CONST 

}

function name()() public {
    Begin block 0x2af
    prev=[], succ=[0x2b7, 0x2bb]
    =================================
    0x2b0: v2b0 = CALLVALUE 
    0x2b2: v2b2 = ISZERO v2b0
    0x2b3: v2b3(0x2bb) = CONST 
    0x2b6: JUMPI v2b3(0x2bb), v2b2

    Begin block 0x2b7
    prev=[0x2af], succ=[]
    =================================
    0x2b7: v2b7(0x0) = CONST 
    0x2ba: REVERT v2b7(0x0), v2b7(0x0)

    Begin block 0x2bb
    prev=[0x2af], succ=[0x2c40x2af]
    =================================
    0x2bd: v2bd(0x2c4) = CONST 
    0x2c0: v2c0(0xacc) = CONST 
    0x2c3: v2c3_0, v2c3_1 = CALLPRIVATE v2c0(0xacc), v2bd(0x2c4)

    Begin block 0x2c40x2af
    prev=[0x2bb], succ=[0x2e60x2af]
    =================================
    0x2c50x2af: v2af2c5(0x40) = CONST 
    0x2c80x2af: v2af2c8 = MLOAD v2af2c5(0x40)
    0x2c90x2af: v2af2c9(0x20) = CONST 
    0x2cd0x2af: MSTORE v2af2c8, v2af2c9(0x20)
    0x2cf0x2af: v2af2cf = MLOAD v2c3_0
    0x2d20x2af: v2af2d2 = ADD v2af2c8, v2af2c9(0x20)
    0x2d30x2af: MSTORE v2af2d2, v2af2cf
    0x2d50x2af: v2af2d5 = MLOAD v2c3_0
    0x2dc0x2af: v2af2dc = ADD v2af2c8, v2af2c5(0x40)
    0x2df0x2af: v2af2df = ADD v2c3_0, v2af2c9(0x20)
    0x2e40x2af: v2af2e4(0x0) = CONST 

    Begin block 0x2e60x2af
    prev=[0x2ef0x2af, 0x2c40x2af], succ=[0x2fe0x2af, 0x2ef0x2af]
    =================================
    0x2e60x2af_0x0: v2e62af_0 = PHI v2af2f9, v2af2e4(0x0)
    0x2e90x2af: v2af2e9 = LT v2e62af_0, v2af2d5
    0x2ea0x2af: v2af2ea = ISZERO v2af2e9
    0x2eb0x2af: v2af2eb(0x2fe) = CONST 
    0x2ee0x2af: JUMPI v2af2eb(0x2fe), v2af2ea

    Begin block 0x2fe0x2af
    prev=[0x2e60x2af], succ=[0x32b0x2af, 0x3120x2af]
    =================================
    0x3070x2af: v2af307 = ADD v2af2d5, v2af2dc
    0x3090x2af: v2af309(0x1f) = CONST 
    0x30b0x2af: v2af30b = AND v2af309(0x1f), v2af2d5
    0x30d0x2af: v2af30d = ISZERO v2af30b
    0x30e0x2af: v2af30e(0x32b) = CONST 
    0x3110x2af: JUMPI v2af30e(0x32b), v2af30d

    Begin block 0x32b0x2af
    prev=[0x2fe0x2af, 0x3120x2af], succ=[]
    =================================
    0x32b0x2af_0x1: v32b2af_1 = PHI v2af328, v2af307
    0x3310x2af: v2af331(0x40) = CONST 
    0x3330x2af: v2af333 = MLOAD v2af331(0x40)
    0x3360x2af: v2af336 = SUB v32b2af_1, v2af333
    0x3380x2af: RETURN v2af333, v2af336

    Begin block 0x3120x2af
    prev=[0x2fe0x2af], succ=[0x32b0x2af]
    =================================
    0x3140x2af: v2af314 = SUB v2af307, v2af30b
    0x3160x2af: v2af316 = MLOAD v2af314
    0x3170x2af: v2af317(0x1) = CONST 
    0x31a0x2af: v2af31a(0x20) = CONST 
    0x31c0x2af: v2af31c = SUB v2af31a(0x20), v2af30b
    0x31d0x2af: v2af31d(0x100) = CONST 
    0x3200x2af: v2af320 = EXP v2af31d(0x100), v2af31c
    0x3210x2af: v2af321 = SUB v2af320, v2af317(0x1)
    0x3220x2af: v2af322 = NOT v2af321
    0x3230x2af: v2af323 = AND v2af322, v2af316
    0x3250x2af: MSTORE v2af314, v2af323
    0x3260x2af: v2af326(0x20) = CONST 
    0x3280x2af: v2af328 = ADD v2af326(0x20), v2af314

    Begin block 0x2ef0x2af
    prev=[0x2e60x2af], succ=[0x2e60x2af]
    =================================
    0x2ef0x2af_0x0: v2ef2af_0 = PHI v2af2f9, v2af2e4(0x0)
    0x2f10x2af: v2af2f1 = ADD v2ef2af_0, v2af2df
    0x2f20x2af: v2af2f2 = MLOAD v2af2f1
    0x2f50x2af: v2af2f5 = ADD v2ef2af_0, v2af2dc
    0x2f60x2af: MSTORE v2af2f5, v2af2f2
    0x2f70x2af: v2af2f7(0x20) = CONST 
    0x2f90x2af: v2af2f9 = ADD v2af2f7(0x20), v2ef2af_0
    0x2fa0x2af: v2af2fa(0x2e6) = CONST 
    0x2fd0x2af: JUMP v2af2fa(0x2e6)

}

function delegateToImplementation(bytes)() public {
    Begin block 0x339
    prev=[], succ=[0x341, 0x345]
    =================================
    0x33a: v33a = CALLVALUE 
    0x33c: v33c = ISZERO v33a
    0x33d: v33d(0x345) = CONST 
    0x340: JUMPI v33d(0x345), v33c

    Begin block 0x341
    prev=[0x339], succ=[]
    =================================
    0x341: v341(0x0) = CONST 
    0x344: REVERT v341(0x0), v341(0x0)

    Begin block 0x345
    prev=[0x339], succ=[0x358, 0x35c]
    =================================
    0x347: v347(0x2c4) = CONST 
    0x34a: v34a(0x4) = CONST 
    0x34d: v34d = CALLDATASIZE 
    0x34e: v34e = SUB v34d, v34a(0x4)
    0x34f: v34f(0x20) = CONST 
    0x352: v352 = LT v34e, v34f(0x20)
    0x353: v353 = ISZERO v352
    0x354: v354(0x35c) = CONST 
    0x357: JUMPI v354(0x35c), v353

    Begin block 0x358
    prev=[0x345], succ=[]
    =================================
    0x358: v358(0x0) = CONST 
    0x35b: REVERT v358(0x0), v358(0x0)

    Begin block 0x35c
    prev=[0x345], succ=[0x372, 0x376]
    =================================
    0x35e: v35e = ADD v34a(0x4), v34e
    0x360: v360(0x20) = CONST 
    0x363: v363(0x24) = ADD v34a(0x4), v360(0x20)
    0x365: v365 = CALLDATALOAD v34a(0x4)
    0x366: v366(0x1) = CONST 
    0x368: v368(0x20) = CONST 
    0x36a: v36a(0x100000000) = SHL v368(0x20), v366(0x1)
    0x36c: v36c = GT v365, v36a(0x100000000)
    0x36d: v36d = ISZERO v36c
    0x36e: v36e(0x376) = CONST 
    0x371: JUMPI v36e(0x376), v36d

    Begin block 0x372
    prev=[0x35c], succ=[]
    =================================
    0x372: v372(0x0) = CONST 
    0x375: REVERT v372(0x0), v372(0x0)

    Begin block 0x376
    prev=[0x35c], succ=[0x384, 0x388]
    =================================
    0x378: v378 = ADD v34a(0x4), v365
    0x37a: v37a(0x20) = CONST 
    0x37d: v37d = ADD v378, v37a(0x20)
    0x37e: v37e = GT v37d, v35e
    0x37f: v37f = ISZERO v37e
    0x380: v380(0x388) = CONST 
    0x383: JUMPI v380(0x388), v37f

    Begin block 0x384
    prev=[0x376], succ=[]
    =================================
    0x384: v384(0x0) = CONST 
    0x387: REVERT v384(0x0), v384(0x0)

    Begin block 0x388
    prev=[0x376], succ=[0x3a5, 0x3a9]
    =================================
    0x38a: v38a = CALLDATALOAD v378
    0x38c: v38c(0x20) = CONST 
    0x38e: v38e = ADD v38c(0x20), v378
    0x391: v391(0x1) = CONST 
    0x394: v394 = MUL v38a, v391(0x1)
    0x396: v396 = ADD v38e, v394
    0x397: v397 = GT v396, v35e
    0x398: v398(0x1) = CONST 
    0x39a: v39a(0x20) = CONST 
    0x39c: v39c(0x100000000) = SHL v39a(0x20), v398(0x1)
    0x39e: v39e = GT v38a, v39c(0x100000000)
    0x39f: v39f = OR v39e, v397
    0x3a0: v3a0 = ISZERO v39f
    0x3a1: v3a1(0x3a9) = CONST 
    0x3a4: JUMPI v3a1(0x3a9), v3a0

    Begin block 0x3a5
    prev=[0x388], succ=[]
    =================================
    0x3a5: v3a5(0x0) = CONST 
    0x3a8: REVERT v3a5(0x0), v3a5(0x0)

    Begin block 0x3a9
    prev=[0x388], succ=[0xb590x339]
    =================================
    0x3ae: v3ae(0x1f) = CONST 
    0x3b0: v3b0 = ADD v3ae(0x1f), v38a
    0x3b1: v3b1(0x20) = CONST 
    0x3b5: v3b5 = DIV v3b0, v3b1(0x20)
    0x3b6: v3b6 = MUL v3b5, v3b1(0x20)
    0x3b7: v3b7(0x20) = CONST 
    0x3b9: v3b9 = ADD v3b7(0x20), v3b6
    0x3ba: v3ba(0x40) = CONST 
    0x3bc: v3bc = MLOAD v3ba(0x40)
    0x3bf: v3bf = ADD v3bc, v3b9
    0x3c0: v3c0(0x40) = CONST 
    0x3c2: MSTORE v3c0(0x40), v3bf
    0x3ca: MSTORE v3bc, v38a
    0x3cb: v3cb(0x20) = CONST 
    0x3cd: v3cd = ADD v3cb(0x20), v3bc
    0x3d3: CALLDATACOPY v3cd, v38e, v38a
    0x3d4: v3d4(0x0) = CONST 
    0x3d7: v3d7 = ADD v3cd, v38a
    0x3db: MSTORE v3d7, v3d4(0x0)
    0x3e0: v3e0(0xb59) = CONST 
    0x3e9: JUMP v3e0(0xb59)

    Begin block 0xb590x339
    prev=[0x3a9], succ=[0xb720x339]
    =================================
    0xb5a0x339: v339b5a(0x13) = CONST 
    0xb5c0x339: v339b5c = SLOAD v339b5a(0x13)
    0xb5d0x339: v339b5d(0x60) = CONST 
    0xb600x339: v339b60(0xb72) = CONST 
    0xb640x339: v339b64(0x1) = CONST 
    0xb660x339: v339b66(0x1) = CONST 
    0xb680x339: v339b68(0xa0) = CONST 
    0xb6a0x339: v339b6a(0x10000000000000000000000000000000000000000) = SHL v339b68(0xa0), v339b66(0x1)
    0xb6b0x339: v339b6b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v339b6a(0x10000000000000000000000000000000000000000), v339b64(0x1)
    0xb6c0x339: v339b6c = AND v339b6b(0xffffffffffffffffffffffffffffffffffffffff), v339b5c
    0xb6e0x339: v339b6e(0x114d) = CONST 
    0xb710x339: v339b71_0 = CALLPRIVATE v339b6e(0x114d), v3bc, v339b6c, v339b60(0xb72)

    Begin block 0xb720x339
    prev=[0xb590x339], succ=[0x2c40x339]
    =================================
    0xb770x339: JUMP v347(0x2c4)

    Begin block 0x2c40x339
    prev=[0xb720x339], succ=[0x2e60x339]
    =================================
    0x2c50x339: v3392c5(0x40) = CONST 
    0x2c80x339: v3392c8 = MLOAD v3392c5(0x40)
    0x2c90x339: v3392c9(0x20) = CONST 
    0x2cd0x339: MSTORE v3392c8, v3392c9(0x20)
    0x2cf0x339: v3392cf = MLOAD v339b71_0
    0x2d20x339: v3392d2 = ADD v3392c8, v3392c9(0x20)
    0x2d30x339: MSTORE v3392d2, v3392cf
    0x2d50x339: v3392d5 = MLOAD v339b71_0
    0x2dc0x339: v3392dc = ADD v3392c8, v3392c5(0x40)
    0x2df0x339: v3392df = ADD v339b71_0, v3392c9(0x20)
    0x2e40x339: v3392e4(0x0) = CONST 

    Begin block 0x2e60x339
    prev=[0x2ef0x339, 0x2c40x339], succ=[0x2fe0x339, 0x2ef0x339]
    =================================
    0x2e60x339_0x0: v2e6339_0 = PHI v3392f9, v3392e4(0x0)
    0x2e90x339: v3392e9 = LT v2e6339_0, v3392d5
    0x2ea0x339: v3392ea = ISZERO v3392e9
    0x2eb0x339: v3392eb(0x2fe) = CONST 
    0x2ee0x339: JUMPI v3392eb(0x2fe), v3392ea

    Begin block 0x2fe0x339
    prev=[0x2e60x339], succ=[0x32b0x339, 0x3120x339]
    =================================
    0x3070x339: v339307 = ADD v3392d5, v3392dc
    0x3090x339: v339309(0x1f) = CONST 
    0x30b0x339: v33930b = AND v339309(0x1f), v3392d5
    0x30d0x339: v33930d = ISZERO v33930b
    0x30e0x339: v33930e(0x32b) = CONST 
    0x3110x339: JUMPI v33930e(0x32b), v33930d

    Begin block 0x32b0x339
    prev=[0x2fe0x339, 0x3120x339], succ=[]
    =================================
    0x32b0x339_0x1: v32b339_1 = PHI v339328, v339307
    0x3310x339: v339331(0x40) = CONST 
    0x3330x339: v339333 = MLOAD v339331(0x40)
    0x3360x339: v339336 = SUB v32b339_1, v339333
    0x3380x339: RETURN v339333, v339336

    Begin block 0x3120x339
    prev=[0x2fe0x339], succ=[0x32b0x339]
    =================================
    0x3140x339: v339314 = SUB v339307, v33930b
    0x3160x339: v339316 = MLOAD v339314
    0x3170x339: v339317(0x1) = CONST 
    0x31a0x339: v33931a(0x20) = CONST 
    0x31c0x339: v33931c = SUB v33931a(0x20), v33930b
    0x31d0x339: v33931d(0x100) = CONST 
    0x3200x339: v339320 = EXP v33931d(0x100), v33931c
    0x3210x339: v339321 = SUB v339320, v339317(0x1)
    0x3220x339: v339322 = NOT v339321
    0x3230x339: v339323 = AND v339322, v339316
    0x3250x339: MSTORE v339314, v339323
    0x3260x339: v339326(0x20) = CONST 
    0x3280x339: v339328 = ADD v339326(0x20), v339314

    Begin block 0x2ef0x339
    prev=[0x2e60x339], succ=[0x2e60x339]
    =================================
    0x2ef0x339_0x0: v2ef339_0 = PHI v3392f9, v3392e4(0x0)
    0x2f10x339: v3392f1 = ADD v2ef339_0, v3392df
    0x2f20x339: v3392f2 = MLOAD v3392f1
    0x2f50x339: v3392f5 = ADD v2ef339_0, v3392dc
    0x2f60x339: MSTORE v3392f5, v3392f2
    0x2f70x339: v3392f7(0x20) = CONST 
    0x2f90x339: v3392f9 = ADD v3392f7(0x20), v2ef339_0
    0x2fa0x339: v3392fa(0x2e6) = CONST 
    0x2fd0x339: JUMP v3392fa(0x2e6)

}

function transfer(address,uint256)() public {
    Begin block 0x3ea
    prev=[], succ=[0x3f2, 0x3f6]
    =================================
    0x3eb: v3eb = CALLVALUE 
    0x3ed: v3ed = ISZERO v3eb
    0x3ee: v3ee(0x3f6) = CONST 
    0x3f1: JUMPI v3ee(0x3f6), v3ed

    Begin block 0x3f2
    prev=[0x3ea], succ=[]
    =================================
    0x3f2: v3f2(0x0) = CONST 
    0x3f5: REVERT v3f2(0x0), v3f2(0x0)

    Begin block 0x3f6
    prev=[0x3ea], succ=[0x409, 0x40d]
    =================================
    0x3f8: v3f8(0x149c) = CONST 
    0x3fb: v3fb(0x4) = CONST 
    0x3fe: v3fe = CALLDATASIZE 
    0x3ff: v3ff = SUB v3fe, v3fb(0x4)
    0x400: v400(0x40) = CONST 
    0x403: v403 = LT v3ff, v400(0x40)
    0x404: v404 = ISZERO v403
    0x405: v405(0x40d) = CONST 
    0x408: JUMPI v405(0x40d), v404

    Begin block 0x409
    prev=[0x3f6], succ=[]
    =================================
    0x409: v409(0x0) = CONST 
    0x40c: REVERT v409(0x0), v409(0x0)

    Begin block 0x40d
    prev=[0x3f6], succ=[0xb78]
    =================================
    0x40f: v40f(0x1) = CONST 
    0x411: v411(0x1) = CONST 
    0x413: v413(0xa0) = CONST 
    0x415: v415(0x10000000000000000000000000000000000000000) = SHL v413(0xa0), v411(0x1)
    0x416: v416(0xffffffffffffffffffffffffffffffffffffffff) = SUB v415(0x10000000000000000000000000000000000000000), v40f(0x1)
    0x418: v418 = CALLDATALOAD v3fb(0x4)
    0x419: v419 = AND v418, v416(0xffffffffffffffffffffffffffffffffffffffff)
    0x41b: v41b(0x20) = CONST 
    0x41d: v41d(0x24) = ADD v41b(0x20), v3fb(0x4)
    0x41e: v41e = CALLDATALOAD v41d(0x24)
    0x41f: v41f(0xb78) = CONST 
    0x422: JUMP v41f(0xb78)

    Begin block 0xb78
    prev=[0x40d], succ=[0xa440x3ea]
    =================================
    0xb79: vb79(0x0) = CONST 
    0xb7b: vb7b(0x1a52) = CONST 
    0xb7e: vb7e(0xa44) = CONST 
    0xb81: JUMP vb7e(0xa44)

    Begin block 0xa440x3ea
    prev=[0xb78], succ=[0xa8b0x3ea, 0xaac0x3ea]
    =================================
    0xa450x3ea: v3eaa45(0x13) = CONST 
    0xa470x3ea: v3eaa47 = SLOAD v3eaa45(0x13)
    0xa480x3ea: v3eaa48(0x40) = CONST 
    0xa4a0x3ea: v3eaa4a = MLOAD v3eaa48(0x40)
    0xa4b0x3ea: v3eaa4b(0x60) = CONST 
    0xa4e0x3ea: v3eaa4e(0x0) = CONST 
    0xa510x3ea: v3eaa51(0x1) = CONST 
    0xa530x3ea: v3eaa53(0x1) = CONST 
    0xa550x3ea: v3eaa55(0xa0) = CONST 
    0xa570x3ea: v3eaa57(0x10000000000000000000000000000000000000000) = SHL v3eaa55(0xa0), v3eaa53(0x1)
    0xa580x3ea: v3eaa58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3eaa57(0x10000000000000000000000000000000000000000), v3eaa51(0x1)
    0xa5b0x3ea: v3eaa5b = AND v3eaa47, v3eaa58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x3ea: v3eaa5f = CALLDATASIZE 
    0xa670x3ea: CALLDATACOPY v3eaa4a, v3eaa4e(0x0), v3eaa5f
    0xa680x3ea: v3eaa68(0x40) = CONST 
    0xa6a0x3ea: v3eaa6a = MLOAD v3eaa68(0x40)
    0xa6c0x3ea: v3eaa6c = ADD v3eaa4a, v3eaa5f
    0xa6f0x3ea: v3eaa6f(0x0) = CONST 
    0xa790x3ea: v3eaa79 = SUB v3eaa6c, v3eaa6a
    0xa7c0x3ea: v3eaa7c = GAS 
    0xa7d0x3ea: v3eaa7d = DELEGATECALL v3eaa7c, v3eaa5b, v3eaa6a, v3eaa79, v3eaa6a, v3eaa6f(0x0)
    0xa810x3ea: v3eaa81 = RETURNDATASIZE 
    0xa830x3ea: v3eaa83(0x0) = CONST 
    0xa860x3ea: v3eaa86 = EQ v3eaa81, v3eaa83(0x0)
    0xa870x3ea: v3eaa87(0xaac) = CONST 
    0xa8a0x3ea: JUMPI v3eaa87(0xaac), v3eaa86

    Begin block 0xa8b0x3ea
    prev=[0xa440x3ea], succ=[0xab10x3ea]
    =================================
    0xa8b0x3ea: v3eaa8b(0x40) = CONST 
    0xa8d0x3ea: v3eaa8d = MLOAD v3eaa8b(0x40)
    0xa900x3ea: v3eaa90(0x1f) = CONST 
    0xa920x3ea: v3eaa92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3eaa90(0x1f)
    0xa930x3ea: v3eaa93(0x3f) = CONST 
    0xa950x3ea: v3eaa95 = RETURNDATASIZE 
    0xa960x3ea: v3eaa96 = ADD v3eaa95, v3eaa93(0x3f)
    0xa970x3ea: v3eaa97 = AND v3eaa96, v3eaa92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x3ea: v3eaa99 = ADD v3eaa8d, v3eaa97
    0xa9a0x3ea: v3eaa9a(0x40) = CONST 
    0xa9c0x3ea: MSTORE v3eaa9a(0x40), v3eaa99
    0xa9d0x3ea: v3eaa9d = RETURNDATASIZE 
    0xa9f0x3ea: MSTORE v3eaa8d, v3eaa9d
    0xaa00x3ea: v3eaaa0 = RETURNDATASIZE 
    0xaa10x3ea: v3eaaa1(0x0) = CONST 
    0xaa30x3ea: v3eaaa3(0x20) = CONST 
    0xaa60x3ea: v3eaaa6 = ADD v3eaa8d, v3eaaa3(0x20)
    0xaa70x3ea: RETURNDATACOPY v3eaaa6, v3eaaa1(0x0), v3eaaa0
    0xaa80x3ea: v3eaaa8(0xab1) = CONST 
    0xaab0x3ea: JUMP v3eaaa8(0xab1)

    Begin block 0xab10x3ea
    prev=[0xa8b0x3ea, 0xaac0x3ea], succ=[0xac50x3ea, 0x14560x3ea]
    =================================
    0xab60x3ea: v3eaab6(0x40) = CONST 
    0xab80x3ea: v3eaab8 = MLOAD v3eaab6(0x40)
    0xab90x3ea: v3eaab9 = RETURNDATASIZE 
    0xaba0x3ea: v3eaaba(0x0) = CONST 
    0xabd0x3ea: RETURNDATACOPY v3eaab8, v3eaaba(0x0), v3eaab9
    0xac00x3ea: v3eaac0 = ISZERO v3eaa7d
    0xac10x3ea: v3eaac1(0x1456) = CONST 
    0xac40x3ea: JUMPI v3eaac1(0x1456), v3eaac0

    Begin block 0xac50x3ea
    prev=[0xab10x3ea], succ=[]
    =================================
    0xac50x3ea: v3eaac5 = RETURNDATASIZE 
    0xac70x3ea: RETURN v3eaab8, v3eaac5

    Begin block 0x14560x3ea
    prev=[0xab10x3ea], succ=[]
    =================================
    0x14570x3ea: v3ea1457 = RETURNDATASIZE 
    0x14590x3ea: REVERT v3eaab8, v3ea1457

    Begin block 0xaac0x3ea
    prev=[0xa440x3ea], succ=[0xab10x3ea]
    =================================
    0xaad0x3ea: v3eaaad(0x60) = CONST 

}

function maxScalingFactor()() public {
    Begin block 0x437
    prev=[], succ=[0x43f, 0x443]
    =================================
    0x438: v438 = CALLVALUE 
    0x43a: v43a = ISZERO v438
    0x43b: v43b(0x443) = CONST 
    0x43e: JUMPI v43b(0x443), v43a

    Begin block 0x43f
    prev=[0x437], succ=[]
    =================================
    0x43f: v43f(0x0) = CONST 
    0x442: REVERT v43f(0x0), v43f(0x0)

    Begin block 0x443
    prev=[0x437], succ=[0xb89]
    =================================
    0x445: v445(0x14cf) = CONST 
    0x448: v448(0xb89) = CONST 
    0x44b: JUMP v448(0xb89)

    Begin block 0xb89
    prev=[0x443], succ=[0x120f0x437]
    =================================
    0xb8a: vb8a(0x0) = CONST 
    0xb8c: vb8c(0xb93) = CONST 
    0xb8f: vb8f(0x120f) = CONST 
    0xb92: JUMP vb8f(0x120f)

    Begin block 0x120f0x437
    prev=[0xb89], succ=[0x12910x437]
    =================================
    0x12100x437: v4371210(0x60) = CONST 
    0x12120x437: v4371212(0x0) = CONST 
    0x12140x437: v4371214 = ADDRESS 
    0x12150x437: v4371215(0x1) = CONST 
    0x12170x437: v4371217(0x1) = CONST 
    0x12190x437: v4371219(0xa0) = CONST 
    0x121b0x437: v437121b(0x10000000000000000000000000000000000000000) = SHL v4371219(0xa0), v4371217(0x1)
    0x121c0x437: v437121c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v437121b(0x10000000000000000000000000000000000000000), v4371215(0x1)
    0x121d0x437: v437121d = AND v437121c(0xffffffffffffffffffffffffffffffffffffffff), v4371214
    0x121e0x437: v437121e(0x0) = CONST 
    0x12200x437: v4371220 = CALLDATASIZE 
    0x12210x437: v4371221(0x40) = CONST 
    0x12230x437: v4371223 = MLOAD v4371221(0x40)
    0x12240x437: v4371224(0x24) = CONST 
    0x12260x437: v4371226 = ADD v4371224(0x24), v4371223
    0x12290x437: v4371229(0x20) = CONST 
    0x122b0x437: v437122b = ADD v4371229(0x20), v4371226
    0x122e0x437: v437122e(0x20) = SUB v437122b, v4371226
    0x12300x437: MSTORE v4371226, v437122e(0x20)
    0x12360x437: MSTORE v437122b, v4371220
    0x12370x437: v4371237(0x20) = CONST 
    0x12390x437: v4371239 = ADD v4371237(0x20), v437122b
    0x123f0x437: CALLDATACOPY v4371239, v437121e(0x0), v4371220
    0x12400x437: v4371240(0x0) = CONST 
    0x12440x437: v4371244 = ADD v4371220, v4371239
    0x12450x437: MSTORE v4371244, v4371240(0x0)
    0x12460x437: v4371246(0x40) = CONST 
    0x12490x437: v4371249 = MLOAD v4371246(0x40)
    0x124a0x437: v437124a(0x1f) = CONST 
    0x124e0x437: v437124e = ADD v4371220, v437124a(0x1f)
    0x124f0x437: v437124f(0x1f) = CONST 
    0x12510x437: v4371251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v437124f(0x1f)
    0x12540x437: v4371254 = AND v4371251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v437124e
    0x12570x437: v4371257 = ADD v4371239, v4371254
    0x125a0x437: v437125a = SUB v4371257, v4371249
    0x125d0x437: v437125d = ADD v4371251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v437125a
    0x125f0x437: MSTORE v4371249, v437125d
    0x12620x437: MSTORE v4371246(0x40), v4371257
    0x12630x437: v4371263(0x20) = CONST 
    0x12660x437: v4371266 = ADD v4371249, v4371263(0x20)
    0x12680x437: v4371268 = MLOAD v4371266
    0x12690x437: v4371269(0x1) = CONST 
    0x126b0x437: v437126b(0x1) = CONST 
    0x126d0x437: v437126d(0xe0) = CONST 
    0x126f0x437: v437126f(0x100000000000000000000000000000000000000000000000000000000) = SHL v437126d(0xe0), v437126b(0x1)
    0x12700x437: v4371270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v437126f(0x100000000000000000000000000000000000000000000000000000000), v4371269(0x1)
    0x12710x437: v4371271 = AND v4371270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v4371268
    0x12720x437: v4371272(0x933c1ed) = CONST 
    0x12770x437: v4371277(0xe0) = CONST 
    0x12790x437: v4371279(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v4371277(0xe0), v4371272(0x933c1ed)
    0x127a0x437: v437127a = OR v4371279(0x933c1ed00000000000000000000000000000000000000000000000000000000), v4371271
    0x127c0x437: MSTORE v4371266, v437127a
    0x127e0x437: v437127e = MLOAD v4371246(0x40)
    0x12800x437: v4371280 = MLOAD v4371249

    Begin block 0x12910x437
    prev=[0x129a0x437, 0x120f0x437], succ=[0x12b00x437, 0x129a0x437]
    =================================
    0x12910x437_0x2: v1291437_2 = PHI v43712a3, v4371280
    0x12920x437: v4371292(0x20) = CONST 
    0x12950x437: v4371295 = LT v1291437_2, v4371292(0x20)
    0x12960x437: v4371296(0x12b0) = CONST 
    0x12990x437: JUMPI v4371296(0x12b0), v4371295

    Begin block 0x12b00x437
    prev=[0x12910x437], succ=[0x12ef0x437, 0x13100x437]
    =================================
    0x12b00x437_0x0: v12b0437_0 = PHI v43712ab, v4371266
    0x12b00x437_0x1: v12b0437_1 = PHI v43712a9, v437127e
    0x12b00x437_0x2: v12b0437_2 = PHI v43712a3, v4371280
    0x12b10x437: v43712b1(0x1) = CONST 
    0x12b40x437: v43712b4(0x20) = CONST 
    0x12b60x437: v43712b6 = SUB v43712b4(0x20), v12b0437_2
    0x12b70x437: v43712b7(0x100) = CONST 
    0x12ba0x437: v43712ba = EXP v43712b7(0x100), v43712b6
    0x12bb0x437: v43712bb = SUB v43712ba, v43712b1(0x1)
    0x12bd0x437: v43712bd = NOT v43712bb
    0x12bf0x437: v43712bf = MLOAD v12b0437_0
    0x12c00x437: v43712c0 = AND v43712bf, v43712bd
    0x12c30x437: v43712c3 = MLOAD v12b0437_1
    0x12c40x437: v43712c4 = AND v43712c3, v43712bb
    0x12c70x437: v43712c7 = OR v43712c0, v43712c4
    0x12c90x437: MSTORE v12b0437_1, v43712c7
    0x12d20x437: v43712d2 = ADD v4371280, v437127e
    0x12d60x437: v43712d6(0x0) = CONST 
    0x12d80x437: v43712d8(0x40) = CONST 
    0x12da0x437: v43712da = MLOAD v43712d8(0x40)
    0x12dd0x437: v43712dd = SUB v43712d2, v43712da
    0x12e00x437: v43712e0 = GAS 
    0x12e10x437: v43712e1 = STATICCALL v43712e0, v437121d, v43712da, v43712dd, v43712da, v43712d6(0x0)
    0x12e50x437: v43712e5 = RETURNDATASIZE 
    0x12e70x437: v43712e7(0x0) = CONST 
    0x12ea0x437: v43712ea = EQ v43712e5, v43712e7(0x0)
    0x12eb0x437: v43712eb(0x1310) = CONST 
    0x12ee0x437: JUMPI v43712eb(0x1310), v43712ea

    Begin block 0x12ef0x437
    prev=[0x12b00x437], succ=[0x13150x437]
    =================================
    0x12ef0x437: v43712ef(0x40) = CONST 
    0x12f10x437: v43712f1 = MLOAD v43712ef(0x40)
    0x12f40x437: v43712f4(0x1f) = CONST 
    0x12f60x437: v43712f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v43712f4(0x1f)
    0x12f70x437: v43712f7(0x3f) = CONST 
    0x12f90x437: v43712f9 = RETURNDATASIZE 
    0x12fa0x437: v43712fa = ADD v43712f9, v43712f7(0x3f)
    0x12fb0x437: v43712fb = AND v43712fa, v43712f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12fd0x437: v43712fd = ADD v43712f1, v43712fb
    0x12fe0x437: v43712fe(0x40) = CONST 
    0x13000x437: MSTORE v43712fe(0x40), v43712fd
    0x13010x437: v4371301 = RETURNDATASIZE 
    0x13030x437: MSTORE v43712f1, v4371301
    0x13040x437: v4371304 = RETURNDATASIZE 
    0x13050x437: v4371305(0x0) = CONST 
    0x13070x437: v4371307(0x20) = CONST 
    0x130a0x437: v437130a = ADD v43712f1, v4371307(0x20)
    0x130b0x437: RETURNDATACOPY v437130a, v4371305(0x0), v4371304
    0x130c0x437: v437130c(0x1315) = CONST 
    0x130f0x437: JUMP v437130c(0x1315)

    Begin block 0x13150x437
    prev=[0x12ef0x437, 0x13100x437], succ=[0x13290x437, 0x14790x437]
    =================================
    0x131a0x437: v437131a(0x40) = CONST 
    0x131c0x437: v437131c = MLOAD v437131a(0x40)
    0x131d0x437: v437131d = RETURNDATASIZE 
    0x131e0x437: v437131e(0x0) = CONST 
    0x13210x437: RETURNDATACOPY v437131c, v437131e(0x0), v437131d
    0x13240x437: v4371324 = ISZERO v43712e1
    0x13250x437: v4371325(0x1479) = CONST 
    0x13280x437: JUMPI v4371325(0x1479), v4371324

    Begin block 0x13290x437
    prev=[0x13150x437], succ=[]
    =================================
    0x13290x437: v4371329 = RETURNDATASIZE 
    0x132a0x437: v437132a(0x40) = CONST 
    0x132d0x437: v437132d = ADD v437131c, v437132a(0x40)
    0x132e0x437: RETURN v437132d, v4371329

    Begin block 0x14790x437
    prev=[0x13150x437], succ=[]
    =================================
    0x147a0x437: v437147a = RETURNDATASIZE 
    0x147c0x437: REVERT v437131c, v437147a

    Begin block 0x13100x437
    prev=[0x12b00x437], succ=[0x13150x437]
    =================================
    0x13110x437: v4371311(0x60) = CONST 

    Begin block 0x129a0x437
    prev=[0x12910x437], succ=[0x12910x437]
    =================================
    0x129a0x437_0x0: v129a437_0 = PHI v43712ab, v4371266
    0x129a0x437_0x1: v129a437_1 = PHI v43712a9, v437127e
    0x129a0x437_0x2: v129a437_2 = PHI v43712a3, v4371280
    0x129b0x437: v437129b = MLOAD v129a437_0
    0x129d0x437: MSTORE v129a437_1, v437129b
    0x129e0x437: v437129e(0x1f) = CONST 
    0x12a00x437: v43712a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v437129e(0x1f)
    0x12a30x437: v43712a3 = ADD v129a437_2, v43712a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a50x437: v43712a5(0x20) = CONST 
    0x12a90x437: v43712a9 = ADD v43712a5(0x20), v129a437_1
    0x12ab0x437: v43712ab = ADD v43712a5(0x20), v129a437_0
    0x12ac0x437: v43712ac(0x1291) = CONST 
    0x12af0x437: JUMP v43712ac(0x1291)

}

function rebaser()() public {
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
    prev=[0x45e], succ=[0xb97]
    =================================
    0x46c: v46c(0x1500) = CONST 
    0x46f: v46f(0xb97) = CONST 
    0x472: JUMP v46f(0xb97)

    Begin block 0xb97
    prev=[0x46a], succ=[0x1500]
    =================================
    0xb98: vb98(0x5) = CONST 
    0xb9a: vb9a = SLOAD vb98(0x5)
    0xb9b: vb9b(0x1) = CONST 
    0xb9d: vb9d(0x1) = CONST 
    0xb9f: vb9f(0xa0) = CONST 
    0xba1: vba1(0x10000000000000000000000000000000000000000) = SHL vb9f(0xa0), vb9d(0x1)
    0xba2: vba2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vba1(0x10000000000000000000000000000000000000000), vb9b(0x1)
    0xba3: vba3 = AND vba2(0xffffffffffffffffffffffffffffffffffffffff), vb9a
    0xba5: JUMP v46c(0x1500)

    Begin block 0x1500
    prev=[0xb97], succ=[]
    =================================
    0x1501: v1501(0x40) = CONST 
    0x1504: v1504 = MLOAD v1501(0x40)
    0x1505: v1505(0x1) = CONST 
    0x1507: v1507(0x1) = CONST 
    0x1509: v1509(0xa0) = CONST 
    0x150b: v150b(0x10000000000000000000000000000000000000000) = SHL v1509(0xa0), v1507(0x1)
    0x150c: v150c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v150b(0x10000000000000000000000000000000000000000), v1505(0x1)
    0x150f: v150f = AND vba3, v150c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1511: MSTORE v1504, v150f
    0x1512: v1512 = MLOAD v1501(0x40)
    0x1516: v1516(0x0) = SUB v1504, v1512
    0x1517: v1517(0x20) = CONST 
    0x1519: v1519(0x20) = ADD v1517(0x20), v1516(0x0)
    0x151b: RETURN v1512, v1519(0x20)

}

function gov()() public {
    Begin block 0x48f
    prev=[], succ=[0x497, 0x49b]
    =================================
    0x490: v490 = CALLVALUE 
    0x492: v492 = ISZERO v490
    0x493: v493(0x49b) = CONST 
    0x496: JUMPI v493(0x49b), v492

    Begin block 0x497
    prev=[0x48f], succ=[]
    =================================
    0x497: v497(0x0) = CONST 
    0x49a: REVERT v497(0x0), v497(0x0)

    Begin block 0x49b
    prev=[0x48f], succ=[0xba6]
    =================================
    0x49d: v49d(0x153b) = CONST 
    0x4a0: v4a0(0xba6) = CONST 
    0x4a3: JUMP v4a0(0xba6)

    Begin block 0xba6
    prev=[0x49b], succ=[0x153b]
    =================================
    0xba7: vba7(0x3) = CONST 
    0xba9: vba9 = SLOAD vba7(0x3)
    0xbaa: vbaa(0x100) = CONST 
    0xbae: vbae = DIV vba9, vbaa(0x100)
    0xbaf: vbaf(0x1) = CONST 
    0xbb1: vbb1(0x1) = CONST 
    0xbb3: vbb3(0xa0) = CONST 
    0xbb5: vbb5(0x10000000000000000000000000000000000000000) = SHL vbb3(0xa0), vbb1(0x1)
    0xbb6: vbb6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb5(0x10000000000000000000000000000000000000000), vbaf(0x1)
    0xbb7: vbb7 = AND vbb6(0xffffffffffffffffffffffffffffffffffffffff), vbae
    0xbb9: JUMP v49d(0x153b)

    Begin block 0x153b
    prev=[0xba6], succ=[]
    =================================
    0x153c: v153c(0x40) = CONST 
    0x153f: v153f = MLOAD v153c(0x40)
    0x1540: v1540(0x1) = CONST 
    0x1542: v1542(0x1) = CONST 
    0x1544: v1544(0xa0) = CONST 
    0x1546: v1546(0x10000000000000000000000000000000000000000) = SHL v1544(0xa0), v1542(0x1)
    0x1547: v1547(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1546(0x10000000000000000000000000000000000000000), v1540(0x1)
    0x154a: v154a = AND vbb7, v1547(0xffffffffffffffffffffffffffffffffffffffff)
    0x154c: MSTORE v153f, v154a
    0x154d: v154d = MLOAD v153c(0x40)
    0x1551: v1551(0x0) = SUB v153f, v154d
    0x1552: v1552(0x20) = CONST 
    0x1554: v1554(0x20) = ADD v1552(0x20), v1551(0x0)
    0x1556: RETURN v154d, v1554(0x20)

}

function totalSupply()() public {
    Begin block 0x4a4
    prev=[], succ=[0x4ac, 0x4b0]
    =================================
    0x4a5: v4a5 = CALLVALUE 
    0x4a7: v4a7 = ISZERO v4a5
    0x4a8: v4a8(0x4b0) = CONST 
    0x4ab: JUMPI v4a8(0x4b0), v4a7

    Begin block 0x4ac
    prev=[0x4a4], succ=[]
    =================================
    0x4ac: v4ac(0x0) = CONST 
    0x4af: REVERT v4ac(0x0), v4ac(0x0)

    Begin block 0x4b0
    prev=[0x4a4], succ=[0xbba]
    =================================
    0x4b2: v4b2(0x1576) = CONST 
    0x4b5: v4b5(0xbba) = CONST 
    0x4b8: JUMP v4b5(0xbba)

    Begin block 0xbba
    prev=[0x4b0], succ=[0x1576]
    =================================
    0xbbb: vbbb(0x7) = CONST 
    0xbbd: vbbd = SLOAD vbbb(0x7)
    0xbbf: JUMP v4b2(0x1576)

    Begin block 0x1576
    prev=[0xbba], succ=[]
    =================================
    0x1577: v1577(0x40) = CONST 
    0x157a: v157a = MLOAD v1577(0x40)
    0x157d: MSTORE v157a, vbbd
    0x157e: v157e = MLOAD v1577(0x40)
    0x1582: v1582(0x0) = SUB v157a, v157e
    0x1583: v1583(0x20) = CONST 
    0x1585: v1585(0x20) = ADD v1583(0x20), v1582(0x0)
    0x1587: RETURN v157e, v1585(0x20)

}

function addressWhiteList(uint256)() public {
    Begin block 0x4b9
    prev=[], succ=[0x4c1, 0x4c5]
    =================================
    0x4ba: v4ba = CALLVALUE 
    0x4bc: v4bc = ISZERO v4ba
    0x4bd: v4bd(0x4c5) = CONST 
    0x4c0: JUMPI v4bd(0x4c5), v4bc

    Begin block 0x4c1
    prev=[0x4b9], succ=[]
    =================================
    0x4c1: v4c1(0x0) = CONST 
    0x4c4: REVERT v4c1(0x0), v4c1(0x0)

    Begin block 0x4c5
    prev=[0x4b9], succ=[0x4d8, 0x4dc]
    =================================
    0x4c7: v4c7(0x15a7) = CONST 
    0x4ca: v4ca(0x4) = CONST 
    0x4cd: v4cd = CALLDATASIZE 
    0x4ce: v4ce = SUB v4cd, v4ca(0x4)
    0x4cf: v4cf(0x20) = CONST 
    0x4d2: v4d2 = LT v4ce, v4cf(0x20)
    0x4d3: v4d3 = ISZERO v4d2
    0x4d4: v4d4(0x4dc) = CONST 
    0x4d7: JUMPI v4d4(0x4dc), v4d3

    Begin block 0x4d8
    prev=[0x4c5], succ=[]
    =================================
    0x4d8: v4d8(0x0) = CONST 
    0x4db: REVERT v4d8(0x0), v4d8(0x0)

    Begin block 0x4dc
    prev=[0x4c5], succ=[0xbc0]
    =================================
    0x4de: v4de = CALLDATALOAD v4ca(0x4)
    0x4df: v4df(0xbc0) = CONST 
    0x4e2: JUMP v4df(0xbc0)

    Begin block 0xbc0
    prev=[0x4dc], succ=[0xbcc, 0xbcd]
    =================================
    0xbc1: vbc1(0xe) = CONST 
    0xbc5: vbc5 = SLOAD vbc1(0xe)
    0xbc7: vbc7 = LT v4de, vbc5
    0xbc8: vbc8(0xbcd) = CONST 
    0xbcb: JUMPI vbc8(0xbcd), vbc7

    Begin block 0xbcc
    prev=[0xbc0], succ=[]
    =================================
    0xbcc: THROW 

    Begin block 0xbcd
    prev=[0xbc0], succ=[0x15a7]
    =================================
    0xbce: vbce(0x0) = CONST 
    0xbd2: MSTORE vbce(0x0), vbc1(0xe)
    0xbd3: vbd3(0x20) = CONST 
    0xbd7: vbd7 = SHA3 vbce(0x0), vbd3(0x20)
    0xbd8: vbd8 = ADD vbd7, v4de
    0xbd9: vbd9 = SLOAD vbd8
    0xbda: vbda(0x1) = CONST 
    0xbdc: vbdc(0x1) = CONST 
    0xbde: vbde(0xa0) = CONST 
    0xbe0: vbe0(0x10000000000000000000000000000000000000000) = SHL vbde(0xa0), vbdc(0x1)
    0xbe1: vbe1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbe0(0x10000000000000000000000000000000000000000), vbda(0x1)
    0xbe2: vbe2 = AND vbe1(0xffffffffffffffffffffffffffffffffffffffff), vbd9
    0xbe6: JUMP v4c7(0x15a7)

    Begin block 0x15a7
    prev=[0xbcd], succ=[]
    =================================
    0x15a8: v15a8(0x40) = CONST 
    0x15ab: v15ab = MLOAD v15a8(0x40)
    0x15ac: v15ac(0x1) = CONST 
    0x15ae: v15ae(0x1) = CONST 
    0x15b0: v15b0(0xa0) = CONST 
    0x15b2: v15b2(0x10000000000000000000000000000000000000000) = SHL v15b0(0xa0), v15ae(0x1)
    0x15b3: v15b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15b2(0x10000000000000000000000000000000000000000), v15ac(0x1)
    0x15b6: v15b6 = AND vbe2, v15b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x15b8: MSTORE v15ab, v15b6
    0x15b9: v15b9 = MLOAD v15a8(0x40)
    0x15bd: v15bd(0x0) = SUB v15ab, v15b9
    0x15be: v15be(0x20) = CONST 
    0x15c0: v15c0(0x20) = ADD v15be(0x20), v15bd(0x0)
    0x15c2: RETURN v15b9, v15c0(0x20)

}

function DOMAIN_TYPEHASH()() public {
    Begin block 0x4e3
    prev=[], succ=[0x4eb, 0x4ef]
    =================================
    0x4e4: v4e4 = CALLVALUE 
    0x4e6: v4e6 = ISZERO v4e4
    0x4e7: v4e7(0x4ef) = CONST 
    0x4ea: JUMPI v4e7(0x4ef), v4e6

    Begin block 0x4eb
    prev=[0x4e3], succ=[]
    =================================
    0x4eb: v4eb(0x0) = CONST 
    0x4ee: REVERT v4eb(0x0), v4eb(0x0)

    Begin block 0x4ef
    prev=[0x4e3], succ=[0xbe7]
    =================================
    0x4f1: v4f1(0x15e2) = CONST 
    0x4f4: v4f4(0xbe7) = CONST 
    0x4f7: JUMP v4f4(0xbe7)

    Begin block 0xbe7
    prev=[0x4ef], succ=[0x15e2]
    =================================
    0xbe8: vbe8(0x40) = CONST 
    0xbea: vbea = MLOAD vbe8(0x40)
    0xbec: vbec(0x43) = CONST 
    0xbee: vbee(0x1398) = CONST 
    0xbf2: CODECOPY vbea, vbee(0x1398), vbec(0x43)
    0xbf3: vbf3(0x43) = CONST 
    0xbf5: vbf5 = ADD vbf3(0x43), vbea
    0xbf8: vbf8(0x40) = CONST 
    0xbfa: vbfa = MLOAD vbf8(0x40)
    0xbfd: vbfd(0x43) = SUB vbf5, vbfa
    0xbff: vbff = SHA3 vbfa, vbfd(0x43)
    0xc01: JUMP v4f1(0x15e2)

    Begin block 0x15e2
    prev=[0xbe7], succ=[]
    =================================
    0x15e3: v15e3(0x40) = CONST 
    0x15e6: v15e6 = MLOAD v15e3(0x40)
    0x15e9: MSTORE v15e6, vbff
    0x15ea: v15ea = MLOAD v15e3(0x40)
    0x15ee: v15ee(0x0) = SUB v15e6, v15ea
    0x15ef: v15ef(0x20) = CONST 
    0x15f1: v15f1(0x20) = ADD v15ef(0x20), v15ee(0x0)
    0x15f3: RETURN v15ea, v15f1(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x4f8
    prev=[], succ=[0x500, 0x504]
    =================================
    0x4f9: v4f9 = CALLVALUE 
    0x4fb: v4fb = ISZERO v4f9
    0x4fc: v4fc(0x504) = CONST 
    0x4ff: JUMPI v4fc(0x504), v4fb

    Begin block 0x500
    prev=[0x4f8], succ=[]
    =================================
    0x500: v500(0x0) = CONST 
    0x503: REVERT v500(0x0), v500(0x0)

    Begin block 0x504
    prev=[0x4f8], succ=[0x517, 0x51b]
    =================================
    0x506: v506(0x1613) = CONST 
    0x509: v509(0x4) = CONST 
    0x50c: v50c = CALLDATASIZE 
    0x50d: v50d = SUB v50c, v509(0x4)
    0x50e: v50e(0x60) = CONST 
    0x511: v511 = LT v50d, v50e(0x60)
    0x512: v512 = ISZERO v511
    0x513: v513(0x51b) = CONST 
    0x516: JUMPI v513(0x51b), v512

    Begin block 0x517
    prev=[0x504], succ=[]
    =================================
    0x517: v517(0x0) = CONST 
    0x51a: REVERT v517(0x0), v517(0x0)

    Begin block 0x51b
    prev=[0x504], succ=[0xc020x4f8]
    =================================
    0x51d: v51d(0x1) = CONST 
    0x51f: v51f(0x1) = CONST 
    0x521: v521(0xa0) = CONST 
    0x523: v523(0x10000000000000000000000000000000000000000) = SHL v521(0xa0), v51f(0x1)
    0x524: v524(0xffffffffffffffffffffffffffffffffffffffff) = SUB v523(0x10000000000000000000000000000000000000000), v51d(0x1)
    0x526: v526 = CALLDATALOAD v509(0x4)
    0x528: v528 = AND v524(0xffffffffffffffffffffffffffffffffffffffff), v526
    0x52a: v52a(0x20) = CONST 
    0x52d: v52d(0x24) = ADD v509(0x4), v52a(0x20)
    0x52e: v52e = CALLDATALOAD v52d(0x24)
    0x531: v531 = AND v524(0xffffffffffffffffffffffffffffffffffffffff), v52e
    0x533: v533(0x40) = CONST 
    0x535: v535(0x44) = ADD v533(0x40), v509(0x4)
    0x536: v536 = CALLDATALOAD v535(0x44)
    0x537: v537(0xc02) = CONST 
    0x53a: JUMP v537(0xc02)

    Begin block 0xc020x4f8
    prev=[0x51b], succ=[0xa440x4f8]
    =================================
    0xc030x4f8: v4f8c03(0x0) = CONST 
    0xc050x4f8: v4f8c05(0xc0c) = CONST 
    0xc080x4f8: v4f8c08(0xa44) = CONST 
    0xc0b0x4f8: JUMP v4f8c08(0xa44)

    Begin block 0xa440x4f8
    prev=[0xc020x4f8], succ=[0xa8b0x4f8, 0xaac0x4f8]
    =================================
    0xa450x4f8: v4f8a45(0x13) = CONST 
    0xa470x4f8: v4f8a47 = SLOAD v4f8a45(0x13)
    0xa480x4f8: v4f8a48(0x40) = CONST 
    0xa4a0x4f8: v4f8a4a = MLOAD v4f8a48(0x40)
    0xa4b0x4f8: v4f8a4b(0x60) = CONST 
    0xa4e0x4f8: v4f8a4e(0x0) = CONST 
    0xa510x4f8: v4f8a51(0x1) = CONST 
    0xa530x4f8: v4f8a53(0x1) = CONST 
    0xa550x4f8: v4f8a55(0xa0) = CONST 
    0xa570x4f8: v4f8a57(0x10000000000000000000000000000000000000000) = SHL v4f8a55(0xa0), v4f8a53(0x1)
    0xa580x4f8: v4f8a58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f8a57(0x10000000000000000000000000000000000000000), v4f8a51(0x1)
    0xa5b0x4f8: v4f8a5b = AND v4f8a47, v4f8a58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x4f8: v4f8a5f = CALLDATASIZE 
    0xa670x4f8: CALLDATACOPY v4f8a4a, v4f8a4e(0x0), v4f8a5f
    0xa680x4f8: v4f8a68(0x40) = CONST 
    0xa6a0x4f8: v4f8a6a = MLOAD v4f8a68(0x40)
    0xa6c0x4f8: v4f8a6c = ADD v4f8a4a, v4f8a5f
    0xa6f0x4f8: v4f8a6f(0x0) = CONST 
    0xa790x4f8: v4f8a79 = SUB v4f8a6c, v4f8a6a
    0xa7c0x4f8: v4f8a7c = GAS 
    0xa7d0x4f8: v4f8a7d = DELEGATECALL v4f8a7c, v4f8a5b, v4f8a6a, v4f8a79, v4f8a6a, v4f8a6f(0x0)
    0xa810x4f8: v4f8a81 = RETURNDATASIZE 
    0xa830x4f8: v4f8a83(0x0) = CONST 
    0xa860x4f8: v4f8a86 = EQ v4f8a81, v4f8a83(0x0)
    0xa870x4f8: v4f8a87(0xaac) = CONST 
    0xa8a0x4f8: JUMPI v4f8a87(0xaac), v4f8a86

    Begin block 0xa8b0x4f8
    prev=[0xa440x4f8], succ=[0xab10x4f8]
    =================================
    0xa8b0x4f8: v4f8a8b(0x40) = CONST 
    0xa8d0x4f8: v4f8a8d = MLOAD v4f8a8b(0x40)
    0xa900x4f8: v4f8a90(0x1f) = CONST 
    0xa920x4f8: v4f8a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v4f8a90(0x1f)
    0xa930x4f8: v4f8a93(0x3f) = CONST 
    0xa950x4f8: v4f8a95 = RETURNDATASIZE 
    0xa960x4f8: v4f8a96 = ADD v4f8a95, v4f8a93(0x3f)
    0xa970x4f8: v4f8a97 = AND v4f8a96, v4f8a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x4f8: v4f8a99 = ADD v4f8a8d, v4f8a97
    0xa9a0x4f8: v4f8a9a(0x40) = CONST 
    0xa9c0x4f8: MSTORE v4f8a9a(0x40), v4f8a99
    0xa9d0x4f8: v4f8a9d = RETURNDATASIZE 
    0xa9f0x4f8: MSTORE v4f8a8d, v4f8a9d
    0xaa00x4f8: v4f8aa0 = RETURNDATASIZE 
    0xaa10x4f8: v4f8aa1(0x0) = CONST 
    0xaa30x4f8: v4f8aa3(0x20) = CONST 
    0xaa60x4f8: v4f8aa6 = ADD v4f8a8d, v4f8aa3(0x20)
    0xaa70x4f8: RETURNDATACOPY v4f8aa6, v4f8aa1(0x0), v4f8aa0
    0xaa80x4f8: v4f8aa8(0xab1) = CONST 
    0xaab0x4f8: JUMP v4f8aa8(0xab1)

    Begin block 0xab10x4f8
    prev=[0xa8b0x4f8, 0xaac0x4f8], succ=[0xac50x4f8, 0x14560x4f8]
    =================================
    0xab60x4f8: v4f8ab6(0x40) = CONST 
    0xab80x4f8: v4f8ab8 = MLOAD v4f8ab6(0x40)
    0xab90x4f8: v4f8ab9 = RETURNDATASIZE 
    0xaba0x4f8: v4f8aba(0x0) = CONST 
    0xabd0x4f8: RETURNDATACOPY v4f8ab8, v4f8aba(0x0), v4f8ab9
    0xac00x4f8: v4f8ac0 = ISZERO v4f8a7d
    0xac10x4f8: v4f8ac1(0x1456) = CONST 
    0xac40x4f8: JUMPI v4f8ac1(0x1456), v4f8ac0

    Begin block 0xac50x4f8
    prev=[0xab10x4f8], succ=[]
    =================================
    0xac50x4f8: v4f8ac5 = RETURNDATASIZE 
    0xac70x4f8: RETURN v4f8ab8, v4f8ac5

    Begin block 0x14560x4f8
    prev=[0xab10x4f8], succ=[]
    =================================
    0x14570x4f8: v4f81457 = RETURNDATASIZE 
    0x14590x4f8: REVERT v4f8ab8, v4f81457

    Begin block 0xaac0x4f8
    prev=[0xa440x4f8], succ=[0xab10x4f8]
    =================================
    0xaad0x4f8: v4f8aad(0x60) = CONST 

}

function pendingGov()() public {
    Begin block 0x53b
    prev=[], succ=[0x543, 0x547]
    =================================
    0x53c: v53c = CALLVALUE 
    0x53e: v53e = ISZERO v53c
    0x53f: v53f(0x547) = CONST 
    0x542: JUMPI v53f(0x547), v53e

    Begin block 0x543
    prev=[0x53b], succ=[]
    =================================
    0x543: v543(0x0) = CONST 
    0x546: REVERT v543(0x0), v543(0x0)

    Begin block 0x547
    prev=[0x53b], succ=[0xc14]
    =================================
    0x549: v549(0x1646) = CONST 
    0x54c: v54c(0xc14) = CONST 
    0x54f: JUMP v54c(0xc14)

    Begin block 0xc14
    prev=[0x547], succ=[0x1646]
    =================================
    0xc15: vc15(0x4) = CONST 
    0xc17: vc17 = SLOAD vc15(0x4)
    0xc18: vc18(0x1) = CONST 
    0xc1a: vc1a(0x1) = CONST 
    0xc1c: vc1c(0xa0) = CONST 
    0xc1e: vc1e(0x10000000000000000000000000000000000000000) = SHL vc1c(0xa0), vc1a(0x1)
    0xc1f: vc1f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc1e(0x10000000000000000000000000000000000000000), vc18(0x1)
    0xc20: vc20 = AND vc1f(0xffffffffffffffffffffffffffffffffffffffff), vc17
    0xc22: JUMP v549(0x1646)

    Begin block 0x1646
    prev=[0xc14], succ=[]
    =================================
    0x1647: v1647(0x40) = CONST 
    0x164a: v164a = MLOAD v1647(0x40)
    0x164b: v164b(0x1) = CONST 
    0x164d: v164d(0x1) = CONST 
    0x164f: v164f(0xa0) = CONST 
    0x1651: v1651(0x10000000000000000000000000000000000000000) = SHL v164f(0xa0), v164d(0x1)
    0x1652: v1652(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1651(0x10000000000000000000000000000000000000000), v164b(0x1)
    0x1655: v1655 = AND vc20, v1652(0xffffffffffffffffffffffffffffffffffffffff)
    0x1657: MSTORE v164a, v1655
    0x1658: v1658 = MLOAD v1647(0x40)
    0x165c: v165c(0x0) = SUB v164a, v1658
    0x165d: v165d(0x20) = CONST 
    0x165f: v165f(0x20) = ADD v165d(0x20), v165c(0x0)
    0x1661: RETURN v1658, v165f(0x20)

}

function decimals()() public {
    Begin block 0x550
    prev=[], succ=[0x558, 0x55c]
    =================================
    0x551: v551 = CALLVALUE 
    0x553: v553 = ISZERO v551
    0x554: v554(0x55c) = CONST 
    0x557: JUMPI v554(0x55c), v553

    Begin block 0x558
    prev=[0x550], succ=[]
    =================================
    0x558: v558(0x0) = CONST 
    0x55b: REVERT v558(0x0), v558(0x0)

    Begin block 0x55c
    prev=[0x550], succ=[0xc23]
    =================================
    0x55e: v55e(0x565) = CONST 
    0x561: v561(0xc23) = CONST 
    0x564: JUMP v561(0xc23)

    Begin block 0xc23
    prev=[0x55c], succ=[0x565]
    =================================
    0xc24: vc24(0x3) = CONST 
    0xc26: vc26 = SLOAD vc24(0x3)
    0xc27: vc27(0xff) = CONST 
    0xc29: vc29 = AND vc27(0xff), vc26
    0xc2b: JUMP v55e(0x565)

    Begin block 0x565
    prev=[0xc23], succ=[]
    =================================
    0x566: v566(0x40) = CONST 
    0x569: v569 = MLOAD v566(0x40)
    0x56a: v56a(0xff) = CONST 
    0x56e: v56e = AND vc29, v56a(0xff)
    0x570: MSTORE v569, v56e
    0x571: v571 = MLOAD v566(0x40)
    0x575: v575(0x0) = SUB v569, v571
    0x576: v576(0x20) = CONST 
    0x578: v578(0x20) = ADD v576(0x20), v575(0x0)
    0x57a: RETURN v571, v578(0x20)

}

function gameStart()() public {
    Begin block 0x57b
    prev=[], succ=[0x583, 0x587]
    =================================
    0x57c: v57c = CALLVALUE 
    0x57e: v57e = ISZERO v57c
    0x57f: v57f(0x587) = CONST 
    0x582: JUMPI v57f(0x587), v57e

    Begin block 0x583
    prev=[0x57b], succ=[]
    =================================
    0x583: v583(0x0) = CONST 
    0x586: REVERT v583(0x0), v583(0x0)

    Begin block 0x587
    prev=[0x57b], succ=[0xc2c]
    =================================
    0x589: v589(0x1681) = CONST 
    0x58c: v58c(0xc2c) = CONST 
    0x58f: JUMP v58c(0xc2c)

    Begin block 0xc2c
    prev=[0x587], succ=[0x1681]
    =================================
    0xc2d: vc2d(0xa) = CONST 
    0xc2f: vc2f = SLOAD vc2d(0xa)
    0xc30: vc30(0xff) = CONST 
    0xc32: vc32 = AND vc30(0xff), vc2f
    0xc34: JUMP v589(0x1681)

    Begin block 0x1681
    prev=[0xc2c], succ=[]
    =================================
    0x1682: v1682(0x40) = CONST 
    0x1685: v1685 = MLOAD v1682(0x40)
    0x1687: v1687 = ISZERO vc32
    0x1688: v1688 = ISZERO v1687
    0x168a: MSTORE v1685, v1688
    0x168b: v168b = MLOAD v1682(0x40)
    0x168f: v168f(0x0) = SUB v1685, v168b
    0x1690: v1690(0x20) = CONST 
    0x1692: v1692(0x20) = ADD v1690(0x20), v168f(0x0)
    0x1694: RETURN v168b, v1692(0x20)

}

function getCurrentVotes(address)() public {
    Begin block 0x590
    prev=[], succ=[0x598, 0x59c]
    =================================
    0x591: v591 = CALLVALUE 
    0x593: v593 = ISZERO v591
    0x594: v594(0x59c) = CONST 
    0x597: JUMPI v594(0x59c), v593

    Begin block 0x598
    prev=[0x590], succ=[]
    =================================
    0x598: v598(0x0) = CONST 
    0x59b: REVERT v598(0x0), v598(0x0)

    Begin block 0x59c
    prev=[0x590], succ=[0x5af, 0x5b30x590]
    =================================
    0x59e: v59e(0x16b4) = CONST 
    0x5a1: v5a1(0x4) = CONST 
    0x5a4: v5a4 = CALLDATASIZE 
    0x5a5: v5a5 = SUB v5a4, v5a1(0x4)
    0x5a6: v5a6(0x20) = CONST 
    0x5a9: v5a9 = LT v5a5, v5a6(0x20)
    0x5aa: v5aa = ISZERO v5a9
    0x5ab: v5ab(0x5b3) = CONST 
    0x5ae: JUMPI v5ab(0x5b3), v5aa

    Begin block 0x5af
    prev=[0x59c], succ=[]
    =================================
    0x5af: v5af(0x0) = CONST 
    0x5b2: REVERT v5af(0x0), v5af(0x0)

    Begin block 0x5b30x590
    prev=[0x59c], succ=[0xc350x590]
    =================================
    0x5b50x590: v5905b5 = CALLDATALOAD v5a1(0x4)
    0x5b60x590: v5905b6(0x1) = CONST 
    0x5b80x590: v5905b8(0x1) = CONST 
    0x5ba0x590: v5905ba(0xa0) = CONST 
    0x5bc0x590: v5905bc(0x10000000000000000000000000000000000000000) = SHL v5905ba(0xa0), v5905b8(0x1)
    0x5bd0x590: v5905bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5905bc(0x10000000000000000000000000000000000000000), v5905b6(0x1)
    0x5be0x590: v5905be = AND v5905bd(0xffffffffffffffffffffffffffffffffffffffff), v5905b5
    0x5bf0x590: v5905bf(0xc35) = CONST 
    0x5c20x590: JUMP v5905bf(0xc35)

    Begin block 0xc350x590
    prev=[0x5b30x590], succ=[0x120f0x590]
    =================================
    0xc360x590: v590c36(0x0) = CONST 
    0xc380x590: v590c38(0xc3f) = CONST 
    0xc3b0x590: v590c3b(0x120f) = CONST 
    0xc3e0x590: JUMP v590c3b(0x120f)

    Begin block 0x120f0x590
    prev=[0xc350x590], succ=[0x12910x590]
    =================================
    0x12100x590: v5901210(0x60) = CONST 
    0x12120x590: v5901212(0x0) = CONST 
    0x12140x590: v5901214 = ADDRESS 
    0x12150x590: v5901215(0x1) = CONST 
    0x12170x590: v5901217(0x1) = CONST 
    0x12190x590: v5901219(0xa0) = CONST 
    0x121b0x590: v590121b(0x10000000000000000000000000000000000000000) = SHL v5901219(0xa0), v5901217(0x1)
    0x121c0x590: v590121c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v590121b(0x10000000000000000000000000000000000000000), v5901215(0x1)
    0x121d0x590: v590121d = AND v590121c(0xffffffffffffffffffffffffffffffffffffffff), v5901214
    0x121e0x590: v590121e(0x0) = CONST 
    0x12200x590: v5901220 = CALLDATASIZE 
    0x12210x590: v5901221(0x40) = CONST 
    0x12230x590: v5901223 = MLOAD v5901221(0x40)
    0x12240x590: v5901224(0x24) = CONST 
    0x12260x590: v5901226 = ADD v5901224(0x24), v5901223
    0x12290x590: v5901229(0x20) = CONST 
    0x122b0x590: v590122b = ADD v5901229(0x20), v5901226
    0x122e0x590: v590122e(0x20) = SUB v590122b, v5901226
    0x12300x590: MSTORE v5901226, v590122e(0x20)
    0x12360x590: MSTORE v590122b, v5901220
    0x12370x590: v5901237(0x20) = CONST 
    0x12390x590: v5901239 = ADD v5901237(0x20), v590122b
    0x123f0x590: CALLDATACOPY v5901239, v590121e(0x0), v5901220
    0x12400x590: v5901240(0x0) = CONST 
    0x12440x590: v5901244 = ADD v5901220, v5901239
    0x12450x590: MSTORE v5901244, v5901240(0x0)
    0x12460x590: v5901246(0x40) = CONST 
    0x12490x590: v5901249 = MLOAD v5901246(0x40)
    0x124a0x590: v590124a(0x1f) = CONST 
    0x124e0x590: v590124e = ADD v5901220, v590124a(0x1f)
    0x124f0x590: v590124f(0x1f) = CONST 
    0x12510x590: v5901251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v590124f(0x1f)
    0x12540x590: v5901254 = AND v5901251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v590124e
    0x12570x590: v5901257 = ADD v5901239, v5901254
    0x125a0x590: v590125a = SUB v5901257, v5901249
    0x125d0x590: v590125d = ADD v5901251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v590125a
    0x125f0x590: MSTORE v5901249, v590125d
    0x12620x590: MSTORE v5901246(0x40), v5901257
    0x12630x590: v5901263(0x20) = CONST 
    0x12660x590: v5901266 = ADD v5901249, v5901263(0x20)
    0x12680x590: v5901268 = MLOAD v5901266
    0x12690x590: v5901269(0x1) = CONST 
    0x126b0x590: v590126b(0x1) = CONST 
    0x126d0x590: v590126d(0xe0) = CONST 
    0x126f0x590: v590126f(0x100000000000000000000000000000000000000000000000000000000) = SHL v590126d(0xe0), v590126b(0x1)
    0x12700x590: v5901270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v590126f(0x100000000000000000000000000000000000000000000000000000000), v5901269(0x1)
    0x12710x590: v5901271 = AND v5901270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v5901268
    0x12720x590: v5901272(0x933c1ed) = CONST 
    0x12770x590: v5901277(0xe0) = CONST 
    0x12790x590: v5901279(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v5901277(0xe0), v5901272(0x933c1ed)
    0x127a0x590: v590127a = OR v5901279(0x933c1ed00000000000000000000000000000000000000000000000000000000), v5901271
    0x127c0x590: MSTORE v5901266, v590127a
    0x127e0x590: v590127e = MLOAD v5901246(0x40)
    0x12800x590: v5901280 = MLOAD v5901249

    Begin block 0x12910x590
    prev=[0x129a0x590, 0x120f0x590], succ=[0x12b00x590, 0x129a0x590]
    =================================
    0x12910x590_0x2: v1291590_2 = PHI v59012a3, v5901280
    0x12920x590: v5901292(0x20) = CONST 
    0x12950x590: v5901295 = LT v1291590_2, v5901292(0x20)
    0x12960x590: v5901296(0x12b0) = CONST 
    0x12990x590: JUMPI v5901296(0x12b0), v5901295

    Begin block 0x12b00x590
    prev=[0x12910x590], succ=[0x12ef0x590, 0x13100x590]
    =================================
    0x12b00x590_0x0: v12b0590_0 = PHI v59012ab, v5901266
    0x12b00x590_0x1: v12b0590_1 = PHI v59012a9, v590127e
    0x12b00x590_0x2: v12b0590_2 = PHI v59012a3, v5901280
    0x12b10x590: v59012b1(0x1) = CONST 
    0x12b40x590: v59012b4(0x20) = CONST 
    0x12b60x590: v59012b6 = SUB v59012b4(0x20), v12b0590_2
    0x12b70x590: v59012b7(0x100) = CONST 
    0x12ba0x590: v59012ba = EXP v59012b7(0x100), v59012b6
    0x12bb0x590: v59012bb = SUB v59012ba, v59012b1(0x1)
    0x12bd0x590: v59012bd = NOT v59012bb
    0x12bf0x590: v59012bf = MLOAD v12b0590_0
    0x12c00x590: v59012c0 = AND v59012bf, v59012bd
    0x12c30x590: v59012c3 = MLOAD v12b0590_1
    0x12c40x590: v59012c4 = AND v59012c3, v59012bb
    0x12c70x590: v59012c7 = OR v59012c0, v59012c4
    0x12c90x590: MSTORE v12b0590_1, v59012c7
    0x12d20x590: v59012d2 = ADD v5901280, v590127e
    0x12d60x590: v59012d6(0x0) = CONST 
    0x12d80x590: v59012d8(0x40) = CONST 
    0x12da0x590: v59012da = MLOAD v59012d8(0x40)
    0x12dd0x590: v59012dd = SUB v59012d2, v59012da
    0x12e00x590: v59012e0 = GAS 
    0x12e10x590: v59012e1 = STATICCALL v59012e0, v590121d, v59012da, v59012dd, v59012da, v59012d6(0x0)
    0x12e50x590: v59012e5 = RETURNDATASIZE 
    0x12e70x590: v59012e7(0x0) = CONST 
    0x12ea0x590: v59012ea = EQ v59012e5, v59012e7(0x0)
    0x12eb0x590: v59012eb(0x1310) = CONST 
    0x12ee0x590: JUMPI v59012eb(0x1310), v59012ea

    Begin block 0x12ef0x590
    prev=[0x12b00x590], succ=[0x13150x590]
    =================================
    0x12ef0x590: v59012ef(0x40) = CONST 
    0x12f10x590: v59012f1 = MLOAD v59012ef(0x40)
    0x12f40x590: v59012f4(0x1f) = CONST 
    0x12f60x590: v59012f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v59012f4(0x1f)
    0x12f70x590: v59012f7(0x3f) = CONST 
    0x12f90x590: v59012f9 = RETURNDATASIZE 
    0x12fa0x590: v59012fa = ADD v59012f9, v59012f7(0x3f)
    0x12fb0x590: v59012fb = AND v59012fa, v59012f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12fd0x590: v59012fd = ADD v59012f1, v59012fb
    0x12fe0x590: v59012fe(0x40) = CONST 
    0x13000x590: MSTORE v59012fe(0x40), v59012fd
    0x13010x590: v5901301 = RETURNDATASIZE 
    0x13030x590: MSTORE v59012f1, v5901301
    0x13040x590: v5901304 = RETURNDATASIZE 
    0x13050x590: v5901305(0x0) = CONST 
    0x13070x590: v5901307(0x20) = CONST 
    0x130a0x590: v590130a = ADD v59012f1, v5901307(0x20)
    0x130b0x590: RETURNDATACOPY v590130a, v5901305(0x0), v5901304
    0x130c0x590: v590130c(0x1315) = CONST 
    0x130f0x590: JUMP v590130c(0x1315)

    Begin block 0x13150x590
    prev=[0x12ef0x590, 0x13100x590], succ=[0x13290x590, 0x14790x590]
    =================================
    0x131a0x590: v590131a(0x40) = CONST 
    0x131c0x590: v590131c = MLOAD v590131a(0x40)
    0x131d0x590: v590131d = RETURNDATASIZE 
    0x131e0x590: v590131e(0x0) = CONST 
    0x13210x590: RETURNDATACOPY v590131c, v590131e(0x0), v590131d
    0x13240x590: v5901324 = ISZERO v59012e1
    0x13250x590: v5901325(0x1479) = CONST 
    0x13280x590: JUMPI v5901325(0x1479), v5901324

    Begin block 0x13290x590
    prev=[0x13150x590], succ=[]
    =================================
    0x13290x590: v5901329 = RETURNDATASIZE 
    0x132a0x590: v590132a(0x40) = CONST 
    0x132d0x590: v590132d = ADD v590131c, v590132a(0x40)
    0x132e0x590: RETURN v590132d, v5901329

    Begin block 0x14790x590
    prev=[0x13150x590], succ=[]
    =================================
    0x147a0x590: v590147a = RETURNDATASIZE 
    0x147c0x590: REVERT v590131c, v590147a

    Begin block 0x13100x590
    prev=[0x12b00x590], succ=[0x13150x590]
    =================================
    0x13110x590: v5901311(0x60) = CONST 

    Begin block 0x129a0x590
    prev=[0x12910x590], succ=[0x12910x590]
    =================================
    0x129a0x590_0x0: v129a590_0 = PHI v59012ab, v5901266
    0x129a0x590_0x1: v129a590_1 = PHI v59012a9, v590127e
    0x129a0x590_0x2: v129a590_2 = PHI v59012a3, v5901280
    0x129b0x590: v590129b = MLOAD v129a590_0
    0x129d0x590: MSTORE v129a590_1, v590129b
    0x129e0x590: v590129e(0x1f) = CONST 
    0x12a00x590: v59012a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v590129e(0x1f)
    0x12a30x590: v59012a3 = ADD v129a590_2, v59012a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a50x590: v59012a5(0x20) = CONST 
    0x12a90x590: v59012a9 = ADD v59012a5(0x20), v129a590_1
    0x12ab0x590: v59012ab = ADD v59012a5(0x20), v129a590_0
    0x12ac0x590: v59012ac(0x1291) = CONST 
    0x12af0x590: JUMP v59012ac(0x1291)

}

function delegateToViewImplementation(bytes)() public {
    Begin block 0x5c3
    prev=[], succ=[0x5cb, 0x5cf]
    =================================
    0x5c4: v5c4 = CALLVALUE 
    0x5c6: v5c6 = ISZERO v5c4
    0x5c7: v5c7(0x5cf) = CONST 
    0x5ca: JUMPI v5c7(0x5cf), v5c6

    Begin block 0x5cb
    prev=[0x5c3], succ=[]
    =================================
    0x5cb: v5cb(0x0) = CONST 
    0x5ce: REVERT v5cb(0x0), v5cb(0x0)

    Begin block 0x5cf
    prev=[0x5c3], succ=[0x5e2, 0x5e6]
    =================================
    0x5d1: v5d1(0x2c4) = CONST 
    0x5d4: v5d4(0x4) = CONST 
    0x5d7: v5d7 = CALLDATASIZE 
    0x5d8: v5d8 = SUB v5d7, v5d4(0x4)
    0x5d9: v5d9(0x20) = CONST 
    0x5dc: v5dc = LT v5d8, v5d9(0x20)
    0x5dd: v5dd = ISZERO v5dc
    0x5de: v5de(0x5e6) = CONST 
    0x5e1: JUMPI v5de(0x5e6), v5dd

    Begin block 0x5e2
    prev=[0x5cf], succ=[]
    =================================
    0x5e2: v5e2(0x0) = CONST 
    0x5e5: REVERT v5e2(0x0), v5e2(0x0)

    Begin block 0x5e6
    prev=[0x5cf], succ=[0x5fc, 0x600]
    =================================
    0x5e8: v5e8 = ADD v5d4(0x4), v5d8
    0x5ea: v5ea(0x20) = CONST 
    0x5ed: v5ed(0x24) = ADD v5d4(0x4), v5ea(0x20)
    0x5ef: v5ef = CALLDATALOAD v5d4(0x4)
    0x5f0: v5f0(0x1) = CONST 
    0x5f2: v5f2(0x20) = CONST 
    0x5f4: v5f4(0x100000000) = SHL v5f2(0x20), v5f0(0x1)
    0x5f6: v5f6 = GT v5ef, v5f4(0x100000000)
    0x5f7: v5f7 = ISZERO v5f6
    0x5f8: v5f8(0x600) = CONST 
    0x5fb: JUMPI v5f8(0x600), v5f7

    Begin block 0x5fc
    prev=[0x5e6], succ=[]
    =================================
    0x5fc: v5fc(0x0) = CONST 
    0x5ff: REVERT v5fc(0x0), v5fc(0x0)

    Begin block 0x600
    prev=[0x5e6], succ=[0x60e, 0x612]
    =================================
    0x602: v602 = ADD v5d4(0x4), v5ef
    0x604: v604(0x20) = CONST 
    0x607: v607 = ADD v602, v604(0x20)
    0x608: v608 = GT v607, v5e8
    0x609: v609 = ISZERO v608
    0x60a: v60a(0x612) = CONST 
    0x60d: JUMPI v60a(0x612), v609

    Begin block 0x60e
    prev=[0x600], succ=[]
    =================================
    0x60e: v60e(0x0) = CONST 
    0x611: REVERT v60e(0x0), v60e(0x0)

    Begin block 0x612
    prev=[0x600], succ=[0x62f, 0x633]
    =================================
    0x614: v614 = CALLDATALOAD v602
    0x616: v616(0x20) = CONST 
    0x618: v618 = ADD v616(0x20), v602
    0x61b: v61b(0x1) = CONST 
    0x61e: v61e = MUL v614, v61b(0x1)
    0x620: v620 = ADD v618, v61e
    0x621: v621 = GT v620, v5e8
    0x622: v622(0x1) = CONST 
    0x624: v624(0x20) = CONST 
    0x626: v626(0x100000000) = SHL v624(0x20), v622(0x1)
    0x628: v628 = GT v614, v626(0x100000000)
    0x629: v629 = OR v628, v621
    0x62a: v62a = ISZERO v629
    0x62b: v62b(0x633) = CONST 
    0x62e: JUMPI v62b(0x633), v62a

    Begin block 0x62f
    prev=[0x612], succ=[]
    =================================
    0x62f: v62f(0x0) = CONST 
    0x632: REVERT v62f(0x0), v62f(0x0)

    Begin block 0x633
    prev=[0x612], succ=[0xc45]
    =================================
    0x638: v638(0x1f) = CONST 
    0x63a: v63a = ADD v638(0x1f), v614
    0x63b: v63b(0x20) = CONST 
    0x63f: v63f = DIV v63a, v63b(0x20)
    0x640: v640 = MUL v63f, v63b(0x20)
    0x641: v641(0x20) = CONST 
    0x643: v643 = ADD v641(0x20), v640
    0x644: v644(0x40) = CONST 
    0x646: v646 = MLOAD v644(0x40)
    0x649: v649 = ADD v646, v643
    0x64a: v64a(0x40) = CONST 
    0x64c: MSTORE v64a(0x40), v649
    0x654: MSTORE v646, v614
    0x655: v655(0x20) = CONST 
    0x657: v657 = ADD v655(0x20), v646
    0x65d: CALLDATACOPY v657, v618, v614
    0x65e: v65e(0x0) = CONST 
    0x661: v661 = ADD v657, v614
    0x665: MSTORE v661, v65e(0x0)
    0x66a: v66a(0xc45) = CONST 
    0x673: JUMP v66a(0xc45)

    Begin block 0xc45
    prev=[0x633], succ=[0xc7e]
    =================================
    0xc46: vc46(0x60) = CONST 
    0xc48: vc48(0x0) = CONST 
    0xc4a: vc4a(0x60) = CONST 
    0xc4c: vc4c = ADDRESS 
    0xc4d: vc4d(0x1) = CONST 
    0xc4f: vc4f(0x1) = CONST 
    0xc51: vc51(0xa0) = CONST 
    0xc53: vc53(0x10000000000000000000000000000000000000000) = SHL vc51(0xa0), vc4f(0x1)
    0xc54: vc54(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc53(0x10000000000000000000000000000000000000000), vc4d(0x1)
    0xc55: vc55 = AND vc54(0xffffffffffffffffffffffffffffffffffffffff), vc4c
    0xc57: vc57(0x40) = CONST 
    0xc59: vc59 = MLOAD vc57(0x40)
    0xc5a: vc5a(0x24) = CONST 
    0xc5c: vc5c = ADD vc5a(0x24), vc59
    0xc5f: vc5f(0x20) = CONST 
    0xc61: vc61 = ADD vc5f(0x20), vc5c
    0xc64: vc64(0x20) = SUB vc61, vc5c
    0xc66: MSTORE vc5c, vc64(0x20)
    0xc6a: vc6a = MLOAD v646
    0xc6c: MSTORE vc61, vc6a
    0xc6d: vc6d(0x20) = CONST 
    0xc6f: vc6f = ADD vc6d(0x20), vc61
    0xc73: vc73 = MLOAD v646
    0xc75: vc75(0x20) = CONST 
    0xc77: vc77 = ADD vc75(0x20), v646
    0xc7c: vc7c(0x0) = CONST 

    Begin block 0xc7e
    prev=[0xc45, 0xc87], succ=[0xc96, 0xc87]
    =================================
    0xc7e_0x0: vc7e_0 = PHI vc7c(0x0), vc91
    0xc81: vc81 = LT vc7e_0, vc73
    0xc82: vc82 = ISZERO vc81
    0xc83: vc83(0xc96) = CONST 
    0xc86: JUMPI vc83(0xc96), vc82

    Begin block 0xc96
    prev=[0xc7e], succ=[0xcc3, 0xcaa]
    =================================
    0xc9f: vc9f = ADD vc73, vc6f
    0xca1: vca1(0x1f) = CONST 
    0xca3: vca3 = AND vca1(0x1f), vc73
    0xca5: vca5 = ISZERO vca3
    0xca6: vca6(0xcc3) = CONST 
    0xca9: JUMPI vca6(0xcc3), vca5

    Begin block 0xcc3
    prev=[0xc96, 0xcaa], succ=[0xcff]
    =================================
    0xcc3_0x1: vcc3_1 = PHI vc9f, vcc0
    0xcc5: vcc5(0x40) = CONST 
    0xcc8: vcc8 = MLOAD vcc5(0x40)
    0xcc9: vcc9(0x1f) = CONST 
    0xccb: vccb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vcc9(0x1f)
    0xcce: vcce = SUB vcc3_1, vcc8
    0xccf: vccf = ADD vcce, vccb(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xcd1: MSTORE vcc8, vccf
    0xcd4: MSTORE vcc5(0x40), vcc3_1
    0xcd5: vcd5(0x20) = CONST 
    0xcd8: vcd8 = ADD vcc8, vcd5(0x20)
    0xcda: vcda = MLOAD vcd8
    0xcdb: vcdb(0x1) = CONST 
    0xcdd: vcdd(0x1) = CONST 
    0xcdf: vcdf(0xe0) = CONST 
    0xce1: vce1(0x100000000000000000000000000000000000000000000000000000000) = SHL vcdf(0xe0), vcdd(0x1)
    0xce2: vce2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vce1(0x100000000000000000000000000000000000000000000000000000000), vcdb(0x1)
    0xce3: vce3 = AND vce2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vcda
    0xce4: vce4(0x933c1ed) = CONST 
    0xce9: vce9(0xe0) = CONST 
    0xceb: vceb(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL vce9(0xe0), vce4(0x933c1ed)
    0xcec: vcec = OR vceb(0x933c1ed00000000000000000000000000000000000000000000000000000000), vce3
    0xcee: MSTORE vcd8, vcec
    0xcf0: vcf0 = MLOAD vcc5(0x40)
    0xcf2: vcf2 = MLOAD vcc8

    Begin block 0xcff
    prev=[0xcc3, 0xd08], succ=[0xd1e, 0xd08]
    =================================
    0xcff_0x2: vcff_2 = PHI vcf2, vd11
    0xd00: vd00(0x20) = CONST 
    0xd03: vd03 = LT vcff_2, vd00(0x20)
    0xd04: vd04(0xd1e) = CONST 
    0xd07: JUMPI vd04(0xd1e), vd03

    Begin block 0xd1e
    prev=[0xcff], succ=[0xd5d, 0xd7e]
    =================================
    0xd1e_0x0: vd1e_0 = PHI vcd8, vd19
    0xd1e_0x1: vd1e_1 = PHI vcf0, vd17
    0xd1e_0x2: vd1e_2 = PHI vcf2, vd11
    0xd1f: vd1f(0x1) = CONST 
    0xd22: vd22(0x20) = CONST 
    0xd24: vd24 = SUB vd22(0x20), vd1e_2
    0xd25: vd25(0x100) = CONST 
    0xd28: vd28 = EXP vd25(0x100), vd24
    0xd29: vd29 = SUB vd28, vd1f(0x1)
    0xd2b: vd2b = NOT vd29
    0xd2d: vd2d = MLOAD vd1e_0
    0xd2e: vd2e = AND vd2d, vd2b
    0xd31: vd31 = MLOAD vd1e_1
    0xd32: vd32 = AND vd31, vd29
    0xd35: vd35 = OR vd2e, vd32
    0xd37: MSTORE vd1e_1, vd35
    0xd40: vd40 = ADD vcf2, vcf0
    0xd44: vd44(0x0) = CONST 
    0xd46: vd46(0x40) = CONST 
    0xd48: vd48 = MLOAD vd46(0x40)
    0xd4b: vd4b = SUB vd40, vd48
    0xd4e: vd4e = GAS 
    0xd4f: vd4f = STATICCALL vd4e, vc55, vd48, vd4b, vd48, vd44(0x0)
    0xd53: vd53 = RETURNDATASIZE 
    0xd55: vd55(0x0) = CONST 
    0xd58: vd58 = EQ vd53, vd55(0x0)
    0xd59: vd59(0xd7e) = CONST 
    0xd5c: JUMPI vd59(0xd7e), vd58

    Begin block 0xd5d
    prev=[0xd1e], succ=[0xd83]
    =================================
    0xd5d: vd5d(0x40) = CONST 
    0xd5f: vd5f = MLOAD vd5d(0x40)
    0xd62: vd62(0x1f) = CONST 
    0xd64: vd64(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vd62(0x1f)
    0xd65: vd65(0x3f) = CONST 
    0xd67: vd67 = RETURNDATASIZE 
    0xd68: vd68 = ADD vd67, vd65(0x3f)
    0xd69: vd69 = AND vd68, vd64(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xd6b: vd6b = ADD vd5f, vd69
    0xd6c: vd6c(0x40) = CONST 
    0xd6e: MSTORE vd6c(0x40), vd6b
    0xd6f: vd6f = RETURNDATASIZE 
    0xd71: MSTORE vd5f, vd6f
    0xd72: vd72 = RETURNDATASIZE 
    0xd73: vd73(0x0) = CONST 
    0xd75: vd75(0x20) = CONST 
    0xd78: vd78 = ADD vd5f, vd75(0x20)
    0xd79: RETURNDATACOPY vd78, vd73(0x0), vd72
    0xd7a: vd7a(0xd83) = CONST 
    0xd7d: JUMP vd7a(0xd83)

    Begin block 0xd83
    prev=[0xd5d, 0xd7e], succ=[0xd92, 0xd98]
    =================================
    0xd89: vd89(0x0) = CONST 
    0xd8c: vd8c = EQ vd4f, vd89(0x0)
    0xd8d: vd8d = ISZERO vd8c
    0xd8e: vd8e(0xd98) = CONST 
    0xd91: JUMPI vd8e(0xd98), vd8d

    Begin block 0xd92
    prev=[0xd83], succ=[]
    =================================
    0xd92: vd92 = RETURNDATASIZE 
    0xd92_0x0: vd92_0 = PHI vd5f, vd7f(0x60)
    0xd93: vd93(0x20) = CONST 
    0xd96: vd96 = ADD vd92_0, vd93(0x20)
    0xd97: REVERT vd96, vd92

    Begin block 0xd98
    prev=[0xd83], succ=[0xda9, 0xdad]
    =================================
    0xd98_0x0: vd98_0 = PHI vd5f, vd7f(0x60)
    0xd9b: vd9b(0x20) = CONST 
    0xd9d: vd9d = ADD vd9b(0x20), vd98_0
    0xd9f: vd9f = MLOAD vd98_0
    0xda0: vda0(0x20) = CONST 
    0xda3: vda3 = LT vd9f, vda0(0x20)
    0xda4: vda4 = ISZERO vda3
    0xda5: vda5(0xdad) = CONST 
    0xda8: JUMPI vda5(0xdad), vda4

    Begin block 0xda9
    prev=[0xd98], succ=[]
    =================================
    0xda9: vda9(0x0) = CONST 
    0xdac: REVERT vda9(0x0), vda9(0x0)

    Begin block 0xdad
    prev=[0xd98], succ=[0xdc8, 0xdcc]
    =================================
    0xdaf: vdaf = ADD vd9d, vd9f
    0xdb3: vdb3 = MLOAD vd9d
    0xdb4: vdb4(0x40) = CONST 
    0xdb6: vdb6 = MLOAD vdb4(0x40)
    0xdbc: vdbc(0x1) = CONST 
    0xdbe: vdbe(0x20) = CONST 
    0xdc0: vdc0(0x100000000) = SHL vdbe(0x20), vdbc(0x1)
    0xdc2: vdc2 = GT vdb3, vdc0(0x100000000)
    0xdc3: vdc3 = ISZERO vdc2
    0xdc4: vdc4(0xdcc) = CONST 
    0xdc7: JUMPI vdc4(0xdcc), vdc3

    Begin block 0xdc8
    prev=[0xdad], succ=[]
    =================================
    0xdc8: vdc8(0x0) = CONST 
    0xdcb: REVERT vdc8(0x0), vdc8(0x0)

    Begin block 0xdcc
    prev=[0xdad], succ=[0xddd, 0xde1]
    =================================
    0xdcf: vdcf = ADD vd9d, vdb3
    0xdd1: vdd1(0x20) = CONST 
    0xdd4: vdd4 = ADD vdcf, vdd1(0x20)
    0xdd7: vdd7 = GT vdd4, vdaf
    0xdd8: vdd8 = ISZERO vdd7
    0xdd9: vdd9(0xde1) = CONST 
    0xddc: JUMPI vdd9(0xde1), vdd8

    Begin block 0xddd
    prev=[0xdcc], succ=[]
    =================================
    0xddd: vddd(0x0) = CONST 
    0xde0: REVERT vddd(0x0), vddd(0x0)

    Begin block 0xde1
    prev=[0xdcc], succ=[0xdf6, 0xdfa]
    =================================
    0xde3: vde3 = MLOAD vdcf
    0xde4: vde4(0x1) = CONST 
    0xde6: vde6(0x20) = CONST 
    0xde8: vde8(0x100000000) = SHL vde6(0x20), vde4(0x1)
    0xdea: vdea = GT vde3, vde8(0x100000000)
    0xded: vded = ADD vde3, vdd4
    0xdef: vdef = LT vdaf, vded
    0xdf0: vdf0 = OR vdef, vdea
    0xdf1: vdf1 = ISZERO vdf0
    0xdf2: vdf2(0xdfa) = CONST 
    0xdf5: JUMPI vdf2(0xdfa), vdf1

    Begin block 0xdf6
    prev=[0xde1], succ=[]
    =================================
    0xdf6: vdf6(0x0) = CONST 
    0xdf9: REVERT vdf6(0x0), vdf6(0x0)

    Begin block 0xdfa
    prev=[0xde1], succ=[0xe0f]
    =================================
    0xdfc: MSTORE vdb6, vde3
    0xdff: vdff = MLOAD vdcf
    0xe00: ve00(0x20) = CONST 
    0xe04: ve04 = ADD ve00(0x20), vdb6
    0xe08: ve08 = ADD ve00(0x20), vdcf
    0xe0d: ve0d(0x0) = CONST 

    Begin block 0xe0f
    prev=[0xdfa, 0xe18], succ=[0xe27, 0xe18]
    =================================
    0xe0f_0x0: ve0f_0 = PHI ve0d(0x0), ve22
    0xe12: ve12 = LT ve0f_0, vdff
    0xe13: ve13 = ISZERO ve12
    0xe14: ve14(0xe27) = CONST 
    0xe17: JUMPI ve14(0xe27), ve13

    Begin block 0xe27
    prev=[0xe0f], succ=[0xe54, 0xe3b]
    =================================
    0xe30: ve30 = ADD vdff, ve04
    0xe32: ve32(0x1f) = CONST 
    0xe34: ve34 = AND ve32(0x1f), vdff
    0xe36: ve36 = ISZERO ve34
    0xe37: ve37(0xe54) = CONST 
    0xe3a: JUMPI ve37(0xe54), ve36

    Begin block 0xe54
    prev=[0xe27, 0xe3b], succ=[0x2c40x5c3]
    =================================
    0xe54_0x1: ve54_1 = PHI ve30, ve51
    0xe56: ve56(0x40) = CONST 
    0xe58: MSTORE ve56(0x40), ve54_1
    0xe63: JUMP v5d1(0x2c4)

    Begin block 0x2c40x5c3
    prev=[0xe54], succ=[0x2e60x5c3]
    =================================
    0x2c50x5c3: v5c32c5(0x40) = CONST 
    0x2c80x5c3: v5c32c8 = MLOAD v5c32c5(0x40)
    0x2c90x5c3: v5c32c9(0x20) = CONST 
    0x2cd0x5c3: MSTORE v5c32c8, v5c32c9(0x20)
    0x2cf0x5c3: v5c32cf = MLOAD vdb6
    0x2d20x5c3: v5c32d2 = ADD v5c32c8, v5c32c9(0x20)
    0x2d30x5c3: MSTORE v5c32d2, v5c32cf
    0x2d50x5c3: v5c32d5 = MLOAD vdb6
    0x2dc0x5c3: v5c32dc = ADD v5c32c8, v5c32c5(0x40)
    0x2df0x5c3: v5c32df = ADD vdb6, v5c32c9(0x20)
    0x2e40x5c3: v5c32e4(0x0) = CONST 

    Begin block 0x2e60x5c3
    prev=[0x2ef0x5c3, 0x2c40x5c3], succ=[0x2fe0x5c3, 0x2ef0x5c3]
    =================================
    0x2e60x5c3_0x0: v2e65c3_0 = PHI v5c32f9, v5c32e4(0x0)
    0x2e90x5c3: v5c32e9 = LT v2e65c3_0, v5c32d5
    0x2ea0x5c3: v5c32ea = ISZERO v5c32e9
    0x2eb0x5c3: v5c32eb(0x2fe) = CONST 
    0x2ee0x5c3: JUMPI v5c32eb(0x2fe), v5c32ea

    Begin block 0x2fe0x5c3
    prev=[0x2e60x5c3], succ=[0x32b0x5c3, 0x3120x5c3]
    =================================
    0x3070x5c3: v5c3307 = ADD v5c32d5, v5c32dc
    0x3090x5c3: v5c3309(0x1f) = CONST 
    0x30b0x5c3: v5c330b = AND v5c3309(0x1f), v5c32d5
    0x30d0x5c3: v5c330d = ISZERO v5c330b
    0x30e0x5c3: v5c330e(0x32b) = CONST 
    0x3110x5c3: JUMPI v5c330e(0x32b), v5c330d

    Begin block 0x32b0x5c3
    prev=[0x2fe0x5c3, 0x3120x5c3], succ=[]
    =================================
    0x32b0x5c3_0x1: v32b5c3_1 = PHI v5c3328, v5c3307
    0x3310x5c3: v5c3331(0x40) = CONST 
    0x3330x5c3: v5c3333 = MLOAD v5c3331(0x40)
    0x3360x5c3: v5c3336 = SUB v32b5c3_1, v5c3333
    0x3380x5c3: RETURN v5c3333, v5c3336

    Begin block 0x3120x5c3
    prev=[0x2fe0x5c3], succ=[0x32b0x5c3]
    =================================
    0x3140x5c3: v5c3314 = SUB v5c3307, v5c330b
    0x3160x5c3: v5c3316 = MLOAD v5c3314
    0x3170x5c3: v5c3317(0x1) = CONST 
    0x31a0x5c3: v5c331a(0x20) = CONST 
    0x31c0x5c3: v5c331c = SUB v5c331a(0x20), v5c330b
    0x31d0x5c3: v5c331d(0x100) = CONST 
    0x3200x5c3: v5c3320 = EXP v5c331d(0x100), v5c331c
    0x3210x5c3: v5c3321 = SUB v5c3320, v5c3317(0x1)
    0x3220x5c3: v5c3322 = NOT v5c3321
    0x3230x5c3: v5c3323 = AND v5c3322, v5c3316
    0x3250x5c3: MSTORE v5c3314, v5c3323
    0x3260x5c3: v5c3326(0x20) = CONST 
    0x3280x5c3: v5c3328 = ADD v5c3326(0x20), v5c3314

    Begin block 0x2ef0x5c3
    prev=[0x2e60x5c3], succ=[0x2e60x5c3]
    =================================
    0x2ef0x5c3_0x0: v2ef5c3_0 = PHI v5c32f9, v5c32e4(0x0)
    0x2f10x5c3: v5c32f1 = ADD v2ef5c3_0, v5c32df
    0x2f20x5c3: v5c32f2 = MLOAD v5c32f1
    0x2f50x5c3: v5c32f5 = ADD v2ef5c3_0, v5c32dc
    0x2f60x5c3: MSTORE v5c32f5, v5c32f2
    0x2f70x5c3: v5c32f7(0x20) = CONST 
    0x2f90x5c3: v5c32f9 = ADD v5c32f7(0x20), v2ef5c3_0
    0x2fa0x5c3: v5c32fa(0x2e6) = CONST 
    0x2fd0x5c3: JUMP v5c32fa(0x2e6)

    Begin block 0xe3b
    prev=[0xe27], succ=[0xe54]
    =================================
    0xe3d: ve3d = SUB ve30, ve34
    0xe3f: ve3f = MLOAD ve3d
    0xe40: ve40(0x1) = CONST 
    0xe43: ve43(0x20) = CONST 
    0xe45: ve45 = SUB ve43(0x20), ve34
    0xe46: ve46(0x100) = CONST 
    0xe49: ve49 = EXP ve46(0x100), ve45
    0xe4a: ve4a = SUB ve49, ve40(0x1)
    0xe4b: ve4b = NOT ve4a
    0xe4c: ve4c = AND ve4b, ve3f
    0xe4e: MSTORE ve3d, ve4c
    0xe4f: ve4f(0x20) = CONST 
    0xe51: ve51 = ADD ve4f(0x20), ve3d

    Begin block 0xe18
    prev=[0xe0f], succ=[0xe0f]
    =================================
    0xe18_0x0: ve18_0 = PHI ve0d(0x0), ve22
    0xe1a: ve1a = ADD ve18_0, ve08
    0xe1b: ve1b = MLOAD ve1a
    0xe1e: ve1e = ADD ve18_0, ve04
    0xe1f: MSTORE ve1e, ve1b
    0xe20: ve20(0x20) = CONST 
    0xe22: ve22 = ADD ve20(0x20), ve18_0
    0xe23: ve23(0xe0f) = CONST 
    0xe26: JUMP ve23(0xe0f)

    Begin block 0xd7e
    prev=[0xd1e], succ=[0xd83]
    =================================
    0xd7f: vd7f(0x60) = CONST 

    Begin block 0xd08
    prev=[0xcff], succ=[0xcff]
    =================================
    0xd08_0x0: vd08_0 = PHI vcd8, vd19
    0xd08_0x1: vd08_1 = PHI vcf0, vd17
    0xd08_0x2: vd08_2 = PHI vcf2, vd11
    0xd09: vd09 = MLOAD vd08_0
    0xd0b: MSTORE vd08_1, vd09
    0xd0c: vd0c(0x1f) = CONST 
    0xd0e: vd0e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vd0c(0x1f)
    0xd11: vd11 = ADD vd08_2, vd0e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xd13: vd13(0x20) = CONST 
    0xd17: vd17 = ADD vd13(0x20), vd08_1
    0xd19: vd19 = ADD vd13(0x20), vd08_0
    0xd1a: vd1a(0xcff) = CONST 
    0xd1d: JUMP vd1a(0xcff)

    Begin block 0xcaa
    prev=[0xc96], succ=[0xcc3]
    =================================
    0xcac: vcac = SUB vc9f, vca3
    0xcae: vcae = MLOAD vcac
    0xcaf: vcaf(0x1) = CONST 
    0xcb2: vcb2(0x20) = CONST 
    0xcb4: vcb4 = SUB vcb2(0x20), vca3
    0xcb5: vcb5(0x100) = CONST 
    0xcb8: vcb8 = EXP vcb5(0x100), vcb4
    0xcb9: vcb9 = SUB vcb8, vcaf(0x1)
    0xcba: vcba = NOT vcb9
    0xcbb: vcbb = AND vcba, vcae
    0xcbd: MSTORE vcac, vcbb
    0xcbe: vcbe(0x20) = CONST 
    0xcc0: vcc0 = ADD vcbe(0x20), vcac

    Begin block 0xc87
    prev=[0xc7e], succ=[0xc7e]
    =================================
    0xc87_0x0: vc87_0 = PHI vc7c(0x0), vc91
    0xc89: vc89 = ADD vc87_0, vc77
    0xc8a: vc8a = MLOAD vc89
    0xc8d: vc8d = ADD vc87_0, vc6f
    0xc8e: MSTORE vc8d, vc8a
    0xc8f: vc8f(0x20) = CONST 
    0xc91: vc91 = ADD vc8f(0x20), vc87_0
    0xc92: vc92(0xc7e) = CONST 
    0xc95: JUMP vc92(0xc7e)

}

function _acceptGov()() public {
    Begin block 0x674
    prev=[], succ=[0x67c, 0x680]
    =================================
    0x675: v675 = CALLVALUE 
    0x677: v677 = ISZERO v675
    0x678: v678(0x680) = CONST 
    0x67b: JUMPI v678(0x680), v677

    Begin block 0x67c
    prev=[0x674], succ=[]
    =================================
    0x67c: v67c(0x0) = CONST 
    0x67f: REVERT v67c(0x0), v67c(0x0)

    Begin block 0x680
    prev=[0x674], succ=[0xe64]
    =================================
    0x682: v682(0x16e5) = CONST 
    0x685: v685(0xe64) = CONST 
    0x688: JUMP v685(0xe64)

    Begin block 0xe64
    prev=[0x680], succ=[0xa440x674]
    =================================
    0xe65: ve65(0xe6c) = CONST 
    0xe68: ve68(0xa44) = CONST 
    0xe6b: JUMP ve68(0xa44)

    Begin block 0xa440x674
    prev=[0xe64], succ=[0xa8b0x674, 0xaac0x674]
    =================================
    0xa450x674: v674a45(0x13) = CONST 
    0xa470x674: v674a47 = SLOAD v674a45(0x13)
    0xa480x674: v674a48(0x40) = CONST 
    0xa4a0x674: v674a4a = MLOAD v674a48(0x40)
    0xa4b0x674: v674a4b(0x60) = CONST 
    0xa4e0x674: v674a4e(0x0) = CONST 
    0xa510x674: v674a51(0x1) = CONST 
    0xa530x674: v674a53(0x1) = CONST 
    0xa550x674: v674a55(0xa0) = CONST 
    0xa570x674: v674a57(0x10000000000000000000000000000000000000000) = SHL v674a55(0xa0), v674a53(0x1)
    0xa580x674: v674a58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v674a57(0x10000000000000000000000000000000000000000), v674a51(0x1)
    0xa5b0x674: v674a5b = AND v674a47, v674a58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x674: v674a5f = CALLDATASIZE 
    0xa670x674: CALLDATACOPY v674a4a, v674a4e(0x0), v674a5f
    0xa680x674: v674a68(0x40) = CONST 
    0xa6a0x674: v674a6a = MLOAD v674a68(0x40)
    0xa6c0x674: v674a6c = ADD v674a4a, v674a5f
    0xa6f0x674: v674a6f(0x0) = CONST 
    0xa790x674: v674a79 = SUB v674a6c, v674a6a
    0xa7c0x674: v674a7c = GAS 
    0xa7d0x674: v674a7d = DELEGATECALL v674a7c, v674a5b, v674a6a, v674a79, v674a6a, v674a6f(0x0)
    0xa810x674: v674a81 = RETURNDATASIZE 
    0xa830x674: v674a83(0x0) = CONST 
    0xa860x674: v674a86 = EQ v674a81, v674a83(0x0)
    0xa870x674: v674a87(0xaac) = CONST 
    0xa8a0x674: JUMPI v674a87(0xaac), v674a86

    Begin block 0xa8b0x674
    prev=[0xa440x674], succ=[0xab10x674]
    =================================
    0xa8b0x674: v674a8b(0x40) = CONST 
    0xa8d0x674: v674a8d = MLOAD v674a8b(0x40)
    0xa900x674: v674a90(0x1f) = CONST 
    0xa920x674: v674a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v674a90(0x1f)
    0xa930x674: v674a93(0x3f) = CONST 
    0xa950x674: v674a95 = RETURNDATASIZE 
    0xa960x674: v674a96 = ADD v674a95, v674a93(0x3f)
    0xa970x674: v674a97 = AND v674a96, v674a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x674: v674a99 = ADD v674a8d, v674a97
    0xa9a0x674: v674a9a(0x40) = CONST 
    0xa9c0x674: MSTORE v674a9a(0x40), v674a99
    0xa9d0x674: v674a9d = RETURNDATASIZE 
    0xa9f0x674: MSTORE v674a8d, v674a9d
    0xaa00x674: v674aa0 = RETURNDATASIZE 
    0xaa10x674: v674aa1(0x0) = CONST 
    0xaa30x674: v674aa3(0x20) = CONST 
    0xaa60x674: v674aa6 = ADD v674a8d, v674aa3(0x20)
    0xaa70x674: RETURNDATACOPY v674aa6, v674aa1(0x0), v674aa0
    0xaa80x674: v674aa8(0xab1) = CONST 
    0xaab0x674: JUMP v674aa8(0xab1)

    Begin block 0xab10x674
    prev=[0xa8b0x674, 0xaac0x674], succ=[0xac50x674, 0x14560x674]
    =================================
    0xab60x674: v674ab6(0x40) = CONST 
    0xab80x674: v674ab8 = MLOAD v674ab6(0x40)
    0xab90x674: v674ab9 = RETURNDATASIZE 
    0xaba0x674: v674aba(0x0) = CONST 
    0xabd0x674: RETURNDATACOPY v674ab8, v674aba(0x0), v674ab9
    0xac00x674: v674ac0 = ISZERO v674a7d
    0xac10x674: v674ac1(0x1456) = CONST 
    0xac40x674: JUMPI v674ac1(0x1456), v674ac0

    Begin block 0xac50x674
    prev=[0xab10x674], succ=[]
    =================================
    0xac50x674: v674ac5 = RETURNDATASIZE 
    0xac70x674: RETURN v674ab8, v674ac5

    Begin block 0x14560x674
    prev=[0xab10x674], succ=[]
    =================================
    0x14570x674: v6741457 = RETURNDATASIZE 
    0x14590x674: REVERT v674ab8, v6741457

    Begin block 0xaac0x674
    prev=[0xa440x674], succ=[0xab10x674]
    =================================
    0xaad0x674: v674aad(0x60) = CONST 

}

function _setImplementation(address,bool,bytes)() public {
    Begin block 0x68b
    prev=[], succ=[0x693, 0x697]
    =================================
    0x68c: v68c = CALLVALUE 
    0x68e: v68e = ISZERO v68c
    0x68f: v68f(0x697) = CONST 
    0x692: JUMPI v68f(0x697), v68e

    Begin block 0x693
    prev=[0x68b], succ=[]
    =================================
    0x693: v693(0x0) = CONST 
    0x696: REVERT v693(0x0), v693(0x0)

    Begin block 0x697
    prev=[0x68b], succ=[0x6aa, 0x6ae]
    =================================
    0x699: v699(0x1706) = CONST 
    0x69c: v69c(0x4) = CONST 
    0x69f: v69f = CALLDATASIZE 
    0x6a0: v6a0 = SUB v69f, v69c(0x4)
    0x6a1: v6a1(0x60) = CONST 
    0x6a4: v6a4 = LT v6a0, v6a1(0x60)
    0x6a5: v6a5 = ISZERO v6a4
    0x6a6: v6a6(0x6ae) = CONST 
    0x6a9: JUMPI v6a6(0x6ae), v6a5

    Begin block 0x6aa
    prev=[0x697], succ=[]
    =================================
    0x6aa: v6aa(0x0) = CONST 
    0x6ad: REVERT v6aa(0x0), v6aa(0x0)

    Begin block 0x6ae
    prev=[0x697], succ=[0x6db, 0x6df]
    =================================
    0x6af: v6af(0x1) = CONST 
    0x6b1: v6b1(0x1) = CONST 
    0x6b3: v6b3(0xa0) = CONST 
    0x6b5: v6b5(0x10000000000000000000000000000000000000000) = SHL v6b3(0xa0), v6b1(0x1)
    0x6b6: v6b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b5(0x10000000000000000000000000000000000000000), v6af(0x1)
    0x6b8: v6b8 = CALLDATALOAD v69c(0x4)
    0x6b9: v6b9 = AND v6b8, v6b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x6bb: v6bb(0x20) = CONST 
    0x6be: v6be(0x24) = ADD v69c(0x4), v6bb(0x20)
    0x6bf: v6bf = CALLDATALOAD v6be(0x24)
    0x6c0: v6c0 = ISZERO v6bf
    0x6c1: v6c1 = ISZERO v6c0
    0x6c4: v6c4 = ADD v69c(0x4), v6a0
    0x6c6: v6c6(0x60) = CONST 
    0x6c9: v6c9(0x64) = ADD v69c(0x4), v6c6(0x60)
    0x6ca: v6ca(0x40) = CONST 
    0x6cd: v6cd(0x44) = ADD v69c(0x4), v6ca(0x40)
    0x6ce: v6ce = CALLDATALOAD v6cd(0x44)
    0x6cf: v6cf(0x1) = CONST 
    0x6d1: v6d1(0x20) = CONST 
    0x6d3: v6d3(0x100000000) = SHL v6d1(0x20), v6cf(0x1)
    0x6d5: v6d5 = GT v6ce, v6d3(0x100000000)
    0x6d6: v6d6 = ISZERO v6d5
    0x6d7: v6d7(0x6df) = CONST 
    0x6da: JUMPI v6d7(0x6df), v6d6

    Begin block 0x6db
    prev=[0x6ae], succ=[]
    =================================
    0x6db: v6db(0x0) = CONST 
    0x6de: REVERT v6db(0x0), v6db(0x0)

    Begin block 0x6df
    prev=[0x6ae], succ=[0x6ed, 0x6f1]
    =================================
    0x6e1: v6e1 = ADD v69c(0x4), v6ce
    0x6e3: v6e3(0x20) = CONST 
    0x6e6: v6e6 = ADD v6e1, v6e3(0x20)
    0x6e7: v6e7 = GT v6e6, v6c4
    0x6e8: v6e8 = ISZERO v6e7
    0x6e9: v6e9(0x6f1) = CONST 
    0x6ec: JUMPI v6e9(0x6f1), v6e8

    Begin block 0x6ed
    prev=[0x6df], succ=[]
    =================================
    0x6ed: v6ed(0x0) = CONST 
    0x6f0: REVERT v6ed(0x0), v6ed(0x0)

    Begin block 0x6f1
    prev=[0x6df], succ=[0x70e, 0x712]
    =================================
    0x6f3: v6f3 = CALLDATALOAD v6e1
    0x6f5: v6f5(0x20) = CONST 
    0x6f7: v6f7 = ADD v6f5(0x20), v6e1
    0x6fa: v6fa(0x1) = CONST 
    0x6fd: v6fd = MUL v6f3, v6fa(0x1)
    0x6ff: v6ff = ADD v6f7, v6fd
    0x700: v700 = GT v6ff, v6c4
    0x701: v701(0x1) = CONST 
    0x703: v703(0x20) = CONST 
    0x705: v705(0x100000000) = SHL v703(0x20), v701(0x1)
    0x707: v707 = GT v6f3, v705(0x100000000)
    0x708: v708 = OR v707, v700
    0x709: v709 = ISZERO v708
    0x70a: v70a(0x712) = CONST 
    0x70d: JUMPI v70a(0x712), v709

    Begin block 0x70e
    prev=[0x6f1], succ=[]
    =================================
    0x70e: v70e(0x0) = CONST 
    0x711: REVERT v70e(0x0), v70e(0x0)

    Begin block 0x712
    prev=[0x6f1], succ=[0xe6f]
    =================================
    0x717: v717(0x1f) = CONST 
    0x719: v719 = ADD v717(0x1f), v6f3
    0x71a: v71a(0x20) = CONST 
    0x71e: v71e = DIV v719, v71a(0x20)
    0x71f: v71f = MUL v71e, v71a(0x20)
    0x720: v720(0x20) = CONST 
    0x722: v722 = ADD v720(0x20), v71f
    0x723: v723(0x40) = CONST 
    0x725: v725 = MLOAD v723(0x40)
    0x728: v728 = ADD v725, v722
    0x729: v729(0x40) = CONST 
    0x72b: MSTORE v729(0x40), v728
    0x733: MSTORE v725, v6f3
    0x734: v734(0x20) = CONST 
    0x736: v736 = ADD v734(0x20), v725
    0x73c: CALLDATACOPY v736, v6f7, v6f3
    0x73d: v73d(0x0) = CONST 
    0x740: v740 = ADD v736, v6f3
    0x744: MSTORE v740, v73d(0x0)
    0x749: v749(0xe6f) = CONST 
    0x752: JUMP v749(0xe6f)

    Begin block 0xe6f
    prev=[0x712], succ=[0xe87, 0xebd]
    =================================
    0xe70: ve70(0x3) = CONST 
    0xe72: ve72 = SLOAD ve70(0x3)
    0xe73: ve73(0x100) = CONST 
    0xe77: ve77 = DIV ve72, ve73(0x100)
    0xe78: ve78(0x1) = CONST 
    0xe7a: ve7a(0x1) = CONST 
    0xe7c: ve7c(0xa0) = CONST 
    0xe7e: ve7e(0x10000000000000000000000000000000000000000) = SHL ve7c(0xa0), ve7a(0x1)
    0xe7f: ve7f(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve7e(0x10000000000000000000000000000000000000000), ve78(0x1)
    0xe80: ve80 = AND ve7f(0xffffffffffffffffffffffffffffffffffffffff), ve77
    0xe81: ve81 = CALLER 
    0xe82: ve82 = EQ ve81, ve80
    0xe83: ve83(0xebd) = CONST 
    0xe86: JUMPI ve83(0xebd), ve82

    Begin block 0xe87
    prev=[0xe6f], succ=[]
    =================================
    0xe87: ve87(0x40) = CONST 
    0xe89: ve89 = MLOAD ve87(0x40)
    0xe8a: ve8a(0x461bcd) = CONST 
    0xe8e: ve8e(0xe5) = CONST 
    0xe90: ve90(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL ve8e(0xe5), ve8a(0x461bcd)
    0xe92: MSTORE ve89, ve90(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe93: ve93(0x4) = CONST 
    0xe95: ve95 = ADD ve93(0x4), ve89
    0xe98: ve98(0x20) = CONST 
    0xe9a: ve9a = ADD ve98(0x20), ve95
    0xe9d: ve9d(0x20) = SUB ve9a, ve95
    0xe9f: MSTORE ve95, ve9d(0x20)
    0xea0: vea0(0x34) = CONST 
    0xea3: MSTORE ve9a, vea0(0x34)
    0xea4: vea4(0x20) = CONST 
    0xea6: vea6 = ADD vea4(0x20), ve9a
    0xea8: vea8(0x1330) = CONST 
    0xeab: veab(0x34) = CONST 
    0xeae: CODECOPY vea6, vea8(0x1330), veab(0x34)
    0xeaf: veaf(0x40) = CONST 
    0xeb1: veb1 = ADD veaf(0x40), vea6
    0xeb5: veb5(0x40) = CONST 
    0xeb7: veb7 = MLOAD veb5(0x40)
    0xeba: veba(0x84) = SUB veb1, veb7
    0xebc: REVERT veb7, veba(0x84)

    Begin block 0xebd
    prev=[0xe6f], succ=[0xec4, 0xef7]
    =================================
    0xebf: vebf = ISZERO v6c1
    0xec0: vec0(0xef7) = CONST 
    0xec3: JUMPI vec0(0xef7), vebf

    Begin block 0xec4
    prev=[0xebd], succ=[0xb59B0xec4]
    =================================
    0xec4: vec4(0x40) = CONST 
    0xec7: vec7 = MLOAD vec4(0x40)
    0xec8: vec8(0x4) = CONST 
    0xecb: MSTORE vec7, vec8(0x4)
    0xecc: vecc(0x24) = CONST 
    0xecf: vecf = ADD vec7, vecc(0x24)
    0xed2: MSTORE vec4(0x40), vecf
    0xed3: ved3(0x20) = CONST 
    0xed6: ved6 = ADD vec7, ved3(0x20)
    0xed8: ved8 = MLOAD ved6
    0xed9: ved9(0x1) = CONST 
    0xedb: vedb(0x1) = CONST 
    0xedd: vedd(0xe0) = CONST 
    0xedf: vedf(0x100000000000000000000000000000000000000000000000000000000) = SHL vedd(0xe0), vedb(0x1)
    0xee0: vee0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vedf(0x100000000000000000000000000000000000000000000000000000000), ved9(0x1)
    0xee1: vee1 = AND vee0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), ved8
    0xee2: vee2(0x153ab505) = CONST 
    0xee7: vee7(0xe0) = CONST 
    0xee9: vee9(0x153ab50500000000000000000000000000000000000000000000000000000000) = SHL vee7(0xe0), vee2(0x153ab505)
    0xeea: veea = OR vee9(0x153ab50500000000000000000000000000000000000000000000000000000000), vee1
    0xeec: MSTORE ved6, veea
    0xeed: veed(0xef5) = CONST 
    0xef1: vef1(0xb59) = CONST 
    0xef4: JUMP vef1(0xb59)

    Begin block 0xb59B0xec4
    prev=[0xec4], succ=[0xb720xb59B0xec4]
    =================================
    0xb5aS0xec4: vb5aVec4(0x13) = CONST 
    0xb5cS0xec4: vb5cVec4 = SLOAD vb5aVec4(0x13)
    0xb5dS0xec4: vb5dVec4(0x60) = CONST 
    0xb60S0xec4: vb60Vec4(0xb72) = CONST 
    0xb64S0xec4: vb64Vec4(0x1) = CONST 
    0xb66S0xec4: vb66Vec4(0x1) = CONST 
    0xb68S0xec4: vb68Vec4(0xa0) = CONST 
    0xb6aS0xec4: vb6aVec4(0x10000000000000000000000000000000000000000) = SHL vb68Vec4(0xa0), vb66Vec4(0x1)
    0xb6bS0xec4: vb6bVec4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb6aVec4(0x10000000000000000000000000000000000000000), vb64Vec4(0x1)
    0xb6cS0xec4: vb6cVec4 = AND vb6bVec4(0xffffffffffffffffffffffffffffffffffffffff), vb5cVec4
    0xb6eS0xec4: vb6eVec4(0x114d) = CONST 
    0xb71S0xec4: vb71_0Vec4 = CALLPRIVATE vb6eVec4(0x114d), vec7, vb6cVec4, vb60Vec4(0xb72)

    Begin block 0xb720xb59B0xec4
    prev=[0xb59B0xec4], succ=[0xef5]
    =================================
    0xb770xb59S0xec4: JUMP veed(0xef5)

    Begin block 0xef5
    prev=[0xb720xb59B0xec4], succ=[0xef7]
    =================================

    Begin block 0xef7
    prev=[0xebd, 0xef5], succ=[0xf49]
    =================================
    0xef8: vef8(0x13) = CONST 
    0xefb: vefb = SLOAD vef8(0x13)
    0xefc: vefc(0x1) = CONST 
    0xefe: vefe(0x1) = CONST 
    0xf00: vf00(0xa0) = CONST 
    0xf02: vf02(0x10000000000000000000000000000000000000000) = SHL vf00(0xa0), vefe(0x1)
    0xf03: vf03(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf02(0x10000000000000000000000000000000000000000), vefc(0x1)
    0xf06: vf06 = AND vf03(0xffffffffffffffffffffffffffffffffffffffff), v6b9
    0xf07: vf07(0x1) = CONST 
    0xf09: vf09(0x1) = CONST 
    0xf0b: vf0b(0xa0) = CONST 
    0xf0d: vf0d(0x10000000000000000000000000000000000000000) = SHL vf0b(0xa0), vf09(0x1)
    0xf0e: vf0e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf0d(0x10000000000000000000000000000000000000000), vf07(0x1)
    0xf0f: vf0f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vf0e(0xffffffffffffffffffffffffffffffffffffffff)
    0xf11: vf11 = AND vefb, vf0f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0xf12: vf12 = OR vf11, vf06
    0xf15: SSTORE vef8(0x13), vf12
    0xf16: vf16(0x40) = CONST 
    0xf18: vf18 = MLOAD vf16(0x40)
    0xf19: vf19(0x20) = CONST 
    0xf1b: vf1b(0x24) = CONST 
    0xf1e: vf1e = ADD vf18, vf1b(0x24)
    0xf21: MSTORE vf1e, vf19(0x20)
    0xf23: vf23 = MLOAD v725
    0xf24: vf24(0x44) = CONST 
    0xf27: vf27 = ADD vf18, vf24(0x44)
    0xf28: MSTORE vf27, vf23
    0xf2a: vf2a = MLOAD v725
    0xf2e: vf2e = AND vefb, vf03(0xffffffffffffffffffffffffffffffffffffffff)
    0xf30: vf30(0xfc3) = CONST 
    0xf3a: vf3a(0x64) = CONST 
    0xf3e: vf3e = ADD vf18, vf3a(0x64)
    0xf42: vf42 = ADD v725, vf19(0x20)
    0xf47: vf47(0x0) = CONST 

    Begin block 0xf49
    prev=[0xef7, 0xf52], succ=[0xf61, 0xf52]
    =================================
    0xf49_0x0: vf49_0 = PHI vf47(0x0), vf5c
    0xf4c: vf4c = LT vf49_0, vf2a
    0xf4d: vf4d = ISZERO vf4c
    0xf4e: vf4e(0xf61) = CONST 
    0xf51: JUMPI vf4e(0xf61), vf4d

    Begin block 0xf61
    prev=[0xf49], succ=[0xf8e, 0xf75]
    =================================
    0xf6a: vf6a = ADD vf2a, vf3e
    0xf6c: vf6c(0x1f) = CONST 
    0xf6e: vf6e = AND vf6c(0x1f), vf2a
    0xf70: vf70 = ISZERO vf6e
    0xf71: vf71(0xf8e) = CONST 
    0xf74: JUMPI vf71(0xf8e), vf70

    Begin block 0xf8e
    prev=[0xf61, 0xf75], succ=[0xb590x68b]
    =================================
    0xf8e_0x1: vf8e_1 = PHI vf6a, vf8b
    0xf90: vf90(0x40) = CONST 
    0xf93: vf93 = MLOAD vf90(0x40)
    0xf94: vf94(0x1f) = CONST 
    0xf96: vf96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vf94(0x1f)
    0xf99: vf99 = SUB vf8e_1, vf93
    0xf9a: vf9a = ADD vf99, vf96(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xf9c: MSTORE vf93, vf9a
    0xf9f: MSTORE vf90(0x40), vf8e_1
    0xfa0: vfa0(0x20) = CONST 
    0xfa3: vfa3 = ADD vf93, vfa0(0x20)
    0xfa5: vfa5 = MLOAD vfa3
    0xfa6: vfa6(0x1) = CONST 
    0xfa8: vfa8(0x1) = CONST 
    0xfaa: vfaa(0xe0) = CONST 
    0xfac: vfac(0x100000000000000000000000000000000000000000000000000000000) = SHL vfaa(0xe0), vfa8(0x1)
    0xfad: vfad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vfac(0x100000000000000000000000000000000000000000000000000000000), vfa6(0x1)
    0xfae: vfae = AND vfad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vfa5
    0xfaf: vfaf(0xadccee5) = CONST 
    0xfb4: vfb4(0xe3) = CONST 
    0xfb6: vfb6(0x56e6772800000000000000000000000000000000000000000000000000000000) = SHL vfb4(0xe3), vfaf(0xadccee5)
    0xfb7: vfb7 = OR vfb6(0x56e6772800000000000000000000000000000000000000000000000000000000), vfae
    0xfb9: MSTORE vfa3, vfb7
    0xfbc: vfbc(0xb59) = CONST 
    0xfc2: JUMP vfbc(0xb59)

    Begin block 0xb590x68b
    prev=[0xf8e], succ=[0xb720x68b]
    =================================
    0xb5a0x68b: v68bb5a(0x13) = CONST 
    0xb5c0x68b: v68bb5c = SLOAD v68bb5a(0x13)
    0xb5d0x68b: v68bb5d(0x60) = CONST 
    0xb600x68b: v68bb60(0xb72) = CONST 
    0xb640x68b: v68bb64(0x1) = CONST 
    0xb660x68b: v68bb66(0x1) = CONST 
    0xb680x68b: v68bb68(0xa0) = CONST 
    0xb6a0x68b: v68bb6a(0x10000000000000000000000000000000000000000) = SHL v68bb68(0xa0), v68bb66(0x1)
    0xb6b0x68b: v68bb6b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v68bb6a(0x10000000000000000000000000000000000000000), v68bb64(0x1)
    0xb6c0x68b: v68bb6c = AND v68bb6b(0xffffffffffffffffffffffffffffffffffffffff), v68bb5c
    0xb6e0x68b: v68bb6e(0x114d) = CONST 
    0xb710x68b: v68bb71_0 = CALLPRIVATE v68bb6e(0x114d), vf93, v68bb6c, v68bb60(0xb72)

    Begin block 0xb720x68b
    prev=[0xb590x68b], succ=[0xfc3]
    =================================
    0xb770x68b: JUMP vf30(0xfc3)

    Begin block 0xfc3
    prev=[0xb720x68b], succ=[0x1706]
    =================================
    0xfc5: vfc5(0x13) = CONST 
    0xfc7: vfc7 = SLOAD vfc5(0x13)
    0xfc8: vfc8(0x40) = CONST 
    0xfcb: vfcb = MLOAD vfc8(0x40)
    0xfcc: vfcc(0x1) = CONST 
    0xfce: vfce(0x1) = CONST 
    0xfd0: vfd0(0xa0) = CONST 
    0xfd2: vfd2(0x10000000000000000000000000000000000000000) = SHL vfd0(0xa0), vfce(0x1)
    0xfd3: vfd3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfd2(0x10000000000000000000000000000000000000000), vfcc(0x1)
    0xfd6: vfd6 = AND vf2e, vfd3(0xffffffffffffffffffffffffffffffffffffffff)
    0xfd8: MSTORE vfcb, vfd6
    0xfdb: vfdb = AND vfc7, vfd3(0xffffffffffffffffffffffffffffffffffffffff)
    0xfdc: vfdc(0x20) = CONST 
    0xfdf: vfdf = ADD vfcb, vfdc(0x20)
    0xfe0: MSTORE vfdf, vfdb
    0xfe2: vfe2 = MLOAD vfc8(0x40)
    0xfe3: vfe3(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x1007: v1007(0x0) = SUB vfcb, vfe2
    0x100a: v100a(0x40) = ADD vfc8(0x40), v1007(0x0)
    0x100c: LOG1 vfe2, v100a(0x40), vfe3(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x1011: JUMP v699(0x1706)

    Begin block 0x1706
    prev=[0xfc3], succ=[]
    =================================
    0x1707: STOP 

    Begin block 0xf75
    prev=[0xf61], succ=[0xf8e]
    =================================
    0xf77: vf77 = SUB vf6a, vf6e
    0xf79: vf79 = MLOAD vf77
    0xf7a: vf7a(0x1) = CONST 
    0xf7d: vf7d(0x20) = CONST 
    0xf7f: vf7f = SUB vf7d(0x20), vf6e
    0xf80: vf80(0x100) = CONST 
    0xf83: vf83 = EXP vf80(0x100), vf7f
    0xf84: vf84 = SUB vf83, vf7a(0x1)
    0xf85: vf85 = NOT vf84
    0xf86: vf86 = AND vf85, vf79
    0xf88: MSTORE vf77, vf86
    0xf89: vf89(0x20) = CONST 
    0xf8b: vf8b = ADD vf89(0x20), vf77

    Begin block 0xf52
    prev=[0xf49], succ=[0xf49]
    =================================
    0xf52_0x0: vf52_0 = PHI vf47(0x0), vf5c
    0xf54: vf54 = ADD vf52_0, vf42
    0xf55: vf55 = MLOAD vf54
    0xf58: vf58 = ADD vf52_0, vf3e
    0xf59: MSTORE vf58, vf55
    0xf5a: vf5a(0x20) = CONST 
    0xf5c: vf5c = ADD vf5a(0x20), vf52_0
    0xf5d: vf5d(0xf49) = CONST 
    0xf60: JUMP vf5d(0xf49)

}

function lastScalingTime()() public {
    Begin block 0x753
    prev=[], succ=[0x75b, 0x75f]
    =================================
    0x754: v754 = CALLVALUE 
    0x756: v756 = ISZERO v754
    0x757: v757(0x75f) = CONST 
    0x75a: JUMPI v757(0x75f), v756

    Begin block 0x75b
    prev=[0x753], succ=[]
    =================================
    0x75b: v75b(0x0) = CONST 
    0x75e: REVERT v75b(0x0), v75b(0x0)

    Begin block 0x75f
    prev=[0x753], succ=[0x1012]
    =================================
    0x761: v761(0x1727) = CONST 
    0x764: v764(0x1012) = CONST 
    0x767: JUMP v764(0x1012)

    Begin block 0x1012
    prev=[0x75f], succ=[0x1727]
    =================================
    0x1013: v1013(0x9) = CONST 
    0x1015: v1015 = SLOAD v1013(0x9)
    0x1017: JUMP v761(0x1727)

    Begin block 0x1727
    prev=[0x1012], succ=[]
    =================================
    0x1728: v1728(0x40) = CONST 
    0x172b: v172b = MLOAD v1728(0x40)
    0x172e: MSTORE v172b, v1015
    0x172f: v172f = MLOAD v1728(0x40)
    0x1733: v1733(0x0) = SUB v172b, v172f
    0x1734: v1734(0x20) = CONST 
    0x1736: v1736(0x20) = ADD v1734(0x20), v1733(0x0)
    0x1738: RETURN v172f, v1736(0x20)

}

function delegates(address)() public {
    Begin block 0x768
    prev=[], succ=[0x770, 0x774]
    =================================
    0x769: v769 = CALLVALUE 
    0x76b: v76b = ISZERO v769
    0x76c: v76c(0x774) = CONST 
    0x76f: JUMPI v76c(0x774), v76b

    Begin block 0x770
    prev=[0x768], succ=[]
    =================================
    0x770: v770(0x0) = CONST 
    0x773: REVERT v770(0x0), v770(0x0)

    Begin block 0x774
    prev=[0x768], succ=[0x787, 0x5b30x768]
    =================================
    0x776: v776(0x1758) = CONST 
    0x779: v779(0x4) = CONST 
    0x77c: v77c = CALLDATASIZE 
    0x77d: v77d = SUB v77c, v779(0x4)
    0x77e: v77e(0x20) = CONST 
    0x781: v781 = LT v77d, v77e(0x20)
    0x782: v782 = ISZERO v781
    0x783: v783(0x5b3) = CONST 
    0x786: JUMPI v783(0x5b3), v782

    Begin block 0x787
    prev=[0x774], succ=[]
    =================================
    0x787: v787(0x0) = CONST 
    0x78a: REVERT v787(0x0), v787(0x0)

    Begin block 0x5b30x768
    prev=[0x774], succ=[0xc350x768]
    =================================
    0x5b50x768: v7685b5 = CALLDATALOAD v779(0x4)
    0x5b60x768: v7685b6(0x1) = CONST 
    0x5b80x768: v7685b8(0x1) = CONST 
    0x5ba0x768: v7685ba(0xa0) = CONST 
    0x5bc0x768: v7685bc(0x10000000000000000000000000000000000000000) = SHL v7685ba(0xa0), v7685b8(0x1)
    0x5bd0x768: v7685bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7685bc(0x10000000000000000000000000000000000000000), v7685b6(0x1)
    0x5be0x768: v7685be = AND v7685bd(0xffffffffffffffffffffffffffffffffffffffff), v7685b5
    0x5bf0x768: v7685bf(0xc35) = CONST 
    0x5c20x768: JUMP v7685bf(0xc35)

    Begin block 0xc350x768
    prev=[0x5b30x768], succ=[0x120f0x768]
    =================================
    0xc360x768: v768c36(0x0) = CONST 
    0xc380x768: v768c38(0xc3f) = CONST 
    0xc3b0x768: v768c3b(0x120f) = CONST 
    0xc3e0x768: JUMP v768c3b(0x120f)

    Begin block 0x120f0x768
    prev=[0xc350x768], succ=[0x12910x768]
    =================================
    0x12100x768: v7681210(0x60) = CONST 
    0x12120x768: v7681212(0x0) = CONST 
    0x12140x768: v7681214 = ADDRESS 
    0x12150x768: v7681215(0x1) = CONST 
    0x12170x768: v7681217(0x1) = CONST 
    0x12190x768: v7681219(0xa0) = CONST 
    0x121b0x768: v768121b(0x10000000000000000000000000000000000000000) = SHL v7681219(0xa0), v7681217(0x1)
    0x121c0x768: v768121c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v768121b(0x10000000000000000000000000000000000000000), v7681215(0x1)
    0x121d0x768: v768121d = AND v768121c(0xffffffffffffffffffffffffffffffffffffffff), v7681214
    0x121e0x768: v768121e(0x0) = CONST 
    0x12200x768: v7681220 = CALLDATASIZE 
    0x12210x768: v7681221(0x40) = CONST 
    0x12230x768: v7681223 = MLOAD v7681221(0x40)
    0x12240x768: v7681224(0x24) = CONST 
    0x12260x768: v7681226 = ADD v7681224(0x24), v7681223
    0x12290x768: v7681229(0x20) = CONST 
    0x122b0x768: v768122b = ADD v7681229(0x20), v7681226
    0x122e0x768: v768122e(0x20) = SUB v768122b, v7681226
    0x12300x768: MSTORE v7681226, v768122e(0x20)
    0x12360x768: MSTORE v768122b, v7681220
    0x12370x768: v7681237(0x20) = CONST 
    0x12390x768: v7681239 = ADD v7681237(0x20), v768122b
    0x123f0x768: CALLDATACOPY v7681239, v768121e(0x0), v7681220
    0x12400x768: v7681240(0x0) = CONST 
    0x12440x768: v7681244 = ADD v7681220, v7681239
    0x12450x768: MSTORE v7681244, v7681240(0x0)
    0x12460x768: v7681246(0x40) = CONST 
    0x12490x768: v7681249 = MLOAD v7681246(0x40)
    0x124a0x768: v768124a(0x1f) = CONST 
    0x124e0x768: v768124e = ADD v7681220, v768124a(0x1f)
    0x124f0x768: v768124f(0x1f) = CONST 
    0x12510x768: v7681251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v768124f(0x1f)
    0x12540x768: v7681254 = AND v7681251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v768124e
    0x12570x768: v7681257 = ADD v7681239, v7681254
    0x125a0x768: v768125a = SUB v7681257, v7681249
    0x125d0x768: v768125d = ADD v7681251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v768125a
    0x125f0x768: MSTORE v7681249, v768125d
    0x12620x768: MSTORE v7681246(0x40), v7681257
    0x12630x768: v7681263(0x20) = CONST 
    0x12660x768: v7681266 = ADD v7681249, v7681263(0x20)
    0x12680x768: v7681268 = MLOAD v7681266
    0x12690x768: v7681269(0x1) = CONST 
    0x126b0x768: v768126b(0x1) = CONST 
    0x126d0x768: v768126d(0xe0) = CONST 
    0x126f0x768: v768126f(0x100000000000000000000000000000000000000000000000000000000) = SHL v768126d(0xe0), v768126b(0x1)
    0x12700x768: v7681270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v768126f(0x100000000000000000000000000000000000000000000000000000000), v7681269(0x1)
    0x12710x768: v7681271 = AND v7681270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v7681268
    0x12720x768: v7681272(0x933c1ed) = CONST 
    0x12770x768: v7681277(0xe0) = CONST 
    0x12790x768: v7681279(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v7681277(0xe0), v7681272(0x933c1ed)
    0x127a0x768: v768127a = OR v7681279(0x933c1ed00000000000000000000000000000000000000000000000000000000), v7681271
    0x127c0x768: MSTORE v7681266, v768127a
    0x127e0x768: v768127e = MLOAD v7681246(0x40)
    0x12800x768: v7681280 = MLOAD v7681249

    Begin block 0x12910x768
    prev=[0x129a0x768, 0x120f0x768], succ=[0x12b00x768, 0x129a0x768]
    =================================
    0x12910x768_0x2: v1291768_2 = PHI v76812a3, v7681280
    0x12920x768: v7681292(0x20) = CONST 
    0x12950x768: v7681295 = LT v1291768_2, v7681292(0x20)
    0x12960x768: v7681296(0x12b0) = CONST 
    0x12990x768: JUMPI v7681296(0x12b0), v7681295

    Begin block 0x12b00x768
    prev=[0x12910x768], succ=[0x12ef0x768, 0x13100x768]
    =================================
    0x12b00x768_0x0: v12b0768_0 = PHI v76812ab, v7681266
    0x12b00x768_0x1: v12b0768_1 = PHI v76812a9, v768127e
    0x12b00x768_0x2: v12b0768_2 = PHI v76812a3, v7681280
    0x12b10x768: v76812b1(0x1) = CONST 
    0x12b40x768: v76812b4(0x20) = CONST 
    0x12b60x768: v76812b6 = SUB v76812b4(0x20), v12b0768_2
    0x12b70x768: v76812b7(0x100) = CONST 
    0x12ba0x768: v76812ba = EXP v76812b7(0x100), v76812b6
    0x12bb0x768: v76812bb = SUB v76812ba, v76812b1(0x1)
    0x12bd0x768: v76812bd = NOT v76812bb
    0x12bf0x768: v76812bf = MLOAD v12b0768_0
    0x12c00x768: v76812c0 = AND v76812bf, v76812bd
    0x12c30x768: v76812c3 = MLOAD v12b0768_1
    0x12c40x768: v76812c4 = AND v76812c3, v76812bb
    0x12c70x768: v76812c7 = OR v76812c0, v76812c4
    0x12c90x768: MSTORE v12b0768_1, v76812c7
    0x12d20x768: v76812d2 = ADD v7681280, v768127e
    0x12d60x768: v76812d6(0x0) = CONST 
    0x12d80x768: v76812d8(0x40) = CONST 
    0x12da0x768: v76812da = MLOAD v76812d8(0x40)
    0x12dd0x768: v76812dd = SUB v76812d2, v76812da
    0x12e00x768: v76812e0 = GAS 
    0x12e10x768: v76812e1 = STATICCALL v76812e0, v768121d, v76812da, v76812dd, v76812da, v76812d6(0x0)
    0x12e50x768: v76812e5 = RETURNDATASIZE 
    0x12e70x768: v76812e7(0x0) = CONST 
    0x12ea0x768: v76812ea = EQ v76812e5, v76812e7(0x0)
    0x12eb0x768: v76812eb(0x1310) = CONST 
    0x12ee0x768: JUMPI v76812eb(0x1310), v76812ea

    Begin block 0x12ef0x768
    prev=[0x12b00x768], succ=[0x13150x768]
    =================================
    0x12ef0x768: v76812ef(0x40) = CONST 
    0x12f10x768: v76812f1 = MLOAD v76812ef(0x40)
    0x12f40x768: v76812f4(0x1f) = CONST 
    0x12f60x768: v76812f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v76812f4(0x1f)
    0x12f70x768: v76812f7(0x3f) = CONST 
    0x12f90x768: v76812f9 = RETURNDATASIZE 
    0x12fa0x768: v76812fa = ADD v76812f9, v76812f7(0x3f)
    0x12fb0x768: v76812fb = AND v76812fa, v76812f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12fd0x768: v76812fd = ADD v76812f1, v76812fb
    0x12fe0x768: v76812fe(0x40) = CONST 
    0x13000x768: MSTORE v76812fe(0x40), v76812fd
    0x13010x768: v7681301 = RETURNDATASIZE 
    0x13030x768: MSTORE v76812f1, v7681301
    0x13040x768: v7681304 = RETURNDATASIZE 
    0x13050x768: v7681305(0x0) = CONST 
    0x13070x768: v7681307(0x20) = CONST 
    0x130a0x768: v768130a = ADD v76812f1, v7681307(0x20)
    0x130b0x768: RETURNDATACOPY v768130a, v7681305(0x0), v7681304
    0x130c0x768: v768130c(0x1315) = CONST 
    0x130f0x768: JUMP v768130c(0x1315)

    Begin block 0x13150x768
    prev=[0x12ef0x768, 0x13100x768], succ=[0x13290x768, 0x14790x768]
    =================================
    0x131a0x768: v768131a(0x40) = CONST 
    0x131c0x768: v768131c = MLOAD v768131a(0x40)
    0x131d0x768: v768131d = RETURNDATASIZE 
    0x131e0x768: v768131e(0x0) = CONST 
    0x13210x768: RETURNDATACOPY v768131c, v768131e(0x0), v768131d
    0x13240x768: v7681324 = ISZERO v76812e1
    0x13250x768: v7681325(0x1479) = CONST 
    0x13280x768: JUMPI v7681325(0x1479), v7681324

    Begin block 0x13290x768
    prev=[0x13150x768], succ=[]
    =================================
    0x13290x768: v7681329 = RETURNDATASIZE 
    0x132a0x768: v768132a(0x40) = CONST 
    0x132d0x768: v768132d = ADD v768131c, v768132a(0x40)
    0x132e0x768: RETURN v768132d, v7681329

    Begin block 0x14790x768
    prev=[0x13150x768], succ=[]
    =================================
    0x147a0x768: v768147a = RETURNDATASIZE 
    0x147c0x768: REVERT v768131c, v768147a

    Begin block 0x13100x768
    prev=[0x12b00x768], succ=[0x13150x768]
    =================================
    0x13110x768: v7681311(0x60) = CONST 

    Begin block 0x129a0x768
    prev=[0x12910x768], succ=[0x12910x768]
    =================================
    0x129a0x768_0x0: v129a768_0 = PHI v76812ab, v7681266
    0x129a0x768_0x1: v129a768_1 = PHI v76812a9, v768127e
    0x129a0x768_0x2: v129a768_2 = PHI v76812a3, v7681280
    0x129b0x768: v768129b = MLOAD v129a768_0
    0x129d0x768: MSTORE v129a768_1, v768129b
    0x129e0x768: v768129e(0x1f) = CONST 
    0x12a00x768: v76812a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v768129e(0x1f)
    0x12a30x768: v76812a3 = ADD v129a768_2, v76812a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a50x768: v76812a5(0x20) = CONST 
    0x12a90x768: v76812a9 = ADD v76812a5(0x20), v129a768_1
    0x12ab0x768: v76812ab = ADD v76812a5(0x20), v129a768_0
    0x12ac0x768: v76812ac(0x1291) = CONST 
    0x12af0x768: JUMP v76812ac(0x1291)

}

function _setRebaser(address)() public {
    Begin block 0x78b
    prev=[], succ=[0x793, 0x797]
    =================================
    0x78c: v78c = CALLVALUE 
    0x78e: v78e = ISZERO v78c
    0x78f: v78f(0x797) = CONST 
    0x792: JUMPI v78f(0x797), v78e

    Begin block 0x793
    prev=[0x78b], succ=[]
    =================================
    0x793: v793(0x0) = CONST 
    0x796: REVERT v793(0x0), v793(0x0)

    Begin block 0x797
    prev=[0x78b], succ=[0x7aa, 0x7ae]
    =================================
    0x799: v799(0x1793) = CONST 
    0x79c: v79c(0x4) = CONST 
    0x79f: v79f = CALLDATASIZE 
    0x7a0: v7a0 = SUB v79f, v79c(0x4)
    0x7a1: v7a1(0x20) = CONST 
    0x7a4: v7a4 = LT v7a0, v7a1(0x20)
    0x7a5: v7a5 = ISZERO v7a4
    0x7a6: v7a6(0x7ae) = CONST 
    0x7a9: JUMPI v7a6(0x7ae), v7a5

    Begin block 0x7aa
    prev=[0x797], succ=[]
    =================================
    0x7aa: v7aa(0x0) = CONST 
    0x7ad: REVERT v7aa(0x0), v7aa(0x0)

    Begin block 0x7ae
    prev=[0x797], succ=[0x1018]
    =================================
    0x7b0: v7b0 = CALLDATALOAD v79c(0x4)
    0x7b1: v7b1(0x1) = CONST 
    0x7b3: v7b3(0x1) = CONST 
    0x7b5: v7b5(0xa0) = CONST 
    0x7b7: v7b7(0x10000000000000000000000000000000000000000) = SHL v7b5(0xa0), v7b3(0x1)
    0x7b8: v7b8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b7(0x10000000000000000000000000000000000000000), v7b1(0x1)
    0x7b9: v7b9 = AND v7b8(0xffffffffffffffffffffffffffffffffffffffff), v7b0
    0x7ba: v7ba(0x1018) = CONST 
    0x7bd: JUMP v7ba(0x1018)

    Begin block 0x1018
    prev=[0x7ae], succ=[0xa440x78b]
    =================================
    0x1019: v1019(0x1020) = CONST 
    0x101c: v101c(0xa44) = CONST 
    0x101f: JUMP v101c(0xa44)

    Begin block 0xa440x78b
    prev=[0x1018], succ=[0xa8b0x78b, 0xaac0x78b]
    =================================
    0xa450x78b: v78ba45(0x13) = CONST 
    0xa470x78b: v78ba47 = SLOAD v78ba45(0x13)
    0xa480x78b: v78ba48(0x40) = CONST 
    0xa4a0x78b: v78ba4a = MLOAD v78ba48(0x40)
    0xa4b0x78b: v78ba4b(0x60) = CONST 
    0xa4e0x78b: v78ba4e(0x0) = CONST 
    0xa510x78b: v78ba51(0x1) = CONST 
    0xa530x78b: v78ba53(0x1) = CONST 
    0xa550x78b: v78ba55(0xa0) = CONST 
    0xa570x78b: v78ba57(0x10000000000000000000000000000000000000000) = SHL v78ba55(0xa0), v78ba53(0x1)
    0xa580x78b: v78ba58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v78ba57(0x10000000000000000000000000000000000000000), v78ba51(0x1)
    0xa5b0x78b: v78ba5b = AND v78ba47, v78ba58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x78b: v78ba5f = CALLDATASIZE 
    0xa670x78b: CALLDATACOPY v78ba4a, v78ba4e(0x0), v78ba5f
    0xa680x78b: v78ba68(0x40) = CONST 
    0xa6a0x78b: v78ba6a = MLOAD v78ba68(0x40)
    0xa6c0x78b: v78ba6c = ADD v78ba4a, v78ba5f
    0xa6f0x78b: v78ba6f(0x0) = CONST 
    0xa790x78b: v78ba79 = SUB v78ba6c, v78ba6a
    0xa7c0x78b: v78ba7c = GAS 
    0xa7d0x78b: v78ba7d = DELEGATECALL v78ba7c, v78ba5b, v78ba6a, v78ba79, v78ba6a, v78ba6f(0x0)
    0xa810x78b: v78ba81 = RETURNDATASIZE 
    0xa830x78b: v78ba83(0x0) = CONST 
    0xa860x78b: v78ba86 = EQ v78ba81, v78ba83(0x0)
    0xa870x78b: v78ba87(0xaac) = CONST 
    0xa8a0x78b: JUMPI v78ba87(0xaac), v78ba86

    Begin block 0xa8b0x78b
    prev=[0xa440x78b], succ=[0xab10x78b]
    =================================
    0xa8b0x78b: v78ba8b(0x40) = CONST 
    0xa8d0x78b: v78ba8d = MLOAD v78ba8b(0x40)
    0xa900x78b: v78ba90(0x1f) = CONST 
    0xa920x78b: v78ba92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v78ba90(0x1f)
    0xa930x78b: v78ba93(0x3f) = CONST 
    0xa950x78b: v78ba95 = RETURNDATASIZE 
    0xa960x78b: v78ba96 = ADD v78ba95, v78ba93(0x3f)
    0xa970x78b: v78ba97 = AND v78ba96, v78ba92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x78b: v78ba99 = ADD v78ba8d, v78ba97
    0xa9a0x78b: v78ba9a(0x40) = CONST 
    0xa9c0x78b: MSTORE v78ba9a(0x40), v78ba99
    0xa9d0x78b: v78ba9d = RETURNDATASIZE 
    0xa9f0x78b: MSTORE v78ba8d, v78ba9d
    0xaa00x78b: v78baa0 = RETURNDATASIZE 
    0xaa10x78b: v78baa1(0x0) = CONST 
    0xaa30x78b: v78baa3(0x20) = CONST 
    0xaa60x78b: v78baa6 = ADD v78ba8d, v78baa3(0x20)
    0xaa70x78b: RETURNDATACOPY v78baa6, v78baa1(0x0), v78baa0
    0xaa80x78b: v78baa8(0xab1) = CONST 
    0xaab0x78b: JUMP v78baa8(0xab1)

    Begin block 0xab10x78b
    prev=[0xa8b0x78b, 0xaac0x78b], succ=[0xac50x78b, 0x14560x78b]
    =================================
    0xab60x78b: v78bab6(0x40) = CONST 
    0xab80x78b: v78bab8 = MLOAD v78bab6(0x40)
    0xab90x78b: v78bab9 = RETURNDATASIZE 
    0xaba0x78b: v78baba(0x0) = CONST 
    0xabd0x78b: RETURNDATACOPY v78bab8, v78baba(0x0), v78bab9
    0xac00x78b: v78bac0 = ISZERO v78ba7d
    0xac10x78b: v78bac1(0x1456) = CONST 
    0xac40x78b: JUMPI v78bac1(0x1456), v78bac0

    Begin block 0xac50x78b
    prev=[0xab10x78b], succ=[]
    =================================
    0xac50x78b: v78bac5 = RETURNDATASIZE 
    0xac70x78b: RETURN v78bab8, v78bac5

    Begin block 0x14560x78b
    prev=[0xab10x78b], succ=[]
    =================================
    0x14570x78b: v78b1457 = RETURNDATASIZE 
    0x14590x78b: REVERT v78bab8, v78b1457

    Begin block 0xaac0x78b
    prev=[0xa440x78b], succ=[0xab10x78b]
    =================================
    0xaad0x78b: v78baad(0x60) = CONST 

}

function implementation()() public {
    Begin block 0x7be
    prev=[], succ=[0x7c6, 0x7ca]
    =================================
    0x7bf: v7bf = CALLVALUE 
    0x7c1: v7c1 = ISZERO v7bf
    0x7c2: v7c2(0x7ca) = CONST 
    0x7c5: JUMPI v7c2(0x7ca), v7c1

    Begin block 0x7c6
    prev=[0x7be], succ=[]
    =================================
    0x7c6: v7c6(0x0) = CONST 
    0x7c9: REVERT v7c6(0x0), v7c6(0x0)

    Begin block 0x7ca
    prev=[0x7be], succ=[0x1024]
    =================================
    0x7cc: v7cc(0x17b4) = CONST 
    0x7cf: v7cf(0x1024) = CONST 
    0x7d2: JUMP v7cf(0x1024)

    Begin block 0x1024
    prev=[0x7ca], succ=[0x17b4]
    =================================
    0x1025: v1025(0x13) = CONST 
    0x1027: v1027 = SLOAD v1025(0x13)
    0x1028: v1028(0x1) = CONST 
    0x102a: v102a(0x1) = CONST 
    0x102c: v102c(0xa0) = CONST 
    0x102e: v102e(0x10000000000000000000000000000000000000000) = SHL v102c(0xa0), v102a(0x1)
    0x102f: v102f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v102e(0x10000000000000000000000000000000000000000), v1028(0x1)
    0x1030: v1030 = AND v102f(0xffffffffffffffffffffffffffffffffffffffff), v1027
    0x1032: JUMP v7cc(0x17b4)

    Begin block 0x17b4
    prev=[0x1024], succ=[]
    =================================
    0x17b5: v17b5(0x40) = CONST 
    0x17b8: v17b8 = MLOAD v17b5(0x40)
    0x17b9: v17b9(0x1) = CONST 
    0x17bb: v17bb(0x1) = CONST 
    0x17bd: v17bd(0xa0) = CONST 
    0x17bf: v17bf(0x10000000000000000000000000000000000000000) = SHL v17bd(0xa0), v17bb(0x1)
    0x17c0: v17c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17bf(0x10000000000000000000000000000000000000000), v17b9(0x1)
    0x17c3: v17c3 = AND v1030, v17c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x17c5: MSTORE v17b8, v17c3
    0x17c6: v17c6 = MLOAD v17b5(0x40)
    0x17ca: v17ca(0x0) = SUB v17b8, v17c6
    0x17cb: v17cb(0x20) = CONST 
    0x17cd: v17cd(0x20) = ADD v17cb(0x20), v17ca(0x0)
    0x17cf: RETURN v17c6, v17cd(0x20)

}

function internalDecimals()() public {
    Begin block 0x7d3
    prev=[], succ=[0x7db, 0x7df]
    =================================
    0x7d4: v7d4 = CALLVALUE 
    0x7d6: v7d6 = ISZERO v7d4
    0x7d7: v7d7(0x7df) = CONST 
    0x7da: JUMPI v7d7(0x7df), v7d6

    Begin block 0x7db
    prev=[0x7d3], succ=[]
    =================================
    0x7db: v7db(0x0) = CONST 
    0x7de: REVERT v7db(0x0), v7db(0x0)

    Begin block 0x7df
    prev=[0x7d3], succ=[0x1033]
    =================================
    0x7e1: v7e1(0x17ef) = CONST 
    0x7e4: v7e4(0x1033) = CONST 
    0x7e7: JUMP v7e4(0x1033)

    Begin block 0x1033
    prev=[0x7df], succ=[0x17ef]
    =================================
    0x1034: v1034(0xd3c21bcecceda1000000) = CONST 
    0x1040: JUMP v7e1(0x17ef)

    Begin block 0x17ef
    prev=[0x1033], succ=[]
    =================================
    0x17f0: v17f0(0x40) = CONST 
    0x17f3: v17f3 = MLOAD v17f0(0x40)
    0x17f6: MSTORE v17f3, v1034(0xd3c21bcecceda1000000)
    0x17f7: v17f7 = MLOAD v17f0(0x40)
    0x17fb: v17fb(0x0) = SUB v17f3, v17f7
    0x17fc: v17fc(0x20) = CONST 
    0x17fe: v17fe(0x20) = ADD v17fc(0x20), v17fb(0x0)
    0x1800: RETURN v17f7, v17fe(0x20)

}

function incentivizer()() public {
    Begin block 0x7e8
    prev=[], succ=[0x7f0, 0x7f4]
    =================================
    0x7e9: v7e9 = CALLVALUE 
    0x7eb: v7eb = ISZERO v7e9
    0x7ec: v7ec(0x7f4) = CONST 
    0x7ef: JUMPI v7ec(0x7f4), v7eb

    Begin block 0x7f0
    prev=[0x7e8], succ=[]
    =================================
    0x7f0: v7f0(0x0) = CONST 
    0x7f3: REVERT v7f0(0x0), v7f0(0x0)

    Begin block 0x7f4
    prev=[0x7e8], succ=[0x1041]
    =================================
    0x7f6: v7f6(0x1820) = CONST 
    0x7f9: v7f9(0x1041) = CONST 
    0x7fc: JUMP v7f9(0x1041)

    Begin block 0x1041
    prev=[0x7f4], succ=[0x1820]
    =================================
    0x1042: v1042(0x6) = CONST 
    0x1044: v1044 = SLOAD v1042(0x6)
    0x1045: v1045(0x1) = CONST 
    0x1047: v1047(0x1) = CONST 
    0x1049: v1049(0xa0) = CONST 
    0x104b: v104b(0x10000000000000000000000000000000000000000) = SHL v1049(0xa0), v1047(0x1)
    0x104c: v104c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v104b(0x10000000000000000000000000000000000000000), v1045(0x1)
    0x104d: v104d = AND v104c(0xffffffffffffffffffffffffffffffffffffffff), v1044
    0x104f: JUMP v7f6(0x1820)

    Begin block 0x1820
    prev=[0x1041], succ=[]
    =================================
    0x1821: v1821(0x40) = CONST 
    0x1824: v1824 = MLOAD v1821(0x40)
    0x1825: v1825(0x1) = CONST 
    0x1827: v1827(0x1) = CONST 
    0x1829: v1829(0xa0) = CONST 
    0x182b: v182b(0x10000000000000000000000000000000000000000) = SHL v1829(0xa0), v1827(0x1)
    0x182c: v182c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v182b(0x10000000000000000000000000000000000000000), v1825(0x1)
    0x182f: v182f = AND v104d, v182c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1831: MSTORE v1824, v182f
    0x1832: v1832 = MLOAD v1821(0x40)
    0x1836: v1836(0x0) = SUB v1824, v1832
    0x1837: v1837(0x20) = CONST 
    0x1839: v1839(0x20) = ADD v1837(0x20), v1836(0x0)
    0x183b: RETURN v1832, v1839(0x20)

}

function numCheckpoints(address)() public {
    Begin block 0x7fd
    prev=[], succ=[0x805, 0x809]
    =================================
    0x7fe: v7fe = CALLVALUE 
    0x800: v800 = ISZERO v7fe
    0x801: v801(0x809) = CONST 
    0x804: JUMPI v801(0x809), v800

    Begin block 0x805
    prev=[0x7fd], succ=[]
    =================================
    0x805: v805(0x0) = CONST 
    0x808: REVERT v805(0x0), v805(0x0)

    Begin block 0x809
    prev=[0x7fd], succ=[0x81c, 0x820]
    =================================
    0x80b: v80b(0x830) = CONST 
    0x80e: v80e(0x4) = CONST 
    0x811: v811 = CALLDATASIZE 
    0x812: v812 = SUB v811, v80e(0x4)
    0x813: v813(0x20) = CONST 
    0x816: v816 = LT v812, v813(0x20)
    0x817: v817 = ISZERO v816
    0x818: v818(0x820) = CONST 
    0x81b: JUMPI v818(0x820), v817

    Begin block 0x81c
    prev=[0x809], succ=[]
    =================================
    0x81c: v81c(0x0) = CONST 
    0x81f: REVERT v81c(0x0), v81c(0x0)

    Begin block 0x820
    prev=[0x809], succ=[0x1050]
    =================================
    0x822: v822 = CALLDATALOAD v80e(0x4)
    0x823: v823(0x1) = CONST 
    0x825: v825(0x1) = CONST 
    0x827: v827(0xa0) = CONST 
    0x829: v829(0x10000000000000000000000000000000000000000) = SHL v827(0xa0), v825(0x1)
    0x82a: v82a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v829(0x10000000000000000000000000000000000000000), v823(0x1)
    0x82b: v82b = AND v82a(0xffffffffffffffffffffffffffffffffffffffff), v822
    0x82c: v82c(0x1050) = CONST 
    0x82f: JUMP v82c(0x1050)

    Begin block 0x1050
    prev=[0x820], succ=[0x830]
    =================================
    0x1051: v1051(0x11) = CONST 
    0x1053: v1053(0x20) = CONST 
    0x1055: MSTORE v1053(0x20), v1051(0x11)
    0x1056: v1056(0x0) = CONST 
    0x105a: MSTORE v1056(0x0), v82b
    0x105b: v105b(0x40) = CONST 
    0x105e: v105e = SHA3 v1056(0x0), v105b(0x40)
    0x105f: v105f = SLOAD v105e
    0x1060: v1060(0xffffffff) = CONST 
    0x1065: v1065 = AND v1060(0xffffffff), v105f
    0x1067: JUMP v80b(0x830)

    Begin block 0x830
    prev=[0x1050], succ=[]
    =================================
    0x831: v831(0x40) = CONST 
    0x834: v834 = MLOAD v831(0x40)
    0x835: v835(0xffffffff) = CONST 
    0x83c: v83c = AND v1065, v835(0xffffffff)
    0x83e: MSTORE v834, v83c
    0x83f: v83f = MLOAD v831(0x40)
    0x843: v843(0x0) = SUB v834, v83f
    0x844: v844(0x20) = CONST 
    0x846: v846(0x20) = ADD v844(0x20), v843(0x0)
    0x848: RETURN v83f, v846(0x20)

}

function getPriorVotes(address,uint256)() public {
    Begin block 0x849
    prev=[], succ=[0x851, 0x855]
    =================================
    0x84a: v84a = CALLVALUE 
    0x84c: v84c = ISZERO v84a
    0x84d: v84d(0x855) = CONST 
    0x850: JUMPI v84d(0x855), v84c

    Begin block 0x851
    prev=[0x849], succ=[]
    =================================
    0x851: v851(0x0) = CONST 
    0x854: REVERT v851(0x0), v851(0x0)

    Begin block 0x855
    prev=[0x849], succ=[0x868, 0x86c]
    =================================
    0x857: v857(0x185b) = CONST 
    0x85a: v85a(0x4) = CONST 
    0x85d: v85d = CALLDATASIZE 
    0x85e: v85e = SUB v85d, v85a(0x4)
    0x85f: v85f(0x40) = CONST 
    0x862: v862 = LT v85e, v85f(0x40)
    0x863: v863 = ISZERO v862
    0x864: v864(0x86c) = CONST 
    0x867: JUMPI v864(0x86c), v863

    Begin block 0x868
    prev=[0x855], succ=[]
    =================================
    0x868: v868(0x0) = CONST 
    0x86b: REVERT v868(0x0), v868(0x0)

    Begin block 0x86c
    prev=[0x855], succ=[0x10680x849]
    =================================
    0x86e: v86e(0x1) = CONST 
    0x870: v870(0x1) = CONST 
    0x872: v872(0xa0) = CONST 
    0x874: v874(0x10000000000000000000000000000000000000000) = SHL v872(0xa0), v870(0x1)
    0x875: v875(0xffffffffffffffffffffffffffffffffffffffff) = SUB v874(0x10000000000000000000000000000000000000000), v86e(0x1)
    0x877: v877 = CALLDATALOAD v85a(0x4)
    0x878: v878 = AND v877, v875(0xffffffffffffffffffffffffffffffffffffffff)
    0x87a: v87a(0x20) = CONST 
    0x87c: v87c(0x24) = ADD v87a(0x20), v85a(0x4)
    0x87d: v87d = CALLDATALOAD v87c(0x24)
    0x87e: v87e(0x1068) = CONST 
    0x881: JUMP v87e(0x1068)

    Begin block 0x10680x849
    prev=[0x86c], succ=[0x120f0x849]
    =================================
    0x10690x849: v8491069(0x0) = CONST 
    0x106b0x849: v849106b(0x1a78) = CONST 
    0x106e0x849: v849106e(0x120f) = CONST 
    0x10710x849: JUMP v849106e(0x120f)

    Begin block 0x120f0x849
    prev=[0x10680x849], succ=[0x12910x849]
    =================================
    0x12100x849: v8491210(0x60) = CONST 
    0x12120x849: v8491212(0x0) = CONST 
    0x12140x849: v8491214 = ADDRESS 
    0x12150x849: v8491215(0x1) = CONST 
    0x12170x849: v8491217(0x1) = CONST 
    0x12190x849: v8491219(0xa0) = CONST 
    0x121b0x849: v849121b(0x10000000000000000000000000000000000000000) = SHL v8491219(0xa0), v8491217(0x1)
    0x121c0x849: v849121c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v849121b(0x10000000000000000000000000000000000000000), v8491215(0x1)
    0x121d0x849: v849121d = AND v849121c(0xffffffffffffffffffffffffffffffffffffffff), v8491214
    0x121e0x849: v849121e(0x0) = CONST 
    0x12200x849: v8491220 = CALLDATASIZE 
    0x12210x849: v8491221(0x40) = CONST 
    0x12230x849: v8491223 = MLOAD v8491221(0x40)
    0x12240x849: v8491224(0x24) = CONST 
    0x12260x849: v8491226 = ADD v8491224(0x24), v8491223
    0x12290x849: v8491229(0x20) = CONST 
    0x122b0x849: v849122b = ADD v8491229(0x20), v8491226
    0x122e0x849: v849122e(0x20) = SUB v849122b, v8491226
    0x12300x849: MSTORE v8491226, v849122e(0x20)
    0x12360x849: MSTORE v849122b, v8491220
    0x12370x849: v8491237(0x20) = CONST 
    0x12390x849: v8491239 = ADD v8491237(0x20), v849122b
    0x123f0x849: CALLDATACOPY v8491239, v849121e(0x0), v8491220
    0x12400x849: v8491240(0x0) = CONST 
    0x12440x849: v8491244 = ADD v8491220, v8491239
    0x12450x849: MSTORE v8491244, v8491240(0x0)
    0x12460x849: v8491246(0x40) = CONST 
    0x12490x849: v8491249 = MLOAD v8491246(0x40)
    0x124a0x849: v849124a(0x1f) = CONST 
    0x124e0x849: v849124e = ADD v8491220, v849124a(0x1f)
    0x124f0x849: v849124f(0x1f) = CONST 
    0x12510x849: v8491251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v849124f(0x1f)
    0x12540x849: v8491254 = AND v8491251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v849124e
    0x12570x849: v8491257 = ADD v8491239, v8491254
    0x125a0x849: v849125a = SUB v8491257, v8491249
    0x125d0x849: v849125d = ADD v8491251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v849125a
    0x125f0x849: MSTORE v8491249, v849125d
    0x12620x849: MSTORE v8491246(0x40), v8491257
    0x12630x849: v8491263(0x20) = CONST 
    0x12660x849: v8491266 = ADD v8491249, v8491263(0x20)
    0x12680x849: v8491268 = MLOAD v8491266
    0x12690x849: v8491269(0x1) = CONST 
    0x126b0x849: v849126b(0x1) = CONST 
    0x126d0x849: v849126d(0xe0) = CONST 
    0x126f0x849: v849126f(0x100000000000000000000000000000000000000000000000000000000) = SHL v849126d(0xe0), v849126b(0x1)
    0x12700x849: v8491270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v849126f(0x100000000000000000000000000000000000000000000000000000000), v8491269(0x1)
    0x12710x849: v8491271 = AND v8491270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v8491268
    0x12720x849: v8491272(0x933c1ed) = CONST 
    0x12770x849: v8491277(0xe0) = CONST 
    0x12790x849: v8491279(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v8491277(0xe0), v8491272(0x933c1ed)
    0x127a0x849: v849127a = OR v8491279(0x933c1ed00000000000000000000000000000000000000000000000000000000), v8491271
    0x127c0x849: MSTORE v8491266, v849127a
    0x127e0x849: v849127e = MLOAD v8491246(0x40)
    0x12800x849: v8491280 = MLOAD v8491249

    Begin block 0x12910x849
    prev=[0x129a0x849, 0x120f0x849], succ=[0x12b00x849, 0x129a0x849]
    =================================
    0x12910x849_0x2: v1291849_2 = PHI v84912a3, v8491280
    0x12920x849: v8491292(0x20) = CONST 
    0x12950x849: v8491295 = LT v1291849_2, v8491292(0x20)
    0x12960x849: v8491296(0x12b0) = CONST 
    0x12990x849: JUMPI v8491296(0x12b0), v8491295

    Begin block 0x12b00x849
    prev=[0x12910x849], succ=[0x12ef0x849, 0x13100x849]
    =================================
    0x12b00x849_0x0: v12b0849_0 = PHI v84912ab, v8491266
    0x12b00x849_0x1: v12b0849_1 = PHI v84912a9, v849127e
    0x12b00x849_0x2: v12b0849_2 = PHI v84912a3, v8491280
    0x12b10x849: v84912b1(0x1) = CONST 
    0x12b40x849: v84912b4(0x20) = CONST 
    0x12b60x849: v84912b6 = SUB v84912b4(0x20), v12b0849_2
    0x12b70x849: v84912b7(0x100) = CONST 
    0x12ba0x849: v84912ba = EXP v84912b7(0x100), v84912b6
    0x12bb0x849: v84912bb = SUB v84912ba, v84912b1(0x1)
    0x12bd0x849: v84912bd = NOT v84912bb
    0x12bf0x849: v84912bf = MLOAD v12b0849_0
    0x12c00x849: v84912c0 = AND v84912bf, v84912bd
    0x12c30x849: v84912c3 = MLOAD v12b0849_1
    0x12c40x849: v84912c4 = AND v84912c3, v84912bb
    0x12c70x849: v84912c7 = OR v84912c0, v84912c4
    0x12c90x849: MSTORE v12b0849_1, v84912c7
    0x12d20x849: v84912d2 = ADD v8491280, v849127e
    0x12d60x849: v84912d6(0x0) = CONST 
    0x12d80x849: v84912d8(0x40) = CONST 
    0x12da0x849: v84912da = MLOAD v84912d8(0x40)
    0x12dd0x849: v84912dd = SUB v84912d2, v84912da
    0x12e00x849: v84912e0 = GAS 
    0x12e10x849: v84912e1 = STATICCALL v84912e0, v849121d, v84912da, v84912dd, v84912da, v84912d6(0x0)
    0x12e50x849: v84912e5 = RETURNDATASIZE 
    0x12e70x849: v84912e7(0x0) = CONST 
    0x12ea0x849: v84912ea = EQ v84912e5, v84912e7(0x0)
    0x12eb0x849: v84912eb(0x1310) = CONST 
    0x12ee0x849: JUMPI v84912eb(0x1310), v84912ea

    Begin block 0x12ef0x849
    prev=[0x12b00x849], succ=[0x13150x849]
    =================================
    0x12ef0x849: v84912ef(0x40) = CONST 
    0x12f10x849: v84912f1 = MLOAD v84912ef(0x40)
    0x12f40x849: v84912f4(0x1f) = CONST 
    0x12f60x849: v84912f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v84912f4(0x1f)
    0x12f70x849: v84912f7(0x3f) = CONST 
    0x12f90x849: v84912f9 = RETURNDATASIZE 
    0x12fa0x849: v84912fa = ADD v84912f9, v84912f7(0x3f)
    0x12fb0x849: v84912fb = AND v84912fa, v84912f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12fd0x849: v84912fd = ADD v84912f1, v84912fb
    0x12fe0x849: v84912fe(0x40) = CONST 
    0x13000x849: MSTORE v84912fe(0x40), v84912fd
    0x13010x849: v8491301 = RETURNDATASIZE 
    0x13030x849: MSTORE v84912f1, v8491301
    0x13040x849: v8491304 = RETURNDATASIZE 
    0x13050x849: v8491305(0x0) = CONST 
    0x13070x849: v8491307(0x20) = CONST 
    0x130a0x849: v849130a = ADD v84912f1, v8491307(0x20)
    0x130b0x849: RETURNDATACOPY v849130a, v8491305(0x0), v8491304
    0x130c0x849: v849130c(0x1315) = CONST 
    0x130f0x849: JUMP v849130c(0x1315)

    Begin block 0x13150x849
    prev=[0x12ef0x849, 0x13100x849], succ=[0x13290x849, 0x14790x849]
    =================================
    0x131a0x849: v849131a(0x40) = CONST 
    0x131c0x849: v849131c = MLOAD v849131a(0x40)
    0x131d0x849: v849131d = RETURNDATASIZE 
    0x131e0x849: v849131e(0x0) = CONST 
    0x13210x849: RETURNDATACOPY v849131c, v849131e(0x0), v849131d
    0x13240x849: v8491324 = ISZERO v84912e1
    0x13250x849: v8491325(0x1479) = CONST 
    0x13280x849: JUMPI v8491325(0x1479), v8491324

    Begin block 0x13290x849
    prev=[0x13150x849], succ=[]
    =================================
    0x13290x849: v8491329 = RETURNDATASIZE 
    0x132a0x849: v849132a(0x40) = CONST 
    0x132d0x849: v849132d = ADD v849131c, v849132a(0x40)
    0x132e0x849: RETURN v849132d, v8491329

    Begin block 0x14790x849
    prev=[0x13150x849], succ=[]
    =================================
    0x147a0x849: v849147a = RETURNDATASIZE 
    0x147c0x849: REVERT v849131c, v849147a

    Begin block 0x13100x849
    prev=[0x12b00x849], succ=[0x13150x849]
    =================================
    0x13110x849: v8491311(0x60) = CONST 

    Begin block 0x129a0x849
    prev=[0x12910x849], succ=[0x12910x849]
    =================================
    0x129a0x849_0x0: v129a849_0 = PHI v84912ab, v8491266
    0x129a0x849_0x1: v129a849_1 = PHI v84912a9, v849127e
    0x129a0x849_0x2: v129a849_2 = PHI v84912a3, v8491280
    0x129b0x849: v849129b = MLOAD v129a849_0
    0x129d0x849: MSTORE v129a849_1, v849129b
    0x129e0x849: v849129e(0x1f) = CONST 
    0x12a00x849: v84912a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v849129e(0x1f)
    0x12a30x849: v84912a3 = ADD v129a849_2, v84912a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a50x849: v84912a5(0x20) = CONST 
    0x12a90x849: v84912a9 = ADD v84912a5(0x20), v129a849_1
    0x12ab0x849: v84912ab = ADD v84912a5(0x20), v129a849_0
    0x12ac0x849: v84912ac(0x1291) = CONST 
    0x12af0x849: JUMP v84912ac(0x1291)

}

function rebase(uint256,uint256,bool)() public {
    Begin block 0x882
    prev=[], succ=[0x88a, 0x88e]
    =================================
    0x883: v883 = CALLVALUE 
    0x885: v885 = ISZERO v883
    0x886: v886(0x88e) = CONST 
    0x889: JUMPI v886(0x88e), v885

    Begin block 0x88a
    prev=[0x882], succ=[]
    =================================
    0x88a: v88a(0x0) = CONST 
    0x88d: REVERT v88a(0x0), v88a(0x0)

    Begin block 0x88e
    prev=[0x882], succ=[0x8a1, 0x8a5]
    =================================
    0x890: v890(0x188c) = CONST 
    0x893: v893(0x4) = CONST 
    0x896: v896 = CALLDATASIZE 
    0x897: v897 = SUB v896, v893(0x4)
    0x898: v898(0x60) = CONST 
    0x89b: v89b = LT v897, v898(0x60)
    0x89c: v89c = ISZERO v89b
    0x89d: v89d(0x8a5) = CONST 
    0x8a0: JUMPI v89d(0x8a5), v89c

    Begin block 0x8a1
    prev=[0x88e], succ=[]
    =================================
    0x8a1: v8a1(0x0) = CONST 
    0x8a4: REVERT v8a1(0x0), v8a1(0x0)

    Begin block 0x8a5
    prev=[0x88e], succ=[0xc020x882]
    =================================
    0x8a8: v8a8 = CALLDATALOAD v893(0x4)
    0x8aa: v8aa(0x20) = CONST 
    0x8ad: v8ad(0x24) = ADD v893(0x4), v8aa(0x20)
    0x8ae: v8ae = CALLDATALOAD v8ad(0x24)
    0x8b0: v8b0(0x40) = CONST 
    0x8b2: v8b2(0x44) = ADD v8b0(0x40), v893(0x4)
    0x8b3: v8b3 = CALLDATALOAD v8b2(0x44)
    0x8b4: v8b4 = ISZERO v8b3
    0x8b5: v8b5 = ISZERO v8b4
    0x8b6: v8b6(0xc02) = CONST 
    0x8b9: JUMP v8b6(0xc02)

    Begin block 0xc020x882
    prev=[0x8a5], succ=[0xa440x882]
    =================================
    0xc030x882: v882c03(0x0) = CONST 
    0xc050x882: v882c05(0xc0c) = CONST 
    0xc080x882: v882c08(0xa44) = CONST 
    0xc0b0x882: JUMP v882c08(0xa44)

    Begin block 0xa440x882
    prev=[0xc020x882], succ=[0xa8b0x882, 0xaac0x882]
    =================================
    0xa450x882: v882a45(0x13) = CONST 
    0xa470x882: v882a47 = SLOAD v882a45(0x13)
    0xa480x882: v882a48(0x40) = CONST 
    0xa4a0x882: v882a4a = MLOAD v882a48(0x40)
    0xa4b0x882: v882a4b(0x60) = CONST 
    0xa4e0x882: v882a4e(0x0) = CONST 
    0xa510x882: v882a51(0x1) = CONST 
    0xa530x882: v882a53(0x1) = CONST 
    0xa550x882: v882a55(0xa0) = CONST 
    0xa570x882: v882a57(0x10000000000000000000000000000000000000000) = SHL v882a55(0xa0), v882a53(0x1)
    0xa580x882: v882a58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v882a57(0x10000000000000000000000000000000000000000), v882a51(0x1)
    0xa5b0x882: v882a5b = AND v882a47, v882a58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x882: v882a5f = CALLDATASIZE 
    0xa670x882: CALLDATACOPY v882a4a, v882a4e(0x0), v882a5f
    0xa680x882: v882a68(0x40) = CONST 
    0xa6a0x882: v882a6a = MLOAD v882a68(0x40)
    0xa6c0x882: v882a6c = ADD v882a4a, v882a5f
    0xa6f0x882: v882a6f(0x0) = CONST 
    0xa790x882: v882a79 = SUB v882a6c, v882a6a
    0xa7c0x882: v882a7c = GAS 
    0xa7d0x882: v882a7d = DELEGATECALL v882a7c, v882a5b, v882a6a, v882a79, v882a6a, v882a6f(0x0)
    0xa810x882: v882a81 = RETURNDATASIZE 
    0xa830x882: v882a83(0x0) = CONST 
    0xa860x882: v882a86 = EQ v882a81, v882a83(0x0)
    0xa870x882: v882a87(0xaac) = CONST 
    0xa8a0x882: JUMPI v882a87(0xaac), v882a86

    Begin block 0xa8b0x882
    prev=[0xa440x882], succ=[0xab10x882]
    =================================
    0xa8b0x882: v882a8b(0x40) = CONST 
    0xa8d0x882: v882a8d = MLOAD v882a8b(0x40)
    0xa900x882: v882a90(0x1f) = CONST 
    0xa920x882: v882a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v882a90(0x1f)
    0xa930x882: v882a93(0x3f) = CONST 
    0xa950x882: v882a95 = RETURNDATASIZE 
    0xa960x882: v882a96 = ADD v882a95, v882a93(0x3f)
    0xa970x882: v882a97 = AND v882a96, v882a92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x882: v882a99 = ADD v882a8d, v882a97
    0xa9a0x882: v882a9a(0x40) = CONST 
    0xa9c0x882: MSTORE v882a9a(0x40), v882a99
    0xa9d0x882: v882a9d = RETURNDATASIZE 
    0xa9f0x882: MSTORE v882a8d, v882a9d
    0xaa00x882: v882aa0 = RETURNDATASIZE 
    0xaa10x882: v882aa1(0x0) = CONST 
    0xaa30x882: v882aa3(0x20) = CONST 
    0xaa60x882: v882aa6 = ADD v882a8d, v882aa3(0x20)
    0xaa70x882: RETURNDATACOPY v882aa6, v882aa1(0x0), v882aa0
    0xaa80x882: v882aa8(0xab1) = CONST 
    0xaab0x882: JUMP v882aa8(0xab1)

    Begin block 0xab10x882
    prev=[0xa8b0x882, 0xaac0x882], succ=[0xac50x882, 0x14560x882]
    =================================
    0xab60x882: v882ab6(0x40) = CONST 
    0xab80x882: v882ab8 = MLOAD v882ab6(0x40)
    0xab90x882: v882ab9 = RETURNDATASIZE 
    0xaba0x882: v882aba(0x0) = CONST 
    0xabd0x882: RETURNDATACOPY v882ab8, v882aba(0x0), v882ab9
    0xac00x882: v882ac0 = ISZERO v882a7d
    0xac10x882: v882ac1(0x1456) = CONST 
    0xac40x882: JUMPI v882ac1(0x1456), v882ac0

    Begin block 0xac50x882
    prev=[0xab10x882], succ=[]
    =================================
    0xac50x882: v882ac5 = RETURNDATASIZE 
    0xac70x882: RETURN v882ab8, v882ac5

    Begin block 0x14560x882
    prev=[0xab10x882], succ=[]
    =================================
    0x14570x882: v8821457 = RETURNDATASIZE 
    0x14590x882: REVERT v882ab8, v8821457

    Begin block 0xaac0x882
    prev=[0xa440x882], succ=[0xab10x882]
    =================================
    0xaad0x882: v882aad(0x60) = CONST 

}

function nonces(address)() public {
    Begin block 0x8ba
    prev=[], succ=[0x8c2, 0x8c6]
    =================================
    0x8bb: v8bb = CALLVALUE 
    0x8bd: v8bd = ISZERO v8bb
    0x8be: v8be(0x8c6) = CONST 
    0x8c1: JUMPI v8be(0x8c6), v8bd

    Begin block 0x8c2
    prev=[0x8ba], succ=[]
    =================================
    0x8c2: v8c2(0x0) = CONST 
    0x8c5: REVERT v8c2(0x0), v8c2(0x0)

    Begin block 0x8c6
    prev=[0x8ba], succ=[0x8d9, 0x8dd]
    =================================
    0x8c8: v8c8(0x18bd) = CONST 
    0x8cb: v8cb(0x4) = CONST 
    0x8ce: v8ce = CALLDATASIZE 
    0x8cf: v8cf = SUB v8ce, v8cb(0x4)
    0x8d0: v8d0(0x20) = CONST 
    0x8d3: v8d3 = LT v8cf, v8d0(0x20)
    0x8d4: v8d4 = ISZERO v8d3
    0x8d5: v8d5(0x8dd) = CONST 
    0x8d8: JUMPI v8d5(0x8dd), v8d4

    Begin block 0x8d9
    prev=[0x8c6], succ=[]
    =================================
    0x8d9: v8d9(0x0) = CONST 
    0x8dc: REVERT v8d9(0x0), v8d9(0x0)

    Begin block 0x8dd
    prev=[0x8c6], succ=[0x1072]
    =================================
    0x8df: v8df = CALLDATALOAD v8cb(0x4)
    0x8e0: v8e0(0x1) = CONST 
    0x8e2: v8e2(0x1) = CONST 
    0x8e4: v8e4(0xa0) = CONST 
    0x8e6: v8e6(0x10000000000000000000000000000000000000000) = SHL v8e4(0xa0), v8e2(0x1)
    0x8e7: v8e7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8e6(0x10000000000000000000000000000000000000000), v8e0(0x1)
    0x8e8: v8e8 = AND v8e7(0xffffffffffffffffffffffffffffffffffffffff), v8df
    0x8e9: v8e9(0x1072) = CONST 
    0x8ec: JUMP v8e9(0x1072)

    Begin block 0x1072
    prev=[0x8dd], succ=[0x18bd]
    =================================
    0x1073: v1073(0x12) = CONST 
    0x1075: v1075(0x20) = CONST 
    0x1077: MSTORE v1075(0x20), v1073(0x12)
    0x1078: v1078(0x0) = CONST 
    0x107c: MSTORE v1078(0x0), v8e8
    0x107d: v107d(0x40) = CONST 
    0x1080: v1080 = SHA3 v1078(0x0), v107d(0x40)
    0x1081: v1081 = SLOAD v1080
    0x1083: JUMP v8c8(0x18bd)

    Begin block 0x18bd
    prev=[0x1072], succ=[]
    =================================
    0x18be: v18be(0x40) = CONST 
    0x18c1: v18c1 = MLOAD v18be(0x40)
    0x18c4: MSTORE v18c1, v1081
    0x18c5: v18c5 = MLOAD v18be(0x40)
    0x18c9: v18c9(0x0) = SUB v18c1, v18c5
    0x18ca: v18ca(0x20) = CONST 
    0x18cc: v18cc(0x20) = ADD v18ca(0x20), v18c9(0x0)
    0x18ce: RETURN v18c5, v18cc(0x20)

}

function symbol()() public {
    Begin block 0x8ed
    prev=[], succ=[0x8f5, 0x8f9]
    =================================
    0x8ee: v8ee = CALLVALUE 
    0x8f0: v8f0 = ISZERO v8ee
    0x8f1: v8f1(0x8f9) = CONST 
    0x8f4: JUMPI v8f1(0x8f9), v8f0

    Begin block 0x8f5
    prev=[0x8ed], succ=[]
    =================================
    0x8f5: v8f5(0x0) = CONST 
    0x8f8: REVERT v8f5(0x0), v8f5(0x0)

    Begin block 0x8f9
    prev=[0x8ed], succ=[0x2c40x8ed]
    =================================
    0x8fb: v8fb(0x2c4) = CONST 
    0x8fe: v8fe(0x1084) = CONST 
    0x901: v901_0, v901_1 = CALLPRIVATE v8fe(0x1084), v8fb(0x2c4)

    Begin block 0x2c40x8ed
    prev=[0x8f9], succ=[0x2e60x8ed]
    =================================
    0x2c50x8ed: v8ed2c5(0x40) = CONST 
    0x2c80x8ed: v8ed2c8 = MLOAD v8ed2c5(0x40)
    0x2c90x8ed: v8ed2c9(0x20) = CONST 
    0x2cd0x8ed: MSTORE v8ed2c8, v8ed2c9(0x20)
    0x2cf0x8ed: v8ed2cf = MLOAD v901_0
    0x2d20x8ed: v8ed2d2 = ADD v8ed2c8, v8ed2c9(0x20)
    0x2d30x8ed: MSTORE v8ed2d2, v8ed2cf
    0x2d50x8ed: v8ed2d5 = MLOAD v901_0
    0x2dc0x8ed: v8ed2dc = ADD v8ed2c8, v8ed2c5(0x40)
    0x2df0x8ed: v8ed2df = ADD v901_0, v8ed2c9(0x20)
    0x2e40x8ed: v8ed2e4(0x0) = CONST 

    Begin block 0x2e60x8ed
    prev=[0x2ef0x8ed, 0x2c40x8ed], succ=[0x2fe0x8ed, 0x2ef0x8ed]
    =================================
    0x2e60x8ed_0x0: v2e68ed_0 = PHI v8ed2f9, v8ed2e4(0x0)
    0x2e90x8ed: v8ed2e9 = LT v2e68ed_0, v8ed2d5
    0x2ea0x8ed: v8ed2ea = ISZERO v8ed2e9
    0x2eb0x8ed: v8ed2eb(0x2fe) = CONST 
    0x2ee0x8ed: JUMPI v8ed2eb(0x2fe), v8ed2ea

    Begin block 0x2fe0x8ed
    prev=[0x2e60x8ed], succ=[0x32b0x8ed, 0x3120x8ed]
    =================================
    0x3070x8ed: v8ed307 = ADD v8ed2d5, v8ed2dc
    0x3090x8ed: v8ed309(0x1f) = CONST 
    0x30b0x8ed: v8ed30b = AND v8ed309(0x1f), v8ed2d5
    0x30d0x8ed: v8ed30d = ISZERO v8ed30b
    0x30e0x8ed: v8ed30e(0x32b) = CONST 
    0x3110x8ed: JUMPI v8ed30e(0x32b), v8ed30d

    Begin block 0x32b0x8ed
    prev=[0x2fe0x8ed, 0x3120x8ed], succ=[]
    =================================
    0x32b0x8ed_0x1: v32b8ed_1 = PHI v8ed328, v8ed307
    0x3310x8ed: v8ed331(0x40) = CONST 
    0x3330x8ed: v8ed333 = MLOAD v8ed331(0x40)
    0x3360x8ed: v8ed336 = SUB v32b8ed_1, v8ed333
    0x3380x8ed: RETURN v8ed333, v8ed336

    Begin block 0x3120x8ed
    prev=[0x2fe0x8ed], succ=[0x32b0x8ed]
    =================================
    0x3140x8ed: v8ed314 = SUB v8ed307, v8ed30b
    0x3160x8ed: v8ed316 = MLOAD v8ed314
    0x3170x8ed: v8ed317(0x1) = CONST 
    0x31a0x8ed: v8ed31a(0x20) = CONST 
    0x31c0x8ed: v8ed31c = SUB v8ed31a(0x20), v8ed30b
    0x31d0x8ed: v8ed31d(0x100) = CONST 
    0x3200x8ed: v8ed320 = EXP v8ed31d(0x100), v8ed31c
    0x3210x8ed: v8ed321 = SUB v8ed320, v8ed317(0x1)
    0x3220x8ed: v8ed322 = NOT v8ed321
    0x3230x8ed: v8ed323 = AND v8ed322, v8ed316
    0x3250x8ed: MSTORE v8ed314, v8ed323
    0x3260x8ed: v8ed326(0x20) = CONST 
    0x3280x8ed: v8ed328 = ADD v8ed326(0x20), v8ed314

    Begin block 0x2ef0x8ed
    prev=[0x2e60x8ed], succ=[0x2e60x8ed]
    =================================
    0x2ef0x8ed_0x0: v2ef8ed_0 = PHI v8ed2f9, v8ed2e4(0x0)
    0x2f10x8ed: v8ed2f1 = ADD v2ef8ed_0, v8ed2df
    0x2f20x8ed: v8ed2f2 = MLOAD v8ed2f1
    0x2f50x8ed: v8ed2f5 = ADD v2ef8ed_0, v8ed2dc
    0x2f60x8ed: MSTORE v8ed2f5, v8ed2f2
    0x2f70x8ed: v8ed2f7(0x20) = CONST 
    0x2f90x8ed: v8ed2f9 = ADD v8ed2f7(0x20), v2ef8ed_0
    0x2fa0x8ed: v8ed2fa(0x2e6) = CONST 
    0x2fd0x8ed: JUMP v8ed2fa(0x2e6)

}

function initSupply()() public {
    Begin block 0x902
    prev=[], succ=[0x90a, 0x90e]
    =================================
    0x903: v903 = CALLVALUE 
    0x905: v905 = ISZERO v903
    0x906: v906(0x90e) = CONST 
    0x909: JUMPI v906(0x90e), v905

    Begin block 0x90a
    prev=[0x902], succ=[]
    =================================
    0x90a: v90a(0x0) = CONST 
    0x90d: REVERT v90a(0x0), v90a(0x0)

    Begin block 0x90e
    prev=[0x902], succ=[0x10dc]
    =================================
    0x910: v910(0x18ee) = CONST 
    0x913: v913(0x10dc) = CONST 
    0x916: JUMP v913(0x10dc)

    Begin block 0x10dc
    prev=[0x90e], succ=[0x18ee]
    =================================
    0x10dd: v10dd(0xd) = CONST 
    0x10df: v10df = SLOAD v10dd(0xd)
    0x10e1: JUMP v910(0x18ee)

    Begin block 0x18ee
    prev=[0x10dc], succ=[]
    =================================
    0x18ef: v18ef(0x40) = CONST 
    0x18f2: v18f2 = MLOAD v18ef(0x40)
    0x18f5: MSTORE v18f2, v10df
    0x18f6: v18f6 = MLOAD v18ef(0x40)
    0x18fa: v18fa(0x0) = SUB v18f2, v18f6
    0x18fb: v18fb(0x20) = CONST 
    0x18fd: v18fd(0x20) = ADD v18fb(0x20), v18fa(0x0)
    0x18ff: RETURN v18f6, v18fd(0x20)

}

function yamsScalingFactor()() public {
    Begin block 0x917
    prev=[], succ=[0x91f, 0x923]
    =================================
    0x918: v918 = CALLVALUE 
    0x91a: v91a = ISZERO v918
    0x91b: v91b(0x923) = CONST 
    0x91e: JUMPI v91b(0x923), v91a

    Begin block 0x91f
    prev=[0x917], succ=[]
    =================================
    0x91f: v91f(0x0) = CONST 
    0x922: REVERT v91f(0x0), v91f(0x0)

    Begin block 0x923
    prev=[0x917], succ=[0x10e2]
    =================================
    0x925: v925(0x191f) = CONST 
    0x928: v928(0x10e2) = CONST 
    0x92b: JUMP v928(0x10e2)

    Begin block 0x10e2
    prev=[0x923], succ=[0x191f]
    =================================
    0x10e3: v10e3(0x8) = CONST 
    0x10e5: v10e5 = SLOAD v10e3(0x8)
    0x10e7: JUMP v925(0x191f)

    Begin block 0x191f
    prev=[0x10e2], succ=[]
    =================================
    0x1920: v1920(0x40) = CONST 
    0x1923: v1923 = MLOAD v1920(0x40)
    0x1926: MSTORE v1923, v10e5
    0x1927: v1927 = MLOAD v1920(0x40)
    0x192b: v192b(0x0) = SUB v1923, v1927
    0x192c: v192c(0x20) = CONST 
    0x192e: v192e(0x20) = ADD v192c(0x20), v192b(0x0)
    0x1930: RETURN v1927, v192e(0x20)

}

function delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32)() public {
    Begin block 0x92c
    prev=[], succ=[0x934, 0x938]
    =================================
    0x92d: v92d = CALLVALUE 
    0x92f: v92f = ISZERO v92d
    0x930: v930(0x938) = CONST 
    0x933: JUMPI v930(0x938), v92f

    Begin block 0x934
    prev=[0x92c], succ=[]
    =================================
    0x934: v934(0x0) = CONST 
    0x937: REVERT v934(0x0), v934(0x0)

    Begin block 0x938
    prev=[0x92c], succ=[0x94b, 0x94f]
    =================================
    0x93a: v93a(0x1950) = CONST 
    0x93d: v93d(0x4) = CONST 
    0x940: v940 = CALLDATASIZE 
    0x941: v941 = SUB v940, v93d(0x4)
    0x942: v942(0xc0) = CONST 
    0x945: v945 = LT v941, v942(0xc0)
    0x946: v946 = ISZERO v945
    0x947: v947(0x94f) = CONST 
    0x94a: JUMPI v947(0x94f), v946

    Begin block 0x94b
    prev=[0x938], succ=[]
    =================================
    0x94b: v94b(0x0) = CONST 
    0x94e: REVERT v94b(0x0), v94b(0x0)

    Begin block 0x94f
    prev=[0x938], succ=[0x10e8]
    =================================
    0x951: v951(0x1) = CONST 
    0x953: v953(0x1) = CONST 
    0x955: v955(0xa0) = CONST 
    0x957: v957(0x10000000000000000000000000000000000000000) = SHL v955(0xa0), v953(0x1)
    0x958: v958(0xffffffffffffffffffffffffffffffffffffffff) = SUB v957(0x10000000000000000000000000000000000000000), v951(0x1)
    0x95a: v95a = CALLDATALOAD v93d(0x4)
    0x95b: v95b = AND v95a, v958(0xffffffffffffffffffffffffffffffffffffffff)
    0x95d: v95d(0x20) = CONST 
    0x960: v960(0x24) = ADD v93d(0x4), v95d(0x20)
    0x961: v961 = CALLDATALOAD v960(0x24)
    0x963: v963(0x40) = CONST 
    0x966: v966(0x44) = ADD v93d(0x4), v963(0x40)
    0x967: v967 = CALLDATALOAD v966(0x44)
    0x969: v969(0xff) = CONST 
    0x96b: v96b(0x60) = CONST 
    0x96e: v96e(0x64) = ADD v93d(0x4), v96b(0x60)
    0x96f: v96f = CALLDATALOAD v96e(0x64)
    0x970: v970 = AND v96f, v969(0xff)
    0x972: v972(0x80) = CONST 
    0x975: v975(0x84) = ADD v93d(0x4), v972(0x80)
    0x976: v976 = CALLDATALOAD v975(0x84)
    0x978: v978(0xa0) = CONST 
    0x97a: v97a(0xa4) = ADD v978(0xa0), v93d(0x4)
    0x97b: v97b = CALLDATALOAD v97a(0xa4)
    0x97c: v97c(0x10e8) = CONST 
    0x97f: JUMP v97c(0x10e8)

    Begin block 0x10e8
    prev=[0x94f], succ=[0xa440x92c]
    =================================
    0x10e9: v10e9(0x10f0) = CONST 
    0x10ec: v10ec(0xa44) = CONST 
    0x10ef: JUMP v10ec(0xa44)

    Begin block 0xa440x92c
    prev=[0x10e8], succ=[0xa8b0x92c, 0xaac0x92c]
    =================================
    0xa450x92c: v92ca45(0x13) = CONST 
    0xa470x92c: v92ca47 = SLOAD v92ca45(0x13)
    0xa480x92c: v92ca48(0x40) = CONST 
    0xa4a0x92c: v92ca4a = MLOAD v92ca48(0x40)
    0xa4b0x92c: v92ca4b(0x60) = CONST 
    0xa4e0x92c: v92ca4e(0x0) = CONST 
    0xa510x92c: v92ca51(0x1) = CONST 
    0xa530x92c: v92ca53(0x1) = CONST 
    0xa550x92c: v92ca55(0xa0) = CONST 
    0xa570x92c: v92ca57(0x10000000000000000000000000000000000000000) = SHL v92ca55(0xa0), v92ca53(0x1)
    0xa580x92c: v92ca58(0xffffffffffffffffffffffffffffffffffffffff) = SUB v92ca57(0x10000000000000000000000000000000000000000), v92ca51(0x1)
    0xa5b0x92c: v92ca5b = AND v92ca47, v92ca58(0xffffffffffffffffffffffffffffffffffffffff)
    0xa5f0x92c: v92ca5f = CALLDATASIZE 
    0xa670x92c: CALLDATACOPY v92ca4a, v92ca4e(0x0), v92ca5f
    0xa680x92c: v92ca68(0x40) = CONST 
    0xa6a0x92c: v92ca6a = MLOAD v92ca68(0x40)
    0xa6c0x92c: v92ca6c = ADD v92ca4a, v92ca5f
    0xa6f0x92c: v92ca6f(0x0) = CONST 
    0xa790x92c: v92ca79 = SUB v92ca6c, v92ca6a
    0xa7c0x92c: v92ca7c = GAS 
    0xa7d0x92c: v92ca7d = DELEGATECALL v92ca7c, v92ca5b, v92ca6a, v92ca79, v92ca6a, v92ca6f(0x0)
    0xa810x92c: v92ca81 = RETURNDATASIZE 
    0xa830x92c: v92ca83(0x0) = CONST 
    0xa860x92c: v92ca86 = EQ v92ca81, v92ca83(0x0)
    0xa870x92c: v92ca87(0xaac) = CONST 
    0xa8a0x92c: JUMPI v92ca87(0xaac), v92ca86

    Begin block 0xa8b0x92c
    prev=[0xa440x92c], succ=[0xab10x92c]
    =================================
    0xa8b0x92c: v92ca8b(0x40) = CONST 
    0xa8d0x92c: v92ca8d = MLOAD v92ca8b(0x40)
    0xa900x92c: v92ca90(0x1f) = CONST 
    0xa920x92c: v92ca92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v92ca90(0x1f)
    0xa930x92c: v92ca93(0x3f) = CONST 
    0xa950x92c: v92ca95 = RETURNDATASIZE 
    0xa960x92c: v92ca96 = ADD v92ca95, v92ca93(0x3f)
    0xa970x92c: v92ca97 = AND v92ca96, v92ca92(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa990x92c: v92ca99 = ADD v92ca8d, v92ca97
    0xa9a0x92c: v92ca9a(0x40) = CONST 
    0xa9c0x92c: MSTORE v92ca9a(0x40), v92ca99
    0xa9d0x92c: v92ca9d = RETURNDATASIZE 
    0xa9f0x92c: MSTORE v92ca8d, v92ca9d
    0xaa00x92c: v92caa0 = RETURNDATASIZE 
    0xaa10x92c: v92caa1(0x0) = CONST 
    0xaa30x92c: v92caa3(0x20) = CONST 
    0xaa60x92c: v92caa6 = ADD v92ca8d, v92caa3(0x20)
    0xaa70x92c: RETURNDATACOPY v92caa6, v92caa1(0x0), v92caa0
    0xaa80x92c: v92caa8(0xab1) = CONST 
    0xaab0x92c: JUMP v92caa8(0xab1)

    Begin block 0xab10x92c
    prev=[0xa8b0x92c, 0xaac0x92c], succ=[0xac50x92c, 0x14560x92c]
    =================================
    0xab60x92c: v92cab6(0x40) = CONST 
    0xab80x92c: v92cab8 = MLOAD v92cab6(0x40)
    0xab90x92c: v92cab9 = RETURNDATASIZE 
    0xaba0x92c: v92caba(0x0) = CONST 
    0xabd0x92c: RETURNDATACOPY v92cab8, v92caba(0x0), v92cab9
    0xac00x92c: v92cac0 = ISZERO v92ca7d
    0xac10x92c: v92cac1(0x1456) = CONST 
    0xac40x92c: JUMPI v92cac1(0x1456), v92cac0

    Begin block 0xac50x92c
    prev=[0xab10x92c], succ=[]
    =================================
    0xac50x92c: v92cac5 = RETURNDATASIZE 
    0xac70x92c: RETURN v92cab8, v92cac5

    Begin block 0x14560x92c
    prev=[0xab10x92c], succ=[]
    =================================
    0x14570x92c: v92c1457 = RETURNDATASIZE 
    0x14590x92c: REVERT v92cab8, v92c1457

    Begin block 0xaac0x92c
    prev=[0xa440x92c], succ=[0xab10x92c]
    =================================
    0xaad0x92c: v92caad(0x60) = CONST 

}

function allowance(address,address)() public {
    Begin block 0x980
    prev=[], succ=[0x988, 0x98c]
    =================================
    0x981: v981 = CALLVALUE 
    0x983: v983 = ISZERO v981
    0x984: v984(0x98c) = CONST 
    0x987: JUMPI v984(0x98c), v983

    Begin block 0x988
    prev=[0x980], succ=[]
    =================================
    0x988: v988(0x0) = CONST 
    0x98b: REVERT v988(0x0), v988(0x0)

    Begin block 0x98c
    prev=[0x980], succ=[0x99f, 0x9a3]
    =================================
    0x98e: v98e(0x1971) = CONST 
    0x991: v991(0x4) = CONST 
    0x994: v994 = CALLDATASIZE 
    0x995: v995 = SUB v994, v991(0x4)
    0x996: v996(0x40) = CONST 
    0x999: v999 = LT v995, v996(0x40)
    0x99a: v99a = ISZERO v999
    0x99b: v99b(0x9a3) = CONST 
    0x99e: JUMPI v99b(0x9a3), v99a

    Begin block 0x99f
    prev=[0x98c], succ=[]
    =================================
    0x99f: v99f(0x0) = CONST 
    0x9a2: REVERT v99f(0x0), v99f(0x0)

    Begin block 0x9a3
    prev=[0x98c], succ=[0x10680x980]
    =================================
    0x9a5: v9a5(0x1) = CONST 
    0x9a7: v9a7(0x1) = CONST 
    0x9a9: v9a9(0xa0) = CONST 
    0x9ab: v9ab(0x10000000000000000000000000000000000000000) = SHL v9a9(0xa0), v9a7(0x1)
    0x9ac: v9ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9ab(0x10000000000000000000000000000000000000000), v9a5(0x1)
    0x9ae: v9ae = CALLDATALOAD v991(0x4)
    0x9b0: v9b0 = AND v9ac(0xffffffffffffffffffffffffffffffffffffffff), v9ae
    0x9b2: v9b2(0x20) = CONST 
    0x9b4: v9b4(0x24) = ADD v9b2(0x20), v991(0x4)
    0x9b5: v9b5 = CALLDATALOAD v9b4(0x24)
    0x9b6: v9b6 = AND v9b5, v9ac(0xffffffffffffffffffffffffffffffffffffffff)
    0x9b7: v9b7(0x1068) = CONST 
    0x9ba: JUMP v9b7(0x1068)

    Begin block 0x10680x980
    prev=[0x9a3], succ=[0x120f0x980]
    =================================
    0x10690x980: v9801069(0x0) = CONST 
    0x106b0x980: v980106b(0x1a78) = CONST 
    0x106e0x980: v980106e(0x120f) = CONST 
    0x10710x980: JUMP v980106e(0x120f)

    Begin block 0x120f0x980
    prev=[0x10680x980], succ=[0x12910x980]
    =================================
    0x12100x980: v9801210(0x60) = CONST 
    0x12120x980: v9801212(0x0) = CONST 
    0x12140x980: v9801214 = ADDRESS 
    0x12150x980: v9801215(0x1) = CONST 
    0x12170x980: v9801217(0x1) = CONST 
    0x12190x980: v9801219(0xa0) = CONST 
    0x121b0x980: v980121b(0x10000000000000000000000000000000000000000) = SHL v9801219(0xa0), v9801217(0x1)
    0x121c0x980: v980121c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v980121b(0x10000000000000000000000000000000000000000), v9801215(0x1)
    0x121d0x980: v980121d = AND v980121c(0xffffffffffffffffffffffffffffffffffffffff), v9801214
    0x121e0x980: v980121e(0x0) = CONST 
    0x12200x980: v9801220 = CALLDATASIZE 
    0x12210x980: v9801221(0x40) = CONST 
    0x12230x980: v9801223 = MLOAD v9801221(0x40)
    0x12240x980: v9801224(0x24) = CONST 
    0x12260x980: v9801226 = ADD v9801224(0x24), v9801223
    0x12290x980: v9801229(0x20) = CONST 
    0x122b0x980: v980122b = ADD v9801229(0x20), v9801226
    0x122e0x980: v980122e(0x20) = SUB v980122b, v9801226
    0x12300x980: MSTORE v9801226, v980122e(0x20)
    0x12360x980: MSTORE v980122b, v9801220
    0x12370x980: v9801237(0x20) = CONST 
    0x12390x980: v9801239 = ADD v9801237(0x20), v980122b
    0x123f0x980: CALLDATACOPY v9801239, v980121e(0x0), v9801220
    0x12400x980: v9801240(0x0) = CONST 
    0x12440x980: v9801244 = ADD v9801220, v9801239
    0x12450x980: MSTORE v9801244, v9801240(0x0)
    0x12460x980: v9801246(0x40) = CONST 
    0x12490x980: v9801249 = MLOAD v9801246(0x40)
    0x124a0x980: v980124a(0x1f) = CONST 
    0x124e0x980: v980124e = ADD v9801220, v980124a(0x1f)
    0x124f0x980: v980124f(0x1f) = CONST 
    0x12510x980: v9801251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v980124f(0x1f)
    0x12540x980: v9801254 = AND v9801251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v980124e
    0x12570x980: v9801257 = ADD v9801239, v9801254
    0x125a0x980: v980125a = SUB v9801257, v9801249
    0x125d0x980: v980125d = ADD v9801251(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v980125a
    0x125f0x980: MSTORE v9801249, v980125d
    0x12620x980: MSTORE v9801246(0x40), v9801257
    0x12630x980: v9801263(0x20) = CONST 
    0x12660x980: v9801266 = ADD v9801249, v9801263(0x20)
    0x12680x980: v9801268 = MLOAD v9801266
    0x12690x980: v9801269(0x1) = CONST 
    0x126b0x980: v980126b(0x1) = CONST 
    0x126d0x980: v980126d(0xe0) = CONST 
    0x126f0x980: v980126f(0x100000000000000000000000000000000000000000000000000000000) = SHL v980126d(0xe0), v980126b(0x1)
    0x12700x980: v9801270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v980126f(0x100000000000000000000000000000000000000000000000000000000), v9801269(0x1)
    0x12710x980: v9801271 = AND v9801270(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v9801268
    0x12720x980: v9801272(0x933c1ed) = CONST 
    0x12770x980: v9801277(0xe0) = CONST 
    0x12790x980: v9801279(0x933c1ed00000000000000000000000000000000000000000000000000000000) = SHL v9801277(0xe0), v9801272(0x933c1ed)
    0x127a0x980: v980127a = OR v9801279(0x933c1ed00000000000000000000000000000000000000000000000000000000), v9801271
    0x127c0x980: MSTORE v9801266, v980127a
    0x127e0x980: v980127e = MLOAD v9801246(0x40)
    0x12800x980: v9801280 = MLOAD v9801249

    Begin block 0x12910x980
    prev=[0x129a0x980, 0x120f0x980], succ=[0x12b00x980, 0x129a0x980]
    =================================
    0x12910x980_0x2: v1291980_2 = PHI v98012a3, v9801280
    0x12920x980: v9801292(0x20) = CONST 
    0x12950x980: v9801295 = LT v1291980_2, v9801292(0x20)
    0x12960x980: v9801296(0x12b0) = CONST 
    0x12990x980: JUMPI v9801296(0x12b0), v9801295

    Begin block 0x12b00x980
    prev=[0x12910x980], succ=[0x12ef0x980, 0x13100x980]
    =================================
    0x12b00x980_0x0: v12b0980_0 = PHI v98012ab, v9801266
    0x12b00x980_0x1: v12b0980_1 = PHI v98012a9, v980127e
    0x12b00x980_0x2: v12b0980_2 = PHI v98012a3, v9801280
    0x12b10x980: v98012b1(0x1) = CONST 
    0x12b40x980: v98012b4(0x20) = CONST 
    0x12b60x980: v98012b6 = SUB v98012b4(0x20), v12b0980_2
    0x12b70x980: v98012b7(0x100) = CONST 
    0x12ba0x980: v98012ba = EXP v98012b7(0x100), v98012b6
    0x12bb0x980: v98012bb = SUB v98012ba, v98012b1(0x1)
    0x12bd0x980: v98012bd = NOT v98012bb
    0x12bf0x980: v98012bf = MLOAD v12b0980_0
    0x12c00x980: v98012c0 = AND v98012bf, v98012bd
    0x12c30x980: v98012c3 = MLOAD v12b0980_1
    0x12c40x980: v98012c4 = AND v98012c3, v98012bb
    0x12c70x980: v98012c7 = OR v98012c0, v98012c4
    0x12c90x980: MSTORE v12b0980_1, v98012c7
    0x12d20x980: v98012d2 = ADD v9801280, v980127e
    0x12d60x980: v98012d6(0x0) = CONST 
    0x12d80x980: v98012d8(0x40) = CONST 
    0x12da0x980: v98012da = MLOAD v98012d8(0x40)
    0x12dd0x980: v98012dd = SUB v98012d2, v98012da
    0x12e00x980: v98012e0 = GAS 
    0x12e10x980: v98012e1 = STATICCALL v98012e0, v980121d, v98012da, v98012dd, v98012da, v98012d6(0x0)
    0x12e50x980: v98012e5 = RETURNDATASIZE 
    0x12e70x980: v98012e7(0x0) = CONST 
    0x12ea0x980: v98012ea = EQ v98012e5, v98012e7(0x0)
    0x12eb0x980: v98012eb(0x1310) = CONST 
    0x12ee0x980: JUMPI v98012eb(0x1310), v98012ea

    Begin block 0x12ef0x980
    prev=[0x12b00x980], succ=[0x13150x980]
    =================================
    0x12ef0x980: v98012ef(0x40) = CONST 
    0x12f10x980: v98012f1 = MLOAD v98012ef(0x40)
    0x12f40x980: v98012f4(0x1f) = CONST 
    0x12f60x980: v98012f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v98012f4(0x1f)
    0x12f70x980: v98012f7(0x3f) = CONST 
    0x12f90x980: v98012f9 = RETURNDATASIZE 
    0x12fa0x980: v98012fa = ADD v98012f9, v98012f7(0x3f)
    0x12fb0x980: v98012fb = AND v98012fa, v98012f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12fd0x980: v98012fd = ADD v98012f1, v98012fb
    0x12fe0x980: v98012fe(0x40) = CONST 
    0x13000x980: MSTORE v98012fe(0x40), v98012fd
    0x13010x980: v9801301 = RETURNDATASIZE 
    0x13030x980: MSTORE v98012f1, v9801301
    0x13040x980: v9801304 = RETURNDATASIZE 
    0x13050x980: v9801305(0x0) = CONST 
    0x13070x980: v9801307(0x20) = CONST 
    0x130a0x980: v980130a = ADD v98012f1, v9801307(0x20)
    0x130b0x980: RETURNDATACOPY v980130a, v9801305(0x0), v9801304
    0x130c0x980: v980130c(0x1315) = CONST 
    0x130f0x980: JUMP v980130c(0x1315)

    Begin block 0x13150x980
    prev=[0x12ef0x980, 0x13100x980], succ=[0x13290x980, 0x14790x980]
    =================================
    0x131a0x980: v980131a(0x40) = CONST 
    0x131c0x980: v980131c = MLOAD v980131a(0x40)
    0x131d0x980: v980131d = RETURNDATASIZE 
    0x131e0x980: v980131e(0x0) = CONST 
    0x13210x980: RETURNDATACOPY v980131c, v980131e(0x0), v980131d
    0x13240x980: v9801324 = ISZERO v98012e1
    0x13250x980: v9801325(0x1479) = CONST 
    0x13280x980: JUMPI v9801325(0x1479), v9801324

    Begin block 0x13290x980
    prev=[0x13150x980], succ=[]
    =================================
    0x13290x980: v9801329 = RETURNDATASIZE 
    0x132a0x980: v980132a(0x40) = CONST 
    0x132d0x980: v980132d = ADD v980131c, v980132a(0x40)
    0x132e0x980: RETURN v980132d, v9801329

    Begin block 0x14790x980
    prev=[0x13150x980], succ=[]
    =================================
    0x147a0x980: v980147a = RETURNDATASIZE 
    0x147c0x980: REVERT v980131c, v980147a

    Begin block 0x13100x980
    prev=[0x12b00x980], succ=[0x13150x980]
    =================================
    0x13110x980: v9801311(0x60) = CONST 

    Begin block 0x129a0x980
    prev=[0x12910x980], succ=[0x12910x980]
    =================================
    0x129a0x980_0x0: v129a980_0 = PHI v98012ab, v9801266
    0x129a0x980_0x1: v129a980_1 = PHI v98012a9, v980127e
    0x129a0x980_0x2: v129a980_2 = PHI v98012a3, v9801280
    0x129b0x980: v980129b = MLOAD v129a980_0
    0x129d0x980: MSTORE v129a980_1, v980129b
    0x129e0x980: v980129e(0x1f) = CONST 
    0x12a00x980: v98012a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v980129e(0x1f)
    0x12a30x980: v98012a3 = ADD v129a980_2, v98012a0(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x12a50x980: v98012a5(0x20) = CONST 
    0x12a90x980: v98012a9 = ADD v98012a5(0x20), v129a980_1
    0x12ab0x980: v98012ab = ADD v98012a5(0x20), v129a980_0
    0x12ac0x980: v98012ac(0x1291) = CONST 
    0x12af0x980: JUMP v98012ac(0x1291)

}

function DELEGATION_TYPEHASH()() public {
    Begin block 0x9bb
    prev=[], succ=[0x9c3, 0x9c7]
    =================================
    0x9bc: v9bc = CALLVALUE 
    0x9be: v9be = ISZERO v9bc
    0x9bf: v9bf(0x9c7) = CONST 
    0x9c2: JUMPI v9bf(0x9c7), v9be

    Begin block 0x9c3
    prev=[0x9bb], succ=[]
    =================================
    0x9c3: v9c3(0x0) = CONST 
    0x9c6: REVERT v9c3(0x0), v9c3(0x0)

    Begin block 0x9c7
    prev=[0x9bb], succ=[0x10f9]
    =================================
    0x9c9: v9c9(0x19a2) = CONST 
    0x9cc: v9cc(0x10f9) = CONST 
    0x9cf: JUMP v9cc(0x10f9)

    Begin block 0x10f9
    prev=[0x9c7], succ=[0x19a2]
    =================================
    0x10fa: v10fa(0x40) = CONST 
    0x10fc: v10fc = MLOAD v10fa(0x40)
    0x10fe: v10fe(0x3a) = CONST 
    0x1100: v1100(0x13db) = CONST 
    0x1104: CODECOPY v10fc, v1100(0x13db), v10fe(0x3a)
    0x1105: v1105(0x3a) = CONST 
    0x1107: v1107 = ADD v1105(0x3a), v10fc
    0x110a: v110a(0x40) = CONST 
    0x110c: v110c = MLOAD v110a(0x40)
    0x110f: v110f(0x3a) = SUB v1107, v110c
    0x1111: v1111 = SHA3 v110c, v110f(0x3a)
    0x1113: JUMP v9c9(0x19a2)

    Begin block 0x19a2
    prev=[0x10f9], succ=[]
    =================================
    0x19a3: v19a3(0x40) = CONST 
    0x19a6: v19a6 = MLOAD v19a3(0x40)
    0x19a9: MSTORE v19a6, v1111
    0x19aa: v19aa = MLOAD v19a3(0x40)
    0x19ae: v19ae(0x0) = SUB v19a6, v19aa
    0x19af: v19af(0x20) = CONST 
    0x19b1: v19b1(0x20) = ADD v19af(0x20), v19ae(0x0)
    0x19b3: RETURN v19aa, v19b1(0x20)

}

function BASE()() public {
    Begin block 0x9d0
    prev=[], succ=[0x9d8, 0x9dc]
    =================================
    0x9d1: v9d1 = CALLVALUE 
    0x9d3: v9d3 = ISZERO v9d1
    0x9d4: v9d4(0x9dc) = CONST 
    0x9d7: JUMPI v9d4(0x9dc), v9d3

    Begin block 0x9d8
    prev=[0x9d0], succ=[]
    =================================
    0x9d8: v9d8(0x0) = CONST 
    0x9db: REVERT v9d8(0x0), v9d8(0x0)

    Begin block 0x9dc
    prev=[0x9d0], succ=[0x1114]
    =================================
    0x9de: v9de(0x19d3) = CONST 
    0x9e1: v9e1(0x1114) = CONST 
    0x9e4: JUMP v9e1(0x1114)

    Begin block 0x1114
    prev=[0x9dc], succ=[0x19d3]
    =================================
    0x1115: v1115(0xde0b6b3a7640000) = CONST 
    0x111f: JUMP v9de(0x19d3)

    Begin block 0x19d3
    prev=[0x1114], succ=[]
    =================================
    0x19d4: v19d4(0x40) = CONST 
    0x19d7: v19d7 = MLOAD v19d4(0x40)
    0x19da: MSTORE v19d7, v1115(0xde0b6b3a7640000)
    0x19db: v19db = MLOAD v19d4(0x40)
    0x19df: v19df(0x0) = SUB v19d7, v19db
    0x19e0: v19e0(0x20) = CONST 
    0x19e2: v19e2(0x20) = ADD v19e0(0x20), v19df(0x0)
    0x19e4: RETURN v19db, v19e2(0x20)

}

function checkpoints(address,uint32)() public {
    Begin block 0x9e5
    prev=[], succ=[0x9ed, 0x9f1]
    =================================
    0x9e6: v9e6 = CALLVALUE 
    0x9e8: v9e8 = ISZERO v9e6
    0x9e9: v9e9(0x9f1) = CONST 
    0x9ec: JUMPI v9e9(0x9f1), v9e8

    Begin block 0x9ed
    prev=[0x9e5], succ=[]
    =================================
    0x9ed: v9ed(0x0) = CONST 
    0x9f0: REVERT v9ed(0x0), v9ed(0x0)

    Begin block 0x9f1
    prev=[0x9e5], succ=[0xa04, 0xa08]
    =================================
    0x9f3: v9f3(0xa24) = CONST 
    0x9f6: v9f6(0x4) = CONST 
    0x9f9: v9f9 = CALLDATASIZE 
    0x9fa: v9fa = SUB v9f9, v9f6(0x4)
    0x9fb: v9fb(0x40) = CONST 
    0x9fe: v9fe = LT v9fa, v9fb(0x40)
    0x9ff: v9ff = ISZERO v9fe
    0xa00: va00(0xa08) = CONST 
    0xa03: JUMPI va00(0xa08), v9ff

    Begin block 0xa04
    prev=[0x9f1], succ=[]
    =================================
    0xa04: va04(0x0) = CONST 
    0xa07: REVERT va04(0x0), va04(0x0)

    Begin block 0xa08
    prev=[0x9f1], succ=[0x1120]
    =================================
    0xa0b: va0b = CALLDATALOAD v9f6(0x4)
    0xa0c: va0c(0x1) = CONST 
    0xa0e: va0e(0x1) = CONST 
    0xa10: va10(0xa0) = CONST 
    0xa12: va12(0x10000000000000000000000000000000000000000) = SHL va10(0xa0), va0e(0x1)
    0xa13: va13(0xffffffffffffffffffffffffffffffffffffffff) = SUB va12(0x10000000000000000000000000000000000000000), va0c(0x1)
    0xa14: va14 = AND va13(0xffffffffffffffffffffffffffffffffffffffff), va0b
    0xa16: va16(0x20) = CONST 
    0xa18: va18(0x24) = ADD va16(0x20), v9f6(0x4)
    0xa19: va19 = CALLDATALOAD va18(0x24)
    0xa1a: va1a(0xffffffff) = CONST 
    0xa1f: va1f = AND va1a(0xffffffff), va19
    0xa20: va20(0x1120) = CONST 
    0xa23: JUMP va20(0x1120)

    Begin block 0x1120
    prev=[0xa08], succ=[0xa24]
    =================================
    0x1121: v1121(0x10) = CONST 
    0x1123: v1123(0x20) = CONST 
    0x1127: MSTORE v1123(0x20), v1121(0x10)
    0x1128: v1128(0x0) = CONST 
    0x112c: MSTORE v1128(0x0), va14
    0x112d: v112d(0x40) = CONST 
    0x1131: v1131 = SHA3 v1128(0x0), v112d(0x40)
    0x1134: MSTORE v1123(0x20), v1131
    0x1137: MSTORE v1128(0x0), va1f
    0x1139: v1139 = SHA3 v1128(0x0), v112d(0x40)
    0x113b: v113b = SLOAD v1139
    0x113c: v113c(0x1) = CONST 
    0x1140: v1140 = ADD v1139, v113c(0x1)
    0x1141: v1141 = SLOAD v1140
    0x1142: v1142(0xffffffff) = CONST 
    0x1149: v1149 = AND v113b, v1142(0xffffffff)
    0x114c: JUMP v9f3(0xa24)

    Begin block 0xa24
    prev=[0x1120], succ=[]
    =================================
    0xa25: va25(0x40) = CONST 
    0xa28: va28 = MLOAD va25(0x40)
    0xa29: va29(0xffffffff) = CONST 
    0xa30: va30 = AND v1149, va29(0xffffffff)
    0xa32: MSTORE va28, va30
    0xa33: va33(0x20) = CONST 
    0xa36: va36 = ADD va28, va33(0x20)
    0xa3a: MSTORE va36, v1141
    0xa3c: va3c = MLOAD va25(0x40)
    0xa40: va40(0x0) = SUB va28, va3c
    0xa41: va41(0x40) = ADD va40(0x0), va25(0x40)
    0xa43: RETURN va3c, va41(0x40)

}

function 0xacc(0xaccarg0x0) private {
    Begin block 0xacc
    prev=[], succ=[0x1a04, 0xb0b]
    =================================
    0xacd: vacd(0x1) = CONST 
    0xad0: vad0 = SLOAD vacd(0x1)
    0xad1: vad1(0x40) = CONST 
    0xad4: vad4 = MLOAD vad1(0x40)
    0xad5: vad5(0x20) = CONST 
    0xad7: vad7(0x2) = CONST 
    0xadb: vadb = AND vacd(0x1), vad0
    0xadc: vadc = ISZERO vadb
    0xadd: vadd(0x100) = CONST 
    0xae0: vae0 = MUL vadd(0x100), vadc
    0xae1: vae1(0x0) = CONST 
    0xae3: vae3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vae1(0x0)
    0xae4: vae4 = ADD vae3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vae0
    0xae7: vae7 = AND vad0, vae4
    0xaeb: vaeb = DIV vae7, vad7(0x2)
    0xaec: vaec(0x1f) = CONST 
    0xaef: vaef = ADD vaeb, vaec(0x1f)
    0xaf2: vaf2 = DIV vaef, vad5(0x20)
    0xaf4: vaf4 = MUL vad5(0x20), vaf2
    0xaf6: vaf6 = ADD vad4, vaf4
    0xaf8: vaf8 = ADD vad5(0x20), vaf6
    0xafb: MSTORE vad1(0x40), vaf8
    0xafe: MSTORE vad4, vaeb
    0xb02: vb02 = ADD vad4, vad5(0x20)
    0xb06: vb06 = ISZERO vaeb
    0xb07: vb07(0x1a04) = CONST 
    0xb0a: JUMPI vb07(0x1a04), vb06

    Begin block 0x1a04
    prev=[0xacc], succ=[]
    =================================
    0x1a0b: RETURNPRIVATE vaccarg0, vad4, vaccarg0

    Begin block 0xb0b
    prev=[0xacc], succ=[0xb13, 0xb260xacc]
    =================================
    0xb0c: vb0c(0x1f) = CONST 
    0xb0e: vb0e = LT vb0c(0x1f), vaeb
    0xb0f: vb0f(0xb26) = CONST 
    0xb12: JUMPI vb0f(0xb26), vb0e

    Begin block 0xb13
    prev=[0xb0b], succ=[0x1a2b]
    =================================
    0xb13: vb13(0x100) = CONST 
    0xb18: vb18 = SLOAD vacd(0x1)
    0xb19: vb19 = DIV vb18, vb13(0x100)
    0xb1a: vb1a = MUL vb19, vb13(0x100)
    0xb1c: MSTORE vb02, vb1a
    0xb1e: vb1e(0x20) = CONST 
    0xb20: vb20 = ADD vb1e(0x20), vb02
    0xb22: vb22(0x1a2b) = CONST 
    0xb25: JUMP vb22(0x1a2b)

    Begin block 0x1a2b
    prev=[0xb13], succ=[]
    =================================
    0x1a32: RETURNPRIVATE vaccarg0, vad4, vaccarg0

    Begin block 0xb260xacc
    prev=[0xb0b], succ=[0xb340xacc]
    =================================
    0xb280xacc: vaccb28 = ADD vb02, vaeb
    0xb2b0xacc: vaccb2b(0x0) = CONST 
    0xb2d0xacc: MSTORE vaccb2b(0x0), vacd(0x1)
    0xb2e0xacc: vaccb2e(0x20) = CONST 
    0xb300xacc: vaccb30(0x0) = CONST 
    0xb320xacc: vaccb32 = SHA3 vaccb30(0x0), vaccb2e(0x20)

    Begin block 0xb340xacc
    prev=[0xb340xacc, 0xb260xacc], succ=[0xb340xacc, 0xb480xacc]
    =================================
    0xb340xacc_0x0: vb34acc_0 = PHI vb02, vaccb40
    0xb340xacc_0x1: vb34acc_1 = PHI vaccb3c, vaccb32
    0xb360xacc: vaccb36 = SLOAD vb34acc_1
    0xb380xacc: MSTORE vb34acc_0, vaccb36
    0xb3a0xacc: vaccb3a(0x1) = CONST 
    0xb3c0xacc: vaccb3c = ADD vaccb3a(0x1), vb34acc_1
    0xb3e0xacc: vaccb3e(0x20) = CONST 
    0xb400xacc: vaccb40 = ADD vaccb3e(0x20), vb34acc_0
    0xb430xacc: vaccb43 = GT vaccb28, vaccb40
    0xb440xacc: vaccb44(0xb34) = CONST 
    0xb470xacc: JUMPI vaccb44(0xb34), vaccb43

    Begin block 0xb480xacc
    prev=[0xb340xacc], succ=[0xb510xacc]
    =================================
    0xb4a0xacc: vaccb4a = SUB vaccb40, vaccb28
    0xb4b0xacc: vaccb4b(0x1f) = CONST 
    0xb4d0xacc: vaccb4d = AND vaccb4b(0x1f), vaccb4a
    0xb4f0xacc: vaccb4f = ADD vaccb28, vaccb4d

    Begin block 0xb510xacc
    prev=[0xb480xacc], succ=[]
    =================================
    0xb580xacc: RETURNPRIVATE vaccarg0, vad4, vaccarg0

}

