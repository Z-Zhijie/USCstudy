function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2b50]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x2b10: v2b10(0x2b50) = CONST 
    0x2b11: JUMPI v2b10(0x2b50), v8

    Begin block 0xd
    prev=[0x0], succ=[0x2b53, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x2b12: v2b12(0x2b53) = CONST 
    0x2b13: JUMPI v2b12(0x2b53), v3c

    Begin block 0x2b53
    prev=[0xd], succ=[]
    =================================
    0x2b54: v2b54(0x2b6) = CONST 
    0x2b55: CALLPRIVATE v2b54(0x2b6)

    Begin block 0x41
    prev=[0xd], succ=[0x2b56, 0x4c]
    =================================
    0x42: v42(0x13af4035) = CONST 
    0x47: v47 = EQ v42(0x13af4035), v35
    0x2b14: v2b14(0x2b56) = CONST 
    0x2b15: JUMPI v2b14(0x2b56), v47

    Begin block 0x2b56
    prev=[0x41], succ=[]
    =================================
    0x2b57: v2b57(0x344) = CONST 
    0x2b58: CALLPRIVATE v2b57(0x344)

    Begin block 0x4c
    prev=[0x41], succ=[0x2b59, 0x57]
    =================================
    0x4d: v4d(0x18160ddd) = CONST 
    0x52: v52 = EQ v4d(0x18160ddd), v35
    0x2b16: v2b16(0x2b59) = CONST 
    0x2b17: JUMPI v2b16(0x2b59), v52

    Begin block 0x2b59
    prev=[0x4c], succ=[]
    =================================
    0x2b5a: v2b5a(0x37d) = CONST 
    0x2b5b: CALLPRIVATE v2b5a(0x37d)

    Begin block 0x57
    prev=[0x4c], succ=[0x2b5c, 0x62]
    =================================
    0x58: v58(0x2f745c59) = CONST 
    0x5d: v5d = EQ v58(0x2f745c59), v35
    0x2b18: v2b18(0x2b5c) = CONST 
    0x2b19: JUMPI v2b18(0x2b5c), v5d

    Begin block 0x2b5c
    prev=[0x57], succ=[]
    =================================
    0x2b5d: v2b5d(0x3a6) = CONST 
    0x2b5e: CALLPRIVATE v2b5d(0x3a6)

    Begin block 0x62
    prev=[0x57], succ=[0x2b5f, 0x6d]
    =================================
    0x63: v63(0x3f4ba83a) = CONST 
    0x68: v68 = EQ v63(0x3f4ba83a), v35
    0x2b1a: v2b1a(0x2b5f) = CONST 
    0x2b1b: JUMPI v2b1a(0x2b5f), v68

    Begin block 0x2b5f
    prev=[0x62], succ=[]
    =================================
    0x2b60: v2b60(0x3fc) = CONST 
    0x2b61: CALLPRIVATE v2b60(0x3fc)

    Begin block 0x6d
    prev=[0x62], succ=[0x2b62, 0x78]
    =================================
    0x6e: v6e(0x41c0e1b5) = CONST 
    0x73: v73 = EQ v6e(0x41c0e1b5), v35
    0x2b1c: v2b1c(0x2b62) = CONST 
    0x2b1d: JUMPI v2b1c(0x2b62), v73

    Begin block 0x2b62
    prev=[0x6d], succ=[]
    =================================
    0x2b63: v2b63(0x411) = CONST 
    0x2b64: CALLPRIVATE v2b63(0x411)

    Begin block 0x78
    prev=[0x6d], succ=[0x2b65, 0x83]
    =================================
    0x79: v79(0x474da79a) = CONST 
    0x7e: v7e = EQ v79(0x474da79a), v35
    0x2b1e: v2b1e(0x2b65) = CONST 
    0x2b1f: JUMPI v2b1e(0x2b65), v7e

    Begin block 0x2b65
    prev=[0x78], succ=[]
    =================================
    0x2b66: v2b66(0x426) = CONST 
    0x2b67: CALLPRIVATE v2b66(0x426)

    Begin block 0x83
    prev=[0x78], succ=[0x2b68, 0x8e]
    =================================
    0x84: v84(0x47ef01a1) = CONST 
    0x89: v89 = EQ v84(0x47ef01a1), v35
    0x2b20: v2b20(0x2b68) = CONST 
    0x2b21: JUMPI v2b20(0x2b68), v89

    Begin block 0x2b68
    prev=[0x83], succ=[]
    =================================
    0x2b69: v2b69(0x489) = CONST 
    0x2b6a: CALLPRIVATE v2b69(0x489)

    Begin block 0x8e
    prev=[0x83], succ=[0x2b6b, 0x99]
    =================================
    0x8f: v8f(0x4f6ccce7) = CONST 
    0x94: v94 = EQ v8f(0x4f6ccce7), v35
    0x2b22: v2b22(0x2b6b) = CONST 
    0x2b23: JUMPI v2b22(0x2b6b), v94

    Begin block 0x2b6b
    prev=[0x8e], succ=[]
    =================================
    0x2b6c: v2b6c(0x4c0) = CONST 
    0x2b6d: CALLPRIVATE v2b6c(0x4c0)

    Begin block 0x99
    prev=[0x8e], succ=[0xa4, 0x2b6e]
    =================================
    0x9a: v9a(0x54fd4d50) = CONST 
    0x9f: v9f = EQ v9a(0x54fd4d50), v35
    0x2b24: v2b24(0x2b6e) = CONST 
    0x2b25: JUMPI v2b24(0x2b6e), v9f

    Begin block 0xa4
    prev=[0x99], succ=[0x2b71, 0xaf]
    =================================
    0xa5: va5(0x5acb6787) = CONST 
    0xaa: vaa = EQ va5(0x5acb6787), v35
    0x2b26: v2b26(0x2b71) = CONST 
    0x2b27: JUMPI v2b26(0x2b71), vaa

    Begin block 0x2b71
    prev=[0xa4], succ=[]
    =================================
    0x2b72: v2b72(0x556) = CONST 
    0x2b73: CALLPRIVATE v2b72(0x556)

    Begin block 0xaf
    prev=[0xa4], succ=[0x2b74, 0xba]
    =================================
    0xb0: vb0(0x5c975abb) = CONST 
    0xb5: vb5 = EQ vb0(0x5c975abb), v35
    0x2b28: v2b28(0x2b74) = CONST 
    0x2b29: JUMPI v2b28(0x2b74), vb5

    Begin block 0x2b74
    prev=[0xaf], succ=[]
    =================================
    0x2b75: v2b75(0x5a8) = CONST 
    0x2b76: CALLPRIVATE v2b75(0x5a8)

    Begin block 0xba
    prev=[0xaf], succ=[0x2b77, 0xc5]
    =================================
    0xbb: vbb(0x5fd8c710) = CONST 
    0xc0: vc0 = EQ vbb(0x5fd8c710), v35
    0x2b2a: v2b2a(0x2b77) = CONST 
    0x2b2b: JUMPI v2b2a(0x2b77), vc0

    Begin block 0x2b77
    prev=[0xba], succ=[]
    =================================
    0x2b78: v2b78(0x5d5) = CONST 
    0x2b79: CALLPRIVATE v2b78(0x5d5)

    Begin block 0xc5
    prev=[0xba], succ=[0x2b7a, 0xd0]
    =================================
    0xc6: vc6(0x6352211e) = CONST 
    0xcb: vcb = EQ vc6(0x6352211e), v35
    0x2b2c: v2b2c(0x2b7a) = CONST 
    0x2b2d: JUMPI v2b2c(0x2b7a), vcb

    Begin block 0x2b7a
    prev=[0xc5], succ=[]
    =================================
    0x2b7b: v2b7b(0x5ea) = CONST 
    0x2b7c: CALLPRIVATE v2b7b(0x5ea)

    Begin block 0xd0
    prev=[0xc5], succ=[0x2b7d, 0xdb]
    =================================
    0xd1: vd1(0x70a08231) = CONST 
    0xd6: vd6 = EQ vd1(0x70a08231), v35
    0x2b2e: v2b2e(0x2b7d) = CONST 
    0x2b2f: JUMPI v2b2e(0x2b7d), vd6

    Begin block 0x2b7d
    prev=[0xd0], succ=[]
    =================================
    0x2b7e: v2b7e(0x64d) = CONST 
    0x2b7f: CALLPRIVATE v2b7e(0x64d)

    Begin block 0xdb
    prev=[0xd0], succ=[0x2b80, 0xe6]
    =================================
    0xdc: vdc(0x8456cb59) = CONST 
    0xe1: ve1 = EQ vdc(0x8456cb59), v35
    0x2b30: v2b30(0x2b80) = CONST 
    0x2b31: JUMPI v2b30(0x2b80), ve1

    Begin block 0x2b80
    prev=[0xdb], succ=[]
    =================================
    0x2b81: v2b81(0x69a) = CONST 
    0x2b82: CALLPRIVATE v2b81(0x69a)

    Begin block 0xe6
    prev=[0xdb], succ=[0x2b83, 0xf1]
    =================================
    0xe7: ve7(0x8b4ce7ce) = CONST 
    0xec: vec = EQ ve7(0x8b4ce7ce), v35
    0x2b32: v2b32(0x2b83) = CONST 
    0x2b33: JUMPI v2b32(0x2b83), vec

    Begin block 0x2b83
    prev=[0xe6], succ=[]
    =================================
    0x2b84: v2b84(0x6af) = CONST 
    0x2b85: CALLPRIVATE v2b84(0x6af)

    Begin block 0xf1
    prev=[0xe6], succ=[0x2b86, 0xfc]
    =================================
    0xf2: vf2(0x8f84aa09) = CONST 
    0xf7: vf7 = EQ vf2(0x8f84aa09), v35
    0x2b34: v2b34(0x2b86) = CONST 
    0x2b35: JUMPI v2b34(0x2b86), vf7

    Begin block 0x2b86
    prev=[0xf1], succ=[]
    =================================
    0x2b87: v2b87(0x6d0) = CONST 
    0x2b88: CALLPRIVATE v2b87(0x6d0)

    Begin block 0xfc
    prev=[0xf1], succ=[0x2b89, 0x107]
    =================================
    0xfd: vfd(0x95d89b41) = CONST 
    0x102: v102 = EQ vfd(0x95d89b41), v35
    0x2b36: v2b36(0x2b89) = CONST 
    0x2b37: JUMPI v2b36(0x2b89), v102

    Begin block 0x2b89
    prev=[0xfc], succ=[]
    =================================
    0x2b8a: v2b8a(0x725) = CONST 
    0x2b8b: CALLPRIVATE v2b8a(0x725)

    Begin block 0x107
    prev=[0xfc], succ=[0x2b8c, 0x112]
    =================================
    0x108: v108(0xa951c994) = CONST 
    0x10d: v10d = EQ v108(0xa951c994), v35
    0x2b38: v2b38(0x2b8c) = CONST 
    0x2b39: JUMPI v2b38(0x2b8c), v10d

    Begin block 0x2b8c
    prev=[0x107], succ=[]
    =================================
    0x2b8d: v2b8d(0x7b3) = CONST 
    0x2b8e: CALLPRIVATE v2b8d(0x7b3)

    Begin block 0x112
    prev=[0x107], succ=[0x2b8f, 0x11d]
    =================================
    0x113: v113(0xb6635be6) = CONST 
    0x118: v118 = EQ v113(0xb6635be6), v35
    0x2b3a: v2b3a(0x2b8f) = CONST 
    0x2b3b: JUMPI v2b3a(0x2b8f), v118

    Begin block 0x2b8f
    prev=[0x112], succ=[]
    =================================
    0x2b90: v2b90(0x7c8) = CONST 
    0x2b91: CALLPRIVATE v2b90(0x7c8)

    Begin block 0x11d
    prev=[0x112], succ=[0x2b92, 0x128]
    =================================
    0x11e: v11e(0xc87b56dd) = CONST 
    0x123: v123 = EQ v11e(0xc87b56dd), v35
    0x2b3c: v2b3c(0x2b92) = CONST 
    0x2b3d: JUMPI v2b3c(0x2b92), v123

    Begin block 0x2b92
    prev=[0x11d], succ=[]
    =================================
    0x2b93: v2b93(0x7f5) = CONST 
    0x2b94: CALLPRIVATE v2b93(0x7f5)

    Begin block 0x128
    prev=[0x11d], succ=[0x2b95, 0x133]
    =================================
    0x129: v129(0xce8e95d4) = CONST 
    0x12e: v12e = EQ v129(0xce8e95d4), v35
    0x2b3e: v2b3e(0x2b95) = CONST 
    0x2b3f: JUMPI v2b3e(0x2b95), v12e

    Begin block 0x2b95
    prev=[0x128], succ=[]
    =================================
    0x2b96: v2b96(0x891) = CONST 
    0x2b97: CALLPRIVATE v2b96(0x891)

    Begin block 0x133
    prev=[0x128], succ=[0x2b98, 0x13e]
    =================================
    0x134: v134(0xcf73a1bc) = CONST 
    0x139: v139 = EQ v134(0xcf73a1bc), v35
    0x2b40: v2b40(0x2b98) = CONST 
    0x2b41: JUMPI v2b40(0x2b98), v139

    Begin block 0x2b98
    prev=[0x133], succ=[]
    =================================
    0x2b99: v2b99(0x95f) = CONST 
    0x2b9a: CALLPRIVATE v2b99(0x95f)

    Begin block 0x13e
    prev=[0x133], succ=[0x2b9b, 0x149]
    =================================
    0x13f: v13f(0xd0ebdbe7) = CONST 
    0x144: v144 = EQ v13f(0xd0ebdbe7), v35
    0x2b42: v2b42(0x2b9b) = CONST 
    0x2b43: JUMPI v2b42(0x2b9b), v144

    Begin block 0x2b9b
    prev=[0x13e], succ=[]
    =================================
    0x2b9c: v2b9c(0x9b4) = CONST 
    0x2b9d: CALLPRIVATE v2b9c(0x9b4)

    Begin block 0x149
    prev=[0x13e], succ=[0x2b9e, 0x154]
    =================================
    0x14a: v14a(0xd64c2018) = CONST 
    0x14f: v14f = EQ v14a(0xd64c2018), v35
    0x2b44: v2b44(0x2b9e) = CONST 
    0x2b45: JUMPI v2b44(0x2b9e), v14f

    Begin block 0x2b9e
    prev=[0x149], succ=[]
    =================================
    0x2b9f: v2b9f(0x9ed) = CONST 
    0x2ba0: CALLPRIVATE v2b9f(0x9ed)

    Begin block 0x154
    prev=[0x149], succ=[0x2ba1, 0x15f]
    =================================
    0x155: v155(0xe168a31a) = CONST 
    0x15a: v15a = EQ v155(0xe168a31a), v35
    0x2b46: v2b46(0x2ba1) = CONST 
    0x2b47: JUMPI v2b46(0x2ba1), v15a

    Begin block 0x2ba1
    prev=[0x154], succ=[]
    =================================
    0x2ba2: v2ba2(0xa77) = CONST 
    0x2ba3: CALLPRIVATE v2ba2(0xa77)

    Begin block 0x15f
    prev=[0x154], succ=[0x2ba4, 0x16a]
    =================================
    0x160: v160(0xeeb7ab0c) = CONST 
    0x165: v165 = EQ v160(0xeeb7ab0c), v35
    0x2b48: v2b48(0x2ba4) = CONST 
    0x2b49: JUMPI v2b48(0x2ba4), v165

    Begin block 0x2ba4
    prev=[0x15f], succ=[]
    =================================
    0x2ba5: v2ba5(0xac4) = CONST 
    0x2ba6: CALLPRIVATE v2ba5(0xac4)

    Begin block 0x16a
    prev=[0x15f], succ=[0x2ba7, 0x175]
    =================================
    0x16b: v16b(0xefef39a1) = CONST 
    0x170: v170 = EQ v16b(0xefef39a1), v35
    0x2b4a: v2b4a(0x2ba7) = CONST 
    0x2b4b: JUMPI v2b4a(0x2ba7), v170

    Begin block 0x2ba7
    prev=[0x16a], succ=[]
    =================================
    0x2ba8: v2ba8(0xb46) = CONST 
    0x2ba9: CALLPRIVATE v2ba8(0xb46)

    Begin block 0x175
    prev=[0x16a], succ=[0x2baa, 0x180]
    =================================
    0x176: v176(0xf5ea15d3) = CONST 
    0x17b: v17b = EQ v176(0xf5ea15d3), v35
    0x2b4c: v2b4c(0x2baa) = CONST 
    0x2b4d: JUMPI v2b4c(0x2baa), v17b

    Begin block 0x2baa
    prev=[0x175], succ=[]
    =================================
    0x2bab: v2bab(0xb5e) = CONST 
    0x2bac: CALLPRIVATE v2bab(0xb5e)

    Begin block 0x180
    prev=[0x175], succ=[0x2b50, 0x2bad]
    =================================
    0x181: v181(0xf8b096bb) = CONST 
    0x186: v186 = EQ v181(0xf8b096bb), v35
    0x2b4e: v2b4e(0x2bad) = CONST 
    0x2b4f: JUMPI v2b4e(0x2bad), v186

    Begin block 0x2b50
    prev=[0x0, 0x180], succ=[]
    =================================
    0x2b51: v2b51(0x18b) = CONST 
    0x2b52: CALLPRIVATE v2b51(0x18b)

    Begin block 0x2bad
    prev=[0x180], succ=[]
    =================================
    0x2bae: v2bae(0xb80) = CONST 
    0x2baf: CALLPRIVATE v2bae(0xb80)

    Begin block 0x2b6e
    prev=[0x99], succ=[]
    =================================
    0x2b6f: v2b6f(0x4f7) = CONST 
    0x2b70: CALLPRIVATE v2b6f(0x4f7)

}

