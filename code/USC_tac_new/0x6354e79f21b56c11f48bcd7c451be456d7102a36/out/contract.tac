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
    prev=[0x0], succ=[0x1a, 0x1e9c]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x1e04: v1e04(0x1e9c) = CONST 
    0x1e05: JUMPI v1e04(0x1e9c), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x104, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0xa622ee7c) = CONST 
    0x26: v26 = GT v21(0xa622ee7c), v1f
    0x27: v27(0x104) = CONST 
    0x2a: JUMPI v27(0x104), v26

    Begin block 0x104
    prev=[0x1a], succ=[0x17c, 0x110]
    =================================
    0x106: v106(0x6dcd64e5) = CONST 
    0x10b: v10b = GT v106(0x6dcd64e5), v1f
    0x10c: v10c(0x17c) = CONST 
    0x10f: JUMPI v10c(0x17c), v10b

    Begin block 0x17c
    prev=[0x104], succ=[0x1b8, 0x188]
    =================================
    0x17e: v17e(0x590bbb60) = CONST 
    0x183: v183 = GT v17e(0x590bbb60), v1f
    0x184: v184(0x1b8) = CONST 
    0x187: JUMPI v184(0x1b8), v183

    Begin block 0x1b8
    prev=[0x17c], succ=[0x1e42, 0x1c4]
    =================================
    0x1ba: v1ba(0x197baa6d) = CONST 
    0x1bf: v1bf = EQ v1ba(0x197baa6d), v1f
    0x1e3c: v1e3c(0x1e42) = CONST 
    0x1e3d: JUMPI v1e3c(0x1e42), v1bf

    Begin block 0x1e42
    prev=[0x1b8], succ=[]
    =================================
    0x1e43: v1e43(0x1df) = CONST 
    0x1e44: CALLPRIVATE v1e43(0x1df)

    Begin block 0x1c4
    prev=[0x1b8], succ=[0x1e45, 0x1cf]
    =================================
    0x1c5: v1c5(0x1fe4a686) = CONST 
    0x1ca: v1ca = EQ v1c5(0x1fe4a686), v1f
    0x1e3e: v1e3e(0x1e45) = CONST 
    0x1e3f: JUMPI v1e3e(0x1e45), v1ca

    Begin block 0x1e45
    prev=[0x1c4], succ=[]
    =================================
    0x1e46: v1e46(0x20f) = CONST 
    0x1e47: CALLPRIVATE v1e46(0x20f)

    Begin block 0x1cf
    prev=[0x1c4], succ=[0x1e48, 0x1da]
    =================================
    0x1d0: v1d0(0x39ebf823) = CONST 
    0x1d5: v1d5 = EQ v1d0(0x39ebf823), v1f
    0x1e40: v1e40(0x1e48) = CONST 
    0x1e41: JUMPI v1e40(0x1e48), v1d5

    Begin block 0x1e48
    prev=[0x1cf], succ=[]
    =================================
    0x1e49: v1e49(0x233) = CONST 
    0x1e4a: CALLPRIVATE v1e49(0x233)

    Begin block 0x1da
    prev=[0x1cf], succ=[]
    =================================
    0x1db: v1db(0x0) = CONST 
    0x1de: REVERT v1db(0x0), v1db(0x0)

    Begin block 0x188
    prev=[0x17c], succ=[0x1e4b, 0x193]
    =================================
    0x189: v189(0x590bbb60) = CONST 
    0x18e: v18e = EQ v189(0x590bbb60), v1f
    0x1e34: v1e34(0x1e4b) = CONST 
    0x1e35: JUMPI v1e34(0x1e4b), v18e

    Begin block 0x1e4b
    prev=[0x188], succ=[]
    =================================
    0x1e4c: v1e4c(0x259) = CONST 
    0x1e4d: CALLPRIVATE v1e4c(0x259)

    Begin block 0x193
    prev=[0x188], succ=[0x1e4e, 0x19e]
    =================================
    0x194: v194(0x5aa6e675) = CONST 
    0x199: v199 = EQ v194(0x5aa6e675), v1f
    0x1e36: v1e36(0x1e4e) = CONST 
    0x1e37: JUMPI v1e36(0x1e4e), v199

    Begin block 0x1e4e
    prev=[0x193], succ=[]
    =================================
    0x1e4f: v1e4f(0x287) = CONST 
    0x1e50: CALLPRIVATE v1e4f(0x287)

    Begin block 0x19e
    prev=[0x193], succ=[0x1e51, 0x1a9]
    =================================
    0x19f: v19f(0x674e694f) = CONST 
    0x1a4: v1a4 = EQ v19f(0x674e694f), v1f
    0x1e38: v1e38(0x1e51) = CONST 
    0x1e39: JUMPI v1e38(0x1e51), v1a4

    Begin block 0x1e51
    prev=[0x19e], succ=[]
    =================================
    0x1e52: v1e52(0x28f) = CONST 
    0x1e53: CALLPRIVATE v1e52(0x28f)

    Begin block 0x1a9
    prev=[0x19e], succ=[0x1b4, 0x1e54]
    =================================
    0x1aa: v1aa(0x6ac5db19) = CONST 
    0x1af: v1af = EQ v1aa(0x6ac5db19), v1f
    0x1e3a: v1e3a(0x1e54) = CONST 
    0x1e3b: JUMPI v1e3a(0x1e54), v1af

    Begin block 0x1b4
    prev=[0x1a9], succ=[0x1812]
    =================================
    0x1b4: v1b4(0x1812) = CONST 
    0x1b7: JUMP v1b4(0x1812)

    Begin block 0x1812
    prev=[0x1b4], succ=[]
    =================================
    0x1813: v1813(0x0) = CONST 
    0x1816: REVERT v1813(0x0), v1813(0x0)

    Begin block 0x1e54
    prev=[0x1a9], succ=[]
    =================================
    0x1e55: v1e55(0x2ac) = CONST 
    0x1e56: CALLPRIVATE v1e55(0x2ac)

    Begin block 0x110
    prev=[0x104], succ=[0x14b, 0x11b]
    =================================
    0x111: v111(0x748747e6) = CONST 
    0x116: v116 = GT v111(0x748747e6), v1f
    0x117: v117(0x14b) = CONST 
    0x11a: JUMPI v117(0x14b), v116

    Begin block 0x14b
    prev=[0x110], succ=[0x1e57, 0x157]
    =================================
    0x14d: v14d(0x6dcd64e5) = CONST 
    0x152: v152 = EQ v14d(0x6dcd64e5), v1f
    0x1e2c: v1e2c(0x1e57) = CONST 
    0x1e2d: JUMPI v1e2c(0x1e57), v152

    Begin block 0x1e57
    prev=[0x14b], succ=[]
    =================================
    0x1e58: v1e58(0x2c6) = CONST 
    0x1e59: CALLPRIVATE v1e58(0x2c6)

    Begin block 0x157
    prev=[0x14b], succ=[0x1e5a, 0x162]
    =================================
    0x158: v158(0x70a08231) = CONST 
    0x15d: v15d = EQ v158(0x70a08231), v1f
    0x1e2e: v1e2e(0x1e5a) = CONST 
    0x1e2f: JUMPI v1e2e(0x1e5a), v15d

    Begin block 0x1e5a
    prev=[0x157], succ=[]
    =================================
    0x1e5b: v1e5b(0x2fc) = CONST 
    0x1e5c: CALLPRIVATE v1e5b(0x2fc)

    Begin block 0x162
    prev=[0x157], succ=[0x1e5d, 0x16d]
    =================================
    0x163: v163(0x714ccf7b) = CONST 
    0x168: v168 = EQ v163(0x714ccf7b), v1f
    0x1e30: v1e30(0x1e5d) = CONST 
    0x1e31: JUMPI v1e30(0x1e5d), v168

    Begin block 0x1e5d
    prev=[0x162], succ=[]
    =================================
    0x1e5e: v1e5e(0x322) = CONST 
    0x1e5f: CALLPRIVATE v1e5e(0x322)

    Begin block 0x16d
    prev=[0x162], succ=[0x178, 0x1e60]
    =================================
    0x16e: v16e(0x72cb5d97) = CONST 
    0x173: v173 = EQ v16e(0x72cb5d97), v1f
    0x1e32: v1e32(0x1e60) = CONST 
    0x1e33: JUMPI v1e32(0x1e60), v173

    Begin block 0x178
    prev=[0x16d], succ=[0x17ee]
    =================================
    0x178: v178(0x17ee) = CONST 
    0x17b: JUMP v178(0x17ee)

    Begin block 0x17ee
    prev=[0x178], succ=[]
    =================================
    0x17ef: v17ef(0x0) = CONST 
    0x17f2: REVERT v17ef(0x0), v17ef(0x0)

    Begin block 0x1e60
    prev=[0x16d], succ=[]
    =================================
    0x1e61: v1e61(0x350) = CONST 
    0x1e62: CALLPRIVATE v1e61(0x350)

    Begin block 0x11b
    prev=[0x110], succ=[0x1e63, 0x126]
    =================================
    0x11c: v11c(0x748747e6) = CONST 
    0x121: v121 = EQ v11c(0x748747e6), v1f
    0x1e24: v1e24(0x1e63) = CONST 
    0x1e25: JUMPI v1e24(0x1e63), v121

    Begin block 0x1e63
    prev=[0x11b], succ=[]
    =================================
    0x1e64: v1e64(0x37e) = CONST 
    0x1e65: CALLPRIVATE v1e64(0x37e)

    Begin block 0x126
    prev=[0x11b], succ=[0x1e66, 0x131]
    =================================
    0x127: v127(0x8da1df4d) = CONST 
    0x12c: v12c = EQ v127(0x8da1df4d), v1f
    0x1e26: v1e26(0x1e66) = CONST 
    0x1e27: JUMPI v1e26(0x1e66), v12c

    Begin block 0x1e66
    prev=[0x126], succ=[]
    =================================
    0x1e67: v1e67(0x3a4) = CONST 
    0x1e68: CALLPRIVATE v1e67(0x3a4)

    Begin block 0x131
    prev=[0x126], succ=[0x1e69, 0x13c]
    =================================
    0x132: v132(0x9ec5a894) = CONST 
    0x137: v137 = EQ v132(0x9ec5a894), v1f
    0x1e28: v1e28(0x1e69) = CONST 
    0x1e29: JUMPI v1e28(0x1e69), v137

    Begin block 0x1e69
    prev=[0x131], succ=[]
    =================================
    0x1e6a: v1e6a(0x3ca) = CONST 
    0x1e6b: CALLPRIVATE v1e6a(0x3ca)

    Begin block 0x13c
    prev=[0x131], succ=[0x147, 0x1e6c]
    =================================
    0x13d: v13d(0xa1578b6a) = CONST 
    0x142: v142 = EQ v13d(0xa1578b6a), v1f
    0x1e2a: v1e2a(0x1e6c) = CONST 
    0x1e2b: JUMPI v1e2a(0x1e6c), v142

    Begin block 0x147
    prev=[0x13c], succ=[0x17ca]
    =================================
    0x147: v147(0x17ca) = CONST 
    0x14a: JUMP v147(0x17ca)

    Begin block 0x17ca
    prev=[0x147], succ=[]
    =================================
    0x17cb: v17cb(0x0) = CONST 
    0x17ce: REVERT v17cb(0x0), v17cb(0x0)

    Begin block 0x1e6c
    prev=[0x13c], succ=[]
    =================================
    0x1e6d: v1e6d(0x3d2) = CONST 
    0x1e6e: CALLPRIVATE v1e6d(0x3d2)

    Begin block 0x2b
    prev=[0x1a], succ=[0xa2, 0x36]
    =================================
    0x2c: v2c(0xccd06318) = CONST 
    0x31: v31 = GT v2c(0xccd06318), v1f
    0x32: v32(0xa2) = CONST 
    0x35: JUMPI v32(0xa2), v31

    Begin block 0xa2
    prev=[0x2b], succ=[0xde, 0xae]
    =================================
    0xa4: va4(0xb02bf4b9) = CONST 
    0xa9: va9 = GT va4(0xb02bf4b9), v1f
    0xaa: vaa(0xde) = CONST 
    0xad: JUMPI vaa(0xde), va9

    Begin block 0xde
    prev=[0xa2], succ=[0x1e6f, 0xea]
    =================================
    0xe0: ve0(0xa622ee7c) = CONST 
    0xe5: ve5 = EQ ve0(0xa622ee7c), v1f
    0x1e1e: v1e1e(0x1e6f) = CONST 
    0x1e1f: JUMPI v1e1e(0x1e6f), ve5

    Begin block 0x1e6f
    prev=[0xde], succ=[]
    =================================
    0x1e70: v1e70(0x414) = CONST 
    0x1e71: CALLPRIVATE v1e70(0x414)

    Begin block 0xea
    prev=[0xde], succ=[0x1e72, 0xf5]
    =================================
    0xeb: veb(0xab033ea9) = CONST 
    0xf0: vf0 = EQ veb(0xab033ea9), v1f
    0x1e20: v1e20(0x1e72) = CONST 
    0x1e21: JUMPI v1e20(0x1e72), vf0

    Begin block 0x1e72
    prev=[0xea], succ=[]
    =================================
    0x1e73: v1e73(0x43a) = CONST 
    0x1e74: CALLPRIVATE v1e73(0x43a)

    Begin block 0xf5
    prev=[0xea], succ=[0x100, 0x1e75]
    =================================
    0xf6: vf6(0xaced1661) = CONST 
    0xfb: vfb = EQ vf6(0xaced1661), v1f
    0x1e22: v1e22(0x1e75) = CONST 
    0x1e23: JUMPI v1e22(0x1e75), vfb

    Begin block 0x100
    prev=[0xf5], succ=[0x17a6]
    =================================
    0x100: v100(0x17a6) = CONST 
    0x103: JUMP v100(0x17a6)

    Begin block 0x17a6
    prev=[0x100], succ=[]
    =================================
    0x17a7: v17a7(0x0) = CONST 
    0x17aa: REVERT v17a7(0x0), v17a7(0x0)

    Begin block 0x1e75
    prev=[0xf5], succ=[]
    =================================
    0x1e76: v1e76(0x460) = CONST 
    0x1e77: CALLPRIVATE v1e76(0x460)

    Begin block 0xae
    prev=[0xa2], succ=[0x1e78, 0xb9]
    =================================
    0xaf: vaf(0xb02bf4b9) = CONST 
    0xb4: vb4 = EQ vaf(0xb02bf4b9), v1f
    0x1e16: v1e16(0x1e78) = CONST 
    0x1e17: JUMPI v1e16(0x1e78), vb4

    Begin block 0x1e78
    prev=[0xae], succ=[]
    =================================
    0x1e79: v1e79(0x468) = CONST 
    0x1e7a: CALLPRIVATE v1e79(0x468)

    Begin block 0xb9
    prev=[0xae], succ=[0x1e7b, 0xc4]
    =================================
    0xba: vba(0xc494448e) = CONST 
    0xbf: vbf = EQ vba(0xc494448e), v1f
    0x1e18: v1e18(0x1e7b) = CONST 
    0x1e19: JUMPI v1e18(0x1e7b), vbf

    Begin block 0x1e7b
    prev=[0xb9], succ=[]
    =================================
    0x1e7c: v1e7c(0x494) = CONST 
    0x1e7d: CALLPRIVATE v1e7c(0x494)

    Begin block 0xc4
    prev=[0xb9], succ=[0x1e7e, 0xcf]
    =================================
    0xc5: vc5(0xc6d758cb) = CONST 
    0xca: vca = EQ vc5(0xc6d758cb), v1f
    0x1e1a: v1e1a(0x1e7e) = CONST 
    0x1e1b: JUMPI v1e1a(0x1e7e), vca

    Begin block 0x1e7e
    prev=[0xc4], succ=[]
    =================================
    0x1e7f: v1e7f(0x4c2) = CONST 
    0x1e80: CALLPRIVATE v1e7f(0x4c2)

    Begin block 0xcf
    prev=[0xc4], succ=[0xda, 0x1e81]
    =================================
    0xd0: vd0(0xc7b9d530) = CONST 
    0xd5: vd5 = EQ vd0(0xc7b9d530), v1f
    0x1e1c: v1e1c(0x1e81) = CONST 
    0x1e1d: JUMPI v1e1c(0x1e81), vd5

    Begin block 0xda
    prev=[0xcf], succ=[0x1782]
    =================================
    0xda: vda(0x1782) = CONST 
    0xdd: JUMP vda(0x1782)

    Begin block 0x1782
    prev=[0xda], succ=[]
    =================================
    0x1783: v1783(0x0) = CONST 
    0x1786: REVERT v1783(0x0), v1783(0x0)

    Begin block 0x1e81
    prev=[0xcf], succ=[]
    =================================
    0x1e82: v1e82(0x4ee) = CONST 
    0x1e83: CALLPRIVATE v1e82(0x4ee)

    Begin block 0x36
    prev=[0x2b], succ=[0x71, 0x41]
    =================================
    0x37: v37(0xf712adbb) = CONST 
    0x3c: v3c = GT v37(0xf712adbb), v1f
    0x3d: v3d(0x71) = CONST 
    0x40: JUMPI v3d(0x71), v3c

    Begin block 0x71
    prev=[0x36], succ=[0x1e84, 0x7d]
    =================================
    0x73: v73(0xccd06318) = CONST 
    0x78: v78 = EQ v73(0xccd06318), v1f
    0x1e0e: v1e0e(0x1e84) = CONST 
    0x1e0f: JUMPI v1e0e(0x1e84), v78

    Begin block 0x1e84
    prev=[0x71], succ=[]
    =================================
    0x1e85: v1e85(0x514) = CONST 
    0x1e86: CALLPRIVATE v1e85(0x514)

    Begin block 0x7d
    prev=[0x71], succ=[0x1e87, 0x88]
    =================================
    0x7e: v7e(0xe4f2494d) = CONST 
    0x83: v83 = EQ v7e(0xe4f2494d), v1f
    0x1e10: v1e10(0x1e87) = CONST 
    0x1e11: JUMPI v1e10(0x1e87), v83

    Begin block 0x1e87
    prev=[0x7d], succ=[]
    =================================
    0x1e88: v1e88(0x54c) = CONST 
    0x1e89: CALLPRIVATE v1e88(0x54c)

    Begin block 0x88
    prev=[0x7d], succ=[0x1e8a, 0x93]
    =================================
    0x89: v89(0xec38a862) = CONST 
    0x8e: v8e = EQ v89(0xec38a862), v1f
    0x1e12: v1e12(0x1e8a) = CONST 
    0x1e13: JUMPI v1e12(0x1e8a), v8e

    Begin block 0x1e8a
    prev=[0x88], succ=[]
    =================================
    0x1e8b: v1e8b(0x57a) = CONST 
    0x1e8c: CALLPRIVATE v1e8b(0x57a)

    Begin block 0x93
    prev=[0x88], succ=[0x9e, 0x1e8d]
    =================================
    0x94: v94(0xf3fef3a3) = CONST 
    0x99: v99 = EQ v94(0xf3fef3a3), v1f
    0x1e14: v1e14(0x1e8d) = CONST 
    0x1e15: JUMPI v1e14(0x1e8d), v99

    Begin block 0x9e
    prev=[0x93], succ=[0x175e]
    =================================
    0x9e: v9e(0x175e) = CONST 
    0xa1: JUMP v9e(0x175e)

    Begin block 0x175e
    prev=[0x9e], succ=[]
    =================================
    0x175f: v175f(0x0) = CONST 
    0x1762: REVERT v175f(0x0), v175f(0x0)

    Begin block 0x1e8d
    prev=[0x93], succ=[]
    =================================
    0x1e8e: v1e8e(0x5a0) = CONST 
    0x1e8f: CALLPRIVATE v1e8e(0x5a0)

    Begin block 0x41
    prev=[0x36], succ=[0x1e90, 0x4c]
    =================================
    0x42: v42(0xf712adbb) = CONST 
    0x47: v47 = EQ v42(0xf712adbb), v1f
    0x1e06: v1e06(0x1e90) = CONST 
    0x1e07: JUMPI v1e06(0x1e90), v47

    Begin block 0x1e90
    prev=[0x41], succ=[]
    =================================
    0x1e91: v1e91(0x5cc) = CONST 
    0x1e92: CALLPRIVATE v1e91(0x5cc)

    Begin block 0x4c
    prev=[0x41], succ=[0x1e93, 0x57]
    =================================
    0x4d: v4d(0xf7654176) = CONST 
    0x52: v52 = EQ v4d(0xf7654176), v1f
    0x1e08: v1e08(0x1e93) = CONST 
    0x1e09: JUMPI v1e08(0x1e93), v52

    Begin block 0x1e93
    prev=[0x4c], succ=[]
    =================================
    0x1e94: v1e94(0x5d4) = CONST 
    0x1e95: CALLPRIVATE v1e94(0x5d4)

    Begin block 0x57
    prev=[0x4c], succ=[0x1e96, 0x62]
    =================================
    0x58: v58(0xf8c8765e) = CONST 
    0x5d: v5d = EQ v58(0xf8c8765e), v1f
    0x1e0a: v1e0a(0x1e96) = CONST 
    0x1e0b: JUMPI v1e0a(0x1e96), v5d

    Begin block 0x1e96
    prev=[0x57], succ=[]
    =================================
    0x1e97: v1e97(0x5dc) = CONST 
    0x1e98: CALLPRIVATE v1e97(0x5dc)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0x1e99]
    =================================
    0x63: v63(0xfa09e630) = CONST 
    0x68: v68 = EQ v63(0xfa09e630), v1f
    0x1e0c: v1e0c(0x1e99) = CONST 
    0x1e0d: JUMPI v1e0c(0x1e99), v68

    Begin block 0x6d
    prev=[0x62], succ=[0x173a]
    =================================
    0x6d: v6d(0x173a) = CONST 
    0x70: JUMP v6d(0x173a)

    Begin block 0x173a
    prev=[0x6d], succ=[]
    =================================
    0x173b: v173b(0x0) = CONST 
    0x173e: REVERT v173b(0x0), v173b(0x0)

    Begin block 0x1e99
    prev=[0x62], succ=[]
    =================================
    0x1e9a: v1e9a(0x61a) = CONST 
    0x1e9b: CALLPRIVATE v1e9a(0x61a)

    Begin block 0x1e9c
    prev=[0x10], succ=[]
    =================================
    0x1e9d: v1e9d(0x1716) = CONST 
    0x1e9e: CALLPRIVATE v1e9d(0x1716)

}

