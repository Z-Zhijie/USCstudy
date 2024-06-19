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
    prev=[0x0], succ=[0x1a, 0x2563]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x24bc: v24bc(0x2563) = CONST 
    0x24bd: JUMPI v24bc(0x2563), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x11a, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x5ead86c6) = CONST 
    0x26: v26 = GT v21(0x5ead86c6), v1f
    0x27: v27(0x11a) = CONST 
    0x2a: JUMPI v27(0x11a), v26

    Begin block 0x11a
    prev=[0x1a], succ=[0x192, 0x126]
    =================================
    0x11c: v11c(0x26cb32b7) = CONST 
    0x121: v121 = GT v11c(0x26cb32b7), v1f
    0x122: v122(0x192) = CONST 
    0x125: JUMPI v122(0x192), v121

    Begin block 0x192
    prev=[0x11a], succ=[0x1ce, 0x19e]
    =================================
    0x194: v194(0x177d4507) = CONST 
    0x199: v199 = GT v194(0x177d4507), v1f
    0x19a: v19a(0x1ce) = CONST 
    0x19d: JUMPI v19a(0x1ce), v199

    Begin block 0x1ce
    prev=[0x192], succ=[0x2500, 0x1da]
    =================================
    0x1d0: v1d0(0x25b22bc) = CONST 
    0x1d5: v1d5 = EQ v1d0(0x25b22bc), v1f
    0x24f8: v24f8(0x2500) = CONST 
    0x24f9: JUMPI v24f8(0x2500), v1d5

    Begin block 0x2500
    prev=[0x1ce], succ=[]
    =================================
    0x2501: v2501(0x200) = CONST 
    0x2502: CALLPRIVATE v2501(0x200)

    Begin block 0x1da
    prev=[0x1ce], succ=[0x2503, 0x1e5]
    =================================
    0x1db: v1db(0x1459457a) = CONST 
    0x1e0: v1e0 = EQ v1db(0x1459457a), v1f
    0x24fa: v24fa(0x2503) = CONST 
    0x24fb: JUMPI v24fa(0x2503), v1e0

    Begin block 0x2503
    prev=[0x1da], succ=[]
    =================================
    0x2504: v2504(0x228) = CONST 
    0x2505: CALLPRIVATE v2504(0x228)

    Begin block 0x1e5
    prev=[0x1da], succ=[0x2506, 0x1f0]
    =================================
    0x1e6: v1e6(0x155bf4e2) = CONST 
    0x1eb: v1eb = EQ v1e6(0x155bf4e2), v1f
    0x24fc: v24fc(0x2506) = CONST 
    0x24fd: JUMPI v24fc(0x2506), v1eb

    Begin block 0x2506
    prev=[0x1e5], succ=[]
    =================================
    0x2507: v2507(0x270) = CONST 
    0x2508: CALLPRIVATE v2507(0x270)

    Begin block 0x1f0
    prev=[0x1e5], succ=[0x2509, 0x1fb]
    =================================
    0x1f1: v1f1(0x1745145e) = CONST 
    0x1f6: v1f6 = EQ v1f1(0x1745145e), v1f
    0x24fe: v24fe(0x2509) = CONST 
    0x24ff: JUMPI v24fe(0x2509), v1f6

    Begin block 0x2509
    prev=[0x1f0], succ=[]
    =================================
    0x250a: v250a(0x2a9) = CONST 
    0x250b: CALLPRIVATE v250a(0x2a9)

    Begin block 0x1fb
    prev=[0x1f0], succ=[]
    =================================
    0x1fc: v1fc(0x0) = CONST 
    0x1ff: REVERT v1fc(0x0), v1fc(0x0)

    Begin block 0x19e
    prev=[0x192], succ=[0x250c, 0x1a9]
    =================================
    0x19f: v19f(0x177d4507) = CONST 
    0x1a4: v1a4 = EQ v19f(0x177d4507), v1f
    0x24f0: v24f0(0x250c) = CONST 
    0x24f1: JUMPI v24f0(0x250c), v1a4

    Begin block 0x250c
    prev=[0x19e], succ=[]
    =================================
    0x250d: v250d(0x2cf) = CONST 
    0x250e: CALLPRIVATE v250d(0x2cf)

    Begin block 0x1a9
    prev=[0x19e], succ=[0x250f, 0x1b4]
    =================================
    0x1aa: v1aa(0x1c6bbabc) = CONST 
    0x1af: v1af = EQ v1aa(0x1c6bbabc), v1f
    0x24f2: v24f2(0x250f) = CONST 
    0x24f3: JUMPI v24f2(0x250f), v1af

    Begin block 0x250f
    prev=[0x1a9], succ=[]
    =================================
    0x2510: v2510(0x2d7) = CONST 
    0x2511: CALLPRIVATE v2510(0x2d7)

    Begin block 0x1b4
    prev=[0x1a9], succ=[0x2512, 0x1bf]
    =================================
    0x1b5: v1b5(0x2341c963) = CONST 
    0x1ba: v1ba = EQ v1b5(0x2341c963), v1f
    0x24f4: v24f4(0x2512) = CONST 
    0x24f5: JUMPI v24f4(0x2512), v1ba

    Begin block 0x2512
    prev=[0x1b4], succ=[]
    =================================
    0x2513: v2513(0x2df) = CONST 
    0x2514: CALLPRIVATE v2513(0x2df)

    Begin block 0x1bf
    prev=[0x1b4], succ=[0x1ca, 0x2515]
    =================================
    0x1c0: v1c0(0x24d7806c) = CONST 
    0x1c5: v1c5 = EQ v1c0(0x24d7806c), v1f
    0x24f6: v24f6(0x2515) = CONST 
    0x24f7: JUMPI v24f6(0x2515), v1c5

    Begin block 0x1ca
    prev=[0x1bf], succ=[0x1eac]
    =================================
    0x1ca: v1ca(0x1eac) = CONST 
    0x1cd: JUMP v1ca(0x1eac)

    Begin block 0x1eac
    prev=[0x1ca], succ=[]
    =================================
    0x1ead: v1ead(0x0) = CONST 
    0x1eb0: REVERT v1ead(0x0), v1ead(0x0)

    Begin block 0x2515
    prev=[0x1bf], succ=[]
    =================================
    0x2516: v2516(0x2fc) = CONST 
    0x2517: CALLPRIVATE v2516(0x2fc)

    Begin block 0x126
    prev=[0x11a], succ=[0x161, 0x131]
    =================================
    0x127: v127(0x392e53cd) = CONST 
    0x12c: v12c = GT v127(0x392e53cd), v1f
    0x12d: v12d(0x161) = CONST 
    0x130: JUMPI v12d(0x161), v12c

    Begin block 0x161
    prev=[0x126], succ=[0x2518, 0x16d]
    =================================
    0x163: v163(0x26cb32b7) = CONST 
    0x168: v168 = EQ v163(0x26cb32b7), v1f
    0x24e8: v24e8(0x2518) = CONST 
    0x24e9: JUMPI v24e8(0x2518), v168

    Begin block 0x2518
    prev=[0x161], succ=[]
    =================================
    0x2519: v2519(0x336) = CONST 
    0x251a: CALLPRIVATE v2519(0x336)

    Begin block 0x16d
    prev=[0x161], succ=[0x251b, 0x178]
    =================================
    0x16e: v16e(0x29518514) = CONST 
    0x173: v173 = EQ v16e(0x29518514), v1f
    0x24ea: v24ea(0x251b) = CONST 
    0x24eb: JUMPI v24ea(0x251b), v173

    Begin block 0x251b
    prev=[0x16d], succ=[]
    =================================
    0x251c: v251c(0x35c) = CONST 
    0x251d: CALLPRIVATE v251c(0x35c)

    Begin block 0x178
    prev=[0x16d], succ=[0x251e, 0x183]
    =================================
    0x179: v179(0x332136ed) = CONST 
    0x17e: v17e = EQ v179(0x332136ed), v1f
    0x24ec: v24ec(0x251e) = CONST 
    0x24ed: JUMPI v24ec(0x251e), v17e

    Begin block 0x251e
    prev=[0x178], succ=[]
    =================================
    0x251f: v251f(0x382) = CONST 
    0x2520: CALLPRIVATE v251f(0x382)

    Begin block 0x183
    prev=[0x178], succ=[0x18e, 0x2521]
    =================================
    0x184: v184(0x34cdcf26) = CONST 
    0x189: v189 = EQ v184(0x34cdcf26), v1f
    0x24ee: v24ee(0x2521) = CONST 
    0x24ef: JUMPI v24ee(0x2521), v189

    Begin block 0x18e
    prev=[0x183], succ=[0x1e88]
    =================================
    0x18e: v18e(0x1e88) = CONST 
    0x191: JUMP v18e(0x1e88)

    Begin block 0x1e88
    prev=[0x18e], succ=[]
    =================================
    0x1e89: v1e89(0x0) = CONST 
    0x1e8c: REVERT v1e89(0x0), v1e89(0x0)

    Begin block 0x2521
    prev=[0x183], succ=[]
    =================================
    0x2522: v2522(0x38a) = CONST 
    0x2523: CALLPRIVATE v2522(0x38a)

    Begin block 0x131
    prev=[0x126], succ=[0x2524, 0x13c]
    =================================
    0x132: v132(0x392e53cd) = CONST 
    0x137: v137 = EQ v132(0x392e53cd), v1f
    0x24e0: v24e0(0x2524) = CONST 
    0x24e1: JUMPI v24e0(0x2524), v137

    Begin block 0x2524
    prev=[0x131], succ=[]
    =================================
    0x2525: v2525(0x3b0) = CONST 
    0x2526: CALLPRIVATE v2525(0x3b0)

    Begin block 0x13c
    prev=[0x131], succ=[0x2527, 0x147]
    =================================
    0x13d: v13d(0x3e47158c) = CONST 
    0x142: v142 = EQ v13d(0x3e47158c), v1f
    0x24e2: v24e2(0x2527) = CONST 
    0x24e3: JUMPI v24e2(0x2527), v142

    Begin block 0x2527
    prev=[0x13c], succ=[]
    =================================
    0x2528: v2528(0x3b8) = CONST 
    0x2529: CALLPRIVATE v2528(0x3b8)

    Begin block 0x147
    prev=[0x13c], succ=[0x252a, 0x152]
    =================================
    0x148: v148(0x485cc955) = CONST 
    0x14d: v14d = EQ v148(0x485cc955), v1f
    0x24e4: v24e4(0x252a) = CONST 
    0x24e5: JUMPI v24e4(0x252a), v14d

    Begin block 0x252a
    prev=[0x147], succ=[]
    =================================
    0x252b: v252b(0x3c0) = CONST 
    0x252c: CALLPRIVATE v252b(0x3c0)

    Begin block 0x152
    prev=[0x147], succ=[0x15d, 0x252d]
    =================================
    0x153: v153(0x5c60da1b) = CONST 
    0x158: v158 = EQ v153(0x5c60da1b), v1f
    0x24e6: v24e6(0x252d) = CONST 
    0x24e7: JUMPI v24e6(0x252d), v158

    Begin block 0x15d
    prev=[0x152], succ=[0x1e64]
    =================================
    0x15d: v15d(0x1e64) = CONST 
    0x160: JUMP v15d(0x1e64)

    Begin block 0x1e64
    prev=[0x15d], succ=[]
    =================================
    0x1e65: v1e65(0x0) = CONST 
    0x1e68: REVERT v1e65(0x0), v1e65(0x0)

    Begin block 0x252d
    prev=[0x152], succ=[]
    =================================
    0x252e: v252e(0x3ee) = CONST 
    0x252f: CALLPRIVATE v252e(0x3ee)

    Begin block 0x2b
    prev=[0x1a], succ=[0xad, 0x36]
    =================================
    0x2c: v2c(0x97c82253) = CONST 
    0x31: v31 = GT v2c(0x97c82253), v1f
    0x32: v32(0xad) = CONST 
    0x35: JUMPI v32(0xad), v31

    Begin block 0xad
    prev=[0x2b], succ=[0xe9, 0xb9]
    =================================
    0xaf: vaf(0x6d70f7ae) = CONST 
    0xb4: vb4 = GT vaf(0x6d70f7ae), v1f
    0xb5: vb5(0xe9) = CONST 
    0xb8: JUMPI vb5(0xe9), vb4

    Begin block 0xe9
    prev=[0xad], succ=[0x2530, 0xf5]
    =================================
    0xeb: veb(0x5ead86c6) = CONST 
    0xf0: vf0 = EQ veb(0x5ead86c6), v1f
    0x24d8: v24d8(0x2530) = CONST 
    0x24d9: JUMPI v24d8(0x2530), vf0

    Begin block 0x2530
    prev=[0xe9], succ=[]
    =================================
    0x2531: v2531(0x3f6) = CONST 
    0x2532: CALLPRIVATE v2531(0x3f6)

    Begin block 0xf5
    prev=[0xe9], succ=[0x100, 0x2533]
    =================================
    0xf6: vf6(0x6026978c) = CONST 
    0xfb: vfb = EQ vf6(0x6026978c), v1f
    0x24da: v24da(0x2533) = CONST 
    0x24db: JUMPI v24da(0x2533), vfb

    Begin block 0x100
    prev=[0xf5], succ=[0x2536, 0x10b]
    =================================
    0x101: v101(0x639d250b) = CONST 
    0x106: v106 = EQ v101(0x639d250b), v1f
    0x24dc: v24dc(0x2536) = CONST 
    0x24dd: JUMPI v24dc(0x2536), v106

    Begin block 0x2536
    prev=[0x100], succ=[]
    =================================
    0x2537: v2537(0x41b) = CONST 
    0x2538: CALLPRIVATE v2537(0x41b)

    Begin block 0x10b
    prev=[0x100], succ=[0x116, 0x2539]
    =================================
    0x10c: v10c(0x668f6ace) = CONST 
    0x111: v111 = EQ v10c(0x668f6ace), v1f
    0x24de: v24de(0x2539) = CONST 
    0x24df: JUMPI v24de(0x2539), v111

    Begin block 0x116
    prev=[0x10b], succ=[0x1e40]
    =================================
    0x116: v116(0x1e40) = CONST 
    0x119: JUMP v116(0x1e40)

    Begin block 0x1e40
    prev=[0x116], succ=[]
    =================================
    0x1e41: v1e41(0x0) = CONST 
    0x1e44: REVERT v1e41(0x0), v1e41(0x0)

    Begin block 0x2539
    prev=[0x10b], succ=[]
    =================================
    0x253a: v253a(0x438) = CONST 
    0x253b: CALLPRIVATE v253a(0x438)

    Begin block 0x2533
    prev=[0xf5], succ=[]
    =================================
    0x2534: v2534(0x3fe) = CONST 
    0x2535: CALLPRIVATE v2534(0x3fe)

    Begin block 0xb9
    prev=[0xad], succ=[0xc4, 0x253c]
    =================================
    0xba: vba(0x6d70f7ae) = CONST 
    0xbf: vbf = EQ vba(0x6d70f7ae), v1f
    0x24d0: v24d0(0x253c) = CONST 
    0x24d1: JUMPI v24d0(0x253c), vbf

    Begin block 0xc4
    prev=[0xb9], succ=[0x253f, 0xcf]
    =================================
    0xc5: vc5(0x8535a56b) = CONST 
    0xca: vca = EQ vc5(0x8535a56b), v1f
    0x24d2: v24d2(0x253f) = CONST 
    0x24d3: JUMPI v24d2(0x253f), vca

    Begin block 0x253f
    prev=[0xc4], succ=[]
    =================================
    0x2540: v2540(0x484) = CONST 
    0x2541: CALLPRIVATE v2540(0x484)

    Begin block 0xcf
    prev=[0xc4], succ=[0x2542, 0xda]
    =================================
    0xd0: vd0(0x877b9a67) = CONST 
    0xd5: vd5 = EQ vd0(0x877b9a67), v1f
    0x24d4: v24d4(0x2542) = CONST 
    0x24d5: JUMPI v24d4(0x2542), vd5

    Begin block 0x2542
    prev=[0xcf], succ=[]
    =================================
    0x2543: v2543(0x48c) = CONST 
    0x2544: CALLPRIVATE v2543(0x48c)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x2545]
    =================================
    0xdb: vdb(0x9068d3be) = CONST 
    0xe0: ve0 = EQ vdb(0x9068d3be), v1f
    0x24d6: v24d6(0x2545) = CONST 
    0x24d7: JUMPI v24d6(0x2545), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0x1e1c]
    =================================
    0xe5: ve5(0x1e1c) = CONST 
    0xe8: JUMP ve5(0x1e1c)

    Begin block 0x1e1c
    prev=[0xe5], succ=[]
    =================================
    0x1e1d: v1e1d(0x0) = CONST 
    0x1e20: REVERT v1e1d(0x0), v1e1d(0x0)

    Begin block 0x2545
    prev=[0xda], succ=[]
    =================================
    0x2546: v2546(0x4b2) = CONST 
    0x2547: CALLPRIVATE v2546(0x4b2)

    Begin block 0x253c
    prev=[0xb9], succ=[]
    =================================
    0x253d: v253d(0x45e) = CONST 
    0x253e: CALLPRIVATE v253d(0x45e)

    Begin block 0x36
    prev=[0x2b], succ=[0x7c, 0x41]
    =================================
    0x37: v37(0xbf672c8f) = CONST 
    0x3c: v3c = GT v37(0xbf672c8f), v1f
    0x3d: v3d(0x7c) = CONST 
    0x40: JUMPI v3d(0x7c), v3c

    Begin block 0x7c
    prev=[0x36], succ=[0x2548, 0x88]
    =================================
    0x7e: v7e(0x97c82253) = CONST 
    0x83: v83 = EQ v7e(0x97c82253), v1f
    0x24c8: v24c8(0x2548) = CONST 
    0x24c9: JUMPI v24c8(0x2548), v83

    Begin block 0x2548
    prev=[0x7c], succ=[]
    =================================
    0x2549: v2549(0x4ba) = CONST 
    0x254a: CALLPRIVATE v2549(0x4ba)

    Begin block 0x88
    prev=[0x7c], succ=[0x254b, 0x93]
    =================================
    0x89: v89(0xab20c9d8) = CONST 
    0x8e: v8e = EQ v89(0xab20c9d8), v1f
    0x24ca: v24ca(0x254b) = CONST 
    0x24cb: JUMPI v24ca(0x254b), v8e

    Begin block 0x254b
    prev=[0x88], succ=[]
    =================================
    0x254c: v254c(0x4e0) = CONST 
    0x254d: CALLPRIVATE v254c(0x4e0)

    Begin block 0x93
    prev=[0x88], succ=[0x254e, 0x9e]
    =================================
    0x94: v94(0xb61585f8) = CONST 
    0x99: v99 = EQ v94(0xb61585f8), v1f
    0x24cc: v24cc(0x254e) = CONST 
    0x24cd: JUMPI v24cc(0x254e), v99

    Begin block 0x254e
    prev=[0x93], succ=[]
    =================================
    0x254f: v254f(0x541) = CONST 
    0x2550: CALLPRIVATE v254f(0x541)

    Begin block 0x9e
    prev=[0x93], succ=[0xa9, 0x2551]
    =================================
    0x9f: v9f(0xbb48cd3a) = CONST 
    0xa4: va4 = EQ v9f(0xbb48cd3a), v1f
    0x24ce: v24ce(0x2551) = CONST 
    0x24cf: JUMPI v24ce(0x2551), va4

    Begin block 0xa9
    prev=[0x9e], succ=[0x1df8]
    =================================
    0xa9: va9(0x1df8) = CONST 
    0xac: JUMP va9(0x1df8)

    Begin block 0x1df8
    prev=[0xa9], succ=[]
    =================================
    0x1df9: v1df9(0x0) = CONST 
    0x1dfc: REVERT v1df9(0x0), v1df9(0x0)

    Begin block 0x2551
    prev=[0x9e], succ=[]
    =================================
    0x2552: v2552(0x592) = CONST 
    0x2553: CALLPRIVATE v2552(0x592)

    Begin block 0x41
    prev=[0x36], succ=[0x2554, 0x4c]
    =================================
    0x42: v42(0xbf672c8f) = CONST 
    0x47: v47 = EQ v42(0xbf672c8f), v1f
    0x24be: v24be(0x2554) = CONST 
    0x24bf: JUMPI v24be(0x2554), v47

    Begin block 0x2554
    prev=[0x41], succ=[]
    =================================
    0x2555: v2555(0x5b8) = CONST 
    0x2556: CALLPRIVATE v2555(0x5b8)

    Begin block 0x4c
    prev=[0x41], succ=[0x2557, 0x57]
    =================================
    0x4d: v4d(0xc4d66de8) = CONST 
    0x52: v52 = EQ v4d(0xc4d66de8), v1f
    0x24c0: v24c0(0x2557) = CONST 
    0x24c1: JUMPI v24c0(0x2557), v52

    Begin block 0x2557
    prev=[0x4c], succ=[]
    =================================
    0x2558: v2558(0x5fb) = CONST 
    0x2559: CALLPRIVATE v2558(0x5fb)

    Begin block 0x57
    prev=[0x4c], succ=[0x255a, 0x62]
    =================================
    0x58: v58(0xc87a8701) = CONST 
    0x5d: v5d = EQ v58(0xc87a8701), v1f
    0x24c2: v24c2(0x255a) = CONST 
    0x24c3: JUMPI v24c2(0x255a), v5d

    Begin block 0x255a
    prev=[0x57], succ=[]
    =================================
    0x255b: v255b(0x621) = CONST 
    0x255c: CALLPRIVATE v255b(0x621)

    Begin block 0x62
    prev=[0x57], succ=[0x255d, 0x6d]
    =================================
    0x63: v63(0xcee2a9cf) = CONST 
    0x68: v68 = EQ v63(0xcee2a9cf), v1f
    0x24c4: v24c4(0x255d) = CONST 
    0x24c5: JUMPI v24c4(0x255d), v68

    Begin block 0x255d
    prev=[0x62], succ=[]
    =================================
    0x255e: v255e(0x629) = CONST 
    0x255f: CALLPRIVATE v255e(0x629)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x2560]
    =================================
    0x6e: v6e(0xd0ea5f4d) = CONST 
    0x73: v73 = EQ v6e(0xd0ea5f4d), v1f
    0x24c6: v24c6(0x2560) = CONST 
    0x24c7: JUMPI v24c6(0x2560), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x1dd4]
    =================================
    0x78: v78(0x1dd4) = CONST 
    0x7b: JUMP v78(0x1dd4)

    Begin block 0x1dd4
    prev=[0x78], succ=[]
    =================================
    0x1dd5: v1dd5(0x0) = CONST 
    0x1dd8: REVERT v1dd5(0x0), v1dd5(0x0)

    Begin block 0x2560
    prev=[0x6d], succ=[]
    =================================
    0x2561: v2561(0x64f) = CONST 
    0x2562: CALLPRIVATE v2561(0x64f)

    Begin block 0x2563
    prev=[0x10], succ=[]
    =================================
    0x2564: v2564(0x1db0) = CONST 
    0x2565: CALLPRIVATE v2564(0x1db0)

}

function 0x1791(0x1791arg0x0, 0x1791arg0x1) private {
    Begin block 0x1791
    prev=[], succ=[0x17aa0x1791, 0x17a20x1791]
    =================================
    0x1792: v1792(0x0) = CONST 
    0x1794: v1794 = SLOAD v1792(0x0)
    0x1795: v1795(0x100) = CONST 
    0x1799: v1799 = DIV v1794, v1795(0x100)
    0x179a: v179a(0xff) = CONST 
    0x179c: v179c = AND v179a(0xff), v1799
    0x179e: v179e(0x17aa) = CONST 
    0x17a1: JUMPI v179e(0x17aa), v179c

    Begin block 0x17aa0x1791
    prev=[0x1791, 0x18eeB0x17a20x1791], succ=[0x17b80x1791, 0x17b00x1791]
    =================================
    0x17aa0x1791_0x0: v17aa1791_0 = PHI v179c, v18f1V17a21791
    0x17ac0x1791: v179117ac(0x17b8) = CONST 
    0x17af0x1791: JUMPI v179117ac(0x17b8), v17aa1791_0

    Begin block 0x17b80x1791
    prev=[0x17aa0x1791, 0x17b00x1791], succ=[0x17bd0x1791, 0x17f30x1791]
    =================================
    0x17b80x1791_0x0: v17b81791_0 = PHI v179c, v179117b7, v18f1V17a21791
    0x17b90x1791: v179117b9(0x17f3) = CONST 
    0x17bc0x1791: JUMPI v179117b9(0x17f3), v17b81791_0

    Begin block 0x17bd0x1791
    prev=[0x17b80x1791], succ=[]
    =================================
    0x17bd0x1791: v179117bd(0x40) = CONST 
    0x17bf0x1791: v179117bf = MLOAD v179117bd(0x40)
    0x17c00x1791: v179117c0(0x461bcd) = CONST 
    0x17c40x1791: v179117c4(0xe5) = CONST 
    0x17c60x1791: v179117c6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v179117c4(0xe5), v179117c0(0x461bcd)
    0x17c80x1791: MSTORE v179117bf, v179117c6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17c90x1791: v179117c9(0x4) = CONST 
    0x17cb0x1791: v179117cb = ADD v179117c9(0x4), v179117bf
    0x17ce0x1791: v179117ce(0x20) = CONST 
    0x17d00x1791: v179117d0 = ADD v179117ce(0x20), v179117cb
    0x17d30x1791: v179117d3(0x20) = SUB v179117d0, v179117cb
    0x17d50x1791: MSTORE v179117cb, v179117d3(0x20)
    0x17d60x1791: v179117d6(0x3d) = CONST 
    0x17d90x1791: MSTORE v179117d0, v179117d6(0x3d)
    0x17da0x1791: v179117da(0x20) = CONST 
    0x17dc0x1791: v179117dc = ADD v179117da(0x20), v179117d0
    0x17de0x1791: v179117de(0x1cf3) = CONST 
    0x17e10x1791: v179117e1(0x3d) = CONST 
    0x17e40x1791: CODECOPY v179117dc, v179117de(0x1cf3), v179117e1(0x3d)
    0x17e50x1791: v179117e5(0x40) = CONST 
    0x17e70x1791: v179117e7 = ADD v179117e5(0x40), v179117dc
    0x17eb0x1791: v179117eb(0x40) = CONST 
    0x17ed0x1791: v179117ed = MLOAD v179117eb(0x40)
    0x17f00x1791: v179117f0(0x84) = SUB v179117e7, v179117ed
    0x17f20x1791: REVERT v179117ed, v179117f0(0x84)

    Begin block 0x17f30x1791
    prev=[0x17b80x1791], succ=[0x18060x1791, 0x181e0x1791]
    =================================
    0x17f40x1791: v179117f4(0x0) = CONST 
    0x17f60x1791: v179117f6 = SLOAD v179117f4(0x0)
    0x17f70x1791: v179117f7(0x100) = CONST 
    0x17fb0x1791: v179117fb = DIV v179117f6, v179117f7(0x100)
    0x17fc0x1791: v179117fc(0xff) = CONST 
    0x17fe0x1791: v179117fe = AND v179117fc(0xff), v179117fb
    0x17ff0x1791: v179117ff = ISZERO v179117fe
    0x18010x1791: v17911801 = ISZERO v179117ff
    0x18020x1791: v17911802(0x181e) = CONST 
    0x18050x1791: JUMPI v17911802(0x181e), v17911801

    Begin block 0x18060x1791
    prev=[0x17f30x1791], succ=[0x181e0x1791]
    =================================
    0x18060x1791: v17911806(0x0) = CONST 
    0x18090x1791: v17911809 = SLOAD v17911806(0x0)
    0x180a0x1791: v1791180a(0xff) = CONST 
    0x180c0x1791: v1791180c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1791180a(0xff)
    0x180d0x1791: v1791180d(0xff00) = CONST 
    0x18100x1791: v17911810(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v1791180d(0xff00)
    0x18130x1791: v17911813 = AND v17911809, v17911810(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x18140x1791: v17911814(0x100) = CONST 
    0x18170x1791: v17911817 = OR v17911814(0x100), v17911813
    0x18180x1791: v17911818 = AND v17911817, v1791180c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x18190x1791: v17911819(0x1) = CONST 
    0x181b0x1791: v1791181b = OR v17911819(0x1), v17911818
    0x181d0x1791: SSTORE v17911806(0x0), v1791181b

    Begin block 0x181e0x1791
    prev=[0x18060x1791, 0x17f30x1791], succ=[0x1985B0x181e0x1791]
    =================================
    0x181f0x1791: v1791181f(0x1827) = CONST 
    0x18230x1791: v17911823(0x1985) = CONST 
    0x18260x1791: JUMP v17911823(0x1985), v1791arg0, v1791181f(0x1827)

    Begin block 0x1985B0x181e0x1791
    prev=[0x181e0x1791], succ=[0x1994B0x181e0x1791, 0x19caB0x181e0x1791]
    =================================
    0x1986S0x181e0x1791: v1986V181e1791(0x1) = CONST 
    0x1988S0x181e0x1791: v1988V181e1791(0x1) = CONST 
    0x198aS0x181e0x1791: v198aV181e1791(0xa0) = CONST 
    0x198cS0x181e0x1791: v198cV181e1791(0x10000000000000000000000000000000000000000) = SHL v198aV181e1791(0xa0), v1988V181e1791(0x1)
    0x198dS0x181e0x1791: v198dV181e1791(0xffffffffffffffffffffffffffffffffffffffff) = SUB v198cV181e1791(0x10000000000000000000000000000000000000000), v1986V181e1791(0x1)
    0x198fS0x181e0x1791: v198fV181e1791 = AND v1791arg0, v198dV181e1791(0xffffffffffffffffffffffffffffffffffffffff)
    0x1990S0x181e0x1791: v1990V181e1791(0x19ca) = CONST 
    0x1993S0x181e0x1791: JUMPI v1990V181e1791(0x19ca), v198fV181e1791

    Begin block 0x1994B0x181e0x1791
    prev=[0x1985B0x181e0x1791], succ=[]
    =================================
    0x1994S0x181e0x1791: v1994V181e1791(0x40) = CONST 
    0x1996S0x181e0x1791: v1996V181e1791 = MLOAD v1994V181e1791(0x40)
    0x1997S0x181e0x1791: v1997V181e1791(0x461bcd) = CONST 
    0x199bS0x181e0x1791: v199bV181e1791(0xe5) = CONST 
    0x199dS0x181e0x1791: v199dV181e1791(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v199bV181e1791(0xe5), v1997V181e1791(0x461bcd)
    0x199fS0x181e0x1791: MSTORE v1996V181e1791, v199dV181e1791(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19a0S0x181e0x1791: v19a0V181e1791(0x4) = CONST 
    0x19a2S0x181e0x1791: v19a2V181e1791 = ADD v19a0V181e1791(0x4), v1996V181e1791
    0x19a5S0x181e0x1791: v19a5V181e1791(0x20) = CONST 
    0x19a7S0x181e0x1791: v19a7V181e1791 = ADD v19a5V181e1791(0x20), v19a2V181e1791
    0x19aaS0x181e0x1791: v19aaV181e1791(0x20) = SUB v19a7V181e1791, v19a2V181e1791
    0x19acS0x181e0x1791: MSTORE v19a2V181e1791, v19aaV181e1791(0x20)
    0x19adS0x181e0x1791: v19adV181e1791(0x3e) = CONST 
    0x19b0S0x181e0x1791: MSTORE v19a7V181e1791, v19adV181e1791(0x3e)
    0x19b1S0x181e0x1791: v19b1V181e1791(0x20) = CONST 
    0x19b3S0x181e0x1791: v19b3V181e1791 = ADD v19b1V181e1791(0x20), v19a7V181e1791
    0x19b5S0x181e0x1791: v19b5V181e1791(0x1b27) = CONST 
    0x19b8S0x181e0x1791: v19b8V181e1791(0x3e) = CONST 
    0x19bbS0x181e0x1791: CODECOPY v19b3V181e1791, v19b5V181e1791(0x1b27), v19b8V181e1791(0x3e)
    0x19bcS0x181e0x1791: v19bcV181e1791(0x40) = CONST 
    0x19beS0x181e0x1791: v19beV181e1791 = ADD v19bcV181e1791(0x40), v19b3V181e1791
    0x19c2S0x181e0x1791: v19c2V181e1791(0x40) = CONST 
    0x19c4S0x181e0x1791: v19c4V181e1791 = MLOAD v19c2V181e1791(0x40)
    0x19c7S0x181e0x1791: v19c7V181e1791(0x84) = SUB v19beV181e1791, v19c4V181e1791
    0x19c9S0x181e0x1791: REVERT v19c4V181e1791, v19c7V181e1791(0x84)

    Begin block 0x19caB0x181e0x1791
    prev=[0x1985B0x181e0x1791], succ=[0x18270x1791]
    =================================
    0x19cbS0x181e0x1791: v19cbV181e1791(0x33) = CONST 
    0x19ceS0x181e0x1791: v19ceV181e1791 = SLOAD v19cbV181e1791(0x33)
    0x19cfS0x181e0x1791: v19cfV181e1791(0x1) = CONST 
    0x19d1S0x181e0x1791: v19d1V181e1791(0x1) = CONST 
    0x19d3S0x181e0x1791: v19d3V181e1791(0xa0) = CONST 
    0x19d5S0x181e0x1791: v19d5V181e1791(0x10000000000000000000000000000000000000000) = SHL v19d3V181e1791(0xa0), v19d1V181e1791(0x1)
    0x19d6S0x181e0x1791: v19d6V181e1791(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19d5V181e1791(0x10000000000000000000000000000000000000000), v19cfV181e1791(0x1)
    0x19d7S0x181e0x1791: v19d7V181e1791(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v19d6V181e1791(0xffffffffffffffffffffffffffffffffffffffff)
    0x19d8S0x181e0x1791: v19d8V181e1791 = AND v19d7V181e1791(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v19ceV181e1791
    0x19d9S0x181e0x1791: v19d9V181e1791(0x1) = CONST 
    0x19dbS0x181e0x1791: v19dbV181e1791(0x1) = CONST 
    0x19ddS0x181e0x1791: v19ddV181e1791(0xa0) = CONST 
    0x19dfS0x181e0x1791: v19dfV181e1791(0x10000000000000000000000000000000000000000) = SHL v19ddV181e1791(0xa0), v19dbV181e1791(0x1)
    0x19e0S0x181e0x1791: v19e0V181e1791(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19dfV181e1791(0x10000000000000000000000000000000000000000), v19d9V181e1791(0x1)
    0x19e2S0x181e0x1791: v19e2V181e1791 = AND v1791arg0, v19e0V181e1791(0xffffffffffffffffffffffffffffffffffffffff)
    0x19e5S0x181e0x1791: v19e5V181e1791 = OR v19e2V181e1791, v19d8V181e1791
    0x19e8S0x181e0x1791: SSTORE v19cbV181e1791(0x33), v19e5V181e1791
    0x19e9S0x181e0x1791: v19e9V181e1791(0x40) = CONST 
    0x19ebS0x181e0x1791: v19ebV181e1791 = MLOAD v19e9V181e1791(0x40)
    0x19ecS0x181e0x1791: v19ecV181e1791 = CALLER 
    0x19eeS0x181e0x1791: v19eeV181e1791(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e) = CONST 
    0x1a10S0x181e0x1791: v1a10V181e1791(0x0) = CONST 
    0x1a13S0x181e0x1791: LOG3 v19ebV181e1791, v1a10V181e1791(0x0), v19eeV181e1791(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e), v19ecV181e1791, v19e2V181e1791
    0x1a15S0x181e0x1791: JUMP v1791181f(0x1827)

    Begin block 0x18270x1791
    prev=[0x19caB0x181e0x1791], succ=[0x182e0x1791, 0x18390x1791]
    =================================
    0x18290x1791: v17911829 = ISZERO v179117ff
    0x182a0x1791: v1791182a(0x1839) = CONST 
    0x182d0x1791: JUMPI v1791182a(0x1839), v17911829

    Begin block 0x182e0x1791
    prev=[0x18270x1791], succ=[0x18390x1791]
    =================================
    0x182e0x1791: v1791182e(0x0) = CONST 
    0x18310x1791: v17911831 = SLOAD v1791182e(0x0)
    0x18320x1791: v17911832(0xff00) = CONST 
    0x18350x1791: v17911835(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v17911832(0xff00)
    0x18360x1791: v17911836 = AND v17911835(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v17911831
    0x18380x1791: SSTORE v1791182e(0x0), v17911836

    Begin block 0x18390x1791
    prev=[0x182e0x1791, 0x18270x1791], succ=[]
    =================================
    0x183c0x1791: RETURNPRIVATE v1791arg1

    Begin block 0x17b00x1791
    prev=[0x17aa0x1791], succ=[0x17b80x1791]
    =================================
    0x17b10x1791: v179117b1(0x0) = CONST 
    0x17b30x1791: v179117b3 = SLOAD v179117b1(0x0)
    0x17b40x1791: v179117b4(0xff) = CONST 
    0x17b60x1791: v179117b6 = AND v179117b4(0xff), v179117b3
    0x17b70x1791: v179117b7 = ISZERO v179117b6

    Begin block 0x17a20x1791
    prev=[0x1791], succ=[0x18eeB0x17a20x1791]
    =================================
    0x17a30x1791: v179117a3(0x17aa) = CONST 
    0x17a60x1791: v179117a6(0x18ee) = CONST 
    0x17a90x1791: JUMP v179117a6(0x18ee)

    Begin block 0x18eeB0x17a20x1791
    prev=[0x17a20x1791], succ=[0x17aa0x1791]
    =================================
    0x18efS0x17a20x1791: v18efV17a21791 = ADDRESS 
    0x18f0S0x17a20x1791: v18f0V17a21791 = EXTCODESIZE v18efV17a21791
    0x18f1S0x17a20x1791: v18f1V17a21791 = ISZERO v18f0V17a21791
    0x18f3S0x17a20x1791: JUMP v179117a3(0x17aa)

}

function fallback()() public {
    Begin block 0x1db0
    prev=[], succ=[]
    =================================
    0x1db1: v1db1(0x0) = CONST 
    0x1db4: REVERT v1db1(0x0), v1db1(0x0)

}

function updateImplementation(address)() public {
    Begin block 0x200
    prev=[], succ=[0x212, 0x216]
    =================================
    0x201: v201(0x1ed0) = CONST 
    0x204: v204(0x4) = CONST 
    0x207: v207 = CALLDATASIZE 
    0x208: v208 = SUB v207, v204(0x4)
    0x209: v209(0x20) = CONST 
    0x20c: v20c = LT v208, v209(0x20)
    0x20d: v20d = ISZERO v20c
    0x20e: v20e(0x216) = CONST 
    0x211: JUMPI v20e(0x216), v20d

    Begin block 0x212
    prev=[0x200], succ=[]
    =================================
    0x212: v212(0x0) = CONST 
    0x215: REVERT v212(0x0), v212(0x0)

    Begin block 0x216
    prev=[0x200], succ=[0x675]
    =================================
    0x218: v218 = CALLDATALOAD v204(0x4)
    0x219: v219(0x1) = CONST 
    0x21b: v21b(0x1) = CONST 
    0x21d: v21d(0xa0) = CONST 
    0x21f: v21f(0x10000000000000000000000000000000000000000) = SHL v21d(0xa0), v21b(0x1)
    0x220: v220(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21f(0x10000000000000000000000000000000000000000), v219(0x1)
    0x221: v221 = AND v220(0xffffffffffffffffffffffffffffffffffffffff), v218
    0x222: v222(0x675) = CONST 
    0x225: JUMP v222(0x675)

    Begin block 0x675
    prev=[0x216], succ=[0x67e]
    =================================
    0x676: v676(0x67e) = CONST 
    0x679: v679 = CALLER 
    0x67a: v67a(0xe53) = CONST 
    0x67d: v67d_0 = CALLPRIVATE v67a(0xe53), v679, v676(0x67e)

    Begin block 0x67e
    prev=[0x675], succ=[0x683, 0x6b9]
    =================================
    0x67f: v67f(0x6b9) = CONST 
    0x682: JUMPI v67f(0x6b9), v67d_0

    Begin block 0x683
    prev=[0x67e], succ=[]
    =================================
    0x683: v683(0x40) = CONST 
    0x685: v685 = MLOAD v683(0x40)
    0x686: v686(0x461bcd) = CONST 
    0x68a: v68a(0xe5) = CONST 
    0x68c: v68c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v68a(0xe5), v686(0x461bcd)
    0x68e: MSTORE v685, v68c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x68f: v68f(0x4) = CONST 
    0x691: v691 = ADD v68f(0x4), v685
    0x694: v694(0x20) = CONST 
    0x696: v696 = ADD v694(0x20), v691
    0x699: v699(0x20) = SUB v696, v691
    0x69b: MSTORE v691, v699(0x20)
    0x69c: v69c(0x34) = CONST 
    0x69f: MSTORE v696, v69c(0x34)
    0x6a0: v6a0(0x20) = CONST 
    0x6a2: v6a2 = ADD v6a0(0x20), v696
    0x6a4: v6a4(0x1bfb) = CONST 
    0x6a7: v6a7(0x34) = CONST 
    0x6aa: CODECOPY v6a2, v6a4(0x1bfb), v6a7(0x34)
    0x6ab: v6ab(0x40) = CONST 
    0x6ad: v6ad = ADD v6ab(0x40), v6a2
    0x6b1: v6b1(0x40) = CONST 
    0x6b3: v6b3 = MLOAD v6b1(0x40)
    0x6b6: v6b6(0x84) = SUB v6ad, v6b3
    0x6b8: REVERT v6b3, v6b6(0x84)

    Begin block 0x6b9
    prev=[0x67e], succ=[0x1ed0]
    =================================
    0x6ba: v6ba(0x39) = CONST 
    0x6bd: v6bd = SLOAD v6ba(0x39)
    0x6be: v6be(0x1) = CONST 
    0x6c0: v6c0(0x1) = CONST 
    0x6c2: v6c2(0xa0) = CONST 
    0x6c4: v6c4(0x10000000000000000000000000000000000000000) = SHL v6c2(0xa0), v6c0(0x1)
    0x6c5: v6c5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c4(0x10000000000000000000000000000000000000000), v6be(0x1)
    0x6c6: v6c6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v6c5(0xffffffffffffffffffffffffffffffffffffffff)
    0x6c7: v6c7 = AND v6c6(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v6bd
    0x6c8: v6c8(0x1) = CONST 
    0x6ca: v6ca(0x1) = CONST 
    0x6cc: v6cc(0xa0) = CONST 
    0x6ce: v6ce(0x10000000000000000000000000000000000000000) = SHL v6cc(0xa0), v6ca(0x1)
    0x6cf: v6cf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ce(0x10000000000000000000000000000000000000000), v6c8(0x1)
    0x6d1: v6d1 = AND v221, v6cf(0xffffffffffffffffffffffffffffffffffffffff)
    0x6d4: v6d4 = OR v6d1, v6c7
    0x6d7: SSTORE v6ba(0x39), v6d4
    0x6d8: v6d8(0x40) = CONST 
    0x6da: v6da = MLOAD v6d8(0x40)
    0x6db: v6db(0x87c4e67a766ffddda27f441d63853a36ae64fbb07775a7c59d395e064b204eeb) = CONST 
    0x6fd: v6fd(0x0) = CONST 
    0x700: LOG2 v6da, v6fd(0x0), v6db(0x87c4e67a766ffddda27f441d63853a36ae64fbb07775a7c59d395e064b204eeb), v6d1
    0x702: JUMP v201(0x1ed0)

    Begin block 0x1ed0
    prev=[0x6b9], succ=[]
    =================================
    0x1ed1: STOP 

}

function initialize(address,address,address,address,address)() public {
    Begin block 0x228
    prev=[], succ=[0x23a, 0x23e]
    =================================
    0x229: v229(0x1ef1) = CONST 
    0x22c: v22c(0x4) = CONST 
    0x22f: v22f = CALLDATASIZE 
    0x230: v230 = SUB v22f, v22c(0x4)
    0x231: v231(0xa0) = CONST 
    0x234: v234 = LT v230, v231(0xa0)
    0x235: v235 = ISZERO v234
    0x236: v236(0x23e) = CONST 
    0x239: JUMPI v236(0x23e), v235

    Begin block 0x23a
    prev=[0x228], succ=[]
    =================================
    0x23a: v23a(0x0) = CONST 
    0x23d: REVERT v23a(0x0), v23a(0x0)

    Begin block 0x23e
    prev=[0x228], succ=[0x703]
    =================================
    0x240: v240(0x1) = CONST 
    0x242: v242(0x1) = CONST 
    0x244: v244(0xa0) = CONST 
    0x246: v246(0x10000000000000000000000000000000000000000) = SHL v244(0xa0), v242(0x1)
    0x247: v247(0xffffffffffffffffffffffffffffffffffffffff) = SUB v246(0x10000000000000000000000000000000000000000), v240(0x1)
    0x249: v249 = CALLDATALOAD v22c(0x4)
    0x24b: v24b = AND v247(0xffffffffffffffffffffffffffffffffffffffff), v249
    0x24d: v24d(0x20) = CONST 
    0x250: v250(0x24) = ADD v22c(0x4), v24d(0x20)
    0x251: v251 = CALLDATALOAD v250(0x24)
    0x253: v253 = AND v247(0xffffffffffffffffffffffffffffffffffffffff), v251
    0x255: v255(0x40) = CONST 
    0x258: v258(0x44) = ADD v22c(0x4), v255(0x40)
    0x259: v259 = CALLDATALOAD v258(0x44)
    0x25b: v25b = AND v247(0xffffffffffffffffffffffffffffffffffffffff), v259
    0x25d: v25d(0x60) = CONST 
    0x260: v260(0x64) = ADD v22c(0x4), v25d(0x60)
    0x261: v261 = CALLDATALOAD v260(0x64)
    0x263: v263 = AND v247(0xffffffffffffffffffffffffffffffffffffffff), v261
    0x265: v265(0x80) = CONST 
    0x269: v269(0x84) = ADD v22c(0x4), v265(0x80)
    0x26a: v26a = CALLDATALOAD v269(0x84)
    0x26b: v26b = AND v26a, v247(0xffffffffffffffffffffffffffffffffffffffff)
    0x26c: v26c(0x703) = CONST 
    0x26f: JUMP v26c(0x703)

    Begin block 0x703
    prev=[0x23e], succ=[0x71c, 0x714]
    =================================
    0x704: v704(0x0) = CONST 
    0x706: v706 = SLOAD v704(0x0)
    0x707: v707(0x100) = CONST 
    0x70b: v70b = DIV v706, v707(0x100)
    0x70c: v70c(0xff) = CONST 
    0x70e: v70e = AND v70c(0xff), v70b
    0x710: v710(0x71c) = CONST 
    0x713: JUMPI v710(0x71c), v70e

    Begin block 0x71c
    prev=[0x703, 0x18eeB0x714], succ=[0x72a, 0x722]
    =================================
    0x71c_0x0: v71c_0 = PHI v70e, v18f1V714
    0x71e: v71e(0x72a) = CONST 
    0x721: JUMPI v71e(0x72a), v71c_0

    Begin block 0x72a
    prev=[0x71c, 0x722], succ=[0x72f, 0x765]
    =================================
    0x72a_0x0: v72a_0 = PHI v70e, v729, v18f1V714
    0x72b: v72b(0x765) = CONST 
    0x72e: JUMPI v72b(0x765), v72a_0

    Begin block 0x72f
    prev=[0x72a], succ=[]
    =================================
    0x72f: v72f(0x40) = CONST 
    0x731: v731 = MLOAD v72f(0x40)
    0x732: v732(0x461bcd) = CONST 
    0x736: v736(0xe5) = CONST 
    0x738: v738(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v736(0xe5), v732(0x461bcd)
    0x73a: MSTORE v731, v738(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x73b: v73b(0x4) = CONST 
    0x73d: v73d = ADD v73b(0x4), v731
    0x740: v740(0x20) = CONST 
    0x742: v742 = ADD v740(0x20), v73d
    0x745: v745(0x20) = SUB v742, v73d
    0x747: MSTORE v73d, v745(0x20)
    0x748: v748(0x3d) = CONST 
    0x74b: MSTORE v742, v748(0x3d)
    0x74c: v74c(0x20) = CONST 
    0x74e: v74e = ADD v74c(0x20), v742
    0x750: v750(0x1cf3) = CONST 
    0x753: v753(0x3d) = CONST 
    0x756: CODECOPY v74e, v750(0x1cf3), v753(0x3d)
    0x757: v757(0x40) = CONST 
    0x759: v759 = ADD v757(0x40), v74e
    0x75d: v75d(0x40) = CONST 
    0x75f: v75f = MLOAD v75d(0x40)
    0x762: v762(0x84) = SUB v759, v75f
    0x764: REVERT v75f, v762(0x84)

    Begin block 0x765
    prev=[0x72a], succ=[0x778, 0x790]
    =================================
    0x766: v766(0x0) = CONST 
    0x768: v768 = SLOAD v766(0x0)
    0x769: v769(0x100) = CONST 
    0x76d: v76d = DIV v768, v769(0x100)
    0x76e: v76e(0xff) = CONST 
    0x770: v770 = AND v76e(0xff), v76d
    0x771: v771 = ISZERO v770
    0x773: v773 = ISZERO v771
    0x774: v774(0x790) = CONST 
    0x777: JUMPI v774(0x790), v773

    Begin block 0x778
    prev=[0x765], succ=[0x790]
    =================================
    0x778: v778(0x0) = CONST 
    0x77b: v77b = SLOAD v778(0x0)
    0x77c: v77c(0xff) = CONST 
    0x77e: v77e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v77c(0xff)
    0x77f: v77f(0xff00) = CONST 
    0x782: v782(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v77f(0xff00)
    0x785: v785 = AND v77b, v782(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x786: v786(0x100) = CONST 
    0x789: v789 = OR v786(0x100), v785
    0x78a: v78a = AND v789, v77e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x78b: v78b(0x1) = CONST 
    0x78d: v78d = OR v78b(0x1), v78a
    0x78f: SSTORE v778(0x0), v78d

    Begin block 0x790
    prev=[0x778, 0x765], succ=[0x79f, 0x7d5]
    =================================
    0x791: v791(0x1) = CONST 
    0x793: v793(0x1) = CONST 
    0x795: v795(0xa0) = CONST 
    0x797: v797(0x10000000000000000000000000000000000000000) = SHL v795(0xa0), v793(0x1)
    0x798: v798(0xffffffffffffffffffffffffffffffffffffffff) = SUB v797(0x10000000000000000000000000000000000000000), v791(0x1)
    0x79a: v79a = AND v24b, v798(0xffffffffffffffffffffffffffffffffffffffff)
    0x79b: v79b(0x7d5) = CONST 
    0x79e: JUMPI v79b(0x7d5), v79a

    Begin block 0x79f
    prev=[0x790], succ=[]
    =================================
    0x79f: v79f(0x40) = CONST 
    0x7a1: v7a1 = MLOAD v79f(0x40)
    0x7a2: v7a2(0x461bcd) = CONST 
    0x7a6: v7a6(0xe5) = CONST 
    0x7a8: v7a8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7a6(0xe5), v7a2(0x461bcd)
    0x7aa: MSTORE v7a1, v7a8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7ab: v7ab(0x4) = CONST 
    0x7ad: v7ad = ADD v7ab(0x4), v7a1
    0x7b0: v7b0(0x20) = CONST 
    0x7b2: v7b2 = ADD v7b0(0x20), v7ad
    0x7b5: v7b5(0x20) = SUB v7b2, v7ad
    0x7b7: MSTORE v7ad, v7b5(0x20)
    0x7b8: v7b8(0x35) = CONST 
    0x7bb: MSTORE v7b2, v7b8(0x35)
    0x7bc: v7bc(0x20) = CONST 
    0x7be: v7be = ADD v7bc(0x20), v7b2
    0x7c0: v7c0(0x1d30) = CONST 
    0x7c3: v7c3(0x35) = CONST 
    0x7c6: CODECOPY v7be, v7c0(0x1d30), v7c3(0x35)
    0x7c7: v7c7(0x40) = CONST 
    0x7c9: v7c9 = ADD v7c7(0x40), v7be
    0x7cd: v7cd(0x40) = CONST 
    0x7cf: v7cf = MLOAD v7cd(0x40)
    0x7d2: v7d2(0x84) = SUB v7c9, v7cf
    0x7d4: REVERT v7cf, v7d2(0x84)

    Begin block 0x7d5
    prev=[0x790], succ=[0x7e4, 0x81a]
    =================================
    0x7d6: v7d6(0x1) = CONST 
    0x7d8: v7d8(0x1) = CONST 
    0x7da: v7da(0xa0) = CONST 
    0x7dc: v7dc(0x10000000000000000000000000000000000000000) = SHL v7da(0xa0), v7d8(0x1)
    0x7dd: v7dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7dc(0x10000000000000000000000000000000000000000), v7d6(0x1)
    0x7df: v7df = AND v263, v7dd(0xffffffffffffffffffffffffffffffffffffffff)
    0x7e0: v7e0(0x81a) = CONST 
    0x7e3: JUMPI v7e0(0x81a), v7df

    Begin block 0x7e4
    prev=[0x7d5], succ=[]
    =================================
    0x7e4: v7e4(0x40) = CONST 
    0x7e6: v7e6 = MLOAD v7e4(0x40)
    0x7e7: v7e7(0x461bcd) = CONST 
    0x7eb: v7eb(0xe5) = CONST 
    0x7ed: v7ed(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7eb(0xe5), v7e7(0x461bcd)
    0x7ef: MSTORE v7e6, v7ed(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7f0: v7f0(0x4) = CONST 
    0x7f2: v7f2 = ADD v7f0(0x4), v7e6
    0x7f5: v7f5(0x20) = CONST 
    0x7f7: v7f7 = ADD v7f5(0x20), v7f2
    0x7fa: v7fa(0x20) = SUB v7f7, v7f2
    0x7fc: MSTORE v7f2, v7fa(0x20)
    0x7fd: v7fd(0x3b) = CONST 
    0x800: MSTORE v7f7, v7fd(0x3b)
    0x801: v801(0x20) = CONST 
    0x803: v803 = ADD v801(0x20), v7f7
    0x805: v805(0x1aec) = CONST 
    0x808: v808(0x3b) = CONST 
    0x80b: CODECOPY v803, v805(0x1aec), v808(0x3b)
    0x80c: v80c(0x40) = CONST 
    0x80e: v80e = ADD v80c(0x40), v803
    0x812: v812(0x40) = CONST 
    0x814: v814 = MLOAD v812(0x40)
    0x817: v817(0x84) = SUB v80e, v814
    0x819: REVERT v814, v817(0x84)

    Begin block 0x81a
    prev=[0x7d5], succ=[0x829, 0x85f]
    =================================
    0x81b: v81b(0x1) = CONST 
    0x81d: v81d(0x1) = CONST 
    0x81f: v81f(0xa0) = CONST 
    0x821: v821(0x10000000000000000000000000000000000000000) = SHL v81f(0xa0), v81d(0x1)
    0x822: v822(0xffffffffffffffffffffffffffffffffffffffff) = SUB v821(0x10000000000000000000000000000000000000000), v81b(0x1)
    0x824: v824 = AND v26b, v822(0xffffffffffffffffffffffffffffffffffffffff)
    0x825: v825(0x85f) = CONST 
    0x828: JUMPI v825(0x85f), v824

    Begin block 0x829
    prev=[0x81a], succ=[]
    =================================
    0x829: v829(0x40) = CONST 
    0x82b: v82b = MLOAD v829(0x40)
    0x82c: v82c(0x461bcd) = CONST 
    0x830: v830(0xe5) = CONST 
    0x832: v832(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v830(0xe5), v82c(0x461bcd)
    0x834: MSTORE v82b, v832(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x835: v835(0x4) = CONST 
    0x837: v837 = ADD v835(0x4), v82b
    0x83a: v83a(0x20) = CONST 
    0x83c: v83c = ADD v83a(0x20), v837
    0x83f: v83f(0x20) = SUB v83c, v837
    0x841: MSTORE v837, v83f(0x20)
    0x842: v842(0x3f) = CONST 
    0x845: MSTORE v83c, v842(0x3f)
    0x846: v846(0x20) = CONST 
    0x848: v848 = ADD v846(0x20), v83c
    0x84a: v84a(0x1a64) = CONST 
    0x84d: v84d(0x3f) = CONST 
    0x850: CODECOPY v848, v84a(0x1a64), v84d(0x3f)
    0x851: v851(0x40) = CONST 
    0x853: v853 = ADD v851(0x40), v848
    0x857: v857(0x40) = CONST 
    0x859: v859 = MLOAD v857(0x40)
    0x85c: v85c(0x84) = SUB v853, v859
    0x85e: REVERT v859, v85c(0x84)

    Begin block 0x85f
    prev=[0x81a], succ=[0xc11B0x85f]
    =================================
    0x860: v860(0x37) = CONST 
    0x863: v863 = SLOAD v860(0x37)
    0x864: v864(0x1) = CONST 
    0x866: v866(0x1) = CONST 
    0x868: v868(0xa0) = CONST 
    0x86a: v86a(0x10000000000000000000000000000000000000000) = SHL v868(0xa0), v866(0x1)
    0x86b: v86b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v86a(0x10000000000000000000000000000000000000000), v864(0x1)
    0x86e: v86e = AND v24b, v86b(0xffffffffffffffffffffffffffffffffffffffff)
    0x86f: v86f(0x1) = CONST 
    0x871: v871(0x1) = CONST 
    0x873: v873(0xa0) = CONST 
    0x875: v875(0x10000000000000000000000000000000000000000) = SHL v873(0xa0), v871(0x1)
    0x876: v876(0xffffffffffffffffffffffffffffffffffffffff) = SUB v875(0x10000000000000000000000000000000000000000), v86f(0x1)
    0x877: v877(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v876(0xffffffffffffffffffffffffffffffffffffffff)
    0x87a: v87a = AND v877(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v863
    0x87b: v87b = OR v87a, v86e
    0x87e: SSTORE v860(0x37), v87b
    0x87f: v87f(0x38) = CONST 
    0x882: v882 = SLOAD v87f(0x38)
    0x885: v885 = AND v86b(0xffffffffffffffffffffffffffffffffffffffff), v263
    0x888: v888 = AND v877(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v882
    0x889: v889 = OR v888, v885
    0x88b: SSTORE v87f(0x38), v889
    0x88c: v88c(0x39) = CONST 
    0x88f: v88f = SLOAD v88c(0x39)
    0x892: v892 = AND v26b, v86b(0xffffffffffffffffffffffffffffffffffffffff)
    0x896: v896 = AND v877(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v88f
    0x89a: v89a = OR v896, v892
    0x89c: SSTORE v88c(0x39), v89a
    0x89d: v89d(0x8a6) = CONST 
    0x8a2: v8a2(0xc11) = CONST 
    0x8a5: JUMP v8a2(0xc11), v25b, v253, v89d(0x8a6)

    Begin block 0xc11B0x85f
    prev=[0x85f], succ=[0xc220xc11B0x85f, 0xc2a0xc11B0x85f]
    =================================
    0xc12S0x85f: vc12V85f(0x0) = CONST 
    0xc14S0x85f: vc14V85f = SLOAD vc12V85f(0x0)
    0xc15S0x85f: vc15V85f(0x100) = CONST 
    0xc19S0x85f: vc19V85f = DIV vc14V85f, vc15V85f(0x100)
    0xc1aS0x85f: vc1aV85f(0xff) = CONST 
    0xc1cS0x85f: vc1cV85f = AND vc1aV85f(0xff), vc19V85f
    0xc1eS0x85f: vc1eV85f(0xc2a) = CONST 
    0xc21S0x85f: JUMPI vc1eV85f(0xc2a), vc1cV85f

    Begin block 0xc220xc11B0x85f
    prev=[0xc11B0x85f], succ=[0x18eeB0xc220xc11B0x85f]
    =================================
    0xc230xc11S0x85f: vc11c23V85f(0xc2a) = CONST 
    0xc260xc11S0x85f: vc11c26V85f(0x18ee) = CONST 
    0xc290xc11S0x85f: JUMP vc11c26V85f(0x18ee)

    Begin block 0x18eeB0xc220xc11B0x85f
    prev=[0xc220xc11B0x85f], succ=[0xc2a0xc11B0x85f]
    =================================
    0x18efS0xc220xc11S0x85f: v18efVc22c11V85f = ADDRESS 
    0x18f0S0xc220xc11S0x85f: v18f0Vc22c11V85f = EXTCODESIZE v18efVc22c11V85f
    0x18f1S0xc220xc11S0x85f: v18f1Vc22c11V85f = ISZERO v18f0Vc22c11V85f
    0x18f3S0xc220xc11S0x85f: JUMP vc11c23V85f(0xc2a)

    Begin block 0xc2a0xc11B0x85f
    prev=[0xc11B0x85f, 0x18eeB0xc220xc11B0x85f], succ=[0xc380xc11B0x85f, 0xc300xc11B0x85f]
    =================================
    0xc2a0xc11_0x0S0x85f: vc2ac11_0V85f = PHI vc1cV85f, v18f1Vc22c11V85f
    0xc2c0xc11S0x85f: vc11c2cV85f(0xc38) = CONST 
    0xc2f0xc11S0x85f: JUMPI vc11c2cV85f(0xc38), vc2ac11_0V85f

    Begin block 0xc380xc11B0x85f
    prev=[0xc2a0xc11B0x85f, 0xc300xc11B0x85f], succ=[0xc3d0xc11B0x85f, 0xc730xc11B0x85f]
    =================================
    0xc380xc11_0x0S0x85f: vc38c11_0V85f = PHI vc1cV85f, vc11c37V85f, v18f1Vc22c11V85f
    0xc390xc11S0x85f: vc11c39V85f(0xc73) = CONST 
    0xc3c0xc11S0x85f: JUMPI vc11c39V85f(0xc73), vc38c11_0V85f

    Begin block 0xc3d0xc11B0x85f
    prev=[0xc380xc11B0x85f], succ=[]
    =================================
    0xc3d0xc11S0x85f: vc11c3dV85f(0x40) = CONST 
    0xc3f0xc11S0x85f: vc11c3fV85f = MLOAD vc11c3dV85f(0x40)
    0xc400xc11S0x85f: vc11c40V85f(0x461bcd) = CONST 
    0xc440xc11S0x85f: vc11c44V85f(0xe5) = CONST 
    0xc460xc11S0x85f: vc11c46V85f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc11c44V85f(0xe5), vc11c40V85f(0x461bcd)
    0xc480xc11S0x85f: MSTORE vc11c3fV85f, vc11c46V85f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc490xc11S0x85f: vc11c49V85f(0x4) = CONST 
    0xc4b0xc11S0x85f: vc11c4bV85f = ADD vc11c49V85f(0x4), vc11c3fV85f
    0xc4e0xc11S0x85f: vc11c4eV85f(0x20) = CONST 
    0xc500xc11S0x85f: vc11c50V85f = ADD vc11c4eV85f(0x20), vc11c4bV85f
    0xc530xc11S0x85f: vc11c53V85f(0x20) = SUB vc11c50V85f, vc11c4bV85f
    0xc550xc11S0x85f: MSTORE vc11c4bV85f, vc11c53V85f(0x20)
    0xc560xc11S0x85f: vc11c56V85f(0x3d) = CONST 
    0xc590xc11S0x85f: MSTORE vc11c50V85f, vc11c56V85f(0x3d)
    0xc5a0xc11S0x85f: vc11c5aV85f(0x20) = CONST 
    0xc5c0xc11S0x85f: vc11c5cV85f = ADD vc11c5aV85f(0x20), vc11c50V85f
    0xc5e0xc11S0x85f: vc11c5eV85f(0x1cf3) = CONST 
    0xc610xc11S0x85f: vc11c61V85f(0x3d) = CONST 
    0xc640xc11S0x85f: CODECOPY vc11c5cV85f, vc11c5eV85f(0x1cf3), vc11c61V85f(0x3d)
    0xc650xc11S0x85f: vc11c65V85f(0x40) = CONST 
    0xc670xc11S0x85f: vc11c67V85f = ADD vc11c65V85f(0x40), vc11c5cV85f
    0xc6b0xc11S0x85f: vc11c6bV85f(0x40) = CONST 
    0xc6d0xc11S0x85f: vc11c6dV85f = MLOAD vc11c6bV85f(0x40)
    0xc700xc11S0x85f: vc11c70V85f(0x84) = SUB vc11c67V85f, vc11c6dV85f
    0xc720xc11S0x85f: REVERT vc11c6dV85f, vc11c70V85f(0x84)

    Begin block 0xc730xc11B0x85f
    prev=[0xc380xc11B0x85f], succ=[0xc860xc11B0x85f, 0xc9e0xc11B0x85f]
    =================================
    0xc740xc11S0x85f: vc11c74V85f(0x0) = CONST 
    0xc760xc11S0x85f: vc11c76V85f = SLOAD vc11c74V85f(0x0)
    0xc770xc11S0x85f: vc11c77V85f(0x100) = CONST 
    0xc7b0xc11S0x85f: vc11c7bV85f = DIV vc11c76V85f, vc11c77V85f(0x100)
    0xc7c0xc11S0x85f: vc11c7cV85f(0xff) = CONST 
    0xc7e0xc11S0x85f: vc11c7eV85f = AND vc11c7cV85f(0xff), vc11c7bV85f
    0xc7f0xc11S0x85f: vc11c7fV85f = ISZERO vc11c7eV85f
    0xc810xc11S0x85f: vc11c81V85f = ISZERO vc11c7fV85f
    0xc820xc11S0x85f: vc11c82V85f(0xc9e) = CONST 
    0xc850xc11S0x85f: JUMPI vc11c82V85f(0xc9e), vc11c81V85f

    Begin block 0xc860xc11B0x85f
    prev=[0xc730xc11B0x85f], succ=[0xc9e0xc11B0x85f]
    =================================
    0xc860xc11S0x85f: vc11c86V85f(0x0) = CONST 
    0xc890xc11S0x85f: vc11c89V85f = SLOAD vc11c86V85f(0x0)
    0xc8a0xc11S0x85f: vc11c8aV85f(0xff) = CONST 
    0xc8c0xc11S0x85f: vc11c8cV85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vc11c8aV85f(0xff)
    0xc8d0xc11S0x85f: vc11c8dV85f(0xff00) = CONST 
    0xc900xc11S0x85f: vc11c90V85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT vc11c8dV85f(0xff00)
    0xc930xc11S0x85f: vc11c93V85f = AND vc11c89V85f, vc11c90V85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0xc940xc11S0x85f: vc11c94V85f(0x100) = CONST 
    0xc970xc11S0x85f: vc11c97V85f = OR vc11c94V85f(0x100), vc11c93V85f
    0xc980xc11S0x85f: vc11c98V85f = AND vc11c97V85f, vc11c8cV85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0xc990xc11S0x85f: vc11c99V85f(0x1) = CONST 
    0xc9b0xc11S0x85f: vc11c9bV85f = OR vc11c99V85f(0x1), vc11c98V85f
    0xc9d0xc11S0x85f: SSTORE vc11c86V85f(0x0), vc11c9bV85f

    Begin block 0xc9e0xc11B0x85f
    prev=[0xc860xc11B0x85f, 0xc730xc11B0x85f], succ=[0xca70xc11B0x85f]
    =================================
    0xc9f0xc11S0x85f: vc11c9fV85f(0xca7) = CONST 
    0xca30xc11S0x85f: vc11ca3V85f(0x1791) = CONST 
    0xca60xc11S0x85f: CALLPRIVATE vc11ca3V85f(0x1791), v253, vc11c9fV85f(0xca7)

    Begin block 0xca70xc11B0x85f
    prev=[0xc9e0xc11B0x85f], succ=[0x18f4B0xca70xc11B0x85f]
    =================================
    0xca80xc11S0x85f: vc11ca8V85f(0xcb0) = CONST 
    0xcac0xc11S0x85f: vc11cacV85f(0x18f4) = CONST 
    0xcaf0xc11S0x85f: JUMP vc11cacV85f(0x18f4), v25b, vc11ca8V85f(0xcb0)

    Begin block 0x18f4B0xca70xc11B0x85f
    prev=[0xca70xc11B0x85f], succ=[0x1903B0xca70xc11B0x85f, 0x1939B0xca70xc11B0x85f]
    =================================
    0x18f5S0xca70xc11S0x85f: v18f5Vca7c11V85f(0x1) = CONST 
    0x18f7S0xca70xc11S0x85f: v18f7Vca7c11V85f(0x1) = CONST 
    0x18f9S0xca70xc11S0x85f: v18f9Vca7c11V85f(0xa0) = CONST 
    0x18fbS0xca70xc11S0x85f: v18fbVca7c11V85f(0x10000000000000000000000000000000000000000) = SHL v18f9Vca7c11V85f(0xa0), v18f7Vca7c11V85f(0x1)
    0x18fcS0xca70xc11S0x85f: v18fcVca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18fbVca7c11V85f(0x10000000000000000000000000000000000000000), v18f5Vca7c11V85f(0x1)
    0x18feS0xca70xc11S0x85f: v18feVca7c11V85f = AND v25b, v18fcVca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff)
    0x18ffS0xca70xc11S0x85f: v18ffVca7c11V85f(0x1939) = CONST 
    0x1902S0xca70xc11S0x85f: JUMPI v18ffVca7c11V85f(0x1939), v18feVca7c11V85f

    Begin block 0x1903B0xca70xc11B0x85f
    prev=[0x18f4B0xca70xc11B0x85f], succ=[]
    =================================
    0x1903S0xca70xc11S0x85f: v1903Vca7c11V85f(0x40) = CONST 
    0x1905S0xca70xc11S0x85f: v1905Vca7c11V85f = MLOAD v1903Vca7c11V85f(0x40)
    0x1906S0xca70xc11S0x85f: v1906Vca7c11V85f(0x461bcd) = CONST 
    0x190aS0xca70xc11S0x85f: v190aVca7c11V85f(0xe5) = CONST 
    0x190cS0xca70xc11S0x85f: v190cVca7c11V85f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v190aVca7c11V85f(0xe5), v1906Vca7c11V85f(0x461bcd)
    0x190eS0xca70xc11S0x85f: MSTORE v1905Vca7c11V85f, v190cVca7c11V85f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x190fS0xca70xc11S0x85f: v190fVca7c11V85f(0x4) = CONST 
    0x1911S0xca70xc11S0x85f: v1911Vca7c11V85f = ADD v190fVca7c11V85f(0x4), v1905Vca7c11V85f
    0x1914S0xca70xc11S0x85f: v1914Vca7c11V85f(0x20) = CONST 
    0x1916S0xca70xc11S0x85f: v1916Vca7c11V85f = ADD v1914Vca7c11V85f(0x20), v1911Vca7c11V85f
    0x1919S0xca70xc11S0x85f: v1919Vca7c11V85f(0x20) = SUB v1916Vca7c11V85f, v1911Vca7c11V85f
    0x191bS0xca70xc11S0x85f: MSTORE v1911Vca7c11V85f, v1919Vca7c11V85f(0x20)
    0x191cS0xca70xc11S0x85f: v191cVca7c11V85f(0x49) = CONST 
    0x191fS0xca70xc11S0x85f: MSTORE v1916Vca7c11V85f, v191cVca7c11V85f(0x49)
    0x1920S0xca70xc11S0x85f: v1920Vca7c11V85f(0x20) = CONST 
    0x1922S0xca70xc11S0x85f: v1922Vca7c11V85f = ADD v1920Vca7c11V85f(0x20), v1916Vca7c11V85f
    0x1924S0xca70xc11S0x85f: v1924Vca7c11V85f(0x1aa3) = CONST 
    0x1927S0xca70xc11S0x85f: v1927Vca7c11V85f(0x49) = CONST 
    0x192aS0xca70xc11S0x85f: CODECOPY v1922Vca7c11V85f, v1924Vca7c11V85f(0x1aa3), v1927Vca7c11V85f(0x49)
    0x192bS0xca70xc11S0x85f: v192bVca7c11V85f(0x60) = CONST 
    0x192dS0xca70xc11S0x85f: v192dVca7c11V85f = ADD v192bVca7c11V85f(0x60), v1922Vca7c11V85f
    0x1931S0xca70xc11S0x85f: v1931Vca7c11V85f(0x40) = CONST 
    0x1933S0xca70xc11S0x85f: v1933Vca7c11V85f = MLOAD v1931Vca7c11V85f(0x40)
    0x1936S0xca70xc11S0x85f: v1936Vca7c11V85f(0xa4) = SUB v192dVca7c11V85f, v1933Vca7c11V85f
    0x1938S0xca70xc11S0x85f: REVERT v1933Vca7c11V85f, v1936Vca7c11V85f(0xa4)

    Begin block 0x1939B0xca70xc11B0x85f
    prev=[0x18f4B0xca70xc11B0x85f], succ=[0xcb00xc11B0x85f]
    =================================
    0x193aS0xca70xc11S0x85f: v193aVca7c11V85f(0x35) = CONST 
    0x193dS0xca70xc11S0x85f: v193dVca7c11V85f = SLOAD v193aVca7c11V85f(0x35)
    0x193eS0xca70xc11S0x85f: v193eVca7c11V85f(0x1) = CONST 
    0x1940S0xca70xc11S0x85f: v1940Vca7c11V85f(0x1) = CONST 
    0x1942S0xca70xc11S0x85f: v1942Vca7c11V85f(0xa0) = CONST 
    0x1944S0xca70xc11S0x85f: v1944Vca7c11V85f(0x10000000000000000000000000000000000000000) = SHL v1942Vca7c11V85f(0xa0), v1940Vca7c11V85f(0x1)
    0x1945S0xca70xc11S0x85f: v1945Vca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1944Vca7c11V85f(0x10000000000000000000000000000000000000000), v193eVca7c11V85f(0x1)
    0x1946S0xca70xc11S0x85f: v1946Vca7c11V85f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1945Vca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1947S0xca70xc11S0x85f: v1947Vca7c11V85f = AND v1946Vca7c11V85f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v193dVca7c11V85f
    0x1948S0xca70xc11S0x85f: v1948Vca7c11V85f(0x1) = CONST 
    0x194aS0xca70xc11S0x85f: v194aVca7c11V85f(0x1) = CONST 
    0x194cS0xca70xc11S0x85f: v194cVca7c11V85f(0xa0) = CONST 
    0x194eS0xca70xc11S0x85f: v194eVca7c11V85f(0x10000000000000000000000000000000000000000) = SHL v194cVca7c11V85f(0xa0), v194aVca7c11V85f(0x1)
    0x194fS0xca70xc11S0x85f: v194fVca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v194eVca7c11V85f(0x10000000000000000000000000000000000000000), v1948Vca7c11V85f(0x1)
    0x1951S0xca70xc11S0x85f: v1951Vca7c11V85f = AND v25b, v194fVca7c11V85f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1954S0xca70xc11S0x85f: v1954Vca7c11V85f = OR v1951Vca7c11V85f, v1947Vca7c11V85f
    0x1957S0xca70xc11S0x85f: SSTORE v193aVca7c11V85f(0x35), v1954Vca7c11V85f
    0x1958S0xca70xc11S0x85f: v1958Vca7c11V85f(0x40) = CONST 
    0x195aS0xca70xc11S0x85f: v195aVca7c11V85f = MLOAD v1958Vca7c11V85f(0x40)
    0x195bS0xca70xc11S0x85f: v195bVca7c11V85f = CALLER 
    0x195dS0xca70xc11S0x85f: v195dVca7c11V85f(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c) = CONST 
    0x197fS0xca70xc11S0x85f: v197fVca7c11V85f(0x0) = CONST 
    0x1982S0xca70xc11S0x85f: LOG3 v195aVca7c11V85f, v197fVca7c11V85f(0x0), v195dVca7c11V85f(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c), v195bVca7c11V85f, v1951Vca7c11V85f
    0x1984S0xca70xc11S0x85f: JUMP vc11ca8V85f(0xcb0)

    Begin block 0xcb00xc11B0x85f
    prev=[0x1939B0xca70xc11B0x85f], succ=[0xcb70xc11B0x85f, 0xcc20xc11B0x85f]
    =================================
    0xcb20xc11S0x85f: vc11cb2V85f = ISZERO vc11c7fV85f
    0xcb30xc11S0x85f: vc11cb3V85f(0xcc2) = CONST 
    0xcb60xc11S0x85f: JUMPI vc11cb3V85f(0xcc2), vc11cb2V85f

    Begin block 0xcb70xc11B0x85f
    prev=[0xcb00xc11B0x85f], succ=[0xcc20xc11B0x85f]
    =================================
    0xcb70xc11S0x85f: vc11cb7V85f(0x0) = CONST 
    0xcba0xc11S0x85f: vc11cbaV85f = SLOAD vc11cb7V85f(0x0)
    0xcbb0xc11S0x85f: vc11cbbV85f(0xff00) = CONST 
    0xcbe0xc11S0x85f: vc11cbeV85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT vc11cbbV85f(0xff00)
    0xcbf0xc11S0x85f: vc11cbfV85f = AND vc11cbeV85f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), vc11cbaV85f
    0xcc10xc11S0x85f: SSTORE vc11cb7V85f(0x0), vc11cbfV85f

    Begin block 0xcc20xc11B0x85f
    prev=[0xcb70xc11B0x85f, 0xcb00xc11B0x85f], succ=[0x8a6]
    =================================
    0xcc60xc11S0x85f: JUMP v89d(0x8a6)

    Begin block 0x8a6
    prev=[0xcc20xc11B0x85f], succ=[0x8ad, 0x8b8]
    =================================
    0x8a8: v8a8 = ISZERO v771
    0x8a9: v8a9(0x8b8) = CONST 
    0x8ac: JUMPI v8a9(0x8b8), v8a8

    Begin block 0x8ad
    prev=[0x8a6], succ=[0x8b8]
    =================================
    0x8ad: v8ad(0x0) = CONST 
    0x8b0: v8b0 = SLOAD v8ad(0x0)
    0x8b1: v8b1(0xff00) = CONST 
    0x8b4: v8b4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v8b1(0xff00)
    0x8b5: v8b5 = AND v8b4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v8b0
    0x8b7: SSTORE v8ad(0x0), v8b5

    Begin block 0x8b8
    prev=[0x8ad, 0x8a6], succ=[0x1ef1]
    =================================
    0x8bf: JUMP v229(0x1ef1)

    Begin block 0x1ef1
    prev=[0x8b8], succ=[]
    =================================
    0x1ef2: STOP 

    Begin block 0xc300xc11B0x85f
    prev=[0xc2a0xc11B0x85f], succ=[0xc380xc11B0x85f]
    =================================
    0xc310xc11S0x85f: vc11c31V85f(0x0) = CONST 
    0xc330xc11S0x85f: vc11c33V85f = SLOAD vc11c31V85f(0x0)
    0xc340xc11S0x85f: vc11c34V85f(0xff) = CONST 
    0xc360xc11S0x85f: vc11c36V85f = AND vc11c34V85f(0xff), vc11c33V85f
    0xc370xc11S0x85f: vc11c37V85f = ISZERO vc11c36V85f

    Begin block 0x722
    prev=[0x71c], succ=[0x72a]
    =================================
    0x723: v723(0x0) = CONST 
    0x725: v725 = SLOAD v723(0x0)
    0x726: v726(0xff) = CONST 
    0x728: v728 = AND v726(0xff), v725
    0x729: v729 = ISZERO v728

    Begin block 0x714
    prev=[0x703], succ=[0x18eeB0x714]
    =================================
    0x715: v715(0x71c) = CONST 
    0x718: v718(0x18ee) = CONST 
    0x71b: JUMP v718(0x18ee)

    Begin block 0x18eeB0x714
    prev=[0x714], succ=[0x71c]
    =================================
    0x18efS0x714: v18efV714 = ADDRESS 
    0x18f0S0x714: v18f0V714 = EXTCODESIZE v18efV714
    0x18f1S0x714: v18f1V714 = ISZERO v18f0V714
    0x18f3S0x714: JUMP v715(0x71c)

}

function getToken(bytes32)() public {
    Begin block 0x270
    prev=[], succ=[0x282, 0x286]
    =================================
    0x271: v271(0x1f12) = CONST 
    0x274: v274(0x4) = CONST 
    0x277: v277 = CALLDATASIZE 
    0x278: v278 = SUB v277, v274(0x4)
    0x279: v279(0x20) = CONST 
    0x27c: v27c = LT v278, v279(0x20)
    0x27d: v27d = ISZERO v27c
    0x27e: v27e(0x286) = CONST 
    0x281: JUMPI v27e(0x286), v27d

    Begin block 0x282
    prev=[0x270], succ=[]
    =================================
    0x282: v282(0x0) = CONST 
    0x285: REVERT v282(0x0), v282(0x0)

    Begin block 0x286
    prev=[0x270], succ=[0x8c0]
    =================================
    0x288: v288 = CALLDATALOAD v274(0x4)
    0x289: v289(0x8c0) = CONST 
    0x28c: JUMP v289(0x8c0)

    Begin block 0x8c0
    prev=[0x286], succ=[0x1f12]
    =================================
    0x8c1: v8c1(0x0) = CONST 
    0x8c5: MSTORE v8c1(0x0), v288
    0x8c6: v8c6(0x3a) = CONST 
    0x8c8: v8c8(0x20) = CONST 
    0x8ca: MSTORE v8c8(0x20), v8c6(0x3a)
    0x8cb: v8cb(0x40) = CONST 
    0x8ce: v8ce = SHA3 v8c1(0x0), v8cb(0x40)
    0x8cf: v8cf(0x3) = CONST 
    0x8d1: v8d1 = ADD v8cf(0x3), v8ce
    0x8d2: v8d2 = SLOAD v8d1
    0x8d3: v8d3(0x1) = CONST 
    0x8d5: v8d5(0x1) = CONST 
    0x8d7: v8d7(0xa0) = CONST 
    0x8d9: v8d9(0x10000000000000000000000000000000000000000) = SHL v8d7(0xa0), v8d5(0x1)
    0x8da: v8da(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8d9(0x10000000000000000000000000000000000000000), v8d3(0x1)
    0x8db: v8db = AND v8da(0xffffffffffffffffffffffffffffffffffffffff), v8d2
    0x8dd: JUMP v271(0x1f12)

    Begin block 0x1f12
    prev=[0x8c0], succ=[]
    =================================
    0x1f13: v1f13(0x40) = CONST 
    0x1f16: v1f16 = MLOAD v1f13(0x40)
    0x1f17: v1f17(0x1) = CONST 
    0x1f19: v1f19(0x1) = CONST 
    0x1f1b: v1f1b(0xa0) = CONST 
    0x1f1d: v1f1d(0x10000000000000000000000000000000000000000) = SHL v1f1b(0xa0), v1f19(0x1)
    0x1f1e: v1f1e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f1d(0x10000000000000000000000000000000000000000), v1f17(0x1)
    0x1f21: v1f21 = AND v8db, v1f1e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f23: MSTORE v1f16, v1f21
    0x1f24: v1f24 = MLOAD v1f13(0x40)
    0x1f28: v1f28(0x0) = SUB v1f16, v1f24
    0x1f29: v1f29(0x20) = CONST 
    0x1f2b: v1f2b(0x20) = ADD v1f29(0x20), v1f28(0x0)
    0x1f2d: RETURN v1f24, v1f2b(0x20)

}

function setOperatorsContract(address)() public {
    Begin block 0x2a9
    prev=[], succ=[0x2bb, 0x2bf]
    =================================
    0x2aa: v2aa(0x1f4d) = CONST 
    0x2ad: v2ad(0x4) = CONST 
    0x2b0: v2b0 = CALLDATASIZE 
    0x2b1: v2b1 = SUB v2b0, v2ad(0x4)
    0x2b2: v2b2(0x20) = CONST 
    0x2b5: v2b5 = LT v2b1, v2b2(0x20)
    0x2b6: v2b6 = ISZERO v2b5
    0x2b7: v2b7(0x2bf) = CONST 
    0x2ba: JUMPI v2b7(0x2bf), v2b6

    Begin block 0x2bb
    prev=[0x2a9], succ=[]
    =================================
    0x2bb: v2bb(0x0) = CONST 
    0x2be: REVERT v2bb(0x0), v2bb(0x0)

    Begin block 0x2bf
    prev=[0x2a9], succ=[0x8de]
    =================================
    0x2c1: v2c1 = CALLDATALOAD v2ad(0x4)
    0x2c2: v2c2(0x1) = CONST 
    0x2c4: v2c4(0x1) = CONST 
    0x2c6: v2c6(0xa0) = CONST 
    0x2c8: v2c8(0x10000000000000000000000000000000000000000) = SHL v2c6(0xa0), v2c4(0x1)
    0x2c9: v2c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c8(0x10000000000000000000000000000000000000000), v2c2(0x1)
    0x2ca: v2ca = AND v2c9(0xffffffffffffffffffffffffffffffffffffffff), v2c1
    0x2cb: v2cb(0x8de) = CONST 
    0x2ce: JUMP v2cb(0x8de)

    Begin block 0x8de
    prev=[0x2bf], succ=[0x8e7]
    =================================
    0x8df: v8df(0x8e7) = CONST 
    0x8e2: v8e2 = CALLER 
    0x8e3: v8e3(0x9ef) = CONST 
    0x8e6: v8e6_0 = CALLPRIVATE v8e3(0x9ef), v8e2, v8df(0x8e7)

    Begin block 0x8e7
    prev=[0x8de], succ=[0x8ec, 0x922]
    =================================
    0x8e8: v8e8(0x922) = CONST 
    0x8eb: JUMPI v8e8(0x922), v8e6_0

    Begin block 0x8ec
    prev=[0x8e7], succ=[]
    =================================
    0x8ec: v8ec(0x40) = CONST 
    0x8ee: v8ee = MLOAD v8ec(0x40)
    0x8ef: v8ef(0x461bcd) = CONST 
    0x8f3: v8f3(0xe5) = CONST 
    0x8f5: v8f5(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v8f3(0xe5), v8ef(0x461bcd)
    0x8f7: MSTORE v8ee, v8f5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8f8: v8f8(0x4) = CONST 
    0x8fa: v8fa = ADD v8f8(0x4), v8ee
    0x8fd: v8fd(0x20) = CONST 
    0x8ff: v8ff = ADD v8fd(0x20), v8fa
    0x902: v902(0x20) = SUB v8ff, v8fa
    0x904: MSTORE v8fa, v902(0x20)
    0x905: v905(0x31) = CONST 
    0x908: MSTORE v8ff, v905(0x31)
    0x909: v909(0x20) = CONST 
    0x90b: v90b = ADD v909(0x20), v8ff
    0x90d: v90d(0x1b65) = CONST 
    0x910: v910(0x31) = CONST 
    0x913: CODECOPY v90b, v90d(0x1b65), v910(0x31)
    0x914: v914(0x40) = CONST 
    0x916: v916 = ADD v914(0x40), v90b
    0x91a: v91a(0x40) = CONST 
    0x91c: v91c = MLOAD v91a(0x40)
    0x91f: v91f(0x84) = SUB v916, v91c
    0x921: REVERT v91c, v91f(0x84)

    Begin block 0x922
    prev=[0x8e7], succ=[0x931, 0x967]
    =================================
    0x923: v923(0x1) = CONST 
    0x925: v925(0x1) = CONST 
    0x927: v927(0xa0) = CONST 
    0x929: v929(0x10000000000000000000000000000000000000000) = SHL v927(0xa0), v925(0x1)
    0x92a: v92a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v929(0x10000000000000000000000000000000000000000), v923(0x1)
    0x92c: v92c = AND v2ca, v92a(0xffffffffffffffffffffffffffffffffffffffff)
    0x92d: v92d(0x967) = CONST 
    0x930: JUMPI v92d(0x967), v92c

    Begin block 0x931
    prev=[0x922], succ=[]
    =================================
    0x931: v931(0x40) = CONST 
    0x933: v933 = MLOAD v931(0x40)
    0x934: v934(0x461bcd) = CONST 
    0x938: v938(0xe5) = CONST 
    0x93a: v93a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v938(0xe5), v934(0x461bcd)
    0x93c: MSTORE v933, v93a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x93d: v93d(0x4) = CONST 
    0x93f: v93f = ADD v93d(0x4), v933
    0x942: v942(0x20) = CONST 
    0x944: v944 = ADD v942(0x20), v93f
    0x947: v947(0x20) = SUB v944, v93f
    0x949: MSTORE v93f, v947(0x20)
    0x94a: v94a(0x3f) = CONST 
    0x94d: MSTORE v944, v94a(0x3f)
    0x94e: v94e(0x20) = CONST 
    0x950: v950 = ADD v94e(0x20), v944
    0x952: v952(0x1cb4) = CONST 
    0x955: v955(0x3f) = CONST 
    0x958: CODECOPY v950, v952(0x1cb4), v955(0x3f)
    0x959: v959(0x40) = CONST 
    0x95b: v95b = ADD v959(0x40), v950
    0x95f: v95f(0x40) = CONST 
    0x961: v961 = MLOAD v95f(0x40)
    0x964: v964(0x84) = SUB v95b, v961
    0x966: REVERT v961, v964(0x84)

    Begin block 0x967
    prev=[0x922], succ=[0x1f4d]
    =================================
    0x968: v968(0x34) = CONST 
    0x96b: v96b = SLOAD v968(0x34)
    0x96c: v96c(0x1) = CONST 
    0x96e: v96e(0x1) = CONST 
    0x970: v970(0xa0) = CONST 
    0x972: v972(0x10000000000000000000000000000000000000000) = SHL v970(0xa0), v96e(0x1)
    0x973: v973(0xffffffffffffffffffffffffffffffffffffffff) = SUB v972(0x10000000000000000000000000000000000000000), v96c(0x1)
    0x974: v974(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v973(0xffffffffffffffffffffffffffffffffffffffff)
    0x975: v975 = AND v974(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v96b
    0x976: v976(0x1) = CONST 
    0x978: v978(0x1) = CONST 
    0x97a: v97a(0xa0) = CONST 
    0x97c: v97c(0x10000000000000000000000000000000000000000) = SHL v97a(0xa0), v978(0x1)
    0x97d: v97d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v97c(0x10000000000000000000000000000000000000000), v976(0x1)
    0x97f: v97f = AND v2ca, v97d(0xffffffffffffffffffffffffffffffffffffffff)
    0x982: v982 = OR v97f, v975
    0x985: SSTORE v968(0x34), v982
    0x986: v986(0x40) = CONST 
    0x988: v988 = MLOAD v986(0x40)
    0x989: v989 = CALLER 
    0x98b: v98b(0x1e6311290e7fb795a47761d6ca6a39b9c898bbf2e8b0e40211aa9f2f6c02029) = CONST 
    0x9ad: v9ad(0x0) = CONST 
    0x9b0: LOG3 v988, v9ad(0x0), v98b(0x1e6311290e7fb795a47761d6ca6a39b9c898bbf2e8b0e40211aa9f2f6c02029), v989, v97f
    0x9b2: JUMP v2aa(0x1f4d)

    Begin block 0x1f4d
    prev=[0x967], succ=[]
    =================================
    0x1f4e: STOP 

}

function dchf()() public {
    Begin block 0x2cf
    prev=[], succ=[0x9b3]
    =================================
    0x2d0: v2d0(0x1f6e) = CONST 
    0x2d3: v2d3(0x9b3) = CONST 
    0x2d6: JUMP v2d3(0x9b3)

    Begin block 0x9b3
    prev=[0x2cf], succ=[0x1f6e]
    =================================
    0x9b4: v9b4(0x37) = CONST 
    0x9b6: v9b6 = SLOAD v9b4(0x37)
    0x9b7: v9b7(0x1) = CONST 
    0x9b9: v9b9(0x1) = CONST 
    0x9bb: v9bb(0xa0) = CONST 
    0x9bd: v9bd(0x10000000000000000000000000000000000000000) = SHL v9bb(0xa0), v9b9(0x1)
    0x9be: v9be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9bd(0x10000000000000000000000000000000000000000), v9b7(0x1)
    0x9bf: v9bf = AND v9be(0xffffffffffffffffffffffffffffffffffffffff), v9b6
    0x9c1: JUMP v2d0(0x1f6e)

    Begin block 0x1f6e
    prev=[0x9b3], succ=[]
    =================================
    0x1f6f: v1f6f(0x40) = CONST 
    0x1f72: v1f72 = MLOAD v1f6f(0x40)
    0x1f73: v1f73(0x1) = CONST 
    0x1f75: v1f75(0x1) = CONST 
    0x1f77: v1f77(0xa0) = CONST 
    0x1f79: v1f79(0x10000000000000000000000000000000000000000) = SHL v1f77(0xa0), v1f75(0x1)
    0x1f7a: v1f7a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f79(0x10000000000000000000000000000000000000000), v1f73(0x1)
    0x1f7d: v1f7d = AND v9bf, v1f7a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f7f: MSTORE v1f72, v1f7d
    0x1f80: v1f80 = MLOAD v1f6f(0x40)
    0x1f84: v1f84(0x0) = SUB v1f72, v1f80
    0x1f85: v1f85(0x20) = CONST 
    0x1f87: v1f87(0x20) = ADD v1f85(0x20), v1f84(0x0)
    0x1f89: RETURN v1f80, v1f87(0x20)

}

function getOperatorsPending()() public {
    Begin block 0x2d7
    prev=[], succ=[0x9c2]
    =================================
    0x2d8: v2d8(0x1fa9) = CONST 
    0x2db: v2db(0x9c2) = CONST 
    0x2de: JUMP v2db(0x9c2)

    Begin block 0x9c2
    prev=[0x2d7], succ=[0x1fa9]
    =================================
    0x9c3: v9c3(0x34) = CONST 
    0x9c5: v9c5 = SLOAD v9c3(0x34)
    0x9c6: v9c6(0x1) = CONST 
    0x9c8: v9c8(0x1) = CONST 
    0x9ca: v9ca(0xa0) = CONST 
    0x9cc: v9cc(0x10000000000000000000000000000000000000000) = SHL v9ca(0xa0), v9c8(0x1)
    0x9cd: v9cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9cc(0x10000000000000000000000000000000000000000), v9c6(0x1)
    0x9ce: v9ce = AND v9cd(0xffffffffffffffffffffffffffffffffffffffff), v9c5
    0x9d0: JUMP v2d8(0x1fa9)

    Begin block 0x1fa9
    prev=[0x9c2], succ=[]
    =================================
    0x1faa: v1faa(0x40) = CONST 
    0x1fad: v1fad = MLOAD v1faa(0x40)
    0x1fae: v1fae(0x1) = CONST 
    0x1fb0: v1fb0(0x1) = CONST 
    0x1fb2: v1fb2(0xa0) = CONST 
    0x1fb4: v1fb4(0x10000000000000000000000000000000000000000) = SHL v1fb2(0xa0), v1fb0(0x1)
    0x1fb5: v1fb5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fb4(0x10000000000000000000000000000000000000000), v1fae(0x1)
    0x1fb8: v1fb8 = AND v9ce, v1fb5(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fba: MSTORE v1fad, v1fb8
    0x1fbb: v1fbb = MLOAD v1faa(0x40)
    0x1fbf: v1fbf(0x0) = SUB v1fad, v1fbb
    0x1fc0: v1fc0(0x20) = CONST 
    0x1fc2: v1fc2(0x20) = ADD v1fc0(0x20), v1fbf(0x0)
    0x1fc4: RETURN v1fbb, v1fc2(0x20)

}

function getIssuer(bytes32)() public {
    Begin block 0x2df
    prev=[], succ=[0x2f1, 0x2f5]
    =================================
    0x2e0: v2e0(0x1fe4) = CONST 
    0x2e3: v2e3(0x4) = CONST 
    0x2e6: v2e6 = CALLDATASIZE 
    0x2e7: v2e7 = SUB v2e6, v2e3(0x4)
    0x2e8: v2e8(0x20) = CONST 
    0x2eb: v2eb = LT v2e7, v2e8(0x20)
    0x2ec: v2ec = ISZERO v2eb
    0x2ed: v2ed(0x2f5) = CONST 
    0x2f0: JUMPI v2ed(0x2f5), v2ec

    Begin block 0x2f1
    prev=[0x2df], succ=[]
    =================================
    0x2f1: v2f1(0x0) = CONST 
    0x2f4: REVERT v2f1(0x0), v2f1(0x0)

    Begin block 0x2f5
    prev=[0x2df], succ=[0x9d1]
    =================================
    0x2f7: v2f7 = CALLDATALOAD v2e3(0x4)
    0x2f8: v2f8(0x9d1) = CONST 
    0x2fb: JUMP v2f8(0x9d1)

    Begin block 0x9d1
    prev=[0x2f5], succ=[0x1fe4]
    =================================
    0x9d2: v9d2(0x0) = CONST 
    0x9d6: MSTORE v9d2(0x0), v2f7
    0x9d7: v9d7(0x3a) = CONST 
    0x9d9: v9d9(0x20) = CONST 
    0x9db: MSTORE v9d9(0x20), v9d7(0x3a)
    0x9dc: v9dc(0x40) = CONST 
    0x9df: v9df = SHA3 v9d2(0x0), v9dc(0x40)
    0x9e0: v9e0(0x2) = CONST 
    0x9e2: v9e2 = ADD v9e0(0x2), v9df
    0x9e3: v9e3 = SLOAD v9e2
    0x9e4: v9e4(0x1) = CONST 
    0x9e6: v9e6(0x1) = CONST 
    0x9e8: v9e8(0xa0) = CONST 
    0x9ea: v9ea(0x10000000000000000000000000000000000000000) = SHL v9e8(0xa0), v9e6(0x1)
    0x9eb: v9eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9ea(0x10000000000000000000000000000000000000000), v9e4(0x1)
    0x9ec: v9ec = AND v9eb(0xffffffffffffffffffffffffffffffffffffffff), v9e3
    0x9ee: JUMP v2e0(0x1fe4)

    Begin block 0x1fe4
    prev=[0x9d1], succ=[]
    =================================
    0x1fe5: v1fe5(0x40) = CONST 
    0x1fe8: v1fe8 = MLOAD v1fe5(0x40)
    0x1fe9: v1fe9(0x1) = CONST 
    0x1feb: v1feb(0x1) = CONST 
    0x1fed: v1fed(0xa0) = CONST 
    0x1fef: v1fef(0x10000000000000000000000000000000000000000) = SHL v1fed(0xa0), v1feb(0x1)
    0x1ff0: v1ff0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fef(0x10000000000000000000000000000000000000000), v1fe9(0x1)
    0x1ff3: v1ff3 = AND v9ec, v1ff0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ff5: MSTORE v1fe8, v1ff3
    0x1ff6: v1ff6 = MLOAD v1fe5(0x40)
    0x1ffa: v1ffa(0x0) = SUB v1fe8, v1ff6
    0x1ffb: v1ffb(0x20) = CONST 
    0x1ffd: v1ffd(0x20) = ADD v1ffb(0x20), v1ffa(0x0)
    0x1fff: RETURN v1ff6, v1ffd(0x20)

}

function isAdmin(address)() public {
    Begin block 0x2fc
    prev=[], succ=[0x30e, 0x312]
    =================================
    0x2fd: v2fd(0x201f) = CONST 
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
    prev=[0x2fc], succ=[0x9ef0x2fc]
    =================================
    0x314: v314 = CALLDATALOAD v300(0x4)
    0x315: v315(0x1) = CONST 
    0x317: v317(0x1) = CONST 
    0x319: v319(0xa0) = CONST 
    0x31b: v31b(0x10000000000000000000000000000000000000000) = SHL v319(0xa0), v317(0x1)
    0x31c: v31c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v31b(0x10000000000000000000000000000000000000000), v315(0x1)
    0x31d: v31d = AND v31c(0xffffffffffffffffffffffffffffffffffffffff), v314
    0x31e: v31e(0x9ef) = CONST 
    0x321: JUMP v31e(0x9ef)

    Begin block 0x9ef0x2fc
    prev=[0x312], succ=[0xa3c0x2fc, 0xa400x2fc]
    =================================
    0x9f00x2fc: v2fc9f0(0x33) = CONST 
    0x9f20x2fc: v2fc9f2 = SLOAD v2fc9f0(0x33)
    0x9f30x2fc: v2fc9f3(0x40) = CONST 
    0x9f60x2fc: v2fc9f6 = MLOAD v2fc9f3(0x40)
    0x9f70x2fc: v2fc9f7(0x935e01b) = CONST 
    0x9fc0x2fc: v2fc9fc(0xe2) = CONST 
    0x9fe0x2fc: v2fc9fe(0x24d7806c00000000000000000000000000000000000000000000000000000000) = SHL v2fc9fc(0xe2), v2fc9f7(0x935e01b)
    0xa000x2fc: MSTORE v2fc9f6, v2fc9fe(0x24d7806c00000000000000000000000000000000000000000000000000000000)
    0xa010x2fc: v2fca01(0x1) = CONST 
    0xa030x2fc: v2fca03(0x1) = CONST 
    0xa050x2fc: v2fca05(0xa0) = CONST 
    0xa070x2fc: v2fca07(0x10000000000000000000000000000000000000000) = SHL v2fca05(0xa0), v2fca03(0x1)
    0xa080x2fc: v2fca08(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2fca07(0x10000000000000000000000000000000000000000), v2fca01(0x1)
    0xa0b0x2fc: v2fca0b = AND v2fca08(0xffffffffffffffffffffffffffffffffffffffff), v31d
    0xa0c0x2fc: v2fca0c(0x4) = CONST 
    0xa0f0x2fc: v2fca0f = ADD v2fc9f6, v2fca0c(0x4)
    0xa100x2fc: MSTORE v2fca0f, v2fca0b
    0xa120x2fc: v2fca12 = MLOAD v2fc9f3(0x40)
    0xa130x2fc: v2fca13(0x0) = CONST 
    0xa190x2fc: v2fca19 = AND v2fc9f2, v2fca08(0xffffffffffffffffffffffffffffffffffffffff)
    0xa1b0x2fc: v2fca1b(0x24d7806c) = CONST 
    0xa210x2fc: v2fca21(0x24) = CONST 
    0xa250x2fc: v2fca25 = ADD v2fc9f6, v2fca21(0x24)
    0xa270x2fc: v2fca27(0x20) = CONST 
    0xa2f0x2fc: v2fca2f(0x0) = SUB v2fc9f6, v2fca12
    0xa300x2fc: v2fca30(0x24) = ADD v2fca2f(0x0), v2fca21(0x24)
    0xa340x2fc: v2fca34 = EXTCODESIZE v2fca19
    0xa350x2fc: v2fca35 = ISZERO v2fca34
    0xa370x2fc: v2fca37 = ISZERO v2fca35
    0xa380x2fc: v2fca38(0xa40) = CONST 
    0xa3b0x2fc: JUMPI v2fca38(0xa40), v2fca37

    Begin block 0xa3c0x2fc
    prev=[0x9ef0x2fc], succ=[]
    =================================
    0xa3c0x2fc: v2fca3c(0x0) = CONST 
    0xa3f0x2fc: REVERT v2fca3c(0x0), v2fca3c(0x0)

    Begin block 0xa400x2fc
    prev=[0x9ef0x2fc], succ=[0xa4b0x2fc, 0xa540x2fc]
    =================================
    0xa420x2fc: v2fca42 = GAS 
    0xa430x2fc: v2fca43 = STATICCALL v2fca42, v2fca19, v2fca12, v2fca30(0x24), v2fca12, v2fca27(0x20)
    0xa440x2fc: v2fca44 = ISZERO v2fca43
    0xa460x2fc: v2fca46 = ISZERO v2fca44
    0xa470x2fc: v2fca47(0xa54) = CONST 
    0xa4a0x2fc: JUMPI v2fca47(0xa54), v2fca46

    Begin block 0xa4b0x2fc
    prev=[0xa400x2fc], succ=[]
    =================================
    0xa4b0x2fc: v2fca4b = RETURNDATASIZE 
    0xa4c0x2fc: v2fca4c(0x0) = CONST 
    0xa4f0x2fc: RETURNDATACOPY v2fca4c(0x0), v2fca4c(0x0), v2fca4b
    0xa500x2fc: v2fca50 = RETURNDATASIZE 
    0xa510x2fc: v2fca51(0x0) = CONST 
    0xa530x2fc: REVERT v2fca51(0x0), v2fca50

    Begin block 0xa540x2fc
    prev=[0xa400x2fc], succ=[0xa660x2fc, 0xa6a0x2fc]
    =================================
    0xa590x2fc: v2fca59(0x40) = CONST 
    0xa5b0x2fc: v2fca5b = MLOAD v2fca59(0x40)
    0xa5c0x2fc: v2fca5c = RETURNDATASIZE 
    0xa5d0x2fc: v2fca5d(0x20) = CONST 
    0xa600x2fc: v2fca60 = LT v2fca5c, v2fca5d(0x20)
    0xa610x2fc: v2fca61 = ISZERO v2fca60
    0xa620x2fc: v2fca62(0xa6a) = CONST 
    0xa650x2fc: JUMPI v2fca62(0xa6a), v2fca61

    Begin block 0xa660x2fc
    prev=[0xa540x2fc], succ=[]
    =================================
    0xa660x2fc: v2fca66(0x0) = CONST 
    0xa690x2fc: REVERT v2fca66(0x0), v2fca66(0x0)

    Begin block 0xa6a0x2fc
    prev=[0xa540x2fc], succ=[0x201f]
    =================================
    0xa6c0x2fc: v2fca6c = MLOAD v2fca5b
    0xa710x2fc: JUMP v2fd(0x201f)

    Begin block 0x201f
    prev=[0xa6a0x2fc], succ=[]
    =================================
    0x2020: v2020(0x40) = CONST 
    0x2023: v2023 = MLOAD v2020(0x40)
    0x2025: v2025 = ISZERO v2fca6c
    0x2026: v2026 = ISZERO v2025
    0x2028: MSTORE v2023, v2026
    0x2029: v2029 = MLOAD v2020(0x40)
    0x202d: v202d(0x0) = SUB v2023, v2029
    0x202e: v202e(0x20) = CONST 
    0x2030: v2030(0x20) = ADD v202e(0x20), v202d(0x0)
    0x2032: RETURN v2029, v2030(0x20)

}

function isRelay(address)() public {
    Begin block 0x336
    prev=[], succ=[0x348, 0x34c]
    =================================
    0x337: v337(0x2052) = CONST 
    0x33a: v33a(0x4) = CONST 
    0x33d: v33d = CALLDATASIZE 
    0x33e: v33e = SUB v33d, v33a(0x4)
    0x33f: v33f(0x20) = CONST 
    0x342: v342 = LT v33e, v33f(0x20)
    0x343: v343 = ISZERO v342
    0x344: v344(0x34c) = CONST 
    0x347: JUMPI v344(0x34c), v343

    Begin block 0x348
    prev=[0x336], succ=[]
    =================================
    0x348: v348(0x0) = CONST 
    0x34b: REVERT v348(0x0), v348(0x0)

    Begin block 0x34c
    prev=[0x336], succ=[0xa72]
    =================================
    0x34e: v34e = CALLDATALOAD v33a(0x4)
    0x34f: v34f(0x1) = CONST 
    0x351: v351(0x1) = CONST 
    0x353: v353(0xa0) = CONST 
    0x355: v355(0x10000000000000000000000000000000000000000) = SHL v353(0xa0), v351(0x1)
    0x356: v356(0xffffffffffffffffffffffffffffffffffffffff) = SUB v355(0x10000000000000000000000000000000000000000), v34f(0x1)
    0x357: v357 = AND v356(0xffffffffffffffffffffffffffffffffffffffff), v34e
    0x358: v358(0xa72) = CONST 
    0x35b: JUMP v358(0xa72)

    Begin block 0xa72
    prev=[0x34c], succ=[0xabf, 0xa400x336]
    =================================
    0xa73: va73(0x33) = CONST 
    0xa75: va75 = SLOAD va73(0x33)
    0xa76: va76(0x40) = CONST 
    0xa79: va79 = MLOAD va76(0x40)
    0xa7a: va7a(0x26cb32b7) = CONST 
    0xa7f: va7f(0xe0) = CONST 
    0xa81: va81(0x26cb32b700000000000000000000000000000000000000000000000000000000) = SHL va7f(0xe0), va7a(0x26cb32b7)
    0xa83: MSTORE va79, va81(0x26cb32b700000000000000000000000000000000000000000000000000000000)
    0xa84: va84(0x1) = CONST 
    0xa86: va86(0x1) = CONST 
    0xa88: va88(0xa0) = CONST 
    0xa8a: va8a(0x10000000000000000000000000000000000000000) = SHL va88(0xa0), va86(0x1)
    0xa8b: va8b(0xffffffffffffffffffffffffffffffffffffffff) = SUB va8a(0x10000000000000000000000000000000000000000), va84(0x1)
    0xa8e: va8e = AND va8b(0xffffffffffffffffffffffffffffffffffffffff), v357
    0xa8f: va8f(0x4) = CONST 
    0xa92: va92 = ADD va79, va8f(0x4)
    0xa93: MSTORE va92, va8e
    0xa95: va95 = MLOAD va76(0x40)
    0xa96: va96(0x0) = CONST 
    0xa9c: va9c = AND va75, va8b(0xffffffffffffffffffffffffffffffffffffffff)
    0xa9e: va9e(0x26cb32b7) = CONST 
    0xaa4: vaa4(0x24) = CONST 
    0xaa8: vaa8 = ADD va79, vaa4(0x24)
    0xaaa: vaaa(0x20) = CONST 
    0xab2: vab2(0x0) = SUB va79, va95
    0xab3: vab3(0x24) = ADD vab2(0x0), vaa4(0x24)
    0xab7: vab7 = EXTCODESIZE va9c
    0xab8: vab8 = ISZERO vab7
    0xaba: vaba = ISZERO vab8
    0xabb: vabb(0xa40) = CONST 
    0xabe: JUMPI vabb(0xa40), vaba

    Begin block 0xabf
    prev=[0xa72], succ=[]
    =================================
    0xabf: vabf(0x0) = CONST 
    0xac2: REVERT vabf(0x0), vabf(0x0)

    Begin block 0xa400x336
    prev=[0xa72], succ=[0xa4b0x336, 0xa540x336]
    =================================
    0xa420x336: v336a42 = GAS 
    0xa430x336: v336a43 = STATICCALL v336a42, va9c, va95, vab3(0x24), va95, vaaa(0x20)
    0xa440x336: v336a44 = ISZERO v336a43
    0xa460x336: v336a46 = ISZERO v336a44
    0xa470x336: v336a47(0xa54) = CONST 
    0xa4a0x336: JUMPI v336a47(0xa54), v336a46

    Begin block 0xa4b0x336
    prev=[0xa400x336], succ=[]
    =================================
    0xa4b0x336: v336a4b = RETURNDATASIZE 
    0xa4c0x336: v336a4c(0x0) = CONST 
    0xa4f0x336: RETURNDATACOPY v336a4c(0x0), v336a4c(0x0), v336a4b
    0xa500x336: v336a50 = RETURNDATASIZE 
    0xa510x336: v336a51(0x0) = CONST 
    0xa530x336: REVERT v336a51(0x0), v336a50

    Begin block 0xa540x336
    prev=[0xa400x336], succ=[0xa660x336, 0xa6a0x336]
    =================================
    0xa590x336: v336a59(0x40) = CONST 
    0xa5b0x336: v336a5b = MLOAD v336a59(0x40)
    0xa5c0x336: v336a5c = RETURNDATASIZE 
    0xa5d0x336: v336a5d(0x20) = CONST 
    0xa600x336: v336a60 = LT v336a5c, v336a5d(0x20)
    0xa610x336: v336a61 = ISZERO v336a60
    0xa620x336: v336a62(0xa6a) = CONST 
    0xa650x336: JUMPI v336a62(0xa6a), v336a61

    Begin block 0xa660x336
    prev=[0xa540x336], succ=[]
    =================================
    0xa660x336: v336a66(0x0) = CONST 
    0xa690x336: REVERT v336a66(0x0), v336a66(0x0)

    Begin block 0xa6a0x336
    prev=[0xa540x336], succ=[0x2052]
    =================================
    0xa6c0x336: v336a6c = MLOAD v336a5b
    0xa710x336: JUMP v337(0x2052)

    Begin block 0x2052
    prev=[0xa6a0x336], succ=[]
    =================================
    0x2053: v2053(0x40) = CONST 
    0x2056: v2056 = MLOAD v2053(0x40)
    0x2058: v2058 = ISZERO v336a6c
    0x2059: v2059 = ISZERO v2058
    0x205b: MSTORE v2056, v2059
    0x205c: v205c = MLOAD v2053(0x40)
    0x2060: v2060(0x0) = SUB v2056, v205c
    0x2061: v2061(0x20) = CONST 
    0x2063: v2063(0x20) = ADD v2061(0x20), v2060(0x0)
    0x2065: RETURN v205c, v2063(0x20)

}

function isOperatorOrSystem(address)() public {
    Begin block 0x35c
    prev=[], succ=[0x36e, 0x372]
    =================================
    0x35d: v35d(0x2085) = CONST 
    0x360: v360(0x4) = CONST 
    0x363: v363 = CALLDATASIZE 
    0x364: v364 = SUB v363, v360(0x4)
    0x365: v365(0x20) = CONST 
    0x368: v368 = LT v364, v365(0x20)
    0x369: v369 = ISZERO v368
    0x36a: v36a(0x372) = CONST 
    0x36d: JUMPI v36a(0x372), v369

    Begin block 0x36e
    prev=[0x35c], succ=[]
    =================================
    0x36e: v36e(0x0) = CONST 
    0x371: REVERT v36e(0x0), v36e(0x0)

    Begin block 0x372
    prev=[0x35c], succ=[0xac3]
    =================================
    0x374: v374 = CALLDATALOAD v360(0x4)
    0x375: v375(0x1) = CONST 
    0x377: v377(0x1) = CONST 
    0x379: v379(0xa0) = CONST 
    0x37b: v37b(0x10000000000000000000000000000000000000000) = SHL v379(0xa0), v377(0x1)
    0x37c: v37c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37b(0x10000000000000000000000000000000000000000), v375(0x1)
    0x37d: v37d = AND v37c(0xffffffffffffffffffffffffffffffffffffffff), v374
    0x37e: v37e(0xac3) = CONST 
    0x381: JUMP v37e(0xac3)

    Begin block 0xac3
    prev=[0x372], succ=[0xb10, 0xb140x35c]
    =================================
    0xac4: vac4(0x33) = CONST 
    0xac6: vac6 = SLOAD vac4(0x33)
    0xac7: vac7(0x40) = CONST 
    0xaca: vaca = MLOAD vac7(0x40)
    0xacb: vacb(0x36b87bd7) = CONST 
    0xad0: vad0(0xe1) = CONST 
    0xad2: vad2(0x6d70f7ae00000000000000000000000000000000000000000000000000000000) = SHL vad0(0xe1), vacb(0x36b87bd7)
    0xad4: MSTORE vaca, vad2(0x6d70f7ae00000000000000000000000000000000000000000000000000000000)
    0xad5: vad5(0x1) = CONST 
    0xad7: vad7(0x1) = CONST 
    0xad9: vad9(0xa0) = CONST 
    0xadb: vadb(0x10000000000000000000000000000000000000000) = SHL vad9(0xa0), vad7(0x1)
    0xadc: vadc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vadb(0x10000000000000000000000000000000000000000), vad5(0x1)
    0xadf: vadf = AND vadc(0xffffffffffffffffffffffffffffffffffffffff), v37d
    0xae0: vae0(0x4) = CONST 
    0xae3: vae3 = ADD vaca, vae0(0x4)
    0xae4: MSTORE vae3, vadf
    0xae6: vae6 = MLOAD vac7(0x40)
    0xae7: vae7(0x0) = CONST 
    0xaed: vaed = AND vac6, vadc(0xffffffffffffffffffffffffffffffffffffffff)
    0xaef: vaef(0x6d70f7ae) = CONST 
    0xaf5: vaf5(0x24) = CONST 
    0xaf9: vaf9 = ADD vaca, vaf5(0x24)
    0xafb: vafb(0x20) = CONST 
    0xb03: vb03(0x0) = SUB vaca, vae6
    0xb04: vb04(0x24) = ADD vb03(0x0), vaf5(0x24)
    0xb08: vb08 = EXTCODESIZE vaed
    0xb09: vb09 = ISZERO vb08
    0xb0b: vb0b = ISZERO vb09
    0xb0c: vb0c(0xb14) = CONST 
    0xb0f: JUMPI vb0c(0xb14), vb0b

    Begin block 0xb10
    prev=[0xac3], succ=[]
    =================================
    0xb10: vb10(0x0) = CONST 
    0xb13: REVERT vb10(0x0), vb10(0x0)

    Begin block 0xb140x35c
    prev=[0xac3], succ=[0xb1f0x35c, 0xb280x35c]
    =================================
    0xb160x35c: v35cb16 = GAS 
    0xb170x35c: v35cb17 = STATICCALL v35cb16, vaed, vae6, vb04(0x24), vae6, vafb(0x20)
    0xb180x35c: v35cb18 = ISZERO v35cb17
    0xb1a0x35c: v35cb1a = ISZERO v35cb18
    0xb1b0x35c: v35cb1b(0xb28) = CONST 
    0xb1e0x35c: JUMPI v35cb1b(0xb28), v35cb1a

    Begin block 0xb1f0x35c
    prev=[0xb140x35c], succ=[]
    =================================
    0xb1f0x35c: v35cb1f = RETURNDATASIZE 
    0xb200x35c: v35cb20(0x0) = CONST 
    0xb230x35c: RETURNDATACOPY v35cb20(0x0), v35cb20(0x0), v35cb1f
    0xb240x35c: v35cb24 = RETURNDATASIZE 
    0xb250x35c: v35cb25(0x0) = CONST 
    0xb270x35c: REVERT v35cb25(0x0), v35cb24

    Begin block 0xb280x35c
    prev=[0xb140x35c], succ=[0xb3a0x35c, 0xb3e0x35c]
    =================================
    0xb2d0x35c: v35cb2d(0x40) = CONST 
    0xb2f0x35c: v35cb2f = MLOAD v35cb2d(0x40)
    0xb300x35c: v35cb30 = RETURNDATASIZE 
    0xb310x35c: v35cb31(0x20) = CONST 
    0xb340x35c: v35cb34 = LT v35cb30, v35cb31(0x20)
    0xb350x35c: v35cb35 = ISZERO v35cb34
    0xb360x35c: v35cb36(0xb3e) = CONST 
    0xb390x35c: JUMPI v35cb36(0xb3e), v35cb35

    Begin block 0xb3a0x35c
    prev=[0xb280x35c], succ=[]
    =================================
    0xb3a0x35c: v35cb3a(0x0) = CONST 
    0xb3d0x35c: REVERT v35cb3a(0x0), v35cb3a(0x0)

    Begin block 0xb3e0x35c
    prev=[0xb280x35c], succ=[0xb460x35c, 0xb930x35c]
    =================================
    0xb400x35c: v35cb40 = MLOAD v35cb2f
    0xb420x35c: v35cb42(0xb93) = CONST 
    0xb450x35c: JUMPI v35cb42(0xb93), v35cb40

    Begin block 0xb460x35c
    prev=[0xb3e0x35c], succ=[0xb8f0x35c, 0xa400x35c]
    =================================
    0xb470x35c: v35cb47(0x33) = CONST 
    0xb490x35c: v35cb49 = SLOAD v35cb47(0x33)
    0xb4a0x35c: v35cb4a(0x40) = CONST 
    0xb4d0x35c: v35cb4d = MLOAD v35cb4a(0x40)
    0xb4e0x35c: v35cb4e(0x1a66e793) = CONST 
    0xb530x35c: v35cb53(0xe1) = CONST 
    0xb550x35c: v35cb55(0x34cdcf2600000000000000000000000000000000000000000000000000000000) = SHL v35cb53(0xe1), v35cb4e(0x1a66e793)
    0xb570x35c: MSTORE v35cb4d, v35cb55(0x34cdcf2600000000000000000000000000000000000000000000000000000000)
    0xb580x35c: v35cb58(0x1) = CONST 
    0xb5a0x35c: v35cb5a(0x1) = CONST 
    0xb5c0x35c: v35cb5c(0xa0) = CONST 
    0xb5e0x35c: v35cb5e(0x10000000000000000000000000000000000000000) = SHL v35cb5c(0xa0), v35cb5a(0x1)
    0xb5f0x35c: v35cb5f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35cb5e(0x10000000000000000000000000000000000000000), v35cb58(0x1)
    0xb620x35c: v35cb62 = AND v35cb5f(0xffffffffffffffffffffffffffffffffffffffff), v37d
    0xb630x35c: v35cb63(0x4) = CONST 
    0xb660x35c: v35cb66 = ADD v35cb4d, v35cb63(0x4)
    0xb670x35c: MSTORE v35cb66, v35cb62
    0xb690x35c: v35cb69 = MLOAD v35cb4a(0x40)
    0xb6d0x35c: v35cb6d = AND v35cb49, v35cb5f(0xffffffffffffffffffffffffffffffffffffffff)
    0xb6f0x35c: v35cb6f(0x34cdcf26) = CONST 
    0xb750x35c: v35cb75(0x24) = CONST 
    0xb790x35c: v35cb79 = ADD v35cb4d, v35cb75(0x24)
    0xb7b0x35c: v35cb7b(0x20) = CONST 
    0xb820x35c: v35cb82(0x0) = SUB v35cb4d, v35cb69
    0xb830x35c: v35cb83(0x24) = ADD v35cb82(0x0), v35cb75(0x24)
    0xb870x35c: v35cb87 = EXTCODESIZE v35cb6d
    0xb880x35c: v35cb88 = ISZERO v35cb87
    0xb8a0x35c: v35cb8a = ISZERO v35cb88
    0xb8b0x35c: v35cb8b(0xa40) = CONST 
    0xb8e0x35c: JUMPI v35cb8b(0xa40), v35cb8a

    Begin block 0xb8f0x35c
    prev=[0xb460x35c], succ=[]
    =================================
    0xb8f0x35c: v35cb8f(0x0) = CONST 
    0xb920x35c: REVERT v35cb8f(0x0), v35cb8f(0x0)

    Begin block 0xa400x35c
    prev=[0xb460x35c], succ=[0xa4b0x35c, 0xa540x35c]
    =================================
    0xa420x35c: v35ca42 = GAS 
    0xa430x35c: v35ca43 = STATICCALL v35ca42, v35cb6d, v35cb69, v35cb83(0x24), v35cb69, v35cb7b(0x20)
    0xa440x35c: v35ca44 = ISZERO v35ca43
    0xa460x35c: v35ca46 = ISZERO v35ca44
    0xa470x35c: v35ca47(0xa54) = CONST 
    0xa4a0x35c: JUMPI v35ca47(0xa54), v35ca46

    Begin block 0xa4b0x35c
    prev=[0xa400x35c], succ=[]
    =================================
    0xa4b0x35c: v35ca4b = RETURNDATASIZE 
    0xa4c0x35c: v35ca4c(0x0) = CONST 
    0xa4f0x35c: RETURNDATACOPY v35ca4c(0x0), v35ca4c(0x0), v35ca4b
    0xa500x35c: v35ca50 = RETURNDATASIZE 
    0xa510x35c: v35ca51(0x0) = CONST 
    0xa530x35c: REVERT v35ca51(0x0), v35ca50

    Begin block 0xa540x35c
    prev=[0xa400x35c], succ=[0xa660x35c, 0xa6a0x35c]
    =================================
    0xa590x35c: v35ca59(0x40) = CONST 
    0xa5b0x35c: v35ca5b = MLOAD v35ca59(0x40)
    0xa5c0x35c: v35ca5c = RETURNDATASIZE 
    0xa5d0x35c: v35ca5d(0x20) = CONST 
    0xa600x35c: v35ca60 = LT v35ca5c, v35ca5d(0x20)
    0xa610x35c: v35ca61 = ISZERO v35ca60
    0xa620x35c: v35ca62(0xa6a) = CONST 
    0xa650x35c: JUMPI v35ca62(0xa6a), v35ca61

    Begin block 0xa660x35c
    prev=[0xa540x35c], succ=[]
    =================================
    0xa660x35c: v35ca66(0x0) = CONST 
    0xa690x35c: REVERT v35ca66(0x0), v35ca66(0x0)

    Begin block 0xa6a0x35c
    prev=[0xa540x35c], succ=[0x2085]
    =================================
    0xa6c0x35c: v35ca6c = MLOAD v35ca5b
    0xa710x35c: JUMP v35d(0x2085)

    Begin block 0x2085
    prev=[0xa6a0x35c, 0xb930x35c], succ=[]
    =================================
    0x2085_0x0: v2085_0 = PHI v35cb40, v35ca6c
    0x2086: v2086(0x40) = CONST 
    0x2089: v2089 = MLOAD v2086(0x40)
    0x208b: v208b = ISZERO v2085_0
    0x208c: v208c = ISZERO v208b
    0x208e: MSTORE v2089, v208c
    0x208f: v208f = MLOAD v2086(0x40)
    0x2093: v2093(0x0) = SUB v2089, v208f
    0x2094: v2094(0x20) = CONST 
    0x2096: v2096(0x20) = ADD v2094(0x20), v2093(0x0)
    0x2098: RETURN v208f, v2096(0x20)

    Begin block 0xb930x35c
    prev=[0xb3e0x35c], succ=[0x2085]
    =================================
    0xb980x35c: JUMP v35d(0x2085)

}

function getRaiseOperatorsContract()() public {
    Begin block 0x382
    prev=[], succ=[0xb99B0x382]
    =================================
    0x383: v383(0x20b8) = CONST 
    0x386: v386(0xb99) = CONST 
    0x389: JUMP v386(0xb99)

    Begin block 0xb99B0x382
    prev=[0x382], succ=[0x20b8]
    =================================
    0xb9aS0x382: vb9aV382(0x35) = CONST 
    0xb9cS0x382: vb9cV382 = SLOAD vb9aV382(0x35)
    0xb9dS0x382: vb9dV382(0x1) = CONST 
    0xb9fS0x382: vb9fV382(0x1) = CONST 
    0xba1S0x382: vba1V382(0xa0) = CONST 
    0xba3S0x382: vba3V382(0x10000000000000000000000000000000000000000) = SHL vba1V382(0xa0), vb9fV382(0x1)
    0xba4S0x382: vba4V382(0xffffffffffffffffffffffffffffffffffffffff) = SUB vba3V382(0x10000000000000000000000000000000000000000), vb9dV382(0x1)
    0xba5S0x382: vba5V382 = AND vba4V382(0xffffffffffffffffffffffffffffffffffffffff), vb9cV382
    0xba7S0x382: JUMP v383(0x20b8)

    Begin block 0x20b8
    prev=[0xb99B0x382], succ=[]
    =================================
    0x20b9: v20b9(0x40) = CONST 
    0x20bc: v20bc = MLOAD v20b9(0x40)
    0x20bd: v20bd(0x1) = CONST 
    0x20bf: v20bf(0x1) = CONST 
    0x20c1: v20c1(0xa0) = CONST 
    0x20c3: v20c3(0x10000000000000000000000000000000000000000) = SHL v20c1(0xa0), v20bf(0x1)
    0x20c4: v20c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20c3(0x10000000000000000000000000000000000000000), v20bd(0x1)
    0x20c7: v20c7 = AND vba5V382, v20c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x20c9: MSTORE v20bc, v20c7
    0x20ca: v20ca = MLOAD v20b9(0x40)
    0x20ce: v20ce(0x0) = SUB v20bc, v20ca
    0x20cf: v20cf(0x20) = CONST 
    0x20d1: v20d1(0x20) = ADD v20cf(0x20), v20ce(0x0)
    0x20d3: RETURN v20ca, v20d1(0x20)

}

function isSystem(address)() public {
    Begin block 0x38a
    prev=[], succ=[0x39c, 0x3a0]
    =================================
    0x38b: v38b(0x20f3) = CONST 
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
    prev=[0x38a], succ=[0xba8]
    =================================
    0x3a2: v3a2 = CALLDATALOAD v38e(0x4)
    0x3a3: v3a3(0x1) = CONST 
    0x3a5: v3a5(0x1) = CONST 
    0x3a7: v3a7(0xa0) = CONST 
    0x3a9: v3a9(0x10000000000000000000000000000000000000000) = SHL v3a7(0xa0), v3a5(0x1)
    0x3aa: v3aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a9(0x10000000000000000000000000000000000000000), v3a3(0x1)
    0x3ab: v3ab = AND v3aa(0xffffffffffffffffffffffffffffffffffffffff), v3a2
    0x3ac: v3ac(0xba8) = CONST 
    0x3af: JUMP v3ac(0xba8)

    Begin block 0xba8
    prev=[0x3a0], succ=[0xbf5, 0xa400x38a]
    =================================
    0xba9: vba9(0x33) = CONST 
    0xbab: vbab = SLOAD vba9(0x33)
    0xbac: vbac(0x40) = CONST 
    0xbaf: vbaf = MLOAD vbac(0x40)
    0xbb0: vbb0(0x1a66e793) = CONST 
    0xbb5: vbb5(0xe1) = CONST 
    0xbb7: vbb7(0x34cdcf2600000000000000000000000000000000000000000000000000000000) = SHL vbb5(0xe1), vbb0(0x1a66e793)
    0xbb9: MSTORE vbaf, vbb7(0x34cdcf2600000000000000000000000000000000000000000000000000000000)
    0xbba: vbba(0x1) = CONST 
    0xbbc: vbbc(0x1) = CONST 
    0xbbe: vbbe(0xa0) = CONST 
    0xbc0: vbc0(0x10000000000000000000000000000000000000000) = SHL vbbe(0xa0), vbbc(0x1)
    0xbc1: vbc1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbc0(0x10000000000000000000000000000000000000000), vbba(0x1)
    0xbc4: vbc4 = AND vbc1(0xffffffffffffffffffffffffffffffffffffffff), v3ab
    0xbc5: vbc5(0x4) = CONST 
    0xbc8: vbc8 = ADD vbaf, vbc5(0x4)
    0xbc9: MSTORE vbc8, vbc4
    0xbcb: vbcb = MLOAD vbac(0x40)
    0xbcc: vbcc(0x0) = CONST 
    0xbd2: vbd2 = AND vbab, vbc1(0xffffffffffffffffffffffffffffffffffffffff)
    0xbd4: vbd4(0x34cdcf26) = CONST 
    0xbda: vbda(0x24) = CONST 
    0xbde: vbde = ADD vbaf, vbda(0x24)
    0xbe0: vbe0(0x20) = CONST 
    0xbe8: vbe8(0x0) = SUB vbaf, vbcb
    0xbe9: vbe9(0x24) = ADD vbe8(0x0), vbda(0x24)
    0xbed: vbed = EXTCODESIZE vbd2
    0xbee: vbee = ISZERO vbed
    0xbf0: vbf0 = ISZERO vbee
    0xbf1: vbf1(0xa40) = CONST 
    0xbf4: JUMPI vbf1(0xa40), vbf0

    Begin block 0xbf5
    prev=[0xba8], succ=[]
    =================================
    0xbf5: vbf5(0x0) = CONST 
    0xbf8: REVERT vbf5(0x0), vbf5(0x0)

    Begin block 0xa400x38a
    prev=[0xba8], succ=[0xa4b0x38a, 0xa540x38a]
    =================================
    0xa420x38a: v38aa42 = GAS 
    0xa430x38a: v38aa43 = STATICCALL v38aa42, vbd2, vbcb, vbe9(0x24), vbcb, vbe0(0x20)
    0xa440x38a: v38aa44 = ISZERO v38aa43
    0xa460x38a: v38aa46 = ISZERO v38aa44
    0xa470x38a: v38aa47(0xa54) = CONST 
    0xa4a0x38a: JUMPI v38aa47(0xa54), v38aa46

    Begin block 0xa4b0x38a
    prev=[0xa400x38a], succ=[]
    =================================
    0xa4b0x38a: v38aa4b = RETURNDATASIZE 
    0xa4c0x38a: v38aa4c(0x0) = CONST 
    0xa4f0x38a: RETURNDATACOPY v38aa4c(0x0), v38aa4c(0x0), v38aa4b
    0xa500x38a: v38aa50 = RETURNDATASIZE 
    0xa510x38a: v38aa51(0x0) = CONST 
    0xa530x38a: REVERT v38aa51(0x0), v38aa50

    Begin block 0xa540x38a
    prev=[0xa400x38a], succ=[0xa660x38a, 0xa6a0x38a]
    =================================
    0xa590x38a: v38aa59(0x40) = CONST 
    0xa5b0x38a: v38aa5b = MLOAD v38aa59(0x40)
    0xa5c0x38a: v38aa5c = RETURNDATASIZE 
    0xa5d0x38a: v38aa5d(0x20) = CONST 
    0xa600x38a: v38aa60 = LT v38aa5c, v38aa5d(0x20)
    0xa610x38a: v38aa61 = ISZERO v38aa60
    0xa620x38a: v38aa62(0xa6a) = CONST 
    0xa650x38a: JUMPI v38aa62(0xa6a), v38aa61

    Begin block 0xa660x38a
    prev=[0xa540x38a], succ=[]
    =================================
    0xa660x38a: v38aa66(0x0) = CONST 
    0xa690x38a: REVERT v38aa66(0x0), v38aa66(0x0)

    Begin block 0xa6a0x38a
    prev=[0xa540x38a], succ=[0x20f3]
    =================================
    0xa6c0x38a: v38aa6c = MLOAD v38aa5b
    0xa710x38a: JUMP v38b(0x20f3)

    Begin block 0x20f3
    prev=[0xa6a0x38a], succ=[]
    =================================
    0x20f4: v20f4(0x40) = CONST 
    0x20f7: v20f7 = MLOAD v20f4(0x40)
    0x20f9: v20f9 = ISZERO v38aa6c
    0x20fa: v20fa = ISZERO v20f9
    0x20fc: MSTORE v20f7, v20fa
    0x20fd: v20fd = MLOAD v20f4(0x40)
    0x2101: v2101(0x0) = SUB v20f7, v20fd
    0x2102: v2102(0x20) = CONST 
    0x2104: v2104(0x20) = ADD v2102(0x20), v2101(0x0)
    0x2106: RETURN v20fd, v2104(0x20)

}

function isInitialized()() public {
    Begin block 0x3b0
    prev=[], succ=[0xbf9]
    =================================
    0x3b1: v3b1(0x2126) = CONST 
    0x3b4: v3b4(0xbf9) = CONST 
    0x3b7: JUMP v3b4(0xbf9)

    Begin block 0xbf9
    prev=[0x3b0], succ=[0x2126]
    =================================
    0xbfa: vbfa(0x0) = CONST 
    0xbfc: vbfc = SLOAD vbfa(0x0)
    0xbfd: vbfd(0xff) = CONST 
    0xbff: vbff = AND vbfd(0xff), vbfc
    0xc01: JUMP v3b1(0x2126)

    Begin block 0x2126
    prev=[0xbf9], succ=[]
    =================================
    0x2127: v2127(0x40) = CONST 
    0x212a: v212a = MLOAD v2127(0x40)
    0x212c: v212c = ISZERO vbff
    0x212d: v212d = ISZERO v212c
    0x212f: MSTORE v212a, v212d
    0x2130: v2130 = MLOAD v2127(0x40)
    0x2134: v2134(0x0) = SUB v212a, v2130
    0x2135: v2135(0x20) = CONST 
    0x2137: v2137(0x20) = ADD v2135(0x20), v2134(0x0)
    0x2139: RETURN v2130, v2137(0x20)

}

function proxyAdmin()() public {
    Begin block 0x3b8
    prev=[], succ=[0xc02]
    =================================
    0x3b9: v3b9(0x2159) = CONST 
    0x3bc: v3bc(0xc02) = CONST 
    0x3bf: JUMP v3bc(0xc02)

    Begin block 0xc02
    prev=[0x3b8], succ=[0x2159]
    =================================
    0xc03: vc03(0x38) = CONST 
    0xc05: vc05 = SLOAD vc03(0x38)
    0xc06: vc06(0x1) = CONST 
    0xc08: vc08(0x1) = CONST 
    0xc0a: vc0a(0xa0) = CONST 
    0xc0c: vc0c(0x10000000000000000000000000000000000000000) = SHL vc0a(0xa0), vc08(0x1)
    0xc0d: vc0d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc0c(0x10000000000000000000000000000000000000000), vc06(0x1)
    0xc0e: vc0e = AND vc0d(0xffffffffffffffffffffffffffffffffffffffff), vc05
    0xc10: JUMP v3b9(0x2159)

    Begin block 0x2159
    prev=[0xc02], succ=[]
    =================================
    0x215a: v215a(0x40) = CONST 
    0x215d: v215d = MLOAD v215a(0x40)
    0x215e: v215e(0x1) = CONST 
    0x2160: v2160(0x1) = CONST 
    0x2162: v2162(0xa0) = CONST 
    0x2164: v2164(0x10000000000000000000000000000000000000000) = SHL v2162(0xa0), v2160(0x1)
    0x2165: v2165(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2164(0x10000000000000000000000000000000000000000), v215e(0x1)
    0x2168: v2168 = AND vc0e, v2165(0xffffffffffffffffffffffffffffffffffffffff)
    0x216a: MSTORE v215d, v2168
    0x216b: v216b = MLOAD v215a(0x40)
    0x216f: v216f(0x0) = SUB v215d, v216b
    0x2170: v2170(0x20) = CONST 
    0x2172: v2172(0x20) = ADD v2170(0x20), v216f(0x0)
    0x2174: RETURN v216b, v2172(0x20)

}

function initialize(address,address)() public {
    Begin block 0x3c0
    prev=[], succ=[0x3d2, 0x3d6]
    =================================
    0x3c1: v3c1(0x2194) = CONST 
    0x3c4: v3c4(0x4) = CONST 
    0x3c7: v3c7 = CALLDATASIZE 
    0x3c8: v3c8 = SUB v3c7, v3c4(0x4)
    0x3c9: v3c9(0x40) = CONST 
    0x3cc: v3cc = LT v3c8, v3c9(0x40)
    0x3cd: v3cd = ISZERO v3cc
    0x3ce: v3ce(0x3d6) = CONST 
    0x3d1: JUMPI v3ce(0x3d6), v3cd

    Begin block 0x3d2
    prev=[0x3c0], succ=[]
    =================================
    0x3d2: v3d2(0x0) = CONST 
    0x3d5: REVERT v3d2(0x0), v3d2(0x0)

    Begin block 0x3d6
    prev=[0x3c0], succ=[0xc110x3c0]
    =================================
    0x3d8: v3d8(0x1) = CONST 
    0x3da: v3da(0x1) = CONST 
    0x3dc: v3dc(0xa0) = CONST 
    0x3de: v3de(0x10000000000000000000000000000000000000000) = SHL v3dc(0xa0), v3da(0x1)
    0x3df: v3df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3de(0x10000000000000000000000000000000000000000), v3d8(0x1)
    0x3e1: v3e1 = CALLDATALOAD v3c4(0x4)
    0x3e3: v3e3 = AND v3df(0xffffffffffffffffffffffffffffffffffffffff), v3e1
    0x3e5: v3e5(0x20) = CONST 
    0x3e7: v3e7(0x24) = ADD v3e5(0x20), v3c4(0x4)
    0x3e8: v3e8 = CALLDATALOAD v3e7(0x24)
    0x3e9: v3e9 = AND v3e8, v3df(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ea: v3ea(0xc11) = CONST 
    0x3ed: JUMP v3ea(0xc11)

    Begin block 0xc110x3c0
    prev=[0x3d6], succ=[0xc2a0x3c0, 0xc220x3c0]
    =================================
    0xc120x3c0: v3c0c12(0x0) = CONST 
    0xc140x3c0: v3c0c14 = SLOAD v3c0c12(0x0)
    0xc150x3c0: v3c0c15(0x100) = CONST 
    0xc190x3c0: v3c0c19 = DIV v3c0c14, v3c0c15(0x100)
    0xc1a0x3c0: v3c0c1a(0xff) = CONST 
    0xc1c0x3c0: v3c0c1c = AND v3c0c1a(0xff), v3c0c19
    0xc1e0x3c0: v3c0c1e(0xc2a) = CONST 
    0xc210x3c0: JUMPI v3c0c1e(0xc2a), v3c0c1c

    Begin block 0xc2a0x3c0
    prev=[0xc110x3c0, 0x18eeB0xc220x3c0], succ=[0xc380x3c0, 0xc300x3c0]
    =================================
    0xc2a0x3c0_0x0: vc2a3c0_0 = PHI v3c0c1c, v18f1Vc223c0
    0xc2c0x3c0: v3c0c2c(0xc38) = CONST 
    0xc2f0x3c0: JUMPI v3c0c2c(0xc38), vc2a3c0_0

    Begin block 0xc380x3c0
    prev=[0xc2a0x3c0, 0xc300x3c0], succ=[0xc3d0x3c0, 0xc730x3c0]
    =================================
    0xc380x3c0_0x0: vc383c0_0 = PHI v3c0c37, v3c0c1c, v18f1Vc223c0
    0xc390x3c0: v3c0c39(0xc73) = CONST 
    0xc3c0x3c0: JUMPI v3c0c39(0xc73), vc383c0_0

    Begin block 0xc3d0x3c0
    prev=[0xc380x3c0], succ=[]
    =================================
    0xc3d0x3c0: v3c0c3d(0x40) = CONST 
    0xc3f0x3c0: v3c0c3f = MLOAD v3c0c3d(0x40)
    0xc400x3c0: v3c0c40(0x461bcd) = CONST 
    0xc440x3c0: v3c0c44(0xe5) = CONST 
    0xc460x3c0: v3c0c46(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3c0c44(0xe5), v3c0c40(0x461bcd)
    0xc480x3c0: MSTORE v3c0c3f, v3c0c46(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc490x3c0: v3c0c49(0x4) = CONST 
    0xc4b0x3c0: v3c0c4b = ADD v3c0c49(0x4), v3c0c3f
    0xc4e0x3c0: v3c0c4e(0x20) = CONST 
    0xc500x3c0: v3c0c50 = ADD v3c0c4e(0x20), v3c0c4b
    0xc530x3c0: v3c0c53(0x20) = SUB v3c0c50, v3c0c4b
    0xc550x3c0: MSTORE v3c0c4b, v3c0c53(0x20)
    0xc560x3c0: v3c0c56(0x3d) = CONST 
    0xc590x3c0: MSTORE v3c0c50, v3c0c56(0x3d)
    0xc5a0x3c0: v3c0c5a(0x20) = CONST 
    0xc5c0x3c0: v3c0c5c = ADD v3c0c5a(0x20), v3c0c50
    0xc5e0x3c0: v3c0c5e(0x1cf3) = CONST 
    0xc610x3c0: v3c0c61(0x3d) = CONST 
    0xc640x3c0: CODECOPY v3c0c5c, v3c0c5e(0x1cf3), v3c0c61(0x3d)
    0xc650x3c0: v3c0c65(0x40) = CONST 
    0xc670x3c0: v3c0c67 = ADD v3c0c65(0x40), v3c0c5c
    0xc6b0x3c0: v3c0c6b(0x40) = CONST 
    0xc6d0x3c0: v3c0c6d = MLOAD v3c0c6b(0x40)
    0xc700x3c0: v3c0c70(0x84) = SUB v3c0c67, v3c0c6d
    0xc720x3c0: REVERT v3c0c6d, v3c0c70(0x84)

    Begin block 0xc730x3c0
    prev=[0xc380x3c0], succ=[0xc860x3c0, 0xc9e0x3c0]
    =================================
    0xc740x3c0: v3c0c74(0x0) = CONST 
    0xc760x3c0: v3c0c76 = SLOAD v3c0c74(0x0)
    0xc770x3c0: v3c0c77(0x100) = CONST 
    0xc7b0x3c0: v3c0c7b = DIV v3c0c76, v3c0c77(0x100)
    0xc7c0x3c0: v3c0c7c(0xff) = CONST 
    0xc7e0x3c0: v3c0c7e = AND v3c0c7c(0xff), v3c0c7b
    0xc7f0x3c0: v3c0c7f = ISZERO v3c0c7e
    0xc810x3c0: v3c0c81 = ISZERO v3c0c7f
    0xc820x3c0: v3c0c82(0xc9e) = CONST 
    0xc850x3c0: JUMPI v3c0c82(0xc9e), v3c0c81

    Begin block 0xc860x3c0
    prev=[0xc730x3c0], succ=[0xc9e0x3c0]
    =================================
    0xc860x3c0: v3c0c86(0x0) = CONST 
    0xc890x3c0: v3c0c89 = SLOAD v3c0c86(0x0)
    0xc8a0x3c0: v3c0c8a(0xff) = CONST 
    0xc8c0x3c0: v3c0c8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v3c0c8a(0xff)
    0xc8d0x3c0: v3c0c8d(0xff00) = CONST 
    0xc900x3c0: v3c0c90(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v3c0c8d(0xff00)
    0xc930x3c0: v3c0c93 = AND v3c0c89, v3c0c90(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0xc940x3c0: v3c0c94(0x100) = CONST 
    0xc970x3c0: v3c0c97 = OR v3c0c94(0x100), v3c0c93
    0xc980x3c0: v3c0c98 = AND v3c0c97, v3c0c8c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0xc990x3c0: v3c0c99(0x1) = CONST 
    0xc9b0x3c0: v3c0c9b = OR v3c0c99(0x1), v3c0c98
    0xc9d0x3c0: SSTORE v3c0c86(0x0), v3c0c9b

    Begin block 0xc9e0x3c0
    prev=[0xc860x3c0, 0xc730x3c0], succ=[0xca70x3c0]
    =================================
    0xc9f0x3c0: v3c0c9f(0xca7) = CONST 
    0xca30x3c0: v3c0ca3(0x1791) = CONST 
    0xca60x3c0: CALLPRIVATE v3c0ca3(0x1791), v3e3, v3c0c9f(0xca7)

    Begin block 0xca70x3c0
    prev=[0xc9e0x3c0], succ=[0x18f4B0xca70x3c0]
    =================================
    0xca80x3c0: v3c0ca8(0xcb0) = CONST 
    0xcac0x3c0: v3c0cac(0x18f4) = CONST 
    0xcaf0x3c0: JUMP v3c0cac(0x18f4), v3e9, v3c0ca8(0xcb0)

    Begin block 0x18f4B0xca70x3c0
    prev=[0xca70x3c0], succ=[0x1903B0xca70x3c0, 0x1939B0xca70x3c0]
    =================================
    0x18f5S0xca70x3c0: v18f5Vca73c0(0x1) = CONST 
    0x18f7S0xca70x3c0: v18f7Vca73c0(0x1) = CONST 
    0x18f9S0xca70x3c0: v18f9Vca73c0(0xa0) = CONST 
    0x18fbS0xca70x3c0: v18fbVca73c0(0x10000000000000000000000000000000000000000) = SHL v18f9Vca73c0(0xa0), v18f7Vca73c0(0x1)
    0x18fcS0xca70x3c0: v18fcVca73c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18fbVca73c0(0x10000000000000000000000000000000000000000), v18f5Vca73c0(0x1)
    0x18feS0xca70x3c0: v18feVca73c0 = AND v3e9, v18fcVca73c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x18ffS0xca70x3c0: v18ffVca73c0(0x1939) = CONST 
    0x1902S0xca70x3c0: JUMPI v18ffVca73c0(0x1939), v18feVca73c0

    Begin block 0x1903B0xca70x3c0
    prev=[0x18f4B0xca70x3c0], succ=[]
    =================================
    0x1903S0xca70x3c0: v1903Vca73c0(0x40) = CONST 
    0x1905S0xca70x3c0: v1905Vca73c0 = MLOAD v1903Vca73c0(0x40)
    0x1906S0xca70x3c0: v1906Vca73c0(0x461bcd) = CONST 
    0x190aS0xca70x3c0: v190aVca73c0(0xe5) = CONST 
    0x190cS0xca70x3c0: v190cVca73c0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v190aVca73c0(0xe5), v1906Vca73c0(0x461bcd)
    0x190eS0xca70x3c0: MSTORE v1905Vca73c0, v190cVca73c0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x190fS0xca70x3c0: v190fVca73c0(0x4) = CONST 
    0x1911S0xca70x3c0: v1911Vca73c0 = ADD v190fVca73c0(0x4), v1905Vca73c0
    0x1914S0xca70x3c0: v1914Vca73c0(0x20) = CONST 
    0x1916S0xca70x3c0: v1916Vca73c0 = ADD v1914Vca73c0(0x20), v1911Vca73c0
    0x1919S0xca70x3c0: v1919Vca73c0(0x20) = SUB v1916Vca73c0, v1911Vca73c0
    0x191bS0xca70x3c0: MSTORE v1911Vca73c0, v1919Vca73c0(0x20)
    0x191cS0xca70x3c0: v191cVca73c0(0x49) = CONST 
    0x191fS0xca70x3c0: MSTORE v1916Vca73c0, v191cVca73c0(0x49)
    0x1920S0xca70x3c0: v1920Vca73c0(0x20) = CONST 
    0x1922S0xca70x3c0: v1922Vca73c0 = ADD v1920Vca73c0(0x20), v1916Vca73c0
    0x1924S0xca70x3c0: v1924Vca73c0(0x1aa3) = CONST 
    0x1927S0xca70x3c0: v1927Vca73c0(0x49) = CONST 
    0x192aS0xca70x3c0: CODECOPY v1922Vca73c0, v1924Vca73c0(0x1aa3), v1927Vca73c0(0x49)
    0x192bS0xca70x3c0: v192bVca73c0(0x60) = CONST 
    0x192dS0xca70x3c0: v192dVca73c0 = ADD v192bVca73c0(0x60), v1922Vca73c0
    0x1931S0xca70x3c0: v1931Vca73c0(0x40) = CONST 
    0x1933S0xca70x3c0: v1933Vca73c0 = MLOAD v1931Vca73c0(0x40)
    0x1936S0xca70x3c0: v1936Vca73c0(0xa4) = SUB v192dVca73c0, v1933Vca73c0
    0x1938S0xca70x3c0: REVERT v1933Vca73c0, v1936Vca73c0(0xa4)

    Begin block 0x1939B0xca70x3c0
    prev=[0x18f4B0xca70x3c0], succ=[0xcb00x3c0]
    =================================
    0x193aS0xca70x3c0: v193aVca73c0(0x35) = CONST 
    0x193dS0xca70x3c0: v193dVca73c0 = SLOAD v193aVca73c0(0x35)
    0x193eS0xca70x3c0: v193eVca73c0(0x1) = CONST 
    0x1940S0xca70x3c0: v1940Vca73c0(0x1) = CONST 
    0x1942S0xca70x3c0: v1942Vca73c0(0xa0) = CONST 
    0x1944S0xca70x3c0: v1944Vca73c0(0x10000000000000000000000000000000000000000) = SHL v1942Vca73c0(0xa0), v1940Vca73c0(0x1)
    0x1945S0xca70x3c0: v1945Vca73c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1944Vca73c0(0x10000000000000000000000000000000000000000), v193eVca73c0(0x1)
    0x1946S0xca70x3c0: v1946Vca73c0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1945Vca73c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1947S0xca70x3c0: v1947Vca73c0 = AND v1946Vca73c0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v193dVca73c0
    0x1948S0xca70x3c0: v1948Vca73c0(0x1) = CONST 
    0x194aS0xca70x3c0: v194aVca73c0(0x1) = CONST 
    0x194cS0xca70x3c0: v194cVca73c0(0xa0) = CONST 
    0x194eS0xca70x3c0: v194eVca73c0(0x10000000000000000000000000000000000000000) = SHL v194cVca73c0(0xa0), v194aVca73c0(0x1)
    0x194fS0xca70x3c0: v194fVca73c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v194eVca73c0(0x10000000000000000000000000000000000000000), v1948Vca73c0(0x1)
    0x1951S0xca70x3c0: v1951Vca73c0 = AND v3e9, v194fVca73c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1954S0xca70x3c0: v1954Vca73c0 = OR v1951Vca73c0, v1947Vca73c0
    0x1957S0xca70x3c0: SSTORE v193aVca73c0(0x35), v1954Vca73c0
    0x1958S0xca70x3c0: v1958Vca73c0(0x40) = CONST 
    0x195aS0xca70x3c0: v195aVca73c0 = MLOAD v1958Vca73c0(0x40)
    0x195bS0xca70x3c0: v195bVca73c0 = CALLER 
    0x195dS0xca70x3c0: v195dVca73c0(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c) = CONST 
    0x197fS0xca70x3c0: v197fVca73c0(0x0) = CONST 
    0x1982S0xca70x3c0: LOG3 v195aVca73c0, v197fVca73c0(0x0), v195dVca73c0(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c), v195bVca73c0, v1951Vca73c0
    0x1984S0xca70x3c0: JUMP v3c0ca8(0xcb0)

    Begin block 0xcb00x3c0
    prev=[0x1939B0xca70x3c0], succ=[0xcb70x3c0, 0xcc20x3c0]
    =================================
    0xcb20x3c0: v3c0cb2 = ISZERO v3c0c7f
    0xcb30x3c0: v3c0cb3(0xcc2) = CONST 
    0xcb60x3c0: JUMPI v3c0cb3(0xcc2), v3c0cb2

    Begin block 0xcb70x3c0
    prev=[0xcb00x3c0], succ=[0xcc20x3c0]
    =================================
    0xcb70x3c0: v3c0cb7(0x0) = CONST 
    0xcba0x3c0: v3c0cba = SLOAD v3c0cb7(0x0)
    0xcbb0x3c0: v3c0cbb(0xff00) = CONST 
    0xcbe0x3c0: v3c0cbe(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v3c0cbb(0xff00)
    0xcbf0x3c0: v3c0cbf = AND v3c0cbe(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v3c0cba
    0xcc10x3c0: SSTORE v3c0cb7(0x0), v3c0cbf

    Begin block 0xcc20x3c0
    prev=[0xcb70x3c0, 0xcb00x3c0], succ=[0x2194]
    =================================
    0xcc60x3c0: JUMP v3c1(0x2194)

    Begin block 0x2194
    prev=[0xcc20x3c0], succ=[]
    =================================
    0x2195: STOP 

    Begin block 0xc300x3c0
    prev=[0xc2a0x3c0], succ=[0xc380x3c0]
    =================================
    0xc310x3c0: v3c0c31(0x0) = CONST 
    0xc330x3c0: v3c0c33 = SLOAD v3c0c31(0x0)
    0xc340x3c0: v3c0c34(0xff) = CONST 
    0xc360x3c0: v3c0c36 = AND v3c0c34(0xff), v3c0c33
    0xc370x3c0: v3c0c37 = ISZERO v3c0c36

    Begin block 0xc220x3c0
    prev=[0xc110x3c0], succ=[0x18eeB0xc220x3c0]
    =================================
    0xc230x3c0: v3c0c23(0xc2a) = CONST 
    0xc260x3c0: v3c0c26(0x18ee) = CONST 
    0xc290x3c0: JUMP v3c0c26(0x18ee)

    Begin block 0x18eeB0xc220x3c0
    prev=[0xc220x3c0], succ=[0xc2a0x3c0]
    =================================
    0x18efS0xc220x3c0: v18efVc223c0 = ADDRESS 
    0x18f0S0xc220x3c0: v18f0Vc223c0 = EXTCODESIZE v18efVc223c0
    0x18f1S0xc220x3c0: v18f1Vc223c0 = ISZERO v18f0Vc223c0
    0x18f3S0xc220x3c0: JUMP v3c0c23(0xc2a)

}

function implementation()() public {
    Begin block 0x3ee
    prev=[], succ=[0xcc7]
    =================================
    0x3ef: v3ef(0x21b5) = CONST 
    0x3f2: v3f2(0xcc7) = CONST 
    0x3f5: JUMP v3f2(0xcc7)

    Begin block 0xcc7
    prev=[0x3ee], succ=[0x21b5]
    =================================
    0xcc8: vcc8(0x39) = CONST 
    0xcca: vcca = SLOAD vcc8(0x39)
    0xccb: vccb(0x1) = CONST 
    0xccd: vccd(0x1) = CONST 
    0xccf: vccf(0xa0) = CONST 
    0xcd1: vcd1(0x10000000000000000000000000000000000000000) = SHL vccf(0xa0), vccd(0x1)
    0xcd2: vcd2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcd1(0x10000000000000000000000000000000000000000), vccb(0x1)
    0xcd3: vcd3 = AND vcd2(0xffffffffffffffffffffffffffffffffffffffff), vcca
    0xcd5: JUMP v3ef(0x21b5)

    Begin block 0x21b5
    prev=[0xcc7], succ=[]
    =================================
    0x21b6: v21b6(0x40) = CONST 
    0x21b9: v21b9 = MLOAD v21b6(0x40)
    0x21ba: v21ba(0x1) = CONST 
    0x21bc: v21bc(0x1) = CONST 
    0x21be: v21be(0xa0) = CONST 
    0x21c0: v21c0(0x10000000000000000000000000000000000000000) = SHL v21be(0xa0), v21bc(0x1)
    0x21c1: v21c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21c0(0x10000000000000000000000000000000000000000), v21ba(0x1)
    0x21c4: v21c4 = AND vcd3, v21c1(0xffffffffffffffffffffffffffffffffffffffff)
    0x21c6: MSTORE v21b9, v21c4
    0x21c7: v21c7 = MLOAD v21b6(0x40)
    0x21cb: v21cb(0x0) = SUB v21b9, v21c7
    0x21cc: v21cc(0x20) = CONST 
    0x21ce: v21ce(0x20) = ADD v21cc(0x20), v21cb(0x0)
    0x21d0: RETURN v21c7, v21ce(0x20)

}

function getOperatorsContract()() public {
    Begin block 0x3f6
    prev=[], succ=[0xcd6B0x3f6]
    =================================
    0x3f7: v3f7(0x21f0) = CONST 
    0x3fa: v3fa(0xcd6) = CONST 
    0x3fd: JUMP v3fa(0xcd6)

    Begin block 0xcd6B0x3f6
    prev=[0x3f6], succ=[0x21f0]
    =================================
    0xcd7S0x3f6: vcd7V3f6(0x33) = CONST 
    0xcd9S0x3f6: vcd9V3f6 = SLOAD vcd7V3f6(0x33)
    0xcdaS0x3f6: vcdaV3f6(0x1) = CONST 
    0xcdcS0x3f6: vcdcV3f6(0x1) = CONST 
    0xcdeS0x3f6: vcdeV3f6(0xa0) = CONST 
    0xce0S0x3f6: vce0V3f6(0x10000000000000000000000000000000000000000) = SHL vcdeV3f6(0xa0), vcdcV3f6(0x1)
    0xce1S0x3f6: vce1V3f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce0V3f6(0x10000000000000000000000000000000000000000), vcdaV3f6(0x1)
    0xce2S0x3f6: vce2V3f6 = AND vce1V3f6(0xffffffffffffffffffffffffffffffffffffffff), vcd9V3f6
    0xce4S0x3f6: JUMP v3f7(0x21f0)

    Begin block 0x21f0
    prev=[0xcd6B0x3f6], succ=[]
    =================================
    0x21f1: v21f1(0x40) = CONST 
    0x21f4: v21f4 = MLOAD v21f1(0x40)
    0x21f5: v21f5(0x1) = CONST 
    0x21f7: v21f7(0x1) = CONST 
    0x21f9: v21f9(0xa0) = CONST 
    0x21fb: v21fb(0x10000000000000000000000000000000000000000) = SHL v21f9(0xa0), v21f7(0x1)
    0x21fc: v21fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21fb(0x10000000000000000000000000000000000000000), v21f5(0x1)
    0x21ff: v21ff = AND vce2V3f6, v21fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x2201: MSTORE v21f4, v21ff
    0x2202: v2202 = MLOAD v21f1(0x40)
    0x2206: v2206(0x0) = SUB v21f4, v2202
    0x2207: v2207(0x20) = CONST 
    0x2209: v2209(0x20) = ADD v2207(0x20), v2206(0x0)
    0x220b: RETURN v2202, v2209(0x20)

}

function implementationExists(bytes32)() public {
    Begin block 0x3fe
    prev=[], succ=[0x410, 0x414]
    =================================
    0x3ff: v3ff(0x222b) = CONST 
    0x402: v402(0x4) = CONST 
    0x405: v405 = CALLDATASIZE 
    0x406: v406 = SUB v405, v402(0x4)
    0x407: v407(0x20) = CONST 
    0x40a: v40a = LT v406, v407(0x20)
    0x40b: v40b = ISZERO v40a
    0x40c: v40c(0x414) = CONST 
    0x40f: JUMPI v40c(0x414), v40b

    Begin block 0x410
    prev=[0x3fe], succ=[]
    =================================
    0x410: v410(0x0) = CONST 
    0x413: REVERT v410(0x0), v410(0x0)

    Begin block 0x414
    prev=[0x3fe], succ=[0xce5]
    =================================
    0x416: v416 = CALLDATALOAD v402(0x4)
    0x417: v417(0xce5) = CONST 
    0x41a: JUMP v417(0xce5)

    Begin block 0xce5
    prev=[0x414], succ=[0x222b]
    =================================
    0xce6: vce6(0x0) = CONST 
    0xcea: MSTORE vce6(0x0), v416
    0xceb: vceb(0x3a) = CONST 
    0xced: vced(0x20) = CONST 
    0xcef: MSTORE vced(0x20), vceb(0x3a)
    0xcf0: vcf0(0x40) = CONST 
    0xcf3: vcf3 = SHA3 vce6(0x0), vcf0(0x40)
    0xcf4: vcf4 = SLOAD vcf3
    0xcf5: vcf5(0x1) = CONST 
    0xcf7: vcf7(0x1) = CONST 
    0xcf9: vcf9(0xa0) = CONST 
    0xcfb: vcfb(0x10000000000000000000000000000000000000000) = SHL vcf9(0xa0), vcf7(0x1)
    0xcfc: vcfc(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcfb(0x10000000000000000000000000000000000000000), vcf5(0x1)
    0xcfd: vcfd = AND vcfc(0xffffffffffffffffffffffffffffffffffffffff), vcf4
    0xcfe: vcfe = ISZERO vcfd
    0xcff: vcff = ISZERO vcfe
    0xd01: JUMP v3ff(0x222b)

    Begin block 0x222b
    prev=[0xce5], succ=[]
    =================================
    0x222c: v222c(0x40) = CONST 
    0x222f: v222f = MLOAD v222c(0x40)
    0x2231: v2231 = ISZERO vcff
    0x2232: v2232 = ISZERO v2231
    0x2234: MSTORE v222f, v2232
    0x2235: v2235 = MLOAD v222c(0x40)
    0x2239: v2239(0x0) = SUB v222f, v2235
    0x223a: v223a(0x20) = CONST 
    0x223c: v223c(0x20) = ADD v223a(0x20), v2239(0x0)
    0x223e: RETURN v2235, v223c(0x20)

}

function newRaiseProposal(bytes32)() public {
    Begin block 0x41b
    prev=[], succ=[0x42d, 0x431]
    =================================
    0x41c: v41c(0x225e) = CONST 
    0x41f: v41f(0x4) = CONST 
    0x422: v422 = CALLDATASIZE 
    0x423: v423 = SUB v422, v41f(0x4)
    0x424: v424(0x20) = CONST 
    0x427: v427 = LT v423, v424(0x20)
    0x428: v428 = ISZERO v427
    0x429: v429(0x431) = CONST 
    0x42c: JUMPI v429(0x431), v428

    Begin block 0x42d
    prev=[0x41b], succ=[]
    =================================
    0x42d: v42d(0x0) = CONST 
    0x430: REVERT v42d(0x0), v42d(0x0)

    Begin block 0x431
    prev=[0x41b], succ=[0xd02]
    =================================
    0x433: v433 = CALLDATALOAD v41f(0x4)
    0x434: v434(0xd02) = CONST 
    0x437: JUMP v434(0xd02)

    Begin block 0xd02
    prev=[0x431], succ=[0xf4bB0xd02]
    =================================
    0xd03: vd03(0xd0b) = CONST 
    0xd06: vd06 = CALLER 
    0xd07: vd07(0xf4b) = CONST 
    0xd0a: JUMP vd07(0xf4b)

    Begin block 0xf4bB0xd02
    prev=[0xd02], succ=[0xf980xf4bB0xd02, 0xa400xf4bB0xd02]
    =================================
    0xf4cS0xd02: vf4cVd02(0x35) = CONST 
    0xf4eS0xd02: vf4eVd02 = SLOAD vf4cVd02(0x35)
    0xf4fS0xd02: vf4fVd02(0x40) = CONST 
    0xf52S0xd02: vf52Vd02 = MLOAD vf4fVd02(0x40)
    0xf53S0xd02: vf53Vd02(0x877b9a67) = CONST 
    0xf58S0xd02: vf58Vd02(0xe0) = CONST 
    0xf5aS0xd02: vf5aVd02(0x877b9a6700000000000000000000000000000000000000000000000000000000) = SHL vf58Vd02(0xe0), vf53Vd02(0x877b9a67)
    0xf5cS0xd02: MSTORE vf52Vd02, vf5aVd02(0x877b9a6700000000000000000000000000000000000000000000000000000000)
    0xf5dS0xd02: vf5dVd02(0x1) = CONST 
    0xf5fS0xd02: vf5fVd02(0x1) = CONST 
    0xf61S0xd02: vf61Vd02(0xa0) = CONST 
    0xf63S0xd02: vf63Vd02(0x10000000000000000000000000000000000000000) = SHL vf61Vd02(0xa0), vf5fVd02(0x1)
    0xf64S0xd02: vf64Vd02(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf63Vd02(0x10000000000000000000000000000000000000000), vf5dVd02(0x1)
    0xf67S0xd02: vf67Vd02 = AND vf64Vd02(0xffffffffffffffffffffffffffffffffffffffff), vd06
    0xf68S0xd02: vf68Vd02(0x4) = CONST 
    0xf6bS0xd02: vf6bVd02 = ADD vf52Vd02, vf68Vd02(0x4)
    0xf6cS0xd02: MSTORE vf6bVd02, vf67Vd02
    0xf6eS0xd02: vf6eVd02 = MLOAD vf4fVd02(0x40)
    0xf6fS0xd02: vf6fVd02(0x0) = CONST 
    0xf75S0xd02: vf75Vd02 = AND vf4eVd02, vf64Vd02(0xffffffffffffffffffffffffffffffffffffffff)
    0xf77S0xd02: vf77Vd02(0x877b9a67) = CONST 
    0xf7dS0xd02: vf7dVd02(0x24) = CONST 
    0xf81S0xd02: vf81Vd02 = ADD vf52Vd02, vf7dVd02(0x24)
    0xf83S0xd02: vf83Vd02(0x20) = CONST 
    0xf8bS0xd02: vf8bVd02(0x0) = SUB vf52Vd02, vf6eVd02
    0xf8cS0xd02: vf8cVd02(0x24) = ADD vf8bVd02(0x0), vf7dVd02(0x24)
    0xf90S0xd02: vf90Vd02 = EXTCODESIZE vf75Vd02
    0xf91S0xd02: vf91Vd02 = ISZERO vf90Vd02
    0xf93S0xd02: vf93Vd02 = ISZERO vf91Vd02
    0xf94S0xd02: vf94Vd02(0xa40) = CONST 
    0xf97S0xd02: JUMPI vf94Vd02(0xa40), vf93Vd02

    Begin block 0xf980xf4bB0xd02
    prev=[0xf4bB0xd02], succ=[]
    =================================
    0xf980xf4bS0xd02: vf4bf98Vd02(0x0) = CONST 
    0xf9b0xf4bS0xd02: REVERT vf4bf98Vd02(0x0), vf4bf98Vd02(0x0)

    Begin block 0xa400xf4bB0xd02
    prev=[0xf4bB0xd02], succ=[0xa4b0xf4bB0xd02, 0xa540xf4bB0xd02]
    =================================
    0xa420xf4bS0xd02: vf4ba42Vd02 = GAS 
    0xa430xf4bS0xd02: vf4ba43Vd02 = STATICCALL vf4ba42Vd02, vf75Vd02, vf6eVd02, vf8cVd02(0x24), vf6eVd02, vf83Vd02(0x20)
    0xa440xf4bS0xd02: vf4ba44Vd02 = ISZERO vf4ba43Vd02
    0xa460xf4bS0xd02: vf4ba46Vd02 = ISZERO vf4ba44Vd02
    0xa470xf4bS0xd02: vf4ba47Vd02(0xa54) = CONST 
    0xa4a0xf4bS0xd02: JUMPI vf4ba47Vd02(0xa54), vf4ba46Vd02

    Begin block 0xa4b0xf4bB0xd02
    prev=[0xa400xf4bB0xd02], succ=[]
    =================================
    0xa4b0xf4bS0xd02: vf4ba4bVd02 = RETURNDATASIZE 
    0xa4c0xf4bS0xd02: vf4ba4cVd02(0x0) = CONST 
    0xa4f0xf4bS0xd02: RETURNDATACOPY vf4ba4cVd02(0x0), vf4ba4cVd02(0x0), vf4ba4bVd02
    0xa500xf4bS0xd02: vf4ba50Vd02 = RETURNDATASIZE 
    0xa510xf4bS0xd02: vf4ba51Vd02(0x0) = CONST 
    0xa530xf4bS0xd02: REVERT vf4ba51Vd02(0x0), vf4ba50Vd02

    Begin block 0xa540xf4bB0xd02
    prev=[0xa400xf4bB0xd02], succ=[0xa660xf4bB0xd02, 0xa6a0xf4bB0xd02]
    =================================
    0xa590xf4bS0xd02: vf4ba59Vd02(0x40) = CONST 
    0xa5b0xf4bS0xd02: vf4ba5bVd02 = MLOAD vf4ba59Vd02(0x40)
    0xa5c0xf4bS0xd02: vf4ba5cVd02 = RETURNDATASIZE 
    0xa5d0xf4bS0xd02: vf4ba5dVd02(0x20) = CONST 
    0xa600xf4bS0xd02: vf4ba60Vd02 = LT vf4ba5cVd02, vf4ba5dVd02(0x20)
    0xa610xf4bS0xd02: vf4ba61Vd02 = ISZERO vf4ba60Vd02
    0xa620xf4bS0xd02: vf4ba62Vd02(0xa6a) = CONST 
    0xa650xf4bS0xd02: JUMPI vf4ba62Vd02(0xa6a), vf4ba61Vd02

    Begin block 0xa660xf4bB0xd02
    prev=[0xa540xf4bB0xd02], succ=[]
    =================================
    0xa660xf4bS0xd02: vf4ba66Vd02(0x0) = CONST 
    0xa690xf4bS0xd02: REVERT vf4ba66Vd02(0x0), vf4ba66Vd02(0x0)

    Begin block 0xa6a0xf4bB0xd02
    prev=[0xa540xf4bB0xd02], succ=[0xd0b]
    =================================
    0xa6c0xf4bS0xd02: vf4ba6cVd02 = MLOAD vf4ba5bVd02
    0xa710xf4bS0xd02: JUMP vd03(0xd0b)

    Begin block 0xd0b
    prev=[0xa6a0xf4bB0xd02], succ=[0xd10, 0xd46]
    =================================
    0xd0c: vd0c(0xd46) = CONST 
    0xd0f: JUMPI vd0c(0xd46), vf4ba6cVd02

    Begin block 0xd10
    prev=[0xd0b], succ=[]
    =================================
    0xd10: vd10(0x40) = CONST 
    0xd12: vd12 = MLOAD vd10(0x40)
    0xd13: vd13(0x461bcd) = CONST 
    0xd17: vd17(0xe5) = CONST 
    0xd19: vd19(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd17(0xe5), vd13(0x461bcd)
    0xd1b: MSTORE vd12, vd19(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd1c: vd1c(0x4) = CONST 
    0xd1e: vd1e = ADD vd1c(0x4), vd12
    0xd21: vd21(0x20) = CONST 
    0xd23: vd23 = ADD vd21(0x20), vd1e
    0xd26: vd26(0x20) = SUB vd23, vd1e
    0xd28: MSTORE vd1e, vd26(0x20)
    0xd29: vd29(0x27) = CONST 
    0xd2c: MSTORE vd23, vd29(0x27)
    0xd2d: vd2d(0x20) = CONST 
    0xd2f: vd2f = ADD vd2d(0x20), vd23
    0xd31: vd31(0x1c8d) = CONST 
    0xd34: vd34(0x27) = CONST 
    0xd37: CODECOPY vd2f, vd31(0x1c8d), vd34(0x27)
    0xd38: vd38(0x40) = CONST 
    0xd3a: vd3a = ADD vd38(0x40), vd2f
    0xd3e: vd3e(0x40) = CONST 
    0xd40: vd40 = MLOAD vd3e(0x40)
    0xd43: vd43(0x84) = SUB vd3a, vd40
    0xd45: REVERT vd40, vd43(0x84)

    Begin block 0xd46
    prev=[0xd0b], succ=[0xd67, 0xdb3]
    =================================
    0xd47: vd47(0x0) = CONST 
    0xd4b: MSTORE vd47(0x0), v433
    0xd4c: vd4c(0x3a) = CONST 
    0xd4e: vd4e(0x20) = CONST 
    0xd50: MSTORE vd4e(0x20), vd4c(0x3a)
    0xd51: vd51(0x40) = CONST 
    0xd54: vd54 = SHA3 vd47(0x0), vd51(0x40)
    0xd55: vd55(0x2) = CONST 
    0xd57: vd57 = ADD vd55(0x2), vd54
    0xd58: vd58 = SLOAD vd57
    0xd59: vd59(0x1) = CONST 
    0xd5b: vd5b(0x1) = CONST 
    0xd5d: vd5d(0xa0) = CONST 
    0xd5f: vd5f(0x10000000000000000000000000000000000000000) = SHL vd5d(0xa0), vd5b(0x1)
    0xd60: vd60(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd5f(0x10000000000000000000000000000000000000000), vd59(0x1)
    0xd61: vd61 = AND vd60(0xffffffffffffffffffffffffffffffffffffffff), vd58
    0xd62: vd62 = ISZERO vd61
    0xd63: vd63(0xdb3) = CONST 
    0xd66: JUMPI vd63(0xdb3), vd62

    Begin block 0xd67
    prev=[0xd46], succ=[]
    =================================
    0xd67: vd67(0x40) = CONST 
    0xd6a: vd6a = MLOAD vd67(0x40)
    0xd6b: vd6b(0x461bcd) = CONST 
    0xd6f: vd6f(0xe5) = CONST 
    0xd71: vd71(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd6f(0xe5), vd6b(0x461bcd)
    0xd73: MSTORE vd6a, vd71(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd74: vd74(0x20) = CONST 
    0xd76: vd76(0x4) = CONST 
    0xd79: vd79 = ADD vd6a, vd76(0x4)
    0xd7a: MSTORE vd79, vd74(0x20)
    0xd7b: vd7b(0x1c) = CONST 
    0xd7d: vd7d(0x24) = CONST 
    0xd80: vd80 = ADD vd6a, vd7d(0x24)
    0xd81: MSTORE vd80, vd7b(0x1c)
    0xd82: vd82(0x5261697365466163746f72793a20616c72656164792065786973747300000000) = CONST 
    0xda3: vda3(0x44) = CONST 
    0xda6: vda6 = ADD vd6a, vda3(0x44)
    0xda7: MSTORE vda6, vd82(0x5261697365466163746f72793a20616c72656164792065786973747300000000)
    0xda9: vda9 = MLOAD vd67(0x40)
    0xdad: vdad(0x0) = SUB vd6a, vda9
    0xdae: vdae(0x64) = CONST 
    0xdb0: vdb0(0x64) = ADD vdae(0x64), vdad(0x0)
    0xdb2: REVERT vda9, vdb0(0x64)

    Begin block 0xdb3
    prev=[0xd46], succ=[0x225e]
    =================================
    0xdb4: vdb4(0x0) = CONST 
    0xdb8: MSTORE vdb4(0x0), v433
    0xdb9: vdb9(0x3a) = CONST 
    0xdbb: vdbb(0x20) = CONST 
    0xdbd: MSTORE vdbb(0x20), vdb9(0x3a)
    0xdbe: vdbe(0x40) = CONST 
    0xdc2: vdc2 = SHA3 vdb4(0x0), vdbe(0x40)
    0xdc3: vdc3(0x2) = CONST 
    0xdc5: vdc5 = ADD vdc3(0x2), vdc2
    0xdc7: vdc7 = SLOAD vdc5
    0xdc8: vdc8(0x1) = CONST 
    0xdca: vdca(0x1) = CONST 
    0xdcc: vdcc(0xa0) = CONST 
    0xdce: vdce(0x10000000000000000000000000000000000000000) = SHL vdcc(0xa0), vdca(0x1)
    0xdcf: vdcf(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdce(0x10000000000000000000000000000000000000000), vdc8(0x1)
    0xdd0: vdd0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vdcf(0xffffffffffffffffffffffffffffffffffffffff)
    0xdd1: vdd1 = AND vdd0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdc7
    0xdd2: vdd2 = CALLER 
    0xdd5: vdd5 = OR vdd2, vdd1
    0xdd8: SSTORE vdc5, vdd5
    0xdda: vdda = MLOAD vdbe(0x40)
    0xddd: vddd(0xa098e4aa95181d7892af9a687441a51cb9704f834c52294185e9f80aea7291c3) = CONST 
    0xdff: LOG3 vdda, vdb4(0x0), vddd(0xa098e4aa95181d7892af9a687441a51cb9704f834c52294185e9f80aea7291c3), vdd2, v433
    0xe01: JUMP v41c(0x225e)

    Begin block 0x225e
    prev=[0xdb3], succ=[]
    =================================
    0x225f: STOP 

}

function isMultisig(address)() public {
    Begin block 0x438
    prev=[], succ=[0x44a, 0x44e]
    =================================
    0x439: v439(0x227f) = CONST 
    0x43c: v43c(0x4) = CONST 
    0x43f: v43f = CALLDATASIZE 
    0x440: v440 = SUB v43f, v43c(0x4)
    0x441: v441(0x20) = CONST 
    0x444: v444 = LT v440, v441(0x20)
    0x445: v445 = ISZERO v444
    0x446: v446(0x44e) = CONST 
    0x449: JUMPI v446(0x44e), v445

    Begin block 0x44a
    prev=[0x438], succ=[]
    =================================
    0x44a: v44a(0x0) = CONST 
    0x44d: REVERT v44a(0x0), v44a(0x0)

    Begin block 0x44e
    prev=[0x438], succ=[0xe02]
    =================================
    0x450: v450 = CALLDATALOAD v43c(0x4)
    0x451: v451(0x1) = CONST 
    0x453: v453(0x1) = CONST 
    0x455: v455(0xa0) = CONST 
    0x457: v457(0x10000000000000000000000000000000000000000) = SHL v455(0xa0), v453(0x1)
    0x458: v458(0xffffffffffffffffffffffffffffffffffffffff) = SUB v457(0x10000000000000000000000000000000000000000), v451(0x1)
    0x459: v459 = AND v458(0xffffffffffffffffffffffffffffffffffffffff), v450
    0x45a: v45a(0xe02) = CONST 
    0x45d: JUMP v45a(0xe02)

    Begin block 0xe02
    prev=[0x44e], succ=[0xe4f, 0xa400x438]
    =================================
    0xe03: ve03(0x33) = CONST 
    0xe05: ve05 = SLOAD ve03(0x33)
    0xe06: ve06(0x40) = CONST 
    0xe09: ve09 = MLOAD ve06(0x40)
    0xe0a: ve0a(0x3347b567) = CONST 
    0xe0f: ve0f(0xe1) = CONST 
    0xe11: ve11(0x668f6ace00000000000000000000000000000000000000000000000000000000) = SHL ve0f(0xe1), ve0a(0x3347b567)
    0xe13: MSTORE ve09, ve11(0x668f6ace00000000000000000000000000000000000000000000000000000000)
    0xe14: ve14(0x1) = CONST 
    0xe16: ve16(0x1) = CONST 
    0xe18: ve18(0xa0) = CONST 
    0xe1a: ve1a(0x10000000000000000000000000000000000000000) = SHL ve18(0xa0), ve16(0x1)
    0xe1b: ve1b(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve1a(0x10000000000000000000000000000000000000000), ve14(0x1)
    0xe1e: ve1e = AND ve1b(0xffffffffffffffffffffffffffffffffffffffff), v459
    0xe1f: ve1f(0x4) = CONST 
    0xe22: ve22 = ADD ve09, ve1f(0x4)
    0xe23: MSTORE ve22, ve1e
    0xe25: ve25 = MLOAD ve06(0x40)
    0xe26: ve26(0x0) = CONST 
    0xe2c: ve2c = AND ve05, ve1b(0xffffffffffffffffffffffffffffffffffffffff)
    0xe2e: ve2e(0x668f6ace) = CONST 
    0xe34: ve34(0x24) = CONST 
    0xe38: ve38 = ADD ve09, ve34(0x24)
    0xe3a: ve3a(0x20) = CONST 
    0xe42: ve42(0x0) = SUB ve09, ve25
    0xe43: ve43(0x24) = ADD ve42(0x0), ve34(0x24)
    0xe47: ve47 = EXTCODESIZE ve2c
    0xe48: ve48 = ISZERO ve47
    0xe4a: ve4a = ISZERO ve48
    0xe4b: ve4b(0xa40) = CONST 
    0xe4e: JUMPI ve4b(0xa40), ve4a

    Begin block 0xe4f
    prev=[0xe02], succ=[]
    =================================
    0xe4f: ve4f(0x0) = CONST 
    0xe52: REVERT ve4f(0x0), ve4f(0x0)

    Begin block 0xa400x438
    prev=[0xe02], succ=[0xa4b0x438, 0xa540x438]
    =================================
    0xa420x438: v438a42 = GAS 
    0xa430x438: v438a43 = STATICCALL v438a42, ve2c, ve25, ve43(0x24), ve25, ve3a(0x20)
    0xa440x438: v438a44 = ISZERO v438a43
    0xa460x438: v438a46 = ISZERO v438a44
    0xa470x438: v438a47(0xa54) = CONST 
    0xa4a0x438: JUMPI v438a47(0xa54), v438a46

    Begin block 0xa4b0x438
    prev=[0xa400x438], succ=[]
    =================================
    0xa4b0x438: v438a4b = RETURNDATASIZE 
    0xa4c0x438: v438a4c(0x0) = CONST 
    0xa4f0x438: RETURNDATACOPY v438a4c(0x0), v438a4c(0x0), v438a4b
    0xa500x438: v438a50 = RETURNDATASIZE 
    0xa510x438: v438a51(0x0) = CONST 
    0xa530x438: REVERT v438a51(0x0), v438a50

    Begin block 0xa540x438
    prev=[0xa400x438], succ=[0xa660x438, 0xa6a0x438]
    =================================
    0xa590x438: v438a59(0x40) = CONST 
    0xa5b0x438: v438a5b = MLOAD v438a59(0x40)
    0xa5c0x438: v438a5c = RETURNDATASIZE 
    0xa5d0x438: v438a5d(0x20) = CONST 
    0xa600x438: v438a60 = LT v438a5c, v438a5d(0x20)
    0xa610x438: v438a61 = ISZERO v438a60
    0xa620x438: v438a62(0xa6a) = CONST 
    0xa650x438: JUMPI v438a62(0xa6a), v438a61

    Begin block 0xa660x438
    prev=[0xa540x438], succ=[]
    =================================
    0xa660x438: v438a66(0x0) = CONST 
    0xa690x438: REVERT v438a66(0x0), v438a66(0x0)

    Begin block 0xa6a0x438
    prev=[0xa540x438], succ=[0x227f]
    =================================
    0xa6c0x438: v438a6c = MLOAD v438a5b
    0xa710x438: JUMP v439(0x227f)

    Begin block 0x227f
    prev=[0xa6a0x438], succ=[]
    =================================
    0x2280: v2280(0x40) = CONST 
    0x2283: v2283 = MLOAD v2280(0x40)
    0x2285: v2285 = ISZERO v438a6c
    0x2286: v2286 = ISZERO v2285
    0x2288: MSTORE v2283, v2286
    0x2289: v2289 = MLOAD v2280(0x40)
    0x228d: v228d(0x0) = SUB v2283, v2289
    0x228e: v228e(0x20) = CONST 
    0x2290: v2290(0x20) = ADD v228e(0x20), v228d(0x0)
    0x2292: RETURN v2289, v2290(0x20)

}

function isOperator(address)() public {
    Begin block 0x45e
    prev=[], succ=[0x470, 0x474]
    =================================
    0x45f: v45f(0x22b2) = CONST 
    0x462: v462(0x4) = CONST 
    0x465: v465 = CALLDATASIZE 
    0x466: v466 = SUB v465, v462(0x4)
    0x467: v467(0x20) = CONST 
    0x46a: v46a = LT v466, v467(0x20)
    0x46b: v46b = ISZERO v46a
    0x46c: v46c(0x474) = CONST 
    0x46f: JUMPI v46c(0x474), v46b

    Begin block 0x470
    prev=[0x45e], succ=[]
    =================================
    0x470: v470(0x0) = CONST 
    0x473: REVERT v470(0x0), v470(0x0)

    Begin block 0x474
    prev=[0x45e], succ=[0xe530x45e]
    =================================
    0x476: v476 = CALLDATALOAD v462(0x4)
    0x477: v477(0x1) = CONST 
    0x479: v479(0x1) = CONST 
    0x47b: v47b(0xa0) = CONST 
    0x47d: v47d(0x10000000000000000000000000000000000000000) = SHL v47b(0xa0), v479(0x1)
    0x47e: v47e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v47d(0x10000000000000000000000000000000000000000), v477(0x1)
    0x47f: v47f = AND v47e(0xffffffffffffffffffffffffffffffffffffffff), v476
    0x480: v480(0xe53) = CONST 
    0x483: JUMP v480(0xe53)

    Begin block 0xe530x45e
    prev=[0x474], succ=[0xea00x45e, 0xa400x45e]
    =================================
    0xe540x45e: v45ee54(0x33) = CONST 
    0xe560x45e: v45ee56 = SLOAD v45ee54(0x33)
    0xe570x45e: v45ee57(0x40) = CONST 
    0xe5a0x45e: v45ee5a = MLOAD v45ee57(0x40)
    0xe5b0x45e: v45ee5b(0x36b87bd7) = CONST 
    0xe600x45e: v45ee60(0xe1) = CONST 
    0xe620x45e: v45ee62(0x6d70f7ae00000000000000000000000000000000000000000000000000000000) = SHL v45ee60(0xe1), v45ee5b(0x36b87bd7)
    0xe640x45e: MSTORE v45ee5a, v45ee62(0x6d70f7ae00000000000000000000000000000000000000000000000000000000)
    0xe650x45e: v45ee65(0x1) = CONST 
    0xe670x45e: v45ee67(0x1) = CONST 
    0xe690x45e: v45ee69(0xa0) = CONST 
    0xe6b0x45e: v45ee6b(0x10000000000000000000000000000000000000000) = SHL v45ee69(0xa0), v45ee67(0x1)
    0xe6c0x45e: v45ee6c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45ee6b(0x10000000000000000000000000000000000000000), v45ee65(0x1)
    0xe6f0x45e: v45ee6f = AND v45ee6c(0xffffffffffffffffffffffffffffffffffffffff), v47f
    0xe700x45e: v45ee70(0x4) = CONST 
    0xe730x45e: v45ee73 = ADD v45ee5a, v45ee70(0x4)
    0xe740x45e: MSTORE v45ee73, v45ee6f
    0xe760x45e: v45ee76 = MLOAD v45ee57(0x40)
    0xe770x45e: v45ee77(0x0) = CONST 
    0xe7d0x45e: v45ee7d = AND v45ee56, v45ee6c(0xffffffffffffffffffffffffffffffffffffffff)
    0xe7f0x45e: v45ee7f(0x6d70f7ae) = CONST 
    0xe850x45e: v45ee85(0x24) = CONST 
    0xe890x45e: v45ee89 = ADD v45ee5a, v45ee85(0x24)
    0xe8b0x45e: v45ee8b(0x20) = CONST 
    0xe930x45e: v45ee93(0x0) = SUB v45ee5a, v45ee76
    0xe940x45e: v45ee94(0x24) = ADD v45ee93(0x0), v45ee85(0x24)
    0xe980x45e: v45ee98 = EXTCODESIZE v45ee7d
    0xe990x45e: v45ee99 = ISZERO v45ee98
    0xe9b0x45e: v45ee9b = ISZERO v45ee99
    0xe9c0x45e: v45ee9c(0xa40) = CONST 
    0xe9f0x45e: JUMPI v45ee9c(0xa40), v45ee9b

    Begin block 0xea00x45e
    prev=[0xe530x45e], succ=[]
    =================================
    0xea00x45e: v45eea0(0x0) = CONST 
    0xea30x45e: REVERT v45eea0(0x0), v45eea0(0x0)

    Begin block 0xa400x45e
    prev=[0xe530x45e], succ=[0xa4b0x45e, 0xa540x45e]
    =================================
    0xa420x45e: v45ea42 = GAS 
    0xa430x45e: v45ea43 = STATICCALL v45ea42, v45ee7d, v45ee76, v45ee94(0x24), v45ee76, v45ee8b(0x20)
    0xa440x45e: v45ea44 = ISZERO v45ea43
    0xa460x45e: v45ea46 = ISZERO v45ea44
    0xa470x45e: v45ea47(0xa54) = CONST 
    0xa4a0x45e: JUMPI v45ea47(0xa54), v45ea46

    Begin block 0xa4b0x45e
    prev=[0xa400x45e], succ=[]
    =================================
    0xa4b0x45e: v45ea4b = RETURNDATASIZE 
    0xa4c0x45e: v45ea4c(0x0) = CONST 
    0xa4f0x45e: RETURNDATACOPY v45ea4c(0x0), v45ea4c(0x0), v45ea4b
    0xa500x45e: v45ea50 = RETURNDATASIZE 
    0xa510x45e: v45ea51(0x0) = CONST 
    0xa530x45e: REVERT v45ea51(0x0), v45ea50

    Begin block 0xa540x45e
    prev=[0xa400x45e], succ=[0xa660x45e, 0xa6a0x45e]
    =================================
    0xa590x45e: v45ea59(0x40) = CONST 
    0xa5b0x45e: v45ea5b = MLOAD v45ea59(0x40)
    0xa5c0x45e: v45ea5c = RETURNDATASIZE 
    0xa5d0x45e: v45ea5d(0x20) = CONST 
    0xa600x45e: v45ea60 = LT v45ea5c, v45ea5d(0x20)
    0xa610x45e: v45ea61 = ISZERO v45ea60
    0xa620x45e: v45ea62(0xa6a) = CONST 
    0xa650x45e: JUMPI v45ea62(0xa6a), v45ea61

    Begin block 0xa660x45e
    prev=[0xa540x45e], succ=[]
    =================================
    0xa660x45e: v45ea66(0x0) = CONST 
    0xa690x45e: REVERT v45ea66(0x0), v45ea66(0x0)

    Begin block 0xa6a0x45e
    prev=[0xa540x45e], succ=[0x22b2]
    =================================
    0xa6c0x45e: v45ea6c = MLOAD v45ea5b
    0xa710x45e: JUMP v45f(0x22b2)

    Begin block 0x22b2
    prev=[0xa6a0x45e], succ=[]
    =================================
    0x22b3: v22b3(0x40) = CONST 
    0x22b6: v22b6 = MLOAD v22b3(0x40)
    0x22b8: v22b8 = ISZERO v45ea6c
    0x22b9: v22b9 = ISZERO v22b8
    0x22bb: MSTORE v22b6, v22b9
    0x22bc: v22bc = MLOAD v22b3(0x40)
    0x22c0: v22c0(0x0) = SUB v22b6, v22bc
    0x22c1: v22c1(0x20) = CONST 
    0x22c3: v22c3(0x20) = ADD v22c1(0x20), v22c0(0x0)
    0x22c5: RETURN v22bc, v22c3(0x20)

}

function confirmOperatorsContract()() public {
    Begin block 0x484
    prev=[], succ=[0xea4B0x484]
    =================================
    0x485: v485(0x22e5) = CONST 
    0x488: v488(0xea4) = CONST 
    0x48b: JUMP v488(0xea4), v485(0x22e5)

    Begin block 0xea4B0x484
    prev=[0x484], succ=[0xeb5B0x484, 0xeebB0x484]
    =================================
    0xea5S0x484: vea5V484(0x34) = CONST 
    0xea7S0x484: vea7V484 = SLOAD vea5V484(0x34)
    0xea8S0x484: vea8V484(0x1) = CONST 
    0xeaaS0x484: veaaV484(0x1) = CONST 
    0xeacS0x484: veacV484(0xa0) = CONST 
    0xeaeS0x484: veaeV484(0x10000000000000000000000000000000000000000) = SHL veacV484(0xa0), veaaV484(0x1)
    0xeafS0x484: veafV484(0xffffffffffffffffffffffffffffffffffffffff) = SUB veaeV484(0x10000000000000000000000000000000000000000), vea8V484(0x1)
    0xeb0S0x484: veb0V484 = AND veafV484(0xffffffffffffffffffffffffffffffffffffffff), vea7V484
    0xeb1S0x484: veb1V484(0xeeb) = CONST 
    0xeb4S0x484: JUMPI veb1V484(0xeeb), veb0V484

    Begin block 0xeb5B0x484
    prev=[0xea4B0x484], succ=[]
    =================================
    0xeb5S0x484: veb5V484(0x40) = CONST 
    0xeb7S0x484: veb7V484 = MLOAD veb5V484(0x40)
    0xeb8S0x484: veb8V484(0x461bcd) = CONST 
    0xebcS0x484: vebcV484(0xe5) = CONST 
    0xebeS0x484: vebeV484(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vebcV484(0xe5), veb8V484(0x461bcd)
    0xec0S0x484: MSTORE veb7V484, vebeV484(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xec1S0x484: vec1V484(0x4) = CONST 
    0xec3S0x484: vec3V484 = ADD vec1V484(0x4), veb7V484
    0xec6S0x484: vec6V484(0x20) = CONST 
    0xec8S0x484: vec8V484 = ADD vec6V484(0x20), vec3V484
    0xecbS0x484: vecbV484(0x20) = SUB vec8V484, vec3V484
    0xecdS0x484: MSTORE vec3V484, vecbV484(0x20)
    0xeceS0x484: veceV484(0x3f) = CONST 
    0xed1S0x484: MSTORE vec8V484, veceV484(0x3f)
    0xed2S0x484: ved2V484(0x20) = CONST 
    0xed4S0x484: ved4V484 = ADD ved2V484(0x20), vec8V484
    0xed6S0x484: ved6V484(0x1cb4) = CONST 
    0xed9S0x484: ved9V484(0x3f) = CONST 
    0xedcS0x484: CODECOPY ved4V484, ved6V484(0x1cb4), ved9V484(0x3f)
    0xeddS0x484: veddV484(0x40) = CONST 
    0xedfS0x484: vedfV484 = ADD veddV484(0x40), ved4V484
    0xee3S0x484: vee3V484(0x40) = CONST 
    0xee5S0x484: vee5V484 = MLOAD vee3V484(0x40)
    0xee8S0x484: vee8V484(0x84) = SUB vedfV484, vee5V484
    0xeeaS0x484: REVERT vee5V484, vee8V484(0x84)

    Begin block 0xeebB0x484
    prev=[0xea4B0x484], succ=[0xefeB0x484, 0xf34B0x484]
    =================================
    0xeecS0x484: veecV484(0x34) = CONST 
    0xeeeS0x484: veeeV484 = SLOAD veecV484(0x34)
    0xeefS0x484: veefV484(0x1) = CONST 
    0xef1S0x484: vef1V484(0x1) = CONST 
    0xef3S0x484: vef3V484(0xa0) = CONST 
    0xef5S0x484: vef5V484(0x10000000000000000000000000000000000000000) = SHL vef3V484(0xa0), vef1V484(0x1)
    0xef6S0x484: vef6V484(0xffffffffffffffffffffffffffffffffffffffff) = SUB vef5V484(0x10000000000000000000000000000000000000000), veefV484(0x1)
    0xef7S0x484: vef7V484 = AND vef6V484(0xffffffffffffffffffffffffffffffffffffffff), veeeV484
    0xef8S0x484: vef8V484 = CALLER 
    0xef9S0x484: vef9V484 = EQ vef8V484, vef7V484
    0xefaS0x484: vefaV484(0xf34) = CONST 
    0xefdS0x484: JUMPI vefaV484(0xf34), vef9V484

    Begin block 0xefeB0x484
    prev=[0xeebB0x484], succ=[]
    =================================
    0xefeS0x484: vefeV484(0x40) = CONST 
    0xf00S0x484: vf00V484 = MLOAD vefeV484(0x40)
    0xf01S0x484: vf01V484(0x461bcd) = CONST 
    0xf05S0x484: vf05V484(0xe5) = CONST 
    0xf07S0x484: vf07V484(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf05V484(0xe5), vf01V484(0x461bcd)
    0xf09S0x484: MSTORE vf00V484, vf07V484(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf0aS0x484: vf0aV484(0x4) = CONST 
    0xf0cS0x484: vf0cV484 = ADD vf0aV484(0x4), vf00V484
    0xf0fS0x484: vf0fV484(0x20) = CONST 
    0xf11S0x484: vf11V484 = ADD vf0fV484(0x20), vf0cV484
    0xf14S0x484: vf14V484(0x20) = SUB vf11V484, vf0cV484
    0xf16S0x484: MSTORE vf0cV484, vf14V484(0x20)
    0xf17S0x484: vf17V484(0x3a) = CONST 
    0xf1aS0x484: MSTORE vf11V484, vf17V484(0x3a)
    0xf1bS0x484: vf1bV484(0x20) = CONST 
    0xf1dS0x484: vf1dV484 = ADD vf1bV484(0x20), vf11V484
    0xf1fS0x484: vf1fV484(0x1c2f) = CONST 
    0xf22S0x484: vf22V484(0x3a) = CONST 
    0xf25S0x484: CODECOPY vf1dV484, vf1fV484(0x1c2f), vf22V484(0x3a)
    0xf26S0x484: vf26V484(0x40) = CONST 
    0xf28S0x484: vf28V484 = ADD vf26V484(0x40), vf1dV484
    0xf2cS0x484: vf2cV484(0x40) = CONST 
    0xf2eS0x484: vf2eV484 = MLOAD vf2cV484(0x40)
    0xf31S0x484: vf31V484(0x84) = SUB vf28V484, vf2eV484
    0xf33S0x484: REVERT vf2eV484, vf31V484(0x84)

    Begin block 0xf34B0x484
    prev=[0xeebB0x484], succ=[0x1985B0xf34B0x484]
    =================================
    0xf35S0x484: vf35V484(0x34) = CONST 
    0xf37S0x484: vf37V484 = SLOAD vf35V484(0x34)
    0xf38S0x484: vf38V484(0x2499) = CONST 
    0xf3cS0x484: vf3cV484(0x1) = CONST 
    0xf3eS0x484: vf3eV484(0x1) = CONST 
    0xf40S0x484: vf40V484(0xa0) = CONST 
    0xf42S0x484: vf42V484(0x10000000000000000000000000000000000000000) = SHL vf40V484(0xa0), vf3eV484(0x1)
    0xf43S0x484: vf43V484(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf42V484(0x10000000000000000000000000000000000000000), vf3cV484(0x1)
    0xf44S0x484: vf44V484 = AND vf43V484(0xffffffffffffffffffffffffffffffffffffffff), vf37V484
    0xf45S0x484: vf45V484(0x1985) = CONST 
    0xf48S0x484: JUMP vf45V484(0x1985), vf44V484, vf38V484(0x2499)

    Begin block 0x1985B0xf34B0x484
    prev=[0xf34B0x484], succ=[0x1994B0xf34B0x484, 0x19caB0xf34B0x484]
    =================================
    0x1986S0xf34S0x484: v1986Vf34V484(0x1) = CONST 
    0x1988S0xf34S0x484: v1988Vf34V484(0x1) = CONST 
    0x198aS0xf34S0x484: v198aVf34V484(0xa0) = CONST 
    0x198cS0xf34S0x484: v198cVf34V484(0x10000000000000000000000000000000000000000) = SHL v198aVf34V484(0xa0), v1988Vf34V484(0x1)
    0x198dS0xf34S0x484: v198dVf34V484(0xffffffffffffffffffffffffffffffffffffffff) = SUB v198cVf34V484(0x10000000000000000000000000000000000000000), v1986Vf34V484(0x1)
    0x198fS0xf34S0x484: v198fVf34V484 = AND vf44V484, v198dVf34V484(0xffffffffffffffffffffffffffffffffffffffff)
    0x1990S0xf34S0x484: v1990Vf34V484(0x19ca) = CONST 
    0x1993S0xf34S0x484: JUMPI v1990Vf34V484(0x19ca), v198fVf34V484

    Begin block 0x1994B0xf34B0x484
    prev=[0x1985B0xf34B0x484], succ=[]
    =================================
    0x1994S0xf34S0x484: v1994Vf34V484(0x40) = CONST 
    0x1996S0xf34S0x484: v1996Vf34V484 = MLOAD v1994Vf34V484(0x40)
    0x1997S0xf34S0x484: v1997Vf34V484(0x461bcd) = CONST 
    0x199bS0xf34S0x484: v199bVf34V484(0xe5) = CONST 
    0x199dS0xf34S0x484: v199dVf34V484(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v199bVf34V484(0xe5), v1997Vf34V484(0x461bcd)
    0x199fS0xf34S0x484: MSTORE v1996Vf34V484, v199dVf34V484(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19a0S0xf34S0x484: v19a0Vf34V484(0x4) = CONST 
    0x19a2S0xf34S0x484: v19a2Vf34V484 = ADD v19a0Vf34V484(0x4), v1996Vf34V484
    0x19a5S0xf34S0x484: v19a5Vf34V484(0x20) = CONST 
    0x19a7S0xf34S0x484: v19a7Vf34V484 = ADD v19a5Vf34V484(0x20), v19a2Vf34V484
    0x19aaS0xf34S0x484: v19aaVf34V484(0x20) = SUB v19a7Vf34V484, v19a2Vf34V484
    0x19acS0xf34S0x484: MSTORE v19a2Vf34V484, v19aaVf34V484(0x20)
    0x19adS0xf34S0x484: v19adVf34V484(0x3e) = CONST 
    0x19b0S0xf34S0x484: MSTORE v19a7Vf34V484, v19adVf34V484(0x3e)
    0x19b1S0xf34S0x484: v19b1Vf34V484(0x20) = CONST 
    0x19b3S0xf34S0x484: v19b3Vf34V484 = ADD v19b1Vf34V484(0x20), v19a7Vf34V484
    0x19b5S0xf34S0x484: v19b5Vf34V484(0x1b27) = CONST 
    0x19b8S0xf34S0x484: v19b8Vf34V484(0x3e) = CONST 
    0x19bbS0xf34S0x484: CODECOPY v19b3Vf34V484, v19b5Vf34V484(0x1b27), v19b8Vf34V484(0x3e)
    0x19bcS0xf34S0x484: v19bcVf34V484(0x40) = CONST 
    0x19beS0xf34S0x484: v19beVf34V484 = ADD v19bcVf34V484(0x40), v19b3Vf34V484
    0x19c2S0xf34S0x484: v19c2Vf34V484(0x40) = CONST 
    0x19c4S0xf34S0x484: v19c4Vf34V484 = MLOAD v19c2Vf34V484(0x40)
    0x19c7S0xf34S0x484: v19c7Vf34V484(0x84) = SUB v19beVf34V484, v19c4Vf34V484
    0x19c9S0xf34S0x484: REVERT v19c4Vf34V484, v19c7Vf34V484(0x84)

    Begin block 0x19caB0xf34B0x484
    prev=[0x1985B0xf34B0x484], succ=[0x2499B0x484]
    =================================
    0x19cbS0xf34S0x484: v19cbVf34V484(0x33) = CONST 
    0x19ceS0xf34S0x484: v19ceVf34V484 = SLOAD v19cbVf34V484(0x33)
    0x19cfS0xf34S0x484: v19cfVf34V484(0x1) = CONST 
    0x19d1S0xf34S0x484: v19d1Vf34V484(0x1) = CONST 
    0x19d3S0xf34S0x484: v19d3Vf34V484(0xa0) = CONST 
    0x19d5S0xf34S0x484: v19d5Vf34V484(0x10000000000000000000000000000000000000000) = SHL v19d3Vf34V484(0xa0), v19d1Vf34V484(0x1)
    0x19d6S0xf34S0x484: v19d6Vf34V484(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19d5Vf34V484(0x10000000000000000000000000000000000000000), v19cfVf34V484(0x1)
    0x19d7S0xf34S0x484: v19d7Vf34V484(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v19d6Vf34V484(0xffffffffffffffffffffffffffffffffffffffff)
    0x19d8S0xf34S0x484: v19d8Vf34V484 = AND v19d7Vf34V484(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v19ceVf34V484
    0x19d9S0xf34S0x484: v19d9Vf34V484(0x1) = CONST 
    0x19dbS0xf34S0x484: v19dbVf34V484(0x1) = CONST 
    0x19ddS0xf34S0x484: v19ddVf34V484(0xa0) = CONST 
    0x19dfS0xf34S0x484: v19dfVf34V484(0x10000000000000000000000000000000000000000) = SHL v19ddVf34V484(0xa0), v19dbVf34V484(0x1)
    0x19e0S0xf34S0x484: v19e0Vf34V484(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19dfVf34V484(0x10000000000000000000000000000000000000000), v19d9Vf34V484(0x1)
    0x19e2S0xf34S0x484: v19e2Vf34V484 = AND vf44V484, v19e0Vf34V484(0xffffffffffffffffffffffffffffffffffffffff)
    0x19e5S0xf34S0x484: v19e5Vf34V484 = OR v19e2Vf34V484, v19d8Vf34V484
    0x19e8S0xf34S0x484: SSTORE v19cbVf34V484(0x33), v19e5Vf34V484
    0x19e9S0xf34S0x484: v19e9Vf34V484(0x40) = CONST 
    0x19ebS0xf34S0x484: v19ebVf34V484 = MLOAD v19e9Vf34V484(0x40)
    0x19ecS0xf34S0x484: v19ecVf34V484 = CALLER 
    0x19eeS0xf34S0x484: v19eeVf34V484(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e) = CONST 
    0x1a10S0xf34S0x484: v1a10Vf34V484(0x0) = CONST 
    0x1a13S0xf34S0x484: LOG3 v19ebVf34V484, v1a10Vf34V484(0x0), v19eeVf34V484(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e), v19ecVf34V484, v19e2Vf34V484
    0x1a15S0xf34S0x484: JUMP vf38V484(0x2499)

    Begin block 0x2499B0x484
    prev=[0x19caB0xf34B0x484], succ=[0x22e5]
    =================================
    0x249aS0x484: JUMP v485(0x22e5)

    Begin block 0x22e5
    prev=[0x2499B0x484], succ=[]
    =================================
    0x22e6: STOP 

}

function isIssuer(address)() public {
    Begin block 0x48c
    prev=[], succ=[0x49e, 0x4a2]
    =================================
    0x48d: v48d(0x2306) = CONST 
    0x490: v490(0x4) = CONST 
    0x493: v493 = CALLDATASIZE 
    0x494: v494 = SUB v493, v490(0x4)
    0x495: v495(0x20) = CONST 
    0x498: v498 = LT v494, v495(0x20)
    0x499: v499 = ISZERO v498
    0x49a: v49a(0x4a2) = CONST 
    0x49d: JUMPI v49a(0x4a2), v499

    Begin block 0x49e
    prev=[0x48c], succ=[]
    =================================
    0x49e: v49e(0x0) = CONST 
    0x4a1: REVERT v49e(0x0), v49e(0x0)

    Begin block 0x4a2
    prev=[0x48c], succ=[0xf4b0x48c]
    =================================
    0x4a4: v4a4 = CALLDATALOAD v490(0x4)
    0x4a5: v4a5(0x1) = CONST 
    0x4a7: v4a7(0x1) = CONST 
    0x4a9: v4a9(0xa0) = CONST 
    0x4ab: v4ab(0x10000000000000000000000000000000000000000) = SHL v4a9(0xa0), v4a7(0x1)
    0x4ac: v4ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ab(0x10000000000000000000000000000000000000000), v4a5(0x1)
    0x4ad: v4ad = AND v4ac(0xffffffffffffffffffffffffffffffffffffffff), v4a4
    0x4ae: v4ae(0xf4b) = CONST 
    0x4b1: JUMP v4ae(0xf4b)

    Begin block 0xf4b0x48c
    prev=[0x4a2], succ=[0xf980x48c, 0xa400x48c]
    =================================
    0xf4c0x48c: v48cf4c(0x35) = CONST 
    0xf4e0x48c: v48cf4e = SLOAD v48cf4c(0x35)
    0xf4f0x48c: v48cf4f(0x40) = CONST 
    0xf520x48c: v48cf52 = MLOAD v48cf4f(0x40)
    0xf530x48c: v48cf53(0x877b9a67) = CONST 
    0xf580x48c: v48cf58(0xe0) = CONST 
    0xf5a0x48c: v48cf5a(0x877b9a6700000000000000000000000000000000000000000000000000000000) = SHL v48cf58(0xe0), v48cf53(0x877b9a67)
    0xf5c0x48c: MSTORE v48cf52, v48cf5a(0x877b9a6700000000000000000000000000000000000000000000000000000000)
    0xf5d0x48c: v48cf5d(0x1) = CONST 
    0xf5f0x48c: v48cf5f(0x1) = CONST 
    0xf610x48c: v48cf61(0xa0) = CONST 
    0xf630x48c: v48cf63(0x10000000000000000000000000000000000000000) = SHL v48cf61(0xa0), v48cf5f(0x1)
    0xf640x48c: v48cf64(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48cf63(0x10000000000000000000000000000000000000000), v48cf5d(0x1)
    0xf670x48c: v48cf67 = AND v48cf64(0xffffffffffffffffffffffffffffffffffffffff), v4ad
    0xf680x48c: v48cf68(0x4) = CONST 
    0xf6b0x48c: v48cf6b = ADD v48cf52, v48cf68(0x4)
    0xf6c0x48c: MSTORE v48cf6b, v48cf67
    0xf6e0x48c: v48cf6e = MLOAD v48cf4f(0x40)
    0xf6f0x48c: v48cf6f(0x0) = CONST 
    0xf750x48c: v48cf75 = AND v48cf4e, v48cf64(0xffffffffffffffffffffffffffffffffffffffff)
    0xf770x48c: v48cf77(0x877b9a67) = CONST 
    0xf7d0x48c: v48cf7d(0x24) = CONST 
    0xf810x48c: v48cf81 = ADD v48cf52, v48cf7d(0x24)
    0xf830x48c: v48cf83(0x20) = CONST 
    0xf8b0x48c: v48cf8b(0x0) = SUB v48cf52, v48cf6e
    0xf8c0x48c: v48cf8c(0x24) = ADD v48cf8b(0x0), v48cf7d(0x24)
    0xf900x48c: v48cf90 = EXTCODESIZE v48cf75
    0xf910x48c: v48cf91 = ISZERO v48cf90
    0xf930x48c: v48cf93 = ISZERO v48cf91
    0xf940x48c: v48cf94(0xa40) = CONST 
    0xf970x48c: JUMPI v48cf94(0xa40), v48cf93

    Begin block 0xf980x48c
    prev=[0xf4b0x48c], succ=[]
    =================================
    0xf980x48c: v48cf98(0x0) = CONST 
    0xf9b0x48c: REVERT v48cf98(0x0), v48cf98(0x0)

    Begin block 0xa400x48c
    prev=[0xf4b0x48c], succ=[0xa4b0x48c, 0xa540x48c]
    =================================
    0xa420x48c: v48ca42 = GAS 
    0xa430x48c: v48ca43 = STATICCALL v48ca42, v48cf75, v48cf6e, v48cf8c(0x24), v48cf6e, v48cf83(0x20)
    0xa440x48c: v48ca44 = ISZERO v48ca43
    0xa460x48c: v48ca46 = ISZERO v48ca44
    0xa470x48c: v48ca47(0xa54) = CONST 
    0xa4a0x48c: JUMPI v48ca47(0xa54), v48ca46

    Begin block 0xa4b0x48c
    prev=[0xa400x48c], succ=[]
    =================================
    0xa4b0x48c: v48ca4b = RETURNDATASIZE 
    0xa4c0x48c: v48ca4c(0x0) = CONST 
    0xa4f0x48c: RETURNDATACOPY v48ca4c(0x0), v48ca4c(0x0), v48ca4b
    0xa500x48c: v48ca50 = RETURNDATASIZE 
    0xa510x48c: v48ca51(0x0) = CONST 
    0xa530x48c: REVERT v48ca51(0x0), v48ca50

    Begin block 0xa540x48c
    prev=[0xa400x48c], succ=[0xa660x48c, 0xa6a0x48c]
    =================================
    0xa590x48c: v48ca59(0x40) = CONST 
    0xa5b0x48c: v48ca5b = MLOAD v48ca59(0x40)
    0xa5c0x48c: v48ca5c = RETURNDATASIZE 
    0xa5d0x48c: v48ca5d(0x20) = CONST 
    0xa600x48c: v48ca60 = LT v48ca5c, v48ca5d(0x20)
    0xa610x48c: v48ca61 = ISZERO v48ca60
    0xa620x48c: v48ca62(0xa6a) = CONST 
    0xa650x48c: JUMPI v48ca62(0xa6a), v48ca61

    Begin block 0xa660x48c
    prev=[0xa540x48c], succ=[]
    =================================
    0xa660x48c: v48ca66(0x0) = CONST 
    0xa690x48c: REVERT v48ca66(0x0), v48ca66(0x0)

    Begin block 0xa6a0x48c
    prev=[0xa540x48c], succ=[0x2306]
    =================================
    0xa6c0x48c: v48ca6c = MLOAD v48ca5b
    0xa710x48c: JUMP v48d(0x2306)

    Begin block 0x2306
    prev=[0xa6a0x48c], succ=[]
    =================================
    0x2307: v2307(0x40) = CONST 
    0x230a: v230a = MLOAD v2307(0x40)
    0x230c: v230c = ISZERO v48ca6c
    0x230d: v230d = ISZERO v230c
    0x230f: MSTORE v230a, v230d
    0x2310: v2310 = MLOAD v2307(0x40)
    0x2314: v2314(0x0) = SUB v230a, v2310
    0x2315: v2315(0x20) = CONST 
    0x2317: v2317(0x20) = ADD v2315(0x20), v2314(0x0)
    0x2319: RETURN v2310, v2317(0x20)

}

function confirmRaiseOperatorsContract()() public {
    Begin block 0x4b2
    prev=[], succ=[0xf9cB0x4b2]
    =================================
    0x4b3: v4b3(0x2339) = CONST 
    0x4b6: v4b6(0xf9c) = CONST 
    0x4b9: JUMP v4b6(0xf9c), v4b3(0x2339)

    Begin block 0xf9cB0x4b2
    prev=[0x4b2], succ=[0xfadB0x4b2, 0xfe3B0x4b2]
    =================================
    0xf9dS0x4b2: vf9dV4b2(0x36) = CONST 
    0xf9fS0x4b2: vf9fV4b2 = SLOAD vf9dV4b2(0x36)
    0xfa0S0x4b2: vfa0V4b2(0x1) = CONST 
    0xfa2S0x4b2: vfa2V4b2(0x1) = CONST 
    0xfa4S0x4b2: vfa4V4b2(0xa0) = CONST 
    0xfa6S0x4b2: vfa6V4b2(0x10000000000000000000000000000000000000000) = SHL vfa4V4b2(0xa0), vfa2V4b2(0x1)
    0xfa7S0x4b2: vfa7V4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfa6V4b2(0x10000000000000000000000000000000000000000), vfa0V4b2(0x1)
    0xfa8S0x4b2: vfa8V4b2 = AND vfa7V4b2(0xffffffffffffffffffffffffffffffffffffffff), vf9fV4b2
    0xfa9S0x4b2: vfa9V4b2(0xfe3) = CONST 
    0xfacS0x4b2: JUMPI vfa9V4b2(0xfe3), vfa8V4b2

    Begin block 0xfadB0x4b2
    prev=[0xf9cB0x4b2], succ=[]
    =================================
    0xfadS0x4b2: vfadV4b2(0x40) = CONST 
    0xfafS0x4b2: vfafV4b2 = MLOAD vfadV4b2(0x40)
    0xfb0S0x4b2: vfb0V4b2(0x461bcd) = CONST 
    0xfb4S0x4b2: vfb4V4b2(0xe5) = CONST 
    0xfb6S0x4b2: vfb6V4b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vfb4V4b2(0xe5), vfb0V4b2(0x461bcd)
    0xfb8S0x4b2: MSTORE vfafV4b2, vfb6V4b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xfb9S0x4b2: vfb9V4b2(0x4) = CONST 
    0xfbbS0x4b2: vfbbV4b2 = ADD vfb9V4b2(0x4), vfafV4b2
    0xfbeS0x4b2: vfbeV4b2(0x20) = CONST 
    0xfc0S0x4b2: vfc0V4b2 = ADD vfbeV4b2(0x20), vfbbV4b2
    0xfc3S0x4b2: vfc3V4b2(0x20) = SUB vfc0V4b2, vfbbV4b2
    0xfc5S0x4b2: MSTORE vfbbV4b2, vfc3V4b2(0x20)
    0xfc6S0x4b2: vfc6V4b2(0x4d) = CONST 
    0xfc9S0x4b2: MSTORE vfc0V4b2, vfc6V4b2(0x4d)
    0xfcaS0x4b2: vfcaV4b2(0x20) = CONST 
    0xfccS0x4b2: vfccV4b2 = ADD vfcaV4b2(0x20), vfc0V4b2
    0xfceS0x4b2: vfceV4b2(0x1a17) = CONST 
    0xfd1S0x4b2: vfd1V4b2(0x4d) = CONST 
    0xfd4S0x4b2: CODECOPY vfccV4b2, vfceV4b2(0x1a17), vfd1V4b2(0x4d)
    0xfd5S0x4b2: vfd5V4b2(0x60) = CONST 
    0xfd7S0x4b2: vfd7V4b2 = ADD vfd5V4b2(0x60), vfccV4b2
    0xfdbS0x4b2: vfdbV4b2(0x40) = CONST 
    0xfddS0x4b2: vfddV4b2 = MLOAD vfdbV4b2(0x40)
    0xfe0S0x4b2: vfe0V4b2(0xa4) = SUB vfd7V4b2, vfddV4b2
    0xfe2S0x4b2: REVERT vfddV4b2, vfe0V4b2(0xa4)

    Begin block 0xfe3B0x4b2
    prev=[0xf9cB0x4b2], succ=[0xff6B0x4b2, 0x102cB0x4b2]
    =================================
    0xfe4S0x4b2: vfe4V4b2(0x36) = CONST 
    0xfe6S0x4b2: vfe6V4b2 = SLOAD vfe4V4b2(0x36)
    0xfe7S0x4b2: vfe7V4b2(0x1) = CONST 
    0xfe9S0x4b2: vfe9V4b2(0x1) = CONST 
    0xfebS0x4b2: vfebV4b2(0xa0) = CONST 
    0xfedS0x4b2: vfedV4b2(0x10000000000000000000000000000000000000000) = SHL vfebV4b2(0xa0), vfe9V4b2(0x1)
    0xfeeS0x4b2: vfeeV4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfedV4b2(0x10000000000000000000000000000000000000000), vfe7V4b2(0x1)
    0xfefS0x4b2: vfefV4b2 = AND vfeeV4b2(0xffffffffffffffffffffffffffffffffffffffff), vfe6V4b2
    0xff0S0x4b2: vff0V4b2 = CALLER 
    0xff1S0x4b2: vff1V4b2 = EQ vff0V4b2, vfefV4b2
    0xff2S0x4b2: vff2V4b2(0x102c) = CONST 
    0xff5S0x4b2: JUMPI vff2V4b2(0x102c), vff1V4b2

    Begin block 0xff6B0x4b2
    prev=[0xfe3B0x4b2], succ=[]
    =================================
    0xff6S0x4b2: vff6V4b2(0x40) = CONST 
    0xff8S0x4b2: vff8V4b2 = MLOAD vff6V4b2(0x40)
    0xff9S0x4b2: vff9V4b2(0x461bcd) = CONST 
    0xffdS0x4b2: vffdV4b2(0xe5) = CONST 
    0xfffS0x4b2: vfffV4b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vffdV4b2(0xe5), vff9V4b2(0x461bcd)
    0x1001S0x4b2: MSTORE vff8V4b2, vfffV4b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1002S0x4b2: v1002V4b2(0x4) = CONST 
    0x1004S0x4b2: v1004V4b2 = ADD v1002V4b2(0x4), vff8V4b2
    0x1007S0x4b2: v1007V4b2(0x20) = CONST 
    0x1009S0x4b2: v1009V4b2 = ADD v1007V4b2(0x20), v1004V4b2
    0x100cS0x4b2: v100cV4b2(0x20) = SUB v1009V4b2, v1004V4b2
    0x100eS0x4b2: MSTORE v1004V4b2, v100cV4b2(0x20)
    0x100fS0x4b2: v100fV4b2(0x44) = CONST 
    0x1012S0x4b2: MSTORE v1009V4b2, v100fV4b2(0x44)
    0x1013S0x4b2: v1013V4b2(0x20) = CONST 
    0x1015S0x4b2: v1015V4b2 = ADD v1013V4b2(0x20), v1009V4b2
    0x1017S0x4b2: v1017V4b2(0x1b96) = CONST 
    0x101aS0x4b2: v101aV4b2(0x44) = CONST 
    0x101dS0x4b2: CODECOPY v1015V4b2, v1017V4b2(0x1b96), v101aV4b2(0x44)
    0x101eS0x4b2: v101eV4b2(0x60) = CONST 
    0x1020S0x4b2: v1020V4b2 = ADD v101eV4b2(0x60), v1015V4b2
    0x1024S0x4b2: v1024V4b2(0x40) = CONST 
    0x1026S0x4b2: v1026V4b2 = MLOAD v1024V4b2(0x40)
    0x1029S0x4b2: v1029V4b2(0xa4) = SUB v1020V4b2, v1026V4b2
    0x102bS0x4b2: REVERT v1026V4b2, v1029V4b2(0xa4)

    Begin block 0x102cB0x4b2
    prev=[0xfe3B0x4b2], succ=[0x18f4B0x102cB0x4b2]
    =================================
    0x102dS0x4b2: v102dV4b2(0x36) = CONST 
    0x102fS0x4b2: v102fV4b2 = SLOAD v102dV4b2(0x36)
    0x1030S0x4b2: v1030V4b2(0x24ba) = CONST 
    0x1034S0x4b2: v1034V4b2(0x1) = CONST 
    0x1036S0x4b2: v1036V4b2(0x1) = CONST 
    0x1038S0x4b2: v1038V4b2(0xa0) = CONST 
    0x103aS0x4b2: v103aV4b2(0x10000000000000000000000000000000000000000) = SHL v1038V4b2(0xa0), v1036V4b2(0x1)
    0x103bS0x4b2: v103bV4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v103aV4b2(0x10000000000000000000000000000000000000000), v1034V4b2(0x1)
    0x103cS0x4b2: v103cV4b2 = AND v103bV4b2(0xffffffffffffffffffffffffffffffffffffffff), v102fV4b2
    0x103dS0x4b2: v103dV4b2(0x18f4) = CONST 
    0x1040S0x4b2: JUMP v103dV4b2(0x18f4), v103cV4b2, v1030V4b2(0x24ba)

    Begin block 0x18f4B0x102cB0x4b2
    prev=[0x102cB0x4b2], succ=[0x1903B0x102cB0x4b2, 0x1939B0x102cB0x4b2]
    =================================
    0x18f5S0x102cS0x4b2: v18f5V102cV4b2(0x1) = CONST 
    0x18f7S0x102cS0x4b2: v18f7V102cV4b2(0x1) = CONST 
    0x18f9S0x102cS0x4b2: v18f9V102cV4b2(0xa0) = CONST 
    0x18fbS0x102cS0x4b2: v18fbV102cV4b2(0x10000000000000000000000000000000000000000) = SHL v18f9V102cV4b2(0xa0), v18f7V102cV4b2(0x1)
    0x18fcS0x102cS0x4b2: v18fcV102cV4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18fbV102cV4b2(0x10000000000000000000000000000000000000000), v18f5V102cV4b2(0x1)
    0x18feS0x102cS0x4b2: v18feV102cV4b2 = AND v103cV4b2, v18fcV102cV4b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x18ffS0x102cS0x4b2: v18ffV102cV4b2(0x1939) = CONST 
    0x1902S0x102cS0x4b2: JUMPI v18ffV102cV4b2(0x1939), v18feV102cV4b2

    Begin block 0x1903B0x102cB0x4b2
    prev=[0x18f4B0x102cB0x4b2], succ=[]
    =================================
    0x1903S0x102cS0x4b2: v1903V102cV4b2(0x40) = CONST 
    0x1905S0x102cS0x4b2: v1905V102cV4b2 = MLOAD v1903V102cV4b2(0x40)
    0x1906S0x102cS0x4b2: v1906V102cV4b2(0x461bcd) = CONST 
    0x190aS0x102cS0x4b2: v190aV102cV4b2(0xe5) = CONST 
    0x190cS0x102cS0x4b2: v190cV102cV4b2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v190aV102cV4b2(0xe5), v1906V102cV4b2(0x461bcd)
    0x190eS0x102cS0x4b2: MSTORE v1905V102cV4b2, v190cV102cV4b2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x190fS0x102cS0x4b2: v190fV102cV4b2(0x4) = CONST 
    0x1911S0x102cS0x4b2: v1911V102cV4b2 = ADD v190fV102cV4b2(0x4), v1905V102cV4b2
    0x1914S0x102cS0x4b2: v1914V102cV4b2(0x20) = CONST 
    0x1916S0x102cS0x4b2: v1916V102cV4b2 = ADD v1914V102cV4b2(0x20), v1911V102cV4b2
    0x1919S0x102cS0x4b2: v1919V102cV4b2(0x20) = SUB v1916V102cV4b2, v1911V102cV4b2
    0x191bS0x102cS0x4b2: MSTORE v1911V102cV4b2, v1919V102cV4b2(0x20)
    0x191cS0x102cS0x4b2: v191cV102cV4b2(0x49) = CONST 
    0x191fS0x102cS0x4b2: MSTORE v1916V102cV4b2, v191cV102cV4b2(0x49)
    0x1920S0x102cS0x4b2: v1920V102cV4b2(0x20) = CONST 
    0x1922S0x102cS0x4b2: v1922V102cV4b2 = ADD v1920V102cV4b2(0x20), v1916V102cV4b2
    0x1924S0x102cS0x4b2: v1924V102cV4b2(0x1aa3) = CONST 
    0x1927S0x102cS0x4b2: v1927V102cV4b2(0x49) = CONST 
    0x192aS0x102cS0x4b2: CODECOPY v1922V102cV4b2, v1924V102cV4b2(0x1aa3), v1927V102cV4b2(0x49)
    0x192bS0x102cS0x4b2: v192bV102cV4b2(0x60) = CONST 
    0x192dS0x102cS0x4b2: v192dV102cV4b2 = ADD v192bV102cV4b2(0x60), v1922V102cV4b2
    0x1931S0x102cS0x4b2: v1931V102cV4b2(0x40) = CONST 
    0x1933S0x102cS0x4b2: v1933V102cV4b2 = MLOAD v1931V102cV4b2(0x40)
    0x1936S0x102cS0x4b2: v1936V102cV4b2(0xa4) = SUB v192dV102cV4b2, v1933V102cV4b2
    0x1938S0x102cS0x4b2: REVERT v1933V102cV4b2, v1936V102cV4b2(0xa4)

    Begin block 0x1939B0x102cB0x4b2
    prev=[0x18f4B0x102cB0x4b2], succ=[0x24baB0x4b2]
    =================================
    0x193aS0x102cS0x4b2: v193aV102cV4b2(0x35) = CONST 
    0x193dS0x102cS0x4b2: v193dV102cV4b2 = SLOAD v193aV102cV4b2(0x35)
    0x193eS0x102cS0x4b2: v193eV102cV4b2(0x1) = CONST 
    0x1940S0x102cS0x4b2: v1940V102cV4b2(0x1) = CONST 
    0x1942S0x102cS0x4b2: v1942V102cV4b2(0xa0) = CONST 
    0x1944S0x102cS0x4b2: v1944V102cV4b2(0x10000000000000000000000000000000000000000) = SHL v1942V102cV4b2(0xa0), v1940V102cV4b2(0x1)
    0x1945S0x102cS0x4b2: v1945V102cV4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1944V102cV4b2(0x10000000000000000000000000000000000000000), v193eV102cV4b2(0x1)
    0x1946S0x102cS0x4b2: v1946V102cV4b2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1945V102cV4b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x1947S0x102cS0x4b2: v1947V102cV4b2 = AND v1946V102cV4b2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v193dV102cV4b2
    0x1948S0x102cS0x4b2: v1948V102cV4b2(0x1) = CONST 
    0x194aS0x102cS0x4b2: v194aV102cV4b2(0x1) = CONST 
    0x194cS0x102cS0x4b2: v194cV102cV4b2(0xa0) = CONST 
    0x194eS0x102cS0x4b2: v194eV102cV4b2(0x10000000000000000000000000000000000000000) = SHL v194cV102cV4b2(0xa0), v194aV102cV4b2(0x1)
    0x194fS0x102cS0x4b2: v194fV102cV4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v194eV102cV4b2(0x10000000000000000000000000000000000000000), v1948V102cV4b2(0x1)
    0x1951S0x102cS0x4b2: v1951V102cV4b2 = AND v103cV4b2, v194fV102cV4b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x1954S0x102cS0x4b2: v1954V102cV4b2 = OR v1951V102cV4b2, v1947V102cV4b2
    0x1957S0x102cS0x4b2: SSTORE v193aV102cV4b2(0x35), v1954V102cV4b2
    0x1958S0x102cS0x4b2: v1958V102cV4b2(0x40) = CONST 
    0x195aS0x102cS0x4b2: v195aV102cV4b2 = MLOAD v1958V102cV4b2(0x40)
    0x195bS0x102cS0x4b2: v195bV102cV4b2 = CALLER 
    0x195dS0x102cS0x4b2: v195dV102cV4b2(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c) = CONST 
    0x197fS0x102cS0x4b2: v197fV102cV4b2(0x0) = CONST 
    0x1982S0x102cS0x4b2: LOG3 v195aV102cV4b2, v197fV102cV4b2(0x0), v195dV102cV4b2(0x21e27c3f8de384977920f143c7a66b44be415d61d5e112bd124cd45a5151ec7c), v195bV102cV4b2, v1951V102cV4b2
    0x1984S0x102cS0x4b2: JUMP v1030V4b2(0x24ba)

    Begin block 0x24baB0x4b2
    prev=[0x1939B0x102cB0x4b2], succ=[0x2339]
    =================================
    0x24bbS0x4b2: JUMP v4b3(0x2339)

    Begin block 0x2339
    prev=[0x24baB0x4b2], succ=[]
    =================================
    0x233a: STOP 

}

function setRaiseOperatorsContract(address)() public {
    Begin block 0x4ba
    prev=[], succ=[0x4cc, 0x4d0]
    =================================
    0x4bb: v4bb(0x235a) = CONST 
    0x4be: v4be(0x4) = CONST 
    0x4c1: v4c1 = CALLDATASIZE 
    0x4c2: v4c2 = SUB v4c1, v4be(0x4)
    0x4c3: v4c3(0x20) = CONST 
    0x4c6: v4c6 = LT v4c2, v4c3(0x20)
    0x4c7: v4c7 = ISZERO v4c6
    0x4c8: v4c8(0x4d0) = CONST 
    0x4cb: JUMPI v4c8(0x4d0), v4c7

    Begin block 0x4cc
    prev=[0x4ba], succ=[]
    =================================
    0x4cc: v4cc(0x0) = CONST 
    0x4cf: REVERT v4cc(0x0), v4cc(0x0)

    Begin block 0x4d0
    prev=[0x4ba], succ=[0x1041]
    =================================
    0x4d2: v4d2 = CALLDATALOAD v4be(0x4)
    0x4d3: v4d3(0x1) = CONST 
    0x4d5: v4d5(0x1) = CONST 
    0x4d7: v4d7(0xa0) = CONST 
    0x4d9: v4d9(0x10000000000000000000000000000000000000000) = SHL v4d7(0xa0), v4d5(0x1)
    0x4da: v4da(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d9(0x10000000000000000000000000000000000000000), v4d3(0x1)
    0x4db: v4db = AND v4da(0xffffffffffffffffffffffffffffffffffffffff), v4d2
    0x4dc: v4dc(0x1041) = CONST 
    0x4df: JUMP v4dc(0x1041)

    Begin block 0x1041
    prev=[0x4d0], succ=[0x104a]
    =================================
    0x1042: v1042(0x104a) = CONST 
    0x1045: v1045 = CALLER 
    0x1046: v1046(0x9ef) = CONST 
    0x1049: v1049_0 = CALLPRIVATE v1046(0x9ef), v1045, v1042(0x104a)

    Begin block 0x104a
    prev=[0x1041], succ=[0x104f, 0x1085]
    =================================
    0x104b: v104b(0x1085) = CONST 
    0x104e: JUMPI v104b(0x1085), v1049_0

    Begin block 0x104f
    prev=[0x104a], succ=[]
    =================================
    0x104f: v104f(0x40) = CONST 
    0x1051: v1051 = MLOAD v104f(0x40)
    0x1052: v1052(0x461bcd) = CONST 
    0x1056: v1056(0xe5) = CONST 
    0x1058: v1058(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1056(0xe5), v1052(0x461bcd)
    0x105a: MSTORE v1051, v1058(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x105b: v105b(0x4) = CONST 
    0x105d: v105d = ADD v105b(0x4), v1051
    0x1060: v1060(0x20) = CONST 
    0x1062: v1062 = ADD v1060(0x20), v105d
    0x1065: v1065(0x20) = SUB v1062, v105d
    0x1067: MSTORE v105d, v1065(0x20)
    0x1068: v1068(0x31) = CONST 
    0x106b: MSTORE v1062, v1068(0x31)
    0x106c: v106c(0x20) = CONST 
    0x106e: v106e = ADD v106c(0x20), v1062
    0x1070: v1070(0x1b65) = CONST 
    0x1073: v1073(0x31) = CONST 
    0x1076: CODECOPY v106e, v1070(0x1b65), v1073(0x31)
    0x1077: v1077(0x40) = CONST 
    0x1079: v1079 = ADD v1077(0x40), v106e
    0x107d: v107d(0x40) = CONST 
    0x107f: v107f = MLOAD v107d(0x40)
    0x1082: v1082(0x84) = SUB v1079, v107f
    0x1084: REVERT v107f, v1082(0x84)

    Begin block 0x1085
    prev=[0x104a], succ=[0x1094, 0x10ca]
    =================================
    0x1086: v1086(0x1) = CONST 
    0x1088: v1088(0x1) = CONST 
    0x108a: v108a(0xa0) = CONST 
    0x108c: v108c(0x10000000000000000000000000000000000000000) = SHL v108a(0xa0), v1088(0x1)
    0x108d: v108d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v108c(0x10000000000000000000000000000000000000000), v1086(0x1)
    0x108f: v108f = AND v4db, v108d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1090: v1090(0x10ca) = CONST 
    0x1093: JUMPI v1090(0x10ca), v108f

    Begin block 0x1094
    prev=[0x1085], succ=[]
    =================================
    0x1094: v1094(0x40) = CONST 
    0x1096: v1096 = MLOAD v1094(0x40)
    0x1097: v1097(0x461bcd) = CONST 
    0x109b: v109b(0xe5) = CONST 
    0x109d: v109d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v109b(0xe5), v1097(0x461bcd)
    0x109f: MSTORE v1096, v109d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10a0: v10a0(0x4) = CONST 
    0x10a2: v10a2 = ADD v10a0(0x4), v1096
    0x10a5: v10a5(0x20) = CONST 
    0x10a7: v10a7 = ADD v10a5(0x20), v10a2
    0x10aa: v10aa(0x20) = SUB v10a7, v10a2
    0x10ac: MSTORE v10a2, v10aa(0x20)
    0x10ad: v10ad(0x49) = CONST 
    0x10b0: MSTORE v10a7, v10ad(0x49)
    0x10b1: v10b1(0x20) = CONST 
    0x10b3: v10b3 = ADD v10b1(0x20), v10a7
    0x10b5: v10b5(0x1aa3) = CONST 
    0x10b8: v10b8(0x49) = CONST 
    0x10bb: CODECOPY v10b3, v10b5(0x1aa3), v10b8(0x49)
    0x10bc: v10bc(0x60) = CONST 
    0x10be: v10be = ADD v10bc(0x60), v10b3
    0x10c2: v10c2(0x40) = CONST 
    0x10c4: v10c4 = MLOAD v10c2(0x40)
    0x10c7: v10c7(0xa4) = SUB v10be, v10c4
    0x10c9: REVERT v10c4, v10c7(0xa4)

    Begin block 0x10ca
    prev=[0x1085], succ=[0x235a]
    =================================
    0x10cb: v10cb(0x36) = CONST 
    0x10ce: v10ce = SLOAD v10cb(0x36)
    0x10cf: v10cf(0x1) = CONST 
    0x10d1: v10d1(0x1) = CONST 
    0x10d3: v10d3(0xa0) = CONST 
    0x10d5: v10d5(0x10000000000000000000000000000000000000000) = SHL v10d3(0xa0), v10d1(0x1)
    0x10d6: v10d6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10d5(0x10000000000000000000000000000000000000000), v10cf(0x1)
    0x10d7: v10d7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v10d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x10d8: v10d8 = AND v10d7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v10ce
    0x10d9: v10d9(0x1) = CONST 
    0x10db: v10db(0x1) = CONST 
    0x10dd: v10dd(0xa0) = CONST 
    0x10df: v10df(0x10000000000000000000000000000000000000000) = SHL v10dd(0xa0), v10db(0x1)
    0x10e0: v10e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10df(0x10000000000000000000000000000000000000000), v10d9(0x1)
    0x10e2: v10e2 = AND v4db, v10e0(0xffffffffffffffffffffffffffffffffffffffff)
    0x10e5: v10e5 = OR v10e2, v10d8
    0x10e8: SSTORE v10cb(0x36), v10e5
    0x10e9: v10e9(0x40) = CONST 
    0x10eb: v10eb = MLOAD v10e9(0x40)
    0x10ec: v10ec = CALLER 
    0x10ee: v10ee(0xddf0def21db43e749fe6492e2f575c88b15a5564840edcabe6eed865bb9183e3) = CONST 
    0x1110: v1110(0x0) = CONST 
    0x1113: LOG3 v10eb, v1110(0x0), v10ee(0xddf0def21db43e749fe6492e2f575c88b15a5564840edcabe6eed865bb9183e3), v10ec, v10e2
    0x1115: JUMP v4bb(0x235a)

    Begin block 0x235a
    prev=[0x10ca], succ=[]
    =================================
    0x235b: STOP 

}

function operatorProposal(bytes32,bool,uint256,uint256,uint256,uint256,uint256,uint256,uint256,address)() public {
    Begin block 0x4e0
    prev=[], succ=[0x4f3, 0x4f7]
    =================================
    0x4e1: v4e1(0x237b) = CONST 
    0x4e4: v4e4(0x4) = CONST 
    0x4e7: v4e7 = CALLDATASIZE 
    0x4e8: v4e8 = SUB v4e7, v4e4(0x4)
    0x4e9: v4e9(0x140) = CONST 
    0x4ed: v4ed = LT v4e8, v4e9(0x140)
    0x4ee: v4ee = ISZERO v4ed
    0x4ef: v4ef(0x4f7) = CONST 
    0x4f2: JUMPI v4ef(0x4f7), v4ee

    Begin block 0x4f3
    prev=[0x4e0], succ=[]
    =================================
    0x4f3: v4f3(0x0) = CONST 
    0x4f6: REVERT v4f3(0x0), v4f3(0x0)

    Begin block 0x4f7
    prev=[0x4e0], succ=[0x1116]
    =================================
    0x4fa: v4fa = CALLDATALOAD v4e4(0x4)
    0x4fc: v4fc(0x20) = CONST 
    0x4ff: v4ff(0x24) = ADD v4e4(0x4), v4fc(0x20)
    0x500: v500 = CALLDATALOAD v4ff(0x24)
    0x501: v501 = ISZERO v500
    0x502: v502 = ISZERO v501
    0x504: v504(0x40) = CONST 
    0x507: v507(0x44) = ADD v4e4(0x4), v504(0x40)
    0x508: v508 = CALLDATALOAD v507(0x44)
    0x50a: v50a(0x60) = CONST 
    0x50d: v50d(0x64) = ADD v4e4(0x4), v50a(0x60)
    0x50e: v50e = CALLDATALOAD v50d(0x64)
    0x510: v510(0x80) = CONST 
    0x513: v513(0x84) = ADD v4e4(0x4), v510(0x80)
    0x514: v514 = CALLDATALOAD v513(0x84)
    0x516: v516(0xa0) = CONST 
    0x519: v519(0xa4) = ADD v4e4(0x4), v516(0xa0)
    0x51a: v51a = CALLDATALOAD v519(0xa4)
    0x51c: v51c(0xc0) = CONST 
    0x51f: v51f(0xc4) = ADD v4e4(0x4), v51c(0xc0)
    0x520: v520 = CALLDATALOAD v51f(0xc4)
    0x522: v522(0xe0) = CONST 
    0x525: v525(0xe4) = ADD v4e4(0x4), v522(0xe0)
    0x526: v526 = CALLDATALOAD v525(0xe4)
    0x528: v528(0x100) = CONST 
    0x52c: v52c(0x104) = ADD v4e4(0x4), v528(0x100)
    0x52d: v52d = CALLDATALOAD v52c(0x104)
    0x52f: v52f(0x120) = CONST 
    0x532: v532(0x124) = ADD v52f(0x120), v4e4(0x4)
    0x533: v533 = CALLDATALOAD v532(0x124)
    0x534: v534(0x1) = CONST 
    0x536: v536(0x1) = CONST 
    0x538: v538(0xa0) = CONST 
    0x53a: v53a(0x10000000000000000000000000000000000000000) = SHL v538(0xa0), v536(0x1)
    0x53b: v53b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53a(0x10000000000000000000000000000000000000000), v534(0x1)
    0x53c: v53c = AND v53b(0xffffffffffffffffffffffffffffffffffffffff), v533
    0x53d: v53d(0x1116) = CONST 
    0x540: JUMP v53d(0x1116)

    Begin block 0x1116
    prev=[0x4f7], succ=[0x1121]
    =================================
    0x1117: v1117(0x0) = CONST 
    0x1119: v1119(0x1121) = CONST 
    0x111c: v111c = CALLER 
    0x111d: v111d(0xe53) = CONST 
    0x1120: v1120_0 = CALLPRIVATE v111d(0xe53), v111c, v1119(0x1121)

    Begin block 0x1121
    prev=[0x1116], succ=[0x1126, 0x115c]
    =================================
    0x1122: v1122(0x115c) = CONST 
    0x1125: JUMPI v1122(0x115c), v1120_0

    Begin block 0x1126
    prev=[0x1121], succ=[]
    =================================
    0x1126: v1126(0x40) = CONST 
    0x1128: v1128 = MLOAD v1126(0x40)
    0x1129: v1129(0x461bcd) = CONST 
    0x112d: v112d(0xe5) = CONST 
    0x112f: v112f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v112d(0xe5), v1129(0x461bcd)
    0x1131: MSTORE v1128, v112f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1132: v1132(0x4) = CONST 
    0x1134: v1134 = ADD v1132(0x4), v1128
    0x1137: v1137(0x20) = CONST 
    0x1139: v1139 = ADD v1137(0x20), v1134
    0x113c: v113c(0x20) = SUB v1139, v1134
    0x113e: MSTORE v1134, v113c(0x20)
    0x113f: v113f(0x34) = CONST 
    0x1142: MSTORE v1139, v113f(0x34)
    0x1143: v1143(0x20) = CONST 
    0x1145: v1145 = ADD v1143(0x20), v1139
    0x1147: v1147(0x1bfb) = CONST 
    0x114a: v114a(0x34) = CONST 
    0x114d: CODECOPY v1145, v1147(0x1bfb), v114a(0x34)
    0x114e: v114e(0x40) = CONST 
    0x1150: v1150 = ADD v114e(0x40), v1145
    0x1154: v1154(0x40) = CONST 
    0x1156: v1156 = MLOAD v1154(0x40)
    0x1159: v1159(0x84) = SUB v1150, v1156
    0x115b: REVERT v1156, v1159(0x84)

    Begin block 0x115c
    prev=[0x1121], succ=[0x117b, 0x11c7]
    =================================
    0x115d: v115d(0x0) = CONST 
    0x1161: MSTORE v115d(0x0), v4fa
    0x1162: v1162(0x3a) = CONST 
    0x1164: v1164(0x20) = CONST 
    0x1166: MSTORE v1164(0x20), v1162(0x3a)
    0x1167: v1167(0x40) = CONST 
    0x116a: v116a = SHA3 v115d(0x0), v1167(0x40)
    0x116c: v116c = SLOAD v116a
    0x116d: v116d(0x1) = CONST 
    0x116f: v116f(0x1) = CONST 
    0x1171: v1171(0xa0) = CONST 
    0x1173: v1173(0x10000000000000000000000000000000000000000) = SHL v1171(0xa0), v116f(0x1)
    0x1174: v1174(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1173(0x10000000000000000000000000000000000000000), v116d(0x1)
    0x1175: v1175 = AND v1174(0xffffffffffffffffffffffffffffffffffffffff), v116c
    0x1176: v1176 = ISZERO v1175
    0x1177: v1177(0x11c7) = CONST 
    0x117a: JUMPI v1177(0x11c7), v1176

    Begin block 0x117b
    prev=[0x115c], succ=[]
    =================================
    0x117b: v117b(0x40) = CONST 
    0x117e: v117e = MLOAD v117b(0x40)
    0x117f: v117f(0x461bcd) = CONST 
    0x1183: v1183(0xe5) = CONST 
    0x1185: v1185(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1183(0xe5), v117f(0x461bcd)
    0x1187: MSTORE v117e, v1185(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1188: v1188(0x20) = CONST 
    0x118a: v118a(0x4) = CONST 
    0x118d: v118d = ADD v117e, v118a(0x4)
    0x118e: MSTORE v118d, v1188(0x20)
    0x118f: v118f(0x1c) = CONST 
    0x1191: v1191(0x24) = CONST 
    0x1194: v1194 = ADD v117e, v1191(0x24)
    0x1195: MSTORE v1194, v118f(0x1c)
    0x1196: v1196(0x5261697365466163746f72793a20616c72656164792065786973747300000000) = CONST 
    0x11b7: v11b7(0x44) = CONST 
    0x11ba: v11ba = ADD v117e, v11b7(0x44)
    0x11bb: MSTORE v11ba, v1196(0x5261697365466163746f72793a20616c72656164792065786973747300000000)
    0x11bd: v11bd = MLOAD v117b(0x40)
    0x11c1: v11c1(0x0) = SUB v117e, v11bd
    0x11c2: v11c2(0x64) = CONST 
    0x11c4: v11c4(0x64) = ADD v11c2(0x64), v11c1(0x0)
    0x11c6: REVERT v11bd, v11c4(0x64)

    Begin block 0x11c7
    prev=[0x115c], succ=[0x11da, 0x1210]
    =================================
    0x11c8: v11c8(0x2) = CONST 
    0x11cb: v11cb = ADD v116a, v11c8(0x2)
    0x11cc: v11cc = SLOAD v11cb
    0x11cd: v11cd(0x1) = CONST 
    0x11cf: v11cf(0x1) = CONST 
    0x11d1: v11d1(0xa0) = CONST 
    0x11d3: v11d3(0x10000000000000000000000000000000000000000) = SHL v11d1(0xa0), v11cf(0x1)
    0x11d4: v11d4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11d3(0x10000000000000000000000000000000000000000), v11cd(0x1)
    0x11d5: v11d5 = AND v11d4(0xffffffffffffffffffffffffffffffffffffffff), v11cc
    0x11d6: v11d6(0x1210) = CONST 
    0x11d9: JUMPI v11d6(0x1210), v11d5

    Begin block 0x11da
    prev=[0x11c7], succ=[]
    =================================
    0x11da: v11da(0x40) = CONST 
    0x11dc: v11dc = MLOAD v11da(0x40)
    0x11dd: v11dd(0x461bcd) = CONST 
    0x11e1: v11e1(0xe5) = CONST 
    0x11e3: v11e3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v11e1(0xe5), v11dd(0x461bcd)
    0x11e5: MSTORE v11dc, v11e3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11e6: v11e6(0x4) = CONST 
    0x11e8: v11e8 = ADD v11e6(0x4), v11dc
    0x11eb: v11eb(0x20) = CONST 
    0x11ed: v11ed = ADD v11eb(0x20), v11e8
    0x11f0: v11f0(0x20) = SUB v11ed, v11e8
    0x11f2: MSTORE v11e8, v11f0(0x20)
    0x11f3: v11f3(0x21) = CONST 
    0x11f6: MSTORE v11ed, v11f3(0x21)
    0x11f7: v11f7(0x20) = CONST 
    0x11f9: v11f9 = ADD v11f7(0x20), v11ed
    0x11fb: v11fb(0x1bda) = CONST 
    0x11fe: v11fe(0x21) = CONST 
    0x1201: CODECOPY v11f9, v11fb(0x1bda), v11fe(0x21)
    0x1202: v1202(0x40) = CONST 
    0x1204: v1204 = ADD v1202(0x40), v11f9
    0x1208: v1208(0x40) = CONST 
    0x120a: v120a = MLOAD v1208(0x40)
    0x120d: v120d(0x84) = SUB v1204, v120a
    0x120f: REVERT v120a, v120d(0x84)

    Begin block 0x1210
    prev=[0x11c7], succ=[0x1216, 0x12fc]
    =================================
    0x1212: v1212(0x12fc) = CONST 
    0x1215: JUMPI v1212(0x12fc), v502

    Begin block 0x1216
    prev=[0x1210], succ=[0x168b]
    =================================
    0x1216: v1216(0x3a) = CONST 
    0x1218: v1218(0x0) = CONST 
    0x121c: MSTORE v1218(0x0), v4fa
    0x121d: v121d(0x20) = CONST 
    0x121f: v121f(0x20) = ADD v121d(0x20), v1218(0x0)
    0x1222: MSTORE v121f(0x20), v1216(0x3a)
    0x1223: v1223(0x20) = CONST 
    0x1225: v1225(0x40) = ADD v1223(0x20), v121f(0x20)
    0x1226: v1226(0x0) = CONST 
    0x1228: v1228 = SHA3 v1226(0x0), v1225(0x40)
    0x1229: v1229(0x0) = CONST 
    0x122d: v122d = ADD v1228, v1229(0x0)
    0x122e: v122e(0x0) = CONST 
    0x1230: v1230(0x100) = CONST 
    0x1233: v1233(0x1) = EXP v1230(0x100), v122e(0x0)
    0x1235: v1235 = SLOAD v122d
    0x1237: v1237(0x1) = CONST 
    0x1239: v1239(0x1) = CONST 
    0x123b: v123b(0xa0) = CONST 
    0x123d: v123d(0x10000000000000000000000000000000000000000) = SHL v123b(0xa0), v1239(0x1)
    0x123e: v123e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v123d(0x10000000000000000000000000000000000000000), v1237(0x1)
    0x123f: v123f(0xffffffffffffffffffffffffffffffffffffffff) = MUL v123e(0xffffffffffffffffffffffffffffffffffffffff), v1233(0x1)
    0x1240: v1240(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v123f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1241: v1241 = AND v1240(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1235
    0x1243: SSTORE v122d, v1241
    0x1244: v1244(0x1) = CONST 
    0x1247: v1247 = ADD v1228, v1244(0x1)
    0x1248: v1248(0x0) = CONST 
    0x124a: v124a(0x100) = CONST 
    0x124d: v124d(0x1) = EXP v124a(0x100), v1248(0x0)
    0x124f: v124f = SLOAD v1247
    0x1251: v1251(0x1) = CONST 
    0x1253: v1253(0x1) = CONST 
    0x1255: v1255(0xa0) = CONST 
    0x1257: v1257(0x10000000000000000000000000000000000000000) = SHL v1255(0xa0), v1253(0x1)
    0x1258: v1258(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1257(0x10000000000000000000000000000000000000000), v1251(0x1)
    0x1259: v1259(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1258(0xffffffffffffffffffffffffffffffffffffffff), v124d(0x1)
    0x125a: v125a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1259(0xffffffffffffffffffffffffffffffffffffffff)
    0x125b: v125b = AND v125a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v124f
    0x125d: SSTORE v1247, v125b
    0x125e: v125e(0x2) = CONST 
    0x1261: v1261 = ADD v1228, v125e(0x2)
    0x1262: v1262(0x0) = CONST 
    0x1264: v1264(0x100) = CONST 
    0x1267: v1267(0x1) = EXP v1264(0x100), v1262(0x0)
    0x1269: v1269 = SLOAD v1261
    0x126b: v126b(0x1) = CONST 
    0x126d: v126d(0x1) = CONST 
    0x126f: v126f(0xa0) = CONST 
    0x1271: v1271(0x10000000000000000000000000000000000000000) = SHL v126f(0xa0), v126d(0x1)
    0x1272: v1272(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1271(0x10000000000000000000000000000000000000000), v126b(0x1)
    0x1273: v1273(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1272(0xffffffffffffffffffffffffffffffffffffffff), v1267(0x1)
    0x1274: v1274(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1273(0xffffffffffffffffffffffffffffffffffffffff)
    0x1275: v1275 = AND v1274(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1269
    0x1277: SSTORE v1261, v1275
    0x1278: v1278(0x3) = CONST 
    0x127b: v127b = ADD v1228, v1278(0x3)
    0x127c: v127c(0x0) = CONST 
    0x127e: v127e(0x100) = CONST 
    0x1281: v1281(0x1) = EXP v127e(0x100), v127c(0x0)
    0x1283: v1283 = SLOAD v127b
    0x1285: v1285(0x1) = CONST 
    0x1287: v1287(0x1) = CONST 
    0x1289: v1289(0xa0) = CONST 
    0x128b: v128b(0x10000000000000000000000000000000000000000) = SHL v1289(0xa0), v1287(0x1)
    0x128c: v128c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v128b(0x10000000000000000000000000000000000000000), v1285(0x1)
    0x128d: v128d(0xffffffffffffffffffffffffffffffffffffffff) = MUL v128c(0xffffffffffffffffffffffffffffffffffffffff), v1281(0x1)
    0x128e: v128e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v128d(0xffffffffffffffffffffffffffffffffffffffff)
    0x128f: v128f = AND v128e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1283
    0x1291: SSTORE v127b, v128f
    0x1294: v1294 = CALLER 
    0x1295: v1295(0x1) = CONST 
    0x1297: v1297(0x1) = CONST 
    0x1299: v1299(0xa0) = CONST 
    0x129b: v129b(0x10000000000000000000000000000000000000000) = SHL v1299(0xa0), v1297(0x1)
    0x129c: v129c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v129b(0x10000000000000000000000000000000000000000), v1295(0x1)
    0x129d: v129d = AND v129c(0xffffffffffffffffffffffffffffffffffffffff), v1294
    0x12a0: v12a0(0x2) = CONST 
    0x12a2: v12a2 = ADD v12a0(0x2), v116a
    0x12a3: v12a3(0x0) = CONST 
    0x12a6: v12a6 = SLOAD v12a2
    0x12a8: v12a8(0x100) = CONST 
    0x12ab: v12ab(0x1) = EXP v12a8(0x100), v12a3(0x0)
    0x12ad: v12ad = DIV v12a6, v12ab(0x1)
    0x12ae: v12ae(0x1) = CONST 
    0x12b0: v12b0(0x1) = CONST 
    0x12b2: v12b2(0xa0) = CONST 
    0x12b4: v12b4(0x10000000000000000000000000000000000000000) = SHL v12b2(0xa0), v12b0(0x1)
    0x12b5: v12b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12b4(0x10000000000000000000000000000000000000000), v12ae(0x1)
    0x12b6: v12b6 = AND v12b5(0xffffffffffffffffffffffffffffffffffffffff), v12ad
    0x12b7: v12b7(0x1) = CONST 
    0x12b9: v12b9(0x1) = CONST 
    0x12bb: v12bb(0xa0) = CONST 
    0x12bd: v12bd(0x10000000000000000000000000000000000000000) = SHL v12bb(0xa0), v12b9(0x1)
    0x12be: v12be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12bd(0x10000000000000000000000000000000000000000), v12b7(0x1)
    0x12bf: v12bf = AND v12be(0xffffffffffffffffffffffffffffffffffffffff), v12b6
    0x12c0: v12c0(0x9b9dc5f61d264f36c4047bf16e1599aaf483412bc25eb9f7edbde9ac32bf1596) = CONST 
    0x12e1: v12e1 = TIMESTAMP 
    0x12e2: v12e2(0x40) = CONST 
    0x12e4: v12e4 = MLOAD v12e2(0x40)
    0x12e8: MSTORE v12e4, v12e1
    0x12e9: v12e9(0x20) = CONST 
    0x12eb: v12eb = ADD v12e9(0x20), v12e4
    0x12ef: v12ef(0x40) = CONST 
    0x12f1: v12f1 = MLOAD v12ef(0x40)
    0x12f4: v12f4(0x20) = SUB v12eb, v12f1
    0x12f6: LOG4 v12f1, v12f4(0x20), v12c0(0x9b9dc5f61d264f36c4047bf16e1599aaf483412bc25eb9f7edbde9ac32bf1596), v12bf, v4fa, v129d
    0x12f8: v12f8(0x168b) = CONST 
    0x12fb: JUMP v12f8(0x168b)

    Begin block 0x168b
    prev=[0x1216, 0x14db], succ=[0x237b]
    =================================
    0x1698: JUMP v4e1(0x237b)

    Begin block 0x237b
    prev=[0x168b], succ=[]
    =================================
    0x237b_0x0: v237b_0 = PHI v1117(0x0), v139f
    0x237c: v237c(0x40) = CONST 
    0x237f: v237f = MLOAD v237c(0x40)
    0x2380: v2380(0x1) = CONST 
    0x2382: v2382(0x1) = CONST 
    0x2384: v2384(0xa0) = CONST 
    0x2386: v2386(0x10000000000000000000000000000000000000000) = SHL v2384(0xa0), v2382(0x1)
    0x2387: v2387(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2386(0x10000000000000000000000000000000000000000), v2380(0x1)
    0x238a: v238a = AND v237b_0, v2387(0xffffffffffffffffffffffffffffffffffffffff)
    0x238c: MSTORE v237f, v238a
    0x238d: v238d = MLOAD v237c(0x40)
    0x2391: v2391(0x0) = SUB v237f, v238d
    0x2392: v2392(0x20) = CONST 
    0x2394: v2394(0x20) = ADD v2392(0x20), v2391(0x0)
    0x2396: RETURN v238d, v2394(0x20)

    Begin block 0x12fc
    prev=[0x1210], succ=[0x136f, 0x1373]
    =================================
    0x12fd: v12fd(0x39) = CONST 
    0x12ff: v12ff = SLOAD v12fd(0x39)
    0x1300: v1300(0x38) = CONST 
    0x1302: v1302 = SLOAD v1300(0x38)
    0x1303: v1303(0x40) = CONST 
    0x1306: v1306 = MLOAD v1303(0x40)
    0x1307: v1307(0x3c56e06b) = CONST 
    0x130c: v130c(0xe1) = CONST 
    0x130e: v130e(0x78adc0d600000000000000000000000000000000000000000000000000000000) = SHL v130c(0xe1), v1307(0x3c56e06b)
    0x1310: MSTORE v1306, v130e(0x78adc0d600000000000000000000000000000000000000000000000000000000)
    0x1311: v1311(0x1) = CONST 
    0x1313: v1313(0x1) = CONST 
    0x1315: v1315(0xa0) = CONST 
    0x1317: v1317(0x10000000000000000000000000000000000000000) = SHL v1315(0xa0), v1313(0x1)
    0x1318: v1318(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1317(0x10000000000000000000000000000000000000000), v1311(0x1)
    0x131b: v131b = AND v1318(0xffffffffffffffffffffffffffffffffffffffff), v12ff
    0x131c: v131c(0x4) = CONST 
    0x131f: v131f = ADD v1306, v131c(0x4)
    0x1320: MSTORE v131f, v131b
    0x1324: v1324 = AND v1302, v1318(0xffffffffffffffffffffffffffffffffffffffff)
    0x1325: v1325(0x24) = CONST 
    0x1328: v1328 = ADD v1306, v1325(0x24)
    0x1329: MSTORE v1328, v1324
    0x132a: v132a(0x60) = CONST 
    0x132c: v132c(0x44) = CONST 
    0x132f: v132f = ADD v1306, v132c(0x44)
    0x1330: MSTORE v132f, v132a(0x60)
    0x1331: v1331(0x0) = CONST 
    0x1333: v1333(0x64) = CONST 
    0x1336: v1336 = ADD v1306, v1333(0x64)
    0x1337: MSTORE v1336, v1331(0x0)
    0x1338: v1338 = MLOAD v1303(0x40)
    0x1339: v1339(0xdb3069eb173c10424de2a58b8e3650a2db7e2cb4) = CONST 
    0x134f: v134f(0x78adc0d6) = CONST 
    0x1355: v1355(0xa4) = CONST 
    0x1359: v1359 = ADD v1306, v1355(0xa4)
    0x135b: v135b(0x20) = CONST 
    0x1362: v1362(0x0) = SUB v1306, v1338
    0x1363: v1363(0xa4) = ADD v1362(0x0), v1355(0xa4)
    0x1367: v1367 = EXTCODESIZE v1339(0xdb3069eb173c10424de2a58b8e3650a2db7e2cb4)
    0x1368: v1368 = ISZERO v1367
    0x136a: v136a = ISZERO v1368
    0x136b: v136b(0x1373) = CONST 
    0x136e: JUMPI v136b(0x1373), v136a

    Begin block 0x136f
    prev=[0x12fc], succ=[]
    =================================
    0x136f: v136f(0x0) = CONST 
    0x1372: REVERT v136f(0x0), v136f(0x0)

    Begin block 0x1373
    prev=[0x12fc], succ=[0x137e, 0x1387]
    =================================
    0x1375: v1375 = GAS 
    0x1376: v1376 = DELEGATECALL v1375, v1339(0xdb3069eb173c10424de2a58b8e3650a2db7e2cb4), v1338, v1363(0xa4), v1338, v135b(0x20)
    0x1377: v1377 = ISZERO v1376
    0x1379: v1379 = ISZERO v1377
    0x137a: v137a(0x1387) = CONST 
    0x137d: JUMPI v137a(0x1387), v1379

    Begin block 0x137e
    prev=[0x1373], succ=[]
    =================================
    0x137e: v137e = RETURNDATASIZE 
    0x137f: v137f(0x0) = CONST 
    0x1382: RETURNDATACOPY v137f(0x0), v137f(0x0), v137e
    0x1383: v1383 = RETURNDATASIZE 
    0x1384: v1384(0x0) = CONST 
    0x1386: REVERT v1384(0x0), v1383

    Begin block 0x1387
    prev=[0x1373], succ=[0x1399, 0x139d]
    =================================
    0x138c: v138c(0x40) = CONST 
    0x138e: v138e = MLOAD v138c(0x40)
    0x138f: v138f = RETURNDATASIZE 
    0x1390: v1390(0x20) = CONST 
    0x1393: v1393 = LT v138f, v1390(0x20)
    0x1394: v1394 = ISZERO v1393
    0x1395: v1395(0x139d) = CONST 
    0x1398: JUMPI v1395(0x139d), v1394

    Begin block 0x1399
    prev=[0x1387], succ=[]
    =================================
    0x1399: v1399(0x0) = CONST 
    0x139c: REVERT v1399(0x0), v1399(0x0)

    Begin block 0x139d
    prev=[0x1387], succ=[0xcd6B0x139d]
    =================================
    0x139f: v139f = MLOAD v138e
    0x13a0: v13a0(0x37) = CONST 
    0x13a2: v13a2 = SLOAD v13a0(0x37)
    0x13a3: v13a3(0x2) = CONST 
    0x13a6: v13a6 = ADD v116a, v13a3(0x2)
    0x13a7: v13a7 = SLOAD v13a6
    0x13ab: v13ab(0xd19b2c6a68dce187d2cb9c08d2b35f96924a76d4) = CONST 
    0x13c1: v13c1(0x566c6131) = CONST 
    0x13c9: v13c9(0x1) = CONST 
    0x13cb: v13cb(0x1) = CONST 
    0x13cd: v13cd(0xa0) = CONST 
    0x13cf: v13cf(0x10000000000000000000000000000000000000000) = SHL v13cd(0xa0), v13cb(0x1)
    0x13d0: v13d0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13cf(0x10000000000000000000000000000000000000000), v13c9(0x1)
    0x13d3: v13d3 = AND v13d0(0xffffffffffffffffffffffffffffffffffffffff), v13a2
    0x13d5: v13d5 = AND v13d0(0xffffffffffffffffffffffffffffffffffffffff), v13a7
    0x13dd: v13dd(0x13e4) = CONST 
    0x13e0: v13e0(0xcd6) = CONST 
    0x13e3: JUMP v13e0(0xcd6)

    Begin block 0xcd6B0x139d
    prev=[0x139d], succ=[0x13e4]
    =================================
    0xcd7S0x139d: vcd7V139d(0x33) = CONST 
    0xcd9S0x139d: vcd9V139d = SLOAD vcd7V139d(0x33)
    0xcdaS0x139d: vcdaV139d(0x1) = CONST 
    0xcdcS0x139d: vcdcV139d(0x1) = CONST 
    0xcdeS0x139d: vcdeV139d(0xa0) = CONST 
    0xce0S0x139d: vce0V139d(0x10000000000000000000000000000000000000000) = SHL vcdeV139d(0xa0), vcdcV139d(0x1)
    0xce1S0x139d: vce1V139d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce0V139d(0x10000000000000000000000000000000000000000), vcdaV139d(0x1)
    0xce2S0x139d: vce2V139d = AND vce1V139d(0xffffffffffffffffffffffffffffffffffffffff), vcd9V139d
    0xce4S0x139d: JUMP v13dd(0x13e4)

    Begin block 0x13e4
    prev=[0xcd6B0x139d], succ=[0xb99B0x13e4]
    =================================
    0x13e5: v13e5(0x13ec) = CONST 
    0x13e8: v13e8(0xb99) = CONST 
    0x13eb: JUMP v13e8(0xb99)

    Begin block 0xb99B0x13e4
    prev=[0x13e4], succ=[0x13ec]
    =================================
    0xb9aS0x13e4: vb9aV13e4(0x35) = CONST 
    0xb9cS0x13e4: vb9cV13e4 = SLOAD vb9aV13e4(0x35)
    0xb9dS0x13e4: vb9dV13e4(0x1) = CONST 
    0xb9fS0x13e4: vb9fV13e4(0x1) = CONST 
    0xba1S0x13e4: vba1V13e4(0xa0) = CONST 
    0xba3S0x13e4: vba3V13e4(0x10000000000000000000000000000000000000000) = SHL vba1V13e4(0xa0), vb9fV13e4(0x1)
    0xba4S0x13e4: vba4V13e4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vba3V13e4(0x10000000000000000000000000000000000000000), vb9dV13e4(0x1)
    0xba5S0x13e4: vba5V13e4 = AND vba4V13e4(0xffffffffffffffffffffffffffffffffffffffff), vb9cV13e4
    0xba7S0x13e4: JUMP v13e5(0x13ec)

    Begin block 0x13ec
    prev=[0xb99B0x13e4], succ=[0x14c3, 0x14c7]
    =================================
    0x13ed: v13ed(0x40) = CONST 
    0x13ef: v13ef = MLOAD v13ed(0x40)
    0x13f1: v13f1(0xffffffff) = CONST 
    0x13f6: v13f6(0x566c6131) = AND v13f1(0xffffffff), v13c1(0x566c6131)
    0x13f7: v13f7(0xe0) = CONST 
    0x13f9: v13f9(0x566c613100000000000000000000000000000000000000000000000000000000) = SHL v13f7(0xe0), v13f6(0x566c6131)
    0x13fb: MSTORE v13ef, v13f9(0x566c613100000000000000000000000000000000000000000000000000000000)
    0x13fc: v13fc(0x4) = CONST 
    0x13fe: v13fe = ADD v13fc(0x4), v13ef
    0x1401: v1401(0x1) = CONST 
    0x1403: v1403(0x1) = CONST 
    0x1405: v1405(0xa0) = CONST 
    0x1407: v1407(0x10000000000000000000000000000000000000000) = SHL v1405(0xa0), v1403(0x1)
    0x1408: v1408(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1407(0x10000000000000000000000000000000000000000), v1401(0x1)
    0x1409: v1409 = AND v1408(0xffffffffffffffffffffffffffffffffffffffff), v139f
    0x140a: v140a(0x1) = CONST 
    0x140c: v140c(0x1) = CONST 
    0x140e: v140e(0xa0) = CONST 
    0x1410: v1410(0x10000000000000000000000000000000000000000) = SHL v140e(0xa0), v140c(0x1)
    0x1411: v1411(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1410(0x10000000000000000000000000000000000000000), v140a(0x1)
    0x1412: v1412 = AND v1411(0xffffffffffffffffffffffffffffffffffffffff), v1409
    0x1414: MSTORE v13fe, v1412
    0x1415: v1415(0x20) = CONST 
    0x1417: v1417 = ADD v1415(0x20), v13fe
    0x1419: v1419(0x1) = CONST 
    0x141b: v141b(0x1) = CONST 
    0x141d: v141d(0xa0) = CONST 
    0x141f: v141f(0x10000000000000000000000000000000000000000) = SHL v141d(0xa0), v141b(0x1)
    0x1420: v1420(0xffffffffffffffffffffffffffffffffffffffff) = SUB v141f(0x10000000000000000000000000000000000000000), v1419(0x1)
    0x1421: v1421 = AND v1420(0xffffffffffffffffffffffffffffffffffffffff), v13d3
    0x1422: v1422(0x1) = CONST 
    0x1424: v1424(0x1) = CONST 
    0x1426: v1426(0xa0) = CONST 
    0x1428: v1428(0x10000000000000000000000000000000000000000) = SHL v1426(0xa0), v1424(0x1)
    0x1429: v1429(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1428(0x10000000000000000000000000000000000000000), v1422(0x1)
    0x142a: v142a = AND v1429(0xffffffffffffffffffffffffffffffffffffffff), v1421
    0x142c: MSTORE v1417, v142a
    0x142d: v142d(0x20) = CONST 
    0x142f: v142f = ADD v142d(0x20), v1417
    0x1431: v1431(0x1) = CONST 
    0x1433: v1433(0x1) = CONST 
    0x1435: v1435(0xa0) = CONST 
    0x1437: v1437(0x10000000000000000000000000000000000000000) = SHL v1435(0xa0), v1433(0x1)
    0x1438: v1438(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1437(0x10000000000000000000000000000000000000000), v1431(0x1)
    0x1439: v1439 = AND v1438(0xffffffffffffffffffffffffffffffffffffffff), v13d5
    0x143a: v143a(0x1) = CONST 
    0x143c: v143c(0x1) = CONST 
    0x143e: v143e(0xa0) = CONST 
    0x1440: v1440(0x10000000000000000000000000000000000000000) = SHL v143e(0xa0), v143c(0x1)
    0x1441: v1441(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1440(0x10000000000000000000000000000000000000000), v143a(0x1)
    0x1442: v1442 = AND v1441(0xffffffffffffffffffffffffffffffffffffffff), v1439
    0x1444: MSTORE v142f, v1442
    0x1445: v1445(0x20) = CONST 
    0x1447: v1447 = ADD v1445(0x20), v142f
    0x144a: MSTORE v1447, v508
    0x144b: v144b(0x20) = CONST 
    0x144d: v144d = ADD v144b(0x20), v1447
    0x1450: MSTORE v144d, v50e
    0x1451: v1451(0x20) = CONST 
    0x1453: v1453 = ADD v1451(0x20), v144d
    0x1456: MSTORE v1453, v514
    0x1457: v1457(0x20) = CONST 
    0x1459: v1459 = ADD v1457(0x20), v1453
    0x145c: MSTORE v1459, v51a
    0x145d: v145d(0x20) = CONST 
    0x145f: v145f = ADD v145d(0x20), v1459
    0x1462: MSTORE v145f, v520
    0x1463: v1463(0x20) = CONST 
    0x1465: v1465 = ADD v1463(0x20), v145f
    0x1468: MSTORE v1465, v526
    0x1469: v1469(0x20) = CONST 
    0x146b: v146b = ADD v1469(0x20), v1465
    0x146e: MSTORE v146b, v52d
    0x146f: v146f(0x20) = CONST 
    0x1471: v1471 = ADD v146f(0x20), v146b
    0x1473: v1473(0x1) = CONST 
    0x1475: v1475(0x1) = CONST 
    0x1477: v1477(0xa0) = CONST 
    0x1479: v1479(0x10000000000000000000000000000000000000000) = SHL v1477(0xa0), v1475(0x1)
    0x147a: v147a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1479(0x10000000000000000000000000000000000000000), v1473(0x1)
    0x147b: v147b = AND v147a(0xffffffffffffffffffffffffffffffffffffffff), vce2V139d
    0x147c: v147c(0x1) = CONST 
    0x147e: v147e(0x1) = CONST 
    0x1480: v1480(0xa0) = CONST 
    0x1482: v1482(0x10000000000000000000000000000000000000000) = SHL v1480(0xa0), v147e(0x1)
    0x1483: v1483(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1482(0x10000000000000000000000000000000000000000), v147c(0x1)
    0x1484: v1484 = AND v1483(0xffffffffffffffffffffffffffffffffffffffff), v147b
    0x1486: MSTORE v1471, v1484
    0x1487: v1487(0x20) = CONST 
    0x1489: v1489 = ADD v1487(0x20), v1471
    0x148b: v148b(0x1) = CONST 
    0x148d: v148d(0x1) = CONST 
    0x148f: v148f(0xa0) = CONST 
    0x1491: v1491(0x10000000000000000000000000000000000000000) = SHL v148f(0xa0), v148d(0x1)
    0x1492: v1492(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1491(0x10000000000000000000000000000000000000000), v148b(0x1)
    0x1493: v1493 = AND v1492(0xffffffffffffffffffffffffffffffffffffffff), vba5V13e4
    0x1494: v1494(0x1) = CONST 
    0x1496: v1496(0x1) = CONST 
    0x1498: v1498(0xa0) = CONST 
    0x149a: v149a(0x10000000000000000000000000000000000000000) = SHL v1498(0xa0), v1496(0x1)
    0x149b: v149b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v149a(0x10000000000000000000000000000000000000000), v1494(0x1)
    0x149c: v149c = AND v149b(0xffffffffffffffffffffffffffffffffffffffff), v1493
    0x149e: MSTORE v1489, v149c
    0x149f: v149f(0x20) = CONST 
    0x14a1: v14a1 = ADD v149f(0x20), v1489
    0x14b0: v14b0(0x0) = CONST 
    0x14b2: v14b2(0x40) = CONST 
    0x14b4: v14b4 = MLOAD v14b2(0x40)
    0x14b7: v14b7(0x184) = SUB v14a1, v14b4
    0x14bb: v14bb = EXTCODESIZE v13ab(0xd19b2c6a68dce187d2cb9c08d2b35f96924a76d4)
    0x14bc: v14bc = ISZERO v14bb
    0x14be: v14be = ISZERO v14bc
    0x14bf: v14bf(0x14c7) = CONST 
    0x14c2: JUMPI v14bf(0x14c7), v14be

    Begin block 0x14c3
    prev=[0x13ec], succ=[]
    =================================
    0x14c3: v14c3(0x0) = CONST 
    0x14c6: REVERT v14c3(0x0), v14c3(0x0)

    Begin block 0x14c7
    prev=[0x13ec], succ=[0x14d2, 0x14db]
    =================================
    0x14c9: v14c9 = GAS 
    0x14ca: v14ca = DELEGATECALL v14c9, v13ab(0xd19b2c6a68dce187d2cb9c08d2b35f96924a76d4), v14b4, v14b7(0x184), v14b4, v14b0(0x0)
    0x14cb: v14cb = ISZERO v14ca
    0x14cd: v14cd = ISZERO v14cb
    0x14ce: v14ce(0x14db) = CONST 
    0x14d1: JUMPI v14ce(0x14db), v14cd

    Begin block 0x14d2
    prev=[0x14c7], succ=[]
    =================================
    0x14d2: v14d2 = RETURNDATASIZE 
    0x14d3: v14d3(0x0) = CONST 
    0x14d6: RETURNDATACOPY v14d3(0x0), v14d3(0x0), v14d2
    0x14d7: v14d7 = RETURNDATASIZE 
    0x14d8: v14d8(0x0) = CONST 
    0x14da: REVERT v14d8(0x0), v14d7

    Begin block 0x14db
    prev=[0x14c7], succ=[0x168b]
    =================================
    0x14e1: v14e1(0x3a) = CONST 
    0x14e3: v14e3(0x0) = CONST 
    0x14e7: MSTORE v14e3(0x0), v4fa
    0x14e8: v14e8(0x20) = CONST 
    0x14ea: v14ea(0x20) = ADD v14e8(0x20), v14e3(0x0)
    0x14ed: MSTORE v14ea(0x20), v14e1(0x3a)
    0x14ee: v14ee(0x20) = CONST 
    0x14f0: v14f0(0x40) = ADD v14ee(0x20), v14ea(0x20)
    0x14f1: v14f1(0x0) = CONST 
    0x14f3: v14f3 = SHA3 v14f1(0x0), v14f0(0x40)
    0x14f4: v14f4(0x3) = CONST 
    0x14f6: v14f6 = ADD v14f4(0x3), v14f3
    0x14f7: v14f7(0x0) = CONST 
    0x14f9: v14f9(0x100) = CONST 
    0x14fc: v14fc(0x1) = EXP v14f9(0x100), v14f7(0x0)
    0x14fe: v14fe = SLOAD v14f6
    0x1500: v1500(0x1) = CONST 
    0x1502: v1502(0x1) = CONST 
    0x1504: v1504(0xa0) = CONST 
    0x1506: v1506(0x10000000000000000000000000000000000000000) = SHL v1504(0xa0), v1502(0x1)
    0x1507: v1507(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1506(0x10000000000000000000000000000000000000000), v1500(0x1)
    0x1508: v1508(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1507(0xffffffffffffffffffffffffffffffffffffffff), v14fc(0x1)
    0x1509: v1509(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1508(0xffffffffffffffffffffffffffffffffffffffff)
    0x150a: v150a = AND v1509(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v14fe
    0x150d: v150d(0x1) = CONST 
    0x150f: v150f(0x1) = CONST 
    0x1511: v1511(0xa0) = CONST 
    0x1513: v1513(0x10000000000000000000000000000000000000000) = SHL v1511(0xa0), v150f(0x1)
    0x1514: v1514(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1513(0x10000000000000000000000000000000000000000), v150d(0x1)
    0x1515: v1515 = AND v1514(0xffffffffffffffffffffffffffffffffffffffff), v53c
    0x1516: v1516 = MUL v1515, v14fc(0x1)
    0x1517: v1517 = OR v1516, v150a
    0x1519: SSTORE v14f6, v1517
    0x151b: v151b(0x39) = CONST 
    0x151d: v151d(0x0) = CONST 
    0x1520: v1520 = SLOAD v151b(0x39)
    0x1522: v1522(0x100) = CONST 
    0x1525: v1525(0x1) = EXP v1522(0x100), v151d(0x0)
    0x1527: v1527 = DIV v1520, v1525(0x1)
    0x1528: v1528(0x1) = CONST 
    0x152a: v152a(0x1) = CONST 
    0x152c: v152c(0xa0) = CONST 
    0x152e: v152e(0x10000000000000000000000000000000000000000) = SHL v152c(0xa0), v152a(0x1)
    0x152f: v152f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v152e(0x10000000000000000000000000000000000000000), v1528(0x1)
    0x1530: v1530 = AND v152f(0xffffffffffffffffffffffffffffffffffffffff), v1527
    0x1531: v1531(0x3a) = CONST 
    0x1533: v1533(0x0) = CONST 
    0x1537: MSTORE v1533(0x0), v4fa
    0x1538: v1538(0x20) = CONST 
    0x153a: v153a(0x20) = ADD v1538(0x20), v1533(0x0)
    0x153d: MSTORE v153a(0x20), v1531(0x3a)
    0x153e: v153e(0x20) = CONST 
    0x1540: v1540(0x40) = ADD v153e(0x20), v153a(0x20)
    0x1541: v1541(0x0) = CONST 
    0x1543: v1543 = SHA3 v1541(0x0), v1540(0x40)
    0x1544: v1544(0x0) = CONST 
    0x1546: v1546 = ADD v1544(0x0), v1543
    0x1547: v1547(0x0) = CONST 
    0x1549: v1549(0x100) = CONST 
    0x154c: v154c(0x1) = EXP v1549(0x100), v1547(0x0)
    0x154e: v154e = SLOAD v1546
    0x1550: v1550(0x1) = CONST 
    0x1552: v1552(0x1) = CONST 
    0x1554: v1554(0xa0) = CONST 
    0x1556: v1556(0x10000000000000000000000000000000000000000) = SHL v1554(0xa0), v1552(0x1)
    0x1557: v1557(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1556(0x10000000000000000000000000000000000000000), v1550(0x1)
    0x1558: v1558(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1557(0xffffffffffffffffffffffffffffffffffffffff), v154c(0x1)
    0x1559: v1559(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1558(0xffffffffffffffffffffffffffffffffffffffff)
    0x155a: v155a = AND v1559(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v154e
    0x155d: v155d(0x1) = CONST 
    0x155f: v155f(0x1) = CONST 
    0x1561: v1561(0xa0) = CONST 
    0x1563: v1563(0x10000000000000000000000000000000000000000) = SHL v1561(0xa0), v155f(0x1)
    0x1564: v1564(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1563(0x10000000000000000000000000000000000000000), v155d(0x1)
    0x1565: v1565 = AND v1564(0xffffffffffffffffffffffffffffffffffffffff), v1530
    0x1566: v1566 = MUL v1565, v154c(0x1)
    0x1567: v1567 = OR v1566, v155a
    0x1569: SSTORE v1546, v1567
    0x156c: v156c(0x3a) = CONST 
    0x156e: v156e(0x0) = CONST 
    0x1572: MSTORE v156e(0x0), v4fa
    0x1573: v1573(0x20) = CONST 
    0x1575: v1575(0x20) = ADD v1573(0x20), v156e(0x0)
    0x1578: MSTORE v1575(0x20), v156c(0x3a)
    0x1579: v1579(0x20) = CONST 
    0x157b: v157b(0x40) = ADD v1579(0x20), v1575(0x20)
    0x157c: v157c(0x0) = CONST 
    0x157e: v157e = SHA3 v157c(0x0), v157b(0x40)
    0x157f: v157f(0x1) = CONST 
    0x1581: v1581 = ADD v157f(0x1), v157e
    0x1582: v1582(0x0) = CONST 
    0x1584: v1584(0x100) = CONST 
    0x1587: v1587(0x1) = EXP v1584(0x100), v1582(0x0)
    0x1589: v1589 = SLOAD v1581
    0x158b: v158b(0x1) = CONST 
    0x158d: v158d(0x1) = CONST 
    0x158f: v158f(0xa0) = CONST 
    0x1591: v1591(0x10000000000000000000000000000000000000000) = SHL v158f(0xa0), v158d(0x1)
    0x1592: v1592(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1591(0x10000000000000000000000000000000000000000), v158b(0x1)
    0x1593: v1593(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1592(0xffffffffffffffffffffffffffffffffffffffff), v1587(0x1)
    0x1594: v1594(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1593(0xffffffffffffffffffffffffffffffffffffffff)
    0x1595: v1595 = AND v1594(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1589
    0x1598: v1598(0x1) = CONST 
    0x159a: v159a(0x1) = CONST 
    0x159c: v159c(0xa0) = CONST 
    0x159e: v159e(0x10000000000000000000000000000000000000000) = SHL v159c(0xa0), v159a(0x1)
    0x159f: v159f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v159e(0x10000000000000000000000000000000000000000), v1598(0x1)
    0x15a0: v15a0 = AND v159f(0xffffffffffffffffffffffffffffffffffffffff), v139f
    0x15a1: v15a1 = MUL v15a0, v1587(0x1)
    0x15a2: v15a2 = OR v15a1, v1595
    0x15a4: SSTORE v1581, v15a2
    0x15a8: v15a8(0x2) = CONST 
    0x15aa: v15aa = ADD v15a8(0x2), v116a
    0x15ab: v15ab(0x0) = CONST 
    0x15ae: v15ae = SLOAD v15aa
    0x15b0: v15b0(0x100) = CONST 
    0x15b3: v15b3(0x1) = EXP v15b0(0x100), v15ab(0x0)
    0x15b5: v15b5 = DIV v15ae, v15b3(0x1)
    0x15b6: v15b6(0x1) = CONST 
    0x15b8: v15b8(0x1) = CONST 
    0x15ba: v15ba(0xa0) = CONST 
    0x15bc: v15bc(0x10000000000000000000000000000000000000000) = SHL v15ba(0xa0), v15b8(0x1)
    0x15bd: v15bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15bc(0x10000000000000000000000000000000000000000), v15b6(0x1)
    0x15be: v15be = AND v15bd(0xffffffffffffffffffffffffffffffffffffffff), v15b5
    0x15bf: v15bf(0x1) = CONST 
    0x15c1: v15c1(0x1) = CONST 
    0x15c3: v15c3(0xa0) = CONST 
    0x15c5: v15c5(0x10000000000000000000000000000000000000000) = SHL v15c3(0xa0), v15c1(0x1)
    0x15c6: v15c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15c5(0x10000000000000000000000000000000000000000), v15bf(0x1)
    0x15c7: v15c7 = AND v15c6(0xffffffffffffffffffffffffffffffffffffffff), v15be
    0x15c8: v15c8(0x25bd9222921fd6501d87587a6a3ebd3574ff91be284fecfb29ee6a84c69b005a) = CONST 
    0x15ea: v15ea(0x0) = CONST 
    0x15ec: v15ec = ADD v15ea(0x0), v116a
    0x15ed: v15ed(0x0) = CONST 
    0x15f0: v15f0 = SLOAD v15ec
    0x15f2: v15f2(0x100) = CONST 
    0x15f5: v15f5(0x1) = EXP v15f2(0x100), v15ed(0x0)
    0x15f7: v15f7 = DIV v15f0, v15f5(0x1)
    0x15f8: v15f8(0x1) = CONST 
    0x15fa: v15fa(0x1) = CONST 
    0x15fc: v15fc(0xa0) = CONST 
    0x15fe: v15fe(0x10000000000000000000000000000000000000000) = SHL v15fc(0xa0), v15fa(0x1)
    0x15ff: v15ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15fe(0x10000000000000000000000000000000000000000), v15f8(0x1)
    0x1600: v1600 = AND v15ff(0xffffffffffffffffffffffffffffffffffffffff), v15f7
    0x1602: v1602(0x1) = CONST 
    0x1604: v1604 = ADD v1602(0x1), v116a
    0x1605: v1605(0x0) = CONST 
    0x1608: v1608 = SLOAD v1604
    0x160a: v160a(0x100) = CONST 
    0x160d: v160d(0x1) = EXP v160a(0x100), v1605(0x0)
    0x160f: v160f = DIV v1608, v160d(0x1)
    0x1610: v1610(0x1) = CONST 
    0x1612: v1612(0x1) = CONST 
    0x1614: v1614(0xa0) = CONST 
    0x1616: v1616(0x10000000000000000000000000000000000000000) = SHL v1614(0xa0), v1612(0x1)
    0x1617: v1617(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1616(0x10000000000000000000000000000000000000000), v1610(0x1)
    0x1618: v1618 = AND v1617(0xffffffffffffffffffffffffffffffffffffffff), v160f
    0x161a: v161a(0x3) = CONST 
    0x161c: v161c = ADD v161a(0x3), v116a
    0x161d: v161d(0x0) = CONST 
    0x1620: v1620 = SLOAD v161c
    0x1622: v1622(0x100) = CONST 
    0x1625: v1625(0x1) = EXP v1622(0x100), v161d(0x0)
    0x1627: v1627 = DIV v1620, v1625(0x1)
    0x1628: v1628(0x1) = CONST 
    0x162a: v162a(0x1) = CONST 
    0x162c: v162c(0xa0) = CONST 
    0x162e: v162e(0x10000000000000000000000000000000000000000) = SHL v162c(0xa0), v162a(0x1)
    0x162f: v162f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v162e(0x10000000000000000000000000000000000000000), v1628(0x1)
    0x1630: v1630 = AND v162f(0xffffffffffffffffffffffffffffffffffffffff), v1627
    0x1631: v1631(0x40) = CONST 
    0x1633: v1633 = MLOAD v1631(0x40)
    0x1636: v1636(0x1) = CONST 
    0x1638: v1638(0x1) = CONST 
    0x163a: v163a(0xa0) = CONST 
    0x163c: v163c(0x10000000000000000000000000000000000000000) = SHL v163a(0xa0), v1638(0x1)
    0x163d: v163d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v163c(0x10000000000000000000000000000000000000000), v1636(0x1)
    0x163e: v163e = AND v163d(0xffffffffffffffffffffffffffffffffffffffff), v1600
    0x163f: v163f(0x1) = CONST 
    0x1641: v1641(0x1) = CONST 
    0x1643: v1643(0xa0) = CONST 
    0x1645: v1645(0x10000000000000000000000000000000000000000) = SHL v1643(0xa0), v1641(0x1)
    0x1646: v1646(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1645(0x10000000000000000000000000000000000000000), v163f(0x1)
    0x1647: v1647 = AND v1646(0xffffffffffffffffffffffffffffffffffffffff), v163e
    0x1649: MSTORE v1633, v1647
    0x164a: v164a(0x20) = CONST 
    0x164c: v164c = ADD v164a(0x20), v1633
    0x164e: v164e(0x1) = CONST 
    0x1650: v1650(0x1) = CONST 
    0x1652: v1652(0xa0) = CONST 
    0x1654: v1654(0x10000000000000000000000000000000000000000) = SHL v1652(0xa0), v1650(0x1)
    0x1655: v1655(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1654(0x10000000000000000000000000000000000000000), v164e(0x1)
    0x1656: v1656 = AND v1655(0xffffffffffffffffffffffffffffffffffffffff), v1618
    0x1657: v1657(0x1) = CONST 
    0x1659: v1659(0x1) = CONST 
    0x165b: v165b(0xa0) = CONST 
    0x165d: v165d(0x10000000000000000000000000000000000000000) = SHL v165b(0xa0), v1659(0x1)
    0x165e: v165e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v165d(0x10000000000000000000000000000000000000000), v1657(0x1)
    0x165f: v165f = AND v165e(0xffffffffffffffffffffffffffffffffffffffff), v1656
    0x1661: MSTORE v164c, v165f
    0x1662: v1662(0x20) = CONST 
    0x1664: v1664 = ADD v1662(0x20), v164c
    0x1666: v1666(0x1) = CONST 
    0x1668: v1668(0x1) = CONST 
    0x166a: v166a(0xa0) = CONST 
    0x166c: v166c(0x10000000000000000000000000000000000000000) = SHL v166a(0xa0), v1668(0x1)
    0x166d: v166d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v166c(0x10000000000000000000000000000000000000000), v1666(0x1)
    0x166e: v166e = AND v166d(0xffffffffffffffffffffffffffffffffffffffff), v1630
    0x166f: v166f(0x1) = CONST 
    0x1671: v1671(0x1) = CONST 
    0x1673: v1673(0xa0) = CONST 
    0x1675: v1675(0x10000000000000000000000000000000000000000) = SHL v1673(0xa0), v1671(0x1)
    0x1676: v1676(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1675(0x10000000000000000000000000000000000000000), v166f(0x1)
    0x1677: v1677 = AND v1676(0xffffffffffffffffffffffffffffffffffffffff), v166e
    0x1679: MSTORE v1664, v1677
    0x167a: v167a(0x20) = CONST 
    0x167c: v167c = ADD v167a(0x20), v1664
    0x1682: v1682(0x40) = CONST 
    0x1684: v1684 = MLOAD v1682(0x40)
    0x1687: v1687(0x60) = SUB v167c, v1684
    0x1689: LOG3 v1684, v1687(0x60), v15c8(0x25bd9222921fd6501d87587a6a3ebd3574ff91be284fecfb29ee6a84c69b005a), v15c7, v4fa

}

function raise(bytes32)() public {
    Begin block 0x541
    prev=[], succ=[0x553, 0x557]
    =================================
    0x542: v542(0x55e) = CONST 
    0x545: v545(0x4) = CONST 
    0x548: v548 = CALLDATASIZE 
    0x549: v549 = SUB v548, v545(0x4)
    0x54a: v54a(0x20) = CONST 
    0x54d: v54d = LT v549, v54a(0x20)
    0x54e: v54e = ISZERO v54d
    0x54f: v54f(0x557) = CONST 
    0x552: JUMPI v54f(0x557), v54e

    Begin block 0x553
    prev=[0x541], succ=[]
    =================================
    0x553: v553(0x0) = CONST 
    0x556: REVERT v553(0x0), v553(0x0)

    Begin block 0x557
    prev=[0x541], succ=[0x1699]
    =================================
    0x559: v559 = CALLDATALOAD v545(0x4)
    0x55a: v55a(0x1699) = CONST 
    0x55d: JUMP v55a(0x1699)

    Begin block 0x1699
    prev=[0x557], succ=[0x55e]
    =================================
    0x169a: v169a(0x3a) = CONST 
    0x169c: v169c(0x20) = CONST 
    0x169e: MSTORE v169c(0x20), v169a(0x3a)
    0x169f: v169f(0x0) = CONST 
    0x16a3: MSTORE v169f(0x0), v559
    0x16a4: v16a4(0x40) = CONST 
    0x16a7: v16a7 = SHA3 v169f(0x0), v16a4(0x40)
    0x16a9: v16a9 = SLOAD v16a7
    0x16aa: v16aa(0x1) = CONST 
    0x16ad: v16ad = ADD v16a7, v16aa(0x1)
    0x16ae: v16ae = SLOAD v16ad
    0x16af: v16af(0x2) = CONST 
    0x16b2: v16b2 = ADD v16a7, v16af(0x2)
    0x16b3: v16b3 = SLOAD v16b2
    0x16b4: v16b4(0x3) = CONST 
    0x16b8: v16b8 = ADD v16a7, v16b4(0x3)
    0x16b9: v16b9 = SLOAD v16b8
    0x16ba: v16ba(0x1) = CONST 
    0x16bc: v16bc(0x1) = CONST 
    0x16be: v16be(0xa0) = CONST 
    0x16c0: v16c0(0x10000000000000000000000000000000000000000) = SHL v16be(0xa0), v16bc(0x1)
    0x16c1: v16c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16c0(0x10000000000000000000000000000000000000000), v16ba(0x1)
    0x16c4: v16c4 = AND v16c1(0xffffffffffffffffffffffffffffffffffffffff), v16a9
    0x16c8: v16c8 = AND v16c1(0xffffffffffffffffffffffffffffffffffffffff), v16ae
    0x16cc: v16cc = AND v16c1(0xffffffffffffffffffffffffffffffffffffffff), v16b3
    0x16ce: v16ce = AND v16c1(0xffffffffffffffffffffffffffffffffffffffff), v16b9
    0x16d0: JUMP v542(0x55e)

    Begin block 0x55e
    prev=[0x1699], succ=[]
    =================================
    0x55f: v55f(0x40) = CONST 
    0x562: v562 = MLOAD v55f(0x40)
    0x563: v563(0x1) = CONST 
    0x565: v565(0x1) = CONST 
    0x567: v567(0xa0) = CONST 
    0x569: v569(0x10000000000000000000000000000000000000000) = SHL v567(0xa0), v565(0x1)
    0x56a: v56a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v569(0x10000000000000000000000000000000000000000), v563(0x1)
    0x56d: v56d = AND v56a(0xffffffffffffffffffffffffffffffffffffffff), v16c4
    0x56f: MSTORE v562, v56d
    0x572: v572 = AND v56a(0xffffffffffffffffffffffffffffffffffffffff), v16c8
    0x573: v573(0x20) = CONST 
    0x576: v576 = ADD v562, v573(0x20)
    0x577: MSTORE v576, v572
    0x57a: v57a = AND v56a(0xffffffffffffffffffffffffffffffffffffffff), v16cc
    0x57d: v57d = ADD v55f(0x40), v562
    0x57e: MSTORE v57d, v57a
    0x581: v581 = AND v56a(0xffffffffffffffffffffffffffffffffffffffff), v16ce
    0x582: v582(0x60) = CONST 
    0x585: v585 = ADD v562, v582(0x60)
    0x586: MSTORE v585, v581
    0x588: v588 = MLOAD v55f(0x40)
    0x58c: v58c(0x0) = SUB v562, v588
    0x58d: v58d(0x80) = CONST 
    0x58f: v58f(0x80) = ADD v58d(0x80), v58c(0x0)
    0x591: RETURN v588, v58f(0x80)

}

function updateProxyAdmin(address)() public {
    Begin block 0x592
    prev=[], succ=[0x5a4, 0x5a8]
    =================================
    0x593: v593(0x23b6) = CONST 
    0x596: v596(0x4) = CONST 
    0x599: v599 = CALLDATASIZE 
    0x59a: v59a = SUB v599, v596(0x4)
    0x59b: v59b(0x20) = CONST 
    0x59e: v59e = LT v59a, v59b(0x20)
    0x59f: v59f = ISZERO v59e
    0x5a0: v5a0(0x5a8) = CONST 
    0x5a3: JUMPI v5a0(0x5a8), v59f

    Begin block 0x5a4
    prev=[0x592], succ=[]
    =================================
    0x5a4: v5a4(0x0) = CONST 
    0x5a7: REVERT v5a4(0x0), v5a4(0x0)

    Begin block 0x5a8
    prev=[0x592], succ=[0x16d1]
    =================================
    0x5aa: v5aa = CALLDATALOAD v596(0x4)
    0x5ab: v5ab(0x1) = CONST 
    0x5ad: v5ad(0x1) = CONST 
    0x5af: v5af(0xa0) = CONST 
    0x5b1: v5b1(0x10000000000000000000000000000000000000000) = SHL v5af(0xa0), v5ad(0x1)
    0x5b2: v5b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5b1(0x10000000000000000000000000000000000000000), v5ab(0x1)
    0x5b3: v5b3 = AND v5b2(0xffffffffffffffffffffffffffffffffffffffff), v5aa
    0x5b4: v5b4(0x16d1) = CONST 
    0x5b7: JUMP v5b4(0x16d1)

    Begin block 0x16d1
    prev=[0x5a8], succ=[0x16e4, 0x171a]
    =================================
    0x16d2: v16d2(0x38) = CONST 
    0x16d4: v16d4 = SLOAD v16d2(0x38)
    0x16d5: v16d5(0x1) = CONST 
    0x16d7: v16d7(0x1) = CONST 
    0x16d9: v16d9(0xa0) = CONST 
    0x16db: v16db(0x10000000000000000000000000000000000000000) = SHL v16d9(0xa0), v16d7(0x1)
    0x16dc: v16dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16db(0x10000000000000000000000000000000000000000), v16d5(0x1)
    0x16dd: v16dd = AND v16dc(0xffffffffffffffffffffffffffffffffffffffff), v16d4
    0x16de: v16de = CALLER 
    0x16df: v16df = EQ v16de, v16dd
    0x16e0: v16e0(0x171a) = CONST 
    0x16e3: JUMPI v16e0(0x171a), v16df

    Begin block 0x16e4
    prev=[0x16d1], succ=[]
    =================================
    0x16e4: v16e4(0x40) = CONST 
    0x16e6: v16e6 = MLOAD v16e4(0x40)
    0x16e7: v16e7(0x461bcd) = CONST 
    0x16eb: v16eb(0xe5) = CONST 
    0x16ed: v16ed(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v16eb(0xe5), v16e7(0x461bcd)
    0x16ef: MSTORE v16e6, v16ed(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x16f0: v16f0(0x4) = CONST 
    0x16f2: v16f2 = ADD v16f0(0x4), v16e6
    0x16f5: v16f5(0x20) = CONST 
    0x16f7: v16f7 = ADD v16f5(0x20), v16f2
    0x16fa: v16fa(0x20) = SUB v16f7, v16f2
    0x16fc: MSTORE v16f2, v16fa(0x20)
    0x16fd: v16fd(0x24) = CONST 
    0x1700: MSTORE v16f7, v16fd(0x24)
    0x1701: v1701(0x20) = CONST 
    0x1703: v1703 = ADD v1701(0x20), v16f7
    0x1705: v1705(0x1c69) = CONST 
    0x1708: v1708(0x24) = CONST 
    0x170b: CODECOPY v1703, v1705(0x1c69), v1708(0x24)
    0x170c: v170c(0x40) = CONST 
    0x170e: v170e = ADD v170c(0x40), v1703
    0x1712: v1712(0x40) = CONST 
    0x1714: v1714 = MLOAD v1712(0x40)
    0x1717: v1717(0x84) = SUB v170e, v1714
    0x1719: REVERT v1714, v1717(0x84)

    Begin block 0x171a
    prev=[0x16d1], succ=[0x23b6]
    =================================
    0x171b: v171b(0x38) = CONST 
    0x171e: v171e = SLOAD v171b(0x38)
    0x171f: v171f(0x1) = CONST 
    0x1721: v1721(0x1) = CONST 
    0x1723: v1723(0xa0) = CONST 
    0x1725: v1725(0x10000000000000000000000000000000000000000) = SHL v1723(0xa0), v1721(0x1)
    0x1726: v1726(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1725(0x10000000000000000000000000000000000000000), v171f(0x1)
    0x1727: v1727(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1726(0xffffffffffffffffffffffffffffffffffffffff)
    0x1728: v1728 = AND v1727(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v171e
    0x1729: v1729(0x1) = CONST 
    0x172b: v172b(0x1) = CONST 
    0x172d: v172d(0xa0) = CONST 
    0x172f: v172f(0x10000000000000000000000000000000000000000) = SHL v172d(0xa0), v172b(0x1)
    0x1730: v1730(0xffffffffffffffffffffffffffffffffffffffff) = SUB v172f(0x10000000000000000000000000000000000000000), v1729(0x1)
    0x1733: v1733 = AND v1730(0xffffffffffffffffffffffffffffffffffffffff), v5b3
    0x1737: v1737 = OR v1733, v1728
    0x173b: SSTORE v171b(0x38), v1737
    0x173c: v173c(0x40) = CONST 
    0x173e: v173e = MLOAD v173c(0x40)
    0x1740: v1740 = AND v1737, v1730(0xffffffffffffffffffffffffffffffffffffffff)
    0x1742: v1742(0xfe6d16ecf6ab2a1bb269c55684f6a1b20c1f9a756787689f873061b4d999e76e) = CONST 
    0x1764: v1764(0x0) = CONST 
    0x1767: LOG2 v173e, v1764(0x0), v1742(0xfe6d16ecf6ab2a1bb269c55684f6a1b20c1f9a756787689f873061b4d999e76e), v1740
    0x1769: JUMP v593(0x23b6)

    Begin block 0x23b6
    prev=[0x171a], succ=[]
    =================================
    0x23b7: STOP 

}

function getImplementationAndProxy(bytes32)() public {
    Begin block 0x5b8
    prev=[], succ=[0x5ca, 0x5ce]
    =================================
    0x5b9: v5b9(0x5d5) = CONST 
    0x5bc: v5bc(0x4) = CONST 
    0x5bf: v5bf = CALLDATASIZE 
    0x5c0: v5c0 = SUB v5bf, v5bc(0x4)
    0x5c1: v5c1(0x20) = CONST 
    0x5c4: v5c4 = LT v5c0, v5c1(0x20)
    0x5c5: v5c5 = ISZERO v5c4
    0x5c6: v5c6(0x5ce) = CONST 
    0x5c9: JUMPI v5c6(0x5ce), v5c5

    Begin block 0x5ca
    prev=[0x5b8], succ=[]
    =================================
    0x5ca: v5ca(0x0) = CONST 
    0x5cd: REVERT v5ca(0x0), v5ca(0x0)

    Begin block 0x5ce
    prev=[0x5b8], succ=[0x176a]
    =================================
    0x5d0: v5d0 = CALLDATALOAD v5bc(0x4)
    0x5d1: v5d1(0x176a) = CONST 
    0x5d4: JUMP v5d1(0x176a)

    Begin block 0x176a
    prev=[0x5ce], succ=[0x5d5]
    =================================
    0x176b: v176b(0x0) = CONST 
    0x176f: MSTORE v176b(0x0), v5d0
    0x1770: v1770(0x3a) = CONST 
    0x1772: v1772(0x20) = CONST 
    0x1774: MSTORE v1772(0x20), v1770(0x3a)
    0x1775: v1775(0x40) = CONST 
    0x1778: v1778 = SHA3 v176b(0x0), v1775(0x40)
    0x177a: v177a = SLOAD v1778
    0x177b: v177b(0x1) = CONST 
    0x177f: v177f = ADD v1778, v177b(0x1)
    0x1780: v1780 = SLOAD v177f
    0x1781: v1781(0x1) = CONST 
    0x1783: v1783(0x1) = CONST 
    0x1785: v1785(0xa0) = CONST 
    0x1787: v1787(0x10000000000000000000000000000000000000000) = SHL v1785(0xa0), v1783(0x1)
    0x1788: v1788(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1787(0x10000000000000000000000000000000000000000), v1781(0x1)
    0x178b: v178b = AND v1788(0xffffffffffffffffffffffffffffffffffffffff), v177a
    0x178e: v178e = AND v1788(0xffffffffffffffffffffffffffffffffffffffff), v1780
    0x1790: JUMP v5b9(0x5d5)

    Begin block 0x5d5
    prev=[0x176a], succ=[]
    =================================
    0x5d6: v5d6(0x40) = CONST 
    0x5d9: v5d9 = MLOAD v5d6(0x40)
    0x5da: v5da(0x1) = CONST 
    0x5dc: v5dc(0x1) = CONST 
    0x5de: v5de(0xa0) = CONST 
    0x5e0: v5e0(0x10000000000000000000000000000000000000000) = SHL v5de(0xa0), v5dc(0x1)
    0x5e1: v5e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5e0(0x10000000000000000000000000000000000000000), v5da(0x1)
    0x5e4: v5e4 = AND v5e1(0xffffffffffffffffffffffffffffffffffffffff), v178b
    0x5e6: MSTORE v5d9, v5e4
    0x5ea: v5ea = AND v5e1(0xffffffffffffffffffffffffffffffffffffffff), v178e
    0x5eb: v5eb(0x20) = CONST 
    0x5ee: v5ee = ADD v5d9, v5eb(0x20)
    0x5ef: MSTORE v5ee, v5ea
    0x5f1: v5f1 = MLOAD v5d6(0x40)
    0x5f5: v5f5(0x0) = SUB v5d9, v5f1
    0x5f8: v5f8(0x40) = ADD v5d6(0x40), v5f5(0x0)
    0x5fa: RETURN v5f1, v5f8(0x40)

}

function initialize(address)() public {
    Begin block 0x5fb
    prev=[], succ=[0x60d, 0x611]
    =================================
    0x5fc: v5fc(0x23d7) = CONST 
    0x5ff: v5ff(0x4) = CONST 
    0x602: v602 = CALLDATASIZE 
    0x603: v603 = SUB v602, v5ff(0x4)
    0x604: v604(0x20) = CONST 
    0x607: v607 = LT v603, v604(0x20)
    0x608: v608 = ISZERO v607
    0x609: v609(0x611) = CONST 
    0x60c: JUMPI v609(0x611), v608

    Begin block 0x60d
    prev=[0x5fb], succ=[]
    =================================
    0x60d: v60d(0x0) = CONST 
    0x610: REVERT v60d(0x0), v60d(0x0)

    Begin block 0x611
    prev=[0x5fb], succ=[0x17910x5fb]
    =================================
    0x613: v613 = CALLDATALOAD v5ff(0x4)
    0x614: v614(0x1) = CONST 
    0x616: v616(0x1) = CONST 
    0x618: v618(0xa0) = CONST 
    0x61a: v61a(0x10000000000000000000000000000000000000000) = SHL v618(0xa0), v616(0x1)
    0x61b: v61b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v61a(0x10000000000000000000000000000000000000000), v614(0x1)
    0x61c: v61c = AND v61b(0xffffffffffffffffffffffffffffffffffffffff), v613
    0x61d: v61d(0x1791) = CONST 
    0x620: JUMP v61d(0x1791)

    Begin block 0x17910x5fb
    prev=[0x611], succ=[0x17aa0x5fb, 0x17a20x5fb]
    =================================
    0x17920x5fb: v5fb1792(0x0) = CONST 
    0x17940x5fb: v5fb1794 = SLOAD v5fb1792(0x0)
    0x17950x5fb: v5fb1795(0x100) = CONST 
    0x17990x5fb: v5fb1799 = DIV v5fb1794, v5fb1795(0x100)
    0x179a0x5fb: v5fb179a(0xff) = CONST 
    0x179c0x5fb: v5fb179c = AND v5fb179a(0xff), v5fb1799
    0x179e0x5fb: v5fb179e(0x17aa) = CONST 
    0x17a10x5fb: JUMPI v5fb179e(0x17aa), v5fb179c

    Begin block 0x17aa0x5fb
    prev=[0x17910x5fb, 0x18eeB0x17a20x5fb], succ=[0x17b80x5fb, 0x17b00x5fb]
    =================================
    0x17aa0x5fb_0x0: v17aa5fb_0 = PHI v5fb179c, v18f1V17a25fb
    0x17ac0x5fb: v5fb17ac(0x17b8) = CONST 
    0x17af0x5fb: JUMPI v5fb17ac(0x17b8), v17aa5fb_0

    Begin block 0x17b80x5fb
    prev=[0x17aa0x5fb, 0x17b00x5fb], succ=[0x17bd0x5fb, 0x17f30x5fb]
    =================================
    0x17b80x5fb_0x0: v17b85fb_0 = PHI v5fb17b7, v5fb179c, v18f1V17a25fb
    0x17b90x5fb: v5fb17b9(0x17f3) = CONST 
    0x17bc0x5fb: JUMPI v5fb17b9(0x17f3), v17b85fb_0

    Begin block 0x17bd0x5fb
    prev=[0x17b80x5fb], succ=[]
    =================================
    0x17bd0x5fb: v5fb17bd(0x40) = CONST 
    0x17bf0x5fb: v5fb17bf = MLOAD v5fb17bd(0x40)
    0x17c00x5fb: v5fb17c0(0x461bcd) = CONST 
    0x17c40x5fb: v5fb17c4(0xe5) = CONST 
    0x17c60x5fb: v5fb17c6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5fb17c4(0xe5), v5fb17c0(0x461bcd)
    0x17c80x5fb: MSTORE v5fb17bf, v5fb17c6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17c90x5fb: v5fb17c9(0x4) = CONST 
    0x17cb0x5fb: v5fb17cb = ADD v5fb17c9(0x4), v5fb17bf
    0x17ce0x5fb: v5fb17ce(0x20) = CONST 
    0x17d00x5fb: v5fb17d0 = ADD v5fb17ce(0x20), v5fb17cb
    0x17d30x5fb: v5fb17d3(0x20) = SUB v5fb17d0, v5fb17cb
    0x17d50x5fb: MSTORE v5fb17cb, v5fb17d3(0x20)
    0x17d60x5fb: v5fb17d6(0x3d) = CONST 
    0x17d90x5fb: MSTORE v5fb17d0, v5fb17d6(0x3d)
    0x17da0x5fb: v5fb17da(0x20) = CONST 
    0x17dc0x5fb: v5fb17dc = ADD v5fb17da(0x20), v5fb17d0
    0x17de0x5fb: v5fb17de(0x1cf3) = CONST 
    0x17e10x5fb: v5fb17e1(0x3d) = CONST 
    0x17e40x5fb: CODECOPY v5fb17dc, v5fb17de(0x1cf3), v5fb17e1(0x3d)
    0x17e50x5fb: v5fb17e5(0x40) = CONST 
    0x17e70x5fb: v5fb17e7 = ADD v5fb17e5(0x40), v5fb17dc
    0x17eb0x5fb: v5fb17eb(0x40) = CONST 
    0x17ed0x5fb: v5fb17ed = MLOAD v5fb17eb(0x40)
    0x17f00x5fb: v5fb17f0(0x84) = SUB v5fb17e7, v5fb17ed
    0x17f20x5fb: REVERT v5fb17ed, v5fb17f0(0x84)

    Begin block 0x17f30x5fb
    prev=[0x17b80x5fb], succ=[0x18060x5fb, 0x181e0x5fb]
    =================================
    0x17f40x5fb: v5fb17f4(0x0) = CONST 
    0x17f60x5fb: v5fb17f6 = SLOAD v5fb17f4(0x0)
    0x17f70x5fb: v5fb17f7(0x100) = CONST 
    0x17fb0x5fb: v5fb17fb = DIV v5fb17f6, v5fb17f7(0x100)
    0x17fc0x5fb: v5fb17fc(0xff) = CONST 
    0x17fe0x5fb: v5fb17fe = AND v5fb17fc(0xff), v5fb17fb
    0x17ff0x5fb: v5fb17ff = ISZERO v5fb17fe
    0x18010x5fb: v5fb1801 = ISZERO v5fb17ff
    0x18020x5fb: v5fb1802(0x181e) = CONST 
    0x18050x5fb: JUMPI v5fb1802(0x181e), v5fb1801

    Begin block 0x18060x5fb
    prev=[0x17f30x5fb], succ=[0x181e0x5fb]
    =================================
    0x18060x5fb: v5fb1806(0x0) = CONST 
    0x18090x5fb: v5fb1809 = SLOAD v5fb1806(0x0)
    0x180a0x5fb: v5fb180a(0xff) = CONST 
    0x180c0x5fb: v5fb180c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v5fb180a(0xff)
    0x180d0x5fb: v5fb180d(0xff00) = CONST 
    0x18100x5fb: v5fb1810(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v5fb180d(0xff00)
    0x18130x5fb: v5fb1813 = AND v5fb1809, v5fb1810(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x18140x5fb: v5fb1814(0x100) = CONST 
    0x18170x5fb: v5fb1817 = OR v5fb1814(0x100), v5fb1813
    0x18180x5fb: v5fb1818 = AND v5fb1817, v5fb180c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x18190x5fb: v5fb1819(0x1) = CONST 
    0x181b0x5fb: v5fb181b = OR v5fb1819(0x1), v5fb1818
    0x181d0x5fb: SSTORE v5fb1806(0x0), v5fb181b

    Begin block 0x181e0x5fb
    prev=[0x18060x5fb, 0x17f30x5fb], succ=[0x1985B0x181e0x5fb]
    =================================
    0x181f0x5fb: v5fb181f(0x1827) = CONST 
    0x18230x5fb: v5fb1823(0x1985) = CONST 
    0x18260x5fb: JUMP v5fb1823(0x1985), v61c, v5fb181f(0x1827)

    Begin block 0x1985B0x181e0x5fb
    prev=[0x181e0x5fb], succ=[0x1994B0x181e0x5fb, 0x19caB0x181e0x5fb]
    =================================
    0x1986S0x181e0x5fb: v1986V181e5fb(0x1) = CONST 
    0x1988S0x181e0x5fb: v1988V181e5fb(0x1) = CONST 
    0x198aS0x181e0x5fb: v198aV181e5fb(0xa0) = CONST 
    0x198cS0x181e0x5fb: v198cV181e5fb(0x10000000000000000000000000000000000000000) = SHL v198aV181e5fb(0xa0), v1988V181e5fb(0x1)
    0x198dS0x181e0x5fb: v198dV181e5fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v198cV181e5fb(0x10000000000000000000000000000000000000000), v1986V181e5fb(0x1)
    0x198fS0x181e0x5fb: v198fV181e5fb = AND v61c, v198dV181e5fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x1990S0x181e0x5fb: v1990V181e5fb(0x19ca) = CONST 
    0x1993S0x181e0x5fb: JUMPI v1990V181e5fb(0x19ca), v198fV181e5fb

    Begin block 0x1994B0x181e0x5fb
    prev=[0x1985B0x181e0x5fb], succ=[]
    =================================
    0x1994S0x181e0x5fb: v1994V181e5fb(0x40) = CONST 
    0x1996S0x181e0x5fb: v1996V181e5fb = MLOAD v1994V181e5fb(0x40)
    0x1997S0x181e0x5fb: v1997V181e5fb(0x461bcd) = CONST 
    0x199bS0x181e0x5fb: v199bV181e5fb(0xe5) = CONST 
    0x199dS0x181e0x5fb: v199dV181e5fb(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v199bV181e5fb(0xe5), v1997V181e5fb(0x461bcd)
    0x199fS0x181e0x5fb: MSTORE v1996V181e5fb, v199dV181e5fb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19a0S0x181e0x5fb: v19a0V181e5fb(0x4) = CONST 
    0x19a2S0x181e0x5fb: v19a2V181e5fb = ADD v19a0V181e5fb(0x4), v1996V181e5fb
    0x19a5S0x181e0x5fb: v19a5V181e5fb(0x20) = CONST 
    0x19a7S0x181e0x5fb: v19a7V181e5fb = ADD v19a5V181e5fb(0x20), v19a2V181e5fb
    0x19aaS0x181e0x5fb: v19aaV181e5fb(0x20) = SUB v19a7V181e5fb, v19a2V181e5fb
    0x19acS0x181e0x5fb: MSTORE v19a2V181e5fb, v19aaV181e5fb(0x20)
    0x19adS0x181e0x5fb: v19adV181e5fb(0x3e) = CONST 
    0x19b0S0x181e0x5fb: MSTORE v19a7V181e5fb, v19adV181e5fb(0x3e)
    0x19b1S0x181e0x5fb: v19b1V181e5fb(0x20) = CONST 
    0x19b3S0x181e0x5fb: v19b3V181e5fb = ADD v19b1V181e5fb(0x20), v19a7V181e5fb
    0x19b5S0x181e0x5fb: v19b5V181e5fb(0x1b27) = CONST 
    0x19b8S0x181e0x5fb: v19b8V181e5fb(0x3e) = CONST 
    0x19bbS0x181e0x5fb: CODECOPY v19b3V181e5fb, v19b5V181e5fb(0x1b27), v19b8V181e5fb(0x3e)
    0x19bcS0x181e0x5fb: v19bcV181e5fb(0x40) = CONST 
    0x19beS0x181e0x5fb: v19beV181e5fb = ADD v19bcV181e5fb(0x40), v19b3V181e5fb
    0x19c2S0x181e0x5fb: v19c2V181e5fb(0x40) = CONST 
    0x19c4S0x181e0x5fb: v19c4V181e5fb = MLOAD v19c2V181e5fb(0x40)
    0x19c7S0x181e0x5fb: v19c7V181e5fb(0x84) = SUB v19beV181e5fb, v19c4V181e5fb
    0x19c9S0x181e0x5fb: REVERT v19c4V181e5fb, v19c7V181e5fb(0x84)

    Begin block 0x19caB0x181e0x5fb
    prev=[0x1985B0x181e0x5fb], succ=[0x18270x5fb]
    =================================
    0x19cbS0x181e0x5fb: v19cbV181e5fb(0x33) = CONST 
    0x19ceS0x181e0x5fb: v19ceV181e5fb = SLOAD v19cbV181e5fb(0x33)
    0x19cfS0x181e0x5fb: v19cfV181e5fb(0x1) = CONST 
    0x19d1S0x181e0x5fb: v19d1V181e5fb(0x1) = CONST 
    0x19d3S0x181e0x5fb: v19d3V181e5fb(0xa0) = CONST 
    0x19d5S0x181e0x5fb: v19d5V181e5fb(0x10000000000000000000000000000000000000000) = SHL v19d3V181e5fb(0xa0), v19d1V181e5fb(0x1)
    0x19d6S0x181e0x5fb: v19d6V181e5fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19d5V181e5fb(0x10000000000000000000000000000000000000000), v19cfV181e5fb(0x1)
    0x19d7S0x181e0x5fb: v19d7V181e5fb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v19d6V181e5fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x19d8S0x181e0x5fb: v19d8V181e5fb = AND v19d7V181e5fb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v19ceV181e5fb
    0x19d9S0x181e0x5fb: v19d9V181e5fb(0x1) = CONST 
    0x19dbS0x181e0x5fb: v19dbV181e5fb(0x1) = CONST 
    0x19ddS0x181e0x5fb: v19ddV181e5fb(0xa0) = CONST 
    0x19dfS0x181e0x5fb: v19dfV181e5fb(0x10000000000000000000000000000000000000000) = SHL v19ddV181e5fb(0xa0), v19dbV181e5fb(0x1)
    0x19e0S0x181e0x5fb: v19e0V181e5fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19dfV181e5fb(0x10000000000000000000000000000000000000000), v19d9V181e5fb(0x1)
    0x19e2S0x181e0x5fb: v19e2V181e5fb = AND v61c, v19e0V181e5fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x19e5S0x181e0x5fb: v19e5V181e5fb = OR v19e2V181e5fb, v19d8V181e5fb
    0x19e8S0x181e0x5fb: SSTORE v19cbV181e5fb(0x33), v19e5V181e5fb
    0x19e9S0x181e0x5fb: v19e9V181e5fb(0x40) = CONST 
    0x19ebS0x181e0x5fb: v19ebV181e5fb = MLOAD v19e9V181e5fb(0x40)
    0x19ecS0x181e0x5fb: v19ecV181e5fb = CALLER 
    0x19eeS0x181e0x5fb: v19eeV181e5fb(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e) = CONST 
    0x1a10S0x181e0x5fb: v1a10V181e5fb(0x0) = CONST 
    0x1a13S0x181e0x5fb: LOG3 v19ebV181e5fb, v1a10V181e5fb(0x0), v19eeV181e5fb(0x581e9e5016a25985d2da9da423c68d9946de634ff0e3447eaaa9575d135e819e), v19ecV181e5fb, v19e2V181e5fb
    0x1a15S0x181e0x5fb: JUMP v5fb181f(0x1827)

    Begin block 0x18270x5fb
    prev=[0x19caB0x181e0x5fb], succ=[0x182e0x5fb, 0x18390x5fb]
    =================================
    0x18290x5fb: v5fb1829 = ISZERO v5fb17ff
    0x182a0x5fb: v5fb182a(0x1839) = CONST 
    0x182d0x5fb: JUMPI v5fb182a(0x1839), v5fb1829

    Begin block 0x182e0x5fb
    prev=[0x18270x5fb], succ=[0x18390x5fb]
    =================================
    0x182e0x5fb: v5fb182e(0x0) = CONST 
    0x18310x5fb: v5fb1831 = SLOAD v5fb182e(0x0)
    0x18320x5fb: v5fb1832(0xff00) = CONST 
    0x18350x5fb: v5fb1835(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v5fb1832(0xff00)
    0x18360x5fb: v5fb1836 = AND v5fb1835(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v5fb1831
    0x18380x5fb: SSTORE v5fb182e(0x0), v5fb1836

    Begin block 0x18390x5fb
    prev=[0x182e0x5fb, 0x18270x5fb], succ=[0x23d7]
    =================================
    0x183c0x5fb: JUMP v5fc(0x23d7)

    Begin block 0x23d7
    prev=[0x18390x5fb], succ=[]
    =================================
    0x23d8: STOP 

    Begin block 0x17b00x5fb
    prev=[0x17aa0x5fb], succ=[0x17b80x5fb]
    =================================
    0x17b10x5fb: v5fb17b1(0x0) = CONST 
    0x17b30x5fb: v5fb17b3 = SLOAD v5fb17b1(0x0)
    0x17b40x5fb: v5fb17b4(0xff) = CONST 
    0x17b60x5fb: v5fb17b6 = AND v5fb17b4(0xff), v5fb17b3
    0x17b70x5fb: v5fb17b7 = ISZERO v5fb17b6

    Begin block 0x17a20x5fb
    prev=[0x17910x5fb], succ=[0x18eeB0x17a20x5fb]
    =================================
    0x17a30x5fb: v5fb17a3(0x17aa) = CONST 
    0x17a60x5fb: v5fb17a6(0x18ee) = CONST 
    0x17a90x5fb: JUMP v5fb17a6(0x18ee)

    Begin block 0x18eeB0x17a20x5fb
    prev=[0x17a20x5fb], succ=[0x17aa0x5fb]
    =================================
    0x18efS0x17a20x5fb: v18efV17a25fb = ADDRESS 
    0x18f0S0x17a20x5fb: v18f0V17a25fb = EXTCODESIZE v18efV17a25fb
    0x18f1S0x17a20x5fb: v18f1V17a25fb = ISZERO v18f0V17a25fb
    0x18f3S0x17a20x5fb: JUMP v5fb17a3(0x17aa)

}

function getRaiseOperatorsPending()() public {
    Begin block 0x621
    prev=[], succ=[0x183d]
    =================================
    0x622: v622(0x23f8) = CONST 
    0x625: v625(0x183d) = CONST 
    0x628: JUMP v625(0x183d)

    Begin block 0x183d
    prev=[0x621], succ=[0x23f8]
    =================================
    0x183e: v183e(0x36) = CONST 
    0x1840: v1840 = SLOAD v183e(0x36)
    0x1841: v1841(0x1) = CONST 
    0x1843: v1843(0x1) = CONST 
    0x1845: v1845(0xa0) = CONST 
    0x1847: v1847(0x10000000000000000000000000000000000000000) = SHL v1845(0xa0), v1843(0x1)
    0x1848: v1848(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1847(0x10000000000000000000000000000000000000000), v1841(0x1)
    0x1849: v1849 = AND v1848(0xffffffffffffffffffffffffffffffffffffffff), v1840
    0x184b: JUMP v622(0x23f8)

    Begin block 0x23f8
    prev=[0x183d], succ=[]
    =================================
    0x23f9: v23f9(0x40) = CONST 
    0x23fc: v23fc = MLOAD v23f9(0x40)
    0x23fd: v23fd(0x1) = CONST 
    0x23ff: v23ff(0x1) = CONST 
    0x2401: v2401(0xa0) = CONST 
    0x2403: v2403(0x10000000000000000000000000000000000000000) = SHL v2401(0xa0), v23ff(0x1)
    0x2404: v2404(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2403(0x10000000000000000000000000000000000000000), v23fd(0x1)
    0x2407: v2407 = AND v1849, v2404(0xffffffffffffffffffffffffffffffffffffffff)
    0x2409: MSTORE v23fc, v2407
    0x240a: v240a = MLOAD v23f9(0x40)
    0x240e: v240e(0x0) = SUB v23fc, v240a
    0x240f: v240f(0x20) = CONST 
    0x2411: v2411(0x20) = ADD v240f(0x20), v240e(0x0)
    0x2413: RETURN v240a, v2411(0x20)

}

function isInvestor(address)() public {
    Begin block 0x629
    prev=[], succ=[0x63b, 0x63f]
    =================================
    0x62a: v62a(0x2433) = CONST 
    0x62d: v62d(0x4) = CONST 
    0x630: v630 = CALLDATASIZE 
    0x631: v631 = SUB v630, v62d(0x4)
    0x632: v632(0x20) = CONST 
    0x635: v635 = LT v631, v632(0x20)
    0x636: v636 = ISZERO v635
    0x637: v637(0x63f) = CONST 
    0x63a: JUMPI v637(0x63f), v636

    Begin block 0x63b
    prev=[0x629], succ=[]
    =================================
    0x63b: v63b(0x0) = CONST 
    0x63e: REVERT v63b(0x0), v63b(0x0)

    Begin block 0x63f
    prev=[0x629], succ=[0x184c]
    =================================
    0x641: v641 = CALLDATALOAD v62d(0x4)
    0x642: v642(0x1) = CONST 
    0x644: v644(0x1) = CONST 
    0x646: v646(0xa0) = CONST 
    0x648: v648(0x10000000000000000000000000000000000000000) = SHL v646(0xa0), v644(0x1)
    0x649: v649(0xffffffffffffffffffffffffffffffffffffffff) = SUB v648(0x10000000000000000000000000000000000000000), v642(0x1)
    0x64a: v64a = AND v649(0xffffffffffffffffffffffffffffffffffffffff), v641
    0x64b: v64b(0x184c) = CONST 
    0x64e: JUMP v64b(0x184c)

    Begin block 0x184c
    prev=[0x63f], succ=[0x1899, 0xa400x629]
    =================================
    0x184d: v184d(0x35) = CONST 
    0x184f: v184f = SLOAD v184d(0x35)
    0x1850: v1850(0x40) = CONST 
    0x1853: v1853 = MLOAD v1850(0x40)
    0x1854: v1854(0xcee2a9cf) = CONST 
    0x1859: v1859(0xe0) = CONST 
    0x185b: v185b(0xcee2a9cf00000000000000000000000000000000000000000000000000000000) = SHL v1859(0xe0), v1854(0xcee2a9cf)
    0x185d: MSTORE v1853, v185b(0xcee2a9cf00000000000000000000000000000000000000000000000000000000)
    0x185e: v185e(0x1) = CONST 
    0x1860: v1860(0x1) = CONST 
    0x1862: v1862(0xa0) = CONST 
    0x1864: v1864(0x10000000000000000000000000000000000000000) = SHL v1862(0xa0), v1860(0x1)
    0x1865: v1865(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1864(0x10000000000000000000000000000000000000000), v185e(0x1)
    0x1868: v1868 = AND v1865(0xffffffffffffffffffffffffffffffffffffffff), v64a
    0x1869: v1869(0x4) = CONST 
    0x186c: v186c = ADD v1853, v1869(0x4)
    0x186d: MSTORE v186c, v1868
    0x186f: v186f = MLOAD v1850(0x40)
    0x1870: v1870(0x0) = CONST 
    0x1876: v1876 = AND v184f, v1865(0xffffffffffffffffffffffffffffffffffffffff)
    0x1878: v1878(0xcee2a9cf) = CONST 
    0x187e: v187e(0x24) = CONST 
    0x1882: v1882 = ADD v1853, v187e(0x24)
    0x1884: v1884(0x20) = CONST 
    0x188c: v188c(0x0) = SUB v1853, v186f
    0x188d: v188d(0x24) = ADD v188c(0x0), v187e(0x24)
    0x1891: v1891 = EXTCODESIZE v1876
    0x1892: v1892 = ISZERO v1891
    0x1894: v1894 = ISZERO v1892
    0x1895: v1895(0xa40) = CONST 
    0x1898: JUMPI v1895(0xa40), v1894

    Begin block 0x1899
    prev=[0x184c], succ=[]
    =================================
    0x1899: v1899(0x0) = CONST 
    0x189c: REVERT v1899(0x0), v1899(0x0)

    Begin block 0xa400x629
    prev=[0x184c], succ=[0xa4b0x629, 0xa540x629]
    =================================
    0xa420x629: v629a42 = GAS 
    0xa430x629: v629a43 = STATICCALL v629a42, v1876, v186f, v188d(0x24), v186f, v1884(0x20)
    0xa440x629: v629a44 = ISZERO v629a43
    0xa460x629: v629a46 = ISZERO v629a44
    0xa470x629: v629a47(0xa54) = CONST 
    0xa4a0x629: JUMPI v629a47(0xa54), v629a46

    Begin block 0xa4b0x629
    prev=[0xa400x629], succ=[]
    =================================
    0xa4b0x629: v629a4b = RETURNDATASIZE 
    0xa4c0x629: v629a4c(0x0) = CONST 
    0xa4f0x629: RETURNDATACOPY v629a4c(0x0), v629a4c(0x0), v629a4b
    0xa500x629: v629a50 = RETURNDATASIZE 
    0xa510x629: v629a51(0x0) = CONST 
    0xa530x629: REVERT v629a51(0x0), v629a50

    Begin block 0xa540x629
    prev=[0xa400x629], succ=[0xa660x629, 0xa6a0x629]
    =================================
    0xa590x629: v629a59(0x40) = CONST 
    0xa5b0x629: v629a5b = MLOAD v629a59(0x40)
    0xa5c0x629: v629a5c = RETURNDATASIZE 
    0xa5d0x629: v629a5d(0x20) = CONST 
    0xa600x629: v629a60 = LT v629a5c, v629a5d(0x20)
    0xa610x629: v629a61 = ISZERO v629a60
    0xa620x629: v629a62(0xa6a) = CONST 
    0xa650x629: JUMPI v629a62(0xa6a), v629a61

    Begin block 0xa660x629
    prev=[0xa540x629], succ=[]
    =================================
    0xa660x629: v629a66(0x0) = CONST 
    0xa690x629: REVERT v629a66(0x0), v629a66(0x0)

    Begin block 0xa6a0x629
    prev=[0xa540x629], succ=[0x2433]
    =================================
    0xa6c0x629: v629a6c = MLOAD v629a5b
    0xa710x629: JUMP v62a(0x2433)

    Begin block 0x2433
    prev=[0xa6a0x629], succ=[]
    =================================
    0x2434: v2434(0x40) = CONST 
    0x2437: v2437 = MLOAD v2434(0x40)
    0x2439: v2439 = ISZERO v629a6c
    0x243a: v243a = ISZERO v2439
    0x243c: MSTORE v2437, v243a
    0x243d: v243d = MLOAD v2434(0x40)
    0x2441: v2441(0x0) = SUB v2437, v243d
    0x2442: v2442(0x20) = CONST 
    0x2444: v2444(0x20) = ADD v2442(0x20), v2441(0x0)
    0x2446: RETURN v243d, v2444(0x20)

}

function isAdminOrSystem(address)() public {
    Begin block 0x64f
    prev=[], succ=[0x661, 0x665]
    =================================
    0x650: v650(0x2466) = CONST 
    0x653: v653(0x4) = CONST 
    0x656: v656 = CALLDATASIZE 
    0x657: v657 = SUB v656, v653(0x4)
    0x658: v658(0x20) = CONST 
    0x65b: v65b = LT v657, v658(0x20)
    0x65c: v65c = ISZERO v65b
    0x65d: v65d(0x665) = CONST 
    0x660: JUMPI v65d(0x665), v65c

    Begin block 0x661
    prev=[0x64f], succ=[]
    =================================
    0x661: v661(0x0) = CONST 
    0x664: REVERT v661(0x0), v661(0x0)

    Begin block 0x665
    prev=[0x64f], succ=[0x189d]
    =================================
    0x667: v667 = CALLDATALOAD v653(0x4)
    0x668: v668(0x1) = CONST 
    0x66a: v66a(0x1) = CONST 
    0x66c: v66c(0xa0) = CONST 
    0x66e: v66e(0x10000000000000000000000000000000000000000) = SHL v66c(0xa0), v66a(0x1)
    0x66f: v66f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v66e(0x10000000000000000000000000000000000000000), v668(0x1)
    0x670: v670 = AND v66f(0xffffffffffffffffffffffffffffffffffffffff), v667
    0x671: v671(0x189d) = CONST 
    0x674: JUMP v671(0x189d)

    Begin block 0x189d
    prev=[0x665], succ=[0x18ea, 0xb140x64f]
    =================================
    0x189e: v189e(0x33) = CONST 
    0x18a0: v18a0 = SLOAD v189e(0x33)
    0x18a1: v18a1(0x40) = CONST 
    0x18a4: v18a4 = MLOAD v18a1(0x40)
    0x18a5: v18a5(0x935e01b) = CONST 
    0x18aa: v18aa(0xe2) = CONST 
    0x18ac: v18ac(0x24d7806c00000000000000000000000000000000000000000000000000000000) = SHL v18aa(0xe2), v18a5(0x935e01b)
    0x18ae: MSTORE v18a4, v18ac(0x24d7806c00000000000000000000000000000000000000000000000000000000)
    0x18af: v18af(0x1) = CONST 
    0x18b1: v18b1(0x1) = CONST 
    0x18b3: v18b3(0xa0) = CONST 
    0x18b5: v18b5(0x10000000000000000000000000000000000000000) = SHL v18b3(0xa0), v18b1(0x1)
    0x18b6: v18b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18b5(0x10000000000000000000000000000000000000000), v18af(0x1)
    0x18b9: v18b9 = AND v18b6(0xffffffffffffffffffffffffffffffffffffffff), v670
    0x18ba: v18ba(0x4) = CONST 
    0x18bd: v18bd = ADD v18a4, v18ba(0x4)
    0x18be: MSTORE v18bd, v18b9
    0x18c0: v18c0 = MLOAD v18a1(0x40)
    0x18c1: v18c1(0x0) = CONST 
    0x18c7: v18c7 = AND v18a0, v18b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x18c9: v18c9(0x24d7806c) = CONST 
    0x18cf: v18cf(0x24) = CONST 
    0x18d3: v18d3 = ADD v18a4, v18cf(0x24)
    0x18d5: v18d5(0x20) = CONST 
    0x18dd: v18dd(0x0) = SUB v18a4, v18c0
    0x18de: v18de(0x24) = ADD v18dd(0x0), v18cf(0x24)
    0x18e2: v18e2 = EXTCODESIZE v18c7
    0x18e3: v18e3 = ISZERO v18e2
    0x18e5: v18e5 = ISZERO v18e3
    0x18e6: v18e6(0xb14) = CONST 
    0x18e9: JUMPI v18e6(0xb14), v18e5

    Begin block 0x18ea
    prev=[0x189d], succ=[]
    =================================
    0x18ea: v18ea(0x0) = CONST 
    0x18ed: REVERT v18ea(0x0), v18ea(0x0)

    Begin block 0xb140x64f
    prev=[0x189d], succ=[0xb1f0x64f, 0xb280x64f]
    =================================
    0xb160x64f: v64fb16 = GAS 
    0xb170x64f: v64fb17 = STATICCALL v64fb16, v18c7, v18c0, v18de(0x24), v18c0, v18d5(0x20)
    0xb180x64f: v64fb18 = ISZERO v64fb17
    0xb1a0x64f: v64fb1a = ISZERO v64fb18
    0xb1b0x64f: v64fb1b(0xb28) = CONST 
    0xb1e0x64f: JUMPI v64fb1b(0xb28), v64fb1a

    Begin block 0xb1f0x64f
    prev=[0xb140x64f], succ=[]
    =================================
    0xb1f0x64f: v64fb1f = RETURNDATASIZE 
    0xb200x64f: v64fb20(0x0) = CONST 
    0xb230x64f: RETURNDATACOPY v64fb20(0x0), v64fb20(0x0), v64fb1f
    0xb240x64f: v64fb24 = RETURNDATASIZE 
    0xb250x64f: v64fb25(0x0) = CONST 
    0xb270x64f: REVERT v64fb25(0x0), v64fb24

    Begin block 0xb280x64f
    prev=[0xb140x64f], succ=[0xb3a0x64f, 0xb3e0x64f]
    =================================
    0xb2d0x64f: v64fb2d(0x40) = CONST 
    0xb2f0x64f: v64fb2f = MLOAD v64fb2d(0x40)
    0xb300x64f: v64fb30 = RETURNDATASIZE 
    0xb310x64f: v64fb31(0x20) = CONST 
    0xb340x64f: v64fb34 = LT v64fb30, v64fb31(0x20)
    0xb350x64f: v64fb35 = ISZERO v64fb34
    0xb360x64f: v64fb36(0xb3e) = CONST 
    0xb390x64f: JUMPI v64fb36(0xb3e), v64fb35

    Begin block 0xb3a0x64f
    prev=[0xb280x64f], succ=[]
    =================================
    0xb3a0x64f: v64fb3a(0x0) = CONST 
    0xb3d0x64f: REVERT v64fb3a(0x0), v64fb3a(0x0)

    Begin block 0xb3e0x64f
    prev=[0xb280x64f], succ=[0xb460x64f, 0xb930x64f]
    =================================
    0xb400x64f: v64fb40 = MLOAD v64fb2f
    0xb420x64f: v64fb42(0xb93) = CONST 
    0xb450x64f: JUMPI v64fb42(0xb93), v64fb40

    Begin block 0xb460x64f
    prev=[0xb3e0x64f], succ=[0xb8f0x64f, 0xa400x64f]
    =================================
    0xb470x64f: v64fb47(0x33) = CONST 
    0xb490x64f: v64fb49 = SLOAD v64fb47(0x33)
    0xb4a0x64f: v64fb4a(0x40) = CONST 
    0xb4d0x64f: v64fb4d = MLOAD v64fb4a(0x40)
    0xb4e0x64f: v64fb4e(0x1a66e793) = CONST 
    0xb530x64f: v64fb53(0xe1) = CONST 
    0xb550x64f: v64fb55(0x34cdcf2600000000000000000000000000000000000000000000000000000000) = SHL v64fb53(0xe1), v64fb4e(0x1a66e793)
    0xb570x64f: MSTORE v64fb4d, v64fb55(0x34cdcf2600000000000000000000000000000000000000000000000000000000)
    0xb580x64f: v64fb58(0x1) = CONST 
    0xb5a0x64f: v64fb5a(0x1) = CONST 
    0xb5c0x64f: v64fb5c(0xa0) = CONST 
    0xb5e0x64f: v64fb5e(0x10000000000000000000000000000000000000000) = SHL v64fb5c(0xa0), v64fb5a(0x1)
    0xb5f0x64f: v64fb5f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64fb5e(0x10000000000000000000000000000000000000000), v64fb58(0x1)
    0xb620x64f: v64fb62 = AND v64fb5f(0xffffffffffffffffffffffffffffffffffffffff), v670
    0xb630x64f: v64fb63(0x4) = CONST 
    0xb660x64f: v64fb66 = ADD v64fb4d, v64fb63(0x4)
    0xb670x64f: MSTORE v64fb66, v64fb62
    0xb690x64f: v64fb69 = MLOAD v64fb4a(0x40)
    0xb6d0x64f: v64fb6d = AND v64fb49, v64fb5f(0xffffffffffffffffffffffffffffffffffffffff)
    0xb6f0x64f: v64fb6f(0x34cdcf26) = CONST 
    0xb750x64f: v64fb75(0x24) = CONST 
    0xb790x64f: v64fb79 = ADD v64fb4d, v64fb75(0x24)
    0xb7b0x64f: v64fb7b(0x20) = CONST 
    0xb820x64f: v64fb82(0x0) = SUB v64fb4d, v64fb69
    0xb830x64f: v64fb83(0x24) = ADD v64fb82(0x0), v64fb75(0x24)
    0xb870x64f: v64fb87 = EXTCODESIZE v64fb6d
    0xb880x64f: v64fb88 = ISZERO v64fb87
    0xb8a0x64f: v64fb8a = ISZERO v64fb88
    0xb8b0x64f: v64fb8b(0xa40) = CONST 
    0xb8e0x64f: JUMPI v64fb8b(0xa40), v64fb8a

    Begin block 0xb8f0x64f
    prev=[0xb460x64f], succ=[]
    =================================
    0xb8f0x64f: v64fb8f(0x0) = CONST 
    0xb920x64f: REVERT v64fb8f(0x0), v64fb8f(0x0)

    Begin block 0xa400x64f
    prev=[0xb460x64f], succ=[0xa4b0x64f, 0xa540x64f]
    =================================
    0xa420x64f: v64fa42 = GAS 
    0xa430x64f: v64fa43 = STATICCALL v64fa42, v64fb6d, v64fb69, v64fb83(0x24), v64fb69, v64fb7b(0x20)
    0xa440x64f: v64fa44 = ISZERO v64fa43
    0xa460x64f: v64fa46 = ISZERO v64fa44
    0xa470x64f: v64fa47(0xa54) = CONST 
    0xa4a0x64f: JUMPI v64fa47(0xa54), v64fa46

    Begin block 0xa4b0x64f
    prev=[0xa400x64f], succ=[]
    =================================
    0xa4b0x64f: v64fa4b = RETURNDATASIZE 
    0xa4c0x64f: v64fa4c(0x0) = CONST 
    0xa4f0x64f: RETURNDATACOPY v64fa4c(0x0), v64fa4c(0x0), v64fa4b
    0xa500x64f: v64fa50 = RETURNDATASIZE 
    0xa510x64f: v64fa51(0x0) = CONST 
    0xa530x64f: REVERT v64fa51(0x0), v64fa50

    Begin block 0xa540x64f
    prev=[0xa400x64f], succ=[0xa660x64f, 0xa6a0x64f]
    =================================
    0xa590x64f: v64fa59(0x40) = CONST 
    0xa5b0x64f: v64fa5b = MLOAD v64fa59(0x40)
    0xa5c0x64f: v64fa5c = RETURNDATASIZE 
    0xa5d0x64f: v64fa5d(0x20) = CONST 
    0xa600x64f: v64fa60 = LT v64fa5c, v64fa5d(0x20)
    0xa610x64f: v64fa61 = ISZERO v64fa60
    0xa620x64f: v64fa62(0xa6a) = CONST 
    0xa650x64f: JUMPI v64fa62(0xa6a), v64fa61

    Begin block 0xa660x64f
    prev=[0xa540x64f], succ=[]
    =================================
    0xa660x64f: v64fa66(0x0) = CONST 
    0xa690x64f: REVERT v64fa66(0x0), v64fa66(0x0)

    Begin block 0xa6a0x64f
    prev=[0xa540x64f], succ=[0x2466]
    =================================
    0xa6c0x64f: v64fa6c = MLOAD v64fa5b
    0xa710x64f: JUMP v650(0x2466)

    Begin block 0x2466
    prev=[0xa6a0x64f, 0xb930x64f], succ=[]
    =================================
    0x2466_0x0: v2466_0 = PHI v64fb40, v64fa6c
    0x2467: v2467(0x40) = CONST 
    0x246a: v246a = MLOAD v2467(0x40)
    0x246c: v246c = ISZERO v2466_0
    0x246d: v246d = ISZERO v246c
    0x246f: MSTORE v246a, v246d
    0x2470: v2470 = MLOAD v2467(0x40)
    0x2474: v2474(0x0) = SUB v246a, v2470
    0x2475: v2475(0x20) = CONST 
    0x2477: v2477(0x20) = ADD v2475(0x20), v2474(0x0)
    0x2479: RETURN v2470, v2477(0x20)

    Begin block 0xb930x64f
    prev=[0xb3e0x64f], succ=[0x2466]
    =================================
    0xb980x64f: JUMP v650(0x2466)

}

function 0x9ef(0x9efarg0x0, 0x9efarg0x1) private {
    Begin block 0x9ef
    prev=[], succ=[0xa3c0x9ef, 0xa400x9ef]
    =================================
    0x9f0: v9f0(0x33) = CONST 
    0x9f2: v9f2 = SLOAD v9f0(0x33)
    0x9f3: v9f3(0x40) = CONST 
    0x9f6: v9f6 = MLOAD v9f3(0x40)
    0x9f7: v9f7(0x935e01b) = CONST 
    0x9fc: v9fc(0xe2) = CONST 
    0x9fe: v9fe(0x24d7806c00000000000000000000000000000000000000000000000000000000) = SHL v9fc(0xe2), v9f7(0x935e01b)
    0xa00: MSTORE v9f6, v9fe(0x24d7806c00000000000000000000000000000000000000000000000000000000)
    0xa01: va01(0x1) = CONST 
    0xa03: va03(0x1) = CONST 
    0xa05: va05(0xa0) = CONST 
    0xa07: va07(0x10000000000000000000000000000000000000000) = SHL va05(0xa0), va03(0x1)
    0xa08: va08(0xffffffffffffffffffffffffffffffffffffffff) = SUB va07(0x10000000000000000000000000000000000000000), va01(0x1)
    0xa0b: va0b = AND va08(0xffffffffffffffffffffffffffffffffffffffff), v9efarg0
    0xa0c: va0c(0x4) = CONST 
    0xa0f: va0f = ADD v9f6, va0c(0x4)
    0xa10: MSTORE va0f, va0b
    0xa12: va12 = MLOAD v9f3(0x40)
    0xa13: va13(0x0) = CONST 
    0xa19: va19 = AND v9f2, va08(0xffffffffffffffffffffffffffffffffffffffff)
    0xa1b: va1b(0x24d7806c) = CONST 
    0xa21: va21(0x24) = CONST 
    0xa25: va25 = ADD v9f6, va21(0x24)
    0xa27: va27(0x20) = CONST 
    0xa2f: va2f(0x0) = SUB v9f6, va12
    0xa30: va30(0x24) = ADD va2f(0x0), va21(0x24)
    0xa34: va34 = EXTCODESIZE va19
    0xa35: va35 = ISZERO va34
    0xa37: va37 = ISZERO va35
    0xa38: va38(0xa40) = CONST 
    0xa3b: JUMPI va38(0xa40), va37

    Begin block 0xa3c0x9ef
    prev=[0x9ef], succ=[]
    =================================
    0xa3c0x9ef: v9efa3c(0x0) = CONST 
    0xa3f0x9ef: REVERT v9efa3c(0x0), v9efa3c(0x0)

    Begin block 0xa400x9ef
    prev=[0x9ef], succ=[0xa4b0x9ef, 0xa540x9ef]
    =================================
    0xa420x9ef: v9efa42 = GAS 
    0xa430x9ef: v9efa43 = STATICCALL v9efa42, va19, va12, va30(0x24), va12, va27(0x20)
    0xa440x9ef: v9efa44 = ISZERO v9efa43
    0xa460x9ef: v9efa46 = ISZERO v9efa44
    0xa470x9ef: v9efa47(0xa54) = CONST 
    0xa4a0x9ef: JUMPI v9efa47(0xa54), v9efa46

    Begin block 0xa4b0x9ef
    prev=[0xa400x9ef], succ=[]
    =================================
    0xa4b0x9ef: v9efa4b = RETURNDATASIZE 
    0xa4c0x9ef: v9efa4c(0x0) = CONST 
    0xa4f0x9ef: RETURNDATACOPY v9efa4c(0x0), v9efa4c(0x0), v9efa4b
    0xa500x9ef: v9efa50 = RETURNDATASIZE 
    0xa510x9ef: v9efa51(0x0) = CONST 
    0xa530x9ef: REVERT v9efa51(0x0), v9efa50

    Begin block 0xa540x9ef
    prev=[0xa400x9ef], succ=[0xa660x9ef, 0xa6a0x9ef]
    =================================
    0xa590x9ef: v9efa59(0x40) = CONST 
    0xa5b0x9ef: v9efa5b = MLOAD v9efa59(0x40)
    0xa5c0x9ef: v9efa5c = RETURNDATASIZE 
    0xa5d0x9ef: v9efa5d(0x20) = CONST 
    0xa600x9ef: v9efa60 = LT v9efa5c, v9efa5d(0x20)
    0xa610x9ef: v9efa61 = ISZERO v9efa60
    0xa620x9ef: v9efa62(0xa6a) = CONST 
    0xa650x9ef: JUMPI v9efa62(0xa6a), v9efa61

    Begin block 0xa660x9ef
    prev=[0xa540x9ef], succ=[]
    =================================
    0xa660x9ef: v9efa66(0x0) = CONST 
    0xa690x9ef: REVERT v9efa66(0x0), v9efa66(0x0)

    Begin block 0xa6a0x9ef
    prev=[0xa540x9ef], succ=[]
    =================================
    0xa6c0x9ef: v9efa6c = MLOAD v9efa5b
    0xa710x9ef: RETURNPRIVATE v9efarg1, v9efa6c

}

function 0xe53(0xe53arg0x0, 0xe53arg0x1) private {
    Begin block 0xe53
    prev=[], succ=[0xea00xe53, 0xa400xe53]
    =================================
    0xe54: ve54(0x33) = CONST 
    0xe56: ve56 = SLOAD ve54(0x33)
    0xe57: ve57(0x40) = CONST 
    0xe5a: ve5a = MLOAD ve57(0x40)
    0xe5b: ve5b(0x36b87bd7) = CONST 
    0xe60: ve60(0xe1) = CONST 
    0xe62: ve62(0x6d70f7ae00000000000000000000000000000000000000000000000000000000) = SHL ve60(0xe1), ve5b(0x36b87bd7)
    0xe64: MSTORE ve5a, ve62(0x6d70f7ae00000000000000000000000000000000000000000000000000000000)
    0xe65: ve65(0x1) = CONST 
    0xe67: ve67(0x1) = CONST 
    0xe69: ve69(0xa0) = CONST 
    0xe6b: ve6b(0x10000000000000000000000000000000000000000) = SHL ve69(0xa0), ve67(0x1)
    0xe6c: ve6c(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve6b(0x10000000000000000000000000000000000000000), ve65(0x1)
    0xe6f: ve6f = AND ve6c(0xffffffffffffffffffffffffffffffffffffffff), ve53arg0
    0xe70: ve70(0x4) = CONST 
    0xe73: ve73 = ADD ve5a, ve70(0x4)
    0xe74: MSTORE ve73, ve6f
    0xe76: ve76 = MLOAD ve57(0x40)
    0xe77: ve77(0x0) = CONST 
    0xe7d: ve7d = AND ve56, ve6c(0xffffffffffffffffffffffffffffffffffffffff)
    0xe7f: ve7f(0x6d70f7ae) = CONST 
    0xe85: ve85(0x24) = CONST 
    0xe89: ve89 = ADD ve5a, ve85(0x24)
    0xe8b: ve8b(0x20) = CONST 
    0xe93: ve93(0x0) = SUB ve5a, ve76
    0xe94: ve94(0x24) = ADD ve93(0x0), ve85(0x24)
    0xe98: ve98 = EXTCODESIZE ve7d
    0xe99: ve99 = ISZERO ve98
    0xe9b: ve9b = ISZERO ve99
    0xe9c: ve9c(0xa40) = CONST 
    0xe9f: JUMPI ve9c(0xa40), ve9b

    Begin block 0xea00xe53
    prev=[0xe53], succ=[]
    =================================
    0xea00xe53: ve53ea0(0x0) = CONST 
    0xea30xe53: REVERT ve53ea0(0x0), ve53ea0(0x0)

    Begin block 0xa400xe53
    prev=[0xe53], succ=[0xa4b0xe53, 0xa540xe53]
    =================================
    0xa420xe53: ve53a42 = GAS 
    0xa430xe53: ve53a43 = STATICCALL ve53a42, ve7d, ve76, ve94(0x24), ve76, ve8b(0x20)
    0xa440xe53: ve53a44 = ISZERO ve53a43
    0xa460xe53: ve53a46 = ISZERO ve53a44
    0xa470xe53: ve53a47(0xa54) = CONST 
    0xa4a0xe53: JUMPI ve53a47(0xa54), ve53a46

    Begin block 0xa4b0xe53
    prev=[0xa400xe53], succ=[]
    =================================
    0xa4b0xe53: ve53a4b = RETURNDATASIZE 
    0xa4c0xe53: ve53a4c(0x0) = CONST 
    0xa4f0xe53: RETURNDATACOPY ve53a4c(0x0), ve53a4c(0x0), ve53a4b
    0xa500xe53: ve53a50 = RETURNDATASIZE 
    0xa510xe53: ve53a51(0x0) = CONST 
    0xa530xe53: REVERT ve53a51(0x0), ve53a50

    Begin block 0xa540xe53
    prev=[0xa400xe53], succ=[0xa660xe53, 0xa6a0xe53]
    =================================
    0xa590xe53: ve53a59(0x40) = CONST 
    0xa5b0xe53: ve53a5b = MLOAD ve53a59(0x40)
    0xa5c0xe53: ve53a5c = RETURNDATASIZE 
    0xa5d0xe53: ve53a5d(0x20) = CONST 
    0xa600xe53: ve53a60 = LT ve53a5c, ve53a5d(0x20)
    0xa610xe53: ve53a61 = ISZERO ve53a60
    0xa620xe53: ve53a62(0xa6a) = CONST 
    0xa650xe53: JUMPI ve53a62(0xa6a), ve53a61

    Begin block 0xa660xe53
    prev=[0xa540xe53], succ=[]
    =================================
    0xa660xe53: ve53a66(0x0) = CONST 
    0xa690xe53: REVERT ve53a66(0x0), ve53a66(0x0)

    Begin block 0xa6a0xe53
    prev=[0xa540xe53], succ=[]
    =================================
    0xa6c0xe53: ve53a6c = MLOAD ve53a5b
    0xa710xe53: RETURNPRIVATE ve53arg1, ve53a6c

}

