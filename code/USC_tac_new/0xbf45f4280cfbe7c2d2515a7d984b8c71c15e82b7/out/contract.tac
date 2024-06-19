function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x98b]
    =================================
    0x0: v0(0x60) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x60)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x965: v965(0x98b) = CONST 
    0x966: JUMPI v965(0x98b), v8

    Begin block 0xd
    prev=[0x0], succ=[0x40, 0x98e]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x30: v30(0x0) = CONST 
    0x32: v32 = CALLDATALOAD v30(0x0)
    0x33: v33 = DIV v32, v12(0x100000000000000000000000000000000000000000000000000000000)
    0x34: v34 = AND v33, vd(0xffffffff)
    0x35: v35(0x19774d43) = CONST 
    0x3b: v3b = EQ v34, v35(0x19774d43)
    0x967: v967(0x98e) = CONST 
    0x968: JUMPI v967(0x98e), v3b

    Begin block 0x40
    prev=[0xd], succ=[0x991, 0x4b]
    =================================
    0x41: v41(0x1bff4786) = CONST 
    0x46: v46 = EQ v41(0x1bff4786), v34
    0x969: v969(0x991) = CONST 
    0x96a: JUMPI v969(0x991), v46

    Begin block 0x991
    prev=[0x40], succ=[]
    =================================
    0x992: v992(0x19b) = CONST 
    0x993: CALLPRIVATE v992(0x19b)

    Begin block 0x4b
    prev=[0x40], succ=[0x994, 0x56]
    =================================
    0x4c: v4c(0x3cf52ffb) = CONST 
    0x51: v51 = EQ v4c(0x3cf52ffb), v34
    0x96b: v96b(0x994) = CONST 
    0x96c: JUMPI v96b(0x994), v51

    Begin block 0x994
    prev=[0x4b], succ=[]
    =================================
    0x995: v995(0x1c6) = CONST 
    0x996: CALLPRIVATE v995(0x1c6)

    Begin block 0x56
    prev=[0x4b], succ=[0x997, 0x61]
    =================================
    0x57: v57(0x508493bc) = CONST 
    0x5c: v5c = EQ v57(0x508493bc), v34
    0x96d: v96d(0x997) = CONST 
    0x96e: JUMPI v96d(0x997), v5c

    Begin block 0x997
    prev=[0x56], succ=[]
    =================================
    0x998: v998(0x1d9) = CONST 
    0x999: CALLPRIVATE v998(0x1d9)

    Begin block 0x61
    prev=[0x56], succ=[0x99a, 0x6c]
    =================================
    0x62: v62(0x55ce76e6) = CONST 
    0x67: v67 = EQ v62(0x55ce76e6), v34
    0x96f: v96f(0x99a) = CONST 
    0x970: JUMPI v96f(0x99a), v67

    Begin block 0x99a
    prev=[0x61], succ=[]
    =================================
    0x99b: v99b(0x1fe) = CONST 
    0x99c: CALLPRIVATE v99b(0x1fe)

    Begin block 0x6c
    prev=[0x61], succ=[0x99d, 0x77]
    =================================
    0x6d: v6d(0x5bd948b1) = CONST 
    0x72: v72 = EQ v6d(0x5bd948b1), v34
    0x971: v971(0x99d) = CONST 
    0x972: JUMPI v971(0x99d), v72

    Begin block 0x99d
    prev=[0x6c], succ=[]
    =================================
    0x99e: v99e(0x211) = CONST 
    0x99f: CALLPRIVATE v99e(0x211)

    Begin block 0x77
    prev=[0x6c], succ=[0x9a0, 0x82]
    =================================
    0x78: v78(0x5d4d061e) = CONST 
    0x7d: v7d = EQ v78(0x5d4d061e), v34
    0x973: v973(0x9a0) = CONST 
    0x974: JUMPI v973(0x9a0), v7d

    Begin block 0x9a0
    prev=[0x77], succ=[]
    =================================
    0x9a1: v9a1(0x238) = CONST 
    0x9a2: CALLPRIVATE v9a1(0x238)

    Begin block 0x82
    prev=[0x77], succ=[0x9a3, 0x8d]
    =================================
    0x83: v83(0x65e17c9d) = CONST 
    0x88: v88 = EQ v83(0x65e17c9d), v34
    0x975: v975(0x9a3) = CONST 
    0x976: JUMPI v975(0x9a3), v88

    Begin block 0x9a3
    prev=[0x82], succ=[]
    =================================
    0x9a4: v9a4(0x267) = CONST 
    0x9a5: CALLPRIVATE v9a4(0x267)

    Begin block 0x8d
    prev=[0x82], succ=[0x9a6, 0x98]
    =================================
    0x8e: v8e(0x8e1e2add) = CONST 
    0x93: v93 = EQ v8e(0x8e1e2add), v34
    0x977: v977(0x9a6) = CONST 
    0x978: JUMPI v977(0x9a6), v93

    Begin block 0x9a6
    prev=[0x8d], succ=[]
    =================================
    0x9a7: v9a7(0x27a) = CONST 
    0x9a8: CALLPRIVATE v9a7(0x27a)

    Begin block 0x98
    prev=[0x8d], succ=[0x9a9, 0xa3]
    =================================
    0x99: v99(0xaaf10f42) = CONST 
    0x9e: v9e = EQ v99(0xaaf10f42), v34
    0x979: v979(0x9a9) = CONST 
    0x97a: JUMPI v979(0x9a9), v9e

    Begin block 0x9a9
    prev=[0x98], succ=[]
    =================================
    0x9aa: v9aa(0x28d) = CONST 
    0x9ab: CALLPRIVATE v9aa(0x28d)

    Begin block 0xa3
    prev=[0x98], succ=[0x9ac, 0xae]
    =================================
    0xa4: va4(0xbb057c5e) = CONST 
    0xa9: va9 = EQ va4(0xbb057c5e), v34
    0x97b: v97b(0x9ac) = CONST 
    0x97c: JUMPI v97b(0x9ac), va9

    Begin block 0x9ac
    prev=[0xa3], succ=[]
    =================================
    0x9ad: v9ad(0x2a0) = CONST 
    0x9ae: CALLPRIVATE v9ad(0x2a0)

    Begin block 0xae
    prev=[0xa3], succ=[0x9af, 0xb9]
    =================================
    0xaf: vaf(0xbb5f4629) = CONST 
    0xb4: vb4 = EQ vaf(0xbb5f4629), v34
    0x97d: v97d(0x9af) = CONST 
    0x97e: JUMPI v97d(0x9af), vb4

    Begin block 0x9af
    prev=[0xae], succ=[]
    =================================
    0x9b0: v9b0(0x2b3) = CONST 
    0x9b1: CALLPRIVATE v9b0(0x2b3)

    Begin block 0xb9
    prev=[0xae], succ=[0x9b2, 0xc4]
    =================================
    0xba: vba(0xc281309e) = CONST 
    0xbf: vbf = EQ vba(0xc281309e), v34
    0x97f: v97f(0x9b2) = CONST 
    0x980: JUMPI v97f(0x9b2), vbf

    Begin block 0x9b2
    prev=[0xb9], succ=[]
    =================================
    0x9b3: v9b3(0x2d5) = CONST 
    0x9b4: CALLPRIVATE v9b3(0x2d5)

    Begin block 0xc4
    prev=[0xb9], succ=[0x9b5, 0xcf]
    =================================
    0xc5: vc5(0xc915fc93) = CONST 
    0xca: vca = EQ vc5(0xc915fc93), v34
    0x981: v981(0x9b5) = CONST 
    0x982: JUMPI v981(0x9b5), vca

    Begin block 0x9b5
    prev=[0xc4], succ=[]
    =================================
    0x9b6: v9b6(0x2e8) = CONST 
    0x9b7: CALLPRIVATE v9b6(0x2e8)

    Begin block 0xcf
    prev=[0xc4], succ=[0x9b8, 0xda]
    =================================
    0xd0: vd0(0xd55ec697) = CONST 
    0xd5: vd5 = EQ vd0(0xd55ec697), v34
    0x983: v983(0x9b8) = CONST 
    0x984: JUMPI v983(0x9b8), vd5

    Begin block 0x9b8
    prev=[0xcf], succ=[]
    =================================
    0x9b9: v9b9(0x309) = CONST 
    0x9ba: CALLPRIVATE v9b9(0x309)

    Begin block 0xda
    prev=[0xcf], succ=[0x9bb, 0xe5]
    =================================
    0xdb: vdb(0xd67a10e3) = CONST 
    0xe0: ve0 = EQ vdb(0xd67a10e3), v34
    0x985: v985(0x9bb) = CONST 
    0x986: JUMPI v985(0x9bb), ve0

    Begin block 0x9bb
    prev=[0xda], succ=[]
    =================================
    0x9bc: v9bc(0x31c) = CONST 
    0x9bd: CALLPRIVATE v9bc(0x31c)

    Begin block 0xe5
    prev=[0xda], succ=[0x9be, 0xf0]
    =================================
    0xe6: ve6(0xf851a440) = CONST 
    0xeb: veb = EQ ve6(0xf851a440), v34
    0x987: v987(0x9be) = CONST 
    0x988: JUMPI v987(0x9be), veb

    Begin block 0x9be
    prev=[0xe5], succ=[]
    =================================
    0x9bf: v9bf(0x32f) = CONST 
    0x9c0: CALLPRIVATE v9bf(0x32f)

    Begin block 0xf0
    prev=[0xe5], succ=[0x98b, 0x9c1]
    =================================
    0xf1: vf1(0xfe26f16f) = CONST 
    0xf6: vf6 = EQ vf1(0xfe26f16f), v34
    0x989: v989(0x9c1) = CONST 
    0x98a: JUMPI v989(0x9c1), vf6

    Begin block 0x98b
    prev=[0x0, 0xf0], succ=[]
    =================================
    0x98c: v98c(0xfb) = CONST 
    0x98d: CALLPRIVATE v98c(0xfb)

    Begin block 0x9c1
    prev=[0xf0], succ=[]
    =================================
    0x9c2: v9c2(0x342) = CONST 
    0x9c3: CALLPRIVATE v9c2(0x342)

    Begin block 0x98e
    prev=[0xd], succ=[]
    =================================
    0x98f: v98f(0x167) = CONST 
    0x990: CALLPRIVATE v98f(0x167)

}

