function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x2b71]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x2b31: v2b31(0x2b71) = CONST 
    0x2b32: JUMPI v2b31(0x2b71), v8

    Begin block 0xd
    prev=[0x0], succ=[0x2b74, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x6fdde03) = CONST 
    0x3c: v3c = EQ v37(0x6fdde03), v35
    0x2b33: v2b33(0x2b74) = CONST 
    0x2b34: JUMPI v2b33(0x2b74), v3c

    Begin block 0x2b74
    prev=[0xd], succ=[]
    =================================
    0x2b75: v2b75(0x2b6) = CONST 
    0x2b76: CALLPRIVATE v2b75(0x2b6)

    Begin block 0x41
    prev=[0xd], succ=[0x2b77, 0x4c]
    =================================
    0x42: v42(0x13af4035) = CONST 
    0x47: v47 = EQ v42(0x13af4035), v35
    0x2b35: v2b35(0x2b77) = CONST 
    0x2b36: JUMPI v2b35(0x2b77), v47

    Begin block 0x2b77
    prev=[0x41], succ=[]
    =================================
    0x2b78: v2b78(0x344) = CONST 
    0x2b79: CALLPRIVATE v2b78(0x344)

    Begin block 0x4c
    prev=[0x41], succ=[0x2b7a, 0x57]
    =================================
    0x4d: v4d(0x18160ddd) = CONST 
    0x52: v52 = EQ v4d(0x18160ddd), v35
    0x2b37: v2b37(0x2b7a) = CONST 
    0x2b38: JUMPI v2b37(0x2b7a), v52

    Begin block 0x2b7a
    prev=[0x4c], succ=[]
    =================================
    0x2b7b: v2b7b(0x37d) = CONST 
    0x2b7c: CALLPRIVATE v2b7b(0x37d)

    Begin block 0x57
    prev=[0x4c], succ=[0x2b7d, 0x62]
    =================================
    0x58: v58(0x2f745c59) = CONST 
    0x5d: v5d = EQ v58(0x2f745c59), v35
    0x2b39: v2b39(0x2b7d) = CONST 
    0x2b3a: JUMPI v2b39(0x2b7d), v5d

    Begin block 0x2b7d
    prev=[0x57], succ=[]
    =================================
    0x2b7e: v2b7e(0x3a6) = CONST 
    0x2b7f: CALLPRIVATE v2b7e(0x3a6)

    Begin block 0x62
    prev=[0x57], succ=[0x2b80, 0x6d]
    =================================
    0x63: v63(0x3f4ba83a) = CONST 
    0x68: v68 = EQ v63(0x3f4ba83a), v35
    0x2b3b: v2b3b(0x2b80) = CONST 
    0x2b3c: JUMPI v2b3b(0x2b80), v68

    Begin block 0x2b80
    prev=[0x62], succ=[]
    =================================
    0x2b81: v2b81(0x3fc) = CONST 
    0x2b82: CALLPRIVATE v2b81(0x3fc)

    Begin block 0x6d
    prev=[0x62], succ=[0x2b83, 0x78]
    =================================
    0x6e: v6e(0x41c0e1b5) = CONST 
    0x73: v73 = EQ v6e(0x41c0e1b5), v35
    0x2b3d: v2b3d(0x2b83) = CONST 
    0x2b3e: JUMPI v2b3d(0x2b83), v73

    Begin block 0x2b83
    prev=[0x6d], succ=[]
    =================================
    0x2b84: v2b84(0x411) = CONST 
    0x2b85: CALLPRIVATE v2b84(0x411)

    Begin block 0x78
    prev=[0x6d], succ=[0x2b86, 0x83]
    =================================
    0x79: v79(0x474da79a) = CONST 
    0x7e: v7e = EQ v79(0x474da79a), v35
    0x2b3f: v2b3f(0x2b86) = CONST 
    0x2b40: JUMPI v2b3f(0x2b86), v7e

    Begin block 0x2b86
    prev=[0x78], succ=[]
    =================================
    0x2b87: v2b87(0x426) = CONST 
    0x2b88: CALLPRIVATE v2b87(0x426)

    Begin block 0x83
    prev=[0x78], succ=[0x2b89, 0x8e]
    =================================
    0x84: v84(0x47ef01a1) = CONST 
    0x89: v89 = EQ v84(0x47ef01a1), v35
    0x2b41: v2b41(0x2b89) = CONST 
    0x2b42: JUMPI v2b41(0x2b89), v89

    Begin block 0x2b89
    prev=[0x83], succ=[]
    =================================
    0x2b8a: v2b8a(0x489) = CONST 
    0x2b8b: CALLPRIVATE v2b8a(0x489)

    Begin block 0x8e
    prev=[0x83], succ=[0x2b8c, 0x99]
    =================================
    0x8f: v8f(0x4f6ccce7) = CONST 
    0x94: v94 = EQ v8f(0x4f6ccce7), v35
    0x2b43: v2b43(0x2b8c) = CONST 
    0x2b44: JUMPI v2b43(0x2b8c), v94

    Begin block 0x2b8c
    prev=[0x8e], succ=[]
    =================================
    0x2b8d: v2b8d(0x4c0) = CONST 
    0x2b8e: CALLPRIVATE v2b8d(0x4c0)

    Begin block 0x99
    prev=[0x8e], succ=[0xa4, 0x2b8f]
    =================================
    0x9a: v9a(0x54fd4d50) = CONST 
    0x9f: v9f = EQ v9a(0x54fd4d50), v35
    0x2b45: v2b45(0x2b8f) = CONST 
    0x2b46: JUMPI v2b45(0x2b8f), v9f

    Begin block 0xa4
    prev=[0x99], succ=[0x2b92, 0xaf]
    =================================
    0xa5: va5(0x57835720) = CONST 
    0xaa: vaa = EQ va5(0x57835720), v35
    0x2b47: v2b47(0x2b92) = CONST 
    0x2b48: JUMPI v2b47(0x2b92), vaa

    Begin block 0x2b92
    prev=[0xa4], succ=[]
    =================================
    0x2b93: v2b93(0x556) = CONST 
    0x2b94: CALLPRIVATE v2b93(0x556)

    Begin block 0xaf
    prev=[0xa4], succ=[0x2b95, 0xba]
    =================================
    0xb0: vb0(0x5acb6787) = CONST 
    0xb5: vb5 = EQ vb0(0x5acb6787), v35
    0x2b49: v2b49(0x2b95) = CONST 
    0x2b4a: JUMPI v2b49(0x2b95), vb5

    Begin block 0x2b95
    prev=[0xaf], succ=[]
    =================================
    0x2b96: v2b96(0x56b) = CONST 
    0x2b97: CALLPRIVATE v2b96(0x56b)

    Begin block 0xba
    prev=[0xaf], succ=[0x2b98, 0xc5]
    =================================
    0xbb: vbb(0x5c975abb) = CONST 
    0xc0: vc0 = EQ vbb(0x5c975abb), v35
    0x2b4b: v2b4b(0x2b98) = CONST 
    0x2b4c: JUMPI v2b4b(0x2b98), vc0

    Begin block 0x2b98
    prev=[0xba], succ=[]
    =================================
    0x2b99: v2b99(0x5bd) = CONST 
    0x2b9a: CALLPRIVATE v2b99(0x5bd)

    Begin block 0xc5
    prev=[0xba], succ=[0x2b9b, 0xd0]
    =================================
    0xc6: vc6(0x5fd8c710) = CONST 
    0xcb: vcb = EQ vc6(0x5fd8c710), v35
    0x2b4d: v2b4d(0x2b9b) = CONST 
    0x2b4e: JUMPI v2b4d(0x2b9b), vcb

    Begin block 0x2b9b
    prev=[0xc5], succ=[]
    =================================
    0x2b9c: v2b9c(0x5ea) = CONST 
    0x2b9d: CALLPRIVATE v2b9c(0x5ea)

    Begin block 0xd0
    prev=[0xc5], succ=[0x2b9e, 0xdb]
    =================================
    0xd1: vd1(0x609da897) = CONST 
    0xd6: vd6 = EQ vd1(0x609da897), v35
    0x2b4f: v2b4f(0x2b9e) = CONST 
    0x2b50: JUMPI v2b4f(0x2b9e), vd6

    Begin block 0x2b9e
    prev=[0xd0], succ=[]
    =================================
    0x2b9f: v2b9f(0x5ff) = CONST 
    0x2ba0: CALLPRIVATE v2b9f(0x5ff)

    Begin block 0xdb
    prev=[0xd0], succ=[0x2ba1, 0xe6]
    =================================
    0xdc: vdc(0x6352211e) = CONST 
    0xe1: ve1 = EQ vdc(0x6352211e), v35
    0x2b51: v2b51(0x2ba1) = CONST 
    0x2b52: JUMPI v2b51(0x2ba1), ve1

    Begin block 0x2ba1
    prev=[0xdb], succ=[]
    =================================
    0x2ba2: v2ba2(0x62c) = CONST 
    0x2ba3: CALLPRIVATE v2ba2(0x62c)

    Begin block 0xe6
    prev=[0xdb], succ=[0x2ba4, 0xf1]
    =================================
    0xe7: ve7(0x70a08231) = CONST 
    0xec: vec = EQ ve7(0x70a08231), v35
    0x2b53: v2b53(0x2ba4) = CONST 
    0x2b54: JUMPI v2b53(0x2ba4), vec

    Begin block 0x2ba4
    prev=[0xe6], succ=[]
    =================================
    0x2ba5: v2ba5(0x68f) = CONST 
    0x2ba6: CALLPRIVATE v2ba5(0x68f)

    Begin block 0xf1
    prev=[0xe6], succ=[0x2ba7, 0xfc]
    =================================
    0xf2: vf2(0x8456cb59) = CONST 
    0xf7: vf7 = EQ vf2(0x8456cb59), v35
    0x2b55: v2b55(0x2ba7) = CONST 
    0x2b56: JUMPI v2b55(0x2ba7), vf7

    Begin block 0x2ba7
    prev=[0xf1], succ=[]
    =================================
    0x2ba8: v2ba8(0x6dc) = CONST 
    0x2ba9: CALLPRIVATE v2ba8(0x6dc)

    Begin block 0xfc
    prev=[0xf1], succ=[0x2baa, 0x107]
    =================================
    0xfd: vfd(0x8b4ce7ce) = CONST 
    0x102: v102 = EQ vfd(0x8b4ce7ce), v35
    0x2b57: v2b57(0x2baa) = CONST 
    0x2b58: JUMPI v2b57(0x2baa), v102

    Begin block 0x2baa
    prev=[0xfc], succ=[]
    =================================
    0x2bab: v2bab(0x6f1) = CONST 
    0x2bac: CALLPRIVATE v2bab(0x6f1)

    Begin block 0x107
    prev=[0xfc], succ=[0x2bad, 0x112]
    =================================
    0x108: v108(0x8f84aa09) = CONST 
    0x10d: v10d = EQ v108(0x8f84aa09), v35
    0x2b59: v2b59(0x2bad) = CONST 
    0x2b5a: JUMPI v2b59(0x2bad), v10d

    Begin block 0x2bad
    prev=[0x107], succ=[]
    =================================
    0x2bae: v2bae(0x712) = CONST 
    0x2baf: CALLPRIVATE v2bae(0x712)

    Begin block 0x112
    prev=[0x107], succ=[0x2bb0, 0x11d]
    =================================
    0x113: v113(0x95d89b41) = CONST 
    0x118: v118 = EQ v113(0x95d89b41), v35
    0x2b5b: v2b5b(0x2bb0) = CONST 
    0x2b5c: JUMPI v2b5b(0x2bb0), v118

    Begin block 0x2bb0
    prev=[0x112], succ=[]
    =================================
    0x2bb1: v2bb1(0x767) = CONST 
    0x2bb2: CALLPRIVATE v2bb1(0x767)

    Begin block 0x11d
    prev=[0x112], succ=[0x2bb3, 0x128]
    =================================
    0x11e: v11e(0xc87b56dd) = CONST 
    0x123: v123 = EQ v11e(0xc87b56dd), v35
    0x2b5d: v2b5d(0x2bb3) = CONST 
    0x2b5e: JUMPI v2b5d(0x2bb3), v123

    Begin block 0x2bb3
    prev=[0x11d], succ=[]
    =================================
    0x2bb4: v2bb4(0x7f5) = CONST 
    0x2bb5: CALLPRIVATE v2bb4(0x7f5)

    Begin block 0x128
    prev=[0x11d], succ=[0x2bb6, 0x133]
    =================================
    0x129: v129(0xce8e95d4) = CONST 
    0x12e: v12e = EQ v129(0xce8e95d4), v35
    0x2b5f: v2b5f(0x2bb6) = CONST 
    0x2b60: JUMPI v2b5f(0x2bb6), v12e

    Begin block 0x2bb6
    prev=[0x128], succ=[]
    =================================
    0x2bb7: v2bb7(0x891) = CONST 
    0x2bb8: CALLPRIVATE v2bb7(0x891)

    Begin block 0x133
    prev=[0x128], succ=[0x2bb9, 0x13e]
    =================================
    0x134: v134(0xcf73a1bc) = CONST 
    0x139: v139 = EQ v134(0xcf73a1bc), v35
    0x2b61: v2b61(0x2bb9) = CONST 
    0x2b62: JUMPI v2b61(0x2bb9), v139

    Begin block 0x2bb9
    prev=[0x133], succ=[]
    =================================
    0x2bba: v2bba(0x95f) = CONST 
    0x2bbb: CALLPRIVATE v2bba(0x95f)

    Begin block 0x13e
    prev=[0x133], succ=[0x2bbc, 0x149]
    =================================
    0x13f: v13f(0xd0ebdbe7) = CONST 
    0x144: v144 = EQ v13f(0xd0ebdbe7), v35
    0x2b63: v2b63(0x2bbc) = CONST 
    0x2b64: JUMPI v2b63(0x2bbc), v144

    Begin block 0x2bbc
    prev=[0x13e], succ=[]
    =================================
    0x2bbd: v2bbd(0x9b4) = CONST 
    0x2bbe: CALLPRIVATE v2bbd(0x9b4)

    Begin block 0x149
    prev=[0x13e], succ=[0x2bbf, 0x154]
    =================================
    0x14a: v14a(0xd64c2018) = CONST 
    0x14f: v14f = EQ v14a(0xd64c2018), v35
    0x2b65: v2b65(0x2bbf) = CONST 
    0x2b66: JUMPI v2b65(0x2bbf), v14f

    Begin block 0x2bbf
    prev=[0x149], succ=[]
    =================================
    0x2bc0: v2bc0(0x9ed) = CONST 
    0x2bc1: CALLPRIVATE v2bc0(0x9ed)

    Begin block 0x154
    prev=[0x149], succ=[0x2bc2, 0x15f]
    =================================
    0x155: v155(0xe168a31a) = CONST 
    0x15a: v15a = EQ v155(0xe168a31a), v35
    0x2b67: v2b67(0x2bc2) = CONST 
    0x2b68: JUMPI v2b67(0x2bc2), v15a

    Begin block 0x2bc2
    prev=[0x154], succ=[]
    =================================
    0x2bc3: v2bc3(0xa77) = CONST 
    0x2bc4: CALLPRIVATE v2bc3(0xa77)

    Begin block 0x15f
    prev=[0x154], succ=[0x2bc5, 0x16a]
    =================================
    0x160: v160(0xeeb7ab0c) = CONST 
    0x165: v165 = EQ v160(0xeeb7ab0c), v35
    0x2b69: v2b69(0x2bc5) = CONST 
    0x2b6a: JUMPI v2b69(0x2bc5), v165

    Begin block 0x2bc5
    prev=[0x15f], succ=[]
    =================================
    0x2bc6: v2bc6(0xac4) = CONST 
    0x2bc7: CALLPRIVATE v2bc6(0xac4)

    Begin block 0x16a
    prev=[0x15f], succ=[0x2bc8, 0x175]
    =================================
    0x16b: v16b(0xefef39a1) = CONST 
    0x170: v170 = EQ v16b(0xefef39a1), v35
    0x2b6b: v2b6b(0x2bc8) = CONST 
    0x2b6c: JUMPI v2b6b(0x2bc8), v170

    Begin block 0x2bc8
    prev=[0x16a], succ=[]
    =================================
    0x2bc9: v2bc9(0xb46) = CONST 
    0x2bca: CALLPRIVATE v2bc9(0xb46)

    Begin block 0x175
    prev=[0x16a], succ=[0x2bcb, 0x180]
    =================================
    0x176: v176(0xf5ea15d3) = CONST 
    0x17b: v17b = EQ v176(0xf5ea15d3), v35
    0x2b6d: v2b6d(0x2bcb) = CONST 
    0x2b6e: JUMPI v2b6d(0x2bcb), v17b

    Begin block 0x2bcb
    prev=[0x175], succ=[]
    =================================
    0x2bcc: v2bcc(0xb5e) = CONST 
    0x2bcd: CALLPRIVATE v2bcc(0xb5e)

    Begin block 0x180
    prev=[0x175], succ=[0x2b71, 0x2bce]
    =================================
    0x181: v181(0xf8b096bb) = CONST 
    0x186: v186 = EQ v181(0xf8b096bb), v35
    0x2b6f: v2b6f(0x2bce) = CONST 
    0x2b70: JUMPI v2b6f(0x2bce), v186

    Begin block 0x2b71
    prev=[0x0, 0x180], succ=[]
    =================================
    0x2b72: v2b72(0x18b) = CONST 
    0x2b73: CALLPRIVATE v2b72(0x18b)

    Begin block 0x2bce
    prev=[0x180], succ=[]
    =================================
    0x2bcf: v2bcf(0xb80) = CONST 
    0x2bd0: CALLPRIVATE v2bcf(0xb80)

    Begin block 0x2b8f
    prev=[0x99], succ=[]
    =================================
    0x2b90: v2b90(0x4f7) = CONST 
    0x2b91: CALLPRIVATE v2b90(0x4f7)

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
    prev=[0x18b], succ=[0x2a07B0x196]
    =================================
    0x197: v197(0x0) = CONST 
    0x199: v199(0x1a0) = CONST 
    0x19c: v19c(0x2a07) = CONST 
    0x19f: JUMP v19c(0x2a07)

    Begin block 0x2a07B0x196
    prev=[0x196], succ=[0x1a0]
    =================================
    0x2a08S0x196: v2a08V196(0x20) = CONST 
    0x2a0aS0x196: v2a0aV196(0x40) = CONST 
    0x2a0cS0x196: v2a0cV196 = MLOAD v2a0aV196(0x40)
    0x2a0fS0x196: v2a0fV196 = ADD v2a0cV196, v2a08V196(0x20)
    0x2a10S0x196: v2a10V196(0x40) = CONST 
    0x2a12S0x196: MSTORE v2a10V196(0x40), v2a0fV196
    0x2a14S0x196: v2a14V196(0x0) = CONST 
    0x2a17S0x196: MSTORE v2a0cV196, v2a14V196(0x0)
    0x2a1aS0x196: JUMP v199(0x1a0)

    Begin block 0x1a0
    prev=[0x2a07B0x196], succ=[0x1c2, 0x212]
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
    prev=[0x2c1], succ=[0x2a1bB0xc41]
    =================================
    0xc42: vc42(0xc49) = CONST 
    0xc45: vc45(0x2a1b) = CONST 
    0xc48: JUMP vc45(0x2a1b)

    Begin block 0x2a1bB0xc41
    prev=[0xc41], succ=[0xc49]
    =================================
    0x2a1cS0xc41: v2a1cVc41(0x20) = CONST 
    0x2a1eS0xc41: v2a1eVc41(0x40) = CONST 
    0x2a20S0xc41: v2a20Vc41 = MLOAD v2a1eVc41(0x40)
    0x2a23S0xc41: v2a23Vc41 = ADD v2a20Vc41, v2a1cVc41(0x20)
    0x2a24S0xc41: v2a24Vc41(0x40) = CONST 
    0x2a26S0xc41: MSTORE v2a24Vc41(0x40), v2a23Vc41
    0x2a28S0xc41: v2a28Vc41(0x0) = CONST 
    0x2a2bS0xc41: MSTORE v2a20Vc41, v2a28Vc41(0x0)
    0x2a2eS0xc41: JUMP vc42(0xc49)

    Begin block 0xc49
    prev=[0x2a1bB0xc41], succ=[0x2c9]
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
    prev=[0xd5e, 0xd88], succ=[0x29ea0x37d]
    =================================
    0xdd8: vdd8(0x29ea) = CONST 
    0xddb: JUMP vdd8(0x29ea)

    Begin block 0x29ea0x37d
    prev=[0xdd2], succ=[0x29fa0x37d, 0x29fb0x37d]
    =================================
    0x29eb0x37d: v37d29eb(0x0) = CONST 
    0x29ee0x37d: v37d29ee(0x6) = CONST 
    0x29f00x37d: v37d29f0(0x10) = CONST 
    0x29f30x37d: v37d29f3(0x1) = LT v37d29ee(0x6), v37d29f0(0x10)
    0x29f40x37d: v37d29f4(0x0) = ISZERO v37d29f3(0x1)
    0x29f50x37d: v37d29f5(0x1) = ISZERO v37d29f4(0x0)
    0x29f60x37d: v37d29f6(0x29fb) = CONST 
    0x29f90x37d: JUMPI v37d29f6(0x29fb), v37d29f5(0x1)

    Begin block 0x29fa0x37d
    prev=[0x29ea0x37d], succ=[]
    =================================
    0x29fa0x37d: THROW 

    Begin block 0x29fb0x37d
    prev=[0x29ea0x37d], succ=[0xddc]
    =================================
    0x29fc0x37d: v37d29fc(0x20) = CONST 
    0x29fe0x37d: v37d29fe(0xc0) = MUL v37d29fc(0x20), v37d29ee(0x6)
    0x29ff0x37d: v37d29ff = ADD v37d29fe(0xc0), vd6e
    0x2a000x37d: v37d2a00 = MLOAD v37d29ff
    0x2a060x37d: JUMP vd61(0xddc)

    Begin block 0xddc
    prev=[0x29fb0x37d], succ=[0xe43, 0xe47]
    =================================
    0xddd: vddd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf2: vdf2 = AND vddd(0xffffffffffffffffffffffffffffffffffffffff), v37d2a00
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
    prev=[0xe67, 0xe91], succ=[0x29ea0x3a6]
    =================================
    0xee1: vee1(0x29ea) = CONST 
    0xee4: JUMP vee1(0x29ea)

    Begin block 0x29ea0x3a6
    prev=[0xedb], succ=[0x29fa0x3a6, 0x29fb0x3a6]
    =================================
    0x29eb0x3a6: v3a629eb(0x0) = CONST 
    0x29ee0x3a6: v3a629ee(0x6) = CONST 
    0x29f00x3a6: v3a629f0(0x10) = CONST 
    0x29f30x3a6: v3a629f3(0x1) = LT v3a629ee(0x6), v3a629f0(0x10)
    0x29f40x3a6: v3a629f4(0x0) = ISZERO v3a629f3(0x1)
    0x29f50x3a6: v3a629f5(0x1) = ISZERO v3a629f4(0x0)
    0x29f60x3a6: v3a629f6(0x29fb) = CONST 
    0x29f90x3a6: JUMPI v3a629f6(0x29fb), v3a629f5(0x1)

    Begin block 0x29fa0x3a6
    prev=[0x29ea0x3a6], succ=[]
    =================================
    0x29fa0x3a6: THROW 

    Begin block 0x29fb0x3a6
    prev=[0x29ea0x3a6], succ=[0xee5]
    =================================
    0x29fc0x3a6: v3a629fc(0x20) = CONST 
    0x29fe0x3a6: v3a629fe(0xc0) = MUL v3a629fc(0x20), v3a629ee(0x6)
    0x29ff0x3a6: v3a629ff = ADD v3a629fe(0xc0), ve77
    0x2a000x3a6: v3a62a00 = MLOAD v3a629ff
    0x2a060x3a6: JUMP ve6a(0xee5)

    Begin block 0xee5
    prev=[0x29fb0x3a6], succ=[0xf8b, 0xf8f]
    =================================
    0xee6: vee6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xefb: vefb = AND vee6(0xffffffffffffffffffffffffffffffffffffffff), v3a62a00
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
    0x11aaS0x494: v11aaV494(0xd8479c546b80ce91916c7800c1840bd6446b06ce) = CONST 
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
    0x1267S0x494: v1267V494 = EXTCODESIZE v11aaV494(0xd8479c546b80ce91916c7800c1840bd6446b06ce)
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
    0x1278S0x494: v1278V494 = DELEGATECALL v1277V494, v11aaV494(0xd8479c546b80ce91916c7800c1840bd6446b06ce), v1260V494, v1263V494, v1260V494, v125cV494(0x0)
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
    prev=[0x128b, 0x12b5], succ=[0x29ea0x4c0]
    =================================
    0x1305: v1305(0x29ea) = CONST 
    0x1308: JUMP v1305(0x29ea)

    Begin block 0x29ea0x4c0
    prev=[0x12ff], succ=[0x29fa0x4c0, 0x29fb0x4c0]
    =================================
    0x29eb0x4c0: v4c029eb(0x0) = CONST 
    0x29ee0x4c0: v4c029ee(0x6) = CONST 
    0x29f00x4c0: v4c029f0(0x10) = CONST 
    0x29f30x4c0: v4c029f3(0x1) = LT v4c029ee(0x6), v4c029f0(0x10)
    0x29f40x4c0: v4c029f4(0x0) = ISZERO v4c029f3(0x1)
    0x29f50x4c0: v4c029f5(0x1) = ISZERO v4c029f4(0x0)
    0x29f60x4c0: v4c029f6(0x29fb) = CONST 
    0x29f90x4c0: JUMPI v4c029f6(0x29fb), v4c029f5(0x1)

    Begin block 0x29fa0x4c0
    prev=[0x29ea0x4c0], succ=[]
    =================================
    0x29fa0x4c0: THROW 

    Begin block 0x29fb0x4c0
    prev=[0x29ea0x4c0], succ=[0x1309]
    =================================
    0x29fc0x4c0: v4c029fc(0x20) = CONST 
    0x29fe0x4c0: v4c029fe(0xc0) = MUL v4c029fc(0x20), v4c029ee(0x6)
    0x29ff0x4c0: v4c029ff = ADD v4c029fe(0xc0), v129b
    0x2a000x4c0: v4c02a00 = MLOAD v4c029ff
    0x2a060x4c0: JUMP v128e(0x1309)

    Begin block 0x1309
    prev=[0x29fb0x4c0], succ=[0x137b, 0x137f]
    =================================
    0x130a: v130a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x131f: v131f = AND v130a(0xffffffffffffffffffffffffffffffffffffffff), v4c02a00
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

