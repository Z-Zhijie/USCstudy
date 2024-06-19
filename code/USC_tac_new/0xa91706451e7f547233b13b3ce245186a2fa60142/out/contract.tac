function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xa0]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0xa0) = CONST 
    0xc: JUMPI v9(0xa0), v8

    Begin block 0xd
    prev=[0x0], succ=[0x64, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x570ca735) = CONST 
    0x19: v19 = GT v14(0x570ca735), v12
    0x1a: v1a(0x64) = CONST 
    0x1d: JUMPI v1a(0x64), v19

    Begin block 0x64
    prev=[0xd], succ=[0x16d8, 0x70]
    =================================
    0x66: v66(0x54d50d4) = CONST 
    0x6b: v6b = EQ v66(0x54d50d4), v12
    0x16cb: v16cb(0x16d8) = CONST 
    0x16cc: JUMPI v16cb(0x16d8), v6b

    Begin block 0x16d8
    prev=[0x64], succ=[]
    =================================
    0x16d9: v16d9(0xac) = CONST 
    0x16da: CALLPRIVATE v16d9(0xac)

    Begin block 0x70
    prev=[0x64], succ=[0x16db, 0x7b]
    =================================
    0x71: v71(0xd358f87) = CONST 
    0x76: v76 = EQ v71(0xd358f87), v12
    0x16cd: v16cd(0x16db) = CONST 
    0x16ce: JUMPI v16cd(0x16db), v76

    Begin block 0x16db
    prev=[0x70], succ=[]
    =================================
    0x16dc: v16dc(0x10f) = CONST 
    0x16dd: CALLPRIVATE v16dc(0x10f)

    Begin block 0x7b
    prev=[0x70], succ=[0x16de, 0x86]
    =================================
    0x7c: v7c(0x149ad8a4) = CONST 
    0x81: v81 = EQ v7c(0x149ad8a4), v12
    0x16cf: v16cf(0x16de) = CONST 
    0x16d0: JUMPI v16cf(0x16de), v81

    Begin block 0x16de
    prev=[0x7b], succ=[]
    =================================
    0x16df: v16df(0x150) = CONST 
    0x16e0: CALLPRIVATE v16df(0x150)

    Begin block 0x86
    prev=[0x7b], succ=[0x16e1, 0x91]
    =================================
    0x87: v87(0x3cdc5389) = CONST 
    0x8c: v8c = EQ v87(0x3cdc5389), v12
    0x16d1: v16d1(0x16e1) = CONST 
    0x16d2: JUMPI v16d1(0x16e1), v8c

    Begin block 0x16e1
    prev=[0x86], succ=[]
    =================================
    0x16e2: v16e2(0x191) = CONST 
    0x16e3: CALLPRIVATE v16e2(0x191)

    Begin block 0x91
    prev=[0x86], succ=[0x9c, 0x16e4]
    =================================
    0x92: v92(0x3fc8cef3) = CONST 
    0x97: v97 = EQ v92(0x3fc8cef3), v12
    0x16d3: v16d3(0x16e4) = CONST 
    0x16d4: JUMPI v16d3(0x16e4), v97

    Begin block 0x9c
    prev=[0x91], succ=[0x1696]
    =================================
    0x9c: v9c(0x1696) = CONST 
    0x9f: JUMP v9c(0x1696)

    Begin block 0x1696
    prev=[0x9c], succ=[]
    =================================
    0x1697: v1697(0x0) = CONST 
    0x169a: REVERT v1697(0x0), v1697(0x0)

    Begin block 0x16e4
    prev=[0x91], succ=[]
    =================================
    0x16e5: v16e5(0x1d2) = CONST 
    0x16e6: CALLPRIVATE v16e5(0x1d2)

    Begin block 0x1e
    prev=[0xd], succ=[0x16e7, 0x29]
    =================================
    0x1f: v1f(0x570ca735) = CONST 
    0x24: v24 = EQ v1f(0x570ca735), v12
    0x16bf: v16bf(0x16e7) = CONST 
    0x16c0: JUMPI v16bf(0x16e7), v24

    Begin block 0x16e7
    prev=[0x1e], succ=[]
    =================================
    0x16e8: v16e8(0x213) = CONST 
    0x16e9: CALLPRIVATE v16e8(0x213)

    Begin block 0x29
    prev=[0x1e], succ=[0x16ea, 0x34]
    =================================
    0x2a: v2a(0x5780101d) = CONST 
    0x2f: v2f = EQ v2a(0x5780101d), v12
    0x16c1: v16c1(0x16ea) = CONST 
    0x16c2: JUMPI v16c1(0x16ea), v2f

    Begin block 0x16ea
    prev=[0x29], succ=[]
    =================================
    0x16eb: v16eb(0x254) = CONST 
    0x16ec: CALLPRIVATE v16eb(0x254)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x16ed]
    =================================
    0x35: v35(0x940a4e45) = CONST 
    0x3a: v3a = EQ v35(0x940a4e45), v12
    0x16c3: v16c3(0x16ed) = CONST 
    0x16c4: JUMPI v16c3(0x16ed), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x16f0, 0x4a]
    =================================
    0x40: v40(0xc4d66de8) = CONST 
    0x45: v45 = EQ v40(0xc4d66de8), v12
    0x16c5: v16c5(0x16f0) = CONST 
    0x16c6: JUMPI v16c5(0x16f0), v45

    Begin block 0x16f0
    prev=[0x3f], succ=[]
    =================================
    0x16f1: v16f1(0x2ea) = CONST 
    0x16f2: CALLPRIVATE v16f1(0x2ea)

    Begin block 0x4a
    prev=[0x3f], succ=[0x16f3, 0x55]
    =================================
    0x4b: v4b(0xcf98a6b7) = CONST 
    0x50: v50 = EQ v4b(0xcf98a6b7), v12
    0x16c7: v16c7(0x16f3) = CONST 
    0x16c8: JUMPI v16c7(0x16f3), v50

    Begin block 0x16f3
    prev=[0x4a], succ=[]
    =================================
    0x16f4: v16f4(0x33b) = CONST 
    0x16f5: CALLPRIVATE v16f4(0x33b)

    Begin block 0x55
    prev=[0x4a], succ=[0x60, 0x16f6]
    =================================
    0x56: v56(0xe9b70dda) = CONST 
    0x5b: v5b = EQ v56(0xe9b70dda), v12
    0x16c9: v16c9(0x16f6) = CONST 
    0x16ca: JUMPI v16c9(0x16f6), v5b

    Begin block 0x60
    prev=[0x55], succ=[0x1672]
    =================================
    0x60: v60(0x1672) = CONST 
    0x63: JUMP v60(0x1672)

    Begin block 0x1672
    prev=[0x60], succ=[]
    =================================
    0x1673: v1673(0x0) = CONST 
    0x1676: REVERT v1673(0x0), v1673(0x0)

    Begin block 0x16f6
    prev=[0x55], succ=[]
    =================================
    0x16f7: v16f7(0x3a0) = CONST 
    0x16f8: CALLPRIVATE v16f7(0x3a0)

    Begin block 0x16ed
    prev=[0x34], succ=[]
    =================================
    0x16ee: v16ee(0x2af) = CONST 
    0x16ef: CALLPRIVATE v16ee(0x2af)

    Begin block 0xa0
    prev=[0x0], succ=[0x16d5, 0x16ba]
    =================================
    0xa1: va1 = CALLDATASIZE 
    0xa2: va2(0x16ba) = CONST 
    0xa5: JUMPI va2(0x16ba), va1

    Begin block 0x16d5
    prev=[0xa0], succ=[]
    =================================
    0x16d5: v16d5(0x16d7) = CONST 
    0x16d6: CALLPRIVATE v16d5(0x16d7)

    Begin block 0x16ba
    prev=[0xa0], succ=[]
    =================================
    0x16bb: v16bb(0x0) = CONST 
    0x16be: REVERT v16bb(0x0), v16bb(0x0)

}

function wbtc_weth_pair()() public {
    Begin block 0x10f
    prev=[], succ=[0x117, 0x11b]
    =================================
    0x110: v110 = CALLVALUE 
    0x112: v112 = ISZERO v110
    0x113: v113(0x11b) = CONST 
    0x116: JUMPI v113(0x11b), v112

    Begin block 0x117
    prev=[0x10f], succ=[]
    =================================
    0x117: v117(0x0) = CONST 
    0x11a: REVERT v117(0x0), v117(0x0)

    Begin block 0x11b
    prev=[0x10f], succ=[0x501]
    =================================
    0x11d: v11d(0x124) = CONST 
    0x120: v120(0x501) = CONST 
    0x123: JUMP v120(0x501)

    Begin block 0x501
    prev=[0x11b], succ=[0x124]
    =================================
    0x502: v502(0x4) = CONST 
    0x504: v504(0x0) = CONST 
    0x507: v507 = SLOAD v502(0x4)
    0x509: v509(0x100) = CONST 
    0x50c: v50c(0x1) = EXP v509(0x100), v504(0x0)
    0x50e: v50e = DIV v507, v50c(0x1)
    0x50f: v50f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x524: v524 = AND v50f(0xffffffffffffffffffffffffffffffffffffffff), v50e
    0x526: JUMP v11d(0x124)

    Begin block 0x124
    prev=[0x501], succ=[]
    =================================
    0x125: v125(0x40) = CONST 
    0x127: v127 = MLOAD v125(0x40)
    0x12a: v12a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13f: v13f = AND v12a(0xffffffffffffffffffffffffffffffffffffffff), v524
    0x141: MSTORE v127, v13f
    0x142: v142(0x20) = CONST 
    0x144: v144 = ADD v142(0x20), v127
    0x148: v148(0x40) = CONST 
    0x14a: v14a = MLOAD v148(0x40)
    0x14d: v14d(0x20) = SUB v144, v14a
    0x14f: RETURN v14a, v14d(0x20)

}

