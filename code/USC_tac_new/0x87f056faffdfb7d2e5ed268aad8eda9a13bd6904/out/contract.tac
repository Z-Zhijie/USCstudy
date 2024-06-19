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
    prev=[0x0], succ=[0x1a, 0x1b40]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x1ad0: v1ad0(0x1b40) = CONST 
    0x1ad1: JUMPI v1ad0(0x1b40), v15

    Begin block 0x1a
    prev=[0x10], succ=[0xb8, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x5c975abb) = CONST 
    0x26: v26 = GT v21(0x5c975abb), v1f
    0x27: v27(0xb8) = CONST 
    0x2a: JUMPI v27(0xb8), v26

    Begin block 0xb8
    prev=[0x1a], succ=[0x10a, 0xc4]
    =================================
    0xba: vba(0x23b872dd) = CONST 
    0xbf: vbf = GT vba(0x23b872dd), v1f
    0xc0: vc0(0x10a) = CONST 
    0xc3: JUMPI vc0(0x10a), vbf

    Begin block 0x10a
    prev=[0xb8], succ=[0x1afe, 0x116]
    =================================
    0x10c: v10c(0x6fdde03) = CONST 
    0x111: v111 = EQ v10c(0x6fdde03), v1f
    0x1af4: v1af4(0x1afe) = CONST 
    0x1af5: JUMPI v1af4(0x1afe), v111

    Begin block 0x1afe
    prev=[0x10a], succ=[]
    =================================
    0x1aff: v1aff(0x147) = CONST 
    0x1b00: CALLPRIVATE v1aff(0x147)

    Begin block 0x116
    prev=[0x10a], succ=[0x1b01, 0x121]
    =================================
    0x117: v117(0x95ea7b3) = CONST 
    0x11c: v11c = EQ v117(0x95ea7b3), v1f
    0x1af6: v1af6(0x1b01) = CONST 
    0x1af7: JUMPI v1af6(0x1b01), v11c

    Begin block 0x1b01
    prev=[0x116], succ=[]
    =================================
    0x1b02: v1b02(0x1c4) = CONST 
    0x1b03: CALLPRIVATE v1b02(0x1c4)

    Begin block 0x121
    prev=[0x116], succ=[0x1b04, 0x12c]
    =================================
    0x122: v122(0x1624f6c6) = CONST 
    0x127: v127 = EQ v122(0x1624f6c6), v1f
    0x1af8: v1af8(0x1b04) = CONST 
    0x1af9: JUMPI v1af8(0x1b04), v127

    Begin block 0x1b04
    prev=[0x121], succ=[]
    =================================
    0x1b05: v1b05(0x204) = CONST 
    0x1b06: CALLPRIVATE v1b05(0x204)

    Begin block 0x12c
    prev=[0x121], succ=[0x1b07, 0x137]
    =================================
    0x12d: v12d(0x1785f53c) = CONST 
    0x132: v132 = EQ v12d(0x1785f53c), v1f
    0x1afa: v1afa(0x1b07) = CONST 
    0x1afb: JUMPI v1afa(0x1b07), v132

    Begin block 0x1b07
    prev=[0x12c], succ=[]
    =================================
    0x1b08: v1b08(0x338) = CONST 
    0x1b09: CALLPRIVATE v1b08(0x338)

    Begin block 0x137
    prev=[0x12c], succ=[0x1b0a, 0x142]
    =================================
    0x138: v138(0x18160ddd) = CONST 
    0x13d: v13d = EQ v138(0x18160ddd), v1f
    0x1afc: v1afc(0x1b0a) = CONST 
    0x1afd: JUMPI v1afc(0x1b0a), v13d

    Begin block 0x1b0a
    prev=[0x137], succ=[]
    =================================
    0x1b0b: v1b0b(0x35e) = CONST 
    0x1b0c: CALLPRIVATE v1b0b(0x35e)

    Begin block 0x142
    prev=[0x137], succ=[]
    =================================
    0x143: v143(0x0) = CONST 
    0x146: REVERT v143(0x0), v143(0x0)

    Begin block 0xc4
    prev=[0xb8], succ=[0x1b0d, 0xcf]
    =================================
    0xc5: vc5(0x23b872dd) = CONST 
    0xca: vca = EQ vc5(0x23b872dd), v1f
    0x1ae8: v1ae8(0x1b0d) = CONST 
    0x1ae9: JUMPI v1ae8(0x1b0d), vca

    Begin block 0x1b0d
    prev=[0xc4], succ=[]
    =================================
    0x1b0e: v1b0e(0x378) = CONST 
    0x1b0f: CALLPRIVATE v1b0e(0x378)

    Begin block 0xcf
    prev=[0xc4], succ=[0x1b10, 0xda]
    =================================
    0xd0: vd0(0x24d7806c) = CONST 
    0xd5: vd5 = EQ vd0(0x24d7806c), v1f
    0x1aea: v1aea(0x1b10) = CONST 
    0x1aeb: JUMPI v1aea(0x1b10), vd5

    Begin block 0x1b10
    prev=[0xcf], succ=[]
    =================================
    0x1b11: v1b11(0x3ae) = CONST 
    0x1b12: CALLPRIVATE v1b11(0x3ae)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x1b13]
    =================================
    0xdb: vdb(0x313ce567) = CONST 
    0xe0: ve0 = EQ vdb(0x313ce567), v1f
    0x1aec: v1aec(0x1b13) = CONST 
    0x1aed: JUMPI v1aec(0x1b13), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0x1b16, 0xf0]
    =================================
    0xe6: ve6(0x39509351) = CONST 
    0xeb: veb = EQ ve6(0x39509351), v1f
    0x1aee: v1aee(0x1b16) = CONST 
    0x1aef: JUMPI v1aee(0x1b16), veb

    Begin block 0x1b16
    prev=[0xe5], succ=[]
    =================================
    0x1b17: v1b17(0x3f2) = CONST 
    0x1b18: CALLPRIVATE v1b17(0x3f2)

    Begin block 0xf0
    prev=[0xe5], succ=[0x1b19, 0xfb]
    =================================
    0xf1: vf1(0x40c10f19) = CONST 
    0xf6: vf6 = EQ vf1(0x40c10f19), v1f
    0x1af0: v1af0(0x1b19) = CONST 
    0x1af1: JUMPI v1af0(0x1b19), vf6

    Begin block 0x1b19
    prev=[0xf0], succ=[]
    =================================
    0x1b1a: v1b1a(0x41e) = CONST 
    0x1b1b: CALLPRIVATE v1b1a(0x41e)

    Begin block 0xfb
    prev=[0xf0], succ=[0x106, 0x1b1c]
    =================================
    0xfc: vfc(0x42966c68) = CONST 
    0x101: v101 = EQ vfc(0x42966c68), v1f
    0x1af2: v1af2(0x1b1c) = CONST 
    0x1af3: JUMPI v1af2(0x1b1c), v101

    Begin block 0x106
    prev=[0xfb], succ=[0x15d8]
    =================================
    0x106: v106(0x15d8) = CONST 
    0x109: JUMP v106(0x15d8)

    Begin block 0x15d8
    prev=[0x106], succ=[]
    =================================
    0x15d9: v15d9(0x0) = CONST 
    0x15dc: REVERT v15d9(0x0), v15d9(0x0)

    Begin block 0x1b1c
    prev=[0xfb], succ=[]
    =================================
    0x1b1d: v1b1d(0x44a) = CONST 
    0x1b1e: CALLPRIVATE v1b1d(0x44a)

    Begin block 0x1b13
    prev=[0xda], succ=[]
    =================================
    0x1b14: v1b14(0x3d4) = CONST 
    0x1b15: CALLPRIVATE v1b14(0x3d4)

    Begin block 0x2b
    prev=[0x1a], succ=[0x7c, 0x36]
    =================================
    0x2c: v2c(0x95d89b41) = CONST 
    0x31: v31 = GT v2c(0x95d89b41), v1f
    0x32: v32(0x7c) = CONST 
    0x35: JUMPI v32(0x7c), v31

    Begin block 0x7c
    prev=[0x2b], succ=[0x1b1f, 0x88]
    =================================
    0x7e: v7e(0x5c975abb) = CONST 
    0x83: v83 = EQ v7e(0x5c975abb), v1f
    0x1ade: v1ade(0x1b1f) = CONST 
    0x1adf: JUMPI v1ade(0x1b1f), v83

    Begin block 0x1b1f
    prev=[0x7c], succ=[]
    =================================
    0x1b20: v1b20(0x467) = CONST 
    0x1b21: CALLPRIVATE v1b20(0x467)

    Begin block 0x88
    prev=[0x7c], succ=[0x1b22, 0x93]
    =================================
    0x89: v89(0x70480275) = CONST 
    0x8e: v8e = EQ v89(0x70480275), v1f
    0x1ae0: v1ae0(0x1b22) = CONST 
    0x1ae1: JUMPI v1ae0(0x1b22), v8e

    Begin block 0x1b22
    prev=[0x88], succ=[]
    =================================
    0x1b23: v1b23(0x46f) = CONST 
    0x1b24: CALLPRIVATE v1b23(0x46f)

    Begin block 0x93
    prev=[0x88], succ=[0x1b25, 0x9e]
    =================================
    0x94: v94(0x70a08231) = CONST 
    0x99: v99 = EQ v94(0x70a08231), v1f
    0x1ae2: v1ae2(0x1b25) = CONST 
    0x1ae3: JUMPI v1ae2(0x1b25), v99

    Begin block 0x1b25
    prev=[0x93], succ=[]
    =================================
    0x1b26: v1b26(0x495) = CONST 
    0x1b27: CALLPRIVATE v1b26(0x495)

    Begin block 0x9e
    prev=[0x93], succ=[0x1b28, 0xa9]
    =================================
    0x9f: v9f(0x79ba5097) = CONST 
    0xa4: va4 = EQ v9f(0x79ba5097), v1f
    0x1ae4: v1ae4(0x1b28) = CONST 
    0x1ae5: JUMPI v1ae4(0x1b28), va4

    Begin block 0x1b28
    prev=[0x9e], succ=[]
    =================================
    0x1b29: v1b29(0x4bb) = CONST 
    0x1b2a: CALLPRIVATE v1b29(0x4bb)

    Begin block 0xa9
    prev=[0x9e], succ=[0xb4, 0x1b2b]
    =================================
    0xaa: vaa(0x8da5cb5b) = CONST 
    0xaf: vaf = EQ vaa(0x8da5cb5b), v1f
    0x1ae6: v1ae6(0x1b2b) = CONST 
    0x1ae7: JUMPI v1ae6(0x1b2b), vaf

    Begin block 0xb4
    prev=[0xa9], succ=[0x15b4]
    =================================
    0xb4: vb4(0x15b4) = CONST 
    0xb7: JUMP vb4(0x15b4)

    Begin block 0x15b4
    prev=[0xb4], succ=[]
    =================================
    0x15b5: v15b5(0x0) = CONST 
    0x15b8: REVERT v15b5(0x0), v15b5(0x0)

    Begin block 0x1b2b
    prev=[0xa9], succ=[]
    =================================
    0x1b2c: v1b2c(0x4c3) = CONST 
    0x1b2d: CALLPRIVATE v1b2c(0x4c3)

    Begin block 0x36
    prev=[0x2b], succ=[0x1b2e, 0x41]
    =================================
    0x37: v37(0x95d89b41) = CONST 
    0x3c: v3c = EQ v37(0x95d89b41), v1f
    0x1ad2: v1ad2(0x1b2e) = CONST 
    0x1ad3: JUMPI v1ad2(0x1b2e), v3c

    Begin block 0x1b2e
    prev=[0x36], succ=[]
    =================================
    0x1b2f: v1b2f(0x4e7) = CONST 
    0x1b30: CALLPRIVATE v1b2f(0x4e7)

    Begin block 0x41
    prev=[0x36], succ=[0x1b31, 0x4c]
    =================================
    0x42: v42(0xa457c2d7) = CONST 
    0x47: v47 = EQ v42(0xa457c2d7), v1f
    0x1ad4: v1ad4(0x1b31) = CONST 
    0x1ad5: JUMPI v1ad4(0x1b31), v47

    Begin block 0x1b31
    prev=[0x41], succ=[]
    =================================
    0x1b32: v1b32(0x4ef) = CONST 
    0x1b33: CALLPRIVATE v1b32(0x4ef)

    Begin block 0x4c
    prev=[0x41], succ=[0x1b34, 0x57]
    =================================
    0x4d: v4d(0xa9059cbb) = CONST 
    0x52: v52 = EQ v4d(0xa9059cbb), v1f
    0x1ad6: v1ad6(0x1b34) = CONST 
    0x1ad7: JUMPI v1ad6(0x1b34), v52

    Begin block 0x1b34
    prev=[0x4c], succ=[]
    =================================
    0x1b35: v1b35(0x51b) = CONST 
    0x1b36: CALLPRIVATE v1b35(0x51b)

    Begin block 0x57
    prev=[0x4c], succ=[0x1b37, 0x62]
    =================================
    0x58: v58(0xdd62ed3e) = CONST 
    0x5d: v5d = EQ v58(0xdd62ed3e), v1f
    0x1ad8: v1ad8(0x1b37) = CONST 
    0x1ad9: JUMPI v1ad8(0x1b37), v5d

    Begin block 0x1b37
    prev=[0x57], succ=[]
    =================================
    0x1b38: v1b38(0x547) = CONST 
    0x1b39: CALLPRIVATE v1b38(0x547)

    Begin block 0x62
    prev=[0x57], succ=[0x1b3a, 0x6d]
    =================================
    0x63: v63(0xe30c3978) = CONST 
    0x68: v68 = EQ v63(0xe30c3978), v1f
    0x1ada: v1ada(0x1b3a) = CONST 
    0x1adb: JUMPI v1ada(0x1b3a), v68

    Begin block 0x1b3a
    prev=[0x62], succ=[]
    =================================
    0x1b3b: v1b3b(0x575) = CONST 
    0x1b3c: CALLPRIVATE v1b3b(0x575)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x1b3d]
    =================================
    0x6e: v6e(0xf2fde38b) = CONST 
    0x73: v73 = EQ v6e(0xf2fde38b), v1f
    0x1adc: v1adc(0x1b3d) = CONST 
    0x1add: JUMPI v1adc(0x1b3d), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x1590]
    =================================
    0x78: v78(0x1590) = CONST 
    0x7b: JUMP v78(0x1590)

    Begin block 0x1590
    prev=[0x78], succ=[]
    =================================
    0x1591: v1591(0x0) = CONST 
    0x1594: REVERT v1591(0x0), v1591(0x0)

    Begin block 0x1b3d
    prev=[0x6d], succ=[]
    =================================
    0x1b3e: v1b3e(0x57d) = CONST 
    0x1b3f: CALLPRIVATE v1b3e(0x57d)

    Begin block 0x1b40
    prev=[0x10], succ=[]
    =================================
    0x1b41: v1b41(0x156c) = CONST 
    0x1b42: CALLPRIVATE v1b41(0x156c)

}