function 0x1222(0x1222arg0x0) private {
    Begin block 0x1222
    prev=[], succ=[0x124b, 0x1236]
    =================================
    0x1223: v1223(0x1) = CONST 
    0x1225: v1225 = SLOAD v1223(0x1)
    0x1226: v1226(0x1) = CONST 
    0x1228: v1228(0x1) = CONST 
    0x122a: v122a(0xa0) = CONST 
    0x122c: v122c(0x10000000000000000000000000000000000000000) = SHL v122a(0xa0), v1228(0x1)
    0x122d: v122d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v122c(0x10000000000000000000000000000000000000000), v1226(0x1)
    0x122e: v122e = AND v122d(0xffffffffffffffffffffffffffffffffffffffff), v1225
    0x122f: v122f = CALLER 
    0x1230: v1230 = EQ v122f, v122e
    0x1232: v1232(0x124b) = CONST 
    0x1235: JUMPI v1232(0x124b), v1230

    Begin block 0x124b
    prev=[0x1222, 0x1236], succ=[0x1250, 0x1d27]
    =================================
    0x124b_0x0: v124b_0 = PHI v1230, v124a
    0x124c: v124c(0x1d27) = CONST 
    0x124f: JUMPI v124c(0x1d27), v124b_0

    Begin block 0x1250
    prev=[0x124b], succ=[]
    =================================
    0x1250: v1250(0x40) = CONST 
    0x1253: v1253 = MLOAD v1250(0x40)
    0x1254: v1254(0x461bcd) = CONST 
    0x1258: v1258(0xe5) = CONST 
    0x125a: v125a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1258(0xe5), v1254(0x461bcd)
    0x125c: MSTORE v1253, v125a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x125d: v125d(0x20) = CONST 
    0x125f: v125f(0x4) = CONST 
    0x1262: v1262 = ADD v1253, v125f(0x4)
    0x1263: MSTORE v1262, v125d(0x20)
    0x1264: v1264(0x1a) = CONST 
    0x1266: v1266(0x24) = CONST 
    0x1269: v1269 = ADD v1253, v1266(0x24)
    0x126a: MSTORE v1269, v1264(0x1a)
    0x126b: v126b(0x6f6e6c79476f7665726e616e63654f7253747261746567697374000000000000) = CONST 
    0x128c: v128c(0x44) = CONST 
    0x128f: v128f = ADD v1253, v128c(0x44)
    0x1290: MSTORE v128f, v126b(0x6f6e6c79476f7665726e616e63654f7253747261746567697374000000000000)
    0x1292: v1292 = MLOAD v1250(0x40)
    0x1296: v1296(0x0) = SUB v1253, v1292
    0x1297: v1297(0x64) = CONST 
    0x1299: v1299(0x64) = ADD v1297(0x64), v1296(0x0)
    0x129b: REVERT v1292, v1299(0x64)

    Begin block 0x1d27
    prev=[0x124b], succ=[]
    =================================
    0x1d28: RETURNPRIVATE v1222arg0

    Begin block 0x1236
    prev=[0x1222], succ=[0x124b]
    =================================
    0x1237: v1237(0x0) = CONST 
    0x1239: v1239 = SLOAD v1237(0x0)
    0x123a: v123a(0x10000) = CONST 
    0x123f: v123f = DIV v1239, v123a(0x10000)
    0x1240: v1240(0x1) = CONST 
    0x1242: v1242(0x1) = CONST 
    0x1244: v1244(0xa0) = CONST 
    0x1246: v1246(0x10000000000000000000000000000000000000000) = SHL v1244(0xa0), v1242(0x1)
    0x1247: v1247(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1246(0x10000000000000000000000000000000000000000), v1240(0x1)
    0x1248: v1248 = AND v1247(0xffffffffffffffffffffffffffffffffffffffff), v123f
    0x1249: v1249 = CALLER 
    0x124a: v124a = EQ v1249, v1248

}

function 0x1398(0x1398arg0x0, 0x1398arg0x1, 0x1398arg0x2, 0x1398arg0x3) private {
    Begin block 0x1398
    prev=[], succ=[0x13f0B0x1398]
    =================================
    0x1399: v1399(0x40) = CONST 
    0x139c: v139c = MLOAD v1399(0x40)
    0x139d: v139d(0x1) = CONST 
    0x139f: v139f(0x1) = CONST 
    0x13a1: v13a1(0xa0) = CONST 
    0x13a3: v13a3(0x10000000000000000000000000000000000000000) = SHL v13a1(0xa0), v139f(0x1)
    0x13a4: v13a4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13a3(0x10000000000000000000000000000000000000000), v139d(0x1)
    0x13a6: v13a6 = AND v1398arg1, v13a4(0xffffffffffffffffffffffffffffffffffffffff)
    0x13a7: v13a7(0x24) = CONST 
    0x13aa: v13aa = ADD v139c, v13a7(0x24)
    0x13ab: MSTORE v13aa, v13a6
    0x13ac: v13ac(0x44) = CONST 
    0x13b0: v13b0 = ADD v139c, v13ac(0x44)
    0x13b3: MSTORE v13b0, v1398arg0
    0x13b5: v13b5 = MLOAD v1399(0x40)
    0x13b8: v13b8(0x0) = SUB v139c, v13b5
    0x13bb: v13bb(0x44) = ADD v13ac(0x44), v13b8(0x0)
    0x13bd: MSTORE v13b5, v13bb(0x44)
    0x13be: v13be(0x64) = CONST 
    0x13c2: v13c2 = ADD v139c, v13be(0x64)
    0x13c5: MSTORE v1399(0x40), v13c2
    0x13c6: v13c6(0x20) = CONST 
    0x13c9: v13c9 = ADD v13b5, v13c6(0x20)
    0x13cb: v13cb = MLOAD v13c9
    0x13cc: v13cc(0x1) = CONST 
    0x13ce: v13ce(0x1) = CONST 
    0x13d0: v13d0(0xe0) = CONST 
    0x13d2: v13d2(0x100000000000000000000000000000000000000000000000000000000) = SHL v13d0(0xe0), v13ce(0x1)
    0x13d3: v13d3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v13d2(0x100000000000000000000000000000000000000000000000000000000), v13cc(0x1)
    0x13d4: v13d4 = AND v13d3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v13cb
    0x13d5: v13d5(0xa9059cbb) = CONST 
    0x13da: v13da(0xe0) = CONST 
    0x13dc: v13dc(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL v13da(0xe0), v13d5(0xa9059cbb)
    0x13dd: v13dd = OR v13dc(0xa9059cbb00000000000000000000000000000000000000000000000000000000), v13d4
    0x13df: MSTORE v13c9, v13dd
    0x13e0: v13e0(0x1d69) = CONST 
    0x13e6: v13e6(0x13f0) = CONST 
    0x13e9: JUMP v13e6(0x13f0), v13b5, v1398arg2, v13e0(0x1d69)

    Begin block 0x13f0B0x1398
    prev=[0x1398], succ=[0x14a1B0x13f0B0x1398]
    =================================
    0x13f1S0x1398: v13f1V1398(0x60) = CONST 
    0x13f3S0x1398: v13f3V1398(0x1445) = CONST 
    0x13f7S0x1398: v13f7V1398(0x40) = CONST 
    0x13f9S0x1398: v13f9V1398 = MLOAD v13f7V1398(0x40)
    0x13fbS0x1398: v13fbV1398(0x40) = CONST 
    0x13fdS0x1398: v13fdV1398 = ADD v13fbV1398(0x40), v13f9V1398
    0x13feS0x1398: v13feV1398(0x40) = CONST 
    0x1400S0x1398: MSTORE v13feV1398(0x40), v13fdV1398
    0x1402S0x1398: v1402V1398(0x20) = CONST 
    0x1405S0x1398: MSTORE v13f9V1398, v1402V1398(0x20)
    0x1406S0x1398: v1406V1398(0x20) = CONST 
    0x1408S0x1398: v1408V1398 = ADD v1406V1398(0x20), v13f9V1398
    0x1409S0x1398: v1409V1398(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564) = CONST 
    0x142bS0x1398: MSTORE v1408V1398, v1409V1398(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564)
    0x142eS0x1398: v142eV1398(0x1) = CONST 
    0x1430S0x1398: v1430V1398(0x1) = CONST 
    0x1432S0x1398: v1432V1398(0xa0) = CONST 
    0x1434S0x1398: v1434V1398(0x10000000000000000000000000000000000000000) = SHL v1432V1398(0xa0), v1430V1398(0x1)
    0x1435S0x1398: v1435V1398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1434V1398(0x10000000000000000000000000000000000000000), v142eV1398(0x1)
    0x1436S0x1398: v1436V1398 = AND v1435V1398(0xffffffffffffffffffffffffffffffffffffffff), v1398arg2
    0x1437S0x1398: v1437V1398(0x14a1) = CONST 
    0x143eS0x1398: v143eV1398(0xffffffff) = CONST 
    0x1443S0x1398: v1443V1398(0x14a1) = AND v143eV1398(0xffffffff), v1437V1398(0x14a1)
    0x1444S0x1398: JUMP v1443V1398(0x14a1)

    Begin block 0x14a1B0x13f0B0x1398
    prev=[0x13f0B0x1398], succ=[0x14b8B0x14a1B0x13f0B0x1398]
    =================================
    0x14a2S0x13f0S0x1398: v14a2V13f0V1398(0x60) = CONST 
    0x14a4S0x13f0S0x1398: v14a4V13f0V1398(0x1dd5) = CONST 
    0x14a9S0x13f0S0x1398: v14a9V13f0V1398(0x0) = CONST 
    0x14acS0x13f0S0x1398: v14acV13f0V1398(0x14b8) = CONST 
    0x14afS0x13f0S0x1398: JUMP v14acV13f0V1398(0x14b8)

    Begin block 0x14b8B0x14a1B0x13f0B0x1398
    prev=[0x14a1B0x13f0B0x1398], succ=[0x1663B0x14a1B0x13f0B0x1398]
    =================================
    0x14b9S0x14a1S0x13f0S0x1398: v14b9V14a1V13f0V1398(0x60) = CONST 
    0x14bbS0x14a1S0x13f0S0x1398: v14bbV14a1V13f0V1398(0x14c3) = CONST 
    0x14bfS0x14a1S0x13f0S0x1398: v14bfV14a1V13f0V1398(0x1663) = CONST 
    0x14c2S0x14a1S0x13f0S0x1398: JUMP v14bfV14a1V13f0V1398(0x1663)

    Begin block 0x1663B0x14a1B0x13f0B0x1398
    prev=[0x14b8B0x14a1B0x13f0B0x1398], succ=[0x14c3B0x14a1B0x13f0B0x1398]
    =================================
    0x1664S0x14a1S0x13f0S0x1398: v1664V14a1V13f0V1398 = EXTCODESIZE v1436V1398
    0x1665S0x14a1S0x13f0S0x1398: v1665V14a1V13f0V1398 = ISZERO v1664V14a1V13f0V1398
    0x1666S0x14a1S0x13f0S0x1398: v1666V14a1V13f0V1398 = ISZERO v1665V14a1V13f0V1398
    0x1668S0x14a1S0x13f0S0x1398: JUMP v14bbV14a1V13f0V1398(0x14c3)

    Begin block 0x14c3B0x14a1B0x13f0B0x1398
    prev=[0x1663B0x14a1B0x13f0B0x1398], succ=[0x14c8B0x14a1B0x13f0B0x1398, 0x1514B0x14a1B0x13f0B0x1398]
    =================================
    0x14c4S0x14a1S0x13f0S0x1398: v14c4V14a1V13f0V1398(0x1514) = CONST 
    0x14c7S0x14a1S0x13f0S0x1398: JUMPI v14c4V14a1V13f0V1398(0x1514), v1666V14a1V13f0V1398

    Begin block 0x14c8B0x14a1B0x13f0B0x1398
    prev=[0x14c3B0x14a1B0x13f0B0x1398], succ=[]
    =================================
    0x14c8S0x14a1S0x13f0S0x1398: v14c8V14a1V13f0V1398(0x40) = CONST 
    0x14cbS0x14a1S0x13f0S0x1398: v14cbV14a1V13f0V1398 = MLOAD v14c8V14a1V13f0V1398(0x40)
    0x14ccS0x14a1S0x13f0S0x1398: v14ccV14a1V13f0V1398(0x461bcd) = CONST 
    0x14d0S0x14a1S0x13f0S0x1398: v14d0V14a1V13f0V1398(0xe5) = CONST 
    0x14d2S0x14a1S0x13f0S0x1398: v14d2V14a1V13f0V1398(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v14d0V14a1V13f0V1398(0xe5), v14ccV14a1V13f0V1398(0x461bcd)
    0x14d4S0x14a1S0x13f0S0x1398: MSTORE v14cbV14a1V13f0V1398, v14d2V14a1V13f0V1398(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14d5S0x14a1S0x13f0S0x1398: v14d5V14a1V13f0V1398(0x20) = CONST 
    0x14d7S0x14a1S0x13f0S0x1398: v14d7V14a1V13f0V1398(0x4) = CONST 
    0x14daS0x14a1S0x13f0S0x1398: v14daV14a1V13f0V1398 = ADD v14cbV14a1V13f0V1398, v14d7V14a1V13f0V1398(0x4)
    0x14dbS0x14a1S0x13f0S0x1398: MSTORE v14daV14a1V13f0V1398, v14d5V14a1V13f0V1398(0x20)
    0x14dcS0x14a1S0x13f0S0x1398: v14dcV14a1V13f0V1398(0x1d) = CONST 
    0x14deS0x14a1S0x13f0S0x1398: v14deV14a1V13f0V1398(0x24) = CONST 
    0x14e1S0x14a1S0x13f0S0x1398: v14e1V14a1V13f0V1398 = ADD v14cbV14a1V13f0V1398, v14deV14a1V13f0V1398(0x24)
    0x14e2S0x14a1S0x13f0S0x1398: MSTORE v14e1V14a1V13f0V1398, v14dcV14a1V13f0V1398(0x1d)
    0x14e3S0x14a1S0x13f0S0x1398: v14e3V14a1V13f0V1398(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000) = CONST 
    0x1504S0x14a1S0x13f0S0x1398: v1504V14a1V13f0V1398(0x44) = CONST 
    0x1507S0x14a1S0x13f0S0x1398: v1507V14a1V13f0V1398 = ADD v14cbV14a1V13f0V1398, v1504V14a1V13f0V1398(0x44)
    0x1508S0x14a1S0x13f0S0x1398: MSTORE v1507V14a1V13f0V1398, v14e3V14a1V13f0V1398(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000)
    0x150aS0x14a1S0x13f0S0x1398: v150aV14a1V13f0V1398 = MLOAD v14c8V14a1V13f0V1398(0x40)
    0x150eS0x14a1S0x13f0S0x1398: v150eV14a1V13f0V1398(0x0) = SUB v14cbV14a1V13f0V1398, v150aV14a1V13f0V1398
    0x150fS0x14a1S0x13f0S0x1398: v150fV14a1V13f0V1398(0x64) = CONST 
    0x1511S0x14a1S0x13f0S0x1398: v1511V14a1V13f0V1398(0x64) = ADD v150fV14a1V13f0V1398(0x64), v150eV14a1V13f0V1398(0x0)
    0x1513S0x14a1S0x13f0S0x1398: REVERT v150aV14a1V13f0V1398, v1511V14a1V13f0V1398(0x64)

    Begin block 0x1514B0x14a1B0x13f0B0x1398
    prev=[0x14c3B0x14a1B0x13f0B0x1398], succ=[0x1534B0x14a1B0x13f0B0x1398]
    =================================
    0x1515S0x14a1S0x13f0S0x1398: v1515V14a1V13f0V1398(0x0) = CONST 
    0x1517S0x14a1S0x13f0S0x1398: v1517V14a1V13f0V1398(0x60) = CONST 
    0x151aS0x14a1S0x13f0S0x1398: v151aV14a1V13f0V1398(0x1) = CONST 
    0x151cS0x14a1S0x13f0S0x1398: v151cV14a1V13f0V1398(0x1) = CONST 
    0x151eS0x14a1S0x13f0S0x1398: v151eV14a1V13f0V1398(0xa0) = CONST 
    0x1520S0x14a1S0x13f0S0x1398: v1520V14a1V13f0V1398(0x10000000000000000000000000000000000000000) = SHL v151eV14a1V13f0V1398(0xa0), v151cV14a1V13f0V1398(0x1)
    0x1521S0x14a1S0x13f0S0x1398: v1521V14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1520V14a1V13f0V1398(0x10000000000000000000000000000000000000000), v151aV14a1V13f0V1398(0x1)
    0x1522S0x14a1S0x13f0S0x1398: v1522V14a1V13f0V1398 = AND v1521V14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffff), v1436V1398
    0x1525S0x14a1S0x13f0S0x1398: v1525V14a1V13f0V1398(0x40) = CONST 
    0x1527S0x14a1S0x13f0S0x1398: v1527V14a1V13f0V1398 = MLOAD v1525V14a1V13f0V1398(0x40)
    0x152bS0x14a1S0x13f0S0x1398: v152bV14a1V13f0V1398(0x44) = MLOAD v13b5
    0x152dS0x14a1S0x13f0S0x1398: v152dV14a1V13f0V1398(0x20) = CONST 
    0x152fS0x14a1S0x13f0S0x1398: v152fV14a1V13f0V1398 = ADD v152dV14a1V13f0V1398(0x20), v13b5

    Begin block 0x1534B0x14a1B0x13f0B0x1398
    prev=[0x1514B0x14a1B0x13f0B0x1398, 0x153dB0x14a1B0x13f0B0x1398], succ=[0x1553B0x14a1B0x13f0B0x1398, 0x153dB0x14a1B0x13f0B0x1398]
    =================================
    0x1534_0x2S0x14a1S0x13f0S0x1398: v1534_2V14a1V13f0V1398 = PHI v152bV14a1V13f0V1398(0x44), v1546V14a1V13f0V1398
    0x1535S0x14a1S0x13f0S0x1398: v1535V14a1V13f0V1398(0x20) = CONST 
    0x1538S0x14a1S0x13f0S0x1398: v1538V14a1V13f0V1398 = LT v1534_2V14a1V13f0V1398, v1535V14a1V13f0V1398(0x20)
    0x1539S0x14a1S0x13f0S0x1398: v1539V14a1V13f0V1398(0x1553) = CONST 
    0x153cS0x14a1S0x13f0S0x1398: JUMPI v1539V14a1V13f0V1398(0x1553), v1538V14a1V13f0V1398

    Begin block 0x1553B0x14a1B0x13f0B0x1398
    prev=[0x1534B0x14a1B0x13f0B0x1398], succ=[0x1594B0x14a1B0x13f0B0x1398, 0x15b5B0x14a1B0x13f0B0x1398]
    =================================
    0x1553_0x0S0x14a1S0x13f0S0x1398: v1553_0V14a1V13f0V1398 = PHI v152fV14a1V13f0V1398, v154eV14a1V13f0V1398
    0x1553_0x1S0x14a1S0x13f0S0x1398: v1553_1V14a1V13f0V1398 = PHI v1527V14a1V13f0V1398, v154cV14a1V13f0V1398
    0x1553_0x2S0x14a1S0x13f0S0x1398: v1553_2V14a1V13f0V1398 = PHI v152bV14a1V13f0V1398(0x44), v1546V14a1V13f0V1398
    0x1554S0x14a1S0x13f0S0x1398: v1554V14a1V13f0V1398(0x1) = CONST 
    0x1557S0x14a1S0x13f0S0x1398: v1557V14a1V13f0V1398(0x20) = CONST 
    0x1559S0x14a1S0x13f0S0x1398: v1559V14a1V13f0V1398 = SUB v1557V14a1V13f0V1398(0x20), v1553_2V14a1V13f0V1398
    0x155aS0x14a1S0x13f0S0x1398: v155aV14a1V13f0V1398(0x100) = CONST 
    0x155dS0x14a1S0x13f0S0x1398: v155dV14a1V13f0V1398 = EXP v155aV14a1V13f0V1398(0x100), v1559V14a1V13f0V1398
    0x155eS0x14a1S0x13f0S0x1398: v155eV14a1V13f0V1398 = SUB v155dV14a1V13f0V1398, v1554V14a1V13f0V1398(0x1)
    0x1560S0x14a1S0x13f0S0x1398: v1560V14a1V13f0V1398 = NOT v155eV14a1V13f0V1398
    0x1562S0x14a1S0x13f0S0x1398: v1562V14a1V13f0V1398 = MLOAD v1553_0V14a1V13f0V1398
    0x1563S0x14a1S0x13f0S0x1398: v1563V14a1V13f0V1398 = AND v1562V14a1V13f0V1398, v1560V14a1V13f0V1398
    0x1566S0x14a1S0x13f0S0x1398: v1566V14a1V13f0V1398 = MLOAD v1553_1V14a1V13f0V1398
    0x1567S0x14a1S0x13f0S0x1398: v1567V14a1V13f0V1398 = AND v1566V14a1V13f0V1398, v155eV14a1V13f0V1398
    0x156aS0x14a1S0x13f0S0x1398: v156aV14a1V13f0V1398 = OR v1563V14a1V13f0V1398, v1567V14a1V13f0V1398
    0x156cS0x14a1S0x13f0S0x1398: MSTORE v1553_1V14a1V13f0V1398, v156aV14a1V13f0V1398
    0x1575S0x14a1S0x13f0S0x1398: v1575V14a1V13f0V1398 = ADD v152bV14a1V13f0V1398(0x44), v1527V14a1V13f0V1398
    0x1579S0x14a1S0x13f0S0x1398: v1579V14a1V13f0V1398(0x0) = CONST 
    0x157bS0x14a1S0x13f0S0x1398: v157bV14a1V13f0V1398(0x40) = CONST 
    0x157dS0x14a1S0x13f0S0x1398: v157dV14a1V13f0V1398 = MLOAD v157bV14a1V13f0V1398(0x40)
    0x1580S0x14a1S0x13f0S0x1398: v1580V14a1V13f0V1398(0x44) = SUB v1575V14a1V13f0V1398, v157dV14a1V13f0V1398
    0x1584S0x14a1S0x13f0S0x1398: v1584V14a1V13f0V1398 = GAS 
    0x1585S0x14a1S0x13f0S0x1398: v1585V14a1V13f0V1398 = CALL v1584V14a1V13f0V1398, v1522V14a1V13f0V1398, v14a9V13f0V1398(0x0), v157dV14a1V13f0V1398, v1580V14a1V13f0V1398(0x44), v157dV14a1V13f0V1398, v1579V14a1V13f0V1398(0x0)
    0x158aS0x14a1S0x13f0S0x1398: v158aV14a1V13f0V1398 = RETURNDATASIZE 
    0x158cS0x14a1S0x13f0S0x1398: v158cV14a1V13f0V1398(0x0) = CONST 
    0x158fS0x14a1S0x13f0S0x1398: v158fV14a1V13f0V1398 = EQ v158aV14a1V13f0V1398, v158cV14a1V13f0V1398(0x0)
    0x1590S0x14a1S0x13f0S0x1398: v1590V14a1V13f0V1398(0x15b5) = CONST 
    0x1593S0x14a1S0x13f0S0x1398: JUMPI v1590V14a1V13f0V1398(0x15b5), v158fV14a1V13f0V1398

    Begin block 0x1594B0x14a1B0x13f0B0x1398
    prev=[0x1553B0x14a1B0x13f0B0x1398], succ=[0x15baB0x14a1B0x13f0B0x1398]
    =================================
    0x1594S0x14a1S0x13f0S0x1398: v1594V14a1V13f0V1398(0x40) = CONST 
    0x1596S0x14a1S0x13f0S0x1398: v1596V14a1V13f0V1398 = MLOAD v1594V14a1V13f0V1398(0x40)
    0x1599S0x14a1S0x13f0S0x1398: v1599V14a1V13f0V1398(0x1f) = CONST 
    0x159bS0x14a1S0x13f0S0x1398: v159bV14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1599V14a1V13f0V1398(0x1f)
    0x159cS0x14a1S0x13f0S0x1398: v159cV14a1V13f0V1398(0x3f) = CONST 
    0x159eS0x14a1S0x13f0S0x1398: v159eV14a1V13f0V1398 = RETURNDATASIZE 
    0x159fS0x14a1S0x13f0S0x1398: v159fV14a1V13f0V1398 = ADD v159eV14a1V13f0V1398, v159cV14a1V13f0V1398(0x3f)
    0x15a0S0x14a1S0x13f0S0x1398: v15a0V14a1V13f0V1398 = AND v159fV14a1V13f0V1398, v159bV14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x15a2S0x14a1S0x13f0S0x1398: v15a2V14a1V13f0V1398 = ADD v1596V14a1V13f0V1398, v15a0V14a1V13f0V1398
    0x15a3S0x14a1S0x13f0S0x1398: v15a3V14a1V13f0V1398(0x40) = CONST 
    0x15a5S0x14a1S0x13f0S0x1398: MSTORE v15a3V14a1V13f0V1398(0x40), v15a2V14a1V13f0V1398
    0x15a6S0x14a1S0x13f0S0x1398: v15a6V14a1V13f0V1398 = RETURNDATASIZE 
    0x15a8S0x14a1S0x13f0S0x1398: MSTORE v1596V14a1V13f0V1398, v15a6V14a1V13f0V1398
    0x15a9S0x14a1S0x13f0S0x1398: v15a9V14a1V13f0V1398 = RETURNDATASIZE 
    0x15aaS0x14a1S0x13f0S0x1398: v15aaV14a1V13f0V1398(0x0) = CONST 
    0x15acS0x14a1S0x13f0S0x1398: v15acV14a1V13f0V1398(0x20) = CONST 
    0x15afS0x14a1S0x13f0S0x1398: v15afV14a1V13f0V1398 = ADD v1596V14a1V13f0V1398, v15acV14a1V13f0V1398(0x20)
    0x15b0S0x14a1S0x13f0S0x1398: RETURNDATACOPY v15afV14a1V13f0V1398, v15aaV14a1V13f0V1398(0x0), v15a9V14a1V13f0V1398
    0x15b1S0x14a1S0x13f0S0x1398: v15b1V14a1V13f0V1398(0x15ba) = CONST 
    0x15b4S0x14a1S0x13f0S0x1398: JUMP v15b1V14a1V13f0V1398(0x15ba)

    Begin block 0x15baB0x14a1B0x13f0B0x1398
    prev=[0x1594B0x14a1B0x13f0B0x1398, 0x15b5B0x14a1B0x13f0B0x1398], succ=[0x15ceB0x14a1B0x13f0B0x1398, 0x15c6B0x14a1B0x13f0B0x1398]
    =================================
    0x15c1S0x14a1S0x13f0S0x1398: v15c1V14a1V13f0V1398 = ISZERO v1585V14a1V13f0V1398
    0x15c2S0x14a1S0x13f0S0x1398: v15c2V14a1V13f0V1398(0x15ce) = CONST 
    0x15c5S0x14a1S0x13f0S0x1398: JUMPI v15c2V14a1V13f0V1398(0x15ce), v15c1V14a1V13f0V1398

    Begin block 0x15ceB0x14a1B0x13f0B0x1398
    prev=[0x15baB0x14a1B0x13f0B0x1398], succ=[0x15deB0x14a1B0x13f0B0x1398, 0x15d6B0x14a1B0x13f0B0x1398]
    =================================
    0x15ce_0x0S0x14a1S0x13f0S0x1398: v15ce_0V14a1V13f0V1398 = PHI v1596V14a1V13f0V1398, v15b6V14a1V13f0V1398(0x60)
    0x15d0S0x14a1S0x13f0S0x1398: v15d0V14a1V13f0V1398 = MLOAD v15ce_0V14a1V13f0V1398
    0x15d1S0x14a1S0x13f0S0x1398: v15d1V14a1V13f0V1398 = ISZERO v15d0V14a1V13f0V1398
    0x15d2S0x14a1S0x13f0S0x1398: v15d2V14a1V13f0V1398(0x15de) = CONST 
    0x15d5S0x14a1S0x13f0S0x1398: JUMPI v15d2V14a1V13f0V1398(0x15de), v15d1V14a1V13f0V1398

    Begin block 0x15deB0x14a1B0x13f0B0x1398
    prev=[0x15ceB0x14a1B0x13f0B0x1398], succ=[0x1610B0x14a1B0x13f0B0x1398]
    =================================
    0x15e0S0x14a1S0x13f0S0x1398: v15e0V14a1V13f0V1398(0x40) = CONST 
    0x15e2S0x14a1S0x13f0S0x1398: v15e2V14a1V13f0V1398 = MLOAD v15e0V14a1V13f0V1398(0x40)
    0x15e3S0x14a1S0x13f0S0x1398: v15e3V14a1V13f0V1398(0x461bcd) = CONST 
    0x15e7S0x14a1S0x13f0S0x1398: v15e7V14a1V13f0V1398(0xe5) = CONST 
    0x15e9S0x14a1S0x13f0S0x1398: v15e9V14a1V13f0V1398(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v15e7V14a1V13f0V1398(0xe5), v15e3V14a1V13f0V1398(0x461bcd)
    0x15ebS0x14a1S0x13f0S0x1398: MSTORE v15e2V14a1V13f0V1398, v15e9V14a1V13f0V1398(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15ecS0x14a1S0x13f0S0x1398: v15ecV14a1V13f0V1398(0x4) = CONST 
    0x15eeS0x14a1S0x13f0S0x1398: v15eeV14a1V13f0V1398 = ADD v15ecV14a1V13f0V1398(0x4), v15e2V14a1V13f0V1398
    0x15f1S0x14a1S0x13f0S0x1398: v15f1V14a1V13f0V1398(0x20) = CONST 
    0x15f3S0x14a1S0x13f0S0x1398: v15f3V14a1V13f0V1398 = ADD v15f1V14a1V13f0V1398(0x20), v15eeV14a1V13f0V1398
    0x15f6S0x14a1S0x13f0S0x1398: v15f6V14a1V13f0V1398(0x20) = SUB v15f3V14a1V13f0V1398, v15eeV14a1V13f0V1398
    0x15f8S0x14a1S0x13f0S0x1398: MSTORE v15eeV14a1V13f0V1398, v15f6V14a1V13f0V1398(0x20)
    0x15fcS0x14a1S0x13f0S0x1398: v15fcV14a1V13f0V1398(0x20) = MLOAD v13f9V1398
    0x15feS0x14a1S0x13f0S0x1398: MSTORE v15f3V14a1V13f0V1398, v15fcV14a1V13f0V1398(0x20)
    0x15ffS0x14a1S0x13f0S0x1398: v15ffV14a1V13f0V1398(0x20) = CONST 
    0x1601S0x14a1S0x13f0S0x1398: v1601V14a1V13f0V1398 = ADD v15ffV14a1V13f0V1398(0x20), v15f3V14a1V13f0V1398
    0x1605S0x14a1S0x13f0S0x1398: v1605V14a1V13f0V1398(0x20) = MLOAD v13f9V1398
    0x1607S0x14a1S0x13f0S0x1398: v1607V14a1V13f0V1398(0x20) = CONST 
    0x1609S0x14a1S0x13f0S0x1398: v1609V14a1V13f0V1398 = ADD v1607V14a1V13f0V1398(0x20), v13f9V1398
    0x160eS0x14a1S0x13f0S0x1398: v160eV14a1V13f0V1398(0x0) = CONST 

    Begin block 0x1610B0x14a1B0x13f0B0x1398
    prev=[0x15deB0x14a1B0x13f0B0x1398, 0x1619B0x14a1B0x13f0B0x1398], succ=[0x1628B0x14a1B0x13f0B0x1398, 0x1619B0x14a1B0x13f0B0x1398]
    =================================
    0x1610_0x0S0x14a1S0x13f0S0x1398: v1610_0V14a1V13f0V1398 = PHI v160eV14a1V13f0V1398(0x0), v1623V14a1V13f0V1398
    0x1613S0x14a1S0x13f0S0x1398: v1613V14a1V13f0V1398 = LT v1610_0V14a1V13f0V1398, v1605V14a1V13f0V1398(0x20)
    0x1614S0x14a1S0x13f0S0x1398: v1614V14a1V13f0V1398 = ISZERO v1613V14a1V13f0V1398
    0x1615S0x14a1S0x13f0S0x1398: v1615V14a1V13f0V1398(0x1628) = CONST 
    0x1618S0x14a1S0x13f0S0x1398: JUMPI v1615V14a1V13f0V1398(0x1628), v1614V14a1V13f0V1398

    Begin block 0x1628B0x14a1B0x13f0B0x1398
    prev=[0x1610B0x14a1B0x13f0B0x1398], succ=[0x1655B0x14a1B0x13f0B0x1398, 0x163cB0x14a1B0x13f0B0x1398]
    =================================
    0x1631S0x14a1S0x13f0S0x1398: v1631V14a1V13f0V1398 = ADD v1605V14a1V13f0V1398(0x20), v1601V14a1V13f0V1398
    0x1633S0x14a1S0x13f0S0x1398: v1633V14a1V13f0V1398(0x1f) = CONST 
    0x1635S0x14a1S0x13f0S0x1398: v1635V14a1V13f0V1398(0x0) = AND v1633V14a1V13f0V1398(0x1f), v1605V14a1V13f0V1398(0x20)
    0x1637S0x14a1S0x13f0S0x1398: v1637V14a1V13f0V1398 = ISZERO v1635V14a1V13f0V1398(0x0)
    0x1638S0x14a1S0x13f0S0x1398: v1638V14a1V13f0V1398(0x1655) = CONST 
    0x163bS0x14a1S0x13f0S0x1398: JUMPI v1638V14a1V13f0V1398(0x1655), v1637V14a1V13f0V1398

    Begin block 0x1655B0x14a1B0x13f0B0x1398
    prev=[0x1628B0x14a1B0x13f0B0x1398, 0x163cB0x14a1B0x13f0B0x1398], succ=[]
    =================================
    0x1655_0x1S0x14a1S0x13f0S0x1398: v1655_1V14a1V13f0V1398 = PHI v1631V14a1V13f0V1398, v1652V14a1V13f0V1398
    0x165bS0x14a1S0x13f0S0x1398: v165bV14a1V13f0V1398(0x40) = CONST 
    0x165dS0x14a1S0x13f0S0x1398: v165dV14a1V13f0V1398 = MLOAD v165bV14a1V13f0V1398(0x40)
    0x1660S0x14a1S0x13f0S0x1398: v1660V14a1V13f0V1398 = SUB v1655_1V14a1V13f0V1398, v165dV14a1V13f0V1398
    0x1662S0x14a1S0x13f0S0x1398: REVERT v165dV14a1V13f0V1398, v1660V14a1V13f0V1398

    Begin block 0x163cB0x14a1B0x13f0B0x1398
    prev=[0x1628B0x14a1B0x13f0B0x1398], succ=[0x1655B0x14a1B0x13f0B0x1398]
    =================================
    0x163eS0x14a1S0x13f0S0x1398: v163eV14a1V13f0V1398 = SUB v1631V14a1V13f0V1398, v1635V14a1V13f0V1398(0x0)
    0x1640S0x14a1S0x13f0S0x1398: v1640V14a1V13f0V1398 = MLOAD v163eV14a1V13f0V1398
    0x1641S0x14a1S0x13f0S0x1398: v1641V14a1V13f0V1398(0x1) = CONST 
    0x1644S0x14a1S0x13f0S0x1398: v1644V14a1V13f0V1398(0x20) = CONST 
    0x1646S0x14a1S0x13f0S0x1398: v1646V14a1V13f0V1398(0x20) = SUB v1644V14a1V13f0V1398(0x20), v1635V14a1V13f0V1398(0x0)
    0x1647S0x14a1S0x13f0S0x1398: v1647V14a1V13f0V1398(0x100) = CONST 
    0x164aS0x14a1S0x13f0S0x1398: v164aV14a1V13f0V1398(0x1) = EXP v1647V14a1V13f0V1398(0x100), v1646V14a1V13f0V1398(0x20)
    0x164bS0x14a1S0x13f0S0x1398: v164bV14a1V13f0V1398(0x0) = SUB v164aV14a1V13f0V1398(0x1), v1641V14a1V13f0V1398(0x1)
    0x164cS0x14a1S0x13f0S0x1398: v164cV14a1V13f0V1398 = NOT v164bV14a1V13f0V1398(0x0)
    0x164dS0x14a1S0x13f0S0x1398: v164dV14a1V13f0V1398 = AND v164cV14a1V13f0V1398, v1640V14a1V13f0V1398
    0x164fS0x14a1S0x13f0S0x1398: MSTORE v163eV14a1V13f0V1398, v164dV14a1V13f0V1398
    0x1650S0x14a1S0x13f0S0x1398: v1650V14a1V13f0V1398(0x20) = CONST 
    0x1652S0x14a1S0x13f0S0x1398: v1652V14a1V13f0V1398 = ADD v1650V14a1V13f0V1398(0x20), v163eV14a1V13f0V1398

    Begin block 0x1619B0x14a1B0x13f0B0x1398
    prev=[0x1610B0x14a1B0x13f0B0x1398], succ=[0x1610B0x14a1B0x13f0B0x1398]
    =================================
    0x1619_0x0S0x14a1S0x13f0S0x1398: v1619_0V14a1V13f0V1398 = PHI v160eV14a1V13f0V1398(0x0), v1623V14a1V13f0V1398
    0x161bS0x14a1S0x13f0S0x1398: v161bV14a1V13f0V1398 = ADD v1619_0V14a1V13f0V1398, v1609V14a1V13f0V1398
    0x161cS0x14a1S0x13f0S0x1398: v161cV14a1V13f0V1398 = MLOAD v161bV14a1V13f0V1398
    0x161fS0x14a1S0x13f0S0x1398: v161fV14a1V13f0V1398 = ADD v1619_0V14a1V13f0V1398, v1601V14a1V13f0V1398
    0x1620S0x14a1S0x13f0S0x1398: MSTORE v161fV14a1V13f0V1398, v161cV14a1V13f0V1398
    0x1621S0x14a1S0x13f0S0x1398: v1621V14a1V13f0V1398(0x20) = CONST 
    0x1623S0x14a1S0x13f0S0x1398: v1623V14a1V13f0V1398 = ADD v1621V14a1V13f0V1398(0x20), v1619_0V14a1V13f0V1398
    0x1624S0x14a1S0x13f0S0x1398: v1624V14a1V13f0V1398(0x1610) = CONST 
    0x1627S0x14a1S0x13f0S0x1398: JUMP v1624V14a1V13f0V1398(0x1610)

    Begin block 0x15d6B0x14a1B0x13f0B0x1398
    prev=[0x15ceB0x14a1B0x13f0B0x1398], succ=[]
    =================================
    0x15d6_0x0S0x14a1S0x13f0S0x1398: v15d6_0V14a1V13f0V1398 = PHI v1596V14a1V13f0V1398, v15b6V14a1V13f0V1398(0x60)
    0x15d7S0x14a1S0x13f0S0x1398: v15d7V14a1V13f0V1398 = MLOAD v15d6_0V14a1V13f0V1398
    0x15daS0x14a1S0x13f0S0x1398: v15daV14a1V13f0V1398(0x20) = CONST 
    0x15dcS0x14a1S0x13f0S0x1398: v15dcV14a1V13f0V1398 = ADD v15daV14a1V13f0V1398(0x20), v15d6_0V14a1V13f0V1398
    0x15ddS0x14a1S0x13f0S0x1398: REVERT v15dcV14a1V13f0V1398, v15d7V14a1V13f0V1398

    Begin block 0x15c6B0x14a1B0x13f0B0x1398
    prev=[0x15baB0x14a1B0x13f0B0x1398], succ=[0x1dfcB0x14a1B0x13f0B0x1398]
    =================================
    0x15c8S0x14a1S0x13f0S0x1398: v15c8V14a1V13f0V1398(0x1dfc) = CONST 
    0x15cdS0x14a1S0x13f0S0x1398: JUMP v15c8V14a1V13f0V1398(0x1dfc)

    Begin block 0x1dfcB0x14a1B0x13f0B0x1398
    prev=[0x15c6B0x14a1B0x13f0B0x1398], succ=[0x1dd5B0x13f0B0x1398]
    =================================
    0x1dfc_0x0S0x14a1S0x13f0S0x1398: v1dfc_0V14a1V13f0V1398 = PHI v1596V14a1V13f0V1398, v15b6V14a1V13f0V1398(0x60)
    0x1e03S0x14a1S0x13f0S0x1398: JUMP v14a4V13f0V1398(0x1dd5)

    Begin block 0x1dd5B0x13f0B0x1398
    prev=[0x1dfcB0x14a1B0x13f0B0x1398], succ=[0x1445B0x1398]
    =================================
    0x1ddcS0x13f0S0x1398: JUMP v13f3V1398(0x1445)

    Begin block 0x1445B0x1398
    prev=[0x1dd5B0x13f0B0x1398], succ=[0x1450B0x1398, 0x1d8dB0x1398]
    =================================
    0x1447S0x1398: v1447V1398 = MLOAD v1dfc_0V14a1V13f0V1398
    0x144bS0x1398: v144bV1398 = ISZERO v1447V1398
    0x144cS0x1398: v144cV1398(0x1d8d) = CONST 
    0x144fS0x1398: JUMPI v144cV1398(0x1d8d), v144bV1398

    Begin block 0x1450B0x1398
    prev=[0x1445B0x1398], succ=[0x1460B0x1398, 0x1464B0x1398]
    =================================
    0x1452S0x1398: v1452V1398(0x20) = CONST 
    0x1454S0x1398: v1454V1398 = ADD v1452V1398(0x20), v1dfc_0V14a1V13f0V1398
    0x1456S0x1398: v1456V1398 = MLOAD v1dfc_0V14a1V13f0V1398
    0x1457S0x1398: v1457V1398(0x20) = CONST 
    0x145aS0x1398: v145aV1398 = LT v1456V1398, v1457V1398(0x20)
    0x145bS0x1398: v145bV1398 = ISZERO v145aV1398
    0x145cS0x1398: v145cV1398(0x1464) = CONST 
    0x145fS0x1398: JUMPI v145cV1398(0x1464), v145bV1398

    Begin block 0x1460B0x1398
    prev=[0x1450B0x1398], succ=[]
    =================================
    0x1460S0x1398: v1460V1398(0x0) = CONST 
    0x1463S0x1398: REVERT v1460V1398(0x0), v1460V1398(0x0)

    Begin block 0x1464B0x1398
    prev=[0x1450B0x1398], succ=[0x146bB0x1398, 0x1db1B0x1398]
    =================================
    0x1466S0x1398: v1466V1398 = MLOAD v1454V1398
    0x1467S0x1398: v1467V1398(0x1db1) = CONST 
    0x146aS0x1398: JUMPI v1467V1398(0x1db1), v1466V1398

    Begin block 0x146bB0x1398
    prev=[0x1464B0x1398], succ=[]
    =================================
    0x146bS0x1398: v146bV1398(0x40) = CONST 
    0x146dS0x1398: v146dV1398 = MLOAD v146bV1398(0x40)
    0x146eS0x1398: v146eV1398(0x461bcd) = CONST 
    0x1472S0x1398: v1472V1398(0xe5) = CONST 
    0x1474S0x1398: v1474V1398(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1472V1398(0xe5), v146eV1398(0x461bcd)
    0x1476S0x1398: MSTORE v146dV1398, v1474V1398(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1477S0x1398: v1477V1398(0x4) = CONST 
    0x1479S0x1398: v1479V1398 = ADD v1477V1398(0x4), v146dV1398
    0x147cS0x1398: v147cV1398(0x20) = CONST 
    0x147eS0x1398: v147eV1398 = ADD v147cV1398(0x20), v1479V1398
    0x1481S0x1398: v1481V1398(0x20) = SUB v147eV1398, v1479V1398
    0x1483S0x1398: MSTORE v1479V1398, v1481V1398(0x20)
    0x1484S0x1398: v1484V1398(0x2a) = CONST 
    0x1487S0x1398: MSTORE v147eV1398, v1484V1398(0x2a)
    0x1488S0x1398: v1488V1398(0x20) = CONST 
    0x148aS0x1398: v148aV1398 = ADD v1488V1398(0x20), v147eV1398
    0x148cS0x1398: v148cV1398(0x1698) = CONST 
    0x148fS0x1398: v148fV1398(0x2a) = CONST 
    0x1492S0x1398: CODECOPY v148aV1398, v148cV1398(0x1698), v148fV1398(0x2a)
    0x1493S0x1398: v1493V1398(0x40) = CONST 
    0x1495S0x1398: v1495V1398 = ADD v1493V1398(0x40), v148aV1398
    0x1499S0x1398: v1499V1398(0x40) = CONST 
    0x149bS0x1398: v149bV1398 = MLOAD v1499V1398(0x40)
    0x149eS0x1398: v149eV1398(0x84) = SUB v1495V1398, v149bV1398
    0x14a0S0x1398: REVERT v149bV1398, v149eV1398(0x84)

    Begin block 0x1db1B0x1398
    prev=[0x1464B0x1398], succ=[0x1d69]
    =================================
    0x1db5S0x1398: JUMP v13e0(0x1d69)

    Begin block 0x1d69
    prev=[0x1d8dB0x1398, 0x1db1B0x1398], succ=[]
    =================================
    0x1d6d: RETURNPRIVATE v1398arg3

    Begin block 0x1d8dB0x1398
    prev=[0x1445B0x1398], succ=[0x1d69]
    =================================
    0x1d91S0x1398: JUMP v13e0(0x1d69)

    Begin block 0x15b5B0x14a1B0x13f0B0x1398
    prev=[0x1553B0x14a1B0x13f0B0x1398], succ=[0x15baB0x14a1B0x13f0B0x1398]
    =================================
    0x15b6S0x14a1S0x13f0S0x1398: v15b6V14a1V13f0V1398(0x60) = CONST 

    Begin block 0x153dB0x14a1B0x13f0B0x1398
    prev=[0x1534B0x14a1B0x13f0B0x1398], succ=[0x1534B0x14a1B0x13f0B0x1398]
    =================================
    0x153d_0x0S0x14a1S0x13f0S0x1398: v153d_0V14a1V13f0V1398 = PHI v152fV14a1V13f0V1398, v154eV14a1V13f0V1398
    0x153d_0x1S0x14a1S0x13f0S0x1398: v153d_1V14a1V13f0V1398 = PHI v1527V14a1V13f0V1398, v154cV14a1V13f0V1398
    0x153d_0x2S0x14a1S0x13f0S0x1398: v153d_2V14a1V13f0V1398 = PHI v152bV14a1V13f0V1398(0x44), v1546V14a1V13f0V1398
    0x153eS0x14a1S0x13f0S0x1398: v153eV14a1V13f0V1398 = MLOAD v153d_0V14a1V13f0V1398
    0x1540S0x14a1S0x13f0S0x1398: MSTORE v153d_1V14a1V13f0V1398, v153eV14a1V13f0V1398
    0x1541S0x14a1S0x13f0S0x1398: v1541V14a1V13f0V1398(0x1f) = CONST 
    0x1543S0x14a1S0x13f0S0x1398: v1543V14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1541V14a1V13f0V1398(0x1f)
    0x1546S0x14a1S0x13f0S0x1398: v1546V14a1V13f0V1398 = ADD v153d_2V14a1V13f0V1398, v1543V14a1V13f0V1398(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x1548S0x14a1S0x13f0S0x1398: v1548V14a1V13f0V1398(0x20) = CONST 
    0x154cS0x14a1S0x13f0S0x1398: v154cV14a1V13f0V1398 = ADD v1548V14a1V13f0V1398(0x20), v153d_1V14a1V13f0V1398
    0x154eS0x14a1S0x13f0S0x1398: v154eV14a1V13f0V1398 = ADD v1548V14a1V13f0V1398(0x20), v153d_0V14a1V13f0V1398
    0x154fS0x14a1S0x13f0S0x1398: v154fV14a1V13f0V1398(0x1534) = CONST 
    0x1552S0x14a1S0x13f0S0x1398: JUMP v154fV14a1V13f0V1398(0x1534)

}

function fallback()() public {
    Begin block 0x1716
    prev=[], succ=[]
    =================================
    0x1717: v1717(0x0) = CONST 
    0x171a: REVERT v1717(0x0), v1717(0x0)

}

function inCaseStrategyTokenGetStuck(address,address)() public {
    Begin block 0x1df
    prev=[], succ=[0x1f1, 0x1f5]
    =================================
    0x1e0: v1e0(0x1836) = CONST 
    0x1e3: v1e3(0x4) = CONST 
    0x1e6: v1e6 = CALLDATASIZE 
    0x1e7: v1e7 = SUB v1e6, v1e3(0x4)
    0x1e8: v1e8(0x40) = CONST 
    0x1eb: v1eb = LT v1e7, v1e8(0x40)
    0x1ec: v1ec = ISZERO v1eb
    0x1ed: v1ed(0x1f5) = CONST 
    0x1f0: JUMPI v1ed(0x1f5), v1ec

    Begin block 0x1f1
    prev=[0x1df], succ=[]
    =================================
    0x1f1: v1f1(0x0) = CONST 
    0x1f4: REVERT v1f1(0x0), v1f1(0x0)

    Begin block 0x1f5
    prev=[0x1df], succ=[0x640]
    =================================
    0x1f7: v1f7(0x1) = CONST 
    0x1f9: v1f9(0x1) = CONST 
    0x1fb: v1fb(0xa0) = CONST 
    0x1fd: v1fd(0x10000000000000000000000000000000000000000) = SHL v1fb(0xa0), v1f9(0x1)
    0x1fe: v1fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fd(0x10000000000000000000000000000000000000000), v1f7(0x1)
    0x200: v200 = CALLDATALOAD v1e3(0x4)
    0x202: v202 = AND v1fe(0xffffffffffffffffffffffffffffffffffffffff), v200
    0x204: v204(0x20) = CONST 
    0x206: v206(0x24) = ADD v204(0x20), v1e3(0x4)
    0x207: v207 = CALLDATALOAD v206(0x24)
    0x208: v208 = AND v207, v1fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x209: v209(0x640) = CONST 
    0x20c: JUMP v209(0x640)

    Begin block 0x640
    prev=[0x1f5], succ=[0x648]
    =================================
    0x641: v641(0x648) = CONST 
    0x644: v644(0x1222) = CONST 
    0x647: CALLPRIVATE v644(0x1222), v641(0x648)

    Begin block 0x648
    prev=[0x640], succ=[0x693, 0x697]
    =================================
    0x64a: v64a(0x1) = CONST 
    0x64c: v64c(0x1) = CONST 
    0x64e: v64e(0xa0) = CONST 
    0x650: v650(0x10000000000000000000000000000000000000000) = SHL v64e(0xa0), v64c(0x1)
    0x651: v651(0xffffffffffffffffffffffffffffffffffffffff) = SUB v650(0x10000000000000000000000000000000000000000), v64a(0x1)
    0x652: v652 = AND v651(0xffffffffffffffffffffffffffffffffffffffff), v202
    0x653: v653(0x1bd43be3) = CONST 
    0x659: v659(0x40) = CONST 
    0x65b: v65b = MLOAD v659(0x40)
    0x65d: v65d(0xffffffff) = CONST 
    0x662: v662(0x1bd43be3) = AND v65d(0xffffffff), v653(0x1bd43be3)
    0x663: v663(0xe0) = CONST 
    0x665: v665(0x1bd43be300000000000000000000000000000000000000000000000000000000) = SHL v663(0xe0), v662(0x1bd43be3)
    0x667: MSTORE v65b, v665(0x1bd43be300000000000000000000000000000000000000000000000000000000)
    0x668: v668(0x4) = CONST 
    0x66a: v66a = ADD v668(0x4), v65b
    0x66d: v66d(0x1) = CONST 
    0x66f: v66f(0x1) = CONST 
    0x671: v671(0xa0) = CONST 
    0x673: v673(0x10000000000000000000000000000000000000000) = SHL v671(0xa0), v66f(0x1)
    0x674: v674(0xffffffffffffffffffffffffffffffffffffffff) = SUB v673(0x10000000000000000000000000000000000000000), v66d(0x1)
    0x675: v675 = AND v674(0xffffffffffffffffffffffffffffffffffffffff), v208
    0x677: MSTORE v66a, v675
    0x678: v678(0x20) = CONST 
    0x67a: v67a = ADD v678(0x20), v66a
    0x67e: v67e(0x20) = CONST 
    0x680: v680(0x40) = CONST 
    0x682: v682 = MLOAD v680(0x40)
    0x685: v685(0x24) = SUB v67a, v682
    0x687: v687(0x0) = CONST 
    0x68b: v68b = EXTCODESIZE v652
    0x68c: v68c = ISZERO v68b
    0x68e: v68e = ISZERO v68c
    0x68f: v68f(0x697) = CONST 
    0x692: JUMPI v68f(0x697), v68e

    Begin block 0x693
    prev=[0x648], succ=[]
    =================================
    0x693: v693(0x0) = CONST 
    0x696: REVERT v693(0x0), v693(0x0)

    Begin block 0x697
    prev=[0x648], succ=[0x6a2, 0x6ab]
    =================================
    0x699: v699 = GAS 
    0x69a: v69a = CALL v699, v652, v687(0x0), v682, v685(0x24), v682, v67e(0x20)
    0x69b: v69b = ISZERO v69a
    0x69d: v69d = ISZERO v69b
    0x69e: v69e(0x6ab) = CONST 
    0x6a1: JUMPI v69e(0x6ab), v69d

    Begin block 0x6a2
    prev=[0x697], succ=[]
    =================================
    0x6a2: v6a2 = RETURNDATASIZE 
    0x6a3: v6a3(0x0) = CONST 
    0x6a6: RETURNDATACOPY v6a3(0x0), v6a3(0x0), v6a2
    0x6a7: v6a7 = RETURNDATASIZE 
    0x6a8: v6a8(0x0) = CONST 
    0x6aa: REVERT v6a8(0x0), v6a7

    Begin block 0x6ab
    prev=[0x697], succ=[0x6bd, 0x6c1]
    =================================
    0x6b0: v6b0(0x40) = CONST 
    0x6b2: v6b2 = MLOAD v6b0(0x40)
    0x6b3: v6b3 = RETURNDATASIZE 
    0x6b4: v6b4(0x20) = CONST 
    0x6b7: v6b7 = LT v6b3, v6b4(0x20)
    0x6b8: v6b8 = ISZERO v6b7
    0x6b9: v6b9(0x6c1) = CONST 
    0x6bc: JUMPI v6b9(0x6c1), v6b8

    Begin block 0x6bd
    prev=[0x6ab], succ=[]
    =================================
    0x6bd: v6bd(0x0) = CONST 
    0x6c0: REVERT v6bd(0x0), v6bd(0x0)

    Begin block 0x6c1
    prev=[0x6ab], succ=[0x1836]
    =================================
    0x6c6: JUMP v1e0(0x1836)

    Begin block 0x1836
    prev=[0x6c1], succ=[]
    =================================
    0x1837: STOP 

}

function strategist()() public {
    Begin block 0x20f
    prev=[], succ=[0x6c7]
    =================================
    0x210: v210(0x1857) = CONST 
    0x213: v213(0x6c7) = CONST 
    0x216: JUMP v213(0x6c7)

    Begin block 0x6c7
    prev=[0x20f], succ=[0x1857]
    =================================
    0x6c8: v6c8(0x1) = CONST 
    0x6ca: v6ca = SLOAD v6c8(0x1)
    0x6cb: v6cb(0x1) = CONST 
    0x6cd: v6cd(0x1) = CONST 
    0x6cf: v6cf(0xa0) = CONST 
    0x6d1: v6d1(0x10000000000000000000000000000000000000000) = SHL v6cf(0xa0), v6cd(0x1)
    0x6d2: v6d2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6d1(0x10000000000000000000000000000000000000000), v6cb(0x1)
    0x6d3: v6d3 = AND v6d2(0xffffffffffffffffffffffffffffffffffffffff), v6ca
    0x6d5: JUMP v210(0x1857)

    Begin block 0x1857
    prev=[0x6c7], succ=[]
    =================================
    0x1858: v1858(0x40) = CONST 
    0x185b: v185b = MLOAD v1858(0x40)
    0x185c: v185c(0x1) = CONST 
    0x185e: v185e(0x1) = CONST 
    0x1860: v1860(0xa0) = CONST 
    0x1862: v1862(0x10000000000000000000000000000000000000000) = SHL v1860(0xa0), v185e(0x1)
    0x1863: v1863(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1862(0x10000000000000000000000000000000000000000), v185c(0x1)
    0x1866: v1866 = AND v6d3, v1863(0xffffffffffffffffffffffffffffffffffffffff)
    0x1868: MSTORE v185b, v1866
    0x1869: v1869 = MLOAD v1858(0x40)
    0x186d: v186d(0x0) = SUB v185b, v1869
    0x186e: v186e(0x20) = CONST 
    0x1870: v1870(0x20) = ADD v186e(0x20), v186d(0x0)
    0x1872: RETURN v1869, v1870(0x20)

}

function strategies(address)() public {
    Begin block 0x233
    prev=[], succ=[0x245, 0x249]
    =================================
    0x234: v234(0x1892) = CONST 
    0x237: v237(0x4) = CONST 
    0x23a: v23a = CALLDATASIZE 
    0x23b: v23b = SUB v23a, v237(0x4)
    0x23c: v23c(0x20) = CONST 
    0x23f: v23f = LT v23b, v23c(0x20)
    0x240: v240 = ISZERO v23f
    0x241: v241(0x249) = CONST 
    0x244: JUMPI v241(0x249), v240

    Begin block 0x245
    prev=[0x233], succ=[]
    =================================
    0x245: v245(0x0) = CONST 
    0x248: REVERT v245(0x0), v245(0x0)

    Begin block 0x249
    prev=[0x233], succ=[0x6d6]
    =================================
    0x24b: v24b = CALLDATALOAD v237(0x4)
    0x24c: v24c(0x1) = CONST 
    0x24e: v24e(0x1) = CONST 
    0x250: v250(0xa0) = CONST 
    0x252: v252(0x10000000000000000000000000000000000000000) = SHL v250(0xa0), v24e(0x1)
    0x253: v253(0xffffffffffffffffffffffffffffffffffffffff) = SUB v252(0x10000000000000000000000000000000000000000), v24c(0x1)
    0x254: v254 = AND v253(0xffffffffffffffffffffffffffffffffffffffff), v24b
    0x255: v255(0x6d6) = CONST 
    0x258: JUMP v255(0x6d6)

    Begin block 0x6d6
    prev=[0x249], succ=[0x1892]
    =================================
    0x6d7: v6d7(0x38) = CONST 
    0x6d9: v6d9(0x20) = CONST 
    0x6db: MSTORE v6d9(0x20), v6d7(0x38)
    0x6dc: v6dc(0x0) = CONST 
    0x6e0: MSTORE v6dc(0x0), v254
    0x6e1: v6e1(0x40) = CONST 
    0x6e4: v6e4 = SHA3 v6dc(0x0), v6e1(0x40)
    0x6e5: v6e5 = SLOAD v6e4
    0x6e6: v6e6(0x1) = CONST 
    0x6e8: v6e8(0x1) = CONST 
    0x6ea: v6ea(0xa0) = CONST 
    0x6ec: v6ec(0x10000000000000000000000000000000000000000) = SHL v6ea(0xa0), v6e8(0x1)
    0x6ed: v6ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ec(0x10000000000000000000000000000000000000000), v6e6(0x1)
    0x6ee: v6ee = AND v6ed(0xffffffffffffffffffffffffffffffffffffffff), v6e5
    0x6f0: JUMP v234(0x1892)

    Begin block 0x1892
    prev=[0x6d6], succ=[]
    =================================
    0x1893: v1893(0x40) = CONST 
    0x1896: v1896 = MLOAD v1893(0x40)
    0x1897: v1897(0x1) = CONST 
    0x1899: v1899(0x1) = CONST 
    0x189b: v189b(0xa0) = CONST 
    0x189d: v189d(0x10000000000000000000000000000000000000000) = SHL v189b(0xa0), v1899(0x1)
    0x189e: v189e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v189d(0x10000000000000000000000000000000000000000), v1897(0x1)
    0x18a1: v18a1 = AND v6ee, v189e(0xffffffffffffffffffffffffffffffffffffffff)
    0x18a3: MSTORE v1896, v18a1
    0x18a4: v18a4 = MLOAD v1893(0x40)
    0x18a8: v18a8(0x0) = SUB v1896, v18a4
    0x18a9: v18a9(0x20) = CONST 
    0x18ab: v18ab(0x20) = ADD v18a9(0x20), v18a8(0x0)
    0x18ad: RETURN v18a4, v18ab(0x20)

}

function revokeStrategy(address,address)() public {
    Begin block 0x259
    prev=[], succ=[0x26b, 0x26f]
    =================================
    0x25a: v25a(0x18cd) = CONST 
    0x25d: v25d(0x4) = CONST 
    0x260: v260 = CALLDATASIZE 
    0x261: v261 = SUB v260, v25d(0x4)
    0x262: v262(0x40) = CONST 
    0x265: v265 = LT v261, v262(0x40)
    0x266: v266 = ISZERO v265
    0x267: v267(0x26f) = CONST 
    0x26a: JUMPI v267(0x26f), v266

    Begin block 0x26b
    prev=[0x259], succ=[]
    =================================
    0x26b: v26b(0x0) = CONST 
    0x26e: REVERT v26b(0x0), v26b(0x0)

    Begin block 0x26f
    prev=[0x259], succ=[0x6f1]
    =================================
    0x271: v271(0x1) = CONST 
    0x273: v273(0x1) = CONST 
    0x275: v275(0xa0) = CONST 
    0x277: v277(0x10000000000000000000000000000000000000000) = SHL v275(0xa0), v273(0x1)
    0x278: v278(0xffffffffffffffffffffffffffffffffffffffff) = SUB v277(0x10000000000000000000000000000000000000000), v271(0x1)
    0x27a: v27a = CALLDATALOAD v25d(0x4)
    0x27c: v27c = AND v278(0xffffffffffffffffffffffffffffffffffffffff), v27a
    0x27e: v27e(0x20) = CONST 
    0x280: v280(0x24) = ADD v27e(0x20), v25d(0x4)
    0x281: v281 = CALLDATALOAD v280(0x24)
    0x282: v282 = AND v281, v278(0xffffffffffffffffffffffffffffffffffffffff)
    0x283: v283(0x6f1) = CONST 
    0x286: JUMP v283(0x6f1)

    Begin block 0x6f1
    prev=[0x26f], succ=[0x129eB0x6f1]
    =================================
    0x6f2: v6f2(0x6f9) = CONST 
    0x6f5: v6f5(0x129e) = CONST 
    0x6f8: JUMP v6f5(0x129e), v6f2(0x6f9)

    Begin block 0x129eB0x6f1
    prev=[0x6f1], succ=[0x12b7B0x6f1, 0x1d48B0x6f1]
    =================================
    0x129fS0x6f1: v129fV6f1(0x0) = CONST 
    0x12a1S0x6f1: v12a1V6f1 = SLOAD v129fV6f1(0x0)
    0x12a2S0x6f1: v12a2V6f1(0x10000) = CONST 
    0x12a7S0x6f1: v12a7V6f1 = DIV v12a1V6f1, v12a2V6f1(0x10000)
    0x12a8S0x6f1: v12a8V6f1(0x1) = CONST 
    0x12aaS0x6f1: v12aaV6f1(0x1) = CONST 
    0x12acS0x6f1: v12acV6f1(0xa0) = CONST 
    0x12aeS0x6f1: v12aeV6f1(0x10000000000000000000000000000000000000000) = SHL v12acV6f1(0xa0), v12aaV6f1(0x1)
    0x12afS0x6f1: v12afV6f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeV6f1(0x10000000000000000000000000000000000000000), v12a8V6f1(0x1)
    0x12b0S0x6f1: v12b0V6f1 = AND v12afV6f1(0xffffffffffffffffffffffffffffffffffffffff), v12a7V6f1
    0x12b1S0x6f1: v12b1V6f1 = CALLER 
    0x12b2S0x6f1: v12b2V6f1 = EQ v12b1V6f1, v12b0V6f1
    0x12b3S0x6f1: v12b3V6f1(0x1d48) = CONST 
    0x12b6S0x6f1: JUMPI v12b3V6f1(0x1d48), v12b2V6f1

    Begin block 0x12b7B0x6f1
    prev=[0x129eB0x6f1], succ=[]
    =================================
    0x12b7S0x6f1: v12b7V6f1(0x40) = CONST 
    0x12baS0x6f1: v12baV6f1 = MLOAD v12b7V6f1(0x40)
    0x12bbS0x6f1: v12bbV6f1(0x461bcd) = CONST 
    0x12bfS0x6f1: v12bfV6f1(0xe5) = CONST 
    0x12c1S0x6f1: v12c1V6f1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfV6f1(0xe5), v12bbV6f1(0x461bcd)
    0x12c3S0x6f1: MSTORE v12baV6f1, v12c1V6f1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0x6f1: v12c4V6f1(0x20) = CONST 
    0x12c6S0x6f1: v12c6V6f1(0x4) = CONST 
    0x12c9S0x6f1: v12c9V6f1 = ADD v12baV6f1, v12c6V6f1(0x4)
    0x12caS0x6f1: MSTORE v12c9V6f1, v12c4V6f1(0x20)
    0x12cbS0x6f1: v12cbV6f1(0xe) = CONST 
    0x12cdS0x6f1: v12cdV6f1(0x24) = CONST 
    0x12d0S0x6f1: v12d0V6f1 = ADD v12baV6f1, v12cdV6f1(0x24)
    0x12d1S0x6f1: MSTORE v12d0V6f1, v12cbV6f1(0xe)
    0x12d2S0x6f1: v12d2V6f1(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0x6f1: v12e1V6f1(0x90) = CONST 
    0x12e3S0x6f1: v12e3V6f1(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1V6f1(0x90), v12d2V6f1(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0x6f1: v12e4V6f1(0x44) = CONST 
    0x12e7S0x6f1: v12e7V6f1 = ADD v12baV6f1, v12e4V6f1(0x44)
    0x12e8S0x6f1: MSTORE v12e7V6f1, v12e3V6f1(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0x6f1: v12eaV6f1 = MLOAD v12b7V6f1(0x40)
    0x12eeS0x6f1: v12eeV6f1(0x0) = SUB v12baV6f1, v12eaV6f1
    0x12efS0x6f1: v12efV6f1(0x64) = CONST 
    0x12f1S0x6f1: v12f1V6f1(0x64) = ADD v12efV6f1(0x64), v12eeV6f1(0x0)
    0x12f3S0x6f1: REVERT v12eaV6f1, v12f1V6f1(0x64)

    Begin block 0x1d48B0x6f1
    prev=[0x129eB0x6f1], succ=[0x6f9]
    =================================
    0x1d49S0x6f1: JUMP v6f2(0x6f9)

    Begin block 0x6f9
    prev=[0x1d48B0x6f1], succ=[0x18cd]
    =================================
    0x6fa: v6fa(0x1) = CONST 
    0x6fc: v6fc(0x1) = CONST 
    0x6fe: v6fe(0xa0) = CONST 
    0x700: v700(0x10000000000000000000000000000000000000000) = SHL v6fe(0xa0), v6fc(0x1)
    0x701: v701(0xffffffffffffffffffffffffffffffffffffffff) = SUB v700(0x10000000000000000000000000000000000000000), v6fa(0x1)
    0x704: v704 = AND v701(0xffffffffffffffffffffffffffffffffffffffff), v27c
    0x705: v705(0x0) = CONST 
    0x709: MSTORE v705(0x0), v704
    0x70a: v70a(0x3a) = CONST 
    0x70c: v70c(0x20) = CONST 
    0x710: MSTORE v70c(0x20), v70a(0x3a)
    0x711: v711(0x40) = CONST 
    0x715: v715 = SHA3 v705(0x0), v711(0x40)
    0x719: v719 = AND v701(0xffffffffffffffffffffffffffffffffffffffff), v282
    0x71b: MSTORE v705(0x0), v719
    0x71f: MSTORE v70c(0x20), v715
    0x720: v720 = SHA3 v705(0x0), v711(0x40)
    0x722: v722 = SLOAD v720
    0x723: v723(0xff) = CONST 
    0x725: v725(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v723(0xff)
    0x726: v726 = AND v725(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v722
    0x728: SSTORE v720, v726
    0x729: JUMP v25a(0x18cd)

    Begin block 0x18cd
    prev=[0x6f9], succ=[]
    =================================
    0x18ce: STOP 

}

function governance()() public {
    Begin block 0x287
    prev=[], succ=[0x72a]
    =================================
    0x288: v288(0x18ee) = CONST 
    0x28b: v28b(0x72a) = CONST 
    0x28e: JUMP v28b(0x72a)

    Begin block 0x72a
    prev=[0x287], succ=[0x18ee]
    =================================
    0x72b: v72b(0x0) = CONST 
    0x72d: v72d = SLOAD v72b(0x0)
    0x72e: v72e(0x10000) = CONST 
    0x733: v733 = DIV v72d, v72e(0x10000)
    0x734: v734(0x1) = CONST 
    0x736: v736(0x1) = CONST 
    0x738: v738(0xa0) = CONST 
    0x73a: v73a(0x10000000000000000000000000000000000000000) = SHL v738(0xa0), v736(0x1)
    0x73b: v73b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v73a(0x10000000000000000000000000000000000000000), v734(0x1)
    0x73c: v73c = AND v73b(0xffffffffffffffffffffffffffffffffffffffff), v733
    0x73e: JUMP v288(0x18ee)

    Begin block 0x18ee
    prev=[0x72a], succ=[]
    =================================
    0x18ef: v18ef(0x40) = CONST 
    0x18f2: v18f2 = MLOAD v18ef(0x40)
    0x18f3: v18f3(0x1) = CONST 
    0x18f5: v18f5(0x1) = CONST 
    0x18f7: v18f7(0xa0) = CONST 
    0x18f9: v18f9(0x10000000000000000000000000000000000000000) = SHL v18f7(0xa0), v18f5(0x1)
    0x18fa: v18fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18f9(0x10000000000000000000000000000000000000000), v18f3(0x1)
    0x18fd: v18fd = AND v73c, v18fa(0xffffffffffffffffffffffffffffffffffffffff)
    0x18ff: MSTORE v18f2, v18fd
    0x1900: v1900 = MLOAD v18ef(0x40)
    0x1904: v1904(0x0) = SUB v18f2, v1900
    0x1905: v1905(0x20) = CONST 
    0x1907: v1907(0x20) = ADD v1905(0x20), v1904(0x0)
    0x1909: RETURN v1900, v1907(0x20)

}

function setSplit(uint256)() public {
    Begin block 0x28f
    prev=[], succ=[0x2a1, 0x2a5]
    =================================
    0x290: v290(0x1929) = CONST 
    0x293: v293(0x4) = CONST 
    0x296: v296 = CALLDATASIZE 
    0x297: v297 = SUB v296, v293(0x4)
    0x298: v298(0x20) = CONST 
    0x29b: v29b = LT v297, v298(0x20)
    0x29c: v29c = ISZERO v29b
    0x29d: v29d(0x2a5) = CONST 
    0x2a0: JUMPI v29d(0x2a5), v29c

    Begin block 0x2a1
    prev=[0x28f], succ=[]
    =================================
    0x2a1: v2a1(0x0) = CONST 
    0x2a4: REVERT v2a1(0x0), v2a1(0x0)

    Begin block 0x2a5
    prev=[0x28f], succ=[0x73f]
    =================================
    0x2a7: v2a7 = CALLDATALOAD v293(0x4)
    0x2a8: v2a8(0x73f) = CONST 
    0x2ab: JUMP v2a8(0x73f)

    Begin block 0x73f
    prev=[0x2a5], succ=[0x129eB0x73f]
    =================================
    0x740: v740(0x747) = CONST 
    0x743: v743(0x129e) = CONST 
    0x746: JUMP v743(0x129e), v740(0x747)

    Begin block 0x129eB0x73f
    prev=[0x73f], succ=[0x12b7B0x73f, 0x1d48B0x73f]
    =================================
    0x129fS0x73f: v129fV73f(0x0) = CONST 
    0x12a1S0x73f: v12a1V73f = SLOAD v129fV73f(0x0)
    0x12a2S0x73f: v12a2V73f(0x10000) = CONST 
    0x12a7S0x73f: v12a7V73f = DIV v12a1V73f, v12a2V73f(0x10000)
    0x12a8S0x73f: v12a8V73f(0x1) = CONST 
    0x12aaS0x73f: v12aaV73f(0x1) = CONST 
    0x12acS0x73f: v12acV73f(0xa0) = CONST 
    0x12aeS0x73f: v12aeV73f(0x10000000000000000000000000000000000000000) = SHL v12acV73f(0xa0), v12aaV73f(0x1)
    0x12afS0x73f: v12afV73f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeV73f(0x10000000000000000000000000000000000000000), v12a8V73f(0x1)
    0x12b0S0x73f: v12b0V73f = AND v12afV73f(0xffffffffffffffffffffffffffffffffffffffff), v12a7V73f
    0x12b1S0x73f: v12b1V73f = CALLER 
    0x12b2S0x73f: v12b2V73f = EQ v12b1V73f, v12b0V73f
    0x12b3S0x73f: v12b3V73f(0x1d48) = CONST 
    0x12b6S0x73f: JUMPI v12b3V73f(0x1d48), v12b2V73f

    Begin block 0x12b7B0x73f
    prev=[0x129eB0x73f], succ=[]
    =================================
    0x12b7S0x73f: v12b7V73f(0x40) = CONST 
    0x12baS0x73f: v12baV73f = MLOAD v12b7V73f(0x40)
    0x12bbS0x73f: v12bbV73f(0x461bcd) = CONST 
    0x12bfS0x73f: v12bfV73f(0xe5) = CONST 
    0x12c1S0x73f: v12c1V73f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfV73f(0xe5), v12bbV73f(0x461bcd)
    0x12c3S0x73f: MSTORE v12baV73f, v12c1V73f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0x73f: v12c4V73f(0x20) = CONST 
    0x12c6S0x73f: v12c6V73f(0x4) = CONST 
    0x12c9S0x73f: v12c9V73f = ADD v12baV73f, v12c6V73f(0x4)
    0x12caS0x73f: MSTORE v12c9V73f, v12c4V73f(0x20)
    0x12cbS0x73f: v12cbV73f(0xe) = CONST 
    0x12cdS0x73f: v12cdV73f(0x24) = CONST 
    0x12d0S0x73f: v12d0V73f = ADD v12baV73f, v12cdV73f(0x24)
    0x12d1S0x73f: MSTORE v12d0V73f, v12cbV73f(0xe)
    0x12d2S0x73f: v12d2V73f(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0x73f: v12e1V73f(0x90) = CONST 
    0x12e3S0x73f: v12e3V73f(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1V73f(0x90), v12d2V73f(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0x73f: v12e4V73f(0x44) = CONST 
    0x12e7S0x73f: v12e7V73f = ADD v12baV73f, v12e4V73f(0x44)
    0x12e8S0x73f: MSTORE v12e7V73f, v12e3V73f(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0x73f: v12eaV73f = MLOAD v12b7V73f(0x40)
    0x12eeS0x73f: v12eeV73f(0x0) = SUB v12baV73f, v12eaV73f
    0x12efS0x73f: v12efV73f(0x64) = CONST 
    0x12f1S0x73f: v12f1V73f(0x64) = ADD v12efV73f(0x64), v12eeV73f(0x0)
    0x12f3S0x73f: REVERT v12eaV73f, v12f1V73f(0x64)

    Begin block 0x1d48B0x73f
    prev=[0x129eB0x73f], succ=[0x747]
    =================================
    0x1d49S0x73f: JUMP v740(0x747)

    Begin block 0x747
    prev=[0x1d48B0x73f], succ=[0x1929]
    =================================
    0x748: v748(0x3b) = CONST 
    0x74a: SSTORE v748(0x3b), v2a7
    0x74b: JUMP v290(0x1929)

    Begin block 0x1929
    prev=[0x747], succ=[]
    =================================
    0x192a: STOP 

}

function max()() public {
    Begin block 0x2ac
    prev=[], succ=[0x74c]
    =================================
    0x2ad: v2ad(0x194a) = CONST 
    0x2b0: v2b0(0x74c) = CONST 
    0x2b3: JUMP v2b0(0x74c)

    Begin block 0x74c
    prev=[0x2ac], succ=[0x194a]
    =================================
    0x74d: v74d(0x2710) = CONST 
    0x751: JUMP v2ad(0x194a)

    Begin block 0x194a
    prev=[0x74c], succ=[]
    =================================
    0x194b: v194b(0x40) = CONST 
    0x194e: v194e = MLOAD v194b(0x40)
    0x1951: MSTORE v194e, v74d(0x2710)
    0x1952: v1952 = MLOAD v194b(0x40)
    0x1956: v1956(0x0) = SUB v194e, v1952
    0x1957: v1957(0x20) = CONST 
    0x1959: v1959(0x20) = ADD v1957(0x20), v1956(0x0)
    0x195b: RETURN v1952, v1959(0x20)

}

function getExpectedReturn(address,address,uint256)() public {
    Begin block 0x2c6
    prev=[], succ=[0x2d8, 0x2dc]
    =================================
    0x2c7: v2c7(0x197b) = CONST 
    0x2ca: v2ca(0x4) = CONST 
    0x2cd: v2cd = CALLDATASIZE 
    0x2ce: v2ce = SUB v2cd, v2ca(0x4)
    0x2cf: v2cf(0x60) = CONST 
    0x2d2: v2d2 = LT v2ce, v2cf(0x60)
    0x2d3: v2d3 = ISZERO v2d2
    0x2d4: v2d4(0x2dc) = CONST 
    0x2d7: JUMPI v2d4(0x2dc), v2d3

    Begin block 0x2d8
    prev=[0x2c6], succ=[]
    =================================
    0x2d8: v2d8(0x0) = CONST 
    0x2db: REVERT v2d8(0x0), v2d8(0x0)

    Begin block 0x2dc
    prev=[0x2c6], succ=[0x752]
    =================================
    0x2de: v2de(0x1) = CONST 
    0x2e0: v2e0(0x1) = CONST 
    0x2e2: v2e2(0xa0) = CONST 
    0x2e4: v2e4(0x10000000000000000000000000000000000000000) = SHL v2e2(0xa0), v2e0(0x1)
    0x2e5: v2e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e4(0x10000000000000000000000000000000000000000), v2de(0x1)
    0x2e7: v2e7 = CALLDATALOAD v2ca(0x4)
    0x2e9: v2e9 = AND v2e5(0xffffffffffffffffffffffffffffffffffffffff), v2e7
    0x2eb: v2eb(0x20) = CONST 
    0x2ee: v2ee(0x24) = ADD v2ca(0x4), v2eb(0x20)
    0x2ef: v2ef = CALLDATALOAD v2ee(0x24)
    0x2f2: v2f2 = AND v2e5(0xffffffffffffffffffffffffffffffffffffffff), v2ef
    0x2f4: v2f4(0x40) = CONST 
    0x2f6: v2f6(0x44) = ADD v2f4(0x40), v2ca(0x4)
    0x2f7: v2f7 = CALLDATALOAD v2f6(0x44)
    0x2f8: v2f8(0x752) = CONST 
    0x2fb: JUMP v2f8(0x752)

    Begin block 0x752
    prev=[0x2dc], succ=[0x79e, 0x7a2]
    =================================
    0x753: v753(0x0) = CONST 
    0x757: v757(0x1) = CONST 
    0x759: v759(0x1) = CONST 
    0x75b: v75b(0xa0) = CONST 
    0x75d: v75d(0x10000000000000000000000000000000000000000) = SHL v75b(0xa0), v759(0x1)
    0x75e: v75e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75d(0x10000000000000000000000000000000000000000), v757(0x1)
    0x75f: v75f = AND v75e(0xffffffffffffffffffffffffffffffffffffffff), v2f2
    0x760: v760(0x70a08231) = CONST 
    0x766: v766(0x40) = CONST 
    0x768: v768 = MLOAD v766(0x40)
    0x76a: v76a(0xffffffff) = CONST 
    0x76f: v76f(0x70a08231) = AND v76a(0xffffffff), v760(0x70a08231)
    0x770: v770(0xe0) = CONST 
    0x772: v772(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v770(0xe0), v76f(0x70a08231)
    0x774: MSTORE v768, v772(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x775: v775(0x4) = CONST 
    0x777: v777 = ADD v775(0x4), v768
    0x77a: v77a(0x1) = CONST 
    0x77c: v77c(0x1) = CONST 
    0x77e: v77e(0xa0) = CONST 
    0x780: v780(0x10000000000000000000000000000000000000000) = SHL v77e(0xa0), v77c(0x1)
    0x781: v781(0xffffffffffffffffffffffffffffffffffffffff) = SUB v780(0x10000000000000000000000000000000000000000), v77a(0x1)
    0x782: v782 = AND v781(0xffffffffffffffffffffffffffffffffffffffff), v2e9
    0x784: MSTORE v777, v782
    0x785: v785(0x20) = CONST 
    0x787: v787 = ADD v785(0x20), v777
    0x78b: v78b(0x20) = CONST 
    0x78d: v78d(0x40) = CONST 
    0x78f: v78f = MLOAD v78d(0x40)
    0x792: v792(0x24) = SUB v787, v78f
    0x796: v796 = EXTCODESIZE v75f
    0x797: v797 = ISZERO v796
    0x799: v799 = ISZERO v797
    0x79a: v79a(0x7a2) = CONST 
    0x79d: JUMPI v79a(0x7a2), v799

    Begin block 0x79e
    prev=[0x752], succ=[]
    =================================
    0x79e: v79e(0x0) = CONST 
    0x7a1: REVERT v79e(0x0), v79e(0x0)

    Begin block 0x7a2
    prev=[0x752], succ=[0x7ad, 0x7b6]
    =================================
    0x7a4: v7a4 = GAS 
    0x7a5: v7a5 = STATICCALL v7a4, v75f, v78f, v792(0x24), v78f, v78b(0x20)
    0x7a6: v7a6 = ISZERO v7a5
    0x7a8: v7a8 = ISZERO v7a6
    0x7a9: v7a9(0x7b6) = CONST 
    0x7ac: JUMPI v7a9(0x7b6), v7a8

    Begin block 0x7ad
    prev=[0x7a2], succ=[]
    =================================
    0x7ad: v7ad = RETURNDATASIZE 
    0x7ae: v7ae(0x0) = CONST 
    0x7b1: RETURNDATACOPY v7ae(0x0), v7ae(0x0), v7ad
    0x7b2: v7b2 = RETURNDATASIZE 
    0x7b3: v7b3(0x0) = CONST 
    0x7b5: REVERT v7b3(0x0), v7b2

    Begin block 0x7b6
    prev=[0x7a2], succ=[0x7c8, 0x7cc]
    =================================
    0x7bb: v7bb(0x40) = CONST 
    0x7bd: v7bd = MLOAD v7bb(0x40)
    0x7be: v7be = RETURNDATASIZE 
    0x7bf: v7bf(0x20) = CONST 
    0x7c2: v7c2 = LT v7be, v7bf(0x20)
    0x7c3: v7c3 = ISZERO v7c2
    0x7c4: v7c4(0x7cc) = CONST 
    0x7c7: JUMPI v7c4(0x7cc), v7c3

    Begin block 0x7c8
    prev=[0x7b6], succ=[]
    =================================
    0x7c8: v7c8(0x0) = CONST 
    0x7cb: REVERT v7c8(0x0), v7c8(0x0)

    Begin block 0x7cc
    prev=[0x7b6], succ=[0x810, 0x814]
    =================================
    0x7ce: v7ce = MLOAD v7bd
    0x7cf: v7cf(0x40) = CONST 
    0x7d2: v7d2 = MLOAD v7cf(0x40)
    0x7d3: v7d3(0x1f1fcd51) = CONST 
    0x7d8: v7d8(0xe0) = CONST 
    0x7da: v7da(0x1f1fcd5100000000000000000000000000000000000000000000000000000000) = SHL v7d8(0xe0), v7d3(0x1f1fcd51)
    0x7dc: MSTORE v7d2, v7da(0x1f1fcd5100000000000000000000000000000000000000000000000000000000)
    0x7de: v7de = MLOAD v7cf(0x40)
    0x7e2: v7e2(0x0) = CONST 
    0x7e5: v7e5(0x1) = CONST 
    0x7e7: v7e7(0x1) = CONST 
    0x7e9: v7e9(0xa0) = CONST 
    0x7eb: v7eb(0x10000000000000000000000000000000000000000) = SHL v7e9(0xa0), v7e7(0x1)
    0x7ec: v7ec(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7eb(0x10000000000000000000000000000000000000000), v7e5(0x1)
    0x7ee: v7ee = AND v2e9, v7ec(0xffffffffffffffffffffffffffffffffffffffff)
    0x7f0: v7f0(0x1f1fcd51) = CONST 
    0x7f6: v7f6(0x4) = CONST 
    0x7fa: v7fa = ADD v7d2, v7f6(0x4)
    0x7fc: v7fc(0x20) = CONST 
    0x803: v803(0x0) = SUB v7d2, v7de
    0x804: v804(0x4) = ADD v803(0x0), v7f6(0x4)
    0x808: v808 = EXTCODESIZE v7ee
    0x809: v809 = ISZERO v808
    0x80b: v80b = ISZERO v809
    0x80c: v80c(0x814) = CONST 
    0x80f: JUMPI v80c(0x814), v80b

    Begin block 0x810
    prev=[0x7cc], succ=[]
    =================================
    0x810: v810(0x0) = CONST 
    0x813: REVERT v810(0x0), v810(0x0)

    Begin block 0x814
    prev=[0x7cc], succ=[0x81f, 0x828]
    =================================
    0x816: v816 = GAS 
    0x817: v817 = STATICCALL v816, v7ee, v7de, v804(0x4), v7de, v7fc(0x20)
    0x818: v818 = ISZERO v817
    0x81a: v81a = ISZERO v818
    0x81b: v81b(0x828) = CONST 
    0x81e: JUMPI v81b(0x828), v81a

    Begin block 0x81f
    prev=[0x814], succ=[]
    =================================
    0x81f: v81f = RETURNDATASIZE 
    0x820: v820(0x0) = CONST 
    0x823: RETURNDATACOPY v820(0x0), v820(0x0), v81f
    0x824: v824 = RETURNDATASIZE 
    0x825: v825(0x0) = CONST 
    0x827: REVERT v825(0x0), v824

    Begin block 0x828
    prev=[0x814], succ=[0x83a, 0x83e]
    =================================
    0x82d: v82d(0x40) = CONST 
    0x82f: v82f = MLOAD v82d(0x40)
    0x830: v830 = RETURNDATASIZE 
    0x831: v831(0x20) = CONST 
    0x834: v834 = LT v830, v831(0x20)
    0x835: v835 = ISZERO v834
    0x836: v836(0x83e) = CONST 
    0x839: JUMPI v836(0x83e), v835

    Begin block 0x83a
    prev=[0x828], succ=[]
    =================================
    0x83a: v83a(0x0) = CONST 
    0x83d: REVERT v83a(0x0), v83a(0x0)

    Begin block 0x83e
    prev=[0x828], succ=[0x8a7, 0x8ab]
    =================================
    0x840: v840 = MLOAD v82f
    0x841: v841(0x35) = CONST 
    0x843: v843 = SLOAD v841(0x35)
    0x844: v844(0x40) = CONST 
    0x847: v847 = MLOAD v844(0x40)
    0x848: v848(0x85e2c5b) = CONST 
    0x84d: v84d(0xe0) = CONST 
    0x84f: v84f(0x85e2c5b00000000000000000000000000000000000000000000000000000000) = SHL v84d(0xe0), v848(0x85e2c5b)
    0x851: MSTORE v847, v84f(0x85e2c5b00000000000000000000000000000000000000000000000000000000)
    0x852: v852(0x1) = CONST 
    0x854: v854(0x1) = CONST 
    0x856: v856(0xa0) = CONST 
    0x858: v858(0x10000000000000000000000000000000000000000) = SHL v856(0xa0), v854(0x1)
    0x859: v859(0xffffffffffffffffffffffffffffffffffffffff) = SUB v858(0x10000000000000000000000000000000000000000), v852(0x1)
    0x85c: v85c = AND v859(0xffffffffffffffffffffffffffffffffffffffff), v2f2
    0x85d: v85d(0x4) = CONST 
    0x860: v860 = ADD v847, v85d(0x4)
    0x861: MSTORE v860, v85c
    0x864: v864 = AND v840, v859(0xffffffffffffffffffffffffffffffffffffffff)
    0x865: v865(0x24) = CONST 
    0x868: v868 = ADD v847, v865(0x24)
    0x869: MSTORE v868, v864
    0x86a: v86a(0x44) = CONST 
    0x86d: v86d = ADD v847, v86a(0x44)
    0x870: MSTORE v86d, v7ce
    0x871: v871(0x64) = CONST 
    0x874: v874 = ADD v847, v871(0x64)
    0x877: MSTORE v874, v2f7
    0x878: v878(0x0) = CONST 
    0x87a: v87a(0x84) = CONST 
    0x87d: v87d = ADD v847, v87a(0x84)
    0x880: MSTORE v87d, v878(0x0)
    0x882: v882 = MLOAD v844(0x40)
    0x888: v888 = AND v843, v859(0xffffffffffffffffffffffffffffffffffffffff)
    0x88a: v88a(0x85e2c5b) = CONST 
    0x890: v890(0xa4) = CONST 
    0x894: v894 = ADD v847, v890(0xa4)
    0x89a: v89a(0x0) = SUB v847, v882
    0x89b: v89b(0xa4) = ADD v89a(0x0), v890(0xa4)
    0x89f: v89f = EXTCODESIZE v888
    0x8a0: v8a0 = ISZERO v89f
    0x8a2: v8a2 = ISZERO v8a0
    0x8a3: v8a3(0x8ab) = CONST 
    0x8a6: JUMPI v8a3(0x8ab), v8a2

    Begin block 0x8a7
    prev=[0x83e], succ=[]
    =================================
    0x8a7: v8a7(0x0) = CONST 
    0x8aa: REVERT v8a7(0x0), v8a7(0x0)

    Begin block 0x8ab
    prev=[0x83e], succ=[0x8b6, 0x8bf]
    =================================
    0x8ad: v8ad = GAS 
    0x8ae: v8ae = STATICCALL v8ad, v888, v882, v89b(0xa4), v882, v878(0x0)
    0x8af: v8af = ISZERO v8ae
    0x8b1: v8b1 = ISZERO v8af
    0x8b2: v8b2(0x8bf) = CONST 
    0x8b5: JUMPI v8b2(0x8bf), v8b1

    Begin block 0x8b6
    prev=[0x8ab], succ=[]
    =================================
    0x8b6: v8b6 = RETURNDATASIZE 
    0x8b7: v8b7(0x0) = CONST 
    0x8ba: RETURNDATACOPY v8b7(0x0), v8b7(0x0), v8b6
    0x8bb: v8bb = RETURNDATASIZE 
    0x8bc: v8bc(0x0) = CONST 
    0x8be: REVERT v8bc(0x0), v8bb

    Begin block 0x8bf
    prev=[0x8ab], succ=[0x8e4, 0x8e8]
    =================================
    0x8c4: v8c4(0x40) = CONST 
    0x8c6: v8c6 = MLOAD v8c4(0x40)
    0x8c7: v8c7 = RETURNDATASIZE 
    0x8c8: v8c8(0x0) = CONST 
    0x8cb: RETURNDATACOPY v8c6, v8c8(0x0), v8c7
    0x8cc: v8cc(0x1f) = CONST 
    0x8ce: v8ce = RETURNDATASIZE 
    0x8d1: v8d1 = ADD v8ce, v8cc(0x1f)
    0x8d2: v8d2(0x1f) = CONST 
    0x8d4: v8d4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v8d2(0x1f)
    0x8d5: v8d5 = AND v8d4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), v8d1
    0x8d7: v8d7 = ADD v8c6, v8d5
    0x8d8: v8d8(0x40) = CONST 
    0x8dc: MSTORE v8d8(0x40), v8d7
    0x8de: v8de = LT v8ce, v8d8(0x40)
    0x8df: v8df = ISZERO v8de
    0x8e0: v8e0(0x8e8) = CONST 
    0x8e3: JUMPI v8e0(0x8e8), v8df

    Begin block 0x8e4
    prev=[0x8bf], succ=[]
    =================================
    0x8e4: v8e4(0x0) = CONST 
    0x8e7: REVERT v8e4(0x0), v8e4(0x0)

    Begin block 0x8e8
    prev=[0x8bf], succ=[0x90b, 0x90f]
    =================================
    0x8ea: v8ea = MLOAD v8c6
    0x8eb: v8eb(0x20) = CONST 
    0x8ee: v8ee = ADD v8c6, v8eb(0x20)
    0x8f0: v8f0 = MLOAD v8ee
    0x8f1: v8f1(0x40) = CONST 
    0x8f3: v8f3 = MLOAD v8f1(0x40)
    0x8f9: v8f9 = ADD v8c6, v8ce
    0x8fe: v8fe(0x100000000) = CONST 
    0x905: v905 = GT v8f0, v8fe(0x100000000)
    0x906: v906 = ISZERO v905
    0x907: v907(0x90f) = CONST 
    0x90a: JUMPI v907(0x90f), v906

    Begin block 0x90b
    prev=[0x8e8], succ=[]
    =================================
    0x90b: v90b(0x0) = CONST 
    0x90e: REVERT v90b(0x0), v90b(0x0)

    Begin block 0x90f
    prev=[0x8e8], succ=[0x920, 0x924]
    =================================
    0x912: v912 = ADD v8c6, v8f0
    0x914: v914(0x20) = CONST 
    0x917: v917 = ADD v912, v914(0x20)
    0x91a: v91a = GT v917, v8f9
    0x91b: v91b = ISZERO v91a
    0x91c: v91c(0x924) = CONST 
    0x91f: JUMPI v91c(0x924), v91b

    Begin block 0x920
    prev=[0x90f], succ=[]
    =================================
    0x920: v920(0x0) = CONST 
    0x923: REVERT v920(0x0), v920(0x0)

    Begin block 0x924
    prev=[0x90f], succ=[0x93d, 0x941]
    =================================
    0x926: v926 = MLOAD v912
    0x928: v928(0x20) = CONST 
    0x92b: v92b = MUL v926, v928(0x20)
    0x92d: v92d = ADD v917, v92b
    0x92e: v92e = GT v92d, v8f9
    0x92f: v92f(0x100000000) = CONST 
    0x936: v936 = GT v926, v92f(0x100000000)
    0x937: v937 = OR v936, v92e
    0x938: v938 = ISZERO v937
    0x939: v939(0x941) = CONST 
    0x93c: JUMPI v939(0x941), v938

    Begin block 0x93d
    prev=[0x924], succ=[]
    =================================
    0x93d: v93d(0x0) = CONST 
    0x940: REVERT v93d(0x0), v93d(0x0)

    Begin block 0x941
    prev=[0x924], succ=[0x956]
    =================================
    0x943: MSTORE v8f3, v926
    0x946: v946 = MLOAD v912
    0x947: v947(0x20) = CONST 
    0x94b: v94b = ADD v947(0x20), v8f3
    0x94e: v94e = ADD v947(0x20), v912
    0x950: v950 = MUL v947(0x20), v946
    0x954: v954(0x0) = CONST 

    Begin block 0x956
    prev=[0x941, 0x95f], succ=[0x96e, 0x95f]
    =================================
    0x956_0x0: v956_0 = PHI v954(0x0), v969
    0x959: v959 = LT v956_0, v950
    0x95a: v95a = ISZERO v959
    0x95b: v95b(0x96e) = CONST 
    0x95e: JUMPI v95b(0x96e), v95a

    Begin block 0x96e
    prev=[0x956], succ=[0x197b]
    =================================
    0x975: v975 = ADD v950, v94b
    0x976: v976(0x40) = CONST 
    0x978: MSTORE v976(0x40), v975
    0x988: JUMP v2c7(0x197b)

    Begin block 0x197b
    prev=[0x96e], succ=[]
    =================================
    0x197c: v197c(0x40) = CONST 
    0x197f: v197f = MLOAD v197c(0x40)
    0x1982: MSTORE v197f, v8ea
    0x1983: v1983 = MLOAD v197c(0x40)
    0x1987: v1987(0x0) = SUB v197f, v1983
    0x1988: v1988(0x20) = CONST 
    0x198a: v198a(0x20) = ADD v1988(0x20), v1987(0x0)
    0x198c: RETURN v1983, v198a(0x20)

    Begin block 0x95f
    prev=[0x956], succ=[0x956]
    =================================
    0x95f_0x0: v95f_0 = PHI v954(0x0), v969
    0x961: v961 = ADD v95f_0, v94e
    0x962: v962 = MLOAD v961
    0x965: v965 = ADD v95f_0, v94b
    0x966: MSTORE v965, v962
    0x967: v967(0x20) = CONST 
    0x969: v969 = ADD v967(0x20), v95f_0
    0x96a: v96a(0x956) = CONST 
    0x96d: JUMP v96a(0x956)

}

function balanceOf(address)() public {
    Begin block 0x2fc
    prev=[], succ=[0x30e, 0x312]
    =================================
    0x2fd: v2fd(0x19ac) = CONST 
    0x300: v300(0x4) = CONST 
    0x303: v303 = CALLDATASIZE 
    0x304: v304 = SUB v303, v300(0x4)
    0x305: v305(0x20) = CONST 
    0x308: v308 = LT v304, v305(0x20)
    0x309: v309 = ISZERO v308
    0x30a: v30a(0x312) = CONST 
    0x30d: JUMPI v30a(0x312), v309

    Begin block 0x30e
    prev=[0x2fc], succ=[]
    =================================
    0x30e: v30e(0x0) = CONST 
    0x311: REVERT v30e(0x0), v30e(0x0)

    Begin block 0x312
    prev=[0x2fc], succ=[0x989]
    =================================
    0x314: v314 = CALLDATALOAD v300(0x4)
    0x315: v315(0x1) = CONST 
    0x317: v317(0x1) = CONST 
    0x319: v319(0xa0) = CONST 
    0x31b: v31b(0x10000000000000000000000000000000000000000) = SHL v319(0xa0), v317(0x1)
    0x31c: v31c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v31b(0x10000000000000000000000000000000000000000), v315(0x1)
    0x31d: v31d = AND v31c(0xffffffffffffffffffffffffffffffffffffffff), v314
    0x31e: v31e(0x989) = CONST 
    0x321: JUMP v31e(0x989)

    Begin block 0x989
    prev=[0x312], succ=[0x9d7, 0x9db]
    =================================
    0x98a: v98a(0x1) = CONST 
    0x98c: v98c(0x1) = CONST 
    0x98e: v98e(0xa0) = CONST 
    0x990: v990(0x10000000000000000000000000000000000000000) = SHL v98e(0xa0), v98c(0x1)
    0x991: v991(0xffffffffffffffffffffffffffffffffffffffff) = SUB v990(0x10000000000000000000000000000000000000000), v98a(0x1)
    0x994: v994 = AND v31d, v991(0xffffffffffffffffffffffffffffffffffffffff)
    0x995: v995(0x0) = CONST 
    0x999: MSTORE v995(0x0), v994
    0x99a: v99a(0x38) = CONST 
    0x99c: v99c(0x20) = CONST 
    0x9a0: MSTORE v99c(0x20), v99a(0x38)
    0x9a1: v9a1(0x40) = CONST 
    0x9a5: v9a5 = SHA3 v995(0x0), v9a1(0x40)
    0x9a6: v9a6 = SLOAD v9a5
    0x9a8: v9a8 = MLOAD v9a1(0x40)
    0x9a9: v9a9(0x722713f7) = CONST 
    0x9ae: v9ae(0xe0) = CONST 
    0x9b0: v9b0(0x722713f700000000000000000000000000000000000000000000000000000000) = SHL v9ae(0xe0), v9a9(0x722713f7)
    0x9b2: MSTORE v9a8, v9b0(0x722713f700000000000000000000000000000000000000000000000000000000)
    0x9b4: v9b4 = MLOAD v9a1(0x40)
    0x9b7: v9b7 = AND v991(0xffffffffffffffffffffffffffffffffffffffff), v9a6
    0x9b9: v9b9(0x722713f7) = CONST 
    0x9bf: v9bf(0x4) = CONST 
    0x9c3: v9c3 = ADD v9a8, v9bf(0x4)
    0x9ca: v9ca(0x0) = SUB v9a8, v9b4
    0x9cb: v9cb(0x4) = ADD v9ca(0x0), v9bf(0x4)
    0x9cf: v9cf = EXTCODESIZE v9b7
    0x9d0: v9d0 = ISZERO v9cf
    0x9d2: v9d2 = ISZERO v9d0
    0x9d3: v9d3(0x9db) = CONST 
    0x9d6: JUMPI v9d3(0x9db), v9d2

    Begin block 0x9d7
    prev=[0x989], succ=[]
    =================================
    0x9d7: v9d7(0x0) = CONST 
    0x9da: REVERT v9d7(0x0), v9d7(0x0)

    Begin block 0x9db
    prev=[0x989], succ=[0x9e6, 0x9ef]
    =================================
    0x9dd: v9dd = GAS 
    0x9de: v9de = STATICCALL v9dd, v9b7, v9b4, v9cb(0x4), v9b4, v99c(0x20)
    0x9df: v9df = ISZERO v9de
    0x9e1: v9e1 = ISZERO v9df
    0x9e2: v9e2(0x9ef) = CONST 
    0x9e5: JUMPI v9e2(0x9ef), v9e1

    Begin block 0x9e6
    prev=[0x9db], succ=[]
    =================================
    0x9e6: v9e6 = RETURNDATASIZE 
    0x9e7: v9e7(0x0) = CONST 
    0x9ea: RETURNDATACOPY v9e7(0x0), v9e7(0x0), v9e6
    0x9eb: v9eb = RETURNDATASIZE 
    0x9ec: v9ec(0x0) = CONST 
    0x9ee: REVERT v9ec(0x0), v9eb

    Begin block 0x9ef
    prev=[0x9db], succ=[0xa01, 0xa05]
    =================================
    0x9f4: v9f4(0x40) = CONST 
    0x9f6: v9f6 = MLOAD v9f4(0x40)
    0x9f7: v9f7 = RETURNDATASIZE 
    0x9f8: v9f8(0x20) = CONST 
    0x9fb: v9fb = LT v9f7, v9f8(0x20)
    0x9fc: v9fc = ISZERO v9fb
    0x9fd: v9fd(0xa05) = CONST 
    0xa00: JUMPI v9fd(0xa05), v9fc

    Begin block 0xa01
    prev=[0x9ef], succ=[]
    =================================
    0xa01: va01(0x0) = CONST 
    0xa04: REVERT va01(0x0), va01(0x0)

    Begin block 0xa05
    prev=[0x9ef], succ=[0x19ac]
    =================================
    0xa07: va07 = MLOAD v9f6
    0xa0c: JUMP v2fd(0x19ac)

    Begin block 0x19ac
    prev=[0xa05], succ=[]
    =================================
    0x19ad: v19ad(0x40) = CONST 
    0x19b0: v19b0 = MLOAD v19ad(0x40)
    0x19b3: MSTORE v19b0, va07
    0x19b4: v19b4 = MLOAD v19ad(0x40)
    0x19b8: v19b8(0x0) = SUB v19b0, v19b4
    0x19b9: v19b9(0x20) = CONST 
    0x19bb: v19bb(0x20) = ADD v19b9(0x20), v19b8(0x0)
    0x19bd: RETURN v19b4, v19bb(0x20)

}

function setVault(address,address)() public {
    Begin block 0x322
    prev=[], succ=[0x334, 0x338]
    =================================
    0x323: v323(0x19dd) = CONST 
    0x326: v326(0x4) = CONST 
    0x329: v329 = CALLDATASIZE 
    0x32a: v32a = SUB v329, v326(0x4)
    0x32b: v32b(0x40) = CONST 
    0x32e: v32e = LT v32a, v32b(0x40)
    0x32f: v32f = ISZERO v32e
    0x330: v330(0x338) = CONST 
    0x333: JUMPI v330(0x338), v32f

    Begin block 0x334
    prev=[0x322], succ=[]
    =================================
    0x334: v334(0x0) = CONST 
    0x337: REVERT v334(0x0), v334(0x0)

    Begin block 0x338
    prev=[0x322], succ=[0xa0d]
    =================================
    0x33a: v33a(0x1) = CONST 
    0x33c: v33c(0x1) = CONST 
    0x33e: v33e(0xa0) = CONST 
    0x340: v340(0x10000000000000000000000000000000000000000) = SHL v33e(0xa0), v33c(0x1)
    0x341: v341(0xffffffffffffffffffffffffffffffffffffffff) = SUB v340(0x10000000000000000000000000000000000000000), v33a(0x1)
    0x343: v343 = CALLDATALOAD v326(0x4)
    0x345: v345 = AND v341(0xffffffffffffffffffffffffffffffffffffffff), v343
    0x347: v347(0x20) = CONST 
    0x349: v349(0x24) = ADD v347(0x20), v326(0x4)
    0x34a: v34a = CALLDATALOAD v349(0x24)
    0x34b: v34b = AND v34a, v341(0xffffffffffffffffffffffffffffffffffffffff)
    0x34c: v34c(0xa0d) = CONST 
    0x34f: JUMP v34c(0xa0d)

    Begin block 0xa0d
    prev=[0x338], succ=[0xa15]
    =================================
    0xa0e: va0e(0xa15) = CONST 
    0xa11: va11(0x1222) = CONST 
    0xa14: CALLPRIVATE va11(0x1222), va0e(0xa15)

    Begin block 0xa15
    prev=[0xa0d], succ=[0xa36, 0xa6a]
    =================================
    0xa16: va16(0x1) = CONST 
    0xa18: va18(0x1) = CONST 
    0xa1a: va1a(0xa0) = CONST 
    0xa1c: va1c(0x10000000000000000000000000000000000000000) = SHL va1a(0xa0), va18(0x1)
    0xa1d: va1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1c(0x10000000000000000000000000000000000000000), va16(0x1)
    0xa20: va20 = AND va1d(0xffffffffffffffffffffffffffffffffffffffff), v345
    0xa21: va21(0x0) = CONST 
    0xa25: MSTORE va21(0x0), va20
    0xa26: va26(0x37) = CONST 
    0xa28: va28(0x20) = CONST 
    0xa2a: MSTORE va28(0x20), va26(0x37)
    0xa2b: va2b(0x40) = CONST 
    0xa2e: va2e = SHA3 va21(0x0), va2b(0x40)
    0xa2f: va2f = SLOAD va2e
    0xa30: va30 = AND va2f, va1d(0xffffffffffffffffffffffffffffffffffffffff)
    0xa31: va31 = ISZERO va30
    0xa32: va32(0xa6a) = CONST 
    0xa35: JUMPI va32(0xa6a), va31

    Begin block 0xa36
    prev=[0xa15], succ=[]
    =================================
    0xa36: va36(0x40) = CONST 
    0xa39: va39 = MLOAD va36(0x40)
    0xa3a: va3a(0x461bcd) = CONST 
    0xa3e: va3e(0xe5) = CONST 
    0xa40: va40(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL va3e(0xe5), va3a(0x461bcd)
    0xa42: MSTORE va39, va40(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa43: va43(0x20) = CONST 
    0xa45: va45(0x4) = CONST 
    0xa48: va48 = ADD va39, va45(0x4)
    0xa49: MSTORE va48, va43(0x20)
    0xa4a: va4a(0x5) = CONST 
    0xa4c: va4c(0x24) = CONST 
    0xa4f: va4f = ADD va39, va4c(0x24)
    0xa50: MSTORE va4f, va4a(0x5)
    0xa51: va51(0x1d985d5b1d) = CONST 
    0xa57: va57(0xda) = CONST 
    0xa59: va59(0x7661756c74000000000000000000000000000000000000000000000000000000) = SHL va57(0xda), va51(0x1d985d5b1d)
    0xa5a: va5a(0x44) = CONST 
    0xa5d: va5d = ADD va39, va5a(0x44)
    0xa5e: MSTORE va5d, va59(0x7661756c74000000000000000000000000000000000000000000000000000000)
    0xa60: va60 = MLOAD va36(0x40)
    0xa64: va64(0x0) = SUB va39, va60
    0xa65: va65(0x64) = CONST 
    0xa67: va67(0x64) = ADD va65(0x64), va64(0x0)
    0xa69: REVERT va60, va67(0x64)

    Begin block 0xa6a
    prev=[0xa15], succ=[0x19dd]
    =================================
    0xa6b: va6b(0x1) = CONST 
    0xa6d: va6d(0x1) = CONST 
    0xa6f: va6f(0xa0) = CONST 
    0xa71: va71(0x10000000000000000000000000000000000000000) = SHL va6f(0xa0), va6d(0x1)
    0xa72: va72(0xffffffffffffffffffffffffffffffffffffffff) = SUB va71(0x10000000000000000000000000000000000000000), va6b(0x1)
    0xa75: va75 = AND va72(0xffffffffffffffffffffffffffffffffffffffff), v345
    0xa76: va76(0x0) = CONST 
    0xa7a: MSTORE va76(0x0), va75
    0xa7b: va7b(0x37) = CONST 
    0xa7d: va7d(0x20) = CONST 
    0xa7f: MSTORE va7d(0x20), va7b(0x37)
    0xa80: va80(0x40) = CONST 
    0xa83: va83 = SHA3 va76(0x0), va80(0x40)
    0xa85: va85 = SLOAD va83
    0xa86: va86(0x1) = CONST 
    0xa88: va88(0x1) = CONST 
    0xa8a: va8a(0xa0) = CONST 
    0xa8c: va8c(0x10000000000000000000000000000000000000000) = SHL va8a(0xa0), va88(0x1)
    0xa8d: va8d(0xffffffffffffffffffffffffffffffffffffffff) = SUB va8c(0x10000000000000000000000000000000000000000), va86(0x1)
    0xa8e: va8e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT va8d(0xffffffffffffffffffffffffffffffffffffffff)
    0xa8f: va8f = AND va8e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va85
    0xa93: va93 = AND va72(0xffffffffffffffffffffffffffffffffffffffff), v34b
    0xa94: va94 = OR va93, va8f
    0xa96: SSTORE va83, va94
    0xa97: JUMP v323(0x19dd)

    Begin block 0x19dd
    prev=[0xa6a], succ=[]
    =================================
    0x19de: STOP 

}

function setStrategy(address,address)() public {
    Begin block 0x350
    prev=[], succ=[0x362, 0x366]
    =================================
    0x351: v351(0x19fe) = CONST 
    0x354: v354(0x4) = CONST 
    0x357: v357 = CALLDATASIZE 
    0x358: v358 = SUB v357, v354(0x4)
    0x359: v359(0x40) = CONST 
    0x35c: v35c = LT v358, v359(0x40)
    0x35d: v35d = ISZERO v35c
    0x35e: v35e(0x366) = CONST 
    0x361: JUMPI v35e(0x366), v35d

    Begin block 0x362
    prev=[0x350], succ=[]
    =================================
    0x362: v362(0x0) = CONST 
    0x365: REVERT v362(0x0), v362(0x0)

    Begin block 0x366
    prev=[0x350], succ=[0xa98]
    =================================
    0x368: v368(0x1) = CONST 
    0x36a: v36a(0x1) = CONST 
    0x36c: v36c(0xa0) = CONST 
    0x36e: v36e(0x10000000000000000000000000000000000000000) = SHL v36c(0xa0), v36a(0x1)
    0x36f: v36f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v36e(0x10000000000000000000000000000000000000000), v368(0x1)
    0x371: v371 = CALLDATALOAD v354(0x4)
    0x373: v373 = AND v36f(0xffffffffffffffffffffffffffffffffffffffff), v371
    0x375: v375(0x20) = CONST 
    0x377: v377(0x24) = ADD v375(0x20), v354(0x4)
    0x378: v378 = CALLDATALOAD v377(0x24)
    0x379: v379 = AND v378, v36f(0xffffffffffffffffffffffffffffffffffffffff)
    0x37a: v37a(0xa98) = CONST 
    0x37d: JUMP v37a(0xa98)

    Begin block 0xa98
    prev=[0x366], succ=[0xaa0]
    =================================
    0xa99: va99(0xaa0) = CONST 
    0xa9c: va9c(0x1222) = CONST 
    0xa9f: CALLPRIVATE va9c(0x1222), va99(0xaa0)

    Begin block 0xaa0
    prev=[0xa98], succ=[0xad3, 0xb0b]
    =================================
    0xaa1: vaa1(0x1) = CONST 
    0xaa3: vaa3(0x1) = CONST 
    0xaa5: vaa5(0xa0) = CONST 
    0xaa7: vaa7(0x10000000000000000000000000000000000000000) = SHL vaa5(0xa0), vaa3(0x1)
    0xaa8: vaa8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaa7(0x10000000000000000000000000000000000000000), vaa1(0x1)
    0xaab: vaab = AND v373, vaa8(0xffffffffffffffffffffffffffffffffffffffff)
    0xaac: vaac(0x0) = CONST 
    0xab0: MSTORE vaac(0x0), vaab
    0xab1: vab1(0x3a) = CONST 
    0xab3: vab3(0x20) = CONST 
    0xab7: MSTORE vab3(0x20), vab1(0x3a)
    0xab8: vab8(0x40) = CONST 
    0xabc: vabc = SHA3 vaac(0x0), vab8(0x40)
    0xabf: vabf = AND v379, vaa8(0xffffffffffffffffffffffffffffffffffffffff)
    0xac1: MSTORE vaac(0x0), vabf
    0xac4: MSTORE vab3(0x20), vabc
    0xac5: vac5 = SHA3 vaac(0x0), vab8(0x40)
    0xac6: vac6 = SLOAD vac5
    0xac7: vac7(0xff) = CONST 
    0xac9: vac9 = AND vac7(0xff), vac6
    0xaca: vaca = ISZERO vac9
    0xacb: vacb = ISZERO vaca
    0xacc: vacc(0x1) = CONST 
    0xace: vace = EQ vacc(0x1), vacb
    0xacf: vacf(0xb0b) = CONST 
    0xad2: JUMPI vacf(0xb0b), vace

    Begin block 0xad3
    prev=[0xaa0], succ=[]
    =================================
    0xad3: vad3(0x40) = CONST 
    0xad6: vad6 = MLOAD vad3(0x40)
    0xad7: vad7(0x461bcd) = CONST 
    0xadb: vadb(0xe5) = CONST 
    0xadd: vadd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vadb(0xe5), vad7(0x461bcd)
    0xadf: MSTORE vad6, vadd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xae0: vae0(0x20) = CONST 
    0xae2: vae2(0x4) = CONST 
    0xae5: vae5 = ADD vad6, vae2(0x4)
    0xae6: MSTORE vae5, vae0(0x20)
    0xae7: vae7(0x9) = CONST 
    0xae9: vae9(0x24) = CONST 
    0xaec: vaec = ADD vad6, vae9(0x24)
    0xaed: MSTORE vaec, vae7(0x9)
    0xaee: vaee(0x8585c1c1c9bdd9959) = CONST 
    0xaf8: vaf8(0xba) = CONST 
    0xafa: vafa(0x21617070726f7665640000000000000000000000000000000000000000000000) = SHL vaf8(0xba), vaee(0x8585c1c1c9bdd9959)
    0xafb: vafb(0x44) = CONST 
    0xafe: vafe = ADD vad6, vafb(0x44)
    0xaff: MSTORE vafe, vafa(0x21617070726f7665640000000000000000000000000000000000000000000000)
    0xb01: vb01 = MLOAD vad3(0x40)
    0xb05: vb05(0x0) = SUB vad6, vb01
    0xb06: vb06(0x64) = CONST 
    0xb08: vb08(0x64) = ADD vb06(0x64), vb05(0x0)
    0xb0a: REVERT vb01, vb08(0x64)

    Begin block 0xb0b
    prev=[0xaa0], succ=[0xb94, 0xb2d]
    =================================
    0xb0c: vb0c(0x1) = CONST 
    0xb0e: vb0e(0x1) = CONST 
    0xb10: vb10(0xa0) = CONST 
    0xb12: vb12(0x10000000000000000000000000000000000000000) = SHL vb10(0xa0), vb0e(0x1)
    0xb13: vb13(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb12(0x10000000000000000000000000000000000000000), vb0c(0x1)
    0xb16: vb16 = AND v373, vb13(0xffffffffffffffffffffffffffffffffffffffff)
    0xb17: vb17(0x0) = CONST 
    0xb1b: MSTORE vb17(0x0), vb16
    0xb1c: vb1c(0x38) = CONST 
    0xb1e: vb1e(0x20) = CONST 
    0xb20: MSTORE vb1e(0x20), vb1c(0x38)
    0xb21: vb21(0x40) = CONST 
    0xb24: vb24 = SHA3 vb17(0x0), vb21(0x40)
    0xb25: vb25 = SLOAD vb24
    0xb26: vb26 = AND vb25, vb13(0xffffffffffffffffffffffffffffffffffffffff)
    0xb28: vb28 = ISZERO vb26
    0xb29: vb29(0xb94) = CONST 
    0xb2c: JUMPI vb29(0xb94), vb28

    Begin block 0xb94
    prev=[0xb0b, 0xb91], succ=[0x19fe]
    =================================
    0xb96: vb96(0x1) = CONST 
    0xb98: vb98(0x1) = CONST 
    0xb9a: vb9a(0xa0) = CONST 
    0xb9c: vb9c(0x10000000000000000000000000000000000000000) = SHL vb9a(0xa0), vb98(0x1)
    0xb9d: vb9d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb9c(0x10000000000000000000000000000000000000000), vb96(0x1)
    0xba0: vba0 = AND vb9d(0xffffffffffffffffffffffffffffffffffffffff), v373
    0xba1: vba1(0x0) = CONST 
    0xba5: MSTORE vba1(0x0), vba0
    0xba6: vba6(0x38) = CONST 
    0xba8: vba8(0x20) = CONST 
    0xbaa: MSTORE vba8(0x20), vba6(0x38)
    0xbab: vbab(0x40) = CONST 
    0xbae: vbae = SHA3 vba1(0x0), vbab(0x40)
    0xbb0: vbb0 = SLOAD vbae
    0xbb1: vbb1(0x1) = CONST 
    0xbb3: vbb3(0x1) = CONST 
    0xbb5: vbb5(0xa0) = CONST 
    0xbb7: vbb7(0x10000000000000000000000000000000000000000) = SHL vbb5(0xa0), vbb3(0x1)
    0xbb8: vbb8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb7(0x10000000000000000000000000000000000000000), vbb1(0x1)
    0xbb9: vbb9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vbb8(0xffffffffffffffffffffffffffffffffffffffff)
    0xbba: vbba = AND vbb9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbb0
    0xbbe: vbbe = AND vb9d(0xffffffffffffffffffffffffffffffffffffffff), v379
    0xbbf: vbbf = OR vbbe, vbba
    0xbc1: SSTORE vbae, vbbf
    0xbc2: JUMP v351(0x19fe)

    Begin block 0x19fe
    prev=[0xb94], succ=[]
    =================================
    0x19ff: STOP 

    Begin block 0xb2d
    prev=[0xb0b], succ=[0xb63, 0xb67]
    =================================
    0xb2e: vb2e(0x1) = CONST 
    0xb30: vb30(0x1) = CONST 
    0xb32: vb32(0xa0) = CONST 
    0xb34: vb34(0x10000000000000000000000000000000000000000) = SHL vb32(0xa0), vb30(0x1)
    0xb35: vb35(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb34(0x10000000000000000000000000000000000000000), vb2e(0x1)
    0xb36: vb36 = AND vb35(0xffffffffffffffffffffffffffffffffffffffff), vb26
    0xb37: vb37(0x853828b6) = CONST 
    0xb3c: vb3c(0x40) = CONST 
    0xb3e: vb3e = MLOAD vb3c(0x40)
    0xb40: vb40(0xffffffff) = CONST 
    0xb45: vb45(0x853828b6) = AND vb40(0xffffffff), vb37(0x853828b6)
    0xb46: vb46(0xe0) = CONST 
    0xb48: vb48(0x853828b600000000000000000000000000000000000000000000000000000000) = SHL vb46(0xe0), vb45(0x853828b6)
    0xb4a: MSTORE vb3e, vb48(0x853828b600000000000000000000000000000000000000000000000000000000)
    0xb4b: vb4b(0x4) = CONST 
    0xb4d: vb4d = ADD vb4b(0x4), vb3e
    0xb4e: vb4e(0x20) = CONST 
    0xb50: vb50(0x40) = CONST 
    0xb52: vb52 = MLOAD vb50(0x40)
    0xb55: vb55(0x4) = SUB vb4d, vb52
    0xb57: vb57(0x0) = CONST 
    0xb5b: vb5b = EXTCODESIZE vb36
    0xb5c: vb5c = ISZERO vb5b
    0xb5e: vb5e = ISZERO vb5c
    0xb5f: vb5f(0xb67) = CONST 
    0xb62: JUMPI vb5f(0xb67), vb5e

    Begin block 0xb63
    prev=[0xb2d], succ=[]
    =================================
    0xb63: vb63(0x0) = CONST 
    0xb66: REVERT vb63(0x0), vb63(0x0)

    Begin block 0xb67
    prev=[0xb2d], succ=[0xb72, 0xb7b]
    =================================
    0xb69: vb69 = GAS 
    0xb6a: vb6a = CALL vb69, vb36, vb57(0x0), vb52, vb55(0x4), vb52, vb4e(0x20)
    0xb6b: vb6b = ISZERO vb6a
    0xb6d: vb6d = ISZERO vb6b
    0xb6e: vb6e(0xb7b) = CONST 
    0xb71: JUMPI vb6e(0xb7b), vb6d

    Begin block 0xb72
    prev=[0xb67], succ=[]
    =================================
    0xb72: vb72 = RETURNDATASIZE 
    0xb73: vb73(0x0) = CONST 
    0xb76: RETURNDATACOPY vb73(0x0), vb73(0x0), vb72
    0xb77: vb77 = RETURNDATASIZE 
    0xb78: vb78(0x0) = CONST 
    0xb7a: REVERT vb78(0x0), vb77

    Begin block 0xb7b
    prev=[0xb67], succ=[0xb8d, 0xb91]
    =================================
    0xb80: vb80(0x40) = CONST 
    0xb82: vb82 = MLOAD vb80(0x40)
    0xb83: vb83 = RETURNDATASIZE 
    0xb84: vb84(0x20) = CONST 
    0xb87: vb87 = LT vb83, vb84(0x20)
    0xb88: vb88 = ISZERO vb87
    0xb89: vb89(0xb91) = CONST 
    0xb8c: JUMPI vb89(0xb91), vb88

    Begin block 0xb8d
    prev=[0xb7b], succ=[]
    =================================
    0xb8d: vb8d(0x0) = CONST 
    0xb90: REVERT vb8d(0x0), vb8d(0x0)

    Begin block 0xb91
    prev=[0xb7b], succ=[0xb94]
    =================================

}

function setKeeper(address)() public {
    Begin block 0x37e
    prev=[], succ=[0x390, 0x394]
    =================================
    0x37f: v37f(0x1a1f) = CONST 
    0x382: v382(0x4) = CONST 
    0x385: v385 = CALLDATASIZE 
    0x386: v386 = SUB v385, v382(0x4)
    0x387: v387(0x20) = CONST 
    0x38a: v38a = LT v386, v387(0x20)
    0x38b: v38b = ISZERO v38a
    0x38c: v38c(0x394) = CONST 
    0x38f: JUMPI v38c(0x394), v38b

    Begin block 0x390
    prev=[0x37e], succ=[]
    =================================
    0x390: v390(0x0) = CONST 
    0x393: REVERT v390(0x0), v390(0x0)

    Begin block 0x394
    prev=[0x37e], succ=[0xbc3]
    =================================
    0x396: v396 = CALLDATALOAD v382(0x4)
    0x397: v397(0x1) = CONST 
    0x399: v399(0x1) = CONST 
    0x39b: v39b(0xa0) = CONST 
    0x39d: v39d(0x10000000000000000000000000000000000000000) = SHL v39b(0xa0), v399(0x1)
    0x39e: v39e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39d(0x10000000000000000000000000000000000000000), v397(0x1)
    0x39f: v39f = AND v39e(0xffffffffffffffffffffffffffffffffffffffff), v396
    0x3a0: v3a0(0xbc3) = CONST 
    0x3a3: JUMP v3a0(0xbc3)

    Begin block 0xbc3
    prev=[0x394], succ=[0x129eB0xbc3]
    =================================
    0xbc4: vbc4(0xbcb) = CONST 
    0xbc7: vbc7(0x129e) = CONST 
    0xbca: JUMP vbc7(0x129e), vbc4(0xbcb)

    Begin block 0x129eB0xbc3
    prev=[0xbc3], succ=[0x12b7B0xbc3, 0x1d48B0xbc3]
    =================================
    0x129fS0xbc3: v129fVbc3(0x0) = CONST 
    0x12a1S0xbc3: v12a1Vbc3 = SLOAD v129fVbc3(0x0)
    0x12a2S0xbc3: v12a2Vbc3(0x10000) = CONST 
    0x12a7S0xbc3: v12a7Vbc3 = DIV v12a1Vbc3, v12a2Vbc3(0x10000)
    0x12a8S0xbc3: v12a8Vbc3(0x1) = CONST 
    0x12aaS0xbc3: v12aaVbc3(0x1) = CONST 
    0x12acS0xbc3: v12acVbc3(0xa0) = CONST 
    0x12aeS0xbc3: v12aeVbc3(0x10000000000000000000000000000000000000000) = SHL v12acVbc3(0xa0), v12aaVbc3(0x1)
    0x12afS0xbc3: v12afVbc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVbc3(0x10000000000000000000000000000000000000000), v12a8Vbc3(0x1)
    0x12b0S0xbc3: v12b0Vbc3 = AND v12afVbc3(0xffffffffffffffffffffffffffffffffffffffff), v12a7Vbc3
    0x12b1S0xbc3: v12b1Vbc3 = CALLER 
    0x12b2S0xbc3: v12b2Vbc3 = EQ v12b1Vbc3, v12b0Vbc3
    0x12b3S0xbc3: v12b3Vbc3(0x1d48) = CONST 
    0x12b6S0xbc3: JUMPI v12b3Vbc3(0x1d48), v12b2Vbc3

    Begin block 0x12b7B0xbc3
    prev=[0x129eB0xbc3], succ=[]
    =================================
    0x12b7S0xbc3: v12b7Vbc3(0x40) = CONST 
    0x12baS0xbc3: v12baVbc3 = MLOAD v12b7Vbc3(0x40)
    0x12bbS0xbc3: v12bbVbc3(0x461bcd) = CONST 
    0x12bfS0xbc3: v12bfVbc3(0xe5) = CONST 
    0x12c1S0xbc3: v12c1Vbc3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVbc3(0xe5), v12bbVbc3(0x461bcd)
    0x12c3S0xbc3: MSTORE v12baVbc3, v12c1Vbc3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xbc3: v12c4Vbc3(0x20) = CONST 
    0x12c6S0xbc3: v12c6Vbc3(0x4) = CONST 
    0x12c9S0xbc3: v12c9Vbc3 = ADD v12baVbc3, v12c6Vbc3(0x4)
    0x12caS0xbc3: MSTORE v12c9Vbc3, v12c4Vbc3(0x20)
    0x12cbS0xbc3: v12cbVbc3(0xe) = CONST 
    0x12cdS0xbc3: v12cdVbc3(0x24) = CONST 
    0x12d0S0xbc3: v12d0Vbc3 = ADD v12baVbc3, v12cdVbc3(0x24)
    0x12d1S0xbc3: MSTORE v12d0Vbc3, v12cbVbc3(0xe)
    0x12d2S0xbc3: v12d2Vbc3(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xbc3: v12e1Vbc3(0x90) = CONST 
    0x12e3S0xbc3: v12e3Vbc3(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Vbc3(0x90), v12d2Vbc3(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xbc3: v12e4Vbc3(0x44) = CONST 
    0x12e7S0xbc3: v12e7Vbc3 = ADD v12baVbc3, v12e4Vbc3(0x44)
    0x12e8S0xbc3: MSTORE v12e7Vbc3, v12e3Vbc3(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xbc3: v12eaVbc3 = MLOAD v12b7Vbc3(0x40)
    0x12eeS0xbc3: v12eeVbc3(0x0) = SUB v12baVbc3, v12eaVbc3
    0x12efS0xbc3: v12efVbc3(0x64) = CONST 
    0x12f1S0xbc3: v12f1Vbc3(0x64) = ADD v12efVbc3(0x64), v12eeVbc3(0x0)
    0x12f3S0xbc3: REVERT v12eaVbc3, v12f1Vbc3(0x64)

    Begin block 0x1d48B0xbc3
    prev=[0x129eB0xbc3], succ=[0xbcb]
    =================================
    0x1d49S0xbc3: JUMP vbc4(0xbcb)

    Begin block 0xbcb
    prev=[0x1d48B0xbc3], succ=[0x1a1f]
    =================================
    0xbcc: vbcc(0x2) = CONST 
    0xbcf: vbcf = SLOAD vbcc(0x2)
    0xbd0: vbd0(0x1) = CONST 
    0xbd2: vbd2(0x1) = CONST 
    0xbd4: vbd4(0xa0) = CONST 
    0xbd6: vbd6(0x10000000000000000000000000000000000000000) = SHL vbd4(0xa0), vbd2(0x1)
    0xbd7: vbd7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbd6(0x10000000000000000000000000000000000000000), vbd0(0x1)
    0xbd8: vbd8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vbd7(0xffffffffffffffffffffffffffffffffffffffff)
    0xbd9: vbd9 = AND vbd8(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbcf
    0xbda: vbda(0x1) = CONST 
    0xbdc: vbdc(0x1) = CONST 
    0xbde: vbde(0xa0) = CONST 
    0xbe0: vbe0(0x10000000000000000000000000000000000000000) = SHL vbde(0xa0), vbdc(0x1)
    0xbe1: vbe1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbe0(0x10000000000000000000000000000000000000000), vbda(0x1)
    0xbe5: vbe5 = AND vbe1(0xffffffffffffffffffffffffffffffffffffffff), v39f
    0xbe9: vbe9 = OR vbe5, vbd9
    0xbeb: SSTORE vbcc(0x2), vbe9
    0xbec: JUMP v37f(0x1a1f)

    Begin block 0x1a1f
    prev=[0xbcb], succ=[]
    =================================
    0x1a20: STOP 

}

function setOneSplit(address)() public {
    Begin block 0x3a4
    prev=[], succ=[0x3b6, 0x3ba]
    =================================
    0x3a5: v3a5(0x1a40) = CONST 
    0x3a8: v3a8(0x4) = CONST 
    0x3ab: v3ab = CALLDATASIZE 
    0x3ac: v3ac = SUB v3ab, v3a8(0x4)
    0x3ad: v3ad(0x20) = CONST 
    0x3b0: v3b0 = LT v3ac, v3ad(0x20)
    0x3b1: v3b1 = ISZERO v3b0
    0x3b2: v3b2(0x3ba) = CONST 
    0x3b5: JUMPI v3b2(0x3ba), v3b1

    Begin block 0x3b6
    prev=[0x3a4], succ=[]
    =================================
    0x3b6: v3b6(0x0) = CONST 
    0x3b9: REVERT v3b6(0x0), v3b6(0x0)

    Begin block 0x3ba
    prev=[0x3a4], succ=[0xbed]
    =================================
    0x3bc: v3bc = CALLDATALOAD v3a8(0x4)
    0x3bd: v3bd(0x1) = CONST 
    0x3bf: v3bf(0x1) = CONST 
    0x3c1: v3c1(0xa0) = CONST 
    0x3c3: v3c3(0x10000000000000000000000000000000000000000) = SHL v3c1(0xa0), v3bf(0x1)
    0x3c4: v3c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c3(0x10000000000000000000000000000000000000000), v3bd(0x1)
    0x3c5: v3c5 = AND v3c4(0xffffffffffffffffffffffffffffffffffffffff), v3bc
    0x3c6: v3c6(0xbed) = CONST 
    0x3c9: JUMP v3c6(0xbed)

    Begin block 0xbed
    prev=[0x3ba], succ=[0x129eB0xbed]
    =================================
    0xbee: vbee(0xbf5) = CONST 
    0xbf1: vbf1(0x129e) = CONST 
    0xbf4: JUMP vbf1(0x129e), vbee(0xbf5)

    Begin block 0x129eB0xbed
    prev=[0xbed], succ=[0x12b7B0xbed, 0x1d48B0xbed]
    =================================
    0x129fS0xbed: v129fVbed(0x0) = CONST 
    0x12a1S0xbed: v12a1Vbed = SLOAD v129fVbed(0x0)
    0x12a2S0xbed: v12a2Vbed(0x10000) = CONST 
    0x12a7S0xbed: v12a7Vbed = DIV v12a1Vbed, v12a2Vbed(0x10000)
    0x12a8S0xbed: v12a8Vbed(0x1) = CONST 
    0x12aaS0xbed: v12aaVbed(0x1) = CONST 
    0x12acS0xbed: v12acVbed(0xa0) = CONST 
    0x12aeS0xbed: v12aeVbed(0x10000000000000000000000000000000000000000) = SHL v12acVbed(0xa0), v12aaVbed(0x1)
    0x12afS0xbed: v12afVbed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVbed(0x10000000000000000000000000000000000000000), v12a8Vbed(0x1)
    0x12b0S0xbed: v12b0Vbed = AND v12afVbed(0xffffffffffffffffffffffffffffffffffffffff), v12a7Vbed
    0x12b1S0xbed: v12b1Vbed = CALLER 
    0x12b2S0xbed: v12b2Vbed = EQ v12b1Vbed, v12b0Vbed
    0x12b3S0xbed: v12b3Vbed(0x1d48) = CONST 
    0x12b6S0xbed: JUMPI v12b3Vbed(0x1d48), v12b2Vbed

    Begin block 0x12b7B0xbed
    prev=[0x129eB0xbed], succ=[]
    =================================
    0x12b7S0xbed: v12b7Vbed(0x40) = CONST 
    0x12baS0xbed: v12baVbed = MLOAD v12b7Vbed(0x40)
    0x12bbS0xbed: v12bbVbed(0x461bcd) = CONST 
    0x12bfS0xbed: v12bfVbed(0xe5) = CONST 
    0x12c1S0xbed: v12c1Vbed(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVbed(0xe5), v12bbVbed(0x461bcd)
    0x12c3S0xbed: MSTORE v12baVbed, v12c1Vbed(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xbed: v12c4Vbed(0x20) = CONST 
    0x12c6S0xbed: v12c6Vbed(0x4) = CONST 
    0x12c9S0xbed: v12c9Vbed = ADD v12baVbed, v12c6Vbed(0x4)
    0x12caS0xbed: MSTORE v12c9Vbed, v12c4Vbed(0x20)
    0x12cbS0xbed: v12cbVbed(0xe) = CONST 
    0x12cdS0xbed: v12cdVbed(0x24) = CONST 
    0x12d0S0xbed: v12d0Vbed = ADD v12baVbed, v12cdVbed(0x24)
    0x12d1S0xbed: MSTORE v12d0Vbed, v12cbVbed(0xe)
    0x12d2S0xbed: v12d2Vbed(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xbed: v12e1Vbed(0x90) = CONST 
    0x12e3S0xbed: v12e3Vbed(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Vbed(0x90), v12d2Vbed(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xbed: v12e4Vbed(0x44) = CONST 
    0x12e7S0xbed: v12e7Vbed = ADD v12baVbed, v12e4Vbed(0x44)
    0x12e8S0xbed: MSTORE v12e7Vbed, v12e3Vbed(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xbed: v12eaVbed = MLOAD v12b7Vbed(0x40)
    0x12eeS0xbed: v12eeVbed(0x0) = SUB v12baVbed, v12eaVbed
    0x12efS0xbed: v12efVbed(0x64) = CONST 
    0x12f1S0xbed: v12f1Vbed(0x64) = ADD v12efVbed(0x64), v12eeVbed(0x0)
    0x12f3S0xbed: REVERT v12eaVbed, v12f1Vbed(0x64)

    Begin block 0x1d48B0xbed
    prev=[0x129eB0xbed], succ=[0xbf5]
    =================================
    0x1d49S0xbed: JUMP vbee(0xbf5)

    Begin block 0xbf5
    prev=[0x1d48B0xbed], succ=[0x1a40]
    =================================
    0xbf6: vbf6(0x35) = CONST 
    0xbf9: vbf9 = SLOAD vbf6(0x35)
    0xbfa: vbfa(0x1) = CONST 
    0xbfc: vbfc(0x1) = CONST 
    0xbfe: vbfe(0xa0) = CONST 
    0xc00: vc00(0x10000000000000000000000000000000000000000) = SHL vbfe(0xa0), vbfc(0x1)
    0xc01: vc01(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc00(0x10000000000000000000000000000000000000000), vbfa(0x1)
    0xc02: vc02(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vc01(0xffffffffffffffffffffffffffffffffffffffff)
    0xc03: vc03 = AND vc02(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbf9
    0xc04: vc04(0x1) = CONST 
    0xc06: vc06(0x1) = CONST 
    0xc08: vc08(0xa0) = CONST 
    0xc0a: vc0a(0x10000000000000000000000000000000000000000) = SHL vc08(0xa0), vc06(0x1)
    0xc0b: vc0b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc0a(0x10000000000000000000000000000000000000000), vc04(0x1)
    0xc0f: vc0f = AND vc0b(0xffffffffffffffffffffffffffffffffffffffff), v3c5
    0xc13: vc13 = OR vc0f, vc03
    0xc15: SSTORE vbf6(0x35), vc13
    0xc16: JUMP v3a5(0x1a40)

    Begin block 0x1a40
    prev=[0xbf5], succ=[]
    =================================
    0x1a41: STOP 

}

function rewards()() public {
    Begin block 0x3ca
    prev=[], succ=[0xc17]
    =================================
    0x3cb: v3cb(0x1a61) = CONST 
    0x3ce: v3ce(0xc17) = CONST 
    0x3d1: JUMP v3ce(0xc17)

    Begin block 0xc17
    prev=[0x3ca], succ=[0x1a61]
    =================================
    0xc18: vc18(0x36) = CONST 
    0xc1a: vc1a = SLOAD vc18(0x36)
    0xc1b: vc1b(0x1) = CONST 
    0xc1d: vc1d(0x1) = CONST 
    0xc1f: vc1f(0xa0) = CONST 
    0xc21: vc21(0x10000000000000000000000000000000000000000) = SHL vc1f(0xa0), vc1d(0x1)
    0xc22: vc22(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc21(0x10000000000000000000000000000000000000000), vc1b(0x1)
    0xc23: vc23 = AND vc22(0xffffffffffffffffffffffffffffffffffffffff), vc1a
    0xc25: JUMP v3cb(0x1a61)

    Begin block 0x1a61
    prev=[0xc17], succ=[]
    =================================
    0x1a62: v1a62(0x40) = CONST 
    0x1a65: v1a65 = MLOAD v1a62(0x40)
    0x1a66: v1a66(0x1) = CONST 
    0x1a68: v1a68(0x1) = CONST 
    0x1a6a: v1a6a(0xa0) = CONST 
    0x1a6c: v1a6c(0x10000000000000000000000000000000000000000) = SHL v1a6a(0xa0), v1a68(0x1)
    0x1a6d: v1a6d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a6c(0x10000000000000000000000000000000000000000), v1a66(0x1)
    0x1a70: v1a70 = AND vc23, v1a6d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a72: MSTORE v1a65, v1a70
    0x1a73: v1a73 = MLOAD v1a62(0x40)
    0x1a77: v1a77(0x0) = SUB v1a65, v1a73
    0x1a78: v1a78(0x20) = CONST 
    0x1a7a: v1a7a(0x20) = ADD v1a78(0x20), v1a77(0x0)
    0x1a7c: RETURN v1a73, v1a7a(0x20)

}

function approvedStrategies(address,address)() public {
    Begin block 0x3d2
    prev=[], succ=[0x3e4, 0x3e8]
    =================================
    0x3d3: v3d3(0x400) = CONST 
    0x3d6: v3d6(0x4) = CONST 
    0x3d9: v3d9 = CALLDATASIZE 
    0x3da: v3da = SUB v3d9, v3d6(0x4)
    0x3db: v3db(0x40) = CONST 
    0x3de: v3de = LT v3da, v3db(0x40)
    0x3df: v3df = ISZERO v3de
    0x3e0: v3e0(0x3e8) = CONST 
    0x3e3: JUMPI v3e0(0x3e8), v3df

    Begin block 0x3e4
    prev=[0x3d2], succ=[]
    =================================
    0x3e4: v3e4(0x0) = CONST 
    0x3e7: REVERT v3e4(0x0), v3e4(0x0)

    Begin block 0x3e8
    prev=[0x3d2], succ=[0xc26]
    =================================
    0x3ea: v3ea(0x1) = CONST 
    0x3ec: v3ec(0x1) = CONST 
    0x3ee: v3ee(0xa0) = CONST 
    0x3f0: v3f0(0x10000000000000000000000000000000000000000) = SHL v3ee(0xa0), v3ec(0x1)
    0x3f1: v3f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f0(0x10000000000000000000000000000000000000000), v3ea(0x1)
    0x3f3: v3f3 = CALLDATALOAD v3d6(0x4)
    0x3f5: v3f5 = AND v3f1(0xffffffffffffffffffffffffffffffffffffffff), v3f3
    0x3f7: v3f7(0x20) = CONST 
    0x3f9: v3f9(0x24) = ADD v3f7(0x20), v3d6(0x4)
    0x3fa: v3fa = CALLDATALOAD v3f9(0x24)
    0x3fb: v3fb = AND v3fa, v3f1(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fc: v3fc(0xc26) = CONST 
    0x3ff: JUMP v3fc(0xc26)

    Begin block 0xc26
    prev=[0x3e8], succ=[0x400]
    =================================
    0xc27: vc27(0x3a) = CONST 
    0xc29: vc29(0x20) = CONST 
    0xc2d: MSTORE vc29(0x20), vc27(0x3a)
    0xc2e: vc2e(0x0) = CONST 
    0xc32: MSTORE vc2e(0x0), v3f5
    0xc33: vc33(0x40) = CONST 
    0xc37: vc37 = SHA3 vc2e(0x0), vc33(0x40)
    0xc3a: MSTORE vc29(0x20), vc37
    0xc3d: MSTORE vc2e(0x0), v3fb
    0xc3f: vc3f = SHA3 vc2e(0x0), vc33(0x40)
    0xc40: vc40 = SLOAD vc3f
    0xc41: vc41(0xff) = CONST 
    0xc43: vc43 = AND vc41(0xff), vc40
    0xc45: JUMP v3d3(0x400)

    Begin block 0x400
    prev=[0xc26], succ=[]
    =================================
    0x401: v401(0x40) = CONST 
    0x404: v404 = MLOAD v401(0x40)
    0x406: v406 = ISZERO vc43
    0x407: v407 = ISZERO v406
    0x409: MSTORE v404, v407
    0x40a: v40a = MLOAD v401(0x40)
    0x40e: v40e(0x0) = SUB v404, v40a
    0x40f: v40f(0x20) = CONST 
    0x411: v411(0x20) = ADD v40f(0x20), v40e(0x0)
    0x413: RETURN v40a, v411(0x20)

}

function vaults(address)() public {
    Begin block 0x414
    prev=[], succ=[0x426, 0x42a]
    =================================
    0x415: v415(0x1a9c) = CONST 
    0x418: v418(0x4) = CONST 
    0x41b: v41b = CALLDATASIZE 
    0x41c: v41c = SUB v41b, v418(0x4)
    0x41d: v41d(0x20) = CONST 
    0x420: v420 = LT v41c, v41d(0x20)
    0x421: v421 = ISZERO v420
    0x422: v422(0x42a) = CONST 
    0x425: JUMPI v422(0x42a), v421

    Begin block 0x426
    prev=[0x414], succ=[]
    =================================
    0x426: v426(0x0) = CONST 
    0x429: REVERT v426(0x0), v426(0x0)

    Begin block 0x42a
    prev=[0x414], succ=[0xc46]
    =================================
    0x42c: v42c = CALLDATALOAD v418(0x4)
    0x42d: v42d(0x1) = CONST 
    0x42f: v42f(0x1) = CONST 
    0x431: v431(0xa0) = CONST 
    0x433: v433(0x10000000000000000000000000000000000000000) = SHL v431(0xa0), v42f(0x1)
    0x434: v434(0xffffffffffffffffffffffffffffffffffffffff) = SUB v433(0x10000000000000000000000000000000000000000), v42d(0x1)
    0x435: v435 = AND v434(0xffffffffffffffffffffffffffffffffffffffff), v42c
    0x436: v436(0xc46) = CONST 
    0x439: JUMP v436(0xc46)

    Begin block 0xc46
    prev=[0x42a], succ=[0x1a9c]
    =================================
    0xc47: vc47(0x37) = CONST 
    0xc49: vc49(0x20) = CONST 
    0xc4b: MSTORE vc49(0x20), vc47(0x37)
    0xc4c: vc4c(0x0) = CONST 
    0xc50: MSTORE vc4c(0x0), v435
    0xc51: vc51(0x40) = CONST 
    0xc54: vc54 = SHA3 vc4c(0x0), vc51(0x40)
    0xc55: vc55 = SLOAD vc54
    0xc56: vc56(0x1) = CONST 
    0xc58: vc58(0x1) = CONST 
    0xc5a: vc5a(0xa0) = CONST 
    0xc5c: vc5c(0x10000000000000000000000000000000000000000) = SHL vc5a(0xa0), vc58(0x1)
    0xc5d: vc5d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc5c(0x10000000000000000000000000000000000000000), vc56(0x1)
    0xc5e: vc5e = AND vc5d(0xffffffffffffffffffffffffffffffffffffffff), vc55
    0xc60: JUMP v415(0x1a9c)

    Begin block 0x1a9c
    prev=[0xc46], succ=[]
    =================================
    0x1a9d: v1a9d(0x40) = CONST 
    0x1aa0: v1aa0 = MLOAD v1a9d(0x40)
    0x1aa1: v1aa1(0x1) = CONST 
    0x1aa3: v1aa3(0x1) = CONST 
    0x1aa5: v1aa5(0xa0) = CONST 
    0x1aa7: v1aa7(0x10000000000000000000000000000000000000000) = SHL v1aa5(0xa0), v1aa3(0x1)
    0x1aa8: v1aa8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1aa7(0x10000000000000000000000000000000000000000), v1aa1(0x1)
    0x1aab: v1aab = AND vc5e, v1aa8(0xffffffffffffffffffffffffffffffffffffffff)
    0x1aad: MSTORE v1aa0, v1aab
    0x1aae: v1aae = MLOAD v1a9d(0x40)
    0x1ab2: v1ab2(0x0) = SUB v1aa0, v1aae
    0x1ab3: v1ab3(0x20) = CONST 
    0x1ab5: v1ab5(0x20) = ADD v1ab3(0x20), v1ab2(0x0)
    0x1ab7: RETURN v1aae, v1ab5(0x20)

}

function setGovernance(address)() public {
    Begin block 0x43a
    prev=[], succ=[0x44c, 0x450]
    =================================
    0x43b: v43b(0x1ad7) = CONST 
    0x43e: v43e(0x4) = CONST 
    0x441: v441 = CALLDATASIZE 
    0x442: v442 = SUB v441, v43e(0x4)
    0x443: v443(0x20) = CONST 
    0x446: v446 = LT v442, v443(0x20)
    0x447: v447 = ISZERO v446
    0x448: v448(0x450) = CONST 
    0x44b: JUMPI v448(0x450), v447

    Begin block 0x44c
    prev=[0x43a], succ=[]
    =================================
    0x44c: v44c(0x0) = CONST 
    0x44f: REVERT v44c(0x0), v44c(0x0)

    Begin block 0x450
    prev=[0x43a], succ=[0xc61]
    =================================
    0x452: v452 = CALLDATALOAD v43e(0x4)
    0x453: v453(0x1) = CONST 
    0x455: v455(0x1) = CONST 
    0x457: v457(0xa0) = CONST 
    0x459: v459(0x10000000000000000000000000000000000000000) = SHL v457(0xa0), v455(0x1)
    0x45a: v45a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v459(0x10000000000000000000000000000000000000000), v453(0x1)
    0x45b: v45b = AND v45a(0xffffffffffffffffffffffffffffffffffffffff), v452
    0x45c: v45c(0xc61) = CONST 
    0x45f: JUMP v45c(0xc61)

    Begin block 0xc61
    prev=[0x450], succ=[0x129eB0xc61]
    =================================
    0xc62: vc62(0xc69) = CONST 
    0xc65: vc65(0x129e) = CONST 
    0xc68: JUMP vc65(0x129e), vc62(0xc69)

    Begin block 0x129eB0xc61
    prev=[0xc61], succ=[0x12b7B0xc61, 0x1d48B0xc61]
    =================================
    0x129fS0xc61: v129fVc61(0x0) = CONST 
    0x12a1S0xc61: v12a1Vc61 = SLOAD v129fVc61(0x0)
    0x12a2S0xc61: v12a2Vc61(0x10000) = CONST 
    0x12a7S0xc61: v12a7Vc61 = DIV v12a1Vc61, v12a2Vc61(0x10000)
    0x12a8S0xc61: v12a8Vc61(0x1) = CONST 
    0x12aaS0xc61: v12aaVc61(0x1) = CONST 
    0x12acS0xc61: v12acVc61(0xa0) = CONST 
    0x12aeS0xc61: v12aeVc61(0x10000000000000000000000000000000000000000) = SHL v12acVc61(0xa0), v12aaVc61(0x1)
    0x12afS0xc61: v12afVc61(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVc61(0x10000000000000000000000000000000000000000), v12a8Vc61(0x1)
    0x12b0S0xc61: v12b0Vc61 = AND v12afVc61(0xffffffffffffffffffffffffffffffffffffffff), v12a7Vc61
    0x12b1S0xc61: v12b1Vc61 = CALLER 
    0x12b2S0xc61: v12b2Vc61 = EQ v12b1Vc61, v12b0Vc61
    0x12b3S0xc61: v12b3Vc61(0x1d48) = CONST 
    0x12b6S0xc61: JUMPI v12b3Vc61(0x1d48), v12b2Vc61

    Begin block 0x12b7B0xc61
    prev=[0x129eB0xc61], succ=[]
    =================================
    0x12b7S0xc61: v12b7Vc61(0x40) = CONST 
    0x12baS0xc61: v12baVc61 = MLOAD v12b7Vc61(0x40)
    0x12bbS0xc61: v12bbVc61(0x461bcd) = CONST 
    0x12bfS0xc61: v12bfVc61(0xe5) = CONST 
    0x12c1S0xc61: v12c1Vc61(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVc61(0xe5), v12bbVc61(0x461bcd)
    0x12c3S0xc61: MSTORE v12baVc61, v12c1Vc61(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xc61: v12c4Vc61(0x20) = CONST 
    0x12c6S0xc61: v12c6Vc61(0x4) = CONST 
    0x12c9S0xc61: v12c9Vc61 = ADD v12baVc61, v12c6Vc61(0x4)
    0x12caS0xc61: MSTORE v12c9Vc61, v12c4Vc61(0x20)
    0x12cbS0xc61: v12cbVc61(0xe) = CONST 
    0x12cdS0xc61: v12cdVc61(0x24) = CONST 
    0x12d0S0xc61: v12d0Vc61 = ADD v12baVc61, v12cdVc61(0x24)
    0x12d1S0xc61: MSTORE v12d0Vc61, v12cbVc61(0xe)
    0x12d2S0xc61: v12d2Vc61(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xc61: v12e1Vc61(0x90) = CONST 
    0x12e3S0xc61: v12e3Vc61(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Vc61(0x90), v12d2Vc61(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xc61: v12e4Vc61(0x44) = CONST 
    0x12e7S0xc61: v12e7Vc61 = ADD v12baVc61, v12e4Vc61(0x44)
    0x12e8S0xc61: MSTORE v12e7Vc61, v12e3Vc61(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xc61: v12eaVc61 = MLOAD v12b7Vc61(0x40)
    0x12eeS0xc61: v12eeVc61(0x0) = SUB v12baVc61, v12eaVc61
    0x12efS0xc61: v12efVc61(0x64) = CONST 
    0x12f1S0xc61: v12f1Vc61(0x64) = ADD v12efVc61(0x64), v12eeVc61(0x0)
    0x12f3S0xc61: REVERT v12eaVc61, v12f1Vc61(0x64)

    Begin block 0x1d48B0xc61
    prev=[0x129eB0xc61], succ=[0xc69]
    =================================
    0x1d49S0xc61: JUMP vc62(0xc69)

    Begin block 0xc69
    prev=[0x1d48B0xc61], succ=[0x1ad7]
    =================================
    0xc6a: vc6a(0x0) = CONST 
    0xc6d: vc6d = SLOAD vc6a(0x0)
    0xc6e: vc6e(0x1) = CONST 
    0xc70: vc70(0x1) = CONST 
    0xc72: vc72(0xa0) = CONST 
    0xc74: vc74(0x10000000000000000000000000000000000000000) = SHL vc72(0xa0), vc70(0x1)
    0xc75: vc75(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc74(0x10000000000000000000000000000000000000000), vc6e(0x1)
    0xc78: vc78 = AND v45b, vc75(0xffffffffffffffffffffffffffffffffffffffff)
    0xc79: vc79(0x10000) = CONST 
    0xc7d: vc7d = MUL vc79(0x10000), vc78
    0xc7e: vc7e(0x10000) = CONST 
    0xc82: vc82(0x1) = CONST 
    0xc84: vc84(0xb0) = CONST 
    0xc86: vc86(0x100000000000000000000000000000000000000000000) = SHL vc84(0xb0), vc82(0x1)
    0xc87: vc87(0xffffffffffffffffffffffffffffffffffffffff0000) = SUB vc86(0x100000000000000000000000000000000000000000000), vc7e(0x10000)
    0xc88: vc88(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT vc87(0xffffffffffffffffffffffffffffffffffffffff0000)
    0xc8b: vc8b = AND vc6d, vc88(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff)
    0xc8f: vc8f = OR vc8b, vc7d
    0xc91: SSTORE vc6a(0x0), vc8f
    0xc92: JUMP v43b(0x1ad7)

    Begin block 0x1ad7
    prev=[0xc69], succ=[]
    =================================
    0x1ad8: STOP 

}

function keeper()() public {
    Begin block 0x460
    prev=[], succ=[0xc93]
    =================================
    0x461: v461(0x1af8) = CONST 
    0x464: v464(0xc93) = CONST 
    0x467: JUMP v464(0xc93)

    Begin block 0xc93
    prev=[0x460], succ=[0x1af8]
    =================================
    0xc94: vc94(0x2) = CONST 
    0xc96: vc96 = SLOAD vc94(0x2)
    0xc97: vc97(0x1) = CONST 
    0xc99: vc99(0x1) = CONST 
    0xc9b: vc9b(0xa0) = CONST 
    0xc9d: vc9d(0x10000000000000000000000000000000000000000) = SHL vc9b(0xa0), vc99(0x1)
    0xc9e: vc9e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc9d(0x10000000000000000000000000000000000000000), vc97(0x1)
    0xc9f: vc9f = AND vc9e(0xffffffffffffffffffffffffffffffffffffffff), vc96
    0xca1: JUMP v461(0x1af8)

    Begin block 0x1af8
    prev=[0xc93], succ=[]
    =================================
    0x1af9: v1af9(0x40) = CONST 
    0x1afc: v1afc = MLOAD v1af9(0x40)
    0x1afd: v1afd(0x1) = CONST 
    0x1aff: v1aff(0x1) = CONST 
    0x1b01: v1b01(0xa0) = CONST 
    0x1b03: v1b03(0x10000000000000000000000000000000000000000) = SHL v1b01(0xa0), v1aff(0x1)
    0x1b04: v1b04(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b03(0x10000000000000000000000000000000000000000), v1afd(0x1)
    0x1b07: v1b07 = AND vc9f, v1b04(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b09: MSTORE v1afc, v1b07
    0x1b0a: v1b0a = MLOAD v1af9(0x40)
    0x1b0e: v1b0e(0x0) = SUB v1afc, v1b0a
    0x1b0f: v1b0f(0x20) = CONST 
    0x1b11: v1b11(0x20) = ADD v1b0f(0x20), v1b0e(0x0)
    0x1b13: RETURN v1b0a, v1b11(0x20)

}

function earn(address,uint256)() public {
    Begin block 0x468
    prev=[], succ=[0x47a, 0x47e]
    =================================
    0x469: v469(0x1b33) = CONST 
    0x46c: v46c(0x4) = CONST 
    0x46f: v46f = CALLDATASIZE 
    0x470: v470 = SUB v46f, v46c(0x4)
    0x471: v471(0x40) = CONST 
    0x474: v474 = LT v470, v471(0x40)
    0x475: v475 = ISZERO v474
    0x476: v476(0x47e) = CONST 
    0x479: JUMPI v476(0x47e), v475

    Begin block 0x47a
    prev=[0x468], succ=[]
    =================================
    0x47a: v47a(0x0) = CONST 
    0x47d: REVERT v47a(0x0), v47a(0x0)

    Begin block 0x47e
    prev=[0x468], succ=[0xca2]
    =================================
    0x480: v480(0x1) = CONST 
    0x482: v482(0x1) = CONST 
    0x484: v484(0xa0) = CONST 
    0x486: v486(0x10000000000000000000000000000000000000000) = SHL v484(0xa0), v482(0x1)
    0x487: v487(0xffffffffffffffffffffffffffffffffffffffff) = SUB v486(0x10000000000000000000000000000000000000000), v480(0x1)
    0x489: v489 = CALLDATALOAD v46c(0x4)
    0x48a: v48a = AND v489, v487(0xffffffffffffffffffffffffffffffffffffffff)
    0x48c: v48c(0x20) = CONST 
    0x48e: v48e(0x24) = ADD v48c(0x20), v46c(0x4)
    0x48f: v48f = CALLDATALOAD v48e(0x24)
    0x490: v490(0xca2) = CONST 
    0x493: JUMP v490(0xca2)

    Begin block 0xca2
    prev=[0x47e], succ=[0xcef, 0xcf3]
    =================================
    0xca3: vca3(0x1) = CONST 
    0xca5: vca5(0x1) = CONST 
    0xca7: vca7(0xa0) = CONST 
    0xca9: vca9(0x10000000000000000000000000000000000000000) = SHL vca7(0xa0), vca5(0x1)
    0xcaa: vcaa(0xffffffffffffffffffffffffffffffffffffffff) = SUB vca9(0x10000000000000000000000000000000000000000), vca3(0x1)
    0xcad: vcad = AND v48a, vcaa(0xffffffffffffffffffffffffffffffffffffffff)
    0xcae: vcae(0x0) = CONST 
    0xcb2: MSTORE vcae(0x0), vcad
    0xcb3: vcb3(0x38) = CONST 
    0xcb5: vcb5(0x20) = CONST 
    0xcb9: MSTORE vcb5(0x20), vcb3(0x38)
    0xcba: vcba(0x40) = CONST 
    0xcbe: vcbe = SHA3 vcae(0x0), vcba(0x40)
    0xcbf: vcbf = SLOAD vcbe
    0xcc1: vcc1 = MLOAD vcba(0x40)
    0xcc2: vcc2(0x1f1fcd51) = CONST 
    0xcc7: vcc7(0xe0) = CONST 
    0xcc9: vcc9(0x1f1fcd5100000000000000000000000000000000000000000000000000000000) = SHL vcc7(0xe0), vcc2(0x1f1fcd51)
    0xccb: MSTORE vcc1, vcc9(0x1f1fcd5100000000000000000000000000000000000000000000000000000000)
    0xccd: vccd = MLOAD vcba(0x40)
    0xccf: vccf = AND vcaa(0xffffffffffffffffffffffffffffffffffffffff), vcbf
    0xcd3: vcd3(0x1f1fcd51) = CONST 
    0xcd9: vcd9(0x4) = CONST 
    0xcdd: vcdd = ADD vcc1, vcd9(0x4)
    0xce2: vce2(0x0) = SUB vcc1, vccd
    0xce3: vce3(0x4) = ADD vce2(0x0), vcd9(0x4)
    0xce7: vce7 = EXTCODESIZE vccf
    0xce8: vce8 = ISZERO vce7
    0xcea: vcea = ISZERO vce8
    0xceb: vceb(0xcf3) = CONST 
    0xcee: JUMPI vceb(0xcf3), vcea

    Begin block 0xcef
    prev=[0xca2], succ=[]
    =================================
    0xcef: vcef(0x0) = CONST 
    0xcf2: REVERT vcef(0x0), vcef(0x0)

    Begin block 0xcf3
    prev=[0xca2], succ=[0xcfe, 0xd07]
    =================================
    0xcf5: vcf5 = GAS 
    0xcf6: vcf6 = STATICCALL vcf5, vccf, vccd, vce3(0x4), vccd, vcb5(0x20)
    0xcf7: vcf7 = ISZERO vcf6
    0xcf9: vcf9 = ISZERO vcf7
    0xcfa: vcfa(0xd07) = CONST 
    0xcfd: JUMPI vcfa(0xd07), vcf9

    Begin block 0xcfe
    prev=[0xcf3], succ=[]
    =================================
    0xcfe: vcfe = RETURNDATASIZE 
    0xcff: vcff(0x0) = CONST 
    0xd02: RETURNDATACOPY vcff(0x0), vcff(0x0), vcfe
    0xd03: vd03 = RETURNDATASIZE 
    0xd04: vd04(0x0) = CONST 
    0xd06: REVERT vd04(0x0), vd03

    Begin block 0xd07
    prev=[0xcf3], succ=[0xd19, 0xd1d]
    =================================
    0xd0c: vd0c(0x40) = CONST 
    0xd0e: vd0e = MLOAD vd0c(0x40)
    0xd0f: vd0f = RETURNDATASIZE 
    0xd10: vd10(0x20) = CONST 
    0xd13: vd13 = LT vd0f, vd10(0x20)
    0xd14: vd14 = ISZERO vd13
    0xd15: vd15(0xd1d) = CONST 
    0xd18: JUMPI vd15(0xd1d), vd14

    Begin block 0xd19
    prev=[0xd07], succ=[]
    =================================
    0xd19: vd19(0x0) = CONST 
    0xd1c: REVERT vd19(0x0), vd19(0x0)

    Begin block 0xd1d
    prev=[0xd07], succ=[0x12f4B0xd1d]
    =================================
    0xd1f: vd1f = MLOAD vd0e
    0xd22: vd22(0xd2a) = CONST 
    0xd26: vd26(0x12f4) = CONST 
    0xd29: JUMP vd26(0x12f4), vd1f, vd22(0xd2a)

    Begin block 0x12f4B0xd1d
    prev=[0xd1d], succ=[0x1326B0xd1d, 0x1317B0xd1d]
    =================================
    0x12f5S0xd1d: v12f5Vd1d(0x1) = CONST 
    0x12f7S0xd1d: v12f7Vd1d(0x1) = CONST 
    0x12f9S0xd1d: v12f9Vd1d(0xa0) = CONST 
    0x12fbS0xd1d: v12fbVd1d(0x10000000000000000000000000000000000000000) = SHL v12f9Vd1d(0xa0), v12f7Vd1d(0x1)
    0x12fcS0xd1d: v12fcVd1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12fbVd1d(0x10000000000000000000000000000000000000000), v12f5Vd1d(0x1)
    0x12ffS0xd1d: v12ffVd1d = AND v12fcVd1d(0xffffffffffffffffffffffffffffffffffffffff), vd1f
    0x1300S0xd1d: v1300Vd1d(0x0) = CONST 
    0x1304S0xd1d: MSTORE v1300Vd1d(0x0), v12ffVd1d
    0x1305S0xd1d: v1305Vd1d(0x37) = CONST 
    0x1307S0xd1d: v1307Vd1d(0x20) = CONST 
    0x1309S0xd1d: MSTORE v1307Vd1d(0x20), v1305Vd1d(0x37)
    0x130aS0xd1d: v130aVd1d(0x40) = CONST 
    0x130dS0xd1d: v130dVd1d = SHA3 v1300Vd1d(0x0), v130aVd1d(0x40)
    0x130eS0xd1d: v130eVd1d = SLOAD v130dVd1d
    0x130fS0xd1d: v130fVd1d = AND v130eVd1d, v12fcVd1d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1310S0xd1d: v1310Vd1d = CALLER 
    0x1311S0xd1d: v1311Vd1d = EQ v1310Vd1d, v130fVd1d
    0x1313S0xd1d: v1313Vd1d(0x1326) = CONST 
    0x1316S0xd1d: JUMPI v1313Vd1d(0x1326), v1311Vd1d

    Begin block 0x1326B0xd1d
    prev=[0x12f4B0xd1d, 0x1317B0xd1d], succ=[0x133bB0xd1d, 0x132cB0xd1d]
    =================================
    0x1326_0x0S0xd1d: v1326_0Vd1d = PHI v1311Vd1d, v1325Vd1d
    0x1328S0xd1d: v1328Vd1d(0x133b) = CONST 
    0x132bS0xd1d: JUMPI v1328Vd1d(0x133b), v1326_0Vd1d

    Begin block 0x133bB0xd1d
    prev=[0x1326B0xd1d, 0x132cB0xd1d], succ=[0x1356B0xd1d, 0x1341B0xd1d]
    =================================
    0x133b_0x0S0xd1d: v133b_0Vd1d = PHI v1311Vd1d, v1325Vd1d, v133aVd1d
    0x133dS0xd1d: v133dVd1d(0x1356) = CONST 
    0x1340S0xd1d: JUMPI v133dVd1d(0x1356), v133b_0Vd1d

    Begin block 0x1356B0xd1d
    prev=[0x133bB0xd1d, 0x1341B0xd1d], succ=[0x135bB0xd1d, 0x1395B0xd1d]
    =================================
    0x1356_0x0S0xd1d: v1356_0Vd1d = PHI v1311Vd1d, v1325Vd1d, v133aVd1d, v1355Vd1d
    0x1357S0xd1d: v1357Vd1d(0x1395) = CONST 
    0x135aS0xd1d: JUMPI v1357Vd1d(0x1395), v1356_0Vd1d

    Begin block 0x135bB0xd1d
    prev=[0x1356B0xd1d], succ=[]
    =================================
    0x135bS0xd1d: v135bVd1d(0x40) = CONST 
    0x135eS0xd1d: v135eVd1d = MLOAD v135bVd1d(0x40)
    0x135fS0xd1d: v135fVd1d(0x461bcd) = CONST 
    0x1363S0xd1d: v1363Vd1d(0xe5) = CONST 
    0x1365S0xd1d: v1365Vd1d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1363Vd1d(0xe5), v135fVd1d(0x461bcd)
    0x1367S0xd1d: MSTORE v135eVd1d, v1365Vd1d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1368S0xd1d: v1368Vd1d(0x20) = CONST 
    0x136aS0xd1d: v136aVd1d(0x4) = CONST 
    0x136dS0xd1d: v136dVd1d = ADD v135eVd1d, v136aVd1d(0x4)
    0x136eS0xd1d: MSTORE v136dVd1d, v1368Vd1d(0x20)
    0x136fS0xd1d: v136fVd1d(0xb) = CONST 
    0x1371S0xd1d: v1371Vd1d(0x24) = CONST 
    0x1374S0xd1d: v1374Vd1d = ADD v135eVd1d, v1371Vd1d(0x24)
    0x1375S0xd1d: MSTORE v1374Vd1d, v136fVd1d(0xb)
    0x1376S0xd1d: v1376Vd1d(0x8585d5d1a1bdc9a5e9959) = CONST 
    0x1382S0xd1d: v1382Vd1d(0xaa) = CONST 
    0x1384S0xd1d: v1384Vd1d(0x21617574686f72697a6564000000000000000000000000000000000000000000) = SHL v1382Vd1d(0xaa), v1376Vd1d(0x8585d5d1a1bdc9a5e9959)
    0x1385S0xd1d: v1385Vd1d(0x44) = CONST 
    0x1388S0xd1d: v1388Vd1d = ADD v135eVd1d, v1385Vd1d(0x44)
    0x1389S0xd1d: MSTORE v1388Vd1d, v1384Vd1d(0x21617574686f72697a6564000000000000000000000000000000000000000000)
    0x138bS0xd1d: v138bVd1d = MLOAD v135bVd1d(0x40)
    0x138fS0xd1d: v138fVd1d(0x0) = SUB v135eVd1d, v138bVd1d
    0x1390S0xd1d: v1390Vd1d(0x64) = CONST 
    0x1392S0xd1d: v1392Vd1d(0x64) = ADD v1390Vd1d(0x64), v138fVd1d(0x0)
    0x1394S0xd1d: REVERT v138bVd1d, v1392Vd1d(0x64)

    Begin block 0x1395B0xd1d
    prev=[0x1356B0xd1d], succ=[0xd2a]
    =================================
    0x1397S0xd1d: JUMP vd22(0xd2a)

    Begin block 0xd2a
    prev=[0x1395B0xd1d], succ=[0xd44, 0xe10]
    =================================
    0xd2c: vd2c(0x1) = CONST 
    0xd2e: vd2e(0x1) = CONST 
    0xd30: vd30(0xa0) = CONST 
    0xd32: vd32(0x10000000000000000000000000000000000000000) = SHL vd30(0xa0), vd2e(0x1)
    0xd33: vd33(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd32(0x10000000000000000000000000000000000000000), vd2c(0x1)
    0xd34: vd34 = AND vd33(0xffffffffffffffffffffffffffffffffffffffff), v48a
    0xd36: vd36(0x1) = CONST 
    0xd38: vd38(0x1) = CONST 
    0xd3a: vd3a(0xa0) = CONST 
    0xd3c: vd3c(0x10000000000000000000000000000000000000000) = SHL vd3a(0xa0), vd38(0x1)
    0xd3d: vd3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd3c(0x10000000000000000000000000000000000000000), vd36(0x1)
    0xd3e: vd3e = AND vd3d(0xffffffffffffffffffffffffffffffffffffffff), vd1f
    0xd3f: vd3f = EQ vd3e, vd34
    0xd40: vd40(0xe10) = CONST 
    0xd43: JUMPI vd40(0xe10), vd3f

    Begin block 0xd44
    prev=[0xd2a], succ=[0xd79]
    =================================
    0xd44: vd44(0x1) = CONST 
    0xd46: vd46(0x1) = CONST 
    0xd48: vd48(0xa0) = CONST 
    0xd4a: vd4a(0x10000000000000000000000000000000000000000) = SHL vd48(0xa0), vd46(0x1)
    0xd4b: vd4b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd4a(0x10000000000000000000000000000000000000000), vd44(0x1)
    0xd4e: vd4e = AND v48a, vd4b(0xffffffffffffffffffffffffffffffffffffffff)
    0xd4f: vd4f(0x0) = CONST 
    0xd53: MSTORE vd4f(0x0), vd4e
    0xd54: vd54(0x39) = CONST 
    0xd56: vd56(0x20) = CONST 
    0xd5a: MSTORE vd56(0x20), vd54(0x39)
    0xd5b: vd5b(0x40) = CONST 
    0xd5f: vd5f = SHA3 vd4f(0x0), vd5b(0x40)
    0xd62: vd62 = AND vd4b(0xffffffffffffffffffffffffffffffffffffffff), vd1f
    0xd64: MSTORE vd4f(0x0), vd62
    0xd67: MSTORE vd56(0x20), vd5f
    0xd69: vd69 = SHA3 vd4f(0x0), vd5b(0x40)
    0xd6a: vd6a = SLOAD vd69
    0xd6d: vd6d = AND vd4b(0xffffffffffffffffffffffffffffffffffffffff), vd6a
    0xd6f: vd6f(0xd79) = CONST 
    0xd75: vd75(0x1398) = CONST 
    0xd78: CALLPRIVATE vd75(0x1398), v48f, vd6d, vd4e, vd6f(0xd79)

    Begin block 0xd79
    prev=[0xd44], succ=[0xdc4, 0xdc8]
    =================================
    0xd7b: vd7b(0x1) = CONST 
    0xd7d: vd7d(0x1) = CONST 
    0xd7f: vd7f(0xa0) = CONST 
    0xd81: vd81(0x10000000000000000000000000000000000000000) = SHL vd7f(0xa0), vd7d(0x1)
    0xd82: vd82(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd81(0x10000000000000000000000000000000000000000), vd7b(0x1)
    0xd83: vd83 = AND vd82(0xffffffffffffffffffffffffffffffffffffffff), vd6d
    0xd84: vd84(0xdef2489b) = CONST 
    0xd8a: vd8a(0x40) = CONST 
    0xd8c: vd8c = MLOAD vd8a(0x40)
    0xd8e: vd8e(0xffffffff) = CONST 
    0xd93: vd93(0xdef2489b) = AND vd8e(0xffffffff), vd84(0xdef2489b)
    0xd94: vd94(0xe0) = CONST 
    0xd96: vd96(0xdef2489b00000000000000000000000000000000000000000000000000000000) = SHL vd94(0xe0), vd93(0xdef2489b)
    0xd98: MSTORE vd8c, vd96(0xdef2489b00000000000000000000000000000000000000000000000000000000)
    0xd99: vd99(0x4) = CONST 
    0xd9b: vd9b = ADD vd99(0x4), vd8c
    0xd9e: vd9e(0x1) = CONST 
    0xda0: vda0(0x1) = CONST 
    0xda2: vda2(0xa0) = CONST 
    0xda4: vda4(0x10000000000000000000000000000000000000000) = SHL vda2(0xa0), vda0(0x1)
    0xda5: vda5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vda4(0x10000000000000000000000000000000000000000), vd9e(0x1)
    0xda6: vda6 = AND vda5(0xffffffffffffffffffffffffffffffffffffffff), vccf
    0xda8: MSTORE vd9b, vda6
    0xda9: vda9(0x20) = CONST 
    0xdab: vdab = ADD vda9(0x20), vd9b
    0xdaf: vdaf(0x20) = CONST 
    0xdb1: vdb1(0x40) = CONST 
    0xdb3: vdb3 = MLOAD vdb1(0x40)
    0xdb6: vdb6(0x24) = SUB vdab, vdb3
    0xdb8: vdb8(0x0) = CONST 
    0xdbc: vdbc = EXTCODESIZE vd83
    0xdbd: vdbd = ISZERO vdbc
    0xdbf: vdbf = ISZERO vdbd
    0xdc0: vdc0(0xdc8) = CONST 
    0xdc3: JUMPI vdc0(0xdc8), vdbf

    Begin block 0xdc4
    prev=[0xd79], succ=[]
    =================================
    0xdc4: vdc4(0x0) = CONST 
    0xdc7: REVERT vdc4(0x0), vdc4(0x0)

    Begin block 0xdc8
    prev=[0xd79], succ=[0xdd3, 0xddc]
    =================================
    0xdca: vdca = GAS 
    0xdcb: vdcb = CALL vdca, vd83, vdb8(0x0), vdb3, vdb6(0x24), vdb3, vdaf(0x20)
    0xdcc: vdcc = ISZERO vdcb
    0xdce: vdce = ISZERO vdcc
    0xdcf: vdcf(0xddc) = CONST 
    0xdd2: JUMPI vdcf(0xddc), vdce

    Begin block 0xdd3
    prev=[0xdc8], succ=[]
    =================================
    0xdd3: vdd3 = RETURNDATASIZE 
    0xdd4: vdd4(0x0) = CONST 
    0xdd7: RETURNDATACOPY vdd4(0x0), vdd4(0x0), vdd3
    0xdd8: vdd8 = RETURNDATASIZE 
    0xdd9: vdd9(0x0) = CONST 
    0xddb: REVERT vdd9(0x0), vdd8

    Begin block 0xddc
    prev=[0xdc8], succ=[0xdee, 0xdf2]
    =================================
    0xde1: vde1(0x40) = CONST 
    0xde3: vde3 = MLOAD vde1(0x40)
    0xde4: vde4 = RETURNDATASIZE 
    0xde5: vde5(0x20) = CONST 
    0xde8: vde8 = LT vde4, vde5(0x20)
    0xde9: vde9 = ISZERO vde8
    0xdea: vdea(0xdf2) = CONST 
    0xded: JUMPI vdea(0xdf2), vde9

    Begin block 0xdee
    prev=[0xddc], succ=[]
    =================================
    0xdee: vdee(0x0) = CONST 
    0xdf1: REVERT vdee(0x0), vdee(0x0)

    Begin block 0xdf2
    prev=[0xddc], succ=[0xe0a]
    =================================
    0xdf4: vdf4 = MLOAD vde3
    0xdf7: vdf7(0xe0a) = CONST 
    0xdfa: vdfa(0x1) = CONST 
    0xdfc: vdfc(0x1) = CONST 
    0xdfe: vdfe(0xa0) = CONST 
    0xe00: ve00(0x10000000000000000000000000000000000000000) = SHL vdfe(0xa0), vdfc(0x1)
    0xe01: ve01(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve00(0x10000000000000000000000000000000000000000), vdfa(0x1)
    0xe03: ve03 = AND vd1f, ve01(0xffffffffffffffffffffffffffffffffffffffff)
    0xe06: ve06(0x1398) = CONST 
    0xe09: CALLPRIVATE ve06(0x1398), vdf4, vccf, ve03, vdf7(0xe0a)

    Begin block 0xe0a
    prev=[0xdf2], succ=[0xe24]
    =================================
    0xe0c: ve0c(0xe24) = CONST 
    0xe0f: JUMP ve0c(0xe24)

    Begin block 0xe24
    prev=[0xe10, 0xe0a], succ=[0xe5b, 0xe5f]
    =================================
    0xe26: ve26(0x1) = CONST 
    0xe28: ve28(0x1) = CONST 
    0xe2a: ve2a(0xa0) = CONST 
    0xe2c: ve2c(0x10000000000000000000000000000000000000000) = SHL ve2a(0xa0), ve28(0x1)
    0xe2d: ve2d(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve2c(0x10000000000000000000000000000000000000000), ve26(0x1)
    0xe2e: ve2e = AND ve2d(0xffffffffffffffffffffffffffffffffffffffff), vccf
    0xe2f: ve2f(0xd0e30db0) = CONST 
    0xe34: ve34(0x40) = CONST 
    0xe36: ve36 = MLOAD ve34(0x40)
    0xe38: ve38(0xffffffff) = CONST 
    0xe3d: ve3d(0xd0e30db0) = AND ve38(0xffffffff), ve2f(0xd0e30db0)
    0xe3e: ve3e(0xe0) = CONST 
    0xe40: ve40(0xd0e30db000000000000000000000000000000000000000000000000000000000) = SHL ve3e(0xe0), ve3d(0xd0e30db0)
    0xe42: MSTORE ve36, ve40(0xd0e30db000000000000000000000000000000000000000000000000000000000)
    0xe43: ve43(0x4) = CONST 
    0xe45: ve45 = ADD ve43(0x4), ve36
    0xe46: ve46(0x0) = CONST 
    0xe48: ve48(0x40) = CONST 
    0xe4a: ve4a = MLOAD ve48(0x40)
    0xe4d: ve4d(0x4) = SUB ve45, ve4a
    0xe4f: ve4f(0x0) = CONST 
    0xe53: ve53 = EXTCODESIZE ve2e
    0xe54: ve54 = ISZERO ve53
    0xe56: ve56 = ISZERO ve54
    0xe57: ve57(0xe5f) = CONST 
    0xe5a: JUMPI ve57(0xe5f), ve56

    Begin block 0xe5b
    prev=[0xe24], succ=[]
    =================================
    0xe5b: ve5b(0x0) = CONST 
    0xe5e: REVERT ve5b(0x0), ve5b(0x0)

    Begin block 0xe5f
    prev=[0xe24], succ=[0xe6a, 0xe73]
    =================================
    0xe61: ve61 = GAS 
    0xe62: ve62 = CALL ve61, ve2e, ve4f(0x0), ve4a, ve4d(0x4), ve4a, ve46(0x0)
    0xe63: ve63 = ISZERO ve62
    0xe65: ve65 = ISZERO ve63
    0xe66: ve66(0xe73) = CONST 
    0xe69: JUMPI ve66(0xe73), ve65

    Begin block 0xe6a
    prev=[0xe5f], succ=[]
    =================================
    0xe6a: ve6a = RETURNDATASIZE 
    0xe6b: ve6b(0x0) = CONST 
    0xe6e: RETURNDATACOPY ve6b(0x0), ve6b(0x0), ve6a
    0xe6f: ve6f = RETURNDATASIZE 
    0xe70: ve70(0x0) = CONST 
    0xe72: REVERT ve70(0x0), ve6f

    Begin block 0xe73
    prev=[0xe5f], succ=[0x1b33]
    =================================
    0xe7c: JUMP v469(0x1b33)

    Begin block 0x1b33
    prev=[0xe73], succ=[]
    =================================
    0x1b34: STOP 

    Begin block 0xe10
    prev=[0xd2a], succ=[0xe24]
    =================================
    0xe11: ve11(0xe24) = CONST 
    0xe14: ve14(0x1) = CONST 
    0xe16: ve16(0x1) = CONST 
    0xe18: ve18(0xa0) = CONST 
    0xe1a: ve1a(0x10000000000000000000000000000000000000000) = SHL ve18(0xa0), ve16(0x1)
    0xe1b: ve1b(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve1a(0x10000000000000000000000000000000000000000), ve14(0x1)
    0xe1d: ve1d = AND v48a, ve1b(0xffffffffffffffffffffffffffffffffffffffff)
    0xe20: ve20(0x1398) = CONST 
    0xe23: CALLPRIVATE ve20(0x1398), v48f, vccf, ve1d, ve11(0xe24)

    Begin block 0x1341B0xd1d
    prev=[0x133bB0xd1d], succ=[0x1356B0xd1d]
    =================================
    0x1342S0xd1d: v1342Vd1d(0x0) = CONST 
    0x1344S0xd1d: v1344Vd1d = SLOAD v1342Vd1d(0x0)
    0x1345S0xd1d: v1345Vd1d(0x10000) = CONST 
    0x134aS0xd1d: v134aVd1d = DIV v1344Vd1d, v1345Vd1d(0x10000)
    0x134bS0xd1d: v134bVd1d(0x1) = CONST 
    0x134dS0xd1d: v134dVd1d(0x1) = CONST 
    0x134fS0xd1d: v134fVd1d(0xa0) = CONST 
    0x1351S0xd1d: v1351Vd1d(0x10000000000000000000000000000000000000000) = SHL v134fVd1d(0xa0), v134dVd1d(0x1)
    0x1352S0xd1d: v1352Vd1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1351Vd1d(0x10000000000000000000000000000000000000000), v134bVd1d(0x1)
    0x1353S0xd1d: v1353Vd1d = AND v1352Vd1d(0xffffffffffffffffffffffffffffffffffffffff), v134aVd1d
    0x1354S0xd1d: v1354Vd1d = CALLER 
    0x1355S0xd1d: v1355Vd1d = EQ v1354Vd1d, v1353Vd1d

    Begin block 0x132cB0xd1d
    prev=[0x1326B0xd1d], succ=[0x133bB0xd1d]
    =================================
    0x132dS0xd1d: v132dVd1d(0x1) = CONST 
    0x132fS0xd1d: v132fVd1d = SLOAD v132dVd1d(0x1)
    0x1330S0xd1d: v1330Vd1d(0x1) = CONST 
    0x1332S0xd1d: v1332Vd1d(0x1) = CONST 
    0x1334S0xd1d: v1334Vd1d(0xa0) = CONST 
    0x1336S0xd1d: v1336Vd1d(0x10000000000000000000000000000000000000000) = SHL v1334Vd1d(0xa0), v1332Vd1d(0x1)
    0x1337S0xd1d: v1337Vd1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1336Vd1d(0x10000000000000000000000000000000000000000), v1330Vd1d(0x1)
    0x1338S0xd1d: v1338Vd1d = AND v1337Vd1d(0xffffffffffffffffffffffffffffffffffffffff), v132fVd1d
    0x1339S0xd1d: v1339Vd1d = CALLER 
    0x133aS0xd1d: v133aVd1d = EQ v1339Vd1d, v1338Vd1d

    Begin block 0x1317B0xd1d
    prev=[0x12f4B0xd1d], succ=[0x1326B0xd1d]
    =================================
    0x1318S0xd1d: v1318Vd1d(0x2) = CONST 
    0x131aS0xd1d: v131aVd1d = SLOAD v1318Vd1d(0x2)
    0x131bS0xd1d: v131bVd1d(0x1) = CONST 
    0x131dS0xd1d: v131dVd1d(0x1) = CONST 
    0x131fS0xd1d: v131fVd1d(0xa0) = CONST 
    0x1321S0xd1d: v1321Vd1d(0x10000000000000000000000000000000000000000) = SHL v131fVd1d(0xa0), v131dVd1d(0x1)
    0x1322S0xd1d: v1322Vd1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1321Vd1d(0x10000000000000000000000000000000000000000), v131bVd1d(0x1)
    0x1323S0xd1d: v1323Vd1d = AND v1322Vd1d(0xffffffffffffffffffffffffffffffffffffffff), v131aVd1d
    0x1324S0xd1d: v1324Vd1d = CALLER 
    0x1325S0xd1d: v1325Vd1d = EQ v1324Vd1d, v1323Vd1d

}

function approveStrategy(address,address)() public {
    Begin block 0x494
    prev=[], succ=[0x4a6, 0x4aa]
    =================================
    0x495: v495(0x1b54) = CONST 
    0x498: v498(0x4) = CONST 
    0x49b: v49b = CALLDATASIZE 
    0x49c: v49c = SUB v49b, v498(0x4)
    0x49d: v49d(0x40) = CONST 
    0x4a0: v4a0 = LT v49c, v49d(0x40)
    0x4a1: v4a1 = ISZERO v4a0
    0x4a2: v4a2(0x4aa) = CONST 
    0x4a5: JUMPI v4a2(0x4aa), v4a1

    Begin block 0x4a6
    prev=[0x494], succ=[]
    =================================
    0x4a6: v4a6(0x0) = CONST 
    0x4a9: REVERT v4a6(0x0), v4a6(0x0)

    Begin block 0x4aa
    prev=[0x494], succ=[0xe7d]
    =================================
    0x4ac: v4ac(0x1) = CONST 
    0x4ae: v4ae(0x1) = CONST 
    0x4b0: v4b0(0xa0) = CONST 
    0x4b2: v4b2(0x10000000000000000000000000000000000000000) = SHL v4b0(0xa0), v4ae(0x1)
    0x4b3: v4b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b2(0x10000000000000000000000000000000000000000), v4ac(0x1)
    0x4b5: v4b5 = CALLDATALOAD v498(0x4)
    0x4b7: v4b7 = AND v4b3(0xffffffffffffffffffffffffffffffffffffffff), v4b5
    0x4b9: v4b9(0x20) = CONST 
    0x4bb: v4bb(0x24) = ADD v4b9(0x20), v498(0x4)
    0x4bc: v4bc = CALLDATALOAD v4bb(0x24)
    0x4bd: v4bd = AND v4bc, v4b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x4be: v4be(0xe7d) = CONST 
    0x4c1: JUMP v4be(0xe7d)

    Begin block 0xe7d
    prev=[0x4aa], succ=[0x129eB0xe7d]
    =================================
    0xe7e: ve7e(0xe85) = CONST 
    0xe81: ve81(0x129e) = CONST 
    0xe84: JUMP ve81(0x129e), ve7e(0xe85)

    Begin block 0x129eB0xe7d
    prev=[0xe7d], succ=[0x12b7B0xe7d, 0x1d48B0xe7d]
    =================================
    0x129fS0xe7d: v129fVe7d(0x0) = CONST 
    0x12a1S0xe7d: v12a1Ve7d = SLOAD v129fVe7d(0x0)
    0x12a2S0xe7d: v12a2Ve7d(0x10000) = CONST 
    0x12a7S0xe7d: v12a7Ve7d = DIV v12a1Ve7d, v12a2Ve7d(0x10000)
    0x12a8S0xe7d: v12a8Ve7d(0x1) = CONST 
    0x12aaS0xe7d: v12aaVe7d(0x1) = CONST 
    0x12acS0xe7d: v12acVe7d(0xa0) = CONST 
    0x12aeS0xe7d: v12aeVe7d(0x10000000000000000000000000000000000000000) = SHL v12acVe7d(0xa0), v12aaVe7d(0x1)
    0x12afS0xe7d: v12afVe7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVe7d(0x10000000000000000000000000000000000000000), v12a8Ve7d(0x1)
    0x12b0S0xe7d: v12b0Ve7d = AND v12afVe7d(0xffffffffffffffffffffffffffffffffffffffff), v12a7Ve7d
    0x12b1S0xe7d: v12b1Ve7d = CALLER 
    0x12b2S0xe7d: v12b2Ve7d = EQ v12b1Ve7d, v12b0Ve7d
    0x12b3S0xe7d: v12b3Ve7d(0x1d48) = CONST 
    0x12b6S0xe7d: JUMPI v12b3Ve7d(0x1d48), v12b2Ve7d

    Begin block 0x12b7B0xe7d
    prev=[0x129eB0xe7d], succ=[]
    =================================
    0x12b7S0xe7d: v12b7Ve7d(0x40) = CONST 
    0x12baS0xe7d: v12baVe7d = MLOAD v12b7Ve7d(0x40)
    0x12bbS0xe7d: v12bbVe7d(0x461bcd) = CONST 
    0x12bfS0xe7d: v12bfVe7d(0xe5) = CONST 
    0x12c1S0xe7d: v12c1Ve7d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVe7d(0xe5), v12bbVe7d(0x461bcd)
    0x12c3S0xe7d: MSTORE v12baVe7d, v12c1Ve7d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xe7d: v12c4Ve7d(0x20) = CONST 
    0x12c6S0xe7d: v12c6Ve7d(0x4) = CONST 
    0x12c9S0xe7d: v12c9Ve7d = ADD v12baVe7d, v12c6Ve7d(0x4)
    0x12caS0xe7d: MSTORE v12c9Ve7d, v12c4Ve7d(0x20)
    0x12cbS0xe7d: v12cbVe7d(0xe) = CONST 
    0x12cdS0xe7d: v12cdVe7d(0x24) = CONST 
    0x12d0S0xe7d: v12d0Ve7d = ADD v12baVe7d, v12cdVe7d(0x24)
    0x12d1S0xe7d: MSTORE v12d0Ve7d, v12cbVe7d(0xe)
    0x12d2S0xe7d: v12d2Ve7d(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xe7d: v12e1Ve7d(0x90) = CONST 
    0x12e3S0xe7d: v12e3Ve7d(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Ve7d(0x90), v12d2Ve7d(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xe7d: v12e4Ve7d(0x44) = CONST 
    0x12e7S0xe7d: v12e7Ve7d = ADD v12baVe7d, v12e4Ve7d(0x44)
    0x12e8S0xe7d: MSTORE v12e7Ve7d, v12e3Ve7d(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xe7d: v12eaVe7d = MLOAD v12b7Ve7d(0x40)
    0x12eeS0xe7d: v12eeVe7d(0x0) = SUB v12baVe7d, v12eaVe7d
    0x12efS0xe7d: v12efVe7d(0x64) = CONST 
    0x12f1S0xe7d: v12f1Ve7d(0x64) = ADD v12efVe7d(0x64), v12eeVe7d(0x0)
    0x12f3S0xe7d: REVERT v12eaVe7d, v12f1Ve7d(0x64)

    Begin block 0x1d48B0xe7d
    prev=[0x129eB0xe7d], succ=[0xe85]
    =================================
    0x1d49S0xe7d: JUMP ve7e(0xe85)

    Begin block 0xe85
    prev=[0x1d48B0xe7d], succ=[0x1b54]
    =================================
    0xe86: ve86(0x1) = CONST 
    0xe88: ve88(0x1) = CONST 
    0xe8a: ve8a(0xa0) = CONST 
    0xe8c: ve8c(0x10000000000000000000000000000000000000000) = SHL ve8a(0xa0), ve88(0x1)
    0xe8d: ve8d(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve8c(0x10000000000000000000000000000000000000000), ve86(0x1)
    0xe90: ve90 = AND ve8d(0xffffffffffffffffffffffffffffffffffffffff), v4b7
    0xe91: ve91(0x0) = CONST 
    0xe95: MSTORE ve91(0x0), ve90
    0xe96: ve96(0x3a) = CONST 
    0xe98: ve98(0x20) = CONST 
    0xe9c: MSTORE ve98(0x20), ve96(0x3a)
    0xe9d: ve9d(0x40) = CONST 
    0xea1: vea1 = SHA3 ve91(0x0), ve9d(0x40)
    0xea5: vea5 = AND ve8d(0xffffffffffffffffffffffffffffffffffffffff), v4bd
    0xea7: MSTORE ve91(0x0), vea5
    0xeab: MSTORE ve98(0x20), vea1
    0xeac: veac = SHA3 ve91(0x0), ve9d(0x40)
    0xeae: veae = SLOAD veac
    0xeaf: veaf(0xff) = CONST 
    0xeb1: veb1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT veaf(0xff)
    0xeb2: veb2 = AND veb1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), veae
    0xeb3: veb3(0x1) = CONST 
    0xeb5: veb5 = OR veb3(0x1), veb2
    0xeb7: SSTORE veac, veb5
    0xeb8: JUMP v495(0x1b54)

    Begin block 0x1b54
    prev=[0xe85], succ=[]
    =================================
    0x1b55: STOP 

}

function inCaseTokensGetStuck(address,uint256)() public {
    Begin block 0x4c2
    prev=[], succ=[0x4d4, 0x4d8]
    =================================
    0x4c3: v4c3(0x1b75) = CONST 
    0x4c6: v4c6(0x4) = CONST 
    0x4c9: v4c9 = CALLDATASIZE 
    0x4ca: v4ca = SUB v4c9, v4c6(0x4)
    0x4cb: v4cb(0x40) = CONST 
    0x4ce: v4ce = LT v4ca, v4cb(0x40)
    0x4cf: v4cf = ISZERO v4ce
    0x4d0: v4d0(0x4d8) = CONST 
    0x4d3: JUMPI v4d0(0x4d8), v4cf

    Begin block 0x4d4
    prev=[0x4c2], succ=[]
    =================================
    0x4d4: v4d4(0x0) = CONST 
    0x4d7: REVERT v4d4(0x0), v4d4(0x0)

    Begin block 0x4d8
    prev=[0x4c2], succ=[0xeb9]
    =================================
    0x4da: v4da(0x1) = CONST 
    0x4dc: v4dc(0x1) = CONST 
    0x4de: v4de(0xa0) = CONST 
    0x4e0: v4e0(0x10000000000000000000000000000000000000000) = SHL v4de(0xa0), v4dc(0x1)
    0x4e1: v4e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e0(0x10000000000000000000000000000000000000000), v4da(0x1)
    0x4e3: v4e3 = CALLDATALOAD v4c6(0x4)
    0x4e4: v4e4 = AND v4e3, v4e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e6: v4e6(0x20) = CONST 
    0x4e8: v4e8(0x24) = ADD v4e6(0x20), v4c6(0x4)
    0x4e9: v4e9 = CALLDATALOAD v4e8(0x24)
    0x4ea: v4ea(0xeb9) = CONST 
    0x4ed: JUMP v4ea(0xeb9)

    Begin block 0xeb9
    prev=[0x4d8], succ=[0xec1]
    =================================
    0xeba: veba(0xec1) = CONST 
    0xebd: vebd(0x1222) = CONST 
    0xec0: CALLPRIVATE vebd(0x1222), veba(0xec1)

    Begin block 0xec1
    prev=[0xeb9], succ=[0xed5]
    =================================
    0xec2: vec2(0xed5) = CONST 
    0xec5: vec5(0x1) = CONST 
    0xec7: vec7(0x1) = CONST 
    0xec9: vec9(0xa0) = CONST 
    0xecb: vecb(0x10000000000000000000000000000000000000000) = SHL vec9(0xa0), vec7(0x1)
    0xecc: vecc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vecb(0x10000000000000000000000000000000000000000), vec5(0x1)
    0xece: vece = AND v4e4, vecc(0xffffffffffffffffffffffffffffffffffffffff)
    0xecf: vecf = CALLER 
    0xed1: ved1(0x1398) = CONST 
    0xed4: CALLPRIVATE ved1(0x1398), v4e9, vecf, vece, vec2(0xed5)

    Begin block 0xed5
    prev=[0xec1], succ=[0x1b75]
    =================================
    0xed8: JUMP v4c3(0x1b75)

    Begin block 0x1b75
    prev=[0xed5], succ=[]
    =================================
    0x1b76: STOP 

}

function setStrategist(address)() public {
    Begin block 0x4ee
    prev=[], succ=[0x500, 0x504]
    =================================
    0x4ef: v4ef(0x1b96) = CONST 
    0x4f2: v4f2(0x4) = CONST 
    0x4f5: v4f5 = CALLDATASIZE 
    0x4f6: v4f6 = SUB v4f5, v4f2(0x4)
    0x4f7: v4f7(0x20) = CONST 
    0x4fa: v4fa = LT v4f6, v4f7(0x20)
    0x4fb: v4fb = ISZERO v4fa
    0x4fc: v4fc(0x504) = CONST 
    0x4ff: JUMPI v4fc(0x504), v4fb

    Begin block 0x500
    prev=[0x4ee], succ=[]
    =================================
    0x500: v500(0x0) = CONST 
    0x503: REVERT v500(0x0), v500(0x0)

    Begin block 0x504
    prev=[0x4ee], succ=[0xed9]
    =================================
    0x506: v506 = CALLDATALOAD v4f2(0x4)
    0x507: v507(0x1) = CONST 
    0x509: v509(0x1) = CONST 
    0x50b: v50b(0xa0) = CONST 
    0x50d: v50d(0x10000000000000000000000000000000000000000) = SHL v50b(0xa0), v509(0x1)
    0x50e: v50e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v50d(0x10000000000000000000000000000000000000000), v507(0x1)
    0x50f: v50f = AND v50e(0xffffffffffffffffffffffffffffffffffffffff), v506
    0x510: v510(0xed9) = CONST 
    0x513: JUMP v510(0xed9)

    Begin block 0xed9
    prev=[0x504], succ=[0x129eB0xed9]
    =================================
    0xeda: veda(0xee1) = CONST 
    0xedd: vedd(0x129e) = CONST 
    0xee0: JUMP vedd(0x129e), veda(0xee1)

    Begin block 0x129eB0xed9
    prev=[0xed9], succ=[0x12b7B0xed9, 0x1d48B0xed9]
    =================================
    0x129fS0xed9: v129fVed9(0x0) = CONST 
    0x12a1S0xed9: v12a1Ved9 = SLOAD v129fVed9(0x0)
    0x12a2S0xed9: v12a2Ved9(0x10000) = CONST 
    0x12a7S0xed9: v12a7Ved9 = DIV v12a1Ved9, v12a2Ved9(0x10000)
    0x12a8S0xed9: v12a8Ved9(0x1) = CONST 
    0x12aaS0xed9: v12aaVed9(0x1) = CONST 
    0x12acS0xed9: v12acVed9(0xa0) = CONST 
    0x12aeS0xed9: v12aeVed9(0x10000000000000000000000000000000000000000) = SHL v12acVed9(0xa0), v12aaVed9(0x1)
    0x12afS0xed9: v12afVed9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVed9(0x10000000000000000000000000000000000000000), v12a8Ved9(0x1)
    0x12b0S0xed9: v12b0Ved9 = AND v12afVed9(0xffffffffffffffffffffffffffffffffffffffff), v12a7Ved9
    0x12b1S0xed9: v12b1Ved9 = CALLER 
    0x12b2S0xed9: v12b2Ved9 = EQ v12b1Ved9, v12b0Ved9
    0x12b3S0xed9: v12b3Ved9(0x1d48) = CONST 
    0x12b6S0xed9: JUMPI v12b3Ved9(0x1d48), v12b2Ved9

    Begin block 0x12b7B0xed9
    prev=[0x129eB0xed9], succ=[]
    =================================
    0x12b7S0xed9: v12b7Ved9(0x40) = CONST 
    0x12baS0xed9: v12baVed9 = MLOAD v12b7Ved9(0x40)
    0x12bbS0xed9: v12bbVed9(0x461bcd) = CONST 
    0x12bfS0xed9: v12bfVed9(0xe5) = CONST 
    0x12c1S0xed9: v12c1Ved9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVed9(0xe5), v12bbVed9(0x461bcd)
    0x12c3S0xed9: MSTORE v12baVed9, v12c1Ved9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xed9: v12c4Ved9(0x20) = CONST 
    0x12c6S0xed9: v12c6Ved9(0x4) = CONST 
    0x12c9S0xed9: v12c9Ved9 = ADD v12baVed9, v12c6Ved9(0x4)
    0x12caS0xed9: MSTORE v12c9Ved9, v12c4Ved9(0x20)
    0x12cbS0xed9: v12cbVed9(0xe) = CONST 
    0x12cdS0xed9: v12cdVed9(0x24) = CONST 
    0x12d0S0xed9: v12d0Ved9 = ADD v12baVed9, v12cdVed9(0x24)
    0x12d1S0xed9: MSTORE v12d0Ved9, v12cbVed9(0xe)
    0x12d2S0xed9: v12d2Ved9(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xed9: v12e1Ved9(0x90) = CONST 
    0x12e3S0xed9: v12e3Ved9(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Ved9(0x90), v12d2Ved9(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xed9: v12e4Ved9(0x44) = CONST 
    0x12e7S0xed9: v12e7Ved9 = ADD v12baVed9, v12e4Ved9(0x44)
    0x12e8S0xed9: MSTORE v12e7Ved9, v12e3Ved9(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xed9: v12eaVed9 = MLOAD v12b7Ved9(0x40)
    0x12eeS0xed9: v12eeVed9(0x0) = SUB v12baVed9, v12eaVed9
    0x12efS0xed9: v12efVed9(0x64) = CONST 
    0x12f1S0xed9: v12f1Ved9(0x64) = ADD v12efVed9(0x64), v12eeVed9(0x0)
    0x12f3S0xed9: REVERT v12eaVed9, v12f1Ved9(0x64)

    Begin block 0x1d48B0xed9
    prev=[0x129eB0xed9], succ=[0xee1]
    =================================
    0x1d49S0xed9: JUMP veda(0xee1)

    Begin block 0xee1
    prev=[0x1d48B0xed9], succ=[0x1b96]
    =================================
    0xee2: vee2(0x1) = CONST 
    0xee5: vee5 = SLOAD vee2(0x1)
    0xee6: vee6(0x1) = CONST 
    0xee8: vee8(0x1) = CONST 
    0xeea: veea(0xa0) = CONST 
    0xeec: veec(0x10000000000000000000000000000000000000000) = SHL veea(0xa0), vee8(0x1)
    0xeed: veed(0xffffffffffffffffffffffffffffffffffffffff) = SUB veec(0x10000000000000000000000000000000000000000), vee6(0x1)
    0xeee: veee(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT veed(0xffffffffffffffffffffffffffffffffffffffff)
    0xeef: veef = AND veee(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vee5
    0xef0: vef0(0x1) = CONST 
    0xef2: vef2(0x1) = CONST 
    0xef4: vef4(0xa0) = CONST 
    0xef6: vef6(0x10000000000000000000000000000000000000000) = SHL vef4(0xa0), vef2(0x1)
    0xef7: vef7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vef6(0x10000000000000000000000000000000000000000), vef0(0x1)
    0xefb: vefb = AND vef7(0xffffffffffffffffffffffffffffffffffffffff), v50f
    0xeff: veff = OR vefb, veef
    0xf01: SSTORE vee2(0x1), veff
    0xf02: JUMP v4ef(0x1b96)

    Begin block 0x1b96
    prev=[0xee1], succ=[]
    =================================
    0x1b97: STOP 

}

function setConverter(address,address,address)() public {
    Begin block 0x514
    prev=[], succ=[0x526, 0x52a]
    =================================
    0x515: v515(0x1bb7) = CONST 
    0x518: v518(0x4) = CONST 
    0x51b: v51b = CALLDATASIZE 
    0x51c: v51c = SUB v51b, v518(0x4)
    0x51d: v51d(0x60) = CONST 
    0x520: v520 = LT v51c, v51d(0x60)
    0x521: v521 = ISZERO v520
    0x522: v522(0x52a) = CONST 
    0x525: JUMPI v522(0x52a), v521

    Begin block 0x526
    prev=[0x514], succ=[]
    =================================
    0x526: v526(0x0) = CONST 
    0x529: REVERT v526(0x0), v526(0x0)

    Begin block 0x52a
    prev=[0x514], succ=[0xf03]
    =================================
    0x52c: v52c(0x1) = CONST 
    0x52e: v52e(0x1) = CONST 
    0x530: v530(0xa0) = CONST 
    0x532: v532(0x10000000000000000000000000000000000000000) = SHL v530(0xa0), v52e(0x1)
    0x533: v533(0xffffffffffffffffffffffffffffffffffffffff) = SUB v532(0x10000000000000000000000000000000000000000), v52c(0x1)
    0x535: v535 = CALLDATALOAD v518(0x4)
    0x537: v537 = AND v533(0xffffffffffffffffffffffffffffffffffffffff), v535
    0x539: v539(0x20) = CONST 
    0x53c: v53c(0x24) = ADD v518(0x4), v539(0x20)
    0x53d: v53d = CALLDATALOAD v53c(0x24)
    0x53f: v53f = AND v533(0xffffffffffffffffffffffffffffffffffffffff), v53d
    0x541: v541(0x40) = CONST 
    0x545: v545(0x44) = ADD v518(0x4), v541(0x40)
    0x546: v546 = CALLDATALOAD v545(0x44)
    0x547: v547 = AND v546, v533(0xffffffffffffffffffffffffffffffffffffffff)
    0x548: v548(0xf03) = CONST 
    0x54b: JUMP v548(0xf03)

    Begin block 0xf03
    prev=[0x52a], succ=[0xf0b]
    =================================
    0xf04: vf04(0xf0b) = CONST 
    0xf07: vf07(0x1222) = CONST 
    0xf0a: CALLPRIVATE vf07(0x1222), vf04(0xf0b)

    Begin block 0xf0b
    prev=[0xf03], succ=[0x1bb7]
    =================================
    0xf0c: vf0c(0x1) = CONST 
    0xf0e: vf0e(0x1) = CONST 
    0xf10: vf10(0xa0) = CONST 
    0xf12: vf12(0x10000000000000000000000000000000000000000) = SHL vf10(0xa0), vf0e(0x1)
    0xf13: vf13(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf12(0x10000000000000000000000000000000000000000), vf0c(0x1)
    0xf16: vf16 = AND vf13(0xffffffffffffffffffffffffffffffffffffffff), v537
    0xf17: vf17(0x0) = CONST 
    0xf1b: MSTORE vf17(0x0), vf16
    0xf1c: vf1c(0x39) = CONST 
    0xf1e: vf1e(0x20) = CONST 
    0xf22: MSTORE vf1e(0x20), vf1c(0x39)
    0xf23: vf23(0x40) = CONST 
    0xf27: vf27 = SHA3 vf17(0x0), vf23(0x40)
    0xf2a: vf2a = AND vf13(0xffffffffffffffffffffffffffffffffffffffff), v53f
    0xf2c: MSTORE vf17(0x0), vf2a
    0xf2f: MSTORE vf1e(0x20), vf27
    0xf33: vf33 = SHA3 vf17(0x0), vf23(0x40)
    0xf35: vf35 = SLOAD vf33
    0xf36: vf36(0x1) = CONST 
    0xf38: vf38(0x1) = CONST 
    0xf3a: vf3a(0xa0) = CONST 
    0xf3c: vf3c(0x10000000000000000000000000000000000000000) = SHL vf3a(0xa0), vf38(0x1)
    0xf3d: vf3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf3c(0x10000000000000000000000000000000000000000), vf36(0x1)
    0xf3e: vf3e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vf3d(0xffffffffffffffffffffffffffffffffffffffff)
    0xf3f: vf3f = AND vf3e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vf35
    0xf43: vf43 = AND vf13(0xffffffffffffffffffffffffffffffffffffffff), v547
    0xf44: vf44 = OR vf43, vf3f
    0xf46: SSTORE vf33, vf44
    0xf47: JUMP v515(0x1bb7)

    Begin block 0x1bb7
    prev=[0xf0b], succ=[]
    =================================
    0x1bb8: STOP 

}

function converters(address,address)() public {
    Begin block 0x54c
    prev=[], succ=[0x55e, 0x562]
    =================================
    0x54d: v54d(0x1bd8) = CONST 
    0x550: v550(0x4) = CONST 
    0x553: v553 = CALLDATASIZE 
    0x554: v554 = SUB v553, v550(0x4)
    0x555: v555(0x40) = CONST 
    0x558: v558 = LT v554, v555(0x40)
    0x559: v559 = ISZERO v558
    0x55a: v55a(0x562) = CONST 
    0x55d: JUMPI v55a(0x562), v559

    Begin block 0x55e
    prev=[0x54c], succ=[]
    =================================
    0x55e: v55e(0x0) = CONST 
    0x561: REVERT v55e(0x0), v55e(0x0)

    Begin block 0x562
    prev=[0x54c], succ=[0xf48]
    =================================
    0x564: v564(0x1) = CONST 
    0x566: v566(0x1) = CONST 
    0x568: v568(0xa0) = CONST 
    0x56a: v56a(0x10000000000000000000000000000000000000000) = SHL v568(0xa0), v566(0x1)
    0x56b: v56b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v56a(0x10000000000000000000000000000000000000000), v564(0x1)
    0x56d: v56d = CALLDATALOAD v550(0x4)
    0x56f: v56f = AND v56b(0xffffffffffffffffffffffffffffffffffffffff), v56d
    0x571: v571(0x20) = CONST 
    0x573: v573(0x24) = ADD v571(0x20), v550(0x4)
    0x574: v574 = CALLDATALOAD v573(0x24)
    0x575: v575 = AND v574, v56b(0xffffffffffffffffffffffffffffffffffffffff)
    0x576: v576(0xf48) = CONST 
    0x579: JUMP v576(0xf48)

    Begin block 0xf48
    prev=[0x562], succ=[0x1bd8]
    =================================
    0xf49: vf49(0x39) = CONST 
    0xf4b: vf4b(0x20) = CONST 
    0xf4f: MSTORE vf4b(0x20), vf49(0x39)
    0xf50: vf50(0x0) = CONST 
    0xf54: MSTORE vf50(0x0), v56f
    0xf55: vf55(0x40) = CONST 
    0xf59: vf59 = SHA3 vf50(0x0), vf55(0x40)
    0xf5c: MSTORE vf4b(0x20), vf59
    0xf5f: MSTORE vf50(0x0), v575
    0xf61: vf61 = SHA3 vf50(0x0), vf55(0x40)
    0xf62: vf62 = SLOAD vf61
    0xf63: vf63(0x1) = CONST 
    0xf65: vf65(0x1) = CONST 
    0xf67: vf67(0xa0) = CONST 
    0xf69: vf69(0x10000000000000000000000000000000000000000) = SHL vf67(0xa0), vf65(0x1)
    0xf6a: vf6a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf69(0x10000000000000000000000000000000000000000), vf63(0x1)
    0xf6b: vf6b = AND vf6a(0xffffffffffffffffffffffffffffffffffffffff), vf62
    0xf6d: JUMP v54d(0x1bd8)

    Begin block 0x1bd8
    prev=[0xf48], succ=[]
    =================================
    0x1bd9: v1bd9(0x40) = CONST 
    0x1bdc: v1bdc = MLOAD v1bd9(0x40)
    0x1bdd: v1bdd(0x1) = CONST 
    0x1bdf: v1bdf(0x1) = CONST 
    0x1be1: v1be1(0xa0) = CONST 
    0x1be3: v1be3(0x10000000000000000000000000000000000000000) = SHL v1be1(0xa0), v1bdf(0x1)
    0x1be4: v1be4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1be3(0x10000000000000000000000000000000000000000), v1bdd(0x1)
    0x1be7: v1be7 = AND vf6b, v1be4(0xffffffffffffffffffffffffffffffffffffffff)
    0x1be9: MSTORE v1bdc, v1be7
    0x1bea: v1bea = MLOAD v1bd9(0x40)
    0x1bee: v1bee(0x0) = SUB v1bdc, v1bea
    0x1bef: v1bef(0x20) = CONST 
    0x1bf1: v1bf1(0x20) = ADD v1bef(0x20), v1bee(0x0)
    0x1bf3: RETURN v1bea, v1bf1(0x20)

}

function setRewards(address)() public {
    Begin block 0x57a
    prev=[], succ=[0x58c, 0x590]
    =================================
    0x57b: v57b(0x1c13) = CONST 
    0x57e: v57e(0x4) = CONST 
    0x581: v581 = CALLDATASIZE 
    0x582: v582 = SUB v581, v57e(0x4)
    0x583: v583(0x20) = CONST 
    0x586: v586 = LT v582, v583(0x20)
    0x587: v587 = ISZERO v586
    0x588: v588(0x590) = CONST 
    0x58b: JUMPI v588(0x590), v587

    Begin block 0x58c
    prev=[0x57a], succ=[]
    =================================
    0x58c: v58c(0x0) = CONST 
    0x58f: REVERT v58c(0x0), v58c(0x0)

    Begin block 0x590
    prev=[0x57a], succ=[0xf6e]
    =================================
    0x592: v592 = CALLDATALOAD v57e(0x4)
    0x593: v593(0x1) = CONST 
    0x595: v595(0x1) = CONST 
    0x597: v597(0xa0) = CONST 
    0x599: v599(0x10000000000000000000000000000000000000000) = SHL v597(0xa0), v595(0x1)
    0x59a: v59a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v599(0x10000000000000000000000000000000000000000), v593(0x1)
    0x59b: v59b = AND v59a(0xffffffffffffffffffffffffffffffffffffffff), v592
    0x59c: v59c(0xf6e) = CONST 
    0x59f: JUMP v59c(0xf6e)

    Begin block 0xf6e
    prev=[0x590], succ=[0x129eB0xf6e]
    =================================
    0xf6f: vf6f(0xf76) = CONST 
    0xf72: vf72(0x129e) = CONST 
    0xf75: JUMP vf72(0x129e), vf6f(0xf76)

    Begin block 0x129eB0xf6e
    prev=[0xf6e], succ=[0x12b7B0xf6e, 0x1d48B0xf6e]
    =================================
    0x129fS0xf6e: v129fVf6e(0x0) = CONST 
    0x12a1S0xf6e: v12a1Vf6e = SLOAD v129fVf6e(0x0)
    0x12a2S0xf6e: v12a2Vf6e(0x10000) = CONST 
    0x12a7S0xf6e: v12a7Vf6e = DIV v12a1Vf6e, v12a2Vf6e(0x10000)
    0x12a8S0xf6e: v12a8Vf6e(0x1) = CONST 
    0x12aaS0xf6e: v12aaVf6e(0x1) = CONST 
    0x12acS0xf6e: v12acVf6e(0xa0) = CONST 
    0x12aeS0xf6e: v12aeVf6e(0x10000000000000000000000000000000000000000) = SHL v12acVf6e(0xa0), v12aaVf6e(0x1)
    0x12afS0xf6e: v12afVf6e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12aeVf6e(0x10000000000000000000000000000000000000000), v12a8Vf6e(0x1)
    0x12b0S0xf6e: v12b0Vf6e = AND v12afVf6e(0xffffffffffffffffffffffffffffffffffffffff), v12a7Vf6e
    0x12b1S0xf6e: v12b1Vf6e = CALLER 
    0x12b2S0xf6e: v12b2Vf6e = EQ v12b1Vf6e, v12b0Vf6e
    0x12b3S0xf6e: v12b3Vf6e(0x1d48) = CONST 
    0x12b6S0xf6e: JUMPI v12b3Vf6e(0x1d48), v12b2Vf6e

    Begin block 0x12b7B0xf6e
    prev=[0x129eB0xf6e], succ=[]
    =================================
    0x12b7S0xf6e: v12b7Vf6e(0x40) = CONST 
    0x12baS0xf6e: v12baVf6e = MLOAD v12b7Vf6e(0x40)
    0x12bbS0xf6e: v12bbVf6e(0x461bcd) = CONST 
    0x12bfS0xf6e: v12bfVf6e(0xe5) = CONST 
    0x12c1S0xf6e: v12c1Vf6e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12bfVf6e(0xe5), v12bbVf6e(0x461bcd)
    0x12c3S0xf6e: MSTORE v12baVf6e, v12c1Vf6e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12c4S0xf6e: v12c4Vf6e(0x20) = CONST 
    0x12c6S0xf6e: v12c6Vf6e(0x4) = CONST 
    0x12c9S0xf6e: v12c9Vf6e = ADD v12baVf6e, v12c6Vf6e(0x4)
    0x12caS0xf6e: MSTORE v12c9Vf6e, v12c4Vf6e(0x20)
    0x12cbS0xf6e: v12cbVf6e(0xe) = CONST 
    0x12cdS0xf6e: v12cdVf6e(0x24) = CONST 
    0x12d0S0xf6e: v12d0Vf6e = ADD v12baVf6e, v12cdVf6e(0x24)
    0x12d1S0xf6e: MSTORE v12d0Vf6e, v12cbVf6e(0xe)
    0x12d2S0xf6e: v12d2Vf6e(0x6f6e6c79476f7665726e616e6365) = CONST 
    0x12e1S0xf6e: v12e1Vf6e(0x90) = CONST 
    0x12e3S0xf6e: v12e3Vf6e(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000) = SHL v12e1Vf6e(0x90), v12d2Vf6e(0x6f6e6c79476f7665726e616e6365)
    0x12e4S0xf6e: v12e4Vf6e(0x44) = CONST 
    0x12e7S0xf6e: v12e7Vf6e = ADD v12baVf6e, v12e4Vf6e(0x44)
    0x12e8S0xf6e: MSTORE v12e7Vf6e, v12e3Vf6e(0x6f6e6c79476f7665726e616e6365000000000000000000000000000000000000)
    0x12eaS0xf6e: v12eaVf6e = MLOAD v12b7Vf6e(0x40)
    0x12eeS0xf6e: v12eeVf6e(0x0) = SUB v12baVf6e, v12eaVf6e
    0x12efS0xf6e: v12efVf6e(0x64) = CONST 
    0x12f1S0xf6e: v12f1Vf6e(0x64) = ADD v12efVf6e(0x64), v12eeVf6e(0x0)
    0x12f3S0xf6e: REVERT v12eaVf6e, v12f1Vf6e(0x64)

    Begin block 0x1d48B0xf6e
    prev=[0x129eB0xf6e], succ=[0xf76]
    =================================
    0x1d49S0xf6e: JUMP vf6f(0xf76)

    Begin block 0xf76
    prev=[0x1d48B0xf6e], succ=[0x1c13]
    =================================
    0xf77: vf77(0x36) = CONST 
    0xf7a: vf7a = SLOAD vf77(0x36)
    0xf7b: vf7b(0x1) = CONST 
    0xf7d: vf7d(0x1) = CONST 
    0xf7f: vf7f(0xa0) = CONST 
    0xf81: vf81(0x10000000000000000000000000000000000000000) = SHL vf7f(0xa0), vf7d(0x1)
    0xf82: vf82(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf81(0x10000000000000000000000000000000000000000), vf7b(0x1)
    0xf83: vf83(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vf82(0xffffffffffffffffffffffffffffffffffffffff)
    0xf84: vf84 = AND vf83(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vf7a
    0xf85: vf85(0x1) = CONST 
    0xf87: vf87(0x1) = CONST 
    0xf89: vf89(0xa0) = CONST 
    0xf8b: vf8b(0x10000000000000000000000000000000000000000) = SHL vf89(0xa0), vf87(0x1)
    0xf8c: vf8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf8b(0x10000000000000000000000000000000000000000), vf85(0x1)
    0xf90: vf90 = AND vf8c(0xffffffffffffffffffffffffffffffffffffffff), v59b
    0xf94: vf94 = OR vf90, vf84
    0xf96: SSTORE vf77(0x36), vf94
    0xf97: JUMP v57b(0x1c13)

    Begin block 0x1c13
    prev=[0xf76], succ=[]
    =================================
    0x1c14: STOP 

}

function withdraw(address,uint256)() public {
    Begin block 0x5a0
    prev=[], succ=[0x5b2, 0x5b6]
    =================================
    0x5a1: v5a1(0x1c34) = CONST 
    0x5a4: v5a4(0x4) = CONST 
    0x5a7: v5a7 = CALLDATASIZE 
    0x5a8: v5a8 = SUB v5a7, v5a4(0x4)
    0x5a9: v5a9(0x40) = CONST 
    0x5ac: v5ac = LT v5a8, v5a9(0x40)
    0x5ad: v5ad = ISZERO v5ac
    0x5ae: v5ae(0x5b6) = CONST 
    0x5b1: JUMPI v5ae(0x5b6), v5ad

    Begin block 0x5b2
    prev=[0x5a0], succ=[]
    =================================
    0x5b2: v5b2(0x0) = CONST 
    0x5b5: REVERT v5b2(0x0), v5b2(0x0)

    Begin block 0x5b6
    prev=[0x5a0], succ=[0xf98]
    =================================
    0x5b8: v5b8(0x1) = CONST 
    0x5ba: v5ba(0x1) = CONST 
    0x5bc: v5bc(0xa0) = CONST 
    0x5be: v5be(0x10000000000000000000000000000000000000000) = SHL v5bc(0xa0), v5ba(0x1)
    0x5bf: v5bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5be(0x10000000000000000000000000000000000000000), v5b8(0x1)
    0x5c1: v5c1 = CALLDATALOAD v5a4(0x4)
    0x5c2: v5c2 = AND v5c1, v5bf(0xffffffffffffffffffffffffffffffffffffffff)
    0x5c4: v5c4(0x20) = CONST 
    0x5c6: v5c6(0x24) = ADD v5c4(0x20), v5a4(0x4)
    0x5c7: v5c7 = CALLDATALOAD v5c6(0x24)
    0x5c8: v5c8(0xf98) = CONST 
    0x5cb: JUMP v5c8(0xf98)

    Begin block 0xf98
    prev=[0x5b6], succ=[0xfba, 0xfef]
    =================================
    0xf99: vf99(0x1) = CONST 
    0xf9b: vf9b(0x1) = CONST 
    0xf9d: vf9d(0xa0) = CONST 
    0xf9f: vf9f(0x10000000000000000000000000000000000000000) = SHL vf9d(0xa0), vf9b(0x1)
    0xfa0: vfa0(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf9f(0x10000000000000000000000000000000000000000), vf99(0x1)
    0xfa3: vfa3 = AND vfa0(0xffffffffffffffffffffffffffffffffffffffff), v5c2
    0xfa4: vfa4(0x0) = CONST 
    0xfa8: MSTORE vfa4(0x0), vfa3
    0xfa9: vfa9(0x37) = CONST 
    0xfab: vfab(0x20) = CONST 
    0xfad: MSTORE vfab(0x20), vfa9(0x37)
    0xfae: vfae(0x40) = CONST 
    0xfb1: vfb1 = SHA3 vfa4(0x0), vfae(0x40)
    0xfb2: vfb2 = SLOAD vfb1
    0xfb3: vfb3 = AND vfb2, vfa0(0xffffffffffffffffffffffffffffffffffffffff)
    0xfb4: vfb4 = CALLER 
    0xfb5: vfb5 = EQ vfb4, vfb3
    0xfb6: vfb6(0xfef) = CONST 
    0xfb9: JUMPI vfb6(0xfef), vfb5

    Begin block 0xfba
    prev=[0xf98], succ=[]
    =================================
    0xfba: vfba(0x40) = CONST 
    0xfbd: vfbd = MLOAD vfba(0x40)
    0xfbe: vfbe(0x461bcd) = CONST 
    0xfc2: vfc2(0xe5) = CONST 
    0xfc4: vfc4(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vfc2(0xe5), vfbe(0x461bcd)
    0xfc6: MSTORE vfbd, vfc4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xfc7: vfc7(0x20) = CONST 
    0xfc9: vfc9(0x4) = CONST 
    0xfcc: vfcc = ADD vfbd, vfc9(0x4)
    0xfcd: MSTORE vfcc, vfc7(0x20)
    0xfce: vfce(0x6) = CONST 
    0xfd0: vfd0(0x24) = CONST 
    0xfd3: vfd3 = ADD vfbd, vfd0(0x24)
    0xfd4: MSTORE vfd3, vfce(0x6)
    0xfd5: vfd5(0x85d985d5b1d) = CONST 
    0xfdc: vfdc(0xd2) = CONST 
    0xfde: vfde(0x217661756c740000000000000000000000000000000000000000000000000000) = SHL vfdc(0xd2), vfd5(0x85d985d5b1d)
    0xfdf: vfdf(0x44) = CONST 
    0xfe2: vfe2 = ADD vfbd, vfdf(0x44)
    0xfe3: MSTORE vfe2, vfde(0x217661756c740000000000000000000000000000000000000000000000000000)
    0xfe5: vfe5 = MLOAD vfba(0x40)
    0xfe9: vfe9(0x0) = SUB vfbd, vfe5
    0xfea: vfea(0x64) = CONST 
    0xfec: vfec(0x64) = ADD vfea(0x64), vfe9(0x0)
    0xfee: REVERT vfe5, vfec(0x64)

    Begin block 0xfef
    prev=[0xf98], succ=[0x1042, 0x1046]
    =================================
    0xff0: vff0(0x1) = CONST 
    0xff2: vff2(0x1) = CONST 
    0xff4: vff4(0xa0) = CONST 
    0xff6: vff6(0x10000000000000000000000000000000000000000) = SHL vff4(0xa0), vff2(0x1)
    0xff7: vff7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vff6(0x10000000000000000000000000000000000000000), vff0(0x1)
    0xffa: vffa = AND v5c2, vff7(0xffffffffffffffffffffffffffffffffffffffff)
    0xffb: vffb(0x0) = CONST 
    0xfff: MSTORE vffb(0x0), vffa
    0x1000: v1000(0x38) = CONST 
    0x1002: v1002(0x20) = CONST 
    0x1004: MSTORE v1002(0x20), v1000(0x38)
    0x1005: v1005(0x40) = CONST 
    0x1009: v1009 = SHA3 vffb(0x0), v1005(0x40)
    0x100a: v100a = SLOAD v1009
    0x100c: v100c = MLOAD v1005(0x40)
    0x100d: v100d(0x2e1a7d4d) = CONST 
    0x1012: v1012(0xe0) = CONST 
    0x1014: v1014(0x2e1a7d4d00000000000000000000000000000000000000000000000000000000) = SHL v1012(0xe0), v100d(0x2e1a7d4d)
    0x1016: MSTORE v100c, v1014(0x2e1a7d4d00000000000000000000000000000000000000000000000000000000)
    0x1017: v1017(0x4) = CONST 
    0x101a: v101a = ADD v100c, v1017(0x4)
    0x101d: MSTORE v101a, v5c7
    0x101f: v101f = MLOAD v1005(0x40)
    0x1021: v1021 = AND vff7(0xffffffffffffffffffffffffffffffffffffffff), v100a
    0x1023: v1023(0x2e1a7d4d) = CONST 
    0x1029: v1029(0x24) = CONST 
    0x102d: v102d = ADD v100c, v1029(0x24)
    0x1034: v1034(0x0) = SUB v100c, v101f
    0x1035: v1035(0x24) = ADD v1034(0x0), v1029(0x24)
    0x103a: v103a = EXTCODESIZE v1021
    0x103b: v103b = ISZERO v103a
    0x103d: v103d = ISZERO v103b
    0x103e: v103e(0x1046) = CONST 
    0x1041: JUMPI v103e(0x1046), v103d

    Begin block 0x1042
    prev=[0xfef], succ=[]
    =================================
    0x1042: v1042(0x0) = CONST 
    0x1045: REVERT v1042(0x0), v1042(0x0)

    Begin block 0x1046
    prev=[0xfef], succ=[0x1051, 0x105a]
    =================================
    0x1048: v1048 = GAS 
    0x1049: v1049 = CALL v1048, v1021, vffb(0x0), v101f, v1035(0x24), v101f, vffb(0x0)
    0x104a: v104a = ISZERO v1049
    0x104c: v104c = ISZERO v104a
    0x104d: v104d(0x105a) = CONST 
    0x1050: JUMPI v104d(0x105a), v104c

    Begin block 0x1051
    prev=[0x1046], succ=[]
    =================================
    0x1051: v1051 = RETURNDATASIZE 
    0x1052: v1052(0x0) = CONST 
    0x1055: RETURNDATACOPY v1052(0x0), v1052(0x0), v1051
    0x1056: v1056 = RETURNDATASIZE 
    0x1057: v1057(0x0) = CONST 
    0x1059: REVERT v1057(0x0), v1056

    Begin block 0x105a
    prev=[0x1046], succ=[0x1c34]
    =================================
    0x1061: JUMP v5a1(0x1c34)

    Begin block 0x1c34
    prev=[0x105a], succ=[]
    =================================
    0x1c35: STOP 

}

function onesplit()() public {
    Begin block 0x5cc
    prev=[], succ=[0x1062]
    =================================
    0x5cd: v5cd(0x1c55) = CONST 
    0x5d0: v5d0(0x1062) = CONST 
    0x5d3: JUMP v5d0(0x1062)

    Begin block 0x1062
    prev=[0x5cc], succ=[0x1c55]
    =================================
    0x1063: v1063(0x35) = CONST 
    0x1065: v1065 = SLOAD v1063(0x35)
    0x1066: v1066(0x1) = CONST 
    0x1068: v1068(0x1) = CONST 
    0x106a: v106a(0xa0) = CONST 
    0x106c: v106c(0x10000000000000000000000000000000000000000) = SHL v106a(0xa0), v1068(0x1)
    0x106d: v106d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v106c(0x10000000000000000000000000000000000000000), v1066(0x1)
    0x106e: v106e = AND v106d(0xffffffffffffffffffffffffffffffffffffffff), v1065
    0x1070: JUMP v5cd(0x1c55)

    Begin block 0x1c55
    prev=[0x1062], succ=[]
    =================================
    0x1c56: v1c56(0x40) = CONST 
    0x1c59: v1c59 = MLOAD v1c56(0x40)
    0x1c5a: v1c5a(0x1) = CONST 
    0x1c5c: v1c5c(0x1) = CONST 
    0x1c5e: v1c5e(0xa0) = CONST 
    0x1c60: v1c60(0x10000000000000000000000000000000000000000) = SHL v1c5e(0xa0), v1c5c(0x1)
    0x1c61: v1c61(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c60(0x10000000000000000000000000000000000000000), v1c5a(0x1)
    0x1c64: v1c64 = AND v106e, v1c61(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c66: MSTORE v1c59, v1c64
    0x1c67: v1c67 = MLOAD v1c56(0x40)
    0x1c6b: v1c6b(0x0) = SUB v1c59, v1c67
    0x1c6c: v1c6c(0x20) = CONST 
    0x1c6e: v1c6e(0x20) = ADD v1c6c(0x20), v1c6b(0x0)
    0x1c70: RETURN v1c67, v1c6e(0x20)

}

function split()() public {
    Begin block 0x5d4
    prev=[], succ=[0x1071]
    =================================
    0x5d5: v5d5(0x1c90) = CONST 
    0x5d8: v5d8(0x1071) = CONST 
    0x5db: JUMP v5d8(0x1071)

    Begin block 0x1071
    prev=[0x5d4], succ=[0x1c90]
    =================================
    0x1072: v1072(0x3b) = CONST 
    0x1074: v1074 = SLOAD v1072(0x3b)
    0x1076: JUMP v5d5(0x1c90)

    Begin block 0x1c90
    prev=[0x1071], succ=[]
    =================================
    0x1c91: v1c91(0x40) = CONST 
    0x1c94: v1c94 = MLOAD v1c91(0x40)
    0x1c97: MSTORE v1c94, v1074
    0x1c98: v1c98 = MLOAD v1c91(0x40)
    0x1c9c: v1c9c(0x0) = SUB v1c94, v1c98
    0x1c9d: v1c9d(0x20) = CONST 
    0x1c9f: v1c9f(0x20) = ADD v1c9d(0x20), v1c9c(0x0)
    0x1ca1: RETURN v1c98, v1c9f(0x20)

}

function initialize(address,address,address,address)() public {
    Begin block 0x5dc
    prev=[], succ=[0x5ee, 0x5f2]
    =================================
    0x5dd: v5dd(0x1cc1) = CONST 
    0x5e0: v5e0(0x4) = CONST 
    0x5e3: v5e3 = CALLDATASIZE 
    0x5e4: v5e4 = SUB v5e3, v5e0(0x4)
    0x5e5: v5e5(0x80) = CONST 
    0x5e8: v5e8 = LT v5e4, v5e5(0x80)
    0x5e9: v5e9 = ISZERO v5e8
    0x5ea: v5ea(0x5f2) = CONST 
    0x5ed: JUMPI v5ea(0x5f2), v5e9

    Begin block 0x5ee
    prev=[0x5dc], succ=[]
    =================================
    0x5ee: v5ee(0x0) = CONST 
    0x5f1: REVERT v5ee(0x0), v5ee(0x0)

    Begin block 0x5f2
    prev=[0x5dc], succ=[0x1077]
    =================================
    0x5f4: v5f4(0x1) = CONST 
    0x5f6: v5f6(0x1) = CONST 
    0x5f8: v5f8(0xa0) = CONST 
    0x5fa: v5fa(0x10000000000000000000000000000000000000000) = SHL v5f8(0xa0), v5f6(0x1)
    0x5fb: v5fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5fa(0x10000000000000000000000000000000000000000), v5f4(0x1)
    0x5fd: v5fd = CALLDATALOAD v5e0(0x4)
    0x5ff: v5ff = AND v5fb(0xffffffffffffffffffffffffffffffffffffffff), v5fd
    0x601: v601(0x20) = CONST 
    0x604: v604(0x24) = ADD v5e0(0x4), v601(0x20)
    0x605: v605 = CALLDATALOAD v604(0x24)
    0x607: v607 = AND v5fb(0xffffffffffffffffffffffffffffffffffffffff), v605
    0x609: v609(0x40) = CONST 
    0x60c: v60c(0x44) = ADD v5e0(0x4), v609(0x40)
    0x60d: v60d = CALLDATALOAD v60c(0x44)
    0x60f: v60f = AND v5fb(0xffffffffffffffffffffffffffffffffffffffff), v60d
    0x611: v611(0x60) = CONST 
    0x613: v613(0x64) = ADD v611(0x60), v5e0(0x4)
    0x614: v614 = CALLDATALOAD v613(0x64)
    0x615: v615 = AND v614, v5fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x616: v616(0x1077) = CONST 
    0x619: JUMP v616(0x1077)

    Begin block 0x1077
    prev=[0x5f2], succ=[0x1090, 0x1088]
    =================================
    0x1078: v1078(0x0) = CONST 
    0x107a: v107a = SLOAD v1078(0x0)
    0x107b: v107b(0x100) = CONST 
    0x107f: v107f = DIV v107a, v107b(0x100)
    0x1080: v1080(0xff) = CONST 
    0x1082: v1082 = AND v1080(0xff), v107f
    0x1084: v1084(0x1090) = CONST 
    0x1087: JUMPI v1084(0x1090), v1082

    Begin block 0x1090
    prev=[0x1077, 0x13ea], succ=[0x109e, 0x1096]
    =================================
    0x1090_0x0: v1090_0 = PHI v1082, v13ed
    0x1092: v1092(0x109e) = CONST 
    0x1095: JUMPI v1092(0x109e), v1090_0

    Begin block 0x109e
    prev=[0x1090, 0x1096], succ=[0x10a3, 0x10d9]
    =================================
    0x109e_0x0: v109e_0 = PHI v1082, v109d, v13ed
    0x109f: v109f(0x10d9) = CONST 
    0x10a2: JUMPI v109f(0x10d9), v109e_0

    Begin block 0x10a3
    prev=[0x109e], succ=[]
    =================================
    0x10a3: v10a3(0x40) = CONST 
    0x10a5: v10a5 = MLOAD v10a3(0x40)
    0x10a6: v10a6(0x461bcd) = CONST 
    0x10aa: v10aa(0xe5) = CONST 
    0x10ac: v10ac(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v10aa(0xe5), v10a6(0x461bcd)
    0x10ae: MSTORE v10a5, v10ac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10af: v10af(0x4) = CONST 
    0x10b1: v10b1 = ADD v10af(0x4), v10a5
    0x10b4: v10b4(0x20) = CONST 
    0x10b6: v10b6 = ADD v10b4(0x20), v10b1
    0x10b9: v10b9(0x20) = SUB v10b6, v10b1
    0x10bb: MSTORE v10b1, v10b9(0x20)
    0x10bc: v10bc(0x2e) = CONST 
    0x10bf: MSTORE v10b6, v10bc(0x2e)
    0x10c0: v10c0(0x20) = CONST 
    0x10c2: v10c2 = ADD v10c0(0x20), v10b6
    0x10c4: v10c4(0x166a) = CONST 
    0x10c7: v10c7(0x2e) = CONST 
    0x10ca: CODECOPY v10c2, v10c4(0x166a), v10c7(0x2e)
    0x10cb: v10cb(0x40) = CONST 
    0x10cd: v10cd = ADD v10cb(0x40), v10c2
    0x10d1: v10d1(0x40) = CONST 
    0x10d3: v10d3 = MLOAD v10d1(0x40)
    0x10d6: v10d6(0x84) = SUB v10cd, v10d3
    0x10d8: REVERT v10d3, v10d6(0x84)

    Begin block 0x10d9
    prev=[0x109e], succ=[0x10ec, 0x1104]
    =================================
    0x10da: v10da(0x0) = CONST 
    0x10dc: v10dc = SLOAD v10da(0x0)
    0x10dd: v10dd(0x100) = CONST 
    0x10e1: v10e1 = DIV v10dc, v10dd(0x100)
    0x10e2: v10e2(0xff) = CONST 
    0x10e4: v10e4 = AND v10e2(0xff), v10e1
    0x10e5: v10e5 = ISZERO v10e4
    0x10e7: v10e7 = ISZERO v10e5
    0x10e8: v10e8(0x1104) = CONST 
    0x10eb: JUMPI v10e8(0x1104), v10e7

    Begin block 0x10ec
    prev=[0x10d9], succ=[0x1104]
    =================================
    0x10ec: v10ec(0x0) = CONST 
    0x10ef: v10ef = SLOAD v10ec(0x0)
    0x10f0: v10f0(0xff) = CONST 
    0x10f2: v10f2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v10f0(0xff)
    0x10f3: v10f3(0xff00) = CONST 
    0x10f6: v10f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v10f3(0xff00)
    0x10f9: v10f9 = AND v10ef, v10f6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x10fa: v10fa(0x100) = CONST 
    0x10fd: v10fd = OR v10fa(0x100), v10f9
    0x10fe: v10fe = AND v10fd, v10f2(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x10ff: v10ff(0x1) = CONST 
    0x1101: v1101 = OR v10ff(0x1), v10fe
    0x1103: SSTORE v10ec(0x0), v1101

    Begin block 0x1104
    prev=[0x10ec, 0x10d9], succ=[0x1188, 0x1193]
    =================================
    0x1105: v1105(0x0) = CONST 
    0x1108: v1108 = SLOAD v1105(0x0)
    0x1109: v1109(0x1) = CONST 
    0x110b: v110b(0x1) = CONST 
    0x110d: v110d(0xa0) = CONST 
    0x110f: v110f(0x10000000000000000000000000000000000000000) = SHL v110d(0xa0), v110b(0x1)
    0x1110: v1110(0xffffffffffffffffffffffffffffffffffffffff) = SUB v110f(0x10000000000000000000000000000000000000000), v1109(0x1)
    0x1113: v1113 = AND v5ff, v1110(0xffffffffffffffffffffffffffffffffffffffff)
    0x1114: v1114(0x10000) = CONST 
    0x1118: v1118 = MUL v1114(0x10000), v1113
    0x1119: v1119(0x10000) = CONST 
    0x111d: v111d(0x1) = CONST 
    0x111f: v111f(0xb0) = CONST 
    0x1121: v1121(0x100000000000000000000000000000000000000000000) = SHL v111f(0xb0), v111d(0x1)
    0x1122: v1122(0xffffffffffffffffffffffffffffffffffffffff0000) = SUB v1121(0x100000000000000000000000000000000000000000000), v1119(0x10000)
    0x1123: v1123(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT v1122(0xffffffffffffffffffffffffffffffffffffffff0000)
    0x1126: v1126 = AND v1108, v1123(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff)
    0x112a: v112a = OR v1126, v1118
    0x112d: SSTORE v1105(0x0), v112a
    0x112e: v112e(0x1) = CONST 
    0x1131: v1131 = SLOAD v112e(0x1)
    0x1134: v1134 = AND v1110(0xffffffffffffffffffffffffffffffffffffffff), v607
    0x1135: v1135(0x1) = CONST 
    0x1137: v1137(0x1) = CONST 
    0x1139: v1139(0xa0) = CONST 
    0x113b: v113b(0x10000000000000000000000000000000000000000) = SHL v1139(0xa0), v1137(0x1)
    0x113c: v113c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v113b(0x10000000000000000000000000000000000000000), v1135(0x1)
    0x113d: v113d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v113c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1140: v1140 = AND v113d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1131
    0x1141: v1141 = OR v1140, v1134
    0x1144: SSTORE v112e(0x1), v1141
    0x1145: v1145(0x2) = CONST 
    0x1148: v1148 = SLOAD v1145(0x2)
    0x114b: v114b = AND v1110(0xffffffffffffffffffffffffffffffffffffffff), v60f
    0x114e: v114e = AND v113d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1148
    0x114f: v114f = OR v114e, v114b
    0x1151: SSTORE v1145(0x2), v114f
    0x1152: v1152(0x36) = CONST 
    0x1155: v1155 = SLOAD v1152(0x36)
    0x1158: v1158 = AND v615, v1110(0xffffffffffffffffffffffffffffffffffffffff)
    0x115b: v115b = AND v113d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1155
    0x115f: v115f = OR v115b, v1158
    0x1162: SSTORE v1152(0x36), v115f
    0x1163: v1163(0x35) = CONST 
    0x1166: v1166 = SLOAD v1163(0x35)
    0x1169: v1169 = AND v113d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1166
    0x116a: v116a(0x50fda034c0ce7a8f7efdaebda7aa7ca21cc1267e) = CONST 
    0x117f: v117f = OR v116a(0x50fda034c0ce7a8f7efdaebda7aa7ca21cc1267e), v1169
    0x1181: SSTORE v1163(0x35), v117f
    0x1183: v1183 = ISZERO v10e5
    0x1184: v1184(0x1193) = CONST 
    0x1187: JUMPI v1184(0x1193), v1183

    Begin block 0x1188
    prev=[0x1104], succ=[0x1193]
    =================================
    0x1188: v1188(0x0) = CONST 
    0x118b: v118b = SLOAD v1188(0x0)
    0x118c: v118c(0xff00) = CONST 
    0x118f: v118f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v118c(0xff00)
    0x1190: v1190 = AND v118f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v118b
    0x1192: SSTORE v1188(0x0), v1190

    Begin block 0x1193
    prev=[0x1188, 0x1104], succ=[0x1cc1]
    =================================
    0x1199: JUMP v5dd(0x1cc1)

    Begin block 0x1cc1
    prev=[0x1193], succ=[]
    =================================
    0x1cc2: STOP 

    Begin block 0x1096
    prev=[0x1090], succ=[0x109e]
    =================================
    0x1097: v1097(0x0) = CONST 
    0x1099: v1099 = SLOAD v1097(0x0)
    0x109a: v109a(0xff) = CONST 
    0x109c: v109c = AND v109a(0xff), v1099
    0x109d: v109d = ISZERO v109c

    Begin block 0x1088
    prev=[0x1077], succ=[0x13ea]
    =================================
    0x1089: v1089(0x1090) = CONST 
    0x108c: v108c(0x13ea) = CONST 
    0x108f: JUMP v108c(0x13ea)

    Begin block 0x13ea
    prev=[0x1088], succ=[0x1090]
    =================================
    0x13eb: v13eb = ADDRESS 
    0x13ec: v13ec = EXTCODESIZE v13eb
    0x13ed: v13ed = ISZERO v13ec
    0x13ef: JUMP v1089(0x1090)

}

function withdrawAll(address)() public {
    Begin block 0x61a
    prev=[], succ=[0x62c, 0x630]
    =================================
    0x61b: v61b(0x1ce2) = CONST 
    0x61e: v61e(0x4) = CONST 
    0x621: v621 = CALLDATASIZE 
    0x622: v622 = SUB v621, v61e(0x4)
    0x623: v623(0x20) = CONST 
    0x626: v626 = LT v622, v623(0x20)
    0x627: v627 = ISZERO v626
    0x628: v628(0x630) = CONST 
    0x62b: JUMPI v628(0x630), v627

    Begin block 0x62c
    prev=[0x61a], succ=[]
    =================================
    0x62c: v62c(0x0) = CONST 
    0x62f: REVERT v62c(0x0), v62c(0x0)

    Begin block 0x630
    prev=[0x61a], succ=[0x119a]
    =================================
    0x632: v632 = CALLDATALOAD v61e(0x4)
    0x633: v633(0x1) = CONST 
    0x635: v635(0x1) = CONST 
    0x637: v637(0xa0) = CONST 
    0x639: v639(0x10000000000000000000000000000000000000000) = SHL v637(0xa0), v635(0x1)
    0x63a: v63a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v639(0x10000000000000000000000000000000000000000), v633(0x1)
    0x63b: v63b = AND v63a(0xffffffffffffffffffffffffffffffffffffffff), v632
    0x63c: v63c(0x119a) = CONST 
    0x63f: JUMP v63c(0x119a)

    Begin block 0x119a
    prev=[0x630], succ=[0x11a2]
    =================================
    0x119b: v119b(0x11a2) = CONST 
    0x119e: v119e(0x1222) = CONST 
    0x11a1: CALLPRIVATE v119e(0x1222), v119b(0x11a2)

    Begin block 0x11a2
    prev=[0x119a], succ=[0x11ef, 0x11f3]
    =================================
    0x11a3: v11a3(0x1) = CONST 
    0x11a5: v11a5(0x1) = CONST 
    0x11a7: v11a7(0xa0) = CONST 
    0x11a9: v11a9(0x10000000000000000000000000000000000000000) = SHL v11a7(0xa0), v11a5(0x1)
    0x11aa: v11aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11a9(0x10000000000000000000000000000000000000000), v11a3(0x1)
    0x11ad: v11ad = AND v63b, v11aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x11ae: v11ae(0x0) = CONST 
    0x11b2: MSTORE v11ae(0x0), v11ad
    0x11b3: v11b3(0x38) = CONST 
    0x11b5: v11b5(0x20) = CONST 
    0x11b9: MSTORE v11b5(0x20), v11b3(0x38)
    0x11ba: v11ba(0x40) = CONST 
    0x11be: v11be = SHA3 v11ae(0x0), v11ba(0x40)
    0x11bf: v11bf = SLOAD v11be
    0x11c1: v11c1 = MLOAD v11ba(0x40)
    0x11c2: v11c2(0x429c145b) = CONST 
    0x11c7: v11c7(0xe1) = CONST 
    0x11c9: v11c9(0x853828b600000000000000000000000000000000000000000000000000000000) = SHL v11c7(0xe1), v11c2(0x429c145b)
    0x11cb: MSTORE v11c1, v11c9(0x853828b600000000000000000000000000000000000000000000000000000000)
    0x11cd: v11cd = MLOAD v11ba(0x40)
    0x11cf: v11cf = AND v11aa(0xffffffffffffffffffffffffffffffffffffffff), v11bf
    0x11d1: v11d1(0x853828b6) = CONST 
    0x11d7: v11d7(0x4) = CONST 
    0x11db: v11db = ADD v11c1, v11d7(0x4)
    0x11e0: v11e0(0x0) = SUB v11c1, v11cd
    0x11e1: v11e1(0x4) = ADD v11e0(0x0), v11d7(0x4)
    0x11e7: v11e7 = EXTCODESIZE v11cf
    0x11e8: v11e8 = ISZERO v11e7
    0x11ea: v11ea = ISZERO v11e8
    0x11eb: v11eb(0x11f3) = CONST 
    0x11ee: JUMPI v11eb(0x11f3), v11ea

    Begin block 0x11ef
    prev=[0x11a2], succ=[]
    =================================
    0x11ef: v11ef(0x0) = CONST 
    0x11f2: REVERT v11ef(0x0), v11ef(0x0)

    Begin block 0x11f3
    prev=[0x11a2], succ=[0x11fe, 0x1207]
    =================================
    0x11f5: v11f5 = GAS 
    0x11f6: v11f6 = CALL v11f5, v11cf, v11ae(0x0), v11cd, v11e1(0x4), v11cd, v11b5(0x20)
    0x11f7: v11f7 = ISZERO v11f6
    0x11f9: v11f9 = ISZERO v11f7
    0x11fa: v11fa(0x1207) = CONST 
    0x11fd: JUMPI v11fa(0x1207), v11f9

    Begin block 0x11fe
    prev=[0x11f3], succ=[]
    =================================
    0x11fe: v11fe = RETURNDATASIZE 
    0x11ff: v11ff(0x0) = CONST 
    0x1202: RETURNDATACOPY v11ff(0x0), v11ff(0x0), v11fe
    0x1203: v1203 = RETURNDATASIZE 
    0x1204: v1204(0x0) = CONST 
    0x1206: REVERT v1204(0x0), v1203

    Begin block 0x1207
    prev=[0x11f3], succ=[0x1219, 0x1d03]
    =================================
    0x120c: v120c(0x40) = CONST 
    0x120e: v120e = MLOAD v120c(0x40)
    0x120f: v120f = RETURNDATASIZE 
    0x1210: v1210(0x20) = CONST 
    0x1213: v1213 = LT v120f, v1210(0x20)
    0x1214: v1214 = ISZERO v1213
    0x1215: v1215(0x1d03) = CONST 
    0x1218: JUMPI v1215(0x1d03), v1214

    Begin block 0x1219
    prev=[0x1207], succ=[]
    =================================
    0x1219: v1219(0x0) = CONST 
    0x121c: REVERT v1219(0x0), v1219(0x0)

    Begin block 0x1d03
    prev=[0x1207], succ=[0x1ce2]
    =================================
    0x1d07: JUMP v61b(0x1ce2)

    Begin block 0x1ce2
    prev=[0x1d03], succ=[]
    =================================
    0x1ce3: STOP 

}

