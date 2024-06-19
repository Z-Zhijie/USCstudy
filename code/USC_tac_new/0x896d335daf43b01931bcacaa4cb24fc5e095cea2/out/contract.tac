function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x186d]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x1847: v1847(0x186d) = CONST 
    0x1848: JUMPI v1847(0x186d), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x1870]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x11c67c52) = CONST 
    0x3b: v3b = EQ v34, v35(0x11c67c52)
    0x1849: v1849(0x1870) = CONST 
    0x184a: JUMPI v1849(0x1870), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x1873, 0x4b]
    =================================
    0x41: v41(0x13af4035) = CONST 
    0x46: v46 = EQ v41(0x13af4035), v34
    0x184b: v184b(0x1873) = CONST 
    0x184c: JUMPI v184b(0x1873), v46

    Begin block 0x1873
    prev=[0x40], succ=[]
    =================================
    0x1874: v1874(0x166) = CONST 
    0x1875: CALLPRIVATE v1874(0x166)

    Begin block 0x4b
    prev=[0x40], succ=[0x1876, 0x56]
    =================================
    0x4c: v4c(0x23aa7e12) = CONST 
    0x51: v51 = EQ v4c(0x23aa7e12), v34
    0x184d: v184d(0x1876) = CONST 
    0x184e: JUMPI v184d(0x1876), v51

    Begin block 0x1876
    prev=[0x4b], succ=[]
    =================================
    0x1877: v1877(0x187) = CONST 
    0x1878: CALLPRIVATE v1877(0x187)

    Begin block 0x56
    prev=[0x4b], succ=[0x1879, 0x61]
    =================================
    0x57: v57(0x25e16063) = CONST 
    0x5c: v5c = EQ v57(0x25e16063), v34
    0x184f: v184f(0x1879) = CONST 
    0x1850: JUMPI v184f(0x1879), v5c

    Begin block 0x1879
    prev=[0x56], succ=[]
    =================================
    0x187a: v187a(0x1b8) = CONST 
    0x187b: CALLPRIVATE v187a(0x1b8)

    Begin block 0x61
    prev=[0x56], succ=[0x187c, 0x6c]
    =================================
    0x62: v62(0x3b22f35f) = CONST 
    0x67: v67 = EQ v62(0x3b22f35f), v34
    0x1851: v1851(0x187c) = CONST 
    0x1852: JUMPI v1851(0x187c), v67

    Begin block 0x187c
    prev=[0x61], succ=[]
    =================================
    0x187d: v187d(0x1d9) = CONST 
    0x187e: CALLPRIVATE v187d(0x1d9)

    Begin block 0x6c
    prev=[0x61], succ=[0x187f, 0x77]
    =================================
    0x6d: v6d(0x3f579f42) = CONST 
    0x72: v72 = EQ v6d(0x3f579f42), v34
    0x1853: v1853(0x187f) = CONST 
    0x1854: JUMPI v1853(0x187f), v72

    Begin block 0x187f
    prev=[0x6c], succ=[]
    =================================
    0x1880: v1880(0x203) = CONST 
    0x1881: CALLPRIVATE v1880(0x203)

    Begin block 0x77
    prev=[0x6c], succ=[0x1882, 0x82]
    =================================
    0x78: v78(0x57acc118) = CONST 
    0x7d: v7d = EQ v78(0x57acc118), v34
    0x1855: v1855(0x1882) = CONST 
    0x1856: JUMPI v1855(0x1882), v7d

    Begin block 0x1882
    prev=[0x77], succ=[]
    =================================
    0x1883: v1883(0x26c) = CONST 
    0x1884: CALLPRIVATE v1883(0x26c)

    Begin block 0x82
    prev=[0x77], succ=[0x1885, 0x8d]
    =================================
    0x83: v83(0x59c3f7f0) = CONST 
    0x88: v88 = EQ v83(0x59c3f7f0), v34
    0x1857: v1857(0x1885) = CONST 
    0x1858: JUMPI v1857(0x1885), v88

    Begin block 0x1885
    prev=[0x82], succ=[]
    =================================
    0x1886: v1886(0x28d) = CONST 
    0x1887: CALLPRIVATE v1886(0x28d)

    Begin block 0x8d
    prev=[0x82], succ=[0x1888, 0x98]
    =================================
    0x8e: v8e(0x806ad57e) = CONST 
    0x93: v93 = EQ v8e(0x806ad57e), v34
    0x1859: v1859(0x1888) = CONST 
    0x185a: JUMPI v1859(0x1888), v93

    Begin block 0x1888
    prev=[0x8d], succ=[]
    =================================
    0x1889: v1889(0x2a5) = CONST 
    0x188a: CALLPRIVATE v1889(0x2a5)

    Begin block 0x98
    prev=[0x8d], succ=[0x188b, 0xa3]
    =================================
    0x99: v99(0x81427e45) = CONST 
    0x9e: v9e = EQ v99(0x81427e45), v34
    0x185b: v185b(0x188b) = CONST 
    0x185c: JUMPI v185b(0x188b), v9e

    Begin block 0x188b
    prev=[0x98], succ=[]
    =================================
    0x188c: v188c(0x2c6) = CONST 
    0x188d: CALLPRIVATE v188c(0x2c6)

    Begin block 0xa3
    prev=[0x98], succ=[0x188e, 0xae]
    =================================
    0xa4: va4(0x8da5cb5b) = CONST 
    0xa9: va9 = EQ va4(0x8da5cb5b), v34
    0x185d: v185d(0x188e) = CONST 
    0x185e: JUMPI v185d(0x188e), va9

    Begin block 0x188e
    prev=[0xa3], succ=[]
    =================================
    0x188f: v188f(0x329) = CONST 
    0x1890: CALLPRIVATE v188f(0x329)

    Begin block 0xae
    prev=[0xa3], succ=[0x1891, 0xb9]
    =================================
    0xaf: vaf(0x9456fbcc) = CONST 
    0xb4: vb4 = EQ vaf(0x9456fbcc), v34
    0x185f: v185f(0x1891) = CONST 
    0x1860: JUMPI v185f(0x1891), vb4

    Begin block 0x1891
    prev=[0xae], succ=[]
    =================================
    0x1892: v1892(0x33e) = CONST 
    0x1893: CALLPRIVATE v1892(0x33e)

    Begin block 0xb9
    prev=[0xae], succ=[0x1894, 0xc4]
    =================================
    0xba: vba(0xaa156645) = CONST 
    0xbf: vbf = EQ vba(0xaa156645), v34
    0x1861: v1861(0x1894) = CONST 
    0x1862: JUMPI v1861(0x1894), vbf

    Begin block 0x1894
    prev=[0xb9], succ=[]
    =================================
    0x1895: v1895(0x365) = CONST 
    0x1896: CALLPRIVATE v1895(0x365)

    Begin block 0xc4
    prev=[0xb9], succ=[0x1897, 0xcf]
    =================================
    0xc5: vc5(0xc4f987a5) = CONST 
    0xca: vca = EQ vc5(0xc4f987a5), v34
    0x1863: v1863(0x1897) = CONST 
    0x1864: JUMPI v1863(0x1897), vca

    Begin block 0x1897
    prev=[0xc4], succ=[]
    =================================
    0x1898: v1898(0x386) = CONST 
    0x1899: CALLPRIVATE v1898(0x386)

    Begin block 0xcf
    prev=[0xc4], succ=[0x189a, 0xda]
    =================================
    0xd0: vd0(0xcb3eef2c) = CONST 
    0xd5: vd5 = EQ vd0(0xcb3eef2c), v34
    0x1865: v1865(0x189a) = CONST 
    0x1866: JUMPI v1865(0x189a), vd5

    Begin block 0x189a
    prev=[0xcf], succ=[]
    =================================
    0x189b: v189b(0x3a7) = CONST 
    0x189c: CALLPRIVATE v189b(0x3a7)

    Begin block 0xda
    prev=[0xcf], succ=[0x189d, 0xe5]
    =================================
    0xdb: vdb(0xd264e05e) = CONST 
    0xe0: ve0 = EQ vdb(0xd264e05e), v34
    0x1867: v1867(0x189d) = CONST 
    0x1868: JUMPI v1867(0x189d), ve0

    Begin block 0x189d
    prev=[0xda], succ=[]
    =================================
    0x189e: v189e(0x40c) = CONST 
    0x189f: CALLPRIVATE v189e(0x40c)

    Begin block 0xe5
    prev=[0xda], succ=[0x18a0, 0xf0]
    =================================
    0xe6: ve6(0xd273285b) = CONST 
    0xeb: veb = EQ ve6(0xd273285b), v34
    0x1869: v1869(0x18a0) = CONST 
    0x186a: JUMPI v1869(0x18a0), veb

    Begin block 0x18a0
    prev=[0xe5], succ=[]
    =================================
    0x18a1: v18a1(0x421) = CONST 
    0x18a2: CALLPRIVATE v18a1(0x421)

    Begin block 0xf0
    prev=[0xe5], succ=[0x186d, 0x18a3]
    =================================
    0xf1: vf1(0xfa34b345) = CONST 
    0xf6: vf6 = EQ vf1(0xfa34b345), v34
    0x186b: v186b(0x18a3) = CONST 
    0x186c: JUMPI v186b(0x18a3), vf6

    Begin block 0x186d
    prev=[0x0, 0xf0], succ=[]
    =================================
    0x186e: v186e(0xfb) = CONST 
    0x186f: CALLPRIVATE v186e(0xfb)

    Begin block 0x18a3
    prev=[0xf0], succ=[]
    =================================
    0x18a4: v18a4(0x436) = CONST 
    0x18a5: CALLPRIVATE v18a4(0x436)

    Begin block 0x1870
    prev=[0xd], succ=[]
    =================================
    0x1871: v1871(0xfd) = CONST 
    0x1872: CALLPRIVATE v1871(0xfd)

}

function setOwner(address)() public {
    Begin block 0x166
    prev=[], succ=[0x16e, 0x172]
    =================================
    0x167: v167 = CALLVALUE 
    0x169: v169 = ISZERO v167
    0x16a: v16a(0x172) = CONST 
    0x16d: JUMPI v16a(0x172), v169

    Begin block 0x16e
    prev=[0x166], succ=[]
    =================================
    0x16e: v16e(0x0) = CONST 
    0x171: REVERT v16e(0x0), v16e(0x0)

    Begin block 0x172
    prev=[0x166], succ=[0x5b6]
    =================================
    0x174: v174(0x145b) = CONST 
    0x177: v177(0x1) = CONST 
    0x179: v179(0xa0) = CONST 
    0x17b: v17b(0x2) = CONST 
    0x17d: v17d(0x10000000000000000000000000000000000000000) = EXP v17b(0x2), v179(0xa0)
    0x17e: v17e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17d(0x10000000000000000000000000000000000000000), v177(0x1)
    0x17f: v17f(0x4) = CONST 
    0x181: v181 = CALLDATALOAD v17f(0x4)
    0x182: v182 = AND v181, v17e(0xffffffffffffffffffffffffffffffffffffffff)
    0x183: v183(0x5b6) = CONST 
    0x186: JUMP v183(0x5b6)

    Begin block 0x5b6
    prev=[0x172], succ=[0x5d0, 0x5d4]
    =================================
    0x5b7: v5b7(0x5) = CONST 
    0x5b9: v5b9 = SLOAD v5b7(0x5)
    0x5ba: v5ba(0x0) = CONST 
    0x5bd: v5bd = CALLER 
    0x5be: v5be(0x1) = CONST 
    0x5c0: v5c0(0xa0) = CONST 
    0x5c2: v5c2(0x2) = CONST 
    0x5c4: v5c4(0x10000000000000000000000000000000000000000) = EXP v5c2(0x2), v5c0(0xa0)
    0x5c5: v5c5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c4(0x10000000000000000000000000000000000000000), v5be(0x1)
    0x5c8: v5c8 = AND v5c5(0xffffffffffffffffffffffffffffffffffffffff), v5bd
    0x5ca: v5ca = AND v5b9, v5c5(0xffffffffffffffffffffffffffffffffffffffff)
    0x5cb: v5cb = EQ v5ca, v5c8
    0x5cc: v5cc(0x5d4) = CONST 
    0x5cf: JUMPI v5cc(0x5d4), v5cb

    Begin block 0x5d0
    prev=[0x5b6], succ=[]
    =================================
    0x5d0: v5d0(0x0) = CONST 
    0x5d3: REVERT v5d0(0x0), v5d0(0x0)

    Begin block 0x5d4
    prev=[0x5b6], succ=[0x5e5, 0x5e9]
    =================================
    0x5d5: v5d5(0x1) = CONST 
    0x5d7: v5d7(0xa0) = CONST 
    0x5d9: v5d9(0x2) = CONST 
    0x5db: v5db(0x10000000000000000000000000000000000000000) = EXP v5d9(0x2), v5d7(0xa0)
    0x5dc: v5dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5db(0x10000000000000000000000000000000000000000), v5d5(0x1)
    0x5de: v5de = AND v182, v5dc(0xffffffffffffffffffffffffffffffffffffffff)
    0x5df: v5df = ISZERO v5de
    0x5e0: v5e0 = ISZERO v5df
    0x5e1: v5e1(0x5e9) = CONST 
    0x5e4: JUMPI v5e1(0x5e9), v5e0

    Begin block 0x5e5
    prev=[0x5d4], succ=[]
    =================================
    0x5e5: v5e5(0x0) = CONST 
    0x5e8: REVERT v5e5(0x0), v5e5(0x0)

    Begin block 0x5e9
    prev=[0x5d4], succ=[0x145b]
    =================================
    0x5eb: v5eb(0x5) = CONST 
    0x5ee: v5ee = SLOAD v5eb(0x5)
    0x5ef: v5ef(0x1) = CONST 
    0x5f1: v5f1(0xa0) = CONST 
    0x5f3: v5f3(0x2) = CONST 
    0x5f5: v5f5(0x10000000000000000000000000000000000000000) = EXP v5f3(0x2), v5f1(0xa0)
    0x5f6: v5f6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5f5(0x10000000000000000000000000000000000000000), v5ef(0x1)
    0x5f8: v5f8 = AND v182, v5f6(0xffffffffffffffffffffffffffffffffffffffff)
    0x5f9: v5f9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x60e: v60e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v5f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x611: v611 = AND v5ee, v60e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x612: v612 = OR v611, v5f8
    0x614: SSTORE v5eb(0x5), v612
    0x615: v615(0x1) = CONST 
    0x61a: JUMP v174(0x145b)

    Begin block 0x145b
    prev=[0x5e9], succ=[]
    =================================
    0x145c: v145c(0x40) = CONST 
    0x145f: v145f = MLOAD v145c(0x40)
    0x1461: v1461 = ISZERO v615(0x1)
    0x1462: v1462 = ISZERO v1461
    0x1464: MSTORE v145f, v1462
    0x1465: v1465 = MLOAD v145c(0x40)
    0x1469: v1469(0x0) = SUB v145f, v1465
    0x146a: v146a(0x20) = CONST 
    0x146c: v146c(0x20) = ADD v146a(0x20), v1469(0x0)
    0x146e: RETURN v1465, v146c(0x20)

}

function controllerDelegate()() public {
    Begin block 0x187
    prev=[], succ=[0x18f, 0x193]
    =================================
    0x188: v188 = CALLVALUE 
    0x18a: v18a = ISZERO v188
    0x18b: v18b(0x193) = CONST 
    0x18e: JUMPI v18b(0x193), v18a

    Begin block 0x18f
    prev=[0x187], succ=[]
    =================================
    0x18f: v18f(0x0) = CONST 
    0x192: REVERT v18f(0x0), v18f(0x0)

    Begin block 0x193
    prev=[0x187], succ=[0x61b]
    =================================
    0x195: v195(0x148e) = CONST 
    0x198: v198(0x61b) = CONST 
    0x19b: JUMP v198(0x61b)

    Begin block 0x61b
    prev=[0x193], succ=[0x148e]
    =================================
    0x61c: v61c(0x1) = CONST 
    0x61e: v61e = SLOAD v61c(0x1)
    0x61f: v61f(0x1) = CONST 
    0x621: v621(0xa0) = CONST 
    0x623: v623(0x2) = CONST 
    0x625: v625(0x10000000000000000000000000000000000000000) = EXP v623(0x2), v621(0xa0)
    0x626: v626(0xffffffffffffffffffffffffffffffffffffffff) = SUB v625(0x10000000000000000000000000000000000000000), v61f(0x1)
    0x627: v627 = AND v626(0xffffffffffffffffffffffffffffffffffffffff), v61e
    0x629: JUMP v195(0x148e)

    Begin block 0x148e
    prev=[0x61b], succ=[]
    =================================
    0x148f: v148f(0x40) = CONST 
    0x1492: v1492 = MLOAD v148f(0x40)
    0x1493: v1493(0x1) = CONST 
    0x1495: v1495(0xa0) = CONST 
    0x1497: v1497(0x2) = CONST 
    0x1499: v1499(0x10000000000000000000000000000000000000000) = EXP v1497(0x2), v1495(0xa0)
    0x149a: v149a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1499(0x10000000000000000000000000000000000000000), v1493(0x1)
    0x149d: v149d = AND v627, v149a(0xffffffffffffffffffffffffffffffffffffffff)
    0x149f: MSTORE v1492, v149d
    0x14a0: v14a0 = MLOAD v148f(0x40)
    0x14a4: v14a4(0x0) = SUB v1492, v14a0
    0x14a5: v14a5(0x20) = CONST 
    0x14a7: v14a7(0x20) = ADD v14a5(0x20), v14a4(0x0)
    0x14a9: RETURN v14a0, v14a7(0x20)

}

