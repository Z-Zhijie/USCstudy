function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xc00]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xbd1: vbd1(0xc00) = CONST 
    0xbd2: JUMPI vbd1(0xc00), v8

    Begin block 0xd
    prev=[0x0], succ=[0x76, 0x3b]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x31: v31(0x8f32d59b) = CONST 
    0x36: v36 = GT v31(0x8f32d59b), v2f
    0x37: v37(0x76) = CONST 
    0x3a: JUMPI v37(0x76), v36

    Begin block 0x76
    prev=[0xd], succ=[0xbe5, 0x82]
    =================================
    0x78: v78(0x204e1c7a) = CONST 
    0x7d: v7d = EQ v78(0x204e1c7a), v2f
    0xbdd: vbdd(0xbe5) = CONST 
    0xbde: JUMPI vbdd(0xbe5), v7d

    Begin block 0xbe5
    prev=[0x76], succ=[]
    =================================
    0xbe6: vbe6(0xa8) = CONST 
    0xbe7: CALLPRIVATE vbe6(0xa8)

    Begin block 0x82
    prev=[0x76], succ=[0xbe8, 0x8d]
    =================================
    0x83: v83(0x715018a6) = CONST 
    0x88: v88 = EQ v83(0x715018a6), v2f
    0xbdf: vbdf(0xbe8) = CONST 
    0xbe0: JUMPI vbdf(0xbe8), v88

    Begin block 0xbe8
    prev=[0x82], succ=[]
    =================================
    0xbe9: vbe9(0x139) = CONST 
    0xbea: CALLPRIVATE vbe9(0x139)

    Begin block 0x8d
    prev=[0x82], succ=[0xbeb, 0x98]
    =================================
    0x8e: v8e(0x7eff275e) = CONST 
    0x93: v93 = EQ v8e(0x7eff275e), v2f
    0xbe1: vbe1(0xbeb) = CONST 
    0xbe2: JUMPI vbe1(0xbeb), v93

    Begin block 0xbeb
    prev=[0x8d], succ=[]
    =================================
    0xbec: vbec(0x150) = CONST 
    0xbed: CALLPRIVATE vbec(0x150)

    Begin block 0x98
    prev=[0x8d], succ=[0xbee, 0xa3]
    =================================
    0x99: v99(0x8da5cb5b) = CONST 
    0x9e: v9e = EQ v99(0x8da5cb5b), v2f
    0xbe3: vbe3(0xbee) = CONST 
    0xbe4: JUMPI vbe3(0xbee), v9e

    Begin block 0xbee
    prev=[0x98], succ=[]
    =================================
    0xbef: vbef(0x1c1) = CONST 
    0xbf0: CALLPRIVATE vbef(0x1c1)

    Begin block 0xa3
    prev=[0x98], succ=[]
    =================================
    0xa4: va4(0x0) = CONST 
    0xa7: REVERT va4(0x0), va4(0x0)

    Begin block 0x3b
    prev=[0xd], succ=[0xbf1, 0x46]
    =================================
    0x3c: v3c(0x8f32d59b) = CONST 
    0x41: v41 = EQ v3c(0x8f32d59b), v2f
    0xbd3: vbd3(0xbf1) = CONST 
    0xbd4: JUMPI vbd3(0xbf1), v41

    Begin block 0xbf1
    prev=[0x3b], succ=[]
    =================================
    0xbf2: vbf2(0x218) = CONST 
    0xbf3: CALLPRIVATE vbf2(0x218)

    Begin block 0x46
    prev=[0x3b], succ=[0xbf4, 0x51]
    =================================
    0x47: v47(0x9623609d) = CONST 
    0x4c: v4c = EQ v47(0x9623609d), v2f
    0xbd5: vbd5(0xbf4) = CONST 
    0xbd6: JUMPI vbd5(0xbf4), v4c

    Begin block 0xbf4
    prev=[0x46], succ=[]
    =================================
    0xbf5: vbf5(0x247) = CONST 
    0xbf6: CALLPRIVATE vbf5(0x247)

    Begin block 0x51
    prev=[0x46], succ=[0xbf7, 0x5c]
    =================================
    0x52: v52(0x99a88ec4) = CONST 
    0x57: v57 = EQ v52(0x99a88ec4), v2f
    0xbd7: vbd7(0xbf7) = CONST 
    0xbd8: JUMPI vbd7(0xbf7), v57

    Begin block 0xbf7
    prev=[0x51], succ=[]
    =================================
    0xbf8: vbf8(0x342) = CONST 
    0xbf9: CALLPRIVATE vbf8(0x342)

    Begin block 0x5c
    prev=[0x51], succ=[0xbfa, 0x67]
    =================================
    0x5d: v5d(0xf2fde38b) = CONST 
    0x62: v62 = EQ v5d(0xf2fde38b), v2f
    0xbd9: vbd9(0xbfa) = CONST 
    0xbda: JUMPI vbd9(0xbfa), v62

    Begin block 0xbfa
    prev=[0x5c], succ=[]
    =================================
    0xbfb: vbfb(0x3b3) = CONST 
    0xbfc: CALLPRIVATE vbfb(0x3b3)

    Begin block 0x67
    prev=[0x5c], succ=[0x72, 0xbfd]
    =================================
    0x68: v68(0xf3b7dead) = CONST 
    0x6d: v6d = EQ v68(0xf3b7dead), v2f
    0xbdb: vbdb(0xbfd) = CONST 
    0xbdc: JUMPI vbdb(0xbfd), v6d

    Begin block 0x72
    prev=[0x67], succ=[0xbcc]
    =================================
    0x72: v72(0xbcc) = CONST 
    0x75: JUMP v72(0xbcc)

    Begin block 0xbcc
    prev=[0x72], succ=[]
    =================================
    0xbcd: vbcd(0x0) = CONST 
    0xbd0: REVERT vbcd(0x0), vbcd(0x0)

    Begin block 0xbfd
    prev=[0x67], succ=[]
    =================================
    0xbfe: vbfe(0x404) = CONST 
    0xbff: CALLPRIVATE vbfe(0x404)

    Begin block 0xc00
    prev=[0x0], succ=[]
    =================================
    0xc01: vc01(0xba8) = CONST 
    0xc02: CALLPRIVATE vc01(0xba8)

}

