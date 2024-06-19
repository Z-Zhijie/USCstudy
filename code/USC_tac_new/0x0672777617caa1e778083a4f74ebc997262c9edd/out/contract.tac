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
    prev=[0x0], succ=[0x1a, 0xa9a]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0xa75: va75(0xa9a) = CONST 
    0xa76: JUMPI va75(0xa9a), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x5b, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0xabf158d5) = CONST 
    0x26: v26 = GT v21(0xabf158d5), v1f
    0x27: v27(0x5b) = CONST 
    0x2a: JUMPI v27(0x5b), v26

    Begin block 0x5b
    prev=[0x1a], succ=[0xa85, 0x67]
    =================================
    0x5d: v5d(0x5536b682) = CONST 
    0x62: v62 = EQ v5d(0x5536b682), v1f
    0xa7f: va7f(0xa85) = CONST 
    0xa80: JUMPI va7f(0xa85), v62

    Begin block 0xa85
    prev=[0x5b], succ=[]
    =================================
    0xa86: va86(0x82) = CONST 
    0xa87: CALLPRIVATE va86(0x82)

    Begin block 0x67
    prev=[0x5b], succ=[0xa88, 0x72]
    =================================
    0x68: v68(0x6e699d87) = CONST 
    0x6d: v6d = EQ v68(0x6e699d87), v1f
    0xa81: va81(0xa88) = CONST 
    0xa82: JUMPI va81(0xa88), v6d

    Begin block 0xa88
    prev=[0x67], succ=[]
    =================================
    0xa89: va89(0xc2) = CONST 
    0xa8a: CALLPRIVATE va89(0xc2)

    Begin block 0x72
    prev=[0x67], succ=[0xa8b, 0x7d]
    =================================
    0x73: v73(0x7b103999) = CONST 
    0x78: v78 = EQ v73(0x7b103999), v1f
    0xa83: va83(0xa8b) = CONST 
    0xa84: JUMPI va83(0xa8b), v78

    Begin block 0xa8b
    prev=[0x72], succ=[]
    =================================
    0xa8c: va8c(0xfa) = CONST 
    0xa8d: CALLPRIVATE va8c(0xfa)

    Begin block 0x7d
    prev=[0x72], succ=[]
    =================================
    0x7e: v7e(0x0) = CONST 
    0x81: REVERT v7e(0x0), v7e(0x0)

    Begin block 0x2b
    prev=[0x1a], succ=[0xa8e, 0x36]
    =================================
    0x2c: v2c(0xabf158d5) = CONST 
    0x31: v31 = EQ v2c(0xabf158d5), v1f
    0xa77: va77(0xa8e) = CONST 
    0xa78: JUMPI va77(0xa8e), v31

    Begin block 0xa8e
    prev=[0x2b], succ=[]
    =================================
    0xa8f: va8f(0x11e) = CONST 
    0xa90: CALLPRIVATE va8f(0x11e)

    Begin block 0x36
    prev=[0x2b], succ=[0xa91, 0x41]
    =================================
    0x37: v37(0xc08b3f9d) = CONST 
    0x3c: v3c = EQ v37(0xc08b3f9d), v1f
    0xa79: va79(0xa91) = CONST 
    0xa7a: JUMPI va79(0xa91), v3c

    Begin block 0xa91
    prev=[0x36], succ=[]
    =================================
    0xa92: va92(0x147) = CONST 
    0xa93: CALLPRIVATE va92(0x147)

    Begin block 0x41
    prev=[0x36], succ=[0xa94, 0x4c]
    =================================
    0x42: v42(0xc4d66de8) = CONST 
    0x47: v47 = EQ v42(0xc4d66de8), v1f
    0xa7b: va7b(0xa94) = CONST 
    0xa7c: JUMPI va7b(0xa94), v47

    Begin block 0xa94
    prev=[0x41], succ=[]
    =================================
    0xa95: va95(0x183) = CONST 
    0xa96: CALLPRIVATE va95(0x183)

    Begin block 0x4c
    prev=[0x41], succ=[0x57, 0xa97]
    =================================
    0x4d: v4d(0xc98cc002) = CONST 
    0x52: v52 = EQ v4d(0xc98cc002), v1f
    0xa7d: va7d(0xa97) = CONST 
    0xa7e: JUMPI va7d(0xa97), v52

    Begin block 0x57
    prev=[0x4c], succ=[0x9aa]
    =================================
    0x57: v57(0x9aa) = CONST 
    0x5a: JUMP v57(0x9aa)

    Begin block 0x9aa
    prev=[0x57], succ=[]
    =================================
    0x9ab: v9ab(0x0) = CONST 
    0x9ae: REVERT v9ab(0x0), v9ab(0x0)

    Begin block 0xa97
    prev=[0x4c], succ=[]
    =================================
    0xa98: va98(0x1a9) = CONST 
    0xa99: CALLPRIVATE va98(0x1a9)

    Begin block 0xa9a
    prev=[0x10], succ=[]
    =================================
    0xa9b: va9b(0x986) = CONST 
    0xa9c: CALLPRIVATE va9b(0x986)

}

