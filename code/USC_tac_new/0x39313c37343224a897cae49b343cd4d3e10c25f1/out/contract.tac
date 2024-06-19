function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x858]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x846: v846(0x858) = CONST 
    0x847: JUMPI v846(0x858), v8

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
    prev=[0xd], succ=[0x85b, 0x5a]
    =================================
    0x50: v50(0x26782247) = CONST 
    0x55: v55 = EQ v50(0x26782247), v12
    0x850: v850(0x85b) = CONST 
    0x851: JUMPI v850(0x85b), v55

    Begin block 0x85b
    prev=[0x4e], succ=[]
    =================================
    0x85c: v85c(0xfe) = CONST 
    0x85d: CALLPRIVATE v85c(0xfe)

    Begin block 0x5a
    prev=[0x4e], succ=[0x85e, 0x65]
    =================================
    0x5b: v5b(0x8e6c0959) = CONST 
    0x60: v60 = EQ v5b(0x8e6c0959), v12
    0x852: v852(0x85e) = CONST 
    0x853: JUMPI v852(0x85e), v60

    Begin block 0x85e
    prev=[0x5a], succ=[]
    =================================
    0x85f: v85f(0x12f) = CONST 
    0x860: CALLPRIVATE v85f(0x12f)

    Begin block 0x65
    prev=[0x5a], succ=[0x861, 0x70]
    =================================
    0x66: v66(0x9788e731) = CONST 
    0x6b: v6b = EQ v66(0x9788e731), v12
    0x854: v854(0x861) = CONST 
    0x855: JUMPI v854(0x861), v6b

    Begin block 0x861
    prev=[0x65], succ=[]
    =================================
    0x862: v862(0x144) = CONST 
    0x863: CALLPRIVATE v862(0x144)

    Begin block 0x70
    prev=[0x65], succ=[0x858, 0x864]
    =================================
    0x71: v71(0xb71d1a0c) = CONST 
    0x76: v76 = EQ v71(0xb71d1a0c), v12
    0x856: v856(0x864) = CONST 
    0x857: JUMPI v856(0x864), v76

    Begin block 0x858
    prev=[0x0, 0x70], succ=[]
    =================================
    0x859: v859(0x7b) = CONST 
    0x85a: CALLPRIVATE v859(0x7b)

    Begin block 0x864
    prev=[0x70], succ=[]
    =================================
    0x865: v865(0x159) = CONST 
    0x866: CALLPRIVATE v865(0x159)

    Begin block 0x1e
    prev=[0xd], succ=[0x867, 0x29]
    =================================
    0x1f: v1f(0xc1e80334) = CONST 
    0x24: v24 = EQ v1f(0xc1e80334), v12
    0x848: v848(0x867) = CONST 
    0x849: JUMPI v848(0x867), v24

    Begin block 0x867
    prev=[0x1e], succ=[]
    =================================
    0x868: v868(0x19e) = CONST 
    0x869: CALLPRIVATE v868(0x19e)

    Begin block 0x29
    prev=[0x1e], succ=[0x86a, 0x34]
    =================================
    0x2a: v2a(0xe992a041) = CONST 
    0x2f: v2f = EQ v2a(0xe992a041), v12
    0x84a: v84a(0x86a) = CONST 
    0x84b: JUMPI v84a(0x86a), v2f

    Begin block 0x86a
    prev=[0x29], succ=[]
    =================================
    0x86b: v86b(0x1b3) = CONST 
    0x86c: CALLPRIVATE v86b(0x1b3)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x86d]
    =================================
    0x35: v35(0xe9c714f2) = CONST 
    0x3a: v3a = EQ v35(0xe9c714f2), v12
    0x84c: v84c(0x86d) = CONST 
    0x84d: JUMPI v84c(0x86d), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x870]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x84e: v84e(0x870) = CONST 
    0x84f: JUMPI v84e(0x870), v45

    Begin block 0x4a
    prev=[0x3f], succ=[]
    =================================
    0x4a: v4a(0x7b) = CONST 
    0x4d: JUMP v4a(0x7b)

    Begin block 0x870
    prev=[0x3f], succ=[]
    =================================
    0x871: v871(0x1fb) = CONST 
    0x872: CALLPRIVATE v871(0x1fb)

    Begin block 0x86d
    prev=[0x34], succ=[]
    =================================
    0x86e: v86e(0x1e6) = CONST 
    0x86f: CALLPRIVATE v86e(0x1e6)

}

