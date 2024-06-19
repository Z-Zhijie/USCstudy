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
    prev=[0x0], succ=[0x1a, 0x2633]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x247d: v247d(0x2633) = CONST 
    0x247e: JUMPI v247d(0x2633), v15

    Begin block 0x1a
    prev=[0x10], succ=[0xb2, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x8da5cb5b) = CONST 
    0x26: v26 = GT v21(0x8da5cb5b), v1f
    0x27: v27(0xb2) = CONST 
    0x2a: JUMPI v27(0xb2), v26

    Begin block 0xb2
    prev=[0x1a], succ=[0x109, 0xbe]
    =================================
    0xb4: vb4(0x4c96a389) = CONST 
    0xb9: vb9 = GT vb4(0x4c96a389), v1f
    0xba: vba(0x109) = CONST 
    0xbd: JUMPI vba(0x109), vb9

    Begin block 0x109
    prev=[0xb2], succ=[0x24a3, 0x115]
    =================================
    0x10b: v10b(0xc0edbe8) = CONST 
    0x110: v110 = EQ v10b(0xc0edbe8), v1f
    0x249b: v249b(0x24a3) = CONST 
    0x249c: JUMPI v249b(0x24a3), v110

    Begin block 0x24a3
    prev=[0x109], succ=[]
    =================================
    0x24a4: v24a4(0x13b) = CONST 
    0x24a5: CALLPRIVATE v24a4(0x13b)

    Begin block 0x115
    prev=[0x109], succ=[0x24a6, 0x120]
    =================================
    0x116: v116(0x158ef93e) = CONST 
    0x11b: v11b = EQ v116(0x158ef93e), v1f
    0x249d: v249d(0x24a6) = CONST 
    0x249e: JUMPI v249d(0x24a6), v11b

    Begin block 0x24a6
    prev=[0x115], succ=[]
    =================================
    0x24a7: v24a7(0x145) = CONST 
    0x24a8: CALLPRIVATE v24a7(0x145)

    Begin block 0x120
    prev=[0x115], succ=[0x24a9, 0x12b]
    =================================
    0x121: v121(0x25e22370) = CONST 
    0x126: v126 = EQ v121(0x25e22370), v1f
    0x249f: v249f(0x24a9) = CONST 
    0x24a0: JUMPI v249f(0x24a9), v126

    Begin block 0x24a9
    prev=[0x120], succ=[]
    =================================
    0x24aa: v24aa(0x161) = CONST 
    0x24ab: CALLPRIVATE v24aa(0x161)

    Begin block 0x12b
    prev=[0x120], succ=[0x24ac, 0x136]
    =================================
    0x12c: v12c(0x344e5e34) = CONST 
    0x131: v131 = EQ v12c(0x344e5e34), v1f
    0x24a1: v24a1(0x24ac) = CONST 
    0x24a2: JUMPI v24a1(0x24ac), v131

    Begin block 0x24ac
    prev=[0x12b], succ=[]
    =================================
    0x24ad: v24ad(0x192) = CONST 
    0x24ae: CALLPRIVATE v24ad(0x192)

    Begin block 0x136
    prev=[0x12b], succ=[]
    =================================
    0x137: v137(0x0) = CONST 
    0x13a: REVERT v137(0x0), v137(0x0)

    Begin block 0xbe
    prev=[0xb2], succ=[0xee, 0xc9]
    =================================
    0xbf: vbf(0x715018a6) = CONST 
    0xc4: vc4 = GT vbf(0x715018a6), v1f
    0xc5: vc5(0xee) = CONST 
    0xc8: JUMPI vc5(0xee), vc4

    Begin block 0xee
    prev=[0xbe], succ=[0x24af, 0xfa]
    =================================
    0xf0: vf0(0x4c96a389) = CONST 
    0xf5: vf5 = EQ vf0(0x4c96a389), v1f
    0x2497: v2497(0x24af) = CONST 
    0x2498: JUMPI v2497(0x24af), vf5

    Begin block 0x24af
    prev=[0xee], succ=[]
    =================================
    0x24b0: v24b0(0x1af) = CONST 
    0x24b1: CALLPRIVATE v24b0(0x1af)

    Begin block 0xfa
    prev=[0xee], succ=[0x105, 0x24b2]
    =================================
    0xfb: vfb(0x69a17989) = CONST 
    0x100: v100 = EQ vfb(0x69a17989), v1f
    0x2499: v2499(0x24b2) = CONST 
    0x249a: JUMPI v2499(0x24b2), v100

    Begin block 0x105
    prev=[0xfa], succ=[0x210a]
    =================================
    0x105: v105(0x210a) = CONST 
    0x108: JUMP v105(0x210a)

    Begin block 0x210a
    prev=[0x105], succ=[]
    =================================
    0x210b: v210b(0x0) = CONST 
    0x210e: REVERT v210b(0x0), v210b(0x0)

    Begin block 0x24b2
    prev=[0xfa], succ=[]
    =================================
    0x24b3: v24b3(0x1e2) = CONST 
    0x24b4: CALLPRIVATE v24b3(0x1e2)

    Begin block 0xc9
    prev=[0xbe], succ=[0x24b5, 0xd4]
    =================================
    0xca: vca(0x715018a6) = CONST 
    0xcf: vcf = EQ vca(0x715018a6), v1f
    0x2491: v2491(0x24b5) = CONST 
    0x2492: JUMPI v2491(0x24b5), vcf

    Begin block 0x24b5
    prev=[0xc9], succ=[]
    =================================
    0x24b6: v24b6(0x1fc) = CONST 
    0x24b7: CALLPRIVATE v24b6(0x1fc)

    Begin block 0xd4
    prev=[0xc9], succ=[0x24b8, 0xdf]
    =================================
    0xd5: vd5(0x728fa2a9) = CONST 
    0xda: vda = EQ vd5(0x728fa2a9), v1f
    0x2493: v2493(0x24b8) = CONST 
    0x2494: JUMPI v2493(0x24b8), vda

    Begin block 0x24b8
    prev=[0xd4], succ=[]
    =================================
    0x24b9: v24b9(0x204) = CONST 
    0x24ba: CALLPRIVATE v24b9(0x204)

    Begin block 0xdf
    prev=[0xd4], succ=[0xea, 0x24bb]
    =================================
    0xe0: ve0(0x87854396) = CONST 
    0xe5: ve5 = EQ ve0(0x87854396), v1f
    0x2495: v2495(0x24bb) = CONST 
    0x2496: JUMPI v2495(0x24bb), ve5

    Begin block 0xea
    prev=[0xdf], succ=[0x20e6]
    =================================
    0xea: vea(0x20e6) = CONST 
    0xed: JUMP vea(0x20e6)

    Begin block 0x20e6
    prev=[0xea], succ=[]
    =================================
    0x20e7: v20e7(0x0) = CONST 
    0x20ea: REVERT v20e7(0x0), v20e7(0x0)

    Begin block 0x24bb
    prev=[0xdf], succ=[]
    =================================
    0x24bc: v24bc(0x20c) = CONST 
    0x24bd: CALLPRIVATE v24bc(0x20c)

    Begin block 0x2b
    prev=[0x1a], succ=[0x81, 0x36]
    =================================
    0x2c: v2c(0xd1af0c7d) = CONST 
    0x31: v31 = GT v2c(0xd1af0c7d), v1f
    0x32: v32(0x81) = CONST 
    0x35: JUMPI v32(0x81), v31

    Begin block 0x81
    prev=[0x2b], succ=[0x24be, 0x8d]
    =================================
    0x83: v83(0x8da5cb5b) = CONST 
    0x88: v88 = EQ v83(0x8da5cb5b), v1f
    0x2489: v2489(0x24be) = CONST 
    0x248a: JUMPI v2489(0x24be), v88

    Begin block 0x24be
    prev=[0x81], succ=[]
    =================================
    0x24bf: v24bf(0x256) = CONST 
    0x24c0: CALLPRIVATE v24bf(0x256)

    Begin block 0x8d
    prev=[0x81], succ=[0x24c1, 0x98]
    =================================
    0x8e: v8e(0x9d8fac7f) = CONST 
    0x93: v93 = EQ v8e(0x9d8fac7f), v1f
    0x248b: v248b(0x24c1) = CONST 
    0x248c: JUMPI v248b(0x24c1), v93

    Begin block 0x24c1
    prev=[0x8d], succ=[]
    =================================
    0x24c2: v24c2(0x25e) = CONST 
    0x24c3: CALLPRIVATE v24c2(0x25e)

    Begin block 0x98
    prev=[0x8d], succ=[0x24c4, 0xa3]
    =================================
    0x99: v99(0xaaf5a58f) = CONST 
    0x9e: v9e = EQ v99(0xaaf5a58f), v1f
    0x248d: v248d(0x24c4) = CONST 
    0x248e: JUMPI v248d(0x24c4), v9e

    Begin block 0x24c4
    prev=[0x98], succ=[]
    =================================
    0x24c5: v24c5(0x38a) = CONST 
    0x24c6: CALLPRIVATE v24c5(0x38a)

    Begin block 0xa3
    prev=[0x98], succ=[0xae, 0x24c7]
    =================================
    0xa4: va4(0xc0c53b8b) = CONST 
    0xa9: va9 = EQ va4(0xc0c53b8b), v1f
    0x248f: v248f(0x24c7) = CONST 
    0x2490: JUMPI v248f(0x24c7), va9

    Begin block 0xae
    prev=[0xa3], succ=[0x20c2]
    =================================
    0xae: vae(0x20c2) = CONST 
    0xb1: JUMP vae(0x20c2)

    Begin block 0x20c2
    prev=[0xae], succ=[]
    =================================
    0x20c3: v20c3(0x0) = CONST 
    0x20c6: REVERT v20c3(0x0), v20c3(0x0)

    Begin block 0x24c7
    prev=[0xa3], succ=[]
    =================================
    0x24c8: v24c8(0x3bd) = CONST 
    0x24c9: CALLPRIVATE v24c8(0x3bd)

    Begin block 0x36
    prev=[0x2b], succ=[0x66, 0x41]
    =================================
    0x37: v37(0xea411344) = CONST 
    0x3c: v3c = GT v37(0xea411344), v1f
    0x3d: v3d(0x66) = CONST 
    0x40: JUMPI v3d(0x66), v3c

    Begin block 0x66
    prev=[0x36], succ=[0x24ca, 0x72]
    =================================
    0x68: v68(0xd1af0c7d) = CONST 
    0x6d: v6d = EQ v68(0xd1af0c7d), v1f
    0x2485: v2485(0x24ca) = CONST 
    0x2486: JUMPI v2485(0x24ca), v6d

    Begin block 0x24ca
    prev=[0x66], succ=[]
    =================================
    0x24cb: v24cb(0x402) = CONST 
    0x24cc: CALLPRIVATE v24cb(0x402)

    Begin block 0x72
    prev=[0x66], succ=[0x7d, 0x24cd]
    =================================
    0x73: v73(0xd34b1e6a) = CONST 
    0x78: v78 = EQ v73(0xd34b1e6a), v1f
    0x2487: v2487(0x24cd) = CONST 
    0x2488: JUMPI v2487(0x24cd), v78

    Begin block 0x7d
    prev=[0x72], succ=[0x209e]
    =================================
    0x7d: v7d(0x209e) = CONST 
    0x80: JUMP v7d(0x209e)

    Begin block 0x209e
    prev=[0x7d], succ=[]
    =================================
    0x209f: v209f(0x0) = CONST 
    0x20a2: REVERT v209f(0x0), v209f(0x0)

    Begin block 0x24cd
    prev=[0x72], succ=[]
    =================================
    0x24ce: v24ce(0x40a) = CONST 
    0x24cf: CALLPRIVATE v24ce(0x40a)

    Begin block 0x41
    prev=[0x36], succ=[0x24d0, 0x4c]
    =================================
    0x42: v42(0xea411344) = CONST 
    0x47: v47 = EQ v42(0xea411344), v1f
    0x247f: v247f(0x24d0) = CONST 
    0x2480: JUMPI v247f(0x24d0), v47

    Begin block 0x24d0
    prev=[0x41], succ=[]
    =================================
    0x24d1: v24d1(0x412) = CONST 
    0x24d2: CALLPRIVATE v24d1(0x412)

    Begin block 0x4c
    prev=[0x41], succ=[0x24d3, 0x57]
    =================================
    0x4d: v4d(0xeacdc5ff) = CONST 
    0x52: v52 = EQ v4d(0xeacdc5ff), v1f
    0x2481: v2481(0x24d3) = CONST 
    0x2482: JUMPI v2481(0x24d3), v52

    Begin block 0x24d3
    prev=[0x4c], succ=[]
    =================================
    0x24d4: v24d4(0x41a) = CONST 
    0x24d5: CALLPRIVATE v24d4(0x41a)

    Begin block 0x57
    prev=[0x4c], succ=[0x62, 0x24d6]
    =================================
    0x58: v58(0xf2fde38b) = CONST 
    0x5d: v5d = EQ v58(0xf2fde38b), v1f
    0x2483: v2483(0x24d6) = CONST 
    0x2484: JUMPI v2483(0x24d6), v5d

    Begin block 0x62
    prev=[0x57], succ=[0x207a]
    =================================
    0x62: v62(0x207a) = CONST 
    0x65: JUMP v62(0x207a)

    Begin block 0x207a
    prev=[0x62], succ=[]
    =================================
    0x207b: v207b(0x0) = CONST 
    0x207e: REVERT v207b(0x0), v207b(0x0)

    Begin block 0x24d6
    prev=[0x57], succ=[]
    =================================
    0x24d7: v24d7(0x422) = CONST 
    0x24d8: CALLPRIVATE v24d7(0x422)

    Begin block 0x2633
    prev=[0x10], succ=[]
    =================================
    0x2634: v2634(0x2056) = CONST 
    0x2635: CALLPRIVATE v2634(0x2056)

}