function orderFills(address,bytes32)() public {
    Begin block 0x167
    prev=[], succ=[0x16e, 0x172]
    =================================
    0x168: v168 = CALLVALUE 
    0x169: v169 = ISZERO v168
    0x16a: v16a(0x172) = CONST 
    0x16d: JUMPI v16a(0x172), v169

    Begin block 0x16e
    prev=[0x167], succ=[]
    =================================
    0x16e: v16e(0x0) = CONST 
    0x171: REVERT v16e(0x0), v16e(0x0)

    Begin block 0x172
    prev=[0x167], succ=[0x364]
    =================================
    0x173: v173(0x623) = CONST 
    0x176: v176(0x1) = CONST 
    0x178: v178(0xa0) = CONST 
    0x17a: v17a(0x2) = CONST 
    0x17c: v17c(0x10000000000000000000000000000000000000000) = EXP v17a(0x2), v178(0xa0)
    0x17d: v17d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17c(0x10000000000000000000000000000000000000000), v176(0x1)
    0x17e: v17e(0x4) = CONST 
    0x180: v180 = CALLDATALOAD v17e(0x4)
    0x181: v181 = AND v180, v17d(0xffffffffffffffffffffffffffffffffffffffff)
    0x182: v182(0x24) = CONST 
    0x184: v184 = CALLDATALOAD v182(0x24)
    0x185: v185(0x364) = CONST 
    0x188: JUMP v185(0x364)

    Begin block 0x364
    prev=[0x172], succ=[0x623]
    =================================
    0x365: v365(0xe) = CONST 
    0x367: v367(0x20) = CONST 
    0x36b: MSTORE v367(0x20), v365(0xe)
    0x36c: v36c(0x0) = CONST 
    0x370: MSTORE v36c(0x0), v181
    0x371: v371(0x40) = CONST 
    0x375: v375 = SHA3 v36c(0x0), v371(0x40)
    0x378: MSTORE v367(0x20), v375
    0x37b: MSTORE v36c(0x0), v184
    0x37d: v37d = SHA3 v36c(0x0), v371(0x40)
    0x37e: v37e = SLOAD v37d
    0x380: JUMP v173(0x623)

    Begin block 0x623
    prev=[0x364], succ=[]
    =================================
    0x624: v624(0x40) = CONST 
    0x626: v626 = MLOAD v624(0x40)
    0x629: MSTORE v626, v37e
    0x62a: v62a(0x20) = CONST 
    0x62c: v62c = ADD v62a(0x20), v626
    0x62d: v62d(0x40) = CONST 
    0x62f: v62f = MLOAD v62d(0x40)
    0x632: v632(0x20) = SUB v62c, v62f
    0x634: RETURN v62f, v632(0x20)

}

function etherDeltaInfo()() public {
    Begin block 0x19b
    prev=[], succ=[0x1a2, 0x1a6]
    =================================
    0x19c: v19c = CALLVALUE 
    0x19d: v19d = ISZERO v19c
    0x19e: v19e(0x1a6) = CONST 
    0x1a1: JUMPI v19e(0x1a6), v19d

    Begin block 0x1a2
    prev=[0x19b], succ=[]
    =================================
    0x1a2: v1a2(0x0) = CONST 
    0x1a5: REVERT v1a2(0x0), v1a2(0x0)

    Begin block 0x1a6
    prev=[0x19b], succ=[0x381]
    =================================
    0x1a7: v1a7(0x1ae) = CONST 
    0x1aa: v1aa(0x381) = CONST 
    0x1ad: JUMP v1aa(0x381)

    Begin block 0x381
    prev=[0x1a6], succ=[0x1ae]
    =================================
    0x382: v382(0x3) = CONST 
    0x384: v384 = SLOAD v382(0x3)
    0x385: v385(0x4) = CONST 
    0x387: v387 = SLOAD v385(0x4)
    0x389: JUMP v1a7(0x1ae)

    Begin block 0x1ae
    prev=[0x381], succ=[]
    =================================
    0x1af: v1af(0x40) = CONST 
    0x1b1: v1b1 = MLOAD v1af(0x40)
    0x1b4: MSTORE v1b1, v384
    0x1b5: v1b5(0x20) = CONST 
    0x1b8: v1b8 = ADD v1b1, v1b5(0x20)
    0x1b9: MSTORE v1b8, v387
    0x1ba: v1ba(0x40) = CONST 
    0x1be: v1be = ADD v1ba(0x40), v1b1
    0x1c0: v1c0 = MLOAD v1ba(0x40)
    0x1c3: v1c3(0x40) = SUB v1be, v1c0
    0x1c5: RETURN v1c0, v1c3(0x40)

}

function proposedTimestamp()() public {
    Begin block 0x1c6
    prev=[], succ=[0x1cd, 0x1d1]
    =================================
    0x1c7: v1c7 = CALLVALUE 
    0x1c8: v1c8 = ISZERO v1c7
    0x1c9: v1c9(0x1d1) = CONST 
    0x1cc: JUMPI v1c9(0x1d1), v1c8

    Begin block 0x1cd
    prev=[0x1c6], succ=[]
    =================================
    0x1cd: v1cd(0x0) = CONST 
    0x1d0: REVERT v1cd(0x0), v1cd(0x0)

    Begin block 0x1d1
    prev=[0x1c6], succ=[0x38a]
    =================================
    0x1d2: v1d2(0x654) = CONST 
    0x1d5: v1d5(0x38a) = CONST 
    0x1d8: JUMP v1d5(0x38a)

    Begin block 0x38a
    prev=[0x1d1], succ=[0x654]
    =================================
    0x38b: v38b(0x11) = CONST 
    0x38d: v38d = SLOAD v38b(0x11)
    0x38f: JUMP v1d2(0x654)

    Begin block 0x654
    prev=[0x38a], succ=[]
    =================================
    0x655: v655(0x40) = CONST 
    0x657: v657 = MLOAD v655(0x40)
    0x65a: MSTORE v657, v38d
    0x65b: v65b(0x20) = CONST 
    0x65d: v65d = ADD v65b(0x20), v657
    0x65e: v65e(0x40) = CONST 
    0x660: v660 = MLOAD v65e(0x40)
    0x663: v663(0x20) = SUB v65d, v660
    0x665: RETURN v660, v663(0x20)

}

