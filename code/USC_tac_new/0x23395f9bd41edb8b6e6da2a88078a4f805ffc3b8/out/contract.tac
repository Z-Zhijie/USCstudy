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
    prev=[0x0], succ=[0x1a, 0x3b7d]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x3af4: v3af4(0x3b7d) = CONST 
    0x3af5: JUMPI v3af4(0x3b7d), v15

    Begin block 0x1a
    prev=[0x10], succ=[0xf9, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x641579a6) = CONST 
    0x26: v26 = GT v21(0x641579a6), v1f
    0x27: v27(0xf9) = CONST 
    0x2a: JUMPI v27(0xf9), v26

    Begin block 0xf9
    prev=[0x1a], succ=[0x166, 0x105]
    =================================
    0xfb: vfb(0x313ce567) = CONST 
    0x100: v100 = GT vfb(0x313ce567), v1f
    0x101: v101(0x166) = CONST 
    0x104: JUMPI v101(0x166), v100

    Begin block 0x166
    prev=[0xf9], succ=[0x3b2c, 0x172]
    =================================
    0x168: v168(0x6fdde03) = CONST 
    0x16d: v16d = EQ v168(0x6fdde03), v1f
    0x3b20: v3b20(0x3b2c) = CONST 
    0x3b21: JUMPI v3b20(0x3b2c), v16d

    Begin block 0x3b2c
    prev=[0x166], succ=[]
    =================================
    0x3b2d: v3b2d(0x1ae) = CONST 
    0x3b2e: CALLPRIVATE v3b2d(0x1ae)

    Begin block 0x172
    prev=[0x166], succ=[0x3b2f, 0x17d]
    =================================
    0x173: v173(0x95ea7b3) = CONST 
    0x178: v178 = EQ v173(0x95ea7b3), v1f
    0x3b22: v3b22(0x3b2f) = CONST 
    0x3b23: JUMPI v3b22(0x3b2f), v178

    Begin block 0x3b2f
    prev=[0x172], succ=[]
    =================================
    0x3b30: v3b30(0x231) = CONST 
    0x3b31: CALLPRIVATE v3b30(0x231)

    Begin block 0x17d
    prev=[0x172], succ=[0x3b32, 0x188]
    =================================
    0x17e: v17e(0x158ef93e) = CONST 
    0x183: v183 = EQ v17e(0x158ef93e), v1f
    0x3b24: v3b24(0x3b32) = CONST 
    0x3b25: JUMPI v3b24(0x3b32), v183

    Begin block 0x3b32
    prev=[0x17d], succ=[]
    =================================
    0x3b33: v3b33(0x295) = CONST 
    0x3b34: CALLPRIVATE v3b33(0x295)

    Begin block 0x188
    prev=[0x17d], succ=[0x3b35, 0x193]
    =================================
    0x189: v189(0x18160ddd) = CONST 
    0x18e: v18e = EQ v189(0x18160ddd), v1f
    0x3b26: v3b26(0x3b35) = CONST 
    0x3b27: JUMPI v3b26(0x3b35), v18e

    Begin block 0x3b35
    prev=[0x188], succ=[]
    =================================
    0x3b36: v3b36(0x2b5) = CONST 
    0x3b37: CALLPRIVATE v3b36(0x2b5)

    Begin block 0x193
    prev=[0x188], succ=[0x3b38, 0x19e]
    =================================
    0x194: v194(0x1b3ed722) = CONST 
    0x199: v199 = EQ v194(0x1b3ed722), v1f
    0x3b28: v3b28(0x3b38) = CONST 
    0x3b29: JUMPI v3b28(0x3b38), v199

    Begin block 0x3b38
    prev=[0x193], succ=[]
    =================================
    0x3b39: v3b39(0x2d3) = CONST 
    0x3b3a: CALLPRIVATE v3b39(0x2d3)

    Begin block 0x19e
    prev=[0x193], succ=[0x3b3b, 0x1a9]
    =================================
    0x19f: v19f(0x23b872dd) = CONST 
    0x1a4: v1a4 = EQ v19f(0x23b872dd), v1f
    0x3b2a: v3b2a(0x3b3b) = CONST 
    0x3b2b: JUMPI v3b2a(0x3b3b), v1a4

    Begin block 0x3b3b
    prev=[0x19e], succ=[]
    =================================
    0x3b3c: v3b3c(0x2f1) = CONST 
    0x3b3d: CALLPRIVATE v3b3c(0x2f1)

    Begin block 0x1a9
    prev=[0x19e], succ=[]
    =================================
    0x1aa: v1aa(0x0) = CONST 
    0x1ad: REVERT v1aa(0x0), v1aa(0x0)

    Begin block 0x105
    prev=[0xf9], succ=[0x140, 0x110]
    =================================
    0x106: v106(0x3f4ba83a) = CONST 
    0x10b: v10b = GT v106(0x3f4ba83a), v1f
    0x10c: v10c(0x140) = CONST 
    0x10f: JUMPI v10c(0x140), v10b

    Begin block 0x140
    prev=[0x105], succ=[0x3b3e, 0x14c]
    =================================
    0x142: v142(0x313ce567) = CONST 
    0x147: v147 = EQ v142(0x313ce567), v1f
    0x3b1a: v3b1a(0x3b3e) = CONST 
    0x3b1b: JUMPI v3b1a(0x3b3e), v147

    Begin block 0x3b3e
    prev=[0x140], succ=[]
    =================================
    0x3b3f: v3b3f(0x375) = CONST 
    0x3b40: CALLPRIVATE v3b3f(0x375)

    Begin block 0x14c
    prev=[0x140], succ=[0x3b41, 0x157]
    =================================
    0x14d: v14d(0x39509351) = CONST 
    0x152: v152 = EQ v14d(0x39509351), v1f
    0x3b1c: v3b1c(0x3b41) = CONST 
    0x3b1d: JUMPI v3b1c(0x3b41), v152

    Begin block 0x3b41
    prev=[0x14c], succ=[]
    =================================
    0x3b42: v3b42(0x396) = CONST 
    0x3b43: CALLPRIVATE v3b42(0x396)

    Begin block 0x157
    prev=[0x14c], succ=[0x162, 0x3b44]
    =================================
    0x158: v158(0x3afada39) = CONST 
    0x15d: v15d = EQ v158(0x3afada39), v1f
    0x3b1e: v3b1e(0x3b44) = CONST 
    0x3b1f: JUMPI v3b1e(0x3b44), v15d

    Begin block 0x162
    prev=[0x157], succ=[0x3aef]
    =================================
    0x162: v162(0x3aef) = CONST 
    0x165: JUMP v162(0x3aef)

    Begin block 0x3aef
    prev=[0x162], succ=[]
    =================================
    0x3af0: v3af0(0x0) = CONST 
    0x3af3: REVERT v3af0(0x0), v3af0(0x0)

    Begin block 0x3b44
    prev=[0x157], succ=[]
    =================================
    0x3b45: v3b45(0x3fa) = CONST 
    0x3b46: CALLPRIVATE v3b45(0x3fa)

    Begin block 0x110
    prev=[0x105], succ=[0x3b47, 0x11b]
    =================================
    0x111: v111(0x3f4ba83a) = CONST 
    0x116: v116 = EQ v111(0x3f4ba83a), v1f
    0x3b12: v3b12(0x3b47) = CONST 
    0x3b13: JUMPI v3b12(0x3b47), v116

    Begin block 0x3b47
    prev=[0x110], succ=[]
    =================================
    0x3b48: v3b48(0x43e) = CONST 
    0x3b49: CALLPRIVATE v3b48(0x43e)

    Begin block 0x11b
    prev=[0x110], succ=[0x3b4a, 0x126]
    =================================
    0x11c: v11c(0x40c10f19) = CONST 
    0x121: v121 = EQ v11c(0x40c10f19), v1f
    0x3b14: v3b14(0x3b4a) = CONST 
    0x3b15: JUMPI v3b14(0x3b4a), v121

    Begin block 0x3b4a
    prev=[0x11b], succ=[]
    =================================
    0x3b4b: v3b4b(0x448) = CONST 
    0x3b4c: CALLPRIVATE v3b4b(0x448)

    Begin block 0x126
    prev=[0x11b], succ=[0x3b4d, 0x131]
    =================================
    0x127: v127(0x46951954) = CONST 
    0x12c: v12c = EQ v127(0x46951954), v1f
    0x3b16: v3b16(0x3b4d) = CONST 
    0x3b17: JUMPI v3b16(0x3b4d), v12c

    Begin block 0x3b4d
    prev=[0x126], succ=[]
    =================================
    0x3b4e: v3b4e(0x4ac) = CONST 
    0x3b4f: CALLPRIVATE v3b4e(0x4ac)

    Begin block 0x131
    prev=[0x126], succ=[0x13c, 0x3b50]
    =================================
    0x132: v132(0x52d1902d) = CONST 
    0x137: v137 = EQ v132(0x52d1902d), v1f
    0x3b18: v3b18(0x3b50) = CONST 
    0x3b19: JUMPI v3b18(0x3b50), v137

    Begin block 0x13c
    prev=[0x131], succ=[0x3acb]
    =================================
    0x13c: v13c(0x3acb) = CONST 
    0x13f: JUMP v13c(0x3acb)

    Begin block 0x3acb
    prev=[0x13c], succ=[]
    =================================
    0x3acc: v3acc(0x0) = CONST 
    0x3acf: REVERT v3acc(0x0), v3acc(0x0)

    Begin block 0x3b50
    prev=[0x131], succ=[]
    =================================
    0x3b51: v3b51(0x4f0) = CONST 
    0x3b52: CALLPRIVATE v3b51(0x4f0)

    Begin block 0x2b
    prev=[0x1a], succ=[0x97, 0x36]
    =================================
    0x2c: v2c(0xa9059cbb) = CONST 
    0x31: v31 = GT v2c(0xa9059cbb), v1f
    0x32: v32(0x97) = CONST 
    0x35: JUMPI v32(0x97), v31

    Begin block 0x97
    prev=[0x2b], succ=[0xd3, 0xa3]
    =================================
    0x99: v99(0x8456cb59) = CONST 
    0x9e: v9e = GT v99(0x8456cb59), v1f
    0x9f: v9f(0xd3) = CONST 
    0xa2: JUMPI v9f(0xd3), v9e

    Begin block 0xd3
    prev=[0x97], succ=[0x3b53, 0xdf]
    =================================
    0xd5: vd5(0x641579a6) = CONST 
    0xda: vda = EQ vd5(0x641579a6), v1f
    0x3b0c: v3b0c(0x3b53) = CONST 
    0x3b0d: JUMPI v3b0c(0x3b53), vda

    Begin block 0x3b53
    prev=[0xd3], succ=[]
    =================================
    0x3b54: v3b54(0x50e) = CONST 
    0x3b55: CALLPRIVATE v3b54(0x50e)

    Begin block 0xdf
    prev=[0xd3], succ=[0x3b56, 0xea]
    =================================
    0xe0: ve0(0x6b713f4f) = CONST 
    0xe5: ve5 = EQ ve0(0x6b713f4f), v1f
    0x3b0e: v3b0e(0x3b56) = CONST 
    0x3b0f: JUMPI v3b0e(0x3b56), ve5

    Begin block 0x3b56
    prev=[0xdf], succ=[]
    =================================
    0x3b57: v3b57(0x53c) = CONST 
    0x3b58: CALLPRIVATE v3b57(0x53c)

    Begin block 0xea
    prev=[0xdf], succ=[0xf5, 0x3b59]
    =================================
    0xeb: veb(0x70a08231) = CONST 
    0xf0: vf0 = EQ veb(0x70a08231), v1f
    0x3b10: v3b10(0x3b59) = CONST 
    0x3b11: JUMPI v3b10(0x3b59), vf0

    Begin block 0xf5
    prev=[0xea], succ=[0x3aa7]
    =================================
    0xf5: vf5(0x3aa7) = CONST 
    0xf8: JUMP vf5(0x3aa7)

    Begin block 0x3aa7
    prev=[0xf5], succ=[]
    =================================
    0x3aa8: v3aa8(0x0) = CONST 
    0x3aab: REVERT v3aa8(0x0), v3aa8(0x0)

    Begin block 0x3b59
    prev=[0xea], succ=[]
    =================================
    0x3b5a: v3b5a(0x580) = CONST 
    0x3b5b: CALLPRIVATE v3b5a(0x580)

    Begin block 0xa3
    prev=[0x97], succ=[0x3b5c, 0xae]
    =================================
    0xa4: va4(0x8456cb59) = CONST 
    0xa9: va9 = EQ va4(0x8456cb59), v1f
    0x3b04: v3b04(0x3b5c) = CONST 
    0x3b05: JUMPI v3b04(0x3b5c), va9

    Begin block 0x3b5c
    prev=[0xa3], succ=[]
    =================================
    0x3b5d: v3b5d(0x5d8) = CONST 
    0x3b5e: CALLPRIVATE v3b5d(0x5d8)

    Begin block 0xae
    prev=[0xa3], succ=[0x3b5f, 0xb9]
    =================================
    0xaf: vaf(0x95d89b41) = CONST 
    0xb4: vb4 = EQ vaf(0x95d89b41), v1f
    0x3b06: v3b06(0x3b5f) = CONST 
    0x3b07: JUMPI v3b06(0x3b5f), vb4

    Begin block 0x3b5f
    prev=[0xae], succ=[]
    =================================
    0x3b60: v3b60(0x5e2) = CONST 
    0x3b61: CALLPRIVATE v3b60(0x5e2)

    Begin block 0xb9
    prev=[0xae], succ=[0x3b62, 0xc4]
    =================================
    0xba: vba(0x9dc29fac) = CONST 
    0xbf: vbf = EQ vba(0x9dc29fac), v1f
    0x3b08: v3b08(0x3b62) = CONST 
    0x3b09: JUMPI v3b08(0x3b62), vbf

    Begin block 0x3b62
    prev=[0xb9], succ=[]
    =================================
    0x3b63: v3b63(0x665) = CONST 
    0x3b64: CALLPRIVATE v3b63(0x665)

    Begin block 0xc4
    prev=[0xb9], succ=[0xcf, 0x3b65]
    =================================
    0xc5: vc5(0xa457c2d7) = CONST 
    0xca: vca = EQ vc5(0xa457c2d7), v1f
    0x3b0a: v3b0a(0x3b65) = CONST 
    0x3b0b: JUMPI v3b0a(0x3b65), vca

    Begin block 0xcf
    prev=[0xc4], succ=[0x3a83]
    =================================
    0xcf: vcf(0x3a83) = CONST 
    0xd2: JUMP vcf(0x3a83)

    Begin block 0x3a83
    prev=[0xcf], succ=[]
    =================================
    0x3a84: v3a84(0x0) = CONST 
    0x3a87: REVERT v3a84(0x0), v3a84(0x0)

    Begin block 0x3b65
    prev=[0xc4], succ=[]
    =================================
    0x3b66: v3b66(0x6c9) = CONST 
    0x3b67: CALLPRIVATE v3b66(0x6c9)

    Begin block 0x36
    prev=[0x2b], succ=[0x71, 0x41]
    =================================
    0x37: v37(0xf7ea7a3d) = CONST 
    0x3c: v3c = GT v37(0xf7ea7a3d), v1f
    0x3d: v3d(0x71) = CONST 
    0x40: JUMPI v3d(0x71), v3c

    Begin block 0x71
    prev=[0x36], succ=[0x3b68, 0x7d]
    =================================
    0x73: v73(0xa9059cbb) = CONST 
    0x78: v78 = EQ v73(0xa9059cbb), v1f
    0x3afe: v3afe(0x3b68) = CONST 
    0x3aff: JUMPI v3afe(0x3b68), v78

    Begin block 0x3b68
    prev=[0x71], succ=[]
    =================================
    0x3b69: v3b69(0x72d) = CONST 
    0x3b6a: CALLPRIVATE v3b69(0x72d)

    Begin block 0x7d
    prev=[0x71], succ=[0x3b6b, 0x88]
    =================================
    0x7e: v7e(0xb1eb3468) = CONST 
    0x83: v83 = EQ v7e(0xb1eb3468), v1f
    0x3b00: v3b00(0x3b6b) = CONST 
    0x3b01: JUMPI v3b00(0x3b6b), v83

    Begin block 0x3b6b
    prev=[0x7d], succ=[]
    =================================
    0x3b6c: v3b6c(0x791) = CONST 
    0x3b6d: CALLPRIVATE v3b6c(0x791)

    Begin block 0x88
    prev=[0x7d], succ=[0x93, 0x3b6e]
    =================================
    0x89: v89(0xdd62ed3e) = CONST 
    0x8e: v8e = EQ v89(0xdd62ed3e), v1f
    0x3b02: v3b02(0x3b6e) = CONST 
    0x3b03: JUMPI v3b02(0x3b6e), v8e

    Begin block 0x93
    prev=[0x88], succ=[0x3a5f]
    =================================
    0x93: v93(0x3a5f) = CONST 
    0x96: JUMP v93(0x3a5f)

    Begin block 0x3a5f
    prev=[0x93], succ=[]
    =================================
    0x3a60: v3a60(0x0) = CONST 
    0x3a63: REVERT v3a60(0x0), v3a60(0x0)

    Begin block 0x3b6e
    prev=[0x88], succ=[]
    =================================
    0x3b6f: v3b6f(0x7d5) = CONST 
    0x3b70: CALLPRIVATE v3b6f(0x7d5)

    Begin block 0x41
    prev=[0x36], succ=[0x3b71, 0x4c]
    =================================
    0x42: v42(0xf7ea7a3d) = CONST 
    0x47: v47 = EQ v42(0xf7ea7a3d), v1f
    0x3af6: v3af6(0x3b71) = CONST 
    0x3af7: JUMPI v3af6(0x3b71), v47

    Begin block 0x3b71
    prev=[0x41], succ=[]
    =================================
    0x3b72: v3b72(0x84d) = CONST 
    0x3b73: CALLPRIVATE v3b72(0x84d)

    Begin block 0x4c
    prev=[0x41], succ=[0x3b74, 0x57]
    =================================
    0x4d: v4d(0xf851a440) = CONST 
    0x52: v52 = EQ v4d(0xf851a440), v1f
    0x3af8: v3af8(0x3b74) = CONST 
    0x3af9: JUMPI v3af8(0x3b74), v52

    Begin block 0x3b74
    prev=[0x4c], succ=[]
    =================================
    0x3b75: v3b75(0x87b) = CONST 
    0x3b76: CALLPRIVATE v3b75(0x87b)

    Begin block 0x57
    prev=[0x4c], succ=[0x3b77, 0x62]
    =================================
    0x58: v58(0xf9f92be4) = CONST 
    0x5d: v5d = EQ v58(0xf9f92be4), v1f
    0x3afa: v3afa(0x3b77) = CONST 
    0x3afb: JUMPI v3afa(0x3b77), v5d

    Begin block 0x3b77
    prev=[0x57], succ=[]
    =================================
    0x3b78: v3b78(0x8af) = CONST 
    0x3b79: CALLPRIVATE v3b78(0x8af)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0x3b7a]
    =================================
    0x63: v63(0xfe4b84df) = CONST 
    0x68: v68 = EQ v63(0xfe4b84df), v1f
    0x3afc: v3afc(0x3b7a) = CONST 
    0x3afd: JUMPI v3afc(0x3b7a), v68

    Begin block 0x6d
    prev=[0x62], succ=[0x3a3b]
    =================================
    0x6d: v6d(0x3a3b) = CONST 
    0x70: JUMP v6d(0x3a3b)

    Begin block 0x3a3b
    prev=[0x6d], succ=[]
    =================================
    0x3a3c: v3a3c(0x0) = CONST 
    0x3a3f: REVERT v3a3c(0x0), v3a3c(0x0)

    Begin block 0x3b7a
    prev=[0x62], succ=[]
    =================================
    0x3b7b: v3b7b(0x909) = CONST 
    0x3b7c: CALLPRIVATE v3b7b(0x909)

    Begin block 0x3b7d
    prev=[0x10], succ=[]
    =================================
    0x3b7e: v3b7e(0x3a17) = CONST 
    0x3b7f: CALLPRIVATE v3b7e(0x3a17)

}

function name()() public {
    Begin block 0x1ae
    prev=[], succ=[0x937]
    =================================
    0x1af: v1af(0x1b6) = CONST 
    0x1b2: v1b2(0x937) = CONST 
    0x1b5: JUMP v1b2(0x937)

    Begin block 0x937
    prev=[0x1ae], succ=[0x1b6]
    =================================
    0x938: v938(0x40) = CONST 
    0x93a: v93a = MLOAD v938(0x40)
    0x93c: v93c(0x40) = CONST 
    0x93e: v93e = ADD v93c(0x40), v93a
    0x93f: v93f(0x40) = CONST 
    0x941: MSTORE v93f(0x40), v93e
    0x943: v943(0xd) = CONST 
    0x946: MSTORE v93a, v943(0xd)
    0x947: v947(0x20) = CONST 
    0x949: v949 = ADD v947(0x20), v93a
    0x94a: v94a(0x4772617065667275697455534400000000000000000000000000000000000000) = CONST 
    0x96c: MSTORE v949, v94a(0x4772617065667275697455534400000000000000000000000000000000000000)
    0x96f: JUMP v1af(0x1b6)

    Begin block 0x1b6
    prev=[0x937], succ=[0x1db]
    =================================
    0x1b7: v1b7(0x40) = CONST 
    0x1b9: v1b9 = MLOAD v1b7(0x40)
    0x1bc: v1bc(0x20) = CONST 
    0x1be: v1be = ADD v1bc(0x20), v1b9
    0x1c1: v1c1(0x20) = SUB v1be, v1b9
    0x1c3: MSTORE v1b9, v1c1(0x20)
    0x1c7: v1c7(0xd) = MLOAD v93a
    0x1c9: MSTORE v1be, v1c7(0xd)
    0x1ca: v1ca(0x20) = CONST 
    0x1cc: v1cc = ADD v1ca(0x20), v1be
    0x1d0: v1d0(0xd) = MLOAD v93a
    0x1d2: v1d2(0x20) = CONST 
    0x1d4: v1d4 = ADD v1d2(0x20), v93a
    0x1d9: v1d9(0x0) = CONST 

    Begin block 0x1db
    prev=[0x1b6, 0x1e4], succ=[0x1f6, 0x1e4]
    =================================
    0x1db_0x0: v1db_0 = PHI v1d9(0x0), v1ef
    0x1de: v1de = LT v1db_0, v1d0(0xd)
    0x1df: v1df = ISZERO v1de
    0x1e0: v1e0(0x1f6) = CONST 
    0x1e3: JUMPI v1e0(0x1f6), v1df

    Begin block 0x1f6
    prev=[0x1db], succ=[0x223, 0x20a]
    =================================
    0x1ff: v1ff = ADD v1d0(0xd), v1cc
    0x201: v201(0x1f) = CONST 
    0x203: v203(0xd) = AND v201(0x1f), v1d0(0xd)
    0x205: v205 = ISZERO v203(0xd)
    0x206: v206(0x223) = CONST 
    0x209: JUMPI v206(0x223), v205

    Begin block 0x223
    prev=[0x1f6, 0x20a], succ=[]
    =================================
    0x223_0x1: v223_1 = PHI v1ff, v220
    0x229: v229(0x40) = CONST 
    0x22b: v22b = MLOAD v229(0x40)
    0x22e: v22e = SUB v223_1, v22b
    0x230: RETURN v22b, v22e

    Begin block 0x20a
    prev=[0x1f6], succ=[0x223]
    =================================
    0x20c: v20c = SUB v1ff, v203(0xd)
    0x20e: v20e = MLOAD v20c
    0x20f: v20f(0x1) = CONST 
    0x212: v212(0x20) = CONST 
    0x214: v214(0x13) = SUB v212(0x20), v203(0xd)
    0x215: v215(0x100) = CONST 
    0x218: v218(0x100000000000000000000000000000000000000) = EXP v215(0x100), v214(0x13)
    0x219: v219(0xffffffffffffffffffffffffffffffffffffff) = SUB v218(0x100000000000000000000000000000000000000), v20f(0x1)
    0x21a: v21a = NOT v219(0xffffffffffffffffffffffffffffffffffffff)
    0x21b: v21b = AND v21a, v20e
    0x21d: MSTORE v20c, v21b
    0x21e: v21e(0x20) = CONST 
    0x220: v220 = ADD v21e(0x20), v20c

    Begin block 0x1e4
    prev=[0x1db], succ=[0x1db]
    =================================
    0x1e4_0x0: v1e4_0 = PHI v1d9(0x0), v1ef
    0x1e6: v1e6 = ADD v1d4, v1e4_0
    0x1e7: v1e7 = MLOAD v1e6
    0x1ea: v1ea = ADD v1cc, v1e4_0
    0x1eb: MSTORE v1ea, v1e7
    0x1ec: v1ec(0x20) = CONST 
    0x1ef: v1ef = ADD v1e4_0, v1ec(0x20)
    0x1f2: v1f2(0x1db) = CONST 
    0x1f5: JUMP v1f2(0x1db)

}

