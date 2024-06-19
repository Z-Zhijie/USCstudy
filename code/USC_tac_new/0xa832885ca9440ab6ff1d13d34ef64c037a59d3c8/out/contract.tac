function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x35d9]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x359b: v359b(0x35d9) = CONST 
    0x359c: JUMPI v359b(0x35d9), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x35dc]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x95ea7b3) = CONST 
    0x3b: v3b = EQ v34, v35(0x95ea7b3)
    0x359d: v359d(0x35dc) = CONST 
    0x359e: JUMPI v359d(0x35dc), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x35df, 0x4b]
    =================================
    0x41: v41(0x18160ddd) = CONST 
    0x46: v46 = EQ v41(0x18160ddd), v34
    0x359f: v359f(0x35df) = CONST 
    0x35a0: JUMPI v359f(0x35df), v46

    Begin block 0x35df
    prev=[0x40], succ=[]
    =================================
    0x35e0: v35e0(0x1bc) = CONST 
    0x35e1: CALLPRIVATE v35e0(0x1bc)

    Begin block 0x4b
    prev=[0x40], succ=[0x35e2, 0x56]
    =================================
    0x4c: v4c(0x23b872dd) = CONST 
    0x51: v51 = EQ v4c(0x23b872dd), v34
    0x35a1: v35a1(0x35e2) = CONST 
    0x35a2: JUMPI v35a1(0x35e2), v51

    Begin block 0x35e2
    prev=[0x4b], succ=[]
    =================================
    0x35e3: v35e3(0x1e3) = CONST 
    0x35e4: CALLPRIVATE v35e3(0x1e3)

    Begin block 0x56
    prev=[0x4b], succ=[0x35e5, 0x61]
    =================================
    0x57: v57(0x3c584d86) = CONST 
    0x5c: v5c = EQ v57(0x3c584d86), v34
    0x35a3: v35a3(0x35e5) = CONST 
    0x35a4: JUMPI v35a3(0x35e5), v5c

    Begin block 0x35e5
    prev=[0x56], succ=[]
    =================================
    0x35e6: v35e6(0x20d) = CONST 
    0x35e7: CALLPRIVATE v35e6(0x20d)

    Begin block 0x61
    prev=[0x56], succ=[0x35e8, 0x6c]
    =================================
    0x62: v62(0x3f4ba83a) = CONST 
    0x67: v67 = EQ v62(0x3f4ba83a), v34
    0x35a5: v35a5(0x35e8) = CONST 
    0x35a6: JUMPI v35a5(0x35e8), v67

    Begin block 0x35e8
    prev=[0x61], succ=[]
    =================================
    0x35e9: v35e9(0x227) = CONST 
    0x35ea: CALLPRIVATE v35e9(0x227)

    Begin block 0x6c
    prev=[0x61], succ=[0x35eb, 0x77]
    =================================
    0x6d: v6d(0x40c10f19) = CONST 
    0x72: v72 = EQ v6d(0x40c10f19), v34
    0x35a7: v35a7(0x35eb) = CONST 
    0x35a8: JUMPI v35a7(0x35eb), v72

    Begin block 0x35eb
    prev=[0x6c], succ=[]
    =================================
    0x35ec: v35ec(0x23c) = CONST 
    0x35ed: CALLPRIVATE v35ec(0x23c)

    Begin block 0x77
    prev=[0x6c], succ=[0x35ee, 0x82]
    =================================
    0x78: v78(0x42966c68) = CONST 
    0x7d: v7d = EQ v78(0x42966c68), v34
    0x35a9: v35a9(0x35ee) = CONST 
    0x35aa: JUMPI v35a9(0x35ee), v7d

    Begin block 0x35ee
    prev=[0x77], succ=[]
    =================================
    0x35ef: v35ef(0x260) = CONST 
    0x35f0: CALLPRIVATE v35ef(0x260)

    Begin block 0x82
    prev=[0x77], succ=[0x35f1, 0x8d]
    =================================
    0x83: v83(0x4e71e0c8) = CONST 
    0x88: v88 = EQ v83(0x4e71e0c8), v34
    0x35ab: v35ab(0x35f1) = CONST 
    0x35ac: JUMPI v35ab(0x35f1), v88

    Begin block 0x35f1
    prev=[0x82], succ=[]
    =================================
    0x35f2: v35f2(0x278) = CONST 
    0x35f3: CALLPRIVATE v35f2(0x278)

    Begin block 0x8d
    prev=[0x82], succ=[0x35f4, 0x98]
    =================================
    0x8e: v8e(0x5bae9ce9) = CONST 
    0x93: v93 = EQ v8e(0x5bae9ce9), v34
    0x35ad: v35ad(0x35f4) = CONST 
    0x35ae: JUMPI v35ad(0x35f4), v93

    Begin block 0x35f4
    prev=[0x8d], succ=[]
    =================================
    0x35f5: v35f5(0x28d) = CONST 
    0x35f6: CALLPRIVATE v35f5(0x28d)

    Begin block 0x98
    prev=[0x8d], succ=[0x35f7, 0xa3]
    =================================
    0x99: v99(0x5c975abb) = CONST 
    0x9e: v9e = EQ v99(0x5c975abb), v34
    0x35af: v35af(0x35f7) = CONST 
    0x35b0: JUMPI v35af(0x35f7), v9e

    Begin block 0x35f7
    prev=[0x98], succ=[]
    =================================
    0x35f8: v35f8(0x2a2) = CONST 
    0x35f9: CALLPRIVATE v35f8(0x2a2)

    Begin block 0xa3
    prev=[0x98], succ=[0x35fa, 0xae]
    =================================
    0xa4: va4(0x636f0cf8) = CONST 
    0xa9: va9 = EQ va4(0x636f0cf8), v34
    0x35b1: v35b1(0x35fa) = CONST 
    0x35b2: JUMPI v35b1(0x35fa), va9

    Begin block 0x35fa
    prev=[0xa3], succ=[]
    =================================
    0x35fb: v35fb(0x2b7) = CONST 
    0x35fc: CALLPRIVATE v35fb(0x2b7)

    Begin block 0xae
    prev=[0xa3], succ=[0x35fd, 0xb9]
    =================================
    0xaf: vaf(0x66188463) = CONST 
    0xb4: vb4 = EQ vaf(0x66188463), v34
    0x35b3: v35b3(0x35fd) = CONST 
    0x35b4: JUMPI v35b3(0x35fd), vb4

    Begin block 0x35fd
    prev=[0xae], succ=[]
    =================================
    0x35fe: v35fe(0x2e8) = CONST 
    0x35ff: CALLPRIVATE v35fe(0x2e8)

    Begin block 0xb9
    prev=[0xae], succ=[0x3600, 0xc4]
    =================================
    0xba: vba(0x662f94c0) = CONST 
    0xbf: vbf = EQ vba(0x662f94c0), v34
    0x35b5: v35b5(0x3600) = CONST 
    0x35b6: JUMPI v35b5(0x3600), vbf

    Begin block 0x3600
    prev=[0xb9], succ=[]
    =================================
    0x3601: v3601(0x30c) = CONST 
    0x3602: CALLPRIVATE v3601(0x30c)

    Begin block 0xc4
    prev=[0xb9], succ=[0x3603, 0xcf]
    =================================
    0xc5: vc5(0x70a08231) = CONST 
    0xca: vca = EQ vc5(0x70a08231), v34
    0x35b7: v35b7(0x3603) = CONST 
    0x35b8: JUMPI v35b7(0x3603), vca

    Begin block 0x3603
    prev=[0xc4], succ=[]
    =================================
    0x3604: v3604(0x32d) = CONST 
    0x3605: CALLPRIVATE v3604(0x32d)

    Begin block 0xcf
    prev=[0xc4], succ=[0x3606, 0xda]
    =================================
    0xd0: vd0(0x8456cb59) = CONST 
    0xd5: vd5 = EQ vd0(0x8456cb59), v34
    0x35b9: v35b9(0x3606) = CONST 
    0x35ba: JUMPI v35b9(0x3606), vd5

    Begin block 0x3606
    prev=[0xcf], succ=[]
    =================================
    0x3607: v3607(0x34e) = CONST 
    0x3608: CALLPRIVATE v3607(0x34e)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x3609]
    =================================
    0xdb: vdb(0x88fa2617) = CONST 
    0xe0: ve0 = EQ vdb(0x88fa2617), v34
    0x35bb: v35bb(0x3609) = CONST 
    0x35bc: JUMPI v35bb(0x3609), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0x360c, 0xf0]
    =================================
    0xe6: ve6(0x8da5cb5b) = CONST 
    0xeb: veb = EQ ve6(0x8da5cb5b), v34
    0x35bd: v35bd(0x360c) = CONST 
    0x35be: JUMPI v35bd(0x360c), veb

    Begin block 0x360c
    prev=[0xe5], succ=[]
    =================================
    0x360d: v360d(0x378) = CONST 
    0x360e: CALLPRIVATE v360d(0x378)

    Begin block 0xf0
    prev=[0xe5], succ=[0x360f, 0xfb]
    =================================
    0xf1: vf1(0x91dc1b1d) = CONST 
    0xf6: vf6 = EQ vf1(0x91dc1b1d), v34
    0x35bf: v35bf(0x360f) = CONST 
    0x35c0: JUMPI v35bf(0x360f), vf6

    Begin block 0x360f
    prev=[0xf0], succ=[]
    =================================
    0x3610: v3610(0x38d) = CONST 
    0x3611: CALLPRIVATE v3610(0x38d)

    Begin block 0xfb
    prev=[0xf0], succ=[0x3612, 0x106]
    =================================
    0xfc: vfc(0xa00d7740) = CONST 
    0x101: v101 = EQ vfc(0xa00d7740), v34
    0x35c1: v35c1(0x3612) = CONST 
    0x35c2: JUMPI v35c1(0x3612), v101

    Begin block 0x3612
    prev=[0xfb], succ=[]
    =================================
    0x3613: v3613(0x3b1) = CONST 
    0x3614: CALLPRIVATE v3613(0x3b1)

    Begin block 0x106
    prev=[0xfb], succ=[0x3615, 0x111]
    =================================
    0x107: v107(0xa69df4b5) = CONST 
    0x10c: v10c = EQ v107(0xa69df4b5), v34
    0x35c3: v35c3(0x3615) = CONST 
    0x35c4: JUMPI v35c3(0x3615), v10c

    Begin block 0x3615
    prev=[0x106], succ=[]
    =================================
    0x3616: v3616(0x3d2) = CONST 
    0x3617: CALLPRIVATE v3616(0x3d2)

    Begin block 0x111
    prev=[0x106], succ=[0x3618, 0x11c]
    =================================
    0x112: v112(0xa9059cbb) = CONST 
    0x117: v117 = EQ v112(0xa9059cbb), v34
    0x35c5: v35c5(0x3618) = CONST 
    0x35c6: JUMPI v35c5(0x3618), v117

    Begin block 0x3618
    prev=[0x111], succ=[]
    =================================
    0x3619: v3619(0x3e7) = CONST 
    0x361a: CALLPRIVATE v3619(0x3e7)

    Begin block 0x11c
    prev=[0x111], succ=[0x361b, 0x127]
    =================================
    0x11d: v11d(0xb199efb5) = CONST 
    0x122: v122 = EQ v11d(0xb199efb5), v34
    0x35c7: v35c7(0x361b) = CONST 
    0x35c8: JUMPI v35c7(0x361b), v122

    Begin block 0x361b
    prev=[0x11c], succ=[]
    =================================
    0x361c: v361c(0x40b) = CONST 
    0x361d: CALLPRIVATE v361c(0x40b)

    Begin block 0x127
    prev=[0x11c], succ=[0x361e, 0x132]
    =================================
    0x128: v128(0xc534ba4b) = CONST 
    0x12d: v12d = EQ v128(0xc534ba4b), v34
    0x35c9: v35c9(0x361e) = CONST 
    0x35ca: JUMPI v35c9(0x361e), v12d

    Begin block 0x361e
    prev=[0x127], succ=[]
    =================================
    0x361f: v361f(0x420) = CONST 
    0x3620: CALLPRIVATE v361f(0x420)

    Begin block 0x132
    prev=[0x127], succ=[0x3621, 0x13d]
    =================================
    0x133: v133(0xcde0a4f8) = CONST 
    0x138: v138 = EQ v133(0xcde0a4f8), v34
    0x35cb: v35cb(0x3621) = CONST 
    0x35cc: JUMPI v35cb(0x3621), v138

    Begin block 0x3621
    prev=[0x132], succ=[]
    =================================
    0x3622: v3622(0x444) = CONST 
    0x3623: CALLPRIVATE v3622(0x444)

    Begin block 0x13d
    prev=[0x132], succ=[0x3624, 0x148]
    =================================
    0x13e: v13e(0xd73dd623) = CONST 
    0x143: v143 = EQ v13e(0xd73dd623), v34
    0x35cd: v35cd(0x3624) = CONST 
    0x35ce: JUMPI v35cd(0x3624), v143

    Begin block 0x3624
    prev=[0x13d], succ=[]
    =================================
    0x3625: v3625(0x465) = CONST 
    0x3626: CALLPRIVATE v3625(0x465)

    Begin block 0x148
    prev=[0x13d], succ=[0x3627, 0x153]
    =================================
    0x149: v149(0xdd62ed3e) = CONST 
    0x14e: v14e = EQ v149(0xdd62ed3e), v34
    0x35cf: v35cf(0x3627) = CONST 
    0x35d0: JUMPI v35cf(0x3627), v14e

    Begin block 0x3627
    prev=[0x148], succ=[]
    =================================
    0x3628: v3628(0x489) = CONST 
    0x3629: CALLPRIVATE v3628(0x489)

    Begin block 0x153
    prev=[0x148], succ=[0x362a, 0x15e]
    =================================
    0x154: v154(0xdd8fee14) = CONST 
    0x159: v159 = EQ v154(0xdd8fee14), v34
    0x35d1: v35d1(0x362a) = CONST 
    0x35d2: JUMPI v35d1(0x362a), v159

    Begin block 0x362a
    prev=[0x153], succ=[]
    =================================
    0x362b: v362b(0x4b0) = CONST 
    0x362c: CALLPRIVATE v362b(0x4b0)

    Begin block 0x15e
    prev=[0x153], succ=[0x362d, 0x169]
    =================================
    0x15f: v15f(0xe30c3978) = CONST 
    0x164: v164 = EQ v15f(0xe30c3978), v34
    0x35d3: v35d3(0x362d) = CONST 
    0x35d4: JUMPI v35d3(0x362d), v164

    Begin block 0x362d
    prev=[0x15e], succ=[]
    =================================
    0x362e: v362e(0x4c5) = CONST 
    0x362f: CALLPRIVATE v362e(0x4c5)

    Begin block 0x169
    prev=[0x15e], succ=[0x3630, 0x174]
    =================================
    0x16a: v16a(0xf2fde38b) = CONST 
    0x16f: v16f = EQ v16a(0xf2fde38b), v34
    0x35d5: v35d5(0x3630) = CONST 
    0x35d6: JUMPI v35d5(0x3630), v16f

    Begin block 0x3630
    prev=[0x169], succ=[]
    =================================
    0x3631: v3631(0x4da) = CONST 
    0x3632: CALLPRIVATE v3631(0x4da)

    Begin block 0x174
    prev=[0x169], succ=[0x35d9, 0x3633]
    =================================
    0x175: v175(0xf83d08ba) = CONST 
    0x17a: v17a = EQ v175(0xf83d08ba), v34
    0x35d7: v35d7(0x3633) = CONST 
    0x35d8: JUMPI v35d7(0x3633), v17a

    Begin block 0x35d9
    prev=[0x0, 0x174], succ=[]
    =================================
    0x35da: v35da(0x17f) = CONST 
    0x35db: CALLPRIVATE v35da(0x17f)

    Begin block 0x3633
    prev=[0x174], succ=[]
    =================================
    0x3634: v3634(0x4fb) = CONST 
    0x3635: CALLPRIVATE v3634(0x4fb)

    Begin block 0x3609
    prev=[0xda], succ=[]
    =================================
    0x360a: v360a(0x363) = CONST 
    0x360b: CALLPRIVATE v360a(0x363)

    Begin block 0x35dc
    prev=[0xd], succ=[]
    =================================
    0x35dd: v35dd(0x184) = CONST 
    0x35de: CALLPRIVATE v35dd(0x184)

}

function 0x16d7(0x16d7arg0x0, 0x16d7arg0x1) private {
    Begin block 0x16d7
    prev=[], succ=[0x173e, 0x1742]
    =================================
    0x16d8: v16d8(0x2) = CONST 
    0x16da: v16da = SLOAD v16d8(0x2)
    0x16db: v16db(0x40) = CONST 
    0x16de: v16de = MLOAD v16db(0x40)
    0x16df: v16df(0x27e235e300000000000000000000000000000000000000000000000000000000) = CONST 
    0x1701: MSTORE v16de, v16df(0x27e235e300000000000000000000000000000000000000000000000000000000)
    0x1702: v1702(0x1) = CONST 
    0x1704: v1704(0xa0) = CONST 
    0x1706: v1706(0x2) = CONST 
    0x1708: v1708(0x10000000000000000000000000000000000000000) = EXP v1706(0x2), v1704(0xa0)
    0x1709: v1709(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1708(0x10000000000000000000000000000000000000000), v1702(0x1)
    0x170c: v170c = AND v1709(0xffffffffffffffffffffffffffffffffffffffff), v16d7arg0
    0x170d: v170d(0x4) = CONST 
    0x1710: v1710 = ADD v16de, v170d(0x4)
    0x1711: MSTORE v1710, v170c
    0x1713: v1713 = MLOAD v16db(0x40)
    0x1714: v1714(0x0) = CONST 
    0x171a: v171a = AND v16da, v1709(0xffffffffffffffffffffffffffffffffffffffff)
    0x171c: v171c(0x27e235e3) = CONST 
    0x1722: v1722(0x24) = CONST 
    0x1726: v1726 = ADD v16de, v1722(0x24)
    0x1728: v1728(0x20) = CONST 
    0x1730: v1730(0x0) = SUB v16de, v1713
    0x1731: v1731(0x24) = ADD v1730(0x0), v1722(0x24)
    0x1736: v1736 = EXTCODESIZE v171a
    0x1737: v1737 = ISZERO v1736
    0x1739: v1739 = ISZERO v1737
    0x173a: v173a(0x1742) = CONST 
    0x173d: JUMPI v173a(0x1742), v1739

    Begin block 0x173e
    prev=[0x16d7], succ=[]
    =================================
    0x173e: v173e(0x0) = CONST 
    0x1741: REVERT v173e(0x0), v173e(0x0)

    Begin block 0x1742
    prev=[0x16d7], succ=[0x174d, 0x1756]
    =================================
    0x1744: v1744 = GAS 
    0x1745: v1745 = CALL v1744, v171a, v1714(0x0), v1713, v1731(0x24), v1713, v1728(0x20)
    0x1746: v1746 = ISZERO v1745
    0x1748: v1748 = ISZERO v1746
    0x1749: v1749(0x1756) = CONST 
    0x174c: JUMPI v1749(0x1756), v1748

    Begin block 0x174d
    prev=[0x1742], succ=[]
    =================================
    0x174d: v174d = RETURNDATASIZE 
    0x174e: v174e(0x0) = CONST 
    0x1751: RETURNDATACOPY v174e(0x0), v174e(0x0), v174d
    0x1752: v1752 = RETURNDATASIZE 
    0x1753: v1753(0x0) = CONST 
    0x1755: REVERT v1753(0x0), v1752

    Begin block 0x1756
    prev=[0x1742], succ=[0x1768, 0x176c]
    =================================
    0x175b: v175b(0x40) = CONST 
    0x175d: v175d = MLOAD v175b(0x40)
    0x175e: v175e = RETURNDATASIZE 
    0x175f: v175f(0x20) = CONST 
    0x1762: v1762 = LT v175e, v175f(0x20)
    0x1763: v1763 = ISZERO v1762
    0x1764: v1764(0x176c) = CONST 
    0x1767: JUMPI v1764(0x176c), v1763

    Begin block 0x1768
    prev=[0x1756], succ=[]
    =================================
    0x1768: v1768(0x0) = CONST 
    0x176b: REVERT v1768(0x0), v1768(0x0)

    Begin block 0x176c
    prev=[0x1756], succ=[]
    =================================
    0x176e: v176e = MLOAD v175d
    0x1773: RETURNPRIVATE v16d7arg1, v176e

}

function fallback()() public {
    Begin block 0x17f
    prev=[], succ=[]
    =================================
    0x180: v180(0x0) = CONST 
    0x183: REVERT v180(0x0), v180(0x0)

}

function approve(address,uint256)() public {
    Begin block 0x184
    prev=[], succ=[0x18c, 0x190]
    =================================
    0x185: v185 = CALLVALUE 
    0x187: v187 = ISZERO v185
    0x188: v188(0x190) = CONST 
    0x18b: JUMPI v188(0x190), v187

    Begin block 0x18c
    prev=[0x184], succ=[]
    =================================
    0x18c: v18c(0x0) = CONST 
    0x18f: REVERT v18c(0x0), v18c(0x0)

    Begin block 0x190
    prev=[0x184], succ=[0x510]
    =================================
    0x192: v192(0x2fd4) = CONST 
    0x195: v195(0x1) = CONST 
    0x197: v197(0xa0) = CONST 
    0x199: v199(0x2) = CONST 
    0x19b: v19b(0x10000000000000000000000000000000000000000) = EXP v199(0x2), v197(0xa0)
    0x19c: v19c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19b(0x10000000000000000000000000000000000000000), v195(0x1)
    0x19d: v19d(0x4) = CONST 
    0x19f: v19f = CALLDATALOAD v19d(0x4)
    0x1a0: v1a0 = AND v19f, v19c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a1: v1a1(0x24) = CONST 
    0x1a3: v1a3 = CALLDATALOAD v1a1(0x24)
    0x1a4: v1a4(0x510) = CONST 
    0x1a7: JUMP v1a4(0x510)

    Begin block 0x510
    prev=[0x190], succ=[0x55f, 0x563]
    =================================
    0x511: v511(0x3) = CONST 
    0x513: v513 = SLOAD v511(0x3)
    0x514: v514(0x40) = CONST 
    0x517: v517 = MLOAD v514(0x40)
    0x518: v518(0xe0) = CONST 
    0x51a: v51a(0x2) = CONST 
    0x51c: v51c(0x100000000000000000000000000000000000000000000000000000000) = EXP v51a(0x2), v518(0xe0)
    0x51d: v51d(0x7ccce851) = CONST 
    0x522: v522(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v51d(0x7ccce851), v51c(0x100000000000000000000000000000000000000000000000000000000)
    0x524: MSTORE v517, v522(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x525: v525(0x1) = CONST 
    0x527: v527(0xa0) = CONST 
    0x529: v529(0x2) = CONST 
    0x52b: v52b(0x10000000000000000000000000000000000000000) = EXP v529(0x2), v527(0xa0)
    0x52c: v52c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v52b(0x10000000000000000000000000000000000000000), v525(0x1)
    0x52f: v52f = AND v1a0, v52c(0xffffffffffffffffffffffffffffffffffffffff)
    0x530: v530(0x4) = CONST 
    0x533: v533 = ADD v517, v530(0x4)
    0x534: MSTORE v533, v52f
    0x536: v536 = MLOAD v514(0x40)
    0x537: v537(0x0) = CONST 
    0x53c: v53c = AND v52c(0xffffffffffffffffffffffffffffffffffffffff), v513
    0x53e: v53e(0x7ccce851) = CONST 
    0x544: v544(0x24) = CONST 
    0x548: v548 = ADD v517, v544(0x24)
    0x54a: v54a(0x20) = CONST 
    0x551: v551(0x0) = SUB v517, v536
    0x552: v552(0x24) = ADD v551(0x0), v544(0x24)
    0x557: v557 = EXTCODESIZE v53c
    0x558: v558 = ISZERO v557
    0x55a: v55a = ISZERO v558
    0x55b: v55b(0x563) = CONST 
    0x55e: JUMPI v55b(0x563), v55a

    Begin block 0x55f
    prev=[0x510], succ=[]
    =================================
    0x55f: v55f(0x0) = CONST 
    0x562: REVERT v55f(0x0), v55f(0x0)

    Begin block 0x563
    prev=[0x510], succ=[0x56e, 0x577]
    =================================
    0x565: v565 = GAS 
    0x566: v566 = CALL v565, v53c, v537(0x0), v536, v552(0x24), v536, v54a(0x20)
    0x567: v567 = ISZERO v566
    0x569: v569 = ISZERO v567
    0x56a: v56a(0x577) = CONST 
    0x56d: JUMPI v56a(0x577), v569

    Begin block 0x56e
    prev=[0x563], succ=[]
    =================================
    0x56e: v56e = RETURNDATASIZE 
    0x56f: v56f(0x0) = CONST 
    0x572: RETURNDATACOPY v56f(0x0), v56f(0x0), v56e
    0x573: v573 = RETURNDATASIZE 
    0x574: v574(0x0) = CONST 
    0x576: REVERT v574(0x0), v573

    Begin block 0x577
    prev=[0x563], succ=[0x589, 0x58d]
    =================================
    0x57c: v57c(0x40) = CONST 
    0x57e: v57e = MLOAD v57c(0x40)
    0x57f: v57f = RETURNDATASIZE 
    0x580: v580(0x20) = CONST 
    0x583: v583 = LT v57f, v580(0x20)
    0x584: v584 = ISZERO v583
    0x585: v585(0x58d) = CONST 
    0x588: JUMPI v585(0x58d), v584

    Begin block 0x589
    prev=[0x577], succ=[]
    =================================
    0x589: v589(0x0) = CONST 
    0x58c: REVERT v589(0x0), v589(0x0)

    Begin block 0x58d
    prev=[0x577], succ=[0x595, 0x5d2]
    =================================
    0x58f: v58f = MLOAD v57e
    0x590: v590 = ISZERO v58f
    0x591: v591(0x5d2) = CONST 
    0x594: JUMPI v591(0x5d2), v590

    Begin block 0x595
    prev=[0x58d], succ=[]
    =================================
    0x595: v595(0x40) = CONST 
    0x598: v598 = MLOAD v595(0x40)
    0x599: v599(0xe5) = CONST 
    0x59b: v59b(0x2) = CONST 
    0x59d: v59d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v59b(0x2), v599(0xe5)
    0x59e: v59e(0x461bcd) = CONST 
    0x5a2: v5a2(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v59e(0x461bcd), v59d(0x2000000000000000000000000000000000000000000000000000000000)
    0x5a4: MSTORE v598, v5a2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5a5: v5a5(0x20) = CONST 
    0x5a7: v5a7(0x4) = CONST 
    0x5aa: v5aa = ADD v598, v5a7(0x4)
    0x5ab: MSTORE v5aa, v5a5(0x20)
    0x5ac: v5ac(0x1c) = CONST 
    0x5ae: v5ae(0x24) = CONST 
    0x5b1: v5b1 = ADD v598, v5ae(0x24)
    0x5b2: MSTORE v5b1, v5ac(0x1c)
    0x5b3: v5b3(0x0) = CONST 
    0x5b6: v5b6 = MLOAD v5b3(0x0)
    0x5b7: v5b7(0x20) = CONST 
    0x5b9: v5b9(0x2f6a) = CONST 
    0x5c1: MSTORE v5b3(0x0), v5b6
    0x5c2: v5c2(0x44) = CONST 
    0x5c5: v5c5 = ADD v598, v5c2(0x44)
    0x5c6: MSTORE v5c5, v363a(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x5c8: v5c8 = MLOAD v595(0x40)
    0x5cc: v5cc(0x0) = SUB v598, v5c8
    0x5cd: v5cd(0x64) = CONST 
    0x5cf: v5cf(0x64) = ADD v5cd(0x64), v5cc(0x0)
    0x5d1: REVERT v5c8, v5cf(0x64)
    0x363a: v363a(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x5d2
    prev=[0x58d], succ=[0x620, 0x624]
    =================================
    0x5d3: v5d3(0x3) = CONST 
    0x5d5: v5d5 = SLOAD v5d3(0x3)
    0x5d6: v5d6(0x40) = CONST 
    0x5d9: v5d9 = MLOAD v5d6(0x40)
    0x5da: v5da(0xe0) = CONST 
    0x5dc: v5dc(0x2) = CONST 
    0x5de: v5de(0x100000000000000000000000000000000000000000000000000000000) = EXP v5dc(0x2), v5da(0xe0)
    0x5df: v5df(0x7ccce851) = CONST 
    0x5e4: v5e4(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v5df(0x7ccce851), v5de(0x100000000000000000000000000000000000000000000000000000000)
    0x5e6: MSTORE v5d9, v5e4(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x5e7: v5e7 = CALLER 
    0x5e8: v5e8(0x4) = CONST 
    0x5eb: v5eb = ADD v5d9, v5e8(0x4)
    0x5ee: MSTORE v5eb, v5e7
    0x5f0: v5f0 = MLOAD v5d6(0x40)
    0x5f3: v5f3(0x1) = CONST 
    0x5f5: v5f5(0xa0) = CONST 
    0x5f7: v5f7(0x2) = CONST 
    0x5f9: v5f9(0x10000000000000000000000000000000000000000) = EXP v5f7(0x2), v5f5(0xa0)
    0x5fa: v5fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5f9(0x10000000000000000000000000000000000000000), v5f3(0x1)
    0x5fb: v5fb = AND v5fa(0xffffffffffffffffffffffffffffffffffffffff), v5d5
    0x5fd: v5fd(0x7ccce851) = CONST 
    0x603: v603(0x24) = CONST 
    0x607: v607 = ADD v5d9, v603(0x24)
    0x609: v609(0x20) = CONST 
    0x611: v611(0x0) = SUB v5d9, v5f0
    0x612: v612(0x24) = ADD v611(0x0), v603(0x24)
    0x614: v614(0x0) = CONST 
    0x618: v618 = EXTCODESIZE v5fb
    0x619: v619 = ISZERO v618
    0x61b: v61b = ISZERO v619
    0x61c: v61c(0x624) = CONST 
    0x61f: JUMPI v61c(0x624), v61b

    Begin block 0x620
    prev=[0x5d2], succ=[]
    =================================
    0x620: v620(0x0) = CONST 
    0x623: REVERT v620(0x0), v620(0x0)

    Begin block 0x624
    prev=[0x5d2], succ=[0x62f, 0x638]
    =================================
    0x626: v626 = GAS 
    0x627: v627 = CALL v626, v5fb, v614(0x0), v5f0, v612(0x24), v5f0, v609(0x20)
    0x628: v628 = ISZERO v627
    0x62a: v62a = ISZERO v628
    0x62b: v62b(0x638) = CONST 
    0x62e: JUMPI v62b(0x638), v62a

    Begin block 0x62f
    prev=[0x624], succ=[]
    =================================
    0x62f: v62f = RETURNDATASIZE 
    0x630: v630(0x0) = CONST 
    0x633: RETURNDATACOPY v630(0x0), v630(0x0), v62f
    0x634: v634 = RETURNDATASIZE 
    0x635: v635(0x0) = CONST 
    0x637: REVERT v635(0x0), v634

    Begin block 0x638
    prev=[0x624], succ=[0x64a, 0x64e]
    =================================
    0x63d: v63d(0x40) = CONST 
    0x63f: v63f = MLOAD v63d(0x40)
    0x640: v640 = RETURNDATASIZE 
    0x641: v641(0x20) = CONST 
    0x644: v644 = LT v640, v641(0x20)
    0x645: v645 = ISZERO v644
    0x646: v646(0x64e) = CONST 
    0x649: JUMPI v646(0x64e), v645

    Begin block 0x64a
    prev=[0x638], succ=[]
    =================================
    0x64a: v64a(0x0) = CONST 
    0x64d: REVERT v64a(0x0), v64a(0x0)

    Begin block 0x64e
    prev=[0x638], succ=[0x656, 0x693]
    =================================
    0x650: v650 = MLOAD v63f
    0x651: v651 = ISZERO v650
    0x652: v652(0x693) = CONST 
    0x655: JUMPI v652(0x693), v651

    Begin block 0x656
    prev=[0x64e], succ=[]
    =================================
    0x656: v656(0x40) = CONST 
    0x659: v659 = MLOAD v656(0x40)
    0x65a: v65a(0xe5) = CONST 
    0x65c: v65c(0x2) = CONST 
    0x65e: v65e(0x2000000000000000000000000000000000000000000000000000000000) = EXP v65c(0x2), v65a(0xe5)
    0x65f: v65f(0x461bcd) = CONST 
    0x663: v663(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v65f(0x461bcd), v65e(0x2000000000000000000000000000000000000000000000000000000000)
    0x665: MSTORE v659, v663(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x666: v666(0x20) = CONST 
    0x668: v668(0x4) = CONST 
    0x66b: v66b = ADD v659, v668(0x4)
    0x66c: MSTORE v66b, v666(0x20)
    0x66d: v66d(0x1c) = CONST 
    0x66f: v66f(0x24) = CONST 
    0x672: v672 = ADD v659, v66f(0x24)
    0x673: MSTORE v672, v66d(0x1c)
    0x674: v674(0x0) = CONST 
    0x677: v677 = MLOAD v674(0x0)
    0x678: v678(0x20) = CONST 
    0x67a: v67a(0x2f6a) = CONST 
    0x682: MSTORE v674(0x0), v677
    0x683: v683(0x44) = CONST 
    0x686: v686 = ADD v659, v683(0x44)
    0x687: MSTORE v686, v363f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x689: v689 = MLOAD v656(0x40)
    0x68d: v68d(0x0) = SUB v659, v689
    0x68e: v68e(0x64) = CONST 
    0x690: v690(0x64) = ADD v68e(0x64), v68d(0x0)
    0x692: REVERT v689, v690(0x64)
    0x363f: v363f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x693
    prev=[0x64e], succ=[0x6a6, 0x6aa]
    =================================
    0x694: v694(0x1) = CONST 
    0x696: v696 = SLOAD v694(0x1)
    0x697: v697(0xa0) = CONST 
    0x699: v699(0x2) = CONST 
    0x69b: v69b(0x10000000000000000000000000000000000000000) = EXP v699(0x2), v697(0xa0)
    0x69d: v69d = DIV v696, v69b(0x10000000000000000000000000000000000000000)
    0x69e: v69e(0xff) = CONST 
    0x6a0: v6a0 = AND v69e(0xff), v69d
    0x6a1: v6a1 = ISZERO v6a0
    0x6a2: v6a2(0x6aa) = CONST 
    0x6a5: JUMPI v6a2(0x6aa), v6a1

    Begin block 0x6a6
    prev=[0x693], succ=[]
    =================================
    0x6a6: v6a6(0x0) = CONST 
    0x6a9: REVERT v6a6(0x0), v6a6(0x0)

    Begin block 0x6aa
    prev=[0x693], succ=[0x6d0, 0x6d4]
    =================================
    0x6ab: v6ab(0x1) = CONST 
    0x6ad: v6ad = SLOAD v6ab(0x1)
    0x6ae: v6ae(0x1000000000000000000000000000000000000000000) = CONST 
    0x6c6: v6c6 = DIV v6ad, v6ae(0x1000000000000000000000000000000000000000000)
    0x6c7: v6c7(0xff) = CONST 
    0x6c9: v6c9 = AND v6c7(0xff), v6c6
    0x6ca: v6ca = ISZERO v6c9
    0x6cb: v6cb = ISZERO v6ca
    0x6cc: v6cc(0x6d4) = CONST 
    0x6cf: JUMPI v6cc(0x6d4), v6cb

    Begin block 0x6d0
    prev=[0x6aa], succ=[]
    =================================
    0x6d0: v6d0(0x0) = CONST 
    0x6d3: REVERT v6d0(0x0), v6d0(0x0)

    Begin block 0x6d4
    prev=[0x6aa], succ=[0x744, 0x748]
    =================================
    0x6d5: v6d5(0x2) = CONST 
    0x6d7: v6d7 = SLOAD v6d5(0x2)
    0x6d8: v6d8(0x40) = CONST 
    0x6db: v6db = MLOAD v6d8(0x40)
    0x6dc: v6dc(0xda46098c00000000000000000000000000000000000000000000000000000000) = CONST 
    0x6fe: MSTORE v6db, v6dc(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0x6ff: v6ff = CALLER 
    0x700: v700(0x4) = CONST 
    0x703: v703 = ADD v6db, v700(0x4)
    0x704: MSTORE v703, v6ff
    0x705: v705(0x1) = CONST 
    0x707: v707(0xa0) = CONST 
    0x709: v709(0x2) = CONST 
    0x70b: v70b(0x10000000000000000000000000000000000000000) = EXP v709(0x2), v707(0xa0)
    0x70c: v70c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v70b(0x10000000000000000000000000000000000000000), v705(0x1)
    0x70f: v70f = AND v70c(0xffffffffffffffffffffffffffffffffffffffff), v1a0
    0x710: v710(0x24) = CONST 
    0x713: v713 = ADD v6db, v710(0x24)
    0x714: MSTORE v713, v70f
    0x715: v715(0x44) = CONST 
    0x718: v718 = ADD v6db, v715(0x44)
    0x71b: MSTORE v718, v1a3
    0x71d: v71d = MLOAD v6d8(0x40)
    0x721: v721 = AND v6d7, v70c(0xffffffffffffffffffffffffffffffffffffffff)
    0x723: v723(0xda46098c) = CONST 
    0x729: v729(0x64) = CONST 
    0x72d: v72d = ADD v6db, v729(0x64)
    0x72f: v72f(0x0) = CONST 
    0x736: v736(0x0) = SUB v6db, v71d
    0x737: v737(0x64) = ADD v736(0x0), v729(0x64)
    0x73c: v73c = EXTCODESIZE v721
    0x73d: v73d = ISZERO v73c
    0x73f: v73f = ISZERO v73d
    0x740: v740(0x748) = CONST 
    0x743: JUMPI v740(0x748), v73f

    Begin block 0x744
    prev=[0x6d4], succ=[]
    =================================
    0x744: v744(0x0) = CONST 
    0x747: REVERT v744(0x0), v744(0x0)

    Begin block 0x748
    prev=[0x6d4], succ=[0x753, 0x75c]
    =================================
    0x74a: v74a = GAS 
    0x74b: v74b = CALL v74a, v721, v72f(0x0), v71d, v737(0x64), v71d, v72f(0x0)
    0x74c: v74c = ISZERO v74b
    0x74e: v74e = ISZERO v74c
    0x74f: v74f(0x75c) = CONST 
    0x752: JUMPI v74f(0x75c), v74e

    Begin block 0x753
    prev=[0x748], succ=[]
    =================================
    0x753: v753 = RETURNDATASIZE 
    0x754: v754(0x0) = CONST 
    0x757: RETURNDATACOPY v754(0x0), v754(0x0), v753
    0x758: v758 = RETURNDATASIZE 
    0x759: v759(0x0) = CONST 
    0x75b: REVERT v759(0x0), v758

    Begin block 0x75c
    prev=[0x748], succ=[0x2fd4]
    =================================
    0x75f: v75f(0x40) = CONST 
    0x762: v762 = MLOAD v75f(0x40)
    0x765: MSTORE v762, v1a3
    0x767: v767 = MLOAD v75f(0x40)
    0x768: v768(0x1) = CONST 
    0x76a: v76a(0xa0) = CONST 
    0x76c: v76c(0x2) = CONST 
    0x76e: v76e(0x10000000000000000000000000000000000000000) = EXP v76c(0x2), v76a(0xa0)
    0x76f: v76f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v76e(0x10000000000000000000000000000000000000000), v768(0x1)
    0x771: v771 = AND v1a0, v76f(0xffffffffffffffffffffffffffffffffffffffff)
    0x774: v774 = CALLER 
    0x777: v777(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x79b: v79b(0x0) = SUB v762, v767
    0x79c: v79c(0x20) = CONST 
    0x79e: v79e(0x20) = ADD v79c(0x20), v79b(0x0)
    0x7a0: LOG3 v767, v79e(0x20), v777(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v774, v771
    0x7a2: v7a2(0x1) = CONST 
    0x7aa: JUMP v192(0x2fd4)

    Begin block 0x2fd4
    prev=[0x75c], succ=[]
    =================================
    0x2fd5: v2fd5(0x40) = CONST 
    0x2fd8: v2fd8 = MLOAD v2fd5(0x40)
    0x2fda: v2fda = ISZERO v7a2(0x1)
    0x2fdb: v2fdb = ISZERO v2fda
    0x2fdd: MSTORE v2fd8, v2fdb
    0x2fde: v2fde = MLOAD v2fd5(0x40)
    0x2fe2: v2fe2(0x0) = SUB v2fd8, v2fde
    0x2fe3: v2fe3(0x20) = CONST 
    0x2fe5: v2fe5(0x20) = ADD v2fe3(0x20), v2fe2(0x0)
    0x2fe7: RETURN v2fde, v2fe5(0x20)

}

function totalSupply()() public {
    Begin block 0x1bc
    prev=[], succ=[0x1c4, 0x1c8]
    =================================
    0x1bd: v1bd = CALLVALUE 
    0x1bf: v1bf = ISZERO v1bd
    0x1c0: v1c0(0x1c8) = CONST 
    0x1c3: JUMPI v1c0(0x1c8), v1bf

    Begin block 0x1c4
    prev=[0x1bc], succ=[]
    =================================
    0x1c4: v1c4(0x0) = CONST 
    0x1c7: REVERT v1c4(0x0), v1c4(0x0)

    Begin block 0x1c8
    prev=[0x1bc], succ=[0x7ab]
    =================================
    0x1ca: v1ca(0x3007) = CONST 
    0x1cd: v1cd(0x7ab) = CONST 
    0x1d0: JUMP v1cd(0x7ab)

    Begin block 0x7ab
    prev=[0x1c8], succ=[0x806, 0x80a]
    =================================
    0x7ac: v7ac(0x2) = CONST 
    0x7ae: v7ae = SLOAD v7ac(0x2)
    0x7af: v7af(0x40) = CONST 
    0x7b2: v7b2 = MLOAD v7af(0x40)
    0x7b3: v7b3(0x18160ddd00000000000000000000000000000000000000000000000000000000) = CONST 
    0x7d5: MSTORE v7b2, v7b3(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x7d7: v7d7 = MLOAD v7af(0x40)
    0x7d8: v7d8(0x0) = CONST 
    0x7db: v7db(0x1) = CONST 
    0x7dd: v7dd(0xa0) = CONST 
    0x7df: v7df(0x2) = CONST 
    0x7e1: v7e1(0x10000000000000000000000000000000000000000) = EXP v7df(0x2), v7dd(0xa0)
    0x7e2: v7e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7e1(0x10000000000000000000000000000000000000000), v7db(0x1)
    0x7e3: v7e3 = AND v7e2(0xffffffffffffffffffffffffffffffffffffffff), v7ae
    0x7e5: v7e5(0x18160ddd) = CONST 
    0x7eb: v7eb(0x4) = CONST 
    0x7ef: v7ef = ADD v7b2, v7eb(0x4)
    0x7f1: v7f1(0x20) = CONST 
    0x7f8: v7f8(0x0) = SUB v7b2, v7d7
    0x7f9: v7f9(0x4) = ADD v7f8(0x0), v7eb(0x4)
    0x7fe: v7fe = EXTCODESIZE v7e3
    0x7ff: v7ff = ISZERO v7fe
    0x801: v801 = ISZERO v7ff
    0x802: v802(0x80a) = CONST 
    0x805: JUMPI v802(0x80a), v801

    Begin block 0x806
    prev=[0x7ab], succ=[]
    =================================
    0x806: v806(0x0) = CONST 
    0x809: REVERT v806(0x0), v806(0x0)

    Begin block 0x80a
    prev=[0x7ab], succ=[0x815, 0x81e]
    =================================
    0x80c: v80c = GAS 
    0x80d: v80d = CALL v80c, v7e3, v7d8(0x0), v7d7, v7f9(0x4), v7d7, v7f1(0x20)
    0x80e: v80e = ISZERO v80d
    0x810: v810 = ISZERO v80e
    0x811: v811(0x81e) = CONST 
    0x814: JUMPI v811(0x81e), v810

    Begin block 0x815
    prev=[0x80a], succ=[]
    =================================
    0x815: v815 = RETURNDATASIZE 
    0x816: v816(0x0) = CONST 
    0x819: RETURNDATACOPY v816(0x0), v816(0x0), v815
    0x81a: v81a = RETURNDATASIZE 
    0x81b: v81b(0x0) = CONST 
    0x81d: REVERT v81b(0x0), v81a

    Begin block 0x81e
    prev=[0x80a], succ=[0x830, 0x834]
    =================================
    0x823: v823(0x40) = CONST 
    0x825: v825 = MLOAD v823(0x40)
    0x826: v826 = RETURNDATASIZE 
    0x827: v827(0x20) = CONST 
    0x82a: v82a = LT v826, v827(0x20)
    0x82b: v82b = ISZERO v82a
    0x82c: v82c(0x834) = CONST 
    0x82f: JUMPI v82c(0x834), v82b

    Begin block 0x830
    prev=[0x81e], succ=[]
    =================================
    0x830: v830(0x0) = CONST 
    0x833: REVERT v830(0x0), v830(0x0)

    Begin block 0x834
    prev=[0x81e], succ=[0x3007]
    =================================
    0x836: v836 = MLOAD v825
    0x83a: JUMP v1ca(0x3007)

    Begin block 0x3007
    prev=[0x834], succ=[]
    =================================
    0x3008: v3008(0x40) = CONST 
    0x300b: v300b = MLOAD v3008(0x40)
    0x300e: MSTORE v300b, v836
    0x300f: v300f = MLOAD v3008(0x40)
    0x3013: v3013(0x0) = SUB v300b, v300f
    0x3014: v3014(0x20) = CONST 
    0x3016: v3016(0x20) = ADD v3014(0x20), v3013(0x0)
    0x3018: RETURN v300f, v3016(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x1e3
    prev=[], succ=[0x1eb, 0x1ef]
    =================================
    0x1e4: v1e4 = CALLVALUE 
    0x1e6: v1e6 = ISZERO v1e4
    0x1e7: v1e7(0x1ef) = CONST 
    0x1ea: JUMPI v1e7(0x1ef), v1e6

    Begin block 0x1eb
    prev=[0x1e3], succ=[]
    =================================
    0x1eb: v1eb(0x0) = CONST 
    0x1ee: REVERT v1eb(0x0), v1eb(0x0)

    Begin block 0x1ef
    prev=[0x1e3], succ=[0x83b]
    =================================
    0x1f1: v1f1(0x3038) = CONST 
    0x1f4: v1f4(0x1) = CONST 
    0x1f6: v1f6(0xa0) = CONST 
    0x1f8: v1f8(0x2) = CONST 
    0x1fa: v1fa(0x10000000000000000000000000000000000000000) = EXP v1f8(0x2), v1f6(0xa0)
    0x1fb: v1fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fa(0x10000000000000000000000000000000000000000), v1f4(0x1)
    0x1fc: v1fc(0x4) = CONST 
    0x1fe: v1fe = CALLDATALOAD v1fc(0x4)
    0x200: v200 = AND v1fb(0xffffffffffffffffffffffffffffffffffffffff), v1fe
    0x202: v202(0x24) = CONST 
    0x204: v204 = CALLDATALOAD v202(0x24)
    0x205: v205 = AND v204, v1fb(0xffffffffffffffffffffffffffffffffffffffff)
    0x206: v206(0x44) = CONST 
    0x208: v208 = CALLDATALOAD v206(0x44)
    0x209: v209(0x83b) = CONST 
    0x20c: JUMP v209(0x83b)

    Begin block 0x83b
    prev=[0x1ef], succ=[0x851, 0x855]
    =================================
    0x83c: v83c(0x1) = CONST 
    0x83e: v83e = SLOAD v83c(0x1)
    0x83f: v83f(0x0) = CONST 
    0x842: v842(0xa0) = CONST 
    0x844: v844(0x2) = CONST 
    0x846: v846(0x10000000000000000000000000000000000000000) = EXP v844(0x2), v842(0xa0)
    0x848: v848 = DIV v83e, v846(0x10000000000000000000000000000000000000000)
    0x849: v849(0xff) = CONST 
    0x84b: v84b = AND v849(0xff), v848
    0x84c: v84c = ISZERO v84b
    0x84d: v84d(0x855) = CONST 
    0x850: JUMPI v84d(0x855), v84c

    Begin block 0x851
    prev=[0x83b], succ=[]
    =================================
    0x851: v851(0x0) = CONST 
    0x854: REVERT v851(0x0), v851(0x0)

    Begin block 0x855
    prev=[0x83b], succ=[0x8ab, 0x8af]
    =================================
    0x856: v856(0x3) = CONST 
    0x858: v858 = SLOAD v856(0x3)
    0x859: v859(0x40) = CONST 
    0x85c: v85c = MLOAD v859(0x40)
    0x85d: v85d(0xe0) = CONST 
    0x85f: v85f(0x2) = CONST 
    0x861: v861(0x100000000000000000000000000000000000000000000000000000000) = EXP v85f(0x2), v85d(0xe0)
    0x862: v862(0x7ccce851) = CONST 
    0x867: v867(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v862(0x7ccce851), v861(0x100000000000000000000000000000000000000000000000000000000)
    0x869: MSTORE v85c, v867(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x86a: v86a(0x1) = CONST 
    0x86c: v86c(0xa0) = CONST 
    0x86e: v86e(0x2) = CONST 
    0x870: v870(0x10000000000000000000000000000000000000000) = EXP v86e(0x2), v86c(0xa0)
    0x871: v871(0xffffffffffffffffffffffffffffffffffffffff) = SUB v870(0x10000000000000000000000000000000000000000), v86a(0x1)
    0x874: v874 = AND v205, v871(0xffffffffffffffffffffffffffffffffffffffff)
    0x875: v875(0x4) = CONST 
    0x878: v878 = ADD v85c, v875(0x4)
    0x879: MSTORE v878, v874
    0x87b: v87b = MLOAD v859(0x40)
    0x880: v880(0x0) = CONST 
    0x888: v888 = AND v858, v871(0xffffffffffffffffffffffffffffffffffffffff)
    0x88a: v88a(0x7ccce851) = CONST 
    0x890: v890(0x24) = CONST 
    0x894: v894 = ADD v85c, v890(0x24)
    0x896: v896(0x20) = CONST 
    0x89d: v89d(0x0) = SUB v85c, v87b
    0x89e: v89e(0x24) = ADD v89d(0x0), v890(0x24)
    0x8a3: v8a3 = EXTCODESIZE v888
    0x8a4: v8a4 = ISZERO v8a3
    0x8a6: v8a6 = ISZERO v8a4
    0x8a7: v8a7(0x8af) = CONST 
    0x8aa: JUMPI v8a7(0x8af), v8a6

    Begin block 0x8ab
    prev=[0x855], succ=[]
    =================================
    0x8ab: v8ab(0x0) = CONST 
    0x8ae: REVERT v8ab(0x0), v8ab(0x0)

    Begin block 0x8af
    prev=[0x855], succ=[0x8ba, 0x8c3]
    =================================
    0x8b1: v8b1 = GAS 
    0x8b2: v8b2 = CALL v8b1, v888, v880(0x0), v87b, v89e(0x24), v87b, v896(0x20)
    0x8b3: v8b3 = ISZERO v8b2
    0x8b5: v8b5 = ISZERO v8b3
    0x8b6: v8b6(0x8c3) = CONST 
    0x8b9: JUMPI v8b6(0x8c3), v8b5

    Begin block 0x8ba
    prev=[0x8af], succ=[]
    =================================
    0x8ba: v8ba = RETURNDATASIZE 
    0x8bb: v8bb(0x0) = CONST 
    0x8be: RETURNDATACOPY v8bb(0x0), v8bb(0x0), v8ba
    0x8bf: v8bf = RETURNDATASIZE 
    0x8c0: v8c0(0x0) = CONST 
    0x8c2: REVERT v8c0(0x0), v8bf

    Begin block 0x8c3
    prev=[0x8af], succ=[0x8d5, 0x8d9]
    =================================
    0x8c8: v8c8(0x40) = CONST 
    0x8ca: v8ca = MLOAD v8c8(0x40)
    0x8cb: v8cb = RETURNDATASIZE 
    0x8cc: v8cc(0x20) = CONST 
    0x8cf: v8cf = LT v8cb, v8cc(0x20)
    0x8d0: v8d0 = ISZERO v8cf
    0x8d1: v8d1(0x8d9) = CONST 
    0x8d4: JUMPI v8d1(0x8d9), v8d0

    Begin block 0x8d5
    prev=[0x8c3], succ=[]
    =================================
    0x8d5: v8d5(0x0) = CONST 
    0x8d8: REVERT v8d5(0x0), v8d5(0x0)

    Begin block 0x8d9
    prev=[0x8c3], succ=[0x8e1, 0x930]
    =================================
    0x8db: v8db = MLOAD v8ca
    0x8dc: v8dc = ISZERO v8db
    0x8dd: v8dd(0x930) = CONST 
    0x8e0: JUMPI v8dd(0x930), v8dc

    Begin block 0x8e1
    prev=[0x8d9], succ=[]
    =================================
    0x8e1: v8e1(0x40) = CONST 
    0x8e4: v8e4 = MLOAD v8e1(0x40)
    0x8e5: v8e5(0xe5) = CONST 
    0x8e7: v8e7(0x2) = CONST 
    0x8e9: v8e9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v8e7(0x2), v8e5(0xe5)
    0x8ea: v8ea(0x461bcd) = CONST 
    0x8ee: v8ee(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v8ea(0x461bcd), v8e9(0x2000000000000000000000000000000000000000000000000000000000)
    0x8f0: MSTORE v8e4, v8ee(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8f1: v8f1(0x20) = CONST 
    0x8f3: v8f3(0x4) = CONST 
    0x8f6: v8f6 = ADD v8e4, v8f3(0x4)
    0x8f7: MSTORE v8f6, v8f1(0x20)
    0x8f8: v8f8(0x1f) = CONST 
    0x8fa: v8fa(0x24) = CONST 
    0x8fd: v8fd = ADD v8e4, v8fa(0x24)
    0x8fe: MSTORE v8fd, v8f8(0x1f)
    0x8ff: v8ff(0x526563697069656e742063616e6e6f7420626520626c61636b6c697374656400) = CONST 
    0x920: v920(0x44) = CONST 
    0x923: v923 = ADD v8e4, v920(0x44)
    0x924: MSTORE v923, v8ff(0x526563697069656e742063616e6e6f7420626520626c61636b6c697374656400)
    0x926: v926 = MLOAD v8e1(0x40)
    0x92a: v92a(0x0) = SUB v8e4, v926
    0x92b: v92b(0x64) = CONST 
    0x92d: v92d(0x64) = ADD v92b(0x64), v92a(0x0)
    0x92f: REVERT v926, v92d(0x64)

    Begin block 0x930
    prev=[0x8d9], succ=[0x97e, 0x982]
    =================================
    0x931: v931(0x3) = CONST 
    0x933: v933 = SLOAD v931(0x3)
    0x934: v934(0x40) = CONST 
    0x937: v937 = MLOAD v934(0x40)
    0x938: v938(0xe0) = CONST 
    0x93a: v93a(0x2) = CONST 
    0x93c: v93c(0x100000000000000000000000000000000000000000000000000000000) = EXP v93a(0x2), v938(0xe0)
    0x93d: v93d(0x7ccce851) = CONST 
    0x942: v942(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v93d(0x7ccce851), v93c(0x100000000000000000000000000000000000000000000000000000000)
    0x944: MSTORE v937, v942(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x945: v945(0x1) = CONST 
    0x947: v947(0xa0) = CONST 
    0x949: v949(0x2) = CONST 
    0x94b: v94b(0x10000000000000000000000000000000000000000) = EXP v949(0x2), v947(0xa0)
    0x94c: v94c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v94b(0x10000000000000000000000000000000000000000), v945(0x1)
    0x94f: v94f = AND v94c(0xffffffffffffffffffffffffffffffffffffffff), v200
    0x950: v950(0x4) = CONST 
    0x953: v953 = ADD v937, v950(0x4)
    0x954: MSTORE v953, v94f
    0x956: v956 = MLOAD v934(0x40)
    0x95a: v95a = AND v933, v94c(0xffffffffffffffffffffffffffffffffffffffff)
    0x95c: v95c(0x7ccce851) = CONST 
    0x962: v962(0x24) = CONST 
    0x966: v966 = ADD v937, v962(0x24)
    0x968: v968(0x20) = CONST 
    0x96f: v96f(0x0) = SUB v937, v956
    0x970: v970(0x24) = ADD v96f(0x0), v962(0x24)
    0x972: v972(0x0) = CONST 
    0x976: v976 = EXTCODESIZE v95a
    0x977: v977 = ISZERO v976
    0x979: v979 = ISZERO v977
    0x97a: v97a(0x982) = CONST 
    0x97d: JUMPI v97a(0x982), v979

    Begin block 0x97e
    prev=[0x930], succ=[]
    =================================
    0x97e: v97e(0x0) = CONST 
    0x981: REVERT v97e(0x0), v97e(0x0)

    Begin block 0x982
    prev=[0x930], succ=[0x98d, 0x996]
    =================================
    0x984: v984 = GAS 
    0x985: v985 = CALL v984, v95a, v972(0x0), v956, v970(0x24), v956, v968(0x20)
    0x986: v986 = ISZERO v985
    0x988: v988 = ISZERO v986
    0x989: v989(0x996) = CONST 
    0x98c: JUMPI v989(0x996), v988

    Begin block 0x98d
    prev=[0x982], succ=[]
    =================================
    0x98d: v98d = RETURNDATASIZE 
    0x98e: v98e(0x0) = CONST 
    0x991: RETURNDATACOPY v98e(0x0), v98e(0x0), v98d
    0x992: v992 = RETURNDATASIZE 
    0x993: v993(0x0) = CONST 
    0x995: REVERT v993(0x0), v992

    Begin block 0x996
    prev=[0x982], succ=[0x9a8, 0x9ac]
    =================================
    0x99b: v99b(0x40) = CONST 
    0x99d: v99d = MLOAD v99b(0x40)
    0x99e: v99e = RETURNDATASIZE 
    0x99f: v99f(0x20) = CONST 
    0x9a2: v9a2 = LT v99e, v99f(0x20)
    0x9a3: v9a3 = ISZERO v9a2
    0x9a4: v9a4(0x9ac) = CONST 
    0x9a7: JUMPI v9a4(0x9ac), v9a3

    Begin block 0x9a8
    prev=[0x996], succ=[]
    =================================
    0x9a8: v9a8(0x0) = CONST 
    0x9ab: REVERT v9a8(0x0), v9a8(0x0)

    Begin block 0x9ac
    prev=[0x996], succ=[0xa13, 0xa17]
    =================================
    0x9ae: v9ae = MLOAD v99d
    0x9af: v9af(0x3) = CONST 
    0x9b1: v9b1 = SLOAD v9af(0x3)
    0x9b2: v9b2(0x40) = CONST 
    0x9b5: v9b5 = MLOAD v9b2(0x40)
    0x9b6: v9b6(0x91c4529f00000000000000000000000000000000000000000000000000000000) = CONST 
    0x9d8: MSTORE v9b5, v9b6(0x91c4529f00000000000000000000000000000000000000000000000000000000)
    0x9d9: v9d9 = CALLER 
    0x9da: v9da(0x4) = CONST 
    0x9dd: v9dd = ADD v9b5, v9da(0x4)
    0x9de: MSTORE v9dd, v9d9
    0x9e0: v9e0 = MLOAD v9b2(0x40)
    0x9e4: v9e4(0x1) = CONST 
    0x9e6: v9e6(0xa0) = CONST 
    0x9e8: v9e8(0x2) = CONST 
    0x9ea: v9ea(0x10000000000000000000000000000000000000000) = EXP v9e8(0x2), v9e6(0xa0)
    0x9eb: v9eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9ea(0x10000000000000000000000000000000000000000), v9e4(0x1)
    0x9ee: v9ee = AND v9b1, v9eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x9f0: v9f0(0x91c4529f) = CONST 
    0x9f6: v9f6(0x24) = CONST 
    0x9fa: v9fa = ADD v9b5, v9f6(0x24)
    0x9fc: v9fc(0x20) = CONST 
    0xa04: va04(0x0) = SUB v9b5, v9e0
    0xa05: va05(0x24) = ADD va04(0x0), v9f6(0x24)
    0xa07: va07(0x0) = CONST 
    0xa0b: va0b = EXTCODESIZE v9ee
    0xa0c: va0c = ISZERO va0b
    0xa0e: va0e = ISZERO va0c
    0xa0f: va0f(0xa17) = CONST 
    0xa12: JUMPI va0f(0xa17), va0e

    Begin block 0xa13
    prev=[0x9ac], succ=[]
    =================================
    0xa13: va13(0x0) = CONST 
    0xa16: REVERT va13(0x0), va13(0x0)

    Begin block 0xa17
    prev=[0x9ac], succ=[0xa22, 0xa2b]
    =================================
    0xa19: va19 = GAS 
    0xa1a: va1a = CALL va19, v9ee, va07(0x0), v9e0, va05(0x24), v9e0, v9fc(0x20)
    0xa1b: va1b = ISZERO va1a
    0xa1d: va1d = ISZERO va1b
    0xa1e: va1e(0xa2b) = CONST 
    0xa21: JUMPI va1e(0xa2b), va1d

    Begin block 0xa22
    prev=[0xa17], succ=[]
    =================================
    0xa22: va22 = RETURNDATASIZE 
    0xa23: va23(0x0) = CONST 
    0xa26: RETURNDATACOPY va23(0x0), va23(0x0), va22
    0xa27: va27 = RETURNDATASIZE 
    0xa28: va28(0x0) = CONST 
    0xa2a: REVERT va28(0x0), va27

    Begin block 0xa2b
    prev=[0xa17], succ=[0xa3d, 0xa41]
    =================================
    0xa30: va30(0x40) = CONST 
    0xa32: va32 = MLOAD va30(0x40)
    0xa33: va33 = RETURNDATASIZE 
    0xa34: va34(0x20) = CONST 
    0xa37: va37 = LT va33, va34(0x20)
    0xa38: va38 = ISZERO va37
    0xa39: va39(0xa41) = CONST 
    0xa3c: JUMPI va39(0xa41), va38

    Begin block 0xa3d
    prev=[0xa2b], succ=[]
    =================================
    0xa3d: va3d(0x0) = CONST 
    0xa40: REVERT va3d(0x0), va3d(0x0)

    Begin block 0xa41
    prev=[0xa2b], succ=[0xa4f, 0xa4d]
    =================================
    0xa43: va43 = MLOAD va32
    0xa47: va47 = ISZERO v9ae
    0xa49: va49(0xa4f) = CONST 
    0xa4c: JUMPI va49(0xa4f), va47

    Begin block 0xa4f
    prev=[0xa41, 0xa4d], succ=[0xa56, 0xaf1]
    =================================
    0xa4f_0x0: va4f_0 = PHI va43, va47
    0xa50: va50 = ISZERO va4f_0
    0xa51: va51 = ISZERO va50
    0xa52: va52(0xaf1) = CONST 
    0xa55: JUMPI va52(0xaf1), va51

    Begin block 0xa56
    prev=[0xa4f], succ=[]
    =================================
    0xa56: va56(0x40) = CONST 
    0xa59: va59 = MLOAD va56(0x40)
    0xa5a: va5a(0xe5) = CONST 
    0xa5c: va5c(0x2) = CONST 
    0xa5e: va5e(0x2000000000000000000000000000000000000000000000000000000000) = EXP va5c(0x2), va5a(0xe5)
    0xa5f: va5f(0x461bcd) = CONST 
    0xa63: va63(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL va5f(0x461bcd), va5e(0x2000000000000000000000000000000000000000000000000000000000)
    0xa65: MSTORE va59, va63(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa66: va66(0x20) = CONST 
    0xa68: va68(0x4) = CONST 
    0xa6b: va6b = ADD va59, va68(0x4)
    0xa6c: MSTORE va6b, va66(0x20)
    0xa6d: va6d(0x4c) = CONST 
    0xa6f: va6f(0x24) = CONST 
    0xa72: va72 = ADD va59, va6f(0x24)
    0xa73: MSTORE va72, va6d(0x4c)
    0xa74: va74(0x4f726967696e2063616e6e6f7420626520626c61636b6c697374656420696620) = CONST 
    0xa95: va95(0x44) = CONST 
    0xa98: va98 = ADD va59, va95(0x44)
    0xa99: MSTORE va98, va74(0x4f726967696e2063616e6e6f7420626520626c61636b6c697374656420696620)
    0xa9a: va9a(0x7370656e646572206973206e6f7420616e20617070726f76656420626c61636b) = CONST 
    0xabb: vabb(0x64) = CONST 
    0xabe: vabe = ADD va59, vabb(0x64)
    0xabf: MSTORE vabe, va9a(0x7370656e646572206973206e6f7420616e20617070726f76656420626c61636b)
    0xac0: vac0(0x6c697374207370656e6465720000000000000000000000000000000000000000) = CONST 
    0xae1: vae1(0x84) = CONST 
    0xae4: vae4 = ADD va59, vae1(0x84)
    0xae5: MSTORE vae4, vac0(0x6c697374207370656e6465720000000000000000000000000000000000000000)
    0xae7: vae7 = MLOAD va56(0x40)
    0xaeb: vaeb(0x0) = SUB va59, vae7
    0xaec: vaec(0xa4) = CONST 
    0xaee: vaee(0xa4) = ADD vaec(0xa4), vaeb(0x0)
    0xaf0: REVERT vae7, vaee(0xa4)

    Begin block 0xaf1
    prev=[0xa4f], succ=[0xafb]
    =================================
    0xaf2: vaf2(0xafb) = CONST 
    0xaf6: vaf6 = CALLER 
    0xaf7: vaf7(0x237f) = CONST 
    0xafa: vafa_0 = CALLPRIVATE vaf7(0x237f), vaf6, v200, vaf2(0xafb)

    Begin block 0xafb
    prev=[0xaf1], succ=[0xb03, 0xb52]
    =================================
    0xafd: vafd = GT v208, vafa_0
    0xafe: vafe = ISZERO vafd
    0xaff: vaff(0xb52) = CONST 
    0xb02: JUMPI vaff(0xb52), vafe

    Begin block 0xb03
    prev=[0xafb], succ=[]
    =================================
    0xb03: vb03(0x40) = CONST 
    0xb06: vb06 = MLOAD vb03(0x40)
    0xb07: vb07(0xe5) = CONST 
    0xb09: vb09(0x2) = CONST 
    0xb0b: vb0b(0x2000000000000000000000000000000000000000000000000000000000) = EXP vb09(0x2), vb07(0xe5)
    0xb0c: vb0c(0x461bcd) = CONST 
    0xb10: vb10(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vb0c(0x461bcd), vb0b(0x2000000000000000000000000000000000000000000000000000000000)
    0xb12: MSTORE vb06, vb10(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb13: vb13(0x20) = CONST 
    0xb15: vb15(0x4) = CONST 
    0xb18: vb18 = ADD vb06, vb15(0x4)
    0xb1b: MSTORE vb18, vb13(0x20)
    0xb1c: vb1c(0x24) = CONST 
    0xb1f: vb1f = ADD vb06, vb1c(0x24)
    0xb20: MSTORE vb1f, vb13(0x20)
    0xb21: vb21(0x6e6f7420656e6f75676820616c6c6f77616e636520746f207472616e73666572) = CONST 
    0xb42: vb42(0x44) = CONST 
    0xb45: vb45 = ADD vb06, vb42(0x44)
    0xb46: MSTORE vb45, vb21(0x6e6f7420656e6f75676820616c6c6f77616e636520746f207472616e73666572)
    0xb48: vb48 = MLOAD vb03(0x40)
    0xb4c: vb4c(0x0) = SUB vb06, vb48
    0xb4d: vb4d(0x64) = CONST 
    0xb4f: vb4f(0x64) = ADD vb4d(0x64), vb4c(0x0)
    0xb51: REVERT vb48, vb4f(0x64)

    Begin block 0xb52
    prev=[0xafb], succ=[0xb5d]
    =================================
    0xb53: vb53(0xb5d) = CONST 
    0xb59: vb59(0x24ff) = CONST 
    0xb5c: CALLPRIVATE vb59(0x24ff), v208, v200, v205, vb53(0xb5d)

    Begin block 0xb5d
    prev=[0xb52], succ=[0xbcd, 0xbd1]
    =================================
    0xb5e: vb5e(0x2) = CONST 
    0xb60: vb60 = SLOAD vb5e(0x2)
    0xb61: vb61(0x40) = CONST 
    0xb64: vb64 = MLOAD vb61(0x40)
    0xb65: vb65(0x97d88cd200000000000000000000000000000000000000000000000000000000) = CONST 
    0xb87: MSTORE vb64, vb65(0x97d88cd200000000000000000000000000000000000000000000000000000000)
    0xb88: vb88(0x1) = CONST 
    0xb8a: vb8a(0xa0) = CONST 
    0xb8c: vb8c(0x2) = CONST 
    0xb8e: vb8e(0x10000000000000000000000000000000000000000) = EXP vb8c(0x2), vb8a(0xa0)
    0xb8f: vb8f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb8e(0x10000000000000000000000000000000000000000), vb88(0x1)
    0xb92: vb92 = AND vb8f(0xffffffffffffffffffffffffffffffffffffffff), v200
    0xb93: vb93(0x4) = CONST 
    0xb96: vb96 = ADD vb64, vb93(0x4)
    0xb97: MSTORE vb96, vb92
    0xb98: vb98 = CALLER 
    0xb99: vb99(0x24) = CONST 
    0xb9c: vb9c = ADD vb64, vb99(0x24)
    0xb9d: MSTORE vb9c, vb98
    0xb9e: vb9e(0x44) = CONST 
    0xba1: vba1 = ADD vb64, vb9e(0x44)
    0xba4: MSTORE vba1, v208
    0xba6: vba6 = MLOAD vb61(0x40)
    0xbaa: vbaa = AND vb60, vb8f(0xffffffffffffffffffffffffffffffffffffffff)
    0xbac: vbac(0x97d88cd2) = CONST 
    0xbb2: vbb2(0x64) = CONST 
    0xbb6: vbb6 = ADD vb64, vbb2(0x64)
    0xbb8: vbb8(0x0) = CONST 
    0xbbf: vbbf(0x0) = SUB vb64, vba6
    0xbc0: vbc0(0x64) = ADD vbbf(0x0), vbb2(0x64)
    0xbc5: vbc5 = EXTCODESIZE vbaa
    0xbc6: vbc6 = ISZERO vbc5
    0xbc8: vbc8 = ISZERO vbc6
    0xbc9: vbc9(0xbd1) = CONST 
    0xbcc: JUMPI vbc9(0xbd1), vbc8

    Begin block 0xbcd
    prev=[0xb5d], succ=[]
    =================================
    0xbcd: vbcd(0x0) = CONST 
    0xbd0: REVERT vbcd(0x0), vbcd(0x0)

    Begin block 0xbd1
    prev=[0xb5d], succ=[0xbdc, 0xbe5]
    =================================
    0xbd3: vbd3 = GAS 
    0xbd4: vbd4 = CALL vbd3, vbaa, vbb8(0x0), vba6, vbc0(0x64), vba6, vbb8(0x0)
    0xbd5: vbd5 = ISZERO vbd4
    0xbd7: vbd7 = ISZERO vbd5
    0xbd8: vbd8(0xbe5) = CONST 
    0xbdb: JUMPI vbd8(0xbe5), vbd7

    Begin block 0xbdc
    prev=[0xbd1], succ=[]
    =================================
    0xbdc: vbdc = RETURNDATASIZE 
    0xbdd: vbdd(0x0) = CONST 
    0xbe0: RETURNDATACOPY vbdd(0x0), vbdd(0x0), vbdc
    0xbe1: vbe1 = RETURNDATASIZE 
    0xbe2: vbe2(0x0) = CONST 
    0xbe4: REVERT vbe2(0x0), vbe1

    Begin block 0xbe5
    prev=[0xbd1], succ=[0x3038]
    =================================
    0xbe7: vbe7(0x1) = CONST 
    0xbf6: JUMP v1f1(0x3038)

    Begin block 0x3038
    prev=[0xbe5], succ=[]
    =================================
    0x3039: v3039(0x40) = CONST 
    0x303c: v303c = MLOAD v3039(0x40)
    0x303e: v303e = ISZERO vbe7(0x1)
    0x303f: v303f = ISZERO v303e
    0x3041: MSTORE v303c, v303f
    0x3042: v3042 = MLOAD v3039(0x40)
    0x3046: v3046(0x0) = SUB v303c, v3042
    0x3047: v3047(0x20) = CONST 
    0x3049: v3049(0x20) = ADD v3047(0x20), v3046(0x0)
    0x304b: RETURN v3042, v3049(0x20)

    Begin block 0xa4d
    prev=[0xa41], succ=[0xa4f]
    =================================

}

function convertWT(uint256)() public {
    Begin block 0x20d
    prev=[], succ=[0x215, 0x219]
    =================================
    0x20e: v20e = CALLVALUE 
    0x210: v210 = ISZERO v20e
    0x211: v211(0x219) = CONST 
    0x214: JUMPI v211(0x219), v210

    Begin block 0x215
    prev=[0x20d], succ=[]
    =================================
    0x215: v215(0x0) = CONST 
    0x218: REVERT v215(0x0), v215(0x0)

    Begin block 0x219
    prev=[0x20d], succ=[0xbf7]
    =================================
    0x21b: v21b(0x306b) = CONST 
    0x21e: v21e(0x4) = CONST 
    0x220: v220 = CALLDATALOAD v21e(0x4)
    0x221: v221(0xbf7) = CONST 
    0x224: JUMP v221(0xbf7)

    Begin block 0xbf7
    prev=[0x219], succ=[0xc45, 0xc49]
    =================================
    0xbf8: vbf8(0x3) = CONST 
    0xbfa: vbfa = SLOAD vbf8(0x3)
    0xbfb: vbfb(0x40) = CONST 
    0xbfe: vbfe = MLOAD vbfb(0x40)
    0xbff: vbff(0xe0) = CONST 
    0xc01: vc01(0x2) = CONST 
    0xc03: vc03(0x100000000000000000000000000000000000000000000000000000000) = EXP vc01(0x2), vbff(0xe0)
    0xc04: vc04(0x7ccce851) = CONST 
    0xc09: vc09(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL vc04(0x7ccce851), vc03(0x100000000000000000000000000000000000000000000000000000000)
    0xc0b: MSTORE vbfe, vc09(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0xc0c: vc0c = CALLER 
    0xc0d: vc0d(0x4) = CONST 
    0xc10: vc10 = ADD vbfe, vc0d(0x4)
    0xc13: MSTORE vc10, vc0c
    0xc15: vc15 = MLOAD vbfb(0x40)
    0xc18: vc18(0x1) = CONST 
    0xc1a: vc1a(0xa0) = CONST 
    0xc1c: vc1c(0x2) = CONST 
    0xc1e: vc1e(0x10000000000000000000000000000000000000000) = EXP vc1c(0x2), vc1a(0xa0)
    0xc1f: vc1f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc1e(0x10000000000000000000000000000000000000000), vc18(0x1)
    0xc20: vc20 = AND vc1f(0xffffffffffffffffffffffffffffffffffffffff), vbfa
    0xc22: vc22(0x7ccce851) = CONST 
    0xc28: vc28(0x24) = CONST 
    0xc2c: vc2c = ADD vbfe, vc28(0x24)
    0xc2e: vc2e(0x20) = CONST 
    0xc36: vc36(0x0) = SUB vbfe, vc15
    0xc37: vc37(0x24) = ADD vc36(0x0), vc28(0x24)
    0xc39: vc39(0x0) = CONST 
    0xc3d: vc3d = EXTCODESIZE vc20
    0xc3e: vc3e = ISZERO vc3d
    0xc40: vc40 = ISZERO vc3e
    0xc41: vc41(0xc49) = CONST 
    0xc44: JUMPI vc41(0xc49), vc40

    Begin block 0xc45
    prev=[0xbf7], succ=[]
    =================================
    0xc45: vc45(0x0) = CONST 
    0xc48: REVERT vc45(0x0), vc45(0x0)

    Begin block 0xc49
    prev=[0xbf7], succ=[0xc54, 0xc5d]
    =================================
    0xc4b: vc4b = GAS 
    0xc4c: vc4c = CALL vc4b, vc20, vc39(0x0), vc15, vc37(0x24), vc15, vc2e(0x20)
    0xc4d: vc4d = ISZERO vc4c
    0xc4f: vc4f = ISZERO vc4d
    0xc50: vc50(0xc5d) = CONST 
    0xc53: JUMPI vc50(0xc5d), vc4f

    Begin block 0xc54
    prev=[0xc49], succ=[]
    =================================
    0xc54: vc54 = RETURNDATASIZE 
    0xc55: vc55(0x0) = CONST 
    0xc58: RETURNDATACOPY vc55(0x0), vc55(0x0), vc54
    0xc59: vc59 = RETURNDATASIZE 
    0xc5a: vc5a(0x0) = CONST 
    0xc5c: REVERT vc5a(0x0), vc59

    Begin block 0xc5d
    prev=[0xc49], succ=[0xc6f, 0xc73]
    =================================
    0xc62: vc62(0x40) = CONST 
    0xc64: vc64 = MLOAD vc62(0x40)
    0xc65: vc65 = RETURNDATASIZE 
    0xc66: vc66(0x20) = CONST 
    0xc69: vc69 = LT vc65, vc66(0x20)
    0xc6a: vc6a = ISZERO vc69
    0xc6b: vc6b(0xc73) = CONST 
    0xc6e: JUMPI vc6b(0xc73), vc6a

    Begin block 0xc6f
    prev=[0xc5d], succ=[]
    =================================
    0xc6f: vc6f(0x0) = CONST 
    0xc72: REVERT vc6f(0x0), vc6f(0x0)

    Begin block 0xc73
    prev=[0xc5d], succ=[0xc7b, 0xcb8]
    =================================
    0xc75: vc75 = MLOAD vc64
    0xc76: vc76 = ISZERO vc75
    0xc77: vc77(0xcb8) = CONST 
    0xc7a: JUMPI vc77(0xcb8), vc76

    Begin block 0xc7b
    prev=[0xc73], succ=[]
    =================================
    0xc7b: vc7b(0x40) = CONST 
    0xc7e: vc7e = MLOAD vc7b(0x40)
    0xc7f: vc7f(0xe5) = CONST 
    0xc81: vc81(0x2) = CONST 
    0xc83: vc83(0x2000000000000000000000000000000000000000000000000000000000) = EXP vc81(0x2), vc7f(0xe5)
    0xc84: vc84(0x461bcd) = CONST 
    0xc88: vc88(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vc84(0x461bcd), vc83(0x2000000000000000000000000000000000000000000000000000000000)
    0xc8a: MSTORE vc7e, vc88(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc8b: vc8b(0x20) = CONST 
    0xc8d: vc8d(0x4) = CONST 
    0xc90: vc90 = ADD vc7e, vc8d(0x4)
    0xc91: MSTORE vc90, vc8b(0x20)
    0xc92: vc92(0x1c) = CONST 
    0xc94: vc94(0x24) = CONST 
    0xc97: vc97 = ADD vc7e, vc94(0x24)
    0xc98: MSTORE vc97, vc92(0x1c)
    0xc99: vc99(0x0) = CONST 
    0xc9c: vc9c = MLOAD vc99(0x0)
    0xc9d: vc9d(0x20) = CONST 
    0xc9f: vc9f(0x2f6a) = CONST 
    0xca7: MSTORE vc99(0x0), vc9c
    0xca8: vca8(0x44) = CONST 
    0xcab: vcab = ADD vc7e, vca8(0x44)
    0xcac: MSTORE vcab, v3644(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0xcae: vcae = MLOAD vc7b(0x40)
    0xcb2: vcb2(0x0) = SUB vc7e, vcae
    0xcb3: vcb3(0x64) = CONST 
    0xcb5: vcb5(0x64) = ADD vcb3(0x64), vcb2(0x0)
    0xcb7: REVERT vcae, vcb5(0x64)
    0x3644: v3644(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0xcb8
    prev=[0xc73], succ=[0xccb, 0xccf]
    =================================
    0xcb9: vcb9(0x1) = CONST 
    0xcbb: vcbb = SLOAD vcb9(0x1)
    0xcbc: vcbc(0xa0) = CONST 
    0xcbe: vcbe(0x2) = CONST 
    0xcc0: vcc0(0x10000000000000000000000000000000000000000) = EXP vcbe(0x2), vcbc(0xa0)
    0xcc2: vcc2 = DIV vcbb, vcc0(0x10000000000000000000000000000000000000000)
    0xcc3: vcc3(0xff) = CONST 
    0xcc5: vcc5 = AND vcc3(0xff), vcc2
    0xcc6: vcc6 = ISZERO vcc5
    0xcc7: vcc7(0xccf) = CONST 
    0xcca: JUMPI vcc7(0xccf), vcc6

    Begin block 0xccb
    prev=[0xcb8], succ=[]
    =================================
    0xccb: vccb(0x0) = CONST 
    0xcce: REVERT vccb(0x0), vccb(0x0)

    Begin block 0xccf
    prev=[0xcb8], succ=[0xcd9]
    =================================
    0xcd1: vcd1(0xcd9) = CONST 
    0xcd4: vcd4 = CALLER 
    0xcd5: vcd5(0x16d7) = CONST 
    0xcd8: vcd8_0 = CALLPRIVATE vcd5(0x16d7), vcd4, vcd1(0xcd9)

    Begin block 0xcd9
    prev=[0xccf], succ=[0xce0, 0xd55]
    =================================
    0xcda: vcda = LT vcd8_0, v220
    0xcdb: vcdb = ISZERO vcda
    0xcdc: vcdc(0xd55) = CONST 
    0xcdf: JUMPI vcdc(0xd55), vcdb

    Begin block 0xce0
    prev=[0xcd9], succ=[]
    =================================
    0xce0: vce0(0x40) = CONST 
    0xce3: vce3 = MLOAD vce0(0x40)
    0xce4: vce4(0xe5) = CONST 
    0xce6: vce6(0x2) = CONST 
    0xce8: vce8(0x2000000000000000000000000000000000000000000000000000000000) = EXP vce6(0x2), vce4(0xe5)
    0xce9: vce9(0x461bcd) = CONST 
    0xced: vced(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vce9(0x461bcd), vce8(0x2000000000000000000000000000000000000000000000000000000000)
    0xcef: MSTORE vce3, vced(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xcf0: vcf0(0x20) = CONST 
    0xcf2: vcf2(0x4) = CONST 
    0xcf5: vcf5 = ADD vce3, vcf2(0x4)
    0xcf6: MSTORE vcf5, vcf0(0x20)
    0xcf7: vcf7(0x2d) = CONST 
    0xcf9: vcf9(0x24) = CONST 
    0xcfc: vcfc = ADD vce3, vcf9(0x24)
    0xcfd: MSTORE vcfc, vcf7(0x2d)
    0xcfe: vcfe(0x436f6e76657273696f6e20616d6f756e742073686f756c64206265206c657373) = CONST 
    0xd1f: vd1f(0x44) = CONST 
    0xd22: vd22 = ADD vce3, vd1f(0x44)
    0xd23: MSTORE vd22, vcfe(0x436f6e76657273696f6e20616d6f756e742073686f756c64206265206c657373)
    0xd24: vd24(0x207468616e2062616c616e636500000000000000000000000000000000000000) = CONST 
    0xd45: vd45(0x64) = CONST 
    0xd48: vd48 = ADD vce3, vd45(0x64)
    0xd49: MSTORE vd48, vd24(0x207468616e2062616c616e636500000000000000000000000000000000000000)
    0xd4b: vd4b = MLOAD vce0(0x40)
    0xd4f: vd4f(0x0) = SUB vce3, vd4b
    0xd50: vd50(0x84) = CONST 
    0xd52: vd52(0x84) = ADD vd50(0x84), vd4f(0x0)
    0xd54: REVERT vd4b, vd52(0x84)

    Begin block 0xd55
    prev=[0xcd9], succ=[0xd5f]
    =================================
    0xd56: vd56(0xd5f) = CONST 
    0xd59: vd59 = CALLER 
    0xd5b: vd5b(0x2712) = CONST 
    0xd5e: CALLPRIVATE vd5b(0x2712), v220, vd59, vd56(0xd5f)

    Begin block 0xd5f
    prev=[0xd55], succ=[0xd69]
    =================================
    0xd60: vd60(0xd69) = CONST 
    0xd63: vd63 = CALLER 
    0xd65: vd65(0x295a) = CONST 
    0xd68: CALLPRIVATE vd65(0x295a), v220, vd63, vd60(0xd69)

    Begin block 0xd69
    prev=[0xd5f], succ=[0x306b]
    =================================
    0xd6a: vd6a(0x40) = CONST 
    0xd6d: vd6d = MLOAD vd6a(0x40)
    0xd70: MSTORE vd6d, v220
    0xd72: vd72 = MLOAD vd6a(0x40)
    0xd73: vd73 = CALLER 
    0xd75: vd75(0x8bd92e48ca7380f64ff4556585a7161f9f0b0f67d1bb875fc1df0ae4fe6c0ae8) = CONST 
    0xd9a: vd9a(0x0) = SUB vd6d, vd72
    0xd9b: vd9b(0x20) = CONST 
    0xd9d: vd9d(0x20) = ADD vd9b(0x20), vd9a(0x0)
    0xd9f: LOG2 vd72, vd9d(0x20), vd75(0x8bd92e48ca7380f64ff4556585a7161f9f0b0f67d1bb875fc1df0ae4fe6c0ae8), vd73
    0xda2: JUMP v21b(0x306b)

    Begin block 0x306b
    prev=[0xd69], succ=[]
    =================================
    0x306c: STOP 

}

function unpause()() public {
    Begin block 0x227
    prev=[], succ=[0x22f, 0x233]
    =================================
    0x228: v228 = CALLVALUE 
    0x22a: v22a = ISZERO v228
    0x22b: v22b(0x233) = CONST 
    0x22e: JUMPI v22b(0x233), v22a

    Begin block 0x22f
    prev=[0x227], succ=[]
    =================================
    0x22f: v22f(0x0) = CONST 
    0x232: REVERT v22f(0x0), v22f(0x0)

    Begin block 0x233
    prev=[0x227], succ=[0xda3]
    =================================
    0x235: v235(0x308c) = CONST 
    0x238: v238(0xda3) = CONST 
    0x23b: JUMP v238(0xda3)

    Begin block 0xda3
    prev=[0x233], succ=[0xdb6, 0xdba]
    =================================
    0xda4: vda4(0x0) = CONST 
    0xda6: vda6 = SLOAD vda4(0x0)
    0xda7: vda7(0x1) = CONST 
    0xda9: vda9(0xa0) = CONST 
    0xdab: vdab(0x2) = CONST 
    0xdad: vdad(0x10000000000000000000000000000000000000000) = EXP vdab(0x2), vda9(0xa0)
    0xdae: vdae(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdad(0x10000000000000000000000000000000000000000), vda7(0x1)
    0xdaf: vdaf = AND vdae(0xffffffffffffffffffffffffffffffffffffffff), vda6
    0xdb0: vdb0 = CALLER 
    0xdb1: vdb1 = EQ vdb0, vdaf
    0xdb2: vdb2(0xdba) = CONST 
    0xdb5: JUMPI vdb2(0xdba), vdb1

    Begin block 0xdb6
    prev=[0xda3], succ=[]
    =================================
    0xdb6: vdb6(0x0) = CONST 
    0xdb9: REVERT vdb6(0x0), vdb6(0x0)

    Begin block 0xdba
    prev=[0xda3], succ=[0xdce, 0xdd2]
    =================================
    0xdbb: vdbb(0x1) = CONST 
    0xdbd: vdbd = SLOAD vdbb(0x1)
    0xdbe: vdbe(0xa0) = CONST 
    0xdc0: vdc0(0x2) = CONST 
    0xdc2: vdc2(0x10000000000000000000000000000000000000000) = EXP vdc0(0x2), vdbe(0xa0)
    0xdc4: vdc4 = DIV vdbd, vdc2(0x10000000000000000000000000000000000000000)
    0xdc5: vdc5(0xff) = CONST 
    0xdc7: vdc7 = AND vdc5(0xff), vdc4
    0xdc8: vdc8 = ISZERO vdc7
    0xdc9: vdc9 = ISZERO vdc8
    0xdca: vdca(0xdd2) = CONST 
    0xdcd: JUMPI vdca(0xdd2), vdc9

    Begin block 0xdce
    prev=[0xdba], succ=[]
    =================================
    0xdce: vdce(0x0) = CONST 
    0xdd1: REVERT vdce(0x0), vdce(0x0)

    Begin block 0xdd2
    prev=[0xdba], succ=[0x308c]
    =================================
    0xdd3: vdd3(0x1) = CONST 
    0xdd6: vdd6 = SLOAD vdd3(0x1)
    0xdd7: vdd7(0xff0000000000000000000000000000000000000000) = CONST 
    0xded: vded(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT vdd7(0xff0000000000000000000000000000000000000000)
    0xdee: vdee = AND vded(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), vdd6
    0xdf0: SSTORE vdd3(0x1), vdee
    0xdf1: vdf1(0x40) = CONST 
    0xdf3: vdf3 = MLOAD vdf1(0x40)
    0xdf4: vdf4(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33) = CONST 
    0xe16: ve16(0x0) = CONST 
    0xe19: LOG1 vdf3, ve16(0x0), vdf4(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33)
    0xe1a: JUMP v235(0x308c)

    Begin block 0x308c
    prev=[0xdd2], succ=[]
    =================================
    0x308d: STOP 

}

function 0x237f(0x237farg0x0, 0x237farg0x1, 0x237farg0x2) private {
    Begin block 0x237f
    prev=[], succ=[0x23ee, 0x23f2]
    =================================
    0x2380: v2380(0x2) = CONST 
    0x2382: v2382 = SLOAD v2380(0x2)
    0x2383: v2383(0x40) = CONST 
    0x2386: v2386 = MLOAD v2383(0x40)
    0x2387: v2387(0x55b6ed5c00000000000000000000000000000000000000000000000000000000) = CONST 
    0x23a9: MSTORE v2386, v2387(0x55b6ed5c00000000000000000000000000000000000000000000000000000000)
    0x23aa: v23aa(0x1) = CONST 
    0x23ac: v23ac(0xa0) = CONST 
    0x23ae: v23ae(0x2) = CONST 
    0x23b0: v23b0(0x10000000000000000000000000000000000000000) = EXP v23ae(0x2), v23ac(0xa0)
    0x23b1: v23b1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23b0(0x10000000000000000000000000000000000000000), v23aa(0x1)
    0x23b4: v23b4 = AND v23b1(0xffffffffffffffffffffffffffffffffffffffff), v237farg1
    0x23b5: v23b5(0x4) = CONST 
    0x23b8: v23b8 = ADD v2386, v23b5(0x4)
    0x23b9: MSTORE v23b8, v23b4
    0x23bc: v23bc = AND v23b1(0xffffffffffffffffffffffffffffffffffffffff), v237farg0
    0x23bd: v23bd(0x24) = CONST 
    0x23c0: v23c0 = ADD v2386, v23bd(0x24)
    0x23c1: MSTORE v23c0, v23bc
    0x23c3: v23c3 = MLOAD v2383(0x40)
    0x23c4: v23c4(0x0) = CONST 
    0x23ca: v23ca = AND v2382, v23b1(0xffffffffffffffffffffffffffffffffffffffff)
    0x23cc: v23cc(0x55b6ed5c) = CONST 
    0x23d2: v23d2(0x44) = CONST 
    0x23d6: v23d6 = ADD v2386, v23d2(0x44)
    0x23d8: v23d8(0x20) = CONST 
    0x23e0: v23e0(0x0) = SUB v2386, v23c3
    0x23e1: v23e1(0x44) = ADD v23e0(0x0), v23d2(0x44)
    0x23e6: v23e6 = EXTCODESIZE v23ca
    0x23e7: v23e7 = ISZERO v23e6
    0x23e9: v23e9 = ISZERO v23e7
    0x23ea: v23ea(0x23f2) = CONST 
    0x23ed: JUMPI v23ea(0x23f2), v23e9

    Begin block 0x23ee
    prev=[0x237f], succ=[]
    =================================
    0x23ee: v23ee(0x0) = CONST 
    0x23f1: REVERT v23ee(0x0), v23ee(0x0)

    Begin block 0x23f2
    prev=[0x237f], succ=[0x23fd, 0x2406]
    =================================
    0x23f4: v23f4 = GAS 
    0x23f5: v23f5 = CALL v23f4, v23ca, v23c4(0x0), v23c3, v23e1(0x44), v23c3, v23d8(0x20)
    0x23f6: v23f6 = ISZERO v23f5
    0x23f8: v23f8 = ISZERO v23f6
    0x23f9: v23f9(0x2406) = CONST 
    0x23fc: JUMPI v23f9(0x2406), v23f8

    Begin block 0x23fd
    prev=[0x23f2], succ=[]
    =================================
    0x23fd: v23fd = RETURNDATASIZE 
    0x23fe: v23fe(0x0) = CONST 
    0x2401: RETURNDATACOPY v23fe(0x0), v23fe(0x0), v23fd
    0x2402: v2402 = RETURNDATASIZE 
    0x2403: v2403(0x0) = CONST 
    0x2405: REVERT v2403(0x0), v2402

    Begin block 0x2406
    prev=[0x23f2], succ=[0x2418, 0x241c]
    =================================
    0x240b: v240b(0x40) = CONST 
    0x240d: v240d = MLOAD v240b(0x40)
    0x240e: v240e = RETURNDATASIZE 
    0x240f: v240f(0x20) = CONST 
    0x2412: v2412 = LT v240e, v240f(0x20)
    0x2413: v2413 = ISZERO v2412
    0x2414: v2414(0x241c) = CONST 
    0x2417: JUMPI v2414(0x241c), v2413

    Begin block 0x2418
    prev=[0x2406], succ=[]
    =================================
    0x2418: v2418(0x0) = CONST 
    0x241b: REVERT v2418(0x0), v2418(0x0)

    Begin block 0x241c
    prev=[0x2406], succ=[]
    =================================
    0x241e: v241e = MLOAD v240d
    0x2424: RETURNPRIVATE v237farg2, v241e

}

function mint(address,uint256)() public {
    Begin block 0x23c
    prev=[], succ=[0x244, 0x248]
    =================================
    0x23d: v23d = CALLVALUE 
    0x23f: v23f = ISZERO v23d
    0x240: v240(0x248) = CONST 
    0x243: JUMPI v240(0x248), v23f

    Begin block 0x244
    prev=[0x23c], succ=[]
    =================================
    0x244: v244(0x0) = CONST 
    0x247: REVERT v244(0x0), v244(0x0)

    Begin block 0x248
    prev=[0x23c], succ=[0xe1bB0x248]
    =================================
    0x24a: v24a(0x30ad) = CONST 
    0x24d: v24d(0x1) = CONST 
    0x24f: v24f(0xa0) = CONST 
    0x251: v251(0x2) = CONST 
    0x253: v253(0x10000000000000000000000000000000000000000) = EXP v251(0x2), v24f(0xa0)
    0x254: v254(0xffffffffffffffffffffffffffffffffffffffff) = SUB v253(0x10000000000000000000000000000000000000000), v24d(0x1)
    0x255: v255(0x4) = CONST 
    0x257: v257 = CALLDATALOAD v255(0x4)
    0x258: v258 = AND v257, v254(0xffffffffffffffffffffffffffffffffffffffff)
    0x259: v259(0x24) = CONST 
    0x25b: v25b = CALLDATALOAD v259(0x24)
    0x25c: v25c(0xe1b) = CONST 
    0x25f: JUMP v25c(0xe1b), v25b, v258, v24a(0x30ad)

    Begin block 0xe1bB0x248
    prev=[0x248], succ=[0xe6cB0x248, 0xe70B0x248]
    =================================
    0xe1cS0x248: ve1cV248(0x3) = CONST 
    0xe1eS0x248: ve1eV248 = SLOAD ve1cV248(0x3)
    0xe1fS0x248: ve1fV248(0x40) = CONST 
    0xe22S0x248: ve22V248 = MLOAD ve1fV248(0x40)
    0xe23S0x248: ve23V248(0xe0) = CONST 
    0xe25S0x248: ve25V248(0x2) = CONST 
    0xe27S0x248: ve27V248(0x100000000000000000000000000000000000000000000000000000000) = EXP ve25V248(0x2), ve23V248(0xe0)
    0xe28S0x248: ve28V248(0x7ccce851) = CONST 
    0xe2dS0x248: ve2dV248(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL ve28V248(0x7ccce851), ve27V248(0x100000000000000000000000000000000000000000000000000000000)
    0xe2fS0x248: MSTORE ve22V248, ve2dV248(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0xe30S0x248: ve30V248(0x1) = CONST 
    0xe32S0x248: ve32V248(0xa0) = CONST 
    0xe34S0x248: ve34V248(0x2) = CONST 
    0xe36S0x248: ve36V248(0x10000000000000000000000000000000000000000) = EXP ve34V248(0x2), ve32V248(0xa0)
    0xe37S0x248: ve37V248(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve36V248(0x10000000000000000000000000000000000000000), ve30V248(0x1)
    0xe3aS0x248: ve3aV248 = AND v258, ve37V248(0xffffffffffffffffffffffffffffffffffffffff)
    0xe3bS0x248: ve3bV248(0x4) = CONST 
    0xe3eS0x248: ve3eV248 = ADD ve22V248, ve3bV248(0x4)
    0xe3fS0x248: MSTORE ve3eV248, ve3aV248
    0xe41S0x248: ve41V248 = MLOAD ve1fV248(0x40)
    0xe47S0x248: ve47V248 = AND ve1eV248, ve37V248(0xffffffffffffffffffffffffffffffffffffffff)
    0xe49S0x248: ve49V248(0x7ccce851) = CONST 
    0xe4fS0x248: ve4fV248(0x24) = CONST 
    0xe53S0x248: ve53V248 = ADD ve22V248, ve4fV248(0x24)
    0xe55S0x248: ve55V248(0x20) = CONST 
    0xe5dS0x248: ve5dV248(0x0) = SUB ve22V248, ve41V248
    0xe5eS0x248: ve5eV248(0x24) = ADD ve5dV248(0x0), ve4fV248(0x24)
    0xe60S0x248: ve60V248(0x0) = CONST 
    0xe64S0x248: ve64V248 = EXTCODESIZE ve47V248
    0xe65S0x248: ve65V248 = ISZERO ve64V248
    0xe67S0x248: ve67V248 = ISZERO ve65V248
    0xe68S0x248: ve68V248(0xe70) = CONST 
    0xe6bS0x248: JUMPI ve68V248(0xe70), ve67V248

    Begin block 0xe6cB0x248
    prev=[0xe1bB0x248], succ=[]
    =================================
    0xe6cS0x248: ve6cV248(0x0) = CONST 
    0xe6fS0x248: REVERT ve6cV248(0x0), ve6cV248(0x0)

    Begin block 0xe70B0x248
    prev=[0xe1bB0x248], succ=[0xe7bB0x248, 0xe84B0x248]
    =================================
    0xe72S0x248: ve72V248 = GAS 
    0xe73S0x248: ve73V248 = CALL ve72V248, ve47V248, ve60V248(0x0), ve41V248, ve5eV248(0x24), ve41V248, ve55V248(0x20)
    0xe74S0x248: ve74V248 = ISZERO ve73V248
    0xe76S0x248: ve76V248 = ISZERO ve74V248
    0xe77S0x248: ve77V248(0xe84) = CONST 
    0xe7aS0x248: JUMPI ve77V248(0xe84), ve76V248

    Begin block 0xe7bB0x248
    prev=[0xe70B0x248], succ=[]
    =================================
    0xe7bS0x248: ve7bV248 = RETURNDATASIZE 
    0xe7cS0x248: ve7cV248(0x0) = CONST 
    0xe7fS0x248: RETURNDATACOPY ve7cV248(0x0), ve7cV248(0x0), ve7bV248
    0xe80S0x248: ve80V248 = RETURNDATASIZE 
    0xe81S0x248: ve81V248(0x0) = CONST 
    0xe83S0x248: REVERT ve81V248(0x0), ve80V248

    Begin block 0xe84B0x248
    prev=[0xe70B0x248], succ=[0xe96B0x248, 0xe9aB0x248]
    =================================
    0xe89S0x248: ve89V248(0x40) = CONST 
    0xe8bS0x248: ve8bV248 = MLOAD ve89V248(0x40)
    0xe8cS0x248: ve8cV248 = RETURNDATASIZE 
    0xe8dS0x248: ve8dV248(0x20) = CONST 
    0xe90S0x248: ve90V248 = LT ve8cV248, ve8dV248(0x20)
    0xe91S0x248: ve91V248 = ISZERO ve90V248
    0xe92S0x248: ve92V248(0xe9a) = CONST 
    0xe95S0x248: JUMPI ve92V248(0xe9a), ve91V248

    Begin block 0xe96B0x248
    prev=[0xe84B0x248], succ=[]
    =================================
    0xe96S0x248: ve96V248(0x0) = CONST 
    0xe99S0x248: REVERT ve96V248(0x0), ve96V248(0x0)

    Begin block 0xe9aB0x248
    prev=[0xe84B0x248], succ=[0xea2B0x248, 0xedfB0x248]
    =================================
    0xe9cS0x248: ve9cV248 = MLOAD ve8bV248
    0xe9dS0x248: ve9dV248 = ISZERO ve9cV248
    0xe9eS0x248: ve9eV248(0xedf) = CONST 
    0xea1S0x248: JUMPI ve9eV248(0xedf), ve9dV248

    Begin block 0xea2B0x248
    prev=[0xe9aB0x248], succ=[]
    =================================
    0xea2S0x248: vea2V248(0x40) = CONST 
    0xea5S0x248: vea5V248 = MLOAD vea2V248(0x40)
    0xea6S0x248: vea6V248(0xe5) = CONST 
    0xea8S0x248: vea8V248(0x2) = CONST 
    0xeaaS0x248: veaaV248(0x2000000000000000000000000000000000000000000000000000000000) = EXP vea8V248(0x2), vea6V248(0xe5)
    0xeabS0x248: veabV248(0x461bcd) = CONST 
    0xeafS0x248: veafV248(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL veabV248(0x461bcd), veaaV248(0x2000000000000000000000000000000000000000000000000000000000)
    0xeb1S0x248: MSTORE vea5V248, veafV248(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xeb2S0x248: veb2V248(0x20) = CONST 
    0xeb4S0x248: veb4V248(0x4) = CONST 
    0xeb7S0x248: veb7V248 = ADD vea5V248, veb4V248(0x4)
    0xeb8S0x248: MSTORE veb7V248, veb2V248(0x20)
    0xeb9S0x248: veb9V248(0x1c) = CONST 
    0xebbS0x248: vebbV248(0x24) = CONST 
    0xebeS0x248: vebeV248 = ADD vea5V248, vebbV248(0x24)
    0xebfS0x248: MSTORE vebeV248, veb9V248(0x1c)
    0xec0S0x248: vec0V248(0x0) = CONST 
    0xec3S0x248: vec3V248 = MLOAD vec0V248(0x0)
    0xec4S0x248: vec4V248(0x20) = CONST 
    0xec6S0x248: vec6V248(0x2f6a) = CONST 
    0xeceS0x248: MSTORE vec0V248(0x0), vec3V248
    0xecfS0x248: vecfV248(0x44) = CONST 
    0xed2S0x248: ved2V248 = ADD vea5V248, vecfV248(0x44)
    0xed3S0x248: MSTORE ved2V248, v3649V248(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0xed5S0x248: ved5V248 = MLOAD vea2V248(0x40)
    0xed9S0x248: ved9V248(0x0) = SUB vea5V248, ved5V248
    0xedaS0x248: vedaV248(0x64) = CONST 
    0xedcS0x248: vedcV248(0x64) = ADD vedaV248(0x64), ved9V248(0x0)
    0xedeS0x248: REVERT ved5V248, vedcV248(0x64)
    0x3649S0x248: v3649V248(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0xedfB0x248
    prev=[0xe9aB0x248], succ=[0xf3fB0x248, 0xf43B0x248]
    =================================
    0xee0S0x248: vee0V248(0x3) = CONST 
    0xee2S0x248: vee2V248 = SLOAD vee0V248(0x3)
    0xee3S0x248: vee3V248(0x40) = CONST 
    0xee6S0x248: vee6V248 = MLOAD vee3V248(0x40)
    0xee7S0x248: vee7V248(0xe3) = CONST 
    0xee9S0x248: vee9V248(0x2) = CONST 
    0xeebS0x248: veebV248(0x800000000000000000000000000000000000000000000000000000000) = EXP vee9V248(0x2), vee7V248(0xe3)
    0xeecS0x248: veecV248(0x29b6dab) = CONST 
    0xef1S0x248: vef1V248(0x14db6d5800000000000000000000000000000000000000000000000000000000) = MUL veecV248(0x29b6dab), veebV248(0x800000000000000000000000000000000000000000000000000000000)
    0xef3S0x248: MSTORE vee6V248, vef1V248(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0xef4S0x248: vef4V248 = CALLER 
    0xef5S0x248: vef5V248(0x4) = CONST 
    0xef8S0x248: vef8V248 = ADD vee6V248, vef5V248(0x4)
    0xef9S0x248: MSTORE vef8V248, vef4V248
    0xefaS0x248: vefaV248(0x0) = CONST 
    0xefdS0x248: vefdV248 = CALLDATALOAD vefaV248(0x0)
    0xefeS0x248: vefeV248(0x1) = CONST 
    0xf00S0x248: vf00V248(0xe0) = CONST 
    0xf02S0x248: vf02V248(0x2) = CONST 
    0xf04S0x248: vf04V248(0x100000000000000000000000000000000000000000000000000000000) = EXP vf02V248(0x2), vf00V248(0xe0)
    0xf05S0x248: vf05V248(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vf04V248(0x100000000000000000000000000000000000000000000000000000000), vefeV248(0x1)
    0xf06S0x248: vf06V248(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT vf05V248(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xf07S0x248: vf07V248 = AND vf06V248(0xffffffff00000000000000000000000000000000000000000000000000000000), vefdV248
    0xf08S0x248: vf08V248(0x24) = CONST 
    0xf0bS0x248: vf0bV248 = ADD vee6V248, vf08V248(0x24)
    0xf0cS0x248: MSTORE vf0bV248, vf07V248
    0xf0eS0x248: vf0eV248 = MLOAD vee3V248(0x40)
    0xf0fS0x248: vf0fV248(0x1) = CONST 
    0xf11S0x248: vf11V248(0xa0) = CONST 
    0xf13S0x248: vf13V248(0x2) = CONST 
    0xf15S0x248: vf15V248(0x10000000000000000000000000000000000000000) = EXP vf13V248(0x2), vf11V248(0xa0)
    0xf16S0x248: vf16V248(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf15V248(0x10000000000000000000000000000000000000000), vf0fV248(0x1)
    0xf19S0x248: vf19V248 = AND vee2V248, vf16V248(0xffffffffffffffffffffffffffffffffffffffff)
    0xf1bS0x248: vf1bV248(0x14db6d58) = CONST 
    0xf21S0x248: vf21V248(0x44) = CONST 
    0xf25S0x248: vf25V248 = ADD vee6V248, vf21V248(0x44)
    0xf27S0x248: vf27V248(0x20) = CONST 
    0xf2eS0x248: vf2eV248(0x0) = SUB vee6V248, vf0eV248
    0xf31S0x248: vf31V248(0x44) = ADD vf21V248(0x44), vf2eV248(0x0)
    0xf37S0x248: vf37V248 = EXTCODESIZE vf19V248
    0xf38S0x248: vf38V248 = ISZERO vf37V248
    0xf3aS0x248: vf3aV248 = ISZERO vf38V248
    0xf3bS0x248: vf3bV248(0xf43) = CONST 
    0xf3eS0x248: JUMPI vf3bV248(0xf43), vf3aV248

    Begin block 0xf3fB0x248
    prev=[0xedfB0x248], succ=[]
    =================================
    0xf3fS0x248: vf3fV248(0x0) = CONST 
    0xf42S0x248: REVERT vf3fV248(0x0), vf3fV248(0x0)

    Begin block 0xf43B0x248
    prev=[0xedfB0x248], succ=[0xf4eB0x248, 0xf57B0x248]
    =================================
    0xf45S0x248: vf45V248 = GAS 
    0xf46S0x248: vf46V248 = CALL vf45V248, vf19V248, vefaV248(0x0), vf0eV248, vf31V248(0x44), vf0eV248, vf27V248(0x20)
    0xf47S0x248: vf47V248 = ISZERO vf46V248
    0xf49S0x248: vf49V248 = ISZERO vf47V248
    0xf4aS0x248: vf4aV248(0xf57) = CONST 
    0xf4dS0x248: JUMPI vf4aV248(0xf57), vf49V248

    Begin block 0xf4eB0x248
    prev=[0xf43B0x248], succ=[]
    =================================
    0xf4eS0x248: vf4eV248 = RETURNDATASIZE 
    0xf4fS0x248: vf4fV248(0x0) = CONST 
    0xf52S0x248: RETURNDATACOPY vf4fV248(0x0), vf4fV248(0x0), vf4eV248
    0xf53S0x248: vf53V248 = RETURNDATASIZE 
    0xf54S0x248: vf54V248(0x0) = CONST 
    0xf56S0x248: REVERT vf54V248(0x0), vf53V248

    Begin block 0xf57B0x248
    prev=[0xf43B0x248], succ=[0xf69B0x248, 0xf6dB0x248]
    =================================
    0xf5cS0x248: vf5cV248(0x40) = CONST 
    0xf5eS0x248: vf5eV248 = MLOAD vf5cV248(0x40)
    0xf5fS0x248: vf5fV248 = RETURNDATASIZE 
    0xf60S0x248: vf60V248(0x20) = CONST 
    0xf63S0x248: vf63V248 = LT vf5fV248, vf60V248(0x20)
    0xf64S0x248: vf64V248 = ISZERO vf63V248
    0xf65S0x248: vf65V248(0xf6d) = CONST 
    0xf68S0x248: JUMPI vf65V248(0xf6d), vf64V248

    Begin block 0xf69B0x248
    prev=[0xf57B0x248], succ=[]
    =================================
    0xf69S0x248: vf69V248(0x0) = CONST 
    0xf6cS0x248: REVERT vf69V248(0x0), vf69V248(0x0)

    Begin block 0xf6dB0x248
    prev=[0xf57B0x248], succ=[0xf76B0x248, 0xfc7B0x248]
    =================================
    0xf6fS0x248: vf6fV248 = MLOAD vf5eV248
    0xf70S0x248: vf70V248 = ISZERO vf6fV248
    0xf71S0x248: vf71V248 = ISZERO vf70V248
    0xf72S0x248: vf72V248(0xfc7) = CONST 
    0xf75S0x248: JUMPI vf72V248(0xfc7), vf71V248

    Begin block 0xf76B0x248
    prev=[0xf6dB0x248], succ=[]
    =================================
    0xf76S0x248: vf76V248(0x40) = CONST 
    0xf79S0x248: vf79V248 = MLOAD vf76V248(0x40)
    0xf7aS0x248: vf7aV248(0xe5) = CONST 
    0xf7cS0x248: vf7cV248(0x2) = CONST 
    0xf7eS0x248: vf7eV248(0x2000000000000000000000000000000000000000000000000000000000) = EXP vf7cV248(0x2), vf7aV248(0xe5)
    0xf7fS0x248: vf7fV248(0x461bcd) = CONST 
    0xf83S0x248: vf83V248(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL vf7fV248(0x461bcd), vf7eV248(0x2000000000000000000000000000000000000000000000000000000000)
    0xf85S0x248: MSTORE vf79V248, vf83V248(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf86S0x248: vf86V248(0x20) = CONST 
    0xf88S0x248: vf88V248(0x4) = CONST 
    0xf8bS0x248: vf8bV248 = ADD vf79V248, vf88V248(0x4)
    0xf8cS0x248: MSTORE vf8bV248, vf86V248(0x20)
    0xf8dS0x248: vf8dV248(0x31) = CONST 
    0xf8fS0x248: vf8fV248(0x24) = CONST 
    0xf92S0x248: vf92V248 = ADD vf79V248, vf8fV248(0x24)
    0xf93S0x248: MSTORE vf92V248, vf8dV248(0x31)
    0xf94S0x248: vf94V248(0x0) = CONST 
    0xf97S0x248: vf97V248 = MLOAD vf94V248(0x0)
    0xf98S0x248: vf98V248(0x20) = CONST 
    0xf9aS0x248: vf9aV248(0x2f4a) = CONST 
    0xfa2S0x248: MSTORE vf94V248(0x0), vf97V248
    0xfa3S0x248: vfa3V248(0x44) = CONST 
    0xfa6S0x248: vfa6V248 = ADD vf79V248, vfa3V248(0x44)
    0xfa7S0x248: MSTORE vfa6V248, v364eV248(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0xfa8S0x248: vfa8V248(0x0) = CONST 
    0xfabS0x248: vfabV248 = MLOAD vfa8V248(0x0)
    0xfacS0x248: vfacV248(0x20) = CONST 
    0xfaeS0x248: vfaeV248(0x2f2a) = CONST 
    0xfb6S0x248: MSTORE vfa8V248(0x0), vfabV248
    0xfb7S0x248: vfb7V248(0x64) = CONST 
    0xfbaS0x248: vfbaV248 = ADD vf79V248, vfb7V248(0x64)
    0xfbbS0x248: MSTORE vfbaV248, v3653V248(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0xfbdS0x248: vfbdV248 = MLOAD vf76V248(0x40)
    0xfc1S0x248: vfc1V248(0x0) = SUB vf79V248, vfbdV248
    0xfc2S0x248: vfc2V248(0x84) = CONST 
    0xfc4S0x248: vfc4V248(0x84) = ADD vfc2V248(0x84), vfc1V248(0x0)
    0xfc6S0x248: REVERT vfbdV248, vfc4V248(0x84)
    0x364eS0x248: v364eV248(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x3653S0x248: v3653V248(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 

    Begin block 0xfc7B0x248
    prev=[0xf6dB0x248], succ=[0xfdaB0x248, 0xfdeB0x248]
    =================================
    0xfc8S0x248: vfc8V248(0x1) = CONST 
    0xfcaS0x248: vfcaV248 = SLOAD vfc8V248(0x1)
    0xfcbS0x248: vfcbV248(0xa0) = CONST 
    0xfcdS0x248: vfcdV248(0x2) = CONST 
    0xfcfS0x248: vfcfV248(0x10000000000000000000000000000000000000000) = EXP vfcdV248(0x2), vfcbV248(0xa0)
    0xfd1S0x248: vfd1V248 = DIV vfcaV248, vfcfV248(0x10000000000000000000000000000000000000000)
    0xfd2S0x248: vfd2V248(0xff) = CONST 
    0xfd4S0x248: vfd4V248 = AND vfd2V248(0xff), vfd1V248
    0xfd5S0x248: vfd5V248 = ISZERO vfd4V248
    0xfd6S0x248: vfd6V248(0xfde) = CONST 
    0xfd9S0x248: JUMPI vfd6V248(0xfde), vfd5V248

    Begin block 0xfdaB0x248
    prev=[0xfc7B0x248], succ=[]
    =================================
    0xfdaS0x248: vfdaV248(0x0) = CONST 
    0xfddS0x248: REVERT vfdaV248(0x0), vfdaV248(0x0)

    Begin block 0xfdeB0x248
    prev=[0xfc7B0x248], succ=[0x34f4B0x248]
    =================================
    0xfdfS0x248: vfdfV248(0x34f4) = CONST 
    0xfe4S0x248: vfe4V248(0x2aca) = CONST 
    0xfe7S0x248: CALLPRIVATE vfe4V248(0x2aca), v25b, v258, vfdfV248(0x34f4)

    Begin block 0x34f4B0x248
    prev=[0xfdeB0x248], succ=[0x30ad]
    =================================
    0x34f8S0x248: JUMP v24a(0x30ad)

    Begin block 0x30ad
    prev=[0x34f4B0x248], succ=[]
    =================================
    0x30ae: STOP 

}

function 0x24ff(0x24ffarg0x0, 0x24ffarg0x1, 0x24ffarg0x2, 0x24ffarg0x3) private {
    Begin block 0x24ff
    prev=[], succ=[0x2510, 0x255f]
    =================================
    0x2500: v2500(0x1) = CONST 
    0x2502: v2502(0xa0) = CONST 
    0x2504: v2504(0x2) = CONST 
    0x2506: v2506(0x10000000000000000000000000000000000000000) = EXP v2504(0x2), v2502(0xa0)
    0x2507: v2507(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2506(0x10000000000000000000000000000000000000000), v2500(0x1)
    0x2509: v2509 = AND v24ffarg2, v2507(0xffffffffffffffffffffffffffffffffffffffff)
    0x250a: v250a = ISZERO v2509
    0x250b: v250b = ISZERO v250a
    0x250c: v250c(0x255f) = CONST 
    0x250f: JUMPI v250c(0x255f), v250b

    Begin block 0x2510
    prev=[0x24ff], succ=[]
    =================================
    0x2510: v2510(0x40) = CONST 
    0x2513: v2513 = MLOAD v2510(0x40)
    0x2514: v2514(0xe5) = CONST 
    0x2516: v2516(0x2) = CONST 
    0x2518: v2518(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2516(0x2), v2514(0xe5)
    0x2519: v2519(0x461bcd) = CONST 
    0x251d: v251d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2519(0x461bcd), v2518(0x2000000000000000000000000000000000000000000000000000000000)
    0x251f: MSTORE v2513, v251d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2520: v2520(0x20) = CONST 
    0x2522: v2522(0x4) = CONST 
    0x2525: v2525 = ADD v2513, v2522(0x4)
    0x2526: MSTORE v2525, v2520(0x20)
    0x2527: v2527(0x18) = CONST 
    0x2529: v2529(0x24) = CONST 
    0x252c: v252c = ADD v2513, v2529(0x24)
    0x252d: MSTORE v252c, v2527(0x18)
    0x252e: v252e(0x746f20616464726573732063616e6e6f74206265203078300000000000000000) = CONST 
    0x254f: v254f(0x44) = CONST 
    0x2552: v2552 = ADD v2513, v254f(0x44)
    0x2553: MSTORE v2552, v252e(0x746f20616464726573732063616e6e6f74206265203078300000000000000000)
    0x2555: v2555 = MLOAD v2510(0x40)
    0x2559: v2559(0x0) = SUB v2513, v2555
    0x255a: v255a(0x64) = CONST 
    0x255c: v255c(0x64) = ADD v255a(0x64), v2559(0x0)
    0x255e: REVERT v2555, v255c(0x64)

    Begin block 0x255f
    prev=[0x24ff], succ=[0x2568]
    =================================
    0x2560: v2560(0x2568) = CONST 
    0x2564: v2564(0x16d7) = CONST 
    0x2567: v2567_0 = CALLPRIVATE v2564(0x16d7), v24ffarg1, v2560(0x2568)

    Begin block 0x2568
    prev=[0x255f], succ=[0x2570, 0x25bf]
    =================================
    0x256a: v256a = GT v24ffarg0, v2567_0
    0x256b: v256b = ISZERO v256a
    0x256c: v256c(0x25bf) = CONST 
    0x256f: JUMPI v256c(0x25bf), v256b

    Begin block 0x2570
    prev=[0x2568], succ=[]
    =================================
    0x2570: v2570(0x40) = CONST 
    0x2573: v2573 = MLOAD v2570(0x40)
    0x2574: v2574(0xe5) = CONST 
    0x2576: v2576(0x2) = CONST 
    0x2578: v2578(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2576(0x2), v2574(0xe5)
    0x2579: v2579(0x461bcd) = CONST 
    0x257d: v257d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2579(0x461bcd), v2578(0x2000000000000000000000000000000000000000000000000000000000)
    0x257f: MSTORE v2573, v257d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2580: v2580(0x20) = CONST 
    0x2582: v2582(0x4) = CONST 
    0x2585: v2585 = ADD v2573, v2582(0x4)
    0x2586: MSTORE v2585, v2580(0x20)
    0x2587: v2587(0x1e) = CONST 
    0x2589: v2589(0x24) = CONST 
    0x258c: v258c = ADD v2573, v2589(0x24)
    0x258d: MSTORE v258c, v2587(0x1e)
    0x258e: v258e(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000) = CONST 
    0x25af: v25af(0x44) = CONST 
    0x25b2: v25b2 = ADD v2573, v25af(0x44)
    0x25b3: MSTORE v25b2, v258e(0x6e6f7420656e6f7567682062616c616e636520746f207472616e736665720000)
    0x25b5: v25b5 = MLOAD v2570(0x40)
    0x25b9: v25b9(0x0) = SUB v2573, v25b5
    0x25ba: v25ba(0x64) = CONST 
    0x25bc: v25bc(0x64) = ADD v25ba(0x64), v25b9(0x0)
    0x25be: REVERT v25b5, v25bc(0x64)

    Begin block 0x25bf
    prev=[0x2568], succ=[0x2629, 0x262d]
    =================================
    0x25c0: v25c0(0x2) = CONST 
    0x25c2: v25c2 = SLOAD v25c0(0x2)
    0x25c3: v25c3(0x40) = CONST 
    0x25c6: v25c6 = MLOAD v25c3(0x40)
    0x25c7: v25c7(0x21e5383a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x25e9: MSTORE v25c6, v25c7(0x21e5383a00000000000000000000000000000000000000000000000000000000)
    0x25ea: v25ea(0x1) = CONST 
    0x25ec: v25ec(0xa0) = CONST 
    0x25ee: v25ee(0x2) = CONST 
    0x25f0: v25f0(0x10000000000000000000000000000000000000000) = EXP v25ee(0x2), v25ec(0xa0)
    0x25f1: v25f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25f0(0x10000000000000000000000000000000000000000), v25ea(0x1)
    0x25f4: v25f4 = AND v25f1(0xffffffffffffffffffffffffffffffffffffffff), v24ffarg2
    0x25f5: v25f5(0x4) = CONST 
    0x25f8: v25f8 = ADD v25c6, v25f5(0x4)
    0x25f9: MSTORE v25f8, v25f4
    0x25fa: v25fa(0x24) = CONST 
    0x25fd: v25fd = ADD v25c6, v25fa(0x24)
    0x2600: MSTORE v25fd, v24ffarg0
    0x2602: v2602 = MLOAD v25c3(0x40)
    0x2606: v2606 = AND v25c2, v25f1(0xffffffffffffffffffffffffffffffffffffffff)
    0x2608: v2608(0x21e5383a) = CONST 
    0x260e: v260e(0x44) = CONST 
    0x2612: v2612 = ADD v25c6, v260e(0x44)
    0x2614: v2614(0x0) = CONST 
    0x261b: v261b(0x0) = SUB v25c6, v2602
    0x261c: v261c(0x44) = ADD v261b(0x0), v260e(0x44)
    0x2621: v2621 = EXTCODESIZE v2606
    0x2622: v2622 = ISZERO v2621
    0x2624: v2624 = ISZERO v2622
    0x2625: v2625(0x262d) = CONST 
    0x2628: JUMPI v2625(0x262d), v2624

    Begin block 0x2629
    prev=[0x25bf], succ=[]
    =================================
    0x2629: v2629(0x0) = CONST 
    0x262c: REVERT v2629(0x0), v2629(0x0)

    Begin block 0x262d
    prev=[0x25bf], succ=[0x2638, 0x2641]
    =================================
    0x262f: v262f = GAS 
    0x2630: v2630 = CALL v262f, v2606, v2614(0x0), v2602, v261c(0x44), v2602, v2614(0x0)
    0x2631: v2631 = ISZERO v2630
    0x2633: v2633 = ISZERO v2631
    0x2634: v2634(0x2641) = CONST 
    0x2637: JUMPI v2634(0x2641), v2633

    Begin block 0x2638
    prev=[0x262d], succ=[]
    =================================
    0x2638: v2638 = RETURNDATASIZE 
    0x2639: v2639(0x0) = CONST 
    0x263c: RETURNDATACOPY v2639(0x0), v2639(0x0), v2638
    0x263d: v263d = RETURNDATASIZE 
    0x263e: v263e(0x0) = CONST 
    0x2640: REVERT v263e(0x0), v263d

    Begin block 0x2641
    prev=[0x262d], succ=[0x26af, 0x26b3]
    =================================
    0x2644: v2644(0x2) = CONST 
    0x2646: v2646 = SLOAD v2644(0x2)
    0x2647: v2647(0x40) = CONST 
    0x264a: v264a = MLOAD v2647(0x40)
    0x264b: v264b(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = CONST 
    0x266d: MSTORE v264a, v264b(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x266e: v266e(0x1) = CONST 
    0x2670: v2670(0xa0) = CONST 
    0x2672: v2672(0x2) = CONST 
    0x2674: v2674(0x10000000000000000000000000000000000000000) = EXP v2672(0x2), v2670(0xa0)
    0x2675: v2675(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2674(0x10000000000000000000000000000000000000000), v266e(0x1)
    0x2678: v2678 = AND v2675(0xffffffffffffffffffffffffffffffffffffffff), v24ffarg1
    0x2679: v2679(0x4) = CONST 
    0x267c: v267c = ADD v264a, v2679(0x4)
    0x267d: MSTORE v267c, v2678
    0x267e: v267e(0x24) = CONST 
    0x2681: v2681 = ADD v264a, v267e(0x24)
    0x2684: MSTORE v2681, v24ffarg0
    0x2686: v2686 = MLOAD v2647(0x40)
    0x268a: v268a = AND v2646, v2675(0xffffffffffffffffffffffffffffffffffffffff)
    0x268d: v268d(0xcf8eeb7e) = CONST 
    0x2694: v2694(0x44) = CONST 
    0x2698: v2698 = ADD v264a, v2694(0x44)
    0x269a: v269a(0x0) = CONST 
    0x26a1: v26a1(0x0) = SUB v264a, v2686
    0x26a2: v26a2(0x44) = ADD v26a1(0x0), v2694(0x44)
    0x26a7: v26a7 = EXTCODESIZE v268a
    0x26a8: v26a8 = ISZERO v26a7
    0x26aa: v26aa = ISZERO v26a8
    0x26ab: v26ab(0x26b3) = CONST 
    0x26ae: JUMPI v26ab(0x26b3), v26aa

    Begin block 0x26af
    prev=[0x2641], succ=[]
    =================================
    0x26af: v26af(0x0) = CONST 
    0x26b2: REVERT v26af(0x0), v26af(0x0)

    Begin block 0x26b3
    prev=[0x2641], succ=[0x26be, 0x26c7]
    =================================
    0x26b5: v26b5 = GAS 
    0x26b6: v26b6 = CALL v26b5, v268a, v269a(0x0), v2686, v26a2(0x44), v2686, v269a(0x0)
    0x26b7: v26b7 = ISZERO v26b6
    0x26b9: v26b9 = ISZERO v26b7
    0x26ba: v26ba(0x26c7) = CONST 
    0x26bd: JUMPI v26ba(0x26c7), v26b9

    Begin block 0x26be
    prev=[0x26b3], succ=[]
    =================================
    0x26be: v26be = RETURNDATASIZE 
    0x26bf: v26bf(0x0) = CONST 
    0x26c2: RETURNDATACOPY v26bf(0x0), v26bf(0x0), v26be
    0x26c3: v26c3 = RETURNDATASIZE 
    0x26c4: v26c4(0x0) = CONST 
    0x26c6: REVERT v26c4(0x0), v26c3

    Begin block 0x26c7
    prev=[0x26b3], succ=[]
    =================================
    0x26ca: v26ca(0x40) = CONST 
    0x26cd: v26cd = MLOAD v26ca(0x40)
    0x26d0: MSTORE v26cd, v24ffarg0
    0x26d2: v26d2 = MLOAD v26ca(0x40)
    0x26d3: v26d3(0x1) = CONST 
    0x26d5: v26d5(0xa0) = CONST 
    0x26d7: v26d7(0x2) = CONST 
    0x26d9: v26d9(0x10000000000000000000000000000000000000000) = EXP v26d7(0x2), v26d5(0xa0)
    0x26da: v26da(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26d9(0x10000000000000000000000000000000000000000), v26d3(0x1)
    0x26dd: v26dd = AND v24ffarg2, v26da(0xffffffffffffffffffffffffffffffffffffffff)
    0x26e1: v26e1 = AND v24ffarg1, v26da(0xffffffffffffffffffffffffffffffffffffffff)
    0x26e4: v26e4(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x2708: v2708(0x0) = SUB v26cd, v26d2
    0x2709: v2709(0x20) = CONST 
    0x270b: v270b(0x20) = ADD v2709(0x20), v2708(0x0)
    0x270d: LOG3 v26d2, v270b(0x20), v26e4(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v26e1, v26dd
    0x2711: RETURNPRIVATE v24ffarg3

}

function burn(uint256)() public {
    Begin block 0x260
    prev=[], succ=[0x268, 0x26c]
    =================================
    0x261: v261 = CALLVALUE 
    0x263: v263 = ISZERO v261
    0x264: v264(0x26c) = CONST 
    0x267: JUMPI v264(0x26c), v263

    Begin block 0x268
    prev=[0x260], succ=[]
    =================================
    0x268: v268(0x0) = CONST 
    0x26b: REVERT v268(0x0), v268(0x0)

    Begin block 0x26c
    prev=[0x260], succ=[0xfedB0x26c]
    =================================
    0x26e: v26e(0x30ce) = CONST 
    0x271: v271(0x4) = CONST 
    0x273: v273 = CALLDATALOAD v271(0x4)
    0x274: v274(0xfed) = CONST 
    0x277: JUMP v274(0xfed), v273, v26e(0x30ce)

    Begin block 0xfedB0x26c
    prev=[0x26c], succ=[0x103bB0x26c, 0x103fB0x26c]
    =================================
    0xfeeS0x26c: vfeeV26c(0x3) = CONST 
    0xff0S0x26c: vff0V26c = SLOAD vfeeV26c(0x3)
    0xff1S0x26c: vff1V26c(0x40) = CONST 
    0xff4S0x26c: vff4V26c = MLOAD vff1V26c(0x40)
    0xff5S0x26c: vff5V26c(0xe0) = CONST 
    0xff7S0x26c: vff7V26c(0x2) = CONST 
    0xff9S0x26c: vff9V26c(0x100000000000000000000000000000000000000000000000000000000) = EXP vff7V26c(0x2), vff5V26c(0xe0)
    0xffaS0x26c: vffaV26c(0x7ccce851) = CONST 
    0xfffS0x26c: vfffV26c(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL vffaV26c(0x7ccce851), vff9V26c(0x100000000000000000000000000000000000000000000000000000000)
    0x1001S0x26c: MSTORE vff4V26c, vfffV26c(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1002S0x26c: v1002V26c = CALLER 
    0x1003S0x26c: v1003V26c(0x4) = CONST 
    0x1006S0x26c: v1006V26c = ADD vff4V26c, v1003V26c(0x4)
    0x1009S0x26c: MSTORE v1006V26c, v1002V26c
    0x100bS0x26c: v100bV26c = MLOAD vff1V26c(0x40)
    0x100eS0x26c: v100eV26c(0x1) = CONST 
    0x1010S0x26c: v1010V26c(0xa0) = CONST 
    0x1012S0x26c: v1012V26c(0x2) = CONST 
    0x1014S0x26c: v1014V26c(0x10000000000000000000000000000000000000000) = EXP v1012V26c(0x2), v1010V26c(0xa0)
    0x1015S0x26c: v1015V26c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1014V26c(0x10000000000000000000000000000000000000000), v100eV26c(0x1)
    0x1016S0x26c: v1016V26c = AND v1015V26c(0xffffffffffffffffffffffffffffffffffffffff), vff0V26c
    0x1018S0x26c: v1018V26c(0x7ccce851) = CONST 
    0x101eS0x26c: v101eV26c(0x24) = CONST 
    0x1022S0x26c: v1022V26c = ADD vff4V26c, v101eV26c(0x24)
    0x1024S0x26c: v1024V26c(0x20) = CONST 
    0x102cS0x26c: v102cV26c(0x0) = SUB vff4V26c, v100bV26c
    0x102dS0x26c: v102dV26c(0x24) = ADD v102cV26c(0x0), v101eV26c(0x24)
    0x102fS0x26c: v102fV26c(0x0) = CONST 
    0x1033S0x26c: v1033V26c = EXTCODESIZE v1016V26c
    0x1034S0x26c: v1034V26c = ISZERO v1033V26c
    0x1036S0x26c: v1036V26c = ISZERO v1034V26c
    0x1037S0x26c: v1037V26c(0x103f) = CONST 
    0x103aS0x26c: JUMPI v1037V26c(0x103f), v1036V26c

    Begin block 0x103bB0x26c
    prev=[0xfedB0x26c], succ=[]
    =================================
    0x103bS0x26c: v103bV26c(0x0) = CONST 
    0x103eS0x26c: REVERT v103bV26c(0x0), v103bV26c(0x0)

    Begin block 0x103fB0x26c
    prev=[0xfedB0x26c], succ=[0x104aB0x26c, 0x1053B0x26c]
    =================================
    0x1041S0x26c: v1041V26c = GAS 
    0x1042S0x26c: v1042V26c = CALL v1041V26c, v1016V26c, v102fV26c(0x0), v100bV26c, v102dV26c(0x24), v100bV26c, v1024V26c(0x20)
    0x1043S0x26c: v1043V26c = ISZERO v1042V26c
    0x1045S0x26c: v1045V26c = ISZERO v1043V26c
    0x1046S0x26c: v1046V26c(0x1053) = CONST 
    0x1049S0x26c: JUMPI v1046V26c(0x1053), v1045V26c

    Begin block 0x104aB0x26c
    prev=[0x103fB0x26c], succ=[]
    =================================
    0x104aS0x26c: v104aV26c = RETURNDATASIZE 
    0x104bS0x26c: v104bV26c(0x0) = CONST 
    0x104eS0x26c: RETURNDATACOPY v104bV26c(0x0), v104bV26c(0x0), v104aV26c
    0x104fS0x26c: v104fV26c = RETURNDATASIZE 
    0x1050S0x26c: v1050V26c(0x0) = CONST 
    0x1052S0x26c: REVERT v1050V26c(0x0), v104fV26c

    Begin block 0x1053B0x26c
    prev=[0x103fB0x26c], succ=[0x1065B0x26c, 0x1069B0x26c]
    =================================
    0x1058S0x26c: v1058V26c(0x40) = CONST 
    0x105aS0x26c: v105aV26c = MLOAD v1058V26c(0x40)
    0x105bS0x26c: v105bV26c = RETURNDATASIZE 
    0x105cS0x26c: v105cV26c(0x20) = CONST 
    0x105fS0x26c: v105fV26c = LT v105bV26c, v105cV26c(0x20)
    0x1060S0x26c: v1060V26c = ISZERO v105fV26c
    0x1061S0x26c: v1061V26c(0x1069) = CONST 
    0x1064S0x26c: JUMPI v1061V26c(0x1069), v1060V26c

    Begin block 0x1065B0x26c
    prev=[0x1053B0x26c], succ=[]
    =================================
    0x1065S0x26c: v1065V26c(0x0) = CONST 
    0x1068S0x26c: REVERT v1065V26c(0x0), v1065V26c(0x0)

    Begin block 0x1069B0x26c
    prev=[0x1053B0x26c], succ=[0x1071B0x26c, 0x10aeB0x26c]
    =================================
    0x106bS0x26c: v106bV26c = MLOAD v105aV26c
    0x106cS0x26c: v106cV26c = ISZERO v106bV26c
    0x106dS0x26c: v106dV26c(0x10ae) = CONST 
    0x1070S0x26c: JUMPI v106dV26c(0x10ae), v106cV26c

    Begin block 0x1071B0x26c
    prev=[0x1069B0x26c], succ=[]
    =================================
    0x1071S0x26c: v1071V26c(0x40) = CONST 
    0x1074S0x26c: v1074V26c = MLOAD v1071V26c(0x40)
    0x1075S0x26c: v1075V26c(0xe5) = CONST 
    0x1077S0x26c: v1077V26c(0x2) = CONST 
    0x1079S0x26c: v1079V26c(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1077V26c(0x2), v1075V26c(0xe5)
    0x107aS0x26c: v107aV26c(0x461bcd) = CONST 
    0x107eS0x26c: v107eV26c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v107aV26c(0x461bcd), v1079V26c(0x2000000000000000000000000000000000000000000000000000000000)
    0x1080S0x26c: MSTORE v1074V26c, v107eV26c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1081S0x26c: v1081V26c(0x20) = CONST 
    0x1083S0x26c: v1083V26c(0x4) = CONST 
    0x1086S0x26c: v1086V26c = ADD v1074V26c, v1083V26c(0x4)
    0x1087S0x26c: MSTORE v1086V26c, v1081V26c(0x20)
    0x1088S0x26c: v1088V26c(0x1c) = CONST 
    0x108aS0x26c: v108aV26c(0x24) = CONST 
    0x108dS0x26c: v108dV26c = ADD v1074V26c, v108aV26c(0x24)
    0x108eS0x26c: MSTORE v108dV26c, v1088V26c(0x1c)
    0x108fS0x26c: v108fV26c(0x0) = CONST 
    0x1092S0x26c: v1092V26c = MLOAD v108fV26c(0x0)
    0x1093S0x26c: v1093V26c(0x20) = CONST 
    0x1095S0x26c: v1095V26c(0x2f6a) = CONST 
    0x109dS0x26c: MSTORE v108fV26c(0x0), v1092V26c
    0x109eS0x26c: v109eV26c(0x44) = CONST 
    0x10a1S0x26c: v10a1V26c = ADD v1074V26c, v109eV26c(0x44)
    0x10a2S0x26c: MSTORE v10a1V26c, v3658V26c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x10a4S0x26c: v10a4V26c = MLOAD v1071V26c(0x40)
    0x10a8S0x26c: v10a8V26c(0x0) = SUB v1074V26c, v10a4V26c
    0x10a9S0x26c: v10a9V26c(0x64) = CONST 
    0x10abS0x26c: v10abV26c(0x64) = ADD v10a9V26c(0x64), v10a8V26c(0x0)
    0x10adS0x26c: REVERT v10a4V26c, v10abV26c(0x64)
    0x3658S0x26c: v3658V26c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x10aeB0x26c
    prev=[0x1069B0x26c], succ=[0x10c1B0x26c, 0x10c5B0x26c]
    =================================
    0x10afS0x26c: v10afV26c(0x1) = CONST 
    0x10b1S0x26c: v10b1V26c = SLOAD v10afV26c(0x1)
    0x10b2S0x26c: v10b2V26c(0xa0) = CONST 
    0x10b4S0x26c: v10b4V26c(0x2) = CONST 
    0x10b6S0x26c: v10b6V26c(0x10000000000000000000000000000000000000000) = EXP v10b4V26c(0x2), v10b2V26c(0xa0)
    0x10b8S0x26c: v10b8V26c = DIV v10b1V26c, v10b6V26c(0x10000000000000000000000000000000000000000)
    0x10b9S0x26c: v10b9V26c(0xff) = CONST 
    0x10bbS0x26c: v10bbV26c = AND v10b9V26c(0xff), v10b8V26c
    0x10bcS0x26c: v10bcV26c = ISZERO v10bbV26c
    0x10bdS0x26c: v10bdV26c(0x10c5) = CONST 
    0x10c0S0x26c: JUMPI v10bdV26c(0x10c5), v10bcV26c

    Begin block 0x10c1B0x26c
    prev=[0x10aeB0x26c], succ=[]
    =================================
    0x10c1S0x26c: v10c1V26c(0x0) = CONST 
    0x10c4S0x26c: REVERT v10c1V26c(0x0), v10c1V26c(0x0)

    Begin block 0x10c5B0x26c
    prev=[0x10aeB0x26c], succ=[0x10cfB0x26c]
    =================================
    0x10c6S0x26c: v10c6V26c(0x10cf) = CONST 
    0x10c9S0x26c: v10c9V26c = CALLER 
    0x10cbS0x26c: v10cbV26c(0x2712) = CONST 
    0x10ceS0x26c: CALLPRIVATE v10cbV26c(0x2712), v273, v10c9V26c, v10c6V26c(0x10cf)

    Begin block 0x10cfB0x26c
    prev=[0x10c5B0x26c], succ=[0x30ce]
    =================================
    0x10d2S0x26c: JUMP v26e(0x30ce)

    Begin block 0x30ce
    prev=[0x10cfB0x26c], succ=[]
    =================================
    0x30cf: STOP 

}

function 0x2712(0x2712arg0x0, 0x2712arg0x1, 0x2712arg0x2) private {
    Begin block 0x2712
    prev=[], succ=[0x2723, 0x2772]
    =================================
    0x2713: v2713(0x1) = CONST 
    0x2715: v2715(0xa0) = CONST 
    0x2717: v2717(0x2) = CONST 
    0x2719: v2719(0x10000000000000000000000000000000000000000) = EXP v2717(0x2), v2715(0xa0)
    0x271a: v271a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2719(0x10000000000000000000000000000000000000000), v2713(0x1)
    0x271c: v271c = AND v2712arg1, v271a(0xffffffffffffffffffffffffffffffffffffffff)
    0x271d: v271d = ISZERO v271c
    0x271e: v271e = ISZERO v271d
    0x271f: v271f(0x2772) = CONST 
    0x2722: JUMPI v271f(0x2772), v271e

    Begin block 0x2723
    prev=[0x2712], succ=[]
    =================================
    0x2723: v2723(0x40) = CONST 
    0x2726: v2726 = MLOAD v2723(0x40)
    0x2727: v2727(0xe5) = CONST 
    0x2729: v2729(0x2) = CONST 
    0x272b: v272b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2729(0x2), v2727(0xe5)
    0x272c: v272c(0x461bcd) = CONST 
    0x2730: v2730(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v272c(0x461bcd), v272b(0x2000000000000000000000000000000000000000000000000000000000)
    0x2732: MSTORE v2726, v2730(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2733: v2733(0x20) = CONST 
    0x2735: v2735(0x4) = CONST 
    0x2738: v2738 = ADD v2726, v2735(0x4)
    0x2739: MSTORE v2738, v2733(0x20)
    0x273a: v273a(0x1c) = CONST 
    0x273c: v273c(0x24) = CONST 
    0x273f: v273f = ADD v2726, v273c(0x24)
    0x2740: MSTORE v273f, v273a(0x1c)
    0x2741: v2741(0x6275726e657220616464726573732063616e6e6f742062652030783000000000) = CONST 
    0x2762: v2762(0x44) = CONST 
    0x2765: v2765 = ADD v2726, v2762(0x44)
    0x2766: MSTORE v2765, v2741(0x6275726e657220616464726573732063616e6e6f742062652030783000000000)
    0x2768: v2768 = MLOAD v2723(0x40)
    0x276c: v276c(0x0) = SUB v2726, v2768
    0x276d: v276d(0x64) = CONST 
    0x276f: v276f(0x64) = ADD v276d(0x64), v276c(0x0)
    0x2771: REVERT v2768, v276f(0x64)

    Begin block 0x2772
    prev=[0x2712], succ=[0x277b]
    =================================
    0x2773: v2773(0x277b) = CONST 
    0x2777: v2777(0x16d7) = CONST 
    0x277a: v277a_0 = CALLPRIVATE v2777(0x16d7), v2712arg1, v2773(0x277b)

    Begin block 0x277b
    prev=[0x2772], succ=[0x2783, 0x27d2]
    =================================
    0x277d: v277d = GT v2712arg0, v277a_0
    0x277e: v277e = ISZERO v277d
    0x277f: v277f(0x27d2) = CONST 
    0x2782: JUMPI v277f(0x27d2), v277e

    Begin block 0x2783
    prev=[0x277b], succ=[]
    =================================
    0x2783: v2783(0x40) = CONST 
    0x2786: v2786 = MLOAD v2783(0x40)
    0x2787: v2787(0xe5) = CONST 
    0x2789: v2789(0x2) = CONST 
    0x278b: v278b(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2789(0x2), v2787(0xe5)
    0x278c: v278c(0x461bcd) = CONST 
    0x2790: v2790(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v278c(0x461bcd), v278b(0x2000000000000000000000000000000000000000000000000000000000)
    0x2792: MSTORE v2786, v2790(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2793: v2793(0x20) = CONST 
    0x2795: v2795(0x4) = CONST 
    0x2798: v2798 = ADD v2786, v2795(0x4)
    0x2799: MSTORE v2798, v2793(0x20)
    0x279a: v279a(0x1a) = CONST 
    0x279c: v279c(0x24) = CONST 
    0x279f: v279f = ADD v2786, v279c(0x24)
    0x27a0: MSTORE v279f, v279a(0x1a)
    0x27a1: v27a1(0x6e6f7420656e6f7567682062616c616e636520746f206275726e000000000000) = CONST 
    0x27c2: v27c2(0x44) = CONST 
    0x27c5: v27c5 = ADD v2786, v27c2(0x44)
    0x27c6: MSTORE v27c5, v27a1(0x6e6f7420656e6f7567682062616c616e636520746f206275726e000000000000)
    0x27c8: v27c8 = MLOAD v2783(0x40)
    0x27cc: v27cc(0x0) = SUB v2786, v27c8
    0x27cd: v27cd(0x64) = CONST 
    0x27cf: v27cf(0x64) = ADD v27cd(0x64), v27cc(0x0)
    0x27d1: REVERT v27c8, v27cf(0x64)

    Begin block 0x27d2
    prev=[0x277b], succ=[0x283c, 0x2840]
    =================================
    0x27d3: v27d3(0x2) = CONST 
    0x27d5: v27d5 = SLOAD v27d3(0x2)
    0x27d6: v27d6(0x40) = CONST 
    0x27d9: v27d9 = MLOAD v27d6(0x40)
    0x27da: v27da(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = CONST 
    0x27fc: MSTORE v27d9, v27da(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x27fd: v27fd(0x1) = CONST 
    0x27ff: v27ff(0xa0) = CONST 
    0x2801: v2801(0x2) = CONST 
    0x2803: v2803(0x10000000000000000000000000000000000000000) = EXP v2801(0x2), v27ff(0xa0)
    0x2804: v2804(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2803(0x10000000000000000000000000000000000000000), v27fd(0x1)
    0x2807: v2807 = AND v2804(0xffffffffffffffffffffffffffffffffffffffff), v2712arg1
    0x2808: v2808(0x4) = CONST 
    0x280b: v280b = ADD v27d9, v2808(0x4)
    0x280c: MSTORE v280b, v2807
    0x280d: v280d(0x24) = CONST 
    0x2810: v2810 = ADD v27d9, v280d(0x24)
    0x2813: MSTORE v2810, v2712arg0
    0x2815: v2815 = MLOAD v27d6(0x40)
    0x2819: v2819 = AND v27d5, v2804(0xffffffffffffffffffffffffffffffffffffffff)
    0x281b: v281b(0xcf8eeb7e) = CONST 
    0x2821: v2821(0x44) = CONST 
    0x2825: v2825 = ADD v27d9, v2821(0x44)
    0x2827: v2827(0x0) = CONST 
    0x282e: v282e(0x0) = SUB v27d9, v2815
    0x282f: v282f(0x44) = ADD v282e(0x0), v2821(0x44)
    0x2834: v2834 = EXTCODESIZE v2819
    0x2835: v2835 = ISZERO v2834
    0x2837: v2837 = ISZERO v2835
    0x2838: v2838(0x2840) = CONST 
    0x283b: JUMPI v2838(0x2840), v2837

    Begin block 0x283c
    prev=[0x27d2], succ=[]
    =================================
    0x283c: v283c(0x0) = CONST 
    0x283f: REVERT v283c(0x0), v283c(0x0)

    Begin block 0x2840
    prev=[0x27d2], succ=[0x284b, 0x2854]
    =================================
    0x2842: v2842 = GAS 
    0x2843: v2843 = CALL v2842, v2819, v2827(0x0), v2815, v282f(0x44), v2815, v2827(0x0)
    0x2844: v2844 = ISZERO v2843
    0x2846: v2846 = ISZERO v2844
    0x2847: v2847(0x2854) = CONST 
    0x284a: JUMPI v2847(0x2854), v2846

    Begin block 0x284b
    prev=[0x2840], succ=[]
    =================================
    0x284b: v284b = RETURNDATASIZE 
    0x284c: v284c(0x0) = CONST 
    0x284f: RETURNDATACOPY v284c(0x0), v284c(0x0), v284b
    0x2850: v2850 = RETURNDATASIZE 
    0x2851: v2851(0x0) = CONST 
    0x2853: REVERT v2851(0x0), v2850

    Begin block 0x2854
    prev=[0x2840], succ=[0x28ba, 0x28be]
    =================================
    0x2857: v2857(0x2) = CONST 
    0x2859: v2859 = SLOAD v2857(0x2)
    0x285a: v285a(0x40) = CONST 
    0x285d: v285d = MLOAD v285a(0x40)
    0x285e: v285e(0x82838c7600000000000000000000000000000000000000000000000000000000) = CONST 
    0x2880: MSTORE v285d, v285e(0x82838c7600000000000000000000000000000000000000000000000000000000)
    0x2881: v2881(0x4) = CONST 
    0x2884: v2884 = ADD v285d, v2881(0x4)
    0x2887: MSTORE v2884, v2712arg0
    0x2889: v2889 = MLOAD v285a(0x40)
    0x288a: v288a(0x1) = CONST 
    0x288c: v288c(0xa0) = CONST 
    0x288e: v288e(0x2) = CONST 
    0x2890: v2890(0x10000000000000000000000000000000000000000) = EXP v288e(0x2), v288c(0xa0)
    0x2891: v2891(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2890(0x10000000000000000000000000000000000000000), v288a(0x1)
    0x2894: v2894 = AND v2859, v2891(0xffffffffffffffffffffffffffffffffffffffff)
    0x2897: v2897(0x82838c76) = CONST 
    0x289e: v289e(0x24) = CONST 
    0x28a2: v28a2 = ADD v285d, v289e(0x24)
    0x28a4: v28a4(0x0) = CONST 
    0x28ac: v28ac(0x0) = SUB v285d, v2889
    0x28ad: v28ad(0x24) = ADD v28ac(0x0), v289e(0x24)
    0x28b2: v28b2 = EXTCODESIZE v2894
    0x28b3: v28b3 = ISZERO v28b2
    0x28b5: v28b5 = ISZERO v28b3
    0x28b6: v28b6(0x28be) = CONST 
    0x28b9: JUMPI v28b6(0x28be), v28b5

    Begin block 0x28ba
    prev=[0x2854], succ=[]
    =================================
    0x28ba: v28ba(0x0) = CONST 
    0x28bd: REVERT v28ba(0x0), v28ba(0x0)

    Begin block 0x28be
    prev=[0x2854], succ=[0x28c9, 0x28d2]
    =================================
    0x28c0: v28c0 = GAS 
    0x28c1: v28c1 = CALL v28c0, v2894, v28a4(0x0), v2889, v28ad(0x24), v2889, v28a4(0x0)
    0x28c2: v28c2 = ISZERO v28c1
    0x28c4: v28c4 = ISZERO v28c2
    0x28c5: v28c5(0x28d2) = CONST 
    0x28c8: JUMPI v28c5(0x28d2), v28c4

    Begin block 0x28c9
    prev=[0x28be], succ=[]
    =================================
    0x28c9: v28c9 = RETURNDATASIZE 
    0x28ca: v28ca(0x0) = CONST 
    0x28cd: RETURNDATACOPY v28ca(0x0), v28ca(0x0), v28c9
    0x28ce: v28ce = RETURNDATASIZE 
    0x28cf: v28cf(0x0) = CONST 
    0x28d1: REVERT v28cf(0x0), v28ce

    Begin block 0x28d2
    prev=[0x28be], succ=[]
    =================================
    0x28d5: v28d5(0x40) = CONST 
    0x28d8: v28d8 = MLOAD v28d5(0x40)
    0x28db: MSTORE v28d8, v2712arg0
    0x28dd: v28dd = MLOAD v28d5(0x40)
    0x28de: v28de(0x1) = CONST 
    0x28e0: v28e0(0xa0) = CONST 
    0x28e2: v28e2(0x2) = CONST 
    0x28e4: v28e4(0x10000000000000000000000000000000000000000) = EXP v28e2(0x2), v28e0(0xa0)
    0x28e5: v28e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v28e4(0x10000000000000000000000000000000000000000), v28de(0x1)
    0x28e7: v28e7 = AND v2712arg1, v28e5(0xffffffffffffffffffffffffffffffffffffffff)
    0x28ea: v28ea(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0x2910: v2910(0x0) = SUB v28d8, v28dd
    0x2911: v2911(0x20) = CONST 
    0x2913: v2913(0x20) = ADD v2911(0x20), v2910(0x0)
    0x2915: LOG2 v28dd, v2913(0x20), v28ea(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), v28e7
    0x2916: v2916(0x40) = CONST 
    0x2919: v2919 = MLOAD v2916(0x40)
    0x291c: MSTORE v2919, v2712arg0
    0x291e: v291e = MLOAD v2916(0x40)
    0x291f: v291f(0x0) = CONST 
    0x2922: v2922(0x1) = CONST 
    0x2924: v2924(0xa0) = CONST 
    0x2926: v2926(0x2) = CONST 
    0x2928: v2928(0x10000000000000000000000000000000000000000) = EXP v2926(0x2), v2924(0xa0)
    0x2929: v2929(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2928(0x10000000000000000000000000000000000000000), v2922(0x1)
    0x292b: v292b = AND v2712arg1, v2929(0xffffffffffffffffffffffffffffffffffffffff)
    0x292d: v292d(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x2951: v2951(0x0) = SUB v2919, v291e
    0x2952: v2952(0x20) = CONST 
    0x2954: v2954(0x20) = ADD v2952(0x20), v2951(0x0)
    0x2956: LOG3 v291e, v2954(0x20), v292d(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v292b, v291f(0x0)
    0x2959: RETURNPRIVATE v2712arg2

}

function claimOwnership()() public {
    Begin block 0x278
    prev=[], succ=[0x280, 0x284]
    =================================
    0x279: v279 = CALLVALUE 
    0x27b: v27b = ISZERO v279
    0x27c: v27c(0x284) = CONST 
    0x27f: JUMPI v27c(0x284), v27b

    Begin block 0x280
    prev=[0x278], succ=[]
    =================================
    0x280: v280(0x0) = CONST 
    0x283: REVERT v280(0x0), v280(0x0)

    Begin block 0x284
    prev=[0x278], succ=[0x10d3]
    =================================
    0x286: v286(0x30ef) = CONST 
    0x289: v289(0x10d3) = CONST 
    0x28c: JUMP v289(0x10d3)

    Begin block 0x10d3
    prev=[0x284], succ=[0x10e6, 0x10ea]
    =================================
    0x10d4: v10d4(0x1) = CONST 
    0x10d6: v10d6 = SLOAD v10d4(0x1)
    0x10d7: v10d7(0x1) = CONST 
    0x10d9: v10d9(0xa0) = CONST 
    0x10db: v10db(0x2) = CONST 
    0x10dd: v10dd(0x10000000000000000000000000000000000000000) = EXP v10db(0x2), v10d9(0xa0)
    0x10de: v10de(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10dd(0x10000000000000000000000000000000000000000), v10d7(0x1)
    0x10df: v10df = AND v10de(0xffffffffffffffffffffffffffffffffffffffff), v10d6
    0x10e0: v10e0 = CALLER 
    0x10e1: v10e1 = EQ v10e0, v10df
    0x10e2: v10e2(0x10ea) = CONST 
    0x10e5: JUMPI v10e2(0x10ea), v10e1

    Begin block 0x10e6
    prev=[0x10d3], succ=[]
    =================================
    0x10e6: v10e6(0x0) = CONST 
    0x10e9: REVERT v10e6(0x0), v10e6(0x0)

    Begin block 0x10ea
    prev=[0x10d3], succ=[0x30ef]
    =================================
    0x10eb: v10eb(0x1) = CONST 
    0x10ed: v10ed = SLOAD v10eb(0x1)
    0x10ee: v10ee(0x0) = CONST 
    0x10f1: v10f1 = SLOAD v10ee(0x0)
    0x10f2: v10f2(0x40) = CONST 
    0x10f4: v10f4 = MLOAD v10f2(0x40)
    0x10f5: v10f5(0x1) = CONST 
    0x10f7: v10f7(0xa0) = CONST 
    0x10f9: v10f9(0x2) = CONST 
    0x10fb: v10fb(0x10000000000000000000000000000000000000000) = EXP v10f9(0x2), v10f7(0xa0)
    0x10fc: v10fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10fb(0x10000000000000000000000000000000000000000), v10f5(0x1)
    0x10ff: v10ff = AND v10fc(0xffffffffffffffffffffffffffffffffffffffff), v10ed
    0x1103: v1103 = AND v10f1, v10fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x1105: v1105(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x1127: LOG3 v10f4, v10ee(0x0), v1105(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v1103, v10ff
    0x1128: v1128(0x1) = CONST 
    0x112b: v112b = SLOAD v1128(0x1)
    0x112c: v112c(0x0) = CONST 
    0x112f: v112f = SLOAD v112c(0x0)
    0x1130: v1130(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1145: v1145(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1130(0xffffffffffffffffffffffffffffffffffffffff)
    0x1148: v1148 = AND v1145(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v112f
    0x1149: v1149(0x1) = CONST 
    0x114b: v114b(0xa0) = CONST 
    0x114d: v114d(0x2) = CONST 
    0x114f: v114f(0x10000000000000000000000000000000000000000) = EXP v114d(0x2), v114b(0xa0)
    0x1150: v1150(0xffffffffffffffffffffffffffffffffffffffff) = SUB v114f(0x10000000000000000000000000000000000000000), v1149(0x1)
    0x1152: v1152 = AND v112b, v1150(0xffffffffffffffffffffffffffffffffffffffff)
    0x1153: v1153 = OR v1152, v1148
    0x1156: SSTORE v112c(0x0), v1153
    0x1157: v1157 = AND v1145(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v112b
    0x1159: SSTORE v1128(0x1), v1157
    0x115a: JUMP v286(0x30ef)

    Begin block 0x30ef
    prev=[0x10ea], succ=[]
    =================================
    0x30f0: STOP 

}

function blacklisted()() public {
    Begin block 0x28d
    prev=[], succ=[0x295, 0x299]
    =================================
    0x28e: v28e = CALLVALUE 
    0x290: v290 = ISZERO v28e
    0x291: v291(0x299) = CONST 
    0x294: JUMPI v291(0x299), v290

    Begin block 0x295
    prev=[0x28d], succ=[]
    =================================
    0x295: v295(0x0) = CONST 
    0x298: REVERT v295(0x0), v295(0x0)

    Begin block 0x299
    prev=[0x28d], succ=[0x115b]
    =================================
    0x29b: v29b(0x3110) = CONST 
    0x29e: v29e(0x115b) = CONST 
    0x2a1: JUMP v29e(0x115b)

    Begin block 0x115b
    prev=[0x299], succ=[0x11b9, 0x11bd]
    =================================
    0x115c: v115c(0x3) = CONST 
    0x115e: v115e = SLOAD v115c(0x3)
    0x115f: v115f(0x40) = CONST 
    0x1162: v1162 = MLOAD v115f(0x40)
    0x1163: v1163(0xe3) = CONST 
    0x1165: v1165(0x2) = CONST 
    0x1167: v1167(0x800000000000000000000000000000000000000000000000000000000) = EXP v1165(0x2), v1163(0xe3)
    0x1168: v1168(0x29b6dab) = CONST 
    0x116d: v116d(0x14db6d5800000000000000000000000000000000000000000000000000000000) = MUL v1168(0x29b6dab), v1167(0x800000000000000000000000000000000000000000000000000000000)
    0x116f: MSTORE v1162, v116d(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1170: v1170 = CALLER 
    0x1171: v1171(0x4) = CONST 
    0x1174: v1174 = ADD v1162, v1171(0x4)
    0x1175: MSTORE v1174, v1170
    0x1176: v1176(0x0) = CONST 
    0x1179: v1179 = CALLDATALOAD v1176(0x0)
    0x117a: v117a(0x1) = CONST 
    0x117c: v117c(0xe0) = CONST 
    0x117e: v117e(0x2) = CONST 
    0x1180: v1180(0x100000000000000000000000000000000000000000000000000000000) = EXP v117e(0x2), v117c(0xe0)
    0x1181: v1181(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1180(0x100000000000000000000000000000000000000000000000000000000), v117a(0x1)
    0x1182: v1182(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1181(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1183: v1183 = AND v1182(0xffffffff00000000000000000000000000000000000000000000000000000000), v1179
    0x1184: v1184(0x24) = CONST 
    0x1187: v1187 = ADD v1162, v1184(0x24)
    0x1188: MSTORE v1187, v1183
    0x118a: v118a = MLOAD v115f(0x40)
    0x118d: v118d(0x1) = CONST 
    0x118f: v118f(0xa0) = CONST 
    0x1191: v1191(0x2) = CONST 
    0x1193: v1193(0x10000000000000000000000000000000000000000) = EXP v1191(0x2), v118f(0xa0)
    0x1194: v1194(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1193(0x10000000000000000000000000000000000000000), v118d(0x1)
    0x1195: v1195 = AND v1194(0xffffffffffffffffffffffffffffffffffffffff), v115e
    0x1197: v1197(0x14db6d58) = CONST 
    0x119d: v119d(0x44) = CONST 
    0x11a1: v11a1 = ADD v1162, v119d(0x44)
    0x11a3: v11a3(0x20) = CONST 
    0x11ab: v11ab(0x0) = SUB v1162, v118a
    0x11ac: v11ac(0x44) = ADD v11ab(0x0), v119d(0x44)
    0x11b1: v11b1 = EXTCODESIZE v1195
    0x11b2: v11b2 = ISZERO v11b1
    0x11b4: v11b4 = ISZERO v11b2
    0x11b5: v11b5(0x11bd) = CONST 
    0x11b8: JUMPI v11b5(0x11bd), v11b4

    Begin block 0x11b9
    prev=[0x115b], succ=[]
    =================================
    0x11b9: v11b9(0x0) = CONST 
    0x11bc: REVERT v11b9(0x0), v11b9(0x0)

    Begin block 0x11bd
    prev=[0x115b], succ=[0x11c8, 0x11d1]
    =================================
    0x11bf: v11bf = GAS 
    0x11c0: v11c0 = CALL v11bf, v1195, v1176(0x0), v118a, v11ac(0x44), v118a, v11a3(0x20)
    0x11c1: v11c1 = ISZERO v11c0
    0x11c3: v11c3 = ISZERO v11c1
    0x11c4: v11c4(0x11d1) = CONST 
    0x11c7: JUMPI v11c4(0x11d1), v11c3

    Begin block 0x11c8
    prev=[0x11bd], succ=[]
    =================================
    0x11c8: v11c8 = RETURNDATASIZE 
    0x11c9: v11c9(0x0) = CONST 
    0x11cc: RETURNDATACOPY v11c9(0x0), v11c9(0x0), v11c8
    0x11cd: v11cd = RETURNDATASIZE 
    0x11ce: v11ce(0x0) = CONST 
    0x11d0: REVERT v11ce(0x0), v11cd

    Begin block 0x11d1
    prev=[0x11bd], succ=[0x11e3, 0x11e7]
    =================================
    0x11d6: v11d6(0x40) = CONST 
    0x11d8: v11d8 = MLOAD v11d6(0x40)
    0x11d9: v11d9 = RETURNDATASIZE 
    0x11da: v11da(0x20) = CONST 
    0x11dd: v11dd = LT v11d9, v11da(0x20)
    0x11de: v11de = ISZERO v11dd
    0x11df: v11df(0x11e7) = CONST 
    0x11e2: JUMPI v11df(0x11e7), v11de

    Begin block 0x11e3
    prev=[0x11d1], succ=[]
    =================================
    0x11e3: v11e3(0x0) = CONST 
    0x11e6: REVERT v11e3(0x0), v11e3(0x0)

    Begin block 0x11e7
    prev=[0x11d1], succ=[0x11f0, 0x1241]
    =================================
    0x11e9: v11e9 = MLOAD v11d8
    0x11ea: v11ea = ISZERO v11e9
    0x11eb: v11eb = ISZERO v11ea
    0x11ec: v11ec(0x1241) = CONST 
    0x11ef: JUMPI v11ec(0x1241), v11eb

    Begin block 0x11f0
    prev=[0x11e7], succ=[]
    =================================
    0x11f0: v11f0(0x40) = CONST 
    0x11f3: v11f3 = MLOAD v11f0(0x40)
    0x11f4: v11f4(0xe5) = CONST 
    0x11f6: v11f6(0x2) = CONST 
    0x11f8: v11f8(0x2000000000000000000000000000000000000000000000000000000000) = EXP v11f6(0x2), v11f4(0xe5)
    0x11f9: v11f9(0x461bcd) = CONST 
    0x11fd: v11fd(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v11f9(0x461bcd), v11f8(0x2000000000000000000000000000000000000000000000000000000000)
    0x11ff: MSTORE v11f3, v11fd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1200: v1200(0x20) = CONST 
    0x1202: v1202(0x4) = CONST 
    0x1205: v1205 = ADD v11f3, v1202(0x4)
    0x1206: MSTORE v1205, v1200(0x20)
    0x1207: v1207(0x31) = CONST 
    0x1209: v1209(0x24) = CONST 
    0x120c: v120c = ADD v11f3, v1209(0x24)
    0x120d: MSTORE v120c, v1207(0x31)
    0x120e: v120e(0x0) = CONST 
    0x1211: v1211 = MLOAD v120e(0x0)
    0x1212: v1212(0x20) = CONST 
    0x1214: v1214(0x2f4a) = CONST 
    0x121c: MSTORE v120e(0x0), v1211
    0x121d: v121d(0x44) = CONST 
    0x1220: v1220 = ADD v11f3, v121d(0x44)
    0x1221: MSTORE v1220, v365d(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x1222: v1222(0x0) = CONST 
    0x1225: v1225 = MLOAD v1222(0x0)
    0x1226: v1226(0x20) = CONST 
    0x1228: v1228(0x2f2a) = CONST 
    0x1230: MSTORE v1222(0x0), v1225
    0x1231: v1231(0x64) = CONST 
    0x1234: v1234 = ADD v11f3, v1231(0x64)
    0x1235: MSTORE v1234, v3662(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x1237: v1237 = MLOAD v11f0(0x40)
    0x123b: v123b(0x0) = SUB v11f3, v1237
    0x123c: v123c(0x84) = CONST 
    0x123e: v123e(0x84) = ADD v123c(0x84), v123b(0x0)
    0x1240: REVERT v1237, v123e(0x84)
    0x365d: v365d(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x3662: v3662(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 

    Begin block 0x1241
    prev=[0x11e7], succ=[0x3110]
    =================================
    0x1243: v1243(0x1) = CONST 
    0x1246: JUMP v29b(0x3110)

    Begin block 0x3110
    prev=[0x1241], succ=[]
    =================================
    0x3111: v3111(0x40) = CONST 
    0x3114: v3114 = MLOAD v3111(0x40)
    0x3116: v3116 = ISZERO v1243(0x1)
    0x3117: v3117 = ISZERO v3116
    0x3119: MSTORE v3114, v3117
    0x311a: v311a = MLOAD v3111(0x40)
    0x311e: v311e(0x0) = SUB v3114, v311a
    0x311f: v311f(0x20) = CONST 
    0x3121: v3121(0x20) = ADD v311f(0x20), v311e(0x0)
    0x3123: RETURN v311a, v3121(0x20)

}

function 0x295a(0x295aarg0x0, 0x295aarg0x1, 0x295aarg0x2) private {
    Begin block 0x295a
    prev=[], succ=[0x2971, 0x29e6]
    =================================
    0x295b: v295b(0x4) = CONST 
    0x295d: v295d = SLOAD v295b(0x4)
    0x295e: v295e(0x1) = CONST 
    0x2960: v2960(0xa0) = CONST 
    0x2962: v2962(0x2) = CONST 
    0x2964: v2964(0x10000000000000000000000000000000000000000) = EXP v2962(0x2), v2960(0xa0)
    0x2965: v2965(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2964(0x10000000000000000000000000000000000000000), v295e(0x1)
    0x2968: v2968 = AND v2965(0xffffffffffffffffffffffffffffffffffffffff), v295aarg1
    0x296a: v296a = AND v295d, v2965(0xffffffffffffffffffffffffffffffffffffffff)
    0x296b: v296b = EQ v296a, v2968
    0x296c: v296c = ISZERO v296b
    0x296d: v296d(0x29e6) = CONST 
    0x2970: JUMPI v296d(0x29e6), v296c

    Begin block 0x2971
    prev=[0x295a], succ=[]
    =================================
    0x2971: v2971(0x40) = CONST 
    0x2974: v2974 = MLOAD v2971(0x40)
    0x2975: v2975(0xe5) = CONST 
    0x2977: v2977(0x2) = CONST 
    0x2979: v2979(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2977(0x2), v2975(0xe5)
    0x297a: v297a(0x461bcd) = CONST 
    0x297e: v297e(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v297a(0x461bcd), v2979(0x2000000000000000000000000000000000000000000000000000000000)
    0x2980: MSTORE v2974, v297e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2981: v2981(0x20) = CONST 
    0x2983: v2983(0x4) = CONST 
    0x2986: v2986 = ADD v2974, v2983(0x4)
    0x2987: MSTORE v2986, v2981(0x20)
    0x2988: v2988(0x21) = CONST 
    0x298a: v298a(0x24) = CONST 
    0x298d: v298d = ADD v2974, v298a(0x24)
    0x298e: MSTORE v298d, v2988(0x21)
    0x298f: v298f(0x43616e6e6f74206d696e7420746f20436172626f6e55534420636f6e74726163) = CONST 
    0x29b0: v29b0(0x44) = CONST 
    0x29b3: v29b3 = ADD v2974, v29b0(0x44)
    0x29b4: MSTORE v29b3, v298f(0x43616e6e6f74206d696e7420746f20436172626f6e55534420636f6e74726163)
    0x29b5: v29b5(0x7400000000000000000000000000000000000000000000000000000000000000) = CONST 
    0x29d6: v29d6(0x64) = CONST 
    0x29d9: v29d9 = ADD v2974, v29d6(0x64)
    0x29da: MSTORE v29d9, v29b5(0x7400000000000000000000000000000000000000000000000000000000000000)
    0x29dc: v29dc = MLOAD v2971(0x40)
    0x29e0: v29e0(0x0) = SUB v2974, v29dc
    0x29e1: v29e1(0x84) = CONST 
    0x29e3: v29e3(0x84) = ADD v29e1(0x84), v29e0(0x0)
    0x29e5: REVERT v29dc, v29e3(0x84)

    Begin block 0x29e6
    prev=[0x295a], succ=[0x2a54, 0x2a58]
    =================================
    0x29e7: v29e7(0x4) = CONST 
    0x29ea: v29ea = SLOAD v29e7(0x4)
    0x29eb: v29eb(0x40) = CONST 
    0x29ee: v29ee = MLOAD v29eb(0x40)
    0x29ef: v29ef(0x40c10f1900000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a11: MSTORE v29ee, v29ef(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0x2a12: v2a12(0x1) = CONST 
    0x2a14: v2a14(0xa0) = CONST 
    0x2a16: v2a16(0x2) = CONST 
    0x2a18: v2a18(0x10000000000000000000000000000000000000000) = EXP v2a16(0x2), v2a14(0xa0)
    0x2a19: v2a19(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a18(0x10000000000000000000000000000000000000000), v2a12(0x1)
    0x2a1c: v2a1c = AND v2a19(0xffffffffffffffffffffffffffffffffffffffff), v295aarg1
    0x2a1f: v2a1f = ADD v29ee, v29e7(0x4)
    0x2a23: MSTORE v2a1f, v2a1c
    0x2a24: v2a24(0x24) = CONST 
    0x2a27: v2a27 = ADD v29ee, v2a24(0x24)
    0x2a2a: MSTORE v2a27, v295aarg0
    0x2a2c: v2a2c = MLOAD v29eb(0x40)
    0x2a30: v2a30 = AND v29ea, v2a19(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a32: v2a32(0x40c10f19) = CONST 
    0x2a38: v2a38(0x44) = CONST 
    0x2a3c: v2a3c = ADD v29ee, v2a38(0x44)
    0x2a3e: v2a3e(0x0) = CONST 
    0x2a46: v2a46(0x0) = SUB v29ee, v2a2c
    0x2a47: v2a47(0x44) = ADD v2a46(0x0), v2a38(0x44)
    0x2a4c: v2a4c = EXTCODESIZE v2a30
    0x2a4d: v2a4d = ISZERO v2a4c
    0x2a4f: v2a4f = ISZERO v2a4d
    0x2a50: v2a50(0x2a58) = CONST 
    0x2a53: JUMPI v2a50(0x2a58), v2a4f

    Begin block 0x2a54
    prev=[0x29e6], succ=[]
    =================================
    0x2a54: v2a54(0x0) = CONST 
    0x2a57: REVERT v2a54(0x0), v2a54(0x0)

    Begin block 0x2a58
    prev=[0x29e6], succ=[0x2a63, 0x2a6c]
    =================================
    0x2a5a: v2a5a = GAS 
    0x2a5b: v2a5b = CALL v2a5a, v2a30, v2a3e(0x0), v2a2c, v2a47(0x44), v2a2c, v2a3e(0x0)
    0x2a5c: v2a5c = ISZERO v2a5b
    0x2a5e: v2a5e = ISZERO v2a5c
    0x2a5f: v2a5f(0x2a6c) = CONST 
    0x2a62: JUMPI v2a5f(0x2a6c), v2a5e

    Begin block 0x2a63
    prev=[0x2a58], succ=[]
    =================================
    0x2a63: v2a63 = RETURNDATASIZE 
    0x2a64: v2a64(0x0) = CONST 
    0x2a67: RETURNDATACOPY v2a64(0x0), v2a64(0x0), v2a63
    0x2a68: v2a68 = RETURNDATASIZE 
    0x2a69: v2a69(0x0) = CONST 
    0x2a6b: REVERT v2a69(0x0), v2a68

    Begin block 0x2a6c
    prev=[0x2a58], succ=[0x2a87]
    =================================
    0x2a6f: v2a6f(0x4) = CONST 
    0x2a71: v2a71 = SLOAD v2a6f(0x4)
    0x2a72: v2a72(0x2a87) = CONST 
    0x2a77: v2a77(0x1) = CONST 
    0x2a79: v2a79(0xa0) = CONST 
    0x2a7b: v2a7b(0x2) = CONST 
    0x2a7d: v2a7d(0x10000000000000000000000000000000000000000) = EXP v2a7b(0x2), v2a79(0xa0)
    0x2a7e: v2a7e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a7d(0x10000000000000000000000000000000000000000), v2a77(0x1)
    0x2a7f: v2a7f = AND v2a7e(0xffffffffffffffffffffffffffffffffffffffff), v2a71
    0x2a83: v2a83(0x2aca) = CONST 
    0x2a86: CALLPRIVATE v2a83(0x2aca), v295aarg0, v2a7f, v2a72(0x2a87)

    Begin block 0x2a87
    prev=[0x2a6c], succ=[]
    =================================
    0x2a88: v2a88(0x40) = CONST 
    0x2a8b: v2a8b = MLOAD v2a88(0x40)
    0x2a8e: MSTORE v2a8b, v295aarg0
    0x2a90: v2a90 = MLOAD v2a88(0x40)
    0x2a91: v2a91(0x1) = CONST 
    0x2a93: v2a93(0xa0) = CONST 
    0x2a95: v2a95(0x2) = CONST 
    0x2a97: v2a97(0x10000000000000000000000000000000000000000) = EXP v2a95(0x2), v2a93(0xa0)
    0x2a98: v2a98(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2a97(0x10000000000000000000000000000000000000000), v2a91(0x1)
    0x2a9a: v2a9a = AND v295aarg1, v2a98(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a9c: v2a9c(0xaa3eb15142a2b8e4c65e571df7bdd989b9f56c6034258ede1c26c1f89d6e3c2) = CONST 
    0x2ac1: v2ac1(0x0) = SUB v2a8b, v2a90
    0x2ac2: v2ac2(0x20) = CONST 
    0x2ac4: v2ac4(0x20) = ADD v2ac2(0x20), v2ac1(0x0)
    0x2ac6: LOG2 v2a90, v2ac4(0x20), v2a9c(0xaa3eb15142a2b8e4c65e571df7bdd989b9f56c6034258ede1c26c1f89d6e3c2), v2a9a
    0x2ac9: RETURNPRIVATE v295aarg2

}

function paused()() public {
    Begin block 0x2a2
    prev=[], succ=[0x2aa, 0x2ae]
    =================================
    0x2a3: v2a3 = CALLVALUE 
    0x2a5: v2a5 = ISZERO v2a3
    0x2a6: v2a6(0x2ae) = CONST 
    0x2a9: JUMPI v2a6(0x2ae), v2a5

    Begin block 0x2aa
    prev=[0x2a2], succ=[]
    =================================
    0x2aa: v2aa(0x0) = CONST 
    0x2ad: REVERT v2aa(0x0), v2aa(0x0)

    Begin block 0x2ae
    prev=[0x2a2], succ=[0x1247]
    =================================
    0x2b0: v2b0(0x3143) = CONST 
    0x2b3: v2b3(0x1247) = CONST 
    0x2b6: JUMP v2b3(0x1247)

    Begin block 0x1247
    prev=[0x2ae], succ=[0x3143]
    =================================
    0x1248: v1248(0x1) = CONST 
    0x124a: v124a = SLOAD v1248(0x1)
    0x124b: v124b(0xa0) = CONST 
    0x124d: v124d(0x2) = CONST 
    0x124f: v124f(0x10000000000000000000000000000000000000000) = EXP v124d(0x2), v124b(0xa0)
    0x1251: v1251 = DIV v124a, v124f(0x10000000000000000000000000000000000000000)
    0x1252: v1252(0xff) = CONST 
    0x1254: v1254 = AND v1252(0xff), v1251
    0x1256: JUMP v2b0(0x3143)

    Begin block 0x3143
    prev=[0x1247], succ=[]
    =================================
    0x3144: v3144(0x40) = CONST 
    0x3147: v3147 = MLOAD v3144(0x40)
    0x3149: v3149 = ISZERO v1254
    0x314a: v314a = ISZERO v3149
    0x314c: MSTORE v3147, v314a
    0x314d: v314d = MLOAD v3144(0x40)
    0x3151: v3151(0x0) = SUB v3147, v314d
    0x3152: v3152(0x20) = CONST 
    0x3154: v3154(0x20) = ADD v3152(0x20), v3151(0x0)
    0x3156: RETURN v314d, v3154(0x20)

}

function 0x2aca(0x2acaarg0x0, 0x2acaarg0x1, 0x2acaarg0x2) private {
    Begin block 0x2aca
    prev=[], succ=[0x2adb, 0x2b2a]
    =================================
    0x2acb: v2acb(0x1) = CONST 
    0x2acd: v2acd(0xa0) = CONST 
    0x2acf: v2acf(0x2) = CONST 
    0x2ad1: v2ad1(0x10000000000000000000000000000000000000000) = EXP v2acf(0x2), v2acd(0xa0)
    0x2ad2: v2ad2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ad1(0x10000000000000000000000000000000000000000), v2acb(0x1)
    0x2ad4: v2ad4 = AND v2acaarg1, v2ad2(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ad5: v2ad5 = ISZERO v2ad4
    0x2ad6: v2ad6 = ISZERO v2ad5
    0x2ad7: v2ad7(0x2b2a) = CONST 
    0x2ada: JUMPI v2ad7(0x2b2a), v2ad6

    Begin block 0x2adb
    prev=[0x2aca], succ=[]
    =================================
    0x2adb: v2adb(0x40) = CONST 
    0x2ade: v2ade = MLOAD v2adb(0x40)
    0x2adf: v2adf(0xe5) = CONST 
    0x2ae1: v2ae1(0x2) = CONST 
    0x2ae3: v2ae3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2ae1(0x2), v2adf(0xe5)
    0x2ae4: v2ae4(0x461bcd) = CONST 
    0x2ae8: v2ae8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2ae4(0x461bcd), v2ae3(0x2000000000000000000000000000000000000000000000000000000000)
    0x2aea: MSTORE v2ade, v2ae8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2aeb: v2aeb(0x20) = CONST 
    0x2aed: v2aed(0x4) = CONST 
    0x2af0: v2af0 = ADD v2ade, v2aed(0x4)
    0x2af1: MSTORE v2af0, v2aeb(0x20)
    0x2af2: v2af2(0x18) = CONST 
    0x2af4: v2af4(0x24) = CONST 
    0x2af7: v2af7 = ADD v2ade, v2af4(0x24)
    0x2af8: MSTORE v2af7, v2af2(0x18)
    0x2af9: v2af9(0x746f20616464726573732063616e6e6f74206265203078300000000000000000) = CONST 
    0x2b1a: v2b1a(0x44) = CONST 
    0x2b1d: v2b1d = ADD v2ade, v2b1a(0x44)
    0x2b1e: MSTORE v2b1d, v2af9(0x746f20616464726573732063616e6e6f74206265203078300000000000000000)
    0x2b20: v2b20 = MLOAD v2adb(0x40)
    0x2b24: v2b24(0x0) = SUB v2ade, v2b20
    0x2b25: v2b25(0x64) = CONST 
    0x2b27: v2b27(0x64) = ADD v2b25(0x64), v2b24(0x0)
    0x2b29: REVERT v2b20, v2b27(0x64)

    Begin block 0x2b2a
    prev=[0x2aca], succ=[0x2b8c, 0x2b90]
    =================================
    0x2b2b: v2b2b(0x2) = CONST 
    0x2b2d: v2b2d = SLOAD v2b2b(0x2)
    0x2b2e: v2b2e(0x40) = CONST 
    0x2b31: v2b31 = MLOAD v2b2e(0x40)
    0x2b32: v2b32(0xe468688e00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2b54: MSTORE v2b31, v2b32(0xe468688e00000000000000000000000000000000000000000000000000000000)
    0x2b55: v2b55(0x4) = CONST 
    0x2b58: v2b58 = ADD v2b31, v2b55(0x4)
    0x2b5b: MSTORE v2b58, v2acaarg0
    0x2b5d: v2b5d = MLOAD v2b2e(0x40)
    0x2b5e: v2b5e(0x1) = CONST 
    0x2b60: v2b60(0xa0) = CONST 
    0x2b62: v2b62(0x2) = CONST 
    0x2b64: v2b64(0x10000000000000000000000000000000000000000) = EXP v2b62(0x2), v2b60(0xa0)
    0x2b65: v2b65(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b64(0x10000000000000000000000000000000000000000), v2b5e(0x1)
    0x2b68: v2b68 = AND v2b2d, v2b65(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b6a: v2b6a(0xe468688e) = CONST 
    0x2b70: v2b70(0x24) = CONST 
    0x2b74: v2b74 = ADD v2b31, v2b70(0x24)
    0x2b76: v2b76(0x0) = CONST 
    0x2b7e: v2b7e(0x0) = SUB v2b31, v2b5d
    0x2b7f: v2b7f(0x24) = ADD v2b7e(0x0), v2b70(0x24)
    0x2b84: v2b84 = EXTCODESIZE v2b68
    0x2b85: v2b85 = ISZERO v2b84
    0x2b87: v2b87 = ISZERO v2b85
    0x2b88: v2b88(0x2b90) = CONST 
    0x2b8b: JUMPI v2b88(0x2b90), v2b87

    Begin block 0x2b8c
    prev=[0x2b2a], succ=[]
    =================================
    0x2b8c: v2b8c(0x0) = CONST 
    0x2b8f: REVERT v2b8c(0x0), v2b8c(0x0)

    Begin block 0x2b90
    prev=[0x2b2a], succ=[0x2b9b, 0x2ba4]
    =================================
    0x2b92: v2b92 = GAS 
    0x2b93: v2b93 = CALL v2b92, v2b68, v2b76(0x0), v2b5d, v2b7f(0x24), v2b5d, v2b76(0x0)
    0x2b94: v2b94 = ISZERO v2b93
    0x2b96: v2b96 = ISZERO v2b94
    0x2b97: v2b97(0x2ba4) = CONST 
    0x2b9a: JUMPI v2b97(0x2ba4), v2b96

    Begin block 0x2b9b
    prev=[0x2b90], succ=[]
    =================================
    0x2b9b: v2b9b = RETURNDATASIZE 
    0x2b9c: v2b9c(0x0) = CONST 
    0x2b9f: RETURNDATACOPY v2b9c(0x0), v2b9c(0x0), v2b9b
    0x2ba0: v2ba0 = RETURNDATASIZE 
    0x2ba1: v2ba1(0x0) = CONST 
    0x2ba3: REVERT v2ba1(0x0), v2ba0

    Begin block 0x2ba4
    prev=[0x2b90], succ=[0x2c12, 0x2c16]
    =================================
    0x2ba7: v2ba7(0x2) = CONST 
    0x2ba9: v2ba9 = SLOAD v2ba7(0x2)
    0x2baa: v2baa(0x40) = CONST 
    0x2bad: v2bad = MLOAD v2baa(0x40)
    0x2bae: v2bae(0x21e5383a00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2bd0: MSTORE v2bad, v2bae(0x21e5383a00000000000000000000000000000000000000000000000000000000)
    0x2bd1: v2bd1(0x1) = CONST 
    0x2bd3: v2bd3(0xa0) = CONST 
    0x2bd5: v2bd5(0x2) = CONST 
    0x2bd7: v2bd7(0x10000000000000000000000000000000000000000) = EXP v2bd5(0x2), v2bd3(0xa0)
    0x2bd8: v2bd8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2bd7(0x10000000000000000000000000000000000000000), v2bd1(0x1)
    0x2bdb: v2bdb = AND v2bd8(0xffffffffffffffffffffffffffffffffffffffff), v2acaarg1
    0x2bdc: v2bdc(0x4) = CONST 
    0x2bdf: v2bdf = ADD v2bad, v2bdc(0x4)
    0x2be0: MSTORE v2bdf, v2bdb
    0x2be1: v2be1(0x24) = CONST 
    0x2be4: v2be4 = ADD v2bad, v2be1(0x24)
    0x2be7: MSTORE v2be4, v2acaarg0
    0x2be9: v2be9 = MLOAD v2baa(0x40)
    0x2bed: v2bed = AND v2ba9, v2bd8(0xffffffffffffffffffffffffffffffffffffffff)
    0x2bf0: v2bf0(0x21e5383a) = CONST 
    0x2bf7: v2bf7(0x44) = CONST 
    0x2bfb: v2bfb = ADD v2bad, v2bf7(0x44)
    0x2bfd: v2bfd(0x0) = CONST 
    0x2c04: v2c04(0x0) = SUB v2bad, v2be9
    0x2c05: v2c05(0x44) = ADD v2c04(0x0), v2bf7(0x44)
    0x2c0a: v2c0a = EXTCODESIZE v2bed
    0x2c0b: v2c0b = ISZERO v2c0a
    0x2c0d: v2c0d = ISZERO v2c0b
    0x2c0e: v2c0e(0x2c16) = CONST 
    0x2c11: JUMPI v2c0e(0x2c16), v2c0d

    Begin block 0x2c12
    prev=[0x2ba4], succ=[]
    =================================
    0x2c12: v2c12(0x0) = CONST 
    0x2c15: REVERT v2c12(0x0), v2c12(0x0)

    Begin block 0x2c16
    prev=[0x2ba4], succ=[0x2c21, 0x2c2a]
    =================================
    0x2c18: v2c18 = GAS 
    0x2c19: v2c19 = CALL v2c18, v2bed, v2bfd(0x0), v2be9, v2c05(0x44), v2be9, v2bfd(0x0)
    0x2c1a: v2c1a = ISZERO v2c19
    0x2c1c: v2c1c = ISZERO v2c1a
    0x2c1d: v2c1d(0x2c2a) = CONST 
    0x2c20: JUMPI v2c1d(0x2c2a), v2c1c

    Begin block 0x2c21
    prev=[0x2c16], succ=[]
    =================================
    0x2c21: v2c21 = RETURNDATASIZE 
    0x2c22: v2c22(0x0) = CONST 
    0x2c25: RETURNDATACOPY v2c22(0x0), v2c22(0x0), v2c21
    0x2c26: v2c26 = RETURNDATASIZE 
    0x2c27: v2c27(0x0) = CONST 
    0x2c29: REVERT v2c27(0x0), v2c26

    Begin block 0x2c2a
    prev=[0x2c16], succ=[]
    =================================
    0x2c2d: v2c2d(0x40) = CONST 
    0x2c30: v2c30 = MLOAD v2c2d(0x40)
    0x2c33: MSTORE v2c30, v2acaarg0
    0x2c35: v2c35 = MLOAD v2c2d(0x40)
    0x2c36: v2c36(0x1) = CONST 
    0x2c38: v2c38(0xa0) = CONST 
    0x2c3a: v2c3a(0x2) = CONST 
    0x2c3c: v2c3c(0x10000000000000000000000000000000000000000) = EXP v2c3a(0x2), v2c38(0xa0)
    0x2c3d: v2c3d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c3c(0x10000000000000000000000000000000000000000), v2c36(0x1)
    0x2c3f: v2c3f = AND v2acaarg1, v2c3d(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c42: v2c42(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885) = CONST 
    0x2c68: v2c68(0x0) = SUB v2c30, v2c35
    0x2c69: v2c69(0x20) = CONST 
    0x2c6b: v2c6b(0x20) = ADD v2c69(0x20), v2c68(0x0)
    0x2c6d: LOG2 v2c35, v2c6b(0x20), v2c42(0xf6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885), v2c3f
    0x2c6e: v2c6e(0x40) = CONST 
    0x2c71: v2c71 = MLOAD v2c6e(0x40)
    0x2c74: MSTORE v2c71, v2acaarg0
    0x2c76: v2c76 = MLOAD v2c6e(0x40)
    0x2c77: v2c77(0x1) = CONST 
    0x2c79: v2c79(0xa0) = CONST 
    0x2c7b: v2c7b(0x2) = CONST 
    0x2c7d: v2c7d(0x10000000000000000000000000000000000000000) = EXP v2c7b(0x2), v2c79(0xa0)
    0x2c7e: v2c7e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c7d(0x10000000000000000000000000000000000000000), v2c77(0x1)
    0x2c80: v2c80 = AND v2acaarg1, v2c7e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c82: v2c82(0x0) = CONST 
    0x2c85: v2c85(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x2ca9: v2ca9(0x0) = SUB v2c71, v2c76
    0x2caa: v2caa(0x20) = CONST 
    0x2cac: v2cac(0x20) = ADD v2caa(0x20), v2ca9(0x0)
    0x2cae: LOG3 v2c76, v2cac(0x20), v2c85(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v2c82(0x0), v2c80
    0x2cb1: RETURNPRIVATE v2acaarg2

}

function cusdAddress()() public {
    Begin block 0x2b7
    prev=[], succ=[0x2bf, 0x2c3]
    =================================
    0x2b8: v2b8 = CALLVALUE 
    0x2ba: v2ba = ISZERO v2b8
    0x2bb: v2bb(0x2c3) = CONST 
    0x2be: JUMPI v2bb(0x2c3), v2ba

    Begin block 0x2bf
    prev=[0x2b7], succ=[]
    =================================
    0x2bf: v2bf(0x0) = CONST 
    0x2c2: REVERT v2bf(0x0), v2bf(0x0)

    Begin block 0x2c3
    prev=[0x2b7], succ=[0x1257]
    =================================
    0x2c5: v2c5(0x3176) = CONST 
    0x2c8: v2c8(0x1257) = CONST 
    0x2cb: JUMP v2c8(0x1257)

    Begin block 0x1257
    prev=[0x2c3], succ=[0x3176]
    =================================
    0x1258: v1258(0x4) = CONST 
    0x125a: v125a = SLOAD v1258(0x4)
    0x125b: v125b(0x1) = CONST 
    0x125d: v125d(0xa0) = CONST 
    0x125f: v125f(0x2) = CONST 
    0x1261: v1261(0x10000000000000000000000000000000000000000) = EXP v125f(0x2), v125d(0xa0)
    0x1262: v1262(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1261(0x10000000000000000000000000000000000000000), v125b(0x1)
    0x1263: v1263 = AND v1262(0xffffffffffffffffffffffffffffffffffffffff), v125a
    0x1265: JUMP v2c5(0x3176)

    Begin block 0x3176
    prev=[0x1257], succ=[]
    =================================
    0x3177: v3177(0x40) = CONST 
    0x317a: v317a = MLOAD v3177(0x40)
    0x317b: v317b(0x1) = CONST 
    0x317d: v317d(0xa0) = CONST 
    0x317f: v317f(0x2) = CONST 
    0x3181: v3181(0x10000000000000000000000000000000000000000) = EXP v317f(0x2), v317d(0xa0)
    0x3182: v3182(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3181(0x10000000000000000000000000000000000000000), v317b(0x1)
    0x3185: v3185 = AND v1263, v3182(0xffffffffffffffffffffffffffffffffffffffff)
    0x3187: MSTORE v317a, v3185
    0x3188: v3188 = MLOAD v3177(0x40)
    0x318c: v318c(0x0) = SUB v317a, v3188
    0x318d: v318d(0x20) = CONST 
    0x318f: v318f(0x20) = ADD v318d(0x20), v318c(0x0)
    0x3191: RETURN v3188, v318f(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x2e8
    prev=[], succ=[0x2f0, 0x2f4]
    =================================
    0x2e9: v2e9 = CALLVALUE 
    0x2eb: v2eb = ISZERO v2e9
    0x2ec: v2ec(0x2f4) = CONST 
    0x2ef: JUMPI v2ec(0x2f4), v2eb

    Begin block 0x2f0
    prev=[0x2e8], succ=[]
    =================================
    0x2f0: v2f0(0x0) = CONST 
    0x2f3: REVERT v2f0(0x0), v2f0(0x0)

    Begin block 0x2f4
    prev=[0x2e8], succ=[0x1266]
    =================================
    0x2f6: v2f6(0x31b1) = CONST 
    0x2f9: v2f9(0x1) = CONST 
    0x2fb: v2fb(0xa0) = CONST 
    0x2fd: v2fd(0x2) = CONST 
    0x2ff: v2ff(0x10000000000000000000000000000000000000000) = EXP v2fd(0x2), v2fb(0xa0)
    0x300: v300(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ff(0x10000000000000000000000000000000000000000), v2f9(0x1)
    0x301: v301(0x4) = CONST 
    0x303: v303 = CALLDATALOAD v301(0x4)
    0x304: v304 = AND v303, v300(0xffffffffffffffffffffffffffffffffffffffff)
    0x305: v305(0x24) = CONST 
    0x307: v307 = CALLDATALOAD v305(0x24)
    0x308: v308(0x1266) = CONST 
    0x30b: JUMP v308(0x1266)

    Begin block 0x1266
    prev=[0x2f4], succ=[0x12b5, 0x12b9]
    =================================
    0x1267: v1267(0x3) = CONST 
    0x1269: v1269 = SLOAD v1267(0x3)
    0x126a: v126a(0x40) = CONST 
    0x126d: v126d = MLOAD v126a(0x40)
    0x126e: v126e(0xe0) = CONST 
    0x1270: v1270(0x2) = CONST 
    0x1272: v1272(0x100000000000000000000000000000000000000000000000000000000) = EXP v1270(0x2), v126e(0xe0)
    0x1273: v1273(0x7ccce851) = CONST 
    0x1278: v1278(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1273(0x7ccce851), v1272(0x100000000000000000000000000000000000000000000000000000000)
    0x127a: MSTORE v126d, v1278(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x127b: v127b(0x1) = CONST 
    0x127d: v127d(0xa0) = CONST 
    0x127f: v127f(0x2) = CONST 
    0x1281: v1281(0x10000000000000000000000000000000000000000) = EXP v127f(0x2), v127d(0xa0)
    0x1282: v1282(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1281(0x10000000000000000000000000000000000000000), v127b(0x1)
    0x1285: v1285 = AND v304, v1282(0xffffffffffffffffffffffffffffffffffffffff)
    0x1286: v1286(0x4) = CONST 
    0x1289: v1289 = ADD v126d, v1286(0x4)
    0x128a: MSTORE v1289, v1285
    0x128c: v128c = MLOAD v126a(0x40)
    0x128d: v128d(0x0) = CONST 
    0x1292: v1292 = AND v1282(0xffffffffffffffffffffffffffffffffffffffff), v1269
    0x1294: v1294(0x7ccce851) = CONST 
    0x129a: v129a(0x24) = CONST 
    0x129e: v129e = ADD v126d, v129a(0x24)
    0x12a0: v12a0(0x20) = CONST 
    0x12a7: v12a7(0x0) = SUB v126d, v128c
    0x12a8: v12a8(0x24) = ADD v12a7(0x0), v129a(0x24)
    0x12ad: v12ad = EXTCODESIZE v1292
    0x12ae: v12ae = ISZERO v12ad
    0x12b0: v12b0 = ISZERO v12ae
    0x12b1: v12b1(0x12b9) = CONST 
    0x12b4: JUMPI v12b1(0x12b9), v12b0

    Begin block 0x12b5
    prev=[0x1266], succ=[]
    =================================
    0x12b5: v12b5(0x0) = CONST 
    0x12b8: REVERT v12b5(0x0), v12b5(0x0)

    Begin block 0x12b9
    prev=[0x1266], succ=[0x12c4, 0x12cd]
    =================================
    0x12bb: v12bb = GAS 
    0x12bc: v12bc = CALL v12bb, v1292, v128d(0x0), v128c, v12a8(0x24), v128c, v12a0(0x20)
    0x12bd: v12bd = ISZERO v12bc
    0x12bf: v12bf = ISZERO v12bd
    0x12c0: v12c0(0x12cd) = CONST 
    0x12c3: JUMPI v12c0(0x12cd), v12bf

    Begin block 0x12c4
    prev=[0x12b9], succ=[]
    =================================
    0x12c4: v12c4 = RETURNDATASIZE 
    0x12c5: v12c5(0x0) = CONST 
    0x12c8: RETURNDATACOPY v12c5(0x0), v12c5(0x0), v12c4
    0x12c9: v12c9 = RETURNDATASIZE 
    0x12ca: v12ca(0x0) = CONST 
    0x12cc: REVERT v12ca(0x0), v12c9

    Begin block 0x12cd
    prev=[0x12b9], succ=[0x12df, 0x12e3]
    =================================
    0x12d2: v12d2(0x40) = CONST 
    0x12d4: v12d4 = MLOAD v12d2(0x40)
    0x12d5: v12d5 = RETURNDATASIZE 
    0x12d6: v12d6(0x20) = CONST 
    0x12d9: v12d9 = LT v12d5, v12d6(0x20)
    0x12da: v12da = ISZERO v12d9
    0x12db: v12db(0x12e3) = CONST 
    0x12de: JUMPI v12db(0x12e3), v12da

    Begin block 0x12df
    prev=[0x12cd], succ=[]
    =================================
    0x12df: v12df(0x0) = CONST 
    0x12e2: REVERT v12df(0x0), v12df(0x0)

    Begin block 0x12e3
    prev=[0x12cd], succ=[0x12eb, 0x1328]
    =================================
    0x12e5: v12e5 = MLOAD v12d4
    0x12e6: v12e6 = ISZERO v12e5
    0x12e7: v12e7(0x1328) = CONST 
    0x12ea: JUMPI v12e7(0x1328), v12e6

    Begin block 0x12eb
    prev=[0x12e3], succ=[]
    =================================
    0x12eb: v12eb(0x40) = CONST 
    0x12ee: v12ee = MLOAD v12eb(0x40)
    0x12ef: v12ef(0xe5) = CONST 
    0x12f1: v12f1(0x2) = CONST 
    0x12f3: v12f3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v12f1(0x2), v12ef(0xe5)
    0x12f4: v12f4(0x461bcd) = CONST 
    0x12f8: v12f8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v12f4(0x461bcd), v12f3(0x2000000000000000000000000000000000000000000000000000000000)
    0x12fa: MSTORE v12ee, v12f8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12fb: v12fb(0x20) = CONST 
    0x12fd: v12fd(0x4) = CONST 
    0x1300: v1300 = ADD v12ee, v12fd(0x4)
    0x1301: MSTORE v1300, v12fb(0x20)
    0x1302: v1302(0x1c) = CONST 
    0x1304: v1304(0x24) = CONST 
    0x1307: v1307 = ADD v12ee, v1304(0x24)
    0x1308: MSTORE v1307, v1302(0x1c)
    0x1309: v1309(0x0) = CONST 
    0x130c: v130c = MLOAD v1309(0x0)
    0x130d: v130d(0x20) = CONST 
    0x130f: v130f(0x2f6a) = CONST 
    0x1317: MSTORE v1309(0x0), v130c
    0x1318: v1318(0x44) = CONST 
    0x131b: v131b = ADD v12ee, v1318(0x44)
    0x131c: MSTORE v131b, v3667(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x131e: v131e = MLOAD v12eb(0x40)
    0x1322: v1322(0x0) = SUB v12ee, v131e
    0x1323: v1323(0x64) = CONST 
    0x1325: v1325(0x64) = ADD v1323(0x64), v1322(0x0)
    0x1327: REVERT v131e, v1325(0x64)
    0x3667: v3667(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x1328
    prev=[0x12e3], succ=[0x1376, 0x137a]
    =================================
    0x1329: v1329(0x3) = CONST 
    0x132b: v132b = SLOAD v1329(0x3)
    0x132c: v132c(0x40) = CONST 
    0x132f: v132f = MLOAD v132c(0x40)
    0x1330: v1330(0xe0) = CONST 
    0x1332: v1332(0x2) = CONST 
    0x1334: v1334(0x100000000000000000000000000000000000000000000000000000000) = EXP v1332(0x2), v1330(0xe0)
    0x1335: v1335(0x7ccce851) = CONST 
    0x133a: v133a(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1335(0x7ccce851), v1334(0x100000000000000000000000000000000000000000000000000000000)
    0x133c: MSTORE v132f, v133a(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x133d: v133d = CALLER 
    0x133e: v133e(0x4) = CONST 
    0x1341: v1341 = ADD v132f, v133e(0x4)
    0x1344: MSTORE v1341, v133d
    0x1346: v1346 = MLOAD v132c(0x40)
    0x1349: v1349(0x1) = CONST 
    0x134b: v134b(0xa0) = CONST 
    0x134d: v134d(0x2) = CONST 
    0x134f: v134f(0x10000000000000000000000000000000000000000) = EXP v134d(0x2), v134b(0xa0)
    0x1350: v1350(0xffffffffffffffffffffffffffffffffffffffff) = SUB v134f(0x10000000000000000000000000000000000000000), v1349(0x1)
    0x1351: v1351 = AND v1350(0xffffffffffffffffffffffffffffffffffffffff), v132b
    0x1353: v1353(0x7ccce851) = CONST 
    0x1359: v1359(0x24) = CONST 
    0x135d: v135d = ADD v132f, v1359(0x24)
    0x135f: v135f(0x20) = CONST 
    0x1367: v1367(0x0) = SUB v132f, v1346
    0x1368: v1368(0x24) = ADD v1367(0x0), v1359(0x24)
    0x136a: v136a(0x0) = CONST 
    0x136e: v136e = EXTCODESIZE v1351
    0x136f: v136f = ISZERO v136e
    0x1371: v1371 = ISZERO v136f
    0x1372: v1372(0x137a) = CONST 
    0x1375: JUMPI v1372(0x137a), v1371

    Begin block 0x1376
    prev=[0x1328], succ=[]
    =================================
    0x1376: v1376(0x0) = CONST 
    0x1379: REVERT v1376(0x0), v1376(0x0)

    Begin block 0x137a
    prev=[0x1328], succ=[0x1385, 0x138e]
    =================================
    0x137c: v137c = GAS 
    0x137d: v137d = CALL v137c, v1351, v136a(0x0), v1346, v1368(0x24), v1346, v135f(0x20)
    0x137e: v137e = ISZERO v137d
    0x1380: v1380 = ISZERO v137e
    0x1381: v1381(0x138e) = CONST 
    0x1384: JUMPI v1381(0x138e), v1380

    Begin block 0x1385
    prev=[0x137a], succ=[]
    =================================
    0x1385: v1385 = RETURNDATASIZE 
    0x1386: v1386(0x0) = CONST 
    0x1389: RETURNDATACOPY v1386(0x0), v1386(0x0), v1385
    0x138a: v138a = RETURNDATASIZE 
    0x138b: v138b(0x0) = CONST 
    0x138d: REVERT v138b(0x0), v138a

    Begin block 0x138e
    prev=[0x137a], succ=[0x13a0, 0x13a4]
    =================================
    0x1393: v1393(0x40) = CONST 
    0x1395: v1395 = MLOAD v1393(0x40)
    0x1396: v1396 = RETURNDATASIZE 
    0x1397: v1397(0x20) = CONST 
    0x139a: v139a = LT v1396, v1397(0x20)
    0x139b: v139b = ISZERO v139a
    0x139c: v139c(0x13a4) = CONST 
    0x139f: JUMPI v139c(0x13a4), v139b

    Begin block 0x13a0
    prev=[0x138e], succ=[]
    =================================
    0x13a0: v13a0(0x0) = CONST 
    0x13a3: REVERT v13a0(0x0), v13a0(0x0)

    Begin block 0x13a4
    prev=[0x138e], succ=[0x13ac, 0x13e9]
    =================================
    0x13a6: v13a6 = MLOAD v1395
    0x13a7: v13a7 = ISZERO v13a6
    0x13a8: v13a8(0x13e9) = CONST 
    0x13ab: JUMPI v13a8(0x13e9), v13a7

    Begin block 0x13ac
    prev=[0x13a4], succ=[]
    =================================
    0x13ac: v13ac(0x40) = CONST 
    0x13af: v13af = MLOAD v13ac(0x40)
    0x13b0: v13b0(0xe5) = CONST 
    0x13b2: v13b2(0x2) = CONST 
    0x13b4: v13b4(0x2000000000000000000000000000000000000000000000000000000000) = EXP v13b2(0x2), v13b0(0xe5)
    0x13b5: v13b5(0x461bcd) = CONST 
    0x13b9: v13b9(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v13b5(0x461bcd), v13b4(0x2000000000000000000000000000000000000000000000000000000000)
    0x13bb: MSTORE v13af, v13b9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13bc: v13bc(0x20) = CONST 
    0x13be: v13be(0x4) = CONST 
    0x13c1: v13c1 = ADD v13af, v13be(0x4)
    0x13c2: MSTORE v13c1, v13bc(0x20)
    0x13c3: v13c3(0x1c) = CONST 
    0x13c5: v13c5(0x24) = CONST 
    0x13c8: v13c8 = ADD v13af, v13c5(0x24)
    0x13c9: MSTORE v13c8, v13c3(0x1c)
    0x13ca: v13ca(0x0) = CONST 
    0x13cd: v13cd = MLOAD v13ca(0x0)
    0x13ce: v13ce(0x20) = CONST 
    0x13d0: v13d0(0x2f6a) = CONST 
    0x13d8: MSTORE v13ca(0x0), v13cd
    0x13d9: v13d9(0x44) = CONST 
    0x13dc: v13dc = ADD v13af, v13d9(0x44)
    0x13dd: MSTORE v13dc, v366c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x13df: v13df = MLOAD v13ac(0x40)
    0x13e3: v13e3(0x0) = SUB v13af, v13df
    0x13e4: v13e4(0x64) = CONST 
    0x13e6: v13e6(0x64) = ADD v13e4(0x64), v13e3(0x0)
    0x13e8: REVERT v13df, v13e6(0x64)
    0x366c: v366c(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x13e9
    prev=[0x13a4], succ=[0x13fc, 0x1400]
    =================================
    0x13ea: v13ea(0x1) = CONST 
    0x13ec: v13ec = SLOAD v13ea(0x1)
    0x13ed: v13ed(0xa0) = CONST 
    0x13ef: v13ef(0x2) = CONST 
    0x13f1: v13f1(0x10000000000000000000000000000000000000000) = EXP v13ef(0x2), v13ed(0xa0)
    0x13f3: v13f3 = DIV v13ec, v13f1(0x10000000000000000000000000000000000000000)
    0x13f4: v13f4(0xff) = CONST 
    0x13f6: v13f6 = AND v13f4(0xff), v13f3
    0x13f7: v13f7 = ISZERO v13f6
    0x13f8: v13f8(0x1400) = CONST 
    0x13fb: JUMPI v13f8(0x1400), v13f7

    Begin block 0x13fc
    prev=[0x13e9], succ=[]
    =================================
    0x13fc: v13fc(0x0) = CONST 
    0x13ff: REVERT v13fc(0x0), v13fc(0x0)

    Begin block 0x1400
    prev=[0x13e9], succ=[0x2cb2]
    =================================
    0x1401: v1401(0x3518) = CONST 
    0x1406: v1406 = CALLER 
    0x1407: v1407(0x2cb2) = CONST 
    0x140a: JUMP v1407(0x2cb2)

    Begin block 0x2cb2
    prev=[0x1400], succ=[0x2cbe]
    =================================
    0x2cb3: v2cb3(0x0) = CONST 
    0x2cb5: v2cb5(0x2cbe) = CONST 
    0x2cba: v2cba(0x237f) = CONST 
    0x2cbd: v2cbd_0 = CALLPRIVATE v2cba(0x237f), v304, v1406, v2cb5(0x2cbe)

    Begin block 0x2cbe
    prev=[0x2cb2], succ=[0x2cc9, 0x2d59]
    =================================
    0x2cc3: v2cc3 = GT v307, v2cbd_0
    0x2cc4: v2cc4 = ISZERO v2cc3
    0x2cc5: v2cc5(0x2d59) = CONST 
    0x2cc8: JUMPI v2cc5(0x2d59), v2cc4

    Begin block 0x2cc9
    prev=[0x2cbe], succ=[0x2d38, 0x2d3c]
    =================================
    0x2cc9: v2cc9(0x2) = CONST 
    0x2ccb: v2ccb = SLOAD v2cc9(0x2)
    0x2ccc: v2ccc(0x40) = CONST 
    0x2ccf: v2ccf = MLOAD v2ccc(0x40)
    0x2cd0: v2cd0(0xda46098c00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2cf2: MSTORE v2ccf, v2cd0(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0x2cf3: v2cf3(0x1) = CONST 
    0x2cf5: v2cf5(0xa0) = CONST 
    0x2cf7: v2cf7(0x2) = CONST 
    0x2cf9: v2cf9(0x10000000000000000000000000000000000000000) = EXP v2cf7(0x2), v2cf5(0xa0)
    0x2cfa: v2cfa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2cf9(0x10000000000000000000000000000000000000000), v2cf3(0x1)
    0x2cfd: v2cfd = AND v2cfa(0xffffffffffffffffffffffffffffffffffffffff), v1406
    0x2cfe: v2cfe(0x4) = CONST 
    0x2d01: v2d01 = ADD v2ccf, v2cfe(0x4)
    0x2d02: MSTORE v2d01, v2cfd
    0x2d05: v2d05 = AND v2cfa(0xffffffffffffffffffffffffffffffffffffffff), v304
    0x2d06: v2d06(0x24) = CONST 
    0x2d09: v2d09 = ADD v2ccf, v2d06(0x24)
    0x2d0a: MSTORE v2d09, v2d05
    0x2d0b: v2d0b(0x0) = CONST 
    0x2d0d: v2d0d(0x44) = CONST 
    0x2d10: v2d10 = ADD v2ccf, v2d0d(0x44)
    0x2d13: MSTORE v2d10, v2d0b(0x0)
    0x2d15: v2d15 = MLOAD v2ccc(0x40)
    0x2d17: v2d17 = AND v2ccb, v2cfa(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d19: v2d19(0xda46098c) = CONST 
    0x2d1f: v2d1f(0x64) = CONST 
    0x2d23: v2d23 = ADD v2ccf, v2d1f(0x64)
    0x2d2a: v2d2a(0x0) = SUB v2ccf, v2d15
    0x2d2b: v2d2b(0x64) = ADD v2d2a(0x0), v2d1f(0x64)
    0x2d30: v2d30 = EXTCODESIZE v2d17
    0x2d31: v2d31 = ISZERO v2d30
    0x2d33: v2d33 = ISZERO v2d31
    0x2d34: v2d34(0x2d3c) = CONST 
    0x2d37: JUMPI v2d34(0x2d3c), v2d33

    Begin block 0x2d38
    prev=[0x2cc9], succ=[]
    =================================
    0x2d38: v2d38(0x0) = CONST 
    0x2d3b: REVERT v2d38(0x0), v2d38(0x0)

    Begin block 0x2d3c
    prev=[0x2cc9], succ=[0x2d47, 0x2d50]
    =================================
    0x2d3e: v2d3e = GAS 
    0x2d3f: v2d3f = CALL v2d3e, v2d17, v2d0b(0x0), v2d15, v2d2b(0x64), v2d15, v2d0b(0x0)
    0x2d40: v2d40 = ISZERO v2d3f
    0x2d42: v2d42 = ISZERO v2d40
    0x2d43: v2d43(0x2d50) = CONST 
    0x2d46: JUMPI v2d43(0x2d50), v2d42

    Begin block 0x2d47
    prev=[0x2d3c], succ=[]
    =================================
    0x2d47: v2d47 = RETURNDATASIZE 
    0x2d48: v2d48(0x0) = CONST 
    0x2d4b: RETURNDATACOPY v2d48(0x0), v2d48(0x0), v2d47
    0x2d4c: v2d4c = RETURNDATASIZE 
    0x2d4d: v2d4d(0x0) = CONST 
    0x2d4f: REVERT v2d4d(0x0), v2d4c

    Begin block 0x2d50
    prev=[0x2d3c], succ=[0x2de8]
    =================================
    0x2d55: v2d55(0x2de8) = CONST 
    0x2d58: JUMP v2d55(0x2de8)

    Begin block 0x2de8
    prev=[0x2d50, 0x2de3], succ=[0x2e27]
    =================================
    0x2dea: v2dea(0x1) = CONST 
    0x2dec: v2dec(0xa0) = CONST 
    0x2dee: v2dee(0x2) = CONST 
    0x2df0: v2df0(0x10000000000000000000000000000000000000000) = EXP v2dee(0x2), v2dec(0xa0)
    0x2df1: v2df1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2df0(0x10000000000000000000000000000000000000000), v2dea(0x1)
    0x2df2: v2df2 = AND v2df1(0xffffffffffffffffffffffffffffffffffffffff), v304
    0x2df4: v2df4(0x1) = CONST 
    0x2df6: v2df6(0xa0) = CONST 
    0x2df8: v2df8(0x2) = CONST 
    0x2dfa: v2dfa(0x10000000000000000000000000000000000000000) = EXP v2df8(0x2), v2df6(0xa0)
    0x2dfb: v2dfb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2dfa(0x10000000000000000000000000000000000000000), v2df4(0x1)
    0x2dfc: v2dfc = AND v2dfb(0xffffffffffffffffffffffffffffffffffffffff), v1406
    0x2dfd: v2dfd(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x2e1e: v2e1e(0x2e27) = CONST 
    0x2e23: v2e23(0x237f) = CONST 
    0x2e26: v2e26_0 = CALLPRIVATE v2e23(0x237f), v304, v1406, v2e1e(0x2e27)

    Begin block 0x2e27
    prev=[0x2de8], succ=[0x3518]
    =================================
    0x2e28: v2e28(0x40) = CONST 
    0x2e2b: v2e2b = MLOAD v2e28(0x40)
    0x2e2e: MSTORE v2e2b, v2e26_0
    0x2e2f: v2e2f = MLOAD v2e28(0x40)
    0x2e33: v2e33(0x0) = SUB v2e2b, v2e2f
    0x2e34: v2e34(0x20) = CONST 
    0x2e36: v2e36(0x20) = ADD v2e34(0x20), v2e33(0x0)
    0x2e38: LOG3 v2e2f, v2e36(0x20), v2dfd(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v2dfc, v2df2
    0x2e3d: JUMP v1401(0x3518)

    Begin block 0x3518
    prev=[0x2e27], succ=[0x31b1]
    =================================
    0x351a: v351a(0x1) = CONST 
    0x3522: JUMP v2f6(0x31b1)

    Begin block 0x31b1
    prev=[0x3518], succ=[]
    =================================
    0x31b2: v31b2(0x40) = CONST 
    0x31b5: v31b5 = MLOAD v31b2(0x40)
    0x31b7: v31b7 = ISZERO v351a(0x1)
    0x31b8: v31b8 = ISZERO v31b7
    0x31ba: MSTORE v31b5, v31b8
    0x31bb: v31bb = MLOAD v31b2(0x40)
    0x31bf: v31bf(0x0) = SUB v31b5, v31bb
    0x31c0: v31c0(0x20) = CONST 
    0x31c2: v31c2(0x20) = ADD v31c0(0x20), v31bf(0x0)
    0x31c4: RETURN v31bb, v31c2(0x20)

    Begin block 0x2d59
    prev=[0x2cbe], succ=[0x2dcb, 0x2dcf]
    =================================
    0x2d5a: v2d5a(0x2) = CONST 
    0x2d5c: v2d5c = SLOAD v2d5a(0x2)
    0x2d5d: v2d5d(0x40) = CONST 
    0x2d60: v2d60 = MLOAD v2d5d(0x40)
    0x2d61: v2d61(0x97d88cd200000000000000000000000000000000000000000000000000000000) = CONST 
    0x2d83: MSTORE v2d60, v2d61(0x97d88cd200000000000000000000000000000000000000000000000000000000)
    0x2d84: v2d84(0x1) = CONST 
    0x2d86: v2d86(0xa0) = CONST 
    0x2d88: v2d88(0x2) = CONST 
    0x2d8a: v2d8a(0x10000000000000000000000000000000000000000) = EXP v2d88(0x2), v2d86(0xa0)
    0x2d8b: v2d8b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d8a(0x10000000000000000000000000000000000000000), v2d84(0x1)
    0x2d8e: v2d8e = AND v2d8b(0xffffffffffffffffffffffffffffffffffffffff), v1406
    0x2d8f: v2d8f(0x4) = CONST 
    0x2d92: v2d92 = ADD v2d60, v2d8f(0x4)
    0x2d93: MSTORE v2d92, v2d8e
    0x2d96: v2d96 = AND v2d8b(0xffffffffffffffffffffffffffffffffffffffff), v304
    0x2d97: v2d97(0x24) = CONST 
    0x2d9a: v2d9a = ADD v2d60, v2d97(0x24)
    0x2d9b: MSTORE v2d9a, v2d96
    0x2d9c: v2d9c(0x44) = CONST 
    0x2d9f: v2d9f = ADD v2d60, v2d9c(0x44)
    0x2da2: MSTORE v2d9f, v307
    0x2da4: v2da4 = MLOAD v2d5d(0x40)
    0x2da8: v2da8 = AND v2d5c, v2d8b(0xffffffffffffffffffffffffffffffffffffffff)
    0x2daa: v2daa(0x97d88cd2) = CONST 
    0x2db0: v2db0(0x64) = CONST 
    0x2db4: v2db4 = ADD v2d60, v2db0(0x64)
    0x2db6: v2db6(0x0) = CONST 
    0x2dbd: v2dbd(0x0) = SUB v2d60, v2da4
    0x2dbe: v2dbe(0x64) = ADD v2dbd(0x0), v2db0(0x64)
    0x2dc3: v2dc3 = EXTCODESIZE v2da8
    0x2dc4: v2dc4 = ISZERO v2dc3
    0x2dc6: v2dc6 = ISZERO v2dc4
    0x2dc7: v2dc7(0x2dcf) = CONST 
    0x2dca: JUMPI v2dc7(0x2dcf), v2dc6

    Begin block 0x2dcb
    prev=[0x2d59], succ=[]
    =================================
    0x2dcb: v2dcb(0x0) = CONST 
    0x2dce: REVERT v2dcb(0x0), v2dcb(0x0)

    Begin block 0x2dcf
    prev=[0x2d59], succ=[0x2dda, 0x2de3]
    =================================
    0x2dd1: v2dd1 = GAS 
    0x2dd2: v2dd2 = CALL v2dd1, v2da8, v2db6(0x0), v2da4, v2dbe(0x64), v2da4, v2db6(0x0)
    0x2dd3: v2dd3 = ISZERO v2dd2
    0x2dd5: v2dd5 = ISZERO v2dd3
    0x2dd6: v2dd6(0x2de3) = CONST 
    0x2dd9: JUMPI v2dd6(0x2de3), v2dd5

    Begin block 0x2dda
    prev=[0x2dcf], succ=[]
    =================================
    0x2dda: v2dda = RETURNDATASIZE 
    0x2ddb: v2ddb(0x0) = CONST 
    0x2dde: RETURNDATACOPY v2ddb(0x0), v2ddb(0x0), v2dda
    0x2ddf: v2ddf = RETURNDATASIZE 
    0x2de0: v2de0(0x0) = CONST 
    0x2de2: REVERT v2de0(0x0), v2ddf

    Begin block 0x2de3
    prev=[0x2dcf], succ=[0x2de8]
    =================================

}

function approveBlacklistedAddressSpender(address)() public {
    Begin block 0x30c
    prev=[], succ=[0x314, 0x318]
    =================================
    0x30d: v30d = CALLVALUE 
    0x30f: v30f = ISZERO v30d
    0x310: v310(0x318) = CONST 
    0x313: JUMPI v310(0x318), v30f

    Begin block 0x314
    prev=[0x30c], succ=[]
    =================================
    0x314: v314(0x0) = CONST 
    0x317: REVERT v314(0x0), v314(0x0)

    Begin block 0x318
    prev=[0x30c], succ=[0x1416]
    =================================
    0x31a: v31a(0x31e4) = CONST 
    0x31d: v31d(0x1) = CONST 
    0x31f: v31f(0xa0) = CONST 
    0x321: v321(0x2) = CONST 
    0x323: v323(0x10000000000000000000000000000000000000000) = EXP v321(0x2), v31f(0xa0)
    0x324: v324(0xffffffffffffffffffffffffffffffffffffffff) = SUB v323(0x10000000000000000000000000000000000000000), v31d(0x1)
    0x325: v325(0x4) = CONST 
    0x327: v327 = CALLDATALOAD v325(0x4)
    0x328: v328 = AND v327, v324(0xffffffffffffffffffffffffffffffffffffffff)
    0x329: v329(0x1416) = CONST 
    0x32c: JUMP v329(0x1416)

    Begin block 0x1416
    prev=[0x318], succ=[0x1467, 0x146b]
    =================================
    0x1417: v1417(0x3) = CONST 
    0x1419: v1419 = SLOAD v1417(0x3)
    0x141a: v141a(0x40) = CONST 
    0x141d: v141d = MLOAD v141a(0x40)
    0x141e: v141e(0xe0) = CONST 
    0x1420: v1420(0x2) = CONST 
    0x1422: v1422(0x100000000000000000000000000000000000000000000000000000000) = EXP v1420(0x2), v141e(0xe0)
    0x1423: v1423(0x7ccce851) = CONST 
    0x1428: v1428(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1423(0x7ccce851), v1422(0x100000000000000000000000000000000000000000000000000000000)
    0x142a: MSTORE v141d, v1428(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x142b: v142b(0x1) = CONST 
    0x142d: v142d(0xa0) = CONST 
    0x142f: v142f(0x2) = CONST 
    0x1431: v1431(0x10000000000000000000000000000000000000000) = EXP v142f(0x2), v142d(0xa0)
    0x1432: v1432(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1431(0x10000000000000000000000000000000000000000), v142b(0x1)
    0x1435: v1435 = AND v328, v1432(0xffffffffffffffffffffffffffffffffffffffff)
    0x1436: v1436(0x4) = CONST 
    0x1439: v1439 = ADD v141d, v1436(0x4)
    0x143a: MSTORE v1439, v1435
    0x143c: v143c = MLOAD v141a(0x40)
    0x1442: v1442 = AND v1419, v1432(0xffffffffffffffffffffffffffffffffffffffff)
    0x1444: v1444(0x7ccce851) = CONST 
    0x144a: v144a(0x24) = CONST 
    0x144e: v144e = ADD v141d, v144a(0x24)
    0x1450: v1450(0x20) = CONST 
    0x1458: v1458(0x0) = SUB v141d, v143c
    0x1459: v1459(0x24) = ADD v1458(0x0), v144a(0x24)
    0x145b: v145b(0x0) = CONST 
    0x145f: v145f = EXTCODESIZE v1442
    0x1460: v1460 = ISZERO v145f
    0x1462: v1462 = ISZERO v1460
    0x1463: v1463(0x146b) = CONST 
    0x1466: JUMPI v1463(0x146b), v1462

    Begin block 0x1467
    prev=[0x1416], succ=[]
    =================================
    0x1467: v1467(0x0) = CONST 
    0x146a: REVERT v1467(0x0), v1467(0x0)

    Begin block 0x146b
    prev=[0x1416], succ=[0x1476, 0x147f]
    =================================
    0x146d: v146d = GAS 
    0x146e: v146e = CALL v146d, v1442, v145b(0x0), v143c, v1459(0x24), v143c, v1450(0x20)
    0x146f: v146f = ISZERO v146e
    0x1471: v1471 = ISZERO v146f
    0x1472: v1472(0x147f) = CONST 
    0x1475: JUMPI v1472(0x147f), v1471

    Begin block 0x1476
    prev=[0x146b], succ=[]
    =================================
    0x1476: v1476 = RETURNDATASIZE 
    0x1477: v1477(0x0) = CONST 
    0x147a: RETURNDATACOPY v1477(0x0), v1477(0x0), v1476
    0x147b: v147b = RETURNDATASIZE 
    0x147c: v147c(0x0) = CONST 
    0x147e: REVERT v147c(0x0), v147b

    Begin block 0x147f
    prev=[0x146b], succ=[0x1491, 0x1495]
    =================================
    0x1484: v1484(0x40) = CONST 
    0x1486: v1486 = MLOAD v1484(0x40)
    0x1487: v1487 = RETURNDATASIZE 
    0x1488: v1488(0x20) = CONST 
    0x148b: v148b = LT v1487, v1488(0x20)
    0x148c: v148c = ISZERO v148b
    0x148d: v148d(0x1495) = CONST 
    0x1490: JUMPI v148d(0x1495), v148c

    Begin block 0x1491
    prev=[0x147f], succ=[]
    =================================
    0x1491: v1491(0x0) = CONST 
    0x1494: REVERT v1491(0x0), v1491(0x0)

    Begin block 0x1495
    prev=[0x147f], succ=[0x149e, 0x14ed]
    =================================
    0x1497: v1497 = MLOAD v1486
    0x1498: v1498 = ISZERO v1497
    0x1499: v1499 = ISZERO v1498
    0x149a: v149a(0x14ed) = CONST 
    0x149d: JUMPI v149a(0x14ed), v1499

    Begin block 0x149e
    prev=[0x1495], succ=[]
    =================================
    0x149e: v149e(0x40) = CONST 
    0x14a1: v14a1 = MLOAD v149e(0x40)
    0x14a2: v14a2(0xe5) = CONST 
    0x14a4: v14a4(0x2) = CONST 
    0x14a6: v14a6(0x2000000000000000000000000000000000000000000000000000000000) = EXP v14a4(0x2), v14a2(0xe5)
    0x14a7: v14a7(0x461bcd) = CONST 
    0x14ab: v14ab(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v14a7(0x461bcd), v14a6(0x2000000000000000000000000000000000000000000000000000000000)
    0x14ad: MSTORE v14a1, v14ab(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14ae: v14ae(0x20) = CONST 
    0x14b0: v14b0(0x4) = CONST 
    0x14b3: v14b3 = ADD v14a1, v14b0(0x4)
    0x14b4: MSTORE v14b3, v14ae(0x20)
    0x14b5: v14b5(0x18) = CONST 
    0x14b7: v14b7(0x24) = CONST 
    0x14ba: v14ba = ADD v14a1, v14b7(0x24)
    0x14bb: MSTORE v14ba, v14b5(0x18)
    0x14bc: v14bc(0x55736572206d75737420626520626c61636b6c69737465640000000000000000) = CONST 
    0x14dd: v14dd(0x44) = CONST 
    0x14e0: v14e0 = ADD v14a1, v14dd(0x44)
    0x14e1: MSTORE v14e0, v14bc(0x55736572206d75737420626520626c61636b6c69737465640000000000000000)
    0x14e3: v14e3 = MLOAD v149e(0x40)
    0x14e7: v14e7(0x0) = SUB v14a1, v14e3
    0x14e8: v14e8(0x64) = CONST 
    0x14ea: v14ea(0x64) = ADD v14e8(0x64), v14e7(0x0)
    0x14ec: REVERT v14e3, v14ea(0x64)

    Begin block 0x14ed
    prev=[0x1495], succ=[0x1500, 0x1504]
    =================================
    0x14ee: v14ee(0x1) = CONST 
    0x14f0: v14f0 = SLOAD v14ee(0x1)
    0x14f1: v14f1(0xa0) = CONST 
    0x14f3: v14f3(0x2) = CONST 
    0x14f5: v14f5(0x10000000000000000000000000000000000000000) = EXP v14f3(0x2), v14f1(0xa0)
    0x14f7: v14f7 = DIV v14f0, v14f5(0x10000000000000000000000000000000000000000)
    0x14f8: v14f8(0xff) = CONST 
    0x14fa: v14fa = AND v14f8(0xff), v14f7
    0x14fb: v14fb = ISZERO v14fa
    0x14fc: v14fc(0x1504) = CONST 
    0x14ff: JUMPI v14fc(0x1504), v14fb

    Begin block 0x1500
    prev=[0x14ed], succ=[]
    =================================
    0x1500: v1500(0x0) = CONST 
    0x1503: REVERT v1500(0x0), v1500(0x0)

    Begin block 0x1504
    prev=[0x14ed], succ=[0x1564, 0x1568]
    =================================
    0x1505: v1505(0x3) = CONST 
    0x1507: v1507 = SLOAD v1505(0x3)
    0x1508: v1508(0x40) = CONST 
    0x150b: v150b = MLOAD v1508(0x40)
    0x150c: v150c(0xe3) = CONST 
    0x150e: v150e(0x2) = CONST 
    0x1510: v1510(0x800000000000000000000000000000000000000000000000000000000) = EXP v150e(0x2), v150c(0xe3)
    0x1511: v1511(0x29b6dab) = CONST 
    0x1516: v1516(0x14db6d5800000000000000000000000000000000000000000000000000000000) = MUL v1511(0x29b6dab), v1510(0x800000000000000000000000000000000000000000000000000000000)
    0x1518: MSTORE v150b, v1516(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1519: v1519 = CALLER 
    0x151a: v151a(0x4) = CONST 
    0x151d: v151d = ADD v150b, v151a(0x4)
    0x151e: MSTORE v151d, v1519
    0x151f: v151f(0x0) = CONST 
    0x1522: v1522 = CALLDATALOAD v151f(0x0)
    0x1523: v1523(0x1) = CONST 
    0x1525: v1525(0xe0) = CONST 
    0x1527: v1527(0x2) = CONST 
    0x1529: v1529(0x100000000000000000000000000000000000000000000000000000000) = EXP v1527(0x2), v1525(0xe0)
    0x152a: v152a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1529(0x100000000000000000000000000000000000000000000000000000000), v1523(0x1)
    0x152b: v152b(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v152a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x152c: v152c = AND v152b(0xffffffff00000000000000000000000000000000000000000000000000000000), v1522
    0x152d: v152d(0x24) = CONST 
    0x1530: v1530 = ADD v150b, v152d(0x24)
    0x1531: MSTORE v1530, v152c
    0x1533: v1533 = MLOAD v1508(0x40)
    0x1534: v1534(0x1) = CONST 
    0x1536: v1536(0xa0) = CONST 
    0x1538: v1538(0x2) = CONST 
    0x153a: v153a(0x10000000000000000000000000000000000000000) = EXP v1538(0x2), v1536(0xa0)
    0x153b: v153b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v153a(0x10000000000000000000000000000000000000000), v1534(0x1)
    0x153e: v153e = AND v1507, v153b(0xffffffffffffffffffffffffffffffffffffffff)
    0x1540: v1540(0x14db6d58) = CONST 
    0x1546: v1546(0x44) = CONST 
    0x154a: v154a = ADD v150b, v1546(0x44)
    0x154c: v154c(0x20) = CONST 
    0x1553: v1553(0x0) = SUB v150b, v1533
    0x1556: v1556(0x44) = ADD v1546(0x44), v1553(0x0)
    0x155c: v155c = EXTCODESIZE v153e
    0x155d: v155d = ISZERO v155c
    0x155f: v155f = ISZERO v155d
    0x1560: v1560(0x1568) = CONST 
    0x1563: JUMPI v1560(0x1568), v155f

    Begin block 0x1564
    prev=[0x1504], succ=[]
    =================================
    0x1564: v1564(0x0) = CONST 
    0x1567: REVERT v1564(0x0), v1564(0x0)

    Begin block 0x1568
    prev=[0x1504], succ=[0x1573, 0x157c]
    =================================
    0x156a: v156a = GAS 
    0x156b: v156b = CALL v156a, v153e, v151f(0x0), v1533, v1556(0x44), v1533, v154c(0x20)
    0x156c: v156c = ISZERO v156b
    0x156e: v156e = ISZERO v156c
    0x156f: v156f(0x157c) = CONST 
    0x1572: JUMPI v156f(0x157c), v156e

    Begin block 0x1573
    prev=[0x1568], succ=[]
    =================================
    0x1573: v1573 = RETURNDATASIZE 
    0x1574: v1574(0x0) = CONST 
    0x1577: RETURNDATACOPY v1574(0x0), v1574(0x0), v1573
    0x1578: v1578 = RETURNDATASIZE 
    0x1579: v1579(0x0) = CONST 
    0x157b: REVERT v1579(0x0), v1578

    Begin block 0x157c
    prev=[0x1568], succ=[0x158e, 0x1592]
    =================================
    0x1581: v1581(0x40) = CONST 
    0x1583: v1583 = MLOAD v1581(0x40)
    0x1584: v1584 = RETURNDATASIZE 
    0x1585: v1585(0x20) = CONST 
    0x1588: v1588 = LT v1584, v1585(0x20)
    0x1589: v1589 = ISZERO v1588
    0x158a: v158a(0x1592) = CONST 
    0x158d: JUMPI v158a(0x1592), v1589

    Begin block 0x158e
    prev=[0x157c], succ=[]
    =================================
    0x158e: v158e(0x0) = CONST 
    0x1591: REVERT v158e(0x0), v158e(0x0)

    Begin block 0x1592
    prev=[0x157c], succ=[0x159b, 0x15ec]
    =================================
    0x1594: v1594 = MLOAD v1583
    0x1595: v1595 = ISZERO v1594
    0x1596: v1596 = ISZERO v1595
    0x1597: v1597(0x15ec) = CONST 
    0x159a: JUMPI v1597(0x15ec), v1596

    Begin block 0x159b
    prev=[0x1592], succ=[]
    =================================
    0x159b: v159b(0x40) = CONST 
    0x159e: v159e = MLOAD v159b(0x40)
    0x159f: v159f(0xe5) = CONST 
    0x15a1: v15a1(0x2) = CONST 
    0x15a3: v15a3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v15a1(0x2), v159f(0xe5)
    0x15a4: v15a4(0x461bcd) = CONST 
    0x15a8: v15a8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v15a4(0x461bcd), v15a3(0x2000000000000000000000000000000000000000000000000000000000)
    0x15aa: MSTORE v159e, v15a8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15ab: v15ab(0x20) = CONST 
    0x15ad: v15ad(0x4) = CONST 
    0x15b0: v15b0 = ADD v159e, v15ad(0x4)
    0x15b1: MSTORE v15b0, v15ab(0x20)
    0x15b2: v15b2(0x31) = CONST 
    0x15b4: v15b4(0x24) = CONST 
    0x15b7: v15b7 = ADD v159e, v15b4(0x24)
    0x15b8: MSTORE v15b7, v15b2(0x31)
    0x15b9: v15b9(0x0) = CONST 
    0x15bc: v15bc = MLOAD v15b9(0x0)
    0x15bd: v15bd(0x20) = CONST 
    0x15bf: v15bf(0x2f4a) = CONST 
    0x15c7: MSTORE v15b9(0x0), v15bc
    0x15c8: v15c8(0x44) = CONST 
    0x15cb: v15cb = ADD v159e, v15c8(0x44)
    0x15cc: MSTORE v15cb, v3671(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x15cd: v15cd(0x0) = CONST 
    0x15d0: v15d0 = MLOAD v15cd(0x0)
    0x15d1: v15d1(0x20) = CONST 
    0x15d3: v15d3(0x2f2a) = CONST 
    0x15db: MSTORE v15cd(0x0), v15d0
    0x15dc: v15dc(0x64) = CONST 
    0x15df: v15df = ADD v159e, v15dc(0x64)
    0x15e0: MSTORE v15df, v3676(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x15e2: v15e2 = MLOAD v159b(0x40)
    0x15e6: v15e6(0x0) = SUB v159e, v15e2
    0x15e7: v15e7(0x84) = CONST 
    0x15e9: v15e9(0x84) = ADD v15e7(0x84), v15e6(0x0)
    0x15eb: REVERT v15e2, v15e9(0x84)
    0x3671: v3671(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x3676: v3676(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 

    Begin block 0x15ec
    prev=[0x1592], succ=[0x1608]
    =================================
    0x15ed: v15ed(0x2) = CONST 
    0x15ef: v15ef = SLOAD v15ed(0x2)
    0x15f0: v15f0(0x1) = CONST 
    0x15f2: v15f2(0xa0) = CONST 
    0x15f4: v15f4(0x2) = CONST 
    0x15f6: v15f6(0x10000000000000000000000000000000000000000) = EXP v15f4(0x2), v15f2(0xa0)
    0x15f7: v15f7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15f6(0x10000000000000000000000000000000000000000), v15f0(0x1)
    0x15f8: v15f8 = AND v15f7(0xffffffffffffffffffffffffffffffffffffffff), v15ef
    0x15f9: v15f9(0xda46098c) = CONST 
    0x15ff: v15ff = CALLER 
    0x1600: v1600(0x1608) = CONST 
    0x1604: v1604(0x16d7) = CONST 
    0x1607: v1607_0 = CALLPRIVATE v1604(0x16d7), v328, v1600(0x1608)

    Begin block 0x1608
    prev=[0x15ec], succ=[0x1670, 0x1674]
    =================================
    0x1609: v1609(0x40) = CONST 
    0x160c: v160c = MLOAD v1609(0x40)
    0x160d: v160d(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x162b: v162b(0xffffffff) = CONST 
    0x1631: v1631(0xda46098c) = AND v15f9(0xda46098c), v162b(0xffffffff)
    0x1632: v1632(0xda46098c00000000000000000000000000000000000000000000000000000000) = MUL v1631(0xda46098c), v160d(0x100000000000000000000000000000000000000000000000000000000)
    0x1634: MSTORE v160c, v1632(0xda46098c00000000000000000000000000000000000000000000000000000000)
    0x1635: v1635(0x1) = CONST 
    0x1637: v1637(0xa0) = CONST 
    0x1639: v1639(0x2) = CONST 
    0x163b: v163b(0x10000000000000000000000000000000000000000) = EXP v1639(0x2), v1637(0xa0)
    0x163c: v163c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v163b(0x10000000000000000000000000000000000000000), v1635(0x1)
    0x163f: v163f = AND v163c(0xffffffffffffffffffffffffffffffffffffffff), v328
    0x1640: v1640(0x4) = CONST 
    0x1643: v1643 = ADD v160c, v1640(0x4)
    0x1644: MSTORE v1643, v163f
    0x1648: v1648 = AND v163c(0xffffffffffffffffffffffffffffffffffffffff), v15ff
    0x1649: v1649(0x24) = CONST 
    0x164c: v164c = ADD v160c, v1649(0x24)
    0x164d: MSTORE v164c, v1648
    0x164e: v164e(0x44) = CONST 
    0x1651: v1651 = ADD v160c, v164e(0x44)
    0x1652: MSTORE v1651, v1607_0
    0x1654: v1654 = MLOAD v1609(0x40)
    0x1655: v1655(0x64) = CONST 
    0x1659: v1659 = ADD v160c, v1655(0x64)
    0x165b: v165b(0x0) = CONST 
    0x1662: v1662(0x0) = SUB v160c, v1654
    0x1663: v1663(0x64) = ADD v1662(0x0), v1655(0x64)
    0x1668: v1668 = EXTCODESIZE v15f8
    0x1669: v1669 = ISZERO v1668
    0x166b: v166b = ISZERO v1669
    0x166c: v166c(0x1674) = CONST 
    0x166f: JUMPI v166c(0x1674), v166b

    Begin block 0x1670
    prev=[0x1608], succ=[]
    =================================
    0x1670: v1670(0x0) = CONST 
    0x1673: REVERT v1670(0x0), v1670(0x0)

    Begin block 0x1674
    prev=[0x1608], succ=[0x167f, 0x1688]
    =================================
    0x1676: v1676 = GAS 
    0x1677: v1677 = CALL v1676, v15f8, v165b(0x0), v1654, v1663(0x64), v1654, v165b(0x0)
    0x1678: v1678 = ISZERO v1677
    0x167a: v167a = ISZERO v1678
    0x167b: v167b(0x1688) = CONST 
    0x167e: JUMPI v167b(0x1688), v167a

    Begin block 0x167f
    prev=[0x1674], succ=[]
    =================================
    0x167f: v167f = RETURNDATASIZE 
    0x1680: v1680(0x0) = CONST 
    0x1683: RETURNDATACOPY v1680(0x0), v1680(0x0), v167f
    0x1684: v1684 = RETURNDATASIZE 
    0x1685: v1685(0x0) = CONST 
    0x1687: REVERT v1685(0x0), v1684

    Begin block 0x1688
    prev=[0x1674], succ=[0x16c2]
    =================================
    0x168a: v168a = CALLER 
    0x168f: v168f(0x1) = CONST 
    0x1691: v1691(0xa0) = CONST 
    0x1693: v1693(0x2) = CONST 
    0x1695: v1695(0x10000000000000000000000000000000000000000) = EXP v1693(0x2), v1691(0xa0)
    0x1696: v1696(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1695(0x10000000000000000000000000000000000000000), v168f(0x1)
    0x1698: v1698 = AND v328, v1696(0xffffffffffffffffffffffffffffffffffffffff)
    0x1699: v1699(0x3b1ffca3903932aa264fbb5b7b381746e2b7b61c9c5a6024bad48d23f958a6c2) = CONST 
    0x16ba: v16ba(0x16c2) = CONST 
    0x16be: v16be(0x16d7) = CONST 
    0x16c1: v16c1_0 = CALLPRIVATE v16be(0x16d7), v328, v16ba(0x16c2)

    Begin block 0x16c2
    prev=[0x1688], succ=[0x31e4]
    =================================
    0x16c3: v16c3(0x40) = CONST 
    0x16c6: v16c6 = MLOAD v16c3(0x40)
    0x16c9: MSTORE v16c6, v16c1_0
    0x16ca: v16ca = MLOAD v16c3(0x40)
    0x16ce: v16ce(0x0) = SUB v16c6, v16ca
    0x16cf: v16cf(0x20) = CONST 
    0x16d1: v16d1(0x20) = ADD v16cf(0x20), v16ce(0x0)
    0x16d3: LOG3 v16ca, v16d1(0x20), v1699(0x3b1ffca3903932aa264fbb5b7b381746e2b7b61c9c5a6024bad48d23f958a6c2), v1698, v168a
    0x16d6: JUMP v31a(0x31e4)

    Begin block 0x31e4
    prev=[0x16c2], succ=[]
    =================================
    0x31e5: STOP 

}

function balanceOf(address)() public {
    Begin block 0x32d
    prev=[], succ=[0x335, 0x339]
    =================================
    0x32e: v32e = CALLVALUE 
    0x330: v330 = ISZERO v32e
    0x331: v331(0x339) = CONST 
    0x334: JUMPI v331(0x339), v330

    Begin block 0x335
    prev=[0x32d], succ=[]
    =================================
    0x335: v335(0x0) = CONST 
    0x338: REVERT v335(0x0), v335(0x0)

    Begin block 0x339
    prev=[0x32d], succ=[0x3205]
    =================================
    0x33b: v33b(0x3205) = CONST 
    0x33e: v33e(0x1) = CONST 
    0x340: v340(0xa0) = CONST 
    0x342: v342(0x2) = CONST 
    0x344: v344(0x10000000000000000000000000000000000000000) = EXP v342(0x2), v340(0xa0)
    0x345: v345(0xffffffffffffffffffffffffffffffffffffffff) = SUB v344(0x10000000000000000000000000000000000000000), v33e(0x1)
    0x346: v346(0x4) = CONST 
    0x348: v348 = CALLDATALOAD v346(0x4)
    0x349: v349 = AND v348, v345(0xffffffffffffffffffffffffffffffffffffffff)
    0x34a: v34a(0x16d7) = CONST 
    0x34d: v34d_0 = CALLPRIVATE v34a(0x16d7), v349, v33b(0x3205)

    Begin block 0x3205
    prev=[0x339], succ=[]
    =================================
    0x3206: v3206(0x40) = CONST 
    0x3209: v3209 = MLOAD v3206(0x40)
    0x320c: MSTORE v3209, v34d_0
    0x320d: v320d = MLOAD v3206(0x40)
    0x3211: v3211(0x0) = SUB v3209, v320d
    0x3212: v3212(0x20) = CONST 
    0x3214: v3214(0x20) = ADD v3212(0x20), v3211(0x0)
    0x3216: RETURN v320d, v3214(0x20)

}

function pause()() public {
    Begin block 0x34e
    prev=[], succ=[0x356, 0x35a]
    =================================
    0x34f: v34f = CALLVALUE 
    0x351: v351 = ISZERO v34f
    0x352: v352(0x35a) = CONST 
    0x355: JUMPI v352(0x35a), v351

    Begin block 0x356
    prev=[0x34e], succ=[]
    =================================
    0x356: v356(0x0) = CONST 
    0x359: REVERT v356(0x0), v356(0x0)

    Begin block 0x35a
    prev=[0x34e], succ=[0x1774]
    =================================
    0x35c: v35c(0x3236) = CONST 
    0x35f: v35f(0x1774) = CONST 
    0x362: JUMP v35f(0x1774)

    Begin block 0x1774
    prev=[0x35a], succ=[0x1787, 0x178b]
    =================================
    0x1775: v1775(0x0) = CONST 
    0x1777: v1777 = SLOAD v1775(0x0)
    0x1778: v1778(0x1) = CONST 
    0x177a: v177a(0xa0) = CONST 
    0x177c: v177c(0x2) = CONST 
    0x177e: v177e(0x10000000000000000000000000000000000000000) = EXP v177c(0x2), v177a(0xa0)
    0x177f: v177f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v177e(0x10000000000000000000000000000000000000000), v1778(0x1)
    0x1780: v1780 = AND v177f(0xffffffffffffffffffffffffffffffffffffffff), v1777
    0x1781: v1781 = CALLER 
    0x1782: v1782 = EQ v1781, v1780
    0x1783: v1783(0x178b) = CONST 
    0x1786: JUMPI v1783(0x178b), v1782

    Begin block 0x1787
    prev=[0x1774], succ=[]
    =================================
    0x1787: v1787(0x0) = CONST 
    0x178a: REVERT v1787(0x0), v1787(0x0)

    Begin block 0x178b
    prev=[0x1774], succ=[0x179e, 0x17a2]
    =================================
    0x178c: v178c(0x1) = CONST 
    0x178e: v178e = SLOAD v178c(0x1)
    0x178f: v178f(0xa0) = CONST 
    0x1791: v1791(0x2) = CONST 
    0x1793: v1793(0x10000000000000000000000000000000000000000) = EXP v1791(0x2), v178f(0xa0)
    0x1795: v1795 = DIV v178e, v1793(0x10000000000000000000000000000000000000000)
    0x1796: v1796(0xff) = CONST 
    0x1798: v1798 = AND v1796(0xff), v1795
    0x1799: v1799 = ISZERO v1798
    0x179a: v179a(0x17a2) = CONST 
    0x179d: JUMPI v179a(0x17a2), v1799

    Begin block 0x179e
    prev=[0x178b], succ=[]
    =================================
    0x179e: v179e(0x0) = CONST 
    0x17a1: REVERT v179e(0x0), v179e(0x0)

    Begin block 0x17a2
    prev=[0x178b], succ=[0x3236]
    =================================
    0x17a3: v17a3(0x1) = CONST 
    0x17a6: v17a6 = SLOAD v17a3(0x1)
    0x17a7: v17a7(0xff0000000000000000000000000000000000000000) = CONST 
    0x17bd: v17bd(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = NOT v17a7(0xff0000000000000000000000000000000000000000)
    0x17be: v17be = AND v17bd(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v17a6
    0x17bf: v17bf(0xa0) = CONST 
    0x17c1: v17c1(0x2) = CONST 
    0x17c3: v17c3(0x10000000000000000000000000000000000000000) = EXP v17c1(0x2), v17bf(0xa0)
    0x17c4: v17c4 = OR v17c3(0x10000000000000000000000000000000000000000), v17be
    0x17c6: SSTORE v17a3(0x1), v17c4
    0x17c7: v17c7(0x40) = CONST 
    0x17c9: v17c9 = MLOAD v17c7(0x40)
    0x17ca: v17ca(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625) = CONST 
    0x17ec: v17ec(0x0) = CONST 
    0x17ef: LOG1 v17c9, v17ec(0x0), v17ca(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625)
    0x17f0: JUMP v35c(0x3236)

    Begin block 0x3236
    prev=[0x17a2], succ=[]
    =================================
    0x3237: STOP 

}

function isMethodEnabled()() public {
    Begin block 0x363
    prev=[], succ=[0x36b, 0x36f]
    =================================
    0x364: v364 = CALLVALUE 
    0x366: v366 = ISZERO v364
    0x367: v367(0x36f) = CONST 
    0x36a: JUMPI v367(0x36f), v366

    Begin block 0x36b
    prev=[0x363], succ=[]
    =================================
    0x36b: v36b(0x0) = CONST 
    0x36e: REVERT v36b(0x0), v36b(0x0)

    Begin block 0x36f
    prev=[0x363], succ=[0x17f1]
    =================================
    0x371: v371(0x3257) = CONST 
    0x374: v374(0x17f1) = CONST 
    0x377: JUMP v374(0x17f1)

    Begin block 0x17f1
    prev=[0x36f], succ=[0x3257]
    =================================
    0x17f2: v17f2(0x1) = CONST 
    0x17f4: v17f4 = SLOAD v17f2(0x1)
    0x17f5: v17f5(0x1000000000000000000000000000000000000000000) = CONST 
    0x180d: v180d = DIV v17f4, v17f5(0x1000000000000000000000000000000000000000000)
    0x180e: v180e(0xff) = CONST 
    0x1810: v1810 = AND v180e(0xff), v180d
    0x1812: JUMP v371(0x3257)

    Begin block 0x3257
    prev=[0x17f1], succ=[]
    =================================
    0x3258: v3258(0x40) = CONST 
    0x325b: v325b = MLOAD v3258(0x40)
    0x325d: v325d = ISZERO v1810
    0x325e: v325e = ISZERO v325d
    0x3260: MSTORE v325b, v325e
    0x3261: v3261 = MLOAD v3258(0x40)
    0x3265: v3265(0x0) = SUB v325b, v3261
    0x3266: v3266(0x20) = CONST 
    0x3268: v3268(0x20) = ADD v3266(0x20), v3265(0x0)
    0x326a: RETURN v3261, v3268(0x20)

}

function owner()() public {
    Begin block 0x378
    prev=[], succ=[0x380, 0x384]
    =================================
    0x379: v379 = CALLVALUE 
    0x37b: v37b = ISZERO v379
    0x37c: v37c(0x384) = CONST 
    0x37f: JUMPI v37c(0x384), v37b

    Begin block 0x380
    prev=[0x378], succ=[]
    =================================
    0x380: v380(0x0) = CONST 
    0x383: REVERT v380(0x0), v380(0x0)

    Begin block 0x384
    prev=[0x378], succ=[0x1813]
    =================================
    0x386: v386(0x328a) = CONST 
    0x389: v389(0x1813) = CONST 
    0x38c: JUMP v389(0x1813)

    Begin block 0x1813
    prev=[0x384], succ=[0x328a]
    =================================
    0x1814: v1814(0x0) = CONST 
    0x1816: v1816 = SLOAD v1814(0x0)
    0x1817: v1817(0x1) = CONST 
    0x1819: v1819(0xa0) = CONST 
    0x181b: v181b(0x2) = CONST 
    0x181d: v181d(0x10000000000000000000000000000000000000000) = EXP v181b(0x2), v1819(0xa0)
    0x181e: v181e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v181d(0x10000000000000000000000000000000000000000), v1817(0x1)
    0x181f: v181f = AND v181e(0xffffffffffffffffffffffffffffffffffffffff), v1816
    0x1821: JUMP v386(0x328a)

    Begin block 0x328a
    prev=[0x1813], succ=[]
    =================================
    0x328b: v328b(0x40) = CONST 
    0x328e: v328e = MLOAD v328b(0x40)
    0x328f: v328f(0x1) = CONST 
    0x3291: v3291(0xa0) = CONST 
    0x3293: v3293(0x2) = CONST 
    0x3295: v3295(0x10000000000000000000000000000000000000000) = EXP v3293(0x2), v3291(0xa0)
    0x3296: v3296(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3295(0x10000000000000000000000000000000000000000), v328f(0x1)
    0x3299: v3299 = AND v181f, v3296(0xffffffffffffffffffffffffffffffffffffffff)
    0x329b: MSTORE v328e, v3299
    0x329c: v329c = MLOAD v328b(0x40)
    0x32a0: v32a0(0x0) = SUB v328e, v329c
    0x32a1: v32a1(0x20) = CONST 
    0x32a3: v32a3(0x20) = ADD v32a1(0x20), v32a0(0x0)
    0x32a5: RETURN v329c, v32a3(0x20)

}

function mintCUSD(address,uint256)() public {
    Begin block 0x38d
    prev=[], succ=[0x395, 0x399]
    =================================
    0x38e: v38e = CALLVALUE 
    0x390: v390 = ISZERO v38e
    0x391: v391(0x399) = CONST 
    0x394: JUMPI v391(0x399), v390

    Begin block 0x395
    prev=[0x38d], succ=[]
    =================================
    0x395: v395(0x0) = CONST 
    0x398: REVERT v395(0x0), v395(0x0)

    Begin block 0x399
    prev=[0x38d], succ=[0x1822B0x399]
    =================================
    0x39b: v39b(0x32c5) = CONST 
    0x39e: v39e(0x1) = CONST 
    0x3a0: v3a0(0xa0) = CONST 
    0x3a2: v3a2(0x2) = CONST 
    0x3a4: v3a4(0x10000000000000000000000000000000000000000) = EXP v3a2(0x2), v3a0(0xa0)
    0x3a5: v3a5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a4(0x10000000000000000000000000000000000000000), v39e(0x1)
    0x3a6: v3a6(0x4) = CONST 
    0x3a8: v3a8 = CALLDATALOAD v3a6(0x4)
    0x3a9: v3a9 = AND v3a8, v3a5(0xffffffffffffffffffffffffffffffffffffffff)
    0x3aa: v3aa(0x24) = CONST 
    0x3ac: v3ac = CALLDATALOAD v3aa(0x24)
    0x3ad: v3ad(0x1822) = CONST 
    0x3b0: JUMP v3ad(0x1822), v3ac, v3a9, v39b(0x32c5)

    Begin block 0x1822B0x399
    prev=[0x399], succ=[0x1882B0x399, 0x1886B0x399]
    =================================
    0x1823S0x399: v1823V399(0x3) = CONST 
    0x1825S0x399: v1825V399 = SLOAD v1823V399(0x3)
    0x1826S0x399: v1826V399(0x40) = CONST 
    0x1829S0x399: v1829V399 = MLOAD v1826V399(0x40)
    0x182aS0x399: v182aV399(0xe3) = CONST 
    0x182cS0x399: v182cV399(0x2) = CONST 
    0x182eS0x399: v182eV399(0x800000000000000000000000000000000000000000000000000000000) = EXP v182cV399(0x2), v182aV399(0xe3)
    0x182fS0x399: v182fV399(0x29b6dab) = CONST 
    0x1834S0x399: v1834V399(0x14db6d5800000000000000000000000000000000000000000000000000000000) = MUL v182fV399(0x29b6dab), v182eV399(0x800000000000000000000000000000000000000000000000000000000)
    0x1836S0x399: MSTORE v1829V399, v1834V399(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1837S0x399: v1837V399 = CALLER 
    0x1838S0x399: v1838V399(0x4) = CONST 
    0x183bS0x399: v183bV399 = ADD v1829V399, v1838V399(0x4)
    0x183cS0x399: MSTORE v183bV399, v1837V399
    0x183dS0x399: v183dV399(0x0) = CONST 
    0x1840S0x399: v1840V399 = CALLDATALOAD v183dV399(0x0)
    0x1841S0x399: v1841V399(0x1) = CONST 
    0x1843S0x399: v1843V399(0xe0) = CONST 
    0x1845S0x399: v1845V399(0x2) = CONST 
    0x1847S0x399: v1847V399(0x100000000000000000000000000000000000000000000000000000000) = EXP v1845V399(0x2), v1843V399(0xe0)
    0x1848S0x399: v1848V399(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1847V399(0x100000000000000000000000000000000000000000000000000000000), v1841V399(0x1)
    0x1849S0x399: v1849V399(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1848V399(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x184aS0x399: v184aV399 = AND v1849V399(0xffffffff00000000000000000000000000000000000000000000000000000000), v1840V399
    0x184bS0x399: v184bV399(0x24) = CONST 
    0x184eS0x399: v184eV399 = ADD v1829V399, v184bV399(0x24)
    0x184fS0x399: MSTORE v184eV399, v184aV399
    0x1851S0x399: v1851V399 = MLOAD v1826V399(0x40)
    0x1852S0x399: v1852V399(0x1) = CONST 
    0x1854S0x399: v1854V399(0xa0) = CONST 
    0x1856S0x399: v1856V399(0x2) = CONST 
    0x1858S0x399: v1858V399(0x10000000000000000000000000000000000000000) = EXP v1856V399(0x2), v1854V399(0xa0)
    0x1859S0x399: v1859V399(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1858V399(0x10000000000000000000000000000000000000000), v1852V399(0x1)
    0x185cS0x399: v185cV399 = AND v1825V399, v1859V399(0xffffffffffffffffffffffffffffffffffffffff)
    0x185eS0x399: v185eV399(0x14db6d58) = CONST 
    0x1864S0x399: v1864V399(0x44) = CONST 
    0x1868S0x399: v1868V399 = ADD v1829V399, v1864V399(0x44)
    0x186aS0x399: v186aV399(0x20) = CONST 
    0x1871S0x399: v1871V399(0x0) = SUB v1829V399, v1851V399
    0x1874S0x399: v1874V399(0x44) = ADD v1864V399(0x44), v1871V399(0x0)
    0x187aS0x399: v187aV399 = EXTCODESIZE v185cV399
    0x187bS0x399: v187bV399 = ISZERO v187aV399
    0x187dS0x399: v187dV399 = ISZERO v187bV399
    0x187eS0x399: v187eV399(0x1886) = CONST 
    0x1881S0x399: JUMPI v187eV399(0x1886), v187dV399

    Begin block 0x1882B0x399
    prev=[0x1822B0x399], succ=[]
    =================================
    0x1882S0x399: v1882V399(0x0) = CONST 
    0x1885S0x399: REVERT v1882V399(0x0), v1882V399(0x0)

    Begin block 0x1886B0x399
    prev=[0x1822B0x399], succ=[0x1891B0x399, 0x189aB0x399]
    =================================
    0x1888S0x399: v1888V399 = GAS 
    0x1889S0x399: v1889V399 = CALL v1888V399, v185cV399, v183dV399(0x0), v1851V399, v1874V399(0x44), v1851V399, v186aV399(0x20)
    0x188aS0x399: v188aV399 = ISZERO v1889V399
    0x188cS0x399: v188cV399 = ISZERO v188aV399
    0x188dS0x399: v188dV399(0x189a) = CONST 
    0x1890S0x399: JUMPI v188dV399(0x189a), v188cV399

    Begin block 0x1891B0x399
    prev=[0x1886B0x399], succ=[]
    =================================
    0x1891S0x399: v1891V399 = RETURNDATASIZE 
    0x1892S0x399: v1892V399(0x0) = CONST 
    0x1895S0x399: RETURNDATACOPY v1892V399(0x0), v1892V399(0x0), v1891V399
    0x1896S0x399: v1896V399 = RETURNDATASIZE 
    0x1897S0x399: v1897V399(0x0) = CONST 
    0x1899S0x399: REVERT v1897V399(0x0), v1896V399

    Begin block 0x189aB0x399
    prev=[0x1886B0x399], succ=[0x18acB0x399, 0x18b0B0x399]
    =================================
    0x189fS0x399: v189fV399(0x40) = CONST 
    0x18a1S0x399: v18a1V399 = MLOAD v189fV399(0x40)
    0x18a2S0x399: v18a2V399 = RETURNDATASIZE 
    0x18a3S0x399: v18a3V399(0x20) = CONST 
    0x18a6S0x399: v18a6V399 = LT v18a2V399, v18a3V399(0x20)
    0x18a7S0x399: v18a7V399 = ISZERO v18a6V399
    0x18a8S0x399: v18a8V399(0x18b0) = CONST 
    0x18abS0x399: JUMPI v18a8V399(0x18b0), v18a7V399

    Begin block 0x18acB0x399
    prev=[0x189aB0x399], succ=[]
    =================================
    0x18acS0x399: v18acV399(0x0) = CONST 
    0x18afS0x399: REVERT v18acV399(0x0), v18acV399(0x0)

    Begin block 0x18b0B0x399
    prev=[0x189aB0x399], succ=[0x18b9B0x399, 0x190aB0x399]
    =================================
    0x18b2S0x399: v18b2V399 = MLOAD v18a1V399
    0x18b3S0x399: v18b3V399 = ISZERO v18b2V399
    0x18b4S0x399: v18b4V399 = ISZERO v18b3V399
    0x18b5S0x399: v18b5V399(0x190a) = CONST 
    0x18b8S0x399: JUMPI v18b5V399(0x190a), v18b4V399

    Begin block 0x18b9B0x399
    prev=[0x18b0B0x399], succ=[]
    =================================
    0x18b9S0x399: v18b9V399(0x40) = CONST 
    0x18bcS0x399: v18bcV399 = MLOAD v18b9V399(0x40)
    0x18bdS0x399: v18bdV399(0xe5) = CONST 
    0x18bfS0x399: v18bfV399(0x2) = CONST 
    0x18c1S0x399: v18c1V399(0x2000000000000000000000000000000000000000000000000000000000) = EXP v18bfV399(0x2), v18bdV399(0xe5)
    0x18c2S0x399: v18c2V399(0x461bcd) = CONST 
    0x18c6S0x399: v18c6V399(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v18c2V399(0x461bcd), v18c1V399(0x2000000000000000000000000000000000000000000000000000000000)
    0x18c8S0x399: MSTORE v18bcV399, v18c6V399(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x18c9S0x399: v18c9V399(0x20) = CONST 
    0x18cbS0x399: v18cbV399(0x4) = CONST 
    0x18ceS0x399: v18ceV399 = ADD v18bcV399, v18cbV399(0x4)
    0x18cfS0x399: MSTORE v18ceV399, v18c9V399(0x20)
    0x18d0S0x399: v18d0V399(0x31) = CONST 
    0x18d2S0x399: v18d2V399(0x24) = CONST 
    0x18d5S0x399: v18d5V399 = ADD v18bcV399, v18d2V399(0x24)
    0x18d6S0x399: MSTORE v18d5V399, v18d0V399(0x31)
    0x18d7S0x399: v18d7V399(0x0) = CONST 
    0x18daS0x399: v18daV399 = MLOAD v18d7V399(0x0)
    0x18dbS0x399: v18dbV399(0x20) = CONST 
    0x18ddS0x399: v18ddV399(0x2f4a) = CONST 
    0x18e5S0x399: MSTORE v18d7V399(0x0), v18daV399
    0x18e6S0x399: v18e6V399(0x44) = CONST 
    0x18e9S0x399: v18e9V399 = ADD v18bcV399, v18e6V399(0x44)
    0x18eaS0x399: MSTORE v18e9V399, v367bV399(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x18ebS0x399: v18ebV399(0x0) = CONST 
    0x18eeS0x399: v18eeV399 = MLOAD v18ebV399(0x0)
    0x18efS0x399: v18efV399(0x20) = CONST 
    0x18f1S0x399: v18f1V399(0x2f2a) = CONST 
    0x18f9S0x399: MSTORE v18ebV399(0x0), v18eeV399
    0x18faS0x399: v18faV399(0x64) = CONST 
    0x18fdS0x399: v18fdV399 = ADD v18bcV399, v18faV399(0x64)
    0x18feS0x399: MSTORE v18fdV399, v3680V399(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x1900S0x399: v1900V399 = MLOAD v18b9V399(0x40)
    0x1904S0x399: v1904V399(0x0) = SUB v18bcV399, v1900V399
    0x1905S0x399: v1905V399(0x84) = CONST 
    0x1907S0x399: v1907V399(0x84) = ADD v1905V399(0x84), v1904V399(0x0)
    0x1909S0x399: REVERT v1900V399, v1907V399(0x84)
    0x367bS0x399: v367bV399(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x3680S0x399: v3680V399(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 

    Begin block 0x190aB0x399
    prev=[0x18b0B0x399], succ=[0x191dB0x399, 0x1921B0x399]
    =================================
    0x190bS0x399: v190bV399(0x1) = CONST 
    0x190dS0x399: v190dV399 = SLOAD v190bV399(0x1)
    0x190eS0x399: v190eV399(0xa0) = CONST 
    0x1910S0x399: v1910V399(0x2) = CONST 
    0x1912S0x399: v1912V399(0x10000000000000000000000000000000000000000) = EXP v1910V399(0x2), v190eV399(0xa0)
    0x1914S0x399: v1914V399 = DIV v190dV399, v1912V399(0x10000000000000000000000000000000000000000)
    0x1915S0x399: v1915V399(0xff) = CONST 
    0x1917S0x399: v1917V399 = AND v1915V399(0xff), v1914V399
    0x1918S0x399: v1918V399 = ISZERO v1917V399
    0x1919S0x399: v1919V399(0x1921) = CONST 
    0x191cS0x399: JUMPI v1919V399(0x1921), v1918V399

    Begin block 0x191dB0x399
    prev=[0x190aB0x399], succ=[]
    =================================
    0x191dS0x399: v191dV399(0x0) = CONST 
    0x1920S0x399: REVERT v191dV399(0x0), v191dV399(0x0)

    Begin block 0x1921B0x399
    prev=[0x190aB0x399], succ=[0x1972B0x399, 0x1976B0x399]
    =================================
    0x1922S0x399: v1922V399(0x3) = CONST 
    0x1924S0x399: v1924V399 = SLOAD v1922V399(0x3)
    0x1925S0x399: v1925V399(0x40) = CONST 
    0x1928S0x399: v1928V399 = MLOAD v1925V399(0x40)
    0x1929S0x399: v1929V399(0xe0) = CONST 
    0x192bS0x399: v192bV399(0x2) = CONST 
    0x192dS0x399: v192dV399(0x100000000000000000000000000000000000000000000000000000000) = EXP v192bV399(0x2), v1929V399(0xe0)
    0x192eS0x399: v192eV399(0x7ccce851) = CONST 
    0x1933S0x399: v1933V399(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v192eV399(0x7ccce851), v192dV399(0x100000000000000000000000000000000000000000000000000000000)
    0x1935S0x399: MSTORE v1928V399, v1933V399(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1936S0x399: v1936V399(0x1) = CONST 
    0x1938S0x399: v1938V399(0xa0) = CONST 
    0x193aS0x399: v193aV399(0x2) = CONST 
    0x193cS0x399: v193cV399(0x10000000000000000000000000000000000000000) = EXP v193aV399(0x2), v1938V399(0xa0)
    0x193dS0x399: v193dV399(0xffffffffffffffffffffffffffffffffffffffff) = SUB v193cV399(0x10000000000000000000000000000000000000000), v1936V399(0x1)
    0x1940S0x399: v1940V399 = AND v3a9, v193dV399(0xffffffffffffffffffffffffffffffffffffffff)
    0x1941S0x399: v1941V399(0x4) = CONST 
    0x1944S0x399: v1944V399 = ADD v1928V399, v1941V399(0x4)
    0x1945S0x399: MSTORE v1944V399, v1940V399
    0x1947S0x399: v1947V399 = MLOAD v1925V399(0x40)
    0x194dS0x399: v194dV399 = AND v1924V399, v193dV399(0xffffffffffffffffffffffffffffffffffffffff)
    0x194fS0x399: v194fV399(0x7ccce851) = CONST 
    0x1955S0x399: v1955V399(0x24) = CONST 
    0x1959S0x399: v1959V399 = ADD v1928V399, v1955V399(0x24)
    0x195bS0x399: v195bV399(0x20) = CONST 
    0x1963S0x399: v1963V399(0x0) = SUB v1928V399, v1947V399
    0x1964S0x399: v1964V399(0x24) = ADD v1963V399(0x0), v1955V399(0x24)
    0x1966S0x399: v1966V399(0x0) = CONST 
    0x196aS0x399: v196aV399 = EXTCODESIZE v194dV399
    0x196bS0x399: v196bV399 = ISZERO v196aV399
    0x196dS0x399: v196dV399 = ISZERO v196bV399
    0x196eS0x399: v196eV399(0x1976) = CONST 
    0x1971S0x399: JUMPI v196eV399(0x1976), v196dV399

    Begin block 0x1972B0x399
    prev=[0x1921B0x399], succ=[]
    =================================
    0x1972S0x399: v1972V399(0x0) = CONST 
    0x1975S0x399: REVERT v1972V399(0x0), v1972V399(0x0)

    Begin block 0x1976B0x399
    prev=[0x1921B0x399], succ=[0x1981B0x399, 0x198aB0x399]
    =================================
    0x1978S0x399: v1978V399 = GAS 
    0x1979S0x399: v1979V399 = CALL v1978V399, v194dV399, v1966V399(0x0), v1947V399, v1964V399(0x24), v1947V399, v195bV399(0x20)
    0x197aS0x399: v197aV399 = ISZERO v1979V399
    0x197cS0x399: v197cV399 = ISZERO v197aV399
    0x197dS0x399: v197dV399(0x198a) = CONST 
    0x1980S0x399: JUMPI v197dV399(0x198a), v197cV399

    Begin block 0x1981B0x399
    prev=[0x1976B0x399], succ=[]
    =================================
    0x1981S0x399: v1981V399 = RETURNDATASIZE 
    0x1982S0x399: v1982V399(0x0) = CONST 
    0x1985S0x399: RETURNDATACOPY v1982V399(0x0), v1982V399(0x0), v1981V399
    0x1986S0x399: v1986V399 = RETURNDATASIZE 
    0x1987S0x399: v1987V399(0x0) = CONST 
    0x1989S0x399: REVERT v1987V399(0x0), v1986V399

    Begin block 0x198aB0x399
    prev=[0x1976B0x399], succ=[0x199cB0x399, 0x19a0B0x399]
    =================================
    0x198fS0x399: v198fV399(0x40) = CONST 
    0x1991S0x399: v1991V399 = MLOAD v198fV399(0x40)
    0x1992S0x399: v1992V399 = RETURNDATASIZE 
    0x1993S0x399: v1993V399(0x20) = CONST 
    0x1996S0x399: v1996V399 = LT v1992V399, v1993V399(0x20)
    0x1997S0x399: v1997V399 = ISZERO v1996V399
    0x1998S0x399: v1998V399(0x19a0) = CONST 
    0x199bS0x399: JUMPI v1998V399(0x19a0), v1997V399

    Begin block 0x199cB0x399
    prev=[0x198aB0x399], succ=[]
    =================================
    0x199cS0x399: v199cV399(0x0) = CONST 
    0x199fS0x399: REVERT v199cV399(0x0), v199cV399(0x0)

    Begin block 0x19a0B0x399
    prev=[0x198aB0x399], succ=[0x19a8B0x399, 0x19e5B0x399]
    =================================
    0x19a2S0x399: v19a2V399 = MLOAD v1991V399
    0x19a3S0x399: v19a3V399 = ISZERO v19a2V399
    0x19a4S0x399: v19a4V399(0x19e5) = CONST 
    0x19a7S0x399: JUMPI v19a4V399(0x19e5), v19a3V399

    Begin block 0x19a8B0x399
    prev=[0x19a0B0x399], succ=[]
    =================================
    0x19a8S0x399: v19a8V399(0x40) = CONST 
    0x19abS0x399: v19abV399 = MLOAD v19a8V399(0x40)
    0x19acS0x399: v19acV399(0xe5) = CONST 
    0x19aeS0x399: v19aeV399(0x2) = CONST 
    0x19b0S0x399: v19b0V399(0x2000000000000000000000000000000000000000000000000000000000) = EXP v19aeV399(0x2), v19acV399(0xe5)
    0x19b1S0x399: v19b1V399(0x461bcd) = CONST 
    0x19b5S0x399: v19b5V399(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v19b1V399(0x461bcd), v19b0V399(0x2000000000000000000000000000000000000000000000000000000000)
    0x19b7S0x399: MSTORE v19abV399, v19b5V399(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19b8S0x399: v19b8V399(0x20) = CONST 
    0x19baS0x399: v19baV399(0x4) = CONST 
    0x19bdS0x399: v19bdV399 = ADD v19abV399, v19baV399(0x4)
    0x19beS0x399: MSTORE v19bdV399, v19b8V399(0x20)
    0x19bfS0x399: v19bfV399(0x1c) = CONST 
    0x19c1S0x399: v19c1V399(0x24) = CONST 
    0x19c4S0x399: v19c4V399 = ADD v19abV399, v19c1V399(0x24)
    0x19c5S0x399: MSTORE v19c4V399, v19bfV399(0x1c)
    0x19c6S0x399: v19c6V399(0x0) = CONST 
    0x19c9S0x399: v19c9V399 = MLOAD v19c6V399(0x0)
    0x19caS0x399: v19caV399(0x20) = CONST 
    0x19ccS0x399: v19ccV399(0x2f6a) = CONST 
    0x19d4S0x399: MSTORE v19c6V399(0x0), v19c9V399
    0x19d5S0x399: v19d5V399(0x44) = CONST 
    0x19d8S0x399: v19d8V399 = ADD v19abV399, v19d5V399(0x44)
    0x19d9S0x399: MSTORE v19d8V399, v3685V399(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x19dbS0x399: v19dbV399 = MLOAD v19a8V399(0x40)
    0x19dfS0x399: v19dfV399(0x0) = SUB v19abV399, v19dbV399
    0x19e0S0x399: v19e0V399(0x64) = CONST 
    0x19e2S0x399: v19e2V399(0x64) = ADD v19e0V399(0x64), v19dfV399(0x0)
    0x19e4S0x399: REVERT v19dbV399, v19e2V399(0x64)
    0x3685S0x399: v3685V399(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x19e5B0x399
    prev=[0x19a0B0x399], succ=[0x3542B0x399]
    =================================
    0x19e6S0x399: v19e6V399(0x3542) = CONST 
    0x19ebS0x399: v19ebV399(0x295a) = CONST 
    0x19eeS0x399: CALLPRIVATE v19ebV399(0x295a), v3ac, v3a9, v19e6V399(0x3542)

    Begin block 0x3542B0x399
    prev=[0x19e5B0x399], succ=[0x32c5]
    =================================
    0x3546S0x399: JUMP v39b(0x32c5)

    Begin block 0x32c5
    prev=[0x3542B0x399], succ=[]
    =================================
    0x32c6: STOP 

}

function setCUSDAddress(address)() public {
    Begin block 0x3b1
    prev=[], succ=[0x3b9, 0x3bd]
    =================================
    0x3b2: v3b2 = CALLVALUE 
    0x3b4: v3b4 = ISZERO v3b2
    0x3b5: v3b5(0x3bd) = CONST 
    0x3b8: JUMPI v3b5(0x3bd), v3b4

    Begin block 0x3b9
    prev=[0x3b1], succ=[]
    =================================
    0x3b9: v3b9(0x0) = CONST 
    0x3bc: REVERT v3b9(0x0), v3b9(0x0)

    Begin block 0x3bd
    prev=[0x3b1], succ=[0x19ef]
    =================================
    0x3bf: v3bf(0x32e6) = CONST 
    0x3c2: v3c2(0x1) = CONST 
    0x3c4: v3c4(0xa0) = CONST 
    0x3c6: v3c6(0x2) = CONST 
    0x3c8: v3c8(0x10000000000000000000000000000000000000000) = EXP v3c6(0x2), v3c4(0xa0)
    0x3c9: v3c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c8(0x10000000000000000000000000000000000000000), v3c2(0x1)
    0x3ca: v3ca(0x4) = CONST 
    0x3cc: v3cc = CALLDATALOAD v3ca(0x4)
    0x3cd: v3cd = AND v3cc, v3c9(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ce: v3ce(0x19ef) = CONST 
    0x3d1: JUMP v3ce(0x19ef)

    Begin block 0x19ef
    prev=[0x3bd], succ=[0x1a03, 0x1a07]
    =================================
    0x19f0: v19f0(0x0) = CONST 
    0x19f3: v19f3 = SLOAD v19f0(0x0)
    0x19f4: v19f4(0x1) = CONST 
    0x19f6: v19f6(0xa0) = CONST 
    0x19f8: v19f8(0x2) = CONST 
    0x19fa: v19fa(0x10000000000000000000000000000000000000000) = EXP v19f8(0x2), v19f6(0xa0)
    0x19fb: v19fb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19fa(0x10000000000000000000000000000000000000000), v19f4(0x1)
    0x19fc: v19fc = AND v19fb(0xffffffffffffffffffffffffffffffffffffffff), v19f3
    0x19fd: v19fd = CALLER 
    0x19fe: v19fe = EQ v19fd, v19fc
    0x19ff: v19ff(0x1a07) = CONST 
    0x1a02: JUMPI v19ff(0x1a07), v19fe

    Begin block 0x1a03
    prev=[0x19ef], succ=[]
    =================================
    0x1a03: v1a03(0x0) = CONST 
    0x1a06: REVERT v1a03(0x0), v1a03(0x0)

    Begin block 0x1a07
    prev=[0x19ef], succ=[0x1a1e, 0x1a6d]
    =================================
    0x1a08: v1a08(0x4) = CONST 
    0x1a0a: v1a0a = SLOAD v1a08(0x4)
    0x1a0b: v1a0b(0x1) = CONST 
    0x1a0d: v1a0d(0xa0) = CONST 
    0x1a0f: v1a0f(0x2) = CONST 
    0x1a11: v1a11(0x10000000000000000000000000000000000000000) = EXP v1a0f(0x2), v1a0d(0xa0)
    0x1a12: v1a12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a11(0x10000000000000000000000000000000000000000), v1a0b(0x1)
    0x1a15: v1a15 = AND v1a12(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0x1a17: v1a17 = AND v1a0a, v1a12(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a18: v1a18 = EQ v1a17, v1a15
    0x1a19: v1a19 = ISZERO v1a18
    0x1a1a: v1a1a(0x1a6d) = CONST 
    0x1a1d: JUMPI v1a1a(0x1a6d), v1a19

    Begin block 0x1a1e
    prev=[0x1a07], succ=[]
    =================================
    0x1a1e: v1a1e(0x40) = CONST 
    0x1a21: v1a21 = MLOAD v1a1e(0x40)
    0x1a22: v1a22(0xe5) = CONST 
    0x1a24: v1a24(0x2) = CONST 
    0x1a26: v1a26(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1a24(0x2), v1a22(0xe5)
    0x1a27: v1a27(0x461bcd) = CONST 
    0x1a2b: v1a2b(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1a27(0x461bcd), v1a26(0x2000000000000000000000000000000000000000000000000000000000)
    0x1a2d: MSTORE v1a21, v1a2b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a2e: v1a2e(0x20) = CONST 
    0x1a30: v1a30(0x4) = CONST 
    0x1a33: v1a33 = ADD v1a21, v1a30(0x4)
    0x1a34: MSTORE v1a33, v1a2e(0x20)
    0x1a35: v1a35(0x1a) = CONST 
    0x1a37: v1a37(0x24) = CONST 
    0x1a3a: v1a3a = ADD v1a21, v1a37(0x24)
    0x1a3b: MSTORE v1a3a, v1a35(0x1a)
    0x1a3c: v1a3c(0x4d7573742062652061206e657720637573642061646472657373000000000000) = CONST 
    0x1a5d: v1a5d(0x44) = CONST 
    0x1a60: v1a60 = ADD v1a21, v1a5d(0x44)
    0x1a61: MSTORE v1a60, v1a3c(0x4d7573742062652061206e657720637573642061646472657373000000000000)
    0x1a63: v1a63 = MLOAD v1a1e(0x40)
    0x1a67: v1a67(0x0) = SUB v1a21, v1a63
    0x1a68: v1a68(0x64) = CONST 
    0x1a6a: v1a6a(0x64) = ADD v1a68(0x64), v1a67(0x0)
    0x1a6c: REVERT v1a63, v1a6a(0x64)

    Begin block 0x1a6d
    prev=[0x1a07], succ=[0x2e3eB0x1a6d]
    =================================
    0x1a6e: v1a6e(0x1a76) = CONST 
    0x1a72: v1a72(0x2e3e) = CONST 
    0x1a75: JUMP v1a72(0x2e3e)

    Begin block 0x2e3eB0x1a6d
    prev=[0x1a6d], succ=[0x1a76]
    =================================
    0x2e3fS0x1a6d: v2e3fV1a6d(0x0) = CONST 
    0x2e42S0x1a6d: v2e42V1a6d = EXTCODESIZE v3cd
    0x2e43S0x1a6d: v2e43V1a6d = GT v2e42V1a6d, v2e3fV1a6d(0x0)
    0x2e45S0x1a6d: JUMP v1a6e(0x1a76)

    Begin block 0x1a76
    prev=[0x2e3eB0x1a6d], succ=[0x1a7d, 0x1acc]
    =================================
    0x1a77: v1a77 = ISZERO v2e43V1a6d
    0x1a78: v1a78 = ISZERO v1a77
    0x1a79: v1a79(0x1acc) = CONST 
    0x1a7c: JUMPI v1a79(0x1acc), v1a78

    Begin block 0x1a7d
    prev=[0x1a76], succ=[]
    =================================
    0x1a7d: v1a7d(0x40) = CONST 
    0x1a80: v1a80 = MLOAD v1a7d(0x40)
    0x1a81: v1a81(0xe5) = CONST 
    0x1a83: v1a83(0x2) = CONST 
    0x1a85: v1a85(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1a83(0x2), v1a81(0xe5)
    0x1a86: v1a86(0x461bcd) = CONST 
    0x1a8a: v1a8a(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1a86(0x461bcd), v1a85(0x2000000000000000000000000000000000000000000000000000000000)
    0x1a8c: MSTORE v1a80, v1a8a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a8d: v1a8d(0x20) = CONST 
    0x1a8f: v1a8f(0x4) = CONST 
    0x1a92: v1a92 = ADD v1a80, v1a8f(0x4)
    0x1a93: MSTORE v1a92, v1a8d(0x20)
    0x1a94: v1a94(0x1a) = CONST 
    0x1a96: v1a96(0x24) = CONST 
    0x1a99: v1a99 = ADD v1a80, v1a96(0x24)
    0x1a9a: MSTORE v1a99, v1a94(0x1a)
    0x1a9b: v1a9b(0x4d75737420626520616e2061637475616c20636f6e7472616374000000000000) = CONST 
    0x1abc: v1abc(0x44) = CONST 
    0x1abf: v1abf = ADD v1a80, v1abc(0x44)
    0x1ac0: MSTORE v1abf, v1a9b(0x4d75737420626520616e2061637475616c20636f6e7472616374000000000000)
    0x1ac2: v1ac2 = MLOAD v1a7d(0x40)
    0x1ac6: v1ac6(0x0) = SUB v1a80, v1ac2
    0x1ac7: v1ac7(0x64) = CONST 
    0x1ac9: v1ac9(0x64) = ADD v1ac7(0x64), v1ac6(0x0)
    0x1acb: REVERT v1ac2, v1ac9(0x64)

    Begin block 0x1acc
    prev=[0x1a76], succ=[0x32e6]
    =================================
    0x1ace: v1ace(0x4) = CONST 
    0x1ad1: v1ad1 = SLOAD v1ace(0x4)
    0x1ad2: v1ad2(0x1) = CONST 
    0x1ad4: v1ad4(0xa0) = CONST 
    0x1ad6: v1ad6(0x2) = CONST 
    0x1ad8: v1ad8(0x10000000000000000000000000000000000000000) = EXP v1ad6(0x2), v1ad4(0xa0)
    0x1ad9: v1ad9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ad8(0x10000000000000000000000000000000000000000), v1ad2(0x1)
    0x1adc: v1adc = AND v1ad9(0xffffffffffffffffffffffffffffffffffffffff), v3cd
    0x1add: v1add(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1af2: v1af2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1add(0xffffffffffffffffffffffffffffffffffffffff)
    0x1af4: v1af4 = AND v1ad1, v1af2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x1af6: v1af6 = OR v1adc, v1af4
    0x1af9: SSTORE v1ace(0x4), v1af6
    0x1afa: v1afa(0x40) = CONST 
    0x1afc: v1afc = MLOAD v1afa(0x40)
    0x1afe: v1afe = AND v1ad1, v1ad9(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b03: v1b03(0xec1b8e8ba02bcff9ae905a36374bb7e8f3bbd8ac86b05d99e881092f538a0aa) = CONST 
    0x1b25: v1b25(0x0) = CONST 
    0x1b28: LOG3 v1afc, v1b25(0x0), v1b03(0xec1b8e8ba02bcff9ae905a36374bb7e8f3bbd8ac86b05d99e881092f538a0aa), v1afe, v1adc
    0x1b2b: JUMP v3bf(0x32e6)

    Begin block 0x32e6
    prev=[0x1acc], succ=[]
    =================================
    0x32e7: STOP 

}

function unlock()() public {
    Begin block 0x3d2
    prev=[], succ=[0x3da, 0x3de]
    =================================
    0x3d3: v3d3 = CALLVALUE 
    0x3d5: v3d5 = ISZERO v3d3
    0x3d6: v3d6(0x3de) = CONST 
    0x3d9: JUMPI v3d6(0x3de), v3d5

    Begin block 0x3da
    prev=[0x3d2], succ=[]
    =================================
    0x3da: v3da(0x0) = CONST 
    0x3dd: REVERT v3da(0x0), v3da(0x0)

    Begin block 0x3de
    prev=[0x3d2], succ=[0x1b2c]
    =================================
    0x3e0: v3e0(0x3307) = CONST 
    0x3e3: v3e3(0x1b2c) = CONST 
    0x3e6: JUMP v3e3(0x1b2c)

    Begin block 0x1b2c
    prev=[0x3de], succ=[0x1b3f, 0x1b43]
    =================================
    0x1b2d: v1b2d(0x0) = CONST 
    0x1b2f: v1b2f = SLOAD v1b2d(0x0)
    0x1b30: v1b30(0x1) = CONST 
    0x1b32: v1b32(0xa0) = CONST 
    0x1b34: v1b34(0x2) = CONST 
    0x1b36: v1b36(0x10000000000000000000000000000000000000000) = EXP v1b34(0x2), v1b32(0xa0)
    0x1b37: v1b37(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b36(0x10000000000000000000000000000000000000000), v1b30(0x1)
    0x1b38: v1b38 = AND v1b37(0xffffffffffffffffffffffffffffffffffffffff), v1b2f
    0x1b39: v1b39 = CALLER 
    0x1b3a: v1b3a = EQ v1b39, v1b38
    0x1b3b: v1b3b(0x1b43) = CONST 
    0x1b3e: JUMPI v1b3b(0x1b43), v1b3a

    Begin block 0x1b3f
    prev=[0x1b2c], succ=[]
    =================================
    0x1b3f: v1b3f(0x0) = CONST 
    0x1b42: REVERT v1b3f(0x0), v1b3f(0x0)

    Begin block 0x1b43
    prev=[0x1b2c], succ=[0x3307]
    =================================
    0x1b44: v1b44(0x1) = CONST 
    0x1b47: v1b47 = SLOAD v1b44(0x1)
    0x1b48: v1b48(0xff000000000000000000000000000000000000000000) = CONST 
    0x1b5f: v1b5f(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v1b48(0xff000000000000000000000000000000000000000000)
    0x1b60: v1b60 = AND v1b5f(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v1b47
    0x1b61: v1b61(0x1000000000000000000000000000000000000000000) = CONST 
    0x1b78: v1b78 = OR v1b61(0x1000000000000000000000000000000000000000000), v1b60
    0x1b7a: SSTORE v1b44(0x1), v1b78
    0x1b7b: v1b7b(0x40) = CONST 
    0x1b7d: v1b7d = MLOAD v1b7b(0x40)
    0x1b7e: v1b7e(0x19aad37188a1d3921e29eb3c66acf43d81975e107cb650d58cca878627955fd6) = CONST 
    0x1ba0: v1ba0(0x0) = CONST 
    0x1ba3: LOG1 v1b7d, v1ba0(0x0), v1b7e(0x19aad37188a1d3921e29eb3c66acf43d81975e107cb650d58cca878627955fd6)
    0x1ba4: JUMP v3e0(0x3307)

    Begin block 0x3307
    prev=[0x1b43], succ=[]
    =================================
    0x3308: STOP 

}

function transfer(address,uint256)() public {
    Begin block 0x3e7
    prev=[], succ=[0x3ef, 0x3f3]
    =================================
    0x3e8: v3e8 = CALLVALUE 
    0x3ea: v3ea = ISZERO v3e8
    0x3eb: v3eb(0x3f3) = CONST 
    0x3ee: JUMPI v3eb(0x3f3), v3ea

    Begin block 0x3ef
    prev=[0x3e7], succ=[]
    =================================
    0x3ef: v3ef(0x0) = CONST 
    0x3f2: REVERT v3ef(0x0), v3ef(0x0)

    Begin block 0x3f3
    prev=[0x3e7], succ=[0x1ba5]
    =================================
    0x3f5: v3f5(0x3328) = CONST 
    0x3f8: v3f8(0x1) = CONST 
    0x3fa: v3fa(0xa0) = CONST 
    0x3fc: v3fc(0x2) = CONST 
    0x3fe: v3fe(0x10000000000000000000000000000000000000000) = EXP v3fc(0x2), v3fa(0xa0)
    0x3ff: v3ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fe(0x10000000000000000000000000000000000000000), v3f8(0x1)
    0x400: v400(0x4) = CONST 
    0x402: v402 = CALLDATALOAD v400(0x4)
    0x403: v403 = AND v402, v3ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x404: v404(0x24) = CONST 
    0x406: v406 = CALLDATALOAD v404(0x24)
    0x407: v407(0x1ba5) = CONST 
    0x40a: JUMP v407(0x1ba5)

    Begin block 0x1ba5
    prev=[0x3f3], succ=[0x1bf4, 0x1bf8]
    =================================
    0x1ba6: v1ba6(0x3) = CONST 
    0x1ba8: v1ba8 = SLOAD v1ba6(0x3)
    0x1ba9: v1ba9(0x40) = CONST 
    0x1bac: v1bac = MLOAD v1ba9(0x40)
    0x1bad: v1bad(0xe0) = CONST 
    0x1baf: v1baf(0x2) = CONST 
    0x1bb1: v1bb1(0x100000000000000000000000000000000000000000000000000000000) = EXP v1baf(0x2), v1bad(0xe0)
    0x1bb2: v1bb2(0x7ccce851) = CONST 
    0x1bb7: v1bb7(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1bb2(0x7ccce851), v1bb1(0x100000000000000000000000000000000000000000000000000000000)
    0x1bb9: MSTORE v1bac, v1bb7(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1bba: v1bba(0x1) = CONST 
    0x1bbc: v1bbc(0xa0) = CONST 
    0x1bbe: v1bbe(0x2) = CONST 
    0x1bc0: v1bc0(0x10000000000000000000000000000000000000000) = EXP v1bbe(0x2), v1bbc(0xa0)
    0x1bc1: v1bc1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1bc0(0x10000000000000000000000000000000000000000), v1bba(0x1)
    0x1bc4: v1bc4 = AND v403, v1bc1(0xffffffffffffffffffffffffffffffffffffffff)
    0x1bc5: v1bc5(0x4) = CONST 
    0x1bc8: v1bc8 = ADD v1bac, v1bc5(0x4)
    0x1bc9: MSTORE v1bc8, v1bc4
    0x1bcb: v1bcb = MLOAD v1ba9(0x40)
    0x1bcc: v1bcc(0x0) = CONST 
    0x1bd1: v1bd1 = AND v1bc1(0xffffffffffffffffffffffffffffffffffffffff), v1ba8
    0x1bd3: v1bd3(0x7ccce851) = CONST 
    0x1bd9: v1bd9(0x24) = CONST 
    0x1bdd: v1bdd = ADD v1bac, v1bd9(0x24)
    0x1bdf: v1bdf(0x20) = CONST 
    0x1be6: v1be6(0x0) = SUB v1bac, v1bcb
    0x1be7: v1be7(0x24) = ADD v1be6(0x0), v1bd9(0x24)
    0x1bec: v1bec = EXTCODESIZE v1bd1
    0x1bed: v1bed = ISZERO v1bec
    0x1bef: v1bef = ISZERO v1bed
    0x1bf0: v1bf0(0x1bf8) = CONST 
    0x1bf3: JUMPI v1bf0(0x1bf8), v1bef

    Begin block 0x1bf4
    prev=[0x1ba5], succ=[]
    =================================
    0x1bf4: v1bf4(0x0) = CONST 
    0x1bf7: REVERT v1bf4(0x0), v1bf4(0x0)

    Begin block 0x1bf8
    prev=[0x1ba5], succ=[0x1c03, 0x1c0c]
    =================================
    0x1bfa: v1bfa = GAS 
    0x1bfb: v1bfb = CALL v1bfa, v1bd1, v1bcc(0x0), v1bcb, v1be7(0x24), v1bcb, v1bdf(0x20)
    0x1bfc: v1bfc = ISZERO v1bfb
    0x1bfe: v1bfe = ISZERO v1bfc
    0x1bff: v1bff(0x1c0c) = CONST 
    0x1c02: JUMPI v1bff(0x1c0c), v1bfe

    Begin block 0x1c03
    prev=[0x1bf8], succ=[]
    =================================
    0x1c03: v1c03 = RETURNDATASIZE 
    0x1c04: v1c04(0x0) = CONST 
    0x1c07: RETURNDATACOPY v1c04(0x0), v1c04(0x0), v1c03
    0x1c08: v1c08 = RETURNDATASIZE 
    0x1c09: v1c09(0x0) = CONST 
    0x1c0b: REVERT v1c09(0x0), v1c08

    Begin block 0x1c0c
    prev=[0x1bf8], succ=[0x1c1e, 0x1c22]
    =================================
    0x1c11: v1c11(0x40) = CONST 
    0x1c13: v1c13 = MLOAD v1c11(0x40)
    0x1c14: v1c14 = RETURNDATASIZE 
    0x1c15: v1c15(0x20) = CONST 
    0x1c18: v1c18 = LT v1c14, v1c15(0x20)
    0x1c19: v1c19 = ISZERO v1c18
    0x1c1a: v1c1a(0x1c22) = CONST 
    0x1c1d: JUMPI v1c1a(0x1c22), v1c19

    Begin block 0x1c1e
    prev=[0x1c0c], succ=[]
    =================================
    0x1c1e: v1c1e(0x0) = CONST 
    0x1c21: REVERT v1c1e(0x0), v1c1e(0x0)

    Begin block 0x1c22
    prev=[0x1c0c], succ=[0x1c2a, 0x1c67]
    =================================
    0x1c24: v1c24 = MLOAD v1c13
    0x1c25: v1c25 = ISZERO v1c24
    0x1c26: v1c26(0x1c67) = CONST 
    0x1c29: JUMPI v1c26(0x1c67), v1c25

    Begin block 0x1c2a
    prev=[0x1c22], succ=[]
    =================================
    0x1c2a: v1c2a(0x40) = CONST 
    0x1c2d: v1c2d = MLOAD v1c2a(0x40)
    0x1c2e: v1c2e(0xe5) = CONST 
    0x1c30: v1c30(0x2) = CONST 
    0x1c32: v1c32(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1c30(0x2), v1c2e(0xe5)
    0x1c33: v1c33(0x461bcd) = CONST 
    0x1c37: v1c37(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1c33(0x461bcd), v1c32(0x2000000000000000000000000000000000000000000000000000000000)
    0x1c39: MSTORE v1c2d, v1c37(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c3a: v1c3a(0x20) = CONST 
    0x1c3c: v1c3c(0x4) = CONST 
    0x1c3f: v1c3f = ADD v1c2d, v1c3c(0x4)
    0x1c40: MSTORE v1c3f, v1c3a(0x20)
    0x1c41: v1c41(0x1c) = CONST 
    0x1c43: v1c43(0x24) = CONST 
    0x1c46: v1c46 = ADD v1c2d, v1c43(0x24)
    0x1c47: MSTORE v1c46, v1c41(0x1c)
    0x1c48: v1c48(0x0) = CONST 
    0x1c4b: v1c4b = MLOAD v1c48(0x0)
    0x1c4c: v1c4c(0x20) = CONST 
    0x1c4e: v1c4e(0x2f6a) = CONST 
    0x1c56: MSTORE v1c48(0x0), v1c4b
    0x1c57: v1c57(0x44) = CONST 
    0x1c5a: v1c5a = ADD v1c2d, v1c57(0x44)
    0x1c5b: MSTORE v1c5a, v368a(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x1c5d: v1c5d = MLOAD v1c2a(0x40)
    0x1c61: v1c61(0x0) = SUB v1c2d, v1c5d
    0x1c62: v1c62(0x64) = CONST 
    0x1c64: v1c64(0x64) = ADD v1c62(0x64), v1c61(0x0)
    0x1c66: REVERT v1c5d, v1c64(0x64)
    0x368a: v368a(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x1c67
    prev=[0x1c22], succ=[0x1cb5, 0x1cb9]
    =================================
    0x1c68: v1c68(0x3) = CONST 
    0x1c6a: v1c6a = SLOAD v1c68(0x3)
    0x1c6b: v1c6b(0x40) = CONST 
    0x1c6e: v1c6e = MLOAD v1c6b(0x40)
    0x1c6f: v1c6f(0xe0) = CONST 
    0x1c71: v1c71(0x2) = CONST 
    0x1c73: v1c73(0x100000000000000000000000000000000000000000000000000000000) = EXP v1c71(0x2), v1c6f(0xe0)
    0x1c74: v1c74(0x7ccce851) = CONST 
    0x1c79: v1c79(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1c74(0x7ccce851), v1c73(0x100000000000000000000000000000000000000000000000000000000)
    0x1c7b: MSTORE v1c6e, v1c79(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1c7c: v1c7c = CALLER 
    0x1c7d: v1c7d(0x4) = CONST 
    0x1c80: v1c80 = ADD v1c6e, v1c7d(0x4)
    0x1c83: MSTORE v1c80, v1c7c
    0x1c85: v1c85 = MLOAD v1c6b(0x40)
    0x1c88: v1c88(0x1) = CONST 
    0x1c8a: v1c8a(0xa0) = CONST 
    0x1c8c: v1c8c(0x2) = CONST 
    0x1c8e: v1c8e(0x10000000000000000000000000000000000000000) = EXP v1c8c(0x2), v1c8a(0xa0)
    0x1c8f: v1c8f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1c8e(0x10000000000000000000000000000000000000000), v1c88(0x1)
    0x1c90: v1c90 = AND v1c8f(0xffffffffffffffffffffffffffffffffffffffff), v1c6a
    0x1c92: v1c92(0x7ccce851) = CONST 
    0x1c98: v1c98(0x24) = CONST 
    0x1c9c: v1c9c = ADD v1c6e, v1c98(0x24)
    0x1c9e: v1c9e(0x20) = CONST 
    0x1ca6: v1ca6(0x0) = SUB v1c6e, v1c85
    0x1ca7: v1ca7(0x24) = ADD v1ca6(0x0), v1c98(0x24)
    0x1ca9: v1ca9(0x0) = CONST 
    0x1cad: v1cad = EXTCODESIZE v1c90
    0x1cae: v1cae = ISZERO v1cad
    0x1cb0: v1cb0 = ISZERO v1cae
    0x1cb1: v1cb1(0x1cb9) = CONST 
    0x1cb4: JUMPI v1cb1(0x1cb9), v1cb0

    Begin block 0x1cb5
    prev=[0x1c67], succ=[]
    =================================
    0x1cb5: v1cb5(0x0) = CONST 
    0x1cb8: REVERT v1cb5(0x0), v1cb5(0x0)

    Begin block 0x1cb9
    prev=[0x1c67], succ=[0x1cc4, 0x1ccd]
    =================================
    0x1cbb: v1cbb = GAS 
    0x1cbc: v1cbc = CALL v1cbb, v1c90, v1ca9(0x0), v1c85, v1ca7(0x24), v1c85, v1c9e(0x20)
    0x1cbd: v1cbd = ISZERO v1cbc
    0x1cbf: v1cbf = ISZERO v1cbd
    0x1cc0: v1cc0(0x1ccd) = CONST 
    0x1cc3: JUMPI v1cc0(0x1ccd), v1cbf

    Begin block 0x1cc4
    prev=[0x1cb9], succ=[]
    =================================
    0x1cc4: v1cc4 = RETURNDATASIZE 
    0x1cc5: v1cc5(0x0) = CONST 
    0x1cc8: RETURNDATACOPY v1cc5(0x0), v1cc5(0x0), v1cc4
    0x1cc9: v1cc9 = RETURNDATASIZE 
    0x1cca: v1cca(0x0) = CONST 
    0x1ccc: REVERT v1cca(0x0), v1cc9

    Begin block 0x1ccd
    prev=[0x1cb9], succ=[0x1cdf, 0x1ce3]
    =================================
    0x1cd2: v1cd2(0x40) = CONST 
    0x1cd4: v1cd4 = MLOAD v1cd2(0x40)
    0x1cd5: v1cd5 = RETURNDATASIZE 
    0x1cd6: v1cd6(0x20) = CONST 
    0x1cd9: v1cd9 = LT v1cd5, v1cd6(0x20)
    0x1cda: v1cda = ISZERO v1cd9
    0x1cdb: v1cdb(0x1ce3) = CONST 
    0x1cde: JUMPI v1cdb(0x1ce3), v1cda

    Begin block 0x1cdf
    prev=[0x1ccd], succ=[]
    =================================
    0x1cdf: v1cdf(0x0) = CONST 
    0x1ce2: REVERT v1cdf(0x0), v1cdf(0x0)

    Begin block 0x1ce3
    prev=[0x1ccd], succ=[0x1ceb, 0x1d28]
    =================================
    0x1ce5: v1ce5 = MLOAD v1cd4
    0x1ce6: v1ce6 = ISZERO v1ce5
    0x1ce7: v1ce7(0x1d28) = CONST 
    0x1cea: JUMPI v1ce7(0x1d28), v1ce6

    Begin block 0x1ceb
    prev=[0x1ce3], succ=[]
    =================================
    0x1ceb: v1ceb(0x40) = CONST 
    0x1cee: v1cee = MLOAD v1ceb(0x40)
    0x1cef: v1cef(0xe5) = CONST 
    0x1cf1: v1cf1(0x2) = CONST 
    0x1cf3: v1cf3(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1cf1(0x2), v1cef(0xe5)
    0x1cf4: v1cf4(0x461bcd) = CONST 
    0x1cf8: v1cf8(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1cf4(0x461bcd), v1cf3(0x2000000000000000000000000000000000000000000000000000000000)
    0x1cfa: MSTORE v1cee, v1cf8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cfb: v1cfb(0x20) = CONST 
    0x1cfd: v1cfd(0x4) = CONST 
    0x1d00: v1d00 = ADD v1cee, v1cfd(0x4)
    0x1d01: MSTORE v1d00, v1cfb(0x20)
    0x1d02: v1d02(0x1c) = CONST 
    0x1d04: v1d04(0x24) = CONST 
    0x1d07: v1d07 = ADD v1cee, v1d04(0x24)
    0x1d08: MSTORE v1d07, v1d02(0x1c)
    0x1d09: v1d09(0x0) = CONST 
    0x1d0c: v1d0c = MLOAD v1d09(0x0)
    0x1d0d: v1d0d(0x20) = CONST 
    0x1d0f: v1d0f(0x2f6a) = CONST 
    0x1d17: MSTORE v1d09(0x0), v1d0c
    0x1d18: v1d18(0x44) = CONST 
    0x1d1b: v1d1b = ADD v1cee, v1d18(0x44)
    0x1d1c: MSTORE v1d1b, v368f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x1d1e: v1d1e = MLOAD v1ceb(0x40)
    0x1d22: v1d22(0x0) = SUB v1cee, v1d1e
    0x1d23: v1d23(0x64) = CONST 
    0x1d25: v1d25(0x64) = ADD v1d23(0x64), v1d22(0x0)
    0x1d27: REVERT v1d1e, v1d25(0x64)
    0x368f: v368f(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x1d28
    prev=[0x1ce3], succ=[0x1d3b, 0x1d3f]
    =================================
    0x1d29: v1d29(0x1) = CONST 
    0x1d2b: v1d2b = SLOAD v1d29(0x1)
    0x1d2c: v1d2c(0xa0) = CONST 
    0x1d2e: v1d2e(0x2) = CONST 
    0x1d30: v1d30(0x10000000000000000000000000000000000000000) = EXP v1d2e(0x2), v1d2c(0xa0)
    0x1d32: v1d32 = DIV v1d2b, v1d30(0x10000000000000000000000000000000000000000)
    0x1d33: v1d33(0xff) = CONST 
    0x1d35: v1d35 = AND v1d33(0xff), v1d32
    0x1d36: v1d36 = ISZERO v1d35
    0x1d37: v1d37(0x1d3f) = CONST 
    0x1d3a: JUMPI v1d37(0x1d3f), v1d36

    Begin block 0x1d3b
    prev=[0x1d28], succ=[]
    =================================
    0x1d3b: v1d3b(0x0) = CONST 
    0x1d3e: REVERT v1d3b(0x0), v1d3b(0x0)

    Begin block 0x1d3f
    prev=[0x1d28], succ=[0x3566]
    =================================
    0x1d40: v1d40(0x3566) = CONST 
    0x1d44: v1d44 = CALLER 
    0x1d46: v1d46(0x24ff) = CONST 
    0x1d49: CALLPRIVATE v1d46(0x24ff), v406, v1d44, v403, v1d40(0x3566)

    Begin block 0x3566
    prev=[0x1d3f], succ=[0x3328]
    =================================
    0x3568: v3568(0x1) = CONST 
    0x3570: JUMP v3f5(0x3328)

    Begin block 0x3328
    prev=[0x3566], succ=[]
    =================================
    0x3329: v3329(0x40) = CONST 
    0x332c: v332c = MLOAD v3329(0x40)
    0x332e: v332e = ISZERO v3568(0x1)
    0x332f: v332f = ISZERO v332e
    0x3331: MSTORE v332c, v332f
    0x3332: v3332 = MLOAD v3329(0x40)
    0x3336: v3336(0x0) = SUB v332c, v3332
    0x3337: v3337(0x20) = CONST 
    0x3339: v3339(0x20) = ADD v3337(0x20), v3336(0x0)
    0x333b: RETURN v3332, v3339(0x20)

}

function tokenStorage()() public {
    Begin block 0x40b
    prev=[], succ=[0x413, 0x417]
    =================================
    0x40c: v40c = CALLVALUE 
    0x40e: v40e = ISZERO v40c
    0x40f: v40f(0x417) = CONST 
    0x412: JUMPI v40f(0x417), v40e

    Begin block 0x413
    prev=[0x40b], succ=[]
    =================================
    0x413: v413(0x0) = CONST 
    0x416: REVERT v413(0x0), v413(0x0)

    Begin block 0x417
    prev=[0x40b], succ=[0x1d4a]
    =================================
    0x419: v419(0x335b) = CONST 
    0x41c: v41c(0x1d4a) = CONST 
    0x41f: JUMP v41c(0x1d4a)

    Begin block 0x1d4a
    prev=[0x417], succ=[0x335b]
    =================================
    0x1d4b: v1d4b(0x2) = CONST 
    0x1d4d: v1d4d = SLOAD v1d4b(0x2)
    0x1d4e: v1d4e(0x1) = CONST 
    0x1d50: v1d50(0xa0) = CONST 
    0x1d52: v1d52(0x2) = CONST 
    0x1d54: v1d54(0x10000000000000000000000000000000000000000) = EXP v1d52(0x2), v1d50(0xa0)
    0x1d55: v1d55(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d54(0x10000000000000000000000000000000000000000), v1d4e(0x1)
    0x1d56: v1d56 = AND v1d55(0xffffffffffffffffffffffffffffffffffffffff), v1d4d
    0x1d58: JUMP v419(0x335b)

    Begin block 0x335b
    prev=[0x1d4a], succ=[]
    =================================
    0x335c: v335c(0x40) = CONST 
    0x335f: v335f = MLOAD v335c(0x40)
    0x3360: v3360(0x1) = CONST 
    0x3362: v3362(0xa0) = CONST 
    0x3364: v3364(0x2) = CONST 
    0x3366: v3366(0x10000000000000000000000000000000000000000) = EXP v3364(0x2), v3362(0xa0)
    0x3367: v3367(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3366(0x10000000000000000000000000000000000000000), v3360(0x1)
    0x336a: v336a = AND v1d56, v3367(0xffffffffffffffffffffffffffffffffffffffff)
    0x336c: MSTORE v335f, v336a
    0x336d: v336d = MLOAD v335c(0x40)
    0x3371: v3371(0x0) = SUB v335f, v336d
    0x3372: v3372(0x20) = CONST 
    0x3374: v3374(0x20) = ADD v3372(0x20), v3371(0x0)
    0x3376: RETURN v336d, v3374(0x20)

}

function destroyBlacklistedTokens(address,uint256)() public {
    Begin block 0x420
    prev=[], succ=[0x428, 0x42c]
    =================================
    0x421: v421 = CALLVALUE 
    0x423: v423 = ISZERO v421
    0x424: v424(0x42c) = CONST 
    0x427: JUMPI v424(0x42c), v423

    Begin block 0x428
    prev=[0x420], succ=[]
    =================================
    0x428: v428(0x0) = CONST 
    0x42b: REVERT v428(0x0), v428(0x0)

    Begin block 0x42c
    prev=[0x420], succ=[0x1d59]
    =================================
    0x42e: v42e(0x3396) = CONST 
    0x431: v431(0x1) = CONST 
    0x433: v433(0xa0) = CONST 
    0x435: v435(0x2) = CONST 
    0x437: v437(0x10000000000000000000000000000000000000000) = EXP v435(0x2), v433(0xa0)
    0x438: v438(0xffffffffffffffffffffffffffffffffffffffff) = SUB v437(0x10000000000000000000000000000000000000000), v431(0x1)
    0x439: v439(0x4) = CONST 
    0x43b: v43b = CALLDATALOAD v439(0x4)
    0x43c: v43c = AND v43b, v438(0xffffffffffffffffffffffffffffffffffffffff)
    0x43d: v43d(0x24) = CONST 
    0x43f: v43f = CALLDATALOAD v43d(0x24)
    0x440: v440(0x1d59) = CONST 
    0x443: JUMP v440(0x1d59)

    Begin block 0x1d59
    prev=[0x42c], succ=[0x1daa, 0x1dae]
    =================================
    0x1d5a: v1d5a(0x3) = CONST 
    0x1d5c: v1d5c = SLOAD v1d5a(0x3)
    0x1d5d: v1d5d(0x40) = CONST 
    0x1d60: v1d60 = MLOAD v1d5d(0x40)
    0x1d61: v1d61(0xe0) = CONST 
    0x1d63: v1d63(0x2) = CONST 
    0x1d65: v1d65(0x100000000000000000000000000000000000000000000000000000000) = EXP v1d63(0x2), v1d61(0xe0)
    0x1d66: v1d66(0x7ccce851) = CONST 
    0x1d6b: v1d6b(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v1d66(0x7ccce851), v1d65(0x100000000000000000000000000000000000000000000000000000000)
    0x1d6d: MSTORE v1d60, v1d6b(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x1d6e: v1d6e(0x1) = CONST 
    0x1d70: v1d70(0xa0) = CONST 
    0x1d72: v1d72(0x2) = CONST 
    0x1d74: v1d74(0x10000000000000000000000000000000000000000) = EXP v1d72(0x2), v1d70(0xa0)
    0x1d75: v1d75(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d74(0x10000000000000000000000000000000000000000), v1d6e(0x1)
    0x1d78: v1d78 = AND v43c, v1d75(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d79: v1d79(0x4) = CONST 
    0x1d7c: v1d7c = ADD v1d60, v1d79(0x4)
    0x1d7d: MSTORE v1d7c, v1d78
    0x1d7f: v1d7f = MLOAD v1d5d(0x40)
    0x1d85: v1d85 = AND v1d5c, v1d75(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d87: v1d87(0x7ccce851) = CONST 
    0x1d8d: v1d8d(0x24) = CONST 
    0x1d91: v1d91 = ADD v1d60, v1d8d(0x24)
    0x1d93: v1d93(0x20) = CONST 
    0x1d9b: v1d9b(0x0) = SUB v1d60, v1d7f
    0x1d9c: v1d9c(0x24) = ADD v1d9b(0x0), v1d8d(0x24)
    0x1d9e: v1d9e(0x0) = CONST 
    0x1da2: v1da2 = EXTCODESIZE v1d85
    0x1da3: v1da3 = ISZERO v1da2
    0x1da5: v1da5 = ISZERO v1da3
    0x1da6: v1da6(0x1dae) = CONST 
    0x1da9: JUMPI v1da6(0x1dae), v1da5

    Begin block 0x1daa
    prev=[0x1d59], succ=[]
    =================================
    0x1daa: v1daa(0x0) = CONST 
    0x1dad: REVERT v1daa(0x0), v1daa(0x0)

    Begin block 0x1dae
    prev=[0x1d59], succ=[0x1db9, 0x1dc2]
    =================================
    0x1db0: v1db0 = GAS 
    0x1db1: v1db1 = CALL v1db0, v1d85, v1d9e(0x0), v1d7f, v1d9c(0x24), v1d7f, v1d93(0x20)
    0x1db2: v1db2 = ISZERO v1db1
    0x1db4: v1db4 = ISZERO v1db2
    0x1db5: v1db5(0x1dc2) = CONST 
    0x1db8: JUMPI v1db5(0x1dc2), v1db4

    Begin block 0x1db9
    prev=[0x1dae], succ=[]
    =================================
    0x1db9: v1db9 = RETURNDATASIZE 
    0x1dba: v1dba(0x0) = CONST 
    0x1dbd: RETURNDATACOPY v1dba(0x0), v1dba(0x0), v1db9
    0x1dbe: v1dbe = RETURNDATASIZE 
    0x1dbf: v1dbf(0x0) = CONST 
    0x1dc1: REVERT v1dbf(0x0), v1dbe

    Begin block 0x1dc2
    prev=[0x1dae], succ=[0x1dd4, 0x1dd8]
    =================================
    0x1dc7: v1dc7(0x40) = CONST 
    0x1dc9: v1dc9 = MLOAD v1dc7(0x40)
    0x1dca: v1dca = RETURNDATASIZE 
    0x1dcb: v1dcb(0x20) = CONST 
    0x1dce: v1dce = LT v1dca, v1dcb(0x20)
    0x1dcf: v1dcf = ISZERO v1dce
    0x1dd0: v1dd0(0x1dd8) = CONST 
    0x1dd3: JUMPI v1dd0(0x1dd8), v1dcf

    Begin block 0x1dd4
    prev=[0x1dc2], succ=[]
    =================================
    0x1dd4: v1dd4(0x0) = CONST 
    0x1dd7: REVERT v1dd4(0x0), v1dd4(0x0)

    Begin block 0x1dd8
    prev=[0x1dc2], succ=[0x1de1, 0x1e30]
    =================================
    0x1dda: v1dda = MLOAD v1dc9
    0x1ddb: v1ddb = ISZERO v1dda
    0x1ddc: v1ddc = ISZERO v1ddb
    0x1ddd: v1ddd(0x1e30) = CONST 
    0x1de0: JUMPI v1ddd(0x1e30), v1ddc

    Begin block 0x1de1
    prev=[0x1dd8], succ=[]
    =================================
    0x1de1: v1de1(0x40) = CONST 
    0x1de4: v1de4 = MLOAD v1de1(0x40)
    0x1de5: v1de5(0xe5) = CONST 
    0x1de7: v1de7(0x2) = CONST 
    0x1de9: v1de9(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1de7(0x2), v1de5(0xe5)
    0x1dea: v1dea(0x461bcd) = CONST 
    0x1dee: v1dee(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1dea(0x461bcd), v1de9(0x2000000000000000000000000000000000000000000000000000000000)
    0x1df0: MSTORE v1de4, v1dee(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1df1: v1df1(0x20) = CONST 
    0x1df3: v1df3(0x4) = CONST 
    0x1df6: v1df6 = ADD v1de4, v1df3(0x4)
    0x1df7: MSTORE v1df6, v1df1(0x20)
    0x1df8: v1df8(0x18) = CONST 
    0x1dfa: v1dfa(0x24) = CONST 
    0x1dfd: v1dfd = ADD v1de4, v1dfa(0x24)
    0x1dfe: MSTORE v1dfd, v1df8(0x18)
    0x1dff: v1dff(0x55736572206d75737420626520626c61636b6c69737465640000000000000000) = CONST 
    0x1e20: v1e20(0x44) = CONST 
    0x1e23: v1e23 = ADD v1de4, v1e20(0x44)
    0x1e24: MSTORE v1e23, v1dff(0x55736572206d75737420626520626c61636b6c69737465640000000000000000)
    0x1e26: v1e26 = MLOAD v1de1(0x40)
    0x1e2a: v1e2a(0x0) = SUB v1de4, v1e26
    0x1e2b: v1e2b(0x64) = CONST 
    0x1e2d: v1e2d(0x64) = ADD v1e2b(0x64), v1e2a(0x0)
    0x1e2f: REVERT v1e26, v1e2d(0x64)

    Begin block 0x1e30
    prev=[0x1dd8], succ=[0x1e43, 0x1e47]
    =================================
    0x1e31: v1e31(0x1) = CONST 
    0x1e33: v1e33 = SLOAD v1e31(0x1)
    0x1e34: v1e34(0xa0) = CONST 
    0x1e36: v1e36(0x2) = CONST 
    0x1e38: v1e38(0x10000000000000000000000000000000000000000) = EXP v1e36(0x2), v1e34(0xa0)
    0x1e3a: v1e3a = DIV v1e33, v1e38(0x10000000000000000000000000000000000000000)
    0x1e3b: v1e3b(0xff) = CONST 
    0x1e3d: v1e3d = AND v1e3b(0xff), v1e3a
    0x1e3e: v1e3e = ISZERO v1e3d
    0x1e3f: v1e3f(0x1e47) = CONST 
    0x1e42: JUMPI v1e3f(0x1e47), v1e3e

    Begin block 0x1e43
    prev=[0x1e30], succ=[]
    =================================
    0x1e43: v1e43(0x0) = CONST 
    0x1e46: REVERT v1e43(0x0), v1e43(0x0)

    Begin block 0x1e47
    prev=[0x1e30], succ=[0x1ea7, 0x1eab]
    =================================
    0x1e48: v1e48(0x3) = CONST 
    0x1e4a: v1e4a = SLOAD v1e48(0x3)
    0x1e4b: v1e4b(0x40) = CONST 
    0x1e4e: v1e4e = MLOAD v1e4b(0x40)
    0x1e4f: v1e4f(0xe3) = CONST 
    0x1e51: v1e51(0x2) = CONST 
    0x1e53: v1e53(0x800000000000000000000000000000000000000000000000000000000) = EXP v1e51(0x2), v1e4f(0xe3)
    0x1e54: v1e54(0x29b6dab) = CONST 
    0x1e59: v1e59(0x14db6d5800000000000000000000000000000000000000000000000000000000) = MUL v1e54(0x29b6dab), v1e53(0x800000000000000000000000000000000000000000000000000000000)
    0x1e5b: MSTORE v1e4e, v1e59(0x14db6d5800000000000000000000000000000000000000000000000000000000)
    0x1e5c: v1e5c = CALLER 
    0x1e5d: v1e5d(0x4) = CONST 
    0x1e60: v1e60 = ADD v1e4e, v1e5d(0x4)
    0x1e61: MSTORE v1e60, v1e5c
    0x1e62: v1e62(0x0) = CONST 
    0x1e65: v1e65 = CALLDATALOAD v1e62(0x0)
    0x1e66: v1e66(0x1) = CONST 
    0x1e68: v1e68(0xe0) = CONST 
    0x1e6a: v1e6a(0x2) = CONST 
    0x1e6c: v1e6c(0x100000000000000000000000000000000000000000000000000000000) = EXP v1e6a(0x2), v1e68(0xe0)
    0x1e6d: v1e6d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1e6c(0x100000000000000000000000000000000000000000000000000000000), v1e66(0x1)
    0x1e6e: v1e6e(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1e6d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1e6f: v1e6f = AND v1e6e(0xffffffff00000000000000000000000000000000000000000000000000000000), v1e65
    0x1e70: v1e70(0x24) = CONST 
    0x1e73: v1e73 = ADD v1e4e, v1e70(0x24)
    0x1e74: MSTORE v1e73, v1e6f
    0x1e76: v1e76 = MLOAD v1e4b(0x40)
    0x1e77: v1e77(0x1) = CONST 
    0x1e79: v1e79(0xa0) = CONST 
    0x1e7b: v1e7b(0x2) = CONST 
    0x1e7d: v1e7d(0x10000000000000000000000000000000000000000) = EXP v1e7b(0x2), v1e79(0xa0)
    0x1e7e: v1e7e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e7d(0x10000000000000000000000000000000000000000), v1e77(0x1)
    0x1e81: v1e81 = AND v1e4a, v1e7e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e83: v1e83(0x14db6d58) = CONST 
    0x1e89: v1e89(0x44) = CONST 
    0x1e8d: v1e8d = ADD v1e4e, v1e89(0x44)
    0x1e8f: v1e8f(0x20) = CONST 
    0x1e96: v1e96(0x0) = SUB v1e4e, v1e76
    0x1e99: v1e99(0x44) = ADD v1e89(0x44), v1e96(0x0)
    0x1e9f: v1e9f = EXTCODESIZE v1e81
    0x1ea0: v1ea0 = ISZERO v1e9f
    0x1ea2: v1ea2 = ISZERO v1ea0
    0x1ea3: v1ea3(0x1eab) = CONST 
    0x1ea6: JUMPI v1ea3(0x1eab), v1ea2

    Begin block 0x1ea7
    prev=[0x1e47], succ=[]
    =================================
    0x1ea7: v1ea7(0x0) = CONST 
    0x1eaa: REVERT v1ea7(0x0), v1ea7(0x0)

    Begin block 0x1eab
    prev=[0x1e47], succ=[0x1eb6, 0x1ebf]
    =================================
    0x1ead: v1ead = GAS 
    0x1eae: v1eae = CALL v1ead, v1e81, v1e62(0x0), v1e76, v1e99(0x44), v1e76, v1e8f(0x20)
    0x1eaf: v1eaf = ISZERO v1eae
    0x1eb1: v1eb1 = ISZERO v1eaf
    0x1eb2: v1eb2(0x1ebf) = CONST 
    0x1eb5: JUMPI v1eb2(0x1ebf), v1eb1

    Begin block 0x1eb6
    prev=[0x1eab], succ=[]
    =================================
    0x1eb6: v1eb6 = RETURNDATASIZE 
    0x1eb7: v1eb7(0x0) = CONST 
    0x1eba: RETURNDATACOPY v1eb7(0x0), v1eb7(0x0), v1eb6
    0x1ebb: v1ebb = RETURNDATASIZE 
    0x1ebc: v1ebc(0x0) = CONST 
    0x1ebe: REVERT v1ebc(0x0), v1ebb

    Begin block 0x1ebf
    prev=[0x1eab], succ=[0x1ed1, 0x1ed5]
    =================================
    0x1ec4: v1ec4(0x40) = CONST 
    0x1ec6: v1ec6 = MLOAD v1ec4(0x40)
    0x1ec7: v1ec7 = RETURNDATASIZE 
    0x1ec8: v1ec8(0x20) = CONST 
    0x1ecb: v1ecb = LT v1ec7, v1ec8(0x20)
    0x1ecc: v1ecc = ISZERO v1ecb
    0x1ecd: v1ecd(0x1ed5) = CONST 
    0x1ed0: JUMPI v1ecd(0x1ed5), v1ecc

    Begin block 0x1ed1
    prev=[0x1ebf], succ=[]
    =================================
    0x1ed1: v1ed1(0x0) = CONST 
    0x1ed4: REVERT v1ed1(0x0), v1ed1(0x0)

    Begin block 0x1ed5
    prev=[0x1ebf], succ=[0x1ede, 0x1f2f]
    =================================
    0x1ed7: v1ed7 = MLOAD v1ec6
    0x1ed8: v1ed8 = ISZERO v1ed7
    0x1ed9: v1ed9 = ISZERO v1ed8
    0x1eda: v1eda(0x1f2f) = CONST 
    0x1edd: JUMPI v1eda(0x1f2f), v1ed9

    Begin block 0x1ede
    prev=[0x1ed5], succ=[]
    =================================
    0x1ede: v1ede(0x40) = CONST 
    0x1ee1: v1ee1 = MLOAD v1ede(0x40)
    0x1ee2: v1ee2(0xe5) = CONST 
    0x1ee4: v1ee4(0x2) = CONST 
    0x1ee6: v1ee6(0x2000000000000000000000000000000000000000000000000000000000) = EXP v1ee4(0x2), v1ee2(0xe5)
    0x1ee7: v1ee7(0x461bcd) = CONST 
    0x1eeb: v1eeb(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v1ee7(0x461bcd), v1ee6(0x2000000000000000000000000000000000000000000000000000000000)
    0x1eed: MSTORE v1ee1, v1eeb(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1eee: v1eee(0x20) = CONST 
    0x1ef0: v1ef0(0x4) = CONST 
    0x1ef3: v1ef3 = ADD v1ee1, v1ef0(0x4)
    0x1ef4: MSTORE v1ef3, v1eee(0x20)
    0x1ef5: v1ef5(0x31) = CONST 
    0x1ef7: v1ef7(0x24) = CONST 
    0x1efa: v1efa = ADD v1ee1, v1ef7(0x24)
    0x1efb: MSTORE v1efa, v1ef5(0x31)
    0x1efc: v1efc(0x0) = CONST 
    0x1eff: v1eff = MLOAD v1efc(0x0)
    0x1f00: v1f00(0x20) = CONST 
    0x1f02: v1f02(0x2f4a) = CONST 
    0x1f0a: MSTORE v1efc(0x0), v1eff
    0x1f0b: v1f0b(0x44) = CONST 
    0x1f0e: v1f0e = ADD v1ee1, v1f0b(0x44)
    0x1f0f: MSTORE v1f0e, v3694(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f)
    0x1f10: v1f10(0x0) = CONST 
    0x1f13: v1f13 = MLOAD v1f10(0x0)
    0x1f14: v1f14(0x20) = CONST 
    0x1f16: v1f16(0x2f2a) = CONST 
    0x1f1e: MSTORE v1f10(0x0), v1f13
    0x1f1f: v1f1f(0x64) = CONST 
    0x1f22: v1f22 = ADD v1ee1, v1f1f(0x64)
    0x1f23: MSTORE v1f22, v3699(0x20657865637574652066756e6374696f6e000000000000000000000000000000)
    0x1f25: v1f25 = MLOAD v1ede(0x40)
    0x1f29: v1f29(0x0) = SUB v1ee1, v1f25
    0x1f2a: v1f2a(0x84) = CONST 
    0x1f2c: v1f2c(0x84) = ADD v1f2a(0x84), v1f29(0x0)
    0x1f2e: REVERT v1f25, v1f2c(0x84)
    0x3694: v3694(0x5573657220646f6573206e6f742068617665207065726d697373696f6e20746f) = CONST 
    0x3699: v3699(0x20657865637574652066756e6374696f6e000000000000000000000000000000) = CONST 

    Begin block 0x1f2f
    prev=[0x1ed5], succ=[0x1f99, 0x1f9d]
    =================================
    0x1f30: v1f30(0x2) = CONST 
    0x1f32: v1f32 = SLOAD v1f30(0x2)
    0x1f33: v1f33(0x40) = CONST 
    0x1f36: v1f36 = MLOAD v1f33(0x40)
    0x1f37: v1f37(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f59: MSTORE v1f36, v1f37(0xcf8eeb7e00000000000000000000000000000000000000000000000000000000)
    0x1f5a: v1f5a(0x1) = CONST 
    0x1f5c: v1f5c(0xa0) = CONST 
    0x1f5e: v1f5e(0x2) = CONST 
    0x1f60: v1f60(0x10000000000000000000000000000000000000000) = EXP v1f5e(0x2), v1f5c(0xa0)
    0x1f61: v1f61(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f60(0x10000000000000000000000000000000000000000), v1f5a(0x1)
    0x1f64: v1f64 = AND v1f61(0xffffffffffffffffffffffffffffffffffffffff), v43c
    0x1f65: v1f65(0x4) = CONST 
    0x1f68: v1f68 = ADD v1f36, v1f65(0x4)
    0x1f69: MSTORE v1f68, v1f64
    0x1f6a: v1f6a(0x24) = CONST 
    0x1f6d: v1f6d = ADD v1f36, v1f6a(0x24)
    0x1f70: MSTORE v1f6d, v43f
    0x1f72: v1f72 = MLOAD v1f33(0x40)
    0x1f76: v1f76 = AND v1f32, v1f61(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f78: v1f78(0xcf8eeb7e) = CONST 
    0x1f7e: v1f7e(0x44) = CONST 
    0x1f82: v1f82 = ADD v1f36, v1f7e(0x44)
    0x1f84: v1f84(0x0) = CONST 
    0x1f8b: v1f8b(0x0) = SUB v1f36, v1f72
    0x1f8c: v1f8c(0x44) = ADD v1f8b(0x0), v1f7e(0x44)
    0x1f91: v1f91 = EXTCODESIZE v1f76
    0x1f92: v1f92 = ISZERO v1f91
    0x1f94: v1f94 = ISZERO v1f92
    0x1f95: v1f95(0x1f9d) = CONST 
    0x1f98: JUMPI v1f95(0x1f9d), v1f94

    Begin block 0x1f99
    prev=[0x1f2f], succ=[]
    =================================
    0x1f99: v1f99(0x0) = CONST 
    0x1f9c: REVERT v1f99(0x0), v1f99(0x0)

    Begin block 0x1f9d
    prev=[0x1f2f], succ=[0x1fa8, 0x1fb1]
    =================================
    0x1f9f: v1f9f = GAS 
    0x1fa0: v1fa0 = CALL v1f9f, v1f76, v1f84(0x0), v1f72, v1f8c(0x44), v1f72, v1f84(0x0)
    0x1fa1: v1fa1 = ISZERO v1fa0
    0x1fa3: v1fa3 = ISZERO v1fa1
    0x1fa4: v1fa4(0x1fb1) = CONST 
    0x1fa7: JUMPI v1fa4(0x1fb1), v1fa3

    Begin block 0x1fa8
    prev=[0x1f9d], succ=[]
    =================================
    0x1fa8: v1fa8 = RETURNDATASIZE 
    0x1fa9: v1fa9(0x0) = CONST 
    0x1fac: RETURNDATACOPY v1fa9(0x0), v1fa9(0x0), v1fa8
    0x1fad: v1fad = RETURNDATASIZE 
    0x1fae: v1fae(0x0) = CONST 
    0x1fb0: REVERT v1fae(0x0), v1fad

    Begin block 0x1fb1
    prev=[0x1f9d], succ=[0x2017, 0x201b]
    =================================
    0x1fb4: v1fb4(0x2) = CONST 
    0x1fb6: v1fb6 = SLOAD v1fb4(0x2)
    0x1fb7: v1fb7(0x40) = CONST 
    0x1fba: v1fba = MLOAD v1fb7(0x40)
    0x1fbb: v1fbb(0x82838c7600000000000000000000000000000000000000000000000000000000) = CONST 
    0x1fdd: MSTORE v1fba, v1fbb(0x82838c7600000000000000000000000000000000000000000000000000000000)
    0x1fde: v1fde(0x4) = CONST 
    0x1fe1: v1fe1 = ADD v1fba, v1fde(0x4)
    0x1fe4: MSTORE v1fe1, v43f
    0x1fe6: v1fe6 = MLOAD v1fb7(0x40)
    0x1fe7: v1fe7(0x1) = CONST 
    0x1fe9: v1fe9(0xa0) = CONST 
    0x1feb: v1feb(0x2) = CONST 
    0x1fed: v1fed(0x10000000000000000000000000000000000000000) = EXP v1feb(0x2), v1fe9(0xa0)
    0x1fee: v1fee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fed(0x10000000000000000000000000000000000000000), v1fe7(0x1)
    0x1ff1: v1ff1 = AND v1fb6, v1fee(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ff4: v1ff4(0x82838c76) = CONST 
    0x1ffb: v1ffb(0x24) = CONST 
    0x1fff: v1fff = ADD v1fba, v1ffb(0x24)
    0x2001: v2001(0x0) = CONST 
    0x2009: v2009(0x0) = SUB v1fba, v1fe6
    0x200a: v200a(0x24) = ADD v2009(0x0), v1ffb(0x24)
    0x200f: v200f = EXTCODESIZE v1ff1
    0x2010: v2010 = ISZERO v200f
    0x2012: v2012 = ISZERO v2010
    0x2013: v2013(0x201b) = CONST 
    0x2016: JUMPI v2013(0x201b), v2012

    Begin block 0x2017
    prev=[0x1fb1], succ=[]
    =================================
    0x2017: v2017(0x0) = CONST 
    0x201a: REVERT v2017(0x0), v2017(0x0)

    Begin block 0x201b
    prev=[0x1fb1], succ=[0x2026, 0x202f]
    =================================
    0x201d: v201d = GAS 
    0x201e: v201e = CALL v201d, v1ff1, v2001(0x0), v1fe6, v200a(0x24), v1fe6, v2001(0x0)
    0x201f: v201f = ISZERO v201e
    0x2021: v2021 = ISZERO v201f
    0x2022: v2022(0x202f) = CONST 
    0x2025: JUMPI v2022(0x202f), v2021

    Begin block 0x2026
    prev=[0x201b], succ=[]
    =================================
    0x2026: v2026 = RETURNDATASIZE 
    0x2027: v2027(0x0) = CONST 
    0x202a: RETURNDATACOPY v2027(0x0), v2027(0x0), v2026
    0x202b: v202b = RETURNDATASIZE 
    0x202c: v202c(0x0) = CONST 
    0x202e: REVERT v202c(0x0), v202b

    Begin block 0x202f
    prev=[0x201b], succ=[0x3396]
    =================================
    0x2032: v2032(0x40) = CONST 
    0x2035: v2035 = MLOAD v2032(0x40)
    0x2038: MSTORE v2035, v43f
    0x203a: v203a = MLOAD v2032(0x40)
    0x203b: v203b(0x1) = CONST 
    0x203d: v203d(0xa0) = CONST 
    0x203f: v203f(0x2) = CONST 
    0x2041: v2041(0x10000000000000000000000000000000000000000) = EXP v203f(0x2), v203d(0xa0)
    0x2042: v2042(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2041(0x10000000000000000000000000000000000000000), v203b(0x1)
    0x2044: v2044 = AND v43c, v2042(0xffffffffffffffffffffffffffffffffffffffff)
    0x2047: v2047(0xb81d1dffb753076892e04e6e1234d137b031f70d859c299876b0486e966424fd) = CONST 
    0x206d: v206d(0x0) = SUB v2035, v203a
    0x206e: v206e(0x20) = CONST 
    0x2070: v2070(0x20) = ADD v206e(0x20), v206d(0x0)
    0x2072: LOG2 v203a, v2070(0x20), v2047(0xb81d1dffb753076892e04e6e1234d137b031f70d859c299876b0486e966424fd), v2044
    0x2076: JUMP v42e(0x3396)

    Begin block 0x3396
    prev=[0x202f], succ=[]
    =================================
    0x3397: STOP 

}

function setRegulator(address)() public {
    Begin block 0x444
    prev=[], succ=[0x44c, 0x450]
    =================================
    0x445: v445 = CALLVALUE 
    0x447: v447 = ISZERO v445
    0x448: v448(0x450) = CONST 
    0x44b: JUMPI v448(0x450), v447

    Begin block 0x44c
    prev=[0x444], succ=[]
    =================================
    0x44c: v44c(0x0) = CONST 
    0x44f: REVERT v44c(0x0), v44c(0x0)

    Begin block 0x450
    prev=[0x444], succ=[0x2077]
    =================================
    0x452: v452(0x33b7) = CONST 
    0x455: v455(0x1) = CONST 
    0x457: v457(0xa0) = CONST 
    0x459: v459(0x2) = CONST 
    0x45b: v45b(0x10000000000000000000000000000000000000000) = EXP v459(0x2), v457(0xa0)
    0x45c: v45c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v45b(0x10000000000000000000000000000000000000000), v455(0x1)
    0x45d: v45d(0x4) = CONST 
    0x45f: v45f = CALLDATALOAD v45d(0x4)
    0x460: v460 = AND v45f, v45c(0xffffffffffffffffffffffffffffffffffffffff)
    0x461: v461(0x2077) = CONST 
    0x464: JUMP v461(0x2077)

    Begin block 0x2077
    prev=[0x450], succ=[0x208b, 0x208f]
    =================================
    0x2078: v2078(0x0) = CONST 
    0x207b: v207b = SLOAD v2078(0x0)
    0x207c: v207c(0x1) = CONST 
    0x207e: v207e(0xa0) = CONST 
    0x2080: v2080(0x2) = CONST 
    0x2082: v2082(0x10000000000000000000000000000000000000000) = EXP v2080(0x2), v207e(0xa0)
    0x2083: v2083(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2082(0x10000000000000000000000000000000000000000), v207c(0x1)
    0x2084: v2084 = AND v2083(0xffffffffffffffffffffffffffffffffffffffff), v207b
    0x2085: v2085 = CALLER 
    0x2086: v2086 = EQ v2085, v2084
    0x2087: v2087(0x208f) = CONST 
    0x208a: JUMPI v2087(0x208f), v2086

    Begin block 0x208b
    prev=[0x2077], succ=[]
    =================================
    0x208b: v208b(0x0) = CONST 
    0x208e: REVERT v208b(0x0), v208b(0x0)

    Begin block 0x208f
    prev=[0x2077], succ=[0x20a6, 0x20f5]
    =================================
    0x2090: v2090(0x3) = CONST 
    0x2092: v2092 = SLOAD v2090(0x3)
    0x2093: v2093(0x1) = CONST 
    0x2095: v2095(0xa0) = CONST 
    0x2097: v2097(0x2) = CONST 
    0x2099: v2099(0x10000000000000000000000000000000000000000) = EXP v2097(0x2), v2095(0xa0)
    0x209a: v209a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2099(0x10000000000000000000000000000000000000000), v2093(0x1)
    0x209d: v209d = AND v209a(0xffffffffffffffffffffffffffffffffffffffff), v460
    0x209f: v209f = AND v2092, v209a(0xffffffffffffffffffffffffffffffffffffffff)
    0x20a0: v20a0 = EQ v209f, v209d
    0x20a1: v20a1 = ISZERO v20a0
    0x20a2: v20a2(0x20f5) = CONST 
    0x20a5: JUMPI v20a2(0x20f5), v20a1

    Begin block 0x20a6
    prev=[0x208f], succ=[]
    =================================
    0x20a6: v20a6(0x40) = CONST 
    0x20a9: v20a9 = MLOAD v20a6(0x40)
    0x20aa: v20aa(0xe5) = CONST 
    0x20ac: v20ac(0x2) = CONST 
    0x20ae: v20ae(0x2000000000000000000000000000000000000000000000000000000000) = EXP v20ac(0x2), v20aa(0xe5)
    0x20af: v20af(0x461bcd) = CONST 
    0x20b3: v20b3(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v20af(0x461bcd), v20ae(0x2000000000000000000000000000000000000000000000000000000000)
    0x20b5: MSTORE v20a9, v20b3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x20b6: v20b6(0x20) = CONST 
    0x20b8: v20b8(0x4) = CONST 
    0x20bb: v20bb = ADD v20a9, v20b8(0x4)
    0x20bc: MSTORE v20bb, v20b6(0x20)
    0x20bd: v20bd(0x17) = CONST 
    0x20bf: v20bf(0x24) = CONST 
    0x20c2: v20c2 = ADD v20a9, v20bf(0x24)
    0x20c3: MSTORE v20c2, v20bd(0x17)
    0x20c4: v20c4(0x4d7573742062652061206e657720726567756c61746f72000000000000000000) = CONST 
    0x20e5: v20e5(0x44) = CONST 
    0x20e8: v20e8 = ADD v20a9, v20e5(0x44)
    0x20e9: MSTORE v20e8, v20c4(0x4d7573742062652061206e657720726567756c61746f72000000000000000000)
    0x20eb: v20eb = MLOAD v20a6(0x40)
    0x20ef: v20ef(0x0) = SUB v20a9, v20eb
    0x20f0: v20f0(0x64) = CONST 
    0x20f2: v20f2(0x64) = ADD v20f0(0x64), v20ef(0x0)
    0x20f4: REVERT v20eb, v20f2(0x64)

    Begin block 0x20f5
    prev=[0x208f], succ=[0x2e3eB0x20f5]
    =================================
    0x20f6: v20f6(0x20fe) = CONST 
    0x20fa: v20fa(0x2e3e) = CONST 
    0x20fd: JUMP v20fa(0x2e3e)

    Begin block 0x2e3eB0x20f5
    prev=[0x20f5], succ=[0x20fe]
    =================================
    0x2e3fS0x20f5: v2e3fV20f5(0x0) = CONST 
    0x2e42S0x20f5: v2e42V20f5 = EXTCODESIZE v460
    0x2e43S0x20f5: v2e43V20f5 = GT v2e42V20f5, v2e3fV20f5(0x0)
    0x2e45S0x20f5: JUMP v20f6(0x20fe)

    Begin block 0x20fe
    prev=[0x2e3eB0x20f5], succ=[0x2105, 0x217a]
    =================================
    0x20ff: v20ff = ISZERO v2e43V20f5
    0x2100: v2100 = ISZERO v20ff
    0x2101: v2101(0x217a) = CONST 
    0x2104: JUMPI v2101(0x217a), v2100

    Begin block 0x2105
    prev=[0x20fe], succ=[]
    =================================
    0x2105: v2105(0x40) = CONST 
    0x2108: v2108 = MLOAD v2105(0x40)
    0x2109: v2109(0xe5) = CONST 
    0x210b: v210b(0x2) = CONST 
    0x210d: v210d(0x2000000000000000000000000000000000000000000000000000000000) = EXP v210b(0x2), v2109(0xe5)
    0x210e: v210e(0x461bcd) = CONST 
    0x2112: v2112(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v210e(0x461bcd), v210d(0x2000000000000000000000000000000000000000000000000000000000)
    0x2114: MSTORE v2108, v2112(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2115: v2115(0x20) = CONST 
    0x2117: v2117(0x4) = CONST 
    0x211a: v211a = ADD v2108, v2117(0x4)
    0x211b: MSTORE v211a, v2115(0x20)
    0x211c: v211c(0x38) = CONST 
    0x211e: v211e(0x24) = CONST 
    0x2121: v2121 = ADD v2108, v211e(0x24)
    0x2122: MSTORE v2121, v211c(0x38)
    0x2123: v2123(0x43616e6e6f7420736574206120726567756c61746f722073746f726167652074) = CONST 
    0x2144: v2144(0x44) = CONST 
    0x2147: v2147 = ADD v2108, v2144(0x44)
    0x2148: MSTORE v2147, v2123(0x43616e6e6f7420736574206120726567756c61746f722073746f726167652074)
    0x2149: v2149(0x6f2061206e6f6e2d636f6e747261637420616464726573730000000000000000) = CONST 
    0x216a: v216a(0x64) = CONST 
    0x216d: v216d = ADD v2108, v216a(0x64)
    0x216e: MSTORE v216d, v2149(0x6f2061206e6f6e2d636f6e747261637420616464726573730000000000000000)
    0x2170: v2170 = MLOAD v2105(0x40)
    0x2174: v2174(0x0) = SUB v2108, v2170
    0x2175: v2175(0x84) = CONST 
    0x2177: v2177(0x84) = ADD v2175(0x84), v2174(0x0)
    0x2179: REVERT v2170, v2177(0x84)

    Begin block 0x217a
    prev=[0x20fe], succ=[0x33b7]
    =================================
    0x217c: v217c(0x3) = CONST 
    0x217f: v217f = SLOAD v217c(0x3)
    0x2180: v2180(0x1) = CONST 
    0x2182: v2182(0xa0) = CONST 
    0x2184: v2184(0x2) = CONST 
    0x2186: v2186(0x10000000000000000000000000000000000000000) = EXP v2184(0x2), v2182(0xa0)
    0x2187: v2187(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2186(0x10000000000000000000000000000000000000000), v2180(0x1)
    0x218a: v218a = AND v2187(0xffffffffffffffffffffffffffffffffffffffff), v460
    0x218b: v218b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x21a0: v21a0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v218b(0xffffffffffffffffffffffffffffffffffffffff)
    0x21a2: v21a2 = AND v217f, v21a0(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x21a4: v21a4 = OR v218a, v21a2
    0x21a7: SSTORE v217c(0x3), v21a4
    0x21a8: v21a8(0x40) = CONST 
    0x21aa: v21aa = MLOAD v21a8(0x40)
    0x21ac: v21ac = AND v217f, v2187(0xffffffffffffffffffffffffffffffffffffffff)
    0x21b1: v21b1(0x4a59b4b607c6055b37a4716d7813d7d4d2c288e4d0dd8298e365b260a1f262e8) = CONST 
    0x21d3: v21d3(0x0) = CONST 
    0x21d6: LOG3 v21aa, v21d3(0x0), v21b1(0x4a59b4b607c6055b37a4716d7813d7d4d2c288e4d0dd8298e365b260a1f262e8), v21ac, v218a
    0x21d9: JUMP v452(0x33b7)

    Begin block 0x33b7
    prev=[0x217a], succ=[]
    =================================
    0x33b8: STOP 

}

function increaseApproval(address,uint256)() public {
    Begin block 0x465
    prev=[], succ=[0x46d, 0x471]
    =================================
    0x466: v466 = CALLVALUE 
    0x468: v468 = ISZERO v466
    0x469: v469(0x471) = CONST 
    0x46c: JUMPI v469(0x471), v468

    Begin block 0x46d
    prev=[0x465], succ=[]
    =================================
    0x46d: v46d(0x0) = CONST 
    0x470: REVERT v46d(0x0), v46d(0x0)

    Begin block 0x471
    prev=[0x465], succ=[0x21da]
    =================================
    0x473: v473(0x33d8) = CONST 
    0x476: v476(0x1) = CONST 
    0x478: v478(0xa0) = CONST 
    0x47a: v47a(0x2) = CONST 
    0x47c: v47c(0x10000000000000000000000000000000000000000) = EXP v47a(0x2), v478(0xa0)
    0x47d: v47d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v47c(0x10000000000000000000000000000000000000000), v476(0x1)
    0x47e: v47e(0x4) = CONST 
    0x480: v480 = CALLDATALOAD v47e(0x4)
    0x481: v481 = AND v480, v47d(0xffffffffffffffffffffffffffffffffffffffff)
    0x482: v482(0x24) = CONST 
    0x484: v484 = CALLDATALOAD v482(0x24)
    0x485: v485(0x21da) = CONST 
    0x488: JUMP v485(0x21da)

    Begin block 0x21da
    prev=[0x471], succ=[0x2229, 0x222d]
    =================================
    0x21db: v21db(0x3) = CONST 
    0x21dd: v21dd = SLOAD v21db(0x3)
    0x21de: v21de(0x40) = CONST 
    0x21e1: v21e1 = MLOAD v21de(0x40)
    0x21e2: v21e2(0xe0) = CONST 
    0x21e4: v21e4(0x2) = CONST 
    0x21e6: v21e6(0x100000000000000000000000000000000000000000000000000000000) = EXP v21e4(0x2), v21e2(0xe0)
    0x21e7: v21e7(0x7ccce851) = CONST 
    0x21ec: v21ec(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v21e7(0x7ccce851), v21e6(0x100000000000000000000000000000000000000000000000000000000)
    0x21ee: MSTORE v21e1, v21ec(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x21ef: v21ef(0x1) = CONST 
    0x21f1: v21f1(0xa0) = CONST 
    0x21f3: v21f3(0x2) = CONST 
    0x21f5: v21f5(0x10000000000000000000000000000000000000000) = EXP v21f3(0x2), v21f1(0xa0)
    0x21f6: v21f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21f5(0x10000000000000000000000000000000000000000), v21ef(0x1)
    0x21f9: v21f9 = AND v481, v21f6(0xffffffffffffffffffffffffffffffffffffffff)
    0x21fa: v21fa(0x4) = CONST 
    0x21fd: v21fd = ADD v21e1, v21fa(0x4)
    0x21fe: MSTORE v21fd, v21f9
    0x2200: v2200 = MLOAD v21de(0x40)
    0x2201: v2201(0x0) = CONST 
    0x2206: v2206 = AND v21f6(0xffffffffffffffffffffffffffffffffffffffff), v21dd
    0x2208: v2208(0x7ccce851) = CONST 
    0x220e: v220e(0x24) = CONST 
    0x2212: v2212 = ADD v21e1, v220e(0x24)
    0x2214: v2214(0x20) = CONST 
    0x221b: v221b(0x0) = SUB v21e1, v2200
    0x221c: v221c(0x24) = ADD v221b(0x0), v220e(0x24)
    0x2221: v2221 = EXTCODESIZE v2206
    0x2222: v2222 = ISZERO v2221
    0x2224: v2224 = ISZERO v2222
    0x2225: v2225(0x222d) = CONST 
    0x2228: JUMPI v2225(0x222d), v2224

    Begin block 0x2229
    prev=[0x21da], succ=[]
    =================================
    0x2229: v2229(0x0) = CONST 
    0x222c: REVERT v2229(0x0), v2229(0x0)

    Begin block 0x222d
    prev=[0x21da], succ=[0x2238, 0x2241]
    =================================
    0x222f: v222f = GAS 
    0x2230: v2230 = CALL v222f, v2206, v2201(0x0), v2200, v221c(0x24), v2200, v2214(0x20)
    0x2231: v2231 = ISZERO v2230
    0x2233: v2233 = ISZERO v2231
    0x2234: v2234(0x2241) = CONST 
    0x2237: JUMPI v2234(0x2241), v2233

    Begin block 0x2238
    prev=[0x222d], succ=[]
    =================================
    0x2238: v2238 = RETURNDATASIZE 
    0x2239: v2239(0x0) = CONST 
    0x223c: RETURNDATACOPY v2239(0x0), v2239(0x0), v2238
    0x223d: v223d = RETURNDATASIZE 
    0x223e: v223e(0x0) = CONST 
    0x2240: REVERT v223e(0x0), v223d

    Begin block 0x2241
    prev=[0x222d], succ=[0x2253, 0x2257]
    =================================
    0x2246: v2246(0x40) = CONST 
    0x2248: v2248 = MLOAD v2246(0x40)
    0x2249: v2249 = RETURNDATASIZE 
    0x224a: v224a(0x20) = CONST 
    0x224d: v224d = LT v2249, v224a(0x20)
    0x224e: v224e = ISZERO v224d
    0x224f: v224f(0x2257) = CONST 
    0x2252: JUMPI v224f(0x2257), v224e

    Begin block 0x2253
    prev=[0x2241], succ=[]
    =================================
    0x2253: v2253(0x0) = CONST 
    0x2256: REVERT v2253(0x0), v2253(0x0)

    Begin block 0x2257
    prev=[0x2241], succ=[0x225f, 0x229c]
    =================================
    0x2259: v2259 = MLOAD v2248
    0x225a: v225a = ISZERO v2259
    0x225b: v225b(0x229c) = CONST 
    0x225e: JUMPI v225b(0x229c), v225a

    Begin block 0x225f
    prev=[0x2257], succ=[]
    =================================
    0x225f: v225f(0x40) = CONST 
    0x2262: v2262 = MLOAD v225f(0x40)
    0x2263: v2263(0xe5) = CONST 
    0x2265: v2265(0x2) = CONST 
    0x2267: v2267(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2265(0x2), v2263(0xe5)
    0x2268: v2268(0x461bcd) = CONST 
    0x226c: v226c(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2268(0x461bcd), v2267(0x2000000000000000000000000000000000000000000000000000000000)
    0x226e: MSTORE v2262, v226c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x226f: v226f(0x20) = CONST 
    0x2271: v2271(0x4) = CONST 
    0x2274: v2274 = ADD v2262, v2271(0x4)
    0x2275: MSTORE v2274, v226f(0x20)
    0x2276: v2276(0x1c) = CONST 
    0x2278: v2278(0x24) = CONST 
    0x227b: v227b = ADD v2262, v2278(0x24)
    0x227c: MSTORE v227b, v2276(0x1c)
    0x227d: v227d(0x0) = CONST 
    0x2280: v2280 = MLOAD v227d(0x0)
    0x2281: v2281(0x20) = CONST 
    0x2283: v2283(0x2f6a) = CONST 
    0x228b: MSTORE v227d(0x0), v2280
    0x228c: v228c(0x44) = CONST 
    0x228f: v228f = ADD v2262, v228c(0x44)
    0x2290: MSTORE v228f, v369e(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x2292: v2292 = MLOAD v225f(0x40)
    0x2296: v2296(0x0) = SUB v2262, v2292
    0x2297: v2297(0x64) = CONST 
    0x2299: v2299(0x64) = ADD v2297(0x64), v2296(0x0)
    0x229b: REVERT v2292, v2299(0x64)
    0x369e: v369e(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x229c
    prev=[0x2257], succ=[0x22ea, 0x22ee]
    =================================
    0x229d: v229d(0x3) = CONST 
    0x229f: v229f = SLOAD v229d(0x3)
    0x22a0: v22a0(0x40) = CONST 
    0x22a3: v22a3 = MLOAD v22a0(0x40)
    0x22a4: v22a4(0xe0) = CONST 
    0x22a6: v22a6(0x2) = CONST 
    0x22a8: v22a8(0x100000000000000000000000000000000000000000000000000000000) = EXP v22a6(0x2), v22a4(0xe0)
    0x22a9: v22a9(0x7ccce851) = CONST 
    0x22ae: v22ae(0x7ccce85100000000000000000000000000000000000000000000000000000000) = MUL v22a9(0x7ccce851), v22a8(0x100000000000000000000000000000000000000000000000000000000)
    0x22b0: MSTORE v22a3, v22ae(0x7ccce85100000000000000000000000000000000000000000000000000000000)
    0x22b1: v22b1 = CALLER 
    0x22b2: v22b2(0x4) = CONST 
    0x22b5: v22b5 = ADD v22a3, v22b2(0x4)
    0x22b8: MSTORE v22b5, v22b1
    0x22ba: v22ba = MLOAD v22a0(0x40)
    0x22bd: v22bd(0x1) = CONST 
    0x22bf: v22bf(0xa0) = CONST 
    0x22c1: v22c1(0x2) = CONST 
    0x22c3: v22c3(0x10000000000000000000000000000000000000000) = EXP v22c1(0x2), v22bf(0xa0)
    0x22c4: v22c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22c3(0x10000000000000000000000000000000000000000), v22bd(0x1)
    0x22c5: v22c5 = AND v22c4(0xffffffffffffffffffffffffffffffffffffffff), v229f
    0x22c7: v22c7(0x7ccce851) = CONST 
    0x22cd: v22cd(0x24) = CONST 
    0x22d1: v22d1 = ADD v22a3, v22cd(0x24)
    0x22d3: v22d3(0x20) = CONST 
    0x22db: v22db(0x0) = SUB v22a3, v22ba
    0x22dc: v22dc(0x24) = ADD v22db(0x0), v22cd(0x24)
    0x22de: v22de(0x0) = CONST 
    0x22e2: v22e2 = EXTCODESIZE v22c5
    0x22e3: v22e3 = ISZERO v22e2
    0x22e5: v22e5 = ISZERO v22e3
    0x22e6: v22e6(0x22ee) = CONST 
    0x22e9: JUMPI v22e6(0x22ee), v22e5

    Begin block 0x22ea
    prev=[0x229c], succ=[]
    =================================
    0x22ea: v22ea(0x0) = CONST 
    0x22ed: REVERT v22ea(0x0), v22ea(0x0)

    Begin block 0x22ee
    prev=[0x229c], succ=[0x22f9, 0x2302]
    =================================
    0x22f0: v22f0 = GAS 
    0x22f1: v22f1 = CALL v22f0, v22c5, v22de(0x0), v22ba, v22dc(0x24), v22ba, v22d3(0x20)
    0x22f2: v22f2 = ISZERO v22f1
    0x22f4: v22f4 = ISZERO v22f2
    0x22f5: v22f5(0x2302) = CONST 
    0x22f8: JUMPI v22f5(0x2302), v22f4

    Begin block 0x22f9
    prev=[0x22ee], succ=[]
    =================================
    0x22f9: v22f9 = RETURNDATASIZE 
    0x22fa: v22fa(0x0) = CONST 
    0x22fd: RETURNDATACOPY v22fa(0x0), v22fa(0x0), v22f9
    0x22fe: v22fe = RETURNDATASIZE 
    0x22ff: v22ff(0x0) = CONST 
    0x2301: REVERT v22ff(0x0), v22fe

    Begin block 0x2302
    prev=[0x22ee], succ=[0x2314, 0x2318]
    =================================
    0x2307: v2307(0x40) = CONST 
    0x2309: v2309 = MLOAD v2307(0x40)
    0x230a: v230a = RETURNDATASIZE 
    0x230b: v230b(0x20) = CONST 
    0x230e: v230e = LT v230a, v230b(0x20)
    0x230f: v230f = ISZERO v230e
    0x2310: v2310(0x2318) = CONST 
    0x2313: JUMPI v2310(0x2318), v230f

    Begin block 0x2314
    prev=[0x2302], succ=[]
    =================================
    0x2314: v2314(0x0) = CONST 
    0x2317: REVERT v2314(0x0), v2314(0x0)

    Begin block 0x2318
    prev=[0x2302], succ=[0x2320, 0x235d]
    =================================
    0x231a: v231a = MLOAD v2309
    0x231b: v231b = ISZERO v231a
    0x231c: v231c(0x235d) = CONST 
    0x231f: JUMPI v231c(0x235d), v231b

    Begin block 0x2320
    prev=[0x2318], succ=[]
    =================================
    0x2320: v2320(0x40) = CONST 
    0x2323: v2323 = MLOAD v2320(0x40)
    0x2324: v2324(0xe5) = CONST 
    0x2326: v2326(0x2) = CONST 
    0x2328: v2328(0x2000000000000000000000000000000000000000000000000000000000) = EXP v2326(0x2), v2324(0xe5)
    0x2329: v2329(0x461bcd) = CONST 
    0x232d: v232d(0x8c379a000000000000000000000000000000000000000000000000000000000) = MUL v2329(0x461bcd), v2328(0x2000000000000000000000000000000000000000000000000000000000)
    0x232f: MSTORE v2323, v232d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2330: v2330(0x20) = CONST 
    0x2332: v2332(0x4) = CONST 
    0x2335: v2335 = ADD v2323, v2332(0x4)
    0x2336: MSTORE v2335, v2330(0x20)
    0x2337: v2337(0x1c) = CONST 
    0x2339: v2339(0x24) = CONST 
    0x233c: v233c = ADD v2323, v2339(0x24)
    0x233d: MSTORE v233c, v2337(0x1c)
    0x233e: v233e(0x0) = CONST 
    0x2341: v2341 = MLOAD v233e(0x0)
    0x2342: v2342(0x20) = CONST 
    0x2344: v2344(0x2f6a) = CONST 
    0x234c: MSTORE v233e(0x0), v2341
    0x234d: v234d(0x44) = CONST 
    0x2350: v2350 = ADD v2323, v234d(0x44)
    0x2351: MSTORE v2350, v36a3(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000)
    0x2353: v2353 = MLOAD v2320(0x40)
    0x2357: v2357(0x0) = SUB v2323, v2353
    0x2358: v2358(0x64) = CONST 
    0x235a: v235a(0x64) = ADD v2358(0x64), v2357(0x0)
    0x235c: REVERT v2353, v235a(0x64)
    0x36a3: v36a3(0x55736572206d757374206e6f7420626520626c61636b6c697374656400000000) = CONST 

    Begin block 0x235d
    prev=[0x2318], succ=[0x2370, 0x2374]
    =================================
    0x235e: v235e(0x1) = CONST 
    0x2360: v2360 = SLOAD v235e(0x1)
    0x2361: v2361(0xa0) = CONST 
    0x2363: v2363(0x2) = CONST 
    0x2365: v2365(0x10000000000000000000000000000000000000000) = EXP v2363(0x2), v2361(0xa0)
    0x2367: v2367 = DIV v2360, v2365(0x10000000000000000000000000000000000000000)
    0x2368: v2368(0xff) = CONST 
    0x236a: v236a = AND v2368(0xff), v2367
    0x236b: v236b = ISZERO v236a
    0x236c: v236c(0x2374) = CONST 
    0x236f: JUMPI v236c(0x2374), v236b

    Begin block 0x2370
    prev=[0x235d], succ=[]
    =================================
    0x2370: v2370(0x0) = CONST 
    0x2373: REVERT v2370(0x0), v2370(0x0)

    Begin block 0x2374
    prev=[0x235d], succ=[0x2e46]
    =================================
    0x2375: v2375(0x3590) = CONST 
    0x237a: v237a = CALLER 
    0x237b: v237b(0x2e46) = CONST 
    0x237e: JUMP v237b(0x2e46)

    Begin block 0x2e46
    prev=[0x2374], succ=[0x2eb8, 0x2ebc]
    =================================
    0x2e47: v2e47(0x2) = CONST 
    0x2e49: v2e49 = SLOAD v2e47(0x2)
    0x2e4a: v2e4a(0x40) = CONST 
    0x2e4d: v2e4d = MLOAD v2e4a(0x40)
    0x2e4e: v2e4e(0x5fd72d1600000000000000000000000000000000000000000000000000000000) = CONST 
    0x2e70: MSTORE v2e4d, v2e4e(0x5fd72d1600000000000000000000000000000000000000000000000000000000)
    0x2e71: v2e71(0x1) = CONST 
    0x2e73: v2e73(0xa0) = CONST 
    0x2e75: v2e75(0x2) = CONST 
    0x2e77: v2e77(0x10000000000000000000000000000000000000000) = EXP v2e75(0x2), v2e73(0xa0)
    0x2e78: v2e78(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e77(0x10000000000000000000000000000000000000000), v2e71(0x1)
    0x2e7b: v2e7b = AND v2e78(0xffffffffffffffffffffffffffffffffffffffff), v237a
    0x2e7c: v2e7c(0x4) = CONST 
    0x2e7f: v2e7f = ADD v2e4d, v2e7c(0x4)
    0x2e80: MSTORE v2e7f, v2e7b
    0x2e83: v2e83 = AND v2e78(0xffffffffffffffffffffffffffffffffffffffff), v481
    0x2e84: v2e84(0x24) = CONST 
    0x2e87: v2e87 = ADD v2e4d, v2e84(0x24)
    0x2e88: MSTORE v2e87, v2e83
    0x2e89: v2e89(0x44) = CONST 
    0x2e8c: v2e8c = ADD v2e4d, v2e89(0x44)
    0x2e8f: MSTORE v2e8c, v484
    0x2e91: v2e91 = MLOAD v2e4a(0x40)
    0x2e95: v2e95 = AND v2e49, v2e78(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e97: v2e97(0x5fd72d16) = CONST 
    0x2e9d: v2e9d(0x64) = CONST 
    0x2ea1: v2ea1 = ADD v2e4d, v2e9d(0x64)
    0x2ea3: v2ea3(0x0) = CONST 
    0x2eaa: v2eaa(0x0) = SUB v2e4d, v2e91
    0x2eab: v2eab(0x64) = ADD v2eaa(0x0), v2e9d(0x64)
    0x2eb0: v2eb0 = EXTCODESIZE v2e95
    0x2eb1: v2eb1 = ISZERO v2eb0
    0x2eb3: v2eb3 = ISZERO v2eb1
    0x2eb4: v2eb4(0x2ebc) = CONST 
    0x2eb7: JUMPI v2eb4(0x2ebc), v2eb3

    Begin block 0x2eb8
    prev=[0x2e46], succ=[]
    =================================
    0x2eb8: v2eb8(0x0) = CONST 
    0x2ebb: REVERT v2eb8(0x0), v2eb8(0x0)

    Begin block 0x2ebc
    prev=[0x2e46], succ=[0x2ec7, 0x2ed0]
    =================================
    0x2ebe: v2ebe = GAS 
    0x2ebf: v2ebf = CALL v2ebe, v2e95, v2ea3(0x0), v2e91, v2eab(0x64), v2e91, v2ea3(0x0)
    0x2ec0: v2ec0 = ISZERO v2ebf
    0x2ec2: v2ec2 = ISZERO v2ec0
    0x2ec3: v2ec3(0x2ed0) = CONST 
    0x2ec6: JUMPI v2ec3(0x2ed0), v2ec2

    Begin block 0x2ec7
    prev=[0x2ebc], succ=[]
    =================================
    0x2ec7: v2ec7 = RETURNDATASIZE 
    0x2ec8: v2ec8(0x0) = CONST 
    0x2ecb: RETURNDATACOPY v2ec8(0x0), v2ec8(0x0), v2ec7
    0x2ecc: v2ecc = RETURNDATASIZE 
    0x2ecd: v2ecd(0x0) = CONST 
    0x2ecf: REVERT v2ecd(0x0), v2ecc

    Begin block 0x2ed0
    prev=[0x2ebc], succ=[0x2f13]
    =================================
    0x2ed6: v2ed6(0x1) = CONST 
    0x2ed8: v2ed8(0xa0) = CONST 
    0x2eda: v2eda(0x2) = CONST 
    0x2edc: v2edc(0x10000000000000000000000000000000000000000) = EXP v2eda(0x2), v2ed8(0xa0)
    0x2edd: v2edd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2edc(0x10000000000000000000000000000000000000000), v2ed6(0x1)
    0x2ede: v2ede = AND v2edd(0xffffffffffffffffffffffffffffffffffffffff), v481
    0x2ee0: v2ee0(0x1) = CONST 
    0x2ee2: v2ee2(0xa0) = CONST 
    0x2ee4: v2ee4(0x2) = CONST 
    0x2ee6: v2ee6(0x10000000000000000000000000000000000000000) = EXP v2ee4(0x2), v2ee2(0xa0)
    0x2ee7: v2ee7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ee6(0x10000000000000000000000000000000000000000), v2ee0(0x1)
    0x2ee8: v2ee8 = AND v2ee7(0xffffffffffffffffffffffffffffffffffffffff), v237a
    0x2ee9: v2ee9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x2f0a: v2f0a(0x2f13) = CONST 
    0x2f0f: v2f0f(0x237f) = CONST 
    0x2f12: v2f12_0 = CALLPRIVATE v2f0f(0x237f), v481, v237a, v2f0a(0x2f13)

    Begin block 0x2f13
    prev=[0x2ed0], succ=[0x3590]
    =================================
    0x2f14: v2f14(0x40) = CONST 
    0x2f17: v2f17 = MLOAD v2f14(0x40)
    0x2f1a: MSTORE v2f17, v2f12_0
    0x2f1b: v2f1b = MLOAD v2f14(0x40)
    0x2f1f: v2f1f(0x0) = SUB v2f17, v2f1b
    0x2f20: v2f20(0x20) = CONST 
    0x2f22: v2f22(0x20) = ADD v2f20(0x20), v2f1f(0x0)
    0x2f24: LOG3 v2f1b, v2f22(0x20), v2ee9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v2ee8, v2ede
    0x2f28: JUMP v2375(0x3590)

    Begin block 0x3590
    prev=[0x2f13], succ=[0x33d8]
    =================================
    0x3592: v3592(0x1) = CONST 
    0x359a: JUMP v473(0x33d8)

    Begin block 0x33d8
    prev=[0x3590], succ=[]
    =================================
    0x33d9: v33d9(0x40) = CONST 
    0x33dc: v33dc = MLOAD v33d9(0x40)
    0x33de: v33de = ISZERO v3592(0x1)
    0x33df: v33df = ISZERO v33de
    0x33e1: MSTORE v33dc, v33df
    0x33e2: v33e2 = MLOAD v33d9(0x40)
    0x33e6: v33e6(0x0) = SUB v33dc, v33e2
    0x33e7: v33e7(0x20) = CONST 
    0x33e9: v33e9(0x20) = ADD v33e7(0x20), v33e6(0x0)
    0x33eb: RETURN v33e2, v33e9(0x20)

}

function allowance(address,address)() public {
    Begin block 0x489
    prev=[], succ=[0x491, 0x495]
    =================================
    0x48a: v48a = CALLVALUE 
    0x48c: v48c = ISZERO v48a
    0x48d: v48d(0x495) = CONST 
    0x490: JUMPI v48d(0x495), v48c

    Begin block 0x491
    prev=[0x489], succ=[]
    =================================
    0x491: v491(0x0) = CONST 
    0x494: REVERT v491(0x0), v491(0x0)

    Begin block 0x495
    prev=[0x489], succ=[0x340b]
    =================================
    0x497: v497(0x340b) = CONST 
    0x49a: v49a(0x1) = CONST 
    0x49c: v49c(0xa0) = CONST 
    0x49e: v49e(0x2) = CONST 
    0x4a0: v4a0(0x10000000000000000000000000000000000000000) = EXP v49e(0x2), v49c(0xa0)
    0x4a1: v4a1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4a0(0x10000000000000000000000000000000000000000), v49a(0x1)
    0x4a2: v4a2(0x4) = CONST 
    0x4a4: v4a4 = CALLDATALOAD v4a2(0x4)
    0x4a6: v4a6 = AND v4a1(0xffffffffffffffffffffffffffffffffffffffff), v4a4
    0x4a8: v4a8(0x24) = CONST 
    0x4aa: v4aa = CALLDATALOAD v4a8(0x24)
    0x4ab: v4ab = AND v4aa, v4a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x4ac: v4ac(0x237f) = CONST 
    0x4af: v4af_0 = CALLPRIVATE v4ac(0x237f), v4ab, v4a6, v497(0x340b)

    Begin block 0x340b
    prev=[0x495], succ=[]
    =================================
    0x340c: v340c(0x40) = CONST 
    0x340f: v340f = MLOAD v340c(0x40)
    0x3412: MSTORE v340f, v4af_0
    0x3413: v3413 = MLOAD v340c(0x40)
    0x3417: v3417(0x0) = SUB v340f, v3413
    0x3418: v3418(0x20) = CONST 
    0x341a: v341a(0x20) = ADD v3418(0x20), v3417(0x0)
    0x341c: RETURN v3413, v341a(0x20)

}

function regulator()() public {
    Begin block 0x4b0
    prev=[], succ=[0x4b8, 0x4bc]
    =================================
    0x4b1: v4b1 = CALLVALUE 
    0x4b3: v4b3 = ISZERO v4b1
    0x4b4: v4b4(0x4bc) = CONST 
    0x4b7: JUMPI v4b4(0x4bc), v4b3

    Begin block 0x4b8
    prev=[0x4b0], succ=[]
    =================================
    0x4b8: v4b8(0x0) = CONST 
    0x4bb: REVERT v4b8(0x0), v4b8(0x0)

    Begin block 0x4bc
    prev=[0x4b0], succ=[0x2425]
    =================================
    0x4be: v4be(0x343c) = CONST 
    0x4c1: v4c1(0x2425) = CONST 
    0x4c4: JUMP v4c1(0x2425)

    Begin block 0x2425
    prev=[0x4bc], succ=[0x343c]
    =================================
    0x2426: v2426(0x3) = CONST 
    0x2428: v2428 = SLOAD v2426(0x3)
    0x2429: v2429(0x1) = CONST 
    0x242b: v242b(0xa0) = CONST 
    0x242d: v242d(0x2) = CONST 
    0x242f: v242f(0x10000000000000000000000000000000000000000) = EXP v242d(0x2), v242b(0xa0)
    0x2430: v2430(0xffffffffffffffffffffffffffffffffffffffff) = SUB v242f(0x10000000000000000000000000000000000000000), v2429(0x1)
    0x2431: v2431 = AND v2430(0xffffffffffffffffffffffffffffffffffffffff), v2428
    0x2433: JUMP v4be(0x343c)

    Begin block 0x343c
    prev=[0x2425], succ=[]
    =================================
    0x343d: v343d(0x40) = CONST 
    0x3440: v3440 = MLOAD v343d(0x40)
    0x3441: v3441(0x1) = CONST 
    0x3443: v3443(0xa0) = CONST 
    0x3445: v3445(0x2) = CONST 
    0x3447: v3447(0x10000000000000000000000000000000000000000) = EXP v3445(0x2), v3443(0xa0)
    0x3448: v3448(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3447(0x10000000000000000000000000000000000000000), v3441(0x1)
    0x344b: v344b = AND v2431, v3448(0xffffffffffffffffffffffffffffffffffffffff)
    0x344d: MSTORE v3440, v344b
    0x344e: v344e = MLOAD v343d(0x40)
    0x3452: v3452(0x0) = SUB v3440, v344e
    0x3453: v3453(0x20) = CONST 
    0x3455: v3455(0x20) = ADD v3453(0x20), v3452(0x0)
    0x3457: RETURN v344e, v3455(0x20)

}

function pendingOwner()() public {
    Begin block 0x4c5
    prev=[], succ=[0x4cd, 0x4d1]
    =================================
    0x4c6: v4c6 = CALLVALUE 
    0x4c8: v4c8 = ISZERO v4c6
    0x4c9: v4c9(0x4d1) = CONST 
    0x4cc: JUMPI v4c9(0x4d1), v4c8

    Begin block 0x4cd
    prev=[0x4c5], succ=[]
    =================================
    0x4cd: v4cd(0x0) = CONST 
    0x4d0: REVERT v4cd(0x0), v4cd(0x0)

    Begin block 0x4d1
    prev=[0x4c5], succ=[0x2434]
    =================================
    0x4d3: v4d3(0x3477) = CONST 
    0x4d6: v4d6(0x2434) = CONST 
    0x4d9: JUMP v4d6(0x2434)

    Begin block 0x2434
    prev=[0x4d1], succ=[0x3477]
    =================================
    0x2435: v2435(0x1) = CONST 
    0x2437: v2437 = SLOAD v2435(0x1)
    0x2438: v2438(0x1) = CONST 
    0x243a: v243a(0xa0) = CONST 
    0x243c: v243c(0x2) = CONST 
    0x243e: v243e(0x10000000000000000000000000000000000000000) = EXP v243c(0x2), v243a(0xa0)
    0x243f: v243f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v243e(0x10000000000000000000000000000000000000000), v2438(0x1)
    0x2440: v2440 = AND v243f(0xffffffffffffffffffffffffffffffffffffffff), v2437
    0x2442: JUMP v4d3(0x3477)

    Begin block 0x3477
    prev=[0x2434], succ=[]
    =================================
    0x3478: v3478(0x40) = CONST 
    0x347b: v347b = MLOAD v3478(0x40)
    0x347c: v347c(0x1) = CONST 
    0x347e: v347e(0xa0) = CONST 
    0x3480: v3480(0x2) = CONST 
    0x3482: v3482(0x10000000000000000000000000000000000000000) = EXP v3480(0x2), v347e(0xa0)
    0x3483: v3483(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3482(0x10000000000000000000000000000000000000000), v347c(0x1)
    0x3486: v3486 = AND v2440, v3483(0xffffffffffffffffffffffffffffffffffffffff)
    0x3488: MSTORE v347b, v3486
    0x3489: v3489 = MLOAD v3478(0x40)
    0x348d: v348d(0x0) = SUB v347b, v3489
    0x348e: v348e(0x20) = CONST 
    0x3490: v3490(0x20) = ADD v348e(0x20), v348d(0x0)
    0x3492: RETURN v3489, v3490(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x4da
    prev=[], succ=[0x4e2, 0x4e6]
    =================================
    0x4db: v4db = CALLVALUE 
    0x4dd: v4dd = ISZERO v4db
    0x4de: v4de(0x4e6) = CONST 
    0x4e1: JUMPI v4de(0x4e6), v4dd

    Begin block 0x4e2
    prev=[0x4da], succ=[]
    =================================
    0x4e2: v4e2(0x0) = CONST 
    0x4e5: REVERT v4e2(0x0), v4e2(0x0)

    Begin block 0x4e6
    prev=[0x4da], succ=[0x2443]
    =================================
    0x4e8: v4e8(0x34b2) = CONST 
    0x4eb: v4eb(0x1) = CONST 
    0x4ed: v4ed(0xa0) = CONST 
    0x4ef: v4ef(0x2) = CONST 
    0x4f1: v4f1(0x10000000000000000000000000000000000000000) = EXP v4ef(0x2), v4ed(0xa0)
    0x4f2: v4f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f1(0x10000000000000000000000000000000000000000), v4eb(0x1)
    0x4f3: v4f3(0x4) = CONST 
    0x4f5: v4f5 = CALLDATALOAD v4f3(0x4)
    0x4f6: v4f6 = AND v4f5, v4f2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4f7: v4f7(0x2443) = CONST 
    0x4fa: JUMP v4f7(0x2443)

    Begin block 0x2443
    prev=[0x4e6], succ=[0x2456, 0x245a]
    =================================
    0x2444: v2444(0x0) = CONST 
    0x2446: v2446 = SLOAD v2444(0x0)
    0x2447: v2447(0x1) = CONST 
    0x2449: v2449(0xa0) = CONST 
    0x244b: v244b(0x2) = CONST 
    0x244d: v244d(0x10000000000000000000000000000000000000000) = EXP v244b(0x2), v2449(0xa0)
    0x244e: v244e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v244d(0x10000000000000000000000000000000000000000), v2447(0x1)
    0x244f: v244f = AND v244e(0xffffffffffffffffffffffffffffffffffffffff), v2446
    0x2450: v2450 = CALLER 
    0x2451: v2451 = EQ v2450, v244f
    0x2452: v2452(0x245a) = CONST 
    0x2455: JUMPI v2452(0x245a), v2451

    Begin block 0x2456
    prev=[0x2443], succ=[]
    =================================
    0x2456: v2456(0x0) = CONST 
    0x2459: REVERT v2456(0x0), v2456(0x0)

    Begin block 0x245a
    prev=[0x2443], succ=[0x246b, 0x246f]
    =================================
    0x245b: v245b(0x1) = CONST 
    0x245d: v245d(0xa0) = CONST 
    0x245f: v245f(0x2) = CONST 
    0x2461: v2461(0x10000000000000000000000000000000000000000) = EXP v245f(0x2), v245d(0xa0)
    0x2462: v2462(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2461(0x10000000000000000000000000000000000000000), v245b(0x1)
    0x2464: v2464 = AND v4f6, v2462(0xffffffffffffffffffffffffffffffffffffffff)
    0x2465: v2465 = ISZERO v2464
    0x2466: v2466 = ISZERO v2465
    0x2467: v2467(0x246f) = CONST 
    0x246a: JUMPI v2467(0x246f), v2466

    Begin block 0x246b
    prev=[0x245a], succ=[]
    =================================
    0x246b: v246b(0x0) = CONST 
    0x246e: REVERT v246b(0x0), v246b(0x0)

    Begin block 0x246f
    prev=[0x245a], succ=[0x34b2]
    =================================
    0x2470: v2470(0x1) = CONST 
    0x2473: v2473 = SLOAD v2470(0x1)
    0x2474: v2474(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2489: v2489(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v2474(0xffffffffffffffffffffffffffffffffffffffff)
    0x248a: v248a = AND v2489(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2473
    0x248b: v248b(0x1) = CONST 
    0x248d: v248d(0xa0) = CONST 
    0x248f: v248f(0x2) = CONST 
    0x2491: v2491(0x10000000000000000000000000000000000000000) = EXP v248f(0x2), v248d(0xa0)
    0x2492: v2492(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2491(0x10000000000000000000000000000000000000000), v248b(0x1)
    0x2496: v2496 = AND v2492(0xffffffffffffffffffffffffffffffffffffffff), v4f6
    0x249a: v249a = OR v2496, v248a
    0x249c: SSTORE v2470(0x1), v249a
    0x249d: JUMP v4e8(0x34b2)

    Begin block 0x34b2
    prev=[0x246f], succ=[]
    =================================
    0x34b3: STOP 

}

function lock()() public {
    Begin block 0x4fb
    prev=[], succ=[0x503, 0x507]
    =================================
    0x4fc: v4fc = CALLVALUE 
    0x4fe: v4fe = ISZERO v4fc
    0x4ff: v4ff(0x507) = CONST 
    0x502: JUMPI v4ff(0x507), v4fe

    Begin block 0x503
    prev=[0x4fb], succ=[]
    =================================
    0x503: v503(0x0) = CONST 
    0x506: REVERT v503(0x0), v503(0x0)

    Begin block 0x507
    prev=[0x4fb], succ=[0x249e]
    =================================
    0x509: v509(0x34d3) = CONST 
    0x50c: v50c(0x249e) = CONST 
    0x50f: JUMP v50c(0x249e)

    Begin block 0x249e
    prev=[0x507], succ=[0x24b1, 0x24b5]
    =================================
    0x249f: v249f(0x0) = CONST 
    0x24a1: v24a1 = SLOAD v249f(0x0)
    0x24a2: v24a2(0x1) = CONST 
    0x24a4: v24a4(0xa0) = CONST 
    0x24a6: v24a6(0x2) = CONST 
    0x24a8: v24a8(0x10000000000000000000000000000000000000000) = EXP v24a6(0x2), v24a4(0xa0)
    0x24a9: v24a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v24a8(0x10000000000000000000000000000000000000000), v24a2(0x1)
    0x24aa: v24aa = AND v24a9(0xffffffffffffffffffffffffffffffffffffffff), v24a1
    0x24ab: v24ab = CALLER 
    0x24ac: v24ac = EQ v24ab, v24aa
    0x24ad: v24ad(0x24b5) = CONST 
    0x24b0: JUMPI v24ad(0x24b5), v24ac

    Begin block 0x24b1
    prev=[0x249e], succ=[]
    =================================
    0x24b1: v24b1(0x0) = CONST 
    0x24b4: REVERT v24b1(0x0), v24b1(0x0)

    Begin block 0x24b5
    prev=[0x249e], succ=[0x34d3]
    =================================
    0x24b6: v24b6(0x1) = CONST 
    0x24b9: v24b9 = SLOAD v24b6(0x1)
    0x24ba: v24ba(0xff000000000000000000000000000000000000000000) = CONST 
    0x24d1: v24d1(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff) = NOT v24ba(0xff000000000000000000000000000000000000000000)
    0x24d2: v24d2 = AND v24d1(0xffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffffff), v24b9
    0x24d4: SSTORE v24b6(0x1), v24d2
    0x24d5: v24d5(0x40) = CONST 
    0x24d7: v24d7 = MLOAD v24d5(0x40)
    0x24d8: v24d8(0xf2e5b6c72c6a4491efd919a9f9a409f324ef0708c11ee57d410c2cb06c0992b) = CONST 
    0x24fa: v24fa(0x0) = CONST 
    0x24fd: LOG1 v24d7, v24fa(0x0), v24d8(0xf2e5b6c72c6a4491efd919a9f9a409f324ef0708c11ee57d410c2cb06c0992b)
    0x24fe: JUMP v509(0x34d3)

    Begin block 0x34d3
    prev=[0x24b5], succ=[]
    =================================
    0x34d4: STOP 

}