function renounceOwnership()() public {
    Begin block 0x139
    prev=[], succ=[0x141, 0x145]
    =================================
    0x13a: v13a = CALLVALUE 
    0x13c: v13c = ISZERO v13a
    0x13d: v13d(0x145) = CONST 
    0x140: JUMPI v13d(0x145), v13c

    Begin block 0x141
    prev=[0x139], succ=[]
    =================================
    0x141: v141(0x0) = CONST 
    0x144: REVERT v141(0x0), v141(0x0)

    Begin block 0x145
    prev=[0x139], succ=[0x55f]
    =================================
    0x147: v147(0x14e) = CONST 
    0x14a: v14a(0x55f) = CONST 
    0x14d: JUMP v14a(0x55f)

    Begin block 0x55f
    prev=[0x145], succ=[0x724B0x55f]
    =================================
    0x560: v560(0x567) = CONST 
    0x563: v563(0x724) = CONST 
    0x566: JUMP v563(0x724)

    Begin block 0x724B0x55f
    prev=[0x55f], succ=[0x567]
    =================================
    0x725S0x55f: v725V55f(0x0) = CONST 
    0x728S0x55f: v728V55f(0x0) = CONST 
    0x72bS0x55f: v72bV55f = SLOAD v725V55f(0x0)
    0x72dS0x55f: v72dV55f(0x100) = CONST 
    0x730S0x55f: v730V55f(0x1) = EXP v72dV55f(0x100), v728V55f(0x0)
    0x732S0x55f: v732V55f = DIV v72bV55f, v730V55f(0x1)
    0x733S0x55f: v733V55f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x55f: v748V55f = AND v733V55f(0xffffffffffffffffffffffffffffffffffffffff), v732V55f
    0x749S0x55f: v749V55f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x55f: v75eV55f = AND v749V55f(0xffffffffffffffffffffffffffffffffffffffff), v748V55f
    0x75fS0x55f: v75fV55f = CALLER 
    0x760S0x55f: v760V55f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x55f: v775V55f = AND v760V55f(0xffffffffffffffffffffffffffffffffffffffff), v75fV55f
    0x776S0x55f: v776V55f = EQ v775V55f, v75eV55f
    0x77aS0x55f: JUMP v560(0x567)

    Begin block 0x567
    prev=[0x724B0x55f], succ=[0x56e, 0x572]
    =================================
    0x568: v568 = ISZERO v776V55f
    0x569: v569 = ISZERO v568
    0x56a: v56a(0x572) = CONST 
    0x56d: JUMPI v56a(0x572), v569

    Begin block 0x56e
    prev=[0x567], succ=[]
    =================================
    0x56e: v56e(0x0) = CONST 
    0x571: REVERT v56e(0x0), v56e(0x0)

    Begin block 0x572
    prev=[0x567], succ=[0x14e]
    =================================
    0x573: v573(0x0) = CONST 
    0x575: v575(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x58a: v58a(0x0) = AND v575(0xffffffffffffffffffffffffffffffffffffffff), v573(0x0)
    0x58b: v58b(0x0) = CONST 
    0x58f: v58f = SLOAD v58b(0x0)
    0x591: v591(0x100) = CONST 
    0x594: v594(0x1) = EXP v591(0x100), v58b(0x0)
    0x596: v596 = DIV v58f, v594(0x1)
    0x597: v597(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ac: v5ac = AND v597(0xffffffffffffffffffffffffffffffffffffffff), v596
    0x5ad: v5ad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5c2: v5c2 = AND v5ad(0xffffffffffffffffffffffffffffffffffffffff), v5ac
    0x5c3: v5c3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x5e4: v5e4(0x40) = CONST 
    0x5e6: v5e6 = MLOAD v5e4(0x40)
    0x5e7: v5e7(0x40) = CONST 
    0x5e9: v5e9 = MLOAD v5e7(0x40)
    0x5ec: v5ec(0x0) = SUB v5e6, v5e9
    0x5ee: LOG3 v5e9, v5ec(0x0), v5c3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v5c2, v58a(0x0)
    0x5ef: v5ef(0x0) = CONST 
    0x5f2: v5f2(0x0) = CONST 
    0x5f4: v5f4(0x100) = CONST 
    0x5f7: v5f7(0x1) = EXP v5f4(0x100), v5f2(0x0)
    0x5f9: v5f9 = SLOAD v5ef(0x0)
    0x5fb: v5fb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x610: v610(0xffffffffffffffffffffffffffffffffffffffff) = MUL v5fb(0xffffffffffffffffffffffffffffffffffffffff), v5f7(0x1)
    0x611: v611(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v610(0xffffffffffffffffffffffffffffffffffffffff)
    0x612: v612 = AND v611(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v5f9
    0x615: v615(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x62a: v62a(0x0) = AND v615(0xffffffffffffffffffffffffffffffffffffffff), v5ef(0x0)
    0x62b: v62b(0x0) = MUL v62a(0x0), v5f7(0x1)
    0x62c: v62c = OR v62b(0x0), v612
    0x62e: SSTORE v5ef(0x0), v62c
    0x630: JUMP v147(0x14e)

    Begin block 0x14e
    prev=[0x572], succ=[]
    =================================
    0x14f: STOP 

}

function changeProxyAdmin(address,address)() public {
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
    prev=[0x150], succ=[0x16f, 0x173]
    =================================
    0x15e: v15e(0x1bf) = CONST 
    0x161: v161(0x4) = CONST 
    0x164: v164 = CALLDATASIZE 
    0x165: v165 = SUB v164, v161(0x4)
    0x166: v166(0x40) = CONST 
    0x169: v169 = LT v165, v166(0x40)
    0x16a: v16a = ISZERO v169
    0x16b: v16b(0x173) = CONST 
    0x16e: JUMPI v16b(0x173), v16a

    Begin block 0x16f
    prev=[0x15c], succ=[]
    =================================
    0x16f: v16f(0x0) = CONST 
    0x172: REVERT v16f(0x0), v16f(0x0)

    Begin block 0x173
    prev=[0x15c], succ=[0x631]
    =================================
    0x175: v175 = ADD v161(0x4), v165
    0x179: v179 = CALLDATALOAD v161(0x4)
    0x17a: v17a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18f: v18f = AND v17a(0xffffffffffffffffffffffffffffffffffffffff), v179
    0x191: v191(0x20) = CONST 
    0x193: v193(0x24) = ADD v191(0x20), v161(0x4)
    0x199: v199 = CALLDATALOAD v193(0x24)
    0x19a: v19a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1af: v1af = AND v19a(0xffffffffffffffffffffffffffffffffffffffff), v199
    0x1b1: v1b1(0x20) = CONST 
    0x1b3: v1b3(0x44) = ADD v1b1(0x20), v193(0x24)
    0x1bb: v1bb(0x631) = CONST 
    0x1be: JUMP v1bb(0x631)

    Begin block 0x631
    prev=[0x173], succ=[0x724B0x631]
    =================================
    0x632: v632(0x639) = CONST 
    0x635: v635(0x724) = CONST 
    0x638: JUMP v635(0x724)

    Begin block 0x724B0x631
    prev=[0x631], succ=[0x639]
    =================================
    0x725S0x631: v725V631(0x0) = CONST 
    0x728S0x631: v728V631(0x0) = CONST 
    0x72bS0x631: v72bV631 = SLOAD v725V631(0x0)
    0x72dS0x631: v72dV631(0x100) = CONST 
    0x730S0x631: v730V631(0x1) = EXP v72dV631(0x100), v728V631(0x0)
    0x732S0x631: v732V631 = DIV v72bV631, v730V631(0x1)
    0x733S0x631: v733V631(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x631: v748V631 = AND v733V631(0xffffffffffffffffffffffffffffffffffffffff), v732V631
    0x749S0x631: v749V631(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x631: v75eV631 = AND v749V631(0xffffffffffffffffffffffffffffffffffffffff), v748V631
    0x75fS0x631: v75fV631 = CALLER 
    0x760S0x631: v760V631(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x631: v775V631 = AND v760V631(0xffffffffffffffffffffffffffffffffffffffff), v75fV631
    0x776S0x631: v776V631 = EQ v775V631, v75eV631
    0x77aS0x631: JUMP v632(0x639)

    Begin block 0x639
    prev=[0x724B0x631], succ=[0x640, 0x644]
    =================================
    0x63a: v63a = ISZERO v776V631
    0x63b: v63b = ISZERO v63a
    0x63c: v63c(0x644) = CONST 
    0x63f: JUMPI v63c(0x644), v63b

    Begin block 0x640
    prev=[0x639], succ=[]
    =================================
    0x640: v640(0x0) = CONST 
    0x643: REVERT v640(0x0), v640(0x0)

    Begin block 0x644
    prev=[0x639], succ=[0x6db, 0x6df]
    =================================
    0x646: v646(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x65b: v65b = AND v646(0xffffffffffffffffffffffffffffffffffffffff), v18f
    0x65c: v65c(0x8f283970) = CONST 
    0x662: v662(0x40) = CONST 
    0x664: v664 = MLOAD v662(0x40)
    0x666: v666(0xffffffff) = CONST 
    0x66b: v66b(0x8f283970) = AND v666(0xffffffff), v65c(0x8f283970)
    0x66c: v66c(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x68a: v68a(0x8f28397000000000000000000000000000000000000000000000000000000000) = MUL v66c(0x100000000000000000000000000000000000000000000000000000000), v66b(0x8f283970)
    0x68c: MSTORE v664, v68a(0x8f28397000000000000000000000000000000000000000000000000000000000)
    0x68d: v68d(0x4) = CONST 
    0x68f: v68f = ADD v68d(0x4), v664
    0x692: v692(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6a7: v6a7 = AND v692(0xffffffffffffffffffffffffffffffffffffffff), v1af
    0x6a8: v6a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6bd: v6bd = AND v6a8(0xffffffffffffffffffffffffffffffffffffffff), v6a7
    0x6bf: MSTORE v68f, v6bd
    0x6c0: v6c0(0x20) = CONST 
    0x6c2: v6c2 = ADD v6c0(0x20), v68f
    0x6c6: v6c6(0x0) = CONST 
    0x6c8: v6c8(0x40) = CONST 
    0x6ca: v6ca = MLOAD v6c8(0x40)
    0x6cd: v6cd(0x24) = SUB v6c2, v6ca
    0x6cf: v6cf(0x0) = CONST 
    0x6d3: v6d3 = EXTCODESIZE v65b
    0x6d4: v6d4 = ISZERO v6d3
    0x6d6: v6d6 = ISZERO v6d4
    0x6d7: v6d7(0x6df) = CONST 
    0x6da: JUMPI v6d7(0x6df), v6d6

    Begin block 0x6db
    prev=[0x644], succ=[]
    =================================
    0x6db: v6db(0x0) = CONST 
    0x6de: REVERT v6db(0x0), v6db(0x0)

    Begin block 0x6df
    prev=[0x644], succ=[0x6ea, 0x6f3]
    =================================
    0x6e1: v6e1 = GAS 
    0x6e2: v6e2 = CALL v6e1, v65b, v6cf(0x0), v6ca, v6cd(0x24), v6ca, v6c6(0x0)
    0x6e3: v6e3 = ISZERO v6e2
    0x6e5: v6e5 = ISZERO v6e3
    0x6e6: v6e6(0x6f3) = CONST 
    0x6e9: JUMPI v6e6(0x6f3), v6e5

    Begin block 0x6ea
    prev=[0x6df], succ=[]
    =================================
    0x6ea: v6ea = RETURNDATASIZE 
    0x6eb: v6eb(0x0) = CONST 
    0x6ee: RETURNDATACOPY v6eb(0x0), v6eb(0x0), v6ea
    0x6ef: v6ef = RETURNDATASIZE 
    0x6f0: v6f0(0x0) = CONST 
    0x6f2: REVERT v6f0(0x0), v6ef

    Begin block 0x6f3
    prev=[0x6df], succ=[0x1bf]
    =================================
    0x6fa: JUMP v15e(0x1bf)

    Begin block 0x1bf
    prev=[0x6f3], succ=[]
    =================================
    0x1c0: STOP 

}

function owner()() public {
    Begin block 0x1c1
    prev=[], succ=[0x1c9, 0x1cd]
    =================================
    0x1c2: v1c2 = CALLVALUE 
    0x1c4: v1c4 = ISZERO v1c2
    0x1c5: v1c5(0x1cd) = CONST 
    0x1c8: JUMPI v1c5(0x1cd), v1c4

    Begin block 0x1c9
    prev=[0x1c1], succ=[]
    =================================
    0x1c9: v1c9(0x0) = CONST 
    0x1cc: REVERT v1c9(0x0), v1c9(0x0)

    Begin block 0x1cd
    prev=[0x1c1], succ=[0x6fb]
    =================================
    0x1cf: v1cf(0x1d6) = CONST 
    0x1d2: v1d2(0x6fb) = CONST 
    0x1d5: JUMP v1d2(0x6fb)

    Begin block 0x6fb
    prev=[0x1cd], succ=[0x1d6]
    =================================
    0x6fc: v6fc(0x0) = CONST 
    0x6ff: v6ff(0x0) = CONST 
    0x702: v702 = SLOAD v6fc(0x0)
    0x704: v704(0x100) = CONST 
    0x707: v707(0x1) = EXP v704(0x100), v6ff(0x0)
    0x709: v709 = DIV v702, v707(0x1)
    0x70a: v70a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x71f: v71f = AND v70a(0xffffffffffffffffffffffffffffffffffffffff), v709
    0x723: JUMP v1cf(0x1d6)

    Begin block 0x1d6
    prev=[0x6fb], succ=[]
    =================================
    0x1d7: v1d7(0x40) = CONST 
    0x1d9: v1d9 = MLOAD v1d7(0x40)
    0x1dc: v1dc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f1: v1f1 = AND v1dc(0xffffffffffffffffffffffffffffffffffffffff), v71f
    0x1f2: v1f2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x207: v207 = AND v1f2(0xffffffffffffffffffffffffffffffffffffffff), v1f1
    0x209: MSTORE v1d9, v207
    0x20a: v20a(0x20) = CONST 
    0x20c: v20c = ADD v20a(0x20), v1d9
    0x210: v210(0x40) = CONST 
    0x212: v212 = MLOAD v210(0x40)
    0x215: v215(0x20) = SUB v20c, v212
    0x217: RETURN v212, v215(0x20)

}

function isOwner()() public {
    Begin block 0x218
    prev=[], succ=[0x220, 0x224]
    =================================
    0x219: v219 = CALLVALUE 
    0x21b: v21b = ISZERO v219
    0x21c: v21c(0x224) = CONST 
    0x21f: JUMPI v21c(0x224), v21b

    Begin block 0x220
    prev=[0x218], succ=[]
    =================================
    0x220: v220(0x0) = CONST 
    0x223: REVERT v220(0x0), v220(0x0)

    Begin block 0x224
    prev=[0x218], succ=[0x724B0x224]
    =================================
    0x226: v226(0x22d) = CONST 
    0x229: v229(0x724) = CONST 
    0x22c: JUMP v229(0x724)

    Begin block 0x724B0x224
    prev=[0x224], succ=[0x22d]
    =================================
    0x725S0x224: v725V224(0x0) = CONST 
    0x728S0x224: v728V224(0x0) = CONST 
    0x72bS0x224: v72bV224 = SLOAD v725V224(0x0)
    0x72dS0x224: v72dV224(0x100) = CONST 
    0x730S0x224: v730V224(0x1) = EXP v72dV224(0x100), v728V224(0x0)
    0x732S0x224: v732V224 = DIV v72bV224, v730V224(0x1)
    0x733S0x224: v733V224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x224: v748V224 = AND v733V224(0xffffffffffffffffffffffffffffffffffffffff), v732V224
    0x749S0x224: v749V224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x224: v75eV224 = AND v749V224(0xffffffffffffffffffffffffffffffffffffffff), v748V224
    0x75fS0x224: v75fV224 = CALLER 
    0x760S0x224: v760V224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x224: v775V224 = AND v760V224(0xffffffffffffffffffffffffffffffffffffffff), v75fV224
    0x776S0x224: v776V224 = EQ v775V224, v75eV224
    0x77aS0x224: JUMP v226(0x22d)

    Begin block 0x22d
    prev=[0x724B0x224], succ=[]
    =================================
    0x22e: v22e(0x40) = CONST 
    0x230: v230 = MLOAD v22e(0x40)
    0x233: v233 = ISZERO v776V224
    0x234: v234 = ISZERO v233
    0x235: v235 = ISZERO v234
    0x236: v236 = ISZERO v235
    0x238: MSTORE v230, v236
    0x239: v239(0x20) = CONST 
    0x23b: v23b = ADD v239(0x20), v230
    0x23f: v23f(0x40) = CONST 
    0x241: v241 = MLOAD v23f(0x40)
    0x244: v244(0x20) = SUB v23b, v241
    0x246: RETURN v241, v244(0x20)

}

function upgradeAndCall(address,address,bytes)() public {
    Begin block 0x247
    prev=[], succ=[0x259, 0x25d]
    =================================
    0x248: v248(0x340) = CONST 
    0x24b: v24b(0x4) = CONST 
    0x24e: v24e = CALLDATASIZE 
    0x24f: v24f = SUB v24e, v24b(0x4)
    0x250: v250(0x60) = CONST 
    0x253: v253 = LT v24f, v250(0x60)
    0x254: v254 = ISZERO v253
    0x255: v255(0x25d) = CONST 
    0x258: JUMPI v255(0x25d), v254

    Begin block 0x259
    prev=[0x247], succ=[]
    =================================
    0x259: v259(0x0) = CONST 
    0x25c: REVERT v259(0x0), v259(0x0)

    Begin block 0x25d
    prev=[0x247], succ=[0x2b6, 0x2ba]
    =================================
    0x25f: v25f = ADD v24b(0x4), v24f
    0x263: v263 = CALLDATALOAD v24b(0x4)
    0x264: v264(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x279: v279 = AND v264(0xffffffffffffffffffffffffffffffffffffffff), v263
    0x27b: v27b(0x20) = CONST 
    0x27d: v27d(0x24) = ADD v27b(0x20), v24b(0x4)
    0x283: v283 = CALLDATALOAD v27d(0x24)
    0x284: v284(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x299: v299 = AND v284(0xffffffffffffffffffffffffffffffffffffffff), v283
    0x29b: v29b(0x20) = CONST 
    0x29d: v29d(0x44) = ADD v29b(0x20), v27d(0x24)
    0x2a3: v2a3 = CALLDATALOAD v29d(0x44)
    0x2a5: v2a5(0x20) = CONST 
    0x2a7: v2a7(0x64) = ADD v2a5(0x20), v29d(0x44)
    0x2a9: v2a9(0x100000000) = CONST 
    0x2b0: v2b0 = GT v2a3, v2a9(0x100000000)
    0x2b1: v2b1 = ISZERO v2b0
    0x2b2: v2b2(0x2ba) = CONST 
    0x2b5: JUMPI v2b2(0x2ba), v2b1

    Begin block 0x2b6
    prev=[0x25d], succ=[]
    =================================
    0x2b6: v2b6(0x0) = CONST 
    0x2b9: REVERT v2b6(0x0), v2b6(0x0)

    Begin block 0x2ba
    prev=[0x25d], succ=[0x2c8, 0x2cc]
    =================================
    0x2bc: v2bc = ADD v24b(0x4), v2a3
    0x2be: v2be(0x20) = CONST 
    0x2c1: v2c1 = ADD v2bc, v2be(0x20)
    0x2c2: v2c2 = GT v2c1, v25f
    0x2c3: v2c3 = ISZERO v2c2
    0x2c4: v2c4(0x2cc) = CONST 
    0x2c7: JUMPI v2c4(0x2cc), v2c3

    Begin block 0x2c8
    prev=[0x2ba], succ=[]
    =================================
    0x2c8: v2c8(0x0) = CONST 
    0x2cb: REVERT v2c8(0x0), v2c8(0x0)

    Begin block 0x2cc
    prev=[0x2ba], succ=[0x2ea, 0x2ee]
    =================================
    0x2ce: v2ce = CALLDATALOAD v2bc
    0x2d0: v2d0(0x20) = CONST 
    0x2d2: v2d2 = ADD v2d0(0x20), v2bc
    0x2d5: v2d5(0x1) = CONST 
    0x2d8: v2d8 = MUL v2ce, v2d5(0x1)
    0x2da: v2da = ADD v2d2, v2d8
    0x2db: v2db = GT v2da, v25f
    0x2dc: v2dc(0x100000000) = CONST 
    0x2e3: v2e3 = GT v2ce, v2dc(0x100000000)
    0x2e4: v2e4 = OR v2e3, v2db
    0x2e5: v2e5 = ISZERO v2e4
    0x2e6: v2e6(0x2ee) = CONST 
    0x2e9: JUMPI v2e6(0x2ee), v2e5

    Begin block 0x2ea
    prev=[0x2cc], succ=[]
    =================================
    0x2ea: v2ea(0x0) = CONST 
    0x2ed: REVERT v2ea(0x0), v2ea(0x0)

    Begin block 0x2ee
    prev=[0x2cc], succ=[0x77b]
    =================================
    0x2f3: v2f3(0x1f) = CONST 
    0x2f5: v2f5 = ADD v2f3(0x1f), v2ce
    0x2f6: v2f6(0x20) = CONST 
    0x2fa: v2fa = DIV v2f5, v2f6(0x20)
    0x2fb: v2fb = MUL v2fa, v2f6(0x20)
    0x2fc: v2fc(0x20) = CONST 
    0x2fe: v2fe = ADD v2fc(0x20), v2fb
    0x2ff: v2ff(0x40) = CONST 
    0x301: v301 = MLOAD v2ff(0x40)
    0x304: v304 = ADD v301, v2fe
    0x305: v305(0x40) = CONST 
    0x307: MSTORE v305(0x40), v304
    0x30f: MSTORE v301, v2ce
    0x310: v310(0x20) = CONST 
    0x312: v312 = ADD v310(0x20), v301
    0x318: CALLDATACOPY v312, v2d2, v2ce
    0x319: v319(0x0) = CONST 
    0x31d: v31d = ADD v312, v2ce
    0x31e: MSTORE v31d, v319(0x0)
    0x31f: v31f(0x1f) = CONST 
    0x321: v321(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v31f(0x1f)
    0x322: v322(0x1f) = CONST 
    0x325: v325 = ADD v2ce, v322(0x1f)
    0x326: v326 = AND v325, v321(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x32b: v32b = ADD v312, v326
    0x33c: v33c(0x77b) = CONST 
    0x33f: JUMP v33c(0x77b)

    Begin block 0x77b
    prev=[0x2ee], succ=[0x724B0x77b]
    =================================
    0x77c: v77c(0x783) = CONST 
    0x77f: v77f(0x724) = CONST 
    0x782: JUMP v77f(0x724)

    Begin block 0x724B0x77b
    prev=[0x77b], succ=[0x783]
    =================================
    0x725S0x77b: v725V77b(0x0) = CONST 
    0x728S0x77b: v728V77b(0x0) = CONST 
    0x72bS0x77b: v72bV77b = SLOAD v725V77b(0x0)
    0x72dS0x77b: v72dV77b(0x100) = CONST 
    0x730S0x77b: v730V77b(0x1) = EXP v72dV77b(0x100), v728V77b(0x0)
    0x732S0x77b: v732V77b = DIV v72bV77b, v730V77b(0x1)
    0x733S0x77b: v733V77b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x77b: v748V77b = AND v733V77b(0xffffffffffffffffffffffffffffffffffffffff), v732V77b
    0x749S0x77b: v749V77b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x77b: v75eV77b = AND v749V77b(0xffffffffffffffffffffffffffffffffffffffff), v748V77b
    0x75fS0x77b: v75fV77b = CALLER 
    0x760S0x77b: v760V77b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x77b: v775V77b = AND v760V77b(0xffffffffffffffffffffffffffffffffffffffff), v75fV77b
    0x776S0x77b: v776V77b = EQ v775V77b, v75eV77b
    0x77aS0x77b: JUMP v77c(0x783)

    Begin block 0x783
    prev=[0x724B0x77b], succ=[0x78a, 0x78e]
    =================================
    0x784: v784 = ISZERO v776V77b
    0x785: v785 = ISZERO v784
    0x786: v786(0x78e) = CONST 
    0x789: JUMPI v786(0x78e), v785

    Begin block 0x78a
    prev=[0x783], succ=[]
    =================================
    0x78a: v78a(0x0) = CONST 
    0x78d: REVERT v78a(0x0), v78a(0x0)

    Begin block 0x78e
    prev=[0x783], succ=[0x82f]
    =================================
    0x790: v790(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7a5: v7a5 = AND v790(0xffffffffffffffffffffffffffffffffffffffff), v279
    0x7a6: v7a6(0x4f1ef286) = CONST 
    0x7ab: v7ab = CALLVALUE 
    0x7ae: v7ae(0x40) = CONST 
    0x7b0: v7b0 = MLOAD v7ae(0x40)
    0x7b2: v7b2(0xffffffff) = CONST 
    0x7b7: v7b7(0x4f1ef286) = AND v7b2(0xffffffff), v7a6(0x4f1ef286)
    0x7b8: v7b8(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x7d6: v7d6(0x4f1ef28600000000000000000000000000000000000000000000000000000000) = MUL v7b8(0x100000000000000000000000000000000000000000000000000000000), v7b7(0x4f1ef286)
    0x7d8: MSTORE v7b0, v7d6(0x4f1ef28600000000000000000000000000000000000000000000000000000000)
    0x7d9: v7d9(0x4) = CONST 
    0x7db: v7db = ADD v7d9(0x4), v7b0
    0x7de: v7de(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7f3: v7f3 = AND v7de(0xffffffffffffffffffffffffffffffffffffffff), v299
    0x7f4: v7f4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x809: v809 = AND v7f4(0xffffffffffffffffffffffffffffffffffffffff), v7f3
    0x80b: MSTORE v7db, v809
    0x80c: v80c(0x20) = CONST 
    0x80e: v80e = ADD v80c(0x20), v7db
    0x810: v810(0x20) = CONST 
    0x812: v812 = ADD v810(0x20), v80e
    0x815: v815(0x40) = SUB v812, v7db
    0x817: MSTORE v80e, v815(0x40)
    0x81b: v81b = MLOAD v301
    0x81d: MSTORE v812, v81b
    0x81e: v81e(0x20) = CONST 
    0x820: v820 = ADD v81e(0x20), v812
    0x824: v824 = MLOAD v301
    0x826: v826(0x20) = CONST 
    0x828: v828 = ADD v826(0x20), v301
    0x82d: v82d(0x0) = CONST 

    Begin block 0x82f
    prev=[0x78e, 0x838], succ=[0x84a, 0x838]
    =================================
    0x82f_0x0: v82f_0 = PHI v82d(0x0), v843
    0x832: v832 = LT v82f_0, v824
    0x833: v833 = ISZERO v832
    0x834: v834(0x84a) = CONST 
    0x837: JUMPI v834(0x84a), v833

    Begin block 0x84a
    prev=[0x82f], succ=[0x877, 0x85e]
    =================================
    0x853: v853 = ADD v824, v820
    0x855: v855(0x1f) = CONST 
    0x857: v857 = AND v855(0x1f), v824
    0x859: v859 = ISZERO v857
    0x85a: v85a(0x877) = CONST 
    0x85d: JUMPI v85a(0x877), v859

    Begin block 0x877
    prev=[0x84a, 0x85e], succ=[0x892, 0x896]
    =================================
    0x877_0x1: v877_1 = PHI v853, v874
    0x87e: v87e(0x0) = CONST 
    0x880: v880(0x40) = CONST 
    0x882: v882 = MLOAD v880(0x40)
    0x885: v885 = SUB v877_1, v882
    0x88a: v88a = EXTCODESIZE v7a5
    0x88b: v88b = ISZERO v88a
    0x88d: v88d = ISZERO v88b
    0x88e: v88e(0x896) = CONST 
    0x891: JUMPI v88e(0x896), v88d

    Begin block 0x892
    prev=[0x877], succ=[]
    =================================
    0x892: v892(0x0) = CONST 
    0x895: REVERT v892(0x0), v892(0x0)

    Begin block 0x896
    prev=[0x877], succ=[0x8a1, 0x8aa]
    =================================
    0x898: v898 = GAS 
    0x899: v899 = CALL v898, v7a5, v7ab, v882, v885, v882, v87e(0x0)
    0x89a: v89a = ISZERO v899
    0x89c: v89c = ISZERO v89a
    0x89d: v89d(0x8aa) = CONST 
    0x8a0: JUMPI v89d(0x8aa), v89c

    Begin block 0x8a1
    prev=[0x896], succ=[]
    =================================
    0x8a1: v8a1 = RETURNDATASIZE 
    0x8a2: v8a2(0x0) = CONST 
    0x8a5: RETURNDATACOPY v8a2(0x0), v8a2(0x0), v8a1
    0x8a6: v8a6 = RETURNDATASIZE 
    0x8a7: v8a7(0x0) = CONST 
    0x8a9: REVERT v8a7(0x0), v8a6

    Begin block 0x8aa
    prev=[0x896], succ=[0x340]
    =================================
    0x8b3: JUMP v248(0x340)

    Begin block 0x340
    prev=[0x8aa], succ=[]
    =================================
    0x341: STOP 

    Begin block 0x85e
    prev=[0x84a], succ=[0x877]
    =================================
    0x860: v860 = SUB v853, v857
    0x862: v862 = MLOAD v860
    0x863: v863(0x1) = CONST 
    0x866: v866(0x20) = CONST 
    0x868: v868 = SUB v866(0x20), v857
    0x869: v869(0x100) = CONST 
    0x86c: v86c = EXP v869(0x100), v868
    0x86d: v86d = SUB v86c, v863(0x1)
    0x86e: v86e = NOT v86d
    0x86f: v86f = AND v86e, v862
    0x871: MSTORE v860, v86f
    0x872: v872(0x20) = CONST 
    0x874: v874 = ADD v872(0x20), v860

    Begin block 0x838
    prev=[0x82f], succ=[0x82f]
    =================================
    0x838_0x0: v838_0 = PHI v82d(0x0), v843
    0x83a: v83a = ADD v828, v838_0
    0x83b: v83b = MLOAD v83a
    0x83e: v83e = ADD v820, v838_0
    0x83f: MSTORE v83e, v83b
    0x840: v840(0x20) = CONST 
    0x843: v843 = ADD v838_0, v840(0x20)
    0x846: v846(0x82f) = CONST 
    0x849: JUMP v846(0x82f)

}

function upgrade(address,address)() public {
    Begin block 0x342
    prev=[], succ=[0x34a, 0x34e]
    =================================
    0x343: v343 = CALLVALUE 
    0x345: v345 = ISZERO v343
    0x346: v346(0x34e) = CONST 
    0x349: JUMPI v346(0x34e), v345

    Begin block 0x34a
    prev=[0x342], succ=[]
    =================================
    0x34a: v34a(0x0) = CONST 
    0x34d: REVERT v34a(0x0), v34a(0x0)

    Begin block 0x34e
    prev=[0x342], succ=[0x361, 0x365]
    =================================
    0x350: v350(0x3b1) = CONST 
    0x353: v353(0x4) = CONST 
    0x356: v356 = CALLDATASIZE 
    0x357: v357 = SUB v356, v353(0x4)
    0x358: v358(0x40) = CONST 
    0x35b: v35b = LT v357, v358(0x40)
    0x35c: v35c = ISZERO v35b
    0x35d: v35d(0x365) = CONST 
    0x360: JUMPI v35d(0x365), v35c

    Begin block 0x361
    prev=[0x34e], succ=[]
    =================================
    0x361: v361(0x0) = CONST 
    0x364: REVERT v361(0x0), v361(0x0)

    Begin block 0x365
    prev=[0x34e], succ=[0x8b4]
    =================================
    0x367: v367 = ADD v353(0x4), v357
    0x36b: v36b = CALLDATALOAD v353(0x4)
    0x36c: v36c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x381: v381 = AND v36c(0xffffffffffffffffffffffffffffffffffffffff), v36b
    0x383: v383(0x20) = CONST 
    0x385: v385(0x24) = ADD v383(0x20), v353(0x4)
    0x38b: v38b = CALLDATALOAD v385(0x24)
    0x38c: v38c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a1: v3a1 = AND v38c(0xffffffffffffffffffffffffffffffffffffffff), v38b
    0x3a3: v3a3(0x20) = CONST 
    0x3a5: v3a5(0x44) = ADD v3a3(0x20), v385(0x24)
    0x3ad: v3ad(0x8b4) = CONST 
    0x3b0: JUMP v3ad(0x8b4)

    Begin block 0x8b4
    prev=[0x365], succ=[0x724B0x8b4]
    =================================
    0x8b5: v8b5(0x8bc) = CONST 
    0x8b8: v8b8(0x724) = CONST 
    0x8bb: JUMP v8b8(0x724)

    Begin block 0x724B0x8b4
    prev=[0x8b4], succ=[0x8bc]
    =================================
    0x725S0x8b4: v725V8b4(0x0) = CONST 
    0x728S0x8b4: v728V8b4(0x0) = CONST 
    0x72bS0x8b4: v72bV8b4 = SLOAD v725V8b4(0x0)
    0x72dS0x8b4: v72dV8b4(0x100) = CONST 
    0x730S0x8b4: v730V8b4(0x1) = EXP v72dV8b4(0x100), v728V8b4(0x0)
    0x732S0x8b4: v732V8b4 = DIV v72bV8b4, v730V8b4(0x1)
    0x733S0x8b4: v733V8b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x8b4: v748V8b4 = AND v733V8b4(0xffffffffffffffffffffffffffffffffffffffff), v732V8b4
    0x749S0x8b4: v749V8b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x8b4: v75eV8b4 = AND v749V8b4(0xffffffffffffffffffffffffffffffffffffffff), v748V8b4
    0x75fS0x8b4: v75fV8b4 = CALLER 
    0x760S0x8b4: v760V8b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x8b4: v775V8b4 = AND v760V8b4(0xffffffffffffffffffffffffffffffffffffffff), v75fV8b4
    0x776S0x8b4: v776V8b4 = EQ v775V8b4, v75eV8b4
    0x77aS0x8b4: JUMP v8b5(0x8bc)

    Begin block 0x8bc
    prev=[0x724B0x8b4], succ=[0x8c3, 0x8c7]
    =================================
    0x8bd: v8bd = ISZERO v776V8b4
    0x8be: v8be = ISZERO v8bd
    0x8bf: v8bf(0x8c7) = CONST 
    0x8c2: JUMPI v8bf(0x8c7), v8be

    Begin block 0x8c3
    prev=[0x8bc], succ=[]
    =================================
    0x8c3: v8c3(0x0) = CONST 
    0x8c6: REVERT v8c3(0x0), v8c3(0x0)

    Begin block 0x8c7
    prev=[0x8bc], succ=[0x95e, 0x962]
    =================================
    0x8c9: v8c9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8de: v8de = AND v8c9(0xffffffffffffffffffffffffffffffffffffffff), v381
    0x8df: v8df(0x3659cfe6) = CONST 
    0x8e5: v8e5(0x40) = CONST 
    0x8e7: v8e7 = MLOAD v8e5(0x40)
    0x8e9: v8e9(0xffffffff) = CONST 
    0x8ee: v8ee(0x3659cfe6) = AND v8e9(0xffffffff), v8df(0x3659cfe6)
    0x8ef: v8ef(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x90d: v90d(0x3659cfe600000000000000000000000000000000000000000000000000000000) = MUL v8ef(0x100000000000000000000000000000000000000000000000000000000), v8ee(0x3659cfe6)
    0x90f: MSTORE v8e7, v90d(0x3659cfe600000000000000000000000000000000000000000000000000000000)
    0x910: v910(0x4) = CONST 
    0x912: v912 = ADD v910(0x4), v8e7
    0x915: v915(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x92a: v92a = AND v915(0xffffffffffffffffffffffffffffffffffffffff), v3a1
    0x92b: v92b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x940: v940 = AND v92b(0xffffffffffffffffffffffffffffffffffffffff), v92a
    0x942: MSTORE v912, v940
    0x943: v943(0x20) = CONST 
    0x945: v945 = ADD v943(0x20), v912
    0x949: v949(0x0) = CONST 
    0x94b: v94b(0x40) = CONST 
    0x94d: v94d = MLOAD v94b(0x40)
    0x950: v950(0x24) = SUB v945, v94d
    0x952: v952(0x0) = CONST 
    0x956: v956 = EXTCODESIZE v8de
    0x957: v957 = ISZERO v956
    0x959: v959 = ISZERO v957
    0x95a: v95a(0x962) = CONST 
    0x95d: JUMPI v95a(0x962), v959

    Begin block 0x95e
    prev=[0x8c7], succ=[]
    =================================
    0x95e: v95e(0x0) = CONST 
    0x961: REVERT v95e(0x0), v95e(0x0)

    Begin block 0x962
    prev=[0x8c7], succ=[0x96d, 0x976]
    =================================
    0x964: v964 = GAS 
    0x965: v965 = CALL v964, v8de, v952(0x0), v94d, v950(0x24), v94d, v949(0x0)
    0x966: v966 = ISZERO v965
    0x968: v968 = ISZERO v966
    0x969: v969(0x976) = CONST 
    0x96c: JUMPI v969(0x976), v968

    Begin block 0x96d
    prev=[0x962], succ=[]
    =================================
    0x96d: v96d = RETURNDATASIZE 
    0x96e: v96e(0x0) = CONST 
    0x971: RETURNDATACOPY v96e(0x0), v96e(0x0), v96d
    0x972: v972 = RETURNDATASIZE 
    0x973: v973(0x0) = CONST 
    0x975: REVERT v973(0x0), v972

    Begin block 0x976
    prev=[0x962], succ=[0x3b1]
    =================================
    0x97d: JUMP v350(0x3b1)

    Begin block 0x3b1
    prev=[0x976], succ=[]
    =================================
    0x3b2: STOP 

}

function transferOwnership(address)() public {
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
    prev=[0x3b3], succ=[0x3d2, 0x3d6]
    =================================
    0x3c1: v3c1(0x402) = CONST 
    0x3c4: v3c4(0x4) = CONST 
    0x3c7: v3c7 = CALLDATASIZE 
    0x3c8: v3c8 = SUB v3c7, v3c4(0x4)
    0x3c9: v3c9(0x20) = CONST 
    0x3cc: v3cc = LT v3c8, v3c9(0x20)
    0x3cd: v3cd = ISZERO v3cc
    0x3ce: v3ce(0x3d6) = CONST 
    0x3d1: JUMPI v3ce(0x3d6), v3cd

    Begin block 0x3d2
    prev=[0x3bf], succ=[]
    =================================
    0x3d2: v3d2(0x0) = CONST 
    0x3d5: REVERT v3d2(0x0), v3d2(0x0)

    Begin block 0x3d6
    prev=[0x3bf], succ=[0x97e]
    =================================
    0x3d8: v3d8 = ADD v3c4(0x4), v3c8
    0x3dc: v3dc = CALLDATALOAD v3c4(0x4)
    0x3dd: v3dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3f2: v3f2 = AND v3dd(0xffffffffffffffffffffffffffffffffffffffff), v3dc
    0x3f4: v3f4(0x20) = CONST 
    0x3f6: v3f6(0x24) = ADD v3f4(0x20), v3c4(0x4)
    0x3fe: v3fe(0x97e) = CONST 
    0x401: JUMP v3fe(0x97e)

    Begin block 0x97e
    prev=[0x3d6], succ=[0x724B0x97e]
    =================================
    0x97f: v97f(0x986) = CONST 
    0x982: v982(0x724) = CONST 
    0x985: JUMP v982(0x724)

    Begin block 0x724B0x97e
    prev=[0x97e], succ=[0x986]
    =================================
    0x725S0x97e: v725V97e(0x0) = CONST 
    0x728S0x97e: v728V97e(0x0) = CONST 
    0x72bS0x97e: v72bV97e = SLOAD v725V97e(0x0)
    0x72dS0x97e: v72dV97e(0x100) = CONST 
    0x730S0x97e: v730V97e(0x1) = EXP v72dV97e(0x100), v728V97e(0x0)
    0x732S0x97e: v732V97e = DIV v72bV97e, v730V97e(0x1)
    0x733S0x97e: v733V97e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x748S0x97e: v748V97e = AND v733V97e(0xffffffffffffffffffffffffffffffffffffffff), v732V97e
    0x749S0x97e: v749V97e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x75eS0x97e: v75eV97e = AND v749V97e(0xffffffffffffffffffffffffffffffffffffffff), v748V97e
    0x75fS0x97e: v75fV97e = CALLER 
    0x760S0x97e: v760V97e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x775S0x97e: v775V97e = AND v760V97e(0xffffffffffffffffffffffffffffffffffffffff), v75fV97e
    0x776S0x97e: v776V97e = EQ v775V97e, v75eV97e
    0x77aS0x97e: JUMP v97f(0x986)

    Begin block 0x986
    prev=[0x724B0x97e], succ=[0x98d, 0x991]
    =================================
    0x987: v987 = ISZERO v776V97e
    0x988: v988 = ISZERO v987
    0x989: v989(0x991) = CONST 
    0x98c: JUMPI v989(0x991), v988

    Begin block 0x98d
    prev=[0x986], succ=[]
    =================================
    0x98d: v98d(0x0) = CONST 
    0x990: REVERT v98d(0x0), v98d(0x0)

    Begin block 0x991
    prev=[0x986], succ=[0xa67]
    =================================
    0x992: v992(0x99a) = CONST 
    0x996: v996(0xa67) = CONST 
    0x999: JUMP v996(0xa67)

    Begin block 0xa67
    prev=[0x991], succ=[0xa9f, 0xaa3]
    =================================
    0xa68: va68(0x0) = CONST 
    0xa6a: va6a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa7f: va7f(0x0) = AND va6a(0xffffffffffffffffffffffffffffffffffffffff), va68(0x0)
    0xa81: va81(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa96: va96 = AND va81(0xffffffffffffffffffffffffffffffffffffffff), v3f2
    0xa97: va97 = EQ va96, va7f(0x0)
    0xa98: va98 = ISZERO va97
    0xa99: va99 = ISZERO va98
    0xa9a: va9a = ISZERO va99
    0xa9b: va9b(0xaa3) = CONST 
    0xa9e: JUMPI va9b(0xaa3), va9a

    Begin block 0xa9f
    prev=[0xa67], succ=[]
    =================================
    0xa9f: va9f(0x0) = CONST 
    0xaa2: REVERT va9f(0x0), va9f(0x0)

    Begin block 0xaa3
    prev=[0xa67], succ=[0x99a]
    =================================
    0xaa5: vaa5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaba: vaba = AND vaa5(0xffffffffffffffffffffffffffffffffffffffff), v3f2
    0xabb: vabb(0x0) = CONST 
    0xabf: vabf = SLOAD vabb(0x0)
    0xac1: vac1(0x100) = CONST 
    0xac4: vac4(0x1) = EXP vac1(0x100), vabb(0x0)
    0xac6: vac6 = DIV vabf, vac4(0x1)
    0xac7: vac7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xadc: vadc = AND vac7(0xffffffffffffffffffffffffffffffffffffffff), vac6
    0xadd: vadd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf2: vaf2 = AND vadd(0xffffffffffffffffffffffffffffffffffffffff), vadc
    0xaf3: vaf3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0xb14: vb14(0x40) = CONST 
    0xb16: vb16 = MLOAD vb14(0x40)
    0xb17: vb17(0x40) = CONST 
    0xb19: vb19 = MLOAD vb17(0x40)
    0xb1c: vb1c(0x0) = SUB vb16, vb19
    0xb1e: LOG3 vb19, vb1c(0x0), vaf3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), vaf2, vaba
    0xb20: vb20(0x0) = CONST 
    0xb23: vb23(0x100) = CONST 
    0xb26: vb26(0x1) = EXP vb23(0x100), vb20(0x0)
    0xb28: vb28 = SLOAD vb20(0x0)
    0xb2a: vb2a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb3f: vb3f(0xffffffffffffffffffffffffffffffffffffffff) = MUL vb2a(0xffffffffffffffffffffffffffffffffffffffff), vb26(0x1)
    0xb40: vb40(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vb3f(0xffffffffffffffffffffffffffffffffffffffff)
    0xb41: vb41 = AND vb40(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vb28
    0xb44: vb44(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb59: vb59 = AND vb44(0xffffffffffffffffffffffffffffffffffffffff), v3f2
    0xb5a: vb5a = MUL vb59, vb26(0x1)
    0xb5b: vb5b = OR vb5a, vb41
    0xb5d: SSTORE vb20(0x0), vb5b
    0xb60: JUMP v992(0x99a)

    Begin block 0x99a
    prev=[0xaa3], succ=[0x402]
    =================================
    0x99c: JUMP v3c1(0x402)

    Begin block 0x402
    prev=[0x99a], succ=[]
    =================================
    0x403: STOP 

}

function getProxyAdmin(address)() public {
    Begin block 0x404
    prev=[], succ=[0x40c, 0x410]
    =================================
    0x405: v405 = CALLVALUE 
    0x407: v407 = ISZERO v405
    0x408: v408(0x410) = CONST 
    0x40b: JUMPI v408(0x410), v407

    Begin block 0x40c
    prev=[0x404], succ=[]
    =================================
    0x40c: v40c(0x0) = CONST 
    0x40f: REVERT v40c(0x0), v40c(0x0)

    Begin block 0x410
    prev=[0x404], succ=[0x423, 0x427]
    =================================
    0x412: v412(0x453) = CONST 
    0x415: v415(0x4) = CONST 
    0x418: v418 = CALLDATASIZE 
    0x419: v419 = SUB v418, v415(0x4)
    0x41a: v41a(0x20) = CONST 
    0x41d: v41d = LT v419, v41a(0x20)
    0x41e: v41e = ISZERO v41d
    0x41f: v41f(0x427) = CONST 
    0x422: JUMPI v41f(0x427), v41e

    Begin block 0x423
    prev=[0x410], succ=[]
    =================================
    0x423: v423(0x0) = CONST 
    0x426: REVERT v423(0x0), v423(0x0)

    Begin block 0x427
    prev=[0x410], succ=[0x99d]
    =================================
    0x429: v429 = ADD v415(0x4), v419
    0x42d: v42d = CALLDATALOAD v415(0x4)
    0x42e: v42e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x443: v443 = AND v42e(0xffffffffffffffffffffffffffffffffffffffff), v42d
    0x445: v445(0x20) = CONST 
    0x447: v447(0x24) = ADD v445(0x20), v415(0x4)
    0x44f: v44f(0x99d) = CONST 
    0x452: JUMP v44f(0x99d)

    Begin block 0x99d
    prev=[0x427], succ=[0xa01, 0xa22]
    =================================
    0x99e: v99e(0x0) = CONST 
    0x9a1: v9a1(0x60) = CONST 
    0x9a4: v9a4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x9b9: v9b9 = AND v9a4(0xffffffffffffffffffffffffffffffffffffffff), v443
    0x9ba: v9ba(0x40) = CONST 
    0x9bc: v9bc = MLOAD v9ba(0x40)
    0x9bf: v9bf(0xf851a44000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9e1: MSTORE v9bc, v9bf(0xf851a44000000000000000000000000000000000000000000000000000000000)
    0x9e3: v9e3(0x4) = CONST 
    0x9e5: v9e5 = ADD v9e3(0x4), v9bc
    0x9e8: v9e8(0x0) = CONST 
    0x9ea: v9ea(0x40) = CONST 
    0x9ec: v9ec = MLOAD v9ea(0x40)
    0x9ef: v9ef(0x4) = SUB v9e5, v9ec
    0x9f2: v9f2 = GAS 
    0x9f3: v9f3 = STATICCALL v9f2, v9b9, v9ec, v9ef(0x4), v9ec, v9e8(0x0)
    0x9f7: v9f7 = RETURNDATASIZE 
    0x9f9: v9f9(0x0) = CONST 
    0x9fc: v9fc = EQ v9f7, v9f9(0x0)
    0x9fd: v9fd(0xa22) = CONST 
    0xa00: JUMPI v9fd(0xa22), v9fc

    Begin block 0xa01
    prev=[0x99d], succ=[0xa27]
    =================================
    0xa01: va01(0x40) = CONST 
    0xa03: va03 = MLOAD va01(0x40)
    0xa06: va06(0x1f) = CONST 
    0xa08: va08(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT va06(0x1f)
    0xa09: va09(0x3f) = CONST 
    0xa0b: va0b = RETURNDATASIZE 
    0xa0c: va0c = ADD va0b, va09(0x3f)
    0xa0d: va0d = AND va0c, va08(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xa0f: va0f = ADD va03, va0d
    0xa10: va10(0x40) = CONST 
    0xa12: MSTORE va10(0x40), va0f
    0xa13: va13 = RETURNDATASIZE 
    0xa15: MSTORE va03, va13
    0xa16: va16 = RETURNDATASIZE 
    0xa17: va17(0x0) = CONST 
    0xa19: va19(0x20) = CONST 
    0xa1c: va1c = ADD va03, va19(0x20)
    0xa1d: RETURNDATACOPY va1c, va17(0x0), va16
    0xa1e: va1e(0xa27) = CONST 
    0xa21: JUMP va1e(0xa27)

    Begin block 0xa27
    prev=[0xa01, 0xa22], succ=[0xa34, 0xa38]
    =================================
    0xa2e: va2e = ISZERO v9f3
    0xa2f: va2f = ISZERO va2e
    0xa30: va30(0xa38) = CONST 
    0xa33: JUMPI va30(0xa38), va2f

    Begin block 0xa34
    prev=[0xa27], succ=[]
    =================================
    0xa34: va34(0x0) = CONST 
    0xa37: REVERT va34(0x0), va34(0x0)

    Begin block 0xa38
    prev=[0xa27], succ=[0xa49, 0xa4d]
    =================================
    0xa38_0x0: va38_0 = PHI va03, va23(0x60)
    0xa3b: va3b(0x20) = CONST 
    0xa3d: va3d = ADD va3b(0x20), va38_0
    0xa3f: va3f = MLOAD va38_0
    0xa40: va40(0x20) = CONST 
    0xa43: va43 = LT va3f, va40(0x20)
    0xa44: va44 = ISZERO va43
    0xa45: va45(0xa4d) = CONST 
    0xa48: JUMPI va45(0xa4d), va44

    Begin block 0xa49
    prev=[0xa38], succ=[]
    =================================
    0xa49: va49(0x0) = CONST 
    0xa4c: REVERT va49(0x0), va49(0x0)

    Begin block 0xa4d
    prev=[0xa38], succ=[0x453]
    =================================
    0xa4f: va4f = ADD va3d, va3f
    0xa53: va53 = MLOAD va3d
    0xa55: va55(0x20) = CONST 
    0xa57: va57 = ADD va55(0x20), va3d
    0xa66: JUMP v412(0x453)

    Begin block 0x453
    prev=[0xa4d], succ=[]
    =================================
    0x454: v454(0x40) = CONST 
    0x456: v456 = MLOAD v454(0x40)
    0x459: v459(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x46e: v46e = AND v459(0xffffffffffffffffffffffffffffffffffffffff), va53
    0x46f: v46f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x484: v484 = AND v46f(0xffffffffffffffffffffffffffffffffffffffff), v46e
    0x486: MSTORE v456, v484
    0x487: v487(0x20) = CONST 
    0x489: v489 = ADD v487(0x20), v456
    0x48d: v48d(0x40) = CONST 
    0x48f: v48f = MLOAD v48d(0x40)
    0x492: v492(0x20) = SUB v489, v48f
    0x494: RETURN v48f, v492(0x20)

    Begin block 0xa22
    prev=[0x99d], succ=[0xa27]
    =================================
    0xa23: va23(0x60) = CONST 

}

function getProxyImplementation(address)() public {
    Begin block 0xa8
    prev=[], succ=[0xb0, 0xb4]
    =================================
    0xa9: va9 = CALLVALUE 
    0xab: vab = ISZERO va9
    0xac: vac(0xb4) = CONST 
    0xaf: JUMPI vac(0xb4), vab

    Begin block 0xb0
    prev=[0xa8], succ=[]
    =================================
    0xb0: vb0(0x0) = CONST 
    0xb3: REVERT vb0(0x0), vb0(0x0)

    Begin block 0xb4
    prev=[0xa8], succ=[0xc7, 0xcb]
    =================================
    0xb6: vb6(0xf7) = CONST 
    0xb9: vb9(0x4) = CONST 
    0xbc: vbc = CALLDATASIZE 
    0xbd: vbd = SUB vbc, vb9(0x4)
    0xbe: vbe(0x20) = CONST 
    0xc1: vc1 = LT vbd, vbe(0x20)
    0xc2: vc2 = ISZERO vc1
    0xc3: vc3(0xcb) = CONST 
    0xc6: JUMPI vc3(0xcb), vc2

    Begin block 0xc7
    prev=[0xb4], succ=[]
    =================================
    0xc7: vc7(0x0) = CONST 
    0xca: REVERT vc7(0x0), vc7(0x0)

    Begin block 0xcb
    prev=[0xb4], succ=[0x495]
    =================================
    0xcd: vcd = ADD vb9(0x4), vbd
    0xd1: vd1 = CALLDATALOAD vb9(0x4)
    0xd2: vd2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe7: ve7 = AND vd2(0xffffffffffffffffffffffffffffffffffffffff), vd1
    0xe9: ve9(0x20) = CONST 
    0xeb: veb(0x24) = ADD ve9(0x20), vb9(0x4)
    0xf3: vf3(0x495) = CONST 
    0xf6: JUMP vf3(0x495)

    Begin block 0x495
    prev=[0xcb], succ=[0x4f9, 0x51a]
    =================================
    0x496: v496(0x0) = CONST 
    0x499: v499(0x60) = CONST 
    0x49c: v49c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4b1: v4b1 = AND v49c(0xffffffffffffffffffffffffffffffffffffffff), ve7
    0x4b2: v4b2(0x40) = CONST 
    0x4b4: v4b4 = MLOAD v4b2(0x40)
    0x4b7: v4b7(0x5c60da1b00000000000000000000000000000000000000000000000000000000) = CONST 
    0x4d9: MSTORE v4b4, v4b7(0x5c60da1b00000000000000000000000000000000000000000000000000000000)
    0x4db: v4db(0x4) = CONST 
    0x4dd: v4dd = ADD v4db(0x4), v4b4
    0x4e0: v4e0(0x0) = CONST 
    0x4e2: v4e2(0x40) = CONST 
    0x4e4: v4e4 = MLOAD v4e2(0x40)
    0x4e7: v4e7(0x4) = SUB v4dd, v4e4
    0x4ea: v4ea = GAS 
    0x4eb: v4eb = STATICCALL v4ea, v4b1, v4e4, v4e7(0x4), v4e4, v4e0(0x0)
    0x4ef: v4ef = RETURNDATASIZE 
    0x4f1: v4f1(0x0) = CONST 
    0x4f4: v4f4 = EQ v4ef, v4f1(0x0)
    0x4f5: v4f5(0x51a) = CONST 
    0x4f8: JUMPI v4f5(0x51a), v4f4

    Begin block 0x4f9
    prev=[0x495], succ=[0x51f]
    =================================
    0x4f9: v4f9(0x40) = CONST 
    0x4fb: v4fb = MLOAD v4f9(0x40)
    0x4fe: v4fe(0x1f) = CONST 
    0x500: v500(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v4fe(0x1f)
    0x501: v501(0x3f) = CONST 
    0x503: v503 = RETURNDATASIZE 
    0x504: v504 = ADD v503, v501(0x3f)
    0x505: v505 = AND v504, v500(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x507: v507 = ADD v4fb, v505
    0x508: v508(0x40) = CONST 
    0x50a: MSTORE v508(0x40), v507
    0x50b: v50b = RETURNDATASIZE 
    0x50d: MSTORE v4fb, v50b
    0x50e: v50e = RETURNDATASIZE 
    0x50f: v50f(0x0) = CONST 
    0x511: v511(0x20) = CONST 
    0x514: v514 = ADD v4fb, v511(0x20)
    0x515: RETURNDATACOPY v514, v50f(0x0), v50e
    0x516: v516(0x51f) = CONST 
    0x519: JUMP v516(0x51f)

    Begin block 0x51f
    prev=[0x4f9, 0x51a], succ=[0x52c, 0x530]
    =================================
    0x526: v526 = ISZERO v4eb
    0x527: v527 = ISZERO v526
    0x528: v528(0x530) = CONST 
    0x52b: JUMPI v528(0x530), v527

    Begin block 0x52c
    prev=[0x51f], succ=[]
    =================================
    0x52c: v52c(0x0) = CONST 
    0x52f: REVERT v52c(0x0), v52c(0x0)

    Begin block 0x530
    prev=[0x51f], succ=[0x541, 0x545]
    =================================
    0x530_0x0: v530_0 = PHI v4fb, v51b(0x60)
    0x533: v533(0x20) = CONST 
    0x535: v535 = ADD v533(0x20), v530_0
    0x537: v537 = MLOAD v530_0
    0x538: v538(0x20) = CONST 
    0x53b: v53b = LT v537, v538(0x20)
    0x53c: v53c = ISZERO v53b
    0x53d: v53d(0x545) = CONST 
    0x540: JUMPI v53d(0x545), v53c

    Begin block 0x541
    prev=[0x530], succ=[]
    =================================
    0x541: v541(0x0) = CONST 
    0x544: REVERT v541(0x0), v541(0x0)

    Begin block 0x545
    prev=[0x530], succ=[0xf7]
    =================================
    0x547: v547 = ADD v535, v537
    0x54b: v54b = MLOAD v535
    0x54d: v54d(0x20) = CONST 
    0x54f: v54f = ADD v54d(0x20), v535
    0x55e: JUMP vb6(0xf7)

    Begin block 0xf7
    prev=[0x545], succ=[]
    =================================
    0xf8: vf8(0x40) = CONST 
    0xfa: vfa = MLOAD vf8(0x40)
    0xfd: vfd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x112: v112 = AND vfd(0xffffffffffffffffffffffffffffffffffffffff), v54b
    0x113: v113(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x128: v128 = AND v113(0xffffffffffffffffffffffffffffffffffffffff), v112
    0x12a: MSTORE vfa, v128
    0x12b: v12b(0x20) = CONST 
    0x12d: v12d = ADD v12b(0x20), vfa
    0x131: v131(0x40) = CONST 
    0x133: v133 = MLOAD v131(0x40)
    0x136: v136(0x20) = SUB v12d, v133
    0x138: RETURN v133, v136(0x20)

    Begin block 0x51a
    prev=[0x495], succ=[0x51f]
    =================================
    0x51b: v51b(0x60) = CONST 

}

function fallback()() public {
    Begin block 0xba8
    prev=[], succ=[]
    =================================
    0xba9: vba9(0x0) = CONST 
    0xbac: REVERT vba9(0x0), vba9(0x0)

}