function controllerImplementation()() public {
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
    0x13d: v13d(0x6f0) = CONST 
    0x140: v140(0x21f) = CONST 
    0x143: JUMP v140(0x21f)

    Begin block 0x21f
    prev=[0x13b], succ=[0x6f0]
    =================================
    0x220: v220(0x2) = CONST 
    0x222: v222 = SLOAD v220(0x2)
    0x223: v223(0x1) = CONST 
    0x225: v225(0x1) = CONST 
    0x227: v227(0xa0) = CONST 
    0x229: v229(0x10000000000000000000000000000000000000000) = SHL v227(0xa0), v225(0x1)
    0x22a: v22a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v229(0x10000000000000000000000000000000000000000), v223(0x1)
    0x22b: v22b = AND v22a(0xffffffffffffffffffffffffffffffffffffffff), v222
    0x22d: JUMP v13d(0x6f0)

    Begin block 0x6f0
    prev=[0x21f], succ=[]
    =================================
    0x6f1: v6f1(0x40) = CONST 
    0x6f4: v6f4 = MLOAD v6f1(0x40)
    0x6f5: v6f5(0x1) = CONST 
    0x6f7: v6f7(0x1) = CONST 
    0x6f9: v6f9(0xa0) = CONST 
    0x6fb: v6fb(0x10000000000000000000000000000000000000000) = SHL v6f9(0xa0), v6f7(0x1)
    0x6fc: v6fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6fb(0x10000000000000000000000000000000000000000), v6f5(0x1)
    0x6ff: v6ff = AND v22b, v6fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x701: MSTORE v6f4, v6ff
    0x702: v702 = MLOAD v6f1(0x40)
    0x706: v706(0x0) = SUB v6f4, v702
    0x707: v707(0x20) = CONST 
    0x709: v709(0x20) = ADD v707(0x20), v706(0x0)
    0x70b: RETURN v702, v709(0x20)

}

