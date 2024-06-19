function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x1852]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x181c: v181c(0x1852) = CONST 
    0x181d: JUMPI v181c(0x1852), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x1855]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x6fdde03) = CONST 
    0x3b: v3b = EQ v34, v35(0x6fdde03)
    0x181e: v181e(0x1855) = CONST 
    0x181f: JUMPI v181e(0x1855), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x1858, 0x4b]
    =================================
    0x41: v41(0x95ea7b3) = CONST 
    0x46: v46 = EQ v41(0x95ea7b3), v34
    0x1820: v1820(0x1858) = CONST 
    0x1821: JUMPI v1820(0x1858), v46

    Begin block 0x1858
    prev=[0x40], succ=[]
    =================================
    0x1859: v1859(0x1e2) = CONST 
    0x185a: CALLPRIVATE v1859(0x1e2)

    Begin block 0x4b
    prev=[0x40], succ=[0x185b, 0x56]
    =================================
    0x4c: v4c(0x18160ddd) = CONST 
    0x51: v51 = EQ v4c(0x18160ddd), v34
    0x1822: v1822(0x185b) = CONST 
    0x1823: JUMPI v1822(0x185b), v51

    Begin block 0x185b
    prev=[0x4b], succ=[]
    =================================
    0x185c: v185c(0x21a) = CONST 
    0x185d: CALLPRIVATE v185c(0x21a)

    Begin block 0x56
    prev=[0x4b], succ=[0x185e, 0x61]
    =================================
    0x57: v57(0x23b872dd) = CONST 
    0x5c: v5c = EQ v57(0x23b872dd), v34
    0x1824: v1824(0x185e) = CONST 
    0x1825: JUMPI v1824(0x185e), v5c

    Begin block 0x185e
    prev=[0x56], succ=[]
    =================================
    0x185f: v185f(0x241) = CONST 
    0x1860: CALLPRIVATE v185f(0x241)

    Begin block 0x61
    prev=[0x56], succ=[0x1861, 0x6c]
    =================================
    0x62: v62(0x313ce567) = CONST 
    0x67: v67 = EQ v62(0x313ce567), v34
    0x1826: v1826(0x1861) = CONST 
    0x1827: JUMPI v1826(0x1861), v67

    Begin block 0x1861
    prev=[0x61], succ=[]
    =================================
    0x1862: v1862(0x26b) = CONST 
    0x1863: CALLPRIVATE v1862(0x26b)

    Begin block 0x6c
    prev=[0x61], succ=[0x1864, 0x77]
    =================================
    0x6d: v6d(0x3659cfe6) = CONST 
    0x72: v72 = EQ v6d(0x3659cfe6), v34
    0x1828: v1828(0x1864) = CONST 
    0x1829: JUMPI v1828(0x1864), v72

    Begin block 0x1864
    prev=[0x6c], succ=[]
    =================================
    0x1865: v1865(0x296) = CONST 
    0x1866: CALLPRIVATE v1865(0x296)

    Begin block 0x77
    prev=[0x6c], succ=[0x1867, 0x82]
    =================================
    0x78: v78(0x3f4ba83a) = CONST 
    0x7d: v7d = EQ v78(0x3f4ba83a), v34
    0x182a: v182a(0x1867) = CONST 
    0x182b: JUMPI v182a(0x1867), v7d

    Begin block 0x1867
    prev=[0x77], succ=[]
    =================================
    0x1868: v1868(0x2b7) = CONST 
    0x1869: CALLPRIVATE v1868(0x2b7)

    Begin block 0x82
    prev=[0x77], succ=[0x186a, 0x8d]
    =================================
    0x83: v83(0x40c10f19) = CONST 
    0x88: v88 = EQ v83(0x40c10f19), v34
    0x182c: v182c(0x186a) = CONST 
    0x182d: JUMPI v182c(0x186a), v88

    Begin block 0x186a
    prev=[0x82], succ=[]
    =================================
    0x186b: v186b(0x2ce) = CONST 
    0x186c: CALLPRIVATE v186b(0x2ce)

    Begin block 0x8d
    prev=[0x82], succ=[0x186d, 0x98]
    =================================
    0x8e: v8e(0x54fd4d50) = CONST 
    0x93: v93 = EQ v8e(0x54fd4d50), v34
    0x182e: v182e(0x186d) = CONST 
    0x182f: JUMPI v182e(0x186d), v93

    Begin block 0x186d
    prev=[0x8d], succ=[]
    =================================
    0x186e: v186e(0x2f2) = CONST 
    0x186f: CALLPRIVATE v186e(0x2f2)

    Begin block 0x98
    prev=[0x8d], succ=[0x1870, 0xa3]
    =================================
    0x99: v99(0x5c975abb) = CONST 
    0x9e: v9e = EQ v99(0x5c975abb), v34
    0x1830: v1830(0x1870) = CONST 
    0x1831: JUMPI v1830(0x1870), v9e

    Begin block 0x1870
    prev=[0x98], succ=[]
    =================================
    0x1871: v1871(0x307) = CONST 
    0x1872: CALLPRIVATE v1871(0x307)

    Begin block 0xa3
    prev=[0x98], succ=[0x1873, 0xae]
    =================================
    0xa4: va4(0x66188463) = CONST 
    0xa9: va9 = EQ va4(0x66188463), v34
    0x1832: v1832(0x1873) = CONST 
    0x1833: JUMPI v1832(0x1873), va9

    Begin block 0x1873
    prev=[0xa3], succ=[]
    =================================
    0x1874: v1874(0x31c) = CONST 
    0x1875: CALLPRIVATE v1874(0x31c)

    Begin block 0xae
    prev=[0xa3], succ=[0x1876, 0xb9]
    =================================
    0xaf: vaf(0x66e3cb68) = CONST 
    0xb4: vb4 = EQ vaf(0x66e3cb68), v34
    0x1834: v1834(0x1876) = CONST 
    0x1835: JUMPI v1834(0x1876), vb4

    Begin block 0x1876
    prev=[0xae], succ=[]
    =================================
    0x1877: v1877(0x340) = CONST 
    0x1878: CALLPRIVATE v1877(0x340)

    Begin block 0xb9
    prev=[0xae], succ=[0x1879, 0xc4]
    =================================
    0xba: vba(0x6ff968c3) = CONST 
    0xbf: vbf = EQ vba(0x6ff968c3), v34
    0x1836: v1836(0x1879) = CONST 
    0x1837: JUMPI v1836(0x1879), vbf

    Begin block 0x1879
    prev=[0xb9], succ=[]
    =================================
    0x187a: v187a(0x361) = CONST 
    0x187b: CALLPRIVATE v187a(0x361)

    Begin block 0xc4
    prev=[0xb9], succ=[0x187c, 0xcf]
    =================================
    0xc5: vc5(0x70a08231) = CONST 
    0xca: vca = EQ vc5(0x70a08231), v34
    0x1838: v1838(0x187c) = CONST 
    0x1839: JUMPI v1838(0x187c), vca

    Begin block 0x187c
    prev=[0xc4], succ=[]
    =================================
    0x187d: v187d(0x392) = CONST 
    0x187e: CALLPRIVATE v187d(0x392)

    Begin block 0xcf
    prev=[0xc4], succ=[0x187f, 0xda]
    =================================
    0xd0: vd0(0x715018a6) = CONST 
    0xd5: vd5 = EQ vd0(0x715018a6), v34
    0x183a: v183a(0x187f) = CONST 
    0x183b: JUMPI v183a(0x187f), vd5

    Begin block 0x187f
    prev=[0xcf], succ=[]
    =================================
    0x1880: v1880(0x3b3) = CONST 
    0x1881: CALLPRIVATE v1880(0x3b3)

    Begin block 0xda
    prev=[0xcf], succ=[0x1882, 0xe5]
    =================================
    0xdb: vdb(0x8456cb59) = CONST 
    0xe0: ve0 = EQ vdb(0x8456cb59), v34
    0x183c: v183c(0x1882) = CONST 
    0x183d: JUMPI v183c(0x1882), ve0

    Begin block 0x1882
    prev=[0xda], succ=[]
    =================================
    0x1883: v1883(0x3c8) = CONST 
    0x1884: CALLPRIVATE v1883(0x3c8)

    Begin block 0xe5
    prev=[0xda], succ=[0x1885, 0xf0]
    =================================
    0xe6: ve6(0x8da5cb5b) = CONST 
    0xeb: veb = EQ ve6(0x8da5cb5b), v34
    0x183e: v183e(0x1885) = CONST 
    0x183f: JUMPI v183e(0x1885), veb

    Begin block 0x1885
    prev=[0xe5], succ=[]
    =================================
    0x1886: v1886(0x3dd) = CONST 
    0x1887: CALLPRIVATE v1886(0x3dd)

    Begin block 0xf0
    prev=[0xe5], succ=[0x1888, 0xfb]
    =================================
    0xf1: vf1(0x9137c1a7) = CONST 
    0xf6: vf6 = EQ vf1(0x9137c1a7), v34
    0x1840: v1840(0x1888) = CONST 
    0x1841: JUMPI v1840(0x1888), vf6

    Begin block 0x1888
    prev=[0xf0], succ=[]
    =================================
    0x1889: v1889(0x3f2) = CONST 
    0x188a: CALLPRIVATE v1889(0x3f2)

    Begin block 0xfb
    prev=[0xf0], succ=[0x188b, 0x106]
    =================================
    0xfc: vfc(0x95d89b41) = CONST 
    0x101: v101 = EQ vfc(0x95d89b41), v34
    0x1842: v1842(0x188b) = CONST 
    0x1843: JUMPI v1842(0x188b), v101

    Begin block 0x188b
    prev=[0xfb], succ=[]
    =================================
    0x188c: v188c(0x413) = CONST 
    0x188d: CALLPRIVATE v188c(0x413)

    Begin block 0x106
    prev=[0xfb], succ=[0x188e, 0x111]
    =================================
    0x107: v107(0xa9059cbb) = CONST 
    0x10c: v10c = EQ v107(0xa9059cbb), v34
    0x1844: v1844(0x188e) = CONST 
    0x1845: JUMPI v1844(0x188e), v10c

    Begin block 0x188e
    prev=[0x106], succ=[]
    =================================
    0x188f: v188f(0x428) = CONST 
    0x1890: CALLPRIVATE v188f(0x428)

    Begin block 0x111
    prev=[0x106], succ=[0x1891, 0x11c]
    =================================
    0x112: v112(0xb719d032) = CONST 
    0x117: v117 = EQ v112(0xb719d032), v34
    0x1846: v1846(0x1891) = CONST 
    0x1847: JUMPI v1846(0x1891), v117

    Begin block 0x1891
    prev=[0x111], succ=[]
    =================================
    0x1892: v1892(0x44c) = CONST 
    0x1893: CALLPRIVATE v1892(0x44c)

    Begin block 0x11c
    prev=[0x111], succ=[0x1894, 0x127]
    =================================
    0x11d: v11d(0xc7178230) = CONST 
    0x122: v122 = EQ v11d(0xc7178230), v34
    0x1848: v1848(0x1894) = CONST 
    0x1849: JUMPI v1848(0x1894), v122

    Begin block 0x1894
    prev=[0x11c], succ=[]
    =================================
    0x1895: v1895(0x461) = CONST 
    0x1896: CALLPRIVATE v1895(0x461)

    Begin block 0x127
    prev=[0x11c], succ=[0x1897, 0x132]
    =================================
    0x128: v128(0xd73dd623) = CONST 
    0x12d: v12d = EQ v128(0xd73dd623), v34
    0x184a: v184a(0x1897) = CONST 
    0x184b: JUMPI v184a(0x1897), v12d

    Begin block 0x1897
    prev=[0x127], succ=[]
    =================================
    0x1898: v1898(0x476) = CONST 
    0x1899: CALLPRIVATE v1898(0x476)

    Begin block 0x132
    prev=[0x127], succ=[0x189a, 0x13d]
    =================================
    0x133: v133(0xdd62ed3e) = CONST 
    0x138: v138 = EQ v133(0xdd62ed3e), v34
    0x184c: v184c(0x189a) = CONST 
    0x184d: JUMPI v184c(0x189a), v138

    Begin block 0x189a
    prev=[0x132], succ=[]
    =================================
    0x189b: v189b(0x49a) = CONST 
    0x189c: CALLPRIVATE v189b(0x49a)

    Begin block 0x13d
    prev=[0x132], succ=[0x189d, 0x148]
    =================================
    0x13e: v13e(0xf2fde38b) = CONST 
    0x143: v143 = EQ v13e(0xf2fde38b), v34
    0x184e: v184e(0x189d) = CONST 
    0x184f: JUMPI v184e(0x189d), v143

    Begin block 0x189d
    prev=[0x13d], succ=[]
    =================================
    0x189e: v189e(0x4c1) = CONST 
    0x189f: CALLPRIVATE v189e(0x4c1)

    Begin block 0x148
    prev=[0x13d], succ=[0x1852, 0x18a0]
    =================================
    0x149: v149(0xf7ea7a3d) = CONST 
    0x14e: v14e = EQ v149(0xf7ea7a3d), v34
    0x1850: v1850(0x18a0) = CONST 
    0x1851: JUMPI v1850(0x18a0), v14e

    Begin block 0x1852
    prev=[0x0, 0x148], succ=[]
    =================================
    0x1853: v1853(0x153) = CONST 
    0x1854: CALLPRIVATE v1853(0x153)

    Begin block 0x18a0
    prev=[0x148], succ=[]
    =================================
    0x18a1: v18a1(0x4e2) = CONST 
    0x18a2: CALLPRIVATE v18a1(0x4e2)

    Begin block 0x1855
    prev=[0xd], succ=[]
    =================================
    0x1856: v1856(0x158) = CONST 
    0x1857: CALLPRIVATE v1856(0x158)

}

function fallback()() public {
    Begin block 0x153
    prev=[], succ=[]
    =================================
    0x154: v154(0x0) = CONST 
    0x157: REVERT v154(0x0), v154(0x0)

}

function name()() public {
    Begin block 0x158
    prev=[], succ=[0x160, 0x164]
    =================================
    0x159: v159 = CALLVALUE 
    0x15b: v15b = ISZERO v159
    0x15c: v15c(0x164) = CONST 
    0x15f: JUMPI v15c(0x164), v15b

    Begin block 0x160
    prev=[0x158], succ=[]
    =================================
    0x160: v160(0x0) = CONST 
    0x163: REVERT v160(0x0), v160(0x0)

    Begin block 0x164
    prev=[0x158], succ=[0x16d0x158]
    =================================
    0x166: v166(0x16d) = CONST 
    0x169: v169(0x4fa) = CONST 
    0x16c: v16c_0, v16c_1 = CALLPRIVATE v169(0x4fa), v166(0x16d)

    Begin block 0x16d0x158
    prev=[0x164], succ=[0x18f0x158]
    =================================
    0x16e0x158: v15816e(0x40) = CONST 
    0x1710x158: v158171 = MLOAD v15816e(0x40)
    0x1720x158: v158172(0x20) = CONST 
    0x1760x158: MSTORE v158171, v158172(0x20)
    0x1780x158: v158178 = MLOAD v16c_0
    0x17b0x158: v15817b = ADD v158171, v158172(0x20)
    0x17c0x158: MSTORE v15817b, v158178
    0x17e0x158: v15817e = MLOAD v16c_0
    0x1850x158: v158185 = ADD v158171, v15816e(0x40)
    0x1880x158: v158188 = ADD v16c_0, v158172(0x20)
    0x18d0x158: v15818d(0x0) = CONST 

    Begin block 0x18f0x158
    prev=[0x1980x158, 0x16d0x158], succ=[0x1a70x158, 0x1980x158]
    =================================
    0x18f0x158_0x0: v18f158_0 = PHI v1581a2, v15818d(0x0)
    0x1920x158: v158192 = LT v18f158_0, v15817e
    0x1930x158: v158193 = ISZERO v158192
    0x1940x158: v158194(0x1a7) = CONST 
    0x1970x158: JUMPI v158194(0x1a7), v158193

    Begin block 0x1a70x158
    prev=[0x18f0x158], succ=[0x1d40x158, 0x1bb0x158]
    =================================
    0x1b00x158: v1581b0 = ADD v15817e, v158185
    0x1b20x158: v1581b2(0x1f) = CONST 
    0x1b40x158: v1581b4 = AND v1581b2(0x1f), v15817e
    0x1b60x158: v1581b6 = ISZERO v1581b4
    0x1b70x158: v1581b7(0x1d4) = CONST 
    0x1ba0x158: JUMPI v1581b7(0x1d4), v1581b6

    Begin block 0x1d40x158
    prev=[0x1a70x158, 0x1bb0x158], succ=[]
    =================================
    0x1d40x158_0x1: v1d4158_1 = PHI v1581d1, v1581b0
    0x1da0x158: v1581da(0x40) = CONST 
    0x1dc0x158: v1581dc = MLOAD v1581da(0x40)
    0x1df0x158: v1581df = SUB v1d4158_1, v1581dc
    0x1e10x158: RETURN v1581dc, v1581df

    Begin block 0x1bb0x158
    prev=[0x1a70x158], succ=[0x1d40x158]
    =================================
    0x1bd0x158: v1581bd = SUB v1581b0, v1581b4
    0x1bf0x158: v1581bf = MLOAD v1581bd
    0x1c00x158: v1581c0(0x1) = CONST 
    0x1c30x158: v1581c3(0x20) = CONST 
    0x1c50x158: v1581c5 = SUB v1581c3(0x20), v1581b4
    0x1c60x158: v1581c6(0x100) = CONST 
    0x1c90x158: v1581c9 = EXP v1581c6(0x100), v1581c5
    0x1ca0x158: v1581ca = SUB v1581c9, v1581c0(0x1)
    0x1cb0x158: v1581cb = NOT v1581ca
    0x1cc0x158: v1581cc = AND v1581cb, v1581bf
    0x1ce0x158: MSTORE v1581bd, v1581cc
    0x1cf0x158: v1581cf(0x20) = CONST 
    0x1d10x158: v1581d1 = ADD v1581cf(0x20), v1581bd

    Begin block 0x1980x158
    prev=[0x18f0x158], succ=[0x18f0x158]
    =================================
    0x1980x158_0x0: v198158_0 = PHI v1581a2, v15818d(0x0)
    0x19a0x158: v15819a = ADD v198158_0, v158188
    0x19b0x158: v15819b = MLOAD v15819a
    0x19e0x158: v15819e = ADD v198158_0, v158185
    0x19f0x158: MSTORE v15819e, v15819b
    0x1a00x158: v1581a0(0x20) = CONST 
    0x1a20x158: v1581a2 = ADD v1581a0(0x20), v198158_0
    0x1a30x158: v1581a3(0x18f) = CONST 
    0x1a60x158: JUMP v1581a3(0x18f)

}

function approve(address,uint256)() public {
    Begin block 0x1e2
    prev=[], succ=[0x1ea, 0x1ee]
    =================================
    0x1e3: v1e3 = CALLVALUE 
    0x1e5: v1e5 = ISZERO v1e3
    0x1e6: v1e6(0x1ee) = CONST 
    0x1e9: JUMPI v1e6(0x1ee), v1e5

    Begin block 0x1ea
    prev=[0x1e2], succ=[]
    =================================
    0x1ea: v1ea(0x0) = CONST 
    0x1ed: REVERT v1ea(0x0), v1ea(0x0)

    Begin block 0x1ee
    prev=[0x1e2], succ=[0x588B0x1ee]
    =================================
    0x1f0: v1f0(0x135b) = CONST 
    0x1f3: v1f3(0x1) = CONST 
    0x1f5: v1f5(0xa0) = CONST 
    0x1f7: v1f7(0x2) = CONST 
    0x1f9: v1f9(0x10000000000000000000000000000000000000000) = EXP v1f7(0x2), v1f5(0xa0)
    0x1fa: v1fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f9(0x10000000000000000000000000000000000000000), v1f3(0x1)
    0x1fb: v1fb(0x4) = CONST 
    0x1fd: v1fd = CALLDATALOAD v1fb(0x4)
    0x1fe: v1fe = AND v1fd, v1fa(0xffffffffffffffffffffffffffffffffffffffff)
    0x1ff: v1ff(0x24) = CONST 
    0x201: v201 = CALLDATALOAD v1ff(0x24)
    0x202: v202(0x588) = CONST 
    0x205: JUMP v202(0x588)

    Begin block 0x588B0x1ee
    prev=[0x1ee], succ=[0x5adB0x1ee, 0x59fB0x1ee]
    =================================
    0x589S0x1ee: v589V1ee(0x2) = CONST 
    0x58bS0x1ee: v58bV1ee = SLOAD v589V1ee(0x2)
    0x58cS0x1ee: v58cV1ee(0x0) = CONST 
    0x58fS0x1ee: v58fV1ee(0x1) = CONST 
    0x591S0x1ee: v591V1ee(0xa0) = CONST 
    0x593S0x1ee: v593V1ee(0x2) = CONST 
    0x595S0x1ee: v595V1ee(0x10000000000000000000000000000000000000000) = EXP v593V1ee(0x2), v591V1ee(0xa0)
    0x596S0x1ee: v596V1ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v595V1ee(0x10000000000000000000000000000000000000000), v58fV1ee(0x1)
    0x597S0x1ee: v597V1ee = AND v596V1ee(0xffffffffffffffffffffffffffffffffffffffff), v58bV1ee
    0x598S0x1ee: v598V1ee = CALLER 
    0x599S0x1ee: v599V1ee = EQ v598V1ee, v597V1ee
    0x59bS0x1ee: v59bV1ee(0x5ad) = CONST 
    0x59eS0x1ee: JUMPI v59bV1ee(0x5ad), v599V1ee

    Begin block 0x5adB0x1ee
    prev=[0x588B0x1ee, 0x59fB0x1ee], succ=[0x5b4B0x1ee, 0x5b8B0x1ee]
    =================================
    0x5ad_0x0S0x1ee: v5ad_0V1ee = PHI v599V1ee, v5acV1ee
    0x5aeS0x1ee: v5aeV1ee = ISZERO v5ad_0V1ee
    0x5afS0x1ee: v5afV1ee = ISZERO v5aeV1ee
    0x5b0S0x1ee: v5b0V1ee(0x5b8) = CONST 
    0x5b3S0x1ee: JUMPI v5b0V1ee(0x5b8), v5afV1ee

    Begin block 0x5b4B0x1ee
    prev=[0x5adB0x1ee], succ=[]
    =================================
    0x5b4S0x1ee: v5b4V1ee(0x0) = CONST 
    0x5b7S0x1ee: REVERT v5b4V1ee(0x0), v5b4V1ee(0x0)

    Begin block 0x5b8B0x1ee
    prev=[0x5adB0x1ee], succ=[0x5c9B0x1ee, 0x5cdB0x1ee]
    =================================
    0x5b9S0x1ee: v5b9V1ee(0x6) = CONST 
    0x5bbS0x1ee: v5bbV1ee = SLOAD v5b9V1ee(0x6)
    0x5bcS0x1ee: v5bcV1ee(0x100) = CONST 
    0x5c0S0x1ee: v5c0V1ee = DIV v5bbV1ee, v5bcV1ee(0x100)
    0x5c1S0x1ee: v5c1V1ee(0xff) = CONST 
    0x5c3S0x1ee: v5c3V1ee = AND v5c1V1ee(0xff), v5c0V1ee
    0x5c4S0x1ee: v5c4V1ee = ISZERO v5c3V1ee
    0x5c5S0x1ee: v5c5V1ee(0x5cd) = CONST 
    0x5c8S0x1ee: JUMPI v5c5V1ee(0x5cd), v5c4V1ee

    Begin block 0x5c9B0x1ee
    prev=[0x5b8B0x1ee], succ=[]
    =================================
    0x5c9S0x1ee: v5c9V1ee(0x0) = CONST 
    0x5ccS0x1ee: REVERT v5c9V1ee(0x0), v5c9V1ee(0x0)

    Begin block 0x5cdB0x1ee
    prev=[0x5b8B0x1ee], succ=[0x654B0x1ee, 0x6580x588B0x1ee]
    =================================
    0x5ceS0x1ee: v5ceV1ee(0x6) = CONST 
    0x5d0S0x1ee: v5d0V1ee = SLOAD v5ceV1ee(0x6)
    0x5d1S0x1ee: v5d1V1ee(0x40) = CONST 
    0x5d4S0x1ee: v5d4V1ee = MLOAD v5d1V1ee(0x40)
    0x5d5S0x1ee: v5d5V1ee(0xe1f21c6700000000000000000000000000000000000000000000000000000000) = CONST 
    0x5f7S0x1ee: MSTORE v5d4V1ee, v5d5V1ee(0xe1f21c6700000000000000000000000000000000000000000000000000000000)
    0x5f8S0x1ee: v5f8V1ee(0x1) = CONST 
    0x5faS0x1ee: v5faV1ee(0xa0) = CONST 
    0x5fcS0x1ee: v5fcV1ee(0x2) = CONST 
    0x5feS0x1ee: v5feV1ee(0x10000000000000000000000000000000000000000) = EXP v5fcV1ee(0x2), v5faV1ee(0xa0)
    0x5ffS0x1ee: v5ffV1ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5feV1ee(0x10000000000000000000000000000000000000000), v5f8V1ee(0x1)
    0x600S0x1ee: v600V1ee(0x10000) = CONST 
    0x606S0x1ee: v606V1ee = DIV v5d0V1ee, v600V1ee(0x10000)
    0x608S0x1ee: v608V1ee = AND v5ffV1ee(0xffffffffffffffffffffffffffffffffffffffff), v606V1ee
    0x609S0x1ee: v609V1ee(0x4) = CONST 
    0x60cS0x1ee: v60cV1ee = ADD v5d4V1ee, v609V1ee(0x4)
    0x60dS0x1ee: MSTORE v60cV1ee, v608V1ee
    0x610S0x1ee: v610V1ee = AND v1fe, v5ffV1ee(0xffffffffffffffffffffffffffffffffffffffff)
    0x611S0x1ee: v611V1ee(0x24) = CONST 
    0x614S0x1ee: v614V1ee = ADD v5d4V1ee, v611V1ee(0x24)
    0x615S0x1ee: MSTORE v614V1ee, v610V1ee
    0x616S0x1ee: v616V1ee(0x44) = CONST 
    0x619S0x1ee: v619V1ee = ADD v5d4V1ee, v616V1ee(0x44)
    0x61cS0x1ee: MSTORE v619V1ee, v201
    0x61dS0x1ee: v61dV1ee = MLOAD v5d1V1ee(0x40)
    0x61eS0x1ee: v61eV1ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x634S0x1ee: v634V1ee(0xe1f21c67) = CONST 
    0x63aS0x1ee: v63aV1ee(0x64) = CONST 
    0x63eS0x1ee: v63eV1ee = ADD v5d4V1ee, v63aV1ee(0x64)
    0x640S0x1ee: v640V1ee(0x20) = CONST 
    0x647S0x1ee: v647V1ee(0x0) = SUB v5d4V1ee, v61dV1ee
    0x648S0x1ee: v648V1ee(0x64) = ADD v647V1ee(0x0), v63aV1ee(0x64)
    0x64cS0x1ee: v64cV1ee = EXTCODESIZE v61eV1ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x64dS0x1ee: v64dV1ee = ISZERO v64cV1ee
    0x64fS0x1ee: v64fV1ee = ISZERO v64dV1ee
    0x650S0x1ee: v650V1ee(0x658) = CONST 
    0x653S0x1ee: JUMPI v650V1ee(0x658), v64fV1ee

    Begin block 0x654B0x1ee
    prev=[0x5cdB0x1ee], succ=[]
    =================================
    0x654S0x1ee: v654V1ee(0x0) = CONST 
    0x657S0x1ee: REVERT v654V1ee(0x0), v654V1ee(0x0)

    Begin block 0x6580x588B0x1ee
    prev=[0x5cdB0x1ee], succ=[0x6630x588B0x1ee, 0x66c0x588B0x1ee]
    =================================
    0x65a0x588S0x1ee: v58865aV1ee = GAS 
    0x65b0x588S0x1ee: v58865bV1ee = DELEGATECALL v58865aV1ee, v61eV1ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v61dV1ee, v648V1ee(0x64), v61dV1ee, v640V1ee(0x20)
    0x65c0x588S0x1ee: v58865cV1ee = ISZERO v58865bV1ee
    0x65e0x588S0x1ee: v58865eV1ee = ISZERO v58865cV1ee
    0x65f0x588S0x1ee: v58865fV1ee(0x66c) = CONST 
    0x6620x588S0x1ee: JUMPI v58865fV1ee(0x66c), v58865eV1ee

    Begin block 0x6630x588B0x1ee
    prev=[0x6580x588B0x1ee], succ=[]
    =================================
    0x6630x588S0x1ee: v588663V1ee = RETURNDATASIZE 
    0x6640x588S0x1ee: v588664V1ee(0x0) = CONST 
    0x6670x588S0x1ee: RETURNDATACOPY v588664V1ee(0x0), v588664V1ee(0x0), v588663V1ee
    0x6680x588S0x1ee: v588668V1ee = RETURNDATASIZE 
    0x6690x588S0x1ee: v588669V1ee(0x0) = CONST 
    0x66b0x588S0x1ee: REVERT v588669V1ee(0x0), v588668V1ee

    Begin block 0x66c0x588B0x1ee
    prev=[0x6580x588B0x1ee], succ=[0x67e0x588B0x1ee, 0x6820x588B0x1ee]
    =================================
    0x6710x588S0x1ee: v588671V1ee(0x40) = CONST 
    0x6730x588S0x1ee: v588673V1ee = MLOAD v588671V1ee(0x40)
    0x6740x588S0x1ee: v588674V1ee = RETURNDATASIZE 
    0x6750x588S0x1ee: v588675V1ee(0x20) = CONST 
    0x6780x588S0x1ee: v588678V1ee = LT v588674V1ee, v588675V1ee(0x20)
    0x6790x588S0x1ee: v588679V1ee = ISZERO v588678V1ee
    0x67a0x588S0x1ee: v58867aV1ee(0x682) = CONST 
    0x67d0x588S0x1ee: JUMPI v58867aV1ee(0x682), v588679V1ee

    Begin block 0x67e0x588B0x1ee
    prev=[0x66c0x588B0x1ee], succ=[]
    =================================
    0x67e0x588S0x1ee: v58867eV1ee(0x0) = CONST 
    0x6810x588S0x1ee: REVERT v58867eV1ee(0x0), v58867eV1ee(0x0)

    Begin block 0x6820x588B0x1ee
    prev=[0x66c0x588B0x1ee], succ=[0x135b]
    =================================
    0x6840x588S0x1ee: v588684V1ee = MLOAD v588673V1ee
    0x68a0x588S0x1ee: JUMP v1f0(0x135b)

    Begin block 0x135b
    prev=[0x6820x588B0x1ee], succ=[]
    =================================
    0x135c: v135c(0x40) = CONST 
    0x135f: v135f = MLOAD v135c(0x40)
    0x1361: v1361 = ISZERO v588684V1ee
    0x1362: v1362 = ISZERO v1361
    0x1364: MSTORE v135f, v1362
    0x1365: v1365 = MLOAD v135c(0x40)
    0x1369: v1369(0x0) = SUB v135f, v1365
    0x136a: v136a(0x20) = CONST 
    0x136c: v136c(0x20) = ADD v136a(0x20), v1369(0x0)
    0x136e: RETURN v1365, v136c(0x20)

    Begin block 0x59fB0x1ee
    prev=[0x588B0x1ee], succ=[0x5adB0x1ee]
    =================================
    0x5a0S0x1ee: v5a0V1ee(0x2) = CONST 
    0x5a2S0x1ee: v5a2V1ee = SLOAD v5a0V1ee(0x2)
    0x5a3S0x1ee: v5a3V1ee(0x1) = CONST 
    0x5a5S0x1ee: v5a5V1ee(0xa0) = CONST 
    0x5a7S0x1ee: v5a7V1ee(0x2) = CONST 
    0x5a9S0x1ee: v5a9V1ee(0x10000000000000000000000000000000000000000) = EXP v5a7V1ee(0x2), v5a5V1ee(0xa0)
    0x5aaS0x1ee: v5aaV1ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5a9V1ee(0x10000000000000000000000000000000000000000), v5a3V1ee(0x1)
    0x5abS0x1ee: v5abV1ee = AND v5aaV1ee(0xffffffffffffffffffffffffffffffffffffffff), v5a2V1ee
    0x5acS0x1ee: v5acV1ee = ISZERO v5abV1ee

}

