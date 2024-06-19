function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x7a6]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x794: v794(0x7a6) = CONST 
    0x795: JUMPI v794(0x7a6), v8

    Begin block 0xd
    prev=[0x0], succ=[0x4e, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0xc1e80334) = CONST 
    0x19: v19 = GT v14(0xc1e80334), v12
    0x1a: v1a(0x4e) = CONST 
    0x1d: JUMPI v1a(0x4e), v19

    Begin block 0x4e
    prev=[0xd], succ=[0x7a9, 0x5a]
    =================================
    0x50: v50(0x26782247) = CONST 
    0x55: v55 = EQ v50(0x26782247), v12
    0x79e: v79e(0x7a9) = CONST 
    0x79f: JUMPI v79e(0x7a9), v55

    Begin block 0x7a9
    prev=[0x4e], succ=[]
    =================================
    0x7aa: v7aa(0xfe) = CONST 
    0x7ab: CALLPRIVATE v7aa(0xfe)

    Begin block 0x5a
    prev=[0x4e], succ=[0x7ac, 0x65]
    =================================
    0x5b: v5b(0x4a036c50) = CONST 
    0x60: v60 = EQ v5b(0x4a036c50), v12
    0x7a0: v7a0(0x7ac) = CONST 
    0x7a1: JUMPI v7a0(0x7ac), v60

    Begin block 0x7ac
    prev=[0x5a], succ=[]
    =================================
    0x7ad: v7ad(0x12f) = CONST 
    0x7ae: CALLPRIVATE v7ad(0x12f)

    Begin block 0x65
    prev=[0x5a], succ=[0x7af, 0x70]
    =================================
    0x66: v66(0x6c6a0a0e) = CONST 
    0x6b: v6b = EQ v66(0x6c6a0a0e), v12
    0x7a2: v7a2(0x7af) = CONST 
    0x7a3: JUMPI v7a2(0x7af), v6b

    Begin block 0x7af
    prev=[0x65], succ=[]
    =================================
    0x7b0: v7b0(0x144) = CONST 
    0x7b1: CALLPRIVATE v7b0(0x144)

    Begin block 0x70
    prev=[0x65], succ=[0x7a6, 0x7b2]
    =================================
    0x71: v71(0xb71d1a0c) = CONST 
    0x76: v76 = EQ v71(0xb71d1a0c), v12
    0x7a4: v7a4(0x7b2) = CONST 
    0x7a5: JUMPI v7a4(0x7b2), v76

    Begin block 0x7a6
    prev=[0x0, 0x70], succ=[]
    =================================
    0x7a7: v7a7(0x7b) = CONST 
    0x7a8: CALLPRIVATE v7a7(0x7b)

    Begin block 0x7b2
    prev=[0x70], succ=[]
    =================================
    0x7b3: v7b3(0x159) = CONST 
    0x7b4: CALLPRIVATE v7b3(0x159)

    Begin block 0x1e
    prev=[0xd], succ=[0x7b5, 0x29]
    =================================
    0x1f: v1f(0xc1e80334) = CONST 
    0x24: v24 = EQ v1f(0xc1e80334), v12
    0x796: v796(0x7b5) = CONST 
    0x797: JUMPI v796(0x7b5), v24

    Begin block 0x7b5
    prev=[0x1e], succ=[]
    =================================
    0x7b6: v7b6(0x19e) = CONST 
    0x7b7: CALLPRIVATE v7b6(0x19e)

    Begin block 0x29
    prev=[0x1e], succ=[0x7b8, 0x34]
    =================================
    0x2a: v2a(0xe992a041) = CONST 
    0x2f: v2f = EQ v2a(0xe992a041), v12
    0x798: v798(0x7b8) = CONST 
    0x799: JUMPI v798(0x7b8), v2f

    Begin block 0x7b8
    prev=[0x29], succ=[]
    =================================
    0x7b9: v7b9(0x1b3) = CONST 
    0x7ba: CALLPRIVATE v7b9(0x1b3)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x7bb]
    =================================
    0x35: v35(0xe9c714f2) = CONST 
    0x3a: v3a = EQ v35(0xe9c714f2), v12
    0x79a: v79a(0x7bb) = CONST 
    0x79b: JUMPI v79a(0x7bb), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x7be]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x79c: v79c(0x7be) = CONST 
    0x79d: JUMPI v79c(0x7be), v45

    Begin block 0x4a
    prev=[0x3f], succ=[]
    =================================
    0x4a: v4a(0x7b) = CONST 
    0x4d: JUMP v4a(0x7b)

    Begin block 0x7be
    prev=[0x3f], succ=[]
    =================================
    0x7bf: v7bf(0x1fb) = CONST 
    0x7c0: CALLPRIVATE v7bf(0x1fb)

    Begin block 0x7bb
    prev=[0x34], succ=[]
    =================================
    0x7bc: v7bc(0x1e6) = CONST 
    0x7bd: CALLPRIVATE v7bc(0x1e6)

}

function pendingWanFarmImplementation()() public {
    Begin block 0x12f
    prev=[], succ=[0x137, 0x13b]
    =================================
    0x130: v130 = CALLVALUE 
    0x132: v132 = ISZERO v130
    0x133: v133(0x13b) = CONST 
    0x136: JUMPI v133(0x13b), v132

    Begin block 0x137
    prev=[0x12f], succ=[]
    =================================
    0x137: v137(0x0) = CONST 
    0x13a: REVERT v137(0x0), v137(0x0)

    Begin block 0x13b
    prev=[0x12f], succ=[0x21f]
    =================================
    0x13d: v13d(0x63e) = CONST 
    0x140: v140(0x21f) = CONST 
    0x143: JUMP v140(0x21f)

    Begin block 0x21f
    prev=[0x13b], succ=[0x63e]
    =================================
    0x220: v220(0x3) = CONST 
    0x222: v222 = SLOAD v220(0x3)
    0x223: v223(0x1) = CONST 
    0x225: v225(0x1) = CONST 
    0x227: v227(0xa0) = CONST 
    0x229: v229(0x10000000000000000000000000000000000000000) = SHL v227(0xa0), v225(0x1)
    0x22a: v22a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v229(0x10000000000000000000000000000000000000000), v223(0x1)
    0x22b: v22b = AND v22a(0xffffffffffffffffffffffffffffffffffffffff), v222
    0x22d: JUMP v13d(0x63e)

    Begin block 0x63e
    prev=[0x21f], succ=[]
    =================================
    0x63f: v63f(0x40) = CONST 
    0x642: v642 = MLOAD v63f(0x40)
    0x643: v643(0x1) = CONST 
    0x645: v645(0x1) = CONST 
    0x647: v647(0xa0) = CONST 
    0x649: v649(0x10000000000000000000000000000000000000000) = SHL v647(0xa0), v645(0x1)
    0x64a: v64a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v649(0x10000000000000000000000000000000000000000), v643(0x1)
    0x64d: v64d = AND v22b, v64a(0xffffffffffffffffffffffffffffffffffffffff)
    0x64f: MSTORE v642, v64d
    0x650: v650 = MLOAD v63f(0x40)
    0x654: v654(0x0) = SUB v642, v650
    0x655: v655(0x20) = CONST 
    0x657: v657(0x20) = ADD v655(0x20), v654(0x0)
    0x659: RETURN v650, v657(0x20)

}