function marsStakingForWbtc()() public {
    Begin block 0x150
    prev=[], succ=[0x158, 0x15c]
    =================================
    0x151: v151 = CALLVALUE 
    0x153: v153 = ISZERO v151
    0x154: v154(0x15c) = CONST 
    0x157: JUMPI v154(0x15c), v153

    Begin block 0x158
    prev=[0x150], succ=[]
    =================================
    0x158: v158(0x0) = CONST 
    0x15b: REVERT v158(0x0), v158(0x0)

    Begin block 0x15c
    prev=[0x150], succ=[0x527]
    =================================
    0x15e: v15e(0x165) = CONST 
    0x161: v161(0x527) = CONST 
    0x164: JUMP v161(0x527)

    Begin block 0x527
    prev=[0x15c], succ=[0x165]
    =================================
    0x528: v528(0x3) = CONST 
    0x52a: v52a(0x0) = CONST 
    0x52d: v52d = SLOAD v528(0x3)
    0x52f: v52f(0x100) = CONST 
    0x532: v532(0x1) = EXP v52f(0x100), v52a(0x0)
    0x534: v534 = DIV v52d, v532(0x1)
    0x535: v535(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x54a: v54a = AND v535(0xffffffffffffffffffffffffffffffffffffffff), v534
    0x54c: JUMP v15e(0x165)

    Begin block 0x165
    prev=[0x527], succ=[]
    =================================
    0x166: v166(0x40) = CONST 
    0x168: v168 = MLOAD v166(0x40)
    0x16b: v16b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x180: v180 = AND v16b(0xffffffffffffffffffffffffffffffffffffffff), v54a
    0x182: MSTORE v168, v180
    0x183: v183(0x20) = CONST 
    0x185: v185 = ADD v183(0x20), v168
    0x189: v189(0x40) = CONST 
    0x18b: v18b = MLOAD v189(0x40)
    0x18e: v18e(0x20) = SUB v185, v18b
    0x190: RETURN v18b, v18e(0x20)

}

function fallback()() public {
    Begin block 0x16d7
    prev=[], succ=[]
    =================================
    0xa6: STOP 

}

function wbtc()() public {
    Begin block 0x191
    prev=[], succ=[0x199, 0x19d]
    =================================
    0x192: v192 = CALLVALUE 
    0x194: v194 = ISZERO v192
    0x195: v195(0x19d) = CONST 
    0x198: JUMPI v195(0x19d), v194

    Begin block 0x199
    prev=[0x191], succ=[]
    =================================
    0x199: v199(0x0) = CONST 
    0x19c: REVERT v199(0x0), v199(0x0)

    Begin block 0x19d
    prev=[0x191], succ=[0x54d]
    =================================
    0x19f: v19f(0x1a6) = CONST 
    0x1a2: v1a2(0x54d) = CONST 
    0x1a5: JUMP v1a2(0x54d)

    Begin block 0x54d
    prev=[0x19d], succ=[0x1a6]
    =================================
    0x54e: v54e(0x1) = CONST 
    0x550: v550(0x0) = CONST 
    0x553: v553 = SLOAD v54e(0x1)
    0x555: v555(0x100) = CONST 
    0x558: v558(0x1) = EXP v555(0x100), v550(0x0)
    0x55a: v55a = DIV v553, v558(0x1)
    0x55b: v55b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x570: v570 = AND v55b(0xffffffffffffffffffffffffffffffffffffffff), v55a
    0x572: JUMP v19f(0x1a6)

    Begin block 0x1a6
    prev=[0x54d], succ=[]
    =================================
    0x1a7: v1a7(0x40) = CONST 
    0x1a9: v1a9 = MLOAD v1a7(0x40)
    0x1ac: v1ac(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c1: v1c1 = AND v1ac(0xffffffffffffffffffffffffffffffffffffffff), v570
    0x1c3: MSTORE v1a9, v1c1
    0x1c4: v1c4(0x20) = CONST 
    0x1c6: v1c6 = ADD v1c4(0x20), v1a9
    0x1ca: v1ca(0x40) = CONST 
    0x1cc: v1cc = MLOAD v1ca(0x40)
    0x1cf: v1cf(0x20) = SUB v1c6, v1cc
    0x1d1: RETURN v1cc, v1cf(0x20)

}

function weth()() public {
    Begin block 0x1d2
    prev=[], succ=[0x1da, 0x1de]
    =================================
    0x1d3: v1d3 = CALLVALUE 
    0x1d5: v1d5 = ISZERO v1d3
    0x1d6: v1d6(0x1de) = CONST 
    0x1d9: JUMPI v1d6(0x1de), v1d5

    Begin block 0x1da
    prev=[0x1d2], succ=[]
    =================================
    0x1da: v1da(0x0) = CONST 
    0x1dd: REVERT v1da(0x0), v1da(0x0)

    Begin block 0x1de
    prev=[0x1d2], succ=[0x573]
    =================================
    0x1e0: v1e0(0x1e7) = CONST 
    0x1e3: v1e3(0x573) = CONST 
    0x1e6: JUMP v1e3(0x573)

    Begin block 0x573
    prev=[0x1de], succ=[0x1e7]
    =================================
    0x574: v574(0x2) = CONST 
    0x576: v576(0x0) = CONST 
    0x579: v579 = SLOAD v574(0x2)
    0x57b: v57b(0x100) = CONST 
    0x57e: v57e(0x1) = EXP v57b(0x100), v576(0x0)
    0x580: v580 = DIV v579, v57e(0x1)
    0x581: v581(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x596: v596 = AND v581(0xffffffffffffffffffffffffffffffffffffffff), v580
    0x598: JUMP v1e0(0x1e7)

    Begin block 0x1e7
    prev=[0x573], succ=[]
    =================================
    0x1e8: v1e8(0x40) = CONST 
    0x1ea: v1ea = MLOAD v1e8(0x40)
    0x1ed: v1ed(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x202: v202 = AND v1ed(0xffffffffffffffffffffffffffffffffffffffff), v596
    0x204: MSTORE v1ea, v202
    0x205: v205(0x20) = CONST 
    0x207: v207 = ADD v205(0x20), v1ea
    0x20b: v20b(0x40) = CONST 
    0x20d: v20d = MLOAD v20b(0x40)
    0x210: v210(0x20) = SUB v207, v20d
    0x212: RETURN v20d, v210(0x20)

}

function operator()() public {
    Begin block 0x213
    prev=[], succ=[0x21b, 0x21f]
    =================================
    0x214: v214 = CALLVALUE 
    0x216: v216 = ISZERO v214
    0x217: v217(0x21f) = CONST 
    0x21a: JUMPI v217(0x21f), v216

    Begin block 0x21b
    prev=[0x213], succ=[]
    =================================
    0x21b: v21b(0x0) = CONST 
    0x21e: REVERT v21b(0x0), v21b(0x0)

    Begin block 0x21f
    prev=[0x213], succ=[0x599]
    =================================
    0x221: v221(0x228) = CONST 
    0x224: v224(0x599) = CONST 
    0x227: JUMP v224(0x599)

    Begin block 0x599
    prev=[0x21f], succ=[0x228]
    =================================
    0x59a: v59a(0x0) = CONST 
    0x59c: v59c(0x1) = CONST 
    0x59f: v59f = SLOAD v59a(0x0)
    0x5a1: v5a1(0x100) = CONST 
    0x5a4: v5a4(0x100) = EXP v5a1(0x100), v59c(0x1)
    0x5a6: v5a6 = DIV v59f, v5a4(0x100)
    0x5a7: v5a7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5bc: v5bc = AND v5a7(0xffffffffffffffffffffffffffffffffffffffff), v5a6
    0x5be: JUMP v221(0x228)

    Begin block 0x228
    prev=[0x599], succ=[]
    =================================
    0x229: v229(0x40) = CONST 
    0x22b: v22b = MLOAD v229(0x40)
    0x22e: v22e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x243: v243 = AND v22e(0xffffffffffffffffffffffffffffffffffffffff), v5bc
    0x245: MSTORE v22b, v243
    0x246: v246(0x20) = CONST 
    0x248: v248 = ADD v246(0x20), v22b
    0x24c: v24c(0x40) = CONST 
    0x24e: v24e = MLOAD v24c(0x40)
    0x251: v251(0x20) = SUB v248, v24e
    0x253: RETURN v24e, v251(0x20)

}

function setLpStakingFeeRate(address,uint256)() public {
    Begin block 0x254
    prev=[], succ=[0x25c, 0x260]
    =================================
    0x255: v255 = CALLVALUE 
    0x257: v257 = ISZERO v255
    0x258: v258(0x260) = CONST 
    0x25b: JUMPI v258(0x260), v257

    Begin block 0x25c
    prev=[0x254], succ=[]
    =================================
    0x25c: v25c(0x0) = CONST 
    0x25f: REVERT v25c(0x0), v25c(0x0)

    Begin block 0x260
    prev=[0x254], succ=[0x273, 0x277]
    =================================
    0x262: v262(0x2ad) = CONST 
    0x265: v265(0x4) = CONST 
    0x268: v268 = CALLDATASIZE 
    0x269: v269 = SUB v268, v265(0x4)
    0x26a: v26a(0x40) = CONST 
    0x26d: v26d = LT v269, v26a(0x40)
    0x26e: v26e = ISZERO v26d
    0x26f: v26f(0x277) = CONST 
    0x272: JUMPI v26f(0x277), v26e

    Begin block 0x273
    prev=[0x260], succ=[]
    =================================
    0x273: v273(0x0) = CONST 
    0x276: REVERT v273(0x0), v273(0x0)

    Begin block 0x277
    prev=[0x260], succ=[0x5bf]
    =================================
    0x279: v279 = ADD v265(0x4), v269
    0x27d: v27d = CALLDATALOAD v265(0x4)
    0x27e: v27e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x293: v293 = AND v27e(0xffffffffffffffffffffffffffffffffffffffff), v27d
    0x295: v295(0x20) = CONST 
    0x297: v297(0x24) = ADD v295(0x20), v265(0x4)
    0x29d: v29d = CALLDATALOAD v297(0x24)
    0x29f: v29f(0x20) = CONST 
    0x2a1: v2a1(0x44) = ADD v29f(0x20), v297(0x24)
    0x2a9: v2a9(0x5bf) = CONST 
    0x2ac: JUMP v2a9(0x5bf)

    Begin block 0x5bf
    prev=[0x277], succ=[0x615, 0x682]
    =================================
    0x5c0: v5c0(0x0) = CONST 
    0x5c2: v5c2(0x1) = CONST 
    0x5c5: v5c5 = SLOAD v5c0(0x0)
    0x5c7: v5c7(0x100) = CONST 
    0x5ca: v5ca(0x100) = EXP v5c7(0x100), v5c2(0x1)
    0x5cc: v5cc = DIV v5c5, v5ca(0x100)
    0x5cd: v5cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5e2: v5e2 = AND v5cd(0xffffffffffffffffffffffffffffffffffffffff), v5cc
    0x5e3: v5e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5f8: v5f8 = AND v5e3(0xffffffffffffffffffffffffffffffffffffffff), v5e2
    0x5f9: v5f9 = CALLER 
    0x5fa: v5fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x60f: v60f = AND v5fa(0xffffffffffffffffffffffffffffffffffffffff), v5f9
    0x610: v610 = EQ v60f, v5f8
    0x611: v611(0x682) = CONST 
    0x614: JUMPI v611(0x682), v610

    Begin block 0x615
    prev=[0x5bf], succ=[]
    =================================
    0x615: v615(0x40) = CONST 
    0x617: v617 = MLOAD v615(0x40)
    0x618: v618(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x63a: MSTORE v617, v618(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x63b: v63b(0x4) = CONST 
    0x63d: v63d = ADD v63b(0x4), v617
    0x640: v640(0x20) = CONST 
    0x642: v642 = ADD v640(0x20), v63d
    0x645: v645(0x20) = SUB v642, v63d
    0x647: MSTORE v63d, v645(0x20)
    0x648: v648(0x9) = CONST 
    0x64b: MSTORE v642, v648(0x9)
    0x64c: v64c(0x20) = CONST 
    0x64e: v64e = ADD v64c(0x20), v642
    0x650: v650(0x216f70657261746f720000000000000000000000000000000000000000000000) = CONST 
    0x672: MSTORE v64e, v650(0x216f70657261746f720000000000000000000000000000000000000000000000)
    0x674: v674(0x20) = CONST 
    0x676: v676 = ADD v674(0x20), v64e
    0x67a: v67a(0x40) = CONST 
    0x67c: v67c = MLOAD v67a(0x40)
    0x67f: v67f(0x64) = SUB v676, v67c
    0x681: REVERT v67c, v67f(0x64)

    Begin block 0x682
    prev=[0x5bf], succ=[0x717, 0x784]
    =================================
    0x683: v683(0x0) = CONST 
    0x685: v685(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x69a: v69a(0x0) = AND v685(0xffffffffffffffffffffffffffffffffffffffff), v683(0x0)
    0x69b: v69b(0x6) = CONST 
    0x69d: v69d(0x0) = CONST 
    0x6a0: v6a0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6b5: v6b5 = AND v6a0(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x6b6: v6b6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6cb: v6cb = AND v6b6(0xffffffffffffffffffffffffffffffffffffffff), v6b5
    0x6cd: MSTORE v69d(0x0), v6cb
    0x6ce: v6ce(0x20) = CONST 
    0x6d0: v6d0(0x20) = ADD v6ce(0x20), v69d(0x0)
    0x6d3: MSTORE v6d0(0x20), v69b(0x6)
    0x6d4: v6d4(0x20) = CONST 
    0x6d6: v6d6(0x40) = ADD v6d4(0x20), v6d0(0x20)
    0x6d7: v6d7(0x0) = CONST 
    0x6d9: v6d9 = SHA3 v6d7(0x0), v6d6(0x40)
    0x6da: v6da(0x0) = CONST 
    0x6dd: v6dd = SLOAD v6d9
    0x6df: v6df(0x100) = CONST 
    0x6e2: v6e2(0x1) = EXP v6df(0x100), v6da(0x0)
    0x6e4: v6e4 = DIV v6dd, v6e2(0x1)
    0x6e5: v6e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6fa: v6fa = AND v6e5(0xffffffffffffffffffffffffffffffffffffffff), v6e4
    0x6fb: v6fb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x710: v710 = AND v6fb(0xffffffffffffffffffffffffffffffffffffffff), v6fa
    0x711: v711 = EQ v710, v69a(0x0)
    0x712: v712 = ISZERO v711
    0x713: v713(0x784) = CONST 
    0x716: JUMPI v713(0x784), v712

    Begin block 0x717
    prev=[0x682], succ=[]
    =================================
    0x717: v717(0x40) = CONST 
    0x719: v719 = MLOAD v717(0x40)
    0x71a: v71a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x73c: MSTORE v719, v71a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x73d: v73d(0x4) = CONST 
    0x73f: v73f = ADD v73d(0x4), v719
    0x742: v742(0x20) = CONST 
    0x744: v744 = ADD v742(0x20), v73f
    0x747: v747(0x20) = SUB v744, v73f
    0x749: MSTORE v73f, v747(0x20)
    0x74a: v74a(0xa) = CONST 
    0x74d: MSTORE v744, v74a(0xa)
    0x74e: v74e(0x20) = CONST 
    0x750: v750 = ADD v74e(0x20), v744
    0x752: v752(0x6e6f742061646465642e00000000000000000000000000000000000000000000) = CONST 
    0x774: MSTORE v750, v752(0x6e6f742061646465642e00000000000000000000000000000000000000000000)
    0x776: v776(0x20) = CONST 
    0x778: v778 = ADD v776(0x20), v750
    0x77c: v77c(0x40) = CONST 
    0x77e: v77e = MLOAD v77c(0x40)
    0x781: v781(0x64) = SUB v778, v77e
    0x783: REVERT v77e, v781(0x64)

    Begin block 0x784
    prev=[0x682], succ=[0x7d3, 0x7d7]
    =================================
    0x786: v786(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x79b: v79b = AND v786(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x79c: v79c(0x45596e2e) = CONST 
    0x7a2: v7a2(0x40) = CONST 
    0x7a4: v7a4 = MLOAD v7a2(0x40)
    0x7a6: v7a6(0xffffffff) = CONST 
    0x7ab: v7ab(0x45596e2e) = AND v7a6(0xffffffff), v79c(0x45596e2e)
    0x7ac: v7ac(0xe0) = CONST 
    0x7ae: v7ae(0x45596e2e00000000000000000000000000000000000000000000000000000000) = SHL v7ac(0xe0), v7ab(0x45596e2e)
    0x7b0: MSTORE v7a4, v7ae(0x45596e2e00000000000000000000000000000000000000000000000000000000)
    0x7b1: v7b1(0x4) = CONST 
    0x7b3: v7b3 = ADD v7b1(0x4), v7a4
    0x7b7: MSTORE v7b3, v29d
    0x7b8: v7b8(0x20) = CONST 
    0x7ba: v7ba = ADD v7b8(0x20), v7b3
    0x7be: v7be(0x0) = CONST 
    0x7c0: v7c0(0x40) = CONST 
    0x7c2: v7c2 = MLOAD v7c0(0x40)
    0x7c5: v7c5(0x24) = SUB v7ba, v7c2
    0x7c7: v7c7(0x0) = CONST 
    0x7cb: v7cb = EXTCODESIZE v79b
    0x7cc: v7cc = ISZERO v7cb
    0x7ce: v7ce = ISZERO v7cc
    0x7cf: v7cf(0x7d7) = CONST 
    0x7d2: JUMPI v7cf(0x7d7), v7ce

    Begin block 0x7d3
    prev=[0x784], succ=[]
    =================================
    0x7d3: v7d3(0x0) = CONST 
    0x7d6: REVERT v7d3(0x0), v7d3(0x0)

    Begin block 0x7d7
    prev=[0x784], succ=[0x7e2, 0x7eb]
    =================================
    0x7d9: v7d9 = GAS 
    0x7da: v7da = CALL v7d9, v79b, v7c7(0x0), v7c2, v7c5(0x24), v7c2, v7be(0x0)
    0x7db: v7db = ISZERO v7da
    0x7dd: v7dd = ISZERO v7db
    0x7de: v7de(0x7eb) = CONST 
    0x7e1: JUMPI v7de(0x7eb), v7dd

    Begin block 0x7e2
    prev=[0x7d7], succ=[]
    =================================
    0x7e2: v7e2 = RETURNDATASIZE 
    0x7e3: v7e3(0x0) = CONST 
    0x7e6: RETURNDATACOPY v7e3(0x0), v7e3(0x0), v7e2
    0x7e7: v7e7 = RETURNDATASIZE 
    0x7e8: v7e8(0x0) = CONST 
    0x7ea: REVERT v7e8(0x0), v7e7

    Begin block 0x7eb
    prev=[0x7d7], succ=[0x2ad]
    =================================
    0x7f2: JUMP v262(0x2ad)

    Begin block 0x2ad
    prev=[0x7eb], succ=[]
    =================================
    0x2ae: STOP 

}

function distributeReward(uint256)() public {
    Begin block 0x2af
    prev=[], succ=[0x2b7, 0x2bb]
    =================================
    0x2b0: v2b0 = CALLVALUE 
    0x2b2: v2b2 = ISZERO v2b0
    0x2b3: v2b3(0x2bb) = CONST 
    0x2b6: JUMPI v2b3(0x2bb), v2b2

    Begin block 0x2b7
    prev=[0x2af], succ=[]
    =================================
    0x2b7: v2b7(0x0) = CONST 
    0x2ba: REVERT v2b7(0x0), v2b7(0x0)

    Begin block 0x2bb
    prev=[0x2af], succ=[0x2ce, 0x2d2]
    =================================
    0x2bd: v2bd(0x2e8) = CONST 
    0x2c0: v2c0(0x4) = CONST 
    0x2c3: v2c3 = CALLDATASIZE 
    0x2c4: v2c4 = SUB v2c3, v2c0(0x4)
    0x2c5: v2c5(0x20) = CONST 
    0x2c8: v2c8 = LT v2c4, v2c5(0x20)
    0x2c9: v2c9 = ISZERO v2c8
    0x2ca: v2ca(0x2d2) = CONST 
    0x2cd: JUMPI v2ca(0x2d2), v2c9

    Begin block 0x2ce
    prev=[0x2bb], succ=[]
    =================================
    0x2ce: v2ce(0x0) = CONST 
    0x2d1: REVERT v2ce(0x0), v2ce(0x0)

    Begin block 0x2d2
    prev=[0x2bb], succ=[0x7f3]
    =================================
    0x2d4: v2d4 = ADD v2c0(0x4), v2c4
    0x2d8: v2d8 = CALLDATALOAD v2c0(0x4)
    0x2da: v2da(0x20) = CONST 
    0x2dc: v2dc(0x24) = ADD v2da(0x20), v2c0(0x4)
    0x2e4: v2e4(0x7f3) = CONST 
    0x2e7: JUMP v2e4(0x7f3)

    Begin block 0x7f3
    prev=[0x2d2], succ=[0x849, 0x8b6]
    =================================
    0x7f4: v7f4(0x0) = CONST 
    0x7f6: v7f6(0x1) = CONST 
    0x7f9: v7f9 = SLOAD v7f4(0x0)
    0x7fb: v7fb(0x100) = CONST 
    0x7fe: v7fe(0x100) = EXP v7fb(0x100), v7f6(0x1)
    0x800: v800 = DIV v7f9, v7fe(0x100)
    0x801: v801(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x816: v816 = AND v801(0xffffffffffffffffffffffffffffffffffffffff), v800
    0x817: v817(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x82c: v82c = AND v817(0xffffffffffffffffffffffffffffffffffffffff), v816
    0x82d: v82d = CALLER 
    0x82e: v82e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x843: v843 = AND v82e(0xffffffffffffffffffffffffffffffffffffffff), v82d
    0x844: v844 = EQ v843, v82c
    0x845: v845(0x8b6) = CONST 
    0x848: JUMPI v845(0x8b6), v844

    Begin block 0x849
    prev=[0x7f3], succ=[]
    =================================
    0x849: v849(0x40) = CONST 
    0x84b: v84b = MLOAD v849(0x40)
    0x84c: v84c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x86e: MSTORE v84b, v84c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x86f: v86f(0x4) = CONST 
    0x871: v871 = ADD v86f(0x4), v84b
    0x874: v874(0x20) = CONST 
    0x876: v876 = ADD v874(0x20), v871
    0x879: v879(0x20) = SUB v876, v871
    0x87b: MSTORE v871, v879(0x20)
    0x87c: v87c(0x9) = CONST 
    0x87f: MSTORE v876, v87c(0x9)
    0x880: v880(0x20) = CONST 
    0x882: v882 = ADD v880(0x20), v876
    0x884: v884(0x216f70657261746f720000000000000000000000000000000000000000000000) = CONST 
    0x8a6: MSTORE v882, v884(0x216f70657261746f720000000000000000000000000000000000000000000000)
    0x8a8: v8a8(0x20) = CONST 
    0x8aa: v8aa = ADD v8a8(0x20), v882
    0x8ae: v8ae(0x40) = CONST 
    0x8b0: v8b0 = MLOAD v8ae(0x40)
    0x8b3: v8b3(0x64) = SUB v8aa, v8b0
    0x8b5: REVERT v8b0, v8b3(0x64)

    Begin block 0x8b6
    prev=[0x7f3], succ=[0x8ba]
    =================================
    0x8b7: v8b7(0x0) = CONST 

    Begin block 0x8ba
    prev=[0x8b6, 0x1001], succ=[0x8c8, 0x1011]
    =================================
    0x8ba_0x0: v8ba_0 = PHI v8b7(0x0), v1009
    0x8bb: v8bb(0x5) = CONST 
    0x8be: v8be = SLOAD v8bb(0x5)
    0x8c2: v8c2 = LT v8ba_0, v8be
    0x8c3: v8c3 = ISZERO v8c2
    0x8c4: v8c4(0x1011) = CONST 
    0x8c7: JUMPI v8c4(0x1011), v8c3

    Begin block 0x8c8
    prev=[0x8ba], succ=[0x8d5, 0x8d6]
    =================================
    0x8c8: v8c8(0x0) = CONST 
    0x8c8_0x0: v8c8_0 = PHI v8b7(0x0), v1009
    0x8ca: v8ca(0x5) = CONST 
    0x8ce: v8ce = SLOAD v8ca(0x5)
    0x8d0: v8d0 = LT v8c8_0, v8ce
    0x8d1: v8d1(0x8d6) = CONST 
    0x8d4: JUMPI v8d1(0x8d6), v8d0

    Begin block 0x8d5
    prev=[0x8c8], succ=[]
    =================================
    0x8d5: THROW 

    Begin block 0x8d6
    prev=[0x8c8], succ=[0x9ab, 0x9af]
    =================================
    0x8d6_0x0: v8d6_0 = PHI v8b7(0x0), v1009
    0x8d8: v8d8(0x0) = CONST 
    0x8da: MSTORE v8d8(0x0), v8ca(0x5)
    0x8db: v8db(0x20) = CONST 
    0x8dd: v8dd(0x0) = CONST 
    0x8df: v8df = SHA3 v8dd(0x0), v8db(0x20)
    0x8e0: v8e0 = ADD v8df, v8d6_0
    0x8e1: v8e1(0x0) = CONST 
    0x8e4: v8e4 = SLOAD v8e0
    0x8e6: v8e6(0x100) = CONST 
    0x8e9: v8e9(0x1) = EXP v8e6(0x100), v8e1(0x0)
    0x8eb: v8eb = DIV v8e4, v8e9(0x1)
    0x8ec: v8ec(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x901: v901 = AND v8ec(0xffffffffffffffffffffffffffffffffffffffff), v8eb
    0x904: v904(0x0) = CONST 
    0x906: v906(0x6) = CONST 
    0x908: v908(0x0) = CONST 
    0x90b: v90b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x920: v920 = AND v90b(0xffffffffffffffffffffffffffffffffffffffff), v901
    0x921: v921(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x936: v936 = AND v921(0xffffffffffffffffffffffffffffffffffffffff), v920
    0x938: MSTORE v908(0x0), v936
    0x939: v939(0x20) = CONST 
    0x93b: v93b(0x20) = ADD v939(0x20), v908(0x0)
    0x93e: MSTORE v93b(0x20), v906(0x6)
    0x93f: v93f(0x20) = CONST 
    0x941: v941(0x40) = ADD v93f(0x20), v93b(0x20)
    0x942: v942(0x0) = CONST 
    0x944: v944 = SHA3 v942(0x0), v941(0x40)
    0x945: v945(0x0) = CONST 
    0x948: v948 = SLOAD v944
    0x94a: v94a(0x100) = CONST 
    0x94d: v94d(0x1) = EXP v94a(0x100), v945(0x0)
    0x94f: v94f = DIV v948, v94d(0x1)
    0x950: v950(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x965: v965 = AND v950(0xffffffffffffffffffffffffffffffffffffffff), v94f
    0x968: v968(0x0) = CONST 
    0x96b: v96b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x980: v980 = AND v96b(0xffffffffffffffffffffffffffffffffffffffff), v901
    0x981: v981(0x5f0d92ac) = CONST 
    0x986: v986(0x40) = CONST 
    0x988: v988 = MLOAD v986(0x40)
    0x98a: v98a(0xffffffff) = CONST 
    0x98f: v98f(0x5f0d92ac) = AND v98a(0xffffffff), v981(0x5f0d92ac)
    0x990: v990(0xe0) = CONST 
    0x992: v992(0x5f0d92ac00000000000000000000000000000000000000000000000000000000) = SHL v990(0xe0), v98f(0x5f0d92ac)
    0x994: MSTORE v988, v992(0x5f0d92ac00000000000000000000000000000000000000000000000000000000)
    0x995: v995(0x4) = CONST 
    0x997: v997 = ADD v995(0x4), v988
    0x998: v998(0x20) = CONST 
    0x99a: v99a(0x40) = CONST 
    0x99c: v99c = MLOAD v99a(0x40)
    0x99f: v99f(0x4) = SUB v997, v99c
    0x9a3: v9a3 = EXTCODESIZE v980
    0x9a4: v9a4 = ISZERO v9a3
    0x9a6: v9a6 = ISZERO v9a4
    0x9a7: v9a7(0x9af) = CONST 
    0x9aa: JUMPI v9a7(0x9af), v9a6

    Begin block 0x9ab
    prev=[0x8d6], succ=[]
    =================================
    0x9ab: v9ab(0x0) = CONST 
    0x9ae: REVERT v9ab(0x0), v9ab(0x0)

    Begin block 0x9af
    prev=[0x8d6], succ=[0x9ba, 0x9c3]
    =================================
    0x9b1: v9b1 = GAS 
    0x9b2: v9b2 = STATICCALL v9b1, v980, v99c, v99f(0x4), v99c, v998(0x20)
    0x9b3: v9b3 = ISZERO v9b2
    0x9b5: v9b5 = ISZERO v9b3
    0x9b6: v9b6(0x9c3) = CONST 
    0x9b9: JUMPI v9b6(0x9c3), v9b5

    Begin block 0x9ba
    prev=[0x9af], succ=[]
    =================================
    0x9ba: v9ba = RETURNDATASIZE 
    0x9bb: v9bb(0x0) = CONST 
    0x9be: RETURNDATACOPY v9bb(0x0), v9bb(0x0), v9ba
    0x9bf: v9bf = RETURNDATASIZE 
    0x9c0: v9c0(0x0) = CONST 
    0x9c2: REVERT v9c0(0x0), v9bf

    Begin block 0x9c3
    prev=[0x9af], succ=[0x9d5, 0x9d9]
    =================================
    0x9c8: v9c8(0x40) = CONST 
    0x9ca: v9ca = MLOAD v9c8(0x40)
    0x9cb: v9cb = RETURNDATASIZE 
    0x9cc: v9cc(0x20) = CONST 
    0x9cf: v9cf = LT v9cb, v9cc(0x20)
    0x9d0: v9d0 = ISZERO v9cf
    0x9d1: v9d1(0x9d9) = CONST 
    0x9d4: JUMPI v9d1(0x9d9), v9d0

    Begin block 0x9d5
    prev=[0x9c3], succ=[]
    =================================
    0x9d5: v9d5(0x0) = CONST 
    0x9d8: REVERT v9d5(0x0), v9d5(0x0)

    Begin block 0x9d9
    prev=[0x9c3], succ=[0xaef, 0xa43]
    =================================
    0x9db: v9db = ADD v9ca, v9cb
    0x9df: v9df = MLOAD v9ca
    0x9e1: v9e1(0x20) = CONST 
    0x9e3: v9e3 = ADD v9e1(0x20), v9ca
    0x9ed: v9ed(0x1) = CONST 
    0x9ef: v9ef(0x0) = CONST 
    0x9f2: v9f2 = SLOAD v9ed(0x1)
    0x9f4: v9f4(0x100) = CONST 
    0x9f7: v9f7(0x1) = EXP v9f4(0x100), v9ef(0x0)
    0x9f9: v9f9 = DIV v9f2, v9f7(0x1)
    0x9fa: v9fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa0f: va0f = AND v9fa(0xffffffffffffffffffffffffffffffffffffffff), v9f9
    0xa10: va10(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa25: va25 = AND va10(0xffffffffffffffffffffffffffffffffffffffff), va0f
    0xa27: va27(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa3c: va3c = AND va27(0xffffffffffffffffffffffffffffffffffffffff), v965
    0xa3d: va3d = EQ va3c, va25
    0xa3e: va3e = ISZERO va3d
    0xa3f: va3f(0xaef) = CONST 
    0xa42: JUMPI va3f(0xaef), va3e

    Begin block 0xaef
    prev=[0x9d9], succ=[0xb54, 0xb58]
    =================================
    0xaf1: vaf1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb06: vb06 = AND vaf1(0xffffffffffffffffffffffffffffffffffffffff), v901
    0xb07: vb07(0x998e7a80) = CONST 
    0xb0c: vb0c = ADDRESS 
    0xb0d: vb0d(0x40) = CONST 
    0xb0f: vb0f = MLOAD vb0d(0x40)
    0xb11: vb11(0xffffffff) = CONST 
    0xb16: vb16(0x998e7a80) = AND vb11(0xffffffff), vb07(0x998e7a80)
    0xb17: vb17(0xe0) = CONST 
    0xb19: vb19(0x998e7a8000000000000000000000000000000000000000000000000000000000) = SHL vb17(0xe0), vb16(0x998e7a80)
    0xb1b: MSTORE vb0f, vb19(0x998e7a8000000000000000000000000000000000000000000000000000000000)
    0xb1c: vb1c(0x4) = CONST 
    0xb1e: vb1e = ADD vb1c(0x4), vb0f
    0xb21: vb21(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb36: vb36 = AND vb21(0xffffffffffffffffffffffffffffffffffffffff), vb0c
    0xb38: MSTORE vb1e, vb36
    0xb39: vb39(0x20) = CONST 
    0xb3b: vb3b = ADD vb39(0x20), vb1e
    0xb3f: vb3f(0x0) = CONST 
    0xb41: vb41(0x40) = CONST 
    0xb43: vb43 = MLOAD vb41(0x40)
    0xb46: vb46(0x24) = SUB vb3b, vb43
    0xb48: vb48(0x0) = CONST 
    0xb4c: vb4c = EXTCODESIZE vb06
    0xb4d: vb4d = ISZERO vb4c
    0xb4f: vb4f = ISZERO vb4d
    0xb50: vb50(0xb58) = CONST 
    0xb53: JUMPI vb50(0xb58), vb4f

    Begin block 0xb54
    prev=[0xaef], succ=[]
    =================================
    0xb54: vb54(0x0) = CONST 
    0xb57: REVERT vb54(0x0), vb54(0x0)

    Begin block 0xb58
    prev=[0xaef], succ=[0xb63, 0xb6c]
    =================================
    0xb5a: vb5a = GAS 
    0xb5b: vb5b = CALL vb5a, vb06, vb48(0x0), vb43, vb46(0x24), vb43, vb3f(0x0)
    0xb5c: vb5c = ISZERO vb5b
    0xb5e: vb5e = ISZERO vb5c
    0xb5f: vb5f(0xb6c) = CONST 
    0xb62: JUMPI vb5f(0xb6c), vb5e

    Begin block 0xb63
    prev=[0xb58], succ=[]
    =================================
    0xb63: vb63 = RETURNDATASIZE 
    0xb64: vb64(0x0) = CONST 
    0xb67: RETURNDATACOPY vb64(0x0), vb64(0x0), vb63
    0xb68: vb68 = RETURNDATASIZE 
    0xb69: vb69(0x0) = CONST 
    0xb6b: REVERT vb69(0x0), vb68

    Begin block 0xb6c
    prev=[0xb58], succ=[0xbd6, 0xbda]
    =================================
    0xb71: vb71(0x2) = CONST 
    0xb73: vb73(0x0) = CONST 
    0xb76: vb76 = SLOAD vb71(0x2)
    0xb78: vb78(0x100) = CONST 
    0xb7b: vb7b(0x1) = EXP vb78(0x100), vb73(0x0)
    0xb7d: vb7d = DIV vb76, vb7b(0x1)
    0xb7e: vb7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb93: vb93 = AND vb7e(0xffffffffffffffffffffffffffffffffffffffff), vb7d
    0xb94: vb94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xba9: vba9 = AND vb94(0xffffffffffffffffffffffffffffffffffffffff), vb93
    0xbaa: vbaa(0xd0e30db0) = CONST 
    0xbb0: vbb0(0x40) = CONST 
    0xbb2: vbb2 = MLOAD vbb0(0x40)
    0xbb4: vbb4(0xffffffff) = CONST 
    0xbb9: vbb9(0xd0e30db0) = AND vbb4(0xffffffff), vbaa(0xd0e30db0)
    0xbba: vbba(0xe0) = CONST 
    0xbbc: vbbc(0xd0e30db000000000000000000000000000000000000000000000000000000000) = SHL vbba(0xe0), vbb9(0xd0e30db0)
    0xbbe: MSTORE vbb2, vbbc(0xd0e30db000000000000000000000000000000000000000000000000000000000)
    0xbbf: vbbf(0x4) = CONST 
    0xbc1: vbc1 = ADD vbbf(0x4), vbb2
    0xbc2: vbc2(0x0) = CONST 
    0xbc4: vbc4(0x40) = CONST 
    0xbc6: vbc6 = MLOAD vbc4(0x40)
    0xbc9: vbc9(0x4) = SUB vbc1, vbc6
    0xbce: vbce = EXTCODESIZE vba9
    0xbcf: vbcf = ISZERO vbce
    0xbd1: vbd1 = ISZERO vbcf
    0xbd2: vbd2(0xbda) = CONST 
    0xbd5: JUMPI vbd2(0xbda), vbd1

    Begin block 0xbd6
    prev=[0xb6c], succ=[]
    =================================
    0xbd6: vbd6(0x0) = CONST 
    0xbd9: REVERT vbd6(0x0), vbd6(0x0)

    Begin block 0xbda
    prev=[0xb6c], succ=[0xbe5, 0xbee]
    =================================
    0xbdc: vbdc = GAS 
    0xbdd: vbdd = CALL vbdc, vba9, v9df, vbc6, vbc9(0x4), vbc6, vbc2(0x0)
    0xbde: vbde = ISZERO vbdd
    0xbe0: vbe0 = ISZERO vbde
    0xbe1: vbe1(0xbee) = CONST 
    0xbe4: JUMPI vbe1(0xbee), vbe0

    Begin block 0xbe5
    prev=[0xbda], succ=[]
    =================================
    0xbe5: vbe5 = RETURNDATASIZE 
    0xbe6: vbe6(0x0) = CONST 
    0xbe9: RETURNDATACOPY vbe6(0x0), vbe6(0x0), vbe5
    0xbea: vbea = RETURNDATASIZE 
    0xbeb: vbeb(0x0) = CONST 
    0xbed: REVERT vbeb(0x0), vbea

    Begin block 0xbee
    prev=[0xbda], succ=[0xca4, 0xca8]
    =================================
    0xbf4: vbf4(0x2) = CONST 
    0xbf6: vbf6(0x0) = CONST 
    0xbf9: vbf9 = SLOAD vbf4(0x2)
    0xbfb: vbfb(0x100) = CONST 
    0xbfe: vbfe(0x1) = EXP vbfb(0x100), vbf6(0x0)
    0xc00: vc00 = DIV vbf9, vbfe(0x1)
    0xc01: vc01(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc16: vc16 = AND vc01(0xffffffffffffffffffffffffffffffffffffffff), vc00
    0xc17: vc17(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc2c: vc2c = AND vc17(0xffffffffffffffffffffffffffffffffffffffff), vc16
    0xc2d: vc2d(0xa9059cbb) = CONST 
    0xc32: vc32(0x4) = CONST 
    0xc34: vc34(0x0) = CONST 
    0xc37: vc37 = SLOAD vc32(0x4)
    0xc39: vc39(0x100) = CONST 
    0xc3c: vc3c(0x1) = EXP vc39(0x100), vc34(0x0)
    0xc3e: vc3e = DIV vc37, vc3c(0x1)
    0xc3f: vc3f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc54: vc54 = AND vc3f(0xffffffffffffffffffffffffffffffffffffffff), vc3e
    0xc56: vc56(0x40) = CONST 
    0xc58: vc58 = MLOAD vc56(0x40)
    0xc5a: vc5a(0xffffffff) = CONST 
    0xc5f: vc5f(0xa9059cbb) = AND vc5a(0xffffffff), vc2d(0xa9059cbb)
    0xc60: vc60(0xe0) = CONST 
    0xc62: vc62(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = SHL vc60(0xe0), vc5f(0xa9059cbb)
    0xc64: MSTORE vc58, vc62(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0xc65: vc65(0x4) = CONST 
    0xc67: vc67 = ADD vc65(0x4), vc58
    0xc6a: vc6a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc7f: vc7f = AND vc6a(0xffffffffffffffffffffffffffffffffffffffff), vc54
    0xc81: MSTORE vc67, vc7f
    0xc82: vc82(0x20) = CONST 
    0xc84: vc84 = ADD vc82(0x20), vc67
    0xc87: MSTORE vc84, v9df
    0xc88: vc88(0x20) = CONST 
    0xc8a: vc8a = ADD vc88(0x20), vc84
    0xc8f: vc8f(0x20) = CONST 
    0xc91: vc91(0x40) = CONST 
    0xc93: vc93 = MLOAD vc91(0x40)
    0xc96: vc96(0x44) = SUB vc8a, vc93
    0xc98: vc98(0x0) = CONST 
    0xc9c: vc9c = EXTCODESIZE vc2c
    0xc9d: vc9d = ISZERO vc9c
    0xc9f: vc9f = ISZERO vc9d
    0xca0: vca0(0xca8) = CONST 
    0xca3: JUMPI vca0(0xca8), vc9f

    Begin block 0xca4
    prev=[0xbee], succ=[]
    =================================
    0xca4: vca4(0x0) = CONST 
    0xca7: REVERT vca4(0x0), vca4(0x0)

    Begin block 0xca8
    prev=[0xbee], succ=[0xcb3, 0xcbc]
    =================================
    0xcaa: vcaa = GAS 
    0xcab: vcab = CALL vcaa, vc2c, vc98(0x0), vc93, vc96(0x44), vc93, vc8f(0x20)
    0xcac: vcac = ISZERO vcab
    0xcae: vcae = ISZERO vcac
    0xcaf: vcaf(0xcbc) = CONST 
    0xcb2: JUMPI vcaf(0xcbc), vcae

    Begin block 0xcb3
    prev=[0xca8], succ=[]
    =================================
    0xcb3: vcb3 = RETURNDATASIZE 
    0xcb4: vcb4(0x0) = CONST 
    0xcb7: RETURNDATACOPY vcb4(0x0), vcb4(0x0), vcb3
    0xcb8: vcb8 = RETURNDATASIZE 
    0xcb9: vcb9(0x0) = CONST 
    0xcbb: REVERT vcb9(0x0), vcb8

    Begin block 0xcbc
    prev=[0xca8], succ=[0xcce, 0xcd2]
    =================================
    0xcc1: vcc1(0x40) = CONST 
    0xcc3: vcc3 = MLOAD vcc1(0x40)
    0xcc4: vcc4 = RETURNDATASIZE 
    0xcc5: vcc5(0x20) = CONST 
    0xcc8: vcc8 = LT vcc4, vcc5(0x20)
    0xcc9: vcc9 = ISZERO vcc8
    0xcca: vcca(0xcd2) = CONST 
    0xccd: JUMPI vcca(0xcd2), vcc9

    Begin block 0xcce
    prev=[0xcbc], succ=[]
    =================================
    0xcce: vcce(0x0) = CONST 
    0xcd1: REVERT vcce(0x0), vcce(0x0)

    Begin block 0xcd2
    prev=[0xcbc], succ=[0xce8, 0xce9]
    =================================
    0xcd4: vcd4 = ADD vcc3, vcc4
    0xcd8: vcd8 = MLOAD vcc3
    0xcda: vcda(0x20) = CONST 
    0xcdc: vcdc = ADD vcda(0x20), vcc3
    0xce4: vce4(0xce9) = CONST 
    0xce7: JUMPI vce4(0xce9), vcd8

    Begin block 0xce8
    prev=[0xcd2], succ=[]
    =================================
    0xce8: THROW 

    Begin block 0xce9
    prev=[0xcd2], succ=[0xd50, 0xd54]
    =================================
    0xcea: vcea(0x0) = CONST 
    0xced: vced(0x4) = CONST 
    0xcef: vcef(0x0) = CONST 
    0xcf2: vcf2 = SLOAD vced(0x4)
    0xcf4: vcf4(0x100) = CONST 
    0xcf7: vcf7(0x1) = EXP vcf4(0x100), vcef(0x0)
    0xcf9: vcf9 = DIV vcf2, vcf7(0x1)
    0xcfa: vcfa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd0f: vd0f = AND vcfa(0xffffffffffffffffffffffffffffffffffffffff), vcf9
    0xd10: vd10(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd25: vd25 = AND vd10(0xffffffffffffffffffffffffffffffffffffffff), vd0f
    0xd26: vd26(0x902f1ac) = CONST 
    0xd2b: vd2b(0x40) = CONST 
    0xd2d: vd2d = MLOAD vd2b(0x40)
    0xd2f: vd2f(0xffffffff) = CONST 
    0xd34: vd34(0x902f1ac) = AND vd2f(0xffffffff), vd26(0x902f1ac)
    0xd35: vd35(0xe0) = CONST 
    0xd37: vd37(0x902f1ac00000000000000000000000000000000000000000000000000000000) = SHL vd35(0xe0), vd34(0x902f1ac)
    0xd39: MSTORE vd2d, vd37(0x902f1ac00000000000000000000000000000000000000000000000000000000)
    0xd3a: vd3a(0x4) = CONST 
    0xd3c: vd3c = ADD vd3a(0x4), vd2d
    0xd3d: vd3d(0x60) = CONST 
    0xd3f: vd3f(0x40) = CONST 
    0xd41: vd41 = MLOAD vd3f(0x40)
    0xd44: vd44(0x4) = SUB vd3c, vd41
    0xd48: vd48 = EXTCODESIZE vd25
    0xd49: vd49 = ISZERO vd48
    0xd4b: vd4b = ISZERO vd49
    0xd4c: vd4c(0xd54) = CONST 
    0xd4f: JUMPI vd4c(0xd54), vd4b

    Begin block 0xd50
    prev=[0xce9], succ=[]
    =================================
    0xd50: vd50(0x0) = CONST 
    0xd53: REVERT vd50(0x0), vd50(0x0)

    Begin block 0xd54
    prev=[0xce9], succ=[0xd5f, 0xd68]
    =================================
    0xd56: vd56 = GAS 
    0xd57: vd57 = STATICCALL vd56, vd25, vd41, vd44(0x4), vd41, vd3d(0x60)
    0xd58: vd58 = ISZERO vd57
    0xd5a: vd5a = ISZERO vd58
    0xd5b: vd5b(0xd68) = CONST 
    0xd5e: JUMPI vd5b(0xd68), vd5a

    Begin block 0xd5f
    prev=[0xd54], succ=[]
    =================================
    0xd5f: vd5f = RETURNDATASIZE 
    0xd60: vd60(0x0) = CONST 
    0xd63: RETURNDATACOPY vd60(0x0), vd60(0x0), vd5f
    0xd64: vd64 = RETURNDATASIZE 
    0xd65: vd65(0x0) = CONST 
    0xd67: REVERT vd65(0x0), vd64

    Begin block 0xd68
    prev=[0xd54], succ=[0xd7a, 0xd7e]
    =================================
    0xd6d: vd6d(0x40) = CONST 
    0xd6f: vd6f = MLOAD vd6d(0x40)
    0xd70: vd70 = RETURNDATASIZE 
    0xd71: vd71(0x60) = CONST 
    0xd74: vd74 = LT vd70, vd71(0x60)
    0xd75: vd75 = ISZERO vd74
    0xd76: vd76(0xd7e) = CONST 
    0xd79: JUMPI vd76(0xd7e), vd75

    Begin block 0xd7a
    prev=[0xd68], succ=[]
    =================================
    0xd7a: vd7a(0x0) = CONST 
    0xd7d: REVERT vd7a(0x0), vd7a(0x0)

    Begin block 0xd7e
    prev=[0xd68], succ=[0x4110x2af]
    =================================
    0xd80: vd80 = ADD vd6f, vd70
    0xd84: vd84 = MLOAD vd6f
    0xd86: vd86(0x20) = CONST 
    0xd88: vd88 = ADD vd86(0x20), vd6f
    0xd8e: vd8e = MLOAD vd88
    0xd90: vd90(0x20) = CONST 
    0xd92: vd92 = ADD vd90(0x20), vd88
    0xd98: vd98 = MLOAD vd92
    0xd9a: vd9a(0x20) = CONST 
    0xd9c: vd9c = ADD vd9a(0x20), vd92
    0xda5: vda5(0xffffffffffffffffffffffffffff) = CONST 
    0xdb4: vdb4 = AND vda5(0xffffffffffffffffffffffffffff), vd8e
    0xdb7: vdb7(0xffffffffffffffffffffffffffff) = CONST 
    0xdc6: vdc6 = AND vdb7(0xffffffffffffffffffffffffffff), vd84
    0xdc9: vdc9(0x0) = CONST 
    0xdcb: vdcb(0xdd5) = CONST 
    0xdd1: vdd1(0x411) = CONST 
    0xdd4: JUMP vdd1(0x411)

    Begin block 0x4110x2af
    prev=[0xd7e], succ=[0x41b0x2af, 0x46b0x2af]
    =================================
    0x4120x2af: v2af412(0x0) = CONST 
    0x4160x2af: v2af416 = GT v9df, v2af412(0x0)
    0x4170x2af: v2af417(0x46b) = CONST 
    0x41a0x2af: JUMPI v2af417(0x46b), v2af416

    Begin block 0x41b0x2af
    prev=[0x4110x2af], succ=[]
    =================================
    0x41b0x2af: v2af41b(0x40) = CONST 
    0x41d0x2af: v2af41d = MLOAD v2af41b(0x40)
    0x41e0x2af: v2af41e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4400x2af: MSTORE v2af41d, v2af41e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4410x2af: v2af441(0x4) = CONST 
    0x4430x2af: v2af443 = ADD v2af441(0x4), v2af41d
    0x4460x2af: v2af446(0x20) = CONST 
    0x4480x2af: v2af448 = ADD v2af446(0x20), v2af443
    0x44b0x2af: v2af44b(0x20) = SUB v2af448, v2af443
    0x44d0x2af: MSTORE v2af443, v2af44b(0x20)
    0x44e0x2af: v2af44e(0x30) = CONST 
    0x4510x2af: MSTORE v2af448, v2af44e(0x30)
    0x4520x2af: v2af452(0x20) = CONST 
    0x4540x2af: v2af454 = ADD v2af452(0x20), v2af448
    0x4560x2af: v2af456(0x15d4) = CONST 
    0x4590x2af: v2af459(0x30) = CONST 
    0x45c0x2af: CODECOPY v2af454, v2af456(0x15d4), v2af459(0x30)
    0x45d0x2af: v2af45d(0x40) = CONST 
    0x45f0x2af: v2af45f = ADD v2af45d(0x40), v2af454
    0x4630x2af: v2af463(0x40) = CONST 
    0x4650x2af: v2af465 = MLOAD v2af463(0x40)
    0x4680x2af: v2af468(0x84) = SUB v2af45f, v2af465
    0x46a0x2af: REVERT v2af465, v2af468(0x84)

    Begin block 0x46b0x2af
    prev=[0x4110x2af], succ=[0x47b0x2af, 0x4760x2af]
    =================================
    0x46c0x2af: v2af46c(0x0) = CONST 
    0x46f0x2af: v2af46f = GT vdb4, v2af46c(0x0)
    0x4710x2af: v2af471 = ISZERO v2af46f
    0x4720x2af: v2af472(0x47b) = CONST 
    0x4750x2af: JUMPI v2af472(0x47b), v2af471

    Begin block 0x47b0x2af
    prev=[0x46b0x2af, 0x4760x2af], succ=[0x4800x2af, 0x4d00x2af]
    =================================
    0x47b0x2af_0x0: v47b2af_0 = PHI v2af47a, v2af46f
    0x47c0x2af: v2af47c(0x4d0) = CONST 
    0x47f0x2af: JUMPI v2af47c(0x4d0), v47b2af_0

    Begin block 0x4800x2af
    prev=[0x47b0x2af], succ=[]
    =================================
    0x4800x2af: v2af480(0x40) = CONST 
    0x4820x2af: v2af482 = MLOAD v2af480(0x40)
    0x4830x2af: v2af483(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4a50x2af: MSTORE v2af482, v2af483(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4a60x2af: v2af4a6(0x4) = CONST 
    0x4a80x2af: v2af4a8 = ADD v2af4a6(0x4), v2af482
    0x4ab0x2af: v2af4ab(0x20) = CONST 
    0x4ad0x2af: v2af4ad = ADD v2af4ab(0x20), v2af4a8
    0x4b00x2af: v2af4b0(0x20) = SUB v2af4ad, v2af4a8
    0x4b20x2af: MSTORE v2af4a8, v2af4b0(0x20)
    0x4b30x2af: v2af4b3(0x2d) = CONST 
    0x4b60x2af: MSTORE v2af4ad, v2af4b3(0x2d)
    0x4b70x2af: v2af4b7(0x20) = CONST 
    0x4b90x2af: v2af4b9 = ADD v2af4b7(0x20), v2af4ad
    0x4bb0x2af: v2af4bb(0x1604) = CONST 
    0x4be0x2af: v2af4be(0x2d) = CONST 
    0x4c10x2af: CODECOPY v2af4b9, v2af4bb(0x1604), v2af4be(0x2d)
    0x4c20x2af: v2af4c2(0x40) = CONST 
    0x4c40x2af: v2af4c4 = ADD v2af4c2(0x40), v2af4b9
    0x4c80x2af: v2af4c8(0x40) = CONST 
    0x4ca0x2af: v2af4ca = MLOAD v2af4c8(0x40)
    0x4cd0x2af: v2af4cd(0x84) = SUB v2af4c4, v2af4ca
    0x4cf0x2af: REVERT v2af4ca, v2af4cd(0x84)

    Begin block 0x4d00x2af
    prev=[0x47b0x2af], succ=[0x4f30x2af, 0x4f40x2af]
    =================================
    0x4d10x2af: v2af4d1(0x0) = CONST 
    0x4d30x2af: v2af4d3(0x3e5) = CONST 
    0x4d70x2af: v2af4d7 = MUL v9df, v2af4d3(0x3e5)
    0x4da0x2af: v2af4da(0x0) = CONST 
    0x4de0x2af: v2af4de = MUL v2af4d7, vdc6
    0x4e10x2af: v2af4e1(0x0) = CONST 
    0x4e40x2af: v2af4e4(0x3e8) = CONST 
    0x4e80x2af: v2af4e8 = MUL vdb4, v2af4e4(0x3e8)
    0x4e90x2af: v2af4e9 = ADD v2af4e8, v2af4d7
    0x4ef0x2af: v2af4ef(0x4f4) = CONST 
    0x4f20x2af: JUMPI v2af4ef(0x4f4), v2af4e9

    Begin block 0x4f30x2af
    prev=[0x4d00x2af], succ=[]
    =================================
    0x4f30x2af: THROW 

    Begin block 0x4f40x2af
    prev=[0x4d00x2af], succ=[0xdd5]
    =================================
    0x4f50x2af: v2af4f5 = DIV v2af4de, v2af4e9
    0x5000x2af: JUMP vdcb(0xdd5)

    Begin block 0xdd5
    prev=[0x4f40x2af], succ=[0xde7, 0xde8]
    =================================
    0xdd8: vdd8(0x0) = CONST 
    0xddb: vddb(0x2540be400) = CONST 
    0xde3: vde3(0xde8) = CONST 
    0xde6: JUMPI vde3(0xde8), vddb(0x2540be400)

    Begin block 0xde7
    prev=[0xdd5], succ=[]
    =================================
    0xde7: THROW 

    Begin block 0xde8
    prev=[0xdd5], succ=[0xdef, 0xdf0]
    =================================
    0xde9: vde9 = DIV v9df, vddb(0x2540be400)
    0xdeb: vdeb(0xdf0) = CONST 
    0xdee: JUMPI vdeb(0xdf0), v2af4f5

    Begin block 0xdef
    prev=[0xde8], succ=[]
    =================================
    0xdef: THROW 

    Begin block 0xdf0
    prev=[0xde8], succ=[0xdfc, 0xe69]
    =================================
    0xdf1: vdf1 = DIV vde9, v2af4f5
    0xdf6: vdf6 = LT vdf1, v2d8
    0xdf7: vdf7 = ISZERO vdf6
    0xdf8: vdf8(0xe69) = CONST 
    0xdfb: JUMPI vdf8(0xe69), vdf7

    Begin block 0xdfc
    prev=[0xdf0], succ=[]
    =================================
    0xdfc: vdfc(0x40) = CONST 
    0xdfe: vdfe = MLOAD vdfc(0x40)
    0xdff: vdff(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xe21: MSTORE vdfe, vdff(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe22: ve22(0x4) = CONST 
    0xe24: ve24 = ADD ve22(0x4), vdfe
    0xe27: ve27(0x20) = CONST 
    0xe29: ve29 = ADD ve27(0x20), ve24
    0xe2c: ve2c(0x20) = SUB ve29, ve24
    0xe2e: MSTORE ve24, ve2c(0x20)
    0xe2f: ve2f(0xa) = CONST 
    0xe32: MSTORE ve29, ve2f(0xa)
    0xe33: ve33(0x20) = CONST 
    0xe35: ve35 = ADD ve33(0x20), ve29
    0xe37: ve37(0x7072696365206d6f766500000000000000000000000000000000000000000000) = CONST 
    0xe59: MSTORE ve35, ve37(0x7072696365206d6f766500000000000000000000000000000000000000000000)
    0xe5b: ve5b(0x20) = CONST 
    0xe5d: ve5d = ADD ve5b(0x20), ve35
    0xe61: ve61(0x40) = CONST 
    0xe63: ve63 = MLOAD ve61(0x40)
    0xe66: ve66(0x64) = SUB ve5d, ve63
    0xe68: REVERT ve63, ve66(0x64)

    Begin block 0xe69
    prev=[0xdf0], succ=[0xee1, 0xee5]
    =================================
    0xe6a: ve6a(0x4) = CONST 
    0xe6c: ve6c(0x0) = CONST 
    0xe6f: ve6f = SLOAD ve6a(0x4)
    0xe71: ve71(0x100) = CONST 
    0xe74: ve74(0x1) = EXP ve71(0x100), ve6c(0x0)
    0xe76: ve76 = DIV ve6f, ve74(0x1)
    0xe77: ve77(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe8c: ve8c = AND ve77(0xffffffffffffffffffffffffffffffffffffffff), ve76
    0xe8d: ve8d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xea2: vea2 = AND ve8d(0xffffffffffffffffffffffffffffffffffffffff), ve8c
    0xea3: vea3(0x22c0d9f) = CONST 
    0xea9: vea9(0x0) = CONST 
    0xeab: veab(0x3) = CONST 
    0xead: vead(0x0) = CONST 
    0xeb0: veb0 = SLOAD veab(0x3)
    0xeb2: veb2(0x100) = CONST 
    0xeb5: veb5(0x1) = EXP veb2(0x100), vead(0x0)
    0xeb7: veb7 = DIV veb0, veb5(0x1)
    0xeb8: veb8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xecd: vecd = AND veb8(0xffffffffffffffffffffffffffffffffffffffff), veb7
    0xece: vece(0x0) = CONST 
    0xed0: ved0(0xffffffffffffffff) = CONST 
    0xeda: veda(0x0) = GT vece(0x0), ved0(0xffffffffffffffff)
    0xedc: vedc(0x1) = ISZERO veda(0x0)
    0xedd: vedd(0xee5) = CONST 
    0xee0: JUMPI vedd(0xee5), vedc(0x1)

    Begin block 0xee1
    prev=[0xe69], succ=[]
    =================================
    0xee1: vee1(0x0) = CONST 
    0xee4: REVERT vee1(0x0), vee1(0x0)

    Begin block 0xee5
    prev=[0xe69], succ=[0xf18, 0xf04]
    =================================
    0xee7: vee7(0x40) = CONST 
    0xee9: vee9 = MLOAD vee7(0x40)
    0xeed: MSTORE vee9, vece(0x0)
    0xeef: veef(0x1f) = CONST 
    0xef1: vef1(0x1f) = ADD veef(0x1f), vece(0x0)
    0xef2: vef2(0x1f) = CONST 
    0xef4: vef4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT vef2(0x1f)
    0xef5: vef5(0x0) = AND vef4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0), vef1(0x1f)
    0xef6: vef6(0x20) = CONST 
    0xef8: vef8(0x20) = ADD vef6(0x20), vef5(0x0)
    0xefa: vefa = ADD vee9, vef8(0x20)
    0xefb: vefb(0x40) = CONST 
    0xefd: MSTORE vefb(0x40), vefa
    0xeff: veff = ISZERO vece(0x0)
    0xf00: vf00(0xf18) = CONST 
    0xf03: JUMPI vf00(0xf18), veff

    Begin block 0xf18
    prev=[0xee5, 0xf04], succ=[0xf75]
    =================================
    0xf1a: vf1a(0x40) = CONST 
    0xf1c: vf1c = MLOAD vf1a(0x40)
    0xf1e: vf1e(0xffffffff) = CONST 
    0xf23: vf23(0x22c0d9f) = AND vf1e(0xffffffff), vea3(0x22c0d9f)
    0xf24: vf24(0xe0) = CONST 
    0xf26: vf26(0x22c0d9f00000000000000000000000000000000000000000000000000000000) = SHL vf24(0xe0), vf23(0x22c0d9f)
    0xf28: MSTORE vf1c, vf26(0x22c0d9f00000000000000000000000000000000000000000000000000000000)
    0xf29: vf29(0x4) = CONST 
    0xf2b: vf2b = ADD vf29(0x4), vf1c
    0xf2f: MSTORE vf2b, v2af4f5
    0xf30: vf30(0x20) = CONST 
    0xf32: vf32 = ADD vf30(0x20), vf2b
    0xf35: MSTORE vf32, vea9(0x0)
    0xf36: vf36(0x20) = CONST 
    0xf38: vf38 = ADD vf36(0x20), vf32
    0xf3a: vf3a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf4f: vf4f = AND vf3a(0xffffffffffffffffffffffffffffffffffffffff), vecd
    0xf51: MSTORE vf38, vf4f
    0xf52: vf52(0x20) = CONST 
    0xf54: vf54 = ADD vf52(0x20), vf38
    0xf56: vf56(0x20) = CONST 
    0xf58: vf58 = ADD vf56(0x20), vf54
    0xf5b: vf5b(0x80) = SUB vf58, vf2b
    0xf5d: MSTORE vf54, vf5b(0x80)
    0xf61: vf61(0x0) = MLOAD vee9
    0xf63: MSTORE vf58, vf61(0x0)
    0xf64: vf64(0x20) = CONST 
    0xf66: vf66 = ADD vf64(0x20), vf58
    0xf6a: vf6a(0x0) = MLOAD vee9
    0xf6c: vf6c(0x20) = CONST 
    0xf6e: vf6e = ADD vf6c(0x20), vee9
    0xf73: vf73(0x0) = CONST 

    Begin block 0xf75
    prev=[0xf18, 0xf7e], succ=[0xf90, 0xf7e]
    =================================
    0xf75_0x0: vf75_0 = PHI vf73(0x0), vf89
    0xf78: vf78 = LT vf75_0, vf6a(0x0)
    0xf79: vf79 = ISZERO vf78
    0xf7a: vf7a(0xf90) = CONST 
    0xf7d: JUMPI vf7a(0xf90), vf79

    Begin block 0xf90
    prev=[0xf75], succ=[0xfbd, 0xfa4]
    =================================
    0xf99: vf99 = ADD vf6a(0x0), vf66
    0xf9b: vf9b(0x1f) = CONST 
    0xf9d: vf9d(0x0) = AND vf9b(0x1f), vf6a(0x0)
    0xf9f: vf9f = ISZERO vf9d(0x0)
    0xfa0: vfa0(0xfbd) = CONST 
    0xfa3: JUMPI vfa0(0xfbd), vf9f

    Begin block 0xfbd
    prev=[0xf90, 0xfa4], succ=[0xfdb, 0xfdf]
    =================================
    0xfbd_0x1: vfbd_1 = PHI vf99, vfba
    0xfc6: vfc6(0x0) = CONST 
    0xfc8: vfc8(0x40) = CONST 
    0xfca: vfca = MLOAD vfc8(0x40)
    0xfcd: vfcd = SUB vfbd_1, vfca
    0xfcf: vfcf(0x0) = CONST 
    0xfd3: vfd3 = EXTCODESIZE vea2
    0xfd4: vfd4 = ISZERO vfd3
    0xfd6: vfd6 = ISZERO vfd4
    0xfd7: vfd7(0xfdf) = CONST 
    0xfda: JUMPI vfd7(0xfdf), vfd6

    Begin block 0xfdb
    prev=[0xfbd], succ=[]
    =================================
    0xfdb: vfdb(0x0) = CONST 
    0xfde: REVERT vfdb(0x0), vfdb(0x0)

    Begin block 0xfdf
    prev=[0xfbd], succ=[0xfea, 0xff3]
    =================================
    0xfe1: vfe1 = GAS 
    0xfe2: vfe2 = CALL vfe1, vea2, vfcf(0x0), vfca, vfcd, vfca, vfc6(0x0)
    0xfe3: vfe3 = ISZERO vfe2
    0xfe5: vfe5 = ISZERO vfe3
    0xfe6: vfe6(0xff3) = CONST 
    0xfe9: JUMPI vfe6(0xff3), vfe5

    Begin block 0xfea
    prev=[0xfdf], succ=[]
    =================================
    0xfea: vfea = RETURNDATASIZE 
    0xfeb: vfeb(0x0) = CONST 
    0xfee: RETURNDATACOPY vfeb(0x0), vfeb(0x0), vfea
    0xfef: vfef = RETURNDATASIZE 
    0xff0: vff0(0x0) = CONST 
    0xff2: REVERT vff0(0x0), vfef

    Begin block 0xff3
    prev=[0xfdf], succ=[0x1001]
    =================================
    0xff3_0xc: vff3_c = PHI v8b7(0x0), vae8, vffa
    0xffa: vffa = ADD vff3_c, v2af4f5

    Begin block 0x1001
    prev=[0xae1, 0xff3], succ=[0x8ba]
    =================================
    0x1001_0x3: v1001_3 = PHI v8b7(0x0), v1009
    0x1007: v1007(0x1) = CONST 
    0x1009: v1009 = ADD v1007(0x1), v1001_3
    0x100d: v100d(0x8ba) = CONST 
    0x1010: JUMP v100d(0x8ba)

    Begin block 0xfa4
    prev=[0xf90], succ=[0xfbd]
    =================================
    0xfa6: vfa6 = SUB vf99, vf9d(0x0)
    0xfa8: vfa8 = MLOAD vfa6
    0xfa9: vfa9(0x1) = CONST 
    0xfac: vfac(0x20) = CONST 
    0xfae: vfae(0x20) = SUB vfac(0x20), vf9d(0x0)
    0xfaf: vfaf(0x100) = CONST 
    0xfb2: vfb2(0x1) = EXP vfaf(0x100), vfae(0x20)
    0xfb3: vfb3(0x0) = SUB vfb2(0x1), vfa9(0x1)
    0xfb4: vfb4 = NOT vfb3(0x0)
    0xfb5: vfb5 = AND vfb4, vfa8
    0xfb7: MSTORE vfa6, vfb5
    0xfb8: vfb8(0x20) = CONST 
    0xfba: vfba = ADD vfb8(0x20), vfa6

    Begin block 0xf7e
    prev=[0xf75], succ=[0xf75]
    =================================
    0xf7e_0x0: vf7e_0 = PHI vf73(0x0), vf89
    0xf80: vf80 = ADD vf6e, vf7e_0
    0xf81: vf81 = MLOAD vf80
    0xf84: vf84 = ADD vf66, vf7e_0
    0xf85: MSTORE vf84, vf81
    0xf86: vf86(0x20) = CONST 
    0xf89: vf89 = ADD vf7e_0, vf86(0x20)
    0xf8c: vf8c(0xf75) = CONST 
    0xf8f: JUMP vf8c(0xf75)

    Begin block 0xf04
    prev=[0xee5], succ=[0xf18]
    =================================
    0xf05: vf05(0x20) = CONST 
    0xf07: vf07 = ADD vf05(0x20), vee9
    0xf08: vf08(0x1) = CONST 
    0xf0b: vf0b(0x0) = MUL vece(0x0), vf08(0x1)
    0xf0d: vf0d = CALLDATASIZE 
    0xf0f: CALLDATACOPY vf07, vf0d, vf0b(0x0)
    0xf12: vf12 = ADD vf07, vf0b(0x0)

    Begin block 0x4760x2af
    prev=[0x46b0x2af], succ=[0x47b0x2af]
    =================================
    0x4770x2af: v2af477(0x0) = CONST 
    0x47a0x2af: v2af47a = GT vdc6, v2af477(0x0)

    Begin block 0xa43
    prev=[0x9d9], succ=[0xac9, 0xacd]
    =================================
    0xa44: va44(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa59: va59 = AND va44(0xffffffffffffffffffffffffffffffffffffffff), v901
    0xa5a: va5a(0x998e7a80) = CONST 
    0xa5f: va5f(0x3) = CONST 
    0xa61: va61(0x0) = CONST 
    0xa64: va64 = SLOAD va5f(0x3)
    0xa66: va66(0x100) = CONST 
    0xa69: va69(0x1) = EXP va66(0x100), va61(0x0)
    0xa6b: va6b = DIV va64, va69(0x1)
    0xa6c: va6c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa81: va81 = AND va6c(0xffffffffffffffffffffffffffffffffffffffff), va6b
    0xa82: va82(0x40) = CONST 
    0xa84: va84 = MLOAD va82(0x40)
    0xa86: va86(0xffffffff) = CONST 
    0xa8b: va8b(0x998e7a80) = AND va86(0xffffffff), va5a(0x998e7a80)
    0xa8c: va8c(0xe0) = CONST 
    0xa8e: va8e(0x998e7a8000000000000000000000000000000000000000000000000000000000) = SHL va8c(0xe0), va8b(0x998e7a80)
    0xa90: MSTORE va84, va8e(0x998e7a8000000000000000000000000000000000000000000000000000000000)
    0xa91: va91(0x4) = CONST 
    0xa93: va93 = ADD va91(0x4), va84
    0xa96: va96(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaab: vaab = AND va96(0xffffffffffffffffffffffffffffffffffffffff), va81
    0xaad: MSTORE va93, vaab
    0xaae: vaae(0x20) = CONST 
    0xab0: vab0 = ADD vaae(0x20), va93
    0xab4: vab4(0x0) = CONST 
    0xab6: vab6(0x40) = CONST 
    0xab8: vab8 = MLOAD vab6(0x40)
    0xabb: vabb(0x24) = SUB vab0, vab8
    0xabd: vabd(0x0) = CONST 
    0xac1: vac1 = EXTCODESIZE va59
    0xac2: vac2 = ISZERO vac1
    0xac4: vac4 = ISZERO vac2
    0xac5: vac5(0xacd) = CONST 
    0xac8: JUMPI vac5(0xacd), vac4

    Begin block 0xac9
    prev=[0xa43], succ=[]
    =================================
    0xac9: vac9(0x0) = CONST 
    0xacc: REVERT vac9(0x0), vac9(0x0)

    Begin block 0xacd
    prev=[0xa43], succ=[0xad8, 0xae1]
    =================================
    0xacf: vacf = GAS 
    0xad0: vad0 = CALL vacf, va59, vabd(0x0), vab8, vabb(0x24), vab8, vab4(0x0)
    0xad1: vad1 = ISZERO vad0
    0xad3: vad3 = ISZERO vad1
    0xad4: vad4(0xae1) = CONST 
    0xad7: JUMPI vad4(0xae1), vad3

    Begin block 0xad8
    prev=[0xacd], succ=[]
    =================================
    0xad8: vad8 = RETURNDATASIZE 
    0xad9: vad9(0x0) = CONST 
    0xadc: RETURNDATACOPY vad9(0x0), vad9(0x0), vad8
    0xadd: vadd = RETURNDATASIZE 
    0xade: vade(0x0) = CONST 
    0xae0: REVERT vade(0x0), vadd

    Begin block 0xae1
    prev=[0xacd], succ=[0x1001]
    =================================
    0xae1_0x8: vae1_8 = PHI v8b7(0x0), vae8, vffa
    0xae8: vae8 = ADD vae1_8, v9df
    0xaeb: vaeb(0x1001) = CONST 
    0xaee: JUMP vaeb(0x1001)

    Begin block 0x1011
    prev=[0x8ba], succ=[0x101c, 0x10b4]
    =================================
    0x1011_0x1: v1011_1 = PHI v8b7(0x0), vae8, vffa
    0x1013: v1013(0x0) = CONST 
    0x1016: v1016 = GT v1011_1, v1013(0x0)
    0x1017: v1017 = ISZERO v1016
    0x1018: v1018(0x10b4) = CONST 
    0x101b: JUMPI v1018(0x10b4), v1017

    Begin block 0x101c
    prev=[0x1011], succ=[0x1097, 0x109b]
    =================================
    0x101c: v101c(0x3) = CONST 
    0x101c_0x0: v101c_0 = PHI v8b7(0x0), vae8, vffa
    0x101e: v101e(0x0) = CONST 
    0x1021: v1021 = SLOAD v101c(0x3)
    0x1023: v1023(0x100) = CONST 
    0x1026: v1026(0x1) = EXP v1023(0x100), v101e(0x0)
    0x1028: v1028 = DIV v1021, v1026(0x1)
    0x1029: v1029(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x103e: v103e = AND v1029(0xffffffffffffffffffffffffffffffffffffffff), v1028
    0x103f: v103f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1054: v1054 = AND v103f(0xffffffffffffffffffffffffffffffffffffffff), v103e
    0x1055: v1055(0x246132f9) = CONST 
    0x105b: v105b(0xd2f00) = CONST 
    0x105f: v105f(0x40) = CONST 
    0x1061: v1061 = MLOAD v105f(0x40)
    0x1063: v1063(0xffffffff) = CONST 
    0x1068: v1068(0x246132f9) = AND v1063(0xffffffff), v1055(0x246132f9)
    0x1069: v1069(0xe0) = CONST 
    0x106b: v106b(0x246132f900000000000000000000000000000000000000000000000000000000) = SHL v1069(0xe0), v1068(0x246132f9)
    0x106d: MSTORE v1061, v106b(0x246132f900000000000000000000000000000000000000000000000000000000)
    0x106e: v106e(0x4) = CONST 
    0x1070: v1070 = ADD v106e(0x4), v1061
    0x1074: MSTORE v1070, v101c_0
    0x1075: v1075(0x20) = CONST 
    0x1077: v1077 = ADD v1075(0x20), v1070
    0x107a: MSTORE v1077, v105b(0xd2f00)
    0x107b: v107b(0x20) = CONST 
    0x107d: v107d = ADD v107b(0x20), v1077
    0x1082: v1082(0x0) = CONST 
    0x1084: v1084(0x40) = CONST 
    0x1086: v1086 = MLOAD v1084(0x40)
    0x1089: v1089(0x44) = SUB v107d, v1086
    0x108b: v108b(0x0) = CONST 
    0x108f: v108f = EXTCODESIZE v1054
    0x1090: v1090 = ISZERO v108f
    0x1092: v1092 = ISZERO v1090
    0x1093: v1093(0x109b) = CONST 
    0x1096: JUMPI v1093(0x109b), v1092

    Begin block 0x1097
    prev=[0x101c], succ=[]
    =================================
    0x1097: v1097(0x0) = CONST 
    0x109a: REVERT v1097(0x0), v1097(0x0)

    Begin block 0x109b
    prev=[0x101c], succ=[0x10a6, 0x10af]
    =================================
    0x109d: v109d = GAS 
    0x109e: v109e = CALL v109d, v1054, v108b(0x0), v1086, v1089(0x44), v1086, v1082(0x0)
    0x109f: v109f = ISZERO v109e
    0x10a1: v10a1 = ISZERO v109f
    0x10a2: v10a2(0x10af) = CONST 
    0x10a5: JUMPI v10a2(0x10af), v10a1

    Begin block 0x10a6
    prev=[0x109b], succ=[]
    =================================
    0x10a6: v10a6 = RETURNDATASIZE 
    0x10a7: v10a7(0x0) = CONST 
    0x10aa: RETURNDATACOPY v10a7(0x0), v10a7(0x0), v10a6
    0x10ab: v10ab = RETURNDATASIZE 
    0x10ac: v10ac(0x0) = CONST 
    0x10ae: REVERT v10ac(0x0), v10ab

    Begin block 0x10af
    prev=[0x109b], succ=[0x10b4]
    =================================

    Begin block 0x10b4
    prev=[0x1011, 0x10af], succ=[0x2e8]
    =================================
    0x10b7: JUMP v2bd(0x2e8)

    Begin block 0x2e8
    prev=[0x10b4], succ=[]
    =================================
    0x2e9: STOP 

}

function initialize(address)() public {
    Begin block 0x2ea
    prev=[], succ=[0x2f2, 0x2f6]
    =================================
    0x2eb: v2eb = CALLVALUE 
    0x2ed: v2ed = ISZERO v2eb
    0x2ee: v2ee(0x2f6) = CONST 
    0x2f1: JUMPI v2ee(0x2f6), v2ed

    Begin block 0x2f2
    prev=[0x2ea], succ=[]
    =================================
    0x2f2: v2f2(0x0) = CONST 
    0x2f5: REVERT v2f2(0x0), v2f2(0x0)

    Begin block 0x2f6
    prev=[0x2ea], succ=[0x309, 0x30d]
    =================================
    0x2f8: v2f8(0x339) = CONST 
    0x2fb: v2fb(0x4) = CONST 
    0x2fe: v2fe = CALLDATASIZE 
    0x2ff: v2ff = SUB v2fe, v2fb(0x4)
    0x300: v300(0x20) = CONST 
    0x303: v303 = LT v2ff, v300(0x20)
    0x304: v304 = ISZERO v303
    0x305: v305(0x30d) = CONST 
    0x308: JUMPI v305(0x30d), v304

    Begin block 0x309
    prev=[0x2f6], succ=[]
    =================================
    0x309: v309(0x0) = CONST 
    0x30c: REVERT v309(0x0), v309(0x0)

    Begin block 0x30d
    prev=[0x2f6], succ=[0x10b8]
    =================================
    0x30f: v30f = ADD v2fb(0x4), v2ff
    0x313: v313 = CALLDATALOAD v2fb(0x4)
    0x314: v314(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x329: v329 = AND v314(0xffffffffffffffffffffffffffffffffffffffff), v313
    0x32b: v32b(0x20) = CONST 
    0x32d: v32d(0x24) = ADD v32b(0x20), v2fb(0x4)
    0x335: v335(0x10b8) = CONST 
    0x338: JUMP v335(0x10b8)

    Begin block 0x10b8
    prev=[0x30d], succ=[0x10cc, 0x1139]
    =================================
    0x10b9: v10b9(0x0) = CONST 
    0x10bc: v10bc = SLOAD v10b9(0x0)
    0x10be: v10be(0x100) = CONST 
    0x10c1: v10c1(0x1) = EXP v10be(0x100), v10b9(0x0)
    0x10c3: v10c3 = DIV v10bc, v10c1(0x1)
    0x10c4: v10c4(0xff) = CONST 
    0x10c6: v10c6 = AND v10c4(0xff), v10c3
    0x10c7: v10c7 = ISZERO v10c6
    0x10c8: v10c8(0x1139) = CONST 
    0x10cb: JUMPI v10c8(0x1139), v10c7

    Begin block 0x10cc
    prev=[0x10b8], succ=[]
    =================================
    0x10cc: v10cc(0x40) = CONST 
    0x10ce: v10ce = MLOAD v10cc(0x40)
    0x10cf: v10cf(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x10f1: MSTORE v10ce, v10cf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10f2: v10f2(0x4) = CONST 
    0x10f4: v10f4 = ADD v10f2(0x4), v10ce
    0x10f7: v10f7(0x20) = CONST 
    0x10f9: v10f9 = ADD v10f7(0x20), v10f4
    0x10fc: v10fc(0x20) = SUB v10f9, v10f4
    0x10fe: MSTORE v10f4, v10fc(0x20)
    0x10ff: v10ff(0x13) = CONST 
    0x1102: MSTORE v10f9, v10ff(0x13)
    0x1103: v1103(0x20) = CONST 
    0x1105: v1105 = ADD v1103(0x20), v10f9
    0x1107: v1107(0x616c726561647920696e697469616c697a656400000000000000000000000000) = CONST 
    0x1129: MSTORE v1105, v1107(0x616c726561647920696e697469616c697a656400000000000000000000000000)
    0x112b: v112b(0x20) = CONST 
    0x112d: v112d = ADD v112b(0x20), v1105
    0x1131: v1131(0x40) = CONST 
    0x1133: v1133 = MLOAD v1131(0x40)
    0x1136: v1136(0x64) = SUB v112d, v1133
    0x1138: REVERT v1133, v1136(0x64)

    Begin block 0x1139
    prev=[0x10b8], succ=[0x339]
    =================================
    0x113a: v113a(0x1) = CONST 
    0x113c: v113c(0x0) = CONST 
    0x113f: v113f(0x100) = CONST 
    0x1142: v1142(0x1) = EXP v113f(0x100), v113c(0x0)
    0x1144: v1144 = SLOAD v113c(0x0)
    0x1146: v1146(0xff) = CONST 
    0x1148: v1148(0xff) = MUL v1146(0xff), v1142(0x1)
    0x1149: v1149(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1148(0xff)
    0x114a: v114a = AND v1149(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1144
    0x114d: v114d(0x0) = ISZERO v113a(0x1)
    0x114e: v114e(0x1) = ISZERO v114d(0x0)
    0x114f: v114f(0x1) = MUL v114e(0x1), v1142(0x1)
    0x1150: v1150 = OR v114f(0x1), v114a
    0x1152: SSTORE v113c(0x0), v1150
    0x1155: v1155(0x0) = CONST 
    0x1157: v1157(0x1) = CONST 
    0x1159: v1159(0x100) = CONST 
    0x115c: v115c(0x100) = EXP v1159(0x100), v1157(0x1)
    0x115e: v115e = SLOAD v1155(0x0)
    0x1160: v1160(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1175: v1175(0xffffffffffffffffffffffffffffffffffffffff00) = MUL v1160(0xffffffffffffffffffffffffffffffffffffffff), v115c(0x100)
    0x1176: v1176(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v1175(0xffffffffffffffffffffffffffffffffffffffff00)
    0x1177: v1177 = AND v1176(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff), v115e
    0x117a: v117a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x118f: v118f = AND v117a(0xffffffffffffffffffffffffffffffffffffffff), v329
    0x1190: v1190 = MUL v118f, v115c(0x100)
    0x1191: v1191 = OR v1190, v1177
    0x1193: SSTORE v1155(0x0), v1191
    0x1195: v1195(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599) = CONST 
    0x11aa: v11aa(0x1) = CONST 
    0x11ac: v11ac(0x0) = CONST 
    0x11ae: v11ae(0x100) = CONST 
    0x11b1: v11b1(0x1) = EXP v11ae(0x100), v11ac(0x0)
    0x11b3: v11b3 = SLOAD v11aa(0x1)
    0x11b5: v11b5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11ca: v11ca(0xffffffffffffffffffffffffffffffffffffffff) = MUL v11b5(0xffffffffffffffffffffffffffffffffffffffff), v11b1(0x1)
    0x11cb: v11cb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v11ca(0xffffffffffffffffffffffffffffffffffffffff)
    0x11cc: v11cc = AND v11cb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v11b3
    0x11cf: v11cf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11e4: v11e4(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599) = AND v11cf(0xffffffffffffffffffffffffffffffffffffffff), v1195(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599)
    0x11e5: v11e5(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599) = MUL v11e4(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599), v11b1(0x1)
    0x11e6: v11e6 = OR v11e5(0x2260fac5e5542a773aa44fbcfedf7c193bc2c599), v11cc
    0x11e8: SSTORE v11aa(0x1), v11e6
    0x11ea: v11ea(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = CONST 
    0x11ff: v11ff(0x2) = CONST 
    0x1201: v1201(0x0) = CONST 
    0x1203: v1203(0x100) = CONST 
    0x1206: v1206(0x1) = EXP v1203(0x100), v1201(0x0)
    0x1208: v1208 = SLOAD v11ff(0x2)
    0x120a: v120a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x121f: v121f(0xffffffffffffffffffffffffffffffffffffffff) = MUL v120a(0xffffffffffffffffffffffffffffffffffffffff), v1206(0x1)
    0x1220: v1220(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v121f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1221: v1221 = AND v1220(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1208
    0x1224: v1224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1239: v1239(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = AND v1224(0xffffffffffffffffffffffffffffffffffffffff), v11ea(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
    0x123a: v123a(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = MUL v1239(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2), v1206(0x1)
    0x123b: v123b = OR v123a(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2), v1221
    0x123d: SSTORE v11ff(0x2), v123b
    0x123f: v123f(0xbb2b8038a1640196fbe3e38816f3e67cba72d940) = CONST 
    0x1254: v1254(0x4) = CONST 
    0x1256: v1256(0x0) = CONST 
    0x1258: v1258(0x100) = CONST 
    0x125b: v125b(0x1) = EXP v1258(0x100), v1256(0x0)
    0x125d: v125d = SLOAD v1254(0x4)
    0x125f: v125f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1274: v1274(0xffffffffffffffffffffffffffffffffffffffff) = MUL v125f(0xffffffffffffffffffffffffffffffffffffffff), v125b(0x1)
    0x1275: v1275(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1274(0xffffffffffffffffffffffffffffffffffffffff)
    0x1276: v1276 = AND v1275(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v125d
    0x1279: v1279(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x128e: v128e(0xbb2b8038a1640196fbe3e38816f3e67cba72d940) = AND v1279(0xffffffffffffffffffffffffffffffffffffffff), v123f(0xbb2b8038a1640196fbe3e38816f3e67cba72d940)
    0x128f: v128f(0xbb2b8038a1640196fbe3e38816f3e67cba72d940) = MUL v128e(0xbb2b8038a1640196fbe3e38816f3e67cba72d940), v125b(0x1)
    0x1290: v1290 = OR v128f(0xbb2b8038a1640196fbe3e38816f3e67cba72d940), v1276
    0x1292: SSTORE v1254(0x4), v1290
    0x1294: v1294(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11) = CONST 
    0x12a9: v12a9(0x3) = CONST 
    0x12ab: v12ab(0x0) = CONST 
    0x12ad: v12ad(0x100) = CONST 
    0x12b0: v12b0(0x1) = EXP v12ad(0x100), v12ab(0x0)
    0x12b2: v12b2 = SLOAD v12a9(0x3)
    0x12b4: v12b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12c9: v12c9(0xffffffffffffffffffffffffffffffffffffffff) = MUL v12b4(0xffffffffffffffffffffffffffffffffffffffff), v12b0(0x1)
    0x12ca: v12ca(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v12c9(0xffffffffffffffffffffffffffffffffffffffff)
    0x12cb: v12cb = AND v12ca(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12b2
    0x12ce: v12ce(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12e3: v12e3(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11) = AND v12ce(0xffffffffffffffffffffffffffffffffffffffff), v1294(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11)
    0x12e4: v12e4(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11) = MUL v12e3(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11), v12b0(0x1)
    0x12e5: v12e5 = OR v12e4(0x51a710218ec2ba2ac459ee28ec37c6df7fe18e11), v12cb
    0x12e7: SSTORE v12a9(0x3), v12e5
    0x12ea: JUMP v2f8(0x339)

    Begin block 0x339
    prev=[0x1139], succ=[]
    =================================
    0x33a: STOP 

}

function lpStakings(uint256)() public {
    Begin block 0x33b
    prev=[], succ=[0x343, 0x347]
    =================================
    0x33c: v33c = CALLVALUE 
    0x33e: v33e = ISZERO v33c
    0x33f: v33f(0x347) = CONST 
    0x342: JUMPI v33f(0x347), v33e

    Begin block 0x343
    prev=[0x33b], succ=[]
    =================================
    0x343: v343(0x0) = CONST 
    0x346: REVERT v343(0x0), v343(0x0)

    Begin block 0x347
    prev=[0x33b], succ=[0x35a, 0x35e]
    =================================
    0x349: v349(0x374) = CONST 
    0x34c: v34c(0x4) = CONST 
    0x34f: v34f = CALLDATASIZE 
    0x350: v350 = SUB v34f, v34c(0x4)
    0x351: v351(0x20) = CONST 
    0x354: v354 = LT v350, v351(0x20)
    0x355: v355 = ISZERO v354
    0x356: v356(0x35e) = CONST 
    0x359: JUMPI v356(0x35e), v355

    Begin block 0x35a
    prev=[0x347], succ=[]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35d: REVERT v35a(0x0), v35a(0x0)

    Begin block 0x35e
    prev=[0x347], succ=[0x12eb]
    =================================
    0x360: v360 = ADD v34c(0x4), v350
    0x364: v364 = CALLDATALOAD v34c(0x4)
    0x366: v366(0x20) = CONST 
    0x368: v368(0x24) = ADD v366(0x20), v34c(0x4)
    0x370: v370(0x12eb) = CONST 
    0x373: JUMP v370(0x12eb)

    Begin block 0x12eb
    prev=[0x35e], succ=[0x12f7, 0x12fb]
    =================================
    0x12ec: v12ec(0x5) = CONST 
    0x12f0: v12f0 = SLOAD v12ec(0x5)
    0x12f2: v12f2 = LT v364, v12f0
    0x12f3: v12f3(0x12fb) = CONST 
    0x12f6: JUMPI v12f3(0x12fb), v12f2

    Begin block 0x12f7
    prev=[0x12eb], succ=[]
    =================================
    0x12f7: v12f7(0x0) = CONST 
    0x12fa: REVERT v12f7(0x0), v12f7(0x0)

    Begin block 0x12fb
    prev=[0x12eb], succ=[0x374]
    =================================
    0x12fd: v12fd(0x0) = CONST 
    0x12ff: MSTORE v12fd(0x0), v12ec(0x5)
    0x1300: v1300(0x20) = CONST 
    0x1302: v1302(0x0) = CONST 
    0x1304: v1304 = SHA3 v1302(0x0), v1300(0x20)
    0x1305: v1305 = ADD v1304, v364
    0x1306: v1306(0x0) = CONST 
    0x130a: v130a = SLOAD v1305
    0x130c: v130c(0x100) = CONST 
    0x130f: v130f(0x1) = EXP v130c(0x100), v1306(0x0)
    0x1311: v1311 = DIV v130a, v130f(0x1)
    0x1312: v1312(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1327: v1327 = AND v1312(0xffffffffffffffffffffffffffffffffffffffff), v1311
    0x1329: JUMP v349(0x374)

    Begin block 0x374
    prev=[0x12fb], succ=[]
    =================================
    0x375: v375(0x40) = CONST 
    0x377: v377 = MLOAD v375(0x40)
    0x37a: v37a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x38f: v38f = AND v37a(0xffffffffffffffffffffffffffffffffffffffff), v1327
    0x391: MSTORE v377, v38f
    0x392: v392(0x20) = CONST 
    0x394: v394 = ADD v392(0x20), v377
    0x398: v398(0x40) = CONST 
    0x39a: v39a = MLOAD v398(0x40)
    0x39d: v39d(0x20) = SUB v394, v39a
    0x39f: RETURN v39a, v39d(0x20)

}

function addStakingAndRewardToken(address,address)() public {
    Begin block 0x3a0
    prev=[], succ=[0x3a8, 0x3ac]
    =================================
    0x3a1: v3a1 = CALLVALUE 
    0x3a3: v3a3 = ISZERO v3a1
    0x3a4: v3a4(0x3ac) = CONST 
    0x3a7: JUMPI v3a4(0x3ac), v3a3

    Begin block 0x3a8
    prev=[0x3a0], succ=[]
    =================================
    0x3a8: v3a8(0x0) = CONST 
    0x3ab: REVERT v3a8(0x0), v3a8(0x0)

    Begin block 0x3ac
    prev=[0x3a0], succ=[0x3bf, 0x3c3]
    =================================
    0x3ae: v3ae(0x40f) = CONST 
    0x3b1: v3b1(0x4) = CONST 
    0x3b4: v3b4 = CALLDATASIZE 
    0x3b5: v3b5 = SUB v3b4, v3b1(0x4)
    0x3b6: v3b6(0x40) = CONST 
    0x3b9: v3b9 = LT v3b5, v3b6(0x40)
    0x3ba: v3ba = ISZERO v3b9
    0x3bb: v3bb(0x3c3) = CONST 
    0x3be: JUMPI v3bb(0x3c3), v3ba

    Begin block 0x3bf
    prev=[0x3ac], succ=[]
    =================================
    0x3bf: v3bf(0x0) = CONST 
    0x3c2: REVERT v3bf(0x0), v3bf(0x0)

    Begin block 0x3c3
    prev=[0x3ac], succ=[0x132a]
    =================================
    0x3c5: v3c5 = ADD v3b1(0x4), v3b5
    0x3c9: v3c9 = CALLDATALOAD v3b1(0x4)
    0x3ca: v3ca(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3df: v3df = AND v3ca(0xffffffffffffffffffffffffffffffffffffffff), v3c9
    0x3e1: v3e1(0x20) = CONST 
    0x3e3: v3e3(0x24) = ADD v3e1(0x20), v3b1(0x4)
    0x3e9: v3e9 = CALLDATALOAD v3e3(0x24)
    0x3ea: v3ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ff: v3ff = AND v3ea(0xffffffffffffffffffffffffffffffffffffffff), v3e9
    0x401: v401(0x20) = CONST 
    0x403: v403(0x44) = ADD v401(0x20), v3e3(0x24)
    0x40b: v40b(0x132a) = CONST 
    0x40e: JUMP v40b(0x132a)

    Begin block 0x132a
    prev=[0x3c3], succ=[0x1380, 0x13ed]
    =================================
    0x132b: v132b(0x0) = CONST 
    0x132d: v132d(0x1) = CONST 
    0x1330: v1330 = SLOAD v132b(0x0)
    0x1332: v1332(0x100) = CONST 
    0x1335: v1335(0x100) = EXP v1332(0x100), v132d(0x1)
    0x1337: v1337 = DIV v1330, v1335(0x100)
    0x1338: v1338(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x134d: v134d = AND v1338(0xffffffffffffffffffffffffffffffffffffffff), v1337
    0x134e: v134e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1363: v1363 = AND v134e(0xffffffffffffffffffffffffffffffffffffffff), v134d
    0x1364: v1364 = CALLER 
    0x1365: v1365(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x137a: v137a = AND v1365(0xffffffffffffffffffffffffffffffffffffffff), v1364
    0x137b: v137b = EQ v137a, v1363
    0x137c: v137c(0x13ed) = CONST 
    0x137f: JUMPI v137c(0x13ed), v137b

    Begin block 0x1380
    prev=[0x132a], succ=[]
    =================================
    0x1380: v1380(0x40) = CONST 
    0x1382: v1382 = MLOAD v1380(0x40)
    0x1383: v1383(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x13a5: MSTORE v1382, v1383(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13a6: v13a6(0x4) = CONST 
    0x13a8: v13a8 = ADD v13a6(0x4), v1382
    0x13ab: v13ab(0x20) = CONST 
    0x13ad: v13ad = ADD v13ab(0x20), v13a8
    0x13b0: v13b0(0x20) = SUB v13ad, v13a8
    0x13b2: MSTORE v13a8, v13b0(0x20)
    0x13b3: v13b3(0x9) = CONST 
    0x13b6: MSTORE v13ad, v13b3(0x9)
    0x13b7: v13b7(0x20) = CONST 
    0x13b9: v13b9 = ADD v13b7(0x20), v13ad
    0x13bb: v13bb(0x216f70657261746f720000000000000000000000000000000000000000000000) = CONST 
    0x13dd: MSTORE v13b9, v13bb(0x216f70657261746f720000000000000000000000000000000000000000000000)
    0x13df: v13df(0x20) = CONST 
    0x13e1: v13e1 = ADD v13df(0x20), v13b9
    0x13e5: v13e5(0x40) = CONST 
    0x13e7: v13e7 = MLOAD v13e5(0x40)
    0x13ea: v13ea(0x64) = SUB v13e1, v13e7
    0x13ec: REVERT v13e7, v13ea(0x64)

    Begin block 0x13ed
    prev=[0x132a], succ=[0x1481, 0x14ee]
    =================================
    0x13ee: v13ee(0x0) = CONST 
    0x13f0: v13f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1405: v1405(0x0) = AND v13f0(0xffffffffffffffffffffffffffffffffffffffff), v13ee(0x0)
    0x1406: v1406(0x6) = CONST 
    0x1408: v1408(0x0) = CONST 
    0x140b: v140b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1420: v1420 = AND v140b(0xffffffffffffffffffffffffffffffffffffffff), v3df
    0x1421: v1421(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1436: v1436 = AND v1421(0xffffffffffffffffffffffffffffffffffffffff), v1420
    0x1438: MSTORE v1408(0x0), v1436
    0x1439: v1439(0x20) = CONST 
    0x143b: v143b(0x20) = ADD v1439(0x20), v1408(0x0)
    0x143e: MSTORE v143b(0x20), v1406(0x6)
    0x143f: v143f(0x20) = CONST 
    0x1441: v1441(0x40) = ADD v143f(0x20), v143b(0x20)
    0x1442: v1442(0x0) = CONST 
    0x1444: v1444 = SHA3 v1442(0x0), v1441(0x40)
    0x1445: v1445(0x0) = CONST 
    0x1448: v1448 = SLOAD v1444
    0x144a: v144a(0x100) = CONST 
    0x144d: v144d(0x1) = EXP v144a(0x100), v1445(0x0)
    0x144f: v144f = DIV v1448, v144d(0x1)
    0x1450: v1450(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1465: v1465 = AND v1450(0xffffffffffffffffffffffffffffffffffffffff), v144f
    0x1466: v1466(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x147b: v147b = AND v1466(0xffffffffffffffffffffffffffffffffffffffff), v1465
    0x147c: v147c = EQ v147b, v1405(0x0)
    0x147d: v147d(0x14ee) = CONST 
    0x1480: JUMPI v147d(0x14ee), v147c

    Begin block 0x1481
    prev=[0x13ed], succ=[]
    =================================
    0x1481: v1481(0x40) = CONST 
    0x1483: v1483 = MLOAD v1481(0x40)
    0x1484: v1484(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x14a6: MSTORE v1483, v1484(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14a7: v14a7(0x4) = CONST 
    0x14a9: v14a9 = ADD v14a7(0x4), v1483
    0x14ac: v14ac(0x20) = CONST 
    0x14ae: v14ae = ADD v14ac(0x20), v14a9
    0x14b1: v14b1(0x20) = SUB v14ae, v14a9
    0x14b3: MSTORE v14a9, v14b1(0x20)
    0x14b4: v14b4(0xe) = CONST 
    0x14b7: MSTORE v14ae, v14b4(0xe)
    0x14b8: v14b8(0x20) = CONST 
    0x14ba: v14ba = ADD v14b8(0x20), v14ae
    0x14bc: v14bc(0x616c72656164792061646465642e000000000000000000000000000000000000) = CONST 
    0x14de: MSTORE v14ba, v14bc(0x616c72656164792061646465642e000000000000000000000000000000000000)
    0x14e0: v14e0(0x20) = CONST 
    0x14e2: v14e2 = ADD v14e0(0x20), v14ba
    0x14e6: v14e6(0x40) = CONST 
    0x14e8: v14e8 = MLOAD v14e6(0x40)
    0x14eb: v14eb(0x64) = SUB v14e2, v14e8
    0x14ed: REVERT v14e8, v14eb(0x64)

    Begin block 0x14ee
    prev=[0x13ed], succ=[0x40f]
    =================================
    0x14ef: v14ef(0x5) = CONST 
    0x14f4: v14f4(0x1) = CONST 
    0x14f7: v14f7 = SLOAD v14ef(0x5)
    0x14f8: v14f8 = ADD v14f7, v14f4(0x1)
    0x14fb: SSTORE v14ef(0x5), v14f8
    0x1500: v1500(0x1) = CONST 
    0x1503: v1503 = SUB v14f8, v1500(0x1)
    0x1505: v1505(0x0) = CONST 
    0x1507: MSTORE v1505(0x0), v14ef(0x5)
    0x1508: v1508(0x20) = CONST 
    0x150a: v150a(0x0) = CONST 
    0x150c: v150c = SHA3 v150a(0x0), v1508(0x20)
    0x150d: v150d = ADD v150c, v1503
    0x150e: v150e(0x0) = CONST 
    0x1516: v1516(0x100) = CONST 
    0x1519: v1519(0x1) = EXP v1516(0x100), v150e(0x0)
    0x151b: v151b = SLOAD v150d
    0x151d: v151d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1532: v1532(0xffffffffffffffffffffffffffffffffffffffff) = MUL v151d(0xffffffffffffffffffffffffffffffffffffffff), v1519(0x1)
    0x1533: v1533(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1532(0xffffffffffffffffffffffffffffffffffffffff)
    0x1534: v1534 = AND v1533(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v151b
    0x1537: v1537(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x154c: v154c = AND v1537(0xffffffffffffffffffffffffffffffffffffffff), v3df
    0x154d: v154d = MUL v154c, v1519(0x1)
    0x154e: v154e = OR v154d, v1534
    0x1550: SSTORE v150d, v154e
    0x1553: v1553(0x6) = CONST 
    0x1555: v1555(0x0) = CONST 
    0x1558: v1558(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x156d: v156d = AND v1558(0xffffffffffffffffffffffffffffffffffffffff), v3df
    0x156e: v156e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1583: v1583 = AND v156e(0xffffffffffffffffffffffffffffffffffffffff), v156d
    0x1585: MSTORE v1555(0x0), v1583
    0x1586: v1586(0x20) = CONST 
    0x1588: v1588(0x20) = ADD v1586(0x20), v1555(0x0)
    0x158b: MSTORE v1588(0x20), v1553(0x6)
    0x158c: v158c(0x20) = CONST 
    0x158e: v158e(0x40) = ADD v158c(0x20), v1588(0x20)
    0x158f: v158f(0x0) = CONST 
    0x1591: v1591 = SHA3 v158f(0x0), v158e(0x40)
    0x1592: v1592(0x0) = CONST 
    0x1594: v1594(0x100) = CONST 
    0x1597: v1597(0x1) = EXP v1594(0x100), v1592(0x0)
    0x1599: v1599 = SLOAD v1591
    0x159b: v159b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15b0: v15b0(0xffffffffffffffffffffffffffffffffffffffff) = MUL v159b(0xffffffffffffffffffffffffffffffffffffffff), v1597(0x1)
    0x15b1: v15b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v15b0(0xffffffffffffffffffffffffffffffffffffffff)
    0x15b2: v15b2 = AND v15b1(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1599
    0x15b5: v15b5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x15ca: v15ca = AND v15b5(0xffffffffffffffffffffffffffffffffffffffff), v3ff
    0x15cb: v15cb = MUL v15ca, v1597(0x1)
    0x15cc: v15cc = OR v15cb, v15b2
    0x15ce: SSTORE v1591, v15cc
    0x15d2: JUMP v3ae(0x40f)

    Begin block 0x40f
    prev=[0x14ee], succ=[]
    =================================
    0x410: STOP 

}

function getAmountOut(uint256,uint256,uint256)() public {
    Begin block 0xac
    prev=[], succ=[0xb4, 0xb8]
    =================================
    0xad: vad = CALLVALUE 
    0xaf: vaf = ISZERO vad
    0xb0: vb0(0xb8) = CONST 
    0xb3: JUMPI vb0(0xb8), vaf

    Begin block 0xb4
    prev=[0xac], succ=[]
    =================================
    0xb4: vb4(0x0) = CONST 
    0xb7: REVERT vb4(0x0), vb4(0x0)

    Begin block 0xb8
    prev=[0xac], succ=[0xcb, 0xcf]
    =================================
    0xba: vba(0xf9) = CONST 
    0xbd: vbd(0x4) = CONST 
    0xc0: vc0 = CALLDATASIZE 
    0xc1: vc1 = SUB vc0, vbd(0x4)
    0xc2: vc2(0x60) = CONST 
    0xc5: vc5 = LT vc1, vc2(0x60)
    0xc6: vc6 = ISZERO vc5
    0xc7: vc7(0xcf) = CONST 
    0xca: JUMPI vc7(0xcf), vc6

    Begin block 0xcb
    prev=[0xb8], succ=[]
    =================================
    0xcb: vcb(0x0) = CONST 
    0xce: REVERT vcb(0x0), vcb(0x0)

    Begin block 0xcf
    prev=[0xb8], succ=[0x4110xac]
    =================================
    0xd1: vd1 = ADD vbd(0x4), vc1
    0xd5: vd5 = CALLDATALOAD vbd(0x4)
    0xd7: vd7(0x20) = CONST 
    0xd9: vd9(0x24) = ADD vd7(0x20), vbd(0x4)
    0xdf: vdf = CALLDATALOAD vd9(0x24)
    0xe1: ve1(0x20) = CONST 
    0xe3: ve3(0x44) = ADD ve1(0x20), vd9(0x24)
    0xe9: ve9 = CALLDATALOAD ve3(0x44)
    0xeb: veb(0x20) = CONST 
    0xed: ved(0x64) = ADD veb(0x20), ve3(0x44)
    0xf5: vf5(0x411) = CONST 
    0xf8: JUMP vf5(0x411)

    Begin block 0x4110xac
    prev=[0xcf], succ=[0x41b0xac, 0x46b0xac]
    =================================
    0x4120xac: vac412(0x0) = CONST 
    0x4160xac: vac416 = GT vd5, vac412(0x0)
    0x4170xac: vac417(0x46b) = CONST 
    0x41a0xac: JUMPI vac417(0x46b), vac416

    Begin block 0x41b0xac
    prev=[0x4110xac], succ=[]
    =================================
    0x41b0xac: vac41b(0x40) = CONST 
    0x41d0xac: vac41d = MLOAD vac41b(0x40)
    0x41e0xac: vac41e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4400xac: MSTORE vac41d, vac41e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4410xac: vac441(0x4) = CONST 
    0x4430xac: vac443 = ADD vac441(0x4), vac41d
    0x4460xac: vac446(0x20) = CONST 
    0x4480xac: vac448 = ADD vac446(0x20), vac443
    0x44b0xac: vac44b(0x20) = SUB vac448, vac443
    0x44d0xac: MSTORE vac443, vac44b(0x20)
    0x44e0xac: vac44e(0x30) = CONST 
    0x4510xac: MSTORE vac448, vac44e(0x30)
    0x4520xac: vac452(0x20) = CONST 
    0x4540xac: vac454 = ADD vac452(0x20), vac448
    0x4560xac: vac456(0x15d4) = CONST 
    0x4590xac: vac459(0x30) = CONST 
    0x45c0xac: CODECOPY vac454, vac456(0x15d4), vac459(0x30)
    0x45d0xac: vac45d(0x40) = CONST 
    0x45f0xac: vac45f = ADD vac45d(0x40), vac454
    0x4630xac: vac463(0x40) = CONST 
    0x4650xac: vac465 = MLOAD vac463(0x40)
    0x4680xac: vac468(0x84) = SUB vac45f, vac465
    0x46a0xac: REVERT vac465, vac468(0x84)

    Begin block 0x46b0xac
    prev=[0x4110xac], succ=[0x47b0xac, 0x4760xac]
    =================================
    0x46c0xac: vac46c(0x0) = CONST 
    0x46f0xac: vac46f = GT vdf, vac46c(0x0)
    0x4710xac: vac471 = ISZERO vac46f
    0x4720xac: vac472(0x47b) = CONST 
    0x4750xac: JUMPI vac472(0x47b), vac471

    Begin block 0x47b0xac
    prev=[0x46b0xac, 0x4760xac], succ=[0x4800xac, 0x4d00xac]
    =================================
    0x47b0xac_0x0: v47bac_0 = PHI vac47a, vac46f
    0x47c0xac: vac47c(0x4d0) = CONST 
    0x47f0xac: JUMPI vac47c(0x4d0), v47bac_0

    Begin block 0x4800xac
    prev=[0x47b0xac], succ=[]
    =================================
    0x4800xac: vac480(0x40) = CONST 
    0x4820xac: vac482 = MLOAD vac480(0x40)
    0x4830xac: vac483(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x4a50xac: MSTORE vac482, vac483(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4a60xac: vac4a6(0x4) = CONST 
    0x4a80xac: vac4a8 = ADD vac4a6(0x4), vac482
    0x4ab0xac: vac4ab(0x20) = CONST 
    0x4ad0xac: vac4ad = ADD vac4ab(0x20), vac4a8
    0x4b00xac: vac4b0(0x20) = SUB vac4ad, vac4a8
    0x4b20xac: MSTORE vac4a8, vac4b0(0x20)
    0x4b30xac: vac4b3(0x2d) = CONST 
    0x4b60xac: MSTORE vac4ad, vac4b3(0x2d)
    0x4b70xac: vac4b7(0x20) = CONST 
    0x4b90xac: vac4b9 = ADD vac4b7(0x20), vac4ad
    0x4bb0xac: vac4bb(0x1604) = CONST 
    0x4be0xac: vac4be(0x2d) = CONST 
    0x4c10xac: CODECOPY vac4b9, vac4bb(0x1604), vac4be(0x2d)
    0x4c20xac: vac4c2(0x40) = CONST 
    0x4c40xac: vac4c4 = ADD vac4c2(0x40), vac4b9
    0x4c80xac: vac4c8(0x40) = CONST 
    0x4ca0xac: vac4ca = MLOAD vac4c8(0x40)
    0x4cd0xac: vac4cd(0x84) = SUB vac4c4, vac4ca
    0x4cf0xac: REVERT vac4ca, vac4cd(0x84)

    Begin block 0x4d00xac
    prev=[0x47b0xac], succ=[0x4f30xac, 0x4f40xac]
    =================================
    0x4d10xac: vac4d1(0x0) = CONST 
    0x4d30xac: vac4d3(0x3e5) = CONST 
    0x4d70xac: vac4d7 = MUL vd5, vac4d3(0x3e5)
    0x4da0xac: vac4da(0x0) = CONST 
    0x4de0xac: vac4de = MUL vac4d7, ve9
    0x4e10xac: vac4e1(0x0) = CONST 
    0x4e40xac: vac4e4(0x3e8) = CONST 
    0x4e80xac: vac4e8 = MUL vdf, vac4e4(0x3e8)
    0x4e90xac: vac4e9 = ADD vac4e8, vac4d7
    0x4ef0xac: vac4ef(0x4f4) = CONST 
    0x4f20xac: JUMPI vac4ef(0x4f4), vac4e9

    Begin block 0x4f30xac
    prev=[0x4d00xac], succ=[]
    =================================
    0x4f30xac: THROW 

    Begin block 0x4f40xac
    prev=[0x4d00xac], succ=[0xf9]
    =================================
    0x4f50xac: vac4f5 = DIV vac4de, vac4e9
    0x5000xac: JUMP vba(0xf9)

    Begin block 0xf9
    prev=[0x4f40xac], succ=[]
    =================================
    0xfa: vfa(0x40) = CONST 
    0xfc: vfc = MLOAD vfa(0x40)
    0x100: MSTORE vfc, vac4f5
    0x101: v101(0x20) = CONST 
    0x103: v103 = ADD v101(0x20), vfc
    0x107: v107(0x40) = CONST 
    0x109: v109 = MLOAD v107(0x40)
    0x10c: v10c(0x20) = SUB v103, v109
    0x10e: RETURN v109, v10c(0x20)

    Begin block 0x4760xac
    prev=[0x46b0xac], succ=[0x47b0xac]
    =================================
    0x4770xac: vac477(0x0) = CONST 
    0x47a0xac: vac47a = GT ve9, vac477(0x0)

}