function setSetupCompleted()() public {
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
    0x562: v562(0x569) = CONST 
    0x565: v565(0x13cc) = CONST 
    0x568: JUMP v565(0x13cc)

    Begin block 0x13cc
    prev=[0x561], succ=[0x1423, 0x1427]
    =================================
    0x13cd: v13cd(0x0) = CONST 
    0x13d1: v13d1 = SLOAD v13cd(0x0)
    0x13d3: v13d3(0x100) = CONST 
    0x13d6: v13d6(0x1) = EXP v13d3(0x100), v13cd(0x0)
    0x13d8: v13d8 = DIV v13d1, v13d6(0x1)
    0x13d9: v13d9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13ee: v13ee = AND v13d9(0xffffffffffffffffffffffffffffffffffffffff), v13d8
    0x13ef: v13ef(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1404: v1404 = AND v13ef(0xffffffffffffffffffffffffffffffffffffffff), v13ee
    0x1405: v1405 = CALLER 
    0x1406: v1406(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x141b: v141b = AND v1406(0xffffffffffffffffffffffffffffffffffffffff), v1405
    0x141c: v141c = EQ v141b, v1404
    0x141d: v141d = ISZERO v141c
    0x141e: v141e = ISZERO v141d
    0x141f: v141f(0x1427) = CONST 
    0x1422: JUMPI v141f(0x1427), v141e

    Begin block 0x1423
    prev=[0x13cc], succ=[]
    =================================
    0x1423: v1423(0x0) = CONST 
    0x1426: REVERT v1423(0x0), v1423(0x0)

    Begin block 0x1427
    prev=[0x13cc], succ=[0x569]
    =================================
    0x1428: v1428(0x1) = CONST 
    0x142a: v142a(0x12) = CONST 
    0x142c: v142c(0x1) = CONST 
    0x142e: v142e(0x100) = CONST 
    0x1431: v1431(0x100) = EXP v142e(0x100), v142c(0x1)
    0x1433: v1433 = SLOAD v142a(0x12)
    0x1435: v1435(0xff) = CONST 
    0x1437: v1437(0xff00) = MUL v1435(0xff), v1431(0x100)
    0x1438: v1438(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v1437(0xff00)
    0x1439: v1439 = AND v1438(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v1433
    0x143c: v143c(0x0) = ISZERO v1428(0x1)
    0x143d: v143d(0x1) = ISZERO v143c(0x0)
    0x143e: v143e(0x100) = MUL v143d(0x1), v1431(0x100)
    0x143f: v143f = OR v143e(0x100), v1439
    0x1441: SSTORE v142a(0x12), v143f
    0x1443: JUMP v562(0x569)

    Begin block 0x569
    prev=[0x1427], succ=[]
    =================================
    0x56a: STOP 

}

function createRegion(uint256,uint256,uint256,uint256)() public {
    Begin block 0x56b
    prev=[], succ=[0x572, 0x576]
    =================================
    0x56c: v56c = CALLVALUE 
    0x56d: v56d = ISZERO v56c
    0x56e: v56e(0x576) = CONST 
    0x571: JUMPI v56e(0x576), v56d

    Begin block 0x572
    prev=[0x56b], succ=[]
    =================================
    0x572: v572(0x0) = CONST 
    0x575: REVERT v572(0x0), v572(0x0)

    Begin block 0x576
    prev=[0x56b], succ=[0x1444]
    =================================
    0x577: v577(0x5a7) = CONST 
    0x57a: v57a(0x4) = CONST 
    0x57e: v57e = CALLDATALOAD v57a(0x4)
    0x580: v580(0x20) = CONST 
    0x582: v582(0x24) = ADD v580(0x20), v57a(0x4)
    0x587: v587 = CALLDATALOAD v582(0x24)
    0x589: v589(0x20) = CONST 
    0x58b: v58b(0x44) = ADD v589(0x20), v582(0x24)
    0x590: v590 = CALLDATALOAD v58b(0x44)
    0x592: v592(0x20) = CONST 
    0x594: v594(0x64) = ADD v592(0x20), v58b(0x44)
    0x599: v599 = CALLDATALOAD v594(0x64)
    0x59b: v59b(0x20) = CONST 
    0x59d: v59d(0x84) = ADD v59b(0x20), v594(0x64)
    0x5a3: v5a3(0x1444) = CONST 
    0x5a6: JUMP v5a3(0x1444)

    Begin block 0x1444
    prev=[0x576], succ=[0x14ee, 0x149c]
    =================================
    0x1445: v1445(0x0) = CONST 
    0x1448: v1448(0x0) = CONST 
    0x144b: v144b = SLOAD v1445(0x0)
    0x144d: v144d(0x100) = CONST 
    0x1450: v1450(0x1) = EXP v144d(0x100), v1448(0x0)
    0x1452: v1452 = DIV v144b, v1450(0x1)
    0x1453: v1453(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1468: v1468 = AND v1453(0xffffffffffffffffffffffffffffffffffffffff), v1452
    0x1469: v1469(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x147e: v147e = AND v1469(0xffffffffffffffffffffffffffffffffffffffff), v1468
    0x147f: v147f = CALLER 
    0x1480: v1480(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1495: v1495 = AND v1480(0xffffffffffffffffffffffffffffffffffffffff), v147f
    0x1496: v1496 = EQ v1495, v147e
    0x1498: v1498(0x14ee) = CONST 
    0x149b: JUMPI v1498(0x14ee), v1496

    Begin block 0x14ee
    prev=[0x1444, 0x149c], succ=[0x14f5, 0x14f9]
    =================================
    0x14ee_0x0: v14ee_0 = PHI v1496, v14ed
    0x14ef: v14ef = ISZERO v14ee_0
    0x14f0: v14f0 = ISZERO v14ef
    0x14f1: v14f1(0x14f9) = CONST 
    0x14f4: JUMPI v14f1(0x14f9), v14f0

    Begin block 0x14f5
    prev=[0x14ee], succ=[]
    =================================
    0x14f5: v14f5(0x0) = CONST 
    0x14f8: REVERT v14f5(0x0), v14f5(0x0)

    Begin block 0x14f9
    prev=[0x14ee], succ=[0x157d, 0x15cd]
    =================================
    0x14fa: v14fa(0xd8479c546b80ce91916c7800c1840bd6446b06ce) = CONST 
    0x150f: v150f(0xf7a919be) = CONST 
    0x1514: v1514(0x2) = CONST 
    0x1516: v1516(0x0) = CONST 
    0x151a: v151a = SLOAD v1516(0x0)
    0x151c: v151c(0x100) = CONST 
    0x151f: v151f(0x1) = EXP v151c(0x100), v1516(0x0)
    0x1521: v1521 = DIV v151a, v151f(0x1)
    0x1522: v1522(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1537: v1537 = AND v1522(0xffffffffffffffffffffffffffffffffffffffff), v1521
    0x153c: v153c(0x0) = CONST 
    0x153e: v153e(0x40) = CONST 
    0x1540: v1540 = MLOAD v153e(0x40)
    0x1541: v1541(0x20) = CONST 
    0x1543: v1543 = ADD v1541(0x20), v1540
    0x1544: MSTORE v1543, v153c(0x0)
    0x1545: v1545(0x40) = CONST 
    0x1547: v1547 = MLOAD v1545(0x40)
    0x1549: v1549(0xffffffff) = CONST 
    0x154e: v154e(0xf7a919be) = AND v1549(0xffffffff), v150f(0xf7a919be)
    0x154f: v154f(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x156d: v156d(0xf7a919be00000000000000000000000000000000000000000000000000000000) = MUL v154f(0x100000000000000000000000000000000000000000000000000000000), v154e(0xf7a919be)
    0x156f: MSTORE v1547, v156d(0xf7a919be00000000000000000000000000000000000000000000000000000000)
    0x1570: v1570(0x4) = CONST 
    0x1572: v1572 = ADD v1570(0x4), v1547
    0x1575: v1575(0x10) = CONST 
    0x1578: v1578(0x0) = ISZERO v1575(0x10)
    0x1579: v1579(0x15cd) = CONST 
    0x157c: JUMPI v1579(0x15cd), v1578(0x0)

    Begin block 0x157d
    prev=[0x14f9], succ=[0x1583]
    =================================
    0x157d: v157d(0x20) = CONST 
    0x157f: v157f(0x200) = MUL v157d(0x20), v1575(0x10)
    0x1581: v1581 = ADD v1572, v157f(0x200)

    Begin block 0x1583
    prev=[0x157d, 0x1583], succ=[0x15cd, 0x1583]
    =================================
    0x1583_0x0: v1583_0 = PHI v1572, v15c0
    0x1583_0x1: v1583_1 = PHI v1514(0x2), v15c4
    0x1585: v1585(0x0) = CONST 
    0x1588: v1588 = SLOAD v1583_1
    0x158a: v158a(0x100) = CONST 
    0x158d: v158d(0x1) = EXP v158a(0x100), v1585(0x0)
    0x158f: v158f = DIV v1588, v158d(0x1)
    0x1590: v1590(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15a5: v15a5 = AND v1590(0xffffffffffffffffffffffffffffffffffffffff), v158f
    0x15a6: v15a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15bb: v15bb = AND v15a6(0xffffffffffffffffffffffffffffffffffffffff), v15a5
    0x15bd: MSTORE v1583_0, v15bb
    0x15be: v15be(0x20) = CONST 
    0x15c0: v15c0 = ADD v15be(0x20), v1583_0
    0x15c2: v15c2(0x1) = CONST 
    0x15c4: v15c4 = ADD v15c2(0x1), v1583_1
    0x15c8: v15c8 = GT v1581, v15c0
    0x15c9: v15c9(0x1583) = CONST 
    0x15cc: JUMPI v15c9(0x1583), v15c8

    Begin block 0x15cd
    prev=[0x14f9, 0x1583], succ=[0x1634, 0x1638]
    =================================
    0x15cd_0x2: v15cd_2 = PHI v1572, v1581
    0x15d1: v15d1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15e6: v15e6 = AND v15d1(0xffffffffffffffffffffffffffffffffffffffff), v1537
    0x15e7: v15e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15fc: v15fc = AND v15e7(0xffffffffffffffffffffffffffffffffffffffff), v15e6
    0x15fe: MSTORE v15cd_2, v15fc
    0x15ff: v15ff(0x20) = CONST 
    0x1601: v1601 = ADD v15ff(0x20), v15cd_2
    0x1604: MSTORE v1601, v57e
    0x1605: v1605(0x20) = CONST 
    0x1607: v1607 = ADD v1605(0x20), v1601
    0x160a: MSTORE v1607, v587
    0x160b: v160b(0x20) = CONST 
    0x160d: v160d = ADD v160b(0x20), v1607
    0x1610: MSTORE v160d, v590
    0x1611: v1611(0x20) = CONST 
    0x1613: v1613 = ADD v1611(0x20), v160d
    0x1616: MSTORE v1613, v599
    0x1617: v1617(0x20) = CONST 
    0x1619: v1619 = ADD v1617(0x20), v1613
    0x1622: v1622(0x20) = CONST 
    0x1624: v1624(0x40) = CONST 
    0x1626: v1626 = MLOAD v1624(0x40)
    0x1629: v1629 = SUB v1619, v1626
    0x162d: v162d = EXTCODESIZE v14fa(0xd8479c546b80ce91916c7800c1840bd6446b06ce)
    0x162e: v162e = ISZERO v162d
    0x162f: v162f = ISZERO v162e
    0x1630: v1630(0x1638) = CONST 
    0x1633: JUMPI v1630(0x1638), v162f

    Begin block 0x1634
    prev=[0x15cd], succ=[]
    =================================
    0x1634: v1634(0x0) = CONST 
    0x1637: REVERT v1634(0x0), v1634(0x0)

    Begin block 0x1638
    prev=[0x15cd], succ=[0x1645, 0x1649]
    =================================
    0x1639: v1639(0x2c6) = CONST 
    0x163c: v163c = GAS 
    0x163d: v163d = SUB v163c, v1639(0x2c6)
    0x163e: v163e = DELEGATECALL v163d, v14fa(0xd8479c546b80ce91916c7800c1840bd6446b06ce), v1626, v1629, v1626, v1622(0x20)
    0x163f: v163f = ISZERO v163e
    0x1640: v1640 = ISZERO v163f
    0x1641: v1641(0x1649) = CONST 
    0x1644: JUMPI v1641(0x1649), v1640

    Begin block 0x1645
    prev=[0x1638], succ=[]
    =================================
    0x1645: v1645(0x0) = CONST 
    0x1648: REVERT v1645(0x0), v1645(0x0)

    Begin block 0x1649
    prev=[0x1638], succ=[0x5a7]
    =================================
    0x164d: v164d(0x40) = CONST 
    0x164f: v164f = MLOAD v164d(0x40)
    0x1651: v1651 = MLOAD v164f
    0x165b: JUMP v577(0x5a7)

    Begin block 0x5a7
    prev=[0x1649], succ=[]
    =================================
    0x5a8: v5a8(0x40) = CONST 
    0x5aa: v5aa = MLOAD v5a8(0x40)
    0x5ae: MSTORE v5aa, v1445(0x0)
    0x5af: v5af(0x20) = CONST 
    0x5b1: v5b1 = ADD v5af(0x20), v5aa
    0x5b5: v5b5(0x40) = CONST 
    0x5b7: v5b7 = MLOAD v5b5(0x40)
    0x5ba: v5ba(0x20) = SUB v5b1, v5b7
    0x5bc: RETURN v5b7, v5ba(0x20)

    Begin block 0x149c
    prev=[0x1444], succ=[0x14ee]
    =================================
    0x149d: v149d(0x1) = CONST 
    0x149f: v149f(0x0) = CONST 
    0x14a2: v14a2 = SLOAD v149d(0x1)
    0x14a4: v14a4(0x100) = CONST 
    0x14a7: v14a7(0x1) = EXP v14a4(0x100), v149f(0x0)
    0x14a9: v14a9 = DIV v14a2, v14a7(0x1)
    0x14aa: v14aa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14bf: v14bf = AND v14aa(0xffffffffffffffffffffffffffffffffffffffff), v14a9
    0x14c0: v14c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14d5: v14d5 = AND v14c0(0xffffffffffffffffffffffffffffffffffffffff), v14bf
    0x14d6: v14d6 = CALLER 
    0x14d7: v14d7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14ec: v14ec = AND v14d7(0xffffffffffffffffffffffffffffffffffffffff), v14d6
    0x14ed: v14ed = EQ v14ec, v14d5

}

function paused()() public {
    Begin block 0x5bd
    prev=[], succ=[0x5c4, 0x5c8]
    =================================
    0x5be: v5be = CALLVALUE 
    0x5bf: v5bf = ISZERO v5be
    0x5c0: v5c0(0x5c8) = CONST 
    0x5c3: JUMPI v5c0(0x5c8), v5bf

    Begin block 0x5c4
    prev=[0x5bd], succ=[]
    =================================
    0x5c4: v5c4(0x0) = CONST 
    0x5c7: REVERT v5c4(0x0), v5c4(0x0)

    Begin block 0x5c8
    prev=[0x5bd], succ=[0x165c]
    =================================
    0x5c9: v5c9(0x5d0) = CONST 
    0x5cc: v5cc(0x165c) = CONST 
    0x5cf: JUMP v5cc(0x165c)

    Begin block 0x165c
    prev=[0x5c8], succ=[0x5d0]
    =================================
    0x165d: v165d(0x12) = CONST 
    0x165f: v165f(0x0) = CONST 
    0x1662: v1662 = SLOAD v165d(0x12)
    0x1664: v1664(0x100) = CONST 
    0x1667: v1667(0x1) = EXP v1664(0x100), v165f(0x0)
    0x1669: v1669 = DIV v1662, v1667(0x1)
    0x166a: v166a(0xff) = CONST 
    0x166c: v166c = AND v166a(0xff), v1669
    0x166e: JUMP v5c9(0x5d0)

    Begin block 0x5d0
    prev=[0x165c], succ=[]
    =================================
    0x5d1: v5d1(0x40) = CONST 
    0x5d3: v5d3 = MLOAD v5d1(0x40)
    0x5d6: v5d6 = ISZERO v166c
    0x5d7: v5d7 = ISZERO v5d6
    0x5d8: v5d8 = ISZERO v5d7
    0x5d9: v5d9 = ISZERO v5d8
    0x5db: MSTORE v5d3, v5d9
    0x5dc: v5dc(0x20) = CONST 
    0x5de: v5de = ADD v5dc(0x20), v5d3
    0x5e2: v5e2(0x40) = CONST 
    0x5e4: v5e4 = MLOAD v5e2(0x40)
    0x5e7: v5e7(0x20) = SUB v5de, v5e4
    0x5e9: RETURN v5e4, v5e7(0x20)

}

function withdrawBalance()() public {
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
    prev=[0x5ea], succ=[0x166fB0x5f5]
    =================================
    0x5f6: v5f6(0x5fd) = CONST 
    0x5f9: v5f9(0x166f) = CONST 
    0x5fc: JUMP v5f9(0x166f), v5f6(0x5fd)

    Begin block 0x166fB0x5f5
    prev=[0x5f5], succ=[0x16c6B0x5f5, 0x16caB0x5f5]
    =================================
    0x1670S0x5f5: v1670V5f5(0x0) = CONST 
    0x1674S0x5f5: v1674V5f5 = SLOAD v1670V5f5(0x0)
    0x1676S0x5f5: v1676V5f5(0x100) = CONST 
    0x1679S0x5f5: v1679V5f5(0x1) = EXP v1676V5f5(0x100), v1670V5f5(0x0)
    0x167bS0x5f5: v167bV5f5 = DIV v1674V5f5, v1679V5f5(0x1)
    0x167cS0x5f5: v167cV5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1691S0x5f5: v1691V5f5 = AND v167cV5f5(0xffffffffffffffffffffffffffffffffffffffff), v167bV5f5
    0x1692S0x5f5: v1692V5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16a7S0x5f5: v16a7V5f5 = AND v1692V5f5(0xffffffffffffffffffffffffffffffffffffffff), v1691V5f5
    0x16a8S0x5f5: v16a8V5f5 = CALLER 
    0x16a9S0x5f5: v16a9V5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16beS0x5f5: v16beV5f5 = AND v16a9V5f5(0xffffffffffffffffffffffffffffffffffffffff), v16a8V5f5
    0x16bfS0x5f5: v16bfV5f5 = EQ v16beV5f5, v16a7V5f5
    0x16c0S0x5f5: v16c0V5f5 = ISZERO v16bfV5f5
    0x16c1S0x5f5: v16c1V5f5 = ISZERO v16c0V5f5
    0x16c2S0x5f5: v16c2V5f5(0x16ca) = CONST 
    0x16c5S0x5f5: JUMPI v16c2V5f5(0x16ca), v16c1V5f5

    Begin block 0x16c6B0x5f5
    prev=[0x166fB0x5f5], succ=[]
    =================================
    0x16c6S0x5f5: v16c6V5f5(0x0) = CONST 
    0x16c9S0x5f5: REVERT v16c6V5f5(0x0), v16c6V5f5(0x0)

    Begin block 0x16caB0x5f5
    prev=[0x166fB0x5f5], succ=[0x173eB0x5f5, 0x1742B0x5f5]
    =================================
    0x16cbS0x5f5: v16cbV5f5(0x0) = CONST 
    0x16cfS0x5f5: v16cfV5f5 = SLOAD v16cbV5f5(0x0)
    0x16d1S0x5f5: v16d1V5f5(0x100) = CONST 
    0x16d4S0x5f5: v16d4V5f5(0x1) = EXP v16d1V5f5(0x100), v16cbV5f5(0x0)
    0x16d6S0x5f5: v16d6V5f5 = DIV v16cfV5f5, v16d4V5f5(0x1)
    0x16d7S0x5f5: v16d7V5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16ecS0x5f5: v16ecV5f5 = AND v16d7V5f5(0xffffffffffffffffffffffffffffffffffffffff), v16d6V5f5
    0x16edS0x5f5: v16edV5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1702S0x5f5: v1702V5f5 = AND v16edV5f5(0xffffffffffffffffffffffffffffffffffffffff), v16ecV5f5
    0x1703S0x5f5: v1703V5f5(0x8fc) = CONST 
    0x1706S0x5f5: v1706V5f5 = ADDRESS 
    0x1707S0x5f5: v1707V5f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x171cS0x5f5: v171cV5f5 = AND v1707V5f5(0xffffffffffffffffffffffffffffffffffffffff), v1706V5f5
    0x171dS0x5f5: v171dV5f5 = BALANCE v171cV5f5
    0x1720S0x5f5: v1720V5f5 = ISZERO v171dV5f5
    0x1721S0x5f5: v1721V5f5 = MUL v1720V5f5, v1703V5f5(0x8fc)
    0x1723S0x5f5: v1723V5f5(0x40) = CONST 
    0x1725S0x5f5: v1725V5f5 = MLOAD v1723V5f5(0x40)
    0x1726S0x5f5: v1726V5f5(0x0) = CONST 
    0x1728S0x5f5: v1728V5f5(0x40) = CONST 
    0x172aS0x5f5: v172aV5f5 = MLOAD v1728V5f5(0x40)
    0x172dS0x5f5: v172dV5f5(0x0) = SUB v1725V5f5, v172aV5f5
    0x1732S0x5f5: v1732V5f5 = CALL v1721V5f5, v1702V5f5, v171dV5f5, v172aV5f5, v172dV5f5(0x0), v172aV5f5, v1726V5f5(0x0)
    0x1738S0x5f5: v1738V5f5 = ISZERO v1732V5f5
    0x1739S0x5f5: v1739V5f5 = ISZERO v1738V5f5
    0x173aS0x5f5: v173aV5f5(0x1742) = CONST 
    0x173dS0x5f5: JUMPI v173aV5f5(0x1742), v1739V5f5

    Begin block 0x173eB0x5f5
    prev=[0x16caB0x5f5], succ=[]
    =================================
    0x173eS0x5f5: v173eV5f5(0x0) = CONST 
    0x1741S0x5f5: REVERT v173eV5f5(0x0), v173eV5f5(0x0)

    Begin block 0x1742B0x5f5
    prev=[0x16caB0x5f5], succ=[0x5fd]
    =================================
    0x1743S0x5f5: JUMP v5f6(0x5fd)

    Begin block 0x5fd
    prev=[0x1742B0x5f5], succ=[]
    =================================
    0x5fe: STOP 

}

function setupCompleted()() public {
    Begin block 0x5ff
    prev=[], succ=[0x606, 0x60a]
    =================================
    0x600: v600 = CALLVALUE 
    0x601: v601 = ISZERO v600
    0x602: v602(0x60a) = CONST 
    0x605: JUMPI v602(0x60a), v601

    Begin block 0x606
    prev=[0x5ff], succ=[]
    =================================
    0x606: v606(0x0) = CONST 
    0x609: REVERT v606(0x0), v606(0x0)

    Begin block 0x60a
    prev=[0x5ff], succ=[0x1744]
    =================================
    0x60b: v60b(0x612) = CONST 
    0x60e: v60e(0x1744) = CONST 
    0x611: JUMP v60e(0x1744)

    Begin block 0x1744
    prev=[0x60a], succ=[0x612]
    =================================
    0x1745: v1745(0x12) = CONST 
    0x1747: v1747(0x1) = CONST 
    0x174a: v174a = SLOAD v1745(0x12)
    0x174c: v174c(0x100) = CONST 
    0x174f: v174f(0x100) = EXP v174c(0x100), v1747(0x1)
    0x1751: v1751 = DIV v174a, v174f(0x100)
    0x1752: v1752(0xff) = CONST 
    0x1754: v1754 = AND v1752(0xff), v1751
    0x1756: JUMP v60b(0x612)

    Begin block 0x612
    prev=[0x1744], succ=[]
    =================================
    0x613: v613(0x40) = CONST 
    0x615: v615 = MLOAD v613(0x40)
    0x618: v618 = ISZERO v1754
    0x619: v619 = ISZERO v618
    0x61a: v61a = ISZERO v619
    0x61b: v61b = ISZERO v61a
    0x61d: MSTORE v615, v61b
    0x61e: v61e(0x20) = CONST 
    0x620: v620 = ADD v61e(0x20), v615
    0x624: v624(0x40) = CONST 
    0x626: v626 = MLOAD v624(0x40)
    0x629: v629(0x20) = SUB v620, v626
    0x62b: RETURN v626, v629(0x20)

}

function ownerOf(uint256)() public {
    Begin block 0x62c
    prev=[], succ=[0x633, 0x637]
    =================================
    0x62d: v62d = CALLVALUE 
    0x62e: v62e = ISZERO v62d
    0x62f: v62f(0x637) = CONST 
    0x632: JUMPI v62f(0x637), v62e

    Begin block 0x633
    prev=[0x62c], succ=[]
    =================================
    0x633: v633(0x0) = CONST 
    0x636: REVERT v633(0x0), v633(0x0)

    Begin block 0x637
    prev=[0x62c], succ=[0x1757]
    =================================
    0x638: v638(0x64d) = CONST 
    0x63b: v63b(0x4) = CONST 
    0x63f: v63f = CALLDATALOAD v63b(0x4)
    0x641: v641(0x20) = CONST 
    0x643: v643(0x24) = ADD v641(0x20), v63b(0x4)
    0x649: v649(0x1757) = CONST 
    0x64c: JUMP v649(0x1757)

    Begin block 0x1757
    prev=[0x637], succ=[0x17b8, 0x1808]
    =================================
    0x1758: v1758(0x0) = CONST 
    0x175a: v175a(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77) = CONST 
    0x176f: v176f(0xd6e4ddc5) = CONST 
    0x1774: v1774(0x2) = CONST 
    0x1777: v1777(0x0) = CONST 
    0x1779: v1779(0x40) = CONST 
    0x177b: v177b = MLOAD v1779(0x40)
    0x177c: v177c(0x20) = CONST 
    0x177e: v177e = ADD v177c(0x20), v177b
    0x177f: MSTORE v177e, v1777(0x0)
    0x1780: v1780(0x40) = CONST 
    0x1782: v1782 = MLOAD v1780(0x40)
    0x1784: v1784(0xffffffff) = CONST 
    0x1789: v1789(0xd6e4ddc5) = AND v1784(0xffffffff), v176f(0xd6e4ddc5)
    0x178a: v178a(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x17a8: v17a8(0xd6e4ddc500000000000000000000000000000000000000000000000000000000) = MUL v178a(0x100000000000000000000000000000000000000000000000000000000), v1789(0xd6e4ddc5)
    0x17aa: MSTORE v1782, v17a8(0xd6e4ddc500000000000000000000000000000000000000000000000000000000)
    0x17ab: v17ab(0x4) = CONST 
    0x17ad: v17ad = ADD v17ab(0x4), v1782
    0x17b0: v17b0(0x10) = CONST 
    0x17b3: v17b3(0x0) = ISZERO v17b0(0x10)
    0x17b4: v17b4(0x1808) = CONST 
    0x17b7: JUMPI v17b4(0x1808), v17b3(0x0)

    Begin block 0x17b8
    prev=[0x1757], succ=[0x17be]
    =================================
    0x17b8: v17b8(0x20) = CONST 
    0x17ba: v17ba(0x200) = MUL v17b8(0x20), v17b0(0x10)
    0x17bc: v17bc = ADD v17ad, v17ba(0x200)

    Begin block 0x17be
    prev=[0x17b8, 0x17be], succ=[0x1808, 0x17be]
    =================================
    0x17be_0x0: v17be_0 = PHI v17ad, v17fb
    0x17be_0x1: v17be_1 = PHI v1774(0x2), v17ff
    0x17c0: v17c0(0x0) = CONST 
    0x17c3: v17c3 = SLOAD v17be_1
    0x17c5: v17c5(0x100) = CONST 
    0x17c8: v17c8(0x1) = EXP v17c5(0x100), v17c0(0x0)
    0x17ca: v17ca = DIV v17c3, v17c8(0x1)
    0x17cb: v17cb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17e0: v17e0 = AND v17cb(0xffffffffffffffffffffffffffffffffffffffff), v17ca
    0x17e1: v17e1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17f6: v17f6 = AND v17e1(0xffffffffffffffffffffffffffffffffffffffff), v17e0
    0x17f8: MSTORE v17be_0, v17f6
    0x17f9: v17f9(0x20) = CONST 
    0x17fb: v17fb = ADD v17f9(0x20), v17be_0
    0x17fd: v17fd(0x1) = CONST 
    0x17ff: v17ff = ADD v17fd(0x1), v17be_1
    0x1803: v1803 = GT v17bc, v17fb
    0x1804: v1804(0x17be) = CONST 
    0x1807: JUMPI v1804(0x17be), v1803

    Begin block 0x1808
    prev=[0x1757, 0x17be], succ=[0x1827, 0x182b]
    =================================
    0x1808_0x2: v1808_2 = PHI v17ad, v17bc
    0x180d: MSTORE v1808_2, v63f
    0x180e: v180e(0x20) = CONST 
    0x1810: v1810 = ADD v180e(0x20), v1808_2
    0x1815: v1815(0x20) = CONST 
    0x1817: v1817(0x40) = CONST 
    0x1819: v1819 = MLOAD v1817(0x40)
    0x181c: v181c = SUB v1810, v1819
    0x1820: v1820 = EXTCODESIZE v175a(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77)
    0x1821: v1821 = ISZERO v1820
    0x1822: v1822 = ISZERO v1821
    0x1823: v1823(0x182b) = CONST 
    0x1826: JUMPI v1823(0x182b), v1822

    Begin block 0x1827
    prev=[0x1808], succ=[]
    =================================
    0x1827: v1827(0x0) = CONST 
    0x182a: REVERT v1827(0x0), v1827(0x0)

    Begin block 0x182b
    prev=[0x1808], succ=[0x1838, 0x183c]
    =================================
    0x182c: v182c(0x2c6) = CONST 
    0x182f: v182f = GAS 
    0x1830: v1830 = SUB v182f, v182c(0x2c6)
    0x1831: v1831 = DELEGATECALL v1830, v175a(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77), v1819, v181c, v1819, v1815(0x20)
    0x1832: v1832 = ISZERO v1831
    0x1833: v1833 = ISZERO v1832
    0x1834: v1834(0x183c) = CONST 
    0x1837: JUMPI v1834(0x183c), v1833

    Begin block 0x1838
    prev=[0x182b], succ=[]
    =================================
    0x1838: v1838(0x0) = CONST 
    0x183b: REVERT v1838(0x0), v1838(0x0)

    Begin block 0x183c
    prev=[0x182b], succ=[0x64d]
    =================================
    0x1840: v1840(0x40) = CONST 
    0x1842: v1842 = MLOAD v1840(0x40)
    0x1844: v1844 = MLOAD v1842
    0x184c: JUMP v638(0x64d)

    Begin block 0x64d
    prev=[0x183c], succ=[]
    =================================
    0x64e: v64e(0x40) = CONST 
    0x650: v650 = MLOAD v64e(0x40)
    0x653: v653(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x668: v668 = AND v653(0xffffffffffffffffffffffffffffffffffffffff), v1844
    0x669: v669(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x67e: v67e = AND v669(0xffffffffffffffffffffffffffffffffffffffff), v668
    0x680: MSTORE v650, v67e
    0x681: v681(0x20) = CONST 
    0x683: v683 = ADD v681(0x20), v650
    0x687: v687(0x40) = CONST 
    0x689: v689 = MLOAD v687(0x40)
    0x68c: v68c(0x20) = SUB v683, v689
    0x68e: RETURN v689, v68c(0x20)

}

function balanceOf(address)() public {
    Begin block 0x68f
    prev=[], succ=[0x696, 0x69a]
    =================================
    0x690: v690 = CALLVALUE 
    0x691: v691 = ISZERO v690
    0x692: v692(0x69a) = CONST 
    0x695: JUMPI v692(0x69a), v691

    Begin block 0x696
    prev=[0x68f], succ=[]
    =================================
    0x696: v696(0x0) = CONST 
    0x699: REVERT v696(0x0), v696(0x0)

    Begin block 0x69a
    prev=[0x68f], succ=[0x184d]
    =================================
    0x69b: v69b(0x6c6) = CONST 
    0x69e: v69e(0x4) = CONST 
    0x6a2: v6a2 = CALLDATALOAD v69e(0x4)
    0x6a3: v6a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6b8: v6b8 = AND v6a3(0xffffffffffffffffffffffffffffffffffffffff), v6a2
    0x6ba: v6ba(0x20) = CONST 
    0x6bc: v6bc(0x24) = ADD v6ba(0x20), v69e(0x4)
    0x6c2: v6c2(0x184d) = CONST 
    0x6c5: JUMP v6c2(0x184d)

    Begin block 0x184d
    prev=[0x69a], succ=[0x18ae, 0x18fe]
    =================================
    0x184e: v184e(0x0) = CONST 
    0x1850: v1850(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77) = CONST 
    0x1865: v1865(0xad7f02b5) = CONST 
    0x186a: v186a(0x2) = CONST 
    0x186d: v186d(0x0) = CONST 
    0x186f: v186f(0x40) = CONST 
    0x1871: v1871 = MLOAD v186f(0x40)
    0x1872: v1872(0x20) = CONST 
    0x1874: v1874 = ADD v1872(0x20), v1871
    0x1875: MSTORE v1874, v186d(0x0)
    0x1876: v1876(0x40) = CONST 
    0x1878: v1878 = MLOAD v1876(0x40)
    0x187a: v187a(0xffffffff) = CONST 
    0x187f: v187f(0xad7f02b5) = AND v187a(0xffffffff), v1865(0xad7f02b5)
    0x1880: v1880(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x189e: v189e(0xad7f02b500000000000000000000000000000000000000000000000000000000) = MUL v1880(0x100000000000000000000000000000000000000000000000000000000), v187f(0xad7f02b5)
    0x18a0: MSTORE v1878, v189e(0xad7f02b500000000000000000000000000000000000000000000000000000000)
    0x18a1: v18a1(0x4) = CONST 
    0x18a3: v18a3 = ADD v18a1(0x4), v1878
    0x18a6: v18a6(0x10) = CONST 
    0x18a9: v18a9(0x0) = ISZERO v18a6(0x10)
    0x18aa: v18aa(0x18fe) = CONST 
    0x18ad: JUMPI v18aa(0x18fe), v18a9(0x0)

    Begin block 0x18ae
    prev=[0x184d], succ=[0x18b4]
    =================================
    0x18ae: v18ae(0x20) = CONST 
    0x18b0: v18b0(0x200) = MUL v18ae(0x20), v18a6(0x10)
    0x18b2: v18b2 = ADD v18a3, v18b0(0x200)

    Begin block 0x18b4
    prev=[0x18ae, 0x18b4], succ=[0x18fe, 0x18b4]
    =================================
    0x18b4_0x0: v18b4_0 = PHI v18a3, v18f1
    0x18b4_0x1: v18b4_1 = PHI v186a(0x2), v18f5
    0x18b6: v18b6(0x0) = CONST 
    0x18b9: v18b9 = SLOAD v18b4_1
    0x18bb: v18bb(0x100) = CONST 
    0x18be: v18be(0x1) = EXP v18bb(0x100), v18b6(0x0)
    0x18c0: v18c0 = DIV v18b9, v18be(0x1)
    0x18c1: v18c1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18d6: v18d6 = AND v18c1(0xffffffffffffffffffffffffffffffffffffffff), v18c0
    0x18d7: v18d7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18ec: v18ec = AND v18d7(0xffffffffffffffffffffffffffffffffffffffff), v18d6
    0x18ee: MSTORE v18b4_0, v18ec
    0x18ef: v18ef(0x20) = CONST 
    0x18f1: v18f1 = ADD v18ef(0x20), v18b4_0
    0x18f3: v18f3(0x1) = CONST 
    0x18f5: v18f5 = ADD v18f3(0x1), v18b4_1
    0x18f9: v18f9 = GT v18b2, v18f1
    0x18fa: v18fa(0x18b4) = CONST 
    0x18fd: JUMPI v18fa(0x18b4), v18f9

    Begin block 0x18fe
    prev=[0x184d, 0x18b4], succ=[0x1949, 0x194d]
    =================================
    0x18fe_0x2: v18fe_2 = PHI v18a3, v18b2
    0x1902: v1902(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1917: v1917 = AND v1902(0xffffffffffffffffffffffffffffffffffffffff), v6b8
    0x1918: v1918(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x192d: v192d = AND v1918(0xffffffffffffffffffffffffffffffffffffffff), v1917
    0x192f: MSTORE v18fe_2, v192d
    0x1930: v1930(0x20) = CONST 
    0x1932: v1932 = ADD v1930(0x20), v18fe_2
    0x1937: v1937(0x20) = CONST 
    0x1939: v1939(0x40) = CONST 
    0x193b: v193b = MLOAD v1939(0x40)
    0x193e: v193e = SUB v1932, v193b
    0x1942: v1942 = EXTCODESIZE v1850(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77)
    0x1943: v1943 = ISZERO v1942
    0x1944: v1944 = ISZERO v1943
    0x1945: v1945(0x194d) = CONST 
    0x1948: JUMPI v1945(0x194d), v1944

    Begin block 0x1949
    prev=[0x18fe], succ=[]
    =================================
    0x1949: v1949(0x0) = CONST 
    0x194c: REVERT v1949(0x0), v1949(0x0)

    Begin block 0x194d
    prev=[0x18fe], succ=[0x195a, 0x195e]
    =================================
    0x194e: v194e(0x2c6) = CONST 
    0x1951: v1951 = GAS 
    0x1952: v1952 = SUB v1951, v194e(0x2c6)
    0x1953: v1953 = DELEGATECALL v1952, v1850(0xe5568ad7f29e67890bfe8f76a0f50b4113a62c77), v193b, v193e, v193b, v1937(0x20)
    0x1954: v1954 = ISZERO v1953
    0x1955: v1955 = ISZERO v1954
    0x1956: v1956(0x195e) = CONST 
    0x1959: JUMPI v1956(0x195e), v1955

    Begin block 0x195a
    prev=[0x194d], succ=[]
    =================================
    0x195a: v195a(0x0) = CONST 
    0x195d: REVERT v195a(0x0), v195a(0x0)

    Begin block 0x195e
    prev=[0x194d], succ=[0x6c6]
    =================================
    0x1962: v1962(0x40) = CONST 
    0x1964: v1964 = MLOAD v1962(0x40)
    0x1966: v1966 = MLOAD v1964
    0x196e: JUMP v69b(0x6c6)

    Begin block 0x6c6
    prev=[0x195e], succ=[]
    =================================
    0x6c7: v6c7(0x40) = CONST 
    0x6c9: v6c9 = MLOAD v6c7(0x40)
    0x6cd: MSTORE v6c9, v1966
    0x6ce: v6ce(0x20) = CONST 
    0x6d0: v6d0 = ADD v6ce(0x20), v6c9
    0x6d4: v6d4(0x40) = CONST 
    0x6d6: v6d6 = MLOAD v6d4(0x40)
    0x6d9: v6d9(0x20) = SUB v6d0, v6d6
    0x6db: RETURN v6d6, v6d9(0x20)

}

function pause()() public {
    Begin block 0x6dc
    prev=[], succ=[0x6e3, 0x6e7]
    =================================
    0x6dd: v6dd = CALLVALUE 
    0x6de: v6de = ISZERO v6dd
    0x6df: v6df(0x6e7) = CONST 
    0x6e2: JUMPI v6df(0x6e7), v6de

    Begin block 0x6e3
    prev=[0x6dc], succ=[]
    =================================
    0x6e3: v6e3(0x0) = CONST 
    0x6e6: REVERT v6e3(0x0), v6e3(0x0)

    Begin block 0x6e7
    prev=[0x6dc], succ=[0x196f]
    =================================
    0x6e8: v6e8(0x6ef) = CONST 
    0x6eb: v6eb(0x196f) = CONST 
    0x6ee: JUMP v6eb(0x196f)

    Begin block 0x196f
    prev=[0x6e7], succ=[0x1a17, 0x19c5]
    =================================
    0x1970: v1970(0x0) = CONST 
    0x1974: v1974 = SLOAD v1970(0x0)
    0x1976: v1976(0x100) = CONST 
    0x1979: v1979(0x1) = EXP v1976(0x100), v1970(0x0)
    0x197b: v197b = DIV v1974, v1979(0x1)
    0x197c: v197c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1991: v1991 = AND v197c(0xffffffffffffffffffffffffffffffffffffffff), v197b
    0x1992: v1992(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19a7: v19a7 = AND v1992(0xffffffffffffffffffffffffffffffffffffffff), v1991
    0x19a8: v19a8 = CALLER 
    0x19a9: v19a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19be: v19be = AND v19a9(0xffffffffffffffffffffffffffffffffffffffff), v19a8
    0x19bf: v19bf = EQ v19be, v19a7
    0x19c1: v19c1(0x1a17) = CONST 
    0x19c4: JUMPI v19c1(0x1a17), v19bf

    Begin block 0x1a17
    prev=[0x196f, 0x19c5], succ=[0x1a1e, 0x1a22]
    =================================
    0x1a17_0x0: v1a17_0 = PHI v19bf, v1a16
    0x1a18: v1a18 = ISZERO v1a17_0
    0x1a19: v1a19 = ISZERO v1a18
    0x1a1a: v1a1a(0x1a22) = CONST 
    0x1a1d: JUMPI v1a1a(0x1a22), v1a19

    Begin block 0x1a1e
    prev=[0x1a17], succ=[]
    =================================
    0x1a1e: v1a1e(0x0) = CONST 
    0x1a21: REVERT v1a1e(0x0), v1a1e(0x0)

    Begin block 0x1a22
    prev=[0x1a17], succ=[0x6ef]
    =================================
    0x1a23: v1a23(0x1) = CONST 
    0x1a25: v1a25(0x12) = CONST 
    0x1a27: v1a27(0x0) = CONST 
    0x1a29: v1a29(0x100) = CONST 
    0x1a2c: v1a2c(0x1) = EXP v1a29(0x100), v1a27(0x0)
    0x1a2e: v1a2e = SLOAD v1a25(0x12)
    0x1a30: v1a30(0xff) = CONST 
    0x1a32: v1a32(0xff) = MUL v1a30(0xff), v1a2c(0x1)
    0x1a33: v1a33(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1a32(0xff)
    0x1a34: v1a34 = AND v1a33(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1a2e
    0x1a37: v1a37(0x0) = ISZERO v1a23(0x1)
    0x1a38: v1a38(0x1) = ISZERO v1a37(0x0)
    0x1a39: v1a39(0x1) = MUL v1a38(0x1), v1a2c(0x1)
    0x1a3a: v1a3a = OR v1a39(0x1), v1a34
    0x1a3c: SSTORE v1a25(0x12), v1a3a
    0x1a3e: JUMP v6e8(0x6ef)

    Begin block 0x6ef
    prev=[0x1a22], succ=[]
    =================================
    0x6f0: STOP 

    Begin block 0x19c5
    prev=[0x196f], succ=[0x1a17]
    =================================
    0x19c6: v19c6(0x1) = CONST 
    0x19c8: v19c8(0x0) = CONST 
    0x19cb: v19cb = SLOAD v19c6(0x1)
    0x19cd: v19cd(0x100) = CONST 
    0x19d0: v19d0(0x1) = EXP v19cd(0x100), v19c8(0x0)
    0x19d2: v19d2 = DIV v19cb, v19d0(0x1)
    0x19d3: v19d3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19e8: v19e8 = AND v19d3(0xffffffffffffffffffffffffffffffffffffffff), v19d2
    0x19e9: v19e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19fe: v19fe = AND v19e9(0xffffffffffffffffffffffffffffffffffffffff), v19e8
    0x19ff: v19ff = CALLER 
    0x1a00: v1a00(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a15: v1a15 = AND v1a00(0xffffffffffffffffffffffffffffffffffffffff), v19ff
    0x1a16: v1a16 = EQ v1a15, v19fe

}

function updateRegionPixelPrice(uint256,uint256)() public {
    Begin block 0x6f1
    prev=[], succ=[0x1a3fB0x6f1]
    =================================
    0x6f2: v6f2(0x710) = CONST 
    0x6f5: v6f5(0x4) = CONST 
    0x6f9: v6f9 = CALLDATALOAD v6f5(0x4)
    0x6fb: v6fb(0x20) = CONST 
    0x6fd: v6fd(0x24) = ADD v6fb(0x20), v6f5(0x4)
    0x702: v702 = CALLDATALOAD v6fd(0x24)
    0x704: v704(0x20) = CONST 
    0x706: v706(0x44) = ADD v704(0x20), v6fd(0x24)
    0x70c: v70c(0x1a3f) = CONST 
    0x70f: JUMP v70c(0x1a3f), v702, v6f9, v6f2(0x710)

    Begin block 0x1a3fB0x6f1
    prev=[0x6f1], succ=[0x1a68B0x6f1, 0x1a57B0x6f1]
    =================================
    0x1a40S0x6f1: v1a40V6f1(0x12) = CONST 
    0x1a42S0x6f1: v1a42V6f1(0x0) = CONST 
    0x1a45S0x6f1: v1a45V6f1 = SLOAD v1a40V6f1(0x12)
    0x1a47S0x6f1: v1a47V6f1(0x100) = CONST 
    0x1a4aS0x6f1: v1a4aV6f1(0x1) = EXP v1a47V6f1(0x100), v1a42V6f1(0x0)
    0x1a4cS0x6f1: v1a4cV6f1 = DIV v1a45V6f1, v1a4aV6f1(0x1)
    0x1a4dS0x6f1: v1a4dV6f1(0xff) = CONST 
    0x1a4fS0x6f1: v1a4fV6f1 = AND v1a4dV6f1(0xff), v1a4cV6f1
    0x1a50S0x6f1: v1a50V6f1 = ISZERO v1a4fV6f1
    0x1a52S0x6f1: v1a52V6f1 = ISZERO v1a50V6f1
    0x1a53S0x6f1: v1a53V6f1(0x1a68) = CONST 
    0x1a56S0x6f1: JUMPI v1a53V6f1(0x1a68), v1a52V6f1

    Begin block 0x1a68B0x6f1
    prev=[0x1a3fB0x6f1, 0x1a57B0x6f1], succ=[0x1a6fB0x6f1, 0x1a73B0x6f1]
    =================================
    0x1a68_0x0S0x6f1: v1a68_0V6f1 = PHI v1a50V6f1, v1a67V6f1
    0x1a69S0x6f1: v1a69V6f1 = ISZERO v1a68_0V6f1
    0x1a6aS0x6f1: v1a6aV6f1 = ISZERO v1a69V6f1
    0x1a6bS0x6f1: v1a6bV6f1(0x1a73) = CONST 
    0x1a6eS0x6f1: JUMPI v1a6bV6f1(0x1a73), v1a6aV6f1

    Begin block 0x1a6fB0x6f1
    prev=[0x1a68B0x6f1], succ=[]
    =================================
    0x1a6fS0x6f1: v1a6fV6f1(0x0) = CONST 
    0x1a72S0x6f1: REVERT v1a6fV6f1(0x0), v1a6fV6f1(0x0)

    Begin block 0x1a73B0x6f1
    prev=[0x1a68B0x6f1], succ=[0x1acaB0x6f1, 0x1b1aB0x6f1]
    =================================
    0x1a74S0x6f1: v1a74V6f1(0xd8479c546b80ce91916c7800c1840bd6446b06ce) = CONST 
    0x1a89S0x6f1: v1a89V6f1(0x42f88548) = CONST 
    0x1a8eS0x6f1: v1a8eV6f1(0x2) = CONST 
    0x1a92S0x6f1: v1a92V6f1(0x40) = CONST 
    0x1a94S0x6f1: v1a94V6f1 = MLOAD v1a92V6f1(0x40)
    0x1a96S0x6f1: v1a96V6f1(0xffffffff) = CONST 
    0x1a9bS0x6f1: v1a9bV6f1(0x42f88548) = AND v1a96V6f1(0xffffffff), v1a89V6f1(0x42f88548)
    0x1a9cS0x6f1: v1a9cV6f1(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x1abaS0x6f1: v1abaV6f1(0x42f8854800000000000000000000000000000000000000000000000000000000) = MUL v1a9cV6f1(0x100000000000000000000000000000000000000000000000000000000), v1a9bV6f1(0x42f88548)
    0x1abcS0x6f1: MSTORE v1a94V6f1, v1abaV6f1(0x42f8854800000000000000000000000000000000000000000000000000000000)
    0x1abdS0x6f1: v1abdV6f1(0x4) = CONST 
    0x1abfS0x6f1: v1abfV6f1 = ADD v1abdV6f1(0x4), v1a94V6f1
    0x1ac2S0x6f1: v1ac2V6f1(0x10) = CONST 
    0x1ac5S0x6f1: v1ac5V6f1(0x0) = ISZERO v1ac2V6f1(0x10)
    0x1ac6S0x6f1: v1ac6V6f1(0x1b1a) = CONST 
    0x1ac9S0x6f1: JUMPI v1ac6V6f1(0x1b1a), v1ac5V6f1(0x0)

    Begin block 0x1acaB0x6f1
    prev=[0x1a73B0x6f1], succ=[0x1ad0B0x6f1]
    =================================
    0x1acaS0x6f1: v1acaV6f1(0x20) = CONST 
    0x1accS0x6f1: v1accV6f1(0x200) = MUL v1acaV6f1(0x20), v1ac2V6f1(0x10)
    0x1aceS0x6f1: v1aceV6f1 = ADD v1abfV6f1, v1accV6f1(0x200)

    Begin block 0x1ad0B0x6f1
    prev=[0x1acaB0x6f1, 0x1ad0B0x6f1], succ=[0x1b1aB0x6f1, 0x1ad0B0x6f1]
    =================================
    0x1ad0_0x0S0x6f1: v1ad0_0V6f1 = PHI v1abfV6f1, v1b0dV6f1
    0x1ad0_0x1S0x6f1: v1ad0_1V6f1 = PHI v1a8eV6f1(0x2), v1b11V6f1
    0x1ad2S0x6f1: v1ad2V6f1(0x0) = CONST 
    0x1ad5S0x6f1: v1ad5V6f1 = SLOAD v1ad0_1V6f1
    0x1ad7S0x6f1: v1ad7V6f1(0x100) = CONST 
    0x1adaS0x6f1: v1adaV6f1(0x1) = EXP v1ad7V6f1(0x100), v1ad2V6f1(0x0)
    0x1adcS0x6f1: v1adcV6f1 = DIV v1ad5V6f1, v1adaV6f1(0x1)
    0x1addS0x6f1: v1addV6f1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1af2S0x6f1: v1af2V6f1 = AND v1addV6f1(0xffffffffffffffffffffffffffffffffffffffff), v1adcV6f1
    0x1af3S0x6f1: v1af3V6f1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b08S0x6f1: v1b08V6f1 = AND v1af3V6f1(0xffffffffffffffffffffffffffffffffffffffff), v1af2V6f1
    0x1b0aS0x6f1: MSTORE v1ad0_0V6f1, v1b08V6f1
    0x1b0bS0x6f1: v1b0bV6f1(0x20) = CONST 
    0x1b0dS0x6f1: v1b0dV6f1 = ADD v1b0bV6f1(0x20), v1ad0_0V6f1
    0x1b0fS0x6f1: v1b0fV6f1(0x1) = CONST 
    0x1b11S0x6f1: v1b11V6f1 = ADD v1b0fV6f1(0x1), v1ad0_1V6f1
    0x1b15S0x6f1: v1b15V6f1 = GT v1aceV6f1, v1b0dV6f1
    0x1b16S0x6f1: v1b16V6f1(0x1ad0) = CONST 
    0x1b19S0x6f1: JUMPI v1b16V6f1(0x1ad0), v1b15V6f1

    Begin block 0x1b1aB0x6f1
    prev=[0x1a73B0x6f1, 0x1ad0B0x6f1], succ=[0x1b40B0x6f1, 0x1b44B0x6f1]
    =================================
    0x1b1a_0x2S0x6f1: v1b1a_2V6f1 = PHI v1aceV6f1, v1abfV6f1
    0x1b1fS0x6f1: MSTORE v1b1a_2V6f1, v6f9
    0x1b20S0x6f1: v1b20V6f1(0x20) = CONST 
    0x1b22S0x6f1: v1b22V6f1 = ADD v1b20V6f1(0x20), v1b1a_2V6f1
    0x1b25S0x6f1: MSTORE v1b22V6f1, v702
    0x1b26S0x6f1: v1b26V6f1(0x20) = CONST 
    0x1b28S0x6f1: v1b28V6f1 = ADD v1b26V6f1(0x20), v1b22V6f1
    0x1b2eS0x6f1: v1b2eV6f1(0x0) = CONST 
    0x1b30S0x6f1: v1b30V6f1(0x40) = CONST 
    0x1b32S0x6f1: v1b32V6f1 = MLOAD v1b30V6f1(0x40)
    0x1b35S0x6f1: v1b35V6f1 = SUB v1b28V6f1, v1b32V6f1
    0x1b39S0x6f1: v1b39V6f1 = EXTCODESIZE v1a74V6f1(0xd8479c546b80ce91916c7800c1840bd6446b06ce)
    0x1b3aS0x6f1: v1b3aV6f1 = ISZERO v1b39V6f1
    0x1b3bS0x6f1: v1b3bV6f1 = ISZERO v1b3aV6f1
    0x1b3cS0x6f1: v1b3cV6f1(0x1b44) = CONST 
    0x1b3fS0x6f1: JUMPI v1b3cV6f1(0x1b44), v1b3bV6f1

    Begin block 0x1b40B0x6f1
    prev=[0x1b1aB0x6f1], succ=[]
    =================================
    0x1b40S0x6f1: v1b40V6f1(0x0) = CONST 
    0x1b43S0x6f1: REVERT v1b40V6f1(0x0), v1b40V6f1(0x0)

    Begin block 0x1b44B0x6f1
    prev=[0x1b1aB0x6f1], succ=[0x1b51B0x6f1, 0x1b55B0x6f1]
    =================================
    0x1b45S0x6f1: v1b45V6f1(0x2c6) = CONST 
    0x1b48S0x6f1: v1b48V6f1 = GAS 
    0x1b49S0x6f1: v1b49V6f1 = SUB v1b48V6f1, v1b45V6f1(0x2c6)
    0x1b4aS0x6f1: v1b4aV6f1 = DELEGATECALL v1b49V6f1, v1a74V6f1(0xd8479c546b80ce91916c7800c1840bd6446b06ce), v1b32V6f1, v1b35V6f1, v1b32V6f1, v1b2eV6f1(0x0)
    0x1b4bS0x6f1: v1b4bV6f1 = ISZERO v1b4aV6f1
    0x1b4cS0x6f1: v1b4cV6f1 = ISZERO v1b4bV6f1
    0x1b4dS0x6f1: v1b4dV6f1(0x1b55) = CONST 
    0x1b50S0x6f1: JUMPI v1b4dV6f1(0x1b55), v1b4cV6f1

    Begin block 0x1b51B0x6f1
    prev=[0x1b44B0x6f1], succ=[]
    =================================
    0x1b51S0x6f1: v1b51V6f1(0x0) = CONST 
    0x1b54S0x6f1: REVERT v1b51V6f1(0x0), v1b51V6f1(0x0)

    Begin block 0x1b55B0x6f1
    prev=[0x1b44B0x6f1], succ=[0x710]
    =================================
    0x1b5bS0x6f1: JUMP v6f2(0x710)

    Begin block 0x710
    prev=[0x1b55B0x6f1], succ=[]
    =================================
    0x711: STOP 

    Begin block 0x1a57B0x6f1
    prev=[0x1a3fB0x6f1], succ=[0x1a68B0x6f1]
    =================================
    0x1a58S0x6f1: v1a58V6f1(0x12) = CONST 
    0x1a5aS0x6f1: v1a5aV6f1(0x1) = CONST 
    0x1a5dS0x6f1: v1a5dV6f1 = SLOAD v1a58V6f1(0x12)
    0x1a5fS0x6f1: v1a5fV6f1(0x100) = CONST 
    0x1a62S0x6f1: v1a62V6f1(0x100) = EXP v1a5fV6f1(0x100), v1a5aV6f1(0x1)
    0x1a64S0x6f1: v1a64V6f1 = DIV v1a5dV6f1, v1a62V6f1(0x100)
    0x1a65S0x6f1: v1a65V6f1(0xff) = CONST 
    0x1a67S0x6f1: v1a67V6f1 = AND v1a65V6f1(0xff), v1a64V6f1

}

function ownerAddress()() public {
    Begin block 0x712
    prev=[], succ=[0x719, 0x71d]
    =================================
    0x713: v713 = CALLVALUE 
    0x714: v714 = ISZERO v713
    0x715: v715(0x71d) = CONST 
    0x718: JUMPI v715(0x71d), v714

    Begin block 0x719
    prev=[0x712], succ=[]
    =================================
    0x719: v719(0x0) = CONST 
    0x71c: REVERT v719(0x0), v719(0x0)

    Begin block 0x71d
    prev=[0x712], succ=[0x1b5c]
    =================================
    0x71e: v71e(0x725) = CONST 
    0x721: v721(0x1b5c) = CONST 
    0x724: JUMP v721(0x1b5c)

    Begin block 0x1b5c
    prev=[0x71d], succ=[0x725]
    =================================
    0x1b5d: v1b5d(0x0) = CONST 
    0x1b61: v1b61 = SLOAD v1b5d(0x0)
    0x1b63: v1b63(0x100) = CONST 
    0x1b66: v1b66(0x1) = EXP v1b63(0x100), v1b5d(0x0)
    0x1b68: v1b68 = DIV v1b61, v1b66(0x1)
    0x1b69: v1b69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b7e: v1b7e = AND v1b69(0xffffffffffffffffffffffffffffffffffffffff), v1b68
    0x1b80: JUMP v71e(0x725)

    Begin block 0x725
    prev=[0x1b5c], succ=[]
    =================================
    0x726: v726(0x40) = CONST 
    0x728: v728 = MLOAD v726(0x40)
    0x72b: v72b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x740: v740 = AND v72b(0xffffffffffffffffffffffffffffffffffffffff), v1b7e
    0x741: v741(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x756: v756 = AND v741(0xffffffffffffffffffffffffffffffffffffffff), v740
    0x758: MSTORE v728, v756
    0x759: v759(0x20) = CONST 
    0x75b: v75b = ADD v759(0x20), v728
    0x75f: v75f(0x40) = CONST 
    0x761: v761 = MLOAD v75f(0x40)
    0x764: v764(0x20) = SUB v75b, v761
    0x766: RETURN v761, v764(0x20)

}

function symbol()() public {
    Begin block 0x767
    prev=[], succ=[0x76e, 0x772]
    =================================
    0x768: v768 = CALLVALUE 
    0x769: v769 = ISZERO v768
    0x76a: v76a(0x772) = CONST 
    0x76d: JUMPI v76a(0x772), v769

    Begin block 0x76e
    prev=[0x767], succ=[]
    =================================
    0x76e: v76e(0x0) = CONST 
    0x771: REVERT v76e(0x0), v76e(0x0)

    Begin block 0x772
    prev=[0x767], succ=[0x1b81]
    =================================
    0x773: v773(0x77a) = CONST 
    0x776: v776(0x1b81) = CONST 
    0x779: JUMP v776(0x1b81)

    Begin block 0x1b81
    prev=[0x772], succ=[0x2a1bB0x1b81]
    =================================
    0x1b82: v1b82(0x1b89) = CONST 
    0x1b85: v1b85(0x2a1b) = CONST 
    0x1b88: JUMP v1b85(0x2a1b)

    Begin block 0x2a1bB0x1b81
    prev=[0x1b81], succ=[0x1b89]
    =================================
    0x2a1cS0x1b81: v2a1cV1b81(0x20) = CONST 
    0x2a1eS0x1b81: v2a1eV1b81(0x40) = CONST 
    0x2a20S0x1b81: v2a20V1b81 = MLOAD v2a1eV1b81(0x40)
    0x2a23S0x1b81: v2a23V1b81 = ADD v2a20V1b81, v2a1cV1b81(0x20)
    0x2a24S0x1b81: v2a24V1b81(0x40) = CONST 
    0x2a26S0x1b81: MSTORE v2a24V1b81(0x40), v2a23V1b81
    0x2a28S0x1b81: v2a28V1b81(0x0) = CONST 
    0x2a2bS0x1b81: MSTORE v2a20V1b81, v2a28V1b81(0x0)
    0x2a2eS0x1b81: JUMP v1b82(0x1b89)

    Begin block 0x1b89
    prev=[0x2a1bB0x1b81], succ=[0x77a]
    =================================
    0x1b8a: v1b8a(0x40) = CONST 
    0x1b8d: v1b8d = MLOAD v1b8a(0x40)
    0x1b90: v1b90 = ADD v1b8d, v1b8a(0x40)
    0x1b91: v1b91(0x40) = CONST 
    0x1b93: MSTORE v1b91(0x40), v1b90
    0x1b95: v1b95(0x3) = CONST 
    0x1b98: MSTORE v1b8d, v1b95(0x3)
    0x1b99: v1b99(0x20) = CONST 
    0x1b9b: v1b9b = ADD v1b99(0x20), v1b8d
    0x1b9c: v1b9c(0x4244500000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1bbe: MSTORE v1b9b, v1b9c(0x4244500000000000000000000000000000000000000000000000000000000000)
    0x1bc3: JUMP v773(0x77a)

    Begin block 0x77a
    prev=[0x1b89], succ=[0x79f]
    =================================
    0x77b: v77b(0x40) = CONST 
    0x77d: v77d = MLOAD v77b(0x40)
    0x780: v780(0x20) = CONST 
    0x782: v782 = ADD v780(0x20), v77d
    0x785: v785(0x20) = SUB v782, v77d
    0x787: MSTORE v77d, v785(0x20)
    0x78b: v78b(0x3) = MLOAD v1b8d
    0x78d: MSTORE v782, v78b(0x3)
    0x78e: v78e(0x20) = CONST 
    0x790: v790 = ADD v78e(0x20), v782
    0x794: v794(0x3) = MLOAD v1b8d
    0x796: v796(0x20) = CONST 
    0x798: v798 = ADD v796(0x20), v1b8d
    0x79d: v79d(0x0) = CONST 

    Begin block 0x79f
    prev=[0x77a, 0x7a8], succ=[0x7ba, 0x7a8]
    =================================
    0x79f_0x0: v79f_0 = PHI v79d(0x0), v7b3
    0x7a2: v7a2 = LT v79f_0, v794(0x3)
    0x7a3: v7a3 = ISZERO v7a2
    0x7a4: v7a4(0x7ba) = CONST 
    0x7a7: JUMPI v7a4(0x7ba), v7a3

    Begin block 0x7ba
    prev=[0x79f], succ=[0x7e7, 0x7ce]
    =================================
    0x7c3: v7c3 = ADD v794(0x3), v790
    0x7c5: v7c5(0x1f) = CONST 
    0x7c7: v7c7(0x3) = AND v7c5(0x1f), v794(0x3)
    0x7c9: v7c9 = ISZERO v7c7(0x3)
    0x7ca: v7ca(0x7e7) = CONST 
    0x7cd: JUMPI v7ca(0x7e7), v7c9

    Begin block 0x7e7
    prev=[0x7ba, 0x7ce], succ=[]
    =================================
    0x7e7_0x1: v7e7_1 = PHI v7c3, v7e4
    0x7ed: v7ed(0x40) = CONST 
    0x7ef: v7ef = MLOAD v7ed(0x40)
    0x7f2: v7f2 = SUB v7e7_1, v7ef
    0x7f4: RETURN v7ef, v7f2

    Begin block 0x7ce
    prev=[0x7ba], succ=[0x7e7]
    =================================
    0x7d0: v7d0 = SUB v7c3, v7c7(0x3)
    0x7d2: v7d2 = MLOAD v7d0
    0x7d3: v7d3(0x1) = CONST 
    0x7d6: v7d6(0x20) = CONST 
    0x7d8: v7d8(0x1d) = SUB v7d6(0x20), v7c7(0x3)
    0x7d9: v7d9(0x100) = CONST 
    0x7dc: v7dc(0x10000000000000000000000000000000000000000000000000000000000) = EXP v7d9(0x100), v7d8(0x1d)
    0x7dd: v7dd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v7dc(0x10000000000000000000000000000000000000000000000000000000000), v7d3(0x1)
    0x7de: v7de = NOT v7dd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x7df: v7df = AND v7de, v7d2
    0x7e1: MSTORE v7d0, v7df
    0x7e2: v7e2(0x20) = CONST 
    0x7e4: v7e4 = ADD v7e2(0x20), v7d0

    Begin block 0x7a8
    prev=[0x79f], succ=[0x79f]
    =================================
    0x7a8_0x0: v7a8_0 = PHI v79d(0x0), v7b3
    0x7aa: v7aa = ADD v798, v7a8_0
    0x7ab: v7ab = MLOAD v7aa
    0x7ae: v7ae = ADD v790, v7a8_0
    0x7af: MSTORE v7ae, v7ab
    0x7b0: v7b0(0x20) = CONST 
    0x7b3: v7b3 = ADD v7a8_0, v7b0(0x20)
    0x7b6: v7b6(0x79f) = CONST 
    0x7b9: JUMP v7b6(0x79f)

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
    prev=[0x7f5], succ=[0x1bc4]
    =================================
    0x801: v801(0x816) = CONST 
    0x804: v804(0x4) = CONST 
    0x808: v808 = CALLDATALOAD v804(0x4)
    0x80a: v80a(0x20) = CONST 
    0x80c: v80c(0x24) = ADD v80a(0x20), v804(0x4)
    0x812: v812(0x1bc4) = CONST 
    0x815: JUMP v812(0x1bc4)

    Begin block 0x1bc4
    prev=[0x800], succ=[0x2a1bB0x1bc4]
    =================================
    0x1bc5: v1bc5(0x1bcc) = CONST 
    0x1bc8: v1bc8(0x2a1b) = CONST 
    0x1bcb: JUMP v1bc8(0x2a1b)

    Begin block 0x2a1bB0x1bc4
    prev=[0x1bc4], succ=[0x1bcc]
    =================================
    0x2a1cS0x1bc4: v2a1cV1bc4(0x20) = CONST 
    0x2a1eS0x1bc4: v2a1eV1bc4(0x40) = CONST 
    0x2a20S0x1bc4: v2a20V1bc4 = MLOAD v2a1eV1bc4(0x40)
    0x2a23S0x1bc4: v2a23V1bc4 = ADD v2a20V1bc4, v2a1cV1bc4(0x20)
    0x2a24S0x1bc4: v2a24V1bc4(0x40) = CONST 
    0x2a26S0x1bc4: MSTORE v2a24V1bc4(0x40), v2a23V1bc4
    0x2a28S0x1bc4: v2a28V1bc4(0x0) = CONST 
    0x2a2bS0x1bc4: MSTORE v2a20V1bc4, v2a28V1bc4(0x0)
    0x2a2eS0x1bc4: JUMP v1bc5(0x1bcc)

    Begin block 0x1bcc
    prev=[0x2a1bB0x1bc4], succ=[0x2a07B0x1bcc]
    =================================
    0x1bcd: v1bcd(0x1bd4) = CONST 
    0x1bd0: v1bd0(0x2a07) = CONST 
    0x1bd3: JUMP v1bd0(0x2a07)

    Begin block 0x2a07B0x1bcc
    prev=[0x1bcc], succ=[0x1bd4]
    =================================
    0x2a08S0x1bcc: v2a08V1bcc(0x20) = CONST 
    0x2a0aS0x1bcc: v2a0aV1bcc(0x40) = CONST 
    0x2a0cS0x1bcc: v2a0cV1bcc = MLOAD v2a0aV1bcc(0x40)
    0x2a0fS0x1bcc: v2a0fV1bcc = ADD v2a0cV1bcc, v2a08V1bcc(0x20)
    0x2a10S0x1bcc: v2a10V1bcc(0x40) = CONST 
    0x2a12S0x1bcc: MSTORE v2a10V1bcc(0x40), v2a0fV1bcc
    0x2a14S0x1bcc: v2a14V1bcc(0x0) = CONST 
    0x2a17S0x1bcc: MSTORE v2a0cV1bcc, v2a14V1bcc(0x0)
    0x2a1aS0x1bcc: JUMP v1bcd(0x1bd4)

    Begin block 0x1bd4
    prev=[0x2a07B0x1bcc], succ=[0x1c45, 0x1c46]
    =================================
    0x1bd5: v1bd5(0x60) = CONST 
    0x1bd7: v1bd7(0x40) = CONST 
    0x1bd9: v1bd9 = MLOAD v1bd7(0x40)
    0x1bdc: v1bdc = ADD v1bd9, v1bd5(0x60)
    0x1bdd: v1bdd(0x40) = CONST 
    0x1bdf: MSTORE v1bdd(0x40), v1bdc
    0x1be1: v1be1(0x2d) = CONST 
    0x1be4: MSTORE v1bd9, v1be1(0x2d)
    0x1be5: v1be5(0x20) = CONST 
    0x1be7: v1be7 = ADD v1be5(0x20), v1bd9
    0x1be8: v1be8(0x68747470733a2f2f7777772e62696c6c696f6e646f6c6c617270696374757265) = CONST 
    0x1c0a: MSTORE v1be7, v1be8(0x68747470733a2f2f7777772e62696c6c696f6e646f6c6c617270696374757265)
    0x1c0b: v1c0b(0x20) = CONST 
    0x1c0d: v1c0d = ADD v1c0b(0x20), v1be7
    0x1c0e: v1c0e(0x2e636f6d2f233030303030303000000000000000000000000000000000000000) = CONST 
    0x1c30: MSTORE v1c0d, v1c0e(0x2e636f6d2f233030303030303000000000000000000000000000000000000000)
    0x1c37: v1c37(0xa) = CONST 
    0x1c39: v1c39(0xf4240) = CONST 
    0x1c3f: v1c3f(0x0) = ISZERO v1c39(0xf4240)
    0x1c40: v1c40(0x1) = ISZERO v1c3f(0x0)
    0x1c41: v1c41(0x1c46) = CONST 
    0x1c44: JUMPI v1c41(0x1c46), v1c40(0x1)

    Begin block 0x1c45
    prev=[0x1bd4], succ=[]
    =================================
    0x1c45: THROW 

    Begin block 0x1c46
    prev=[0x1bd4], succ=[0x1c4f, 0x1c50]
    =================================
    0x1c47: v1c47 = DIV v808, v1c39(0xf4240)
    0x1c49: v1c49 = ISZERO v1c37(0xa)
    0x1c4a: v1c4a = ISZERO v1c49
    0x1c4b: v1c4b(0x1c50) = CONST 
    0x1c4e: JUMPI v1c4b(0x1c50), v1c4a

    Begin block 0x1c4f
    prev=[0x1c46], succ=[]
    =================================
    0x1c4f: THROW 

    Begin block 0x1c50
    prev=[0x1c46], succ=[0x1c84, 0x1c85]
    =================================
    0x1c51: v1c51 = MOD v1c47, v1c37(0xa)
    0x1c52: v1c52(0x30) = CONST 
    0x1c54: v1c54 = ADD v1c52(0x30), v1c51
    0x1c55: v1c55(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c76: v1c76 = MUL v1c55(0x100000000000000000000000000000000000000000000000000000000000000), v1c54
    0x1c78: v1c78(0x22) = CONST 
    0x1c7b: v1c7b(0x2d) = MLOAD v1bd9
    0x1c7d: v1c7d(0x1) = LT v1c78(0x22), v1c7b(0x2d)
    0x1c7e: v1c7e = ISZERO v1c7d(0x1)
    0x1c7f: v1c7f = ISZERO v1c7e
    0x1c80: v1c80(0x1c85) = CONST 
    0x1c83: JUMPI v1c80(0x1c85), v1c7f

    Begin block 0x1c84
    prev=[0x1c50], succ=[]
    =================================
    0x1c84: THROW 

    Begin block 0x1c85
    prev=[0x1c50], succ=[0x1cc4, 0x1cc5]
    =================================
    0x1c87: v1c87(0x20) = CONST 
    0x1c89: v1c89 = ADD v1c87(0x20), v1bd9
    0x1c8a: v1c8a = ADD v1c89, v1c78(0x22)
    0x1c8c: v1c8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cac: v1cac(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1c8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1cad: v1cad = AND v1cac(0xff00000000000000000000000000000000000000000000000000000000000000), v1c76
    0x1cb0: v1cb0(0x0) = CONST 
    0x1cb2: v1cb2 = BYTE v1cb0(0x0), v1cad
    0x1cb4: MSTORE8 v1c8a, v1cb2
    0x1cb6: v1cb6(0xa) = CONST 
    0x1cb8: v1cb8(0x186a0) = CONST 
    0x1cbe: v1cbe(0x0) = ISZERO v1cb8(0x186a0)
    0x1cbf: v1cbf(0x1) = ISZERO v1cbe(0x0)
    0x1cc0: v1cc0(0x1cc5) = CONST 
    0x1cc3: JUMPI v1cc0(0x1cc5), v1cbf(0x1)

    Begin block 0x1cc4
    prev=[0x1c85], succ=[]
    =================================
    0x1cc4: THROW 

    Begin block 0x1cc5
    prev=[0x1c85], succ=[0x1cce, 0x1ccf]
    =================================
    0x1cc6: v1cc6 = DIV v808, v1cb8(0x186a0)
    0x1cc8: v1cc8 = ISZERO v1cb6(0xa)
    0x1cc9: v1cc9 = ISZERO v1cc8
    0x1cca: v1cca(0x1ccf) = CONST 
    0x1ccd: JUMPI v1cca(0x1ccf), v1cc9

    Begin block 0x1cce
    prev=[0x1cc5], succ=[]
    =================================
    0x1cce: THROW 

    Begin block 0x1ccf
    prev=[0x1cc5], succ=[0x1d03, 0x1d04]
    =================================
    0x1cd0: v1cd0 = MOD v1cc6, v1cb6(0xa)
    0x1cd1: v1cd1(0x30) = CONST 
    0x1cd3: v1cd3 = ADD v1cd1(0x30), v1cd0
    0x1cd4: v1cd4(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1cf5: v1cf5 = MUL v1cd4(0x100000000000000000000000000000000000000000000000000000000000000), v1cd3
    0x1cf7: v1cf7(0x23) = CONST 
    0x1cfa: v1cfa(0x2d) = MLOAD v1bd9
    0x1cfc: v1cfc(0x1) = LT v1cf7(0x23), v1cfa(0x2d)
    0x1cfd: v1cfd = ISZERO v1cfc(0x1)
    0x1cfe: v1cfe = ISZERO v1cfd
    0x1cff: v1cff(0x1d04) = CONST 
    0x1d02: JUMPI v1cff(0x1d04), v1cfe

    Begin block 0x1d03
    prev=[0x1ccf], succ=[]
    =================================
    0x1d03: THROW 

    Begin block 0x1d04
    prev=[0x1ccf], succ=[0x1d42, 0x1d43]
    =================================
    0x1d06: v1d06(0x20) = CONST 
    0x1d08: v1d08 = ADD v1d06(0x20), v1bd9
    0x1d09: v1d09 = ADD v1d08, v1cf7(0x23)
    0x1d0b: v1d0b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d2b: v1d2b(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1d0b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1d2c: v1d2c = AND v1d2b(0xff00000000000000000000000000000000000000000000000000000000000000), v1cf5
    0x1d2f: v1d2f(0x0) = CONST 
    0x1d31: v1d31 = BYTE v1d2f(0x0), v1d2c
    0x1d33: MSTORE8 v1d09, v1d31
    0x1d35: v1d35(0xa) = CONST 
    0x1d37: v1d37(0x2710) = CONST 
    0x1d3c: v1d3c(0x0) = ISZERO v1d37(0x2710)
    0x1d3d: v1d3d(0x1) = ISZERO v1d3c(0x0)
    0x1d3e: v1d3e(0x1d43) = CONST 
    0x1d41: JUMPI v1d3e(0x1d43), v1d3d(0x1)

    Begin block 0x1d42
    prev=[0x1d04], succ=[]
    =================================
    0x1d42: THROW 

    Begin block 0x1d43
    prev=[0x1d04], succ=[0x1d4c, 0x1d4d]
    =================================
    0x1d44: v1d44 = DIV v808, v1d37(0x2710)
    0x1d46: v1d46 = ISZERO v1d35(0xa)
    0x1d47: v1d47 = ISZERO v1d46
    0x1d48: v1d48(0x1d4d) = CONST 
    0x1d4b: JUMPI v1d48(0x1d4d), v1d47

    Begin block 0x1d4c
    prev=[0x1d43], succ=[]
    =================================
    0x1d4c: THROW 

    Begin block 0x1d4d
    prev=[0x1d43], succ=[0x1d81, 0x1d82]
    =================================
    0x1d4e: v1d4e = MOD v1d44, v1d35(0xa)
    0x1d4f: v1d4f(0x30) = CONST 
    0x1d51: v1d51 = ADD v1d4f(0x30), v1d4e
    0x1d52: v1d52(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d73: v1d73 = MUL v1d52(0x100000000000000000000000000000000000000000000000000000000000000), v1d51
    0x1d75: v1d75(0x24) = CONST 
    0x1d78: v1d78(0x2d) = MLOAD v1bd9
    0x1d7a: v1d7a(0x1) = LT v1d75(0x24), v1d78(0x2d)
    0x1d7b: v1d7b = ISZERO v1d7a(0x1)
    0x1d7c: v1d7c = ISZERO v1d7b
    0x1d7d: v1d7d(0x1d82) = CONST 
    0x1d80: JUMPI v1d7d(0x1d82), v1d7c

    Begin block 0x1d81
    prev=[0x1d4d], succ=[]
    =================================
    0x1d81: THROW 

    Begin block 0x1d82
    prev=[0x1d4d], succ=[0x1dc0, 0x1dc1]
    =================================
    0x1d84: v1d84(0x20) = CONST 
    0x1d86: v1d86 = ADD v1d84(0x20), v1bd9
    0x1d87: v1d87 = ADD v1d86, v1d75(0x24)
    0x1d89: v1d89(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1da9: v1da9(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1d89(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1daa: v1daa = AND v1da9(0xff00000000000000000000000000000000000000000000000000000000000000), v1d73
    0x1dad: v1dad(0x0) = CONST 
    0x1daf: v1daf = BYTE v1dad(0x0), v1daa
    0x1db1: MSTORE8 v1d87, v1daf
    0x1db3: v1db3(0xa) = CONST 
    0x1db5: v1db5(0x3e8) = CONST 
    0x1dba: v1dba(0x0) = ISZERO v1db5(0x3e8)
    0x1dbb: v1dbb(0x1) = ISZERO v1dba(0x0)
    0x1dbc: v1dbc(0x1dc1) = CONST 
    0x1dbf: JUMPI v1dbc(0x1dc1), v1dbb(0x1)

    Begin block 0x1dc0
    prev=[0x1d82], succ=[]
    =================================
    0x1dc0: THROW 

    Begin block 0x1dc1
    prev=[0x1d82], succ=[0x1dca, 0x1dcb]
    =================================
    0x1dc2: v1dc2 = DIV v808, v1db5(0x3e8)
    0x1dc4: v1dc4 = ISZERO v1db3(0xa)
    0x1dc5: v1dc5 = ISZERO v1dc4
    0x1dc6: v1dc6(0x1dcb) = CONST 
    0x1dc9: JUMPI v1dc6(0x1dcb), v1dc5

    Begin block 0x1dca
    prev=[0x1dc1], succ=[]
    =================================
    0x1dca: THROW 

    Begin block 0x1dcb
    prev=[0x1dc1], succ=[0x1dff, 0x1e00]
    =================================
    0x1dcc: v1dcc = MOD v1dc2, v1db3(0xa)
    0x1dcd: v1dcd(0x30) = CONST 
    0x1dcf: v1dcf = ADD v1dcd(0x30), v1dcc
    0x1dd0: v1dd0(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1df1: v1df1 = MUL v1dd0(0x100000000000000000000000000000000000000000000000000000000000000), v1dcf
    0x1df3: v1df3(0x25) = CONST 
    0x1df6: v1df6(0x2d) = MLOAD v1bd9
    0x1df8: v1df8(0x1) = LT v1df3(0x25), v1df6(0x2d)
    0x1df9: v1df9 = ISZERO v1df8(0x1)
    0x1dfa: v1dfa = ISZERO v1df9
    0x1dfb: v1dfb(0x1e00) = CONST 
    0x1dfe: JUMPI v1dfb(0x1e00), v1dfa

    Begin block 0x1dff
    prev=[0x1dcb], succ=[]
    =================================
    0x1dff: THROW 

    Begin block 0x1e00
    prev=[0x1dcb], succ=[0x1e3d, 0x1e3e]
    =================================
    0x1e02: v1e02(0x20) = CONST 
    0x1e04: v1e04 = ADD v1e02(0x20), v1bd9
    0x1e05: v1e05 = ADD v1e04, v1df3(0x25)
    0x1e07: v1e07(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e27: v1e27(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1e07(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1e28: v1e28 = AND v1e27(0xff00000000000000000000000000000000000000000000000000000000000000), v1df1
    0x1e2b: v1e2b(0x0) = CONST 
    0x1e2d: v1e2d = BYTE v1e2b(0x0), v1e28
    0x1e2f: MSTORE8 v1e05, v1e2d
    0x1e31: v1e31(0xa) = CONST 
    0x1e33: v1e33(0x64) = CONST 
    0x1e37: v1e37(0x0) = ISZERO v1e33(0x64)
    0x1e38: v1e38(0x1) = ISZERO v1e37(0x0)
    0x1e39: v1e39(0x1e3e) = CONST 
    0x1e3c: JUMPI v1e39(0x1e3e), v1e38(0x1)

    Begin block 0x1e3d
    prev=[0x1e00], succ=[]
    =================================
    0x1e3d: THROW 

    Begin block 0x1e3e
    prev=[0x1e00], succ=[0x1e47, 0x1e48]
    =================================
    0x1e3f: v1e3f = DIV v808, v1e33(0x64)
    0x1e41: v1e41 = ISZERO v1e31(0xa)
    0x1e42: v1e42 = ISZERO v1e41
    0x1e43: v1e43(0x1e48) = CONST 
    0x1e46: JUMPI v1e43(0x1e48), v1e42

    Begin block 0x1e47
    prev=[0x1e3e], succ=[]
    =================================
    0x1e47: THROW 

    Begin block 0x1e48
    prev=[0x1e3e], succ=[0x1e7c, 0x1e7d]
    =================================
    0x1e49: v1e49 = MOD v1e3f, v1e31(0xa)
    0x1e4a: v1e4a(0x30) = CONST 
    0x1e4c: v1e4c = ADD v1e4a(0x30), v1e49
    0x1e4d: v1e4d(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e6e: v1e6e = MUL v1e4d(0x100000000000000000000000000000000000000000000000000000000000000), v1e4c
    0x1e70: v1e70(0x26) = CONST 
    0x1e73: v1e73(0x2d) = MLOAD v1bd9
    0x1e75: v1e75(0x1) = LT v1e70(0x26), v1e73(0x2d)
    0x1e76: v1e76 = ISZERO v1e75(0x1)
    0x1e77: v1e77 = ISZERO v1e76
    0x1e78: v1e78(0x1e7d) = CONST 
    0x1e7b: JUMPI v1e78(0x1e7d), v1e77

    Begin block 0x1e7c
    prev=[0x1e48], succ=[]
    =================================
    0x1e7c: THROW 

    Begin block 0x1e7d
    prev=[0x1e48], succ=[0x1eb9, 0x1eba]
    =================================
    0x1e7f: v1e7f(0x20) = CONST 
    0x1e81: v1e81 = ADD v1e7f(0x20), v1bd9
    0x1e82: v1e82 = ADD v1e81, v1e70(0x26)
    0x1e84: v1e84(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ea4: v1ea4(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1e84(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1ea5: v1ea5 = AND v1ea4(0xff00000000000000000000000000000000000000000000000000000000000000), v1e6e
    0x1ea8: v1ea8(0x0) = CONST 
    0x1eaa: v1eaa = BYTE v1ea8(0x0), v1ea5
    0x1eac: MSTORE8 v1e82, v1eaa
    0x1eae: v1eae(0xa) = CONST 
    0x1eb3: v1eb3(0x0) = ISZERO v1eae(0xa)
    0x1eb4: v1eb4(0x1) = ISZERO v1eb3(0x0)
    0x1eb5: v1eb5(0x1eba) = CONST 
    0x1eb8: JUMPI v1eb5(0x1eba), v1eb4(0x1)

    Begin block 0x1eb9
    prev=[0x1e7d], succ=[]
    =================================
    0x1eb9: THROW 

    Begin block 0x1eba
    prev=[0x1e7d], succ=[0x1ec3, 0x1ec4]
    =================================
    0x1ebb: v1ebb = DIV v808, v1eae(0xa)
    0x1ebd: v1ebd = ISZERO v1eae(0xa)
    0x1ebe: v1ebe = ISZERO v1ebd
    0x1ebf: v1ebf(0x1ec4) = CONST 
    0x1ec2: JUMPI v1ebf(0x1ec4), v1ebe

    Begin block 0x1ec3
    prev=[0x1eba], succ=[]
    =================================
    0x1ec3: THROW 

    Begin block 0x1ec4
    prev=[0x1eba], succ=[0x1ef8, 0x1ef9]
    =================================
    0x1ec5: v1ec5 = MOD v1ebb, v1eae(0xa)
    0x1ec6: v1ec6(0x30) = CONST 
    0x1ec8: v1ec8 = ADD v1ec6(0x30), v1ec5
    0x1ec9: v1ec9(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1eea: v1eea = MUL v1ec9(0x100000000000000000000000000000000000000000000000000000000000000), v1ec8
    0x1eec: v1eec(0x27) = CONST 
    0x1eef: v1eef(0x2d) = MLOAD v1bd9
    0x1ef1: v1ef1(0x1) = LT v1eec(0x27), v1eef(0x2d)
    0x1ef2: v1ef2 = ISZERO v1ef1(0x1)
    0x1ef3: v1ef3 = ISZERO v1ef2
    0x1ef4: v1ef4(0x1ef9) = CONST 
    0x1ef7: JUMPI v1ef4(0x1ef9), v1ef3

    Begin block 0x1ef8
    prev=[0x1ec4], succ=[]
    =================================
    0x1ef8: THROW 

    Begin block 0x1ef9
    prev=[0x1ec4], succ=[0x1f36, 0x1f37]
    =================================
    0x1efb: v1efb(0x20) = CONST 
    0x1efd: v1efd = ADD v1efb(0x20), v1bd9
    0x1efe: v1efe = ADD v1efd, v1eec(0x27)
    0x1f00: v1f00(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f20: v1f20(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1f00(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1f21: v1f21 = AND v1f20(0xff00000000000000000000000000000000000000000000000000000000000000), v1eea
    0x1f24: v1f24(0x0) = CONST 
    0x1f26: v1f26 = BYTE v1f24(0x0), v1f21
    0x1f28: MSTORE8 v1efe, v1f26
    0x1f2a: v1f2a(0xa) = CONST 
    0x1f2c: v1f2c(0x1) = CONST 
    0x1f30: v1f30(0x0) = ISZERO v1f2c(0x1)
    0x1f31: v1f31(0x1) = ISZERO v1f30(0x0)
    0x1f32: v1f32(0x1f37) = CONST 
    0x1f35: JUMPI v1f32(0x1f37), v1f31(0x1)

    Begin block 0x1f36
    prev=[0x1ef9], succ=[]
    =================================
    0x1f36: THROW 

    Begin block 0x1f37
    prev=[0x1ef9], succ=[0x1f40, 0x1f41]
    =================================
    0x1f38: v1f38 = DIV v808, v1f2c(0x1)
    0x1f3a: v1f3a = ISZERO v1f2a(0xa)
    0x1f3b: v1f3b = ISZERO v1f3a
    0x1f3c: v1f3c(0x1f41) = CONST 
    0x1f3f: JUMPI v1f3c(0x1f41), v1f3b

    Begin block 0x1f40
    prev=[0x1f37], succ=[]
    =================================
    0x1f40: THROW 

    Begin block 0x1f41
    prev=[0x1f37], succ=[0x1f75, 0x1f76]
    =================================
    0x1f42: v1f42 = MOD v1f38, v1f2a(0xa)
    0x1f43: v1f43(0x30) = CONST 
    0x1f45: v1f45 = ADD v1f43(0x30), v1f42
    0x1f46: v1f46(0x100000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f67: v1f67 = MUL v1f46(0x100000000000000000000000000000000000000000000000000000000000000), v1f45
    0x1f69: v1f69(0x28) = CONST 
    0x1f6c: v1f6c(0x2d) = MLOAD v1bd9
    0x1f6e: v1f6e(0x1) = LT v1f69(0x28), v1f6c(0x2d)
    0x1f6f: v1f6f = ISZERO v1f6e(0x1)
    0x1f70: v1f70 = ISZERO v1f6f
    0x1f71: v1f71(0x1f76) = CONST 
    0x1f74: JUMPI v1f71(0x1f76), v1f70

    Begin block 0x1f75
    prev=[0x1f41], succ=[]
    =================================
    0x1f75: THROW 

    Begin block 0x1f76
    prev=[0x1f41], succ=[0x816]
    =================================
    0x1f78: v1f78(0x20) = CONST 
    0x1f7a: v1f7a = ADD v1f78(0x20), v1bd9
    0x1f7b: v1f7b = ADD v1f7a, v1f69(0x28)
    0x1f7d: v1f7d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f9d: v1f9d(0xff00000000000000000000000000000000000000000000000000000000000000) = NOT v1f7d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1f9e: v1f9e = AND v1f9d(0xff00000000000000000000000000000000000000000000000000000000000000), v1f67
    0x1fa1: v1fa1(0x0) = CONST 
    0x1fa3: v1fa3 = BYTE v1fa1(0x0), v1f9e
    0x1fa5: MSTORE8 v1f7b, v1fa3
    0x1fab: JUMP v801(0x816)

    Begin block 0x816
    prev=[0x1f76], succ=[0x83b]
    =================================
    0x817: v817(0x40) = CONST 
    0x819: v819 = MLOAD v817(0x40)
    0x81c: v81c(0x20) = CONST 
    0x81e: v81e = ADD v81c(0x20), v819
    0x821: v821(0x20) = SUB v81e, v819
    0x823: MSTORE v819, v821(0x20)
    0x827: v827(0x2d) = MLOAD v1bd9
    0x829: MSTORE v81e, v827(0x2d)
    0x82a: v82a(0x20) = CONST 
    0x82c: v82c = ADD v82a(0x20), v81e
    0x830: v830(0x2d) = MLOAD v1bd9
    0x832: v832(0x20) = CONST 
    0x834: v834 = ADD v832(0x20), v1bd9
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
    prev=[], succ=[0x1facB0x891]
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
    0x959: v959(0x1fac) = CONST 
    0x95c: JUMP v959(0x1fac), v94f, v930, v90e, v8f8, v8ed, v8c4, v8a2, v899, v892(0x95d)

    Begin block 0x1facB0x891
    prev=[0x891], succ=[0x1fd5B0x891, 0x1fc4B0x891]
    =================================
    0x1fadS0x891: v1fadV891(0x12) = CONST 
    0x1fafS0x891: v1fafV891(0x0) = CONST 
    0x1fb2S0x891: v1fb2V891 = SLOAD v1fadV891(0x12)
    0x1fb4S0x891: v1fb4V891(0x100) = CONST 
    0x1fb7S0x891: v1fb7V891(0x1) = EXP v1fb4V891(0x100), v1fafV891(0x0)
    0x1fb9S0x891: v1fb9V891 = DIV v1fb2V891, v1fb7V891(0x1)
    0x1fbaS0x891: v1fbaV891(0xff) = CONST 
    0x1fbcS0x891: v1fbcV891 = AND v1fbaV891(0xff), v1fb9V891
    0x1fbdS0x891: v1fbdV891 = ISZERO v1fbcV891
    0x1fbfS0x891: v1fbfV891 = ISZERO v1fbdV891
    0x1fc0S0x891: v1fc0V891(0x1fd5) = CONST 
    0x1fc3S0x891: JUMPI v1fc0V891(0x1fd5), v1fbfV891

    Begin block 0x1fd5B0x891
    prev=[0x1facB0x891, 0x1fc4B0x891], succ=[0x1fdcB0x891, 0x1fe0B0x891]
    =================================
    0x1fd5_0x0S0x891: v1fd5_0V891 = PHI v1fbdV891, v1fd4V891
    0x1fd6S0x891: v1fd6V891 = ISZERO v1fd5_0V891
    0x1fd7S0x891: v1fd7V891 = ISZERO v1fd6V891
    0x1fd8S0x891: v1fd8V891(0x1fe0) = CONST 
    0x1fdbS0x891: JUMPI v1fd8V891(0x1fe0), v1fd7V891

    Begin block 0x1fdcB0x891
    prev=[0x1fd5B0x891], succ=[]
    =================================
    0x1fdcS0x891: v1fdcV891(0x0) = CONST 
    0x1fdfS0x891: REVERT v1fdcV891(0x0), v1fdcV891(0x0)

    Begin block 0x1fe0B0x891
    prev=[0x1fd5B0x891], succ=[0x203dB0x891, 0x208dB0x891]
    =================================
    0x1fe1S0x891: v1fe1V891(0xd8479c546b80ce91916c7800c1840bd6446b06ce) = CONST 
    0x1ff6S0x891: v1ff6V891(0x523f110e) = CONST 
    0x1ffbS0x891: v1ffbV891(0x2) = CONST 
    0x2005S0x891: v2005V891(0x40) = CONST 
    0x2007S0x891: v2007V891 = MLOAD v2005V891(0x40)
    0x2009S0x891: v2009V891(0xffffffff) = CONST 
    0x200eS0x891: v200eV891(0x523f110e) = AND v2009V891(0xffffffff), v1ff6V891(0x523f110e)
    0x200fS0x891: v200fV891(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x202dS0x891: v202dV891(0x523f110e00000000000000000000000000000000000000000000000000000000) = MUL v200fV891(0x100000000000000000000000000000000000000000000000000000000), v200eV891(0x523f110e)
    0x202fS0x891: MSTORE v2007V891, v202dV891(0x523f110e00000000000000000000000000000000000000000000000000000000)
    0x2030S0x891: v2030V891(0x4) = CONST 
    0x2032S0x891: v2032V891 = ADD v2030V891(0x4), v2007V891
    0x2035S0x891: v2035V891(0x10) = CONST 
    0x2038S0x891: v2038V891(0x0) = ISZERO v2035V891(0x10)
    0x2039S0x891: v2039V891(0x208d) = CONST 
    0x203cS0x891: JUMPI v2039V891(0x208d), v2038V891(0x0)

    Begin block 0x203dB0x891
    prev=[0x1fe0B0x891], succ=[0x2043B0x891]
    =================================
    0x203dS0x891: v203dV891(0x20) = CONST 
    0x203fS0x891: v203fV891(0x200) = MUL v203dV891(0x20), v2035V891(0x10)
    0x2041S0x891: v2041V891 = ADD v2032V891, v203fV891(0x200)

    Begin block 0x2043B0x891
    prev=[0x203dB0x891, 0x2043B0x891], succ=[0x208dB0x891, 0x2043B0x891]
    =================================
    0x2043_0x0S0x891: v2043_0V891 = PHI v2032V891, v2080V891
    0x2043_0x1S0x891: v2043_1V891 = PHI v1ffbV891(0x2), v2084V891
    0x2045S0x891: v2045V891(0x0) = CONST 
    0x2048S0x891: v2048V891 = SLOAD v2043_1V891
    0x204aS0x891: v204aV891(0x100) = CONST 
    0x204dS0x891: v204dV891(0x1) = EXP v204aV891(0x100), v2045V891(0x0)
    0x204fS0x891: v204fV891 = DIV v2048V891, v204dV891(0x1)
    0x2050S0x891: v2050V891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2065S0x891: v2065V891 = AND v2050V891(0xffffffffffffffffffffffffffffffffffffffff), v204fV891
    0x2066S0x891: v2066V891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x207bS0x891: v207bV891 = AND v2066V891(0xffffffffffffffffffffffffffffffffffffffff), v2065V891
    0x207dS0x891: MSTORE v2043_0V891, v207bV891
    0x207eS0x891: v207eV891(0x20) = CONST 
    0x2080S0x891: v2080V891 = ADD v207eV891(0x20), v2043_0V891
    0x2082S0x891: v2082V891(0x1) = CONST 
    0x2084S0x891: v2084V891 = ADD v2082V891(0x1), v2043_1V891
    0x2088S0x891: v2088V891 = GT v2041V891, v2080V891
    0x2089S0x891: v2089V891(0x2043) = CONST 
    0x208cS0x891: JUMPI v2089V891(0x2043), v2088V891

    Begin block 0x208dB0x891
    prev=[0x1fe0B0x891, 0x2043B0x891], succ=[0x20bfB0x891]
    =================================
    0x208d_0x2S0x891: v208d_2V891 = PHI v2041V891, v2032V891
    0x2092S0x891: MSTORE v208d_2V891, v899
    0x2093S0x891: v2093V891(0x20) = CONST 
    0x2095S0x891: v2095V891 = ADD v2093V891(0x20), v208d_2V891
    0x2098S0x891: MSTORE v2095V891, v8a2
    0x2099S0x891: v2099V891(0x20) = CONST 
    0x209bS0x891: v209bV891 = ADD v2099V891(0x20), v2095V891
    0x209dS0x891: v209dV891(0x20) = CONST 
    0x209fS0x891: v209fV891 = ADD v209dV891(0x20), v209bV891
    0x20a1S0x891: v20a1V891 = ISZERO v8ed
    0x20a2S0x891: v20a2V891 = ISZERO v20a1V891
    0x20a3S0x891: v20a3V891 = ISZERO v20a2V891
    0x20a4S0x891: v20a4V891 = ISZERO v20a3V891
    0x20a6S0x891: MSTORE v209fV891, v20a4V891
    0x20a7S0x891: v20a7V891(0x20) = CONST 
    0x20a9S0x891: v20a9V891 = ADD v20a7V891(0x20), v209fV891
    0x20abS0x891: v20abV891 = ISZERO v8f8
    0x20acS0x891: v20acV891 = ISZERO v20abV891
    0x20adS0x891: v20adV891 = ISZERO v20acV891
    0x20aeS0x891: v20aeV891 = ISZERO v20adV891
    0x20b0S0x891: MSTORE v20a9V891, v20aeV891
    0x20b1S0x891: v20b1V891(0x20) = CONST 
    0x20b3S0x891: v20b3V891 = ADD v20b1V891(0x20), v20a9V891
    0x20b5S0x891: v20b5V891(0x80) = CONST 
    0x20b7S0x891: v20b7V891(0x20) = CONST 
    0x20b9S0x891: v20b9V891(0x1000) = MUL v20b7V891(0x20), v20b5V891(0x80)
    0x20bdS0x891: v20bdV891(0x0) = CONST 

    Begin block 0x20bfB0x891
    prev=[0x208dB0x891, 0x20c8B0x891], succ=[0x20daB0x891, 0x20c8B0x891]
    =================================
    0x20bf_0x0S0x891: v20bf_0V891 = PHI v20bdV891(0x0), v20d3V891
    0x20c2S0x891: v20c2V891 = LT v20bf_0V891, v20b9V891(0x1000)
    0x20c3S0x891: v20c3V891 = ISZERO v20c2V891
    0x20c4S0x891: v20c4V891(0x20da) = CONST 
    0x20c7S0x891: JUMPI v20c4V891(0x20da), v20c3V891

    Begin block 0x20daB0x891
    prev=[0x20bfB0x891], succ=[0x213dB0x891]
    =================================
    0x20e1S0x891: v20e1V891 = ADD v20b9V891(0x1000), v20b3V891
    0x20e3S0x891: v20e3V891 = ISZERO v930
    0x20e4S0x891: v20e4V891 = ISZERO v20e3V891
    0x20e5S0x891: v20e5V891 = ISZERO v20e4V891
    0x20e6S0x891: v20e6V891 = ISZERO v20e5V891
    0x20e8S0x891: MSTORE v20e1V891, v20e6V891
    0x20e9S0x891: v20e9V891(0x20) = CONST 
    0x20ebS0x891: v20ebV891 = ADD v20e9V891(0x20), v20e1V891
    0x20edS0x891: v20edV891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2102S0x891: v2102V891 = AND v20edV891(0xffffffffffffffffffffffffffffffffffffffff), v94f
    0x2103S0x891: v2103V891(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2118S0x891: v2118V891 = AND v2103V891(0xffffffffffffffffffffffffffffffffffffffff), v2102V891
    0x211aS0x891: MSTORE v20ebV891, v2118V891
    0x211bS0x891: v211bV891(0x20) = CONST 
    0x211dS0x891: v211dV891 = ADD v211bV891(0x20), v20ebV891
    0x2120S0x891: v2120V891 = SUB v211dV891, v2032V891
    0x2122S0x891: MSTORE v209bV891, v2120V891
    0x2126S0x891: v2126V891 = MLOAD v8c4
    0x2128S0x891: MSTORE v211dV891, v2126V891
    0x2129S0x891: v2129V891(0x20) = CONST 
    0x212bS0x891: v212bV891 = ADD v2129V891(0x20), v211dV891
    0x212fS0x891: v212fV891 = MLOAD v8c4
    0x2131S0x891: v2131V891(0x20) = CONST 
    0x2133S0x891: v2133V891 = ADD v2131V891(0x20), v8c4
    0x2135S0x891: v2135V891(0x20) = CONST 
    0x2137S0x891: v2137V891 = MUL v2135V891(0x20), v212fV891
    0x213bS0x891: v213bV891(0x0) = CONST 

    Begin block 0x213dB0x891
    prev=[0x20daB0x891, 0x2146B0x891], succ=[0x2158B0x891, 0x2146B0x891]
    =================================
    0x213d_0x0S0x891: v213d_0V891 = PHI v213bV891(0x0), v2151V891
    0x2140S0x891: v2140V891 = LT v213d_0V891, v2137V891
    0x2141S0x891: v2141V891 = ISZERO v2140V891
    0x2142S0x891: v2142V891(0x2158) = CONST 
    0x2145S0x891: JUMPI v2142V891(0x2158), v2141V891

    Begin block 0x2158B0x891
    prev=[0x213dB0x891], succ=[0x217eB0x891, 0x2182B0x891]
    =================================
    0x215fS0x891: v215fV891 = ADD v2137V891, v212bV891
    0x216cS0x891: v216cV891(0x0) = CONST 
    0x216eS0x891: v216eV891(0x40) = CONST 
    0x2170S0x891: v2170V891 = MLOAD v216eV891(0x40)
    0x2173S0x891: v2173V891 = SUB v215fV891, v2170V891
    0x2177S0x891: v2177V891 = EXTCODESIZE v1fe1V891(0xd8479c546b80ce91916c7800c1840bd6446b06ce)
    0x2178S0x891: v2178V891 = ISZERO v2177V891
    0x2179S0x891: v2179V891 = ISZERO v2178V891
    0x217aS0x891: v217aV891(0x2182) = CONST 
    0x217dS0x891: JUMPI v217aV891(0x2182), v2179V891

    Begin block 0x217eB0x891
    prev=[0x2158B0x891], succ=[]
    =================================
    0x217eS0x891: v217eV891(0x0) = CONST 
    0x2181S0x891: REVERT v217eV891(0x0), v217eV891(0x0)

    Begin block 0x2182B0x891
    prev=[0x2158B0x891], succ=[0x218fB0x891, 0x2193B0x891]
    =================================
    0x2183S0x891: v2183V891(0x2c6) = CONST 
    0x2186S0x891: v2186V891 = GAS 
    0x2187S0x891: v2187V891 = SUB v2186V891, v2183V891(0x2c6)
    0x2188S0x891: v2188V891 = DELEGATECALL v2187V891, v1fe1V891(0xd8479c546b80ce91916c7800c1840bd6446b06ce), v2170V891, v2173V891, v2170V891, v216cV891(0x0)
    0x2189S0x891: v2189V891 = ISZERO v2188V891
    0x218aS0x891: v218aV891 = ISZERO v2189V891
    0x218bS0x891: v218bV891(0x2193) = CONST 
    0x218eS0x891: JUMPI v218bV891(0x2193), v218aV891

    Begin block 0x218fB0x891
    prev=[0x2182B0x891], succ=[]
    =================================
    0x218fS0x891: v218fV891(0x0) = CONST 
    0x2192S0x891: REVERT v218fV891(0x0), v218fV891(0x0)

    Begin block 0x2193B0x891
    prev=[0x2182B0x891], succ=[0x95d]
    =================================
    0x219fS0x891: JUMP v892(0x95d)

    Begin block 0x95d
    prev=[0x2193B0x891], succ=[]
    =================================
    0x95e: STOP 

    Begin block 0x2146B0x891
    prev=[0x213dB0x891], succ=[0x213dB0x891]
    =================================
    0x2146_0x0S0x891: v2146_0V891 = PHI v213bV891(0x0), v2151V891
    0x2148S0x891: v2148V891 = ADD v2133V891, v2146_0V891
    0x2149S0x891: v2149V891 = MLOAD v2148V891
    0x214cS0x891: v214cV891 = ADD v212bV891, v2146_0V891
    0x214dS0x891: MSTORE v214cV891, v2149V891
    0x214eS0x891: v214eV891(0x20) = CONST 
    0x2151S0x891: v2151V891 = ADD v2146_0V891, v214eV891(0x20)
    0x2154S0x891: v2154V891(0x213d) = CONST 
    0x2157S0x891: JUMP v2154V891(0x213d)

    Begin block 0x20c8B0x891
    prev=[0x20bfB0x891], succ=[0x20bfB0x891]
    =================================
    0x20c8_0x0S0x891: v20c8_0V891 = PHI v20bdV891(0x0), v20d3V891
    0x20caS0x891: v20caV891 = ADD v90e, v20c8_0V891
    0x20cbS0x891: v20cbV891 = MLOAD v20caV891
    0x20ceS0x891: v20ceV891 = ADD v20b3V891, v20c8_0V891
    0x20cfS0x891: MSTORE v20ceV891, v20cbV891
    0x20d0S0x891: v20d0V891(0x20) = CONST 
    0x20d3S0x891: v20d3V891 = ADD v20c8_0V891, v20d0V891(0x20)
    0x20d6S0x891: v20d6V891(0x20bf) = CONST 
    0x20d9S0x891: JUMP v20d6V891(0x20bf)

    Begin block 0x1fc4B0x891
    prev=[0x1facB0x891], succ=[0x1fd5B0x891]
    =================================
    0x1fc5S0x891: v1fc5V891(0x12) = CONST 
    0x1fc7S0x891: v1fc7V891(0x1) = CONST 
    0x1fcaS0x891: v1fcaV891 = SLOAD v1fc5V891(0x12)
    0x1fccS0x891: v1fccV891(0x100) = CONST 
    0x1fcfS0x891: v1fcfV891(0x100) = EXP v1fccV891(0x100), v1fc7V891(0x1)
    0x1fd1S0x891: v1fd1V891 = DIV v1fcaV891, v1fcfV891(0x100)
    0x1fd2S0x891: v1fd2V891(0xff) = CONST 
    0x1fd4S0x891: v1fd4V891 = AND v1fd2V891(0xff), v1fd1V891

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
    prev=[0x95f], succ=[0x21a0]
    =================================
    0x96b: v96b(0x972) = CONST 
    0x96e: v96e(0x21a0) = CONST 
    0x971: JUMP v96e(0x21a0)

    Begin block 0x21a0
    prev=[0x96a], succ=[0x972]
    =================================
    0x21a1: v21a1(0x1) = CONST 
    0x21a3: v21a3(0x0) = CONST 
    0x21a6: v21a6 = SLOAD v21a1(0x1)
    0x21a8: v21a8(0x100) = CONST 
    0x21ab: v21ab(0x1) = EXP v21a8(0x100), v21a3(0x0)
    0x21ad: v21ad = DIV v21a6, v21ab(0x1)
    0x21ae: v21ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21c3: v21c3 = AND v21ae(0xffffffffffffffffffffffffffffffffffffffff), v21ad
    0x21c5: JUMP v96b(0x972)

    Begin block 0x972
    prev=[0x21a0], succ=[]
    =================================
    0x973: v973(0x40) = CONST 
    0x975: v975 = MLOAD v973(0x40)
    0x978: v978(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x98d: v98d = AND v978(0xffffffffffffffffffffffffffffffffffffffff), v21c3
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
    prev=[0x9b4], succ=[0x21c6]
    =================================
    0x9c0: v9c0(0x9eb) = CONST 
    0x9c3: v9c3(0x4) = CONST 
    0x9c7: v9c7 = CALLDATALOAD v9c3(0x4)
    0x9c8: v9c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9dd: v9dd = AND v9c8(0xffffffffffffffffffffffffffffffffffffffff), v9c7
    0x9df: v9df(0x20) = CONST 
    0x9e1: v9e1(0x24) = ADD v9df(0x20), v9c3(0x4)
    0x9e7: v9e7(0x21c6) = CONST 
    0x9ea: JUMP v9e7(0x21c6)

    Begin block 0x21c6
    prev=[0x9bf], succ=[0x221d, 0x2221]
    =================================
    0x21c7: v21c7(0x0) = CONST 
    0x21cb: v21cb = SLOAD v21c7(0x0)
    0x21cd: v21cd(0x100) = CONST 
    0x21d0: v21d0(0x1) = EXP v21cd(0x100), v21c7(0x0)
    0x21d2: v21d2 = DIV v21cb, v21d0(0x1)
    0x21d3: v21d3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21e8: v21e8 = AND v21d3(0xffffffffffffffffffffffffffffffffffffffff), v21d2
    0x21e9: v21e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21fe: v21fe = AND v21e9(0xffffffffffffffffffffffffffffffffffffffff), v21e8
    0x21ff: v21ff = CALLER 
    0x2200: v2200(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2215: v2215 = AND v2200(0xffffffffffffffffffffffffffffffffffffffff), v21ff
    0x2216: v2216 = EQ v2215, v21fe
    0x2217: v2217 = ISZERO v2216
    0x2218: v2218 = ISZERO v2217
    0x2219: v2219(0x2221) = CONST 
    0x221c: JUMPI v2219(0x2221), v2218

    Begin block 0x221d
    prev=[0x21c6], succ=[]
    =================================
    0x221d: v221d(0x0) = CONST 
    0x2220: REVERT v221d(0x0), v221d(0x0)

    Begin block 0x2221
    prev=[0x21c6], succ=[0x2259, 0x225d]
    =================================
    0x2222: v2222(0x0) = CONST 
    0x2224: v2224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2239: v2239(0x0) = AND v2224(0xffffffffffffffffffffffffffffffffffffffff), v2222(0x0)
    0x223b: v223b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2250: v2250 = AND v223b(0xffffffffffffffffffffffffffffffffffffffff), v9dd
    0x2251: v2251 = EQ v2250, v2239(0x0)
    0x2252: v2252 = ISZERO v2251
    0x2253: v2253 = ISZERO v2252
    0x2254: v2254 = ISZERO v2253
    0x2255: v2255(0x225d) = CONST 
    0x2258: JUMPI v2255(0x225d), v2254

    Begin block 0x2259
    prev=[0x2221], succ=[]
    =================================
    0x2259: v2259(0x0) = CONST 
    0x225c: REVERT v2259(0x0), v2259(0x0)

    Begin block 0x225d
    prev=[0x2221], succ=[0x9eb]
    =================================
    0x225f: v225f(0x1) = CONST 
    0x2261: v2261(0x0) = CONST 
    0x2263: v2263(0x100) = CONST 
    0x2266: v2266(0x1) = EXP v2263(0x100), v2261(0x0)
    0x2268: v2268 = SLOAD v225f(0x1)
    0x226a: v226a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x227f: v227f(0xffffffffffffffffffffffffffffffffffffffff) = MUL v226a(0xffffffffffffffffffffffffffffffffffffffff), v2266(0x1)
    0x2280: v2280(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v227f(0xffffffffffffffffffffffffffffffffffffffff)
    0x2281: v2281 = AND v2280(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2268
    0x2284: v2284(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2299: v2299 = AND v2284(0xffffffffffffffffffffffffffffffffffffffff), v9dd
    0x229a: v229a = MUL v2299, v2266(0x1)
    0x229b: v229b = OR v229a, v2281
    0x229d: SSTORE v225f(0x1), v229b
    0x22a0: JUMP v9c0(0x9eb)

    Begin block 0x9eb
    prev=[0x225d], succ=[]
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
    prev=[0x9ed], succ=[0x22a1B0x9f8]
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
    0xa71: va71(0x22a1) = CONST 
    0xa74: JUMP va71(0x22a1), va49, va27, va1a, va0d, va00, v9f9(0xa75)

    Begin block 0x22a1B0x9f8
    prev=[0x9f8], succ=[0x22caB0x9f8, 0x22b9B0x9f8]
    =================================
    0x22a2S0x9f8: v22a2V9f8(0x12) = CONST 
    0x22a4S0x9f8: v22a4V9f8(0x0) = CONST 
    0x22a7S0x9f8: v22a7V9f8 = SLOAD v22a2V9f8(0x12)
    0x22a9S0x9f8: v22a9V9f8(0x100) = CONST 
    0x22acS0x9f8: v22acV9f8(0x1) = EXP v22a9V9f8(0x100), v22a4V9f8(0x0)
    0x22aeS0x9f8: v22aeV9f8 = DIV v22a7V9f8, v22acV9f8(0x1)
    0x22afS0x9f8: v22afV9f8(0xff) = CONST 
    0x22b1S0x9f8: v22b1V9f8 = AND v22afV9f8(0xff), v22aeV9f8
    0x22b2S0x9f8: v22b2V9f8 = ISZERO v22b1V9f8
    0x22b4S0x9f8: v22b4V9f8 = ISZERO v22b2V9f8
    0x22b5S0x9f8: v22b5V9f8(0x22ca) = CONST 
    0x22b8S0x9f8: JUMPI v22b5V9f8(0x22ca), v22b4V9f8

    Begin block 0x22caB0x9f8
    prev=[0x22a1B0x9f8, 0x22b9B0x9f8], succ=[0x22d1B0x9f8, 0x22d5B0x9f8]
    =================================
    0x22ca_0x0S0x9f8: v22ca_0V9f8 = PHI v22b2V9f8, v22c9V9f8
    0x22cbS0x9f8: v22cbV9f8 = ISZERO v22ca_0V9f8
    0x22ccS0x9f8: v22ccV9f8 = ISZERO v22cbV9f8
    0x22cdS0x9f8: v22cdV9f8(0x22d5) = CONST 
    0x22d0S0x9f8: JUMPI v22cdV9f8(0x22d5), v22ccV9f8

    Begin block 0x22d1B0x9f8
    prev=[0x22caB0x9f8], succ=[]
    =================================
    0x22d1S0x9f8: v22d1V9f8(0x0) = CONST 
    0x22d4S0x9f8: REVERT v22d1V9f8(0x0), v22d1V9f8(0x0)

    Begin block 0x22d5B0x9f8
    prev=[0x22caB0x9f8], succ=[0x232fB0x9f8, 0x237fB0x9f8]
    =================================
    0x22d6S0x9f8: v22d6V9f8(0xb80f7ad4db894093658474ae57d94345bea474f4) = CONST 
    0x22ebS0x9f8: v22ebV9f8(0x9c161d1a) = CONST 
    0x22f0S0x9f8: v22f0V9f8(0x2) = CONST 
    0x22f7S0x9f8: v22f7V9f8(0x40) = CONST 
    0x22f9S0x9f8: v22f9V9f8 = MLOAD v22f7V9f8(0x40)
    0x22fbS0x9f8: v22fbV9f8(0xffffffff) = CONST 
    0x2300S0x9f8: v2300V9f8(0x9c161d1a) = AND v22fbV9f8(0xffffffff), v22ebV9f8(0x9c161d1a)
    0x2301S0x9f8: v2301V9f8(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x231fS0x9f8: v231fV9f8(0x9c161d1a00000000000000000000000000000000000000000000000000000000) = MUL v2301V9f8(0x100000000000000000000000000000000000000000000000000000000), v2300V9f8(0x9c161d1a)
    0x2321S0x9f8: MSTORE v22f9V9f8, v231fV9f8(0x9c161d1a00000000000000000000000000000000000000000000000000000000)
    0x2322S0x9f8: v2322V9f8(0x4) = CONST 
    0x2324S0x9f8: v2324V9f8 = ADD v2322V9f8(0x4), v22f9V9f8
    0x2327S0x9f8: v2327V9f8(0x10) = CONST 
    0x232aS0x9f8: v232aV9f8(0x0) = ISZERO v2327V9f8(0x10)
    0x232bS0x9f8: v232bV9f8(0x237f) = CONST 
    0x232eS0x9f8: JUMPI v232bV9f8(0x237f), v232aV9f8(0x0)

    Begin block 0x232fB0x9f8
    prev=[0x22d5B0x9f8], succ=[0x2335B0x9f8]
    =================================
    0x232fS0x9f8: v232fV9f8(0x20) = CONST 
    0x2331S0x9f8: v2331V9f8(0x200) = MUL v232fV9f8(0x20), v2327V9f8(0x10)
    0x2333S0x9f8: v2333V9f8 = ADD v2324V9f8, v2331V9f8(0x200)

    Begin block 0x2335B0x9f8
    prev=[0x232fB0x9f8, 0x2335B0x9f8], succ=[0x237fB0x9f8, 0x2335B0x9f8]
    =================================
    0x2335_0x0S0x9f8: v2335_0V9f8 = PHI v2324V9f8, v2372V9f8
    0x2335_0x1S0x9f8: v2335_1V9f8 = PHI v22f0V9f8(0x2), v2376V9f8
    0x2337S0x9f8: v2337V9f8(0x0) = CONST 
    0x233aS0x9f8: v233aV9f8 = SLOAD v2335_1V9f8
    0x233cS0x9f8: v233cV9f8(0x100) = CONST 
    0x233fS0x9f8: v233fV9f8(0x1) = EXP v233cV9f8(0x100), v2337V9f8(0x0)
    0x2341S0x9f8: v2341V9f8 = DIV v233aV9f8, v233fV9f8(0x1)
    0x2342S0x9f8: v2342V9f8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2357S0x9f8: v2357V9f8 = AND v2342V9f8(0xffffffffffffffffffffffffffffffffffffffff), v2341V9f8
    0x2358S0x9f8: v2358V9f8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x236dS0x9f8: v236dV9f8 = AND v2358V9f8(0xffffffffffffffffffffffffffffffffffffffff), v2357V9f8
    0x236fS0x9f8: MSTORE v2335_0V9f8, v236dV9f8
    0x2370S0x9f8: v2370V9f8(0x20) = CONST 
    0x2372S0x9f8: v2372V9f8 = ADD v2370V9f8(0x20), v2335_0V9f8
    0x2374S0x9f8: v2374V9f8(0x1) = CONST 
    0x2376S0x9f8: v2376V9f8 = ADD v2374V9f8(0x1), v2335_1V9f8
    0x237aS0x9f8: v237aV9f8 = GT v2333V9f8, v2372V9f8
    0x237bS0x9f8: v237bV9f8(0x2335) = CONST 
    0x237eS0x9f8: JUMPI v237bV9f8(0x2335), v237aV9f8

    Begin block 0x237fB0x9f8
    prev=[0x22d5B0x9f8, 0x2335B0x9f8], succ=[0x23d5B0x9f8]
    =================================
    0x237f_0x2S0x9f8: v237f_2V9f8 = PHI v2333V9f8, v2324V9f8
    0x2384S0x9f8: MSTORE v237f_2V9f8, va00
    0x2385S0x9f8: v2385V9f8(0x20) = CONST 
    0x2387S0x9f8: v2387V9f8 = ADD v2385V9f8(0x20), v237f_2V9f8
    0x2389S0x9f8: v2389V9f8(0xffff) = CONST 
    0x238cS0x9f8: v238cV9f8 = AND v2389V9f8(0xffff), va0d
    0x238dS0x9f8: v238dV9f8(0xffff) = CONST 
    0x2390S0x9f8: v2390V9f8 = AND v238dV9f8(0xffff), v238cV9f8
    0x2392S0x9f8: MSTORE v2387V9f8, v2390V9f8
    0x2393S0x9f8: v2393V9f8(0x20) = CONST 
    0x2395S0x9f8: v2395V9f8 = ADD v2393V9f8(0x20), v2387V9f8
    0x2397S0x9f8: v2397V9f8(0xffff) = CONST 
    0x239aS0x9f8: v239aV9f8 = AND v2397V9f8(0xffff), va1a
    0x239bS0x9f8: v239bV9f8(0xffff) = CONST 
    0x239eS0x9f8: v239eV9f8 = AND v239bV9f8(0xffff), v239aV9f8
    0x23a0S0x9f8: MSTORE v2395V9f8, v239eV9f8
    0x23a1S0x9f8: v23a1V9f8(0x20) = CONST 
    0x23a3S0x9f8: v23a3V9f8 = ADD v23a1V9f8(0x20), v2395V9f8
    0x23a5S0x9f8: v23a5V9f8(0xffff) = CONST 
    0x23a8S0x9f8: v23a8V9f8 = AND v23a5V9f8(0xffff), va27
    0x23a9S0x9f8: v23a9V9f8(0xffff) = CONST 
    0x23acS0x9f8: v23acV9f8 = AND v23a9V9f8(0xffff), v23a8V9f8
    0x23aeS0x9f8: MSTORE v23a3V9f8, v23acV9f8
    0x23afS0x9f8: v23afV9f8(0x20) = CONST 
    0x23b1S0x9f8: v23b1V9f8 = ADD v23afV9f8(0x20), v23a3V9f8
    0x23b3S0x9f8: v23b3V9f8(0x20) = CONST 
    0x23b5S0x9f8: v23b5V9f8 = ADD v23b3V9f8(0x20), v23b1V9f8
    0x23b8S0x9f8: v23b8V9f8 = SUB v23b5V9f8, v2324V9f8
    0x23baS0x9f8: MSTORE v23b1V9f8, v23b8V9f8
    0x23beS0x9f8: v23beV9f8 = MLOAD va49
    0x23c0S0x9f8: MSTORE v23b5V9f8, v23beV9f8
    0x23c1S0x9f8: v23c1V9f8(0x20) = CONST 
    0x23c3S0x9f8: v23c3V9f8 = ADD v23c1V9f8(0x20), v23b5V9f8
    0x23c7S0x9f8: v23c7V9f8 = MLOAD va49
    0x23c9S0x9f8: v23c9V9f8(0x20) = CONST 
    0x23cbS0x9f8: v23cbV9f8 = ADD v23c9V9f8(0x20), va49
    0x23cdS0x9f8: v23cdV9f8(0x20) = CONST 
    0x23cfS0x9f8: v23cfV9f8 = MUL v23cdV9f8(0x20), v23c7V9f8
    0x23d3S0x9f8: v23d3V9f8(0x0) = CONST 

    Begin block 0x23d5B0x9f8
    prev=[0x237fB0x9f8, 0x23deB0x9f8], succ=[0x23f0B0x9f8, 0x23deB0x9f8]
    =================================
    0x23d5_0x0S0x9f8: v23d5_0V9f8 = PHI v23d3V9f8(0x0), v23e9V9f8
    0x23d8S0x9f8: v23d8V9f8 = LT v23d5_0V9f8, v23cfV9f8
    0x23d9S0x9f8: v23d9V9f8 = ISZERO v23d8V9f8
    0x23daS0x9f8: v23daV9f8(0x23f0) = CONST 
    0x23ddS0x9f8: JUMPI v23daV9f8(0x23f0), v23d9V9f8

    Begin block 0x23f0B0x9f8
    prev=[0x23d5B0x9f8], succ=[0x2413B0x9f8, 0x2417B0x9f8]
    =================================
    0x23f7S0x9f8: v23f7V9f8 = ADD v23cfV9f8, v23c3V9f8
    0x2401S0x9f8: v2401V9f8(0x0) = CONST 
    0x2403S0x9f8: v2403V9f8(0x40) = CONST 
    0x2405S0x9f8: v2405V9f8 = MLOAD v2403V9f8(0x40)
    0x2408S0x9f8: v2408V9f8 = SUB v23f7V9f8, v2405V9f8
    0x240cS0x9f8: v240cV9f8 = EXTCODESIZE v22d6V9f8(0xb80f7ad4db894093658474ae57d94345bea474f4)
    0x240dS0x9f8: v240dV9f8 = ISZERO v240cV9f8
    0x240eS0x9f8: v240eV9f8 = ISZERO v240dV9f8
    0x240fS0x9f8: v240fV9f8(0x2417) = CONST 
    0x2412S0x9f8: JUMPI v240fV9f8(0x2417), v240eV9f8

    Begin block 0x2413B0x9f8
    prev=[0x23f0B0x9f8], succ=[]
    =================================
    0x2413S0x9f8: v2413V9f8(0x0) = CONST 
    0x2416S0x9f8: REVERT v2413V9f8(0x0), v2413V9f8(0x0)

    Begin block 0x2417B0x9f8
    prev=[0x23f0B0x9f8], succ=[0x2424B0x9f8, 0x2428B0x9f8]
    =================================
    0x2418S0x9f8: v2418V9f8(0x2c6) = CONST 
    0x241bS0x9f8: v241bV9f8 = GAS 
    0x241cS0x9f8: v241cV9f8 = SUB v241bV9f8, v2418V9f8(0x2c6)
    0x241dS0x9f8: v241dV9f8 = DELEGATECALL v241cV9f8, v22d6V9f8(0xb80f7ad4db894093658474ae57d94345bea474f4), v2405V9f8, v2408V9f8, v2405V9f8, v2401V9f8(0x0)
    0x241eS0x9f8: v241eV9f8 = ISZERO v241dV9f8
    0x241fS0x9f8: v241fV9f8 = ISZERO v241eV9f8
    0x2420S0x9f8: v2420V9f8(0x2428) = CONST 
    0x2423S0x9f8: JUMPI v2420V9f8(0x2428), v241fV9f8

    Begin block 0x2424B0x9f8
    prev=[0x2417B0x9f8], succ=[]
    =================================
    0x2424S0x9f8: v2424V9f8(0x0) = CONST 
    0x2427S0x9f8: REVERT v2424V9f8(0x0), v2424V9f8(0x0)

    Begin block 0x2428B0x9f8
    prev=[0x2417B0x9f8], succ=[0xa75]
    =================================
    0x2431S0x9f8: JUMP v9f9(0xa75)

    Begin block 0xa75
    prev=[0x2428B0x9f8], succ=[]
    =================================
    0xa76: STOP 

    Begin block 0x23deB0x9f8
    prev=[0x23d5B0x9f8], succ=[0x23d5B0x9f8]
    =================================
    0x23de_0x0S0x9f8: v23de_0V9f8 = PHI v23d3V9f8(0x0), v23e9V9f8
    0x23e0S0x9f8: v23e0V9f8 = ADD v23cbV9f8, v23de_0V9f8
    0x23e1S0x9f8: v23e1V9f8 = MLOAD v23e0V9f8
    0x23e4S0x9f8: v23e4V9f8 = ADD v23c3V9f8, v23de_0V9f8
    0x23e5S0x9f8: MSTORE v23e4V9f8, v23e1V9f8
    0x23e6S0x9f8: v23e6V9f8(0x20) = CONST 
    0x23e9S0x9f8: v23e9V9f8 = ADD v23de_0V9f8, v23e6V9f8(0x20)
    0x23ecS0x9f8: v23ecV9f8(0x23d5) = CONST 
    0x23efS0x9f8: JUMP v23ecV9f8(0x23d5)

    Begin block 0x22b9B0x9f8
    prev=[0x22a1B0x9f8], succ=[0x22caB0x9f8]
    =================================
    0x22baS0x9f8: v22baV9f8(0x12) = CONST 
    0x22bcS0x9f8: v22bcV9f8(0x1) = CONST 
    0x22bfS0x9f8: v22bfV9f8 = SLOAD v22baV9f8(0x12)
    0x22c1S0x9f8: v22c1V9f8(0x100) = CONST 
    0x22c4S0x9f8: v22c4V9f8(0x100) = EXP v22c1V9f8(0x100), v22bcV9f8(0x1)
    0x22c6S0x9f8: v22c6V9f8 = DIV v22bfV9f8, v22c4V9f8(0x100)
    0x22c7S0x9f8: v22c7V9f8(0xff) = CONST 
    0x22c9S0x9f8: v22c9V9f8 = AND v22c7V9f8(0xff), v22c6V9f8

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
    prev=[0xa77], succ=[0x2432]
    =================================
    0xa83: va83(0xaae) = CONST 
    0xa86: va86(0x4) = CONST 
    0xa8a: va8a = CALLDATALOAD va86(0x4)
    0xa8b: va8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaa0: vaa0 = AND va8b(0xffffffffffffffffffffffffffffffffffffffff), va8a
    0xaa2: vaa2(0x20) = CONST 
    0xaa4: vaa4(0x24) = ADD vaa2(0x20), va86(0x4)
    0xaaa: vaaa(0x2432) = CONST 
    0xaad: JUMP vaaa(0x2432)

    Begin block 0x2432
    prev=[0xa82], succ=[0x2456, 0x24a6]
    =================================
    0x2433: v2433(0x0) = CONST 
    0x2435: v2435(0x24b0) = CONST 
    0x2438: v2438(0x2) = CONST 
    0x243a: v243a(0x10) = CONST 
    0x243d: v243d(0x20) = CONST 
    0x243f: v243f(0x200) = MUL v243d(0x20), v243a(0x10)
    0x2440: v2440(0x40) = CONST 
    0x2442: v2442 = MLOAD v2440(0x40)
    0x2445: v2445 = ADD v2442, v243f(0x200)
    0x2446: v2446(0x40) = CONST 
    0x2448: MSTORE v2446(0x40), v2445
    0x244e: v244e(0x10) = CONST 
    0x2451: v2451(0x0) = ISZERO v244e(0x10)
    0x2452: v2452(0x24a6) = CONST 
    0x2455: JUMPI v2452(0x24a6), v2451(0x0)

    Begin block 0x2456
    prev=[0x2432], succ=[0x245c]
    =================================
    0x2456: v2456(0x20) = CONST 
    0x2458: v2458(0x200) = MUL v2456(0x20), v244e(0x10)
    0x245a: v245a = ADD v2442, v2458(0x200)

    Begin block 0x245c
    prev=[0x2456, 0x245c], succ=[0x24a6, 0x245c]
    =================================
    0x245c_0x0: v245c_0 = PHI v2442, v2499
    0x245c_0x1: v245c_1 = PHI v2438(0x2), v249d
    0x245e: v245e(0x0) = CONST 
    0x2461: v2461 = SLOAD v245c_1
    0x2463: v2463(0x100) = CONST 
    0x2466: v2466(0x1) = EXP v2463(0x100), v245e(0x0)
    0x2468: v2468 = DIV v2461, v2466(0x1)
    0x2469: v2469(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x247e: v247e = AND v2469(0xffffffffffffffffffffffffffffffffffffffff), v2468
    0x247f: v247f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2494: v2494 = AND v247f(0xffffffffffffffffffffffffffffffffffffffff), v247e
    0x2496: MSTORE v245c_0, v2494
    0x2497: v2497(0x20) = CONST 
    0x2499: v2499 = ADD v2497(0x20), v245c_0
    0x249b: v249b(0x1) = CONST 
    0x249d: v249d = ADD v249b(0x1), v245c_1
    0x24a1: v24a1 = GT v245a, v2499
    0x24a2: v24a2(0x245c) = CONST 
    0x24a5: JUMPI v24a2(0x245c), v24a1

    Begin block 0x24a6
    prev=[0x2432, 0x245c], succ=[0x29ea0xa77]
    =================================
    0x24ac: v24ac(0x29ea) = CONST 
    0x24af: JUMP v24ac(0x29ea)

    Begin block 0x29ea0xa77
    prev=[0x24a6], succ=[0x29fa0xa77, 0x29fb0xa77]
    =================================
    0x29eb0xa77: va7729eb(0x0) = CONST 
    0x29ee0xa77: va7729ee(0x6) = CONST 
    0x29f00xa77: va7729f0(0x10) = CONST 
    0x29f30xa77: va7729f3(0x1) = LT va7729ee(0x6), va7729f0(0x10)
    0x29f40xa77: va7729f4(0x0) = ISZERO va7729f3(0x1)
    0x29f50xa77: va7729f5(0x1) = ISZERO va7729f4(0x0)
    0x29f60xa77: va7729f6(0x29fb) = CONST 
    0x29f90xa77: JUMPI va7729f6(0x29fb), va7729f5(0x1)

    Begin block 0x29fa0xa77
    prev=[0x29ea0xa77], succ=[]
    =================================
    0x29fa0xa77: THROW 

    Begin block 0x29fb0xa77
    prev=[0x29ea0xa77], succ=[0x24b0]
    =================================
    0x29fc0xa77: va7729fc(0x20) = CONST 
    0x29fe0xa77: va7729fe(0xc0) = MUL va7729fc(0x20), va7729ee(0x6)
    0x29ff0xa77: va7729ff = ADD va7729fe(0xc0), v2442
    0x2a000xa77: va772a00 = MLOAD va7729ff
    0x2a060xa77: JUMP v2435(0x24b0)

    Begin block 0x24b0
    prev=[0x29fb0xa77], succ=[0x254e, 0x2552]
    =================================
    0x24b1: v24b1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24c6: v24c6 = AND v24b1(0xffffffffffffffffffffffffffffffffffffffff), va772a00
    0x24c7: v24c7(0xe168a31a) = CONST 
    0x24cd: v24cd(0x0) = CONST 
    0x24cf: v24cf(0x40) = CONST 
    0x24d1: v24d1 = MLOAD v24cf(0x40)
    0x24d2: v24d2(0x20) = CONST 
    0x24d4: v24d4 = ADD v24d2(0x20), v24d1
    0x24d5: MSTORE v24d4, v24cd(0x0)
    0x24d6: v24d6(0x40) = CONST 
    0x24d8: v24d8 = MLOAD v24d6(0x40)
    0x24da: v24da(0xffffffff) = CONST 
    0x24df: v24df(0xe168a31a) = AND v24da(0xffffffff), v24c7(0xe168a31a)
    0x24e0: v24e0(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x24fe: v24fe(0xe168a31a00000000000000000000000000000000000000000000000000000000) = MUL v24e0(0x100000000000000000000000000000000000000000000000000000000), v24df(0xe168a31a)
    0x2500: MSTORE v24d8, v24fe(0xe168a31a00000000000000000000000000000000000000000000000000000000)
    0x2501: v2501(0x4) = CONST 
    0x2503: v2503 = ADD v2501(0x4), v24d8
    0x2506: v2506(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x251b: v251b = AND v2506(0xffffffffffffffffffffffffffffffffffffffff), vaa0
    0x251c: v251c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2531: v2531 = AND v251c(0xffffffffffffffffffffffffffffffffffffffff), v251b
    0x2533: MSTORE v2503, v2531
    0x2534: v2534(0x20) = CONST 
    0x2536: v2536 = ADD v2534(0x20), v2503
    0x253a: v253a(0x20) = CONST 
    0x253c: v253c(0x40) = CONST 
    0x253e: v253e = MLOAD v253c(0x40)
    0x2541: v2541(0x24) = SUB v2536, v253e
    0x2543: v2543(0x0) = CONST 
    0x2547: v2547 = EXTCODESIZE v24c6
    0x2548: v2548 = ISZERO v2547
    0x2549: v2549 = ISZERO v2548
    0x254a: v254a(0x2552) = CONST 
    0x254d: JUMPI v254a(0x2552), v2549

    Begin block 0x254e
    prev=[0x24b0], succ=[]
    =================================
    0x254e: v254e(0x0) = CONST 
    0x2551: REVERT v254e(0x0), v254e(0x0)

    Begin block 0x2552
    prev=[0x24b0], succ=[0x255f, 0x2563]
    =================================
    0x2553: v2553(0x2c6) = CONST 
    0x2556: v2556 = GAS 
    0x2557: v2557 = SUB v2556, v2553(0x2c6)
    0x2558: v2558 = CALL v2557, v24c6, v2543(0x0), v253e, v2541(0x24), v253e, v253a(0x20)
    0x2559: v2559 = ISZERO v2558
    0x255a: v255a = ISZERO v2559
    0x255b: v255b(0x2563) = CONST 
    0x255e: JUMPI v255b(0x2563), v255a

    Begin block 0x255f
    prev=[0x2552], succ=[]
    =================================
    0x255f: v255f(0x0) = CONST 
    0x2562: REVERT v255f(0x0), v255f(0x0)

    Begin block 0x2563
    prev=[0x2552], succ=[0xaae]
    =================================
    0x2567: v2567(0x40) = CONST 
    0x2569: v2569 = MLOAD v2567(0x40)
    0x256b: v256b = MLOAD v2569
    0x2573: JUMP va83(0xaae)

    Begin block 0xaae
    prev=[0x2563], succ=[]
    =================================
    0xaaf: vaaf(0x40) = CONST 
    0xab1: vab1 = MLOAD vaaf(0x40)
    0xab5: MSTORE vab1, v256b
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
    prev=[0xac4], succ=[0x2574B0xacf]
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
    0xb40: vb40(0x2574) = CONST 
    0xb43: JUMP vb40(0x2574), vb36, vb2b, vb02, vae0, vad7, vad0(0xb44)

    Begin block 0x2574B0xacf
    prev=[0xacf], succ=[0x25ceB0xacf, 0x261eB0xacf]
    =================================
    0x2575S0xacf: v2575Vacf(0xb80f7ad4db894093658474ae57d94345bea474f4) = CONST 
    0x258aS0xacf: v258aVacf(0x33840712) = CONST 
    0x258fS0xacf: v258fVacf(0x2) = CONST 
    0x2596S0xacf: v2596Vacf(0x40) = CONST 
    0x2598S0xacf: v2598Vacf = MLOAD v2596Vacf(0x40)
    0x259aS0xacf: v259aVacf(0xffffffff) = CONST 
    0x259fS0xacf: v259fVacf(0x33840712) = AND v259aVacf(0xffffffff), v258aVacf(0x33840712)
    0x25a0S0xacf: v25a0Vacf(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x25beS0xacf: v25beVacf(0x3384071200000000000000000000000000000000000000000000000000000000) = MUL v25a0Vacf(0x100000000000000000000000000000000000000000000000000000000), v259fVacf(0x33840712)
    0x25c0S0xacf: MSTORE v2598Vacf, v25beVacf(0x3384071200000000000000000000000000000000000000000000000000000000)
    0x25c1S0xacf: v25c1Vacf(0x4) = CONST 
    0x25c3S0xacf: v25c3Vacf = ADD v25c1Vacf(0x4), v2598Vacf
    0x25c6S0xacf: v25c6Vacf(0x10) = CONST 
    0x25c9S0xacf: v25c9Vacf(0x0) = ISZERO v25c6Vacf(0x10)
    0x25caS0xacf: v25caVacf(0x261e) = CONST 
    0x25cdS0xacf: JUMPI v25caVacf(0x261e), v25c9Vacf(0x0)

    Begin block 0x25ceB0xacf
    prev=[0x2574B0xacf], succ=[0x25d4B0xacf]
    =================================
    0x25ceS0xacf: v25ceVacf(0x20) = CONST 
    0x25d0S0xacf: v25d0Vacf(0x200) = MUL v25ceVacf(0x20), v25c6Vacf(0x10)
    0x25d2S0xacf: v25d2Vacf = ADD v25c3Vacf, v25d0Vacf(0x200)

    Begin block 0x25d4B0xacf
    prev=[0x25ceB0xacf, 0x25d4B0xacf], succ=[0x261eB0xacf, 0x25d4B0xacf]
    =================================
    0x25d4_0x0S0xacf: v25d4_0Vacf = PHI v25c3Vacf, v2611Vacf
    0x25d4_0x1S0xacf: v25d4_1Vacf = PHI v258fVacf(0x2), v2615Vacf
    0x25d6S0xacf: v25d6Vacf(0x0) = CONST 
    0x25d9S0xacf: v25d9Vacf = SLOAD v25d4_1Vacf
    0x25dbS0xacf: v25dbVacf(0x100) = CONST 
    0x25deS0xacf: v25deVacf(0x1) = EXP v25dbVacf(0x100), v25d6Vacf(0x0)
    0x25e0S0xacf: v25e0Vacf = DIV v25d9Vacf, v25deVacf(0x1)
    0x25e1S0xacf: v25e1Vacf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25f6S0xacf: v25f6Vacf = AND v25e1Vacf(0xffffffffffffffffffffffffffffffffffffffff), v25e0Vacf
    0x25f7S0xacf: v25f7Vacf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x260cS0xacf: v260cVacf = AND v25f7Vacf(0xffffffffffffffffffffffffffffffffffffffff), v25f6Vacf
    0x260eS0xacf: MSTORE v25d4_0Vacf, v260cVacf
    0x260fS0xacf: v260fVacf(0x20) = CONST 
    0x2611S0xacf: v2611Vacf = ADD v260fVacf(0x20), v25d4_0Vacf
    0x2613S0xacf: v2613Vacf(0x1) = CONST 
    0x2615S0xacf: v2615Vacf = ADD v2613Vacf(0x1), v25d4_1Vacf
    0x2619S0xacf: v2619Vacf = GT v25d2Vacf, v2611Vacf
    0x261aS0xacf: v261aVacf(0x25d4) = CONST 
    0x261dS0xacf: JUMPI v261aVacf(0x25d4), v2619Vacf

    Begin block 0x261eB0xacf
    prev=[0x2574B0xacf, 0x25d4B0xacf], succ=[0x2664B0xacf]
    =================================
    0x261e_0x2S0xacf: v261e_2Vacf = PHI v25d2Vacf, v25c3Vacf
    0x2623S0xacf: MSTORE v261e_2Vacf, vad7
    0x2624S0xacf: v2624Vacf(0x20) = CONST 
    0x2626S0xacf: v2626Vacf = ADD v2624Vacf(0x20), v261e_2Vacf
    0x2629S0xacf: MSTORE v2626Vacf, vae0
    0x262aS0xacf: v262aVacf(0x20) = CONST 
    0x262cS0xacf: v262cVacf = ADD v262aVacf(0x20), v2626Vacf
    0x262eS0xacf: v262eVacf(0x20) = CONST 
    0x2630S0xacf: v2630Vacf = ADD v262eVacf(0x20), v262cVacf
    0x2632S0xacf: v2632Vacf = ISZERO vb2b
    0x2633S0xacf: v2633Vacf = ISZERO v2632Vacf
    0x2634S0xacf: v2634Vacf = ISZERO v2633Vacf
    0x2635S0xacf: v2635Vacf = ISZERO v2634Vacf
    0x2637S0xacf: MSTORE v2630Vacf, v2635Vacf
    0x2638S0xacf: v2638Vacf(0x20) = CONST 
    0x263aS0xacf: v263aVacf = ADD v2638Vacf(0x20), v2630Vacf
    0x263cS0xacf: v263cVacf = ISZERO vb36
    0x263dS0xacf: v263dVacf = ISZERO v263cVacf
    0x263eS0xacf: v263eVacf = ISZERO v263dVacf
    0x263fS0xacf: v263fVacf = ISZERO v263eVacf
    0x2641S0xacf: MSTORE v263aVacf, v263fVacf
    0x2642S0xacf: v2642Vacf(0x20) = CONST 
    0x2644S0xacf: v2644Vacf = ADD v2642Vacf(0x20), v263aVacf
    0x2647S0xacf: v2647Vacf = SUB v2644Vacf, v25c3Vacf
    0x2649S0xacf: MSTORE v262cVacf, v2647Vacf
    0x264dS0xacf: v264dVacf = MLOAD vb02
    0x264fS0xacf: MSTORE v2644Vacf, v264dVacf
    0x2650S0xacf: v2650Vacf(0x20) = CONST 
    0x2652S0xacf: v2652Vacf = ADD v2650Vacf(0x20), v2644Vacf
    0x2656S0xacf: v2656Vacf = MLOAD vb02
    0x2658S0xacf: v2658Vacf(0x20) = CONST 
    0x265aS0xacf: v265aVacf = ADD v2658Vacf(0x20), vb02
    0x265cS0xacf: v265cVacf(0x20) = CONST 
    0x265eS0xacf: v265eVacf = MUL v265cVacf(0x20), v2656Vacf
    0x2662S0xacf: v2662Vacf(0x0) = CONST 

    Begin block 0x2664B0xacf
    prev=[0x261eB0xacf, 0x266dB0xacf], succ=[0x267fB0xacf, 0x266dB0xacf]
    =================================
    0x2664_0x0S0xacf: v2664_0Vacf = PHI v2662Vacf(0x0), v2678Vacf
    0x2667S0xacf: v2667Vacf = LT v2664_0Vacf, v265eVacf
    0x2668S0xacf: v2668Vacf = ISZERO v2667Vacf
    0x2669S0xacf: v2669Vacf(0x267f) = CONST 
    0x266cS0xacf: JUMPI v2669Vacf(0x267f), v2668Vacf

    Begin block 0x267fB0xacf
    prev=[0x2664B0xacf], succ=[0x26a2B0xacf, 0x26a6B0xacf]
    =================================
    0x2686S0xacf: v2686Vacf = ADD v265eVacf, v2652Vacf
    0x2690S0xacf: v2690Vacf(0x0) = CONST 
    0x2692S0xacf: v2692Vacf(0x40) = CONST 
    0x2694S0xacf: v2694Vacf = MLOAD v2692Vacf(0x40)
    0x2697S0xacf: v2697Vacf = SUB v2686Vacf, v2694Vacf
    0x269bS0xacf: v269bVacf = EXTCODESIZE v2575Vacf(0xb80f7ad4db894093658474ae57d94345bea474f4)
    0x269cS0xacf: v269cVacf = ISZERO v269bVacf
    0x269dS0xacf: v269dVacf = ISZERO v269cVacf
    0x269eS0xacf: v269eVacf(0x26a6) = CONST 
    0x26a1S0xacf: JUMPI v269eVacf(0x26a6), v269dVacf

    Begin block 0x26a2B0xacf
    prev=[0x267fB0xacf], succ=[]
    =================================
    0x26a2S0xacf: v26a2Vacf(0x0) = CONST 
    0x26a5S0xacf: REVERT v26a2Vacf(0x0), v26a2Vacf(0x0)

    Begin block 0x26a6B0xacf
    prev=[0x267fB0xacf], succ=[0x26b3B0xacf, 0x26b7B0xacf]
    =================================
    0x26a7S0xacf: v26a7Vacf(0x2c6) = CONST 
    0x26aaS0xacf: v26aaVacf = GAS 
    0x26abS0xacf: v26abVacf = SUB v26aaVacf, v26a7Vacf(0x2c6)
    0x26acS0xacf: v26acVacf = DELEGATECALL v26abVacf, v2575Vacf(0xb80f7ad4db894093658474ae57d94345bea474f4), v2694Vacf, v2697Vacf, v2694Vacf, v2690Vacf(0x0)
    0x26adS0xacf: v26adVacf = ISZERO v26acVacf
    0x26aeS0xacf: v26aeVacf = ISZERO v26adVacf
    0x26afS0xacf: v26afVacf(0x26b7) = CONST 
    0x26b2S0xacf: JUMPI v26afVacf(0x26b7), v26aeVacf

    Begin block 0x26b3B0xacf
    prev=[0x26a6B0xacf], succ=[]
    =================================
    0x26b3S0xacf: v26b3Vacf(0x0) = CONST 
    0x26b6S0xacf: REVERT v26b3Vacf(0x0), v26b3Vacf(0x0)

    Begin block 0x26b7B0xacf
    prev=[0x26a6B0xacf], succ=[0xb44]
    =================================
    0x26c0S0xacf: JUMP vad0(0xb44)

    Begin block 0xb44
    prev=[0x26b7B0xacf], succ=[]
    =================================
    0xb45: STOP 

    Begin block 0x266dB0xacf
    prev=[0x2664B0xacf], succ=[0x2664B0xacf]
    =================================
    0x266d_0x0S0xacf: v266d_0Vacf = PHI v2662Vacf(0x0), v2678Vacf
    0x266fS0xacf: v266fVacf = ADD v265aVacf, v266d_0Vacf
    0x2670S0xacf: v2670Vacf = MLOAD v266fVacf
    0x2673S0xacf: v2673Vacf = ADD v2652Vacf, v266d_0Vacf
    0x2674S0xacf: MSTORE v2673Vacf, v2670Vacf
    0x2675S0xacf: v2675Vacf(0x20) = CONST 
    0x2678S0xacf: v2678Vacf = ADD v266d_0Vacf, v2675Vacf(0x20)
    0x267bS0xacf: v267bVacf(0x2664) = CONST 
    0x267eS0xacf: JUMP v267bVacf(0x2664)

}

function purchase(uint256)() public {
    Begin block 0xb46
    prev=[], succ=[0x26c1B0xb46]
    =================================
    0xb47: vb47(0xb5c) = CONST 
    0xb4a: vb4a(0x4) = CONST 
    0xb4e: vb4e = CALLDATALOAD vb4a(0x4)
    0xb50: vb50(0x20) = CONST 
    0xb52: vb52(0x24) = ADD vb50(0x20), vb4a(0x4)
    0xb58: vb58(0x26c1) = CONST 
    0xb5b: JUMP vb58(0x26c1), vb4e, vb47(0xb5c)

    Begin block 0x26c1B0xb46
    prev=[0xb46], succ=[0x26eaB0xb46, 0x26d9B0xb46]
    =================================
    0x26c2S0xb46: v26c2Vb46(0x12) = CONST 
    0x26c4S0xb46: v26c4Vb46(0x0) = CONST 
    0x26c7S0xb46: v26c7Vb46 = SLOAD v26c2Vb46(0x12)
    0x26c9S0xb46: v26c9Vb46(0x100) = CONST 
    0x26ccS0xb46: v26ccVb46(0x1) = EXP v26c9Vb46(0x100), v26c4Vb46(0x0)
    0x26ceS0xb46: v26ceVb46 = DIV v26c7Vb46, v26ccVb46(0x1)
    0x26cfS0xb46: v26cfVb46(0xff) = CONST 
    0x26d1S0xb46: v26d1Vb46 = AND v26cfVb46(0xff), v26ceVb46
    0x26d2S0xb46: v26d2Vb46 = ISZERO v26d1Vb46
    0x26d4S0xb46: v26d4Vb46 = ISZERO v26d2Vb46
    0x26d5S0xb46: v26d5Vb46(0x26ea) = CONST 
    0x26d8S0xb46: JUMPI v26d5Vb46(0x26ea), v26d4Vb46

    Begin block 0x26eaB0xb46
    prev=[0x26c1B0xb46, 0x26d9B0xb46], succ=[0x26f1B0xb46, 0x26f5B0xb46]
    =================================
    0x26ea_0x0S0xb46: v26ea_0Vb46 = PHI v26d2Vb46, v26e9Vb46
    0x26ebS0xb46: v26ebVb46 = ISZERO v26ea_0Vb46
    0x26ecS0xb46: v26ecVb46 = ISZERO v26ebVb46
    0x26edS0xb46: v26edVb46(0x26f5) = CONST 
    0x26f0S0xb46: JUMPI v26edVb46(0x26f5), v26ecVb46

    Begin block 0x26f1B0xb46
    prev=[0x26eaB0xb46], succ=[]
    =================================
    0x26f1S0xb46: v26f1Vb46(0x0) = CONST 
    0x26f4S0xb46: REVERT v26f1Vb46(0x0), v26f1Vb46(0x0)

    Begin block 0x26f5B0xb46
    prev=[0x26eaB0xb46], succ=[0x274bB0xb46, 0x279bB0xb46]
    =================================
    0x26f6S0xb46: v26f6Vb46(0x1d7b5788d3844010664900615e966f8e9e464738) = CONST 
    0x270bS0xb46: v270bVb46(0x1fc7d658) = CONST 
    0x2710S0xb46: v2710Vb46(0x2) = CONST 
    0x2713S0xb46: v2713Vb46(0x40) = CONST 
    0x2715S0xb46: v2715Vb46 = MLOAD v2713Vb46(0x40)
    0x2717S0xb46: v2717Vb46(0xffffffff) = CONST 
    0x271cS0xb46: v271cVb46(0x1fc7d658) = AND v2717Vb46(0xffffffff), v270bVb46(0x1fc7d658)
    0x271dS0xb46: v271dVb46(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x273bS0xb46: v273bVb46(0x1fc7d65800000000000000000000000000000000000000000000000000000000) = MUL v271dVb46(0x100000000000000000000000000000000000000000000000000000000), v271cVb46(0x1fc7d658)
    0x273dS0xb46: MSTORE v2715Vb46, v273bVb46(0x1fc7d65800000000000000000000000000000000000000000000000000000000)
    0x273eS0xb46: v273eVb46(0x4) = CONST 
    0x2740S0xb46: v2740Vb46 = ADD v273eVb46(0x4), v2715Vb46
    0x2743S0xb46: v2743Vb46(0x10) = CONST 
    0x2746S0xb46: v2746Vb46(0x0) = ISZERO v2743Vb46(0x10)
    0x2747S0xb46: v2747Vb46(0x279b) = CONST 
    0x274aS0xb46: JUMPI v2747Vb46(0x279b), v2746Vb46(0x0)

    Begin block 0x274bB0xb46
    prev=[0x26f5B0xb46], succ=[0x2751B0xb46]
    =================================
    0x274bS0xb46: v274bVb46(0x20) = CONST 
    0x274dS0xb46: v274dVb46(0x200) = MUL v274bVb46(0x20), v2743Vb46(0x10)
    0x274fS0xb46: v274fVb46 = ADD v2740Vb46, v274dVb46(0x200)

    Begin block 0x2751B0xb46
    prev=[0x274bB0xb46, 0x2751B0xb46], succ=[0x279bB0xb46, 0x2751B0xb46]
    =================================
    0x2751_0x0S0xb46: v2751_0Vb46 = PHI v2740Vb46, v278eVb46
    0x2751_0x1S0xb46: v2751_1Vb46 = PHI v2710Vb46(0x2), v2792Vb46
    0x2753S0xb46: v2753Vb46(0x0) = CONST 
    0x2756S0xb46: v2756Vb46 = SLOAD v2751_1Vb46
    0x2758S0xb46: v2758Vb46(0x100) = CONST 
    0x275bS0xb46: v275bVb46(0x1) = EXP v2758Vb46(0x100), v2753Vb46(0x0)
    0x275dS0xb46: v275dVb46 = DIV v2756Vb46, v275bVb46(0x1)
    0x275eS0xb46: v275eVb46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2773S0xb46: v2773Vb46 = AND v275eVb46(0xffffffffffffffffffffffffffffffffffffffff), v275dVb46
    0x2774S0xb46: v2774Vb46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2789S0xb46: v2789Vb46 = AND v2774Vb46(0xffffffffffffffffffffffffffffffffffffffff), v2773Vb46
    0x278bS0xb46: MSTORE v2751_0Vb46, v2789Vb46
    0x278cS0xb46: v278cVb46(0x20) = CONST 
    0x278eS0xb46: v278eVb46 = ADD v278cVb46(0x20), v2751_0Vb46
    0x2790S0xb46: v2790Vb46(0x1) = CONST 
    0x2792S0xb46: v2792Vb46 = ADD v2790Vb46(0x1), v2751_1Vb46
    0x2796S0xb46: v2796Vb46 = GT v274fVb46, v278eVb46
    0x2797S0xb46: v2797Vb46(0x2751) = CONST 
    0x279aS0xb46: JUMPI v2797Vb46(0x2751), v2796Vb46

    Begin block 0x279bB0xb46
    prev=[0x26f5B0xb46, 0x2751B0xb46], succ=[0x27baB0xb46, 0x27beB0xb46]
    =================================
    0x279b_0x2S0xb46: v279b_2Vb46 = PHI v274fVb46, v2740Vb46
    0x27a0S0xb46: MSTORE v279b_2Vb46, vb4e
    0x27a1S0xb46: v27a1Vb46(0x20) = CONST 
    0x27a3S0xb46: v27a3Vb46 = ADD v27a1Vb46(0x20), v279b_2Vb46
    0x27a8S0xb46: v27a8Vb46(0x0) = CONST 
    0x27aaS0xb46: v27aaVb46(0x40) = CONST 
    0x27acS0xb46: v27acVb46 = MLOAD v27aaVb46(0x40)
    0x27afS0xb46: v27afVb46 = SUB v27a3Vb46, v27acVb46
    0x27b3S0xb46: v27b3Vb46 = EXTCODESIZE v26f6Vb46(0x1d7b5788d3844010664900615e966f8e9e464738)
    0x27b4S0xb46: v27b4Vb46 = ISZERO v27b3Vb46
    0x27b5S0xb46: v27b5Vb46 = ISZERO v27b4Vb46
    0x27b6S0xb46: v27b6Vb46(0x27be) = CONST 
    0x27b9S0xb46: JUMPI v27b6Vb46(0x27be), v27b5Vb46

    Begin block 0x27baB0xb46
    prev=[0x279bB0xb46], succ=[]
    =================================
    0x27baS0xb46: v27baVb46(0x0) = CONST 
    0x27bdS0xb46: REVERT v27baVb46(0x0), v27baVb46(0x0)

    Begin block 0x27beB0xb46
    prev=[0x279bB0xb46], succ=[0x27cbB0xb46, 0x27cfB0xb46]
    =================================
    0x27bfS0xb46: v27bfVb46(0x2c6) = CONST 
    0x27c2S0xb46: v27c2Vb46 = GAS 
    0x27c3S0xb46: v27c3Vb46 = SUB v27c2Vb46, v27bfVb46(0x2c6)
    0x27c4S0xb46: v27c4Vb46 = DELEGATECALL v27c3Vb46, v26f6Vb46(0x1d7b5788d3844010664900615e966f8e9e464738), v27acVb46, v27afVb46, v27acVb46, v27a8Vb46(0x0)
    0x27c5S0xb46: v27c5Vb46 = ISZERO v27c4Vb46
    0x27c6S0xb46: v27c6Vb46 = ISZERO v27c5Vb46
    0x27c7S0xb46: v27c7Vb46(0x27cf) = CONST 
    0x27caS0xb46: JUMPI v27c7Vb46(0x27cf), v27c6Vb46

    Begin block 0x27cbB0xb46
    prev=[0x27beB0xb46], succ=[]
    =================================
    0x27cbS0xb46: v27cbVb46(0x0) = CONST 
    0x27ceS0xb46: REVERT v27cbVb46(0x0), v27cbVb46(0x0)

    Begin block 0x27cfB0xb46
    prev=[0x27beB0xb46], succ=[0xb5c]
    =================================
    0x27d4S0xb46: JUMP vb47(0xb5c)

    Begin block 0xb5c
    prev=[0x27cfB0xb46], succ=[]
    =================================
    0xb5d: STOP 

    Begin block 0x26d9B0xb46
    prev=[0x26c1B0xb46], succ=[0x26eaB0xb46]
    =================================
    0x26daS0xb46: v26daVb46(0x12) = CONST 
    0x26dcS0xb46: v26dcVb46(0x1) = CONST 
    0x26dfS0xb46: v26dfVb46 = SLOAD v26daVb46(0x12)
    0x26e1S0xb46: v26e1Vb46(0x100) = CONST 
    0x26e4S0xb46: v26e4Vb46(0x100) = EXP v26e1Vb46(0x100), v26dcVb46(0x1)
    0x26e6S0xb46: v26e6Vb46 = DIV v26dfVb46, v26e4Vb46(0x100)
    0x26e7S0xb46: v26e7Vb46(0xff) = CONST 
    0x26e9S0xb46: v26e9Vb46 = AND v26e7Vb46(0xff), v26e6Vb46

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
    prev=[0xb5e], succ=[0x27d5B0xb69]
    =================================
    0xb6a: vb6a(0xb7e) = CONST 
    0xb6d: vb6d(0x4) = CONST 
    0xb71: vb71(0x200) = CONST 
    0xb74: vb74(0x204) = ADD vb71(0x200), vb6d(0x4)
    0xb7a: vb7a(0x27d5) = CONST 
    0xb7d: JUMP vb7a(0x27d5), vb6d(0x4), vb6a(0xb7e)

    Begin block 0x27d5B0xb69
    prev=[0xb69], succ=[0x282cB0xb69, 0x2830B0xb69]
    =================================
    0x27d6S0xb69: v27d6Vb69(0x0) = CONST 
    0x27daS0xb69: v27daVb69 = SLOAD v27d6Vb69(0x0)
    0x27dcS0xb69: v27dcVb69(0x100) = CONST 
    0x27dfS0xb69: v27dfVb69(0x1) = EXP v27dcVb69(0x100), v27d6Vb69(0x0)
    0x27e1S0xb69: v27e1Vb69 = DIV v27daVb69, v27dfVb69(0x1)
    0x27e2S0xb69: v27e2Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27f7S0xb69: v27f7Vb69 = AND v27e2Vb69(0xffffffffffffffffffffffffffffffffffffffff), v27e1Vb69
    0x27f8S0xb69: v27f8Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x280dS0xb69: v280dVb69 = AND v27f8Vb69(0xffffffffffffffffffffffffffffffffffffffff), v27f7Vb69
    0x280eS0xb69: v280eVb69 = CALLER 
    0x280fS0xb69: v280fVb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2824S0xb69: v2824Vb69 = AND v280fVb69(0xffffffffffffffffffffffffffffffffffffffff), v280eVb69
    0x2825S0xb69: v2825Vb69 = EQ v2824Vb69, v280dVb69
    0x2826S0xb69: v2826Vb69 = ISZERO v2825Vb69
    0x2827S0xb69: v2827Vb69 = ISZERO v2826Vb69
    0x2828S0xb69: v2828Vb69(0x2830) = CONST 
    0x282bS0xb69: JUMPI v2828Vb69(0x2830), v2827Vb69

    Begin block 0x282cB0xb69
    prev=[0x27d5B0xb69], succ=[]
    =================================
    0x282cS0xb69: v282cVb69(0x0) = CONST 
    0x282fS0xb69: REVERT v282cVb69(0x0), v282cVb69(0x0)

    Begin block 0x2830B0xb69
    prev=[0x27d5B0xb69], succ=[0x2a2fB0x2830B0xb69]
    =================================
    0x2832S0xb69: v2832Vb69(0x2) = CONST 
    0x2835S0xb69: v2835Vb69(0x10) = CONST 
    0x2837S0xb69: v2837Vb69(0x2841) = CONST 
    0x283dS0xb69: v283dVb69(0x2a2f) = CONST 
    0x2840S0xb69: JUMP v283dVb69(0x2a2f)

    Begin block 0x2a2fB0x2830B0xb69
    prev=[0x2830B0xb69], succ=[0x2ab1B0x2830B0xb69, 0x2a3cB0x2830B0xb69]
    =================================
    0x2a31S0x2830S0xb69: v2a31V2830Vb69(0x10) = CONST 
    0x2a34S0x2830S0xb69: v2a34V2830Vb69(0x12) = ADD v2832Vb69(0x2), v2a31V2830Vb69(0x10)
    0x2a37S0x2830S0xb69: v2a37V2830Vb69 = ISZERO v2835Vb69(0x10)
    0x2a38S0x2830S0xb69: v2a38V2830Vb69(0x2ab1) = CONST 
    0x2a3bS0x2830S0xb69: JUMPI v2a38V2830Vb69(0x2ab1), v2a37V2830Vb69

    Begin block 0x2ab1B0x2830B0xb69
    prev=[0x2a2fB0x2830B0xb69, 0x2ab0B0x2830B0xb69], succ=[0x2ac2B0x2ab1B0x2830B0xb69]
    =================================
    0x2ab1_0x1S0x2830S0xb69: v2ab1_1V2830Vb69 = PHI v2832Vb69(0x2), v2aaaV2830Vb69
    0x2ab5S0x2830S0xb69: v2ab5V2830Vb69(0x2abe) = CONST 
    0x2abaS0x2830S0xb69: v2abaV2830Vb69(0x2ac2) = CONST 
    0x2abdS0x2830S0xb69: JUMP v2abaV2830Vb69(0x2ac2)

    Begin block 0x2ac2B0x2ab1B0x2830B0xb69
    prev=[0x2ab1B0x2830B0xb69], succ=[0x2ac8B0x2ab1B0x2830B0xb69]
    =================================
    0x2ac3S0x2ab1S0x2830S0xb69: v2ac3V2ab1V2830Vb69(0x2b02) = CONST 

    Begin block 0x2ac8B0x2ab1B0x2830B0xb69
    prev=[0x2ad1B0x2ab1B0x2830B0xb69, 0x2ac2B0x2ab1B0x2830B0xb69], succ=[0x2ad1B0x2ab1B0x2830B0xb69, 0x2afeB0x2ab1B0x2830B0xb69]
    =================================
    0x2ac8_0x0S0x2ab1S0x2830S0xb69: v2ac8_0V2ab1V2830Vb69 = PHI v2ab1_1V2830Vb69, v2af9V2ab1V2830Vb69
    0x2acbS0x2ab1S0x2830S0xb69: v2acbV2ab1V2830Vb69 = GT v2a34V2830Vb69(0x12), v2ac8_0V2ab1V2830Vb69
    0x2accS0x2ab1S0x2830S0xb69: v2accV2ab1V2830Vb69 = ISZERO v2acbV2ab1V2830Vb69
    0x2acdS0x2ab1S0x2830S0xb69: v2acdV2ab1V2830Vb69(0x2afe) = CONST 
    0x2ad0S0x2ab1S0x2830S0xb69: JUMPI v2acdV2ab1V2830Vb69(0x2afe), v2accV2ab1V2830Vb69

    Begin block 0x2ad1B0x2ab1B0x2830B0xb69
    prev=[0x2ac8B0x2ab1B0x2830B0xb69], succ=[0x2ac8B0x2ab1B0x2830B0xb69]
    =================================
    0x2ad1S0x2ab1S0x2830S0xb69: v2ad1V2ab1V2830Vb69(0x0) = CONST 
    0x2ad1_0x0S0x2ab1S0x2830S0xb69: v2ad1_0V2ab1V2830Vb69 = PHI v2ab1_1V2830Vb69, v2af9V2ab1V2830Vb69
    0x2ad5S0x2ab1S0x2830S0xb69: v2ad5V2ab1V2830Vb69(0x100) = CONST 
    0x2ad8S0x2ab1S0x2830S0xb69: v2ad8V2ab1V2830Vb69(0x1) = EXP v2ad5V2ab1V2830Vb69(0x100), v2ad1V2ab1V2830Vb69(0x0)
    0x2adaS0x2ab1S0x2830S0xb69: v2adaV2ab1V2830Vb69 = SLOAD v2ad1_0V2ab1V2830Vb69
    0x2adcS0x2ab1S0x2830S0xb69: v2adcV2ab1V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2af1S0x2ab1S0x2830S0xb69: v2af1V2ab1V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2adcV2ab1V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff), v2ad8V2ab1V2830Vb69(0x1)
    0x2af2S0x2ab1S0x2830S0xb69: v2af2V2ab1V2830Vb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2af1V2ab1V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff)
    0x2af3S0x2ab1S0x2830S0xb69: v2af3V2ab1V2830Vb69 = AND v2af2V2ab1V2830Vb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2adaV2ab1V2830Vb69
    0x2af5S0x2ab1S0x2830S0xb69: SSTORE v2ad1_0V2ab1V2830Vb69, v2af3V2ab1V2830Vb69
    0x2af7S0x2ab1S0x2830S0xb69: v2af7V2ab1V2830Vb69(0x1) = CONST 
    0x2af9S0x2ab1S0x2830S0xb69: v2af9V2ab1V2830Vb69 = ADD v2af7V2ab1V2830Vb69(0x1), v2ad1_0V2ab1V2830Vb69
    0x2afaS0x2ab1S0x2830S0xb69: v2afaV2ab1V2830Vb69(0x2ac8) = CONST 
    0x2afdS0x2ab1S0x2830S0xb69: JUMP v2afaV2ab1V2830Vb69(0x2ac8)

    Begin block 0x2afeB0x2ab1B0x2830B0xb69
    prev=[0x2ac8B0x2ab1B0x2830B0xb69], succ=[0x2b02B0x2ab1B0x2830B0xb69]
    =================================
    0x2b01S0x2ab1S0x2830S0xb69: JUMP v2ac3V2ab1V2830Vb69(0x2b02)

    Begin block 0x2b02B0x2ab1B0x2830B0xb69
    prev=[0x2afeB0x2ab1B0x2830B0xb69], succ=[0x2abeB0x2830B0xb69]
    =================================
    0x2b04S0x2ab1S0x2830S0xb69: JUMP v2ab5V2830Vb69(0x2abe)

    Begin block 0x2abeB0x2830B0xb69
    prev=[0x2b02B0x2ab1B0x2830B0xb69], succ=[0x2841B0xb69]
    =================================
    0x2ac1S0x2830S0xb69: JUMP v2837Vb69(0x2841)

    Begin block 0x2841B0xb69
    prev=[0x2abeB0x2830B0xb69], succ=[0xb7e]
    =================================
    0x2844S0xb69: JUMP vb6a(0xb7e)

    Begin block 0xb7e
    prev=[0x2841B0xb69], succ=[]
    =================================
    0xb7f: STOP 

    Begin block 0x2a3cB0x2830B0xb69
    prev=[0x2a2fB0x2830B0xb69], succ=[0x2a42B0x2830B0xb69]
    =================================
    0x2a3dS0x2830S0xb69: v2a3dV2830Vb69(0x20) = CONST 
    0x2a3fS0x2830S0xb69: v2a3fV2830Vb69(0x200) = MUL v2a3dV2830Vb69(0x20), v2835Vb69(0x10)
    0x2a41S0x2830S0xb69: v2a41V2830Vb69(0x204) = ADD vb6d(0x4), v2a3fV2830Vb69(0x200)

    Begin block 0x2a42B0x2830B0xb69
    prev=[0x2a3cB0x2830B0xb69, 0x2a4bB0x2830B0xb69], succ=[0x2a4bB0x2830B0xb69, 0x2ab0B0x2830B0xb69]
    =================================
    0x2a42_0x2S0x2830S0xb69: v2a42_2V2830Vb69 = PHI vb6d(0x4), v2aa5V2830Vb69
    0x2a45S0x2830S0xb69: v2a45V2830Vb69 = GT v2a41V2830Vb69(0x204), v2a42_2V2830Vb69
    0x2a46S0x2830S0xb69: v2a46V2830Vb69 = ISZERO v2a45V2830Vb69
    0x2a47S0x2830S0xb69: v2a47V2830Vb69(0x2ab0) = CONST 
    0x2a4aS0x2830S0xb69: JUMPI v2a47V2830Vb69(0x2ab0), v2a46V2830Vb69

    Begin block 0x2a4bB0x2830B0xb69
    prev=[0x2a42B0x2830B0xb69], succ=[0x2a42B0x2830B0xb69]
    =================================
    0x2a4b_0x1S0x2830S0xb69: v2a4b_1V2830Vb69 = PHI v2832Vb69(0x2), v2aaaV2830Vb69
    0x2a4b_0x2S0x2830S0xb69: v2a4b_2V2830Vb69 = PHI vb6d(0x4), v2aa5V2830Vb69
    0x2a4cS0x2830S0xb69: v2a4cV2830Vb69 = CALLDATALOAD v2a4b_2V2830Vb69
    0x2a4dS0x2830S0xb69: v2a4dV2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a62S0x2830S0xb69: v2a62V2830Vb69 = AND v2a4dV2830Vb69(0xffffffffffffffffffffffffffffffffffffffff), v2a4cV2830Vb69
    0x2a64S0x2830S0xb69: v2a64V2830Vb69(0x0) = CONST 
    0x2a66S0x2830S0xb69: v2a66V2830Vb69(0x100) = CONST 
    0x2a69S0x2830S0xb69: v2a69V2830Vb69(0x1) = EXP v2a66V2830Vb69(0x100), v2a64V2830Vb69(0x0)
    0x2a6bS0x2830S0xb69: v2a6bV2830Vb69 = SLOAD v2a4b_1V2830Vb69
    0x2a6dS0x2830S0xb69: v2a6dV2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a82S0x2830S0xb69: v2a82V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2a6dV2830Vb69(0xffffffffffffffffffffffffffffffffffffffff), v2a69V2830Vb69(0x1)
    0x2a83S0x2830S0xb69: v2a83V2830Vb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2a82V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a84S0x2830S0xb69: v2a84V2830Vb69 = AND v2a83V2830Vb69(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2a6bV2830Vb69
    0x2a87S0x2830S0xb69: v2a87V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a9cS0x2830S0xb69: v2a9cV2830Vb69 = AND v2a87V2830Vb69(0xffffffffffffffffffffffffffffffffffffffff), v2a62V2830Vb69
    0x2a9dS0x2830S0xb69: v2a9dV2830Vb69 = MUL v2a9cV2830Vb69, v2a69V2830Vb69(0x1)
    0x2a9eS0x2830S0xb69: v2a9eV2830Vb69 = OR v2a9dV2830Vb69, v2a84V2830Vb69
    0x2aa0S0x2830S0xb69: SSTORE v2a4b_1V2830Vb69, v2a9eV2830Vb69
    0x2aa3S0x2830S0xb69: v2aa3V2830Vb69(0x20) = CONST 
    0x2aa5S0x2830S0xb69: v2aa5V2830Vb69 = ADD v2aa3V2830Vb69(0x20), v2a4b_2V2830Vb69
    0x2aa8S0x2830S0xb69: v2aa8V2830Vb69(0x1) = CONST 
    0x2aaaS0x2830S0xb69: v2aaaV2830Vb69 = ADD v2aa8V2830Vb69(0x1), v2a4b_1V2830Vb69
    0x2aacS0x2830S0xb69: v2aacV2830Vb69(0x2a42) = CONST 
    0x2aafS0x2830S0xb69: JUMP v2aacV2830Vb69(0x2a42)

    Begin block 0x2ab0B0x2830B0xb69
    prev=[0x2a42B0x2830B0xb69], succ=[0x2ab1B0x2830B0xb69]
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
    prev=[0xb80], succ=[0x2845B0xb8b]
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
    0xc1e: vc1e(0x2845) = CONST 
    0xc21: JUMP vc1e(0x2845), vbfd, vbe7, vbbe, vb9c, vb93, vb8c(0xc22)

    Begin block 0x2845B0xb8b
    prev=[0xb8b], succ=[0x286eB0xb8b, 0x285dB0xb8b]
    =================================
    0x2846S0xb8b: v2846Vb8b(0x12) = CONST 
    0x2848S0xb8b: v2848Vb8b(0x0) = CONST 
    0x284bS0xb8b: v284bVb8b = SLOAD v2846Vb8b(0x12)
    0x284dS0xb8b: v284dVb8b(0x100) = CONST 
    0x2850S0xb8b: v2850Vb8b(0x1) = EXP v284dVb8b(0x100), v2848Vb8b(0x0)
    0x2852S0xb8b: v2852Vb8b = DIV v284bVb8b, v2850Vb8b(0x1)
    0x2853S0xb8b: v2853Vb8b(0xff) = CONST 
    0x2855S0xb8b: v2855Vb8b = AND v2853Vb8b(0xff), v2852Vb8b
    0x2856S0xb8b: v2856Vb8b = ISZERO v2855Vb8b
    0x2858S0xb8b: v2858Vb8b = ISZERO v2856Vb8b
    0x2859S0xb8b: v2859Vb8b(0x286e) = CONST 
    0x285cS0xb8b: JUMPI v2859Vb8b(0x286e), v2858Vb8b

    Begin block 0x286eB0xb8b
    prev=[0x2845B0xb8b, 0x285dB0xb8b], succ=[0x2875B0xb8b, 0x2879B0xb8b]
    =================================
    0x286e_0x0S0xb8b: v286e_0Vb8b = PHI v2856Vb8b, v286dVb8b
    0x286fS0xb8b: v286fVb8b = ISZERO v286e_0Vb8b
    0x2870S0xb8b: v2870Vb8b = ISZERO v286fVb8b
    0x2871S0xb8b: v2871Vb8b(0x2879) = CONST 
    0x2874S0xb8b: JUMPI v2871Vb8b(0x2879), v2870Vb8b

    Begin block 0x2875B0xb8b
    prev=[0x286eB0xb8b], succ=[]
    =================================
    0x2875S0xb8b: v2875Vb8b(0x0) = CONST 
    0x2878S0xb8b: REVERT v2875Vb8b(0x0), v2875Vb8b(0x0)

    Begin block 0x2879B0xb8b
    prev=[0x286eB0xb8b], succ=[0x28d3B0xb8b, 0x2923B0xb8b]
    =================================
    0x287aS0xb8b: v287aVb8b(0xd8479c546b80ce91916c7800c1840bd6446b06ce) = CONST 
    0x288fS0xb8b: v288fVb8b(0xbad4481) = CONST 
    0x2894S0xb8b: v2894Vb8b(0x2) = CONST 
    0x289bS0xb8b: v289bVb8b(0x40) = CONST 
    0x289dS0xb8b: v289dVb8b = MLOAD v289bVb8b(0x40)
    0x289fS0xb8b: v289fVb8b(0xffffffff) = CONST 
    0x28a4S0xb8b: v28a4Vb8b(0xbad4481) = AND v289fVb8b(0xffffffff), v288fVb8b(0xbad4481)
    0x28a5S0xb8b: v28a5Vb8b(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x28c3S0xb8b: v28c3Vb8b(0xbad448100000000000000000000000000000000000000000000000000000000) = MUL v28a5Vb8b(0x100000000000000000000000000000000000000000000000000000000), v28a4Vb8b(0xbad4481)
    0x28c5S0xb8b: MSTORE v289dVb8b, v28c3Vb8b(0xbad448100000000000000000000000000000000000000000000000000000000)
    0x28c6S0xb8b: v28c6Vb8b(0x4) = CONST 
    0x28c8S0xb8b: v28c8Vb8b = ADD v28c6Vb8b(0x4), v289dVb8b
    0x28cbS0xb8b: v28cbVb8b(0x10) = CONST 
    0x28ceS0xb8b: v28ceVb8b(0x0) = ISZERO v28cbVb8b(0x10)
    0x28cfS0xb8b: v28cfVb8b(0x2923) = CONST 
    0x28d2S0xb8b: JUMPI v28cfVb8b(0x2923), v28ceVb8b(0x0)

    Begin block 0x28d3B0xb8b
    prev=[0x2879B0xb8b], succ=[0x28d9B0xb8b]
    =================================
    0x28d3S0xb8b: v28d3Vb8b(0x20) = CONST 
    0x28d5S0xb8b: v28d5Vb8b(0x200) = MUL v28d3Vb8b(0x20), v28cbVb8b(0x10)
    0x28d7S0xb8b: v28d7Vb8b = ADD v28c8Vb8b, v28d5Vb8b(0x200)

    Begin block 0x28d9B0xb8b
    prev=[0x28d3B0xb8b, 0x28d9B0xb8b], succ=[0x2923B0xb8b, 0x28d9B0xb8b]
    =================================
    0x28d9_0x0S0xb8b: v28d9_0Vb8b = PHI v28c8Vb8b, v2916Vb8b
    0x28d9_0x1S0xb8b: v28d9_1Vb8b = PHI v2894Vb8b(0x2), v291aVb8b
    0x28dbS0xb8b: v28dbVb8b(0x0) = CONST 
    0x28deS0xb8b: v28deVb8b = SLOAD v28d9_1Vb8b
    0x28e0S0xb8b: v28e0Vb8b(0x100) = CONST 
    0x28e3S0xb8b: v28e3Vb8b(0x1) = EXP v28e0Vb8b(0x100), v28dbVb8b(0x0)
    0x28e5S0xb8b: v28e5Vb8b = DIV v28deVb8b, v28e3Vb8b(0x1)
    0x28e6S0xb8b: v28e6Vb8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28fbS0xb8b: v28fbVb8b = AND v28e6Vb8b(0xffffffffffffffffffffffffffffffffffffffff), v28e5Vb8b
    0x28fcS0xb8b: v28fcVb8b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2911S0xb8b: v2911Vb8b = AND v28fcVb8b(0xffffffffffffffffffffffffffffffffffffffff), v28fbVb8b
    0x2913S0xb8b: MSTORE v28d9_0Vb8b, v2911Vb8b
    0x2914S0xb8b: v2914Vb8b(0x20) = CONST 
    0x2916S0xb8b: v2916Vb8b = ADD v2914Vb8b(0x20), v28d9_0Vb8b
    0x2918S0xb8b: v2918Vb8b(0x1) = CONST 
    0x291aS0xb8b: v291aVb8b = ADD v2918Vb8b(0x1), v28d9_1Vb8b
    0x291eS0xb8b: v291eVb8b = GT v28d7Vb8b, v2916Vb8b
    0x291fS0xb8b: v291fVb8b(0x28d9) = CONST 
    0x2922S0xb8b: JUMPI v291fVb8b(0x28d9), v291eVb8b

    Begin block 0x2923B0xb8b
    prev=[0x2879B0xb8b, 0x28d9B0xb8b], succ=[0x294bB0xb8b]
    =================================
    0x2923_0x2S0xb8b: v2923_2Vb8b = PHI v28d7Vb8b, v28c8Vb8b
    0x2928S0xb8b: MSTORE v2923_2Vb8b, vb93
    0x2929S0xb8b: v2929Vb8b(0x20) = CONST 
    0x292bS0xb8b: v292bVb8b = ADD v2929Vb8b(0x20), v2923_2Vb8b
    0x292eS0xb8b: MSTORE v292bVb8b, vb9c
    0x292fS0xb8b: v292fVb8b(0x20) = CONST 
    0x2931S0xb8b: v2931Vb8b = ADD v292fVb8b(0x20), v292bVb8b
    0x2933S0xb8b: v2933Vb8b(0x20) = CONST 
    0x2935S0xb8b: v2935Vb8b = ADD v2933Vb8b(0x20), v2931Vb8b
    0x2937S0xb8b: v2937Vb8b = ISZERO vbe7
    0x2938S0xb8b: v2938Vb8b = ISZERO v2937Vb8b
    0x2939S0xb8b: v2939Vb8b = ISZERO v2938Vb8b
    0x293aS0xb8b: v293aVb8b = ISZERO v2939Vb8b
    0x293cS0xb8b: MSTORE v2935Vb8b, v293aVb8b
    0x293dS0xb8b: v293dVb8b(0x20) = CONST 
    0x293fS0xb8b: v293fVb8b = ADD v293dVb8b(0x20), v2935Vb8b
    0x2941S0xb8b: v2941Vb8b(0x80) = CONST 
    0x2943S0xb8b: v2943Vb8b(0x20) = CONST 
    0x2945S0xb8b: v2945Vb8b(0x1000) = MUL v2943Vb8b(0x20), v2941Vb8b(0x80)
    0x2949S0xb8b: v2949Vb8b(0x0) = CONST 

    Begin block 0x294bB0xb8b
    prev=[0x2923B0xb8b, 0x2954B0xb8b], succ=[0x2966B0xb8b, 0x2954B0xb8b]
    =================================
    0x294b_0x0S0xb8b: v294b_0Vb8b = PHI v2949Vb8b(0x0), v295fVb8b
    0x294eS0xb8b: v294eVb8b = LT v294b_0Vb8b, v2945Vb8b(0x1000)
    0x294fS0xb8b: v294fVb8b = ISZERO v294eVb8b
    0x2950S0xb8b: v2950Vb8b(0x2966) = CONST 
    0x2953S0xb8b: JUMPI v2950Vb8b(0x2966), v294fVb8b

    Begin block 0x2966B0xb8b
    prev=[0x294bB0xb8b], succ=[0x298dB0xb8b]
    =================================
    0x296dS0xb8b: v296dVb8b = ADD v2945Vb8b(0x1000), v293fVb8b
    0x2970S0xb8b: v2970Vb8b = SUB v296dVb8b, v28c8Vb8b
    0x2972S0xb8b: MSTORE v2931Vb8b, v2970Vb8b
    0x2976S0xb8b: v2976Vb8b = MLOAD vbbe
    0x2978S0xb8b: MSTORE v296dVb8b, v2976Vb8b
    0x2979S0xb8b: v2979Vb8b(0x20) = CONST 
    0x297bS0xb8b: v297bVb8b = ADD v2979Vb8b(0x20), v296dVb8b
    0x297fS0xb8b: v297fVb8b = MLOAD vbbe
    0x2981S0xb8b: v2981Vb8b(0x20) = CONST 
    0x2983S0xb8b: v2983Vb8b = ADD v2981Vb8b(0x20), vbbe
    0x2985S0xb8b: v2985Vb8b(0x20) = CONST 
    0x2987S0xb8b: v2987Vb8b = MUL v2985Vb8b(0x20), v297fVb8b
    0x298bS0xb8b: v298bVb8b(0x0) = CONST 

    Begin block 0x298dB0xb8b
    prev=[0x2966B0xb8b, 0x2996B0xb8b], succ=[0x29a8B0xb8b, 0x2996B0xb8b]
    =================================
    0x298d_0x0S0xb8b: v298d_0Vb8b = PHI v298bVb8b(0x0), v29a1Vb8b
    0x2990S0xb8b: v2990Vb8b = LT v298d_0Vb8b, v2987Vb8b
    0x2991S0xb8b: v2991Vb8b = ISZERO v2990Vb8b
    0x2992S0xb8b: v2992Vb8b(0x29a8) = CONST 
    0x2995S0xb8b: JUMPI v2992Vb8b(0x29a8), v2991Vb8b

    Begin block 0x29a8B0xb8b
    prev=[0x298dB0xb8b], succ=[0x29cbB0xb8b, 0x29cfB0xb8b]
    =================================
    0x29afS0xb8b: v29afVb8b = ADD v2987Vb8b, v297bVb8b
    0x29b9S0xb8b: v29b9Vb8b(0x0) = CONST 
    0x29bbS0xb8b: v29bbVb8b(0x40) = CONST 
    0x29bdS0xb8b: v29bdVb8b = MLOAD v29bbVb8b(0x40)
    0x29c0S0xb8b: v29c0Vb8b = SUB v29afVb8b, v29bdVb8b
    0x29c4S0xb8b: v29c4Vb8b = EXTCODESIZE v287aVb8b(0xd8479c546b80ce91916c7800c1840bd6446b06ce)
    0x29c5S0xb8b: v29c5Vb8b = ISZERO v29c4Vb8b
    0x29c6S0xb8b: v29c6Vb8b = ISZERO v29c5Vb8b
    0x29c7S0xb8b: v29c7Vb8b(0x29cf) = CONST 
    0x29caS0xb8b: JUMPI v29c7Vb8b(0x29cf), v29c6Vb8b

    Begin block 0x29cbB0xb8b
    prev=[0x29a8B0xb8b], succ=[]
    =================================
    0x29cbS0xb8b: v29cbVb8b(0x0) = CONST 
    0x29ceS0xb8b: REVERT v29cbVb8b(0x0), v29cbVb8b(0x0)

    Begin block 0x29cfB0xb8b
    prev=[0x29a8B0xb8b], succ=[0x29dcB0xb8b, 0x29e0B0xb8b]
    =================================
    0x29d0S0xb8b: v29d0Vb8b(0x2c6) = CONST 
    0x29d3S0xb8b: v29d3Vb8b = GAS 
    0x29d4S0xb8b: v29d4Vb8b = SUB v29d3Vb8b, v29d0Vb8b(0x2c6)
    0x29d5S0xb8b: v29d5Vb8b = DELEGATECALL v29d4Vb8b, v287aVb8b(0xd8479c546b80ce91916c7800c1840bd6446b06ce), v29bdVb8b, v29c0Vb8b, v29bdVb8b, v29b9Vb8b(0x0)
    0x29d6S0xb8b: v29d6Vb8b = ISZERO v29d5Vb8b
    0x29d7S0xb8b: v29d7Vb8b = ISZERO v29d6Vb8b
    0x29d8S0xb8b: v29d8Vb8b(0x29e0) = CONST 
    0x29dbS0xb8b: JUMPI v29d8Vb8b(0x29e0), v29d7Vb8b

    Begin block 0x29dcB0xb8b
    prev=[0x29cfB0xb8b], succ=[]
    =================================
    0x29dcS0xb8b: v29dcVb8b(0x0) = CONST 
    0x29dfS0xb8b: REVERT v29dcVb8b(0x0), v29dcVb8b(0x0)

    Begin block 0x29e0B0xb8b
    prev=[0x29cfB0xb8b], succ=[0xc22]
    =================================
    0x29e9S0xb8b: JUMP vb8c(0xc22)

    Begin block 0xc22
    prev=[0x29e0B0xb8b], succ=[]
    =================================
    0xc23: STOP 

    Begin block 0x2996B0xb8b
    prev=[0x298dB0xb8b], succ=[0x298dB0xb8b]
    =================================
    0x2996_0x0S0xb8b: v2996_0Vb8b = PHI v298bVb8b(0x0), v29a1Vb8b
    0x2998S0xb8b: v2998Vb8b = ADD v2983Vb8b, v2996_0Vb8b
    0x2999S0xb8b: v2999Vb8b = MLOAD v2998Vb8b
    0x299cS0xb8b: v299cVb8b = ADD v297bVb8b, v2996_0Vb8b
    0x299dS0xb8b: MSTORE v299cVb8b, v2999Vb8b
    0x299eS0xb8b: v299eVb8b(0x20) = CONST 
    0x29a1S0xb8b: v29a1Vb8b = ADD v2996_0Vb8b, v299eVb8b(0x20)
    0x29a4S0xb8b: v29a4Vb8b(0x298d) = CONST 
    0x29a7S0xb8b: JUMP v29a4Vb8b(0x298d)

    Begin block 0x2954B0xb8b
    prev=[0x294bB0xb8b], succ=[0x294bB0xb8b]
    =================================
    0x2954_0x0S0xb8b: v2954_0Vb8b = PHI v2949Vb8b(0x0), v295fVb8b
    0x2956S0xb8b: v2956Vb8b = ADD vbfd, v2954_0Vb8b
    0x2957S0xb8b: v2957Vb8b = MLOAD v2956Vb8b
    0x295aS0xb8b: v295aVb8b = ADD v293fVb8b, v2954_0Vb8b
    0x295bS0xb8b: MSTORE v295aVb8b, v2957Vb8b
    0x295cS0xb8b: v295cVb8b(0x20) = CONST 
    0x295fS0xb8b: v295fVb8b = ADD v2954_0Vb8b, v295cVb8b(0x20)
    0x2962S0xb8b: v2962Vb8b(0x294b) = CONST 
    0x2965S0xb8b: JUMP v2962Vb8b(0x294b)

    Begin block 0x285dB0xb8b
    prev=[0x2845B0xb8b], succ=[0x286eB0xb8b]
    =================================
    0x285eS0xb8b: v285eVb8b(0x12) = CONST 
    0x2860S0xb8b: v2860Vb8b(0x1) = CONST 
    0x2863S0xb8b: v2863Vb8b = SLOAD v285eVb8b(0x12)
    0x2865S0xb8b: v2865Vb8b(0x100) = CONST 
    0x2868S0xb8b: v2868Vb8b(0x100) = EXP v2865Vb8b(0x100), v2860Vb8b(0x1)
    0x286aS0xb8b: v286aVb8b = DIV v2863Vb8b, v2868Vb8b(0x100)
    0x286bS0xb8b: v286bVb8b(0xff) = CONST 
    0x286dS0xb8b: v286dVb8b = AND v286bVb8b(0xff), v286aVb8b

}