function tokens(address,address)() public {
    Begin block 0x1d9
    prev=[], succ=[0x1e0, 0x1e4]
    =================================
    0x1da: v1da = CALLVALUE 
    0x1db: v1db = ISZERO v1da
    0x1dc: v1dc(0x1e4) = CONST 
    0x1df: JUMPI v1dc(0x1e4), v1db

    Begin block 0x1e0
    prev=[0x1d9], succ=[]
    =================================
    0x1e0: v1e0(0x0) = CONST 
    0x1e3: REVERT v1e0(0x0), v1e0(0x0)

    Begin block 0x1e4
    prev=[0x1d9], succ=[0x390]
    =================================
    0x1e5: v1e5(0x685) = CONST 
    0x1e8: v1e8(0x1) = CONST 
    0x1ea: v1ea(0xa0) = CONST 
    0x1ec: v1ec(0x2) = CONST 
    0x1ee: v1ee(0x10000000000000000000000000000000000000000) = EXP v1ec(0x2), v1ea(0xa0)
    0x1ef: v1ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ee(0x10000000000000000000000000000000000000000), v1e8(0x1)
    0x1f0: v1f0(0x4) = CONST 
    0x1f2: v1f2 = CALLDATALOAD v1f0(0x4)
    0x1f4: v1f4 = AND v1ef(0xffffffffffffffffffffffffffffffffffffffff), v1f2
    0x1f6: v1f6(0x24) = CONST 
    0x1f8: v1f8 = CALLDATALOAD v1f6(0x24)
    0x1f9: v1f9 = AND v1f8, v1ef(0xffffffffffffffffffffffffffffffffffffffff)
    0x1fa: v1fa(0x390) = CONST 
    0x1fd: JUMP v1fa(0x390)

    Begin block 0x390
    prev=[0x1e4], succ=[0x685]
    =================================
    0x391: v391(0xc) = CONST 
    0x393: v393(0x20) = CONST 
    0x397: MSTORE v393(0x20), v391(0xc)
    0x398: v398(0x0) = CONST 
    0x39c: MSTORE v398(0x0), v1f4
    0x39d: v39d(0x40) = CONST 
    0x3a1: v3a1 = SHA3 v398(0x0), v39d(0x40)
    0x3a4: MSTORE v393(0x20), v3a1
    0x3a7: MSTORE v398(0x0), v1f9
    0x3a9: v3a9 = SHA3 v398(0x0), v39d(0x40)
    0x3aa: v3aa = SLOAD v3a9
    0x3ac: JUMP v1e5(0x685)

    Begin block 0x685
    prev=[0x390], succ=[]
    =================================
    0x686: v686(0x40) = CONST 
    0x688: v688 = MLOAD v686(0x40)
    0x68b: MSTORE v688, v3aa
    0x68c: v68c(0x20) = CONST 
    0x68e: v68e = ADD v68c(0x20), v688
    0x68f: v68f(0x40) = CONST 
    0x691: v691 = MLOAD v68f(0x40)
    0x694: v694(0x20) = SUB v68e, v691
    0x696: RETURN v691, v694(0x20)

}

function feeAmountThreshold()() public {
    Begin block 0x1fe
    prev=[], succ=[0x205, 0x209]
    =================================
    0x1ff: v1ff = CALLVALUE 
    0x200: v200 = ISZERO v1ff
    0x201: v201(0x209) = CONST 
    0x204: JUMPI v201(0x209), v200

    Begin block 0x205
    prev=[0x1fe], succ=[]
    =================================
    0x205: v205(0x0) = CONST 
    0x208: REVERT v205(0x0), v205(0x0)

    Begin block 0x209
    prev=[0x1fe], succ=[0x3ad]
    =================================
    0x20a: v20a(0x6b6) = CONST 
    0x20d: v20d(0x3ad) = CONST 
    0x210: JUMP v20d(0x3ad)

    Begin block 0x3ad
    prev=[0x209], succ=[0x6b6]
    =================================
    0x3ae: v3ae(0x6) = CONST 
    0x3b0: v3b0 = SLOAD v3ae(0x6)
    0x3b2: JUMP v20a(0x6b6)

    Begin block 0x6b6
    prev=[0x3ad], succ=[]
    =================================
    0x6b7: v6b7(0x40) = CONST 
    0x6b9: v6b9 = MLOAD v6b7(0x40)
    0x6bc: MSTORE v6b9, v3b0
    0x6bd: v6bd(0x20) = CONST 
    0x6bf: v6bf = ADD v6bd(0x20), v6b9
    0x6c0: v6c0(0x40) = CONST 
    0x6c2: v6c2 = MLOAD v6c0(0x40)
    0x6c5: v6c5(0x20) = SUB v6bf, v6c2
    0x6c7: RETURN v6c2, v6c5(0x20)

}

function useEIP712()() public {
    Begin block 0x211
    prev=[], succ=[0x218, 0x21c]
    =================================
    0x212: v212 = CALLVALUE 
    0x213: v213 = ISZERO v212
    0x214: v214(0x21c) = CONST 
    0x217: JUMPI v214(0x21c), v213

    Begin block 0x218
    prev=[0x211], succ=[]
    =================================
    0x218: v218(0x0) = CONST 
    0x21b: REVERT v218(0x0), v218(0x0)

    Begin block 0x21c
    prev=[0x211], succ=[0x3b3]
    =================================
    0x21d: v21d(0x6e7) = CONST 
    0x220: v220(0x3b3) = CONST 
    0x223: JUMP v220(0x3b3)

    Begin block 0x3b3
    prev=[0x21c], succ=[0x6e7]
    =================================
    0x3b4: v3b4(0x7) = CONST 
    0x3b6: v3b6 = SLOAD v3b4(0x7)
    0x3b7: v3b7(0x10000000000000000000000000000000000000000) = CONST 
    0x3ce: v3ce = DIV v3b6, v3b7(0x10000000000000000000000000000000000000000)
    0x3cf: v3cf(0xff) = CONST 
    0x3d1: v3d1 = AND v3cf(0xff), v3ce
    0x3d3: JUMP v21d(0x6e7)

    Begin block 0x6e7
    prev=[0x3b3], succ=[]
    =================================
    0x6e8: v6e8(0x40) = CONST 
    0x6ea: v6ea = MLOAD v6e8(0x40)
    0x6ec: v6ec = ISZERO v3d1
    0x6ed: v6ed = ISZERO v6ec
    0x6ef: MSTORE v6ea, v6ed
    0x6f0: v6f0(0x20) = CONST 
    0x6f2: v6f2 = ADD v6f0(0x20), v6ea
    0x6f3: v6f3(0x40) = CONST 
    0x6f5: v6f5 = MLOAD v6f3(0x40)
    0x6f8: v6f8(0x20) = SUB v6f2, v6f5
    0x6fa: RETURN v6f5, v6f8(0x20)

}