function pendingControllerImplementation()() public {
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
    0x152: v152(0x72b) = CONST 
    0x155: v155(0x22e) = CONST 
    0x158: JUMP v155(0x22e)

    Begin block 0x22e
    prev=[0x150], succ=[0x72b]
    =================================
    0x22f: v22f(0x3) = CONST 
    0x231: v231 = SLOAD v22f(0x3)
    0x232: v232(0x1) = CONST 
    0x234: v234(0x1) = CONST 
    0x236: v236(0xa0) = CONST 
    0x238: v238(0x10000000000000000000000000000000000000000) = SHL v236(0xa0), v234(0x1)
    0x239: v239(0xffffffffffffffffffffffffffffffffffffffff) = SUB v238(0x10000000000000000000000000000000000000000), v232(0x1)
    0x23a: v23a = AND v239(0xffffffffffffffffffffffffffffffffffffffff), v231
    0x23c: JUMP v152(0x72b)

    Begin block 0x72b
    prev=[0x22e], succ=[]
    =================================
    0x72c: v72c(0x40) = CONST 
    0x72f: v72f = MLOAD v72c(0x40)
    0x730: v730(0x1) = CONST 
    0x732: v732(0x1) = CONST 
    0x734: v734(0xa0) = CONST 
    0x736: v736(0x10000000000000000000000000000000000000000) = SHL v734(0xa0), v732(0x1)
    0x737: v737(0xffffffffffffffffffffffffffffffffffffffff) = SUB v736(0x10000000000000000000000000000000000000000), v730(0x1)
    0x73a: v73a = AND v23a, v737(0xffffffffffffffffffffffffffffffffffffffff)
    0x73c: MSTORE v72f, v73a
    0x73d: v73d = MLOAD v72c(0x40)
    0x741: v741(0x0) = SUB v72f, v73d
    0x742: v742(0x20) = CONST 
    0x744: v744(0x20) = ADD v742(0x20), v741(0x0)
    0x746: RETURN v73d, v744(0x20)

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
    0x167: v167(0x766) = CONST 
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
    0x256: v256(0xe) = CONST 
    0x258: v258(0x54b) = CONST 
    0x25b: v25b_0 = CALLPRIVATE v258(0x54b), v256(0xe), v254(0x1), v251(0x25c)

    Begin block 0x25c0x159
    prev=[0x251], succ=[0x2c90x159]
    =================================
    0x25f0x159: v15925f(0x2c9) = CONST 
    0x2620x159: JUMP v15925f(0x2c9)

    Begin block 0x2c90x159
    prev=[0x25c0x159, 0x2c50x159], succ=[0x766]
    =================================
    0x2cd0x159: JUMP v167(0x766)

    Begin block 0x766
    prev=[0x2c90x159], succ=[]
    =================================
    0x766_0x0: v766_0 = PHI v2c3(0x0), v25b_0
    0x767: v767(0x40) = CONST 
    0x76a: v76a = MLOAD v767(0x40)
    0x76d: MSTORE v76a, v766_0
    0x76e: v76e = MLOAD v767(0x40)
    0x772: v772(0x0) = SUB v76a, v76e
    0x773: v773(0x20) = CONST 
    0x775: v775(0x20) = ADD v773(0x20), v772(0x0)
    0x777: RETURN v76e, v775(0x20)

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
    0x1ac: v1ac(0x797) = CONST 
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
    0x300S0x1aa: v300V1aa(0x54b) = CONST 
    0x303S0x1aa: v303_0V1aa = CALLPRIVATE v300V1aa(0x54b), v2fdV1aa(0x1), v2fdV1aa(0x1), v2faV1aa(0x304)

    Begin block 0x3040x2ceB0x1aa
    prev=[0x2faB0x1aa], succ=[0x3c60x2ceB0x1aa]
    =================================
    0x3070x2ceS0x1aa: v2ce307V1aa(0x3c6) = CONST 
    0x30a0x2ceS0x1aa: JUMP v2ce307V1aa(0x3c6)

    Begin block 0x3c60x2ceB0x1aa
    prev=[0x3040x2ceB0x1aa, 0x3c10x2ceB0x1aa], succ=[0x797]
    =================================
    0x3c60x2ce_0x0S0x1aa: v3c62ce_0V1aa = PHI v303_0V1aa, v3bfV1aa(0x0)
    0x3c80x2ceS0x1aa: JUMP v1ac(0x797)

    Begin block 0x797
    prev=[0x3c60x2ceB0x1aa], succ=[]
    =================================
    0x798: v798(0x40) = CONST 
    0x79b: v79b = MLOAD v798(0x40)
    0x79e: MSTORE v79b, v3c62ce_0V1aa
    0x79f: v79f = MLOAD v798(0x40)
    0x7a3: v7a3(0x0) = SUB v79b, v79f
    0x7a4: v7a4(0x20) = CONST 
    0x7a6: v7a6(0x20) = ADD v7a4(0x20), v7a3(0x0)
    0x7a8: RETURN v79f, v7a6(0x20)

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
    0x1c1: v1c1(0x7c8) = CONST 
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
    0x3e2: v3e2(0xf) = CONST 
    0x3e4: v3e4(0x54b) = CONST 
    0x3e7: v3e7_0 = CALLPRIVATE v3e4(0x54b), v3e2(0xf), v3e0(0x1), v3dd(0x25c)

    Begin block 0x25c0x1b3
    prev=[0x3dd], succ=[0x2c90x1b3]
    =================================
    0x25f0x1b3: v1b325f(0x2c9) = CONST 
    0x2620x1b3: JUMP v1b325f(0x2c9)

    Begin block 0x2c90x1b3
    prev=[0x25c0x1b3, 0x2c50x1b3], succ=[0x7c8]
    =================================
    0x2cd0x1b3: JUMP v1c1(0x7c8)

    Begin block 0x7c8
    prev=[0x2c90x1b3], succ=[]
    =================================
    0x7c8_0x0: v7c8_0 = PHI v450(0x0), v3e7_0
    0x7c9: v7c9(0x40) = CONST 
    0x7cc: v7cc = MLOAD v7c9(0x40)
    0x7cf: MSTORE v7cc, v7c8_0
    0x7d0: v7d0 = MLOAD v7c9(0x40)
    0x7d4: v7d4(0x0) = SUB v7cc, v7d0
    0x7d5: v7d5(0x20) = CONST 
    0x7d7: v7d7(0x20) = ADD v7d5(0x20), v7d4(0x0)
    0x7d9: RETURN v7d0, v7d7(0x20)

    Begin block 0x3e8
    prev=[0x3c9], succ=[0x5b8]
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
    0x447: v447(0x44f) = CONST 
    0x44b: v44b(0x5b8) = CONST 
    0x44e: JUMP v44b(0x5b8)

    Begin block 0x5b8
    prev=[0x3e8], succ=[0x620]
    =================================
    0x5b9: v5b9(0x5c1) = CONST 
    0x5bd: v5bd(0x620) = CONST 
    0x5c0: JUMP v5bd(0x620)

    Begin block 0x620
    prev=[0x5b8], succ=[0x5c1]
    =================================
    0x621: v621 = EXTCODESIZE v1e1
    0x622: v622 = ISZERO v621
    0x623: v623 = ISZERO v622
    0x625: JUMP v5b9(0x5c1)

    Begin block 0x5c1
    prev=[0x620], succ=[0x5c6, 0x5fc]
    =================================
    0x5c2: v5c2(0x5fc) = CONST 
    0x5c5: JUMPI v5c2(0x5fc), v623

    Begin block 0x5c6
    prev=[0x5c1], succ=[]
    =================================
    0x5c6: v5c6(0x40) = CONST 
    0x5c8: v5c8 = MLOAD v5c6(0x40)
    0x5c9: v5c9(0x461bcd) = CONST 
    0x5cd: v5cd(0xe5) = CONST 
    0x5cf: v5cf(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5cd(0xe5), v5c9(0x461bcd)
    0x5d1: MSTORE v5c8, v5cf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5d2: v5d2(0x4) = CONST 
    0x5d4: v5d4 = ADD v5d2(0x4), v5c8
    0x5d7: v5d7(0x20) = CONST 
    0x5d9: v5d9 = ADD v5d7(0x20), v5d4
    0x5dc: v5dc(0x20) = SUB v5d9, v5d4
    0x5de: MSTORE v5d4, v5dc(0x20)
    0x5df: v5df(0x3b) = CONST 
    0x5e2: MSTORE v5d9, v5df(0x3b)
    0x5e3: v5e3(0x20) = CONST 
    0x5e5: v5e5 = ADD v5e3(0x20), v5d9
    0x5e7: v5e7(0x627) = CONST 
    0x5ea: v5ea(0x3b) = CONST 
    0x5ed: CODECOPY v5e5, v5e7(0x627), v5ea(0x3b)
    0x5ee: v5ee(0x40) = CONST 
    0x5f0: v5f0 = ADD v5ee(0x40), v5e5
    0x5f4: v5f4(0x40) = CONST 
    0x5f6: v5f6 = MLOAD v5f4(0x40)
    0x5f9: v5f9(0x84) = SUB v5f0, v5f6
    0x5fb: REVERT v5f6, v5f9(0x84)

    Begin block 0x5fc
    prev=[0x5c1], succ=[0x44f]
    =================================
    0x5fd: v5fd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x61e: SSTORE v5fd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v1e1
    0x61f: JUMP v447(0x44f)

    Begin block 0x44f
    prev=[0x5fc], succ=[0x2c50x1b3]
    =================================
    0x450: v450(0x0) = CONST 
    0x452: v452(0x2c5) = CONST 
    0x455: JUMP v452(0x2c5)

    Begin block 0x2c50x1b3
    prev=[0x44f], succ=[0x2c90x1b3]
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
    prev=[0x1e6], succ=[0x456B0x1f2]
    =================================
    0x1f4: v1f4(0x7f9) = CONST 
    0x1f7: v1f7(0x456) = CONST 
    0x1fa: JUMP v1f7(0x456)

    Begin block 0x456B0x1f2
    prev=[0x1f2], succ=[0x471B0x1f2, 0x46eB0x1f2]
    =================================
    0x457S0x1f2: v457V1f2(0x1) = CONST 
    0x459S0x1f2: v459V1f2 = SLOAD v457V1f2(0x1)
    0x45aS0x1f2: v45aV1f2(0x0) = CONST 
    0x45dS0x1f2: v45dV1f2(0x1) = CONST 
    0x45fS0x1f2: v45fV1f2(0x1) = CONST 
    0x461S0x1f2: v461V1f2(0xa0) = CONST 
    0x463S0x1f2: v463V1f2(0x10000000000000000000000000000000000000000) = SHL v461V1f2(0xa0), v45fV1f2(0x1)
    0x464S0x1f2: v464V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v463V1f2(0x10000000000000000000000000000000000000000), v45dV1f2(0x1)
    0x465S0x1f2: v465V1f2 = AND v464V1f2(0xffffffffffffffffffffffffffffffffffffffff), v459V1f2
    0x466S0x1f2: v466V1f2 = CALLER 
    0x467S0x1f2: v467V1f2 = EQ v466V1f2, v465V1f2
    0x468S0x1f2: v468V1f2 = ISZERO v467V1f2
    0x46aS0x1f2: v46aV1f2(0x471) = CONST 
    0x46dS0x1f2: JUMPI v46aV1f2(0x471), v468V1f2

    Begin block 0x471B0x1f2
    prev=[0x456B0x1f2, 0x46eB0x1f2], succ=[0x477B0x1f2, 0x482B0x1f2]
    =================================
    0x471_0x0S0x1f2: v471_0V1f2 = PHI v468V1f2, v470V1f2
    0x472S0x1f2: v472V1f2 = ISZERO v471_0V1f2
    0x473S0x1f2: v473V1f2(0x482) = CONST 
    0x476S0x1f2: JUMPI v473V1f2(0x482), v472V1f2

    Begin block 0x477B0x1f2
    prev=[0x471B0x1f2], succ=[0x3040x456B0x1f2]
    =================================
    0x477S0x1f2: v477V1f2(0x304) = CONST 
    0x47aS0x1f2: v47aV1f2(0x1) = CONST 
    0x47cS0x1f2: v47cV1f2(0x0) = CONST 
    0x47eS0x1f2: v47eV1f2(0x54b) = CONST 
    0x481S0x1f2: v481_0V1f2 = CALLPRIVATE v47eV1f2(0x54b), v47cV1f2(0x0), v47aV1f2(0x1), v477V1f2(0x304)

    Begin block 0x3040x456B0x1f2
    prev=[0x477B0x1f2], succ=[0x3c60x456B0x1f2]
    =================================
    0x3070x456S0x1f2: v456307V1f2(0x3c6) = CONST 
    0x30a0x456S0x1f2: JUMP v456307V1f2(0x3c6)

    Begin block 0x3c60x456B0x1f2
    prev=[0x3040x456B0x1f2, 0x3c10x456B0x1f2], succ=[0x7f9]
    =================================
    0x3c60x456_0x0S0x1f2: v3c6456_0V1f2 = PHI v481_0V1f2, v536V1f2(0x0)
    0x3c80x456S0x1f2: JUMP v1f4(0x7f9)

    Begin block 0x7f9
    prev=[0x3c60x456B0x1f2], succ=[]
    =================================
    0x7fa: v7fa(0x40) = CONST 
    0x7fd: v7fd = MLOAD v7fa(0x40)
    0x800: MSTORE v7fd, v3c6456_0V1f2
    0x801: v801 = MLOAD v7fa(0x40)
    0x805: v805(0x0) = SUB v7fd, v801
    0x806: v806(0x20) = CONST 
    0x808: v808(0x20) = ADD v806(0x20), v805(0x0)
    0x80a: RETURN v801, v808(0x20)

    Begin block 0x482B0x1f2
    prev=[0x471B0x1f2], succ=[0x3c10x456B0x1f2]
    =================================
    0x483S0x1f2: v483V1f2(0x0) = CONST 
    0x486S0x1f2: v486V1f2 = SLOAD v483V1f2(0x0)
    0x487S0x1f2: v487V1f2(0x1) = CONST 
    0x48aS0x1f2: v48aV1f2 = SLOAD v487V1f2(0x1)
    0x48bS0x1f2: v48bV1f2(0x1) = CONST 
    0x48dS0x1f2: v48dV1f2(0x1) = CONST 
    0x48fS0x1f2: v48fV1f2(0xa0) = CONST 
    0x491S0x1f2: v491V1f2(0x10000000000000000000000000000000000000000) = SHL v48fV1f2(0xa0), v48dV1f2(0x1)
    0x492S0x1f2: v492V1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v491V1f2(0x10000000000000000000000000000000000000000), v48bV1f2(0x1)
    0x495S0x1f2: v495V1f2 = AND v48aV1f2, v492V1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x496S0x1f2: v496V1f2(0x1) = CONST 
    0x498S0x1f2: v498V1f2(0x1) = CONST 
    0x49aS0x1f2: v49aV1f2(0xa0) = CONST 
    0x49cS0x1f2: v49cV1f2(0x10000000000000000000000000000000000000000) = SHL v49aV1f2(0xa0), v498V1f2(0x1)
    0x49dS0x1f2: v49dV1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49cV1f2(0x10000000000000000000000000000000000000000), v496V1f2(0x1)
    0x49eS0x1f2: v49eV1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v49dV1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4a1S0x1f2: v4a1V1f2 = AND v486V1f2, v49eV1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4a3S0x1f2: v4a3V1f2 = OR v495V1f2, v4a1V1f2
    0x4a7S0x1f2: SSTORE v483V1f2(0x0), v4a3V1f2
    0x4aaS0x1f2: v4aaV1f2 = AND v48aV1f2, v49eV1f2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x4adS0x1f2: SSTORE v487V1f2(0x1), v4aaV1f2
    0x4aeS0x1f2: v4aeV1f2(0x40) = CONST 
    0x4b1S0x1f2: v4b1V1f2 = MLOAD v4aeV1f2(0x40)
    0x4b4S0x1f2: v4b4V1f2 = AND v492V1f2(0xffffffffffffffffffffffffffffffffffffffff), v486V1f2
    0x4b7S0x1f2: MSTORE v4b1V1f2, v4b4V1f2
    0x4bbS0x1f2: v4bbV1f2 = AND v492V1f2(0xffffffffffffffffffffffffffffffffffffffff), v4a3V1f2
    0x4bcS0x1f2: v4bcV1f2(0x20) = CONST 
    0x4bfS0x1f2: v4bfV1f2 = ADD v4b1V1f2, v4bcV1f2(0x20)
    0x4c0S0x1f2: MSTORE v4bfV1f2, v4bbV1f2
    0x4c2S0x1f2: v4c2V1f2 = MLOAD v4aeV1f2(0x40)
    0x4c5S0x1f2: v4c5V1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc) = CONST 
    0x4eaS0x1f2: v4eaV1f2(0x0) = SUB v4b1V1f2, v4c2V1f2
    0x4ebS0x1f2: v4ebV1f2(0x40) = ADD v4eaV1f2(0x0), v4aeV1f2(0x40)
    0x4edS0x1f2: LOG1 v4c2V1f2, v4ebV1f2(0x40), v4c5V1f2(0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc)
    0x4eeS0x1f2: v4eeV1f2(0x1) = CONST 
    0x4f0S0x1f2: v4f0V1f2 = SLOAD v4eeV1f2(0x1)
    0x4f1S0x1f2: v4f1V1f2(0x40) = CONST 
    0x4f4S0x1f2: v4f4V1f2 = MLOAD v4f1V1f2(0x40)
    0x4f5S0x1f2: v4f5V1f2(0x1) = CONST 
    0x4f7S0x1f2: v4f7V1f2(0x1) = CONST 
    0x4f9S0x1f2: v4f9V1f2(0xa0) = CONST 
    0x4fbS0x1f2: v4fbV1f2(0x10000000000000000000000000000000000000000) = SHL v4f9V1f2(0xa0), v4f7V1f2(0x1)
    0x4fcS0x1f2: v4fcV1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4fbV1f2(0x10000000000000000000000000000000000000000), v4f5V1f2(0x1)
    0x4ffS0x1f2: v4ffV1f2 = AND v495V1f2, v4fcV1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x501S0x1f2: MSTORE v4f4V1f2, v4ffV1f2
    0x504S0x1f2: v504V1f2 = AND v4f0V1f2, v4fcV1f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x505S0x1f2: v505V1f2(0x20) = CONST 
    0x508S0x1f2: v508V1f2 = ADD v4f4V1f2, v505V1f2(0x20)
    0x509S0x1f2: MSTORE v508V1f2, v504V1f2
    0x50bS0x1f2: v50bV1f2 = MLOAD v4f1V1f2(0x40)
    0x50cS0x1f2: v50cV1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9) = CONST 
    0x530S0x1f2: v530V1f2(0x0) = SUB v4f4V1f2, v50bV1f2
    0x533S0x1f2: v533V1f2(0x40) = ADD v4f1V1f2(0x40), v530V1f2(0x0)
    0x535S0x1f2: LOG1 v50bV1f2, v533V1f2(0x40), v50cV1f2(0xca4f2f25d0898edd99413412fb94012f9e54ec8142f9b093e7720646a95b16a9)
    0x536S0x1f2: v536V1f2(0x0) = CONST 
    0x538S0x1f2: v538V1f2(0x3c1) = CONST 
    0x53bS0x1f2: JUMP v538V1f2(0x3c1)

    Begin block 0x3c10x456B0x1f2
    prev=[0x482B0x1f2], succ=[0x3c60x456B0x1f2]
    =================================

    Begin block 0x46eB0x1f2
    prev=[0x456B0x1f2], succ=[0x471B0x1f2]
    =================================
    0x46fS0x1f2: v46fV1f2 = CALLER 
    0x470S0x1f2: v470V1f2 = ISZERO v46fV1f2

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
    prev=[0x1fb], succ=[0x53c]
    =================================
    0x209: v209(0x82a) = CONST 
    0x20c: v20c(0x53c) = CONST 
    0x20f: JUMP v20c(0x53c)

    Begin block 0x53c
    prev=[0x207], succ=[0x82a]
    =================================
    0x53d: v53d(0x0) = CONST 
    0x53f: v53f = SLOAD v53d(0x0)
    0x540: v540(0x1) = CONST 
    0x542: v542(0x1) = CONST 
    0x544: v544(0xa0) = CONST 
    0x546: v546(0x10000000000000000000000000000000000000000) = SHL v544(0xa0), v542(0x1)
    0x547: v547(0xffffffffffffffffffffffffffffffffffffffff) = SUB v546(0x10000000000000000000000000000000000000000), v540(0x1)
    0x548: v548 = AND v547(0xffffffffffffffffffffffffffffffffffffffff), v53f
    0x54a: JUMP v209(0x82a)

    Begin block 0x82a
    prev=[0x53c], succ=[]
    =================================
    0x82b: v82b(0x40) = CONST 
    0x82e: v82e = MLOAD v82b(0x40)
    0x82f: v82f(0x1) = CONST 
    0x831: v831(0x1) = CONST 
    0x833: v833(0xa0) = CONST 
    0x835: v835(0x10000000000000000000000000000000000000000) = SHL v833(0xa0), v831(0x1)
    0x836: v836(0xffffffffffffffffffffffffffffffffffffffff) = SUB v835(0x10000000000000000000000000000000000000000), v82f(0x1)
    0x839: v839 = AND v548, v836(0xffffffffffffffffffffffffffffffffffffffff)
    0x83b: MSTORE v82e, v839
    0x83c: v83c = MLOAD v82b(0x40)
    0x840: v840(0x0) = SUB v82e, v83c
    0x841: v841(0x20) = CONST 
    0x843: v843(0x20) = ADD v841(0x20), v840(0x0)
    0x845: RETURN v83c, v843(0x20)

}

