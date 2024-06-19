function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8d7]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x8b9: v8b9(0x8d7) = CONST 
    0x8ba: JUMPI v8b9(0x8d7), v8

    Begin block 0xd
    prev=[0x0], succ=[0x7f, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x7b103999) = CONST 
    0x19: v19 = GT v14(0x7b103999), v12
    0x1a: v1a(0x7f) = CONST 
    0x1d: JUMPI v1a(0x7f), v19

    Begin block 0x7f
    prev=[0xd], succ=[0xbb, 0x8b]
    =================================
    0x81: v81(0x4555d5c9) = CONST 
    0x86: v86 = GT v81(0x4555d5c9), v12
    0x87: v87(0xbb) = CONST 
    0x8a: JUMPI v87(0xbb), v86

    Begin block 0xbb
    prev=[0x7f], succ=[0x8da, 0xc7]
    =================================
    0xbd: vbd(0x1a5da6c8) = CONST 
    0xc2: vc2 = EQ vbd(0x1a5da6c8), v12
    0x8d1: v8d1(0x8da) = CONST 
    0x8d2: JUMPI v8d1(0x8da), vc2

    Begin block 0x8da
    prev=[0xbb], succ=[]
    =================================
    0x8db: v8db(0x121) = CONST 
    0x8dc: CALLPRIVATE v8db(0x121)

    Begin block 0xc7
    prev=[0xbb], succ=[0x8dd, 0xd2]
    =================================
    0xc8: vc8(0x2dfdf0b5) = CONST 
    0xcd: vcd = EQ vc8(0x2dfdf0b5), v12
    0x8d3: v8d3(0x8dd) = CONST 
    0x8d4: JUMPI v8d3(0x8dd), vcd

    Begin block 0x8dd
    prev=[0xc7], succ=[]
    =================================
    0x8de: v8de(0x156) = CONST 
    0x8df: CALLPRIVATE v8de(0x156)

    Begin block 0xd2
    prev=[0xc7], succ=[0x8d7, 0x8e0]
    =================================
    0xd3: vd3(0x3f4ba83a) = CONST 
    0xd8: vd8 = EQ vd3(0x3f4ba83a), v12
    0x8d5: v8d5(0x8e0) = CONST 
    0x8d6: JUMPI v8d5(0x8e0), vd8

    Begin block 0x8d7
    prev=[0x0, 0xd2], succ=[]
    =================================
    0x8d8: v8d8(0xdd) = CONST 
    0x8d9: CALLPRIVATE v8d8(0xdd)

    Begin block 0x8e0
    prev=[0xd2], succ=[]
    =================================
    0x8e1: v8e1(0x17d) = CONST 
    0x8e2: CALLPRIVATE v8e1(0x17d)

    Begin block 0x8b
    prev=[0x7f], succ=[0x8e3, 0x96]
    =================================
    0x8c: v8c(0x4555d5c9) = CONST 
    0x91: v91 = EQ v8c(0x4555d5c9), v12
    0x8c9: v8c9(0x8e3) = CONST 
    0x8ca: JUMPI v8c9(0x8e3), v91

    Begin block 0x8e3
    prev=[0x8b], succ=[]
    =================================
    0x8e4: v8e4(0x192) = CONST 
    0x8e5: CALLPRIVATE v8e4(0x192)

    Begin block 0x96
    prev=[0x8b], succ=[0x8e6, 0xa1]
    =================================
    0x97: v97(0x5c60da1b) = CONST 
    0x9c: v9c = EQ v97(0x5c60da1b), v12
    0x8cb: v8cb(0x8e6) = CONST 
    0x8cc: JUMPI v8cb(0x8e6), v9c

    Begin block 0x8e6
    prev=[0x96], succ=[]
    =================================
    0x8e7: v8e7(0x1a7) = CONST 
    0x8e8: CALLPRIVATE v8e7(0x1a7)

    Begin block 0xa1
    prev=[0x96], succ=[0x8e9, 0xac]
    =================================
    0xa2: va2(0x5c975abb) = CONST 
    0xa7: va7 = EQ va2(0x5c975abb), v12
    0x8cd: v8cd(0x8e9) = CONST 
    0x8ce: JUMPI v8cd(0x8e9), va7

    Begin block 0x8e9
    prev=[0xa1], succ=[]
    =================================
    0x8ea: v8ea(0x1d8) = CONST 
    0x8eb: CALLPRIVATE v8ea(0x1d8)

    Begin block 0xac
    prev=[0xa1], succ=[0xb7, 0x8ec]
    =================================
    0xad: vad(0x5cc07076) = CONST 
    0xb2: vb2 = EQ vad(0x5cc07076), v12
    0x8cf: v8cf(0x8ec) = CONST 
    0x8d0: JUMPI v8cf(0x8ec), vb2

    Begin block 0xb7
    prev=[0xac], succ=[]
    =================================
    0xb7: vb7(0xdd) = CONST 
    0xba: JUMP vb7(0xdd)

    Begin block 0x8ec
    prev=[0xac], succ=[]
    =================================
    0x8ed: v8ed(0x201) = CONST 
    0x8ee: CALLPRIVATE v8ed(0x201)

    Begin block 0x1e
    prev=[0xd], succ=[0x59, 0x29]
    =================================
    0x1f: v1f(0x9a202d47) = CONST 
    0x24: v24 = GT v1f(0x9a202d47), v12
    0x25: v25(0x59) = CONST 
    0x28: JUMPI v25(0x59), v24

    Begin block 0x59
    prev=[0x1e], succ=[0x8ef, 0x65]
    =================================
    0x5b: v5b(0x7b103999) = CONST 
    0x60: v60 = EQ v5b(0x7b103999), v12
    0x8c3: v8c3(0x8ef) = CONST 
    0x8c4: JUMPI v8c3(0x8ef), v60

    Begin block 0x8ef
    prev=[0x59], succ=[]
    =================================
    0x8f0: v8f0(0x255) = CONST 
    0x8f1: CALLPRIVATE v8f0(0x255)

    Begin block 0x65
    prev=[0x59], succ=[0x8f2, 0x70]
    =================================
    0x66: v66(0x8456cb59) = CONST 
    0x6b: v6b = EQ v66(0x8456cb59), v12
    0x8c5: v8c5(0x8f2) = CONST 
    0x8c6: JUMPI v8c5(0x8f2), v6b

    Begin block 0x8f2
    prev=[0x65], succ=[]
    =================================
    0x8f3: v8f3(0x26a) = CONST 
    0x8f4: CALLPRIVATE v8f3(0x26a)

    Begin block 0x70
    prev=[0x65], succ=[0x7b, 0x8f5]
    =================================
    0x71: v71(0x8f283970) = CONST 
    0x76: v76 = EQ v71(0x8f283970), v12
    0x8c7: v8c7(0x8f5) = CONST 
    0x8c8: JUMPI v8c7(0x8f5), v76

    Begin block 0x7b
    prev=[0x70], succ=[]
    =================================
    0x7b: v7b(0xdd) = CONST 
    0x7e: JUMP v7b(0xdd)

    Begin block 0x8f5
    prev=[0x70], succ=[]
    =================================
    0x8f6: v8f6(0x27f) = CONST 
    0x8f7: CALLPRIVATE v8f6(0x27f)

    Begin block 0x29
    prev=[0x1e], succ=[0x8f8, 0x34]
    =================================
    0x2a: v2a(0x9a202d47) = CONST 
    0x2f: v2f = EQ v2a(0x9a202d47), v12
    0x8bb: v8bb(0x8f8) = CONST 
    0x8bc: JUMPI v8bb(0x8f8), v2f

    Begin block 0x8f8
    prev=[0x29], succ=[]
    =================================
    0x8f9: v8f9(0x2b2) = CONST 
    0x8fa: CALLPRIVATE v8f9(0x2b2)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x8fb]
    =================================
    0x35: v35(0xb02c43d0) = CONST 
    0x3a: v3a = EQ v35(0xb02c43d0), v12
    0x8bd: v8bd(0x8fb) = CONST 
    0x8be: JUMPI v8bd(0x8fb), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x8fe, 0x4a]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x8bf: v8bf(0x8fe) = CONST 
    0x8c0: JUMPI v8bf(0x8fe), v45

    Begin block 0x8fe
    prev=[0x3f], succ=[]
    =================================
    0x8ff: v8ff(0x331) = CONST 
    0x900: CALLPRIVATE v8ff(0x331)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0x901]
    =================================
    0x4b: v4b(0xfd840de2) = CONST 
    0x50: v50 = EQ v4b(0xfd840de2), v12
    0x8c1: v8c1(0x901) = CONST 
    0x8c2: JUMPI v8c1(0x901), v50

    Begin block 0x55
    prev=[0x4a], succ=[]
    =================================
    0x55: v55(0xdd) = CONST 
    0x58: JUMP v55(0xdd)

    Begin block 0x901
    prev=[0x4a], succ=[]
    =================================
    0x902: v902(0x346) = CONST 
    0x903: CALLPRIVATE v902(0x346)

    Begin block 0x8fb
    prev=[0x34], succ=[]
    =================================
    0x8fc: v8fc(0x2c7) = CONST 
    0x8fd: CALLPRIVATE v8fc(0x2c7)

}