function keyValueStorage()() public {
    Begin block 0x238
    prev=[], succ=[0x23f, 0x243]
    =================================
    0x239: v239 = CALLVALUE 
    0x23a: v23a = ISZERO v239
    0x23b: v23b(0x243) = CONST 
    0x23e: JUMPI v23b(0x243), v23a

    Begin block 0x23f
    prev=[0x238], succ=[]
    =================================
    0x23f: v23f(0x0) = CONST 
    0x242: REVERT v23f(0x0), v23f(0x0)

    Begin block 0x243
    prev=[0x238], succ=[0x3d4]
    =================================
    0x244: v244(0x71a) = CONST 
    0x247: v247(0x3d4) = CONST 
    0x24a: JUMP v247(0x3d4)

    Begin block 0x3d4
    prev=[0x243], succ=[0x71a]
    =================================
    0x3d5: v3d5(0x0) = CONST 
    0x3d7: v3d7 = SLOAD v3d5(0x0)
    0x3d8: v3d8(0x1) = CONST 
    0x3da: v3da(0xa0) = CONST 
    0x3dc: v3dc(0x2) = CONST 
    0x3de: v3de(0x10000000000000000000000000000000000000000) = EXP v3dc(0x2), v3da(0xa0)
    0x3df: v3df(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3de(0x10000000000000000000000000000000000000000), v3d8(0x1)
    0x3e0: v3e0 = AND v3df(0xffffffffffffffffffffffffffffffffffffffff), v3d7
    0x3e2: JUMP v244(0x71a)

    Begin block 0x71a
    prev=[0x3d4], succ=[]
    =================================
    0x71b: v71b(0x40) = CONST 
    0x71d: v71d = MLOAD v71b(0x40)
    0x71e: v71e(0x1) = CONST 
    0x720: v720(0xa0) = CONST 
    0x722: v722(0x2) = CONST 
    0x724: v724(0x10000000000000000000000000000000000000000) = EXP v722(0x2), v720(0xa0)
    0x725: v725(0xffffffffffffffffffffffffffffffffffffffff) = SUB v724(0x10000000000000000000000000000000000000000), v71e(0x1)
    0x728: v728 = AND v3e0, v725(0xffffffffffffffffffffffffffffffffffffffff)
    0x72a: MSTORE v71d, v728
    0x72b: v72b(0x20) = CONST 
    0x72d: v72d = ADD v72b(0x20), v71d
    0x72e: v72e(0x40) = CONST 
    0x730: v730 = MLOAD v72e(0x40)
    0x733: v733(0x20) = SUB v72d, v730
    0x735: RETURN v730, v733(0x20)

}

function feeAccount()() public {
    Begin block 0x267
    prev=[], succ=[0x26e, 0x272]
    =================================
    0x268: v268 = CALLVALUE 
    0x269: v269 = ISZERO v268
    0x26a: v26a(0x272) = CONST 
    0x26d: JUMPI v26a(0x272), v269

    Begin block 0x26e
    prev=[0x267], succ=[]
    =================================
    0x26e: v26e(0x0) = CONST 
    0x271: REVERT v26e(0x0), v26e(0x0)

    Begin block 0x272
    prev=[0x267], succ=[0x3e3]
    =================================
    0x273: v273(0x755) = CONST 
    0x276: v276(0x3e3) = CONST 
    0x279: JUMP v276(0x3e3)

    Begin block 0x3e3
    prev=[0x272], succ=[0x755]
    =================================
    0x3e4: v3e4(0x2) = CONST 
    0x3e6: v3e6 = SLOAD v3e4(0x2)
    0x3e7: v3e7(0x1) = CONST 
    0x3e9: v3e9(0xa0) = CONST 
    0x3eb: v3eb(0x2) = CONST 
    0x3ed: v3ed(0x10000000000000000000000000000000000000000) = EXP v3eb(0x2), v3e9(0xa0)
    0x3ee: v3ee(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ed(0x10000000000000000000000000000000000000000), v3e7(0x1)
    0x3ef: v3ef = AND v3ee(0xffffffffffffffffffffffffffffffffffffffff), v3e6
    0x3f1: JUMP v273(0x755)

    Begin block 0x755
    prev=[0x3e3], succ=[]
    =================================
    0x756: v756(0x40) = CONST 
    0x758: v758 = MLOAD v756(0x40)
    0x759: v759(0x1) = CONST 
    0x75b: v75b(0xa0) = CONST 
    0x75d: v75d(0x2) = CONST 
    0x75f: v75f(0x10000000000000000000000000000000000000000) = EXP v75d(0x2), v75b(0xa0)
    0x760: v760(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75f(0x10000000000000000000000000000000000000000), v759(0x1)
    0x763: v763 = AND v3ef, v760(0xffffffffffffffffffffffffffffffffffffffff)
    0x765: MSTORE v758, v763
    0x766: v766(0x20) = CONST 
    0x768: v768 = ADD v766(0x20), v758
    0x769: v769(0x40) = CONST 
    0x76b: v76b = MLOAD v769(0x40)
    0x76e: v76e(0x20) = SUB v768, v76b
    0x770: RETURN v76b, v76e(0x20)

}

function tradeABIHash()() public {
    Begin block 0x27a
    prev=[], succ=[0x281, 0x285]
    =================================
    0x27b: v27b = CALLVALUE 
    0x27c: v27c = ISZERO v27b
    0x27d: v27d(0x285) = CONST 
    0x280: JUMPI v27d(0x285), v27c

    Begin block 0x281
    prev=[0x27a], succ=[]
    =================================
    0x281: v281(0x0) = CONST 
    0x284: REVERT v281(0x0), v281(0x0)

    Begin block 0x285
    prev=[0x27a], succ=[0x3f2]
    =================================
    0x286: v286(0x790) = CONST 
    0x289: v289(0x3f2) = CONST 
    0x28c: JUMP v289(0x3f2)

    Begin block 0x3f2
    prev=[0x285], succ=[0x790]
    =================================
    0x3f3: v3f3(0x8) = CONST 
    0x3f5: v3f5 = SLOAD v3f3(0x8)
    0x3f7: JUMP v286(0x790)

    Begin block 0x790
    prev=[0x3f2], succ=[]
    =================================
    0x791: v791(0x40) = CONST 
    0x793: v793 = MLOAD v791(0x40)
    0x796: MSTORE v793, v3f5
    0x797: v797(0x20) = CONST 
    0x799: v799 = ADD v797(0x20), v793
    0x79a: v79a(0x40) = CONST 
    0x79c: v79c = MLOAD v79a(0x40)
    0x79f: v79f(0x20) = SUB v799, v79c
    0x7a1: RETURN v79c, v79f(0x20)

}

function getImplementation()() public {
    Begin block 0x28d
    prev=[], succ=[0x294, 0x298]
    =================================
    0x28e: v28e = CALLVALUE 
    0x28f: v28f = ISZERO v28e
    0x290: v290(0x298) = CONST 
    0x293: JUMPI v290(0x298), v28f

    Begin block 0x294
    prev=[0x28d], succ=[]
    =================================
    0x294: v294(0x0) = CONST 
    0x297: REVERT v294(0x0), v294(0x0)

    Begin block 0x298
    prev=[0x28d], succ=[0x355B0x298]
    =================================
    0x299: v299(0x7c1) = CONST 
    0x29c: v29c(0x355) = CONST 
    0x29f: JUMP v29c(0x355)

    Begin block 0x355B0x298
    prev=[0x298], succ=[0x7c1]
    =================================
    0x356S0x298: v356V298(0xf) = CONST 
    0x358S0x298: v358V298 = SLOAD v356V298(0xf)
    0x359S0x298: v359V298(0x1) = CONST 
    0x35bS0x298: v35bV298(0xa0) = CONST 
    0x35dS0x298: v35dV298(0x2) = CONST 
    0x35fS0x298: v35fV298(0x10000000000000000000000000000000000000000) = EXP v35dV298(0x2), v35bV298(0xa0)
    0x360S0x298: v360V298(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35fV298(0x10000000000000000000000000000000000000000), v359V298(0x1)
    0x361S0x298: v361V298 = AND v360V298(0xffffffffffffffffffffffffffffffffffffffff), v358V298
    0x363S0x298: JUMP v299(0x7c1)

    Begin block 0x7c1
    prev=[0x355B0x298], succ=[]
    =================================
    0x7c2: v7c2(0x40) = CONST 
    0x7c4: v7c4 = MLOAD v7c2(0x40)
    0x7c5: v7c5(0x1) = CONST 
    0x7c7: v7c7(0xa0) = CONST 
    0x7c9: v7c9(0x2) = CONST 
    0x7cb: v7cb(0x10000000000000000000000000000000000000000) = EXP v7c9(0x2), v7c7(0xa0)
    0x7cc: v7cc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7cb(0x10000000000000000000000000000000000000000), v7c5(0x1)
    0x7cf: v7cf = AND v361V298, v7cc(0xffffffffffffffffffffffffffffffffffffffff)
    0x7d1: MSTORE v7c4, v7cf
    0x7d2: v7d2(0x20) = CONST 
    0x7d4: v7d4 = ADD v7d2(0x20), v7c4
    0x7d5: v7d5(0x40) = CONST 
    0x7d7: v7d7 = MLOAD v7d5(0x40)
    0x7da: v7da(0x20) = SUB v7d4, v7d7
    0x7dc: RETURN v7d7, v7da(0x20)

}

function proposedImplementation()() public {
    Begin block 0x2a0
    prev=[], succ=[0x2a7, 0x2ab]
    =================================
    0x2a1: v2a1 = CALLVALUE 
    0x2a2: v2a2 = ISZERO v2a1
    0x2a3: v2a3(0x2ab) = CONST 
    0x2a6: JUMPI v2a3(0x2ab), v2a2

    Begin block 0x2a7
    prev=[0x2a0], succ=[]
    =================================
    0x2a7: v2a7(0x0) = CONST 
    0x2aa: REVERT v2a7(0x0), v2a7(0x0)

    Begin block 0x2ab
    prev=[0x2a0], succ=[0x3f8]
    =================================
    0x2ac: v2ac(0x7fc) = CONST 
    0x2af: v2af(0x3f8) = CONST 
    0x2b2: JUMP v2af(0x3f8)

    Begin block 0x3f8
    prev=[0x2ab], succ=[0x7fc]
    =================================
    0x3f9: v3f9(0x10) = CONST 
    0x3fb: v3fb = SLOAD v3f9(0x10)
    0x3fc: v3fc(0x1) = CONST 
    0x3fe: v3fe(0xa0) = CONST 
    0x400: v400(0x2) = CONST 
    0x402: v402(0x10000000000000000000000000000000000000000) = EXP v400(0x2), v3fe(0xa0)
    0x403: v403(0xffffffffffffffffffffffffffffffffffffffff) = SUB v402(0x10000000000000000000000000000000000000000), v3fc(0x1)
    0x404: v404 = AND v403(0xffffffffffffffffffffffffffffffffffffffff), v3fb
    0x406: JUMP v2ac(0x7fc)

    Begin block 0x7fc
    prev=[0x3f8], succ=[]
    =================================
    0x7fd: v7fd(0x40) = CONST 
    0x7ff: v7ff = MLOAD v7fd(0x40)
    0x800: v800(0x1) = CONST 
    0x802: v802(0xa0) = CONST 
    0x804: v804(0x2) = CONST 
    0x806: v806(0x10000000000000000000000000000000000000000) = EXP v804(0x2), v802(0xa0)
    0x807: v807(0xffffffffffffffffffffffffffffffffffffffff) = SUB v806(0x10000000000000000000000000000000000000000), v800(0x1)
    0x80a: v80a = AND v404, v807(0xffffffffffffffffffffffffffffffffffffffff)
    0x80c: MSTORE v7ff, v80a
    0x80d: v80d(0x20) = CONST 
    0x80f: v80f = ADD v80d(0x20), v7ff
    0x810: v810(0x40) = CONST 
    0x812: v812 = MLOAD v810(0x40)
    0x815: v815(0x20) = SUB v80f, v812
    0x817: RETURN v812, v815(0x20)

}

function orders(address,bytes32)() public {
    Begin block 0x2b3
    prev=[], succ=[0x2ba, 0x2be]
    =================================
    0x2b4: v2b4 = CALLVALUE 
    0x2b5: v2b5 = ISZERO v2b4
    0x2b6: v2b6(0x2be) = CONST 
    0x2b9: JUMPI v2b6(0x2be), v2b5

    Begin block 0x2ba
    prev=[0x2b3], succ=[]
    =================================
    0x2ba: v2ba(0x0) = CONST 
    0x2bd: REVERT v2ba(0x0), v2ba(0x0)

    Begin block 0x2be
    prev=[0x2b3], succ=[0x407]
    =================================
    0x2bf: v2bf(0x837) = CONST 
    0x2c2: v2c2(0x1) = CONST 
    0x2c4: v2c4(0xa0) = CONST 
    0x2c6: v2c6(0x2) = CONST 
    0x2c8: v2c8(0x10000000000000000000000000000000000000000) = EXP v2c6(0x2), v2c4(0xa0)
    0x2c9: v2c9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c8(0x10000000000000000000000000000000000000000), v2c2(0x1)
    0x2ca: v2ca(0x4) = CONST 
    0x2cc: v2cc = CALLDATALOAD v2ca(0x4)
    0x2cd: v2cd = AND v2cc, v2c9(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ce: v2ce(0x24) = CONST 
    0x2d0: v2d0 = CALLDATALOAD v2ce(0x24)
    0x2d1: v2d1(0x407) = CONST 
    0x2d4: JUMP v2d1(0x407)

    Begin block 0x407
    prev=[0x2be], succ=[0x837]
    =================================
    0x408: v408(0xd) = CONST 
    0x40a: v40a(0x20) = CONST 
    0x40e: MSTORE v40a(0x20), v408(0xd)
    0x40f: v40f(0x0) = CONST 
    0x413: MSTORE v40f(0x0), v2cd
    0x414: v414(0x40) = CONST 
    0x418: v418 = SHA3 v40f(0x0), v414(0x40)
    0x41b: MSTORE v40a(0x20), v418
    0x41e: MSTORE v40f(0x0), v2d0
    0x420: v420 = SHA3 v40f(0x0), v414(0x40)
    0x421: v421 = SLOAD v420
    0x422: v422(0xff) = CONST 
    0x424: v424 = AND v422(0xff), v421
    0x426: JUMP v2bf(0x837)

    Begin block 0x837
    prev=[0x407], succ=[]
    =================================
    0x838: v838(0x40) = CONST 
    0x83a: v83a = MLOAD v838(0x40)
    0x83c: v83c = ISZERO v424
    0x83d: v83d = ISZERO v83c
    0x83f: MSTORE v83a, v83d
    0x840: v840(0x20) = CONST 
    0x842: v842 = ADD v840(0x20), v83a
    0x843: v843(0x40) = CONST 
    0x845: v845 = MLOAD v843(0x40)
    0x848: v848(0x20) = SUB v842, v845
    0x84a: RETURN v845, v848(0x20)

}

function feeTake()() public {
    Begin block 0x2d5
    prev=[], succ=[0x2dc, 0x2e0]
    =================================
    0x2d6: v2d6 = CALLVALUE 
    0x2d7: v2d7 = ISZERO v2d6
    0x2d8: v2d8(0x2e0) = CONST 
    0x2db: JUMPI v2d8(0x2e0), v2d7

    Begin block 0x2dc
    prev=[0x2d5], succ=[]
    =================================
    0x2dc: v2dc(0x0) = CONST 
    0x2df: REVERT v2dc(0x0), v2dc(0x0)

    Begin block 0x2e0
    prev=[0x2d5], succ=[0x427]
    =================================
    0x2e1: v2e1(0x86a) = CONST 
    0x2e4: v2e4(0x427) = CONST 
    0x2e7: JUMP v2e4(0x427)

    Begin block 0x427
    prev=[0x2e0], succ=[0x86a]
    =================================
    0x428: v428(0x5) = CONST 
    0x42a: v42a = SLOAD v428(0x5)
    0x42c: JUMP v2e1(0x86a)

    Begin block 0x86a
    prev=[0x427], succ=[]
    =================================
    0x86b: v86b(0x40) = CONST 
    0x86d: v86d = MLOAD v86b(0x40)
    0x870: MSTORE v86d, v42a
    0x871: v871(0x20) = CONST 
    0x873: v873 = ADD v871(0x20), v86d
    0x874: v874(0x40) = CONST 
    0x876: v876 = MLOAD v874(0x40)
    0x879: v879(0x20) = SUB v873, v876
    0x87b: RETURN v876, v879(0x20)

}

function proposeUpgrade(address)() public {
    Begin block 0x2e8
    prev=[], succ=[0x2ef, 0x2f3]
    =================================
    0x2e9: v2e9 = CALLVALUE 
    0x2ea: v2ea = ISZERO v2e9
    0x2eb: v2eb(0x2f3) = CONST 
    0x2ee: JUMPI v2eb(0x2f3), v2ea

    Begin block 0x2ef
    prev=[0x2e8], succ=[]
    =================================
    0x2ef: v2ef(0x0) = CONST 
    0x2f2: REVERT v2ef(0x0), v2ef(0x0)

    Begin block 0x2f3
    prev=[0x2e8], succ=[0x42d]
    =================================
    0x2f4: v2f4(0x89b) = CONST 
    0x2f7: v2f7(0x1) = CONST 
    0x2f9: v2f9(0xa0) = CONST 
    0x2fb: v2fb(0x2) = CONST 
    0x2fd: v2fd(0x10000000000000000000000000000000000000000) = EXP v2fb(0x2), v2f9(0xa0)
    0x2fe: v2fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2fd(0x10000000000000000000000000000000000000000), v2f7(0x1)
    0x2ff: v2ff(0x4) = CONST 
    0x301: v301 = CALLDATALOAD v2ff(0x4)
    0x302: v302 = AND v301, v2fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x303: v303(0x42d) = CONST 
    0x306: JUMP v303(0x42d)

    Begin block 0x42d
    prev=[0x2f3], succ=[0x444, 0x448]
    =================================
    0x42e: v42e(0x1) = CONST 
    0x430: v430 = SLOAD v42e(0x1)
    0x431: v431 = CALLER 
    0x432: v432(0x1) = CONST 
    0x434: v434(0xa0) = CONST 
    0x436: v436(0x2) = CONST 
    0x438: v438(0x10000000000000000000000000000000000000000) = EXP v436(0x2), v434(0xa0)
    0x439: v439(0xffffffffffffffffffffffffffffffffffffffff) = SUB v438(0x10000000000000000000000000000000000000000), v432(0x1)
    0x43c: v43c = AND v439(0xffffffffffffffffffffffffffffffffffffffff), v431
    0x43e: v43e = AND v430, v439(0xffffffffffffffffffffffffffffffffffffffff)
    0x43f: v43f = EQ v43e, v43c
    0x440: v440(0x448) = CONST 
    0x443: JUMPI v440(0x448), v43f

    Begin block 0x444
    prev=[0x42d], succ=[]
    =================================
    0x444: v444(0x0) = CONST 
    0x447: REVERT v444(0x0), v444(0x0)

    Begin block 0x448
    prev=[0x42d], succ=[0x45f, 0x463]
    =================================
    0x449: v449(0xf) = CONST 
    0x44b: v44b = SLOAD v449(0xf)
    0x44c: v44c(0x1) = CONST 
    0x44e: v44e(0xa0) = CONST 
    0x450: v450(0x2) = CONST 
    0x452: v452(0x10000000000000000000000000000000000000000) = EXP v450(0x2), v44e(0xa0)
    0x453: v453(0xffffffffffffffffffffffffffffffffffffffff) = SUB v452(0x10000000000000000000000000000000000000000), v44c(0x1)
    0x456: v456 = AND v453(0xffffffffffffffffffffffffffffffffffffffff), v302
    0x458: v458 = AND v44b, v453(0xffffffffffffffffffffffffffffffffffffffff)
    0x459: v459 = EQ v458, v456
    0x45a: v45a = ISZERO v459
    0x45b: v45b(0x463) = CONST 
    0x45e: JUMPI v45b(0x463), v45a

    Begin block 0x45f
    prev=[0x448], succ=[]
    =================================
    0x45f: v45f(0x0) = CONST 
    0x462: REVERT v45f(0x0), v45f(0x0)

    Begin block 0x463
    prev=[0x448], succ=[0x474, 0x478]
    =================================
    0x464: v464(0x1) = CONST 
    0x466: v466(0xa0) = CONST 
    0x468: v468(0x2) = CONST 
    0x46a: v46a(0x10000000000000000000000000000000000000000) = EXP v468(0x2), v466(0xa0)
    0x46b: v46b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v46a(0x10000000000000000000000000000000000000000), v464(0x1)
    0x46d: v46d = AND v302, v46b(0xffffffffffffffffffffffffffffffffffffffff)
    0x46e: v46e = ISZERO v46d
    0x46f: v46f = ISZERO v46e
    0x470: v470(0x478) = CONST 
    0x473: JUMPI v470(0x478), v46f

    Begin block 0x474
    prev=[0x463], succ=[]
    =================================
    0x474: v474(0x0) = CONST 
    0x477: REVERT v474(0x0), v474(0x0)

    Begin block 0x478
    prev=[0x463], succ=[0x89b]
    =================================
    0x479: v479(0x10) = CONST 
    0x47c: v47c = SLOAD v479(0x10)
    0x47d: v47d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x492: v492(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v47d(0xffffffffffffffffffffffffffffffffffffffff)
    0x493: v493 = AND v492(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v47c
    0x494: v494(0x1) = CONST 
    0x496: v496(0xa0) = CONST 
    0x498: v498(0x2) = CONST 
    0x49a: v49a(0x10000000000000000000000000000000000000000) = EXP v498(0x2), v496(0xa0)
    0x49b: v49b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49a(0x10000000000000000000000000000000000000000), v494(0x1)
    0x49e: v49e = AND v49b(0xffffffffffffffffffffffffffffffffffffffff), v302
    0x4a2: v4a2 = OR v49e, v493
    0x4a6: SSTORE v479(0x10), v4a2
    0x4a7: v4a7 = TIMESTAMP 
    0x4a8: v4a8(0x127500) = CONST 
    0x4ad: v4ad = ADD v4a7, v4a8(0x127500)
    0x4ae: v4ae(0x11) = CONST 
    0x4b0: SSTORE v4ae(0x11), v4ad
    0x4b1: v4b1(0xec67bbd1e1c0c74039cb44e4ee8278b388155a131c81387e07f800c16f776e83) = CONST 
    0x4d5: v4d5 = AND v49b(0xffffffffffffffffffffffffffffffffffffffff), v4a2
    0x4d7: v4d7(0x40) = CONST 
    0x4d9: v4d9 = MLOAD v4d7(0x40)
    0x4da: v4da(0x1) = CONST 
    0x4dc: v4dc(0xa0) = CONST 
    0x4de: v4de(0x2) = CONST 
    0x4e0: v4e0(0x10000000000000000000000000000000000000000) = EXP v4de(0x2), v4dc(0xa0)
    0x4e1: v4e1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e0(0x10000000000000000000000000000000000000000), v4da(0x1)
    0x4e4: v4e4 = AND v4d5, v4e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e6: MSTORE v4d9, v4e4
    0x4e7: v4e7(0x20) = CONST 
    0x4ea: v4ea = ADD v4d9, v4e7(0x20)
    0x4eb: MSTORE v4ea, v4a7
    0x4ec: v4ec(0x40) = CONST 
    0x4f0: v4f0 = ADD v4ec(0x40), v4d9
    0x4f2: v4f2 = MLOAD v4ec(0x40)
    0x4f5: v4f5(0x40) = SUB v4f0, v4f2
    0x4f7: LOG1 v4f2, v4f5(0x40), v4b1(0xec67bbd1e1c0c74039cb44e4ee8278b388155a131c81387e07f800c16f776e83)
    0x4f9: JUMP v2f4(0x89b)

    Begin block 0x89b
    prev=[0x478], succ=[]
    =================================
    0x89c: STOP 

}

function upgrade()() public {
    Begin block 0x309
    prev=[], succ=[0x310, 0x314]
    =================================
    0x30a: v30a = CALLVALUE 
    0x30b: v30b = ISZERO v30a
    0x30c: v30c(0x314) = CONST 
    0x30f: JUMPI v30c(0x314), v30b

    Begin block 0x310
    prev=[0x309], succ=[]
    =================================
    0x310: v310(0x0) = CONST 
    0x313: REVERT v310(0x0), v310(0x0)

    Begin block 0x314
    prev=[0x309], succ=[0x4fa]
    =================================
    0x315: v315(0x8bc) = CONST 
    0x318: v318(0x4fa) = CONST 
    0x31b: JUMP v318(0x4fa)

    Begin block 0x4fa
    prev=[0x314], succ=[0x511, 0x515]
    =================================
    0x4fb: v4fb(0x1) = CONST 
    0x4fd: v4fd = SLOAD v4fb(0x1)
    0x4fe: v4fe = CALLER 
    0x4ff: v4ff(0x1) = CONST 
    0x501: v501(0xa0) = CONST 
    0x503: v503(0x2) = CONST 
    0x505: v505(0x10000000000000000000000000000000000000000) = EXP v503(0x2), v501(0xa0)
    0x506: v506(0xffffffffffffffffffffffffffffffffffffffff) = SUB v505(0x10000000000000000000000000000000000000000), v4ff(0x1)
    0x509: v509 = AND v506(0xffffffffffffffffffffffffffffffffffffffff), v4fe
    0x50b: v50b = AND v4fd, v506(0xffffffffffffffffffffffffffffffffffffffff)
    0x50c: v50c = EQ v50b, v509
    0x50d: v50d(0x515) = CONST 
    0x510: JUMPI v50d(0x515), v50c

    Begin block 0x511
    prev=[0x4fa], succ=[]
    =================================
    0x511: v511(0x0) = CONST 
    0x514: REVERT v511(0x0), v511(0x0)

    Begin block 0x515
    prev=[0x4fa], succ=[0x528, 0x52c]
    =================================
    0x516: v516(0x10) = CONST 
    0x518: v518 = SLOAD v516(0x10)
    0x519: v519(0x1) = CONST 
    0x51b: v51b(0xa0) = CONST 
    0x51d: v51d(0x2) = CONST 
    0x51f: v51f(0x10000000000000000000000000000000000000000) = EXP v51d(0x2), v51b(0xa0)
    0x520: v520(0xffffffffffffffffffffffffffffffffffffffff) = SUB v51f(0x10000000000000000000000000000000000000000), v519(0x1)
    0x521: v521 = AND v520(0xffffffffffffffffffffffffffffffffffffffff), v518
    0x522: v522 = ISZERO v521
    0x523: v523 = ISZERO v522
    0x524: v524(0x52c) = CONST 
    0x527: JUMPI v524(0x52c), v523

    Begin block 0x528
    prev=[0x515], succ=[]
    =================================
    0x528: v528(0x0) = CONST 
    0x52b: REVERT v528(0x0), v528(0x0)

    Begin block 0x52c
    prev=[0x515], succ=[0x537, 0x53b]
    =================================
    0x52d: v52d(0x11) = CONST 
    0x52f: v52f = SLOAD v52d(0x11)
    0x530: v530 = TIMESTAMP 
    0x532: v532 = LT v52f, v530
    0x533: v533(0x53b) = CONST 
    0x536: JUMPI v533(0x53b), v532

    Begin block 0x537
    prev=[0x52c], succ=[]
    =================================
    0x537: v537(0x0) = CONST 
    0x53a: REVERT v537(0x0), v537(0x0)

    Begin block 0x53b
    prev=[0x52c], succ=[0x8bc]
    =================================
    0x53c: v53c(0x10) = CONST 
    0x53e: v53e = SLOAD v53c(0x10)
    0x53f: v53f(0xf) = CONST 
    0x542: v542 = SLOAD v53f(0xf)
    0x543: v543(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x558: v558(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v543(0xffffffffffffffffffffffffffffffffffffffff)
    0x559: v559 = AND v558(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v542
    0x55a: v55a(0x1) = CONST 
    0x55c: v55c(0xa0) = CONST 
    0x55e: v55e(0x2) = CONST 
    0x560: v560(0x10000000000000000000000000000000000000000) = EXP v55e(0x2), v55c(0xa0)
    0x561: v561(0xffffffffffffffffffffffffffffffffffffffff) = SUB v560(0x10000000000000000000000000000000000000000), v55a(0x1)
    0x564: v564 = AND v561(0xffffffffffffffffffffffffffffffffffffffff), v53e
    0x565: v565 = OR v564, v559
    0x569: SSTORE v53f(0xf), v565
    0x56a: v56a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x58c: v58c = AND v561(0xffffffffffffffffffffffffffffffffffffffff), v565
    0x58d: v58d(0x40) = CONST 
    0x58f: v58f = MLOAD v58d(0x40)
    0x590: v590(0x1) = CONST 
    0x592: v592(0xa0) = CONST 
    0x594: v594(0x2) = CONST 
    0x596: v596(0x10000000000000000000000000000000000000000) = EXP v594(0x2), v592(0xa0)
    0x597: v597(0xffffffffffffffffffffffffffffffffffffffff) = SUB v596(0x10000000000000000000000000000000000000000), v590(0x1)
    0x59a: v59a = AND v58c, v597(0xffffffffffffffffffffffffffffffffffffffff)
    0x59c: MSTORE v58f, v59a
    0x59d: v59d(0x20) = CONST 
    0x59f: v59f = ADD v59d(0x20), v58f
    0x5a0: v5a0(0x40) = CONST 
    0x5a2: v5a2 = MLOAD v5a0(0x40)
    0x5a5: v5a5(0x20) = SUB v59f, v5a2
    0x5a7: LOG1 v5a2, v5a5(0x20), v56a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b)
    0x5a8: JUMP v315(0x8bc)

    Begin block 0x8bc
    prev=[0x53b], succ=[]
    =================================
    0x8bd: STOP 

}

function etherDelta()() public {
    Begin block 0x31c
    prev=[], succ=[0x323, 0x327]
    =================================
    0x31d: v31d = CALLVALUE 
    0x31e: v31e = ISZERO v31d
    0x31f: v31f(0x327) = CONST 
    0x322: JUMPI v31f(0x327), v31e

    Begin block 0x323
    prev=[0x31c], succ=[]
    =================================
    0x323: v323(0x0) = CONST 
    0x326: REVERT v323(0x0), v323(0x0)

    Begin block 0x327
    prev=[0x31c], succ=[0x5a9]
    =================================
    0x328: v328(0x8dd) = CONST 
    0x32b: v32b(0x5a9) = CONST 
    0x32e: JUMP v32b(0x5a9)

    Begin block 0x5a9
    prev=[0x327], succ=[0x8dd]
    =================================
    0x5aa: v5aa(0x7) = CONST 
    0x5ac: v5ac = SLOAD v5aa(0x7)
    0x5ad: v5ad(0x1) = CONST 
    0x5af: v5af(0xa0) = CONST 
    0x5b1: v5b1(0x2) = CONST 
    0x5b3: v5b3(0x10000000000000000000000000000000000000000) = EXP v5b1(0x2), v5af(0xa0)
    0x5b4: v5b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5b3(0x10000000000000000000000000000000000000000), v5ad(0x1)
    0x5b5: v5b5 = AND v5b4(0xffffffffffffffffffffffffffffffffffffffff), v5ac
    0x5b7: JUMP v328(0x8dd)

    Begin block 0x8dd
    prev=[0x5a9], succ=[]
    =================================
    0x8de: v8de(0x40) = CONST 
    0x8e0: v8e0 = MLOAD v8de(0x40)
    0x8e1: v8e1(0x1) = CONST 
    0x8e3: v8e3(0xa0) = CONST 
    0x8e5: v8e5(0x2) = CONST 
    0x8e7: v8e7(0x10000000000000000000000000000000000000000) = EXP v8e5(0x2), v8e3(0xa0)
    0x8e8: v8e8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8e7(0x10000000000000000000000000000000000000000), v8e1(0x1)
    0x8eb: v8eb = AND v5b5, v8e8(0xffffffffffffffffffffffffffffffffffffffff)
    0x8ed: MSTORE v8e0, v8eb
    0x8ee: v8ee(0x20) = CONST 
    0x8f0: v8f0 = ADD v8ee(0x20), v8e0
    0x8f1: v8f1(0x40) = CONST 
    0x8f3: v8f3 = MLOAD v8f1(0x40)
    0x8f6: v8f6(0x20) = SUB v8f0, v8f3
    0x8f8: RETURN v8f3, v8f6(0x20)

}

function admin()() public {
    Begin block 0x32f
    prev=[], succ=[0x336, 0x33a]
    =================================
    0x330: v330 = CALLVALUE 
    0x331: v331 = ISZERO v330
    0x332: v332(0x33a) = CONST 
    0x335: JUMPI v332(0x33a), v331

    Begin block 0x336
    prev=[0x32f], succ=[]
    =================================
    0x336: v336(0x0) = CONST 
    0x339: REVERT v336(0x0), v336(0x0)

    Begin block 0x33a
    prev=[0x32f], succ=[0x5b8]
    =================================
    0x33b: v33b(0x918) = CONST 
    0x33e: v33e(0x5b8) = CONST 
    0x341: JUMP v33e(0x5b8)

    Begin block 0x5b8
    prev=[0x33a], succ=[0x918]
    =================================
    0x5b9: v5b9(0x1) = CONST 
    0x5bb: v5bb = SLOAD v5b9(0x1)
    0x5bc: v5bc(0x1) = CONST 
    0x5be: v5be(0xa0) = CONST 
    0x5c0: v5c0(0x2) = CONST 
    0x5c2: v5c2(0x10000000000000000000000000000000000000000) = EXP v5c0(0x2), v5be(0xa0)
    0x5c3: v5c3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5c2(0x10000000000000000000000000000000000000000), v5bc(0x1)
    0x5c4: v5c4 = AND v5c3(0xffffffffffffffffffffffffffffffffffffffff), v5bb
    0x5c6: JUMP v33b(0x918)

    Begin block 0x918
    prev=[0x5b8], succ=[]
    =================================
    0x919: v919(0x40) = CONST 
    0x91b: v91b = MLOAD v919(0x40)
    0x91c: v91c(0x1) = CONST 
    0x91e: v91e(0xa0) = CONST 
    0x920: v920(0x2) = CONST 
    0x922: v922(0x10000000000000000000000000000000000000000) = EXP v920(0x2), v91e(0xa0)
    0x923: v923(0xffffffffffffffffffffffffffffffffffffffff) = SUB v922(0x10000000000000000000000000000000000000000), v91c(0x1)
    0x926: v926 = AND v5c4, v923(0xffffffffffffffffffffffffffffffffffffffff)
    0x928: MSTORE v91b, v926
    0x929: v929(0x20) = CONST 
    0x92b: v92b = ADD v929(0x20), v91b
    0x92c: v92c(0x40) = CONST 
    0x92e: v92e = MLOAD v92c(0x40)
    0x931: v931(0x20) = SUB v92b, v92e
    0x933: RETURN v92e, v931(0x20)

}

function withdrawABIHash()() public {
    Begin block 0x342
    prev=[], succ=[0x349, 0x34d]
    =================================
    0x343: v343 = CALLVALUE 
    0x344: v344 = ISZERO v343
    0x345: v345(0x34d) = CONST 
    0x348: JUMPI v345(0x34d), v344

    Begin block 0x349
    prev=[0x342], succ=[]
    =================================
    0x349: v349(0x0) = CONST 
    0x34c: REVERT v349(0x0), v349(0x0)

    Begin block 0x34d
    prev=[0x342], succ=[0x5c7]
    =================================
    0x34e: v34e(0x953) = CONST 
    0x351: v351(0x5c7) = CONST 
    0x354: JUMP v351(0x5c7)

    Begin block 0x5c7
    prev=[0x34d], succ=[0x953]
    =================================
    0x5c8: v5c8(0x9) = CONST 
    0x5ca: v5ca = SLOAD v5c8(0x9)
    0x5cc: JUMP v34e(0x953)

    Begin block 0x953
    prev=[0x5c7], succ=[]
    =================================
    0x954: v954(0x40) = CONST 
    0x956: v956 = MLOAD v954(0x40)
    0x959: MSTORE v956, v5ca
    0x95a: v95a(0x20) = CONST 
    0x95c: v95c = ADD v95a(0x20), v956
    0x95d: v95d(0x40) = CONST 
    0x95f: v95f = MLOAD v95d(0x40)
    0x962: v962(0x20) = SUB v95c, v95f
    0x964: RETURN v95f, v962(0x20)

}

function fallback()() public {
    Begin block 0xfb
    prev=[], succ=[0x5cd]
    =================================
    0xfc: vfc(0x103) = CONST 
    0xff: vff(0x5cd) = CONST 
    0x102: JUMP vff(0x5cd)

    Begin block 0x5cd
    prev=[0xfb], succ=[0x103]
    =================================
    0x5ce: v5ce(0x20) = CONST 
    0x5d0: v5d0(0x40) = CONST 
    0x5d2: v5d2 = MLOAD v5d0(0x40)
    0x5d5: v5d5 = ADD v5d2, v5ce(0x20)
    0x5d6: v5d6(0x40) = CONST 
    0x5d8: MSTORE v5d6(0x40), v5d5
    0x5d9: v5d9(0x0) = CONST 
    0x5dc: MSTORE v5d2, v5d9(0x0)
    0x5de: JUMP vfc(0x103)

    Begin block 0x103
    prev=[0x5cd], succ=[0x355B0x103]
    =================================
    0x104: v104(0x0) = CONST 
    0x107: v107 = CALLDATASIZE 
    0x10a: v10a(0x1f) = CONST 
    0x10c: v10c = ADD v10a(0x1f), v107
    0x10d: v10d(0x20) = CONST 
    0x111: v111 = DIV v10c, v10d(0x20)
    0x112: v112 = MUL v111, v10d(0x20)
    0x113: v113(0x20) = CONST 
    0x115: v115 = ADD v113(0x20), v112
    0x116: v116(0x40) = CONST 
    0x118: v118 = MLOAD v116(0x40)
    0x11b: v11b = ADD v118, v115
    0x11c: v11c(0x40) = CONST 
    0x11e: MSTORE v11c(0x40), v11b
    0x121: MSTORE v118, v107
    0x125: v125(0x20) = CONST 
    0x128: v128 = ADD v118, v125(0x20)
    0x12e: CALLDATACOPY v128, v104(0x0), v107
    0x130: v130 = ADD v128, v107
    0x13a: v13a(0x141) = CONST 
    0x13d: v13d(0x355) = CONST 
    0x140: JUMP v13d(0x355)

    Begin block 0x355B0x103
    prev=[0x103], succ=[0x141]
    =================================
    0x356S0x103: v356V103(0xf) = CONST 
    0x358S0x103: v358V103 = SLOAD v356V103(0xf)
    0x359S0x103: v359V103(0x1) = CONST 
    0x35bS0x103: v35bV103(0xa0) = CONST 
    0x35dS0x103: v35dV103(0x2) = CONST 
    0x35fS0x103: v35fV103(0x10000000000000000000000000000000000000000) = EXP v35dV103(0x2), v35bV103(0xa0)
    0x360S0x103: v360V103(0xffffffffffffffffffffffffffffffffffffffff) = SUB v35fV103(0x10000000000000000000000000000000000000000), v359V103(0x1)
    0x361S0x103: v361V103 = AND v360V103(0xffffffffffffffffffffffffffffffffffffffff), v358V103
    0x363S0x103: JUMP v13a(0x141)

    Begin block 0x141
    prev=[0x355B0x103], succ=[0x163, 0x160]
    =================================
    0x144: v144(0x0) = CONST 
    0x148: v148 = MLOAD v118
    0x149: v149(0x20) = CONST 
    0x14c: v14c = ADD v118, v149(0x20)
    0x14e: v14e = GAS 
    0x14f: v14f = DELEGATECALL v14e, v361V103, v14c, v148, v144(0x0), v144(0x0)
    0x150: v150 = RETURNDATASIZE 
    0x151: v151(0x40) = CONST 
    0x153: v153 = MLOAD v151(0x40)
    0x155: v155(0x0) = CONST 
    0x158: RETURNDATACOPY v153, v155(0x0), v150
    0x15b: v15b = ISZERO v14f
    0x15c: v15c(0x163) = CONST 
    0x15f: JUMPI v15c(0x163), v15b

    Begin block 0x163
    prev=[0x141], succ=[]
    =================================
    0x166: REVERT v153, v150

    Begin block 0x160
    prev=[0x141], succ=[]
    =================================
    0x162: RETURN v153, v150

}