function withdrawEth(address)() public {
    Begin block 0x1b8
    prev=[], succ=[0x1c0, 0x1c4]
    =================================
    0x1b9: v1b9 = CALLVALUE 
    0x1bb: v1bb = ISZERO v1b9
    0x1bc: v1bc(0x1c4) = CONST 
    0x1bf: JUMPI v1bc(0x1c4), v1bb

    Begin block 0x1c0
    prev=[0x1b8], succ=[]
    =================================
    0x1c0: v1c0(0x0) = CONST 
    0x1c3: REVERT v1c0(0x0), v1c0(0x0)

    Begin block 0x1c4
    prev=[0x1b8], succ=[0x62aB0x1c4]
    =================================
    0x1c6: v1c6(0x14c9) = CONST 
    0x1c9: v1c9(0x1) = CONST 
    0x1cb: v1cb(0xa0) = CONST 
    0x1cd: v1cd(0x2) = CONST 
    0x1cf: v1cf(0x10000000000000000000000000000000000000000) = EXP v1cd(0x2), v1cb(0xa0)
    0x1d0: v1d0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cf(0x10000000000000000000000000000000000000000), v1c9(0x1)
    0x1d1: v1d1(0x4) = CONST 
    0x1d3: v1d3 = CALLDATALOAD v1d1(0x4)
    0x1d4: v1d4 = AND v1d3, v1d0(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d5: v1d5(0x62a) = CONST 
    0x1d8: JUMP v1d5(0x62a)

    Begin block 0x62aB0x1c4
    prev=[0x1c4], succ=[0xee6B0x62aB0x1c4]
    =================================
    0x62bS0x1c4: v62bV1c4(0x0) = CONST 
    0x62eS0x1c4: v62eV1c4(0x636) = CONST 
    0x631S0x1c4: v631V1c4 = CALLER 
    0x632S0x1c4: v632V1c4(0xee6) = CONST 
    0x635S0x1c4: JUMP v632V1c4(0xee6)

    Begin block 0xee6B0x62aB0x1c4
    prev=[0x62aB0x1c4], succ=[0x636B0x1c4]
    =================================
    0xee7S0x62aS0x1c4: vee7V62aV1c4(0x1) = CONST 
    0xee9S0x62aS0x1c4: vee9V62aV1c4(0xa0) = CONST 
    0xeebS0x62aS0x1c4: veebV62aV1c4(0x2) = CONST 
    0xeedS0x62aS0x1c4: veedV62aV1c4(0x10000000000000000000000000000000000000000) = EXP veebV62aV1c4(0x2), vee9V62aV1c4(0xa0)
    0xeeeS0x62aS0x1c4: veeeV62aV1c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedV62aV1c4(0x10000000000000000000000000000000000000000), vee7V62aV1c4(0x1)
    0xeefS0x62aS0x1c4: veefV62aV1c4 = AND veeeV62aV1c4(0xffffffffffffffffffffffffffffffffffffffff), v631V1c4
    0xef0S0x62aS0x1c4: vef0V62aV1c4(0x0) = CONST 
    0xef4S0x62aS0x1c4: MSTORE vef0V62aV1c4(0x0), veefV62aV1c4
    0xef5S0x62aS0x1c4: vef5V62aV1c4(0x6) = CONST 
    0xef7S0x62aS0x1c4: vef7V62aV1c4(0x20) = CONST 
    0xef9S0x62aS0x1c4: MSTORE vef7V62aV1c4(0x20), vef5V62aV1c4(0x6)
    0xefaS0x62aS0x1c4: vefaV62aV1c4(0x40) = CONST 
    0xefdS0x62aS0x1c4: vefdV62aV1c4 = SHA3 vef0V62aV1c4(0x0), vefaV62aV1c4(0x40)
    0xefeS0x62aS0x1c4: vefeV62aV1c4 = SLOAD vefdV62aV1c4
    0xeffS0x62aS0x1c4: veffV62aV1c4 = ISZERO vefeV62aV1c4
    0xf00S0x62aS0x1c4: vf00V62aV1c4 = ISZERO veffV62aV1c4
    0xf02S0x62aS0x1c4: JUMP v62eV1c4(0x636)

    Begin block 0x636B0x1c4
    prev=[0xee6B0x62aB0x1c4], succ=[0x63dB0x1c4, 0x641B0x1c4]
    =================================
    0x637S0x1c4: v637V1c4 = ISZERO vf00V62aV1c4
    0x638S0x1c4: v638V1c4 = ISZERO v637V1c4
    0x639S0x1c4: v639V1c4(0x641) = CONST 
    0x63cS0x1c4: JUMPI v639V1c4(0x641), v638V1c4

    Begin block 0x63dB0x1c4
    prev=[0x636B0x1c4], succ=[]
    =================================
    0x63dS0x1c4: v63dV1c4(0x0) = CONST 
    0x640S0x1c4: REVERT v63dV1c4(0x0), v63dV1c4(0x0)

    Begin block 0x641B0x1c4
    prev=[0x636B0x1c4], succ=[0x6b2B0x1c4, 0x6b6B0x1c4]
    =================================
    0x643S0x1c4: v643V1c4(0x2) = CONST 
    0x645S0x1c4: v645V1c4 = SLOAD v643V1c4(0x2)
    0x646S0x1c4: v646V1c4(0x40) = CONST 
    0x649S0x1c4: v649V1c4 = MLOAD v646V1c4(0x40)
    0x64aS0x1c4: v64aV1c4(0x5b1137b00000000000000000000000000000000000000000000000000000000) = CONST 
    0x66cS0x1c4: MSTORE v649V1c4, v64aV1c4(0x5b1137b00000000000000000000000000000000000000000000000000000000)
    0x66dS0x1c4: v66dV1c4(0x1) = CONST 
    0x66fS0x1c4: v66fV1c4(0xa0) = CONST 
    0x671S0x1c4: v671V1c4(0x2) = CONST 
    0x673S0x1c4: v673V1c4(0x10000000000000000000000000000000000000000) = EXP v671V1c4(0x2), v66fV1c4(0xa0)
    0x674S0x1c4: v674V1c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v673V1c4(0x10000000000000000000000000000000000000000), v66dV1c4(0x1)
    0x677S0x1c4: v677V1c4 = AND v674V1c4(0xffffffffffffffffffffffffffffffffffffffff), v645V1c4
    0x678S0x1c4: v678V1c4(0x4) = CONST 
    0x67bS0x1c4: v67bV1c4 = ADD v649V1c4, v678V1c4(0x4)
    0x67cS0x1c4: MSTORE v67bV1c4, v677V1c4
    0x67fS0x1c4: v67fV1c4 = AND v1d4, v674V1c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x681S0x1c4: v681V1c4 = BALANCE v67fV1c4
    0x682S0x1c4: v682V1c4(0x24) = CONST 
    0x685S0x1c4: v685V1c4 = ADD v649V1c4, v682V1c4(0x24)
    0x688S0x1c4: MSTORE v685V1c4, v681V1c4
    0x68aS0x1c4: v68aV1c4 = MLOAD v646V1c4(0x40)
    0x68fS0x1c4: v68fV1c4(0x5b1137b) = CONST 
    0x695S0x1c4: v695V1c4(0x44) = CONST 
    0x699S0x1c4: v699V1c4 = ADD v649V1c4, v695V1c4(0x44)
    0x69bS0x1c4: v69bV1c4(0x20) = CONST 
    0x6a3S0x1c4: v6a3V1c4(0x0) = SUB v649V1c4, v68aV1c4
    0x6a4S0x1c4: v6a4V1c4(0x44) = ADD v6a3V1c4(0x0), v695V1c4(0x44)
    0x6a6S0x1c4: v6a6V1c4(0x0) = CONST 
    0x6aaS0x1c4: v6aaV1c4 = EXTCODESIZE v67fV1c4
    0x6abS0x1c4: v6abV1c4 = ISZERO v6aaV1c4
    0x6adS0x1c4: v6adV1c4 = ISZERO v6abV1c4
    0x6aeS0x1c4: v6aeV1c4(0x6b6) = CONST 
    0x6b1S0x1c4: JUMPI v6aeV1c4(0x6b6), v6adV1c4

    Begin block 0x6b2B0x1c4
    prev=[0x641B0x1c4], succ=[]
    =================================
    0x6b2S0x1c4: v6b2V1c4(0x0) = CONST 
    0x6b5S0x1c4: REVERT v6b2V1c4(0x0), v6b2V1c4(0x0)

    Begin block 0x6b6B0x1c4
    prev=[0x641B0x1c4], succ=[0x6c1B0x1c4, 0x6caB0x1c4]
    =================================
    0x6b8S0x1c4: v6b8V1c4 = GAS 
    0x6b9S0x1c4: v6b9V1c4 = CALL v6b8V1c4, v67fV1c4, v6a6V1c4(0x0), v68aV1c4, v6a4V1c4(0x44), v68aV1c4, v69bV1c4(0x20)
    0x6baS0x1c4: v6baV1c4 = ISZERO v6b9V1c4
    0x6bcS0x1c4: v6bcV1c4 = ISZERO v6baV1c4
    0x6bdS0x1c4: v6bdV1c4(0x6ca) = CONST 
    0x6c0S0x1c4: JUMPI v6bdV1c4(0x6ca), v6bcV1c4

    Begin block 0x6c1B0x1c4
    prev=[0x6b6B0x1c4], succ=[]
    =================================
    0x6c1S0x1c4: v6c1V1c4 = RETURNDATASIZE 
    0x6c2S0x1c4: v6c2V1c4(0x0) = CONST 
    0x6c5S0x1c4: RETURNDATACOPY v6c2V1c4(0x0), v6c2V1c4(0x0), v6c1V1c4
    0x6c6S0x1c4: v6c6V1c4 = RETURNDATASIZE 
    0x6c7S0x1c4: v6c7V1c4(0x0) = CONST 
    0x6c9S0x1c4: REVERT v6c7V1c4(0x0), v6c6V1c4

    Begin block 0x6caB0x1c4
    prev=[0x6b6B0x1c4], succ=[0x6dcB0x1c4, 0x6e0B0x1c4]
    =================================
    0x6cfS0x1c4: v6cfV1c4(0x40) = CONST 
    0x6d1S0x1c4: v6d1V1c4 = MLOAD v6cfV1c4(0x40)
    0x6d2S0x1c4: v6d2V1c4 = RETURNDATASIZE 
    0x6d3S0x1c4: v6d3V1c4(0x20) = CONST 
    0x6d6S0x1c4: v6d6V1c4 = LT v6d2V1c4, v6d3V1c4(0x20)
    0x6d7S0x1c4: v6d7V1c4 = ISZERO v6d6V1c4
    0x6d8S0x1c4: v6d8V1c4(0x6e0) = CONST 
    0x6dbS0x1c4: JUMPI v6d8V1c4(0x6e0), v6d7V1c4

    Begin block 0x6dcB0x1c4
    prev=[0x6caB0x1c4], succ=[]
    =================================
    0x6dcS0x1c4: v6dcV1c4(0x0) = CONST 
    0x6dfS0x1c4: REVERT v6dcV1c4(0x0), v6dcV1c4(0x0)

    Begin block 0x6e0B0x1c4
    prev=[0x6caB0x1c4], succ=[0x6ebB0x1c4, 0x738B0x1c4]
    =================================
    0x6e2S0x1c4: v6e2V1c4 = MLOAD v6d1V1c4
    0x6e6S0x1c4: v6e6V1c4 = ISZERO v6e2V1c4
    0x6e7S0x1c4: v6e7V1c4(0x738) = CONST 
    0x6eaS0x1c4: JUMPI v6e7V1c4(0x738), v6e6V1c4

    Begin block 0x6ebB0x1c4
    prev=[0x6e0B0x1c4], succ=[0x738B0x1c4]
    =================================
    0x6ebS0x1c4: v6ebV1c4(0x2) = CONST 
    0x6edS0x1c4: v6edV1c4 = SLOAD v6ebV1c4(0x2)
    0x6eeS0x1c4: v6eeV1c4(0x40) = CONST 
    0x6f1S0x1c4: v6f1V1c4 = MLOAD v6eeV1c4(0x40)
    0x6f2S0x1c4: v6f2V1c4(0x1) = CONST 
    0x6f4S0x1c4: v6f4V1c4(0xa0) = CONST 
    0x6f6S0x1c4: v6f6V1c4(0x2) = CONST 
    0x6f8S0x1c4: v6f8V1c4(0x10000000000000000000000000000000000000000) = EXP v6f6V1c4(0x2), v6f4V1c4(0xa0)
    0x6f9S0x1c4: v6f9V1c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6f8V1c4(0x10000000000000000000000000000000000000000), v6f2V1c4(0x1)
    0x6fcS0x1c4: v6fcV1c4 = AND v1d4, v6f9V1c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x6feS0x1c4: MSTORE v6f1V1c4, v6fcV1c4
    0x701S0x1c4: v701V1c4 = AND v6edV1c4, v6f9V1c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x702S0x1c4: v702V1c4(0x20) = CONST 
    0x705S0x1c4: v705V1c4 = ADD v6f1V1c4, v702V1c4(0x20)
    0x706S0x1c4: MSTORE v705V1c4, v701V1c4
    0x709S0x1c4: v709V1c4 = ADD v6eeV1c4(0x40), v6f1V1c4
    0x70cS0x1c4: MSTORE v709V1c4, v681V1c4
    0x70dS0x1c4: v70dV1c4 = MLOAD v6eeV1c4(0x40)
    0x70eS0x1c4: v70eV1c4(0xe70f5b0cde63d9585e55497b8b0a46df83751189868f8b77ddc353ea444f6c19) = CONST 
    0x732S0x1c4: v732V1c4(0x0) = SUB v6f1V1c4, v70dV1c4
    0x733S0x1c4: v733V1c4(0x60) = CONST 
    0x735S0x1c4: v735V1c4(0x60) = ADD v733V1c4(0x60), v732V1c4(0x0)
    0x737S0x1c4: LOG1 v70dV1c4, v735V1c4(0x60), v70eV1c4(0xe70f5b0cde63d9585e55497b8b0a46df83751189868f8b77ddc353ea444f6c19)

    Begin block 0x738B0x1c4
    prev=[0x6ebB0x1c4, 0x6e0B0x1c4], succ=[0x14c9]
    =================================
    0x73dS0x1c4: JUMP v1c6(0x14c9)

    Begin block 0x14c9
    prev=[0x738B0x1c4], succ=[]
    =================================
    0x14ca: v14ca(0x40) = CONST 
    0x14cd: v14cd = MLOAD v14ca(0x40)
    0x14cf: v14cf = ISZERO v6e2V1c4
    0x14d0: v14d0 = ISZERO v14cf
    0x14d2: MSTORE v14cd, v14d0
    0x14d3: v14d3 = MLOAD v14ca(0x40)
    0x14d7: v14d7(0x0) = SUB v14cd, v14d3
    0x14d8: v14d8(0x20) = CONST 
    0x14da: v14da(0x20) = ADD v14d8(0x20), v14d7(0x0)
    0x14dc: RETURN v14d3, v14da(0x20)

}

function gStorage(bytes32)() public {
    Begin block 0x1d9
    prev=[], succ=[0x1e1, 0x1e5]
    =================================
    0x1da: v1da = CALLVALUE 
    0x1dc: v1dc = ISZERO v1da
    0x1dd: v1dd(0x1e5) = CONST 
    0x1e0: JUMPI v1dd(0x1e5), v1dc

    Begin block 0x1e1
    prev=[0x1d9], succ=[]
    =================================
    0x1e1: v1e1(0x0) = CONST 
    0x1e4: REVERT v1e1(0x0), v1e1(0x0)

    Begin block 0x1e5
    prev=[0x1d9], succ=[0x73e]
    =================================
    0x1e7: v1e7(0x14fc) = CONST 
    0x1ea: v1ea(0x4) = CONST 
    0x1ec: v1ec = CALLDATALOAD v1ea(0x4)
    0x1ed: v1ed(0x73e) = CONST 
    0x1f0: JUMP v1ed(0x73e)

    Begin block 0x73e
    prev=[0x1e5], succ=[0x14fc]
    =================================
    0x73f: v73f(0x4) = CONST 
    0x741: v741(0x20) = CONST 
    0x743: MSTORE v741(0x20), v73f(0x4)
    0x744: v744(0x0) = CONST 
    0x748: MSTORE v744(0x0), v1ec
    0x749: v749(0x40) = CONST 
    0x74c: v74c = SHA3 v744(0x0), v749(0x40)
    0x74d: v74d = SLOAD v74c
    0x74f: JUMP v1e7(0x14fc)

    Begin block 0x14fc
    prev=[0x73e], succ=[]
    =================================
    0x14fd: v14fd(0x40) = CONST 
    0x1500: v1500 = MLOAD v14fd(0x40)
    0x1503: MSTORE v1500, v74d
    0x1504: v1504 = MLOAD v14fd(0x40)
    0x1508: v1508(0x0) = SUB v1500, v1504
    0x1509: v1509(0x20) = CONST 
    0x150b: v150b(0x20) = ADD v1509(0x20), v1508(0x0)
    0x150d: RETURN v1504, v150b(0x20)

}

function executeTransaction(address,uint256,bytes)() public {
    Begin block 0x203
    prev=[], succ=[0x20b, 0x20f]
    =================================
    0x204: v204 = CALLVALUE 
    0x206: v206 = ISZERO v204
    0x207: v207(0x20f) = CONST 
    0x20a: JUMPI v207(0x20f), v206

    Begin block 0x20b
    prev=[0x203], succ=[]
    =================================
    0x20b: v20b(0x0) = CONST 
    0x20e: REVERT v20b(0x0), v20b(0x0)

    Begin block 0x20f
    prev=[0x203], succ=[0x750]
    =================================
    0x211: v211(0x40) = CONST 
    0x214: v214 = MLOAD v211(0x40)
    0x215: v215(0x20) = CONST 
    0x217: v217(0x4) = CONST 
    0x219: v219(0x44) = CONST 
    0x21b: v21b = CALLDATALOAD v219(0x44)
    0x21e: v21e = ADD v21b, v217(0x4)
    0x21f: v21f = CALLDATALOAD v21e
    0x220: v220(0x1f) = CONST 
    0x223: v223 = ADD v21f, v220(0x1f)
    0x226: v226 = DIV v223, v215(0x20)
    0x228: v228 = MUL v215(0x20), v226
    0x22a: v22a = ADD v214, v228
    0x22c: v22c = ADD v215(0x20), v22a
    0x22f: MSTORE v211(0x40), v22c
    0x232: MSTORE v214, v21f
    0x233: v233(0x152d) = CONST 
    0x238: v238 = CALLDATALOAD v217(0x4)
    0x239: v239(0x1) = CONST 
    0x23b: v23b(0xa0) = CONST 
    0x23d: v23d(0x2) = CONST 
    0x23f: v23f(0x10000000000000000000000000000000000000000) = EXP v23d(0x2), v23b(0xa0)
    0x240: v240(0xffffffffffffffffffffffffffffffffffffffff) = SUB v23f(0x10000000000000000000000000000000000000000), v239(0x1)
    0x241: v241 = AND v240(0xffffffffffffffffffffffffffffffffffffffff), v238
    0x243: v243(0x24) = CONST 
    0x246: v246 = CALLDATALOAD v243(0x24)
    0x248: v248 = CALLDATASIZE 
    0x24b: v24b(0x64) = CONST 
    0x24f: v24f = ADD v243(0x24), v21b
    0x255: v255 = ADD v214, v215(0x20)
    0x25b: CALLDATACOPY v255, v24f, v21f
    0x260: v260(0x750) = CONST 
    0x26b: JUMP v260(0x750)

    Begin block 0x750
    prev=[0x20f], succ=[0x76a, 0x76e]
    =================================
    0x751: v751(0x5) = CONST 
    0x753: v753 = SLOAD v751(0x5)
    0x754: v754(0x0) = CONST 
    0x757: v757 = CALLER 
    0x758: v758(0x1) = CONST 
    0x75a: v75a(0xa0) = CONST 
    0x75c: v75c(0x2) = CONST 
    0x75e: v75e(0x10000000000000000000000000000000000000000) = EXP v75c(0x2), v75a(0xa0)
    0x75f: v75f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75e(0x10000000000000000000000000000000000000000), v758(0x1)
    0x762: v762 = AND v75f(0xffffffffffffffffffffffffffffffffffffffff), v757
    0x764: v764 = AND v753, v75f(0xffffffffffffffffffffffffffffffffffffffff)
    0x765: v765 = EQ v764, v762
    0x766: v766(0x76e) = CONST 
    0x769: JUMPI v766(0x76e), v765

    Begin block 0x76a
    prev=[0x750], succ=[]
    =================================
    0x76a: v76a(0x0) = CONST 
    0x76d: REVERT v76a(0x0), v76a(0x0)

    Begin block 0x76e
    prev=[0x750], succ=[0x78c]
    =================================
    0x770: v770(0x1) = CONST 
    0x772: v772(0xa0) = CONST 
    0x774: v774(0x2) = CONST 
    0x776: v776(0x10000000000000000000000000000000000000000) = EXP v774(0x2), v772(0xa0)
    0x777: v777(0xffffffffffffffffffffffffffffffffffffffff) = SUB v776(0x10000000000000000000000000000000000000000), v770(0x1)
    0x778: v778 = AND v777(0xffffffffffffffffffffffffffffffffffffffff), v241
    0x77b: v77b(0x40) = CONST 
    0x77d: v77d = MLOAD v77b(0x40)
    0x781: v781 = MLOAD v214
    0x783: v783(0x20) = CONST 
    0x785: v785 = ADD v783(0x20), v214
    0x78a: v78a(0x0) = CONST 

    Begin block 0x78c
    prev=[0x76e, 0x795], succ=[0x7a4, 0x795]
    =================================
    0x78c_0x0: v78c_0 = PHI v78a(0x0), v79f
    0x78f: v78f = LT v78c_0, v781
    0x790: v790 = ISZERO v78f
    0x791: v791(0x7a4) = CONST 
    0x794: JUMPI v791(0x7a4), v790

    Begin block 0x7a4
    prev=[0x78c], succ=[0x7d1, 0x7b8]
    =================================
    0x7ad: v7ad = ADD v781, v77d
    0x7af: v7af(0x1f) = CONST 
    0x7b1: v7b1 = AND v7af(0x1f), v781
    0x7b3: v7b3 = ISZERO v7b1
    0x7b4: v7b4(0x7d1) = CONST 
    0x7b7: JUMPI v7b4(0x7d1), v7b3

    Begin block 0x7d1
    prev=[0x7a4, 0x7b8], succ=[0x152d]
    =================================
    0x7d1_0x1: v7d1_1 = PHI v7ad, v7ce
    0x7d6: v7d6(0x0) = CONST 
    0x7d8: v7d8(0x40) = CONST 
    0x7da: v7da = MLOAD v7d8(0x40)
    0x7dd: v7dd = SUB v7d1_1, v7da
    0x7e1: v7e1 = GAS 
    0x7e2: v7e2 = CALL v7e1, v778, v246, v7da, v7dd, v7da, v7d6(0x0)
    0x7ec: JUMP v233(0x152d)

    Begin block 0x152d
    prev=[0x7d1], succ=[]
    =================================
    0x152e: v152e(0x40) = CONST 
    0x1531: v1531 = MLOAD v152e(0x40)
    0x1533: v1533 = ISZERO v7e2
    0x1534: v1534 = ISZERO v1533
    0x1536: MSTORE v1531, v1534
    0x1537: v1537 = MLOAD v152e(0x40)
    0x153b: v153b(0x0) = SUB v1531, v1537
    0x153c: v153c(0x20) = CONST 
    0x153e: v153e(0x20) = ADD v153c(0x20), v153b(0x0)
    0x1540: RETURN v1537, v153e(0x20)

    Begin block 0x7b8
    prev=[0x7a4], succ=[0x7d1]
    =================================
    0x7ba: v7ba = SUB v7ad, v7b1
    0x7bc: v7bc = MLOAD v7ba
    0x7bd: v7bd(0x1) = CONST 
    0x7c0: v7c0(0x20) = CONST 
    0x7c2: v7c2 = SUB v7c0(0x20), v7b1
    0x7c3: v7c3(0x100) = CONST 
    0x7c6: v7c6 = EXP v7c3(0x100), v7c2
    0x7c7: v7c7 = SUB v7c6, v7bd(0x1)
    0x7c8: v7c8 = NOT v7c7
    0x7c9: v7c9 = AND v7c8, v7bc
    0x7cb: MSTORE v7ba, v7c9
    0x7cc: v7cc(0x20) = CONST 
    0x7ce: v7ce = ADD v7cc(0x20), v7ba

    Begin block 0x795
    prev=[0x78c], succ=[0x78c]
    =================================
    0x795_0x0: v795_0 = PHI v78a(0x0), v79f
    0x797: v797 = ADD v795_0, v785
    0x798: v798 = MLOAD v797
    0x79b: v79b = ADD v795_0, v77d
    0x79c: MSTORE v79b, v798
    0x79d: v79d(0x20) = CONST 
    0x79f: v79f = ADD v79d(0x20), v795_0
    0x7a0: v7a0(0x78c) = CONST 
    0x7a3: JUMP v7a0(0x78c)

}

function setForward(address)() public {
    Begin block 0x26c
    prev=[], succ=[0x274, 0x278]
    =================================
    0x26d: v26d = CALLVALUE 
    0x26f: v26f = ISZERO v26d
    0x270: v270(0x278) = CONST 
    0x273: JUMPI v270(0x278), v26f

    Begin block 0x274
    prev=[0x26c], succ=[]
    =================================
    0x274: v274(0x0) = CONST 
    0x277: REVERT v274(0x0), v274(0x0)

    Begin block 0x278
    prev=[0x26c], succ=[0x7ed]
    =================================
    0x27a: v27a(0x1560) = CONST 
    0x27d: v27d(0x1) = CONST 
    0x27f: v27f(0xa0) = CONST 
    0x281: v281(0x2) = CONST 
    0x283: v283(0x10000000000000000000000000000000000000000) = EXP v281(0x2), v27f(0xa0)
    0x284: v284(0xffffffffffffffffffffffffffffffffffffffff) = SUB v283(0x10000000000000000000000000000000000000000), v27d(0x1)
    0x285: v285(0x4) = CONST 
    0x287: v287 = CALLDATALOAD v285(0x4)
    0x288: v288 = AND v287, v284(0xffffffffffffffffffffffffffffffffffffffff)
    0x289: v289(0x7ed) = CONST 
    0x28c: JUMP v289(0x7ed)

    Begin block 0x7ed
    prev=[0x278], succ=[0x807, 0x80b]
    =================================
    0x7ee: v7ee(0x5) = CONST 
    0x7f0: v7f0 = SLOAD v7ee(0x5)
    0x7f1: v7f1(0x0) = CONST 
    0x7f4: v7f4 = CALLER 
    0x7f5: v7f5(0x1) = CONST 
    0x7f7: v7f7(0xa0) = CONST 
    0x7f9: v7f9(0x2) = CONST 
    0x7fb: v7fb(0x10000000000000000000000000000000000000000) = EXP v7f9(0x2), v7f7(0xa0)
    0x7fc: v7fc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fb(0x10000000000000000000000000000000000000000), v7f5(0x1)
    0x7ff: v7ff = AND v7fc(0xffffffffffffffffffffffffffffffffffffffff), v7f4
    0x801: v801 = AND v7f0, v7fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x802: v802 = EQ v801, v7ff
    0x803: v803(0x80b) = CONST 
    0x806: JUMPI v803(0x80b), v802

    Begin block 0x807
    prev=[0x7ed], succ=[]
    =================================
    0x807: v807(0x0) = CONST 
    0x80a: REVERT v807(0x0), v807(0x0)

    Begin block 0x80b
    prev=[0x7ed], succ=[0x1560]
    =================================
    0x80c: v80c(0x2) = CONST 
    0x80e: v80e = SLOAD v80c(0x2)
    0x80f: v80f(0x40) = CONST 
    0x812: v812 = MLOAD v80f(0x40)
    0x813: v813(0x1) = CONST 
    0x815: v815(0xa0) = CONST 
    0x817: v817(0x2) = CONST 
    0x819: v819(0x10000000000000000000000000000000000000000) = EXP v817(0x2), v815(0xa0)
    0x81a: v81a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v819(0x10000000000000000000000000000000000000000), v813(0x1)
    0x81d: v81d = AND v81a(0xffffffffffffffffffffffffffffffffffffffff), v80e
    0x81f: MSTORE v812, v81d
    0x822: v822 = AND v81a(0xffffffffffffffffffffffffffffffffffffffff), v288
    0x823: v823(0x20) = CONST 
    0x826: v826 = ADD v812, v823(0x20)
    0x827: MSTORE v826, v822
    0x828: v828 = CALLER 
    0x82b: v82b = AND v81a(0xffffffffffffffffffffffffffffffffffffffff), v828
    0x82e: v82e = ADD v80f(0x40), v812
    0x82f: MSTORE v82e, v82b
    0x830: v830 = MLOAD v80f(0x40)
    0x831: v831(0x76a74160015863df9851c834368976525b0049b381d93ef3ec612e7b517ce4c4) = CONST 
    0x855: v855(0x0) = SUB v812, v830
    0x856: v856(0x60) = CONST 
    0x858: v858(0x60) = ADD v856(0x60), v855(0x0)
    0x85a: LOG1 v830, v858(0x60), v831(0x76a74160015863df9851c834368976525b0049b381d93ef3ec612e7b517ce4c4)
    0x85c: v85c(0x2) = CONST 
    0x85f: v85f = SLOAD v85c(0x2)
    0x860: v860(0x1) = CONST 
    0x862: v862(0xa0) = CONST 
    0x864: v864(0x2) = CONST 
    0x866: v866(0x10000000000000000000000000000000000000000) = EXP v864(0x2), v862(0xa0)
    0x867: v867(0xffffffffffffffffffffffffffffffffffffffff) = SUB v866(0x10000000000000000000000000000000000000000), v860(0x1)
    0x869: v869 = AND v288, v867(0xffffffffffffffffffffffffffffffffffffffff)
    0x86a: v86a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x87f: v87f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v86a(0xffffffffffffffffffffffffffffffffffffffff)
    0x882: v882 = AND v85f, v87f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x883: v883 = OR v882, v869
    0x885: SSTORE v85c(0x2), v883
    0x886: v886(0x1) = CONST 
    0x88b: JUMP v27a(0x1560)

    Begin block 0x1560
    prev=[0x80b], succ=[]
    =================================
    0x1561: v1561(0x40) = CONST 
    0x1564: v1564 = MLOAD v1561(0x40)
    0x1566: v1566 = ISZERO v886(0x1)
    0x1567: v1567 = ISZERO v1566
    0x1569: MSTORE v1564, v1567
    0x156a: v156a = MLOAD v1561(0x40)
    0x156e: v156e(0x0) = SUB v1564, v156a
    0x156f: v156f(0x20) = CONST 
    0x1571: v1571(0x20) = ADD v156f(0x20), v156e(0x0)
    0x1573: RETURN v156a, v1571(0x20)

}

function createWallets(uint256)() public {
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
    prev=[0x28d], succ=[0x88c]
    =================================
    0x29b: v29b(0x1593) = CONST 
    0x29e: v29e(0x4) = CONST 
    0x2a0: v2a0 = CALLDATALOAD v29e(0x4)
    0x2a1: v2a1(0x88c) = CONST 
    0x2a4: JUMP v2a1(0x88c)

    Begin block 0x88c
    prev=[0x299], succ=[0xee6B0x88c]
    =================================
    0x88d: v88d(0x0) = CONST 
    0x890: v890(0x898) = CONST 
    0x893: v893 = CALLER 
    0x894: v894(0xee6) = CONST 
    0x897: JUMP v894(0xee6)

    Begin block 0xee6B0x88c
    prev=[0x88c], succ=[0x898]
    =================================
    0xee7S0x88c: vee7V88c(0x1) = CONST 
    0xee9S0x88c: vee9V88c(0xa0) = CONST 
    0xeebS0x88c: veebV88c(0x2) = CONST 
    0xeedS0x88c: veedV88c(0x10000000000000000000000000000000000000000) = EXP veebV88c(0x2), vee9V88c(0xa0)
    0xeeeS0x88c: veeeV88c(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedV88c(0x10000000000000000000000000000000000000000), vee7V88c(0x1)
    0xeefS0x88c: veefV88c = AND veeeV88c(0xffffffffffffffffffffffffffffffffffffffff), v893
    0xef0S0x88c: vef0V88c(0x0) = CONST 
    0xef4S0x88c: MSTORE vef0V88c(0x0), veefV88c
    0xef5S0x88c: vef5V88c(0x6) = CONST 
    0xef7S0x88c: vef7V88c(0x20) = CONST 
    0xef9S0x88c: MSTORE vef7V88c(0x20), vef5V88c(0x6)
    0xefaS0x88c: vefaV88c(0x40) = CONST 
    0xefdS0x88c: vefdV88c = SHA3 vef0V88c(0x0), vefaV88c(0x40)
    0xefeS0x88c: vefeV88c = SLOAD vefdV88c
    0xeffS0x88c: veffV88c = ISZERO vefeV88c
    0xf00S0x88c: vf00V88c = ISZERO veffV88c
    0xf02S0x88c: JUMP v890(0x898)

    Begin block 0x898
    prev=[0xee6B0x88c], succ=[0x89f, 0x8a3]
    =================================
    0x899: v899 = ISZERO vf00V88c
    0x89a: v89a = ISZERO v899
    0x89b: v89b(0x8a3) = CONST 
    0x89e: JUMPI v89b(0x8a3), v89a

    Begin block 0x89f
    prev=[0x898], succ=[]
    =================================
    0x89f: v89f(0x0) = CONST 
    0x8a2: REVERT v89f(0x0), v89f(0x0)

    Begin block 0x8a3
    prev=[0x898], succ=[0x8a7]
    =================================
    0x8a5: v8a5(0x0) = CONST 

    Begin block 0x8a7
    prev=[0x8a3, 0x8f4], succ=[0x8b0, 0x918]
    =================================
    0x8a7_0x0: v8a7_0 = PHI v8a5(0x0), v913
    0x8aa: v8aa = LT v8a7_0, v2a0
    0x8ab: v8ab = ISZERO v8aa
    0x8ac: v8ac(0x918) = CONST 
    0x8af: JUMPI v8ac(0x918), v8ab

    Begin block 0x8b0
    prev=[0x8a7], succ=[0x110d]
    =================================
    0x8b0: v8b0(0x814288eb1684a10181d25f8b2be20cd2f559850b6578bc9a5bb55a2478af882) = CONST 
    0x8d1: v8d1(0x8d8) = CONST 
    0x8d4: v8d4(0x110d) = CONST 
    0x8d7: JUMP v8d4(0x110d)

    Begin block 0x110d
    prev=[0x8b0], succ=[0x8d8]
    =================================
    0x110e: v110e(0x40) = CONST 
    0x1110: v1110 = MLOAD v110e(0x40)
    0x1111: v1111(0x27a) = CONST 
    0x1115: v1115(0x1164) = CONST 
    0x1119: CODECOPY v1110, v1115(0x1164), v1111(0x27a)
    0x111a: v111a = ADD v1111(0x27a), v1110
    0x111c: JUMP v8d1(0x8d8)

    Begin block 0x8d8
    prev=[0x110d], succ=[0x8eb, 0x8f4]
    =================================
    0x8d9: v8d9(0x40) = CONST 
    0x8db: v8db = MLOAD v8d9(0x40)
    0x8de: v8de(0x27a) = SUB v111a, v8db
    0x8e0: v8e0(0x0) = CONST 
    0x8e2: v8e2 = CREATE v8e0(0x0), v8db, v8de(0x27a)
    0x8e4: v8e4 = ISZERO v8e2
    0x8e6: v8e6 = ISZERO v8e4
    0x8e7: v8e7(0x8f4) = CONST 
    0x8ea: JUMPI v8e7(0x8f4), v8e6

    Begin block 0x8eb
    prev=[0x8d8], succ=[]
    =================================
    0x8eb: v8eb = RETURNDATASIZE 
    0x8ec: v8ec(0x0) = CONST 
    0x8ef: RETURNDATACOPY v8ec(0x0), v8ec(0x0), v8eb
    0x8f0: v8f0 = RETURNDATASIZE 
    0x8f1: v8f1(0x0) = CONST 
    0x8f3: REVERT v8f1(0x0), v8f0

    Begin block 0x8f4
    prev=[0x8d8], succ=[0x8a7]
    =================================
    0x8f4_0x3: v8f4_3 = PHI v8a5(0x0), v913
    0x8f6: v8f6(0x40) = CONST 
    0x8f9: v8f9 = MLOAD v8f6(0x40)
    0x8fa: v8fa(0x1) = CONST 
    0x8fc: v8fc(0xa0) = CONST 
    0x8fe: v8fe(0x2) = CONST 
    0x900: v900(0x10000000000000000000000000000000000000000) = EXP v8fe(0x2), v8fc(0xa0)
    0x901: v901(0xffffffffffffffffffffffffffffffffffffffff) = SUB v900(0x10000000000000000000000000000000000000000), v8fa(0x1)
    0x904: v904 = AND v8e2, v901(0xffffffffffffffffffffffffffffffffffffffff)
    0x906: MSTORE v8f9, v904
    0x907: v907 = MLOAD v8f6(0x40)
    0x90b: v90b(0x0) = SUB v8f9, v907
    0x90c: v90c(0x20) = CONST 
    0x90e: v90e(0x20) = ADD v90c(0x20), v90b(0x0)
    0x910: LOG1 v907, v90e(0x20), v8b0(0x814288eb1684a10181d25f8b2be20cd2f559850b6578bc9a5bb55a2478af882)
    0x911: v911(0x1) = CONST 
    0x913: v913 = ADD v911(0x1), v8f4_3
    0x914: v914(0x8a7) = CONST 
    0x917: JUMP v914(0x8a7)

    Begin block 0x918
    prev=[0x8a7], succ=[0x1593]
    =================================
    0x91b: v91b(0x3) = CONST 
    0x91e: v91e = SLOAD v91b(0x3)
    0x922: v922 = ADD v91e, v2a0
    0x924: SSTORE v91b(0x3), v922
    0x925: v925(0x1) = CONST 
    0x928: JUMP v29b(0x1593)

    Begin block 0x1593
    prev=[0x918], succ=[]
    =================================
    0x1594: v1594(0x40) = CONST 
    0x1597: v1597 = MLOAD v1594(0x40)
    0x1599: v1599 = ISZERO v925(0x1)
    0x159a: v159a = ISZERO v1599
    0x159c: MSTORE v1597, v159a
    0x159d: v159d = MLOAD v1594(0x40)
    0x15a1: v15a1(0x0) = SUB v1597, v159d
    0x15a2: v15a2(0x20) = CONST 
    0x15a4: v15a4(0x20) = ADD v15a2(0x20), v15a1(0x0)
    0x15a6: RETURN v159d, v15a4(0x20)

}

function addWorker(address)() public {
    Begin block 0x2a5
    prev=[], succ=[0x2ad, 0x2b1]
    =================================
    0x2a6: v2a6 = CALLVALUE 
    0x2a8: v2a8 = ISZERO v2a6
    0x2a9: v2a9(0x2b1) = CONST 
    0x2ac: JUMPI v2a9(0x2b1), v2a8

    Begin block 0x2ad
    prev=[0x2a5], succ=[]
    =================================
    0x2ad: v2ad(0x0) = CONST 
    0x2b0: REVERT v2ad(0x0), v2ad(0x0)

    Begin block 0x2b1
    prev=[0x2a5], succ=[0x929]
    =================================
    0x2b3: v2b3(0x15c6) = CONST 
    0x2b6: v2b6(0x1) = CONST 
    0x2b8: v2b8(0xa0) = CONST 
    0x2ba: v2ba(0x2) = CONST 
    0x2bc: v2bc(0x10000000000000000000000000000000000000000) = EXP v2ba(0x2), v2b8(0xa0)
    0x2bd: v2bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2bc(0x10000000000000000000000000000000000000000), v2b6(0x1)
    0x2be: v2be(0x4) = CONST 
    0x2c0: v2c0 = CALLDATALOAD v2be(0x4)
    0x2c1: v2c1 = AND v2c0, v2bd(0xffffffffffffffffffffffffffffffffffffffff)
    0x2c2: v2c2(0x929) = CONST 
    0x2c5: JUMP v2c2(0x929)

    Begin block 0x929
    prev=[0x2b1], succ=[0x945, 0x949]
    =================================
    0x92a: v92a(0x5) = CONST 
    0x92c: v92c = SLOAD v92a(0x5)
    0x92d: v92d(0x0) = CONST 
    0x932: v932 = CALLER 
    0x933: v933(0x1) = CONST 
    0x935: v935(0xa0) = CONST 
    0x937: v937(0x2) = CONST 
    0x939: v939(0x10000000000000000000000000000000000000000) = EXP v937(0x2), v935(0xa0)
    0x93a: v93a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v939(0x10000000000000000000000000000000000000000), v933(0x1)
    0x93d: v93d = AND v93a(0xffffffffffffffffffffffffffffffffffffffff), v932
    0x93f: v93f = AND v92c, v93a(0xffffffffffffffffffffffffffffffffffffffff)
    0x940: v940 = EQ v93f, v93d
    0x941: v941(0x949) = CONST 
    0x944: JUMPI v941(0x949), v940

    Begin block 0x945
    prev=[0x929], succ=[]
    =================================
    0x945: v945(0x0) = CONST 
    0x948: REVERT v945(0x0), v945(0x0)

    Begin block 0x949
    prev=[0x929], succ=[0xee6B0x949]
    =================================
    0x94a: v94a(0x952) = CONST 
    0x94e: v94e(0xee6) = CONST 
    0x951: JUMP v94e(0xee6)

    Begin block 0xee6B0x949
    prev=[0x949], succ=[0x952]
    =================================
    0xee7S0x949: vee7V949(0x1) = CONST 
    0xee9S0x949: vee9V949(0xa0) = CONST 
    0xeebS0x949: veebV949(0x2) = CONST 
    0xeedS0x949: veedV949(0x10000000000000000000000000000000000000000) = EXP veebV949(0x2), vee9V949(0xa0)
    0xeeeS0x949: veeeV949(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedV949(0x10000000000000000000000000000000000000000), vee7V949(0x1)
    0xeefS0x949: veefV949 = AND veeeV949(0xffffffffffffffffffffffffffffffffffffffff), v2c1
    0xef0S0x949: vef0V949(0x0) = CONST 
    0xef4S0x949: MSTORE vef0V949(0x0), veefV949
    0xef5S0x949: vef5V949(0x6) = CONST 
    0xef7S0x949: vef7V949(0x20) = CONST 
    0xef9S0x949: MSTORE vef7V949(0x20), vef5V949(0x6)
    0xefaS0x949: vefaV949(0x40) = CONST 
    0xefdS0x949: vefdV949 = SHA3 vef0V949(0x0), vefaV949(0x40)
    0xefeS0x949: vefeV949 = SLOAD vefdV949
    0xeffS0x949: veffV949 = ISZERO vefeV949
    0xf00S0x949: vf00V949 = ISZERO veffV949
    0xf02S0x949: JUMP v94a(0x952)

    Begin block 0x952
    prev=[0xee6B0x949], succ=[0x958, 0x95c]
    =================================
    0x953: v953 = ISZERO vf00V949
    0x954: v954(0x95c) = CONST 
    0x957: JUMPI v954(0x95c), v953

    Begin block 0x958
    prev=[0x952], succ=[]
    =================================
    0x958: v958(0x0) = CONST 
    0x95b: REVERT v958(0x0), v958(0x0)

    Begin block 0x95c
    prev=[0x952], succ=[0x15c6]
    =================================
    0x95e: v95e(0x7) = CONST 
    0x961: v961 = SLOAD v95e(0x7)
    0x962: v962(0x1) = CONST 
    0x965: v965 = ADD v961, v962(0x1)
    0x968: SSTORE v95e(0x7), v965
    0x969: v969(0xa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c688) = CONST 
    0x98b: v98b = ADD v961, v969(0xa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c688)
    0x98d: v98d = SLOAD v98b
    0x98e: v98e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9a3: v9a3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v98e(0xffffffffffffffffffffffffffffffffffffffff)
    0x9a4: v9a4 = AND v9a3(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v98d
    0x9a5: v9a5(0x1) = CONST 
    0x9a7: v9a7(0xa0) = CONST 
    0x9a9: v9a9(0x2) = CONST 
    0x9ab: v9ab(0x10000000000000000000000000000000000000000) = EXP v9a9(0x2), v9a7(0xa0)
    0x9ac: v9ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9ab(0x10000000000000000000000000000000000000000), v9a5(0x1)
    0x9ae: v9ae = AND v2c1, v9ac(0xffffffffffffffffffffffffffffffffffffffff)
    0x9b1: v9b1 = OR v9ae, v9a4
    0x9b4: SSTORE v98b, v9b1
    0x9b5: v9b5(0x0) = CONST 
    0x9b9: MSTORE v9b5(0x0), v9ae
    0x9ba: v9ba(0x6) = CONST 
    0x9bc: v9bc(0x20) = CONST 
    0x9c0: MSTORE v9bc(0x20), v9ba(0x6)
    0x9c1: v9c1(0x40) = CONST 
    0x9c6: v9c6 = SHA3 v9b5(0x0), v9c1(0x40)
    0x9c9: SSTORE v9c6, v961
    0x9cb: v9cb = MLOAD v9c1(0x40)
    0x9ce: MSTORE v9cb, v9ae
    0x9d0: v9d0 = MLOAD v9c1(0x40)
    0x9d1: v9d1(0xdecaaccf65fa0157d575425d16efcccc089f3df91ee0abedec8d1def2f12ab39) = CONST 
    0x9f5: v9f5(0x0) = SUB v9cb, v9d0
    0x9f8: v9f8(0x20) = ADD v9bc(0x20), v9f5(0x0)
    0x9fa: LOG1 v9d0, v9f8(0x20), v9d1(0xdecaaccf65fa0157d575425d16efcccc089f3df91ee0abedec8d1def2f12ab39)
    0x9fc: v9fc(0x1) = CONST 
    0xa02: JUMP v2b3(0x15c6)

    Begin block 0x15c6
    prev=[0x95c], succ=[]
    =================================
    0x15c7: v15c7(0x40) = CONST 
    0x15ca: v15ca = MLOAD v15c7(0x40)
    0x15cc: v15cc = ISZERO v9fc(0x1)
    0x15cd: v15cd = ISZERO v15cc
    0x15cf: MSTORE v15ca, v15cd
    0x15d0: v15d0 = MLOAD v15c7(0x40)
    0x15d4: v15d4(0x0) = SUB v15ca, v15d0
    0x15d5: v15d5(0x20) = CONST 
    0x15d7: v15d7(0x20) = ADD v15d5(0x20), v15d4(0x0)
    0x15d9: RETURN v15d0, v15d7(0x20)

}

function withdrawERC20Batch(address,address[])() public {
    Begin block 0x2c6
    prev=[], succ=[0x2ce, 0x2d2]
    =================================
    0x2c7: v2c7 = CALLVALUE 
    0x2c9: v2c9 = ISZERO v2c7
    0x2ca: v2ca(0x2d2) = CONST 
    0x2cd: JUMPI v2ca(0x2d2), v2c9

    Begin block 0x2ce
    prev=[0x2c6], succ=[]
    =================================
    0x2ce: v2ce(0x0) = CONST 
    0x2d1: REVERT v2ce(0x0), v2ce(0x0)

    Begin block 0x2d2
    prev=[0x2c6], succ=[0xa03]
    =================================
    0x2d4: v2d4(0x40) = CONST 
    0x2d7: v2d7 = MLOAD v2d4(0x40)
    0x2d8: v2d8(0x20) = CONST 
    0x2da: v2da(0x4) = CONST 
    0x2dc: v2dc(0x24) = CONST 
    0x2df: v2df = CALLDATALOAD v2dc(0x24)
    0x2e2: v2e2 = ADD v2df, v2da(0x4)
    0x2e3: v2e3 = CALLDATALOAD v2e2
    0x2e6: v2e6 = MUL v2e3, v2d8(0x20)
    0x2e9: v2e9 = ADD v2d7, v2e6
    0x2eb: v2eb = ADD v2d8(0x20), v2e9
    0x2ee: MSTORE v2d4(0x40), v2eb
    0x2f1: MSTORE v2d7, v2e3
    0x2f2: v2f2(0x15f9) = CONST 
    0x2f7: v2f7 = CALLDATALOAD v2da(0x4)
    0x2f8: v2f8(0x1) = CONST 
    0x2fa: v2fa(0xa0) = CONST 
    0x2fc: v2fc(0x2) = CONST 
    0x2fe: v2fe(0x10000000000000000000000000000000000000000) = EXP v2fc(0x2), v2fa(0xa0)
    0x2ff: v2ff(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2fe(0x10000000000000000000000000000000000000000), v2f8(0x1)
    0x300: v300 = AND v2ff(0xffffffffffffffffffffffffffffffffffffffff), v2f7
    0x302: v302 = CALLDATASIZE 
    0x304: v304(0x44) = CONST 
    0x30b: v30b = ADD v2dc(0x24), v2df
    0x311: v311 = ADD v2d7, v2d8(0x20)
    0x318: CALLDATACOPY v311, v30b, v2e6
    0x31d: v31d(0xa03) = CONST 
    0x328: JUMP v31d(0xa03)

    Begin block 0xa03
    prev=[0x2d2], succ=[0xee6B0xa03]
    =================================
    0xa04: va04(0x0) = CONST 
    0xa07: va07(0x0) = CONST 
    0xa0a: va0a(0x0) = CONST 
    0xa0c: va0c(0xa14) = CONST 
    0xa0f: va0f = CALLER 
    0xa10: va10(0xee6) = CONST 
    0xa13: JUMP va10(0xee6)

    Begin block 0xee6B0xa03
    prev=[0xa03], succ=[0xa14]
    =================================
    0xee7S0xa03: vee7Va03(0x1) = CONST 
    0xee9S0xa03: vee9Va03(0xa0) = CONST 
    0xeebS0xa03: veebVa03(0x2) = CONST 
    0xeedS0xa03: veedVa03(0x10000000000000000000000000000000000000000) = EXP veebVa03(0x2), vee9Va03(0xa0)
    0xeeeS0xa03: veeeVa03(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedVa03(0x10000000000000000000000000000000000000000), vee7Va03(0x1)
    0xeefS0xa03: veefVa03 = AND veeeVa03(0xffffffffffffffffffffffffffffffffffffffff), va0f
    0xef0S0xa03: vef0Va03(0x0) = CONST 
    0xef4S0xa03: MSTORE vef0Va03(0x0), veefVa03
    0xef5S0xa03: vef5Va03(0x6) = CONST 
    0xef7S0xa03: vef7Va03(0x20) = CONST 
    0xef9S0xa03: MSTORE vef7Va03(0x20), vef5Va03(0x6)
    0xefaS0xa03: vefaVa03(0x40) = CONST 
    0xefdS0xa03: vefdVa03 = SHA3 vef0Va03(0x0), vefaVa03(0x40)
    0xefeS0xa03: vefeVa03 = SLOAD vefdVa03
    0xeffS0xa03: veffVa03 = ISZERO vefeVa03
    0xf00S0xa03: vf00Va03 = ISZERO veffVa03
    0xf02S0xa03: JUMP va0c(0xa14)

    Begin block 0xa14
    prev=[0xee6B0xa03], succ=[0xa1b, 0xa1f]
    =================================
    0xa15: va15 = ISZERO vf00Va03
    0xa16: va16 = ISZERO va15
    0xa17: va17(0xa1f) = CONST 
    0xa1a: JUMPI va17(0xa1f), va16

    Begin block 0xa1b
    prev=[0xa14], succ=[]
    =================================
    0xa1b: va1b(0x0) = CONST 
    0xa1e: REVERT va1b(0x0), va1b(0x0)

    Begin block 0xa1f
    prev=[0xa14], succ=[0xa27]
    =================================
    0xa22: va22 = MLOAD v2d7
    0xa25: va25(0x0) = CONST 

    Begin block 0xa27
    prev=[0xa1f, 0xbd7], succ=[0xbdf, 0xa30]
    =================================
    0xa27_0x0: va27_0 = PHI va25(0x0), vbda
    0xa2a: va2a = LT va27_0, va22
    0xa2b: va2b = ISZERO va2a
    0xa2c: va2c(0xbdf) = CONST 
    0xa2f: JUMPI va2c(0xbdf), va2b

    Begin block 0xbdf
    prev=[0xa27], succ=[0xc43, 0xc47]
    =================================
    0xbe0: vbe0(0x2) = CONST 
    0xbe2: vbe2 = SLOAD vbe0(0x2)
    0xbe3: vbe3(0x40) = CONST 
    0xbe6: vbe6 = MLOAD vbe3(0x40)
    0xbe7: vbe7(0xc69e546d00000000000000000000000000000000000000000000000000000000) = CONST 
    0xc09: MSTORE vbe6, vbe7(0xc69e546d00000000000000000000000000000000000000000000000000000000)
    0xc0a: vc0a(0x1) = CONST 
    0xc0c: vc0c(0xa0) = CONST 
    0xc0e: vc0e(0x2) = CONST 
    0xc10: vc10(0x10000000000000000000000000000000000000000) = EXP vc0e(0x2), vc0c(0xa0)
    0xc11: vc11(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc10(0x10000000000000000000000000000000000000000), vc0a(0x1)
    0xc14: vc14 = AND vc11(0xffffffffffffffffffffffffffffffffffffffff), v300
    0xc15: vc15(0x4) = CONST 
    0xc18: vc18 = ADD vbe6, vc15(0x4)
    0xc19: MSTORE vc18, vc14
    0xc1b: vc1b = MLOAD vbe3(0x40)
    0xc1f: vc1f = AND vbe2, vc11(0xffffffffffffffffffffffffffffffffffffffff)
    0xc21: vc21(0xc69e546d) = CONST 
    0xc27: vc27(0x24) = CONST 
    0xc2b: vc2b = ADD vbe6, vc27(0x24)
    0xc2d: vc2d(0x20) = CONST 
    0xc34: vc34(0x0) = SUB vbe6, vc1b
    0xc35: vc35(0x24) = ADD vc34(0x0), vc27(0x24)
    0xc37: vc37(0x0) = CONST 
    0xc3b: vc3b = EXTCODESIZE vc1f
    0xc3c: vc3c = ISZERO vc3b
    0xc3e: vc3e = ISZERO vc3c
    0xc3f: vc3f(0xc47) = CONST 
    0xc42: JUMPI vc3f(0xc47), vc3e

    Begin block 0xc43
    prev=[0xbdf], succ=[]
    =================================
    0xc43: vc43(0x0) = CONST 
    0xc46: REVERT vc43(0x0), vc43(0x0)

    Begin block 0xc47
    prev=[0xbdf], succ=[0xc52, 0xc5b]
    =================================
    0xc49: vc49 = GAS 
    0xc4a: vc4a = CALL vc49, vc1f, vc37(0x0), vc1b, vc35(0x24), vc1b, vc2d(0x20)
    0xc4b: vc4b = ISZERO vc4a
    0xc4d: vc4d = ISZERO vc4b
    0xc4e: vc4e(0xc5b) = CONST 
    0xc51: JUMPI vc4e(0xc5b), vc4d

    Begin block 0xc52
    prev=[0xc47], succ=[]
    =================================
    0xc52: vc52 = RETURNDATASIZE 
    0xc53: vc53(0x0) = CONST 
    0xc56: RETURNDATACOPY vc53(0x0), vc53(0x0), vc52
    0xc57: vc57 = RETURNDATASIZE 
    0xc58: vc58(0x0) = CONST 
    0xc5a: REVERT vc58(0x0), vc57

    Begin block 0xc5b
    prev=[0xc47], succ=[0xc6d, 0xc71]
    =================================
    0xc60: vc60(0x40) = CONST 
    0xc62: vc62 = MLOAD vc60(0x40)
    0xc63: vc63 = RETURNDATASIZE 
    0xc64: vc64(0x20) = CONST 
    0xc67: vc67 = LT vc63, vc64(0x20)
    0xc68: vc68 = ISZERO vc67
    0xc69: vc69(0xc71) = CONST 
    0xc6c: JUMPI vc69(0xc71), vc68

    Begin block 0xc6d
    prev=[0xc5b], succ=[]
    =================================
    0xc6d: vc6d(0x0) = CONST 
    0xc70: REVERT vc6d(0x0), vc6d(0x0)

    Begin block 0xc71
    prev=[0xc5b], succ=[0x15f9]
    =================================
    0xc73: vc73(0x1) = CONST 
    0xc7f: JUMP v2f2(0x15f9)

    Begin block 0x15f9
    prev=[0xc71], succ=[]
    =================================
    0x15fa: v15fa(0x40) = CONST 
    0x15fd: v15fd = MLOAD v15fa(0x40)
    0x15ff: v15ff = ISZERO vc73(0x1)
    0x1600: v1600 = ISZERO v15ff
    0x1602: MSTORE v15fd, v1600
    0x1603: v1603 = MLOAD v15fa(0x40)
    0x1607: v1607(0x0) = SUB v15fd, v1603
    0x1608: v1608(0x20) = CONST 
    0x160a: v160a(0x20) = ADD v1608(0x20), v1607(0x0)
    0x160c: RETURN v1603, v160a(0x20)

    Begin block 0xa30
    prev=[0xa27], succ=[0xa3c, 0xa3d]
    =================================
    0xa30_0x0: va30_0 = PHI va25(0x0), vbda
    0xa33: va33 = MLOAD v2d7
    0xa35: va35 = LT va30_0, va33
    0xa36: va36 = ISZERO va35
    0xa37: va37 = ISZERO va36
    0xa38: va38(0xa3d) = CONST 
    0xa3b: JUMPI va38(0xa3d), va37

    Begin block 0xa3c
    prev=[0xa30], succ=[]
    =================================
    0xa3c: THROW 

    Begin block 0xa3d
    prev=[0xa30], succ=[0xaa6, 0xaaa]
    =================================
    0xa3d_0x0: va3d_0 = PHI va25(0x0), vbda
    0xa3e: va3e(0x20) = CONST 
    0xa42: va42 = MUL va3e(0x20), va3d_0
    0xa45: va45 = ADD v2d7, va42
    0xa47: va47 = ADD va3e(0x20), va45
    0xa48: va48 = MLOAD va47
    0xa49: va49(0x40) = CONST 
    0xa4c: va4c = MLOAD va49(0x40)
    0xa4d: va4d(0x70a0823100000000000000000000000000000000000000000000000000000000) = CONST 
    0xa6f: MSTORE va4c, va4d(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0xa70: va70(0x1) = CONST 
    0xa72: va72(0xa0) = CONST 
    0xa74: va74(0x2) = CONST 
    0xa76: va76(0x10000000000000000000000000000000000000000) = EXP va74(0x2), va72(0xa0)
    0xa77: va77(0xffffffffffffffffffffffffffffffffffffffff) = SUB va76(0x10000000000000000000000000000000000000000), va70(0x1)
    0xa7a: va7a = AND va48, va77(0xffffffffffffffffffffffffffffffffffffffff)
    0xa7b: va7b(0x4) = CONST 
    0xa7e: va7e = ADD va4c, va7b(0x4)
    0xa7f: MSTORE va7e, va7a
    0xa81: va81 = MLOAD va49(0x40)
    0xa87: va87 = AND v300, va77(0xffffffffffffffffffffffffffffffffffffffff)
    0xa89: va89(0x70a08231) = CONST 
    0xa8f: va8f(0x24) = CONST 
    0xa93: va93 = ADD va4c, va8f(0x24)
    0xa97: va97(0x0) = SUB va4c, va81
    0xa98: va98(0x24) = ADD va97(0x0), va8f(0x24)
    0xa9a: va9a(0x0) = CONST 
    0xa9e: va9e = EXTCODESIZE va87
    0xa9f: va9f = ISZERO va9e
    0xaa1: vaa1 = ISZERO va9f
    0xaa2: vaa2(0xaaa) = CONST 
    0xaa5: JUMPI vaa2(0xaaa), vaa1

    Begin block 0xaa6
    prev=[0xa3d], succ=[]
    =================================
    0xaa6: vaa6(0x0) = CONST 
    0xaa9: REVERT vaa6(0x0), vaa6(0x0)

    Begin block 0xaaa
    prev=[0xa3d], succ=[0xab5, 0xabe]
    =================================
    0xaac: vaac = GAS 
    0xaad: vaad = CALL vaac, va87, va9a(0x0), va81, va98(0x24), va81, va3e(0x20)
    0xaae: vaae = ISZERO vaad
    0xab0: vab0 = ISZERO vaae
    0xab1: vab1(0xabe) = CONST 
    0xab4: JUMPI vab1(0xabe), vab0

    Begin block 0xab5
    prev=[0xaaa], succ=[]
    =================================
    0xab5: vab5 = RETURNDATASIZE 
    0xab6: vab6(0x0) = CONST 
    0xab9: RETURNDATACOPY vab6(0x0), vab6(0x0), vab5
    0xaba: vaba = RETURNDATASIZE 
    0xabb: vabb(0x0) = CONST 
    0xabd: REVERT vabb(0x0), vaba

    Begin block 0xabe
    prev=[0xaaa], succ=[0xad0, 0xad4]
    =================================
    0xac3: vac3(0x40) = CONST 
    0xac5: vac5 = MLOAD vac3(0x40)
    0xac6: vac6 = RETURNDATASIZE 
    0xac7: vac7(0x20) = CONST 
    0xaca: vaca = LT vac6, vac7(0x20)
    0xacb: vacb = ISZERO vaca
    0xacc: vacc(0xad4) = CONST 
    0xacf: JUMPI vacc(0xad4), vacb

    Begin block 0xad0
    prev=[0xabe], succ=[]
    =================================
    0xad0: vad0(0x0) = CONST 
    0xad3: REVERT vad0(0x0), vad0(0x0)

    Begin block 0xad4
    prev=[0xabe], succ=[0xb4c, 0xb50]
    =================================
    0xad6: vad6 = MLOAD vac5
    0xad7: vad7(0x2) = CONST 
    0xad9: vad9 = SLOAD vad7(0x2)
    0xada: vada(0x40) = CONST 
    0xadd: vadd = MLOAD vada(0x40)
    0xade: vade(0x92940bf900000000000000000000000000000000000000000000000000000000) = CONST 
    0xb00: MSTORE vadd, vade(0x92940bf900000000000000000000000000000000000000000000000000000000)
    0xb01: vb01(0x1) = CONST 
    0xb03: vb03(0xa0) = CONST 
    0xb05: vb05(0x2) = CONST 
    0xb07: vb07(0x10000000000000000000000000000000000000000) = EXP vb05(0x2), vb03(0xa0)
    0xb08: vb08(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb07(0x10000000000000000000000000000000000000000), vb01(0x1)
    0xb0b: vb0b = AND vb08(0xffffffffffffffffffffffffffffffffffffffff), v300
    0xb0c: vb0c(0x4) = CONST 
    0xb0f: vb0f = ADD vadd, vb0c(0x4)
    0xb10: MSTORE vb0f, vb0b
    0xb13: vb13 = AND vb08(0xffffffffffffffffffffffffffffffffffffffff), vad9
    0xb14: vb14(0x24) = CONST 
    0xb17: vb17 = ADD vadd, vb14(0x24)
    0xb18: MSTORE vb17, vb13
    0xb19: vb19(0x44) = CONST 
    0xb1c: vb1c = ADD vadd, vb19(0x44)
    0xb1f: MSTORE vb1c, vad6
    0xb21: vb21 = MLOAD vada(0x40)
    0xb27: vb27 = AND va48, vb08(0xffffffffffffffffffffffffffffffffffffffff)
    0xb29: vb29(0x92940bf9) = CONST 
    0xb2f: vb2f(0x64) = CONST 
    0xb33: vb33 = ADD vadd, vb2f(0x64)
    0xb35: vb35(0x20) = CONST 
    0xb3d: vb3d(0x0) = SUB vadd, vb21
    0xb3e: vb3e(0x64) = ADD vb3d(0x0), vb2f(0x64)
    0xb40: vb40(0x0) = CONST 
    0xb44: vb44 = EXTCODESIZE vb27
    0xb45: vb45 = ISZERO vb44
    0xb47: vb47 = ISZERO vb45
    0xb48: vb48(0xb50) = CONST 
    0xb4b: JUMPI vb48(0xb50), vb47

    Begin block 0xb4c
    prev=[0xad4], succ=[]
    =================================
    0xb4c: vb4c(0x0) = CONST 
    0xb4f: REVERT vb4c(0x0), vb4c(0x0)

    Begin block 0xb50
    prev=[0xad4], succ=[0xb5b, 0xb64]
    =================================
    0xb52: vb52 = GAS 
    0xb53: vb53 = CALL vb52, vb27, vb40(0x0), vb21, vb3e(0x64), vb21, vb35(0x20)
    0xb54: vb54 = ISZERO vb53
    0xb56: vb56 = ISZERO vb54
    0xb57: vb57(0xb64) = CONST 
    0xb5a: JUMPI vb57(0xb64), vb56

    Begin block 0xb5b
    prev=[0xb50], succ=[]
    =================================
    0xb5b: vb5b = RETURNDATASIZE 
    0xb5c: vb5c(0x0) = CONST 
    0xb5f: RETURNDATACOPY vb5c(0x0), vb5c(0x0), vb5b
    0xb60: vb60 = RETURNDATASIZE 
    0xb61: vb61(0x0) = CONST 
    0xb63: REVERT vb61(0x0), vb60

    Begin block 0xb64
    prev=[0xb50], succ=[0xb76, 0xb7a]
    =================================
    0xb69: vb69(0x40) = CONST 
    0xb6b: vb6b = MLOAD vb69(0x40)
    0xb6c: vb6c = RETURNDATASIZE 
    0xb6d: vb6d(0x20) = CONST 
    0xb70: vb70 = LT vb6c, vb6d(0x20)
    0xb71: vb71 = ISZERO vb70
    0xb72: vb72(0xb7a) = CONST 
    0xb75: JUMPI vb72(0xb7a), vb71

    Begin block 0xb76
    prev=[0xb64], succ=[]
    =================================
    0xb76: vb76(0x0) = CONST 
    0xb79: REVERT vb76(0x0), vb76(0x0)

    Begin block 0xb7a
    prev=[0xb64], succ=[0xb82, 0xbd7]
    =================================
    0xb7c: vb7c = MLOAD vb6b
    0xb7d: vb7d = ISZERO vb7c
    0xb7e: vb7e(0xbd7) = CONST 
    0xb81: JUMPI vb7e(0xbd7), vb7d

    Begin block 0xb82
    prev=[0xb7a], succ=[0xbd7]
    =================================
    0xb82: vb82(0x2) = CONST 
    0xb84: vb84 = SLOAD vb82(0x2)
    0xb85: vb85(0x40) = CONST 
    0xb88: vb88 = MLOAD vb85(0x40)
    0xb89: vb89(0x1) = CONST 
    0xb8b: vb8b(0xa0) = CONST 
    0xb8d: vb8d(0x2) = CONST 
    0xb8f: vb8f(0x10000000000000000000000000000000000000000) = EXP vb8d(0x2), vb8b(0xa0)
    0xb90: vb90(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb8f(0x10000000000000000000000000000000000000000), vb89(0x1)
    0xb93: vb93 = AND v300, vb90(0xffffffffffffffffffffffffffffffffffffffff)
    0xb95: MSTORE vb88, vb93
    0xb98: vb98 = AND va48, vb90(0xffffffffffffffffffffffffffffffffffffffff)
    0xb99: vb99(0x20) = CONST 
    0xb9c: vb9c = ADD vb88, vb99(0x20)
    0xb9d: MSTORE vb9c, vb98
    0xba0: vba0 = AND vb84, vb90(0xffffffffffffffffffffffffffffffffffffffff)
    0xba3: vba3 = ADD vb85(0x40), vb88
    0xba4: MSTORE vba3, vba0
    0xba5: vba5(0x60) = CONST 
    0xba8: vba8 = ADD vb88, vba5(0x60)
    0xbab: MSTORE vba8, vad6
    0xbac: vbac = MLOAD vb85(0x40)
    0xbad: vbad(0x9ca7c1e047552a8048d924a5a8d3c150eb861086a72a9100e5f19d1176c1b746) = CONST 
    0xbd1: vbd1(0x0) = SUB vb88, vbac
    0xbd2: vbd2(0x80) = CONST 
    0xbd4: vbd4(0x80) = ADD vbd2(0x80), vbd1(0x0)
    0xbd6: LOG1 vbac, vbd4(0x80), vbad(0x9ca7c1e047552a8048d924a5a8d3c150eb861086a72a9100e5f19d1176c1b746)

    Begin block 0xbd7
    prev=[0xb82, 0xb7a], succ=[0xa27]
    =================================
    0xbd7_0x0: vbd7_0 = PHI va25(0x0), vbda
    0xbd8: vbd8(0x1) = CONST 
    0xbda: vbda = ADD vbd8(0x1), vbd7_0
    0xbdb: vbdb(0xa27) = CONST 
    0xbde: JUMP vbdb(0xa27)

}

function owner()() public {
    Begin block 0x329
    prev=[], succ=[0x331, 0x335]
    =================================
    0x32a: v32a = CALLVALUE 
    0x32c: v32c = ISZERO v32a
    0x32d: v32d(0x335) = CONST 
    0x330: JUMPI v32d(0x335), v32c

    Begin block 0x331
    prev=[0x329], succ=[]
    =================================
    0x331: v331(0x0) = CONST 
    0x334: REVERT v331(0x0), v331(0x0)

    Begin block 0x335
    prev=[0x329], succ=[0xc80]
    =================================
    0x337: v337(0x162c) = CONST 
    0x33a: v33a(0xc80) = CONST 
    0x33d: JUMP v33a(0xc80)

    Begin block 0xc80
    prev=[0x335], succ=[0x162c]
    =================================
    0xc81: vc81(0x5) = CONST 
    0xc83: vc83 = SLOAD vc81(0x5)
    0xc84: vc84(0x1) = CONST 
    0xc86: vc86(0xa0) = CONST 
    0xc88: vc88(0x2) = CONST 
    0xc8a: vc8a(0x10000000000000000000000000000000000000000) = EXP vc88(0x2), vc86(0xa0)
    0xc8b: vc8b(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc8a(0x10000000000000000000000000000000000000000), vc84(0x1)
    0xc8c: vc8c = AND vc8b(0xffffffffffffffffffffffffffffffffffffffff), vc83
    0xc8e: JUMP v337(0x162c)

    Begin block 0x162c
    prev=[0xc80], succ=[]
    =================================
    0x162d: v162d(0x40) = CONST 
    0x1630: v1630 = MLOAD v162d(0x40)
    0x1631: v1631(0x1) = CONST 
    0x1633: v1633(0xa0) = CONST 
    0x1635: v1635(0x2) = CONST 
    0x1637: v1637(0x10000000000000000000000000000000000000000) = EXP v1635(0x2), v1633(0xa0)
    0x1638: v1638(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1637(0x10000000000000000000000000000000000000000), v1631(0x1)
    0x163b: v163b = AND vc8c, v1638(0xffffffffffffffffffffffffffffffffffffffff)
    0x163d: MSTORE v1630, v163b
    0x163e: v163e = MLOAD v162d(0x40)
    0x1642: v1642(0x0) = SUB v1630, v163e
    0x1643: v1643(0x20) = CONST 
    0x1645: v1645(0x20) = ADD v1643(0x20), v1642(0x0)
    0x1647: RETURN v163e, v1645(0x20)

}

function withdrawERC20(address,address)() public {
    Begin block 0x33e
    prev=[], succ=[0x346, 0x34a]
    =================================
    0x33f: v33f = CALLVALUE 
    0x341: v341 = ISZERO v33f
    0x342: v342(0x34a) = CONST 
    0x345: JUMPI v342(0x34a), v341

    Begin block 0x346
    prev=[0x33e], succ=[]
    =================================
    0x346: v346(0x0) = CONST 
    0x349: REVERT v346(0x0), v346(0x0)

    Begin block 0x34a
    prev=[0x33e], succ=[0xc8fB0x34a]
    =================================
    0x34c: v34c(0x1667) = CONST 
    0x34f: v34f(0x1) = CONST 
    0x351: v351(0xa0) = CONST 
    0x353: v353(0x2) = CONST 
    0x355: v355(0x10000000000000000000000000000000000000000) = EXP v353(0x2), v351(0xa0)
    0x356: v356(0xffffffffffffffffffffffffffffffffffffffff) = SUB v355(0x10000000000000000000000000000000000000000), v34f(0x1)
    0x357: v357(0x4) = CONST 
    0x359: v359 = CALLDATALOAD v357(0x4)
    0x35b: v35b = AND v356(0xffffffffffffffffffffffffffffffffffffffff), v359
    0x35d: v35d(0x24) = CONST 
    0x35f: v35f = CALLDATALOAD v35d(0x24)
    0x360: v360 = AND v35f, v356(0xffffffffffffffffffffffffffffffffffffffff)
    0x361: v361(0xc8f) = CONST 
    0x364: JUMP v361(0xc8f)

    Begin block 0xc8fB0x34a
    prev=[0x34a], succ=[0xee6B0xc8fB0x34a]
    =================================
    0xc90S0x34a: vc90V34a(0x0) = CONST 
    0xc93S0x34a: vc93V34a(0xc9b) = CONST 
    0xc96S0x34a: vc96V34a = CALLER 
    0xc97S0x34a: vc97V34a(0xee6) = CONST 
    0xc9aS0x34a: JUMP vc97V34a(0xee6)

    Begin block 0xee6B0xc8fB0x34a
    prev=[0xc8fB0x34a], succ=[0xc9bB0x34a]
    =================================
    0xee7S0xc8fS0x34a: vee7Vc8fV34a(0x1) = CONST 
    0xee9S0xc8fS0x34a: vee9Vc8fV34a(0xa0) = CONST 
    0xeebS0xc8fS0x34a: veebVc8fV34a(0x2) = CONST 
    0xeedS0xc8fS0x34a: veedVc8fV34a(0x10000000000000000000000000000000000000000) = EXP veebVc8fV34a(0x2), vee9Vc8fV34a(0xa0)
    0xeeeS0xc8fS0x34a: veeeVc8fV34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedVc8fV34a(0x10000000000000000000000000000000000000000), vee7Vc8fV34a(0x1)
    0xeefS0xc8fS0x34a: veefVc8fV34a = AND veeeVc8fV34a(0xffffffffffffffffffffffffffffffffffffffff), vc96V34a
    0xef0S0xc8fS0x34a: vef0Vc8fV34a(0x0) = CONST 
    0xef4S0xc8fS0x34a: MSTORE vef0Vc8fV34a(0x0), veefVc8fV34a
    0xef5S0xc8fS0x34a: vef5Vc8fV34a(0x6) = CONST 
    0xef7S0xc8fS0x34a: vef7Vc8fV34a(0x20) = CONST 
    0xef9S0xc8fS0x34a: MSTORE vef7Vc8fV34a(0x20), vef5Vc8fV34a(0x6)
    0xefaS0xc8fS0x34a: vefaVc8fV34a(0x40) = CONST 
    0xefdS0xc8fS0x34a: vefdVc8fV34a = SHA3 vef0Vc8fV34a(0x0), vefaVc8fV34a(0x40)
    0xefeS0xc8fS0x34a: vefeVc8fV34a = SLOAD vefdVc8fV34a
    0xeffS0xc8fS0x34a: veffVc8fV34a = ISZERO vefeVc8fV34a
    0xf00S0xc8fS0x34a: vf00Vc8fV34a = ISZERO veffVc8fV34a
    0xf02S0xc8fS0x34a: JUMP vc93V34a(0xc9b)

    Begin block 0xc9bB0x34a
    prev=[0xee6B0xc8fB0x34a], succ=[0xca2B0x34a, 0xca6B0x34a]
    =================================
    0xc9cS0x34a: vc9cV34a = ISZERO vf00Vc8fV34a
    0xc9dS0x34a: vc9dV34a = ISZERO vc9cV34a
    0xc9eS0x34a: vc9eV34a(0xca6) = CONST 
    0xca1S0x34a: JUMPI vc9eV34a(0xca6), vc9dV34a

    Begin block 0xca2B0x34a
    prev=[0xc9bB0x34a], succ=[]
    =================================
    0xca2S0x34a: vca2V34a(0x0) = CONST 
    0xca5S0x34a: REVERT vca2V34a(0x0), vca2V34a(0x0)

    Begin block 0xca6B0x34a
    prev=[0xc9bB0x34a], succ=[0xd16B0x34a, 0xd1aB0x34a]
    =================================
    0xca8S0x34a: vca8V34a(0x1) = CONST 
    0xcaaS0x34a: vcaaV34a(0xa0) = CONST 
    0xcacS0x34a: vcacV34a(0x2) = CONST 
    0xcaeS0x34a: vcaeV34a(0x10000000000000000000000000000000000000000) = EXP vcacV34a(0x2), vcaaV34a(0xa0)
    0xcafS0x34a: vcafV34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcaeV34a(0x10000000000000000000000000000000000000000), vca8V34a(0x1)
    0xcb0S0x34a: vcb0V34a = AND vcafV34a(0xffffffffffffffffffffffffffffffffffffffff), v35b
    0xcb1S0x34a: vcb1V34a(0x70a08231) = CONST 
    0xcb7S0x34a: vcb7V34a(0x40) = CONST 
    0xcb9S0x34a: vcb9V34a = MLOAD vcb7V34a(0x40)
    0xcbbS0x34a: vcbbV34a(0xffffffff) = CONST 
    0xcc0S0x34a: vcc0V34a(0x70a08231) = AND vcbbV34a(0xffffffff), vcb1V34a(0x70a08231)
    0xcc1S0x34a: vcc1V34a(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0xcdfS0x34a: vcdfV34a(0x70a0823100000000000000000000000000000000000000000000000000000000) = MUL vcc1V34a(0x100000000000000000000000000000000000000000000000000000000), vcc0V34a(0x70a08231)
    0xce1S0x34a: MSTORE vcb9V34a, vcdfV34a(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0xce2S0x34a: vce2V34a(0x4) = CONST 
    0xce4S0x34a: vce4V34a = ADD vce2V34a(0x4), vcb9V34a
    0xce7S0x34a: vce7V34a(0x1) = CONST 
    0xce9S0x34a: vce9V34a(0xa0) = CONST 
    0xcebS0x34a: vcebV34a(0x2) = CONST 
    0xcedS0x34a: vcedV34a(0x10000000000000000000000000000000000000000) = EXP vcebV34a(0x2), vce9V34a(0xa0)
    0xceeS0x34a: vceeV34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcedV34a(0x10000000000000000000000000000000000000000), vce7V34a(0x1)
    0xcefS0x34a: vcefV34a = AND vceeV34a(0xffffffffffffffffffffffffffffffffffffffff), v360
    0xcf0S0x34a: vcf0V34a(0x1) = CONST 
    0xcf2S0x34a: vcf2V34a(0xa0) = CONST 
    0xcf4S0x34a: vcf4V34a(0x2) = CONST 
    0xcf6S0x34a: vcf6V34a(0x10000000000000000000000000000000000000000) = EXP vcf4V34a(0x2), vcf2V34a(0xa0)
    0xcf7S0x34a: vcf7V34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcf6V34a(0x10000000000000000000000000000000000000000), vcf0V34a(0x1)
    0xcf8S0x34a: vcf8V34a = AND vcf7V34a(0xffffffffffffffffffffffffffffffffffffffff), vcefV34a
    0xcfaS0x34a: MSTORE vce4V34a, vcf8V34a
    0xcfbS0x34a: vcfbV34a(0x20) = CONST 
    0xcfdS0x34a: vcfdV34a = ADD vcfbV34a(0x20), vce4V34a
    0xd01S0x34a: vd01V34a(0x20) = CONST 
    0xd03S0x34a: vd03V34a(0x40) = CONST 
    0xd05S0x34a: vd05V34a = MLOAD vd03V34a(0x40)
    0xd08S0x34a: vd08V34a(0x24) = SUB vcfdV34a, vd05V34a
    0xd0aS0x34a: vd0aV34a(0x0) = CONST 
    0xd0eS0x34a: vd0eV34a = EXTCODESIZE vcb0V34a
    0xd0fS0x34a: vd0fV34a = ISZERO vd0eV34a
    0xd11S0x34a: vd11V34a = ISZERO vd0fV34a
    0xd12S0x34a: vd12V34a(0xd1a) = CONST 
    0xd15S0x34a: JUMPI vd12V34a(0xd1a), vd11V34a

    Begin block 0xd16B0x34a
    prev=[0xca6B0x34a], succ=[]
    =================================
    0xd16S0x34a: vd16V34a(0x0) = CONST 
    0xd19S0x34a: REVERT vd16V34a(0x0), vd16V34a(0x0)

    Begin block 0xd1aB0x34a
    prev=[0xca6B0x34a], succ=[0xd25B0x34a, 0xd2eB0x34a]
    =================================
    0xd1cS0x34a: vd1cV34a = GAS 
    0xd1dS0x34a: vd1dV34a = CALL vd1cV34a, vcb0V34a, vd0aV34a(0x0), vd05V34a, vd08V34a(0x24), vd05V34a, vd01V34a(0x20)
    0xd1eS0x34a: vd1eV34a = ISZERO vd1dV34a
    0xd20S0x34a: vd20V34a = ISZERO vd1eV34a
    0xd21S0x34a: vd21V34a(0xd2e) = CONST 
    0xd24S0x34a: JUMPI vd21V34a(0xd2e), vd20V34a

    Begin block 0xd25B0x34a
    prev=[0xd1aB0x34a], succ=[]
    =================================
    0xd25S0x34a: vd25V34a = RETURNDATASIZE 
    0xd26S0x34a: vd26V34a(0x0) = CONST 
    0xd29S0x34a: RETURNDATACOPY vd26V34a(0x0), vd26V34a(0x0), vd25V34a
    0xd2aS0x34a: vd2aV34a = RETURNDATASIZE 
    0xd2bS0x34a: vd2bV34a(0x0) = CONST 
    0xd2dS0x34a: REVERT vd2bV34a(0x0), vd2aV34a

    Begin block 0xd2eB0x34a
    prev=[0xd1aB0x34a], succ=[0xd40B0x34a, 0xd44B0x34a]
    =================================
    0xd33S0x34a: vd33V34a(0x40) = CONST 
    0xd35S0x34a: vd35V34a = MLOAD vd33V34a(0x40)
    0xd36S0x34a: vd36V34a = RETURNDATASIZE 
    0xd37S0x34a: vd37V34a(0x20) = CONST 
    0xd3aS0x34a: vd3aV34a = LT vd36V34a, vd37V34a(0x20)
    0xd3bS0x34a: vd3bV34a = ISZERO vd3aV34a
    0xd3cS0x34a: vd3cV34a(0xd44) = CONST 
    0xd3fS0x34a: JUMPI vd3cV34a(0xd44), vd3bV34a

    Begin block 0xd40B0x34a
    prev=[0xd2eB0x34a], succ=[]
    =================================
    0xd40S0x34a: vd40V34a(0x0) = CONST 
    0xd43S0x34a: REVERT vd40V34a(0x0), vd40V34a(0x0)

    Begin block 0xd44B0x34a
    prev=[0xd2eB0x34a], succ=[0xdbcB0x34a, 0xdc0B0x34a]
    =================================
    0xd46S0x34a: vd46V34a = MLOAD vd35V34a
    0xd47S0x34a: vd47V34a(0x2) = CONST 
    0xd49S0x34a: vd49V34a = SLOAD vd47V34a(0x2)
    0xd4aS0x34a: vd4aV34a(0x40) = CONST 
    0xd4dS0x34a: vd4dV34a = MLOAD vd4aV34a(0x40)
    0xd4eS0x34a: vd4eV34a(0x92940bf900000000000000000000000000000000000000000000000000000000) = CONST 
    0xd70S0x34a: MSTORE vd4dV34a, vd4eV34a(0x92940bf900000000000000000000000000000000000000000000000000000000)
    0xd71S0x34a: vd71V34a(0x1) = CONST 
    0xd73S0x34a: vd73V34a(0xa0) = CONST 
    0xd75S0x34a: vd75V34a(0x2) = CONST 
    0xd77S0x34a: vd77V34a(0x10000000000000000000000000000000000000000) = EXP vd75V34a(0x2), vd73V34a(0xa0)
    0xd78S0x34a: vd78V34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd77V34a(0x10000000000000000000000000000000000000000), vd71V34a(0x1)
    0xd7bS0x34a: vd7bV34a = AND vd78V34a(0xffffffffffffffffffffffffffffffffffffffff), v35b
    0xd7cS0x34a: vd7cV34a(0x4) = CONST 
    0xd7fS0x34a: vd7fV34a = ADD vd4dV34a, vd7cV34a(0x4)
    0xd80S0x34a: MSTORE vd7fV34a, vd7bV34a
    0xd83S0x34a: vd83V34a = AND vd78V34a(0xffffffffffffffffffffffffffffffffffffffff), vd49V34a
    0xd84S0x34a: vd84V34a(0x24) = CONST 
    0xd87S0x34a: vd87V34a = ADD vd4dV34a, vd84V34a(0x24)
    0xd88S0x34a: MSTORE vd87V34a, vd83V34a
    0xd89S0x34a: vd89V34a(0x44) = CONST 
    0xd8cS0x34a: vd8cV34a = ADD vd4dV34a, vd89V34a(0x44)
    0xd8fS0x34a: MSTORE vd8cV34a, vd46V34a
    0xd91S0x34a: vd91V34a = MLOAD vd4aV34a(0x40)
    0xd97S0x34a: vd97V34a = AND v360, vd78V34a(0xffffffffffffffffffffffffffffffffffffffff)
    0xd99S0x34a: vd99V34a(0x92940bf9) = CONST 
    0xd9fS0x34a: vd9fV34a(0x64) = CONST 
    0xda3S0x34a: vda3V34a = ADD vd4dV34a, vd9fV34a(0x64)
    0xda5S0x34a: vda5V34a(0x20) = CONST 
    0xdadS0x34a: vdadV34a(0x0) = SUB vd4dV34a, vd91V34a
    0xdaeS0x34a: vdaeV34a(0x64) = ADD vdadV34a(0x0), vd9fV34a(0x64)
    0xdb0S0x34a: vdb0V34a(0x0) = CONST 
    0xdb4S0x34a: vdb4V34a = EXTCODESIZE vd97V34a
    0xdb5S0x34a: vdb5V34a = ISZERO vdb4V34a
    0xdb7S0x34a: vdb7V34a = ISZERO vdb5V34a
    0xdb8S0x34a: vdb8V34a(0xdc0) = CONST 
    0xdbbS0x34a: JUMPI vdb8V34a(0xdc0), vdb7V34a

    Begin block 0xdbcB0x34a
    prev=[0xd44B0x34a], succ=[]
    =================================
    0xdbcS0x34a: vdbcV34a(0x0) = CONST 
    0xdbfS0x34a: REVERT vdbcV34a(0x0), vdbcV34a(0x0)

    Begin block 0xdc0B0x34a
    prev=[0xd44B0x34a], succ=[0xdcbB0x34a, 0xdd4B0x34a]
    =================================
    0xdc2S0x34a: vdc2V34a = GAS 
    0xdc3S0x34a: vdc3V34a = CALL vdc2V34a, vd97V34a, vdb0V34a(0x0), vd91V34a, vdaeV34a(0x64), vd91V34a, vda5V34a(0x20)
    0xdc4S0x34a: vdc4V34a = ISZERO vdc3V34a
    0xdc6S0x34a: vdc6V34a = ISZERO vdc4V34a
    0xdc7S0x34a: vdc7V34a(0xdd4) = CONST 
    0xdcaS0x34a: JUMPI vdc7V34a(0xdd4), vdc6V34a

    Begin block 0xdcbB0x34a
    prev=[0xdc0B0x34a], succ=[]
    =================================
    0xdcbS0x34a: vdcbV34a = RETURNDATASIZE 
    0xdccS0x34a: vdccV34a(0x0) = CONST 
    0xdcfS0x34a: RETURNDATACOPY vdccV34a(0x0), vdccV34a(0x0), vdcbV34a
    0xdd0S0x34a: vdd0V34a = RETURNDATASIZE 
    0xdd1S0x34a: vdd1V34a(0x0) = CONST 
    0xdd3S0x34a: REVERT vdd1V34a(0x0), vdd0V34a

    Begin block 0xdd4B0x34a
    prev=[0xdc0B0x34a], succ=[0xde6B0x34a, 0xdeaB0x34a]
    =================================
    0xdd9S0x34a: vdd9V34a(0x40) = CONST 
    0xddbS0x34a: vddbV34a = MLOAD vdd9V34a(0x40)
    0xddcS0x34a: vddcV34a = RETURNDATASIZE 
    0xdddS0x34a: vdddV34a(0x20) = CONST 
    0xde0S0x34a: vde0V34a = LT vddcV34a, vdddV34a(0x20)
    0xde1S0x34a: vde1V34a = ISZERO vde0V34a
    0xde2S0x34a: vde2V34a(0xdea) = CONST 
    0xde5S0x34a: JUMPI vde2V34a(0xdea), vde1V34a

    Begin block 0xde6B0x34a
    prev=[0xdd4B0x34a], succ=[]
    =================================
    0xde6S0x34a: vde6V34a(0x0) = CONST 
    0xde9S0x34a: REVERT vde6V34a(0x0), vde6V34a(0x0)

    Begin block 0xdeaB0x34a
    prev=[0xdd4B0x34a], succ=[0xdf5B0x34a, 0xe4aB0x34a]
    =================================
    0xdecS0x34a: vdecV34a = MLOAD vddbV34a
    0xdf0S0x34a: vdf0V34a = ISZERO vdecV34a
    0xdf1S0x34a: vdf1V34a(0xe4a) = CONST 
    0xdf4S0x34a: JUMPI vdf1V34a(0xe4a), vdf0V34a

    Begin block 0xdf5B0x34a
    prev=[0xdeaB0x34a], succ=[0xe4aB0x34a]
    =================================
    0xdf5S0x34a: vdf5V34a(0x2) = CONST 
    0xdf7S0x34a: vdf7V34a = SLOAD vdf5V34a(0x2)
    0xdf8S0x34a: vdf8V34a(0x40) = CONST 
    0xdfbS0x34a: vdfbV34a = MLOAD vdf8V34a(0x40)
    0xdfcS0x34a: vdfcV34a(0x1) = CONST 
    0xdfeS0x34a: vdfeV34a(0xa0) = CONST 
    0xe00S0x34a: ve00V34a(0x2) = CONST 
    0xe02S0x34a: ve02V34a(0x10000000000000000000000000000000000000000) = EXP ve00V34a(0x2), vdfeV34a(0xa0)
    0xe03S0x34a: ve03V34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve02V34a(0x10000000000000000000000000000000000000000), vdfcV34a(0x1)
    0xe06S0x34a: ve06V34a = AND v35b, ve03V34a(0xffffffffffffffffffffffffffffffffffffffff)
    0xe08S0x34a: MSTORE vdfbV34a, ve06V34a
    0xe0bS0x34a: ve0bV34a = AND v360, ve03V34a(0xffffffffffffffffffffffffffffffffffffffff)
    0xe0cS0x34a: ve0cV34a(0x20) = CONST 
    0xe0fS0x34a: ve0fV34a = ADD vdfbV34a, ve0cV34a(0x20)
    0xe10S0x34a: MSTORE ve0fV34a, ve0bV34a
    0xe13S0x34a: ve13V34a = AND vdf7V34a, ve03V34a(0xffffffffffffffffffffffffffffffffffffffff)
    0xe16S0x34a: ve16V34a = ADD vdf8V34a(0x40), vdfbV34a
    0xe17S0x34a: MSTORE ve16V34a, ve13V34a
    0xe18S0x34a: ve18V34a(0x60) = CONST 
    0xe1bS0x34a: ve1bV34a = ADD vdfbV34a, ve18V34a(0x60)
    0xe1eS0x34a: MSTORE ve1bV34a, vd46V34a
    0xe1fS0x34a: ve1fV34a = MLOAD vdf8V34a(0x40)
    0xe20S0x34a: ve20V34a(0x9ca7c1e047552a8048d924a5a8d3c150eb861086a72a9100e5f19d1176c1b746) = CONST 
    0xe44S0x34a: ve44V34a(0x0) = SUB vdfbV34a, ve1fV34a
    0xe45S0x34a: ve45V34a(0x80) = CONST 
    0xe47S0x34a: ve47V34a(0x80) = ADD ve45V34a(0x80), ve44V34a(0x0)
    0xe49S0x34a: LOG1 ve1fV34a, ve47V34a(0x80), ve20V34a(0x9ca7c1e047552a8048d924a5a8d3c150eb861086a72a9100e5f19d1176c1b746)

    Begin block 0xe4aB0x34a
    prev=[0xdf5B0x34a, 0xdeaB0x34a], succ=[0xeaeB0x34a, 0xeb2B0x34a]
    =================================
    0xe4bS0x34a: ve4bV34a(0x2) = CONST 
    0xe4dS0x34a: ve4dV34a = SLOAD ve4bV34a(0x2)
    0xe4eS0x34a: ve4eV34a(0x40) = CONST 
    0xe51S0x34a: ve51V34a = MLOAD ve4eV34a(0x40)
    0xe52S0x34a: ve52V34a(0xc69e546d00000000000000000000000000000000000000000000000000000000) = CONST 
    0xe74S0x34a: MSTORE ve51V34a, ve52V34a(0xc69e546d00000000000000000000000000000000000000000000000000000000)
    0xe75S0x34a: ve75V34a(0x1) = CONST 
    0xe77S0x34a: ve77V34a(0xa0) = CONST 
    0xe79S0x34a: ve79V34a(0x2) = CONST 
    0xe7bS0x34a: ve7bV34a(0x10000000000000000000000000000000000000000) = EXP ve79V34a(0x2), ve77V34a(0xa0)
    0xe7cS0x34a: ve7cV34a(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve7bV34a(0x10000000000000000000000000000000000000000), ve75V34a(0x1)
    0xe7fS0x34a: ve7fV34a = AND ve7cV34a(0xffffffffffffffffffffffffffffffffffffffff), v35b
    0xe80S0x34a: ve80V34a(0x4) = CONST 
    0xe83S0x34a: ve83V34a = ADD ve51V34a, ve80V34a(0x4)
    0xe84S0x34a: MSTORE ve83V34a, ve7fV34a
    0xe86S0x34a: ve86V34a = MLOAD ve4eV34a(0x40)
    0xe8aS0x34a: ve8aV34a = AND ve4dV34a, ve7cV34a(0xffffffffffffffffffffffffffffffffffffffff)
    0xe8cS0x34a: ve8cV34a(0xc69e546d) = CONST 
    0xe92S0x34a: ve92V34a(0x24) = CONST 
    0xe96S0x34a: ve96V34a = ADD ve51V34a, ve92V34a(0x24)
    0xe98S0x34a: ve98V34a(0x20) = CONST 
    0xe9fS0x34a: ve9fV34a(0x0) = SUB ve51V34a, ve86V34a
    0xea0S0x34a: vea0V34a(0x24) = ADD ve9fV34a(0x0), ve92V34a(0x24)
    0xea2S0x34a: vea2V34a(0x0) = CONST 
    0xea6S0x34a: vea6V34a = EXTCODESIZE ve8aV34a
    0xea7S0x34a: vea7V34a = ISZERO vea6V34a
    0xea9S0x34a: vea9V34a = ISZERO vea7V34a
    0xeaaS0x34a: veaaV34a(0xeb2) = CONST 
    0xeadS0x34a: JUMPI veaaV34a(0xeb2), vea9V34a

    Begin block 0xeaeB0x34a
    prev=[0xe4aB0x34a], succ=[]
    =================================
    0xeaeS0x34a: veaeV34a(0x0) = CONST 
    0xeb1S0x34a: REVERT veaeV34a(0x0), veaeV34a(0x0)

    Begin block 0xeb2B0x34a
    prev=[0xe4aB0x34a], succ=[0xebdB0x34a, 0xec6B0x34a]
    =================================
    0xeb4S0x34a: veb4V34a = GAS 
    0xeb5S0x34a: veb5V34a = CALL veb4V34a, ve8aV34a, vea2V34a(0x0), ve86V34a, vea0V34a(0x24), ve86V34a, ve98V34a(0x20)
    0xeb6S0x34a: veb6V34a = ISZERO veb5V34a
    0xeb8S0x34a: veb8V34a = ISZERO veb6V34a
    0xeb9S0x34a: veb9V34a(0xec6) = CONST 
    0xebcS0x34a: JUMPI veb9V34a(0xec6), veb8V34a

    Begin block 0xebdB0x34a
    prev=[0xeb2B0x34a], succ=[]
    =================================
    0xebdS0x34a: vebdV34a = RETURNDATASIZE 
    0xebeS0x34a: vebeV34a(0x0) = CONST 
    0xec1S0x34a: RETURNDATACOPY vebeV34a(0x0), vebeV34a(0x0), vebdV34a
    0xec2S0x34a: vec2V34a = RETURNDATASIZE 
    0xec3S0x34a: vec3V34a(0x0) = CONST 
    0xec5S0x34a: REVERT vec3V34a(0x0), vec2V34a

    Begin block 0xec6B0x34a
    prev=[0xeb2B0x34a], succ=[0xed8B0x34a, 0xedcB0x34a]
    =================================
    0xecbS0x34a: vecbV34a(0x40) = CONST 
    0xecdS0x34a: vecdV34a = MLOAD vecbV34a(0x40)
    0xeceS0x34a: veceV34a = RETURNDATASIZE 
    0xecfS0x34a: vecfV34a(0x20) = CONST 
    0xed2S0x34a: ved2V34a = LT veceV34a, vecfV34a(0x20)
    0xed3S0x34a: ved3V34a = ISZERO ved2V34a
    0xed4S0x34a: ved4V34a(0xedc) = CONST 
    0xed7S0x34a: JUMPI ved4V34a(0xedc), ved3V34a

    Begin block 0xed8B0x34a
    prev=[0xec6B0x34a], succ=[]
    =================================
    0xed8S0x34a: ved8V34a(0x0) = CONST 
    0xedbS0x34a: REVERT ved8V34a(0x0), ved8V34a(0x0)

    Begin block 0xedcB0x34a
    prev=[0xec6B0x34a], succ=[0x1667]
    =================================
    0xee5S0x34a: JUMP v34c(0x1667)

    Begin block 0x1667
    prev=[0xedcB0x34a], succ=[]
    =================================
    0x1668: v1668(0x40) = CONST 
    0x166b: v166b = MLOAD v1668(0x40)
    0x166d: v166d = ISZERO vdecV34a
    0x166e: v166e = ISZERO v166d
    0x1670: MSTORE v166b, v166e
    0x1671: v1671 = MLOAD v1668(0x40)
    0x1675: v1675(0x0) = SUB v166b, v1671
    0x1676: v1676(0x20) = CONST 
    0x1678: v1678(0x20) = ADD v1676(0x20), v1675(0x0)
    0x167a: RETURN v1671, v1678(0x20)

}

function isWorker(address)() public {
    Begin block 0x365
    prev=[], succ=[0x36d, 0x371]
    =================================
    0x366: v366 = CALLVALUE 
    0x368: v368 = ISZERO v366
    0x369: v369(0x371) = CONST 
    0x36c: JUMPI v369(0x371), v368

    Begin block 0x36d
    prev=[0x365], succ=[]
    =================================
    0x36d: v36d(0x0) = CONST 
    0x370: REVERT v36d(0x0), v36d(0x0)

    Begin block 0x371
    prev=[0x365], succ=[0xee6B0x371]
    =================================
    0x373: v373(0x169a) = CONST 
    0x376: v376(0x1) = CONST 
    0x378: v378(0xa0) = CONST 
    0x37a: v37a(0x2) = CONST 
    0x37c: v37c(0x10000000000000000000000000000000000000000) = EXP v37a(0x2), v378(0xa0)
    0x37d: v37d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37c(0x10000000000000000000000000000000000000000), v376(0x1)
    0x37e: v37e(0x4) = CONST 
    0x380: v380 = CALLDATALOAD v37e(0x4)
    0x381: v381 = AND v380, v37d(0xffffffffffffffffffffffffffffffffffffffff)
    0x382: v382(0xee6) = CONST 
    0x385: JUMP v382(0xee6)

    Begin block 0xee6B0x371
    prev=[0x371], succ=[0x169a]
    =================================
    0xee7S0x371: vee7V371(0x1) = CONST 
    0xee9S0x371: vee9V371(0xa0) = CONST 
    0xeebS0x371: veebV371(0x2) = CONST 
    0xeedS0x371: veedV371(0x10000000000000000000000000000000000000000) = EXP veebV371(0x2), vee9V371(0xa0)
    0xeeeS0x371: veeeV371(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedV371(0x10000000000000000000000000000000000000000), vee7V371(0x1)
    0xeefS0x371: veefV371 = AND veeeV371(0xffffffffffffffffffffffffffffffffffffffff), v381
    0xef0S0x371: vef0V371(0x0) = CONST 
    0xef4S0x371: MSTORE vef0V371(0x0), veefV371
    0xef5S0x371: vef5V371(0x6) = CONST 
    0xef7S0x371: vef7V371(0x20) = CONST 
    0xef9S0x371: MSTORE vef7V371(0x20), vef5V371(0x6)
    0xefaS0x371: vefaV371(0x40) = CONST 
    0xefdS0x371: vefdV371 = SHA3 vef0V371(0x0), vefaV371(0x40)
    0xefeS0x371: vefeV371 = SLOAD vefdV371
    0xeffS0x371: veffV371 = ISZERO vefeV371
    0xf00S0x371: vf00V371 = ISZERO veffV371
    0xf02S0x371: JUMP v373(0x169a)

    Begin block 0x169a
    prev=[0xee6B0x371], succ=[]
    =================================
    0x169b: v169b(0x40) = CONST 
    0x169e: v169e = MLOAD v169b(0x40)
    0x16a0: v16a0 = ISZERO vf00V371
    0x16a1: v16a1 = ISZERO v16a0
    0x16a3: MSTORE v169e, v16a1
    0x16a4: v16a4 = MLOAD v169b(0x40)
    0x16a8: v16a8(0x0) = SUB v169e, v16a4
    0x16a9: v16a9(0x20) = CONST 
    0x16ab: v16ab(0x20) = ADD v16a9(0x20), v16a8(0x0)
    0x16ad: RETURN v16a4, v16ab(0x20)

}

function removeWorker(address)() public {
    Begin block 0x386
    prev=[], succ=[0x38e, 0x392]
    =================================
    0x387: v387 = CALLVALUE 
    0x389: v389 = ISZERO v387
    0x38a: v38a(0x392) = CONST 
    0x38d: JUMPI v38a(0x392), v389

    Begin block 0x38e
    prev=[0x386], succ=[]
    =================================
    0x38e: v38e(0x0) = CONST 
    0x391: REVERT v38e(0x0), v38e(0x0)

    Begin block 0x392
    prev=[0x386], succ=[0xf03]
    =================================
    0x394: v394(0x16cd) = CONST 
    0x397: v397(0x1) = CONST 
    0x399: v399(0xa0) = CONST 
    0x39b: v39b(0x2) = CONST 
    0x39d: v39d(0x10000000000000000000000000000000000000000) = EXP v39b(0x2), v399(0xa0)
    0x39e: v39e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39d(0x10000000000000000000000000000000000000000), v397(0x1)
    0x39f: v39f(0x4) = CONST 
    0x3a1: v3a1 = CALLDATALOAD v39f(0x4)
    0x3a2: v3a2 = AND v3a1, v39e(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a3: v3a3(0xf03) = CONST 
    0x3a6: JUMP v3a3(0xf03)

    Begin block 0xf03
    prev=[0x392], succ=[0xf21, 0xf25]
    =================================
    0xf04: vf04(0x5) = CONST 
    0xf06: vf06 = SLOAD vf04(0x5)
    0xf07: vf07(0x0) = CONST 
    0xf0e: vf0e = CALLER 
    0xf0f: vf0f(0x1) = CONST 
    0xf11: vf11(0xa0) = CONST 
    0xf13: vf13(0x2) = CONST 
    0xf15: vf15(0x10000000000000000000000000000000000000000) = EXP vf13(0x2), vf11(0xa0)
    0xf16: vf16(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf15(0x10000000000000000000000000000000000000000), vf0f(0x1)
    0xf19: vf19 = AND vf16(0xffffffffffffffffffffffffffffffffffffffff), vf0e
    0xf1b: vf1b = AND vf06, vf16(0xffffffffffffffffffffffffffffffffffffffff)
    0xf1c: vf1c = EQ vf1b, vf19
    0xf1d: vf1d(0xf25) = CONST 
    0xf20: JUMPI vf1d(0xf25), vf1c

    Begin block 0xf21
    prev=[0xf03], succ=[]
    =================================
    0xf21: vf21(0x0) = CONST 
    0xf24: REVERT vf21(0x0), vf21(0x0)

    Begin block 0xf25
    prev=[0xf03], succ=[0xee6B0xf25]
    =================================
    0xf26: vf26(0xf2e) = CONST 
    0xf2a: vf2a(0xee6) = CONST 
    0xf2d: JUMP vf2a(0xee6)

    Begin block 0xee6B0xf25
    prev=[0xf25], succ=[0xf2e]
    =================================
    0xee7S0xf25: vee7Vf25(0x1) = CONST 
    0xee9S0xf25: vee9Vf25(0xa0) = CONST 
    0xeebS0xf25: veebVf25(0x2) = CONST 
    0xeedS0xf25: veedVf25(0x10000000000000000000000000000000000000000) = EXP veebVf25(0x2), vee9Vf25(0xa0)
    0xeeeS0xf25: veeeVf25(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedVf25(0x10000000000000000000000000000000000000000), vee7Vf25(0x1)
    0xeefS0xf25: veefVf25 = AND veeeVf25(0xffffffffffffffffffffffffffffffffffffffff), v3a2
    0xef0S0xf25: vef0Vf25(0x0) = CONST 
    0xef4S0xf25: MSTORE vef0Vf25(0x0), veefVf25
    0xef5S0xf25: vef5Vf25(0x6) = CONST 
    0xef7S0xf25: vef7Vf25(0x20) = CONST 
    0xef9S0xf25: MSTORE vef7Vf25(0x20), vef5Vf25(0x6)
    0xefaS0xf25: vefaVf25(0x40) = CONST 
    0xefdS0xf25: vefdVf25 = SHA3 vef0Vf25(0x0), vefaVf25(0x40)
    0xefeS0xf25: vefeVf25 = SLOAD vefdVf25
    0xeffS0xf25: veffVf25 = ISZERO vefeVf25
    0xf00S0xf25: vf00Vf25 = ISZERO veffVf25
    0xf02S0xf25: JUMP vf26(0xf2e)

    Begin block 0xf2e
    prev=[0xee6B0xf25], succ=[0xf35, 0xf39]
    =================================
    0xf2f: vf2f = ISZERO vf00Vf25
    0xf30: vf30 = ISZERO vf2f
    0xf31: vf31(0xf39) = CONST 
    0xf34: JUMPI vf31(0xf39), vf30

    Begin block 0xf35
    prev=[0xf2e], succ=[]
    =================================
    0xf35: vf35(0x0) = CONST 
    0xf38: REVERT vf35(0x0), vf35(0x0)

    Begin block 0xf39
    prev=[0xf2e], succ=[0xf67, 0xf68]
    =================================
    0xf3a: vf3a(0x1) = CONST 
    0xf3c: vf3c(0xa0) = CONST 
    0xf3e: vf3e(0x2) = CONST 
    0xf40: vf40(0x10000000000000000000000000000000000000000) = EXP vf3e(0x2), vf3c(0xa0)
    0xf41: vf41(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf40(0x10000000000000000000000000000000000000000), vf3a(0x1)
    0xf43: vf43 = AND v3a2, vf41(0xffffffffffffffffffffffffffffffffffffffff)
    0xf44: vf44(0x0) = CONST 
    0xf48: MSTORE vf44(0x0), vf43
    0xf49: vf49(0x6) = CONST 
    0xf4b: vf4b(0x20) = CONST 
    0xf4d: MSTORE vf4b(0x20), vf49(0x6)
    0xf4e: vf4e(0x40) = CONST 
    0xf51: vf51 = SHA3 vf44(0x0), vf4e(0x40)
    0xf52: vf52 = SLOAD vf51
    0xf53: vf53(0x7) = CONST 
    0xf56: vf56 = SLOAD vf53(0x7)
    0xf5b: vf5b(0x0) = CONST 
    0xf5d: vf5d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vf5b(0x0)
    0xf5f: vf5f = ADD vf56, vf5d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xf62: vf62 = LT vf5f, vf56
    0xf63: vf63(0xf68) = CONST 
    0xf66: JUMPI vf63(0xf68), vf62

    Begin block 0xf67
    prev=[0xf39], succ=[]
    =================================
    0xf67: THROW 

    Begin block 0xf68
    prev=[0xf39], succ=[0xfa1, 0xfa2]
    =================================
    0xf69: vf69(0x0) = CONST 
    0xf6d: MSTORE vf69(0x0), vf53(0x7)
    0xf6e: vf6e(0x20) = CONST 
    0xf72: vf72 = SHA3 vf69(0x0), vf6e(0x20)
    0xf75: vf75 = ADD vf5f, vf72
    0xf76: vf76 = SLOAD vf75
    0xf77: vf77(0x1) = CONST 
    0xf79: vf79(0xa0) = CONST 
    0xf7b: vf7b(0x2) = CONST 
    0xf7d: vf7d(0x10000000000000000000000000000000000000000) = EXP vf7b(0x2), vf79(0xa0)
    0xf7e: vf7e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf7d(0x10000000000000000000000000000000000000000), vf77(0x1)
    0xf7f: vf7f = AND vf7e(0xffffffffffffffffffffffffffffffffffffffff), vf76
    0xf82: MSTORE vf69(0x0), vf7f
    0xf83: vf83(0x6) = CONST 
    0xf87: MSTORE vf6e(0x20), vf83(0x6)
    0xf88: vf88(0x40) = CONST 
    0xf8c: vf8c = SHA3 vf69(0x0), vf88(0x40)
    0xf8f: SSTORE vf8c, vf52
    0xf90: vf90(0x7) = CONST 
    0xf93: vf93 = SLOAD vf90(0x7)
    0xf9c: vf9c = LT vf52, vf93
    0xf9d: vf9d(0xfa2) = CONST 
    0xfa0: JUMPI vf9d(0xfa2), vf9c

    Begin block 0xfa1
    prev=[0xf68], succ=[]
    =================================
    0xfa1: THROW 

    Begin block 0xfa2
    prev=[0xf68], succ=[0x111dB0xfa2]
    =================================
    0xfa3: vfa3(0x0) = CONST 
    0xfa7: MSTORE vfa3(0x0), vf90(0x7)
    0xfa8: vfa8(0x20) = CONST 
    0xfac: vfac = SHA3 vfa3(0x0), vfa8(0x20)
    0xfad: vfad = ADD vfac, vf52
    0xfaf: vfaf = SLOAD vfad
    0xfb0: vfb0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfc5: vfc5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vfb0(0xffffffffffffffffffffffffffffffffffffffff)
    0xfc6: vfc6 = AND vfc5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vfaf
    0xfc7: vfc7(0x1) = CONST 
    0xfc9: vfc9(0xa0) = CONST 
    0xfcb: vfcb(0x2) = CONST 
    0xfcd: vfcd(0x10000000000000000000000000000000000000000) = EXP vfcb(0x2), vfc9(0xa0)
    0xfce: vfce(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfcd(0x10000000000000000000000000000000000000000), vfc7(0x1)
    0xfd2: vfd2 = AND vfce(0xffffffffffffffffffffffffffffffffffffffff), vf7f
    0xfd6: vfd6 = OR vfd2, vfc6
    0xfd8: SSTORE vfad, vfd6
    0xfd9: vfd9(0x7) = CONST 
    0xfdc: vfdc = SLOAD vfd9(0x7)
    0xfde: vfde(0xfeb) = CONST 
    0xfe2: vfe2(0x0) = CONST 
    0xfe4: vfe4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vfe2(0x0)
    0xfe6: vfe6 = ADD vfdc, vfe4(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xfe7: vfe7(0x111d) = CONST 
    0xfea: JUMP vfe7(0x111d), vfe6, vfd9(0x7), vfde(0xfeb)

    Begin block 0x111dB0xfa2
    prev=[0xfa2], succ=[0x112bB0xfa2, 0x17caB0xfa2]
    =================================
    0x111fS0xfa2: v111fVfa2 = SLOAD vfd9(0x7)
    0x1122S0xfa2: SSTORE vfd9(0x7), vfe6
    0x1125S0xfa2: v1125Vfa2 = GT v111fVfa2, vfe6
    0x1126S0xfa2: v1126Vfa2 = ISZERO v1125Vfa2
    0x1127S0xfa2: v1127Vfa2(0x17ca) = CONST 
    0x112aS0xfa2: JUMPI v1127Vfa2(0x17ca), v1126Vfa2

    Begin block 0x112bB0xfa2
    prev=[0x111dB0xfa2], succ=[0x1146B0x112bB0xfa2]
    =================================
    0x112bS0xfa2: v112bVfa2(0x0) = CONST 
    0x112fS0xfa2: MSTORE v112bVfa2(0x0), vfd9(0x7)
    0x1130S0xfa2: v1130Vfa2(0x20) = CONST 
    0x1133S0xfa2: v1133Vfa2 = SHA3 v112bVfa2(0x0), v1130Vfa2(0x20)
    0x1134S0xfa2: v1134Vfa2(0x17ee) = CONST 
    0x1139S0xfa2: v1139Vfa2 = ADD v1133Vfa2, v111fVfa2
    0x113cS0xfa2: v113cVfa2 = ADD vfe6, v1133Vfa2
    0x113dS0xfa2: v113dVfa2(0x1146) = CONST 
    0x1140S0xfa2: JUMP v113dVfa2(0x1146)

    Begin block 0x1146B0x112bB0xfa2
    prev=[0x112bB0xfa2], succ=[0x114cB0x112bB0xfa2]
    =================================
    0x1147S0x112bS0xfa2: v1147V112bVfa2(0x1160) = CONST 

    Begin block 0x114cB0x112bB0xfa2
    prev=[0x1155B0x112bB0xfa2, 0x1146B0x112bB0xfa2], succ=[0x1155B0x112bB0xfa2, 0x1812B0x112bB0xfa2]
    =================================
    0x114c_0x0S0x112bS0xfa2: v114c_0V112bVfa2 = PHI v113cVfa2, v115bV112bVfa2
    0x114fS0x112bS0xfa2: v114fV112bVfa2 = GT v1139Vfa2, v114c_0V112bVfa2
    0x1150S0x112bS0xfa2: v1150V112bVfa2 = ISZERO v114fV112bVfa2
    0x1151S0x112bS0xfa2: v1151V112bVfa2(0x1812) = CONST 
    0x1154S0x112bS0xfa2: JUMPI v1151V112bVfa2(0x1812), v1150V112bVfa2

    Begin block 0x1155B0x112bB0xfa2
    prev=[0x114cB0x112bB0xfa2], succ=[0x114cB0x112bB0xfa2]
    =================================
    0x1155S0x112bS0xfa2: v1155V112bVfa2(0x0) = CONST 
    0x1155_0x0S0x112bS0xfa2: v1155_0V112bVfa2 = PHI v113cVfa2, v115bV112bVfa2
    0x1158S0x112bS0xfa2: SSTORE v1155_0V112bVfa2, v1155V112bVfa2(0x0)
    0x1159S0x112bS0xfa2: v1159V112bVfa2(0x1) = CONST 
    0x115bS0x112bS0xfa2: v115bV112bVfa2 = ADD v1159V112bVfa2(0x1), v1155_0V112bVfa2
    0x115cS0x112bS0xfa2: v115cV112bVfa2(0x114c) = CONST 
    0x115fS0x112bS0xfa2: JUMP v115cV112bVfa2(0x114c)

    Begin block 0x1812B0x112bB0xfa2
    prev=[0x114cB0x112bB0xfa2], succ=[0x1160B0x112bB0xfa2]
    =================================
    0x1815S0x112bS0xfa2: JUMP v1147V112bVfa2(0x1160)

    Begin block 0x1160B0x112bB0xfa2
    prev=[0x1812B0x112bB0xfa2], succ=[0x17eeB0xfa2]
    =================================
    0x1162S0x112bS0xfa2: JUMP v1134Vfa2(0x17ee)

    Begin block 0x17eeB0xfa2
    prev=[0x1160B0x112bB0xfa2], succ=[0xfeb]
    =================================
    0x17f2S0xfa2: JUMP vfde(0xfeb)

    Begin block 0xfeb
    prev=[0x17caB0xfa2, 0x17eeB0xfa2], succ=[0x16cd]
    =================================
    0xfed: vfed(0x1) = CONST 
    0xfef: vfef(0xa0) = CONST 
    0xff1: vff1(0x2) = CONST 
    0xff3: vff3(0x10000000000000000000000000000000000000000) = EXP vff1(0x2), vfef(0xa0)
    0xff4: vff4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vff3(0x10000000000000000000000000000000000000000), vfed(0x1)
    0xff6: vff6 = AND v3a2, vff4(0xffffffffffffffffffffffffffffffffffffffff)
    0xff7: vff7(0x0) = CONST 
    0xffb: MSTORE vff7(0x0), vff6
    0xffc: vffc(0x6) = CONST 
    0xffe: vffe(0x20) = CONST 
    0x1002: MSTORE vffe(0x20), vffc(0x6)
    0x1003: v1003(0x40) = CONST 
    0x1007: v1007 = SHA3 vff7(0x0), v1003(0x40)
    0x100b: SSTORE v1007, vff7(0x0)
    0x100d: v100d = MLOAD v1003(0x40)
    0x1010: MSTORE v100d, vff6
    0x1012: v1012 = MLOAD v1003(0x40)
    0x1013: v1013(0x3edc40c0328998eaea1b10228950034eb711623f80702c71897e856964c203c3) = CONST 
    0x1037: v1037(0x0) = SUB v100d, v1012
    0x103a: v103a(0x20) = ADD vffe(0x20), v1037(0x0)
    0x103c: LOG1 v1012, v103a(0x20), v1013(0x3edc40c0328998eaea1b10228950034eb711623f80702c71897e856964c203c3)
    0x103e: v103e(0x1) = CONST 
    0x1045: JUMP v394(0x16cd)

    Begin block 0x16cd
    prev=[0xfeb], succ=[]
    =================================
    0x16ce: v16ce(0x40) = CONST 
    0x16d1: v16d1 = MLOAD v16ce(0x40)
    0x16d3: v16d3 = ISZERO v103e(0x1)
    0x16d4: v16d4 = ISZERO v16d3
    0x16d6: MSTORE v16d1, v16d4
    0x16d7: v16d7 = MLOAD v16ce(0x40)
    0x16db: v16db(0x0) = SUB v16d1, v16d7
    0x16dc: v16dc(0x20) = CONST 
    0x16de: v16de(0x20) = ADD v16dc(0x20), v16db(0x0)
    0x16e0: RETURN v16d7, v16de(0x20)

    Begin block 0x17caB0xfa2
    prev=[0x111dB0xfa2], succ=[0xfeb]
    =================================
    0x17ceS0xfa2: JUMP vfde(0xfeb)

}

function allWorkers()() public {
    Begin block 0x3a7
    prev=[], succ=[0x3af, 0x3b3]
    =================================
    0x3a8: v3a8 = CALLVALUE 
    0x3aa: v3aa = ISZERO v3a8
    0x3ab: v3ab(0x3b3) = CONST 
    0x3ae: JUMPI v3ab(0x3b3), v3aa

    Begin block 0x3af
    prev=[0x3a7], succ=[]
    =================================
    0x3af: v3af(0x0) = CONST 
    0x3b2: REVERT v3af(0x0), v3af(0x0)

    Begin block 0x3b3
    prev=[0x3a7], succ=[0x1046B0x3b3]
    =================================
    0x3b5: v3b5(0x3bc) = CONST 
    0x3b8: v3b8(0x1046) = CONST 
    0x3bb: JUMP v3b8(0x1046)

    Begin block 0x1046B0x3b3
    prev=[0x3b3], succ=[0x107cB0x3b3, 0x106dB0x3b3]
    =================================
    0x1047S0x3b3: v1047V3b3(0x60) = CONST 
    0x1049S0x3b3: v1049V3b3(0x0) = CONST 
    0x104bS0x3b3: v104bV3b3(0x1) = CONST 
    0x104dS0x3b3: v104dV3b3(0x7) = CONST 
    0x1050S0x3b3: v1050V3b3 = SLOAD v104dV3b3(0x7)
    0x1053S0x3b3: v1053V3b3 = SUB v1050V3b3, v104bV3b3(0x1)
    0x1054S0x3b3: v1054V3b3(0x40) = CONST 
    0x1056S0x3b3: v1056V3b3 = MLOAD v1054V3b3(0x40)
    0x105aS0x3b3: MSTORE v1056V3b3, v1053V3b3
    0x105cS0x3b3: v105cV3b3(0x20) = CONST 
    0x105eS0x3b3: v105eV3b3 = MUL v105cV3b3(0x20), v1053V3b3
    0x105fS0x3b3: v105fV3b3(0x20) = CONST 
    0x1061S0x3b3: v1061V3b3 = ADD v105fV3b3(0x20), v105eV3b3
    0x1063S0x3b3: v1063V3b3 = ADD v1056V3b3, v1061V3b3
    0x1064S0x3b3: v1064V3b3(0x40) = CONST 
    0x1066S0x3b3: MSTORE v1064V3b3(0x40), v1063V3b3
    0x1068S0x3b3: v1068V3b3 = ISZERO v1053V3b3
    0x1069S0x3b3: v1069V3b3(0x107c) = CONST 
    0x106cS0x3b3: JUMPI v1069V3b3(0x107c), v1068V3b3

    Begin block 0x107cB0x3b3
    prev=[0x1046B0x3b3, 0x106dB0x3b3], succ=[0x1084B0x3b3]
    =================================
    0x1080S0x3b3: v1080V3b3(0x1) = CONST 

    Begin block 0x1084B0x3b3
    prev=[0x107cB0x3b3, 0x10c6B0x3b3], succ=[0x108fB0x3b3, 0x17a7B0x3b3]
    =================================
    0x1084_0x0S0x3b3: v1084_0V3b3 = PHI v1080V3b3(0x1), v10e0V3b3
    0x1085S0x3b3: v1085V3b3(0x7) = CONST 
    0x1087S0x3b3: v1087V3b3 = SLOAD v1085V3b3(0x7)
    0x1089S0x3b3: v1089V3b3 = LT v1084_0V3b3, v1087V3b3
    0x108aS0x3b3: v108aV3b3 = ISZERO v1089V3b3
    0x108bS0x3b3: v108bV3b3(0x17a7) = CONST 
    0x108eS0x3b3: JUMPI v108bV3b3(0x17a7), v108aV3b3

    Begin block 0x108fB0x3b3
    prev=[0x1084B0x3b3], succ=[0x109cB0x3b3, 0x109bB0x3b3]
    =================================
    0x108fS0x3b3: v108fV3b3(0x7) = CONST 
    0x108f_0x0S0x3b3: v108f_0V3b3 = PHI v1080V3b3(0x1), v10e0V3b3
    0x1092S0x3b3: v1092V3b3 = SLOAD v108fV3b3(0x7)
    0x1096S0x3b3: v1096V3b3 = LT v108f_0V3b3, v1092V3b3
    0x1097S0x3b3: v1097V3b3(0x109c) = CONST 
    0x109aS0x3b3: JUMPI v1097V3b3(0x109c), v1096V3b3

    Begin block 0x109cB0x3b3
    prev=[0x108fB0x3b3], succ=[0x10c6B0x3b3, 0x10c5B0x3b3]
    =================================
    0x109c_0x0S0x3b3: v109c_0V3b3 = PHI v1080V3b3(0x1), v10e0V3b3
    0x109c_0x2S0x3b3: v109c_2V3b3 = PHI v1080V3b3(0x1), v10e0V3b3
    0x109dS0x3b3: v109dV3b3(0x0) = CONST 
    0x10a1S0x3b3: MSTORE v109dV3b3(0x0), v108fV3b3(0x7)
    0x10a2S0x3b3: v10a2V3b3(0x20) = CONST 
    0x10a6S0x3b3: v10a6V3b3 = SHA3 v109dV3b3(0x0), v10a2V3b3(0x20)
    0x10a7S0x3b3: v10a7V3b3 = ADD v10a6V3b3, v109c_0V3b3
    0x10a8S0x3b3: v10a8V3b3 = SLOAD v10a7V3b3
    0x10aaS0x3b3: v10aaV3b3 = MLOAD v1056V3b3
    0x10abS0x3b3: v10abV3b3(0x1) = CONST 
    0x10adS0x3b3: v10adV3b3(0xa0) = CONST 
    0x10afS0x3b3: v10afV3b3(0x2) = CONST 
    0x10b1S0x3b3: v10b1V3b3(0x10000000000000000000000000000000000000000) = EXP v10afV3b3(0x2), v10adV3b3(0xa0)
    0x10b2S0x3b3: v10b2V3b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10b1V3b3(0x10000000000000000000000000000000000000000), v10abV3b3(0x1)
    0x10b5S0x3b3: v10b5V3b3 = AND v10a8V3b3, v10b2V3b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x10b9S0x3b3: v10b9V3b3(0x0) = CONST 
    0x10bbS0x3b3: v10bbV3b3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v10b9V3b3(0x0)
    0x10bdS0x3b3: v10bdV3b3 = ADD v109c_2V3b3, v10bbV3b3(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x10c0S0x3b3: v10c0V3b3 = LT v10bdV3b3, v10aaV3b3
    0x10c1S0x3b3: v10c1V3b3(0x10c6) = CONST 
    0x10c4S0x3b3: JUMPI v10c1V3b3(0x10c6), v10c0V3b3

    Begin block 0x10c6B0x3b3
    prev=[0x109cB0x3b3], succ=[0x1084B0x3b3]
    =================================
    0x10c6_0x3S0x3b3: v10c6_3V3b3 = PHI v1080V3b3(0x1), v10e0V3b3
    0x10c7S0x3b3: v10c7V3b3(0x1) = CONST 
    0x10c9S0x3b3: v10c9V3b3(0xa0) = CONST 
    0x10cbS0x3b3: v10cbV3b3(0x2) = CONST 
    0x10cdS0x3b3: v10cdV3b3(0x10000000000000000000000000000000000000000) = EXP v10cbV3b3(0x2), v10c9V3b3(0xa0)
    0x10ceS0x3b3: v10ceV3b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10cdV3b3(0x10000000000000000000000000000000000000000), v10c7V3b3(0x1)
    0x10d1S0x3b3: v10d1V3b3 = AND v10b5V3b3, v10ceV3b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x10d2S0x3b3: v10d2V3b3(0x20) = CONST 
    0x10d6S0x3b3: v10d6V3b3 = MUL v10d2V3b3(0x20), v10bdV3b3
    0x10d9S0x3b3: v10d9V3b3 = ADD v1056V3b3, v10d6V3b3
    0x10dcS0x3b3: v10dcV3b3 = ADD v10d2V3b3(0x20), v10d9V3b3
    0x10ddS0x3b3: MSTORE v10dcV3b3, v10d1V3b3
    0x10deS0x3b3: v10deV3b3(0x1) = CONST 
    0x10e0S0x3b3: v10e0V3b3 = ADD v10deV3b3(0x1), v10c6_3V3b3
    0x10e1S0x3b3: v10e1V3b3(0x1084) = CONST 
    0x10e4S0x3b3: JUMP v10e1V3b3(0x1084)

    Begin block 0x10c5B0x3b3
    prev=[0x109cB0x3b3], succ=[]
    =================================
    0x10c5S0x3b3: THROW 

    Begin block 0x109bB0x3b3
    prev=[0x108fB0x3b3], succ=[]
    =================================
    0x109bS0x3b3: THROW 

    Begin block 0x17a7B0x3b3
    prev=[0x1084B0x3b3], succ=[0x3bc]
    =================================
    0x17aaS0x3b3: JUMP v3b5(0x3bc)

    Begin block 0x3bc
    prev=[0x17a7B0x3b3], succ=[0x3e0]
    =================================
    0x3bd: v3bd(0x40) = CONST 
    0x3c0: v3c0 = MLOAD v3bd(0x40)
    0x3c1: v3c1(0x20) = CONST 
    0x3c5: MSTORE v3c0, v3c1(0x20)
    0x3c7: v3c7 = MLOAD v1056V3b3
    0x3ca: v3ca = ADD v3c0, v3c1(0x20)
    0x3cb: MSTORE v3ca, v3c7
    0x3cd: v3cd = MLOAD v1056V3b3
    0x3d4: v3d4 = ADD v3c0, v3bd(0x40)
    0x3d8: v3d8 = ADD v3c1(0x20), v1056V3b3
    0x3da: v3da = MUL v3cd, v3c1(0x20)
    0x3de: v3de(0x0) = CONST 

    Begin block 0x3e0
    prev=[0x3bc, 0x3e9], succ=[0x3f8, 0x3e9]
    =================================
    0x3e0_0x0: v3e0_0 = PHI v3de(0x0), v3f3
    0x3e3: v3e3 = LT v3e0_0, v3da
    0x3e4: v3e4 = ISZERO v3e3
    0x3e5: v3e5(0x3f8) = CONST 
    0x3e8: JUMPI v3e5(0x3f8), v3e4

    Begin block 0x3f8
    prev=[0x3e0], succ=[]
    =================================
    0x3ff: v3ff = ADD v3da, v3d4
    0x404: v404(0x40) = CONST 
    0x406: v406 = MLOAD v404(0x40)
    0x409: v409 = SUB v3ff, v406
    0x40b: RETURN v406, v409

    Begin block 0x3e9
    prev=[0x3e0], succ=[0x3e0]
    =================================
    0x3e9_0x0: v3e9_0 = PHI v3de(0x0), v3f3
    0x3eb: v3eb = ADD v3e9_0, v3d8
    0x3ec: v3ec = MLOAD v3eb
    0x3ef: v3ef = ADD v3e9_0, v3d4
    0x3f0: MSTORE v3ef, v3ec
    0x3f1: v3f1(0x20) = CONST 
    0x3f3: v3f3 = ADD v3f1(0x20), v3e9_0
    0x3f4: v3f4(0x3e0) = CONST 
    0x3f7: JUMP v3f4(0x3e0)

    Begin block 0x106dB0x3b3
    prev=[0x1046B0x3b3], succ=[0x107cB0x3b3]
    =================================
    0x106eS0x3b3: v106eV3b3(0x20) = CONST 
    0x1070S0x3b3: v1070V3b3 = ADD v106eV3b3(0x20), v1056V3b3
    0x1071S0x3b3: v1071V3b3(0x20) = CONST 
    0x1074S0x3b3: v1074V3b3 = MUL v1053V3b3, v1071V3b3(0x20)
    0x1076S0x3b3: v1076V3b3 = CODESIZE 
    0x1078S0x3b3: CODECOPY v1070V3b3, v1076V3b3, v1074V3b3
    0x1079S0x3b3: v1079V3b3 = ADD v1074V3b3, v1070V3b3

}

function forward()() public {
    Begin block 0x40c
    prev=[], succ=[0x414, 0x418]
    =================================
    0x40d: v40d = CALLVALUE 
    0x40f: v40f = ISZERO v40d
    0x410: v410(0x418) = CONST 
    0x413: JUMPI v410(0x418), v40f

    Begin block 0x414
    prev=[0x40c], succ=[]
    =================================
    0x414: v414(0x0) = CONST 
    0x417: REVERT v414(0x0), v414(0x0)

    Begin block 0x418
    prev=[0x40c], succ=[0x10e9]
    =================================
    0x41a: v41a(0x1700) = CONST 
    0x41d: v41d(0x10e9) = CONST 
    0x420: JUMP v41d(0x10e9)

    Begin block 0x10e9
    prev=[0x418], succ=[0x1700]
    =================================
    0x10ea: v10ea(0x2) = CONST 
    0x10ec: v10ec = SLOAD v10ea(0x2)
    0x10ed: v10ed(0x1) = CONST 
    0x10ef: v10ef(0xa0) = CONST 
    0x10f1: v10f1(0x2) = CONST 
    0x10f3: v10f3(0x10000000000000000000000000000000000000000) = EXP v10f1(0x2), v10ef(0xa0)
    0x10f4: v10f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10f3(0x10000000000000000000000000000000000000000), v10ed(0x1)
    0x10f5: v10f5 = AND v10f4(0xffffffffffffffffffffffffffffffffffffffff), v10ec
    0x10f7: JUMP v41a(0x1700)

    Begin block 0x1700
    prev=[0x10e9], succ=[]
    =================================
    0x1701: v1701(0x40) = CONST 
    0x1704: v1704 = MLOAD v1701(0x40)
    0x1705: v1705(0x1) = CONST 
    0x1707: v1707(0xa0) = CONST 
    0x1709: v1709(0x2) = CONST 
    0x170b: v170b(0x10000000000000000000000000000000000000000) = EXP v1709(0x2), v1707(0xa0)
    0x170c: v170c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v170b(0x10000000000000000000000000000000000000000), v1705(0x1)
    0x170f: v170f = AND v10f5, v170c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1711: MSTORE v1704, v170f
    0x1712: v1712 = MLOAD v1701(0x40)
    0x1716: v1716(0x0) = SUB v1704, v1712
    0x1717: v1717(0x20) = CONST 
    0x1719: v1719(0x20) = ADD v1717(0x20), v1716(0x0)
    0x171b: RETURN v1712, v1719(0x20)

}

function createdWallets()() public {
    Begin block 0x421
    prev=[], succ=[0x429, 0x42d]
    =================================
    0x422: v422 = CALLVALUE 
    0x424: v424 = ISZERO v422
    0x425: v425(0x42d) = CONST 
    0x428: JUMPI v425(0x42d), v424

    Begin block 0x429
    prev=[0x421], succ=[]
    =================================
    0x429: v429(0x0) = CONST 
    0x42c: REVERT v429(0x0), v429(0x0)

    Begin block 0x42d
    prev=[0x421], succ=[0x10f8]
    =================================
    0x42f: v42f(0x173b) = CONST 
    0x432: v432(0x10f8) = CONST 
    0x435: JUMP v432(0x10f8)

    Begin block 0x10f8
    prev=[0x42d], succ=[0x173b]
    =================================
    0x10f9: v10f9(0x3) = CONST 
    0x10fb: v10fb = SLOAD v10f9(0x3)
    0x10fd: JUMP v42f(0x173b)

    Begin block 0x173b
    prev=[0x10f8], succ=[]
    =================================
    0x173c: v173c(0x40) = CONST 
    0x173f: v173f = MLOAD v173c(0x40)
    0x1742: MSTORE v173f, v10fb
    0x1743: v1743 = MLOAD v173c(0x40)
    0x1747: v1747(0x0) = SUB v173f, v1743
    0x1748: v1748(0x20) = CONST 
    0x174a: v174a(0x20) = ADD v1748(0x20), v1747(0x0)
    0x174c: RETURN v1743, v174a(0x20)

}

function walletsDelegate()() public {
    Begin block 0x436
    prev=[], succ=[0x43e, 0x442]
    =================================
    0x437: v437 = CALLVALUE 
    0x439: v439 = ISZERO v437
    0x43a: v43a(0x442) = CONST 
    0x43d: JUMPI v43a(0x442), v439

    Begin block 0x43e
    prev=[0x436], succ=[]
    =================================
    0x43e: v43e(0x0) = CONST 
    0x441: REVERT v43e(0x0), v43e(0x0)

    Begin block 0x442
    prev=[0x436], succ=[0x10fe]
    =================================
    0x444: v444(0x176c) = CONST 
    0x447: v447(0x10fe) = CONST 
    0x44a: JUMP v447(0x10fe)

    Begin block 0x10fe
    prev=[0x442], succ=[0x176c]
    =================================
    0x10ff: v10ff(0x0) = CONST 
    0x1101: v1101 = SLOAD v10ff(0x0)
    0x1102: v1102(0x1) = CONST 
    0x1104: v1104(0xa0) = CONST 
    0x1106: v1106(0x2) = CONST 
    0x1108: v1108(0x10000000000000000000000000000000000000000) = EXP v1106(0x2), v1104(0xa0)
    0x1109: v1109(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1108(0x10000000000000000000000000000000000000000), v1102(0x1)
    0x110a: v110a = AND v1109(0xffffffffffffffffffffffffffffffffffffffff), v1101
    0x110c: JUMP v444(0x176c)

    Begin block 0x176c
    prev=[0x10fe], succ=[]
    =================================
    0x176d: v176d(0x40) = CONST 
    0x1770: v1770 = MLOAD v176d(0x40)
    0x1771: v1771(0x1) = CONST 
    0x1773: v1773(0xa0) = CONST 
    0x1775: v1775(0x2) = CONST 
    0x1777: v1777(0x10000000000000000000000000000000000000000) = EXP v1775(0x2), v1773(0xa0)
    0x1778: v1778(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1777(0x10000000000000000000000000000000000000000), v1771(0x1)
    0x177b: v177b = AND v110a, v1778(0xffffffffffffffffffffffffffffffffffffffff)
    0x177d: MSTORE v1770, v177b
    0x177e: v177e = MLOAD v176d(0x40)
    0x1782: v1782(0x0) = SUB v1770, v177e
    0x1783: v1783(0x20) = CONST 
    0x1785: v1785(0x20) = ADD v1783(0x20), v1782(0x0)
    0x1787: RETURN v177e, v1785(0x20)

}

function fallback()() public {
    Begin block 0xfb
    prev=[], succ=[]
    =================================
    0xfc: STOP 

}

function withdrawEthBatch(address[])() public {
    Begin block 0xfd
    prev=[], succ=[0x105, 0x109]
    =================================
    0xfe: vfe = CALLVALUE 
    0x100: v100 = ISZERO vfe
    0x101: v101(0x109) = CONST 
    0x104: JUMPI v101(0x109), v100

    Begin block 0x105
    prev=[0xfd], succ=[]
    =================================
    0x105: v105(0x0) = CONST 
    0x108: REVERT v105(0x0), v105(0x0)

    Begin block 0x109
    prev=[0xfd], succ=[0x44b]
    =================================
    0x10b: v10b(0x40) = CONST 
    0x10e: v10e = MLOAD v10b(0x40)
    0x10f: v10f(0x20) = CONST 
    0x111: v111(0x4) = CONST 
    0x114: v114 = CALLDATALOAD v111(0x4)
    0x117: v117 = ADD v111(0x4), v114
    0x118: v118 = CALLDATALOAD v117
    0x11b: v11b = MUL v118, v10f(0x20)
    0x11e: v11e = ADD v10e, v11b
    0x120: v120 = ADD v10f(0x20), v11e
    0x123: MSTORE v10b(0x40), v120
    0x126: MSTORE v10e, v118
    0x127: v127(0x1428) = CONST 
    0x12b: v12b = CALLDATASIZE 
    0x12f: v12f(0x24) = CONST 
    0x134: v134 = ADD v12f(0x24), v114
    0x13a: v13a = ADD v10e, v10f(0x20)
    0x141: CALLDATACOPY v13a, v134, v11b
    0x146: v146(0x44b) = CONST 
    0x151: JUMP v146(0x44b)

    Begin block 0x44b
    prev=[0x109], succ=[0xee6B0x44b]
    =================================
    0x44c: v44c(0x0) = CONST 
    0x44f: v44f(0x0) = CONST 
    0x452: v452(0x0) = CONST 
    0x454: v454(0x45c) = CONST 
    0x457: v457 = CALLER 
    0x458: v458(0xee6) = CONST 
    0x45b: JUMP v458(0xee6)

    Begin block 0xee6B0x44b
    prev=[0x44b], succ=[0x45c]
    =================================
    0xee7S0x44b: vee7V44b(0x1) = CONST 
    0xee9S0x44b: vee9V44b(0xa0) = CONST 
    0xeebS0x44b: veebV44b(0x2) = CONST 
    0xeedS0x44b: veedV44b(0x10000000000000000000000000000000000000000) = EXP veebV44b(0x2), vee9V44b(0xa0)
    0xeeeS0x44b: veeeV44b(0xffffffffffffffffffffffffffffffffffffffff) = SUB veedV44b(0x10000000000000000000000000000000000000000), vee7V44b(0x1)
    0xeefS0x44b: veefV44b = AND veeeV44b(0xffffffffffffffffffffffffffffffffffffffff), v457
    0xef0S0x44b: vef0V44b(0x0) = CONST 
    0xef4S0x44b: MSTORE vef0V44b(0x0), veefV44b
    0xef5S0x44b: vef5V44b(0x6) = CONST 
    0xef7S0x44b: vef7V44b(0x20) = CONST 
    0xef9S0x44b: MSTORE vef7V44b(0x20), vef5V44b(0x6)
    0xefaS0x44b: vefaV44b(0x40) = CONST 
    0xefdS0x44b: vefdV44b = SHA3 vef0V44b(0x0), vefaV44b(0x40)
    0xefeS0x44b: vefeV44b = SLOAD vefdV44b
    0xeffS0x44b: veffV44b = ISZERO vefeV44b
    0xf00S0x44b: vf00V44b = ISZERO veffV44b
    0xf02S0x44b: JUMP v454(0x45c)

    Begin block 0x45c
    prev=[0xee6B0x44b], succ=[0x463, 0x467]
    =================================
    0x45d: v45d = ISZERO vf00V44b
    0x45e: v45e = ISZERO v45d
    0x45f: v45f(0x467) = CONST 
    0x462: JUMPI v45f(0x467), v45e

    Begin block 0x463
    prev=[0x45c], succ=[]
    =================================
    0x463: v463(0x0) = CONST 
    0x466: REVERT v463(0x0), v463(0x0)

    Begin block 0x467
    prev=[0x45c], succ=[0x46f]
    =================================
    0x46a: v46a = MLOAD v10e
    0x46d: v46d(0x0) = CONST 

    Begin block 0x46f
    prev=[0x467, 0x57f], succ=[0x587, 0x478]
    =================================
    0x46f_0x0: v46f_0 = PHI v46d(0x0), v582
    0x472: v472 = LT v46f_0, v46a
    0x473: v473 = ISZERO v472
    0x474: v474(0x587) = CONST 
    0x477: JUMPI v474(0x587), v473

    Begin block 0x587
    prev=[0x46f], succ=[0x1428]
    =================================
    0x588: v588(0x2) = CONST 
    0x58a: v58a = SLOAD v588(0x2)
    0x58b: v58b(0x40) = CONST 
    0x58d: v58d = MLOAD v58b(0x40)
    0x58e: v58e(0x1) = CONST 
    0x590: v590(0xa0) = CONST 
    0x592: v592(0x2) = CONST 
    0x594: v594(0x10000000000000000000000000000000000000000) = EXP v592(0x2), v590(0xa0)
    0x595: v595(0xffffffffffffffffffffffffffffffffffffffff) = SUB v594(0x10000000000000000000000000000000000000000), v58e(0x1)
    0x598: v598 = AND v595(0xffffffffffffffffffffffffffffffffffffffff), v58a
    0x59a: v59a = ADDRESS 
    0x59b: v59b = AND v59a, v595(0xffffffffffffffffffffffffffffffffffffffff)
    0x59c: v59c = BALANCE v59b
    0x59e: v59e(0x0) = CONST 
    0x5a5: v5a5 = GAS 
    0x5a6: v5a6 = CALL v5a5, v598, v59c, v58d, v59e(0x0), v58d, v59e(0x0)
    0x5a8: v5a8(0x1) = CONST 
    0x5b5: JUMP v127(0x1428)

    Begin block 0x1428
    prev=[0x587], succ=[]
    =================================
    0x1429: v1429(0x40) = CONST 
    0x142c: v142c = MLOAD v1429(0x40)
    0x142e: v142e = ISZERO v5a8(0x1)
    0x142f: v142f = ISZERO v142e
    0x1431: MSTORE v142c, v142f
    0x1432: v1432 = MLOAD v1429(0x40)
    0x1436: v1436(0x0) = SUB v142c, v1432
    0x1437: v1437(0x20) = CONST 
    0x1439: v1439(0x20) = ADD v1437(0x20), v1436(0x0)
    0x143b: RETURN v1432, v1439(0x20)

    Begin block 0x478
    prev=[0x46f], succ=[0x484, 0x485]
    =================================
    0x478_0x0: v478_0 = PHI v46d(0x0), v582
    0x47b: v47b = MLOAD v10e
    0x47d: v47d = LT v478_0, v47b
    0x47e: v47e = ISZERO v47d
    0x47f: v47f = ISZERO v47e
    0x480: v480(0x485) = CONST 
    0x483: JUMPI v480(0x485), v47f

    Begin block 0x484
    prev=[0x478], succ=[]
    =================================
    0x484: THROW 

    Begin block 0x485
    prev=[0x478], succ=[0x4fc, 0x500]
    =================================
    0x485_0x0: v485_0 = PHI v46d(0x0), v582
    0x486: v486(0x20) = CONST 
    0x48a: v48a = MUL v486(0x20), v485_0
    0x48d: v48d = ADD v10e, v48a
    0x48f: v48f = ADD v486(0x20), v48d
    0x490: v490 = MLOAD v48f
    0x491: v491(0x40) = CONST 
    0x494: v494 = MLOAD v491(0x40)
    0x495: v495(0x5b1137b00000000000000000000000000000000000000000000000000000000) = CONST 
    0x4b7: MSTORE v494, v495(0x5b1137b00000000000000000000000000000000000000000000000000000000)
    0x4b8: v4b8 = ADDRESS 
    0x4b9: v4b9(0x1) = CONST 
    0x4bb: v4bb(0xa0) = CONST 
    0x4bd: v4bd(0x2) = CONST 
    0x4bf: v4bf(0x10000000000000000000000000000000000000000) = EXP v4bd(0x2), v4bb(0xa0)
    0x4c0: v4c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4bf(0x10000000000000000000000000000000000000000), v4b9(0x1)
    0x4c3: v4c3 = AND v4c0(0xffffffffffffffffffffffffffffffffffffffff), v4b8
    0x4c4: v4c4(0x4) = CONST 
    0x4c7: v4c7 = ADD v494, v4c4(0x4)
    0x4c8: MSTORE v4c7, v4c3
    0x4ca: v4ca = AND v490, v4c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x4cc: v4cc = BALANCE v4ca
    0x4cd: v4cd(0x24) = CONST 
    0x4d0: v4d0 = ADD v494, v4cd(0x24)
    0x4d3: MSTORE v4d0, v4cc
    0x4d5: v4d5 = MLOAD v491(0x40)
    0x4de: v4de(0x5b1137b) = CONST 
    0x4e4: v4e4(0x44) = CONST 
    0x4e8: v4e8 = ADD v494, v4e4(0x44)
    0x4ed: v4ed(0x0) = SUB v494, v4d5
    0x4ee: v4ee(0x44) = ADD v4ed(0x0), v4e4(0x44)
    0x4f0: v4f0(0x0) = CONST 
    0x4f4: v4f4 = EXTCODESIZE v4ca
    0x4f5: v4f5 = ISZERO v4f4
    0x4f7: v4f7 = ISZERO v4f5
    0x4f8: v4f8(0x500) = CONST 
    0x4fb: JUMPI v4f8(0x500), v4f7

    Begin block 0x4fc
    prev=[0x485], succ=[]
    =================================
    0x4fc: v4fc(0x0) = CONST 
    0x4ff: REVERT v4fc(0x0), v4fc(0x0)

    Begin block 0x500
    prev=[0x485], succ=[0x50b, 0x514]
    =================================
    0x502: v502 = GAS 
    0x503: v503 = CALL v502, v4ca, v4f0(0x0), v4d5, v4ee(0x44), v4d5, v486(0x20)
    0x504: v504 = ISZERO v503
    0x506: v506 = ISZERO v504
    0x507: v507(0x514) = CONST 
    0x50a: JUMPI v507(0x514), v506

    Begin block 0x50b
    prev=[0x500], succ=[]
    =================================
    0x50b: v50b = RETURNDATASIZE 
    0x50c: v50c(0x0) = CONST 
    0x50f: RETURNDATACOPY v50c(0x0), v50c(0x0), v50b
    0x510: v510 = RETURNDATASIZE 
    0x511: v511(0x0) = CONST 
    0x513: REVERT v511(0x0), v510

    Begin block 0x514
    prev=[0x500], succ=[0x526, 0x52a]
    =================================
    0x519: v519(0x40) = CONST 
    0x51b: v51b = MLOAD v519(0x40)
    0x51c: v51c = RETURNDATASIZE 
    0x51d: v51d(0x20) = CONST 
    0x520: v520 = LT v51c, v51d(0x20)
    0x521: v521 = ISZERO v520
    0x522: v522(0x52a) = CONST 
    0x525: JUMPI v522(0x52a), v521

    Begin block 0x526
    prev=[0x514], succ=[]
    =================================
    0x526: v526(0x0) = CONST 
    0x529: REVERT v526(0x0), v526(0x0)

    Begin block 0x52a
    prev=[0x514], succ=[0x532, 0x57f]
    =================================
    0x52c: v52c = MLOAD v51b
    0x52d: v52d = ISZERO v52c
    0x52e: v52e(0x57f) = CONST 
    0x531: JUMPI v52e(0x57f), v52d

    Begin block 0x532
    prev=[0x52a], succ=[0x57f]
    =================================
    0x532: v532(0x2) = CONST 
    0x534: v534 = SLOAD v532(0x2)
    0x535: v535(0x40) = CONST 
    0x538: v538 = MLOAD v535(0x40)
    0x539: v539(0x1) = CONST 
    0x53b: v53b(0xa0) = CONST 
    0x53d: v53d(0x2) = CONST 
    0x53f: v53f(0x10000000000000000000000000000000000000000) = EXP v53d(0x2), v53b(0xa0)
    0x540: v540(0xffffffffffffffffffffffffffffffffffffffff) = SUB v53f(0x10000000000000000000000000000000000000000), v539(0x1)
    0x543: v543 = AND v490, v540(0xffffffffffffffffffffffffffffffffffffffff)
    0x545: MSTORE v538, v543
    0x548: v548 = AND v534, v540(0xffffffffffffffffffffffffffffffffffffffff)
    0x549: v549(0x20) = CONST 
    0x54c: v54c = ADD v538, v549(0x20)
    0x54d: MSTORE v54c, v548
    0x550: v550 = ADD v535(0x40), v538
    0x553: MSTORE v550, v4cc
    0x554: v554 = MLOAD v535(0x40)
    0x555: v555(0xe70f5b0cde63d9585e55497b8b0a46df83751189868f8b77ddc353ea444f6c19) = CONST 
    0x579: v579(0x0) = SUB v538, v554
    0x57a: v57a(0x60) = CONST 
    0x57c: v57c(0x60) = ADD v57a(0x60), v579(0x0)
    0x57e: LOG1 v554, v57c(0x60), v555(0xe70f5b0cde63d9585e55497b8b0a46df83751189868f8b77ddc353ea444f6c19)

    Begin block 0x57f
    prev=[0x532, 0x52a], succ=[0x46f]
    =================================
    0x57f_0x0: v57f_0 = PHI v46d(0x0), v582
    0x580: v580(0x1) = CONST 
    0x582: v582 = ADD v580(0x1), v57f_0
    0x583: v583(0x46f) = CONST 
    0x586: JUMP v583(0x46f)

}