function 0x54b(0x54barg0x0, 0x54barg0x1, 0x54barg0x2) private {
    Begin block 0x54b
    prev=[], succ=[0x579, 0x57a]
    =================================
    0x54c: v54c(0x0) = CONST 
    0x54e: v54e(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0) = CONST 
    0x570: v570(0x11) = CONST 
    0x573: v573 = GT v54barg1, v570(0x11)
    0x574: v574 = ISZERO v573
    0x575: v575(0x57a) = CONST 
    0x578: JUMPI v575(0x57a), v574

    Begin block 0x579
    prev=[0x54b], succ=[]
    =================================
    0x579: THROW 

    Begin block 0x57a
    prev=[0x54b], succ=[0x585, 0x586]
    =================================
    0x57c: v57c(0x13) = CONST 
    0x57f: v57f = GT v54barg0, v57c(0x13)
    0x580: v580 = ISZERO v57f
    0x581: v581(0x586) = CONST 
    0x584: JUMPI v581(0x586), v580

    Begin block 0x585
    prev=[0x57a], succ=[]
    =================================
    0x585: THROW 

    Begin block 0x586
    prev=[0x57a], succ=[0x5b0, 0x5b1]
    =================================
    0x587: v587(0x40) = CONST 
    0x58a: v58a = MLOAD v587(0x40)
    0x58d: MSTORE v58a, v54barg1
    0x58e: v58e(0x20) = CONST 
    0x591: v591 = ADD v58a, v58e(0x20)
    0x595: MSTORE v591, v54barg0
    0x596: v596(0x0) = CONST 
    0x59a: v59a = ADD v587(0x40), v58a
    0x59b: MSTORE v59a, v596(0x0)
    0x59c: v59c = MLOAD v587(0x40)
    0x5a0: v5a0(0x0) = SUB v58a, v59c
    0x5a1: v5a1(0x60) = CONST 
    0x5a3: v5a3(0x60) = ADD v5a1(0x60), v5a0(0x0)
    0x5a5: LOG1 v59c, v5a3(0x60), v54e(0x45b96fe442630264581b197e84bbada861235052c5a1aadfff9ea4e40a969aa0)
    0x5a7: v5a7(0x11) = CONST 
    0x5aa: v5aa = GT v54barg1, v5a7(0x11)
    0x5ab: v5ab = ISZERO v5aa
    0x5ac: v5ac(0x5b1) = CONST 
    0x5af: JUMPI v5ac(0x5b1), v5ab

    Begin block 0x5b0
    prev=[0x586], succ=[]
    =================================
    0x5b0: THROW 

    Begin block 0x5b1
    prev=[0x586], succ=[]
    =================================
    0x5b7: RETURNPRIVATE v54barg2, v54barg1

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
    0x10c: v10c(0x6b5) = CONST 
    0x10f: v10f(0x210) = CONST 
    0x112: JUMP v10f(0x210)

    Begin block 0x210
    prev=[0x10a], succ=[0x6b5]
    =================================
    0x211: v211(0x1) = CONST 
    0x213: v213 = SLOAD v211(0x1)
    0x214: v214(0x1) = CONST 
    0x216: v216(0x1) = CONST 
    0x218: v218(0xa0) = CONST 
    0x21a: v21a(0x10000000000000000000000000000000000000000) = SHL v218(0xa0), v216(0x1)
    0x21b: v21b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21a(0x10000000000000000000000000000000000000000), v214(0x1)
    0x21c: v21c = AND v21b(0xffffffffffffffffffffffffffffffffffffffff), v213
    0x21e: JUMP v10c(0x6b5)

    Begin block 0x6b5
    prev=[0x210], succ=[]
    =================================
    0x6b6: v6b6(0x40) = CONST 
    0x6b9: v6b9 = MLOAD v6b6(0x40)
    0x6ba: v6ba(0x1) = CONST 
    0x6bc: v6bc(0x1) = CONST 
    0x6be: v6be(0xa0) = CONST 
    0x6c0: v6c0(0x10000000000000000000000000000000000000000) = SHL v6be(0xa0), v6bc(0x1)
    0x6c1: v6c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c0(0x10000000000000000000000000000000000000000), v6ba(0x1)
    0x6c4: v6c4 = AND v21c, v6c1(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c6: MSTORE v6b9, v6c4
    0x6c7: v6c7 = MLOAD v6b6(0x40)
    0x6cb: v6cb(0x0) = SUB v6b9, v6c7
    0x6cc: v6cc(0x20) = CONST 
    0x6ce: v6ce(0x20) = ADD v6cc(0x20), v6cb(0x0)
    0x6d0: RETURN v6c7, v6ce(0x20)

}