function logRewardParams(uint256,uint256,uint256)() public {
    Begin block 0x11e
    prev=[], succ=[0x130, 0x134]
    =================================
    0x11f: v11f(0xa10) = CONST 
    0x122: v122(0x4) = CONST 
    0x125: v125 = CALLDATASIZE 
    0x126: v126 = SUB v125, v122(0x4)
    0x127: v127(0x60) = CONST 
    0x12a: v12a = LT v126, v127(0x60)
    0x12b: v12b = ISZERO v12a
    0x12c: v12c(0x134) = CONST 
    0x12f: JUMPI v12c(0x134), v12b

    Begin block 0x130
    prev=[0x11e], succ=[]
    =================================
    0x130: v130(0x0) = CONST 
    0x133: REVERT v130(0x0), v130(0x0)

    Begin block 0x134
    prev=[0x11e], succ=[0x512]
    =================================
    0x137: v137 = CALLDATALOAD v122(0x4)
    0x139: v139(0x20) = CONST 
    0x13c: v13c(0x24) = ADD v122(0x4), v139(0x20)
    0x13d: v13d = CALLDATALOAD v13c(0x24)
    0x13f: v13f(0x40) = CONST 
    0x141: v141(0x44) = ADD v13f(0x40), v122(0x4)
    0x142: v142 = CALLDATALOAD v141(0x44)
    0x143: v143(0x512) = CONST 
    0x146: JUMP v143(0x512)

    Begin block 0x512
    prev=[0x134], succ=[0x557, 0x55b]
    =================================
    0x513: v513(0x0) = CONST 
    0x515: v515 = SLOAD v513(0x0)
    0x516: v516(0x40) = CONST 
    0x519: v519 = MLOAD v516(0x40)
    0x51a: v51a(0xa1ef8f9) = CONST 
    0x51f: v51f(0xe2) = CONST 
    0x521: v521(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v51f(0xe2), v51a(0xa1ef8f9)
    0x523: MSTORE v519, v521(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x525: v525 = MLOAD v516(0x40)
    0x526: v526 = CALLER 
    0x528: v528(0x100) = CONST 
    0x52c: v52c = DIV v515, v528(0x100)
    0x52d: v52d(0x1) = CONST 
    0x52f: v52f(0x1) = CONST 
    0x531: v531(0xa0) = CONST 
    0x533: v533(0x10000000000000000000000000000000000000000) = SHL v531(0xa0), v52f(0x1)
    0x534: v534(0xffffffffffffffffffffffffffffffffffffffff) = SUB v533(0x10000000000000000000000000000000000000000), v52d(0x1)
    0x535: v535 = AND v534(0xffffffffffffffffffffffffffffffffffffffff), v52c
    0x537: v537(0x287be3e4) = CONST 
    0x53d: v53d(0x4) = CONST 
    0x541: v541 = ADD v519, v53d(0x4)
    0x543: v543(0x20) = CONST 
    0x54a: v54a(0x0) = SUB v519, v525
    0x54b: v54b(0x4) = ADD v54a(0x0), v53d(0x4)
    0x54f: v54f = EXTCODESIZE v535
    0x550: v550 = ISZERO v54f
    0x552: v552 = ISZERO v550
    0x553: v553(0x55b) = CONST 
    0x556: JUMPI v553(0x55b), v552

    Begin block 0x557
    prev=[0x512], succ=[]
    =================================
    0x557: v557(0x0) = CONST 
    0x55a: REVERT v557(0x0), v557(0x0)

    Begin block 0x55b
    prev=[0x512], succ=[0x566, 0x56f]
    =================================
    0x55d: v55d = GAS 
    0x55e: v55e = STATICCALL v55d, v535, v525, v54b(0x4), v525, v543(0x20)
    0x55f: v55f = ISZERO v55e
    0x561: v561 = ISZERO v55f
    0x562: v562(0x56f) = CONST 
    0x565: JUMPI v562(0x56f), v561

    Begin block 0x566
    prev=[0x55b], succ=[]
    =================================
    0x566: v566 = RETURNDATASIZE 
    0x567: v567(0x0) = CONST 
    0x56a: RETURNDATACOPY v567(0x0), v567(0x0), v566
    0x56b: v56b = RETURNDATASIZE 
    0x56c: v56c(0x0) = CONST 
    0x56e: REVERT v56c(0x0), v56b

    Begin block 0x56f
    prev=[0x55b], succ=[0x581, 0x585]
    =================================
    0x574: v574(0x40) = CONST 
    0x576: v576 = MLOAD v574(0x40)
    0x577: v577 = RETURNDATASIZE 
    0x578: v578(0x20) = CONST 
    0x57b: v57b = LT v577, v578(0x20)
    0x57c: v57c = ISZERO v57b
    0x57d: v57d(0x585) = CONST 
    0x580: JUMPI v57d(0x585), v57c

    Begin block 0x581
    prev=[0x56f], succ=[]
    =================================
    0x581: v581(0x0) = CONST 
    0x584: REVERT v581(0x0), v581(0x0)

    Begin block 0x585
    prev=[0x56f], succ=[0x596, 0x5cc]
    =================================
    0x587: v587 = MLOAD v576
    0x588: v588(0x1) = CONST 
    0x58a: v58a(0x1) = CONST 
    0x58c: v58c(0xa0) = CONST 
    0x58e: v58e(0x10000000000000000000000000000000000000000) = SHL v58c(0xa0), v58a(0x1)
    0x58f: v58f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v58e(0x10000000000000000000000000000000000000000), v588(0x1)
    0x590: v590 = AND v58f(0xffffffffffffffffffffffffffffffffffffffff), v587
    0x591: v591 = EQ v590, v526
    0x592: v592(0x5cc) = CONST 
    0x595: JUMPI v592(0x5cc), v591

    Begin block 0x596
    prev=[0x585], succ=[]
    =================================
    0x596: v596(0x40) = CONST 
    0x598: v598 = MLOAD v596(0x40)
    0x599: v599(0x461bcd) = CONST 
    0x59d: v59d(0xe5) = CONST 
    0x59f: v59f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v59d(0xe5), v599(0x461bcd)
    0x5a1: MSTORE v598, v59f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5a2: v5a2(0x4) = CONST 
    0x5a4: v5a4 = ADD v5a2(0x4), v598
    0x5a7: v5a7(0x20) = CONST 
    0x5a9: v5a9 = ADD v5a7(0x20), v5a4
    0x5ac: v5ac(0x20) = SUB v5a9, v5a4
    0x5ae: MSTORE v5a4, v5ac(0x20)
    0x5af: v5af(0x21) = CONST 
    0x5b2: MSTORE v5a9, v5af(0x21)
    0x5b3: v5b3(0x20) = CONST 
    0x5b5: v5b5 = ADD v5b3(0x20), v5a9
    0x5b7: v5b7(0x912) = CONST 
    0x5ba: v5ba(0x21) = CONST 
    0x5bd: CODECOPY v5b5, v5b7(0x912), v5ba(0x21)
    0x5be: v5be(0x40) = CONST 
    0x5c0: v5c0 = ADD v5be(0x40), v5b5
    0x5c4: v5c4(0x40) = CONST 
    0x5c6: v5c6 = MLOAD v5c4(0x40)
    0x5c9: v5c9(0x84) = SUB v5c0, v5c6
    0x5cb: REVERT v5c6, v5c9(0x84)

    Begin block 0x5cc
    prev=[0x585], succ=[0xa10]
    =================================
    0x5cd: v5cd(0x40) = CONST 
    0x5d0: v5d0 = MLOAD v5cd(0x40)
    0x5d3: MSTORE v5d0, v137
    0x5d4: v5d4(0x20) = CONST 
    0x5d7: v5d7 = ADD v5d0, v5d4(0x20)
    0x5da: MSTORE v5d7, v13d
    0x5dd: v5dd = ADD v5cd(0x40), v5d0
    0x5e0: MSTORE v5dd, v142
    0x5e2: v5e2 = MLOAD v5cd(0x40)
    0x5e3: v5e3(0x801c2d11f1d1780f228c2a497cf5eae033694c8eb057d636044683def26e03ec) = CONST 
    0x607: v607(0x0) = SUB v5d0, v5e2
    0x608: v608(0x60) = CONST 
    0x60a: v60a(0x60) = ADD v608(0x60), v607(0x0)
    0x60c: LOG1 v5e2, v60a(0x60), v5e3(0x801c2d11f1d1780f228c2a497cf5eae033694c8eb057d636044683def26e03ec)
    0x610: JUMP v11f(0xa10)

    Begin block 0xa10
    prev=[0x5cc], succ=[]
    =================================
    0xa11: STOP 

}

function logSharesTransfer(uint256,address,address,uint256)() public {
    Begin block 0x147
    prev=[], succ=[0x159, 0x15d]
    =================================
    0x148: v148(0xa31) = CONST 
    0x14b: v14b(0x4) = CONST 
    0x14e: v14e = CALLDATASIZE 
    0x14f: v14f = SUB v14e, v14b(0x4)
    0x150: v150(0x80) = CONST 
    0x153: v153 = LT v14f, v150(0x80)
    0x154: v154 = ISZERO v153
    0x155: v155(0x15d) = CONST 
    0x158: JUMPI v155(0x15d), v154

    Begin block 0x159
    prev=[0x147], succ=[]
    =================================
    0x159: v159(0x0) = CONST 
    0x15c: REVERT v159(0x0), v159(0x0)

    Begin block 0x15d
    prev=[0x147], succ=[0x611]
    =================================
    0x160: v160 = CALLDATALOAD v14b(0x4)
    0x162: v162(0x1) = CONST 
    0x164: v164(0x1) = CONST 
    0x166: v166(0xa0) = CONST 
    0x168: v168(0x10000000000000000000000000000000000000000) = SHL v166(0xa0), v164(0x1)
    0x169: v169(0xffffffffffffffffffffffffffffffffffffffff) = SUB v168(0x10000000000000000000000000000000000000000), v162(0x1)
    0x16a: v16a(0x20) = CONST 
    0x16d: v16d(0x24) = ADD v14b(0x4), v16a(0x20)
    0x16e: v16e = CALLDATALOAD v16d(0x24)
    0x170: v170 = AND v169(0xffffffffffffffffffffffffffffffffffffffff), v16e
    0x172: v172(0x40) = CONST 
    0x175: v175(0x44) = ADD v14b(0x4), v172(0x40)
    0x176: v176 = CALLDATALOAD v175(0x44)
    0x179: v179 = AND v169(0xffffffffffffffffffffffffffffffffffffffff), v176
    0x17b: v17b(0x60) = CONST 
    0x17d: v17d(0x64) = ADD v17b(0x60), v14b(0x4)
    0x17e: v17e = CALLDATALOAD v17d(0x64)
    0x17f: v17f(0x611) = CONST 
    0x182: JUMP v17f(0x611)

    Begin block 0x611
    prev=[0x15d], succ=[0x65d, 0x661]
    =================================
    0x613: v613(0x0) = CONST 
    0x616: v616(0x1) = CONST 
    0x619: v619 = SLOAD v613(0x0)
    0x61b: v61b(0x100) = CONST 
    0x61e: v61e(0x100) = EXP v61b(0x100), v616(0x1)
    0x620: v620 = DIV v619, v61e(0x100)
    0x621: v621(0x1) = CONST 
    0x623: v623(0x1) = CONST 
    0x625: v625(0xa0) = CONST 
    0x627: v627(0x10000000000000000000000000000000000000000) = SHL v625(0xa0), v623(0x1)
    0x628: v628(0xffffffffffffffffffffffffffffffffffffffff) = SUB v627(0x10000000000000000000000000000000000000000), v621(0x1)
    0x629: v629 = AND v628(0xffffffffffffffffffffffffffffffffffffffff), v620
    0x62a: v62a(0x1) = CONST 
    0x62c: v62c(0x1) = CONST 
    0x62e: v62e(0xa0) = CONST 
    0x630: v630(0x10000000000000000000000000000000000000000) = SHL v62e(0xa0), v62c(0x1)
    0x631: v631(0xffffffffffffffffffffffffffffffffffffffff) = SUB v630(0x10000000000000000000000000000000000000000), v62a(0x1)
    0x632: v632 = AND v631(0xffffffffffffffffffffffffffffffffffffffff), v629
    0x633: v633(0x287be3e4) = CONST 
    0x638: v638(0x40) = CONST 
    0x63a: v63a = MLOAD v638(0x40)
    0x63c: v63c(0xffffffff) = CONST 
    0x641: v641(0x287be3e4) = AND v63c(0xffffffff), v633(0x287be3e4)
    0x642: v642(0xe0) = CONST 
    0x644: v644(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v642(0xe0), v641(0x287be3e4)
    0x646: MSTORE v63a, v644(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x647: v647(0x4) = CONST 
    0x649: v649 = ADD v647(0x4), v63a
    0x64a: v64a(0x20) = CONST 
    0x64c: v64c(0x40) = CONST 
    0x64e: v64e = MLOAD v64c(0x40)
    0x651: v651(0x4) = SUB v649, v64e
    0x655: v655 = EXTCODESIZE v632
    0x656: v656 = ISZERO v655
    0x658: v658 = ISZERO v656
    0x659: v659(0x661) = CONST 
    0x65c: JUMPI v659(0x661), v658

    Begin block 0x65d
    prev=[0x611], succ=[]
    =================================
    0x65d: v65d(0x0) = CONST 
    0x660: REVERT v65d(0x0), v65d(0x0)

    Begin block 0x661
    prev=[0x611], succ=[0x66c, 0x675]
    =================================
    0x663: v663 = GAS 
    0x664: v664 = STATICCALL v663, v632, v64e, v651(0x4), v64e, v64a(0x20)
    0x665: v665 = ISZERO v664
    0x667: v667 = ISZERO v665
    0x668: v668(0x675) = CONST 
    0x66b: JUMPI v668(0x675), v667

    Begin block 0x66c
    prev=[0x661], succ=[]
    =================================
    0x66c: v66c = RETURNDATASIZE 
    0x66d: v66d(0x0) = CONST 
    0x670: RETURNDATACOPY v66d(0x0), v66d(0x0), v66c
    0x671: v671 = RETURNDATASIZE 
    0x672: v672(0x0) = CONST 
    0x674: REVERT v672(0x0), v671

    Begin block 0x675
    prev=[0x661], succ=[0x687, 0x68b]
    =================================
    0x67a: v67a(0x40) = CONST 
    0x67c: v67c = MLOAD v67a(0x40)
    0x67d: v67d = RETURNDATASIZE 
    0x67e: v67e(0x20) = CONST 
    0x681: v681 = LT v67d, v67e(0x20)
    0x682: v682 = ISZERO v681
    0x683: v683(0x68b) = CONST 
    0x686: JUMPI v683(0x68b), v682

    Begin block 0x687
    prev=[0x675], succ=[]
    =================================
    0x687: v687(0x0) = CONST 
    0x68a: REVERT v687(0x0), v687(0x0)

    Begin block 0x68b
    prev=[0x675], succ=[0x6d2, 0x6d6]
    =================================
    0x68d: v68d = MLOAD v67c
    0x68e: v68e(0x40) = CONST 
    0x691: v691 = MLOAD v68e(0x40)
    0x692: v692(0xd6a8b91) = CONST 
    0x697: v697(0xe2) = CONST 
    0x699: v699(0x35aa2e4400000000000000000000000000000000000000000000000000000000) = SHL v697(0xe2), v692(0xd6a8b91)
    0x69b: MSTORE v691, v699(0x35aa2e4400000000000000000000000000000000000000000000000000000000)
    0x69c: v69c(0x4) = CONST 
    0x69f: v69f = ADD v691, v69c(0x4)
    0x6a2: MSTORE v69f, v160
    0x6a4: v6a4 = MLOAD v68e(0x40)
    0x6a5: v6a5(0x1) = CONST 
    0x6a7: v6a7(0x1) = CONST 
    0x6a9: v6a9(0xa0) = CONST 
    0x6ab: v6ab(0x10000000000000000000000000000000000000000) = SHL v6a9(0xa0), v6a7(0x1)
    0x6ac: v6ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ab(0x10000000000000000000000000000000000000000), v6a5(0x1)
    0x6af: v6af = AND v68d, v6ac(0xffffffffffffffffffffffffffffffffffffffff)
    0x6b1: v6b1(0x35aa2e44) = CONST 
    0x6b7: v6b7(0x24) = CONST 
    0x6bb: v6bb = ADD v691, v6b7(0x24)
    0x6bd: v6bd(0xe0) = CONST 
    0x6c5: v6c5(0x0) = SUB v691, v6a4
    0x6c6: v6c6(0x24) = ADD v6c5(0x0), v6b7(0x24)
    0x6ca: v6ca = EXTCODESIZE v6af
    0x6cb: v6cb = ISZERO v6ca
    0x6cd: v6cd = ISZERO v6cb
    0x6ce: v6ce(0x6d6) = CONST 
    0x6d1: JUMPI v6ce(0x6d6), v6cd

    Begin block 0x6d2
    prev=[0x68b], succ=[]
    =================================
    0x6d2: v6d2(0x0) = CONST 
    0x6d5: REVERT v6d2(0x0), v6d2(0x0)

    Begin block 0x6d6
    prev=[0x68b], succ=[0x6e1, 0x6ea]
    =================================
    0x6d8: v6d8 = GAS 
    0x6d9: v6d9 = STATICCALL v6d8, v6af, v6a4, v6c6(0x24), v6a4, v6bd(0xe0)
    0x6da: v6da = ISZERO v6d9
    0x6dc: v6dc = ISZERO v6da
    0x6dd: v6dd(0x6ea) = CONST 
    0x6e0: JUMPI v6dd(0x6ea), v6dc

    Begin block 0x6e1
    prev=[0x6d6], succ=[]
    =================================
    0x6e1: v6e1 = RETURNDATASIZE 
    0x6e2: v6e2(0x0) = CONST 
    0x6e5: RETURNDATACOPY v6e2(0x0), v6e2(0x0), v6e1
    0x6e6: v6e6 = RETURNDATASIZE 
    0x6e7: v6e7(0x0) = CONST 
    0x6e9: REVERT v6e7(0x0), v6e6

    Begin block 0x6ea
    prev=[0x6d6], succ=[0x6fc, 0x700]
    =================================
    0x6ef: v6ef(0x40) = CONST 
    0x6f1: v6f1 = MLOAD v6ef(0x40)
    0x6f2: v6f2 = RETURNDATASIZE 
    0x6f3: v6f3(0xe0) = CONST 
    0x6f6: v6f6 = LT v6f2, v6f3(0xe0)
    0x6f7: v6f7 = ISZERO v6f6
    0x6f8: v6f8(0x700) = CONST 
    0x6fb: JUMPI v6f8(0x700), v6f7

    Begin block 0x6fc
    prev=[0x6ea], succ=[]
    =================================
    0x6fc: v6fc(0x0) = CONST 
    0x6ff: REVERT v6fc(0x0), v6fc(0x0)

    Begin block 0x700
    prev=[0x6ea], succ=[0x718, 0x754]
    =================================
    0x702: v702(0xc0) = CONST 
    0x704: v704 = ADD v702(0xc0), v6f1
    0x705: v705 = MLOAD v704
    0x708: v708(0x1) = CONST 
    0x70a: v70a(0x1) = CONST 
    0x70c: v70c(0xa0) = CONST 
    0x70e: v70e(0x10000000000000000000000000000000000000000) = SHL v70c(0xa0), v70a(0x1)
    0x70f: v70f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v70e(0x10000000000000000000000000000000000000000), v708(0x1)
    0x711: v711 = AND v705, v70f(0xffffffffffffffffffffffffffffffffffffffff)
    0x712: v712 = CALLER 
    0x713: v713 = EQ v712, v711
    0x714: v714(0x754) = CONST 
    0x717: JUMPI v714(0x754), v713

    Begin block 0x718
    prev=[0x700], succ=[]
    =================================
    0x718: v718(0x40) = CONST 
    0x71b: v71b = MLOAD v718(0x40)
    0x71c: v71c(0x461bcd) = CONST 
    0x720: v720(0xe5) = CONST 
    0x722: v722(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v720(0xe5), v71c(0x461bcd)
    0x724: MSTORE v71b, v722(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x725: v725(0x20) = CONST 
    0x727: v727(0x4) = CONST 
    0x72a: v72a = ADD v71b, v727(0x4)
    0x72b: MSTORE v72a, v725(0x20)
    0x72c: v72c(0xd) = CONST 
    0x72e: v72e(0x24) = CONST 
    0x731: v731 = ADD v71b, v72e(0x24)
    0x732: MSTORE v731, v72c(0xd)
    0x733: v733(0x3737ba103b30b634b230ba37b9) = CONST 
    0x741: v741(0x99) = CONST 
    0x743: v743(0x6e6f742076616c696461746f7200000000000000000000000000000000000000) = SHL v741(0x99), v733(0x3737ba103b30b634b230ba37b9)
    0x744: v744(0x44) = CONST 
    0x747: v747 = ADD v71b, v744(0x44)
    0x748: MSTORE v747, v743(0x6e6f742076616c696461746f7200000000000000000000000000000000000000)
    0x74a: v74a = MLOAD v718(0x40)
    0x74e: v74e(0x0) = SUB v71b, v74a
    0x74f: v74f(0x64) = CONST 
    0x751: v751(0x64) = ADD v74f(0x64), v74e(0x0)
    0x753: REVERT v74a, v751(0x64)

    Begin block 0x754
    prev=[0x700], succ=[0xa31]
    =================================
    0x756: v756(0x1) = CONST 
    0x758: v758(0x1) = CONST 
    0x75a: v75a(0xa0) = CONST 
    0x75c: v75c(0x10000000000000000000000000000000000000000) = SHL v75a(0xa0), v758(0x1)
    0x75d: v75d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75c(0x10000000000000000000000000000000000000000), v756(0x1)
    0x75e: v75e = AND v75d(0xffffffffffffffffffffffffffffffffffffffff), v179
    0x760: v760(0x1) = CONST 
    0x762: v762(0x1) = CONST 
    0x764: v764(0xa0) = CONST 
    0x766: v766(0x10000000000000000000000000000000000000000) = SHL v764(0xa0), v762(0x1)
    0x767: v767(0xffffffffffffffffffffffffffffffffffffffff) = SUB v766(0x10000000000000000000000000000000000000000), v760(0x1)
    0x768: v768 = AND v767(0xffffffffffffffffffffffffffffffffffffffff), v170
    0x76a: v76a(0xa11785f16076d5ade1b5a7a0867d5ec042b8ae8c4f0609d0a72bfd062ba2ee0) = CONST 
    0x78c: v78c(0x40) = CONST 
    0x78e: v78e = MLOAD v78c(0x40)
    0x792: MSTORE v78e, v17e
    0x793: v793(0x20) = CONST 
    0x795: v795 = ADD v793(0x20), v78e
    0x799: v799(0x40) = CONST 
    0x79b: v79b = MLOAD v799(0x40)
    0x79e: v79e(0x20) = SUB v795, v79b
    0x7a0: LOG4 v79b, v79e(0x20), v76a(0xa11785f16076d5ade1b5a7a0867d5ec042b8ae8c4f0609d0a72bfd062ba2ee0), v160, v768, v75e
    0x7a7: JUMP v148(0xa31)

    Begin block 0xa31
    prev=[0x754], succ=[]
    =================================
    0xa32: STOP 

}

function initialize(address)() public {
    Begin block 0x183
    prev=[], succ=[0x195, 0x199]
    =================================
    0x184: v184(0xa52) = CONST 
    0x187: v187(0x4) = CONST 
    0x18a: v18a = CALLDATASIZE 
    0x18b: v18b = SUB v18a, v187(0x4)
    0x18c: v18c(0x20) = CONST 
    0x18f: v18f = LT v18b, v18c(0x20)
    0x190: v190 = ISZERO v18f
    0x191: v191(0x199) = CONST 
    0x194: JUMPI v191(0x199), v190

    Begin block 0x195
    prev=[0x183], succ=[]
    =================================
    0x195: v195(0x0) = CONST 
    0x198: REVERT v195(0x0), v195(0x0)

    Begin block 0x199
    prev=[0x183], succ=[0x7a8]
    =================================
    0x19b: v19b = CALLDATALOAD v187(0x4)
    0x19c: v19c(0x1) = CONST 
    0x19e: v19e(0x1) = CONST 
    0x1a0: v1a0(0xa0) = CONST 
    0x1a2: v1a2(0x10000000000000000000000000000000000000000) = SHL v1a0(0xa0), v19e(0x1)
    0x1a3: v1a3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a2(0x10000000000000000000000000000000000000000), v19c(0x1)
    0x1a4: v1a4 = AND v1a3(0xffffffffffffffffffffffffffffffffffffffff), v19b
    0x1a5: v1a5(0x7a8) = CONST 
    0x1a8: JUMP v1a5(0x7a8)

    Begin block 0x7a8
    prev=[0x199], succ=[0x7b4, 0x7f1]
    =================================
    0x7a9: v7a9(0x0) = CONST 
    0x7ab: v7ab = SLOAD v7a9(0x0)
    0x7ac: v7ac(0xff) = CONST 
    0x7ae: v7ae = AND v7ac(0xff), v7ab
    0x7af: v7af = ISZERO v7ae
    0x7b0: v7b0(0x7f1) = CONST 
    0x7b3: JUMPI v7b0(0x7f1), v7af

    Begin block 0x7b4
    prev=[0x7a8], succ=[]
    =================================
    0x7b4: v7b4(0x40) = CONST 
    0x7b7: v7b7 = MLOAD v7b4(0x40)
    0x7b8: v7b8(0x461bcd) = CONST 
    0x7bc: v7bc(0xe5) = CONST 
    0x7be: v7be(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7bc(0xe5), v7b8(0x461bcd)
    0x7c0: MSTORE v7b7, v7be(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7c1: v7c1(0x20) = CONST 
    0x7c3: v7c3(0x4) = CONST 
    0x7c6: v7c6 = ADD v7b7, v7c3(0x4)
    0x7c7: MSTORE v7c6, v7c1(0x20)
    0x7c8: v7c8(0xe) = CONST 
    0x7ca: v7ca(0x24) = CONST 
    0x7cd: v7cd = ADD v7b7, v7ca(0x24)
    0x7ce: MSTORE v7cd, v7c8(0xe)
    0x7cf: v7cf(0x185b1c9958591e481a5b9a5d1959) = CONST 
    0x7de: v7de(0x92) = CONST 
    0x7e0: v7e0(0x616c726561647920696e69746564000000000000000000000000000000000000) = SHL v7de(0x92), v7cf(0x185b1c9958591e481a5b9a5d1959)
    0x7e1: v7e1(0x44) = CONST 
    0x7e4: v7e4 = ADD v7b7, v7e1(0x44)
    0x7e5: MSTORE v7e4, v7e0(0x616c726561647920696e69746564000000000000000000000000000000000000)
    0x7e7: v7e7 = MLOAD v7b4(0x40)
    0x7eb: v7eb(0x0) = SUB v7b7, v7e7
    0x7ec: v7ec(0x64) = CONST 
    0x7ee: v7ee(0x64) = ADD v7ec(0x64), v7eb(0x0)
    0x7f0: REVERT v7e7, v7ee(0x64)

    Begin block 0x7f1
    prev=[0x7a8], succ=[0xa52]
    =================================
    0x7f2: v7f2(0x0) = CONST 
    0x7f5: v7f5 = SLOAD v7f2(0x0)
    0x7f6: v7f6(0x1) = CONST 
    0x7f8: v7f8(0x1) = CONST 
    0x7fa: v7fa(0xa0) = CONST 
    0x7fc: v7fc(0x10000000000000000000000000000000000000000) = SHL v7fa(0xa0), v7f8(0x1)
    0x7fd: v7fd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7fc(0x10000000000000000000000000000000000000000), v7f6(0x1)
    0x800: v800 = AND v1a4, v7fd(0xffffffffffffffffffffffffffffffffffffffff)
    0x801: v801(0x100) = CONST 
    0x804: v804 = MUL v801(0x100), v800
    0x805: v805(0x100) = CONST 
    0x808: v808(0x1) = CONST 
    0x80a: v80a(0xa8) = CONST 
    0x80c: v80c(0x1000000000000000000000000000000000000000000) = SHL v80a(0xa8), v808(0x1)
    0x80d: v80d(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v80c(0x1000000000000000000000000000000000000000000), v805(0x100)
    0x80e: v80e(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v80d(0xffffffffffffffffffffffffffffffffffffffff00)
    0x80f: v80f(0xff) = CONST 
    0x811: v811(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v80f(0xff)
    0x814: v814 = AND v7f5, v811(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x815: v815(0x1) = CONST 
    0x817: v817 = OR v815(0x1), v814
    0x81b: v81b = AND v817, v80e(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff)
    0x81f: v81f = OR v81b, v804
    0x821: SSTORE v7f2(0x0), v81f
    0x822: JUMP v184(0xa52)

    Begin block 0xa52
    prev=[0x7f1], succ=[]
    =================================
    0xa53: STOP 

}

function logUpdateCommissionRate(uint256,uint256,uint256)() public {
    Begin block 0x1a9
    prev=[], succ=[0x1bb, 0x1bf]
    =================================
    0x1aa: v1aa(0xa73) = CONST 
    0x1ad: v1ad(0x4) = CONST 
    0x1b0: v1b0 = CALLDATASIZE 
    0x1b1: v1b1 = SUB v1b0, v1ad(0x4)
    0x1b2: v1b2(0x60) = CONST 
    0x1b5: v1b5 = LT v1b1, v1b2(0x60)
    0x1b6: v1b6 = ISZERO v1b5
    0x1b7: v1b7(0x1bf) = CONST 
    0x1ba: JUMPI v1b7(0x1bf), v1b6

    Begin block 0x1bb
    prev=[0x1a9], succ=[]
    =================================
    0x1bb: v1bb(0x0) = CONST 
    0x1be: REVERT v1bb(0x0), v1bb(0x0)

    Begin block 0x1bf
    prev=[0x1a9], succ=[0x823]
    =================================
    0x1c2: v1c2 = CALLDATALOAD v1ad(0x4)
    0x1c4: v1c4(0x20) = CONST 
    0x1c7: v1c7(0x24) = ADD v1ad(0x4), v1c4(0x20)
    0x1c8: v1c8 = CALLDATALOAD v1c7(0x24)
    0x1ca: v1ca(0x40) = CONST 
    0x1cc: v1cc(0x44) = ADD v1ca(0x40), v1ad(0x4)
    0x1cd: v1cd = CALLDATALOAD v1cc(0x44)
    0x1ce: v1ce(0x823) = CONST 
    0x1d1: JUMP v1ce(0x823)

    Begin block 0x823
    prev=[0x1bf], succ=[0x868, 0x86c]
    =================================
    0x824: v824(0x0) = CONST 
    0x826: v826 = SLOAD v824(0x0)
    0x827: v827(0x40) = CONST 
    0x82a: v82a = MLOAD v827(0x40)
    0x82b: v82b(0xa1ef8f9) = CONST 
    0x830: v830(0xe2) = CONST 
    0x832: v832(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v830(0xe2), v82b(0xa1ef8f9)
    0x834: MSTORE v82a, v832(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x836: v836 = MLOAD v827(0x40)
    0x837: v837 = CALLER 
    0x839: v839(0x100) = CONST 
    0x83d: v83d = DIV v826, v839(0x100)
    0x83e: v83e(0x1) = CONST 
    0x840: v840(0x1) = CONST 
    0x842: v842(0xa0) = CONST 
    0x844: v844(0x10000000000000000000000000000000000000000) = SHL v842(0xa0), v840(0x1)
    0x845: v845(0xffffffffffffffffffffffffffffffffffffffff) = SUB v844(0x10000000000000000000000000000000000000000), v83e(0x1)
    0x846: v846 = AND v845(0xffffffffffffffffffffffffffffffffffffffff), v83d
    0x848: v848(0x287be3e4) = CONST 
    0x84e: v84e(0x4) = CONST 
    0x852: v852 = ADD v82a, v84e(0x4)
    0x854: v854(0x20) = CONST 
    0x85b: v85b(0x0) = SUB v82a, v836
    0x85c: v85c(0x4) = ADD v85b(0x0), v84e(0x4)
    0x860: v860 = EXTCODESIZE v846
    0x861: v861 = ISZERO v860
    0x863: v863 = ISZERO v861
    0x864: v864(0x86c) = CONST 
    0x867: JUMPI v864(0x86c), v863

    Begin block 0x868
    prev=[0x823], succ=[]
    =================================
    0x868: v868(0x0) = CONST 
    0x86b: REVERT v868(0x0), v868(0x0)

    Begin block 0x86c
    prev=[0x823], succ=[0x877, 0x880]
    =================================
    0x86e: v86e = GAS 
    0x86f: v86f = STATICCALL v86e, v846, v836, v85c(0x4), v836, v854(0x20)
    0x870: v870 = ISZERO v86f
    0x872: v872 = ISZERO v870
    0x873: v873(0x880) = CONST 
    0x876: JUMPI v873(0x880), v872

    Begin block 0x877
    prev=[0x86c], succ=[]
    =================================
    0x877: v877 = RETURNDATASIZE 
    0x878: v878(0x0) = CONST 
    0x87b: RETURNDATACOPY v878(0x0), v878(0x0), v877
    0x87c: v87c = RETURNDATASIZE 
    0x87d: v87d(0x0) = CONST 
    0x87f: REVERT v87d(0x0), v87c

    Begin block 0x880
    prev=[0x86c], succ=[0x892, 0x896]
    =================================
    0x885: v885(0x40) = CONST 
    0x887: v887 = MLOAD v885(0x40)
    0x888: v888 = RETURNDATASIZE 
    0x889: v889(0x20) = CONST 
    0x88c: v88c = LT v888, v889(0x20)
    0x88d: v88d = ISZERO v88c
    0x88e: v88e(0x896) = CONST 
    0x891: JUMPI v88e(0x896), v88d

    Begin block 0x892
    prev=[0x880], succ=[]
    =================================
    0x892: v892(0x0) = CONST 
    0x895: REVERT v892(0x0), v892(0x0)

    Begin block 0x896
    prev=[0x880], succ=[0x8a7, 0x8dd]
    =================================
    0x898: v898 = MLOAD v887
    0x899: v899(0x1) = CONST 
    0x89b: v89b(0x1) = CONST 
    0x89d: v89d(0xa0) = CONST 
    0x89f: v89f(0x10000000000000000000000000000000000000000) = SHL v89d(0xa0), v89b(0x1)
    0x8a0: v8a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v89f(0x10000000000000000000000000000000000000000), v899(0x1)
    0x8a1: v8a1 = AND v8a0(0xffffffffffffffffffffffffffffffffffffffff), v898
    0x8a2: v8a2 = EQ v8a1, v837
    0x8a3: v8a3(0x8dd) = CONST 
    0x8a6: JUMPI v8a3(0x8dd), v8a2

    Begin block 0x8a7
    prev=[0x896], succ=[]
    =================================
    0x8a7: v8a7(0x40) = CONST 
    0x8a9: v8a9 = MLOAD v8a7(0x40)
    0x8aa: v8aa(0x461bcd) = CONST 
    0x8ae: v8ae(0xe5) = CONST 
    0x8b0: v8b0(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v8ae(0xe5), v8aa(0x461bcd)
    0x8b2: MSTORE v8a9, v8b0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8b3: v8b3(0x4) = CONST 
    0x8b5: v8b5 = ADD v8b3(0x4), v8a9
    0x8b8: v8b8(0x20) = CONST 
    0x8ba: v8ba = ADD v8b8(0x20), v8b5
    0x8bd: v8bd(0x20) = SUB v8ba, v8b5
    0x8bf: MSTORE v8b5, v8bd(0x20)
    0x8c0: v8c0(0x21) = CONST 
    0x8c3: MSTORE v8ba, v8c0(0x21)
    0x8c4: v8c4(0x20) = CONST 
    0x8c6: v8c6 = ADD v8c4(0x20), v8ba
    0x8c8: v8c8(0x912) = CONST 
    0x8cb: v8cb(0x21) = CONST 
    0x8ce: CODECOPY v8c6, v8c8(0x912), v8cb(0x21)
    0x8cf: v8cf(0x40) = CONST 
    0x8d1: v8d1 = ADD v8cf(0x40), v8c6
    0x8d5: v8d5(0x40) = CONST 
    0x8d7: v8d7 = MLOAD v8d5(0x40)
    0x8da: v8da(0x84) = SUB v8d1, v8d7
    0x8dc: REVERT v8d7, v8da(0x84)

    Begin block 0x8dd
    prev=[0x896], succ=[0xa73]
    =================================
    0x8e1: v8e1(0x7d5da5ece9d43013d62ab966f4704ca376b92be29ca6fbb958154baf1c0dc17e) = CONST 
    0x902: v902(0x40) = CONST 
    0x904: v904 = MLOAD v902(0x40)
    0x905: v905(0x40) = CONST 
    0x907: v907 = MLOAD v905(0x40)
    0x90a: v90a(0x0) = SUB v904, v907
    0x90c: LOG4 v907, v90a(0x0), v8e1(0x7d5da5ece9d43013d62ab966f4704ca376b92be29ca6fbb958154baf1c0dc17e), v1c2, v1c8, v1cd
    0x910: JUMP v1aa(0xa73)

    Begin block 0xa73
    prev=[0x8dd], succ=[]
    =================================
    0xa74: STOP 

}

function logShareBurnedWithId(uint256,address,uint256,uint256,uint256)() public {
    Begin block 0x82
    prev=[], succ=[0x94, 0x98]
    =================================
    0x83: v83(0x9ce) = CONST 
    0x86: v86(0x4) = CONST 
    0x89: v89 = CALLDATASIZE 
    0x8a: v8a = SUB v89, v86(0x4)
    0x8b: v8b(0xa0) = CONST 
    0x8e: v8e = LT v8a, v8b(0xa0)
    0x8f: v8f = ISZERO v8e
    0x90: v90(0x98) = CONST 
    0x93: JUMPI v90(0x98), v8f

    Begin block 0x94
    prev=[0x82], succ=[]
    =================================
    0x94: v94(0x0) = CONST 
    0x97: REVERT v94(0x0), v94(0x0)

    Begin block 0x98
    prev=[0x82], succ=[0x1d2]
    =================================
    0x9b: v9b = CALLDATALOAD v86(0x4)
    0x9d: v9d(0x1) = CONST 
    0x9f: v9f(0x1) = CONST 
    0xa1: va1(0xa0) = CONST 
    0xa3: va3(0x10000000000000000000000000000000000000000) = SHL va1(0xa0), v9f(0x1)
    0xa4: va4(0xffffffffffffffffffffffffffffffffffffffff) = SUB va3(0x10000000000000000000000000000000000000000), v9d(0x1)
    0xa5: va5(0x20) = CONST 
    0xa8: va8(0x24) = ADD v86(0x4), va5(0x20)
    0xa9: va9 = CALLDATALOAD va8(0x24)
    0xaa: vaa = AND va9, va4(0xffffffffffffffffffffffffffffffffffffffff)
    0xac: vac(0x40) = CONST 
    0xaf: vaf(0x44) = ADD v86(0x4), vac(0x40)
    0xb0: vb0 = CALLDATALOAD vaf(0x44)
    0xb2: vb2(0x60) = CONST 
    0xb5: vb5(0x64) = ADD v86(0x4), vb2(0x60)
    0xb6: vb6 = CALLDATALOAD vb5(0x64)
    0xb8: vb8(0x80) = CONST 
    0xba: vba(0x84) = ADD vb8(0x80), v86(0x4)
    0xbb: vbb = CALLDATALOAD vba(0x84)
    0xbc: vbc(0x1d2) = CONST 
    0xbf: JUMP vbc(0x1d2)

    Begin block 0x1d2
    prev=[0x98], succ=[0x21e, 0x222]
    =================================
    0x1d4: v1d4(0x0) = CONST 
    0x1d7: v1d7(0x1) = CONST 
    0x1da: v1da = SLOAD v1d4(0x0)
    0x1dc: v1dc(0x100) = CONST 
    0x1df: v1df(0x100) = EXP v1dc(0x100), v1d7(0x1)
    0x1e1: v1e1 = DIV v1da, v1df(0x100)
    0x1e2: v1e2(0x1) = CONST 
    0x1e4: v1e4(0x1) = CONST 
    0x1e6: v1e6(0xa0) = CONST 
    0x1e8: v1e8(0x10000000000000000000000000000000000000000) = SHL v1e6(0xa0), v1e4(0x1)
    0x1e9: v1e9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e8(0x10000000000000000000000000000000000000000), v1e2(0x1)
    0x1ea: v1ea = AND v1e9(0xffffffffffffffffffffffffffffffffffffffff), v1e1
    0x1eb: v1eb(0x1) = CONST 
    0x1ed: v1ed(0x1) = CONST 
    0x1ef: v1ef(0xa0) = CONST 
    0x1f1: v1f1(0x10000000000000000000000000000000000000000) = SHL v1ef(0xa0), v1ed(0x1)
    0x1f2: v1f2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f1(0x10000000000000000000000000000000000000000), v1eb(0x1)
    0x1f3: v1f3 = AND v1f2(0xffffffffffffffffffffffffffffffffffffffff), v1ea
    0x1f4: v1f4(0x287be3e4) = CONST 
    0x1f9: v1f9(0x40) = CONST 
    0x1fb: v1fb = MLOAD v1f9(0x40)
    0x1fd: v1fd(0xffffffff) = CONST 
    0x202: v202(0x287be3e4) = AND v1fd(0xffffffff), v1f4(0x287be3e4)
    0x203: v203(0xe0) = CONST 
    0x205: v205(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v203(0xe0), v202(0x287be3e4)
    0x207: MSTORE v1fb, v205(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x208: v208(0x4) = CONST 
    0x20a: v20a = ADD v208(0x4), v1fb
    0x20b: v20b(0x20) = CONST 
    0x20d: v20d(0x40) = CONST 
    0x20f: v20f = MLOAD v20d(0x40)
    0x212: v212(0x4) = SUB v20a, v20f
    0x216: v216 = EXTCODESIZE v1f3
    0x217: v217 = ISZERO v216
    0x219: v219 = ISZERO v217
    0x21a: v21a(0x222) = CONST 
    0x21d: JUMPI v21a(0x222), v219

    Begin block 0x21e
    prev=[0x1d2], succ=[]
    =================================
    0x21e: v21e(0x0) = CONST 
    0x221: REVERT v21e(0x0), v21e(0x0)

    Begin block 0x222
    prev=[0x1d2], succ=[0x22d, 0x236]
    =================================
    0x224: v224 = GAS 
    0x225: v225 = STATICCALL v224, v1f3, v20f, v212(0x4), v20f, v20b(0x20)
    0x226: v226 = ISZERO v225
    0x228: v228 = ISZERO v226
    0x229: v229(0x236) = CONST 
    0x22c: JUMPI v229(0x236), v228

    Begin block 0x22d
    prev=[0x222], succ=[]
    =================================
    0x22d: v22d = RETURNDATASIZE 
    0x22e: v22e(0x0) = CONST 
    0x231: RETURNDATACOPY v22e(0x0), v22e(0x0), v22d
    0x232: v232 = RETURNDATASIZE 
    0x233: v233(0x0) = CONST 
    0x235: REVERT v233(0x0), v232

    Begin block 0x236
    prev=[0x222], succ=[0x248, 0x24c]
    =================================
    0x23b: v23b(0x40) = CONST 
    0x23d: v23d = MLOAD v23b(0x40)
    0x23e: v23e = RETURNDATASIZE 
    0x23f: v23f(0x20) = CONST 
    0x242: v242 = LT v23e, v23f(0x20)
    0x243: v243 = ISZERO v242
    0x244: v244(0x24c) = CONST 
    0x247: JUMPI v244(0x24c), v243

    Begin block 0x248
    prev=[0x236], succ=[]
    =================================
    0x248: v248(0x0) = CONST 
    0x24b: REVERT v248(0x0), v248(0x0)

    Begin block 0x24c
    prev=[0x236], succ=[0x293, 0x297]
    =================================
    0x24e: v24e = MLOAD v23d
    0x24f: v24f(0x40) = CONST 
    0x252: v252 = MLOAD v24f(0x40)
    0x253: v253(0xd6a8b91) = CONST 
    0x258: v258(0xe2) = CONST 
    0x25a: v25a(0x35aa2e4400000000000000000000000000000000000000000000000000000000) = SHL v258(0xe2), v253(0xd6a8b91)
    0x25c: MSTORE v252, v25a(0x35aa2e4400000000000000000000000000000000000000000000000000000000)
    0x25d: v25d(0x4) = CONST 
    0x260: v260 = ADD v252, v25d(0x4)
    0x263: MSTORE v260, v9b
    0x265: v265 = MLOAD v24f(0x40)
    0x266: v266(0x1) = CONST 
    0x268: v268(0x1) = CONST 
    0x26a: v26a(0xa0) = CONST 
    0x26c: v26c(0x10000000000000000000000000000000000000000) = SHL v26a(0xa0), v268(0x1)
    0x26d: v26d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v26c(0x10000000000000000000000000000000000000000), v266(0x1)
    0x270: v270 = AND v24e, v26d(0xffffffffffffffffffffffffffffffffffffffff)
    0x272: v272(0x35aa2e44) = CONST 
    0x278: v278(0x24) = CONST 
    0x27c: v27c = ADD v252, v278(0x24)
    0x27e: v27e(0xe0) = CONST 
    0x286: v286(0x0) = SUB v252, v265
    0x287: v287(0x24) = ADD v286(0x0), v278(0x24)
    0x28b: v28b = EXTCODESIZE v270
    0x28c: v28c = ISZERO v28b
    0x28e: v28e = ISZERO v28c
    0x28f: v28f(0x297) = CONST 
    0x292: JUMPI v28f(0x297), v28e

    Begin block 0x293
    prev=[0x24c], succ=[]
    =================================
    0x293: v293(0x0) = CONST 
    0x296: REVERT v293(0x0), v293(0x0)

    Begin block 0x297
    prev=[0x24c], succ=[0x2a2, 0x2ab]
    =================================
    0x299: v299 = GAS 
    0x29a: v29a = STATICCALL v299, v270, v265, v287(0x24), v265, v27e(0xe0)
    0x29b: v29b = ISZERO v29a
    0x29d: v29d = ISZERO v29b
    0x29e: v29e(0x2ab) = CONST 
    0x2a1: JUMPI v29e(0x2ab), v29d

    Begin block 0x2a2
    prev=[0x297], succ=[]
    =================================
    0x2a2: v2a2 = RETURNDATASIZE 
    0x2a3: v2a3(0x0) = CONST 
    0x2a6: RETURNDATACOPY v2a3(0x0), v2a3(0x0), v2a2
    0x2a7: v2a7 = RETURNDATASIZE 
    0x2a8: v2a8(0x0) = CONST 
    0x2aa: REVERT v2a8(0x0), v2a7

    Begin block 0x2ab
    prev=[0x297], succ=[0x2bd, 0x2c1]
    =================================
    0x2b0: v2b0(0x40) = CONST 
    0x2b2: v2b2 = MLOAD v2b0(0x40)
    0x2b3: v2b3 = RETURNDATASIZE 
    0x2b4: v2b4(0xe0) = CONST 
    0x2b7: v2b7 = LT v2b3, v2b4(0xe0)
    0x2b8: v2b8 = ISZERO v2b7
    0x2b9: v2b9(0x2c1) = CONST 
    0x2bc: JUMPI v2b9(0x2c1), v2b8

    Begin block 0x2bd
    prev=[0x2ab], succ=[]
    =================================
    0x2bd: v2bd(0x0) = CONST 
    0x2c0: REVERT v2bd(0x0), v2bd(0x0)

    Begin block 0x2c1
    prev=[0x2ab], succ=[0x2d9, 0x315]
    =================================
    0x2c3: v2c3(0xc0) = CONST 
    0x2c5: v2c5 = ADD v2c3(0xc0), v2b2
    0x2c6: v2c6 = MLOAD v2c5
    0x2c9: v2c9(0x1) = CONST 
    0x2cb: v2cb(0x1) = CONST 
    0x2cd: v2cd(0xa0) = CONST 
    0x2cf: v2cf(0x10000000000000000000000000000000000000000) = SHL v2cd(0xa0), v2cb(0x1)
    0x2d0: v2d0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2cf(0x10000000000000000000000000000000000000000), v2c9(0x1)
    0x2d2: v2d2 = AND v2c6, v2d0(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d3: v2d3 = CALLER 
    0x2d4: v2d4 = EQ v2d3, v2d2
    0x2d5: v2d5(0x315) = CONST 
    0x2d8: JUMPI v2d5(0x315), v2d4

    Begin block 0x2d9
    prev=[0x2c1], succ=[]
    =================================
    0x2d9: v2d9(0x40) = CONST 
    0x2dc: v2dc = MLOAD v2d9(0x40)
    0x2dd: v2dd(0x461bcd) = CONST 
    0x2e1: v2e1(0xe5) = CONST 
    0x2e3: v2e3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2e1(0xe5), v2dd(0x461bcd)
    0x2e5: MSTORE v2dc, v2e3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2e6: v2e6(0x20) = CONST 
    0x2e8: v2e8(0x4) = CONST 
    0x2eb: v2eb = ADD v2dc, v2e8(0x4)
    0x2ec: MSTORE v2eb, v2e6(0x20)
    0x2ed: v2ed(0xd) = CONST 
    0x2ef: v2ef(0x24) = CONST 
    0x2f2: v2f2 = ADD v2dc, v2ef(0x24)
    0x2f3: MSTORE v2f2, v2ed(0xd)
    0x2f4: v2f4(0x3737ba103b30b634b230ba37b9) = CONST 
    0x302: v302(0x99) = CONST 
    0x304: v304(0x6e6f742076616c696461746f7200000000000000000000000000000000000000) = SHL v302(0x99), v2f4(0x3737ba103b30b634b230ba37b9)
    0x305: v305(0x44) = CONST 
    0x308: v308 = ADD v2dc, v305(0x44)
    0x309: MSTORE v308, v304(0x6e6f742076616c696461746f7200000000000000000000000000000000000000)
    0x30b: v30b = MLOAD v2d9(0x40)
    0x30f: v30f(0x0) = SUB v2dc, v30b
    0x310: v310(0x64) = CONST 
    0x312: v312(0x64) = ADD v310(0x64), v30f(0x0)
    0x314: REVERT v30b, v312(0x64)

    Begin block 0x315
    prev=[0x2c1], succ=[0x9ce]
    =================================
    0x318: v318(0x1) = CONST 
    0x31a: v31a(0x1) = CONST 
    0x31c: v31c(0xa0) = CONST 
    0x31e: v31e(0x10000000000000000000000000000000000000000) = SHL v31c(0xa0), v31a(0x1)
    0x31f: v31f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v31e(0x10000000000000000000000000000000000000000), v318(0x1)
    0x320: v320 = AND v31f(0xffffffffffffffffffffffffffffffffffffffff), vaa
    0x322: v322(0x502f5a6697a92e602c626b931a4a771fef4360eb9cece7bf906f10c5cec96aaa) = CONST 
    0x345: v345(0x40) = CONST 
    0x347: v347 = MLOAD v345(0x40)
    0x34b: MSTORE v347, vb6
    0x34c: v34c(0x20) = CONST 
    0x34e: v34e = ADD v34c(0x20), v347
    0x351: MSTORE v34e, vbb
    0x352: v352(0x20) = CONST 
    0x354: v354 = ADD v352(0x20), v34e
    0x359: v359(0x40) = CONST 
    0x35b: v35b = MLOAD v359(0x40)
    0x35e: v35e(0x40) = SUB v354, v35b
    0x360: LOG4 v35b, v35e(0x40), v322(0x502f5a6697a92e602c626b931a4a771fef4360eb9cece7bf906f10c5cec96aaa), v9b, v320, vb0
    0x368: JUMP v83(0x9ce)

    Begin block 0x9ce
    prev=[0x315], succ=[]
    =================================
    0x9cf: STOP 

}

function fallback()() public {
    Begin block 0x986
    prev=[], succ=[]
    =================================
    0x987: v987(0x0) = CONST 
    0x98a: REVERT v987(0x0), v987(0x0)

}

function logDelegatorUnstakedWithId(uint256,address,uint256,uint256)() public {
    Begin block 0xc2
    prev=[], succ=[0xd4, 0xd8]
    =================================
    0xc3: vc3(0x9ef) = CONST 
    0xc6: vc6(0x4) = CONST 
    0xc9: vc9 = CALLDATASIZE 
    0xca: vca = SUB vc9, vc6(0x4)
    0xcb: vcb(0x80) = CONST 
    0xce: vce = LT vca, vcb(0x80)
    0xcf: vcf = ISZERO vce
    0xd0: vd0(0xd8) = CONST 
    0xd3: JUMPI vd0(0xd8), vcf

    Begin block 0xd4
    prev=[0xc2], succ=[]
    =================================
    0xd4: vd4(0x0) = CONST 
    0xd7: REVERT vd4(0x0), vd4(0x0)

    Begin block 0xd8
    prev=[0xc2], succ=[0x369]
    =================================
    0xdb: vdb = CALLDATALOAD vc6(0x4)
    0xdd: vdd(0x1) = CONST 
    0xdf: vdf(0x1) = CONST 
    0xe1: ve1(0xa0) = CONST 
    0xe3: ve3(0x10000000000000000000000000000000000000000) = SHL ve1(0xa0), vdf(0x1)
    0xe4: ve4(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve3(0x10000000000000000000000000000000000000000), vdd(0x1)
    0xe5: ve5(0x20) = CONST 
    0xe8: ve8(0x24) = ADD vc6(0x4), ve5(0x20)
    0xe9: ve9 = CALLDATALOAD ve8(0x24)
    0xea: vea = AND ve9, ve4(0xffffffffffffffffffffffffffffffffffffffff)
    0xec: vec(0x40) = CONST 
    0xef: vef(0x44) = ADD vc6(0x4), vec(0x40)
    0xf0: vf0 = CALLDATALOAD vef(0x44)
    0xf2: vf2(0x60) = CONST 
    0xf4: vf4(0x64) = ADD vf2(0x60), vc6(0x4)
    0xf5: vf5 = CALLDATALOAD vf4(0x64)
    0xf6: vf6(0x369) = CONST 
    0xf9: JUMP vf6(0x369)

    Begin block 0x369
    prev=[0xd8], succ=[0x3b5, 0x3b9]
    =================================
    0x36b: v36b(0x0) = CONST 
    0x36e: v36e(0x1) = CONST 
    0x371: v371 = SLOAD v36b(0x0)
    0x373: v373(0x100) = CONST 
    0x376: v376(0x100) = EXP v373(0x100), v36e(0x1)
    0x378: v378 = DIV v371, v376(0x100)
    0x379: v379(0x1) = CONST 
    0x37b: v37b(0x1) = CONST 
    0x37d: v37d(0xa0) = CONST 
    0x37f: v37f(0x10000000000000000000000000000000000000000) = SHL v37d(0xa0), v37b(0x1)
    0x380: v380(0xffffffffffffffffffffffffffffffffffffffff) = SUB v37f(0x10000000000000000000000000000000000000000), v379(0x1)
    0x381: v381 = AND v380(0xffffffffffffffffffffffffffffffffffffffff), v378
    0x382: v382(0x1) = CONST 
    0x384: v384(0x1) = CONST 
    0x386: v386(0xa0) = CONST 
    0x388: v388(0x10000000000000000000000000000000000000000) = SHL v386(0xa0), v384(0x1)
    0x389: v389(0xffffffffffffffffffffffffffffffffffffffff) = SUB v388(0x10000000000000000000000000000000000000000), v382(0x1)
    0x38a: v38a = AND v389(0xffffffffffffffffffffffffffffffffffffffff), v381
    0x38b: v38b(0x287be3e4) = CONST 
    0x390: v390(0x40) = CONST 
    0x392: v392 = MLOAD v390(0x40)
    0x394: v394(0xffffffff) = CONST 
    0x399: v399(0x287be3e4) = AND v394(0xffffffff), v38b(0x287be3e4)
    0x39a: v39a(0xe0) = CONST 
    0x39c: v39c(0x287be3e400000000000000000000000000000000000000000000000000000000) = SHL v39a(0xe0), v399(0x287be3e4)
    0x39e: MSTORE v392, v39c(0x287be3e400000000000000000000000000000000000000000000000000000000)
    0x39f: v39f(0x4) = CONST 
    0x3a1: v3a1 = ADD v39f(0x4), v392
    0x3a2: v3a2(0x20) = CONST 
    0x3a4: v3a4(0x40) = CONST 
    0x3a6: v3a6 = MLOAD v3a4(0x40)
    0x3a9: v3a9(0x4) = SUB v3a1, v3a6
    0x3ad: v3ad = EXTCODESIZE v38a
    0x3ae: v3ae = ISZERO v3ad
    0x3b0: v3b0 = ISZERO v3ae
    0x3b1: v3b1(0x3b9) = CONST 
    0x3b4: JUMPI v3b1(0x3b9), v3b0

    Begin block 0x3b5
    prev=[0x369], succ=[]
    =================================
    0x3b5: v3b5(0x0) = CONST 
    0x3b8: REVERT v3b5(0x0), v3b5(0x0)

    Begin block 0x3b9
    prev=[0x369], succ=[0x3c4, 0x3cd]
    =================================
    0x3bb: v3bb = GAS 
    0x3bc: v3bc = STATICCALL v3bb, v38a, v3a6, v3a9(0x4), v3a6, v3a2(0x20)
    0x3bd: v3bd = ISZERO v3bc
    0x3bf: v3bf = ISZERO v3bd
    0x3c0: v3c0(0x3cd) = CONST 
    0x3c3: JUMPI v3c0(0x3cd), v3bf

    Begin block 0x3c4
    prev=[0x3b9], succ=[]
    =================================
    0x3c4: v3c4 = RETURNDATASIZE 
    0x3c5: v3c5(0x0) = CONST 
    0x3c8: RETURNDATACOPY v3c5(0x0), v3c5(0x0), v3c4
    0x3c9: v3c9 = RETURNDATASIZE 
    0x3ca: v3ca(0x0) = CONST 
    0x3cc: REVERT v3ca(0x0), v3c9

    Begin block 0x3cd
    prev=[0x3b9], succ=[0x3df, 0x3e3]
    =================================
    0x3d2: v3d2(0x40) = CONST 
    0x3d4: v3d4 = MLOAD v3d2(0x40)
    0x3d5: v3d5 = RETURNDATASIZE 
    0x3d6: v3d6(0x20) = CONST 
    0x3d9: v3d9 = LT v3d5, v3d6(0x20)
    0x3da: v3da = ISZERO v3d9
    0x3db: v3db(0x3e3) = CONST 
    0x3de: JUMPI v3db(0x3e3), v3da

    Begin block 0x3df
    prev=[0x3cd], succ=[]
    =================================
    0x3df: v3df(0x0) = CONST 
    0x3e2: REVERT v3df(0x0), v3df(0x0)

    Begin block 0x3e3
    prev=[0x3cd], succ=[0x42a, 0x42e]
    =================================
    0x3e5: v3e5 = MLOAD v3d4
    0x3e6: v3e6(0x40) = CONST 
    0x3e9: v3e9 = MLOAD v3e6(0x40)
    0x3ea: v3ea(0xd6a8b91) = CONST 
    0x3ef: v3ef(0xe2) = CONST 
    0x3f1: v3f1(0x35aa2e4400000000000000000000000000000000000000000000000000000000) = SHL v3ef(0xe2), v3ea(0xd6a8b91)
    0x3f3: MSTORE v3e9, v3f1(0x35aa2e4400000000000000000000000000000000000000000000000000000000)
    0x3f4: v3f4(0x4) = CONST 
    0x3f7: v3f7 = ADD v3e9, v3f4(0x4)
    0x3fa: MSTORE v3f7, vdb
    0x3fc: v3fc = MLOAD v3e6(0x40)
    0x3fd: v3fd(0x1) = CONST 
    0x3ff: v3ff(0x1) = CONST 
    0x401: v401(0xa0) = CONST 
    0x403: v403(0x10000000000000000000000000000000000000000) = SHL v401(0xa0), v3ff(0x1)
    0x404: v404(0xffffffffffffffffffffffffffffffffffffffff) = SUB v403(0x10000000000000000000000000000000000000000), v3fd(0x1)
    0x407: v407 = AND v3e5, v404(0xffffffffffffffffffffffffffffffffffffffff)
    0x409: v409(0x35aa2e44) = CONST 
    0x40f: v40f(0x24) = CONST 
    0x413: v413 = ADD v3e9, v40f(0x24)
    0x415: v415(0xe0) = CONST 
    0x41d: v41d(0x0) = SUB v3e9, v3fc
    0x41e: v41e(0x24) = ADD v41d(0x0), v40f(0x24)
    0x422: v422 = EXTCODESIZE v407
    0x423: v423 = ISZERO v422
    0x425: v425 = ISZERO v423
    0x426: v426(0x42e) = CONST 
    0x429: JUMPI v426(0x42e), v425

    Begin block 0x42a
    prev=[0x3e3], succ=[]
    =================================
    0x42a: v42a(0x0) = CONST 
    0x42d: REVERT v42a(0x0), v42a(0x0)

    Begin block 0x42e
    prev=[0x3e3], succ=[0x439, 0x442]
    =================================
    0x430: v430 = GAS 
    0x431: v431 = STATICCALL v430, v407, v3fc, v41e(0x24), v3fc, v415(0xe0)
    0x432: v432 = ISZERO v431
    0x434: v434 = ISZERO v432
    0x435: v435(0x442) = CONST 
    0x438: JUMPI v435(0x442), v434

    Begin block 0x439
    prev=[0x42e], succ=[]
    =================================
    0x439: v439 = RETURNDATASIZE 
    0x43a: v43a(0x0) = CONST 
    0x43d: RETURNDATACOPY v43a(0x0), v43a(0x0), v439
    0x43e: v43e = RETURNDATASIZE 
    0x43f: v43f(0x0) = CONST 
    0x441: REVERT v43f(0x0), v43e

    Begin block 0x442
    prev=[0x42e], succ=[0x454, 0x458]
    =================================
    0x447: v447(0x40) = CONST 
    0x449: v449 = MLOAD v447(0x40)
    0x44a: v44a = RETURNDATASIZE 
    0x44b: v44b(0xe0) = CONST 
    0x44e: v44e = LT v44a, v44b(0xe0)
    0x44f: v44f = ISZERO v44e
    0x450: v450(0x458) = CONST 
    0x453: JUMPI v450(0x458), v44f

    Begin block 0x454
    prev=[0x442], succ=[]
    =================================
    0x454: v454(0x0) = CONST 
    0x457: REVERT v454(0x0), v454(0x0)

    Begin block 0x458
    prev=[0x442], succ=[0x470, 0x4ac]
    =================================
    0x45a: v45a(0xc0) = CONST 
    0x45c: v45c = ADD v45a(0xc0), v449
    0x45d: v45d = MLOAD v45c
    0x460: v460(0x1) = CONST 
    0x462: v462(0x1) = CONST 
    0x464: v464(0xa0) = CONST 
    0x466: v466(0x10000000000000000000000000000000000000000) = SHL v464(0xa0), v462(0x1)
    0x467: v467(0xffffffffffffffffffffffffffffffffffffffff) = SUB v466(0x10000000000000000000000000000000000000000), v460(0x1)
    0x469: v469 = AND v45d, v467(0xffffffffffffffffffffffffffffffffffffffff)
    0x46a: v46a = CALLER 
    0x46b: v46b = EQ v46a, v469
    0x46c: v46c(0x4ac) = CONST 
    0x46f: JUMPI v46c(0x4ac), v46b

    Begin block 0x470
    prev=[0x458], succ=[]
    =================================
    0x470: v470(0x40) = CONST 
    0x473: v473 = MLOAD v470(0x40)
    0x474: v474(0x461bcd) = CONST 
    0x478: v478(0xe5) = CONST 
    0x47a: v47a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v478(0xe5), v474(0x461bcd)
    0x47c: MSTORE v473, v47a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x47d: v47d(0x20) = CONST 
    0x47f: v47f(0x4) = CONST 
    0x482: v482 = ADD v473, v47f(0x4)
    0x483: MSTORE v482, v47d(0x20)
    0x484: v484(0xd) = CONST 
    0x486: v486(0x24) = CONST 
    0x489: v489 = ADD v473, v486(0x24)
    0x48a: MSTORE v489, v484(0xd)
    0x48b: v48b(0x3737ba103b30b634b230ba37b9) = CONST 
    0x499: v499(0x99) = CONST 
    0x49b: v49b(0x6e6f742076616c696461746f7200000000000000000000000000000000000000) = SHL v499(0x99), v48b(0x3737ba103b30b634b230ba37b9)
    0x49c: v49c(0x44) = CONST 
    0x49f: v49f = ADD v473, v49c(0x44)
    0x4a0: MSTORE v49f, v49b(0x6e6f742076616c696461746f7200000000000000000000000000000000000000)
    0x4a2: v4a2 = MLOAD v470(0x40)
    0x4a6: v4a6(0x0) = SUB v473, v4a2
    0x4a7: v4a7(0x64) = CONST 
    0x4a9: v4a9(0x64) = ADD v4a7(0x64), v4a6(0x0)
    0x4ab: REVERT v4a2, v4a9(0x64)

    Begin block 0x4ac
    prev=[0x458], succ=[0x9ef]
    =================================
    0x4ae: v4ae(0x1) = CONST 
    0x4b0: v4b0(0x1) = CONST 
    0x4b2: v4b2(0xa0) = CONST 
    0x4b4: v4b4(0x10000000000000000000000000000000000000000) = SHL v4b2(0xa0), v4b0(0x1)
    0x4b5: v4b5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4b4(0x10000000000000000000000000000000000000000), v4ae(0x1)
    0x4b6: v4b6 = AND v4b5(0xffffffffffffffffffffffffffffffffffffffff), vea
    0x4b8: v4b8(0x7beb9bef91040fcf7607c78d4fc668370a9036788d7e6f202a4a2db5b0c28c80) = CONST 
    0x4db: v4db(0x40) = CONST 
    0x4dd: v4dd = MLOAD v4db(0x40)
    0x4e1: MSTORE v4dd, vf0
    0x4e2: v4e2(0x20) = CONST 
    0x4e4: v4e4 = ADD v4e2(0x20), v4dd
    0x4e7: MSTORE v4e4, vf5
    0x4e8: v4e8(0x20) = CONST 
    0x4ea: v4ea = ADD v4e8(0x20), v4e4
    0x4ef: v4ef(0x40) = CONST 
    0x4f1: v4f1 = MLOAD v4ef(0x40)
    0x4f4: v4f4(0x40) = SUB v4ea, v4f1
    0x4f6: LOG3 v4f1, v4f4(0x40), v4b8(0x7beb9bef91040fcf7607c78d4fc668370a9036788d7e6f202a4a2db5b0c28c80), vdb, v4b6
    0x4fd: JUMP vc3(0x9ef)

    Begin block 0x9ef
    prev=[0x4ac], succ=[]
    =================================
    0x9f0: STOP 

}

function registry()() public {
    Begin block 0xfa
    prev=[], succ=[0x4fe]
    =================================
    0xfb: vfb(0x102) = CONST 
    0xfe: vfe(0x4fe) = CONST 
    0x101: JUMP vfe(0x4fe)

    Begin block 0x4fe
    prev=[0xfa], succ=[0x102]
    =================================
    0x4ff: v4ff(0x0) = CONST 
    0x501: v501 = SLOAD v4ff(0x0)
    0x502: v502(0x100) = CONST 
    0x506: v506 = DIV v501, v502(0x100)
    0x507: v507(0x1) = CONST 
    0x509: v509(0x1) = CONST 
    0x50b: v50b(0xa0) = CONST 
    0x50d: v50d(0x10000000000000000000000000000000000000000) = SHL v50b(0xa0), v509(0x1)
    0x50e: v50e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v50d(0x10000000000000000000000000000000000000000), v507(0x1)
    0x50f: v50f = AND v50e(0xffffffffffffffffffffffffffffffffffffffff), v506
    0x511: JUMP vfb(0x102)

    Begin block 0x102
    prev=[0x4fe], succ=[]
    =================================
    0x103: v103(0x40) = CONST 
    0x106: v106 = MLOAD v103(0x40)
    0x107: v107(0x1) = CONST 
    0x109: v109(0x1) = CONST 
    0x10b: v10b(0xa0) = CONST 
    0x10d: v10d(0x10000000000000000000000000000000000000000) = SHL v10b(0xa0), v109(0x1)
    0x10e: v10e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10d(0x10000000000000000000000000000000000000000), v107(0x1)
    0x111: v111 = AND v50f, v10e(0xffffffffffffffffffffffffffffffffffffffff)
    0x113: MSTORE v106, v111
    0x114: v114 = MLOAD v103(0x40)
    0x118: v118(0x0) = SUB v106, v114
    0x119: v119(0x20) = CONST 
    0x11b: v11b(0x20) = ADD v119(0x20), v118(0x0)
    0x11d: RETURN v114, v11b(0x20)

}