function updateRegistry(address)() public {
    Begin block 0x121
    prev=[], succ=[0x129, 0x12d]
    =================================
    0x122: v122 = CALLVALUE 
    0x124: v124 = ISZERO v122
    0x125: v125(0x12d) = CONST 
    0x128: JUMPI v125(0x12d), v124

    Begin block 0x129
    prev=[0x121], succ=[]
    =================================
    0x129: v129(0x0) = CONST 
    0x12c: REVERT v129(0x0), v129(0x0)

    Begin block 0x12d
    prev=[0x121], succ=[0x140, 0x144]
    =================================
    0x12f: v12f(0x6ff) = CONST 
    0x132: v132(0x4) = CONST 
    0x135: v135 = CALLDATASIZE 
    0x136: v136 = SUB v135, v132(0x4)
    0x137: v137(0x20) = CONST 
    0x13a: v13a = LT v136, v137(0x20)
    0x13b: v13b = ISZERO v13a
    0x13c: v13c(0x144) = CONST 
    0x13f: JUMPI v13c(0x144), v13b

    Begin block 0x140
    prev=[0x12d], succ=[]
    =================================
    0x140: v140(0x0) = CONST 
    0x143: REVERT v140(0x0), v140(0x0)

    Begin block 0x144
    prev=[0x12d], succ=[0x388]
    =================================
    0x146: v146 = CALLDATALOAD v132(0x4)
    0x147: v147(0x1) = CONST 
    0x149: v149(0x1) = CONST 
    0x14b: v14b(0xa0) = CONST 
    0x14d: v14d(0x10000000000000000000000000000000000000000) = SHL v14b(0xa0), v149(0x1)
    0x14e: v14e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14d(0x10000000000000000000000000000000000000000), v147(0x1)
    0x14f: v14f = AND v14e(0xffffffffffffffffffffffffffffffffffffffff), v146
    0x150: v150(0x388) = CONST 
    0x153: JUMP v150(0x388)

    Begin block 0x388
    prev=[0x144], succ=[0x39b, 0x39f]
    =================================
    0x389: v389(0x0) = CONST 
    0x38b: v38b = SLOAD v389(0x0)
    0x38c: v38c(0x1) = CONST 
    0x38e: v38e(0x1) = CONST 
    0x390: v390(0xa0) = CONST 
    0x392: v392(0x10000000000000000000000000000000000000000) = SHL v390(0xa0), v38e(0x1)
    0x393: v393(0xffffffffffffffffffffffffffffffffffffffff) = SUB v392(0x10000000000000000000000000000000000000000), v38c(0x1)
    0x394: v394 = AND v393(0xffffffffffffffffffffffffffffffffffffffff), v38b
    0x395: v395 = CALLER 
    0x396: v396 = EQ v395, v394
    0x397: v397(0x39f) = CONST 
    0x39a: JUMPI v397(0x39f), v396

    Begin block 0x39b
    prev=[0x388], succ=[]
    =================================
    0x39b: v39b(0x0) = CONST 
    0x39e: REVERT v39b(0x0), v39b(0x0)

    Begin block 0x39f
    prev=[0x388], succ=[0x6ff]
    =================================
    0x3a0: v3a0(0x2) = CONST 
    0x3a3: v3a3 = SLOAD v3a0(0x2)
    0x3a4: v3a4(0x1) = CONST 
    0x3a6: v3a6(0x1) = CONST 
    0x3a8: v3a8(0xa0) = CONST 
    0x3aa: v3aa(0x10000000000000000000000000000000000000000) = SHL v3a8(0xa0), v3a6(0x1)
    0x3ab: v3ab(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3aa(0x10000000000000000000000000000000000000000), v3a4(0x1)
    0x3ac: v3ac(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3ab(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ad: v3ad = AND v3ac(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v3a3
    0x3ae: v3ae(0x1) = CONST 
    0x3b0: v3b0(0x1) = CONST 
    0x3b2: v3b2(0xa0) = CONST 
    0x3b4: v3b4(0x10000000000000000000000000000000000000000) = SHL v3b2(0xa0), v3b0(0x1)
    0x3b5: v3b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b4(0x10000000000000000000000000000000000000000), v3ae(0x1)
    0x3b9: v3b9 = AND v3b5(0xffffffffffffffffffffffffffffffffffffffff), v14f
    0x3bd: v3bd = OR v3b9, v3ad
    0x3bf: SSTORE v3a0(0x2), v3bd
    0x3c0: JUMP v12f(0x6ff)

    Begin block 0x6ff
    prev=[0x39f], succ=[]
    =================================
    0x700: STOP 

}

function depositCount()() public {
    Begin block 0x156
    prev=[], succ=[0x15e, 0x162]
    =================================
    0x157: v157 = CALLVALUE 
    0x159: v159 = ISZERO v157
    0x15a: v15a(0x162) = CONST 
    0x15d: JUMPI v15a(0x162), v159

    Begin block 0x15e
    prev=[0x156], succ=[]
    =================================
    0x15e: v15e(0x0) = CONST 
    0x161: REVERT v15e(0x0), v15e(0x0)

    Begin block 0x162
    prev=[0x156], succ=[0x3c1]
    =================================
    0x164: v164(0x720) = CONST 
    0x167: v167(0x3c1) = CONST 
    0x16a: JUMP v167(0x3c1)

    Begin block 0x3c1
    prev=[0x162], succ=[0x720]
    =================================
    0x3c2: v3c2(0x3) = CONST 
    0x3c4: v3c4 = SLOAD v3c2(0x3)
    0x3c6: JUMP v164(0x720)

    Begin block 0x720
    prev=[0x3c1], succ=[]
    =================================
    0x721: v721(0x40) = CONST 
    0x724: v724 = MLOAD v721(0x40)
    0x727: MSTORE v724, v3c4
    0x728: v728 = MLOAD v721(0x40)
    0x72c: v72c(0x0) = SUB v724, v728
    0x72d: v72d(0x20) = CONST 
    0x72f: v72f(0x20) = ADD v72d(0x20), v72c(0x0)
    0x731: RETURN v728, v72f(0x20)

}

function unpause()() public {
    Begin block 0x17d
    prev=[], succ=[0x185, 0x189]
    =================================
    0x17e: v17e = CALLVALUE 
    0x180: v180 = ISZERO v17e
    0x181: v181(0x189) = CONST 
    0x184: JUMPI v181(0x189), v180

    Begin block 0x185
    prev=[0x17d], succ=[]
    =================================
    0x185: v185(0x0) = CONST 
    0x188: REVERT v185(0x0), v185(0x0)

    Begin block 0x189
    prev=[0x17d], succ=[0x3c7]
    =================================
    0x18b: v18b(0x751) = CONST 
    0x18e: v18e(0x3c7) = CONST 
    0x191: JUMP v18e(0x3c7)

    Begin block 0x3c7
    prev=[0x189], succ=[0x3da, 0x3de]
    =================================
    0x3c8: v3c8(0x0) = CONST 
    0x3ca: v3ca = SLOAD v3c8(0x0)
    0x3cb: v3cb(0x1) = CONST 
    0x3cd: v3cd(0x1) = CONST 
    0x3cf: v3cf(0xa0) = CONST 
    0x3d1: v3d1(0x10000000000000000000000000000000000000000) = SHL v3cf(0xa0), v3cd(0x1)
    0x3d2: v3d2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d1(0x10000000000000000000000000000000000000000), v3cb(0x1)
    0x3d3: v3d3 = AND v3d2(0xffffffffffffffffffffffffffffffffffffffff), v3ca
    0x3d4: v3d4 = CALLER 
    0x3d5: v3d5 = EQ v3d4, v3d3
    0x3d6: v3d6(0x3de) = CONST 
    0x3d9: JUMPI v3d6(0x3de), v3d5

    Begin block 0x3da
    prev=[0x3c7], succ=[]
    =================================
    0x3da: v3da(0x0) = CONST 
    0x3dd: REVERT v3da(0x0), v3da(0x0)

    Begin block 0x3de
    prev=[0x3c7], succ=[0x3f0, 0x3f4]
    =================================
    0x3df: v3df(0x1) = CONST 
    0x3e1: v3e1 = SLOAD v3df(0x1)
    0x3e2: v3e2(0x1) = CONST 
    0x3e4: v3e4(0xa0) = CONST 
    0x3e6: v3e6(0x10000000000000000000000000000000000000000) = SHL v3e4(0xa0), v3e2(0x1)
    0x3e8: v3e8 = DIV v3e1, v3e6(0x10000000000000000000000000000000000000000)
    0x3e9: v3e9(0xff) = CONST 
    0x3eb: v3eb = AND v3e9(0xff), v3e8
    0x3ec: v3ec(0x3f4) = CONST 
    0x3ef: JUMPI v3ec(0x3f4), v3eb

    Begin block 0x3f0
    prev=[0x3de], succ=[]
    =================================
    0x3f0: v3f0(0x0) = CONST 
    0x3f3: REVERT v3f0(0x0), v3f0(0x0)

    Begin block 0x3f4
    prev=[0x3de], succ=[0x751]
    =================================
    0x3f5: v3f5(0x1) = CONST 
    0x3f8: v3f8 = SLOAD v3f5(0x1)
    0x3f9: v3f9(0xff) = CONST 
    0x3fb: v3fb(0xa0) = CONST 
    0x3fd: v3fd(0xff0000000000000000000000000000000000000000) = SHL v3fb(0xa0), v3f9(0xff)
    0x3fe: v3fe(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v3fd(0xff0000000000000000000000000000000000000000)
    0x3ff: v3ff = AND v3fe(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v3f8
    0x401: SSTORE v3f5(0x1), v3ff
    0x402: v402(0x40) = CONST 
    0x404: v404 = MLOAD v402(0x40)
    0x405: v405(0xa45f47fdea8a1efdd9029a5691c7f759c32b7c698632b563573e155625d16933) = CONST 
    0x427: v427(0x0) = CONST 
    0x42a: LOG1 v404, v427(0x0), v405(0xa45f47fdea8a1efdd9029a5691c7f759c32b7c698632b563573e155625d16933)
    0x42b: JUMP v18b(0x751)

    Begin block 0x751
    prev=[0x3f4], succ=[]
    =================================
    0x752: STOP 

}

function proxyType()() public {
    Begin block 0x192
    prev=[], succ=[0x19a, 0x19e]
    =================================
    0x193: v193 = CALLVALUE 
    0x195: v195 = ISZERO v193
    0x196: v196(0x19e) = CONST 
    0x199: JUMPI v196(0x19e), v195

    Begin block 0x19a
    prev=[0x192], succ=[]
    =================================
    0x19a: v19a(0x0) = CONST 
    0x19d: REVERT v19a(0x0), v19a(0x0)

    Begin block 0x19e
    prev=[0x192], succ=[0x42c]
    =================================
    0x1a0: v1a0(0x772) = CONST 
    0x1a3: v1a3(0x42c) = CONST 
    0x1a6: JUMP v1a3(0x42c)

    Begin block 0x42c
    prev=[0x19e], succ=[0x772]
    =================================
    0x42d: v42d(0x2) = CONST 
    0x430: JUMP v1a0(0x772)

    Begin block 0x772
    prev=[0x42c], succ=[]
    =================================
    0x773: v773(0x40) = CONST 
    0x776: v776 = MLOAD v773(0x40)
    0x779: MSTORE v776, v42d(0x2)
    0x77a: v77a = MLOAD v773(0x40)
    0x77e: v77e(0x0) = SUB v776, v77a
    0x77f: v77f(0x20) = CONST 
    0x781: v781(0x20) = ADD v77f(0x20), v77e(0x0)
    0x783: RETURN v77a, v781(0x20)

}

function implementation()() public {
    Begin block 0x1a7
    prev=[], succ=[0x1af, 0x1b3]
    =================================
    0x1a8: v1a8 = CALLVALUE 
    0x1aa: v1aa = ISZERO v1a8
    0x1ab: v1ab(0x1b3) = CONST 
    0x1ae: JUMPI v1ab(0x1b3), v1aa

    Begin block 0x1af
    prev=[0x1a7], succ=[]
    =================================
    0x1af: v1af(0x0) = CONST 
    0x1b2: REVERT v1af(0x0), v1af(0x0)

    Begin block 0x1b3
    prev=[0x1a7], succ=[0x379B0x1b3]
    =================================
    0x1b5: v1b5(0x7a3) = CONST 
    0x1b8: v1b8(0x379) = CONST 
    0x1bb: JUMP v1b8(0x379)

    Begin block 0x379B0x1b3
    prev=[0x1b3], succ=[0x7a3]
    =================================
    0x37aS0x1b3: v37aV1b3(0x1) = CONST 
    0x37cS0x1b3: v37cV1b3 = SLOAD v37aV1b3(0x1)
    0x37dS0x1b3: v37dV1b3(0x1) = CONST 
    0x37fS0x1b3: v37fV1b3(0x1) = CONST 
    0x381S0x1b3: v381V1b3(0xa0) = CONST 
    0x383S0x1b3: v383V1b3(0x10000000000000000000000000000000000000000) = SHL v381V1b3(0xa0), v37fV1b3(0x1)
    0x384S0x1b3: v384V1b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v383V1b3(0x10000000000000000000000000000000000000000), v37dV1b3(0x1)
    0x385S0x1b3: v385V1b3 = AND v384V1b3(0xffffffffffffffffffffffffffffffffffffffff), v37cV1b3
    0x387S0x1b3: JUMP v1b5(0x7a3)

    Begin block 0x7a3
    prev=[0x379B0x1b3], succ=[]
    =================================
    0x7a4: v7a4(0x40) = CONST 
    0x7a7: v7a7 = MLOAD v7a4(0x40)
    0x7a8: v7a8(0x1) = CONST 
    0x7aa: v7aa(0x1) = CONST 
    0x7ac: v7ac(0xa0) = CONST 
    0x7ae: v7ae(0x10000000000000000000000000000000000000000) = SHL v7ac(0xa0), v7aa(0x1)
    0x7af: v7af(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7ae(0x10000000000000000000000000000000000000000), v7a8(0x1)
    0x7b2: v7b2 = AND v385V1b3, v7af(0xffffffffffffffffffffffffffffffffffffffff)
    0x7b4: MSTORE v7a7, v7b2
    0x7b5: v7b5 = MLOAD v7a4(0x40)
    0x7b9: v7b9(0x0) = SUB v7a7, v7b5
    0x7ba: v7ba(0x20) = CONST 
    0x7bc: v7bc(0x20) = ADD v7ba(0x20), v7b9(0x0)
    0x7be: RETURN v7b5, v7bc(0x20)

}

function paused()() public {
    Begin block 0x1d8
    prev=[], succ=[0x1e0, 0x1e4]
    =================================
    0x1d9: v1d9 = CALLVALUE 
    0x1db: v1db = ISZERO v1d9
    0x1dc: v1dc(0x1e4) = CONST 
    0x1df: JUMPI v1dc(0x1e4), v1db

    Begin block 0x1e0
    prev=[0x1d8], succ=[]
    =================================
    0x1e0: v1e0(0x0) = CONST 
    0x1e3: REVERT v1e0(0x0), v1e0(0x0)

    Begin block 0x1e4
    prev=[0x1d8], succ=[0x431]
    =================================
    0x1e6: v1e6(0x1ed) = CONST 
    0x1e9: v1e9(0x431) = CONST 
    0x1ec: JUMP v1e9(0x431)

    Begin block 0x431
    prev=[0x1e4], succ=[0x1ed]
    =================================
    0x432: v432(0x1) = CONST 
    0x434: v434 = SLOAD v432(0x1)
    0x435: v435(0x1) = CONST 
    0x437: v437(0xa0) = CONST 
    0x439: v439(0x10000000000000000000000000000000000000000) = SHL v437(0xa0), v435(0x1)
    0x43b: v43b = DIV v434, v439(0x10000000000000000000000000000000000000000)
    0x43c: v43c(0xff) = CONST 
    0x43e: v43e = AND v43c(0xff), v43b
    0x440: JUMP v1e6(0x1ed)

    Begin block 0x1ed
    prev=[0x431], succ=[]
    =================================
    0x1ee: v1ee(0x40) = CONST 
    0x1f1: v1f1 = MLOAD v1ee(0x40)
    0x1f3: v1f3 = ISZERO v43e
    0x1f4: v1f4 = ISZERO v1f3
    0x1f6: MSTORE v1f1, v1f4
    0x1f7: v1f7 = MLOAD v1ee(0x40)
    0x1fb: v1fb(0x0) = SUB v1f1, v1f7
    0x1fc: v1fc(0x20) = CONST 
    0x1fe: v1fe(0x20) = ADD v1fc(0x20), v1fb(0x0)
    0x200: RETURN v1f7, v1fe(0x20)

}

function withdrawals(uint256)() public {
    Begin block 0x201
    prev=[], succ=[0x209, 0x20d]
    =================================
    0x202: v202 = CALLVALUE 
    0x204: v204 = ISZERO v202
    0x205: v205(0x20d) = CONST 
    0x208: JUMPI v205(0x20d), v204

    Begin block 0x209
    prev=[0x201], succ=[]
    =================================
    0x209: v209(0x0) = CONST 
    0x20c: REVERT v209(0x0), v209(0x0)

    Begin block 0x20d
    prev=[0x201], succ=[0x220, 0x224]
    =================================
    0x20f: v20f(0x22b) = CONST 
    0x212: v212(0x4) = CONST 
    0x215: v215 = CALLDATASIZE 
    0x216: v216 = SUB v215, v212(0x4)
    0x217: v217(0x20) = CONST 
    0x21a: v21a = LT v216, v217(0x20)
    0x21b: v21b = ISZERO v21a
    0x21c: v21c(0x224) = CONST 
    0x21f: JUMPI v21c(0x224), v21b

    Begin block 0x220
    prev=[0x20d], succ=[]
    =================================
    0x220: v220(0x0) = CONST 
    0x223: REVERT v220(0x0), v220(0x0)

    Begin block 0x224
    prev=[0x20d], succ=[0x441]
    =================================
    0x226: v226 = CALLDATALOAD v212(0x4)
    0x227: v227(0x441) = CONST 
    0x22a: JUMP v227(0x441)

    Begin block 0x441
    prev=[0x224], succ=[0x22b]
    =================================
    0x442: v442(0x5) = CONST 
    0x444: v444(0x20) = CONST 
    0x446: MSTORE v444(0x20), v442(0x5)
    0x447: v447(0x0) = CONST 
    0x44b: MSTORE v447(0x0), v226
    0x44c: v44c(0x40) = CONST 
    0x44f: v44f = SHA3 v447(0x0), v44c(0x40)
    0x451: v451 = SLOAD v44f
    0x452: v452(0x1) = CONST 
    0x455: v455 = ADD v44f, v452(0x1)
    0x456: v456 = SLOAD v455
    0x457: v457(0x2) = CONST 
    0x45b: v45b = ADD v44f, v457(0x2)
    0x45c: v45c = SLOAD v45b
    0x45d: v45d(0x1) = CONST 
    0x45f: v45f(0x1) = CONST 
    0x461: v461(0xa0) = CONST 
    0x463: v463(0x10000000000000000000000000000000000000000) = SHL v461(0xa0), v45f(0x1)
    0x464: v464(0xffffffffffffffffffffffffffffffffffffffff) = SUB v463(0x10000000000000000000000000000000000000000), v45d(0x1)
    0x467: v467 = AND v464(0xffffffffffffffffffffffffffffffffffffffff), v451
    0x46b: v46b = AND v464(0xffffffffffffffffffffffffffffffffffffffff), v456
    0x46e: JUMP v20f(0x22b)

    Begin block 0x22b
    prev=[0x441], succ=[]
    =================================
    0x22c: v22c(0x40) = CONST 
    0x22f: v22f = MLOAD v22c(0x40)
    0x230: v230(0x1) = CONST 
    0x232: v232(0x1) = CONST 
    0x234: v234(0xa0) = CONST 
    0x236: v236(0x10000000000000000000000000000000000000000) = SHL v234(0xa0), v232(0x1)
    0x237: v237(0xffffffffffffffffffffffffffffffffffffffff) = SUB v236(0x10000000000000000000000000000000000000000), v230(0x1)
    0x23a: v23a = AND v237(0xffffffffffffffffffffffffffffffffffffffff), v467
    0x23c: MSTORE v22f, v23a
    0x240: v240 = AND v237(0xffffffffffffffffffffffffffffffffffffffff), v46b
    0x241: v241(0x20) = CONST 
    0x244: v244 = ADD v22f, v241(0x20)
    0x245: MSTORE v244, v240
    0x248: v248 = ADD v22c(0x40), v22f
    0x249: MSTORE v248, v45c
    0x24b: v24b = MLOAD v22c(0x40)
    0x24f: v24f(0x0) = SUB v22f, v24b
    0x250: v250(0x60) = CONST 
    0x252: v252(0x60) = ADD v250(0x60), v24f(0x0)
    0x254: RETURN v24b, v252(0x60)

}

function registry()() public {
    Begin block 0x255
    prev=[], succ=[0x25d, 0x261]
    =================================
    0x256: v256 = CALLVALUE 
    0x258: v258 = ISZERO v256
    0x259: v259(0x261) = CONST 
    0x25c: JUMPI v259(0x261), v258

    Begin block 0x25d
    prev=[0x255], succ=[]
    =================================
    0x25d: v25d(0x0) = CONST 
    0x260: REVERT v25d(0x0), v25d(0x0)

    Begin block 0x261
    prev=[0x255], succ=[0x46f]
    =================================
    0x263: v263(0x7de) = CONST 
    0x266: v266(0x46f) = CONST 
    0x269: JUMP v266(0x46f)

    Begin block 0x46f
    prev=[0x261], succ=[0x7de]
    =================================
    0x470: v470(0x2) = CONST 
    0x472: v472 = SLOAD v470(0x2)
    0x473: v473(0x1) = CONST 
    0x475: v475(0x1) = CONST 
    0x477: v477(0xa0) = CONST 
    0x479: v479(0x10000000000000000000000000000000000000000) = SHL v477(0xa0), v475(0x1)
    0x47a: v47a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v479(0x10000000000000000000000000000000000000000), v473(0x1)
    0x47b: v47b = AND v47a(0xffffffffffffffffffffffffffffffffffffffff), v472
    0x47d: JUMP v263(0x7de)

    Begin block 0x7de
    prev=[0x46f], succ=[]
    =================================
    0x7df: v7df(0x40) = CONST 
    0x7e2: v7e2 = MLOAD v7df(0x40)
    0x7e3: v7e3(0x1) = CONST 
    0x7e5: v7e5(0x1) = CONST 
    0x7e7: v7e7(0xa0) = CONST 
    0x7e9: v7e9(0x10000000000000000000000000000000000000000) = SHL v7e7(0xa0), v7e5(0x1)
    0x7ea: v7ea(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7e9(0x10000000000000000000000000000000000000000), v7e3(0x1)
    0x7ed: v7ed = AND v47b, v7ea(0xffffffffffffffffffffffffffffffffffffffff)
    0x7ef: MSTORE v7e2, v7ed
    0x7f0: v7f0 = MLOAD v7df(0x40)
    0x7f4: v7f4(0x0) = SUB v7e2, v7f0
    0x7f5: v7f5(0x20) = CONST 
    0x7f7: v7f7(0x20) = ADD v7f5(0x20), v7f4(0x0)
    0x7f9: RETURN v7f0, v7f7(0x20)

}

function pause()() public {
    Begin block 0x26a
    prev=[], succ=[0x272, 0x276]
    =================================
    0x26b: v26b = CALLVALUE 
    0x26d: v26d = ISZERO v26b
    0x26e: v26e(0x276) = CONST 
    0x271: JUMPI v26e(0x276), v26d

    Begin block 0x272
    prev=[0x26a], succ=[]
    =================================
    0x272: v272(0x0) = CONST 
    0x275: REVERT v272(0x0), v272(0x0)

    Begin block 0x276
    prev=[0x26a], succ=[0x47e]
    =================================
    0x278: v278(0x819) = CONST 
    0x27b: v27b(0x47e) = CONST 
    0x27e: JUMP v27b(0x47e)

    Begin block 0x47e
    prev=[0x276], succ=[0x491, 0x495]
    =================================
    0x47f: v47f(0x0) = CONST 
    0x481: v481 = SLOAD v47f(0x0)
    0x482: v482(0x1) = CONST 
    0x484: v484(0x1) = CONST 
    0x486: v486(0xa0) = CONST 
    0x488: v488(0x10000000000000000000000000000000000000000) = SHL v486(0xa0), v484(0x1)
    0x489: v489(0xffffffffffffffffffffffffffffffffffffffff) = SUB v488(0x10000000000000000000000000000000000000000), v482(0x1)
    0x48a: v48a = AND v489(0xffffffffffffffffffffffffffffffffffffffff), v481
    0x48b: v48b = CALLER 
    0x48c: v48c = EQ v48b, v48a
    0x48d: v48d(0x495) = CONST 
    0x490: JUMPI v48d(0x495), v48c

    Begin block 0x491
    prev=[0x47e], succ=[]
    =================================
    0x491: v491(0x0) = CONST 
    0x494: REVERT v491(0x0), v491(0x0)

    Begin block 0x495
    prev=[0x47e], succ=[0x4a8, 0x4ac]
    =================================
    0x496: v496(0x1) = CONST 
    0x498: v498 = SLOAD v496(0x1)
    0x499: v499(0x1) = CONST 
    0x49b: v49b(0xa0) = CONST 
    0x49d: v49d(0x10000000000000000000000000000000000000000) = SHL v49b(0xa0), v499(0x1)
    0x49f: v49f = DIV v498, v49d(0x10000000000000000000000000000000000000000)
    0x4a0: v4a0(0xff) = CONST 
    0x4a2: v4a2 = AND v4a0(0xff), v49f
    0x4a3: v4a3 = ISZERO v4a2
    0x4a4: v4a4(0x4ac) = CONST 
    0x4a7: JUMPI v4a4(0x4ac), v4a3

    Begin block 0x4a8
    prev=[0x495], succ=[]
    =================================
    0x4a8: v4a8(0x0) = CONST 
    0x4ab: REVERT v4a8(0x0), v4a8(0x0)

    Begin block 0x4ac
    prev=[0x495], succ=[0x819]
    =================================
    0x4ad: v4ad(0x1) = CONST 
    0x4b0: v4b0 = SLOAD v4ad(0x1)
    0x4b1: v4b1(0xff) = CONST 
    0x4b3: v4b3(0xa0) = CONST 
    0x4b5: v4b5(0xff0000000000000000000000000000000000000000) = SHL v4b3(0xa0), v4b1(0xff)
    0x4b6: v4b6(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v4b5(0xff0000000000000000000000000000000000000000)
    0x4b7: v4b7 = AND v4b6(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v4b0
    0x4b8: v4b8(0x1) = CONST 
    0x4ba: v4ba(0xa0) = CONST 
    0x4bc: v4bc(0x10000000000000000000000000000000000000000) = SHL v4ba(0xa0), v4b8(0x1)
    0x4bd: v4bd = OR v4bc(0x10000000000000000000000000000000000000000), v4b7
    0x4bf: SSTORE v4ad(0x1), v4bd
    0x4c0: v4c0(0x40) = CONST 
    0x4c2: v4c2 = MLOAD v4c0(0x40)
    0x4c3: v4c3(0x9e87fac88ff661f02d44f95383c817fece4bce600a3dab7a54406878b965e752) = CONST 
    0x4e5: v4e5(0x0) = CONST 
    0x4e8: LOG1 v4c2, v4e5(0x0), v4c3(0x9e87fac88ff661f02d44f95383c817fece4bce600a3dab7a54406878b965e752)
    0x4e9: JUMP v278(0x819)

    Begin block 0x819
    prev=[0x4ac], succ=[]
    =================================
    0x81a: STOP 

}

function changeAdmin(address)() public {
    Begin block 0x27f
    prev=[], succ=[0x287, 0x28b]
    =================================
    0x280: v280 = CALLVALUE 
    0x282: v282 = ISZERO v280
    0x283: v283(0x28b) = CONST 
    0x286: JUMPI v283(0x28b), v282

    Begin block 0x287
    prev=[0x27f], succ=[]
    =================================
    0x287: v287(0x0) = CONST 
    0x28a: REVERT v287(0x0), v287(0x0)

    Begin block 0x28b
    prev=[0x27f], succ=[0x29e, 0x2a2]
    =================================
    0x28d: v28d(0x83a) = CONST 
    0x290: v290(0x4) = CONST 
    0x293: v293 = CALLDATASIZE 
    0x294: v294 = SUB v293, v290(0x4)
    0x295: v295(0x20) = CONST 
    0x298: v298 = LT v294, v295(0x20)
    0x299: v299 = ISZERO v298
    0x29a: v29a(0x2a2) = CONST 
    0x29d: JUMPI v29a(0x2a2), v299

    Begin block 0x29e
    prev=[0x28b], succ=[]
    =================================
    0x29e: v29e(0x0) = CONST 
    0x2a1: REVERT v29e(0x0), v29e(0x0)

    Begin block 0x2a2
    prev=[0x28b], succ=[0x4ea]
    =================================
    0x2a4: v2a4 = CALLDATALOAD v290(0x4)
    0x2a5: v2a5(0x1) = CONST 
    0x2a7: v2a7(0x1) = CONST 
    0x2a9: v2a9(0xa0) = CONST 
    0x2ab: v2ab(0x10000000000000000000000000000000000000000) = SHL v2a9(0xa0), v2a7(0x1)
    0x2ac: v2ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ab(0x10000000000000000000000000000000000000000), v2a5(0x1)
    0x2ad: v2ad = AND v2ac(0xffffffffffffffffffffffffffffffffffffffff), v2a4
    0x2ae: v2ae(0x4ea) = CONST 
    0x2b1: JUMP v2ae(0x4ea)

    Begin block 0x4ea
    prev=[0x2a2], succ=[0x4fd, 0x501]
    =================================
    0x4eb: v4eb(0x0) = CONST 
    0x4ed: v4ed = SLOAD v4eb(0x0)
    0x4ee: v4ee(0x1) = CONST 
    0x4f0: v4f0(0x1) = CONST 
    0x4f2: v4f2(0xa0) = CONST 
    0x4f4: v4f4(0x10000000000000000000000000000000000000000) = SHL v4f2(0xa0), v4f0(0x1)
    0x4f5: v4f5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f4(0x10000000000000000000000000000000000000000), v4ee(0x1)
    0x4f6: v4f6 = AND v4f5(0xffffffffffffffffffffffffffffffffffffffff), v4ed
    0x4f7: v4f7 = CALLER 
    0x4f8: v4f8 = EQ v4f7, v4f6
    0x4f9: v4f9(0x501) = CONST 
    0x4fc: JUMPI v4f9(0x501), v4f8

    Begin block 0x4fd
    prev=[0x4ea], succ=[]
    =================================
    0x4fd: v4fd(0x0) = CONST 
    0x500: REVERT v4fd(0x0), v4fd(0x0)

    Begin block 0x501
    prev=[0x4ea], succ=[0x510, 0x514]
    =================================
    0x502: v502(0x1) = CONST 
    0x504: v504(0x1) = CONST 
    0x506: v506(0xa0) = CONST 
    0x508: v508(0x10000000000000000000000000000000000000000) = SHL v506(0xa0), v504(0x1)
    0x509: v509(0xffffffffffffffffffffffffffffffffffffffff) = SUB v508(0x10000000000000000000000000000000000000000), v502(0x1)
    0x50b: v50b = AND v2ad, v509(0xffffffffffffffffffffffffffffffffffffffff)
    0x50c: v50c(0x514) = CONST 
    0x50f: JUMPI v50c(0x514), v50b

    Begin block 0x510
    prev=[0x501], succ=[]
    =================================
    0x510: v510(0x0) = CONST 
    0x513: REVERT v510(0x0), v510(0x0)

    Begin block 0x514
    prev=[0x501], succ=[0x83a]
    =================================
    0x515: v515(0x0) = CONST 
    0x518: v518 = SLOAD v515(0x0)
    0x519: v519(0x40) = CONST 
    0x51b: v51b = MLOAD v519(0x40)
    0x51c: v51c(0x1) = CONST 
    0x51e: v51e(0x1) = CONST 
    0x520: v520(0xa0) = CONST 
    0x522: v522(0x10000000000000000000000000000000000000000) = SHL v520(0xa0), v51e(0x1)
    0x523: v523(0xffffffffffffffffffffffffffffffffffffffff) = SUB v522(0x10000000000000000000000000000000000000000), v51c(0x1)
    0x526: v526 = AND v2ad, v523(0xffffffffffffffffffffffffffffffffffffffff)
    0x529: v529 = AND v518, v523(0xffffffffffffffffffffffffffffffffffffffff)
    0x52b: v52b(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x54d: LOG3 v51b, v515(0x0), v52b(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f), v529, v526
    0x54e: v54e(0x0) = CONST 
    0x551: v551 = SLOAD v54e(0x0)
    0x552: v552(0x1) = CONST 
    0x554: v554(0x1) = CONST 
    0x556: v556(0xa0) = CONST 
    0x558: v558(0x10000000000000000000000000000000000000000) = SHL v556(0xa0), v554(0x1)
    0x559: v559(0xffffffffffffffffffffffffffffffffffffffff) = SUB v558(0x10000000000000000000000000000000000000000), v552(0x1)
    0x55a: v55a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v559(0xffffffffffffffffffffffffffffffffffffffff)
    0x55b: v55b = AND v55a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v551
    0x55c: v55c(0x1) = CONST 
    0x55e: v55e(0x1) = CONST 
    0x560: v560(0xa0) = CONST 
    0x562: v562(0x10000000000000000000000000000000000000000) = SHL v560(0xa0), v55e(0x1)
    0x563: v563(0xffffffffffffffffffffffffffffffffffffffff) = SUB v562(0x10000000000000000000000000000000000000000), v55c(0x1)
    0x567: v567 = AND v563(0xffffffffffffffffffffffffffffffffffffffff), v2ad
    0x56b: v56b = OR v567, v55b
    0x56d: SSTORE v54e(0x0), v56b
    0x56e: JUMP v28d(0x83a)

    Begin block 0x83a
    prev=[0x514], succ=[]
    =================================
    0x83b: STOP 

}

function removeAdmin()() public {
    Begin block 0x2b2
    prev=[], succ=[0x2ba, 0x2be]
    =================================
    0x2b3: v2b3 = CALLVALUE 
    0x2b5: v2b5 = ISZERO v2b3
    0x2b6: v2b6(0x2be) = CONST 
    0x2b9: JUMPI v2b6(0x2be), v2b5

    Begin block 0x2ba
    prev=[0x2b2], succ=[]
    =================================
    0x2ba: v2ba(0x0) = CONST 
    0x2bd: REVERT v2ba(0x0), v2ba(0x0)

    Begin block 0x2be
    prev=[0x2b2], succ=[0x56f]
    =================================
    0x2c0: v2c0(0x85b) = CONST 
    0x2c3: v2c3(0x56f) = CONST 
    0x2c6: JUMP v2c3(0x56f)

    Begin block 0x56f
    prev=[0x2be], succ=[0x582, 0x586]
    =================================
    0x570: v570(0x0) = CONST 
    0x572: v572 = SLOAD v570(0x0)
    0x573: v573(0x1) = CONST 
    0x575: v575(0x1) = CONST 
    0x577: v577(0xa0) = CONST 
    0x579: v579(0x10000000000000000000000000000000000000000) = SHL v577(0xa0), v575(0x1)
    0x57a: v57a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v579(0x10000000000000000000000000000000000000000), v573(0x1)
    0x57b: v57b = AND v57a(0xffffffffffffffffffffffffffffffffffffffff), v572
    0x57c: v57c = CALLER 
    0x57d: v57d = EQ v57c, v57b
    0x57e: v57e(0x586) = CONST 
    0x581: JUMPI v57e(0x586), v57d

    Begin block 0x582
    prev=[0x56f], succ=[]
    =================================
    0x582: v582(0x0) = CONST 
    0x585: REVERT v582(0x0), v582(0x0)

    Begin block 0x586
    prev=[0x56f], succ=[0x85b]
    =================================
    0x587: v587(0x0) = CONST 
    0x58a: v58a = SLOAD v587(0x0)
    0x58b: v58b(0x40) = CONST 
    0x58d: v58d = MLOAD v58b(0x40)
    0x58e: v58e(0x1) = CONST 
    0x590: v590(0x1) = CONST 
    0x592: v592(0xa0) = CONST 
    0x594: v594(0x10000000000000000000000000000000000000000) = SHL v592(0xa0), v590(0x1)
    0x595: v595(0xffffffffffffffffffffffffffffffffffffffff) = SUB v594(0x10000000000000000000000000000000000000000), v58e(0x1)
    0x598: v598 = AND v58a, v595(0xffffffffffffffffffffffffffffffffffffffff)
    0x59a: v59a(0xa3b62bc36326052d97ea62d63c3d60308ed4c3ea8ac079dd8499f1e9c4f80c0f) = CONST 
    0x5bc: LOG2 v58d, v587(0x0), v59a(0xa3b62bc36326052d97ea62d63c3d60308ed4c3ea8ac079dd8499f1e9c4f80c0f), v598
    0x5bd: v5bd(0x0) = CONST 
    0x5c0: v5c0 = SLOAD v5bd(0x0)
    0x5c1: v5c1(0x1) = CONST 
    0x5c3: v5c3(0x1) = CONST 
    0x5c5: v5c5(0xa0) = CONST 
    0x5c7: v5c7(0x10000000000000000000000000000000000000000) = SHL v5c5(0xa0), v5c3(0x1)
    0x5c8: v5c8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c7(0x10000000000000000000000000000000000000000), v5c1(0x1)
    0x5c9: v5c9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5c8(0xffffffffffffffffffffffffffffffffffffffff)
    0x5ca: v5ca = AND v5c9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5c0
    0x5cc: SSTORE v5bd(0x0), v5ca
    0x5cd: JUMP v2c0(0x85b)

    Begin block 0x85b
    prev=[0x586], succ=[]
    =================================
    0x85c: STOP 

}

function deposits(uint256)() public {
    Begin block 0x2c7
    prev=[], succ=[0x2cf, 0x2d3]
    =================================
    0x2c8: v2c8 = CALLVALUE 
    0x2ca: v2ca = ISZERO v2c8
    0x2cb: v2cb(0x2d3) = CONST 
    0x2ce: JUMPI v2cb(0x2d3), v2ca

    Begin block 0x2cf
    prev=[0x2c7], succ=[]
    =================================
    0x2cf: v2cf(0x0) = CONST 
    0x2d2: REVERT v2cf(0x0), v2cf(0x0)

    Begin block 0x2d3
    prev=[0x2c7], succ=[0x2e6, 0x2ea]
    =================================
    0x2d5: v2d5(0x2f1) = CONST 
    0x2d8: v2d8(0x4) = CONST 
    0x2db: v2db = CALLDATASIZE 
    0x2dc: v2dc = SUB v2db, v2d8(0x4)
    0x2dd: v2dd(0x20) = CONST 
    0x2e0: v2e0 = LT v2dc, v2dd(0x20)
    0x2e1: v2e1 = ISZERO v2e0
    0x2e2: v2e2(0x2ea) = CONST 
    0x2e5: JUMPI v2e2(0x2ea), v2e1

    Begin block 0x2e6
    prev=[0x2d3], succ=[]
    =================================
    0x2e6: v2e6(0x0) = CONST 
    0x2e9: REVERT v2e6(0x0), v2e6(0x0)

    Begin block 0x2ea
    prev=[0x2d3], succ=[0x5ce]
    =================================
    0x2ec: v2ec = CALLDATALOAD v2d8(0x4)
    0x2ed: v2ed(0x5ce) = CONST 
    0x2f0: JUMP v2ed(0x5ce)

    Begin block 0x5ce
    prev=[0x2ea], succ=[0x5da, 0x5db]
    =================================
    0x5cf: v5cf(0x4) = CONST 
    0x5d3: v5d3 = SLOAD v5cf(0x4)
    0x5d5: v5d5 = LT v2ec, v5d3
    0x5d6: v5d6(0x5db) = CONST 
    0x5d9: JUMPI v5d6(0x5db), v5d5

    Begin block 0x5da
    prev=[0x5ce], succ=[]
    =================================
    0x5da: THROW 

    Begin block 0x5db
    prev=[0x5ce], succ=[0x2f1]
    =================================
    0x5dc: v5dc(0x0) = CONST 
    0x5e0: MSTORE v5dc(0x0), v5cf(0x4)
    0x5e1: v5e1(0x20) = CONST 
    0x5e5: v5e5 = SHA3 v5dc(0x0), v5e1(0x20)
    0x5e6: v5e6(0x4) = CONST 
    0x5ea: v5ea = MUL v2ec, v5e6(0x4)
    0x5eb: v5eb = ADD v5ea, v5e5
    0x5ed: v5ed = SLOAD v5eb
    0x5ee: v5ee(0x1) = CONST 
    0x5f1: v5f1 = ADD v5eb, v5ee(0x1)
    0x5f2: v5f2 = SLOAD v5f1
    0x5f3: v5f3(0x2) = CONST 
    0x5f6: v5f6 = ADD v5eb, v5f3(0x2)
    0x5f7: v5f7 = SLOAD v5f6
    0x5f8: v5f8(0x3) = CONST 
    0x5fc: v5fc = ADD v5eb, v5f8(0x3)
    0x5fd: v5fd = SLOAD v5fc
    0x5fe: v5fe(0x1) = CONST 
    0x600: v600(0x1) = CONST 
    0x602: v602(0xa0) = CONST 
    0x604: v604(0x10000000000000000000000000000000000000000) = SHL v602(0xa0), v600(0x1)
    0x605: v605(0xffffffffffffffffffffffffffffffffffffffff) = SUB v604(0x10000000000000000000000000000000000000000), v5fe(0x1)
    0x608: v608 = AND v605(0xffffffffffffffffffffffffffffffffffffffff), v5ed
    0x60d: v60d = AND v605(0xffffffffffffffffffffffffffffffffffffffff), v5f2
    0x611: v611 = AND v5f7, v605(0xffffffffffffffffffffffffffffffffffffffff)
    0x613: v613(0x1) = CONST 
    0x615: v615(0xa0) = CONST 
    0x617: v617(0x10000000000000000000000000000000000000000) = SHL v615(0xa0), v613(0x1)
    0x619: v619 = DIV v5f7, v617(0x10000000000000000000000000000000000000000)
    0x61a: v61a(0xffffffff) = CONST 
    0x61f: v61f = AND v61a(0xffffffff), v619
    0x622: JUMP v2d5(0x2f1)

    Begin block 0x2f1
    prev=[0x5db], succ=[]
    =================================
    0x2f2: v2f2(0x40) = CONST 
    0x2f5: v2f5 = MLOAD v2f2(0x40)
    0x2f6: v2f6(0x1) = CONST 
    0x2f8: v2f8(0x1) = CONST 
    0x2fa: v2fa(0xa0) = CONST 
    0x2fc: v2fc(0x10000000000000000000000000000000000000000) = SHL v2fa(0xa0), v2f8(0x1)
    0x2fd: v2fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2fc(0x10000000000000000000000000000000000000000), v2f6(0x1)
    0x300: v300 = AND v2fd(0xffffffffffffffffffffffffffffffffffffffff), v608
    0x302: MSTORE v2f5, v300
    0x305: v305 = AND v2fd(0xffffffffffffffffffffffffffffffffffffffff), v60d
    0x306: v306(0x20) = CONST 
    0x309: v309 = ADD v2f5, v306(0x20)
    0x30a: MSTORE v309, v305
    0x30e: v30e = AND v2fd(0xffffffffffffffffffffffffffffffffffffffff), v611
    0x311: v311 = ADD v2f2(0x40), v2f5
    0x312: MSTORE v311, v30e
    0x313: v313(0xffffffff) = CONST 
    0x318: v318 = AND v313(0xffffffff), v61f
    0x319: v319(0x60) = CONST 
    0x31c: v31c = ADD v2f5, v319(0x60)
    0x31d: MSTORE v31c, v318
    0x31e: v31e(0x80) = CONST 
    0x321: v321 = ADD v2f5, v31e(0x80)
    0x325: MSTORE v321, v5fd
    0x327: v327 = MLOAD v2f2(0x40)
    0x32b: v32b(0x0) = SUB v2f5, v327
    0x32c: v32c(0xa0) = CONST 
    0x32e: v32e(0xa0) = ADD v32c(0xa0), v32b(0x0)
    0x330: RETURN v327, v32e(0xa0)

}

function admin()() public {
    Begin block 0x331
    prev=[], succ=[0x339, 0x33d]
    =================================
    0x332: v332 = CALLVALUE 
    0x334: v334 = ISZERO v332
    0x335: v335(0x33d) = CONST 
    0x338: JUMPI v335(0x33d), v334

    Begin block 0x339
    prev=[0x331], succ=[]
    =================================
    0x339: v339(0x0) = CONST 
    0x33c: REVERT v339(0x0), v339(0x0)

    Begin block 0x33d
    prev=[0x331], succ=[0x623]
    =================================
    0x33f: v33f(0x87c) = CONST 
    0x342: v342(0x623) = CONST 
    0x345: JUMP v342(0x623)

    Begin block 0x623
    prev=[0x33d], succ=[0x87c]
    =================================
    0x624: v624(0x0) = CONST 
    0x626: v626 = SLOAD v624(0x0)
    0x627: v627(0x1) = CONST 
    0x629: v629(0x1) = CONST 
    0x62b: v62b(0xa0) = CONST 
    0x62d: v62d(0x10000000000000000000000000000000000000000) = SHL v62b(0xa0), v629(0x1)
    0x62e: v62e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v62d(0x10000000000000000000000000000000000000000), v627(0x1)
    0x62f: v62f = AND v62e(0xffffffffffffffffffffffffffffffffffffffff), v626
    0x631: JUMP v33f(0x87c)

    Begin block 0x87c
    prev=[0x623], succ=[]
    =================================
    0x87d: v87d(0x40) = CONST 
    0x880: v880 = MLOAD v87d(0x40)
    0x881: v881(0x1) = CONST 
    0x883: v883(0x1) = CONST 
    0x885: v885(0xa0) = CONST 
    0x887: v887(0x10000000000000000000000000000000000000000) = SHL v885(0xa0), v883(0x1)
    0x888: v888(0xffffffffffffffffffffffffffffffffffffffff) = SUB v887(0x10000000000000000000000000000000000000000), v881(0x1)
    0x88b: v88b = AND v62f, v888(0xffffffffffffffffffffffffffffffffffffffff)
    0x88d: MSTORE v880, v88b
    0x88e: v88e = MLOAD v87d(0x40)
    0x892: v892(0x0) = SUB v880, v88e
    0x893: v893(0x20) = CONST 
    0x895: v895(0x20) = ADD v893(0x20), v892(0x0)
    0x897: RETURN v88e, v895(0x20)

}

function updateProxyTo(address)() public {
    Begin block 0x346
    prev=[], succ=[0x34e, 0x352]
    =================================
    0x347: v347 = CALLVALUE 
    0x349: v349 = ISZERO v347
    0x34a: v34a(0x352) = CONST 
    0x34d: JUMPI v34a(0x352), v349

    Begin block 0x34e
    prev=[0x346], succ=[]
    =================================
    0x34e: v34e(0x0) = CONST 
    0x351: REVERT v34e(0x0), v34e(0x0)

    Begin block 0x352
    prev=[0x346], succ=[0x365, 0x369]
    =================================
    0x354: v354(0x8b7) = CONST 
    0x357: v357(0x4) = CONST 
    0x35a: v35a = CALLDATASIZE 
    0x35b: v35b = SUB v35a, v357(0x4)
    0x35c: v35c(0x20) = CONST 
    0x35f: v35f = LT v35b, v35c(0x20)
    0x360: v360 = ISZERO v35f
    0x361: v361(0x369) = CONST 
    0x364: JUMPI v361(0x369), v360

    Begin block 0x365
    prev=[0x352], succ=[]
    =================================
    0x365: v365(0x0) = CONST 
    0x368: REVERT v365(0x0), v365(0x0)

    Begin block 0x369
    prev=[0x352], succ=[0x632]
    =================================
    0x36b: v36b = CALLDATALOAD v357(0x4)
    0x36c: v36c(0x1) = CONST 
    0x36e: v36e(0x1) = CONST 
    0x370: v370(0xa0) = CONST 
    0x372: v372(0x10000000000000000000000000000000000000000) = SHL v370(0xa0), v36e(0x1)
    0x373: v373(0xffffffffffffffffffffffffffffffffffffffff) = SUB v372(0x10000000000000000000000000000000000000000), v36c(0x1)
    0x374: v374 = AND v373(0xffffffffffffffffffffffffffffffffffffffff), v36b
    0x375: v375(0x632) = CONST 
    0x378: JUMP v375(0x632)

    Begin block 0x632
    prev=[0x369], succ=[0x645, 0x649]
    =================================
    0x633: v633(0x0) = CONST 
    0x635: v635 = SLOAD v633(0x0)
    0x636: v636(0x1) = CONST 
    0x638: v638(0x1) = CONST 
    0x63a: v63a(0xa0) = CONST 
    0x63c: v63c(0x10000000000000000000000000000000000000000) = SHL v63a(0xa0), v638(0x1)
    0x63d: v63d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v63c(0x10000000000000000000000000000000000000000), v636(0x1)
    0x63e: v63e = AND v63d(0xffffffffffffffffffffffffffffffffffffffff), v635
    0x63f: v63f = CALLER 
    0x640: v640 = EQ v63f, v63e
    0x641: v641(0x649) = CONST 
    0x644: JUMPI v641(0x649), v640

    Begin block 0x645
    prev=[0x632], succ=[]
    =================================
    0x645: v645(0x0) = CONST 
    0x648: REVERT v645(0x0), v645(0x0)

    Begin block 0x649
    prev=[0x632], succ=[0x658, 0x65c]
    =================================
    0x64a: v64a(0x1) = CONST 
    0x64c: v64c(0x1) = CONST 
    0x64e: v64e(0xa0) = CONST 
    0x650: v650(0x10000000000000000000000000000000000000000) = SHL v64e(0xa0), v64c(0x1)
    0x651: v651(0xffffffffffffffffffffffffffffffffffffffff) = SUB v650(0x10000000000000000000000000000000000000000), v64a(0x1)
    0x653: v653 = AND v374, v651(0xffffffffffffffffffffffffffffffffffffffff)
    0x654: v654(0x65c) = CONST 
    0x657: JUMPI v654(0x65c), v653

    Begin block 0x658
    prev=[0x649], succ=[]
    =================================
    0x658: v658(0x0) = CONST 
    0x65b: REVERT v658(0x0), v658(0x0)

    Begin block 0x65c
    prev=[0x649], succ=[0x8b7]
    =================================
    0x65d: v65d(0x1) = CONST 
    0x660: v660 = SLOAD v65d(0x1)
    0x661: v661(0x1) = CONST 
    0x663: v663(0x1) = CONST 
    0x665: v665(0xa0) = CONST 
    0x667: v667(0x10000000000000000000000000000000000000000) = SHL v665(0xa0), v663(0x1)
    0x668: v668(0xffffffffffffffffffffffffffffffffffffffff) = SUB v667(0x10000000000000000000000000000000000000000), v661(0x1)
    0x669: v669(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v668(0xffffffffffffffffffffffffffffffffffffffff)
    0x66a: v66a = AND v669(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v660
    0x66b: v66b(0x1) = CONST 
    0x66d: v66d(0x1) = CONST 
    0x66f: v66f(0xa0) = CONST 
    0x671: v671(0x10000000000000000000000000000000000000000) = SHL v66f(0xa0), v66d(0x1)
    0x672: v672(0xffffffffffffffffffffffffffffffffffffffff) = SUB v671(0x10000000000000000000000000000000000000000), v66b(0x1)
    0x675: v675 = AND v672(0xffffffffffffffffffffffffffffffffffffffff), v374
    0x678: v678 = OR v675, v66a
    0x67c: SSTORE v65d(0x1), v678
    0x67d: v67d(0x40) = CONST 
    0x67f: v67f = MLOAD v67d(0x40)
    0x681: v681 = AND v678, v672(0xffffffffffffffffffffffffffffffffffffffff)
    0x683: v683(0xd32d24edea94f55e932d9a008afc425a8561462d1b1f57bc6e508e9a6b9509e1) = CONST 
    0x6a5: v6a5(0x0) = CONST 
    0x6a8: LOG3 v67f, v6a5(0x0), v683(0xd32d24edea94f55e932d9a008afc425a8561462d1b1f57bc6e508e9a6b9509e1), v675, v681
    0x6aa: JUMP v354(0x8b7)

    Begin block 0x8b7
    prev=[0x65c], succ=[]
    =================================
    0x8b8: STOP 

}

function fallback()() public {
    Begin block 0xdd
    prev=[], succ=[0x379B0xdd]
    =================================
    0xde: vde(0x0) = CONST 
    0xe0: ve0(0xe7) = CONST 
    0xe3: ve3(0x379) = CONST 
    0xe6: JUMP ve3(0x379)

    Begin block 0x379B0xdd
    prev=[0xdd], succ=[0xe7]
    =================================
    0x37aS0xdd: v37aVdd(0x1) = CONST 
    0x37cS0xdd: v37cVdd = SLOAD v37aVdd(0x1)
    0x37dS0xdd: v37dVdd(0x1) = CONST 
    0x37fS0xdd: v37fVdd(0x1) = CONST 
    0x381S0xdd: v381Vdd(0xa0) = CONST 
    0x383S0xdd: v383Vdd(0x10000000000000000000000000000000000000000) = SHL v381Vdd(0xa0), v37fVdd(0x1)
    0x384S0xdd: v384Vdd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v383Vdd(0x10000000000000000000000000000000000000000), v37dVdd(0x1)
    0x385S0xdd: v385Vdd = AND v384Vdd(0xffffffffffffffffffffffffffffffffffffffff), v37cVdd
    0x387S0xdd: JUMP ve0(0xe7)

    Begin block 0xe7
    prev=[0x379B0xdd], succ=[0xf8, 0xfc]
    =================================
    0xea: vea(0x1) = CONST 
    0xec: vec(0x1) = CONST 
    0xee: vee(0xa0) = CONST 
    0xf0: vf0(0x10000000000000000000000000000000000000000) = SHL vee(0xa0), vec(0x1)
    0xf1: vf1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf0(0x10000000000000000000000000000000000000000), vea(0x1)
    0xf3: vf3 = AND v385Vdd, vf1(0xffffffffffffffffffffffffffffffffffffffff)
    0xf4: vf4(0xfc) = CONST 
    0xf7: JUMPI vf4(0xfc), vf3

    Begin block 0xf8
    prev=[0xe7], succ=[]
    =================================
    0xf8: vf8(0x0) = CONST 
    0xfb: REVERT vf8(0x0), vf8(0x0)

    Begin block 0xfc
    prev=[0xe7], succ=[0x11d, 0x11a]
    =================================
    0xfd: vfd(0x40) = CONST 
    0xff: vff = MLOAD vfd(0x40)
    0x100: v100 = CALLDATASIZE 
    0x101: v101(0x0) = CONST 
    0x104: CALLDATACOPY vff, v101(0x0), v100
    0x105: v105(0x0) = CONST 
    0x108: v108 = CALLDATASIZE 
    0x10b: v10b = GAS 
    0x10c: v10c = DELEGATECALL v10b, v385Vdd, vff, v108, v105(0x0), v105(0x0)
    0x10d: v10d = RETURNDATASIZE 
    0x10f: v10f(0x0) = CONST 
    0x112: RETURNDATACOPY vff, v10f(0x0), v10d
    0x115: v115 = ISZERO v10c
    0x116: v116(0x11d) = CONST 
    0x119: JUMPI v116(0x11d), v115

    Begin block 0x11d
    prev=[0xfc], succ=[]
    =================================
    0x120: REVERT vff, v10d

    Begin block 0x11a
    prev=[0xfc], succ=[]
    =================================
    0x11c: RETURN vff, v10d

}