function totalSupply()() public {
    Begin block 0x21a
    prev=[], succ=[0x222, 0x226]
    =================================
    0x21b: v21b = CALLVALUE 
    0x21d: v21d = ISZERO v21b
    0x21e: v21e(0x226) = CONST 
    0x221: JUMPI v21e(0x226), v21d

    Begin block 0x222
    prev=[0x21a], succ=[]
    =================================
    0x222: v222(0x0) = CONST 
    0x225: REVERT v222(0x0), v222(0x0)

    Begin block 0x226
    prev=[0x21a], succ=[0x68b]
    =================================
    0x228: v228(0x138e) = CONST 
    0x22b: v22b(0x68b) = CONST 
    0x22e: JUMP v22b(0x68b)

    Begin block 0x68b
    prev=[0x226], succ=[0x706, 0x70a]
    =================================
    0x68c: v68c(0x6) = CONST 
    0x68e: v68e = SLOAD v68c(0x6)
    0x68f: v68f(0x40) = CONST 
    0x692: v692 = MLOAD v68f(0x40)
    0x693: v693(0xe4dc2aa400000000000000000000000000000000000000000000000000000000) = CONST 
    0x6b5: MSTORE v692, v693(0xe4dc2aa400000000000000000000000000000000000000000000000000000000)
    0x6b6: v6b6(0x10000) = CONST 
    0x6bc: v6bc = DIV v68e, v6b6(0x10000)
    0x6bd: v6bd(0x1) = CONST 
    0x6bf: v6bf(0xa0) = CONST 
    0x6c1: v6c1(0x2) = CONST 
    0x6c3: v6c3(0x10000000000000000000000000000000000000000) = EXP v6c1(0x2), v6bf(0xa0)
    0x6c4: v6c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c3(0x10000000000000000000000000000000000000000), v6bd(0x1)
    0x6c5: v6c5 = AND v6c4(0xffffffffffffffffffffffffffffffffffffffff), v6bc
    0x6c6: v6c6(0x4) = CONST 
    0x6c9: v6c9 = ADD v692, v6c6(0x4)
    0x6ca: MSTORE v6c9, v6c5
    0x6cb: v6cb = MLOAD v68f(0x40)
    0x6cc: v6cc(0x0) = CONST 
    0x6cf: v6cf(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x6e5: v6e5(0xe4dc2aa4) = CONST 
    0x6eb: v6eb(0x24) = CONST 
    0x6ef: v6ef = ADD v692, v6eb(0x24)
    0x6f1: v6f1(0x20) = CONST 
    0x6f9: v6f9(0x0) = SUB v692, v6cb
    0x6fa: v6fa(0x24) = ADD v6f9(0x0), v6eb(0x24)
    0x6fe: v6fe = EXTCODESIZE v6cf(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x6ff: v6ff = ISZERO v6fe
    0x701: v701 = ISZERO v6ff
    0x702: v702(0x70a) = CONST 
    0x705: JUMPI v702(0x70a), v701

    Begin block 0x706
    prev=[0x68b], succ=[]
    =================================
    0x706: v706(0x0) = CONST 
    0x709: REVERT v706(0x0), v706(0x0)

    Begin block 0x70a
    prev=[0x68b], succ=[0x715, 0x71e]
    =================================
    0x70c: v70c = GAS 
    0x70d: v70d = DELEGATECALL v70c, v6cf(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v6cb, v6fa(0x24), v6cb, v6f1(0x20)
    0x70e: v70e = ISZERO v70d
    0x710: v710 = ISZERO v70e
    0x711: v711(0x71e) = CONST 
    0x714: JUMPI v711(0x71e), v710

    Begin block 0x715
    prev=[0x70a], succ=[]
    =================================
    0x715: v715 = RETURNDATASIZE 
    0x716: v716(0x0) = CONST 
    0x719: RETURNDATACOPY v716(0x0), v716(0x0), v715
    0x71a: v71a = RETURNDATASIZE 
    0x71b: v71b(0x0) = CONST 
    0x71d: REVERT v71b(0x0), v71a

    Begin block 0x71e
    prev=[0x70a], succ=[0x730, 0x734]
    =================================
    0x723: v723(0x40) = CONST 
    0x725: v725 = MLOAD v723(0x40)
    0x726: v726 = RETURNDATASIZE 
    0x727: v727(0x20) = CONST 
    0x72a: v72a = LT v726, v727(0x20)
    0x72b: v72b = ISZERO v72a
    0x72c: v72c(0x734) = CONST 
    0x72f: JUMPI v72c(0x734), v72b

    Begin block 0x730
    prev=[0x71e], succ=[]
    =================================
    0x730: v730(0x0) = CONST 
    0x733: REVERT v730(0x0), v730(0x0)

    Begin block 0x734
    prev=[0x71e], succ=[0x138e]
    =================================
    0x736: v736 = MLOAD v725
    0x73a: JUMP v228(0x138e)

    Begin block 0x138e
    prev=[0x734], succ=[]
    =================================
    0x138f: v138f(0x40) = CONST 
    0x1392: v1392 = MLOAD v138f(0x40)
    0x1395: MSTORE v1392, v736
    0x1396: v1396 = MLOAD v138f(0x40)
    0x139a: v139a(0x0) = SUB v1392, v1396
    0x139b: v139b(0x20) = CONST 
    0x139d: v139d(0x20) = ADD v139b(0x20), v139a(0x0)
    0x139f: RETURN v1396, v139d(0x20)

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x241
    prev=[], succ=[0x249, 0x24d]
    =================================
    0x242: v242 = CALLVALUE 
    0x244: v244 = ISZERO v242
    0x245: v245(0x24d) = CONST 
    0x248: JUMPI v245(0x24d), v244

    Begin block 0x249
    prev=[0x241], succ=[]
    =================================
    0x249: v249(0x0) = CONST 
    0x24c: REVERT v249(0x0), v249(0x0)

    Begin block 0x24d
    prev=[0x241], succ=[0x73b]
    =================================
    0x24f: v24f(0x13bf) = CONST 
    0x252: v252(0x1) = CONST 
    0x254: v254(0xa0) = CONST 
    0x256: v256(0x2) = CONST 
    0x258: v258(0x10000000000000000000000000000000000000000) = EXP v256(0x2), v254(0xa0)
    0x259: v259(0xffffffffffffffffffffffffffffffffffffffff) = SUB v258(0x10000000000000000000000000000000000000000), v252(0x1)
    0x25a: v25a(0x4) = CONST 
    0x25c: v25c = CALLDATALOAD v25a(0x4)
    0x25e: v25e = AND v259(0xffffffffffffffffffffffffffffffffffffffff), v25c
    0x260: v260(0x24) = CONST 
    0x262: v262 = CALLDATALOAD v260(0x24)
    0x263: v263 = AND v262, v259(0xffffffffffffffffffffffffffffffffffffffff)
    0x264: v264(0x44) = CONST 
    0x266: v266 = CALLDATALOAD v264(0x44)
    0x267: v267(0x73b) = CONST 
    0x26a: JUMP v267(0x73b)

    Begin block 0x73b
    prev=[0x24d], succ=[0x760, 0x752]
    =================================
    0x73c: v73c(0x2) = CONST 
    0x73e: v73e = SLOAD v73c(0x2)
    0x73f: v73f(0x0) = CONST 
    0x742: v742(0x1) = CONST 
    0x744: v744(0xa0) = CONST 
    0x746: v746(0x2) = CONST 
    0x748: v748(0x10000000000000000000000000000000000000000) = EXP v746(0x2), v744(0xa0)
    0x749: v749(0xffffffffffffffffffffffffffffffffffffffff) = SUB v748(0x10000000000000000000000000000000000000000), v742(0x1)
    0x74a: v74a = AND v749(0xffffffffffffffffffffffffffffffffffffffff), v73e
    0x74b: v74b = CALLER 
    0x74c: v74c = EQ v74b, v74a
    0x74e: v74e(0x760) = CONST 
    0x751: JUMPI v74e(0x760), v74c

    Begin block 0x760
    prev=[0x73b, 0x752], succ=[0x767, 0x76b]
    =================================
    0x760_0x0: v760_0 = PHI v74c, v75f
    0x761: v761 = ISZERO v760_0
    0x762: v762 = ISZERO v761
    0x763: v763(0x76b) = CONST 
    0x766: JUMPI v763(0x76b), v762

    Begin block 0x767
    prev=[0x760], succ=[]
    =================================
    0x767: v767(0x0) = CONST 
    0x76a: REVERT v767(0x0), v767(0x0)

    Begin block 0x76b
    prev=[0x760], succ=[0x77c, 0x780]
    =================================
    0x76c: v76c(0x6) = CONST 
    0x76e: v76e = SLOAD v76c(0x6)
    0x76f: v76f(0x100) = CONST 
    0x773: v773 = DIV v76e, v76f(0x100)
    0x774: v774(0xff) = CONST 
    0x776: v776 = AND v774(0xff), v773
    0x777: v777 = ISZERO v776
    0x778: v778(0x780) = CONST 
    0x77b: JUMPI v778(0x780), v777

    Begin block 0x77c
    prev=[0x76b], succ=[]
    =================================
    0x77c: v77c(0x0) = CONST 
    0x77f: REVERT v77c(0x0), v77c(0x0)

    Begin block 0x780
    prev=[0x76b], succ=[0x80f, 0x813]
    =================================
    0x781: v781(0x6) = CONST 
    0x783: v783 = SLOAD v781(0x6)
    0x784: v784(0x40) = CONST 
    0x787: v787 = MLOAD v784(0x40)
    0x788: v788(0x15dacbea00000000000000000000000000000000000000000000000000000000) = CONST 
    0x7aa: MSTORE v787, v788(0x15dacbea00000000000000000000000000000000000000000000000000000000)
    0x7ab: v7ab(0x1) = CONST 
    0x7ad: v7ad(0xa0) = CONST 
    0x7af: v7af(0x2) = CONST 
    0x7b1: v7b1(0x10000000000000000000000000000000000000000) = EXP v7af(0x2), v7ad(0xa0)
    0x7b2: v7b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b1(0x10000000000000000000000000000000000000000), v7ab(0x1)
    0x7b3: v7b3(0x10000) = CONST 
    0x7b9: v7b9 = DIV v783, v7b3(0x10000)
    0x7bb: v7bb = AND v7b2(0xffffffffffffffffffffffffffffffffffffffff), v7b9
    0x7bc: v7bc(0x4) = CONST 
    0x7bf: v7bf = ADD v787, v7bc(0x4)
    0x7c0: MSTORE v7bf, v7bb
    0x7c3: v7c3 = AND v7b2(0xffffffffffffffffffffffffffffffffffffffff), v25e
    0x7c4: v7c4(0x24) = CONST 
    0x7c7: v7c7 = ADD v787, v7c4(0x24)
    0x7c8: MSTORE v7c7, v7c3
    0x7cb: v7cb = AND v263, v7b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x7cc: v7cc(0x44) = CONST 
    0x7cf: v7cf = ADD v787, v7cc(0x44)
    0x7d0: MSTORE v7cf, v7cb
    0x7d1: v7d1(0x64) = CONST 
    0x7d4: v7d4 = ADD v787, v7d1(0x64)
    0x7d7: MSTORE v7d4, v266
    0x7d8: v7d8 = MLOAD v784(0x40)
    0x7d9: v7d9(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x7ef: v7ef(0x15dacbea) = CONST 
    0x7f5: v7f5(0x84) = CONST 
    0x7f9: v7f9 = ADD v787, v7f5(0x84)
    0x7fb: v7fb(0x20) = CONST 
    0x802: v802(0x0) = SUB v787, v7d8
    0x803: v803(0x84) = ADD v802(0x0), v7f5(0x84)
    0x807: v807 = EXTCODESIZE v7d9(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x808: v808 = ISZERO v807
    0x80a: v80a = ISZERO v808
    0x80b: v80b(0x813) = CONST 
    0x80e: JUMPI v80b(0x813), v80a

    Begin block 0x80f
    prev=[0x780], succ=[]
    =================================
    0x80f: v80f(0x0) = CONST 
    0x812: REVERT v80f(0x0), v80f(0x0)

    Begin block 0x813
    prev=[0x780], succ=[0x81e, 0x827]
    =================================
    0x815: v815 = GAS 
    0x816: v816 = DELEGATECALL v815, v7d9(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v7d8, v803(0x84), v7d8, v7fb(0x20)
    0x817: v817 = ISZERO v816
    0x819: v819 = ISZERO v817
    0x81a: v81a(0x827) = CONST 
    0x81d: JUMPI v81a(0x827), v819

    Begin block 0x81e
    prev=[0x813], succ=[]
    =================================
    0x81e: v81e = RETURNDATASIZE 
    0x81f: v81f(0x0) = CONST 
    0x822: RETURNDATACOPY v81f(0x0), v81f(0x0), v81e
    0x823: v823 = RETURNDATASIZE 
    0x824: v824(0x0) = CONST 
    0x826: REVERT v824(0x0), v823

    Begin block 0x827
    prev=[0x813], succ=[0x839, 0x83d]
    =================================
    0x82c: v82c(0x40) = CONST 
    0x82e: v82e = MLOAD v82c(0x40)
    0x82f: v82f = RETURNDATASIZE 
    0x830: v830(0x20) = CONST 
    0x833: v833 = LT v82f, v830(0x20)
    0x834: v834 = ISZERO v833
    0x835: v835(0x83d) = CONST 
    0x838: JUMPI v835(0x83d), v834

    Begin block 0x839
    prev=[0x827], succ=[]
    =================================
    0x839: v839(0x0) = CONST 
    0x83c: REVERT v839(0x0), v839(0x0)

    Begin block 0x83d
    prev=[0x827], succ=[0x13bf]
    =================================
    0x83f: v83f = MLOAD v82e
    0x846: JUMP v24f(0x13bf)

    Begin block 0x13bf
    prev=[0x83d], succ=[]
    =================================
    0x13c0: v13c0(0x40) = CONST 
    0x13c3: v13c3 = MLOAD v13c0(0x40)
    0x13c5: v13c5 = ISZERO v83f
    0x13c6: v13c6 = ISZERO v13c5
    0x13c8: MSTORE v13c3, v13c6
    0x13c9: v13c9 = MLOAD v13c0(0x40)
    0x13cd: v13cd(0x0) = SUB v13c3, v13c9
    0x13ce: v13ce(0x20) = CONST 
    0x13d0: v13d0(0x20) = ADD v13ce(0x20), v13cd(0x0)
    0x13d2: RETURN v13c9, v13d0(0x20)

    Begin block 0x752
    prev=[0x73b], succ=[0x760]
    =================================
    0x753: v753(0x2) = CONST 
    0x755: v755 = SLOAD v753(0x2)
    0x756: v756(0x1) = CONST 
    0x758: v758(0xa0) = CONST 
    0x75a: v75a(0x2) = CONST 
    0x75c: v75c(0x10000000000000000000000000000000000000000) = EXP v75a(0x2), v758(0xa0)
    0x75d: v75d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75c(0x10000000000000000000000000000000000000000), v756(0x1)
    0x75e: v75e = AND v75d(0xffffffffffffffffffffffffffffffffffffffff), v755
    0x75f: v75f = ISZERO v75e

}

function decimals()() public {
    Begin block 0x26b
    prev=[], succ=[0x273, 0x277]
    =================================
    0x26c: v26c = CALLVALUE 
    0x26e: v26e = ISZERO v26c
    0x26f: v26f(0x277) = CONST 
    0x272: JUMPI v26f(0x277), v26e

    Begin block 0x273
    prev=[0x26b], succ=[]
    =================================
    0x273: v273(0x0) = CONST 
    0x276: REVERT v273(0x0), v273(0x0)

    Begin block 0x277
    prev=[0x26b], succ=[0x847]
    =================================
    0x279: v279(0x280) = CONST 
    0x27c: v27c(0x847) = CONST 
    0x27f: JUMP v27c(0x847)

    Begin block 0x847
    prev=[0x277], succ=[0x280]
    =================================
    0x848: v848(0x6) = CONST 
    0x84a: v84a = SLOAD v848(0x6)
    0x84b: v84b(0xff) = CONST 
    0x84d: v84d = AND v84b(0xff), v84a
    0x84f: JUMP v279(0x280)

    Begin block 0x280
    prev=[0x847], succ=[]
    =================================
    0x281: v281(0x40) = CONST 
    0x284: v284 = MLOAD v281(0x40)
    0x285: v285(0xff) = CONST 
    0x289: v289 = AND v84d, v285(0xff)
    0x28b: MSTORE v284, v289
    0x28c: v28c = MLOAD v281(0x40)
    0x290: v290(0x0) = SUB v284, v28c
    0x291: v291(0x20) = CONST 
    0x293: v293(0x20) = ADD v291(0x20), v290(0x0)
    0x295: RETURN v28c, v293(0x20)

}

function upgradeTo(address)() public {
    Begin block 0x296
    prev=[], succ=[0x29e, 0x2a2]
    =================================
    0x297: v297 = CALLVALUE 
    0x299: v299 = ISZERO v297
    0x29a: v29a(0x2a2) = CONST 
    0x29d: JUMPI v29a(0x2a2), v299

    Begin block 0x29e
    prev=[0x296], succ=[]
    =================================
    0x29e: v29e(0x0) = CONST 
    0x2a1: REVERT v29e(0x0), v29e(0x0)

    Begin block 0x2a2
    prev=[0x296], succ=[0x850]
    =================================
    0x2a4: v2a4(0x13f2) = CONST 
    0x2a7: v2a7(0x1) = CONST 
    0x2a9: v2a9(0xa0) = CONST 
    0x2ab: v2ab(0x2) = CONST 
    0x2ad: v2ad(0x10000000000000000000000000000000000000000) = EXP v2ab(0x2), v2a9(0xa0)
    0x2ae: v2ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2ad(0x10000000000000000000000000000000000000000), v2a7(0x1)
    0x2af: v2af(0x4) = CONST 
    0x2b1: v2b1 = CALLDATALOAD v2af(0x4)
    0x2b2: v2b2 = AND v2b1, v2ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x2b3: v2b3(0x850) = CONST 
    0x2b6: JUMP v2b3(0x850)

    Begin block 0x850
    prev=[0x2a2], succ=[0x866, 0x86a]
    =================================
    0x851: v851(0x0) = CONST 
    0x854: v854 = SLOAD v851(0x0)
    0x857: v857(0x1) = CONST 
    0x859: v859(0xa0) = CONST 
    0x85b: v85b(0x2) = CONST 
    0x85d: v85d(0x10000000000000000000000000000000000000000) = EXP v85b(0x2), v859(0xa0)
    0x85e: v85e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v85d(0x10000000000000000000000000000000000000000), v857(0x1)
    0x85f: v85f = AND v85e(0xffffffffffffffffffffffffffffffffffffffff), v854
    0x860: v860 = CALLER 
    0x861: v861 = EQ v860, v85f
    0x862: v862(0x86a) = CONST 
    0x865: JUMPI v862(0x86a), v861

    Begin block 0x866
    prev=[0x850], succ=[]
    =================================
    0x866: v866(0x0) = CONST 
    0x869: REVERT v866(0x0), v866(0x0)

    Begin block 0x86a
    prev=[0x850], succ=[0x88c, 0x87e]
    =================================
    0x86b: v86b(0x2) = CONST 
    0x86d: v86d = SLOAD v86b(0x2)
    0x86e: v86e(0x1) = CONST 
    0x870: v870(0xa0) = CONST 
    0x872: v872(0x2) = CONST 
    0x874: v874(0x10000000000000000000000000000000000000000) = EXP v872(0x2), v870(0xa0)
    0x875: v875(0xffffffffffffffffffffffffffffffffffffffff) = SUB v874(0x10000000000000000000000000000000000000000), v86e(0x1)
    0x876: v876 = AND v875(0xffffffffffffffffffffffffffffffffffffffff), v86d
    0x877: v877 = CALLER 
    0x878: v878 = EQ v877, v876
    0x87a: v87a(0x88c) = CONST 
    0x87d: JUMPI v87a(0x88c), v878

    Begin block 0x88c
    prev=[0x86a, 0x87e], succ=[0x893, 0x897]
    =================================
    0x88c_0x0: v88c_0 = PHI v878, v88b
    0x88d: v88d = ISZERO v88c_0
    0x88e: v88e = ISZERO v88d
    0x88f: v88f(0x897) = CONST 
    0x892: JUMPI v88f(0x897), v88e

    Begin block 0x893
    prev=[0x88c], succ=[]
    =================================
    0x893: v893(0x0) = CONST 
    0x896: REVERT v893(0x0), v893(0x0)

    Begin block 0x897
    prev=[0x88c], succ=[0x8a8, 0x8ac]
    =================================
    0x898: v898(0x1) = CONST 
    0x89a: v89a(0xa0) = CONST 
    0x89c: v89c(0x2) = CONST 
    0x89e: v89e(0x10000000000000000000000000000000000000000) = EXP v89c(0x2), v89a(0xa0)
    0x89f: v89f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v89e(0x10000000000000000000000000000000000000000), v898(0x1)
    0x8a1: v8a1 = AND v2b2, v89f(0xffffffffffffffffffffffffffffffffffffffff)
    0x8a2: v8a2 = ISZERO v8a1
    0x8a3: v8a3 = ISZERO v8a2
    0x8a4: v8a4(0x8ac) = CONST 
    0x8a7: JUMPI v8a4(0x8ac), v8a3

    Begin block 0x8a8
    prev=[0x897], succ=[]
    =================================
    0x8a8: v8a8(0x0) = CONST 
    0x8ab: REVERT v8a8(0x0), v8a8(0x0)

    Begin block 0x8ac
    prev=[0x897], succ=[0x8b5]
    =================================
    0x8ad: v8ad(0x8b5) = CONST 
    0x8b0: v8b0 = ADDRESS 
    0x8b1: v8b1(0xce6) = CONST 
    0x8b4: v8b4_0 = CALLPRIVATE v8b1(0xce6), v8b0, v8ad(0x8b5)

    Begin block 0x8b5
    prev=[0x8ac], succ=[0x8c1, 0x955]
    =================================
    0x8b8: v8b8(0x0) = CONST 
    0x8bb: v8bb = GT v8b4_0, v8b8(0x0)
    0x8bc: v8bc = ISZERO v8bb
    0x8bd: v8bd(0x955) = CONST 
    0x8c0: JUMPI v8bd(0x955), v8bc

    Begin block 0x8c1
    prev=[0x8b5], succ=[0x924, 0x928]
    =================================
    0x8c1: v8c1(0x40) = CONST 
    0x8c4: v8c4 = MLOAD v8c1(0x40)
    0x8c5: v8c5(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = CONST 
    0x8e7: MSTORE v8c4, v8c5(0xa9059cbb00000000000000000000000000000000000000000000000000000000)
    0x8e8: v8e8(0x1) = CONST 
    0x8ea: v8ea(0xa0) = CONST 
    0x8ec: v8ec(0x2) = CONST 
    0x8ee: v8ee(0x10000000000000000000000000000000000000000) = EXP v8ec(0x2), v8ea(0xa0)
    0x8ef: v8ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8ee(0x10000000000000000000000000000000000000000), v8e8(0x1)
    0x8f1: v8f1 = AND v2b2, v8ef(0xffffffffffffffffffffffffffffffffffffffff)
    0x8f2: v8f2(0x4) = CONST 
    0x8f5: v8f5 = ADD v8c4, v8f2(0x4)
    0x8f6: MSTORE v8f5, v8f1
    0x8f7: v8f7(0x24) = CONST 
    0x8fa: v8fa = ADD v8c4, v8f7(0x24)
    0x8fd: MSTORE v8fa, v8b4_0
    0x8ff: v8ff = MLOAD v8c1(0x40)
    0x900: v900 = ADDRESS 
    0x902: v902(0xa9059cbb) = CONST 
    0x908: v908(0x44) = CONST 
    0x90c: v90c = ADD v8c4, v908(0x44)
    0x90e: v90e(0x20) = CONST 
    0x915: v915(0x0) = SUB v8c4, v8ff
    0x916: v916(0x44) = ADD v915(0x0), v908(0x44)
    0x918: v918(0x0) = CONST 
    0x91c: v91c = EXTCODESIZE v900
    0x91d: v91d = ISZERO v91c
    0x91f: v91f = ISZERO v91d
    0x920: v920(0x928) = CONST 
    0x923: JUMPI v920(0x928), v91f

    Begin block 0x924
    prev=[0x8c1], succ=[]
    =================================
    0x924: v924(0x0) = CONST 
    0x927: REVERT v924(0x0), v924(0x0)

    Begin block 0x928
    prev=[0x8c1], succ=[0x933, 0x93c]
    =================================
    0x92a: v92a = GAS 
    0x92b: v92b = CALL v92a, v900, v918(0x0), v8ff, v916(0x44), v8ff, v90e(0x20)
    0x92c: v92c = ISZERO v92b
    0x92e: v92e = ISZERO v92c
    0x92f: v92f(0x93c) = CONST 
    0x932: JUMPI v92f(0x93c), v92e

    Begin block 0x933
    prev=[0x928], succ=[]
    =================================
    0x933: v933 = RETURNDATASIZE 
    0x934: v934(0x0) = CONST 
    0x937: RETURNDATACOPY v934(0x0), v934(0x0), v933
    0x938: v938 = RETURNDATASIZE 
    0x939: v939(0x0) = CONST 
    0x93b: REVERT v939(0x0), v938

    Begin block 0x93c
    prev=[0x928], succ=[0x94e, 0x952]
    =================================
    0x941: v941(0x40) = CONST 
    0x943: v943 = MLOAD v941(0x40)
    0x944: v944 = RETURNDATASIZE 
    0x945: v945(0x20) = CONST 
    0x948: v948 = LT v944, v945(0x20)
    0x949: v949 = ISZERO v948
    0x94a: v94a(0x952) = CONST 
    0x94d: JUMPI v94a(0x952), v949

    Begin block 0x94e
    prev=[0x93c], succ=[]
    =================================
    0x94e: v94e(0x0) = CONST 
    0x951: REVERT v94e(0x0), v94e(0x0)

    Begin block 0x952
    prev=[0x93c], succ=[0x955]
    =================================

    Begin block 0x955
    prev=[0x8b5, 0x952], succ=[0x13f2]
    =================================
    0x956: v956(0x2) = CONST 
    0x959: v959 = SLOAD v956(0x2)
    0x95a: v95a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x96f: v96f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v95a(0xffffffffffffffffffffffffffffffffffffffff)
    0x970: v970 = AND v96f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v959
    0x971: v971(0x1) = CONST 
    0x973: v973(0xa0) = CONST 
    0x975: v975(0x2) = CONST 
    0x977: v977(0x10000000000000000000000000000000000000000) = EXP v975(0x2), v973(0xa0)
    0x978: v978(0xffffffffffffffffffffffffffffffffffffffff) = SUB v977(0x10000000000000000000000000000000000000000), v971(0x1)
    0x97a: v97a = AND v2b2, v978(0xffffffffffffffffffffffffffffffffffffffff)
    0x97d: v97d = OR v97a, v970
    0x980: SSTORE v956(0x2), v97d
    0x981: v981(0x40) = CONST 
    0x983: v983 = MLOAD v981(0x40)
    0x984: v984(0x1466d4e2c17718222b4ada7f7cbc8907912d6083fdaf34382703d6a9602eef55) = CONST 
    0x9a6: v9a6(0x0) = CONST 
    0x9a9: LOG2 v983, v9a6(0x0), v984(0x1466d4e2c17718222b4ada7f7cbc8907912d6083fdaf34382703d6a9602eef55), v97a
    0x9ab: v9ab(0x1) = CONST 
    0x9b1: JUMP v2a4(0x13f2)

    Begin block 0x13f2
    prev=[0x955], succ=[]
    =================================
    0x13f3: v13f3(0x40) = CONST 
    0x13f6: v13f6 = MLOAD v13f3(0x40)
    0x13f8: v13f8 = ISZERO v9ab(0x1)
    0x13f9: v13f9 = ISZERO v13f8
    0x13fb: MSTORE v13f6, v13f9
    0x13fc: v13fc = MLOAD v13f3(0x40)
    0x1400: v1400(0x0) = SUB v13f6, v13fc
    0x1401: v1401(0x20) = CONST 
    0x1403: v1403(0x20) = ADD v1401(0x20), v1400(0x0)
    0x1405: RETURN v13fc, v1403(0x20)

    Begin block 0x87e
    prev=[0x86a], succ=[0x88c]
    =================================
    0x87f: v87f(0x2) = CONST 
    0x881: v881 = SLOAD v87f(0x2)
    0x882: v882(0x1) = CONST 
    0x884: v884(0xa0) = CONST 
    0x886: v886(0x2) = CONST 
    0x888: v888(0x10000000000000000000000000000000000000000) = EXP v886(0x2), v884(0xa0)
    0x889: v889(0xffffffffffffffffffffffffffffffffffffffff) = SUB v888(0x10000000000000000000000000000000000000000), v882(0x1)
    0x88a: v88a = AND v889(0xffffffffffffffffffffffffffffffffffffffff), v881
    0x88b: v88b = ISZERO v88a

}

function unpause()() public {
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
    prev=[0x2b7], succ=[0x9b2]
    =================================
    0x2c5: v2c5(0x1425) = CONST 
    0x2c8: v2c8(0x9b2) = CONST 
    0x2cb: JUMP v2c8(0x9b2)

    Begin block 0x9b2
    prev=[0x2c3], succ=[0x9c5, 0x9c9]
    =================================
    0x9b3: v9b3(0x0) = CONST 
    0x9b5: v9b5 = SLOAD v9b3(0x0)
    0x9b6: v9b6(0x1) = CONST 
    0x9b8: v9b8(0xa0) = CONST 
    0x9ba: v9ba(0x2) = CONST 
    0x9bc: v9bc(0x10000000000000000000000000000000000000000) = EXP v9ba(0x2), v9b8(0xa0)
    0x9bd: v9bd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9bc(0x10000000000000000000000000000000000000000), v9b6(0x1)
    0x9be: v9be = AND v9bd(0xffffffffffffffffffffffffffffffffffffffff), v9b5
    0x9bf: v9bf = CALLER 
    0x9c0: v9c0 = EQ v9bf, v9be
    0x9c1: v9c1(0x9c9) = CONST 
    0x9c4: JUMPI v9c1(0x9c9), v9c0

    Begin block 0x9c5
    prev=[0x9b2], succ=[]
    =================================
    0x9c5: v9c5(0x0) = CONST 
    0x9c8: REVERT v9c5(0x0), v9c5(0x0)

    Begin block 0x9c9
    prev=[0x9b2], succ=[0x9db, 0x9df]
    =================================
    0x9ca: v9ca(0x6) = CONST 
    0x9cc: v9cc = SLOAD v9ca(0x6)
    0x9cd: v9cd(0x100) = CONST 
    0x9d1: v9d1 = DIV v9cc, v9cd(0x100)
    0x9d2: v9d2(0xff) = CONST 
    0x9d4: v9d4 = AND v9d2(0xff), v9d1
    0x9d5: v9d5 = ISZERO v9d4
    0x9d6: v9d6 = ISZERO v9d5
    0x9d7: v9d7(0x9df) = CONST 
    0x9da: JUMPI v9d7(0x9df), v9d6

    Begin block 0x9db
    prev=[0x9c9], succ=[]
    =================================
    0x9db: v9db(0x0) = CONST 
    0x9de: REVERT v9db(0x0), v9db(0x0)

    Begin block 0x9df
    prev=[0x9c9], succ=[0x1425]
    =================================
    0x9e0: v9e0(0x6) = CONST 
    0x9e3: v9e3 = SLOAD v9e0(0x6)
    0x9e4: v9e4(0xff00) = CONST 
    0x9e7: v9e7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v9e4(0xff00)
    0x9e8: v9e8 = AND v9e7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v9e3
    0x9ea: SSTORE v9e0(0x6), v9e8
    0x9eb: v9eb(0x40) = CONST 
    0x9ed: v9ed = MLOAD v9eb(0x40)
    0x9ee: v9ee(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33) = CONST 
    0xa10: va10(0x0) = CONST 
    0xa13: LOG1 v9ed, va10(0x0), v9ee(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33)
    0xa14: JUMP v2c5(0x1425)

    Begin block 0x1425
    prev=[0x9df], succ=[]
    =================================
    0x1426: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x2ce
    prev=[], succ=[0x2d6, 0x2da]
    =================================
    0x2cf: v2cf = CALLVALUE 
    0x2d1: v2d1 = ISZERO v2cf
    0x2d2: v2d2(0x2da) = CONST 
    0x2d5: JUMPI v2d2(0x2da), v2d1

    Begin block 0x2d6
    prev=[0x2ce], succ=[]
    =================================
    0x2d6: v2d6(0x0) = CONST 
    0x2d9: REVERT v2d6(0x0), v2d6(0x0)

    Begin block 0x2da
    prev=[0x2ce], succ=[0xa15B0x2da]
    =================================
    0x2dc: v2dc(0x1446) = CONST 
    0x2df: v2df(0x1) = CONST 
    0x2e1: v2e1(0xa0) = CONST 
    0x2e3: v2e3(0x2) = CONST 
    0x2e5: v2e5(0x10000000000000000000000000000000000000000) = EXP v2e3(0x2), v2e1(0xa0)
    0x2e6: v2e6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e5(0x10000000000000000000000000000000000000000), v2df(0x1)
    0x2e7: v2e7(0x4) = CONST 
    0x2e9: v2e9 = CALLDATALOAD v2e7(0x4)
    0x2ea: v2ea = AND v2e9, v2e6(0xffffffffffffffffffffffffffffffffffffffff)
    0x2eb: v2eb(0x24) = CONST 
    0x2ed: v2ed = CALLDATALOAD v2eb(0x24)
    0x2ee: v2ee(0xa15) = CONST 
    0x2f1: JUMP v2ee(0xa15), v2ed, v2ea, v2dc(0x1446)

    Begin block 0xa15B0x2da
    prev=[0x2da], succ=[0xa28B0x2da, 0xa2cB0x2da]
    =================================
    0xa16S0x2da: va16V2da(0x0) = CONST 
    0xa18S0x2da: va18V2da = SLOAD va16V2da(0x0)
    0xa19S0x2da: va19V2da(0x1) = CONST 
    0xa1bS0x2da: va1bV2da(0xa0) = CONST 
    0xa1dS0x2da: va1dV2da(0x2) = CONST 
    0xa1fS0x2da: va1fV2da(0x10000000000000000000000000000000000000000) = EXP va1dV2da(0x2), va1bV2da(0xa0)
    0xa20S0x2da: va20V2da(0xffffffffffffffffffffffffffffffffffffffff) = SUB va1fV2da(0x10000000000000000000000000000000000000000), va19V2da(0x1)
    0xa21S0x2da: va21V2da = AND va20V2da(0xffffffffffffffffffffffffffffffffffffffff), va18V2da
    0xa22S0x2da: va22V2da = CALLER 
    0xa23S0x2da: va23V2da = EQ va22V2da, va21V2da
    0xa24S0x2da: va24V2da(0xa2c) = CONST 
    0xa27S0x2da: JUMPI va24V2da(0xa2c), va23V2da

    Begin block 0xa28B0x2da
    prev=[0xa15B0x2da], succ=[]
    =================================
    0xa28S0x2da: va28V2da(0x0) = CONST 
    0xa2bS0x2da: REVERT va28V2da(0x0), va28V2da(0x0)

    Begin block 0xa2cB0x2da
    prev=[0xa15B0x2da], succ=[0xa4eB0x2da, 0xa40B0x2da]
    =================================
    0xa2dS0x2da: va2dV2da(0x2) = CONST 
    0xa2fS0x2da: va2fV2da = SLOAD va2dV2da(0x2)
    0xa30S0x2da: va30V2da(0x1) = CONST 
    0xa32S0x2da: va32V2da(0xa0) = CONST 
    0xa34S0x2da: va34V2da(0x2) = CONST 
    0xa36S0x2da: va36V2da(0x10000000000000000000000000000000000000000) = EXP va34V2da(0x2), va32V2da(0xa0)
    0xa37S0x2da: va37V2da(0xffffffffffffffffffffffffffffffffffffffff) = SUB va36V2da(0x10000000000000000000000000000000000000000), va30V2da(0x1)
    0xa38S0x2da: va38V2da = AND va37V2da(0xffffffffffffffffffffffffffffffffffffffff), va2fV2da
    0xa39S0x2da: va39V2da = CALLER 
    0xa3aS0x2da: va3aV2da = EQ va39V2da, va38V2da
    0xa3cS0x2da: va3cV2da(0xa4e) = CONST 
    0xa3fS0x2da: JUMPI va3cV2da(0xa4e), va3aV2da

    Begin block 0xa4eB0x2da
    prev=[0xa2cB0x2da, 0xa40B0x2da], succ=[0xa55B0x2da, 0xa59B0x2da]
    =================================
    0xa4e_0x0S0x2da: va4e_0V2da = PHI va3aV2da, va4dV2da
    0xa4fS0x2da: va4fV2da = ISZERO va4e_0V2da
    0xa50S0x2da: va50V2da = ISZERO va4fV2da
    0xa51S0x2da: va51V2da(0xa59) = CONST 
    0xa54S0x2da: JUMPI va51V2da(0xa59), va50V2da

    Begin block 0xa55B0x2da
    prev=[0xa4eB0x2da], succ=[]
    =================================
    0xa55S0x2da: va55V2da(0x0) = CONST 
    0xa58S0x2da: REVERT va55V2da(0x0), va55V2da(0x0)

    Begin block 0xa59B0x2da
    prev=[0xa4eB0x2da], succ=[0xa6aB0x2da, 0xa6eB0x2da]
    =================================
    0xa5aS0x2da: va5aV2da(0x6) = CONST 
    0xa5cS0x2da: va5cV2da = SLOAD va5aV2da(0x6)
    0xa5dS0x2da: va5dV2da(0x100) = CONST 
    0xa61S0x2da: va61V2da = DIV va5cV2da, va5dV2da(0x100)
    0xa62S0x2da: va62V2da(0xff) = CONST 
    0xa64S0x2da: va64V2da = AND va62V2da(0xff), va61V2da
    0xa65S0x2da: va65V2da = ISZERO va64V2da
    0xa66S0x2da: va66V2da(0xa6e) = CONST 
    0xa69S0x2da: JUMPI va66V2da(0xa6e), va65V2da

    Begin block 0xa6aB0x2da
    prev=[0xa59B0x2da], succ=[]
    =================================
    0xa6aS0x2da: va6aV2da(0x0) = CONST 
    0xa6dS0x2da: REVERT va6aV2da(0x0), va6aV2da(0x0)

    Begin block 0xa6eB0x2da
    prev=[0xa59B0x2da], succ=[0xaf5B0x2da, 0xaf9B0x2da]
    =================================
    0xa6fS0x2da: va6fV2da(0x6) = CONST 
    0xa71S0x2da: va71V2da = SLOAD va6fV2da(0x6)
    0xa72S0x2da: va72V2da(0x40) = CONST 
    0xa75S0x2da: va75V2da = MLOAD va72V2da(0x40)
    0xa76S0x2da: va76V2da(0xc6c3bbe600000000000000000000000000000000000000000000000000000000) = CONST 
    0xa98S0x2da: MSTORE va75V2da, va76V2da(0xc6c3bbe600000000000000000000000000000000000000000000000000000000)
    0xa99S0x2da: va99V2da(0x1) = CONST 
    0xa9bS0x2da: va9bV2da(0xa0) = CONST 
    0xa9dS0x2da: va9dV2da(0x2) = CONST 
    0xa9fS0x2da: va9fV2da(0x10000000000000000000000000000000000000000) = EXP va9dV2da(0x2), va9bV2da(0xa0)
    0xaa0S0x2da: vaa0V2da(0xffffffffffffffffffffffffffffffffffffffff) = SUB va9fV2da(0x10000000000000000000000000000000000000000), va99V2da(0x1)
    0xaa1S0x2da: vaa1V2da(0x10000) = CONST 
    0xaa7S0x2da: vaa7V2da = DIV va71V2da, vaa1V2da(0x10000)
    0xaa9S0x2da: vaa9V2da = AND vaa0V2da(0xffffffffffffffffffffffffffffffffffffffff), vaa7V2da
    0xaaaS0x2da: vaaaV2da(0x4) = CONST 
    0xaadS0x2da: vaadV2da = ADD va75V2da, vaaaV2da(0x4)
    0xaaeS0x2da: MSTORE vaadV2da, vaa9V2da
    0xab1S0x2da: vab1V2da = AND v2ea, vaa0V2da(0xffffffffffffffffffffffffffffffffffffffff)
    0xab2S0x2da: vab2V2da(0x24) = CONST 
    0xab5S0x2da: vab5V2da = ADD va75V2da, vab2V2da(0x24)
    0xab6S0x2da: MSTORE vab5V2da, vab1V2da
    0xab7S0x2da: vab7V2da(0x44) = CONST 
    0xabaS0x2da: vabaV2da = ADD va75V2da, vab7V2da(0x44)
    0xabdS0x2da: MSTORE vabaV2da, v2ed
    0xabeS0x2da: vabeV2da = MLOAD va72V2da(0x40)
    0xabfS0x2da: vabfV2da(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0xad5S0x2da: vad5V2da(0xc6c3bbe6) = CONST 
    0xadbS0x2da: vadbV2da(0x64) = CONST 
    0xadfS0x2da: vadfV2da = ADD va75V2da, vadbV2da(0x64)
    0xae1S0x2da: vae1V2da(0x0) = CONST 
    0xae8S0x2da: vae8V2da(0x0) = SUB va75V2da, vabeV2da
    0xae9S0x2da: vae9V2da(0x64) = ADD vae8V2da(0x0), vadbV2da(0x64)
    0xaedS0x2da: vaedV2da = EXTCODESIZE vabfV2da(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0xaeeS0x2da: vaeeV2da = ISZERO vaedV2da
    0xaf0S0x2da: vaf0V2da = ISZERO vaeeV2da
    0xaf1S0x2da: vaf1V2da(0xaf9) = CONST 
    0xaf4S0x2da: JUMPI vaf1V2da(0xaf9), vaf0V2da

    Begin block 0xaf5B0x2da
    prev=[0xa6eB0x2da], succ=[]
    =================================
    0xaf5S0x2da: vaf5V2da(0x0) = CONST 
    0xaf8S0x2da: REVERT vaf5V2da(0x0), vaf5V2da(0x0)

    Begin block 0xaf9B0x2da
    prev=[0xa6eB0x2da], succ=[0xb04B0x2da, 0xb0dB0x2da]
    =================================
    0xafbS0x2da: vafbV2da = GAS 
    0xafcS0x2da: vafcV2da = DELEGATECALL vafbV2da, vabfV2da(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), vabeV2da, vae9V2da(0x64), vabeV2da, vae1V2da(0x0)
    0xafdS0x2da: vafdV2da = ISZERO vafcV2da
    0xaffS0x2da: vaffV2da = ISZERO vafdV2da
    0xb00S0x2da: vb00V2da(0xb0d) = CONST 
    0xb03S0x2da: JUMPI vb00V2da(0xb0d), vaffV2da

    Begin block 0xb04B0x2da
    prev=[0xaf9B0x2da], succ=[]
    =================================
    0xb04S0x2da: vb04V2da = RETURNDATASIZE 
    0xb05S0x2da: vb05V2da(0x0) = CONST 
    0xb08S0x2da: RETURNDATACOPY vb05V2da(0x0), vb05V2da(0x0), vb04V2da
    0xb09S0x2da: vb09V2da = RETURNDATASIZE 
    0xb0aS0x2da: vb0aV2da(0x0) = CONST 
    0xb0cS0x2da: REVERT vb0aV2da(0x0), vb09V2da

    Begin block 0xb0dB0x2da
    prev=[0xaf9B0x2da], succ=[0x1446]
    =================================
    0xb14S0x2da: JUMP v2dc(0x1446)

    Begin block 0x1446
    prev=[0xb0dB0x2da], succ=[]
    =================================
    0x1447: STOP 

    Begin block 0xa40B0x2da
    prev=[0xa2cB0x2da], succ=[0xa4eB0x2da]
    =================================
    0xa41S0x2da: va41V2da(0x2) = CONST 
    0xa43S0x2da: va43V2da = SLOAD va41V2da(0x2)
    0xa44S0x2da: va44V2da(0x1) = CONST 
    0xa46S0x2da: va46V2da(0xa0) = CONST 
    0xa48S0x2da: va48V2da(0x2) = CONST 
    0xa4aS0x2da: va4aV2da(0x10000000000000000000000000000000000000000) = EXP va48V2da(0x2), va46V2da(0xa0)
    0xa4bS0x2da: va4bV2da(0xffffffffffffffffffffffffffffffffffffffff) = SUB va4aV2da(0x10000000000000000000000000000000000000000), va44V2da(0x1)
    0xa4cS0x2da: va4cV2da = AND va4bV2da(0xffffffffffffffffffffffffffffffffffffffff), va43V2da
    0xa4dS0x2da: va4dV2da = ISZERO va4cV2da

}

function version()() public {
    Begin block 0x2f2
    prev=[], succ=[0x2fa, 0x2fe]
    =================================
    0x2f3: v2f3 = CALLVALUE 
    0x2f5: v2f5 = ISZERO v2f3
    0x2f6: v2f6(0x2fe) = CONST 
    0x2f9: JUMPI v2f6(0x2fe), v2f5

    Begin block 0x2fa
    prev=[0x2f2], succ=[]
    =================================
    0x2fa: v2fa(0x0) = CONST 
    0x2fd: REVERT v2fa(0x0), v2fa(0x0)

    Begin block 0x2fe
    prev=[0x2f2], succ=[0x16d0x2f2]
    =================================
    0x300: v300(0x16d) = CONST 
    0x303: v303(0xb15) = CONST 
    0x306: v306_0, v306_1 = CALLPRIVATE v303(0xb15), v300(0x16d)

    Begin block 0x16d0x2f2
    prev=[0x2fe], succ=[0x18f0x2f2]
    =================================
    0x16e0x2f2: v2f216e(0x40) = CONST 
    0x1710x2f2: v2f2171 = MLOAD v2f216e(0x40)
    0x1720x2f2: v2f2172(0x20) = CONST 
    0x1760x2f2: MSTORE v2f2171, v2f2172(0x20)
    0x1780x2f2: v2f2178 = MLOAD v306_0
    0x17b0x2f2: v2f217b = ADD v2f2171, v2f2172(0x20)
    0x17c0x2f2: MSTORE v2f217b, v2f2178
    0x17e0x2f2: v2f217e = MLOAD v306_0
    0x1850x2f2: v2f2185 = ADD v2f2171, v2f216e(0x40)
    0x1880x2f2: v2f2188 = ADD v306_0, v2f2172(0x20)
    0x18d0x2f2: v2f218d(0x0) = CONST 

    Begin block 0x18f0x2f2
    prev=[0x1980x2f2, 0x16d0x2f2], succ=[0x1a70x2f2, 0x1980x2f2]
    =================================
    0x18f0x2f2_0x0: v18f2f2_0 = PHI v2f21a2, v2f218d(0x0)
    0x1920x2f2: v2f2192 = LT v18f2f2_0, v2f217e
    0x1930x2f2: v2f2193 = ISZERO v2f2192
    0x1940x2f2: v2f2194(0x1a7) = CONST 
    0x1970x2f2: JUMPI v2f2194(0x1a7), v2f2193

    Begin block 0x1a70x2f2
    prev=[0x18f0x2f2], succ=[0x1d40x2f2, 0x1bb0x2f2]
    =================================
    0x1b00x2f2: v2f21b0 = ADD v2f217e, v2f2185
    0x1b20x2f2: v2f21b2(0x1f) = CONST 
    0x1b40x2f2: v2f21b4 = AND v2f21b2(0x1f), v2f217e
    0x1b60x2f2: v2f21b6 = ISZERO v2f21b4
    0x1b70x2f2: v2f21b7(0x1d4) = CONST 
    0x1ba0x2f2: JUMPI v2f21b7(0x1d4), v2f21b6

    Begin block 0x1d40x2f2
    prev=[0x1a70x2f2, 0x1bb0x2f2], succ=[]
    =================================
    0x1d40x2f2_0x1: v1d42f2_1 = PHI v2f21d1, v2f21b0
    0x1da0x2f2: v2f21da(0x40) = CONST 
    0x1dc0x2f2: v2f21dc = MLOAD v2f21da(0x40)
    0x1df0x2f2: v2f21df = SUB v1d42f2_1, v2f21dc
    0x1e10x2f2: RETURN v2f21dc, v2f21df

    Begin block 0x1bb0x2f2
    prev=[0x1a70x2f2], succ=[0x1d40x2f2]
    =================================
    0x1bd0x2f2: v2f21bd = SUB v2f21b0, v2f21b4
    0x1bf0x2f2: v2f21bf = MLOAD v2f21bd
    0x1c00x2f2: v2f21c0(0x1) = CONST 
    0x1c30x2f2: v2f21c3(0x20) = CONST 
    0x1c50x2f2: v2f21c5 = SUB v2f21c3(0x20), v2f21b4
    0x1c60x2f2: v2f21c6(0x100) = CONST 
    0x1c90x2f2: v2f21c9 = EXP v2f21c6(0x100), v2f21c5
    0x1ca0x2f2: v2f21ca = SUB v2f21c9, v2f21c0(0x1)
    0x1cb0x2f2: v2f21cb = NOT v2f21ca
    0x1cc0x2f2: v2f21cc = AND v2f21cb, v2f21bf
    0x1ce0x2f2: MSTORE v2f21bd, v2f21cc
    0x1cf0x2f2: v2f21cf(0x20) = CONST 
    0x1d10x2f2: v2f21d1 = ADD v2f21cf(0x20), v2f21bd

    Begin block 0x1980x2f2
    prev=[0x18f0x2f2], succ=[0x18f0x2f2]
    =================================
    0x1980x2f2_0x0: v1982f2_0 = PHI v2f21a2, v2f218d(0x0)
    0x19a0x2f2: v2f219a = ADD v1982f2_0, v2f2188
    0x19b0x2f2: v2f219b = MLOAD v2f219a
    0x19e0x2f2: v2f219e = ADD v1982f2_0, v2f2185
    0x19f0x2f2: MSTORE v2f219e, v2f219b
    0x1a00x2f2: v2f21a0(0x20) = CONST 
    0x1a20x2f2: v2f21a2 = ADD v2f21a0(0x20), v1982f2_0
    0x1a30x2f2: v2f21a3(0x18f) = CONST 
    0x1a60x2f2: JUMP v2f21a3(0x18f)

}

function paused()() public {
    Begin block 0x307
    prev=[], succ=[0x30f, 0x313]
    =================================
    0x308: v308 = CALLVALUE 
    0x30a: v30a = ISZERO v308
    0x30b: v30b(0x313) = CONST 
    0x30e: JUMPI v30b(0x313), v30a

    Begin block 0x30f
    prev=[0x307], succ=[]
    =================================
    0x30f: v30f(0x0) = CONST 
    0x312: REVERT v30f(0x0), v30f(0x0)

    Begin block 0x313
    prev=[0x307], succ=[0xb70]
    =================================
    0x315: v315(0x1467) = CONST 
    0x318: v318(0xb70) = CONST 
    0x31b: JUMP v318(0xb70)

    Begin block 0xb70
    prev=[0x313], succ=[0x1467]
    =================================
    0xb71: vb71(0x6) = CONST 
    0xb73: vb73 = SLOAD vb71(0x6)
    0xb74: vb74(0x100) = CONST 
    0xb78: vb78 = DIV vb73, vb74(0x100)
    0xb79: vb79(0xff) = CONST 
    0xb7b: vb7b = AND vb79(0xff), vb78
    0xb7d: JUMP v315(0x1467)

    Begin block 0x1467
    prev=[0xb70], succ=[]
    =================================
    0x1468: v1468(0x40) = CONST 
    0x146b: v146b = MLOAD v1468(0x40)
    0x146d: v146d = ISZERO vb7b
    0x146e: v146e = ISZERO v146d
    0x1470: MSTORE v146b, v146e
    0x1471: v1471 = MLOAD v1468(0x40)
    0x1475: v1475(0x0) = SUB v146b, v1471
    0x1476: v1476(0x20) = CONST 
    0x1478: v1478(0x20) = ADD v1476(0x20), v1475(0x0)
    0x147a: RETURN v1471, v1478(0x20)

}

function decreaseApproval(address,uint256)() public {
    Begin block 0x31c
    prev=[], succ=[0x324, 0x328]
    =================================
    0x31d: v31d = CALLVALUE 
    0x31f: v31f = ISZERO v31d
    0x320: v320(0x328) = CONST 
    0x323: JUMPI v320(0x328), v31f

    Begin block 0x324
    prev=[0x31c], succ=[]
    =================================
    0x324: v324(0x0) = CONST 
    0x327: REVERT v324(0x0), v324(0x0)

    Begin block 0x328
    prev=[0x31c], succ=[0xb7eB0x328]
    =================================
    0x32a: v32a(0x149a) = CONST 
    0x32d: v32d(0x1) = CONST 
    0x32f: v32f(0xa0) = CONST 
    0x331: v331(0x2) = CONST 
    0x333: v333(0x10000000000000000000000000000000000000000) = EXP v331(0x2), v32f(0xa0)
    0x334: v334(0xffffffffffffffffffffffffffffffffffffffff) = SUB v333(0x10000000000000000000000000000000000000000), v32d(0x1)
    0x335: v335(0x4) = CONST 
    0x337: v337 = CALLDATALOAD v335(0x4)
    0x338: v338 = AND v337, v334(0xffffffffffffffffffffffffffffffffffffffff)
    0x339: v339(0x24) = CONST 
    0x33b: v33b = CALLDATALOAD v339(0x24)
    0x33c: v33c(0xb7e) = CONST 
    0x33f: JUMP v33c(0xb7e)

    Begin block 0xb7eB0x328
    prev=[0x328], succ=[0xba3B0x328, 0xb95B0x328]
    =================================
    0xb7fS0x328: vb7fV328(0x2) = CONST 
    0xb81S0x328: vb81V328 = SLOAD vb7fV328(0x2)
    0xb82S0x328: vb82V328(0x0) = CONST 
    0xb85S0x328: vb85V328(0x1) = CONST 
    0xb87S0x328: vb87V328(0xa0) = CONST 
    0xb89S0x328: vb89V328(0x2) = CONST 
    0xb8bS0x328: vb8bV328(0x10000000000000000000000000000000000000000) = EXP vb89V328(0x2), vb87V328(0xa0)
    0xb8cS0x328: vb8cV328(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb8bV328(0x10000000000000000000000000000000000000000), vb85V328(0x1)
    0xb8dS0x328: vb8dV328 = AND vb8cV328(0xffffffffffffffffffffffffffffffffffffffff), vb81V328
    0xb8eS0x328: vb8eV328 = CALLER 
    0xb8fS0x328: vb8fV328 = EQ vb8eV328, vb8dV328
    0xb91S0x328: vb91V328(0xba3) = CONST 
    0xb94S0x328: JUMPI vb91V328(0xba3), vb8fV328

    Begin block 0xba3B0x328
    prev=[0xb7eB0x328, 0xb95B0x328], succ=[0xbaaB0x328, 0xbaeB0x328]
    =================================
    0xba3_0x0S0x328: vba3_0V328 = PHI vb8fV328, vba2V328
    0xba4S0x328: vba4V328 = ISZERO vba3_0V328
    0xba5S0x328: vba5V328 = ISZERO vba4V328
    0xba6S0x328: vba6V328(0xbae) = CONST 
    0xba9S0x328: JUMPI vba6V328(0xbae), vba5V328

    Begin block 0xbaaB0x328
    prev=[0xba3B0x328], succ=[]
    =================================
    0xbaaS0x328: vbaaV328(0x0) = CONST 
    0xbadS0x328: REVERT vbaaV328(0x0), vbaaV328(0x0)

    Begin block 0xbaeB0x328
    prev=[0xba3B0x328], succ=[0xbbfB0x328, 0xbc3B0x328]
    =================================
    0xbafS0x328: vbafV328(0x6) = CONST 
    0xbb1S0x328: vbb1V328 = SLOAD vbafV328(0x6)
    0xbb2S0x328: vbb2V328(0x100) = CONST 
    0xbb6S0x328: vbb6V328 = DIV vbb1V328, vbb2V328(0x100)
    0xbb7S0x328: vbb7V328(0xff) = CONST 
    0xbb9S0x328: vbb9V328 = AND vbb7V328(0xff), vbb6V328
    0xbbaS0x328: vbbaV328 = ISZERO vbb9V328
    0xbbbS0x328: vbbbV328(0xbc3) = CONST 
    0xbbeS0x328: JUMPI vbbbV328(0xbc3), vbbaV328

    Begin block 0xbbfB0x328
    prev=[0xbaeB0x328], succ=[]
    =================================
    0xbbfS0x328: vbbfV328(0x0) = CONST 
    0xbc2S0x328: REVERT vbbfV328(0x0), vbbfV328(0x0)

    Begin block 0xbc3B0x328
    prev=[0xbaeB0x328], succ=[0xc4aB0x328, 0x6580xb7eB0x328]
    =================================
    0xbc4S0x328: vbc4V328(0x6) = CONST 
    0xbc6S0x328: vbc6V328 = SLOAD vbc4V328(0x6)
    0xbc7S0x328: vbc7V328(0x40) = CONST 
    0xbcaS0x328: vbcaV328 = MLOAD vbc7V328(0x40)
    0xbcbS0x328: vbcbV328(0xf019c26700000000000000000000000000000000000000000000000000000000) = CONST 
    0xbedS0x328: MSTORE vbcaV328, vbcbV328(0xf019c26700000000000000000000000000000000000000000000000000000000)
    0xbeeS0x328: vbeeV328(0x1) = CONST 
    0xbf0S0x328: vbf0V328(0xa0) = CONST 
    0xbf2S0x328: vbf2V328(0x2) = CONST 
    0xbf4S0x328: vbf4V328(0x10000000000000000000000000000000000000000) = EXP vbf2V328(0x2), vbf0V328(0xa0)
    0xbf5S0x328: vbf5V328(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbf4V328(0x10000000000000000000000000000000000000000), vbeeV328(0x1)
    0xbf6S0x328: vbf6V328(0x10000) = CONST 
    0xbfcS0x328: vbfcV328 = DIV vbc6V328, vbf6V328(0x10000)
    0xbfeS0x328: vbfeV328 = AND vbf5V328(0xffffffffffffffffffffffffffffffffffffffff), vbfcV328
    0xbffS0x328: vbffV328(0x4) = CONST 
    0xc02S0x328: vc02V328 = ADD vbcaV328, vbffV328(0x4)
    0xc03S0x328: MSTORE vc02V328, vbfeV328
    0xc06S0x328: vc06V328 = AND v338, vbf5V328(0xffffffffffffffffffffffffffffffffffffffff)
    0xc07S0x328: vc07V328(0x24) = CONST 
    0xc0aS0x328: vc0aV328 = ADD vbcaV328, vc07V328(0x24)
    0xc0bS0x328: MSTORE vc0aV328, vc06V328
    0xc0cS0x328: vc0cV328(0x44) = CONST 
    0xc0fS0x328: vc0fV328 = ADD vbcaV328, vc0cV328(0x44)
    0xc12S0x328: MSTORE vc0fV328, v33b
    0xc13S0x328: vc13V328 = MLOAD vbc7V328(0x40)
    0xc14S0x328: vc14V328(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0xc2aS0x328: vc2aV328(0xf019c267) = CONST 
    0xc30S0x328: vc30V328(0x64) = CONST 
    0xc34S0x328: vc34V328 = ADD vbcaV328, vc30V328(0x64)
    0xc36S0x328: vc36V328(0x20) = CONST 
    0xc3dS0x328: vc3dV328(0x0) = SUB vbcaV328, vc13V328
    0xc3eS0x328: vc3eV328(0x64) = ADD vc3dV328(0x0), vc30V328(0x64)
    0xc42S0x328: vc42V328 = EXTCODESIZE vc14V328(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0xc43S0x328: vc43V328 = ISZERO vc42V328
    0xc45S0x328: vc45V328 = ISZERO vc43V328
    0xc46S0x328: vc46V328(0x658) = CONST 
    0xc49S0x328: JUMPI vc46V328(0x658), vc45V328

    Begin block 0xc4aB0x328
    prev=[0xbc3B0x328], succ=[]
    =================================
    0xc4aS0x328: vc4aV328(0x0) = CONST 
    0xc4dS0x328: REVERT vc4aV328(0x0), vc4aV328(0x0)

    Begin block 0x6580xb7eB0x328
    prev=[0xbc3B0x328], succ=[0x6630xb7eB0x328, 0x66c0xb7eB0x328]
    =================================
    0x65a0xb7eS0x328: vb7e65aV328 = GAS 
    0x65b0xb7eS0x328: vb7e65bV328 = DELEGATECALL vb7e65aV328, vc14V328(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), vc13V328, vc3eV328(0x64), vc13V328, vc36V328(0x20)
    0x65c0xb7eS0x328: vb7e65cV328 = ISZERO vb7e65bV328
    0x65e0xb7eS0x328: vb7e65eV328 = ISZERO vb7e65cV328
    0x65f0xb7eS0x328: vb7e65fV328(0x66c) = CONST 
    0x6620xb7eS0x328: JUMPI vb7e65fV328(0x66c), vb7e65eV328

    Begin block 0x6630xb7eB0x328
    prev=[0x6580xb7eB0x328], succ=[]
    =================================
    0x6630xb7eS0x328: vb7e663V328 = RETURNDATASIZE 
    0x6640xb7eS0x328: vb7e664V328(0x0) = CONST 
    0x6670xb7eS0x328: RETURNDATACOPY vb7e664V328(0x0), vb7e664V328(0x0), vb7e663V328
    0x6680xb7eS0x328: vb7e668V328 = RETURNDATASIZE 
    0x6690xb7eS0x328: vb7e669V328(0x0) = CONST 
    0x66b0xb7eS0x328: REVERT vb7e669V328(0x0), vb7e668V328

    Begin block 0x66c0xb7eB0x328
    prev=[0x6580xb7eB0x328], succ=[0x67e0xb7eB0x328, 0x6820xb7eB0x328]
    =================================
    0x6710xb7eS0x328: vb7e671V328(0x40) = CONST 
    0x6730xb7eS0x328: vb7e673V328 = MLOAD vb7e671V328(0x40)
    0x6740xb7eS0x328: vb7e674V328 = RETURNDATASIZE 
    0x6750xb7eS0x328: vb7e675V328(0x20) = CONST 
    0x6780xb7eS0x328: vb7e678V328 = LT vb7e674V328, vb7e675V328(0x20)
    0x6790xb7eS0x328: vb7e679V328 = ISZERO vb7e678V328
    0x67a0xb7eS0x328: vb7e67aV328(0x682) = CONST 
    0x67d0xb7eS0x328: JUMPI vb7e67aV328(0x682), vb7e679V328

    Begin block 0x67e0xb7eB0x328
    prev=[0x66c0xb7eB0x328], succ=[]
    =================================
    0x67e0xb7eS0x328: vb7e67eV328(0x0) = CONST 
    0x6810xb7eS0x328: REVERT vb7e67eV328(0x0), vb7e67eV328(0x0)

    Begin block 0x6820xb7eB0x328
    prev=[0x66c0xb7eB0x328], succ=[0x149a]
    =================================
    0x6840xb7eS0x328: vb7e684V328 = MLOAD vb7e673V328
    0x68a0xb7eS0x328: JUMP v32a(0x149a)

    Begin block 0x149a
    prev=[0x6820xb7eB0x328], succ=[]
    =================================
    0x149b: v149b(0x40) = CONST 
    0x149e: v149e = MLOAD v149b(0x40)
    0x14a0: v14a0 = ISZERO vb7e684V328
    0x14a1: v14a1 = ISZERO v14a0
    0x14a3: MSTORE v149e, v14a1
    0x14a4: v14a4 = MLOAD v149b(0x40)
    0x14a8: v14a8(0x0) = SUB v149e, v14a4
    0x14a9: v14a9(0x20) = CONST 
    0x14ab: v14ab(0x20) = ADD v14a9(0x20), v14a8(0x0)
    0x14ad: RETURN v14a4, v14ab(0x20)

    Begin block 0xb95B0x328
    prev=[0xb7eB0x328], succ=[0xba3B0x328]
    =================================
    0xb96S0x328: vb96V328(0x2) = CONST 
    0xb98S0x328: vb98V328 = SLOAD vb96V328(0x2)
    0xb99S0x328: vb99V328(0x1) = CONST 
    0xb9bS0x328: vb9bV328(0xa0) = CONST 
    0xb9dS0x328: vb9dV328(0x2) = CONST 
    0xb9fS0x328: vb9fV328(0x10000000000000000000000000000000000000000) = EXP vb9dV328(0x2), vb9bV328(0xa0)
    0xba0S0x328: vba0V328(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb9fV328(0x10000000000000000000000000000000000000000), vb99V328(0x1)
    0xba1S0x328: vba1V328 = AND vba0V328(0xffffffffffffffffffffffffffffffffffffffff), vb98V328
    0xba2S0x328: vba2V328 = ISZERO vba1V328

}

function upgradedFrom(address)() public {
    Begin block 0x340
    prev=[], succ=[0x348, 0x34c]
    =================================
    0x341: v341 = CALLVALUE 
    0x343: v343 = ISZERO v341
    0x344: v344(0x34c) = CONST 
    0x347: JUMPI v344(0x34c), v343

    Begin block 0x348
    prev=[0x340], succ=[]
    =================================
    0x348: v348(0x0) = CONST 
    0x34b: REVERT v348(0x0), v348(0x0)

    Begin block 0x34c
    prev=[0x340], succ=[0xc4e]
    =================================
    0x34e: v34e(0x14cd) = CONST 
    0x351: v351(0x1) = CONST 
    0x353: v353(0xa0) = CONST 
    0x355: v355(0x2) = CONST 
    0x357: v357(0x10000000000000000000000000000000000000000) = EXP v355(0x2), v353(0xa0)
    0x358: v358(0xffffffffffffffffffffffffffffffffffffffff) = SUB v357(0x10000000000000000000000000000000000000000), v351(0x1)
    0x359: v359(0x4) = CONST 
    0x35b: v35b = CALLDATALOAD v359(0x4)
    0x35c: v35c = AND v35b, v358(0xffffffffffffffffffffffffffffffffffffffff)
    0x35d: v35d(0xc4e) = CONST 
    0x360: JUMP v35d(0xc4e)

    Begin block 0xc4e
    prev=[0x34c], succ=[0xc62, 0xc66]
    =================================
    0xc4f: vc4f(0x0) = CONST 
    0xc52: vc52 = SLOAD vc4f(0x0)
    0xc53: vc53(0x1) = CONST 
    0xc55: vc55(0xa0) = CONST 
    0xc57: vc57(0x2) = CONST 
    0xc59: vc59(0x10000000000000000000000000000000000000000) = EXP vc57(0x2), vc55(0xa0)
    0xc5a: vc5a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc59(0x10000000000000000000000000000000000000000), vc53(0x1)
    0xc5b: vc5b = AND vc5a(0xffffffffffffffffffffffffffffffffffffffff), vc52
    0xc5c: vc5c = CALLER 
    0xc5d: vc5d = EQ vc5c, vc5b
    0xc5e: vc5e(0xc66) = CONST 
    0xc61: JUMPI vc5e(0xc66), vc5d

    Begin block 0xc62
    prev=[0xc4e], succ=[]
    =================================
    0xc62: vc62(0x0) = CONST 
    0xc65: REVERT vc62(0x0), vc62(0x0)

    Begin block 0xc66
    prev=[0xc4e], succ=[0xc77, 0xc7b]
    =================================
    0xc67: vc67(0x1) = CONST 
    0xc69: vc69(0xa0) = CONST 
    0xc6b: vc6b(0x2) = CONST 
    0xc6d: vc6d(0x10000000000000000000000000000000000000000) = EXP vc6b(0x2), vc69(0xa0)
    0xc6e: vc6e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc6d(0x10000000000000000000000000000000000000000), vc67(0x1)
    0xc70: vc70 = AND v35c, vc6e(0xffffffffffffffffffffffffffffffffffffffff)
    0xc71: vc71 = ISZERO vc70
    0xc72: vc72 = ISZERO vc71
    0xc73: vc73(0xc7b) = CONST 
    0xc76: JUMPI vc73(0xc7b), vc72

    Begin block 0xc77
    prev=[0xc66], succ=[]
    =================================
    0xc77: vc77(0x0) = CONST 
    0xc7a: REVERT vc77(0x0), vc77(0x0)

    Begin block 0xc7b
    prev=[0xc66], succ=[0x14cd]
    =================================
    0xc7c: vc7c(0x1) = CONST 
    0xc7f: vc7f = SLOAD vc7c(0x1)
    0xc80: vc80(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc95: vc95(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vc80(0xffffffffffffffffffffffffffffffffffffffff)
    0xc96: vc96 = AND vc95(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vc7f
    0xc97: vc97(0x1) = CONST 
    0xc99: vc99(0xa0) = CONST 
    0xc9b: vc9b(0x2) = CONST 
    0xc9d: vc9d(0x10000000000000000000000000000000000000000) = EXP vc9b(0x2), vc99(0xa0)
    0xc9e: vc9e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc9d(0x10000000000000000000000000000000000000000), vc97(0x1)
    0xca0: vca0 = AND v35c, vc9e(0xffffffffffffffffffffffffffffffffffffffff)
    0xca3: vca3 = OR vca0, vc96
    0xca6: SSTORE vc7c(0x1), vca3
    0xca7: vca7(0x40) = CONST 
    0xca9: vca9 = MLOAD vca7(0x40)
    0xcaa: vcaa(0x75c09cedaf6c35dc577b0fd0a8c77c569c84be03eae895084c7c60788eac7d64) = CONST 
    0xccc: vccc(0x0) = CONST 
    0xccf: LOG2 vca9, vccc(0x0), vcaa(0x75c09cedaf6c35dc577b0fd0a8c77c569c84be03eae895084c7c60788eac7d64), vca0
    0xcd1: vcd1(0x1) = CONST 
    0xcd6: JUMP v34e(0x14cd)

    Begin block 0x14cd
    prev=[0xc7b], succ=[]
    =================================
    0x14ce: v14ce(0x40) = CONST 
    0x14d1: v14d1 = MLOAD v14ce(0x40)
    0x14d3: v14d3 = ISZERO vcd1(0x1)
    0x14d4: v14d4 = ISZERO v14d3
    0x14d6: MSTORE v14d1, v14d4
    0x14d7: v14d7 = MLOAD v14ce(0x40)
    0x14db: v14db(0x0) = SUB v14d1, v14d7
    0x14dc: v14dc(0x20) = CONST 
    0x14de: v14de(0x20) = ADD v14dc(0x20), v14db(0x0)
    0x14e0: RETURN v14d7, v14de(0x20)

}

function successor()() public {
    Begin block 0x361
    prev=[], succ=[0x369, 0x36d]
    =================================
    0x362: v362 = CALLVALUE 
    0x364: v364 = ISZERO v362
    0x365: v365(0x36d) = CONST 
    0x368: JUMPI v365(0x36d), v364

    Begin block 0x369
    prev=[0x361], succ=[]
    =================================
    0x369: v369(0x0) = CONST 
    0x36c: REVERT v369(0x0), v369(0x0)

    Begin block 0x36d
    prev=[0x361], succ=[0xcd7]
    =================================
    0x36f: v36f(0x1500) = CONST 
    0x372: v372(0xcd7) = CONST 
    0x375: JUMP v372(0xcd7)

    Begin block 0xcd7
    prev=[0x36d], succ=[0x1500]
    =================================
    0xcd8: vcd8(0x2) = CONST 
    0xcda: vcda = SLOAD vcd8(0x2)
    0xcdb: vcdb(0x1) = CONST 
    0xcdd: vcdd(0xa0) = CONST 
    0xcdf: vcdf(0x2) = CONST 
    0xce1: vce1(0x10000000000000000000000000000000000000000) = EXP vcdf(0x2), vcdd(0xa0)
    0xce2: vce2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce1(0x10000000000000000000000000000000000000000), vcdb(0x1)
    0xce3: vce3 = AND vce2(0xffffffffffffffffffffffffffffffffffffffff), vcda
    0xce5: JUMP v36f(0x1500)

    Begin block 0x1500
    prev=[0xcd7], succ=[]
    =================================
    0x1501: v1501(0x40) = CONST 
    0x1504: v1504 = MLOAD v1501(0x40)
    0x1505: v1505(0x1) = CONST 
    0x1507: v1507(0xa0) = CONST 
    0x1509: v1509(0x2) = CONST 
    0x150b: v150b(0x10000000000000000000000000000000000000000) = EXP v1509(0x2), v1507(0xa0)
    0x150c: v150c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v150b(0x10000000000000000000000000000000000000000), v1505(0x1)
    0x150f: v150f = AND vce3, v150c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1511: MSTORE v1504, v150f
    0x1512: v1512 = MLOAD v1501(0x40)
    0x1516: v1516(0x0) = SUB v1504, v1512
    0x1517: v1517(0x20) = CONST 
    0x1519: v1519(0x20) = ADD v1517(0x20), v1516(0x0)
    0x151b: RETURN v1512, v1519(0x20)

}

function balanceOf(address)() public {
    Begin block 0x392
    prev=[], succ=[0x39a, 0x39e]
    =================================
    0x393: v393 = CALLVALUE 
    0x395: v395 = ISZERO v393
    0x396: v396(0x39e) = CONST 
    0x399: JUMPI v396(0x39e), v395

    Begin block 0x39a
    prev=[0x392], succ=[]
    =================================
    0x39a: v39a(0x0) = CONST 
    0x39d: REVERT v39a(0x0), v39a(0x0)

    Begin block 0x39e
    prev=[0x392], succ=[0x153b]
    =================================
    0x3a0: v3a0(0x153b) = CONST 
    0x3a3: v3a3(0x1) = CONST 
    0x3a5: v3a5(0xa0) = CONST 
    0x3a7: v3a7(0x2) = CONST 
    0x3a9: v3a9(0x10000000000000000000000000000000000000000) = EXP v3a7(0x2), v3a5(0xa0)
    0x3aa: v3aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a9(0x10000000000000000000000000000000000000000), v3a3(0x1)
    0x3ab: v3ab(0x4) = CONST 
    0x3ad: v3ad = CALLDATALOAD v3ab(0x4)
    0x3ae: v3ae = AND v3ad, v3aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x3af: v3af(0xce6) = CONST 
    0x3b2: v3b2_0 = CALLPRIVATE v3af(0xce6), v3ae, v3a0(0x153b)

    Begin block 0x153b
    prev=[0x39e], succ=[]
    =================================
    0x153c: v153c(0x40) = CONST 
    0x153f: v153f = MLOAD v153c(0x40)
    0x1542: MSTORE v153f, v3b2_0
    0x1543: v1543 = MLOAD v153c(0x40)
    0x1547: v1547(0x0) = SUB v153f, v1543
    0x1548: v1548(0x20) = CONST 
    0x154a: v154a(0x20) = ADD v1548(0x20), v1547(0x0)
    0x154c: RETURN v1543, v154a(0x20)

}

function renounceOwnership()() public {
    Begin block 0x3b3
    prev=[], succ=[0x3bb, 0x3bf]
    =================================
    0x3b4: v3b4 = CALLVALUE 
    0x3b6: v3b6 = ISZERO v3b4
    0x3b7: v3b7(0x3bf) = CONST 
    0x3ba: JUMPI v3b7(0x3bf), v3b6

    Begin block 0x3bb
    prev=[0x3b3], succ=[]
    =================================
    0x3bb: v3bb(0x0) = CONST 
    0x3be: REVERT v3bb(0x0), v3bb(0x0)

    Begin block 0x3bf
    prev=[0x3b3], succ=[0xda0]
    =================================
    0x3c1: v3c1(0x156c) = CONST 
    0x3c4: v3c4(0xda0) = CONST 
    0x3c7: JUMP v3c4(0xda0)

    Begin block 0xda0
    prev=[0x3bf], succ=[0xdb3, 0xdb7]
    =================================
    0xda1: vda1(0x0) = CONST 
    0xda3: vda3 = SLOAD vda1(0x0)
    0xda4: vda4(0x1) = CONST 
    0xda6: vda6(0xa0) = CONST 
    0xda8: vda8(0x2) = CONST 
    0xdaa: vdaa(0x10000000000000000000000000000000000000000) = EXP vda8(0x2), vda6(0xa0)
    0xdab: vdab(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdaa(0x10000000000000000000000000000000000000000), vda4(0x1)
    0xdac: vdac = AND vdab(0xffffffffffffffffffffffffffffffffffffffff), vda3
    0xdad: vdad = CALLER 
    0xdae: vdae = EQ vdad, vdac
    0xdaf: vdaf(0xdb7) = CONST 
    0xdb2: JUMPI vdaf(0xdb7), vdae

    Begin block 0xdb3
    prev=[0xda0], succ=[]
    =================================
    0xdb3: vdb3(0x0) = CONST 
    0xdb6: REVERT vdb3(0x0), vdb3(0x0)

    Begin block 0xdb7
    prev=[0xda0], succ=[0x156c]
    =================================
    0xdb8: vdb8(0x0) = CONST 
    0xdbb: vdbb = SLOAD vdb8(0x0)
    0xdbc: vdbc(0x40) = CONST 
    0xdbe: vdbe = MLOAD vdbc(0x40)
    0xdbf: vdbf(0x1) = CONST 
    0xdc1: vdc1(0xa0) = CONST 
    0xdc3: vdc3(0x2) = CONST 
    0xdc5: vdc5(0x10000000000000000000000000000000000000000) = EXP vdc3(0x2), vdc1(0xa0)
    0xdc6: vdc6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdc5(0x10000000000000000000000000000000000000000), vdbf(0x1)
    0xdc9: vdc9 = AND vdbb, vdc6(0xffffffffffffffffffffffffffffffffffffffff)
    0xdcb: vdcb(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820) = CONST 
    0xded: LOG2 vdbe, vdb8(0x0), vdcb(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820), vdc9
    0xdee: vdee(0x0) = CONST 
    0xdf1: vdf1 = SLOAD vdee(0x0)
    0xdf2: vdf2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe07: ve07(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vdf2(0xffffffffffffffffffffffffffffffffffffffff)
    0xe08: ve08 = AND ve07(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdf1
    0xe0a: SSTORE vdee(0x0), ve08
    0xe0b: JUMP v3c1(0x156c)

    Begin block 0x156c
    prev=[0xdb7], succ=[]
    =================================
    0x156d: STOP 

}

function pause()() public {
    Begin block 0x3c8
    prev=[], succ=[0x3d0, 0x3d4]
    =================================
    0x3c9: v3c9 = CALLVALUE 
    0x3cb: v3cb = ISZERO v3c9
    0x3cc: v3cc(0x3d4) = CONST 
    0x3cf: JUMPI v3cc(0x3d4), v3cb

    Begin block 0x3d0
    prev=[0x3c8], succ=[]
    =================================
    0x3d0: v3d0(0x0) = CONST 
    0x3d3: REVERT v3d0(0x0), v3d0(0x0)

    Begin block 0x3d4
    prev=[0x3c8], succ=[0xe0c]
    =================================
    0x3d6: v3d6(0x158d) = CONST 
    0x3d9: v3d9(0xe0c) = CONST 
    0x3dc: JUMP v3d9(0xe0c)

    Begin block 0xe0c
    prev=[0x3d4], succ=[0xe1f, 0xe23]
    =================================
    0xe0d: ve0d(0x0) = CONST 
    0xe0f: ve0f = SLOAD ve0d(0x0)
    0xe10: ve10(0x1) = CONST 
    0xe12: ve12(0xa0) = CONST 
    0xe14: ve14(0x2) = CONST 
    0xe16: ve16(0x10000000000000000000000000000000000000000) = EXP ve14(0x2), ve12(0xa0)
    0xe17: ve17(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve16(0x10000000000000000000000000000000000000000), ve10(0x1)
    0xe18: ve18 = AND ve17(0xffffffffffffffffffffffffffffffffffffffff), ve0f
    0xe19: ve19 = CALLER 
    0xe1a: ve1a = EQ ve19, ve18
    0xe1b: ve1b(0xe23) = CONST 
    0xe1e: JUMPI ve1b(0xe23), ve1a

    Begin block 0xe1f
    prev=[0xe0c], succ=[]
    =================================
    0xe1f: ve1f(0x0) = CONST 
    0xe22: REVERT ve1f(0x0), ve1f(0x0)

    Begin block 0xe23
    prev=[0xe0c], succ=[0xe34, 0xe38]
    =================================
    0xe24: ve24(0x6) = CONST 
    0xe26: ve26 = SLOAD ve24(0x6)
    0xe27: ve27(0x100) = CONST 
    0xe2b: ve2b = DIV ve26, ve27(0x100)
    0xe2c: ve2c(0xff) = CONST 
    0xe2e: ve2e = AND ve2c(0xff), ve2b
    0xe2f: ve2f = ISZERO ve2e
    0xe30: ve30(0xe38) = CONST 
    0xe33: JUMPI ve30(0xe38), ve2f

    Begin block 0xe34
    prev=[0xe23], succ=[]
    =================================
    0xe34: ve34(0x0) = CONST 
    0xe37: REVERT ve34(0x0), ve34(0x0)

    Begin block 0xe38
    prev=[0xe23], succ=[0x158d]
    =================================
    0xe39: ve39(0x6) = CONST 
    0xe3c: ve3c = SLOAD ve39(0x6)
    0xe3d: ve3d(0xff00) = CONST 
    0xe40: ve40(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT ve3d(0xff00)
    0xe41: ve41 = AND ve40(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), ve3c
    0xe42: ve42(0x100) = CONST 
    0xe45: ve45 = OR ve42(0x100), ve41
    0xe47: SSTORE ve39(0x6), ve45
    0xe48: ve48(0x40) = CONST 
    0xe4a: ve4a = MLOAD ve48(0x40)
    0xe4b: ve4b(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625) = CONST 
    0xe6d: ve6d(0x0) = CONST 
    0xe70: LOG1 ve4a, ve6d(0x0), ve4b(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625)
    0xe71: JUMP v3d6(0x158d)

    Begin block 0x158d
    prev=[0xe38], succ=[]
    =================================
    0x158e: STOP 

}

function owner()() public {
    Begin block 0x3dd
    prev=[], succ=[0x3e5, 0x3e9]
    =================================
    0x3de: v3de = CALLVALUE 
    0x3e0: v3e0 = ISZERO v3de
    0x3e1: v3e1(0x3e9) = CONST 
    0x3e4: JUMPI v3e1(0x3e9), v3e0

    Begin block 0x3e5
    prev=[0x3dd], succ=[]
    =================================
    0x3e5: v3e5(0x0) = CONST 
    0x3e8: REVERT v3e5(0x0), v3e5(0x0)

    Begin block 0x3e9
    prev=[0x3dd], succ=[0xe72]
    =================================
    0x3eb: v3eb(0x15ae) = CONST 
    0x3ee: v3ee(0xe72) = CONST 
    0x3f1: JUMP v3ee(0xe72)

    Begin block 0xe72
    prev=[0x3e9], succ=[0x15ae]
    =================================
    0xe73: ve73(0x0) = CONST 
    0xe75: ve75 = SLOAD ve73(0x0)
    0xe76: ve76(0x1) = CONST 
    0xe78: ve78(0xa0) = CONST 
    0xe7a: ve7a(0x2) = CONST 
    0xe7c: ve7c(0x10000000000000000000000000000000000000000) = EXP ve7a(0x2), ve78(0xa0)
    0xe7d: ve7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve7c(0x10000000000000000000000000000000000000000), ve76(0x1)
    0xe7e: ve7e = AND ve7d(0xffffffffffffffffffffffffffffffffffffffff), ve75
    0xe80: JUMP v3eb(0x15ae)

    Begin block 0x15ae
    prev=[0xe72], succ=[]
    =================================
    0x15af: v15af(0x40) = CONST 
    0x15b2: v15b2 = MLOAD v15af(0x40)
    0x15b3: v15b3(0x1) = CONST 
    0x15b5: v15b5(0xa0) = CONST 
    0x15b7: v15b7(0x2) = CONST 
    0x15b9: v15b9(0x10000000000000000000000000000000000000000) = EXP v15b7(0x2), v15b5(0xa0)
    0x15ba: v15ba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15b9(0x10000000000000000000000000000000000000000), v15b3(0x1)
    0x15bd: v15bd = AND ve7e, v15ba(0xffffffffffffffffffffffffffffffffffffffff)
    0x15bf: MSTORE v15b2, v15bd
    0x15c0: v15c0 = MLOAD v15af(0x40)
    0x15c4: v15c4(0x0) = SUB v15b2, v15c0
    0x15c5: v15c5(0x20) = CONST 
    0x15c7: v15c7(0x20) = ADD v15c5(0x20), v15c4(0x0)
    0x15c9: RETURN v15c0, v15c7(0x20)

}

function setStorage(address)() public {
    Begin block 0x3f2
    prev=[], succ=[0x3fa, 0x3fe]
    =================================
    0x3f3: v3f3 = CALLVALUE 
    0x3f5: v3f5 = ISZERO v3f3
    0x3f6: v3f6(0x3fe) = CONST 
    0x3f9: JUMPI v3f6(0x3fe), v3f5

    Begin block 0x3fa
    prev=[0x3f2], succ=[]
    =================================
    0x3fa: v3fa(0x0) = CONST 
    0x3fd: REVERT v3fa(0x0), v3fa(0x0)

    Begin block 0x3fe
    prev=[0x3f2], succ=[0xe81]
    =================================
    0x400: v400(0x15e9) = CONST 
    0x403: v403(0x1) = CONST 
    0x405: v405(0xa0) = CONST 
    0x407: v407(0x2) = CONST 
    0x409: v409(0x10000000000000000000000000000000000000000) = EXP v407(0x2), v405(0xa0)
    0x40a: v40a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v409(0x10000000000000000000000000000000000000000), v403(0x1)
    0x40b: v40b(0x4) = CONST 
    0x40d: v40d = CALLDATALOAD v40b(0x4)
    0x40e: v40e = AND v40d, v40a(0xffffffffffffffffffffffffffffffffffffffff)
    0x40f: v40f(0xe81) = CONST 
    0x412: JUMP v40f(0xe81)

    Begin block 0xe81
    prev=[0x3fe], succ=[0xe94, 0xe98]
    =================================
    0xe82: ve82(0x0) = CONST 
    0xe84: ve84 = SLOAD ve82(0x0)
    0xe85: ve85(0x1) = CONST 
    0xe87: ve87(0xa0) = CONST 
    0xe89: ve89(0x2) = CONST 
    0xe8b: ve8b(0x10000000000000000000000000000000000000000) = EXP ve89(0x2), ve87(0xa0)
    0xe8c: ve8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve8b(0x10000000000000000000000000000000000000000), ve85(0x1)
    0xe8d: ve8d = AND ve8c(0xffffffffffffffffffffffffffffffffffffffff), ve84
    0xe8e: ve8e = CALLER 
    0xe8f: ve8f = EQ ve8e, ve8d
    0xe90: ve90(0xe98) = CONST 
    0xe93: JUMPI ve90(0xe98), ve8f

    Begin block 0xe94
    prev=[0xe81], succ=[]
    =================================
    0xe94: ve94(0x0) = CONST 
    0xe97: REVERT ve94(0x0), ve94(0x0)

    Begin block 0xe98
    prev=[0xe81], succ=[0xeba, 0xeac]
    =================================
    0xe99: ve99(0x2) = CONST 
    0xe9b: ve9b = SLOAD ve99(0x2)
    0xe9c: ve9c(0x1) = CONST 
    0xe9e: ve9e(0xa0) = CONST 
    0xea0: vea0(0x2) = CONST 
    0xea2: vea2(0x10000000000000000000000000000000000000000) = EXP vea0(0x2), ve9e(0xa0)
    0xea3: vea3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vea2(0x10000000000000000000000000000000000000000), ve9c(0x1)
    0xea4: vea4 = AND vea3(0xffffffffffffffffffffffffffffffffffffffff), ve9b
    0xea5: vea5 = CALLER 
    0xea6: vea6 = EQ vea5, vea4
    0xea8: vea8(0xeba) = CONST 
    0xeab: JUMPI vea8(0xeba), vea6

    Begin block 0xeba
    prev=[0xe98, 0xeac], succ=[0xec1, 0xec5]
    =================================
    0xeba_0x0: veba_0 = PHI vea6, veb9
    0xebb: vebb = ISZERO veba_0
    0xebc: vebc = ISZERO vebb
    0xebd: vebd(0xec5) = CONST 
    0xec0: JUMPI vebd(0xec5), vebc

    Begin block 0xec1
    prev=[0xeba], succ=[]
    =================================
    0xec1: vec1(0x0) = CONST 
    0xec4: REVERT vec1(0x0), vec1(0x0)

    Begin block 0xec5
    prev=[0xeba], succ=[0xed6, 0xeda]
    =================================
    0xec6: vec6(0x6) = CONST 
    0xec8: vec8 = SLOAD vec6(0x6)
    0xec9: vec9(0x100) = CONST 
    0xecd: vecd = DIV vec8, vec9(0x100)
    0xece: vece(0xff) = CONST 
    0xed0: ved0 = AND vece(0xff), vecd
    0xed1: ved1 = ISZERO ved0
    0xed2: ved2(0xeda) = CONST 
    0xed5: JUMPI ved2(0xeda), ved1

    Begin block 0xed6
    prev=[0xec5], succ=[]
    =================================
    0xed6: ved6(0x0) = CONST 
    0xed9: REVERT ved6(0x0), ved6(0x0)

    Begin block 0xeda
    prev=[0xec5], succ=[0x15e9]
    =================================
    0xedb: vedb(0x6) = CONST 
    0xede: vede = SLOAD vedb(0x6)
    0xedf: vedf(0x1) = CONST 
    0xee1: vee1(0xa0) = CONST 
    0xee3: vee3(0x2) = CONST 
    0xee5: vee5(0x10000000000000000000000000000000000000000) = EXP vee3(0x2), vee1(0xa0)
    0xee6: vee6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vee5(0x10000000000000000000000000000000000000000), vedf(0x1)
    0xee9: vee9 = AND v40e, vee6(0xffffffffffffffffffffffffffffffffffffffff)
    0xeea: veea(0x10000) = CONST 
    0xeee: veee = MUL veea(0x10000), vee9
    0xeef: veef(0xffffffffffffffffffffffffffffffffffffffff0000) = CONST 
    0xf06: vf06(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT veef(0xffffffffffffffffffffffffffffffffffffffff0000)
    0xf09: vf09 = AND vede, vf06(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff)
    0xf0d: vf0d = OR vf09, veee
    0xf0f: SSTORE vedb(0x6), vf0d
    0xf10: JUMP v400(0x15e9)

    Begin block 0x15e9
    prev=[0xeda], succ=[]
    =================================
    0x15ea: STOP 

    Begin block 0xeac
    prev=[0xe98], succ=[0xeba]
    =================================
    0xead: vead(0x2) = CONST 
    0xeaf: veaf = SLOAD vead(0x2)
    0xeb0: veb0(0x1) = CONST 
    0xeb2: veb2(0xa0) = CONST 
    0xeb4: veb4(0x2) = CONST 
    0xeb6: veb6(0x10000000000000000000000000000000000000000) = EXP veb4(0x2), veb2(0xa0)
    0xeb7: veb7(0xffffffffffffffffffffffffffffffffffffffff) = SUB veb6(0x10000000000000000000000000000000000000000), veb0(0x1)
    0xeb8: veb8 = AND veb7(0xffffffffffffffffffffffffffffffffffffffff), veaf
    0xeb9: veb9 = ISZERO veb8

}

function symbol()() public {
    Begin block 0x413
    prev=[], succ=[0x41b, 0x41f]
    =================================
    0x414: v414 = CALLVALUE 
    0x416: v416 = ISZERO v414
    0x417: v417(0x41f) = CONST 
    0x41a: JUMPI v417(0x41f), v416

    Begin block 0x41b
    prev=[0x413], succ=[]
    =================================
    0x41b: v41b(0x0) = CONST 
    0x41e: REVERT v41b(0x0), v41b(0x0)

    Begin block 0x41f
    prev=[0x413], succ=[0x16d0x413]
    =================================
    0x421: v421(0x16d) = CONST 
    0x424: v424(0xf11) = CONST 
    0x427: v427_0, v427_1 = CALLPRIVATE v424(0xf11), v421(0x16d)

    Begin block 0x16d0x413
    prev=[0x41f], succ=[0x18f0x413]
    =================================
    0x16e0x413: v41316e(0x40) = CONST 
    0x1710x413: v413171 = MLOAD v41316e(0x40)
    0x1720x413: v413172(0x20) = CONST 
    0x1760x413: MSTORE v413171, v413172(0x20)
    0x1780x413: v413178 = MLOAD v427_0
    0x17b0x413: v41317b = ADD v413171, v413172(0x20)
    0x17c0x413: MSTORE v41317b, v413178
    0x17e0x413: v41317e = MLOAD v427_0
    0x1850x413: v413185 = ADD v413171, v41316e(0x40)
    0x1880x413: v413188 = ADD v427_0, v413172(0x20)
    0x18d0x413: v41318d(0x0) = CONST 

    Begin block 0x18f0x413
    prev=[0x1980x413, 0x16d0x413], succ=[0x1a70x413, 0x1980x413]
    =================================
    0x18f0x413_0x0: v18f413_0 = PHI v4131a2, v41318d(0x0)
    0x1920x413: v413192 = LT v18f413_0, v41317e
    0x1930x413: v413193 = ISZERO v413192
    0x1940x413: v413194(0x1a7) = CONST 
    0x1970x413: JUMPI v413194(0x1a7), v413193

    Begin block 0x1a70x413
    prev=[0x18f0x413], succ=[0x1d40x413, 0x1bb0x413]
    =================================
    0x1b00x413: v4131b0 = ADD v41317e, v413185
    0x1b20x413: v4131b2(0x1f) = CONST 
    0x1b40x413: v4131b4 = AND v4131b2(0x1f), v41317e
    0x1b60x413: v4131b6 = ISZERO v4131b4
    0x1b70x413: v4131b7(0x1d4) = CONST 
    0x1ba0x413: JUMPI v4131b7(0x1d4), v4131b6

    Begin block 0x1d40x413
    prev=[0x1a70x413, 0x1bb0x413], succ=[]
    =================================
    0x1d40x413_0x1: v1d4413_1 = PHI v4131d1, v4131b0
    0x1da0x413: v4131da(0x40) = CONST 
    0x1dc0x413: v4131dc = MLOAD v4131da(0x40)
    0x1df0x413: v4131df = SUB v1d4413_1, v4131dc
    0x1e10x413: RETURN v4131dc, v4131df

    Begin block 0x1bb0x413
    prev=[0x1a70x413], succ=[0x1d40x413]
    =================================
    0x1bd0x413: v4131bd = SUB v4131b0, v4131b4
    0x1bf0x413: v4131bf = MLOAD v4131bd
    0x1c00x413: v4131c0(0x1) = CONST 
    0x1c30x413: v4131c3(0x20) = CONST 
    0x1c50x413: v4131c5 = SUB v4131c3(0x20), v4131b4
    0x1c60x413: v4131c6(0x100) = CONST 
    0x1c90x413: v4131c9 = EXP v4131c6(0x100), v4131c5
    0x1ca0x413: v4131ca = SUB v4131c9, v4131c0(0x1)
    0x1cb0x413: v4131cb = NOT v4131ca
    0x1cc0x413: v4131cc = AND v4131cb, v4131bf
    0x1ce0x413: MSTORE v4131bd, v4131cc
    0x1cf0x413: v4131cf(0x20) = CONST 
    0x1d10x413: v4131d1 = ADD v4131cf(0x20), v4131bd

    Begin block 0x1980x413
    prev=[0x18f0x413], succ=[0x18f0x413]
    =================================
    0x1980x413_0x0: v198413_0 = PHI v4131a2, v41318d(0x0)
    0x19a0x413: v41319a = ADD v198413_0, v413188
    0x19b0x413: v41319b = MLOAD v41319a
    0x19e0x413: v41319e = ADD v198413_0, v413185
    0x19f0x413: MSTORE v41319e, v41319b
    0x1a00x413: v4131a0(0x20) = CONST 
    0x1a20x413: v4131a2 = ADD v4131a0(0x20), v198413_0
    0x1a30x413: v4131a3(0x18f) = CONST 
    0x1a60x413: JUMP v4131a3(0x18f)

}

function transfer(address,uint256)() public {
    Begin block 0x428
    prev=[], succ=[0x430, 0x434]
    =================================
    0x429: v429 = CALLVALUE 
    0x42b: v42b = ISZERO v429
    0x42c: v42c(0x434) = CONST 
    0x42f: JUMPI v42c(0x434), v42b

    Begin block 0x430
    prev=[0x428], succ=[]
    =================================
    0x430: v430(0x0) = CONST 
    0x433: REVERT v430(0x0), v430(0x0)

    Begin block 0x434
    prev=[0x428], succ=[0xf6cB0x434]
    =================================
    0x436: v436(0x160a) = CONST 
    0x439: v439(0x1) = CONST 
    0x43b: v43b(0xa0) = CONST 
    0x43d: v43d(0x2) = CONST 
    0x43f: v43f(0x10000000000000000000000000000000000000000) = EXP v43d(0x2), v43b(0xa0)
    0x440: v440(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43f(0x10000000000000000000000000000000000000000), v439(0x1)
    0x441: v441(0x4) = CONST 
    0x443: v443 = CALLDATALOAD v441(0x4)
    0x444: v444 = AND v443, v440(0xffffffffffffffffffffffffffffffffffffffff)
    0x445: v445(0x24) = CONST 
    0x447: v447 = CALLDATALOAD v445(0x24)
    0x448: v448(0xf6c) = CONST 
    0x44b: JUMP v448(0xf6c)

    Begin block 0xf6cB0x434
    prev=[0x434], succ=[0xf91B0x434, 0xf83B0x434]
    =================================
    0xf6dS0x434: vf6dV434(0x2) = CONST 
    0xf6fS0x434: vf6fV434 = SLOAD vf6dV434(0x2)
    0xf70S0x434: vf70V434(0x0) = CONST 
    0xf73S0x434: vf73V434(0x1) = CONST 
    0xf75S0x434: vf75V434(0xa0) = CONST 
    0xf77S0x434: vf77V434(0x2) = CONST 
    0xf79S0x434: vf79V434(0x10000000000000000000000000000000000000000) = EXP vf77V434(0x2), vf75V434(0xa0)
    0xf7aS0x434: vf7aV434(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf79V434(0x10000000000000000000000000000000000000000), vf73V434(0x1)
    0xf7bS0x434: vf7bV434 = AND vf7aV434(0xffffffffffffffffffffffffffffffffffffffff), vf6fV434
    0xf7cS0x434: vf7cV434 = CALLER 
    0xf7dS0x434: vf7dV434 = EQ vf7cV434, vf7bV434
    0xf7fS0x434: vf7fV434(0xf91) = CONST 
    0xf82S0x434: JUMPI vf7fV434(0xf91), vf7dV434

    Begin block 0xf91B0x434
    prev=[0xf6cB0x434, 0xf83B0x434], succ=[0xf98B0x434, 0xf9cB0x434]
    =================================
    0xf91_0x0S0x434: vf91_0V434 = PHI vf7dV434, vf90V434
    0xf92S0x434: vf92V434 = ISZERO vf91_0V434
    0xf93S0x434: vf93V434 = ISZERO vf92V434
    0xf94S0x434: vf94V434(0xf9c) = CONST 
    0xf97S0x434: JUMPI vf94V434(0xf9c), vf93V434

    Begin block 0xf98B0x434
    prev=[0xf91B0x434], succ=[]
    =================================
    0xf98S0x434: vf98V434(0x0) = CONST 
    0xf9bS0x434: REVERT vf98V434(0x0), vf98V434(0x0)

    Begin block 0xf9cB0x434
    prev=[0xf91B0x434], succ=[0xfadB0x434, 0xfb1B0x434]
    =================================
    0xf9dS0x434: vf9dV434(0x6) = CONST 
    0xf9fS0x434: vf9fV434 = SLOAD vf9dV434(0x6)
    0xfa0S0x434: vfa0V434(0x100) = CONST 
    0xfa4S0x434: vfa4V434 = DIV vf9fV434, vfa0V434(0x100)
    0xfa5S0x434: vfa5V434(0xff) = CONST 
    0xfa7S0x434: vfa7V434 = AND vfa5V434(0xff), vfa4V434
    0xfa8S0x434: vfa8V434 = ISZERO vfa7V434
    0xfa9S0x434: vfa9V434(0xfb1) = CONST 
    0xfacS0x434: JUMPI vfa9V434(0xfb1), vfa8V434

    Begin block 0xfadB0x434
    prev=[0xf9cB0x434], succ=[]
    =================================
    0xfadS0x434: vfadV434(0x0) = CONST 
    0xfb0S0x434: REVERT vfadV434(0x0), vfadV434(0x0)

    Begin block 0xfb1B0x434
    prev=[0xf9cB0x434], succ=[0x1038B0x434, 0x6580xf6cB0x434]
    =================================
    0xfb2S0x434: vfb2V434(0x6) = CONST 
    0xfb4S0x434: vfb4V434 = SLOAD vfb2V434(0x6)
    0xfb5S0x434: vfb5V434(0x40) = CONST 
    0xfb8S0x434: vfb8V434 = MLOAD vfb5V434(0x40)
    0xfb9S0x434: vfb9V434(0xbeabacc800000000000000000000000000000000000000000000000000000000) = CONST 
    0xfdbS0x434: MSTORE vfb8V434, vfb9V434(0xbeabacc800000000000000000000000000000000000000000000000000000000)
    0xfdcS0x434: vfdcV434(0x1) = CONST 
    0xfdeS0x434: vfdeV434(0xa0) = CONST 
    0xfe0S0x434: vfe0V434(0x2) = CONST 
    0xfe2S0x434: vfe2V434(0x10000000000000000000000000000000000000000) = EXP vfe0V434(0x2), vfdeV434(0xa0)
    0xfe3S0x434: vfe3V434(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfe2V434(0x10000000000000000000000000000000000000000), vfdcV434(0x1)
    0xfe4S0x434: vfe4V434(0x10000) = CONST 
    0xfeaS0x434: vfeaV434 = DIV vfb4V434, vfe4V434(0x10000)
    0xfecS0x434: vfecV434 = AND vfe3V434(0xffffffffffffffffffffffffffffffffffffffff), vfeaV434
    0xfedS0x434: vfedV434(0x4) = CONST 
    0xff0S0x434: vff0V434 = ADD vfb8V434, vfedV434(0x4)
    0xff1S0x434: MSTORE vff0V434, vfecV434
    0xff4S0x434: vff4V434 = AND v444, vfe3V434(0xffffffffffffffffffffffffffffffffffffffff)
    0xff5S0x434: vff5V434(0x24) = CONST 
    0xff8S0x434: vff8V434 = ADD vfb8V434, vff5V434(0x24)
    0xff9S0x434: MSTORE vff8V434, vff4V434
    0xffaS0x434: vffaV434(0x44) = CONST 
    0xffdS0x434: vffdV434 = ADD vfb8V434, vffaV434(0x44)
    0x1000S0x434: MSTORE vffdV434, v447
    0x1001S0x434: v1001V434 = MLOAD vfb5V434(0x40)
    0x1002S0x434: v1002V434(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x1018S0x434: v1018V434(0xbeabacc8) = CONST 
    0x101eS0x434: v101eV434(0x64) = CONST 
    0x1022S0x434: v1022V434 = ADD vfb8V434, v101eV434(0x64)
    0x1024S0x434: v1024V434(0x20) = CONST 
    0x102bS0x434: v102bV434(0x0) = SUB vfb8V434, v1001V434
    0x102cS0x434: v102cV434(0x64) = ADD v102bV434(0x0), v101eV434(0x64)
    0x1030S0x434: v1030V434 = EXTCODESIZE v1002V434(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x1031S0x434: v1031V434 = ISZERO v1030V434
    0x1033S0x434: v1033V434 = ISZERO v1031V434
    0x1034S0x434: v1034V434(0x658) = CONST 
    0x1037S0x434: JUMPI v1034V434(0x658), v1033V434

    Begin block 0x1038B0x434
    prev=[0xfb1B0x434], succ=[]
    =================================
    0x1038S0x434: v1038V434(0x0) = CONST 
    0x103bS0x434: REVERT v1038V434(0x0), v1038V434(0x0)

    Begin block 0x6580xf6cB0x434
    prev=[0xfb1B0x434], succ=[0x6630xf6cB0x434, 0x66c0xf6cB0x434]
    =================================
    0x65a0xf6cS0x434: vf6c65aV434 = GAS 
    0x65b0xf6cS0x434: vf6c65bV434 = DELEGATECALL vf6c65aV434, v1002V434(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v1001V434, v102cV434(0x64), v1001V434, v1024V434(0x20)
    0x65c0xf6cS0x434: vf6c65cV434 = ISZERO vf6c65bV434
    0x65e0xf6cS0x434: vf6c65eV434 = ISZERO vf6c65cV434
    0x65f0xf6cS0x434: vf6c65fV434(0x66c) = CONST 
    0x6620xf6cS0x434: JUMPI vf6c65fV434(0x66c), vf6c65eV434

    Begin block 0x6630xf6cB0x434
    prev=[0x6580xf6cB0x434], succ=[]
    =================================
    0x6630xf6cS0x434: vf6c663V434 = RETURNDATASIZE 
    0x6640xf6cS0x434: vf6c664V434(0x0) = CONST 
    0x6670xf6cS0x434: RETURNDATACOPY vf6c664V434(0x0), vf6c664V434(0x0), vf6c663V434
    0x6680xf6cS0x434: vf6c668V434 = RETURNDATASIZE 
    0x6690xf6cS0x434: vf6c669V434(0x0) = CONST 
    0x66b0xf6cS0x434: REVERT vf6c669V434(0x0), vf6c668V434

    Begin block 0x66c0xf6cB0x434
    prev=[0x6580xf6cB0x434], succ=[0x67e0xf6cB0x434, 0x6820xf6cB0x434]
    =================================
    0x6710xf6cS0x434: vf6c671V434(0x40) = CONST 
    0x6730xf6cS0x434: vf6c673V434 = MLOAD vf6c671V434(0x40)
    0x6740xf6cS0x434: vf6c674V434 = RETURNDATASIZE 
    0x6750xf6cS0x434: vf6c675V434(0x20) = CONST 
    0x6780xf6cS0x434: vf6c678V434 = LT vf6c674V434, vf6c675V434(0x20)
    0x6790xf6cS0x434: vf6c679V434 = ISZERO vf6c678V434
    0x67a0xf6cS0x434: vf6c67aV434(0x682) = CONST 
    0x67d0xf6cS0x434: JUMPI vf6c67aV434(0x682), vf6c679V434

    Begin block 0x67e0xf6cB0x434
    prev=[0x66c0xf6cB0x434], succ=[]
    =================================
    0x67e0xf6cS0x434: vf6c67eV434(0x0) = CONST 
    0x6810xf6cS0x434: REVERT vf6c67eV434(0x0), vf6c67eV434(0x0)

    Begin block 0x6820xf6cB0x434
    prev=[0x66c0xf6cB0x434], succ=[0x160a]
    =================================
    0x6840xf6cS0x434: vf6c684V434 = MLOAD vf6c673V434
    0x68a0xf6cS0x434: JUMP v436(0x160a)

    Begin block 0x160a
    prev=[0x6820xf6cB0x434], succ=[]
    =================================
    0x160b: v160b(0x40) = CONST 
    0x160e: v160e = MLOAD v160b(0x40)
    0x1610: v1610 = ISZERO vf6c684V434
    0x1611: v1611 = ISZERO v1610
    0x1613: MSTORE v160e, v1611
    0x1614: v1614 = MLOAD v160b(0x40)
    0x1618: v1618(0x0) = SUB v160e, v1614
    0x1619: v1619(0x20) = CONST 
    0x161b: v161b(0x20) = ADD v1619(0x20), v1618(0x0)
    0x161d: RETURN v1614, v161b(0x20)

    Begin block 0xf83B0x434
    prev=[0xf6cB0x434], succ=[0xf91B0x434]
    =================================
    0xf84S0x434: vf84V434(0x2) = CONST 
    0xf86S0x434: vf86V434 = SLOAD vf84V434(0x2)
    0xf87S0x434: vf87V434(0x1) = CONST 
    0xf89S0x434: vf89V434(0xa0) = CONST 
    0xf8bS0x434: vf8bV434(0x2) = CONST 
    0xf8dS0x434: vf8dV434(0x10000000000000000000000000000000000000000) = EXP vf8bV434(0x2), vf89V434(0xa0)
    0xf8eS0x434: vf8eV434(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf8dV434(0x10000000000000000000000000000000000000000), vf87V434(0x1)
    0xf8fS0x434: vf8fV434 = AND vf8eV434(0xffffffffffffffffffffffffffffffffffffffff), vf86V434
    0xf90S0x434: vf90V434 = ISZERO vf8fV434

}

function predecessor()() public {
    Begin block 0x44c
    prev=[], succ=[0x454, 0x458]
    =================================
    0x44d: v44d = CALLVALUE 
    0x44f: v44f = ISZERO v44d
    0x450: v450(0x458) = CONST 
    0x453: JUMPI v450(0x458), v44f

    Begin block 0x454
    prev=[0x44c], succ=[]
    =================================
    0x454: v454(0x0) = CONST 
    0x457: REVERT v454(0x0), v454(0x0)

    Begin block 0x458
    prev=[0x44c], succ=[0x103c]
    =================================
    0x45a: v45a(0x163d) = CONST 
    0x45d: v45d(0x103c) = CONST 
    0x460: JUMP v45d(0x103c)

    Begin block 0x103c
    prev=[0x458], succ=[0x163d]
    =================================
    0x103d: v103d(0x1) = CONST 
    0x103f: v103f = SLOAD v103d(0x1)
    0x1040: v1040(0x1) = CONST 
    0x1042: v1042(0xa0) = CONST 
    0x1044: v1044(0x2) = CONST 
    0x1046: v1046(0x10000000000000000000000000000000000000000) = EXP v1044(0x2), v1042(0xa0)
    0x1047: v1047(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1046(0x10000000000000000000000000000000000000000), v1040(0x1)
    0x1048: v1048 = AND v1047(0xffffffffffffffffffffffffffffffffffffffff), v103f
    0x104a: JUMP v45a(0x163d)

    Begin block 0x163d
    prev=[0x103c], succ=[]
    =================================
    0x163e: v163e(0x40) = CONST 
    0x1641: v1641 = MLOAD v163e(0x40)
    0x1642: v1642(0x1) = CONST 
    0x1644: v1644(0xa0) = CONST 
    0x1646: v1646(0x2) = CONST 
    0x1648: v1648(0x10000000000000000000000000000000000000000) = EXP v1646(0x2), v1644(0xa0)
    0x1649: v1649(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1648(0x10000000000000000000000000000000000000000), v1642(0x1)
    0x164c: v164c = AND v1048, v1649(0xffffffffffffffffffffffffffffffffffffffff)
    0x164e: MSTORE v1641, v164c
    0x164f: v164f = MLOAD v163e(0x40)
    0x1653: v1653(0x0) = SUB v1641, v164f
    0x1654: v1654(0x20) = CONST 
    0x1656: v1656(0x20) = ADD v1654(0x20), v1653(0x0)
    0x1658: RETURN v164f, v1656(0x20)

}

function isDeprecated()() public {
    Begin block 0x461
    prev=[], succ=[0x469, 0x46d]
    =================================
    0x462: v462 = CALLVALUE 
    0x464: v464 = ISZERO v462
    0x465: v465(0x46d) = CONST 
    0x468: JUMPI v465(0x46d), v464

    Begin block 0x469
    prev=[0x461], succ=[]
    =================================
    0x469: v469(0x0) = CONST 
    0x46c: REVERT v469(0x0), v469(0x0)

    Begin block 0x46d
    prev=[0x461], succ=[0x104b]
    =================================
    0x46f: v46f(0x1678) = CONST 
    0x472: v472(0x104b) = CONST 
    0x475: JUMP v472(0x104b)

    Begin block 0x104b
    prev=[0x46d], succ=[0x1678]
    =================================
    0x104c: v104c(0x2) = CONST 
    0x104e: v104e = SLOAD v104c(0x2)
    0x104f: v104f(0x1) = CONST 
    0x1051: v1051(0xa0) = CONST 
    0x1053: v1053(0x2) = CONST 
    0x1055: v1055(0x10000000000000000000000000000000000000000) = EXP v1053(0x2), v1051(0xa0)
    0x1056: v1056(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1055(0x10000000000000000000000000000000000000000), v104f(0x1)
    0x1057: v1057 = AND v1056(0xffffffffffffffffffffffffffffffffffffffff), v104e
    0x1058: v1058 = ISZERO v1057
    0x1059: v1059 = ISZERO v1058
    0x105b: JUMP v46f(0x1678)

    Begin block 0x1678
    prev=[0x104b], succ=[]
    =================================
    0x1679: v1679(0x40) = CONST 
    0x167c: v167c = MLOAD v1679(0x40)
    0x167e: v167e = ISZERO v1059
    0x167f: v167f = ISZERO v167e
    0x1681: MSTORE v167c, v167f
    0x1682: v1682 = MLOAD v1679(0x40)
    0x1686: v1686(0x0) = SUB v167c, v1682
    0x1687: v1687(0x20) = CONST 
    0x1689: v1689(0x20) = ADD v1687(0x20), v1686(0x0)
    0x168b: RETURN v1682, v1689(0x20)

}

function increaseApproval(address,uint256)() public {
    Begin block 0x476
    prev=[], succ=[0x47e, 0x482]
    =================================
    0x477: v477 = CALLVALUE 
    0x479: v479 = ISZERO v477
    0x47a: v47a(0x482) = CONST 
    0x47d: JUMPI v47a(0x482), v479

    Begin block 0x47e
    prev=[0x476], succ=[]
    =================================
    0x47e: v47e(0x0) = CONST 
    0x481: REVERT v47e(0x0), v47e(0x0)

    Begin block 0x482
    prev=[0x476], succ=[0x105cB0x482]
    =================================
    0x484: v484(0x16ab) = CONST 
    0x487: v487(0x1) = CONST 
    0x489: v489(0xa0) = CONST 
    0x48b: v48b(0x2) = CONST 
    0x48d: v48d(0x10000000000000000000000000000000000000000) = EXP v48b(0x2), v489(0xa0)
    0x48e: v48e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48d(0x10000000000000000000000000000000000000000), v487(0x1)
    0x48f: v48f(0x4) = CONST 
    0x491: v491 = CALLDATALOAD v48f(0x4)
    0x492: v492 = AND v491, v48e(0xffffffffffffffffffffffffffffffffffffffff)
    0x493: v493(0x24) = CONST 
    0x495: v495 = CALLDATALOAD v493(0x24)
    0x496: v496(0x105c) = CONST 
    0x499: JUMP v496(0x105c)

    Begin block 0x105cB0x482
    prev=[0x482], succ=[0x1081B0x482, 0x1073B0x482]
    =================================
    0x105dS0x482: v105dV482(0x2) = CONST 
    0x105fS0x482: v105fV482 = SLOAD v105dV482(0x2)
    0x1060S0x482: v1060V482(0x0) = CONST 
    0x1063S0x482: v1063V482(0x1) = CONST 
    0x1065S0x482: v1065V482(0xa0) = CONST 
    0x1067S0x482: v1067V482(0x2) = CONST 
    0x1069S0x482: v1069V482(0x10000000000000000000000000000000000000000) = EXP v1067V482(0x2), v1065V482(0xa0)
    0x106aS0x482: v106aV482(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1069V482(0x10000000000000000000000000000000000000000), v1063V482(0x1)
    0x106bS0x482: v106bV482 = AND v106aV482(0xffffffffffffffffffffffffffffffffffffffff), v105fV482
    0x106cS0x482: v106cV482 = CALLER 
    0x106dS0x482: v106dV482 = EQ v106cV482, v106bV482
    0x106fS0x482: v106fV482(0x1081) = CONST 
    0x1072S0x482: JUMPI v106fV482(0x1081), v106dV482

    Begin block 0x1081B0x482
    prev=[0x105cB0x482, 0x1073B0x482], succ=[0x1088B0x482, 0x108cB0x482]
    =================================
    0x1081_0x0S0x482: v1081_0V482 = PHI v106dV482, v1080V482
    0x1082S0x482: v1082V482 = ISZERO v1081_0V482
    0x1083S0x482: v1083V482 = ISZERO v1082V482
    0x1084S0x482: v1084V482(0x108c) = CONST 
    0x1087S0x482: JUMPI v1084V482(0x108c), v1083V482

    Begin block 0x1088B0x482
    prev=[0x1081B0x482], succ=[]
    =================================
    0x1088S0x482: v1088V482(0x0) = CONST 
    0x108bS0x482: REVERT v1088V482(0x0), v1088V482(0x0)

    Begin block 0x108cB0x482
    prev=[0x1081B0x482], succ=[0x109dB0x482, 0x10a1B0x482]
    =================================
    0x108dS0x482: v108dV482(0x6) = CONST 
    0x108fS0x482: v108fV482 = SLOAD v108dV482(0x6)
    0x1090S0x482: v1090V482(0x100) = CONST 
    0x1094S0x482: v1094V482 = DIV v108fV482, v1090V482(0x100)
    0x1095S0x482: v1095V482(0xff) = CONST 
    0x1097S0x482: v1097V482 = AND v1095V482(0xff), v1094V482
    0x1098S0x482: v1098V482 = ISZERO v1097V482
    0x1099S0x482: v1099V482(0x10a1) = CONST 
    0x109cS0x482: JUMPI v1099V482(0x10a1), v1098V482

    Begin block 0x109dB0x482
    prev=[0x108cB0x482], succ=[]
    =================================
    0x109dS0x482: v109dV482(0x0) = CONST 
    0x10a0S0x482: REVERT v109dV482(0x0), v109dV482(0x0)

    Begin block 0x10a1B0x482
    prev=[0x108cB0x482], succ=[0x1128B0x482, 0x6580x105cB0x482]
    =================================
    0x10a2S0x482: v10a2V482(0x6) = CONST 
    0x10a4S0x482: v10a4V482 = SLOAD v10a2V482(0x6)
    0x10a5S0x482: v10a5V482(0x40) = CONST 
    0x10a8S0x482: v10a8V482 = MLOAD v10a5V482(0x40)
    0x10a9S0x482: v10a9V482(0xbcdd612100000000000000000000000000000000000000000000000000000000) = CONST 
    0x10cbS0x482: MSTORE v10a8V482, v10a9V482(0xbcdd612100000000000000000000000000000000000000000000000000000000)
    0x10ccS0x482: v10ccV482(0x1) = CONST 
    0x10ceS0x482: v10ceV482(0xa0) = CONST 
    0x10d0S0x482: v10d0V482(0x2) = CONST 
    0x10d2S0x482: v10d2V482(0x10000000000000000000000000000000000000000) = EXP v10d0V482(0x2), v10ceV482(0xa0)
    0x10d3S0x482: v10d3V482(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10d2V482(0x10000000000000000000000000000000000000000), v10ccV482(0x1)
    0x10d4S0x482: v10d4V482(0x10000) = CONST 
    0x10daS0x482: v10daV482 = DIV v10a4V482, v10d4V482(0x10000)
    0x10dcS0x482: v10dcV482 = AND v10d3V482(0xffffffffffffffffffffffffffffffffffffffff), v10daV482
    0x10ddS0x482: v10ddV482(0x4) = CONST 
    0x10e0S0x482: v10e0V482 = ADD v10a8V482, v10ddV482(0x4)
    0x10e1S0x482: MSTORE v10e0V482, v10dcV482
    0x10e4S0x482: v10e4V482 = AND v492, v10d3V482(0xffffffffffffffffffffffffffffffffffffffff)
    0x10e5S0x482: v10e5V482(0x24) = CONST 
    0x10e8S0x482: v10e8V482 = ADD v10a8V482, v10e5V482(0x24)
    0x10e9S0x482: MSTORE v10e8V482, v10e4V482
    0x10eaS0x482: v10eaV482(0x44) = CONST 
    0x10edS0x482: v10edV482 = ADD v10a8V482, v10eaV482(0x44)
    0x10f0S0x482: MSTORE v10edV482, v495
    0x10f1S0x482: v10f1V482 = MLOAD v10a5V482(0x40)
    0x10f2S0x482: v10f2V482(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x1108S0x482: v1108V482(0xbcdd6121) = CONST 
    0x110eS0x482: v110eV482(0x64) = CONST 
    0x1112S0x482: v1112V482 = ADD v10a8V482, v110eV482(0x64)
    0x1114S0x482: v1114V482(0x20) = CONST 
    0x111bS0x482: v111bV482(0x0) = SUB v10a8V482, v10f1V482
    0x111cS0x482: v111cV482(0x64) = ADD v111bV482(0x0), v110eV482(0x64)
    0x1120S0x482: v1120V482 = EXTCODESIZE v10f2V482(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x1121S0x482: v1121V482 = ISZERO v1120V482
    0x1123S0x482: v1123V482 = ISZERO v1121V482
    0x1124S0x482: v1124V482(0x658) = CONST 
    0x1127S0x482: JUMPI v1124V482(0x658), v1123V482

    Begin block 0x1128B0x482
    prev=[0x10a1B0x482], succ=[]
    =================================
    0x1128S0x482: v1128V482(0x0) = CONST 
    0x112bS0x482: REVERT v1128V482(0x0), v1128V482(0x0)

    Begin block 0x6580x105cB0x482
    prev=[0x10a1B0x482], succ=[0x6630x105cB0x482, 0x66c0x105cB0x482]
    =================================
    0x65a0x105cS0x482: v105c65aV482 = GAS 
    0x65b0x105cS0x482: v105c65bV482 = DELEGATECALL v105c65aV482, v10f2V482(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v10f1V482, v111cV482(0x64), v10f1V482, v1114V482(0x20)
    0x65c0x105cS0x482: v105c65cV482 = ISZERO v105c65bV482
    0x65e0x105cS0x482: v105c65eV482 = ISZERO v105c65cV482
    0x65f0x105cS0x482: v105c65fV482(0x66c) = CONST 
    0x6620x105cS0x482: JUMPI v105c65fV482(0x66c), v105c65eV482

    Begin block 0x6630x105cB0x482
    prev=[0x6580x105cB0x482], succ=[]
    =================================
    0x6630x105cS0x482: v105c663V482 = RETURNDATASIZE 
    0x6640x105cS0x482: v105c664V482(0x0) = CONST 
    0x6670x105cS0x482: RETURNDATACOPY v105c664V482(0x0), v105c664V482(0x0), v105c663V482
    0x6680x105cS0x482: v105c668V482 = RETURNDATASIZE 
    0x6690x105cS0x482: v105c669V482(0x0) = CONST 
    0x66b0x105cS0x482: REVERT v105c669V482(0x0), v105c668V482

    Begin block 0x66c0x105cB0x482
    prev=[0x6580x105cB0x482], succ=[0x67e0x105cB0x482, 0x6820x105cB0x482]
    =================================
    0x6710x105cS0x482: v105c671V482(0x40) = CONST 
    0x6730x105cS0x482: v105c673V482 = MLOAD v105c671V482(0x40)
    0x6740x105cS0x482: v105c674V482 = RETURNDATASIZE 
    0x6750x105cS0x482: v105c675V482(0x20) = CONST 
    0x6780x105cS0x482: v105c678V482 = LT v105c674V482, v105c675V482(0x20)
    0x6790x105cS0x482: v105c679V482 = ISZERO v105c678V482
    0x67a0x105cS0x482: v105c67aV482(0x682) = CONST 
    0x67d0x105cS0x482: JUMPI v105c67aV482(0x682), v105c679V482

    Begin block 0x67e0x105cB0x482
    prev=[0x66c0x105cB0x482], succ=[]
    =================================
    0x67e0x105cS0x482: v105c67eV482(0x0) = CONST 
    0x6810x105cS0x482: REVERT v105c67eV482(0x0), v105c67eV482(0x0)

    Begin block 0x6820x105cB0x482
    prev=[0x66c0x105cB0x482], succ=[0x16ab]
    =================================
    0x6840x105cS0x482: v105c684V482 = MLOAD v105c673V482
    0x68a0x105cS0x482: JUMP v484(0x16ab)

    Begin block 0x16ab
    prev=[0x6820x105cB0x482], succ=[]
    =================================
    0x16ac: v16ac(0x40) = CONST 
    0x16af: v16af = MLOAD v16ac(0x40)
    0x16b1: v16b1 = ISZERO v105c684V482
    0x16b2: v16b2 = ISZERO v16b1
    0x16b4: MSTORE v16af, v16b2
    0x16b5: v16b5 = MLOAD v16ac(0x40)
    0x16b9: v16b9(0x0) = SUB v16af, v16b5
    0x16ba: v16ba(0x20) = CONST 
    0x16bc: v16bc(0x20) = ADD v16ba(0x20), v16b9(0x0)
    0x16be: RETURN v16b5, v16bc(0x20)

    Begin block 0x1073B0x482
    prev=[0x105cB0x482], succ=[0x1081B0x482]
    =================================
    0x1074S0x482: v1074V482(0x2) = CONST 
    0x1076S0x482: v1076V482 = SLOAD v1074V482(0x2)
    0x1077S0x482: v1077V482(0x1) = CONST 
    0x1079S0x482: v1079V482(0xa0) = CONST 
    0x107bS0x482: v107bV482(0x2) = CONST 
    0x107dS0x482: v107dV482(0x10000000000000000000000000000000000000000) = EXP v107bV482(0x2), v1079V482(0xa0)
    0x107eS0x482: v107eV482(0xffffffffffffffffffffffffffffffffffffffff) = SUB v107dV482(0x10000000000000000000000000000000000000000), v1077V482(0x1)
    0x107fS0x482: v107fV482 = AND v107eV482(0xffffffffffffffffffffffffffffffffffffffff), v1076V482
    0x1080S0x482: v1080V482 = ISZERO v107fV482

}

function allowance(address,address)() public {
    Begin block 0x49a
    prev=[], succ=[0x4a2, 0x4a6]
    =================================
    0x49b: v49b = CALLVALUE 
    0x49d: v49d = ISZERO v49b
    0x49e: v49e(0x4a6) = CONST 
    0x4a1: JUMPI v49e(0x4a6), v49d

    Begin block 0x4a2
    prev=[0x49a], succ=[]
    =================================
    0x4a2: v4a2(0x0) = CONST 
    0x4a5: REVERT v4a2(0x0), v4a2(0x0)

    Begin block 0x4a6
    prev=[0x49a], succ=[0x112cB0x4a6]
    =================================
    0x4a8: v4a8(0x16de) = CONST 
    0x4ab: v4ab(0x1) = CONST 
    0x4ad: v4ad(0xa0) = CONST 
    0x4af: v4af(0x2) = CONST 
    0x4b1: v4b1(0x10000000000000000000000000000000000000000) = EXP v4af(0x2), v4ad(0xa0)
    0x4b2: v4b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b1(0x10000000000000000000000000000000000000000), v4ab(0x1)
    0x4b3: v4b3(0x4) = CONST 
    0x4b5: v4b5 = CALLDATALOAD v4b3(0x4)
    0x4b7: v4b7 = AND v4b2(0xffffffffffffffffffffffffffffffffffffffff), v4b5
    0x4b9: v4b9(0x24) = CONST 
    0x4bb: v4bb = CALLDATALOAD v4b9(0x24)
    0x4bc: v4bc = AND v4bb, v4b2(0xffffffffffffffffffffffffffffffffffffffff)
    0x4bd: v4bd(0x112c) = CONST 
    0x4c0: JUMP v4bd(0x112c)

    Begin block 0x112cB0x4a6
    prev=[0x4a6], succ=[0x11b8B0x4a6, 0x6580x112cB0x4a6]
    =================================
    0x112dS0x4a6: v112dV4a6(0x6) = CONST 
    0x112fS0x4a6: v112fV4a6 = SLOAD v112dV4a6(0x6)
    0x1130S0x4a6: v1130V4a6(0x40) = CONST 
    0x1133S0x4a6: v1133V4a6 = MLOAD v1130V4a6(0x40)
    0x1134S0x4a6: v1134V4a6(0x927da10500000000000000000000000000000000000000000000000000000000) = CONST 
    0x1156S0x4a6: MSTORE v1133V4a6, v1134V4a6(0x927da10500000000000000000000000000000000000000000000000000000000)
    0x1157S0x4a6: v1157V4a6(0x1) = CONST 
    0x1159S0x4a6: v1159V4a6(0xa0) = CONST 
    0x115bS0x4a6: v115bV4a6(0x2) = CONST 
    0x115dS0x4a6: v115dV4a6(0x10000000000000000000000000000000000000000) = EXP v115bV4a6(0x2), v1159V4a6(0xa0)
    0x115eS0x4a6: v115eV4a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v115dV4a6(0x10000000000000000000000000000000000000000), v1157V4a6(0x1)
    0x115fS0x4a6: v115fV4a6(0x10000) = CONST 
    0x1165S0x4a6: v1165V4a6 = DIV v112fV4a6, v115fV4a6(0x10000)
    0x1167S0x4a6: v1167V4a6 = AND v115eV4a6(0xffffffffffffffffffffffffffffffffffffffff), v1165V4a6
    0x1168S0x4a6: v1168V4a6(0x4) = CONST 
    0x116bS0x4a6: v116bV4a6 = ADD v1133V4a6, v1168V4a6(0x4)
    0x116cS0x4a6: MSTORE v116bV4a6, v1167V4a6
    0x116fS0x4a6: v116fV4a6 = AND v115eV4a6(0xffffffffffffffffffffffffffffffffffffffff), v4b7
    0x1170S0x4a6: v1170V4a6(0x24) = CONST 
    0x1173S0x4a6: v1173V4a6 = ADD v1133V4a6, v1170V4a6(0x24)
    0x1174S0x4a6: MSTORE v1173V4a6, v116fV4a6
    0x1177S0x4a6: v1177V4a6 = AND v4bc, v115eV4a6(0xffffffffffffffffffffffffffffffffffffffff)
    0x1178S0x4a6: v1178V4a6(0x44) = CONST 
    0x117bS0x4a6: v117bV4a6 = ADD v1133V4a6, v1178V4a6(0x44)
    0x117cS0x4a6: MSTORE v117bV4a6, v1177V4a6
    0x117dS0x4a6: v117dV4a6 = MLOAD v1130V4a6(0x40)
    0x117eS0x4a6: v117eV4a6(0x0) = CONST 
    0x1181S0x4a6: v1181V4a6(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x1197S0x4a6: v1197V4a6(0x927da105) = CONST 
    0x119dS0x4a6: v119dV4a6(0x64) = CONST 
    0x11a1S0x4a6: v11a1V4a6 = ADD v1133V4a6, v119dV4a6(0x64)
    0x11a3S0x4a6: v11a3V4a6(0x20) = CONST 
    0x11abS0x4a6: v11abV4a6(0x0) = SUB v1133V4a6, v117dV4a6
    0x11acS0x4a6: v11acV4a6(0x64) = ADD v11abV4a6(0x0), v119dV4a6(0x64)
    0x11b0S0x4a6: v11b0V4a6 = EXTCODESIZE v1181V4a6(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x11b1S0x4a6: v11b1V4a6 = ISZERO v11b0V4a6
    0x11b3S0x4a6: v11b3V4a6 = ISZERO v11b1V4a6
    0x11b4S0x4a6: v11b4V4a6(0x658) = CONST 
    0x11b7S0x4a6: JUMPI v11b4V4a6(0x658), v11b3V4a6

    Begin block 0x11b8B0x4a6
    prev=[0x112cB0x4a6], succ=[]
    =================================
    0x11b8S0x4a6: v11b8V4a6(0x0) = CONST 
    0x11bbS0x4a6: REVERT v11b8V4a6(0x0), v11b8V4a6(0x0)

    Begin block 0x6580x112cB0x4a6
    prev=[0x112cB0x4a6], succ=[0x6630x112cB0x4a6, 0x66c0x112cB0x4a6]
    =================================
    0x65a0x112cS0x4a6: v112c65aV4a6 = GAS 
    0x65b0x112cS0x4a6: v112c65bV4a6 = DELEGATECALL v112c65aV4a6, v1181V4a6(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v117dV4a6, v11acV4a6(0x64), v117dV4a6, v11a3V4a6(0x20)
    0x65c0x112cS0x4a6: v112c65cV4a6 = ISZERO v112c65bV4a6
    0x65e0x112cS0x4a6: v112c65eV4a6 = ISZERO v112c65cV4a6
    0x65f0x112cS0x4a6: v112c65fV4a6(0x66c) = CONST 
    0x6620x112cS0x4a6: JUMPI v112c65fV4a6(0x66c), v112c65eV4a6

    Begin block 0x6630x112cB0x4a6
    prev=[0x6580x112cB0x4a6], succ=[]
    =================================
    0x6630x112cS0x4a6: v112c663V4a6 = RETURNDATASIZE 
    0x6640x112cS0x4a6: v112c664V4a6(0x0) = CONST 
    0x6670x112cS0x4a6: RETURNDATACOPY v112c664V4a6(0x0), v112c664V4a6(0x0), v112c663V4a6
    0x6680x112cS0x4a6: v112c668V4a6 = RETURNDATASIZE 
    0x6690x112cS0x4a6: v112c669V4a6(0x0) = CONST 
    0x66b0x112cS0x4a6: REVERT v112c669V4a6(0x0), v112c668V4a6

    Begin block 0x66c0x112cB0x4a6
    prev=[0x6580x112cB0x4a6], succ=[0x67e0x112cB0x4a6, 0x6820x112cB0x4a6]
    =================================
    0x6710x112cS0x4a6: v112c671V4a6(0x40) = CONST 
    0x6730x112cS0x4a6: v112c673V4a6 = MLOAD v112c671V4a6(0x40)
    0x6740x112cS0x4a6: v112c674V4a6 = RETURNDATASIZE 
    0x6750x112cS0x4a6: v112c675V4a6(0x20) = CONST 
    0x6780x112cS0x4a6: v112c678V4a6 = LT v112c674V4a6, v112c675V4a6(0x20)
    0x6790x112cS0x4a6: v112c679V4a6 = ISZERO v112c678V4a6
    0x67a0x112cS0x4a6: v112c67aV4a6(0x682) = CONST 
    0x67d0x112cS0x4a6: JUMPI v112c67aV4a6(0x682), v112c679V4a6

    Begin block 0x67e0x112cB0x4a6
    prev=[0x66c0x112cB0x4a6], succ=[]
    =================================
    0x67e0x112cS0x4a6: v112c67eV4a6(0x0) = CONST 
    0x6810x112cS0x4a6: REVERT v112c67eV4a6(0x0), v112c67eV4a6(0x0)

    Begin block 0x6820x112cB0x4a6
    prev=[0x66c0x112cB0x4a6], succ=[0x16de]
    =================================
    0x6840x112cS0x4a6: v112c684V4a6 = MLOAD v112c673V4a6
    0x68a0x112cS0x4a6: JUMP v4a8(0x16de)

    Begin block 0x16de
    prev=[0x6820x112cB0x4a6], succ=[]
    =================================
    0x16df: v16df(0x40) = CONST 
    0x16e2: v16e2 = MLOAD v16df(0x40)
    0x16e5: MSTORE v16e2, v112c684V4a6
    0x16e6: v16e6 = MLOAD v16df(0x40)
    0x16ea: v16ea(0x0) = SUB v16e2, v16e6
    0x16eb: v16eb(0x20) = CONST 
    0x16ed: v16ed(0x20) = ADD v16eb(0x20), v16ea(0x0)
    0x16ef: RETURN v16e6, v16ed(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x4c1
    prev=[], succ=[0x4c9, 0x4cd]
    =================================
    0x4c2: v4c2 = CALLVALUE 
    0x4c4: v4c4 = ISZERO v4c2
    0x4c5: v4c5(0x4cd) = CONST 
    0x4c8: JUMPI v4c5(0x4cd), v4c4

    Begin block 0x4c9
    prev=[0x4c1], succ=[]
    =================================
    0x4c9: v4c9(0x0) = CONST 
    0x4cc: REVERT v4c9(0x0), v4c9(0x0)

    Begin block 0x4cd
    prev=[0x4c1], succ=[0x11bcB0x4cd]
    =================================
    0x4cf: v4cf(0x170f) = CONST 
    0x4d2: v4d2(0x1) = CONST 
    0x4d4: v4d4(0xa0) = CONST 
    0x4d6: v4d6(0x2) = CONST 
    0x4d8: v4d8(0x10000000000000000000000000000000000000000) = EXP v4d6(0x2), v4d4(0xa0)
    0x4d9: v4d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4d8(0x10000000000000000000000000000000000000000), v4d2(0x1)
    0x4da: v4da(0x4) = CONST 
    0x4dc: v4dc = CALLDATALOAD v4da(0x4)
    0x4dd: v4dd = AND v4dc, v4d9(0xffffffffffffffffffffffffffffffffffffffff)
    0x4de: v4de(0x11bc) = CONST 
    0x4e1: JUMP v4de(0x11bc), v4dd, v4cf(0x170f)

    Begin block 0x11bcB0x4cd
    prev=[0x4cd], succ=[0x11cfB0x4cd, 0x11d3B0x4cd]
    =================================
    0x11bdS0x4cd: v11bdV4cd(0x0) = CONST 
    0x11bfS0x4cd: v11bfV4cd = SLOAD v11bdV4cd(0x0)
    0x11c0S0x4cd: v11c0V4cd(0x1) = CONST 
    0x11c2S0x4cd: v11c2V4cd(0xa0) = CONST 
    0x11c4S0x4cd: v11c4V4cd(0x2) = CONST 
    0x11c6S0x4cd: v11c6V4cd(0x10000000000000000000000000000000000000000) = EXP v11c4V4cd(0x2), v11c2V4cd(0xa0)
    0x11c7S0x4cd: v11c7V4cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11c6V4cd(0x10000000000000000000000000000000000000000), v11c0V4cd(0x1)
    0x11c8S0x4cd: v11c8V4cd = AND v11c7V4cd(0xffffffffffffffffffffffffffffffffffffffff), v11bfV4cd
    0x11c9S0x4cd: v11c9V4cd = CALLER 
    0x11caS0x4cd: v11caV4cd = EQ v11c9V4cd, v11c8V4cd
    0x11cbS0x4cd: v11cbV4cd(0x11d3) = CONST 
    0x11ceS0x4cd: JUMPI v11cbV4cd(0x11d3), v11caV4cd

    Begin block 0x11cfB0x4cd
    prev=[0x11bcB0x4cd], succ=[]
    =================================
    0x11cfS0x4cd: v11cfV4cd(0x0) = CONST 
    0x11d2S0x4cd: REVERT v11cfV4cd(0x0), v11cfV4cd(0x0)

    Begin block 0x11d3B0x4cd
    prev=[0x11bcB0x4cd], succ=[0x1293B0x4cd]
    =================================
    0x11d4S0x4cd: v11d4V4cd(0x11dc) = CONST 
    0x11d8S0x4cd: v11d8V4cd(0x1293) = CONST 
    0x11dbS0x4cd: JUMP v11d8V4cd(0x1293)

    Begin block 0x1293B0x4cd
    prev=[0x11d3B0x4cd], succ=[0x12a4B0x4cd, 0x12a8B0x4cd]
    =================================
    0x1294S0x4cd: v1294V4cd(0x1) = CONST 
    0x1296S0x4cd: v1296V4cd(0xa0) = CONST 
    0x1298S0x4cd: v1298V4cd(0x2) = CONST 
    0x129aS0x4cd: v129aV4cd(0x10000000000000000000000000000000000000000) = EXP v1298V4cd(0x2), v1296V4cd(0xa0)
    0x129bS0x4cd: v129bV4cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v129aV4cd(0x10000000000000000000000000000000000000000), v1294V4cd(0x1)
    0x129dS0x4cd: v129dV4cd = AND v4dd, v129bV4cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x129eS0x4cd: v129eV4cd = ISZERO v129dV4cd
    0x129fS0x4cd: v129fV4cd = ISZERO v129eV4cd
    0x12a0S0x4cd: v12a0V4cd(0x12a8) = CONST 
    0x12a3S0x4cd: JUMPI v12a0V4cd(0x12a8), v129fV4cd

    Begin block 0x12a4B0x4cd
    prev=[0x1293B0x4cd], succ=[]
    =================================
    0x12a4S0x4cd: v12a4V4cd(0x0) = CONST 
    0x12a7S0x4cd: REVERT v12a4V4cd(0x0), v12a4V4cd(0x0)

    Begin block 0x12a8B0x4cd
    prev=[0x1293B0x4cd], succ=[0x11dcB0x4cd]
    =================================
    0x12a9S0x4cd: v12a9V4cd(0x0) = CONST 
    0x12acS0x4cd: v12acV4cd = SLOAD v12a9V4cd(0x0)
    0x12adS0x4cd: v12adV4cd(0x40) = CONST 
    0x12afS0x4cd: v12afV4cd = MLOAD v12adV4cd(0x40)
    0x12b0S0x4cd: v12b0V4cd(0x1) = CONST 
    0x12b2S0x4cd: v12b2V4cd(0xa0) = CONST 
    0x12b4S0x4cd: v12b4V4cd(0x2) = CONST 
    0x12b6S0x4cd: v12b6V4cd(0x10000000000000000000000000000000000000000) = EXP v12b4V4cd(0x2), v12b2V4cd(0xa0)
    0x12b7S0x4cd: v12b7V4cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12b6V4cd(0x10000000000000000000000000000000000000000), v12b0V4cd(0x1)
    0x12baS0x4cd: v12baV4cd = AND v4dd, v12b7V4cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x12bdS0x4cd: v12bdV4cd = AND v12acV4cd, v12b7V4cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x12bfS0x4cd: v12bfV4cd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x12e1S0x4cd: LOG3 v12afV4cd, v12a9V4cd(0x0), v12bfV4cd(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v12bdV4cd, v12baV4cd
    0x12e2S0x4cd: v12e2V4cd(0x0) = CONST 
    0x12e5S0x4cd: v12e5V4cd = SLOAD v12e2V4cd(0x0)
    0x12e6S0x4cd: v12e6V4cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12fbS0x4cd: v12fbV4cd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v12e6V4cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x12fcS0x4cd: v12fcV4cd = AND v12fbV4cd(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12e5V4cd
    0x12fdS0x4cd: v12fdV4cd(0x1) = CONST 
    0x12ffS0x4cd: v12ffV4cd(0xa0) = CONST 
    0x1301S0x4cd: v1301V4cd(0x2) = CONST 
    0x1303S0x4cd: v1303V4cd(0x10000000000000000000000000000000000000000) = EXP v1301V4cd(0x2), v12ffV4cd(0xa0)
    0x1304S0x4cd: v1304V4cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1303V4cd(0x10000000000000000000000000000000000000000), v12fdV4cd(0x1)
    0x1308S0x4cd: v1308V4cd = AND v1304V4cd(0xffffffffffffffffffffffffffffffffffffffff), v4dd
    0x130cS0x4cd: v130cV4cd = OR v1308V4cd, v12fcV4cd
    0x130eS0x4cd: SSTORE v12e2V4cd(0x0), v130cV4cd
    0x130fS0x4cd: JUMP v11d4V4cd(0x11dc)

    Begin block 0x11dcB0x4cd
    prev=[0x12a8B0x4cd], succ=[0x170f]
    =================================
    0x11deS0x4cd: JUMP v4cf(0x170f)

    Begin block 0x170f
    prev=[0x11dcB0x4cd], succ=[]
    =================================
    0x1710: STOP 

}

function setTotalSupply(uint256)() public {
    Begin block 0x4e2
    prev=[], succ=[0x4ea, 0x4ee]
    =================================
    0x4e3: v4e3 = CALLVALUE 
    0x4e5: v4e5 = ISZERO v4e3
    0x4e6: v4e6(0x4ee) = CONST 
    0x4e9: JUMPI v4e6(0x4ee), v4e5

    Begin block 0x4ea
    prev=[0x4e2], succ=[]
    =================================
    0x4ea: v4ea(0x0) = CONST 
    0x4ed: REVERT v4ea(0x0), v4ea(0x0)

    Begin block 0x4ee
    prev=[0x4e2], succ=[0x11dfB0x4ee]
    =================================
    0x4f0: v4f0(0x1730) = CONST 
    0x4f3: v4f3(0x4) = CONST 
    0x4f5: v4f5 = CALLDATALOAD v4f3(0x4)
    0x4f6: v4f6(0x11df) = CONST 
    0x4f9: JUMP v4f6(0x11df), v4f5, v4f0(0x1730)

    Begin block 0x11dfB0x4ee
    prev=[0x4ee], succ=[0x11f2B0x4ee, 0x11f6B0x4ee]
    =================================
    0x11e0S0x4ee: v11e0V4ee(0x0) = CONST 
    0x11e2S0x4ee: v11e2V4ee = SLOAD v11e0V4ee(0x0)
    0x11e3S0x4ee: v11e3V4ee(0x1) = CONST 
    0x11e5S0x4ee: v11e5V4ee(0xa0) = CONST 
    0x11e7S0x4ee: v11e7V4ee(0x2) = CONST 
    0x11e9S0x4ee: v11e9V4ee(0x10000000000000000000000000000000000000000) = EXP v11e7V4ee(0x2), v11e5V4ee(0xa0)
    0x11eaS0x4ee: v11eaV4ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11e9V4ee(0x10000000000000000000000000000000000000000), v11e3V4ee(0x1)
    0x11ebS0x4ee: v11ebV4ee = AND v11eaV4ee(0xffffffffffffffffffffffffffffffffffffffff), v11e2V4ee
    0x11ecS0x4ee: v11ecV4ee = CALLER 
    0x11edS0x4ee: v11edV4ee = EQ v11ecV4ee, v11ebV4ee
    0x11eeS0x4ee: v11eeV4ee(0x11f6) = CONST 
    0x11f1S0x4ee: JUMPI v11eeV4ee(0x11f6), v11edV4ee

    Begin block 0x11f2B0x4ee
    prev=[0x11dfB0x4ee], succ=[]
    =================================
    0x11f2S0x4ee: v11f2V4ee(0x0) = CONST 
    0x11f5S0x4ee: REVERT v11f2V4ee(0x0), v11f2V4ee(0x0)

    Begin block 0x11f6B0x4ee
    prev=[0x11dfB0x4ee], succ=[0x1274B0x4ee, 0x1278B0x4ee]
    =================================
    0x11f7S0x4ee: v11f7V4ee(0x6) = CONST 
    0x11f9S0x4ee: v11f9V4ee = SLOAD v11f7V4ee(0x6)
    0x11faS0x4ee: v11faV4ee(0x40) = CONST 
    0x11fdS0x4ee: v11fdV4ee = MLOAD v11faV4ee(0x40)
    0x11feS0x4ee: v11feV4ee(0x79ba7f3900000000000000000000000000000000000000000000000000000000) = CONST 
    0x1220S0x4ee: MSTORE v11fdV4ee, v11feV4ee(0x79ba7f3900000000000000000000000000000000000000000000000000000000)
    0x1221S0x4ee: v1221V4ee(0x10000) = CONST 
    0x1227S0x4ee: v1227V4ee = DIV v11f9V4ee, v1221V4ee(0x10000)
    0x1228S0x4ee: v1228V4ee(0x1) = CONST 
    0x122aS0x4ee: v122aV4ee(0xa0) = CONST 
    0x122cS0x4ee: v122cV4ee(0x2) = CONST 
    0x122eS0x4ee: v122eV4ee(0x10000000000000000000000000000000000000000) = EXP v122cV4ee(0x2), v122aV4ee(0xa0)
    0x122fS0x4ee: v122fV4ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v122eV4ee(0x10000000000000000000000000000000000000000), v1228V4ee(0x1)
    0x1230S0x4ee: v1230V4ee = AND v122fV4ee(0xffffffffffffffffffffffffffffffffffffffff), v1227V4ee
    0x1231S0x4ee: v1231V4ee(0x4) = CONST 
    0x1234S0x4ee: v1234V4ee = ADD v11fdV4ee, v1231V4ee(0x4)
    0x1235S0x4ee: MSTORE v1234V4ee, v1230V4ee
    0x1236S0x4ee: v1236V4ee(0x24) = CONST 
    0x1239S0x4ee: v1239V4ee = ADD v11fdV4ee, v1236V4ee(0x24)
    0x123cS0x4ee: MSTORE v1239V4ee, v4f5
    0x123dS0x4ee: v123dV4ee = MLOAD v11faV4ee(0x40)
    0x123eS0x4ee: v123eV4ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0x1254S0x4ee: v1254V4ee(0x79ba7f39) = CONST 
    0x125aS0x4ee: v125aV4ee(0x44) = CONST 
    0x125eS0x4ee: v125eV4ee = ADD v11fdV4ee, v125aV4ee(0x44)
    0x1260S0x4ee: v1260V4ee(0x0) = CONST 
    0x1267S0x4ee: v1267V4ee(0x0) = SUB v11fdV4ee, v123dV4ee
    0x1268S0x4ee: v1268V4ee(0x44) = ADD v1267V4ee(0x0), v125aV4ee(0x44)
    0x126cS0x4ee: v126cV4ee = EXTCODESIZE v123eV4ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0x126dS0x4ee: v126dV4ee = ISZERO v126cV4ee
    0x126fS0x4ee: v126fV4ee = ISZERO v126dV4ee
    0x1270S0x4ee: v1270V4ee(0x1278) = CONST 
    0x1273S0x4ee: JUMPI v1270V4ee(0x1278), v126fV4ee

    Begin block 0x1274B0x4ee
    prev=[0x11f6B0x4ee], succ=[]
    =================================
    0x1274S0x4ee: v1274V4ee(0x0) = CONST 
    0x1277S0x4ee: REVERT v1274V4ee(0x0), v1274V4ee(0x0)

    Begin block 0x1278B0x4ee
    prev=[0x11f6B0x4ee], succ=[0x1283B0x4ee, 0x128cB0x4ee]
    =================================
    0x127aS0x4ee: v127aV4ee = GAS 
    0x127bS0x4ee: v127bV4ee = DELEGATECALL v127aV4ee, v123eV4ee(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), v123dV4ee, v1268V4ee(0x44), v123dV4ee, v1260V4ee(0x0)
    0x127cS0x4ee: v127cV4ee = ISZERO v127bV4ee
    0x127eS0x4ee: v127eV4ee = ISZERO v127cV4ee
    0x127fS0x4ee: v127fV4ee(0x128c) = CONST 
    0x1282S0x4ee: JUMPI v127fV4ee(0x128c), v127eV4ee

    Begin block 0x1283B0x4ee
    prev=[0x1278B0x4ee], succ=[]
    =================================
    0x1283S0x4ee: v1283V4ee = RETURNDATASIZE 
    0x1284S0x4ee: v1284V4ee(0x0) = CONST 
    0x1287S0x4ee: RETURNDATACOPY v1284V4ee(0x0), v1284V4ee(0x0), v1283V4ee
    0x1288S0x4ee: v1288V4ee = RETURNDATASIZE 
    0x1289S0x4ee: v1289V4ee(0x0) = CONST 
    0x128bS0x4ee: REVERT v1289V4ee(0x0), v1288V4ee

    Begin block 0x128cB0x4ee
    prev=[0x1278B0x4ee], succ=[0x1730]
    =================================
    0x1292S0x4ee: JUMP v4f0(0x1730)

    Begin block 0x1730
    prev=[0x128cB0x4ee], succ=[]
    =================================
    0x1731: STOP 

}

function 0x4fa(0x4faarg0x0) private {
    Begin block 0x4fa
    prev=[], succ=[0x1751, 0x53a]
    =================================
    0x4fb: v4fb(0x4) = CONST 
    0x4fe: v4fe = SLOAD v4fb(0x4)
    0x4ff: v4ff(0x40) = CONST 
    0x502: v502 = MLOAD v4ff(0x40)
    0x503: v503(0x20) = CONST 
    0x505: v505(0x2) = CONST 
    0x507: v507(0x1) = CONST 
    0x50a: v50a = AND v4fe, v507(0x1)
    0x50b: v50b = ISZERO v50a
    0x50c: v50c(0x100) = CONST 
    0x50f: v50f = MUL v50c(0x100), v50b
    0x510: v510(0x0) = CONST 
    0x512: v512(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v510(0x0)
    0x513: v513 = ADD v512(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v50f
    0x516: v516 = AND v4fe, v513
    0x51a: v51a = DIV v516, v505(0x2)
    0x51b: v51b(0x1f) = CONST 
    0x51e: v51e = ADD v51a, v51b(0x1f)
    0x521: v521 = DIV v51e, v503(0x20)
    0x523: v523 = MUL v503(0x20), v521
    0x525: v525 = ADD v502, v523
    0x527: v527 = ADD v503(0x20), v525
    0x52a: MSTORE v4ff(0x40), v527
    0x52d: MSTORE v502, v51a
    0x531: v531 = ADD v502, v503(0x20)
    0x535: v535 = ISZERO v51a
    0x536: v536(0x1751) = CONST 
    0x539: JUMPI v536(0x1751), v535

    Begin block 0x1751
    prev=[0x4fa], succ=[]
    =================================
    0x1758: RETURNPRIVATE v4faarg0, v502, v4faarg0

    Begin block 0x53a
    prev=[0x4fa], succ=[0x542, 0x5550x4fa]
    =================================
    0x53b: v53b(0x1f) = CONST 
    0x53d: v53d = LT v53b(0x1f), v51a
    0x53e: v53e(0x555) = CONST 
    0x541: JUMPI v53e(0x555), v53d

    Begin block 0x542
    prev=[0x53a], succ=[0x1778]
    =================================
    0x542: v542(0x100) = CONST 
    0x547: v547 = SLOAD v4fb(0x4)
    0x548: v548 = DIV v547, v542(0x100)
    0x549: v549 = MUL v548, v542(0x100)
    0x54b: MSTORE v531, v549
    0x54d: v54d(0x20) = CONST 
    0x54f: v54f = ADD v54d(0x20), v531
    0x551: v551(0x1778) = CONST 
    0x554: JUMP v551(0x1778)

    Begin block 0x1778
    prev=[0x542], succ=[]
    =================================
    0x177f: RETURNPRIVATE v4faarg0, v502, v4faarg0

    Begin block 0x5550x4fa
    prev=[0x53a], succ=[0x5630x4fa]
    =================================
    0x5570x4fa: v4fa557 = ADD v531, v51a
    0x55a0x4fa: v4fa55a(0x0) = CONST 
    0x55c0x4fa: MSTORE v4fa55a(0x0), v4fb(0x4)
    0x55d0x4fa: v4fa55d(0x20) = CONST 
    0x55f0x4fa: v4fa55f(0x0) = CONST 
    0x5610x4fa: v4fa561 = SHA3 v4fa55f(0x0), v4fa55d(0x20)

    Begin block 0x5630x4fa
    prev=[0x5630x4fa, 0x5550x4fa], succ=[0x5630x4fa, 0x5770x4fa]
    =================================
    0x5630x4fa_0x0: v5634fa_0 = PHI v531, v4fa56f
    0x5630x4fa_0x1: v5634fa_1 = PHI v4fa56b, v4fa561
    0x5650x4fa: v4fa565 = SLOAD v5634fa_1
    0x5670x4fa: MSTORE v5634fa_0, v4fa565
    0x5690x4fa: v4fa569(0x1) = CONST 
    0x56b0x4fa: v4fa56b = ADD v4fa569(0x1), v5634fa_1
    0x56d0x4fa: v4fa56d(0x20) = CONST 
    0x56f0x4fa: v4fa56f = ADD v4fa56d(0x20), v5634fa_0
    0x5720x4fa: v4fa572 = GT v4fa557, v4fa56f
    0x5730x4fa: v4fa573(0x563) = CONST 
    0x5760x4fa: JUMPI v4fa573(0x563), v4fa572

    Begin block 0x5770x4fa
    prev=[0x5630x4fa], succ=[0x5800x4fa]
    =================================
    0x5790x4fa: v4fa579 = SUB v4fa56f, v4fa557
    0x57a0x4fa: v4fa57a(0x1f) = CONST 
    0x57c0x4fa: v4fa57c = AND v4fa57a(0x1f), v4fa579
    0x57e0x4fa: v4fa57e = ADD v4fa557, v4fa57c

    Begin block 0x5800x4fa
    prev=[0x5770x4fa], succ=[]
    =================================
    0x5870x4fa: RETURNPRIVATE v4faarg0, v502, v4faarg0

}

function 0xb15(0xb15arg0x0) private {
    Begin block 0xb15
    prev=[], succ=[0x179f, 0xb55]
    =================================
    0xb16: vb16(0x3) = CONST 
    0xb19: vb19 = SLOAD vb16(0x3)
    0xb1a: vb1a(0x40) = CONST 
    0xb1d: vb1d = MLOAD vb1a(0x40)
    0xb1e: vb1e(0x20) = CONST 
    0xb20: vb20(0x2) = CONST 
    0xb22: vb22(0x1) = CONST 
    0xb25: vb25 = AND vb19, vb22(0x1)
    0xb26: vb26 = ISZERO vb25
    0xb27: vb27(0x100) = CONST 
    0xb2a: vb2a = MUL vb27(0x100), vb26
    0xb2b: vb2b(0x0) = CONST 
    0xb2d: vb2d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vb2b(0x0)
    0xb2e: vb2e = ADD vb2d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vb2a
    0xb31: vb31 = AND vb19, vb2e
    0xb35: vb35 = DIV vb31, vb20(0x2)
    0xb36: vb36(0x1f) = CONST 
    0xb39: vb39 = ADD vb35, vb36(0x1f)
    0xb3c: vb3c = DIV vb39, vb1e(0x20)
    0xb3e: vb3e = MUL vb1e(0x20), vb3c
    0xb40: vb40 = ADD vb1d, vb3e
    0xb42: vb42 = ADD vb1e(0x20), vb40
    0xb45: MSTORE vb1a(0x40), vb42
    0xb48: MSTORE vb1d, vb35
    0xb4c: vb4c = ADD vb1d, vb1e(0x20)
    0xb50: vb50 = ISZERO vb35
    0xb51: vb51(0x179f) = CONST 
    0xb54: JUMPI vb51(0x179f), vb50

    Begin block 0x179f
    prev=[0xb15], succ=[]
    =================================
    0x17a6: RETURNPRIVATE vb15arg0, vb1d, vb15arg0

    Begin block 0xb55
    prev=[0xb15], succ=[0xb5d, 0x5550xb15]
    =================================
    0xb56: vb56(0x1f) = CONST 
    0xb58: vb58 = LT vb56(0x1f), vb35
    0xb59: vb59(0x555) = CONST 
    0xb5c: JUMPI vb59(0x555), vb58

    Begin block 0xb5d
    prev=[0xb55], succ=[0x17c6]
    =================================
    0xb5d: vb5d(0x100) = CONST 
    0xb62: vb62 = SLOAD vb16(0x3)
    0xb63: vb63 = DIV vb62, vb5d(0x100)
    0xb64: vb64 = MUL vb63, vb5d(0x100)
    0xb66: MSTORE vb4c, vb64
    0xb68: vb68(0x20) = CONST 
    0xb6a: vb6a = ADD vb68(0x20), vb4c
    0xb6c: vb6c(0x17c6) = CONST 
    0xb6f: JUMP vb6c(0x17c6)

    Begin block 0x17c6
    prev=[0xb5d], succ=[]
    =================================
    0x17cd: RETURNPRIVATE vb15arg0, vb1d, vb15arg0

    Begin block 0x5550xb15
    prev=[0xb55], succ=[0x5630xb15]
    =================================
    0x5570xb15: vb15557 = ADD vb4c, vb35
    0x55a0xb15: vb1555a(0x0) = CONST 
    0x55c0xb15: MSTORE vb1555a(0x0), vb16(0x3)
    0x55d0xb15: vb1555d(0x20) = CONST 
    0x55f0xb15: vb1555f(0x0) = CONST 
    0x5610xb15: vb15561 = SHA3 vb1555f(0x0), vb1555d(0x20)

    Begin block 0x5630xb15
    prev=[0x5630xb15, 0x5550xb15], succ=[0x5630xb15, 0x5770xb15]
    =================================
    0x5630xb15_0x0: v563b15_0 = PHI vb4c, vb1556f
    0x5630xb15_0x1: v563b15_1 = PHI vb1556b, vb15561
    0x5650xb15: vb15565 = SLOAD v563b15_1
    0x5670xb15: MSTORE v563b15_0, vb15565
    0x5690xb15: vb15569(0x1) = CONST 
    0x56b0xb15: vb1556b = ADD vb15569(0x1), v563b15_1
    0x56d0xb15: vb1556d(0x20) = CONST 
    0x56f0xb15: vb1556f = ADD vb1556d(0x20), v563b15_0
    0x5720xb15: vb15572 = GT vb15557, vb1556f
    0x5730xb15: vb15573(0x563) = CONST 
    0x5760xb15: JUMPI vb15573(0x563), vb15572

    Begin block 0x5770xb15
    prev=[0x5630xb15], succ=[0x5800xb15]
    =================================
    0x5790xb15: vb15579 = SUB vb1556f, vb15557
    0x57a0xb15: vb1557a(0x1f) = CONST 
    0x57c0xb15: vb1557c = AND vb1557a(0x1f), vb15579
    0x57e0xb15: vb1557e = ADD vb15557, vb1557c

    Begin block 0x5800xb15
    prev=[0x5770xb15], succ=[]
    =================================
    0x5870xb15: RETURNPRIVATE vb15arg0, vb1d, vb15arg0

}

function 0xce6(0xce6arg0x0, 0xce6arg0x1) private {
    Begin block 0xce6
    prev=[], succ=[0xd6a, 0xd6e]
    =================================
    0xce7: vce7(0x6) = CONST 
    0xce9: vce9 = SLOAD vce7(0x6)
    0xcea: vcea(0x40) = CONST 
    0xced: vced = MLOAD vcea(0x40)
    0xcee: vcee(0xf7888aec00000000000000000000000000000000000000000000000000000000) = CONST 
    0xd10: MSTORE vced, vcee(0xf7888aec00000000000000000000000000000000000000000000000000000000)
    0xd11: vd11(0x1) = CONST 
    0xd13: vd13(0xa0) = CONST 
    0xd15: vd15(0x2) = CONST 
    0xd17: vd17(0x10000000000000000000000000000000000000000) = EXP vd15(0x2), vd13(0xa0)
    0xd18: vd18(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd17(0x10000000000000000000000000000000000000000), vd11(0x1)
    0xd19: vd19(0x10000) = CONST 
    0xd1f: vd1f = DIV vce9, vd19(0x10000)
    0xd21: vd21 = AND vd18(0xffffffffffffffffffffffffffffffffffffffff), vd1f
    0xd22: vd22(0x4) = CONST 
    0xd25: vd25 = ADD vced, vd22(0x4)
    0xd26: MSTORE vd25, vd21
    0xd29: vd29 = AND vce6arg0, vd18(0xffffffffffffffffffffffffffffffffffffffff)
    0xd2a: vd2a(0x24) = CONST 
    0xd2d: vd2d = ADD vced, vd2a(0x24)
    0xd2e: MSTORE vd2d, vd29
    0xd2f: vd2f = MLOAD vcea(0x40)
    0xd30: vd30(0x0) = CONST 
    0xd33: vd33(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27) = CONST 
    0xd49: vd49(0xf7888aec) = CONST 
    0xd4f: vd4f(0x44) = CONST 
    0xd53: vd53 = ADD vced, vd4f(0x44)
    0xd55: vd55(0x20) = CONST 
    0xd5d: vd5d(0x0) = SUB vced, vd2f
    0xd5e: vd5e(0x44) = ADD vd5d(0x0), vd4f(0x44)
    0xd62: vd62 = EXTCODESIZE vd33(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27)
    0xd63: vd63 = ISZERO vd62
    0xd65: vd65 = ISZERO vd63
    0xd66: vd66(0xd6e) = CONST 
    0xd69: JUMPI vd66(0xd6e), vd65

    Begin block 0xd6a
    prev=[0xce6], succ=[]
    =================================
    0xd6a: vd6a(0x0) = CONST 
    0xd6d: REVERT vd6a(0x0), vd6a(0x0)

    Begin block 0xd6e
    prev=[0xce6], succ=[0xd79, 0xd82]
    =================================
    0xd70: vd70 = GAS 
    0xd71: vd71 = DELEGATECALL vd70, vd33(0x1ee9faa44d313a1d2e4bfa135ffb15c6f0da8a27), vd2f, vd5e(0x44), vd2f, vd55(0x20)
    0xd72: vd72 = ISZERO vd71
    0xd74: vd74 = ISZERO vd72
    0xd75: vd75(0xd82) = CONST 
    0xd78: JUMPI vd75(0xd82), vd74

    Begin block 0xd79
    prev=[0xd6e], succ=[]
    =================================
    0xd79: vd79 = RETURNDATASIZE 
    0xd7a: vd7a(0x0) = CONST 
    0xd7d: RETURNDATACOPY vd7a(0x0), vd7a(0x0), vd79
    0xd7e: vd7e = RETURNDATASIZE 
    0xd7f: vd7f(0x0) = CONST 
    0xd81: REVERT vd7f(0x0), vd7e

    Begin block 0xd82
    prev=[0xd6e], succ=[0xd94, 0xd98]
    =================================
    0xd87: vd87(0x40) = CONST 
    0xd89: vd89 = MLOAD vd87(0x40)
    0xd8a: vd8a = RETURNDATASIZE 
    0xd8b: vd8b(0x20) = CONST 
    0xd8e: vd8e = LT vd8a, vd8b(0x20)
    0xd8f: vd8f = ISZERO vd8e
    0xd90: vd90(0xd98) = CONST 
    0xd93: JUMPI vd90(0xd98), vd8f

    Begin block 0xd94
    prev=[0xd82], succ=[]
    =================================
    0xd94: vd94(0x0) = CONST 
    0xd97: REVERT vd94(0x0), vd94(0x0)

    Begin block 0xd98
    prev=[0xd82], succ=[]
    =================================
    0xd9a: vd9a = MLOAD vd89
    0xd9f: RETURNPRIVATE vce6arg1, vd9a

}

function 0xf11(0xf11arg0x0) private {
    Begin block 0xf11
    prev=[], succ=[0x17ed, 0xf51]
    =================================
    0xf12: vf12(0x5) = CONST 
    0xf15: vf15 = SLOAD vf12(0x5)
    0xf16: vf16(0x40) = CONST 
    0xf19: vf19 = MLOAD vf16(0x40)
    0xf1a: vf1a(0x20) = CONST 
    0xf1c: vf1c(0x2) = CONST 
    0xf1e: vf1e(0x1) = CONST 
    0xf21: vf21 = AND vf15, vf1e(0x1)
    0xf22: vf22 = ISZERO vf21
    0xf23: vf23(0x100) = CONST 
    0xf26: vf26 = MUL vf23(0x100), vf22
    0xf27: vf27(0x0) = CONST 
    0xf29: vf29(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vf27(0x0)
    0xf2a: vf2a = ADD vf29(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vf26
    0xf2d: vf2d = AND vf15, vf2a
    0xf31: vf31 = DIV vf2d, vf1c(0x2)
    0xf32: vf32(0x1f) = CONST 
    0xf35: vf35 = ADD vf31, vf32(0x1f)
    0xf38: vf38 = DIV vf35, vf1a(0x20)
    0xf3a: vf3a = MUL vf1a(0x20), vf38
    0xf3c: vf3c = ADD vf19, vf3a
    0xf3e: vf3e = ADD vf1a(0x20), vf3c
    0xf41: MSTORE vf16(0x40), vf3e
    0xf44: MSTORE vf19, vf31
    0xf48: vf48 = ADD vf19, vf1a(0x20)
    0xf4c: vf4c = ISZERO vf31
    0xf4d: vf4d(0x17ed) = CONST 
    0xf50: JUMPI vf4d(0x17ed), vf4c

    Begin block 0x17ed
    prev=[0xf11], succ=[]
    =================================
    0x17f4: RETURNPRIVATE vf11arg0, vf19, vf11arg0

    Begin block 0xf51
    prev=[0xf11], succ=[0xf59, 0x5550xf11]
    =================================
    0xf52: vf52(0x1f) = CONST 
    0xf54: vf54 = LT vf52(0x1f), vf31
    0xf55: vf55(0x555) = CONST 
    0xf58: JUMPI vf55(0x555), vf54

    Begin block 0xf59
    prev=[0xf51], succ=[0x1814]
    =================================
    0xf59: vf59(0x100) = CONST 
    0xf5e: vf5e = SLOAD vf12(0x5)
    0xf5f: vf5f = DIV vf5e, vf59(0x100)
    0xf60: vf60 = MUL vf5f, vf59(0x100)
    0xf62: MSTORE vf48, vf60
    0xf64: vf64(0x20) = CONST 
    0xf66: vf66 = ADD vf64(0x20), vf48
    0xf68: vf68(0x1814) = CONST 
    0xf6b: JUMP vf68(0x1814)

    Begin block 0x1814
    prev=[0xf59], succ=[]
    =================================
    0x181b: RETURNPRIVATE vf11arg0, vf19, vf11arg0

    Begin block 0x5550xf11
    prev=[0xf51], succ=[0x5630xf11]
    =================================
    0x5570xf11: vf11557 = ADD vf48, vf31
    0x55a0xf11: vf1155a(0x0) = CONST 
    0x55c0xf11: MSTORE vf1155a(0x0), vf12(0x5)
    0x55d0xf11: vf1155d(0x20) = CONST 
    0x55f0xf11: vf1155f(0x0) = CONST 
    0x5610xf11: vf11561 = SHA3 vf1155f(0x0), vf1155d(0x20)

    Begin block 0x5630xf11
    prev=[0x5630xf11, 0x5550xf11], succ=[0x5630xf11, 0x5770xf11]
    =================================
    0x5630xf11_0x0: v563f11_0 = PHI vf48, vf1156f
    0x5630xf11_0x1: v563f11_1 = PHI vf1156b, vf11561
    0x5650xf11: vf11565 = SLOAD v563f11_1
    0x5670xf11: MSTORE v563f11_0, vf11565
    0x5690xf11: vf11569(0x1) = CONST 
    0x56b0xf11: vf1156b = ADD vf11569(0x1), v563f11_1
    0x56d0xf11: vf1156d(0x20) = CONST 
    0x56f0xf11: vf1156f = ADD vf1156d(0x20), v563f11_0
    0x5720xf11: vf11572 = GT vf11557, vf1156f
    0x5730xf11: vf11573(0x563) = CONST 
    0x5760xf11: JUMPI vf11573(0x563), vf11572

    Begin block 0x5770xf11
    prev=[0x5630xf11], succ=[0x5800xf11]
    =================================
    0x5790xf11: vf11579 = SUB vf1156f, vf11557
    0x57a0xf11: vf1157a(0x1f) = CONST 
    0x57c0xf11: vf1157c = AND vf1157a(0x1f), vf11579
    0x57e0xf11: vf1157e = ADD vf11557, vf1157c

    Begin block 0x5800xf11
    prev=[0x5770xf11], succ=[]
    =================================
    0x5870xf11: RETURNPRIVATE vf11arg0, vf19, vf11arg0

}

