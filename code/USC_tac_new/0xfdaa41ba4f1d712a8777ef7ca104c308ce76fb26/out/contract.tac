function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2e5c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x2d6f: v2d6f(0x2e5c) = CONST 
    0x2d70: JUMPI v2d6f(0x2e5c), v8

    Begin block 0xd
    prev=[0x0], succ=[0x10d, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x8da5cb5b) = CONST 
    0x19: v19 = GT v14(0x8da5cb5b), v12
    0x1a: v1a(0x10d) = CONST 
    0x1d: JUMPI v1a(0x10d), v19

    Begin block 0x10d
    prev=[0xd], succ=[0x190, 0x119]
    =================================
    0x10f: v10f(0x5c60da1b) = CONST 
    0x114: v114 = GT v10f(0x5c60da1b), v12
    0x115: v115(0x190) = CONST 
    0x118: JUMPI v115(0x190), v114

    Begin block 0x190
    prev=[0x10d], succ=[0x1cc, 0x19c]
    =================================
    0x192: v192(0x30841768) = CONST 
    0x197: v197 = GT v192(0x30841768), v12
    0x198: v198(0x1cc) = CONST 
    0x19b: JUMPI v198(0x1cc), v197

    Begin block 0x1cc
    prev=[0x190], succ=[0x2db5, 0x1d8]
    =================================
    0x1ce: v1ce(0x22c00572) = CONST 
    0x1d3: v1d3 = EQ v1ce(0x22c00572), v12
    0x2dad: v2dad(0x2db5) = CONST 
    0x2dae: JUMPI v2dad(0x2db5), v1d3

    Begin block 0x2db5
    prev=[0x1cc], succ=[]
    =================================
    0x2db6: v2db6(0x1fe) = CONST 
    0x2db7: CALLPRIVATE v2db6(0x1fe)

    Begin block 0x1d8
    prev=[0x1cc], succ=[0x2db8, 0x1e3]
    =================================
    0x1d9: v1d9(0x2a869150) = CONST 
    0x1de: v1de = EQ v1d9(0x2a869150), v12
    0x2daf: v2daf(0x2db8) = CONST 
    0x2db0: JUMPI v2daf(0x2db8), v1de

    Begin block 0x2db8
    prev=[0x1d8], succ=[]
    =================================
    0x2db9: v2db9(0x23f) = CONST 
    0x2dba: CALLPRIVATE v2db9(0x23f)

    Begin block 0x1e3
    prev=[0x1d8], succ=[0x2dbb, 0x1ee]
    =================================
    0x1e4: v1e4(0x2ae97ebf) = CONST 
    0x1e9: v1e9 = EQ v1e4(0x2ae97ebf), v12
    0x2db1: v2db1(0x2dbb) = CONST 
    0x2db2: JUMPI v2db1(0x2dbb), v1e9

    Begin block 0x2dbb
    prev=[0x1e3], succ=[]
    =================================
    0x2dbc: v2dbc(0x28b) = CONST 
    0x2dbd: CALLPRIVATE v2dbc(0x28b)

    Begin block 0x1ee
    prev=[0x1e3], succ=[0x2dbe, 0x1f9]
    =================================
    0x1ef: v1ef(0x2b24cbd2) = CONST 
    0x1f4: v1f4 = EQ v1ef(0x2b24cbd2), v12
    0x2db3: v2db3(0x2dbe) = CONST 
    0x2db4: JUMPI v2db3(0x2dbe), v1f4

    Begin block 0x2dbe
    prev=[0x1ee], succ=[]
    =================================
    0x2dbf: v2dbf(0x354) = CONST 
    0x2dc0: CALLPRIVATE v2dbf(0x354)

    Begin block 0x1f9
    prev=[0x1ee], succ=[]
    =================================
    0x1fa: v1fa(0x0) = CONST 
    0x1fd: REVERT v1fa(0x0), v1fa(0x0)

    Begin block 0x19c
    prev=[0x190], succ=[0x2dc1, 0x1a7]
    =================================
    0x19d: v19d(0x30841768) = CONST 
    0x1a2: v1a2 = EQ v19d(0x30841768), v12
    0x2da5: v2da5(0x2dc1) = CONST 
    0x2da6: JUMPI v2da5(0x2dc1), v1a2

    Begin block 0x2dc1
    prev=[0x19c], succ=[]
    =================================
    0x2dc2: v2dc2(0x399) = CONST 
    0x2dc3: CALLPRIVATE v2dc2(0x399)

    Begin block 0x1a7
    prev=[0x19c], succ=[0x2dc4, 0x1b2]
    =================================
    0x1a8: v1a8(0x3f4ba83a) = CONST 
    0x1ad: v1ad = EQ v1a8(0x3f4ba83a), v12
    0x2da7: v2da7(0x2dc4) = CONST 
    0x2da8: JUMPI v2da7(0x2dc4), v1ad

    Begin block 0x2dc4
    prev=[0x1a7], succ=[]
    =================================
    0x2dc5: v2dc5(0x46b) = CONST 
    0x2dc6: CALLPRIVATE v2dc5(0x46b)

    Begin block 0x1b2
    prev=[0x1a7], succ=[0x2dc7, 0x1bd]
    =================================
    0x1b3: v1b3(0x4d0a32db) = CONST 
    0x1b8: v1b8 = EQ v1b3(0x4d0a32db), v12
    0x2da9: v2da9(0x2dc7) = CONST 
    0x2daa: JUMPI v2da9(0x2dc7), v1b8

    Begin block 0x2dc7
    prev=[0x1b2], succ=[]
    =================================
    0x2dc8: v2dc8(0x480) = CONST 
    0x2dc9: CALLPRIVATE v2dc8(0x480)

    Begin block 0x1bd
    prev=[0x1b2], succ=[0x1c8, 0x2dca]
    =================================
    0x1be: v1be(0x56839e0c) = CONST 
    0x1c3: v1c3 = EQ v1be(0x56839e0c), v12
    0x2dab: v2dab(0x2dca) = CONST 
    0x2dac: JUMPI v2dab(0x2dca), v1c3

    Begin block 0x1c8
    prev=[0x1bd], succ=[0x26bf]
    =================================
    0x1c8: v1c8(0x26bf) = CONST 
    0x1cb: JUMP v1c8(0x26bf)

    Begin block 0x26bf
    prev=[0x1c8], succ=[]
    =================================
    0x26c0: v26c0(0x0) = CONST 
    0x26c3: REVERT v26c0(0x0), v26c0(0x0)

    Begin block 0x2dca
    prev=[0x1bd], succ=[]
    =================================
    0x2dcb: v2dcb(0x4b3) = CONST 
    0x2dcc: CALLPRIVATE v2dcb(0x4b3)

    Begin block 0x119
    prev=[0x10d], succ=[0x15f, 0x124]
    =================================
    0x11a: v11a(0x715018a6) = CONST 
    0x11f: v11f = GT v11a(0x715018a6), v12
    0x120: v120(0x15f) = CONST 
    0x123: JUMPI v120(0x15f), v11f

    Begin block 0x15f
    prev=[0x119], succ=[0x2dcd, 0x16b]
    =================================
    0x161: v161(0x5c60da1b) = CONST 
    0x166: v166 = EQ v161(0x5c60da1b), v12
    0x2d9d: v2d9d(0x2dcd) = CONST 
    0x2d9e: JUMPI v2d9d(0x2dcd), v166

    Begin block 0x2dcd
    prev=[0x15f], succ=[]
    =================================
    0x2dce: v2dce(0x4e8) = CONST 
    0x2dcf: CALLPRIVATE v2dce(0x4e8)

    Begin block 0x16b
    prev=[0x15f], succ=[0x2dd0, 0x176]
    =================================
    0x16c: v16c(0x5c975abb) = CONST 
    0x171: v171 = EQ v16c(0x5c975abb), v12
    0x2d9f: v2d9f(0x2dd0) = CONST 
    0x2da0: JUMPI v2d9f(0x2dd0), v171

    Begin block 0x2dd0
    prev=[0x16b], succ=[]
    =================================
    0x2dd1: v2dd1(0x4fd) = CONST 
    0x2dd2: CALLPRIVATE v2dd1(0x4fd)

    Begin block 0x176
    prev=[0x16b], succ=[0x2dd3, 0x181]
    =================================
    0x177: v177(0x60f0a5ac) = CONST 
    0x17c: v17c = EQ v177(0x60f0a5ac), v12
    0x2da1: v2da1(0x2dd3) = CONST 
    0x2da2: JUMPI v2da1(0x2dd3), v17c

    Begin block 0x2dd3
    prev=[0x176], succ=[]
    =================================
    0x2dd4: v2dd4(0x512) = CONST 
    0x2dd5: CALLPRIVATE v2dd4(0x512)

    Begin block 0x181
    prev=[0x176], succ=[0x18c, 0x2dd6]
    =================================
    0x182: v182(0x693c1987) = CONST 
    0x187: v187 = EQ v182(0x693c1987), v12
    0x2da3: v2da3(0x2dd6) = CONST 
    0x2da4: JUMPI v2da3(0x2dd6), v187

    Begin block 0x18c
    prev=[0x181], succ=[0x269b]
    =================================
    0x18c: v18c(0x269b) = CONST 
    0x18f: JUMP v18c(0x269b)

    Begin block 0x269b
    prev=[0x18c], succ=[]
    =================================
    0x269c: v269c(0x0) = CONST 
    0x269f: REVERT v269c(0x0), v269c(0x0)

    Begin block 0x2dd6
    prev=[0x181], succ=[]
    =================================
    0x2dd7: v2dd7(0x545) = CONST 
    0x2dd8: CALLPRIVATE v2dd7(0x545)

    Begin block 0x124
    prev=[0x119], succ=[0x2dd9, 0x12f]
    =================================
    0x125: v125(0x715018a6) = CONST 
    0x12a: v12a = EQ v125(0x715018a6), v12
    0x2d93: v2d93(0x2dd9) = CONST 
    0x2d94: JUMPI v2d93(0x2dd9), v12a

    Begin block 0x2dd9
    prev=[0x124], succ=[]
    =================================
    0x2dda: v2dda(0x580) = CONST 
    0x2ddb: CALLPRIVATE v2dda(0x580)

    Begin block 0x12f
    prev=[0x124], succ=[0x2ddc, 0x13a]
    =================================
    0x130: v130(0x77624f7a) = CONST 
    0x135: v135 = EQ v130(0x77624f7a), v12
    0x2d95: v2d95(0x2ddc) = CONST 
    0x2d96: JUMPI v2d95(0x2ddc), v135

    Begin block 0x2ddc
    prev=[0x12f], succ=[]
    =================================
    0x2ddd: v2ddd(0x595) = CONST 
    0x2dde: CALLPRIVATE v2ddd(0x595)

    Begin block 0x13a
    prev=[0x12f], succ=[0x2ddf, 0x145]
    =================================
    0x13b: v13b(0x8456cb59) = CONST 
    0x140: v140 = EQ v13b(0x8456cb59), v12
    0x2d97: v2d97(0x2ddf) = CONST 
    0x2d98: JUMPI v2d97(0x2ddf), v140

    Begin block 0x2ddf
    prev=[0x13a], succ=[]
    =================================
    0x2de0: v2de0(0x5ce) = CONST 
    0x2de1: CALLPRIVATE v2de0(0x5ce)

    Begin block 0x145
    prev=[0x13a], succ=[0x2de2, 0x150]
    =================================
    0x146: v146(0x8c6aa3f5) = CONST 
    0x14b: v14b = EQ v146(0x8c6aa3f5), v12
    0x2d99: v2d99(0x2de2) = CONST 
    0x2d9a: JUMPI v2d99(0x2de2), v14b

    Begin block 0x2de2
    prev=[0x145], succ=[]
    =================================
    0x2de3: v2de3(0x5e3) = CONST 
    0x2de4: CALLPRIVATE v2de3(0x5e3)

    Begin block 0x150
    prev=[0x145], succ=[0x15b, 0x2de5]
    =================================
    0x151: v151(0x8cd3f064) = CONST 
    0x156: v156 = EQ v151(0x8cd3f064), v12
    0x2d9b: v2d9b(0x2de5) = CONST 
    0x2d9c: JUMPI v2d9b(0x2de5), v156

    Begin block 0x15b
    prev=[0x150], succ=[0x2677]
    =================================
    0x15b: v15b(0x2677) = CONST 
    0x15e: JUMP v15b(0x2677)

    Begin block 0x2677
    prev=[0x15b], succ=[]
    =================================
    0x2678: v2678(0x0) = CONST 
    0x267b: REVERT v2678(0x0), v2678(0x0)

    Begin block 0x2de5
    prev=[0x150], succ=[]
    =================================
    0x2de6: v2de6(0x616) = CONST 
    0x2de7: CALLPRIVATE v2de6(0x616)

    Begin block 0x1e
    prev=[0xd], succ=[0xa0, 0x29]
    =================================
    0x1f: v1f(0xe3f5ce35) = CONST 
    0x24: v24 = GT v1f(0xe3f5ce35), v12
    0x25: v25(0xa0) = CONST 
    0x28: JUMPI v25(0xa0), v24

    Begin block 0xa0
    prev=[0x1e], succ=[0xdc, 0xac]
    =================================
    0xa2: va2(0xb80777ea) = CONST 
    0xa7: va7 = GT va2(0xb80777ea), v12
    0xa8: va8(0xdc) = CONST 
    0xab: JUMPI va8(0xdc), va7

    Begin block 0xdc
    prev=[0xa0], succ=[0x2de8, 0xe8]
    =================================
    0xde: vde(0x8da5cb5b) = CONST 
    0xe3: ve3 = EQ vde(0x8da5cb5b), v12
    0x2d8b: v2d8b(0x2de8) = CONST 
    0x2d8c: JUMPI v2d8b(0x2de8), ve3

    Begin block 0x2de8
    prev=[0xdc], succ=[]
    =================================
    0x2de9: v2de9(0x649) = CONST 
    0x2dea: CALLPRIVATE v2de9(0x649)

    Begin block 0xe8
    prev=[0xdc], succ=[0x2deb, 0xf3]
    =================================
    0xe9: ve9(0x94dee0a4) = CONST 
    0xee: vee = EQ ve9(0x94dee0a4), v12
    0x2d8d: v2d8d(0x2deb) = CONST 
    0x2d8e: JUMPI v2d8d(0x2deb), vee

    Begin block 0x2deb
    prev=[0xe8], succ=[]
    =================================
    0x2dec: v2dec(0x65e) = CONST 
    0x2ded: CALLPRIVATE v2dec(0x65e)

    Begin block 0xf3
    prev=[0xe8], succ=[0x2dee, 0xfe]
    =================================
    0xf4: vf4(0xa5b00ee3) = CONST 
    0xf9: vf9 = EQ vf4(0xa5b00ee3), v12
    0x2d8f: v2d8f(0x2dee) = CONST 
    0x2d90: JUMPI v2d8f(0x2dee), vf9

    Begin block 0x2dee
    prev=[0xf3], succ=[]
    =================================
    0x2def: v2def(0x691) = CONST 
    0x2df0: CALLPRIVATE v2def(0x691)

    Begin block 0xfe
    prev=[0xf3], succ=[0x109, 0x2df1]
    =================================
    0xff: vff(0xb7760c8f) = CONST 
    0x104: v104 = EQ vff(0xb7760c8f), v12
    0x2d91: v2d91(0x2df1) = CONST 
    0x2d92: JUMPI v2d91(0x2df1), v104

    Begin block 0x109
    prev=[0xfe], succ=[0x2653]
    =================================
    0x109: v109(0x2653) = CONST 
    0x10c: JUMP v109(0x2653)

    Begin block 0x2653
    prev=[0x109], succ=[]
    =================================
    0x2654: v2654(0x0) = CONST 
    0x2657: REVERT v2654(0x0), v2654(0x0)

    Begin block 0x2df1
    prev=[0xfe], succ=[]
    =================================
    0x2df2: v2df2(0x6bb) = CONST 
    0x2df3: CALLPRIVATE v2df2(0x6bb)

    Begin block 0xac
    prev=[0xa0], succ=[0x2df4, 0xb7]
    =================================
    0xad: vad(0xb80777ea) = CONST 
    0xb2: vb2 = EQ vad(0xb80777ea), v12
    0x2d83: v2d83(0x2df4) = CONST 
    0x2d84: JUMPI v2d83(0x2df4), vb2

    Begin block 0x2df4
    prev=[0xac], succ=[]
    =================================
    0x2df5: v2df5(0x6f4) = CONST 
    0x2df6: CALLPRIVATE v2df5(0x6f4)

    Begin block 0xb7
    prev=[0xac], succ=[0x2df7, 0xc2]
    =================================
    0xb8: vb8(0xc9b5ef8e) = CONST 
    0xbd: vbd = EQ vb8(0xc9b5ef8e), v12
    0x2d85: v2d85(0x2df7) = CONST 
    0x2d86: JUMPI v2d85(0x2df7), vbd

    Begin block 0x2df7
    prev=[0xb7], succ=[]
    =================================
    0x2df8: v2df8(0x709) = CONST 
    0x2df9: CALLPRIVATE v2df8(0x709)

    Begin block 0xc2
    prev=[0xb7], succ=[0x2dfa, 0xcd]
    =================================
    0xc3: vc3(0xd5708d5a) = CONST 
    0xc8: vc8 = EQ vc3(0xd5708d5a), v12
    0x2d87: v2d87(0x2dfa) = CONST 
    0x2d88: JUMPI v2d87(0x2dfa), vc8

    Begin block 0x2dfa
    prev=[0xc2], succ=[]
    =================================
    0x2dfb: v2dfb(0x73c) = CONST 
    0x2dfc: CALLPRIVATE v2dfb(0x73c)

    Begin block 0xcd
    prev=[0xc2], succ=[0xd8, 0x2dfd]
    =================================
    0xce: vce(0xdd39f00d) = CONST 
    0xd3: vd3 = EQ vce(0xdd39f00d), v12
    0x2d89: v2d89(0x2dfd) = CONST 
    0x2d8a: JUMPI v2d89(0x2dfd), vd3

    Begin block 0xd8
    prev=[0xcd], succ=[0x262f]
    =================================
    0xd8: vd8(0x262f) = CONST 
    0xdb: JUMP vd8(0x262f)

    Begin block 0x262f
    prev=[0xd8], succ=[]
    =================================
    0x2630: v2630(0x0) = CONST 
    0x2633: REVERT v2630(0x0), v2630(0x0)

    Begin block 0x2dfd
    prev=[0xcd], succ=[]
    =================================
    0x2dfe: v2dfe(0x775) = CONST 
    0x2dff: CALLPRIVATE v2dfe(0x775)

    Begin block 0x29
    prev=[0x1e], succ=[0x6f, 0x34]
    =================================
    0x2a: v2a(0xf2fde38b) = CONST 
    0x2f: v2f = GT v2a(0xf2fde38b), v12
    0x30: v30(0x6f) = CONST 
    0x33: JUMPI v30(0x6f), v2f

    Begin block 0x6f
    prev=[0x29], succ=[0x7b, 0x2e00]
    =================================
    0x71: v71(0xe3f5ce35) = CONST 
    0x76: v76 = EQ v71(0xe3f5ce35), v12
    0x2d7b: v2d7b(0x2e00) = CONST 
    0x2d7c: JUMPI v2d7b(0x2e00), v76

    Begin block 0x7b
    prev=[0x6f], succ=[0x2e03, 0x86]
    =================================
    0x7c: v7c(0xe7e6fb89) = CONST 
    0x81: v81 = EQ v7c(0xe7e6fb89), v12
    0x2d7d: v2d7d(0x2e03) = CONST 
    0x2d7e: JUMPI v2d7d(0x2e03), v81

    Begin block 0x2e03
    prev=[0x7b], succ=[]
    =================================
    0x2e04: v2e04(0x7e6) = CONST 
    0x2e05: CALLPRIVATE v2e04(0x7e6)

    Begin block 0x86
    prev=[0x7b], succ=[0x2e06, 0x91]
    =================================
    0x87: v87(0xebced90c) = CONST 
    0x8c: v8c = EQ v87(0xebced90c), v12
    0x2d7f: v2d7f(0x2e06) = CONST 
    0x2d80: JUMPI v2d7f(0x2e06), v8c

    Begin block 0x2e06
    prev=[0x86], succ=[]
    =================================
    0x2e07: v2e07(0x819) = CONST 
    0x2e08: CALLPRIVATE v2e07(0x819)

    Begin block 0x91
    prev=[0x86], succ=[0x9c, 0x2e09]
    =================================
    0x92: v92(0xefbddf66) = CONST 
    0x97: v97 = EQ v92(0xefbddf66), v12
    0x2d81: v2d81(0x2e09) = CONST 
    0x2d82: JUMPI v2d81(0x2e09), v97

    Begin block 0x9c
    prev=[0x91], succ=[0x260b]
    =================================
    0x9c: v9c(0x260b) = CONST 
    0x9f: JUMP v9c(0x260b)

    Begin block 0x260b
    prev=[0x9c], succ=[]
    =================================
    0x260c: v260c(0x0) = CONST 
    0x260f: REVERT v260c(0x0), v260c(0x0)

    Begin block 0x2e09
    prev=[0x91], succ=[]
    =================================
    0x2e0a: v2e0a(0x84c) = CONST 
    0x2e0b: CALLPRIVATE v2e0a(0x84c)

    Begin block 0x2e00
    prev=[0x6f], succ=[]
    =================================
    0x2e01: v2e01(0x7a8) = CONST 
    0x2e02: CALLPRIVATE v2e01(0x7a8)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x2e0c]
    =================================
    0x35: v35(0xf2fde38b) = CONST 
    0x3a: v3a = EQ v35(0xf2fde38b), v12
    0x2d71: v2d71(0x2e0c) = CONST 
    0x2d72: JUMPI v2d71(0x2e0c), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x2e0f, 0x4a]
    =================================
    0x40: v40(0xf640d508) = CONST 
    0x45: v45 = EQ v40(0xf640d508), v12
    0x2d73: v2d73(0x2e0f) = CONST 
    0x2d74: JUMPI v2d73(0x2e0f), v45

    Begin block 0x2e0f
    prev=[0x3f], succ=[]
    =================================
    0x2e10: v2e10(0x8ac) = CONST 
    0x2e11: CALLPRIVATE v2e10(0x8ac)

    Begin block 0x4a
    prev=[0x3f], succ=[0x2e12, 0x55]
    =================================
    0x4b: v4b(0xf851a440) = CONST 
    0x50: v50 = EQ v4b(0xf851a440), v12
    0x2d75: v2d75(0x2e12) = CONST 
    0x2d76: JUMPI v2d75(0x2e12), v50

    Begin block 0x2e12
    prev=[0x4a], succ=[]
    =================================
    0x2e13: v2e13(0x8ef) = CONST 
    0x2e14: CALLPRIVATE v2e13(0x8ef)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0x2e15]
    =================================
    0x56: v56(0xfb52b065) = CONST 
    0x5b: v5b = EQ v56(0xfb52b065), v12
    0x2d77: v2d77(0x2e15) = CONST 
    0x2d78: JUMPI v2d77(0x2e15), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x6b, 0x2e18]
    =================================
    0x61: v61(0xfc5bfe68) = CONST 
    0x66: v66 = EQ v61(0xfc5bfe68), v12
    0x2d79: v2d79(0x2e18) = CONST 
    0x2d7a: JUMPI v2d79(0x2e18), v66

    Begin block 0x6b
    prev=[0x60], succ=[0x25e7]
    =================================
    0x6b: v6b(0x25e7) = CONST 
    0x6e: JUMP v6b(0x25e7)

    Begin block 0x25e7
    prev=[0x6b], succ=[]
    =================================
    0x25e8: v25e8(0x0) = CONST 
    0x25eb: REVERT v25e8(0x0), v25e8(0x0)

    Begin block 0x2e18
    prev=[0x60], succ=[]
    =================================
    0x2e19: v2e19(0x93d) = CONST 
    0x2e1a: CALLPRIVATE v2e19(0x93d)

    Begin block 0x2e15
    prev=[0x55], succ=[]
    =================================
    0x2e16: v2e16(0x904) = CONST 
    0x2e17: CALLPRIVATE v2e16(0x904)

    Begin block 0x2e0c
    prev=[0x34], succ=[]
    =================================
    0x2e0d: v2e0d(0x879) = CONST 
    0x2e0e: CALLPRIVATE v2e0d(0x879)

    Begin block 0x2e5c
    prev=[0x0], succ=[]
    =================================
    0x2e5d: v2e5d(0x25c3) = CONST 
    0x2e5e: CALLPRIVATE v2e5d(0x25c3)

}

function acceptChain(uint8)() public {
    Begin block 0x1fe
    prev=[], succ=[0x206, 0x20a]
    =================================
    0x1ff: v1ff = CALLVALUE 
    0x201: v201 = ISZERO v1ff
    0x202: v202(0x20a) = CONST 
    0x205: JUMPI v202(0x20a), v201

    Begin block 0x206
    prev=[0x1fe], succ=[]
    =================================
    0x206: v206(0x0) = CONST 
    0x209: REVERT v206(0x0), v206(0x0)

    Begin block 0x20a
    prev=[0x1fe], succ=[0x21d, 0x221]
    =================================
    0x20c: v20c(0x26e3) = CONST 
    0x20f: v20f(0x4) = CONST 
    0x212: v212 = CALLDATASIZE 
    0x213: v213 = SUB v212, v20f(0x4)
    0x214: v214(0x20) = CONST 
    0x217: v217 = LT v213, v214(0x20)
    0x218: v218 = ISZERO v217
    0x219: v219(0x221) = CONST 
    0x21c: JUMPI v219(0x221), v218

    Begin block 0x21d
    prev=[0x20a], succ=[]
    =================================
    0x21d: v21d(0x0) = CONST 
    0x220: REVERT v21d(0x0), v21d(0x0)

    Begin block 0x221
    prev=[0x20a], succ=[0x952]
    =================================
    0x223: v223 = CALLDATALOAD v20f(0x4)
    0x224: v224(0xff) = CONST 
    0x226: v226 = AND v224(0xff), v223
    0x227: v227(0x952) = CONST 
    0x22a: JUMP v227(0x952)

    Begin block 0x952
    prev=[0x221], succ=[0x26e3]
    =================================
    0x953: v953(0x5) = CONST 
    0x955: v955(0x20) = CONST 
    0x957: MSTORE v955(0x20), v953(0x5)
    0x958: v958(0x0) = CONST 
    0x95c: MSTORE v958(0x0), v226
    0x95d: v95d(0x40) = CONST 
    0x960: v960 = SHA3 v958(0x0), v95d(0x40)
    0x961: v961 = SLOAD v960
    0x962: v962(0xff) = CONST 
    0x964: v964 = AND v962(0xff), v961
    0x966: JUMP v20c(0x26e3)

    Begin block 0x26e3
    prev=[0x952], succ=[]
    =================================
    0x26e4: v26e4(0x40) = CONST 
    0x26e7: v26e7 = MLOAD v26e4(0x40)
    0x26e9: v26e9 = ISZERO v964
    0x26ea: v26ea = ISZERO v26e9
    0x26ec: MSTORE v26e7, v26ea
    0x26ed: v26ed = MLOAD v26e4(0x40)
    0x26f1: v26f1(0x0) = SUB v26e7, v26ed
    0x26f2: v26f2(0x20) = CONST 
    0x26f4: v26f4(0x20) = ADD v26f2(0x20), v26f1(0x0)
    0x26f6: RETURN v26ed, v26f4(0x20)

}

function 0x2179(0x2179arg0x0, 0x2179arg0x1) private {
    Begin block 0x2179
    prev=[], succ=[0x21a7, 0x21a8]
    =================================
    0x217a: v217a(0x0) = CONST 
    0x217c: v217c(0x273a84b195de37e06c2a1019a0091cbd72c904c5b8b1711fb97f8774b3afb4f6) = CONST 
    0x219e: v219e(0x2) = CONST 
    0x21a1: v21a1 = GT v2179arg0, v219e(0x2)
    0x21a2: v21a2 = ISZERO v21a1
    0x21a3: v21a3(0x21a8) = CONST 
    0x21a6: JUMPI v21a3(0x21a8), v21a2

    Begin block 0x21a7
    prev=[0x2179], succ=[]
    =================================
    0x21a7: THROW 

    Begin block 0x21a8
    prev=[0x2179], succ=[0x21c4, 0x2cd3]
    =================================
    0x21a9: v21a9(0x40) = CONST 
    0x21ac: v21ac = MLOAD v21a9(0x40)
    0x21af: MSTORE v21ac, v2179arg0
    0x21b0: v21b0 = MLOAD v21a9(0x40)
    0x21b4: v21b4(0x0) = SUB v21ac, v21b0
    0x21b5: v21b5(0x20) = CONST 
    0x21b7: v21b7(0x20) = ADD v21b5(0x20), v21b4(0x0)
    0x21b9: LOG1 v21b0, v21b7(0x20), v217c(0x273a84b195de37e06c2a1019a0091cbd72c904c5b8b1711fb97f8774b3afb4f6)
    0x21bb: v21bb(0x2) = CONST 
    0x21be: v21be = GT v2179arg0, v21bb(0x2)
    0x21bf: v21bf = ISZERO v21be
    0x21c0: v21c0(0x2cd3) = CONST 
    0x21c3: JUMPI v21c0(0x2cd3), v21bf

    Begin block 0x21c4
    prev=[0x21a8], succ=[]
    =================================
    0x21c4: THROW 

    Begin block 0x2cd3
    prev=[0x21a8], succ=[]
    =================================
    0x2cd8: RETURNPRIVATE v2179arg1, v2179arg0

}

function 0x21cb(0x21cbarg0x0, 0x21cbarg0x1, 0x21cbarg0x2, 0x21cbarg0x3) private {
    Begin block 0x21cb
    prev=[], succ=[0x2346B0x21cb]
    =================================
    0x21cc: v21cc(0x0) = CONST 
    0x21cf: v21cf(0x21e6) = CONST 
    0x21d2: v21d2(0x15180) = CONST 
    0x21d6: v21d6(0xe) = CONST 
    0x21d8: v21d8 = SLOAD v21d6(0xe)
    0x21d9: v21d9(0x2346) = CONST 
    0x21df: v21df(0xffffffff) = CONST 
    0x21e4: v21e4(0x2346) = AND v21df(0xffffffff), v21d9(0x2346)
    0x21e5: JUMP v21e4(0x2346)

    Begin block 0x2346B0x21cb
    prev=[0x21cb], succ=[0x2354B0x21cb, 0x2d1dB0x21cb]
    =================================
    0x2347S0x21cb: v2347V21cb(0x0) = CONST 
    0x234bS0x21cb: v234bV21cb = ADD v21d2(0x15180), v21d8
    0x234eS0x21cb: v234eV21cb = LT v234bV21cb, v21d8
    0x234fS0x21cb: v234fV21cb = ISZERO v234eV21cb
    0x2350S0x21cb: v2350V21cb(0x2d1d) = CONST 
    0x2353S0x21cb: JUMPI v2350V21cb(0x2d1d), v234fV21cb

    Begin block 0x2354B0x21cb
    prev=[0x2346B0x21cb], succ=[]
    =================================
    0x2354S0x21cb: v2354V21cb(0x40) = CONST 
    0x2357S0x21cb: v2357V21cb = MLOAD v2354V21cb(0x40)
    0x2358S0x21cb: v2358V21cb(0x461bcd) = CONST 
    0x235cS0x21cb: v235cV21cb(0xe5) = CONST 
    0x235eS0x21cb: v235eV21cb(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v235cV21cb(0xe5), v2358V21cb(0x461bcd)
    0x2360S0x21cb: MSTORE v2357V21cb, v235eV21cb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2361S0x21cb: v2361V21cb(0x20) = CONST 
    0x2363S0x21cb: v2363V21cb(0x4) = CONST 
    0x2366S0x21cb: v2366V21cb = ADD v2357V21cb, v2363V21cb(0x4)
    0x2367S0x21cb: MSTORE v2366V21cb, v2361V21cb(0x20)
    0x2368S0x21cb: v2368V21cb(0x1b) = CONST 
    0x236aS0x21cb: v236aV21cb(0x24) = CONST 
    0x236dS0x21cb: v236dV21cb = ADD v2357V21cb, v236aV21cb(0x24)
    0x236eS0x21cb: MSTORE v236dV21cb, v2368V21cb(0x1b)
    0x236fS0x21cb: v236fV21cb(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2390S0x21cb: v2390V21cb(0x44) = CONST 
    0x2393S0x21cb: v2393V21cb = ADD v2357V21cb, v2390V21cb(0x44)
    0x2394S0x21cb: MSTORE v2393V21cb, v236fV21cb(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2396S0x21cb: v2396V21cb = MLOAD v2354V21cb(0x40)
    0x239aS0x21cb: v239aV21cb(0x0) = SUB v2357V21cb, v2396V21cb
    0x239bS0x21cb: v239bV21cb(0x64) = CONST 
    0x239dS0x21cb: v239dV21cb(0x64) = ADD v239bV21cb(0x64), v239aV21cb(0x0)
    0x239fS0x21cb: REVERT v2396V21cb, v239dV21cb(0x64)

    Begin block 0x2d1dB0x21cb
    prev=[0x2346B0x21cb], succ=[0x21e6]
    =================================
    0x2d23S0x21cb: JUMP v21cf(0x21e6)

    Begin block 0x21e6
    prev=[0x2d1dB0x21cb], succ=[0x21ee, 0x2237]
    =================================
    0x21e7: v21e7 = TIMESTAMP 
    0x21e8: v21e8 = GT v21e7, v234bV21cb
    0x21e9: v21e9 = ISZERO v21e8
    0x21ea: v21ea(0x2237) = CONST 
    0x21ed: JUMPI v21ea(0x2237), v21e9

    Begin block 0x21ee
    prev=[0x21e6], succ=[0x23a7]
    =================================
    0x21ee: v21ee(0x0) = CONST 
    0x21f0: v21f0(0x221e) = CONST 
    0x21f3: v21f3(0x15180) = CONST 
    0x21f7: v21f7(0x2218) = CONST 
    0x21fa: v21fa(0x15180) = CONST 
    0x21fe: v21fe(0x2212) = CONST 
    0x2201: v2201(0xe) = CONST 
    0x2203: v2203 = SLOAD v2201(0xe)
    0x2204: v2204 = TIMESTAMP 
    0x2205: v2205(0x23a7) = CONST 
    0x220b: v220b(0xffffffff) = CONST 
    0x2210: v2210(0x23a7) = AND v220b(0xffffffff), v2205(0x23a7)
    0x2211: JUMP v2210(0x23a7)

    Begin block 0x23a7
    prev=[0x21ee], succ=[0x23b2, 0x23fe]
    =================================
    0x23a8: v23a8(0x0) = CONST 
    0x23ac: v23ac = GT v2203, v2204
    0x23ad: v23ad = ISZERO v23ac
    0x23ae: v23ae(0x23fe) = CONST 
    0x23b1: JUMPI v23ae(0x23fe), v23ad

    Begin block 0x23b2
    prev=[0x23a7], succ=[]
    =================================
    0x23b2: v23b2(0x40) = CONST 
    0x23b5: v23b5 = MLOAD v23b2(0x40)
    0x23b6: v23b6(0x461bcd) = CONST 
    0x23ba: v23ba(0xe5) = CONST 
    0x23bc: v23bc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v23ba(0xe5), v23b6(0x461bcd)
    0x23be: MSTORE v23b5, v23bc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x23bf: v23bf(0x20) = CONST 
    0x23c1: v23c1(0x4) = CONST 
    0x23c4: v23c4 = ADD v23b5, v23c1(0x4)
    0x23c5: MSTORE v23c4, v23bf(0x20)
    0x23c6: v23c6(0x1e) = CONST 
    0x23c8: v23c8(0x24) = CONST 
    0x23cb: v23cb = ADD v23b5, v23c8(0x24)
    0x23cc: MSTORE v23cb, v23c6(0x1e)
    0x23cd: v23cd(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x23ee: v23ee(0x44) = CONST 
    0x23f1: v23f1 = ADD v23b5, v23ee(0x44)
    0x23f2: MSTORE v23f1, v23cd(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x23f4: v23f4 = MLOAD v23b2(0x40)
    0x23f8: v23f8(0x0) = SUB v23b5, v23f4
    0x23f9: v23f9(0x64) = CONST 
    0x23fb: v23fb(0x64) = ADD v23f9(0x64), v23f8(0x0)
    0x23fd: REVERT v23f4, v23fb(0x64)

    Begin block 0x23fe
    prev=[0x23a7], succ=[0x2212]
    =================================
    0x2401: v2401 = SUB v2204, v2203
    0x2403: JUMP v21fe(0x2212)

    Begin block 0x2212
    prev=[0x23fe], succ=[0x2404]
    =================================
    0x2214: v2214(0x2404) = CONST 
    0x2217: JUMP v2214(0x2404)

    Begin block 0x2404
    prev=[0x2212], succ=[0x240e, 0x245a]
    =================================
    0x2405: v2405(0x0) = CONST 
    0x2409: v2409(0x1) = GT v21fa(0x15180), v2405(0x0)
    0x240a: v240a(0x245a) = CONST 
    0x240d: JUMPI v240a(0x245a), v2409(0x1)

    Begin block 0x240e
    prev=[0x2404], succ=[]
    =================================
    0x240e: v240e(0x40) = CONST 
    0x2411: v2411 = MLOAD v240e(0x40)
    0x2412: v2412(0x461bcd) = CONST 
    0x2416: v2416(0xe5) = CONST 
    0x2418: v2418(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2416(0xe5), v2412(0x461bcd)
    0x241a: MSTORE v2411, v2418(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x241b: v241b(0x20) = CONST 
    0x241d: v241d(0x4) = CONST 
    0x2420: v2420 = ADD v2411, v241d(0x4)
    0x2421: MSTORE v2420, v241b(0x20)
    0x2422: v2422(0x1a) = CONST 
    0x2424: v2424(0x24) = CONST 
    0x2427: v2427 = ADD v2411, v2424(0x24)
    0x2428: MSTORE v2427, v2422(0x1a)
    0x2429: v2429(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x244a: v244a(0x44) = CONST 
    0x244d: v244d = ADD v2411, v244a(0x44)
    0x244e: MSTORE v244d, v2429(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x2450: v2450 = MLOAD v240e(0x40)
    0x2454: v2454(0x0) = SUB v2411, v2450
    0x2455: v2455(0x64) = CONST 
    0x2457: v2457(0x64) = ADD v2455(0x64), v2454(0x0)
    0x2459: REVERT v2450, v2457(0x64)

    Begin block 0x245a
    prev=[0x2404], succ=[0x2462, 0x2463]
    =================================
    0x245e: v245e(0x2463) = CONST 
    0x2461: JUMPI v245e(0x2463), v21fa(0x15180)

    Begin block 0x2462
    prev=[0x245a], succ=[]
    =================================
    0x2462: THROW 

    Begin block 0x2463
    prev=[0x245a], succ=[0x2218]
    =================================
    0x2464: v2464 = DIV v2401, v21fa(0x15180)
    0x246a: JUMP v21f7(0x2218)

    Begin block 0x2218
    prev=[0x2463], succ=[0x221e]
    =================================
    0x221a: v221a(0x246b) = CONST 
    0x221d: v221d_0 = CALLPRIVATE v221a(0x246b), v21f3(0x15180), v2464, v21f0(0x221e)

    Begin block 0x221e
    prev=[0x2218], succ=[0x2346B0x221e]
    =================================
    0x221f: v221f(0xe) = CONST 
    0x2221: v2221 = SLOAD v221f(0xe)
    0x2225: v2225(0x222e) = CONST 
    0x222a: v222a(0x2346) = CONST 
    0x222d: JUMP v222a(0x2346)

    Begin block 0x2346B0x221e
    prev=[0x221e], succ=[0x2354B0x221e, 0x2d1dB0x221e]
    =================================
    0x2347S0x221e: v2347V221e(0x0) = CONST 
    0x234bS0x221e: v234bV221e = ADD v221d_0, v2221
    0x234eS0x221e: v234eV221e = LT v234bV221e, v2221
    0x234fS0x221e: v234fV221e = ISZERO v234eV221e
    0x2350S0x221e: v2350V221e(0x2d1d) = CONST 
    0x2353S0x221e: JUMPI v2350V221e(0x2d1d), v234fV221e

    Begin block 0x2354B0x221e
    prev=[0x2346B0x221e], succ=[]
    =================================
    0x2354S0x221e: v2354V221e(0x40) = CONST 
    0x2357S0x221e: v2357V221e = MLOAD v2354V221e(0x40)
    0x2358S0x221e: v2358V221e(0x461bcd) = CONST 
    0x235cS0x221e: v235cV221e(0xe5) = CONST 
    0x235eS0x221e: v235eV221e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v235cV221e(0xe5), v2358V221e(0x461bcd)
    0x2360S0x221e: MSTORE v2357V221e, v235eV221e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2361S0x221e: v2361V221e(0x20) = CONST 
    0x2363S0x221e: v2363V221e(0x4) = CONST 
    0x2366S0x221e: v2366V221e = ADD v2357V221e, v2363V221e(0x4)
    0x2367S0x221e: MSTORE v2366V221e, v2361V221e(0x20)
    0x2368S0x221e: v2368V221e(0x1b) = CONST 
    0x236aS0x221e: v236aV221e(0x24) = CONST 
    0x236dS0x221e: v236dV221e = ADD v2357V221e, v236aV221e(0x24)
    0x236eS0x221e: MSTORE v236dV221e, v2368V221e(0x1b)
    0x236fS0x221e: v236fV221e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2390S0x221e: v2390V221e(0x44) = CONST 
    0x2393S0x221e: v2393V221e = ADD v2357V221e, v2390V221e(0x44)
    0x2394S0x221e: MSTORE v2393V221e, v236fV221e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2396S0x221e: v2396V221e = MLOAD v2354V221e(0x40)
    0x239aS0x221e: v239aV221e(0x0) = SUB v2357V221e, v2396V221e
    0x239bS0x221e: v239bV221e(0x64) = CONST 
    0x239dS0x221e: v239dV221e(0x64) = ADD v239bV221e(0x64), v239aV221e(0x0)
    0x239fS0x221e: REVERT v2396V221e, v239dV221e(0x64)

    Begin block 0x2d1dB0x221e
    prev=[0x2346B0x221e], succ=[0x222e]
    =================================
    0x2d23S0x221e: JUMP v2225(0x222e)

    Begin block 0x222e
    prev=[0x2d1dB0x221e], succ=[0x2237]
    =================================
    0x222f: v222f(0xe) = CONST 
    0x2231: SSTORE v222f(0xe), v234bV221e
    0x2233: v2233(0x0) = CONST 

    Begin block 0x2237
    prev=[0x21e6, 0x222e], succ=[0x2346B0x2237]
    =================================
    0x2237_0x3: v2237_3 = PHI v2233(0x0), v21cbarg1
    0x2238: v2238(0x2241) = CONST 
    0x223d: v223d(0x2346) = CONST 
    0x2240: JUMP v223d(0x2346)

    Begin block 0x2346B0x2237
    prev=[0x2237], succ=[0x2354B0x2237, 0x2d1dB0x2237]
    =================================
    0x2347S0x2237: v2347V2237(0x0) = CONST 
    0x234bS0x2237: v234bV2237 = ADD v21cbarg0, v2237_3
    0x234eS0x2237: v234eV2237 = LT v234bV2237, v2237_3
    0x234fS0x2237: v234fV2237 = ISZERO v234eV2237
    0x2350S0x2237: v2350V2237(0x2d1d) = CONST 
    0x2353S0x2237: JUMPI v2350V2237(0x2d1d), v234fV2237

    Begin block 0x2354B0x2237
    prev=[0x2346B0x2237], succ=[]
    =================================
    0x2354S0x2237: v2354V2237(0x40) = CONST 
    0x2357S0x2237: v2357V2237 = MLOAD v2354V2237(0x40)
    0x2358S0x2237: v2358V2237(0x461bcd) = CONST 
    0x235cS0x2237: v235cV2237(0xe5) = CONST 
    0x235eS0x2237: v235eV2237(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v235cV2237(0xe5), v2358V2237(0x461bcd)
    0x2360S0x2237: MSTORE v2357V2237, v235eV2237(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2361S0x2237: v2361V2237(0x20) = CONST 
    0x2363S0x2237: v2363V2237(0x4) = CONST 
    0x2366S0x2237: v2366V2237 = ADD v2357V2237, v2363V2237(0x4)
    0x2367S0x2237: MSTORE v2366V2237, v2361V2237(0x20)
    0x2368S0x2237: v2368V2237(0x1b) = CONST 
    0x236aS0x2237: v236aV2237(0x24) = CONST 
    0x236dS0x2237: v236dV2237 = ADD v2357V2237, v236aV2237(0x24)
    0x236eS0x2237: MSTORE v236dV2237, v2368V2237(0x1b)
    0x236fS0x2237: v236fV2237(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2390S0x2237: v2390V2237(0x44) = CONST 
    0x2393S0x2237: v2393V2237 = ADD v2357V2237, v2390V2237(0x44)
    0x2394S0x2237: MSTORE v2393V2237, v236fV2237(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2396S0x2237: v2396V2237 = MLOAD v2354V2237(0x40)
    0x239aS0x2237: v239aV2237(0x0) = SUB v2357V2237, v2396V2237
    0x239bS0x2237: v239bV2237(0x64) = CONST 
    0x239dS0x2237: v239dV2237(0x64) = ADD v239bV2237(0x64), v239aV2237(0x0)
    0x239fS0x2237: REVERT v2396V2237, v239dV2237(0x64)

    Begin block 0x2d1dB0x2237
    prev=[0x2346B0x2237], succ=[0x2241]
    =================================
    0x2d23S0x2237: JUMP v2238(0x2241)

    Begin block 0x2241
    prev=[0x2d1dB0x2237], succ=[0x226f, 0x2265]
    =================================
    0x2242: v2242(0x1) = CONST 
    0x2244: v2244(0x1) = CONST 
    0x2246: v2246(0xa0) = CONST 
    0x2248: v2248(0x10000000000000000000000000000000000000000) = SHL v2246(0xa0), v2244(0x1)
    0x2249: v2249(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2248(0x10000000000000000000000000000000000000000), v2242(0x1)
    0x224b: v224b = AND v21cbarg2, v2249(0xffffffffffffffffffffffffffffffffffffffff)
    0x224c: v224c(0x0) = CONST 
    0x2250: MSTORE v224c(0x0), v224b
    0x2251: v2251(0x9) = CONST 
    0x2253: v2253(0x20) = CONST 
    0x2255: MSTORE v2253(0x20), v2251(0x9)
    0x2256: v2256(0x40) = CONST 
    0x2259: v2259 = SHA3 v224c(0x0), v2256(0x40)
    0x225a: v225a = SLOAD v2259
    0x225f: v225f = GT v234bV2237, v225a
    0x2260: v2260 = ISZERO v225f
    0x2261: v2261(0x226f) = CONST 
    0x2264: JUMPI v2261(0x226f), v2260

    Begin block 0x226f
    prev=[0x2241], succ=[0x2276]
    =================================
    0x2271: v2271(0x0) = CONST 

    Begin block 0x2276
    prev=[0x226f, 0x2265], succ=[]
    =================================
    0x2276_0x1: v2276_1 = PHI v2266(0x2), v2271(0x0)
    0x227d: RETURNPRIVATE v21cbarg3, v234bV2237, v2276_1

    Begin block 0x2265
    prev=[0x2241], succ=[0x2276]
    =================================
    0x2266: v2266(0x2) = CONST 
    0x226b: v226b(0x2276) = CONST 
    0x226e: JUMP v226b(0x2276)

}

function relayInfo(bytes32,uint256)() public {
    Begin block 0x23f
    prev=[], succ=[0x247, 0x24b]
    =================================
    0x240: v240 = CALLVALUE 
    0x242: v242 = ISZERO v240
    0x243: v243(0x24b) = CONST 
    0x246: JUMPI v243(0x24b), v242

    Begin block 0x247
    prev=[0x23f], succ=[]
    =================================
    0x247: v247(0x0) = CONST 
    0x24a: REVERT v247(0x0), v247(0x0)

    Begin block 0x24b
    prev=[0x23f], succ=[0x25e, 0x262]
    =================================
    0x24d: v24d(0x2716) = CONST 
    0x250: v250(0x4) = CONST 
    0x253: v253 = CALLDATASIZE 
    0x254: v254 = SUB v253, v250(0x4)
    0x255: v255(0x40) = CONST 
    0x258: v258 = LT v254, v255(0x40)
    0x259: v259 = ISZERO v258
    0x25a: v25a(0x262) = CONST 
    0x25d: JUMPI v25a(0x262), v259

    Begin block 0x25e
    prev=[0x24b], succ=[]
    =================================
    0x25e: v25e(0x0) = CONST 
    0x261: REVERT v25e(0x0), v25e(0x0)

    Begin block 0x262
    prev=[0x24b], succ=[0x967]
    =================================
    0x265: v265 = CALLDATALOAD v250(0x4)
    0x267: v267(0x20) = CONST 
    0x269: v269(0x24) = ADD v267(0x20), v250(0x4)
    0x26a: v26a = CALLDATALOAD v269(0x24)
    0x26b: v26b(0x967) = CONST 
    0x26e: JUMP v26b(0x967)

    Begin block 0x967
    prev=[0x262], succ=[0x97f, 0x980]
    =================================
    0x968: v968(0x6) = CONST 
    0x96a: v96a(0x20) = CONST 
    0x96c: MSTORE v96a(0x20), v968(0x6)
    0x96e: v96e(0x0) = CONST 
    0x970: MSTORE v96e(0x0), v265
    0x971: v971(0x40) = CONST 
    0x973: v973(0x0) = CONST 
    0x975: v975 = SHA3 v973(0x0), v971(0x40)
    0x978: v978 = SLOAD v975
    0x97a: v97a = LT v26a, v978
    0x97b: v97b(0x980) = CONST 
    0x97e: JUMPI v97b(0x980), v97a

    Begin block 0x97f
    prev=[0x967], succ=[]
    =================================
    0x97f: THROW 

    Begin block 0x980
    prev=[0x967], succ=[0x2716]
    =================================
    0x981: v981(0x0) = CONST 
    0x985: MSTORE v981(0x0), v975
    0x986: v986(0x20) = CONST 
    0x98a: v98a = SHA3 v981(0x0), v986(0x20)
    0x98b: v98b = ADD v98a, v26a
    0x98c: v98c = SLOAD v98b
    0x98d: v98d(0x1) = CONST 
    0x98f: v98f(0x1) = CONST 
    0x991: v991(0xa0) = CONST 
    0x993: v993(0x10000000000000000000000000000000000000000) = SHL v991(0xa0), v98f(0x1)
    0x994: v994(0xffffffffffffffffffffffffffffffffffffffff) = SUB v993(0x10000000000000000000000000000000000000000), v98d(0x1)
    0x995: v995 = AND v994(0xffffffffffffffffffffffffffffffffffffffff), v98c
    0x99b: JUMP v24d(0x2716)

    Begin block 0x2716
    prev=[0x980], succ=[]
    =================================
    0x2717: v2717(0x40) = CONST 
    0x271a: v271a = MLOAD v2717(0x40)
    0x271b: v271b(0x1) = CONST 
    0x271d: v271d(0x1) = CONST 
    0x271f: v271f(0xa0) = CONST 
    0x2721: v2721(0x10000000000000000000000000000000000000000) = SHL v271f(0xa0), v271d(0x1)
    0x2722: v2722(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2721(0x10000000000000000000000000000000000000000), v271b(0x1)
    0x2725: v2725 = AND v995, v2722(0xffffffffffffffffffffffffffffffffffffffff)
    0x2727: MSTORE v271a, v2725
    0x2728: v2728 = MLOAD v2717(0x40)
    0x272c: v272c(0x0) = SUB v271a, v2728
    0x272d: v272d(0x20) = CONST 
    0x272f: v272f(0x20) = ADD v272d(0x20), v272c(0x0)
    0x2731: RETURN v2728, v272f(0x20)

}

function 0x246b(0x246barg0x0, 0x246barg0x1, 0x246barg0x2) private {
    Begin block 0x246b
    prev=[], succ=[0x247a, 0x2473]
    =================================
    0x246c: v246c(0x0) = CONST 
    0x246f: v246f(0x247a) = CONST 
    0x2472: JUMPI v246f(0x247a), v246barg1

    Begin block 0x247a
    prev=[0x246b], succ=[0x2486, 0x2487]
    =================================
    0x247d: v247d = MUL v246barg0, v246barg1
    0x2482: v2482(0x2487) = CONST 
    0x2485: JUMPI v2482(0x2487), v246barg1

    Begin block 0x2486
    prev=[0x247a], succ=[]
    =================================
    0x2486: THROW 

    Begin block 0x2487
    prev=[0x247a], succ=[0x248e, 0x2d68]
    =================================
    0x2488: v2488 = DIV v247d, v246barg1
    0x2489: v2489 = EQ v2488, v246barg0
    0x248a: v248a(0x2d68) = CONST 
    0x248d: JUMPI v248a(0x2d68), v2489

    Begin block 0x248e
    prev=[0x2487], succ=[]
    =================================
    0x248e: v248e(0x40) = CONST 
    0x2490: v2490 = MLOAD v248e(0x40)
    0x2491: v2491(0x461bcd) = CONST 
    0x2495: v2495(0xe5) = CONST 
    0x2497: v2497(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2495(0xe5), v2491(0x461bcd)
    0x2499: MSTORE v2490, v2497(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x249a: v249a(0x4) = CONST 
    0x249c: v249c = ADD v249a(0x4), v2490
    0x249f: v249f(0x20) = CONST 
    0x24a1: v24a1 = ADD v249f(0x20), v249c
    0x24a4: v24a4(0x20) = SUB v24a1, v249c
    0x24a6: MSTORE v249c, v24a4(0x20)
    0x24a7: v24a7(0x21) = CONST 
    0x24aa: MSTORE v24a1, v24a7(0x21)
    0x24ab: v24ab(0x20) = CONST 
    0x24ad: v24ad = ADD v24ab(0x20), v24a1
    0x24af: v24af(0x253b) = CONST 
    0x24b2: v24b2(0x21) = CONST 
    0x24b5: CODECOPY v24ad, v24af(0x253b), v24b2(0x21)
    0x24b6: v24b6(0x40) = CONST 
    0x24b8: v24b8 = ADD v24b6(0x40), v24ad
    0x24bc: v24bc(0x40) = CONST 
    0x24be: v24be = MLOAD v24bc(0x40)
    0x24c1: v24c1(0x84) = SUB v24b8, v24be
    0x24c3: REVERT v24be, v24c1(0x84)

    Begin block 0x2d68
    prev=[0x2487], succ=[]
    =================================
    0x2d6e: RETURNPRIVATE v246barg2, v247d

    Begin block 0x2473
    prev=[0x246b], succ=[0x2d43]
    =================================
    0x2474: v2474(0x0) = CONST 
    0x2476: v2476(0x2d43) = CONST 
    0x2479: JUMP v2476(0x2d43)

    Begin block 0x2d43
    prev=[0x2473], succ=[]
    =================================
    0x2d48: RETURNPRIVATE v246barg2, v2474(0x0)

}

function fallback()() public {
    Begin block 0x25c3
    prev=[], succ=[]
    =================================
    0x25c4: v25c4(0x0) = CONST 
    0x25c7: REVERT v25c4(0x0), v25c4(0x0)

}

function initialize(address,uint256,uint8[],uint256)() public {
    Begin block 0x28b
    prev=[], succ=[0x293, 0x297]
    =================================
    0x28c: v28c = CALLVALUE 
    0x28e: v28e = ISZERO v28c
    0x28f: v28f(0x297) = CONST 
    0x292: JUMPI v28f(0x297), v28e

    Begin block 0x293
    prev=[0x28b], succ=[]
    =================================
    0x293: v293(0x0) = CONST 
    0x296: REVERT v293(0x0), v293(0x0)

    Begin block 0x297
    prev=[0x28b], succ=[0x2aa, 0x2ae]
    =================================
    0x299: v299(0x2751) = CONST 
    0x29c: v29c(0x4) = CONST 
    0x29f: v29f = CALLDATASIZE 
    0x2a0: v2a0 = SUB v29f, v29c(0x4)
    0x2a1: v2a1(0x80) = CONST 
    0x2a4: v2a4 = LT v2a0, v2a1(0x80)
    0x2a5: v2a5 = ISZERO v2a4
    0x2a6: v2a6(0x2ae) = CONST 
    0x2a9: JUMPI v2a6(0x2ae), v2a5

    Begin block 0x2aa
    prev=[0x297], succ=[]
    =================================
    0x2aa: v2aa(0x0) = CONST 
    0x2ad: REVERT v2aa(0x0), v2aa(0x0)

    Begin block 0x2ae
    prev=[0x297], succ=[0x2da, 0x2de]
    =================================
    0x2af: v2af(0x1) = CONST 
    0x2b1: v2b1(0x1) = CONST 
    0x2b3: v2b3(0xa0) = CONST 
    0x2b5: v2b5(0x10000000000000000000000000000000000000000) = SHL v2b3(0xa0), v2b1(0x1)
    0x2b6: v2b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b5(0x10000000000000000000000000000000000000000), v2af(0x1)
    0x2b8: v2b8 = CALLDATALOAD v29c(0x4)
    0x2b9: v2b9 = AND v2b8, v2b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x2bb: v2bb(0x20) = CONST 
    0x2be: v2be(0x24) = ADD v29c(0x4), v2bb(0x20)
    0x2bf: v2bf = CALLDATALOAD v2be(0x24)
    0x2c2: v2c2 = ADD v29c(0x4), v2a0
    0x2c4: v2c4(0x60) = CONST 
    0x2c7: v2c7(0x64) = ADD v29c(0x4), v2c4(0x60)
    0x2c8: v2c8(0x40) = CONST 
    0x2cb: v2cb(0x44) = ADD v29c(0x4), v2c8(0x40)
    0x2cc: v2cc = CALLDATALOAD v2cb(0x44)
    0x2cd: v2cd(0x100000000) = CONST 
    0x2d4: v2d4 = GT v2cc, v2cd(0x100000000)
    0x2d5: v2d5 = ISZERO v2d4
    0x2d6: v2d6(0x2de) = CONST 
    0x2d9: JUMPI v2d6(0x2de), v2d5

    Begin block 0x2da
    prev=[0x2ae], succ=[]
    =================================
    0x2da: v2da(0x0) = CONST 
    0x2dd: REVERT v2da(0x0), v2da(0x0)

    Begin block 0x2de
    prev=[0x2ae], succ=[0x2ec, 0x2f0]
    =================================
    0x2e0: v2e0 = ADD v29c(0x4), v2cc
    0x2e2: v2e2(0x20) = CONST 
    0x2e5: v2e5 = ADD v2e0, v2e2(0x20)
    0x2e6: v2e6 = GT v2e5, v2c2
    0x2e7: v2e7 = ISZERO v2e6
    0x2e8: v2e8(0x2f0) = CONST 
    0x2eb: JUMPI v2e8(0x2f0), v2e7

    Begin block 0x2ec
    prev=[0x2de], succ=[]
    =================================
    0x2ec: v2ec(0x0) = CONST 
    0x2ef: REVERT v2ec(0x0), v2ec(0x0)

    Begin block 0x2f0
    prev=[0x2de], succ=[0x30e, 0x312]
    =================================
    0x2f2: v2f2 = CALLDATALOAD v2e0
    0x2f4: v2f4(0x20) = CONST 
    0x2f6: v2f6 = ADD v2f4(0x20), v2e0
    0x2f9: v2f9(0x20) = CONST 
    0x2fc: v2fc = MUL v2f2, v2f9(0x20)
    0x2fe: v2fe = ADD v2f6, v2fc
    0x2ff: v2ff = GT v2fe, v2c2
    0x300: v300(0x100000000) = CONST 
    0x307: v307 = GT v2f2, v300(0x100000000)
    0x308: v308 = OR v307, v2ff
    0x309: v309 = ISZERO v308
    0x30a: v30a(0x312) = CONST 
    0x30d: JUMPI v30a(0x312), v309

    Begin block 0x30e
    prev=[0x2f0], succ=[]
    =================================
    0x30e: v30e(0x0) = CONST 
    0x311: REVERT v30e(0x0), v30e(0x0)

    Begin block 0x312
    prev=[0x2f0], succ=[0x99c]
    =================================
    0x317: v317(0x20) = CONST 
    0x319: v319 = MUL v317(0x20), v2f2
    0x31a: v31a(0x20) = CONST 
    0x31c: v31c = ADD v31a(0x20), v319
    0x31d: v31d(0x40) = CONST 
    0x31f: v31f = MLOAD v31d(0x40)
    0x322: v322 = ADD v31f, v31c
    0x323: v323(0x40) = CONST 
    0x325: MSTORE v323(0x40), v322
    0x32d: MSTORE v31f, v2f2
    0x32e: v32e(0x20) = CONST 
    0x330: v330 = ADD v32e(0x20), v31f
    0x333: v333(0x20) = CONST 
    0x335: v335 = MUL v333(0x20), v2f2
    0x339: CALLDATACOPY v330, v2f6, v335
    0x33a: v33a(0x0) = CONST 
    0x33d: v33d = ADD v330, v335
    0x341: MSTORE v33d, v33a(0x0)
    0x348: v348 = CALLDATALOAD v2c7(0x64)
    0x34b: v34b(0x99c) = CONST 
    0x351: JUMP v34b(0x99c)

    Begin block 0x99c
    prev=[0x312], succ=[0x9af, 0x9ea]
    =================================
    0x99d: v99d(0x1) = CONST 
    0x99f: v99f = SLOAD v99d(0x1)
    0x9a0: v9a0(0x1) = CONST 
    0x9a2: v9a2(0x1) = CONST 
    0x9a4: v9a4(0xa0) = CONST 
    0x9a6: v9a6(0x10000000000000000000000000000000000000000) = SHL v9a4(0xa0), v9a2(0x1)
    0x9a7: v9a7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9a6(0x10000000000000000000000000000000000000000), v9a0(0x1)
    0x9a8: v9a8 = AND v9a7(0xffffffffffffffffffffffffffffffffffffffff), v99f
    0x9a9: v9a9 = CALLER 
    0x9aa: v9aa = EQ v9a9, v9a8
    0x9ab: v9ab(0x9ea) = CONST 
    0x9ae: JUMPI v9ab(0x9ea), v9aa

    Begin block 0x9af
    prev=[0x99c], succ=[]
    =================================
    0x9af: v9af(0x40) = CONST 
    0x9b2: v9b2 = MLOAD v9af(0x40)
    0x9b3: v9b3(0x461bcd) = CONST 
    0x9b7: v9b7(0xe5) = CONST 
    0x9b9: v9b9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v9b7(0xe5), v9b3(0x461bcd)
    0x9bb: MSTORE v9b2, v9b9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9bc: v9bc(0x20) = CONST 
    0x9be: v9be(0x4) = CONST 
    0x9c1: v9c1 = ADD v9b2, v9be(0x4)
    0x9c2: MSTORE v9c1, v9bc(0x20)
    0x9c3: v9c3(0xc) = CONST 
    0x9c5: v9c5(0x24) = CONST 
    0x9c8: v9c8 = ADD v9b2, v9c5(0x24)
    0x9c9: MSTORE v9c8, v9c3(0xc)
    0x9ca: v9ca(0x15539055551213d492569151) = CONST 
    0x9d7: v9d7(0xa2) = CONST 
    0x9d9: v9d9(0x554e415554484f52495a45440000000000000000000000000000000000000000) = SHL v9d7(0xa2), v9ca(0x15539055551213d492569151)
    0x9da: v9da(0x44) = CONST 
    0x9dd: v9dd = ADD v9b2, v9da(0x44)
    0x9de: MSTORE v9dd, v9d9(0x554e415554484f52495a45440000000000000000000000000000000000000000)
    0x9e0: v9e0 = MLOAD v9af(0x40)
    0x9e4: v9e4(0x0) = SUB v9b2, v9e0
    0x9e5: v9e5(0x64) = CONST 
    0x9e7: v9e7(0x64) = ADD v9e5(0x64), v9e4(0x0)
    0x9e9: REVERT v9e0, v9e7(0x64)

    Begin block 0x9ea
    prev=[0x99c], succ=[0x9f3, 0xa35]
    =================================
    0x9eb: v9eb(0xe) = CONST 
    0x9ed: v9ed = SLOAD v9eb(0xe)
    0x9ee: v9ee = ISZERO v9ed
    0x9ef: v9ef(0xa35) = CONST 
    0x9f2: JUMPI v9ef(0xa35), v9ee

    Begin block 0x9f3
    prev=[0x9ea], succ=[]
    =================================
    0x9f3: v9f3(0x40) = CONST 
    0x9f6: v9f6 = MLOAD v9f3(0x40)
    0x9f7: v9f7(0x461bcd) = CONST 
    0x9fb: v9fb(0xe5) = CONST 
    0x9fd: v9fd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v9fb(0xe5), v9f7(0x461bcd)
    0x9ff: MSTORE v9f6, v9fd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa00: va00(0x20) = CONST 
    0xa02: va02(0x4) = CONST 
    0xa05: va05 = ADD v9f6, va02(0x4)
    0xa06: MSTORE va05, va00(0x20)
    0xa07: va07(0x13) = CONST 
    0xa09: va09(0x24) = CONST 
    0xa0c: va0c = ADD v9f6, va09(0x24)
    0xa0d: MSTORE va0c, va07(0x13)
    0xa0e: va0e(0x10531491505116481253925512505312569151) = CONST 
    0xa22: va22(0x6a) = CONST 
    0xa24: va24(0x414c524541445920494e495449414c495a454400000000000000000000000000) = SHL va22(0x6a), va0e(0x10531491505116481253925512505312569151)
    0xa25: va25(0x44) = CONST 
    0xa28: va28 = ADD v9f6, va25(0x44)
    0xa29: MSTORE va28, va24(0x414c524541445920494e495449414c495a454400000000000000000000000000)
    0xa2b: va2b = MLOAD v9f3(0x40)
    0xa2f: va2f(0x0) = SUB v9f6, va2b
    0xa30: va30(0x64) = CONST 
    0xa32: va32(0x64) = ADD va30(0x64), va2f(0x0)
    0xa34: REVERT va2b, va32(0x64)

    Begin block 0xa35
    prev=[0x9ea], succ=[0xa63]
    =================================
    0xa36: va36(0xe) = CONST 
    0xa3a: SSTORE va36(0xe), v348
    0xa3b: va3b(0x7) = CONST 
    0xa3f: SSTORE va3b(0x7), v2bf
    0xa40: va40(0x1) = CONST 
    0xa42: va42(0x1) = CONST 
    0xa44: va44(0xa0) = CONST 
    0xa46: va46(0x10000000000000000000000000000000000000000) = SHL va44(0xa0), va42(0x1)
    0xa47: va47(0xffffffffffffffffffffffffffffffffffffffff) = SUB va46(0x10000000000000000000000000000000000000000), va40(0x1)
    0xa49: va49 = AND v2b9, va47(0xffffffffffffffffffffffffffffffffffffffff)
    0xa4a: va4a(0x0) = CONST 
    0xa4e: MSTORE va4a(0x0), va49
    0xa4f: va4f(0x4) = CONST 
    0xa51: va51(0x20) = CONST 
    0xa53: MSTORE va51(0x20), va4f(0x4)
    0xa54: va54(0x40) = CONST 
    0xa57: va57 = SHA3 va4a(0x0), va54(0x40)
    0xa59: va59 = SLOAD va57
    0xa5a: va5a(0xff) = CONST 
    0xa5c: va5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT va5a(0xff)
    0xa5d: va5d = AND va5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), va59
    0xa5e: va5e(0x1) = CONST 
    0xa60: va60 = OR va5e(0x1), va5d
    0xa62: SSTORE va57, va60

    Begin block 0xa63
    prev=[0xa35, 0xaa2], succ=[0xa70, 0xac9]
    =================================
    0xa63_0x0: va63_0 = PHI va4a(0x0), vac4
    0xa65: va65 = MLOAD v31f
    0xa67: va67(0xff) = CONST 
    0xa69: va69 = AND va67(0xff), va63_0
    0xa6a: va6a = LT va69, va65
    0xa6b: va6b = ISZERO va6a
    0xa6c: va6c(0xac9) = CONST 
    0xa6f: JUMPI va6c(0xac9), va6b

    Begin block 0xa70
    prev=[0xa63], succ=[0xa83, 0xa84]
    =================================
    0xa70: va70(0x1) = CONST 
    0xa70_0x0: va70_0 = PHI va4a(0x0), vac4
    0xa72: va72(0x5) = CONST 
    0xa74: va74(0x0) = CONST 
    0xa78: va78(0xff) = CONST 
    0xa7a: va7a = AND va78(0xff), va70_0
    0xa7c: va7c = MLOAD v31f
    0xa7e: va7e = LT va7a, va7c
    0xa7f: va7f(0xa84) = CONST 
    0xa82: JUMPI va7f(0xa84), va7e

    Begin block 0xa83
    prev=[0xa70], succ=[]
    =================================
    0xa83: THROW 

    Begin block 0xa84
    prev=[0xa70], succ=[0xa96, 0xa97]
    =================================
    0xa85: va85(0x20) = CONST 
    0xa87: va87 = MUL va85(0x20), va7a
    0xa88: va88(0x20) = CONST 
    0xa8a: va8a = ADD va88(0x20), va87
    0xa8b: va8b = ADD va8a, v31f
    0xa8c: va8c = MLOAD va8b
    0xa8d: va8d(0x2) = CONST 
    0xa90: va90 = GT va8c, va8d(0x2)
    0xa91: va91 = ISZERO va90
    0xa92: va92(0xa97) = CONST 
    0xa95: JUMPI va92(0xa97), va91

    Begin block 0xa96
    prev=[0xa84], succ=[]
    =================================
    0xa96: THROW 

    Begin block 0xa97
    prev=[0xa84], succ=[0xaa1, 0xaa2]
    =================================
    0xa98: va98(0x2) = CONST 
    0xa9b: va9b = GT va8c, va98(0x2)
    0xa9c: va9c = ISZERO va9b
    0xa9d: va9d(0xaa2) = CONST 
    0xaa0: JUMPI va9d(0xaa2), va9c

    Begin block 0xaa1
    prev=[0xa97], succ=[]
    =================================
    0xaa1: THROW 

    Begin block 0xaa2
    prev=[0xa97], succ=[0xa63]
    =================================
    0xaa2_0x4: vaa2_4 = PHI va4a(0x0), vac4
    0xaa4: MSTORE va74(0x0), va8c
    0xaa5: vaa5(0x20) = CONST 
    0xaa8: vaa8(0x20) = ADD va74(0x0), vaa5(0x20)
    0xaac: MSTORE vaa8(0x20), va72(0x5)
    0xaad: vaad(0x40) = CONST 
    0xaaf: vaaf(0x40) = ADD vaad(0x40), va74(0x0)
    0xab0: vab0(0x0) = CONST 
    0xab2: vab2 = SHA3 vab0(0x0), vaaf(0x40)
    0xab4: vab4 = SLOAD vab2
    0xab5: vab5(0xff) = CONST 
    0xab7: vab7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vab5(0xff)
    0xab8: vab8 = AND vab7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vab4
    0xaba: vaba = ISZERO va70(0x1)
    0xabb: vabb = ISZERO vaba
    0xabf: vabf = OR vabb, vab8
    0xac1: SSTORE vab2, vabf
    0xac2: vac2(0x1) = CONST 
    0xac4: vac4 = ADD vac2(0x1), vaa2_4
    0xac5: vac5(0xa63) = CONST 
    0xac8: JUMP vac5(0xa63)

    Begin block 0xac9
    prev=[0xa63], succ=[0x2751]
    =================================
    0xacc: vacc(0xf) = CONST 
    0xacf: vacf = SLOAD vacc(0xf)
    0xad0: vad0(0xff) = CONST 
    0xad2: vad2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vad0(0xff)
    0xad3: vad3 = AND vad2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vacf
    0xad5: SSTORE vacc(0xf), vad3
    0xad9: JUMP v299(0x2751)

    Begin block 0x2751
    prev=[0xac9], succ=[]
    =================================
    0x2752: STOP 

}

function receiveTotalAmount(address)() public {
    Begin block 0x354
    prev=[], succ=[0x35c, 0x360]
    =================================
    0x355: v355 = CALLVALUE 
    0x357: v357 = ISZERO v355
    0x358: v358(0x360) = CONST 
    0x35b: JUMPI v358(0x360), v357

    Begin block 0x35c
    prev=[0x354], succ=[]
    =================================
    0x35c: v35c(0x0) = CONST 
    0x35f: REVERT v35c(0x0), v35c(0x0)

    Begin block 0x360
    prev=[0x354], succ=[0x373, 0x377]
    =================================
    0x362: v362(0x2772) = CONST 
    0x365: v365(0x4) = CONST 
    0x368: v368 = CALLDATASIZE 
    0x369: v369 = SUB v368, v365(0x4)
    0x36a: v36a(0x20) = CONST 
    0x36d: v36d = LT v369, v36a(0x20)
    0x36e: v36e = ISZERO v36d
    0x36f: v36f(0x377) = CONST 
    0x372: JUMPI v36f(0x377), v36e

    Begin block 0x373
    prev=[0x360], succ=[]
    =================================
    0x373: v373(0x0) = CONST 
    0x376: REVERT v373(0x0), v373(0x0)

    Begin block 0x377
    prev=[0x360], succ=[0xada]
    =================================
    0x379: v379 = CALLDATALOAD v365(0x4)
    0x37a: v37a(0x1) = CONST 
    0x37c: v37c(0x1) = CONST 
    0x37e: v37e(0xa0) = CONST 
    0x380: v380(0x10000000000000000000000000000000000000000) = SHL v37e(0xa0), v37c(0x1)
    0x381: v381(0xffffffffffffffffffffffffffffffffffffffff) = SUB v380(0x10000000000000000000000000000000000000000), v37a(0x1)
    0x382: v382 = AND v381(0xffffffffffffffffffffffffffffffffffffffff), v379
    0x383: v383(0xada) = CONST 
    0x386: JUMP v383(0xada)

    Begin block 0xada
    prev=[0x377], succ=[0x2772]
    =================================
    0xadb: vadb(0xd) = CONST 
    0xadd: vadd(0x20) = CONST 
    0xadf: MSTORE vadd(0x20), vadb(0xd)
    0xae0: vae0(0x0) = CONST 
    0xae4: MSTORE vae0(0x0), v382
    0xae5: vae5(0x40) = CONST 
    0xae8: vae8 = SHA3 vae0(0x0), vae5(0x40)
    0xae9: vae9 = SLOAD vae8
    0xaeb: JUMP v362(0x2772)

    Begin block 0x2772
    prev=[0xada], succ=[]
    =================================
    0x2773: v2773(0x40) = CONST 
    0x2776: v2776 = MLOAD v2773(0x40)
    0x2779: MSTORE v2776, vae9
    0x277a: v277a = MLOAD v2773(0x40)
    0x277e: v277e(0x0) = SUB v2776, v277a
    0x277f: v277f(0x20) = CONST 
    0x2781: v2781(0x20) = ADD v277f(0x20), v277e(0x0)
    0x2783: RETURN v277a, v2781(0x20)

}

function receiveToken(address,uint256,address,string)() public {
    Begin block 0x399
    prev=[], succ=[0x3a1, 0x3a5]
    =================================
    0x39a: v39a = CALLVALUE 
    0x39c: v39c = ISZERO v39a
    0x39d: v39d(0x3a5) = CONST 
    0x3a0: JUMPI v39d(0x3a5), v39c

    Begin block 0x3a1
    prev=[0x399], succ=[]
    =================================
    0x3a1: v3a1(0x0) = CONST 
    0x3a4: REVERT v3a1(0x0), v3a1(0x0)

    Begin block 0x3a5
    prev=[0x399], succ=[0x3b8, 0x3bc]
    =================================
    0x3a7: v3a7(0x27a3) = CONST 
    0x3aa: v3aa(0x4) = CONST 
    0x3ad: v3ad = CALLDATASIZE 
    0x3ae: v3ae = SUB v3ad, v3aa(0x4)
    0x3af: v3af(0x80) = CONST 
    0x3b2: v3b2 = LT v3ae, v3af(0x80)
    0x3b3: v3b3 = ISZERO v3b2
    0x3b4: v3b4(0x3bc) = CONST 
    0x3b7: JUMPI v3b4(0x3bc), v3b3

    Begin block 0x3b8
    prev=[0x3a5], succ=[]
    =================================
    0x3b8: v3b8(0x0) = CONST 
    0x3bb: REVERT v3b8(0x0), v3b8(0x0)

    Begin block 0x3bc
    prev=[0x3a5], succ=[0x3f2, 0x3f6]
    =================================
    0x3bd: v3bd(0x1) = CONST 
    0x3bf: v3bf(0x1) = CONST 
    0x3c1: v3c1(0xa0) = CONST 
    0x3c3: v3c3(0x10000000000000000000000000000000000000000) = SHL v3c1(0xa0), v3bf(0x1)
    0x3c4: v3c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c3(0x10000000000000000000000000000000000000000), v3bd(0x1)
    0x3c6: v3c6 = CALLDATALOAD v3aa(0x4)
    0x3c8: v3c8 = AND v3c4(0xffffffffffffffffffffffffffffffffffffffff), v3c6
    0x3ca: v3ca(0x20) = CONST 
    0x3cd: v3cd(0x24) = ADD v3aa(0x4), v3ca(0x20)
    0x3ce: v3ce = CALLDATALOAD v3cd(0x24)
    0x3d0: v3d0(0x40) = CONST 
    0x3d3: v3d3(0x44) = ADD v3aa(0x4), v3d0(0x40)
    0x3d4: v3d4 = CALLDATALOAD v3d3(0x44)
    0x3d7: v3d7 = AND v3c4(0xffffffffffffffffffffffffffffffffffffffff), v3d4
    0x3da: v3da = ADD v3aa(0x4), v3ae
    0x3dc: v3dc(0x80) = CONST 
    0x3df: v3df(0x84) = ADD v3aa(0x4), v3dc(0x80)
    0x3e0: v3e0(0x60) = CONST 
    0x3e3: v3e3(0x64) = ADD v3aa(0x4), v3e0(0x60)
    0x3e4: v3e4 = CALLDATALOAD v3e3(0x64)
    0x3e5: v3e5(0x100000000) = CONST 
    0x3ec: v3ec = GT v3e4, v3e5(0x100000000)
    0x3ed: v3ed = ISZERO v3ec
    0x3ee: v3ee(0x3f6) = CONST 
    0x3f1: JUMPI v3ee(0x3f6), v3ed

    Begin block 0x3f2
    prev=[0x3bc], succ=[]
    =================================
    0x3f2: v3f2(0x0) = CONST 
    0x3f5: REVERT v3f2(0x0), v3f2(0x0)

    Begin block 0x3f6
    prev=[0x3bc], succ=[0x404, 0x408]
    =================================
    0x3f8: v3f8 = ADD v3aa(0x4), v3e4
    0x3fa: v3fa(0x20) = CONST 
    0x3fd: v3fd = ADD v3f8, v3fa(0x20)
    0x3fe: v3fe = GT v3fd, v3da
    0x3ff: v3ff = ISZERO v3fe
    0x400: v400(0x408) = CONST 
    0x403: JUMPI v400(0x408), v3ff

    Begin block 0x404
    prev=[0x3f6], succ=[]
    =================================
    0x404: v404(0x0) = CONST 
    0x407: REVERT v404(0x0), v404(0x0)

    Begin block 0x408
    prev=[0x3f6], succ=[0x426, 0x42a]
    =================================
    0x40a: v40a = CALLDATALOAD v3f8
    0x40c: v40c(0x20) = CONST 
    0x40e: v40e = ADD v40c(0x20), v3f8
    0x411: v411(0x1) = CONST 
    0x414: v414 = MUL v40a, v411(0x1)
    0x416: v416 = ADD v40e, v414
    0x417: v417 = GT v416, v3da
    0x418: v418(0x100000000) = CONST 
    0x41f: v41f = GT v40a, v418(0x100000000)
    0x420: v420 = OR v41f, v417
    0x421: v421 = ISZERO v420
    0x422: v422(0x42a) = CONST 
    0x425: JUMPI v422(0x42a), v421

    Begin block 0x426
    prev=[0x408], succ=[]
    =================================
    0x426: v426(0x0) = CONST 
    0x429: REVERT v426(0x0), v426(0x0)

    Begin block 0x42a
    prev=[0x408], succ=[0xaec]
    =================================
    0x42f: v42f(0x1f) = CONST 
    0x431: v431 = ADD v42f(0x1f), v40a
    0x432: v432(0x20) = CONST 
    0x436: v436 = DIV v431, v432(0x20)
    0x437: v437 = MUL v436, v432(0x20)
    0x438: v438(0x20) = CONST 
    0x43a: v43a = ADD v438(0x20), v437
    0x43b: v43b(0x40) = CONST 
    0x43d: v43d = MLOAD v43b(0x40)
    0x440: v440 = ADD v43d, v43a
    0x441: v441(0x40) = CONST 
    0x443: MSTORE v441(0x40), v440
    0x44b: MSTORE v43d, v40a
    0x44c: v44c(0x20) = CONST 
    0x44e: v44e = ADD v44c(0x20), v43d
    0x454: CALLDATACOPY v44e, v40e, v40a
    0x455: v455(0x0) = CONST 
    0x458: v458 = ADD v44e, v40a
    0x45c: MSTORE v458, v455(0x0)
    0x461: v461(0xaec) = CONST 
    0x46a: JUMP v461(0xaec)

    Begin block 0xaec
    prev=[0x42a], succ=[0xb04, 0xb50]
    =================================
    0xaed: vaed = CALLER 
    0xaee: vaee(0x0) = CONST 
    0xaf2: MSTORE vaee(0x0), vaed
    0xaf3: vaf3(0x3) = CONST 
    0xaf5: vaf5(0x20) = CONST 
    0xaf7: MSTORE vaf5(0x20), vaf3(0x3)
    0xaf8: vaf8(0x40) = CONST 
    0xafb: vafb = SHA3 vaee(0x0), vaf8(0x40)
    0xafc: vafc = SLOAD vafb
    0xafd: vafd(0xff) = CONST 
    0xaff: vaff = AND vafd(0xff), vafc
    0xb00: vb00(0xb50) = CONST 
    0xb03: JUMPI vb00(0xb50), vaff

    Begin block 0xb04
    prev=[0xaec], succ=[]
    =================================
    0xb04: vb04(0x40) = CONST 
    0xb07: vb07 = MLOAD vb04(0x40)
    0xb08: vb08(0x461bcd) = CONST 
    0xb0c: vb0c(0xe5) = CONST 
    0xb0e: vb0e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vb0c(0xe5), vb08(0x461bcd)
    0xb10: MSTORE vb07, vb0e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb11: vb11(0x20) = CONST 
    0xb13: vb13(0x4) = CONST 
    0xb16: vb16 = ADD vb07, vb13(0x4)
    0xb17: MSTORE vb16, vb11(0x20)
    0xb18: vb18(0x19) = CONST 
    0xb1a: vb1a(0x24) = CONST 
    0xb1d: vb1d = ADD vb07, vb1a(0x24)
    0xb1e: MSTORE vb1d, vb18(0x19)
    0xb1f: vb1f(0x43616c6c6572206973206e6f74207468652072656c6179657200000000000000) = CONST 
    0xb40: vb40(0x44) = CONST 
    0xb43: vb43 = ADD vb07, vb40(0x44)
    0xb44: MSTORE vb43, vb1f(0x43616c6c6572206973206e6f74207468652072656c6179657200000000000000)
    0xb46: vb46 = MLOAD vb04(0x40)
    0xb4a: vb4a(0x0) = SUB vb07, vb46
    0xb4b: vb4b(0x64) = CONST 
    0xb4d: vb4d(0x64) = ADD vb4b(0x64), vb4a(0x0)
    0xb4f: REVERT vb46, vb4d(0x64)

    Begin block 0xb50
    prev=[0xaec], succ=[0xb5c, 0xb9b]
    =================================
    0xb51: vb51(0xf) = CONST 
    0xb53: vb53 = SLOAD vb51(0xf)
    0xb54: vb54(0xff) = CONST 
    0xb56: vb56 = AND vb54(0xff), vb53
    0xb57: vb57 = ISZERO vb56
    0xb58: vb58(0xb9b) = CONST 
    0xb5b: JUMPI vb58(0xb9b), vb57

    Begin block 0xb5c
    prev=[0xb50], succ=[]
    =================================
    0xb5c: vb5c(0x40) = CONST 
    0xb5f: vb5f = MLOAD vb5c(0x40)
    0xb60: vb60(0x461bcd) = CONST 
    0xb64: vb64(0xe5) = CONST 
    0xb66: vb66(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vb64(0xe5), vb60(0x461bcd)
    0xb68: MSTORE vb5f, vb66(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb69: vb69(0x20) = CONST 
    0xb6b: vb6b(0x4) = CONST 
    0xb6e: vb6e = ADD vb5f, vb6b(0x4)
    0xb6f: MSTORE vb6e, vb69(0x20)
    0xb70: vb70(0x10) = CONST 
    0xb72: vb72(0x24) = CONST 
    0xb75: vb75 = ADD vb5f, vb72(0x24)
    0xb76: MSTORE vb75, vb70(0x10)
    0xb77: vb77(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0xb88: vb88(0x82) = CONST 
    0xb8a: vb8a(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL vb88(0x82), vb77(0x14185d5cd8589b194e881c185d5cd959)
    0xb8b: vb8b(0x44) = CONST 
    0xb8e: vb8e = ADD vb5f, vb8b(0x44)
    0xb8f: MSTORE vb8e, vb8a(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0xb91: vb91 = MLOAD vb5c(0x40)
    0xb95: vb95(0x0) = SUB vb5f, vb91
    0xb96: vb96(0x64) = CONST 
    0xb98: vb98(0x64) = ADD vb96(0x64), vb95(0x0)
    0xb9a: REVERT vb91, vb98(0x64)

    Begin block 0xb9b
    prev=[0xb50], succ=[0xbde]
    =================================
    0xb9c: vb9c(0x0) = CONST 
    0xba2: vba2(0x40) = CONST 
    0xba4: vba4 = MLOAD vba2(0x40)
    0xba5: vba5(0x20) = CONST 
    0xba7: vba7 = ADD vba5(0x20), vba4
    0xbaa: vbaa(0x1) = CONST 
    0xbac: vbac(0x1) = CONST 
    0xbae: vbae(0xa0) = CONST 
    0xbb0: vbb0(0x10000000000000000000000000000000000000000) = SHL vbae(0xa0), vbac(0x1)
    0xbb1: vbb1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb0(0x10000000000000000000000000000000000000000), vbaa(0x1)
    0xbb2: vbb2 = AND vbb1(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0xbb3: vbb3(0x60) = CONST 
    0xbb5: vbb5 = SHL vbb3(0x60), vbb2
    0xbb7: MSTORE vba7, vbb5
    0xbb8: vbb8(0x14) = CONST 
    0xbba: vbba = ADD vbb8(0x14), vba7
    0xbbc: vbbc(0x1) = CONST 
    0xbbe: vbbe(0x1) = CONST 
    0xbc0: vbc0(0xa0) = CONST 
    0xbc2: vbc2(0x10000000000000000000000000000000000000000) = SHL vbc0(0xa0), vbbe(0x1)
    0xbc3: vbc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbc2(0x10000000000000000000000000000000000000000), vbbc(0x1)
    0xbc4: vbc4 = AND vbc3(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0xbc5: vbc5(0x60) = CONST 
    0xbc7: vbc7 = SHL vbc5(0x60), vbc4
    0xbc9: MSTORE vbba, vbc7
    0xbca: vbca(0x14) = CONST 
    0xbcc: vbcc = ADD vbca(0x14), vbba
    0xbcf: MSTORE vbcc, v3ce
    0xbd0: vbd0(0x20) = CONST 
    0xbd2: vbd2 = ADD vbd0(0x20), vbcc
    0xbd5: vbd5 = MLOAD v43d
    0xbd7: vbd7(0x20) = CONST 
    0xbd9: vbd9 = ADD vbd7(0x20), v43d

    Begin block 0xbde
    prev=[0xb9b, 0xbe7], succ=[0xbfd, 0xbe7]
    =================================
    0xbde_0x2: vbde_2 = PHI vbd5, vbf0
    0xbdf: vbdf(0x20) = CONST 
    0xbe2: vbe2 = LT vbde_2, vbdf(0x20)
    0xbe3: vbe3(0xbfd) = CONST 
    0xbe6: JUMPI vbe3(0xbfd), vbe2

    Begin block 0xbfd
    prev=[0xbde], succ=[0x20bcB0xbfd]
    =================================
    0xbfd_0x0: vbfd_0 = PHI vbd9, vbf8
    0xbfd_0x1: vbfd_1 = PHI vbd2, vbf6
    0xbfd_0x2: vbfd_2 = PHI vbd5, vbf0
    0xbfe: vbfe(0x1) = CONST 
    0xc01: vc01(0x20) = CONST 
    0xc03: vc03 = SUB vc01(0x20), vbfd_2
    0xc04: vc04(0x100) = CONST 
    0xc07: vc07 = EXP vc04(0x100), vc03
    0xc08: vc08 = SUB vc07, vbfe(0x1)
    0xc0a: vc0a = NOT vc08
    0xc0c: vc0c = MLOAD vbfd_0
    0xc0d: vc0d = AND vc0c, vc0a
    0xc10: vc10 = MLOAD vbfd_1
    0xc11: vc11 = AND vc10, vc08
    0xc14: vc14 = OR vc0d, vc11
    0xc16: MSTORE vbfd_1, vc14
    0xc1f: vc1f = ADD vbd5, vbd2
    0xc26: vc26(0x40) = CONST 
    0xc28: vc28 = MLOAD vc26(0x40)
    0xc29: vc29(0x20) = CONST 
    0xc2d: vc2d = SUB vc1f, vc28
    0xc2e: vc2e = SUB vc2d, vc29(0x20)
    0xc30: MSTORE vc28, vc2e
    0xc32: vc32(0x40) = CONST 
    0xc34: MSTORE vc32(0x40), vc1f
    0xc36: vc36 = MLOAD vc28
    0xc38: vc38(0x20) = CONST 
    0xc3a: vc3a = ADD vc38(0x20), vc28
    0xc3b: vc3b = SHA3 vc3a, vc36
    0xc3e: vc3e(0xc46) = CONST 
    0xc42: vc42(0x20bc) = CONST 
    0xc45: JUMP vc42(0x20bc)

    Begin block 0x20bcB0xbfd
    prev=[0xbfd], succ=[0x20ecB0xbfd, 0x211aB0xbfd]
    =================================
    0x20bdS0xbfd: v20bdVbfd(0x0) = CONST 
    0x20c1S0xbfd: MSTORE v20bdVbfd(0x0), vc3b
    0x20c2S0xbfd: v20c2Vbfd(0x6) = CONST 
    0x20c4S0xbfd: v20c4Vbfd(0x20) = CONST 
    0x20c8S0xbfd: MSTORE v20c4Vbfd(0x20), v20c2Vbfd(0x6)
    0x20c9S0xbfd: v20c9Vbfd(0x40) = CONST 
    0x20cdS0xbfd: v20cdVbfd = SHA3 v20bdVbfd(0x0), v20c9Vbfd(0x40)
    0x20cfS0xbfd: v20cfVbfd = SLOAD v20cdVbfd
    0x20d1S0xbfd: v20d1Vbfd = MLOAD v20c9Vbfd(0x40)
    0x20d4S0xbfd: v20d4Vbfd = MUL v20c4Vbfd(0x20), v20cfVbfd
    0x20d6S0xbfd: v20d6Vbfd = ADD v20d1Vbfd, v20d4Vbfd
    0x20d8S0xbfd: v20d8Vbfd = ADD v20c4Vbfd(0x20), v20d6Vbfd
    0x20dbS0xbfd: MSTORE v20c9Vbfd(0x40), v20d8Vbfd
    0x20deS0xbfd: MSTORE v20d1Vbfd, v20cfVbfd
    0x20dfS0xbfd: v20dfVbfd(0x60) = CONST 
    0x20e3S0xbfd: v20e3Vbfd = ADD v20d1Vbfd, v20c4Vbfd(0x20)
    0x20e7S0xbfd: v20e7Vbfd = ISZERO v20cfVbfd
    0x20e8S0xbfd: v20e8Vbfd(0x211a) = CONST 
    0x20ebS0xbfd: JUMPI v20e8Vbfd(0x211a), v20e7Vbfd

    Begin block 0x20ecB0xbfd
    prev=[0x20bcB0xbfd], succ=[0x20fcB0xbfd]
    =================================
    0x20ecS0xbfd: v20ecVbfd(0x20) = CONST 
    0x20eeS0xbfd: v20eeVbfd = MUL v20ecVbfd(0x20), v20cfVbfd
    0x20f0S0xbfd: v20f0Vbfd = ADD v20e3Vbfd, v20eeVbfd
    0x20f3S0xbfd: v20f3Vbfd(0x0) = CONST 
    0x20f5S0xbfd: MSTORE v20f3Vbfd(0x0), v20cdVbfd
    0x20f6S0xbfd: v20f6Vbfd(0x20) = CONST 
    0x20f8S0xbfd: v20f8Vbfd(0x0) = CONST 
    0x20faS0xbfd: v20faVbfd = SHA3 v20f8Vbfd(0x0), v20f6Vbfd(0x20)

    Begin block 0x20fcB0xbfd
    prev=[0x20ecB0xbfd, 0x20fcB0xbfd], succ=[0x211aB0xbfd, 0x20fcB0xbfd]
    =================================
    0x20fc_0x0S0xbfd: v20fc_0Vbfd = PHI v20e3Vbfd, v2112Vbfd
    0x20fc_0x1S0xbfd: v20fc_1Vbfd = PHI v20faVbfd, v210eVbfd
    0x20feS0xbfd: v20feVbfd = SLOAD v20fc_1Vbfd
    0x20ffS0xbfd: v20ffVbfd(0x1) = CONST 
    0x2101S0xbfd: v2101Vbfd(0x1) = CONST 
    0x2103S0xbfd: v2103Vbfd(0xa0) = CONST 
    0x2105S0xbfd: v2105Vbfd(0x10000000000000000000000000000000000000000) = SHL v2103Vbfd(0xa0), v2101Vbfd(0x1)
    0x2106S0xbfd: v2106Vbfd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2105Vbfd(0x10000000000000000000000000000000000000000), v20ffVbfd(0x1)
    0x2107S0xbfd: v2107Vbfd = AND v2106Vbfd(0xffffffffffffffffffffffffffffffffffffffff), v20feVbfd
    0x2109S0xbfd: MSTORE v20fc_0Vbfd, v2107Vbfd
    0x210aS0xbfd: v210aVbfd(0x1) = CONST 
    0x210eS0xbfd: v210eVbfd = ADD v20fc_1Vbfd, v210aVbfd(0x1)
    0x2110S0xbfd: v2110Vbfd(0x20) = CONST 
    0x2112S0xbfd: v2112Vbfd = ADD v2110Vbfd(0x20), v20fc_0Vbfd
    0x2115S0xbfd: v2115Vbfd = GT v20f0Vbfd, v2112Vbfd
    0x2116S0xbfd: v2116Vbfd(0x20fc) = CONST 
    0x2119S0xbfd: JUMPI v2116Vbfd(0x20fc), v2115Vbfd

    Begin block 0x211aB0xbfd
    prev=[0x20bcB0xbfd, 0x20fcB0xbfd], succ=[0x2124B0xbfd]
    =================================
    0x2122S0xbfd: v2122Vbfd(0x0) = CONST 

    Begin block 0x2124B0xbfd
    prev=[0x211aB0xbfd, 0x2165B0xbfd], succ=[0x212eB0xbfd, 0x216dB0xbfd]
    =================================
    0x2124_0x0S0xbfd: v2124_0Vbfd = PHI v2122Vbfd(0x0), v2168Vbfd
    0x2126S0xbfd: v2126Vbfd = MLOAD v20d1Vbfd
    0x2128S0xbfd: v2128Vbfd = LT v2124_0Vbfd, v2126Vbfd
    0x2129S0xbfd: v2129Vbfd = ISZERO v2128Vbfd
    0x212aS0xbfd: v212aVbfd(0x216d) = CONST 
    0x212dS0xbfd: JUMPI v212aVbfd(0x216d), v2129Vbfd

    Begin block 0x212eB0xbfd
    prev=[0x2124B0xbfd], succ=[0x2143B0xbfd, 0x2142B0xbfd]
    =================================
    0x212eS0xbfd: v212eVbfd = CALLER 
    0x212e_0x0S0xbfd: v212e_0Vbfd = PHI v2122Vbfd(0x0), v2168Vbfd
    0x212fS0xbfd: v212fVbfd(0x1) = CONST 
    0x2131S0xbfd: v2131Vbfd(0x1) = CONST 
    0x2133S0xbfd: v2133Vbfd(0xa0) = CONST 
    0x2135S0xbfd: v2135Vbfd(0x10000000000000000000000000000000000000000) = SHL v2133Vbfd(0xa0), v2131Vbfd(0x1)
    0x2136S0xbfd: v2136Vbfd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2135Vbfd(0x10000000000000000000000000000000000000000), v212fVbfd(0x1)
    0x2137S0xbfd: v2137Vbfd = AND v2136Vbfd(0xffffffffffffffffffffffffffffffffffffffff), v212eVbfd
    0x213bS0xbfd: v213bVbfd = MLOAD v20d1Vbfd
    0x213dS0xbfd: v213dVbfd = LT v212e_0Vbfd, v213bVbfd
    0x213eS0xbfd: v213eVbfd(0x2143) = CONST 
    0x2141S0xbfd: JUMPI v213eVbfd(0x2143), v213dVbfd

    Begin block 0x2143B0xbfd
    prev=[0x212eB0xbfd], succ=[0x215bB0xbfd, 0x2165B0xbfd]
    =================================
    0x2143_0x0S0xbfd: v2143_0Vbfd = PHI v2122Vbfd(0x0), v2168Vbfd
    0x2144S0xbfd: v2144Vbfd(0x20) = CONST 
    0x2146S0xbfd: v2146Vbfd = MUL v2144Vbfd(0x20), v2143_0Vbfd
    0x2147S0xbfd: v2147Vbfd(0x20) = CONST 
    0x2149S0xbfd: v2149Vbfd = ADD v2147Vbfd(0x20), v2146Vbfd
    0x214aS0xbfd: v214aVbfd = ADD v2149Vbfd, v20d1Vbfd
    0x214bS0xbfd: v214bVbfd = MLOAD v214aVbfd
    0x214cS0xbfd: v214cVbfd(0x1) = CONST 
    0x214eS0xbfd: v214eVbfd(0x1) = CONST 
    0x2150S0xbfd: v2150Vbfd(0xa0) = CONST 
    0x2152S0xbfd: v2152Vbfd(0x10000000000000000000000000000000000000000) = SHL v2150Vbfd(0xa0), v214eVbfd(0x1)
    0x2153S0xbfd: v2153Vbfd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2152Vbfd(0x10000000000000000000000000000000000000000), v214cVbfd(0x1)
    0x2154S0xbfd: v2154Vbfd = AND v2153Vbfd(0xffffffffffffffffffffffffffffffffffffffff), v214bVbfd
    0x2155S0xbfd: v2155Vbfd = EQ v2154Vbfd, v2137Vbfd
    0x2156S0xbfd: v2156Vbfd = ISZERO v2155Vbfd
    0x2157S0xbfd: v2157Vbfd(0x2165) = CONST 
    0x215aS0xbfd: JUMPI v2157Vbfd(0x2165), v2156Vbfd

    Begin block 0x215bB0xbfd
    prev=[0x2143B0xbfd], succ=[0x2174B0xbfd]
    =================================
    0x215bS0xbfd: v215bVbfd(0x1) = CONST 
    0x2161S0xbfd: v2161Vbfd(0x2174) = CONST 
    0x2164S0xbfd: JUMP v2161Vbfd(0x2174)

    Begin block 0x2174B0xbfd
    prev=[0x215bB0xbfd, 0x216dB0xbfd], succ=[0xc46]
    =================================
    0x2174_0x0S0xbfd: v2174_0Vbfd = PHI v215bVbfd(0x1), v216fVbfd(0x0)
    0x2178S0xbfd: JUMP vc3e(0xc46)

    Begin block 0xc46
    prev=[0x2174B0xbfd], succ=[0xc4c, 0xc5d]
    =================================
    0xc47: vc47 = ISZERO v2174_0Vbfd
    0xc48: vc48(0xc5d) = CONST 
    0xc4b: JUMPI vc48(0xc5d), vc47

    Begin block 0xc4c
    prev=[0xc46], succ=[0xc55]
    =================================
    0xc4c: vc4c(0xc55) = CONST 
    0xc4f: vc4f(0x1) = CONST 
    0xc51: vc51(0x2179) = CONST 
    0xc54: vc54_0 = CALLPRIVATE vc51(0x2179), vc4f(0x1), vc4c(0xc55)

    Begin block 0xc55
    prev=[0xc4c], succ=[0x2c85]
    =================================
    0xc59: vc59(0x2c85) = CONST 
    0xc5c: JUMP vc59(0x2c85)

    Begin block 0x2c85
    prev=[0xc55], succ=[0x27a3]
    =================================
    0x2c8c: JUMP v3a7(0x27a3)

    Begin block 0x27a3
    prev=[0x2c85, 0x2cac, 0xfdf], succ=[]
    =================================
    0x27a3_0x0: v27a3_0 = PHI vfd9(0x0), vc54_0, vcb5_0
    0x27a4: v27a4(0x40) = CONST 
    0x27a7: v27a7 = MLOAD v27a4(0x40)
    0x27aa: MSTORE v27a7, v27a3_0
    0x27ab: v27ab = MLOAD v27a4(0x40)
    0x27af: v27af(0x0) = SUB v27a7, v27ab
    0x27b0: v27b0(0x20) = CONST 
    0x27b2: v27b2(0x20) = ADD v27b0(0x20), v27af(0x0)
    0x27b4: RETURN v27ab, v27b2(0x20)

    Begin block 0xc5d
    prev=[0xc46], succ=[0xc72, 0xcdc]
    =================================
    0xc5e: vc5e(0x0) = CONST 
    0xc62: MSTORE vc5e(0x0), vc3b
    0xc63: vc63(0x6) = CONST 
    0xc65: vc65(0x20) = CONST 
    0xc67: MSTORE vc65(0x20), vc63(0x6)
    0xc68: vc68(0x40) = CONST 
    0xc6b: vc6b = SHA3 vc5e(0x0), vc68(0x40)
    0xc6c: vc6c = SLOAD vc6b
    0xc6e: vc6e(0xcdc) = CONST 
    0xc71: JUMPI vc6e(0xcdc), vc6c

    Begin block 0xc72
    prev=[0xc5d], succ=[0xc98]
    =================================
    0xc72: vc72(0x1) = CONST 
    0xc74: vc74(0x1) = CONST 
    0xc76: vc76(0xa0) = CONST 
    0xc78: vc78(0x10000000000000000000000000000000000000000) = SHL vc76(0xa0), vc74(0x1)
    0xc79: vc79(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc78(0x10000000000000000000000000000000000000000), vc72(0x1)
    0xc7b: vc7b = AND v3c8, vc79(0xffffffffffffffffffffffffffffffffffffffff)
    0xc7c: vc7c(0x0) = CONST 
    0xc80: MSTORE vc7c(0x0), vc7b
    0xc81: vc81(0xd) = CONST 
    0xc83: vc83(0x20) = CONST 
    0xc85: MSTORE vc83(0x20), vc81(0xd)
    0xc86: vc86(0x40) = CONST 
    0xc89: vc89 = SHA3 vc7c(0x0), vc86(0x40)
    0xc8a: vc8a = SLOAD vc89
    0xc8d: vc8d(0xc98) = CONST 
    0xc94: vc94(0x21cb) = CONST 
    0xc97: vc97_0, vc97_1 = CALLPRIVATE vc94(0x21cb), v3ce, vc8a, v3c8, vc8d(0xc98)

    Begin block 0xc98
    prev=[0xc72], succ=[0xca7, 0xca8]
    =================================
    0xc9e: vc9e(0x2) = CONST 
    0xca1: vca1 = GT vc97_1, vc9e(0x2)
    0xca2: vca2 = ISZERO vca1
    0xca3: vca3(0xca8) = CONST 
    0xca6: JUMPI vca3(0xca8), vca2

    Begin block 0xca7
    prev=[0xc98], succ=[]
    =================================
    0xca7: THROW 

    Begin block 0xca8
    prev=[0xc98], succ=[0xcae, 0xcc1]
    =================================
    0xca9: vca9 = ISZERO vc97_1
    0xcaa: vcaa(0xcc1) = CONST 
    0xcad: JUMPI vcaa(0xcc1), vca9

    Begin block 0xcae
    prev=[0xca8], succ=[0xcb6]
    =================================
    0xcae: vcae(0xcb6) = CONST 
    0xcb2: vcb2(0x2179) = CONST 
    0xcb5: vcb5_0 = CALLPRIVATE vcb2(0x2179), vc97_1, vcae(0xcb6)

    Begin block 0xcb6
    prev=[0xcae], succ=[0x2cac]
    =================================
    0xcbd: vcbd(0x2cac) = CONST 
    0xcc0: JUMP vcbd(0x2cac)

    Begin block 0x2cac
    prev=[0xcb6], succ=[0x27a3]
    =================================
    0x2cb3: JUMP v3a7(0x27a3)

    Begin block 0xcc1
    prev=[0xca8], succ=[0xcdc]
    =================================
    0xcc2: vcc2(0x1) = CONST 
    0xcc4: vcc4(0x1) = CONST 
    0xcc6: vcc6(0xa0) = CONST 
    0xcc8: vcc8(0x10000000000000000000000000000000000000000) = SHL vcc6(0xa0), vcc4(0x1)
    0xcc9: vcc9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcc8(0x10000000000000000000000000000000000000000), vcc2(0x1)
    0xccb: vccb = AND v3c8, vcc9(0xffffffffffffffffffffffffffffffffffffffff)
    0xccc: vccc(0x0) = CONST 
    0xcd0: MSTORE vccc(0x0), vccb
    0xcd1: vcd1(0xd) = CONST 
    0xcd3: vcd3(0x20) = CONST 
    0xcd5: MSTORE vcd3(0x20), vcd1(0xd)
    0xcd6: vcd6(0x40) = CONST 
    0xcd9: vcd9 = SHA3 vccc(0x0), vcd6(0x40)
    0xcda: SSTORE vcd9, vc97_0

    Begin block 0xcdc
    prev=[0xc5d, 0xcc1], succ=[0xdd4, 0xd1b]
    =================================
    0xcdd: vcdd(0x0) = CONST 
    0xce1: MSTORE vcdd(0x0), vc3b
    0xce2: vce2(0x6) = CONST 
    0xce4: vce4(0x20) = CONST 
    0xce8: MSTORE vce4(0x20), vce2(0x6)
    0xce9: vce9(0x40) = CONST 
    0xcec: vcec = SHA3 vcdd(0x0), vce9(0x40)
    0xcee: vcee = SLOAD vcec
    0xcef: vcef(0x1) = CONST 
    0xcf3: vcf3 = ADD vcef(0x1), vcee
    0xcf5: SSTORE vcec, vcf3
    0xcf8: MSTORE vcdd(0x0), vcec
    0xcfc: vcfc = SHA3 vcdd(0x0), vce4(0x20)
    0xcfd: vcfd = ADD vcfc, vcee
    0xcff: vcff = SLOAD vcfd
    0xd00: vd00(0x1) = CONST 
    0xd02: vd02(0x1) = CONST 
    0xd04: vd04(0xa0) = CONST 
    0xd06: vd06(0x10000000000000000000000000000000000000000) = SHL vd04(0xa0), vd02(0x1)
    0xd07: vd07(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd06(0x10000000000000000000000000000000000000000), vd00(0x1)
    0xd08: vd08(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vd07(0xffffffffffffffffffffffffffffffffffffffff)
    0xd09: vd09 = AND vd08(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vcff
    0xd0a: vd0a = CALLER 
    0xd0b: vd0b = OR vd0a, vd09
    0xd0d: SSTORE vcfd, vd0b
    0xd0e: vd0e(0x7) = CONST 
    0xd10: vd10 = SLOAD vd0e(0x7)
    0xd12: vd12 = ADD vc6c, vcef(0x1)
    0xd15: vd15 = LT vd12, vd10
    0xd16: vd16 = ISZERO vd15
    0xd17: vd17(0xdd4) = CONST 
    0xd1a: JUMPI vd17(0xdd4), vd16

    Begin block 0xdd4
    prev=[0xcdc], succ=[0xfd8, 0xded]
    =================================
    0xdd5: vdd5(0x7) = CONST 
    0xdd7: vdd7 = SLOAD vdd5(0x7)
    0xdd8: vdd8(0x0) = CONST 
    0xddc: MSTORE vdd8(0x0), vc3b
    0xddd: vddd(0x6) = CONST 
    0xddf: vddf(0x20) = CONST 
    0xde1: MSTORE vddf(0x20), vddd(0x6)
    0xde2: vde2(0x40) = CONST 
    0xde5: vde5 = SHA3 vdd8(0x0), vde2(0x40)
    0xde6: vde6 = SLOAD vde5
    0xde7: vde7 = EQ vde6, vdd7
    0xde8: vde8 = ISZERO vde7
    0xde9: vde9(0xfd8) = CONST 
    0xdec: JUMPI vde9(0xfd8), vde8

    Begin block 0xfd8
    prev=[0xdd4, 0xdc1, 0xfc9], succ=[0xfdf]
    =================================
    0xfd9: vfd9(0x0) = CONST 

    Begin block 0xfdf
    prev=[0xfd8], succ=[0x27a3]
    =================================
    0xfe6: JUMP v3a7(0x27a3)

    Begin block 0xded
    prev=[0xdd4], succ=[0xe3f, 0xe43]
    =================================
    0xdee: vdee(0x1) = CONST 
    0xdf0: vdf0(0x1) = CONST 
    0xdf2: vdf2(0xa0) = CONST 
    0xdf4: vdf4(0x10000000000000000000000000000000000000000) = SHL vdf2(0xa0), vdf0(0x1)
    0xdf5: vdf5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdf4(0x10000000000000000000000000000000000000000), vdee(0x1)
    0xdf6: vdf6 = AND vdf5(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0xdf7: vdf7(0xa9059cbb) = CONST 
    0xdfe: vdfe(0x40) = CONST 
    0xe00: ve00 = MLOAD vdfe(0x40)
    0xe02: ve02(0xffffffff) = CONST 
    0xe07: ve07(0xa9059cbb) = AND ve02(0xffffffff), vdf7(0xa9059cbb)
    0xe08: ve08(0xe0) = CONST 
    0xe0a: ve0a(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL ve08(0xe0), ve07(0xa9059cbb)
    0xe0c: MSTORE ve00, ve0a(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0xe0d: ve0d(0x4) = CONST 
    0xe0f: ve0f = ADD ve0d(0x4), ve00
    0xe12: ve12(0x1) = CONST 
    0xe14: ve14(0x1) = CONST 
    0xe16: ve16(0xa0) = CONST 
    0xe18: ve18(0x10000000000000000000000000000000000000000) = SHL ve16(0xa0), ve14(0x1)
    0xe19: ve19(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve18(0x10000000000000000000000000000000000000000), ve12(0x1)
    0xe1a: ve1a = AND ve19(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0xe1c: MSTORE ve0f, ve1a
    0xe1d: ve1d(0x20) = CONST 
    0xe1f: ve1f = ADD ve1d(0x20), ve0f
    0xe22: MSTORE ve1f, v3ce
    0xe23: ve23(0x20) = CONST 
    0xe25: ve25 = ADD ve23(0x20), ve1f
    0xe2a: ve2a(0x20) = CONST 
    0xe2c: ve2c(0x40) = CONST 
    0xe2e: ve2e = MLOAD ve2c(0x40)
    0xe31: ve31(0x44) = SUB ve25, ve2e
    0xe33: ve33(0x0) = CONST 
    0xe37: ve37 = EXTCODESIZE vdf6
    0xe38: ve38 = ISZERO ve37
    0xe3a: ve3a = ISZERO ve38
    0xe3b: ve3b(0xe43) = CONST 
    0xe3e: JUMPI ve3b(0xe43), ve3a

    Begin block 0xe3f
    prev=[0xded], succ=[]
    =================================
    0xe3f: ve3f(0x0) = CONST 
    0xe42: REVERT ve3f(0x0), ve3f(0x0)

    Begin block 0xe43
    prev=[0xded], succ=[0xe4e, 0xe57]
    =================================
    0xe45: ve45 = GAS 
    0xe46: ve46 = CALL ve45, vdf6, ve33(0x0), ve2e, ve31(0x44), ve2e, ve2a(0x20)
    0xe47: ve47 = ISZERO ve46
    0xe49: ve49 = ISZERO ve47
    0xe4a: ve4a(0xe57) = CONST 
    0xe4d: JUMPI ve4a(0xe57), ve49

    Begin block 0xe4e
    prev=[0xe43], succ=[]
    =================================
    0xe4e: ve4e = RETURNDATASIZE 
    0xe4f: ve4f(0x0) = CONST 
    0xe52: RETURNDATACOPY ve4f(0x0), ve4f(0x0), ve4e
    0xe53: ve53 = RETURNDATASIZE 
    0xe54: ve54(0x0) = CONST 
    0xe56: REVERT ve54(0x0), ve53

    Begin block 0xe57
    prev=[0xe43], succ=[0xe69, 0xe6d]
    =================================
    0xe5c: ve5c(0x40) = CONST 
    0xe5e: ve5e = MLOAD ve5c(0x40)
    0xe5f: ve5f = RETURNDATASIZE 
    0xe60: ve60(0x20) = CONST 
    0xe63: ve63 = LT ve5f, ve60(0x20)
    0xe64: ve64 = ISZERO ve63
    0xe65: ve65(0xe6d) = CONST 
    0xe68: JUMPI ve65(0xe6d), ve64

    Begin block 0xe69
    prev=[0xe57], succ=[]
    =================================
    0xe69: ve69(0x0) = CONST 
    0xe6c: REVERT ve69(0x0), ve69(0x0)

    Begin block 0xe6d
    prev=[0xe57], succ=[0xecf]
    =================================
    0xe70: ve70(0x40) = CONST 
    0xe73: ve73 = MLOAD ve70(0x40)
    0xe76: MSTORE ve73, v3ce
    0xe77: ve77(0x20) = CONST 
    0xe7b: ve7b = ADD ve77(0x20), ve73
    0xe7e: MSTORE ve7b, ve70(0x40)
    0xe80: ve80 = MLOAD v43d
    0xe83: ve83 = ADD ve73, ve70(0x40)
    0xe87: MSTORE ve83, ve80
    0xe89: ve89 = MLOAD v43d
    0xe8a: ve8a(0x1) = CONST 
    0xe8c: ve8c(0x1) = CONST 
    0xe8e: ve8e(0xa0) = CONST 
    0xe90: ve90(0x10000000000000000000000000000000000000000) = SHL ve8e(0xa0), ve8c(0x1)
    0xe91: ve91(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve90(0x10000000000000000000000000000000000000000), ve8a(0x1)
    0xe94: ve94 = AND v3c8, ve91(0xffffffffffffffffffffffffffffffffffffffff)
    0xe98: ve98 = AND v3d7, ve91(0xffffffffffffffffffffffffffffffffffffffff)
    0xe9a: ve9a(0x512048caf7808c7bd5eec84574a0698613ae07a6d5a1c6fd389d451658ef379b) = CONST 
    0xec1: vec1(0x60) = CONST 
    0xec4: vec4 = ADD ve73, vec1(0x60)
    0xec8: vec8 = ADD v43d, ve77(0x20)
    0xecd: vecd(0x0) = CONST 

    Begin block 0xecf
    prev=[0xe6d, 0xed8], succ=[0xee7, 0xed8]
    =================================
    0xecf_0x0: vecf_0 = PHI vecd(0x0), vee2
    0xed2: ved2 = LT vecf_0, ve89
    0xed3: ved3 = ISZERO ved2
    0xed4: ved4(0xee7) = CONST 
    0xed7: JUMPI ved4(0xee7), ved3

    Begin block 0xee7
    prev=[0xecf], succ=[0xf14, 0xefb]
    =================================
    0xef0: vef0 = ADD ve89, vec4
    0xef2: vef2(0x1f) = CONST 
    0xef4: vef4 = AND vef2(0x1f), ve89
    0xef6: vef6 = ISZERO vef4
    0xef7: vef7(0xf14) = CONST 
    0xefa: JUMPI vef7(0xf14), vef6

    Begin block 0xf14
    prev=[0xee7, 0xefb], succ=[0xf84]
    =================================
    0xf14_0x1: vf14_1 = PHI vef0, vf11
    0xf1b: vf1b(0x40) = CONST 
    0xf1d: vf1d = MLOAD vf1b(0x40)
    0xf20: vf20 = SUB vf14_1, vf1d
    0xf22: LOG3 vf1d, vf20, ve9a(0x512048caf7808c7bd5eec84574a0698613ae07a6d5a1c6fd389d451658ef379b), ve98, ve94
    0xf24: vf24(0x1) = CONST 
    0xf26: vf26(0x1) = CONST 
    0xf28: vf28(0xa0) = CONST 
    0xf2a: vf2a(0x10000000000000000000000000000000000000000) = SHL vf28(0xa0), vf26(0x1)
    0xf2b: vf2b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf2a(0x10000000000000000000000000000000000000000), vf24(0x1)
    0xf2c: vf2c = AND vf2b(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0xf2e: vf2e(0x1) = CONST 
    0xf30: vf30(0x1) = CONST 
    0xf32: vf32(0xa0) = CONST 
    0xf34: vf34(0x10000000000000000000000000000000000000000) = SHL vf32(0xa0), vf30(0x1)
    0xf35: vf35(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf34(0x10000000000000000000000000000000000000000), vf2e(0x1)
    0xf36: vf36 = AND vf35(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0xf37: vf37(0x8f8d7c53451d5aabbe44bf954d56365e820625c71aef530b64195b6e906a3e24) = CONST 
    0xf5a: vf5a(0x40) = CONST 
    0xf5c: vf5c = MLOAD vf5a(0x40)
    0xf60: MSTORE vf5c, v3ce
    0xf61: vf61(0x20) = CONST 
    0xf63: vf63 = ADD vf61(0x20), vf5c
    0xf65: vf65(0x20) = CONST 
    0xf67: vf67 = ADD vf65(0x20), vf63
    0xf6a: vf6a(0x40) = SUB vf67, vf5c
    0xf6c: MSTORE vf63, vf6a(0x40)
    0xf70: vf70 = MLOAD v43d
    0xf72: MSTORE vf67, vf70
    0xf73: vf73(0x20) = CONST 
    0xf75: vf75 = ADD vf73(0x20), vf67
    0xf79: vf79 = MLOAD v43d
    0xf7b: vf7b(0x20) = CONST 
    0xf7d: vf7d = ADD vf7b(0x20), v43d
    0xf82: vf82(0x0) = CONST 

    Begin block 0xf84
    prev=[0xf14, 0xf8d], succ=[0xf9c, 0xf8d]
    =================================
    0xf84_0x0: vf84_0 = PHI vf82(0x0), vf97
    0xf87: vf87 = LT vf84_0, vf79
    0xf88: vf88 = ISZERO vf87
    0xf89: vf89(0xf9c) = CONST 
    0xf8c: JUMPI vf89(0xf9c), vf88

    Begin block 0xf9c
    prev=[0xf84], succ=[0xfc9, 0xfb0]
    =================================
    0xfa5: vfa5 = ADD vf79, vf75
    0xfa7: vfa7(0x1f) = CONST 
    0xfa9: vfa9 = AND vfa7(0x1f), vf79
    0xfab: vfab = ISZERO vfa9
    0xfac: vfac(0xfc9) = CONST 
    0xfaf: JUMPI vfac(0xfc9), vfab

    Begin block 0xfc9
    prev=[0xf9c, 0xfb0], succ=[0xfd8]
    =================================
    0xfc9_0x1: vfc9_1 = PHI vfa5, vfc6
    0xfd0: vfd0(0x40) = CONST 
    0xfd2: vfd2 = MLOAD vfd0(0x40)
    0xfd5: vfd5 = SUB vfc9_1, vfd2
    0xfd7: LOG3 vfd2, vfd5, vf37(0x8f8d7c53451d5aabbe44bf954d56365e820625c71aef530b64195b6e906a3e24), vf36, vf2c

    Begin block 0xfb0
    prev=[0xf9c], succ=[0xfc9]
    =================================
    0xfb2: vfb2 = SUB vfa5, vfa9
    0xfb4: vfb4 = MLOAD vfb2
    0xfb5: vfb5(0x1) = CONST 
    0xfb8: vfb8(0x20) = CONST 
    0xfba: vfba = SUB vfb8(0x20), vfa9
    0xfbb: vfbb(0x100) = CONST 
    0xfbe: vfbe = EXP vfbb(0x100), vfba
    0xfbf: vfbf = SUB vfbe, vfb5(0x1)
    0xfc0: vfc0 = NOT vfbf
    0xfc1: vfc1 = AND vfc0, vfb4
    0xfc3: MSTORE vfb2, vfc1
    0xfc4: vfc4(0x20) = CONST 
    0xfc6: vfc6 = ADD vfc4(0x20), vfb2

    Begin block 0xf8d
    prev=[0xf84], succ=[0xf84]
    =================================
    0xf8d_0x0: vf8d_0 = PHI vf82(0x0), vf97
    0xf8f: vf8f = ADD vf8d_0, vf7d
    0xf90: vf90 = MLOAD vf8f
    0xf93: vf93 = ADD vf8d_0, vf75
    0xf94: MSTORE vf93, vf90
    0xf95: vf95(0x20) = CONST 
    0xf97: vf97 = ADD vf95(0x20), vf8d_0
    0xf98: vf98(0xf84) = CONST 
    0xf9b: JUMP vf98(0xf84)

    Begin block 0xefb
    prev=[0xee7], succ=[0xf14]
    =================================
    0xefd: vefd = SUB vef0, vef4
    0xeff: veff = MLOAD vefd
    0xf00: vf00(0x1) = CONST 
    0xf03: vf03(0x20) = CONST 
    0xf05: vf05 = SUB vf03(0x20), vef4
    0xf06: vf06(0x100) = CONST 
    0xf09: vf09 = EXP vf06(0x100), vf05
    0xf0a: vf0a = SUB vf09, vf00(0x1)
    0xf0b: vf0b = NOT vf0a
    0xf0c: vf0c = AND vf0b, veff
    0xf0e: MSTORE vefd, vf0c
    0xf0f: vf0f(0x20) = CONST 
    0xf11: vf11 = ADD vf0f(0x20), vefd

    Begin block 0xed8
    prev=[0xecf], succ=[0xecf]
    =================================
    0xed8_0x0: ved8_0 = PHI vecd(0x0), vee2
    0xeda: veda = ADD ved8_0, vec8
    0xedb: vedb = MLOAD veda
    0xede: vede = ADD ved8_0, vec4
    0xedf: MSTORE vede, vedb
    0xee0: vee0(0x20) = CONST 
    0xee2: vee2 = ADD vee0(0x20), ved8_0
    0xee3: vee3(0xecf) = CONST 
    0xee6: JUMP vee3(0xecf)

    Begin block 0xd1b
    prev=[0xcdc], succ=[0xd7c]
    =================================
    0xd1c: vd1c(0x1) = CONST 
    0xd1e: vd1e(0x1) = CONST 
    0xd20: vd20(0xa0) = CONST 
    0xd22: vd22(0x10000000000000000000000000000000000000000) = SHL vd20(0xa0), vd1e(0x1)
    0xd23: vd23(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd22(0x10000000000000000000000000000000000000000), vd1c(0x1)
    0xd24: vd24 = AND vd23(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0xd26: vd26(0x1) = CONST 
    0xd28: vd28(0x1) = CONST 
    0xd2a: vd2a(0xa0) = CONST 
    0xd2c: vd2c(0x10000000000000000000000000000000000000000) = SHL vd2a(0xa0), vd28(0x1)
    0xd2d: vd2d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd2c(0x10000000000000000000000000000000000000000), vd26(0x1)
    0xd2e: vd2e = AND vd2d(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0xd2f: vd2f(0x512048caf7808c7bd5eec84574a0698613ae07a6d5a1c6fd389d451658ef379b) = CONST 
    0xd52: vd52(0x40) = CONST 
    0xd54: vd54 = MLOAD vd52(0x40)
    0xd58: MSTORE vd54, v3ce
    0xd59: vd59(0x20) = CONST 
    0xd5b: vd5b = ADD vd59(0x20), vd54
    0xd5d: vd5d(0x20) = CONST 
    0xd5f: vd5f = ADD vd5d(0x20), vd5b
    0xd62: vd62(0x40) = SUB vd5f, vd54
    0xd64: MSTORE vd5b, vd62(0x40)
    0xd68: vd68 = MLOAD v43d
    0xd6a: MSTORE vd5f, vd68
    0xd6b: vd6b(0x20) = CONST 
    0xd6d: vd6d = ADD vd6b(0x20), vd5f
    0xd71: vd71 = MLOAD v43d
    0xd73: vd73(0x20) = CONST 
    0xd75: vd75 = ADD vd73(0x20), v43d
    0xd7a: vd7a(0x0) = CONST 

    Begin block 0xd7c
    prev=[0xd1b, 0xd85], succ=[0xd94, 0xd85]
    =================================
    0xd7c_0x0: vd7c_0 = PHI vd7a(0x0), vd8f
    0xd7f: vd7f = LT vd7c_0, vd71
    0xd80: vd80 = ISZERO vd7f
    0xd81: vd81(0xd94) = CONST 
    0xd84: JUMPI vd81(0xd94), vd80

    Begin block 0xd94
    prev=[0xd7c], succ=[0xdc1, 0xda8]
    =================================
    0xd9d: vd9d = ADD vd71, vd6d
    0xd9f: vd9f(0x1f) = CONST 
    0xda1: vda1 = AND vd9f(0x1f), vd71
    0xda3: vda3 = ISZERO vda1
    0xda4: vda4(0xdc1) = CONST 
    0xda7: JUMPI vda4(0xdc1), vda3

    Begin block 0xdc1
    prev=[0xd94, 0xda8], succ=[0xfd8]
    =================================
    0xdc1_0x1: vdc1_1 = PHI vd9d, vdbe
    0xdc8: vdc8(0x40) = CONST 
    0xdca: vdca = MLOAD vdc8(0x40)
    0xdcd: vdcd = SUB vdc1_1, vdca
    0xdcf: LOG3 vdca, vdcd, vd2f(0x512048caf7808c7bd5eec84574a0698613ae07a6d5a1c6fd389d451658ef379b), vd2e, vd24
    0xdd0: vdd0(0xfd8) = CONST 
    0xdd3: JUMP vdd0(0xfd8)

    Begin block 0xda8
    prev=[0xd94], succ=[0xdc1]
    =================================
    0xdaa: vdaa = SUB vd9d, vda1
    0xdac: vdac = MLOAD vdaa
    0xdad: vdad(0x1) = CONST 
    0xdb0: vdb0(0x20) = CONST 
    0xdb2: vdb2 = SUB vdb0(0x20), vda1
    0xdb3: vdb3(0x100) = CONST 
    0xdb6: vdb6 = EXP vdb3(0x100), vdb2
    0xdb7: vdb7 = SUB vdb6, vdad(0x1)
    0xdb8: vdb8 = NOT vdb7
    0xdb9: vdb9 = AND vdb8, vdac
    0xdbb: MSTORE vdaa, vdb9
    0xdbc: vdbc(0x20) = CONST 
    0xdbe: vdbe = ADD vdbc(0x20), vdaa

    Begin block 0xd85
    prev=[0xd7c], succ=[0xd7c]
    =================================
    0xd85_0x0: vd85_0 = PHI vd7a(0x0), vd8f
    0xd87: vd87 = ADD vd85_0, vd75
    0xd88: vd88 = MLOAD vd87
    0xd8b: vd8b = ADD vd85_0, vd6d
    0xd8c: MSTORE vd8b, vd88
    0xd8d: vd8d(0x20) = CONST 
    0xd8f: vd8f = ADD vd8d(0x20), vd85_0
    0xd90: vd90(0xd7c) = CONST 
    0xd93: JUMP vd90(0xd7c)

    Begin block 0x2165B0xbfd
    prev=[0x2143B0xbfd], succ=[0x2124B0xbfd]
    =================================
    0x2165_0x0S0xbfd: v2165_0Vbfd = PHI v2122Vbfd(0x0), v2168Vbfd
    0x2166S0xbfd: v2166Vbfd(0x1) = CONST 
    0x2168S0xbfd: v2168Vbfd = ADD v2166Vbfd(0x1), v2165_0Vbfd
    0x2169S0xbfd: v2169Vbfd(0x2124) = CONST 
    0x216cS0xbfd: JUMP v2169Vbfd(0x2124)

    Begin block 0x2142B0xbfd
    prev=[0x212eB0xbfd], succ=[]
    =================================
    0x2142S0xbfd: THROW 

    Begin block 0x216dB0xbfd
    prev=[0x2124B0xbfd], succ=[0x2174B0xbfd]
    =================================
    0x216fS0xbfd: v216fVbfd(0x0) = CONST 

    Begin block 0xbe7
    prev=[0xbde], succ=[0xbde]
    =================================
    0xbe7_0x0: vbe7_0 = PHI vbd9, vbf8
    0xbe7_0x1: vbe7_1 = PHI vbd2, vbf6
    0xbe7_0x2: vbe7_2 = PHI vbd5, vbf0
    0xbe8: vbe8 = MLOAD vbe7_0
    0xbea: MSTORE vbe7_1, vbe8
    0xbeb: vbeb(0x1f) = CONST 
    0xbed: vbed(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vbeb(0x1f)
    0xbf0: vbf0 = ADD vbe7_2, vbed(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xbf2: vbf2(0x20) = CONST 
    0xbf6: vbf6 = ADD vbf2(0x20), vbe7_1
    0xbf8: vbf8 = ADD vbf2(0x20), vbe7_0
    0xbf9: vbf9(0xbde) = CONST 
    0xbfc: JUMP vbf9(0xbde)

}

function unpause()() public {
    Begin block 0x46b
    prev=[], succ=[0x473, 0x477]
    =================================
    0x46c: v46c = CALLVALUE 
    0x46e: v46e = ISZERO v46c
    0x46f: v46f(0x477) = CONST 
    0x472: JUMPI v46f(0x477), v46e

    Begin block 0x473
    prev=[0x46b], succ=[]
    =================================
    0x473: v473(0x0) = CONST 
    0x476: REVERT v473(0x0), v473(0x0)

    Begin block 0x477
    prev=[0x46b], succ=[0xfe7]
    =================================
    0x479: v479(0x27d4) = CONST 
    0x47c: v47c(0xfe7) = CONST 
    0x47f: JUMP v47c(0xfe7)

    Begin block 0xfe7
    prev=[0x477], succ=[0xff2, 0x1035]
    =================================
    0xfe8: vfe8(0xf) = CONST 
    0xfea: vfea = SLOAD vfe8(0xf)
    0xfeb: vfeb(0xff) = CONST 
    0xfed: vfed = AND vfeb(0xff), vfea
    0xfee: vfee(0x1035) = CONST 
    0xff1: JUMPI vfee(0x1035), vfed

    Begin block 0xff2
    prev=[0xfe7], succ=[]
    =================================
    0xff2: vff2(0x40) = CONST 
    0xff5: vff5 = MLOAD vff2(0x40)
    0xff6: vff6(0x461bcd) = CONST 
    0xffa: vffa(0xe5) = CONST 
    0xffc: vffc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vffa(0xe5), vff6(0x461bcd)
    0xffe: MSTORE vff5, vffc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xfff: vfff(0x20) = CONST 
    0x1001: v1001(0x4) = CONST 
    0x1004: v1004 = ADD vff5, v1001(0x4)
    0x1005: MSTORE v1004, vfff(0x20)
    0x1006: v1006(0x14) = CONST 
    0x1008: v1008(0x24) = CONST 
    0x100b: v100b = ADD vff5, v1008(0x24)
    0x100c: MSTORE v100b, v1006(0x14)
    0x100d: v100d(0x14185d5cd8589b194e881b9bdd081c185d5cd959) = CONST 
    0x1022: v1022(0x62) = CONST 
    0x1024: v1024(0x5061757361626c653a206e6f7420706175736564000000000000000000000000) = SHL v1022(0x62), v100d(0x14185d5cd8589b194e881b9bdd081c185d5cd959)
    0x1025: v1025(0x44) = CONST 
    0x1028: v1028 = ADD vff5, v1025(0x44)
    0x1029: MSTORE v1028, v1024(0x5061757361626c653a206e6f7420706175736564000000000000000000000000)
    0x102b: v102b = MLOAD vff2(0x40)
    0x102f: v102f(0x0) = SUB vff5, v102b
    0x1030: v1030(0x64) = CONST 
    0x1032: v1032(0x64) = ADD v1030(0x64), v102f(0x0)
    0x1034: REVERT v102b, v1032(0x64)

    Begin block 0x1035
    prev=[0xfe7], succ=[0x227eB0x1035]
    =================================
    0x1036: v1036(0x103d) = CONST 
    0x1039: v1039(0x227e) = CONST 
    0x103c: JUMP v1039(0x227e)

    Begin block 0x227eB0x1035
    prev=[0x1035], succ=[0x103d]
    =================================
    0x227fS0x1035: v227fV1035 = CALLER 
    0x2281S0x1035: JUMP v1036(0x103d)

    Begin block 0x103d
    prev=[0x227eB0x1035], succ=[0x16ffB0x103d]
    =================================
    0x103e: v103e(0x1) = CONST 
    0x1040: v1040(0x1) = CONST 
    0x1042: v1042(0xa0) = CONST 
    0x1044: v1044(0x10000000000000000000000000000000000000000) = SHL v1042(0xa0), v1040(0x1)
    0x1045: v1045(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1044(0x10000000000000000000000000000000000000000), v103e(0x1)
    0x1046: v1046 = AND v1045(0xffffffffffffffffffffffffffffffffffffffff), v227fV1035
    0x1047: v1047(0x104e) = CONST 
    0x104a: v104a(0x16ff) = CONST 
    0x104d: JUMP v104a(0x16ff)

    Begin block 0x16ffB0x103d
    prev=[0x103d], succ=[0x104e]
    =================================
    0x1700S0x103d: v1700V103d(0x0) = CONST 
    0x1702S0x103d: v1702V103d = SLOAD v1700V103d(0x0)
    0x1703S0x103d: v1703V103d(0x1) = CONST 
    0x1705S0x103d: v1705V103d(0x1) = CONST 
    0x1707S0x103d: v1707V103d(0xa0) = CONST 
    0x1709S0x103d: v1709V103d(0x10000000000000000000000000000000000000000) = SHL v1707V103d(0xa0), v1705V103d(0x1)
    0x170aS0x103d: v170aV103d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V103d(0x10000000000000000000000000000000000000000), v1703V103d(0x1)
    0x170bS0x103d: v170bV103d = AND v170aV103d(0xffffffffffffffffffffffffffffffffffffffff), v1702V103d
    0x170dS0x103d: JUMP v1047(0x104e)

    Begin block 0x104e
    prev=[0x16ffB0x103d], succ=[0x105d, 0x1097]
    =================================
    0x104f: v104f(0x1) = CONST 
    0x1051: v1051(0x1) = CONST 
    0x1053: v1053(0xa0) = CONST 
    0x1055: v1055(0x10000000000000000000000000000000000000000) = SHL v1053(0xa0), v1051(0x1)
    0x1056: v1056(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1055(0x10000000000000000000000000000000000000000), v104f(0x1)
    0x1057: v1057 = AND v1056(0xffffffffffffffffffffffffffffffffffffffff), v170bV103d
    0x1058: v1058 = EQ v1057, v1046
    0x1059: v1059(0x1097) = CONST 
    0x105c: JUMPI v1059(0x1097), v1058

    Begin block 0x105d
    prev=[0x104e], succ=[]
    =================================
    0x105d: v105d(0x40) = CONST 
    0x1060: v1060 = MLOAD v105d(0x40)
    0x1061: v1061(0x461bcd) = CONST 
    0x1065: v1065(0xe5) = CONST 
    0x1067: v1067(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1065(0xe5), v1061(0x461bcd)
    0x1069: MSTORE v1060, v1067(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x106a: v106a(0x20) = CONST 
    0x106c: v106c(0x4) = CONST 
    0x106f: v106f = ADD v1060, v106c(0x4)
    0x1072: MSTORE v106f, v106a(0x20)
    0x1073: v1073(0x24) = CONST 
    0x1076: v1076 = ADD v1060, v1073(0x24)
    0x1077: MSTORE v1076, v106a(0x20)
    0x1078: v1078(0x0) = CONST 
    0x107b: v107b = MLOAD v1078(0x0)
    0x107c: v107c(0x20) = CONST 
    0x107e: v107e(0x255c) = CONST 
    0x1086: MSTORE v1078(0x0), v107b
    0x1087: v1087(0x44) = CONST 
    0x108a: v108a = ADD v1060, v1087(0x44)
    0x108b: MSTORE v108a, v2e1f(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x108d: v108d = MLOAD v105d(0x40)
    0x1091: v1091(0x0) = SUB v1060, v108d
    0x1092: v1092(0x64) = CONST 
    0x1094: v1094(0x64) = ADD v1092(0x64), v1091(0x0)
    0x1096: REVERT v108d, v1094(0x64)
    0x2e1f: v2e1f(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1097
    prev=[0x104e], succ=[0x27d4]
    =================================
    0x1098: v1098(0xf) = CONST 
    0x109b: v109b = SLOAD v1098(0xf)
    0x109c: v109c(0xff) = CONST 
    0x109e: v109e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v109c(0xff)
    0x109f: v109f = AND v109e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v109b
    0x10a1: SSTORE v1098(0xf), v109f
    0x10a2: v10a2(0x40) = CONST 
    0x10a5: v10a5 = MLOAD v10a2(0x40)
    0x10a6: v10a6 = CALLER 
    0x10a8: MSTORE v10a5, v10a6
    0x10aa: v10aa = MLOAD v10a2(0x40)
    0x10ab: v10ab(0x5db9ee0a495bf2e6ff9c91a7834c1ba4fdd244a5e8aa4e537bd38aeae4b073aa) = CONST 
    0x10cf: v10cf(0x0) = SUB v10a5, v10aa
    0x10d0: v10d0(0x20) = CONST 
    0x10d2: v10d2(0x20) = ADD v10d0(0x20), v10cf(0x0)
    0x10d4: LOG1 v10aa, v10d2(0x20), v10ab(0x5db9ee0a495bf2e6ff9c91a7834c1ba4fdd244a5e8aa4e537bd38aeae4b073aa)
    0x10d5: JUMP v479(0x27d4)

    Begin block 0x27d4
    prev=[0x1097], succ=[]
    =================================
    0x27d5: STOP 

}

function minAmount(address)() public {
    Begin block 0x480
    prev=[], succ=[0x488, 0x48c]
    =================================
    0x481: v481 = CALLVALUE 
    0x483: v483 = ISZERO v481
    0x484: v484(0x48c) = CONST 
    0x487: JUMPI v484(0x48c), v483

    Begin block 0x488
    prev=[0x480], succ=[]
    =================================
    0x488: v488(0x0) = CONST 
    0x48b: REVERT v488(0x0), v488(0x0)

    Begin block 0x48c
    prev=[0x480], succ=[0x49f, 0x4a3]
    =================================
    0x48e: v48e(0x27f5) = CONST 
    0x491: v491(0x4) = CONST 
    0x494: v494 = CALLDATASIZE 
    0x495: v495 = SUB v494, v491(0x4)
    0x496: v496(0x20) = CONST 
    0x499: v499 = LT v495, v496(0x20)
    0x49a: v49a = ISZERO v499
    0x49b: v49b(0x4a3) = CONST 
    0x49e: JUMPI v49b(0x4a3), v49a

    Begin block 0x49f
    prev=[0x48c], succ=[]
    =================================
    0x49f: v49f(0x0) = CONST 
    0x4a2: REVERT v49f(0x0), v49f(0x0)

    Begin block 0x4a3
    prev=[0x48c], succ=[0x10d6]
    =================================
    0x4a5: v4a5 = CALLDATALOAD v491(0x4)
    0x4a6: v4a6(0x1) = CONST 
    0x4a8: v4a8(0x1) = CONST 
    0x4aa: v4aa(0xa0) = CONST 
    0x4ac: v4ac(0x10000000000000000000000000000000000000000) = SHL v4aa(0xa0), v4a8(0x1)
    0x4ad: v4ad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ac(0x10000000000000000000000000000000000000000), v4a6(0x1)
    0x4ae: v4ae = AND v4ad(0xffffffffffffffffffffffffffffffffffffffff), v4a5
    0x4af: v4af(0x10d6) = CONST 
    0x4b2: JUMP v4af(0x10d6)

    Begin block 0x10d6
    prev=[0x4a3], succ=[0x27f5]
    =================================
    0x10d7: v10d7(0xb) = CONST 
    0x10d9: v10d9(0x20) = CONST 
    0x10db: MSTORE v10d9(0x20), v10d7(0xb)
    0x10dc: v10dc(0x0) = CONST 
    0x10e0: MSTORE v10dc(0x0), v4ae
    0x10e1: v10e1(0x40) = CONST 
    0x10e4: v10e4 = SHA3 v10dc(0x0), v10e1(0x40)
    0x10e5: v10e5 = SLOAD v10e4
    0x10e7: JUMP v48e(0x27f5)

    Begin block 0x27f5
    prev=[0x10d6], succ=[]
    =================================
    0x27f6: v27f6(0x40) = CONST 
    0x27f9: v27f9 = MLOAD v27f6(0x40)
    0x27fc: MSTORE v27f9, v10e5
    0x27fd: v27fd = MLOAD v27f6(0x40)
    0x2801: v2801(0x0) = SUB v27f9, v27fd
    0x2802: v2802(0x20) = CONST 
    0x2804: v2804(0x20) = ADD v2802(0x20), v2801(0x0)
    0x2806: RETURN v27fd, v2804(0x20)

}

function setAcceptChain(uint8,bool)() public {
    Begin block 0x4b3
    prev=[], succ=[0x4bb, 0x4bf]
    =================================
    0x4b4: v4b4 = CALLVALUE 
    0x4b6: v4b6 = ISZERO v4b4
    0x4b7: v4b7(0x4bf) = CONST 
    0x4ba: JUMPI v4b7(0x4bf), v4b6

    Begin block 0x4bb
    prev=[0x4b3], succ=[]
    =================================
    0x4bb: v4bb(0x0) = CONST 
    0x4be: REVERT v4bb(0x0), v4bb(0x0)

    Begin block 0x4bf
    prev=[0x4b3], succ=[0x4d2, 0x4d6]
    =================================
    0x4c1: v4c1(0x2826) = CONST 
    0x4c4: v4c4(0x4) = CONST 
    0x4c7: v4c7 = CALLDATASIZE 
    0x4c8: v4c8 = SUB v4c7, v4c4(0x4)
    0x4c9: v4c9(0x40) = CONST 
    0x4cc: v4cc = LT v4c8, v4c9(0x40)
    0x4cd: v4cd = ISZERO v4cc
    0x4ce: v4ce(0x4d6) = CONST 
    0x4d1: JUMPI v4ce(0x4d6), v4cd

    Begin block 0x4d2
    prev=[0x4bf], succ=[]
    =================================
    0x4d2: v4d2(0x0) = CONST 
    0x4d5: REVERT v4d2(0x0), v4d2(0x0)

    Begin block 0x4d6
    prev=[0x4bf], succ=[0x10e8]
    =================================
    0x4d8: v4d8(0xff) = CONST 
    0x4db: v4db = CALLDATALOAD v4c4(0x4)
    0x4dc: v4dc = AND v4db, v4d8(0xff)
    0x4de: v4de(0x20) = CONST 
    0x4e0: v4e0(0x24) = ADD v4de(0x20), v4c4(0x4)
    0x4e1: v4e1 = CALLDATALOAD v4e0(0x24)
    0x4e2: v4e2 = ISZERO v4e1
    0x4e3: v4e3 = ISZERO v4e2
    0x4e4: v4e4(0x10e8) = CONST 
    0x4e7: JUMP v4e4(0x10e8)

    Begin block 0x10e8
    prev=[0x4d6], succ=[0x227eB0x10e8]
    =================================
    0x10e9: v10e9(0x10f0) = CONST 
    0x10ec: v10ec(0x227e) = CONST 
    0x10ef: JUMP v10ec(0x227e)

    Begin block 0x227eB0x10e8
    prev=[0x10e8], succ=[0x10f0]
    =================================
    0x227fS0x10e8: v227fV10e8 = CALLER 
    0x2281S0x10e8: JUMP v10e9(0x10f0)

    Begin block 0x10f0
    prev=[0x227eB0x10e8], succ=[0x16ffB0x10f0]
    =================================
    0x10f1: v10f1(0x1) = CONST 
    0x10f3: v10f3(0x1) = CONST 
    0x10f5: v10f5(0xa0) = CONST 
    0x10f7: v10f7(0x10000000000000000000000000000000000000000) = SHL v10f5(0xa0), v10f3(0x1)
    0x10f8: v10f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10f7(0x10000000000000000000000000000000000000000), v10f1(0x1)
    0x10f9: v10f9 = AND v10f8(0xffffffffffffffffffffffffffffffffffffffff), v227fV10e8
    0x10fa: v10fa(0x1101) = CONST 
    0x10fd: v10fd(0x16ff) = CONST 
    0x1100: JUMP v10fd(0x16ff)

    Begin block 0x16ffB0x10f0
    prev=[0x10f0], succ=[0x1101]
    =================================
    0x1700S0x10f0: v1700V10f0(0x0) = CONST 
    0x1702S0x10f0: v1702V10f0 = SLOAD v1700V10f0(0x0)
    0x1703S0x10f0: v1703V10f0(0x1) = CONST 
    0x1705S0x10f0: v1705V10f0(0x1) = CONST 
    0x1707S0x10f0: v1707V10f0(0xa0) = CONST 
    0x1709S0x10f0: v1709V10f0(0x10000000000000000000000000000000000000000) = SHL v1707V10f0(0xa0), v1705V10f0(0x1)
    0x170aS0x10f0: v170aV10f0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V10f0(0x10000000000000000000000000000000000000000), v1703V10f0(0x1)
    0x170bS0x10f0: v170bV10f0 = AND v170aV10f0(0xffffffffffffffffffffffffffffffffffffffff), v1702V10f0
    0x170dS0x10f0: JUMP v10fa(0x1101)

    Begin block 0x1101
    prev=[0x16ffB0x10f0], succ=[0x1110, 0x114a]
    =================================
    0x1102: v1102(0x1) = CONST 
    0x1104: v1104(0x1) = CONST 
    0x1106: v1106(0xa0) = CONST 
    0x1108: v1108(0x10000000000000000000000000000000000000000) = SHL v1106(0xa0), v1104(0x1)
    0x1109: v1109(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1108(0x10000000000000000000000000000000000000000), v1102(0x1)
    0x110a: v110a = AND v1109(0xffffffffffffffffffffffffffffffffffffffff), v170bV10f0
    0x110b: v110b = EQ v110a, v10f9
    0x110c: v110c(0x114a) = CONST 
    0x110f: JUMPI v110c(0x114a), v110b

    Begin block 0x1110
    prev=[0x1101], succ=[]
    =================================
    0x1110: v1110(0x40) = CONST 
    0x1113: v1113 = MLOAD v1110(0x40)
    0x1114: v1114(0x461bcd) = CONST 
    0x1118: v1118(0xe5) = CONST 
    0x111a: v111a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1118(0xe5), v1114(0x461bcd)
    0x111c: MSTORE v1113, v111a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x111d: v111d(0x20) = CONST 
    0x111f: v111f(0x4) = CONST 
    0x1122: v1122 = ADD v1113, v111f(0x4)
    0x1125: MSTORE v1122, v111d(0x20)
    0x1126: v1126(0x24) = CONST 
    0x1129: v1129 = ADD v1113, v1126(0x24)
    0x112a: MSTORE v1129, v111d(0x20)
    0x112b: v112b(0x0) = CONST 
    0x112e: v112e = MLOAD v112b(0x0)
    0x112f: v112f(0x20) = CONST 
    0x1131: v1131(0x255c) = CONST 
    0x1139: MSTORE v112b(0x0), v112e
    0x113a: v113a(0x44) = CONST 
    0x113d: v113d = ADD v1113, v113a(0x44)
    0x113e: MSTORE v113d, v2e24(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1140: v1140 = MLOAD v1110(0x40)
    0x1144: v1144(0x0) = SUB v1113, v1140
    0x1145: v1145(0x64) = CONST 
    0x1147: v1147(0x64) = ADD v1145(0x64), v1144(0x0)
    0x1149: REVERT v1140, v1147(0x64)
    0x2e24: v2e24(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x114a
    prev=[0x1101], succ=[0x115a, 0x115b]
    =================================
    0x114c: v114c(0x5) = CONST 
    0x114e: v114e(0x0) = CONST 
    0x1151: v1151(0x2) = CONST 
    0x1154: v1154 = GT v4dc, v1151(0x2)
    0x1155: v1155 = ISZERO v1154
    0x1156: v1156(0x115b) = CONST 
    0x1159: JUMPI v1156(0x115b), v1155

    Begin block 0x115a
    prev=[0x114a], succ=[]
    =================================
    0x115a: THROW 

    Begin block 0x115b
    prev=[0x114a], succ=[0x1165, 0x1166]
    =================================
    0x115c: v115c(0x2) = CONST 
    0x115f: v115f = GT v4dc, v115c(0x2)
    0x1160: v1160 = ISZERO v115f
    0x1161: v1161(0x1166) = CONST 
    0x1164: JUMPI v1161(0x1166), v1160

    Begin block 0x1165
    prev=[0x115b], succ=[]
    =================================
    0x1165: THROW 

    Begin block 0x1166
    prev=[0x115b], succ=[0x11bd, 0x11be]
    =================================
    0x1168: MSTORE v114e(0x0), v4dc
    0x1169: v1169(0x20) = CONST 
    0x116b: v116b(0x20) = ADD v1169(0x20), v114e(0x0)
    0x116e: MSTORE v116b(0x20), v114c(0x5)
    0x116f: v116f(0x20) = CONST 
    0x1171: v1171(0x40) = ADD v116f(0x20), v116b(0x20)
    0x1172: v1172(0x0) = CONST 
    0x1174: v1174 = SHA3 v1172(0x0), v1171(0x40)
    0x1175: v1175(0x0) = CONST 
    0x1177: v1177(0x100) = CONST 
    0x117a: v117a(0x1) = EXP v1177(0x100), v1175(0x0)
    0x117c: v117c = SLOAD v1174
    0x117e: v117e(0xff) = CONST 
    0x1180: v1180(0xff) = MUL v117e(0xff), v117a(0x1)
    0x1181: v1181(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1180(0xff)
    0x1182: v1182 = AND v1181(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v117c
    0x1185: v1185 = ISZERO v4e3
    0x1186: v1186 = ISZERO v1185
    0x1187: v1187 = MUL v1186, v117a(0x1)
    0x1188: v1188 = OR v1187, v1182
    0x118a: SSTORE v1174, v1188
    0x118c: v118c(0x3752f35a68b1dabe79ab9080972fe005f18f6c881bf575eea68d915431ffe540) = CONST 
    0x11af: v11af(0x40) = CONST 
    0x11b1: v11b1 = MLOAD v11af(0x40)
    0x11b4: v11b4(0x2) = CONST 
    0x11b7: v11b7 = GT v4dc, v11b4(0x2)
    0x11b8: v11b8 = ISZERO v11b7
    0x11b9: v11b9(0x11be) = CONST 
    0x11bc: JUMPI v11b9(0x11be), v11b8

    Begin block 0x11bd
    prev=[0x1166], succ=[]
    =================================
    0x11bd: THROW 

    Begin block 0x11be
    prev=[0x1166], succ=[0x2826]
    =================================
    0x11c0: MSTORE v11b1, v4dc
    0x11c2: v11c2 = ISZERO v4e3
    0x11c3: v11c3 = ISZERO v11c2
    0x11c4: v11c4(0x20) = CONST 
    0x11c7: v11c7 = ADD v11b1, v11c4(0x20)
    0x11c8: MSTORE v11c7, v11c3
    0x11ca: v11ca(0x40) = CONST 
    0x11cd: v11cd = MLOAD v11ca(0x40)
    0x11d1: v11d1(0x0) = SUB v11b1, v11cd
    0x11d2: v11d2(0x40) = ADD v11d1(0x0), v11ca(0x40)
    0x11d5: LOG1 v11cd, v11d2(0x40), v118c(0x3752f35a68b1dabe79ab9080972fe005f18f6c881bf575eea68d915431ffe540)
    0x11d8: JUMP v4c1(0x2826)

    Begin block 0x2826
    prev=[0x11be], succ=[]
    =================================
    0x2827: STOP 

}

function implementation()() public {
    Begin block 0x4e8
    prev=[], succ=[0x4f0, 0x4f4]
    =================================
    0x4e9: v4e9 = CALLVALUE 
    0x4eb: v4eb = ISZERO v4e9
    0x4ec: v4ec(0x4f4) = CONST 
    0x4ef: JUMPI v4ec(0x4f4), v4eb

    Begin block 0x4f0
    prev=[0x4e8], succ=[]
    =================================
    0x4f0: v4f0(0x0) = CONST 
    0x4f3: REVERT v4f0(0x0), v4f0(0x0)

    Begin block 0x4f4
    prev=[0x4e8], succ=[0x11d9]
    =================================
    0x4f6: v4f6(0x2847) = CONST 
    0x4f9: v4f9(0x11d9) = CONST 
    0x4fc: JUMP v4f9(0x11d9)

    Begin block 0x11d9
    prev=[0x4f4], succ=[0x2847]
    =================================
    0x11da: v11da(0x2) = CONST 
    0x11dc: v11dc = SLOAD v11da(0x2)
    0x11dd: v11dd(0x1) = CONST 
    0x11df: v11df(0x1) = CONST 
    0x11e1: v11e1(0xa0) = CONST 
    0x11e3: v11e3(0x10000000000000000000000000000000000000000) = SHL v11e1(0xa0), v11df(0x1)
    0x11e4: v11e4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11e3(0x10000000000000000000000000000000000000000), v11dd(0x1)
    0x11e5: v11e5 = AND v11e4(0xffffffffffffffffffffffffffffffffffffffff), v11dc
    0x11e7: JUMP v4f6(0x2847)

    Begin block 0x2847
    prev=[0x11d9], succ=[]
    =================================
    0x2848: v2848(0x40) = CONST 
    0x284b: v284b = MLOAD v2848(0x40)
    0x284c: v284c(0x1) = CONST 
    0x284e: v284e(0x1) = CONST 
    0x2850: v2850(0xa0) = CONST 
    0x2852: v2852(0x10000000000000000000000000000000000000000) = SHL v2850(0xa0), v284e(0x1)
    0x2853: v2853(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2852(0x10000000000000000000000000000000000000000), v284c(0x1)
    0x2856: v2856 = AND v11e5, v2853(0xffffffffffffffffffffffffffffffffffffffff)
    0x2858: MSTORE v284b, v2856
    0x2859: v2859 = MLOAD v2848(0x40)
    0x285d: v285d(0x0) = SUB v284b, v2859
    0x285e: v285e(0x20) = CONST 
    0x2860: v2860(0x20) = ADD v285e(0x20), v285d(0x0)
    0x2862: RETURN v2859, v2860(0x20)

}

function paused()() public {
    Begin block 0x4fd
    prev=[], succ=[0x505, 0x509]
    =================================
    0x4fe: v4fe = CALLVALUE 
    0x500: v500 = ISZERO v4fe
    0x501: v501(0x509) = CONST 
    0x504: JUMPI v501(0x509), v500

    Begin block 0x505
    prev=[0x4fd], succ=[]
    =================================
    0x505: v505(0x0) = CONST 
    0x508: REVERT v505(0x0), v505(0x0)

    Begin block 0x509
    prev=[0x4fd], succ=[0x11e8]
    =================================
    0x50b: v50b(0x2882) = CONST 
    0x50e: v50e(0x11e8) = CONST 
    0x511: JUMP v50e(0x11e8)

    Begin block 0x11e8
    prev=[0x509], succ=[0x2882]
    =================================
    0x11e9: v11e9(0xf) = CONST 
    0x11eb: v11eb = SLOAD v11e9(0xf)
    0x11ec: v11ec(0xff) = CONST 
    0x11ee: v11ee = AND v11ec(0xff), v11eb
    0x11f0: JUMP v50b(0x2882)

    Begin block 0x2882
    prev=[0x11e8], succ=[]
    =================================
    0x2883: v2883(0x40) = CONST 
    0x2886: v2886 = MLOAD v2883(0x40)
    0x2888: v2888 = ISZERO v11ee
    0x2889: v2889 = ISZERO v2888
    0x288b: MSTORE v2886, v2889
    0x288c: v288c = MLOAD v2883(0x40)
    0x2890: v2890(0x0) = SUB v2886, v288c
    0x2891: v2891(0x20) = CONST 
    0x2893: v2893(0x20) = ADD v2891(0x20), v2890(0x0)
    0x2895: RETURN v288c, v2893(0x20)

}

function removeRelayer(address)() public {
    Begin block 0x512
    prev=[], succ=[0x51a, 0x51e]
    =================================
    0x513: v513 = CALLVALUE 
    0x515: v515 = ISZERO v513
    0x516: v516(0x51e) = CONST 
    0x519: JUMPI v516(0x51e), v515

    Begin block 0x51a
    prev=[0x512], succ=[]
    =================================
    0x51a: v51a(0x0) = CONST 
    0x51d: REVERT v51a(0x0), v51a(0x0)

    Begin block 0x51e
    prev=[0x512], succ=[0x531, 0x535]
    =================================
    0x520: v520(0x28b5) = CONST 
    0x523: v523(0x4) = CONST 
    0x526: v526 = CALLDATASIZE 
    0x527: v527 = SUB v526, v523(0x4)
    0x528: v528(0x20) = CONST 
    0x52b: v52b = LT v527, v528(0x20)
    0x52c: v52c = ISZERO v52b
    0x52d: v52d(0x535) = CONST 
    0x530: JUMPI v52d(0x535), v52c

    Begin block 0x531
    prev=[0x51e], succ=[]
    =================================
    0x531: v531(0x0) = CONST 
    0x534: REVERT v531(0x0), v531(0x0)

    Begin block 0x535
    prev=[0x51e], succ=[0x11f1]
    =================================
    0x537: v537 = CALLDATALOAD v523(0x4)
    0x538: v538(0x1) = CONST 
    0x53a: v53a(0x1) = CONST 
    0x53c: v53c(0xa0) = CONST 
    0x53e: v53e(0x10000000000000000000000000000000000000000) = SHL v53c(0xa0), v53a(0x1)
    0x53f: v53f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53e(0x10000000000000000000000000000000000000000), v538(0x1)
    0x540: v540 = AND v53f(0xffffffffffffffffffffffffffffffffffffffff), v537
    0x541: v541(0x11f1) = CONST 
    0x544: JUMP v541(0x11f1)

    Begin block 0x11f1
    prev=[0x535], succ=[0x227eB0x11f1]
    =================================
    0x11f2: v11f2(0x11f9) = CONST 
    0x11f5: v11f5(0x227e) = CONST 
    0x11f8: JUMP v11f5(0x227e)

    Begin block 0x227eB0x11f1
    prev=[0x11f1], succ=[0x11f9]
    =================================
    0x227fS0x11f1: v227fV11f1 = CALLER 
    0x2281S0x11f1: JUMP v11f2(0x11f9)

    Begin block 0x11f9
    prev=[0x227eB0x11f1], succ=[0x16ffB0x11f9]
    =================================
    0x11fa: v11fa(0x1) = CONST 
    0x11fc: v11fc(0x1) = CONST 
    0x11fe: v11fe(0xa0) = CONST 
    0x1200: v1200(0x10000000000000000000000000000000000000000) = SHL v11fe(0xa0), v11fc(0x1)
    0x1201: v1201(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1200(0x10000000000000000000000000000000000000000), v11fa(0x1)
    0x1202: v1202 = AND v1201(0xffffffffffffffffffffffffffffffffffffffff), v227fV11f1
    0x1203: v1203(0x120a) = CONST 
    0x1206: v1206(0x16ff) = CONST 
    0x1209: JUMP v1206(0x16ff)

    Begin block 0x16ffB0x11f9
    prev=[0x11f9], succ=[0x120a]
    =================================
    0x1700S0x11f9: v1700V11f9(0x0) = CONST 
    0x1702S0x11f9: v1702V11f9 = SLOAD v1700V11f9(0x0)
    0x1703S0x11f9: v1703V11f9(0x1) = CONST 
    0x1705S0x11f9: v1705V11f9(0x1) = CONST 
    0x1707S0x11f9: v1707V11f9(0xa0) = CONST 
    0x1709S0x11f9: v1709V11f9(0x10000000000000000000000000000000000000000) = SHL v1707V11f9(0xa0), v1705V11f9(0x1)
    0x170aS0x11f9: v170aV11f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V11f9(0x10000000000000000000000000000000000000000), v1703V11f9(0x1)
    0x170bS0x11f9: v170bV11f9 = AND v170aV11f9(0xffffffffffffffffffffffffffffffffffffffff), v1702V11f9
    0x170dS0x11f9: JUMP v1203(0x120a)

    Begin block 0x120a
    prev=[0x16ffB0x11f9], succ=[0x1219, 0x1253]
    =================================
    0x120b: v120b(0x1) = CONST 
    0x120d: v120d(0x1) = CONST 
    0x120f: v120f(0xa0) = CONST 
    0x1211: v1211(0x10000000000000000000000000000000000000000) = SHL v120f(0xa0), v120d(0x1)
    0x1212: v1212(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1211(0x10000000000000000000000000000000000000000), v120b(0x1)
    0x1213: v1213 = AND v1212(0xffffffffffffffffffffffffffffffffffffffff), v170bV11f9
    0x1214: v1214 = EQ v1213, v1202
    0x1215: v1215(0x1253) = CONST 
    0x1218: JUMPI v1215(0x1253), v1214

    Begin block 0x1219
    prev=[0x120a], succ=[]
    =================================
    0x1219: v1219(0x40) = CONST 
    0x121c: v121c = MLOAD v1219(0x40)
    0x121d: v121d(0x461bcd) = CONST 
    0x1221: v1221(0xe5) = CONST 
    0x1223: v1223(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1221(0xe5), v121d(0x461bcd)
    0x1225: MSTORE v121c, v1223(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1226: v1226(0x20) = CONST 
    0x1228: v1228(0x4) = CONST 
    0x122b: v122b = ADD v121c, v1228(0x4)
    0x122e: MSTORE v122b, v1226(0x20)
    0x122f: v122f(0x24) = CONST 
    0x1232: v1232 = ADD v121c, v122f(0x24)
    0x1233: MSTORE v1232, v1226(0x20)
    0x1234: v1234(0x0) = CONST 
    0x1237: v1237 = MLOAD v1234(0x0)
    0x1238: v1238(0x20) = CONST 
    0x123a: v123a(0x255c) = CONST 
    0x1242: MSTORE v1234(0x0), v1237
    0x1243: v1243(0x44) = CONST 
    0x1246: v1246 = ADD v121c, v1243(0x44)
    0x1247: MSTORE v1246, v2e29(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1249: v1249 = MLOAD v1219(0x40)
    0x124d: v124d(0x0) = SUB v121c, v1249
    0x124e: v124e(0x64) = CONST 
    0x1250: v1250(0x64) = ADD v124e(0x64), v124d(0x0)
    0x1252: REVERT v1249, v1250(0x64)
    0x2e29: v2e29(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1253
    prev=[0x120a], succ=[0x28b5]
    =================================
    0x1254: v1254(0x1) = CONST 
    0x1256: v1256(0x1) = CONST 
    0x1258: v1258(0xa0) = CONST 
    0x125a: v125a(0x10000000000000000000000000000000000000000) = SHL v1258(0xa0), v1256(0x1)
    0x125b: v125b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v125a(0x10000000000000000000000000000000000000000), v1254(0x1)
    0x125d: v125d = AND v540, v125b(0xffffffffffffffffffffffffffffffffffffffff)
    0x125e: v125e(0x0) = CONST 
    0x1262: MSTORE v125e(0x0), v125d
    0x1263: v1263(0x3) = CONST 
    0x1265: v1265(0x20) = CONST 
    0x1269: MSTORE v1265(0x20), v1263(0x3)
    0x126a: v126a(0x40) = CONST 
    0x126f: v126f = SHA3 v125e(0x0), v126a(0x40)
    0x1271: v1271 = SLOAD v126f
    0x1272: v1272(0xff) = CONST 
    0x1274: v1274(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1272(0xff)
    0x1275: v1275 = AND v1274(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1271
    0x1277: SSTORE v126f, v1275
    0x1279: v1279 = MLOAD v126a(0x40)
    0x127c: MSTORE v1279, v125d
    0x127e: v127e = MLOAD v126a(0x40)
    0x127f: v127f(0x10e1f7ce9fd7d1b90a66d13a2ab3cb8dd7f29f3f8d520b143b063ccfbab6906b) = CONST 
    0x12a3: v12a3(0x0) = SUB v1279, v127e
    0x12a6: v12a6(0x20) = ADD v1265(0x20), v12a3(0x0)
    0x12a8: LOG1 v127e, v12a6(0x20), v127f(0x10e1f7ce9fd7d1b90a66d13a2ab3cb8dd7f29f3f8d520b143b063ccfbab6906b)
    0x12aa: JUMP v520(0x28b5)

    Begin block 0x28b5
    prev=[0x1253], succ=[]
    =================================
    0x28b6: STOP 

}

function setAcceptToken(address,bool)() public {
    Begin block 0x545
    prev=[], succ=[0x54d, 0x551]
    =================================
    0x546: v546 = CALLVALUE 
    0x548: v548 = ISZERO v546
    0x549: v549(0x551) = CONST 
    0x54c: JUMPI v549(0x551), v548

    Begin block 0x54d
    prev=[0x545], succ=[]
    =================================
    0x54d: v54d(0x0) = CONST 
    0x550: REVERT v54d(0x0), v54d(0x0)

    Begin block 0x551
    prev=[0x545], succ=[0x564, 0x568]
    =================================
    0x553: v553(0x28d6) = CONST 
    0x556: v556(0x4) = CONST 
    0x559: v559 = CALLDATASIZE 
    0x55a: v55a = SUB v559, v556(0x4)
    0x55b: v55b(0x40) = CONST 
    0x55e: v55e = LT v55a, v55b(0x40)
    0x55f: v55f = ISZERO v55e
    0x560: v560(0x568) = CONST 
    0x563: JUMPI v560(0x568), v55f

    Begin block 0x564
    prev=[0x551], succ=[]
    =================================
    0x564: v564(0x0) = CONST 
    0x567: REVERT v564(0x0), v564(0x0)

    Begin block 0x568
    prev=[0x551], succ=[0x12ab]
    =================================
    0x56a: v56a(0x1) = CONST 
    0x56c: v56c(0x1) = CONST 
    0x56e: v56e(0xa0) = CONST 
    0x570: v570(0x10000000000000000000000000000000000000000) = SHL v56e(0xa0), v56c(0x1)
    0x571: v571(0xffffffffffffffffffffffffffffffffffffffff) = SUB v570(0x10000000000000000000000000000000000000000), v56a(0x1)
    0x573: v573 = CALLDATALOAD v556(0x4)
    0x574: v574 = AND v573, v571(0xffffffffffffffffffffffffffffffffffffffff)
    0x576: v576(0x20) = CONST 
    0x578: v578(0x24) = ADD v576(0x20), v556(0x4)
    0x579: v579 = CALLDATALOAD v578(0x24)
    0x57a: v57a = ISZERO v579
    0x57b: v57b = ISZERO v57a
    0x57c: v57c(0x12ab) = CONST 
    0x57f: JUMP v57c(0x12ab)

    Begin block 0x12ab
    prev=[0x568], succ=[0x227eB0x12ab]
    =================================
    0x12ac: v12ac(0x12b3) = CONST 
    0x12af: v12af(0x227e) = CONST 
    0x12b2: JUMP v12af(0x227e)

    Begin block 0x227eB0x12ab
    prev=[0x12ab], succ=[0x12b3]
    =================================
    0x227fS0x12ab: v227fV12ab = CALLER 
    0x2281S0x12ab: JUMP v12ac(0x12b3)

    Begin block 0x12b3
    prev=[0x227eB0x12ab], succ=[0x16ffB0x12b3]
    =================================
    0x12b4: v12b4(0x1) = CONST 
    0x12b6: v12b6(0x1) = CONST 
    0x12b8: v12b8(0xa0) = CONST 
    0x12ba: v12ba(0x10000000000000000000000000000000000000000) = SHL v12b8(0xa0), v12b6(0x1)
    0x12bb: v12bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12ba(0x10000000000000000000000000000000000000000), v12b4(0x1)
    0x12bc: v12bc = AND v12bb(0xffffffffffffffffffffffffffffffffffffffff), v227fV12ab
    0x12bd: v12bd(0x12c4) = CONST 
    0x12c0: v12c0(0x16ff) = CONST 
    0x12c3: JUMP v12c0(0x16ff)

    Begin block 0x16ffB0x12b3
    prev=[0x12b3], succ=[0x12c4]
    =================================
    0x1700S0x12b3: v1700V12b3(0x0) = CONST 
    0x1702S0x12b3: v1702V12b3 = SLOAD v1700V12b3(0x0)
    0x1703S0x12b3: v1703V12b3(0x1) = CONST 
    0x1705S0x12b3: v1705V12b3(0x1) = CONST 
    0x1707S0x12b3: v1707V12b3(0xa0) = CONST 
    0x1709S0x12b3: v1709V12b3(0x10000000000000000000000000000000000000000) = SHL v1707V12b3(0xa0), v1705V12b3(0x1)
    0x170aS0x12b3: v170aV12b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V12b3(0x10000000000000000000000000000000000000000), v1703V12b3(0x1)
    0x170bS0x12b3: v170bV12b3 = AND v170aV12b3(0xffffffffffffffffffffffffffffffffffffffff), v1702V12b3
    0x170dS0x12b3: JUMP v12bd(0x12c4)

    Begin block 0x12c4
    prev=[0x16ffB0x12b3], succ=[0x12d3, 0x130d]
    =================================
    0x12c5: v12c5(0x1) = CONST 
    0x12c7: v12c7(0x1) = CONST 
    0x12c9: v12c9(0xa0) = CONST 
    0x12cb: v12cb(0x10000000000000000000000000000000000000000) = SHL v12c9(0xa0), v12c7(0x1)
    0x12cc: v12cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12cb(0x10000000000000000000000000000000000000000), v12c5(0x1)
    0x12cd: v12cd = AND v12cc(0xffffffffffffffffffffffffffffffffffffffff), v170bV12b3
    0x12ce: v12ce = EQ v12cd, v12bc
    0x12cf: v12cf(0x130d) = CONST 
    0x12d2: JUMPI v12cf(0x130d), v12ce

    Begin block 0x12d3
    prev=[0x12c4], succ=[]
    =================================
    0x12d3: v12d3(0x40) = CONST 
    0x12d6: v12d6 = MLOAD v12d3(0x40)
    0x12d7: v12d7(0x461bcd) = CONST 
    0x12db: v12db(0xe5) = CONST 
    0x12dd: v12dd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12db(0xe5), v12d7(0x461bcd)
    0x12df: MSTORE v12d6, v12dd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12e0: v12e0(0x20) = CONST 
    0x12e2: v12e2(0x4) = CONST 
    0x12e5: v12e5 = ADD v12d6, v12e2(0x4)
    0x12e8: MSTORE v12e5, v12e0(0x20)
    0x12e9: v12e9(0x24) = CONST 
    0x12ec: v12ec = ADD v12d6, v12e9(0x24)
    0x12ed: MSTORE v12ec, v12e0(0x20)
    0x12ee: v12ee(0x0) = CONST 
    0x12f1: v12f1 = MLOAD v12ee(0x0)
    0x12f2: v12f2(0x20) = CONST 
    0x12f4: v12f4(0x255c) = CONST 
    0x12fc: MSTORE v12ee(0x0), v12f1
    0x12fd: v12fd(0x44) = CONST 
    0x1300: v1300 = ADD v12d6, v12fd(0x44)
    0x1301: MSTORE v1300, v2e2e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1303: v1303 = MLOAD v12d3(0x40)
    0x1307: v1307(0x0) = SUB v12d6, v1303
    0x1308: v1308(0x64) = CONST 
    0x130a: v130a(0x64) = ADD v1308(0x64), v1307(0x0)
    0x130c: REVERT v1303, v130a(0x64)
    0x2e2e: v2e2e(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x130d
    prev=[0x12c4], succ=[0x28d6]
    =================================
    0x130e: v130e(0x1) = CONST 
    0x1310: v1310(0x1) = CONST 
    0x1312: v1312(0xa0) = CONST 
    0x1314: v1314(0x10000000000000000000000000000000000000000) = SHL v1312(0xa0), v1310(0x1)
    0x1315: v1315(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1314(0x10000000000000000000000000000000000000000), v130e(0x1)
    0x1317: v1317 = AND v574, v1315(0xffffffffffffffffffffffffffffffffffffffff)
    0x1318: v1318(0x0) = CONST 
    0x131c: MSTORE v1318(0x0), v1317
    0x131d: v131d(0x4) = CONST 
    0x131f: v131f(0x20) = CONST 
    0x1323: MSTORE v131f(0x20), v131d(0x4)
    0x1324: v1324(0x40) = CONST 
    0x1329: v1329 = SHA3 v1318(0x0), v1324(0x40)
    0x132b: v132b = SLOAD v1329
    0x132c: v132c(0xff) = CONST 
    0x132e: v132e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v132c(0xff)
    0x132f: v132f = AND v132e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v132b
    0x1331: v1331 = ISZERO v57b
    0x1332: v1332 = ISZERO v1331
    0x1335: v1335 = OR v1332, v132f
    0x1338: SSTORE v1329, v1335
    0x133a: v133a = MLOAD v1324(0x40)
    0x133d: MSTORE v133a, v1317
    0x1340: v1340 = ADD v133a, v131f(0x20)
    0x1341: MSTORE v1340, v1332
    0x1343: v1343 = MLOAD v1324(0x40)
    0x1344: v1344(0xfb83d1604a8a86c6bbaa5e5fab0a9f152a3dff8d1af2df9a3e1e1def5fb0b01e) = CONST 
    0x1368: v1368(0x0) = SUB v133a, v1343
    0x136b: v136b(0x40) = ADD v1324(0x40), v1368(0x0)
    0x136d: LOG1 v1343, v136b(0x40), v1344(0xfb83d1604a8a86c6bbaa5e5fab0a9f152a3dff8d1af2df9a3e1e1def5fb0b01e)
    0x1370: JUMP v553(0x28d6)

    Begin block 0x28d6
    prev=[0x130d], succ=[]
    =================================
    0x28d7: STOP 

}

function renounceOwnership()() public {
    Begin block 0x580
    prev=[], succ=[0x588, 0x58c]
    =================================
    0x581: v581 = CALLVALUE 
    0x583: v583 = ISZERO v581
    0x584: v584(0x58c) = CONST 
    0x587: JUMPI v584(0x58c), v583

    Begin block 0x588
    prev=[0x580], succ=[]
    =================================
    0x588: v588(0x0) = CONST 
    0x58b: REVERT v588(0x0), v588(0x0)

    Begin block 0x58c
    prev=[0x580], succ=[0x1371]
    =================================
    0x58e: v58e(0x28f7) = CONST 
    0x591: v591(0x1371) = CONST 
    0x594: JUMP v591(0x1371)

    Begin block 0x1371
    prev=[0x58c], succ=[0x227eB0x1371]
    =================================
    0x1372: v1372(0x1379) = CONST 
    0x1375: v1375(0x227e) = CONST 
    0x1378: JUMP v1375(0x227e)

    Begin block 0x227eB0x1371
    prev=[0x1371], succ=[0x1379]
    =================================
    0x227fS0x1371: v227fV1371 = CALLER 
    0x2281S0x1371: JUMP v1372(0x1379)

    Begin block 0x1379
    prev=[0x227eB0x1371], succ=[0x16ffB0x1379]
    =================================
    0x137a: v137a(0x1) = CONST 
    0x137c: v137c(0x1) = CONST 
    0x137e: v137e(0xa0) = CONST 
    0x1380: v1380(0x10000000000000000000000000000000000000000) = SHL v137e(0xa0), v137c(0x1)
    0x1381: v1381(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1380(0x10000000000000000000000000000000000000000), v137a(0x1)
    0x1382: v1382 = AND v1381(0xffffffffffffffffffffffffffffffffffffffff), v227fV1371
    0x1383: v1383(0x138a) = CONST 
    0x1386: v1386(0x16ff) = CONST 
    0x1389: JUMP v1386(0x16ff)

    Begin block 0x16ffB0x1379
    prev=[0x1379], succ=[0x138a]
    =================================
    0x1700S0x1379: v1700V1379(0x0) = CONST 
    0x1702S0x1379: v1702V1379 = SLOAD v1700V1379(0x0)
    0x1703S0x1379: v1703V1379(0x1) = CONST 
    0x1705S0x1379: v1705V1379(0x1) = CONST 
    0x1707S0x1379: v1707V1379(0xa0) = CONST 
    0x1709S0x1379: v1709V1379(0x10000000000000000000000000000000000000000) = SHL v1707V1379(0xa0), v1705V1379(0x1)
    0x170aS0x1379: v170aV1379(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1379(0x10000000000000000000000000000000000000000), v1703V1379(0x1)
    0x170bS0x1379: v170bV1379 = AND v170aV1379(0xffffffffffffffffffffffffffffffffffffffff), v1702V1379
    0x170dS0x1379: JUMP v1383(0x138a)

    Begin block 0x138a
    prev=[0x16ffB0x1379], succ=[0x1399, 0x13d3]
    =================================
    0x138b: v138b(0x1) = CONST 
    0x138d: v138d(0x1) = CONST 
    0x138f: v138f(0xa0) = CONST 
    0x1391: v1391(0x10000000000000000000000000000000000000000) = SHL v138f(0xa0), v138d(0x1)
    0x1392: v1392(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1391(0x10000000000000000000000000000000000000000), v138b(0x1)
    0x1393: v1393 = AND v1392(0xffffffffffffffffffffffffffffffffffffffff), v170bV1379
    0x1394: v1394 = EQ v1393, v1382
    0x1395: v1395(0x13d3) = CONST 
    0x1398: JUMPI v1395(0x13d3), v1394

    Begin block 0x1399
    prev=[0x138a], succ=[]
    =================================
    0x1399: v1399(0x40) = CONST 
    0x139c: v139c = MLOAD v1399(0x40)
    0x139d: v139d(0x461bcd) = CONST 
    0x13a1: v13a1(0xe5) = CONST 
    0x13a3: v13a3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13a1(0xe5), v139d(0x461bcd)
    0x13a5: MSTORE v139c, v13a3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13a6: v13a6(0x20) = CONST 
    0x13a8: v13a8(0x4) = CONST 
    0x13ab: v13ab = ADD v139c, v13a8(0x4)
    0x13ae: MSTORE v13ab, v13a6(0x20)
    0x13af: v13af(0x24) = CONST 
    0x13b2: v13b2 = ADD v139c, v13af(0x24)
    0x13b3: MSTORE v13b2, v13a6(0x20)
    0x13b4: v13b4(0x0) = CONST 
    0x13b7: v13b7 = MLOAD v13b4(0x0)
    0x13b8: v13b8(0x20) = CONST 
    0x13ba: v13ba(0x255c) = CONST 
    0x13c2: MSTORE v13b4(0x0), v13b7
    0x13c3: v13c3(0x44) = CONST 
    0x13c6: v13c6 = ADD v139c, v13c3(0x44)
    0x13c7: MSTORE v13c6, v2e33(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x13c9: v13c9 = MLOAD v1399(0x40)
    0x13cd: v13cd(0x0) = SUB v139c, v13c9
    0x13ce: v13ce(0x64) = CONST 
    0x13d0: v13d0(0x64) = ADD v13ce(0x64), v13cd(0x0)
    0x13d2: REVERT v13c9, v13d0(0x64)
    0x2e33: v2e33(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x13d3
    prev=[0x138a], succ=[0x28f7]
    =================================
    0x13d4: v13d4(0x0) = CONST 
    0x13d7: v13d7 = SLOAD v13d4(0x0)
    0x13d8: v13d8(0x40) = CONST 
    0x13da: v13da = MLOAD v13d8(0x40)
    0x13db: v13db(0x1) = CONST 
    0x13dd: v13dd(0x1) = CONST 
    0x13df: v13df(0xa0) = CONST 
    0x13e1: v13e1(0x10000000000000000000000000000000000000000) = SHL v13df(0xa0), v13dd(0x1)
    0x13e2: v13e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13e1(0x10000000000000000000000000000000000000000), v13db(0x1)
    0x13e5: v13e5 = AND v13d7, v13e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x13e7: v13e7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x140b: LOG3 v13da, v13d4(0x0), v13e7(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v13e5, v13d4(0x0)
    0x140c: v140c(0x0) = CONST 
    0x140f: v140f = SLOAD v140c(0x0)
    0x1410: v1410(0x1) = CONST 
    0x1412: v1412(0x1) = CONST 
    0x1414: v1414(0xa0) = CONST 
    0x1416: v1416(0x10000000000000000000000000000000000000000) = SHL v1414(0xa0), v1412(0x1)
    0x1417: v1417(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1416(0x10000000000000000000000000000000000000000), v1410(0x1)
    0x1418: v1418(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1417(0xffffffffffffffffffffffffffffffffffffffff)
    0x1419: v1419 = AND v1418(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v140f
    0x141b: SSTORE v140c(0x0), v1419
    0x141c: JUMP v58e(0x28f7)

    Begin block 0x28f7
    prev=[0x13d3], succ=[]
    =================================
    0x28f8: STOP 

}

function setMaxAmountPerDay(address,uint256)() public {
    Begin block 0x595
    prev=[], succ=[0x59d, 0x5a1]
    =================================
    0x596: v596 = CALLVALUE 
    0x598: v598 = ISZERO v596
    0x599: v599(0x5a1) = CONST 
    0x59c: JUMPI v599(0x5a1), v598

    Begin block 0x59d
    prev=[0x595], succ=[]
    =================================
    0x59d: v59d(0x0) = CONST 
    0x5a0: REVERT v59d(0x0), v59d(0x0)

    Begin block 0x5a1
    prev=[0x595], succ=[0x5b4, 0x5b8]
    =================================
    0x5a3: v5a3(0x2918) = CONST 
    0x5a6: v5a6(0x4) = CONST 
    0x5a9: v5a9 = CALLDATASIZE 
    0x5aa: v5aa = SUB v5a9, v5a6(0x4)
    0x5ab: v5ab(0x40) = CONST 
    0x5ae: v5ae = LT v5aa, v5ab(0x40)
    0x5af: v5af = ISZERO v5ae
    0x5b0: v5b0(0x5b8) = CONST 
    0x5b3: JUMPI v5b0(0x5b8), v5af

    Begin block 0x5b4
    prev=[0x5a1], succ=[]
    =================================
    0x5b4: v5b4(0x0) = CONST 
    0x5b7: REVERT v5b4(0x0), v5b4(0x0)

    Begin block 0x5b8
    prev=[0x5a1], succ=[0x141d]
    =================================
    0x5ba: v5ba(0x1) = CONST 
    0x5bc: v5bc(0x1) = CONST 
    0x5be: v5be(0xa0) = CONST 
    0x5c0: v5c0(0x10000000000000000000000000000000000000000) = SHL v5be(0xa0), v5bc(0x1)
    0x5c1: v5c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c0(0x10000000000000000000000000000000000000000), v5ba(0x1)
    0x5c3: v5c3 = CALLDATALOAD v5a6(0x4)
    0x5c4: v5c4 = AND v5c3, v5c1(0xffffffffffffffffffffffffffffffffffffffff)
    0x5c6: v5c6(0x20) = CONST 
    0x5c8: v5c8(0x24) = ADD v5c6(0x20), v5a6(0x4)
    0x5c9: v5c9 = CALLDATALOAD v5c8(0x24)
    0x5ca: v5ca(0x141d) = CONST 
    0x5cd: JUMP v5ca(0x141d)

    Begin block 0x141d
    prev=[0x5b8], succ=[0x227eB0x141d]
    =================================
    0x141e: v141e(0x1425) = CONST 
    0x1421: v1421(0x227e) = CONST 
    0x1424: JUMP v1421(0x227e)

    Begin block 0x227eB0x141d
    prev=[0x141d], succ=[0x1425]
    =================================
    0x227fS0x141d: v227fV141d = CALLER 
    0x2281S0x141d: JUMP v141e(0x1425)

    Begin block 0x1425
    prev=[0x227eB0x141d], succ=[0x16ffB0x1425]
    =================================
    0x1426: v1426(0x1) = CONST 
    0x1428: v1428(0x1) = CONST 
    0x142a: v142a(0xa0) = CONST 
    0x142c: v142c(0x10000000000000000000000000000000000000000) = SHL v142a(0xa0), v1428(0x1)
    0x142d: v142d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v142c(0x10000000000000000000000000000000000000000), v1426(0x1)
    0x142e: v142e = AND v142d(0xffffffffffffffffffffffffffffffffffffffff), v227fV141d
    0x142f: v142f(0x1436) = CONST 
    0x1432: v1432(0x16ff) = CONST 
    0x1435: JUMP v1432(0x16ff)

    Begin block 0x16ffB0x1425
    prev=[0x1425], succ=[0x1436]
    =================================
    0x1700S0x1425: v1700V1425(0x0) = CONST 
    0x1702S0x1425: v1702V1425 = SLOAD v1700V1425(0x0)
    0x1703S0x1425: v1703V1425(0x1) = CONST 
    0x1705S0x1425: v1705V1425(0x1) = CONST 
    0x1707S0x1425: v1707V1425(0xa0) = CONST 
    0x1709S0x1425: v1709V1425(0x10000000000000000000000000000000000000000) = SHL v1707V1425(0xa0), v1705V1425(0x1)
    0x170aS0x1425: v170aV1425(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1425(0x10000000000000000000000000000000000000000), v1703V1425(0x1)
    0x170bS0x1425: v170bV1425 = AND v170aV1425(0xffffffffffffffffffffffffffffffffffffffff), v1702V1425
    0x170dS0x1425: JUMP v142f(0x1436)

    Begin block 0x1436
    prev=[0x16ffB0x1425], succ=[0x1445, 0x147f]
    =================================
    0x1437: v1437(0x1) = CONST 
    0x1439: v1439(0x1) = CONST 
    0x143b: v143b(0xa0) = CONST 
    0x143d: v143d(0x10000000000000000000000000000000000000000) = SHL v143b(0xa0), v1439(0x1)
    0x143e: v143e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v143d(0x10000000000000000000000000000000000000000), v1437(0x1)
    0x143f: v143f = AND v143e(0xffffffffffffffffffffffffffffffffffffffff), v170bV1425
    0x1440: v1440 = EQ v143f, v142e
    0x1441: v1441(0x147f) = CONST 
    0x1444: JUMPI v1441(0x147f), v1440

    Begin block 0x1445
    prev=[0x1436], succ=[]
    =================================
    0x1445: v1445(0x40) = CONST 
    0x1448: v1448 = MLOAD v1445(0x40)
    0x1449: v1449(0x461bcd) = CONST 
    0x144d: v144d(0xe5) = CONST 
    0x144f: v144f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v144d(0xe5), v1449(0x461bcd)
    0x1451: MSTORE v1448, v144f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1452: v1452(0x20) = CONST 
    0x1454: v1454(0x4) = CONST 
    0x1457: v1457 = ADD v1448, v1454(0x4)
    0x145a: MSTORE v1457, v1452(0x20)
    0x145b: v145b(0x24) = CONST 
    0x145e: v145e = ADD v1448, v145b(0x24)
    0x145f: MSTORE v145e, v1452(0x20)
    0x1460: v1460(0x0) = CONST 
    0x1463: v1463 = MLOAD v1460(0x0)
    0x1464: v1464(0x20) = CONST 
    0x1466: v1466(0x255c) = CONST 
    0x146e: MSTORE v1460(0x0), v1463
    0x146f: v146f(0x44) = CONST 
    0x1472: v1472 = ADD v1448, v146f(0x44)
    0x1473: MSTORE v1472, v2e38(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1475: v1475 = MLOAD v1445(0x40)
    0x1479: v1479(0x0) = SUB v1448, v1475
    0x147a: v147a(0x64) = CONST 
    0x147c: v147c(0x64) = ADD v147a(0x64), v1479(0x0)
    0x147e: REVERT v1475, v147c(0x64)
    0x2e38: v2e38(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x147f
    prev=[0x1436], succ=[0x2918]
    =================================
    0x1480: v1480(0x1) = CONST 
    0x1482: v1482(0x1) = CONST 
    0x1484: v1484(0xa0) = CONST 
    0x1486: v1486(0x10000000000000000000000000000000000000000) = SHL v1484(0xa0), v1482(0x1)
    0x1487: v1487(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1486(0x10000000000000000000000000000000000000000), v1480(0x1)
    0x1489: v1489 = AND v5c4, v1487(0xffffffffffffffffffffffffffffffffffffffff)
    0x148a: v148a(0x0) = CONST 
    0x148e: MSTORE v148a(0x0), v1489
    0x148f: v148f(0x9) = CONST 
    0x1491: v1491(0x20) = CONST 
    0x1495: MSTORE v1491(0x20), v148f(0x9)
    0x1496: v1496(0x40) = CONST 
    0x149b: v149b = SHA3 v148a(0x0), v1496(0x40)
    0x149d: v149d = SLOAD v149b
    0x14a1: SSTORE v149b, v5c9
    0x14a3: v14a3 = MLOAD v1496(0x40)
    0x14a6: MSTORE v14a3, v1489
    0x14a9: v14a9 = ADD v14a3, v1491(0x20)
    0x14ac: MSTORE v14a9, v149d
    0x14af: v14af = ADD v1496(0x40), v14a3
    0x14b2: MSTORE v14af, v5c9
    0x14b4: v14b4 = MLOAD v1496(0x40)
    0x14b7: v14b7(0x9960d8ab6d24d9d231b61cbbbd189a0459a1b592b34a469049576da66d959f88) = CONST 
    0x14dc: v14dc(0x0) = SUB v14a3, v14b4
    0x14dd: v14dd(0x60) = CONST 
    0x14df: v14df(0x60) = ADD v14dd(0x60), v14dc(0x0)
    0x14e1: LOG1 v14b4, v14df(0x60), v14b7(0x9960d8ab6d24d9d231b61cbbbd189a0459a1b592b34a469049576da66d959f88)
    0x14e5: JUMP v5a3(0x2918)

    Begin block 0x2918
    prev=[0x147f], succ=[]
    =================================
    0x2919: STOP 

}

function pause()() public {
    Begin block 0x5ce
    prev=[], succ=[0x5d6, 0x5da]
    =================================
    0x5cf: v5cf = CALLVALUE 
    0x5d1: v5d1 = ISZERO v5cf
    0x5d2: v5d2(0x5da) = CONST 
    0x5d5: JUMPI v5d2(0x5da), v5d1

    Begin block 0x5d6
    prev=[0x5ce], succ=[]
    =================================
    0x5d6: v5d6(0x0) = CONST 
    0x5d9: REVERT v5d6(0x0), v5d6(0x0)

    Begin block 0x5da
    prev=[0x5ce], succ=[0x14e6]
    =================================
    0x5dc: v5dc(0x2939) = CONST 
    0x5df: v5df(0x14e6) = CONST 
    0x5e2: JUMP v5df(0x14e6)

    Begin block 0x14e6
    prev=[0x5da], succ=[0x14f2, 0x1531]
    =================================
    0x14e7: v14e7(0xf) = CONST 
    0x14e9: v14e9 = SLOAD v14e7(0xf)
    0x14ea: v14ea(0xff) = CONST 
    0x14ec: v14ec = AND v14ea(0xff), v14e9
    0x14ed: v14ed = ISZERO v14ec
    0x14ee: v14ee(0x1531) = CONST 
    0x14f1: JUMPI v14ee(0x1531), v14ed

    Begin block 0x14f2
    prev=[0x14e6], succ=[]
    =================================
    0x14f2: v14f2(0x40) = CONST 
    0x14f5: v14f5 = MLOAD v14f2(0x40)
    0x14f6: v14f6(0x461bcd) = CONST 
    0x14fa: v14fa(0xe5) = CONST 
    0x14fc: v14fc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v14fa(0xe5), v14f6(0x461bcd)
    0x14fe: MSTORE v14f5, v14fc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14ff: v14ff(0x20) = CONST 
    0x1501: v1501(0x4) = CONST 
    0x1504: v1504 = ADD v14f5, v1501(0x4)
    0x1505: MSTORE v1504, v14ff(0x20)
    0x1506: v1506(0x10) = CONST 
    0x1508: v1508(0x24) = CONST 
    0x150b: v150b = ADD v14f5, v1508(0x24)
    0x150c: MSTORE v150b, v1506(0x10)
    0x150d: v150d(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0x151e: v151e(0x82) = CONST 
    0x1520: v1520(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL v151e(0x82), v150d(0x14185d5cd8589b194e881c185d5cd959)
    0x1521: v1521(0x44) = CONST 
    0x1524: v1524 = ADD v14f5, v1521(0x44)
    0x1525: MSTORE v1524, v1520(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x1527: v1527 = MLOAD v14f2(0x40)
    0x152b: v152b(0x0) = SUB v14f5, v1527
    0x152c: v152c(0x64) = CONST 
    0x152e: v152e(0x64) = ADD v152c(0x64), v152b(0x0)
    0x1530: REVERT v1527, v152e(0x64)

    Begin block 0x1531
    prev=[0x14e6], succ=[0x227eB0x1531]
    =================================
    0x1532: v1532(0x1539) = CONST 
    0x1535: v1535(0x227e) = CONST 
    0x1538: JUMP v1535(0x227e)

    Begin block 0x227eB0x1531
    prev=[0x1531], succ=[0x1539]
    =================================
    0x227fS0x1531: v227fV1531 = CALLER 
    0x2281S0x1531: JUMP v1532(0x1539)

    Begin block 0x1539
    prev=[0x227eB0x1531], succ=[0x16ffB0x1539]
    =================================
    0x153a: v153a(0x1) = CONST 
    0x153c: v153c(0x1) = CONST 
    0x153e: v153e(0xa0) = CONST 
    0x1540: v1540(0x10000000000000000000000000000000000000000) = SHL v153e(0xa0), v153c(0x1)
    0x1541: v1541(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1540(0x10000000000000000000000000000000000000000), v153a(0x1)
    0x1542: v1542 = AND v1541(0xffffffffffffffffffffffffffffffffffffffff), v227fV1531
    0x1543: v1543(0x154a) = CONST 
    0x1546: v1546(0x16ff) = CONST 
    0x1549: JUMP v1546(0x16ff)

    Begin block 0x16ffB0x1539
    prev=[0x1539], succ=[0x154a]
    =================================
    0x1700S0x1539: v1700V1539(0x0) = CONST 
    0x1702S0x1539: v1702V1539 = SLOAD v1700V1539(0x0)
    0x1703S0x1539: v1703V1539(0x1) = CONST 
    0x1705S0x1539: v1705V1539(0x1) = CONST 
    0x1707S0x1539: v1707V1539(0xa0) = CONST 
    0x1709S0x1539: v1709V1539(0x10000000000000000000000000000000000000000) = SHL v1707V1539(0xa0), v1705V1539(0x1)
    0x170aS0x1539: v170aV1539(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1539(0x10000000000000000000000000000000000000000), v1703V1539(0x1)
    0x170bS0x1539: v170bV1539 = AND v170aV1539(0xffffffffffffffffffffffffffffffffffffffff), v1702V1539
    0x170dS0x1539: JUMP v1543(0x154a)

    Begin block 0x154a
    prev=[0x16ffB0x1539], succ=[0x1559, 0x1593]
    =================================
    0x154b: v154b(0x1) = CONST 
    0x154d: v154d(0x1) = CONST 
    0x154f: v154f(0xa0) = CONST 
    0x1551: v1551(0x10000000000000000000000000000000000000000) = SHL v154f(0xa0), v154d(0x1)
    0x1552: v1552(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1551(0x10000000000000000000000000000000000000000), v154b(0x1)
    0x1553: v1553 = AND v1552(0xffffffffffffffffffffffffffffffffffffffff), v170bV1539
    0x1554: v1554 = EQ v1553, v1542
    0x1555: v1555(0x1593) = CONST 
    0x1558: JUMPI v1555(0x1593), v1554

    Begin block 0x1559
    prev=[0x154a], succ=[]
    =================================
    0x1559: v1559(0x40) = CONST 
    0x155c: v155c = MLOAD v1559(0x40)
    0x155d: v155d(0x461bcd) = CONST 
    0x1561: v1561(0xe5) = CONST 
    0x1563: v1563(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1561(0xe5), v155d(0x461bcd)
    0x1565: MSTORE v155c, v1563(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1566: v1566(0x20) = CONST 
    0x1568: v1568(0x4) = CONST 
    0x156b: v156b = ADD v155c, v1568(0x4)
    0x156e: MSTORE v156b, v1566(0x20)
    0x156f: v156f(0x24) = CONST 
    0x1572: v1572 = ADD v155c, v156f(0x24)
    0x1573: MSTORE v1572, v1566(0x20)
    0x1574: v1574(0x0) = CONST 
    0x1577: v1577 = MLOAD v1574(0x0)
    0x1578: v1578(0x20) = CONST 
    0x157a: v157a(0x255c) = CONST 
    0x1582: MSTORE v1574(0x0), v1577
    0x1583: v1583(0x44) = CONST 
    0x1586: v1586 = ADD v155c, v1583(0x44)
    0x1587: MSTORE v1586, v2e3d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1589: v1589 = MLOAD v1559(0x40)
    0x158d: v158d(0x0) = SUB v155c, v1589
    0x158e: v158e(0x64) = CONST 
    0x1590: v1590(0x64) = ADD v158e(0x64), v158d(0x0)
    0x1592: REVERT v1589, v1590(0x64)
    0x2e3d: v2e3d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1593
    prev=[0x154a], succ=[0x2939]
    =================================
    0x1594: v1594(0xf) = CONST 
    0x1597: v1597 = SLOAD v1594(0xf)
    0x1598: v1598(0xff) = CONST 
    0x159a: v159a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1598(0xff)
    0x159b: v159b = AND v159a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1597
    0x159c: v159c(0x1) = CONST 
    0x159e: v159e = OR v159c(0x1), v159b
    0x15a0: SSTORE v1594(0xf), v159e
    0x15a1: v15a1(0x40) = CONST 
    0x15a4: v15a4 = MLOAD v15a1(0x40)
    0x15a5: v15a5 = CALLER 
    0x15a7: MSTORE v15a4, v15a5
    0x15a9: v15a9 = MLOAD v15a1(0x40)
    0x15aa: v15aa(0x62e78cea01bee320cd4e420270b5ea74000d11b0c9f74754ebdbfc544b05a258) = CONST 
    0x15ce: v15ce(0x0) = SUB v15a4, v15a9
    0x15cf: v15cf(0x20) = CONST 
    0x15d1: v15d1(0x20) = ADD v15cf(0x20), v15ce(0x0)
    0x15d3: LOG1 v15a9, v15d1(0x20), v15aa(0x62e78cea01bee320cd4e420270b5ea74000d11b0c9f74754ebdbfc544b05a258)
    0x15d4: JUMP v5dc(0x2939)

    Begin block 0x2939
    prev=[0x1593], succ=[]
    =================================
    0x293a: STOP 

}

function setFee(uint8,uint256)() public {
    Begin block 0x5e3
    prev=[], succ=[0x5eb, 0x5ef]
    =================================
    0x5e4: v5e4 = CALLVALUE 
    0x5e6: v5e6 = ISZERO v5e4
    0x5e7: v5e7(0x5ef) = CONST 
    0x5ea: JUMPI v5e7(0x5ef), v5e6

    Begin block 0x5eb
    prev=[0x5e3], succ=[]
    =================================
    0x5eb: v5eb(0x0) = CONST 
    0x5ee: REVERT v5eb(0x0), v5eb(0x0)

    Begin block 0x5ef
    prev=[0x5e3], succ=[0x602, 0x606]
    =================================
    0x5f1: v5f1(0x295a) = CONST 
    0x5f4: v5f4(0x4) = CONST 
    0x5f7: v5f7 = CALLDATASIZE 
    0x5f8: v5f8 = SUB v5f7, v5f4(0x4)
    0x5f9: v5f9(0x40) = CONST 
    0x5fc: v5fc = LT v5f8, v5f9(0x40)
    0x5fd: v5fd = ISZERO v5fc
    0x5fe: v5fe(0x606) = CONST 
    0x601: JUMPI v5fe(0x606), v5fd

    Begin block 0x602
    prev=[0x5ef], succ=[]
    =================================
    0x602: v602(0x0) = CONST 
    0x605: REVERT v602(0x0), v602(0x0)

    Begin block 0x606
    prev=[0x5ef], succ=[0x15d5]
    =================================
    0x608: v608(0xff) = CONST 
    0x60b: v60b = CALLDATALOAD v5f4(0x4)
    0x60c: v60c = AND v60b, v608(0xff)
    0x60e: v60e(0x20) = CONST 
    0x610: v610(0x24) = ADD v60e(0x20), v5f4(0x4)
    0x611: v611 = CALLDATALOAD v610(0x24)
    0x612: v612(0x15d5) = CONST 
    0x615: JUMP v612(0x15d5)

    Begin block 0x15d5
    prev=[0x606], succ=[0x227eB0x15d5]
    =================================
    0x15d6: v15d6(0x15dd) = CONST 
    0x15d9: v15d9(0x227e) = CONST 
    0x15dc: JUMP v15d9(0x227e)

    Begin block 0x227eB0x15d5
    prev=[0x15d5], succ=[0x15dd]
    =================================
    0x227fS0x15d5: v227fV15d5 = CALLER 
    0x2281S0x15d5: JUMP v15d6(0x15dd)

    Begin block 0x15dd
    prev=[0x227eB0x15d5], succ=[0x16ffB0x15dd]
    =================================
    0x15de: v15de(0x1) = CONST 
    0x15e0: v15e0(0x1) = CONST 
    0x15e2: v15e2(0xa0) = CONST 
    0x15e4: v15e4(0x10000000000000000000000000000000000000000) = SHL v15e2(0xa0), v15e0(0x1)
    0x15e5: v15e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15e4(0x10000000000000000000000000000000000000000), v15de(0x1)
    0x15e6: v15e6 = AND v15e5(0xffffffffffffffffffffffffffffffffffffffff), v227fV15d5
    0x15e7: v15e7(0x15ee) = CONST 
    0x15ea: v15ea(0x16ff) = CONST 
    0x15ed: JUMP v15ea(0x16ff)

    Begin block 0x16ffB0x15dd
    prev=[0x15dd], succ=[0x15ee]
    =================================
    0x1700S0x15dd: v1700V15dd(0x0) = CONST 
    0x1702S0x15dd: v1702V15dd = SLOAD v1700V15dd(0x0)
    0x1703S0x15dd: v1703V15dd(0x1) = CONST 
    0x1705S0x15dd: v1705V15dd(0x1) = CONST 
    0x1707S0x15dd: v1707V15dd(0xa0) = CONST 
    0x1709S0x15dd: v1709V15dd(0x10000000000000000000000000000000000000000) = SHL v1707V15dd(0xa0), v1705V15dd(0x1)
    0x170aS0x15dd: v170aV15dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V15dd(0x10000000000000000000000000000000000000000), v1703V15dd(0x1)
    0x170bS0x15dd: v170bV15dd = AND v170aV15dd(0xffffffffffffffffffffffffffffffffffffffff), v1702V15dd
    0x170dS0x15dd: JUMP v15e7(0x15ee)

    Begin block 0x15ee
    prev=[0x16ffB0x15dd], succ=[0x15fd, 0x1637]
    =================================
    0x15ef: v15ef(0x1) = CONST 
    0x15f1: v15f1(0x1) = CONST 
    0x15f3: v15f3(0xa0) = CONST 
    0x15f5: v15f5(0x10000000000000000000000000000000000000000) = SHL v15f3(0xa0), v15f1(0x1)
    0x15f6: v15f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15f5(0x10000000000000000000000000000000000000000), v15ef(0x1)
    0x15f7: v15f7 = AND v15f6(0xffffffffffffffffffffffffffffffffffffffff), v170bV15dd
    0x15f8: v15f8 = EQ v15f7, v15e6
    0x15f9: v15f9(0x1637) = CONST 
    0x15fc: JUMPI v15f9(0x1637), v15f8

    Begin block 0x15fd
    prev=[0x15ee], succ=[]
    =================================
    0x15fd: v15fd(0x40) = CONST 
    0x1600: v1600 = MLOAD v15fd(0x40)
    0x1601: v1601(0x461bcd) = CONST 
    0x1605: v1605(0xe5) = CONST 
    0x1607: v1607(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1605(0xe5), v1601(0x461bcd)
    0x1609: MSTORE v1600, v1607(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x160a: v160a(0x20) = CONST 
    0x160c: v160c(0x4) = CONST 
    0x160f: v160f = ADD v1600, v160c(0x4)
    0x1612: MSTORE v160f, v160a(0x20)
    0x1613: v1613(0x24) = CONST 
    0x1616: v1616 = ADD v1600, v1613(0x24)
    0x1617: MSTORE v1616, v160a(0x20)
    0x1618: v1618(0x0) = CONST 
    0x161b: v161b = MLOAD v1618(0x0)
    0x161c: v161c(0x20) = CONST 
    0x161e: v161e(0x255c) = CONST 
    0x1626: MSTORE v1618(0x0), v161b
    0x1627: v1627(0x44) = CONST 
    0x162a: v162a = ADD v1600, v1627(0x44)
    0x162b: MSTORE v162a, v2e42(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x162d: v162d = MLOAD v15fd(0x40)
    0x1631: v1631(0x0) = SUB v1600, v162d
    0x1632: v1632(0x64) = CONST 
    0x1634: v1634(0x64) = ADD v1632(0x64), v1631(0x0)
    0x1636: REVERT v162d, v1634(0x64)
    0x2e42: v2e42(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1637
    prev=[0x15ee], succ=[0x1648, 0x1649]
    =================================
    0x1638: v1638(0x0) = CONST 
    0x163a: v163a(0x8) = CONST 
    0x163c: v163c(0x0) = CONST 
    0x163f: v163f(0x2) = CONST 
    0x1642: v1642 = GT v60c, v163f(0x2)
    0x1643: v1643 = ISZERO v1642
    0x1644: v1644(0x1649) = CONST 
    0x1647: JUMPI v1644(0x1649), v1643

    Begin block 0x1648
    prev=[0x1637], succ=[]
    =================================
    0x1648: THROW 

    Begin block 0x1649
    prev=[0x1637], succ=[0x1653, 0x1654]
    =================================
    0x164a: v164a(0x2) = CONST 
    0x164d: v164d = GT v60c, v164a(0x2)
    0x164e: v164e = ISZERO v164d
    0x164f: v164f(0x1654) = CONST 
    0x1652: JUMPI v164f(0x1654), v164e

    Begin block 0x1653
    prev=[0x1649], succ=[]
    =================================
    0x1653: THROW 

    Begin block 0x1654
    prev=[0x1649], succ=[0x1675, 0x1676]
    =================================
    0x1656: MSTORE v163c(0x0), v60c
    0x1657: v1657(0x20) = CONST 
    0x1659: v1659(0x20) = ADD v1657(0x20), v163c(0x0)
    0x165c: MSTORE v1659(0x20), v163a(0x8)
    0x165d: v165d(0x20) = CONST 
    0x165f: v165f(0x40) = ADD v165d(0x20), v1659(0x20)
    0x1660: v1660(0x0) = CONST 
    0x1662: v1662 = SHA3 v1660(0x0), v165f(0x40)
    0x1663: v1663 = SLOAD v1662
    0x1667: v1667(0x8) = CONST 
    0x1669: v1669(0x0) = CONST 
    0x166c: v166c(0x2) = CONST 
    0x166f: v166f = GT v60c, v166c(0x2)
    0x1670: v1670 = ISZERO v166f
    0x1671: v1671(0x1676) = CONST 
    0x1674: JUMPI v1671(0x1676), v1670

    Begin block 0x1675
    prev=[0x1654], succ=[]
    =================================
    0x1675: THROW 

    Begin block 0x1676
    prev=[0x1654], succ=[0x1680, 0x1681]
    =================================
    0x1677: v1677(0x2) = CONST 
    0x167a: v167a = GT v60c, v1677(0x2)
    0x167b: v167b = ISZERO v167a
    0x167c: v167c(0x1681) = CONST 
    0x167f: JUMPI v167c(0x1681), v167b

    Begin block 0x1680
    prev=[0x1676], succ=[]
    =================================
    0x1680: THROW 

    Begin block 0x1681
    prev=[0x1676], succ=[0x16c6, 0x16c7]
    =================================
    0x1683: MSTORE v1669(0x0), v60c
    0x1684: v1684(0x20) = CONST 
    0x1686: v1686(0x20) = ADD v1684(0x20), v1669(0x0)
    0x1689: MSTORE v1686(0x20), v1667(0x8)
    0x168a: v168a(0x20) = CONST 
    0x168c: v168c(0x40) = ADD v168a(0x20), v1686(0x20)
    0x168d: v168d(0x0) = CONST 
    0x168f: v168f = SHA3 v168d(0x0), v168c(0x40)
    0x1692: SSTORE v168f, v611
    0x1694: v1694(0xdd12f06625ea96c77973a15dcc7830c0763d498c4b16247203051b822a12d082) = CONST 
    0x16b8: v16b8(0x40) = CONST 
    0x16ba: v16ba = MLOAD v16b8(0x40)
    0x16bd: v16bd(0x2) = CONST 
    0x16c0: v16c0 = GT v60c, v16bd(0x2)
    0x16c1: v16c1 = ISZERO v16c0
    0x16c2: v16c2(0x16c7) = CONST 
    0x16c5: JUMPI v16c2(0x16c7), v16c1

    Begin block 0x16c6
    prev=[0x1681], succ=[]
    =================================
    0x16c6: THROW 

    Begin block 0x16c7
    prev=[0x1681], succ=[0x295a]
    =================================
    0x16c9: MSTORE v16ba, v60c
    0x16ca: v16ca(0x20) = CONST 
    0x16cc: v16cc = ADD v16ca(0x20), v16ba
    0x16cf: MSTORE v16cc, v1663
    0x16d0: v16d0(0x20) = CONST 
    0x16d2: v16d2 = ADD v16d0(0x20), v16cc
    0x16d5: MSTORE v16d2, v611
    0x16d6: v16d6(0x20) = CONST 
    0x16d8: v16d8 = ADD v16d6(0x20), v16d2
    0x16de: v16de(0x40) = CONST 
    0x16e0: v16e0 = MLOAD v16de(0x40)
    0x16e3: v16e3(0x60) = SUB v16d8, v16e0
    0x16e5: LOG1 v16e0, v16e3(0x60), v1694(0xdd12f06625ea96c77973a15dcc7830c0763d498c4b16247203051b822a12d082)
    0x16e9: JUMP v5f1(0x295a)

    Begin block 0x295a
    prev=[0x16c7], succ=[]
    =================================
    0x295b: STOP 

}

function acceptToken(address)() public {
    Begin block 0x616
    prev=[], succ=[0x61e, 0x622]
    =================================
    0x617: v617 = CALLVALUE 
    0x619: v619 = ISZERO v617
    0x61a: v61a(0x622) = CONST 
    0x61d: JUMPI v61a(0x622), v619

    Begin block 0x61e
    prev=[0x616], succ=[]
    =================================
    0x61e: v61e(0x0) = CONST 
    0x621: REVERT v61e(0x0), v61e(0x0)

    Begin block 0x622
    prev=[0x616], succ=[0x635, 0x639]
    =================================
    0x624: v624(0x297b) = CONST 
    0x627: v627(0x4) = CONST 
    0x62a: v62a = CALLDATASIZE 
    0x62b: v62b = SUB v62a, v627(0x4)
    0x62c: v62c(0x20) = CONST 
    0x62f: v62f = LT v62b, v62c(0x20)
    0x630: v630 = ISZERO v62f
    0x631: v631(0x639) = CONST 
    0x634: JUMPI v631(0x639), v630

    Begin block 0x635
    prev=[0x622], succ=[]
    =================================
    0x635: v635(0x0) = CONST 
    0x638: REVERT v635(0x0), v635(0x0)

    Begin block 0x639
    prev=[0x622], succ=[0x16ea]
    =================================
    0x63b: v63b = CALLDATALOAD v627(0x4)
    0x63c: v63c(0x1) = CONST 
    0x63e: v63e(0x1) = CONST 
    0x640: v640(0xa0) = CONST 
    0x642: v642(0x10000000000000000000000000000000000000000) = SHL v640(0xa0), v63e(0x1)
    0x643: v643(0xffffffffffffffffffffffffffffffffffffffff) = SUB v642(0x10000000000000000000000000000000000000000), v63c(0x1)
    0x644: v644 = AND v643(0xffffffffffffffffffffffffffffffffffffffff), v63b
    0x645: v645(0x16ea) = CONST 
    0x648: JUMP v645(0x16ea)

    Begin block 0x16ea
    prev=[0x639], succ=[0x297b]
    =================================
    0x16eb: v16eb(0x4) = CONST 
    0x16ed: v16ed(0x20) = CONST 
    0x16ef: MSTORE v16ed(0x20), v16eb(0x4)
    0x16f0: v16f0(0x0) = CONST 
    0x16f4: MSTORE v16f0(0x0), v644
    0x16f5: v16f5(0x40) = CONST 
    0x16f8: v16f8 = SHA3 v16f0(0x0), v16f5(0x40)
    0x16f9: v16f9 = SLOAD v16f8
    0x16fa: v16fa(0xff) = CONST 
    0x16fc: v16fc = AND v16fa(0xff), v16f9
    0x16fe: JUMP v624(0x297b)

    Begin block 0x297b
    prev=[0x16ea], succ=[]
    =================================
    0x297c: v297c(0x40) = CONST 
    0x297f: v297f = MLOAD v297c(0x40)
    0x2981: v2981 = ISZERO v16fc
    0x2982: v2982 = ISZERO v2981
    0x2984: MSTORE v297f, v2982
    0x2985: v2985 = MLOAD v297c(0x40)
    0x2989: v2989(0x0) = SUB v297f, v2985
    0x298a: v298a(0x20) = CONST 
    0x298c: v298c(0x20) = ADD v298a(0x20), v2989(0x0)
    0x298e: RETURN v2985, v298c(0x20)

}

function owner()() public {
    Begin block 0x649
    prev=[], succ=[0x651, 0x655]
    =================================
    0x64a: v64a = CALLVALUE 
    0x64c: v64c = ISZERO v64a
    0x64d: v64d(0x655) = CONST 
    0x650: JUMPI v64d(0x655), v64c

    Begin block 0x651
    prev=[0x649], succ=[]
    =================================
    0x651: v651(0x0) = CONST 
    0x654: REVERT v651(0x0), v651(0x0)

    Begin block 0x655
    prev=[0x649], succ=[0x16ffB0x655]
    =================================
    0x657: v657(0x29ae) = CONST 
    0x65a: v65a(0x16ff) = CONST 
    0x65d: JUMP v65a(0x16ff)

    Begin block 0x16ffB0x655
    prev=[0x655], succ=[0x29ae]
    =================================
    0x1700S0x655: v1700V655(0x0) = CONST 
    0x1702S0x655: v1702V655 = SLOAD v1700V655(0x0)
    0x1703S0x655: v1703V655(0x1) = CONST 
    0x1705S0x655: v1705V655(0x1) = CONST 
    0x1707S0x655: v1707V655(0xa0) = CONST 
    0x1709S0x655: v1709V655(0x10000000000000000000000000000000000000000) = SHL v1707V655(0xa0), v1705V655(0x1)
    0x170aS0x655: v170aV655(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V655(0x10000000000000000000000000000000000000000), v1703V655(0x1)
    0x170bS0x655: v170bV655 = AND v170aV655(0xffffffffffffffffffffffffffffffffffffffff), v1702V655
    0x170dS0x655: JUMP v657(0x29ae)

    Begin block 0x29ae
    prev=[0x16ffB0x655], succ=[]
    =================================
    0x29af: v29af(0x40) = CONST 
    0x29b2: v29b2 = MLOAD v29af(0x40)
    0x29b3: v29b3(0x1) = CONST 
    0x29b5: v29b5(0x1) = CONST 
    0x29b7: v29b7(0xa0) = CONST 
    0x29b9: v29b9(0x10000000000000000000000000000000000000000) = SHL v29b7(0xa0), v29b5(0x1)
    0x29ba: v29ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29b9(0x10000000000000000000000000000000000000000), v29b3(0x1)
    0x29bd: v29bd = AND v170bV655, v29ba(0xffffffffffffffffffffffffffffffffffffffff)
    0x29bf: MSTORE v29b2, v29bd
    0x29c0: v29c0 = MLOAD v29af(0x40)
    0x29c4: v29c4(0x0) = SUB v29b2, v29c0
    0x29c5: v29c5(0x20) = CONST 
    0x29c7: v29c7(0x20) = ADD v29c5(0x20), v29c4(0x0)
    0x29c9: RETURN v29c0, v29c7(0x20)

}

function maxAmount(address)() public {
    Begin block 0x65e
    prev=[], succ=[0x666, 0x66a]
    =================================
    0x65f: v65f = CALLVALUE 
    0x661: v661 = ISZERO v65f
    0x662: v662(0x66a) = CONST 
    0x665: JUMPI v662(0x66a), v661

    Begin block 0x666
    prev=[0x65e], succ=[]
    =================================
    0x666: v666(0x0) = CONST 
    0x669: REVERT v666(0x0), v666(0x0)

    Begin block 0x66a
    prev=[0x65e], succ=[0x67d, 0x681]
    =================================
    0x66c: v66c(0x29e9) = CONST 
    0x66f: v66f(0x4) = CONST 
    0x672: v672 = CALLDATASIZE 
    0x673: v673 = SUB v672, v66f(0x4)
    0x674: v674(0x20) = CONST 
    0x677: v677 = LT v673, v674(0x20)
    0x678: v678 = ISZERO v677
    0x679: v679(0x681) = CONST 
    0x67c: JUMPI v679(0x681), v678

    Begin block 0x67d
    prev=[0x66a], succ=[]
    =================================
    0x67d: v67d(0x0) = CONST 
    0x680: REVERT v67d(0x0), v67d(0x0)

    Begin block 0x681
    prev=[0x66a], succ=[0x170e]
    =================================
    0x683: v683 = CALLDATALOAD v66f(0x4)
    0x684: v684(0x1) = CONST 
    0x686: v686(0x1) = CONST 
    0x688: v688(0xa0) = CONST 
    0x68a: v68a(0x10000000000000000000000000000000000000000) = SHL v688(0xa0), v686(0x1)
    0x68b: v68b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v68a(0x10000000000000000000000000000000000000000), v684(0x1)
    0x68c: v68c = AND v68b(0xffffffffffffffffffffffffffffffffffffffff), v683
    0x68d: v68d(0x170e) = CONST 
    0x690: JUMP v68d(0x170e)

    Begin block 0x170e
    prev=[0x681], succ=[0x29e9]
    =================================
    0x170f: v170f(0xa) = CONST 
    0x1711: v1711(0x20) = CONST 
    0x1713: MSTORE v1711(0x20), v170f(0xa)
    0x1714: v1714(0x0) = CONST 
    0x1718: MSTORE v1714(0x0), v68c
    0x1719: v1719(0x40) = CONST 
    0x171c: v171c = SHA3 v1714(0x0), v1719(0x40)
    0x171d: v171d = SLOAD v171c
    0x171f: JUMP v66c(0x29e9)

    Begin block 0x29e9
    prev=[0x170e], succ=[]
    =================================
    0x29ea: v29ea(0x40) = CONST 
    0x29ed: v29ed = MLOAD v29ea(0x40)
    0x29f0: MSTORE v29ed, v171d
    0x29f1: v29f1 = MLOAD v29ea(0x40)
    0x29f5: v29f5(0x0) = SUB v29ed, v29f1
    0x29f6: v29f6(0x20) = CONST 
    0x29f8: v29f8(0x20) = ADD v29f6(0x20), v29f5(0x0)
    0x29fa: RETURN v29f1, v29f8(0x20)

}

function setConfirmRequireNum(uint256)() public {
    Begin block 0x691
    prev=[], succ=[0x699, 0x69d]
    =================================
    0x692: v692 = CALLVALUE 
    0x694: v694 = ISZERO v692
    0x695: v695(0x69d) = CONST 
    0x698: JUMPI v695(0x69d), v694

    Begin block 0x699
    prev=[0x691], succ=[]
    =================================
    0x699: v699(0x0) = CONST 
    0x69c: REVERT v699(0x0), v699(0x0)

    Begin block 0x69d
    prev=[0x691], succ=[0x6b0, 0x6b4]
    =================================
    0x69f: v69f(0x2a1a) = CONST 
    0x6a2: v6a2(0x4) = CONST 
    0x6a5: v6a5 = CALLDATASIZE 
    0x6a6: v6a6 = SUB v6a5, v6a2(0x4)
    0x6a7: v6a7(0x20) = CONST 
    0x6aa: v6aa = LT v6a6, v6a7(0x20)
    0x6ab: v6ab = ISZERO v6aa
    0x6ac: v6ac(0x6b4) = CONST 
    0x6af: JUMPI v6ac(0x6b4), v6ab

    Begin block 0x6b0
    prev=[0x69d], succ=[]
    =================================
    0x6b0: v6b0(0x0) = CONST 
    0x6b3: REVERT v6b0(0x0), v6b0(0x0)

    Begin block 0x6b4
    prev=[0x69d], succ=[0x1720]
    =================================
    0x6b6: v6b6 = CALLDATALOAD v6a2(0x4)
    0x6b7: v6b7(0x1720) = CONST 
    0x6ba: JUMP v6b7(0x1720)

    Begin block 0x1720
    prev=[0x6b4], succ=[0x227eB0x1720]
    =================================
    0x1721: v1721(0x1728) = CONST 
    0x1724: v1724(0x227e) = CONST 
    0x1727: JUMP v1724(0x227e)

    Begin block 0x227eB0x1720
    prev=[0x1720], succ=[0x1728]
    =================================
    0x227fS0x1720: v227fV1720 = CALLER 
    0x2281S0x1720: JUMP v1721(0x1728)

    Begin block 0x1728
    prev=[0x227eB0x1720], succ=[0x16ffB0x1728]
    =================================
    0x1729: v1729(0x1) = CONST 
    0x172b: v172b(0x1) = CONST 
    0x172d: v172d(0xa0) = CONST 
    0x172f: v172f(0x10000000000000000000000000000000000000000) = SHL v172d(0xa0), v172b(0x1)
    0x1730: v1730(0xffffffffffffffffffffffffffffffffffffffff) = SUB v172f(0x10000000000000000000000000000000000000000), v1729(0x1)
    0x1731: v1731 = AND v1730(0xffffffffffffffffffffffffffffffffffffffff), v227fV1720
    0x1732: v1732(0x1739) = CONST 
    0x1735: v1735(0x16ff) = CONST 
    0x1738: JUMP v1735(0x16ff)

    Begin block 0x16ffB0x1728
    prev=[0x1728], succ=[0x1739]
    =================================
    0x1700S0x1728: v1700V1728(0x0) = CONST 
    0x1702S0x1728: v1702V1728 = SLOAD v1700V1728(0x0)
    0x1703S0x1728: v1703V1728(0x1) = CONST 
    0x1705S0x1728: v1705V1728(0x1) = CONST 
    0x1707S0x1728: v1707V1728(0xa0) = CONST 
    0x1709S0x1728: v1709V1728(0x10000000000000000000000000000000000000000) = SHL v1707V1728(0xa0), v1705V1728(0x1)
    0x170aS0x1728: v170aV1728(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1728(0x10000000000000000000000000000000000000000), v1703V1728(0x1)
    0x170bS0x1728: v170bV1728 = AND v170aV1728(0xffffffffffffffffffffffffffffffffffffffff), v1702V1728
    0x170dS0x1728: JUMP v1732(0x1739)

    Begin block 0x1739
    prev=[0x16ffB0x1728], succ=[0x1748, 0x1782]
    =================================
    0x173a: v173a(0x1) = CONST 
    0x173c: v173c(0x1) = CONST 
    0x173e: v173e(0xa0) = CONST 
    0x1740: v1740(0x10000000000000000000000000000000000000000) = SHL v173e(0xa0), v173c(0x1)
    0x1741: v1741(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1740(0x10000000000000000000000000000000000000000), v173a(0x1)
    0x1742: v1742 = AND v1741(0xffffffffffffffffffffffffffffffffffffffff), v170bV1728
    0x1743: v1743 = EQ v1742, v1731
    0x1744: v1744(0x1782) = CONST 
    0x1747: JUMPI v1744(0x1782), v1743

    Begin block 0x1748
    prev=[0x1739], succ=[]
    =================================
    0x1748: v1748(0x40) = CONST 
    0x174b: v174b = MLOAD v1748(0x40)
    0x174c: v174c(0x461bcd) = CONST 
    0x1750: v1750(0xe5) = CONST 
    0x1752: v1752(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1750(0xe5), v174c(0x461bcd)
    0x1754: MSTORE v174b, v1752(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1755: v1755(0x20) = CONST 
    0x1757: v1757(0x4) = CONST 
    0x175a: v175a = ADD v174b, v1757(0x4)
    0x175d: MSTORE v175a, v1755(0x20)
    0x175e: v175e(0x24) = CONST 
    0x1761: v1761 = ADD v174b, v175e(0x24)
    0x1762: MSTORE v1761, v1755(0x20)
    0x1763: v1763(0x0) = CONST 
    0x1766: v1766 = MLOAD v1763(0x0)
    0x1767: v1767(0x20) = CONST 
    0x1769: v1769(0x255c) = CONST 
    0x1771: MSTORE v1763(0x0), v1766
    0x1772: v1772(0x44) = CONST 
    0x1775: v1775 = ADD v174b, v1772(0x44)
    0x1776: MSTORE v1775, v2e47(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1778: v1778 = MLOAD v1748(0x40)
    0x177c: v177c(0x0) = SUB v174b, v1778
    0x177d: v177d(0x64) = CONST 
    0x177f: v177f(0x64) = ADD v177d(0x64), v177c(0x0)
    0x1781: REVERT v1778, v177f(0x64)
    0x2e47: v2e47(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1782
    prev=[0x1739], succ=[0x2a1a]
    =================================
    0x1783: v1783(0x7) = CONST 
    0x1786: v1786 = SLOAD v1783(0x7)
    0x178a: SSTORE v1783(0x7), v6b6
    0x178b: v178b(0x40) = CONST 
    0x178e: v178e = MLOAD v178b(0x40)
    0x1791: MSTORE v178e, v1786
    0x1792: v1792(0x20) = CONST 
    0x1795: v1795 = ADD v178e, v1792(0x20)
    0x1798: MSTORE v1795, v6b6
    0x179a: v179a = MLOAD v178b(0x40)
    0x179b: v179b(0x1b8d67cafd0d8a192d2236d5754f89f1d10d32a50ecb9eedde65d87ca776c351) = CONST 
    0x17c0: v17c0(0x0) = SUB v178e, v179a
    0x17c3: v17c3(0x40) = ADD v178b(0x40), v17c0(0x0)
    0x17c5: LOG1 v179a, v17c3(0x40), v179b(0x1b8d67cafd0d8a192d2236d5754f89f1d10d32a50ecb9eedde65d87ca776c351)
    0x17c8: JUMP v69f(0x2a1a)

    Begin block 0x2a1a
    prev=[0x1782], succ=[]
    =================================
    0x2a1b: STOP 

}

function transfer(uint256,address)() public {
    Begin block 0x6bb
    prev=[], succ=[0x6c3, 0x6c7]
    =================================
    0x6bc: v6bc = CALLVALUE 
    0x6be: v6be = ISZERO v6bc
    0x6bf: v6bf(0x6c7) = CONST 
    0x6c2: JUMPI v6bf(0x6c7), v6be

    Begin block 0x6c3
    prev=[0x6bb], succ=[]
    =================================
    0x6c3: v6c3(0x0) = CONST 
    0x6c6: REVERT v6c3(0x0), v6c3(0x0)

    Begin block 0x6c7
    prev=[0x6bb], succ=[0x6da, 0x6de]
    =================================
    0x6c9: v6c9(0x2a3b) = CONST 
    0x6cc: v6cc(0x4) = CONST 
    0x6cf: v6cf = CALLDATASIZE 
    0x6d0: v6d0 = SUB v6cf, v6cc(0x4)
    0x6d1: v6d1(0x40) = CONST 
    0x6d4: v6d4 = LT v6d0, v6d1(0x40)
    0x6d5: v6d5 = ISZERO v6d4
    0x6d6: v6d6(0x6de) = CONST 
    0x6d9: JUMPI v6d6(0x6de), v6d5

    Begin block 0x6da
    prev=[0x6c7], succ=[]
    =================================
    0x6da: v6da(0x0) = CONST 
    0x6dd: REVERT v6da(0x0), v6da(0x0)

    Begin block 0x6de
    prev=[0x6c7], succ=[0x17c9]
    =================================
    0x6e1: v6e1 = CALLDATALOAD v6cc(0x4)
    0x6e3: v6e3(0x20) = CONST 
    0x6e5: v6e5(0x24) = ADD v6e3(0x20), v6cc(0x4)
    0x6e6: v6e6 = CALLDATALOAD v6e5(0x24)
    0x6e7: v6e7(0x1) = CONST 
    0x6e9: v6e9(0x1) = CONST 
    0x6eb: v6eb(0xa0) = CONST 
    0x6ed: v6ed(0x10000000000000000000000000000000000000000) = SHL v6eb(0xa0), v6e9(0x1)
    0x6ee: v6ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ed(0x10000000000000000000000000000000000000000), v6e7(0x1)
    0x6ef: v6ef = AND v6ee(0xffffffffffffffffffffffffffffffffffffffff), v6e6
    0x6f0: v6f0(0x17c9) = CONST 
    0x6f3: JUMP v6f0(0x17c9)

    Begin block 0x17c9
    prev=[0x6de], succ=[0x227eB0x17c9]
    =================================
    0x17ca: v17ca(0x17d1) = CONST 
    0x17cd: v17cd(0x227e) = CONST 
    0x17d0: JUMP v17cd(0x227e)

    Begin block 0x227eB0x17c9
    prev=[0x17c9], succ=[0x17d1]
    =================================
    0x227fS0x17c9: v227fV17c9 = CALLER 
    0x2281S0x17c9: JUMP v17ca(0x17d1)

    Begin block 0x17d1
    prev=[0x227eB0x17c9], succ=[0x16ffB0x17d1]
    =================================
    0x17d2: v17d2(0x1) = CONST 
    0x17d4: v17d4(0x1) = CONST 
    0x17d6: v17d6(0xa0) = CONST 
    0x17d8: v17d8(0x10000000000000000000000000000000000000000) = SHL v17d6(0xa0), v17d4(0x1)
    0x17d9: v17d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17d8(0x10000000000000000000000000000000000000000), v17d2(0x1)
    0x17da: v17da = AND v17d9(0xffffffffffffffffffffffffffffffffffffffff), v227fV17c9
    0x17db: v17db(0x17e2) = CONST 
    0x17de: v17de(0x16ff) = CONST 
    0x17e1: JUMP v17de(0x16ff)

    Begin block 0x16ffB0x17d1
    prev=[0x17d1], succ=[0x17e2]
    =================================
    0x1700S0x17d1: v1700V17d1(0x0) = CONST 
    0x1702S0x17d1: v1702V17d1 = SLOAD v1700V17d1(0x0)
    0x1703S0x17d1: v1703V17d1(0x1) = CONST 
    0x1705S0x17d1: v1705V17d1(0x1) = CONST 
    0x1707S0x17d1: v1707V17d1(0xa0) = CONST 
    0x1709S0x17d1: v1709V17d1(0x10000000000000000000000000000000000000000) = SHL v1707V17d1(0xa0), v1705V17d1(0x1)
    0x170aS0x17d1: v170aV17d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V17d1(0x10000000000000000000000000000000000000000), v1703V17d1(0x1)
    0x170bS0x17d1: v170bV17d1 = AND v170aV17d1(0xffffffffffffffffffffffffffffffffffffffff), v1702V17d1
    0x170dS0x17d1: JUMP v17db(0x17e2)

    Begin block 0x17e2
    prev=[0x16ffB0x17d1], succ=[0x17f1, 0x182b]
    =================================
    0x17e3: v17e3(0x1) = CONST 
    0x17e5: v17e5(0x1) = CONST 
    0x17e7: v17e7(0xa0) = CONST 
    0x17e9: v17e9(0x10000000000000000000000000000000000000000) = SHL v17e7(0xa0), v17e5(0x1)
    0x17ea: v17ea(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17e9(0x10000000000000000000000000000000000000000), v17e3(0x1)
    0x17eb: v17eb = AND v17ea(0xffffffffffffffffffffffffffffffffffffffff), v170bV17d1
    0x17ec: v17ec = EQ v17eb, v17da
    0x17ed: v17ed(0x182b) = CONST 
    0x17f0: JUMPI v17ed(0x182b), v17ec

    Begin block 0x17f1
    prev=[0x17e2], succ=[]
    =================================
    0x17f1: v17f1(0x40) = CONST 
    0x17f4: v17f4 = MLOAD v17f1(0x40)
    0x17f5: v17f5(0x461bcd) = CONST 
    0x17f9: v17f9(0xe5) = CONST 
    0x17fb: v17fb(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17f9(0xe5), v17f5(0x461bcd)
    0x17fd: MSTORE v17f4, v17fb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17fe: v17fe(0x20) = CONST 
    0x1800: v1800(0x4) = CONST 
    0x1803: v1803 = ADD v17f4, v1800(0x4)
    0x1806: MSTORE v1803, v17fe(0x20)
    0x1807: v1807(0x24) = CONST 
    0x180a: v180a = ADD v17f4, v1807(0x24)
    0x180b: MSTORE v180a, v17fe(0x20)
    0x180c: v180c(0x0) = CONST 
    0x180f: v180f = MLOAD v180c(0x0)
    0x1810: v1810(0x20) = CONST 
    0x1812: v1812(0x255c) = CONST 
    0x181a: MSTORE v180c(0x0), v180f
    0x181b: v181b(0x44) = CONST 
    0x181e: v181e = ADD v17f4, v181b(0x44)
    0x181f: MSTORE v181e, v2e4c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1821: v1821 = MLOAD v17f1(0x40)
    0x1825: v1825(0x0) = SUB v17f4, v1821
    0x1826: v1826(0x64) = CONST 
    0x1828: v1828(0x64) = ADD v1826(0x64), v1825(0x0)
    0x182a: REVERT v1821, v1828(0x64)
    0x2e4c: v2e4c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x182b
    prev=[0x17e2], succ=[0x1858, 0x1861]
    =================================
    0x182c: v182c(0x40) = CONST 
    0x182e: v182e = MLOAD v182c(0x40)
    0x182f: v182f(0x1) = CONST 
    0x1831: v1831(0x1) = CONST 
    0x1833: v1833(0xa0) = CONST 
    0x1835: v1835(0x10000000000000000000000000000000000000000) = SHL v1833(0xa0), v1831(0x1)
    0x1836: v1836(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1835(0x10000000000000000000000000000000000000000), v182f(0x1)
    0x1838: v1838 = AND v6ef, v1836(0xffffffffffffffffffffffffffffffffffffffff)
    0x183b: v183b = ISZERO v6e1
    0x183c: v183c(0x8fc) = CONST 
    0x183f: v183f = MUL v183c(0x8fc), v183b
    0x1843: v1843(0x0) = CONST 
    0x184b: v184b = CALL v183f, v1838, v6e1, v182e, v1843(0x0), v182e, v1843(0x0)
    0x1851: v1851 = ISZERO v184b
    0x1853: v1853 = ISZERO v1851
    0x1854: v1854(0x1861) = CONST 
    0x1857: JUMPI v1854(0x1861), v1853

    Begin block 0x1858
    prev=[0x182b], succ=[]
    =================================
    0x1858: v1858 = RETURNDATASIZE 
    0x1859: v1859(0x0) = CONST 
    0x185c: RETURNDATACOPY v1859(0x0), v1859(0x0), v1858
    0x185d: v185d = RETURNDATASIZE 
    0x185e: v185e(0x0) = CONST 
    0x1860: REVERT v185e(0x0), v185d

    Begin block 0x1861
    prev=[0x182b], succ=[0x2a3b]
    =================================
    0x1865: JUMP v6c9(0x2a3b)

    Begin block 0x2a3b
    prev=[0x1861], succ=[]
    =================================
    0x2a3c: STOP 

}

function timestamp()() public {
    Begin block 0x6f4
    prev=[], succ=[0x6fc, 0x700]
    =================================
    0x6f5: v6f5 = CALLVALUE 
    0x6f7: v6f7 = ISZERO v6f5
    0x6f8: v6f8(0x700) = CONST 
    0x6fb: JUMPI v6f8(0x700), v6f7

    Begin block 0x6fc
    prev=[0x6f4], succ=[]
    =================================
    0x6fc: v6fc(0x0) = CONST 
    0x6ff: REVERT v6fc(0x0), v6fc(0x0)

    Begin block 0x700
    prev=[0x6f4], succ=[0x1866]
    =================================
    0x702: v702(0x2a5c) = CONST 
    0x705: v705(0x1866) = CONST 
    0x708: JUMP v705(0x1866)

    Begin block 0x1866
    prev=[0x700], succ=[0x2a5c]
    =================================
    0x1867: v1867(0xe) = CONST 
    0x1869: v1869 = SLOAD v1867(0xe)
    0x186b: JUMP v702(0x2a5c)

    Begin block 0x2a5c
    prev=[0x1866], succ=[]
    =================================
    0x2a5d: v2a5d(0x40) = CONST 
    0x2a60: v2a60 = MLOAD v2a5d(0x40)
    0x2a63: MSTORE v2a60, v1869
    0x2a64: v2a64 = MLOAD v2a5d(0x40)
    0x2a68: v2a68(0x0) = SUB v2a60, v2a64
    0x2a69: v2a69(0x20) = CONST 
    0x2a6b: v2a6b(0x20) = ADD v2a69(0x20), v2a68(0x0)
    0x2a6d: RETURN v2a64, v2a6b(0x20)

}

function relayer(address)() public {
    Begin block 0x709
    prev=[], succ=[0x711, 0x715]
    =================================
    0x70a: v70a = CALLVALUE 
    0x70c: v70c = ISZERO v70a
    0x70d: v70d(0x715) = CONST 
    0x710: JUMPI v70d(0x715), v70c

    Begin block 0x711
    prev=[0x709], succ=[]
    =================================
    0x711: v711(0x0) = CONST 
    0x714: REVERT v711(0x0), v711(0x0)

    Begin block 0x715
    prev=[0x709], succ=[0x728, 0x72c]
    =================================
    0x717: v717(0x2a8d) = CONST 
    0x71a: v71a(0x4) = CONST 
    0x71d: v71d = CALLDATASIZE 
    0x71e: v71e = SUB v71d, v71a(0x4)
    0x71f: v71f(0x20) = CONST 
    0x722: v722 = LT v71e, v71f(0x20)
    0x723: v723 = ISZERO v722
    0x724: v724(0x72c) = CONST 
    0x727: JUMPI v724(0x72c), v723

    Begin block 0x728
    prev=[0x715], succ=[]
    =================================
    0x728: v728(0x0) = CONST 
    0x72b: REVERT v728(0x0), v728(0x0)

    Begin block 0x72c
    prev=[0x715], succ=[0x186c]
    =================================
    0x72e: v72e = CALLDATALOAD v71a(0x4)
    0x72f: v72f(0x1) = CONST 
    0x731: v731(0x1) = CONST 
    0x733: v733(0xa0) = CONST 
    0x735: v735(0x10000000000000000000000000000000000000000) = SHL v733(0xa0), v731(0x1)
    0x736: v736(0xffffffffffffffffffffffffffffffffffffffff) = SUB v735(0x10000000000000000000000000000000000000000), v72f(0x1)
    0x737: v737 = AND v736(0xffffffffffffffffffffffffffffffffffffffff), v72e
    0x738: v738(0x186c) = CONST 
    0x73b: JUMP v738(0x186c)

    Begin block 0x186c
    prev=[0x72c], succ=[0x2a8d]
    =================================
    0x186d: v186d(0x3) = CONST 
    0x186f: v186f(0x20) = CONST 
    0x1871: MSTORE v186f(0x20), v186d(0x3)
    0x1872: v1872(0x0) = CONST 
    0x1876: MSTORE v1872(0x0), v737
    0x1877: v1877(0x40) = CONST 
    0x187a: v187a = SHA3 v1872(0x0), v1877(0x40)
    0x187b: v187b = SLOAD v187a
    0x187c: v187c(0xff) = CONST 
    0x187e: v187e = AND v187c(0xff), v187b
    0x1880: JUMP v717(0x2a8d)

    Begin block 0x2a8d
    prev=[0x186c], succ=[]
    =================================
    0x2a8e: v2a8e(0x40) = CONST 
    0x2a91: v2a91 = MLOAD v2a8e(0x40)
    0x2a93: v2a93 = ISZERO v187e
    0x2a94: v2a94 = ISZERO v2a93
    0x2a96: MSTORE v2a91, v2a94
    0x2a97: v2a97 = MLOAD v2a8e(0x40)
    0x2a9b: v2a9b(0x0) = SUB v2a91, v2a97
    0x2a9c: v2a9c(0x20) = CONST 
    0x2a9e: v2a9e(0x20) = ADD v2a9c(0x20), v2a9b(0x0)
    0x2aa0: RETURN v2a97, v2a9e(0x20)

}

function setMinAmount(address,uint256)() public {
    Begin block 0x73c
    prev=[], succ=[0x744, 0x748]
    =================================
    0x73d: v73d = CALLVALUE 
    0x73f: v73f = ISZERO v73d
    0x740: v740(0x748) = CONST 
    0x743: JUMPI v740(0x748), v73f

    Begin block 0x744
    prev=[0x73c], succ=[]
    =================================
    0x744: v744(0x0) = CONST 
    0x747: REVERT v744(0x0), v744(0x0)

    Begin block 0x748
    prev=[0x73c], succ=[0x75b, 0x75f]
    =================================
    0x74a: v74a(0x2ac0) = CONST 
    0x74d: v74d(0x4) = CONST 
    0x750: v750 = CALLDATASIZE 
    0x751: v751 = SUB v750, v74d(0x4)
    0x752: v752(0x40) = CONST 
    0x755: v755 = LT v751, v752(0x40)
    0x756: v756 = ISZERO v755
    0x757: v757(0x75f) = CONST 
    0x75a: JUMPI v757(0x75f), v756

    Begin block 0x75b
    prev=[0x748], succ=[]
    =================================
    0x75b: v75b(0x0) = CONST 
    0x75e: REVERT v75b(0x0), v75b(0x0)

    Begin block 0x75f
    prev=[0x748], succ=[0x1881]
    =================================
    0x761: v761(0x1) = CONST 
    0x763: v763(0x1) = CONST 
    0x765: v765(0xa0) = CONST 
    0x767: v767(0x10000000000000000000000000000000000000000) = SHL v765(0xa0), v763(0x1)
    0x768: v768(0xffffffffffffffffffffffffffffffffffffffff) = SUB v767(0x10000000000000000000000000000000000000000), v761(0x1)
    0x76a: v76a = CALLDATALOAD v74d(0x4)
    0x76b: v76b = AND v76a, v768(0xffffffffffffffffffffffffffffffffffffffff)
    0x76d: v76d(0x20) = CONST 
    0x76f: v76f(0x24) = ADD v76d(0x20), v74d(0x4)
    0x770: v770 = CALLDATALOAD v76f(0x24)
    0x771: v771(0x1881) = CONST 
    0x774: JUMP v771(0x1881)

    Begin block 0x1881
    prev=[0x75f], succ=[0x227eB0x1881]
    =================================
    0x1882: v1882(0x1889) = CONST 
    0x1885: v1885(0x227e) = CONST 
    0x1888: JUMP v1885(0x227e)

    Begin block 0x227eB0x1881
    prev=[0x1881], succ=[0x1889]
    =================================
    0x227fS0x1881: v227fV1881 = CALLER 
    0x2281S0x1881: JUMP v1882(0x1889)

    Begin block 0x1889
    prev=[0x227eB0x1881], succ=[0x16ffB0x1889]
    =================================
    0x188a: v188a(0x1) = CONST 
    0x188c: v188c(0x1) = CONST 
    0x188e: v188e(0xa0) = CONST 
    0x1890: v1890(0x10000000000000000000000000000000000000000) = SHL v188e(0xa0), v188c(0x1)
    0x1891: v1891(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1890(0x10000000000000000000000000000000000000000), v188a(0x1)
    0x1892: v1892 = AND v1891(0xffffffffffffffffffffffffffffffffffffffff), v227fV1881
    0x1893: v1893(0x189a) = CONST 
    0x1896: v1896(0x16ff) = CONST 
    0x1899: JUMP v1896(0x16ff)

    Begin block 0x16ffB0x1889
    prev=[0x1889], succ=[0x189a]
    =================================
    0x1700S0x1889: v1700V1889(0x0) = CONST 
    0x1702S0x1889: v1702V1889 = SLOAD v1700V1889(0x0)
    0x1703S0x1889: v1703V1889(0x1) = CONST 
    0x1705S0x1889: v1705V1889(0x1) = CONST 
    0x1707S0x1889: v1707V1889(0xa0) = CONST 
    0x1709S0x1889: v1709V1889(0x10000000000000000000000000000000000000000) = SHL v1707V1889(0xa0), v1705V1889(0x1)
    0x170aS0x1889: v170aV1889(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1889(0x10000000000000000000000000000000000000000), v1703V1889(0x1)
    0x170bS0x1889: v170bV1889 = AND v170aV1889(0xffffffffffffffffffffffffffffffffffffffff), v1702V1889
    0x170dS0x1889: JUMP v1893(0x189a)

    Begin block 0x189a
    prev=[0x16ffB0x1889], succ=[0x18a9, 0x18e3]
    =================================
    0x189b: v189b(0x1) = CONST 
    0x189d: v189d(0x1) = CONST 
    0x189f: v189f(0xa0) = CONST 
    0x18a1: v18a1(0x10000000000000000000000000000000000000000) = SHL v189f(0xa0), v189d(0x1)
    0x18a2: v18a2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18a1(0x10000000000000000000000000000000000000000), v189b(0x1)
    0x18a3: v18a3 = AND v18a2(0xffffffffffffffffffffffffffffffffffffffff), v170bV1889
    0x18a4: v18a4 = EQ v18a3, v1892
    0x18a5: v18a5(0x18e3) = CONST 
    0x18a8: JUMPI v18a5(0x18e3), v18a4

    Begin block 0x18a9
    prev=[0x189a], succ=[]
    =================================
    0x18a9: v18a9(0x40) = CONST 
    0x18ac: v18ac = MLOAD v18a9(0x40)
    0x18ad: v18ad(0x461bcd) = CONST 
    0x18b1: v18b1(0xe5) = CONST 
    0x18b3: v18b3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v18b1(0xe5), v18ad(0x461bcd)
    0x18b5: MSTORE v18ac, v18b3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x18b6: v18b6(0x20) = CONST 
    0x18b8: v18b8(0x4) = CONST 
    0x18bb: v18bb = ADD v18ac, v18b8(0x4)
    0x18be: MSTORE v18bb, v18b6(0x20)
    0x18bf: v18bf(0x24) = CONST 
    0x18c2: v18c2 = ADD v18ac, v18bf(0x24)
    0x18c3: MSTORE v18c2, v18b6(0x20)
    0x18c4: v18c4(0x0) = CONST 
    0x18c7: v18c7 = MLOAD v18c4(0x0)
    0x18c8: v18c8(0x20) = CONST 
    0x18ca: v18ca(0x255c) = CONST 
    0x18d2: MSTORE v18c4(0x0), v18c7
    0x18d3: v18d3(0x44) = CONST 
    0x18d6: v18d6 = ADD v18ac, v18d3(0x44)
    0x18d7: MSTORE v18d6, v2e51(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x18d9: v18d9 = MLOAD v18a9(0x40)
    0x18dd: v18dd(0x0) = SUB v18ac, v18d9
    0x18de: v18de(0x64) = CONST 
    0x18e0: v18e0(0x64) = ADD v18de(0x64), v18dd(0x0)
    0x18e2: REVERT v18d9, v18e0(0x64)
    0x2e51: v2e51(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x18e3
    prev=[0x189a], succ=[0x1904, 0x1941]
    =================================
    0x18e4: v18e4(0x1) = CONST 
    0x18e6: v18e6(0x1) = CONST 
    0x18e8: v18e8(0xa0) = CONST 
    0x18ea: v18ea(0x10000000000000000000000000000000000000000) = SHL v18e8(0xa0), v18e6(0x1)
    0x18eb: v18eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18ea(0x10000000000000000000000000000000000000000), v18e4(0x1)
    0x18ed: v18ed = AND v76b, v18eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x18ee: v18ee(0x0) = CONST 
    0x18f2: MSTORE v18ee(0x0), v18ed
    0x18f3: v18f3(0xa) = CONST 
    0x18f5: v18f5(0x20) = CONST 
    0x18f7: MSTORE v18f5(0x20), v18f3(0xa)
    0x18f8: v18f8(0x40) = CONST 
    0x18fb: v18fb = SHA3 v18ee(0x0), v18f8(0x40)
    0x18fc: v18fc = SLOAD v18fb
    0x18fe: v18fe = GT v770, v18fc
    0x18ff: v18ff = ISZERO v18fe
    0x1900: v1900(0x1941) = CONST 
    0x1903: JUMPI v1900(0x1941), v18ff

    Begin block 0x1904
    prev=[0x18e3], succ=[]
    =================================
    0x1904: v1904(0x40) = CONST 
    0x1907: v1907 = MLOAD v1904(0x40)
    0x1908: v1908(0x461bcd) = CONST 
    0x190c: v190c(0xe5) = CONST 
    0x190e: v190e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v190c(0xe5), v1908(0x461bcd)
    0x1910: MSTORE v1907, v190e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1911: v1911(0x20) = CONST 
    0x1913: v1913(0x4) = CONST 
    0x1916: v1916 = ADD v1907, v1913(0x4)
    0x1917: MSTORE v1916, v1911(0x20)
    0x1918: v1918(0xe) = CONST 
    0x191a: v191a(0x24) = CONST 
    0x191d: v191d = ADD v1907, v191a(0x24)
    0x191e: MSTORE v191d, v1918(0xe)
    0x191f: v191f(0x125b9d985b1a5908185b5bdd5b9d) = CONST 
    0x192e: v192e(0x92) = CONST 
    0x1930: v1930(0x496e76616c696420616d6f756e74000000000000000000000000000000000000) = SHL v192e(0x92), v191f(0x125b9d985b1a5908185b5bdd5b9d)
    0x1931: v1931(0x44) = CONST 
    0x1934: v1934 = ADD v1907, v1931(0x44)
    0x1935: MSTORE v1934, v1930(0x496e76616c696420616d6f756e74000000000000000000000000000000000000)
    0x1937: v1937 = MLOAD v1904(0x40)
    0x193b: v193b(0x0) = SUB v1907, v1937
    0x193c: v193c(0x64) = CONST 
    0x193e: v193e(0x64) = ADD v193c(0x64), v193b(0x0)
    0x1940: REVERT v1937, v193e(0x64)

    Begin block 0x1941
    prev=[0x18e3], succ=[0x2ac0]
    =================================
    0x1942: v1942(0x1) = CONST 
    0x1944: v1944(0x1) = CONST 
    0x1946: v1946(0xa0) = CONST 
    0x1948: v1948(0x10000000000000000000000000000000000000000) = SHL v1946(0xa0), v1944(0x1)
    0x1949: v1949(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1948(0x10000000000000000000000000000000000000000), v1942(0x1)
    0x194b: v194b = AND v76b, v1949(0xffffffffffffffffffffffffffffffffffffffff)
    0x194c: v194c(0x0) = CONST 
    0x1950: MSTORE v194c(0x0), v194b
    0x1951: v1951(0xb) = CONST 
    0x1953: v1953(0x20) = CONST 
    0x1957: MSTORE v1953(0x20), v1951(0xb)
    0x1958: v1958(0x40) = CONST 
    0x195d: v195d = SHA3 v194c(0x0), v1958(0x40)
    0x195f: v195f = SLOAD v195d
    0x1963: SSTORE v195d, v770
    0x1965: v1965 = MLOAD v1958(0x40)
    0x1968: MSTORE v1965, v194b
    0x196b: v196b = ADD v1965, v1953(0x20)
    0x196e: MSTORE v196b, v195f
    0x1971: v1971 = ADD v1958(0x40), v1965
    0x1974: MSTORE v1971, v770
    0x1976: v1976 = MLOAD v1958(0x40)
    0x1979: v1979(0x6b846216a787efbb604ac42f7ff4ae1de7c0c65d6cb9339dd19969632fa24dff) = CONST 
    0x199e: v199e(0x0) = SUB v1965, v1976
    0x199f: v199f(0x60) = CONST 
    0x19a1: v19a1(0x60) = ADD v199f(0x60), v199e(0x0)
    0x19a3: LOG1 v1976, v19a1(0x60), v1979(0x6b846216a787efbb604ac42f7ff4ae1de7c0c65d6cb9339dd19969632fa24dff)
    0x19a7: JUMP v74a(0x2ac0)

    Begin block 0x2ac0
    prev=[0x1941], succ=[]
    =================================
    0x2ac1: STOP 

}

function addRelayer(address)() public {
    Begin block 0x775
    prev=[], succ=[0x77d, 0x781]
    =================================
    0x776: v776 = CALLVALUE 
    0x778: v778 = ISZERO v776
    0x779: v779(0x781) = CONST 
    0x77c: JUMPI v779(0x781), v778

    Begin block 0x77d
    prev=[0x775], succ=[]
    =================================
    0x77d: v77d(0x0) = CONST 
    0x780: REVERT v77d(0x0), v77d(0x0)

    Begin block 0x781
    prev=[0x775], succ=[0x794, 0x798]
    =================================
    0x783: v783(0x2ae1) = CONST 
    0x786: v786(0x4) = CONST 
    0x789: v789 = CALLDATASIZE 
    0x78a: v78a = SUB v789, v786(0x4)
    0x78b: v78b(0x20) = CONST 
    0x78e: v78e = LT v78a, v78b(0x20)
    0x78f: v78f = ISZERO v78e
    0x790: v790(0x798) = CONST 
    0x793: JUMPI v790(0x798), v78f

    Begin block 0x794
    prev=[0x781], succ=[]
    =================================
    0x794: v794(0x0) = CONST 
    0x797: REVERT v794(0x0), v794(0x0)

    Begin block 0x798
    prev=[0x781], succ=[0x19a8]
    =================================
    0x79a: v79a = CALLDATALOAD v786(0x4)
    0x79b: v79b(0x1) = CONST 
    0x79d: v79d(0x1) = CONST 
    0x79f: v79f(0xa0) = CONST 
    0x7a1: v7a1(0x10000000000000000000000000000000000000000) = SHL v79f(0xa0), v79d(0x1)
    0x7a2: v7a2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7a1(0x10000000000000000000000000000000000000000), v79b(0x1)
    0x7a3: v7a3 = AND v7a2(0xffffffffffffffffffffffffffffffffffffffff), v79a
    0x7a4: v7a4(0x19a8) = CONST 
    0x7a7: JUMP v7a4(0x19a8)

    Begin block 0x19a8
    prev=[0x798], succ=[0x19bb, 0x1a01]
    =================================
    0x19a9: v19a9(0x1) = CONST 
    0x19ab: v19ab = SLOAD v19a9(0x1)
    0x19ac: v19ac(0x1) = CONST 
    0x19ae: v19ae(0x1) = CONST 
    0x19b0: v19b0(0xa0) = CONST 
    0x19b2: v19b2(0x10000000000000000000000000000000000000000) = SHL v19b0(0xa0), v19ae(0x1)
    0x19b3: v19b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19b2(0x10000000000000000000000000000000000000000), v19ac(0x1)
    0x19b4: v19b4 = AND v19b3(0xffffffffffffffffffffffffffffffffffffffff), v19ab
    0x19b5: v19b5 = CALLER 
    0x19b6: v19b6 = EQ v19b5, v19b4
    0x19b7: v19b7(0x1a01) = CONST 
    0x19ba: JUMPI v19b7(0x1a01), v19b6

    Begin block 0x19bb
    prev=[0x19a8], succ=[]
    =================================
    0x19bb: v19bb(0x40) = CONST 
    0x19be: v19be = MLOAD v19bb(0x40)
    0x19bf: v19bf(0x461bcd) = CONST 
    0x19c3: v19c3(0xe5) = CONST 
    0x19c5: v19c5(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v19c3(0xe5), v19bf(0x461bcd)
    0x19c7: MSTORE v19be, v19c5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19c8: v19c8(0x20) = CONST 
    0x19ca: v19ca(0x4) = CONST 
    0x19cd: v19cd = ADD v19be, v19ca(0x4)
    0x19ce: MSTORE v19cd, v19c8(0x20)
    0x19cf: v19cf(0x17) = CONST 
    0x19d1: v19d1(0x24) = CONST 
    0x19d4: v19d4 = ADD v19be, v19d1(0x24)
    0x19d5: MSTORE v19d4, v19cf(0x17)
    0x19d6: v19d6(0x21b0b63632b91034b9903737ba103a34329030b236b4b7) = CONST 
    0x19ee: v19ee(0x49) = CONST 
    0x19f0: v19f0(0x43616c6c6572206973206e6f74207468652061646d696e000000000000000000) = SHL v19ee(0x49), v19d6(0x21b0b63632b91034b9903737ba103a34329030b236b4b7)
    0x19f1: v19f1(0x44) = CONST 
    0x19f4: v19f4 = ADD v19be, v19f1(0x44)
    0x19f5: MSTORE v19f4, v19f0(0x43616c6c6572206973206e6f74207468652061646d696e000000000000000000)
    0x19f7: v19f7 = MLOAD v19bb(0x40)
    0x19fb: v19fb(0x0) = SUB v19be, v19f7
    0x19fc: v19fc(0x64) = CONST 
    0x19fe: v19fe(0x64) = ADD v19fc(0x64), v19fb(0x0)
    0x1a00: REVERT v19f7, v19fe(0x64)

    Begin block 0x1a01
    prev=[0x19a8], succ=[0x2ae1]
    =================================
    0x1a02: v1a02(0x1) = CONST 
    0x1a04: v1a04(0x1) = CONST 
    0x1a06: v1a06(0xa0) = CONST 
    0x1a08: v1a08(0x10000000000000000000000000000000000000000) = SHL v1a06(0xa0), v1a04(0x1)
    0x1a09: v1a09(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a08(0x10000000000000000000000000000000000000000), v1a02(0x1)
    0x1a0b: v1a0b = AND v7a3, v1a09(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a0c: v1a0c(0x0) = CONST 
    0x1a10: MSTORE v1a0c(0x0), v1a0b
    0x1a11: v1a11(0x3) = CONST 
    0x1a13: v1a13(0x20) = CONST 
    0x1a17: MSTORE v1a13(0x20), v1a11(0x3)
    0x1a18: v1a18(0x40) = CONST 
    0x1a1d: v1a1d = SHA3 v1a0c(0x0), v1a18(0x40)
    0x1a1f: v1a1f = SLOAD v1a1d
    0x1a20: v1a20(0xff) = CONST 
    0x1a22: v1a22(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1a20(0xff)
    0x1a23: v1a23 = AND v1a22(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1a1f
    0x1a24: v1a24(0x1) = CONST 
    0x1a26: v1a26 = OR v1a24(0x1), v1a23
    0x1a28: SSTORE v1a1d, v1a26
    0x1a2a: v1a2a = MLOAD v1a18(0x40)
    0x1a2d: MSTORE v1a2a, v1a0b
    0x1a2f: v1a2f = MLOAD v1a18(0x40)
    0x1a30: v1a30(0x3580ee9f53a62b7cb409a2cb56f9be87747dd15017afc5cef6eef321e4fb2c5) = CONST 
    0x1a54: v1a54(0x0) = SUB v1a2a, v1a2f
    0x1a57: v1a57(0x20) = ADD v1a13(0x20), v1a54(0x0)
    0x1a59: LOG1 v1a2f, v1a57(0x20), v1a30(0x3580ee9f53a62b7cb409a2cb56f9be87747dd15017afc5cef6eef321e4fb2c5)
    0x1a5b: JUMP v783(0x2ae1)

    Begin block 0x2ae1
    prev=[0x1a01], succ=[]
    =================================
    0x2ae2: STOP 

}

function crossChainTransfer(address,uint256,address,uint8)() public {
    Begin block 0x7a8
    prev=[], succ=[0x7ba, 0x7be]
    =================================
    0x7a9: v7a9(0x2b02) = CONST 
    0x7ac: v7ac(0x4) = CONST 
    0x7af: v7af = CALLDATASIZE 
    0x7b0: v7b0 = SUB v7af, v7ac(0x4)
    0x7b1: v7b1(0x80) = CONST 
    0x7b4: v7b4 = LT v7b0, v7b1(0x80)
    0x7b5: v7b5 = ISZERO v7b4
    0x7b6: v7b6(0x7be) = CONST 
    0x7b9: JUMPI v7b6(0x7be), v7b5

    Begin block 0x7ba
    prev=[0x7a8], succ=[]
    =================================
    0x7ba: v7ba(0x0) = CONST 
    0x7bd: REVERT v7ba(0x0), v7ba(0x0)

    Begin block 0x7be
    prev=[0x7a8], succ=[0x1a5c]
    =================================
    0x7c1: v7c1 = CALLDATALOAD v7ac(0x4)
    0x7c2: v7c2(0x1) = CONST 
    0x7c4: v7c4(0x1) = CONST 
    0x7c6: v7c6(0xa0) = CONST 
    0x7c8: v7c8(0x10000000000000000000000000000000000000000) = SHL v7c6(0xa0), v7c4(0x1)
    0x7c9: v7c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7c8(0x10000000000000000000000000000000000000000), v7c2(0x1)
    0x7cc: v7cc = AND v7c9(0xffffffffffffffffffffffffffffffffffffffff), v7c1
    0x7ce: v7ce(0x20) = CONST 
    0x7d1: v7d1(0x24) = ADD v7ac(0x4), v7ce(0x20)
    0x7d2: v7d2 = CALLDATALOAD v7d1(0x24)
    0x7d4: v7d4(0x40) = CONST 
    0x7d7: v7d7(0x44) = ADD v7ac(0x4), v7d4(0x40)
    0x7d8: v7d8 = CALLDATALOAD v7d7(0x44)
    0x7d9: v7d9 = AND v7d8, v7c9(0xffffffffffffffffffffffffffffffffffffffff)
    0x7db: v7db(0x60) = CONST 
    0x7dd: v7dd(0x64) = ADD v7db(0x60), v7ac(0x4)
    0x7de: v7de = CALLDATALOAD v7dd(0x64)
    0x7df: v7df(0xff) = CONST 
    0x7e1: v7e1 = AND v7df(0xff), v7de
    0x7e2: v7e2(0x1a5c) = CONST 
    0x7e5: JUMP v7e2(0x1a5c)

    Begin block 0x1a5c
    prev=[0x7be], succ=[0x1a68, 0x1aa7]
    =================================
    0x1a5d: v1a5d(0xf) = CONST 
    0x1a5f: v1a5f = SLOAD v1a5d(0xf)
    0x1a60: v1a60(0xff) = CONST 
    0x1a62: v1a62 = AND v1a60(0xff), v1a5f
    0x1a63: v1a63 = ISZERO v1a62
    0x1a64: v1a64(0x1aa7) = CONST 
    0x1a67: JUMPI v1a64(0x1aa7), v1a63

    Begin block 0x1a68
    prev=[0x1a5c], succ=[]
    =================================
    0x1a68: v1a68(0x40) = CONST 
    0x1a6b: v1a6b = MLOAD v1a68(0x40)
    0x1a6c: v1a6c(0x461bcd) = CONST 
    0x1a70: v1a70(0xe5) = CONST 
    0x1a72: v1a72(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1a70(0xe5), v1a6c(0x461bcd)
    0x1a74: MSTORE v1a6b, v1a72(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a75: v1a75(0x20) = CONST 
    0x1a77: v1a77(0x4) = CONST 
    0x1a7a: v1a7a = ADD v1a6b, v1a77(0x4)
    0x1a7b: MSTORE v1a7a, v1a75(0x20)
    0x1a7c: v1a7c(0x10) = CONST 
    0x1a7e: v1a7e(0x24) = CONST 
    0x1a81: v1a81 = ADD v1a6b, v1a7e(0x24)
    0x1a82: MSTORE v1a81, v1a7c(0x10)
    0x1a83: v1a83(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0x1a94: v1a94(0x82) = CONST 
    0x1a96: v1a96(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL v1a94(0x82), v1a83(0x14185d5cd8589b194e881c185d5cd959)
    0x1a97: v1a97(0x44) = CONST 
    0x1a9a: v1a9a = ADD v1a6b, v1a97(0x44)
    0x1a9b: MSTORE v1a9a, v1a96(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x1a9d: v1a9d = MLOAD v1a68(0x40)
    0x1aa1: v1aa1(0x0) = SUB v1a6b, v1a9d
    0x1aa2: v1aa2(0x64) = CONST 
    0x1aa4: v1aa4(0x64) = ADD v1aa2(0x64), v1aa1(0x0)
    0x1aa6: REVERT v1a9d, v1aa4(0x64)

    Begin block 0x1aa7
    prev=[0x1a5c], succ=[0x1ac8, 0x1b04]
    =================================
    0x1aa8: v1aa8(0x1) = CONST 
    0x1aaa: v1aaa(0x1) = CONST 
    0x1aac: v1aac(0xa0) = CONST 
    0x1aae: v1aae(0x10000000000000000000000000000000000000000) = SHL v1aac(0xa0), v1aaa(0x1)
    0x1aaf: v1aaf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1aae(0x10000000000000000000000000000000000000000), v1aa8(0x1)
    0x1ab1: v1ab1 = AND v7cc, v1aaf(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ab2: v1ab2(0x0) = CONST 
    0x1ab6: MSTORE v1ab2(0x0), v1ab1
    0x1ab7: v1ab7(0x4) = CONST 
    0x1ab9: v1ab9(0x20) = CONST 
    0x1abb: MSTORE v1ab9(0x20), v1ab7(0x4)
    0x1abc: v1abc(0x40) = CONST 
    0x1abf: v1abf = SHA3 v1ab2(0x0), v1abc(0x40)
    0x1ac0: v1ac0 = SLOAD v1abf
    0x1ac1: v1ac1(0xff) = CONST 
    0x1ac3: v1ac3 = AND v1ac1(0xff), v1ac0
    0x1ac4: v1ac4(0x1b04) = CONST 
    0x1ac7: JUMPI v1ac4(0x1b04), v1ac3

    Begin block 0x1ac8
    prev=[0x1aa7], succ=[]
    =================================
    0x1ac8: v1ac8(0x40) = CONST 
    0x1acb: v1acb = MLOAD v1ac8(0x40)
    0x1acc: v1acc(0x461bcd) = CONST 
    0x1ad0: v1ad0(0xe5) = CONST 
    0x1ad2: v1ad2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1ad0(0xe5), v1acc(0x461bcd)
    0x1ad4: MSTORE v1acb, v1ad2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ad5: v1ad5(0x20) = CONST 
    0x1ad7: v1ad7(0x4) = CONST 
    0x1ada: v1ada = ADD v1acb, v1ad7(0x4)
    0x1adb: MSTORE v1ada, v1ad5(0x20)
    0x1adc: v1adc(0xd) = CONST 
    0x1ade: v1ade(0x24) = CONST 
    0x1ae1: v1ae1 = ADD v1acb, v1ade(0x24)
    0x1ae2: MSTORE v1ae1, v1adc(0xd)
    0x1ae3: v1ae3(0x24b73b30b634b2103a37b5b2b7) = CONST 
    0x1af1: v1af1(0x99) = CONST 
    0x1af3: v1af3(0x496e76616c696420746f6b656e00000000000000000000000000000000000000) = SHL v1af1(0x99), v1ae3(0x24b73b30b634b2103a37b5b2b7)
    0x1af4: v1af4(0x44) = CONST 
    0x1af7: v1af7 = ADD v1acb, v1af4(0x44)
    0x1af8: MSTORE v1af7, v1af3(0x496e76616c696420746f6b656e00000000000000000000000000000000000000)
    0x1afa: v1afa = MLOAD v1ac8(0x40)
    0x1afe: v1afe(0x0) = SUB v1acb, v1afa
    0x1aff: v1aff(0x64) = CONST 
    0x1b01: v1b01(0x64) = ADD v1aff(0x64), v1afe(0x0)
    0x1b03: REVERT v1afa, v1b01(0x64)

    Begin block 0x1b04
    prev=[0x1aa7], succ=[0x1b13, 0x1b14]
    =================================
    0x1b05: v1b05(0x5) = CONST 
    0x1b07: v1b07(0x0) = CONST 
    0x1b0a: v1b0a(0x2) = CONST 
    0x1b0d: v1b0d = GT v7e1, v1b0a(0x2)
    0x1b0e: v1b0e = ISZERO v1b0d
    0x1b0f: v1b0f(0x1b14) = CONST 
    0x1b12: JUMPI v1b0f(0x1b14), v1b0e

    Begin block 0x1b13
    prev=[0x1b04], succ=[]
    =================================
    0x1b13: THROW 

    Begin block 0x1b14
    prev=[0x1b04], succ=[0x1b1e, 0x1b1f]
    =================================
    0x1b15: v1b15(0x2) = CONST 
    0x1b18: v1b18 = GT v7e1, v1b15(0x2)
    0x1b19: v1b19 = ISZERO v1b18
    0x1b1a: v1b1a(0x1b1f) = CONST 
    0x1b1d: JUMPI v1b1a(0x1b1f), v1b19

    Begin block 0x1b1e
    prev=[0x1b14], succ=[]
    =================================
    0x1b1e: THROW 

    Begin block 0x1b1f
    prev=[0x1b14], succ=[0x1b38, 0x1b74]
    =================================
    0x1b21: MSTORE v1b07(0x0), v7e1
    0x1b22: v1b22(0x20) = CONST 
    0x1b25: v1b25(0x20) = ADD v1b07(0x0), v1b22(0x20)
    0x1b29: MSTORE v1b25(0x20), v1b05(0x5)
    0x1b2a: v1b2a(0x40) = CONST 
    0x1b2c: v1b2c(0x40) = ADD v1b2a(0x40), v1b07(0x0)
    0x1b2d: v1b2d(0x0) = CONST 
    0x1b2f: v1b2f = SHA3 v1b2d(0x0), v1b2c(0x40)
    0x1b30: v1b30 = SLOAD v1b2f
    0x1b31: v1b31(0xff) = CONST 
    0x1b33: v1b33 = AND v1b31(0xff), v1b30
    0x1b34: v1b34(0x1b74) = CONST 
    0x1b37: JUMPI v1b34(0x1b74), v1b33

    Begin block 0x1b38
    prev=[0x1b1f], succ=[]
    =================================
    0x1b38: v1b38(0x40) = CONST 
    0x1b3b: v1b3b = MLOAD v1b38(0x40)
    0x1b3c: v1b3c(0x461bcd) = CONST 
    0x1b40: v1b40(0xe5) = CONST 
    0x1b42: v1b42(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1b40(0xe5), v1b3c(0x461bcd)
    0x1b44: MSTORE v1b3b, v1b42(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b45: v1b45(0x20) = CONST 
    0x1b47: v1b47(0x4) = CONST 
    0x1b4a: v1b4a = ADD v1b3b, v1b47(0x4)
    0x1b4b: MSTORE v1b4a, v1b45(0x20)
    0x1b4c: v1b4c(0xd) = CONST 
    0x1b4e: v1b4e(0x24) = CONST 
    0x1b51: v1b51 = ADD v1b3b, v1b4e(0x24)
    0x1b52: MSTORE v1b51, v1b4c(0xd)
    0x1b53: v1b53(0x24b73b30b634b21031b430b4b7) = CONST 
    0x1b61: v1b61(0x99) = CONST 
    0x1b63: v1b63(0x496e76616c696420636861696e00000000000000000000000000000000000000) = SHL v1b61(0x99), v1b53(0x24b73b30b634b21031b430b4b7)
    0x1b64: v1b64(0x44) = CONST 
    0x1b67: v1b67 = ADD v1b3b, v1b64(0x44)
    0x1b68: MSTORE v1b67, v1b63(0x496e76616c696420636861696e00000000000000000000000000000000000000)
    0x1b6a: v1b6a = MLOAD v1b38(0x40)
    0x1b6e: v1b6e(0x0) = SUB v1b3b, v1b6a
    0x1b6f: v1b6f(0x64) = CONST 
    0x1b71: v1b71(0x64) = ADD v1b6f(0x64), v1b6e(0x0)
    0x1b73: REVERT v1b6a, v1b71(0x64)

    Begin block 0x1b74
    prev=[0x1b1f], succ=[0x1b83, 0x1b84]
    =================================
    0x1b75: v1b75(0x8) = CONST 
    0x1b77: v1b77(0x0) = CONST 
    0x1b7a: v1b7a(0x2) = CONST 
    0x1b7d: v1b7d = GT v7e1, v1b7a(0x2)
    0x1b7e: v1b7e = ISZERO v1b7d
    0x1b7f: v1b7f(0x1b84) = CONST 
    0x1b82: JUMPI v1b7f(0x1b84), v1b7e

    Begin block 0x1b83
    prev=[0x1b74], succ=[]
    =================================
    0x1b83: THROW 

    Begin block 0x1b84
    prev=[0x1b74], succ=[0x1b8e, 0x1b8f]
    =================================
    0x1b85: v1b85(0x2) = CONST 
    0x1b88: v1b88 = GT v7e1, v1b85(0x2)
    0x1b89: v1b89 = ISZERO v1b88
    0x1b8a: v1b8a(0x1b8f) = CONST 
    0x1b8d: JUMPI v1b8a(0x1b8f), v1b89

    Begin block 0x1b8e
    prev=[0x1b84], succ=[]
    =================================
    0x1b8e: THROW 

    Begin block 0x1b8f
    prev=[0x1b84], succ=[0x1ba6, 0x1be6]
    =================================
    0x1b91: MSTORE v1b77(0x0), v7e1
    0x1b92: v1b92(0x20) = CONST 
    0x1b94: v1b94(0x20) = ADD v1b92(0x20), v1b77(0x0)
    0x1b97: MSTORE v1b94(0x20), v1b75(0x8)
    0x1b98: v1b98(0x20) = CONST 
    0x1b9a: v1b9a(0x40) = ADD v1b98(0x20), v1b94(0x20)
    0x1b9b: v1b9b(0x0) = CONST 
    0x1b9d: v1b9d = SHA3 v1b9b(0x0), v1b9a(0x40)
    0x1b9e: v1b9e = SLOAD v1b9d
    0x1b9f: v1b9f = CALLVALUE 
    0x1ba0: v1ba0 = LT v1b9f, v1b9e
    0x1ba1: v1ba1 = ISZERO v1ba0
    0x1ba2: v1ba2(0x1be6) = CONST 
    0x1ba5: JUMPI v1ba2(0x1be6), v1ba1

    Begin block 0x1ba6
    prev=[0x1b8f], succ=[]
    =================================
    0x1ba6: v1ba6(0x40) = CONST 
    0x1ba9: v1ba9 = MLOAD v1ba6(0x40)
    0x1baa: v1baa(0x461bcd) = CONST 
    0x1bae: v1bae(0xe5) = CONST 
    0x1bb0: v1bb0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1bae(0xe5), v1baa(0x461bcd)
    0x1bb2: MSTORE v1ba9, v1bb0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1bb3: v1bb3(0x20) = CONST 
    0x1bb5: v1bb5(0x4) = CONST 
    0x1bb8: v1bb8 = ADD v1ba9, v1bb5(0x4)
    0x1bb9: MSTORE v1bb8, v1bb3(0x20)
    0x1bba: v1bba(0x11) = CONST 
    0x1bbc: v1bbc(0x24) = CONST 
    0x1bbf: v1bbf = ADD v1ba9, v1bbc(0x24)
    0x1bc0: MSTORE v1bbf, v1bba(0x11)
    0x1bc1: v1bc1(0x8ccaca40d2e640dcdee840cadcdeeaced) = CONST 
    0x1bd3: v1bd3(0x7b) = CONST 
    0x1bd5: v1bd5(0x466565206973206e6f7420656e6f756768000000000000000000000000000000) = SHL v1bd3(0x7b), v1bc1(0x8ccaca40d2e640dcdee840cadcdeeaced)
    0x1bd6: v1bd6(0x44) = CONST 
    0x1bd9: v1bd9 = ADD v1ba9, v1bd6(0x44)
    0x1bda: MSTORE v1bd9, v1bd5(0x466565206973206e6f7420656e6f756768000000000000000000000000000000)
    0x1bdc: v1bdc = MLOAD v1ba6(0x40)
    0x1be0: v1be0(0x0) = SUB v1ba9, v1bdc
    0x1be1: v1be1(0x64) = CONST 
    0x1be3: v1be3(0x64) = ADD v1be1(0x64), v1be0(0x0)
    0x1be5: REVERT v1bdc, v1be3(0x64)

    Begin block 0x1be6
    prev=[0x1b8f], succ=[0x2282B0x1be6]
    =================================
    0x1be7: v1be7(0x1bf0) = CONST 
    0x1bec: v1bec(0x2282) = CONST 
    0x1bef: JUMP v1bec(0x2282)

    Begin block 0x2282B0x1be6
    prev=[0x1be6], succ=[0x22a3B0x1be6, 0x22d9B0x1be6]
    =================================
    0x2283S0x1be6: v2283V1be6(0x1) = CONST 
    0x2285S0x1be6: v2285V1be6(0x1) = CONST 
    0x2287S0x1be6: v2287V1be6(0xa0) = CONST 
    0x2289S0x1be6: v2289V1be6(0x10000000000000000000000000000000000000000) = SHL v2287V1be6(0xa0), v2285V1be6(0x1)
    0x228aS0x1be6: v228aV1be6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2289V1be6(0x10000000000000000000000000000000000000000), v2283V1be6(0x1)
    0x228cS0x1be6: v228cV1be6 = AND v7cc, v228aV1be6(0xffffffffffffffffffffffffffffffffffffffff)
    0x228dS0x1be6: v228dV1be6(0x0) = CONST 
    0x2291S0x1be6: MSTORE v228dV1be6(0x0), v228cV1be6
    0x2292S0x1be6: v2292V1be6(0xa) = CONST 
    0x2294S0x1be6: v2294V1be6(0x20) = CONST 
    0x2296S0x1be6: MSTORE v2294V1be6(0x20), v2292V1be6(0xa)
    0x2297S0x1be6: v2297V1be6(0x40) = CONST 
    0x229aS0x1be6: v229aV1be6 = SHA3 v228dV1be6(0x0), v2297V1be6(0x40)
    0x229bS0x1be6: v229bV1be6 = SLOAD v229aV1be6
    0x229dS0x1be6: v229dV1be6 = GT v7d2, v229bV1be6
    0x229eS0x1be6: v229eV1be6 = ISZERO v229dV1be6
    0x229fS0x1be6: v229fV1be6(0x22d9) = CONST 
    0x22a2S0x1be6: JUMPI v229fV1be6(0x22d9), v229eV1be6

    Begin block 0x22a3B0x1be6
    prev=[0x2282B0x1be6], succ=[]
    =================================
    0x22a3S0x1be6: v22a3V1be6(0x40) = CONST 
    0x22a5S0x1be6: v22a5V1be6 = MLOAD v22a3V1be6(0x40)
    0x22a6S0x1be6: v22a6V1be6(0x461bcd) = CONST 
    0x22aaS0x1be6: v22aaV1be6(0xe5) = CONST 
    0x22acS0x1be6: v22acV1be6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v22aaV1be6(0xe5), v22a6V1be6(0x461bcd)
    0x22aeS0x1be6: MSTORE v22a5V1be6, v22acV1be6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22afS0x1be6: v22afV1be6(0x4) = CONST 
    0x22b1S0x1be6: v22b1V1be6 = ADD v22afV1be6(0x4), v22a5V1be6
    0x22b4S0x1be6: v22b4V1be6(0x20) = CONST 
    0x22b6S0x1be6: v22b6V1be6 = ADD v22b4V1be6(0x20), v22b1V1be6
    0x22b9S0x1be6: v22b9V1be6(0x20) = SUB v22b6V1be6, v22b1V1be6
    0x22bbS0x1be6: MSTORE v22b1V1be6, v22b9V1be6(0x20)
    0x22bcS0x1be6: v22bcV1be6(0x21) = CONST 
    0x22bfS0x1be6: MSTORE v22b6V1be6, v22bcV1be6(0x21)
    0x22c0S0x1be6: v22c0V1be6(0x20) = CONST 
    0x22c2S0x1be6: v22c2V1be6 = ADD v22c0V1be6(0x20), v22b6V1be6
    0x22c4S0x1be6: v22c4V1be6(0x251a) = CONST 
    0x22c7S0x1be6: v22c7V1be6(0x21) = CONST 
    0x22caS0x1be6: CODECOPY v22c2V1be6, v22c4V1be6(0x251a), v22c7V1be6(0x21)
    0x22cbS0x1be6: v22cbV1be6(0x40) = CONST 
    0x22cdS0x1be6: v22cdV1be6 = ADD v22cbV1be6(0x40), v22c2V1be6
    0x22d1S0x1be6: v22d1V1be6(0x40) = CONST 
    0x22d3S0x1be6: v22d3V1be6 = MLOAD v22d1V1be6(0x40)
    0x22d6S0x1be6: v22d6V1be6(0x84) = SUB v22cdV1be6, v22d3V1be6
    0x22d8S0x1be6: REVERT v22d3V1be6, v22d6V1be6(0x84)

    Begin block 0x22d9B0x1be6
    prev=[0x2282B0x1be6], succ=[0x22faB0x1be6, 0x2cf8B0x1be6]
    =================================
    0x22daS0x1be6: v22daV1be6(0x1) = CONST 
    0x22dcS0x1be6: v22dcV1be6(0x1) = CONST 
    0x22deS0x1be6: v22deV1be6(0xa0) = CONST 
    0x22e0S0x1be6: v22e0V1be6(0x10000000000000000000000000000000000000000) = SHL v22deV1be6(0xa0), v22dcV1be6(0x1)
    0x22e1S0x1be6: v22e1V1be6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22e0V1be6(0x10000000000000000000000000000000000000000), v22daV1be6(0x1)
    0x22e3S0x1be6: v22e3V1be6 = AND v7cc, v22e1V1be6(0xffffffffffffffffffffffffffffffffffffffff)
    0x22e4S0x1be6: v22e4V1be6(0x0) = CONST 
    0x22e8S0x1be6: MSTORE v22e4V1be6(0x0), v22e3V1be6
    0x22e9S0x1be6: v22e9V1be6(0xb) = CONST 
    0x22ebS0x1be6: v22ebV1be6(0x20) = CONST 
    0x22edS0x1be6: MSTORE v22ebV1be6(0x20), v22e9V1be6(0xb)
    0x22eeS0x1be6: v22eeV1be6(0x40) = CONST 
    0x22f1S0x1be6: v22f1V1be6 = SHA3 v22e4V1be6(0x0), v22eeV1be6(0x40)
    0x22f2S0x1be6: v22f2V1be6 = SLOAD v22f1V1be6
    0x22f4S0x1be6: v22f4V1be6 = LT v7d2, v22f2V1be6
    0x22f5S0x1be6: v22f5V1be6 = ISZERO v22f4V1be6
    0x22f6S0x1be6: v22f6V1be6(0x2cf8) = CONST 
    0x22f9S0x1be6: JUMPI v22f6V1be6(0x2cf8), v22f5V1be6

    Begin block 0x22faB0x1be6
    prev=[0x22d9B0x1be6], succ=[]
    =================================
    0x22faS0x1be6: v22faV1be6(0x40) = CONST 
    0x22fdS0x1be6: v22fdV1be6 = MLOAD v22faV1be6(0x40)
    0x22feS0x1be6: v22feV1be6(0x461bcd) = CONST 
    0x2302S0x1be6: v2302V1be6(0xe5) = CONST 
    0x2304S0x1be6: v2304V1be6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2302V1be6(0xe5), v22feV1be6(0x461bcd)
    0x2306S0x1be6: MSTORE v22fdV1be6, v2304V1be6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2307S0x1be6: v2307V1be6(0x20) = CONST 
    0x2309S0x1be6: v2309V1be6(0x4) = CONST 
    0x230cS0x1be6: v230cV1be6 = ADD v22fdV1be6, v2309V1be6(0x4)
    0x230dS0x1be6: MSTORE v230cV1be6, v2307V1be6(0x20)
    0x230eS0x1be6: v230eV1be6(0x1e) = CONST 
    0x2310S0x1be6: v2310V1be6(0x24) = CONST 
    0x2313S0x1be6: v2313V1be6 = ADD v22fdV1be6, v2310V1be6(0x24)
    0x2314S0x1be6: MSTORE v2313V1be6, v230eV1be6(0x1e)
    0x2315S0x1be6: v2315V1be6(0x416d6f756e74206973206c657373207468616e206d696e20616d6f756e740000) = CONST 
    0x2336S0x1be6: v2336V1be6(0x44) = CONST 
    0x2339S0x1be6: v2339V1be6 = ADD v22fdV1be6, v2336V1be6(0x44)
    0x233aS0x1be6: MSTORE v2339V1be6, v2315V1be6(0x416d6f756e74206973206c657373207468616e206d696e20616d6f756e740000)
    0x233cS0x1be6: v233cV1be6 = MLOAD v22faV1be6(0x40)
    0x2340S0x1be6: v2340V1be6(0x0) = SUB v22fdV1be6, v233cV1be6
    0x2341S0x1be6: v2341V1be6(0x64) = CONST 
    0x2343S0x1be6: v2343V1be6(0x64) = ADD v2341V1be6(0x64), v2340V1be6(0x0)
    0x2345S0x1be6: REVERT v233cV1be6, v2343V1be6(0x64)

    Begin block 0x2cf8B0x1be6
    prev=[0x22d9B0x1be6], succ=[0x1bf0]
    =================================
    0x2cfdS0x1be6: JUMP v1be7(0x1bf0)

    Begin block 0x1bf0
    prev=[0x2cf8B0x1be6], succ=[0x1c18]
    =================================
    0x1bf2: v1bf2(0x1) = CONST 
    0x1bf4: v1bf4(0x1) = CONST 
    0x1bf6: v1bf6(0xa0) = CONST 
    0x1bf8: v1bf8(0x10000000000000000000000000000000000000000) = SHL v1bf6(0xa0), v1bf4(0x1)
    0x1bf9: v1bf9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1bf8(0x10000000000000000000000000000000000000000), v1bf2(0x1)
    0x1bfb: v1bfb = AND v7cc, v1bf9(0xffffffffffffffffffffffffffffffffffffffff)
    0x1bfc: v1bfc(0x0) = CONST 
    0x1c00: MSTORE v1bfc(0x0), v1bfb
    0x1c01: v1c01(0xc) = CONST 
    0x1c03: v1c03(0x20) = CONST 
    0x1c05: MSTORE v1c03(0x20), v1c01(0xc)
    0x1c06: v1c06(0x40) = CONST 
    0x1c09: v1c09 = SHA3 v1bfc(0x0), v1c06(0x40)
    0x1c0a: v1c0a = SLOAD v1c09
    0x1c0d: v1c0d(0x1c18) = CONST 
    0x1c14: v1c14(0x21cb) = CONST 
    0x1c17: v1c17_0, v1c17_1 = CALLPRIVATE v1c14(0x21cb), v7d2, v1c0a, v7cc, v1c0d(0x1c18)

    Begin block 0x1c18
    prev=[0x1bf0], succ=[0x1c27, 0x1c28]
    =================================
    0x1c1e: v1c1e(0x2) = CONST 
    0x1c21: v1c21 = GT v1c17_1, v1c1e(0x2)
    0x1c22: v1c22 = ISZERO v1c21
    0x1c23: v1c23(0x1c28) = CONST 
    0x1c26: JUMPI v1c23(0x1c28), v1c22

    Begin block 0x1c27
    prev=[0x1c18], succ=[]
    =================================
    0x1c27: THROW 

    Begin block 0x1c28
    prev=[0x1c18], succ=[0x1c2e, 0x1c64]
    =================================
    0x1c29: v1c29 = ISZERO v1c17_1
    0x1c2a: v1c2a(0x1c64) = CONST 
    0x1c2d: JUMPI v1c2a(0x1c64), v1c29

    Begin block 0x1c2e
    prev=[0x1c28], succ=[]
    =================================
    0x1c2e: v1c2e(0x40) = CONST 
    0x1c30: v1c30 = MLOAD v1c2e(0x40)
    0x1c31: v1c31(0x461bcd) = CONST 
    0x1c35: v1c35(0xe5) = CONST 
    0x1c37: v1c37(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1c35(0xe5), v1c31(0x461bcd)
    0x1c39: MSTORE v1c30, v1c37(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c3a: v1c3a(0x4) = CONST 
    0x1c3c: v1c3c = ADD v1c3a(0x4), v1c30
    0x1c3f: v1c3f(0x20) = CONST 
    0x1c41: v1c41 = ADD v1c3f(0x20), v1c3c
    0x1c44: v1c44(0x20) = SUB v1c41, v1c3c
    0x1c46: MSTORE v1c3c, v1c44(0x20)
    0x1c47: v1c47(0x2f) = CONST 
    0x1c4a: MSTORE v1c41, v1c47(0x2f)
    0x1c4b: v1c4b(0x20) = CONST 
    0x1c4d: v1c4d = ADD v1c4b(0x20), v1c41
    0x1c4f: v1c4f(0x24eb) = CONST 
    0x1c52: v1c52(0x2f) = CONST 
    0x1c55: CODECOPY v1c4d, v1c4f(0x24eb), v1c52(0x2f)
    0x1c56: v1c56(0x40) = CONST 
    0x1c58: v1c58 = ADD v1c56(0x40), v1c4d
    0x1c5c: v1c5c(0x40) = CONST 
    0x1c5e: v1c5e = MLOAD v1c5c(0x40)
    0x1c61: v1c61(0x84) = SUB v1c58, v1c5e
    0x1c63: REVERT v1c5e, v1c61(0x84)

    Begin block 0x1c64
    prev=[0x1c28], succ=[0x1cc2, 0x1cc6]
    =================================
    0x1c65: v1c65(0x1) = CONST 
    0x1c67: v1c67(0x1) = CONST 
    0x1c69: v1c69(0xa0) = CONST 
    0x1c6b: v1c6b(0x10000000000000000000000000000000000000000) = SHL v1c69(0xa0), v1c67(0x1)
    0x1c6c: v1c6c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c6b(0x10000000000000000000000000000000000000000), v1c65(0x1)
    0x1c6e: v1c6e = AND v7cc, v1c6c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c6f: v1c6f(0x0) = CONST 
    0x1c73: MSTORE v1c6f(0x0), v1c6e
    0x1c74: v1c74(0xc) = CONST 
    0x1c76: v1c76(0x20) = CONST 
    0x1c7a: MSTORE v1c76(0x20), v1c74(0xc)
    0x1c7b: v1c7b(0x40) = CONST 
    0x1c7f: v1c7f = SHA3 v1c6f(0x0), v1c7b(0x40)
    0x1c82: SSTORE v1c7f, v1c17_0
    0x1c84: v1c84 = MLOAD v1c7b(0x40)
    0x1c85: v1c85(0x23b872dd) = CONST 
    0x1c8a: v1c8a(0xe0) = CONST 
    0x1c8c: v1c8c(0x23b872dd00000000000000000000000000000000000000000000000000000000) = SHL v1c8a(0xe0), v1c85(0x23b872dd)
    0x1c8e: MSTORE v1c84, v1c8c(0x23b872dd00000000000000000000000000000000000000000000000000000000)
    0x1c8f: v1c8f = CALLER 
    0x1c90: v1c90(0x4) = CONST 
    0x1c93: v1c93 = ADD v1c84, v1c90(0x4)
    0x1c94: MSTORE v1c93, v1c8f
    0x1c95: v1c95 = ADDRESS 
    0x1c96: v1c96(0x24) = CONST 
    0x1c99: v1c99 = ADD v1c84, v1c96(0x24)
    0x1c9a: MSTORE v1c99, v1c95
    0x1c9b: v1c9b(0x44) = CONST 
    0x1c9e: v1c9e = ADD v1c84, v1c9b(0x44)
    0x1ca1: MSTORE v1c9e, v7d2
    0x1ca3: v1ca3 = MLOAD v1c7b(0x40)
    0x1ca4: v1ca4(0x23b872dd) = CONST 
    0x1caa: v1caa(0x64) = CONST 
    0x1cae: v1cae = ADD v1c84, v1caa(0x64)
    0x1cb3: v1cb3(0x0) = SUB v1c84, v1ca3
    0x1cb4: v1cb4(0x64) = ADD v1cb3(0x0), v1caa(0x64)
    0x1cba: v1cba = EXTCODESIZE v1c6e
    0x1cbb: v1cbb = ISZERO v1cba
    0x1cbd: v1cbd = ISZERO v1cbb
    0x1cbe: v1cbe(0x1cc6) = CONST 
    0x1cc1: JUMPI v1cbe(0x1cc6), v1cbd

    Begin block 0x1cc2
    prev=[0x1c64], succ=[]
    =================================
    0x1cc2: v1cc2(0x0) = CONST 
    0x1cc5: REVERT v1cc2(0x0), v1cc2(0x0)

    Begin block 0x1cc6
    prev=[0x1c64], succ=[0x1cd1, 0x1cda]
    =================================
    0x1cc8: v1cc8 = GAS 
    0x1cc9: v1cc9 = CALL v1cc8, v1c6e, v1c6f(0x0), v1ca3, v1cb4(0x64), v1ca3, v1c76(0x20)
    0x1cca: v1cca = ISZERO v1cc9
    0x1ccc: v1ccc = ISZERO v1cca
    0x1ccd: v1ccd(0x1cda) = CONST 
    0x1cd0: JUMPI v1ccd(0x1cda), v1ccc

    Begin block 0x1cd1
    prev=[0x1cc6], succ=[]
    =================================
    0x1cd1: v1cd1 = RETURNDATASIZE 
    0x1cd2: v1cd2(0x0) = CONST 
    0x1cd5: RETURNDATACOPY v1cd2(0x0), v1cd2(0x0), v1cd1
    0x1cd6: v1cd6 = RETURNDATASIZE 
    0x1cd7: v1cd7(0x0) = CONST 
    0x1cd9: REVERT v1cd7(0x0), v1cd6

    Begin block 0x1cda
    prev=[0x1cc6], succ=[0x1cec, 0x1cf0]
    =================================
    0x1cdf: v1cdf(0x40) = CONST 
    0x1ce1: v1ce1 = MLOAD v1cdf(0x40)
    0x1ce2: v1ce2 = RETURNDATASIZE 
    0x1ce3: v1ce3(0x20) = CONST 
    0x1ce6: v1ce6 = LT v1ce2, v1ce3(0x20)
    0x1ce7: v1ce7 = ISZERO v1ce6
    0x1ce8: v1ce8(0x1cf0) = CONST 
    0x1ceb: JUMPI v1ce8(0x1cf0), v1ce7

    Begin block 0x1cec
    prev=[0x1cda], succ=[]
    =================================
    0x1cec: v1cec(0x0) = CONST 
    0x1cef: REVERT v1cec(0x0), v1cec(0x0)

    Begin block 0x1cf0
    prev=[0x1cda], succ=[0x1d45, 0x1d46]
    =================================
    0x1cf3: v1cf3(0x40) = CONST 
    0x1cf6: v1cf6 = MLOAD v1cf3(0x40)
    0x1cf9: MSTORE v1cf6, v7d2
    0x1cfa: v1cfa(0x1) = CONST 
    0x1cfc: v1cfc(0x1) = CONST 
    0x1cfe: v1cfe(0xa0) = CONST 
    0x1d00: v1d00(0x10000000000000000000000000000000000000000) = SHL v1cfe(0xa0), v1cfc(0x1)
    0x1d01: v1d01(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d00(0x10000000000000000000000000000000000000000), v1cfa(0x1)
    0x1d04: v1d04 = AND v1d01(0xffffffffffffffffffffffffffffffffffffffff), v7d9
    0x1d05: v1d05(0x20) = CONST 
    0x1d08: v1d08 = ADD v1cf6, v1d05(0x20)
    0x1d09: MSTORE v1d08, v1d04
    0x1d0b: v1d0b = AND v7cc, v1d01(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d0d: v1d0d = CALLER 
    0x1d0f: v1d0f(0x6e21f653fa8ed1281f4a8f23203ec9bc5da09605de93f278dc2a234bbc161e7f) = CONST 
    0x1d37: v1d37 = CALLVALUE 
    0x1d3a: v1d3a = ADD v1cf6, v1cf3(0x40)
    0x1d3c: v1d3c(0x2) = CONST 
    0x1d3f: v1d3f = GT v7e1, v1d3c(0x2)
    0x1d40: v1d40 = ISZERO v1d3f
    0x1d41: v1d41(0x1d46) = CONST 
    0x1d44: JUMPI v1d41(0x1d46), v1d40

    Begin block 0x1d45
    prev=[0x1cf0], succ=[]
    =================================
    0x1d45: THROW 

    Begin block 0x1d46
    prev=[0x1cf0], succ=[0x2b02]
    =================================
    0x1d48: MSTORE v1d3a, v7e1
    0x1d49: v1d49(0x20) = CONST 
    0x1d4b: v1d4b = ADD v1d49(0x20), v1d3a
    0x1d4e: MSTORE v1d4b, v1d37
    0x1d4f: v1d4f(0x20) = CONST 
    0x1d51: v1d51 = ADD v1d4f(0x20), v1d4b
    0x1d58: v1d58(0x40) = CONST 
    0x1d5a: v1d5a = MLOAD v1d58(0x40)
    0x1d5d: v1d5d(0x80) = SUB v1d51, v1d5a
    0x1d5f: LOG3 v1d5a, v1d5d(0x80), v1d0f(0x6e21f653fa8ed1281f4a8f23203ec9bc5da09605de93f278dc2a234bbc161e7f), v1d0d, v1d0b
    0x1d66: JUMP v7a9(0x2b02)

    Begin block 0x2b02
    prev=[0x1d46], succ=[]
    =================================
    0x2b03: STOP 

}

function sendTotalAmount(address)() public {
    Begin block 0x7e6
    prev=[], succ=[0x7ee, 0x7f2]
    =================================
    0x7e7: v7e7 = CALLVALUE 
    0x7e9: v7e9 = ISZERO v7e7
    0x7ea: v7ea(0x7f2) = CONST 
    0x7ed: JUMPI v7ea(0x7f2), v7e9

    Begin block 0x7ee
    prev=[0x7e6], succ=[]
    =================================
    0x7ee: v7ee(0x0) = CONST 
    0x7f1: REVERT v7ee(0x0), v7ee(0x0)

    Begin block 0x7f2
    prev=[0x7e6], succ=[0x805, 0x809]
    =================================
    0x7f4: v7f4(0x2b23) = CONST 
    0x7f7: v7f7(0x4) = CONST 
    0x7fa: v7fa = CALLDATASIZE 
    0x7fb: v7fb = SUB v7fa, v7f7(0x4)
    0x7fc: v7fc(0x20) = CONST 
    0x7ff: v7ff = LT v7fb, v7fc(0x20)
    0x800: v800 = ISZERO v7ff
    0x801: v801(0x809) = CONST 
    0x804: JUMPI v801(0x809), v800

    Begin block 0x805
    prev=[0x7f2], succ=[]
    =================================
    0x805: v805(0x0) = CONST 
    0x808: REVERT v805(0x0), v805(0x0)

    Begin block 0x809
    prev=[0x7f2], succ=[0x1d67]
    =================================
    0x80b: v80b = CALLDATALOAD v7f7(0x4)
    0x80c: v80c(0x1) = CONST 
    0x80e: v80e(0x1) = CONST 
    0x810: v810(0xa0) = CONST 
    0x812: v812(0x10000000000000000000000000000000000000000) = SHL v810(0xa0), v80e(0x1)
    0x813: v813(0xffffffffffffffffffffffffffffffffffffffff) = SUB v812(0x10000000000000000000000000000000000000000), v80c(0x1)
    0x814: v814 = AND v813(0xffffffffffffffffffffffffffffffffffffffff), v80b
    0x815: v815(0x1d67) = CONST 
    0x818: JUMP v815(0x1d67)

    Begin block 0x1d67
    prev=[0x809], succ=[0x2b23]
    =================================
    0x1d68: v1d68(0xc) = CONST 
    0x1d6a: v1d6a(0x20) = CONST 
    0x1d6c: MSTORE v1d6a(0x20), v1d68(0xc)
    0x1d6d: v1d6d(0x0) = CONST 
    0x1d71: MSTORE v1d6d(0x0), v814
    0x1d72: v1d72(0x40) = CONST 
    0x1d75: v1d75 = SHA3 v1d6d(0x0), v1d72(0x40)
    0x1d76: v1d76 = SLOAD v1d75
    0x1d78: JUMP v7f4(0x2b23)

    Begin block 0x2b23
    prev=[0x1d67], succ=[]
    =================================
    0x2b24: v2b24(0x40) = CONST 
    0x2b27: v2b27 = MLOAD v2b24(0x40)
    0x2b2a: MSTORE v2b27, v1d76
    0x2b2b: v2b2b = MLOAD v2b24(0x40)
    0x2b2f: v2b2f(0x0) = SUB v2b27, v2b2b
    0x2b30: v2b30(0x20) = CONST 
    0x2b32: v2b32(0x20) = ADD v2b30(0x20), v2b2f(0x0)
    0x2b34: RETURN v2b2b, v2b32(0x20)

}

function maxAmountPerDay(address)() public {
    Begin block 0x819
    prev=[], succ=[0x821, 0x825]
    =================================
    0x81a: v81a = CALLVALUE 
    0x81c: v81c = ISZERO v81a
    0x81d: v81d(0x825) = CONST 
    0x820: JUMPI v81d(0x825), v81c

    Begin block 0x821
    prev=[0x819], succ=[]
    =================================
    0x821: v821(0x0) = CONST 
    0x824: REVERT v821(0x0), v821(0x0)

    Begin block 0x825
    prev=[0x819], succ=[0x838, 0x83c]
    =================================
    0x827: v827(0x2b54) = CONST 
    0x82a: v82a(0x4) = CONST 
    0x82d: v82d = CALLDATASIZE 
    0x82e: v82e = SUB v82d, v82a(0x4)
    0x82f: v82f(0x20) = CONST 
    0x832: v832 = LT v82e, v82f(0x20)
    0x833: v833 = ISZERO v832
    0x834: v834(0x83c) = CONST 
    0x837: JUMPI v834(0x83c), v833

    Begin block 0x838
    prev=[0x825], succ=[]
    =================================
    0x838: v838(0x0) = CONST 
    0x83b: REVERT v838(0x0), v838(0x0)

    Begin block 0x83c
    prev=[0x825], succ=[0x1d79]
    =================================
    0x83e: v83e = CALLDATALOAD v82a(0x4)
    0x83f: v83f(0x1) = CONST 
    0x841: v841(0x1) = CONST 
    0x843: v843(0xa0) = CONST 
    0x845: v845(0x10000000000000000000000000000000000000000) = SHL v843(0xa0), v841(0x1)
    0x846: v846(0xffffffffffffffffffffffffffffffffffffffff) = SUB v845(0x10000000000000000000000000000000000000000), v83f(0x1)
    0x847: v847 = AND v846(0xffffffffffffffffffffffffffffffffffffffff), v83e
    0x848: v848(0x1d79) = CONST 
    0x84b: JUMP v848(0x1d79)

    Begin block 0x1d79
    prev=[0x83c], succ=[0x2b54]
    =================================
    0x1d7a: v1d7a(0x9) = CONST 
    0x1d7c: v1d7c(0x20) = CONST 
    0x1d7e: MSTORE v1d7c(0x20), v1d7a(0x9)
    0x1d7f: v1d7f(0x0) = CONST 
    0x1d83: MSTORE v1d7f(0x0), v847
    0x1d84: v1d84(0x40) = CONST 
    0x1d87: v1d87 = SHA3 v1d7f(0x0), v1d84(0x40)
    0x1d88: v1d88 = SLOAD v1d87
    0x1d8a: JUMP v827(0x2b54)

    Begin block 0x2b54
    prev=[0x1d79], succ=[]
    =================================
    0x2b55: v2b55(0x40) = CONST 
    0x2b58: v2b58 = MLOAD v2b55(0x40)
    0x2b5b: MSTORE v2b58, v1d88
    0x2b5c: v2b5c = MLOAD v2b55(0x40)
    0x2b60: v2b60(0x0) = SUB v2b58, v2b5c
    0x2b61: v2b61(0x20) = CONST 
    0x2b63: v2b63(0x20) = ADD v2b61(0x20), v2b60(0x0)
    0x2b65: RETURN v2b5c, v2b63(0x20)

}

function fee(uint8)() public {
    Begin block 0x84c
    prev=[], succ=[0x854, 0x858]
    =================================
    0x84d: v84d = CALLVALUE 
    0x84f: v84f = ISZERO v84d
    0x850: v850(0x858) = CONST 
    0x853: JUMPI v850(0x858), v84f

    Begin block 0x854
    prev=[0x84c], succ=[]
    =================================
    0x854: v854(0x0) = CONST 
    0x857: REVERT v854(0x0), v854(0x0)

    Begin block 0x858
    prev=[0x84c], succ=[0x86b, 0x86f]
    =================================
    0x85a: v85a(0x2b85) = CONST 
    0x85d: v85d(0x4) = CONST 
    0x860: v860 = CALLDATASIZE 
    0x861: v861 = SUB v860, v85d(0x4)
    0x862: v862(0x20) = CONST 
    0x865: v865 = LT v861, v862(0x20)
    0x866: v866 = ISZERO v865
    0x867: v867(0x86f) = CONST 
    0x86a: JUMPI v867(0x86f), v866

    Begin block 0x86b
    prev=[0x858], succ=[]
    =================================
    0x86b: v86b(0x0) = CONST 
    0x86e: REVERT v86b(0x0), v86b(0x0)

    Begin block 0x86f
    prev=[0x858], succ=[0x1d8b]
    =================================
    0x871: v871 = CALLDATALOAD v85d(0x4)
    0x872: v872(0xff) = CONST 
    0x874: v874 = AND v872(0xff), v871
    0x875: v875(0x1d8b) = CONST 
    0x878: JUMP v875(0x1d8b)

    Begin block 0x1d8b
    prev=[0x86f], succ=[0x2b85]
    =================================
    0x1d8c: v1d8c(0x8) = CONST 
    0x1d8e: v1d8e(0x20) = CONST 
    0x1d90: MSTORE v1d8e(0x20), v1d8c(0x8)
    0x1d91: v1d91(0x0) = CONST 
    0x1d95: MSTORE v1d91(0x0), v874
    0x1d96: v1d96(0x40) = CONST 
    0x1d99: v1d99 = SHA3 v1d91(0x0), v1d96(0x40)
    0x1d9a: v1d9a = SLOAD v1d99
    0x1d9c: JUMP v85a(0x2b85)

    Begin block 0x2b85
    prev=[0x1d8b], succ=[]
    =================================
    0x2b86: v2b86(0x40) = CONST 
    0x2b89: v2b89 = MLOAD v2b86(0x40)
    0x2b8c: MSTORE v2b89, v1d9a
    0x2b8d: v2b8d = MLOAD v2b86(0x40)
    0x2b91: v2b91(0x0) = SUB v2b89, v2b8d
    0x2b92: v2b92(0x20) = CONST 
    0x2b94: v2b94(0x20) = ADD v2b92(0x20), v2b91(0x0)
    0x2b96: RETURN v2b8d, v2b94(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x879
    prev=[], succ=[0x881, 0x885]
    =================================
    0x87a: v87a = CALLVALUE 
    0x87c: v87c = ISZERO v87a
    0x87d: v87d(0x885) = CONST 
    0x880: JUMPI v87d(0x885), v87c

    Begin block 0x881
    prev=[0x879], succ=[]
    =================================
    0x881: v881(0x0) = CONST 
    0x884: REVERT v881(0x0), v881(0x0)

    Begin block 0x885
    prev=[0x879], succ=[0x898, 0x89c]
    =================================
    0x887: v887(0x2bb6) = CONST 
    0x88a: v88a(0x4) = CONST 
    0x88d: v88d = CALLDATASIZE 
    0x88e: v88e = SUB v88d, v88a(0x4)
    0x88f: v88f(0x20) = CONST 
    0x892: v892 = LT v88e, v88f(0x20)
    0x893: v893 = ISZERO v892
    0x894: v894(0x89c) = CONST 
    0x897: JUMPI v894(0x89c), v893

    Begin block 0x898
    prev=[0x885], succ=[]
    =================================
    0x898: v898(0x0) = CONST 
    0x89b: REVERT v898(0x0), v898(0x0)

    Begin block 0x89c
    prev=[0x885], succ=[0x1d9d]
    =================================
    0x89e: v89e = CALLDATALOAD v88a(0x4)
    0x89f: v89f(0x1) = CONST 
    0x8a1: v8a1(0x1) = CONST 
    0x8a3: v8a3(0xa0) = CONST 
    0x8a5: v8a5(0x10000000000000000000000000000000000000000) = SHL v8a3(0xa0), v8a1(0x1)
    0x8a6: v8a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8a5(0x10000000000000000000000000000000000000000), v89f(0x1)
    0x8a7: v8a7 = AND v8a6(0xffffffffffffffffffffffffffffffffffffffff), v89e
    0x8a8: v8a8(0x1d9d) = CONST 
    0x8ab: JUMP v8a8(0x1d9d)

    Begin block 0x1d9d
    prev=[0x89c], succ=[0x227eB0x1d9d]
    =================================
    0x1d9e: v1d9e(0x1da5) = CONST 
    0x1da1: v1da1(0x227e) = CONST 
    0x1da4: JUMP v1da1(0x227e)

    Begin block 0x227eB0x1d9d
    prev=[0x1d9d], succ=[0x1da5]
    =================================
    0x227fS0x1d9d: v227fV1d9d = CALLER 
    0x2281S0x1d9d: JUMP v1d9e(0x1da5)

    Begin block 0x1da5
    prev=[0x227eB0x1d9d], succ=[0x16ffB0x1da5]
    =================================
    0x1da6: v1da6(0x1) = CONST 
    0x1da8: v1da8(0x1) = CONST 
    0x1daa: v1daa(0xa0) = CONST 
    0x1dac: v1dac(0x10000000000000000000000000000000000000000) = SHL v1daa(0xa0), v1da8(0x1)
    0x1dad: v1dad(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1dac(0x10000000000000000000000000000000000000000), v1da6(0x1)
    0x1dae: v1dae = AND v1dad(0xffffffffffffffffffffffffffffffffffffffff), v227fV1d9d
    0x1daf: v1daf(0x1db6) = CONST 
    0x1db2: v1db2(0x16ff) = CONST 
    0x1db5: JUMP v1db2(0x16ff)

    Begin block 0x16ffB0x1da5
    prev=[0x1da5], succ=[0x1db6]
    =================================
    0x1700S0x1da5: v1700V1da5(0x0) = CONST 
    0x1702S0x1da5: v1702V1da5 = SLOAD v1700V1da5(0x0)
    0x1703S0x1da5: v1703V1da5(0x1) = CONST 
    0x1705S0x1da5: v1705V1da5(0x1) = CONST 
    0x1707S0x1da5: v1707V1da5(0xa0) = CONST 
    0x1709S0x1da5: v1709V1da5(0x10000000000000000000000000000000000000000) = SHL v1707V1da5(0xa0), v1705V1da5(0x1)
    0x170aS0x1da5: v170aV1da5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1da5(0x10000000000000000000000000000000000000000), v1703V1da5(0x1)
    0x170bS0x1da5: v170bV1da5 = AND v170aV1da5(0xffffffffffffffffffffffffffffffffffffffff), v1702V1da5
    0x170dS0x1da5: JUMP v1daf(0x1db6)

    Begin block 0x1db6
    prev=[0x16ffB0x1da5], succ=[0x1dc5, 0x1dff]
    =================================
    0x1db7: v1db7(0x1) = CONST 
    0x1db9: v1db9(0x1) = CONST 
    0x1dbb: v1dbb(0xa0) = CONST 
    0x1dbd: v1dbd(0x10000000000000000000000000000000000000000) = SHL v1dbb(0xa0), v1db9(0x1)
    0x1dbe: v1dbe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1dbd(0x10000000000000000000000000000000000000000), v1db7(0x1)
    0x1dbf: v1dbf = AND v1dbe(0xffffffffffffffffffffffffffffffffffffffff), v170bV1da5
    0x1dc0: v1dc0 = EQ v1dbf, v1dae
    0x1dc1: v1dc1(0x1dff) = CONST 
    0x1dc4: JUMPI v1dc1(0x1dff), v1dc0

    Begin block 0x1dc5
    prev=[0x1db6], succ=[]
    =================================
    0x1dc5: v1dc5(0x40) = CONST 
    0x1dc8: v1dc8 = MLOAD v1dc5(0x40)
    0x1dc9: v1dc9(0x461bcd) = CONST 
    0x1dcd: v1dcd(0xe5) = CONST 
    0x1dcf: v1dcf(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1dcd(0xe5), v1dc9(0x461bcd)
    0x1dd1: MSTORE v1dc8, v1dcf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1dd2: v1dd2(0x20) = CONST 
    0x1dd4: v1dd4(0x4) = CONST 
    0x1dd7: v1dd7 = ADD v1dc8, v1dd4(0x4)
    0x1dda: MSTORE v1dd7, v1dd2(0x20)
    0x1ddb: v1ddb(0x24) = CONST 
    0x1dde: v1dde = ADD v1dc8, v1ddb(0x24)
    0x1ddf: MSTORE v1dde, v1dd2(0x20)
    0x1de0: v1de0(0x0) = CONST 
    0x1de3: v1de3 = MLOAD v1de0(0x0)
    0x1de4: v1de4(0x20) = CONST 
    0x1de6: v1de6(0x255c) = CONST 
    0x1dee: MSTORE v1de0(0x0), v1de3
    0x1def: v1def(0x44) = CONST 
    0x1df2: v1df2 = ADD v1dc8, v1def(0x44)
    0x1df3: MSTORE v1df2, v2e56(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1df5: v1df5 = MLOAD v1dc5(0x40)
    0x1df9: v1df9(0x0) = SUB v1dc8, v1df5
    0x1dfa: v1dfa(0x64) = CONST 
    0x1dfc: v1dfc(0x64) = ADD v1dfa(0x64), v1df9(0x0)
    0x1dfe: REVERT v1df5, v1dfc(0x64)
    0x2e56: v2e56(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1dff
    prev=[0x1db6], succ=[0x1e0e, 0x1e44]
    =================================
    0x1e00: v1e00(0x1) = CONST 
    0x1e02: v1e02(0x1) = CONST 
    0x1e04: v1e04(0xa0) = CONST 
    0x1e06: v1e06(0x10000000000000000000000000000000000000000) = SHL v1e04(0xa0), v1e02(0x1)
    0x1e07: v1e07(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e06(0x10000000000000000000000000000000000000000), v1e00(0x1)
    0x1e09: v1e09 = AND v8a7, v1e07(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e0a: v1e0a(0x1e44) = CONST 
    0x1e0d: JUMPI v1e0a(0x1e44), v1e09

    Begin block 0x1e0e
    prev=[0x1dff], succ=[]
    =================================
    0x1e0e: v1e0e(0x40) = CONST 
    0x1e10: v1e10 = MLOAD v1e0e(0x40)
    0x1e11: v1e11(0x461bcd) = CONST 
    0x1e15: v1e15(0xe5) = CONST 
    0x1e17: v1e17(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e15(0xe5), v1e11(0x461bcd)
    0x1e19: MSTORE v1e10, v1e17(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e1a: v1e1a(0x4) = CONST 
    0x1e1c: v1e1c = ADD v1e1a(0x4), v1e10
    0x1e1f: v1e1f(0x20) = CONST 
    0x1e21: v1e21 = ADD v1e1f(0x20), v1e1c
    0x1e24: v1e24(0x20) = SUB v1e21, v1e1c
    0x1e26: MSTORE v1e1c, v1e24(0x20)
    0x1e27: v1e27(0x26) = CONST 
    0x1e2a: MSTORE v1e21, v1e27(0x26)
    0x1e2b: v1e2b(0x20) = CONST 
    0x1e2d: v1e2d = ADD v1e2b(0x20), v1e21
    0x1e2f: v1e2f(0x24c5) = CONST 
    0x1e32: v1e32(0x26) = CONST 
    0x1e35: CODECOPY v1e2d, v1e2f(0x24c5), v1e32(0x26)
    0x1e36: v1e36(0x40) = CONST 
    0x1e38: v1e38 = ADD v1e36(0x40), v1e2d
    0x1e3c: v1e3c(0x40) = CONST 
    0x1e3e: v1e3e = MLOAD v1e3c(0x40)
    0x1e41: v1e41(0x84) = SUB v1e38, v1e3e
    0x1e43: REVERT v1e3e, v1e41(0x84)

    Begin block 0x1e44
    prev=[0x1dff], succ=[0x2bb6]
    =================================
    0x1e45: v1e45(0x0) = CONST 
    0x1e48: v1e48 = SLOAD v1e45(0x0)
    0x1e49: v1e49(0x40) = CONST 
    0x1e4b: v1e4b = MLOAD v1e49(0x40)
    0x1e4c: v1e4c(0x1) = CONST 
    0x1e4e: v1e4e(0x1) = CONST 
    0x1e50: v1e50(0xa0) = CONST 
    0x1e52: v1e52(0x10000000000000000000000000000000000000000) = SHL v1e50(0xa0), v1e4e(0x1)
    0x1e53: v1e53(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e52(0x10000000000000000000000000000000000000000), v1e4c(0x1)
    0x1e56: v1e56 = AND v8a7, v1e53(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e59: v1e59 = AND v1e48, v1e53(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e5b: v1e5b(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1e7d: LOG3 v1e4b, v1e45(0x0), v1e5b(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1e59, v1e56
    0x1e7e: v1e7e(0x0) = CONST 
    0x1e81: v1e81 = SLOAD v1e7e(0x0)
    0x1e82: v1e82(0x1) = CONST 
    0x1e84: v1e84(0x1) = CONST 
    0x1e86: v1e86(0xa0) = CONST 
    0x1e88: v1e88(0x10000000000000000000000000000000000000000) = SHL v1e86(0xa0), v1e84(0x1)
    0x1e89: v1e89(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e88(0x10000000000000000000000000000000000000000), v1e82(0x1)
    0x1e8a: v1e8a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1e89(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e8b: v1e8b = AND v1e8a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1e81
    0x1e8c: v1e8c(0x1) = CONST 
    0x1e8e: v1e8e(0x1) = CONST 
    0x1e90: v1e90(0xa0) = CONST 
    0x1e92: v1e92(0x10000000000000000000000000000000000000000) = SHL v1e90(0xa0), v1e8e(0x1)
    0x1e93: v1e93(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e92(0x10000000000000000000000000000000000000000), v1e8c(0x1)
    0x1e97: v1e97 = AND v1e93(0xffffffffffffffffffffffffffffffffffffffff), v8a7
    0x1e9b: v1e9b = OR v1e97, v1e8b
    0x1e9d: SSTORE v1e7e(0x0), v1e9b
    0x1e9e: JUMP v887(0x2bb6)

    Begin block 0x2bb6
    prev=[0x1e44], succ=[]
    =================================
    0x2bb7: STOP 

}

function transferToken(address,uint256,address)() public {
    Begin block 0x8ac
    prev=[], succ=[0x8b4, 0x8b8]
    =================================
    0x8ad: v8ad = CALLVALUE 
    0x8af: v8af = ISZERO v8ad
    0x8b0: v8b0(0x8b8) = CONST 
    0x8b3: JUMPI v8b0(0x8b8), v8af

    Begin block 0x8b4
    prev=[0x8ac], succ=[]
    =================================
    0x8b4: v8b4(0x0) = CONST 
    0x8b7: REVERT v8b4(0x0), v8b4(0x0)

    Begin block 0x8b8
    prev=[0x8ac], succ=[0x8cb, 0x8cf]
    =================================
    0x8ba: v8ba(0x2bd7) = CONST 
    0x8bd: v8bd(0x4) = CONST 
    0x8c0: v8c0 = CALLDATASIZE 
    0x8c1: v8c1 = SUB v8c0, v8bd(0x4)
    0x8c2: v8c2(0x60) = CONST 
    0x8c5: v8c5 = LT v8c1, v8c2(0x60)
    0x8c6: v8c6 = ISZERO v8c5
    0x8c7: v8c7(0x8cf) = CONST 
    0x8ca: JUMPI v8c7(0x8cf), v8c6

    Begin block 0x8cb
    prev=[0x8b8], succ=[]
    =================================
    0x8cb: v8cb(0x0) = CONST 
    0x8ce: REVERT v8cb(0x0), v8cb(0x0)

    Begin block 0x8cf
    prev=[0x8b8], succ=[0x1e9f]
    =================================
    0x8d1: v8d1(0x1) = CONST 
    0x8d3: v8d3(0x1) = CONST 
    0x8d5: v8d5(0xa0) = CONST 
    0x8d7: v8d7(0x10000000000000000000000000000000000000000) = SHL v8d5(0xa0), v8d3(0x1)
    0x8d8: v8d8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8d7(0x10000000000000000000000000000000000000000), v8d1(0x1)
    0x8da: v8da = CALLDATALOAD v8bd(0x4)
    0x8dc: v8dc = AND v8d8(0xffffffffffffffffffffffffffffffffffffffff), v8da
    0x8de: v8de(0x20) = CONST 
    0x8e1: v8e1(0x24) = ADD v8bd(0x4), v8de(0x20)
    0x8e2: v8e2 = CALLDATALOAD v8e1(0x24)
    0x8e4: v8e4(0x40) = CONST 
    0x8e8: v8e8(0x44) = ADD v8bd(0x4), v8e4(0x40)
    0x8e9: v8e9 = CALLDATALOAD v8e8(0x44)
    0x8ea: v8ea = AND v8e9, v8d8(0xffffffffffffffffffffffffffffffffffffffff)
    0x8eb: v8eb(0x1e9f) = CONST 
    0x8ee: JUMP v8eb(0x1e9f)

    Begin block 0x1e9f
    prev=[0x8cf], succ=[0x1eb2, 0x1ef8]
    =================================
    0x1ea0: v1ea0(0x1) = CONST 
    0x1ea2: v1ea2 = SLOAD v1ea0(0x1)
    0x1ea3: v1ea3(0x1) = CONST 
    0x1ea5: v1ea5(0x1) = CONST 
    0x1ea7: v1ea7(0xa0) = CONST 
    0x1ea9: v1ea9(0x10000000000000000000000000000000000000000) = SHL v1ea7(0xa0), v1ea5(0x1)
    0x1eaa: v1eaa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ea9(0x10000000000000000000000000000000000000000), v1ea3(0x1)
    0x1eab: v1eab = AND v1eaa(0xffffffffffffffffffffffffffffffffffffffff), v1ea2
    0x1eac: v1eac = CALLER 
    0x1ead: v1ead = EQ v1eac, v1eab
    0x1eae: v1eae(0x1ef8) = CONST 
    0x1eb1: JUMPI v1eae(0x1ef8), v1ead

    Begin block 0x1eb2
    prev=[0x1e9f], succ=[]
    =================================
    0x1eb2: v1eb2(0x40) = CONST 
    0x1eb5: v1eb5 = MLOAD v1eb2(0x40)
    0x1eb6: v1eb6(0x461bcd) = CONST 
    0x1eba: v1eba(0xe5) = CONST 
    0x1ebc: v1ebc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1eba(0xe5), v1eb6(0x461bcd)
    0x1ebe: MSTORE v1eb5, v1ebc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ebf: v1ebf(0x20) = CONST 
    0x1ec1: v1ec1(0x4) = CONST 
    0x1ec4: v1ec4 = ADD v1eb5, v1ec1(0x4)
    0x1ec5: MSTORE v1ec4, v1ebf(0x20)
    0x1ec6: v1ec6(0x17) = CONST 
    0x1ec8: v1ec8(0x24) = CONST 
    0x1ecb: v1ecb = ADD v1eb5, v1ec8(0x24)
    0x1ecc: MSTORE v1ecb, v1ec6(0x17)
    0x1ecd: v1ecd(0x21b0b63632b91034b9903737ba103a34329030b236b4b7) = CONST 
    0x1ee5: v1ee5(0x49) = CONST 
    0x1ee7: v1ee7(0x43616c6c6572206973206e6f74207468652061646d696e000000000000000000) = SHL v1ee5(0x49), v1ecd(0x21b0b63632b91034b9903737ba103a34329030b236b4b7)
    0x1ee8: v1ee8(0x44) = CONST 
    0x1eeb: v1eeb = ADD v1eb5, v1ee8(0x44)
    0x1eec: MSTORE v1eeb, v1ee7(0x43616c6c6572206973206e6f74207468652061646d696e000000000000000000)
    0x1eee: v1eee = MLOAD v1eb2(0x40)
    0x1ef2: v1ef2(0x0) = SUB v1eb5, v1eee
    0x1ef3: v1ef3(0x64) = CONST 
    0x1ef5: v1ef5(0x64) = ADD v1ef3(0x64), v1ef2(0x0)
    0x1ef7: REVERT v1eee, v1ef5(0x64)

    Begin block 0x1ef8
    prev=[0x1e9f], succ=[0x1f4b, 0x1f4f]
    =================================
    0x1efa: v1efa(0x1) = CONST 
    0x1efc: v1efc(0x1) = CONST 
    0x1efe: v1efe(0xa0) = CONST 
    0x1f00: v1f00(0x10000000000000000000000000000000000000000) = SHL v1efe(0xa0), v1efc(0x1)
    0x1f01: v1f01(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f00(0x10000000000000000000000000000000000000000), v1efa(0x1)
    0x1f02: v1f02 = AND v1f01(0xffffffffffffffffffffffffffffffffffffffff), v8dc
    0x1f03: v1f03(0xa9059cbb) = CONST 
    0x1f0a: v1f0a(0x40) = CONST 
    0x1f0c: v1f0c = MLOAD v1f0a(0x40)
    0x1f0e: v1f0e(0xffffffff) = CONST 
    0x1f13: v1f13(0xa9059cbb) = AND v1f0e(0xffffffff), v1f03(0xa9059cbb)
    0x1f14: v1f14(0xe0) = CONST 
    0x1f16: v1f16(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL v1f14(0xe0), v1f13(0xa9059cbb)
    0x1f18: MSTORE v1f0c, v1f16(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x1f19: v1f19(0x4) = CONST 
    0x1f1b: v1f1b = ADD v1f19(0x4), v1f0c
    0x1f1e: v1f1e(0x1) = CONST 
    0x1f20: v1f20(0x1) = CONST 
    0x1f22: v1f22(0xa0) = CONST 
    0x1f24: v1f24(0x10000000000000000000000000000000000000000) = SHL v1f22(0xa0), v1f20(0x1)
    0x1f25: v1f25(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f24(0x10000000000000000000000000000000000000000), v1f1e(0x1)
    0x1f26: v1f26 = AND v1f25(0xffffffffffffffffffffffffffffffffffffffff), v8ea
    0x1f28: MSTORE v1f1b, v1f26
    0x1f29: v1f29(0x20) = CONST 
    0x1f2b: v1f2b = ADD v1f29(0x20), v1f1b
    0x1f2e: MSTORE v1f2b, v8e2
    0x1f2f: v1f2f(0x20) = CONST 
    0x1f31: v1f31 = ADD v1f2f(0x20), v1f2b
    0x1f36: v1f36(0x20) = CONST 
    0x1f38: v1f38(0x40) = CONST 
    0x1f3a: v1f3a = MLOAD v1f38(0x40)
    0x1f3d: v1f3d(0x44) = SUB v1f31, v1f3a
    0x1f3f: v1f3f(0x0) = CONST 
    0x1f43: v1f43 = EXTCODESIZE v1f02
    0x1f44: v1f44 = ISZERO v1f43
    0x1f46: v1f46 = ISZERO v1f44
    0x1f47: v1f47(0x1f4f) = CONST 
    0x1f4a: JUMPI v1f47(0x1f4f), v1f46

    Begin block 0x1f4b
    prev=[0x1ef8], succ=[]
    =================================
    0x1f4b: v1f4b(0x0) = CONST 
    0x1f4e: REVERT v1f4b(0x0), v1f4b(0x0)

    Begin block 0x1f4f
    prev=[0x1ef8], succ=[0x1f5a, 0x1f63]
    =================================
    0x1f51: v1f51 = GAS 
    0x1f52: v1f52 = CALL v1f51, v1f02, v1f3f(0x0), v1f3a, v1f3d(0x44), v1f3a, v1f36(0x20)
    0x1f53: v1f53 = ISZERO v1f52
    0x1f55: v1f55 = ISZERO v1f53
    0x1f56: v1f56(0x1f63) = CONST 
    0x1f59: JUMPI v1f56(0x1f63), v1f55

    Begin block 0x1f5a
    prev=[0x1f4f], succ=[]
    =================================
    0x1f5a: v1f5a = RETURNDATASIZE 
    0x1f5b: v1f5b(0x0) = CONST 
    0x1f5e: RETURNDATACOPY v1f5b(0x0), v1f5b(0x0), v1f5a
    0x1f5f: v1f5f = RETURNDATASIZE 
    0x1f60: v1f60(0x0) = CONST 
    0x1f62: REVERT v1f60(0x0), v1f5f

    Begin block 0x1f63
    prev=[0x1f4f], succ=[0x1f75, 0x1f79]
    =================================
    0x1f68: v1f68(0x40) = CONST 
    0x1f6a: v1f6a = MLOAD v1f68(0x40)
    0x1f6b: v1f6b = RETURNDATASIZE 
    0x1f6c: v1f6c(0x20) = CONST 
    0x1f6f: v1f6f = LT v1f6b, v1f6c(0x20)
    0x1f70: v1f70 = ISZERO v1f6f
    0x1f71: v1f71(0x1f79) = CONST 
    0x1f74: JUMPI v1f71(0x1f79), v1f70

    Begin block 0x1f75
    prev=[0x1f63], succ=[]
    =================================
    0x1f75: v1f75(0x0) = CONST 
    0x1f78: REVERT v1f75(0x0), v1f75(0x0)

    Begin block 0x1f79
    prev=[0x1f63], succ=[0x2bd7]
    =================================
    0x1f7f: JUMP v8ba(0x2bd7)

    Begin block 0x2bd7
    prev=[0x1f79], succ=[]
    =================================
    0x2bd8: STOP 

}

function admin()() public {
    Begin block 0x8ef
    prev=[], succ=[0x8f7, 0x8fb]
    =================================
    0x8f0: v8f0 = CALLVALUE 
    0x8f2: v8f2 = ISZERO v8f0
    0x8f3: v8f3(0x8fb) = CONST 
    0x8f6: JUMPI v8f3(0x8fb), v8f2

    Begin block 0x8f7
    prev=[0x8ef], succ=[]
    =================================
    0x8f7: v8f7(0x0) = CONST 
    0x8fa: REVERT v8f7(0x0), v8f7(0x0)

    Begin block 0x8fb
    prev=[0x8ef], succ=[0x1f80]
    =================================
    0x8fd: v8fd(0x2bf8) = CONST 
    0x900: v900(0x1f80) = CONST 
    0x903: JUMP v900(0x1f80)

    Begin block 0x1f80
    prev=[0x8fb], succ=[0x2bf8]
    =================================
    0x1f81: v1f81(0x1) = CONST 
    0x1f83: v1f83 = SLOAD v1f81(0x1)
    0x1f84: v1f84(0x1) = CONST 
    0x1f86: v1f86(0x1) = CONST 
    0x1f88: v1f88(0xa0) = CONST 
    0x1f8a: v1f8a(0x10000000000000000000000000000000000000000) = SHL v1f88(0xa0), v1f86(0x1)
    0x1f8b: v1f8b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f8a(0x10000000000000000000000000000000000000000), v1f84(0x1)
    0x1f8c: v1f8c = AND v1f8b(0xffffffffffffffffffffffffffffffffffffffff), v1f83
    0x1f8e: JUMP v8fd(0x2bf8)

    Begin block 0x2bf8
    prev=[0x1f80], succ=[]
    =================================
    0x2bf9: v2bf9(0x40) = CONST 
    0x2bfc: v2bfc = MLOAD v2bf9(0x40)
    0x2bfd: v2bfd(0x1) = CONST 
    0x2bff: v2bff(0x1) = CONST 
    0x2c01: v2c01(0xa0) = CONST 
    0x2c03: v2c03(0x10000000000000000000000000000000000000000) = SHL v2c01(0xa0), v2bff(0x1)
    0x2c04: v2c04(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c03(0x10000000000000000000000000000000000000000), v2bfd(0x1)
    0x2c07: v2c07 = AND v1f8c, v2c04(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c09: MSTORE v2bfc, v2c07
    0x2c0a: v2c0a = MLOAD v2bf9(0x40)
    0x2c0e: v2c0e(0x0) = SUB v2bfc, v2c0a
    0x2c0f: v2c0f(0x20) = CONST 
    0x2c11: v2c11(0x20) = ADD v2c0f(0x20), v2c0e(0x0)
    0x2c13: RETURN v2c0a, v2c11(0x20)

}

function setMaxAmount(address,uint256)() public {
    Begin block 0x904
    prev=[], succ=[0x90c, 0x910]
    =================================
    0x905: v905 = CALLVALUE 
    0x907: v907 = ISZERO v905
    0x908: v908(0x910) = CONST 
    0x90b: JUMPI v908(0x910), v907

    Begin block 0x90c
    prev=[0x904], succ=[]
    =================================
    0x90c: v90c(0x0) = CONST 
    0x90f: REVERT v90c(0x0), v90c(0x0)

    Begin block 0x910
    prev=[0x904], succ=[0x923, 0x927]
    =================================
    0x912: v912(0x2c33) = CONST 
    0x915: v915(0x4) = CONST 
    0x918: v918 = CALLDATASIZE 
    0x919: v919 = SUB v918, v915(0x4)
    0x91a: v91a(0x40) = CONST 
    0x91d: v91d = LT v919, v91a(0x40)
    0x91e: v91e = ISZERO v91d
    0x91f: v91f(0x927) = CONST 
    0x922: JUMPI v91f(0x927), v91e

    Begin block 0x923
    prev=[0x910], succ=[]
    =================================
    0x923: v923(0x0) = CONST 
    0x926: REVERT v923(0x0), v923(0x0)

    Begin block 0x927
    prev=[0x910], succ=[0x1f8f]
    =================================
    0x929: v929(0x1) = CONST 
    0x92b: v92b(0x1) = CONST 
    0x92d: v92d(0xa0) = CONST 
    0x92f: v92f(0x10000000000000000000000000000000000000000) = SHL v92d(0xa0), v92b(0x1)
    0x930: v930(0xffffffffffffffffffffffffffffffffffffffff) = SUB v92f(0x10000000000000000000000000000000000000000), v929(0x1)
    0x932: v932 = CALLDATALOAD v915(0x4)
    0x933: v933 = AND v932, v930(0xffffffffffffffffffffffffffffffffffffffff)
    0x935: v935(0x20) = CONST 
    0x937: v937(0x24) = ADD v935(0x20), v915(0x4)
    0x938: v938 = CALLDATALOAD v937(0x24)
    0x939: v939(0x1f8f) = CONST 
    0x93c: JUMP v939(0x1f8f)

    Begin block 0x1f8f
    prev=[0x927], succ=[0x227eB0x1f8f]
    =================================
    0x1f90: v1f90(0x1f97) = CONST 
    0x1f93: v1f93(0x227e) = CONST 
    0x1f96: JUMP v1f93(0x227e)

    Begin block 0x227eB0x1f8f
    prev=[0x1f8f], succ=[0x1f97]
    =================================
    0x227fS0x1f8f: v227fV1f8f = CALLER 
    0x2281S0x1f8f: JUMP v1f90(0x1f97)

    Begin block 0x1f97
    prev=[0x227eB0x1f8f], succ=[0x16ffB0x1f97]
    =================================
    0x1f98: v1f98(0x1) = CONST 
    0x1f9a: v1f9a(0x1) = CONST 
    0x1f9c: v1f9c(0xa0) = CONST 
    0x1f9e: v1f9e(0x10000000000000000000000000000000000000000) = SHL v1f9c(0xa0), v1f9a(0x1)
    0x1f9f: v1f9f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f9e(0x10000000000000000000000000000000000000000), v1f98(0x1)
    0x1fa0: v1fa0 = AND v1f9f(0xffffffffffffffffffffffffffffffffffffffff), v227fV1f8f
    0x1fa1: v1fa1(0x1fa8) = CONST 
    0x1fa4: v1fa4(0x16ff) = CONST 
    0x1fa7: JUMP v1fa4(0x16ff)

    Begin block 0x16ffB0x1f97
    prev=[0x1f97], succ=[0x1fa8]
    =================================
    0x1700S0x1f97: v1700V1f97(0x0) = CONST 
    0x1702S0x1f97: v1702V1f97 = SLOAD v1700V1f97(0x0)
    0x1703S0x1f97: v1703V1f97(0x1) = CONST 
    0x1705S0x1f97: v1705V1f97(0x1) = CONST 
    0x1707S0x1f97: v1707V1f97(0xa0) = CONST 
    0x1709S0x1f97: v1709V1f97(0x10000000000000000000000000000000000000000) = SHL v1707V1f97(0xa0), v1705V1f97(0x1)
    0x170aS0x1f97: v170aV1f97(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1709V1f97(0x10000000000000000000000000000000000000000), v1703V1f97(0x1)
    0x170bS0x1f97: v170bV1f97 = AND v170aV1f97(0xffffffffffffffffffffffffffffffffffffffff), v1702V1f97
    0x170dS0x1f97: JUMP v1fa1(0x1fa8)

    Begin block 0x1fa8
    prev=[0x16ffB0x1f97], succ=[0x1fb7, 0x1ff1]
    =================================
    0x1fa9: v1fa9(0x1) = CONST 
    0x1fab: v1fab(0x1) = CONST 
    0x1fad: v1fad(0xa0) = CONST 
    0x1faf: v1faf(0x10000000000000000000000000000000000000000) = SHL v1fad(0xa0), v1fab(0x1)
    0x1fb0: v1fb0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1faf(0x10000000000000000000000000000000000000000), v1fa9(0x1)
    0x1fb1: v1fb1 = AND v1fb0(0xffffffffffffffffffffffffffffffffffffffff), v170bV1f97
    0x1fb2: v1fb2 = EQ v1fb1, v1fa0
    0x1fb3: v1fb3(0x1ff1) = CONST 
    0x1fb6: JUMPI v1fb3(0x1ff1), v1fb2

    Begin block 0x1fb7
    prev=[0x1fa8], succ=[]
    =================================
    0x1fb7: v1fb7(0x40) = CONST 
    0x1fba: v1fba = MLOAD v1fb7(0x40)
    0x1fbb: v1fbb(0x461bcd) = CONST 
    0x1fbf: v1fbf(0xe5) = CONST 
    0x1fc1: v1fc1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1fbf(0xe5), v1fbb(0x461bcd)
    0x1fc3: MSTORE v1fba, v1fc1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1fc4: v1fc4(0x20) = CONST 
    0x1fc6: v1fc6(0x4) = CONST 
    0x1fc9: v1fc9 = ADD v1fba, v1fc6(0x4)
    0x1fcc: MSTORE v1fc9, v1fc4(0x20)
    0x1fcd: v1fcd(0x24) = CONST 
    0x1fd0: v1fd0 = ADD v1fba, v1fcd(0x24)
    0x1fd1: MSTORE v1fd0, v1fc4(0x20)
    0x1fd2: v1fd2(0x0) = CONST 
    0x1fd5: v1fd5 = MLOAD v1fd2(0x0)
    0x1fd6: v1fd6(0x20) = CONST 
    0x1fd8: v1fd8(0x255c) = CONST 
    0x1fe0: MSTORE v1fd2(0x0), v1fd5
    0x1fe1: v1fe1(0x44) = CONST 
    0x1fe4: v1fe4 = ADD v1fba, v1fe1(0x44)
    0x1fe5: MSTORE v1fe4, v2e5b(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1fe7: v1fe7 = MLOAD v1fb7(0x40)
    0x1feb: v1feb(0x0) = SUB v1fba, v1fe7
    0x1fec: v1fec(0x64) = CONST 
    0x1fee: v1fee(0x64) = ADD v1fec(0x64), v1feb(0x0)
    0x1ff0: REVERT v1fe7, v1fee(0x64)
    0x2e5b: v2e5b(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x1ff1
    prev=[0x1fa8], succ=[0x2012, 0x204f]
    =================================
    0x1ff2: v1ff2(0x1) = CONST 
    0x1ff4: v1ff4(0x1) = CONST 
    0x1ff6: v1ff6(0xa0) = CONST 
    0x1ff8: v1ff8(0x10000000000000000000000000000000000000000) = SHL v1ff6(0xa0), v1ff4(0x1)
    0x1ff9: v1ff9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ff8(0x10000000000000000000000000000000000000000), v1ff2(0x1)
    0x1ffb: v1ffb = AND v933, v1ff9(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ffc: v1ffc(0x0) = CONST 
    0x2000: MSTORE v1ffc(0x0), v1ffb
    0x2001: v2001(0xb) = CONST 
    0x2003: v2003(0x20) = CONST 
    0x2005: MSTORE v2003(0x20), v2001(0xb)
    0x2006: v2006(0x40) = CONST 
    0x2009: v2009 = SHA3 v1ffc(0x0), v2006(0x40)
    0x200a: v200a = SLOAD v2009
    0x200c: v200c = LT v938, v200a
    0x200d: v200d = ISZERO v200c
    0x200e: v200e(0x204f) = CONST 
    0x2011: JUMPI v200e(0x204f), v200d

    Begin block 0x2012
    prev=[0x1ff1], succ=[]
    =================================
    0x2012: v2012(0x40) = CONST 
    0x2015: v2015 = MLOAD v2012(0x40)
    0x2016: v2016(0x461bcd) = CONST 
    0x201a: v201a(0xe5) = CONST 
    0x201c: v201c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v201a(0xe5), v2016(0x461bcd)
    0x201e: MSTORE v2015, v201c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x201f: v201f(0x20) = CONST 
    0x2021: v2021(0x4) = CONST 
    0x2024: v2024 = ADD v2015, v2021(0x4)
    0x2025: MSTORE v2024, v201f(0x20)
    0x2026: v2026(0xe) = CONST 
    0x2028: v2028(0x24) = CONST 
    0x202b: v202b = ADD v2015, v2028(0x24)
    0x202c: MSTORE v202b, v2026(0xe)
    0x202d: v202d(0x125b9d985b1a5908185b5bdd5b9d) = CONST 
    0x203c: v203c(0x92) = CONST 
    0x203e: v203e(0x496e76616c696420616d6f756e74000000000000000000000000000000000000) = SHL v203c(0x92), v202d(0x125b9d985b1a5908185b5bdd5b9d)
    0x203f: v203f(0x44) = CONST 
    0x2042: v2042 = ADD v2015, v203f(0x44)
    0x2043: MSTORE v2042, v203e(0x496e76616c696420616d6f756e74000000000000000000000000000000000000)
    0x2045: v2045 = MLOAD v2012(0x40)
    0x2049: v2049(0x0) = SUB v2015, v2045
    0x204a: v204a(0x64) = CONST 
    0x204c: v204c(0x64) = ADD v204a(0x64), v2049(0x0)
    0x204e: REVERT v2045, v204c(0x64)

    Begin block 0x204f
    prev=[0x1ff1], succ=[0x2c33]
    =================================
    0x2050: v2050(0x1) = CONST 
    0x2052: v2052(0x1) = CONST 
    0x2054: v2054(0xa0) = CONST 
    0x2056: v2056(0x10000000000000000000000000000000000000000) = SHL v2054(0xa0), v2052(0x1)
    0x2057: v2057(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2056(0x10000000000000000000000000000000000000000), v2050(0x1)
    0x2059: v2059 = AND v933, v2057(0xffffffffffffffffffffffffffffffffffffffff)
    0x205a: v205a(0x0) = CONST 
    0x205e: MSTORE v205a(0x0), v2059
    0x205f: v205f(0xa) = CONST 
    0x2061: v2061(0x20) = CONST 
    0x2065: MSTORE v2061(0x20), v205f(0xa)
    0x2066: v2066(0x40) = CONST 
    0x206b: v206b = SHA3 v205a(0x0), v2066(0x40)
    0x206d: v206d = SLOAD v206b
    0x2071: SSTORE v206b, v938
    0x2073: v2073 = MLOAD v2066(0x40)
    0x2076: MSTORE v2073, v2059
    0x2079: v2079 = ADD v2073, v2061(0x20)
    0x207c: MSTORE v2079, v206d
    0x207f: v207f = ADD v2066(0x40), v2073
    0x2082: MSTORE v207f, v938
    0x2084: v2084 = MLOAD v2066(0x40)
    0x2087: v2087(0x8a95745aa3799b05e213d99e2cda16c6ae464312c36f4417ac69b6863d4747da) = CONST 
    0x20ac: v20ac(0x0) = SUB v2073, v2084
    0x20ad: v20ad(0x60) = CONST 
    0x20af: v20af(0x60) = ADD v20ad(0x60), v20ac(0x0)
    0x20b1: LOG1 v2084, v20af(0x60), v2087(0x8a95745aa3799b05e213d99e2cda16c6ae464312c36f4417ac69b6863d4747da)
    0x20b5: JUMP v912(0x2c33)

    Begin block 0x2c33
    prev=[0x204f], succ=[]
    =================================
    0x2c34: STOP 

}

function confirmRequireNum()() public {
    Begin block 0x93d
    prev=[], succ=[0x945, 0x949]
    =================================
    0x93e: v93e = CALLVALUE 
    0x940: v940 = ISZERO v93e
    0x941: v941(0x949) = CONST 
    0x944: JUMPI v941(0x949), v940

    Begin block 0x945
    prev=[0x93d], succ=[]
    =================================
    0x945: v945(0x0) = CONST 
    0x948: REVERT v945(0x0), v945(0x0)

    Begin block 0x949
    prev=[0x93d], succ=[0x20b6]
    =================================
    0x94b: v94b(0x2c54) = CONST 
    0x94e: v94e(0x20b6) = CONST 
    0x951: JUMP v94e(0x20b6)

    Begin block 0x20b6
    prev=[0x949], succ=[0x2c54]
    =================================
    0x20b7: v20b7(0x7) = CONST 
    0x20b9: v20b9 = SLOAD v20b7(0x7)
    0x20bb: JUMP v94b(0x2c54)

    Begin block 0x2c54
    prev=[0x20b6], succ=[]
    =================================
    0x2c55: v2c55(0x40) = CONST 
    0x2c58: v2c58 = MLOAD v2c55(0x40)
    0x2c5b: MSTORE v2c58, v20b9
    0x2c5c: v2c5c = MLOAD v2c55(0x40)
    0x2c60: v2c60(0x0) = SUB v2c58, v2c5c
    0x2c61: v2c61(0x20) = CONST 
    0x2c63: v2c63(0x20) = ADD v2c61(0x20), v2c60(0x0)
    0x2c65: RETURN v2c5c, v2c63(0x20)

}