function 0x126f(0x126farg0x0, 0x126farg0x1, 0x126farg0x2) private {
    Begin block 0x126f
    prev=[], succ=[0x127b, 0x12ba]
    =================================
    0x1270: v1270(0x3) = CONST 
    0x1272: v1272 = SLOAD v1270(0x3)
    0x1273: v1273(0xff) = CONST 
    0x1275: v1275 = AND v1273(0xff), v1272
    0x1276: v1276 = ISZERO v1275
    0x1277: v1277(0x12ba) = CONST 
    0x127a: JUMPI v1277(0x12ba), v1276

    Begin block 0x127b
    prev=[0x126f], succ=[]
    =================================
    0x127b: v127b(0x40) = CONST 
    0x127e: v127e = MLOAD v127b(0x40)
    0x127f: v127f(0x461bcd) = CONST 
    0x1283: v1283(0xe5) = CONST 
    0x1285: v1285(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1283(0xe5), v127f(0x461bcd)
    0x1287: MSTORE v127e, v1285(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1288: v1288(0x20) = CONST 
    0x128a: v128a(0x4) = CONST 
    0x128d: v128d = ADD v127e, v128a(0x4)
    0x128e: MSTORE v128d, v1288(0x20)
    0x128f: v128f(0x10) = CONST 
    0x1291: v1291(0x24) = CONST 
    0x1294: v1294 = ADD v127e, v1291(0x24)
    0x1295: MSTORE v1294, v128f(0x10)
    0x1296: v1296(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0x12a7: v12a7(0x82) = CONST 
    0x12a9: v12a9(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL v12a7(0x82), v1296(0x14185d5cd8589b194e881c185d5cd959)
    0x12aa: v12aa(0x44) = CONST 
    0x12ad: v12ad = ADD v127e, v12aa(0x44)
    0x12ae: MSTORE v12ad, v12a9(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x12b0: v12b0 = MLOAD v127b(0x40)
    0x12b4: v12b4(0x0) = SUB v127e, v12b0
    0x12b5: v12b5(0x64) = CONST 
    0x12b7: v12b7(0x64) = ADD v12b5(0x64), v12b4(0x0)
    0x12b9: REVERT v12b0, v12b7(0x64)

    Begin block 0x12ba
    prev=[0x126f], succ=[0x12c1]
    =================================
    0x12bb: v12bb(0x12c1) = CONST 

    Begin block 0x12c1
    prev=[0x12ba], succ=[]
    =================================
    0x12c5: RETURNPRIVATE v12bb(0x12c1), v126farg0, v126farg1, v126farg2

}

function name()() public {
    Begin block 0x147
    prev=[], succ=[0x5a3B0x147]
    =================================
    0x148: v148(0x14f) = CONST 
    0x14b: v14b(0x5a3) = CONST 
    0x14e: JUMP v14b(0x5a3)

    Begin block 0x5a3B0x147
    prev=[0x147], succ=[0x5e9B0x147, 0x62f0x5a3B0x147]
    =================================
    0x5a4S0x147: v5a4V147(0x7) = CONST 
    0x5a7S0x147: v5a7V147 = SLOAD v5a4V147(0x7)
    0x5a8S0x147: v5a8V147(0x40) = CONST 
    0x5abS0x147: v5abV147 = MLOAD v5a8V147(0x40)
    0x5acS0x147: v5acV147(0x20) = CONST 
    0x5aeS0x147: v5aeV147(0x1f) = CONST 
    0x5b0S0x147: v5b0V147(0x2) = CONST 
    0x5b2S0x147: v5b2V147(0x0) = CONST 
    0x5b4S0x147: v5b4V147(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v5b2V147(0x0)
    0x5b5S0x147: v5b5V147(0x100) = CONST 
    0x5b8S0x147: v5b8V147(0x1) = CONST 
    0x5bbS0x147: v5bbV147 = AND v5a7V147, v5b8V147(0x1)
    0x5bcS0x147: v5bcV147 = ISZERO v5bbV147
    0x5bdS0x147: v5bdV147 = MUL v5bcV147, v5b5V147(0x100)
    0x5beS0x147: v5beV147 = ADD v5bdV147, v5b4V147(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x5c1S0x147: v5c1V147 = AND v5a7V147, v5beV147
    0x5c5S0x147: v5c5V147 = DIV v5c1V147, v5b0V147(0x2)
    0x5c8S0x147: v5c8V147 = ADD v5c5V147, v5aeV147(0x1f)
    0x5cbS0x147: v5cbV147 = DIV v5c8V147, v5acV147(0x20)
    0x5cdS0x147: v5cdV147 = MUL v5acV147(0x20), v5cbV147
    0x5cfS0x147: v5cfV147 = ADD v5abV147, v5cdV147
    0x5d1S0x147: v5d1V147 = ADD v5acV147(0x20), v5cfV147
    0x5d4S0x147: MSTORE v5a8V147(0x40), v5d1V147
    0x5d7S0x147: MSTORE v5abV147, v5c5V147
    0x5d8S0x147: v5d8V147(0x60) = CONST 
    0x5e0S0x147: v5e0V147 = ADD v5abV147, v5acV147(0x20)
    0x5e4S0x147: v5e4V147 = ISZERO v5c5V147
    0x5e5S0x147: v5e5V147(0x62f) = CONST 
    0x5e8S0x147: JUMPI v5e5V147(0x62f), v5e4V147

    Begin block 0x5e9B0x147
    prev=[0x5a3B0x147], succ=[0x5f1B0x147, 0x6040x5a3B0x147]
    =================================
    0x5eaS0x147: v5eaV147(0x1f) = CONST 
    0x5ecS0x147: v5ecV147 = LT v5eaV147(0x1f), v5c5V147
    0x5edS0x147: v5edV147(0x604) = CONST 
    0x5f0S0x147: JUMPI v5edV147(0x604), v5ecV147

    Begin block 0x5f1B0x147
    prev=[0x5e9B0x147], succ=[0x62f0x5a3B0x147]
    =================================
    0x5f1S0x147: v5f1V147(0x100) = CONST 
    0x5f6S0x147: v5f6V147 = SLOAD v5a4V147(0x7)
    0x5f7S0x147: v5f7V147 = DIV v5f6V147, v5f1V147(0x100)
    0x5f8S0x147: v5f8V147 = MUL v5f7V147, v5f1V147(0x100)
    0x5faS0x147: MSTORE v5e0V147, v5f8V147
    0x5fcS0x147: v5fcV147(0x20) = CONST 
    0x5feS0x147: v5feV147 = ADD v5fcV147(0x20), v5e0V147
    0x600S0x147: v600V147(0x62f) = CONST 
    0x603S0x147: JUMP v600V147(0x62f)

    Begin block 0x62f0x5a3B0x147
    prev=[0x5f1B0x147, 0x5a3B0x147, 0x6260x5a3B0x147], succ=[0x6370x5a3B0x147]
    =================================

    Begin block 0x6370x5a3B0x147
    prev=[0x62f0x5a3B0x147], succ=[0x14f0x147]
    =================================
    0x6390x5a3S0x147: JUMP v148(0x14f)

    Begin block 0x14f0x147
    prev=[0x6370x5a3B0x147], succ=[0x1710x147]
    =================================
    0x1500x147: v147150(0x40) = CONST 
    0x1530x147: v147153 = MLOAD v147150(0x40)
    0x1540x147: v147154(0x20) = CONST 
    0x1580x147: MSTORE v147153, v147154(0x20)
    0x15a0x147: v14715a = MLOAD v5abV147
    0x15d0x147: v14715d = ADD v147153, v147154(0x20)
    0x15e0x147: MSTORE v14715d, v14715a
    0x1600x147: v147160 = MLOAD v5abV147
    0x1670x147: v147167 = ADD v147153, v147150(0x40)
    0x16a0x147: v14716a = ADD v5abV147, v147154(0x20)
    0x16f0x147: v14716f(0x0) = CONST 

    Begin block 0x1710x147
    prev=[0x17a0x147, 0x14f0x147], succ=[0x1890x147, 0x17a0x147]
    =================================
    0x1710x147_0x0: v171147_0 = PHI v147184, v14716f(0x0)
    0x1740x147: v147174 = LT v171147_0, v147160
    0x1750x147: v147175 = ISZERO v147174
    0x1760x147: v147176(0x189) = CONST 
    0x1790x147: JUMPI v147176(0x189), v147175

    Begin block 0x1890x147
    prev=[0x1710x147], succ=[0x1b60x147, 0x19d0x147]
    =================================
    0x1920x147: v147192 = ADD v147160, v147167
    0x1940x147: v147194(0x1f) = CONST 
    0x1960x147: v147196 = AND v147194(0x1f), v147160
    0x1980x147: v147198 = ISZERO v147196
    0x1990x147: v147199(0x1b6) = CONST 
    0x19c0x147: JUMPI v147199(0x1b6), v147198

    Begin block 0x1b60x147
    prev=[0x1890x147, 0x19d0x147], succ=[]
    =================================
    0x1b60x147_0x1: v1b6147_1 = PHI v1471b3, v147192
    0x1bc0x147: v1471bc(0x40) = CONST 
    0x1be0x147: v1471be = MLOAD v1471bc(0x40)
    0x1c10x147: v1471c1 = SUB v1b6147_1, v1471be
    0x1c30x147: RETURN v1471be, v1471c1

    Begin block 0x19d0x147
    prev=[0x1890x147], succ=[0x1b60x147]
    =================================
    0x19f0x147: v14719f = SUB v147192, v147196
    0x1a10x147: v1471a1 = MLOAD v14719f
    0x1a20x147: v1471a2(0x1) = CONST 
    0x1a50x147: v1471a5(0x20) = CONST 
    0x1a70x147: v1471a7 = SUB v1471a5(0x20), v147196
    0x1a80x147: v1471a8(0x100) = CONST 
    0x1ab0x147: v1471ab = EXP v1471a8(0x100), v1471a7
    0x1ac0x147: v1471ac = SUB v1471ab, v1471a2(0x1)
    0x1ad0x147: v1471ad = NOT v1471ac
    0x1ae0x147: v1471ae = AND v1471ad, v1471a1
    0x1b00x147: MSTORE v14719f, v1471ae
    0x1b10x147: v1471b1(0x20) = CONST 
    0x1b30x147: v1471b3 = ADD v1471b1(0x20), v14719f

    Begin block 0x17a0x147
    prev=[0x1710x147], succ=[0x1710x147]
    =================================
    0x17a0x147_0x0: v17a147_0 = PHI v147184, v14716f(0x0)
    0x17c0x147: v14717c = ADD v17a147_0, v14716a
    0x17d0x147: v14717d = MLOAD v14717c
    0x1800x147: v147180 = ADD v17a147_0, v147167
    0x1810x147: MSTORE v147180, v14717d
    0x1820x147: v147182(0x20) = CONST 
    0x1840x147: v147184 = ADD v147182(0x20), v17a147_0
    0x1850x147: v147185(0x171) = CONST 
    0x1880x147: JUMP v147185(0x171)

    Begin block 0x6040x5a3B0x147
    prev=[0x5e9B0x147], succ=[0x6120x5a3B0x147]
    =================================
    0x6060x5a3S0x147: v5a3606V147 = ADD v5e0V147, v5c5V147
    0x6090x5a3S0x147: v5a3609V147(0x0) = CONST 
    0x60b0x5a3S0x147: MSTORE v5a3609V147(0x0), v5a4V147(0x7)
    0x60c0x5a3S0x147: v5a360cV147(0x20) = CONST 
    0x60e0x5a3S0x147: v5a360eV147(0x0) = CONST 
    0x6100x5a3S0x147: v5a3610V147 = SHA3 v5a360eV147(0x0), v5a360cV147(0x20)

    Begin block 0x6120x5a3B0x147
    prev=[0x6040x5a3B0x147, 0x6120x5a3B0x147], succ=[0x6120x5a3B0x147, 0x6260x5a3B0x147]
    =================================
    0x6120x5a3_0x0S0x147: v6125a3_0V147 = PHI v5e0V147, v5a361eV147
    0x6120x5a3_0x1S0x147: v6125a3_1V147 = PHI v5a3610V147, v5a361aV147
    0x6140x5a3S0x147: v5a3614V147 = SLOAD v6125a3_1V147
    0x6160x5a3S0x147: MSTORE v6125a3_0V147, v5a3614V147
    0x6180x5a3S0x147: v5a3618V147(0x1) = CONST 
    0x61a0x5a3S0x147: v5a361aV147 = ADD v5a3618V147(0x1), v6125a3_1V147
    0x61c0x5a3S0x147: v5a361cV147(0x20) = CONST 
    0x61e0x5a3S0x147: v5a361eV147 = ADD v5a361cV147(0x20), v6125a3_0V147
    0x6210x5a3S0x147: v5a3621V147 = GT v5a3606V147, v5a361eV147
    0x6220x5a3S0x147: v5a3622V147(0x612) = CONST 
    0x6250x5a3S0x147: JUMPI v5a3622V147(0x612), v5a3621V147

    Begin block 0x6260x5a3B0x147
    prev=[0x6120x5a3B0x147], succ=[0x62f0x5a3B0x147]
    =================================
    0x6280x5a3S0x147: v5a3628V147 = SUB v5a361eV147, v5a3606V147
    0x6290x5a3S0x147: v5a3629V147(0x1f) = CONST 
    0x62b0x5a3S0x147: v5a362bV147 = AND v5a3629V147(0x1f), v5a3628V147
    0x62d0x5a3S0x147: v5a362dV147 = ADD v5a3606V147, v5a362bV147

}

function fallback()() public {
    Begin block 0x156c
    prev=[], succ=[]
    =================================
    0x156d: v156d(0x0) = CONST 
    0x1570: REVERT v156d(0x0), v156d(0x0)

}

function approve(address,uint256)() public {
    Begin block 0x1c4
    prev=[], succ=[0x1d6, 0x1da]
    =================================
    0x1c5: v1c5(0x15fc) = CONST 
    0x1c8: v1c8(0x4) = CONST 
    0x1cb: v1cb = CALLDATASIZE 
    0x1cc: v1cc = SUB v1cb, v1c8(0x4)
    0x1cd: v1cd(0x40) = CONST 
    0x1d0: v1d0 = LT v1cc, v1cd(0x40)
    0x1d1: v1d1 = ISZERO v1d0
    0x1d2: v1d2(0x1da) = CONST 
    0x1d5: JUMPI v1d2(0x1da), v1d1

    Begin block 0x1d6
    prev=[0x1c4], succ=[]
    =================================
    0x1d6: v1d6(0x0) = CONST 
    0x1d9: REVERT v1d6(0x0), v1d6(0x0)

    Begin block 0x1da
    prev=[0x1c4], succ=[0x63a]
    =================================
    0x1dc: v1dc(0x1) = CONST 
    0x1de: v1de(0x1) = CONST 
    0x1e0: v1e0(0xa0) = CONST 
    0x1e2: v1e2(0x10000000000000000000000000000000000000000) = SHL v1e0(0xa0), v1de(0x1)
    0x1e3: v1e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e2(0x10000000000000000000000000000000000000000), v1dc(0x1)
    0x1e5: v1e5 = CALLDATALOAD v1c8(0x4)
    0x1e6: v1e6 = AND v1e5, v1e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e8: v1e8(0x20) = CONST 
    0x1ea: v1ea(0x24) = ADD v1e8(0x20), v1c8(0x4)
    0x1eb: v1eb = CALLDATALOAD v1ea(0x24)
    0x1ec: v1ec(0x63a) = CONST 
    0x1ef: JUMP v1ec(0x63a)

    Begin block 0x63a
    prev=[0x1da], succ=[0xd18B0x63a]
    =================================
    0x63b: v63b(0x0) = CONST 
    0x63d: v63d(0x1951) = CONST 
    0x640: v640(0x647) = CONST 
    0x643: v643(0xd18) = CONST 
    0x646: JUMP v643(0xd18)

    Begin block 0xd18B0x63a
    prev=[0x63a], succ=[0x647]
    =================================
    0xd19S0x63a: vd19V63a = CALLER 
    0xd1bS0x63a: JUMP v640(0x647)

    Begin block 0x647
    prev=[0xd18B0x63a], succ=[0x1951]
    =================================
    0x64a: v64a(0xd1c) = CONST 
    0x64d: CALLPRIVATE v64a(0xd1c), v1eb, v1e6, vd19V63a, v63d(0x1951)

    Begin block 0x1951
    prev=[0x647], succ=[0x15fc]
    =================================
    0x1953: v1953(0x1) = CONST 
    0x1959: JUMP v1c5(0x15fc)

    Begin block 0x15fc
    prev=[0x1951], succ=[]
    =================================
    0x15fd: v15fd(0x40) = CONST 
    0x1600: v1600 = MLOAD v15fd(0x40)
    0x1602: v1602 = ISZERO v1953(0x1)
    0x1603: v1603 = ISZERO v1602
    0x1605: MSTORE v1600, v1603
    0x1606: v1606 = MLOAD v15fd(0x40)
    0x160a: v160a(0x0) = SUB v1600, v1606
    0x160b: v160b(0x20) = CONST 
    0x160d: v160d(0x20) = ADD v160b(0x20), v160a(0x0)
    0x160f: RETURN v1606, v160d(0x20)

}

function initialize(string,string,uint8)() public {
    Begin block 0x204
    prev=[], succ=[0x216, 0x21a]
    =================================
    0x205: v205(0x162f) = CONST 
    0x208: v208(0x4) = CONST 
    0x20b: v20b = CALLDATASIZE 
    0x20c: v20c = SUB v20b, v208(0x4)
    0x20d: v20d(0x60) = CONST 
    0x210: v210 = LT v20c, v20d(0x60)
    0x211: v211 = ISZERO v210
    0x212: v212(0x21a) = CONST 
    0x215: JUMPI v212(0x21a), v211

    Begin block 0x216
    prev=[0x204], succ=[]
    =================================
    0x216: v216(0x0) = CONST 
    0x219: REVERT v216(0x0), v216(0x0)

    Begin block 0x21a
    prev=[0x204], succ=[0x231, 0x235]
    =================================
    0x21c: v21c = ADD v208(0x4), v20c
    0x21e: v21e(0x20) = CONST 
    0x221: v221(0x24) = ADD v208(0x4), v21e(0x20)
    0x223: v223 = CALLDATALOAD v208(0x4)
    0x224: v224(0x100000000) = CONST 
    0x22b: v22b = GT v223, v224(0x100000000)
    0x22c: v22c = ISZERO v22b
    0x22d: v22d(0x235) = CONST 
    0x230: JUMPI v22d(0x235), v22c

    Begin block 0x231
    prev=[0x21a], succ=[]
    =================================
    0x231: v231(0x0) = CONST 
    0x234: REVERT v231(0x0), v231(0x0)

    Begin block 0x235
    prev=[0x21a], succ=[0x243, 0x247]
    =================================
    0x237: v237 = ADD v208(0x4), v223
    0x239: v239(0x20) = CONST 
    0x23c: v23c = ADD v237, v239(0x20)
    0x23d: v23d = GT v23c, v21c
    0x23e: v23e = ISZERO v23d
    0x23f: v23f(0x247) = CONST 
    0x242: JUMPI v23f(0x247), v23e

    Begin block 0x243
    prev=[0x235], succ=[]
    =================================
    0x243: v243(0x0) = CONST 
    0x246: REVERT v243(0x0), v243(0x0)

    Begin block 0x247
    prev=[0x235], succ=[0x265, 0x269]
    =================================
    0x249: v249 = CALLDATALOAD v237
    0x24b: v24b(0x20) = CONST 
    0x24d: v24d = ADD v24b(0x20), v237
    0x250: v250(0x1) = CONST 
    0x253: v253 = MUL v249, v250(0x1)
    0x255: v255 = ADD v24d, v253
    0x256: v256 = GT v255, v21c
    0x257: v257(0x100000000) = CONST 
    0x25e: v25e = GT v249, v257(0x100000000)
    0x25f: v25f = OR v25e, v256
    0x260: v260 = ISZERO v25f
    0x261: v261(0x269) = CONST 
    0x264: JUMPI v261(0x269), v260

    Begin block 0x265
    prev=[0x247], succ=[]
    =================================
    0x265: v265(0x0) = CONST 
    0x268: REVERT v265(0x0), v265(0x0)

    Begin block 0x269
    prev=[0x247], succ=[0x2b8, 0x2bc]
    =================================
    0x26e: v26e(0x1f) = CONST 
    0x270: v270 = ADD v26e(0x1f), v249
    0x271: v271(0x20) = CONST 
    0x275: v275 = DIV v270, v271(0x20)
    0x276: v276 = MUL v275, v271(0x20)
    0x277: v277(0x20) = CONST 
    0x279: v279 = ADD v277(0x20), v276
    0x27a: v27a(0x40) = CONST 
    0x27c: v27c = MLOAD v27a(0x40)
    0x27f: v27f = ADD v27c, v279
    0x280: v280(0x40) = CONST 
    0x282: MSTORE v280(0x40), v27f
    0x28a: MSTORE v27c, v249
    0x28b: v28b(0x20) = CONST 
    0x28d: v28d = ADD v28b(0x20), v27c
    0x293: CALLDATACOPY v28d, v24d, v249
    0x294: v294(0x0) = CONST 
    0x297: v297 = ADD v28d, v249
    0x29b: MSTORE v297, v294(0x0)
    0x2a1: v2a1(0x20) = CONST 
    0x2a4: v2a4(0x44) = ADD v221(0x24), v2a1(0x20)
    0x2a7: v2a7 = CALLDATALOAD v221(0x24)
    0x2ab: v2ab(0x100000000) = CONST 
    0x2b2: v2b2 = GT v2a7, v2ab(0x100000000)
    0x2b3: v2b3 = ISZERO v2b2
    0x2b4: v2b4(0x2bc) = CONST 
    0x2b7: JUMPI v2b4(0x2bc), v2b3

    Begin block 0x2b8
    prev=[0x269], succ=[]
    =================================
    0x2b8: v2b8(0x0) = CONST 
    0x2bb: REVERT v2b8(0x0), v2b8(0x0)

    Begin block 0x2bc
    prev=[0x269], succ=[0x2ca, 0x2ce]
    =================================
    0x2be: v2be = ADD v208(0x4), v2a7
    0x2c0: v2c0(0x20) = CONST 
    0x2c3: v2c3 = ADD v2be, v2c0(0x20)
    0x2c4: v2c4 = GT v2c3, v21c
    0x2c5: v2c5 = ISZERO v2c4
    0x2c6: v2c6(0x2ce) = CONST 
    0x2c9: JUMPI v2c6(0x2ce), v2c5

    Begin block 0x2ca
    prev=[0x2bc], succ=[]
    =================================
    0x2ca: v2ca(0x0) = CONST 
    0x2cd: REVERT v2ca(0x0), v2ca(0x0)

    Begin block 0x2ce
    prev=[0x2bc], succ=[0x2ec, 0x2f0]
    =================================
    0x2d0: v2d0 = CALLDATALOAD v2be
    0x2d2: v2d2(0x20) = CONST 
    0x2d4: v2d4 = ADD v2d2(0x20), v2be
    0x2d7: v2d7(0x1) = CONST 
    0x2da: v2da = MUL v2d0, v2d7(0x1)
    0x2dc: v2dc = ADD v2d4, v2da
    0x2dd: v2dd = GT v2dc, v21c
    0x2de: v2de(0x100000000) = CONST 
    0x2e5: v2e5 = GT v2d0, v2de(0x100000000)
    0x2e6: v2e6 = OR v2e5, v2dd
    0x2e7: v2e7 = ISZERO v2e6
    0x2e8: v2e8(0x2f0) = CONST 
    0x2eb: JUMPI v2e8(0x2f0), v2e7

    Begin block 0x2ec
    prev=[0x2ce], succ=[]
    =================================
    0x2ec: v2ec(0x0) = CONST 
    0x2ef: REVERT v2ec(0x0), v2ec(0x0)

    Begin block 0x2f0
    prev=[0x2ce], succ=[0x657]
    =================================
    0x2f5: v2f5(0x1f) = CONST 
    0x2f7: v2f7 = ADD v2f5(0x1f), v2d0
    0x2f8: v2f8(0x20) = CONST 
    0x2fc: v2fc = DIV v2f7, v2f8(0x20)
    0x2fd: v2fd = MUL v2fc, v2f8(0x20)
    0x2fe: v2fe(0x20) = CONST 
    0x300: v300 = ADD v2fe(0x20), v2fd
    0x301: v301(0x40) = CONST 
    0x303: v303 = MLOAD v301(0x40)
    0x306: v306 = ADD v303, v300
    0x307: v307(0x40) = CONST 
    0x309: MSTORE v307(0x40), v306
    0x311: MSTORE v303, v2d0
    0x312: v312(0x20) = CONST 
    0x314: v314 = ADD v312(0x20), v303
    0x31a: CALLDATACOPY v314, v2d4, v2d0
    0x31b: v31b(0x0) = CONST 
    0x31e: v31e = ADD v314, v2d0
    0x322: MSTORE v31e, v31b(0x0)
    0x32a: v32a = CALLDATALOAD v2a4(0x44)
    0x32b: v32b(0xff) = CONST 
    0x32d: v32d = AND v32b(0xff), v32a
    0x330: v330(0x657) = CONST 
    0x335: JUMP v330(0x657)

    Begin block 0x657
    prev=[0x2f0], succ=[0x668, 0x6b4]
    =================================
    0x658: v658(0x9) = CONST 
    0x65a: v65a = SLOAD v658(0x9)
    0x65b: v65b(0x100) = CONST 
    0x65f: v65f = DIV v65a, v65b(0x100)
    0x660: v660(0xff) = CONST 
    0x662: v662 = AND v660(0xff), v65f
    0x663: v663 = ISZERO v662
    0x664: v664(0x6b4) = CONST 
    0x667: JUMPI v664(0x6b4), v663

    Begin block 0x668
    prev=[0x657], succ=[]
    =================================
    0x668: v668(0x40) = CONST 
    0x66b: v66b = MLOAD v668(0x40)
    0x66c: v66c(0x461bcd) = CONST 
    0x670: v670(0xe5) = CONST 
    0x672: v672(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v670(0xe5), v66c(0x461bcd)
    0x674: MSTORE v66b, v672(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x675: v675(0x20) = CONST 
    0x677: v677(0x4) = CONST 
    0x67a: v67a = ADD v66b, v677(0x4)
    0x67d: MSTORE v67a, v675(0x20)
    0x67e: v67e(0x24) = CONST 
    0x681: v681 = ADD v66b, v67e(0x24)
    0x682: MSTORE v681, v675(0x20)
    0x683: v683(0x696e697469616c697a653a20416c726561647920696e697469616c697a656421) = CONST 
    0x6a4: v6a4(0x44) = CONST 
    0x6a7: v6a7 = ADD v66b, v6a4(0x44)
    0x6a8: MSTORE v6a7, v683(0x696e697469616c697a653a20416c726561647920696e697469616c697a656421)
    0x6aa: v6aa = MLOAD v668(0x40)
    0x6ae: v6ae(0x0) = SUB v66b, v6aa
    0x6af: v6af(0x64) = CONST 
    0x6b1: v6b1(0x64) = ADD v6af(0x64), v6ae(0x0)
    0x6b3: REVERT v6aa, v6b1(0x64)

    Begin block 0x6b4
    prev=[0x657], succ=[0x1308B0x6b4]
    =================================
    0x6b5: v6b5(0x0) = CONST 
    0x6b8: v6b8 = SLOAD v6b5(0x0)
    0x6b9: v6b9(0x1) = CONST 
    0x6bb: v6bb(0x1) = CONST 
    0x6bd: v6bd(0xa0) = CONST 
    0x6bf: v6bf(0x10000000000000000000000000000000000000000) = SHL v6bd(0xa0), v6bb(0x1)
    0x6c0: v6c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6bf(0x10000000000000000000000000000000000000000), v6b9(0x1)
    0x6c1: v6c1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c2: v6c2 = AND v6c1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6b8
    0x6c3: v6c3 = CALLER 
    0x6c4: v6c4 = OR v6c3, v6c2
    0x6c6: SSTORE v6b5(0x0), v6c4
    0x6c8: v6c8 = MLOAD v27c
    0x6c9: v6c9(0x6d9) = CONST 
    0x6cd: v6cd(0x7) = CONST 
    0x6d0: v6d0(0x20) = CONST 
    0x6d3: v6d3 = ADD v27c, v6d0(0x20)
    0x6d5: v6d5(0x1308) = CONST 
    0x6d8: JUMP v6d5(0x1308)

    Begin block 0x1308B0x6b4
    prev=[0x6b4], succ=[0x1349B0x6b4, 0x1339B0x6b4]
    =================================
    0x130bS0x6b4: v130bV6b4 = SLOAD v6cd(0x7)
    0x130cS0x6b4: v130cV6b4(0x1) = CONST 
    0x130fS0x6b4: v130fV6b4(0x1) = CONST 
    0x1311S0x6b4: v1311V6b4 = AND v130fV6b4(0x1), v130bV6b4
    0x1312S0x6b4: v1312V6b4 = ISZERO v1311V6b4
    0x1313S0x6b4: v1313V6b4(0x100) = CONST 
    0x1316S0x6b4: v1316V6b4 = MUL v1313V6b4(0x100), v1312V6b4
    0x1317S0x6b4: v1317V6b4 = SUB v1316V6b4, v130cV6b4(0x1)
    0x1318S0x6b4: v1318V6b4 = AND v1317V6b4, v130bV6b4
    0x1319S0x6b4: v1319V6b4(0x2) = CONST 
    0x131cS0x6b4: v131cV6b4 = DIV v1318V6b4, v1319V6b4(0x2)
    0x131eS0x6b4: v131eV6b4(0x0) = CONST 
    0x1320S0x6b4: MSTORE v131eV6b4(0x0), v6cd(0x7)
    0x1321S0x6b4: v1321V6b4(0x20) = CONST 
    0x1323S0x6b4: v1323V6b4(0x0) = CONST 
    0x1325S0x6b4: v1325V6b4 = SHA3 v1323V6b4(0x0), v1321V6b4(0x20)
    0x1327S0x6b4: v1327V6b4(0x1f) = CONST 
    0x1329S0x6b4: v1329V6b4 = ADD v1327V6b4(0x1f), v131cV6b4
    0x132aS0x6b4: v132aV6b4(0x20) = CONST 
    0x132dS0x6b4: v132dV6b4 = DIV v1329V6b4, v132aV6b4(0x20)
    0x132fS0x6b4: v132fV6b4 = ADD v1325V6b4, v132dV6b4
    0x1332S0x6b4: v1332V6b4(0x1f) = CONST 
    0x1334S0x6b4: v1334V6b4 = LT v1332V6b4(0x1f), v6c8
    0x1335S0x6b4: v1335V6b4(0x1349) = CONST 
    0x1338S0x6b4: JUMPI v1335V6b4(0x1349), v1334V6b4

    Begin block 0x1349B0x6b4
    prev=[0x1308B0x6b4], succ=[0x1376B0x6b4, 0x1358B0x6b4]
    =================================
    0x134cS0x6b4: v134cV6b4 = ADD v6c8, v6c8
    0x134dS0x6b4: v134dV6b4(0x1) = CONST 
    0x134fS0x6b4: v134fV6b4 = ADD v134dV6b4(0x1), v134cV6b4
    0x1351S0x6b4: SSTORE v6cd(0x7), v134fV6b4
    0x1353S0x6b4: v1353V6b4 = ISZERO v6c8
    0x1354S0x6b4: v1354V6b4(0x1376) = CONST 
    0x1357S0x6b4: JUMPI v1354V6b4(0x1376), v1353V6b4

    Begin block 0x1376B0x6b4
    prev=[0x1349B0x6b4, 0x135bB0x6b4, 0x1339B0x6b4], succ=[0x1386B0x1376B0x6b4]
    =================================
    0x1376_0x1S0x6b4: v1376_1V6b4 = PHI v1325V6b4, v1370V6b4
    0x1378S0x6b4: v1378V6b4(0x1aa9) = CONST 
    0x137eS0x6b4: v137eV6b4(0x1386) = CONST 
    0x1381S0x6b4: JUMP v137eV6b4(0x1386)

    Begin block 0x1386B0x1376B0x6b4
    prev=[0x1376B0x6b4], succ=[0x138cB0x1376B0x6b4]
    =================================
    0x1387S0x1376S0x6b4: v1387V1376V6b4(0x637) = CONST 

    Begin block 0x138cB0x1376B0x6b4
    prev=[0x1395B0x1376B0x6b4, 0x1386B0x1376B0x6b4], succ=[0x1395B0x1376B0x6b4, 0x1accB0x1376B0x6b4]
    =================================
    0x138c_0x0S0x1376S0x6b4: v138c_0V1376V6b4 = PHI v1376_1V6b4, v139bV1376V6b4
    0x138fS0x1376S0x6b4: v138fV1376V6b4 = GT v132fV6b4, v138c_0V1376V6b4
    0x1390S0x1376S0x6b4: v1390V1376V6b4 = ISZERO v138fV1376V6b4
    0x1391S0x1376S0x6b4: v1391V1376V6b4(0x1acc) = CONST 
    0x1394S0x1376S0x6b4: JUMPI v1391V1376V6b4(0x1acc), v1390V1376V6b4

    Begin block 0x1395B0x1376B0x6b4
    prev=[0x138cB0x1376B0x6b4], succ=[0x138cB0x1376B0x6b4]
    =================================
    0x1395S0x1376S0x6b4: v1395V1376V6b4(0x0) = CONST 
    0x1395_0x0S0x1376S0x6b4: v1395_0V1376V6b4 = PHI v1376_1V6b4, v139bV1376V6b4
    0x1398S0x1376S0x6b4: SSTORE v1395_0V1376V6b4, v1395V1376V6b4(0x0)
    0x1399S0x1376S0x6b4: v1399V1376V6b4(0x1) = CONST 
    0x139bS0x1376S0x6b4: v139bV1376V6b4 = ADD v1399V1376V6b4(0x1), v1395_0V1376V6b4
    0x139cS0x1376S0x6b4: v139cV1376V6b4(0x138c) = CONST 
    0x139fS0x1376S0x6b4: JUMP v139cV1376V6b4(0x138c)

    Begin block 0x1accB0x1376B0x6b4
    prev=[0x138cB0x1376B0x6b4], succ=[0x6370x1386B0x1376B0x6b4]
    =================================
    0x1acfS0x1376S0x6b4: JUMP v1387V1376V6b4(0x637)

    Begin block 0x6370x1386B0x1376B0x6b4
    prev=[0x1accB0x1376B0x6b4], succ=[0x1aa9B0x6b4]
    =================================
    0x6390x1386S0x1376S0x6b4: JUMP v1378V6b4(0x1aa9)

    Begin block 0x1aa9B0x6b4
    prev=[0x6370x1386B0x1376B0x6b4], succ=[0x6d9]
    =================================
    0x1aacS0x6b4: JUMP v6c9(0x6d9)

    Begin block 0x6d9
    prev=[0x1aa9B0x6b4], succ=[0x1308B0x6d9]
    =================================
    0x6dc: v6dc = MLOAD v303
    0x6dd: v6dd(0x6ed) = CONST 
    0x6e1: v6e1(0x8) = CONST 
    0x6e4: v6e4(0x20) = CONST 
    0x6e7: v6e7 = ADD v303, v6e4(0x20)
    0x6e9: v6e9(0x1308) = CONST 
    0x6ec: JUMP v6e9(0x1308)

    Begin block 0x1308B0x6d9
    prev=[0x6d9], succ=[0x1349B0x6d9, 0x1339B0x6d9]
    =================================
    0x130bS0x6d9: v130bV6d9 = SLOAD v6e1(0x8)
    0x130cS0x6d9: v130cV6d9(0x1) = CONST 
    0x130fS0x6d9: v130fV6d9(0x1) = CONST 
    0x1311S0x6d9: v1311V6d9 = AND v130fV6d9(0x1), v130bV6d9
    0x1312S0x6d9: v1312V6d9 = ISZERO v1311V6d9
    0x1313S0x6d9: v1313V6d9(0x100) = CONST 
    0x1316S0x6d9: v1316V6d9 = MUL v1313V6d9(0x100), v1312V6d9
    0x1317S0x6d9: v1317V6d9 = SUB v1316V6d9, v130cV6d9(0x1)
    0x1318S0x6d9: v1318V6d9 = AND v1317V6d9, v130bV6d9
    0x1319S0x6d9: v1319V6d9(0x2) = CONST 
    0x131cS0x6d9: v131cV6d9 = DIV v1318V6d9, v1319V6d9(0x2)
    0x131eS0x6d9: v131eV6d9(0x0) = CONST 
    0x1320S0x6d9: MSTORE v131eV6d9(0x0), v6e1(0x8)
    0x1321S0x6d9: v1321V6d9(0x20) = CONST 
    0x1323S0x6d9: v1323V6d9(0x0) = CONST 
    0x1325S0x6d9: v1325V6d9 = SHA3 v1323V6d9(0x0), v1321V6d9(0x20)
    0x1327S0x6d9: v1327V6d9(0x1f) = CONST 
    0x1329S0x6d9: v1329V6d9 = ADD v1327V6d9(0x1f), v131cV6d9
    0x132aS0x6d9: v132aV6d9(0x20) = CONST 
    0x132dS0x6d9: v132dV6d9 = DIV v1329V6d9, v132aV6d9(0x20)
    0x132fS0x6d9: v132fV6d9 = ADD v1325V6d9, v132dV6d9
    0x1332S0x6d9: v1332V6d9(0x1f) = CONST 
    0x1334S0x6d9: v1334V6d9 = LT v1332V6d9(0x1f), v6dc
    0x1335S0x6d9: v1335V6d9(0x1349) = CONST 
    0x1338S0x6d9: JUMPI v1335V6d9(0x1349), v1334V6d9

    Begin block 0x1349B0x6d9
    prev=[0x1308B0x6d9], succ=[0x1376B0x6d9, 0x1358B0x6d9]
    =================================
    0x134cS0x6d9: v134cV6d9 = ADD v6dc, v6dc
    0x134dS0x6d9: v134dV6d9(0x1) = CONST 
    0x134fS0x6d9: v134fV6d9 = ADD v134dV6d9(0x1), v134cV6d9
    0x1351S0x6d9: SSTORE v6e1(0x8), v134fV6d9
    0x1353S0x6d9: v1353V6d9 = ISZERO v6dc
    0x1354S0x6d9: v1354V6d9(0x1376) = CONST 
    0x1357S0x6d9: JUMPI v1354V6d9(0x1376), v1353V6d9

    Begin block 0x1376B0x6d9
    prev=[0x1349B0x6d9, 0x135bB0x6d9, 0x1339B0x6d9], succ=[0x1386B0x1376B0x6d9]
    =================================
    0x1376_0x1S0x6d9: v1376_1V6d9 = PHI v1325V6d9, v1370V6d9
    0x1378S0x6d9: v1378V6d9(0x1aa9) = CONST 
    0x137eS0x6d9: v137eV6d9(0x1386) = CONST 
    0x1381S0x6d9: JUMP v137eV6d9(0x1386)

    Begin block 0x1386B0x1376B0x6d9
    prev=[0x1376B0x6d9], succ=[0x138cB0x1376B0x6d9]
    =================================
    0x1387S0x1376S0x6d9: v1387V1376V6d9(0x637) = CONST 

    Begin block 0x138cB0x1376B0x6d9
    prev=[0x1395B0x1376B0x6d9, 0x1386B0x1376B0x6d9], succ=[0x1395B0x1376B0x6d9, 0x1accB0x1376B0x6d9]
    =================================
    0x138c_0x0S0x1376S0x6d9: v138c_0V1376V6d9 = PHI v1376_1V6d9, v139bV1376V6d9
    0x138fS0x1376S0x6d9: v138fV1376V6d9 = GT v132fV6d9, v138c_0V1376V6d9
    0x1390S0x1376S0x6d9: v1390V1376V6d9 = ISZERO v138fV1376V6d9
    0x1391S0x1376S0x6d9: v1391V1376V6d9(0x1acc) = CONST 
    0x1394S0x1376S0x6d9: JUMPI v1391V1376V6d9(0x1acc), v1390V1376V6d9

    Begin block 0x1395B0x1376B0x6d9
    prev=[0x138cB0x1376B0x6d9], succ=[0x138cB0x1376B0x6d9]
    =================================
    0x1395S0x1376S0x6d9: v1395V1376V6d9(0x0) = CONST 
    0x1395_0x0S0x1376S0x6d9: v1395_0V1376V6d9 = PHI v1376_1V6d9, v139bV1376V6d9
    0x1398S0x1376S0x6d9: SSTORE v1395_0V1376V6d9, v1395V1376V6d9(0x0)
    0x1399S0x1376S0x6d9: v1399V1376V6d9(0x1) = CONST 
    0x139bS0x1376S0x6d9: v139bV1376V6d9 = ADD v1399V1376V6d9(0x1), v1395_0V1376V6d9
    0x139cS0x1376S0x6d9: v139cV1376V6d9(0x138c) = CONST 
    0x139fS0x1376S0x6d9: JUMP v139cV1376V6d9(0x138c)

    Begin block 0x1accB0x1376B0x6d9
    prev=[0x138cB0x1376B0x6d9], succ=[0x6370x1386B0x1376B0x6d9]
    =================================
    0x1acfS0x1376S0x6d9: JUMP v1387V1376V6d9(0x637)

    Begin block 0x6370x1386B0x1376B0x6d9
    prev=[0x1accB0x1376B0x6d9], succ=[0x1aa9B0x6d9]
    =================================
    0x6390x1386S0x1376S0x6d9: JUMP v1378V6d9(0x1aa9)

    Begin block 0x1aa9B0x6d9
    prev=[0x6370x1386B0x1376B0x6d9], succ=[0x6ed]
    =================================
    0x1aacS0x6d9: JUMP v6dd(0x6ed)

    Begin block 0x6ed
    prev=[0x1aa9B0x6d9], succ=[0x162f]
    =================================
    0x6ef: v6ef(0x9) = CONST 
    0x6f2: v6f2 = SLOAD v6ef(0x9)
    0x6f3: v6f3(0x100) = CONST 
    0x6f6: v6f6(0xff) = CONST 
    0x6f8: v6f8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v6f6(0xff)
    0x6fb: v6fb = AND v6f2, v6f8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x6fc: v6fc(0xff) = CONST 
    0x6ff: v6ff = AND v32d, v6fc(0xff)
    0x700: v700 = OR v6ff, v6fb
    0x701: v701(0xff00) = CONST 
    0x704: v704(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v701(0xff00)
    0x705: v705 = AND v704(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v700
    0x706: v706 = OR v705, v6f3(0x100)
    0x708: SSTORE v6ef(0x9), v706
    0x709: v709(0x40) = CONST 
    0x70b: v70b = MLOAD v709(0x40)
    0x70c: v70c = CALLER 
    0x70e: v70e(0x0) = CONST 
    0x711: v711(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x735: LOG3 v70b, v70e(0x0), v711(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v70e(0x0), v70c
    0x739: JUMP v205(0x162f)

    Begin block 0x162f
    prev=[0x6ed], succ=[]
    =================================
    0x1630: STOP 

    Begin block 0x1358B0x6d9
    prev=[0x1349B0x6d9], succ=[0x135bB0x6d9]
    =================================
    0x135aS0x6d9: v135aV6d9 = ADD v6e7, v6dc

    Begin block 0x135bB0x6d9
    prev=[0x1358B0x6d9, 0x1364B0x6d9], succ=[0x1376B0x6d9, 0x1364B0x6d9]
    =================================
    0x135b_0x2S0x6d9: v135b_2V6d9 = PHI v6e7, v136bV6d9
    0x135eS0x6d9: v135eV6d9 = GT v135aV6d9, v135b_2V6d9
    0x135fS0x6d9: v135fV6d9 = ISZERO v135eV6d9
    0x1360S0x6d9: v1360V6d9(0x1376) = CONST 
    0x1363S0x6d9: JUMPI v1360V6d9(0x1376), v135fV6d9

    Begin block 0x1364B0x6d9
    prev=[0x135bB0x6d9], succ=[0x135bB0x6d9]
    =================================
    0x1364_0x1S0x6d9: v1364_1V6d9 = PHI v1325V6d9, v1370V6d9
    0x1364_0x2S0x6d9: v1364_2V6d9 = PHI v6e7, v136bV6d9
    0x1365S0x6d9: v1365V6d9 = MLOAD v1364_2V6d9
    0x1367S0x6d9: SSTORE v1364_1V6d9, v1365V6d9
    0x1369S0x6d9: v1369V6d9(0x20) = CONST 
    0x136bS0x6d9: v136bV6d9 = ADD v1369V6d9(0x20), v1364_2V6d9
    0x136eS0x6d9: v136eV6d9(0x1) = CONST 
    0x1370S0x6d9: v1370V6d9 = ADD v136eV6d9(0x1), v1364_1V6d9
    0x1372S0x6d9: v1372V6d9(0x135b) = CONST 
    0x1375S0x6d9: JUMP v1372V6d9(0x135b)

    Begin block 0x1339B0x6d9
    prev=[0x1308B0x6d9], succ=[0x1376B0x6d9]
    =================================
    0x133aS0x6d9: v133aV6d9 = MLOAD v6e7
    0x133bS0x6d9: v133bV6d9(0xff) = CONST 
    0x133dS0x6d9: v133dV6d9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v133bV6d9(0xff)
    0x133eS0x6d9: v133eV6d9 = AND v133dV6d9(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v133aV6d9
    0x1341S0x6d9: v1341V6d9 = ADD v6dc, v6dc
    0x1342S0x6d9: v1342V6d9 = OR v1341V6d9, v133eV6d9
    0x1344S0x6d9: SSTORE v6e1(0x8), v1342V6d9
    0x1345S0x6d9: v1345V6d9(0x1376) = CONST 
    0x1348S0x6d9: JUMP v1345V6d9(0x1376)

    Begin block 0x1358B0x6b4
    prev=[0x1349B0x6b4], succ=[0x135bB0x6b4]
    =================================
    0x135aS0x6b4: v135aV6b4 = ADD v6d3, v6c8

    Begin block 0x135bB0x6b4
    prev=[0x1358B0x6b4, 0x1364B0x6b4], succ=[0x1376B0x6b4, 0x1364B0x6b4]
    =================================
    0x135b_0x2S0x6b4: v135b_2V6b4 = PHI v6d3, v136bV6b4
    0x135eS0x6b4: v135eV6b4 = GT v135aV6b4, v135b_2V6b4
    0x135fS0x6b4: v135fV6b4 = ISZERO v135eV6b4
    0x1360S0x6b4: v1360V6b4(0x1376) = CONST 
    0x1363S0x6b4: JUMPI v1360V6b4(0x1376), v135fV6b4

    Begin block 0x1364B0x6b4
    prev=[0x135bB0x6b4], succ=[0x135bB0x6b4]
    =================================
    0x1364_0x1S0x6b4: v1364_1V6b4 = PHI v1325V6b4, v1370V6b4
    0x1364_0x2S0x6b4: v1364_2V6b4 = PHI v6d3, v136bV6b4
    0x1365S0x6b4: v1365V6b4 = MLOAD v1364_2V6b4
    0x1367S0x6b4: SSTORE v1364_1V6b4, v1365V6b4
    0x1369S0x6b4: v1369V6b4(0x20) = CONST 
    0x136bS0x6b4: v136bV6b4 = ADD v1369V6b4(0x20), v1364_2V6b4
    0x136eS0x6b4: v136eV6b4(0x1) = CONST 
    0x1370S0x6b4: v1370V6b4 = ADD v136eV6b4(0x1), v1364_1V6b4
    0x1372S0x6b4: v1372V6b4(0x135b) = CONST 
    0x1375S0x6b4: JUMP v1372V6b4(0x135b)

    Begin block 0x1339B0x6b4
    prev=[0x1308B0x6b4], succ=[0x1376B0x6b4]
    =================================
    0x133aS0x6b4: v133aV6b4 = MLOAD v6d3
    0x133bS0x6b4: v133bV6b4(0xff) = CONST 
    0x133dS0x6b4: v133dV6b4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v133bV6b4(0xff)
    0x133eS0x6b4: v133eV6b4 = AND v133dV6b4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v133aV6b4
    0x1341S0x6b4: v1341V6b4 = ADD v6c8, v6c8
    0x1342S0x6b4: v1342V6b4 = OR v1341V6b4, v133eV6b4
    0x1344S0x6b4: SSTORE v6cd(0x7), v1342V6b4
    0x1345S0x6b4: v1345V6b4(0x1376) = CONST 
    0x1348S0x6b4: JUMP v1345V6b4(0x1376)

}

function removeAdmin(address)() public {
    Begin block 0x338
    prev=[], succ=[0x34a, 0x34e]
    =================================
    0x339: v339(0x1650) = CONST 
    0x33c: v33c(0x4) = CONST 
    0x33f: v33f = CALLDATASIZE 
    0x340: v340 = SUB v33f, v33c(0x4)
    0x341: v341(0x20) = CONST 
    0x344: v344 = LT v340, v341(0x20)
    0x345: v345 = ISZERO v344
    0x346: v346(0x34e) = CONST 
    0x349: JUMPI v346(0x34e), v345

    Begin block 0x34a
    prev=[0x338], succ=[]
    =================================
    0x34a: v34a(0x0) = CONST 
    0x34d: REVERT v34a(0x0), v34a(0x0)

    Begin block 0x34e
    prev=[0x338], succ=[0x73a]
    =================================
    0x350: v350 = CALLDATALOAD v33c(0x4)
    0x351: v351(0x1) = CONST 
    0x353: v353(0x1) = CONST 
    0x355: v355(0xa0) = CONST 
    0x357: v357(0x10000000000000000000000000000000000000000) = SHL v355(0xa0), v353(0x1)
    0x358: v358(0xffffffffffffffffffffffffffffffffffffffff) = SUB v357(0x10000000000000000000000000000000000000000), v351(0x1)
    0x359: v359 = AND v358(0xffffffffffffffffffffffffffffffffffffffff), v350
    0x35a: v35a(0x73a) = CONST 
    0x35d: JUMP v35a(0x73a)

    Begin block 0x73a
    prev=[0x34e], succ=[0x74d, 0x799]
    =================================
    0x73b: v73b(0x0) = CONST 
    0x73d: v73d = SLOAD v73b(0x0)
    0x73e: v73e(0x1) = CONST 
    0x740: v740(0x1) = CONST 
    0x742: v742(0xa0) = CONST 
    0x744: v744(0x10000000000000000000000000000000000000000) = SHL v742(0xa0), v740(0x1)
    0x745: v745(0xffffffffffffffffffffffffffffffffffffffff) = SUB v744(0x10000000000000000000000000000000000000000), v73e(0x1)
    0x746: v746 = AND v745(0xffffffffffffffffffffffffffffffffffffffff), v73d
    0x747: v747 = CALLER 
    0x748: v748 = EQ v747, v746
    0x749: v749(0x799) = CONST 
    0x74c: JUMPI v749(0x799), v748

    Begin block 0x74d
    prev=[0x73a], succ=[]
    =================================
    0x74d: v74d(0x40) = CONST 
    0x750: v750 = MLOAD v74d(0x40)
    0x751: v751(0x461bcd) = CONST 
    0x755: v755(0xe5) = CONST 
    0x757: v757(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v755(0xe5), v751(0x461bcd)
    0x759: MSTORE v750, v757(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x75a: v75a(0x20) = CONST 
    0x75c: v75c(0x4) = CONST 
    0x75f: v75f = ADD v750, v75c(0x4)
    0x762: MSTORE v75f, v75a(0x20)
    0x763: v763(0x24) = CONST 
    0x766: v766 = ADD v750, v763(0x24)
    0x767: MSTORE v766, v75a(0x20)
    0x768: v768(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x789: v789(0x44) = CONST 
    0x78c: v78c = ADD v750, v789(0x44)
    0x78d: MSTORE v78c, v768(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x78f: v78f = MLOAD v74d(0x40)
    0x793: v793(0x0) = SUB v750, v78f
    0x794: v794(0x64) = CONST 
    0x796: v796(0x64) = ADD v794(0x64), v793(0x0)
    0x798: REVERT v78f, v796(0x64)

    Begin block 0x799
    prev=[0x73a], succ=[0x1650]
    =================================
    0x79a: v79a(0x1) = CONST 
    0x79c: v79c(0x1) = CONST 
    0x79e: v79e(0xa0) = CONST 
    0x7a0: v7a0(0x10000000000000000000000000000000000000000) = SHL v79e(0xa0), v79c(0x1)
    0x7a1: v7a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7a0(0x10000000000000000000000000000000000000000), v79a(0x1)
    0x7a2: v7a2 = AND v7a1(0xffffffffffffffffffffffffffffffffffffffff), v359
    0x7a3: v7a3(0x0) = CONST 
    0x7a7: MSTORE v7a3(0x0), v7a2
    0x7a8: v7a8(0x2) = CONST 
    0x7aa: v7aa(0x20) = CONST 
    0x7ac: MSTORE v7aa(0x20), v7a8(0x2)
    0x7ad: v7ad(0x40) = CONST 
    0x7b0: v7b0 = SHA3 v7a3(0x0), v7ad(0x40)
    0x7b2: v7b2 = SLOAD v7b0
    0x7b3: v7b3(0xff) = CONST 
    0x7b5: v7b5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v7b3(0xff)
    0x7b6: v7b6 = AND v7b5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v7b2
    0x7b8: SSTORE v7b0, v7b6
    0x7b9: JUMP v339(0x1650)

    Begin block 0x1650
    prev=[0x799], succ=[]
    =================================
    0x1651: STOP 

}

function totalSupply()() public {
    Begin block 0x35e
    prev=[], succ=[0x7ba]
    =================================
    0x35f: v35f(0x1671) = CONST 
    0x362: v362(0x7ba) = CONST 
    0x365: JUMP v362(0x7ba)

    Begin block 0x7ba
    prev=[0x35e], succ=[0x1671]
    =================================
    0x7bb: v7bb(0x6) = CONST 
    0x7bd: v7bd = SLOAD v7bb(0x6)
    0x7bf: JUMP v35f(0x1671)

    Begin block 0x1671
    prev=[0x7ba], succ=[]
    =================================
    0x1672: v1672(0x40) = CONST 
    0x1675: v1675 = MLOAD v1672(0x40)
    0x1678: MSTORE v1675, v7bd
    0x1679: v1679 = MLOAD v1672(0x40)
    0x167d: v167d(0x0) = SUB v1675, v1679
    0x167e: v167e(0x20) = CONST 
    0x1680: v1680(0x20) = ADD v167e(0x20), v167d(0x0)
    0x1682: RETURN v1679, v1680(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x378
    prev=[], succ=[0x38a, 0x38e]
    =================================
    0x379: v379(0x16a2) = CONST 
    0x37c: v37c(0x4) = CONST 
    0x37f: v37f = CALLDATASIZE 
    0x380: v380 = SUB v37f, v37c(0x4)
    0x381: v381(0x60) = CONST 
    0x384: v384 = LT v380, v381(0x60)
    0x385: v385 = ISZERO v384
    0x386: v386(0x38e) = CONST 
    0x389: JUMPI v386(0x38e), v385

    Begin block 0x38a
    prev=[0x378], succ=[]
    =================================
    0x38a: v38a(0x0) = CONST 
    0x38d: REVERT v38a(0x0), v38a(0x0)

    Begin block 0x38e
    prev=[0x378], succ=[0x7c0]
    =================================
    0x390: v390(0x1) = CONST 
    0x392: v392(0x1) = CONST 
    0x394: v394(0xa0) = CONST 
    0x396: v396(0x10000000000000000000000000000000000000000) = SHL v394(0xa0), v392(0x1)
    0x397: v397(0xffffffffffffffffffffffffffffffffffffffff) = SUB v396(0x10000000000000000000000000000000000000000), v390(0x1)
    0x399: v399 = CALLDATALOAD v37c(0x4)
    0x39b: v39b = AND v397(0xffffffffffffffffffffffffffffffffffffffff), v399
    0x39d: v39d(0x20) = CONST 
    0x3a0: v3a0(0x24) = ADD v37c(0x4), v39d(0x20)
    0x3a1: v3a1 = CALLDATALOAD v3a0(0x24)
    0x3a4: v3a4 = AND v397(0xffffffffffffffffffffffffffffffffffffffff), v3a1
    0x3a6: v3a6(0x40) = CONST 
    0x3a8: v3a8(0x44) = ADD v3a6(0x40), v37c(0x4)
    0x3a9: v3a9 = CALLDATALOAD v3a8(0x44)
    0x3aa: v3aa(0x7c0) = CONST 
    0x3ad: JUMP v3aa(0x7c0)

    Begin block 0x7c0
    prev=[0x38e], succ=[0x7cd]
    =================================
    0x7c1: v7c1(0x0) = CONST 
    0x7c3: v7c3(0x7cd) = CONST 
    0x7c9: v7c9(0xe08) = CONST 
    0x7cc: v7cc_0, v7cc_1, v7cc_2 = CALLPRIVATE v7c9(0xe08), v3a9, v3a4, v39b

    Begin block 0x7cd
    prev=[0x7c0], succ=[0xd18B0x7cd]
    =================================
    0x7ce: v7ce(0x843) = CONST 
    0x7d2: v7d2(0x7d9) = CONST 
    0x7d5: v7d5(0xd18) = CONST 
    0x7d8: JUMP v7d5(0xd18)

    Begin block 0xd18B0x7cd
    prev=[0x7cd], succ=[0x7d9]
    =================================
    0xd19S0x7cd: vd19V7cd = CALLER 
    0xd1bS0x7cd: JUMP v7d2(0x7d9)

    Begin block 0x7d9
    prev=[0xd18B0x7cd], succ=[0xd18B0x7d9]
    =================================
    0x7da: v7da(0x1979) = CONST 
    0x7de: v7de(0x40) = CONST 
    0x7e0: v7e0 = MLOAD v7de(0x40)
    0x7e2: v7e2(0x60) = CONST 
    0x7e4: v7e4 = ADD v7e2(0x60), v7e0
    0x7e5: v7e5(0x40) = CONST 
    0x7e7: MSTORE v7e5(0x40), v7e4
    0x7e9: v7e9(0x28) = CONST 
    0x7ec: MSTORE v7e0, v7e9(0x28)
    0x7ed: v7ed(0x20) = CONST 
    0x7ef: v7ef = ADD v7ed(0x20), v7e0
    0x7f0: v7f0(0x1454) = CONST 
    0x7f3: v7f3(0x28) = CONST 
    0x7f6: CODECOPY v7ef, v7f0(0x1454), v7f3(0x28)
    0x7f7: v7f7(0x1) = CONST 
    0x7f9: v7f9(0x1) = CONST 
    0x7fb: v7fb(0xa0) = CONST 
    0x7fd: v7fd(0x10000000000000000000000000000000000000000) = SHL v7fb(0xa0), v7f9(0x1)
    0x7fe: v7fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fd(0x10000000000000000000000000000000000000000), v7f7(0x1)
    0x800: v800(0x7cd) = AND v7c3(0x7cd), v7fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x801: v801(0x0) = CONST 
    0x805: MSTORE v801(0x0), v800(0x7cd)
    0x806: v806(0x5) = CONST 
    0x808: v808(0x20) = CONST 
    0x80a: MSTORE v808(0x20), v806(0x5)
    0x80b: v80b(0x40) = CONST 
    0x80e: v80e = SHA3 v801(0x0), v80b(0x40)
    0x810: v810(0x817) = CONST 
    0x813: v813(0xd18) = CONST 
    0x816: JUMP v813(0xd18)

    Begin block 0xd18B0x7d9
    prev=[0x7d9], succ=[0x817]
    =================================
    0xd19S0x7d9: vd19V7d9 = CALLER 
    0xd1bS0x7d9: JUMP v810(0x817)

    Begin block 0x817
    prev=[0xd18B0x7d9], succ=[0x1979]
    =================================
    0x818: v818(0x1) = CONST 
    0x81a: v81a(0x1) = CONST 
    0x81c: v81c(0xa0) = CONST 
    0x81e: v81e(0x10000000000000000000000000000000000000000) = SHL v81c(0xa0), v81a(0x1)
    0x81f: v81f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v81e(0x10000000000000000000000000000000000000000), v818(0x1)
    0x820: v820 = AND v81f(0xffffffffffffffffffffffffffffffffffffffff), vd19V7d9
    0x822: MSTORE v801(0x0), v820
    0x823: v823(0x20) = CONST 
    0x826: v826(0x20) = ADD v801(0x0), v823(0x20)
    0x82a: MSTORE v826(0x20), v80e
    0x82b: v82b(0x40) = CONST 
    0x82d: v82d(0x40) = ADD v82b(0x40), v801(0x0)
    0x82e: v82e(0x0) = CONST 
    0x830: v830 = SHA3 v82e(0x0), v82d(0x40)
    0x831: v831 = SLOAD v830
    0x834: v834(0xffffffff) = CONST 
    0x839: v839(0xf71) = CONST 
    0x83c: v83c(0xf71) = AND v839(0xf71), v834(0xffffffff)
    0x83d: v83d_0 = CALLPRIVATE v83c(0xf71), v7e0, v7cc_1, v831, v7da(0x1979)

    Begin block 0x1979
    prev=[0x817], succ=[0x843]
    =================================
    0x197a: v197a(0xd1c) = CONST 
    0x197d: CALLPRIVATE v197a(0xd1c), v83d_0, vd19V7cd, v7c3(0x7cd), v7ce(0x843)

    Begin block 0x843
    prev=[0x1979], succ=[0x16a2]
    =================================
    0x845: v845(0x1) = CONST 
    0x84c: JUMP v7c1(0x0)

    Begin block 0x16a2
    prev=[0x843], succ=[]
    =================================
    0x16a3: v16a3(0x40) = CONST 
    0x16a6: v16a6 = MLOAD v16a3(0x40)
    0x16a8: v16a8 = ISZERO v845(0x1)
    0x16a9: v16a9 = ISZERO v16a8
    0x16ab: MSTORE v16a6, v16a9
    0x16ac: v16ac = MLOAD v16a3(0x40)
    0x16b0: v16b0(0x0) = SUB v16a6, v16ac
    0x16b1: v16b1(0x20) = CONST 
    0x16b3: v16b3(0x20) = ADD v16b1(0x20), v16b0(0x0)
    0x16b5: RETURN v16ac, v16b3(0x20)

}

function isAdmin(address)() public {
    Begin block 0x3ae
    prev=[], succ=[0x3c0, 0x3c4]
    =================================
    0x3af: v3af(0x16d5) = CONST 
    0x3b2: v3b2(0x4) = CONST 
    0x3b5: v3b5 = CALLDATASIZE 
    0x3b6: v3b6 = SUB v3b5, v3b2(0x4)
    0x3b7: v3b7(0x20) = CONST 
    0x3ba: v3ba = LT v3b6, v3b7(0x20)
    0x3bb: v3bb = ISZERO v3ba
    0x3bc: v3bc(0x3c4) = CONST 
    0x3bf: JUMPI v3bc(0x3c4), v3bb

    Begin block 0x3c0
    prev=[0x3ae], succ=[]
    =================================
    0x3c0: v3c0(0x0) = CONST 
    0x3c3: REVERT v3c0(0x0), v3c0(0x0)

    Begin block 0x3c4
    prev=[0x3ae], succ=[0x84d]
    =================================
    0x3c6: v3c6 = CALLDATALOAD v3b2(0x4)
    0x3c7: v3c7(0x1) = CONST 
    0x3c9: v3c9(0x1) = CONST 
    0x3cb: v3cb(0xa0) = CONST 
    0x3cd: v3cd(0x10000000000000000000000000000000000000000) = SHL v3cb(0xa0), v3c9(0x1)
    0x3ce: v3ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3cd(0x10000000000000000000000000000000000000000), v3c7(0x1)
    0x3cf: v3cf = AND v3ce(0xffffffffffffffffffffffffffffffffffffffff), v3c6
    0x3d0: v3d0(0x84d) = CONST 
    0x3d3: JUMP v3d0(0x84d)

    Begin block 0x84d
    prev=[0x3c4], succ=[0x16d5]
    =================================
    0x84e: v84e(0x2) = CONST 
    0x850: v850(0x20) = CONST 
    0x852: MSTORE v850(0x20), v84e(0x2)
    0x853: v853(0x0) = CONST 
    0x857: MSTORE v853(0x0), v3cf
    0x858: v858(0x40) = CONST 
    0x85b: v85b = SHA3 v853(0x0), v858(0x40)
    0x85c: v85c = SLOAD v85b
    0x85d: v85d(0xff) = CONST 
    0x85f: v85f = AND v85d(0xff), v85c
    0x861: JUMP v3af(0x16d5)

    Begin block 0x16d5
    prev=[0x84d], succ=[]
    =================================
    0x16d6: v16d6(0x40) = CONST 
    0x16d9: v16d9 = MLOAD v16d6(0x40)
    0x16db: v16db = ISZERO v85f
    0x16dc: v16dc = ISZERO v16db
    0x16de: MSTORE v16d9, v16dc
    0x16df: v16df = MLOAD v16d6(0x40)
    0x16e3: v16e3(0x0) = SUB v16d9, v16df
    0x16e4: v16e4(0x20) = CONST 
    0x16e6: v16e6(0x20) = ADD v16e4(0x20), v16e3(0x0)
    0x16e8: RETURN v16df, v16e6(0x20)

}

function decimals()() public {
    Begin block 0x3d4
    prev=[], succ=[0x862]
    =================================
    0x3d5: v3d5(0x3dc) = CONST 
    0x3d8: v3d8(0x862) = CONST 
    0x3db: JUMP v3d8(0x862)

    Begin block 0x862
    prev=[0x3d4], succ=[0x3dc]
    =================================
    0x863: v863(0x9) = CONST 
    0x865: v865 = SLOAD v863(0x9)
    0x866: v866(0xff) = CONST 
    0x868: v868 = AND v866(0xff), v865
    0x86a: JUMP v3d5(0x3dc)

    Begin block 0x3dc
    prev=[0x862], succ=[]
    =================================
    0x3dd: v3dd(0x40) = CONST 
    0x3e0: v3e0 = MLOAD v3dd(0x40)
    0x3e1: v3e1(0xff) = CONST 
    0x3e5: v3e5 = AND v868, v3e1(0xff)
    0x3e7: MSTORE v3e0, v3e5
    0x3e8: v3e8 = MLOAD v3dd(0x40)
    0x3ec: v3ec(0x0) = SUB v3e0, v3e8
    0x3ed: v3ed(0x20) = CONST 
    0x3ef: v3ef(0x20) = ADD v3ed(0x20), v3ec(0x0)
    0x3f1: RETURN v3e8, v3ef(0x20)

}

function increaseAllowance(address,uint256)() public {
    Begin block 0x3f2
    prev=[], succ=[0x404, 0x408]
    =================================
    0x3f3: v3f3(0x1708) = CONST 
    0x3f6: v3f6(0x4) = CONST 
    0x3f9: v3f9 = CALLDATASIZE 
    0x3fa: v3fa = SUB v3f9, v3f6(0x4)
    0x3fb: v3fb(0x40) = CONST 
    0x3fe: v3fe = LT v3fa, v3fb(0x40)
    0x3ff: v3ff = ISZERO v3fe
    0x400: v400(0x408) = CONST 
    0x403: JUMPI v400(0x408), v3ff

    Begin block 0x404
    prev=[0x3f2], succ=[]
    =================================
    0x404: v404(0x0) = CONST 
    0x407: REVERT v404(0x0), v404(0x0)

    Begin block 0x408
    prev=[0x3f2], succ=[0x86b]
    =================================
    0x40a: v40a(0x1) = CONST 
    0x40c: v40c(0x1) = CONST 
    0x40e: v40e(0xa0) = CONST 
    0x410: v410(0x10000000000000000000000000000000000000000) = SHL v40e(0xa0), v40c(0x1)
    0x411: v411(0xffffffffffffffffffffffffffffffffffffffff) = SUB v410(0x10000000000000000000000000000000000000000), v40a(0x1)
    0x413: v413 = CALLDATALOAD v3f6(0x4)
    0x414: v414 = AND v413, v411(0xffffffffffffffffffffffffffffffffffffffff)
    0x416: v416(0x20) = CONST 
    0x418: v418(0x24) = ADD v416(0x20), v3f6(0x4)
    0x419: v419 = CALLDATALOAD v418(0x24)
    0x41a: v41a(0x86b) = CONST 
    0x41d: JUMP v41a(0x86b)

    Begin block 0x86b
    prev=[0x408], succ=[0xd18B0x86b]
    =================================
    0x86c: v86c(0x0) = CONST 
    0x86e: v86e(0x199d) = CONST 
    0x871: v871(0x878) = CONST 
    0x874: v874(0xd18) = CONST 
    0x877: JUMP v874(0xd18)

    Begin block 0xd18B0x86b
    prev=[0x86b], succ=[0x878]
    =================================
    0xd19S0x86b: vd19V86b = CALLER 
    0xd1bS0x86b: JUMP v871(0x878)

    Begin block 0x878
    prev=[0xd18B0x86b], succ=[0xd18B0x878]
    =================================
    0x87a: v87a(0x19c5) = CONST 
    0x87e: v87e(0x5) = CONST 
    0x880: v880(0x0) = CONST 
    0x882: v882(0x889) = CONST 
    0x885: v885(0xd18) = CONST 
    0x888: JUMP v885(0xd18)

    Begin block 0xd18B0x878
    prev=[0x878], succ=[0x889]
    =================================
    0xd19S0x878: vd19V878 = CALLER 
    0xd1bS0x878: JUMP v882(0x889)

    Begin block 0x889
    prev=[0xd18B0x878], succ=[0x1008B0x889]
    =================================
    0x88a: v88a(0x1) = CONST 
    0x88c: v88c(0x1) = CONST 
    0x88e: v88e(0xa0) = CONST 
    0x890: v890(0x10000000000000000000000000000000000000000) = SHL v88e(0xa0), v88c(0x1)
    0x891: v891(0xffffffffffffffffffffffffffffffffffffffff) = SUB v890(0x10000000000000000000000000000000000000000), v88a(0x1)
    0x894: v894 = AND v891(0xffffffffffffffffffffffffffffffffffffffff), vd19V878
    0x896: MSTORE v880(0x0), v894
    0x897: v897(0x20) = CONST 
    0x89b: v89b(0x20) = ADD v880(0x0), v897(0x20)
    0x89f: MSTORE v89b(0x20), v87e(0x5)
    0x8a0: v8a0(0x40) = CONST 
    0x8a4: v8a4(0x40) = ADD v8a0(0x40), v880(0x0)
    0x8a5: v8a5(0x0) = CONST 
    0x8a9: v8a9 = SHA3 v8a5(0x0), v8a4(0x40)
    0x8ac: v8ac = AND v414, v891(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ae: MSTORE v8a5(0x0), v8ac
    0x8b0: MSTORE v897(0x20), v8a9
    0x8b2: v8b2 = SHA3 v8a5(0x0), v8a0(0x40)
    0x8b3: v8b3 = SLOAD v8b2
    0x8b5: v8b5(0xffffffff) = CONST 
    0x8ba: v8ba(0x1008) = CONST 
    0x8bd: v8bd(0x1008) = AND v8ba(0x1008), v8b5(0xffffffff)
    0x8be: JUMP v8bd(0x1008)

    Begin block 0x1008B0x889
    prev=[0x889], succ=[0x1016B0x889, 0x1a5dB0x889]
    =================================
    0x1009S0x889: v1009V889(0x0) = CONST 
    0x100dS0x889: v100dV889 = ADD v419, v8b3
    0x1010S0x889: v1010V889 = LT v100dV889, v8b3
    0x1011S0x889: v1011V889 = ISZERO v1010V889
    0x1012S0x889: v1012V889(0x1a5d) = CONST 
    0x1015S0x889: JUMPI v1012V889(0x1a5d), v1011V889

    Begin block 0x1016B0x889
    prev=[0x1008B0x889], succ=[]
    =================================
    0x1016S0x889: v1016V889(0x40) = CONST 
    0x1019S0x889: v1019V889 = MLOAD v1016V889(0x40)
    0x101aS0x889: v101aV889(0x461bcd) = CONST 
    0x101eS0x889: v101eV889(0xe5) = CONST 
    0x1020S0x889: v1020V889(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v101eV889(0xe5), v101aV889(0x461bcd)
    0x1022S0x889: MSTORE v1019V889, v1020V889(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1023S0x889: v1023V889(0x20) = CONST 
    0x1025S0x889: v1025V889(0x4) = CONST 
    0x1028S0x889: v1028V889 = ADD v1019V889, v1025V889(0x4)
    0x1029S0x889: MSTORE v1028V889, v1023V889(0x20)
    0x102aS0x889: v102aV889(0x1b) = CONST 
    0x102cS0x889: v102cV889(0x24) = CONST 
    0x102fS0x889: v102fV889 = ADD v1019V889, v102cV889(0x24)
    0x1030S0x889: MSTORE v102fV889, v102aV889(0x1b)
    0x1031S0x889: v1031V889(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x1052S0x889: v1052V889(0x44) = CONST 
    0x1055S0x889: v1055V889 = ADD v1019V889, v1052V889(0x44)
    0x1056S0x889: MSTORE v1055V889, v1031V889(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x1058S0x889: v1058V889 = MLOAD v1016V889(0x40)
    0x105cS0x889: v105cV889(0x0) = SUB v1019V889, v1058V889
    0x105dS0x889: v105dV889(0x64) = CONST 
    0x105fS0x889: v105fV889(0x64) = ADD v105dV889(0x64), v105cV889(0x0)
    0x1061S0x889: REVERT v1058V889, v105fV889(0x64)

    Begin block 0x1a5dB0x889
    prev=[0x1008B0x889], succ=[0x19c5]
    =================================
    0x1a63S0x889: JUMP v87a(0x19c5)

    Begin block 0x19c5
    prev=[0x1a5dB0x889], succ=[0x199d]
    =================================
    0x19c6: v19c6(0xd1c) = CONST 
    0x19c9: CALLPRIVATE v19c6(0xd1c), v100dV889, v414, vd19V86b, v86e(0x199d)

    Begin block 0x199d
    prev=[0x19c5], succ=[0x1708]
    =================================
    0x199f: v199f(0x1) = CONST 
    0x19a5: JUMP v3f3(0x1708)

    Begin block 0x1708
    prev=[0x199d], succ=[]
    =================================
    0x1709: v1709(0x40) = CONST 
    0x170c: v170c = MLOAD v1709(0x40)
    0x170e: v170e = ISZERO v199f(0x1)
    0x170f: v170f = ISZERO v170e
    0x1711: MSTORE v170c, v170f
    0x1712: v1712 = MLOAD v1709(0x40)
    0x1716: v1716(0x0) = SUB v170c, v1712
    0x1717: v1717(0x20) = CONST 
    0x1719: v1719(0x20) = ADD v1717(0x20), v1716(0x0)
    0x171b: RETURN v1712, v1719(0x20)

}

function mint(address,uint256)() public {
    Begin block 0x41e
    prev=[], succ=[0x430, 0x434]
    =================================
    0x41f: v41f(0x173b) = CONST 
    0x422: v422(0x4) = CONST 
    0x425: v425 = CALLDATASIZE 
    0x426: v426 = SUB v425, v422(0x4)
    0x427: v427(0x40) = CONST 
    0x42a: v42a = LT v426, v427(0x40)
    0x42b: v42b = ISZERO v42a
    0x42c: v42c(0x434) = CONST 
    0x42f: JUMPI v42c(0x434), v42b

    Begin block 0x430
    prev=[0x41e], succ=[]
    =================================
    0x430: v430(0x0) = CONST 
    0x433: REVERT v430(0x0), v430(0x0)

    Begin block 0x434
    prev=[0x41e], succ=[0x8bf]
    =================================
    0x436: v436(0x1) = CONST 
    0x438: v438(0x1) = CONST 
    0x43a: v43a(0xa0) = CONST 
    0x43c: v43c(0x10000000000000000000000000000000000000000) = SHL v43a(0xa0), v438(0x1)
    0x43d: v43d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43c(0x10000000000000000000000000000000000000000), v436(0x1)
    0x43f: v43f = CALLDATALOAD v422(0x4)
    0x440: v440 = AND v43f, v43d(0xffffffffffffffffffffffffffffffffffffffff)
    0x442: v442(0x20) = CONST 
    0x444: v444(0x24) = ADD v442(0x20), v422(0x4)
    0x445: v445 = CALLDATALOAD v444(0x24)
    0x446: v446(0x8bf) = CONST 
    0x449: JUMP v446(0x8bf)

    Begin block 0x8bf
    prev=[0x434], succ=[0x8e7, 0x8d3]
    =================================
    0x8c0: v8c0(0x0) = CONST 
    0x8c2: v8c2 = SLOAD v8c0(0x0)
    0x8c3: v8c3(0x1) = CONST 
    0x8c5: v8c5(0x1) = CONST 
    0x8c7: v8c7(0xa0) = CONST 
    0x8c9: v8c9(0x10000000000000000000000000000000000000000) = SHL v8c7(0xa0), v8c5(0x1)
    0x8ca: v8ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8c9(0x10000000000000000000000000000000000000000), v8c3(0x1)
    0x8cb: v8cb = AND v8ca(0xffffffffffffffffffffffffffffffffffffffff), v8c2
    0x8cc: v8cc = CALLER 
    0x8cd: v8cd = EQ v8cc, v8cb
    0x8cf: v8cf(0x8e7) = CONST 
    0x8d2: JUMPI v8cf(0x8e7), v8cd

    Begin block 0x8e7
    prev=[0x8bf, 0x8d3], succ=[0x8ec, 0x8f0]
    =================================
    0x8e7_0x0: v8e7_0 = PHI v8cd, v8e6
    0x8e8: v8e8(0x8f0) = CONST 
    0x8eb: JUMPI v8e8(0x8f0), v8e7_0

    Begin block 0x8ec
    prev=[0x8e7], succ=[]
    =================================
    0x8ec: v8ec(0x0) = CONST 
    0x8ef: REVERT v8ec(0x0), v8ec(0x0)

    Begin block 0x8f0
    prev=[0x8e7], succ=[0x8fc, 0x93b]
    =================================
    0x8f1: v8f1(0x3) = CONST 
    0x8f3: v8f3 = SLOAD v8f1(0x3)
    0x8f4: v8f4(0xff) = CONST 
    0x8f6: v8f6 = AND v8f4(0xff), v8f3
    0x8f7: v8f7 = ISZERO v8f6
    0x8f8: v8f8(0x93b) = CONST 
    0x8fb: JUMPI v8f8(0x93b), v8f7

    Begin block 0x8fc
    prev=[0x8f0], succ=[]
    =================================
    0x8fc: v8fc(0x40) = CONST 
    0x8ff: v8ff = MLOAD v8fc(0x40)
    0x900: v900(0x461bcd) = CONST 
    0x904: v904(0xe5) = CONST 
    0x906: v906(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v904(0xe5), v900(0x461bcd)
    0x908: MSTORE v8ff, v906(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x909: v909(0x20) = CONST 
    0x90b: v90b(0x4) = CONST 
    0x90e: v90e = ADD v8ff, v90b(0x4)
    0x90f: MSTORE v90e, v909(0x20)
    0x910: v910(0x10) = CONST 
    0x912: v912(0x24) = CONST 
    0x915: v915 = ADD v8ff, v912(0x24)
    0x916: MSTORE v915, v910(0x10)
    0x917: v917(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0x928: v928(0x82) = CONST 
    0x92a: v92a(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL v928(0x82), v917(0x14185d5cd8589b194e881c185d5cd959)
    0x92b: v92b(0x44) = CONST 
    0x92e: v92e = ADD v8ff, v92b(0x44)
    0x92f: MSTORE v92e, v92a(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x931: v931 = MLOAD v8fc(0x40)
    0x935: v935(0x0) = SUB v8ff, v931
    0x936: v936(0x64) = CONST 
    0x938: v938(0x64) = ADD v936(0x64), v935(0x0)
    0x93a: REVERT v931, v938(0x64)

    Begin block 0x93b
    prev=[0x8f0], succ=[0x1069]
    =================================
    0x93c: v93c(0x945) = CONST 
    0x941: v941(0x1069) = CONST 
    0x944: JUMP v941(0x1069)

    Begin block 0x1069
    prev=[0x93b], succ=[0x1078, 0x10c4]
    =================================
    0x106a: v106a(0x1) = CONST 
    0x106c: v106c(0x1) = CONST 
    0x106e: v106e(0xa0) = CONST 
    0x1070: v1070(0x10000000000000000000000000000000000000000) = SHL v106e(0xa0), v106c(0x1)
    0x1071: v1071(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1070(0x10000000000000000000000000000000000000000), v106a(0x1)
    0x1073: v1073 = AND v440, v1071(0xffffffffffffffffffffffffffffffffffffffff)
    0x1074: v1074(0x10c4) = CONST 
    0x1077: JUMPI v1074(0x10c4), v1073

    Begin block 0x1078
    prev=[0x1069], succ=[]
    =================================
    0x1078: v1078(0x40) = CONST 
    0x107b: v107b = MLOAD v1078(0x40)
    0x107c: v107c(0x461bcd) = CONST 
    0x1080: v1080(0xe5) = CONST 
    0x1082: v1082(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1080(0xe5), v107c(0x461bcd)
    0x1084: MSTORE v107b, v1082(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1085: v1085(0x20) = CONST 
    0x1087: v1087(0x4) = CONST 
    0x108a: v108a = ADD v107b, v1087(0x4)
    0x108b: MSTORE v108a, v1085(0x20)
    0x108c: v108c(0x1f) = CONST 
    0x108e: v108e(0x24) = CONST 
    0x1091: v1091 = ADD v107b, v108e(0x24)
    0x1092: MSTORE v1091, v108c(0x1f)
    0x1093: v1093(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300) = CONST 
    0x10b4: v10b4(0x44) = CONST 
    0x10b7: v10b7 = ADD v107b, v10b4(0x44)
    0x10b8: MSTORE v10b7, v1093(0x45524332303a206d696e7420746f20746865207a65726f206164647265737300)
    0x10ba: v10ba = MLOAD v1078(0x40)
    0x10be: v10be(0x0) = SUB v107b, v10ba
    0x10bf: v10bf(0x64) = CONST 
    0x10c1: v10c1(0x64) = ADD v10bf(0x64), v10be(0x0)
    0x10c3: REVERT v10ba, v10c1(0x64)

    Begin block 0x10c4
    prev=[0x1069], succ=[0x10d0]
    =================================
    0x10c5: v10c5(0x10d0) = CONST 
    0x10c8: v10c8(0x0) = CONST 
    0x10cc: v10cc(0x126f) = CONST 
    0x10cf: v10cf_0, v10cf_1, v10cf_2 = CALLPRIVATE v10cc(0x126f), v445, v440, v10c8(0x0)

    Begin block 0x10d0
    prev=[0x10c4], succ=[0x1008B0x10d0]
    =================================
    0x10d1: v10d1(0x6) = CONST 
    0x10d3: v10d3 = SLOAD v10d1(0x6)
    0x10d4: v10d4(0x10e3) = CONST 
    0x10d9: v10d9(0xffffffff) = CONST 
    0x10de: v10de(0x1008) = CONST 
    0x10e1: v10e1(0x1008) = AND v10de(0x1008), v10d9(0xffffffff)
    0x10e2: JUMP v10e1(0x1008)

    Begin block 0x1008B0x10d0
    prev=[0x10d0], succ=[0x1016B0x10d0, 0x1a5dB0x10d0]
    =================================
    0x1009S0x10d0: v1009V10d0(0x0) = CONST 
    0x100dS0x10d0: v100dV10d0 = ADD v10cf_0, v10d3
    0x1010S0x10d0: v1010V10d0 = LT v100dV10d0, v10d3
    0x1011S0x10d0: v1011V10d0 = ISZERO v1010V10d0
    0x1012S0x10d0: v1012V10d0(0x1a5d) = CONST 
    0x1015S0x10d0: JUMPI v1012V10d0(0x1a5d), v1011V10d0

    Begin block 0x1016B0x10d0
    prev=[0x1008B0x10d0], succ=[]
    =================================
    0x1016S0x10d0: v1016V10d0(0x40) = CONST 
    0x1019S0x10d0: v1019V10d0 = MLOAD v1016V10d0(0x40)
    0x101aS0x10d0: v101aV10d0(0x461bcd) = CONST 
    0x101eS0x10d0: v101eV10d0(0xe5) = CONST 
    0x1020S0x10d0: v1020V10d0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v101eV10d0(0xe5), v101aV10d0(0x461bcd)
    0x1022S0x10d0: MSTORE v1019V10d0, v1020V10d0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1023S0x10d0: v1023V10d0(0x20) = CONST 
    0x1025S0x10d0: v1025V10d0(0x4) = CONST 
    0x1028S0x10d0: v1028V10d0 = ADD v1019V10d0, v1025V10d0(0x4)
    0x1029S0x10d0: MSTORE v1028V10d0, v1023V10d0(0x20)
    0x102aS0x10d0: v102aV10d0(0x1b) = CONST 
    0x102cS0x10d0: v102cV10d0(0x24) = CONST 
    0x102fS0x10d0: v102fV10d0 = ADD v1019V10d0, v102cV10d0(0x24)
    0x1030S0x10d0: MSTORE v102fV10d0, v102aV10d0(0x1b)
    0x1031S0x10d0: v1031V10d0(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x1052S0x10d0: v1052V10d0(0x44) = CONST 
    0x1055S0x10d0: v1055V10d0 = ADD v1019V10d0, v1052V10d0(0x44)
    0x1056S0x10d0: MSTORE v1055V10d0, v1031V10d0(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x1058S0x10d0: v1058V10d0 = MLOAD v1016V10d0(0x40)
    0x105cS0x10d0: v105cV10d0(0x0) = SUB v1019V10d0, v1058V10d0
    0x105dS0x10d0: v105dV10d0(0x64) = CONST 
    0x105fS0x10d0: v105fV10d0(0x64) = ADD v105dV10d0(0x64), v105cV10d0(0x0)
    0x1061S0x10d0: REVERT v1058V10d0, v105fV10d0(0x64)

    Begin block 0x1a5dB0x10d0
    prev=[0x1008B0x10d0], succ=[0x10e3]
    =================================
    0x1a63S0x10d0: JUMP v10d4(0x10e3)

    Begin block 0x10e3
    prev=[0x1a5dB0x10d0], succ=[0x1008B0x10e3]
    =================================
    0x10e4: v10e4(0x6) = CONST 
    0x10e6: SSTORE v10e4(0x6), v100dV10d0
    0x10e7: v10e7(0x1) = CONST 
    0x10e9: v10e9(0x1) = CONST 
    0x10eb: v10eb(0xa0) = CONST 
    0x10ed: v10ed(0x10000000000000000000000000000000000000000) = SHL v10eb(0xa0), v10e9(0x1)
    0x10ee: v10ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10ed(0x10000000000000000000000000000000000000000), v10e7(0x1)
    0x10f0: v10f0 = AND v10cf_1, v10ee(0xffffffffffffffffffffffffffffffffffffffff)
    0x10f1: v10f1(0x0) = CONST 
    0x10f5: MSTORE v10f1(0x0), v10f0
    0x10f6: v10f6(0x4) = CONST 
    0x10f8: v10f8(0x20) = CONST 
    0x10fa: MSTORE v10f8(0x20), v10f6(0x4)
    0x10fb: v10fb(0x40) = CONST 
    0x10fe: v10fe = SHA3 v10f1(0x0), v10fb(0x40)
    0x10ff: v10ff = SLOAD v10fe
    0x1100: v1100(0x110f) = CONST 
    0x1105: v1105(0xffffffff) = CONST 
    0x110a: v110a(0x1008) = CONST 
    0x110d: v110d(0x1008) = AND v110a(0x1008), v1105(0xffffffff)
    0x110e: JUMP v110d(0x1008)

    Begin block 0x1008B0x10e3
    prev=[0x10e3], succ=[0x1016B0x10e3, 0x1a5dB0x10e3]
    =================================
    0x1009S0x10e3: v1009V10e3(0x0) = CONST 
    0x100dS0x10e3: v100dV10e3 = ADD v10cf_0, v10ff
    0x1010S0x10e3: v1010V10e3 = LT v100dV10e3, v10ff
    0x1011S0x10e3: v1011V10e3 = ISZERO v1010V10e3
    0x1012S0x10e3: v1012V10e3(0x1a5d) = CONST 
    0x1015S0x10e3: JUMPI v1012V10e3(0x1a5d), v1011V10e3

    Begin block 0x1016B0x10e3
    prev=[0x1008B0x10e3], succ=[]
    =================================
    0x1016S0x10e3: v1016V10e3(0x40) = CONST 
    0x1019S0x10e3: v1019V10e3 = MLOAD v1016V10e3(0x40)
    0x101aS0x10e3: v101aV10e3(0x461bcd) = CONST 
    0x101eS0x10e3: v101eV10e3(0xe5) = CONST 
    0x1020S0x10e3: v1020V10e3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v101eV10e3(0xe5), v101aV10e3(0x461bcd)
    0x1022S0x10e3: MSTORE v1019V10e3, v1020V10e3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1023S0x10e3: v1023V10e3(0x20) = CONST 
    0x1025S0x10e3: v1025V10e3(0x4) = CONST 
    0x1028S0x10e3: v1028V10e3 = ADD v1019V10e3, v1025V10e3(0x4)
    0x1029S0x10e3: MSTORE v1028V10e3, v1023V10e3(0x20)
    0x102aS0x10e3: v102aV10e3(0x1b) = CONST 
    0x102cS0x10e3: v102cV10e3(0x24) = CONST 
    0x102fS0x10e3: v102fV10e3 = ADD v1019V10e3, v102cV10e3(0x24)
    0x1030S0x10e3: MSTORE v102fV10e3, v102aV10e3(0x1b)
    0x1031S0x10e3: v1031V10e3(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x1052S0x10e3: v1052V10e3(0x44) = CONST 
    0x1055S0x10e3: v1055V10e3 = ADD v1019V10e3, v1052V10e3(0x44)
    0x1056S0x10e3: MSTORE v1055V10e3, v1031V10e3(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x1058S0x10e3: v1058V10e3 = MLOAD v1016V10e3(0x40)
    0x105cS0x10e3: v105cV10e3(0x0) = SUB v1019V10e3, v1058V10e3
    0x105dS0x10e3: v105dV10e3(0x64) = CONST 
    0x105fS0x10e3: v105fV10e3(0x64) = ADD v105dV10e3(0x64), v105cV10e3(0x0)
    0x1061S0x10e3: REVERT v1058V10e3, v105fV10e3(0x64)

    Begin block 0x1a5dB0x10e3
    prev=[0x1008B0x10e3], succ=[0x110f]
    =================================
    0x1a63S0x10e3: JUMP v1100(0x110f)

    Begin block 0x110f
    prev=[0x1a5dB0x10e3], succ=[0x945]
    =================================
    0x1110: v1110(0x1) = CONST 
    0x1112: v1112(0x1) = CONST 
    0x1114: v1114(0xa0) = CONST 
    0x1116: v1116(0x10000000000000000000000000000000000000000) = SHL v1114(0xa0), v1112(0x1)
    0x1117: v1117(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1116(0x10000000000000000000000000000000000000000), v1110(0x1)
    0x1119: v1119 = AND v10cf_1, v1117(0xffffffffffffffffffffffffffffffffffffffff)
    0x111a: v111a(0x0) = CONST 
    0x111e: MSTORE v111a(0x0), v1119
    0x111f: v111f(0x4) = CONST 
    0x1121: v1121(0x20) = CONST 
    0x1125: MSTORE v1121(0x20), v111f(0x4)
    0x1126: v1126(0x40) = CONST 
    0x112a: v112a = SHA3 v111a(0x0), v1126(0x40)
    0x112e: SSTORE v112a, v100dV10e3
    0x1130: v1130 = MLOAD v1126(0x40)
    0x1133: MSTORE v1130, v10cf_0
    0x1135: v1135 = MLOAD v1126(0x40)
    0x113a: v113a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x115e: v115e(0x0) = SUB v1130, v1135
    0x1161: v1161(0x20) = ADD v1121(0x20), v115e(0x0)
    0x1163: LOG3 v1135, v1161(0x20), v113a(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v111a(0x0), v1119
    0x1166: JUMP v10cf_2

    Begin block 0x945
    prev=[0x110f], succ=[0x173b]
    =================================
    0x948: JUMP v440

    Begin block 0x173b
    prev=[0x945], succ=[]
    =================================
    0x173c: STOP 

    Begin block 0x8d3
    prev=[0x8bf], succ=[0x8e7]
    =================================
    0x8d4: v8d4 = CALLER 
    0x8d5: v8d5(0x0) = CONST 
    0x8d9: MSTORE v8d5(0x0), v8d4
    0x8da: v8da(0x2) = CONST 
    0x8dc: v8dc(0x20) = CONST 
    0x8de: MSTORE v8dc(0x20), v8da(0x2)
    0x8df: v8df(0x40) = CONST 
    0x8e2: v8e2 = SHA3 v8d5(0x0), v8df(0x40)
    0x8e3: v8e3 = SLOAD v8e2
    0x8e4: v8e4(0xff) = CONST 
    0x8e6: v8e6 = AND v8e4(0xff), v8e3

}

function burn(uint256)() public {
    Begin block 0x44a
    prev=[], succ=[0x45c, 0x460]
    =================================
    0x44b: v44b(0x175c) = CONST 
    0x44e: v44e(0x4) = CONST 
    0x451: v451 = CALLDATASIZE 
    0x452: v452 = SUB v451, v44e(0x4)
    0x453: v453(0x20) = CONST 
    0x456: v456 = LT v452, v453(0x20)
    0x457: v457 = ISZERO v456
    0x458: v458(0x460) = CONST 
    0x45b: JUMPI v458(0x460), v457

    Begin block 0x45c
    prev=[0x44a], succ=[]
    =================================
    0x45c: v45c(0x0) = CONST 
    0x45f: REVERT v45c(0x0), v45c(0x0)

    Begin block 0x460
    prev=[0x44a], succ=[0x949]
    =================================
    0x462: v462 = CALLDATALOAD v44e(0x4)
    0x463: v463(0x949) = CONST 
    0x466: JUMP v463(0x949)

    Begin block 0x949
    prev=[0x460], succ=[0x971, 0x95d]
    =================================
    0x94a: v94a(0x0) = CONST 
    0x94c: v94c = SLOAD v94a(0x0)
    0x94d: v94d(0x1) = CONST 
    0x94f: v94f(0x1) = CONST 
    0x951: v951(0xa0) = CONST 
    0x953: v953(0x10000000000000000000000000000000000000000) = SHL v951(0xa0), v94f(0x1)
    0x954: v954(0xffffffffffffffffffffffffffffffffffffffff) = SUB v953(0x10000000000000000000000000000000000000000), v94d(0x1)
    0x955: v955 = AND v954(0xffffffffffffffffffffffffffffffffffffffff), v94c
    0x956: v956 = CALLER 
    0x957: v957 = EQ v956, v955
    0x959: v959(0x971) = CONST 
    0x95c: JUMPI v959(0x971), v957

    Begin block 0x971
    prev=[0x949, 0x95d], succ=[0x976, 0x97a]
    =================================
    0x971_0x0: v971_0 = PHI v957, v970
    0x972: v972(0x97a) = CONST 
    0x975: JUMPI v972(0x97a), v971_0

    Begin block 0x976
    prev=[0x971], succ=[]
    =================================
    0x976: v976(0x0) = CONST 
    0x979: REVERT v976(0x0), v976(0x0)

    Begin block 0x97a
    prev=[0x971], succ=[0x986, 0x9c5]
    =================================
    0x97b: v97b(0x3) = CONST 
    0x97d: v97d = SLOAD v97b(0x3)
    0x97e: v97e(0xff) = CONST 
    0x980: v980 = AND v97e(0xff), v97d
    0x981: v981 = ISZERO v980
    0x982: v982(0x9c5) = CONST 
    0x985: JUMPI v982(0x9c5), v981

    Begin block 0x986
    prev=[0x97a], succ=[]
    =================================
    0x986: v986(0x40) = CONST 
    0x989: v989 = MLOAD v986(0x40)
    0x98a: v98a(0x461bcd) = CONST 
    0x98e: v98e(0xe5) = CONST 
    0x990: v990(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v98e(0xe5), v98a(0x461bcd)
    0x992: MSTORE v989, v990(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x993: v993(0x20) = CONST 
    0x995: v995(0x4) = CONST 
    0x998: v998 = ADD v989, v995(0x4)
    0x999: MSTORE v998, v993(0x20)
    0x99a: v99a(0x10) = CONST 
    0x99c: v99c(0x24) = CONST 
    0x99f: v99f = ADD v989, v99c(0x24)
    0x9a0: MSTORE v99f, v99a(0x10)
    0x9a1: v9a1(0x14185d5cd8589b194e881c185d5cd959) = CONST 
    0x9b2: v9b2(0x82) = CONST 
    0x9b4: v9b4(0x5061757361626c653a2070617573656400000000000000000000000000000000) = SHL v9b2(0x82), v9a1(0x14185d5cd8589b194e881c185d5cd959)
    0x9b5: v9b5(0x44) = CONST 
    0x9b8: v9b8 = ADD v989, v9b5(0x44)
    0x9b9: MSTORE v9b8, v9b4(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x9bb: v9bb = MLOAD v986(0x40)
    0x9bf: v9bf(0x0) = SUB v989, v9bb
    0x9c0: v9c0(0x64) = CONST 
    0x9c2: v9c2(0x64) = ADD v9c0(0x64), v9bf(0x0)
    0x9c4: REVERT v9bb, v9c2(0x64)

    Begin block 0x9c5
    prev=[0x97a], succ=[0x1167]
    =================================
    0x9c6: v9c6(0x9cf) = CONST 
    0x9c9: v9c9 = CALLER 
    0x9cb: v9cb(0x1167) = CONST 
    0x9ce: JUMP v9cb(0x1167)

    Begin block 0x1167
    prev=[0x9c5], succ=[0x1176, 0x11ac]
    =================================
    0x1168: v1168(0x1) = CONST 
    0x116a: v116a(0x1) = CONST 
    0x116c: v116c(0xa0) = CONST 
    0x116e: v116e(0x10000000000000000000000000000000000000000) = SHL v116c(0xa0), v116a(0x1)
    0x116f: v116f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v116e(0x10000000000000000000000000000000000000000), v1168(0x1)
    0x1171: v1171 = AND v9c9, v116f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1172: v1172(0x11ac) = CONST 
    0x1175: JUMPI v1172(0x11ac), v1171

    Begin block 0x1176
    prev=[0x1167], succ=[]
    =================================
    0x1176: v1176(0x40) = CONST 
    0x1178: v1178 = MLOAD v1176(0x40)
    0x1179: v1179(0x461bcd) = CONST 
    0x117d: v117d(0xe5) = CONST 
    0x117f: v117f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v117d(0xe5), v1179(0x461bcd)
    0x1181: MSTORE v1178, v117f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1182: v1182(0x4) = CONST 
    0x1184: v1184 = ADD v1182(0x4), v1178
    0x1187: v1187(0x20) = CONST 
    0x1189: v1189 = ADD v1187(0x20), v1184
    0x118c: v118c(0x20) = SUB v1189, v1184
    0x118e: MSTORE v1184, v118c(0x20)
    0x118f: v118f(0x21) = CONST 
    0x1192: MSTORE v1189, v118f(0x21)
    0x1193: v1193(0x20) = CONST 
    0x1195: v1195 = ADD v1193(0x20), v1189
    0x1197: v1197(0x14a4) = CONST 
    0x119a: v119a(0x21) = CONST 
    0x119d: CODECOPY v1195, v1197(0x14a4), v119a(0x21)
    0x119e: v119e(0x40) = CONST 
    0x11a0: v11a0 = ADD v119e(0x40), v1195
    0x11a4: v11a4(0x40) = CONST 
    0x11a6: v11a6 = MLOAD v11a4(0x40)
    0x11a9: v11a9(0x84) = SUB v11a0, v11a6
    0x11ab: REVERT v11a6, v11a9(0x84)

    Begin block 0x11ac
    prev=[0x1167], succ=[0x11b8]
    =================================
    0x11ad: v11ad(0x11b8) = CONST 
    0x11b1: v11b1(0x0) = CONST 
    0x11b4: v11b4(0x126f) = CONST 
    0x11b7: v11b7_0, v11b7_1, v11b7_2 = CALLPRIVATE v11b4(0x126f), v462, v11b1(0x0), v9c9

    Begin block 0x11b8
    prev=[0x11ac], succ=[0x11fb]
    =================================
    0x11b9: v11b9(0x11fb) = CONST 
    0x11bd: v11bd(0x40) = CONST 
    0x11bf: v11bf = MLOAD v11bd(0x40)
    0x11c1: v11c1(0x60) = CONST 
    0x11c3: v11c3 = ADD v11c1(0x60), v11bf
    0x11c4: v11c4(0x40) = CONST 
    0x11c6: MSTORE v11c4(0x40), v11c3
    0x11c8: v11c8(0x22) = CONST 
    0x11cb: MSTORE v11bf, v11c8(0x22)
    0x11cc: v11cc(0x20) = CONST 
    0x11ce: v11ce = ADD v11cc(0x20), v11bf
    0x11cf: v11cf(0x13c4) = CONST 
    0x11d2: v11d2(0x22) = CONST 
    0x11d5: CODECOPY v11ce, v11cf(0x13c4), v11d2(0x22)
    0x11d6: v11d6(0x1) = CONST 
    0x11d8: v11d8(0x1) = CONST 
    0x11da: v11da(0xa0) = CONST 
    0x11dc: v11dc(0x10000000000000000000000000000000000000000) = SHL v11da(0xa0), v11d8(0x1)
    0x11dd: v11dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11dc(0x10000000000000000000000000000000000000000), v11d6(0x1)
    0x11df: v11df = AND v11b7_1, v11dd(0xffffffffffffffffffffffffffffffffffffffff)
    0x11e0: v11e0(0x0) = CONST 
    0x11e4: MSTORE v11e0(0x0), v11df
    0x11e5: v11e5(0x4) = CONST 
    0x11e7: v11e7(0x20) = CONST 
    0x11e9: MSTORE v11e7(0x20), v11e5(0x4)
    0x11ea: v11ea(0x40) = CONST 
    0x11ed: v11ed = SHA3 v11e0(0x0), v11ea(0x40)
    0x11ee: v11ee = SLOAD v11ed
    0x11f1: v11f1(0xffffffff) = CONST 
    0x11f6: v11f6(0xf71) = CONST 
    0x11f9: v11f9(0xf71) = AND v11f6(0xf71), v11f1(0xffffffff)
    0x11fa: v11fa_0 = CALLPRIVATE v11f9(0xf71), v11bf, v11b7_0, v11ee, v11b9(0x11fb)

    Begin block 0x11fb
    prev=[0x11b8], succ=[0x12c6B0x11fb]
    =================================
    0x11fc: v11fc(0x1) = CONST 
    0x11fe: v11fe(0x1) = CONST 
    0x1200: v1200(0xa0) = CONST 
    0x1202: v1202(0x10000000000000000000000000000000000000000) = SHL v1200(0xa0), v11fe(0x1)
    0x1203: v1203(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1202(0x10000000000000000000000000000000000000000), v11fc(0x1)
    0x1205: v1205 = AND v11b7_1, v1203(0xffffffffffffffffffffffffffffffffffffffff)
    0x1206: v1206(0x0) = CONST 
    0x120a: MSTORE v1206(0x0), v1205
    0x120b: v120b(0x4) = CONST 
    0x120d: v120d(0x20) = CONST 
    0x120f: MSTORE v120d(0x20), v120b(0x4)
    0x1210: v1210(0x40) = CONST 
    0x1213: v1213 = SHA3 v1206(0x0), v1210(0x40)
    0x1214: SSTORE v1213, v11fa_0
    0x1215: v1215(0x6) = CONST 
    0x1217: v1217 = SLOAD v1215(0x6)
    0x1218: v1218(0x1227) = CONST 
    0x121d: v121d(0xffffffff) = CONST 
    0x1222: v1222(0x12c6) = CONST 
    0x1225: v1225(0x12c6) = AND v1222(0x12c6), v121d(0xffffffff)
    0x1226: JUMP v1225(0x12c6)

    Begin block 0x12c6B0x11fb
    prev=[0x11fb], succ=[0x1a83B0x11fb]
    =================================
    0x12c7S0x11fb: v12c7V11fb(0x0) = CONST 
    0x12c9S0x11fb: v12c9V11fb(0x1a83) = CONST 
    0x12ceS0x11fb: v12ceV11fb(0x40) = CONST 
    0x12d0S0x11fb: v12d0V11fb = MLOAD v12ceV11fb(0x40)
    0x12d2S0x11fb: v12d2V11fb(0x40) = CONST 
    0x12d4S0x11fb: v12d4V11fb = ADD v12d2V11fb(0x40), v12d0V11fb
    0x12d5S0x11fb: v12d5V11fb(0x40) = CONST 
    0x12d7S0x11fb: MSTORE v12d5V11fb(0x40), v12d4V11fb
    0x12d9S0x11fb: v12d9V11fb(0x1e) = CONST 
    0x12dcS0x11fb: MSTORE v12d0V11fb, v12d9V11fb(0x1e)
    0x12ddS0x11fb: v12ddV11fb(0x20) = CONST 
    0x12dfS0x11fb: v12dfV11fb = ADD v12ddV11fb(0x20), v12d0V11fb
    0x12e0S0x11fb: v12e0V11fb(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x1302S0x11fb: MSTORE v12dfV11fb, v12e0V11fb(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1304S0x11fb: v1304V11fb(0xf71) = CONST 
    0x1307S0x11fb: v1307_0V11fb = CALLPRIVATE v1304V11fb(0xf71), v12d0V11fb, v11b7_0, v1217, v12c9V11fb(0x1a83)

    Begin block 0x1a83B0x11fb
    prev=[0x12c6B0x11fb], succ=[0x1227]
    =================================
    0x1a89S0x11fb: JUMP v1218(0x1227)

    Begin block 0x1227
    prev=[0x1a83B0x11fb], succ=[0x9cf]
    =================================
    0x1228: v1228(0x6) = CONST 
    0x122a: SSTORE v1228(0x6), v1307_0V11fb
    0x122b: v122b(0x40) = CONST 
    0x122e: v122e = MLOAD v122b(0x40)
    0x1231: MSTORE v122e, v11b7_0
    0x1233: v1233 = MLOAD v122b(0x40)
    0x1234: v1234(0x0) = CONST 
    0x1237: v1237(0x1) = CONST 
    0x1239: v1239(0x1) = CONST 
    0x123b: v123b(0xa0) = CONST 
    0x123d: v123d(0x10000000000000000000000000000000000000000) = SHL v123b(0xa0), v1239(0x1)
    0x123e: v123e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v123d(0x10000000000000000000000000000000000000000), v1237(0x1)
    0x1240: v1240 = AND v11b7_1, v123e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1242: v1242(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1266: v1266(0x0) = SUB v122e, v1233
    0x1267: v1267(0x20) = CONST 
    0x1269: v1269(0x20) = ADD v1267(0x20), v1266(0x0)
    0x126b: LOG3 v1233, v1269(0x20), v1242(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1240, v1234(0x0)
    0x126e: JUMP v11b7_2

    Begin block 0x9cf
    prev=[0x1227], succ=[0x175c]
    =================================
    0x9d1: JUMP v462

    Begin block 0x175c
    prev=[0x9cf], succ=[]
    =================================
    0x175d: STOP 

    Begin block 0x95d
    prev=[0x949], succ=[0x971]
    =================================
    0x95e: v95e = CALLER 
    0x95f: v95f(0x0) = CONST 
    0x963: MSTORE v95f(0x0), v95e
    0x964: v964(0x2) = CONST 
    0x966: v966(0x20) = CONST 
    0x968: MSTORE v966(0x20), v964(0x2)
    0x969: v969(0x40) = CONST 
    0x96c: v96c = SHA3 v95f(0x0), v969(0x40)
    0x96d: v96d = SLOAD v96c
    0x96e: v96e(0xff) = CONST 
    0x970: v970 = AND v96e(0xff), v96d

}

function paused()() public {
    Begin block 0x467
    prev=[], succ=[0x9d2]
    =================================
    0x468: v468(0x177d) = CONST 
    0x46b: v46b(0x9d2) = CONST 
    0x46e: JUMP v46b(0x9d2)

    Begin block 0x9d2
    prev=[0x467], succ=[0x177d]
    =================================
    0x9d3: v9d3(0x3) = CONST 
    0x9d5: v9d5 = SLOAD v9d3(0x3)
    0x9d6: v9d6(0xff) = CONST 
    0x9d8: v9d8 = AND v9d6(0xff), v9d5
    0x9da: JUMP v468(0x177d)

    Begin block 0x177d
    prev=[0x9d2], succ=[]
    =================================
    0x177e: v177e(0x40) = CONST 
    0x1781: v1781 = MLOAD v177e(0x40)
    0x1783: v1783 = ISZERO v9d8
    0x1784: v1784 = ISZERO v1783
    0x1786: MSTORE v1781, v1784
    0x1787: v1787 = MLOAD v177e(0x40)
    0x178b: v178b(0x0) = SUB v1781, v1787
    0x178c: v178c(0x20) = CONST 
    0x178e: v178e(0x20) = ADD v178c(0x20), v178b(0x0)
    0x1790: RETURN v1787, v178e(0x20)

}

function addAdmin(address)() public {
    Begin block 0x46f
    prev=[], succ=[0x481, 0x485]
    =================================
    0x470: v470(0x17b0) = CONST 
    0x473: v473(0x4) = CONST 
    0x476: v476 = CALLDATASIZE 
    0x477: v477 = SUB v476, v473(0x4)
    0x478: v478(0x20) = CONST 
    0x47b: v47b = LT v477, v478(0x20)
    0x47c: v47c = ISZERO v47b
    0x47d: v47d(0x485) = CONST 
    0x480: JUMPI v47d(0x485), v47c

    Begin block 0x481
    prev=[0x46f], succ=[]
    =================================
    0x481: v481(0x0) = CONST 
    0x484: REVERT v481(0x0), v481(0x0)

    Begin block 0x485
    prev=[0x46f], succ=[0x9db]
    =================================
    0x487: v487 = CALLDATALOAD v473(0x4)
    0x488: v488(0x1) = CONST 
    0x48a: v48a(0x1) = CONST 
    0x48c: v48c(0xa0) = CONST 
    0x48e: v48e(0x10000000000000000000000000000000000000000) = SHL v48c(0xa0), v48a(0x1)
    0x48f: v48f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48e(0x10000000000000000000000000000000000000000), v488(0x1)
    0x490: v490 = AND v48f(0xffffffffffffffffffffffffffffffffffffffff), v487
    0x491: v491(0x9db) = CONST 
    0x494: JUMP v491(0x9db)

    Begin block 0x9db
    prev=[0x485], succ=[0x9ee, 0xa3a]
    =================================
    0x9dc: v9dc(0x0) = CONST 
    0x9de: v9de = SLOAD v9dc(0x0)
    0x9df: v9df(0x1) = CONST 
    0x9e1: v9e1(0x1) = CONST 
    0x9e3: v9e3(0xa0) = CONST 
    0x9e5: v9e5(0x10000000000000000000000000000000000000000) = SHL v9e3(0xa0), v9e1(0x1)
    0x9e6: v9e6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9e5(0x10000000000000000000000000000000000000000), v9df(0x1)
    0x9e7: v9e7 = AND v9e6(0xffffffffffffffffffffffffffffffffffffffff), v9de
    0x9e8: v9e8 = CALLER 
    0x9e9: v9e9 = EQ v9e8, v9e7
    0x9ea: v9ea(0xa3a) = CONST 
    0x9ed: JUMPI v9ea(0xa3a), v9e9

    Begin block 0x9ee
    prev=[0x9db], succ=[]
    =================================
    0x9ee: v9ee(0x40) = CONST 
    0x9f1: v9f1 = MLOAD v9ee(0x40)
    0x9f2: v9f2(0x461bcd) = CONST 
    0x9f6: v9f6(0xe5) = CONST 
    0x9f8: v9f8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v9f6(0xe5), v9f2(0x461bcd)
    0x9fa: MSTORE v9f1, v9f8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9fb: v9fb(0x20) = CONST 
    0x9fd: v9fd(0x4) = CONST 
    0xa00: va00 = ADD v9f1, v9fd(0x4)
    0xa03: MSTORE va00, v9fb(0x20)
    0xa04: va04(0x24) = CONST 
    0xa07: va07 = ADD v9f1, va04(0x24)
    0xa08: MSTORE va07, v9fb(0x20)
    0xa09: va09(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xa2a: va2a(0x44) = CONST 
    0xa2d: va2d = ADD v9f1, va2a(0x44)
    0xa2e: MSTORE va2d, va09(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xa30: va30 = MLOAD v9ee(0x40)
    0xa34: va34(0x0) = SUB v9f1, va30
    0xa35: va35(0x64) = CONST 
    0xa37: va37(0x64) = ADD va35(0x64), va34(0x0)
    0xa39: REVERT va30, va37(0x64)

    Begin block 0xa3a
    prev=[0x9db], succ=[0x17b0]
    =================================
    0xa3b: va3b(0x1) = CONST 
    0xa3d: va3d(0x1) = CONST 
    0xa3f: va3f(0xa0) = CONST 
    0xa41: va41(0x10000000000000000000000000000000000000000) = SHL va3f(0xa0), va3d(0x1)
    0xa42: va42(0xffffffffffffffffffffffffffffffffffffffff) = SUB va41(0x10000000000000000000000000000000000000000), va3b(0x1)
    0xa43: va43 = AND va42(0xffffffffffffffffffffffffffffffffffffffff), v490
    0xa44: va44(0x0) = CONST 
    0xa48: MSTORE va44(0x0), va43
    0xa49: va49(0x2) = CONST 
    0xa4b: va4b(0x20) = CONST 
    0xa4d: MSTORE va4b(0x20), va49(0x2)
    0xa4e: va4e(0x40) = CONST 
    0xa51: va51 = SHA3 va44(0x0), va4e(0x40)
    0xa53: va53 = SLOAD va51
    0xa54: va54(0xff) = CONST 
    0xa56: va56(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT va54(0xff)
    0xa57: va57 = AND va56(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), va53
    0xa58: va58(0x1) = CONST 
    0xa5a: va5a = OR va58(0x1), va57
    0xa5c: SSTORE va51, va5a
    0xa5d: JUMP v470(0x17b0)

    Begin block 0x17b0
    prev=[0xa3a], succ=[]
    =================================
    0x17b1: STOP 

}

function balanceOf(address)() public {
    Begin block 0x495
    prev=[], succ=[0x4a7, 0x4ab]
    =================================
    0x496: v496(0x17d1) = CONST 
    0x499: v499(0x4) = CONST 
    0x49c: v49c = CALLDATASIZE 
    0x49d: v49d = SUB v49c, v499(0x4)
    0x49e: v49e(0x20) = CONST 
    0x4a1: v4a1 = LT v49d, v49e(0x20)
    0x4a2: v4a2 = ISZERO v4a1
    0x4a3: v4a3(0x4ab) = CONST 
    0x4a6: JUMPI v4a3(0x4ab), v4a2

    Begin block 0x4a7
    prev=[0x495], succ=[]
    =================================
    0x4a7: v4a7(0x0) = CONST 
    0x4aa: REVERT v4a7(0x0), v4a7(0x0)

    Begin block 0x4ab
    prev=[0x495], succ=[0xa5e]
    =================================
    0x4ad: v4ad = CALLDATALOAD v499(0x4)
    0x4ae: v4ae(0x1) = CONST 
    0x4b0: v4b0(0x1) = CONST 
    0x4b2: v4b2(0xa0) = CONST 
    0x4b4: v4b4(0x10000000000000000000000000000000000000000) = SHL v4b2(0xa0), v4b0(0x1)
    0x4b5: v4b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b4(0x10000000000000000000000000000000000000000), v4ae(0x1)
    0x4b6: v4b6 = AND v4b5(0xffffffffffffffffffffffffffffffffffffffff), v4ad
    0x4b7: v4b7(0xa5e) = CONST 
    0x4ba: JUMP v4b7(0xa5e)

    Begin block 0xa5e
    prev=[0x4ab], succ=[0x17d1]
    =================================
    0xa5f: va5f(0x1) = CONST 
    0xa61: va61(0x1) = CONST 
    0xa63: va63(0xa0) = CONST 
    0xa65: va65(0x10000000000000000000000000000000000000000) = SHL va63(0xa0), va61(0x1)
    0xa66: va66(0xffffffffffffffffffffffffffffffffffffffff) = SUB va65(0x10000000000000000000000000000000000000000), va5f(0x1)
    0xa67: va67 = AND va66(0xffffffffffffffffffffffffffffffffffffffff), v4b6
    0xa68: va68(0x0) = CONST 
    0xa6c: MSTORE va68(0x0), va67
    0xa6d: va6d(0x4) = CONST 
    0xa6f: va6f(0x20) = CONST 
    0xa71: MSTORE va6f(0x20), va6d(0x4)
    0xa72: va72(0x40) = CONST 
    0xa75: va75 = SHA3 va68(0x0), va72(0x40)
    0xa76: va76 = SLOAD va75
    0xa78: JUMP v496(0x17d1)

    Begin block 0x17d1
    prev=[0xa5e], succ=[]
    =================================
    0x17d2: v17d2(0x40) = CONST 
    0x17d5: v17d5 = MLOAD v17d2(0x40)
    0x17d8: MSTORE v17d5, va76
    0x17d9: v17d9 = MLOAD v17d2(0x40)
    0x17dd: v17dd(0x0) = SUB v17d5, v17d9
    0x17de: v17de(0x20) = CONST 
    0x17e0: v17e0(0x20) = ADD v17de(0x20), v17dd(0x0)
    0x17e2: RETURN v17d9, v17e0(0x20)

}

function acceptOwnership()() public {
    Begin block 0x4bb
    prev=[], succ=[0xa79]
    =================================
    0x4bc: v4bc(0x1802) = CONST 
    0x4bf: v4bf(0xa79) = CONST 
    0x4c2: JUMP v4bf(0xa79)

    Begin block 0xa79
    prev=[0x4bb], succ=[0xa8c, 0xac2]
    =================================
    0xa7a: va7a(0x1) = CONST 
    0xa7c: va7c = SLOAD va7a(0x1)
    0xa7d: va7d(0x1) = CONST 
    0xa7f: va7f(0x1) = CONST 
    0xa81: va81(0xa0) = CONST 
    0xa83: va83(0x10000000000000000000000000000000000000000) = SHL va81(0xa0), va7f(0x1)
    0xa84: va84(0xffffffffffffffffffffffffffffffffffffffff) = SUB va83(0x10000000000000000000000000000000000000000), va7d(0x1)
    0xa85: va85 = AND va84(0xffffffffffffffffffffffffffffffffffffffff), va7c
    0xa86: va86 = CALLER 
    0xa87: va87 = EQ va86, va85
    0xa88: va88(0xac2) = CONST 
    0xa8b: JUMPI va88(0xac2), va87

    Begin block 0xa8c
    prev=[0xa79], succ=[]
    =================================
    0xa8c: va8c(0x40) = CONST 
    0xa8e: va8e = MLOAD va8c(0x40)
    0xa8f: va8f(0x461bcd) = CONST 
    0xa93: va93(0xe5) = CONST 
    0xa95: va95(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL va93(0xe5), va8f(0x461bcd)
    0xa97: MSTORE va8e, va95(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa98: va98(0x4) = CONST 
    0xa9a: va9a = ADD va98(0x4), va8e
    0xa9d: va9d(0x20) = CONST 
    0xa9f: va9f = ADD va9d(0x20), va9a
    0xaa2: vaa2(0x20) = SUB va9f, va9a
    0xaa4: MSTORE va9a, vaa2(0x20)
    0xaa5: vaa5(0x28) = CONST 
    0xaa8: MSTORE va9f, vaa5(0x28)
    0xaa9: vaa9(0x20) = CONST 
    0xaab: vaab = ADD vaa9(0x20), va9f
    0xaad: vaad(0x147c) = CONST 
    0xab0: vab0(0x28) = CONST 
    0xab3: CODECOPY vaab, vaad(0x147c), vab0(0x28)
    0xab4: vab4(0x40) = CONST 
    0xab6: vab6 = ADD vab4(0x40), vaab
    0xaba: vaba(0x40) = CONST 
    0xabc: vabc = MLOAD vaba(0x40)
    0xabf: vabf(0x84) = SUB vab6, vabc
    0xac1: REVERT vabc, vabf(0x84)

    Begin block 0xac2
    prev=[0xa79], succ=[0x1802]
    =================================
    0xac3: vac3(0x1) = CONST 
    0xac5: vac5 = SLOAD vac3(0x1)
    0xac6: vac6(0x0) = CONST 
    0xac9: vac9 = SLOAD vac6(0x0)
    0xaca: vaca(0x40) = CONST 
    0xacc: vacc = MLOAD vaca(0x40)
    0xacd: vacd(0x1) = CONST 
    0xacf: vacf(0x1) = CONST 
    0xad1: vad1(0xa0) = CONST 
    0xad3: vad3(0x10000000000000000000000000000000000000000) = SHL vad1(0xa0), vacf(0x1)
    0xad4: vad4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vad3(0x10000000000000000000000000000000000000000), vacd(0x1)
    0xad7: vad7 = AND vad4(0xffffffffffffffffffffffffffffffffffffffff), vac5
    0xadb: vadb = AND vac9, vad4(0xffffffffffffffffffffffffffffffffffffffff)
    0xadd: vadd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xaff: LOG3 vacc, vac6(0x0), vadd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vadb, vad7
    0xb00: vb00(0x1) = CONST 
    0xb03: vb03 = SLOAD vb00(0x1)
    0xb04: vb04(0x0) = CONST 
    0xb07: vb07 = SLOAD vb04(0x0)
    0xb08: vb08(0x1) = CONST 
    0xb0a: vb0a(0x1) = CONST 
    0xb0c: vb0c(0xa0) = CONST 
    0xb0e: vb0e(0x10000000000000000000000000000000000000000) = SHL vb0c(0xa0), vb0a(0x1)
    0xb0f: vb0f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb0e(0x10000000000000000000000000000000000000000), vb08(0x1)
    0xb10: vb10(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vb0f(0xffffffffffffffffffffffffffffffffffffffff)
    0xb13: vb13 = AND vb10(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb07
    0xb14: vb14(0x1) = CONST 
    0xb16: vb16(0x1) = CONST 
    0xb18: vb18(0xa0) = CONST 
    0xb1a: vb1a(0x10000000000000000000000000000000000000000) = SHL vb18(0xa0), vb16(0x1)
    0xb1b: vb1b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb1a(0x10000000000000000000000000000000000000000), vb14(0x1)
    0xb1d: vb1d = AND vb03, vb1b(0xffffffffffffffffffffffffffffffffffffffff)
    0xb1e: vb1e = OR vb1d, vb13
    0xb21: SSTORE vb04(0x0), vb1e
    0xb22: vb22 = AND vb10(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb03
    0xb24: SSTORE vb00(0x1), vb22
    0xb25: JUMP v4bc(0x1802)

    Begin block 0x1802
    prev=[0xac2], succ=[]
    =================================
    0x1803: STOP 

}

function owner()() public {
    Begin block 0x4c3
    prev=[], succ=[0xb26]
    =================================
    0x4c4: v4c4(0x1823) = CONST 
    0x4c7: v4c7(0xb26) = CONST 
    0x4ca: JUMP v4c7(0xb26)

    Begin block 0xb26
    prev=[0x4c3], succ=[0x1823]
    =================================
    0xb27: vb27(0x0) = CONST 
    0xb29: vb29 = SLOAD vb27(0x0)
    0xb2a: vb2a(0x1) = CONST 
    0xb2c: vb2c(0x1) = CONST 
    0xb2e: vb2e(0xa0) = CONST 
    0xb30: vb30(0x10000000000000000000000000000000000000000) = SHL vb2e(0xa0), vb2c(0x1)
    0xb31: vb31(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb30(0x10000000000000000000000000000000000000000), vb2a(0x1)
    0xb32: vb32 = AND vb31(0xffffffffffffffffffffffffffffffffffffffff), vb29
    0xb34: JUMP v4c4(0x1823)

    Begin block 0x1823
    prev=[0xb26], succ=[]
    =================================
    0x1824: v1824(0x40) = CONST 
    0x1827: v1827 = MLOAD v1824(0x40)
    0x1828: v1828(0x1) = CONST 
    0x182a: v182a(0x1) = CONST 
    0x182c: v182c(0xa0) = CONST 
    0x182e: v182e(0x10000000000000000000000000000000000000000) = SHL v182c(0xa0), v182a(0x1)
    0x182f: v182f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v182e(0x10000000000000000000000000000000000000000), v1828(0x1)
    0x1832: v1832 = AND vb32, v182f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1834: MSTORE v1827, v1832
    0x1835: v1835 = MLOAD v1824(0x40)
    0x1839: v1839(0x0) = SUB v1827, v1835
    0x183a: v183a(0x20) = CONST 
    0x183c: v183c(0x20) = ADD v183a(0x20), v1839(0x0)
    0x183e: RETURN v1835, v183c(0x20)

}

function symbol()() public {
    Begin block 0x4e7
    prev=[], succ=[0xb35B0x4e7]
    =================================
    0x4e8: v4e8(0x14f) = CONST 
    0x4eb: v4eb(0xb35) = CONST 
    0x4ee: JUMP v4eb(0xb35)

    Begin block 0xb35B0x4e7
    prev=[0x4e7], succ=[0xb7bB0x4e7, 0x62f0xb35B0x4e7]
    =================================
    0xb36S0x4e7: vb36V4e7(0x8) = CONST 
    0xb39S0x4e7: vb39V4e7 = SLOAD vb36V4e7(0x8)
    0xb3aS0x4e7: vb3aV4e7(0x40) = CONST 
    0xb3dS0x4e7: vb3dV4e7 = MLOAD vb3aV4e7(0x40)
    0xb3eS0x4e7: vb3eV4e7(0x20) = CONST 
    0xb40S0x4e7: vb40V4e7(0x1f) = CONST 
    0xb42S0x4e7: vb42V4e7(0x2) = CONST 
    0xb44S0x4e7: vb44V4e7(0x0) = CONST 
    0xb46S0x4e7: vb46V4e7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vb44V4e7(0x0)
    0xb47S0x4e7: vb47V4e7(0x100) = CONST 
    0xb4aS0x4e7: vb4aV4e7(0x1) = CONST 
    0xb4dS0x4e7: vb4dV4e7 = AND vb39V4e7, vb4aV4e7(0x1)
    0xb4eS0x4e7: vb4eV4e7 = ISZERO vb4dV4e7
    0xb4fS0x4e7: vb4fV4e7 = MUL vb4eV4e7, vb47V4e7(0x100)
    0xb50S0x4e7: vb50V4e7 = ADD vb4fV4e7, vb46V4e7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xb53S0x4e7: vb53V4e7 = AND vb39V4e7, vb50V4e7
    0xb57S0x4e7: vb57V4e7 = DIV vb53V4e7, vb42V4e7(0x2)
    0xb5aS0x4e7: vb5aV4e7 = ADD vb57V4e7, vb40V4e7(0x1f)
    0xb5dS0x4e7: vb5dV4e7 = DIV vb5aV4e7, vb3eV4e7(0x20)
    0xb5fS0x4e7: vb5fV4e7 = MUL vb3eV4e7(0x20), vb5dV4e7
    0xb61S0x4e7: vb61V4e7 = ADD vb3dV4e7, vb5fV4e7
    0xb63S0x4e7: vb63V4e7 = ADD vb3eV4e7(0x20), vb61V4e7
    0xb66S0x4e7: MSTORE vb3aV4e7(0x40), vb63V4e7
    0xb69S0x4e7: MSTORE vb3dV4e7, vb57V4e7
    0xb6aS0x4e7: vb6aV4e7(0x60) = CONST 
    0xb72S0x4e7: vb72V4e7 = ADD vb3dV4e7, vb3eV4e7(0x20)
    0xb76S0x4e7: vb76V4e7 = ISZERO vb57V4e7
    0xb77S0x4e7: vb77V4e7(0x62f) = CONST 
    0xb7aS0x4e7: JUMPI vb77V4e7(0x62f), vb76V4e7

    Begin block 0xb7bB0x4e7
    prev=[0xb35B0x4e7], succ=[0xb83B0x4e7, 0x6040xb35B0x4e7]
    =================================
    0xb7cS0x4e7: vb7cV4e7(0x1f) = CONST 
    0xb7eS0x4e7: vb7eV4e7 = LT vb7cV4e7(0x1f), vb57V4e7
    0xb7fS0x4e7: vb7fV4e7(0x604) = CONST 
    0xb82S0x4e7: JUMPI vb7fV4e7(0x604), vb7eV4e7

    Begin block 0xb83B0x4e7
    prev=[0xb7bB0x4e7], succ=[0x62f0xb35B0x4e7]
    =================================
    0xb83S0x4e7: vb83V4e7(0x100) = CONST 
    0xb88S0x4e7: vb88V4e7 = SLOAD vb36V4e7(0x8)
    0xb89S0x4e7: vb89V4e7 = DIV vb88V4e7, vb83V4e7(0x100)
    0xb8aS0x4e7: vb8aV4e7 = MUL vb89V4e7, vb83V4e7(0x100)
    0xb8cS0x4e7: MSTORE vb72V4e7, vb8aV4e7
    0xb8eS0x4e7: vb8eV4e7(0x20) = CONST 
    0xb90S0x4e7: vb90V4e7 = ADD vb8eV4e7(0x20), vb72V4e7
    0xb92S0x4e7: vb92V4e7(0x62f) = CONST 
    0xb95S0x4e7: JUMP vb92V4e7(0x62f)

    Begin block 0x62f0xb35B0x4e7
    prev=[0xb83B0x4e7, 0xb35B0x4e7, 0x6260xb35B0x4e7], succ=[0x6370xb35B0x4e7]
    =================================

    Begin block 0x6370xb35B0x4e7
    prev=[0x62f0xb35B0x4e7], succ=[0x14f0x4e7]
    =================================
    0x6390xb35S0x4e7: JUMP v4e8(0x14f)

    Begin block 0x14f0x4e7
    prev=[0x6370xb35B0x4e7], succ=[0x1710x4e7]
    =================================
    0x1500x4e7: v4e7150(0x40) = CONST 
    0x1530x4e7: v4e7153 = MLOAD v4e7150(0x40)
    0x1540x4e7: v4e7154(0x20) = CONST 
    0x1580x4e7: MSTORE v4e7153, v4e7154(0x20)
    0x15a0x4e7: v4e715a = MLOAD vb3dV4e7
    0x15d0x4e7: v4e715d = ADD v4e7153, v4e7154(0x20)
    0x15e0x4e7: MSTORE v4e715d, v4e715a
    0x1600x4e7: v4e7160 = MLOAD vb3dV4e7
    0x1670x4e7: v4e7167 = ADD v4e7153, v4e7150(0x40)
    0x16a0x4e7: v4e716a = ADD vb3dV4e7, v4e7154(0x20)
    0x16f0x4e7: v4e716f(0x0) = CONST 

    Begin block 0x1710x4e7
    prev=[0x17a0x4e7, 0x14f0x4e7], succ=[0x1890x4e7, 0x17a0x4e7]
    =================================
    0x1710x4e7_0x0: v1714e7_0 = PHI v4e7184, v4e716f(0x0)
    0x1740x4e7: v4e7174 = LT v1714e7_0, v4e7160
    0x1750x4e7: v4e7175 = ISZERO v4e7174
    0x1760x4e7: v4e7176(0x189) = CONST 
    0x1790x4e7: JUMPI v4e7176(0x189), v4e7175

    Begin block 0x1890x4e7
    prev=[0x1710x4e7], succ=[0x1b60x4e7, 0x19d0x4e7]
    =================================
    0x1920x4e7: v4e7192 = ADD v4e7160, v4e7167
    0x1940x4e7: v4e7194(0x1f) = CONST 
    0x1960x4e7: v4e7196 = AND v4e7194(0x1f), v4e7160
    0x1980x4e7: v4e7198 = ISZERO v4e7196
    0x1990x4e7: v4e7199(0x1b6) = CONST 
    0x19c0x4e7: JUMPI v4e7199(0x1b6), v4e7198

    Begin block 0x1b60x4e7
    prev=[0x1890x4e7, 0x19d0x4e7], succ=[]
    =================================
    0x1b60x4e7_0x1: v1b64e7_1 = PHI v4e71b3, v4e7192
    0x1bc0x4e7: v4e71bc(0x40) = CONST 
    0x1be0x4e7: v4e71be = MLOAD v4e71bc(0x40)
    0x1c10x4e7: v4e71c1 = SUB v1b64e7_1, v4e71be
    0x1c30x4e7: RETURN v4e71be, v4e71c1

    Begin block 0x19d0x4e7
    prev=[0x1890x4e7], succ=[0x1b60x4e7]
    =================================
    0x19f0x4e7: v4e719f = SUB v4e7192, v4e7196
    0x1a10x4e7: v4e71a1 = MLOAD v4e719f
    0x1a20x4e7: v4e71a2(0x1) = CONST 
    0x1a50x4e7: v4e71a5(0x20) = CONST 
    0x1a70x4e7: v4e71a7 = SUB v4e71a5(0x20), v4e7196
    0x1a80x4e7: v4e71a8(0x100) = CONST 
    0x1ab0x4e7: v4e71ab = EXP v4e71a8(0x100), v4e71a7
    0x1ac0x4e7: v4e71ac = SUB v4e71ab, v4e71a2(0x1)
    0x1ad0x4e7: v4e71ad = NOT v4e71ac
    0x1ae0x4e7: v4e71ae = AND v4e71ad, v4e71a1
    0x1b00x4e7: MSTORE v4e719f, v4e71ae
    0x1b10x4e7: v4e71b1(0x20) = CONST 
    0x1b30x4e7: v4e71b3 = ADD v4e71b1(0x20), v4e719f

    Begin block 0x17a0x4e7
    prev=[0x1710x4e7], succ=[0x1710x4e7]
    =================================
    0x17a0x4e7_0x0: v17a4e7_0 = PHI v4e7184, v4e716f(0x0)
    0x17c0x4e7: v4e717c = ADD v17a4e7_0, v4e716a
    0x17d0x4e7: v4e717d = MLOAD v4e717c
    0x1800x4e7: v4e7180 = ADD v17a4e7_0, v4e7167
    0x1810x4e7: MSTORE v4e7180, v4e717d
    0x1820x4e7: v4e7182(0x20) = CONST 
    0x1840x4e7: v4e7184 = ADD v4e7182(0x20), v17a4e7_0
    0x1850x4e7: v4e7185(0x171) = CONST 
    0x1880x4e7: JUMP v4e7185(0x171)

    Begin block 0x6040xb35B0x4e7
    prev=[0xb7bB0x4e7], succ=[0x6120xb35B0x4e7]
    =================================
    0x6060xb35S0x4e7: vb35606V4e7 = ADD vb72V4e7, vb57V4e7
    0x6090xb35S0x4e7: vb35609V4e7(0x0) = CONST 
    0x60b0xb35S0x4e7: MSTORE vb35609V4e7(0x0), vb36V4e7(0x8)
    0x60c0xb35S0x4e7: vb3560cV4e7(0x20) = CONST 
    0x60e0xb35S0x4e7: vb3560eV4e7(0x0) = CONST 
    0x6100xb35S0x4e7: vb35610V4e7 = SHA3 vb3560eV4e7(0x0), vb3560cV4e7(0x20)

    Begin block 0x6120xb35B0x4e7
    prev=[0x6040xb35B0x4e7, 0x6120xb35B0x4e7], succ=[0x6120xb35B0x4e7, 0x6260xb35B0x4e7]
    =================================
    0x6120xb35_0x0S0x4e7: v612b35_0V4e7 = PHI vb72V4e7, vb3561eV4e7
    0x6120xb35_0x1S0x4e7: v612b35_1V4e7 = PHI vb35610V4e7, vb3561aV4e7
    0x6140xb35S0x4e7: vb35614V4e7 = SLOAD v612b35_1V4e7
    0x6160xb35S0x4e7: MSTORE v612b35_0V4e7, vb35614V4e7
    0x6180xb35S0x4e7: vb35618V4e7(0x1) = CONST 
    0x61a0xb35S0x4e7: vb3561aV4e7 = ADD vb35618V4e7(0x1), v612b35_1V4e7
    0x61c0xb35S0x4e7: vb3561cV4e7(0x20) = CONST 
    0x61e0xb35S0x4e7: vb3561eV4e7 = ADD vb3561cV4e7(0x20), v612b35_0V4e7
    0x6210xb35S0x4e7: vb35621V4e7 = GT vb35606V4e7, vb3561eV4e7
    0x6220xb35S0x4e7: vb35622V4e7(0x612) = CONST 
    0x6250xb35S0x4e7: JUMPI vb35622V4e7(0x612), vb35621V4e7

    Begin block 0x6260xb35B0x4e7
    prev=[0x6120xb35B0x4e7], succ=[0x62f0xb35B0x4e7]
    =================================
    0x6280xb35S0x4e7: vb35628V4e7 = SUB vb3561eV4e7, vb35606V4e7
    0x6290xb35S0x4e7: vb35629V4e7(0x1f) = CONST 
    0x62b0xb35S0x4e7: vb3562bV4e7 = AND vb35629V4e7(0x1f), vb35628V4e7
    0x62d0xb35S0x4e7: vb3562dV4e7 = ADD vb35606V4e7, vb3562bV4e7

}

function decreaseAllowance(address,uint256)() public {
    Begin block 0x4ef
    prev=[], succ=[0x501, 0x505]
    =================================
    0x4f0: v4f0(0x185e) = CONST 
    0x4f3: v4f3(0x4) = CONST 
    0x4f6: v4f6 = CALLDATASIZE 
    0x4f7: v4f7 = SUB v4f6, v4f3(0x4)
    0x4f8: v4f8(0x40) = CONST 
    0x4fb: v4fb = LT v4f7, v4f8(0x40)
    0x4fc: v4fc = ISZERO v4fb
    0x4fd: v4fd(0x505) = CONST 
    0x500: JUMPI v4fd(0x505), v4fc

    Begin block 0x501
    prev=[0x4ef], succ=[]
    =================================
    0x501: v501(0x0) = CONST 
    0x504: REVERT v501(0x0), v501(0x0)

    Begin block 0x505
    prev=[0x4ef], succ=[0xb96]
    =================================
    0x507: v507(0x1) = CONST 
    0x509: v509(0x1) = CONST 
    0x50b: v50b(0xa0) = CONST 
    0x50d: v50d(0x10000000000000000000000000000000000000000) = SHL v50b(0xa0), v509(0x1)
    0x50e: v50e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v50d(0x10000000000000000000000000000000000000000), v507(0x1)
    0x510: v510 = CALLDATALOAD v4f3(0x4)
    0x511: v511 = AND v510, v50e(0xffffffffffffffffffffffffffffffffffffffff)
    0x513: v513(0x20) = CONST 
    0x515: v515(0x24) = ADD v513(0x20), v4f3(0x4)
    0x516: v516 = CALLDATALOAD v515(0x24)
    0x517: v517(0xb96) = CONST 
    0x51a: JUMP v517(0xb96)

    Begin block 0xb96
    prev=[0x505], succ=[0xd18B0xb96]
    =================================
    0xb97: vb97(0x0) = CONST 
    0xb99: vb99(0x19e9) = CONST 
    0xb9c: vb9c(0xba3) = CONST 
    0xb9f: vb9f(0xd18) = CONST 
    0xba2: JUMP vb9f(0xd18)

    Begin block 0xd18B0xb96
    prev=[0xb96], succ=[0xba3]
    =================================
    0xd19S0xb96: vd19Vb96 = CALLER 
    0xd1bS0xb96: JUMP vb9c(0xba3)

    Begin block 0xba3
    prev=[0xd18B0xb96], succ=[0xd18B0xba3]
    =================================
    0xba5: vba5(0x1a11) = CONST 
    0xba9: vba9(0x40) = CONST 
    0xbab: vbab = MLOAD vba9(0x40)
    0xbad: vbad(0x60) = CONST 
    0xbaf: vbaf = ADD vbad(0x60), vbab
    0xbb0: vbb0(0x40) = CONST 
    0xbb2: MSTORE vbb0(0x40), vbaf
    0xbb4: vbb4(0x25) = CONST 
    0xbb7: MSTORE vbab, vbb4(0x25)
    0xbb8: vbb8(0x20) = CONST 
    0xbba: vbba = ADD vbb8(0x20), vbab
    0xbbb: vbbb(0x150e) = CONST 
    0xbbe: vbbe(0x25) = CONST 
    0xbc1: CODECOPY vbba, vbbb(0x150e), vbbe(0x25)
    0xbc2: vbc2(0x5) = CONST 
    0xbc4: vbc4(0x0) = CONST 
    0xbc6: vbc6(0xbcd) = CONST 
    0xbc9: vbc9(0xd18) = CONST 
    0xbcc: JUMP vbc9(0xd18)

    Begin block 0xd18B0xba3
    prev=[0xba3], succ=[0xbcd]
    =================================
    0xd19S0xba3: vd19Vba3 = CALLER 
    0xd1bS0xba3: JUMP vbc6(0xbcd)

    Begin block 0xbcd
    prev=[0xd18B0xba3], succ=[0x1a11]
    =================================
    0xbce: vbce(0x1) = CONST 
    0xbd0: vbd0(0x1) = CONST 
    0xbd2: vbd2(0xa0) = CONST 
    0xbd4: vbd4(0x10000000000000000000000000000000000000000) = SHL vbd2(0xa0), vbd0(0x1)
    0xbd5: vbd5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbd4(0x10000000000000000000000000000000000000000), vbce(0x1)
    0xbd8: vbd8 = AND vbd5(0xffffffffffffffffffffffffffffffffffffffff), vd19Vba3
    0xbda: MSTORE vbc4(0x0), vbd8
    0xbdb: vbdb(0x20) = CONST 
    0xbdf: vbdf(0x20) = ADD vbc4(0x0), vbdb(0x20)
    0xbe3: MSTORE vbdf(0x20), vbc2(0x5)
    0xbe4: vbe4(0x40) = CONST 
    0xbe8: vbe8(0x40) = ADD vbe4(0x40), vbc4(0x0)
    0xbe9: vbe9(0x0) = CONST 
    0xbed: vbed = SHA3 vbe9(0x0), vbe8(0x40)
    0xbf0: vbf0 = AND v511, vbd5(0xffffffffffffffffffffffffffffffffffffffff)
    0xbf2: MSTORE vbe9(0x0), vbf0
    0xbf4: MSTORE vbdb(0x20), vbed
    0xbf6: vbf6 = SHA3 vbe9(0x0), vbe4(0x40)
    0xbf7: vbf7 = SLOAD vbf6
    0xbfa: vbfa(0xffffffff) = CONST 
    0xbff: vbff(0xf71) = CONST 
    0xc02: vc02(0xf71) = AND vbff(0xf71), vbfa(0xffffffff)
    0xc03: vc03_0 = CALLPRIVATE vc02(0xf71), vbab, v516, vbf7, vba5(0x1a11)

    Begin block 0x1a11
    prev=[0xbcd], succ=[0x19e9]
    =================================
    0x1a12: v1a12(0xd1c) = CONST 
    0x1a15: CALLPRIVATE v1a12(0xd1c), vc03_0, v511, vd19Vb96, vb99(0x19e9)

    Begin block 0x19e9
    prev=[0x1a11], succ=[0x185e]
    =================================
    0x19eb: v19eb(0x1) = CONST 
    0x19f1: JUMP v4f0(0x185e)

    Begin block 0x185e
    prev=[0x19e9], succ=[]
    =================================
    0x185f: v185f(0x40) = CONST 
    0x1862: v1862 = MLOAD v185f(0x40)
    0x1864: v1864 = ISZERO v19eb(0x1)
    0x1865: v1865 = ISZERO v1864
    0x1867: MSTORE v1862, v1865
    0x1868: v1868 = MLOAD v185f(0x40)
    0x186c: v186c(0x0) = SUB v1862, v1868
    0x186d: v186d(0x20) = CONST 
    0x186f: v186f(0x20) = ADD v186d(0x20), v186c(0x0)
    0x1871: RETURN v1868, v186f(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x51b
    prev=[], succ=[0x52d, 0x531]
    =================================
    0x51c: v51c(0x1891) = CONST 
    0x51f: v51f(0x4) = CONST 
    0x522: v522 = CALLDATASIZE 
    0x523: v523 = SUB v522, v51f(0x4)
    0x524: v524(0x40) = CONST 
    0x527: v527 = LT v523, v524(0x40)
    0x528: v528 = ISZERO v527
    0x529: v529(0x531) = CONST 
    0x52c: JUMPI v529(0x531), v528

    Begin block 0x52d
    prev=[0x51b], succ=[]
    =================================
    0x52d: v52d(0x0) = CONST 
    0x530: REVERT v52d(0x0), v52d(0x0)

    Begin block 0x531
    prev=[0x51b], succ=[0xc04]
    =================================
    0x533: v533(0x1) = CONST 
    0x535: v535(0x1) = CONST 
    0x537: v537(0xa0) = CONST 
    0x539: v539(0x10000000000000000000000000000000000000000) = SHL v537(0xa0), v535(0x1)
    0x53a: v53a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v539(0x10000000000000000000000000000000000000000), v533(0x1)
    0x53c: v53c = CALLDATALOAD v51f(0x4)
    0x53d: v53d = AND v53c, v53a(0xffffffffffffffffffffffffffffffffffffffff)
    0x53f: v53f(0x20) = CONST 
    0x541: v541(0x24) = ADD v53f(0x20), v51f(0x4)
    0x542: v542 = CALLDATALOAD v541(0x24)
    0x543: v543(0xc04) = CONST 
    0x546: JUMP v543(0xc04)

    Begin block 0xc04
    prev=[0x531], succ=[0xd18B0xc04]
    =================================
    0xc05: vc05(0x0) = CONST 
    0xc07: vc07(0x1a35) = CONST 
    0xc0a: vc0a(0xc11) = CONST 
    0xc0d: vc0d(0xd18) = CONST 
    0xc10: JUMP vc0d(0xd18)

    Begin block 0xd18B0xc04
    prev=[0xc04], succ=[0xc11]
    =================================
    0xd19S0xc04: vd19Vc04 = CALLER 
    0xd1bS0xc04: JUMP vc0a(0xc11)

    Begin block 0xc11
    prev=[0xd18B0xc04], succ=[0x1a35]
    =================================
    0xc14: vc14(0xe08) = CONST 
    0xc17: vc17_0, vc17_1, vc17_2 = CALLPRIVATE vc14(0xe08), v542, v53d, vd19Vc04

    Begin block 0x1a35
    prev=[0xc11], succ=[0x1891]
    =================================
    0x1a37: v1a37(0x1) = CONST 
    0x1a3d: JUMP vc07(0x1a35)

    Begin block 0x1891
    prev=[0x1a35], succ=[]
    =================================
    0x1892: v1892(0x40) = CONST 
    0x1895: v1895 = MLOAD v1892(0x40)
    0x1897: v1897 = ISZERO v1a37(0x1)
    0x1898: v1898 = ISZERO v1897
    0x189a: MSTORE v1895, v1898
    0x189b: v189b = MLOAD v1892(0x40)
    0x189f: v189f(0x0) = SUB v1895, v189b
    0x18a0: v18a0(0x20) = CONST 
    0x18a2: v18a2(0x20) = ADD v18a0(0x20), v189f(0x0)
    0x18a4: RETURN v189b, v18a2(0x20)

}

function allowance(address,address)() public {
    Begin block 0x547
    prev=[], succ=[0x559, 0x55d]
    =================================
    0x548: v548(0x18c4) = CONST 
    0x54b: v54b(0x4) = CONST 
    0x54e: v54e = CALLDATASIZE 
    0x54f: v54f = SUB v54e, v54b(0x4)
    0x550: v550(0x40) = CONST 
    0x553: v553 = LT v54f, v550(0x40)
    0x554: v554 = ISZERO v553
    0x555: v555(0x55d) = CONST 
    0x558: JUMPI v555(0x55d), v554

    Begin block 0x559
    prev=[0x547], succ=[]
    =================================
    0x559: v559(0x0) = CONST 
    0x55c: REVERT v559(0x0), v559(0x0)

    Begin block 0x55d
    prev=[0x547], succ=[0xc18]
    =================================
    0x55f: v55f(0x1) = CONST 
    0x561: v561(0x1) = CONST 
    0x563: v563(0xa0) = CONST 
    0x565: v565(0x10000000000000000000000000000000000000000) = SHL v563(0xa0), v561(0x1)
    0x566: v566(0xffffffffffffffffffffffffffffffffffffffff) = SUB v565(0x10000000000000000000000000000000000000000), v55f(0x1)
    0x568: v568 = CALLDATALOAD v54b(0x4)
    0x56a: v56a = AND v566(0xffffffffffffffffffffffffffffffffffffffff), v568
    0x56c: v56c(0x20) = CONST 
    0x56e: v56e(0x24) = ADD v56c(0x20), v54b(0x4)
    0x56f: v56f = CALLDATALOAD v56e(0x24)
    0x570: v570 = AND v56f, v566(0xffffffffffffffffffffffffffffffffffffffff)
    0x571: v571(0xc18) = CONST 
    0x574: JUMP v571(0xc18)

    Begin block 0xc18
    prev=[0x55d], succ=[0x18c4]
    =================================
    0xc19: vc19(0x1) = CONST 
    0xc1b: vc1b(0x1) = CONST 
    0xc1d: vc1d(0xa0) = CONST 
    0xc1f: vc1f(0x10000000000000000000000000000000000000000) = SHL vc1d(0xa0), vc1b(0x1)
    0xc20: vc20(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc1f(0x10000000000000000000000000000000000000000), vc19(0x1)
    0xc23: vc23 = AND vc20(0xffffffffffffffffffffffffffffffffffffffff), v56a
    0xc24: vc24(0x0) = CONST 
    0xc28: MSTORE vc24(0x0), vc23
    0xc29: vc29(0x5) = CONST 
    0xc2b: vc2b(0x20) = CONST 
    0xc2f: MSTORE vc2b(0x20), vc29(0x5)
    0xc30: vc30(0x40) = CONST 
    0xc34: vc34 = SHA3 vc24(0x0), vc30(0x40)
    0xc38: vc38 = AND vc20(0xffffffffffffffffffffffffffffffffffffffff), v570
    0xc3a: MSTORE vc24(0x0), vc38
    0xc3e: MSTORE vc2b(0x20), vc34
    0xc3f: vc3f = SHA3 vc24(0x0), vc30(0x40)
    0xc40: vc40 = SLOAD vc3f
    0xc42: JUMP v548(0x18c4)

    Begin block 0x18c4
    prev=[0xc18], succ=[]
    =================================
    0x18c5: v18c5(0x40) = CONST 
    0x18c8: v18c8 = MLOAD v18c5(0x40)
    0x18cb: MSTORE v18c8, vc40
    0x18cc: v18cc = MLOAD v18c5(0x40)
    0x18d0: v18d0(0x0) = SUB v18c8, v18cc
    0x18d1: v18d1(0x20) = CONST 
    0x18d3: v18d3(0x20) = ADD v18d1(0x20), v18d0(0x0)
    0x18d5: RETURN v18cc, v18d3(0x20)

}

function pendingOwner()() public {
    Begin block 0x575
    prev=[], succ=[0xc43]
    =================================
    0x576: v576(0x18f5) = CONST 
    0x579: v579(0xc43) = CONST 
    0x57c: JUMP v579(0xc43)

    Begin block 0xc43
    prev=[0x575], succ=[0x18f5]
    =================================
    0xc44: vc44(0x1) = CONST 
    0xc46: vc46 = SLOAD vc44(0x1)
    0xc47: vc47(0x1) = CONST 
    0xc49: vc49(0x1) = CONST 
    0xc4b: vc4b(0xa0) = CONST 
    0xc4d: vc4d(0x10000000000000000000000000000000000000000) = SHL vc4b(0xa0), vc49(0x1)
    0xc4e: vc4e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc4d(0x10000000000000000000000000000000000000000), vc47(0x1)
    0xc4f: vc4f = AND vc4e(0xffffffffffffffffffffffffffffffffffffffff), vc46
    0xc51: JUMP v576(0x18f5)

    Begin block 0x18f5
    prev=[0xc43], succ=[]
    =================================
    0x18f6: v18f6(0x40) = CONST 
    0x18f9: v18f9 = MLOAD v18f6(0x40)
    0x18fa: v18fa(0x1) = CONST 
    0x18fc: v18fc(0x1) = CONST 
    0x18fe: v18fe(0xa0) = CONST 
    0x1900: v1900(0x10000000000000000000000000000000000000000) = SHL v18fe(0xa0), v18fc(0x1)
    0x1901: v1901(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1900(0x10000000000000000000000000000000000000000), v18fa(0x1)
    0x1904: v1904 = AND vc4f, v1901(0xffffffffffffffffffffffffffffffffffffffff)
    0x1906: MSTORE v18f9, v1904
    0x1907: v1907 = MLOAD v18f6(0x40)
    0x190b: v190b(0x0) = SUB v18f9, v1907
    0x190c: v190c(0x20) = CONST 
    0x190e: v190e(0x20) = ADD v190c(0x20), v190b(0x0)
    0x1910: RETURN v1907, v190e(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x57d
    prev=[], succ=[0x58f, 0x593]
    =================================
    0x57e: v57e(0x1930) = CONST 
    0x581: v581(0x4) = CONST 
    0x584: v584 = CALLDATASIZE 
    0x585: v585 = SUB v584, v581(0x4)
    0x586: v586(0x20) = CONST 
    0x589: v589 = LT v585, v586(0x20)
    0x58a: v58a = ISZERO v589
    0x58b: v58b(0x593) = CONST 
    0x58e: JUMPI v58b(0x593), v58a

    Begin block 0x58f
    prev=[0x57d], succ=[]
    =================================
    0x58f: v58f(0x0) = CONST 
    0x592: REVERT v58f(0x0), v58f(0x0)

    Begin block 0x593
    prev=[0x57d], succ=[0xc52]
    =================================
    0x595: v595 = CALLDATALOAD v581(0x4)
    0x596: v596(0x1) = CONST 
    0x598: v598(0x1) = CONST 
    0x59a: v59a(0xa0) = CONST 
    0x59c: v59c(0x10000000000000000000000000000000000000000) = SHL v59a(0xa0), v598(0x1)
    0x59d: v59d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v59c(0x10000000000000000000000000000000000000000), v596(0x1)
    0x59e: v59e = AND v59d(0xffffffffffffffffffffffffffffffffffffffff), v595
    0x59f: v59f(0xc52) = CONST 
    0x5a2: JUMP v59f(0xc52)

    Begin block 0xc52
    prev=[0x593], succ=[0xc65, 0xcb1]
    =================================
    0xc53: vc53(0x0) = CONST 
    0xc55: vc55 = SLOAD vc53(0x0)
    0xc56: vc56(0x1) = CONST 
    0xc58: vc58(0x1) = CONST 
    0xc5a: vc5a(0xa0) = CONST 
    0xc5c: vc5c(0x10000000000000000000000000000000000000000) = SHL vc5a(0xa0), vc58(0x1)
    0xc5d: vc5d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc5c(0x10000000000000000000000000000000000000000), vc56(0x1)
    0xc5e: vc5e = AND vc5d(0xffffffffffffffffffffffffffffffffffffffff), vc55
    0xc5f: vc5f = CALLER 
    0xc60: vc60 = EQ vc5f, vc5e
    0xc61: vc61(0xcb1) = CONST 
    0xc64: JUMPI vc61(0xcb1), vc60

    Begin block 0xc65
    prev=[0xc52], succ=[]
    =================================
    0xc65: vc65(0x40) = CONST 
    0xc68: vc68 = MLOAD vc65(0x40)
    0xc69: vc69(0x461bcd) = CONST 
    0xc6d: vc6d(0xe5) = CONST 
    0xc6f: vc6f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc6d(0xe5), vc69(0x461bcd)
    0xc71: MSTORE vc68, vc6f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc72: vc72(0x20) = CONST 
    0xc74: vc74(0x4) = CONST 
    0xc77: vc77 = ADD vc68, vc74(0x4)
    0xc7a: MSTORE vc77, vc72(0x20)
    0xc7b: vc7b(0x24) = CONST 
    0xc7e: vc7e = ADD vc68, vc7b(0x24)
    0xc7f: MSTORE vc7e, vc72(0x20)
    0xc80: vc80(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xca1: vca1(0x44) = CONST 
    0xca4: vca4 = ADD vc68, vca1(0x44)
    0xca5: MSTORE vca4, vc80(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xca7: vca7 = MLOAD vc65(0x40)
    0xcab: vcab(0x0) = SUB vc68, vca7
    0xcac: vcac(0x64) = CONST 
    0xcae: vcae(0x64) = ADD vcac(0x64), vcab(0x0)
    0xcb0: REVERT vca7, vcae(0x64)

    Begin block 0xcb1
    prev=[0xc52], succ=[0xcc0, 0xcf6]
    =================================
    0xcb2: vcb2(0x1) = CONST 
    0xcb4: vcb4(0x1) = CONST 
    0xcb6: vcb6(0xa0) = CONST 
    0xcb8: vcb8(0x10000000000000000000000000000000000000000) = SHL vcb6(0xa0), vcb4(0x1)
    0xcb9: vcb9(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcb8(0x10000000000000000000000000000000000000000), vcb2(0x1)
    0xcbb: vcbb = AND v59e, vcb9(0xffffffffffffffffffffffffffffffffffffffff)
    0xcbc: vcbc(0xcf6) = CONST 
    0xcbf: JUMPI vcbc(0xcf6), vcbb

    Begin block 0xcc0
    prev=[0xcb1], succ=[]
    =================================
    0xcc0: vcc0(0x40) = CONST 
    0xcc2: vcc2 = MLOAD vcc0(0x40)
    0xcc3: vcc3(0x461bcd) = CONST 
    0xcc7: vcc7(0xe5) = CONST 
    0xcc9: vcc9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vcc7(0xe5), vcc3(0x461bcd)
    0xccb: MSTORE vcc2, vcc9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xccc: vccc(0x4) = CONST 
    0xcce: vcce = ADD vccc(0x4), vcc2
    0xcd1: vcd1(0x20) = CONST 
    0xcd3: vcd3 = ADD vcd1(0x20), vcce
    0xcd6: vcd6(0x20) = SUB vcd3, vcce
    0xcd8: MSTORE vcce, vcd6(0x20)
    0xcd9: vcd9(0x26) = CONST 
    0xcdc: MSTORE vcd3, vcd9(0x26)
    0xcdd: vcdd(0x20) = CONST 
    0xcdf: vcdf = ADD vcdd(0x20), vcd3
    0xce1: vce1(0x13e6) = CONST 
    0xce4: vce4(0x26) = CONST 
    0xce7: CODECOPY vcdf, vce1(0x13e6), vce4(0x26)
    0xce8: vce8(0x40) = CONST 
    0xcea: vcea = ADD vce8(0x40), vcdf
    0xcee: vcee(0x40) = CONST 
    0xcf0: vcf0 = MLOAD vcee(0x40)
    0xcf3: vcf3(0x84) = SUB vcea, vcf0
    0xcf5: REVERT vcf0, vcf3(0x84)

    Begin block 0xcf6
    prev=[0xcb1], succ=[0x1930]
    =================================
    0xcf7: vcf7(0x1) = CONST 
    0xcfa: vcfa = SLOAD vcf7(0x1)
    0xcfb: vcfb(0x1) = CONST 
    0xcfd: vcfd(0x1) = CONST 
    0xcff: vcff(0xa0) = CONST 
    0xd01: vd01(0x10000000000000000000000000000000000000000) = SHL vcff(0xa0), vcfd(0x1)
    0xd02: vd02(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd01(0x10000000000000000000000000000000000000000), vcfb(0x1)
    0xd03: vd03(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vd02(0xffffffffffffffffffffffffffffffffffffffff)
    0xd04: vd04 = AND vd03(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vcfa
    0xd05: vd05(0x1) = CONST 
    0xd07: vd07(0x1) = CONST 
    0xd09: vd09(0xa0) = CONST 
    0xd0b: vd0b(0x10000000000000000000000000000000000000000) = SHL vd09(0xa0), vd07(0x1)
    0xd0c: vd0c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd0b(0x10000000000000000000000000000000000000000), vd05(0x1)
    0xd10: vd10 = AND vd0c(0xffffffffffffffffffffffffffffffffffffffff), v59e
    0xd14: vd14 = OR vd10, vd04
    0xd16: SSTORE vcf7(0x1), vd14
    0xd17: JUMP v57e(0x1930)

    Begin block 0x1930
    prev=[0xcf6], succ=[]
    =================================
    0x1931: STOP 

}

function 0xd1c(0xd1carg0x0, 0xd1carg0x1, 0xd1carg0x2, 0xd1carg0x3) private {
    Begin block 0xd1c
    prev=[], succ=[0xd2b, 0xd61]
    =================================
    0xd1d: vd1d(0x1) = CONST 
    0xd1f: vd1f(0x1) = CONST 
    0xd21: vd21(0xa0) = CONST 
    0xd23: vd23(0x10000000000000000000000000000000000000000) = SHL vd21(0xa0), vd1f(0x1)
    0xd24: vd24(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd23(0x10000000000000000000000000000000000000000), vd1d(0x1)
    0xd26: vd26 = AND vd1carg2, vd24(0xffffffffffffffffffffffffffffffffffffffff)
    0xd27: vd27(0xd61) = CONST 
    0xd2a: JUMPI vd27(0xd61), vd26

    Begin block 0xd2b
    prev=[0xd1c], succ=[]
    =================================
    0xd2b: vd2b(0x40) = CONST 
    0xd2d: vd2d = MLOAD vd2b(0x40)
    0xd2e: vd2e(0x461bcd) = CONST 
    0xd32: vd32(0xe5) = CONST 
    0xd34: vd34(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd32(0xe5), vd2e(0x461bcd)
    0xd36: MSTORE vd2d, vd34(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd37: vd37(0x4) = CONST 
    0xd39: vd39 = ADD vd37(0x4), vd2d
    0xd3c: vd3c(0x20) = CONST 
    0xd3e: vd3e = ADD vd3c(0x20), vd39
    0xd41: vd41(0x20) = SUB vd3e, vd39
    0xd43: MSTORE vd39, vd41(0x20)
    0xd44: vd44(0x24) = CONST 
    0xd47: MSTORE vd3e, vd44(0x24)
    0xd48: vd48(0x20) = CONST 
    0xd4a: vd4a = ADD vd48(0x20), vd3e
    0xd4c: vd4c(0x14ea) = CONST 
    0xd4f: vd4f(0x24) = CONST 
    0xd52: CODECOPY vd4a, vd4c(0x14ea), vd4f(0x24)
    0xd53: vd53(0x40) = CONST 
    0xd55: vd55 = ADD vd53(0x40), vd4a
    0xd59: vd59(0x40) = CONST 
    0xd5b: vd5b = MLOAD vd59(0x40)
    0xd5e: vd5e(0x84) = SUB vd55, vd5b
    0xd60: REVERT vd5b, vd5e(0x84)

    Begin block 0xd61
    prev=[0xd1c], succ=[0xd70, 0xda6]
    =================================
    0xd62: vd62(0x1) = CONST 
    0xd64: vd64(0x1) = CONST 
    0xd66: vd66(0xa0) = CONST 
    0xd68: vd68(0x10000000000000000000000000000000000000000) = SHL vd66(0xa0), vd64(0x1)
    0xd69: vd69(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd68(0x10000000000000000000000000000000000000000), vd62(0x1)
    0xd6b: vd6b = AND vd1carg1, vd69(0xffffffffffffffffffffffffffffffffffffffff)
    0xd6c: vd6c(0xda6) = CONST 
    0xd6f: JUMPI vd6c(0xda6), vd6b

    Begin block 0xd70
    prev=[0xd61], succ=[]
    =================================
    0xd70: vd70(0x40) = CONST 
    0xd72: vd72 = MLOAD vd70(0x40)
    0xd73: vd73(0x461bcd) = CONST 
    0xd77: vd77(0xe5) = CONST 
    0xd79: vd79(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd77(0xe5), vd73(0x461bcd)
    0xd7b: MSTORE vd72, vd79(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd7c: vd7c(0x4) = CONST 
    0xd7e: vd7e = ADD vd7c(0x4), vd72
    0xd81: vd81(0x20) = CONST 
    0xd83: vd83 = ADD vd81(0x20), vd7e
    0xd86: vd86(0x20) = SUB vd83, vd7e
    0xd88: MSTORE vd7e, vd86(0x20)
    0xd89: vd89(0x22) = CONST 
    0xd8c: MSTORE vd83, vd89(0x22)
    0xd8d: vd8d(0x20) = CONST 
    0xd8f: vd8f = ADD vd8d(0x20), vd83
    0xd91: vd91(0x140c) = CONST 
    0xd94: vd94(0x22) = CONST 
    0xd97: CODECOPY vd8f, vd91(0x140c), vd94(0x22)
    0xd98: vd98(0x40) = CONST 
    0xd9a: vd9a = ADD vd98(0x40), vd8f
    0xd9e: vd9e(0x40) = CONST 
    0xda0: vda0 = MLOAD vd9e(0x40)
    0xda3: vda3(0x84) = SUB vd9a, vda0
    0xda5: REVERT vda0, vda3(0x84)

    Begin block 0xda6
    prev=[0xd61], succ=[]
    =================================
    0xda7: vda7(0x1) = CONST 
    0xda9: vda9(0x1) = CONST 
    0xdab: vdab(0xa0) = CONST 
    0xdad: vdad(0x10000000000000000000000000000000000000000) = SHL vdab(0xa0), vda9(0x1)
    0xdae: vdae(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdad(0x10000000000000000000000000000000000000000), vda7(0x1)
    0xdb1: vdb1 = AND vd1carg2, vdae(0xffffffffffffffffffffffffffffffffffffffff)
    0xdb2: vdb2(0x0) = CONST 
    0xdb6: MSTORE vdb2(0x0), vdb1
    0xdb7: vdb7(0x5) = CONST 
    0xdb9: vdb9(0x20) = CONST 
    0xdbd: MSTORE vdb9(0x20), vdb7(0x5)
    0xdbe: vdbe(0x40) = CONST 
    0xdc2: vdc2 = SHA3 vdb2(0x0), vdbe(0x40)
    0xdc5: vdc5 = AND vd1carg1, vdae(0xffffffffffffffffffffffffffffffffffffffff)
    0xdc8: MSTORE vdb2(0x0), vdc5
    0xdcb: MSTORE vdb9(0x20), vdc2
    0xdcf: vdcf = SHA3 vdb2(0x0), vdbe(0x40)
    0xdd2: SSTORE vdcf, vd1carg0
    0xdd4: vdd4 = MLOAD vdbe(0x40)
    0xdd7: MSTORE vdd4, vd1carg0
    0xdd9: vdd9 = MLOAD vdbe(0x40)
    0xdda: vdda(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0xdfe: vdfe(0x0) = SUB vdd4, vdd9
    0xe01: ve01(0x20) = ADD vdb9(0x20), vdfe(0x0)
    0xe03: LOG3 vdd9, ve01(0x20), vdda(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), vdb1, vdc5
    0xe07: RETURNPRIVATE vd1carg3

}

function 0xe08(0xe08arg0x0, 0xe08arg0x1, 0xe08arg0x2) private {
    Begin block 0xe08
    prev=[], succ=[0xe17, 0xe4d]
    =================================
    0xe09: ve09(0x1) = CONST 
    0xe0b: ve0b(0x1) = CONST 
    0xe0d: ve0d(0xa0) = CONST 
    0xe0f: ve0f(0x10000000000000000000000000000000000000000) = SHL ve0d(0xa0), ve0b(0x1)
    0xe10: ve10(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve0f(0x10000000000000000000000000000000000000000), ve09(0x1)
    0xe12: ve12 = AND ve08arg2, ve10(0xffffffffffffffffffffffffffffffffffffffff)
    0xe13: ve13(0xe4d) = CONST 
    0xe16: JUMPI ve13(0xe4d), ve12

    Begin block 0xe17
    prev=[0xe08], succ=[]
    =================================
    0xe17: ve17(0x40) = CONST 
    0xe19: ve19 = MLOAD ve17(0x40)
    0xe1a: ve1a(0x461bcd) = CONST 
    0xe1e: ve1e(0xe5) = CONST 
    0xe20: ve20(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL ve1e(0xe5), ve1a(0x461bcd)
    0xe22: MSTORE ve19, ve20(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe23: ve23(0x4) = CONST 
    0xe25: ve25 = ADD ve23(0x4), ve19
    0xe28: ve28(0x20) = CONST 
    0xe2a: ve2a = ADD ve28(0x20), ve25
    0xe2d: ve2d(0x20) = SUB ve2a, ve25
    0xe2f: MSTORE ve25, ve2d(0x20)
    0xe30: ve30(0x25) = CONST 
    0xe33: MSTORE ve2a, ve30(0x25)
    0xe34: ve34(0x20) = CONST 
    0xe36: ve36 = ADD ve34(0x20), ve2a
    0xe38: ve38(0x14c5) = CONST 
    0xe3b: ve3b(0x25) = CONST 
    0xe3e: CODECOPY ve36, ve38(0x14c5), ve3b(0x25)
    0xe3f: ve3f(0x40) = CONST 
    0xe41: ve41 = ADD ve3f(0x40), ve36
    0xe45: ve45(0x40) = CONST 
    0xe47: ve47 = MLOAD ve45(0x40)
    0xe4a: ve4a(0x84) = SUB ve41, ve47
    0xe4c: REVERT ve47, ve4a(0x84)

    Begin block 0xe4d
    prev=[0xe08], succ=[0xe5c, 0xe92]
    =================================
    0xe4e: ve4e(0x1) = CONST 
    0xe50: ve50(0x1) = CONST 
    0xe52: ve52(0xa0) = CONST 
    0xe54: ve54(0x10000000000000000000000000000000000000000) = SHL ve52(0xa0), ve50(0x1)
    0xe55: ve55(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve54(0x10000000000000000000000000000000000000000), ve4e(0x1)
    0xe57: ve57 = AND ve08arg1, ve55(0xffffffffffffffffffffffffffffffffffffffff)
    0xe58: ve58(0xe92) = CONST 
    0xe5b: JUMPI ve58(0xe92), ve57

    Begin block 0xe5c
    prev=[0xe4d], succ=[]
    =================================
    0xe5c: ve5c(0x40) = CONST 
    0xe5e: ve5e = MLOAD ve5c(0x40)
    0xe5f: ve5f(0x461bcd) = CONST 
    0xe63: ve63(0xe5) = CONST 
    0xe65: ve65(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL ve63(0xe5), ve5f(0x461bcd)
    0xe67: MSTORE ve5e, ve65(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe68: ve68(0x4) = CONST 
    0xe6a: ve6a = ADD ve68(0x4), ve5e
    0xe6d: ve6d(0x20) = CONST 
    0xe6f: ve6f = ADD ve6d(0x20), ve6a
    0xe72: ve72(0x20) = SUB ve6f, ve6a
    0xe74: MSTORE ve6a, ve72(0x20)
    0xe75: ve75(0x23) = CONST 
    0xe78: MSTORE ve6f, ve75(0x23)
    0xe79: ve79(0x20) = CONST 
    0xe7b: ve7b = ADD ve79(0x20), ve6f
    0xe7d: ve7d(0x13a1) = CONST 
    0xe80: ve80(0x23) = CONST 
    0xe83: CODECOPY ve7b, ve7d(0x13a1), ve80(0x23)
    0xe84: ve84(0x40) = CONST 
    0xe86: ve86 = ADD ve84(0x40), ve7b
    0xe8a: ve8a(0x40) = CONST 
    0xe8c: ve8c = MLOAD ve8a(0x40)
    0xe8f: ve8f(0x84) = SUB ve86, ve8c
    0xe91: REVERT ve8c, ve8f(0x84)

    Begin block 0xe92
    prev=[0xe4d], succ=[0xe9d]
    =================================
    0xe93: ve93(0xe9d) = CONST 
    0xe99: ve99(0x126f) = CONST 
    0xe9c: ve9c_0, ve9c_1, ve9c_2 = CALLPRIVATE ve99(0x126f), ve08arg0, ve08arg1, ve08arg2

    Begin block 0xe9d
    prev=[0xe92], succ=[0xee0]
    =================================
    0xe9e: ve9e(0xee0) = CONST 
    0xea2: vea2(0x40) = CONST 
    0xea4: vea4 = MLOAD vea2(0x40)
    0xea6: vea6(0x60) = CONST 
    0xea8: vea8 = ADD vea6(0x60), vea4
    0xea9: vea9(0x40) = CONST 
    0xeab: MSTORE vea9(0x40), vea8
    0xead: vead(0x26) = CONST 
    0xeb0: MSTORE vea4, vead(0x26)
    0xeb1: veb1(0x20) = CONST 
    0xeb3: veb3 = ADD veb1(0x20), vea4
    0xeb4: veb4(0x142e) = CONST 
    0xeb7: veb7(0x26) = CONST 
    0xeba: CODECOPY veb3, veb4(0x142e), veb7(0x26)
    0xebb: vebb(0x1) = CONST 
    0xebd: vebd(0x1) = CONST 
    0xebf: vebf(0xa0) = CONST 
    0xec1: vec1(0x10000000000000000000000000000000000000000) = SHL vebf(0xa0), vebd(0x1)
    0xec2: vec2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vec1(0x10000000000000000000000000000000000000000), vebb(0x1)
    0xec4: vec4 = AND ve9c_2, vec2(0xffffffffffffffffffffffffffffffffffffffff)
    0xec5: vec5(0x0) = CONST 
    0xec9: MSTORE vec5(0x0), vec4
    0xeca: veca(0x4) = CONST 
    0xecc: vecc(0x20) = CONST 
    0xece: MSTORE vecc(0x20), veca(0x4)
    0xecf: vecf(0x40) = CONST 
    0xed2: ved2 = SHA3 vec5(0x0), vecf(0x40)
    0xed3: ved3 = SLOAD ved2
    0xed6: ved6(0xffffffff) = CONST 
    0xedb: vedb(0xf71) = CONST 
    0xede: vede(0xf71) = AND vedb(0xf71), ved6(0xffffffff)
    0xedf: vedf_0 = CALLPRIVATE vede(0xf71), vea4, ve9c_0, ved3, ve9e(0xee0)

    Begin block 0xee0
    prev=[0xe9d], succ=[0x1008B0xee0]
    =================================
    0xee1: vee1(0x1) = CONST 
    0xee3: vee3(0x1) = CONST 
    0xee5: vee5(0xa0) = CONST 
    0xee7: vee7(0x10000000000000000000000000000000000000000) = SHL vee5(0xa0), vee3(0x1)
    0xee8: vee8(0xffffffffffffffffffffffffffffffffffffffff) = SUB vee7(0x10000000000000000000000000000000000000000), vee1(0x1)
    0xeeb: veeb = AND ve9c_2, vee8(0xffffffffffffffffffffffffffffffffffffffff)
    0xeec: veec(0x0) = CONST 
    0xef0: MSTORE veec(0x0), veeb
    0xef1: vef1(0x4) = CONST 
    0xef3: vef3(0x20) = CONST 
    0xef5: MSTORE vef3(0x20), vef1(0x4)
    0xef6: vef6(0x40) = CONST 
    0xefa: vefa = SHA3 veec(0x0), vef6(0x40)
    0xefe: SSTORE vefa, vedf_0
    0xf01: vf01 = AND ve9c_1, vee8(0xffffffffffffffffffffffffffffffffffffffff)
    0xf03: MSTORE veec(0x0), vf01
    0xf04: vf04 = SHA3 veec(0x0), vef6(0x40)
    0xf05: vf05 = SLOAD vf04
    0xf06: vf06(0xf15) = CONST 
    0xf0b: vf0b(0xffffffff) = CONST 
    0xf10: vf10(0x1008) = CONST 
    0xf13: vf13(0x1008) = AND vf10(0x1008), vf0b(0xffffffff)
    0xf14: JUMP vf13(0x1008)

    Begin block 0x1008B0xee0
    prev=[0xee0], succ=[0x1016B0xee0, 0x1a5dB0xee0]
    =================================
    0x1009S0xee0: v1009Vee0(0x0) = CONST 
    0x100dS0xee0: v100dVee0 = ADD ve9c_0, vf05
    0x1010S0xee0: v1010Vee0 = LT v100dVee0, vf05
    0x1011S0xee0: v1011Vee0 = ISZERO v1010Vee0
    0x1012S0xee0: v1012Vee0(0x1a5d) = CONST 
    0x1015S0xee0: JUMPI v1012Vee0(0x1a5d), v1011Vee0

    Begin block 0x1016B0xee0
    prev=[0x1008B0xee0], succ=[]
    =================================
    0x1016S0xee0: v1016Vee0(0x40) = CONST 
    0x1019S0xee0: v1019Vee0 = MLOAD v1016Vee0(0x40)
    0x101aS0xee0: v101aVee0(0x461bcd) = CONST 
    0x101eS0xee0: v101eVee0(0xe5) = CONST 
    0x1020S0xee0: v1020Vee0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v101eVee0(0xe5), v101aVee0(0x461bcd)
    0x1022S0xee0: MSTORE v1019Vee0, v1020Vee0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1023S0xee0: v1023Vee0(0x20) = CONST 
    0x1025S0xee0: v1025Vee0(0x4) = CONST 
    0x1028S0xee0: v1028Vee0 = ADD v1019Vee0, v1025Vee0(0x4)
    0x1029S0xee0: MSTORE v1028Vee0, v1023Vee0(0x20)
    0x102aS0xee0: v102aVee0(0x1b) = CONST 
    0x102cS0xee0: v102cVee0(0x24) = CONST 
    0x102fS0xee0: v102fVee0 = ADD v1019Vee0, v102cVee0(0x24)
    0x1030S0xee0: MSTORE v102fVee0, v102aVee0(0x1b)
    0x1031S0xee0: v1031Vee0(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x1052S0xee0: v1052Vee0(0x44) = CONST 
    0x1055S0xee0: v1055Vee0 = ADD v1019Vee0, v1052Vee0(0x44)
    0x1056S0xee0: MSTORE v1055Vee0, v1031Vee0(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x1058S0xee0: v1058Vee0 = MLOAD v1016Vee0(0x40)
    0x105cS0xee0: v105cVee0(0x0) = SUB v1019Vee0, v1058Vee0
    0x105dS0xee0: v105dVee0(0x64) = CONST 
    0x105fS0xee0: v105fVee0(0x64) = ADD v105dVee0(0x64), v105cVee0(0x0)
    0x1061S0xee0: REVERT v1058Vee0, v105fVee0(0x64)

    Begin block 0x1a5dB0xee0
    prev=[0x1008B0xee0], succ=[0xf15]
    =================================
    0x1a63S0xee0: JUMP vf06(0xf15)

    Begin block 0xf15
    prev=[0x1a5dB0xee0], succ=[]
    =================================
    0xf16: vf16(0x1) = CONST 
    0xf18: vf18(0x1) = CONST 
    0xf1a: vf1a(0xa0) = CONST 
    0xf1c: vf1c(0x10000000000000000000000000000000000000000) = SHL vf1a(0xa0), vf18(0x1)
    0xf1d: vf1d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf1c(0x10000000000000000000000000000000000000000), vf16(0x1)
    0xf20: vf20 = AND ve9c_1, vf1d(0xffffffffffffffffffffffffffffffffffffffff)
    0xf21: vf21(0x0) = CONST 
    0xf25: MSTORE vf21(0x0), vf20
    0xf26: vf26(0x4) = CONST 
    0xf28: vf28(0x20) = CONST 
    0xf2c: MSTORE vf28(0x20), vf26(0x4)
    0xf2d: vf2d(0x40) = CONST 
    0xf32: vf32 = SHA3 vf21(0x0), vf2d(0x40)
    0xf36: SSTORE vf32, v100dVee0
    0xf38: vf38 = MLOAD vf2d(0x40)
    0xf3b: MSTORE vf38, ve9c_0
    0xf3d: vf3d = MLOAD vf2d(0x40)
    0xf42: vf42 = AND ve9c_2, vf1d(0xffffffffffffffffffffffffffffffffffffffff)
    0xf44: vf44(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0xf69: vf69(0x0) = SUB vf38, vf3d
    0xf6a: vf6a(0x20) = ADD vf69(0x0), vf28(0x20)
    0xf6c: LOG3 vf3d, vf6a(0x20), vf44(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), vf42, vf20
    0xf70: RETURNPRIVATE ve93(0xe9d), ve08arg0, ve08arg1, ve08arg2

}

function 0xf71(0xf71arg0x0, 0xf71arg0x1, 0xf71arg0x2, 0xf71arg0x3) private {
    Begin block 0xf71
    prev=[], succ=[0xf7d, 0x1000]
    =================================
    0xf72: vf72(0x0) = CONST 
    0xf77: vf77 = GT vf71arg1, vf71arg2
    0xf78: vf78 = ISZERO vf77
    0xf79: vf79(0x1000) = CONST 
    0xf7c: JUMPI vf79(0x1000), vf78

    Begin block 0xf7d
    prev=[0xf71], succ=[0xfad]
    =================================
    0xf7d: vf7d(0x40) = CONST 
    0xf7f: vf7f = MLOAD vf7d(0x40)
    0xf80: vf80(0x461bcd) = CONST 
    0xf84: vf84(0xe5) = CONST 
    0xf86: vf86(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf84(0xe5), vf80(0x461bcd)
    0xf88: MSTORE vf7f, vf86(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf89: vf89(0x4) = CONST 
    0xf8b: vf8b = ADD vf89(0x4), vf7f
    0xf8e: vf8e(0x20) = CONST 
    0xf90: vf90 = ADD vf8e(0x20), vf8b
    0xf93: vf93(0x20) = SUB vf90, vf8b
    0xf95: MSTORE vf8b, vf93(0x20)
    0xf99: vf99 = MLOAD vf71arg0
    0xf9b: MSTORE vf90, vf99
    0xf9c: vf9c(0x20) = CONST 
    0xf9e: vf9e = ADD vf9c(0x20), vf90
    0xfa2: vfa2 = MLOAD vf71arg0
    0xfa4: vfa4(0x20) = CONST 
    0xfa6: vfa6 = ADD vfa4(0x20), vf71arg0
    0xfab: vfab(0x0) = CONST 

    Begin block 0xfad
    prev=[0xf7d, 0xfb6], succ=[0xfc5, 0xfb6]
    =================================
    0xfad_0x0: vfad_0 = PHI vfab(0x0), vfc0
    0xfb0: vfb0 = LT vfad_0, vfa2
    0xfb1: vfb1 = ISZERO vfb0
    0xfb2: vfb2(0xfc5) = CONST 
    0xfb5: JUMPI vfb2(0xfc5), vfb1

    Begin block 0xfc5
    prev=[0xfad], succ=[0xff2, 0xfd9]
    =================================
    0xfce: vfce = ADD vfa2, vf9e
    0xfd0: vfd0(0x1f) = CONST 
    0xfd2: vfd2 = AND vfd0(0x1f), vfa2
    0xfd4: vfd4 = ISZERO vfd2
    0xfd5: vfd5(0xff2) = CONST 
    0xfd8: JUMPI vfd5(0xff2), vfd4

    Begin block 0xff2
    prev=[0xfc5, 0xfd9], succ=[]
    =================================
    0xff2_0x1: vff2_1 = PHI vfce, vfef
    0xff8: vff8(0x40) = CONST 
    0xffa: vffa = MLOAD vff8(0x40)
    0xffd: vffd = SUB vff2_1, vffa
    0xfff: REVERT vffa, vffd

    Begin block 0xfd9
    prev=[0xfc5], succ=[0xff2]
    =================================
    0xfdb: vfdb = SUB vfce, vfd2
    0xfdd: vfdd = MLOAD vfdb
    0xfde: vfde(0x1) = CONST 
    0xfe1: vfe1(0x20) = CONST 
    0xfe3: vfe3 = SUB vfe1(0x20), vfd2
    0xfe4: vfe4(0x100) = CONST 
    0xfe7: vfe7 = EXP vfe4(0x100), vfe3
    0xfe8: vfe8 = SUB vfe7, vfde(0x1)
    0xfe9: vfe9 = NOT vfe8
    0xfea: vfea = AND vfe9, vfdd
    0xfec: MSTORE vfdb, vfea
    0xfed: vfed(0x20) = CONST 
    0xfef: vfef = ADD vfed(0x20), vfdb

    Begin block 0xfb6
    prev=[0xfad], succ=[0xfad]
    =================================
    0xfb6_0x0: vfb6_0 = PHI vfab(0x0), vfc0
    0xfb8: vfb8 = ADD vfb6_0, vfa6
    0xfb9: vfb9 = MLOAD vfb8
    0xfbc: vfbc = ADD vfb6_0, vf9e
    0xfbd: MSTORE vfbc, vfb9
    0xfbe: vfbe(0x20) = CONST 
    0xfc0: vfc0 = ADD vfbe(0x20), vfb6_0
    0xfc1: vfc1(0xfad) = CONST 
    0xfc4: JUMP vfc1(0xfad)

    Begin block 0x1000
    prev=[0xf71], succ=[]
    =================================
    0x1005: v1005 = SUB vf71arg2, vf71arg1
    0x1007: RETURNPRIVATE vf71arg3, v1005

}