function fallback()() public {
    Begin block 0x18b
    prev=[], succ=[0x192, 0x196]
    =================================
    0x18c: v18c = CALLVALUE 
    0x18d: v18d = ISZERO v18c
    0x18e: v18e(0x196) = CONST 
    0x191: JUMPI v18e(0x196), v18d

    Begin block 0x192
    prev=[0x18b], succ=[]
    =================================
    0x192: v192(0x0) = CONST 
    0x195: REVERT v192(0x0), v192(0x0)

    Begin block 0x196
    prev=[0x18b], succ=[0x29e6B0x196]
    =================================
    0x197: v197(0x0) = CONST 
    0x199: v199(0x1a0) = CONST 
    0x19c: v19c(0x29e6) = CONST 
    0x19f: JUMP v19c(0x29e6)

    Begin block 0x29e6B0x196
    prev=[0x196], succ=[0x1a0]
    =================================
    0x29e7S0x196: v29e7V196(0x20) = CONST 
    0x29e9S0x196: v29e9V196(0x40) = CONST 
    0x29ebS0x196: v29ebV196 = MLOAD v29e9V196(0x40)
    0x29eeS0x196: v29eeV196 = ADD v29ebV196, v29e7V196(0x20)
    0x29efS0x196: v29efV196(0x40) = CONST 
    0x29f1S0x196: MSTORE v29efV196(0x40), v29eeV196
    0x29f3S0x196: v29f3V196(0x0) = CONST 
    0x29f6S0x196: MSTORE v29ebV196, v29f3V196(0x0)
    0x29f9S0x196: JUMP v199(0x1a0)

    Begin block 0x1a0
    prev=[0x29e6B0x196], succ=[0x1c2, 0x212]
    =================================
    0x1a1: v1a1(0x21c) = CONST 
    0x1a4: v1a4(0x2) = CONST 
    0x1a6: v1a6(0x10) = CONST 
    0x1a9: v1a9(0x20) = CONST 
    0x1ab: v1ab(0x200) = MUL v1a9(0x20), v1a6(0x10)
    0x1ac: v1ac(0x40) = CONST 
    0x1ae: v1ae = MLOAD v1ac(0x40)
    0x1b1: v1b1 = ADD v1ae, v1ab(0x200)
    0x1b2: v1b2(0x40) = CONST 
    0x1b4: MSTORE v1b2(0x40), v1b1
    0x1ba: v1ba(0x10) = CONST 
    0x1bd: v1bd(0x0) = ISZERO v1ba(0x10)
    0x1be: v1be(0x212) = CONST 
    0x1c1: JUMPI v1be(0x212), v1bd(0x0)

    Begin block 0x1c2
    prev=[0x1a0], succ=[0x1c8]
    =================================
    0x1c2: v1c2(0x20) = CONST 
    0x1c4: v1c4(0x200) = MUL v1c2(0x20), v1ba(0x10)
    0x1c6: v1c6 = ADD v1ae, v1c4(0x200)

    Begin block 0x1c8
    prev=[0x1c2, 0x1c8], succ=[0x212, 0x1c8]
    =================================
    0x1c8_0x0: v1c8_0 = PHI v1ae, v205
    0x1c8_0x1: v1c8_1 = PHI v1a4(0x2), v209
    0x1ca: v1ca(0x0) = CONST 
    0x1cd: v1cd = SLOAD v1c8_1
    0x1cf: v1cf(0x100) = CONST 
    0x1d2: v1d2(0x1) = EXP v1cf(0x100), v1ca(0x0)
    0x1d4: v1d4 = DIV v1cd, v1d2(0x1)
    0x1d5: v1d5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ea: v1ea = AND v1d5(0xffffffffffffffffffffffffffffffffffffffff), v1d4
    0x1eb: v1eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x200: v200 = AND v1eb(0xffffffffffffffffffffffffffffffffffffffff), v1ea
    0x202: MSTORE v1c8_0, v200
    0x203: v203(0x20) = CONST 
    0x205: v205 = ADD v203(0x20), v1c8_0
    0x207: v207(0x1) = CONST 
    0x209: v209 = ADD v207(0x1), v1c8_1
    0x20d: v20d = GT v1c6, v205
    0x20e: v20e(0x1c8) = CONST 
    0x211: JUMPI v20e(0x1c8), v20d

    Begin block 0x212
    prev=[0x1a0, 0x1c8], succ=[0xc24]
    =================================
    0x218: v218(0xc24) = CONST 
    0x21b: JUMP v218(0xc24)

    Begin block 0xc24
    prev=[0x212], succ=[0xc34, 0xc35]
    =================================
    0xc25: vc25(0x0) = CONST 
    0xc28: vc28(0x3) = CONST 
    0xc2a: vc2a(0x10) = CONST 
    0xc2d: vc2d(0x1) = LT vc28(0x3), vc2a(0x10)
    0xc2e: vc2e(0x0) = ISZERO vc2d(0x1)
    0xc2f: vc2f(0x1) = ISZERO vc2e(0x0)
    0xc30: vc30(0xc35) = CONST 
    0xc33: JUMPI vc30(0xc35), vc2f(0x1)

    Begin block 0xc34
    prev=[0xc24], succ=[]
    =================================
    0xc34: THROW 

    Begin block 0xc35
    prev=[0xc24], succ=[0x21c]
    =================================
    0xc36: vc36(0x20) = CONST 
    0xc38: vc38(0x60) = MUL vc36(0x20), vc28(0x3)
    0xc39: vc39 = ADD vc38(0x60), v1ae
    0xc3a: vc3a = MLOAD vc39
    0xc40: JUMP v1a1(0x21c)

    Begin block 0x21c
    prev=[0xc35], succ=[0x256, 0x25a]
    =================================
    0x21f: v21f(0x0) = CONST 
    0x221: v221(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x236: v236(0x0) = AND v221(0xffffffffffffffffffffffffffffffffffffffff), v21f(0x0)
    0x238: v238(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24d: v24d = AND v238(0xffffffffffffffffffffffffffffffffffffffff), vc3a
    0x24e: v24e = EQ v24d, v236(0x0)
    0x24f: v24f = ISZERO v24e
    0x250: v250 = ISZERO v24f
    0x251: v251 = ISZERO v250
    0x252: v252(0x25a) = CONST 
    0x255: JUMPI v252(0x25a), v251

    Begin block 0x256
    prev=[0x21c], succ=[]
    =================================
    0x256: v256(0x0) = CONST 
    0x259: REVERT v256(0x0), v256(0x0)

    Begin block 0x25a
    prev=[0x21c], succ=[0x2b2, 0x2af]
    =================================
    0x25b: v25b(0x0) = CONST 
    0x25d: v25d = CALLDATASIZE 
    0x260: v260(0x1f) = CONST 
    0x262: v262 = ADD v260(0x1f), v25d
    0x263: v263(0x20) = CONST 
    0x267: v267 = DIV v262, v263(0x20)
    0x268: v268 = MUL v267, v263(0x20)
    0x269: v269(0x20) = CONST 
    0x26b: v26b = ADD v269(0x20), v268
    0x26c: v26c(0x40) = CONST 
    0x26e: v26e = MLOAD v26c(0x40)
    0x271: v271 = ADD v26e, v26b
    0x272: v272(0x40) = CONST 
    0x274: MSTORE v272(0x40), v271
    0x27c: MSTORE v26e, v25d
    0x27d: v27d(0x20) = CONST 
    0x27f: v27f = ADD v27d(0x20), v26e
    0x285: CALLDATACOPY v27f, v25b(0x0), v25d
    0x287: v287 = ADD v27f, v25d
    0x291: v291(0x0) = CONST 
    0x295: v295 = MLOAD v26e
    0x296: v296(0x20) = CONST 
    0x299: v299 = ADD v26e, v296(0x20)
    0x29b: v29b = GAS 
    0x29c: v29c = DELEGATECALL v29b, vc3a, v299, v295, v291(0x0), v291(0x0)
    0x29d: v29d = RETURNDATASIZE 
    0x29e: v29e(0x40) = CONST 
    0x2a0: v2a0 = MLOAD v29e(0x40)
    0x2a2: v2a2(0x0) = CONST 
    0x2a5: RETURNDATACOPY v2a0, v2a2(0x0), v29d
    0x2a7: v2a7(0x0) = CONST 
    0x2aa: v2aa = EQ v29c, v2a7(0x0)
    0x2ab: v2ab(0x2b2) = CONST 
    0x2ae: JUMPI v2ab(0x2b2), v2aa

    Begin block 0x2b2
    prev=[0x25a], succ=[]
    =================================
    0x2b5: REVERT v2a0, v29d

    Begin block 0x2af
    prev=[0x25a], succ=[]
    =================================
    0x2b1: RETURN v2a0, v29d

}

function name()() public {
    Begin block 0x2b6
    prev=[], succ=[0x2bd, 0x2c1]
    =================================
    0x2b7: v2b7 = CALLVALUE 
    0x2b8: v2b8 = ISZERO v2b7
    0x2b9: v2b9(0x2c1) = CONST 
    0x2bc: JUMPI v2b9(0x2c1), v2b8

    Begin block 0x2bd
    prev=[0x2b6], succ=[]
    =================================
    0x2bd: v2bd(0x0) = CONST 
    0x2c0: REVERT v2bd(0x0), v2bd(0x0)

    Begin block 0x2c1
    prev=[0x2b6], succ=[0xc41]
    =================================
    0x2c2: v2c2(0x2c9) = CONST 
    0x2c5: v2c5(0xc41) = CONST 
    0x2c8: JUMP v2c5(0xc41)

    Begin block 0xc41
    prev=[0x2c1], succ=[0x29faB0xc41]
    =================================
    0xc42: vc42(0xc49) = CONST 
    0xc45: vc45(0x29fa) = CONST 
    0xc48: JUMP vc45(0x29fa)

    Begin block 0x29faB0xc41
    prev=[0xc41], succ=[0xc49]
    =================================
    0x29fbS0xc41: v29fbVc41(0x20) = CONST 
    0x29fdS0xc41: v29fdVc41(0x40) = CONST 
    0x29ffS0xc41: v29ffVc41 = MLOAD v29fdVc41(0x40)
    0x2a02S0xc41: v2a02Vc41 = ADD v29ffVc41, v29fbVc41(0x20)
    0x2a03S0xc41: v2a03Vc41(0x40) = CONST 
    0x2a05S0xc41: MSTORE v2a03Vc41(0x40), v2a02Vc41
    0x2a07S0xc41: v2a07Vc41(0x0) = CONST 
    0x2a0aS0xc41: MSTORE v29ffVc41, v2a07Vc41(0x0)
    0x2a0dS0xc41: JUMP vc42(0xc49)

    Begin block 0xc49
    prev=[0x29faB0xc41], succ=[0x2c9]
    =================================
    0xc4a: vc4a(0x40) = CONST 
    0xc4d: vc4d = MLOAD vc4a(0x40)
    0xc50: vc50 = ADD vc4d, vc4a(0x40)
    0xc51: vc51(0x40) = CONST 
    0xc53: MSTORE vc51(0x40), vc50
    0xc55: vc55(0x1a) = CONST 
    0xc58: MSTORE vc4d, vc55(0x1a)
    0xc59: vc59(0x20) = CONST 
    0xc5b: vc5b = ADD vc59(0x20), vc4d
    0xc5c: vc5c(0x5468652042696c6c696f6e20446f6c6c61722050696374757265000000000000) = CONST 
    0xc7e: MSTORE vc5b, vc5c(0x5468652042696c6c696f6e20446f6c6c61722050696374757265000000000000)
    0xc83: JUMP v2c2(0x2c9)

    Begin block 0x2c9
    prev=[0xc49], succ=[0x2ee]
    =================================
    0x2ca: v2ca(0x40) = CONST 
    0x2cc: v2cc = MLOAD v2ca(0x40)
    0x2cf: v2cf(0x20) = CONST 
    0x2d1: v2d1 = ADD v2cf(0x20), v2cc
    0x2d4: v2d4(0x20) = SUB v2d1, v2cc
    0x2d6: MSTORE v2cc, v2d4(0x20)
    0x2da: v2da(0x1a) = MLOAD vc4d
    0x2dc: MSTORE v2d1, v2da(0x1a)
    0x2dd: v2dd(0x20) = CONST 
    0x2df: v2df = ADD v2dd(0x20), v2d1
    0x2e3: v2e3(0x1a) = MLOAD vc4d
    0x2e5: v2e5(0x20) = CONST 
    0x2e7: v2e7 = ADD v2e5(0x20), vc4d
    0x2ec: v2ec(0x0) = CONST 

    Begin block 0x2ee
    prev=[0x2c9, 0x2f7], succ=[0x309, 0x2f7]
    =================================
    0x2ee_0x0: v2ee_0 = PHI v2ec(0x0), v302
    0x2f1: v2f1 = LT v2ee_0, v2e3(0x1a)
    0x2f2: v2f2 = ISZERO v2f1
    0x2f3: v2f3(0x309) = CONST 
    0x2f6: JUMPI v2f3(0x309), v2f2

    Begin block 0x309
    prev=[0x2ee], succ=[0x336, 0x31d]
    =================================
    0x312: v312 = ADD v2e3(0x1a), v2df
    0x314: v314(0x1f) = CONST 
    0x316: v316(0x1a) = AND v314(0x1f), v2e3(0x1a)
    0x318: v318 = ISZERO v316(0x1a)
    0x319: v319(0x336) = CONST 
    0x31c: JUMPI v319(0x336), v318

    Begin block 0x336
    prev=[0x309, 0x31d], succ=[]
    =================================
    0x336_0x1: v336_1 = PHI v312, v333
    0x33c: v33c(0x40) = CONST 
    0x33e: v33e = MLOAD v33c(0x40)
    0x341: v341 = SUB v336_1, v33e
    0x343: RETURN v33e, v341

    Begin block 0x31d
    prev=[0x309], succ=[0x336]
    =================================
    0x31f: v31f = SUB v312, v316(0x1a)
    0x321: v321 = MLOAD v31f
    0x322: v322(0x1) = CONST 
    0x325: v325(0x20) = CONST 
    0x327: v327(0x6) = SUB v325(0x20), v316(0x1a)
    0x328: v328(0x100) = CONST 
    0x32b: v32b(0x1000000000000) = EXP v328(0x100), v327(0x6)
    0x32c: v32c(0xffffffffffff) = SUB v32b(0x1000000000000), v322(0x1)
    0x32d: v32d = NOT v32c(0xffffffffffff)
    0x32e: v32e = AND v32d, v321
    0x330: MSTORE v31f, v32e
    0x331: v331(0x20) = CONST 
    0x333: v333 = ADD v331(0x20), v31f

    Begin block 0x2f7
    prev=[0x2ee], succ=[0x2ee]
    =================================
    0x2f7_0x0: v2f7_0 = PHI v2ec(0x0), v302
    0x2f9: v2f9 = ADD v2e7, v2f7_0
    0x2fa: v2fa = MLOAD v2f9
    0x2fd: v2fd = ADD v2df, v2f7_0
    0x2fe: MSTORE v2fd, v2fa
    0x2ff: v2ff(0x20) = CONST 
    0x302: v302 = ADD v2f7_0, v2ff(0x20)
    0x305: v305(0x2ee) = CONST 
    0x308: JUMP v305(0x2ee)

}

function setOwner(address)() public {
    Begin block 0x344
    prev=[], succ=[0x34b, 0x34f]
    =================================
    0x345: v345 = CALLVALUE 
    0x346: v346 = ISZERO v345
    0x347: v347(0x34f) = CONST 
    0x34a: JUMPI v347(0x34f), v346

    Begin block 0x34b
    prev=[0x344], succ=[]
    =================================
    0x34b: v34b(0x0) = CONST 
    0x34e: REVERT v34b(0x0), v34b(0x0)

    Begin block 0x34f
    prev=[0x344], succ=[0xc84]
    =================================
    0x350: v350(0x37b) = CONST 
    0x353: v353(0x4) = CONST 
    0x357: v357 = CALLDATALOAD v353(0x4)
    0x358: v358(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36d: v36d = AND v358(0xffffffffffffffffffffffffffffffffffffffff), v357
    0x36f: v36f(0x20) = CONST 
    0x371: v371(0x24) = ADD v36f(0x20), v353(0x4)
    0x377: v377(0xc84) = CONST 
    0x37a: JUMP v377(0xc84)

    Begin block 0xc84
    prev=[0x34f], succ=[0xcdb, 0xcdf]
    =================================
    0xc85: vc85(0x0) = CONST 
    0xc89: vc89 = SLOAD vc85(0x0)
    0xc8b: vc8b(0x100) = CONST 
    0xc8e: vc8e(0x1) = EXP vc8b(0x100), vc85(0x0)
    0xc90: vc90 = DIV vc89, vc8e(0x1)
    0xc91: vc91(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xca6: vca6 = AND vc91(0xffffffffffffffffffffffffffffffffffffffff), vc90
    0xca7: vca7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcbc: vcbc = AND vca7(0xffffffffffffffffffffffffffffffffffffffff), vca6
    0xcbd: vcbd = CALLER 
    0xcbe: vcbe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcd3: vcd3 = AND vcbe(0xffffffffffffffffffffffffffffffffffffffff), vcbd
    0xcd4: vcd4 = EQ vcd3, vcbc
    0xcd5: vcd5 = ISZERO vcd4
    0xcd6: vcd6 = ISZERO vcd5
    0xcd7: vcd7(0xcdf) = CONST 
    0xcda: JUMPI vcd7(0xcdf), vcd6

    Begin block 0xcdb
    prev=[0xc84], succ=[]
    =================================
    0xcdb: vcdb(0x0) = CONST 
    0xcde: REVERT vcdb(0x0), vcdb(0x0)

    Begin block 0xcdf
    prev=[0xc84], succ=[0xd17, 0xd1b]
    =================================
    0xce0: vce0(0x0) = CONST 
    0xce2: vce2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcf7: vcf7(0x0) = AND vce2(0xffffffffffffffffffffffffffffffffffffffff), vce0(0x0)
    0xcf9: vcf9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd0e: vd0e = AND vcf9(0xffffffffffffffffffffffffffffffffffffffff), v36d
    0xd0f: vd0f = EQ vd0e, vcf7(0x0)
    0xd10: vd10 = ISZERO vd0f
    0xd11: vd11 = ISZERO vd10
    0xd12: vd12 = ISZERO vd11
    0xd13: vd13(0xd1b) = CONST 
    0xd16: JUMPI vd13(0xd1b), vd12

    Begin block 0xd17
    prev=[0xcdf], succ=[]
    =================================
    0xd17: vd17(0x0) = CONST 
    0xd1a: REVERT vd17(0x0), vd17(0x0)

    Begin block 0xd1b
    prev=[0xcdf], succ=[0x37b]
    =================================
    0xd1d: vd1d(0x0) = CONST 
    0xd20: vd20(0x100) = CONST 
    0xd23: vd23(0x1) = EXP vd20(0x100), vd1d(0x0)
    0xd25: vd25 = SLOAD vd1d(0x0)
    0xd27: vd27(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd3c: vd3c(0xffffffffffffffffffffffffffffffffffffffff) = MUL vd27(0xffffffffffffffffffffffffffffffffffffffff), vd23(0x1)
    0xd3d: vd3d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vd3c(0xffffffffffffffffffffffffffffffffffffffff)
    0xd3e: vd3e = AND vd3d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd25
    0xd41: vd41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd56: vd56 = AND vd41(0xffffffffffffffffffffffffffffffffffffffff), v36d
    0xd57: vd57 = MUL vd56, vd23(0x1)
    0xd58: vd58 = OR vd57, vd3e
    0xd5a: SSTORE vd1d(0x0), vd58
    0xd5d: JUMP v350(0x37b)

    Begin block 0x37b
    prev=[0xd1b], succ=[]
    =================================
    0x37c: STOP 

}

function totalSupply()() public {
    Begin block 0x37d
    prev=[], succ=[0x384, 0x388]
    =================================
    0x37e: v37e = CALLVALUE 
    0x37f: v37f = ISZERO v37e
    0x380: v380(0x388) = CONST 
    0x383: JUMPI v380(0x388), v37f

    Begin block 0x384
    prev=[0x37d], succ=[]
    =================================
    0x384: v384(0x0) = CONST 
    0x387: REVERT v384(0x0), v384(0x0)

    Begin block 0x388
    prev=[0x37d], succ=[0xd5e]
    =================================
    0x389: v389(0x390) = CONST 
    0x38c: v38c(0xd5e) = CONST 
    0x38f: JUMP v38c(0xd5e)

    Begin block 0xd5e
    prev=[0x388], succ=[0xd82, 0xdd2]
    =================================
    0xd5f: vd5f(0x0) = CONST 
    0xd61: vd61(0xddc) = CONST 
    0xd64: vd64(0x2) = CONST 
    0xd66: vd66(0x10) = CONST 
    0xd69: vd69(0x20) = CONST 
    0xd6b: vd6b(0x200) = MUL vd69(0x20), vd66(0x10)
    0xd6c: vd6c(0x40) = CONST 
    0xd6e: vd6e = MLOAD vd6c(0x40)
    0xd71: vd71 = ADD vd6e, vd6b(0x200)
    0xd72: vd72(0x40) = CONST 
    0xd74: MSTORE vd72(0x40), vd71
    0xd7a: vd7a(0x10) = CONST 
    0xd7d: vd7d(0x0) = ISZERO vd7a(0x10)
    0xd7e: vd7e(0xdd2) = CONST 
    0xd81: JUMPI vd7e(0xdd2), vd7d(0x0)

    Begin block 0xd82
    prev=[0xd5e], succ=[0xd88]
    =================================
    0xd82: vd82(0x20) = CONST 
    0xd84: vd84(0x200) = MUL vd82(0x20), vd7a(0x10)
    0xd86: vd86 = ADD vd6e, vd84(0x200)

    Begin block 0xd88
    prev=[0xd82, 0xd88], succ=[0xdd2, 0xd88]
    =================================
    0xd88_0x0: vd88_0 = PHI vd6e, vdc5
    0xd88_0x1: vd88_1 = PHI vd64(0x2), vdc9
    0xd8a: vd8a(0x0) = CONST 
    0xd8d: vd8d = SLOAD vd88_1
    0xd8f: vd8f(0x100) = CONST 
    0xd92: vd92(0x1) = EXP vd8f(0x100), vd8a(0x0)
    0xd94: vd94 = DIV vd8d, vd92(0x1)
    0xd95: vd95(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdaa: vdaa = AND vd95(0xffffffffffffffffffffffffffffffffffffffff), vd94
    0xdab: vdab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdc0: vdc0 = AND vdab(0xffffffffffffffffffffffffffffffffffffffff), vdaa
    0xdc2: MSTORE vd88_0, vdc0
    0xdc3: vdc3(0x20) = CONST 
    0xdc5: vdc5 = ADD vdc3(0x20), vd88_0
    0xdc7: vdc7(0x1) = CONST 
    0xdc9: vdc9 = ADD vdc7(0x1), vd88_1
    0xdcd: vdcd = GT vd86, vdc5
    0xdce: vdce(0xd88) = CONST 
    0xdd1: JUMPI vdce(0xd88), vdcd

    Begin block 0xdd2
    prev=[0xd5e, 0xd88], succ=[0x29c90x37d]
    =================================
    0xdd8: vdd8(0x29c9) = CONST 
    0xddb: JUMP vdd8(0x29c9)

    Begin block 0x29c90x37d
    prev=[0xdd2], succ=[0x29d90x37d, 0x29da0x37d]
    =================================
    0x29ca0x37d: v37d29ca(0x0) = CONST 
    0x29cd0x37d: v37d29cd(0x6) = CONST 
    0x29cf0x37d: v37d29cf(0x10) = CONST 
    0x29d20x37d: v37d29d2(0x1) = LT v37d29cd(0x6), v37d29cf(0x10)
    0x29d30x37d: v37d29d3(0x0) = ISZERO v37d29d2(0x1)
    0x29d40x37d: v37d29d4(0x1) = ISZERO v37d29d3(0x0)
    0x29d50x37d: v37d29d5(0x29da) = CONST 
    0x29d80x37d: JUMPI v37d29d5(0x29da), v37d29d4(0x1)

    Begin block 0x29d90x37d
    prev=[0x29c90x37d], succ=[]
    =================================
    0x29d90x37d: THROW 

    Begin block 0x29da0x37d
    prev=[0x29c90x37d], succ=[0xddc]
    =================================
    0x29db0x37d: v37d29db(0x20) = CONST 
    0x29dd0x37d: v37d29dd(0xc0) = MUL v37d29db(0x20), v37d29cd(0x6)
    0x29de0x37d: v37d29de = ADD v37d29dd(0xc0), vd6e
    0x29df0x37d: v37d29df = MLOAD v37d29de
    0x29e50x37d: JUMP vd61(0xddc)

    Begin block 0xddc
    prev=[0x29da0x37d], succ=[0xe43, 0xe47]
    =================================
    0xddd: vddd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf2: vdf2 = AND vddd(0xffffffffffffffffffffffffffffffffffffffff), v37d29df
    0xdf3: vdf3(0xcc8c3c45) = CONST 
    0xdf8: vdf8(0x0) = CONST 
    0xdfa: vdfa(0x40) = CONST 
    0xdfc: vdfc = MLOAD vdfa(0x40)
    0xdfd: vdfd(0x20) = CONST 
    0xdff: vdff = ADD vdfd(0x20), vdfc
    0xe00: MSTORE vdff, vdf8(0x0)
    0xe01: ve01(0x40) = CONST 
    0xe03: ve03 = MLOAD ve01(0x40)
    0xe05: ve05(0xffffffff) = CONST 
    0xe0a: ve0a(0xcc8c3c45) = AND ve05(0xffffffff), vdf3(0xcc8c3c45)
    0xe0b: ve0b(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xe29: ve29(0xcc8c3c4500000000000000000000000000000000000000000000000000000000) = MUL ve0b(0x100000000000000000000000000000000000000000000000000000000), ve0a(0xcc8c3c45)
    0xe2b: MSTORE ve03, ve29(0xcc8c3c4500000000000000000000000000000000000000000000000000000000)
    0xe2c: ve2c(0x4) = CONST 
    0xe2e: ve2e = ADD ve2c(0x4), ve03
    0xe2f: ve2f(0x20) = CONST 
    0xe31: ve31(0x40) = CONST 
    0xe33: ve33 = MLOAD ve31(0x40)
    0xe36: ve36(0x4) = SUB ve2e, ve33
    0xe38: ve38(0x0) = CONST 
    0xe3c: ve3c = EXTCODESIZE vdf2
    0xe3d: ve3d = ISZERO ve3c
    0xe3e: ve3e = ISZERO ve3d
    0xe3f: ve3f(0xe47) = CONST 
    0xe42: JUMPI ve3f(0xe47), ve3e

    Begin block 0xe43
    prev=[0xddc], succ=[]
    =================================
    0xe43: ve43(0x0) = CONST 
    0xe46: REVERT ve43(0x0), ve43(0x0)

    Begin block 0xe47
    prev=[0xddc], succ=[0xe54, 0xe58]
    =================================
    0xe48: ve48(0x2c6) = CONST 
    0xe4b: ve4b = GAS 
    0xe4c: ve4c = SUB ve4b, ve48(0x2c6)
    0xe4d: ve4d = CALL ve4c, vdf2, ve38(0x0), ve33, ve36(0x4), ve33, ve2f(0x20)
    0xe4e: ve4e = ISZERO ve4d
    0xe4f: ve4f = ISZERO ve4e
    0xe50: ve50(0xe58) = CONST 
    0xe53: JUMPI ve50(0xe58), ve4f

    Begin block 0xe54
    prev=[0xe47], succ=[]
    =================================
    0xe54: ve54(0x0) = CONST 
    0xe57: REVERT ve54(0x0), ve54(0x0)

    Begin block 0xe58
    prev=[0xe47], succ=[0x390]
    =================================
    0xe5c: ve5c(0x40) = CONST 
    0xe5e: ve5e = MLOAD ve5c(0x40)
    0xe60: ve60 = MLOAD ve5e
    0xe66: JUMP v389(0x390)

    Begin block 0x390
    prev=[0xe58], succ=[]
    =================================
    0x391: v391(0x40) = CONST 
    0x393: v393 = MLOAD v391(0x40)
    0x397: MSTORE v393, ve60
    0x398: v398(0x20) = CONST 
    0x39a: v39a = ADD v398(0x20), v393
    0x39e: v39e(0x40) = CONST 
    0x3a0: v3a0 = MLOAD v39e(0x40)
    0x3a3: v3a3(0x20) = SUB v39a, v3a0
    0x3a5: RETURN v3a0, v3a3(0x20)

}

function tokenOfOwnerByIndex(address,uint256)() public {
    Begin block 0x3a6
    prev=[], succ=[0x3ad, 0x3b1]
    =================================
    0x3a7: v3a7 = CALLVALUE 
    0x3a8: v3a8 = ISZERO v3a7
    0x3a9: v3a9(0x3b1) = CONST 
    0x3ac: JUMPI v3a9(0x3b1), v3a8

    Begin block 0x3ad
    prev=[0x3a6], succ=[]
    =================================
    0x3ad: v3ad(0x0) = CONST 
    0x3b0: REVERT v3ad(0x0), v3ad(0x0)

    Begin block 0x3b1
    prev=[0x3a6], succ=[0xe67]
    =================================
    0x3b2: v3b2(0x3e6) = CONST 
    0x3b5: v3b5(0x4) = CONST 
    0x3b9: v3b9 = CALLDATALOAD v3b5(0x4)
    0x3ba: v3ba(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3cf: v3cf = AND v3ba(0xffffffffffffffffffffffffffffffffffffffff), v3b9
    0x3d1: v3d1(0x20) = CONST 
    0x3d3: v3d3(0x24) = ADD v3d1(0x20), v3b5(0x4)
    0x3d8: v3d8 = CALLDATALOAD v3d3(0x24)
    0x3da: v3da(0x20) = CONST 
    0x3dc: v3dc(0x44) = ADD v3da(0x20), v3d3(0x24)
    0x3e2: v3e2(0xe67) = CONST 
    0x3e5: JUMP v3e2(0xe67)

    Begin block 0xe67
    prev=[0x3b1], succ=[0xe8b, 0xedb]
    =================================
    0xe68: ve68(0x0) = CONST 
    0xe6a: ve6a(0xee5) = CONST 
    0xe6d: ve6d(0x2) = CONST 
    0xe6f: ve6f(0x10) = CONST 
    0xe72: ve72(0x20) = CONST 
    0xe74: ve74(0x200) = MUL ve72(0x20), ve6f(0x10)
    0xe75: ve75(0x40) = CONST 
    0xe77: ve77 = MLOAD ve75(0x40)
    0xe7a: ve7a = ADD ve77, ve74(0x200)
    0xe7b: ve7b(0x40) = CONST 
    0xe7d: MSTORE ve7b(0x40), ve7a
    0xe83: ve83(0x10) = CONST 
    0xe86: ve86(0x0) = ISZERO ve83(0x10)
    0xe87: ve87(0xedb) = CONST 
    0xe8a: JUMPI ve87(0xedb), ve86(0x0)

    Begin block 0xe8b
    prev=[0xe67], succ=[0xe91]
    =================================
    0xe8b: ve8b(0x20) = CONST 
    0xe8d: ve8d(0x200) = MUL ve8b(0x20), ve83(0x10)
    0xe8f: ve8f = ADD ve77, ve8d(0x200)

    Begin block 0xe91
    prev=[0xe8b, 0xe91], succ=[0xedb, 0xe91]
    =================================
    0xe91_0x0: ve91_0 = PHI ve77, vece
    0xe91_0x1: ve91_1 = PHI ve6d(0x2), ved2
    0xe93: ve93(0x0) = CONST 
    0xe96: ve96 = SLOAD ve91_1
    0xe98: ve98(0x100) = CONST 
    0xe9b: ve9b(0x1) = EXP ve98(0x100), ve93(0x0)
    0xe9d: ve9d = DIV ve96, ve9b(0x1)
    0xe9e: ve9e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeb3: veb3 = AND ve9e(0xffffffffffffffffffffffffffffffffffffffff), ve9d
    0xeb4: veb4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec9: vec9 = AND veb4(0xffffffffffffffffffffffffffffffffffffffff), veb3
    0xecb: MSTORE ve91_0, vec9
    0xecc: vecc(0x20) = CONST 
    0xece: vece = ADD vecc(0x20), ve91_0
    0xed0: ved0(0x1) = CONST 
    0xed2: ved2 = ADD ved0(0x1), ve91_1
    0xed6: ved6 = GT ve8f, vece
    0xed7: ved7(0xe91) = CONST 
    0xeda: JUMPI ved7(0xe91), ved6

    Begin block 0xedb
    prev=[0xe67, 0xe91], succ=[0x29c90x3a6]
    =================================
    0xee1: vee1(0x29c9) = CONST 
    0xee4: JUMP vee1(0x29c9)

    Begin block 0x29c90x3a6
    prev=[0xedb], succ=[0x29d90x3a6, 0x29da0x3a6]
    =================================
    0x29ca0x3a6: v3a629ca(0x0) = CONST 
    0x29cd0x3a6: v3a629cd(0x6) = CONST 
    0x29cf0x3a6: v3a629cf(0x10) = CONST 
    0x29d20x3a6: v3a629d2(0x1) = LT v3a629cd(0x6), v3a629cf(0x10)
    0x29d30x3a6: v3a629d3(0x0) = ISZERO v3a629d2(0x1)
    0x29d40x3a6: v3a629d4(0x1) = ISZERO v3a629d3(0x0)
    0x29d50x3a6: v3a629d5(0x29da) = CONST 
    0x29d80x3a6: JUMPI v3a629d5(0x29da), v3a629d4(0x1)

    Begin block 0x29d90x3a6
    prev=[0x29c90x3a6], succ=[]
    =================================
    0x29d90x3a6: THROW 

    Begin block 0x29da0x3a6
    prev=[0x29c90x3a6], succ=[0xee5]
    =================================
    0x29db0x3a6: v3a629db(0x20) = CONST 
    0x29dd0x3a6: v3a629dd(0xc0) = MUL v3a629db(0x20), v3a629cd(0x6)
    0x29de0x3a6: v3a629de = ADD v3a629dd(0xc0), ve77
    0x29df0x3a6: v3a629df = MLOAD v3a629de
    0x29e50x3a6: JUMP ve6a(0xee5)

    Begin block 0xee5
    prev=[0x29da0x3a6], succ=[0xf8b, 0xf8f]
    =================================
    0xee6: vee6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xefb: vefb = AND vee6(0xffffffffffffffffffffffffffffffffffffffff), v3a629df
    0xefc: vefc(0xbab4e3b1) = CONST 
    0xf03: vf03(0x0) = CONST 
    0xf05: vf05(0x40) = CONST 
    0xf07: vf07 = MLOAD vf05(0x40)
    0xf08: vf08(0x20) = CONST 
    0xf0a: vf0a = ADD vf08(0x20), vf07
    0xf0b: MSTORE vf0a, vf03(0x0)
    0xf0c: vf0c(0x40) = CONST 
    0xf0e: vf0e = MLOAD vf0c(0x40)
    0xf10: vf10(0xffffffff) = CONST 
    0xf15: vf15(0xbab4e3b1) = AND vf10(0xffffffff), vefc(0xbab4e3b1)
    0xf16: vf16(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xf34: vf34(0xbab4e3b100000000000000000000000000000000000000000000000000000000) = MUL vf16(0x100000000000000000000000000000000000000000000000000000000), vf15(0xbab4e3b1)
    0xf36: MSTORE vf0e, vf34(0xbab4e3b100000000000000000000000000000000000000000000000000000000)
    0xf37: vf37(0x4) = CONST 
    0xf39: vf39 = ADD vf37(0x4), vf0e
    0xf3c: vf3c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf51: vf51 = AND vf3c(0xffffffffffffffffffffffffffffffffffffffff), v3cf
    0xf52: vf52(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf67: vf67 = AND vf52(0xffffffffffffffffffffffffffffffffffffffff), vf51
    0xf69: MSTORE vf39, vf67
    0xf6a: vf6a(0x20) = CONST 
    0xf6c: vf6c = ADD vf6a(0x20), vf39
    0xf6f: MSTORE vf6c, v3d8
    0xf70: vf70(0x20) = CONST 
    0xf72: vf72 = ADD vf70(0x20), vf6c
    0xf77: vf77(0x20) = CONST 
    0xf79: vf79(0x40) = CONST 
    0xf7b: vf7b = MLOAD vf79(0x40)
    0xf7e: vf7e(0x44) = SUB vf72, vf7b
    0xf80: vf80(0x0) = CONST 
    0xf84: vf84 = EXTCODESIZE vefb
    0xf85: vf85 = ISZERO vf84
    0xf86: vf86 = ISZERO vf85
    0xf87: vf87(0xf8f) = CONST 
    0xf8a: JUMPI vf87(0xf8f), vf86

    Begin block 0xf8b
    prev=[0xee5], succ=[]
    =================================
    0xf8b: vf8b(0x0) = CONST 
    0xf8e: REVERT vf8b(0x0), vf8b(0x0)

    Begin block 0xf8f
    prev=[0xee5], succ=[0xf9c, 0xfa0]
    =================================
    0xf90: vf90(0x2c6) = CONST 
    0xf93: vf93 = GAS 
    0xf94: vf94 = SUB vf93, vf90(0x2c6)
    0xf95: vf95 = CALL vf94, vefb, vf80(0x0), vf7b, vf7e(0x44), vf7b, vf77(0x20)
    0xf96: vf96 = ISZERO vf95
    0xf97: vf97 = ISZERO vf96
    0xf98: vf98(0xfa0) = CONST 
    0xf9b: JUMPI vf98(0xfa0), vf97

    Begin block 0xf9c
    prev=[0xf8f], succ=[]
    =================================
    0xf9c: vf9c(0x0) = CONST 
    0xf9f: REVERT vf9c(0x0), vf9c(0x0)

    Begin block 0xfa0
    prev=[0xf8f], succ=[0x3e6]
    =================================
    0xfa4: vfa4(0x40) = CONST 
    0xfa6: vfa6 = MLOAD vfa4(0x40)
    0xfa8: vfa8 = MLOAD vfa6
    0xfb1: JUMP v3b2(0x3e6)

    Begin block 0x3e6
    prev=[0xfa0], succ=[]
    =================================
    0x3e7: v3e7(0x40) = CONST 
    0x3e9: v3e9 = MLOAD v3e7(0x40)
    0x3ed: MSTORE v3e9, vfa8
    0x3ee: v3ee(0x20) = CONST 
    0x3f0: v3f0 = ADD v3ee(0x20), v3e9
    0x3f4: v3f4(0x40) = CONST 
    0x3f6: v3f6 = MLOAD v3f4(0x40)
    0x3f9: v3f9(0x20) = SUB v3f0, v3f6
    0x3fb: RETURN v3f6, v3f9(0x20)

}

function unpause()() public {
    Begin block 0x3fc
    prev=[], succ=[0x403, 0x407]
    =================================
    0x3fd: v3fd = CALLVALUE 
    0x3fe: v3fe = ISZERO v3fd
    0x3ff: v3ff(0x407) = CONST 
    0x402: JUMPI v3ff(0x407), v3fe

    Begin block 0x403
    prev=[0x3fc], succ=[]
    =================================
    0x403: v403(0x0) = CONST 
    0x406: REVERT v403(0x0), v403(0x0)

    Begin block 0x407
    prev=[0x3fc], succ=[0xfb2]
    =================================
    0x408: v408(0x40f) = CONST 
    0x40b: v40b(0xfb2) = CONST 
    0x40e: JUMP v40b(0xfb2)

    Begin block 0xfb2
    prev=[0x407], succ=[0x1009, 0x100d]
    =================================
    0xfb3: vfb3(0x0) = CONST 
    0xfb7: vfb7 = SLOAD vfb3(0x0)
    0xfb9: vfb9(0x100) = CONST 
    0xfbc: vfbc(0x1) = EXP vfb9(0x100), vfb3(0x0)
    0xfbe: vfbe = DIV vfb7, vfbc(0x1)
    0xfbf: vfbf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfd4: vfd4 = AND vfbf(0xffffffffffffffffffffffffffffffffffffffff), vfbe
    0xfd5: vfd5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfea: vfea = AND vfd5(0xffffffffffffffffffffffffffffffffffffffff), vfd4
    0xfeb: vfeb = CALLER 
    0xfec: vfec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1001: v1001 = AND vfec(0xffffffffffffffffffffffffffffffffffffffff), vfeb
    0x1002: v1002 = EQ v1001, vfea
    0x1003: v1003 = ISZERO v1002
    0x1004: v1004 = ISZERO v1003
    0x1005: v1005(0x100d) = CONST 
    0x1008: JUMPI v1005(0x100d), v1004

    Begin block 0x1009
    prev=[0xfb2], succ=[]
    =================================
    0x1009: v1009(0x0) = CONST 
    0x100c: REVERT v1009(0x0), v1009(0x0)

    Begin block 0x100d
    prev=[0xfb2], succ=[0x40f]
    =================================
    0x100e: v100e(0x0) = CONST 
    0x1010: v1010(0x12) = CONST 
    0x1012: v1012(0x0) = CONST 
    0x1014: v1014(0x100) = CONST 
    0x1017: v1017(0x1) = EXP v1014(0x100), v1012(0x0)
    0x1019: v1019 = SLOAD v1010(0x12)
    0x101b: v101b(0xff) = CONST 
    0x101d: v101d(0xff) = MUL v101b(0xff), v1017(0x1)
    0x101e: v101e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v101d(0xff)
    0x101f: v101f = AND v101e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1019
    0x1022: v1022(0x1) = ISZERO v100e(0x0)
    0x1023: v1023(0x0) = ISZERO v1022(0x1)
    0x1024: v1024(0x0) = MUL v1023(0x0), v1017(0x1)
    0x1025: v1025 = OR v1024(0x0), v101f
    0x1027: SSTORE v1010(0x12), v1025
    0x1029: JUMP v408(0x40f)

    Begin block 0x40f
    prev=[0x100d], succ=[]
    =================================
    0x410: STOP 

}

function kill()() public {
    Begin block 0x411
    prev=[], succ=[0x418, 0x41c]
    =================================
    0x412: v412 = CALLVALUE 
    0x413: v413 = ISZERO v412
    0x414: v414(0x41c) = CONST 
    0x417: JUMPI v414(0x41c), v413

    Begin block 0x418
    prev=[0x411], succ=[]
    =================================
    0x418: v418(0x0) = CONST 
    0x41b: REVERT v418(0x0), v418(0x0)

    Begin block 0x41c
    prev=[0x411], succ=[0x102a]
    =================================
    0x41d: v41d(0x424) = CONST 
    0x420: v420(0x102a) = CONST 
    0x423: JUMP v420(0x102a)

    Begin block 0x102a
    prev=[0x41c], succ=[0x1081, 0x1085]
    =================================
    0x102b: v102b(0x0) = CONST 
    0x102f: v102f = SLOAD v102b(0x0)
    0x1031: v1031(0x100) = CONST 
    0x1034: v1034(0x1) = EXP v1031(0x100), v102b(0x0)
    0x1036: v1036 = DIV v102f, v1034(0x1)
    0x1037: v1037(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x104c: v104c = AND v1037(0xffffffffffffffffffffffffffffffffffffffff), v1036
    0x104d: v104d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1062: v1062 = AND v104d(0xffffffffffffffffffffffffffffffffffffffff), v104c
    0x1063: v1063 = CALLER 
    0x1064: v1064(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1079: v1079 = AND v1064(0xffffffffffffffffffffffffffffffffffffffff), v1063
    0x107a: v107a = EQ v1079, v1062
    0x107b: v107b = ISZERO v107a
    0x107c: v107c = ISZERO v107b
    0x107d: v107d(0x1085) = CONST 
    0x1080: JUMPI v107d(0x1085), v107c

    Begin block 0x1081
    prev=[0x102a], succ=[]
    =================================
    0x1081: v1081(0x0) = CONST 
    0x1084: REVERT v1081(0x0), v1081(0x0)

    Begin block 0x1085
    prev=[0x102a], succ=[]
    =================================
    0x1086: v1086(0x0) = CONST 
    0x108a: v108a = SLOAD v1086(0x0)
    0x108c: v108c(0x100) = CONST 
    0x108f: v108f(0x1) = EXP v108c(0x100), v1086(0x0)
    0x1091: v1091 = DIV v108a, v108f(0x1)
    0x1092: v1092(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10a7: v10a7 = AND v1092(0xffffffffffffffffffffffffffffffffffffffff), v1091
    0x10a8: v10a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10bd: v10bd = AND v10a8(0xffffffffffffffffffffffffffffffffffffffff), v10a7
    0x10be: SELFDESTRUCT v10bd

}

function contracts(uint256)() public {
    Begin block 0x426
    prev=[], succ=[0x42d, 0x431]
    =================================
    0x427: v427 = CALLVALUE 
    0x428: v428 = ISZERO v427
    0x429: v429(0x431) = CONST 
    0x42c: JUMPI v429(0x431), v428

    Begin block 0x42d
    prev=[0x426], succ=[]
    =================================
    0x42d: v42d(0x0) = CONST 
    0x430: REVERT v42d(0x0), v42d(0x0)

    Begin block 0x431
    prev=[0x426], succ=[0x10bf]
    =================================
    0x432: v432(0x447) = CONST 
    0x435: v435(0x4) = CONST 
    0x439: v439 = CALLDATALOAD v435(0x4)
    0x43b: v43b(0x20) = CONST 
    0x43d: v43d(0x24) = ADD v43b(0x20), v435(0x4)
    0x443: v443(0x10bf) = CONST 
    0x446: JUMP v443(0x10bf)

    Begin block 0x10bf
    prev=[0x431], succ=[0x10cd, 0x10ce]
    =================================
    0x10c0: v10c0(0x2) = CONST 
    0x10c3: v10c3(0x10) = CONST 
    0x10c6: v10c6 = LT v439, v10c3(0x10)
    0x10c7: v10c7 = ISZERO v10c6
    0x10c8: v10c8 = ISZERO v10c7
    0x10c9: v10c9(0x10ce) = CONST 
    0x10cc: JUMPI v10c9(0x10ce), v10c8

    Begin block 0x10cd
    prev=[0x10bf], succ=[]
    =================================
    0x10cd: THROW 

    Begin block 0x10ce
    prev=[0x10bf], succ=[0x447]
    =================================
    0x10cf: v10cf = ADD v439, v10c0(0x2)
    0x10d0: v10d0(0x0) = CONST 
    0x10d4: v10d4 = SLOAD v10cf
    0x10d6: v10d6(0x100) = CONST 
    0x10d9: v10d9(0x1) = EXP v10d6(0x100), v10d0(0x0)
    0x10db: v10db = DIV v10d4, v10d9(0x1)
    0x10dc: v10dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10f1: v10f1 = AND v10dc(0xffffffffffffffffffffffffffffffffffffffff), v10db
    0x10f3: JUMP v432(0x447)

    Begin block 0x447
    prev=[0x10ce], succ=[]
    =================================
    0x448: v448(0x40) = CONST 
    0x44a: v44a = MLOAD v448(0x40)
    0x44d: v44d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x462: v462 = AND v44d(0xffffffffffffffffffffffffffffffffffffffff), v10f1
    0x463: v463(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x478: v478 = AND v463(0xffffffffffffffffffffffffffffffffffffffff), v462
    0x47a: MSTORE v44a, v478
    0x47b: v47b(0x20) = CONST 
    0x47d: v47d = ADD v47b(0x20), v44a
    0x481: v481(0x40) = CONST 
    0x483: v483 = MLOAD v481(0x40)
    0x486: v486(0x20) = SUB v47d, v483
    0x488: RETURN v483, v486(0x20)

}

function deleteRegion(uint256)() public {
    Begin block 0x489
    prev=[], succ=[0x490, 0x494]
    =================================
    0x48a: v48a = CALLVALUE 
    0x48b: v48b = ISZERO v48a
    0x48c: v48c(0x494) = CONST 
    0x48f: JUMPI v48c(0x494), v48b

    Begin block 0x490
    prev=[0x489], succ=[]
    =================================
    0x490: v490(0x0) = CONST 
    0x493: REVERT v490(0x0), v490(0x0)

    Begin block 0x494
    prev=[0x489], succ=[0x10f4B0x494]
    =================================
    0x495: v495(0x4aa) = CONST 
    0x498: v498(0x4) = CONST 
    0x49c: v49c = CALLDATALOAD v498(0x4)
    0x49e: v49e(0x20) = CONST 
    0x4a0: v4a0(0x24) = ADD v49e(0x20), v498(0x4)
    0x4a6: v4a6(0x10f4) = CONST 
    0x4a9: JUMP v4a6(0x10f4)

    Begin block 0x10f4B0x494
    prev=[0x494], succ=[0x119eB0x494, 0x114cB0x494]
    =================================
    0x10f5S0x494: v10f5V494(0x0) = CONST 
    0x10f8S0x494: v10f8V494(0x0) = CONST 
    0x10fbS0x494: v10fbV494 = SLOAD v10f5V494(0x0)
    0x10fdS0x494: v10fdV494(0x100) = CONST 
    0x1100S0x494: v1100V494(0x1) = EXP v10fdV494(0x100), v10f8V494(0x0)
    0x1102S0x494: v1102V494 = DIV v10fbV494, v1100V494(0x1)
    0x1103S0x494: v1103V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1118S0x494: v1118V494 = AND v1103V494(0xffffffffffffffffffffffffffffffffffffffff), v1102V494
    0x1119S0x494: v1119V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x112eS0x494: v112eV494 = AND v1119V494(0xffffffffffffffffffffffffffffffffffffffff), v1118V494
    0x112fS0x494: v112fV494 = CALLER 
    0x1130S0x494: v1130V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1145S0x494: v1145V494 = AND v1130V494(0xffffffffffffffffffffffffffffffffffffffff), v112fV494
    0x1146S0x494: v1146V494 = EQ v1145V494, v112eV494
    0x1148S0x494: v1148V494(0x119e) = CONST 
    0x114bS0x494: JUMPI v1148V494(0x119e), v1146V494

    Begin block 0x119eB0x494
    prev=[0x10f4B0x494, 0x114cB0x494], succ=[0x11a5B0x494, 0x11a9B0x494]
    =================================
    0x119e_0x0S0x494: v119e_0V494 = PHI v1146V494, v119dV494
    0x119fS0x494: v119fV494 = ISZERO v119e_0V494
    0x11a0S0x494: v11a0V494 = ISZERO v119fV494
    0x11a1S0x494: v11a1V494(0x11a9) = CONST 
    0x11a4S0x494: JUMPI v11a1V494(0x11a9), v11a0V494

    Begin block 0x11a5B0x494
    prev=[0x119eB0x494], succ=[]
    =================================
    0x11a5S0x494: v11a5V494(0x0) = CONST 
    0x11a8S0x494: REVERT v11a5V494(0x0), v11a5V494(0x0)

    Begin block 0x11a9B0x494
    prev=[0x119eB0x494], succ=[0x11ffB0x494, 0x124fB0x494]
    =================================
    0x11aaS0x494: v11aaV494(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb) = CONST 
    0x11bfS0x494: v11bfV494(0x28339320) = CONST 
    0x11c4S0x494: v11c4V494(0x2) = CONST 
    0x11c7S0x494: v11c7V494(0x40) = CONST 
    0x11c9S0x494: v11c9V494 = MLOAD v11c7V494(0x40)
    0x11cbS0x494: v11cbV494(0xffffffff) = CONST 
    0x11d0S0x494: v11d0V494(0x28339320) = AND v11cbV494(0xffffffff), v11bfV494(0x28339320)
    0x11d1S0x494: v11d1V494(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x11efS0x494: v11efV494(0x2833932000000000000000000000000000000000000000000000000000000000) = MUL v11d1V494(0x100000000000000000000000000000000000000000000000000000000), v11d0V494(0x28339320)
    0x11f1S0x494: MSTORE v11c9V494, v11efV494(0x2833932000000000000000000000000000000000000000000000000000000000)
    0x11f2S0x494: v11f2V494(0x4) = CONST 
    0x11f4S0x494: v11f4V494 = ADD v11f2V494(0x4), v11c9V494
    0x11f7S0x494: v11f7V494(0x10) = CONST 
    0x11faS0x494: v11faV494(0x0) = ISZERO v11f7V494(0x10)
    0x11fbS0x494: v11fbV494(0x124f) = CONST 
    0x11feS0x494: JUMPI v11fbV494(0x124f), v11faV494(0x0)

    Begin block 0x11ffB0x494
    prev=[0x11a9B0x494], succ=[0x1205B0x494]
    =================================
    0x11ffS0x494: v11ffV494(0x20) = CONST 
    0x1201S0x494: v1201V494(0x200) = MUL v11ffV494(0x20), v11f7V494(0x10)
    0x1203S0x494: v1203V494 = ADD v11f4V494, v1201V494(0x200)

    Begin block 0x1205B0x494
    prev=[0x11ffB0x494, 0x1205B0x494], succ=[0x124fB0x494, 0x1205B0x494]
    =================================
    0x1205_0x0S0x494: v1205_0V494 = PHI v11f4V494, v1242V494
    0x1205_0x1S0x494: v1205_1V494 = PHI v11c4V494(0x2), v1246V494
    0x1207S0x494: v1207V494(0x0) = CONST 
    0x120aS0x494: v120aV494 = SLOAD v1205_1V494
    0x120cS0x494: v120cV494(0x100) = CONST 
    0x120fS0x494: v120fV494(0x1) = EXP v120cV494(0x100), v1207V494(0x0)
    0x1211S0x494: v1211V494 = DIV v120aV494, v120fV494(0x1)
    0x1212S0x494: v1212V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1227S0x494: v1227V494 = AND v1212V494(0xffffffffffffffffffffffffffffffffffffffff), v1211V494
    0x1228S0x494: v1228V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x123dS0x494: v123dV494 = AND v1228V494(0xffffffffffffffffffffffffffffffffffffffff), v1227V494
    0x123fS0x494: MSTORE v1205_0V494, v123dV494
    0x1240S0x494: v1240V494(0x20) = CONST 
    0x1242S0x494: v1242V494 = ADD v1240V494(0x20), v1205_0V494
    0x1244S0x494: v1244V494(0x1) = CONST 
    0x1246S0x494: v1246V494 = ADD v1244V494(0x1), v1205_1V494
    0x124aS0x494: v124aV494 = GT v1203V494, v1242V494
    0x124bS0x494: v124bV494(0x1205) = CONST 
    0x124eS0x494: JUMPI v124bV494(0x1205), v124aV494

    Begin block 0x124fB0x494
    prev=[0x11a9B0x494, 0x1205B0x494], succ=[0x126eB0x494, 0x1272B0x494]
    =================================
    0x124f_0x2S0x494: v124f_2V494 = PHI v1203V494, v11f4V494
    0x1254S0x494: MSTORE v124f_2V494, v49c
    0x1255S0x494: v1255V494(0x20) = CONST 
    0x1257S0x494: v1257V494 = ADD v1255V494(0x20), v124f_2V494
    0x125cS0x494: v125cV494(0x0) = CONST 
    0x125eS0x494: v125eV494(0x40) = CONST 
    0x1260S0x494: v1260V494 = MLOAD v125eV494(0x40)
    0x1263S0x494: v1263V494 = SUB v1257V494, v1260V494
    0x1267S0x494: v1267V494 = EXTCODESIZE v11aaV494(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb)
    0x1268S0x494: v1268V494 = ISZERO v1267V494
    0x1269S0x494: v1269V494 = ISZERO v1268V494
    0x126aS0x494: v126aV494(0x1272) = CONST 
    0x126dS0x494: JUMPI v126aV494(0x1272), v1269V494

    Begin block 0x126eB0x494
    prev=[0x124fB0x494], succ=[]
    =================================
    0x126eS0x494: v126eV494(0x0) = CONST 
    0x1271S0x494: REVERT v126eV494(0x0), v126eV494(0x0)

    Begin block 0x1272B0x494
    prev=[0x124fB0x494], succ=[0x127fB0x494, 0x1283B0x494]
    =================================
    0x1273S0x494: v1273V494(0x2c6) = CONST 
    0x1276S0x494: v1276V494 = GAS 
    0x1277S0x494: v1277V494 = SUB v1276V494, v1273V494(0x2c6)
    0x1278S0x494: v1278V494 = DELEGATECALL v1277V494, v11aaV494(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb), v1260V494, v1263V494, v1260V494, v125cV494(0x0)
    0x1279S0x494: v1279V494 = ISZERO v1278V494
    0x127aS0x494: v127aV494 = ISZERO v1279V494
    0x127bS0x494: v127bV494(0x1283) = CONST 
    0x127eS0x494: JUMPI v127bV494(0x1283), v127aV494

    Begin block 0x127fB0x494
    prev=[0x1272B0x494], succ=[]
    =================================
    0x127fS0x494: v127fV494(0x0) = CONST 
    0x1282S0x494: REVERT v127fV494(0x0), v127fV494(0x0)

    Begin block 0x1283B0x494
    prev=[0x1272B0x494], succ=[0x4aa]
    =================================
    0x128aS0x494: JUMP v495(0x4aa)

    Begin block 0x4aa
    prev=[0x1283B0x494], succ=[]
    =================================
    0x4ab: v4ab(0x40) = CONST 
    0x4ad: v4ad = MLOAD v4ab(0x40)
    0x4b1: MSTORE v4ad, v10f5V494(0x0)
    0x4b2: v4b2(0x20) = CONST 
    0x4b4: v4b4 = ADD v4b2(0x20), v4ad
    0x4b8: v4b8(0x40) = CONST 
    0x4ba: v4ba = MLOAD v4b8(0x40)
    0x4bd: v4bd(0x20) = SUB v4b4, v4ba
    0x4bf: RETURN v4ba, v4bd(0x20)

    Begin block 0x114cB0x494
    prev=[0x10f4B0x494], succ=[0x119eB0x494]
    =================================
    0x114dS0x494: v114dV494(0x1) = CONST 
    0x114fS0x494: v114fV494(0x0) = CONST 
    0x1152S0x494: v1152V494 = SLOAD v114dV494(0x1)
    0x1154S0x494: v1154V494(0x100) = CONST 
    0x1157S0x494: v1157V494(0x1) = EXP v1154V494(0x100), v114fV494(0x0)
    0x1159S0x494: v1159V494 = DIV v1152V494, v1157V494(0x1)
    0x115aS0x494: v115aV494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x116fS0x494: v116fV494 = AND v115aV494(0xffffffffffffffffffffffffffffffffffffffff), v1159V494
    0x1170S0x494: v1170V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1185S0x494: v1185V494 = AND v1170V494(0xffffffffffffffffffffffffffffffffffffffff), v116fV494
    0x1186S0x494: v1186V494 = CALLER 
    0x1187S0x494: v1187V494(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x119cS0x494: v119cV494 = AND v1187V494(0xffffffffffffffffffffffffffffffffffffffff), v1186V494
    0x119dS0x494: v119dV494 = EQ v119cV494, v1185V494

}

function tokenByIndex(uint256)() public {
    Begin block 0x4c0
    prev=[], succ=[0x4c7, 0x4cb]
    =================================
    0x4c1: v4c1 = CALLVALUE 
    0x4c2: v4c2 = ISZERO v4c1
    0x4c3: v4c3(0x4cb) = CONST 
    0x4c6: JUMPI v4c3(0x4cb), v4c2

    Begin block 0x4c7
    prev=[0x4c0], succ=[]
    =================================
    0x4c7: v4c7(0x0) = CONST 
    0x4ca: REVERT v4c7(0x0), v4c7(0x0)

    Begin block 0x4cb
    prev=[0x4c0], succ=[0x128b]
    =================================
    0x4cc: v4cc(0x4e1) = CONST 
    0x4cf: v4cf(0x4) = CONST 
    0x4d3: v4d3 = CALLDATALOAD v4cf(0x4)
    0x4d5: v4d5(0x20) = CONST 
    0x4d7: v4d7(0x24) = ADD v4d5(0x20), v4cf(0x4)
    0x4dd: v4dd(0x128b) = CONST 
    0x4e0: JUMP v4dd(0x128b)

    Begin block 0x128b
    prev=[0x4cb], succ=[0x12af, 0x12ff]
    =================================
    0x128c: v128c(0x0) = CONST 
    0x128e: v128e(0x1309) = CONST 
    0x1291: v1291(0x2) = CONST 
    0x1293: v1293(0x10) = CONST 
    0x1296: v1296(0x20) = CONST 
    0x1298: v1298(0x200) = MUL v1296(0x20), v1293(0x10)
    0x1299: v1299(0x40) = CONST 
    0x129b: v129b = MLOAD v1299(0x40)
    0x129e: v129e = ADD v129b, v1298(0x200)
    0x129f: v129f(0x40) = CONST 
    0x12a1: MSTORE v129f(0x40), v129e
    0x12a7: v12a7(0x10) = CONST 
    0x12aa: v12aa(0x0) = ISZERO v12a7(0x10)
    0x12ab: v12ab(0x12ff) = CONST 
    0x12ae: JUMPI v12ab(0x12ff), v12aa(0x0)

    Begin block 0x12af
    prev=[0x128b], succ=[0x12b5]
    =================================
    0x12af: v12af(0x20) = CONST 
    0x12b1: v12b1(0x200) = MUL v12af(0x20), v12a7(0x10)
    0x12b3: v12b3 = ADD v129b, v12b1(0x200)

    Begin block 0x12b5
    prev=[0x12af, 0x12b5], succ=[0x12ff, 0x12b5]
    =================================
    0x12b5_0x0: v12b5_0 = PHI v129b, v12f2
    0x12b5_0x1: v12b5_1 = PHI v1291(0x2), v12f6
    0x12b7: v12b7(0x0) = CONST 
    0x12ba: v12ba = SLOAD v12b5_1
    0x12bc: v12bc(0x100) = CONST 
    0x12bf: v12bf(0x1) = EXP v12bc(0x100), v12b7(0x0)
    0x12c1: v12c1 = DIV v12ba, v12bf(0x1)
    0x12c2: v12c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12d7: v12d7 = AND v12c2(0xffffffffffffffffffffffffffffffffffffffff), v12c1
    0x12d8: v12d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12ed: v12ed = AND v12d8(0xffffffffffffffffffffffffffffffffffffffff), v12d7
    0x12ef: MSTORE v12b5_0, v12ed
    0x12f0: v12f0(0x20) = CONST 
    0x12f2: v12f2 = ADD v12f0(0x20), v12b5_0
    0x12f4: v12f4(0x1) = CONST 
    0x12f6: v12f6 = ADD v12f4(0x1), v12b5_1
    0x12fa: v12fa = GT v12b3, v12f2
    0x12fb: v12fb(0x12b5) = CONST 
    0x12fe: JUMPI v12fb(0x12b5), v12fa

    Begin block 0x12ff
    prev=[0x128b, 0x12b5], succ=[0x29c90x4c0]
    =================================
    0x1305: v1305(0x29c9) = CONST 
    0x1308: JUMP v1305(0x29c9)

    Begin block 0x29c90x4c0
    prev=[0x12ff], succ=[0x29d90x4c0, 0x29da0x4c0]
    =================================
    0x29ca0x4c0: v4c029ca(0x0) = CONST 
    0x29cd0x4c0: v4c029cd(0x6) = CONST 
    0x29cf0x4c0: v4c029cf(0x10) = CONST 
    0x29d20x4c0: v4c029d2(0x1) = LT v4c029cd(0x6), v4c029cf(0x10)
    0x29d30x4c0: v4c029d3(0x0) = ISZERO v4c029d2(0x1)
    0x29d40x4c0: v4c029d4(0x1) = ISZERO v4c029d3(0x0)
    0x29d50x4c0: v4c029d5(0x29da) = CONST 
    0x29d80x4c0: JUMPI v4c029d5(0x29da), v4c029d4(0x1)

    Begin block 0x29d90x4c0
    prev=[0x29c90x4c0], succ=[]
    =================================
    0x29d90x4c0: THROW 

    Begin block 0x29da0x4c0
    prev=[0x29c90x4c0], succ=[0x1309]
    =================================
    0x29db0x4c0: v4c029db(0x20) = CONST 
    0x29dd0x4c0: v4c029dd(0xc0) = MUL v4c029db(0x20), v4c029cd(0x6)
    0x29de0x4c0: v4c029de = ADD v4c029dd(0xc0), v129b
    0x29df0x4c0: v4c029df = MLOAD v4c029de
    0x29e50x4c0: JUMP v128e(0x1309)

    Begin block 0x1309
    prev=[0x29da0x4c0], succ=[0x137b, 0x137f]
    =================================
    0x130a: v130a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x131f: v131f = AND v130a(0xffffffffffffffffffffffffffffffffffffffff), v4c029df
    0x1320: v1320(0x49f202ff) = CONST 
    0x1326: v1326(0x0) = CONST 
    0x1328: v1328(0x40) = CONST 
    0x132a: v132a = MLOAD v1328(0x40)
    0x132b: v132b(0x20) = CONST 
    0x132d: v132d = ADD v132b(0x20), v132a
    0x132e: MSTORE v132d, v1326(0x0)
    0x132f: v132f(0x40) = CONST 
    0x1331: v1331 = MLOAD v132f(0x40)
    0x1333: v1333(0xffffffff) = CONST 
    0x1338: v1338(0x49f202ff) = AND v1333(0xffffffff), v1320(0x49f202ff)
    0x1339: v1339(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x1357: v1357(0x49f202ff00000000000000000000000000000000000000000000000000000000) = MUL v1339(0x100000000000000000000000000000000000000000000000000000000), v1338(0x49f202ff)
    0x1359: MSTORE v1331, v1357(0x49f202ff00000000000000000000000000000000000000000000000000000000)
    0x135a: v135a(0x4) = CONST 
    0x135c: v135c = ADD v135a(0x4), v1331
    0x1360: MSTORE v135c, v4d3
    0x1361: v1361(0x20) = CONST 
    0x1363: v1363 = ADD v1361(0x20), v135c
    0x1367: v1367(0x20) = CONST 
    0x1369: v1369(0x40) = CONST 
    0x136b: v136b = MLOAD v1369(0x40)
    0x136e: v136e(0x24) = SUB v1363, v136b
    0x1370: v1370(0x0) = CONST 
    0x1374: v1374 = EXTCODESIZE v131f
    0x1375: v1375 = ISZERO v1374
    0x1376: v1376 = ISZERO v1375
    0x1377: v1377(0x137f) = CONST 
    0x137a: JUMPI v1377(0x137f), v1376

    Begin block 0x137b
    prev=[0x1309], succ=[]
    =================================
    0x137b: v137b(0x0) = CONST 
    0x137e: REVERT v137b(0x0), v137b(0x0)

    Begin block 0x137f
    prev=[0x1309], succ=[0x138c, 0x1390]
    =================================
    0x1380: v1380(0x2c6) = CONST 
    0x1383: v1383 = GAS 
    0x1384: v1384 = SUB v1383, v1380(0x2c6)
    0x1385: v1385 = CALL v1384, v131f, v1370(0x0), v136b, v136e(0x24), v136b, v1367(0x20)
    0x1386: v1386 = ISZERO v1385
    0x1387: v1387 = ISZERO v1386
    0x1388: v1388(0x1390) = CONST 
    0x138b: JUMPI v1388(0x1390), v1387

    Begin block 0x138c
    prev=[0x137f], succ=[]
    =================================
    0x138c: v138c(0x0) = CONST 
    0x138f: REVERT v138c(0x0), v138c(0x0)

    Begin block 0x1390
    prev=[0x137f], succ=[0x4e1]
    =================================
    0x1394: v1394(0x40) = CONST 
    0x1396: v1396 = MLOAD v1394(0x40)
    0x1398: v1398 = MLOAD v1396
    0x13a0: JUMP v4cc(0x4e1)

    Begin block 0x4e1
    prev=[0x1390], succ=[]
    =================================
    0x4e2: v4e2(0x40) = CONST 
    0x4e4: v4e4 = MLOAD v4e2(0x40)
    0x4e8: MSTORE v4e4, v1398
    0x4e9: v4e9(0x20) = CONST 
    0x4eb: v4eb = ADD v4e9(0x20), v4e4
    0x4ef: v4ef(0x40) = CONST 
    0x4f1: v4f1 = MLOAD v4ef(0x40)
    0x4f4: v4f4(0x20) = SUB v4eb, v4f1
    0x4f6: RETURN v4f1, v4f4(0x20)

}

function version()() public {
    Begin block 0x4f7
    prev=[], succ=[0x4fe, 0x502]
    =================================
    0x4f8: v4f8 = CALLVALUE 
    0x4f9: v4f9 = ISZERO v4f8
    0x4fa: v4fa(0x502) = CONST 
    0x4fd: JUMPI v4fa(0x502), v4f9

    Begin block 0x4fe
    prev=[0x4f7], succ=[]
    =================================
    0x4fe: v4fe(0x0) = CONST 
    0x501: REVERT v4fe(0x0), v4fe(0x0)

    Begin block 0x502
    prev=[0x4f7], succ=[0x13a1]
    =================================
    0x503: v503(0x50a) = CONST 
    0x506: v506(0x13a1) = CONST 
    0x509: JUMP v506(0x13a1)

    Begin block 0x13a1
    prev=[0x502], succ=[0x50a]
    =================================
    0x13a2: v13a2(0x12) = CONST 
    0x13a4: v13a4(0x2) = CONST 
    0x13a7: v13a7 = SLOAD v13a2(0x12)
    0x13a9: v13a9(0x100) = CONST 
    0x13ac: v13ac(0x10000) = EXP v13a9(0x100), v13a4(0x2)
    0x13ae: v13ae = DIV v13a7, v13ac(0x10000)
    0x13af: v13af(0x1000000000000000000000000000000000000000000000000) = CONST 
    0x13c9: v13c9 = MUL v13af(0x1000000000000000000000000000000000000000000000000), v13ae
    0x13cb: JUMP v503(0x50a)

    Begin block 0x50a
    prev=[0x13a1], succ=[]
    =================================
    0x50b: v50b(0x40) = CONST 
    0x50d: v50d = MLOAD v50b(0x40)
    0x510: v510(0xffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x529: v529(0xffffffffffffffff000000000000000000000000000000000000000000000000) = NOT v510(0xffffffffffffffffffffffffffffffffffffffffffffffff)
    0x52a: v52a = AND v529(0xffffffffffffffff000000000000000000000000000000000000000000000000), v13c9
    0x52b: v52b(0xffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x544: v544(0xffffffffffffffff000000000000000000000000000000000000000000000000) = NOT v52b(0xffffffffffffffffffffffffffffffffffffffffffffffff)
    0x545: v545 = AND v544(0xffffffffffffffff000000000000000000000000000000000000000000000000), v52a
    0x547: MSTORE v50d, v545
    0x548: v548(0x20) = CONST 
    0x54a: v54a = ADD v548(0x20), v50d
    0x54e: v54e(0x40) = CONST 
    0x550: v550 = MLOAD v54e(0x40)
    0x553: v553(0x20) = SUB v54a, v550
    0x555: RETURN v550, v553(0x20)

}

function createRegion(uint256,uint256,uint256,uint256)() public {
    Begin block 0x556
    prev=[], succ=[0x55d, 0x561]
    =================================
    0x557: v557 = CALLVALUE 
    0x558: v558 = ISZERO v557
    0x559: v559(0x561) = CONST 
    0x55c: JUMPI v559(0x561), v558

    Begin block 0x55d
    prev=[0x556], succ=[]
    =================================
    0x55d: v55d(0x0) = CONST 
    0x560: REVERT v55d(0x0), v55d(0x0)

    Begin block 0x561
    prev=[0x556], succ=[0x13cc]
    =================================
    0x562: v562(0x592) = CONST 
    0x565: v565(0x4) = CONST 
    0x569: v569 = CALLDATALOAD v565(0x4)
    0x56b: v56b(0x20) = CONST 
    0x56d: v56d(0x24) = ADD v56b(0x20), v565(0x4)
    0x572: v572 = CALLDATALOAD v56d(0x24)
    0x574: v574(0x20) = CONST 
    0x576: v576(0x44) = ADD v574(0x20), v56d(0x24)
    0x57b: v57b = CALLDATALOAD v576(0x44)
    0x57d: v57d(0x20) = CONST 
    0x57f: v57f(0x64) = ADD v57d(0x20), v576(0x44)
    0x584: v584 = CALLDATALOAD v57f(0x64)
    0x586: v586(0x20) = CONST 
    0x588: v588(0x84) = ADD v586(0x20), v57f(0x64)
    0x58e: v58e(0x13cc) = CONST 
    0x591: JUMP v58e(0x13cc)

    Begin block 0x13cc
    prev=[0x561], succ=[0x1476, 0x1424]
    =================================
    0x13cd: v13cd(0x0) = CONST 
    0x13d0: v13d0(0x0) = CONST 
    0x13d3: v13d3 = SLOAD v13cd(0x0)
    0x13d5: v13d5(0x100) = CONST 
    0x13d8: v13d8(0x1) = EXP v13d5(0x100), v13d0(0x0)
    0x13da: v13da = DIV v13d3, v13d8(0x1)
    0x13db: v13db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13f0: v13f0 = AND v13db(0xffffffffffffffffffffffffffffffffffffffff), v13da
    0x13f1: v13f1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1406: v1406 = AND v13f1(0xffffffffffffffffffffffffffffffffffffffff), v13f0
    0x1407: v1407 = CALLER 
    0x1408: v1408(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x141d: v141d = AND v1408(0xffffffffffffffffffffffffffffffffffffffff), v1407
    0x141e: v141e = EQ v141d, v1406
    0x1420: v1420(0x1476) = CONST 
    0x1423: JUMPI v1420(0x1476), v141e

    Begin block 0x1476
    prev=[0x13cc, 0x1424], succ=[0x147d, 0x1481]
    =================================
    0x1476_0x0: v1476_0 = PHI v141e, v1475
    0x1477: v1477 = ISZERO v1476_0
    0x1478: v1478 = ISZERO v1477
    0x1479: v1479(0x1481) = CONST 
    0x147c: JUMPI v1479(0x1481), v1478

    Begin block 0x147d
    prev=[0x1476], succ=[]
    =================================
    0x147d: v147d(0x0) = CONST 
    0x1480: REVERT v147d(0x0), v147d(0x0)

    Begin block 0x1481
    prev=[0x1476], succ=[0x14e4, 0x1534]
    =================================
    0x1482: v1482(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb) = CONST 
    0x1497: v1497(0xf7a919be) = CONST 
    0x149c: v149c(0x2) = CONST 
    0x149e: v149e = CALLER 
    0x14a3: v14a3(0x0) = CONST 
    0x14a5: v14a5(0x40) = CONST 
    0x14a7: v14a7 = MLOAD v14a5(0x40)
    0x14a8: v14a8(0x20) = CONST 
    0x14aa: v14aa = ADD v14a8(0x20), v14a7
    0x14ab: MSTORE v14aa, v14a3(0x0)
    0x14ac: v14ac(0x40) = CONST 
    0x14ae: v14ae = MLOAD v14ac(0x40)
    0x14b0: v14b0(0xffffffff) = CONST 
    0x14b5: v14b5(0xf7a919be) = AND v14b0(0xffffffff), v1497(0xf7a919be)
    0x14b6: v14b6(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x14d4: v14d4(0xf7a919be00000000000000000000000000000000000000000000000000000000) = MUL v14b6(0x100000000000000000000000000000000000000000000000000000000), v14b5(0xf7a919be)
    0x14d6: MSTORE v14ae, v14d4(0xf7a919be00000000000000000000000000000000000000000000000000000000)
    0x14d7: v14d7(0x4) = CONST 
    0x14d9: v14d9 = ADD v14d7(0x4), v14ae
    0x14dc: v14dc(0x10) = CONST 
    0x14df: v14df(0x0) = ISZERO v14dc(0x10)
    0x14e0: v14e0(0x1534) = CONST 
    0x14e3: JUMPI v14e0(0x1534), v14df(0x0)

    Begin block 0x14e4
    prev=[0x1481], succ=[0x14ea]
    =================================
    0x14e4: v14e4(0x20) = CONST 
    0x14e6: v14e6(0x200) = MUL v14e4(0x20), v14dc(0x10)
    0x14e8: v14e8 = ADD v14d9, v14e6(0x200)

    Begin block 0x14ea
    prev=[0x14e4, 0x14ea], succ=[0x1534, 0x14ea]
    =================================
    0x14ea_0x0: v14ea_0 = PHI v14d9, v1527
    0x14ea_0x1: v14ea_1 = PHI v149c(0x2), v152b
    0x14ec: v14ec(0x0) = CONST 
    0x14ef: v14ef = SLOAD v14ea_1
    0x14f1: v14f1(0x100) = CONST 
    0x14f4: v14f4(0x1) = EXP v14f1(0x100), v14ec(0x0)
    0x14f6: v14f6 = DIV v14ef, v14f4(0x1)
    0x14f7: v14f7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x150c: v150c = AND v14f7(0xffffffffffffffffffffffffffffffffffffffff), v14f6
    0x150d: v150d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1522: v1522 = AND v150d(0xffffffffffffffffffffffffffffffffffffffff), v150c
    0x1524: MSTORE v14ea_0, v1522
    0x1525: v1525(0x20) = CONST 
    0x1527: v1527 = ADD v1525(0x20), v14ea_0
    0x1529: v1529(0x1) = CONST 
    0x152b: v152b = ADD v1529(0x1), v14ea_1
    0x152f: v152f = GT v14e8, v1527
    0x1530: v1530(0x14ea) = CONST 
    0x1533: JUMPI v1530(0x14ea), v152f

    Begin block 0x1534
    prev=[0x1481, 0x14ea], succ=[0x159b, 0x159f]
    =================================
    0x1534_0x2: v1534_2 = PHI v14d9, v14e8
    0x1538: v1538(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x154d: v154d = AND v1538(0xffffffffffffffffffffffffffffffffffffffff), v149e
    0x154e: v154e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1563: v1563 = AND v154e(0xffffffffffffffffffffffffffffffffffffffff), v154d
    0x1565: MSTORE v1534_2, v1563
    0x1566: v1566(0x20) = CONST 
    0x1568: v1568 = ADD v1566(0x20), v1534_2
    0x156b: MSTORE v1568, v569
    0x156c: v156c(0x20) = CONST 
    0x156e: v156e = ADD v156c(0x20), v1568
    0x1571: MSTORE v156e, v572
    0x1572: v1572(0x20) = CONST 
    0x1574: v1574 = ADD v1572(0x20), v156e
    0x1577: MSTORE v1574, v57b
    0x1578: v1578(0x20) = CONST 
    0x157a: v157a = ADD v1578(0x20), v1574
    0x157d: MSTORE v157a, v584
    0x157e: v157e(0x20) = CONST 
    0x1580: v1580 = ADD v157e(0x20), v157a
    0x1589: v1589(0x20) = CONST 
    0x158b: v158b(0x40) = CONST 
    0x158d: v158d = MLOAD v158b(0x40)
    0x1590: v1590 = SUB v1580, v158d
    0x1594: v1594 = EXTCODESIZE v1482(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb)
    0x1595: v1595 = ISZERO v1594
    0x1596: v1596 = ISZERO v1595
    0x1597: v1597(0x159f) = CONST 
    0x159a: JUMPI v1597(0x159f), v1596

    Begin block 0x159b
    prev=[0x1534], succ=[]
    =================================
    0x159b: v159b(0x0) = CONST 
    0x159e: REVERT v159b(0x0), v159b(0x0)

    Begin block 0x159f
    prev=[0x1534], succ=[0x15ac, 0x15b0]
    =================================
    0x15a0: v15a0(0x2c6) = CONST 
    0x15a3: v15a3 = GAS 
    0x15a4: v15a4 = SUB v15a3, v15a0(0x2c6)
    0x15a5: v15a5 = DELEGATECALL v15a4, v1482(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb), v158d, v1590, v158d, v1589(0x20)
    0x15a6: v15a6 = ISZERO v15a5
    0x15a7: v15a7 = ISZERO v15a6
    0x15a8: v15a8(0x15b0) = CONST 
    0x15ab: JUMPI v15a8(0x15b0), v15a7

    Begin block 0x15ac
    prev=[0x159f], succ=[]
    =================================
    0x15ac: v15ac(0x0) = CONST 
    0x15af: REVERT v15ac(0x0), v15ac(0x0)

    Begin block 0x15b0
    prev=[0x159f], succ=[0x592]
    =================================
    0x15b4: v15b4(0x40) = CONST 
    0x15b6: v15b6 = MLOAD v15b4(0x40)
    0x15b8: v15b8 = MLOAD v15b6
    0x15c2: JUMP v562(0x592)

    Begin block 0x592
    prev=[0x15b0], succ=[]
    =================================
    0x593: v593(0x40) = CONST 
    0x595: v595 = MLOAD v593(0x40)
    0x599: MSTORE v595, v13cd(0x0)
    0x59a: v59a(0x20) = CONST 
    0x59c: v59c = ADD v59a(0x20), v595
    0x5a0: v5a0(0x40) = CONST 
    0x5a2: v5a2 = MLOAD v5a0(0x40)
    0x5a5: v5a5(0x20) = SUB v59c, v5a2
    0x5a7: RETURN v5a2, v5a5(0x20)

    Begin block 0x1424
    prev=[0x13cc], succ=[0x1476]
    =================================
    0x1425: v1425(0x1) = CONST 
    0x1427: v1427(0x0) = CONST 
    0x142a: v142a = SLOAD v1425(0x1)
    0x142c: v142c(0x100) = CONST 
    0x142f: v142f(0x1) = EXP v142c(0x100), v1427(0x0)
    0x1431: v1431 = DIV v142a, v142f(0x1)
    0x1432: v1432(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1447: v1447 = AND v1432(0xffffffffffffffffffffffffffffffffffffffff), v1431
    0x1448: v1448(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x145d: v145d = AND v1448(0xffffffffffffffffffffffffffffffffffffffff), v1447
    0x145e: v145e = CALLER 
    0x145f: v145f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1474: v1474 = AND v145f(0xffffffffffffffffffffffffffffffffffffffff), v145e
    0x1475: v1475 = EQ v1474, v145d

}

function paused()() public {
    Begin block 0x5a8
    prev=[], succ=[0x5af, 0x5b3]
    =================================
    0x5a9: v5a9 = CALLVALUE 
    0x5aa: v5aa = ISZERO v5a9
    0x5ab: v5ab(0x5b3) = CONST 
    0x5ae: JUMPI v5ab(0x5b3), v5aa

    Begin block 0x5af
    prev=[0x5a8], succ=[]
    =================================
    0x5af: v5af(0x0) = CONST 
    0x5b2: REVERT v5af(0x0), v5af(0x0)

    Begin block 0x5b3
    prev=[0x5a8], succ=[0x15c3]
    =================================
    0x5b4: v5b4(0x5bb) = CONST 
    0x5b7: v5b7(0x15c3) = CONST 
    0x5ba: JUMP v5b7(0x15c3)

    Begin block 0x15c3
    prev=[0x5b3], succ=[0x5bb]
    =================================
    0x15c4: v15c4(0x12) = CONST 
    0x15c6: v15c6(0x0) = CONST 
    0x15c9: v15c9 = SLOAD v15c4(0x12)
    0x15cb: v15cb(0x100) = CONST 
    0x15ce: v15ce(0x1) = EXP v15cb(0x100), v15c6(0x0)
    0x15d0: v15d0 = DIV v15c9, v15ce(0x1)
    0x15d1: v15d1(0xff) = CONST 
    0x15d3: v15d3 = AND v15d1(0xff), v15d0
    0x15d5: JUMP v5b4(0x5bb)

    Begin block 0x5bb
    prev=[0x15c3], succ=[]
    =================================
    0x5bc: v5bc(0x40) = CONST 
    0x5be: v5be = MLOAD v5bc(0x40)
    0x5c1: v5c1 = ISZERO v15d3
    0x5c2: v5c2 = ISZERO v5c1
    0x5c3: v5c3 = ISZERO v5c2
    0x5c4: v5c4 = ISZERO v5c3
    0x5c6: MSTORE v5be, v5c4
    0x5c7: v5c7(0x20) = CONST 
    0x5c9: v5c9 = ADD v5c7(0x20), v5be
    0x5cd: v5cd(0x40) = CONST 
    0x5cf: v5cf = MLOAD v5cd(0x40)
    0x5d2: v5d2(0x20) = SUB v5c9, v5cf
    0x5d4: RETURN v5cf, v5d2(0x20)

}

function withdrawBalance()() public {
    Begin block 0x5d5
    prev=[], succ=[0x5dc, 0x5e0]
    =================================
    0x5d6: v5d6 = CALLVALUE 
    0x5d7: v5d7 = ISZERO v5d6
    0x5d8: v5d8(0x5e0) = CONST 
    0x5db: JUMPI v5d8(0x5e0), v5d7

    Begin block 0x5dc
    prev=[0x5d5], succ=[]
    =================================
    0x5dc: v5dc(0x0) = CONST 
    0x5df: REVERT v5dc(0x0), v5dc(0x0)

    Begin block 0x5e0
    prev=[0x5d5], succ=[0x15d6B0x5e0]
    =================================
    0x5e1: v5e1(0x5e8) = CONST 
    0x5e4: v5e4(0x15d6) = CONST 
    0x5e7: JUMP v5e4(0x15d6), v5e1(0x5e8)

    Begin block 0x15d6B0x5e0
    prev=[0x5e0], succ=[0x162dB0x5e0, 0x1631B0x5e0]
    =================================
    0x15d7S0x5e0: v15d7V5e0(0x0) = CONST 
    0x15dbS0x5e0: v15dbV5e0 = SLOAD v15d7V5e0(0x0)
    0x15ddS0x5e0: v15ddV5e0(0x100) = CONST 
    0x15e0S0x5e0: v15e0V5e0(0x1) = EXP v15ddV5e0(0x100), v15d7V5e0(0x0)
    0x15e2S0x5e0: v15e2V5e0 = DIV v15dbV5e0, v15e0V5e0(0x1)
    0x15e3S0x5e0: v15e3V5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15f8S0x5e0: v15f8V5e0 = AND v15e3V5e0(0xffffffffffffffffffffffffffffffffffffffff), v15e2V5e0
    0x15f9S0x5e0: v15f9V5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x160eS0x5e0: v160eV5e0 = AND v15f9V5e0(0xffffffffffffffffffffffffffffffffffffffff), v15f8V5e0
    0x160fS0x5e0: v160fV5e0 = CALLER 
    0x1610S0x5e0: v1610V5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1625S0x5e0: v1625V5e0 = AND v1610V5e0(0xffffffffffffffffffffffffffffffffffffffff), v160fV5e0
    0x1626S0x5e0: v1626V5e0 = EQ v1625V5e0, v160eV5e0
    0x1627S0x5e0: v1627V5e0 = ISZERO v1626V5e0
    0x1628S0x5e0: v1628V5e0 = ISZERO v1627V5e0
    0x1629S0x5e0: v1629V5e0(0x1631) = CONST 
    0x162cS0x5e0: JUMPI v1629V5e0(0x1631), v1628V5e0

    Begin block 0x162dB0x5e0
    prev=[0x15d6B0x5e0], succ=[]
    =================================
    0x162dS0x5e0: v162dV5e0(0x0) = CONST 
    0x1630S0x5e0: REVERT v162dV5e0(0x0), v162dV5e0(0x0)

    Begin block 0x1631B0x5e0
    prev=[0x15d6B0x5e0], succ=[0x16a5B0x5e0, 0x16a9B0x5e0]
    =================================
    0x1632S0x5e0: v1632V5e0(0x0) = CONST 
    0x1636S0x5e0: v1636V5e0 = SLOAD v1632V5e0(0x0)
    0x1638S0x5e0: v1638V5e0(0x100) = CONST 
    0x163bS0x5e0: v163bV5e0(0x1) = EXP v1638V5e0(0x100), v1632V5e0(0x0)
    0x163dS0x5e0: v163dV5e0 = DIV v1636V5e0, v163bV5e0(0x1)
    0x163eS0x5e0: v163eV5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1653S0x5e0: v1653V5e0 = AND v163eV5e0(0xffffffffffffffffffffffffffffffffffffffff), v163dV5e0
    0x1654S0x5e0: v1654V5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1669S0x5e0: v1669V5e0 = AND v1654V5e0(0xffffffffffffffffffffffffffffffffffffffff), v1653V5e0
    0x166aS0x5e0: v166aV5e0(0x8fc) = CONST 
    0x166dS0x5e0: v166dV5e0 = ADDRESS 
    0x166eS0x5e0: v166eV5e0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1683S0x5e0: v1683V5e0 = AND v166eV5e0(0xffffffffffffffffffffffffffffffffffffffff), v166dV5e0
    0x1684S0x5e0: v1684V5e0 = BALANCE v1683V5e0
    0x1687S0x5e0: v1687V5e0 = ISZERO v1684V5e0
    0x1688S0x5e0: v1688V5e0 = MUL v1687V5e0, v166aV5e0(0x8fc)
    0x168aS0x5e0: v168aV5e0(0x40) = CONST 
    0x168cS0x5e0: v168cV5e0 = MLOAD v168aV5e0(0x40)
    0x168dS0x5e0: v168dV5e0(0x0) = CONST 
    0x168fS0x5e0: v168fV5e0(0x40) = CONST 
    0x1691S0x5e0: v1691V5e0 = MLOAD v168fV5e0(0x40)
    0x1694S0x5e0: v1694V5e0(0x0) = SUB v168cV5e0, v1691V5e0
    0x1699S0x5e0: v1699V5e0 = CALL v1688V5e0, v1669V5e0, v1684V5e0, v1691V5e0, v1694V5e0(0x0), v1691V5e0, v168dV5e0(0x0)
    0x169fS0x5e0: v169fV5e0 = ISZERO v1699V5e0
    0x16a0S0x5e0: v16a0V5e0 = ISZERO v169fV5e0
    0x16a1S0x5e0: v16a1V5e0(0x16a9) = CONST 
    0x16a4S0x5e0: JUMPI v16a1V5e0(0x16a9), v16a0V5e0

    Begin block 0x16a5B0x5e0
    prev=[0x1631B0x5e0], succ=[]
    =================================
    0x16a5S0x5e0: v16a5V5e0(0x0) = CONST 
    0x16a8S0x5e0: REVERT v16a5V5e0(0x0), v16a5V5e0(0x0)

    Begin block 0x16a9B0x5e0
    prev=[0x1631B0x5e0], succ=[0x5e8]
    =================================
    0x16aaS0x5e0: JUMP v5e1(0x5e8)

    Begin block 0x5e8
    prev=[0x16a9B0x5e0], succ=[]
    =================================
    0x5e9: STOP 

}

function ownerOf(uint256)() public {
    Begin block 0x5ea
    prev=[], succ=[0x5f1, 0x5f5]
    =================================
    0x5eb: v5eb = CALLVALUE 
    0x5ec: v5ec = ISZERO v5eb
    0x5ed: v5ed(0x5f5) = CONST 
    0x5f0: JUMPI v5ed(0x5f5), v5ec

    Begin block 0x5f1
    prev=[0x5ea], succ=[]
    =================================
    0x5f1: v5f1(0x0) = CONST 
    0x5f4: REVERT v5f1(0x0), v5f1(0x0)

    Begin block 0x5f5
    prev=[0x5ea], succ=[0x16ab]
    =================================
    0x5f6: v5f6(0x60b) = CONST 
    0x5f9: v5f9(0x4) = CONST 
    0x5fd: v5fd = CALLDATALOAD v5f9(0x4)
    0x5ff: v5ff(0x20) = CONST 
    0x601: v601(0x24) = ADD v5ff(0x20), v5f9(0x4)
    0x607: v607(0x16ab) = CONST 
    0x60a: JUMP v607(0x16ab)

    Begin block 0x16ab
    prev=[0x5f5], succ=[0x170c, 0x175c]
    =================================
    0x16ac: v16ac(0x0) = CONST 
    0x16ae: v16ae(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a) = CONST 
    0x16c3: v16c3(0xd6e4ddc5) = CONST 
    0x16c8: v16c8(0x2) = CONST 
    0x16cb: v16cb(0x0) = CONST 
    0x16cd: v16cd(0x40) = CONST 
    0x16cf: v16cf = MLOAD v16cd(0x40)
    0x16d0: v16d0(0x20) = CONST 
    0x16d2: v16d2 = ADD v16d0(0x20), v16cf
    0x16d3: MSTORE v16d2, v16cb(0x0)
    0x16d4: v16d4(0x40) = CONST 
    0x16d6: v16d6 = MLOAD v16d4(0x40)
    0x16d8: v16d8(0xffffffff) = CONST 
    0x16dd: v16dd(0xd6e4ddc5) = AND v16d8(0xffffffff), v16c3(0xd6e4ddc5)
    0x16de: v16de(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x16fc: v16fc(0xd6e4ddc500000000000000000000000000000000000000000000000000000000) = MUL v16de(0x100000000000000000000000000000000000000000000000000000000), v16dd(0xd6e4ddc5)
    0x16fe: MSTORE v16d6, v16fc(0xd6e4ddc500000000000000000000000000000000000000000000000000000000)
    0x16ff: v16ff(0x4) = CONST 
    0x1701: v1701 = ADD v16ff(0x4), v16d6
    0x1704: v1704(0x10) = CONST 
    0x1707: v1707(0x0) = ISZERO v1704(0x10)
    0x1708: v1708(0x175c) = CONST 
    0x170b: JUMPI v1708(0x175c), v1707(0x0)

    Begin block 0x170c
    prev=[0x16ab], succ=[0x1712]
    =================================
    0x170c: v170c(0x20) = CONST 
    0x170e: v170e(0x200) = MUL v170c(0x20), v1704(0x10)
    0x1710: v1710 = ADD v1701, v170e(0x200)

    Begin block 0x1712
    prev=[0x170c, 0x1712], succ=[0x175c, 0x1712]
    =================================
    0x1712_0x0: v1712_0 = PHI v1701, v174f
    0x1712_0x1: v1712_1 = PHI v16c8(0x2), v1753
    0x1714: v1714(0x0) = CONST 
    0x1717: v1717 = SLOAD v1712_1
    0x1719: v1719(0x100) = CONST 
    0x171c: v171c(0x1) = EXP v1719(0x100), v1714(0x0)
    0x171e: v171e = DIV v1717, v171c(0x1)
    0x171f: v171f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1734: v1734 = AND v171f(0xffffffffffffffffffffffffffffffffffffffff), v171e
    0x1735: v1735(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x174a: v174a = AND v1735(0xffffffffffffffffffffffffffffffffffffffff), v1734
    0x174c: MSTORE v1712_0, v174a
    0x174d: v174d(0x20) = CONST 
    0x174f: v174f = ADD v174d(0x20), v1712_0
    0x1751: v1751(0x1) = CONST 
    0x1753: v1753 = ADD v1751(0x1), v1712_1
    0x1757: v1757 = GT v1710, v174f
    0x1758: v1758(0x1712) = CONST 
    0x175b: JUMPI v1758(0x1712), v1757

    Begin block 0x175c
    prev=[0x16ab, 0x1712], succ=[0x177b, 0x177f]
    =================================
    0x175c_0x2: v175c_2 = PHI v1701, v1710
    0x1761: MSTORE v175c_2, v5fd
    0x1762: v1762(0x20) = CONST 
    0x1764: v1764 = ADD v1762(0x20), v175c_2
    0x1769: v1769(0x20) = CONST 
    0x176b: v176b(0x40) = CONST 
    0x176d: v176d = MLOAD v176b(0x40)
    0x1770: v1770 = SUB v1764, v176d
    0x1774: v1774 = EXTCODESIZE v16ae(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a)
    0x1775: v1775 = ISZERO v1774
    0x1776: v1776 = ISZERO v1775
    0x1777: v1777(0x177f) = CONST 
    0x177a: JUMPI v1777(0x177f), v1776

    Begin block 0x177b
    prev=[0x175c], succ=[]
    =================================
    0x177b: v177b(0x0) = CONST 
    0x177e: REVERT v177b(0x0), v177b(0x0)

    Begin block 0x177f
    prev=[0x175c], succ=[0x178c, 0x1790]
    =================================
    0x1780: v1780(0x2c6) = CONST 
    0x1783: v1783 = GAS 
    0x1784: v1784 = SUB v1783, v1780(0x2c6)
    0x1785: v1785 = DELEGATECALL v1784, v16ae(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a), v176d, v1770, v176d, v1769(0x20)
    0x1786: v1786 = ISZERO v1785
    0x1787: v1787 = ISZERO v1786
    0x1788: v1788(0x1790) = CONST 
    0x178b: JUMPI v1788(0x1790), v1787

    Begin block 0x178c
    prev=[0x177f], succ=[]
    =================================
    0x178c: v178c(0x0) = CONST 
    0x178f: REVERT v178c(0x0), v178c(0x0)

    Begin block 0x1790
    prev=[0x177f], succ=[0x60b]
    =================================
    0x1794: v1794(0x40) = CONST 
    0x1796: v1796 = MLOAD v1794(0x40)
    0x1798: v1798 = MLOAD v1796
    0x17a0: JUMP v5f6(0x60b)

    Begin block 0x60b
    prev=[0x1790], succ=[]
    =================================
    0x60c: v60c(0x40) = CONST 
    0x60e: v60e = MLOAD v60c(0x40)
    0x611: v611(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x626: v626 = AND v611(0xffffffffffffffffffffffffffffffffffffffff), v1798
    0x627: v627(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x63c: v63c = AND v627(0xffffffffffffffffffffffffffffffffffffffff), v626
    0x63e: MSTORE v60e, v63c
    0x63f: v63f(0x20) = CONST 
    0x641: v641 = ADD v63f(0x20), v60e
    0x645: v645(0x40) = CONST 
    0x647: v647 = MLOAD v645(0x40)
    0x64a: v64a(0x20) = SUB v641, v647
    0x64c: RETURN v647, v64a(0x20)

}

function balanceOf(address)() public {
    Begin block 0x64d
    prev=[], succ=[0x654, 0x658]
    =================================
    0x64e: v64e = CALLVALUE 
    0x64f: v64f = ISZERO v64e
    0x650: v650(0x658) = CONST 
    0x653: JUMPI v650(0x658), v64f

    Begin block 0x654
    prev=[0x64d], succ=[]
    =================================
    0x654: v654(0x0) = CONST 
    0x657: REVERT v654(0x0), v654(0x0)

    Begin block 0x658
    prev=[0x64d], succ=[0x17a1]
    =================================
    0x659: v659(0x684) = CONST 
    0x65c: v65c(0x4) = CONST 
    0x660: v660 = CALLDATALOAD v65c(0x4)
    0x661: v661(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x676: v676 = AND v661(0xffffffffffffffffffffffffffffffffffffffff), v660
    0x678: v678(0x20) = CONST 
    0x67a: v67a(0x24) = ADD v678(0x20), v65c(0x4)
    0x680: v680(0x17a1) = CONST 
    0x683: JUMP v680(0x17a1)

    Begin block 0x17a1
    prev=[0x658], succ=[0x1802, 0x1852]
    =================================
    0x17a2: v17a2(0x0) = CONST 
    0x17a4: v17a4(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a) = CONST 
    0x17b9: v17b9(0xad7f02b5) = CONST 
    0x17be: v17be(0x2) = CONST 
    0x17c1: v17c1(0x0) = CONST 
    0x17c3: v17c3(0x40) = CONST 
    0x17c5: v17c5 = MLOAD v17c3(0x40)
    0x17c6: v17c6(0x20) = CONST 
    0x17c8: v17c8 = ADD v17c6(0x20), v17c5
    0x17c9: MSTORE v17c8, v17c1(0x0)
    0x17ca: v17ca(0x40) = CONST 
    0x17cc: v17cc = MLOAD v17ca(0x40)
    0x17ce: v17ce(0xffffffff) = CONST 
    0x17d3: v17d3(0xad7f02b5) = AND v17ce(0xffffffff), v17b9(0xad7f02b5)
    0x17d4: v17d4(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x17f2: v17f2(0xad7f02b500000000000000000000000000000000000000000000000000000000) = MUL v17d4(0x100000000000000000000000000000000000000000000000000000000), v17d3(0xad7f02b5)
    0x17f4: MSTORE v17cc, v17f2(0xad7f02b500000000000000000000000000000000000000000000000000000000)
    0x17f5: v17f5(0x4) = CONST 
    0x17f7: v17f7 = ADD v17f5(0x4), v17cc
    0x17fa: v17fa(0x10) = CONST 
    0x17fd: v17fd(0x0) = ISZERO v17fa(0x10)
    0x17fe: v17fe(0x1852) = CONST 
    0x1801: JUMPI v17fe(0x1852), v17fd(0x0)

    Begin block 0x1802
    prev=[0x17a1], succ=[0x1808]
    =================================
    0x1802: v1802(0x20) = CONST 
    0x1804: v1804(0x200) = MUL v1802(0x20), v17fa(0x10)
    0x1806: v1806 = ADD v17f7, v1804(0x200)

    Begin block 0x1808
    prev=[0x1802, 0x1808], succ=[0x1852, 0x1808]
    =================================
    0x1808_0x0: v1808_0 = PHI v17f7, v1845
    0x1808_0x1: v1808_1 = PHI v17be(0x2), v1849
    0x180a: v180a(0x0) = CONST 
    0x180d: v180d = SLOAD v1808_1
    0x180f: v180f(0x100) = CONST 
    0x1812: v1812(0x1) = EXP v180f(0x100), v180a(0x0)
    0x1814: v1814 = DIV v180d, v1812(0x1)
    0x1815: v1815(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x182a: v182a = AND v1815(0xffffffffffffffffffffffffffffffffffffffff), v1814
    0x182b: v182b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1840: v1840 = AND v182b(0xffffffffffffffffffffffffffffffffffffffff), v182a
    0x1842: MSTORE v1808_0, v1840
    0x1843: v1843(0x20) = CONST 
    0x1845: v1845 = ADD v1843(0x20), v1808_0
    0x1847: v1847(0x1) = CONST 
    0x1849: v1849 = ADD v1847(0x1), v1808_1
    0x184d: v184d = GT v1806, v1845
    0x184e: v184e(0x1808) = CONST 
    0x1851: JUMPI v184e(0x1808), v184d

    Begin block 0x1852
    prev=[0x17a1, 0x1808], succ=[0x189d, 0x18a1]
    =================================
    0x1852_0x2: v1852_2 = PHI v17f7, v1806
    0x1856: v1856(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x186b: v186b = AND v1856(0xffffffffffffffffffffffffffffffffffffffff), v676
    0x186c: v186c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1881: v1881 = AND v186c(0xffffffffffffffffffffffffffffffffffffffff), v186b
    0x1883: MSTORE v1852_2, v1881
    0x1884: v1884(0x20) = CONST 
    0x1886: v1886 = ADD v1884(0x20), v1852_2
    0x188b: v188b(0x20) = CONST 
    0x188d: v188d(0x40) = CONST 
    0x188f: v188f = MLOAD v188d(0x40)
    0x1892: v1892 = SUB v1886, v188f
    0x1896: v1896 = EXTCODESIZE v17a4(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a)
    0x1897: v1897 = ISZERO v1896
    0x1898: v1898 = ISZERO v1897
    0x1899: v1899(0x18a1) = CONST 
    0x189c: JUMPI v1899(0x18a1), v1898

    Begin block 0x189d
    prev=[0x1852], succ=[]
    =================================
    0x189d: v189d(0x0) = CONST 
    0x18a0: REVERT v189d(0x0), v189d(0x0)

    Begin block 0x18a1
    prev=[0x1852], succ=[0x18ae, 0x18b2]
    =================================
    0x18a2: v18a2(0x2c6) = CONST 
    0x18a5: v18a5 = GAS 
    0x18a6: v18a6 = SUB v18a5, v18a2(0x2c6)
    0x18a7: v18a7 = DELEGATECALL v18a6, v17a4(0x9f51e7e4ceb88982da1695297ff7ca591ca2327a), v188f, v1892, v188f, v188b(0x20)
    0x18a8: v18a8 = ISZERO v18a7
    0x18a9: v18a9 = ISZERO v18a8
    0x18aa: v18aa(0x18b2) = CONST 
    0x18ad: JUMPI v18aa(0x18b2), v18a9

    Begin block 0x18ae
    prev=[0x18a1], succ=[]
    =================================
    0x18ae: v18ae(0x0) = CONST 
    0x18b1: REVERT v18ae(0x0), v18ae(0x0)

    Begin block 0x18b2
    prev=[0x18a1], succ=[0x684]
    =================================
    0x18b6: v18b6(0x40) = CONST 
    0x18b8: v18b8 = MLOAD v18b6(0x40)
    0x18ba: v18ba = MLOAD v18b8
    0x18c2: JUMP v659(0x684)

    Begin block 0x684
    prev=[0x18b2], succ=[]
    =================================
    0x685: v685(0x40) = CONST 
    0x687: v687 = MLOAD v685(0x40)
    0x68b: MSTORE v687, v18ba
    0x68c: v68c(0x20) = CONST 
    0x68e: v68e = ADD v68c(0x20), v687
    0x692: v692(0x40) = CONST 
    0x694: v694 = MLOAD v692(0x40)
    0x697: v697(0x20) = SUB v68e, v694
    0x699: RETURN v694, v697(0x20)

}

function pause()() public {
    Begin block 0x69a
    prev=[], succ=[0x6a1, 0x6a5]
    =================================
    0x69b: v69b = CALLVALUE 
    0x69c: v69c = ISZERO v69b
    0x69d: v69d(0x6a5) = CONST 
    0x6a0: JUMPI v69d(0x6a5), v69c

    Begin block 0x6a1
    prev=[0x69a], succ=[]
    =================================
    0x6a1: v6a1(0x0) = CONST 
    0x6a4: REVERT v6a1(0x0), v6a1(0x0)

    Begin block 0x6a5
    prev=[0x69a], succ=[0x18c3]
    =================================
    0x6a6: v6a6(0x6ad) = CONST 
    0x6a9: v6a9(0x18c3) = CONST 
    0x6ac: JUMP v6a9(0x18c3)

    Begin block 0x18c3
    prev=[0x6a5], succ=[0x196b, 0x1919]
    =================================
    0x18c4: v18c4(0x0) = CONST 
    0x18c8: v18c8 = SLOAD v18c4(0x0)
    0x18ca: v18ca(0x100) = CONST 
    0x18cd: v18cd(0x1) = EXP v18ca(0x100), v18c4(0x0)
    0x18cf: v18cf = DIV v18c8, v18cd(0x1)
    0x18d0: v18d0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18e5: v18e5 = AND v18d0(0xffffffffffffffffffffffffffffffffffffffff), v18cf
    0x18e6: v18e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18fb: v18fb = AND v18e6(0xffffffffffffffffffffffffffffffffffffffff), v18e5
    0x18fc: v18fc = CALLER 
    0x18fd: v18fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1912: v1912 = AND v18fd(0xffffffffffffffffffffffffffffffffffffffff), v18fc
    0x1913: v1913 = EQ v1912, v18fb
    0x1915: v1915(0x196b) = CONST 
    0x1918: JUMPI v1915(0x196b), v1913

    Begin block 0x196b
    prev=[0x18c3, 0x1919], succ=[0x1972, 0x1976]
    =================================
    0x196b_0x0: v196b_0 = PHI v1913, v196a
    0x196c: v196c = ISZERO v196b_0
    0x196d: v196d = ISZERO v196c
    0x196e: v196e(0x1976) = CONST 
    0x1971: JUMPI v196e(0x1976), v196d

    Begin block 0x1972
    prev=[0x196b], succ=[]
    =================================
    0x1972: v1972(0x0) = CONST 
    0x1975: REVERT v1972(0x0), v1972(0x0)

    Begin block 0x1976
    prev=[0x196b], succ=[0x6ad]
    =================================
    0x1977: v1977(0x1) = CONST 
    0x1979: v1979(0x12) = CONST 
    0x197b: v197b(0x0) = CONST 
    0x197d: v197d(0x100) = CONST 
    0x1980: v1980(0x1) = EXP v197d(0x100), v197b(0x0)
    0x1982: v1982 = SLOAD v1979(0x12)
    0x1984: v1984(0xff) = CONST 
    0x1986: v1986(0xff) = MUL v1984(0xff), v1980(0x1)
    0x1987: v1987(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1986(0xff)
    0x1988: v1988 = AND v1987(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1982
    0x198b: v198b(0x0) = ISZERO v1977(0x1)
    0x198c: v198c(0x1) = ISZERO v198b(0x0)
    0x198d: v198d(0x1) = MUL v198c(0x1), v1980(0x1)
    0x198e: v198e = OR v198d(0x1), v1988
    0x1990: SSTORE v1979(0x12), v198e
    0x1992: JUMP v6a6(0x6ad)

    Begin block 0x6ad
    prev=[0x1976], succ=[]
    =================================
    0x6ae: STOP 

    Begin block 0x1919
    prev=[0x18c3], succ=[0x196b]
    =================================
    0x191a: v191a(0x1) = CONST 
    0x191c: v191c(0x0) = CONST 
    0x191f: v191f = SLOAD v191a(0x1)
    0x1921: v1921(0x100) = CONST 
    0x1924: v1924(0x1) = EXP v1921(0x100), v191c(0x0)
    0x1926: v1926 = DIV v191f, v1924(0x1)
    0x1927: v1927(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x193c: v193c = AND v1927(0xffffffffffffffffffffffffffffffffffffffff), v1926
    0x193d: v193d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1952: v1952 = AND v193d(0xffffffffffffffffffffffffffffffffffffffff), v193c
    0x1953: v1953 = CALLER 
    0x1954: v1954(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1969: v1969 = AND v1954(0xffffffffffffffffffffffffffffffffffffffff), v1953
    0x196a: v196a = EQ v1969, v1952

}

function updateRegionPixelPrice(uint256,uint256)() public {
    Begin block 0x6af
    prev=[], succ=[0x1993B0x6af]
    =================================
    0x6b0: v6b0(0x6ce) = CONST 
    0x6b3: v6b3(0x4) = CONST 
    0x6b7: v6b7 = CALLDATALOAD v6b3(0x4)
    0x6b9: v6b9(0x20) = CONST 
    0x6bb: v6bb(0x24) = ADD v6b9(0x20), v6b3(0x4)
    0x6c0: v6c0 = CALLDATALOAD v6bb(0x24)
    0x6c2: v6c2(0x20) = CONST 
    0x6c4: v6c4(0x44) = ADD v6c2(0x20), v6bb(0x24)
    0x6ca: v6ca(0x1993) = CONST 
    0x6cd: JUMP v6ca(0x1993), v6c0, v6b7, v6b0(0x6ce)

    Begin block 0x1993B0x6af
    prev=[0x6af], succ=[0x19bcB0x6af, 0x19abB0x6af]
    =================================
    0x1994S0x6af: v1994V6af(0x12) = CONST 
    0x1996S0x6af: v1996V6af(0x0) = CONST 
    0x1999S0x6af: v1999V6af = SLOAD v1994V6af(0x12)
    0x199bS0x6af: v199bV6af(0x100) = CONST 
    0x199eS0x6af: v199eV6af(0x1) = EXP v199bV6af(0x100), v1996V6af(0x0)
    0x19a0S0x6af: v19a0V6af = DIV v1999V6af, v199eV6af(0x1)
    0x19a1S0x6af: v19a1V6af(0xff) = CONST 
    0x19a3S0x6af: v19a3V6af = AND v19a1V6af(0xff), v19a0V6af
    0x19a4S0x6af: v19a4V6af = ISZERO v19a3V6af
    0x19a6S0x6af: v19a6V6af = ISZERO v19a4V6af
    0x19a7S0x6af: v19a7V6af(0x19bc) = CONST 
    0x19aaS0x6af: JUMPI v19a7V6af(0x19bc), v19a6V6af

    Begin block 0x19bcB0x6af
    prev=[0x1993B0x6af, 0x19abB0x6af], succ=[0x19c3B0x6af, 0x19c7B0x6af]
    =================================
    0x19bc_0x0S0x6af: v19bc_0V6af = PHI v19a4V6af, v19bbV6af
    0x19bdS0x6af: v19bdV6af = ISZERO v19bc_0V6af
    0x19beS0x6af: v19beV6af = ISZERO v19bdV6af
    0x19bfS0x6af: v19bfV6af(0x19c7) = CONST 
    0x19c2S0x6af: JUMPI v19bfV6af(0x19c7), v19beV6af

    Begin block 0x19c3B0x6af
    prev=[0x19bcB0x6af], succ=[]
    =================================
    0x19c3S0x6af: v19c3V6af(0x0) = CONST 
    0x19c6S0x6af: REVERT v19c3V6af(0x0), v19c3V6af(0x0)

    Begin block 0x19c7B0x6af
    prev=[0x19bcB0x6af], succ=[0x1a1eB0x6af, 0x1a6eB0x6af]
    =================================
    0x19c8S0x6af: v19c8V6af(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb) = CONST 
    0x19ddS0x6af: v19ddV6af(0x42f88548) = CONST 
    0x19e2S0x6af: v19e2V6af(0x2) = CONST 
    0x19e6S0x6af: v19e6V6af(0x40) = CONST 
    0x19e8S0x6af: v19e8V6af = MLOAD v19e6V6af(0x40)
    0x19eaS0x6af: v19eaV6af(0xffffffff) = CONST 
    0x19efS0x6af: v19efV6af(0x42f88548) = AND v19eaV6af(0xffffffff), v19ddV6af(0x42f88548)
    0x19f0S0x6af: v19f0V6af(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x1a0eS0x6af: v1a0eV6af(0x42f8854800000000000000000000000000000000000000000000000000000000) = MUL v19f0V6af(0x100000000000000000000000000000000000000000000000000000000), v19efV6af(0x42f88548)
    0x1a10S0x6af: MSTORE v19e8V6af, v1a0eV6af(0x42f8854800000000000000000000000000000000000000000000000000000000)
    0x1a11S0x6af: v1a11V6af(0x4) = CONST 
    0x1a13S0x6af: v1a13V6af = ADD v1a11V6af(0x4), v19e8V6af
    0x1a16S0x6af: v1a16V6af(0x10) = CONST 
    0x1a19S0x6af: v1a19V6af(0x0) = ISZERO v1a16V6af(0x10)
    0x1a1aS0x6af: v1a1aV6af(0x1a6e) = CONST 
    0x1a1dS0x6af: JUMPI v1a1aV6af(0x1a6e), v1a19V6af(0x0)

    Begin block 0x1a1eB0x6af
    prev=[0x19c7B0x6af], succ=[0x1a24B0x6af]
    =================================
    0x1a1eS0x6af: v1a1eV6af(0x20) = CONST 
    0x1a20S0x6af: v1a20V6af(0x200) = MUL v1a1eV6af(0x20), v1a16V6af(0x10)
    0x1a22S0x6af: v1a22V6af = ADD v1a13V6af, v1a20V6af(0x200)

    Begin block 0x1a24B0x6af
    prev=[0x1a1eB0x6af, 0x1a24B0x6af], succ=[0x1a6eB0x6af, 0x1a24B0x6af]
    =================================
    0x1a24_0x0S0x6af: v1a24_0V6af = PHI v1a13V6af, v1a61V6af
    0x1a24_0x1S0x6af: v1a24_1V6af = PHI v19e2V6af(0x2), v1a65V6af
    0x1a26S0x6af: v1a26V6af(0x0) = CONST 
    0x1a29S0x6af: v1a29V6af = SLOAD v1a24_1V6af
    0x1a2bS0x6af: v1a2bV6af(0x100) = CONST 
    0x1a2eS0x6af: v1a2eV6af(0x1) = EXP v1a2bV6af(0x100), v1a26V6af(0x0)
    0x1a30S0x6af: v1a30V6af = DIV v1a29V6af, v1a2eV6af(0x1)
    0x1a31S0x6af: v1a31V6af(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a46S0x6af: v1a46V6af = AND v1a31V6af(0xffffffffffffffffffffffffffffffffffffffff), v1a30V6af
    0x1a47S0x6af: v1a47V6af(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a5cS0x6af: v1a5cV6af = AND v1a47V6af(0xffffffffffffffffffffffffffffffffffffffff), v1a46V6af
    0x1a5eS0x6af: MSTORE v1a24_0V6af, v1a5cV6af
    0x1a5fS0x6af: v1a5fV6af(0x20) = CONST 
    0x1a61S0x6af: v1a61V6af = ADD v1a5fV6af(0x20), v1a24_0V6af
    0x1a63S0x6af: v1a63V6af(0x1) = CONST 
    0x1a65S0x6af: v1a65V6af = ADD v1a63V6af(0x1), v1a24_1V6af
    0x1a69S0x6af: v1a69V6af = GT v1a22V6af, v1a61V6af
    0x1a6aS0x6af: v1a6aV6af(0x1a24) = CONST 
    0x1a6dS0x6af: JUMPI v1a6aV6af(0x1a24), v1a69V6af

    Begin block 0x1a6eB0x6af
    prev=[0x19c7B0x6af, 0x1a24B0x6af], succ=[0x1a94B0x6af, 0x1a98B0x6af]
    =================================
    0x1a6e_0x2S0x6af: v1a6e_2V6af = PHI v1a22V6af, v1a13V6af
    0x1a73S0x6af: MSTORE v1a6e_2V6af, v6b7
    0x1a74S0x6af: v1a74V6af(0x20) = CONST 
    0x1a76S0x6af: v1a76V6af = ADD v1a74V6af(0x20), v1a6e_2V6af
    0x1a79S0x6af: MSTORE v1a76V6af, v6c0
    0x1a7aS0x6af: v1a7aV6af(0x20) = CONST 
    0x1a7cS0x6af: v1a7cV6af = ADD v1a7aV6af(0x20), v1a76V6af
    0x1a82S0x6af: v1a82V6af(0x0) = CONST 
    0x1a84S0x6af: v1a84V6af(0x40) = CONST 
    0x1a86S0x6af: v1a86V6af = MLOAD v1a84V6af(0x40)
    0x1a89S0x6af: v1a89V6af = SUB v1a7cV6af, v1a86V6af
    0x1a8dS0x6af: v1a8dV6af = EXTCODESIZE v19c8V6af(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb)
    0x1a8eS0x6af: v1a8eV6af = ISZERO v1a8dV6af
    0x1a8fS0x6af: v1a8fV6af = ISZERO v1a8eV6af
    0x1a90S0x6af: v1a90V6af(0x1a98) = CONST 
    0x1a93S0x6af: JUMPI v1a90V6af(0x1a98), v1a8fV6af

    Begin block 0x1a94B0x6af
    prev=[0x1a6eB0x6af], succ=[]
    =================================
    0x1a94S0x6af: v1a94V6af(0x0) = CONST 
    0x1a97S0x6af: REVERT v1a94V6af(0x0), v1a94V6af(0x0)

    Begin block 0x1a98B0x6af
    prev=[0x1a6eB0x6af], succ=[0x1aa5B0x6af, 0x1aa9B0x6af]
    =================================
    0x1a99S0x6af: v1a99V6af(0x2c6) = CONST 
    0x1a9cS0x6af: v1a9cV6af = GAS 
    0x1a9dS0x6af: v1a9dV6af = SUB v1a9cV6af, v1a99V6af(0x2c6)
    0x1a9eS0x6af: v1a9eV6af = DELEGATECALL v1a9dV6af, v19c8V6af(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb), v1a86V6af, v1a89V6af, v1a86V6af, v1a82V6af(0x0)
    0x1a9fS0x6af: v1a9fV6af = ISZERO v1a9eV6af
    0x1aa0S0x6af: v1aa0V6af = ISZERO v1a9fV6af
    0x1aa1S0x6af: v1aa1V6af(0x1aa9) = CONST 
    0x1aa4S0x6af: JUMPI v1aa1V6af(0x1aa9), v1aa0V6af

    Begin block 0x1aa5B0x6af
    prev=[0x1a98B0x6af], succ=[]
    =================================
    0x1aa5S0x6af: v1aa5V6af(0x0) = CONST 
    0x1aa8S0x6af: REVERT v1aa5V6af(0x0), v1aa5V6af(0x0)

    Begin block 0x1aa9B0x6af
    prev=[0x1a98B0x6af], succ=[0x6ce]
    =================================
    0x1aafS0x6af: JUMP v6b0(0x6ce)

    Begin block 0x6ce
    prev=[0x1aa9B0x6af], succ=[]
    =================================
    0x6cf: STOP 

    Begin block 0x19abB0x6af
    prev=[0x1993B0x6af], succ=[0x19bcB0x6af]
    =================================
    0x19acS0x6af: v19acV6af(0x12) = CONST 
    0x19aeS0x6af: v19aeV6af(0x1) = CONST 
    0x19b1S0x6af: v19b1V6af = SLOAD v19acV6af(0x12)
    0x19b3S0x6af: v19b3V6af(0x100) = CONST 
    0x19b6S0x6af: v19b6V6af(0x100) = EXP v19b3V6af(0x100), v19aeV6af(0x1)
    0x19b8S0x6af: v19b8V6af = DIV v19b1V6af, v19b6V6af(0x100)
    0x19b9S0x6af: v19b9V6af(0xff) = CONST 
    0x19bbS0x6af: v19bbV6af = AND v19b9V6af(0xff), v19b8V6af

}

function ownerAddress()() public {
    Begin block 0x6d0
    prev=[], succ=[0x6d7, 0x6db]
    =================================
    0x6d1: v6d1 = CALLVALUE 
    0x6d2: v6d2 = ISZERO v6d1
    0x6d3: v6d3(0x6db) = CONST 
    0x6d6: JUMPI v6d3(0x6db), v6d2

    Begin block 0x6d7
    prev=[0x6d0], succ=[]
    =================================
    0x6d7: v6d7(0x0) = CONST 
    0x6da: REVERT v6d7(0x0), v6d7(0x0)

    Begin block 0x6db
    prev=[0x6d0], succ=[0x1ab0]
    =================================
    0x6dc: v6dc(0x6e3) = CONST 
    0x6df: v6df(0x1ab0) = CONST 
    0x6e2: JUMP v6df(0x1ab0)

    Begin block 0x1ab0
    prev=[0x6db], succ=[0x6e3]
    =================================
    0x1ab1: v1ab1(0x0) = CONST 
    0x1ab5: v1ab5 = SLOAD v1ab1(0x0)
    0x1ab7: v1ab7(0x100) = CONST 
    0x1aba: v1aba(0x1) = EXP v1ab7(0x100), v1ab1(0x0)
    0x1abc: v1abc = DIV v1ab5, v1aba(0x1)
    0x1abd: v1abd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ad2: v1ad2 = AND v1abd(0xffffffffffffffffffffffffffffffffffffffff), v1abc
    0x1ad4: JUMP v6dc(0x6e3)

    Begin block 0x6e3
    prev=[0x1ab0], succ=[]
    =================================
    0x6e4: v6e4(0x40) = CONST 
    0x6e6: v6e6 = MLOAD v6e4(0x40)
    0x6e9: v6e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6fe: v6fe = AND v6e9(0xffffffffffffffffffffffffffffffffffffffff), v1ad2
    0x6ff: v6ff(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x714: v714 = AND v6ff(0xffffffffffffffffffffffffffffffffffffffff), v6fe
    0x716: MSTORE v6e6, v714
    0x717: v717(0x20) = CONST 
    0x719: v719 = ADD v717(0x20), v6e6
    0x71d: v71d(0x40) = CONST 
    0x71f: v71f = MLOAD v71d(0x40)
    0x722: v722(0x20) = SUB v719, v71f
    0x724: RETURN v71f, v722(0x20)

}

function symbol()() public {
    Begin block 0x725
    prev=[], succ=[0x72c, 0x730]
    =================================
    0x726: v726 = CALLVALUE 
    0x727: v727 = ISZERO v726
    0x728: v728(0x730) = CONST 
    0x72b: JUMPI v728(0x730), v727

    Begin block 0x72c
    prev=[0x725], succ=[]
    =================================
    0x72c: v72c(0x0) = CONST 
    0x72f: REVERT v72c(0x0), v72c(0x0)

    Begin block 0x730
    prev=[0x725], succ=[0x1ad5]
    =================================
    0x731: v731(0x738) = CONST 
    0x734: v734(0x1ad5) = CONST 
    0x737: JUMP v734(0x1ad5)

    Begin block 0x1ad5
    prev=[0x730], succ=[0x29faB0x1ad5]
    =================================
    0x1ad6: v1ad6(0x1add) = CONST 
    0x1ad9: v1ad9(0x29fa) = CONST 
    0x1adc: JUMP v1ad9(0x29fa)

    Begin block 0x29faB0x1ad5
    prev=[0x1ad5], succ=[0x1add]
    =================================
    0x29fbS0x1ad5: v29fbV1ad5(0x20) = CONST 
    0x29fdS0x1ad5: v29fdV1ad5(0x40) = CONST 
    0x29ffS0x1ad5: v29ffV1ad5 = MLOAD v29fdV1ad5(0x40)
    0x2a02S0x1ad5: v2a02V1ad5 = ADD v29ffV1ad5, v29fbV1ad5(0x20)
    0x2a03S0x1ad5: v2a03V1ad5(0x40) = CONST 
    0x2a05S0x1ad5: MSTORE v2a03V1ad5(0x40), v2a02V1ad5
    0x2a07S0x1ad5: v2a07V1ad5(0x0) = CONST 
    0x2a0aS0x1ad5: MSTORE v29ffV1ad5, v2a07V1ad5(0x0)
    0x2a0dS0x1ad5: JUMP v1ad6(0x1add)

    Begin block 0x1add
    prev=[0x29faB0x1ad5], succ=[0x738]
    =================================
    0x1ade: v1ade(0x40) = CONST 
    0x1ae1: v1ae1 = MLOAD v1ade(0x40)
    0x1ae4: v1ae4 = ADD v1ae1, v1ade(0x40)
    0x1ae5: v1ae5(0x40) = CONST 
    0x1ae7: MSTORE v1ae5(0x40), v1ae4
    0x1ae9: v1ae9(0x3) = CONST 
    0x1aec: MSTORE v1ae1, v1ae9(0x3)
    0x1aed: v1aed(0x20) = CONST 
    0x1aef: v1aef = ADD v1aed(0x20), v1ae1
    0x1af0: v1af0(0x4244500000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1b12: MSTORE v1aef, v1af0(0x4244500000000000000000000000000000000000000000000000000000000000)
    0x1b17: JUMP v731(0x738)

    Begin block 0x738
    prev=[0x1add], succ=[0x75d]
    =================================
    0x739: v739(0x40) = CONST 
    0x73b: v73b = MLOAD v739(0x40)
    0x73e: v73e(0x20) = CONST 
    0x740: v740 = ADD v73e(0x20), v73b
    0x743: v743(0x20) = SUB v740, v73b
    0x745: MSTORE v73b, v743(0x20)
    0x749: v749(0x3) = MLOAD v1ae1
    0x74b: MSTORE v740, v749(0x3)
    0x74c: v74c(0x20) = CONST 
    0x74e: v74e = ADD v74c(0x20), v740
    0x752: v752(0x3) = MLOAD v1ae1
    0x754: v754(0x20) = CONST 
    0x756: v756 = ADD v754(0x20), v1ae1
    0x75b: v75b(0x0) = CONST 

    Begin block 0x75d
    prev=[0x738, 0x766], succ=[0x778, 0x766]
    =================================
    0x75d_0x0: v75d_0 = PHI v75b(0x0), v771
    0x760: v760 = LT v75d_0, v752(0x3)
    0x761: v761 = ISZERO v760
    0x762: v762(0x778) = CONST 
    0x765: JUMPI v762(0x778), v761

    Begin block 0x778
    prev=[0x75d], succ=[0x7a5, 0x78c]
    =================================
    0x781: v781 = ADD v752(0x3), v74e
    0x783: v783(0x1f) = CONST 
    0x785: v785(0x3) = AND v783(0x1f), v752(0x3)
    0x787: v787 = ISZERO v785(0x3)
    0x788: v788(0x7a5) = CONST 
    0x78b: JUMPI v788(0x7a5), v787

    Begin block 0x7a5
    prev=[0x778, 0x78c], succ=[]
    =================================
    0x7a5_0x1: v7a5_1 = PHI v781, v7a2
    0x7ab: v7ab(0x40) = CONST 
    0x7ad: v7ad = MLOAD v7ab(0x40)
    0x7b0: v7b0 = SUB v7a5_1, v7ad
    0x7b2: RETURN v7ad, v7b0

    Begin block 0x78c
    prev=[0x778], succ=[0x7a5]
    =================================
    0x78e: v78e = SUB v781, v785(0x3)
    0x790: v790 = MLOAD v78e
    0x791: v791(0x1) = CONST 
    0x794: v794(0x20) = CONST 
    0x796: v796(0x1d) = SUB v794(0x20), v785(0x3)
    0x797: v797(0x100) = CONST 
    0x79a: v79a(0x10000000000000000000000000000000000000000000000000000000000) = EXP v797(0x100), v796(0x1d)
    0x79b: v79b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v79a(0x10000000000000000000000000000000000000000000000000000000000), v791(0x1)
    0x79c: v79c = NOT v79b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x79d: v79d = AND v79c, v790
    0x79f: MSTORE v78e, v79d
    0x7a0: v7a0(0x20) = CONST 
    0x7a2: v7a2 = ADD v7a0(0x20), v78e

    Begin block 0x766
    prev=[0x75d], succ=[0x75d]
    =================================
    0x766_0x0: v766_0 = PHI v75b(0x0), v771
    0x768: v768 = ADD v756, v766_0
    0x769: v769 = MLOAD v768
    0x76c: v76c = ADD v74e, v766_0
    0x76d: MSTORE v76c, v769
    0x76e: v76e(0x20) = CONST 
    0x771: v771 = ADD v766_0, v76e(0x20)
    0x774: v774(0x75d) = CONST 
    0x777: JUMP v774(0x75d)

}

function setSetupComplete()() public {
    Begin block 0x7b3
    prev=[], succ=[0x7ba, 0x7be]
    =================================
    0x7b4: v7b4 = CALLVALUE 
    0x7b5: v7b5 = ISZERO v7b4
    0x7b6: v7b6(0x7be) = CONST 
    0x7b9: JUMPI v7b6(0x7be), v7b5

    Begin block 0x7ba
    prev=[0x7b3], succ=[]
    =================================
    0x7ba: v7ba(0x0) = CONST 
    0x7bd: REVERT v7ba(0x0), v7ba(0x0)

    Begin block 0x7be
    prev=[0x7b3], succ=[0x1b18]
    =================================
    0x7bf: v7bf(0x7c6) = CONST 
    0x7c2: v7c2(0x1b18) = CONST 
    0x7c5: JUMP v7c2(0x1b18)

    Begin block 0x1b18
    prev=[0x7be], succ=[0x1b6f, 0x1b73]
    =================================
    0x1b19: v1b19(0x0) = CONST 
    0x1b1d: v1b1d = SLOAD v1b19(0x0)
    0x1b1f: v1b1f(0x100) = CONST 
    0x1b22: v1b22(0x1) = EXP v1b1f(0x100), v1b19(0x0)
    0x1b24: v1b24 = DIV v1b1d, v1b22(0x1)
    0x1b25: v1b25(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b3a: v1b3a = AND v1b25(0xffffffffffffffffffffffffffffffffffffffff), v1b24
    0x1b3b: v1b3b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b50: v1b50 = AND v1b3b(0xffffffffffffffffffffffffffffffffffffffff), v1b3a
    0x1b51: v1b51 = CALLER 
    0x1b52: v1b52(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b67: v1b67 = AND v1b52(0xffffffffffffffffffffffffffffffffffffffff), v1b51
    0x1b68: v1b68 = EQ v1b67, v1b50
    0x1b69: v1b69 = ISZERO v1b68
    0x1b6a: v1b6a = ISZERO v1b69
    0x1b6b: v1b6b(0x1b73) = CONST 
    0x1b6e: JUMPI v1b6b(0x1b73), v1b6a

    Begin block 0x1b6f
    prev=[0x1b18], succ=[]
    =================================
    0x1b6f: v1b6f(0x0) = CONST 
    0x1b72: REVERT v1b6f(0x0), v1b6f(0x0)

    Begin block 0x1b73
    prev=[0x1b18], succ=[0x7c6]
    =================================
    0x1b74: v1b74(0x1) = CONST 
    0x1b76: v1b76(0x12) = CONST 
    0x1b78: v1b78(0x1) = CONST 
    0x1b7a: v1b7a(0x100) = CONST 
    0x1b7d: v1b7d(0x100) = EXP v1b7a(0x100), v1b78(0x1)
    0x1b7f: v1b7f = SLOAD v1b76(0x12)
    0x1b81: v1b81(0xff) = CONST 
    0x1b83: v1b83(0xff00) = MUL v1b81(0xff), v1b7d(0x100)
    0x1b84: v1b84(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v1b83(0xff00)
    0x1b85: v1b85 = AND v1b84(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v1b7f
    0x1b88: v1b88(0x0) = ISZERO v1b74(0x1)
    0x1b89: v1b89(0x1) = ISZERO v1b88(0x0)
    0x1b8a: v1b8a(0x100) = MUL v1b89(0x1), v1b7d(0x100)
    0x1b8b: v1b8b = OR v1b8a(0x100), v1b85
    0x1b8d: SSTORE v1b76(0x12), v1b8b
    0x1b8f: JUMP v7bf(0x7c6)

    Begin block 0x7c6
    prev=[0x1b73], succ=[]
    =================================
    0x7c7: STOP 

}

function setupComplete()() public {
    Begin block 0x7c8
    prev=[], succ=[0x7cf, 0x7d3]
    =================================
    0x7c9: v7c9 = CALLVALUE 
    0x7ca: v7ca = ISZERO v7c9
    0x7cb: v7cb(0x7d3) = CONST 
    0x7ce: JUMPI v7cb(0x7d3), v7ca

    Begin block 0x7cf
    prev=[0x7c8], succ=[]
    =================================
    0x7cf: v7cf(0x0) = CONST 
    0x7d2: REVERT v7cf(0x0), v7cf(0x0)

    Begin block 0x7d3
    prev=[0x7c8], succ=[0x1b90]
    =================================
    0x7d4: v7d4(0x7db) = CONST 
    0x7d7: v7d7(0x1b90) = CONST 
    0x7da: JUMP v7d7(0x1b90)

    Begin block 0x1b90
    prev=[0x7d3], succ=[0x7db]
    =================================
    0x1b91: v1b91(0x12) = CONST 
    0x1b93: v1b93(0x1) = CONST 
    0x1b96: v1b96 = SLOAD v1b91(0x12)
    0x1b98: v1b98(0x100) = CONST 
    0x1b9b: v1b9b(0x100) = EXP v1b98(0x100), v1b93(0x1)
    0x1b9d: v1b9d = DIV v1b96, v1b9b(0x100)
    0x1b9e: v1b9e(0xff) = CONST 
    0x1ba0: v1ba0 = AND v1b9e(0xff), v1b9d
    0x1ba2: JUMP v7d4(0x7db)

    Begin block 0x7db
    prev=[0x1b90], succ=[]
    =================================
    0x7dc: v7dc(0x40) = CONST 
    0x7de: v7de = MLOAD v7dc(0x40)
    0x7e1: v7e1 = ISZERO v1ba0
    0x7e2: v7e2 = ISZERO v7e1
    0x7e3: v7e3 = ISZERO v7e2
    0x7e4: v7e4 = ISZERO v7e3
    0x7e6: MSTORE v7de, v7e4
    0x7e7: v7e7(0x20) = CONST 
    0x7e9: v7e9 = ADD v7e7(0x20), v7de
    0x7ed: v7ed(0x40) = CONST 
    0x7ef: v7ef = MLOAD v7ed(0x40)
    0x7f2: v7f2(0x20) = SUB v7e9, v7ef
    0x7f4: RETURN v7ef, v7f2(0x20)

}

function tokenURI(uint256)() public {
    Begin block 0x7f5
    prev=[], succ=[0x7fc, 0x800]
    =================================
    0x7f6: v7f6 = CALLVALUE 
    0x7f7: v7f7 = ISZERO v7f6
    0x7f8: v7f8(0x800) = CONST 
    0x7fb: JUMPI v7f8(0x800), v7f7

    Begin block 0x7fc
    prev=[0x7f5], succ=[]
    =================================
    0x7fc: v7fc(0x0) = CONST 
    0x7ff: REVERT v7fc(0x0), v7fc(0x0)

    Begin block 0x800
    prev=[0x7f5], succ=[0x1ba3]
    =================================
    0x801: v801(0x816) = CONST 
    0x804: v804(0x4) = CONST 
    0x808: v808 = CALLDATALOAD v804(0x4)
    0x80a: v80a(0x20) = CONST 
    0x80c: v80c(0x24) = ADD v80a(0x20), v804(0x4)
    0x812: v812(0x1ba3) = CONST 
    0x815: JUMP v812(0x1ba3)

    Begin block 0x1ba3
    prev=[0x800], succ=[0x29faB0x1ba3]
    =================================
    0x1ba4: v1ba4(0x1bab) = CONST 
    0x1ba7: v1ba7(0x29fa) = CONST 
    0x1baa: JUMP v1ba7(0x29fa)

    Begin block 0x29faB0x1ba3
    prev=[0x1ba3], succ=[0x1bab]
    =================================
    0x29fbS0x1ba3: v29fbV1ba3(0x20) = CONST 
    0x29fdS0x1ba3: v29fdV1ba3(0x40) = CONST 
    0x29ffS0x1ba3: v29ffV1ba3 = MLOAD v29fdV1ba3(0x40)
    0x2a02S0x1ba3: v2a02V1ba3 = ADD v29ffV1ba3, v29fbV1ba3(0x20)
    0x2a03S0x1ba3: v2a03V1ba3(0x40) = CONST 
    0x2a05S0x1ba3: MSTORE v2a03V1ba3(0x40), v2a02V1ba3
    0x2a07S0x1ba3: v2a07V1ba3(0x0) = CONST 
    0x2a0aS0x1ba3: MSTORE v29ffV1ba3, v2a07V1ba3(0x0)
    0x2a0dS0x1ba3: JUMP v1ba4(0x1bab)

    Begin block 0x1bab
    prev=[0x29faB0x1ba3], succ=[0x29e6B0x1bab]
    =================================
    0x1bac: v1bac(0x1bb3) = CONST 
    0x1baf: v1baf(0x29e6) = CONST 
    0x1bb2: JUMP v1baf(0x29e6)

    Begin block 0x29e6B0x1bab
    prev=[0x1bab], succ=[0x1bb3]
    =================================
    0x29e7S0x1bab: v29e7V1bab(0x20) = CONST 
    0x29e9S0x1bab: v29e9V1bab(0x40) = CONST 
    0x29ebS0x1bab: v29ebV1bab = MLOAD v29e9V1bab(0x40)
    0x29eeS0x1bab: v29eeV1bab = ADD v29ebV1bab, v29e7V1bab(0x20)
    0x29efS0x1bab: v29efV1bab(0x40) = CONST 
    0x29f1S0x1bab: MSTORE v29efV1bab(0x40), v29eeV1bab
    0x29f3S0x1bab: v29f3V1bab(0x0) = CONST 
    0x29f6S0x1bab: MSTORE v29ebV1bab, v29f3V1bab(0x0)
    0x29f9S0x1bab: JUMP v1bac(0x1bb3)

    Begin block 0x1bb3
    prev=[0x29e6B0x1bab], succ=[0x1c24, 0x1c25]
    =================================
    0x1bb4: v1bb4(0x60) = CONST 
    0x1bb6: v1bb6(0x40) = CONST 
    0x1bb8: v1bb8 = MLOAD v1bb6(0x40)
    0x1bbb: v1bbb = ADD v1bb8, v1bb4(0x60)
    0x1bbc: v1bbc(0x40) = CONST 
    0x1bbe: MSTORE v1bbc(0x40), v1bbb
    0x1bc0: v1bc0(0x2d) = CONST 
    0x1bc3: MSTORE v1bb8, v1bc0(0x2d)
    0x1bc4: v1bc4(0x20) = CONST 
    0x1bc6: v1bc6 = ADD v1bc4(0x20), v1bb8
    0x1bc7: v1bc7(0x68747470733a2f2f7777772e62696c6c696f6e646f6c6c617270696374757265) = CONST 
    0x1be9: MSTORE v1bc6, v1bc7(0x68747470733a2f2f7777772e62696c6c696f6e646f6c6c617270696374757265)
    0x1bea: v1bea(0x20) = CONST 
    0x1bec: v1bec = ADD v1bea(0x20), v1bc6
    0x1bed: v1bed(0x2e636f6d2f233030303030303000000000000000000000000000000000000000) = CONST 
    0x1c0f: MSTORE v1bec, v1bed(0x2e636f6d2f233030303030303000000000000000000000000000000000000000)
    0x1c16: v1c16(0xa) = CONST 
    0x1c18: v1c18(0xf4240) = CONST 
    0x1c1e: v1c1e(0x0) = ISZERO v1c18(0xf4240)
    0x1c1f: v1c1f(0x1) = ISZERO v1c1e(0x0)
    0x1c20: v1c20(0x1c25) = CONST 
    0x1c23: JUMPI v1c20(0x1c25), v1c1f(0x1)

    Begin block 0x1c24
    prev=[0x1bb3], succ=[]
    =================================
    0x1c24: THROW 

    Begin block 0x1c25
    prev=[0x1bb3], succ=[0x1c2e, 0x1c2f]
    =================================
    0x1c26: v1c26 = DIV v808, v1c18(0xf4240)
    0x1c28: v1c28 = ISZERO v1c16(0xa)
    0x1c29: v1c29 = ISZERO v1c28
    0x1c2a: v1c2a(0x1c2f) = CONST 
    0x1c2d: JUMPI v1c2a(0x1c2f), v1c29

    Begin block 0x1c2e
    prev=[0x1c25], succ=[]
    =================================
    0x1c2e: THROW 

    Begin block 0x1c2f
    prev=[0x1c25], succ=[0x1c63, 0x1c64]
    =================================
    0x1c30: v1c30 = MOD v1c26, v1c16(0xa)
    0x1c31: v1c31(0x30) = CONST 
    0x1c33: v1c33 = ADD v1c31(0x30), v1c30
    0x1c34: v1c34(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c55: v1c55 = MUL v1c34(0x100000000000000000000000000000000000000000000000000000000000000), v1c33
    0x1c57: v1c57(0x22) = CONST 
    0x1c5a: v1c5a(0x2d) = MLOAD v1bb8
    0x1c5c: v1c5c(0x1) = LT v1c57(0x22), v1c5a(0x2d)
    0x1c5d: v1c5d = ISZERO v1c5c(0x1)
    0x1c5e: v1c5e = ISZERO v1c5d
    0x1c5f: v1c5f(0x1c64) = CONST 
    0x1c62: JUMPI v1c5f(0x1c64), v1c5e

    Begin block 0x1c63
    prev=[0x1c2f], succ=[]
    =================================
    0x1c63: THROW 

    Begin block 0x1c64
    prev=[0x1c2f], succ=[0x1ca3, 0x1ca4]
    =================================
    0x1c66: v1c66(0x20) = CONST 
    0x1c68: v1c68 = ADD v1c66(0x20), v1bb8
    0x1c69: v1c69 = ADD v1c68, v1c57(0x22)
    0x1c6b: v1c6b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c8b: v1c8b(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1c6b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1c8c: v1c8c = AND v1c8b(0xff00000000000000000000000000000000000000000000000000000000000000), v1c55
    0x1c8f: v1c8f(0x0) = CONST 
    0x1c91: v1c91 = BYTE v1c8f(0x0), v1c8c
    0x1c93: MSTORE8 v1c69, v1c91
    0x1c95: v1c95(0xa) = CONST 
    0x1c97: v1c97(0x186a0) = CONST 
    0x1c9d: v1c9d(0x0) = ISZERO v1c97(0x186a0)
    0x1c9e: v1c9e(0x1) = ISZERO v1c9d(0x0)
    0x1c9f: v1c9f(0x1ca4) = CONST 
    0x1ca2: JUMPI v1c9f(0x1ca4), v1c9e(0x1)

    Begin block 0x1ca3
    prev=[0x1c64], succ=[]
    =================================
    0x1ca3: THROW 

    Begin block 0x1ca4
    prev=[0x1c64], succ=[0x1cad, 0x1cae]
    =================================
    0x1ca5: v1ca5 = DIV v808, v1c97(0x186a0)
    0x1ca7: v1ca7 = ISZERO v1c95(0xa)
    0x1ca8: v1ca8 = ISZERO v1ca7
    0x1ca9: v1ca9(0x1cae) = CONST 
    0x1cac: JUMPI v1ca9(0x1cae), v1ca8

    Begin block 0x1cad
    prev=[0x1ca4], succ=[]
    =================================
    0x1cad: THROW 

    Begin block 0x1cae
    prev=[0x1ca4], succ=[0x1ce2, 0x1ce3]
    =================================
    0x1caf: v1caf = MOD v1ca5, v1c95(0xa)
    0x1cb0: v1cb0(0x30) = CONST 
    0x1cb2: v1cb2 = ADD v1cb0(0x30), v1caf
    0x1cb3: v1cb3(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1cd4: v1cd4 = MUL v1cb3(0x100000000000000000000000000000000000000000000000000000000000000), v1cb2
    0x1cd6: v1cd6(0x23) = CONST 
    0x1cd9: v1cd9(0x2d) = MLOAD v1bb8
    0x1cdb: v1cdb(0x1) = LT v1cd6(0x23), v1cd9(0x2d)
    0x1cdc: v1cdc = ISZERO v1cdb(0x1)
    0x1cdd: v1cdd = ISZERO v1cdc
    0x1cde: v1cde(0x1ce3) = CONST 
    0x1ce1: JUMPI v1cde(0x1ce3), v1cdd

    Begin block 0x1ce2
    prev=[0x1cae], succ=[]
    =================================
    0x1ce2: THROW 

    Begin block 0x1ce3
    prev=[0x1cae], succ=[0x1d21, 0x1d22]
    =================================
    0x1ce5: v1ce5(0x20) = CONST 
    0x1ce7: v1ce7 = ADD v1ce5(0x20), v1bb8
    0x1ce8: v1ce8 = ADD v1ce7, v1cd6(0x23)
    0x1cea: v1cea(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d0a: v1d0a(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1cea(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1d0b: v1d0b = AND v1d0a(0xff00000000000000000000000000000000000000000000000000000000000000), v1cd4
    0x1d0e: v1d0e(0x0) = CONST 
    0x1d10: v1d10 = BYTE v1d0e(0x0), v1d0b
    0x1d12: MSTORE8 v1ce8, v1d10
    0x1d14: v1d14(0xa) = CONST 
    0x1d16: v1d16(0x2710) = CONST 
    0x1d1b: v1d1b(0x0) = ISZERO v1d16(0x2710)
    0x1d1c: v1d1c(0x1) = ISZERO v1d1b(0x0)
    0x1d1d: v1d1d(0x1d22) = CONST 
    0x1d20: JUMPI v1d1d(0x1d22), v1d1c(0x1)

    Begin block 0x1d21
    prev=[0x1ce3], succ=[]
    =================================
    0x1d21: THROW 

    Begin block 0x1d22
    prev=[0x1ce3], succ=[0x1d2b, 0x1d2c]
    =================================
    0x1d23: v1d23 = DIV v808, v1d16(0x2710)
    0x1d25: v1d25 = ISZERO v1d14(0xa)
    0x1d26: v1d26 = ISZERO v1d25
    0x1d27: v1d27(0x1d2c) = CONST 
    0x1d2a: JUMPI v1d27(0x1d2c), v1d26

    Begin block 0x1d2b
    prev=[0x1d22], succ=[]
    =================================
    0x1d2b: THROW 

    Begin block 0x1d2c
    prev=[0x1d22], succ=[0x1d60, 0x1d61]
    =================================
    0x1d2d: v1d2d = MOD v1d23, v1d14(0xa)
    0x1d2e: v1d2e(0x30) = CONST 
    0x1d30: v1d30 = ADD v1d2e(0x30), v1d2d
    0x1d31: v1d31(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d52: v1d52 = MUL v1d31(0x100000000000000000000000000000000000000000000000000000000000000), v1d30
    0x1d54: v1d54(0x24) = CONST 
    0x1d57: v1d57(0x2d) = MLOAD v1bb8
    0x1d59: v1d59(0x1) = LT v1d54(0x24), v1d57(0x2d)
    0x1d5a: v1d5a = ISZERO v1d59(0x1)
    0x1d5b: v1d5b = ISZERO v1d5a
    0x1d5c: v1d5c(0x1d61) = CONST 
    0x1d5f: JUMPI v1d5c(0x1d61), v1d5b

    Begin block 0x1d60
    prev=[0x1d2c], succ=[]
    =================================
    0x1d60: THROW 

    Begin block 0x1d61
    prev=[0x1d2c], succ=[0x1d9f, 0x1da0]
    =================================
    0x1d63: v1d63(0x20) = CONST 
    0x1d65: v1d65 = ADD v1d63(0x20), v1bb8
    0x1d66: v1d66 = ADD v1d65, v1d54(0x24)
    0x1d68: v1d68(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d88: v1d88(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1d68(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1d89: v1d89 = AND v1d88(0xff00000000000000000000000000000000000000000000000000000000000000), v1d52
    0x1d8c: v1d8c(0x0) = CONST 
    0x1d8e: v1d8e = BYTE v1d8c(0x0), v1d89
    0x1d90: MSTORE8 v1d66, v1d8e
    0x1d92: v1d92(0xa) = CONST 
    0x1d94: v1d94(0x3e8) = CONST 
    0x1d99: v1d99(0x0) = ISZERO v1d94(0x3e8)
    0x1d9a: v1d9a(0x1) = ISZERO v1d99(0x0)
    0x1d9b: v1d9b(0x1da0) = CONST 
    0x1d9e: JUMPI v1d9b(0x1da0), v1d9a(0x1)

    Begin block 0x1d9f
    prev=[0x1d61], succ=[]
    =================================
    0x1d9f: THROW 

    Begin block 0x1da0
    prev=[0x1d61], succ=[0x1da9, 0x1daa]
    =================================
    0x1da1: v1da1 = DIV v808, v1d94(0x3e8)
    0x1da3: v1da3 = ISZERO v1d92(0xa)
    0x1da4: v1da4 = ISZERO v1da3
    0x1da5: v1da5(0x1daa) = CONST 
    0x1da8: JUMPI v1da5(0x1daa), v1da4

    Begin block 0x1da9
    prev=[0x1da0], succ=[]
    =================================
    0x1da9: THROW 

    Begin block 0x1daa
    prev=[0x1da0], succ=[0x1dde, 0x1ddf]
    =================================
    0x1dab: v1dab = MOD v1da1, v1d92(0xa)
    0x1dac: v1dac(0x30) = CONST 
    0x1dae: v1dae = ADD v1dac(0x30), v1dab
    0x1daf: v1daf(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1dd0: v1dd0 = MUL v1daf(0x100000000000000000000000000000000000000000000000000000000000000), v1dae
    0x1dd2: v1dd2(0x25) = CONST 
    0x1dd5: v1dd5(0x2d) = MLOAD v1bb8
    0x1dd7: v1dd7(0x1) = LT v1dd2(0x25), v1dd5(0x2d)
    0x1dd8: v1dd8 = ISZERO v1dd7(0x1)
    0x1dd9: v1dd9 = ISZERO v1dd8
    0x1dda: v1dda(0x1ddf) = CONST 
    0x1ddd: JUMPI v1dda(0x1ddf), v1dd9

    Begin block 0x1dde
    prev=[0x1daa], succ=[]
    =================================
    0x1dde: THROW 

    Begin block 0x1ddf
    prev=[0x1daa], succ=[0x1e1c, 0x1e1d]
    =================================
    0x1de1: v1de1(0x20) = CONST 
    0x1de3: v1de3 = ADD v1de1(0x20), v1bb8
    0x1de4: v1de4 = ADD v1de3, v1dd2(0x25)
    0x1de6: v1de6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e06: v1e06(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1de6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1e07: v1e07 = AND v1e06(0xff00000000000000000000000000000000000000000000000000000000000000), v1dd0
    0x1e0a: v1e0a(0x0) = CONST 
    0x1e0c: v1e0c = BYTE v1e0a(0x0), v1e07
    0x1e0e: MSTORE8 v1de4, v1e0c
    0x1e10: v1e10(0xa) = CONST 
    0x1e12: v1e12(0x64) = CONST 
    0x1e16: v1e16(0x0) = ISZERO v1e12(0x64)
    0x1e17: v1e17(0x1) = ISZERO v1e16(0x0)
    0x1e18: v1e18(0x1e1d) = CONST 
    0x1e1b: JUMPI v1e18(0x1e1d), v1e17(0x1)

    Begin block 0x1e1c
    prev=[0x1ddf], succ=[]
    =================================
    0x1e1c: THROW 

    Begin block 0x1e1d
    prev=[0x1ddf], succ=[0x1e26, 0x1e27]
    =================================
    0x1e1e: v1e1e = DIV v808, v1e12(0x64)
    0x1e20: v1e20 = ISZERO v1e10(0xa)
    0x1e21: v1e21 = ISZERO v1e20
    0x1e22: v1e22(0x1e27) = CONST 
    0x1e25: JUMPI v1e22(0x1e27), v1e21

    Begin block 0x1e26
    prev=[0x1e1d], succ=[]
    =================================
    0x1e26: THROW 

    Begin block 0x1e27
    prev=[0x1e1d], succ=[0x1e5b, 0x1e5c]
    =================================
    0x1e28: v1e28 = MOD v1e1e, v1e10(0xa)
    0x1e29: v1e29(0x30) = CONST 
    0x1e2b: v1e2b = ADD v1e29(0x30), v1e28
    0x1e2c: v1e2c(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e4d: v1e4d = MUL v1e2c(0x100000000000000000000000000000000000000000000000000000000000000), v1e2b
    0x1e4f: v1e4f(0x26) = CONST 
    0x1e52: v1e52(0x2d) = MLOAD v1bb8
    0x1e54: v1e54(0x1) = LT v1e4f(0x26), v1e52(0x2d)
    0x1e55: v1e55 = ISZERO v1e54(0x1)
    0x1e56: v1e56 = ISZERO v1e55
    0x1e57: v1e57(0x1e5c) = CONST 
    0x1e5a: JUMPI v1e57(0x1e5c), v1e56

    Begin block 0x1e5b
    prev=[0x1e27], succ=[]
    =================================
    0x1e5b: THROW 

    Begin block 0x1e5c
    prev=[0x1e27], succ=[0x1e98, 0x1e99]
    =================================
    0x1e5e: v1e5e(0x20) = CONST 
    0x1e60: v1e60 = ADD v1e5e(0x20), v1bb8
    0x1e61: v1e61 = ADD v1e60, v1e4f(0x26)
    0x1e63: v1e63(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e83: v1e83(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1e63(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1e84: v1e84 = AND v1e83(0xff00000000000000000000000000000000000000000000000000000000000000), v1e4d
    0x1e87: v1e87(0x0) = CONST 
    0x1e89: v1e89 = BYTE v1e87(0x0), v1e84
    0x1e8b: MSTORE8 v1e61, v1e89
    0x1e8d: v1e8d(0xa) = CONST 
    0x1e92: v1e92(0x0) = ISZERO v1e8d(0xa)
    0x1e93: v1e93(0x1) = ISZERO v1e92(0x0)
    0x1e94: v1e94(0x1e99) = CONST 
    0x1e97: JUMPI v1e94(0x1e99), v1e93(0x1)

    Begin block 0x1e98
    prev=[0x1e5c], succ=[]
    =================================
    0x1e98: THROW 

    Begin block 0x1e99
    prev=[0x1e5c], succ=[0x1ea2, 0x1ea3]
    =================================
    0x1e9a: v1e9a = DIV v808, v1e8d(0xa)
    0x1e9c: v1e9c = ISZERO v1e8d(0xa)
    0x1e9d: v1e9d = ISZERO v1e9c
    0x1e9e: v1e9e(0x1ea3) = CONST 
    0x1ea1: JUMPI v1e9e(0x1ea3), v1e9d

    Begin block 0x1ea2
    prev=[0x1e99], succ=[]
    =================================
    0x1ea2: THROW 

    Begin block 0x1ea3
    prev=[0x1e99], succ=[0x1ed7, 0x1ed8]
    =================================
    0x1ea4: v1ea4 = MOD v1e9a, v1e8d(0xa)
    0x1ea5: v1ea5(0x30) = CONST 
    0x1ea7: v1ea7 = ADD v1ea5(0x30), v1ea4
    0x1ea8: v1ea8(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1ec9: v1ec9 = MUL v1ea8(0x100000000000000000000000000000000000000000000000000000000000000), v1ea7
    0x1ecb: v1ecb(0x27) = CONST 
    0x1ece: v1ece(0x2d) = MLOAD v1bb8
    0x1ed0: v1ed0(0x1) = LT v1ecb(0x27), v1ece(0x2d)
    0x1ed1: v1ed1 = ISZERO v1ed0(0x1)
    0x1ed2: v1ed2 = ISZERO v1ed1
    0x1ed3: v1ed3(0x1ed8) = CONST 
    0x1ed6: JUMPI v1ed3(0x1ed8), v1ed2

    Begin block 0x1ed7
    prev=[0x1ea3], succ=[]
    =================================
    0x1ed7: THROW 

    Begin block 0x1ed8
    prev=[0x1ea3], succ=[0x1f15, 0x1f16]
    =================================
    0x1eda: v1eda(0x20) = CONST 
    0x1edc: v1edc = ADD v1eda(0x20), v1bb8
    0x1edd: v1edd = ADD v1edc, v1ecb(0x27)
    0x1edf: v1edf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1eff: v1eff(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1edf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1f00: v1f00 = AND v1eff(0xff00000000000000000000000000000000000000000000000000000000000000), v1ec9
    0x1f03: v1f03(0x0) = CONST 
    0x1f05: v1f05 = BYTE v1f03(0x0), v1f00
    0x1f07: MSTORE8 v1edd, v1f05
    0x1f09: v1f09(0xa) = CONST 
    0x1f0b: v1f0b(0x1) = CONST 
    0x1f0f: v1f0f(0x0) = ISZERO v1f0b(0x1)
    0x1f10: v1f10(0x1) = ISZERO v1f0f(0x0)
    0x1f11: v1f11(0x1f16) = CONST 
    0x1f14: JUMPI v1f11(0x1f16), v1f10(0x1)

    Begin block 0x1f15
    prev=[0x1ed8], succ=[]
    =================================
    0x1f15: THROW 

    Begin block 0x1f16
    prev=[0x1ed8], succ=[0x1f1f, 0x1f20]
    =================================
    0x1f17: v1f17 = DIV v808, v1f0b(0x1)
    0x1f19: v1f19 = ISZERO v1f09(0xa)
    0x1f1a: v1f1a = ISZERO v1f19
    0x1f1b: v1f1b(0x1f20) = CONST 
    0x1f1e: JUMPI v1f1b(0x1f20), v1f1a

    Begin block 0x1f1f
    prev=[0x1f16], succ=[]
    =================================
    0x1f1f: THROW 

    Begin block 0x1f20
    prev=[0x1f16], succ=[0x1f54, 0x1f55]
    =================================
    0x1f21: v1f21 = MOD v1f17, v1f09(0xa)
    0x1f22: v1f22(0x30) = CONST 
    0x1f24: v1f24 = ADD v1f22(0x30), v1f21
    0x1f25: v1f25(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f46: v1f46 = MUL v1f25(0x100000000000000000000000000000000000000000000000000000000000000), v1f24
    0x1f48: v1f48(0x28) = CONST 
    0x1f4b: v1f4b(0x2d) = MLOAD v1bb8
    0x1f4d: v1f4d(0x1) = LT v1f48(0x28), v1f4b(0x2d)
    0x1f4e: v1f4e = ISZERO v1f4d(0x1)
    0x1f4f: v1f4f = ISZERO v1f4e
    0x1f50: v1f50(0x1f55) = CONST 
    0x1f53: JUMPI v1f50(0x1f55), v1f4f

    Begin block 0x1f54
    prev=[0x1f20], succ=[]
    =================================
    0x1f54: THROW 

    Begin block 0x1f55
    prev=[0x1f20], succ=[0x816]
    =================================
    0x1f57: v1f57(0x20) = CONST 
    0x1f59: v1f59 = ADD v1f57(0x20), v1bb8
    0x1f5a: v1f5a = ADD v1f59, v1f48(0x28)
    0x1f5c: v1f5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f7c: v1f7c(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1f5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1f7d: v1f7d = AND v1f7c(0xff00000000000000000000000000000000000000000000000000000000000000), v1f46
    0x1f80: v1f80(0x0) = CONST 
    0x1f82: v1f82 = BYTE v1f80(0x0), v1f7d
    0x1f84: MSTORE8 v1f5a, v1f82
    0x1f8a: JUMP v801(0x816)

    Begin block 0x816
    prev=[0x1f55], succ=[0x83b]
    =================================
    0x817: v817(0x40) = CONST 
    0x819: v819 = MLOAD v817(0x40)
    0x81c: v81c(0x20) = CONST 
    0x81e: v81e = ADD v81c(0x20), v819
    0x821: v821(0x20) = SUB v81e, v819
    0x823: MSTORE v819, v821(0x20)
    0x827: v827(0x2d) = MLOAD v1bb8
    0x829: MSTORE v81e, v827(0x2d)
    0x82a: v82a(0x20) = CONST 
    0x82c: v82c = ADD v82a(0x20), v81e
    0x830: v830(0x2d) = MLOAD v1bb8
    0x832: v832(0x20) = CONST 
    0x834: v834 = ADD v832(0x20), v1bb8
    0x839: v839(0x0) = CONST 

    Begin block 0x83b
    prev=[0x816, 0x844], succ=[0x856, 0x844]
    =================================
    0x83b_0x0: v83b_0 = PHI v839(0x0), v84f
    0x83e: v83e = LT v83b_0, v830(0x2d)
    0x83f: v83f = ISZERO v83e
    0x840: v840(0x856) = CONST 
    0x843: JUMPI v840(0x856), v83f

    Begin block 0x856
    prev=[0x83b], succ=[0x883, 0x86a]
    =================================
    0x85f: v85f = ADD v830(0x2d), v82c
    0x861: v861(0x1f) = CONST 
    0x863: v863(0xd) = AND v861(0x1f), v830(0x2d)
    0x865: v865 = ISZERO v863(0xd)
    0x866: v866(0x883) = CONST 
    0x869: JUMPI v866(0x883), v865

    Begin block 0x883
    prev=[0x856, 0x86a], succ=[]
    =================================
    0x883_0x1: v883_1 = PHI v85f, v880
    0x889: v889(0x40) = CONST 
    0x88b: v88b = MLOAD v889(0x40)
    0x88e: v88e = SUB v883_1, v88b
    0x890: RETURN v88b, v88e

    Begin block 0x86a
    prev=[0x856], succ=[0x883]
    =================================
    0x86c: v86c = SUB v85f, v863(0xd)
    0x86e: v86e = MLOAD v86c
    0x86f: v86f(0x1) = CONST 
    0x872: v872(0x20) = CONST 
    0x874: v874(0x13) = SUB v872(0x20), v863(0xd)
    0x875: v875(0x100) = CONST 
    0x878: v878(0x100000000000000000000000000000000000000) = EXP v875(0x100), v874(0x13)
    0x879: v879(0xffffffffffffffffffffffffffffffffffffff) = SUB v878(0x100000000000000000000000000000000000000), v86f(0x1)
    0x87a: v87a = NOT v879(0xffffffffffffffffffffffffffffffffffffff)
    0x87b: v87b = AND v87a, v86e
    0x87d: MSTORE v86c, v87b
    0x87e: v87e(0x20) = CONST 
    0x880: v880 = ADD v87e(0x20), v86c

    Begin block 0x844
    prev=[0x83b], succ=[0x83b]
    =================================
    0x844_0x0: v844_0 = PHI v839(0x0), v84f
    0x846: v846 = ADD v834, v844_0
    0x847: v847 = MLOAD v846
    0x84a: v84a = ADD v82c, v844_0
    0x84b: MSTORE v84a, v847
    0x84c: v84c(0x20) = CONST 
    0x84f: v84f = ADD v844_0, v84c(0x20)
    0x852: v852(0x83b) = CONST 
    0x855: JUMP v852(0x83b)

}

function updateRegion(uint256,uint256,uint256[],bool,bool,uint8[128],bool,address)() public {
    Begin block 0x891
    prev=[], succ=[0x1f8bB0x891]
    =================================
    0x892: v892(0x95d) = CONST 
    0x895: v895(0x4) = CONST 
    0x899: v899 = CALLDATALOAD v895(0x4)
    0x89b: v89b(0x20) = CONST 
    0x89d: v89d(0x24) = ADD v89b(0x20), v895(0x4)
    0x8a2: v8a2 = CALLDATALOAD v89d(0x24)
    0x8a4: v8a4(0x20) = CONST 
    0x8a6: v8a6(0x44) = ADD v8a4(0x20), v89d(0x24)
    0x8ab: v8ab = CALLDATALOAD v8a6(0x44)
    0x8ad: v8ad(0x20) = CONST 
    0x8af: v8af(0x64) = ADD v8ad(0x20), v8a6(0x44)
    0x8b2: v8b2 = ADD v895(0x4), v8ab
    0x8b4: v8b4 = CALLDATALOAD v8b2
    0x8b6: v8b6(0x20) = CONST 
    0x8b8: v8b8 = ADD v8b6(0x20), v8b2
    0x8bc: v8bc(0x20) = CONST 
    0x8be: v8be = MUL v8bc(0x20), v8b4
    0x8bf: v8bf(0x20) = CONST 
    0x8c1: v8c1 = ADD v8bf(0x20), v8be
    0x8c2: v8c2(0x40) = CONST 
    0x8c4: v8c4 = MLOAD v8c2(0x40)
    0x8c7: v8c7 = ADD v8c4, v8c1
    0x8c8: v8c8(0x40) = CONST 
    0x8ca: MSTORE v8c8(0x40), v8c7
    0x8d2: MSTORE v8c4, v8b4
    0x8d3: v8d3(0x20) = CONST 
    0x8d5: v8d5 = ADD v8d3(0x20), v8c4
    0x8d8: v8d8(0x20) = CONST 
    0x8da: v8da = MUL v8d8(0x20), v8b4
    0x8de: CALLDATACOPY v8d5, v8b8, v8da
    0x8e0: v8e0 = ADD v8d5, v8da
    0x8eb: v8eb = CALLDATALOAD v8af(0x64)
    0x8ec: v8ec = ISZERO v8eb
    0x8ed: v8ed = ISZERO v8ec
    0x8ef: v8ef(0x20) = CONST 
    0x8f1: v8f1(0x84) = ADD v8ef(0x20), v8af(0x64)
    0x8f6: v8f6 = CALLDATALOAD v8f1(0x84)
    0x8f7: v8f7 = ISZERO v8f6
    0x8f8: v8f8 = ISZERO v8f7
    0x8fa: v8fa(0x20) = CONST 
    0x8fc: v8fc(0xa4) = ADD v8fa(0x20), v8f1(0x84)
    0x901: v901(0x1000) = CONST 
    0x904: v904(0x10a4) = ADD v901(0x1000), v8fc(0xa4)
    0x906: v906(0x80) = CONST 
    0x909: v909(0x20) = CONST 
    0x90b: v90b(0x1000) = MUL v909(0x20), v906(0x80)
    0x90c: v90c(0x40) = CONST 
    0x90e: v90e = MLOAD v90c(0x40)
    0x911: v911 = ADD v90e, v90b(0x1000)
    0x912: v912(0x40) = CONST 
    0x914: MSTORE v912(0x40), v911
    0x91a: v91a(0x80) = CONST 
    0x91c: v91c(0x20) = CONST 
    0x91e: v91e(0x1000) = MUL v91c(0x20), v91a(0x80)
    0x922: CALLDATACOPY v90e, v8fc(0xa4), v91e(0x1000)
    0x924: v924 = ADD v90e, v91e(0x1000)
    0x92e: v92e = CALLDATALOAD v904(0x10a4)
    0x92f: v92f = ISZERO v92e
    0x930: v930 = ISZERO v92f
    0x932: v932(0x20) = CONST 
    0x934: v934(0x10c4) = ADD v932(0x20), v904(0x10a4)
    0x939: v939 = CALLDATALOAD v934(0x10c4)
    0x93a: v93a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x94f: v94f = AND v93a(0xffffffffffffffffffffffffffffffffffffffff), v939
    0x951: v951(0x20) = CONST 
    0x953: v953(0x10e4) = ADD v951(0x20), v934(0x10c4)
    0x959: v959(0x1f8b) = CONST 
    0x95c: JUMP v959(0x1f8b), v94f, v930, v90e, v8f8, v8ed, v8c4, v8a2, v899, v892(0x95d)

    Begin block 0x1f8bB0x891
    prev=[0x891], succ=[0x1fb4B0x891, 0x1fa3B0x891]
    =================================
    0x1f8cS0x891: v1f8cV891(0x12) = CONST 
    0x1f8eS0x891: v1f8eV891(0x0) = CONST 
    0x1f91S0x891: v1f91V891 = SLOAD v1f8cV891(0x12)
    0x1f93S0x891: v1f93V891(0x100) = CONST 
    0x1f96S0x891: v1f96V891(0x1) = EXP v1f93V891(0x100), v1f8eV891(0x0)
    0x1f98S0x891: v1f98V891 = DIV v1f91V891, v1f96V891(0x1)
    0x1f99S0x891: v1f99V891(0xff) = CONST 
    0x1f9bS0x891: v1f9bV891 = AND v1f99V891(0xff), v1f98V891
    0x1f9cS0x891: v1f9cV891 = ISZERO v1f9bV891
    0x1f9eS0x891: v1f9eV891 = ISZERO v1f9cV891
    0x1f9fS0x891: v1f9fV891(0x1fb4) = CONST 
    0x1fa2S0x891: JUMPI v1f9fV891(0x1fb4), v1f9eV891

    Begin block 0x1fb4B0x891
    prev=[0x1f8bB0x891, 0x1fa3B0x891], succ=[0x1fbbB0x891, 0x1fbfB0x891]
    =================================
    0x1fb4_0x0S0x891: v1fb4_0V891 = PHI v1f9cV891, v1fb3V891
    0x1fb5S0x891: v1fb5V891 = ISZERO v1fb4_0V891
    0x1fb6S0x891: v1fb6V891 = ISZERO v1fb5V891
    0x1fb7S0x891: v1fb7V891(0x1fbf) = CONST 
    0x1fbaS0x891: JUMPI v1fb7V891(0x1fbf), v1fb6V891

    Begin block 0x1fbbB0x891
    prev=[0x1fb4B0x891], succ=[]
    =================================
    0x1fbbS0x891: v1fbbV891(0x0) = CONST 
    0x1fbeS0x891: REVERT v1fbbV891(0x0), v1fbbV891(0x0)

    Begin block 0x1fbfB0x891
    prev=[0x1fb4B0x891], succ=[0x201cB0x891, 0x206cB0x891]
    =================================
    0x1fc0S0x891: v1fc0V891(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb) = CONST 
    0x1fd5S0x891: v1fd5V891(0x523f110e) = CONST 
    0x1fdaS0x891: v1fdaV891(0x2) = CONST 
    0x1fe4S0x891: v1fe4V891(0x40) = CONST 
    0x1fe6S0x891: v1fe6V891 = MLOAD v1fe4V891(0x40)
    0x1fe8S0x891: v1fe8V891(0xffffffff) = CONST 
    0x1fedS0x891: v1fedV891(0x523f110e) = AND v1fe8V891(0xffffffff), v1fd5V891(0x523f110e)
    0x1feeS0x891: v1feeV891(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x200cS0x891: v200cV891(0x523f110e00000000000000000000000000000000000000000000000000000000) = MUL v1feeV891(0x100000000000000000000000000000000000000000000000000000000), v1fedV891(0x523f110e)
    0x200eS0x891: MSTORE v1fe6V891, v200cV891(0x523f110e00000000000000000000000000000000000000000000000000000000)
    0x200fS0x891: v200fV891(0x4) = CONST 
    0x2011S0x891: v2011V891 = ADD v200fV891(0x4), v1fe6V891
    0x2014S0x891: v2014V891(0x10) = CONST 
    0x2017S0x891: v2017V891(0x0) = ISZERO v2014V891(0x10)
    0x2018S0x891: v2018V891(0x206c) = CONST 
    0x201bS0x891: JUMPI v2018V891(0x206c), v2017V891(0x0)

    Begin block 0x201cB0x891
    prev=[0x1fbfB0x891], succ=[0x2022B0x891]
    =================================
    0x201cS0x891: v201cV891(0x20) = CONST 
    0x201eS0x891: v201eV891(0x200) = MUL v201cV891(0x20), v2014V891(0x10)
    0x2020S0x891: v2020V891 = ADD v2011V891, v201eV891(0x200)

    Begin block 0x2022B0x891
    prev=[0x201cB0x891, 0x2022B0x891], succ=[0x206cB0x891, 0x2022B0x891]
    =================================
    0x2022_0x0S0x891: v2022_0V891 = PHI v2011V891, v205fV891
    0x2022_0x1S0x891: v2022_1V891 = PHI v1fdaV891(0x2), v2063V891
    0x2024S0x891: v2024V891(0x0) = CONST 
    0x2027S0x891: v2027V891 = SLOAD v2022_1V891
    0x2029S0x891: v2029V891(0x100) = CONST 
    0x202cS0x891: v202cV891(0x1) = EXP v2029V891(0x100), v2024V891(0x0)
    0x202eS0x891: v202eV891 = DIV v2027V891, v202cV891(0x1)
    0x202fS0x891: v202fV891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2044S0x891: v2044V891 = AND v202fV891(0xffffffffffffffffffffffffffffffffffffffff), v202eV891
    0x2045S0x891: v2045V891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x205aS0x891: v205aV891 = AND v2045V891(0xffffffffffffffffffffffffffffffffffffffff), v2044V891
    0x205cS0x891: MSTORE v2022_0V891, v205aV891
    0x205dS0x891: v205dV891(0x20) = CONST 
    0x205fS0x891: v205fV891 = ADD v205dV891(0x20), v2022_0V891
    0x2061S0x891: v2061V891(0x1) = CONST 
    0x2063S0x891: v2063V891 = ADD v2061V891(0x1), v2022_1V891
    0x2067S0x891: v2067V891 = GT v2020V891, v205fV891
    0x2068S0x891: v2068V891(0x2022) = CONST 
    0x206bS0x891: JUMPI v2068V891(0x2022), v2067V891

    Begin block 0x206cB0x891
    prev=[0x1fbfB0x891, 0x2022B0x891], succ=[0x209eB0x891]
    =================================
    0x206c_0x2S0x891: v206c_2V891 = PHI v2020V891, v2011V891
    0x2071S0x891: MSTORE v206c_2V891, v899
    0x2072S0x891: v2072V891(0x20) = CONST 
    0x2074S0x891: v2074V891 = ADD v2072V891(0x20), v206c_2V891
    0x2077S0x891: MSTORE v2074V891, v8a2
    0x2078S0x891: v2078V891(0x20) = CONST 
    0x207aS0x891: v207aV891 = ADD v2078V891(0x20), v2074V891
    0x207cS0x891: v207cV891(0x20) = CONST 
    0x207eS0x891: v207eV891 = ADD v207cV891(0x20), v207aV891
    0x2080S0x891: v2080V891 = ISZERO v8ed
    0x2081S0x891: v2081V891 = ISZERO v2080V891
    0x2082S0x891: v2082V891 = ISZERO v2081V891
    0x2083S0x891: v2083V891 = ISZERO v2082V891
    0x2085S0x891: MSTORE v207eV891, v2083V891
    0x2086S0x891: v2086V891(0x20) = CONST 
    0x2088S0x891: v2088V891 = ADD v2086V891(0x20), v207eV891
    0x208aS0x891: v208aV891 = ISZERO v8f8
    0x208bS0x891: v208bV891 = ISZERO v208aV891
    0x208cS0x891: v208cV891 = ISZERO v208bV891
    0x208dS0x891: v208dV891 = ISZERO v208cV891
    0x208fS0x891: MSTORE v2088V891, v208dV891
    0x2090S0x891: v2090V891(0x20) = CONST 
    0x2092S0x891: v2092V891 = ADD v2090V891(0x20), v2088V891
    0x2094S0x891: v2094V891(0x80) = CONST 
    0x2096S0x891: v2096V891(0x20) = CONST 
    0x2098S0x891: v2098V891(0x1000) = MUL v2096V891(0x20), v2094V891(0x80)
    0x209cS0x891: v209cV891(0x0) = CONST 

    Begin block 0x209eB0x891
    prev=[0x206cB0x891, 0x20a7B0x891], succ=[0x20b9B0x891, 0x20a7B0x891]
    =================================
    0x209e_0x0S0x891: v209e_0V891 = PHI v209cV891(0x0), v20b2V891
    0x20a1S0x891: v20a1V891 = LT v209e_0V891, v2098V891(0x1000)
    0x20a2S0x891: v20a2V891 = ISZERO v20a1V891
    0x20a3S0x891: v20a3V891(0x20b9) = CONST 
    0x20a6S0x891: JUMPI v20a3V891(0x20b9), v20a2V891

    Begin block 0x20b9B0x891
    prev=[0x209eB0x891], succ=[0x211cB0x891]
    =================================
    0x20c0S0x891: v20c0V891 = ADD v2098V891(0x1000), v2092V891
    0x20c2S0x891: v20c2V891 = ISZERO v930
    0x20c3S0x891: v20c3V891 = ISZERO v20c2V891
    0x20c4S0x891: v20c4V891 = ISZERO v20c3V891
    0x20c5S0x891: v20c5V891 = ISZERO v20c4V891
    0x20c7S0x891: MSTORE v20c0V891, v20c5V891
    0x20c8S0x891: v20c8V891(0x20) = CONST 
    0x20caS0x891: v20caV891 = ADD v20c8V891(0x20), v20c0V891
    0x20ccS0x891: v20ccV891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20e1S0x891: v20e1V891 = AND v20ccV891(0xffffffffffffffffffffffffffffffffffffffff), v94f
    0x20e2S0x891: v20e2V891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20f7S0x891: v20f7V891 = AND v20e2V891(0xffffffffffffffffffffffffffffffffffffffff), v20e1V891
    0x20f9S0x891: MSTORE v20caV891, v20f7V891
    0x20faS0x891: v20faV891(0x20) = CONST 
    0x20fcS0x891: v20fcV891 = ADD v20faV891(0x20), v20caV891
    0x20ffS0x891: v20ffV891 = SUB v20fcV891, v2011V891
    0x2101S0x891: MSTORE v207aV891, v20ffV891
    0x2105S0x891: v2105V891 = MLOAD v8c4
    0x2107S0x891: MSTORE v20fcV891, v2105V891
    0x2108S0x891: v2108V891(0x20) = CONST 
    0x210aS0x891: v210aV891 = ADD v2108V891(0x20), v20fcV891
    0x210eS0x891: v210eV891 = MLOAD v8c4
    0x2110S0x891: v2110V891(0x20) = CONST 
    0x2112S0x891: v2112V891 = ADD v2110V891(0x20), v8c4
    0x2114S0x891: v2114V891(0x20) = CONST 
    0x2116S0x891: v2116V891 = MUL v2114V891(0x20), v210eV891
    0x211aS0x891: v211aV891(0x0) = CONST 

    Begin block 0x211cB0x891
    prev=[0x20b9B0x891, 0x2125B0x891], succ=[0x2137B0x891, 0x2125B0x891]
    =================================
    0x211c_0x0S0x891: v211c_0V891 = PHI v211aV891(0x0), v2130V891
    0x211fS0x891: v211fV891 = LT v211c_0V891, v2116V891
    0x2120S0x891: v2120V891 = ISZERO v211fV891
    0x2121S0x891: v2121V891(0x2137) = CONST 
    0x2124S0x891: JUMPI v2121V891(0x2137), v2120V891

    Begin block 0x2137B0x891
    prev=[0x211cB0x891], succ=[0x215dB0x891, 0x2161B0x891]
    =================================
    0x213eS0x891: v213eV891 = ADD v2116V891, v210aV891
    0x214bS0x891: v214bV891(0x0) = CONST 
    0x214dS0x891: v214dV891(0x40) = CONST 
    0x214fS0x891: v214fV891 = MLOAD v214dV891(0x40)
    0x2152S0x891: v2152V891 = SUB v213eV891, v214fV891
    0x2156S0x891: v2156V891 = EXTCODESIZE v1fc0V891(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb)
    0x2157S0x891: v2157V891 = ISZERO v2156V891
    0x2158S0x891: v2158V891 = ISZERO v2157V891
    0x2159S0x891: v2159V891(0x2161) = CONST 
    0x215cS0x891: JUMPI v2159V891(0x2161), v2158V891

    Begin block 0x215dB0x891
    prev=[0x2137B0x891], succ=[]
    =================================
    0x215dS0x891: v215dV891(0x0) = CONST 
    0x2160S0x891: REVERT v215dV891(0x0), v215dV891(0x0)

    Begin block 0x2161B0x891
    prev=[0x2137B0x891], succ=[0x216eB0x891, 0x2172B0x891]
    =================================
    0x2162S0x891: v2162V891(0x2c6) = CONST 
    0x2165S0x891: v2165V891 = GAS 
    0x2166S0x891: v2166V891 = SUB v2165V891, v2162V891(0x2c6)
    0x2167S0x891: v2167V891 = DELEGATECALL v2166V891, v1fc0V891(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb), v214fV891, v2152V891, v214fV891, v214bV891(0x0)
    0x2168S0x891: v2168V891 = ISZERO v2167V891
    0x2169S0x891: v2169V891 = ISZERO v2168V891
    0x216aS0x891: v216aV891(0x2172) = CONST 
    0x216dS0x891: JUMPI v216aV891(0x2172), v2169V891

    Begin block 0x216eB0x891
    prev=[0x2161B0x891], succ=[]
    =================================
    0x216eS0x891: v216eV891(0x0) = CONST 
    0x2171S0x891: REVERT v216eV891(0x0), v216eV891(0x0)

    Begin block 0x2172B0x891
    prev=[0x2161B0x891], succ=[0x95d]
    =================================
    0x217eS0x891: JUMP v892(0x95d)

    Begin block 0x95d
    prev=[0x2172B0x891], succ=[]
    =================================
    0x95e: STOP 

    Begin block 0x2125B0x891
    prev=[0x211cB0x891], succ=[0x211cB0x891]
    =================================
    0x2125_0x0S0x891: v2125_0V891 = PHI v211aV891(0x0), v2130V891
    0x2127S0x891: v2127V891 = ADD v2112V891, v2125_0V891
    0x2128S0x891: v2128V891 = MLOAD v2127V891
    0x212bS0x891: v212bV891 = ADD v210aV891, v2125_0V891
    0x212cS0x891: MSTORE v212bV891, v2128V891
    0x212dS0x891: v212dV891(0x20) = CONST 
    0x2130S0x891: v2130V891 = ADD v2125_0V891, v212dV891(0x20)
    0x2133S0x891: v2133V891(0x211c) = CONST 
    0x2136S0x891: JUMP v2133V891(0x211c)

    Begin block 0x20a7B0x891
    prev=[0x209eB0x891], succ=[0x209eB0x891]
    =================================
    0x20a7_0x0S0x891: v20a7_0V891 = PHI v209cV891(0x0), v20b2V891
    0x20a9S0x891: v20a9V891 = ADD v90e, v20a7_0V891
    0x20aaS0x891: v20aaV891 = MLOAD v20a9V891
    0x20adS0x891: v20adV891 = ADD v2092V891, v20a7_0V891
    0x20aeS0x891: MSTORE v20adV891, v20aaV891
    0x20afS0x891: v20afV891(0x20) = CONST 
    0x20b2S0x891: v20b2V891 = ADD v20a7_0V891, v20afV891(0x20)
    0x20b5S0x891: v20b5V891(0x209e) = CONST 
    0x20b8S0x891: JUMP v20b5V891(0x209e)

    Begin block 0x1fa3B0x891
    prev=[0x1f8bB0x891], succ=[0x1fb4B0x891]
    =================================
    0x1fa4S0x891: v1fa4V891(0x12) = CONST 
    0x1fa6S0x891: v1fa6V891(0x1) = CONST 
    0x1fa9S0x891: v1fa9V891 = SLOAD v1fa4V891(0x12)
    0x1fabS0x891: v1fabV891(0x100) = CONST 
    0x1faeS0x891: v1faeV891(0x100) = EXP v1fabV891(0x100), v1fa6V891(0x1)
    0x1fb0S0x891: v1fb0V891 = DIV v1fa9V891, v1faeV891(0x100)
    0x1fb1S0x891: v1fb1V891(0xff) = CONST 
    0x1fb3S0x891: v1fb3V891 = AND v1fb1V891(0xff), v1fb0V891

}

function managerAddress()() public {
    Begin block 0x95f
    prev=[], succ=[0x966, 0x96a]
    =================================
    0x960: v960 = CALLVALUE 
    0x961: v961 = ISZERO v960
    0x962: v962(0x96a) = CONST 
    0x965: JUMPI v962(0x96a), v961

    Begin block 0x966
    prev=[0x95f], succ=[]
    =================================
    0x966: v966(0x0) = CONST 
    0x969: REVERT v966(0x0), v966(0x0)

    Begin block 0x96a
    prev=[0x95f], succ=[0x217f]
    =================================
    0x96b: v96b(0x972) = CONST 
    0x96e: v96e(0x217f) = CONST 
    0x971: JUMP v96e(0x217f)

    Begin block 0x217f
    prev=[0x96a], succ=[0x972]
    =================================
    0x2180: v2180(0x1) = CONST 
    0x2182: v2182(0x0) = CONST 
    0x2185: v2185 = SLOAD v2180(0x1)
    0x2187: v2187(0x100) = CONST 
    0x218a: v218a(0x1) = EXP v2187(0x100), v2182(0x0)
    0x218c: v218c = DIV v2185, v218a(0x1)
    0x218d: v218d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21a2: v21a2 = AND v218d(0xffffffffffffffffffffffffffffffffffffffff), v218c
    0x21a4: JUMP v96b(0x972)

    Begin block 0x972
    prev=[0x217f], succ=[]
    =================================
    0x973: v973(0x40) = CONST 
    0x975: v975 = MLOAD v973(0x40)
    0x978: v978(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x98d: v98d = AND v978(0xffffffffffffffffffffffffffffffffffffffff), v21a2
    0x98e: v98e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9a3: v9a3 = AND v98e(0xffffffffffffffffffffffffffffffffffffffff), v98d
    0x9a5: MSTORE v975, v9a3
    0x9a6: v9a6(0x20) = CONST 
    0x9a8: v9a8 = ADD v9a6(0x20), v975
    0x9ac: v9ac(0x40) = CONST 
    0x9ae: v9ae = MLOAD v9ac(0x40)
    0x9b1: v9b1(0x20) = SUB v9a8, v9ae
    0x9b3: RETURN v9ae, v9b1(0x20)

}

function setManager(address)() public {
    Begin block 0x9b4
    prev=[], succ=[0x9bb, 0x9bf]
    =================================
    0x9b5: v9b5 = CALLVALUE 
    0x9b6: v9b6 = ISZERO v9b5
    0x9b7: v9b7(0x9bf) = CONST 
    0x9ba: JUMPI v9b7(0x9bf), v9b6

    Begin block 0x9bb
    prev=[0x9b4], succ=[]
    =================================
    0x9bb: v9bb(0x0) = CONST 
    0x9be: REVERT v9bb(0x0), v9bb(0x0)

    Begin block 0x9bf
    prev=[0x9b4], succ=[0x21a5]
    =================================
    0x9c0: v9c0(0x9eb) = CONST 
    0x9c3: v9c3(0x4) = CONST 
    0x9c7: v9c7 = CALLDATALOAD v9c3(0x4)
    0x9c8: v9c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9dd: v9dd = AND v9c8(0xffffffffffffffffffffffffffffffffffffffff), v9c7
    0x9df: v9df(0x20) = CONST 
    0x9e1: v9e1(0x24) = ADD v9df(0x20), v9c3(0x4)
    0x9e7: v9e7(0x21a5) = CONST 
    0x9ea: JUMP v9e7(0x21a5)

    Begin block 0x21a5
    prev=[0x9bf], succ=[0x21fc, 0x2200]
    =================================
    0x21a6: v21a6(0x0) = CONST 
    0x21aa: v21aa = SLOAD v21a6(0x0)
    0x21ac: v21ac(0x100) = CONST 
    0x21af: v21af(0x1) = EXP v21ac(0x100), v21a6(0x0)
    0x21b1: v21b1 = DIV v21aa, v21af(0x1)
    0x21b2: v21b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21c7: v21c7 = AND v21b2(0xffffffffffffffffffffffffffffffffffffffff), v21b1
    0x21c8: v21c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21dd: v21dd = AND v21c8(0xffffffffffffffffffffffffffffffffffffffff), v21c7
    0x21de: v21de = CALLER 
    0x21df: v21df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21f4: v21f4 = AND v21df(0xffffffffffffffffffffffffffffffffffffffff), v21de
    0x21f5: v21f5 = EQ v21f4, v21dd
    0x21f6: v21f6 = ISZERO v21f5
    0x21f7: v21f7 = ISZERO v21f6
    0x21f8: v21f8(0x2200) = CONST 
    0x21fb: JUMPI v21f8(0x2200), v21f7

    Begin block 0x21fc
    prev=[0x21a5], succ=[]
    =================================
    0x21fc: v21fc(0x0) = CONST 
    0x21ff: REVERT v21fc(0x0), v21fc(0x0)

    Begin block 0x2200
    prev=[0x21a5], succ=[0x2238, 0x223c]
    =================================
    0x2201: v2201(0x0) = CONST 
    0x2203: v2203(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2218: v2218(0x0) = AND v2203(0xffffffffffffffffffffffffffffffffffffffff), v2201(0x0)
    0x221a: v221a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x222f: v222f = AND v221a(0xffffffffffffffffffffffffffffffffffffffff), v9dd
    0x2230: v2230 = EQ v222f, v2218(0x0)
    0x2231: v2231 = ISZERO v2230
    0x2232: v2232 = ISZERO v2231
    0x2233: v2233 = ISZERO v2232
    0x2234: v2234(0x223c) = CONST 
    0x2237: JUMPI v2234(0x223c), v2233

    Begin block 0x2238
    prev=[0x2200], succ=[]
    =================================
    0x2238: v2238(0x0) = CONST 
    0x223b: REVERT v2238(0x0), v2238(0x0)

    Begin block 0x223c
    prev=[0x2200], succ=[0x9eb]
    =================================
    0x223e: v223e(0x1) = CONST 
    0x2240: v2240(0x0) = CONST 
    0x2242: v2242(0x100) = CONST 
    0x2245: v2245(0x1) = EXP v2242(0x100), v2240(0x0)
    0x2247: v2247 = SLOAD v223e(0x1)
    0x2249: v2249(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x225e: v225e(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2249(0xffffffffffffffffffffffffffffffffffffffff), v2245(0x1)
    0x225f: v225f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v225e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2260: v2260 = AND v225f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2247
    0x2263: v2263(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2278: v2278 = AND v2263(0xffffffffffffffffffffffffffffffffffffffff), v9dd
    0x2279: v2279 = MUL v2278, v2245(0x1)
    0x227a: v227a = OR v2279, v2260
    0x227c: SSTORE v223e(0x1), v227a
    0x227f: JUMP v9c0(0x9eb)

    Begin block 0x9eb
    prev=[0x223c], succ=[]
    =================================
    0x9ec: STOP 

}

function setNextImagePart(uint256,uint16,uint16,uint16,uint256[])() public {
    Begin block 0x9ed
    prev=[], succ=[0x9f4, 0x9f8]
    =================================
    0x9ee: v9ee = CALLVALUE 
    0x9ef: v9ef = ISZERO v9ee
    0x9f0: v9f0(0x9f8) = CONST 
    0x9f3: JUMPI v9f0(0x9f8), v9ef

    Begin block 0x9f4
    prev=[0x9ed], succ=[]
    =================================
    0x9f4: v9f4(0x0) = CONST 
    0x9f7: REVERT v9f4(0x0), v9f4(0x0)

    Begin block 0x9f8
    prev=[0x9ed], succ=[0x2280B0x9f8]
    =================================
    0x9f9: v9f9(0xa75) = CONST 
    0x9fc: v9fc(0x4) = CONST 
    0xa00: va00 = CALLDATALOAD v9fc(0x4)
    0xa02: va02(0x20) = CONST 
    0xa04: va04(0x24) = ADD va02(0x20), v9fc(0x4)
    0xa09: va09 = CALLDATALOAD va04(0x24)
    0xa0a: va0a(0xffff) = CONST 
    0xa0d: va0d = AND va0a(0xffff), va09
    0xa0f: va0f(0x20) = CONST 
    0xa11: va11(0x44) = ADD va0f(0x20), va04(0x24)
    0xa16: va16 = CALLDATALOAD va11(0x44)
    0xa17: va17(0xffff) = CONST 
    0xa1a: va1a = AND va17(0xffff), va16
    0xa1c: va1c(0x20) = CONST 
    0xa1e: va1e(0x64) = ADD va1c(0x20), va11(0x44)
    0xa23: va23 = CALLDATALOAD va1e(0x64)
    0xa24: va24(0xffff) = CONST 
    0xa27: va27 = AND va24(0xffff), va23
    0xa29: va29(0x20) = CONST 
    0xa2b: va2b(0x84) = ADD va29(0x20), va1e(0x64)
    0xa30: va30 = CALLDATALOAD va2b(0x84)
    0xa32: va32(0x20) = CONST 
    0xa34: va34(0xa4) = ADD va32(0x20), va2b(0x84)
    0xa37: va37 = ADD v9fc(0x4), va30
    0xa39: va39 = CALLDATALOAD va37
    0xa3b: va3b(0x20) = CONST 
    0xa3d: va3d = ADD va3b(0x20), va37
    0xa41: va41(0x20) = CONST 
    0xa43: va43 = MUL va41(0x20), va39
    0xa44: va44(0x20) = CONST 
    0xa46: va46 = ADD va44(0x20), va43
    0xa47: va47(0x40) = CONST 
    0xa49: va49 = MLOAD va47(0x40)
    0xa4c: va4c = ADD va49, va46
    0xa4d: va4d(0x40) = CONST 
    0xa4f: MSTORE va4d(0x40), va4c
    0xa57: MSTORE va49, va39
    0xa58: va58(0x20) = CONST 
    0xa5a: va5a = ADD va58(0x20), va49
    0xa5d: va5d(0x20) = CONST 
    0xa5f: va5f = MUL va5d(0x20), va39
    0xa63: CALLDATACOPY va5a, va3d, va5f
    0xa65: va65 = ADD va5a, va5f
    0xa71: va71(0x2280) = CONST 
    0xa74: JUMP va71(0x2280), va49, va27, va1a, va0d, va00, v9f9(0xa75)

    Begin block 0x2280B0x9f8
    prev=[0x9f8], succ=[0x22a9B0x9f8, 0x2298B0x9f8]
    =================================
    0x2281S0x9f8: v2281V9f8(0x12) = CONST 
    0x2283S0x9f8: v2283V9f8(0x0) = CONST 
    0x2286S0x9f8: v2286V9f8 = SLOAD v2281V9f8(0x12)
    0x2288S0x9f8: v2288V9f8(0x100) = CONST 
    0x228bS0x9f8: v228bV9f8(0x1) = EXP v2288V9f8(0x100), v2283V9f8(0x0)
    0x228dS0x9f8: v228dV9f8 = DIV v2286V9f8, v228bV9f8(0x1)
    0x228eS0x9f8: v228eV9f8(0xff) = CONST 
    0x2290S0x9f8: v2290V9f8 = AND v228eV9f8(0xff), v228dV9f8
    0x2291S0x9f8: v2291V9f8 = ISZERO v2290V9f8
    0x2293S0x9f8: v2293V9f8 = ISZERO v2291V9f8
    0x2294S0x9f8: v2294V9f8(0x22a9) = CONST 
    0x2297S0x9f8: JUMPI v2294V9f8(0x22a9), v2293V9f8

    Begin block 0x22a9B0x9f8
    prev=[0x2280B0x9f8, 0x2298B0x9f8], succ=[0x22b0B0x9f8, 0x22b4B0x9f8]
    =================================
    0x22a9_0x0S0x9f8: v22a9_0V9f8 = PHI v2291V9f8, v22a8V9f8
    0x22aaS0x9f8: v22aaV9f8 = ISZERO v22a9_0V9f8
    0x22abS0x9f8: v22abV9f8 = ISZERO v22aaV9f8
    0x22acS0x9f8: v22acV9f8(0x22b4) = CONST 
    0x22afS0x9f8: JUMPI v22acV9f8(0x22b4), v22abV9f8

    Begin block 0x22b0B0x9f8
    prev=[0x22a9B0x9f8], succ=[]
    =================================
    0x22b0S0x9f8: v22b0V9f8(0x0) = CONST 
    0x22b3S0x9f8: REVERT v22b0V9f8(0x0), v22b0V9f8(0x0)

    Begin block 0x22b4B0x9f8
    prev=[0x22a9B0x9f8], succ=[0x230eB0x9f8, 0x235eB0x9f8]
    =================================
    0x22b5S0x9f8: v22b5V9f8(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab) = CONST 
    0x22caS0x9f8: v22caV9f8(0x9c161d1a) = CONST 
    0x22cfS0x9f8: v22cfV9f8(0x2) = CONST 
    0x22d6S0x9f8: v22d6V9f8(0x40) = CONST 
    0x22d8S0x9f8: v22d8V9f8 = MLOAD v22d6V9f8(0x40)
    0x22daS0x9f8: v22daV9f8(0xffffffff) = CONST 
    0x22dfS0x9f8: v22dfV9f8(0x9c161d1a) = AND v22daV9f8(0xffffffff), v22caV9f8(0x9c161d1a)
    0x22e0S0x9f8: v22e0V9f8(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x22feS0x9f8: v22feV9f8(0x9c161d1a00000000000000000000000000000000000000000000000000000000) = MUL v22e0V9f8(0x100000000000000000000000000000000000000000000000000000000), v22dfV9f8(0x9c161d1a)
    0x2300S0x9f8: MSTORE v22d8V9f8, v22feV9f8(0x9c161d1a00000000000000000000000000000000000000000000000000000000)
    0x2301S0x9f8: v2301V9f8(0x4) = CONST 
    0x2303S0x9f8: v2303V9f8 = ADD v2301V9f8(0x4), v22d8V9f8
    0x2306S0x9f8: v2306V9f8(0x10) = CONST 
    0x2309S0x9f8: v2309V9f8(0x0) = ISZERO v2306V9f8(0x10)
    0x230aS0x9f8: v230aV9f8(0x235e) = CONST 
    0x230dS0x9f8: JUMPI v230aV9f8(0x235e), v2309V9f8(0x0)

    Begin block 0x230eB0x9f8
    prev=[0x22b4B0x9f8], succ=[0x2314B0x9f8]
    =================================
    0x230eS0x9f8: v230eV9f8(0x20) = CONST 
    0x2310S0x9f8: v2310V9f8(0x200) = MUL v230eV9f8(0x20), v2306V9f8(0x10)
    0x2312S0x9f8: v2312V9f8 = ADD v2303V9f8, v2310V9f8(0x200)

    Begin block 0x2314B0x9f8
    prev=[0x230eB0x9f8, 0x2314B0x9f8], succ=[0x235eB0x9f8, 0x2314B0x9f8]
    =================================
    0x2314_0x0S0x9f8: v2314_0V9f8 = PHI v2303V9f8, v2351V9f8
    0x2314_0x1S0x9f8: v2314_1V9f8 = PHI v22cfV9f8(0x2), v2355V9f8
    0x2316S0x9f8: v2316V9f8(0x0) = CONST 
    0x2319S0x9f8: v2319V9f8 = SLOAD v2314_1V9f8
    0x231bS0x9f8: v231bV9f8(0x100) = CONST 
    0x231eS0x9f8: v231eV9f8(0x1) = EXP v231bV9f8(0x100), v2316V9f8(0x0)
    0x2320S0x9f8: v2320V9f8 = DIV v2319V9f8, v231eV9f8(0x1)
    0x2321S0x9f8: v2321V9f8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2336S0x9f8: v2336V9f8 = AND v2321V9f8(0xffffffffffffffffffffffffffffffffffffffff), v2320V9f8
    0x2337S0x9f8: v2337V9f8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x234cS0x9f8: v234cV9f8 = AND v2337V9f8(0xffffffffffffffffffffffffffffffffffffffff), v2336V9f8
    0x234eS0x9f8: MSTORE v2314_0V9f8, v234cV9f8
    0x234fS0x9f8: v234fV9f8(0x20) = CONST 
    0x2351S0x9f8: v2351V9f8 = ADD v234fV9f8(0x20), v2314_0V9f8
    0x2353S0x9f8: v2353V9f8(0x1) = CONST 
    0x2355S0x9f8: v2355V9f8 = ADD v2353V9f8(0x1), v2314_1V9f8
    0x2359S0x9f8: v2359V9f8 = GT v2312V9f8, v2351V9f8
    0x235aS0x9f8: v235aV9f8(0x2314) = CONST 
    0x235dS0x9f8: JUMPI v235aV9f8(0x2314), v2359V9f8

    Begin block 0x235eB0x9f8
    prev=[0x22b4B0x9f8, 0x2314B0x9f8], succ=[0x23b4B0x9f8]
    =================================
    0x235e_0x2S0x9f8: v235e_2V9f8 = PHI v2312V9f8, v2303V9f8
    0x2363S0x9f8: MSTORE v235e_2V9f8, va00
    0x2364S0x9f8: v2364V9f8(0x20) = CONST 
    0x2366S0x9f8: v2366V9f8 = ADD v2364V9f8(0x20), v235e_2V9f8
    0x2368S0x9f8: v2368V9f8(0xffff) = CONST 
    0x236bS0x9f8: v236bV9f8 = AND v2368V9f8(0xffff), va0d
    0x236cS0x9f8: v236cV9f8(0xffff) = CONST 
    0x236fS0x9f8: v236fV9f8 = AND v236cV9f8(0xffff), v236bV9f8
    0x2371S0x9f8: MSTORE v2366V9f8, v236fV9f8
    0x2372S0x9f8: v2372V9f8(0x20) = CONST 
    0x2374S0x9f8: v2374V9f8 = ADD v2372V9f8(0x20), v2366V9f8
    0x2376S0x9f8: v2376V9f8(0xffff) = CONST 
    0x2379S0x9f8: v2379V9f8 = AND v2376V9f8(0xffff), va1a
    0x237aS0x9f8: v237aV9f8(0xffff) = CONST 
    0x237dS0x9f8: v237dV9f8 = AND v237aV9f8(0xffff), v2379V9f8
    0x237fS0x9f8: MSTORE v2374V9f8, v237dV9f8
    0x2380S0x9f8: v2380V9f8(0x20) = CONST 
    0x2382S0x9f8: v2382V9f8 = ADD v2380V9f8(0x20), v2374V9f8
    0x2384S0x9f8: v2384V9f8(0xffff) = CONST 
    0x2387S0x9f8: v2387V9f8 = AND v2384V9f8(0xffff), va27
    0x2388S0x9f8: v2388V9f8(0xffff) = CONST 
    0x238bS0x9f8: v238bV9f8 = AND v2388V9f8(0xffff), v2387V9f8
    0x238dS0x9f8: MSTORE v2382V9f8, v238bV9f8
    0x238eS0x9f8: v238eV9f8(0x20) = CONST 
    0x2390S0x9f8: v2390V9f8 = ADD v238eV9f8(0x20), v2382V9f8
    0x2392S0x9f8: v2392V9f8(0x20) = CONST 
    0x2394S0x9f8: v2394V9f8 = ADD v2392V9f8(0x20), v2390V9f8
    0x2397S0x9f8: v2397V9f8 = SUB v2394V9f8, v2303V9f8
    0x2399S0x9f8: MSTORE v2390V9f8, v2397V9f8
    0x239dS0x9f8: v239dV9f8 = MLOAD va49
    0x239fS0x9f8: MSTORE v2394V9f8, v239dV9f8
    0x23a0S0x9f8: v23a0V9f8(0x20) = CONST 
    0x23a2S0x9f8: v23a2V9f8 = ADD v23a0V9f8(0x20), v2394V9f8
    0x23a6S0x9f8: v23a6V9f8 = MLOAD va49
    0x23a8S0x9f8: v23a8V9f8(0x20) = CONST 
    0x23aaS0x9f8: v23aaV9f8 = ADD v23a8V9f8(0x20), va49
    0x23acS0x9f8: v23acV9f8(0x20) = CONST 
    0x23aeS0x9f8: v23aeV9f8 = MUL v23acV9f8(0x20), v23a6V9f8
    0x23b2S0x9f8: v23b2V9f8(0x0) = CONST 

    Begin block 0x23b4B0x9f8
    prev=[0x235eB0x9f8, 0x23bdB0x9f8], succ=[0x23cfB0x9f8, 0x23bdB0x9f8]
    =================================
    0x23b4_0x0S0x9f8: v23b4_0V9f8 = PHI v23b2V9f8(0x0), v23c8V9f8
    0x23b7S0x9f8: v23b7V9f8 = LT v23b4_0V9f8, v23aeV9f8
    0x23b8S0x9f8: v23b8V9f8 = ISZERO v23b7V9f8
    0x23b9S0x9f8: v23b9V9f8(0x23cf) = CONST 
    0x23bcS0x9f8: JUMPI v23b9V9f8(0x23cf), v23b8V9f8

    Begin block 0x23cfB0x9f8
    prev=[0x23b4B0x9f8], succ=[0x23f2B0x9f8, 0x23f6B0x9f8]
    =================================
    0x23d6S0x9f8: v23d6V9f8 = ADD v23aeV9f8, v23a2V9f8
    0x23e0S0x9f8: v23e0V9f8(0x0) = CONST 
    0x23e2S0x9f8: v23e2V9f8(0x40) = CONST 
    0x23e4S0x9f8: v23e4V9f8 = MLOAD v23e2V9f8(0x40)
    0x23e7S0x9f8: v23e7V9f8 = SUB v23d6V9f8, v23e4V9f8
    0x23ebS0x9f8: v23ebV9f8 = EXTCODESIZE v22b5V9f8(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab)
    0x23ecS0x9f8: v23ecV9f8 = ISZERO v23ebV9f8
    0x23edS0x9f8: v23edV9f8 = ISZERO v23ecV9f8
    0x23eeS0x9f8: v23eeV9f8(0x23f6) = CONST 
    0x23f1S0x9f8: JUMPI v23eeV9f8(0x23f6), v23edV9f8

    Begin block 0x23f2B0x9f8
    prev=[0x23cfB0x9f8], succ=[]
    =================================
    0x23f2S0x9f8: v23f2V9f8(0x0) = CONST 
    0x23f5S0x9f8: REVERT v23f2V9f8(0x0), v23f2V9f8(0x0)

    Begin block 0x23f6B0x9f8
    prev=[0x23cfB0x9f8], succ=[0x2403B0x9f8, 0x2407B0x9f8]
    =================================
    0x23f7S0x9f8: v23f7V9f8(0x2c6) = CONST 
    0x23faS0x9f8: v23faV9f8 = GAS 
    0x23fbS0x9f8: v23fbV9f8 = SUB v23faV9f8, v23f7V9f8(0x2c6)
    0x23fcS0x9f8: v23fcV9f8 = DELEGATECALL v23fbV9f8, v22b5V9f8(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab), v23e4V9f8, v23e7V9f8, v23e4V9f8, v23e0V9f8(0x0)
    0x23fdS0x9f8: v23fdV9f8 = ISZERO v23fcV9f8
    0x23feS0x9f8: v23feV9f8 = ISZERO v23fdV9f8
    0x23ffS0x9f8: v23ffV9f8(0x2407) = CONST 
    0x2402S0x9f8: JUMPI v23ffV9f8(0x2407), v23feV9f8

    Begin block 0x2403B0x9f8
    prev=[0x23f6B0x9f8], succ=[]
    =================================
    0x2403S0x9f8: v2403V9f8(0x0) = CONST 
    0x2406S0x9f8: REVERT v2403V9f8(0x0), v2403V9f8(0x0)

    Begin block 0x2407B0x9f8
    prev=[0x23f6B0x9f8], succ=[0xa75]
    =================================
    0x2410S0x9f8: JUMP v9f9(0xa75)

    Begin block 0xa75
    prev=[0x2407B0x9f8], succ=[]
    =================================
    0xa76: STOP 

    Begin block 0x23bdB0x9f8
    prev=[0x23b4B0x9f8], succ=[0x23b4B0x9f8]
    =================================
    0x23bd_0x0S0x9f8: v23bd_0V9f8 = PHI v23b2V9f8(0x0), v23c8V9f8
    0x23bfS0x9f8: v23bfV9f8 = ADD v23aaV9f8, v23bd_0V9f8
    0x23c0S0x9f8: v23c0V9f8 = MLOAD v23bfV9f8
    0x23c3S0x9f8: v23c3V9f8 = ADD v23a2V9f8, v23bd_0V9f8
    0x23c4S0x9f8: MSTORE v23c3V9f8, v23c0V9f8
    0x23c5S0x9f8: v23c5V9f8(0x20) = CONST 
    0x23c8S0x9f8: v23c8V9f8 = ADD v23bd_0V9f8, v23c5V9f8(0x20)
    0x23cbS0x9f8: v23cbV9f8(0x23b4) = CONST 
    0x23ceS0x9f8: JUMP v23cbV9f8(0x23b4)

    Begin block 0x2298B0x9f8
    prev=[0x2280B0x9f8], succ=[0x22a9B0x9f8]
    =================================
    0x2299S0x9f8: v2299V9f8(0x12) = CONST 
    0x229bS0x9f8: v229bV9f8(0x1) = CONST 
    0x229eS0x9f8: v229eV9f8 = SLOAD v2299V9f8(0x12)
    0x22a0S0x9f8: v22a0V9f8(0x100) = CONST 
    0x22a3S0x9f8: v22a3V9f8(0x100) = EXP v22a0V9f8(0x100), v229bV9f8(0x1)
    0x22a5S0x9f8: v22a5V9f8 = DIV v229eV9f8, v22a3V9f8(0x100)
    0x22a6S0x9f8: v22a6V9f8(0xff) = CONST 
    0x22a8S0x9f8: v22a8V9f8 = AND v22a6V9f8(0xff), v22a5V9f8

}

function getOwnedArea(address)() public {
    Begin block 0xa77
    prev=[], succ=[0xa7e, 0xa82]
    =================================
    0xa78: va78 = CALLVALUE 
    0xa79: va79 = ISZERO va78
    0xa7a: va7a(0xa82) = CONST 
    0xa7d: JUMPI va7a(0xa82), va79

    Begin block 0xa7e
    prev=[0xa77], succ=[]
    =================================
    0xa7e: va7e(0x0) = CONST 
    0xa81: REVERT va7e(0x0), va7e(0x0)

    Begin block 0xa82
    prev=[0xa77], succ=[0x2411]
    =================================
    0xa83: va83(0xaae) = CONST 
    0xa86: va86(0x4) = CONST 
    0xa8a: va8a = CALLDATALOAD va86(0x4)
    0xa8b: va8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaa0: vaa0 = AND va8b(0xffffffffffffffffffffffffffffffffffffffff), va8a
    0xaa2: vaa2(0x20) = CONST 
    0xaa4: vaa4(0x24) = ADD vaa2(0x20), va86(0x4)
    0xaaa: vaaa(0x2411) = CONST 
    0xaad: JUMP vaaa(0x2411)

    Begin block 0x2411
    prev=[0xa82], succ=[0x2435, 0x2485]
    =================================
    0x2412: v2412(0x0) = CONST 
    0x2414: v2414(0x248f) = CONST 
    0x2417: v2417(0x2) = CONST 
    0x2419: v2419(0x10) = CONST 
    0x241c: v241c(0x20) = CONST 
    0x241e: v241e(0x200) = MUL v241c(0x20), v2419(0x10)
    0x241f: v241f(0x40) = CONST 
    0x2421: v2421 = MLOAD v241f(0x40)
    0x2424: v2424 = ADD v2421, v241e(0x200)
    0x2425: v2425(0x40) = CONST 
    0x2427: MSTORE v2425(0x40), v2424
    0x242d: v242d(0x10) = CONST 
    0x2430: v2430(0x0) = ISZERO v242d(0x10)
    0x2431: v2431(0x2485) = CONST 
    0x2434: JUMPI v2431(0x2485), v2430(0x0)

    Begin block 0x2435
    prev=[0x2411], succ=[0x243b]
    =================================
    0x2435: v2435(0x20) = CONST 
    0x2437: v2437(0x200) = MUL v2435(0x20), v242d(0x10)
    0x2439: v2439 = ADD v2421, v2437(0x200)

    Begin block 0x243b
    prev=[0x2435, 0x243b], succ=[0x2485, 0x243b]
    =================================
    0x243b_0x0: v243b_0 = PHI v2421, v2478
    0x243b_0x1: v243b_1 = PHI v2417(0x2), v247c
    0x243d: v243d(0x0) = CONST 
    0x2440: v2440 = SLOAD v243b_1
    0x2442: v2442(0x100) = CONST 
    0x2445: v2445(0x1) = EXP v2442(0x100), v243d(0x0)
    0x2447: v2447 = DIV v2440, v2445(0x1)
    0x2448: v2448(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x245d: v245d = AND v2448(0xffffffffffffffffffffffffffffffffffffffff), v2447
    0x245e: v245e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2473: v2473 = AND v245e(0xffffffffffffffffffffffffffffffffffffffff), v245d
    0x2475: MSTORE v243b_0, v2473
    0x2476: v2476(0x20) = CONST 
    0x2478: v2478 = ADD v2476(0x20), v243b_0
    0x247a: v247a(0x1) = CONST 
    0x247c: v247c = ADD v247a(0x1), v243b_1
    0x2480: v2480 = GT v2439, v2478
    0x2481: v2481(0x243b) = CONST 
    0x2484: JUMPI v2481(0x243b), v2480

    Begin block 0x2485
    prev=[0x2411, 0x243b], succ=[0x29c90xa77]
    =================================
    0x248b: v248b(0x29c9) = CONST 
    0x248e: JUMP v248b(0x29c9)

    Begin block 0x29c90xa77
    prev=[0x2485], succ=[0x29d90xa77, 0x29da0xa77]
    =================================
    0x29ca0xa77: va7729ca(0x0) = CONST 
    0x29cd0xa77: va7729cd(0x6) = CONST 
    0x29cf0xa77: va7729cf(0x10) = CONST 
    0x29d20xa77: va7729d2(0x1) = LT va7729cd(0x6), va7729cf(0x10)
    0x29d30xa77: va7729d3(0x0) = ISZERO va7729d2(0x1)
    0x29d40xa77: va7729d4(0x1) = ISZERO va7729d3(0x0)
    0x29d50xa77: va7729d5(0x29da) = CONST 
    0x29d80xa77: JUMPI va7729d5(0x29da), va7729d4(0x1)

    Begin block 0x29d90xa77
    prev=[0x29c90xa77], succ=[]
    =================================
    0x29d90xa77: THROW 

    Begin block 0x29da0xa77
    prev=[0x29c90xa77], succ=[0x248f]
    =================================
    0x29db0xa77: va7729db(0x20) = CONST 
    0x29dd0xa77: va7729dd(0xc0) = MUL va7729db(0x20), va7729cd(0x6)
    0x29de0xa77: va7729de = ADD va7729dd(0xc0), v2421
    0x29df0xa77: va7729df = MLOAD va7729de
    0x29e50xa77: JUMP v2414(0x248f)

    Begin block 0x248f
    prev=[0x29da0xa77], succ=[0x252d, 0x2531]
    =================================
    0x2490: v2490(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24a5: v24a5 = AND v2490(0xffffffffffffffffffffffffffffffffffffffff), va7729df
    0x24a6: v24a6(0xe168a31a) = CONST 
    0x24ac: v24ac(0x0) = CONST 
    0x24ae: v24ae(0x40) = CONST 
    0x24b0: v24b0 = MLOAD v24ae(0x40)
    0x24b1: v24b1(0x20) = CONST 
    0x24b3: v24b3 = ADD v24b1(0x20), v24b0
    0x24b4: MSTORE v24b3, v24ac(0x0)
    0x24b5: v24b5(0x40) = CONST 
    0x24b7: v24b7 = MLOAD v24b5(0x40)
    0x24b9: v24b9(0xffffffff) = CONST 
    0x24be: v24be(0xe168a31a) = AND v24b9(0xffffffff), v24a6(0xe168a31a)
    0x24bf: v24bf(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x24dd: v24dd(0xe168a31a00000000000000000000000000000000000000000000000000000000) = MUL v24bf(0x100000000000000000000000000000000000000000000000000000000), v24be(0xe168a31a)
    0x24df: MSTORE v24b7, v24dd(0xe168a31a00000000000000000000000000000000000000000000000000000000)
    0x24e0: v24e0(0x4) = CONST 
    0x24e2: v24e2 = ADD v24e0(0x4), v24b7
    0x24e5: v24e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24fa: v24fa = AND v24e5(0xffffffffffffffffffffffffffffffffffffffff), vaa0
    0x24fb: v24fb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2510: v2510 = AND v24fb(0xffffffffffffffffffffffffffffffffffffffff), v24fa
    0x2512: MSTORE v24e2, v2510
    0x2513: v2513(0x20) = CONST 
    0x2515: v2515 = ADD v2513(0x20), v24e2
    0x2519: v2519(0x20) = CONST 
    0x251b: v251b(0x40) = CONST 
    0x251d: v251d = MLOAD v251b(0x40)
    0x2520: v2520(0x24) = SUB v2515, v251d
    0x2522: v2522(0x0) = CONST 
    0x2526: v2526 = EXTCODESIZE v24a5
    0x2527: v2527 = ISZERO v2526
    0x2528: v2528 = ISZERO v2527
    0x2529: v2529(0x2531) = CONST 
    0x252c: JUMPI v2529(0x2531), v2528

    Begin block 0x252d
    prev=[0x248f], succ=[]
    =================================
    0x252d: v252d(0x0) = CONST 
    0x2530: REVERT v252d(0x0), v252d(0x0)

    Begin block 0x2531
    prev=[0x248f], succ=[0x253e, 0x2542]
    =================================
    0x2532: v2532(0x2c6) = CONST 
    0x2535: v2535 = GAS 
    0x2536: v2536 = SUB v2535, v2532(0x2c6)
    0x2537: v2537 = CALL v2536, v24a5, v2522(0x0), v251d, v2520(0x24), v251d, v2519(0x20)
    0x2538: v2538 = ISZERO v2537
    0x2539: v2539 = ISZERO v2538
    0x253a: v253a(0x2542) = CONST 
    0x253d: JUMPI v253a(0x2542), v2539

    Begin block 0x253e
    prev=[0x2531], succ=[]
    =================================
    0x253e: v253e(0x0) = CONST 
    0x2541: REVERT v253e(0x0), v253e(0x0)

    Begin block 0x2542
    prev=[0x2531], succ=[0xaae]
    =================================
    0x2546: v2546(0x40) = CONST 
    0x2548: v2548 = MLOAD v2546(0x40)
    0x254a: v254a = MLOAD v2548
    0x2552: JUMP va83(0xaae)

    Begin block 0xaae
    prev=[0x2542], succ=[]
    =================================
    0xaaf: vaaf(0x40) = CONST 
    0xab1: vab1 = MLOAD vaaf(0x40)
    0xab5: MSTORE vab1, v254a
    0xab6: vab6(0x20) = CONST 
    0xab8: vab8 = ADD vab6(0x20), vab1
    0xabc: vabc(0x40) = CONST 
    0xabe: vabe = MLOAD vabc(0x40)
    0xac1: vac1(0x20) = SUB vab8, vabe
    0xac3: RETURN vabe, vac1(0x20)

}

function checkImageInput(uint256,uint256,uint256[],bool,bool)() public {
    Begin block 0xac4
    prev=[], succ=[0xacb, 0xacf]
    =================================
    0xac5: vac5 = CALLVALUE 
    0xac6: vac6 = ISZERO vac5
    0xac7: vac7(0xacf) = CONST 
    0xaca: JUMPI vac7(0xacf), vac6

    Begin block 0xacb
    prev=[0xac4], succ=[]
    =================================
    0xacb: vacb(0x0) = CONST 
    0xace: REVERT vacb(0x0), vacb(0x0)

    Begin block 0xacf
    prev=[0xac4], succ=[0x2553B0xacf]
    =================================
    0xad0: vad0(0xb44) = CONST 
    0xad3: vad3(0x4) = CONST 
    0xad7: vad7 = CALLDATALOAD vad3(0x4)
    0xad9: vad9(0x20) = CONST 
    0xadb: vadb(0x24) = ADD vad9(0x20), vad3(0x4)
    0xae0: vae0 = CALLDATALOAD vadb(0x24)
    0xae2: vae2(0x20) = CONST 
    0xae4: vae4(0x44) = ADD vae2(0x20), vadb(0x24)
    0xae9: vae9 = CALLDATALOAD vae4(0x44)
    0xaeb: vaeb(0x20) = CONST 
    0xaed: vaed(0x64) = ADD vaeb(0x20), vae4(0x44)
    0xaf0: vaf0 = ADD vad3(0x4), vae9
    0xaf2: vaf2 = CALLDATALOAD vaf0
    0xaf4: vaf4(0x20) = CONST 
    0xaf6: vaf6 = ADD vaf4(0x20), vaf0
    0xafa: vafa(0x20) = CONST 
    0xafc: vafc = MUL vafa(0x20), vaf2
    0xafd: vafd(0x20) = CONST 
    0xaff: vaff = ADD vafd(0x20), vafc
    0xb00: vb00(0x40) = CONST 
    0xb02: vb02 = MLOAD vb00(0x40)
    0xb05: vb05 = ADD vb02, vaff
    0xb06: vb06(0x40) = CONST 
    0xb08: MSTORE vb06(0x40), vb05
    0xb10: MSTORE vb02, vaf2
    0xb11: vb11(0x20) = CONST 
    0xb13: vb13 = ADD vb11(0x20), vb02
    0xb16: vb16(0x20) = CONST 
    0xb18: vb18 = MUL vb16(0x20), vaf2
    0xb1c: CALLDATACOPY vb13, vaf6, vb18
    0xb1e: vb1e = ADD vb13, vb18
    0xb29: vb29 = CALLDATALOAD vaed(0x64)
    0xb2a: vb2a = ISZERO vb29
    0xb2b: vb2b = ISZERO vb2a
    0xb2d: vb2d(0x20) = CONST 
    0xb2f: vb2f(0x84) = ADD vb2d(0x20), vaed(0x64)
    0xb34: vb34 = CALLDATALOAD vb2f(0x84)
    0xb35: vb35 = ISZERO vb34
    0xb36: vb36 = ISZERO vb35
    0xb38: vb38(0x20) = CONST 
    0xb3a: vb3a(0xa4) = ADD vb38(0x20), vb2f(0x84)
    0xb40: vb40(0x2553) = CONST 
    0xb43: JUMP vb40(0x2553), vb36, vb2b, vb02, vae0, vad7, vad0(0xb44)

    Begin block 0x2553B0xacf
    prev=[0xacf], succ=[0x25adB0xacf, 0x25fdB0xacf]
    =================================
    0x2554S0xacf: v2554Vacf(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab) = CONST 
    0x2569S0xacf: v2569Vacf(0x33840712) = CONST 
    0x256eS0xacf: v256eVacf(0x2) = CONST 
    0x2575S0xacf: v2575Vacf(0x40) = CONST 
    0x2577S0xacf: v2577Vacf = MLOAD v2575Vacf(0x40)
    0x2579S0xacf: v2579Vacf(0xffffffff) = CONST 
    0x257eS0xacf: v257eVacf(0x33840712) = AND v2579Vacf(0xffffffff), v2569Vacf(0x33840712)
    0x257fS0xacf: v257fVacf(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x259dS0xacf: v259dVacf(0x3384071200000000000000000000000000000000000000000000000000000000) = MUL v257fVacf(0x100000000000000000000000000000000000000000000000000000000), v257eVacf(0x33840712)
    0x259fS0xacf: MSTORE v2577Vacf, v259dVacf(0x3384071200000000000000000000000000000000000000000000000000000000)
    0x25a0S0xacf: v25a0Vacf(0x4) = CONST 
    0x25a2S0xacf: v25a2Vacf = ADD v25a0Vacf(0x4), v2577Vacf
    0x25a5S0xacf: v25a5Vacf(0x10) = CONST 
    0x25a8S0xacf: v25a8Vacf(0x0) = ISZERO v25a5Vacf(0x10)
    0x25a9S0xacf: v25a9Vacf(0x25fd) = CONST 
    0x25acS0xacf: JUMPI v25a9Vacf(0x25fd), v25a8Vacf(0x0)

    Begin block 0x25adB0xacf
    prev=[0x2553B0xacf], succ=[0x25b3B0xacf]
    =================================
    0x25adS0xacf: v25adVacf(0x20) = CONST 
    0x25afS0xacf: v25afVacf(0x200) = MUL v25adVacf(0x20), v25a5Vacf(0x10)
    0x25b1S0xacf: v25b1Vacf = ADD v25a2Vacf, v25afVacf(0x200)

    Begin block 0x25b3B0xacf
    prev=[0x25adB0xacf, 0x25b3B0xacf], succ=[0x25fdB0xacf, 0x25b3B0xacf]
    =================================
    0x25b3_0x0S0xacf: v25b3_0Vacf = PHI v25a2Vacf, v25f0Vacf
    0x25b3_0x1S0xacf: v25b3_1Vacf = PHI v256eVacf(0x2), v25f4Vacf
    0x25b5S0xacf: v25b5Vacf(0x0) = CONST 
    0x25b8S0xacf: v25b8Vacf = SLOAD v25b3_1Vacf
    0x25baS0xacf: v25baVacf(0x100) = CONST 
    0x25bdS0xacf: v25bdVacf(0x1) = EXP v25baVacf(0x100), v25b5Vacf(0x0)
    0x25bfS0xacf: v25bfVacf = DIV v25b8Vacf, v25bdVacf(0x1)
    0x25c0S0xacf: v25c0Vacf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25d5S0xacf: v25d5Vacf = AND v25c0Vacf(0xffffffffffffffffffffffffffffffffffffffff), v25bfVacf
    0x25d6S0xacf: v25d6Vacf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25ebS0xacf: v25ebVacf = AND v25d6Vacf(0xffffffffffffffffffffffffffffffffffffffff), v25d5Vacf
    0x25edS0xacf: MSTORE v25b3_0Vacf, v25ebVacf
    0x25eeS0xacf: v25eeVacf(0x20) = CONST 
    0x25f0S0xacf: v25f0Vacf = ADD v25eeVacf(0x20), v25b3_0Vacf
    0x25f2S0xacf: v25f2Vacf(0x1) = CONST 
    0x25f4S0xacf: v25f4Vacf = ADD v25f2Vacf(0x1), v25b3_1Vacf
    0x25f8S0xacf: v25f8Vacf = GT v25b1Vacf, v25f0Vacf
    0x25f9S0xacf: v25f9Vacf(0x25b3) = CONST 
    0x25fcS0xacf: JUMPI v25f9Vacf(0x25b3), v25f8Vacf

    Begin block 0x25fdB0xacf
    prev=[0x2553B0xacf, 0x25b3B0xacf], succ=[0x2643B0xacf]
    =================================
    0x25fd_0x2S0xacf: v25fd_2Vacf = PHI v25b1Vacf, v25a2Vacf
    0x2602S0xacf: MSTORE v25fd_2Vacf, vad7
    0x2603S0xacf: v2603Vacf(0x20) = CONST 
    0x2605S0xacf: v2605Vacf = ADD v2603Vacf(0x20), v25fd_2Vacf
    0x2608S0xacf: MSTORE v2605Vacf, vae0
    0x2609S0xacf: v2609Vacf(0x20) = CONST 
    0x260bS0xacf: v260bVacf = ADD v2609Vacf(0x20), v2605Vacf
    0x260dS0xacf: v260dVacf(0x20) = CONST 
    0x260fS0xacf: v260fVacf = ADD v260dVacf(0x20), v260bVacf
    0x2611S0xacf: v2611Vacf = ISZERO vb2b
    0x2612S0xacf: v2612Vacf = ISZERO v2611Vacf
    0x2613S0xacf: v2613Vacf = ISZERO v2612Vacf
    0x2614S0xacf: v2614Vacf = ISZERO v2613Vacf
    0x2616S0xacf: MSTORE v260fVacf, v2614Vacf
    0x2617S0xacf: v2617Vacf(0x20) = CONST 
    0x2619S0xacf: v2619Vacf = ADD v2617Vacf(0x20), v260fVacf
    0x261bS0xacf: v261bVacf = ISZERO vb36
    0x261cS0xacf: v261cVacf = ISZERO v261bVacf
    0x261dS0xacf: v261dVacf = ISZERO v261cVacf
    0x261eS0xacf: v261eVacf = ISZERO v261dVacf
    0x2620S0xacf: MSTORE v2619Vacf, v261eVacf
    0x2621S0xacf: v2621Vacf(0x20) = CONST 
    0x2623S0xacf: v2623Vacf = ADD v2621Vacf(0x20), v2619Vacf
    0x2626S0xacf: v2626Vacf = SUB v2623Vacf, v25a2Vacf
    0x2628S0xacf: MSTORE v260bVacf, v2626Vacf
    0x262cS0xacf: v262cVacf = MLOAD vb02
    0x262eS0xacf: MSTORE v2623Vacf, v262cVacf
    0x262fS0xacf: v262fVacf(0x20) = CONST 
    0x2631S0xacf: v2631Vacf = ADD v262fVacf(0x20), v2623Vacf
    0x2635S0xacf: v2635Vacf = MLOAD vb02
    0x2637S0xacf: v2637Vacf(0x20) = CONST 
    0x2639S0xacf: v2639Vacf = ADD v2637Vacf(0x20), vb02
    0x263bS0xacf: v263bVacf(0x20) = CONST 
    0x263dS0xacf: v263dVacf = MUL v263bVacf(0x20), v2635Vacf
    0x2641S0xacf: v2641Vacf(0x0) = CONST 

    Begin block 0x2643B0xacf
    prev=[0x25fdB0xacf, 0x264cB0xacf], succ=[0x265eB0xacf, 0x264cB0xacf]
    =================================
    0x2643_0x0S0xacf: v2643_0Vacf = PHI v2641Vacf(0x0), v2657Vacf
    0x2646S0xacf: v2646Vacf = LT v2643_0Vacf, v263dVacf
    0x2647S0xacf: v2647Vacf = ISZERO v2646Vacf
    0x2648S0xacf: v2648Vacf(0x265e) = CONST 
    0x264bS0xacf: JUMPI v2648Vacf(0x265e), v2647Vacf

    Begin block 0x265eB0xacf
    prev=[0x2643B0xacf], succ=[0x2681B0xacf, 0x2685B0xacf]
    =================================
    0x2665S0xacf: v2665Vacf = ADD v263dVacf, v2631Vacf
    0x266fS0xacf: v266fVacf(0x0) = CONST 
    0x2671S0xacf: v2671Vacf(0x40) = CONST 
    0x2673S0xacf: v2673Vacf = MLOAD v2671Vacf(0x40)
    0x2676S0xacf: v2676Vacf = SUB v2665Vacf, v2673Vacf
    0x267aS0xacf: v267aVacf = EXTCODESIZE v2554Vacf(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab)
    0x267bS0xacf: v267bVacf = ISZERO v267aVacf
    0x267cS0xacf: v267cVacf = ISZERO v267bVacf
    0x267dS0xacf: v267dVacf(0x2685) = CONST 
    0x2680S0xacf: JUMPI v267dVacf(0x2685), v267cVacf

    Begin block 0x2681B0xacf
    prev=[0x265eB0xacf], succ=[]
    =================================
    0x2681S0xacf: v2681Vacf(0x0) = CONST 
    0x2684S0xacf: REVERT v2681Vacf(0x0), v2681Vacf(0x0)

    Begin block 0x2685B0xacf
    prev=[0x265eB0xacf], succ=[0x2692B0xacf, 0x2696B0xacf]
    =================================
    0x2686S0xacf: v2686Vacf(0x2c6) = CONST 
    0x2689S0xacf: v2689Vacf = GAS 
    0x268aS0xacf: v268aVacf = SUB v2689Vacf, v2686Vacf(0x2c6)
    0x268bS0xacf: v268bVacf = DELEGATECALL v268aVacf, v2554Vacf(0xa9c81661c85e3b09ac5d04683cb344a13dd2a5ab), v2673Vacf, v2676Vacf, v2673Vacf, v266fVacf(0x0)
    0x268cS0xacf: v268cVacf = ISZERO v268bVacf
    0x268dS0xacf: v268dVacf = ISZERO v268cVacf
    0x268eS0xacf: v268eVacf(0x2696) = CONST 
    0x2691S0xacf: JUMPI v268eVacf(0x2696), v268dVacf

    Begin block 0x2692B0xacf
    prev=[0x2685B0xacf], succ=[]
    =================================
    0x2692S0xacf: v2692Vacf(0x0) = CONST 
    0x2695S0xacf: REVERT v2692Vacf(0x0), v2692Vacf(0x0)

    Begin block 0x2696B0xacf
    prev=[0x2685B0xacf], succ=[0xb44]
    =================================
    0x269fS0xacf: JUMP vad0(0xb44)

    Begin block 0xb44
    prev=[0x2696B0xacf], succ=[]
    =================================
    0xb45: STOP 

    Begin block 0x264cB0xacf
    prev=[0x2643B0xacf], succ=[0x2643B0xacf]
    =================================
    0x264c_0x0S0xacf: v264c_0Vacf = PHI v2641Vacf(0x0), v2657Vacf
    0x264eS0xacf: v264eVacf = ADD v2639Vacf, v264c_0Vacf
    0x264fS0xacf: v264fVacf = MLOAD v264eVacf
    0x2652S0xacf: v2652Vacf = ADD v2631Vacf, v264c_0Vacf
    0x2653S0xacf: MSTORE v2652Vacf, v264fVacf
    0x2654S0xacf: v2654Vacf(0x20) = CONST 
    0x2657S0xacf: v2657Vacf = ADD v264c_0Vacf, v2654Vacf(0x20)
    0x265aS0xacf: v265aVacf(0x2643) = CONST 
    0x265dS0xacf: JUMP v265aVacf(0x2643)

}

function purchase(uint256)() public {
    Begin block 0xb46
    prev=[], succ=[0x26a0B0xb46]
    =================================
    0xb47: vb47(0xb5c) = CONST 
    0xb4a: vb4a(0x4) = CONST 
    0xb4e: vb4e = CALLDATALOAD vb4a(0x4)
    0xb50: vb50(0x20) = CONST 
    0xb52: vb52(0x24) = ADD vb50(0x20), vb4a(0x4)
    0xb58: vb58(0x26a0) = CONST 
    0xb5b: JUMP vb58(0x26a0), vb4e, vb47(0xb5c)

    Begin block 0x26a0B0xb46
    prev=[0xb46], succ=[0x26c9B0xb46, 0x26b8B0xb46]
    =================================
    0x26a1S0xb46: v26a1Vb46(0x12) = CONST 
    0x26a3S0xb46: v26a3Vb46(0x0) = CONST 
    0x26a6S0xb46: v26a6Vb46 = SLOAD v26a1Vb46(0x12)
    0x26a8S0xb46: v26a8Vb46(0x100) = CONST 
    0x26abS0xb46: v26abVb46(0x1) = EXP v26a8Vb46(0x100), v26a3Vb46(0x0)
    0x26adS0xb46: v26adVb46 = DIV v26a6Vb46, v26abVb46(0x1)
    0x26aeS0xb46: v26aeVb46(0xff) = CONST 
    0x26b0S0xb46: v26b0Vb46 = AND v26aeVb46(0xff), v26adVb46
    0x26b1S0xb46: v26b1Vb46 = ISZERO v26b0Vb46
    0x26b3S0xb46: v26b3Vb46 = ISZERO v26b1Vb46
    0x26b4S0xb46: v26b4Vb46(0x26c9) = CONST 
    0x26b7S0xb46: JUMPI v26b4Vb46(0x26c9), v26b3Vb46

    Begin block 0x26c9B0xb46
    prev=[0x26a0B0xb46, 0x26b8B0xb46], succ=[0x26d0B0xb46, 0x26d4B0xb46]
    =================================
    0x26c9_0x0S0xb46: v26c9_0Vb46 = PHI v26b1Vb46, v26c8Vb46
    0x26caS0xb46: v26caVb46 = ISZERO v26c9_0Vb46
    0x26cbS0xb46: v26cbVb46 = ISZERO v26caVb46
    0x26ccS0xb46: v26ccVb46(0x26d4) = CONST 
    0x26cfS0xb46: JUMPI v26ccVb46(0x26d4), v26cbVb46

    Begin block 0x26d0B0xb46
    prev=[0x26c9B0xb46], succ=[]
    =================================
    0x26d0S0xb46: v26d0Vb46(0x0) = CONST 
    0x26d3S0xb46: REVERT v26d0Vb46(0x0), v26d0Vb46(0x0)

    Begin block 0x26d4B0xb46
    prev=[0x26c9B0xb46], succ=[0x272aB0xb46, 0x277aB0xb46]
    =================================
    0x26d5S0xb46: v26d5Vb46(0xf284e7b147b72200c48efd4d513309b9734a8993) = CONST 
    0x26eaS0xb46: v26eaVb46(0x1fc7d658) = CONST 
    0x26efS0xb46: v26efVb46(0x2) = CONST 
    0x26f2S0xb46: v26f2Vb46(0x40) = CONST 
    0x26f4S0xb46: v26f4Vb46 = MLOAD v26f2Vb46(0x40)
    0x26f6S0xb46: v26f6Vb46(0xffffffff) = CONST 
    0x26fbS0xb46: v26fbVb46(0x1fc7d658) = AND v26f6Vb46(0xffffffff), v26eaVb46(0x1fc7d658)
    0x26fcS0xb46: v26fcVb46(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x271aS0xb46: v271aVb46(0x1fc7d65800000000000000000000000000000000000000000000000000000000) = MUL v26fcVb46(0x100000000000000000000000000000000000000000000000000000000), v26fbVb46(0x1fc7d658)
    0x271cS0xb46: MSTORE v26f4Vb46, v271aVb46(0x1fc7d65800000000000000000000000000000000000000000000000000000000)
    0x271dS0xb46: v271dVb46(0x4) = CONST 
    0x271fS0xb46: v271fVb46 = ADD v271dVb46(0x4), v26f4Vb46
    0x2722S0xb46: v2722Vb46(0x10) = CONST 
    0x2725S0xb46: v2725Vb46(0x0) = ISZERO v2722Vb46(0x10)
    0x2726S0xb46: v2726Vb46(0x277a) = CONST 
    0x2729S0xb46: JUMPI v2726Vb46(0x277a), v2725Vb46(0x0)

    Begin block 0x272aB0xb46
    prev=[0x26d4B0xb46], succ=[0x2730B0xb46]
    =================================
    0x272aS0xb46: v272aVb46(0x20) = CONST 
    0x272cS0xb46: v272cVb46(0x200) = MUL v272aVb46(0x20), v2722Vb46(0x10)
    0x272eS0xb46: v272eVb46 = ADD v271fVb46, v272cVb46(0x200)

    Begin block 0x2730B0xb46
    prev=[0x272aB0xb46, 0x2730B0xb46], succ=[0x277aB0xb46, 0x2730B0xb46]
    =================================
    0x2730_0x0S0xb46: v2730_0Vb46 = PHI v271fVb46, v276dVb46
    0x2730_0x1S0xb46: v2730_1Vb46 = PHI v26efVb46(0x2), v2771Vb46
    0x2732S0xb46: v2732Vb46(0x0) = CONST 
    0x2735S0xb46: v2735Vb46 = SLOAD v2730_1Vb46
    0x2737S0xb46: v2737Vb46(0x100) = CONST 
    0x273aS0xb46: v273aVb46(0x1) = EXP v2737Vb46(0x100), v2732Vb46(0x0)
    0x273cS0xb46: v273cVb46 = DIV v2735Vb46, v273aVb46(0x1)
    0x273dS0xb46: v273dVb46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2752S0xb46: v2752Vb46 = AND v273dVb46(0xffffffffffffffffffffffffffffffffffffffff), v273cVb46
    0x2753S0xb46: v2753Vb46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2768S0xb46: v2768Vb46 = AND v2753Vb46(0xffffffffffffffffffffffffffffffffffffffff), v2752Vb46
    0x276aS0xb46: MSTORE v2730_0Vb46, v2768Vb46
    0x276bS0xb46: v276bVb46(0x20) = CONST 
    0x276dS0xb46: v276dVb46 = ADD v276bVb46(0x20), v2730_0Vb46
    0x276fS0xb46: v276fVb46(0x1) = CONST 
    0x2771S0xb46: v2771Vb46 = ADD v276fVb46(0x1), v2730_1Vb46
    0x2775S0xb46: v2775Vb46 = GT v272eVb46, v276dVb46
    0x2776S0xb46: v2776Vb46(0x2730) = CONST 
    0x2779S0xb46: JUMPI v2776Vb46(0x2730), v2775Vb46

    Begin block 0x277aB0xb46
    prev=[0x26d4B0xb46, 0x2730B0xb46], succ=[0x2799B0xb46, 0x279dB0xb46]
    =================================
    0x277a_0x2S0xb46: v277a_2Vb46 = PHI v272eVb46, v271fVb46
    0x277fS0xb46: MSTORE v277a_2Vb46, vb4e
    0x2780S0xb46: v2780Vb46(0x20) = CONST 
    0x2782S0xb46: v2782Vb46 = ADD v2780Vb46(0x20), v277a_2Vb46
    0x2787S0xb46: v2787Vb46(0x0) = CONST 
    0x2789S0xb46: v2789Vb46(0x40) = CONST 
    0x278bS0xb46: v278bVb46 = MLOAD v2789Vb46(0x40)
    0x278eS0xb46: v278eVb46 = SUB v2782Vb46, v278bVb46
    0x2792S0xb46: v2792Vb46 = EXTCODESIZE v26d5Vb46(0xf284e7b147b72200c48efd4d513309b9734a8993)
    0x2793S0xb46: v2793Vb46 = ISZERO v2792Vb46
    0x2794S0xb46: v2794Vb46 = ISZERO v2793Vb46
    0x2795S0xb46: v2795Vb46(0x279d) = CONST 
    0x2798S0xb46: JUMPI v2795Vb46(0x279d), v2794Vb46

    Begin block 0x2799B0xb46
    prev=[0x277aB0xb46], succ=[]
    =================================
    0x2799S0xb46: v2799Vb46(0x0) = CONST 
    0x279cS0xb46: REVERT v2799Vb46(0x0), v2799Vb46(0x0)

    Begin block 0x279dB0xb46
    prev=[0x277aB0xb46], succ=[0x27aaB0xb46, 0x27aeB0xb46]
    =================================
    0x279eS0xb46: v279eVb46(0x2c6) = CONST 
    0x27a1S0xb46: v27a1Vb46 = GAS 
    0x27a2S0xb46: v27a2Vb46 = SUB v27a1Vb46, v279eVb46(0x2c6)
    0x27a3S0xb46: v27a3Vb46 = DELEGATECALL v27a2Vb46, v26d5Vb46(0xf284e7b147b72200c48efd4d513309b9734a8993), v278bVb46, v278eVb46, v278bVb46, v2787Vb46(0x0)
    0x27a4S0xb46: v27a4Vb46 = ISZERO v27a3Vb46
    0x27a5S0xb46: v27a5Vb46 = ISZERO v27a4Vb46
    0x27a6S0xb46: v27a6Vb46(0x27ae) = CONST 
    0x27a9S0xb46: JUMPI v27a6Vb46(0x27ae), v27a5Vb46

    Begin block 0x27aaB0xb46
    prev=[0x279dB0xb46], succ=[]
    =================================
    0x27aaS0xb46: v27aaVb46(0x0) = CONST 
    0x27adS0xb46: REVERT v27aaVb46(0x0), v27aaVb46(0x0)

    Begin block 0x27aeB0xb46
    prev=[0x279dB0xb46], succ=[0xb5c]
    =================================
    0x27b3S0xb46: JUMP vb47(0xb5c)

    Begin block 0xb5c
    prev=[0x27aeB0xb46], succ=[]
    =================================
    0xb5d: STOP 

    Begin block 0x26b8B0xb46
    prev=[0x26a0B0xb46], succ=[0x26c9B0xb46]
    =================================
    0x26b9S0xb46: v26b9Vb46(0x12) = CONST 
    0x26bbS0xb46: v26bbVb46(0x1) = CONST 
    0x26beS0xb46: v26beVb46 = SLOAD v26b9Vb46(0x12)
    0x26c0S0xb46: v26c0Vb46(0x100) = CONST 
    0x26c3S0xb46: v26c3Vb46(0x100) = EXP v26c0Vb46(0x100), v26bbVb46(0x1)
    0x26c5S0xb46: v26c5Vb46 = DIV v26beVb46, v26c3Vb46(0x100)
    0x26c6S0xb46: v26c6Vb46(0xff) = CONST 
    0x26c8S0xb46: v26c8Vb46 = AND v26c6Vb46(0xff), v26c5Vb46

}

function setContracts(address[16])() public {
    Begin block 0xb5e
    prev=[], succ=[0xb65, 0xb69]
    =================================
    0xb5f: vb5f = CALLVALUE 
    0xb60: vb60 = ISZERO vb5f
    0xb61: vb61(0xb69) = CONST 
    0xb64: JUMPI vb61(0xb69), vb60

    Begin block 0xb65
    prev=[0xb5e], succ=[]
    =================================
    0xb65: vb65(0x0) = CONST 
    0xb68: REVERT vb65(0x0), vb65(0x0)

    Begin block 0xb69
    prev=[0xb5e], succ=[0x27b4B0xb69]
    =================================
    0xb6a: vb6a(0xb7e) = CONST 
    0xb6d: vb6d(0x4) = CONST 
    0xb71: vb71(0x200) = CONST 
    0xb74: vb74(0x204) = ADD vb71(0x200), vb6d(0x4)
    0xb7a: vb7a(0x27b4) = CONST 
    0xb7d: JUMP vb7a(0x27b4), vb6d(0x4), vb6a(0xb7e)

    Begin block 0x27b4B0xb69
    prev=[0xb69], succ=[0x280bB0xb69, 0x280fB0xb69]
    =================================
    0x27b5S0xb69: v27b5Vb69(0x0) = CONST 
    0x27b9S0xb69: v27b9Vb69 = SLOAD v27b5Vb69(0x0)
    0x27bbS0xb69: v27bbVb69(0x100) = CONST 
    0x27beS0xb69: v27beVb69(0x1) = EXP v27bbVb69(0x100), v27b5Vb69(0x0)
    0x27c0S0xb69: v27c0Vb69 = DIV v27b9Vb69, v27beVb69(0x1)
    0x27c1S0xb69: v27c1Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27d6S0xb69: v27d6Vb69 = AND v27c1Vb69(0xffffffffffffffffffffffffffffffffffffffff), v27c0Vb69
    0x27d7S0xb69: v27d7Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27ecS0xb69: v27ecVb69 = AND v27d7Vb69(0xffffffffffffffffffffffffffffffffffffffff), v27d6Vb69
    0x27edS0xb69: v27edVb69 = CALLER 
    0x27eeS0xb69: v27eeVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2803S0xb69: v2803Vb69 = AND v27eeVb69(0xffffffffffffffffffffffffffffffffffffffff), v27edVb69
    0x2804S0xb69: v2804Vb69 = EQ v2803Vb69, v27ecVb69
    0x2805S0xb69: v2805Vb69 = ISZERO v2804Vb69
    0x2806S0xb69: v2806Vb69 = ISZERO v2805Vb69
    0x2807S0xb69: v2807Vb69(0x280f) = CONST 
    0x280aS0xb69: JUMPI v2807Vb69(0x280f), v2806Vb69

    Begin block 0x280bB0xb69
    prev=[0x27b4B0xb69], succ=[]
    =================================
    0x280bS0xb69: v280bVb69(0x0) = CONST 
    0x280eS0xb69: REVERT v280bVb69(0x0), v280bVb69(0x0)

    Begin block 0x280fB0xb69
    prev=[0x27b4B0xb69], succ=[0x2a0eB0x280fB0xb69]
    =================================
    0x2811S0xb69: v2811Vb69(0x2) = CONST 
    0x2814S0xb69: v2814Vb69(0x10) = CONST 
    0x2816S0xb69: v2816Vb69(0x2820) = CONST 
    0x281cS0xb69: v281cVb69(0x2a0e) = CONST 
    0x281fS0xb69: JUMP v281cVb69(0x2a0e)

    Begin block 0x2a0eB0x280fB0xb69
    prev=[0x280fB0xb69], succ=[0x2a90B0x280fB0xb69, 0x2a1bB0x280fB0xb69]
    =================================
    0x2a10S0x280fS0xb69: v2a10V280fVb69(0x10) = CONST 
    0x2a13S0x280fS0xb69: v2a13V280fVb69(0x12) = ADD v2811Vb69(0x2), v2a10V280fVb69(0x10)
    0x2a16S0x280fS0xb69: v2a16V280fVb69 = ISZERO v2814Vb69(0x10)
    0x2a17S0x280fS0xb69: v2a17V280fVb69(0x2a90) = CONST 
    0x2a1aS0x280fS0xb69: JUMPI v2a17V280fVb69(0x2a90), v2a16V280fVb69

    Begin block 0x2a90B0x280fB0xb69
    prev=[0x2a0eB0x280fB0xb69, 0x2a8fB0x280fB0xb69], succ=[0x2aa1B0x2a90B0x280fB0xb69]
    =================================
    0x2a90_0x1S0x280fS0xb69: v2a90_1V280fVb69 = PHI v2811Vb69(0x2), v2a89V280fVb69
    0x2a94S0x280fS0xb69: v2a94V280fVb69(0x2a9d) = CONST 
    0x2a99S0x280fS0xb69: v2a99V280fVb69(0x2aa1) = CONST 
    0x2a9cS0x280fS0xb69: JUMP v2a99V280fVb69(0x2aa1)

    Begin block 0x2aa1B0x2a90B0x280fB0xb69
    prev=[0x2a90B0x280fB0xb69], succ=[0x2aa7B0x2a90B0x280fB0xb69]
    =================================
    0x2aa2S0x2a90S0x280fS0xb69: v2aa2V2a90V280fVb69(0x2ae1) = CONST 

    Begin block 0x2aa7B0x2a90B0x280fB0xb69
    prev=[0x2ab0B0x2a90B0x280fB0xb69, 0x2aa1B0x2a90B0x280fB0xb69], succ=[0x2ab0B0x2a90B0x280fB0xb69, 0x2addB0x2a90B0x280fB0xb69]
    =================================
    0x2aa7_0x0S0x2a90S0x280fS0xb69: v2aa7_0V2a90V280fVb69 = PHI v2a90_1V280fVb69, v2ad8V2a90V280fVb69
    0x2aaaS0x2a90S0x280fS0xb69: v2aaaV2a90V280fVb69 = GT v2a13V280fVb69(0x12), v2aa7_0V2a90V280fVb69
    0x2aabS0x2a90S0x280fS0xb69: v2aabV2a90V280fVb69 = ISZERO v2aaaV2a90V280fVb69
    0x2aacS0x2a90S0x280fS0xb69: v2aacV2a90V280fVb69(0x2add) = CONST 
    0x2aafS0x2a90S0x280fS0xb69: JUMPI v2aacV2a90V280fVb69(0x2add), v2aabV2a90V280fVb69

    Begin block 0x2ab0B0x2a90B0x280fB0xb69
    prev=[0x2aa7B0x2a90B0x280fB0xb69], succ=[0x2aa7B0x2a90B0x280fB0xb69]
    =================================
    0x2ab0S0x2a90S0x280fS0xb69: v2ab0V2a90V280fVb69(0x0) = CONST 
    0x2ab0_0x0S0x2a90S0x280fS0xb69: v2ab0_0V2a90V280fVb69 = PHI v2a90_1V280fVb69, v2ad8V2a90V280fVb69
    0x2ab4S0x2a90S0x280fS0xb69: v2ab4V2a90V280fVb69(0x100) = CONST 
    0x2ab7S0x2a90S0x280fS0xb69: v2ab7V2a90V280fVb69(0x1) = EXP v2ab4V2a90V280fVb69(0x100), v2ab0V2a90V280fVb69(0x0)
    0x2ab9S0x2a90S0x280fS0xb69: v2ab9V2a90V280fVb69 = SLOAD v2ab0_0V2a90V280fVb69
    0x2abbS0x2a90S0x280fS0xb69: v2abbV2a90V280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ad0S0x2a90S0x280fS0xb69: v2ad0V2a90V280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2abbV2a90V280fVb69(0xffffffffffffffffffffffffffffffffffffffff), v2ab7V2a90V280fVb69(0x1)
    0x2ad1S0x2a90S0x280fS0xb69: v2ad1V2a90V280fVb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2ad0V2a90V280fVb69(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ad2S0x2a90S0x280fS0xb69: v2ad2V2a90V280fVb69 = AND v2ad1V2a90V280fVb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2ab9V2a90V280fVb69
    0x2ad4S0x2a90S0x280fS0xb69: SSTORE v2ab0_0V2a90V280fVb69, v2ad2V2a90V280fVb69
    0x2ad6S0x2a90S0x280fS0xb69: v2ad6V2a90V280fVb69(0x1) = CONST 
    0x2ad8S0x2a90S0x280fS0xb69: v2ad8V2a90V280fVb69 = ADD v2ad6V2a90V280fVb69(0x1), v2ab0_0V2a90V280fVb69
    0x2ad9S0x2a90S0x280fS0xb69: v2ad9V2a90V280fVb69(0x2aa7) = CONST 
    0x2adcS0x2a90S0x280fS0xb69: JUMP v2ad9V2a90V280fVb69(0x2aa7)

    Begin block 0x2addB0x2a90B0x280fB0xb69
    prev=[0x2aa7B0x2a90B0x280fB0xb69], succ=[0x2ae1B0x2a90B0x280fB0xb69]
    =================================
    0x2ae0S0x2a90S0x280fS0xb69: JUMP v2aa2V2a90V280fVb69(0x2ae1)

    Begin block 0x2ae1B0x2a90B0x280fB0xb69
    prev=[0x2addB0x2a90B0x280fB0xb69], succ=[0x2a9dB0x280fB0xb69]
    =================================
    0x2ae3S0x2a90S0x280fS0xb69: JUMP v2a94V280fVb69(0x2a9d)

    Begin block 0x2a9dB0x280fB0xb69
    prev=[0x2ae1B0x2a90B0x280fB0xb69], succ=[0x2820B0xb69]
    =================================
    0x2aa0S0x280fS0xb69: JUMP v2816Vb69(0x2820)

    Begin block 0x2820B0xb69
    prev=[0x2a9dB0x280fB0xb69], succ=[0xb7e]
    =================================
    0x2823S0xb69: JUMP vb6a(0xb7e)

    Begin block 0xb7e
    prev=[0x2820B0xb69], succ=[]
    =================================
    0xb7f: STOP 

    Begin block 0x2a1bB0x280fB0xb69
    prev=[0x2a0eB0x280fB0xb69], succ=[0x2a21B0x280fB0xb69]
    =================================
    0x2a1cS0x280fS0xb69: v2a1cV280fVb69(0x20) = CONST 
    0x2a1eS0x280fS0xb69: v2a1eV280fVb69(0x200) = MUL v2a1cV280fVb69(0x20), v2814Vb69(0x10)
    0x2a20S0x280fS0xb69: v2a20V280fVb69(0x204) = ADD vb6d(0x4), v2a1eV280fVb69(0x200)

    Begin block 0x2a21B0x280fB0xb69
    prev=[0x2a1bB0x280fB0xb69, 0x2a2aB0x280fB0xb69], succ=[0x2a2aB0x280fB0xb69, 0x2a8fB0x280fB0xb69]
    =================================
    0x2a21_0x2S0x280fS0xb69: v2a21_2V280fVb69 = PHI vb6d(0x4), v2a84V280fVb69
    0x2a24S0x280fS0xb69: v2a24V280fVb69 = GT v2a20V280fVb69(0x204), v2a21_2V280fVb69
    0x2a25S0x280fS0xb69: v2a25V280fVb69 = ISZERO v2a24V280fVb69
    0x2a26S0x280fS0xb69: v2a26V280fVb69(0x2a8f) = CONST 
    0x2a29S0x280fS0xb69: JUMPI v2a26V280fVb69(0x2a8f), v2a25V280fVb69

    Begin block 0x2a2aB0x280fB0xb69
    prev=[0x2a21B0x280fB0xb69], succ=[0x2a21B0x280fB0xb69]
    =================================
    0x2a2a_0x1S0x280fS0xb69: v2a2a_1V280fVb69 = PHI v2811Vb69(0x2), v2a89V280fVb69
    0x2a2a_0x2S0x280fS0xb69: v2a2a_2V280fVb69 = PHI vb6d(0x4), v2a84V280fVb69
    0x2a2bS0x280fS0xb69: v2a2bV280fVb69 = CALLDATALOAD v2a2a_2V280fVb69
    0x2a2cS0x280fS0xb69: v2a2cV280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a41S0x280fS0xb69: v2a41V280fVb69 = AND v2a2cV280fVb69(0xffffffffffffffffffffffffffffffffffffffff), v2a2bV280fVb69
    0x2a43S0x280fS0xb69: v2a43V280fVb69(0x0) = CONST 
    0x2a45S0x280fS0xb69: v2a45V280fVb69(0x100) = CONST 
    0x2a48S0x280fS0xb69: v2a48V280fVb69(0x1) = EXP v2a45V280fVb69(0x100), v2a43V280fVb69(0x0)
    0x2a4aS0x280fS0xb69: v2a4aV280fVb69 = SLOAD v2a2a_1V280fVb69
    0x2a4cS0x280fS0xb69: v2a4cV280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a61S0x280fS0xb69: v2a61V280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2a4cV280fVb69(0xffffffffffffffffffffffffffffffffffffffff), v2a48V280fVb69(0x1)
    0x2a62S0x280fS0xb69: v2a62V280fVb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2a61V280fVb69(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a63S0x280fS0xb69: v2a63V280fVb69 = AND v2a62V280fVb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2a4aV280fVb69
    0x2a66S0x280fS0xb69: v2a66V280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a7bS0x280fS0xb69: v2a7bV280fVb69 = AND v2a66V280fVb69(0xffffffffffffffffffffffffffffffffffffffff), v2a41V280fVb69
    0x2a7cS0x280fS0xb69: v2a7cV280fVb69 = MUL v2a7bV280fVb69, v2a48V280fVb69(0x1)
    0x2a7dS0x280fS0xb69: v2a7dV280fVb69 = OR v2a7cV280fVb69, v2a63V280fVb69
    0x2a7fS0x280fS0xb69: SSTORE v2a2a_1V280fVb69, v2a7dV280fVb69
    0x2a82S0x280fS0xb69: v2a82V280fVb69(0x20) = CONST 
    0x2a84S0x280fS0xb69: v2a84V280fVb69 = ADD v2a82V280fVb69(0x20), v2a2a_2V280fVb69
    0x2a87S0x280fS0xb69: v2a87V280fVb69(0x1) = CONST 
    0x2a89S0x280fS0xb69: v2a89V280fVb69 = ADD v2a87V280fVb69(0x1), v2a2a_1V280fVb69
    0x2a8bS0x280fS0xb69: v2a8bV280fVb69(0x2a21) = CONST 
    0x2a8eS0x280fS0xb69: JUMP v2a8bV280fVb69(0x2a21)

    Begin block 0x2a8fB0x280fB0xb69
    prev=[0x2a21B0x280fB0xb69], succ=[0x2a90B0x280fB0xb69]
    =================================

}

function setupRegion(uint256,uint256,uint256[],bool,uint8[128])() public {
    Begin block 0xb80
    prev=[], succ=[0xb87, 0xb8b]
    =================================
    0xb81: vb81 = CALLVALUE 
    0xb82: vb82 = ISZERO vb81
    0xb83: vb83(0xb8b) = CONST 
    0xb86: JUMPI vb83(0xb8b), vb82

    Begin block 0xb87
    prev=[0xb80], succ=[]
    =================================
    0xb87: vb87(0x0) = CONST 
    0xb8a: REVERT vb87(0x0), vb87(0x0)

    Begin block 0xb8b
    prev=[0xb80], succ=[0x2824B0xb8b]
    =================================
    0xb8c: vb8c(0xc22) = CONST 
    0xb8f: vb8f(0x4) = CONST 
    0xb93: vb93 = CALLDATALOAD vb8f(0x4)
    0xb95: vb95(0x20) = CONST 
    0xb97: vb97(0x24) = ADD vb95(0x20), vb8f(0x4)
    0xb9c: vb9c = CALLDATALOAD vb97(0x24)
    0xb9e: vb9e(0x20) = CONST 
    0xba0: vba0(0x44) = ADD vb9e(0x20), vb97(0x24)
    0xba5: vba5 = CALLDATALOAD vba0(0x44)
    0xba7: vba7(0x20) = CONST 
    0xba9: vba9(0x64) = ADD vba7(0x20), vba0(0x44)
    0xbac: vbac = ADD vb8f(0x4), vba5
    0xbae: vbae = CALLDATALOAD vbac
    0xbb0: vbb0(0x20) = CONST 
    0xbb2: vbb2 = ADD vbb0(0x20), vbac
    0xbb6: vbb6(0x20) = CONST 
    0xbb8: vbb8 = MUL vbb6(0x20), vbae
    0xbb9: vbb9(0x20) = CONST 
    0xbbb: vbbb = ADD vbb9(0x20), vbb8
    0xbbc: vbbc(0x40) = CONST 
    0xbbe: vbbe = MLOAD vbbc(0x40)
    0xbc1: vbc1 = ADD vbbe, vbbb
    0xbc2: vbc2(0x40) = CONST 
    0xbc4: MSTORE vbc2(0x40), vbc1
    0xbcc: MSTORE vbbe, vbae
    0xbcd: vbcd(0x20) = CONST 
    0xbcf: vbcf = ADD vbcd(0x20), vbbe
    0xbd2: vbd2(0x20) = CONST 
    0xbd4: vbd4 = MUL vbd2(0x20), vbae
    0xbd8: CALLDATACOPY vbcf, vbb2, vbd4
    0xbda: vbda = ADD vbcf, vbd4
    0xbe5: vbe5 = CALLDATALOAD vba9(0x64)
    0xbe6: vbe6 = ISZERO vbe5
    0xbe7: vbe7 = ISZERO vbe6
    0xbe9: vbe9(0x20) = CONST 
    0xbeb: vbeb(0x84) = ADD vbe9(0x20), vba9(0x64)
    0xbf0: vbf0(0x1000) = CONST 
    0xbf3: vbf3(0x1084) = ADD vbf0(0x1000), vbeb(0x84)
    0xbf5: vbf5(0x80) = CONST 
    0xbf8: vbf8(0x20) = CONST 
    0xbfa: vbfa(0x1000) = MUL vbf8(0x20), vbf5(0x80)
    0xbfb: vbfb(0x40) = CONST 
    0xbfd: vbfd = MLOAD vbfb(0x40)
    0xc00: vc00 = ADD vbfd, vbfa(0x1000)
    0xc01: vc01(0x40) = CONST 
    0xc03: MSTORE vc01(0x40), vc00
    0xc09: vc09(0x80) = CONST 
    0xc0b: vc0b(0x20) = CONST 
    0xc0d: vc0d(0x1000) = MUL vc0b(0x20), vc09(0x80)
    0xc11: CALLDATACOPY vbfd, vbeb(0x84), vc0d(0x1000)
    0xc13: vc13 = ADD vbfd, vc0d(0x1000)
    0xc1e: vc1e(0x2824) = CONST 
    0xc21: JUMP vc1e(0x2824), vbfd, vbe7, vbbe, vb9c, vb93, vb8c(0xc22)

    Begin block 0x2824B0xb8b
    prev=[0xb8b], succ=[0x284dB0xb8b, 0x283cB0xb8b]
    =================================
    0x2825S0xb8b: v2825Vb8b(0x12) = CONST 
    0x2827S0xb8b: v2827Vb8b(0x0) = CONST 
    0x282aS0xb8b: v282aVb8b = SLOAD v2825Vb8b(0x12)
    0x282cS0xb8b: v282cVb8b(0x100) = CONST 
    0x282fS0xb8b: v282fVb8b(0x1) = EXP v282cVb8b(0x100), v2827Vb8b(0x0)
    0x2831S0xb8b: v2831Vb8b = DIV v282aVb8b, v282fVb8b(0x1)
    0x2832S0xb8b: v2832Vb8b(0xff) = CONST 
    0x2834S0xb8b: v2834Vb8b = AND v2832Vb8b(0xff), v2831Vb8b
    0x2835S0xb8b: v2835Vb8b = ISZERO v2834Vb8b
    0x2837S0xb8b: v2837Vb8b = ISZERO v2835Vb8b
    0x2838S0xb8b: v2838Vb8b(0x284d) = CONST 
    0x283bS0xb8b: JUMPI v2838Vb8b(0x284d), v2837Vb8b

    Begin block 0x284dB0xb8b
    prev=[0x2824B0xb8b, 0x283cB0xb8b], succ=[0x2854B0xb8b, 0x2858B0xb8b]
    =================================
    0x284d_0x0S0xb8b: v284d_0Vb8b = PHI v2835Vb8b, v284cVb8b
    0x284eS0xb8b: v284eVb8b = ISZERO v284d_0Vb8b
    0x284fS0xb8b: v284fVb8b = ISZERO v284eVb8b
    0x2850S0xb8b: v2850Vb8b(0x2858) = CONST 
    0x2853S0xb8b: JUMPI v2850Vb8b(0x2858), v284fVb8b

    Begin block 0x2854B0xb8b
    prev=[0x284dB0xb8b], succ=[]
    =================================
    0x2854S0xb8b: v2854Vb8b(0x0) = CONST 
    0x2857S0xb8b: REVERT v2854Vb8b(0x0), v2854Vb8b(0x0)

    Begin block 0x2858B0xb8b
    prev=[0x284dB0xb8b], succ=[0x28b2B0xb8b, 0x2902B0xb8b]
    =================================
    0x2859S0xb8b: v2859Vb8b(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb) = CONST 
    0x286eS0xb8b: v286eVb8b(0xbad4481) = CONST 
    0x2873S0xb8b: v2873Vb8b(0x2) = CONST 
    0x287aS0xb8b: v287aVb8b(0x40) = CONST 
    0x287cS0xb8b: v287cVb8b = MLOAD v287aVb8b(0x40)
    0x287eS0xb8b: v287eVb8b(0xffffffff) = CONST 
    0x2883S0xb8b: v2883Vb8b(0xbad4481) = AND v287eVb8b(0xffffffff), v286eVb8b(0xbad4481)
    0x2884S0xb8b: v2884Vb8b(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x28a2S0xb8b: v28a2Vb8b(0xbad448100000000000000000000000000000000000000000000000000000000) = MUL v2884Vb8b(0x100000000000000000000000000000000000000000000000000000000), v2883Vb8b(0xbad4481)
    0x28a4S0xb8b: MSTORE v287cVb8b, v28a2Vb8b(0xbad448100000000000000000000000000000000000000000000000000000000)
    0x28a5S0xb8b: v28a5Vb8b(0x4) = CONST 
    0x28a7S0xb8b: v28a7Vb8b = ADD v28a5Vb8b(0x4), v287cVb8b
    0x28aaS0xb8b: v28aaVb8b(0x10) = CONST 
    0x28adS0xb8b: v28adVb8b(0x0) = ISZERO v28aaVb8b(0x10)
    0x28aeS0xb8b: v28aeVb8b(0x2902) = CONST 
    0x28b1S0xb8b: JUMPI v28aeVb8b(0x2902), v28adVb8b(0x0)

    Begin block 0x28b2B0xb8b
    prev=[0x2858B0xb8b], succ=[0x28b8B0xb8b]
    =================================
    0x28b2S0xb8b: v28b2Vb8b(0x20) = CONST 
    0x28b4S0xb8b: v28b4Vb8b(0x200) = MUL v28b2Vb8b(0x20), v28aaVb8b(0x10)
    0x28b6S0xb8b: v28b6Vb8b = ADD v28a7Vb8b, v28b4Vb8b(0x200)

    Begin block 0x28b8B0xb8b
    prev=[0x28b2B0xb8b, 0x28b8B0xb8b], succ=[0x2902B0xb8b, 0x28b8B0xb8b]
    =================================
    0x28b8_0x0S0xb8b: v28b8_0Vb8b = PHI v28a7Vb8b, v28f5Vb8b
    0x28b8_0x1S0xb8b: v28b8_1Vb8b = PHI v2873Vb8b(0x2), v28f9Vb8b
    0x28baS0xb8b: v28baVb8b(0x0) = CONST 
    0x28bdS0xb8b: v28bdVb8b = SLOAD v28b8_1Vb8b
    0x28bfS0xb8b: v28bfVb8b(0x100) = CONST 
    0x28c2S0xb8b: v28c2Vb8b(0x1) = EXP v28bfVb8b(0x100), v28baVb8b(0x0)
    0x28c4S0xb8b: v28c4Vb8b = DIV v28bdVb8b, v28c2Vb8b(0x1)
    0x28c5S0xb8b: v28c5Vb8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28daS0xb8b: v28daVb8b = AND v28c5Vb8b(0xffffffffffffffffffffffffffffffffffffffff), v28c4Vb8b
    0x28dbS0xb8b: v28dbVb8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28f0S0xb8b: v28f0Vb8b = AND v28dbVb8b(0xffffffffffffffffffffffffffffffffffffffff), v28daVb8b
    0x28f2S0xb8b: MSTORE v28b8_0Vb8b, v28f0Vb8b
    0x28f3S0xb8b: v28f3Vb8b(0x20) = CONST 
    0x28f5S0xb8b: v28f5Vb8b = ADD v28f3Vb8b(0x20), v28b8_0Vb8b
    0x28f7S0xb8b: v28f7Vb8b(0x1) = CONST 
    0x28f9S0xb8b: v28f9Vb8b = ADD v28f7Vb8b(0x1), v28b8_1Vb8b
    0x28fdS0xb8b: v28fdVb8b = GT v28b6Vb8b, v28f5Vb8b
    0x28feS0xb8b: v28feVb8b(0x28b8) = CONST 
    0x2901S0xb8b: JUMPI v28feVb8b(0x28b8), v28fdVb8b

    Begin block 0x2902B0xb8b
    prev=[0x2858B0xb8b, 0x28b8B0xb8b], succ=[0x292aB0xb8b]
    =================================
    0x2902_0x2S0xb8b: v2902_2Vb8b = PHI v28b6Vb8b, v28a7Vb8b
    0x2907S0xb8b: MSTORE v2902_2Vb8b, vb93
    0x2908S0xb8b: v2908Vb8b(0x20) = CONST 
    0x290aS0xb8b: v290aVb8b = ADD v2908Vb8b(0x20), v2902_2Vb8b
    0x290dS0xb8b: MSTORE v290aVb8b, vb9c
    0x290eS0xb8b: v290eVb8b(0x20) = CONST 
    0x2910S0xb8b: v2910Vb8b = ADD v290eVb8b(0x20), v290aVb8b
    0x2912S0xb8b: v2912Vb8b(0x20) = CONST 
    0x2914S0xb8b: v2914Vb8b = ADD v2912Vb8b(0x20), v2910Vb8b
    0x2916S0xb8b: v2916Vb8b = ISZERO vbe7
    0x2917S0xb8b: v2917Vb8b = ISZERO v2916Vb8b
    0x2918S0xb8b: v2918Vb8b = ISZERO v2917Vb8b
    0x2919S0xb8b: v2919Vb8b = ISZERO v2918Vb8b
    0x291bS0xb8b: MSTORE v2914Vb8b, v2919Vb8b
    0x291cS0xb8b: v291cVb8b(0x20) = CONST 
    0x291eS0xb8b: v291eVb8b = ADD v291cVb8b(0x20), v2914Vb8b
    0x2920S0xb8b: v2920Vb8b(0x80) = CONST 
    0x2922S0xb8b: v2922Vb8b(0x20) = CONST 
    0x2924S0xb8b: v2924Vb8b(0x1000) = MUL v2922Vb8b(0x20), v2920Vb8b(0x80)
    0x2928S0xb8b: v2928Vb8b(0x0) = CONST 

    Begin block 0x292aB0xb8b
    prev=[0x2902B0xb8b, 0x2933B0xb8b], succ=[0x2945B0xb8b, 0x2933B0xb8b]
    =================================
    0x292a_0x0S0xb8b: v292a_0Vb8b = PHI v2928Vb8b(0x0), v293eVb8b
    0x292dS0xb8b: v292dVb8b = LT v292a_0Vb8b, v2924Vb8b(0x1000)
    0x292eS0xb8b: v292eVb8b = ISZERO v292dVb8b
    0x292fS0xb8b: v292fVb8b(0x2945) = CONST 
    0x2932S0xb8b: JUMPI v292fVb8b(0x2945), v292eVb8b

    Begin block 0x2945B0xb8b
    prev=[0x292aB0xb8b], succ=[0x296cB0xb8b]
    =================================
    0x294cS0xb8b: v294cVb8b = ADD v2924Vb8b(0x1000), v291eVb8b
    0x294fS0xb8b: v294fVb8b = SUB v294cVb8b, v28a7Vb8b
    0x2951S0xb8b: MSTORE v2910Vb8b, v294fVb8b
    0x2955S0xb8b: v2955Vb8b = MLOAD vbbe
    0x2957S0xb8b: MSTORE v294cVb8b, v2955Vb8b
    0x2958S0xb8b: v2958Vb8b(0x20) = CONST 
    0x295aS0xb8b: v295aVb8b = ADD v2958Vb8b(0x20), v294cVb8b
    0x295eS0xb8b: v295eVb8b = MLOAD vbbe
    0x2960S0xb8b: v2960Vb8b(0x20) = CONST 
    0x2962S0xb8b: v2962Vb8b = ADD v2960Vb8b(0x20), vbbe
    0x2964S0xb8b: v2964Vb8b(0x20) = CONST 
    0x2966S0xb8b: v2966Vb8b = MUL v2964Vb8b(0x20), v295eVb8b
    0x296aS0xb8b: v296aVb8b(0x0) = CONST 

    Begin block 0x296cB0xb8b
    prev=[0x2945B0xb8b, 0x2975B0xb8b], succ=[0x2987B0xb8b, 0x2975B0xb8b]
    =================================
    0x296c_0x0S0xb8b: v296c_0Vb8b = PHI v296aVb8b(0x0), v2980Vb8b
    0x296fS0xb8b: v296fVb8b = LT v296c_0Vb8b, v2966Vb8b
    0x2970S0xb8b: v2970Vb8b = ISZERO v296fVb8b
    0x2971S0xb8b: v2971Vb8b(0x2987) = CONST 
    0x2974S0xb8b: JUMPI v2971Vb8b(0x2987), v2970Vb8b

    Begin block 0x2987B0xb8b
    prev=[0x296cB0xb8b], succ=[0x29aaB0xb8b, 0x29aeB0xb8b]
    =================================
    0x298eS0xb8b: v298eVb8b = ADD v2966Vb8b, v295aVb8b
    0x2998S0xb8b: v2998Vb8b(0x0) = CONST 
    0x299aS0xb8b: v299aVb8b(0x40) = CONST 
    0x299cS0xb8b: v299cVb8b = MLOAD v299aVb8b(0x40)
    0x299fS0xb8b: v299fVb8b = SUB v298eVb8b, v299cVb8b
    0x29a3S0xb8b: v29a3Vb8b = EXTCODESIZE v2859Vb8b(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb)
    0x29a4S0xb8b: v29a4Vb8b = ISZERO v29a3Vb8b
    0x29a5S0xb8b: v29a5Vb8b = ISZERO v29a4Vb8b
    0x29a6S0xb8b: v29a6Vb8b(0x29ae) = CONST 
    0x29a9S0xb8b: JUMPI v29a6Vb8b(0x29ae), v29a5Vb8b

    Begin block 0x29aaB0xb8b
    prev=[0x2987B0xb8b], succ=[]
    =================================
    0x29aaS0xb8b: v29aaVb8b(0x0) = CONST 
    0x29adS0xb8b: REVERT v29aaVb8b(0x0), v29aaVb8b(0x0)

    Begin block 0x29aeB0xb8b
    prev=[0x2987B0xb8b], succ=[0x29bbB0xb8b, 0x29bfB0xb8b]
    =================================
    0x29afS0xb8b: v29afVb8b(0x2c6) = CONST 
    0x29b2S0xb8b: v29b2Vb8b = GAS 
    0x29b3S0xb8b: v29b3Vb8b = SUB v29b2Vb8b, v29afVb8b(0x2c6)
    0x29b4S0xb8b: v29b4Vb8b = DELEGATECALL v29b3Vb8b, v2859Vb8b(0xb444b84053f7eca1c02d778f0b6fff99dd4608bb), v299cVb8b, v299fVb8b, v299cVb8b, v2998Vb8b(0x0)
    0x29b5S0xb8b: v29b5Vb8b = ISZERO v29b4Vb8b
    0x29b6S0xb8b: v29b6Vb8b = ISZERO v29b5Vb8b
    0x29b7S0xb8b: v29b7Vb8b(0x29bf) = CONST 
    0x29baS0xb8b: JUMPI v29b7Vb8b(0x29bf), v29b6Vb8b

    Begin block 0x29bbB0xb8b
    prev=[0x29aeB0xb8b], succ=[]
    =================================
    0x29bbS0xb8b: v29bbVb8b(0x0) = CONST 
    0x29beS0xb8b: REVERT v29bbVb8b(0x0), v29bbVb8b(0x0)

    Begin block 0x29bfB0xb8b
    prev=[0x29aeB0xb8b], succ=[0xc22]
    =================================
    0x29c8S0xb8b: JUMP vb8c(0xc22)

    Begin block 0xc22
    prev=[0x29bfB0xb8b], succ=[]
    =================================
    0xc23: STOP 

    Begin block 0x2975B0xb8b
    prev=[0x296cB0xb8b], succ=[0x296cB0xb8b]
    =================================
    0x2975_0x0S0xb8b: v2975_0Vb8b = PHI v296aVb8b(0x0), v2980Vb8b
    0x2977S0xb8b: v2977Vb8b = ADD v2962Vb8b, v2975_0Vb8b
    0x2978S0xb8b: v2978Vb8b = MLOAD v2977Vb8b
    0x297bS0xb8b: v297bVb8b = ADD v295aVb8b, v2975_0Vb8b
    0x297cS0xb8b: MSTORE v297bVb8b, v2978Vb8b
    0x297dS0xb8b: v297dVb8b(0x20) = CONST 
    0x2980S0xb8b: v2980Vb8b = ADD v2975_0Vb8b, v297dVb8b(0x20)
    0x2983S0xb8b: v2983Vb8b(0x296c) = CONST 
    0x2986S0xb8b: JUMP v2983Vb8b(0x296c)

    Begin block 0x2933B0xb8b
    prev=[0x292aB0xb8b], succ=[0x292aB0xb8b]
    =================================
    0x2933_0x0S0xb8b: v2933_0Vb8b = PHI v2928Vb8b(0x0), v293eVb8b
    0x2935S0xb8b: v2935Vb8b = ADD vbfd, v2933_0Vb8b
    0x2936S0xb8b: v2936Vb8b = MLOAD v2935Vb8b
    0x2939S0xb8b: v2939Vb8b = ADD v291eVb8b, v2933_0Vb8b
    0x293aS0xb8b: MSTORE v2939Vb8b, v2936Vb8b
    0x293bS0xb8b: v293bVb8b(0x20) = CONST 
    0x293eS0xb8b: v293eVb8b = ADD v2933_0Vb8b, v293bVb8b(0x20)
    0x2941S0xb8b: v2941Vb8b(0x292a) = CONST 
    0x2944S0xb8b: JUMP v2941Vb8b(0x292a)

    Begin block 0x283cB0xb8b
    prev=[0x2824B0xb8b], succ=[0x284dB0xb8b]
    =================================
    0x283dS0xb8b: v283dVb8b(0x12) = CONST 
    0x283fS0xb8b: v283fVb8b(0x1) = CONST 
    0x2842S0xb8b: v2842Vb8b = SLOAD v283dVb8b(0x12)
    0x2844S0xb8b: v2844Vb8b(0x100) = CONST 
    0x2847S0xb8b: v2847Vb8b(0x100) = EXP v2844Vb8b(0x100), v283fVb8b(0x1)
    0x2849S0xb8b: v2849Vb8b = DIV v2842Vb8b, v2847Vb8b(0x100)
    0x284aS0xb8b: v284aVb8b(0xff) = CONST 
    0x284cS0xb8b: v284cVb8b = AND v284aVb8b(0xff), v2849Vb8b

}