function wanFarmImplementation()() public {
    Begin block 0x144
    prev=[], succ=[0x14c, 0x150]
    =================================
    0x145: v145 = CALLVALUE 
    0x147: v147 = ISZERO v145
    0x148: v148(0x150) = CONST 
    0x14b: JUMPI v148(0x150), v147

    Begin block 0x14c
    prev=[0x144], succ=[]
    =================================
    0x14c: v14c(0x0) = CONST 
    0x14f: REVERT v14c(0x0), v14c(0x0)

    Begin block 0x150
    prev=[0x144], succ=[0x22e]
    =================================
    0x152: v152(0x679) = CONST 
    0x155: v155(0x22e) = CONST 
    0x158: JUMP v155(0x22e)

    Begin block 0x22e
    prev=[0x150], succ=[0x679]
    =================================
    0x22f: v22f(0x2) = CONST 
    0x231: v231 = SLOAD v22f(0x2)
    0x232: v232(0x1) = CONST 
    0x234: v234(0x1) = CONST 
    0x236: v236(0xa0) = CONST 
    0x238: v238(0x10000000000000000000000000000000000000000) = SHL v236(0xa0), v234(0x1)
    0x239: v239(0xffffffffffffffffffffffffffffffffffffffff) = SUB v238(0x10000000000000000000000000000000000000000), v232(0x1)
    0x23a: v23a = AND v239(0xffffffffffffffffffffffffffffffffffffffff), v231
    0x23c: JUMP v152(0x679)

    Begin block 0x679
    prev=[0x22e], succ=[]
    =================================
    0x67a: v67a(0x40) = CONST 
    0x67d: v67d = MLOAD v67a(0x40)
    0x67e: v67e(0x1) = CONST 
    0x680: v680(0x1) = CONST 
    0x682: v682(0xa0) = CONST 
    0x684: v684(0x10000000000000000000000000000000000000000) = SHL v682(0xa0), v680(0x1)
    0x685: v685(0xffffffffffffffffffffffffffffffffffffffff) = SUB v684(0x10000000000000000000000000000000000000000), v67e(0x1)
    0x688: v688 = AND v23a, v685(0xffffffffffffffffffffffffffffffffffffffff)
    0x68a: MSTORE v67d, v688
    0x68b: v68b = MLOAD v67a(0x40)
    0x68f: v68f(0x0) = SUB v67d, v68b
    0x690: v690(0x20) = CONST 
    0x692: v692(0x20) = ADD v690(0x20), v68f(0x0)
    0x694: RETURN v68b, v692(0x20)

}