function approve(address,uint256)() public {
    Begin block 0x231
    prev=[], succ=[0x243, 0x247]
    =================================
    0x232: v232(0x27d) = CONST 
    0x235: v235(0x4) = CONST 
    0x238: v238 = CALLDATASIZE 
    0x239: v239 = SUB v238, v235(0x4)
    0x23a: v23a(0x40) = CONST 
    0x23d: v23d = LT v239, v23a(0x40)
    0x23e: v23e = ISZERO v23d
    0x23f: v23f(0x247) = CONST 
    0x242: JUMPI v23f(0x247), v23e

    Begin block 0x243
    prev=[0x231], succ=[]
    =================================
    0x243: v243(0x0) = CONST 
    0x246: REVERT v243(0x0), v243(0x0)

    Begin block 0x247
    prev=[0x231], succ=[0x970]
    =================================
    0x249: v249 = ADD v235(0x4), v239
    0x24d: v24d = CALLDATALOAD v235(0x4)
    0x24e: v24e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x263: v263 = AND v24e(0xffffffffffffffffffffffffffffffffffffffff), v24d
    0x265: v265(0x20) = CONST 
    0x267: v267(0x24) = ADD v265(0x20), v235(0x4)
    0x26d: v26d = CALLDATALOAD v267(0x24)
    0x26f: v26f(0x20) = CONST 
    0x271: v271(0x44) = ADD v26f(0x20), v267(0x24)
    0x279: v279(0x970) = CONST 
    0x27c: JUMP v279(0x970)

    Begin block 0x970
    prev=[0x247], succ=[0x9c6, 0xa33]
    =================================
    0x971: v971(0x0) = CONST 
    0x974: v974(0x3) = CONST 
    0x976: v976(0x0) = CONST 
    0x979: v979(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x98e: v98e = AND v979(0xffffffffffffffffffffffffffffffffffffffff), v263
    0x98f: v98f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9a4: v9a4 = AND v98f(0xffffffffffffffffffffffffffffffffffffffff), v98e
    0x9a6: MSTORE v976(0x0), v9a4
    0x9a7: v9a7(0x20) = CONST 
    0x9a9: v9a9(0x20) = ADD v9a7(0x20), v976(0x0)
    0x9ac: MSTORE v9a9(0x20), v974(0x3)
    0x9ad: v9ad(0x20) = CONST 
    0x9af: v9af(0x40) = ADD v9ad(0x20), v9a9(0x20)
    0x9b0: v9b0(0x0) = CONST 
    0x9b2: v9b2 = SHA3 v9b0(0x0), v9af(0x40)
    0x9b3: v9b3(0x0) = CONST 
    0x9b6: v9b6 = SLOAD v9b2
    0x9b8: v9b8(0x100) = CONST 
    0x9bb: v9bb(0x1) = EXP v9b8(0x100), v9b3(0x0)
    0x9bd: v9bd = DIV v9b6, v9bb(0x1)
    0x9be: v9be(0xff) = CONST 
    0x9c0: v9c0 = AND v9be(0xff), v9bd
    0x9c1: v9c1 = ISZERO v9c0
    0x9c2: v9c2(0xa33) = CONST 
    0x9c5: JUMPI v9c2(0xa33), v9c1

    Begin block 0x9c6
    prev=[0x970], succ=[]
    =================================
    0x9c6: v9c6(0x40) = CONST 
    0x9c8: v9c8 = MLOAD v9c6(0x40)
    0x9c9: v9c9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9eb: MSTORE v9c8, v9c9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9ec: v9ec(0x4) = CONST 
    0x9ee: v9ee = ADD v9ec(0x4), v9c8
    0x9f1: v9f1(0x20) = CONST 
    0x9f3: v9f3 = ADD v9f1(0x20), v9ee
    0x9f6: v9f6(0x20) = SUB v9f3, v9ee
    0x9f8: MSTORE v9ee, v9f6(0x20)
    0x9f9: v9f9(0x16) = CONST 
    0x9fc: MSTORE v9f3, v9f9(0x16)
    0x9fd: v9fd(0x20) = CONST 
    0x9ff: v9ff = ADD v9fd(0x20), v9f3
    0xa01: va01(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xa23: MSTORE v9ff, va01(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xa25: va25(0x20) = CONST 
    0xa27: va27 = ADD va25(0x20), v9ff
    0xa2b: va2b(0x40) = CONST 
    0xa2d: va2d = MLOAD va2b(0x40)
    0xa30: va30(0x64) = SUB va27, va2d
    0xa32: REVERT va2d, va30(0x64)

    Begin block 0xa33
    prev=[0x970], succ=[0xa87, 0xaf4]
    =================================
    0xa34: va34 = CALLER 
    0xa35: va35(0x3) = CONST 
    0xa37: va37(0x0) = CONST 
    0xa3a: va3a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa4f: va4f = AND va3a(0xffffffffffffffffffffffffffffffffffffffff), va34
    0xa50: va50(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa65: va65 = AND va50(0xffffffffffffffffffffffffffffffffffffffff), va4f
    0xa67: MSTORE va37(0x0), va65
    0xa68: va68(0x20) = CONST 
    0xa6a: va6a(0x20) = ADD va68(0x20), va37(0x0)
    0xa6d: MSTORE va6a(0x20), va35(0x3)
    0xa6e: va6e(0x20) = CONST 
    0xa70: va70(0x40) = ADD va6e(0x20), va6a(0x20)
    0xa71: va71(0x0) = CONST 
    0xa73: va73 = SHA3 va71(0x0), va70(0x40)
    0xa74: va74(0x0) = CONST 
    0xa77: va77 = SLOAD va73
    0xa79: va79(0x100) = CONST 
    0xa7c: va7c(0x1) = EXP va79(0x100), va74(0x0)
    0xa7e: va7e = DIV va77, va7c(0x1)
    0xa7f: va7f(0xff) = CONST 
    0xa81: va81 = AND va7f(0xff), va7e
    0xa82: va82 = ISZERO va81
    0xa83: va83(0xaf4) = CONST 
    0xa86: JUMPI va83(0xaf4), va82

    Begin block 0xa87
    prev=[0xa33], succ=[]
    =================================
    0xa87: va87(0x40) = CONST 
    0xa89: va89 = MLOAD va87(0x40)
    0xa8a: va8a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xaac: MSTORE va89, va8a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xaad: vaad(0x4) = CONST 
    0xaaf: vaaf = ADD vaad(0x4), va89
    0xab2: vab2(0x20) = CONST 
    0xab4: vab4 = ADD vab2(0x20), vaaf
    0xab7: vab7(0x20) = SUB vab4, vaaf
    0xab9: MSTORE vaaf, vab7(0x20)
    0xaba: vaba(0x16) = CONST 
    0xabd: MSTORE vab4, vaba(0x16)
    0xabe: vabe(0x20) = CONST 
    0xac0: vac0 = ADD vabe(0x20), vab4
    0xac2: vac2(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xae4: MSTORE vac0, vac2(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xae6: vae6(0x20) = CONST 
    0xae8: vae8 = ADD vae6(0x20), vac0
    0xaec: vaec(0x40) = CONST 
    0xaee: vaee = MLOAD vaec(0x40)
    0xaf1: vaf1(0x64) = SUB vae8, vaee
    0xaf3: REVERT vaee, vaf1(0x64)

    Begin block 0xaf4
    prev=[0xa33], succ=[0xb10, 0xb7d]
    =================================
    0xaf5: vaf5(0x0) = CONST 
    0xaf7: vaf7(0x1) = ISZERO vaf5(0x0)
    0xaf8: vaf8(0x0) = ISZERO vaf7(0x1)
    0xaf9: vaf9(0x6) = CONST 
    0xafb: vafb(0x14) = CONST 
    0xafe: vafe = SLOAD vaf9(0x6)
    0xb00: vb00(0x100) = CONST 
    0xb03: vb03(0x10000000000000000000000000000000000000000) = EXP vb00(0x100), vafb(0x14)
    0xb05: vb05 = DIV vafe, vb03(0x10000000000000000000000000000000000000000)
    0xb06: vb06(0xff) = CONST 
    0xb08: vb08 = AND vb06(0xff), vb05
    0xb09: vb09 = ISZERO vb08
    0xb0a: vb0a = ISZERO vb09
    0xb0b: vb0b = EQ vb0a, vaf8(0x0)
    0xb0c: vb0c(0xb7d) = CONST 
    0xb0f: JUMPI vb0c(0xb7d), vb0b

    Begin block 0xb10
    prev=[0xaf4], succ=[]
    =================================
    0xb10: vb10(0x40) = CONST 
    0xb12: vb12 = MLOAD vb10(0x40)
    0xb13: vb13(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xb35: MSTORE vb12, vb13(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb36: vb36(0x4) = CONST 
    0xb38: vb38 = ADD vb36(0x4), vb12
    0xb3b: vb3b(0x20) = CONST 
    0xb3d: vb3d = ADD vb3b(0x20), vb38
    0xb40: vb40(0x20) = SUB vb3d, vb38
    0xb42: MSTORE vb38, vb40(0x20)
    0xb43: vb43(0x16) = CONST 
    0xb46: MSTORE vb3d, vb43(0x16)
    0xb47: vb47(0x20) = CONST 
    0xb49: vb49 = ADD vb47(0x20), vb3d
    0xb4b: vb4b(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0xb6d: MSTORE vb49, vb4b(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0xb6f: vb6f(0x20) = CONST 
    0xb71: vb71 = ADD vb6f(0x20), vb49
    0xb75: vb75(0x40) = CONST 
    0xb77: vb77 = MLOAD vb75(0x40)
    0xb7a: vb7a(0x64) = SUB vb71, vb77
    0xb7c: REVERT vb77, vb7a(0x64)

    Begin block 0xb7d
    prev=[0xaf4], succ=[0xb8e]
    =================================
    0xb7e: vb7e(0x0) = CONST 
    0xb84: vb84(0xb8e) = CONST 
    0xb87: vb87 = CALLER 
    0xb8a: vb8a(0x29e6) = CONST 
    0xb8d: CALLPRIVATE vb8a(0x29e6), v26d, v263, vb87, vb84(0xb8e)

    Begin block 0xb8e
    prev=[0xb7d], succ=[0x27d]
    =================================
    0xb8f: vb8f(0x1) = CONST 
    0xb9b: JUMP v232(0x27d)

    Begin block 0x27d
    prev=[0xb8e], succ=[]
    =================================
    0x27e: v27e(0x40) = CONST 
    0x280: v280 = MLOAD v27e(0x40)
    0x283: v283 = ISZERO vb8f(0x1)
    0x284: v284 = ISZERO v283
    0x286: MSTORE v280, v284
    0x287: v287(0x20) = CONST 
    0x289: v289 = ADD v287(0x20), v280
    0x28d: v28d(0x40) = CONST 
    0x28f: v28f = MLOAD v28d(0x40)
    0x292: v292(0x20) = SUB v289, v28f
    0x294: RETURN v28f, v292(0x20)

}

function 0x2540(0x2540arg0x0, 0x2540arg0x1, 0x2540arg0x2) private {
    Begin block 0x2540
    prev=[], succ=[0x25890x2540]
    =================================
    0x2541: v2541(0x0) = CONST 
    0x2544: v2544(0x0) = CONST 
    0x2546: v2546(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2569: v2569(0x2597) = CONST 
    0x256c: v256c(0xde0b6b3a7640000) = CONST 
    0x2575: v2575(0x2589) = CONST 
    0x2578: v2578(0x5) = CONST 
    0x257a: v257a = SLOAD v2578(0x5)
    0x257c: v257c(0x2d1e) = CONST 
    0x2582: v2582(0xffffffff) = CONST 
    0x2587: v2587(0x2d1e) = AND v2582(0xffffffff), v257c(0x2d1e)
    0x2588: v2588_0 = CALLPRIVATE v2587(0x2d1e), v257a, v2546(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2575(0x2589)

    Begin block 0x25890x2540
    prev=[0x2540], succ=[0x25970x2540]
    =================================
    0x258a0x2540: v2540258a(0x2c98) = CONST 
    0x25900x2540: v25402590(0xffffffff) = CONST 
    0x25950x2540: v25402595(0x2c98) = AND v25402590(0xffffffff), v2540258a(0x2c98)
    0x25960x2540: v25402596_0 = CALLPRIVATE v25402595(0x2c98), v256c(0xde0b6b3a7640000), v2588_0, v2569(0x2597)

    Begin block 0x25970x2540
    prev=[0x25890x2540], succ=[0x261e0x2540, 0x26450x2540]
    =================================
    0x259b0x2540: v2540259b(0x2) = CONST 
    0x259d0x2540: v2540259d(0x0) = CONST 
    0x25a00x2540: v254025a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25b50x2540: v254025b5 = AND v254025a0(0xffffffffffffffffffffffffffffffffffffffff), v2540arg1
    0x25b60x2540: v254025b6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25cb0x2540: v254025cb = AND v254025b6(0xffffffffffffffffffffffffffffffffffffffff), v254025b5
    0x25cd0x2540: MSTORE v2540259d(0x0), v254025cb
    0x25ce0x2540: v254025ce(0x20) = CONST 
    0x25d00x2540: v254025d0(0x20) = ADD v254025ce(0x20), v2540259d(0x0)
    0x25d30x2540: MSTORE v254025d0(0x20), v2540259b(0x2)
    0x25d40x2540: v254025d4(0x20) = CONST 
    0x25d60x2540: v254025d6(0x40) = ADD v254025d4(0x20), v254025d0(0x20)
    0x25d70x2540: v254025d7(0x0) = CONST 
    0x25d90x2540: v254025d9 = SHA3 v254025d7(0x0), v254025d6(0x40)
    0x25da0x2540: v254025da(0x0) = CONST 
    0x25dd0x2540: v254025dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25f20x2540: v254025f2 = AND v254025dd(0xffffffffffffffffffffffffffffffffffffffff), v2540arg0
    0x25f30x2540: v254025f3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26080x2540: v25402608 = AND v254025f3(0xffffffffffffffffffffffffffffffffffffffff), v254025f2
    0x260a0x2540: MSTORE v254025da(0x0), v25402608
    0x260b0x2540: v2540260b(0x20) = CONST 
    0x260d0x2540: v2540260d(0x20) = ADD v2540260b(0x20), v254025da(0x0)
    0x26100x2540: MSTORE v2540260d(0x20), v254025d9
    0x26110x2540: v25402611(0x20) = CONST 
    0x26130x2540: v25402613(0x40) = ADD v25402611(0x20), v2540260d(0x20)
    0x26140x2540: v25402614(0x0) = CONST 
    0x26160x2540: v25402616 = SHA3 v25402614(0x0), v25402613(0x40)
    0x26170x2540: v25402617 = SLOAD v25402616
    0x26180x2540: v25402618 = GT v25402617, v25402596_0
    0x26190x2540: v25402619 = ISZERO v25402618
    0x261a0x2540: v2540261a(0x2645) = CONST 
    0x261d0x2540: JUMPI v2540261a(0x2645), v25402619

    Begin block 0x261e0x2540
    prev=[0x25970x2540], succ=[0x26f30x2540]
    =================================
    0x261e0x2540: v2540261e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26410x2540: v25402641(0x26f3) = CONST 
    0x26440x2540: JUMP v25402641(0x26f3)

    Begin block 0x26f30x2540
    prev=[0x261e0x2540, 0x26f00x2540], succ=[]
    =================================
    0x26f30x2540_0x1: v26f32540_1 = PHI v254026ef_0, v2540261e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x26fd0x2540: RETURNPRIVATE v2540arg2, v26f32540_1

    Begin block 0x26450x2540
    prev=[0x25970x2540], succ=[0x26e20x2540]
    =================================
    0x26460x2540: v25402646(0x26f0) = CONST 
    0x26490x2540: v25402649(0xde0b6b3a7640000) = CONST 
    0x26520x2540: v25402652(0x26e2) = CONST 
    0x26550x2540: v25402655(0x5) = CONST 
    0x26570x2540: v25402657 = SLOAD v25402655(0x5)
    0x26580x2540: v25402658(0x2) = CONST 
    0x265a0x2540: v2540265a(0x0) = CONST 
    0x265d0x2540: v2540265d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26720x2540: v25402672 = AND v2540265d(0xffffffffffffffffffffffffffffffffffffffff), v2540arg1
    0x26730x2540: v25402673(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26880x2540: v25402688 = AND v25402673(0xffffffffffffffffffffffffffffffffffffffff), v25402672
    0x268a0x2540: MSTORE v2540265a(0x0), v25402688
    0x268b0x2540: v2540268b(0x20) = CONST 
    0x268d0x2540: v2540268d(0x20) = ADD v2540268b(0x20), v2540265a(0x0)
    0x26900x2540: MSTORE v2540268d(0x20), v25402658(0x2)
    0x26910x2540: v25402691(0x20) = CONST 
    0x26930x2540: v25402693(0x40) = ADD v25402691(0x20), v2540268d(0x20)
    0x26940x2540: v25402694(0x0) = CONST 
    0x26960x2540: v25402696 = SHA3 v25402694(0x0), v25402693(0x40)
    0x26970x2540: v25402697(0x0) = CONST 
    0x269a0x2540: v2540269a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26af0x2540: v254026af = AND v2540269a(0xffffffffffffffffffffffffffffffffffffffff), v2540arg0
    0x26b00x2540: v254026b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26c50x2540: v254026c5 = AND v254026b0(0xffffffffffffffffffffffffffffffffffffffff), v254026af
    0x26c70x2540: MSTORE v25402697(0x0), v254026c5
    0x26c80x2540: v254026c8(0x20) = CONST 
    0x26ca0x2540: v254026ca(0x20) = ADD v254026c8(0x20), v25402697(0x0)
    0x26cd0x2540: MSTORE v254026ca(0x20), v25402696
    0x26ce0x2540: v254026ce(0x20) = CONST 
    0x26d00x2540: v254026d0(0x40) = ADD v254026ce(0x20), v254026ca(0x20)
    0x26d10x2540: v254026d1(0x0) = CONST 
    0x26d30x2540: v254026d3 = SHA3 v254026d1(0x0), v254026d0(0x40)
    0x26d40x2540: v254026d4 = SLOAD v254026d3
    0x26d50x2540: v254026d5(0x2c98) = CONST 
    0x26db0x2540: v254026db(0xffffffff) = CONST 
    0x26e00x2540: v254026e0(0x2c98) = AND v254026db(0xffffffff), v254026d5(0x2c98)
    0x26e10x2540: v254026e1_0 = CALLPRIVATE v254026e0(0x2c98), v25402657, v254026d4, v25402652(0x26e2)

    Begin block 0x26e20x2540
    prev=[0x26450x2540], succ=[0x26f00x2540]
    =================================
    0x26e30x2540: v254026e3(0x2d1e) = CONST 
    0x26e90x2540: v254026e9(0xffffffff) = CONST 
    0x26ee0x2540: v254026ee(0x2d1e) = AND v254026e9(0xffffffff), v254026e3(0x2d1e)
    0x26ef0x2540: v254026ef_0 = CALLPRIVATE v254026ee(0x2d1e), v25402649(0xde0b6b3a7640000), v254026e1_0, v25402646(0x26f0)

    Begin block 0x26f00x2540
    prev=[0x26e20x2540], succ=[0x26f30x2540]
    =================================

}

function initialized()() public {
    Begin block 0x295
    prev=[], succ=[0xb9c]
    =================================
    0x296: v296(0x29d) = CONST 
    0x299: v299(0xb9c) = CONST 
    0x29c: JUMP v299(0xb9c)

    Begin block 0xb9c
    prev=[0x295], succ=[0x29d]
    =================================
    0xb9d: vb9d(0x0) = CONST 
    0xba0: vba0 = SLOAD vb9d(0x0)
    0xba2: vba2(0x100) = CONST 
    0xba5: vba5(0x1) = EXP vba2(0x100), vb9d(0x0)
    0xba7: vba7 = DIV vba0, vba5(0x1)
    0xba8: vba8(0xff) = CONST 
    0xbaa: vbaa = AND vba8(0xff), vba7
    0xbac: JUMP v296(0x29d)

    Begin block 0x29d
    prev=[0xb9c], succ=[]
    =================================
    0x29e: v29e(0x40) = CONST 
    0x2a0: v2a0 = MLOAD v29e(0x40)
    0x2a3: v2a3 = ISZERO vbaa
    0x2a4: v2a4 = ISZERO v2a3
    0x2a6: MSTORE v2a0, v2a4
    0x2a7: v2a7(0x20) = CONST 
    0x2a9: v2a9 = ADD v2a7(0x20), v2a0
    0x2ad: v2ad(0x40) = CONST 
    0x2af: v2af = MLOAD v2ad(0x40)
    0x2b2: v2b2(0x20) = SUB v2a9, v2af
    0x2b4: RETURN v2af, v2b2(0x20)

}

function 0x29e6(0x29e6arg0x0, 0x29e6arg0x1, 0x29e6arg0x2, 0x29e6arg0x3) private {
    Begin block 0x29e6
    prev=[], succ=[0x2a1c, 0x2a6c]
    =================================
    0x29e7: v29e7(0x0) = CONST 
    0x29e9: v29e9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29fe: v29fe(0x0) = AND v29e9(0xffffffffffffffffffffffffffffffffffffffff), v29e7(0x0)
    0x2a00: v2a00(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a15: v2a15 = AND v2a00(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg2
    0x2a16: v2a16 = EQ v2a15, v29fe(0x0)
    0x2a17: v2a17 = ISZERO v2a16
    0x2a18: v2a18(0x2a6c) = CONST 
    0x2a1b: JUMPI v2a18(0x2a6c), v2a17

    Begin block 0x2a1c
    prev=[0x29e6], succ=[]
    =================================
    0x2a1c: v2a1c(0x40) = CONST 
    0x2a1e: v2a1e = MLOAD v2a1c(0x40)
    0x2a1f: v2a1f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a41: MSTORE v2a1e, v2a1f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a42: v2a42(0x4) = CONST 
    0x2a44: v2a44 = ADD v2a42(0x4), v2a1e
    0x2a47: v2a47(0x20) = CONST 
    0x2a49: v2a49 = ADD v2a47(0x20), v2a44
    0x2a4c: v2a4c(0x20) = SUB v2a49, v2a44
    0x2a4e: MSTORE v2a44, v2a4c(0x20)
    0x2a4f: v2a4f(0x24) = CONST 
    0x2a52: MSTORE v2a49, v2a4f(0x24)
    0x2a53: v2a53(0x20) = CONST 
    0x2a55: v2a55 = ADD v2a53(0x20), v2a49
    0x2a57: v2a57(0x3944) = CONST 
    0x2a5a: v2a5a(0x24) = CONST 
    0x2a5d: CODECOPY v2a55, v2a57(0x3944), v2a5a(0x24)
    0x2a5e: v2a5e(0x40) = CONST 
    0x2a60: v2a60 = ADD v2a5e(0x40), v2a55
    0x2a64: v2a64(0x40) = CONST 
    0x2a66: v2a66 = MLOAD v2a64(0x40)
    0x2a69: v2a69(0x84) = SUB v2a60, v2a66
    0x2a6b: REVERT v2a66, v2a69(0x84)

    Begin block 0x2a6c
    prev=[0x29e6], succ=[0x2aa2, 0x2af2]
    =================================
    0x2a6d: v2a6d(0x0) = CONST 
    0x2a6f: v2a6f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a84: v2a84(0x0) = AND v2a6f(0xffffffffffffffffffffffffffffffffffffffff), v2a6d(0x0)
    0x2a86: v2a86(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a9b: v2a9b = AND v2a86(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg1
    0x2a9c: v2a9c = EQ v2a9b, v2a84(0x0)
    0x2a9d: v2a9d = ISZERO v2a9c
    0x2a9e: v2a9e(0x2af2) = CONST 
    0x2aa1: JUMPI v2a9e(0x2af2), v2a9d

    Begin block 0x2aa2
    prev=[0x2a6c], succ=[]
    =================================
    0x2aa2: v2aa2(0x40) = CONST 
    0x2aa4: v2aa4 = MLOAD v2aa2(0x40)
    0x2aa5: v2aa5(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ac7: MSTORE v2aa4, v2aa5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ac8: v2ac8(0x4) = CONST 
    0x2aca: v2aca = ADD v2ac8(0x4), v2aa4
    0x2acd: v2acd(0x20) = CONST 
    0x2acf: v2acf = ADD v2acd(0x20), v2aca
    0x2ad2: v2ad2(0x20) = SUB v2acf, v2aca
    0x2ad4: MSTORE v2aca, v2ad2(0x20)
    0x2ad5: v2ad5(0x22) = CONST 
    0x2ad8: MSTORE v2acf, v2ad5(0x22)
    0x2ad9: v2ad9(0x20) = CONST 
    0x2adb: v2adb = ADD v2ad9(0x20), v2acf
    0x2add: v2add(0x37d8) = CONST 
    0x2ae0: v2ae0(0x22) = CONST 
    0x2ae3: CODECOPY v2adb, v2add(0x37d8), v2ae0(0x22)
    0x2ae4: v2ae4(0x40) = CONST 
    0x2ae6: v2ae6 = ADD v2ae4(0x40), v2adb
    0x2aea: v2aea(0x40) = CONST 
    0x2aec: v2aec = MLOAD v2aea(0x40)
    0x2aef: v2aef(0x84) = SUB v2ae6, v2aec
    0x2af1: REVERT v2aec, v2aef(0x84)

    Begin block 0x2af2
    prev=[0x2a6c], succ=[0x2b39]
    =================================
    0x2af3: v2af3(0x0) = CONST 
    0x2af6: v2af6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b19: v2b19(0x2b47) = CONST 
    0x2b1c: v2b1c(0xde0b6b3a7640000) = CONST 
    0x2b25: v2b25(0x2b39) = CONST 
    0x2b28: v2b28(0x5) = CONST 
    0x2b2a: v2b2a = SLOAD v2b28(0x5)
    0x2b2c: v2b2c(0x2d1e) = CONST 
    0x2b32: v2b32(0xffffffff) = CONST 
    0x2b37: v2b37(0x2d1e) = AND v2b32(0xffffffff), v2b2c(0x2d1e)
    0x2b38: v2b38_0 = CALLPRIVATE v2b37(0x2d1e), v2b2a, v2af6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2b25(0x2b39)

    Begin block 0x2b39
    prev=[0x2af2], succ=[0x2b47]
    =================================
    0x2b3a: v2b3a(0x2c98) = CONST 
    0x2b40: v2b40(0xffffffff) = CONST 
    0x2b45: v2b45(0x2c98) = AND v2b40(0xffffffff), v2b3a(0x2c98)
    0x2b46: v2b46_0 = CALLPRIVATE v2b45(0x2c98), v2b1c(0xde0b6b3a7640000), v2b38_0, v2b19(0x2b47)

    Begin block 0x2b47
    prev=[0x2b39], succ=[0x2b52, 0x2b79]
    =================================
    0x2b4c: v2b4c = GT v29e6arg0, v2b46_0
    0x2b4d: v2b4d = ISZERO v2b4c
    0x2b4e: v2b4e(0x2b79) = CONST 
    0x2b51: JUMPI v2b4e(0x2b79), v2b4d

    Begin block 0x2b52
    prev=[0x2b47], succ=[0x2bab]
    =================================
    0x2b52: v2b52(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b75: v2b75(0x2bab) = CONST 
    0x2b78: JUMP v2b75(0x2bab)

    Begin block 0x2bab
    prev=[0x2b52, 0x2ba8], succ=[]
    =================================
    0x2bab_0x1: v2bab_1 = PHI v2b52(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2ba7_0
    0x2bad: v2bad(0x2) = CONST 
    0x2baf: v2baf(0x0) = CONST 
    0x2bb2: v2bb2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2bc7: v2bc7 = AND v2bb2(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg2
    0x2bc8: v2bc8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2bdd: v2bdd = AND v2bc8(0xffffffffffffffffffffffffffffffffffffffff), v2bc7
    0x2bdf: MSTORE v2baf(0x0), v2bdd
    0x2be0: v2be0(0x20) = CONST 
    0x2be2: v2be2(0x20) = ADD v2be0(0x20), v2baf(0x0)
    0x2be5: MSTORE v2be2(0x20), v2bad(0x2)
    0x2be6: v2be6(0x20) = CONST 
    0x2be8: v2be8(0x40) = ADD v2be6(0x20), v2be2(0x20)
    0x2be9: v2be9(0x0) = CONST 
    0x2beb: v2beb = SHA3 v2be9(0x0), v2be8(0x40)
    0x2bec: v2bec(0x0) = CONST 
    0x2bef: v2bef(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c04: v2c04 = AND v2bef(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg1
    0x2c05: v2c05(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c1a: v2c1a = AND v2c05(0xffffffffffffffffffffffffffffffffffffffff), v2c04
    0x2c1c: MSTORE v2bec(0x0), v2c1a
    0x2c1d: v2c1d(0x20) = CONST 
    0x2c1f: v2c1f(0x20) = ADD v2c1d(0x20), v2bec(0x0)
    0x2c22: MSTORE v2c1f(0x20), v2beb
    0x2c23: v2c23(0x20) = CONST 
    0x2c25: v2c25(0x40) = ADD v2c23(0x20), v2c1f(0x20)
    0x2c26: v2c26(0x0) = CONST 
    0x2c28: v2c28 = SHA3 v2c26(0x0), v2c25(0x40)
    0x2c2b: SSTORE v2c28, v2bab_1
    0x2c2e: v2c2e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c43: v2c43 = AND v2c2e(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg1
    0x2c45: v2c45(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c5a: v2c5a = AND v2c45(0xffffffffffffffffffffffffffffffffffffffff), v29e6arg2
    0x2c5b: v2c5b(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x2c7d: v2c7d(0x40) = CONST 
    0x2c7f: v2c7f = MLOAD v2c7d(0x40)
    0x2c83: MSTORE v2c7f, v29e6arg0
    0x2c84: v2c84(0x20) = CONST 
    0x2c86: v2c86 = ADD v2c84(0x20), v2c7f
    0x2c8a: v2c8a(0x40) = CONST 
    0x2c8c: v2c8c = MLOAD v2c8a(0x40)
    0x2c8f: v2c8f(0x20) = SUB v2c86, v2c8c
    0x2c91: LOG3 v2c8c, v2c8f(0x20), v2c5b(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v2c5a, v2c43
    0x2c97: RETURNPRIVATE v29e6arg3

    Begin block 0x2b79
    prev=[0x2b47], succ=[0x2b9a]
    =================================
    0x2b7a: v2b7a(0x2ba8) = CONST 
    0x2b7d: v2b7d(0x5) = CONST 
    0x2b7f: v2b7f = SLOAD v2b7d(0x5)
    0x2b80: v2b80(0x2b9a) = CONST 
    0x2b83: v2b83(0xde0b6b3a7640000) = CONST 
    0x2b8d: v2b8d(0x2c98) = CONST 
    0x2b93: v2b93(0xffffffff) = CONST 
    0x2b98: v2b98(0x2c98) = AND v2b93(0xffffffff), v2b8d(0x2c98)
    0x2b99: v2b99_0 = CALLPRIVATE v2b98(0x2c98), v2b83(0xde0b6b3a7640000), v29e6arg0, v2b80(0x2b9a)

    Begin block 0x2b9a
    prev=[0x2b79], succ=[0x2ba8]
    =================================
    0x2b9b: v2b9b(0x2d1e) = CONST 
    0x2ba1: v2ba1(0xffffffff) = CONST 
    0x2ba6: v2ba6(0x2d1e) = AND v2ba1(0xffffffff), v2b9b(0x2d1e)
    0x2ba7: v2ba7_0 = CALLPRIVATE v2ba6(0x2d1e), v2b7f, v2b99_0, v2b7a(0x2ba8)

    Begin block 0x2ba8
    prev=[0x2b9a], succ=[0x2bab]
    =================================

}

function totalSupply()() public {
    Begin block 0x2b5
    prev=[], succ=[0xbadB0x2b5]
    =================================
    0x2b6: v2b6(0x2bd) = CONST 
    0x2b9: v2b9(0xbad) = CONST 
    0x2bc: JUMP v2b9(0xbad)

    Begin block 0xbadB0x2b5
    prev=[0x2b5], succ=[0xbd2B0x2b5]
    =================================
    0xbaeS0x2b5: vbaeV2b5(0x0) = CONST 
    0xbb0S0x2b5: vbb0V2b5(0xbe0) = CONST 
    0xbb3S0x2b5: vbb3V2b5(0xde0b6b3a7640000) = CONST 
    0xbbcS0x2b5: vbbcV2b5(0xbd2) = CONST 
    0xbbfS0x2b5: vbbfV2b5(0x5) = CONST 
    0xbc1S0x2b5: vbc1V2b5 = SLOAD vbbfV2b5(0x5)
    0xbc2S0x2b5: vbc2V2b5(0x4) = CONST 
    0xbc4S0x2b5: vbc4V2b5 = SLOAD vbc2V2b5(0x4)
    0xbc5S0x2b5: vbc5V2b5(0x2c98) = CONST 
    0xbcbS0x2b5: vbcbV2b5(0xffffffff) = CONST 
    0xbd0S0x2b5: vbd0V2b5(0x2c98) = AND vbcbV2b5(0xffffffff), vbc5V2b5(0x2c98)
    0xbd1S0x2b5: vbd1_0V2b5 = CALLPRIVATE vbd0V2b5(0x2c98), vbc1V2b5, vbc4V2b5, vbbcV2b5(0xbd2)

    Begin block 0xbd2B0x2b5
    prev=[0xbadB0x2b5], succ=[0xbe0B0x2b5]
    =================================
    0xbd3S0x2b5: vbd3V2b5(0x2d1e) = CONST 
    0xbd9S0x2b5: vbd9V2b5(0xffffffff) = CONST 
    0xbdeS0x2b5: vbdeV2b5(0x2d1e) = AND vbd9V2b5(0xffffffff), vbd3V2b5(0x2d1e)
    0xbdfS0x2b5: vbdf_0V2b5 = CALLPRIVATE vbdeV2b5(0x2d1e), vbb3V2b5(0xde0b6b3a7640000), vbd1_0V2b5, vbb0V2b5(0xbe0)

    Begin block 0xbe0B0x2b5
    prev=[0xbd2B0x2b5], succ=[0x2bd]
    =================================
    0xbe4S0x2b5: JUMP v2b6(0x2bd)

    Begin block 0x2bd
    prev=[0xbe0B0x2b5], succ=[]
    =================================
    0x2be: v2be(0x40) = CONST 
    0x2c0: v2c0 = MLOAD v2be(0x40)
    0x2c4: MSTORE v2c0, vbdf_0V2b5
    0x2c5: v2c5(0x20) = CONST 
    0x2c7: v2c7 = ADD v2c5(0x20), v2c0
    0x2cb: v2cb(0x40) = CONST 
    0x2cd: v2cd = MLOAD v2cb(0x40)
    0x2d0: v2d0(0x20) = SUB v2c7, v2cd
    0x2d2: RETURN v2cd, v2d0(0x20)

}

function 0x2c98(0x2c98arg0x0, 0x2c98arg0x1, 0x2c98arg0x2) private {
    Begin block 0x2c98
    prev=[], succ=[0x2ca3, 0x2cab]
    =================================
    0x2c99: v2c99(0x0) = CONST 
    0x2c9d: v2c9d = EQ v2c98arg1, v2c99(0x0)
    0x2c9e: v2c9e = ISZERO v2c9d
    0x2c9f: v2c9f(0x2cab) = CONST 
    0x2ca2: JUMPI v2c9f(0x2cab), v2c9e

    Begin block 0x2ca3
    prev=[0x2c98], succ=[0x2d18]
    =================================
    0x2ca3: v2ca3(0x0) = CONST 
    0x2ca7: v2ca7(0x2d18) = CONST 
    0x2caa: JUMP v2ca7(0x2d18)

    Begin block 0x2d18
    prev=[0x2ca3, 0x2d13], succ=[]
    =================================
    0x2d18_0x0: v2d18_0 = PHI v2ca3(0x0), v2cb0
    0x2d1d: RETURNPRIVATE v2c98arg2, v2d18_0

    Begin block 0x2cab
    prev=[0x2c98], succ=[0x2cbb, 0x2cbc]
    =================================
    0x2cac: v2cac(0x0) = CONST 
    0x2cb0: v2cb0 = MUL v2c98arg1, v2c98arg0
    0x2cb7: v2cb7(0x2cbc) = CONST 
    0x2cba: JUMPI v2cb7(0x2cbc), v2c98arg1

    Begin block 0x2cbb
    prev=[0x2cab], succ=[]
    =================================
    0x2cbb: THROW 

    Begin block 0x2cbc
    prev=[0x2cab], succ=[0x2cc3, 0x2d13]
    =================================
    0x2cbd: v2cbd = DIV v2cb0, v2c98arg1
    0x2cbe: v2cbe = EQ v2cbd, v2c98arg0
    0x2cbf: v2cbf(0x2d13) = CONST 
    0x2cc2: JUMPI v2cbf(0x2d13), v2cbe

    Begin block 0x2cc3
    prev=[0x2cbc], succ=[]
    =================================
    0x2cc3: v2cc3(0x40) = CONST 
    0x2cc5: v2cc5 = MLOAD v2cc3(0x40)
    0x2cc6: v2cc6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ce8: MSTORE v2cc5, v2cc6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ce9: v2ce9(0x4) = CONST 
    0x2ceb: v2ceb = ADD v2ce9(0x4), v2cc5
    0x2cee: v2cee(0x20) = CONST 
    0x2cf0: v2cf0 = ADD v2cee(0x20), v2ceb
    0x2cf3: v2cf3(0x20) = SUB v2cf0, v2ceb
    0x2cf5: MSTORE v2ceb, v2cf3(0x20)
    0x2cf6: v2cf6(0x21) = CONST 
    0x2cf9: MSTORE v2cf0, v2cf6(0x21)
    0x2cfa: v2cfa(0x20) = CONST 
    0x2cfc: v2cfc = ADD v2cfa(0x20), v2cf0
    0x2cfe: v2cfe(0x3849) = CONST 
    0x2d01: v2d01(0x21) = CONST 
    0x2d04: CODECOPY v2cfc, v2cfe(0x3849), v2d01(0x21)
    0x2d05: v2d05(0x40) = CONST 
    0x2d07: v2d07 = ADD v2d05(0x40), v2cfc
    0x2d0b: v2d0b(0x40) = CONST 
    0x2d0d: v2d0d = MLOAD v2d0b(0x40)
    0x2d10: v2d10(0x84) = SUB v2d07, v2d0d
    0x2d12: REVERT v2d0d, v2d10(0x84)

    Begin block 0x2d13
    prev=[0x2cbc], succ=[0x2d18]
    =================================

}

function 0x2d1e(0x2d1earg0x0, 0x2d1earg0x1, 0x2d1earg0x2) private {
    Begin block 0x2d1e
    prev=[], succ=[0x3679]
    =================================
    0x2d1f: v2d1f(0x0) = CONST 
    0x2d21: v2d21(0x2d60) = CONST 
    0x2d26: v2d26(0x40) = CONST 
    0x2d28: v2d28 = MLOAD v2d26(0x40)
    0x2d2a: v2d2a(0x40) = CONST 
    0x2d2c: v2d2c = ADD v2d2a(0x40), v2d28
    0x2d2d: v2d2d(0x40) = CONST 
    0x2d2f: MSTORE v2d2d(0x40), v2d2c
    0x2d31: v2d31(0x1a) = CONST 
    0x2d34: MSTORE v2d28, v2d31(0x1a)
    0x2d35: v2d35(0x20) = CONST 
    0x2d37: v2d37 = ADD v2d35(0x20), v2d28
    0x2d38: v2d38(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x2d5a: MSTORE v2d37, v2d38(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x2d5c: v2d5c(0x3679) = CONST 
    0x2d5f: JUMP v2d5c(0x3679)

    Begin block 0x3679
    prev=[0x2d1e], succ=[0x3685, 0x3725]
    =================================
    0x367a: v367a(0x0) = CONST 
    0x367e: v367e = GT v2d1earg0, v367a(0x0)
    0x3681: v3681(0x3725) = CONST 
    0x3684: JUMPI v3681(0x3725), v367e

    Begin block 0x3685
    prev=[0x3679], succ=[0x36cf]
    =================================
    0x3685: v3685(0x40) = CONST 
    0x3687: v3687 = MLOAD v3685(0x40)
    0x3688: v3688(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x36aa: MSTORE v3687, v3688(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x36ab: v36ab(0x4) = CONST 
    0x36ad: v36ad = ADD v36ab(0x4), v3687
    0x36b0: v36b0(0x20) = CONST 
    0x36b2: v36b2 = ADD v36b0(0x20), v36ad
    0x36b5: v36b5(0x20) = SUB v36b2, v36ad
    0x36b7: MSTORE v36ad, v36b5(0x20)
    0x36bb: v36bb(0x1a) = MLOAD v2d28
    0x36bd: MSTORE v36b2, v36bb(0x1a)
    0x36be: v36be(0x20) = CONST 
    0x36c0: v36c0 = ADD v36be(0x20), v36b2
    0x36c4: v36c4(0x1a) = MLOAD v2d28
    0x36c6: v36c6(0x20) = CONST 
    0x36c8: v36c8 = ADD v36c6(0x20), v2d28
    0x36cd: v36cd(0x0) = CONST 

    Begin block 0x36cf
    prev=[0x3685, 0x36d8], succ=[0x36ea, 0x36d8]
    =================================
    0x36cf_0x0: v36cf_0 = PHI v36cd(0x0), v36e3
    0x36d2: v36d2 = LT v36cf_0, v36c4(0x1a)
    0x36d3: v36d3 = ISZERO v36d2
    0x36d4: v36d4(0x36ea) = CONST 
    0x36d7: JUMPI v36d4(0x36ea), v36d3

    Begin block 0x36ea
    prev=[0x36cf], succ=[0x3717, 0x36fe]
    =================================
    0x36f3: v36f3 = ADD v36c4(0x1a), v36c0
    0x36f5: v36f5(0x1f) = CONST 
    0x36f7: v36f7(0x1a) = AND v36f5(0x1f), v36c4(0x1a)
    0x36f9: v36f9 = ISZERO v36f7(0x1a)
    0x36fa: v36fa(0x3717) = CONST 
    0x36fd: JUMPI v36fa(0x3717), v36f9

    Begin block 0x3717
    prev=[0x36ea, 0x36fe], succ=[]
    =================================
    0x3717_0x1: v3717_1 = PHI v36f3, v3714
    0x371d: v371d(0x40) = CONST 
    0x371f: v371f = MLOAD v371d(0x40)
    0x3722: v3722 = SUB v3717_1, v371f
    0x3724: REVERT v371f, v3722

    Begin block 0x36fe
    prev=[0x36ea], succ=[0x3717]
    =================================
    0x3700: v3700 = SUB v36f3, v36f7(0x1a)
    0x3702: v3702 = MLOAD v3700
    0x3703: v3703(0x1) = CONST 
    0x3706: v3706(0x20) = CONST 
    0x3708: v3708(0x6) = SUB v3706(0x20), v36f7(0x1a)
    0x3709: v3709(0x100) = CONST 
    0x370c: v370c(0x1000000000000) = EXP v3709(0x100), v3708(0x6)
    0x370d: v370d(0xffffffffffff) = SUB v370c(0x1000000000000), v3703(0x1)
    0x370e: v370e = NOT v370d(0xffffffffffff)
    0x370f: v370f = AND v370e, v3702
    0x3711: MSTORE v3700, v370f
    0x3712: v3712(0x20) = CONST 
    0x3714: v3714 = ADD v3712(0x20), v3700

    Begin block 0x36d8
    prev=[0x36cf], succ=[0x36cf]
    =================================
    0x36d8_0x0: v36d8_0 = PHI v36cd(0x0), v36e3
    0x36da: v36da = ADD v36c8, v36d8_0
    0x36db: v36db = MLOAD v36da
    0x36de: v36de = ADD v36c0, v36d8_0
    0x36df: MSTORE v36de, v36db
    0x36e0: v36e0(0x20) = CONST 
    0x36e3: v36e3 = ADD v36d8_0, v36e0(0x20)
    0x36e6: v36e6(0x36cf) = CONST 
    0x36e9: JUMP v36e6(0x36cf)

    Begin block 0x3725
    prev=[0x3679], succ=[0x3730, 0x3731]
    =================================
    0x3727: v3727(0x0) = CONST 
    0x372c: v372c(0x3731) = CONST 
    0x372f: JUMPI v372c(0x3731), v2d1earg0

    Begin block 0x3730
    prev=[0x3725], succ=[]
    =================================
    0x3730: THROW 

    Begin block 0x3731
    prev=[0x3725], succ=[0x2d60]
    =================================
    0x3732: v3732 = DIV v2d1earg1, v2d1earg0
    0x373e: JUMP v2d21(0x2d60)

    Begin block 0x2d60
    prev=[0x3731], succ=[]
    =================================
    0x2d67: RETURNPRIVATE v2d1earg2, v3732

}

function multiplier()() public {
    Begin block 0x2d3
    prev=[], succ=[0xbe5]
    =================================
    0x2d4: v2d4(0x2db) = CONST 
    0x2d7: v2d7(0xbe5) = CONST 
    0x2da: JUMP v2d7(0xbe5)

    Begin block 0xbe5
    prev=[0x2d3], succ=[0x2db]
    =================================
    0xbe6: vbe6(0x5) = CONST 
    0xbe8: vbe8 = SLOAD vbe6(0x5)
    0xbea: JUMP v2d4(0x2db)

    Begin block 0x2db
    prev=[0xbe5], succ=[]
    =================================
    0x2dc: v2dc(0x40) = CONST 
    0x2de: v2de = MLOAD v2dc(0x40)
    0x2e2: MSTORE v2de, vbe8
    0x2e3: v2e3(0x20) = CONST 
    0x2e5: v2e5 = ADD v2e3(0x20), v2de
    0x2e9: v2e9(0x40) = CONST 
    0x2eb: v2eb = MLOAD v2e9(0x40)
    0x2ee: v2ee(0x20) = SUB v2e5, v2eb
    0x2f0: RETURN v2eb, v2ee(0x20)

}

function 0x2d70(0x2d70arg0x0, 0x2d70arg0x1, 0x2d70arg0x2, 0x2d70arg0x3) private {
    Begin block 0x2d70
    prev=[], succ=[0x2da6, 0x2df6]
    =================================
    0x2d71: v2d71(0x0) = CONST 
    0x2d73: v2d73(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d88: v2d88(0x0) = AND v2d73(0xffffffffffffffffffffffffffffffffffffffff), v2d71(0x0)
    0x2d8a: v2d8a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d9f: v2d9f = AND v2d8a(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg2
    0x2da0: v2da0 = EQ v2d9f, v2d88(0x0)
    0x2da1: v2da1 = ISZERO v2da0
    0x2da2: v2da2(0x2df6) = CONST 
    0x2da5: JUMPI v2da2(0x2df6), v2da1

    Begin block 0x2da6
    prev=[0x2d70], succ=[]
    =================================
    0x2da6: v2da6(0x40) = CONST 
    0x2da8: v2da8 = MLOAD v2da6(0x40)
    0x2da9: v2da9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2dcb: MSTORE v2da8, v2da9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2dcc: v2dcc(0x4) = CONST 
    0x2dce: v2dce = ADD v2dcc(0x4), v2da8
    0x2dd1: v2dd1(0x20) = CONST 
    0x2dd3: v2dd3 = ADD v2dd1(0x20), v2dce
    0x2dd6: v2dd6(0x20) = SUB v2dd3, v2dce
    0x2dd8: MSTORE v2dce, v2dd6(0x20)
    0x2dd9: v2dd9(0x25) = CONST 
    0x2ddc: MSTORE v2dd3, v2dd9(0x25)
    0x2ddd: v2ddd(0x20) = CONST 
    0x2ddf: v2ddf = ADD v2ddd(0x20), v2dd3
    0x2de1: v2de1(0x38ec) = CONST 
    0x2de4: v2de4(0x25) = CONST 
    0x2de7: CODECOPY v2ddf, v2de1(0x38ec), v2de4(0x25)
    0x2de8: v2de8(0x40) = CONST 
    0x2dea: v2dea = ADD v2de8(0x40), v2ddf
    0x2dee: v2dee(0x40) = CONST 
    0x2df0: v2df0 = MLOAD v2dee(0x40)
    0x2df3: v2df3(0x84) = SUB v2dea, v2df0
    0x2df5: REVERT v2df0, v2df3(0x84)

    Begin block 0x2df6
    prev=[0x2d70], succ=[0x2e2c, 0x2e7c]
    =================================
    0x2df7: v2df7(0x0) = CONST 
    0x2df9: v2df9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e0e: v2e0e(0x0) = AND v2df9(0xffffffffffffffffffffffffffffffffffffffff), v2df7(0x0)
    0x2e10: v2e10(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e25: v2e25 = AND v2e10(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg1
    0x2e26: v2e26 = EQ v2e25, v2e0e(0x0)
    0x2e27: v2e27 = ISZERO v2e26
    0x2e28: v2e28(0x2e7c) = CONST 
    0x2e2b: JUMPI v2e28(0x2e7c), v2e27

    Begin block 0x2e2c
    prev=[0x2df6], succ=[]
    =================================
    0x2e2c: v2e2c(0x40) = CONST 
    0x2e2e: v2e2e = MLOAD v2e2c(0x40)
    0x2e2f: v2e2f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2e51: MSTORE v2e2e, v2e2f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2e52: v2e52(0x4) = CONST 
    0x2e54: v2e54 = ADD v2e52(0x4), v2e2e
    0x2e57: v2e57(0x20) = CONST 
    0x2e59: v2e59 = ADD v2e57(0x20), v2e54
    0x2e5c: v2e5c(0x20) = SUB v2e59, v2e54
    0x2e5e: MSTORE v2e54, v2e5c(0x20)
    0x2e5f: v2e5f(0x23) = CONST 
    0x2e62: MSTORE v2e59, v2e5f(0x23)
    0x2e63: v2e63(0x20) = CONST 
    0x2e65: v2e65 = ADD v2e63(0x20), v2e59
    0x2e67: v2e67(0x378a) = CONST 
    0x2e6a: v2e6a(0x23) = CONST 
    0x2e6d: CODECOPY v2e65, v2e67(0x378a), v2e6a(0x23)
    0x2e6e: v2e6e(0x40) = CONST 
    0x2e70: v2e70 = ADD v2e6e(0x40), v2e65
    0x2e74: v2e74(0x40) = CONST 
    0x2e76: v2e76 = MLOAD v2e74(0x40)
    0x2e79: v2e79(0x84) = SUB v2e70, v2e76
    0x2e7b: REVERT v2e76, v2e79(0x84)

    Begin block 0x2e7c
    prev=[0x2df6], succ=[0x2e9f]
    =================================
    0x2e7d: v2e7d(0x0) = CONST 
    0x2e7f: v2e7f(0x2ead) = CONST 
    0x2e82: v2e82(0x5) = CONST 
    0x2e84: v2e84 = SLOAD v2e82(0x5)
    0x2e85: v2e85(0x2e9f) = CONST 
    0x2e88: v2e88(0xde0b6b3a7640000) = CONST 
    0x2e92: v2e92(0x2c98) = CONST 
    0x2e98: v2e98(0xffffffff) = CONST 
    0x2e9d: v2e9d(0x2c98) = AND v2e98(0xffffffff), v2e92(0x2c98)
    0x2e9e: v2e9e_0 = CALLPRIVATE v2e9d(0x2c98), v2e88(0xde0b6b3a7640000), v2d70arg0, v2e85(0x2e9f)

    Begin block 0x2e9f
    prev=[0x2e7c], succ=[0x2ead]
    =================================
    0x2ea0: v2ea0(0x2d1e) = CONST 
    0x2ea6: v2ea6(0xffffffff) = CONST 
    0x2eab: v2eab(0x2d1e) = AND v2ea6(0xffffffff), v2ea0(0x2d1e)
    0x2eac: v2eac_0 = CALLPRIVATE v2eab(0x2d1e), v2e84, v2e9e_0, v2e7f(0x2ead)

    Begin block 0x2ead
    prev=[0x2e9f], succ=[0x2f1b]
    =================================
    0x2eb0: v2eb0(0x2f1b) = CONST 
    0x2eb4: v2eb4(0x40) = CONST 
    0x2eb6: v2eb6 = MLOAD v2eb4(0x40)
    0x2eb8: v2eb8(0x60) = CONST 
    0x2eba: v2eba = ADD v2eb8(0x60), v2eb6
    0x2ebb: v2ebb(0x40) = CONST 
    0x2ebd: MSTORE v2ebb(0x40), v2eba
    0x2ebf: v2ebf(0x2b) = CONST 
    0x2ec2: MSTORE v2eb6, v2ebf(0x2b)
    0x2ec3: v2ec3(0x20) = CONST 
    0x2ec5: v2ec5 = ADD v2ec3(0x20), v2eb6
    0x2ec6: v2ec6(0x37ad) = CONST 
    0x2ec9: v2ec9(0x2b) = CONST 
    0x2ecc: CODECOPY v2ec5, v2ec6(0x37ad), v2ec9(0x2b)
    0x2ecd: v2ecd(0x1) = CONST 
    0x2ecf: v2ecf(0x0) = CONST 
    0x2ed2: v2ed2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ee7: v2ee7 = AND v2ed2(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg2
    0x2ee8: v2ee8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2efd: v2efd = AND v2ee8(0xffffffffffffffffffffffffffffffffffffffff), v2ee7
    0x2eff: MSTORE v2ecf(0x0), v2efd
    0x2f00: v2f00(0x20) = CONST 
    0x2f02: v2f02(0x20) = ADD v2f00(0x20), v2ecf(0x0)
    0x2f05: MSTORE v2f02(0x20), v2ecd(0x1)
    0x2f06: v2f06(0x20) = CONST 
    0x2f08: v2f08(0x40) = ADD v2f06(0x20), v2f02(0x20)
    0x2f09: v2f09(0x0) = CONST 
    0x2f0b: v2f0b = SHA3 v2f09(0x0), v2f08(0x40)
    0x2f0c: v2f0c = SLOAD v2f0b
    0x2f0d: v2f0d(0x305e) = CONST 
    0x2f14: v2f14(0xffffffff) = CONST 
    0x2f19: v2f19(0x305e) = AND v2f14(0xffffffff), v2f0d(0x305e)
    0x2f1a: v2f1a_0 = CALLPRIVATE v2f19(0x305e), v2eb6, v2eac_0, v2f0c, v2eb0(0x2f1b)

    Begin block 0x2f1b
    prev=[0x2ead], succ=[0x311eB0x2f1b]
    =================================
    0x2f1c: v2f1c(0x1) = CONST 
    0x2f1e: v2f1e(0x0) = CONST 
    0x2f21: v2f21(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f36: v2f36 = AND v2f21(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg2
    0x2f37: v2f37(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f4c: v2f4c = AND v2f37(0xffffffffffffffffffffffffffffffffffffffff), v2f36
    0x2f4e: MSTORE v2f1e(0x0), v2f4c
    0x2f4f: v2f4f(0x20) = CONST 
    0x2f51: v2f51(0x20) = ADD v2f4f(0x20), v2f1e(0x0)
    0x2f54: MSTORE v2f51(0x20), v2f1c(0x1)
    0x2f55: v2f55(0x20) = CONST 
    0x2f57: v2f57(0x40) = ADD v2f55(0x20), v2f51(0x20)
    0x2f58: v2f58(0x0) = CONST 
    0x2f5a: v2f5a = SHA3 v2f58(0x0), v2f57(0x40)
    0x2f5d: SSTORE v2f5a, v2f1a_0
    0x2f5f: v2f5f(0x2fb0) = CONST 
    0x2f63: v2f63(0x1) = CONST 
    0x2f65: v2f65(0x0) = CONST 
    0x2f68: v2f68(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f7d: v2f7d = AND v2f68(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg1
    0x2f7e: v2f7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2f93: v2f93 = AND v2f7e(0xffffffffffffffffffffffffffffffffffffffff), v2f7d
    0x2f95: MSTORE v2f65(0x0), v2f93
    0x2f96: v2f96(0x20) = CONST 
    0x2f98: v2f98(0x20) = ADD v2f96(0x20), v2f65(0x0)
    0x2f9b: MSTORE v2f98(0x20), v2f63(0x1)
    0x2f9c: v2f9c(0x20) = CONST 
    0x2f9e: v2f9e(0x40) = ADD v2f9c(0x20), v2f98(0x20)
    0x2f9f: v2f9f(0x0) = CONST 
    0x2fa1: v2fa1 = SHA3 v2f9f(0x0), v2f9e(0x40)
    0x2fa2: v2fa2 = SLOAD v2fa1
    0x2fa3: v2fa3(0x311e) = CONST 
    0x2fa9: v2fa9(0xffffffff) = CONST 
    0x2fae: v2fae(0x311e) = AND v2fa9(0xffffffff), v2fa3(0x311e)
    0x2faf: JUMP v2fae(0x311e)

    Begin block 0x311eB0x2f1b
    prev=[0x2f1b], succ=[0x312fB0x2f1b, 0x319cB0x2f1b]
    =================================
    0x311fS0x2f1b: v311fV2f1b(0x0) = CONST 
    0x3124S0x2f1b: v3124V2f1b = ADD v2fa2, v2eac_0
    0x3129S0x2f1b: v3129V2f1b = LT v3124V2f1b, v2fa2
    0x312aS0x2f1b: v312aV2f1b = ISZERO v3129V2f1b
    0x312bS0x2f1b: v312bV2f1b(0x319c) = CONST 
    0x312eS0x2f1b: JUMPI v312bV2f1b(0x319c), v312aV2f1b

    Begin block 0x312fB0x2f1b
    prev=[0x311eB0x2f1b], succ=[]
    =================================
    0x312fS0x2f1b: v312fV2f1b(0x40) = CONST 
    0x3131S0x2f1b: v3131V2f1b = MLOAD v312fV2f1b(0x40)
    0x3132S0x2f1b: v3132V2f1b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3154S0x2f1b: MSTORE v3131V2f1b, v3132V2f1b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3155S0x2f1b: v3155V2f1b(0x4) = CONST 
    0x3157S0x2f1b: v3157V2f1b = ADD v3155V2f1b(0x4), v3131V2f1b
    0x315aS0x2f1b: v315aV2f1b(0x20) = CONST 
    0x315cS0x2f1b: v315cV2f1b = ADD v315aV2f1b(0x20), v3157V2f1b
    0x315fS0x2f1b: v315fV2f1b(0x20) = SUB v315cV2f1b, v3157V2f1b
    0x3161S0x2f1b: MSTORE v3157V2f1b, v315fV2f1b(0x20)
    0x3162S0x2f1b: v3162V2f1b(0x1b) = CONST 
    0x3165S0x2f1b: MSTORE v315cV2f1b, v3162V2f1b(0x1b)
    0x3166S0x2f1b: v3166V2f1b(0x20) = CONST 
    0x3168S0x2f1b: v3168V2f1b = ADD v3166V2f1b(0x20), v315cV2f1b
    0x316aS0x2f1b: v316aV2f1b(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x318cS0x2f1b: MSTORE v3168V2f1b, v316aV2f1b(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x318eS0x2f1b: v318eV2f1b(0x20) = CONST 
    0x3190S0x2f1b: v3190V2f1b = ADD v318eV2f1b(0x20), v3168V2f1b
    0x3194S0x2f1b: v3194V2f1b(0x40) = CONST 
    0x3196S0x2f1b: v3196V2f1b = MLOAD v3194V2f1b(0x40)
    0x3199S0x2f1b: v3199V2f1b(0x64) = SUB v3190V2f1b, v3196V2f1b
    0x319bS0x2f1b: REVERT v3196V2f1b, v3199V2f1b(0x64)

    Begin block 0x319cB0x2f1b
    prev=[0x311eB0x2f1b], succ=[0x2fb0]
    =================================
    0x31a5S0x2f1b: JUMP v2f5f(0x2fb0)

    Begin block 0x2fb0
    prev=[0x319cB0x2f1b], succ=[]
    =================================
    0x2fb1: v2fb1(0x1) = CONST 
    0x2fb3: v2fb3(0x0) = CONST 
    0x2fb6: v2fb6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fcb: v2fcb = AND v2fb6(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg1
    0x2fcc: v2fcc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fe1: v2fe1 = AND v2fcc(0xffffffffffffffffffffffffffffffffffffffff), v2fcb
    0x2fe3: MSTORE v2fb3(0x0), v2fe1
    0x2fe4: v2fe4(0x20) = CONST 
    0x2fe6: v2fe6(0x20) = ADD v2fe4(0x20), v2fb3(0x0)
    0x2fe9: MSTORE v2fe6(0x20), v2fb1(0x1)
    0x2fea: v2fea(0x20) = CONST 
    0x2fec: v2fec(0x40) = ADD v2fea(0x20), v2fe6(0x20)
    0x2fed: v2fed(0x0) = CONST 
    0x2fef: v2fef = SHA3 v2fed(0x0), v2fec(0x40)
    0x2ff2: SSTORE v2fef, v3124V2f1b
    0x2ff5: v2ff5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x300a: v300a = AND v2ff5(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg1
    0x300c: v300c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3021: v3021 = AND v300c(0xffffffffffffffffffffffffffffffffffffffff), v2d70arg2
    0x3022: v3022(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x3044: v3044(0x40) = CONST 
    0x3046: v3046 = MLOAD v3044(0x40)
    0x304a: MSTORE v3046, v2d70arg0
    0x304b: v304b(0x20) = CONST 
    0x304d: v304d = ADD v304b(0x20), v3046
    0x3051: v3051(0x40) = CONST 
    0x3053: v3053 = MLOAD v3051(0x40)
    0x3056: v3056(0x20) = SUB v304d, v3053
    0x3058: LOG3 v3053, v3056(0x20), v3022(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v3021, v300a
    0x305d: RETURNPRIVATE v2d70arg3

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x2f1
    prev=[], succ=[0x303, 0x307]
    =================================
    0x2f2: v2f2(0x35d) = CONST 
    0x2f5: v2f5(0x4) = CONST 
    0x2f8: v2f8 = CALLDATASIZE 
    0x2f9: v2f9 = SUB v2f8, v2f5(0x4)
    0x2fa: v2fa(0x60) = CONST 
    0x2fd: v2fd = LT v2f9, v2fa(0x60)
    0x2fe: v2fe = ISZERO v2fd
    0x2ff: v2ff(0x307) = CONST 
    0x302: JUMPI v2ff(0x307), v2fe

    Begin block 0x303
    prev=[0x2f1], succ=[]
    =================================
    0x303: v303(0x0) = CONST 
    0x306: REVERT v303(0x0), v303(0x0)

    Begin block 0x307
    prev=[0x2f1], succ=[0xbeb]
    =================================
    0x309: v309 = ADD v2f5(0x4), v2f9
    0x30d: v30d = CALLDATALOAD v2f5(0x4)
    0x30e: v30e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x323: v323 = AND v30e(0xffffffffffffffffffffffffffffffffffffffff), v30d
    0x325: v325(0x20) = CONST 
    0x327: v327(0x24) = ADD v325(0x20), v2f5(0x4)
    0x32d: v32d = CALLDATALOAD v327(0x24)
    0x32e: v32e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x343: v343 = AND v32e(0xffffffffffffffffffffffffffffffffffffffff), v32d
    0x345: v345(0x20) = CONST 
    0x347: v347(0x44) = ADD v345(0x20), v327(0x24)
    0x34d: v34d = CALLDATALOAD v347(0x44)
    0x34f: v34f(0x20) = CONST 
    0x351: v351(0x64) = ADD v34f(0x20), v347(0x44)
    0x359: v359(0xbeb) = CONST 
    0x35c: JUMP v359(0xbeb)

    Begin block 0xbeb
    prev=[0x307], succ=[0xc41, 0xcae]
    =================================
    0xbec: vbec(0x0) = CONST 
    0xbef: vbef(0x3) = CONST 
    0xbf1: vbf1(0x0) = CONST 
    0xbf4: vbf4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc09: vc09 = AND vbf4(0xffffffffffffffffffffffffffffffffffffffff), v323
    0xc0a: vc0a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc1f: vc1f = AND vc0a(0xffffffffffffffffffffffffffffffffffffffff), vc09
    0xc21: MSTORE vbf1(0x0), vc1f
    0xc22: vc22(0x20) = CONST 
    0xc24: vc24(0x20) = ADD vc22(0x20), vbf1(0x0)
    0xc27: MSTORE vc24(0x20), vbef(0x3)
    0xc28: vc28(0x20) = CONST 
    0xc2a: vc2a(0x40) = ADD vc28(0x20), vc24(0x20)
    0xc2b: vc2b(0x0) = CONST 
    0xc2d: vc2d = SHA3 vc2b(0x0), vc2a(0x40)
    0xc2e: vc2e(0x0) = CONST 
    0xc31: vc31 = SLOAD vc2d
    0xc33: vc33(0x100) = CONST 
    0xc36: vc36(0x1) = EXP vc33(0x100), vc2e(0x0)
    0xc38: vc38 = DIV vc31, vc36(0x1)
    0xc39: vc39(0xff) = CONST 
    0xc3b: vc3b = AND vc39(0xff), vc38
    0xc3c: vc3c = ISZERO vc3b
    0xc3d: vc3d(0xcae) = CONST 
    0xc40: JUMPI vc3d(0xcae), vc3c

    Begin block 0xc41
    prev=[0xbeb], succ=[]
    =================================
    0xc41: vc41(0x40) = CONST 
    0xc43: vc43 = MLOAD vc41(0x40)
    0xc44: vc44(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xc66: MSTORE vc43, vc44(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc67: vc67(0x4) = CONST 
    0xc69: vc69 = ADD vc67(0x4), vc43
    0xc6c: vc6c(0x20) = CONST 
    0xc6e: vc6e = ADD vc6c(0x20), vc69
    0xc71: vc71(0x20) = SUB vc6e, vc69
    0xc73: MSTORE vc69, vc71(0x20)
    0xc74: vc74(0x16) = CONST 
    0xc77: MSTORE vc6e, vc74(0x16)
    0xc78: vc78(0x20) = CONST 
    0xc7a: vc7a = ADD vc78(0x20), vc6e
    0xc7c: vc7c(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xc9e: MSTORE vc7a, vc7c(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xca0: vca0(0x20) = CONST 
    0xca2: vca2 = ADD vca0(0x20), vc7a
    0xca6: vca6(0x40) = CONST 
    0xca8: vca8 = MLOAD vca6(0x40)
    0xcab: vcab(0x64) = SUB vca2, vca8
    0xcad: REVERT vca8, vcab(0x64)

    Begin block 0xcae
    prev=[0xbeb], succ=[0xd02, 0xd6f]
    =================================
    0xcaf: vcaf = CALLER 
    0xcb0: vcb0(0x3) = CONST 
    0xcb2: vcb2(0x0) = CONST 
    0xcb5: vcb5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcca: vcca = AND vcb5(0xffffffffffffffffffffffffffffffffffffffff), vcaf
    0xccb: vccb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xce0: vce0 = AND vccb(0xffffffffffffffffffffffffffffffffffffffff), vcca
    0xce2: MSTORE vcb2(0x0), vce0
    0xce3: vce3(0x20) = CONST 
    0xce5: vce5(0x20) = ADD vce3(0x20), vcb2(0x0)
    0xce8: MSTORE vce5(0x20), vcb0(0x3)
    0xce9: vce9(0x20) = CONST 
    0xceb: vceb(0x40) = ADD vce9(0x20), vce5(0x20)
    0xcec: vcec(0x0) = CONST 
    0xcee: vcee = SHA3 vcec(0x0), vceb(0x40)
    0xcef: vcef(0x0) = CONST 
    0xcf2: vcf2 = SLOAD vcee
    0xcf4: vcf4(0x100) = CONST 
    0xcf7: vcf7(0x1) = EXP vcf4(0x100), vcef(0x0)
    0xcf9: vcf9 = DIV vcf2, vcf7(0x1)
    0xcfa: vcfa(0xff) = CONST 
    0xcfc: vcfc = AND vcfa(0xff), vcf9
    0xcfd: vcfd = ISZERO vcfc
    0xcfe: vcfe(0xd6f) = CONST 
    0xd01: JUMPI vcfe(0xd6f), vcfd

    Begin block 0xd02
    prev=[0xcae], succ=[]
    =================================
    0xd02: vd02(0x40) = CONST 
    0xd04: vd04 = MLOAD vd02(0x40)
    0xd05: vd05(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xd27: MSTORE vd04, vd05(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd28: vd28(0x4) = CONST 
    0xd2a: vd2a = ADD vd28(0x4), vd04
    0xd2d: vd2d(0x20) = CONST 
    0xd2f: vd2f = ADD vd2d(0x20), vd2a
    0xd32: vd32(0x20) = SUB vd2f, vd2a
    0xd34: MSTORE vd2a, vd32(0x20)
    0xd35: vd35(0x16) = CONST 
    0xd38: MSTORE vd2f, vd35(0x16)
    0xd39: vd39(0x20) = CONST 
    0xd3b: vd3b = ADD vd39(0x20), vd2f
    0xd3d: vd3d(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xd5f: MSTORE vd3b, vd3d(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xd61: vd61(0x20) = CONST 
    0xd63: vd63 = ADD vd61(0x20), vd3b
    0xd67: vd67(0x40) = CONST 
    0xd69: vd69 = MLOAD vd67(0x40)
    0xd6c: vd6c(0x64) = SUB vd63, vd69
    0xd6e: REVERT vd69, vd6c(0x64)

    Begin block 0xd6f
    prev=[0xcae], succ=[0xdc3, 0xe30]
    =================================
    0xd71: vd71(0x3) = CONST 
    0xd73: vd73(0x0) = CONST 
    0xd76: vd76(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd8b: vd8b = AND vd76(0xffffffffffffffffffffffffffffffffffffffff), v343
    0xd8c: vd8c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xda1: vda1 = AND vd8c(0xffffffffffffffffffffffffffffffffffffffff), vd8b
    0xda3: MSTORE vd73(0x0), vda1
    0xda4: vda4(0x20) = CONST 
    0xda6: vda6(0x20) = ADD vda4(0x20), vd73(0x0)
    0xda9: MSTORE vda6(0x20), vd71(0x3)
    0xdaa: vdaa(0x20) = CONST 
    0xdac: vdac(0x40) = ADD vdaa(0x20), vda6(0x20)
    0xdad: vdad(0x0) = CONST 
    0xdaf: vdaf = SHA3 vdad(0x0), vdac(0x40)
    0xdb0: vdb0(0x0) = CONST 
    0xdb3: vdb3 = SLOAD vdaf
    0xdb5: vdb5(0x100) = CONST 
    0xdb8: vdb8(0x1) = EXP vdb5(0x100), vdb0(0x0)
    0xdba: vdba = DIV vdb3, vdb8(0x1)
    0xdbb: vdbb(0xff) = CONST 
    0xdbd: vdbd = AND vdbb(0xff), vdba
    0xdbe: vdbe = ISZERO vdbd
    0xdbf: vdbf(0xe30) = CONST 
    0xdc2: JUMPI vdbf(0xe30), vdbe

    Begin block 0xdc3
    prev=[0xd6f], succ=[]
    =================================
    0xdc3: vdc3(0x40) = CONST 
    0xdc5: vdc5 = MLOAD vdc3(0x40)
    0xdc6: vdc6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xde8: MSTORE vdc5, vdc6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xde9: vde9(0x4) = CONST 
    0xdeb: vdeb = ADD vde9(0x4), vdc5
    0xdee: vdee(0x20) = CONST 
    0xdf0: vdf0 = ADD vdee(0x20), vdeb
    0xdf3: vdf3(0x20) = SUB vdf0, vdeb
    0xdf5: MSTORE vdeb, vdf3(0x20)
    0xdf6: vdf6(0x16) = CONST 
    0xdf9: MSTORE vdf0, vdf6(0x16)
    0xdfa: vdfa(0x20) = CONST 
    0xdfc: vdfc = ADD vdfa(0x20), vdf0
    0xdfe: vdfe(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xe20: MSTORE vdfc, vdfe(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xe22: ve22(0x20) = CONST 
    0xe24: ve24 = ADD ve22(0x20), vdfc
    0xe28: ve28(0x40) = CONST 
    0xe2a: ve2a = MLOAD ve28(0x40)
    0xe2d: ve2d(0x64) = SUB ve24, ve2a
    0xe2f: REVERT ve2a, ve2d(0x64)

    Begin block 0xe30
    prev=[0xd6f], succ=[0xe4c, 0xeb9]
    =================================
    0xe31: ve31(0x0) = CONST 
    0xe33: ve33(0x1) = ISZERO ve31(0x0)
    0xe34: ve34(0x0) = ISZERO ve33(0x1)
    0xe35: ve35(0x6) = CONST 
    0xe37: ve37(0x14) = CONST 
    0xe3a: ve3a = SLOAD ve35(0x6)
    0xe3c: ve3c(0x100) = CONST 
    0xe3f: ve3f(0x10000000000000000000000000000000000000000) = EXP ve3c(0x100), ve37(0x14)
    0xe41: ve41 = DIV ve3a, ve3f(0x10000000000000000000000000000000000000000)
    0xe42: ve42(0xff) = CONST 
    0xe44: ve44 = AND ve42(0xff), ve41
    0xe45: ve45 = ISZERO ve44
    0xe46: ve46 = ISZERO ve45
    0xe47: ve47 = EQ ve46, ve34(0x0)
    0xe48: ve48(0xeb9) = CONST 
    0xe4b: JUMPI ve48(0xeb9), ve47

    Begin block 0xe4c
    prev=[0xe30], succ=[]
    =================================
    0xe4c: ve4c(0x40) = CONST 
    0xe4e: ve4e = MLOAD ve4c(0x40)
    0xe4f: ve4f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xe71: MSTORE ve4e, ve4f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe72: ve72(0x4) = CONST 
    0xe74: ve74 = ADD ve72(0x4), ve4e
    0xe77: ve77(0x20) = CONST 
    0xe79: ve79 = ADD ve77(0x20), ve74
    0xe7c: ve7c(0x20) = SUB ve79, ve74
    0xe7e: MSTORE ve74, ve7c(0x20)
    0xe7f: ve7f(0x16) = CONST 
    0xe82: MSTORE ve79, ve7f(0x16)
    0xe83: ve83(0x20) = CONST 
    0xe85: ve85 = ADD ve83(0x20), ve79
    0xe87: ve87(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0xea9: MSTORE ve85, ve87(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0xeab: veab(0x20) = CONST 
    0xead: vead = ADD veab(0x20), ve85
    0xeb1: veb1(0x40) = CONST 
    0xeb3: veb3 = MLOAD veb1(0x40)
    0xeb6: veb6(0x64) = SUB vead, veb3
    0xeb8: REVERT veb3, veb6(0x64)

    Begin block 0xeb9
    prev=[0xe30], succ=[0x2d68B0xeb9]
    =================================
    0xeba: veba(0x0) = CONST 
    0xebc: vebc(0xecc) = CONST 
    0xec0: vec0(0xec7) = CONST 
    0xec3: vec3(0x2d68) = CONST 
    0xec6: JUMP vec3(0x2d68)

    Begin block 0x2d68B0xeb9
    prev=[0xeb9], succ=[0xec7]
    =================================
    0x2d69S0xeb9: v2d69Veb9(0x0) = CONST 
    0x2d6bS0xeb9: v2d6bVeb9 = CALLER 
    0x2d6fS0xeb9: JUMP vec0(0xec7)

    Begin block 0xec7
    prev=[0x2d68B0xeb9], succ=[0xecc]
    =================================
    0xec8: vec8(0x2540) = CONST 
    0xecb: vecb_0 = CALLPRIVATE vec8(0x2540), v2d6bVeb9, v323, vebc(0xecc)

    Begin block 0xecc
    prev=[0xec7], succ=[0xed9]
    =================================
    0xecf: vecf(0xed9) = CONST 
    0xed5: ved5(0x2d70) = CONST 
    0xed8: CALLPRIVATE ved5(0x2d70), v34d, v343, v323, vecf(0xed9)

    Begin block 0xed9
    prev=[0xecc], succ=[0x2d68B0xed9]
    =================================
    0xeda: veda(0xf17) = CONST 
    0xede: vede(0xee5) = CONST 
    0xee1: vee1(0x2d68) = CONST 
    0xee4: JUMP vee1(0x2d68)

    Begin block 0x2d68B0xed9
    prev=[0xed9], succ=[0xee5]
    =================================
    0x2d69S0xed9: v2d69Ved9(0x0) = CONST 
    0x2d6bS0xed9: v2d6bVed9 = CALLER 
    0x2d6fS0xed9: JUMP vede(0xee5)

    Begin block 0xee5
    prev=[0x2d68B0xed9], succ=[0xf12]
    =================================
    0xee6: vee6(0xf12) = CONST 
    0xeea: veea(0x40) = CONST 
    0xeec: veec = MLOAD veea(0x40)
    0xeee: veee(0x60) = CONST 
    0xef0: vef0 = ADD veee(0x60), veec
    0xef1: vef1(0x40) = CONST 
    0xef3: MSTORE vef1(0x40), vef0
    0xef5: vef5(0x28) = CONST 
    0xef8: MSTORE veec, vef5(0x28)
    0xef9: vef9(0x20) = CONST 
    0xefb: vefb = ADD vef9(0x20), veec
    0xefc: vefc(0x386a) = CONST 
    0xeff: veff(0x28) = CONST 
    0xf02: CODECOPY vefb, vefc(0x386a), veff(0x28)
    0xf04: vf04(0x305e) = CONST 
    0xf0b: vf0b(0xffffffff) = CONST 
    0xf10: vf10(0x305e) = AND vf0b(0xffffffff), vf04(0x305e)
    0xf11: vf11_0 = CALLPRIVATE vf10(0x305e), veec, v34d, vecb_0, vee6(0xf12)

    Begin block 0xf12
    prev=[0xee5], succ=[0xf17]
    =================================
    0xf13: vf13(0x29e6) = CONST 
    0xf16: CALLPRIVATE vf13(0x29e6), vf11_0, v2d6bVed9, v323, veda(0xf17)

    Begin block 0xf17
    prev=[0xf12], succ=[0x35d]
    =================================
    0xf18: vf18(0x1) = CONST 
    0xf25: JUMP v2f2(0x35d)

    Begin block 0x35d
    prev=[0xf17], succ=[]
    =================================
    0x35e: v35e(0x40) = CONST 
    0x360: v360 = MLOAD v35e(0x40)
    0x363: v363 = ISZERO vf18(0x1)
    0x364: v364 = ISZERO v363
    0x366: MSTORE v360, v364
    0x367: v367(0x20) = CONST 
    0x369: v369 = ADD v367(0x20), v360
    0x36d: v36d(0x40) = CONST 
    0x36f: v36f = MLOAD v36d(0x40)
    0x372: v372(0x20) = SUB v369, v36f
    0x374: RETURN v36f, v372(0x20)

}

function 0x305e(0x305earg0x0, 0x305earg0x1, 0x305earg0x2, 0x305earg0x3) private {
    Begin block 0x305e
    prev=[], succ=[0x306b, 0x310b]
    =================================
    0x305f: v305f(0x0) = CONST 
    0x3063: v3063 = GT v305earg1, v305earg2
    0x3064: v3064 = ISZERO v3063
    0x3067: v3067(0x310b) = CONST 
    0x306a: JUMPI v3067(0x310b), v3064

    Begin block 0x306b
    prev=[0x305e], succ=[0x30b5]
    =================================
    0x306b: v306b(0x40) = CONST 
    0x306d: v306d = MLOAD v306b(0x40)
    0x306e: v306e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3090: MSTORE v306d, v306e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3091: v3091(0x4) = CONST 
    0x3093: v3093 = ADD v3091(0x4), v306d
    0x3096: v3096(0x20) = CONST 
    0x3098: v3098 = ADD v3096(0x20), v3093
    0x309b: v309b(0x20) = SUB v3098, v3093
    0x309d: MSTORE v3093, v309b(0x20)
    0x30a1: v30a1 = MLOAD v305earg0
    0x30a3: MSTORE v3098, v30a1
    0x30a4: v30a4(0x20) = CONST 
    0x30a6: v30a6 = ADD v30a4(0x20), v3098
    0x30aa: v30aa = MLOAD v305earg0
    0x30ac: v30ac(0x20) = CONST 
    0x30ae: v30ae = ADD v30ac(0x20), v305earg0
    0x30b3: v30b3(0x0) = CONST 

    Begin block 0x30b5
    prev=[0x306b, 0x30be], succ=[0x30d0, 0x30be]
    =================================
    0x30b5_0x0: v30b5_0 = PHI v30b3(0x0), v30c9
    0x30b8: v30b8 = LT v30b5_0, v30aa
    0x30b9: v30b9 = ISZERO v30b8
    0x30ba: v30ba(0x30d0) = CONST 
    0x30bd: JUMPI v30ba(0x30d0), v30b9

    Begin block 0x30d0
    prev=[0x30b5], succ=[0x30fd, 0x30e4]
    =================================
    0x30d9: v30d9 = ADD v30aa, v30a6
    0x30db: v30db(0x1f) = CONST 
    0x30dd: v30dd = AND v30db(0x1f), v30aa
    0x30df: v30df = ISZERO v30dd
    0x30e0: v30e0(0x30fd) = CONST 
    0x30e3: JUMPI v30e0(0x30fd), v30df

    Begin block 0x30fd
    prev=[0x30d0, 0x30e4], succ=[]
    =================================
    0x30fd_0x1: v30fd_1 = PHI v30d9, v30fa
    0x3103: v3103(0x40) = CONST 
    0x3105: v3105 = MLOAD v3103(0x40)
    0x3108: v3108 = SUB v30fd_1, v3105
    0x310a: REVERT v3105, v3108

    Begin block 0x30e4
    prev=[0x30d0], succ=[0x30fd]
    =================================
    0x30e6: v30e6 = SUB v30d9, v30dd
    0x30e8: v30e8 = MLOAD v30e6
    0x30e9: v30e9(0x1) = CONST 
    0x30ec: v30ec(0x20) = CONST 
    0x30ee: v30ee = SUB v30ec(0x20), v30dd
    0x30ef: v30ef(0x100) = CONST 
    0x30f2: v30f2 = EXP v30ef(0x100), v30ee
    0x30f3: v30f3 = SUB v30f2, v30e9(0x1)
    0x30f4: v30f4 = NOT v30f3
    0x30f5: v30f5 = AND v30f4, v30e8
    0x30f7: MSTORE v30e6, v30f5
    0x30f8: v30f8(0x20) = CONST 
    0x30fa: v30fa = ADD v30f8(0x20), v30e6

    Begin block 0x30be
    prev=[0x30b5], succ=[0x30b5]
    =================================
    0x30be_0x0: v30be_0 = PHI v30b3(0x0), v30c9
    0x30c0: v30c0 = ADD v30ae, v30be_0
    0x30c1: v30c1 = MLOAD v30c0
    0x30c4: v30c4 = ADD v30a6, v30be_0
    0x30c5: MSTORE v30c4, v30c1
    0x30c6: v30c6(0x20) = CONST 
    0x30c9: v30c9 = ADD v30be_0, v30c6(0x20)
    0x30cc: v30cc(0x30b5) = CONST 
    0x30cf: JUMP v30cc(0x30b5)

    Begin block 0x310b
    prev=[0x305e], succ=[]
    =================================
    0x310d: v310d(0x0) = CONST 
    0x3111: v3111 = SUB v305earg2, v305earg1
    0x311d: RETURNPRIVATE v305earg3, v3111

}

function decimals()() public {
    Begin block 0x375
    prev=[], succ=[0xf26]
    =================================
    0x376: v376(0x37d) = CONST 
    0x379: v379(0xf26) = CONST 
    0x37c: JUMP v379(0xf26)

    Begin block 0xf26
    prev=[0x375], succ=[0x37d]
    =================================
    0xf27: vf27(0x12) = CONST 
    0xf2a: JUMP v376(0x37d)

    Begin block 0x37d
    prev=[0xf26], succ=[]
    =================================
    0x37e: v37e(0x40) = CONST 
    0x380: v380 = MLOAD v37e(0x40)
    0x383: v383(0xff) = CONST 
    0x385: v385(0x12) = AND v383(0xff), vf27(0x12)
    0x387: MSTORE v380, v385(0x12)
    0x388: v388(0x20) = CONST 
    0x38a: v38a = ADD v388(0x20), v380
    0x38e: v38e(0x40) = CONST 
    0x390: v390 = MLOAD v38e(0x40)
    0x393: v393(0x20) = SUB v38a, v390
    0x395: RETURN v390, v393(0x20)

}

function increaseAllowance(address,uint256)() public {
    Begin block 0x396
    prev=[], succ=[0x3a8, 0x3ac]
    =================================
    0x397: v397(0x3e2) = CONST 
    0x39a: v39a(0x4) = CONST 
    0x39d: v39d = CALLDATASIZE 
    0x39e: v39e = SUB v39d, v39a(0x4)
    0x39f: v39f(0x40) = CONST 
    0x3a2: v3a2 = LT v39e, v39f(0x40)
    0x3a3: v3a3 = ISZERO v3a2
    0x3a4: v3a4(0x3ac) = CONST 
    0x3a7: JUMPI v3a4(0x3ac), v3a3

    Begin block 0x3a8
    prev=[0x396], succ=[]
    =================================
    0x3a8: v3a8(0x0) = CONST 
    0x3ab: REVERT v3a8(0x0), v3a8(0x0)

    Begin block 0x3ac
    prev=[0x396], succ=[0xf2b]
    =================================
    0x3ae: v3ae = ADD v39a(0x4), v39e
    0x3b2: v3b2 = CALLDATALOAD v39a(0x4)
    0x3b3: v3b3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c8: v3c8 = AND v3b3(0xffffffffffffffffffffffffffffffffffffffff), v3b2
    0x3ca: v3ca(0x20) = CONST 
    0x3cc: v3cc(0x24) = ADD v3ca(0x20), v39a(0x4)
    0x3d2: v3d2 = CALLDATALOAD v3cc(0x24)
    0x3d4: v3d4(0x20) = CONST 
    0x3d6: v3d6(0x44) = ADD v3d4(0x20), v3cc(0x24)
    0x3de: v3de(0xf2b) = CONST 
    0x3e1: JUMP v3de(0xf2b)

    Begin block 0xf2b
    prev=[0x3ac], succ=[0xf81, 0xfee]
    =================================
    0xf2c: vf2c(0x0) = CONST 
    0xf2f: vf2f(0x3) = CONST 
    0xf31: vf31(0x0) = CONST 
    0xf34: vf34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf49: vf49 = AND vf34(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0xf4a: vf4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf5f: vf5f = AND vf4a(0xffffffffffffffffffffffffffffffffffffffff), vf49
    0xf61: MSTORE vf31(0x0), vf5f
    0xf62: vf62(0x20) = CONST 
    0xf64: vf64(0x20) = ADD vf62(0x20), vf31(0x0)
    0xf67: MSTORE vf64(0x20), vf2f(0x3)
    0xf68: vf68(0x20) = CONST 
    0xf6a: vf6a(0x40) = ADD vf68(0x20), vf64(0x20)
    0xf6b: vf6b(0x0) = CONST 
    0xf6d: vf6d = SHA3 vf6b(0x0), vf6a(0x40)
    0xf6e: vf6e(0x0) = CONST 
    0xf71: vf71 = SLOAD vf6d
    0xf73: vf73(0x100) = CONST 
    0xf76: vf76(0x1) = EXP vf73(0x100), vf6e(0x0)
    0xf78: vf78 = DIV vf71, vf76(0x1)
    0xf79: vf79(0xff) = CONST 
    0xf7b: vf7b = AND vf79(0xff), vf78
    0xf7c: vf7c = ISZERO vf7b
    0xf7d: vf7d(0xfee) = CONST 
    0xf80: JUMPI vf7d(0xfee), vf7c

    Begin block 0xf81
    prev=[0xf2b], succ=[]
    =================================
    0xf81: vf81(0x40) = CONST 
    0xf83: vf83 = MLOAD vf81(0x40)
    0xf84: vf84(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xfa6: MSTORE vf83, vf84(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xfa7: vfa7(0x4) = CONST 
    0xfa9: vfa9 = ADD vfa7(0x4), vf83
    0xfac: vfac(0x20) = CONST 
    0xfae: vfae = ADD vfac(0x20), vfa9
    0xfb1: vfb1(0x20) = SUB vfae, vfa9
    0xfb3: MSTORE vfa9, vfb1(0x20)
    0xfb4: vfb4(0x16) = CONST 
    0xfb7: MSTORE vfae, vfb4(0x16)
    0xfb8: vfb8(0x20) = CONST 
    0xfba: vfba = ADD vfb8(0x20), vfae
    0xfbc: vfbc(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0xfde: MSTORE vfba, vfbc(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0xfe0: vfe0(0x20) = CONST 
    0xfe2: vfe2 = ADD vfe0(0x20), vfba
    0xfe6: vfe6(0x40) = CONST 
    0xfe8: vfe8 = MLOAD vfe6(0x40)
    0xfeb: vfeb(0x64) = SUB vfe2, vfe8
    0xfed: REVERT vfe8, vfeb(0x64)

    Begin block 0xfee
    prev=[0xf2b], succ=[0x1042, 0x10af]
    =================================
    0xfef: vfef = CALLER 
    0xff0: vff0(0x3) = CONST 
    0xff2: vff2(0x0) = CONST 
    0xff5: vff5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x100a: v100a = AND vff5(0xffffffffffffffffffffffffffffffffffffffff), vfef
    0x100b: v100b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1020: v1020 = AND v100b(0xffffffffffffffffffffffffffffffffffffffff), v100a
    0x1022: MSTORE vff2(0x0), v1020
    0x1023: v1023(0x20) = CONST 
    0x1025: v1025(0x20) = ADD v1023(0x20), vff2(0x0)
    0x1028: MSTORE v1025(0x20), vff0(0x3)
    0x1029: v1029(0x20) = CONST 
    0x102b: v102b(0x40) = ADD v1029(0x20), v1025(0x20)
    0x102c: v102c(0x0) = CONST 
    0x102e: v102e = SHA3 v102c(0x0), v102b(0x40)
    0x102f: v102f(0x0) = CONST 
    0x1032: v1032 = SLOAD v102e
    0x1034: v1034(0x100) = CONST 
    0x1037: v1037(0x1) = EXP v1034(0x100), v102f(0x0)
    0x1039: v1039 = DIV v1032, v1037(0x1)
    0x103a: v103a(0xff) = CONST 
    0x103c: v103c = AND v103a(0xff), v1039
    0x103d: v103d = ISZERO v103c
    0x103e: v103e(0x10af) = CONST 
    0x1041: JUMPI v103e(0x10af), v103d

    Begin block 0x1042
    prev=[0xfee], succ=[]
    =================================
    0x1042: v1042(0x40) = CONST 
    0x1044: v1044 = MLOAD v1042(0x40)
    0x1045: v1045(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1067: MSTORE v1044, v1045(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1068: v1068(0x4) = CONST 
    0x106a: v106a = ADD v1068(0x4), v1044
    0x106d: v106d(0x20) = CONST 
    0x106f: v106f = ADD v106d(0x20), v106a
    0x1072: v1072(0x20) = SUB v106f, v106a
    0x1074: MSTORE v106a, v1072(0x20)
    0x1075: v1075(0x16) = CONST 
    0x1078: MSTORE v106f, v1075(0x16)
    0x1079: v1079(0x20) = CONST 
    0x107b: v107b = ADD v1079(0x20), v106f
    0x107d: v107d(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0x109f: MSTORE v107b, v107d(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0x10a1: v10a1(0x20) = CONST 
    0x10a3: v10a3 = ADD v10a1(0x20), v107b
    0x10a7: v10a7(0x40) = CONST 
    0x10a9: v10a9 = MLOAD v10a7(0x40)
    0x10ac: v10ac(0x64) = SUB v10a3, v10a9
    0x10ae: REVERT v10a9, v10ac(0x64)

    Begin block 0x10af
    prev=[0xfee], succ=[0x10cb, 0x1138]
    =================================
    0x10b0: v10b0(0x0) = CONST 
    0x10b2: v10b2(0x1) = ISZERO v10b0(0x0)
    0x10b3: v10b3(0x0) = ISZERO v10b2(0x1)
    0x10b4: v10b4(0x6) = CONST 
    0x10b6: v10b6(0x14) = CONST 
    0x10b9: v10b9 = SLOAD v10b4(0x6)
    0x10bb: v10bb(0x100) = CONST 
    0x10be: v10be(0x10000000000000000000000000000000000000000) = EXP v10bb(0x100), v10b6(0x14)
    0x10c0: v10c0 = DIV v10b9, v10be(0x10000000000000000000000000000000000000000)
    0x10c1: v10c1(0xff) = CONST 
    0x10c3: v10c3 = AND v10c1(0xff), v10c0
    0x10c4: v10c4 = ISZERO v10c3
    0x10c5: v10c5 = ISZERO v10c4
    0x10c6: v10c6 = EQ v10c5, v10b3(0x0)
    0x10c7: v10c7(0x1138) = CONST 
    0x10ca: JUMPI v10c7(0x1138), v10c6

    Begin block 0x10cb
    prev=[0x10af], succ=[]
    =================================
    0x10cb: v10cb(0x40) = CONST 
    0x10cd: v10cd = MLOAD v10cb(0x40)
    0x10ce: v10ce(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x10f0: MSTORE v10cd, v10ce(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10f1: v10f1(0x4) = CONST 
    0x10f3: v10f3 = ADD v10f1(0x4), v10cd
    0x10f6: v10f6(0x20) = CONST 
    0x10f8: v10f8 = ADD v10f6(0x20), v10f3
    0x10fb: v10fb(0x20) = SUB v10f8, v10f3
    0x10fd: MSTORE v10f3, v10fb(0x20)
    0x10fe: v10fe(0x16) = CONST 
    0x1101: MSTORE v10f8, v10fe(0x16)
    0x1102: v1102(0x20) = CONST 
    0x1104: v1104 = ADD v1102(0x20), v10f8
    0x1106: v1106(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x1128: MSTORE v1104, v1106(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x112a: v112a(0x20) = CONST 
    0x112c: v112c = ADD v112a(0x20), v1104
    0x1130: v1130(0x40) = CONST 
    0x1132: v1132 = MLOAD v1130(0x40)
    0x1135: v1135(0x64) = SUB v112c, v1132
    0x1137: REVERT v1132, v1135(0x64)

    Begin block 0x1138
    prev=[0x10af], succ=[0x2d68B0x1138]
    =================================
    0x1139: v1139(0x0) = CONST 
    0x113b: v113b(0x114b) = CONST 
    0x113e: v113e(0x1145) = CONST 
    0x1141: v1141(0x2d68) = CONST 
    0x1144: JUMP v1141(0x2d68)

    Begin block 0x2d68B0x1138
    prev=[0x1138], succ=[0x1145]
    =================================
    0x2d69S0x1138: v2d69V1138(0x0) = CONST 
    0x2d6bS0x1138: v2d6bV1138 = CALLER 
    0x2d6fS0x1138: JUMP v113e(0x1145)

    Begin block 0x1145
    prev=[0x2d68B0x1138], succ=[0x114b]
    =================================
    0x1147: v1147(0x2540) = CONST 
    0x114a: v114a_0 = CALLPRIVATE v1147(0x2540), v3c8, v2d6bV1138, v113b(0x114b)

    Begin block 0x114b
    prev=[0x1145], succ=[0x2d68B0x114b]
    =================================
    0x114e: v114e(0x1171) = CONST 
    0x1151: v1151(0x1158) = CONST 
    0x1154: v1154(0x2d68) = CONST 
    0x1157: JUMP v1154(0x2d68)

    Begin block 0x2d68B0x114b
    prev=[0x114b], succ=[0x1158]
    =================================
    0x2d69S0x114b: v2d69V114b(0x0) = CONST 
    0x2d6bS0x114b: v2d6bV114b = CALLER 
    0x2d6fS0x114b: JUMP v1151(0x1158)

    Begin block 0x1158
    prev=[0x2d68B0x114b], succ=[0x311eB0x1158]
    =================================
    0x115a: v115a(0x116c) = CONST 
    0x115f: v115f(0x311e) = CONST 
    0x1165: v1165(0xffffffff) = CONST 
    0x116a: v116a(0x311e) = AND v1165(0xffffffff), v115f(0x311e)
    0x116b: JUMP v116a(0x311e)

    Begin block 0x311eB0x1158
    prev=[0x1158], succ=[0x312fB0x1158, 0x319cB0x1158]
    =================================
    0x311fS0x1158: v311fV1158(0x0) = CONST 
    0x3124S0x1158: v3124V1158 = ADD v114a_0, v3d2
    0x3129S0x1158: v3129V1158 = LT v3124V1158, v114a_0
    0x312aS0x1158: v312aV1158 = ISZERO v3129V1158
    0x312bS0x1158: v312bV1158(0x319c) = CONST 
    0x312eS0x1158: JUMPI v312bV1158(0x319c), v312aV1158

    Begin block 0x312fB0x1158
    prev=[0x311eB0x1158], succ=[]
    =================================
    0x312fS0x1158: v312fV1158(0x40) = CONST 
    0x3131S0x1158: v3131V1158 = MLOAD v312fV1158(0x40)
    0x3132S0x1158: v3132V1158(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3154S0x1158: MSTORE v3131V1158, v3132V1158(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3155S0x1158: v3155V1158(0x4) = CONST 
    0x3157S0x1158: v3157V1158 = ADD v3155V1158(0x4), v3131V1158
    0x315aS0x1158: v315aV1158(0x20) = CONST 
    0x315cS0x1158: v315cV1158 = ADD v315aV1158(0x20), v3157V1158
    0x315fS0x1158: v315fV1158(0x20) = SUB v315cV1158, v3157V1158
    0x3161S0x1158: MSTORE v3157V1158, v315fV1158(0x20)
    0x3162S0x1158: v3162V1158(0x1b) = CONST 
    0x3165S0x1158: MSTORE v315cV1158, v3162V1158(0x1b)
    0x3166S0x1158: v3166V1158(0x20) = CONST 
    0x3168S0x1158: v3168V1158 = ADD v3166V1158(0x20), v315cV1158
    0x316aS0x1158: v316aV1158(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x318cS0x1158: MSTORE v3168V1158, v316aV1158(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x318eS0x1158: v318eV1158(0x20) = CONST 
    0x3190S0x1158: v3190V1158 = ADD v318eV1158(0x20), v3168V1158
    0x3194S0x1158: v3194V1158(0x40) = CONST 
    0x3196S0x1158: v3196V1158 = MLOAD v3194V1158(0x40)
    0x3199S0x1158: v3199V1158(0x64) = SUB v3190V1158, v3196V1158
    0x319bS0x1158: REVERT v3196V1158, v3199V1158(0x64)

    Begin block 0x319cB0x1158
    prev=[0x311eB0x1158], succ=[0x116c]
    =================================
    0x31a5S0x1158: JUMP v115a(0x116c)

    Begin block 0x116c
    prev=[0x319cB0x1158], succ=[0x1171]
    =================================
    0x116d: v116d(0x29e6) = CONST 
    0x1170: CALLPRIVATE v116d(0x29e6), v3124V1158, v3c8, v2d6bV114b, v114e(0x1171)

    Begin block 0x1171
    prev=[0x116c], succ=[0x3e2]
    =================================
    0x1172: v1172(0x1) = CONST 
    0x117d: JUMP v397(0x3e2)

    Begin block 0x3e2
    prev=[0x1171], succ=[]
    =================================
    0x3e3: v3e3(0x40) = CONST 
    0x3e5: v3e5 = MLOAD v3e3(0x40)
    0x3e8: v3e8 = ISZERO v1172(0x1)
    0x3e9: v3e9 = ISZERO v3e8
    0x3eb: MSTORE v3e5, v3e9
    0x3ec: v3ec(0x20) = CONST 
    0x3ee: v3ee = ADD v3ec(0x20), v3e5
    0x3f2: v3f2(0x40) = CONST 
    0x3f4: v3f4 = MLOAD v3f2(0x40)
    0x3f7: v3f7(0x20) = SUB v3ee, v3f4
    0x3f9: RETURN v3f4, v3f7(0x20)

}

function fallback()() public {
    Begin block 0x3a17
    prev=[], succ=[]
    =================================
    0x3a18: v3a18(0x0) = CONST 
    0x3a1b: REVERT v3a18(0x0), v3a18(0x0)

}

function RemoveFromBlacklist(address)() public {
    Begin block 0x3fa
    prev=[], succ=[0x40c, 0x410]
    =================================
    0x3fb: v3fb(0x43c) = CONST 
    0x3fe: v3fe(0x4) = CONST 
    0x401: v401 = CALLDATASIZE 
    0x402: v402 = SUB v401, v3fe(0x4)
    0x403: v403(0x20) = CONST 
    0x406: v406 = LT v402, v403(0x20)
    0x407: v407 = ISZERO v406
    0x408: v408(0x410) = CONST 
    0x40b: JUMPI v408(0x410), v407

    Begin block 0x40c
    prev=[0x3fa], succ=[]
    =================================
    0x40c: v40c(0x0) = CONST 
    0x40f: REVERT v40c(0x0), v40c(0x0)

    Begin block 0x410
    prev=[0x3fa], succ=[0x117e]
    =================================
    0x412: v412 = ADD v3fe(0x4), v402
    0x416: v416 = CALLDATALOAD v3fe(0x4)
    0x417: v417(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42c: v42c = AND v417(0xffffffffffffffffffffffffffffffffffffffff), v416
    0x42e: v42e(0x20) = CONST 
    0x430: v430(0x24) = ADD v42e(0x20), v3fe(0x4)
    0x438: v438(0x117e) = CONST 
    0x43b: JUMP v438(0x117e)

    Begin block 0x117e
    prev=[0x410], succ=[0x11d4, 0x1241]
    =================================
    0x117f: v117f(0x6) = CONST 
    0x1181: v1181(0x0) = CONST 
    0x1184: v1184 = SLOAD v117f(0x6)
    0x1186: v1186(0x100) = CONST 
    0x1189: v1189(0x1) = EXP v1186(0x100), v1181(0x0)
    0x118b: v118b = DIV v1184, v1189(0x1)
    0x118c: v118c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11a1: v11a1 = AND v118c(0xffffffffffffffffffffffffffffffffffffffff), v118b
    0x11a2: v11a2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11b7: v11b7 = AND v11a2(0xffffffffffffffffffffffffffffffffffffffff), v11a1
    0x11b8: v11b8 = CALLER 
    0x11b9: v11b9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11ce: v11ce = AND v11b9(0xffffffffffffffffffffffffffffffffffffffff), v11b8
    0x11cf: v11cf = EQ v11ce, v11b7
    0x11d0: v11d0(0x1241) = CONST 
    0x11d3: JUMPI v11d0(0x1241), v11cf

    Begin block 0x11d4
    prev=[0x117e], succ=[]
    =================================
    0x11d4: v11d4(0x40) = CONST 
    0x11d6: v11d6 = MLOAD v11d4(0x40)
    0x11d7: v11d7(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11f9: MSTORE v11d6, v11d7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11fa: v11fa(0x4) = CONST 
    0x11fc: v11fc = ADD v11fa(0x4), v11d6
    0x11ff: v11ff(0x20) = CONST 
    0x1201: v1201 = ADD v11ff(0x20), v11fc
    0x1204: v1204(0x20) = SUB v1201, v11fc
    0x1206: MSTORE v11fc, v1204(0x20)
    0x1207: v1207(0x15) = CONST 
    0x120a: MSTORE v1201, v1207(0x15)
    0x120b: v120b(0x20) = CONST 
    0x120d: v120d = ADD v120b(0x20), v1201
    0x120f: v120f(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x1231: MSTORE v120d, v120f(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x1233: v1233(0x20) = CONST 
    0x1235: v1235 = ADD v1233(0x20), v120d
    0x1239: v1239(0x40) = CONST 
    0x123b: v123b = MLOAD v1239(0x40)
    0x123e: v123e(0x64) = SUB v1235, v123b
    0x1240: REVERT v123b, v123e(0x64)

    Begin block 0x1241
    prev=[0x117e], succ=[0x43c]
    =================================
    0x1242: v1242(0x0) = CONST 
    0x1244: v1244(0x3) = CONST 
    0x1246: v1246(0x0) = CONST 
    0x1249: v1249(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x125e: v125e = AND v1249(0xffffffffffffffffffffffffffffffffffffffff), v42c
    0x125f: v125f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1274: v1274 = AND v125f(0xffffffffffffffffffffffffffffffffffffffff), v125e
    0x1276: MSTORE v1246(0x0), v1274
    0x1277: v1277(0x20) = CONST 
    0x1279: v1279(0x20) = ADD v1277(0x20), v1246(0x0)
    0x127c: MSTORE v1279(0x20), v1244(0x3)
    0x127d: v127d(0x20) = CONST 
    0x127f: v127f(0x40) = ADD v127d(0x20), v1279(0x20)
    0x1280: v1280(0x0) = CONST 
    0x1282: v1282 = SHA3 v1280(0x0), v127f(0x40)
    0x1283: v1283(0x0) = CONST 
    0x1285: v1285(0x100) = CONST 
    0x1288: v1288(0x1) = EXP v1285(0x100), v1283(0x0)
    0x128a: v128a = SLOAD v1282
    0x128c: v128c(0xff) = CONST 
    0x128e: v128e(0xff) = MUL v128c(0xff), v1288(0x1)
    0x128f: v128f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v128e(0xff)
    0x1290: v1290 = AND v128f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v128a
    0x1293: v1293(0x1) = ISZERO v1242(0x0)
    0x1294: v1294(0x0) = ISZERO v1293(0x1)
    0x1295: v1295(0x0) = MUL v1294(0x0), v1288(0x1)
    0x1296: v1296 = OR v1295(0x0), v1290
    0x1298: SSTORE v1282, v1296
    0x129b: v129b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12b0: v12b0 = AND v129b(0xffffffffffffffffffffffffffffffffffffffff), v42c
    0x12b1: v12b1(0x20fe26e62bba36b5afff8a39e3e59ba2b90f6f0b963037740d55af2d93dd3435) = CONST 
    0x12d2: v12d2(0x0) = CONST 
    0x12d4: v12d4(0x40) = CONST 
    0x12d6: v12d6 = MLOAD v12d4(0x40)
    0x12d9: v12d9(0x1) = ISZERO v12d2(0x0)
    0x12da: v12da(0x0) = ISZERO v12d9(0x1)
    0x12dc: MSTORE v12d6, v12da(0x0)
    0x12dd: v12dd(0x20) = CONST 
    0x12df: v12df = ADD v12dd(0x20), v12d6
    0x12e3: v12e3(0x40) = CONST 
    0x12e5: v12e5 = MLOAD v12e3(0x40)
    0x12e8: v12e8(0x20) = SUB v12df, v12e5
    0x12ea: LOG2 v12e5, v12e8(0x20), v12b1(0x20fe26e62bba36b5afff8a39e3e59ba2b90f6f0b963037740d55af2d93dd3435), v12b0
    0x12ec: JUMP v3fb(0x43c)

    Begin block 0x43c
    prev=[0x1241], succ=[]
    =================================
    0x43d: STOP 

}

function unpause()() public {
    Begin block 0x43e
    prev=[], succ=[0x12ed]
    =================================
    0x43f: v43f(0x446) = CONST 
    0x442: v442(0x12ed) = CONST 
    0x445: JUMP v442(0x12ed)

    Begin block 0x12ed
    prev=[0x43e], succ=[0x1343, 0x13b0]
    =================================
    0x12ee: v12ee(0x6) = CONST 
    0x12f0: v12f0(0x0) = CONST 
    0x12f3: v12f3 = SLOAD v12ee(0x6)
    0x12f5: v12f5(0x100) = CONST 
    0x12f8: v12f8(0x1) = EXP v12f5(0x100), v12f0(0x0)
    0x12fa: v12fa = DIV v12f3, v12f8(0x1)
    0x12fb: v12fb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1310: v1310 = AND v12fb(0xffffffffffffffffffffffffffffffffffffffff), v12fa
    0x1311: v1311(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1326: v1326 = AND v1311(0xffffffffffffffffffffffffffffffffffffffff), v1310
    0x1327: v1327 = CALLER 
    0x1328: v1328(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x133d: v133d = AND v1328(0xffffffffffffffffffffffffffffffffffffffff), v1327
    0x133e: v133e = EQ v133d, v1326
    0x133f: v133f(0x13b0) = CONST 
    0x1342: JUMPI v133f(0x13b0), v133e

    Begin block 0x1343
    prev=[0x12ed], succ=[]
    =================================
    0x1343: v1343(0x40) = CONST 
    0x1345: v1345 = MLOAD v1343(0x40)
    0x1346: v1346(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1368: MSTORE v1345, v1346(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1369: v1369(0x4) = CONST 
    0x136b: v136b = ADD v1369(0x4), v1345
    0x136e: v136e(0x20) = CONST 
    0x1370: v1370 = ADD v136e(0x20), v136b
    0x1373: v1373(0x20) = SUB v1370, v136b
    0x1375: MSTORE v136b, v1373(0x20)
    0x1376: v1376(0x15) = CONST 
    0x1379: MSTORE v1370, v1376(0x15)
    0x137a: v137a(0x20) = CONST 
    0x137c: v137c = ADD v137a(0x20), v1370
    0x137e: v137e(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x13a0: MSTORE v137c, v137e(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x13a2: v13a2(0x20) = CONST 
    0x13a4: v13a4 = ADD v13a2(0x20), v137c
    0x13a8: v13a8(0x40) = CONST 
    0x13aa: v13aa = MLOAD v13a8(0x40)
    0x13ad: v13ad(0x64) = SUB v13a4, v13aa
    0x13af: REVERT v13aa, v13ad(0x64)

    Begin block 0x13b0
    prev=[0x12ed], succ=[0x446]
    =================================
    0x13b1: v13b1(0x0) = CONST 
    0x13b3: v13b3(0x6) = CONST 
    0x13b5: v13b5(0x14) = CONST 
    0x13b7: v13b7(0x100) = CONST 
    0x13ba: v13ba(0x10000000000000000000000000000000000000000) = EXP v13b7(0x100), v13b5(0x14)
    0x13bc: v13bc = SLOAD v13b3(0x6)
    0x13be: v13be(0xff) = CONST 
    0x13c0: v13c0(0xff0000000000000000000000000000000000000000) = MUL v13be(0xff), v13ba(0x10000000000000000000000000000000000000000)
    0x13c1: v13c1(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v13c0(0xff0000000000000000000000000000000000000000)
    0x13c2: v13c2 = AND v13c1(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v13bc
    0x13c5: v13c5(0x1) = ISZERO v13b1(0x0)
    0x13c6: v13c6(0x0) = ISZERO v13c5(0x1)
    0x13c7: v13c7(0x0) = MUL v13c6(0x0), v13ba(0x10000000000000000000000000000000000000000)
    0x13c8: v13c8 = OR v13c7(0x0), v13c2
    0x13ca: SSTORE v13b3(0x6), v13c8
    0x13cc: JUMP v43f(0x446)

    Begin block 0x446
    prev=[0x13b0], succ=[]
    =================================
    0x447: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x448
    prev=[], succ=[0x45a, 0x45e]
    =================================
    0x449: v449(0x494) = CONST 
    0x44c: v44c(0x4) = CONST 
    0x44f: v44f = CALLDATASIZE 
    0x450: v450 = SUB v44f, v44c(0x4)
    0x451: v451(0x40) = CONST 
    0x454: v454 = LT v450, v451(0x40)
    0x455: v455 = ISZERO v454
    0x456: v456(0x45e) = CONST 
    0x459: JUMPI v456(0x45e), v455

    Begin block 0x45a
    prev=[0x448], succ=[]
    =================================
    0x45a: v45a(0x0) = CONST 
    0x45d: REVERT v45a(0x0), v45a(0x0)

    Begin block 0x45e
    prev=[0x448], succ=[0x13cd]
    =================================
    0x460: v460 = ADD v44c(0x4), v450
    0x464: v464 = CALLDATALOAD v44c(0x4)
    0x465: v465(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x47a: v47a = AND v465(0xffffffffffffffffffffffffffffffffffffffff), v464
    0x47c: v47c(0x20) = CONST 
    0x47e: v47e(0x24) = ADD v47c(0x20), v44c(0x4)
    0x484: v484 = CALLDATALOAD v47e(0x24)
    0x486: v486(0x20) = CONST 
    0x488: v488(0x44) = ADD v486(0x20), v47e(0x24)
    0x490: v490(0x13cd) = CONST 
    0x493: JUMP v490(0x13cd)

    Begin block 0x13cd
    prev=[0x45e], succ=[0x1425, 0x1492]
    =================================
    0x13ce: v13ce(0x0) = CONST 
    0x13d0: v13d0(0x6) = CONST 
    0x13d2: v13d2(0x0) = CONST 
    0x13d5: v13d5 = SLOAD v13d0(0x6)
    0x13d7: v13d7(0x100) = CONST 
    0x13da: v13da(0x1) = EXP v13d7(0x100), v13d2(0x0)
    0x13dc: v13dc = DIV v13d5, v13da(0x1)
    0x13dd: v13dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13f2: v13f2 = AND v13dd(0xffffffffffffffffffffffffffffffffffffffff), v13dc
    0x13f3: v13f3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1408: v1408 = AND v13f3(0xffffffffffffffffffffffffffffffffffffffff), v13f2
    0x1409: v1409 = CALLER 
    0x140a: v140a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x141f: v141f = AND v140a(0xffffffffffffffffffffffffffffffffffffffff), v1409
    0x1420: v1420 = EQ v141f, v1408
    0x1421: v1421(0x1492) = CONST 
    0x1424: JUMPI v1421(0x1492), v1420

    Begin block 0x1425
    prev=[0x13cd], succ=[]
    =================================
    0x1425: v1425(0x40) = CONST 
    0x1427: v1427 = MLOAD v1425(0x40)
    0x1428: v1428(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x144a: MSTORE v1427, v1428(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x144b: v144b(0x4) = CONST 
    0x144d: v144d = ADD v144b(0x4), v1427
    0x1450: v1450(0x20) = CONST 
    0x1452: v1452 = ADD v1450(0x20), v144d
    0x1455: v1455(0x20) = SUB v1452, v144d
    0x1457: MSTORE v144d, v1455(0x20)
    0x1458: v1458(0x15) = CONST 
    0x145b: MSTORE v1452, v1458(0x15)
    0x145c: v145c(0x20) = CONST 
    0x145e: v145e = ADD v145c(0x20), v1452
    0x1460: v1460(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x1482: MSTORE v145e, v1460(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x1484: v1484(0x20) = CONST 
    0x1486: v1486 = ADD v1484(0x20), v145e
    0x148a: v148a(0x40) = CONST 
    0x148c: v148c = MLOAD v148a(0x40)
    0x148f: v148f(0x64) = SUB v1486, v148c
    0x1491: REVERT v148c, v148f(0x64)

    Begin block 0x1492
    prev=[0x13cd], succ=[0x14ae, 0x151b]
    =================================
    0x1493: v1493(0x0) = CONST 
    0x1495: v1495(0x1) = ISZERO v1493(0x0)
    0x1496: v1496(0x0) = ISZERO v1495(0x1)
    0x1497: v1497(0x6) = CONST 
    0x1499: v1499(0x14) = CONST 
    0x149c: v149c = SLOAD v1497(0x6)
    0x149e: v149e(0x100) = CONST 
    0x14a1: v14a1(0x10000000000000000000000000000000000000000) = EXP v149e(0x100), v1499(0x14)
    0x14a3: v14a3 = DIV v149c, v14a1(0x10000000000000000000000000000000000000000)
    0x14a4: v14a4(0xff) = CONST 
    0x14a6: v14a6 = AND v14a4(0xff), v14a3
    0x14a7: v14a7 = ISZERO v14a6
    0x14a8: v14a8 = ISZERO v14a7
    0x14a9: v14a9 = EQ v14a8, v1496(0x0)
    0x14aa: v14aa(0x151b) = CONST 
    0x14ad: JUMPI v14aa(0x151b), v14a9

    Begin block 0x14ae
    prev=[0x1492], succ=[]
    =================================
    0x14ae: v14ae(0x40) = CONST 
    0x14b0: v14b0 = MLOAD v14ae(0x40)
    0x14b1: v14b1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x14d3: MSTORE v14b0, v14b1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14d4: v14d4(0x4) = CONST 
    0x14d6: v14d6 = ADD v14d4(0x4), v14b0
    0x14d9: v14d9(0x20) = CONST 
    0x14db: v14db = ADD v14d9(0x20), v14d6
    0x14de: v14de(0x20) = SUB v14db, v14d6
    0x14e0: MSTORE v14d6, v14de(0x20)
    0x14e1: v14e1(0x16) = CONST 
    0x14e4: MSTORE v14db, v14e1(0x16)
    0x14e5: v14e5(0x20) = CONST 
    0x14e7: v14e7 = ADD v14e5(0x20), v14db
    0x14e9: v14e9(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x150b: MSTORE v14e7, v14e9(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x150d: v150d(0x20) = CONST 
    0x150f: v150f = ADD v150d(0x20), v14e7
    0x1513: v1513(0x40) = CONST 
    0x1515: v1515 = MLOAD v1513(0x40)
    0x1518: v1518(0x64) = SUB v150f, v1515
    0x151a: REVERT v1515, v1518(0x64)

    Begin block 0x151b
    prev=[0x1492], succ=[0x1543]
    =================================
    0x151c: v151c(0x0) = CONST 
    0x1521: v1521(0x0) = CONST 
    0x1523: v1523(0x1551) = CONST 
    0x1526: v1526(0x5) = CONST 
    0x1528: v1528 = SLOAD v1526(0x5)
    0x1529: v1529(0x1543) = CONST 
    0x152c: v152c(0xde0b6b3a7640000) = CONST 
    0x1536: v1536(0x2c98) = CONST 
    0x153c: v153c(0xffffffff) = CONST 
    0x1541: v1541(0x2c98) = AND v153c(0xffffffff), v1536(0x2c98)
    0x1542: v1542_0 = CALLPRIVATE v1541(0x2c98), v152c(0xde0b6b3a7640000), v484, v1529(0x1543)

    Begin block 0x1543
    prev=[0x151b], succ=[0x1551]
    =================================
    0x1544: v1544(0x2d1e) = CONST 
    0x154a: v154a(0xffffffff) = CONST 
    0x154f: v154f(0x2d1e) = AND v154a(0xffffffff), v1544(0x2d1e)
    0x1550: v1550_0 = CALLPRIVATE v154f(0x2d1e), v1528, v1542_0, v1523(0x1551)

    Begin block 0x1551
    prev=[0x1543], succ=[0x31a6]
    =================================
    0x1554: v1554(0x155e) = CONST 
    0x155a: v155a(0x31a6) = CONST 
    0x155d: JUMP v155a(0x31a6)

    Begin block 0x31a6
    prev=[0x1551], succ=[0x31dc, 0x3249]
    =================================
    0x31a7: v31a7(0x0) = CONST 
    0x31a9: v31a9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x31be: v31be(0x0) = AND v31a9(0xffffffffffffffffffffffffffffffffffffffff), v31a7(0x0)
    0x31c0: v31c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x31d5: v31d5 = AND v31c0(0xffffffffffffffffffffffffffffffffffffffff), v47a
    0x31d6: v31d6 = EQ v31d5, v31be(0x0)
    0x31d7: v31d7 = ISZERO v31d6
    0x31d8: v31d8(0x3249) = CONST 
    0x31db: JUMPI v31d8(0x3249), v31d7

    Begin block 0x31dc
    prev=[0x31a6], succ=[]
    =================================
    0x31dc: v31dc(0x40) = CONST 
    0x31de: v31de = MLOAD v31dc(0x40)
    0x31df: v31df(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3201: MSTORE v31de, v31df(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3202: v3202(0x4) = CONST 
    0x3204: v3204 = ADD v3202(0x4), v31de
    0x3207: v3207(0x20) = CONST 
    0x3209: v3209 = ADD v3207(0x20), v3204
    0x320c: v320c(0x20) = SUB v3209, v3204
    0x320e: MSTORE v3204, v320c(0x20)
    0x320f: v320f(0x1f) = CONST 
    0x3212: MSTORE v3209, v320f(0x1f)
    0x3213: v3213(0x20) = CONST 
    0x3215: v3215 = ADD v3213(0x20), v3209
    0x3217: v3217(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300) = CONST 
    0x3239: MSTORE v3215, v3217(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300)
    0x323b: v323b(0x20) = CONST 
    0x323d: v323d = ADD v323b(0x20), v3215
    0x3241: v3241(0x40) = CONST 
    0x3243: v3243 = MLOAD v3241(0x40)
    0x3246: v3246(0x64) = SUB v323d, v3243
    0x3248: REVERT v3243, v3246(0x64)

    Begin block 0x3249
    prev=[0x31a6], succ=[0x311eB0x3249]
    =================================
    0x324a: v324a(0x325e) = CONST 
    0x324e: v324e(0x4) = CONST 
    0x3250: v3250 = SLOAD v324e(0x4)
    0x3251: v3251(0x311e) = CONST 
    0x3257: v3257(0xffffffff) = CONST 
    0x325c: v325c(0x311e) = AND v3257(0xffffffff), v3251(0x311e)
    0x325d: JUMP v325c(0x311e)

    Begin block 0x311eB0x3249
    prev=[0x3249], succ=[0x312fB0x3249, 0x319cB0x3249]
    =================================
    0x311fS0x3249: v311fV3249(0x0) = CONST 
    0x3124S0x3249: v3124V3249 = ADD v3250, v1550_0
    0x3129S0x3249: v3129V3249 = LT v3124V3249, v3250
    0x312aS0x3249: v312aV3249 = ISZERO v3129V3249
    0x312bS0x3249: v312bV3249(0x319c) = CONST 
    0x312eS0x3249: JUMPI v312bV3249(0x319c), v312aV3249

    Begin block 0x312fB0x3249
    prev=[0x311eB0x3249], succ=[]
    =================================
    0x312fS0x3249: v312fV3249(0x40) = CONST 
    0x3131S0x3249: v3131V3249 = MLOAD v312fV3249(0x40)
    0x3132S0x3249: v3132V3249(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3154S0x3249: MSTORE v3131V3249, v3132V3249(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3155S0x3249: v3155V3249(0x4) = CONST 
    0x3157S0x3249: v3157V3249 = ADD v3155V3249(0x4), v3131V3249
    0x315aS0x3249: v315aV3249(0x20) = CONST 
    0x315cS0x3249: v315cV3249 = ADD v315aV3249(0x20), v3157V3249
    0x315fS0x3249: v315fV3249(0x20) = SUB v315cV3249, v3157V3249
    0x3161S0x3249: MSTORE v3157V3249, v315fV3249(0x20)
    0x3162S0x3249: v3162V3249(0x1b) = CONST 
    0x3165S0x3249: MSTORE v315cV3249, v3162V3249(0x1b)
    0x3166S0x3249: v3166V3249(0x20) = CONST 
    0x3168S0x3249: v3168V3249 = ADD v3166V3249(0x20), v315cV3249
    0x316aS0x3249: v316aV3249(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x318cS0x3249: MSTORE v3168V3249, v316aV3249(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x318eS0x3249: v318eV3249(0x20) = CONST 
    0x3190S0x3249: v3190V3249 = ADD v318eV3249(0x20), v3168V3249
    0x3194S0x3249: v3194V3249(0x40) = CONST 
    0x3196S0x3249: v3196V3249 = MLOAD v3194V3249(0x40)
    0x3199S0x3249: v3199V3249(0x64) = SUB v3190V3249, v3196V3249
    0x319bS0x3249: REVERT v3196V3249, v3199V3249(0x64)

    Begin block 0x319cB0x3249
    prev=[0x311eB0x3249], succ=[0x325e]
    =================================
    0x31a5S0x3249: JUMP v324a(0x325e)

    Begin block 0x325e
    prev=[0x319cB0x3249], succ=[0x311eB0x325e]
    =================================
    0x325f: v325f(0x4) = CONST 
    0x3263: SSTORE v325f(0x4), v3124V3249
    0x3265: v3265(0x32b6) = CONST 
    0x3269: v3269(0x1) = CONST 
    0x326b: v326b(0x0) = CONST 
    0x326e: v326e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3283: v3283 = AND v326e(0xffffffffffffffffffffffffffffffffffffffff), v47a
    0x3284: v3284(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3299: v3299 = AND v3284(0xffffffffffffffffffffffffffffffffffffffff), v3283
    0x329b: MSTORE v326b(0x0), v3299
    0x329c: v329c(0x20) = CONST 
    0x329e: v329e(0x20) = ADD v329c(0x20), v326b(0x0)
    0x32a1: MSTORE v329e(0x20), v3269(0x1)
    0x32a2: v32a2(0x20) = CONST 
    0x32a4: v32a4(0x40) = ADD v32a2(0x20), v329e(0x20)
    0x32a5: v32a5(0x0) = CONST 
    0x32a7: v32a7 = SHA3 v32a5(0x0), v32a4(0x40)
    0x32a8: v32a8 = SLOAD v32a7
    0x32a9: v32a9(0x311e) = CONST 
    0x32af: v32af(0xffffffff) = CONST 
    0x32b4: v32b4(0x311e) = AND v32af(0xffffffff), v32a9(0x311e)
    0x32b5: JUMP v32b4(0x311e)

    Begin block 0x311eB0x325e
    prev=[0x325e], succ=[0x312fB0x325e, 0x319cB0x325e]
    =================================
    0x311fS0x325e: v311fV325e(0x0) = CONST 
    0x3124S0x325e: v3124V325e = ADD v32a8, v1550_0
    0x3129S0x325e: v3129V325e = LT v3124V325e, v32a8
    0x312aS0x325e: v312aV325e = ISZERO v3129V325e
    0x312bS0x325e: v312bV325e(0x319c) = CONST 
    0x312eS0x325e: JUMPI v312bV325e(0x319c), v312aV325e

    Begin block 0x312fB0x325e
    prev=[0x311eB0x325e], succ=[]
    =================================
    0x312fS0x325e: v312fV325e(0x40) = CONST 
    0x3131S0x325e: v3131V325e = MLOAD v312fV325e(0x40)
    0x3132S0x325e: v3132V325e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3154S0x325e: MSTORE v3131V325e, v3132V325e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3155S0x325e: v3155V325e(0x4) = CONST 
    0x3157S0x325e: v3157V325e = ADD v3155V325e(0x4), v3131V325e
    0x315aS0x325e: v315aV325e(0x20) = CONST 
    0x315cS0x325e: v315cV325e = ADD v315aV325e(0x20), v3157V325e
    0x315fS0x325e: v315fV325e(0x20) = SUB v315cV325e, v3157V325e
    0x3161S0x325e: MSTORE v3157V325e, v315fV325e(0x20)
    0x3162S0x325e: v3162V325e(0x1b) = CONST 
    0x3165S0x325e: MSTORE v315cV325e, v3162V325e(0x1b)
    0x3166S0x325e: v3166V325e(0x20) = CONST 
    0x3168S0x325e: v3168V325e = ADD v3166V325e(0x20), v315cV325e
    0x316aS0x325e: v316aV325e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x318cS0x325e: MSTORE v3168V325e, v316aV325e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x318eS0x325e: v318eV325e(0x20) = CONST 
    0x3190S0x325e: v3190V325e = ADD v318eV325e(0x20), v3168V325e
    0x3194S0x325e: v3194V325e(0x40) = CONST 
    0x3196S0x325e: v3196V325e = MLOAD v3194V325e(0x40)
    0x3199S0x325e: v3199V325e(0x64) = SUB v3190V325e, v3196V325e
    0x319bS0x325e: REVERT v3196V325e, v3199V325e(0x64)

    Begin block 0x319cB0x325e
    prev=[0x311eB0x325e], succ=[0x32b6]
    =================================
    0x31a5S0x325e: JUMP v3265(0x32b6)

    Begin block 0x32b6
    prev=[0x319cB0x325e], succ=[0x155e]
    =================================
    0x32b7: v32b7(0x1) = CONST 
    0x32b9: v32b9(0x0) = CONST 
    0x32bc: v32bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x32d1: v32d1 = AND v32bc(0xffffffffffffffffffffffffffffffffffffffff), v47a
    0x32d2: v32d2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x32e7: v32e7 = AND v32d2(0xffffffffffffffffffffffffffffffffffffffff), v32d1
    0x32e9: MSTORE v32b9(0x0), v32e7
    0x32ea: v32ea(0x20) = CONST 
    0x32ec: v32ec(0x20) = ADD v32ea(0x20), v32b9(0x0)
    0x32ef: MSTORE v32ec(0x20), v32b7(0x1)
    0x32f0: v32f0(0x20) = CONST 
    0x32f2: v32f2(0x40) = ADD v32f0(0x20), v32ec(0x20)
    0x32f3: v32f3(0x0) = CONST 
    0x32f5: v32f5 = SHA3 v32f3(0x0), v32f2(0x40)
    0x32f8: SSTORE v32f5, v3124V325e
    0x32fb: v32fb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3310: v3310 = AND v32fb(0xffffffffffffffffffffffffffffffffffffffff), v47a
    0x3311: v3311(0x0) = CONST 
    0x3313: v3313(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3328: v3328(0x0) = AND v3313(0xffffffffffffffffffffffffffffffffffffffff), v3311(0x0)
    0x3329: v3329(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x334b: v334b(0x40) = CONST 
    0x334d: v334d = MLOAD v334b(0x40)
    0x3351: MSTORE v334d, v484
    0x3352: v3352(0x20) = CONST 
    0x3354: v3354 = ADD v3352(0x20), v334d
    0x3358: v3358(0x40) = CONST 
    0x335a: v335a = MLOAD v3358(0x40)
    0x335d: v335d(0x20) = SUB v3354, v335a
    0x335f: LOG3 v335a, v335d(0x20), v3329(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v3328(0x0), v3310
    0x3363: JUMP v1554(0x155e)

    Begin block 0x155e
    prev=[0x32b6], succ=[0x494]
    =================================
    0x155f: v155f(0x1) = CONST 
    0x1569: JUMP v449(0x494)

    Begin block 0x494
    prev=[0x155e], succ=[]
    =================================
    0x495: v495(0x40) = CONST 
    0x497: v497 = MLOAD v495(0x40)
    0x49a: v49a = ISZERO v155f(0x1)
    0x49b: v49b = ISZERO v49a
    0x49d: MSTORE v497, v49b
    0x49e: v49e(0x20) = CONST 
    0x4a0: v4a0 = ADD v49e(0x20), v497
    0x4a4: v4a4(0x40) = CONST 
    0x4a6: v4a6 = MLOAD v4a4(0x40)
    0x4a9: v4a9(0x20) = SUB v4a0, v4a6
    0x4ab: RETURN v4a6, v4a9(0x20)

}

function updateCode(address)() public {
    Begin block 0x4ac
    prev=[], succ=[0x4be, 0x4c2]
    =================================
    0x4ad: v4ad(0x4ee) = CONST 
    0x4b0: v4b0(0x4) = CONST 
    0x4b3: v4b3 = CALLDATASIZE 
    0x4b4: v4b4 = SUB v4b3, v4b0(0x4)
    0x4b5: v4b5(0x20) = CONST 
    0x4b8: v4b8 = LT v4b4, v4b5(0x20)
    0x4b9: v4b9 = ISZERO v4b8
    0x4ba: v4ba(0x4c2) = CONST 
    0x4bd: JUMPI v4ba(0x4c2), v4b9

    Begin block 0x4be
    prev=[0x4ac], succ=[]
    =================================
    0x4be: v4be(0x0) = CONST 
    0x4c1: REVERT v4be(0x0), v4be(0x0)

    Begin block 0x4c2
    prev=[0x4ac], succ=[0x156a]
    =================================
    0x4c4: v4c4 = ADD v4b0(0x4), v4b4
    0x4c8: v4c8 = CALLDATALOAD v4b0(0x4)
    0x4c9: v4c9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4de: v4de = AND v4c9(0xffffffffffffffffffffffffffffffffffffffff), v4c8
    0x4e0: v4e0(0x20) = CONST 
    0x4e2: v4e2(0x24) = ADD v4e0(0x20), v4b0(0x4)
    0x4ea: v4ea(0x156a) = CONST 
    0x4ed: JUMP v4ea(0x156a)

    Begin block 0x156a
    prev=[0x4c2], succ=[0x15c0, 0x162d]
    =================================
    0x156b: v156b(0x6) = CONST 
    0x156d: v156d(0x0) = CONST 
    0x1570: v1570 = SLOAD v156b(0x6)
    0x1572: v1572(0x100) = CONST 
    0x1575: v1575(0x1) = EXP v1572(0x100), v156d(0x0)
    0x1577: v1577 = DIV v1570, v1575(0x1)
    0x1578: v1578(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x158d: v158d = AND v1578(0xffffffffffffffffffffffffffffffffffffffff), v1577
    0x158e: v158e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15a3: v15a3 = AND v158e(0xffffffffffffffffffffffffffffffffffffffff), v158d
    0x15a4: v15a4 = CALLER 
    0x15a5: v15a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15ba: v15ba = AND v15a5(0xffffffffffffffffffffffffffffffffffffffff), v15a4
    0x15bb: v15bb = EQ v15ba, v15a3
    0x15bc: v15bc(0x162d) = CONST 
    0x15bf: JUMPI v15bc(0x162d), v15bb

    Begin block 0x15c0
    prev=[0x156a], succ=[]
    =================================
    0x15c0: v15c0(0x40) = CONST 
    0x15c2: v15c2 = MLOAD v15c0(0x40)
    0x15c3: v15c3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x15e5: MSTORE v15c2, v15c3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15e6: v15e6(0x4) = CONST 
    0x15e8: v15e8 = ADD v15e6(0x4), v15c2
    0x15eb: v15eb(0x20) = CONST 
    0x15ed: v15ed = ADD v15eb(0x20), v15e8
    0x15f0: v15f0(0x20) = SUB v15ed, v15e8
    0x15f2: MSTORE v15e8, v15f0(0x20)
    0x15f3: v15f3(0x15) = CONST 
    0x15f6: MSTORE v15ed, v15f3(0x15)
    0x15f7: v15f7(0x20) = CONST 
    0x15f9: v15f9 = ADD v15f7(0x20), v15ed
    0x15fb: v15fb(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x161d: MSTORE v15f9, v15fb(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x161f: v161f(0x20) = CONST 
    0x1621: v1621 = ADD v161f(0x20), v15f9
    0x1625: v1625(0x40) = CONST 
    0x1627: v1627 = MLOAD v1625(0x40)
    0x162a: v162a(0x64) = SUB v1621, v1627
    0x162c: REVERT v1627, v162a(0x64)

    Begin block 0x162d
    prev=[0x156a], succ=[0x1647, 0x1697]
    =================================
    0x162e: v162e(0x1) = CONST 
    0x1630: v1630(0x0) = ISZERO v162e(0x1)
    0x1631: v1631(0x1) = ISZERO v1630(0x0)
    0x1632: v1632(0x0) = CONST 
    0x1635: v1635 = SLOAD v1632(0x0)
    0x1637: v1637(0x100) = CONST 
    0x163a: v163a(0x1) = EXP v1637(0x100), v1632(0x0)
    0x163c: v163c = DIV v1635, v163a(0x1)
    0x163d: v163d(0xff) = CONST 
    0x163f: v163f = AND v163d(0xff), v163c
    0x1640: v1640 = ISZERO v163f
    0x1641: v1641 = ISZERO v1640
    0x1642: v1642 = EQ v1641, v1631(0x1)
    0x1643: v1643(0x1697) = CONST 
    0x1646: JUMPI v1643(0x1697), v1642

    Begin block 0x1647
    prev=[0x162d], succ=[]
    =================================
    0x1647: v1647(0x40) = CONST 
    0x1649: v1649 = MLOAD v1647(0x40)
    0x164a: v164a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x166c: MSTORE v1649, v164a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x166d: v166d(0x4) = CONST 
    0x166f: v166f = ADD v166d(0x4), v1649
    0x1672: v1672(0x20) = CONST 
    0x1674: v1674 = ADD v1672(0x20), v166f
    0x1677: v1677(0x20) = SUB v1674, v166f
    0x1679: MSTORE v166f, v1677(0x20)
    0x167a: v167a(0x33) = CONST 
    0x167d: MSTORE v1674, v167a(0x33)
    0x167e: v167e(0x20) = CONST 
    0x1680: v1680 = ADD v167e(0x20), v1674
    0x1682: v1682(0x3911) = CONST 
    0x1685: v1685(0x33) = CONST 
    0x1688: CODECOPY v1680, v1682(0x3911), v1685(0x33)
    0x1689: v1689(0x40) = CONST 
    0x168b: v168b = ADD v1689(0x40), v1680
    0x168f: v168f(0x40) = CONST 
    0x1691: v1691 = MLOAD v168f(0x40)
    0x1694: v1694(0x84) = SUB v168b, v1691
    0x1696: REVERT v1691, v1694(0x84)

    Begin block 0x1697
    prev=[0x162d], succ=[0x3364]
    =================================
    0x1698: v1698(0x16a0) = CONST 
    0x169c: v169c(0x3364) = CONST 
    0x169f: JUMP v169c(0x3364)

    Begin block 0x3364
    prev=[0x1697], succ=[0x33a6, 0x33aa]
    =================================
    0x3366: v3366(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x337b: v337b = AND v3366(0xffffffffffffffffffffffffffffffffffffffff), v4de
    0x337c: v337c(0x52d1902d) = CONST 
    0x3381: v3381(0x40) = CONST 
    0x3383: v3383 = MLOAD v3381(0x40)
    0x3385: v3385(0xffffffff) = CONST 
    0x338a: v338a(0x52d1902d) = AND v3385(0xffffffff), v337c(0x52d1902d)
    0x338b: v338b(0xe0) = CONST 
    0x338d: v338d(0x52d1902d00000000000000000000000000000000000000000000000000000000) = SHL v338b(0xe0), v338a(0x52d1902d)
    0x338f: MSTORE v3383, v338d(0x52d1902d00000000000000000000000000000000000000000000000000000000)
    0x3390: v3390(0x4) = CONST 
    0x3392: v3392 = ADD v3390(0x4), v3383
    0x3393: v3393(0x20) = CONST 
    0x3395: v3395(0x40) = CONST 
    0x3397: v3397 = MLOAD v3395(0x40)
    0x339a: v339a(0x4) = SUB v3392, v3397
    0x339e: v339e = EXTCODESIZE v337b
    0x339f: v339f = ISZERO v339e
    0x33a1: v33a1 = ISZERO v339f
    0x33a2: v33a2(0x33aa) = CONST 
    0x33a5: JUMPI v33a2(0x33aa), v33a1

    Begin block 0x33a6
    prev=[0x3364], succ=[]
    =================================
    0x33a6: v33a6(0x0) = CONST 
    0x33a9: REVERT v33a6(0x0), v33a6(0x0)

    Begin block 0x33aa
    prev=[0x3364], succ=[0x33b5, 0x33be]
    =================================
    0x33ac: v33ac = GAS 
    0x33ad: v33ad = STATICCALL v33ac, v337b, v3397, v339a(0x4), v3397, v3393(0x20)
    0x33ae: v33ae = ISZERO v33ad
    0x33b0: v33b0 = ISZERO v33ae
    0x33b1: v33b1(0x33be) = CONST 
    0x33b4: JUMPI v33b1(0x33be), v33b0

    Begin block 0x33b5
    prev=[0x33aa], succ=[]
    =================================
    0x33b5: v33b5 = RETURNDATASIZE 
    0x33b6: v33b6(0x0) = CONST 
    0x33b9: RETURNDATACOPY v33b6(0x0), v33b6(0x0), v33b5
    0x33ba: v33ba = RETURNDATASIZE 
    0x33bb: v33bb(0x0) = CONST 
    0x33bd: REVERT v33bb(0x0), v33ba

    Begin block 0x33be
    prev=[0x33aa], succ=[0x33d0, 0x33d4]
    =================================
    0x33c3: v33c3(0x40) = CONST 
    0x33c5: v33c5 = MLOAD v33c3(0x40)
    0x33c6: v33c6 = RETURNDATASIZE 
    0x33c7: v33c7(0x20) = CONST 
    0x33ca: v33ca = LT v33c6, v33c7(0x20)
    0x33cb: v33cb = ISZERO v33ca
    0x33cc: v33cc(0x33d4) = CONST 
    0x33cf: JUMPI v33cc(0x33d4), v33cb

    Begin block 0x33d0
    prev=[0x33be], succ=[]
    =================================
    0x33d0: v33d0(0x0) = CONST 
    0x33d3: REVERT v33d0(0x0), v33d0(0x0)

    Begin block 0x33d4
    prev=[0x33be], succ=[0x340f, 0x347c]
    =================================
    0x33d6: v33d6 = ADD v33c5, v33c6
    0x33da: v33da = MLOAD v33c5
    0x33dc: v33dc(0x20) = CONST 
    0x33de: v33de = ADD v33dc(0x20), v33c5
    0x33e6: v33e6(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x3407: v3407(0x0) = CONST 
    0x3409: v3409(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = SHL v3407(0x0), v33e6(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x340a: v340a = EQ v3409(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7), v33da
    0x340b: v340b(0x347c) = CONST 
    0x340e: JUMPI v340b(0x347c), v340a

    Begin block 0x340f
    prev=[0x33d4], succ=[]
    =================================
    0x340f: v340f(0x40) = CONST 
    0x3411: v3411 = MLOAD v340f(0x40)
    0x3412: v3412(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3434: MSTORE v3411, v3412(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3435: v3435(0x4) = CONST 
    0x3437: v3437 = ADD v3435(0x4), v3411
    0x343a: v343a(0x20) = CONST 
    0x343c: v343c = ADD v343a(0x20), v3437
    0x343f: v343f(0x20) = SUB v343c, v3437
    0x3441: MSTORE v3437, v343f(0x20)
    0x3442: v3442(0xe) = CONST 
    0x3445: MSTORE v343c, v3442(0xe)
    0x3446: v3446(0x20) = CONST 
    0x3448: v3448 = ADD v3446(0x20), v343c
    0x344a: v344a(0x4e6f7420636f6d70617469626c65000000000000000000000000000000000000) = CONST 
    0x346c: MSTORE v3448, v344a(0x4e6f7420636f6d70617469626c65000000000000000000000000000000000000)
    0x346e: v346e(0x20) = CONST 
    0x3470: v3470 = ADD v346e(0x20), v3448
    0x3474: v3474(0x40) = CONST 
    0x3476: v3476 = MLOAD v3474(0x40)
    0x3479: v3479(0x64) = SUB v3470, v3476
    0x347b: REVERT v3476, v3479(0x64)

    Begin block 0x347c
    prev=[0x33d4], succ=[0x16a0]
    =================================
    0x347e: v347e(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x349f: SSTORE v347e(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7), v4de
    0x34a1: JUMP v1698(0x16a0)

    Begin block 0x16a0
    prev=[0x347c], succ=[0x4ee]
    =================================
    0x16a2: v16a2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16b7: v16b7 = AND v16a2(0xffffffffffffffffffffffffffffffffffffffff), v4de
    0x16b8: v16b8(0x34459cf4c63f38e9b4af4ff8f74035bad6157484e669ffde70188afdf9917c68) = CONST 
    0x16d9: v16d9(0x40) = CONST 
    0x16db: v16db = MLOAD v16d9(0x40)
    0x16dc: v16dc(0x40) = CONST 
    0x16de: v16de = MLOAD v16dc(0x40)
    0x16e1: v16e1(0x0) = SUB v16db, v16de
    0x16e3: LOG2 v16de, v16e1(0x0), v16b8(0x34459cf4c63f38e9b4af4ff8f74035bad6157484e669ffde70188afdf9917c68), v16b7
    0x16e5: JUMP v4ad(0x4ee)

    Begin block 0x4ee
    prev=[0x16a0], succ=[]
    =================================
    0x4ef: STOP 

}

function proxiableUUID()() public {
    Begin block 0x4f0
    prev=[], succ=[0x16e6]
    =================================
    0x4f1: v4f1(0x4f8) = CONST 
    0x4f4: v4f4(0x16e6) = CONST 
    0x4f7: JUMP v4f4(0x16e6)

    Begin block 0x16e6
    prev=[0x4f0], succ=[0x4f8]
    =================================
    0x16e7: v16e7(0x0) = CONST 
    0x16e9: v16e9(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x170a: v170a(0x0) = CONST 
    0x170c: v170c(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = SHL v170a(0x0), v16e9(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x1710: JUMP v4f1(0x4f8)

    Begin block 0x4f8
    prev=[0x16e6], succ=[]
    =================================
    0x4f9: v4f9(0x40) = CONST 
    0x4fb: v4fb = MLOAD v4f9(0x40)
    0x4ff: MSTORE v4fb, v170c(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x500: v500(0x20) = CONST 
    0x502: v502 = ADD v500(0x20), v4fb
    0x506: v506(0x40) = CONST 
    0x508: v508 = MLOAD v506(0x40)
    0x50b: v50b(0x20) = SUB v502, v508
    0x50d: RETURN v508, v50b(0x20)

}

function setMultiplier(uint256)() public {
    Begin block 0x50e
    prev=[], succ=[0x520, 0x524]
    =================================
    0x50f: v50f(0x53a) = CONST 
    0x512: v512(0x4) = CONST 
    0x515: v515 = CALLDATASIZE 
    0x516: v516 = SUB v515, v512(0x4)
    0x517: v517(0x20) = CONST 
    0x51a: v51a = LT v516, v517(0x20)
    0x51b: v51b = ISZERO v51a
    0x51c: v51c(0x524) = CONST 
    0x51f: JUMPI v51c(0x524), v51b

    Begin block 0x520
    prev=[0x50e], succ=[]
    =================================
    0x520: v520(0x0) = CONST 
    0x523: REVERT v520(0x0), v520(0x0)

    Begin block 0x524
    prev=[0x50e], succ=[0x1711]
    =================================
    0x526: v526 = ADD v512(0x4), v516
    0x52a: v52a = CALLDATALOAD v512(0x4)
    0x52c: v52c(0x20) = CONST 
    0x52e: v52e(0x24) = ADD v52c(0x20), v512(0x4)
    0x536: v536(0x1711) = CONST 
    0x539: JUMP v536(0x1711)

    Begin block 0x1711
    prev=[0x524], succ=[0x1767, 0x17d4]
    =================================
    0x1712: v1712(0x6) = CONST 
    0x1714: v1714(0x0) = CONST 
    0x1717: v1717 = SLOAD v1712(0x6)
    0x1719: v1719(0x100) = CONST 
    0x171c: v171c(0x1) = EXP v1719(0x100), v1714(0x0)
    0x171e: v171e = DIV v1717, v171c(0x1)
    0x171f: v171f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1734: v1734 = AND v171f(0xffffffffffffffffffffffffffffffffffffffff), v171e
    0x1735: v1735(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x174a: v174a = AND v1735(0xffffffffffffffffffffffffffffffffffffffff), v1734
    0x174b: v174b = CALLER 
    0x174c: v174c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1761: v1761 = AND v174c(0xffffffffffffffffffffffffffffffffffffffff), v174b
    0x1762: v1762 = EQ v1761, v174a
    0x1763: v1763(0x17d4) = CONST 
    0x1766: JUMPI v1763(0x17d4), v1762

    Begin block 0x1767
    prev=[0x1711], succ=[]
    =================================
    0x1767: v1767(0x40) = CONST 
    0x1769: v1769 = MLOAD v1767(0x40)
    0x176a: v176a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x178c: MSTORE v1769, v176a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x178d: v178d(0x4) = CONST 
    0x178f: v178f = ADD v178d(0x4), v1769
    0x1792: v1792(0x20) = CONST 
    0x1794: v1794 = ADD v1792(0x20), v178f
    0x1797: v1797(0x20) = SUB v1794, v178f
    0x1799: MSTORE v178f, v1797(0x20)
    0x179a: v179a(0x15) = CONST 
    0x179d: MSTORE v1794, v179a(0x15)
    0x179e: v179e(0x20) = CONST 
    0x17a0: v17a0 = ADD v179e(0x20), v1794
    0x17a2: v17a2(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x17c4: MSTORE v17a0, v17a2(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x17c6: v17c6(0x20) = CONST 
    0x17c8: v17c8 = ADD v17c6(0x20), v17a0
    0x17cc: v17cc(0x40) = CONST 
    0x17ce: v17ce = MLOAD v17cc(0x40)
    0x17d1: v17d1(0x64) = SUB v17c8, v17ce
    0x17d3: REVERT v17ce, v17d1(0x64)

    Begin block 0x17d4
    prev=[0x1711], succ=[0x17f0, 0x185d]
    =================================
    0x17d5: v17d5(0x0) = CONST 
    0x17d7: v17d7(0x1) = ISZERO v17d5(0x0)
    0x17d8: v17d8(0x0) = ISZERO v17d7(0x1)
    0x17d9: v17d9(0x6) = CONST 
    0x17db: v17db(0x14) = CONST 
    0x17de: v17de = SLOAD v17d9(0x6)
    0x17e0: v17e0(0x100) = CONST 
    0x17e3: v17e3(0x10000000000000000000000000000000000000000) = EXP v17e0(0x100), v17db(0x14)
    0x17e5: v17e5 = DIV v17de, v17e3(0x10000000000000000000000000000000000000000)
    0x17e6: v17e6(0xff) = CONST 
    0x17e8: v17e8 = AND v17e6(0xff), v17e5
    0x17e9: v17e9 = ISZERO v17e8
    0x17ea: v17ea = ISZERO v17e9
    0x17eb: v17eb = EQ v17ea, v17d8(0x0)
    0x17ec: v17ec(0x185d) = CONST 
    0x17ef: JUMPI v17ec(0x185d), v17eb

    Begin block 0x17f0
    prev=[0x17d4], succ=[]
    =================================
    0x17f0: v17f0(0x40) = CONST 
    0x17f2: v17f2 = MLOAD v17f0(0x40)
    0x17f3: v17f3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1815: MSTORE v17f2, v17f3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1816: v1816(0x4) = CONST 
    0x1818: v1818 = ADD v1816(0x4), v17f2
    0x181b: v181b(0x20) = CONST 
    0x181d: v181d = ADD v181b(0x20), v1818
    0x1820: v1820(0x20) = SUB v181d, v1818
    0x1822: MSTORE v1818, v1820(0x20)
    0x1823: v1823(0x16) = CONST 
    0x1826: MSTORE v181d, v1823(0x16)
    0x1827: v1827(0x20) = CONST 
    0x1829: v1829 = ADD v1827(0x20), v181d
    0x182b: v182b(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x184d: MSTORE v1829, v182b(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x184f: v184f(0x20) = CONST 
    0x1851: v1851 = ADD v184f(0x20), v1829
    0x1855: v1855(0x40) = CONST 
    0x1857: v1857 = MLOAD v1855(0x40)
    0x185a: v185a(0x64) = SUB v1851, v1857
    0x185c: REVERT v1857, v185a(0x64)

    Begin block 0x185d
    prev=[0x17d4], succ=[0x1867, 0x18b7]
    =================================
    0x185e: v185e(0x5) = CONST 
    0x1860: v1860 = SLOAD v185e(0x5)
    0x1862: v1862 = GT v52a, v1860
    0x1863: v1863(0x18b7) = CONST 
    0x1866: JUMPI v1863(0x18b7), v1862

    Begin block 0x1867
    prev=[0x185d], succ=[]
    =================================
    0x1867: v1867(0x40) = CONST 
    0x1869: v1869 = MLOAD v1867(0x40)
    0x186a: v186a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x188c: MSTORE v1869, v186a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x188d: v188d(0x4) = CONST 
    0x188f: v188f = ADD v188d(0x4), v1869
    0x1892: v1892(0x20) = CONST 
    0x1894: v1894 = ADD v1892(0x20), v188f
    0x1897: v1897(0x20) = SUB v1894, v188f
    0x1899: MSTORE v188f, v1897(0x20)
    0x189a: v189a(0x39) = CONST 
    0x189d: MSTORE v1894, v189a(0x39)
    0x189e: v189e(0x20) = CONST 
    0x18a0: v18a0 = ADD v189e(0x20), v1894
    0x18a2: v18a2(0x3892) = CONST 
    0x18a5: v18a5(0x39) = CONST 
    0x18a8: CODECOPY v18a0, v18a2(0x3892), v18a5(0x39)
    0x18a9: v18a9(0x40) = CONST 
    0x18ab: v18ab = ADD v18a9(0x40), v18a0
    0x18af: v18af(0x40) = CONST 
    0x18b1: v18b1 = MLOAD v18af(0x40)
    0x18b4: v18b4(0x84) = SUB v18ab, v18b1
    0x18b6: REVERT v18b1, v18b4(0x84)

    Begin block 0x18b7
    prev=[0x185d], succ=[0x53a]
    =================================
    0x18b9: v18b9(0x5) = CONST 
    0x18bd: SSTORE v18b9(0x5), v52a
    0x18bf: v18bf(0xd1ac89bfc464ce49c894c4e2379f1ca2b062aff1a640e929764ac1157fa13f0f) = CONST 
    0x18e0: v18e0(0x5) = CONST 
    0x18e2: v18e2 = SLOAD v18e0(0x5)
    0x18e3: v18e3(0x40) = CONST 
    0x18e5: v18e5 = MLOAD v18e3(0x40)
    0x18e9: MSTORE v18e5, v18e2
    0x18ea: v18ea(0x20) = CONST 
    0x18ec: v18ec = ADD v18ea(0x20), v18e5
    0x18f0: v18f0(0x40) = CONST 
    0x18f2: v18f2 = MLOAD v18f0(0x40)
    0x18f5: v18f5(0x20) = SUB v18ec, v18f2
    0x18f7: LOG1 v18f2, v18f5(0x20), v18bf(0xd1ac89bfc464ce49c894c4e2379f1ca2b062aff1a640e929764ac1157fa13f0f)
    0x18f9: JUMP v50f(0x53a)

    Begin block 0x53a
    prev=[0x18b7], succ=[]
    =================================
    0x53b: STOP 

}

function AddToBlacklist(address)() public {
    Begin block 0x53c
    prev=[], succ=[0x54e, 0x552]
    =================================
    0x53d: v53d(0x57e) = CONST 
    0x540: v540(0x4) = CONST 
    0x543: v543 = CALLDATASIZE 
    0x544: v544 = SUB v543, v540(0x4)
    0x545: v545(0x20) = CONST 
    0x548: v548 = LT v544, v545(0x20)
    0x549: v549 = ISZERO v548
    0x54a: v54a(0x552) = CONST 
    0x54d: JUMPI v54a(0x552), v549

    Begin block 0x54e
    prev=[0x53c], succ=[]
    =================================
    0x54e: v54e(0x0) = CONST 
    0x551: REVERT v54e(0x0), v54e(0x0)

    Begin block 0x552
    prev=[0x53c], succ=[0x18fa]
    =================================
    0x554: v554 = ADD v540(0x4), v544
    0x558: v558 = CALLDATALOAD v540(0x4)
    0x559: v559(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x56e: v56e = AND v559(0xffffffffffffffffffffffffffffffffffffffff), v558
    0x570: v570(0x20) = CONST 
    0x572: v572(0x24) = ADD v570(0x20), v540(0x4)
    0x57a: v57a(0x18fa) = CONST 
    0x57d: JUMP v57a(0x18fa)

    Begin block 0x18fa
    prev=[0x552], succ=[0x1950, 0x19bd]
    =================================
    0x18fb: v18fb(0x6) = CONST 
    0x18fd: v18fd(0x0) = CONST 
    0x1900: v1900 = SLOAD v18fb(0x6)
    0x1902: v1902(0x100) = CONST 
    0x1905: v1905(0x1) = EXP v1902(0x100), v18fd(0x0)
    0x1907: v1907 = DIV v1900, v1905(0x1)
    0x1908: v1908(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x191d: v191d = AND v1908(0xffffffffffffffffffffffffffffffffffffffff), v1907
    0x191e: v191e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1933: v1933 = AND v191e(0xffffffffffffffffffffffffffffffffffffffff), v191d
    0x1934: v1934 = CALLER 
    0x1935: v1935(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x194a: v194a = AND v1935(0xffffffffffffffffffffffffffffffffffffffff), v1934
    0x194b: v194b = EQ v194a, v1933
    0x194c: v194c(0x19bd) = CONST 
    0x194f: JUMPI v194c(0x19bd), v194b

    Begin block 0x1950
    prev=[0x18fa], succ=[]
    =================================
    0x1950: v1950(0x40) = CONST 
    0x1952: v1952 = MLOAD v1950(0x40)
    0x1953: v1953(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1975: MSTORE v1952, v1953(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1976: v1976(0x4) = CONST 
    0x1978: v1978 = ADD v1976(0x4), v1952
    0x197b: v197b(0x20) = CONST 
    0x197d: v197d = ADD v197b(0x20), v1978
    0x1980: v1980(0x20) = SUB v197d, v1978
    0x1982: MSTORE v1978, v1980(0x20)
    0x1983: v1983(0x15) = CONST 
    0x1986: MSTORE v197d, v1983(0x15)
    0x1987: v1987(0x20) = CONST 
    0x1989: v1989 = ADD v1987(0x20), v197d
    0x198b: v198b(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x19ad: MSTORE v1989, v198b(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x19af: v19af(0x20) = CONST 
    0x19b1: v19b1 = ADD v19af(0x20), v1989
    0x19b5: v19b5(0x40) = CONST 
    0x19b7: v19b7 = MLOAD v19b5(0x40)
    0x19ba: v19ba(0x64) = SUB v19b1, v19b7
    0x19bc: REVERT v19b7, v19ba(0x64)

    Begin block 0x19bd
    prev=[0x18fa], succ=[0x57e]
    =================================
    0x19be: v19be(0x1) = CONST 
    0x19c0: v19c0(0x3) = CONST 
    0x19c2: v19c2(0x0) = CONST 
    0x19c5: v19c5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19da: v19da = AND v19c5(0xffffffffffffffffffffffffffffffffffffffff), v56e
    0x19db: v19db(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19f0: v19f0 = AND v19db(0xffffffffffffffffffffffffffffffffffffffff), v19da
    0x19f2: MSTORE v19c2(0x0), v19f0
    0x19f3: v19f3(0x20) = CONST 
    0x19f5: v19f5(0x20) = ADD v19f3(0x20), v19c2(0x0)
    0x19f8: MSTORE v19f5(0x20), v19c0(0x3)
    0x19f9: v19f9(0x20) = CONST 
    0x19fb: v19fb(0x40) = ADD v19f9(0x20), v19f5(0x20)
    0x19fc: v19fc(0x0) = CONST 
    0x19fe: v19fe = SHA3 v19fc(0x0), v19fb(0x40)
    0x19ff: v19ff(0x0) = CONST 
    0x1a01: v1a01(0x100) = CONST 
    0x1a04: v1a04(0x1) = EXP v1a01(0x100), v19ff(0x0)
    0x1a06: v1a06 = SLOAD v19fe
    0x1a08: v1a08(0xff) = CONST 
    0x1a0a: v1a0a(0xff) = MUL v1a08(0xff), v1a04(0x1)
    0x1a0b: v1a0b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1a0a(0xff)
    0x1a0c: v1a0c = AND v1a0b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1a06
    0x1a0f: v1a0f(0x0) = ISZERO v19be(0x1)
    0x1a10: v1a10(0x1) = ISZERO v1a0f(0x0)
    0x1a11: v1a11(0x1) = MUL v1a10(0x1), v1a04(0x1)
    0x1a12: v1a12 = OR v1a11(0x1), v1a0c
    0x1a14: SSTORE v19fe, v1a12
    0x1a17: v1a17(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a2c: v1a2c = AND v1a17(0xffffffffffffffffffffffffffffffffffffffff), v56e
    0x1a2d: v1a2d(0x20fe26e62bba36b5afff8a39e3e59ba2b90f6f0b963037740d55af2d93dd3435) = CONST 
    0x1a4e: v1a4e(0x1) = CONST 
    0x1a50: v1a50(0x40) = CONST 
    0x1a52: v1a52 = MLOAD v1a50(0x40)
    0x1a55: v1a55(0x0) = ISZERO v1a4e(0x1)
    0x1a56: v1a56(0x1) = ISZERO v1a55(0x0)
    0x1a58: MSTORE v1a52, v1a56(0x1)
    0x1a59: v1a59(0x20) = CONST 
    0x1a5b: v1a5b = ADD v1a59(0x20), v1a52
    0x1a5f: v1a5f(0x40) = CONST 
    0x1a61: v1a61 = MLOAD v1a5f(0x40)
    0x1a64: v1a64(0x20) = SUB v1a5b, v1a61
    0x1a66: LOG2 v1a61, v1a64(0x20), v1a2d(0x20fe26e62bba36b5afff8a39e3e59ba2b90f6f0b963037740d55af2d93dd3435), v1a2c
    0x1a68: JUMP v53d(0x57e)

    Begin block 0x57e
    prev=[0x19bd], succ=[]
    =================================
    0x57f: STOP 

}

function balanceOf(address)() public {
    Begin block 0x580
    prev=[], succ=[0x592, 0x596]
    =================================
    0x581: v581(0x5c2) = CONST 
    0x584: v584(0x4) = CONST 
    0x587: v587 = CALLDATASIZE 
    0x588: v588 = SUB v587, v584(0x4)
    0x589: v589(0x20) = CONST 
    0x58c: v58c = LT v588, v589(0x20)
    0x58d: v58d = ISZERO v58c
    0x58e: v58e(0x596) = CONST 
    0x591: JUMPI v58e(0x596), v58d

    Begin block 0x592
    prev=[0x580], succ=[]
    =================================
    0x592: v592(0x0) = CONST 
    0x595: REVERT v592(0x0), v592(0x0)

    Begin block 0x596
    prev=[0x580], succ=[0x1a69]
    =================================
    0x598: v598 = ADD v584(0x4), v588
    0x59c: v59c = CALLDATALOAD v584(0x4)
    0x59d: v59d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b2: v5b2 = AND v59d(0xffffffffffffffffffffffffffffffffffffffff), v59c
    0x5b4: v5b4(0x20) = CONST 
    0x5b6: v5b6(0x24) = ADD v5b4(0x20), v584(0x4)
    0x5be: v5be(0x1a69) = CONST 
    0x5c1: JUMP v5be(0x1a69)

    Begin block 0x1a69
    prev=[0x596], succ=[0x1acc]
    =================================
    0x1a6a: v1a6a(0x0) = CONST 
    0x1a6d: v1a6d(0x1ada) = CONST 
    0x1a70: v1a70(0xde0b6b3a7640000) = CONST 
    0x1a79: v1a79(0x1acc) = CONST 
    0x1a7c: v1a7c(0x5) = CONST 
    0x1a7e: v1a7e = SLOAD v1a7c(0x5)
    0x1a7f: v1a7f(0x1) = CONST 
    0x1a81: v1a81(0x0) = CONST 
    0x1a84: v1a84(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a99: v1a99 = AND v1a84(0xffffffffffffffffffffffffffffffffffffffff), v5b2
    0x1a9a: v1a9a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1aaf: v1aaf = AND v1a9a(0xffffffffffffffffffffffffffffffffffffffff), v1a99
    0x1ab1: MSTORE v1a81(0x0), v1aaf
    0x1ab2: v1ab2(0x20) = CONST 
    0x1ab4: v1ab4(0x20) = ADD v1ab2(0x20), v1a81(0x0)
    0x1ab7: MSTORE v1ab4(0x20), v1a7f(0x1)
    0x1ab8: v1ab8(0x20) = CONST 
    0x1aba: v1aba(0x40) = ADD v1ab8(0x20), v1ab4(0x20)
    0x1abb: v1abb(0x0) = CONST 
    0x1abd: v1abd = SHA3 v1abb(0x0), v1aba(0x40)
    0x1abe: v1abe = SLOAD v1abd
    0x1abf: v1abf(0x2c98) = CONST 
    0x1ac5: v1ac5(0xffffffff) = CONST 
    0x1aca: v1aca(0x2c98) = AND v1ac5(0xffffffff), v1abf(0x2c98)
    0x1acb: v1acb_0 = CALLPRIVATE v1aca(0x2c98), v1a7e, v1abe, v1a79(0x1acc)

    Begin block 0x1acc
    prev=[0x1a69], succ=[0x1ada]
    =================================
    0x1acd: v1acd(0x2d1e) = CONST 
    0x1ad3: v1ad3(0xffffffff) = CONST 
    0x1ad8: v1ad8(0x2d1e) = AND v1ad3(0xffffffff), v1acd(0x2d1e)
    0x1ad9: v1ad9_0 = CALLPRIVATE v1ad8(0x2d1e), v1a70(0xde0b6b3a7640000), v1acb_0, v1a6d(0x1ada)

    Begin block 0x1ada
    prev=[0x1acc], succ=[0x5c2]
    =================================
    0x1ae4: JUMP v581(0x5c2)

    Begin block 0x5c2
    prev=[0x1ada], succ=[]
    =================================
    0x5c3: v5c3(0x40) = CONST 
    0x5c5: v5c5 = MLOAD v5c3(0x40)
    0x5c9: MSTORE v5c5, v1ad9_0
    0x5ca: v5ca(0x20) = CONST 
    0x5cc: v5cc = ADD v5ca(0x20), v5c5
    0x5d0: v5d0(0x40) = CONST 
    0x5d2: v5d2 = MLOAD v5d0(0x40)
    0x5d5: v5d5(0x20) = SUB v5cc, v5d2
    0x5d7: RETURN v5d2, v5d5(0x20)

}

function pause()() public {
    Begin block 0x5d8
    prev=[], succ=[0x1ae5]
    =================================
    0x5d9: v5d9(0x5e0) = CONST 
    0x5dc: v5dc(0x1ae5) = CONST 
    0x5df: JUMP v5dc(0x1ae5)

    Begin block 0x1ae5
    prev=[0x5d8], succ=[0x1b3b, 0x1ba8]
    =================================
    0x1ae6: v1ae6(0x6) = CONST 
    0x1ae8: v1ae8(0x0) = CONST 
    0x1aeb: v1aeb = SLOAD v1ae6(0x6)
    0x1aed: v1aed(0x100) = CONST 
    0x1af0: v1af0(0x1) = EXP v1aed(0x100), v1ae8(0x0)
    0x1af2: v1af2 = DIV v1aeb, v1af0(0x1)
    0x1af3: v1af3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b08: v1b08 = AND v1af3(0xffffffffffffffffffffffffffffffffffffffff), v1af2
    0x1b09: v1b09(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b1e: v1b1e = AND v1b09(0xffffffffffffffffffffffffffffffffffffffff), v1b08
    0x1b1f: v1b1f = CALLER 
    0x1b20: v1b20(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b35: v1b35 = AND v1b20(0xffffffffffffffffffffffffffffffffffffffff), v1b1f
    0x1b36: v1b36 = EQ v1b35, v1b1e
    0x1b37: v1b37(0x1ba8) = CONST 
    0x1b3a: JUMPI v1b37(0x1ba8), v1b36

    Begin block 0x1b3b
    prev=[0x1ae5], succ=[]
    =================================
    0x1b3b: v1b3b(0x40) = CONST 
    0x1b3d: v1b3d = MLOAD v1b3b(0x40)
    0x1b3e: v1b3e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1b60: MSTORE v1b3d, v1b3e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b61: v1b61(0x4) = CONST 
    0x1b63: v1b63 = ADD v1b61(0x4), v1b3d
    0x1b66: v1b66(0x20) = CONST 
    0x1b68: v1b68 = ADD v1b66(0x20), v1b63
    0x1b6b: v1b6b(0x20) = SUB v1b68, v1b63
    0x1b6d: MSTORE v1b63, v1b6b(0x20)
    0x1b6e: v1b6e(0x15) = CONST 
    0x1b71: MSTORE v1b68, v1b6e(0x15)
    0x1b72: v1b72(0x20) = CONST 
    0x1b74: v1b74 = ADD v1b72(0x20), v1b68
    0x1b76: v1b76(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x1b98: MSTORE v1b74, v1b76(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x1b9a: v1b9a(0x20) = CONST 
    0x1b9c: v1b9c = ADD v1b9a(0x20), v1b74
    0x1ba0: v1ba0(0x40) = CONST 
    0x1ba2: v1ba2 = MLOAD v1ba0(0x40)
    0x1ba5: v1ba5(0x64) = SUB v1b9c, v1ba2
    0x1ba7: REVERT v1ba2, v1ba5(0x64)

    Begin block 0x1ba8
    prev=[0x1ae5], succ=[0x5e0]
    =================================
    0x1ba9: v1ba9(0x1) = CONST 
    0x1bab: v1bab(0x6) = CONST 
    0x1bad: v1bad(0x14) = CONST 
    0x1baf: v1baf(0x100) = CONST 
    0x1bb2: v1bb2(0x10000000000000000000000000000000000000000) = EXP v1baf(0x100), v1bad(0x14)
    0x1bb4: v1bb4 = SLOAD v1bab(0x6)
    0x1bb6: v1bb6(0xff) = CONST 
    0x1bb8: v1bb8(0xff0000000000000000000000000000000000000000) = MUL v1bb6(0xff), v1bb2(0x10000000000000000000000000000000000000000)
    0x1bb9: v1bb9(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v1bb8(0xff0000000000000000000000000000000000000000)
    0x1bba: v1bba = AND v1bb9(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1bb4
    0x1bbd: v1bbd(0x0) = ISZERO v1ba9(0x1)
    0x1bbe: v1bbe(0x1) = ISZERO v1bbd(0x0)
    0x1bbf: v1bbf(0x10000000000000000000000000000000000000000) = MUL v1bbe(0x1), v1bb2(0x10000000000000000000000000000000000000000)
    0x1bc0: v1bc0 = OR v1bbf(0x10000000000000000000000000000000000000000), v1bba
    0x1bc2: SSTORE v1bab(0x6), v1bc0
    0x1bc4: JUMP v5d9(0x5e0)

    Begin block 0x5e0
    prev=[0x1ba8], succ=[]
    =================================
    0x5e1: STOP 

}

function symbol()() public {
    Begin block 0x5e2
    prev=[], succ=[0x1bc5]
    =================================
    0x5e3: v5e3(0x5ea) = CONST 
    0x5e6: v5e6(0x1bc5) = CONST 
    0x5e9: JUMP v5e6(0x1bc5)

    Begin block 0x1bc5
    prev=[0x5e2], succ=[0x5ea]
    =================================
    0x1bc6: v1bc6(0x40) = CONST 
    0x1bc8: v1bc8 = MLOAD v1bc6(0x40)
    0x1bca: v1bca(0x40) = CONST 
    0x1bcc: v1bcc = ADD v1bca(0x40), v1bc8
    0x1bcd: v1bcd(0x40) = CONST 
    0x1bcf: MSTORE v1bcd(0x40), v1bcc
    0x1bd1: v1bd1(0xd) = CONST 
    0x1bd4: MSTORE v1bc8, v1bd1(0xd)
    0x1bd5: v1bd5(0x20) = CONST 
    0x1bd7: v1bd7 = ADD v1bd5(0x20), v1bc8
    0x1bd8: v1bd8(0x4772617065667275697455534400000000000000000000000000000000000000) = CONST 
    0x1bfa: MSTORE v1bd7, v1bd8(0x4772617065667275697455534400000000000000000000000000000000000000)
    0x1bfd: JUMP v5e3(0x5ea)

    Begin block 0x5ea
    prev=[0x1bc5], succ=[0x60f]
    =================================
    0x5eb: v5eb(0x40) = CONST 
    0x5ed: v5ed = MLOAD v5eb(0x40)
    0x5f0: v5f0(0x20) = CONST 
    0x5f2: v5f2 = ADD v5f0(0x20), v5ed
    0x5f5: v5f5(0x20) = SUB v5f2, v5ed
    0x5f7: MSTORE v5ed, v5f5(0x20)
    0x5fb: v5fb(0xd) = MLOAD v1bc8
    0x5fd: MSTORE v5f2, v5fb(0xd)
    0x5fe: v5fe(0x20) = CONST 
    0x600: v600 = ADD v5fe(0x20), v5f2
    0x604: v604(0xd) = MLOAD v1bc8
    0x606: v606(0x20) = CONST 
    0x608: v608 = ADD v606(0x20), v1bc8
    0x60d: v60d(0x0) = CONST 

    Begin block 0x60f
    prev=[0x5ea, 0x618], succ=[0x62a, 0x618]
    =================================
    0x60f_0x0: v60f_0 = PHI v60d(0x0), v623
    0x612: v612 = LT v60f_0, v604(0xd)
    0x613: v613 = ISZERO v612
    0x614: v614(0x62a) = CONST 
    0x617: JUMPI v614(0x62a), v613

    Begin block 0x62a
    prev=[0x60f], succ=[0x657, 0x63e]
    =================================
    0x633: v633 = ADD v604(0xd), v600
    0x635: v635(0x1f) = CONST 
    0x637: v637(0xd) = AND v635(0x1f), v604(0xd)
    0x639: v639 = ISZERO v637(0xd)
    0x63a: v63a(0x657) = CONST 
    0x63d: JUMPI v63a(0x657), v639

    Begin block 0x657
    prev=[0x62a, 0x63e], succ=[]
    =================================
    0x657_0x1: v657_1 = PHI v633, v654
    0x65d: v65d(0x40) = CONST 
    0x65f: v65f = MLOAD v65d(0x40)
    0x662: v662 = SUB v657_1, v65f
    0x664: RETURN v65f, v662

    Begin block 0x63e
    prev=[0x62a], succ=[0x657]
    =================================
    0x640: v640 = SUB v633, v637(0xd)
    0x642: v642 = MLOAD v640
    0x643: v643(0x1) = CONST 
    0x646: v646(0x20) = CONST 
    0x648: v648(0x13) = SUB v646(0x20), v637(0xd)
    0x649: v649(0x100) = CONST 
    0x64c: v64c(0x100000000000000000000000000000000000000) = EXP v649(0x100), v648(0x13)
    0x64d: v64d(0xffffffffffffffffffffffffffffffffffffff) = SUB v64c(0x100000000000000000000000000000000000000), v643(0x1)
    0x64e: v64e = NOT v64d(0xffffffffffffffffffffffffffffffffffffff)
    0x64f: v64f = AND v64e, v642
    0x651: MSTORE v640, v64f
    0x652: v652(0x20) = CONST 
    0x654: v654 = ADD v652(0x20), v640

    Begin block 0x618
    prev=[0x60f], succ=[0x60f]
    =================================
    0x618_0x0: v618_0 = PHI v60d(0x0), v623
    0x61a: v61a = ADD v608, v618_0
    0x61b: v61b = MLOAD v61a
    0x61e: v61e = ADD v600, v618_0
    0x61f: MSTORE v61e, v61b
    0x620: v620(0x20) = CONST 
    0x623: v623 = ADD v618_0, v620(0x20)
    0x626: v626(0x60f) = CONST 
    0x629: JUMP v626(0x60f)

}

function burn(address,uint256)() public {
    Begin block 0x665
    prev=[], succ=[0x677, 0x67b]
    =================================
    0x666: v666(0x6b1) = CONST 
    0x669: v669(0x4) = CONST 
    0x66c: v66c = CALLDATASIZE 
    0x66d: v66d = SUB v66c, v669(0x4)
    0x66e: v66e(0x40) = CONST 
    0x671: v671 = LT v66d, v66e(0x40)
    0x672: v672 = ISZERO v671
    0x673: v673(0x67b) = CONST 
    0x676: JUMPI v673(0x67b), v672

    Begin block 0x677
    prev=[0x665], succ=[]
    =================================
    0x677: v677(0x0) = CONST 
    0x67a: REVERT v677(0x0), v677(0x0)

    Begin block 0x67b
    prev=[0x665], succ=[0x1bfe]
    =================================
    0x67d: v67d = ADD v669(0x4), v66d
    0x681: v681 = CALLDATALOAD v669(0x4)
    0x682: v682(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x697: v697 = AND v682(0xffffffffffffffffffffffffffffffffffffffff), v681
    0x699: v699(0x20) = CONST 
    0x69b: v69b(0x24) = ADD v699(0x20), v669(0x4)
    0x6a1: v6a1 = CALLDATALOAD v69b(0x24)
    0x6a3: v6a3(0x20) = CONST 
    0x6a5: v6a5(0x44) = ADD v6a3(0x20), v69b(0x24)
    0x6ad: v6ad(0x1bfe) = CONST 
    0x6b0: JUMP v6ad(0x1bfe)

    Begin block 0x1bfe
    prev=[0x67b], succ=[0x1c56, 0x1cc3]
    =================================
    0x1bff: v1bff(0x0) = CONST 
    0x1c01: v1c01(0x6) = CONST 
    0x1c03: v1c03(0x0) = CONST 
    0x1c06: v1c06 = SLOAD v1c01(0x6)
    0x1c08: v1c08(0x100) = CONST 
    0x1c0b: v1c0b(0x1) = EXP v1c08(0x100), v1c03(0x0)
    0x1c0d: v1c0d = DIV v1c06, v1c0b(0x1)
    0x1c0e: v1c0e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c23: v1c23 = AND v1c0e(0xffffffffffffffffffffffffffffffffffffffff), v1c0d
    0x1c24: v1c24(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c39: v1c39 = AND v1c24(0xffffffffffffffffffffffffffffffffffffffff), v1c23
    0x1c3a: v1c3a = CALLER 
    0x1c3b: v1c3b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c50: v1c50 = AND v1c3b(0xffffffffffffffffffffffffffffffffffffffff), v1c3a
    0x1c51: v1c51 = EQ v1c50, v1c39
    0x1c52: v1c52(0x1cc3) = CONST 
    0x1c55: JUMPI v1c52(0x1cc3), v1c51

    Begin block 0x1c56
    prev=[0x1bfe], succ=[]
    =================================
    0x1c56: v1c56(0x40) = CONST 
    0x1c58: v1c58 = MLOAD v1c56(0x40)
    0x1c59: v1c59(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c7b: MSTORE v1c58, v1c59(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c7c: v1c7c(0x4) = CONST 
    0x1c7e: v1c7e = ADD v1c7c(0x4), v1c58
    0x1c81: v1c81(0x20) = CONST 
    0x1c83: v1c83 = ADD v1c81(0x20), v1c7e
    0x1c86: v1c86(0x20) = SUB v1c83, v1c7e
    0x1c88: MSTORE v1c7e, v1c86(0x20)
    0x1c89: v1c89(0x15) = CONST 
    0x1c8c: MSTORE v1c83, v1c89(0x15)
    0x1c8d: v1c8d(0x20) = CONST 
    0x1c8f: v1c8f = ADD v1c8d(0x20), v1c83
    0x1c91: v1c91(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x1cb3: MSTORE v1c8f, v1c91(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x1cb5: v1cb5(0x20) = CONST 
    0x1cb7: v1cb7 = ADD v1cb5(0x20), v1c8f
    0x1cbb: v1cbb(0x40) = CONST 
    0x1cbd: v1cbd = MLOAD v1cbb(0x40)
    0x1cc0: v1cc0(0x64) = SUB v1cb7, v1cbd
    0x1cc2: REVERT v1cbd, v1cc0(0x64)

    Begin block 0x1cc3
    prev=[0x1bfe], succ=[0x1cdf, 0x1d4c]
    =================================
    0x1cc4: v1cc4(0x0) = CONST 
    0x1cc6: v1cc6(0x1) = ISZERO v1cc4(0x0)
    0x1cc7: v1cc7(0x0) = ISZERO v1cc6(0x1)
    0x1cc8: v1cc8(0x6) = CONST 
    0x1cca: v1cca(0x14) = CONST 
    0x1ccd: v1ccd = SLOAD v1cc8(0x6)
    0x1ccf: v1ccf(0x100) = CONST 
    0x1cd2: v1cd2(0x10000000000000000000000000000000000000000) = EXP v1ccf(0x100), v1cca(0x14)
    0x1cd4: v1cd4 = DIV v1ccd, v1cd2(0x10000000000000000000000000000000000000000)
    0x1cd5: v1cd5(0xff) = CONST 
    0x1cd7: v1cd7 = AND v1cd5(0xff), v1cd4
    0x1cd8: v1cd8 = ISZERO v1cd7
    0x1cd9: v1cd9 = ISZERO v1cd8
    0x1cda: v1cda = EQ v1cd9, v1cc7(0x0)
    0x1cdb: v1cdb(0x1d4c) = CONST 
    0x1cde: JUMPI v1cdb(0x1d4c), v1cda

    Begin block 0x1cdf
    prev=[0x1cc3], succ=[]
    =================================
    0x1cdf: v1cdf(0x40) = CONST 
    0x1ce1: v1ce1 = MLOAD v1cdf(0x40)
    0x1ce2: v1ce2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d04: MSTORE v1ce1, v1ce2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d05: v1d05(0x4) = CONST 
    0x1d07: v1d07 = ADD v1d05(0x4), v1ce1
    0x1d0a: v1d0a(0x20) = CONST 
    0x1d0c: v1d0c = ADD v1d0a(0x20), v1d07
    0x1d0f: v1d0f(0x20) = SUB v1d0c, v1d07
    0x1d11: MSTORE v1d07, v1d0f(0x20)
    0x1d12: v1d12(0x16) = CONST 
    0x1d15: MSTORE v1d0c, v1d12(0x16)
    0x1d16: v1d16(0x20) = CONST 
    0x1d18: v1d18 = ADD v1d16(0x20), v1d0c
    0x1d1a: v1d1a(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x1d3c: MSTORE v1d18, v1d1a(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x1d3e: v1d3e(0x20) = CONST 
    0x1d40: v1d40 = ADD v1d3e(0x20), v1d18
    0x1d44: v1d44(0x40) = CONST 
    0x1d46: v1d46 = MLOAD v1d44(0x40)
    0x1d49: v1d49(0x64) = SUB v1d40, v1d46
    0x1d4b: REVERT v1d46, v1d49(0x64)

    Begin block 0x1d4c
    prev=[0x1cc3], succ=[0x1d73]
    =================================
    0x1d4d: v1d4d(0x0) = CONST 
    0x1d53: v1d53(0x1d81) = CONST 
    0x1d56: v1d56(0x5) = CONST 
    0x1d58: v1d58 = SLOAD v1d56(0x5)
    0x1d59: v1d59(0x1d73) = CONST 
    0x1d5c: v1d5c(0xde0b6b3a7640000) = CONST 
    0x1d66: v1d66(0x2c98) = CONST 
    0x1d6c: v1d6c(0xffffffff) = CONST 
    0x1d71: v1d71(0x2c98) = AND v1d6c(0xffffffff), v1d66(0x2c98)
    0x1d72: v1d72_0 = CALLPRIVATE v1d71(0x2c98), v1d5c(0xde0b6b3a7640000), v6a1, v1d59(0x1d73)

    Begin block 0x1d73
    prev=[0x1d4c], succ=[0x1d81]
    =================================
    0x1d74: v1d74(0x2d1e) = CONST 
    0x1d7a: v1d7a(0xffffffff) = CONST 
    0x1d7f: v1d7f(0x2d1e) = AND v1d7a(0xffffffff), v1d74(0x2d1e)
    0x1d80: v1d80_0 = CALLPRIVATE v1d7f(0x2d1e), v1d58, v1d72_0, v1d53(0x1d81)

    Begin block 0x1d81
    prev=[0x1d73], succ=[0x34a2]
    =================================
    0x1d84: v1d84(0x1d8e) = CONST 
    0x1d8a: v1d8a(0x34a2) = CONST 
    0x1d8d: JUMP v1d8a(0x34a2)

    Begin block 0x34a2
    prev=[0x1d81], succ=[0x34d8, 0x3528]
    =================================
    0x34a3: v34a3(0x0) = CONST 
    0x34a5: v34a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x34ba: v34ba(0x0) = AND v34a5(0xffffffffffffffffffffffffffffffffffffffff), v34a3(0x0)
    0x34bc: v34bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x34d1: v34d1 = AND v34bc(0xffffffffffffffffffffffffffffffffffffffff), v697
    0x34d2: v34d2 = EQ v34d1, v34ba(0x0)
    0x34d3: v34d3 = ISZERO v34d2
    0x34d4: v34d4(0x3528) = CONST 
    0x34d7: JUMPI v34d4(0x3528), v34d3

    Begin block 0x34d8
    prev=[0x34a2], succ=[]
    =================================
    0x34d8: v34d8(0x40) = CONST 
    0x34da: v34da = MLOAD v34d8(0x40)
    0x34db: v34db(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x34fd: MSTORE v34da, v34db(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x34fe: v34fe(0x4) = CONST 
    0x3500: v3500 = ADD v34fe(0x4), v34da
    0x3503: v3503(0x20) = CONST 
    0x3505: v3505 = ADD v3503(0x20), v3500
    0x3508: v3508(0x20) = SUB v3505, v3500
    0x350a: MSTORE v3500, v3508(0x20)
    0x350b: v350b(0x21) = CONST 
    0x350e: MSTORE v3505, v350b(0x21)
    0x350f: v350f(0x20) = CONST 
    0x3511: v3511 = ADD v350f(0x20), v3505
    0x3513: v3513(0x38cb) = CONST 
    0x3516: v3516(0x21) = CONST 
    0x3519: CODECOPY v3511, v3513(0x38cb), v3516(0x21)
    0x351a: v351a(0x40) = CONST 
    0x351c: v351c = ADD v351a(0x40), v3511
    0x3520: v3520(0x40) = CONST 
    0x3522: v3522 = MLOAD v3520(0x40)
    0x3525: v3525(0x84) = SUB v351c, v3522
    0x3527: REVERT v3522, v3525(0x84)

    Begin block 0x3528
    prev=[0x34a2], succ=[0x3594]
    =================================
    0x3529: v3529(0x3594) = CONST 
    0x352d: v352d(0x40) = CONST 
    0x352f: v352f = MLOAD v352d(0x40)
    0x3531: v3531(0x60) = CONST 
    0x3533: v3533 = ADD v3531(0x60), v352f
    0x3534: v3534(0x40) = CONST 
    0x3536: MSTORE v3534(0x40), v3533
    0x3538: v3538(0x26) = CONST 
    0x353b: MSTORE v352f, v3538(0x26)
    0x353c: v353c(0x20) = CONST 
    0x353e: v353e = ADD v353c(0x20), v352f
    0x353f: v353f(0x37fa) = CONST 
    0x3542: v3542(0x26) = CONST 
    0x3545: CODECOPY v353e, v353f(0x37fa), v3542(0x26)
    0x3546: v3546(0x1) = CONST 
    0x3548: v3548(0x0) = CONST 
    0x354b: v354b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3560: v3560 = AND v354b(0xffffffffffffffffffffffffffffffffffffffff), v697
    0x3561: v3561(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3576: v3576 = AND v3561(0xffffffffffffffffffffffffffffffffffffffff), v3560
    0x3578: MSTORE v3548(0x0), v3576
    0x3579: v3579(0x20) = CONST 
    0x357b: v357b(0x20) = ADD v3579(0x20), v3548(0x0)
    0x357e: MSTORE v357b(0x20), v3546(0x1)
    0x357f: v357f(0x20) = CONST 
    0x3581: v3581(0x40) = ADD v357f(0x20), v357b(0x20)
    0x3582: v3582(0x0) = CONST 
    0x3584: v3584 = SHA3 v3582(0x0), v3581(0x40)
    0x3585: v3585 = SLOAD v3584
    0x3586: v3586(0x305e) = CONST 
    0x358d: v358d(0xffffffff) = CONST 
    0x3592: v3592(0x305e) = AND v358d(0xffffffff), v3586(0x305e)
    0x3593: v3593_0 = CALLPRIVATE v3592(0x305e), v352f, v1d80_0, v3585, v3529(0x3594)

    Begin block 0x3594
    prev=[0x3528], succ=[0x373fB0x3594]
    =================================
    0x3595: v3595(0x1) = CONST 
    0x3597: v3597(0x0) = CONST 
    0x359a: v359a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x35af: v35af = AND v359a(0xffffffffffffffffffffffffffffffffffffffff), v697
    0x35b0: v35b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x35c5: v35c5 = AND v35b0(0xffffffffffffffffffffffffffffffffffffffff), v35af
    0x35c7: MSTORE v3597(0x0), v35c5
    0x35c8: v35c8(0x20) = CONST 
    0x35ca: v35ca(0x20) = ADD v35c8(0x20), v3597(0x0)
    0x35cd: MSTORE v35ca(0x20), v3595(0x1)
    0x35ce: v35ce(0x20) = CONST 
    0x35d0: v35d0(0x40) = ADD v35ce(0x20), v35ca(0x20)
    0x35d1: v35d1(0x0) = CONST 
    0x35d3: v35d3 = SHA3 v35d1(0x0), v35d0(0x40)
    0x35d6: SSTORE v35d3, v3593_0
    0x35d8: v35d8(0x35ec) = CONST 
    0x35dc: v35dc(0x4) = CONST 
    0x35de: v35de = SLOAD v35dc(0x4)
    0x35df: v35df(0x373f) = CONST 
    0x35e5: v35e5(0xffffffff) = CONST 
    0x35ea: v35ea(0x373f) = AND v35e5(0xffffffff), v35df(0x373f)
    0x35eb: JUMP v35ea(0x373f)

    Begin block 0x373fB0x3594
    prev=[0x3594], succ=[0x3781B0x3594]
    =================================
    0x3740S0x3594: v3740V3594(0x0) = CONST 
    0x3742S0x3594: v3742V3594(0x3781) = CONST 
    0x3747S0x3594: v3747V3594(0x40) = CONST 
    0x3749S0x3594: v3749V3594 = MLOAD v3747V3594(0x40)
    0x374bS0x3594: v374bV3594(0x40) = CONST 
    0x374dS0x3594: v374dV3594 = ADD v374bV3594(0x40), v3749V3594
    0x374eS0x3594: v374eV3594(0x40) = CONST 
    0x3750S0x3594: MSTORE v374eV3594(0x40), v374dV3594
    0x3752S0x3594: v3752V3594(0x1e) = CONST 
    0x3755S0x3594: MSTORE v3749V3594, v3752V3594(0x1e)
    0x3756S0x3594: v3756V3594(0x20) = CONST 
    0x3758S0x3594: v3758V3594 = ADD v3756V3594(0x20), v3749V3594
    0x3759S0x3594: v3759V3594(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x377bS0x3594: MSTORE v3758V3594, v3759V3594(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x377dS0x3594: v377dV3594(0x305e) = CONST 
    0x3780S0x3594: v3780_0V3594 = CALLPRIVATE v377dV3594(0x305e), v3749V3594, v1d80_0, v35de, v3742V3594(0x3781)

    Begin block 0x3781B0x3594
    prev=[0x373fB0x3594], succ=[0x35ec]
    =================================
    0x3788S0x3594: JUMP v35d8(0x35ec)

    Begin block 0x35ec
    prev=[0x3781B0x3594], succ=[0x1d8e]
    =================================
    0x35ed: v35ed(0x4) = CONST 
    0x35f1: SSTORE v35ed(0x4), v3780_0V3594
    0x35f3: v35f3(0x0) = CONST 
    0x35f5: v35f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x360a: v360a(0x0) = AND v35f5(0xffffffffffffffffffffffffffffffffffffffff), v35f3(0x0)
    0x360c: v360c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3621: v3621 = AND v360c(0xffffffffffffffffffffffffffffffffffffffff), v697
    0x3622: v3622(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x3644: v3644(0x40) = CONST 
    0x3646: v3646 = MLOAD v3644(0x40)
    0x364a: MSTORE v3646, v6a1
    0x364b: v364b(0x20) = CONST 
    0x364d: v364d = ADD v364b(0x20), v3646
    0x3651: v3651(0x40) = CONST 
    0x3653: v3653 = MLOAD v3651(0x40)
    0x3656: v3656(0x20) = SUB v364d, v3653
    0x3658: LOG3 v3653, v3656(0x20), v3622(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v3621, v360a(0x0)
    0x365c: JUMP v1d84(0x1d8e)

    Begin block 0x1d8e
    prev=[0x35ec], succ=[0x6b1]
    =================================
    0x1d8f: v1d8f(0x1) = CONST 
    0x1d99: JUMP v666(0x6b1)

    Begin block 0x6b1
    prev=[0x1d8e], succ=[]
    =================================
    0x6b2: v6b2(0x40) = CONST 
    0x6b4: v6b4 = MLOAD v6b2(0x40)
    0x6b7: v6b7 = ISZERO v1d8f(0x1)
    0x6b8: v6b8 = ISZERO v6b7
    0x6ba: MSTORE v6b4, v6b8
    0x6bb: v6bb(0x20) = CONST 
    0x6bd: v6bd = ADD v6bb(0x20), v6b4
    0x6c1: v6c1(0x40) = CONST 
    0x6c3: v6c3 = MLOAD v6c1(0x40)
    0x6c6: v6c6(0x20) = SUB v6bd, v6c3
    0x6c8: RETURN v6c3, v6c6(0x20)

}

function decreaseAllowance(address,uint256)() public {
    Begin block 0x6c9
    prev=[], succ=[0x6db, 0x6df]
    =================================
    0x6ca: v6ca(0x715) = CONST 
    0x6cd: v6cd(0x4) = CONST 
    0x6d0: v6d0 = CALLDATASIZE 
    0x6d1: v6d1 = SUB v6d0, v6cd(0x4)
    0x6d2: v6d2(0x40) = CONST 
    0x6d5: v6d5 = LT v6d1, v6d2(0x40)
    0x6d6: v6d6 = ISZERO v6d5
    0x6d7: v6d7(0x6df) = CONST 
    0x6da: JUMPI v6d7(0x6df), v6d6

    Begin block 0x6db
    prev=[0x6c9], succ=[]
    =================================
    0x6db: v6db(0x0) = CONST 
    0x6de: REVERT v6db(0x0), v6db(0x0)

    Begin block 0x6df
    prev=[0x6c9], succ=[0x1d9a]
    =================================
    0x6e1: v6e1 = ADD v6cd(0x4), v6d1
    0x6e5: v6e5 = CALLDATALOAD v6cd(0x4)
    0x6e6: v6e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6fb: v6fb = AND v6e6(0xffffffffffffffffffffffffffffffffffffffff), v6e5
    0x6fd: v6fd(0x20) = CONST 
    0x6ff: v6ff(0x24) = ADD v6fd(0x20), v6cd(0x4)
    0x705: v705 = CALLDATALOAD v6ff(0x24)
    0x707: v707(0x20) = CONST 
    0x709: v709(0x44) = ADD v707(0x20), v6ff(0x24)
    0x711: v711(0x1d9a) = CONST 
    0x714: JUMP v711(0x1d9a)

    Begin block 0x1d9a
    prev=[0x6df], succ=[0x1df0, 0x1e5d]
    =================================
    0x1d9b: v1d9b(0x0) = CONST 
    0x1d9e: v1d9e(0x3) = CONST 
    0x1da0: v1da0(0x0) = CONST 
    0x1da3: v1da3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1db8: v1db8 = AND v1da3(0xffffffffffffffffffffffffffffffffffffffff), v6fb
    0x1db9: v1db9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dce: v1dce = AND v1db9(0xffffffffffffffffffffffffffffffffffffffff), v1db8
    0x1dd0: MSTORE v1da0(0x0), v1dce
    0x1dd1: v1dd1(0x20) = CONST 
    0x1dd3: v1dd3(0x20) = ADD v1dd1(0x20), v1da0(0x0)
    0x1dd6: MSTORE v1dd3(0x20), v1d9e(0x3)
    0x1dd7: v1dd7(0x20) = CONST 
    0x1dd9: v1dd9(0x40) = ADD v1dd7(0x20), v1dd3(0x20)
    0x1dda: v1dda(0x0) = CONST 
    0x1ddc: v1ddc = SHA3 v1dda(0x0), v1dd9(0x40)
    0x1ddd: v1ddd(0x0) = CONST 
    0x1de0: v1de0 = SLOAD v1ddc
    0x1de2: v1de2(0x100) = CONST 
    0x1de5: v1de5(0x1) = EXP v1de2(0x100), v1ddd(0x0)
    0x1de7: v1de7 = DIV v1de0, v1de5(0x1)
    0x1de8: v1de8(0xff) = CONST 
    0x1dea: v1dea = AND v1de8(0xff), v1de7
    0x1deb: v1deb = ISZERO v1dea
    0x1dec: v1dec(0x1e5d) = CONST 
    0x1def: JUMPI v1dec(0x1e5d), v1deb

    Begin block 0x1df0
    prev=[0x1d9a], succ=[]
    =================================
    0x1df0: v1df0(0x40) = CONST 
    0x1df2: v1df2 = MLOAD v1df0(0x40)
    0x1df3: v1df3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e15: MSTORE v1df2, v1df3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e16: v1e16(0x4) = CONST 
    0x1e18: v1e18 = ADD v1e16(0x4), v1df2
    0x1e1b: v1e1b(0x20) = CONST 
    0x1e1d: v1e1d = ADD v1e1b(0x20), v1e18
    0x1e20: v1e20(0x20) = SUB v1e1d, v1e18
    0x1e22: MSTORE v1e18, v1e20(0x20)
    0x1e23: v1e23(0x16) = CONST 
    0x1e26: MSTORE v1e1d, v1e23(0x16)
    0x1e27: v1e27(0x20) = CONST 
    0x1e29: v1e29 = ADD v1e27(0x20), v1e1d
    0x1e2b: v1e2b(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0x1e4d: MSTORE v1e29, v1e2b(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0x1e4f: v1e4f(0x20) = CONST 
    0x1e51: v1e51 = ADD v1e4f(0x20), v1e29
    0x1e55: v1e55(0x40) = CONST 
    0x1e57: v1e57 = MLOAD v1e55(0x40)
    0x1e5a: v1e5a(0x64) = SUB v1e51, v1e57
    0x1e5c: REVERT v1e57, v1e5a(0x64)

    Begin block 0x1e5d
    prev=[0x1d9a], succ=[0x1eb1, 0x1f1e]
    =================================
    0x1e5e: v1e5e = CALLER 
    0x1e5f: v1e5f(0x3) = CONST 
    0x1e61: v1e61(0x0) = CONST 
    0x1e64: v1e64(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e79: v1e79 = AND v1e64(0xffffffffffffffffffffffffffffffffffffffff), v1e5e
    0x1e7a: v1e7a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e8f: v1e8f = AND v1e7a(0xffffffffffffffffffffffffffffffffffffffff), v1e79
    0x1e91: MSTORE v1e61(0x0), v1e8f
    0x1e92: v1e92(0x20) = CONST 
    0x1e94: v1e94(0x20) = ADD v1e92(0x20), v1e61(0x0)
    0x1e97: MSTORE v1e94(0x20), v1e5f(0x3)
    0x1e98: v1e98(0x20) = CONST 
    0x1e9a: v1e9a(0x40) = ADD v1e98(0x20), v1e94(0x20)
    0x1e9b: v1e9b(0x0) = CONST 
    0x1e9d: v1e9d = SHA3 v1e9b(0x0), v1e9a(0x40)
    0x1e9e: v1e9e(0x0) = CONST 
    0x1ea1: v1ea1 = SLOAD v1e9d
    0x1ea3: v1ea3(0x100) = CONST 
    0x1ea6: v1ea6(0x1) = EXP v1ea3(0x100), v1e9e(0x0)
    0x1ea8: v1ea8 = DIV v1ea1, v1ea6(0x1)
    0x1ea9: v1ea9(0xff) = CONST 
    0x1eab: v1eab = AND v1ea9(0xff), v1ea8
    0x1eac: v1eac = ISZERO v1eab
    0x1ead: v1ead(0x1f1e) = CONST 
    0x1eb0: JUMPI v1ead(0x1f1e), v1eac

    Begin block 0x1eb1
    prev=[0x1e5d], succ=[]
    =================================
    0x1eb1: v1eb1(0x40) = CONST 
    0x1eb3: v1eb3 = MLOAD v1eb1(0x40)
    0x1eb4: v1eb4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1ed6: MSTORE v1eb3, v1eb4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ed7: v1ed7(0x4) = CONST 
    0x1ed9: v1ed9 = ADD v1ed7(0x4), v1eb3
    0x1edc: v1edc(0x20) = CONST 
    0x1ede: v1ede = ADD v1edc(0x20), v1ed9
    0x1ee1: v1ee1(0x20) = SUB v1ede, v1ed9
    0x1ee3: MSTORE v1ed9, v1ee1(0x20)
    0x1ee4: v1ee4(0x16) = CONST 
    0x1ee7: MSTORE v1ede, v1ee4(0x16)
    0x1ee8: v1ee8(0x20) = CONST 
    0x1eea: v1eea = ADD v1ee8(0x20), v1ede
    0x1eec: v1eec(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0x1f0e: MSTORE v1eea, v1eec(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0x1f10: v1f10(0x20) = CONST 
    0x1f12: v1f12 = ADD v1f10(0x20), v1eea
    0x1f16: v1f16(0x40) = CONST 
    0x1f18: v1f18 = MLOAD v1f16(0x40)
    0x1f1b: v1f1b(0x64) = SUB v1f12, v1f18
    0x1f1d: REVERT v1f18, v1f1b(0x64)

    Begin block 0x1f1e
    prev=[0x1e5d], succ=[0x1f3a, 0x1fa7]
    =================================
    0x1f1f: v1f1f(0x0) = CONST 
    0x1f21: v1f21(0x1) = ISZERO v1f1f(0x0)
    0x1f22: v1f22(0x0) = ISZERO v1f21(0x1)
    0x1f23: v1f23(0x6) = CONST 
    0x1f25: v1f25(0x14) = CONST 
    0x1f28: v1f28 = SLOAD v1f23(0x6)
    0x1f2a: v1f2a(0x100) = CONST 
    0x1f2d: v1f2d(0x10000000000000000000000000000000000000000) = EXP v1f2a(0x100), v1f25(0x14)
    0x1f2f: v1f2f = DIV v1f28, v1f2d(0x10000000000000000000000000000000000000000)
    0x1f30: v1f30(0xff) = CONST 
    0x1f32: v1f32 = AND v1f30(0xff), v1f2f
    0x1f33: v1f33 = ISZERO v1f32
    0x1f34: v1f34 = ISZERO v1f33
    0x1f35: v1f35 = EQ v1f34, v1f22(0x0)
    0x1f36: v1f36(0x1fa7) = CONST 
    0x1f39: JUMPI v1f36(0x1fa7), v1f35

    Begin block 0x1f3a
    prev=[0x1f1e], succ=[]
    =================================
    0x1f3a: v1f3a(0x40) = CONST 
    0x1f3c: v1f3c = MLOAD v1f3a(0x40)
    0x1f3d: v1f3d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f5f: MSTORE v1f3c, v1f3d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f60: v1f60(0x4) = CONST 
    0x1f62: v1f62 = ADD v1f60(0x4), v1f3c
    0x1f65: v1f65(0x20) = CONST 
    0x1f67: v1f67 = ADD v1f65(0x20), v1f62
    0x1f6a: v1f6a(0x20) = SUB v1f67, v1f62
    0x1f6c: MSTORE v1f62, v1f6a(0x20)
    0x1f6d: v1f6d(0x16) = CONST 
    0x1f70: MSTORE v1f67, v1f6d(0x16)
    0x1f71: v1f71(0x20) = CONST 
    0x1f73: v1f73 = ADD v1f71(0x20), v1f67
    0x1f75: v1f75(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x1f97: MSTORE v1f73, v1f75(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x1f99: v1f99(0x20) = CONST 
    0x1f9b: v1f9b = ADD v1f99(0x20), v1f73
    0x1f9f: v1f9f(0x40) = CONST 
    0x1fa1: v1fa1 = MLOAD v1f9f(0x40)
    0x1fa4: v1fa4(0x64) = SUB v1f9b, v1fa1
    0x1fa6: REVERT v1fa1, v1fa4(0x64)

    Begin block 0x1fa7
    prev=[0x1f1e], succ=[0x2d68B0x1fa7]
    =================================
    0x1fa8: v1fa8(0x0) = CONST 
    0x1faa: v1faa(0x1fba) = CONST 
    0x1fad: v1fad(0x1fb4) = CONST 
    0x1fb0: v1fb0(0x2d68) = CONST 
    0x1fb3: JUMP v1fb0(0x2d68)

    Begin block 0x2d68B0x1fa7
    prev=[0x1fa7], succ=[0x1fb4]
    =================================
    0x2d69S0x1fa7: v2d69V1fa7(0x0) = CONST 
    0x2d6bS0x1fa7: v2d6bV1fa7 = CALLER 
    0x2d6fS0x1fa7: JUMP v1fad(0x1fb4)

    Begin block 0x1fb4
    prev=[0x2d68B0x1fa7], succ=[0x1fba]
    =================================
    0x1fb6: v1fb6(0x2540) = CONST 
    0x1fb9: v1fb9_0 = CALLPRIVATE v1fb6(0x2540), v6fb, v2d6bV1fa7, v1faa(0x1fba)

    Begin block 0x1fba
    prev=[0x1fb4], succ=[0x2d68B0x1fba]
    =================================
    0x1fbd: v1fbd(0x1ffa) = CONST 
    0x1fc0: v1fc0(0x1fc7) = CONST 
    0x1fc3: v1fc3(0x2d68) = CONST 
    0x1fc6: JUMP v1fc3(0x2d68)

    Begin block 0x2d68B0x1fba
    prev=[0x1fba], succ=[0x1fc7]
    =================================
    0x2d69S0x1fba: v2d69V1fba(0x0) = CONST 
    0x2d6bS0x1fba: v2d6bV1fba = CALLER 
    0x2d6fS0x1fba: JUMP v1fc0(0x1fc7)

    Begin block 0x1fc7
    prev=[0x2d68B0x1fba], succ=[0x1ff5]
    =================================
    0x1fc9: v1fc9(0x1ff5) = CONST 
    0x1fcd: v1fcd(0x40) = CONST 
    0x1fcf: v1fcf = MLOAD v1fcd(0x40)
    0x1fd1: v1fd1(0x60) = CONST 
    0x1fd3: v1fd3 = ADD v1fd1(0x60), v1fcf
    0x1fd4: v1fd4(0x40) = CONST 
    0x1fd6: MSTORE v1fd4(0x40), v1fd3
    0x1fd8: v1fd8(0x25) = CONST 
    0x1fdb: MSTORE v1fcf, v1fd8(0x25)
    0x1fdc: v1fdc(0x20) = CONST 
    0x1fde: v1fde = ADD v1fdc(0x20), v1fcf
    0x1fdf: v1fdf(0x39a7) = CONST 
    0x1fe2: v1fe2(0x25) = CONST 
    0x1fe5: CODECOPY v1fde, v1fdf(0x39a7), v1fe2(0x25)
    0x1fe7: v1fe7(0x305e) = CONST 
    0x1fee: v1fee(0xffffffff) = CONST 
    0x1ff3: v1ff3(0x305e) = AND v1fee(0xffffffff), v1fe7(0x305e)
    0x1ff4: v1ff4_0 = CALLPRIVATE v1ff3(0x305e), v1fcf, v705, v1fb9_0, v1fc9(0x1ff5)

    Begin block 0x1ff5
    prev=[0x1fc7], succ=[0x1ffa]
    =================================
    0x1ff6: v1ff6(0x29e6) = CONST 
    0x1ff9: CALLPRIVATE v1ff6(0x29e6), v1ff4_0, v6fb, v2d6bV1fba, v1fbd(0x1ffa)

    Begin block 0x1ffa
    prev=[0x1ff5], succ=[0x715]
    =================================
    0x1ffb: v1ffb(0x1) = CONST 
    0x2006: JUMP v6ca(0x715)

    Begin block 0x715
    prev=[0x1ffa], succ=[]
    =================================
    0x716: v716(0x40) = CONST 
    0x718: v718 = MLOAD v716(0x40)
    0x71b: v71b = ISZERO v1ffb(0x1)
    0x71c: v71c = ISZERO v71b
    0x71e: MSTORE v718, v71c
    0x71f: v71f(0x20) = CONST 
    0x721: v721 = ADD v71f(0x20), v718
    0x725: v725(0x40) = CONST 
    0x727: v727 = MLOAD v725(0x40)
    0x72a: v72a(0x20) = SUB v721, v727
    0x72c: RETURN v727, v72a(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x72d
    prev=[], succ=[0x73f, 0x743]
    =================================
    0x72e: v72e(0x779) = CONST 
    0x731: v731(0x4) = CONST 
    0x734: v734 = CALLDATASIZE 
    0x735: v735 = SUB v734, v731(0x4)
    0x736: v736(0x40) = CONST 
    0x739: v739 = LT v735, v736(0x40)
    0x73a: v73a = ISZERO v739
    0x73b: v73b(0x743) = CONST 
    0x73e: JUMPI v73b(0x743), v73a

    Begin block 0x73f
    prev=[0x72d], succ=[]
    =================================
    0x73f: v73f(0x0) = CONST 
    0x742: REVERT v73f(0x0), v73f(0x0)

    Begin block 0x743
    prev=[0x72d], succ=[0x2007]
    =================================
    0x745: v745 = ADD v731(0x4), v735
    0x749: v749 = CALLDATALOAD v731(0x4)
    0x74a: v74a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75f: v75f = AND v74a(0xffffffffffffffffffffffffffffffffffffffff), v749
    0x761: v761(0x20) = CONST 
    0x763: v763(0x24) = ADD v761(0x20), v731(0x4)
    0x769: v769 = CALLDATALOAD v763(0x24)
    0x76b: v76b(0x20) = CONST 
    0x76d: v76d(0x44) = ADD v76b(0x20), v763(0x24)
    0x775: v775(0x2007) = CONST 
    0x778: JUMP v775(0x2007)

    Begin block 0x2007
    prev=[0x743], succ=[0x205d, 0x20ca]
    =================================
    0x2008: v2008(0x0) = CONST 
    0x200a: v200a = CALLER 
    0x200b: v200b(0x3) = CONST 
    0x200d: v200d(0x0) = CONST 
    0x2010: v2010(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2025: v2025 = AND v2010(0xffffffffffffffffffffffffffffffffffffffff), v200a
    0x2026: v2026(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x203b: v203b = AND v2026(0xffffffffffffffffffffffffffffffffffffffff), v2025
    0x203d: MSTORE v200d(0x0), v203b
    0x203e: v203e(0x20) = CONST 
    0x2040: v2040(0x20) = ADD v203e(0x20), v200d(0x0)
    0x2043: MSTORE v2040(0x20), v200b(0x3)
    0x2044: v2044(0x20) = CONST 
    0x2046: v2046(0x40) = ADD v2044(0x20), v2040(0x20)
    0x2047: v2047(0x0) = CONST 
    0x2049: v2049 = SHA3 v2047(0x0), v2046(0x40)
    0x204a: v204a(0x0) = CONST 
    0x204d: v204d = SLOAD v2049
    0x204f: v204f(0x100) = CONST 
    0x2052: v2052(0x1) = EXP v204f(0x100), v204a(0x0)
    0x2054: v2054 = DIV v204d, v2052(0x1)
    0x2055: v2055(0xff) = CONST 
    0x2057: v2057 = AND v2055(0xff), v2054
    0x2058: v2058 = ISZERO v2057
    0x2059: v2059(0x20ca) = CONST 
    0x205c: JUMPI v2059(0x20ca), v2058

    Begin block 0x205d
    prev=[0x2007], succ=[]
    =================================
    0x205d: v205d(0x40) = CONST 
    0x205f: v205f = MLOAD v205d(0x40)
    0x2060: v2060(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2082: MSTORE v205f, v2060(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2083: v2083(0x4) = CONST 
    0x2085: v2085 = ADD v2083(0x4), v205f
    0x2088: v2088(0x20) = CONST 
    0x208a: v208a = ADD v2088(0x20), v2085
    0x208d: v208d(0x20) = SUB v208a, v2085
    0x208f: MSTORE v2085, v208d(0x20)
    0x2090: v2090(0x16) = CONST 
    0x2093: MSTORE v208a, v2090(0x16)
    0x2094: v2094(0x20) = CONST 
    0x2096: v2096 = ADD v2094(0x20), v208a
    0x2098: v2098(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0x20ba: MSTORE v2096, v2098(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0x20bc: v20bc(0x20) = CONST 
    0x20be: v20be = ADD v20bc(0x20), v2096
    0x20c2: v20c2(0x40) = CONST 
    0x20c4: v20c4 = MLOAD v20c2(0x40)
    0x20c7: v20c7(0x64) = SUB v20be, v20c4
    0x20c9: REVERT v20c4, v20c7(0x64)

    Begin block 0x20ca
    prev=[0x2007], succ=[0x211e, 0x218b]
    =================================
    0x20cc: v20cc(0x3) = CONST 
    0x20ce: v20ce(0x0) = CONST 
    0x20d1: v20d1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20e6: v20e6 = AND v20d1(0xffffffffffffffffffffffffffffffffffffffff), v75f
    0x20e7: v20e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20fc: v20fc = AND v20e7(0xffffffffffffffffffffffffffffffffffffffff), v20e6
    0x20fe: MSTORE v20ce(0x0), v20fc
    0x20ff: v20ff(0x20) = CONST 
    0x2101: v2101(0x20) = ADD v20ff(0x20), v20ce(0x0)
    0x2104: MSTORE v2101(0x20), v20cc(0x3)
    0x2105: v2105(0x20) = CONST 
    0x2107: v2107(0x40) = ADD v2105(0x20), v2101(0x20)
    0x2108: v2108(0x0) = CONST 
    0x210a: v210a = SHA3 v2108(0x0), v2107(0x40)
    0x210b: v210b(0x0) = CONST 
    0x210e: v210e = SLOAD v210a
    0x2110: v2110(0x100) = CONST 
    0x2113: v2113(0x1) = EXP v2110(0x100), v210b(0x0)
    0x2115: v2115 = DIV v210e, v2113(0x1)
    0x2116: v2116(0xff) = CONST 
    0x2118: v2118 = AND v2116(0xff), v2115
    0x2119: v2119 = ISZERO v2118
    0x211a: v211a(0x218b) = CONST 
    0x211d: JUMPI v211a(0x218b), v2119

    Begin block 0x211e
    prev=[0x20ca], succ=[]
    =================================
    0x211e: v211e(0x40) = CONST 
    0x2120: v2120 = MLOAD v211e(0x40)
    0x2121: v2121(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2143: MSTORE v2120, v2121(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2144: v2144(0x4) = CONST 
    0x2146: v2146 = ADD v2144(0x4), v2120
    0x2149: v2149(0x20) = CONST 
    0x214b: v214b = ADD v2149(0x20), v2146
    0x214e: v214e(0x20) = SUB v214b, v2146
    0x2150: MSTORE v2146, v214e(0x20)
    0x2151: v2151(0x16) = CONST 
    0x2154: MSTORE v214b, v2151(0x16)
    0x2155: v2155(0x20) = CONST 
    0x2157: v2157 = ADD v2155(0x20), v214b
    0x2159: v2159(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000) = CONST 
    0x217b: MSTORE v2157, v2159(0x6163636f756e7420697320626c61636b6c697374656400000000000000000000)
    0x217d: v217d(0x20) = CONST 
    0x217f: v217f = ADD v217d(0x20), v2157
    0x2183: v2183(0x40) = CONST 
    0x2185: v2185 = MLOAD v2183(0x40)
    0x2188: v2188(0x64) = SUB v217f, v2185
    0x218a: REVERT v2185, v2188(0x64)

    Begin block 0x218b
    prev=[0x20ca], succ=[0x21a7, 0x2214]
    =================================
    0x218c: v218c(0x0) = CONST 
    0x218e: v218e(0x1) = ISZERO v218c(0x0)
    0x218f: v218f(0x0) = ISZERO v218e(0x1)
    0x2190: v2190(0x6) = CONST 
    0x2192: v2192(0x14) = CONST 
    0x2195: v2195 = SLOAD v2190(0x6)
    0x2197: v2197(0x100) = CONST 
    0x219a: v219a(0x10000000000000000000000000000000000000000) = EXP v2197(0x100), v2192(0x14)
    0x219c: v219c = DIV v2195, v219a(0x10000000000000000000000000000000000000000)
    0x219d: v219d(0xff) = CONST 
    0x219f: v219f = AND v219d(0xff), v219c
    0x21a0: v21a0 = ISZERO v219f
    0x21a1: v21a1 = ISZERO v21a0
    0x21a2: v21a2 = EQ v21a1, v218f(0x0)
    0x21a3: v21a3(0x2214) = CONST 
    0x21a6: JUMPI v21a3(0x2214), v21a2

    Begin block 0x21a7
    prev=[0x218b], succ=[]
    =================================
    0x21a7: v21a7(0x40) = CONST 
    0x21a9: v21a9 = MLOAD v21a7(0x40)
    0x21aa: v21aa(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x21cc: MSTORE v21a9, v21aa(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21cd: v21cd(0x4) = CONST 
    0x21cf: v21cf = ADD v21cd(0x4), v21a9
    0x21d2: v21d2(0x20) = CONST 
    0x21d4: v21d4 = ADD v21d2(0x20), v21cf
    0x21d7: v21d7(0x20) = SUB v21d4, v21cf
    0x21d9: MSTORE v21cf, v21d7(0x20)
    0x21da: v21da(0x16) = CONST 
    0x21dd: MSTORE v21d4, v21da(0x16)
    0x21de: v21de(0x20) = CONST 
    0x21e0: v21e0 = ADD v21de(0x20), v21d4
    0x21e2: v21e2(0x74686520636f6e74726163742069732070617573656400000000000000000000) = CONST 
    0x2204: MSTORE v21e0, v21e2(0x74686520636f6e74726163742069732070617573656400000000000000000000)
    0x2206: v2206(0x20) = CONST 
    0x2208: v2208 = ADD v2206(0x20), v21e0
    0x220c: v220c(0x40) = CONST 
    0x220e: v220e = MLOAD v220c(0x40)
    0x2211: v2211(0x64) = SUB v2208, v220e
    0x2213: REVERT v220e, v2211(0x64)

    Begin block 0x2214
    prev=[0x218b], succ=[0x223b]
    =================================
    0x2215: v2215(0x0) = CONST 
    0x221b: v221b(0x2249) = CONST 
    0x221e: v221e(0x5) = CONST 
    0x2220: v2220 = SLOAD v221e(0x5)
    0x2221: v2221(0x223b) = CONST 
    0x2224: v2224(0xde0b6b3a7640000) = CONST 
    0x222e: v222e(0x2c98) = CONST 
    0x2234: v2234(0xffffffff) = CONST 
    0x2239: v2239(0x2c98) = AND v2234(0xffffffff), v222e(0x2c98)
    0x223a: v223a_0 = CALLPRIVATE v2239(0x2c98), v2224(0xde0b6b3a7640000), v769, v2221(0x223b)

    Begin block 0x223b
    prev=[0x2214], succ=[0x2249]
    =================================
    0x223c: v223c(0x2d1e) = CONST 
    0x2242: v2242(0xffffffff) = CONST 
    0x2247: v2247(0x2d1e) = AND v2242(0xffffffff), v223c(0x2d1e)
    0x2248: v2248_0 = CALLPRIVATE v2247(0x2d1e), v2220, v223a_0, v221b(0x2249)

    Begin block 0x2249
    prev=[0x223b], succ=[0x2256]
    =================================
    0x224c: v224c(0x2256) = CONST 
    0x224f: v224f = CALLER 
    0x2252: v2252(0x2d70) = CONST 
    0x2255: CALLPRIVATE v2252(0x2d70), v769, v75f, v224f, v224c(0x2256)

    Begin block 0x2256
    prev=[0x2249], succ=[0x779]
    =================================
    0x2257: v2257(0x1) = CONST 
    0x2263: JUMP v72e(0x779)

    Begin block 0x779
    prev=[0x2256], succ=[]
    =================================
    0x77a: v77a(0x40) = CONST 
    0x77c: v77c = MLOAD v77a(0x40)
    0x77f: v77f = ISZERO v2257(0x1)
    0x780: v780 = ISZERO v77f
    0x782: MSTORE v77c, v780
    0x783: v783(0x20) = CONST 
    0x785: v785 = ADD v783(0x20), v77c
    0x789: v789(0x40) = CONST 
    0x78b: v78b = MLOAD v789(0x40)
    0x78e: v78e(0x20) = SUB v785, v78b
    0x790: RETURN v78b, v78e(0x20)

}

function TransferOwnerShip(address)() public {
    Begin block 0x791
    prev=[], succ=[0x7a3, 0x7a7]
    =================================
    0x792: v792(0x7d3) = CONST 
    0x795: v795(0x4) = CONST 
    0x798: v798 = CALLDATASIZE 
    0x799: v799 = SUB v798, v795(0x4)
    0x79a: v79a(0x20) = CONST 
    0x79d: v79d = LT v799, v79a(0x20)
    0x79e: v79e = ISZERO v79d
    0x79f: v79f(0x7a7) = CONST 
    0x7a2: JUMPI v79f(0x7a7), v79e

    Begin block 0x7a3
    prev=[0x791], succ=[]
    =================================
    0x7a3: v7a3(0x0) = CONST 
    0x7a6: REVERT v7a3(0x0), v7a3(0x0)

    Begin block 0x7a7
    prev=[0x791], succ=[0x2264]
    =================================
    0x7a9: v7a9 = ADD v795(0x4), v799
    0x7ad: v7ad = CALLDATALOAD v795(0x4)
    0x7ae: v7ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7c3: v7c3 = AND v7ae(0xffffffffffffffffffffffffffffffffffffffff), v7ad
    0x7c5: v7c5(0x20) = CONST 
    0x7c7: v7c7(0x24) = ADD v7c5(0x20), v795(0x4)
    0x7cf: v7cf(0x2264) = CONST 
    0x7d2: JUMP v7cf(0x2264)

    Begin block 0x2264
    prev=[0x7a7], succ=[0x22ba, 0x2327]
    =================================
    0x2265: v2265(0x6) = CONST 
    0x2267: v2267(0x0) = CONST 
    0x226a: v226a = SLOAD v2265(0x6)
    0x226c: v226c(0x100) = CONST 
    0x226f: v226f(0x1) = EXP v226c(0x100), v2267(0x0)
    0x2271: v2271 = DIV v226a, v226f(0x1)
    0x2272: v2272(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2287: v2287 = AND v2272(0xffffffffffffffffffffffffffffffffffffffff), v2271
    0x2288: v2288(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x229d: v229d = AND v2288(0xffffffffffffffffffffffffffffffffffffffff), v2287
    0x229e: v229e = CALLER 
    0x229f: v229f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22b4: v22b4 = AND v229f(0xffffffffffffffffffffffffffffffffffffffff), v229e
    0x22b5: v22b5 = EQ v22b4, v229d
    0x22b6: v22b6(0x2327) = CONST 
    0x22b9: JUMPI v22b6(0x2327), v22b5

    Begin block 0x22ba
    prev=[0x2264], succ=[]
    =================================
    0x22ba: v22ba(0x40) = CONST 
    0x22bc: v22bc = MLOAD v22ba(0x40)
    0x22bd: v22bd(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x22df: MSTORE v22bc, v22bd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x22e0: v22e0(0x4) = CONST 
    0x22e2: v22e2 = ADD v22e0(0x4), v22bc
    0x22e5: v22e5(0x20) = CONST 
    0x22e7: v22e7 = ADD v22e5(0x20), v22e2
    0x22ea: v22ea(0x20) = SUB v22e7, v22e2
    0x22ec: MSTORE v22e2, v22ea(0x20)
    0x22ed: v22ed(0x15) = CONST 
    0x22f0: MSTORE v22e7, v22ed(0x15)
    0x22f1: v22f1(0x20) = CONST 
    0x22f3: v22f3 = ADD v22f1(0x20), v22e7
    0x22f5: v22f5(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x2317: MSTORE v22f3, v22f5(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x2319: v2319(0x20) = CONST 
    0x231b: v231b = ADD v2319(0x20), v22f3
    0x231f: v231f(0x40) = CONST 
    0x2321: v2321 = MLOAD v231f(0x40)
    0x2324: v2324(0x64) = SUB v231b, v2321
    0x2326: REVERT v2321, v2324(0x64)

    Begin block 0x2327
    prev=[0x2264], succ=[0x235d, 0x23ca]
    =================================
    0x2328: v2328(0x0) = CONST 
    0x232a: v232a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x233f: v233f(0x0) = AND v232a(0xffffffffffffffffffffffffffffffffffffffff), v2328(0x0)
    0x2341: v2341(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2356: v2356 = AND v2341(0xffffffffffffffffffffffffffffffffffffffff), v7c3
    0x2357: v2357 = EQ v2356, v233f(0x0)
    0x2358: v2358 = ISZERO v2357
    0x2359: v2359(0x23ca) = CONST 
    0x235c: JUMPI v2359(0x23ca), v2358

    Begin block 0x235d
    prev=[0x2327], succ=[]
    =================================
    0x235d: v235d(0x40) = CONST 
    0x235f: v235f = MLOAD v235d(0x40)
    0x2360: v2360(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2382: MSTORE v235f, v2360(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2383: v2383(0x4) = CONST 
    0x2385: v2385 = ADD v2383(0x4), v235f
    0x2388: v2388(0x20) = CONST 
    0x238a: v238a = ADD v2388(0x20), v2385
    0x238d: v238d(0x20) = SUB v238a, v2385
    0x238f: MSTORE v2385, v238d(0x20)
    0x2390: v2390(0x1e) = CONST 
    0x2393: MSTORE v238a, v2390(0x1e)
    0x2394: v2394(0x20) = CONST 
    0x2396: v2396 = ADD v2394(0x20), v238a
    0x2398: v2398(0x6163636f756e742063616e6e6f74206265207a65726f20616464726573730000) = CONST 
    0x23ba: MSTORE v2396, v2398(0x6163636f756e742063616e6e6f74206265207a65726f20616464726573730000)
    0x23bc: v23bc(0x20) = CONST 
    0x23be: v23be = ADD v23bc(0x20), v2396
    0x23c2: v23c2(0x40) = CONST 
    0x23c4: v23c4 = MLOAD v23c2(0x40)
    0x23c7: v23c7(0x64) = SUB v23be, v23c4
    0x23c9: REVERT v23c4, v23c7(0x64)

    Begin block 0x23ca
    prev=[0x2327], succ=[0x2420, 0x248d]
    =================================
    0x23cb: v23cb(0x6) = CONST 
    0x23cd: v23cd(0x0) = CONST 
    0x23d0: v23d0 = SLOAD v23cb(0x6)
    0x23d2: v23d2(0x100) = CONST 
    0x23d5: v23d5(0x1) = EXP v23d2(0x100), v23cd(0x0)
    0x23d7: v23d7 = DIV v23d0, v23d5(0x1)
    0x23d8: v23d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23ed: v23ed = AND v23d8(0xffffffffffffffffffffffffffffffffffffffff), v23d7
    0x23ee: v23ee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2403: v2403 = AND v23ee(0xffffffffffffffffffffffffffffffffffffffff), v23ed
    0x2404: v2404 = CALLER 
    0x2405: v2405(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x241a: v241a = AND v2405(0xffffffffffffffffffffffffffffffffffffffff), v2404
    0x241b: v241b = EQ v241a, v2403
    0x241c: v241c(0x248d) = CONST 
    0x241f: JUMPI v241c(0x248d), v241b

    Begin block 0x2420
    prev=[0x23ca], succ=[]
    =================================
    0x2420: v2420(0x40) = CONST 
    0x2422: v2422 = MLOAD v2420(0x40)
    0x2423: v2423(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2445: MSTORE v2422, v2423(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2446: v2446(0x4) = CONST 
    0x2448: v2448 = ADD v2446(0x4), v2422
    0x244b: v244b(0x20) = CONST 
    0x244d: v244d = ADD v244b(0x20), v2448
    0x2450: v2450(0x20) = SUB v244d, v2448
    0x2452: MSTORE v2448, v2450(0x20)
    0x2453: v2453(0x15) = CONST 
    0x2456: MSTORE v244d, v2453(0x15)
    0x2457: v2457(0x20) = CONST 
    0x2459: v2459 = ADD v2457(0x20), v244d
    0x245b: v245b(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x247d: MSTORE v2459, v245b(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x247f: v247f(0x20) = CONST 
    0x2481: v2481 = ADD v247f(0x20), v2459
    0x2485: v2485(0x40) = CONST 
    0x2487: v2487 = MLOAD v2485(0x40)
    0x248a: v248a(0x64) = SUB v2481, v2487
    0x248c: REVERT v2487, v248a(0x64)

    Begin block 0x248d
    prev=[0x23ca], succ=[0x7d3]
    =================================
    0x248f: v248f(0x6) = CONST 
    0x2491: v2491(0x0) = CONST 
    0x2493: v2493(0x100) = CONST 
    0x2496: v2496(0x1) = EXP v2493(0x100), v2491(0x0)
    0x2498: v2498 = SLOAD v248f(0x6)
    0x249a: v249a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24af: v24af(0xffffffffffffffffffffffffffffffffffffffff) = MUL v249a(0xffffffffffffffffffffffffffffffffffffffff), v2496(0x1)
    0x24b0: v24b0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v24af(0xffffffffffffffffffffffffffffffffffffffff)
    0x24b1: v24b1 = AND v24b0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2498
    0x24b4: v24b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24c9: v24c9 = AND v24b4(0xffffffffffffffffffffffffffffffffffffffff), v7c3
    0x24ca: v24ca = MUL v24c9, v2496(0x1)
    0x24cb: v24cb = OR v24ca, v24b1
    0x24cd: SSTORE v248f(0x6), v24cb
    0x24cf: v24cf(0x7ce7ec0b50378fb6c0186ffb5f48325f6593fcb4ca4386f21861af3129188f5c) = CONST 
    0x24f0: v24f0(0x6) = CONST 
    0x24f2: v24f2(0x0) = CONST 
    0x24f5: v24f5 = SLOAD v24f0(0x6)
    0x24f7: v24f7(0x100) = CONST 
    0x24fa: v24fa(0x1) = EXP v24f7(0x100), v24f2(0x0)
    0x24fc: v24fc = DIV v24f5, v24fa(0x1)
    0x24fd: v24fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2512: v2512 = AND v24fd(0xffffffffffffffffffffffffffffffffffffffff), v24fc
    0x2513: v2513(0x40) = CONST 
    0x2515: v2515 = MLOAD v2513(0x40)
    0x2518: v2518(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x252d: v252d = AND v2518(0xffffffffffffffffffffffffffffffffffffffff), v2512
    0x252f: MSTORE v2515, v252d
    0x2530: v2530(0x20) = CONST 
    0x2532: v2532 = ADD v2530(0x20), v2515
    0x2536: v2536(0x40) = CONST 
    0x2538: v2538 = MLOAD v2536(0x40)
    0x253b: v253b(0x20) = SUB v2532, v2538
    0x253d: LOG1 v2538, v253b(0x20), v24cf(0x7ce7ec0b50378fb6c0186ffb5f48325f6593fcb4ca4386f21861af3129188f5c)
    0x253f: JUMP v792(0x7d3)

    Begin block 0x7d3
    prev=[0x248d], succ=[]
    =================================
    0x7d4: STOP 

}

function allowance(address,address)() public {
    Begin block 0x7d5
    prev=[], succ=[0x7e7, 0x7eb]
    =================================
    0x7d6: v7d6(0x837) = CONST 
    0x7d9: v7d9(0x4) = CONST 
    0x7dc: v7dc = CALLDATASIZE 
    0x7dd: v7dd = SUB v7dc, v7d9(0x4)
    0x7de: v7de(0x40) = CONST 
    0x7e1: v7e1 = LT v7dd, v7de(0x40)
    0x7e2: v7e2 = ISZERO v7e1
    0x7e3: v7e3(0x7eb) = CONST 
    0x7e6: JUMPI v7e3(0x7eb), v7e2

    Begin block 0x7e7
    prev=[0x7d5], succ=[]
    =================================
    0x7e7: v7e7(0x0) = CONST 
    0x7ea: REVERT v7e7(0x0), v7e7(0x0)

    Begin block 0x7eb
    prev=[0x7d5], succ=[0x25400x7d5]
    =================================
    0x7ed: v7ed = ADD v7d9(0x4), v7dd
    0x7f1: v7f1 = CALLDATALOAD v7d9(0x4)
    0x7f2: v7f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x807: v807 = AND v7f2(0xffffffffffffffffffffffffffffffffffffffff), v7f1
    0x809: v809(0x20) = CONST 
    0x80b: v80b(0x24) = ADD v809(0x20), v7d9(0x4)
    0x811: v811 = CALLDATALOAD v80b(0x24)
    0x812: v812(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x827: v827 = AND v812(0xffffffffffffffffffffffffffffffffffffffff), v811
    0x829: v829(0x20) = CONST 
    0x82b: v82b(0x44) = ADD v829(0x20), v80b(0x24)
    0x833: v833(0x2540) = CONST 
    0x836: JUMP v833(0x2540)

    Begin block 0x25400x7d5
    prev=[0x7eb], succ=[0x25890x7d5]
    =================================
    0x25410x7d5: v7d52541(0x0) = CONST 
    0x25440x7d5: v7d52544(0x0) = CONST 
    0x25460x7d5: v7d52546(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25690x7d5: v7d52569(0x2597) = CONST 
    0x256c0x7d5: v7d5256c(0xde0b6b3a7640000) = CONST 
    0x25750x7d5: v7d52575(0x2589) = CONST 
    0x25780x7d5: v7d52578(0x5) = CONST 
    0x257a0x7d5: v7d5257a = SLOAD v7d52578(0x5)
    0x257c0x7d5: v7d5257c(0x2d1e) = CONST 
    0x25820x7d5: v7d52582(0xffffffff) = CONST 
    0x25870x7d5: v7d52587(0x2d1e) = AND v7d52582(0xffffffff), v7d5257c(0x2d1e)
    0x25880x7d5: v7d52588_0 = CALLPRIVATE v7d52587(0x2d1e), v7d5257a, v7d52546(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v7d52575(0x2589)

    Begin block 0x25890x7d5
    prev=[0x25400x7d5], succ=[0x25970x7d5]
    =================================
    0x258a0x7d5: v7d5258a(0x2c98) = CONST 
    0x25900x7d5: v7d52590(0xffffffff) = CONST 
    0x25950x7d5: v7d52595(0x2c98) = AND v7d52590(0xffffffff), v7d5258a(0x2c98)
    0x25960x7d5: v7d52596_0 = CALLPRIVATE v7d52595(0x2c98), v7d5256c(0xde0b6b3a7640000), v7d52588_0, v7d52569(0x2597)

    Begin block 0x25970x7d5
    prev=[0x25890x7d5], succ=[0x261e0x7d5, 0x26450x7d5]
    =================================
    0x259b0x7d5: v7d5259b(0x2) = CONST 
    0x259d0x7d5: v7d5259d(0x0) = CONST 
    0x25a00x7d5: v7d525a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25b50x7d5: v7d525b5 = AND v7d525a0(0xffffffffffffffffffffffffffffffffffffffff), v807
    0x25b60x7d5: v7d525b6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25cb0x7d5: v7d525cb = AND v7d525b6(0xffffffffffffffffffffffffffffffffffffffff), v7d525b5
    0x25cd0x7d5: MSTORE v7d5259d(0x0), v7d525cb
    0x25ce0x7d5: v7d525ce(0x20) = CONST 
    0x25d00x7d5: v7d525d0(0x20) = ADD v7d525ce(0x20), v7d5259d(0x0)
    0x25d30x7d5: MSTORE v7d525d0(0x20), v7d5259b(0x2)
    0x25d40x7d5: v7d525d4(0x20) = CONST 
    0x25d60x7d5: v7d525d6(0x40) = ADD v7d525d4(0x20), v7d525d0(0x20)
    0x25d70x7d5: v7d525d7(0x0) = CONST 
    0x25d90x7d5: v7d525d9 = SHA3 v7d525d7(0x0), v7d525d6(0x40)
    0x25da0x7d5: v7d525da(0x0) = CONST 
    0x25dd0x7d5: v7d525dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25f20x7d5: v7d525f2 = AND v7d525dd(0xffffffffffffffffffffffffffffffffffffffff), v827
    0x25f30x7d5: v7d525f3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26080x7d5: v7d52608 = AND v7d525f3(0xffffffffffffffffffffffffffffffffffffffff), v7d525f2
    0x260a0x7d5: MSTORE v7d525da(0x0), v7d52608
    0x260b0x7d5: v7d5260b(0x20) = CONST 
    0x260d0x7d5: v7d5260d(0x20) = ADD v7d5260b(0x20), v7d525da(0x0)
    0x26100x7d5: MSTORE v7d5260d(0x20), v7d525d9
    0x26110x7d5: v7d52611(0x20) = CONST 
    0x26130x7d5: v7d52613(0x40) = ADD v7d52611(0x20), v7d5260d(0x20)
    0x26140x7d5: v7d52614(0x0) = CONST 
    0x26160x7d5: v7d52616 = SHA3 v7d52614(0x0), v7d52613(0x40)
    0x26170x7d5: v7d52617 = SLOAD v7d52616
    0x26180x7d5: v7d52618 = GT v7d52617, v7d52596_0
    0x26190x7d5: v7d52619 = ISZERO v7d52618
    0x261a0x7d5: v7d5261a(0x2645) = CONST 
    0x261d0x7d5: JUMPI v7d5261a(0x2645), v7d52619

    Begin block 0x261e0x7d5
    prev=[0x25970x7d5], succ=[0x26f30x7d5]
    =================================
    0x261e0x7d5: v7d5261e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26410x7d5: v7d52641(0x26f3) = CONST 
    0x26440x7d5: JUMP v7d52641(0x26f3)

    Begin block 0x26f30x7d5
    prev=[0x261e0x7d5, 0x26f00x7d5], succ=[0x837]
    =================================
    0x26fd0x7d5: JUMP v7d6(0x837)

    Begin block 0x837
    prev=[0x26f30x7d5], succ=[]
    =================================
    0x837_0x0: v837_0 = PHI v7d526ef_0, v7d5261e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x838: v838(0x40) = CONST 
    0x83a: v83a = MLOAD v838(0x40)
    0x83e: MSTORE v83a, v837_0
    0x83f: v83f(0x20) = CONST 
    0x841: v841 = ADD v83f(0x20), v83a
    0x845: v845(0x40) = CONST 
    0x847: v847 = MLOAD v845(0x40)
    0x84a: v84a(0x20) = SUB v841, v847
    0x84c: RETURN v847, v84a(0x20)

    Begin block 0x26450x7d5
    prev=[0x25970x7d5], succ=[0x26e20x7d5]
    =================================
    0x26460x7d5: v7d52646(0x26f0) = CONST 
    0x26490x7d5: v7d52649(0xde0b6b3a7640000) = CONST 
    0x26520x7d5: v7d52652(0x26e2) = CONST 
    0x26550x7d5: v7d52655(0x5) = CONST 
    0x26570x7d5: v7d52657 = SLOAD v7d52655(0x5)
    0x26580x7d5: v7d52658(0x2) = CONST 
    0x265a0x7d5: v7d5265a(0x0) = CONST 
    0x265d0x7d5: v7d5265d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26720x7d5: v7d52672 = AND v7d5265d(0xffffffffffffffffffffffffffffffffffffffff), v807
    0x26730x7d5: v7d52673(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26880x7d5: v7d52688 = AND v7d52673(0xffffffffffffffffffffffffffffffffffffffff), v7d52672
    0x268a0x7d5: MSTORE v7d5265a(0x0), v7d52688
    0x268b0x7d5: v7d5268b(0x20) = CONST 
    0x268d0x7d5: v7d5268d(0x20) = ADD v7d5268b(0x20), v7d5265a(0x0)
    0x26900x7d5: MSTORE v7d5268d(0x20), v7d52658(0x2)
    0x26910x7d5: v7d52691(0x20) = CONST 
    0x26930x7d5: v7d52693(0x40) = ADD v7d52691(0x20), v7d5268d(0x20)
    0x26940x7d5: v7d52694(0x0) = CONST 
    0x26960x7d5: v7d52696 = SHA3 v7d52694(0x0), v7d52693(0x40)
    0x26970x7d5: v7d52697(0x0) = CONST 
    0x269a0x7d5: v7d5269a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26af0x7d5: v7d526af = AND v7d5269a(0xffffffffffffffffffffffffffffffffffffffff), v827
    0x26b00x7d5: v7d526b0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26c50x7d5: v7d526c5 = AND v7d526b0(0xffffffffffffffffffffffffffffffffffffffff), v7d526af
    0x26c70x7d5: MSTORE v7d52697(0x0), v7d526c5
    0x26c80x7d5: v7d526c8(0x20) = CONST 
    0x26ca0x7d5: v7d526ca(0x20) = ADD v7d526c8(0x20), v7d52697(0x0)
    0x26cd0x7d5: MSTORE v7d526ca(0x20), v7d52696
    0x26ce0x7d5: v7d526ce(0x20) = CONST 
    0x26d00x7d5: v7d526d0(0x40) = ADD v7d526ce(0x20), v7d526ca(0x20)
    0x26d10x7d5: v7d526d1(0x0) = CONST 
    0x26d30x7d5: v7d526d3 = SHA3 v7d526d1(0x0), v7d526d0(0x40)
    0x26d40x7d5: v7d526d4 = SLOAD v7d526d3
    0x26d50x7d5: v7d526d5(0x2c98) = CONST 
    0x26db0x7d5: v7d526db(0xffffffff) = CONST 
    0x26e00x7d5: v7d526e0(0x2c98) = AND v7d526db(0xffffffff), v7d526d5(0x2c98)
    0x26e10x7d5: v7d526e1_0 = CALLPRIVATE v7d526e0(0x2c98), v7d52657, v7d526d4, v7d52652(0x26e2)

    Begin block 0x26e20x7d5
    prev=[0x26450x7d5], succ=[0x26f00x7d5]
    =================================
    0x26e30x7d5: v7d526e3(0x2d1e) = CONST 
    0x26e90x7d5: v7d526e9(0xffffffff) = CONST 
    0x26ee0x7d5: v7d526ee(0x2d1e) = AND v7d526e9(0xffffffff), v7d526e3(0x2d1e)
    0x26ef0x7d5: v7d526ef_0 = CALLPRIVATE v7d526ee(0x2d1e), v7d52649(0xde0b6b3a7640000), v7d526e1_0, v7d52646(0x26f0)

    Begin block 0x26f00x7d5
    prev=[0x26e20x7d5], succ=[0x26f30x7d5]
    =================================

}

function setTotalSupply(uint256)() public {
    Begin block 0x84d
    prev=[], succ=[0x85f, 0x863]
    =================================
    0x84e: v84e(0x879) = CONST 
    0x851: v851(0x4) = CONST 
    0x854: v854 = CALLDATASIZE 
    0x855: v855 = SUB v854, v851(0x4)
    0x856: v856(0x20) = CONST 
    0x859: v859 = LT v855, v856(0x20)
    0x85a: v85a = ISZERO v859
    0x85b: v85b(0x863) = CONST 
    0x85e: JUMPI v85b(0x863), v85a

    Begin block 0x85f
    prev=[0x84d], succ=[]
    =================================
    0x85f: v85f(0x0) = CONST 
    0x862: REVERT v85f(0x0), v85f(0x0)

    Begin block 0x863
    prev=[0x84d], succ=[0x26fe]
    =================================
    0x865: v865 = ADD v851(0x4), v855
    0x869: v869 = CALLDATALOAD v851(0x4)
    0x86b: v86b(0x20) = CONST 
    0x86d: v86d(0x24) = ADD v86b(0x20), v851(0x4)
    0x875: v875(0x26fe) = CONST 
    0x878: JUMP v875(0x26fe)

    Begin block 0x26fe
    prev=[0x863], succ=[0x2754, 0x27c1]
    =================================
    0x26ff: v26ff(0x6) = CONST 
    0x2701: v2701(0x0) = CONST 
    0x2704: v2704 = SLOAD v26ff(0x6)
    0x2706: v2706(0x100) = CONST 
    0x2709: v2709(0x1) = EXP v2706(0x100), v2701(0x0)
    0x270b: v270b = DIV v2704, v2709(0x1)
    0x270c: v270c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2721: v2721 = AND v270c(0xffffffffffffffffffffffffffffffffffffffff), v270b
    0x2722: v2722(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2737: v2737 = AND v2722(0xffffffffffffffffffffffffffffffffffffffff), v2721
    0x2738: v2738 = CALLER 
    0x2739: v2739(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x274e: v274e = AND v2739(0xffffffffffffffffffffffffffffffffffffffff), v2738
    0x274f: v274f = EQ v274e, v2737
    0x2750: v2750(0x27c1) = CONST 
    0x2753: JUMPI v2750(0x27c1), v274f

    Begin block 0x2754
    prev=[0x26fe], succ=[]
    =================================
    0x2754: v2754(0x40) = CONST 
    0x2756: v2756 = MLOAD v2754(0x40)
    0x2757: v2757(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2779: MSTORE v2756, v2757(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x277a: v277a(0x4) = CONST 
    0x277c: v277c = ADD v277a(0x4), v2756
    0x277f: v277f(0x20) = CONST 
    0x2781: v2781 = ADD v277f(0x20), v277c
    0x2784: v2784(0x20) = SUB v2781, v277c
    0x2786: MSTORE v277c, v2784(0x20)
    0x2787: v2787(0x15) = CONST 
    0x278a: MSTORE v2781, v2787(0x15)
    0x278b: v278b(0x20) = CONST 
    0x278d: v278d = ADD v278b(0x20), v2781
    0x278f: v278f(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000) = CONST 
    0x27b1: MSTORE v278d, v278f(0x796f7520617265206e6f74207468652061646d696e0000000000000000000000)
    0x27b3: v27b3(0x20) = CONST 
    0x27b5: v27b5 = ADD v27b3(0x20), v278d
    0x27b9: v27b9(0x40) = CONST 
    0x27bb: v27bb = MLOAD v27b9(0x40)
    0x27be: v27be(0x64) = SUB v27b5, v27bb
    0x27c0: REVERT v27bb, v27be(0x64)

    Begin block 0x27c1
    prev=[0x26fe], succ=[0xbadB0x27c1]
    =================================
    0x27c2: v27c2(0x27c9) = CONST 
    0x27c5: v27c5(0xbad) = CONST 
    0x27c8: JUMP v27c5(0xbad)

    Begin block 0xbadB0x27c1
    prev=[0x27c1], succ=[0xbd2B0x27c1]
    =================================
    0xbaeS0x27c1: vbaeV27c1(0x0) = CONST 
    0xbb0S0x27c1: vbb0V27c1(0xbe0) = CONST 
    0xbb3S0x27c1: vbb3V27c1(0xde0b6b3a7640000) = CONST 
    0xbbcS0x27c1: vbbcV27c1(0xbd2) = CONST 
    0xbbfS0x27c1: vbbfV27c1(0x5) = CONST 
    0xbc1S0x27c1: vbc1V27c1 = SLOAD vbbfV27c1(0x5)
    0xbc2S0x27c1: vbc2V27c1(0x4) = CONST 
    0xbc4S0x27c1: vbc4V27c1 = SLOAD vbc2V27c1(0x4)
    0xbc5S0x27c1: vbc5V27c1(0x2c98) = CONST 
    0xbcbS0x27c1: vbcbV27c1(0xffffffff) = CONST 
    0xbd0S0x27c1: vbd0V27c1(0x2c98) = AND vbcbV27c1(0xffffffff), vbc5V27c1(0x2c98)
    0xbd1S0x27c1: vbd1_0V27c1 = CALLPRIVATE vbd0V27c1(0x2c98), vbc1V27c1, vbc4V27c1, vbbcV27c1(0xbd2)

    Begin block 0xbd2B0x27c1
    prev=[0xbadB0x27c1], succ=[0xbe0B0x27c1]
    =================================
    0xbd3S0x27c1: vbd3V27c1(0x2d1e) = CONST 
    0xbd9S0x27c1: vbd9V27c1(0xffffffff) = CONST 
    0xbdeS0x27c1: vbdeV27c1(0x2d1e) = AND vbd9V27c1(0xffffffff), vbd3V27c1(0x2d1e)
    0xbdfS0x27c1: vbdf_0V27c1 = CALLPRIVATE vbdeV27c1(0x2d1e), vbb3V27c1(0xde0b6b3a7640000), vbd1_0V27c1, vbb0V27c1(0xbe0)

    Begin block 0xbe0B0x27c1
    prev=[0xbd2B0x27c1], succ=[0x27c9]
    =================================
    0xbe4S0x27c1: JUMP v27c2(0x27c9)

    Begin block 0x27c9
    prev=[0xbe0B0x27c1], succ=[0x27d0, 0x2820]
    =================================
    0x27cb: v27cb = GT v869, vbdf_0V27c1
    0x27cc: v27cc(0x2820) = CONST 
    0x27cf: JUMPI v27cc(0x2820), v27cb

    Begin block 0x27d0
    prev=[0x27c9], succ=[]
    =================================
    0x27d0: v27d0(0x40) = CONST 
    0x27d2: v27d2 = MLOAD v27d0(0x40)
    0x27d3: v27d3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x27f5: MSTORE v27d2, v27d3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x27f6: v27f6(0x4) = CONST 
    0x27f8: v27f8 = ADD v27f6(0x4), v27d2
    0x27fb: v27fb(0x20) = CONST 
    0x27fd: v27fd = ADD v27fb(0x20), v27f8
    0x2800: v2800(0x20) = SUB v27fd, v27f8
    0x2802: MSTORE v27f8, v2800(0x20)
    0x2803: v2803(0x3f) = CONST 
    0x2806: MSTORE v27fd, v2803(0x3f)
    0x2807: v2807(0x20) = CONST 
    0x2809: v2809 = ADD v2807(0x20), v27fd
    0x280b: v280b(0x3968) = CONST 
    0x280e: v280e(0x3f) = CONST 
    0x2811: CODECOPY v2809, v280b(0x3968), v280e(0x3f)
    0x2812: v2812(0x40) = CONST 
    0x2814: v2814 = ADD v2812(0x40), v2809
    0x2818: v2818(0x40) = CONST 
    0x281a: v281a = MLOAD v2818(0x40)
    0x281d: v281d(0x84) = SUB v2814, v281a
    0x281f: REVERT v281a, v281d(0x84)

    Begin block 0x2820
    prev=[0x27c9], succ=[0x2841]
    =================================
    0x2821: v2821(0x284f) = CONST 
    0x2824: v2824(0x4) = CONST 
    0x2826: v2826 = SLOAD v2824(0x4)
    0x2827: v2827(0x2841) = CONST 
    0x282a: v282a(0xde0b6b3a7640000) = CONST 
    0x2834: v2834(0x2c98) = CONST 
    0x283a: v283a(0xffffffff) = CONST 
    0x283f: v283f(0x2c98) = AND v283a(0xffffffff), v2834(0x2c98)
    0x2840: v2840_0 = CALLPRIVATE v283f(0x2c98), v282a(0xde0b6b3a7640000), v869, v2827(0x2841)

    Begin block 0x2841
    prev=[0x2820], succ=[0x284f]
    =================================
    0x2842: v2842(0x2d1e) = CONST 
    0x2848: v2848(0xffffffff) = CONST 
    0x284d: v284d(0x2d1e) = AND v2848(0xffffffff), v2842(0x2d1e)
    0x284e: v284e_0 = CALLPRIVATE v284d(0x2d1e), v2826, v2840_0, v2821(0x284f)

    Begin block 0x284f
    prev=[0x2841], succ=[0x879]
    =================================
    0x2850: v2850(0x5) = CONST 
    0x2854: SSTORE v2850(0x5), v284e_0
    0x2856: v2856(0xd1ac89bfc464ce49c894c4e2379f1ca2b062aff1a640e929764ac1157fa13f0f) = CONST 
    0x2877: v2877(0x5) = CONST 
    0x2879: v2879 = SLOAD v2877(0x5)
    0x287a: v287a(0x40) = CONST 
    0x287c: v287c = MLOAD v287a(0x40)
    0x2880: MSTORE v287c, v2879
    0x2881: v2881(0x20) = CONST 
    0x2883: v2883 = ADD v2881(0x20), v287c
    0x2887: v2887(0x40) = CONST 
    0x2889: v2889 = MLOAD v2887(0x40)
    0x288c: v288c(0x20) = SUB v2883, v2889
    0x288e: LOG1 v2889, v288c(0x20), v2856(0xd1ac89bfc464ce49c894c4e2379f1ca2b062aff1a640e929764ac1157fa13f0f)
    0x2890: JUMP v84e(0x879)

    Begin block 0x879
    prev=[0x284f], succ=[]
    =================================
    0x87a: STOP 

}

function admin()() public {
    Begin block 0x87b
    prev=[], succ=[0x2891]
    =================================
    0x87c: v87c(0x883) = CONST 
    0x87f: v87f(0x2891) = CONST 
    0x882: JUMP v87f(0x2891)

    Begin block 0x2891
    prev=[0x87b], succ=[0x883]
    =================================
    0x2892: v2892(0x6) = CONST 
    0x2894: v2894(0x0) = CONST 
    0x2897: v2897 = SLOAD v2892(0x6)
    0x2899: v2899(0x100) = CONST 
    0x289c: v289c(0x1) = EXP v2899(0x100), v2894(0x0)
    0x289e: v289e = DIV v2897, v289c(0x1)
    0x289f: v289f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28b4: v28b4 = AND v289f(0xffffffffffffffffffffffffffffffffffffffff), v289e
    0x28b6: JUMP v87c(0x883)

    Begin block 0x883
    prev=[0x2891], succ=[]
    =================================
    0x884: v884(0x40) = CONST 
    0x886: v886 = MLOAD v884(0x40)
    0x889: v889(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x89e: v89e = AND v889(0xffffffffffffffffffffffffffffffffffffffff), v28b4
    0x8a0: MSTORE v886, v89e
    0x8a1: v8a1(0x20) = CONST 
    0x8a3: v8a3 = ADD v8a1(0x20), v886
    0x8a7: v8a7(0x40) = CONST 
    0x8a9: v8a9 = MLOAD v8a7(0x40)
    0x8ac: v8ac(0x20) = SUB v8a3, v8a9
    0x8ae: RETURN v8a9, v8ac(0x20)

}

function blacklist(address)() public {
    Begin block 0x8af
    prev=[], succ=[0x8c1, 0x8c5]
    =================================
    0x8b0: v8b0(0x8f1) = CONST 
    0x8b3: v8b3(0x4) = CONST 
    0x8b6: v8b6 = CALLDATASIZE 
    0x8b7: v8b7 = SUB v8b6, v8b3(0x4)
    0x8b8: v8b8(0x20) = CONST 
    0x8bb: v8bb = LT v8b7, v8b8(0x20)
    0x8bc: v8bc = ISZERO v8bb
    0x8bd: v8bd(0x8c5) = CONST 
    0x8c0: JUMPI v8bd(0x8c5), v8bc

    Begin block 0x8c1
    prev=[0x8af], succ=[]
    =================================
    0x8c1: v8c1(0x0) = CONST 
    0x8c4: REVERT v8c1(0x0), v8c1(0x0)

    Begin block 0x8c5
    prev=[0x8af], succ=[0x28b7]
    =================================
    0x8c7: v8c7 = ADD v8b3(0x4), v8b7
    0x8cb: v8cb = CALLDATALOAD v8b3(0x4)
    0x8cc: v8cc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8e1: v8e1 = AND v8cc(0xffffffffffffffffffffffffffffffffffffffff), v8cb
    0x8e3: v8e3(0x20) = CONST 
    0x8e5: v8e5(0x24) = ADD v8e3(0x20), v8b3(0x4)
    0x8ed: v8ed(0x28b7) = CONST 
    0x8f0: JUMP v8ed(0x28b7)

    Begin block 0x28b7
    prev=[0x8c5], succ=[0x8f1]
    =================================
    0x28b8: v28b8(0x3) = CONST 
    0x28ba: v28ba(0x20) = CONST 
    0x28bc: MSTORE v28ba(0x20), v28b8(0x3)
    0x28be: v28be(0x0) = CONST 
    0x28c0: MSTORE v28be(0x0), v8e1
    0x28c1: v28c1(0x40) = CONST 
    0x28c3: v28c3(0x0) = CONST 
    0x28c5: v28c5 = SHA3 v28c3(0x0), v28c1(0x40)
    0x28c6: v28c6(0x0) = CONST 
    0x28ca: v28ca = SLOAD v28c5
    0x28cc: v28cc(0x100) = CONST 
    0x28cf: v28cf(0x1) = EXP v28cc(0x100), v28c6(0x0)
    0x28d1: v28d1 = DIV v28ca, v28cf(0x1)
    0x28d2: v28d2(0xff) = CONST 
    0x28d4: v28d4 = AND v28d2(0xff), v28d1
    0x28d6: JUMP v8b0(0x8f1)

    Begin block 0x8f1
    prev=[0x28b7], succ=[]
    =================================
    0x8f2: v8f2(0x40) = CONST 
    0x8f4: v8f4 = MLOAD v8f2(0x40)
    0x8f7: v8f7 = ISZERO v28d4
    0x8f8: v8f8 = ISZERO v8f7
    0x8fa: MSTORE v8f4, v8f8
    0x8fb: v8fb(0x20) = CONST 
    0x8fd: v8fd = ADD v8fb(0x20), v8f4
    0x901: v901(0x40) = CONST 
    0x903: v903 = MLOAD v901(0x40)
    0x906: v906(0x20) = SUB v8fd, v903
    0x908: RETURN v903, v906(0x20)

}

function initialize(uint256)() public {
    Begin block 0x909
    prev=[], succ=[0x91b, 0x91f]
    =================================
    0x90a: v90a(0x935) = CONST 
    0x90d: v90d(0x4) = CONST 
    0x910: v910 = CALLDATASIZE 
    0x911: v911 = SUB v910, v90d(0x4)
    0x912: v912(0x20) = CONST 
    0x915: v915 = LT v911, v912(0x20)
    0x916: v916 = ISZERO v915
    0x917: v917(0x91f) = CONST 
    0x91a: JUMPI v917(0x91f), v916

    Begin block 0x91b
    prev=[0x909], succ=[]
    =================================
    0x91b: v91b(0x0) = CONST 
    0x91e: REVERT v91b(0x0), v91b(0x0)

    Begin block 0x91f
    prev=[0x909], succ=[0x28d7]
    =================================
    0x921: v921 = ADD v90d(0x4), v911
    0x925: v925 = CALLDATALOAD v90d(0x4)
    0x927: v927(0x20) = CONST 
    0x929: v929(0x24) = ADD v927(0x20), v90d(0x4)
    0x931: v931(0x28d7) = CONST 
    0x934: JUMP v931(0x28d7)

    Begin block 0x28d7
    prev=[0x91f], succ=[0x28eb, 0x293b]
    =================================
    0x28d8: v28d8(0x0) = CONST 
    0x28db: v28db = SLOAD v28d8(0x0)
    0x28dd: v28dd(0x100) = CONST 
    0x28e0: v28e0(0x1) = EXP v28dd(0x100), v28d8(0x0)
    0x28e2: v28e2 = DIV v28db, v28e0(0x1)
    0x28e3: v28e3(0xff) = CONST 
    0x28e5: v28e5 = AND v28e3(0xff), v28e2
    0x28e6: v28e6 = ISZERO v28e5
    0x28e7: v28e7(0x293b) = CONST 
    0x28ea: JUMPI v28e7(0x293b), v28e6

    Begin block 0x28eb
    prev=[0x28d7], succ=[]
    =================================
    0x28eb: v28eb(0x40) = CONST 
    0x28ed: v28ed = MLOAD v28eb(0x40)
    0x28ee: v28ee(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2910: MSTORE v28ed, v28ee(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2911: v2911(0x4) = CONST 
    0x2913: v2913 = ADD v2911(0x4), v28ed
    0x2916: v2916(0x20) = CONST 
    0x2918: v2918 = ADD v2916(0x20), v2913
    0x291b: v291b(0x20) = SUB v2918, v2913
    0x291d: MSTORE v2913, v291b(0x20)
    0x291e: v291e(0x29) = CONST 
    0x2921: MSTORE v2918, v291e(0x29)
    0x2922: v2922(0x20) = CONST 
    0x2924: v2924 = ADD v2922(0x20), v2918
    0x2926: v2926(0x3820) = CONST 
    0x2929: v2929(0x29) = CONST 
    0x292c: CODECOPY v2924, v2926(0x3820), v2929(0x29)
    0x292d: v292d(0x40) = CONST 
    0x292f: v292f = ADD v292d(0x40), v2924
    0x2933: v2933(0x40) = CONST 
    0x2935: v2935 = MLOAD v2933(0x40)
    0x2938: v2938(0x84) = SUB v292f, v2935
    0x293a: REVERT v2935, v2938(0x84)

    Begin block 0x293b
    prev=[0x28d7], succ=[0x365d]
    =================================
    0x293c: v293c(0x2943) = CONST 
    0x293f: v293f(0x365d) = CONST 
    0x2942: JUMP v293f(0x365d)

    Begin block 0x365d
    prev=[0x293b], succ=[0x2943]
    =================================
    0x365e: v365e(0x1) = CONST 
    0x3660: v3660(0x0) = CONST 
    0x3663: v3663(0x100) = CONST 
    0x3666: v3666(0x1) = EXP v3663(0x100), v3660(0x0)
    0x3668: v3668 = SLOAD v3660(0x0)
    0x366a: v366a(0xff) = CONST 
    0x366c: v366c(0xff) = MUL v366a(0xff), v3666(0x1)
    0x366d: v366d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v366c(0xff)
    0x366e: v366e = AND v366d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v3668
    0x3671: v3671(0x0) = ISZERO v365e(0x1)
    0x3672: v3672(0x1) = ISZERO v3671(0x0)
    0x3673: v3673(0x1) = MUL v3672(0x1), v3666(0x1)
    0x3674: v3674 = OR v3673(0x1), v366e
    0x3676: SSTORE v3660(0x0), v3674
    0x3678: JUMP v293c(0x2943)

    Begin block 0x2943
    prev=[0x365d], succ=[0x935]
    =================================
    0x2944: v2944 = CALLER 
    0x2945: v2945(0x6) = CONST 
    0x2947: v2947(0x0) = CONST 
    0x2949: v2949(0x100) = CONST 
    0x294c: v294c(0x1) = EXP v2949(0x100), v2947(0x0)
    0x294e: v294e = SLOAD v2945(0x6)
    0x2950: v2950(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2965: v2965(0xffffffffffffffffffffffffffffffffffffffff) = MUL v2950(0xffffffffffffffffffffffffffffffffffffffff), v294c(0x1)
    0x2966: v2966(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2965(0xffffffffffffffffffffffffffffffffffffffff)
    0x2967: v2967 = AND v2966(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v294e
    0x296a: v296a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x297f: v297f = AND v296a(0xffffffffffffffffffffffffffffffffffffffff), v2944
    0x2980: v2980 = MUL v297f, v294c(0x1)
    0x2981: v2981 = OR v2980, v2967
    0x2983: SSTORE v2945(0x6), v2981
    0x2985: v2985(0xde0b6b3a7640000) = CONST 
    0x298e: v298e(0x1) = CONST 
    0x2990: v2990(0xde0b6b3a7640000) = MUL v298e(0x1), v2985(0xde0b6b3a7640000)
    0x2991: v2991(0x5) = CONST 
    0x2995: SSTORE v2991(0x5), v2990(0xde0b6b3a7640000)
    0x2998: v2998(0x4) = CONST 
    0x299c: SSTORE v2998(0x4), v925
    0x299e: v299e(0x4) = CONST 
    0x29a0: v29a0 = SLOAD v299e(0x4)
    0x29a1: v29a1(0x1) = CONST 
    0x29a3: v29a3(0x0) = CONST 
    0x29a5: v29a5 = CALLER 
    0x29a6: v29a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29bb: v29bb = AND v29a6(0xffffffffffffffffffffffffffffffffffffffff), v29a5
    0x29bc: v29bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29d1: v29d1 = AND v29bc(0xffffffffffffffffffffffffffffffffffffffff), v29bb
    0x29d3: MSTORE v29a3(0x0), v29d1
    0x29d4: v29d4(0x20) = CONST 
    0x29d6: v29d6(0x20) = ADD v29d4(0x20), v29a3(0x0)
    0x29d9: MSTORE v29d6(0x20), v29a1(0x1)
    0x29da: v29da(0x20) = CONST 
    0x29dc: v29dc(0x40) = ADD v29da(0x20), v29d6(0x20)
    0x29dd: v29dd(0x0) = CONST 
    0x29df: v29df = SHA3 v29dd(0x0), v29dc(0x40)
    0x29e2: SSTORE v29df, v29a0
    0x29e5: JUMP v90a(0x935)

    Begin block 0x935
    prev=[0x2943], succ=[]
    =================================
    0x936: STOP 

}