function executeNewEpoch()() public {
    Begin block 0x13b
    prev=[], succ=[0x455]
    =================================
    0x13c: v13c(0x212e) = CONST 
    0x13f: v13f(0x455) = CONST 
    0x142: JUMP v13f(0x455)

    Begin block 0x455
    prev=[0x13b], succ=[0x475, 0x4db]
    =================================
    0x456: v456(0x0) = CONST 
    0x458: v458 = SLOAD v456(0x0)
    0x459: v459(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x46e: v46e = AND v459(0xffffffffffffffffffffffffffffffffffffffff), v458
    0x46f: v46f = CALLER 
    0x470: v470 = EQ v46f, v46e
    0x471: v471(0x4db) = CONST 
    0x474: JUMPI v471(0x4db), v470

    Begin block 0x475
    prev=[0x455], succ=[]
    =================================
    0x475: v475(0x40) = CONST 
    0x478: v478 = MLOAD v475(0x40)
    0x479: v479(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x49b: MSTORE v478, v479(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x49c: v49c(0x20) = CONST 
    0x49e: v49e(0x4) = CONST 
    0x4a1: v4a1 = ADD v478, v49e(0x4)
    0x4a4: MSTORE v4a1, v49c(0x20)
    0x4a5: v4a5(0x24) = CONST 
    0x4a8: v4a8 = ADD v478, v4a5(0x24)
    0x4a9: MSTORE v4a8, v49c(0x20)
    0x4aa: v4aa(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x4cb: v4cb(0x44) = CONST 
    0x4ce: v4ce = ADD v478, v4cb(0x44)
    0x4cf: MSTORE v4ce, v4aa(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x4d1: v4d1 = MLOAD v475(0x40)
    0x4d5: v4d5(0x0) = SUB v478, v4d1
    0x4d6: v4d6(0x64) = CONST 
    0x4d8: v4d8(0x64) = ADD v4d6(0x64), v4d5(0x0)
    0x4da: REVERT v4d1, v4d8(0x64)

    Begin block 0x4db
    prev=[0x455], succ=[0x14b3]
    =================================
    0x4dc: v4dc(0x8) = CONST 
    0x4df: v4df = SLOAD v4dc(0x8)
    0x4e0: v4e0(0x1) = CONST 
    0x4e2: v4e2 = ADD v4e0(0x1), v4df
    0x4e4: SSTORE v4dc(0x8), v4e2
    0x4e5: v4e5(0x4ec) = CONST 
    0x4e8: v4e8(0x14b3) = CONST 
    0x4eb: JUMP v4e8(0x14b3)

    Begin block 0x14b3
    prev=[0x4db], succ=[0x4ec]
    =================================
    0x14b4: v14b4(0x40) = CONST 
    0x14b6: v14b6 = MLOAD v14b4(0x40)
    0x14b8: v14b8(0xe0) = CONST 
    0x14ba: v14ba = ADD v14b8(0xe0), v14b6
    0x14bb: v14bb(0x40) = CONST 
    0x14bd: MSTORE v14bb(0x40), v14ba
    0x14bf: v14bf(0x0) = CONST 
    0x14c2: MSTORE v14b6, v14bf(0x0)
    0x14c3: v14c3(0x20) = CONST 
    0x14c5: v14c5 = ADD v14c3(0x20), v14b6
    0x14c6: v14c6(0x0) = CONST 
    0x14c9: MSTORE v14c5, v14c6(0x0)
    0x14ca: v14ca(0x20) = CONST 
    0x14cc: v14cc = ADD v14ca(0x20), v14c5
    0x14cd: v14cd(0x0) = CONST 
    0x14d0: MSTORE v14cc, v14cd(0x0)
    0x14d1: v14d1(0x20) = CONST 
    0x14d3: v14d3 = ADD v14d1(0x20), v14cc
    0x14d4: v14d4(0x60) = CONST 
    0x14d7: MSTORE v14d3, v14d4(0x60)
    0x14d8: v14d8(0x20) = CONST 
    0x14da: v14da = ADD v14d8(0x20), v14d3
    0x14db: v14db(0x60) = CONST 
    0x14de: MSTORE v14da, v14db(0x60)
    0x14df: v14df(0x20) = CONST 
    0x14e1: v14e1 = ADD v14df(0x20), v14da
    0x14e2: v14e2(0x0) = CONST 
    0x14e5: MSTORE v14e1, v14e2(0x0)
    0x14e6: v14e6(0x20) = CONST 
    0x14e8: v14e8 = ADD v14e6(0x20), v14e1
    0x14e9: v14e9(0x0) = CONST 
    0x14eb: v14eb(0x1) = ISZERO v14e9(0x0)
    0x14ec: v14ec(0x0) = ISZERO v14eb(0x1)
    0x14ee: MSTORE v14e8, v14ec(0x0)
    0x14f1: JUMP v4e5(0x4ec)

    Begin block 0x4ec
    prev=[0x14b3], succ=[0x555, 0x590]
    =================================
    0x4ed: v4ed(0x7) = CONST 
    0x4ef: v4ef(0x0) = CONST 
    0x4f1: v4f1(0x8) = CONST 
    0x4f3: v4f3 = SLOAD v4f1(0x8)
    0x4f5: MSTORE v4ef(0x0), v4f3
    0x4f6: v4f6(0x20) = CONST 
    0x4f8: v4f8(0x20) = ADD v4f6(0x20), v4ef(0x0)
    0x4fb: MSTORE v4f8(0x20), v4ed(0x7)
    0x4fc: v4fc(0x20) = CONST 
    0x4fe: v4fe(0x40) = ADD v4fc(0x20), v4f8(0x20)
    0x4ff: v4ff(0x0) = CONST 
    0x501: v501 = SHA3 v4ff(0x0), v4fe(0x40)
    0x502: v502(0x40) = CONST 
    0x504: v504 = MLOAD v502(0x40)
    0x506: v506(0xe0) = CONST 
    0x508: v508 = ADD v506(0xe0), v504
    0x509: v509(0x40) = CONST 
    0x50b: MSTORE v509(0x40), v508
    0x50e: v50e(0x0) = CONST 
    0x511: v511 = ADD v501, v50e(0x0)
    0x512: v512 = SLOAD v511
    0x514: MSTORE v504, v512
    0x515: v515(0x20) = CONST 
    0x517: v517 = ADD v515(0x20), v504
    0x518: v518(0x1) = CONST 
    0x51b: v51b = ADD v501, v518(0x1)
    0x51c: v51c = SLOAD v51b
    0x51e: MSTORE v517, v51c
    0x51f: v51f(0x20) = CONST 
    0x521: v521 = ADD v51f(0x20), v517
    0x522: v522(0x2) = CONST 
    0x525: v525 = ADD v501, v522(0x2)
    0x526: v526 = SLOAD v525
    0x528: MSTORE v521, v526
    0x529: v529(0x20) = CONST 
    0x52b: v52b = ADD v529(0x20), v521
    0x52c: v52c(0x3) = CONST 
    0x52f: v52f = ADD v501, v52c(0x3)
    0x531: v531 = SLOAD v52f
    0x533: v533(0x20) = CONST 
    0x535: v535 = MUL v533(0x20), v531
    0x536: v536(0x20) = CONST 
    0x538: v538 = ADD v536(0x20), v535
    0x539: v539(0x40) = CONST 
    0x53b: v53b = MLOAD v539(0x40)
    0x53e: v53e = ADD v53b, v538
    0x53f: v53f(0x40) = CONST 
    0x541: MSTORE v53f(0x40), v53e
    0x548: MSTORE v53b, v531
    0x549: v549(0x20) = CONST 
    0x54b: v54b = ADD v549(0x20), v53b
    0x54e: v54e = SLOAD v52f
    0x550: v550 = ISZERO v54e
    0x551: v551(0x590) = CONST 
    0x554: JUMPI v551(0x590), v550

    Begin block 0x555
    prev=[0x4ec], succ=[0x565]
    =================================
    0x555: v555(0x20) = CONST 
    0x557: v557 = MUL v555(0x20), v54e
    0x559: v559 = ADD v54b, v557
    0x55c: v55c(0x0) = CONST 
    0x55e: MSTORE v55c(0x0), v52f
    0x55f: v55f(0x20) = CONST 
    0x561: v561(0x0) = CONST 
    0x563: v563 = SHA3 v561(0x0), v55f(0x20)

    Begin block 0x565
    prev=[0x555, 0x565], succ=[0x590, 0x565]
    =================================
    0x565_0x0: v565_0 = PHI v54b, v588
    0x565_0x1: v565_1 = PHI v563, v584
    0x567: v567 = SLOAD v565_1
    0x568: v568(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x57d: v57d = AND v568(0xffffffffffffffffffffffffffffffffffffffff), v567
    0x57f: MSTORE v565_0, v57d
    0x580: v580(0x1) = CONST 
    0x584: v584 = ADD v565_1, v580(0x1)
    0x586: v586(0x20) = CONST 
    0x588: v588 = ADD v586(0x20), v565_0
    0x58b: v58b = GT v559, v588
    0x58c: v58c(0x565) = CONST 
    0x58f: JUMPI v58c(0x565), v58b

    Begin block 0x590
    prev=[0x4ec, 0x565], succ=[0x5c4, 0x5e8]
    =================================
    0x597: MSTORE v52b, v53b
    0x598: v598(0x20) = CONST 
    0x59a: v59a = ADD v598(0x20), v52b
    0x59b: v59b(0x4) = CONST 
    0x59e: v59e = ADD v501, v59b(0x4)
    0x5a0: v5a0 = SLOAD v59e
    0x5a2: v5a2(0x20) = CONST 
    0x5a4: v5a4 = MUL v5a2(0x20), v5a0
    0x5a5: v5a5(0x20) = CONST 
    0x5a7: v5a7 = ADD v5a5(0x20), v5a4
    0x5a8: v5a8(0x40) = CONST 
    0x5aa: v5aa = MLOAD v5a8(0x40)
    0x5ad: v5ad = ADD v5aa, v5a7
    0x5ae: v5ae(0x40) = CONST 
    0x5b0: MSTORE v5ae(0x40), v5ad
    0x5b7: MSTORE v5aa, v5a0
    0x5b8: v5b8(0x20) = CONST 
    0x5ba: v5ba = ADD v5b8(0x20), v5aa
    0x5bd: v5bd = SLOAD v59e
    0x5bf: v5bf = ISZERO v5bd
    0x5c0: v5c0(0x5e8) = CONST 
    0x5c3: JUMPI v5c0(0x5e8), v5bf

    Begin block 0x5c4
    prev=[0x590], succ=[0x5d4]
    =================================
    0x5c4: v5c4(0x20) = CONST 
    0x5c6: v5c6 = MUL v5c4(0x20), v5bd
    0x5c8: v5c8 = ADD v5ba, v5c6
    0x5cb: v5cb(0x0) = CONST 
    0x5cd: MSTORE v5cb(0x0), v59e
    0x5ce: v5ce(0x20) = CONST 
    0x5d0: v5d0(0x0) = CONST 
    0x5d2: v5d2 = SHA3 v5d0(0x0), v5ce(0x20)

    Begin block 0x5d4
    prev=[0x5c4, 0x5d4], succ=[0x5e8, 0x5d4]
    =================================
    0x5d4_0x0: v5d4_0 = PHI v5ba, v5db
    0x5d4_0x1: v5d4_1 = PHI v5d2, v5df
    0x5d6: v5d6 = SLOAD v5d4_1
    0x5d8: MSTORE v5d4_0, v5d6
    0x5d9: v5d9(0x20) = CONST 
    0x5db: v5db = ADD v5d9(0x20), v5d4_0
    0x5dd: v5dd(0x1) = CONST 
    0x5df: v5df = ADD v5dd(0x1), v5d4_1
    0x5e3: v5e3 = GT v5c8, v5db
    0x5e4: v5e4(0x5d4) = CONST 
    0x5e7: JUMPI v5e4(0x5d4), v5e3

    Begin block 0x5e8
    prev=[0x590, 0x5d4], succ=[0x619, 0x669]
    =================================
    0x5ee: MSTORE v59a, v5aa
    0x5f1: v5f1(0x5) = CONST 
    0x5f4: v5f4 = ADD v501, v5f1(0x5)
    0x5f5: v5f5 = SLOAD v5f4
    0x5f6: v5f6(0x20) = CONST 
    0x5f9: v5f9 = ADD v59a, v5f6(0x20)
    0x5fa: MSTORE v5f9, v5f5
    0x5fb: v5fb(0x6) = CONST 
    0x5ff: v5ff = ADD v501, v5fb(0x6)
    0x600: v600 = SLOAD v5ff
    0x601: v601(0xff) = CONST 
    0x603: v603 = AND v601(0xff), v600
    0x604: v604 = ISZERO v603
    0x605: v605 = ISZERO v604
    0x606: v606(0x40) = CONST 
    0x60a: v60a = ADD v59a, v606(0x40)
    0x60b: MSTORE v60a, v605
    0x60c: v60c(0x8) = CONST 
    0x60e: v60e = SLOAD v60c(0x8)
    0x610: v610 = MLOAD v504
    0x614: v614 = EQ v60e, v610
    0x615: v615(0x669) = CONST 
    0x618: JUMPI v615(0x669), v614

    Begin block 0x619
    prev=[0x5e8], succ=[]
    =================================
    0x619: v619(0x40) = CONST 
    0x61b: v61b = MLOAD v619(0x40)
    0x61c: v61c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x63e: MSTORE v61b, v61c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x63f: v63f(0x4) = CONST 
    0x641: v641 = ADD v63f(0x4), v61b
    0x644: v644(0x20) = CONST 
    0x646: v646 = ADD v644(0x20), v641
    0x649: v649(0x20) = SUB v646, v641
    0x64b: MSTORE v641, v649(0x20)
    0x64c: v64c(0x5c) = CONST 
    0x64f: MSTORE v646, v64c(0x5c)
    0x650: v650(0x20) = CONST 
    0x652: v652 = ADD v650(0x20), v646
    0x654: v654(0x1f27) = CONST 
    0x657: v657(0x5c) = CONST 
    0x65a: CODECOPY v652, v654(0x1f27), v657(0x5c)
    0x65b: v65b(0x60) = CONST 
    0x65d: v65d = ADD v65b(0x60), v652
    0x661: v661(0x40) = CONST 
    0x663: v663 = MLOAD v661(0x40)
    0x666: v666(0xa4) = SUB v65d, v663
    0x668: REVERT v663, v666(0xa4)

    Begin block 0x669
    prev=[0x5e8], succ=[0x674, 0x675]
    =================================
    0x66a: v66a(0xc0) = CONST 
    0x66d: v66d = ADD v504, v66a(0xc0)
    0x66e: v66e = MLOAD v66d
    0x66f: v66f = ISZERO v66e
    0x670: v670(0x675) = CONST 
    0x673: JUMPI v670(0x675), v66f

    Begin block 0x674
    prev=[0x669], succ=[]
    =================================
    0x674: THROW 

    Begin block 0x675
    prev=[0x669], succ=[0x678]
    =================================
    0x676: v676(0x0) = CONST 

    Begin block 0x678
    prev=[0x675, 0x85a], succ=[0x686, 0x86a]
    =================================
    0x678_0x0: v678_0 = PHI v676(0x0), v861
    0x67a: v67a(0x60) = CONST 
    0x67c: v67c = ADD v67a(0x60), v504
    0x67d: v67d = MLOAD v67c
    0x67e: v67e = MLOAD v67d
    0x680: v680 = LT v678_0, v67e
    0x681: v681 = ISZERO v680
    0x682: v682(0x86a) = CONST 
    0x685: JUMPI v682(0x86a), v681

    Begin block 0x686
    prev=[0x678], succ=[0x6b8, 0x6b9]
    =================================
    0x686: v686(0x4) = CONST 
    0x686_0x0: v686_0 = PHI v676(0x0), v861
    0x688: v688 = SLOAD v686(0x4)
    0x689: v689(0x60) = CONST 
    0x68c: v68c = ADD v504, v689(0x60)
    0x68d: v68d = MLOAD v68c
    0x68f: v68f = MLOAD v68d
    0x690: v690(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a7: v6a7 = AND v688, v690(0xffffffffffffffffffffffffffffffffffffffff)
    0x6a9: v6a9(0xa9059cbb) = CONST 
    0x6b3: v6b3 = LT v686_0, v68f
    0x6b4: v6b4(0x6b9) = CONST 
    0x6b7: JUMPI v6b4(0x6b9), v6b3

    Begin block 0x6b8
    prev=[0x686], succ=[]
    =================================
    0x6b8: THROW 

    Begin block 0x6b9
    prev=[0x686], succ=[0x6d0, 0x6d1]
    =================================
    0x6b9_0x0: v6b9_0 = PHI v676(0x0), v861
    0x6b9_0x4: v6b9_4 = PHI v676(0x0), v861
    0x6ba: v6ba(0x20) = CONST 
    0x6bc: v6bc = MUL v6ba(0x20), v6b9_0
    0x6bd: v6bd(0x20) = CONST 
    0x6bf: v6bf = ADD v6bd(0x20), v6bc
    0x6c0: v6c0 = ADD v6bf, v68d
    0x6c1: v6c1 = MLOAD v6c0
    0x6c3: v6c3(0x80) = CONST 
    0x6c5: v6c5 = ADD v6c3(0x80), v504
    0x6c6: v6c6 = MLOAD v6c5
    0x6c9: v6c9 = MLOAD v6c6
    0x6cb: v6cb = LT v6b9_4, v6c9
    0x6cc: v6cc(0x6d1) = CONST 
    0x6cf: JUMPI v6cc(0x6d1), v6cb

    Begin block 0x6d0
    prev=[0x6b9], succ=[]
    =================================
    0x6d0: THROW 

    Begin block 0x6d1
    prev=[0x6b9], succ=[0x728, 0x72c]
    =================================
    0x6d1_0x0: v6d1_0 = PHI v676(0x0), v861
    0x6d2: v6d2(0x20) = CONST 
    0x6d4: v6d4 = MUL v6d2(0x20), v6d1_0
    0x6d5: v6d5(0x20) = CONST 
    0x6d7: v6d7 = ADD v6d5(0x20), v6d4
    0x6d8: v6d8 = ADD v6d7, v6c6
    0x6d9: v6d9 = MLOAD v6d8
    0x6da: v6da(0x40) = CONST 
    0x6dc: v6dc = MLOAD v6da(0x40)
    0x6de: v6de(0xffffffff) = CONST 
    0x6e3: v6e3(0xa9059cbb) = AND v6de(0xffffffff), v6a9(0xa9059cbb)
    0x6e4: v6e4(0xe0) = CONST 
    0x6e6: v6e6(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL v6e4(0xe0), v6e3(0xa9059cbb)
    0x6e8: MSTORE v6dc, v6e6(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x6e9: v6e9(0x4) = CONST 
    0x6eb: v6eb = ADD v6e9(0x4), v6dc
    0x6ee: v6ee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x703: v703 = AND v6ee(0xffffffffffffffffffffffffffffffffffffffff), v6c1
    0x705: MSTORE v6eb, v703
    0x706: v706(0x20) = CONST 
    0x708: v708 = ADD v706(0x20), v6eb
    0x70b: MSTORE v708, v6d9
    0x70c: v70c(0x20) = CONST 
    0x70e: v70e = ADD v70c(0x20), v708
    0x713: v713(0x20) = CONST 
    0x715: v715(0x40) = CONST 
    0x717: v717 = MLOAD v715(0x40)
    0x71a: v71a(0x44) = SUB v70e, v717
    0x71c: v71c(0x0) = CONST 
    0x720: v720 = EXTCODESIZE v6a7
    0x721: v721 = ISZERO v720
    0x723: v723 = ISZERO v721
    0x724: v724(0x72c) = CONST 
    0x727: JUMPI v724(0x72c), v723

    Begin block 0x728
    prev=[0x6d1], succ=[]
    =================================
    0x728: v728(0x0) = CONST 
    0x72b: REVERT v728(0x0), v728(0x0)

    Begin block 0x72c
    prev=[0x6d1], succ=[0x737, 0x740]
    =================================
    0x72e: v72e = GAS 
    0x72f: v72f = CALL v72e, v6a7, v71c(0x0), v717, v71a(0x44), v717, v713(0x20)
    0x730: v730 = ISZERO v72f
    0x732: v732 = ISZERO v730
    0x733: v733(0x740) = CONST 
    0x736: JUMPI v733(0x740), v732

    Begin block 0x737
    prev=[0x72c], succ=[]
    =================================
    0x737: v737 = RETURNDATASIZE 
    0x738: v738(0x0) = CONST 
    0x73b: RETURNDATACOPY v738(0x0), v738(0x0), v737
    0x73c: v73c = RETURNDATASIZE 
    0x73d: v73d(0x0) = CONST 
    0x73f: REVERT v73d(0x0), v73c

    Begin block 0x740
    prev=[0x72c], succ=[0x752, 0x756]
    =================================
    0x745: v745(0x40) = CONST 
    0x747: v747 = MLOAD v745(0x40)
    0x748: v748 = RETURNDATASIZE 
    0x749: v749(0x20) = CONST 
    0x74c: v74c = LT v748, v749(0x20)
    0x74d: v74d = ISZERO v74c
    0x74e: v74e(0x756) = CONST 
    0x751: JUMPI v74e(0x756), v74d

    Begin block 0x752
    prev=[0x740], succ=[]
    =================================
    0x752: v752(0x0) = CONST 
    0x755: REVERT v752(0x0), v752(0x0)

    Begin block 0x756
    prev=[0x740], succ=[0x75d, 0x7ad]
    =================================
    0x758: v758 = MLOAD v747
    0x759: v759(0x7ad) = CONST 
    0x75c: JUMPI v759(0x7ad), v758

    Begin block 0x75d
    prev=[0x756], succ=[]
    =================================
    0x75d: v75d(0x40) = CONST 
    0x75f: v75f = MLOAD v75d(0x40)
    0x760: v760(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x782: MSTORE v75f, v760(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x783: v783(0x4) = CONST 
    0x785: v785 = ADD v783(0x4), v75f
    0x788: v788(0x20) = CONST 
    0x78a: v78a = ADD v788(0x20), v785
    0x78d: v78d(0x20) = SUB v78a, v785
    0x78f: MSTORE v785, v78d(0x20)
    0x790: v790(0x3c) = CONST 
    0x793: MSTORE v78a, v790(0x3c)
    0x794: v794(0x20) = CONST 
    0x796: v796 = ADD v794(0x20), v78a
    0x798: v798(0x1df3) = CONST 
    0x79b: v79b(0x3c) = CONST 
    0x79e: CODECOPY v796, v798(0x1df3), v79b(0x3c)
    0x79f: v79f(0x40) = CONST 
    0x7a1: v7a1 = ADD v79f(0x40), v796
    0x7a5: v7a5(0x40) = CONST 
    0x7a7: v7a7 = MLOAD v7a5(0x40)
    0x7aa: v7aa(0x84) = SUB v7a1, v7a7
    0x7ac: REVERT v7a7, v7aa(0x84)

    Begin block 0x7ad
    prev=[0x756], succ=[0x7bc, 0x7bd]
    =================================
    0x7ad_0x0: v7ad_0 = PHI v676(0x0), v861
    0x7af: v7af(0x60) = CONST 
    0x7b1: v7b1 = ADD v7af(0x60), v504
    0x7b2: v7b2 = MLOAD v7b1
    0x7b5: v7b5 = MLOAD v7b2
    0x7b7: v7b7 = LT v7ad_0, v7b5
    0x7b8: v7b8(0x7bd) = CONST 
    0x7bb: JUMPI v7b8(0x7bd), v7b7

    Begin block 0x7bc
    prev=[0x7ad], succ=[]
    =================================
    0x7bc: THROW 

    Begin block 0x7bd
    prev=[0x7ad], succ=[0x7ef, 0x7f0]
    =================================
    0x7bd_0x0: v7bd_0 = PHI v676(0x0), v861
    0x7bd_0x2: v7bd_2 = PHI v676(0x0), v861
    0x7be: v7be(0x20) = CONST 
    0x7c0: v7c0 = MUL v7be(0x20), v7bd_0
    0x7c1: v7c1(0x20) = CONST 
    0x7c3: v7c3 = ADD v7c1(0x20), v7c0
    0x7c4: v7c4 = ADD v7c3, v7b2
    0x7c5: v7c5 = MLOAD v7c4
    0x7c6: v7c6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7db: v7db = AND v7c6(0xffffffffffffffffffffffffffffffffffffffff), v7c5
    0x7dc: v7dc(0x6e32820) = CONST 
    0x7e2: v7e2(0x80) = CONST 
    0x7e4: v7e4 = ADD v7e2(0x80), v504
    0x7e5: v7e5 = MLOAD v7e4
    0x7e8: v7e8 = MLOAD v7e5
    0x7ea: v7ea = LT v7bd_2, v7e8
    0x7eb: v7eb(0x7f0) = CONST 
    0x7ee: JUMPI v7eb(0x7f0), v7ea

    Begin block 0x7ef
    prev=[0x7bd], succ=[]
    =================================
    0x7ef: THROW 

    Begin block 0x7f0
    prev=[0x7bd], succ=[0x842, 0x846]
    =================================
    0x7f0_0x0: v7f0_0 = PHI v676(0x0), v861
    0x7f1: v7f1(0x20) = CONST 
    0x7f3: v7f3 = MUL v7f1(0x20), v7f0_0
    0x7f4: v7f4(0x20) = CONST 
    0x7f6: v7f6 = ADD v7f4(0x20), v7f3
    0x7f7: v7f7 = ADD v7f6, v7e5
    0x7f8: v7f8 = MLOAD v7f7
    0x7fa: v7fa(0x20) = CONST 
    0x7fc: v7fc = ADD v7fa(0x20), v504
    0x7fd: v7fd = MLOAD v7fc
    0x7ff: v7ff(0x40) = CONST 
    0x801: v801 = ADD v7ff(0x40), v504
    0x802: v802 = MLOAD v801
    0x803: v803(0x40) = CONST 
    0x805: v805 = MLOAD v803(0x40)
    0x807: v807(0xffffffff) = CONST 
    0x80c: v80c(0x6e32820) = AND v807(0xffffffff), v7dc(0x6e32820)
    0x80d: v80d(0xe0) = CONST 
    0x80f: v80f(0x6e3282000000000000000000000000000000000000000000000000000000000) = SHL v80d(0xe0), v80c(0x6e32820)
    0x811: MSTORE v805, v80f(0x6e3282000000000000000000000000000000000000000000000000000000000)
    0x812: v812(0x4) = CONST 
    0x814: v814 = ADD v812(0x4), v805
    0x818: MSTORE v814, v7f8
    0x819: v819(0x20) = CONST 
    0x81b: v81b = ADD v819(0x20), v814
    0x81e: MSTORE v81b, v7fd
    0x81f: v81f(0x20) = CONST 
    0x821: v821 = ADD v81f(0x20), v81b
    0x824: MSTORE v821, v802
    0x825: v825(0x20) = CONST 
    0x827: v827 = ADD v825(0x20), v821
    0x82d: v82d(0x0) = CONST 
    0x82f: v82f(0x40) = CONST 
    0x831: v831 = MLOAD v82f(0x40)
    0x834: v834(0x64) = SUB v827, v831
    0x836: v836(0x0) = CONST 
    0x83a: v83a = EXTCODESIZE v7db
    0x83b: v83b = ISZERO v83a
    0x83d: v83d = ISZERO v83b
    0x83e: v83e(0x846) = CONST 
    0x841: JUMPI v83e(0x846), v83d

    Begin block 0x842
    prev=[0x7f0], succ=[]
    =================================
    0x842: v842(0x0) = CONST 
    0x845: REVERT v842(0x0), v842(0x0)

    Begin block 0x846
    prev=[0x7f0], succ=[0x851, 0x85a]
    =================================
    0x848: v848 = GAS 
    0x849: v849 = CALL v848, v7db, v836(0x0), v831, v834(0x64), v831, v82d(0x0)
    0x84a: v84a = ISZERO v849
    0x84c: v84c = ISZERO v84a
    0x84d: v84d(0x85a) = CONST 
    0x850: JUMPI v84d(0x85a), v84c

    Begin block 0x851
    prev=[0x846], succ=[]
    =================================
    0x851: v851 = RETURNDATASIZE 
    0x852: v852(0x0) = CONST 
    0x855: RETURNDATACOPY v852(0x0), v852(0x0), v851
    0x856: v856 = RETURNDATASIZE 
    0x857: v857(0x0) = CONST 
    0x859: REVERT v857(0x0), v856

    Begin block 0x85a
    prev=[0x846], succ=[0x678]
    =================================
    0x85a_0x4: v85a_4 = PHI v676(0x0), v861
    0x85d: v85d(0x1) = CONST 
    0x861: v861 = ADD v85a_4, v85d(0x1)
    0x864: v864(0x678) = CONST 
    0x869: JUMP v864(0x678)

    Begin block 0x86a
    prev=[0x678], succ=[0x212e]
    =================================
    0x86d: v86d(0x8) = CONST 
    0x86f: v86f = SLOAD v86d(0x8)
    0x870: v870(0x0) = CONST 
    0x874: MSTORE v870(0x0), v86f
    0x875: v875(0x7) = CONST 
    0x877: v877(0x20) = CONST 
    0x879: MSTORE v877(0x20), v875(0x7)
    0x87a: v87a(0x40) = CONST 
    0x87d: v87d = SHA3 v870(0x0), v87a(0x40)
    0x87e: v87e(0x6) = CONST 
    0x880: v880 = ADD v87e(0x6), v87d
    0x882: v882 = SLOAD v880
    0x883: v883(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x8a4: v8a4 = AND v883(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v882
    0x8a5: v8a5(0x1) = CONST 
    0x8a7: v8a7 = OR v8a5(0x1), v8a4
    0x8a9: SSTORE v880, v8a7
    0x8aa: JUMP v13c(0x212e)

    Begin block 0x212e
    prev=[0x86a], succ=[]
    =================================
    0x212f: STOP 

}

function initialized()() public {
    Begin block 0x145
    prev=[], succ=[0x8ab]
    =================================
    0x146: v146(0x14d) = CONST 
    0x149: v149(0x8ab) = CONST 
    0x14c: JUMP v149(0x8ab)

    Begin block 0x8ab
    prev=[0x145], succ=[0x14d]
    =================================
    0x8ac: v8ac(0x2) = CONST 
    0x8ae: v8ae = SLOAD v8ac(0x2)
    0x8af: v8af(0xff) = CONST 
    0x8b1: v8b1 = AND v8af(0xff), v8ae
    0x8b3: JUMP v146(0x14d)

    Begin block 0x14d
    prev=[0x8ab], succ=[]
    =================================
    0x14e: v14e(0x40) = CONST 
    0x151: v151 = MLOAD v14e(0x40)
    0x153: v153 = ISZERO v8b1
    0x154: v154 = ISZERO v153
    0x156: MSTORE v151, v154
    0x157: v157 = MLOAD v14e(0x40)
    0x15b: v15b(0x0) = SUB v151, v157
    0x15c: v15c(0x20) = CONST 
    0x15e: v15e(0x20) = ADD v15c(0x20), v15b(0x0)
    0x160: RETURN v157, v15e(0x20)

}

function externalController()() public {
    Begin block 0x161
    prev=[], succ=[0x8b4]
    =================================
    0x162: v162(0x214f) = CONST 
    0x165: v165(0x8b4) = CONST 
    0x168: JUMP v165(0x8b4)

    Begin block 0x8b4
    prev=[0x161], succ=[0x214f]
    =================================
    0x8b5: v8b5(0x3) = CONST 
    0x8b7: v8b7 = SLOAD v8b5(0x3)
    0x8b8: v8b8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8cd: v8cd = AND v8b8(0xffffffffffffffffffffffffffffffffffffffff), v8b7
    0x8cf: JUMP v162(0x214f)

    Begin block 0x214f
    prev=[0x8b4], succ=[]
    =================================
    0x2150: v2150(0x40) = CONST 
    0x2153: v2153 = MLOAD v2150(0x40)
    0x2154: v2154(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x216b: v216b = AND v8cd, v2154(0xffffffffffffffffffffffffffffffffffffffff)
    0x216d: MSTORE v2153, v216b
    0x216e: v216e = MLOAD v2150(0x40)
    0x2172: v2172(0x0) = SUB v2153, v216e
    0x2173: v2173(0x20) = CONST 
    0x2175: v2175(0x20) = ADD v2173(0x20), v2172(0x0)
    0x2177: RETURN v216e, v2175(0x20)

}

function stakingTokens(uint256)() public {
    Begin block 0x192
    prev=[], succ=[0x1a4, 0x1a8]
    =================================
    0x193: v193(0x2197) = CONST 
    0x196: v196(0x4) = CONST 
    0x199: v199 = CALLDATASIZE 
    0x19a: v19a = SUB v199, v196(0x4)
    0x19b: v19b(0x20) = CONST 
    0x19e: v19e = LT v19a, v19b(0x20)
    0x19f: v19f = ISZERO v19e
    0x1a0: v1a0(0x1a8) = CONST 
    0x1a3: JUMPI v1a0(0x1a8), v19f

    Begin block 0x1a4
    prev=[0x192], succ=[]
    =================================
    0x1a4: v1a4(0x0) = CONST 
    0x1a7: REVERT v1a4(0x0), v1a4(0x0)

    Begin block 0x1a8
    prev=[0x192], succ=[0x8d0]
    =================================
    0x1aa: v1aa = CALLDATALOAD v196(0x4)
    0x1ab: v1ab(0x8d0) = CONST 
    0x1ae: JUMP v1ab(0x8d0)

    Begin block 0x8d0
    prev=[0x1a8], succ=[0x8dc, 0x8dd]
    =================================
    0x8d1: v8d1(0x5) = CONST 
    0x8d5: v8d5 = SLOAD v8d1(0x5)
    0x8d7: v8d7 = LT v1aa, v8d5
    0x8d8: v8d8(0x8dd) = CONST 
    0x8db: JUMPI v8d8(0x8dd), v8d7

    Begin block 0x8dc
    prev=[0x8d0], succ=[]
    =================================
    0x8dc: THROW 

    Begin block 0x8dd
    prev=[0x8d0], succ=[0x2197]
    =================================
    0x8de: v8de(0x0) = CONST 
    0x8e2: MSTORE v8de(0x0), v8d1(0x5)
    0x8e3: v8e3(0x20) = CONST 
    0x8e7: v8e7 = SHA3 v8de(0x0), v8e3(0x20)
    0x8e8: v8e8 = ADD v8e7, v1aa
    0x8e9: v8e9 = SLOAD v8e8
    0x8ea: v8ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8ff: v8ff = AND v8ea(0xffffffffffffffffffffffffffffffffffffffff), v8e9
    0x903: JUMP v193(0x2197)

    Begin block 0x2197
    prev=[0x8dd], succ=[]
    =================================
    0x2198: v2198(0x40) = CONST 
    0x219b: v219b = MLOAD v2198(0x40)
    0x219c: v219c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21b3: v21b3 = AND v8ff, v219c(0xffffffffffffffffffffffffffffffffffffffff)
    0x21b5: MSTORE v219b, v21b3
    0x21b6: v21b6 = MLOAD v2198(0x40)
    0x21ba: v21ba(0x0) = SUB v219b, v21b6
    0x21bb: v21bb(0x20) = CONST 
    0x21bd: v21bd(0x20) = ADD v21bb(0x20), v21ba(0x0)
    0x21bf: RETURN v21b6, v21bd(0x20)

}

function deploy(address)() public {
    Begin block 0x1af
    prev=[], succ=[0x1c1, 0x1c5]
    =================================
    0x1b0: v1b0(0x21df) = CONST 
    0x1b3: v1b3(0x4) = CONST 
    0x1b6: v1b6 = CALLDATASIZE 
    0x1b7: v1b7 = SUB v1b6, v1b3(0x4)
    0x1b8: v1b8(0x20) = CONST 
    0x1bb: v1bb = LT v1b7, v1b8(0x20)
    0x1bc: v1bc = ISZERO v1bb
    0x1bd: v1bd(0x1c5) = CONST 
    0x1c0: JUMPI v1bd(0x1c5), v1bc

    Begin block 0x1c1
    prev=[0x1af], succ=[]
    =================================
    0x1c1: v1c1(0x0) = CONST 
    0x1c4: REVERT v1c1(0x0), v1c1(0x0)

    Begin block 0x1c5
    prev=[0x1af], succ=[0x904]
    =================================
    0x1c7: v1c7 = CALLDATALOAD v1b3(0x4)
    0x1c8: v1c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dd: v1dd = AND v1c8(0xffffffffffffffffffffffffffffffffffffffff), v1c7
    0x1de: v1de(0x904) = CONST 
    0x1e1: JUMP v1de(0x904)

    Begin block 0x904
    prev=[0x1c5], succ=[0x924, 0x98a]
    =================================
    0x905: v905(0x0) = CONST 
    0x907: v907 = SLOAD v905(0x0)
    0x908: v908(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x91d: v91d = AND v908(0xffffffffffffffffffffffffffffffffffffffff), v907
    0x91e: v91e = CALLER 
    0x91f: v91f = EQ v91e, v91d
    0x920: v920(0x98a) = CONST 
    0x923: JUMPI v920(0x98a), v91f

    Begin block 0x924
    prev=[0x904], succ=[]
    =================================
    0x924: v924(0x40) = CONST 
    0x927: v927 = MLOAD v924(0x40)
    0x928: v928(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x94a: MSTORE v927, v928(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x94b: v94b(0x20) = CONST 
    0x94d: v94d(0x4) = CONST 
    0x950: v950 = ADD v927, v94d(0x4)
    0x953: MSTORE v950, v94b(0x20)
    0x954: v954(0x24) = CONST 
    0x957: v957 = ADD v927, v954(0x24)
    0x958: MSTORE v957, v94b(0x20)
    0x959: v959(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x97a: v97a(0x44) = CONST 
    0x97d: v97d = ADD v927, v97a(0x44)
    0x97e: MSTORE v97d, v959(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x980: v980 = MLOAD v924(0x40)
    0x984: v984(0x0) = SUB v927, v980
    0x985: v985(0x64) = CONST 
    0x987: v987(0x64) = ADD v985(0x64), v984(0x0)
    0x989: REVERT v980, v987(0x64)

    Begin block 0x98a
    prev=[0x904], succ=[0x9b8, 0xa08]
    =================================
    0x98b: v98b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9a2: v9a2 = AND v98b(0xffffffffffffffffffffffffffffffffffffffff), v1dd
    0x9a3: v9a3(0x0) = CONST 
    0x9a7: MSTORE v9a3(0x0), v9a2
    0x9a8: v9a8(0x6) = CONST 
    0x9aa: v9aa(0x20) = CONST 
    0x9ac: MSTORE v9aa(0x20), v9a8(0x6)
    0x9ad: v9ad(0x40) = CONST 
    0x9b0: v9b0 = SHA3 v9a3(0x0), v9ad(0x40)
    0x9b1: v9b1 = SLOAD v9b0
    0x9b2: v9b2 = AND v9b1, v98b(0xffffffffffffffffffffffffffffffffffffffff)
    0x9b3: v9b3 = ISZERO v9b2
    0x9b4: v9b4(0xa08) = CONST 
    0x9b7: JUMPI v9b4(0xa08), v9b3

    Begin block 0x9b8
    prev=[0x98a], succ=[]
    =================================
    0x9b8: v9b8(0x40) = CONST 
    0x9ba: v9ba = MLOAD v9b8(0x40)
    0x9bb: v9bb(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9dd: MSTORE v9ba, v9bb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9de: v9de(0x4) = CONST 
    0x9e0: v9e0 = ADD v9de(0x4), v9ba
    0x9e3: v9e3(0x20) = CONST 
    0x9e5: v9e5 = ADD v9e3(0x20), v9e0
    0x9e8: v9e8(0x20) = SUB v9e5, v9e0
    0x9ea: MSTORE v9e0, v9e8(0x20)
    0x9eb: v9eb(0x31) = CONST 
    0x9ee: MSTORE v9e5, v9eb(0x31)
    0x9ef: v9ef(0x20) = CONST 
    0x9f1: v9f1 = ADD v9ef(0x20), v9e5
    0x9f3: v9f3(0x1ef6) = CONST 
    0x9f6: v9f6(0x31) = CONST 
    0x9f9: CODECOPY v9f1, v9f3(0x1ef6), v9f6(0x31)
    0x9fa: v9fa(0x40) = CONST 
    0x9fc: v9fc = ADD v9fa(0x40), v9f1
    0xa00: va00(0x40) = CONST 
    0xa02: va02 = MLOAD va00(0x40)
    0xa05: va05(0x84) = SUB v9fc, va02
    0xa07: REVERT va02, va05(0x84)

    Begin block 0xa08
    prev=[0x98a], succ=[0x14f2]
    =================================
    0xa09: va09(0x40) = CONST 
    0xa0b: va0b = MLOAD va09(0x40)
    0xa0c: va0c(0xa14) = CONST 
    0xa10: va10(0x14f2) = CONST 
    0xa13: JUMP va10(0x14f2)

    Begin block 0x14f2
    prev=[0xa08], succ=[0xa14]
    =================================
    0x14f3: v14f3(0x89b) = CONST 
    0x14f7: v14f7(0x1532) = CONST 
    0x14fb: CODECOPY va0b, v14f7(0x1532), v14f3(0x89b)
    0x14fc: v14fc = ADD v14f3(0x89b), va0b
    0x14fe: JUMP va0c(0xa14)

    Begin block 0xa14
    prev=[0x14f2], succ=[0xa27, 0xa30]
    =================================
    0xa15: va15(0x40) = CONST 
    0xa17: va17 = MLOAD va15(0x40)
    0xa1a: va1a(0x89b) = SUB v14fc, va17
    0xa1c: va1c(0x0) = CONST 
    0xa1e: va1e = CREATE va1c(0x0), va17, va1a(0x89b)
    0xa20: va20 = ISZERO va1e
    0xa22: va22 = ISZERO va20
    0xa23: va23(0xa30) = CONST 
    0xa26: JUMPI va23(0xa30), va22

    Begin block 0xa27
    prev=[0xa14], succ=[]
    =================================
    0xa27: va27 = RETURNDATASIZE 
    0xa28: va28(0x0) = CONST 
    0xa2b: RETURNDATACOPY va28(0x0), va28(0x0), va27
    0xa2c: va2c = RETURNDATASIZE 
    0xa2d: va2d(0x0) = CONST 
    0xa2f: REVERT va2d(0x0), va2c

    Begin block 0xa30
    prev=[0xa14], succ=[0xaf7, 0xafb]
    =================================
    0xa32: va32(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa49: va49 = AND va32(0xffffffffffffffffffffffffffffffffffffffff), v1dd
    0xa4a: va4a(0x0) = CONST 
    0xa4e: MSTORE va4a(0x0), va49
    0xa4f: va4f(0x6) = CONST 
    0xa51: va51(0x20) = CONST 
    0xa53: MSTORE va51(0x20), va4f(0x6)
    0xa54: va54(0x40) = CONST 
    0xa58: va58 = SHA3 va4a(0x0), va54(0x40)
    0xa5a: va5a = SLOAD va58
    0xa5b: va5b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xa7c: va7c = AND va5b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va5a
    0xa7f: va7f = AND va32(0xffffffffffffffffffffffffffffffffffffffff), va1e
    0xa83: va83 = OR va7f, va7c
    0xa87: SSTORE va58, va83
    0xa88: va88(0x2) = CONST 
    0xa8a: va8a = SLOAD va88(0x2)
    0xa8c: va8c = MLOAD va54(0x40)
    0xa8d: va8d(0xcf7a1d7700000000000000000000000000000000000000000000000000000000) = CONST 
    0xaaf: MSTORE va8c, va8d(0xcf7a1d7700000000000000000000000000000000000000000000000000000000)
    0xab0: vab0(0x100) = CONST 
    0xab5: vab5 = DIV va8a, vab0(0x100)
    0xab7: vab7 = AND va32(0xffffffffffffffffffffffffffffffffffffffff), vab5
    0xab8: vab8(0x4) = CONST 
    0xabb: vabb = ADD va8c, vab8(0x4)
    0xabc: MSTORE vabb, vab7
    0xabd: vabd(0x24) = CONST 
    0xac0: vac0 = ADD va8c, vabd(0x24)
    0xac3: MSTORE vac0, va4a(0x0)
    0xac4: vac4(0x60) = CONST 
    0xac6: vac6(0x44) = CONST 
    0xac9: vac9 = ADD va8c, vac6(0x44)
    0xaca: MSTORE vac9, vac4(0x60)
    0xacb: vacb(0x64) = CONST 
    0xace: vace = ADD va8c, vacb(0x64)
    0xad1: MSTORE vace, va4a(0x0)
    0xad3: vad3 = MLOAD va54(0x40)
    0xad7: vad7 = AND va32(0xffffffffffffffffffffffffffffffffffffffff), va83
    0xad9: vad9(0xcf7a1d77) = CONST 
    0xadf: vadf(0xa4) = CONST 
    0xae3: vae3 = ADD va8c, vadf(0xa4)
    0xae9: vae9(0x0) = SUB va8c, vad3
    0xaea: vaea(0xa4) = ADD vae9(0x0), vadf(0xa4)
    0xaef: vaef = EXTCODESIZE vad7
    0xaf0: vaf0 = ISZERO vaef
    0xaf2: vaf2 = ISZERO vaf0
    0xaf3: vaf3(0xafb) = CONST 
    0xaf6: JUMPI vaf3(0xafb), vaf2

    Begin block 0xaf7
    prev=[0xa30], succ=[]
    =================================
    0xaf7: vaf7(0x0) = CONST 
    0xafa: REVERT vaf7(0x0), vaf7(0x0)

    Begin block 0xafb
    prev=[0xa30], succ=[0xb06, 0xb0f]
    =================================
    0xafd: vafd = GAS 
    0xafe: vafe = CALL vafd, vad7, va4a(0x0), vad3, vaea(0xa4), vad3, va4a(0x0)
    0xaff: vaff = ISZERO vafe
    0xb01: vb01 = ISZERO vaff
    0xb02: vb02(0xb0f) = CONST 
    0xb05: JUMPI vb02(0xb0f), vb01

    Begin block 0xb06
    prev=[0xafb], succ=[]
    =================================
    0xb06: vb06 = RETURNDATASIZE 
    0xb07: vb07(0x0) = CONST 
    0xb0a: RETURNDATACOPY vb07(0x0), vb07(0x0), vb06
    0xb0b: vb0b = RETURNDATASIZE 
    0xb0c: vb0c(0x0) = CONST 
    0xb0e: REVERT vb0c(0x0), vb0b

    Begin block 0xb0f
    prev=[0xafb], succ=[0xba8, 0xbac]
    =================================
    0xb13: vb13(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb2a: vb2a = AND v1dd, vb13(0xffffffffffffffffffffffffffffffffffffffff)
    0xb2b: vb2b(0x0) = CONST 
    0xb2f: MSTORE vb2b(0x0), vb2a
    0xb30: vb30(0x6) = CONST 
    0xb32: vb32(0x20) = CONST 
    0xb34: MSTORE vb32(0x20), vb30(0x6)
    0xb35: vb35(0x40) = CONST 
    0xb39: vb39 = SHA3 vb2b(0x0), vb35(0x40)
    0xb3a: vb3a = SLOAD vb39
    0xb3b: vb3b(0x3) = CONST 
    0xb3d: vb3d = SLOAD vb3b(0x3)
    0xb3e: vb3e(0x4) = CONST 
    0xb41: vb41 = SLOAD vb3e(0x4)
    0xb43: vb43 = MLOAD vb35(0x40)
    0xb44: vb44(0xf8c8765e00000000000000000000000000000000000000000000000000000000) = CONST 
    0xb66: MSTORE vb43, vb44(0xf8c8765e00000000000000000000000000000000000000000000000000000000)
    0xb69: vb69 = AND vb13(0xffffffffffffffffffffffffffffffffffffffff), vb3d
    0xb6c: vb6c = ADD vb43, vb3e(0x4)
    0xb70: MSTORE vb6c, vb69
    0xb71: vb71 = ADDRESS 
    0xb72: vb72(0x24) = CONST 
    0xb75: vb75 = ADD vb43, vb72(0x24)
    0xb76: MSTORE vb75, vb71
    0xb78: vb78 = AND vb13(0xffffffffffffffffffffffffffffffffffffffff), vb41
    0xb79: vb79(0x44) = CONST 
    0xb7c: vb7c = ADD vb43, vb79(0x44)
    0xb7d: MSTORE vb7c, vb78
    0xb7e: vb7e(0x64) = CONST 
    0xb81: vb81 = ADD vb43, vb7e(0x64)
    0xb85: MSTORE vb81, vb2a
    0xb87: vb87 = MLOAD vb35(0x40)
    0xb89: vb89 = AND vb13(0xffffffffffffffffffffffffffffffffffffffff), vb3a
    0xb8c: vb8c(0xf8c8765e) = CONST 
    0xb92: vb92(0x84) = CONST 
    0xb96: vb96 = ADD vb43, vb92(0x84)
    0xb9a: vb9a(0x0) = SUB vb43, vb87
    0xb9b: vb9b(0x84) = ADD vb9a(0x0), vb92(0x84)
    0xba0: vba0 = EXTCODESIZE vb89
    0xba1: vba1 = ISZERO vba0
    0xba3: vba3 = ISZERO vba1
    0xba4: vba4(0xbac) = CONST 
    0xba7: JUMPI vba4(0xbac), vba3

    Begin block 0xba8
    prev=[0xb0f], succ=[]
    =================================
    0xba8: vba8(0x0) = CONST 
    0xbab: REVERT vba8(0x0), vba8(0x0)

    Begin block 0xbac
    prev=[0xb0f], succ=[0xbb7, 0xbc0]
    =================================
    0xbae: vbae = GAS 
    0xbaf: vbaf = CALL vbae, vb89, vb2b(0x0), vb87, vb9b(0x84), vb87, vb2b(0x0)
    0xbb0: vbb0 = ISZERO vbaf
    0xbb2: vbb2 = ISZERO vbb0
    0xbb3: vbb3(0xbc0) = CONST 
    0xbb6: JUMPI vbb3(0xbc0), vbb2

    Begin block 0xbb7
    prev=[0xbac], succ=[]
    =================================
    0xbb7: vbb7 = RETURNDATASIZE 
    0xbb8: vbb8(0x0) = CONST 
    0xbbb: RETURNDATACOPY vbb8(0x0), vbb8(0x0), vbb7
    0xbbc: vbbc = RETURNDATASIZE 
    0xbbd: vbbd(0x0) = CONST 
    0xbbf: REVERT vbbd(0x0), vbbc

    Begin block 0xbc0
    prev=[0xbac], succ=[0x21df]
    =================================
    0xbc3: vbc3(0x5) = CONST 
    0xbc6: vbc6 = SLOAD vbc3(0x5)
    0xbc7: vbc7(0x1) = CONST 
    0xbca: vbca = ADD vbc6, vbc7(0x1)
    0xbcc: SSTORE vbc3(0x5), vbca
    0xbcd: vbcd(0x0) = CONST 
    0xbd2: MSTORE vbcd(0x0), vbc3(0x5)
    0xbd3: vbd3(0x36b6384b5eca791c62761152d0c79bb0604c104a5fb6f4eb0703f3154bb3db0) = CONST 
    0xbf4: vbf4 = ADD vbd3(0x36b6384b5eca791c62761152d0c79bb0604c104a5fb6f4eb0703f3154bb3db0), vbc6
    0xbf6: vbf6 = SLOAD vbf4
    0xbf7: vbf7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xc18: vc18 = AND vbf7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vbf6
    0xc19: vc19(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc31: vc31 = AND vc19(0xffffffffffffffffffffffffffffffffffffffff), v1dd
    0xc35: vc35 = OR vc31, vc18
    0xc38: SSTORE vbf4, vc35
    0xc3b: JUMP v1b0(0x21df)

    Begin block 0x21df
    prev=[0xbc0], succ=[]
    =================================
    0x21e0: STOP 

}

function SEALED_TIME()() public {
    Begin block 0x1e2
    prev=[], succ=[0xc3c]
    =================================
    0x1e3: v1e3(0x2200) = CONST 
    0x1e6: v1e6(0xc3c) = CONST 
    0x1e9: JUMP v1e6(0xc3c)

    Begin block 0xc3c
    prev=[0x1e2], succ=[0x2200]
    =================================
    0xc3d: vc3d(0x1) = CONST 
    0xc3f: vc3f = SLOAD vc3d(0x1)
    0xc41: JUMP v1e3(0x2200)

    Begin block 0x2200
    prev=[0xc3c], succ=[]
    =================================
    0x2201: v2201(0x40) = CONST 
    0x2204: v2204 = MLOAD v2201(0x40)
    0x2207: MSTORE v2204, vc3f
    0x2208: v2208 = MLOAD v2201(0x40)
    0x220c: v220c(0x0) = SUB v2204, v2208
    0x220d: v220d(0x20) = CONST 
    0x220f: v220f(0x20) = ADD v220d(0x20), v220c(0x0)
    0x2211: RETURN v2208, v220f(0x20)

}

function renounceOwnership()() public {
    Begin block 0x1fc
    prev=[], succ=[0xc42]
    =================================
    0x1fd: v1fd(0x2231) = CONST 
    0x200: v200(0xc42) = CONST 
    0x203: JUMP v200(0xc42)

    Begin block 0xc42
    prev=[0x1fc], succ=[0xc62, 0xcc8]
    =================================
    0xc43: vc43(0x0) = CONST 
    0xc45: vc45 = SLOAD vc43(0x0)
    0xc46: vc46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc5b: vc5b = AND vc46(0xffffffffffffffffffffffffffffffffffffffff), vc45
    0xc5c: vc5c = CALLER 
    0xc5d: vc5d = EQ vc5c, vc5b
    0xc5e: vc5e(0xcc8) = CONST 
    0xc61: JUMPI vc5e(0xcc8), vc5d

    Begin block 0xc62
    prev=[0xc42], succ=[]
    =================================
    0xc62: vc62(0x40) = CONST 
    0xc65: vc65 = MLOAD vc62(0x40)
    0xc66: vc66(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xc88: MSTORE vc65, vc66(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc89: vc89(0x20) = CONST 
    0xc8b: vc8b(0x4) = CONST 
    0xc8e: vc8e = ADD vc65, vc8b(0x4)
    0xc91: MSTORE vc8e, vc89(0x20)
    0xc92: vc92(0x24) = CONST 
    0xc95: vc95 = ADD vc65, vc92(0x24)
    0xc96: MSTORE vc95, vc89(0x20)
    0xc97: vc97(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xcb8: vcb8(0x44) = CONST 
    0xcbb: vcbb = ADD vc65, vcb8(0x44)
    0xcbc: MSTORE vcbb, vc97(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xcbe: vcbe = MLOAD vc62(0x40)
    0xcc2: vcc2(0x0) = SUB vc65, vcbe
    0xcc3: vcc3(0x64) = CONST 
    0xcc5: vcc5(0x64) = ADD vcc3(0x64), vcc2(0x0)
    0xcc7: REVERT vcbe, vcc5(0x64)

    Begin block 0xcc8
    prev=[0xc42], succ=[0x2231]
    =================================
    0xcc9: vcc9(0x0) = CONST 
    0xccc: vccc = SLOAD vcc9(0x0)
    0xccd: vccd(0x40) = CONST 
    0xccf: vccf = MLOAD vccd(0x40)
    0xcd0: vcd0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xce7: vce7 = AND vccc, vcd0(0xffffffffffffffffffffffffffffffffffffffff)
    0xce9: vce9(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xd0d: LOG3 vccf, vcc9(0x0), vce9(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vce7, vcc9(0x0)
    0xd0e: vd0e(0x0) = CONST 
    0xd11: vd11 = SLOAD vd0e(0x0)
    0xd12: vd12(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xd33: vd33 = AND vd12(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd11
    0xd35: SSTORE vd0e(0x0), vd33
    0xd36: JUMP v1fd(0x2231)

    Begin block 0x2231
    prev=[0xcc8], succ=[]
    =================================
    0x2232: STOP 

}

function cancelNewEpoch()() public {
    Begin block 0x204
    prev=[], succ=[0xd37]
    =================================
    0x205: v205(0x2252) = CONST 
    0x208: v208(0xd37) = CONST 
    0x20b: JUMP v208(0xd37)

    Begin block 0xd37
    prev=[0x204], succ=[0xd57, 0xdbd]
    =================================
    0xd38: vd38(0x0) = CONST 
    0xd3a: vd3a = SLOAD vd38(0x0)
    0xd3b: vd3b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd50: vd50 = AND vd3b(0xffffffffffffffffffffffffffffffffffffffff), vd3a
    0xd51: vd51 = CALLER 
    0xd52: vd52 = EQ vd51, vd50
    0xd53: vd53(0xdbd) = CONST 
    0xd56: JUMPI vd53(0xdbd), vd52

    Begin block 0xd57
    prev=[0xd37], succ=[]
    =================================
    0xd57: vd57(0x40) = CONST 
    0xd5a: vd5a = MLOAD vd57(0x40)
    0xd5b: vd5b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xd7d: MSTORE vd5a, vd5b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd7e: vd7e(0x20) = CONST 
    0xd80: vd80(0x4) = CONST 
    0xd83: vd83 = ADD vd5a, vd80(0x4)
    0xd86: MSTORE vd83, vd7e(0x20)
    0xd87: vd87(0x24) = CONST 
    0xd8a: vd8a = ADD vd5a, vd87(0x24)
    0xd8b: MSTORE vd8a, vd7e(0x20)
    0xd8c: vd8c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xdad: vdad(0x44) = CONST 
    0xdb0: vdb0 = ADD vd5a, vdad(0x44)
    0xdb1: MSTORE vdb0, vd8c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xdb3: vdb3 = MLOAD vd57(0x40)
    0xdb7: vdb7(0x0) = SUB vd5a, vdb3
    0xdb8: vdb8(0x64) = CONST 
    0xdba: vdba(0x64) = ADD vdb8(0x64), vdb7(0x0)
    0xdbc: REVERT vdb3, vdba(0x64)

    Begin block 0xdbd
    prev=[0xd37], succ=[0x14ffB0xdbd]
    =================================
    0xdbe: vdbe(0x8) = CONST 
    0xdc0: vdc0 = SLOAD vdbe(0x8)
    0xdc1: vdc1(0x1) = CONST 
    0xdc5: vdc5 = ADD vdc1(0x1), vdc0
    0xdc6: vdc6(0x0) = CONST 
    0xdca: MSTORE vdc6(0x0), vdc5
    0xdcb: vdcb(0x7) = CONST 
    0xdcd: vdcd(0x20) = CONST 
    0xdcf: MSTORE vdcd(0x20), vdcb(0x7)
    0xdd0: vdd0(0x40) = CONST 
    0xdd3: vdd3 = SHA3 vdc6(0x0), vdd0(0x40)
    0xdd6: SSTORE vdd3, vdc6(0x0)
    0xdd9: vdd9 = ADD vdd3, vdc1(0x1)
    0xddc: SSTORE vdd9, vdc6(0x0)
    0xddd: vddd(0x2) = CONST 
    0xde0: vde0 = ADD vdd3, vddd(0x2)
    0xde3: SSTORE vde0, vdc6(0x0)
    0xde4: vde4(0xdf0) = CONST 
    0xde7: vde7(0x3) = CONST 
    0xdea: vdea = ADD vdd3, vde7(0x3)
    0xdec: vdec(0x14ff) = CONST 
    0xdef: JUMP vdec(0x14ff), vdc6(0x0), vdea, vde4(0xdf0)

    Begin block 0x14ffB0xdbd
    prev=[0xdbd], succ=[0x1519B0xdbd]
    =================================
    0x1502S0xdbd: v1502Vdbd = SLOAD vdea
    0x1503S0xdbd: v1503Vdbd(0x0) = CONST 
    0x1506S0xdbd: SSTORE vdea, v1503Vdbd(0x0)
    0x1508S0xdbd: v1508Vdbd(0x0) = CONST 
    0x150aS0xdbd: MSTORE v1508Vdbd(0x0), vdea
    0x150bS0xdbd: v150bVdbd(0x20) = CONST 
    0x150dS0xdbd: v150dVdbd(0x0) = CONST 
    0x150fS0xdbd: v150fVdbd = SHA3 v150dVdbd(0x0), v150bVdbd(0x20)
    0x1512S0xdbd: v1512Vdbd = ADD v150fVdbd, v1502Vdbd
    0x1514S0xdbd: v1514Vdbd(0x247a) = CONST 

    Begin block 0x1519B0xdbd
    prev=[0x1522B0xdbd, 0x14ffB0xdbd], succ=[0x1522B0xdbd, 0x152dB0xdbd]
    =================================
    0x1519_0x0S0xdbd: v1519_0Vdbd = PHI v1528Vdbd, v150fVdbd
    0x151cS0xdbd: v151cVdbd = GT v1512Vdbd, v1519_0Vdbd
    0x151dS0xdbd: v151dVdbd = ISZERO v151cVdbd
    0x151eS0xdbd: v151eVdbd(0x152d) = CONST 
    0x1521S0xdbd: JUMPI v151eVdbd(0x152d), v151dVdbd

    Begin block 0x1522B0xdbd
    prev=[0x1519B0xdbd], succ=[0x1519B0xdbd]
    =================================
    0x1522S0xdbd: v1522Vdbd(0x0) = CONST 
    0x1522_0x0S0xdbd: v1522_0Vdbd = PHI v1528Vdbd, v150fVdbd
    0x1525S0xdbd: SSTORE v1522_0Vdbd, v1522Vdbd(0x0)
    0x1526S0xdbd: v1526Vdbd(0x1) = CONST 
    0x1528S0xdbd: v1528Vdbd = ADD v1526Vdbd(0x1), v1522_0Vdbd
    0x1529S0xdbd: v1529Vdbd(0x1519) = CONST 
    0x152cS0xdbd: JUMP v1529Vdbd(0x1519)

    Begin block 0x152dB0xdbd
    prev=[0x1519B0xdbd], succ=[0x247aB0xdbd]
    =================================
    0x1530S0xdbd: JUMP v1514Vdbd(0x247a)

    Begin block 0x247aB0xdbd
    prev=[0x152dB0xdbd], succ=[0xdf0]
    =================================
    0x247cS0xdbd: JUMP vde4(0xdf0)

    Begin block 0xdf0
    prev=[0x247aB0xdbd], succ=[0x14ffB0xdf0]
    =================================
    0xdf1: vdf1(0xdfe) = CONST 
    0xdf4: vdf4(0x4) = CONST 
    0xdf7: vdf7 = ADD vdd3, vdf4(0x4)
    0xdf8: vdf8(0x0) = CONST 
    0xdfa: vdfa(0x14ff) = CONST 
    0xdfd: JUMP vdfa(0x14ff), vdf8(0x0), vdf7, vdf1(0xdfe)

    Begin block 0x14ffB0xdf0
    prev=[0xdf0], succ=[0x1519B0xdf0]
    =================================
    0x1502S0xdf0: v1502Vdf0 = SLOAD vdf7
    0x1503S0xdf0: v1503Vdf0(0x0) = CONST 
    0x1506S0xdf0: SSTORE vdf7, v1503Vdf0(0x0)
    0x1508S0xdf0: v1508Vdf0(0x0) = CONST 
    0x150aS0xdf0: MSTORE v1508Vdf0(0x0), vdf7
    0x150bS0xdf0: v150bVdf0(0x20) = CONST 
    0x150dS0xdf0: v150dVdf0(0x0) = CONST 
    0x150fS0xdf0: v150fVdf0 = SHA3 v150dVdf0(0x0), v150bVdf0(0x20)
    0x1512S0xdf0: v1512Vdf0 = ADD v150fVdf0, v1502Vdf0
    0x1514S0xdf0: v1514Vdf0(0x247a) = CONST 

    Begin block 0x1519B0xdf0
    prev=[0x1522B0xdf0, 0x14ffB0xdf0], succ=[0x1522B0xdf0, 0x152dB0xdf0]
    =================================
    0x1519_0x0S0xdf0: v1519_0Vdf0 = PHI v1528Vdf0, v150fVdf0
    0x151cS0xdf0: v151cVdf0 = GT v1512Vdf0, v1519_0Vdf0
    0x151dS0xdf0: v151dVdf0 = ISZERO v151cVdf0
    0x151eS0xdf0: v151eVdf0(0x152d) = CONST 
    0x1521S0xdf0: JUMPI v151eVdf0(0x152d), v151dVdf0

    Begin block 0x1522B0xdf0
    prev=[0x1519B0xdf0], succ=[0x1519B0xdf0]
    =================================
    0x1522S0xdf0: v1522Vdf0(0x0) = CONST 
    0x1522_0x0S0xdf0: v1522_0Vdf0 = PHI v1528Vdf0, v150fVdf0
    0x1525S0xdf0: SSTORE v1522_0Vdf0, v1522Vdf0(0x0)
    0x1526S0xdf0: v1526Vdf0(0x1) = CONST 
    0x1528S0xdf0: v1528Vdf0 = ADD v1526Vdf0(0x1), v1522_0Vdf0
    0x1529S0xdf0: v1529Vdf0(0x1519) = CONST 
    0x152cS0xdf0: JUMP v1529Vdf0(0x1519)

    Begin block 0x152dB0xdf0
    prev=[0x1519B0xdf0], succ=[0x247aB0xdf0]
    =================================
    0x1530S0xdf0: JUMP v1514Vdf0(0x247a)

    Begin block 0x247aB0xdf0
    prev=[0x152dB0xdf0], succ=[0xdfe]
    =================================
    0x247cS0xdf0: JUMP vdf1(0xdfe)

    Begin block 0xdfe
    prev=[0x247aB0xdf0], succ=[0x2252]
    =================================
    0xe00: ve00(0x0) = CONST 
    0xe02: ve02(0x5) = CONST 
    0xe05: ve05 = ADD vdd3, ve02(0x5)
    0xe06: SSTORE ve05, ve00(0x0)
    0xe07: ve07(0x6) = CONST 
    0xe09: ve09 = ADD ve07(0x6), vdd3
    0xe0b: ve0b = SLOAD ve09
    0xe0c: ve0c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0xe2d: ve2d = AND ve0c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), ve0b
    0xe2f: SSTORE ve09, ve2d
    0xe30: JUMP v205(0x2252)

    Begin block 0x2252
    prev=[0xdfe], succ=[]
    =================================
    0x2253: STOP 

}

function fallback()() public {
    Begin block 0x2056
    prev=[], succ=[]
    =================================
    0x2057: v2057(0x0) = CONST 
    0x205a: REVERT v2057(0x0), v2057(0x0)

}

function stakingEpoch(uint256)() public {
    Begin block 0x20c
    prev=[], succ=[0x21e, 0x222]
    =================================
    0x20d: v20d(0x229) = CONST 
    0x210: v210(0x4) = CONST 
    0x213: v213 = CALLDATASIZE 
    0x214: v214 = SUB v213, v210(0x4)
    0x215: v215(0x20) = CONST 
    0x218: v218 = LT v214, v215(0x20)
    0x219: v219 = ISZERO v218
    0x21a: v21a(0x222) = CONST 
    0x21d: JUMPI v21a(0x222), v219

    Begin block 0x21e
    prev=[0x20c], succ=[]
    =================================
    0x21e: v21e(0x0) = CONST 
    0x221: REVERT v21e(0x0), v21e(0x0)

    Begin block 0x222
    prev=[0x20c], succ=[0xe31]
    =================================
    0x224: v224 = CALLDATALOAD v210(0x4)
    0x225: v225(0xe31) = CONST 
    0x228: JUMP v225(0xe31)

    Begin block 0xe31
    prev=[0x222], succ=[0x229]
    =================================
    0xe32: ve32(0x7) = CONST 
    0xe34: ve34(0x20) = CONST 
    0xe36: MSTORE ve34(0x20), ve32(0x7)
    0xe37: ve37(0x0) = CONST 
    0xe3b: MSTORE ve37(0x0), v224
    0xe3c: ve3c(0x40) = CONST 
    0xe3f: ve3f = SHA3 ve37(0x0), ve3c(0x40)
    0xe41: ve41 = SLOAD ve3f
    0xe42: ve42(0x1) = CONST 
    0xe45: ve45 = ADD ve3f, ve42(0x1)
    0xe46: ve46 = SLOAD ve45
    0xe47: ve47(0x2) = CONST 
    0xe4a: ve4a = ADD ve3f, ve47(0x2)
    0xe4b: ve4b = SLOAD ve4a
    0xe4c: ve4c(0x5) = CONST 
    0xe4f: ve4f = ADD ve3f, ve4c(0x5)
    0xe50: ve50 = SLOAD ve4f
    0xe51: ve51(0x6) = CONST 
    0xe55: ve55 = ADD ve3f, ve51(0x6)
    0xe56: ve56 = SLOAD ve55
    0xe5e: ve5e(0xff) = CONST 
    0xe60: ve60 = AND ve5e(0xff), ve56
    0xe62: JUMP v20d(0x229)

    Begin block 0x229
    prev=[0xe31], succ=[]
    =================================
    0x22a: v22a(0x40) = CONST 
    0x22d: v22d = MLOAD v22a(0x40)
    0x230: MSTORE v22d, ve41
    0x231: v231(0x20) = CONST 
    0x234: v234 = ADD v22d, v231(0x20)
    0x238: MSTORE v234, ve46
    0x23b: v23b = ADD v22a(0x40), v22d
    0x23f: MSTORE v23b, ve4b
    0x240: v240(0x60) = CONST 
    0x243: v243 = ADD v22d, v240(0x60)
    0x244: MSTORE v243, ve50
    0x245: v245 = ISZERO ve60
    0x246: v246 = ISZERO v245
    0x247: v247(0x80) = CONST 
    0x24a: v24a = ADD v22d, v247(0x80)
    0x24b: MSTORE v24a, v246
    0x24c: v24c = MLOAD v22a(0x40)
    0x250: v250(0x0) = SUB v22d, v24c
    0x251: v251(0xa0) = CONST 
    0x253: v253(0xa0) = ADD v251(0xa0), v250(0x0)
    0x255: RETURN v24c, v253(0xa0)

}

function owner()() public {
    Begin block 0x256
    prev=[], succ=[0xe63]
    =================================
    0x257: v257(0x2273) = CONST 
    0x25a: v25a(0xe63) = CONST 
    0x25d: JUMP v25a(0xe63)

    Begin block 0xe63
    prev=[0x256], succ=[0x2273]
    =================================
    0xe64: ve64(0x0) = CONST 
    0xe66: ve66 = SLOAD ve64(0x0)
    0xe67: ve67(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe7c: ve7c = AND ve67(0xffffffffffffffffffffffffffffffffffffffff), ve66
    0xe7e: JUMP v257(0x2273)

    Begin block 0x2273
    prev=[0xe63], succ=[]
    =================================
    0x2274: v2274(0x40) = CONST 
    0x2277: v2277 = MLOAD v2274(0x40)
    0x2278: v2278(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x228f: v228f = AND ve7c, v2278(0xffffffffffffffffffffffffffffffffffffffff)
    0x2291: MSTORE v2277, v228f
    0x2292: v2292 = MLOAD v2274(0x40)
    0x2296: v2296(0x0) = SUB v2277, v2292
    0x2297: v2297(0x20) = CONST 
    0x2299: v2299(0x20) = ADD v2297(0x20), v2296(0x0)
    0x229b: RETURN v2292, v2299(0x20)

}

function setupNewEpoch(address[],uint256[],uint256,uint256)() public {
    Begin block 0x25e
    prev=[], succ=[0x270, 0x274]
    =================================
    0x25f: v25f(0x22bb) = CONST 
    0x262: v262(0x4) = CONST 
    0x265: v265 = CALLDATASIZE 
    0x266: v266 = SUB v265, v262(0x4)
    0x267: v267(0x80) = CONST 
    0x26a: v26a = LT v266, v267(0x80)
    0x26b: v26b = ISZERO v26a
    0x26c: v26c(0x274) = CONST 
    0x26f: JUMPI v26c(0x274), v26b

    Begin block 0x270
    prev=[0x25e], succ=[]
    =================================
    0x270: v270(0x0) = CONST 
    0x273: REVERT v270(0x0), v270(0x0)

    Begin block 0x274
    prev=[0x25e], succ=[0x28b, 0x28f]
    =================================
    0x276: v276 = ADD v262(0x4), v266
    0x278: v278(0x20) = CONST 
    0x27b: v27b(0x24) = ADD v262(0x4), v278(0x20)
    0x27d: v27d = CALLDATALOAD v262(0x4)
    0x27e: v27e(0x100000000) = CONST 
    0x285: v285 = GT v27d, v27e(0x100000000)
    0x286: v286 = ISZERO v285
    0x287: v287(0x28f) = CONST 
    0x28a: JUMPI v287(0x28f), v286

    Begin block 0x28b
    prev=[0x274], succ=[]
    =================================
    0x28b: v28b(0x0) = CONST 
    0x28e: REVERT v28b(0x0), v28b(0x0)

    Begin block 0x28f
    prev=[0x274], succ=[0x29d, 0x2a1]
    =================================
    0x291: v291 = ADD v262(0x4), v27d
    0x293: v293(0x20) = CONST 
    0x296: v296 = ADD v291, v293(0x20)
    0x297: v297 = GT v296, v276
    0x298: v298 = ISZERO v297
    0x299: v299(0x2a1) = CONST 
    0x29c: JUMPI v299(0x2a1), v298

    Begin block 0x29d
    prev=[0x28f], succ=[]
    =================================
    0x29d: v29d(0x0) = CONST 
    0x2a0: REVERT v29d(0x0), v29d(0x0)

    Begin block 0x2a1
    prev=[0x28f], succ=[0x2bf, 0x2c3]
    =================================
    0x2a3: v2a3 = CALLDATALOAD v291
    0x2a5: v2a5(0x20) = CONST 
    0x2a7: v2a7 = ADD v2a5(0x20), v291
    0x2aa: v2aa(0x20) = CONST 
    0x2ad: v2ad = MUL v2a3, v2aa(0x20)
    0x2af: v2af = ADD v2a7, v2ad
    0x2b0: v2b0 = GT v2af, v276
    0x2b1: v2b1(0x100000000) = CONST 
    0x2b8: v2b8 = GT v2a3, v2b1(0x100000000)
    0x2b9: v2b9 = OR v2b8, v2b0
    0x2ba: v2ba = ISZERO v2b9
    0x2bb: v2bb(0x2c3) = CONST 
    0x2be: JUMPI v2bb(0x2c3), v2ba

    Begin block 0x2bf
    prev=[0x2a1], succ=[]
    =================================
    0x2bf: v2bf(0x0) = CONST 
    0x2c2: REVERT v2bf(0x0), v2bf(0x0)

    Begin block 0x2c3
    prev=[0x2a1], succ=[0x30f, 0x313]
    =================================
    0x2c8: v2c8(0x20) = CONST 
    0x2ca: v2ca = MUL v2c8(0x20), v2a3
    0x2cb: v2cb(0x20) = CONST 
    0x2cd: v2cd = ADD v2cb(0x20), v2ca
    0x2ce: v2ce(0x40) = CONST 
    0x2d0: v2d0 = MLOAD v2ce(0x40)
    0x2d3: v2d3 = ADD v2d0, v2cd
    0x2d4: v2d4(0x40) = CONST 
    0x2d6: MSTORE v2d4(0x40), v2d3
    0x2de: MSTORE v2d0, v2a3
    0x2df: v2df(0x20) = CONST 
    0x2e1: v2e1 = ADD v2df(0x20), v2d0
    0x2e4: v2e4(0x20) = CONST 
    0x2e6: v2e6 = MUL v2e4(0x20), v2a3
    0x2ea: CALLDATACOPY v2e1, v2a7, v2e6
    0x2eb: v2eb(0x0) = CONST 
    0x2ee: v2ee = ADD v2e1, v2e6
    0x2f2: MSTORE v2ee, v2eb(0x0)
    0x2f8: v2f8(0x20) = CONST 
    0x2fb: v2fb(0x44) = ADD v27b(0x24), v2f8(0x20)
    0x2fe: v2fe = CALLDATALOAD v27b(0x24)
    0x302: v302(0x100000000) = CONST 
    0x309: v309 = GT v2fe, v302(0x100000000)
    0x30a: v30a = ISZERO v309
    0x30b: v30b(0x313) = CONST 
    0x30e: JUMPI v30b(0x313), v30a

    Begin block 0x30f
    prev=[0x2c3], succ=[]
    =================================
    0x30f: v30f(0x0) = CONST 
    0x312: REVERT v30f(0x0), v30f(0x0)

    Begin block 0x313
    prev=[0x2c3], succ=[0x321, 0x325]
    =================================
    0x315: v315 = ADD v262(0x4), v2fe
    0x317: v317(0x20) = CONST 
    0x31a: v31a = ADD v315, v317(0x20)
    0x31b: v31b = GT v31a, v276
    0x31c: v31c = ISZERO v31b
    0x31d: v31d(0x325) = CONST 
    0x320: JUMPI v31d(0x325), v31c

    Begin block 0x321
    prev=[0x313], succ=[]
    =================================
    0x321: v321(0x0) = CONST 
    0x324: REVERT v321(0x0), v321(0x0)

    Begin block 0x325
    prev=[0x313], succ=[0x343, 0x347]
    =================================
    0x327: v327 = CALLDATALOAD v315
    0x329: v329(0x20) = CONST 
    0x32b: v32b = ADD v329(0x20), v315
    0x32e: v32e(0x20) = CONST 
    0x331: v331 = MUL v327, v32e(0x20)
    0x333: v333 = ADD v32b, v331
    0x334: v334 = GT v333, v276
    0x335: v335(0x100000000) = CONST 
    0x33c: v33c = GT v327, v335(0x100000000)
    0x33d: v33d = OR v33c, v334
    0x33e: v33e = ISZERO v33d
    0x33f: v33f(0x347) = CONST 
    0x342: JUMPI v33f(0x347), v33e

    Begin block 0x343
    prev=[0x325], succ=[]
    =================================
    0x343: v343(0x0) = CONST 
    0x346: REVERT v343(0x0), v343(0x0)

    Begin block 0x347
    prev=[0x325], succ=[0xe7f]
    =================================
    0x34c: v34c(0x20) = CONST 
    0x34e: v34e = MUL v34c(0x20), v327
    0x34f: v34f(0x20) = CONST 
    0x351: v351 = ADD v34f(0x20), v34e
    0x352: v352(0x40) = CONST 
    0x354: v354 = MLOAD v352(0x40)
    0x357: v357 = ADD v354, v351
    0x358: v358(0x40) = CONST 
    0x35a: MSTORE v358(0x40), v357
    0x362: MSTORE v354, v327
    0x363: v363(0x20) = CONST 
    0x365: v365 = ADD v363(0x20), v354
    0x368: v368(0x20) = CONST 
    0x36a: v36a = MUL v368(0x20), v327
    0x36e: CALLDATACOPY v365, v32b, v36a
    0x36f: v36f(0x0) = CONST 
    0x372: v372 = ADD v365, v36a
    0x376: MSTORE v372, v36f(0x0)
    0x37d: v37d = CALLDATALOAD v2fb(0x44)
    0x382: v382(0x20) = CONST 
    0x384: v384(0x64) = ADD v382(0x20), v2fb(0x44)
    0x385: v385 = CALLDATALOAD v384(0x64)
    0x386: v386(0xe7f) = CONST 
    0x389: JUMP v386(0xe7f)

    Begin block 0xe7f
    prev=[0x347], succ=[0xe9f, 0xf05]
    =================================
    0xe80: ve80(0x0) = CONST 
    0xe82: ve82 = SLOAD ve80(0x0)
    0xe83: ve83(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe98: ve98 = AND ve83(0xffffffffffffffffffffffffffffffffffffffff), ve82
    0xe99: ve99 = CALLER 
    0xe9a: ve9a = EQ ve99, ve98
    0xe9b: ve9b(0xf05) = CONST 
    0xe9e: JUMPI ve9b(0xf05), ve9a

    Begin block 0xe9f
    prev=[0xe7f], succ=[]
    =================================
    0xe9f: ve9f(0x40) = CONST 
    0xea2: vea2 = MLOAD ve9f(0x40)
    0xea3: vea3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xec5: MSTORE vea2, vea3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xec6: vec6(0x20) = CONST 
    0xec8: vec8(0x4) = CONST 
    0xecb: vecb = ADD vea2, vec8(0x4)
    0xece: MSTORE vecb, vec6(0x20)
    0xecf: vecf(0x24) = CONST 
    0xed2: ved2 = ADD vea2, vecf(0x24)
    0xed3: MSTORE ved2, vec6(0x20)
    0xed4: ved4(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0xef5: vef5(0x44) = CONST 
    0xef8: vef8 = ADD vea2, vef5(0x44)
    0xef9: MSTORE vef8, ved4(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0xefb: vefb = MLOAD ve9f(0x40)
    0xeff: veff(0x0) = SUB vea2, vefb
    0xf00: vf00(0x64) = CONST 
    0xf02: vf02(0x64) = ADD vf00(0x64), veff(0x0)
    0xf04: REVERT vefb, vf02(0x64)

    Begin block 0xf05
    prev=[0xe7f], succ=[0xf0f, 0xf5f]
    =================================
    0xf07: vf07 = MLOAD v354
    0xf09: vf09 = MLOAD v2d0
    0xf0a: vf0a = EQ vf09, vf07
    0xf0b: vf0b(0xf5f) = CONST 
    0xf0e: JUMPI vf0b(0xf5f), vf0a

    Begin block 0xf0f
    prev=[0xf05], succ=[]
    =================================
    0xf0f: vf0f(0x40) = CONST 
    0xf11: vf11 = MLOAD vf0f(0x40)
    0xf12: vf12(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf34: MSTORE vf11, vf12(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf35: vf35(0x4) = CONST 
    0xf37: vf37 = ADD vf35(0x4), vf11
    0xf3a: vf3a(0x20) = CONST 
    0xf3c: vf3c = ADD vf3a(0x20), vf37
    0xf3f: vf3f(0x20) = SUB vf3c, vf37
    0xf41: MSTORE vf37, vf3f(0x20)
    0xf42: vf42(0x44) = CONST 
    0xf45: MSTORE vf3c, vf42(0x44)
    0xf46: vf46(0x20) = CONST 
    0xf48: vf48 = ADD vf46(0x20), vf3c
    0xf4a: vf4a(0x1eb2) = CONST 
    0xf4d: vf4d(0x44) = CONST 
    0xf50: CODECOPY vf48, vf4a(0x1eb2), vf4d(0x44)
    0xf51: vf51(0x60) = CONST 
    0xf53: vf53 = ADD vf51(0x60), vf48
    0xf57: vf57(0x40) = CONST 
    0xf59: vf59 = MLOAD vf57(0x40)
    0xf5c: vf5c(0xa4) = SUB vf53, vf59
    0xf5e: REVERT vf59, vf5c(0xa4)

    Begin block 0xf5f
    prev=[0xf05], succ=[0xf69, 0xfb9]
    =================================
    0xf60: vf60(0x0) = CONST 
    0xf63: vf63 = MLOAD v2d0
    0xf64: vf64 = GT vf63, vf60(0x0)
    0xf65: vf65(0xfb9) = CONST 
    0xf68: JUMPI vf65(0xfb9), vf64

    Begin block 0xf69
    prev=[0xf5f], succ=[]
    =================================
    0xf69: vf69(0x40) = CONST 
    0xf6b: vf6b = MLOAD vf69(0x40)
    0xf6c: vf6c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf8e: MSTORE vf6b, vf6c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf8f: vf8f(0x4) = CONST 
    0xf91: vf91 = ADD vf8f(0x4), vf6b
    0xf94: vf94(0x20) = CONST 
    0xf96: vf96 = ADD vf94(0x20), vf91
    0xf99: vf99(0x20) = SUB vf96, vf91
    0xf9b: MSTORE vf91, vf99(0x20)
    0xf9c: vf9c(0x45) = CONST 
    0xf9f: MSTORE vf96, vf9c(0x45)
    0xfa0: vfa0(0x20) = CONST 
    0xfa2: vfa2 = ADD vfa0(0x20), vf96
    0xfa4: vfa4(0x1f83) = CONST 
    0xfa7: vfa7(0x45) = CONST 
    0xfaa: CODECOPY vfa2, vfa4(0x1f83), vfa7(0x45)
    0xfab: vfab(0x60) = CONST 
    0xfad: vfad = ADD vfab(0x60), vfa2
    0xfb1: vfb1(0x40) = CONST 
    0xfb3: vfb3 = MLOAD vfb1(0x40)
    0xfb6: vfb6(0xa4) = SUB vfad, vfb3
    0xfb8: REVERT vfb3, vfb6(0xa4)

    Begin block 0xfb9
    prev=[0xf5f], succ=[0xfcf]
    =================================
    0xfba: vfba(0x8) = CONST 
    0xfbc: vfbc = SLOAD vfba(0x8)
    0xfbd: vfbd(0x1) = CONST 
    0xfbf: vfbf = ADD vfbd(0x1), vfbc
    0xfc0: vfc0(0x0) = CONST 
    0xfc4: MSTORE vfc0(0x0), vfbf
    0xfc5: vfc5(0x7) = CONST 
    0xfc7: vfc7(0x20) = CONST 
    0xfc9: MSTORE vfc7(0x20), vfc5(0x7)
    0xfca: vfca(0x40) = CONST 
    0xfcd: vfcd = SHA3 vfc0(0x0), vfca(0x40)

    Begin block 0xfcf
    prev=[0xfb9, 0x114c], succ=[0xfd9, 0x117c]
    =================================
    0xfcf_0x0: vfcf_0 = PHI vfc0(0x0), v1175
    0xfd1: vfd1 = MLOAD v2d0
    0xfd3: vfd3 = LT vfcf_0, vfd1
    0xfd4: vfd4 = ISZERO vfd3
    0xfd5: vfd5(0x117c) = CONST 
    0xfd8: JUMPI vfd5(0x117c), vfd4

    Begin block 0xfd9
    prev=[0xfcf], succ=[0xfe9, 0xfea]
    =================================
    0xfd9: vfd9(0x0) = CONST 
    0xfd9_0x0: vfd9_0 = PHI vfc0(0x0), v1175
    0xfdb: vfdb(0x6) = CONST 
    0xfdd: vfdd(0x0) = CONST 
    0xfe2: vfe2 = MLOAD v2d0
    0xfe4: vfe4 = LT vfd9_0, vfe2
    0xfe5: vfe5(0xfea) = CONST 
    0xfe8: JUMPI vfe5(0xfea), vfe4

    Begin block 0xfe9
    prev=[0xfd9], succ=[]
    =================================
    0xfe9: THROW 

    Begin block 0xfea
    prev=[0xfd9], succ=[0x1027, 0x1077]
    =================================
    0xfea_0x0: vfea_0 = PHI vfc0(0x0), v1175
    0xfeb: vfeb(0x20) = CONST 
    0xfef: vfef = MUL vfeb(0x20), vfea_0
    0xff3: vff3 = ADD vfef, v2d0
    0xff5: vff5 = ADD vfeb(0x20), vff3
    0xff6: vff6 = MLOAD vff5
    0xff7: vff7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x100e: v100e = AND vff7(0xffffffffffffffffffffffffffffffffffffffff), vff6
    0x1010: MSTORE vfdd(0x0), v100e
    0x1013: v1013(0x20) = ADD vfdd(0x0), vfeb(0x20)
    0x1017: MSTORE v1013(0x20), vfdb(0x6)
    0x1018: v1018(0x40) = CONST 
    0x101a: v101a(0x40) = ADD v1018(0x40), vfdd(0x0)
    0x101b: v101b(0x0) = CONST 
    0x101d: v101d = SHA3 v101b(0x0), v101a(0x40)
    0x101e: v101e = SLOAD v101d
    0x101f: v101f = AND v101e, vff7(0xffffffffffffffffffffffffffffffffffffffff)
    0x1023: v1023(0x1077) = CONST 
    0x1026: JUMPI v1023(0x1077), v101f

    Begin block 0x1027
    prev=[0xfea], succ=[]
    =================================
    0x1027: v1027(0x40) = CONST 
    0x1029: v1029 = MLOAD v1027(0x40)
    0x102a: v102a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x104c: MSTORE v1029, v102a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x104d: v104d(0x4) = CONST 
    0x104f: v104f = ADD v104d(0x4), v1029
    0x1052: v1052(0x20) = CONST 
    0x1054: v1054 = ADD v1052(0x20), v104f
    0x1057: v1057(0x20) = SUB v1054, v104f
    0x1059: MSTORE v104f, v1057(0x20)
    0x105a: v105a(0x43) = CONST 
    0x105d: MSTORE v1054, v105a(0x43)
    0x105e: v105e(0x20) = CONST 
    0x1060: v1060 = ADD v105e(0x20), v1054
    0x1062: v1062(0x1fc8) = CONST 
    0x1065: v1065(0x43) = CONST 
    0x1068: CODECOPY v1060, v1062(0x1fc8), v1065(0x43)
    0x1069: v1069(0x60) = CONST 
    0x106b: v106b = ADD v1069(0x60), v1060
    0x106f: v106f(0x40) = CONST 
    0x1071: v1071 = MLOAD v106f(0x40)
    0x1074: v1074(0xa4) = SUB v106b, v1071
    0x1076: REVERT v1071, v1074(0xa4)

    Begin block 0x1077
    prev=[0xfea], succ=[0x1082, 0x1083]
    =================================
    0x1077_0x1: v1077_1 = PHI vfc0(0x0), v1175
    0x107b: v107b = MLOAD v354
    0x107d: v107d = LT v1077_1, v107b
    0x107e: v107e(0x1083) = CONST 
    0x1081: JUMPI v107e(0x1083), v107d

    Begin block 0x1082
    prev=[0x1077], succ=[]
    =================================
    0x1082: THROW 

    Begin block 0x1083
    prev=[0x1077], succ=[0x1094, 0x10e4]
    =================================
    0x1083_0x0: v1083_0 = PHI vfc0(0x0), v1175
    0x1084: v1084(0x20) = CONST 
    0x1086: v1086 = MUL v1084(0x20), v1083_0
    0x1087: v1087(0x20) = CONST 
    0x1089: v1089 = ADD v1087(0x20), v1086
    0x108a: v108a = ADD v1089, v354
    0x108b: v108b = MLOAD v108a
    0x108c: v108c(0x0) = CONST 
    0x108e: v108e = EQ v108c(0x0), v108b
    0x108f: v108f = ISZERO v108e
    0x1090: v1090(0x10e4) = CONST 
    0x1093: JUMPI v1090(0x10e4), v108f

    Begin block 0x1094
    prev=[0x1083], succ=[]
    =================================
    0x1094: v1094(0x40) = CONST 
    0x1096: v1096 = MLOAD v1094(0x40)
    0x1097: v1097(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x10b9: MSTORE v1096, v1097(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10ba: v10ba(0x4) = CONST 
    0x10bc: v10bc = ADD v10ba(0x4), v1096
    0x10bf: v10bf(0x20) = CONST 
    0x10c1: v10c1 = ADD v10bf(0x20), v10bc
    0x10c4: v10c4(0x20) = SUB v10c1, v10bc
    0x10c6: MSTORE v10bc, v10c4(0x20)
    0x10c7: v10c7(0x42) = CONST 
    0x10ca: MSTORE v10c1, v10c7(0x42)
    0x10cb: v10cb(0x20) = CONST 
    0x10cd: v10cd = ADD v10cb(0x20), v10c1
    0x10cf: v10cf(0x1e70) = CONST 
    0x10d2: v10d2(0x42) = CONST 
    0x10d5: CODECOPY v10cd, v10cf(0x1e70), v10d2(0x42)
    0x10d6: v10d6(0x60) = CONST 
    0x10d8: v10d8 = ADD v10d6(0x60), v10cd
    0x10dc: v10dc(0x40) = CONST 
    0x10de: v10de = MLOAD v10dc(0x40)
    0x10e1: v10e1(0xa4) = SUB v10d8, v10de
    0x10e3: REVERT v10de, v10e1(0xa4)

    Begin block 0x10e4
    prev=[0x1083], succ=[0x114b, 0x114c]
    =================================
    0x10e4_0x1: v10e4_1 = PHI vfc0(0x0), v1175
    0x10e5: v10e5(0x3) = CONST 
    0x10e8: v10e8 = ADD vfcd, v10e5(0x3)
    0x10ea: v10ea = SLOAD v10e8
    0x10eb: v10eb(0x1) = CONST 
    0x10ee: v10ee = ADD v10ea, v10eb(0x1)
    0x10f0: SSTORE v10e8, v10ee
    0x10f1: v10f1(0x0) = CONST 
    0x10f5: MSTORE v10f1(0x0), v10e8
    0x10f6: v10f6(0x20) = CONST 
    0x10fa: v10fa = SHA3 v10f1(0x0), v10f6(0x20)
    0x10fb: v10fb = ADD v10fa, v10ea
    0x10fd: v10fd = SLOAD v10fb
    0x10fe: v10fe(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x111f: v111f = AND v10fe(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v10fd
    0x1120: v1120(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1136: v1136 = AND v101f, v1120(0xffffffffffffffffffffffffffffffffffffffff)
    0x1137: v1137 = OR v1136, v111f
    0x1139: SSTORE v10fb, v1137
    0x113b: v113b = MLOAD v354
    0x113c: v113c(0x4) = CONST 
    0x113f: v113f = ADD vfcd, v113c(0x4)
    0x1146: v1146 = LT v10e4_1, v113b
    0x1147: v1147(0x114c) = CONST 
    0x114a: JUMPI v1147(0x114c), v1146

    Begin block 0x114b
    prev=[0x10e4], succ=[]
    =================================
    0x114b: THROW 

    Begin block 0x114c
    prev=[0x10e4], succ=[0xfcf]
    =================================
    0x114c_0x0: v114c_0 = PHI vfc0(0x0), v1175
    0x114c_0x4: v114c_4 = PHI vfc0(0x0), v1175
    0x114d: v114d(0x20) = CONST 
    0x1151: v1151 = MUL v114d(0x20), v114c_0
    0x1155: v1155 = ADD v1151, v354
    0x1157: v1157 = ADD v114d(0x20), v1155
    0x1158: v1158 = MLOAD v1157
    0x115a: v115a = SLOAD v113f
    0x115b: v115b(0x1) = CONST 
    0x115f: v115f = ADD v115b(0x1), v115a
    0x1161: SSTORE v113f, v115f
    0x1162: v1162(0x0) = CONST 
    0x1166: MSTORE v1162(0x0), v113f
    0x116a: v116a = SHA3 v1162(0x0), v114d(0x20)
    0x116d: v116d = ADD v115a, v116a
    0x1171: SSTORE v116d, v1158
    0x1175: v1175 = ADD v115b(0x1), v114c_4
    0x1178: v1178(0xfcf) = CONST 
    0x117b: JUMP v1178(0xfcf)

    Begin block 0x117c
    prev=[0xfcf], succ=[0x22bb]
    =================================
    0x117e: v117e(0x1) = CONST 
    0x1182: v1182 = ADD vfcd, v117e(0x1)
    0x1186: SSTORE v1182, v37d
    0x1187: v1187(0x2) = CONST 
    0x118a: v118a = ADD vfcd, v1187(0x2)
    0x118e: SSTORE v118a, v385
    0x118f: v118f(0x8) = CONST 
    0x1191: v1191 = SLOAD v118f(0x8)
    0x1194: v1194 = ADD v117e(0x1), v1191
    0x1196: SSTORE vfcd, v1194
    0x1199: JUMP v25f(0x22bb)

    Begin block 0x22bb
    prev=[0x117c], succ=[]
    =================================
    0x22bc: STOP 

}

function stakingRewardsByStakingToken(address)() public {
    Begin block 0x38a
    prev=[], succ=[0x39c, 0x3a0]
    =================================
    0x38b: v38b(0x22dc) = CONST 
    0x38e: v38e(0x4) = CONST 
    0x391: v391 = CALLDATASIZE 
    0x392: v392 = SUB v391, v38e(0x4)
    0x393: v393(0x20) = CONST 
    0x396: v396 = LT v392, v393(0x20)
    0x397: v397 = ISZERO v396
    0x398: v398(0x3a0) = CONST 
    0x39b: JUMPI v398(0x3a0), v397

    Begin block 0x39c
    prev=[0x38a], succ=[]
    =================================
    0x39c: v39c(0x0) = CONST 
    0x39f: REVERT v39c(0x0), v39c(0x0)

    Begin block 0x3a0
    prev=[0x38a], succ=[0x119a]
    =================================
    0x3a2: v3a2 = CALLDATALOAD v38e(0x4)
    0x3a3: v3a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b8: v3b8 = AND v3a3(0xffffffffffffffffffffffffffffffffffffffff), v3a2
    0x3b9: v3b9(0x119a) = CONST 
    0x3bc: JUMP v3b9(0x119a)

    Begin block 0x119a
    prev=[0x3a0], succ=[0x22dc]
    =================================
    0x119b: v119b(0x6) = CONST 
    0x119d: v119d(0x20) = CONST 
    0x119f: MSTORE v119d(0x20), v119b(0x6)
    0x11a0: v11a0(0x0) = CONST 
    0x11a4: MSTORE v11a0(0x0), v3b8
    0x11a5: v11a5(0x40) = CONST 
    0x11a8: v11a8 = SHA3 v11a0(0x0), v11a5(0x40)
    0x11a9: v11a9 = SLOAD v11a8
    0x11aa: v11aa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11bf: v11bf = AND v11aa(0xffffffffffffffffffffffffffffffffffffffff), v11a9
    0x11c1: JUMP v38b(0x22dc)

    Begin block 0x22dc
    prev=[0x119a], succ=[]
    =================================
    0x22dd: v22dd(0x40) = CONST 
    0x22e0: v22e0 = MLOAD v22dd(0x40)
    0x22e1: v22e1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22f8: v22f8 = AND v11bf, v22e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x22fa: MSTORE v22e0, v22f8
    0x22fb: v22fb = MLOAD v22dd(0x40)
    0x22ff: v22ff(0x0) = SUB v22e0, v22fb
    0x2300: v2300(0x20) = CONST 
    0x2302: v2302(0x20) = ADD v2300(0x20), v22ff(0x0)
    0x2304: RETURN v22fb, v2302(0x20)

}

function initialize(address,address,address)() public {
    Begin block 0x3bd
    prev=[], succ=[0x3cf, 0x3d3]
    =================================
    0x3be: v3be(0x2324) = CONST 
    0x3c1: v3c1(0x4) = CONST 
    0x3c4: v3c4 = CALLDATASIZE 
    0x3c5: v3c5 = SUB v3c4, v3c1(0x4)
    0x3c6: v3c6(0x60) = CONST 
    0x3c9: v3c9 = LT v3c5, v3c6(0x60)
    0x3ca: v3ca = ISZERO v3c9
    0x3cb: v3cb(0x3d3) = CONST 
    0x3ce: JUMPI v3cb(0x3d3), v3ca

    Begin block 0x3cf
    prev=[0x3bd], succ=[]
    =================================
    0x3cf: v3cf(0x0) = CONST 
    0x3d2: REVERT v3cf(0x0), v3cf(0x0)

    Begin block 0x3d3
    prev=[0x3bd], succ=[0x11c2]
    =================================
    0x3d5: v3d5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3eb: v3eb = CALLDATALOAD v3c1(0x4)
    0x3ed: v3ed = AND v3d5(0xffffffffffffffffffffffffffffffffffffffff), v3eb
    0x3ef: v3ef(0x20) = CONST 
    0x3f2: v3f2(0x24) = ADD v3c1(0x4), v3ef(0x20)
    0x3f3: v3f3 = CALLDATALOAD v3f2(0x24)
    0x3f5: v3f5 = AND v3d5(0xffffffffffffffffffffffffffffffffffffffff), v3f3
    0x3f7: v3f7(0x40) = CONST 
    0x3fb: v3fb(0x44) = ADD v3c1(0x4), v3f7(0x40)
    0x3fc: v3fc = CALLDATALOAD v3fb(0x44)
    0x3fd: v3fd = AND v3fc, v3d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fe: v3fe(0x11c2) = CONST 
    0x401: JUMP v3fe(0x11c2)

    Begin block 0x11c2
    prev=[0x3d3], succ=[0x11ce, 0x121e]
    =================================
    0x11c3: v11c3(0x2) = CONST 
    0x11c5: v11c5 = SLOAD v11c3(0x2)
    0x11c6: v11c6(0xff) = CONST 
    0x11c8: v11c8 = AND v11c6(0xff), v11c5
    0x11c9: v11c9 = ISZERO v11c8
    0x11ca: v11ca(0x121e) = CONST 
    0x11cd: JUMPI v11ca(0x121e), v11c9

    Begin block 0x11ce
    prev=[0x11c2], succ=[]
    =================================
    0x11ce: v11ce(0x40) = CONST 
    0x11d0: v11d0 = MLOAD v11ce(0x40)
    0x11d1: v11d1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11f3: MSTORE v11d0, v11d1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11f4: v11f4(0x4) = CONST 
    0x11f6: v11f6 = ADD v11f4(0x4), v11d0
    0x11f9: v11f9(0x20) = CONST 
    0x11fb: v11fb = ADD v11f9(0x20), v11f6
    0x11fe: v11fe(0x20) = SUB v11fb, v11f6
    0x1200: MSTORE v11f6, v11fe(0x20)
    0x1201: v1201(0x41) = CONST 
    0x1204: MSTORE v11fb, v1201(0x41)
    0x1205: v1205(0x20) = CONST 
    0x1207: v1207 = ADD v1205(0x20), v11fb
    0x1209: v1209(0x1e2f) = CONST 
    0x120c: v120c(0x41) = CONST 
    0x120f: CODECOPY v1207, v1209(0x1e2f), v120c(0x41)
    0x1210: v1210(0x60) = CONST 
    0x1212: v1212 = ADD v1210(0x60), v1207
    0x1216: v1216(0x40) = CONST 
    0x1218: v1218 = MLOAD v1216(0x40)
    0x121b: v121b(0xa4) = SUB v1212, v1218
    0x121d: REVERT v1218, v121b(0xa4)

    Begin block 0x121e
    prev=[0x11c2], succ=[0x13baB0x121e]
    =================================
    0x121f: v121f(0x4) = CONST 
    0x1222: v1222 = SLOAD v121f(0x4)
    0x1223: v1223(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x123a: v123a = AND v3ed, v1223(0xffffffffffffffffffffffffffffffffffffffff)
    0x123b: v123b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x125e: v125e = AND v123b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1222
    0x125f: v125f = OR v125e, v123a
    0x1262: SSTORE v121f(0x4), v125f
    0x1263: v1263(0x3) = CONST 
    0x1266: v1266 = SLOAD v1263(0x3)
    0x1269: v1269 = AND v1223(0xffffffffffffffffffffffffffffffffffffffff), v3f5
    0x126b: v126b = AND v123b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1266
    0x126f: v126f = OR v126b, v1269
    0x1271: SSTORE v1263(0x3), v126f
    0x1272: v1272(0x2) = CONST 
    0x1275: v1275 = SLOAD v1272(0x2)
    0x1278: v1278 = AND v3fd, v1223(0xffffffffffffffffffffffffffffffffffffffff)
    0x1279: v1279(0x100) = CONST 
    0x127c: v127c = MUL v1279(0x100), v1278
    0x127d: v127d(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = CONST 
    0x12a0: v12a0 = AND v1275, v127d(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff)
    0x12a4: v12a4 = OR v12a0, v127c
    0x12a6: SSTORE v1272(0x2), v12a4
    0x12a7: v12a7(0x12af) = CONST 
    0x12aa: v12aa = CALLER 
    0x12ab: v12ab(0x13ba) = CONST 
    0x12ae: JUMP v12ab(0x13ba), v12aa, v12a7(0x12af)

    Begin block 0x13baB0x121e
    prev=[0x121e], succ=[0x13d6B0x121e, 0x1426B0x121e]
    =================================
    0x13bbS0x121e: v13bbV121e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13d1S0x121e: v13d1V121e = AND v12aa, v13bbV121e(0xffffffffffffffffffffffffffffffffffffffff)
    0x13d2S0x121e: v13d2V121e(0x1426) = CONST 
    0x13d5S0x121e: JUMPI v13d2V121e(0x1426), v13d1V121e

    Begin block 0x13d6B0x121e
    prev=[0x13baB0x121e], succ=[]
    =================================
    0x13d6S0x121e: v13d6V121e(0x40) = CONST 
    0x13d8S0x121e: v13d8V121e = MLOAD v13d6V121e(0x40)
    0x13d9S0x121e: v13d9V121e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x13fbS0x121e: MSTORE v13d8V121e, v13d9V121e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13fcS0x121e: v13fcV121e(0x4) = CONST 
    0x13feS0x121e: v13feV121e = ADD v13fcV121e(0x4), v13d8V121e
    0x1401S0x121e: v1401V121e(0x20) = CONST 
    0x1403S0x121e: v1403V121e = ADD v1401V121e(0x20), v13feV121e
    0x1406S0x121e: v1406V121e(0x20) = SUB v1403V121e, v13feV121e
    0x1408S0x121e: MSTORE v13feV121e, v1406V121e(0x20)
    0x1409S0x121e: v1409V121e(0x26) = CONST 
    0x140cS0x121e: MSTORE v1403V121e, v1409V121e(0x26)
    0x140dS0x121e: v140dV121e(0x20) = CONST 
    0x140fS0x121e: v140fV121e = ADD v140dV121e(0x20), v1403V121e
    0x1411S0x121e: v1411V121e(0x1dcd) = CONST 
    0x1414S0x121e: v1414V121e(0x26) = CONST 
    0x1417S0x121e: CODECOPY v140fV121e, v1411V121e(0x1dcd), v1414V121e(0x26)
    0x1418S0x121e: v1418V121e(0x40) = CONST 
    0x141aS0x121e: v141aV121e = ADD v1418V121e(0x40), v140fV121e
    0x141eS0x121e: v141eV121e(0x40) = CONST 
    0x1420S0x121e: v1420V121e = MLOAD v141eV121e(0x40)
    0x1423S0x121e: v1423V121e(0x84) = SUB v141aV121e, v1420V121e
    0x1425S0x121e: REVERT v1420V121e, v1423V121e(0x84)

    Begin block 0x1426B0x121e
    prev=[0x13baB0x121e], succ=[0x12af]
    =================================
    0x1427S0x121e: v1427V121e(0x0) = CONST 
    0x142aS0x121e: v142aV121e = SLOAD v1427V121e(0x0)
    0x142bS0x121e: v142bV121e(0x40) = CONST 
    0x142dS0x121e: v142dV121e = MLOAD v142bV121e(0x40)
    0x142eS0x121e: v142eV121e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1445S0x121e: v1445V121e = AND v12aa, v142eV121e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1448S0x121e: v1448V121e = AND v142aV121e, v142eV121e(0xffffffffffffffffffffffffffffffffffffffff)
    0x144aS0x121e: v144aV121e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x146cS0x121e: LOG3 v142dV121e, v1427V121e(0x0), v144aV121e(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1448V121e, v1445V121e
    0x146dS0x121e: v146dV121e(0x0) = CONST 
    0x1470S0x121e: v1470V121e = SLOAD v146dV121e(0x0)
    0x1471S0x121e: v1471V121e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1492S0x121e: v1492V121e = AND v1471V121e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1470V121e
    0x1493S0x121e: v1493V121e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14abS0x121e: v14abV121e = AND v1493V121e(0xffffffffffffffffffffffffffffffffffffffff), v12aa
    0x14afS0x121e: v14afV121e = OR v14abV121e, v1492V121e
    0x14b1S0x121e: SSTORE v146dV121e(0x0), v14afV121e
    0x14b2S0x121e: JUMP v12a7(0x12af)

    Begin block 0x12af
    prev=[0x1426B0x121e], succ=[0x2324]
    =================================
    0x12b2: v12b2(0x2) = CONST 
    0x12b5: v12b5 = SLOAD v12b2(0x2)
    0x12b6: v12b6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x12d7: v12d7 = AND v12b6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v12b5
    0x12d8: v12d8(0x1) = CONST 
    0x12da: v12da = OR v12d8(0x1), v12d7
    0x12dc: SSTORE v12b2(0x2), v12da
    0x12de: JUMP v3be(0x2324)

    Begin block 0x2324
    prev=[0x12af], succ=[]
    =================================
    0x2325: STOP 

}

function rewardsToken()() public {
    Begin block 0x402
    prev=[], succ=[0x12df]
    =================================
    0x403: v403(0x2345) = CONST 
    0x406: v406(0x12df) = CONST 
    0x409: JUMP v406(0x12df)

    Begin block 0x12df
    prev=[0x402], succ=[0x2345]
    =================================
    0x12e0: v12e0(0x4) = CONST 
    0x12e2: v12e2 = SLOAD v12e0(0x4)
    0x12e3: v12e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12f8: v12f8 = AND v12e3(0xffffffffffffffffffffffffffffffffffffffff), v12e2
    0x12fa: JUMP v403(0x2345)

    Begin block 0x2345
    prev=[0x12df], succ=[]
    =================================
    0x2346: v2346(0x40) = CONST 
    0x2349: v2349 = MLOAD v2346(0x40)
    0x234a: v234a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2361: v2361 = AND v12f8, v234a(0xffffffffffffffffffffffffffffffffffffffff)
    0x2363: MSTORE v2349, v2361
    0x2364: v2364 = MLOAD v2346(0x40)
    0x2368: v2368(0x0) = SUB v2349, v2364
    0x2369: v2369(0x20) = CONST 
    0x236b: v236b(0x20) = ADD v2369(0x20), v2368(0x0)
    0x236d: RETURN v2364, v236b(0x20)

}

function upcomingEpochId()() public {
    Begin block 0x40a
    prev=[], succ=[0x12fb]
    =================================
    0x40b: v40b(0x238d) = CONST 
    0x40e: v40e(0x12fb) = CONST 
    0x411: JUMP v40e(0x12fb)

    Begin block 0x12fb
    prev=[0x40a], succ=[0x238d]
    =================================
    0x12fc: v12fc(0x9) = CONST 
    0x12fe: v12fe = SLOAD v12fc(0x9)
    0x1300: JUMP v40b(0x238d)

    Begin block 0x238d
    prev=[0x12fb], succ=[]
    =================================
    0x238e: v238e(0x40) = CONST 
    0x2391: v2391 = MLOAD v238e(0x40)
    0x2394: MSTORE v2391, v12fe
    0x2395: v2395 = MLOAD v238e(0x40)
    0x2399: v2399(0x0) = SUB v2391, v2395
    0x239a: v239a(0x20) = CONST 
    0x239c: v239c(0x20) = ADD v239a(0x20), v2399(0x0)
    0x239e: RETURN v2395, v239c(0x20)

}

function implementationGetter()() public {
    Begin block 0x412
    prev=[], succ=[0x1301]
    =================================
    0x413: v413(0x23be) = CONST 
    0x416: v416(0x1301) = CONST 
    0x419: JUMP v416(0x1301)

    Begin block 0x1301
    prev=[0x412], succ=[0x23be]
    =================================
    0x1302: v1302(0x2) = CONST 
    0x1304: v1304 = SLOAD v1302(0x2)
    0x1305: v1305(0x100) = CONST 
    0x1309: v1309 = DIV v1304, v1305(0x100)
    0x130a: v130a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x131f: v131f = AND v130a(0xffffffffffffffffffffffffffffffffffffffff), v1309
    0x1321: JUMP v413(0x23be)

    Begin block 0x23be
    prev=[0x1301], succ=[]
    =================================
    0x23bf: v23bf(0x40) = CONST 
    0x23c2: v23c2 = MLOAD v23bf(0x40)
    0x23c3: v23c3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23da: v23da = AND v131f, v23c3(0xffffffffffffffffffffffffffffffffffffffff)
    0x23dc: MSTORE v23c2, v23da
    0x23dd: v23dd = MLOAD v23bf(0x40)
    0x23e1: v23e1(0x0) = SUB v23c2, v23dd
    0x23e2: v23e2(0x20) = CONST 
    0x23e4: v23e4(0x20) = ADD v23e2(0x20), v23e1(0x0)
    0x23e6: RETURN v23dd, v23e4(0x20)

}

function currentEpochId()() public {
    Begin block 0x41a
    prev=[], succ=[0x1322]
    =================================
    0x41b: v41b(0x2406) = CONST 
    0x41e: v41e(0x1322) = CONST 
    0x421: JUMP v41e(0x1322)

    Begin block 0x1322
    prev=[0x41a], succ=[0x2406]
    =================================
    0x1323: v1323(0x8) = CONST 
    0x1325: v1325 = SLOAD v1323(0x8)
    0x1327: JUMP v41b(0x2406)

    Begin block 0x2406
    prev=[0x1322], succ=[]
    =================================
    0x2407: v2407(0x40) = CONST 
    0x240a: v240a = MLOAD v2407(0x40)
    0x240d: MSTORE v240a, v1325
    0x240e: v240e = MLOAD v2407(0x40)
    0x2412: v2412(0x0) = SUB v240a, v240e
    0x2413: v2413(0x20) = CONST 
    0x2415: v2415(0x20) = ADD v2413(0x20), v2412(0x0)
    0x2417: RETURN v240e, v2415(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x422
    prev=[], succ=[0x434, 0x438]
    =================================
    0x423: v423(0x2437) = CONST 
    0x426: v426(0x4) = CONST 
    0x429: v429 = CALLDATASIZE 
    0x42a: v42a = SUB v429, v426(0x4)
    0x42b: v42b(0x20) = CONST 
    0x42e: v42e = LT v42a, v42b(0x20)
    0x42f: v42f = ISZERO v42e
    0x430: v430(0x438) = CONST 
    0x433: JUMPI v430(0x438), v42f

    Begin block 0x434
    prev=[0x422], succ=[]
    =================================
    0x434: v434(0x0) = CONST 
    0x437: REVERT v434(0x0), v434(0x0)

    Begin block 0x438
    prev=[0x422], succ=[0x1328]
    =================================
    0x43a: v43a = CALLDATALOAD v426(0x4)
    0x43b: v43b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x450: v450 = AND v43b(0xffffffffffffffffffffffffffffffffffffffff), v43a
    0x451: v451(0x1328) = CONST 
    0x454: JUMP v451(0x1328)

    Begin block 0x1328
    prev=[0x438], succ=[0x1348, 0x13ae]
    =================================
    0x1329: v1329(0x0) = CONST 
    0x132b: v132b = SLOAD v1329(0x0)
    0x132c: v132c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1341: v1341 = AND v132c(0xffffffffffffffffffffffffffffffffffffffff), v132b
    0x1342: v1342 = CALLER 
    0x1343: v1343 = EQ v1342, v1341
    0x1344: v1344(0x13ae) = CONST 
    0x1347: JUMPI v1344(0x13ae), v1343

    Begin block 0x1348
    prev=[0x1328], succ=[]
    =================================
    0x1348: v1348(0x40) = CONST 
    0x134b: v134b = MLOAD v1348(0x40)
    0x134c: v134c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x136e: MSTORE v134b, v134c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x136f: v136f(0x20) = CONST 
    0x1371: v1371(0x4) = CONST 
    0x1374: v1374 = ADD v134b, v1371(0x4)
    0x1377: MSTORE v1374, v136f(0x20)
    0x1378: v1378(0x24) = CONST 
    0x137b: v137b = ADD v134b, v1378(0x24)
    0x137c: MSTORE v137b, v136f(0x20)
    0x137d: v137d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x139e: v139e(0x44) = CONST 
    0x13a1: v13a1 = ADD v134b, v139e(0x44)
    0x13a2: MSTORE v13a1, v137d(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x13a4: v13a4 = MLOAD v1348(0x40)
    0x13a8: v13a8(0x0) = SUB v134b, v13a4
    0x13a9: v13a9(0x64) = CONST 
    0x13ab: v13ab(0x64) = ADD v13a9(0x64), v13a8(0x0)
    0x13ad: REVERT v13a4, v13ab(0x64)

    Begin block 0x13ae
    prev=[0x1328], succ=[0x13baB0x13ae]
    =================================
    0x13af: v13af(0x2458) = CONST 
    0x13b3: v13b3(0x13ba) = CONST 
    0x13b6: JUMP v13b3(0x13ba), v450, v13af(0x2458)

    Begin block 0x13baB0x13ae
    prev=[0x13ae], succ=[0x13d6B0x13ae, 0x1426B0x13ae]
    =================================
    0x13bbS0x13ae: v13bbV13ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13d1S0x13ae: v13d1V13ae = AND v450, v13bbV13ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x13d2S0x13ae: v13d2V13ae(0x1426) = CONST 
    0x13d5S0x13ae: JUMPI v13d2V13ae(0x1426), v13d1V13ae

    Begin block 0x13d6B0x13ae
    prev=[0x13baB0x13ae], succ=[]
    =================================
    0x13d6S0x13ae: v13d6V13ae(0x40) = CONST 
    0x13d8S0x13ae: v13d8V13ae = MLOAD v13d6V13ae(0x40)
    0x13d9S0x13ae: v13d9V13ae(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x13fbS0x13ae: MSTORE v13d8V13ae, v13d9V13ae(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13fcS0x13ae: v13fcV13ae(0x4) = CONST 
    0x13feS0x13ae: v13feV13ae = ADD v13fcV13ae(0x4), v13d8V13ae
    0x1401S0x13ae: v1401V13ae(0x20) = CONST 
    0x1403S0x13ae: v1403V13ae = ADD v1401V13ae(0x20), v13feV13ae
    0x1406S0x13ae: v1406V13ae(0x20) = SUB v1403V13ae, v13feV13ae
    0x1408S0x13ae: MSTORE v13feV13ae, v1406V13ae(0x20)
    0x1409S0x13ae: v1409V13ae(0x26) = CONST 
    0x140cS0x13ae: MSTORE v1403V13ae, v1409V13ae(0x26)
    0x140dS0x13ae: v140dV13ae(0x20) = CONST 
    0x140fS0x13ae: v140fV13ae = ADD v140dV13ae(0x20), v1403V13ae
    0x1411S0x13ae: v1411V13ae(0x1dcd) = CONST 
    0x1414S0x13ae: v1414V13ae(0x26) = CONST 
    0x1417S0x13ae: CODECOPY v140fV13ae, v1411V13ae(0x1dcd), v1414V13ae(0x26)
    0x1418S0x13ae: v1418V13ae(0x40) = CONST 
    0x141aS0x13ae: v141aV13ae = ADD v1418V13ae(0x40), v140fV13ae
    0x141eS0x13ae: v141eV13ae(0x40) = CONST 
    0x1420S0x13ae: v1420V13ae = MLOAD v141eV13ae(0x40)
    0x1423S0x13ae: v1423V13ae(0x84) = SUB v141aV13ae, v1420V13ae
    0x1425S0x13ae: REVERT v1420V13ae, v1423V13ae(0x84)

    Begin block 0x1426B0x13ae
    prev=[0x13baB0x13ae], succ=[0x2458]
    =================================
    0x1427S0x13ae: v1427V13ae(0x0) = CONST 
    0x142aS0x13ae: v142aV13ae = SLOAD v1427V13ae(0x0)
    0x142bS0x13ae: v142bV13ae(0x40) = CONST 
    0x142dS0x13ae: v142dV13ae = MLOAD v142bV13ae(0x40)
    0x142eS0x13ae: v142eV13ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1445S0x13ae: v1445V13ae = AND v450, v142eV13ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x1448S0x13ae: v1448V13ae = AND v142aV13ae, v142eV13ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x144aS0x13ae: v144aV13ae(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x146cS0x13ae: LOG3 v142dV13ae, v1427V13ae(0x0), v144aV13ae(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1448V13ae, v1445V13ae
    0x146dS0x13ae: v146dV13ae(0x0) = CONST 
    0x1470S0x13ae: v1470V13ae = SLOAD v146dV13ae(0x0)
    0x1471S0x13ae: v1471V13ae(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1492S0x13ae: v1492V13ae = AND v1471V13ae(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1470V13ae
    0x1493S0x13ae: v1493V13ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14abS0x13ae: v14abV13ae = AND v1493V13ae(0xffffffffffffffffffffffffffffffffffffffff), v450
    0x14afS0x13ae: v14afV13ae = OR v14abV13ae, v1492V13ae
    0x14b1S0x13ae: SSTORE v146dV13ae(0x0), v14afV13ae
    0x14b2S0x13ae: JUMP v13af(0x2458)

    Begin block 0x2458
    prev=[0x1426B0x13ae], succ=[0x2437]
    =================================
    0x245a: JUMP v423(0x2437)

    Begin block 0x2437
    prev=[0x2458], succ=[]
    =================================
    0x2438: STOP 

}