function _setPendingAdmin(address)() public {
    Begin block 0x159
    prev=[], succ=[0x161, 0x165]
    =================================
    0x15a: v15a = CALLVALUE 
    0x15c: v15c = ISZERO v15a
    0x15d: v15d(0x165) = CONST 
    0x160: JUMPI v15d(0x165), v15c

    Begin block 0x161
    prev=[0x159], succ=[]
    =================================
    0x161: v161(0x0) = CONST 
    0x164: REVERT v161(0x0), v161(0x0)

    Begin block 0x165
    prev=[0x159], succ=[0x178, 0x17c]
    =================================
    0x167: v167(0x6b4) = CONST 
    0x16a: v16a(0x4) = CONST 
    0x16d: v16d = CALLDATASIZE 
    0x16e: v16e = SUB v16d, v16a(0x4)
    0x16f: v16f(0x20) = CONST 
    0x172: v172 = LT v16e, v16f(0x20)
    0x173: v173 = ISZERO v172
    0x174: v174(0x17c) = CONST 
    0x177: JUMPI v174(0x17c), v173

    Begin block 0x178
    prev=[0x165], succ=[]
    =================================
    0x178: v178(0x0) = CONST 
    0x17b: REVERT v178(0x0), v178(0x0)

    Begin block 0x17c
    prev=[0x165], succ=[0x23d]
    =================================
    0x17e: v17e = CALLDATALOAD v16a(0x4)
    0x17f: v17f(0x1) = CONST 
    0x181: v181(0x1) = CONST 
    0x183: v183(0xa0) = CONST 
    0x185: v185(0x10000000000000000000000000000000000000000) = SHL v183(0xa0), v181(0x1)
    0x186: v186(0xffffffffffffffffffffffffffffffffffffffff) = SUB v185(0x10000000000000000000000000000000000000000), v17f(0x1)
    0x187: v187 = AND v186(0xffffffffffffffffffffffffffffffffffffffff), v17e
    0x188: v188(0x23d) = CONST 
    0x18b: JUMP v188(0x23d)

    Begin block 0x23d
    prev=[0x17c], succ=[0x251, 0x263]
    =================================
    0x23e: v23e(0x0) = CONST 
    0x241: v241 = SLOAD v23e(0x0)
    0x242: v242(0x1) = CONST 
    0x244: v244(0x1) = CONST 
    0x246: v246(0xa0) = CONST 
    0x248: v248(0x10000000000000000000000000000000000000000) = SHL v246(0xa0), v244(0x1)
    0x249: v249(0xffffffffffffffffffffffffffffffffffffffff) = SUB v248(0x10000000000000000000000000000000000000000), v242(0x1)
    0x24a: v24a = AND v249(0xffffffffffffffffffffffffffffffffffffffff), v241
    0x24b: v24b = CALLER 
    0x24c: v24c = EQ v24b, v24a
    0x24d: v24d(0x263) = CONST 
    0x250: JUMPI v24d(0x263), v24c

    Begin block 0x251
    prev=[0x23d], succ=[0x25c0x159]
    =================================
    0x251: v251(0x25c) = CONST 
    0x254: v254(0x1) = CONST 
    0x256: v256(0x2) = CONST 
    0x258: v258(0x542) = CONST 
    0x25b: v25b_0 = CALLPRIVATE v258(0x542), v256(0x2), v254(0x1), v251(0x25c)

    Begin block 0x25c0x159
    prev=[0x251], succ=[0x2c90x159]
    =================================
    0x25f0x159: v15925f(0x2c9) = CONST 
    0x2620x159: JUMP v15925f(0x2c9)

    Begin block 0x2c90x159
    prev=[0x25c0x159, 0x2c50x159], succ=[0x6b4]
    =================================
    0x2cd0x159: JUMP v167(0x6b4)

    Begin block 0x6b4
    prev=[0x2c90x159], succ=[]
    =================================
    0x6b4_0x0: v6b4_0 = PHI v2c3(0x0), v25b_0
    0x6b5: v6b5(0x40) = CONST 
    0x6b8: v6b8 = MLOAD v6b5(0x40)
    0x6bb: MSTORE v6b8, v6b4_0
    0x6bc: v6bc = MLOAD v6b5(0x40)
    0x6c0: v6c0(0x0) = SUB v6b8, v6bc
    0x6c1: v6c1(0x20) = CONST 
    0x6c3: v6c3(0x20) = ADD v6c1(0x20), v6c0(0x0)
    0x6c5: RETURN v6bc, v6c3(0x20)

    Begin block 0x263
    prev=[0x23d], succ=[0x2c50x159]
    =================================
    0x264: v264(0x1) = CONST 
    0x267: v267 = SLOAD v264(0x1)
    0x268: v268(0x1) = CONST 
    0x26a: v26a(0x1) = CONST 
    0x26c: v26c(0xa0) = CONST 
    0x26e: v26e(0x10000000000000000000000000000000000000000) = SHL v26c(0xa0), v26a(0x1)
    0x26f: v26f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26e(0x10000000000000000000000000000000000000000), v268(0x1)
    0x272: v272 = AND v26f(0xffffffffffffffffffffffffffffffffffffffff), v187
    0x273: v273(0x1) = CONST 
    0x275: v275(0x1) = CONST 
    0x277: v277(0xa0) = CONST 
    0x279: v279(0x10000000000000000000000000000000000000000) = SHL v277(0xa0), v275(0x1)
    0x27a: v27a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v279(0x10000000000000000000000000000000000000000), v273(0x1)
    0x27b: v27b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v27a(0xffffffffffffffffffffffffffffffffffffffff)
    0x27d: v27d = AND v267, v27b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x27f: v27f = OR v272, v27d
    0x282: SSTORE v264(0x1), v27f
    0x283: v283(0x40) = CONST 
    0x286: v286 = MLOAD v283(0x40)
    0x28a: v28a = AND v267, v26f(0xffffffffffffffffffffffffffffffffffffffff)
    0x28d: MSTORE v286, v28a
    0x28e: v28e(0x20) = CONST 
    0x291: v291 = ADD v286, v28e(0x20)
    0x295: MSTORE v291, v272
    0x297: v297 = MLOAD v283(0x40)
    0x298: v298(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x2bd: v2bd(0x0) = SUB v286, v297
    0x2c0: v2c0(0x40) = ADD v283(0x40), v2bd(0x0)
    0x2c2: LOG1 v297, v2c0(0x40), v298(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x2c3: v2c3(0x0) = CONST 

    Begin block 0x2c50x159
    prev=[0x263], succ=[0x2c90x159]
    =================================

}

function _acceptImplementation()() public {
    Begin block 0x19e
    prev=[], succ=[0x1a6, 0x1aa]
    =================================
    0x19f: v19f = CALLVALUE 
    0x1a1: v1a1 = ISZERO v19f
    0x1a2: v1a2(0x1aa) = CONST 
    0x1a5: JUMPI v1a2(0x1aa), v1a1

    Begin block 0x1a6
    prev=[0x19e], succ=[]
    =================================
    0x1a6: v1a6(0x0) = CONST 
    0x1a9: REVERT v1a6(0x0), v1a6(0x0)

    Begin block 0x1aa
    prev=[0x19e], succ=[0x2ceB0x1aa]
    =================================
    0x1ac: v1ac(0x6e5) = CONST 
    0x1af: v1af(0x2ce) = CONST 
    0x1b2: JUMP v1af(0x2ce)

    Begin block 0x2ceB0x1aa
    prev=[0x1aa], succ=[0x2f4B0x1aa, 0x2e6B0x1aa]
    =================================
    0x2cfS0x1aa: v2cfV1aa(0x3) = CONST 
    0x2d1S0x1aa: v2d1V1aa = SLOAD v2cfV1aa(0x3)
    0x2d2S0x1aa: v2d2V1aa(0x0) = CONST 
    0x2d5S0x1aa: v2d5V1aa(0x1) = CONST 
    0x2d7S0x1aa: v2d7V1aa(0x1) = CONST 
    0x2d9S0x1aa: v2d9V1aa(0xa0) = CONST 
    0x2dbS0x1aa: v2dbV1aa(0x10000000000000000000000000000000000000000) = SHL v2d9V1aa(0xa0), v2d7V1aa(0x1)
    0x2dcS0x1aa: v2dcV1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2dbV1aa(0x10000000000000000000000000000000000000000), v2d5V1aa(0x1)
    0x2ddS0x1aa: v2ddV1aa = AND v2dcV1aa(0xffffffffffffffffffffffffffffffffffffffff), v2d1V1aa
    0x2deS0x1aa: v2deV1aa = CALLER 
    0x2dfS0x1aa: v2dfV1aa = EQ v2deV1aa, v2ddV1aa
    0x2e0S0x1aa: v2e0V1aa = ISZERO v2dfV1aa
    0x2e2S0x1aa: v2e2V1aa(0x2f4) = CONST 
    0x2e5S0x1aa: JUMPI v2e2V1aa(0x2f4), v2e0V1aa

    Begin block 0x2f4B0x1aa
    prev=[0x2ceB0x1aa, 0x2e6B0x1aa], succ=[0x2faB0x1aa, 0x30bB0x1aa]
    =================================
    0x2f4_0x0S0x1aa: v2f4_0V1aa = PHI v2e0V1aa, v2f3V1aa
    0x2f5S0x1aa: v2f5V1aa = ISZERO v2f4_0V1aa
    0x2f6S0x1aa: v2f6V1aa(0x30b) = CONST 
    0x2f9S0x1aa: JUMPI v2f6V1aa(0x30b), v2f5V1aa

    Begin block 0x2faB0x1aa
    prev=[0x2f4B0x1aa], succ=[0x3040x2ceB0x1aa]
    =================================
    0x2faS0x1aa: v2faV1aa(0x304) = CONST 
    0x2fdS0x1aa: v2fdV1aa(0x1) = CONST 
    0x300S0x1aa: v300V1aa(0x542) = CONST 
    0x303S0x1aa: v303_0V1aa = CALLPRIVATE v300V1aa(0x542), v2fdV1aa(0x1), v2fdV1aa(0x1), v2faV1aa(0x304)

    Begin block 0x3040x2ceB0x1aa
    prev=[0x2faB0x1aa], succ=[0x3c60x2ceB0x1aa]
    =================================
    0x3070x2ceS0x1aa: v2ce307V1aa(0x3c6) = CONST 
    0x30a0x2ceS0x1aa: JUMP v2ce307V1aa(0x3c6)

    Begin block 0x3c60x2ceB0x1aa
    prev=[0x3040x2ceB0x1aa, 0x3c10x2ceB0x1aa], succ=[0x6e5]
    =================================
    0x3c60x2ce_0x0S0x1aa: v3c62ce_0V1aa = PHI v303_0V1aa, v3bfV1aa(0x0)
    0x3c80x2ceS0x1aa: JUMP v1ac(0x6e5)

    Begin block 0x6e5
    prev=[0x3c60x2ceB0x1aa], succ=[]
    =================================
    0x6e6: v6e6(0x40) = CONST 
    0x6e9: v6e9 = MLOAD v6e6(0x40)
    0x6ec: MSTORE v6e9, v3c62ce_0V1aa
    0x6ed: v6ed = MLOAD v6e6(0x40)
    0x6f1: v6f1(0x0) = SUB v6e9, v6ed
    0x6f2: v6f2(0x20) = CONST 
    0x6f4: v6f4(0x20) = ADD v6f2(0x20), v6f1(0x0)
    0x6f6: RETURN v6ed, v6f4(0x20)

    Begin block 0x30bB0x1aa
    prev=[0x2f4B0x1aa], succ=[0x3c10x2ceB0x1aa]
    =================================
    0x30cS0x1aa: v30cV1aa(0x2) = CONST 
    0x30fS0x1aa: v30fV1aa = SLOAD v30cV1aa(0x2)
    0x310S0x1aa: v310V1aa(0x3) = CONST 
    0x313S0x1aa: v313V1aa = SLOAD v310V1aa(0x3)
    0x314S0x1aa: v314V1aa(0x1) = CONST 
    0x316S0x1aa: v316V1aa(0x1) = CONST 
    0x318S0x1aa: v318V1aa(0xa0) = CONST 
    0x31aS0x1aa: v31aV1aa(0x10000000000000000000000000000000000000000) = SHL v318V1aa(0xa0), v316V1aa(0x1)
    0x31bS0x1aa: v31bV1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v31aV1aa(0x10000000000000000000000000000000000000000), v314V1aa(0x1)
    0x31eS0x1aa: v31eV1aa = AND v313V1aa, v31bV1aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x31fS0x1aa: v31fV1aa(0x1) = CONST 
    0x321S0x1aa: v321V1aa(0x1) = CONST 
    0x323S0x1aa: v323V1aa(0xa0) = CONST 
    0x325S0x1aa: v325V1aa(0x10000000000000000000000000000000000000000) = SHL v323V1aa(0xa0), v321V1aa(0x1)
    0x326S0x1aa: v326V1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v325V1aa(0x10000000000000000000000000000000000000000), v31fV1aa(0x1)
    0x327S0x1aa: v327V1aa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v326V1aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x32aS0x1aa: v32aV1aa = AND v30fV1aa, v327V1aa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x32cS0x1aa: v32cV1aa = OR v31eV1aa, v32aV1aa
    0x330S0x1aa: SSTORE v30cV1aa(0x2), v32cV1aa
    0x333S0x1aa: v333V1aa = AND v313V1aa, v327V1aa(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x336S0x1aa: SSTORE v310V1aa(0x3), v333V1aa
    0x337S0x1aa: v337V1aa(0x40) = CONST 
    0x33aS0x1aa: v33aV1aa = MLOAD v337V1aa(0x40)
    0x33dS0x1aa: v33dV1aa = AND v31bV1aa(0xffffffffffffffffffffffffffffffffffffffff), v30fV1aa
    0x340S0x1aa: MSTORE v33aV1aa, v33dV1aa
    0x344S0x1aa: v344V1aa = AND v31bV1aa(0xffffffffffffffffffffffffffffffffffffffff), v32cV1aa
    0x345S0x1aa: v345V1aa(0x20) = CONST 
    0x348S0x1aa: v348V1aa = ADD v33aV1aa, v345V1aa(0x20)
    0x349S0x1aa: MSTORE v348V1aa, v344V1aa
    0x34bS0x1aa: v34bV1aa = MLOAD v337V1aa(0x40)
    0x34eS0x1aa: v34eV1aa(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a) = CONST 
    0x373S0x1aa: v373V1aa(0x0) = SUB v33aV1aa, v34bV1aa
    0x374S0x1aa: v374V1aa(0x40) = ADD v373V1aa(0x0), v337V1aa(0x40)
    0x376S0x1aa: LOG1 v34bV1aa, v374V1aa(0x40), v34eV1aa(0xd604de94d45953f9138079ec1b82d533cb2160c906d1076d1f7ed54befbca97a)
    0x377S0x1aa: v377V1aa(0x3) = CONST 
    0x379S0x1aa: v379V1aa = SLOAD v377V1aa(0x3)
    0x37aS0x1aa: v37aV1aa(0x40) = CONST 
    0x37dS0x1aa: v37dV1aa = MLOAD v37aV1aa(0x40)
    0x37eS0x1aa: v37eV1aa(0x1) = CONST 
    0x380S0x1aa: v380V1aa(0x1) = CONST 
    0x382S0x1aa: v382V1aa(0xa0) = CONST 
    0x384S0x1aa: v384V1aa(0x10000000000000000000000000000000000000000) = SHL v382V1aa(0xa0), v380V1aa(0x1)
    0x385S0x1aa: v385V1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v384V1aa(0x10000000000000000000000000000000000000000), v37eV1aa(0x1)
    0x388S0x1aa: v388V1aa = AND v31eV1aa, v385V1aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x38aS0x1aa: MSTORE v37dV1aa, v388V1aa
    0x38dS0x1aa: v38dV1aa = AND v379V1aa, v385V1aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x38eS0x1aa: v38eV1aa(0x20) = CONST 
    0x391S0x1aa: v391V1aa = ADD v37dV1aa, v38eV1aa(0x20)
    0x392S0x1aa: MSTORE v391V1aa, v38dV1aa
    0x394S0x1aa: v394V1aa = MLOAD v37aV1aa(0x40)
    0x395S0x1aa: v395V1aa(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x3b9S0x1aa: v3b9V1aa(0x0) = SUB v37dV1aa, v394V1aa
    0x3bcS0x1aa: v3bcV1aa(0x40) = ADD v37aV1aa(0x40), v3b9V1aa(0x0)
    0x3beS0x1aa: LOG1 v394V1aa, v3bcV1aa(0x40), v395V1aa(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x3bfS0x1aa: v3bfV1aa(0x0) = CONST 

    Begin block 0x3c10x2ceB0x1aa
    prev=[0x30bB0x1aa], succ=[0x3c60x2ceB0x1aa]
    =================================

    Begin block 0x2e6B0x1aa
    prev=[0x2ceB0x1aa], succ=[0x2f4B0x1aa]
    =================================
    0x2e7S0x1aa: v2e7V1aa(0x3) = CONST 
    0x2e9S0x1aa: v2e9V1aa = SLOAD v2e7V1aa(0x3)
    0x2eaS0x1aa: v2eaV1aa(0x1) = CONST 
    0x2ecS0x1aa: v2ecV1aa(0x1) = CONST 
    0x2eeS0x1aa: v2eeV1aa(0xa0) = CONST 
    0x2f0S0x1aa: v2f0V1aa(0x10000000000000000000000000000000000000000) = SHL v2eeV1aa(0xa0), v2ecV1aa(0x1)
    0x2f1S0x1aa: v2f1V1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2f0V1aa(0x10000000000000000000000000000000000000000), v2eaV1aa(0x1)
    0x2f2S0x1aa: v2f2V1aa = AND v2f1V1aa(0xffffffffffffffffffffffffffffffffffffffff), v2e9V1aa
    0x2f3S0x1aa: v2f3V1aa = ISZERO v2f2V1aa

}

function _setPendingImplementation(address)() public {
    Begin block 0x1b3
    prev=[], succ=[0x1bb, 0x1bf]
    =================================
    0x1b4: v1b4 = CALLVALUE 
    0x1b6: v1b6 = ISZERO v1b4
    0x1b7: v1b7(0x1bf) = CONST 
    0x1ba: JUMPI v1b7(0x1bf), v1b6

    Begin block 0x1bb
    prev=[0x1b3], succ=[]
    =================================
    0x1bb: v1bb(0x0) = CONST 
    0x1be: REVERT v1bb(0x0), v1bb(0x0)

    Begin block 0x1bf
    prev=[0x1b3], succ=[0x1d2, 0x1d6]
    =================================
    0x1c1: v1c1(0x716) = CONST 
    0x1c4: v1c4(0x4) = CONST 
    0x1c7: v1c7 = CALLDATASIZE 
    0x1c8: v1c8 = SUB v1c7, v1c4(0x4)
    0x1c9: v1c9(0x20) = CONST 
    0x1cc: v1cc = LT v1c8, v1c9(0x20)
    0x1cd: v1cd = ISZERO v1cc
    0x1ce: v1ce(0x1d6) = CONST 
    0x1d1: JUMPI v1ce(0x1d6), v1cd

    Begin block 0x1d2
    prev=[0x1bf], succ=[]
    =================================
    0x1d2: v1d2(0x0) = CONST 
    0x1d5: REVERT v1d2(0x0), v1d2(0x0)

    Begin block 0x1d6
    prev=[0x1bf], succ=[0x3c9]
    =================================
    0x1d8: v1d8 = CALLDATALOAD v1c4(0x4)
    0x1d9: v1d9(0x1) = CONST 
    0x1db: v1db(0x1) = CONST 
    0x1dd: v1dd(0xa0) = CONST 
    0x1df: v1df(0x10000000000000000000000000000000000000000) = SHL v1dd(0xa0), v1db(0x1)
    0x1e0: v1e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1df(0x10000000000000000000000000000000000000000), v1d9(0x1)
    0x1e1: v1e1 = AND v1e0(0xffffffffffffffffffffffffffffffffffffffff), v1d8
    0x1e2: v1e2(0x3c9) = CONST 
    0x1e5: JUMP v1e2(0x3c9)

    Begin block 0x3c9
    prev=[0x1d6], succ=[0x3dd, 0x3e8]
    =================================
    0x3ca: v3ca(0x0) = CONST 
    0x3cd: v3cd = SLOAD v3ca(0x0)
    0x3ce: v3ce(0x1) = CONST 
    0x3d0: v3d0(0x1) = CONST 
    0x3d2: v3d2(0xa0) = CONST 
    0x3d4: v3d4(0x10000000000000000000000000000000000000000) = SHL v3d2(0xa0), v3d0(0x1)
    0x3d5: v3d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d4(0x10000000000000000000000000000000000000000), v3ce(0x1)
    0x3d6: v3d6 = AND v3d5(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0x3d7: v3d7 = CALLER 
    0x3d8: v3d8 = EQ v3d7, v3d6
    0x3d9: v3d9(0x3e8) = CONST 
    0x3dc: JUMPI v3d9(0x3e8), v3d8

    Begin block 0x3dd
    prev=[0x3c9], succ=[0x25c0x1b3]
    =================================
    0x3dd: v3dd(0x25c) = CONST 
    0x3e0: v3e0(0x1) = CONST 
    0x3e2: v3e2(0x3) = CONST 
    0x3e4: v3e4(0x542) = CONST 
    0x3e7: v3e7_0 = CALLPRIVATE v3e4(0x542), v3e2(0x3), v3e0(0x1), v3dd(0x25c)

    Begin block 0x25c0x1b3
    prev=[0x3dd], succ=[0x2c90x1b3]
    =================================
    0x25f0x1b3: v1b325f(0x2c9) = CONST 
    0x2620x1b3: JUMP v1b325f(0x2c9)

    Begin block 0x2c90x1b3
    prev=[0x25c0x1b3, 0x2c50x1b3], succ=[0x716]
    =================================
    0x2cd0x1b3: JUMP v1c1(0x716)

    Begin block 0x716
    prev=[0x2c90x1b3], succ=[]
    =================================
    0x716_0x0: v716_0 = PHI v447(0x0), v3e7_0
    0x717: v717(0x40) = CONST 
    0x71a: v71a = MLOAD v717(0x40)
    0x71d: MSTORE v71a, v716_0
    0x71e: v71e = MLOAD v717(0x40)
    0x722: v722(0x0) = SUB v71a, v71e
    0x723: v723(0x20) = CONST 
    0x725: v725(0x20) = ADD v723(0x20), v722(0x0)
    0x727: RETURN v71e, v725(0x20)

    Begin block 0x3e8
    prev=[0x3c9], succ=[0x2c50x1b3]
    =================================
    0x3e9: v3e9(0x3) = CONST 
    0x3ec: v3ec = SLOAD v3e9(0x3)
    0x3ed: v3ed(0x1) = CONST 
    0x3ef: v3ef(0x1) = CONST 
    0x3f1: v3f1(0xa0) = CONST 
    0x3f3: v3f3(0x10000000000000000000000000000000000000000) = SHL v3f1(0xa0), v3ef(0x1)
    0x3f4: v3f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f3(0x10000000000000000000000000000000000000000), v3ed(0x1)
    0x3f7: v3f7 = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v1e1
    0x3f8: v3f8(0x1) = CONST 
    0x3fa: v3fa(0x1) = CONST 
    0x3fc: v3fc(0xa0) = CONST 
    0x3fe: v3fe(0x10000000000000000000000000000000000000000) = SHL v3fc(0xa0), v3fa(0x1)
    0x3ff: v3ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fe(0x10000000000000000000000000000000000000000), v3f8(0x1)
    0x400: v400(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v3ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x402: v402 = AND v3ec, v400(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x403: v403 = OR v402, v3f7
    0x407: SSTORE v3e9(0x3), v403
    0x408: v408(0x40) = CONST 
    0x40b: v40b = MLOAD v408(0x40)
    0x40e: v40e = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v3ec
    0x411: MSTORE v40b, v40e
    0x415: v415 = AND v3f4(0xffffffffffffffffffffffffffffffffffffffff), v403
    0x416: v416(0x20) = CONST 
    0x419: v419 = ADD v40b, v416(0x20)
    0x41a: MSTORE v419, v415
    0x41c: v41c = MLOAD v408(0x40)
    0x41d: v41d(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815) = CONST 
    0x441: v441(0x0) = SUB v40b, v41c
    0x444: v444(0x40) = ADD v408(0x40), v441(0x0)
    0x446: LOG1 v41c, v444(0x40), v41d(0xe945ccee5d701fc83f9b8aa8ca94ea4219ec1fcbd4f4cab4f0ea57c5c3e1d815)
    0x447: v447(0x0) = CONST 
    0x449: v449(0x2c5) = CONST 
    0x44c: JUMP v449(0x2c5)

    Begin block 0x2c50x1b3
    prev=[0x3e8], succ=[0x2c90x1b3]
    =================================

}

function _acceptAdmin()() public {
    Begin block 0x1e6
    prev=[], succ=[0x1ee, 0x1f2]
    =================================
    0x1e7: v1e7 = CALLVALUE 
    0x1e9: v1e9 = ISZERO v1e7
    0x1ea: v1ea(0x1f2) = CONST 
    0x1ed: JUMPI v1ea(0x1f2), v1e9

    Begin block 0x1ee
    prev=[0x1e6], succ=[]
    =================================
    0x1ee: v1ee(0x0) = CONST 
    0x1f1: REVERT v1ee(0x0), v1ee(0x0)

    Begin block 0x1f2
    prev=[0x1e6], succ=[0x44dB0x1f2]
    =================================
    0x1f4: v1f4(0x747) = CONST 
    0x1f7: v1f7(0x44d) = CONST 
    0x1fa: JUMP v1f7(0x44d)

    Begin block 0x44dB0x1f2
    prev=[0x1f2], succ=[0x468B0x1f2, 0x465B0x1f2]
    =================================
    0x44eS0x1f2: v44eV1f2(0x1) = CONST 
    0x450S0x1f2: v450V1f2 = SLOAD v44eV1f2(0x1)
    0x451S0x1f2: v451V1f2(0x0) = CONST 
    0x454S0x1f2: v454V1f2(0x1) = CONST 
    0x456S0x1f2: v456V1f2(0x1) = CONST 
    0x458S0x1f2: v458V1f2(0xa0) = CONST 
    0x45aS0x1f2: v45aV1f2(0x10000000000000000000000000000000000000000) = SHL v458V1f2(0xa0), v456V1f2(0x1)
    0x45bS0x1f2: v45bV1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45aV1f2(0x10000000000000000000000000000000000000000), v454V1f2(0x1)
    0x45cS0x1f2: v45cV1f2 = AND v45bV1f2(0xffffffffffffffffffffffffffffffffffffffff), v450V1f2
    0x45dS0x1f2: v45dV1f2 = CALLER 
    0x45eS0x1f2: v45eV1f2 = EQ v45dV1f2, v45cV1f2
    0x45fS0x1f2: v45fV1f2 = ISZERO v45eV1f2
    0x461S0x1f2: v461V1f2(0x468) = CONST 
    0x464S0x1f2: JUMPI v461V1f2(0x468), v45fV1f2

    Begin block 0x468B0x1f2
    prev=[0x44dB0x1f2, 0x465B0x1f2], succ=[0x46eB0x1f2, 0x479B0x1f2]
    =================================
    0x468_0x0S0x1f2: v468_0V1f2 = PHI v45fV1f2, v467V1f2
    0x469S0x1f2: v469V1f2 = ISZERO v468_0V1f2
    0x46aS0x1f2: v46aV1f2(0x479) = CONST 
    0x46dS0x1f2: JUMPI v46aV1f2(0x479), v469V1f2

    Begin block 0x46eB0x1f2
    prev=[0x468B0x1f2], succ=[0x3040x44dB0x1f2]
    =================================
    0x46eS0x1f2: v46eV1f2(0x304) = CONST 
    0x471S0x1f2: v471V1f2(0x1) = CONST 
    0x473S0x1f2: v473V1f2(0x0) = CONST 
    0x475S0x1f2: v475V1f2(0x542) = CONST 
    0x478S0x1f2: v478_0V1f2 = CALLPRIVATE v475V1f2(0x542), v473V1f2(0x0), v471V1f2(0x1), v46eV1f2(0x304)

    Begin block 0x3040x44dB0x1f2
    prev=[0x46eB0x1f2], succ=[0x3c60x44dB0x1f2]
    =================================
    0x3070x44dS0x1f2: v44d307V1f2(0x3c6) = CONST 
    0x30a0x44dS0x1f2: JUMP v44d307V1f2(0x3c6)

    Begin block 0x3c60x44dB0x1f2
    prev=[0x3040x44dB0x1f2, 0x3c10x44dB0x1f2], succ=[0x747]
    =================================
    0x3c60x44d_0x0S0x1f2: v3c644d_0V1f2 = PHI v478_0V1f2, v52dV1f2(0x0)
    0x3c80x44dS0x1f2: JUMP v1f4(0x747)

    Begin block 0x747
    prev=[0x3c60x44dB0x1f2], succ=[]
    =================================
    0x748: v748(0x40) = CONST 
    0x74b: v74b = MLOAD v748(0x40)
    0x74e: MSTORE v74b, v3c644d_0V1f2
    0x74f: v74f = MLOAD v748(0x40)
    0x753: v753(0x0) = SUB v74b, v74f
    0x754: v754(0x20) = CONST 
    0x756: v756(0x20) = ADD v754(0x20), v753(0x0)
    0x758: RETURN v74f, v756(0x20)

    Begin block 0x479B0x1f2
    prev=[0x468B0x1f2], succ=[0x3c10x44dB0x1f2]
    =================================
    0x47aS0x1f2: v47aV1f2(0x0) = CONST 
    0x47dS0x1f2: v47dV1f2 = SLOAD v47aV1f2(0x0)
    0x47eS0x1f2: v47eV1f2(0x1) = CONST 
    0x481S0x1f2: v481V1f2 = SLOAD v47eV1f2(0x1)
    0x482S0x1f2: v482V1f2(0x1) = CONST 
    0x484S0x1f2: v484V1f2(0x1) = CONST 
    0x486S0x1f2: v486V1f2(0xa0) = CONST 
    0x488S0x1f2: v488V1f2(0x10000000000000000000000000000000000000000) = SHL v486V1f2(0xa0), v484V1f2(0x1)
    0x489S0x1f2: v489V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v488V1f2(0x10000000000000000000000000000000000000000), v482V1f2(0x1)
    0x48cS0x1f2: v48cV1f2 = AND v481V1f2, v489V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x48dS0x1f2: v48dV1f2(0x1) = CONST 
    0x48fS0x1f2: v48fV1f2(0x1) = CONST 
    0x491S0x1f2: v491V1f2(0xa0) = CONST 
    0x493S0x1f2: v493V1f2(0x10000000000000000000000000000000000000000) = SHL v491V1f2(0xa0), v48fV1f2(0x1)
    0x494S0x1f2: v494V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v493V1f2(0x10000000000000000000000000000000000000000), v48dV1f2(0x1)
    0x495S0x1f2: v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v494V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x498S0x1f2: v498V1f2 = AND v47dV1f2, v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x49aS0x1f2: v49aV1f2 = OR v48cV1f2, v498V1f2
    0x49eS0x1f2: SSTORE v47aV1f2(0x0), v49aV1f2
    0x4a1S0x1f2: v4a1V1f2 = AND v481V1f2, v495V1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4a4S0x1f2: SSTORE v47eV1f2(0x1), v4a1V1f2
    0x4a5S0x1f2: v4a5V1f2(0x40) = CONST 
    0x4a8S0x1f2: v4a8V1f2 = MLOAD v4a5V1f2(0x40)
    0x4abS0x1f2: v4abV1f2 = AND v489V1f2(0xffffffffffffffffffffffffffffffffffffffff), v47dV1f2
    0x4aeS0x1f2: MSTORE v4a8V1f2, v4abV1f2
    0x4b2S0x1f2: v4b2V1f2 = AND v489V1f2(0xffffffffffffffffffffffffffffffffffffffff), v49aV1f2
    0x4b3S0x1f2: v4b3V1f2(0x20) = CONST 
    0x4b6S0x1f2: v4b6V1f2 = ADD v4a8V1f2, v4b3V1f2(0x20)
    0x4b7S0x1f2: MSTORE v4b6V1f2, v4b2V1f2
    0x4b9S0x1f2: v4b9V1f2 = MLOAD v4a5V1f2(0x40)
    0x4bcS0x1f2: v4bcV1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x4e1S0x1f2: v4e1V1f2(0x0) = SUB v4a8V1f2, v4b9V1f2
    0x4e2S0x1f2: v4e2V1f2(0x40) = ADD v4e1V1f2(0x0), v4a5V1f2(0x40)
    0x4e4S0x1f2: LOG1 v4b9V1f2, v4e2V1f2(0x40), v4bcV1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x4e5S0x1f2: v4e5V1f2(0x1) = CONST 
    0x4e7S0x1f2: v4e7V1f2 = SLOAD v4e5V1f2(0x1)
    0x4e8S0x1f2: v4e8V1f2(0x40) = CONST 
    0x4ebS0x1f2: v4ebV1f2 = MLOAD v4e8V1f2(0x40)
    0x4ecS0x1f2: v4ecV1f2(0x1) = CONST 
    0x4eeS0x1f2: v4eeV1f2(0x1) = CONST 
    0x4f0S0x1f2: v4f0V1f2(0xa0) = CONST 
    0x4f2S0x1f2: v4f2V1f2(0x10000000000000000000000000000000000000000) = SHL v4f0V1f2(0xa0), v4eeV1f2(0x1)
    0x4f3S0x1f2: v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f2V1f2(0x10000000000000000000000000000000000000000), v4ecV1f2(0x1)
    0x4f6S0x1f2: v4f6V1f2 = AND v48cV1f2, v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f8S0x1f2: MSTORE v4ebV1f2, v4f6V1f2
    0x4fbS0x1f2: v4fbV1f2 = AND v4e7V1f2, v4f3V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4fcS0x1f2: v4fcV1f2(0x20) = CONST 
    0x4ffS0x1f2: v4ffV1f2 = ADD v4ebV1f2, v4fcV1f2(0x20)
    0x500S0x1f2: MSTORE v4ffV1f2, v4fbV1f2
    0x502S0x1f2: v502V1f2 = MLOAD v4e8V1f2(0x40)
    0x503S0x1f2: v503V1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x527S0x1f2: v527V1f2(0x0) = SUB v4ebV1f2, v502V1f2
    0x52aS0x1f2: v52aV1f2(0x40) = ADD v4e8V1f2(0x40), v527V1f2(0x0)
    0x52cS0x1f2: LOG1 v502V1f2, v52aV1f2(0x40), v503V1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x52dS0x1f2: v52dV1f2(0x0) = CONST 
    0x52fS0x1f2: v52fV1f2(0x3c1) = CONST 
    0x532S0x1f2: JUMP v52fV1f2(0x3c1)

    Begin block 0x3c10x44dB0x1f2
    prev=[0x479B0x1f2], succ=[0x3c60x44dB0x1f2]
    =================================

    Begin block 0x465B0x1f2
    prev=[0x44dB0x1f2], succ=[0x468B0x1f2]
    =================================
    0x466S0x1f2: v466V1f2 = CALLER 
    0x467S0x1f2: v467V1f2 = ISZERO v466V1f2

}

function admin()() public {
    Begin block 0x1fb
    prev=[], succ=[0x203, 0x207]
    =================================
    0x1fc: v1fc = CALLVALUE 
    0x1fe: v1fe = ISZERO v1fc
    0x1ff: v1ff(0x207) = CONST 
    0x202: JUMPI v1ff(0x207), v1fe

    Begin block 0x203
    prev=[0x1fb], succ=[]
    =================================
    0x203: v203(0x0) = CONST 
    0x206: REVERT v203(0x0), v203(0x0)

    Begin block 0x207
    prev=[0x1fb], succ=[0x533]
    =================================
    0x209: v209(0x778) = CONST 
    0x20c: v20c(0x533) = CONST 
    0x20f: JUMP v20c(0x533)

    Begin block 0x533
    prev=[0x207], succ=[0x778]
    =================================
    0x534: v534(0x0) = CONST 
    0x536: v536 = SLOAD v534(0x0)
    0x537: v537(0x1) = CONST 
    0x539: v539(0x1) = CONST 
    0x53b: v53b(0xa0) = CONST 
    0x53d: v53d(0x10000000000000000000000000000000000000000) = SHL v53b(0xa0), v539(0x1)
    0x53e: v53e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53d(0x10000000000000000000000000000000000000000), v537(0x1)
    0x53f: v53f = AND v53e(0xffffffffffffffffffffffffffffffffffffffff), v536
    0x541: JUMP v209(0x778)

    Begin block 0x778
    prev=[0x533], succ=[]
    =================================
    0x779: v779(0x40) = CONST 
    0x77c: v77c = MLOAD v779(0x40)
    0x77d: v77d(0x1) = CONST 
    0x77f: v77f(0x1) = CONST 
    0x781: v781(0xa0) = CONST 
    0x783: v783(0x10000000000000000000000000000000000000000) = SHL v781(0xa0), v77f(0x1)
    0x784: v784(0xffffffffffffffffffffffffffffffffffffffff) = SUB v783(0x10000000000000000000000000000000000000000), v77d(0x1)
    0x787: v787 = AND v53f, v784(0xffffffffffffffffffffffffffffffffffffffff)
    0x789: MSTORE v77c, v787
    0x78a: v78a = MLOAD v779(0x40)
    0x78e: v78e(0x0) = SUB v77c, v78a
    0x78f: v78f(0x20) = CONST 
    0x791: v791(0x20) = ADD v78f(0x20), v78e(0x0)
    0x793: RETURN v78a, v791(0x20)

}

function 0x542(0x542arg0x0, 0x542arg0x1, 0x542arg0x2) private {
    Begin block 0x542
    prev=[], succ=[0x570, 0x571]
    =================================
    0x543: v543(0x0) = CONST 
    0x545: v545(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0) = CONST 
    0x567: v567(0x1) = CONST 
    0x56a: v56a = GT v542arg1, v567(0x1)
    0x56b: v56b = ISZERO v56a
    0x56c: v56c(0x571) = CONST 
    0x56f: JUMPI v56c(0x571), v56b

    Begin block 0x570
    prev=[0x542], succ=[]
    =================================
    0x570: THROW 

    Begin block 0x571
    prev=[0x542], succ=[0x57c, 0x57d]
    =================================
    0x573: v573(0x3) = CONST 
    0x576: v576 = GT v542arg0, v573(0x3)
    0x577: v577 = ISZERO v576
    0x578: v578(0x57d) = CONST 
    0x57b: JUMPI v578(0x57d), v577

    Begin block 0x57c
    prev=[0x571], succ=[]
    =================================
    0x57c: THROW 

    Begin block 0x57d
    prev=[0x571], succ=[0x5a7, 0x5a8]
    =================================
    0x57e: v57e(0x40) = CONST 
    0x581: v581 = MLOAD v57e(0x40)
    0x584: MSTORE v581, v542arg1
    0x585: v585(0x20) = CONST 
    0x588: v588 = ADD v581, v585(0x20)
    0x58c: MSTORE v588, v542arg0
    0x58d: v58d(0x0) = CONST 
    0x591: v591 = ADD v57e(0x40), v581
    0x592: MSTORE v591, v58d(0x0)
    0x593: v593 = MLOAD v57e(0x40)
    0x597: v597(0x0) = SUB v581, v593
    0x598: v598(0x60) = CONST 
    0x59a: v59a(0x60) = ADD v598(0x60), v597(0x0)
    0x59c: LOG1 v593, v59a(0x60), v545(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0)
    0x59e: v59e(0x1) = CONST 
    0x5a1: v5a1 = GT v542arg1, v59e(0x1)
    0x5a2: v5a2 = ISZERO v5a1
    0x5a3: v5a3(0x5a8) = CONST 
    0x5a6: JUMPI v5a3(0x5a8), v5a2

    Begin block 0x5a7
    prev=[0x57d], succ=[]
    =================================
    0x5a7: THROW 

    Begin block 0x5a8
    prev=[0x57d], succ=[]
    =================================
    0x5ae: RETURNPRIVATE v542arg2, v542arg1

}

function fallback()() public {
    Begin block 0x7b
    prev=[], succ=[0xbd, 0xde]
    =================================
    0x7c: v7c(0x2) = CONST 
    0x7e: v7e = SLOAD v7c(0x2)
    0x7f: v7f(0x40) = CONST 
    0x81: v81 = MLOAD v7f(0x40)
    0x82: v82(0x0) = CONST 
    0x85: v85(0x1) = CONST 
    0x87: v87(0x1) = CONST 
    0x89: v89(0xa0) = CONST 
    0x8b: v8b(0x10000000000000000000000000000000000000000) = SHL v89(0xa0), v87(0x1)
    0x8c: v8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8b(0x10000000000000000000000000000000000000000), v85(0x1)
    0x8d: v8d = AND v8c(0xffffffffffffffffffffffffffffffffffffffff), v7e
    0x91: v91 = CALLDATASIZE 
    0x99: CALLDATACOPY v81, v82(0x0), v91
    0x9a: v9a(0x40) = CONST 
    0x9c: v9c = MLOAD v9a(0x40)
    0x9e: v9e = ADD v81, v91
    0xa1: va1(0x0) = CONST 
    0xab: vab = SUB v9e, v9c
    0xae: vae = GAS 
    0xaf: vaf = DELEGATECALL vae, v8d, v9c, vab, v9c, va1(0x0)
    0xb3: vb3 = RETURNDATASIZE 
    0xb5: vb5(0x0) = CONST 
    0xb8: vb8 = EQ vb3, vb5(0x0)
    0xb9: vb9(0xde) = CONST 
    0xbc: JUMPI vb9(0xde), vb8

    Begin block 0xbd
    prev=[0x7b], succ=[0xe3]
    =================================
    0xbd: vbd(0x40) = CONST 
    0xbf: vbf = MLOAD vbd(0x40)
    0xc2: vc2(0x1f) = CONST 
    0xc4: vc4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vc2(0x1f)
    0xc5: vc5(0x3f) = CONST 
    0xc7: vc7 = RETURNDATASIZE 
    0xc8: vc8 = ADD vc7, vc5(0x3f)
    0xc9: vc9 = AND vc8, vc4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xcb: vcb = ADD vbf, vc9
    0xcc: vcc(0x40) = CONST 
    0xce: MSTORE vcc(0x40), vcb
    0xcf: vcf = RETURNDATASIZE 
    0xd1: MSTORE vbf, vcf
    0xd2: vd2 = RETURNDATASIZE 
    0xd3: vd3(0x0) = CONST 
    0xd5: vd5(0x20) = CONST 
    0xd8: vd8 = ADD vbf, vd5(0x20)
    0xd9: RETURNDATACOPY vd8, vd3(0x0), vd2
    0xda: vda(0xe3) = CONST 
    0xdd: JUMP vda(0xe3)

    Begin block 0xe3
    prev=[0xbd, 0xde], succ=[0xf7, 0xfa]
    =================================
    0xe8: ve8(0x40) = CONST 
    0xea: vea = MLOAD ve8(0x40)
    0xeb: veb = RETURNDATASIZE 
    0xec: vec(0x0) = CONST 
    0xef: RETURNDATACOPY vea, vec(0x0), veb
    0xf2: vf2 = ISZERO vaf
    0xf3: vf3(0xfa) = CONST 
    0xf6: JUMPI vf3(0xfa), vf2

    Begin block 0xf7
    prev=[0xe3], succ=[]
    =================================
    0xf7: vf7 = RETURNDATASIZE 
    0xf9: RETURN vea, vf7

    Begin block 0xfa
    prev=[0xe3], succ=[]
    =================================
    0xfb: vfb = RETURNDATASIZE 
    0xfd: REVERT vea, vfb

    Begin block 0xde
    prev=[0x7b], succ=[0xe3]
    =================================
    0xdf: vdf(0x60) = CONST 

}

function pendingAdmin()() public {
    Begin block 0xfe
    prev=[], succ=[0x106, 0x10a]
    =================================
    0xff: vff = CALLVALUE 
    0x101: v101 = ISZERO vff
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xfe], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xfe], succ=[0x210]
    =================================
    0x10c: v10c(0x603) = CONST 
    0x10f: v10f(0x210) = CONST 
    0x112: JUMP v10f(0x210)

    Begin block 0x210
    prev=[0x10a], succ=[0x603]
    =================================
    0x211: v211(0x1) = CONST 
    0x213: v213 = SLOAD v211(0x1)
    0x214: v214(0x1) = CONST 
    0x216: v216(0x1) = CONST 
    0x218: v218(0xa0) = CONST 
    0x21a: v21a(0x10000000000000000000000000000000000000000) = SHL v218(0xa0), v216(0x1)
    0x21b: v21b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21a(0x10000000000000000000000000000000000000000), v214(0x1)
    0x21c: v21c = AND v21b(0xffffffffffffffffffffffffffffffffffffffff), v213
    0x21e: JUMP v10c(0x603)

    Begin block 0x603
    prev=[0x210], succ=[]
    =================================
    0x604: v604(0x40) = CONST 
    0x607: v607 = MLOAD v604(0x40)
    0x608: v608(0x1) = CONST 
    0x60a: v60a(0x1) = CONST 
    0x60c: v60c(0xa0) = CONST 
    0x60e: v60e(0x10000000000000000000000000000000000000000) = SHL v60c(0xa0), v60a(0x1)
    0x60f: v60f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v60e(0x10000000000000000000000000000000000000000), v608(0x1)
    0x612: v612 = AND v21c, v60f(0xffffffffffffffffffffffffffffffffffffffff)
    0x614: MSTORE v607, v612
    0x615: v615 = MLOAD v604(0x40)
    0x619: v619(0x0) = SUB v607, v615
    0x61a: v61a(0x20) = CONST 
    0x61c: v61c(0x20) = ADD v61a(0x20), v619(0x0)
    0x61e: RETURN v615, v61c(0x20)

}

