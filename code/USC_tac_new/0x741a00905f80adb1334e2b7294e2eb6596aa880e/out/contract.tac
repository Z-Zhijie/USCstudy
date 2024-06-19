function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xcce]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xcb2: vcb2(0xcce) = CONST 
    0xcb3: JUMPI vcb2(0xcce), v8

    Begin block 0xd
    prev=[0x0], succ=[0x7f, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x64a7ce99) = CONST 
    0x19: v19 = GT v14(0x64a7ce99), v12
    0x1a: v1a(0x7f) = CONST 
    0x1d: JUMPI v1a(0x7f), v19

    Begin block 0x7f
    prev=[0xd], succ=[0xcd1, 0x8b]
    =================================
    0x81: v81(0x5f63c8a) = CONST 
    0x86: v86 = EQ v81(0x5f63c8a), v12
    0xcc2: vcc2(0xcd1) = CONST 
    0xcc3: JUMPI vcc2(0xcd1), v86

    Begin block 0xcd1
    prev=[0x7f], succ=[]
    =================================
    0xcd2: vcd2(0xcc) = CONST 
    0xcd3: CALLPRIVATE vcd2(0xcc)

    Begin block 0x8b
    prev=[0x7f], succ=[0xcd4, 0x96]
    =================================
    0x8c: v8c(0x34140748) = CONST 
    0x91: v91 = EQ v8c(0x34140748), v12
    0xcc4: vcc4(0xcd4) = CONST 
    0xcc5: JUMPI vcc4(0xcd4), v91

    Begin block 0xcd4
    prev=[0x8b], succ=[]
    =================================
    0xcd5: vcd5(0x112) = CONST 
    0xcd6: CALLPRIVATE vcd5(0x112)

    Begin block 0x96
    prev=[0x8b], succ=[0xcd7, 0xa1]
    =================================
    0x97: v97(0x4555d5c9) = CONST 
    0x9c: v9c = EQ v97(0x4555d5c9), v12
    0xcc6: vcc6(0xcd7) = CONST 
    0xcc7: JUMPI vcc6(0xcd7), v9c

    Begin block 0xcd7
    prev=[0x96], succ=[]
    =================================
    0xcd8: vcd8(0x145) = CONST 
    0xcd9: CALLPRIVATE vcd8(0x145)

    Begin block 0xa1
    prev=[0x96], succ=[0xcda, 0xac]
    =================================
    0xa2: va2(0x5c60da1b) = CONST 
    0xa7: va7 = EQ va2(0x5c60da1b), v12
    0xcc8: vcc8(0xcda) = CONST 
    0xcc9: JUMPI vcc8(0xcda), va7

    Begin block 0xcda
    prev=[0xa1], succ=[]
    =================================
    0xcdb: vcdb(0x16c) = CONST 
    0xcdc: CALLPRIVATE vcdb(0x16c)

    Begin block 0xac
    prev=[0xa1], succ=[0xcdd, 0xb7]
    =================================
    0xad: vad(0x608fa3c1) = CONST 
    0xb2: vb2 = EQ vad(0x608fa3c1), v12
    0xcca: vcca(0xcdd) = CONST 
    0xccb: JUMPI vcca(0xcdd), vb2

    Begin block 0xcdd
    prev=[0xac], succ=[]
    =================================
    0xcde: vcde(0x181) = CONST 
    0xcdf: CALLPRIVATE vcde(0x181)

    Begin block 0xb7
    prev=[0xac], succ=[0xcce, 0xce0]
    =================================
    0xb8: vb8(0x638c7e17) = CONST 
    0xbd: vbd = EQ vb8(0x638c7e17), v12
    0xccc: vccc(0xce0) = CONST 
    0xccd: JUMPI vccc(0xce0), vbd

    Begin block 0xcce
    prev=[0x0, 0xb7], succ=[]
    =================================
    0xccf: vccf(0xc2) = CONST 
    0xcd0: CALLPRIVATE vccf(0xc2)

    Begin block 0xce0
    prev=[0xb7], succ=[]
    =================================
    0xce1: vce1(0x1dc) = CONST 
    0xce2: CALLPRIVATE vce1(0x1dc)

    Begin block 0x1e
    prev=[0xd], succ=[0x59, 0x29]
    =================================
    0x1f: v1f(0x8f32d59b) = CONST 
    0x24: v24 = GT v1f(0x8f32d59b), v12
    0x25: v25(0x59) = CONST 
    0x28: JUMPI v25(0x59), v24

    Begin block 0x59
    prev=[0x1e], succ=[0xce3, 0x65]
    =================================
    0x5b: v5b(0x64a7ce99) = CONST 
    0x60: v60 = EQ v5b(0x64a7ce99), v12
    0xcbc: vcbc(0xce3) = CONST 
    0xcbd: JUMPI vcbc(0xce3), v60

    Begin block 0xce3
    prev=[0x59], succ=[]
    =================================
    0xce4: vce4(0x1f1) = CONST 
    0xce5: CALLPRIVATE vce4(0x1f1)

    Begin block 0x65
    prev=[0x59], succ=[0xce6, 0x70]
    =================================
    0x66: v66(0x715018a6) = CONST 
    0x6b: v6b = EQ v66(0x715018a6), v12
    0xcbe: vcbe(0xce6) = CONST 
    0xcbf: JUMPI vcbe(0xce6), v6b

    Begin block 0xce6
    prev=[0x65], succ=[]
    =================================
    0xce7: vce7(0x206) = CONST 
    0xce8: CALLPRIVATE vce7(0x206)

    Begin block 0x70
    prev=[0x65], succ=[0x7b, 0xce9]
    =================================
    0x71: v71(0x8da5cb5b) = CONST 
    0x76: v76 = EQ v71(0x8da5cb5b), v12
    0xcc0: vcc0(0xce9) = CONST 
    0xcc1: JUMPI vcc0(0xce9), v76

    Begin block 0x7b
    prev=[0x70], succ=[]
    =================================
    0x7b: v7b(0xc2) = CONST 
    0x7e: JUMP v7b(0xc2)

    Begin block 0xce9
    prev=[0x70], succ=[]
    =================================
    0xcea: vcea(0x21b) = CONST 
    0xceb: CALLPRIVATE vcea(0x21b)

    Begin block 0x29
    prev=[0x1e], succ=[0xcec, 0x34]
    =================================
    0x2a: v2a(0x8f32d59b) = CONST 
    0x2f: v2f = EQ v2a(0x8f32d59b), v12
    0xcb4: vcb4(0xcec) = CONST 
    0xcb5: JUMPI vcb4(0xcec), v2f

    Begin block 0xcec
    prev=[0x29], succ=[]
    =================================
    0xced: vced(0x230) = CONST 
    0xcee: CALLPRIVATE vced(0x230)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xcef]
    =================================
    0x35: v35(0xe7a1c1c0) = CONST 
    0x3a: v3a = EQ v35(0xe7a1c1c0), v12
    0xcb6: vcb6(0xcef) = CONST 
    0xcb7: JUMPI vcb6(0xcef), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xcf2, 0x4a]
    =================================
    0x40: v40(0xf2fde38b) = CONST 
    0x45: v45 = EQ v40(0xf2fde38b), v12
    0xcb8: vcb8(0xcf2) = CONST 
    0xcb9: JUMPI vcb8(0xcf2), v45

    Begin block 0xcf2
    prev=[0x3f], succ=[]
    =================================
    0xcf3: vcf3(0x292) = CONST 
    0xcf4: CALLPRIVATE vcf3(0x292)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0xcf5]
    =================================
    0x4b: v4b(0xf4954387) = CONST 
    0x50: v50 = EQ v4b(0xf4954387), v12
    0xcba: vcba(0xcf5) = CONST 
    0xcbb: JUMPI vcba(0xcf5), v50

    Begin block 0x55
    prev=[0x4a], succ=[]
    =================================
    0x55: v55(0xc2) = CONST 
    0x58: JUMP v55(0xc2)

    Begin block 0xcf5
    prev=[0x4a], succ=[]
    =================================
    0xcf6: vcf6(0x2c5) = CONST 
    0xcf7: CALLPRIVATE vcf6(0x2c5)

    Begin block 0xcef
    prev=[0x34], succ=[]
    =================================
    0xcf0: vcf0(0x259) = CONST 
    0xcf1: CALLPRIVATE vcf0(0x259)

}

function _upgradeTo(address)() public {
    Begin block 0x112
    prev=[], succ=[0x11a, 0x11e]
    =================================
    0x113: v113 = CALLVALUE 
    0x115: v115 = ISZERO v113
    0x116: v116(0x11e) = CONST 
    0x119: JUMPI v116(0x11e), v115

    Begin block 0x11a
    prev=[0x112], succ=[]
    =================================
    0x11a: v11a(0x0) = CONST 
    0x11d: REVERT v11a(0x0), v11a(0x0)

    Begin block 0x11e
    prev=[0x112], succ=[0x131, 0x135]
    =================================
    0x120: v120(0xab6) = CONST 
    0x123: v123(0x4) = CONST 
    0x126: v126 = CALLDATASIZE 
    0x127: v127 = SUB v126, v123(0x4)
    0x128: v128(0x20) = CONST 
    0x12b: v12b = LT v127, v128(0x20)
    0x12c: v12c = ISZERO v12b
    0x12d: v12d(0x135) = CONST 
    0x130: JUMPI v12d(0x135), v12c

    Begin block 0x131
    prev=[0x11e], succ=[]
    =================================
    0x131: v131(0x0) = CONST 
    0x134: REVERT v131(0x0), v131(0x0)

    Begin block 0x135
    prev=[0x11e], succ=[0x326]
    =================================
    0x137: v137 = CALLDATALOAD v123(0x4)
    0x138: v138(0x1) = CONST 
    0x13a: v13a(0x1) = CONST 
    0x13c: v13c(0xa0) = CONST 
    0x13e: v13e(0x10000000000000000000000000000000000000000) = SHL v13c(0xa0), v13a(0x1)
    0x13f: v13f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13e(0x10000000000000000000000000000000000000000), v138(0x1)
    0x140: v140 = AND v13f(0xffffffffffffffffffffffffffffffffffffffff), v137
    0x141: v141(0x326) = CONST 
    0x144: JUMP v141(0x326)

    Begin block 0x326
    prev=[0x135], succ=[0x362, 0x398]
    =================================
    0x327: v327(0x0) = CONST 
    0x32b: MSTORE v327(0x0), v327(0x0)
    0x32c: v32c(0x1) = CONST 
    0x32e: v32e(0x20) = CONST 
    0x330: MSTORE v32e(0x20), v32c(0x1)
    0x331: v331(0xa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49) = CONST 
    0x352: v352 = SLOAD v331(0xa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49)
    0x353: v353(0x1) = CONST 
    0x355: v355(0x1) = CONST 
    0x357: v357(0xa0) = CONST 
    0x359: v359(0x10000000000000000000000000000000000000000) = SHL v357(0xa0), v355(0x1)
    0x35a: v35a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v359(0x10000000000000000000000000000000000000000), v353(0x1)
    0x35b: v35b = AND v35a(0xffffffffffffffffffffffffffffffffffffffff), v352
    0x35c: v35c = CALLER 
    0x35d: v35d = EQ v35c, v35b
    0x35e: v35e(0x398) = CONST 
    0x361: JUMPI v35e(0x398), v35d

    Begin block 0x362
    prev=[0x326], succ=[]
    =================================
    0x362: v362(0x40) = CONST 
    0x364: v364 = MLOAD v362(0x40)
    0x365: v365(0x461bcd) = CONST 
    0x369: v369(0xe5) = CONST 
    0x36b: v36b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v369(0xe5), v365(0x461bcd)
    0x36d: MSTORE v364, v36b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x36e: v36e(0x4) = CONST 
    0x370: v370 = ADD v36e(0x4), v364
    0x373: v373(0x20) = CONST 
    0x375: v375 = ADD v373(0x20), v370
    0x378: v378(0x20) = SUB v375, v370
    0x37a: MSTORE v370, v378(0x20)
    0x37b: v37b(0x2d) = CONST 
    0x37e: MSTORE v375, v37b(0x2d)
    0x37f: v37f(0x20) = CONST 
    0x381: v381 = ADD v37f(0x20), v375
    0x383: v383(0x9da) = CONST 
    0x386: v386(0x2d) = CONST 
    0x389: CODECOPY v381, v383(0x9da), v386(0x2d)
    0x38a: v38a(0x40) = CONST 
    0x38c: v38c = ADD v38a(0x40), v381
    0x390: v390(0x40) = CONST 
    0x392: v392 = MLOAD v390(0x40)
    0x395: v395(0x84) = SUB v38c, v392
    0x397: REVERT v392, v395(0x84)

    Begin block 0x398
    prev=[0x326], succ=[0x672B0x398]
    =================================
    0x399: v399(0x3a0) = CONST 
    0x39c: v39c(0x672) = CONST 
    0x39f: JUMP v39c(0x672), v399(0x3a0)

    Begin block 0x672B0x398
    prev=[0x398], succ=[0x421B0x672B0x398]
    =================================
    0x673S0x398: v673V398(0x0) = CONST 
    0x675S0x398: v675V398 = CALLVALUE 
    0x678S0x398: v678V398(0x0) = CONST 
    0x67aS0x398: v67aV398 = CALLER 
    0x67bS0x398: v67bV398 = ADDRESS 
    0x67dS0x398: v67dV398(0x0) = CONST 
    0x67fS0x398: v67fV398 = CALLDATASIZE 
    0x680S0x398: v680V398(0x40) = CONST 
    0x682S0x398: v682V398 = MLOAD v680V398(0x40)
    0x683S0x398: v683V398(0x20) = CONST 
    0x685S0x398: v685V398 = ADD v683V398(0x20), v682V398
    0x688S0x398: v688V398(0x1) = CONST 
    0x68aS0x398: v68aV398(0x1) = CONST 
    0x68cS0x398: v68cV398(0xa0) = CONST 
    0x68eS0x398: v68eV398(0x10000000000000000000000000000000000000000) = SHL v68cV398(0xa0), v68aV398(0x1)
    0x68fS0x398: v68fV398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v68eV398(0x10000000000000000000000000000000000000000), v688V398(0x1)
    0x690S0x398: v690V398 = AND v68fV398(0xffffffffffffffffffffffffffffffffffffffff), v67aV398
    0x691S0x398: v691V398(0x1) = CONST 
    0x693S0x398: v693V398(0x1) = CONST 
    0x695S0x398: v695V398(0xa0) = CONST 
    0x697S0x398: v697V398(0x10000000000000000000000000000000000000000) = SHL v695V398(0xa0), v693V398(0x1)
    0x698S0x398: v698V398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v697V398(0x10000000000000000000000000000000000000000), v691V398(0x1)
    0x699S0x398: v699V398 = AND v698V398(0xffffffffffffffffffffffffffffffffffffffff), v690V398
    0x69aS0x398: v69aV398(0x60) = CONST 
    0x69cS0x398: v69cV398 = SHL v69aV398(0x60), v699V398
    0x69eS0x398: MSTORE v685V398, v69cV398
    0x69fS0x398: v69fV398(0x14) = CONST 
    0x6a1S0x398: v6a1V398 = ADD v69fV398(0x14), v685V398
    0x6a3S0x398: v6a3V398(0x1) = CONST 
    0x6a5S0x398: v6a5V398(0x1) = CONST 
    0x6a7S0x398: v6a7V398(0xa0) = CONST 
    0x6a9S0x398: v6a9V398(0x10000000000000000000000000000000000000000) = SHL v6a7V398(0xa0), v6a5V398(0x1)
    0x6aaS0x398: v6aaV398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6a9V398(0x10000000000000000000000000000000000000000), v6a3V398(0x1)
    0x6abS0x398: v6abV398 = AND v6aaV398(0xffffffffffffffffffffffffffffffffffffffff), v67bV398
    0x6acS0x398: v6acV398(0x1) = CONST 
    0x6aeS0x398: v6aeV398(0x1) = CONST 
    0x6b0S0x398: v6b0V398(0xa0) = CONST 
    0x6b2S0x398: v6b2V398(0x10000000000000000000000000000000000000000) = SHL v6b0V398(0xa0), v6aeV398(0x1)
    0x6b3S0x398: v6b3V398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6b2V398(0x10000000000000000000000000000000000000000), v6acV398(0x1)
    0x6b4S0x398: v6b4V398 = AND v6b3V398(0xffffffffffffffffffffffffffffffffffffffff), v6abV398
    0x6b5S0x398: v6b5V398(0x60) = CONST 
    0x6b7S0x398: v6b7V398 = SHL v6b5V398(0x60), v6b4V398
    0x6b9S0x398: MSTORE v6a1V398, v6b7V398
    0x6baS0x398: v6baV398(0x14) = CONST 
    0x6bcS0x398: v6bcV398 = ADD v6baV398(0x14), v6a1V398
    0x6bfS0x398: MSTORE v6bcV398, v675V398
    0x6c0S0x398: v6c0V398(0x20) = CONST 
    0x6c2S0x398: v6c2V398 = ADD v6c0V398(0x20), v6bcV398
    0x6c8S0x398: CALLDATACOPY v6c2V398, v67dV398(0x0), v67fV398
    0x6cbS0x398: v6cbV398 = ADD v6c2V398, v67fV398
    0x6d7S0x398: v6d7V398(0x40) = CONST 
    0x6d9S0x398: v6d9V398 = MLOAD v6d7V398(0x40)
    0x6daS0x398: v6daV398(0x20) = CONST 
    0x6deS0x398: v6deV398 = SUB v6cbV398, v6d9V398
    0x6dfS0x398: v6dfV398 = SUB v6deV398, v6daV398(0x20)
    0x6e1S0x398: MSTORE v6d9V398, v6dfV398
    0x6e3S0x398: v6e3V398(0x40) = CONST 
    0x6e5S0x398: MSTORE v6e3V398(0x40), v6cbV398
    0x6e7S0x398: v6e7V398 = MLOAD v6d9V398
    0x6e9S0x398: v6e9V398(0x20) = CONST 
    0x6ebS0x398: v6ebV398 = ADD v6e9V398(0x20), v6d9V398
    0x6ecS0x398: v6ecV398 = SHA3 v6ebV398, v6e7V398
    0x6efS0x398: v6efV398(0x0) = CONST 
    0x6f1S0x398: v6f1V398(0x6f8) = CONST 
    0x6f4S0x398: v6f4V398(0x421) = CONST 
    0x6f7S0x398: JUMP v6f4V398(0x421)

    Begin block 0x421B0x672B0x398
    prev=[0x672B0x398], succ=[0x836B0x421B0x672B0x398]
    =================================
    0x422S0x672S0x398: v422V672V398(0x0) = CONST 
    0x424S0x672S0x398: v424V672V398(0xcad) = CONST 
    0x427S0x672S0x398: v427V672V398(0x40) = CONST 
    0x429S0x672S0x398: v429V672V398 = MLOAD v427V672V398(0x40)
    0x42cS0x672S0x398: v42cV672V398(0x90b) = CONST 
    0x42fS0x672S0x398: v42fV672V398(0x23) = CONST 
    0x432S0x672S0x398: CODECOPY v429V672V398, v42cV672V398(0x90b), v42fV672V398(0x23)
    0x433S0x672S0x398: v433V672V398(0x23) = CONST 
    0x435S0x672S0x398: v435V672V398 = ADD v433V672V398(0x23), v429V672V398
    0x438S0x672S0x398: v438V672V398(0x40) = CONST 
    0x43aS0x672S0x398: v43aV672V398 = MLOAD v438V672V398(0x40)
    0x43dS0x672S0x398: v43dV672V398(0x23) = SUB v435V672V398, v43aV672V398
    0x43fS0x672S0x398: v43fV672V398 = SHA3 v43aV672V398, v43dV672V398(0x23)
    0x440S0x672S0x398: v440V672V398(0x836) = CONST 
    0x443S0x672S0x398: JUMP v440V672V398(0x836)

    Begin block 0x836B0x421B0x672B0x398
    prev=[0x421B0x672B0x398], succ=[0xcadB0x672B0x398]
    =================================
    0x837S0x421S0x672S0x398: v837V421V672V398 = SLOAD v43fV672V398
    0x839S0x421S0x672S0x398: JUMP v424V672V398(0xcad)

    Begin block 0xcadB0x672B0x398
    prev=[0x836B0x421B0x672B0x398], succ=[0x6f8B0x398]
    =================================
    0xcb1S0x672S0x398: JUMP v6f1V398(0x6f8)

    Begin block 0x6f8B0x398
    prev=[0xcadB0x672B0x398], succ=[0x836B0x6f8B0x398]
    =================================
    0x6fbS0x398: v6fbV398(0x0) = CONST 
    0x6fdS0x398: v6fdV398(0x705) = CONST 
    0x701S0x398: v701V398(0x836) = CONST 
    0x704S0x398: JUMP v701V398(0x836)

    Begin block 0x836B0x6f8B0x398
    prev=[0x6f8B0x398], succ=[0x705B0x398]
    =================================
    0x837S0x6f8S0x398: v837V6f8V398 = SLOAD v6ecV398
    0x839S0x6f8S0x398: JUMP v6fdV398(0x705)

    Begin block 0x705B0x398
    prev=[0x836B0x6f8B0x398], succ=[0x751B0x398, 0x755B0x398]
    =================================
    0x708S0x398: v708V398(0x0) = CONST 
    0x70bS0x398: v70bV398(0x1) = CONST 
    0x70dS0x398: v70dV398(0x1) = CONST 
    0x70fS0x398: v70fV398(0xa0) = CONST 
    0x711S0x398: v711V398(0x10000000000000000000000000000000000000000) = SHL v70fV398(0xa0), v70dV398(0x1)
    0x712S0x398: v712V398(0xffffffffffffffffffffffffffffffffffffffff) = SUB v711V398(0x10000000000000000000000000000000000000000), v70bV398(0x1)
    0x713S0x398: v713V398 = AND v712V398(0xffffffffffffffffffffffffffffffffffffffff), v837V421V672V398
    0x714S0x398: v714V398(0x1ebaa166) = CONST 
    0x71bS0x398: v71bV398(0x40) = CONST 
    0x71dS0x398: v71dV398 = MLOAD v71bV398(0x40)
    0x71fS0x398: v71fV398(0xffffffff) = CONST 
    0x724S0x398: v724V398(0x1ebaa166) = AND v71fV398(0xffffffff), v714V398(0x1ebaa166)
    0x725S0x398: v725V398(0xe0) = CONST 
    0x727S0x398: v727V398(0x1ebaa16600000000000000000000000000000000000000000000000000000000) = SHL v725V398(0xe0), v724V398(0x1ebaa166)
    0x729S0x398: MSTORE v71dV398, v727V398(0x1ebaa16600000000000000000000000000000000000000000000000000000000)
    0x72aS0x398: v72aV398(0x4) = CONST 
    0x72cS0x398: v72cV398 = ADD v72aV398(0x4), v71dV398
    0x730S0x398: MSTORE v72cV398, v6ecV398
    0x731S0x398: v731V398(0x20) = CONST 
    0x733S0x398: v733V398 = ADD v731V398(0x20), v72cV398
    0x736S0x398: MSTORE v733V398, v837V6f8V398
    0x737S0x398: v737V398(0x20) = CONST 
    0x739S0x398: v739V398 = ADD v737V398(0x20), v733V398
    0x73eS0x398: v73eV398(0x20) = CONST 
    0x740S0x398: v740V398(0x40) = CONST 
    0x742S0x398: v742V398 = MLOAD v740V398(0x40)
    0x745S0x398: v745V398(0x44) = SUB v739V398, v742V398
    0x749S0x398: v749V398 = EXTCODESIZE v713V398
    0x74aS0x398: v74aV398 = ISZERO v749V398
    0x74cS0x398: v74cV398 = ISZERO v74aV398
    0x74dS0x398: v74dV398(0x755) = CONST 
    0x750S0x398: JUMPI v74dV398(0x755), v74cV398

    Begin block 0x751B0x398
    prev=[0x705B0x398], succ=[]
    =================================
    0x751S0x398: v751V398(0x0) = CONST 
    0x754S0x398: REVERT v751V398(0x0), v751V398(0x0)

    Begin block 0x755B0x398
    prev=[0x705B0x398], succ=[0x760B0x398, 0x769B0x398]
    =================================
    0x757S0x398: v757V398 = GAS 
    0x758S0x398: v758V398 = STATICCALL v757V398, v713V398, v742V398, v745V398(0x44), v742V398, v73eV398(0x20)
    0x759S0x398: v759V398 = ISZERO v758V398
    0x75bS0x398: v75bV398 = ISZERO v759V398
    0x75cS0x398: v75cV398(0x769) = CONST 
    0x75fS0x398: JUMPI v75cV398(0x769), v75bV398

    Begin block 0x760B0x398
    prev=[0x755B0x398], succ=[]
    =================================
    0x760S0x398: v760V398 = RETURNDATASIZE 
    0x761S0x398: v761V398(0x0) = CONST 
    0x764S0x398: RETURNDATACOPY v761V398(0x0), v761V398(0x0), v760V398
    0x765S0x398: v765V398 = RETURNDATASIZE 
    0x766S0x398: v766V398(0x0) = CONST 
    0x768S0x398: REVERT v766V398(0x0), v765V398

    Begin block 0x769B0x398
    prev=[0x755B0x398], succ=[0x77bB0x398, 0x77fB0x398]
    =================================
    0x76eS0x398: v76eV398(0x40) = CONST 
    0x770S0x398: v770V398 = MLOAD v76eV398(0x40)
    0x771S0x398: v771V398 = RETURNDATASIZE 
    0x772S0x398: v772V398(0x20) = CONST 
    0x775S0x398: v775V398 = LT v771V398, v772V398(0x20)
    0x776S0x398: v776V398 = ISZERO v775V398
    0x777S0x398: v777V398(0x77f) = CONST 
    0x77aS0x398: JUMPI v777V398(0x77f), v776V398

    Begin block 0x77bB0x398
    prev=[0x769B0x398], succ=[]
    =================================
    0x77bS0x398: v77bV398(0x0) = CONST 
    0x77eS0x398: REVERT v77bV398(0x0), v77bV398(0x0)

    Begin block 0x77fB0x398
    prev=[0x769B0x398], succ=[0x789B0x398, 0x7bfB0x398]
    =================================
    0x781S0x398: v781V398 = MLOAD v770V398
    0x785S0x398: v785V398(0x7bf) = CONST 
    0x788S0x398: JUMPI v785V398(0x7bf), v781V398

    Begin block 0x789B0x398
    prev=[0x77fB0x398], succ=[]
    =================================
    0x789S0x398: v789V398(0x40) = CONST 
    0x78bS0x398: v78bV398 = MLOAD v789V398(0x40)
    0x78cS0x398: v78cV398(0x461bcd) = CONST 
    0x790S0x398: v790V398(0xe5) = CONST 
    0x792S0x398: v792V398(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v790V398(0xe5), v78cV398(0x461bcd)
    0x794S0x398: MSTORE v78bV398, v792V398(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x795S0x398: v795V398(0x4) = CONST 
    0x797S0x398: v797V398 = ADD v795V398(0x4), v78bV398
    0x79aS0x398: v79aV398(0x20) = CONST 
    0x79cS0x398: v79cV398 = ADD v79aV398(0x20), v797V398
    0x79fS0x398: v79fV398(0x20) = SUB v79cV398, v797V398
    0x7a1S0x398: MSTORE v797V398, v79fV398(0x20)
    0x7a2S0x398: v7a2V398(0x2e) = CONST 
    0x7a5S0x398: MSTORE v79cV398, v7a2V398(0x2e)
    0x7a6S0x398: v7a6V398(0x20) = CONST 
    0x7a8S0x398: v7a8V398 = ADD v7a6V398(0x20), v79cV398
    0x7aaS0x398: v7aaV398(0x92e) = CONST 
    0x7adS0x398: v7adV398(0x2e) = CONST 
    0x7b0S0x398: CODECOPY v7a8V398, v7aaV398(0x92e), v7adV398(0x2e)
    0x7b1S0x398: v7b1V398(0x40) = CONST 
    0x7b3S0x398: v7b3V398 = ADD v7b1V398(0x40), v7a8V398
    0x7b7S0x398: v7b7V398(0x40) = CONST 
    0x7b9S0x398: v7b9V398 = MLOAD v7b7V398(0x40)
    0x7bcS0x398: v7bcV398(0x84) = SUB v7b3V398, v7b9V398
    0x7beS0x398: REVERT v7b9V398, v7bcV398(0x84)

    Begin block 0x7bfB0x398
    prev=[0x77fB0x398], succ=[0x8daB0x398]
    =================================
    0x7c0S0x398: v7c0V398(0x7c9) = CONST 
    0x7c5S0x398: v7c5V398(0x8da) = CONST 
    0x7c8S0x398: JUMP v7c5V398(0x8da)

    Begin block 0x8daB0x398
    prev=[0x7bfB0x398], succ=[0x7c9B0x398]
    =================================
    0x8dcS0x398: SSTORE v6ecV398, v781V398
    0x8ddS0x398: JUMP v7c0V398(0x7c9)

    Begin block 0x7c9B0x398
    prev=[0x8daB0x398], succ=[0x3a0]
    =================================
    0x7cfS0x398: JUMP v399(0x3a0)

    Begin block 0x3a0
    prev=[0x7c9B0x398], succ=[0x7d0]
    =================================
    0x3a1: v3a1(0x3a9) = CONST 
    0x3a5: v3a5(0x7d0) = CONST 
    0x3a8: JUMP v3a5(0x7d0)

    Begin block 0x7d0
    prev=[0x3a0], succ=[0x8de]
    =================================
    0x7d1: v7d1(0x7d9) = CONST 
    0x7d5: v7d5(0x8de) = CONST 
    0x7d8: JUMP v7d5(0x8de)

    Begin block 0x8de
    prev=[0x7d0], succ=[0x7d9]
    =================================
    0x8df: v8df = EXTCODESIZE v140
    0x8e0: v8e0 = ISZERO v8df
    0x8e1: v8e1 = ISZERO v8e0
    0x8e3: JUMP v7d1(0x7d9)

    Begin block 0x7d9
    prev=[0x8de], succ=[0x7de, 0x814]
    =================================
    0x7da: v7da(0x814) = CONST 
    0x7dd: JUMPI v7da(0x814), v8e1

    Begin block 0x7de
    prev=[0x7d9], succ=[]
    =================================
    0x7de: v7de(0x40) = CONST 
    0x7e0: v7e0 = MLOAD v7de(0x40)
    0x7e1: v7e1(0x461bcd) = CONST 
    0x7e5: v7e5(0xe5) = CONST 
    0x7e7: v7e7(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7e5(0xe5), v7e1(0x461bcd)
    0x7e9: MSTORE v7e0, v7e7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7ea: v7ea(0x4) = CONST 
    0x7ec: v7ec = ADD v7ea(0x4), v7e0
    0x7ef: v7ef(0x20) = CONST 
    0x7f1: v7f1 = ADD v7ef(0x20), v7ec
    0x7f4: v7f4(0x20) = SUB v7f1, v7ec
    0x7f6: MSTORE v7ec, v7f4(0x20)
    0x7f7: v7f7(0x3b) = CONST 
    0x7fa: MSTORE v7f1, v7f7(0x3b)
    0x7fb: v7fb(0x20) = CONST 
    0x7fd: v7fd = ADD v7fb(0x20), v7f1
    0x7ff: v7ff(0x99f) = CONST 
    0x802: v802(0x3b) = CONST 
    0x805: CODECOPY v7fd, v7ff(0x99f), v802(0x3b)
    0x806: v806(0x40) = CONST 
    0x808: v808 = ADD v806(0x40), v7fd
    0x80c: v80c(0x40) = CONST 
    0x80e: v80e = MLOAD v80c(0x40)
    0x811: v811(0x84) = SUB v808, v80e
    0x813: REVERT v80e, v811(0x84)

    Begin block 0x814
    prev=[0x7d9], succ=[0x3a9]
    =================================
    0x815: v815(0x0) = CONST 
    0x817: v817(0x40) = CONST 
    0x819: v819 = MLOAD v817(0x40)
    0x81c: v81c(0x97c) = CONST 
    0x81f: v81f(0x23) = CONST 
    0x822: CODECOPY v819, v81c(0x97c), v81f(0x23)
    0x823: v823(0x40) = CONST 
    0x825: v825 = MLOAD v823(0x40)
    0x829: v829(0x0) = SUB v819, v825
    0x82a: v82a(0x23) = CONST 
    0x82c: v82c(0x23) = ADD v82a(0x23), v829(0x0)
    0x82e: v82e = SHA3 v825, v82c(0x23)
    0x832: SSTORE v82e, v140
    0x835: JUMP v3a1(0x3a9)

    Begin block 0x3a9
    prev=[0x814], succ=[0xab6]
    =================================
    0x3aa: v3aa(0x40) = CONST 
    0x3ac: v3ac = MLOAD v3aa(0x40)
    0x3ad: v3ad(0x1) = CONST 
    0x3af: v3af(0x1) = CONST 
    0x3b1: v3b1(0xa0) = CONST 
    0x3b3: v3b3(0x10000000000000000000000000000000000000000) = SHL v3b1(0xa0), v3af(0x1)
    0x3b4: v3b4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b3(0x10000000000000000000000000000000000000000), v3ad(0x1)
    0x3b6: v3b6 = AND v140, v3b4(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b8: v3b8(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x3da: v3da(0x0) = CONST 
    0x3dd: LOG2 v3ac, v3da(0x0), v3b8(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v3b6
    0x3e0: JUMP v120(0xab6)

    Begin block 0xab6
    prev=[0x3a9], succ=[]
    =================================
    0xab7: STOP 

}

function proxyType()() public {
    Begin block 0x145
    prev=[], succ=[0x14d, 0x151]
    =================================
    0x146: v146 = CALLVALUE 
    0x148: v148 = ISZERO v146
    0x149: v149(0x151) = CONST 
    0x14c: JUMPI v149(0x151), v148

    Begin block 0x14d
    prev=[0x145], succ=[]
    =================================
    0x14d: v14d(0x0) = CONST 
    0x150: REVERT v14d(0x0), v14d(0x0)

    Begin block 0x151
    prev=[0x145], succ=[0x3e1]
    =================================
    0x153: v153(0x15a) = CONST 
    0x156: v156(0x3e1) = CONST 
    0x159: JUMP v156(0x3e1)

    Begin block 0x3e1
    prev=[0x151], succ=[0x15a]
    =================================
    0x3e2: v3e2(0x2) = CONST 
    0x3e5: JUMP v153(0x15a)

    Begin block 0x15a
    prev=[0x3e1], succ=[]
    =================================
    0x15b: v15b(0x40) = CONST 
    0x15e: v15e = MLOAD v15b(0x40)
    0x161: MSTORE v15e, v3e2(0x2)
    0x162: v162 = MLOAD v15b(0x40)
    0x166: v166(0x0) = SUB v15e, v162
    0x167: v167(0x20) = CONST 
    0x169: v169(0x20) = ADD v167(0x20), v166(0x0)
    0x16b: RETURN v162, v169(0x20)

}

function implementation()() public {
    Begin block 0x16c
    prev=[], succ=[0x174, 0x178]
    =================================
    0x16d: v16d = CALLVALUE 
    0x16f: v16f = ISZERO v16d
    0x170: v170(0x178) = CONST 
    0x173: JUMPI v170(0x178), v16f

    Begin block 0x174
    prev=[0x16c], succ=[]
    =================================
    0x174: v174(0x0) = CONST 
    0x177: REVERT v174(0x0), v174(0x0)

    Begin block 0x178
    prev=[0x16c], succ=[0x3e6B0x178]
    =================================
    0x17a: v17a(0xad7) = CONST 
    0x17d: v17d(0x3e6) = CONST 
    0x180: JUMP v17d(0x3e6)

    Begin block 0x3e6B0x178
    prev=[0x178], succ=[0x62bB0x3e6B0x178]
    =================================
    0x3e7S0x178: v3e7V178(0x0) = CONST 
    0x3e9S0x178: v3e9V178(0xc89) = CONST 
    0x3ecS0x178: v3ecV178(0x62b) = CONST 
    0x3efS0x178: JUMP v3ecV178(0x62b)

    Begin block 0x62bB0x3e6B0x178
    prev=[0x3e6B0x178], succ=[0xc89B0x178]
    =================================
    0x62cS0x3e6S0x178: v62cV3e6V178(0x0) = CONST 
    0x62fS0x3e6S0x178: v62fV3e6V178(0x40) = CONST 
    0x631S0x3e6S0x178: v631V3e6V178 = MLOAD v62fV3e6V178(0x40)
    0x634S0x3e6S0x178: v634V3e6V178(0x97c) = CONST 
    0x637S0x3e6S0x178: v637V3e6V178(0x23) = CONST 
    0x63aS0x3e6S0x178: CODECOPY v631V3e6V178, v634V3e6V178(0x97c), v637V3e6V178(0x23)
    0x63bS0x3e6S0x178: v63bV3e6V178(0x40) = CONST 
    0x63dS0x3e6S0x178: v63dV3e6V178 = MLOAD v63bV3e6V178(0x40)
    0x641S0x3e6S0x178: v641V3e6V178(0x0) = SUB v631V3e6V178, v63dV3e6V178
    0x642S0x3e6S0x178: v642V3e6V178(0x23) = CONST 
    0x644S0x3e6S0x178: v644V3e6V178(0x23) = ADD v642V3e6V178(0x23), v641V3e6V178(0x0)
    0x646S0x3e6S0x178: v646V3e6V178 = SHA3 v63dV3e6V178, v644V3e6V178(0x23)
    0x647S0x3e6S0x178: v647V3e6V178 = SLOAD v646V3e6V178
    0x64dS0x3e6S0x178: JUMP v3e9V178(0xc89)

    Begin block 0xc89B0x178
    prev=[0x62bB0x3e6B0x178], succ=[0xad7]
    =================================
    0xc8dS0x178: JUMP v17a(0xad7)

    Begin block 0xad7
    prev=[0xc89B0x178], succ=[]
    =================================
    0xad8: vad8(0x40) = CONST 
    0xadb: vadb = MLOAD vad8(0x40)
    0xadc: vadc(0x1) = CONST 
    0xade: vade(0x1) = CONST 
    0xae0: vae0(0xa0) = CONST 
    0xae2: vae2(0x10000000000000000000000000000000000000000) = SHL vae0(0xa0), vade(0x1)
    0xae3: vae3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vae2(0x10000000000000000000000000000000000000000), vadc(0x1)
    0xae6: vae6 = AND v647V3e6V178, vae3(0xffffffffffffffffffffffffffffffffffffffff)
    0xae8: MSTORE vadb, vae6
    0xae9: vae9 = MLOAD vad8(0x40)
    0xaed: vaed(0x0) = SUB vadb, vae9
    0xaee: vaee(0x20) = CONST 
    0xaf0: vaf0(0x20) = ADD vaee(0x20), vaed(0x0)
    0xaf2: RETURN vae9, vaf0(0x20)

}

function allLockedPhx(address)() public {
    Begin block 0x181
    prev=[], succ=[0x189, 0x18d]
    =================================
    0x182: v182 = CALLVALUE 
    0x184: v184 = ISZERO v182
    0x185: v185(0x18d) = CONST 
    0x188: JUMPI v185(0x18d), v184

    Begin block 0x189
    prev=[0x181], succ=[]
    =================================
    0x189: v189(0x0) = CONST 
    0x18c: REVERT v189(0x0), v189(0x0)

    Begin block 0x18d
    prev=[0x181], succ=[0x1a0, 0x1a4]
    =================================
    0x18f: v18f(0x1b4) = CONST 
    0x192: v192(0x4) = CONST 
    0x195: v195 = CALLDATASIZE 
    0x196: v196 = SUB v195, v192(0x4)
    0x197: v197(0x20) = CONST 
    0x19a: v19a = LT v196, v197(0x20)
    0x19b: v19b = ISZERO v19a
    0x19c: v19c(0x1a4) = CONST 
    0x19f: JUMPI v19c(0x1a4), v19b

    Begin block 0x1a0
    prev=[0x18d], succ=[]
    =================================
    0x1a0: v1a0(0x0) = CONST 
    0x1a3: REVERT v1a0(0x0), v1a0(0x0)

    Begin block 0x1a4
    prev=[0x18d], succ=[0x3f5]
    =================================
    0x1a6: v1a6 = CALLDATALOAD v192(0x4)
    0x1a7: v1a7(0x1) = CONST 
    0x1a9: v1a9(0x1) = CONST 
    0x1ab: v1ab(0xa0) = CONST 
    0x1ad: v1ad(0x10000000000000000000000000000000000000000) = SHL v1ab(0xa0), v1a9(0x1)
    0x1ae: v1ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1ad(0x10000000000000000000000000000000000000000), v1a7(0x1)
    0x1af: v1af = AND v1ae(0xffffffffffffffffffffffffffffffffffffffff), v1a6
    0x1b0: v1b0(0x3f5) = CONST 
    0x1b3: JUMP v1b0(0x3f5)

    Begin block 0x3f5
    prev=[0x1a4], succ=[0x1b4]
    =================================
    0x3f6: v3f6(0x3) = CONST 
    0x3f8: v3f8(0x20) = CONST 
    0x3fc: MSTORE v3f8(0x20), v3f6(0x3)
    0x3fd: v3fd(0x0) = CONST 
    0x401: MSTORE v3fd(0x0), v1af
    0x402: v402(0x40) = CONST 
    0x406: v406 = SHA3 v3fd(0x0), v402(0x40)
    0x408: v408 = SLOAD v406
    0x409: v409(0x1) = CONST 
    0x40c: v40c = ADD v406, v409(0x1)
    0x40d: v40d = SLOAD v40c
    0x40e: v40e(0x2) = CONST 
    0x411: v411 = ADD v406, v40e(0x2)
    0x412: v412 = SLOAD v411
    0x416: v416 = ADD v3f6(0x3), v406
    0x417: v417 = SLOAD v416
    0x41c: v41c(0xff) = CONST 
    0x41e: v41e = AND v41c(0xff), v417
    0x420: JUMP v18f(0x1b4)

    Begin block 0x1b4
    prev=[0x3f5], succ=[]
    =================================
    0x1b5: v1b5(0x40) = CONST 
    0x1b8: v1b8 = MLOAD v1b5(0x40)
    0x1bb: MSTORE v1b8, v408
    0x1bc: v1bc(0x20) = CONST 
    0x1bf: v1bf = ADD v1b8, v1bc(0x20)
    0x1c3: MSTORE v1bf, v40d
    0x1c6: v1c6 = ADD v1b5(0x40), v1b8
    0x1ca: MSTORE v1c6, v412
    0x1cb: v1cb = ISZERO v41e
    0x1cc: v1cc = ISZERO v1cb
    0x1cd: v1cd(0x60) = CONST 
    0x1d0: v1d0 = ADD v1b8, v1cd(0x60)
    0x1d1: MSTORE v1d0, v1cc
    0x1d2: v1d2 = MLOAD v1b5(0x40)
    0x1d6: v1d6(0x0) = SUB v1b8, v1d2
    0x1d7: v1d7(0x80) = CONST 
    0x1d9: v1d9(0x80) = ADD v1d7(0x80), v1d6(0x0)
    0x1db: RETURN v1d2, v1d9(0x80)

}

function getMultiSignatureAddress()() public {
    Begin block 0x1dc
    prev=[], succ=[0x1e4, 0x1e8]
    =================================
    0x1dd: v1dd = CALLVALUE 
    0x1df: v1df = ISZERO v1dd
    0x1e0: v1e0(0x1e8) = CONST 
    0x1e3: JUMPI v1e0(0x1e8), v1df

    Begin block 0x1e4
    prev=[0x1dc], succ=[]
    =================================
    0x1e4: v1e4(0x0) = CONST 
    0x1e7: REVERT v1e4(0x0), v1e4(0x0)

    Begin block 0x1e8
    prev=[0x1dc], succ=[0x421B0x1e8]
    =================================
    0x1ea: v1ea(0xb12) = CONST 
    0x1ed: v1ed(0x421) = CONST 
    0x1f0: JUMP v1ed(0x421)

    Begin block 0x421B0x1e8
    prev=[0x1e8], succ=[0x836B0x421B0x1e8]
    =================================
    0x422S0x1e8: v422V1e8(0x0) = CONST 
    0x424S0x1e8: v424V1e8(0xcad) = CONST 
    0x427S0x1e8: v427V1e8(0x40) = CONST 
    0x429S0x1e8: v429V1e8 = MLOAD v427V1e8(0x40)
    0x42cS0x1e8: v42cV1e8(0x90b) = CONST 
    0x42fS0x1e8: v42fV1e8(0x23) = CONST 
    0x432S0x1e8: CODECOPY v429V1e8, v42cV1e8(0x90b), v42fV1e8(0x23)
    0x433S0x1e8: v433V1e8(0x23) = CONST 
    0x435S0x1e8: v435V1e8 = ADD v433V1e8(0x23), v429V1e8
    0x438S0x1e8: v438V1e8(0x40) = CONST 
    0x43aS0x1e8: v43aV1e8 = MLOAD v438V1e8(0x40)
    0x43dS0x1e8: v43dV1e8(0x23) = SUB v435V1e8, v43aV1e8
    0x43fS0x1e8: v43fV1e8 = SHA3 v43aV1e8, v43dV1e8(0x23)
    0x440S0x1e8: v440V1e8(0x836) = CONST 
    0x443S0x1e8: JUMP v440V1e8(0x836)

    Begin block 0x836B0x421B0x1e8
    prev=[0x421B0x1e8], succ=[0xcadB0x1e8]
    =================================
    0x837S0x421S0x1e8: v837V421V1e8 = SLOAD v43fV1e8
    0x839S0x421S0x1e8: JUMP v424V1e8(0xcad)

    Begin block 0xcadB0x1e8
    prev=[0x836B0x421B0x1e8], succ=[0xb12]
    =================================
    0xcb1S0x1e8: JUMP v1ea(0xb12)

    Begin block 0xb12
    prev=[0xcadB0x1e8], succ=[]
    =================================
    0xb13: vb13(0x40) = CONST 
    0xb16: vb16 = MLOAD vb13(0x40)
    0xb17: vb17(0x1) = CONST 
    0xb19: vb19(0x1) = CONST 
    0xb1b: vb1b(0xa0) = CONST 
    0xb1d: vb1d(0x10000000000000000000000000000000000000000) = SHL vb1b(0xa0), vb19(0x1)
    0xb1e: vb1e(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb1d(0x10000000000000000000000000000000000000000), vb17(0x1)
    0xb21: vb21 = AND v837V421V1e8, vb1e(0xffffffffffffffffffffffffffffffffffffffff)
    0xb23: MSTORE vb16, vb21
    0xb24: vb24 = MLOAD vb13(0x40)
    0xb28: vb28(0x0) = SUB vb16, vb24
    0xb29: vb29(0x20) = CONST 
    0xb2b: vb2b(0x20) = ADD vb29(0x20), vb28(0x0)
    0xb2d: RETURN vb24, vb2b(0x20)

}

function phxAddress()() public {
    Begin block 0x1f1
    prev=[], succ=[0x1f9, 0x1fd]
    =================================
    0x1f2: v1f2 = CALLVALUE 
    0x1f4: v1f4 = ISZERO v1f2
    0x1f5: v1f5(0x1fd) = CONST 
    0x1f8: JUMPI v1f5(0x1fd), v1f4

    Begin block 0x1f9
    prev=[0x1f1], succ=[]
    =================================
    0x1f9: v1f9(0x0) = CONST 
    0x1fc: REVERT v1f9(0x0), v1f9(0x0)

    Begin block 0x1fd
    prev=[0x1f1], succ=[0x444]
    =================================
    0x1ff: v1ff(0xb4d) = CONST 
    0x202: v202(0x444) = CONST 
    0x205: JUMP v202(0x444)

    Begin block 0x444
    prev=[0x1fd], succ=[0xb4d]
    =================================
    0x445: v445(0x2) = CONST 
    0x447: v447 = SLOAD v445(0x2)
    0x448: v448(0x100) = CONST 
    0x44c: v44c = DIV v447, v448(0x100)
    0x44d: v44d(0x1) = CONST 
    0x44f: v44f(0x1) = CONST 
    0x451: v451(0xa0) = CONST 
    0x453: v453(0x10000000000000000000000000000000000000000) = SHL v451(0xa0), v44f(0x1)
    0x454: v454(0xffffffffffffffffffffffffffffffffffffffff) = SUB v453(0x10000000000000000000000000000000000000000), v44d(0x1)
    0x455: v455 = AND v454(0xffffffffffffffffffffffffffffffffffffffff), v44c
    0x457: JUMP v1ff(0xb4d)

    Begin block 0xb4d
    prev=[0x444], succ=[]
    =================================
    0xb4e: vb4e(0x40) = CONST 
    0xb51: vb51 = MLOAD vb4e(0x40)
    0xb52: vb52(0x1) = CONST 
    0xb54: vb54(0x1) = CONST 
    0xb56: vb56(0xa0) = CONST 
    0xb58: vb58(0x10000000000000000000000000000000000000000) = SHL vb56(0xa0), vb54(0x1)
    0xb59: vb59(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb58(0x10000000000000000000000000000000000000000), vb52(0x1)
    0xb5c: vb5c = AND v455, vb59(0xffffffffffffffffffffffffffffffffffffffff)
    0xb5e: MSTORE vb51, vb5c
    0xb5f: vb5f = MLOAD vb4e(0x40)
    0xb63: vb63(0x0) = SUB vb51, vb5f
    0xb64: vb64(0x20) = CONST 
    0xb66: vb66(0x20) = ADD vb64(0x20), vb63(0x0)
    0xb68: RETURN vb5f, vb66(0x20)

}

function renounceOwnership()() public {
    Begin block 0x206
    prev=[], succ=[0x20e, 0x212]
    =================================
    0x207: v207 = CALLVALUE 
    0x209: v209 = ISZERO v207
    0x20a: v20a(0x212) = CONST 
    0x20d: JUMPI v20a(0x212), v209

    Begin block 0x20e
    prev=[0x206], succ=[]
    =================================
    0x20e: v20e(0x0) = CONST 
    0x211: REVERT v20e(0x0), v20e(0x0)

    Begin block 0x212
    prev=[0x206], succ=[0x458]
    =================================
    0x214: v214(0xb88) = CONST 
    0x217: v217(0x458) = CONST 
    0x21a: JUMP v217(0x458)

    Begin block 0x458
    prev=[0x212], succ=[0x4f8B0x458]
    =================================
    0x459: v459(0x460) = CONST 
    0x45c: v45c(0x4f8) = CONST 
    0x45f: JUMP v45c(0x4f8)

    Begin block 0x4f8B0x458
    prev=[0x458], succ=[0x460]
    =================================
    0x4f9S0x458: v4f9V458(0x0) = CONST 
    0x4fbS0x458: v4fbV458 = SLOAD v4f9V458(0x0)
    0x4fcS0x458: v4fcV458(0x1) = CONST 
    0x4feS0x458: v4feV458(0x1) = CONST 
    0x500S0x458: v500V458(0xa0) = CONST 
    0x502S0x458: v502V458(0x10000000000000000000000000000000000000000) = SHL v500V458(0xa0), v4feV458(0x1)
    0x503S0x458: v503V458(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502V458(0x10000000000000000000000000000000000000000), v4fcV458(0x1)
    0x504S0x458: v504V458 = AND v503V458(0xffffffffffffffffffffffffffffffffffffffff), v4fbV458
    0x505S0x458: v505V458 = CALLER 
    0x506S0x458: v506V458 = EQ v505V458, v504V458
    0x508S0x458: JUMP v459(0x460)

    Begin block 0x460
    prev=[0x4f8B0x458], succ=[0x465, 0x49f]
    =================================
    0x461: v461(0x49f) = CONST 
    0x464: JUMPI v461(0x49f), v506V458

    Begin block 0x465
    prev=[0x460], succ=[]
    =================================
    0x465: v465(0x40) = CONST 
    0x468: v468 = MLOAD v465(0x40)
    0x469: v469(0x461bcd) = CONST 
    0x46d: v46d(0xe5) = CONST 
    0x46f: v46f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v46d(0xe5), v469(0x461bcd)
    0x471: MSTORE v468, v46f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x472: v472(0x20) = CONST 
    0x474: v474(0x4) = CONST 
    0x477: v477 = ADD v468, v474(0x4)
    0x47a: MSTORE v477, v472(0x20)
    0x47b: v47b(0x24) = CONST 
    0x47e: v47e = ADD v468, v47b(0x24)
    0x47f: MSTORE v47e, v472(0x20)
    0x480: v480(0x0) = CONST 
    0x483: v483 = MLOAD v480(0x0)
    0x484: v484(0x20) = CONST 
    0x486: v486(0x95c) = CONST 
    0x48e: MSTORE v480(0x0), v483
    0x48f: v48f(0x44) = CONST 
    0x492: v492 = ADD v468, v48f(0x44)
    0x493: MSTORE v492, vcfc(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x495: v495 = MLOAD v465(0x40)
    0x499: v499(0x0) = SUB v468, v495
    0x49a: v49a(0x64) = CONST 
    0x49c: v49c(0x64) = ADD v49a(0x64), v499(0x0)
    0x49e: REVERT v495, v49c(0x64)
    0xcfc: vcfc(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x49f
    prev=[0x460], succ=[0xb88]
    =================================
    0x4a0: v4a0(0x0) = CONST 
    0x4a3: v4a3 = SLOAD v4a0(0x0)
    0x4a4: v4a4(0x40) = CONST 
    0x4a6: v4a6 = MLOAD v4a4(0x40)
    0x4a7: v4a7(0x1) = CONST 
    0x4a9: v4a9(0x1) = CONST 
    0x4ab: v4ab(0xa0) = CONST 
    0x4ad: v4ad(0x10000000000000000000000000000000000000000) = SHL v4ab(0xa0), v4a9(0x1)
    0x4ae: v4ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ad(0x10000000000000000000000000000000000000000), v4a7(0x1)
    0x4b1: v4b1 = AND v4a3, v4ae(0xffffffffffffffffffffffffffffffffffffffff)
    0x4b3: v4b3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x4d7: LOG3 v4a6, v4a0(0x0), v4b3(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v4b1, v4a0(0x0)
    0x4d8: v4d8(0x0) = CONST 
    0x4db: v4db = SLOAD v4d8(0x0)
    0x4dc: v4dc(0x1) = CONST 
    0x4de: v4de(0x1) = CONST 
    0x4e0: v4e0(0xa0) = CONST 
    0x4e2: v4e2(0x10000000000000000000000000000000000000000) = SHL v4e0(0xa0), v4de(0x1)
    0x4e3: v4e3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e2(0x10000000000000000000000000000000000000000), v4dc(0x1)
    0x4e4: v4e4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e5: v4e5 = AND v4e4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v4db
    0x4e7: SSTORE v4d8(0x0), v4e5
    0x4e8: JUMP v214(0xb88)

    Begin block 0xb88
    prev=[0x49f], succ=[]
    =================================
    0xb89: STOP 

}

function owner()() public {
    Begin block 0x21b
    prev=[], succ=[0x223, 0x227]
    =================================
    0x21c: v21c = CALLVALUE 
    0x21e: v21e = ISZERO v21c
    0x21f: v21f(0x227) = CONST 
    0x222: JUMPI v21f(0x227), v21e

    Begin block 0x223
    prev=[0x21b], succ=[]
    =================================
    0x223: v223(0x0) = CONST 
    0x226: REVERT v223(0x0), v223(0x0)

    Begin block 0x227
    prev=[0x21b], succ=[0x4e9]
    =================================
    0x229: v229(0xba9) = CONST 
    0x22c: v22c(0x4e9) = CONST 
    0x22f: JUMP v22c(0x4e9)

    Begin block 0x4e9
    prev=[0x227], succ=[0xba9]
    =================================
    0x4ea: v4ea(0x0) = CONST 
    0x4ec: v4ec = SLOAD v4ea(0x0)
    0x4ed: v4ed(0x1) = CONST 
    0x4ef: v4ef(0x1) = CONST 
    0x4f1: v4f1(0xa0) = CONST 
    0x4f3: v4f3(0x10000000000000000000000000000000000000000) = SHL v4f1(0xa0), v4ef(0x1)
    0x4f4: v4f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4f3(0x10000000000000000000000000000000000000000), v4ed(0x1)
    0x4f5: v4f5 = AND v4f4(0xffffffffffffffffffffffffffffffffffffffff), v4ec
    0x4f7: JUMP v229(0xba9)

    Begin block 0xba9
    prev=[0x4e9], succ=[]
    =================================
    0xbaa: vbaa(0x40) = CONST 
    0xbad: vbad = MLOAD vbaa(0x40)
    0xbae: vbae(0x1) = CONST 
    0xbb0: vbb0(0x1) = CONST 
    0xbb2: vbb2(0xa0) = CONST 
    0xbb4: vbb4(0x10000000000000000000000000000000000000000) = SHL vbb2(0xa0), vbb0(0x1)
    0xbb5: vbb5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb4(0x10000000000000000000000000000000000000000), vbae(0x1)
    0xbb8: vbb8 = AND v4f5, vbb5(0xffffffffffffffffffffffffffffffffffffffff)
    0xbba: MSTORE vbad, vbb8
    0xbbb: vbbb = MLOAD vbaa(0x40)
    0xbbf: vbbf(0x0) = SUB vbad, vbbb
    0xbc0: vbc0(0x20) = CONST 
    0xbc2: vbc2(0x20) = ADD vbc0(0x20), vbbf(0x0)
    0xbc4: RETURN vbbb, vbc2(0x20)

}

function isOwner()() public {
    Begin block 0x230
    prev=[], succ=[0x238, 0x23c]
    =================================
    0x231: v231 = CALLVALUE 
    0x233: v233 = ISZERO v231
    0x234: v234(0x23c) = CONST 
    0x237: JUMPI v234(0x23c), v233

    Begin block 0x238
    prev=[0x230], succ=[]
    =================================
    0x238: v238(0x0) = CONST 
    0x23b: REVERT v238(0x0), v238(0x0)

    Begin block 0x23c
    prev=[0x230], succ=[0x4f8B0x23c]
    =================================
    0x23e: v23e(0x245) = CONST 
    0x241: v241(0x4f8) = CONST 
    0x244: JUMP v241(0x4f8)

    Begin block 0x4f8B0x23c
    prev=[0x23c], succ=[0x245]
    =================================
    0x4f9S0x23c: v4f9V23c(0x0) = CONST 
    0x4fbS0x23c: v4fbV23c = SLOAD v4f9V23c(0x0)
    0x4fcS0x23c: v4fcV23c(0x1) = CONST 
    0x4feS0x23c: v4feV23c(0x1) = CONST 
    0x500S0x23c: v500V23c(0xa0) = CONST 
    0x502S0x23c: v502V23c(0x10000000000000000000000000000000000000000) = SHL v500V23c(0xa0), v4feV23c(0x1)
    0x503S0x23c: v503V23c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502V23c(0x10000000000000000000000000000000000000000), v4fcV23c(0x1)
    0x504S0x23c: v504V23c = AND v503V23c(0xffffffffffffffffffffffffffffffffffffffff), v4fbV23c
    0x505S0x23c: v505V23c = CALLER 
    0x506S0x23c: v506V23c = EQ v505V23c, v504V23c
    0x508S0x23c: JUMP v23e(0x245)

    Begin block 0x245
    prev=[0x4f8B0x23c], succ=[]
    =================================
    0x246: v246(0x40) = CONST 
    0x249: v249 = MLOAD v246(0x40)
    0x24b: v24b = ISZERO v506V23c
    0x24c: v24c = ISZERO v24b
    0x24e: MSTORE v249, v24c
    0x24f: v24f = MLOAD v246(0x40)
    0x253: v253(0x0) = SUB v249, v24f
    0x254: v254(0x20) = CONST 
    0x256: v256(0x20) = ADD v254(0x20), v253(0x0)
    0x258: RETURN v24f, v256(0x20)

}

function setOperator(uint256,address)() public {
    Begin block 0x259
    prev=[], succ=[0x261, 0x265]
    =================================
    0x25a: v25a = CALLVALUE 
    0x25c: v25c = ISZERO v25a
    0x25d: v25d(0x265) = CONST 
    0x260: JUMPI v25d(0x265), v25c

    Begin block 0x261
    prev=[0x259], succ=[]
    =================================
    0x261: v261(0x0) = CONST 
    0x264: REVERT v261(0x0), v261(0x0)

    Begin block 0x265
    prev=[0x259], succ=[0x278, 0x27c]
    =================================
    0x267: v267(0xbe4) = CONST 
    0x26a: v26a(0x4) = CONST 
    0x26d: v26d = CALLDATASIZE 
    0x26e: v26e = SUB v26d, v26a(0x4)
    0x26f: v26f(0x40) = CONST 
    0x272: v272 = LT v26e, v26f(0x40)
    0x273: v273 = ISZERO v272
    0x274: v274(0x27c) = CONST 
    0x277: JUMPI v274(0x27c), v273

    Begin block 0x278
    prev=[0x265], succ=[]
    =================================
    0x278: v278(0x0) = CONST 
    0x27b: REVERT v278(0x0), v278(0x0)

    Begin block 0x27c
    prev=[0x265], succ=[0x509]
    =================================
    0x27f: v27f = CALLDATALOAD v26a(0x4)
    0x281: v281(0x20) = CONST 
    0x283: v283(0x24) = ADD v281(0x20), v26a(0x4)
    0x284: v284 = CALLDATALOAD v283(0x24)
    0x285: v285(0x1) = CONST 
    0x287: v287(0x1) = CONST 
    0x289: v289(0xa0) = CONST 
    0x28b: v28b(0x10000000000000000000000000000000000000000) = SHL v289(0xa0), v287(0x1)
    0x28c: v28c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v28b(0x10000000000000000000000000000000000000000), v285(0x1)
    0x28d: v28d = AND v28c(0xffffffffffffffffffffffffffffffffffffffff), v284
    0x28e: v28e(0x509) = CONST 
    0x291: JUMP v28e(0x509)

    Begin block 0x509
    prev=[0x27c], succ=[0x4f8B0x509]
    =================================
    0x50a: v50a(0x511) = CONST 
    0x50d: v50d(0x4f8) = CONST 
    0x510: JUMP v50d(0x4f8)

    Begin block 0x4f8B0x509
    prev=[0x509], succ=[0x511]
    =================================
    0x4f9S0x509: v4f9V509(0x0) = CONST 
    0x4fbS0x509: v4fbV509 = SLOAD v4f9V509(0x0)
    0x4fcS0x509: v4fcV509(0x1) = CONST 
    0x4feS0x509: v4feV509(0x1) = CONST 
    0x500S0x509: v500V509(0xa0) = CONST 
    0x502S0x509: v502V509(0x10000000000000000000000000000000000000000) = SHL v500V509(0xa0), v4feV509(0x1)
    0x503S0x509: v503V509(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502V509(0x10000000000000000000000000000000000000000), v4fcV509(0x1)
    0x504S0x509: v504V509 = AND v503V509(0xffffffffffffffffffffffffffffffffffffffff), v4fbV509
    0x505S0x509: v505V509 = CALLER 
    0x506S0x509: v506V509 = EQ v505V509, v504V509
    0x508S0x509: JUMP v50a(0x511)

    Begin block 0x511
    prev=[0x4f8B0x509], succ=[0x516, 0x550]
    =================================
    0x512: v512(0x550) = CONST 
    0x515: JUMPI v512(0x550), v506V509

    Begin block 0x516
    prev=[0x511], succ=[]
    =================================
    0x516: v516(0x40) = CONST 
    0x519: v519 = MLOAD v516(0x40)
    0x51a: v51a(0x461bcd) = CONST 
    0x51e: v51e(0xe5) = CONST 
    0x520: v520(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v51e(0xe5), v51a(0x461bcd)
    0x522: MSTORE v519, v520(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x523: v523(0x20) = CONST 
    0x525: v525(0x4) = CONST 
    0x528: v528 = ADD v519, v525(0x4)
    0x52b: MSTORE v528, v523(0x20)
    0x52c: v52c(0x24) = CONST 
    0x52f: v52f = ADD v519, v52c(0x24)
    0x530: MSTORE v52f, v523(0x20)
    0x531: v531(0x0) = CONST 
    0x534: v534 = MLOAD v531(0x0)
    0x535: v535(0x20) = CONST 
    0x537: v537(0x95c) = CONST 
    0x53f: MSTORE v531(0x0), v534
    0x540: v540(0x44) = CONST 
    0x543: v543 = ADD v519, v540(0x44)
    0x544: MSTORE v543, vd01(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x546: v546 = MLOAD v516(0x40)
    0x54a: v54a(0x0) = SUB v519, v546
    0x54b: v54b(0x64) = CONST 
    0x54d: v54d(0x64) = ADD v54b(0x64), v54a(0x0)
    0x54f: REVERT v546, v54d(0x64)
    0xd01: vd01(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x550
    prev=[0x511], succ=[0xbe4]
    =================================
    0x551: v551(0x0) = CONST 
    0x555: MSTORE v551(0x0), v27f
    0x556: v556(0x1) = CONST 
    0x558: v558(0x20) = CONST 
    0x55a: MSTORE v558(0x20), v556(0x1)
    0x55b: v55b(0x40) = CONST 
    0x55f: v55f = SHA3 v551(0x0), v55b(0x40)
    0x561: v561 = SLOAD v55f
    0x562: v562(0x1) = CONST 
    0x564: v564(0x1) = CONST 
    0x566: v566(0xa0) = CONST 
    0x568: v568(0x10000000000000000000000000000000000000000) = SHL v566(0xa0), v564(0x1)
    0x569: v569(0xffffffffffffffffffffffffffffffffffffffff) = SUB v568(0x10000000000000000000000000000000000000000), v562(0x1)
    0x56a: v56a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v569(0xffffffffffffffffffffffffffffffffffffffff)
    0x56b: v56b = AND v56a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v561
    0x56c: v56c(0x1) = CONST 
    0x56e: v56e(0x1) = CONST 
    0x570: v570(0xa0) = CONST 
    0x572: v572(0x10000000000000000000000000000000000000000) = SHL v570(0xa0), v56e(0x1)
    0x573: v573(0xffffffffffffffffffffffffffffffffffffffff) = SUB v572(0x10000000000000000000000000000000000000000), v56c(0x1)
    0x576: v576 = AND v28d, v573(0xffffffffffffffffffffffffffffffffffffffff)
    0x57a: v57a = OR v576, v56b
    0x57c: SSTORE v55f, v57a
    0x57d: JUMP v267(0xbe4)

    Begin block 0xbe4
    prev=[0x550], succ=[]
    =================================
    0xbe5: STOP 

}

function transferOwnership(address)() public {
    Begin block 0x292
    prev=[], succ=[0x29a, 0x29e]
    =================================
    0x293: v293 = CALLVALUE 
    0x295: v295 = ISZERO v293
    0x296: v296(0x29e) = CONST 
    0x299: JUMPI v296(0x29e), v295

    Begin block 0x29a
    prev=[0x292], succ=[]
    =================================
    0x29a: v29a(0x0) = CONST 
    0x29d: REVERT v29a(0x0), v29a(0x0)

    Begin block 0x29e
    prev=[0x292], succ=[0x2b1, 0x2b5]
    =================================
    0x2a0: v2a0(0xc05) = CONST 
    0x2a3: v2a3(0x4) = CONST 
    0x2a6: v2a6 = CALLDATASIZE 
    0x2a7: v2a7 = SUB v2a6, v2a3(0x4)
    0x2a8: v2a8(0x20) = CONST 
    0x2ab: v2ab = LT v2a7, v2a8(0x20)
    0x2ac: v2ac = ISZERO v2ab
    0x2ad: v2ad(0x2b5) = CONST 
    0x2b0: JUMPI v2ad(0x2b5), v2ac

    Begin block 0x2b1
    prev=[0x29e], succ=[]
    =================================
    0x2b1: v2b1(0x0) = CONST 
    0x2b4: REVERT v2b1(0x0), v2b1(0x0)

    Begin block 0x2b5
    prev=[0x29e], succ=[0x57e]
    =================================
    0x2b7: v2b7 = CALLDATALOAD v2a3(0x4)
    0x2b8: v2b8(0x1) = CONST 
    0x2ba: v2ba(0x1) = CONST 
    0x2bc: v2bc(0xa0) = CONST 
    0x2be: v2be(0x10000000000000000000000000000000000000000) = SHL v2bc(0xa0), v2ba(0x1)
    0x2bf: v2bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2be(0x10000000000000000000000000000000000000000), v2b8(0x1)
    0x2c0: v2c0 = AND v2bf(0xffffffffffffffffffffffffffffffffffffffff), v2b7
    0x2c1: v2c1(0x57e) = CONST 
    0x2c4: JUMP v2c1(0x57e)

    Begin block 0x57e
    prev=[0x2b5], succ=[0x4f8B0x57e]
    =================================
    0x57f: v57f(0x586) = CONST 
    0x582: v582(0x4f8) = CONST 
    0x585: JUMP v582(0x4f8)

    Begin block 0x4f8B0x57e
    prev=[0x57e], succ=[0x586]
    =================================
    0x4f9S0x57e: v4f9V57e(0x0) = CONST 
    0x4fbS0x57e: v4fbV57e = SLOAD v4f9V57e(0x0)
    0x4fcS0x57e: v4fcV57e(0x1) = CONST 
    0x4feS0x57e: v4feV57e(0x1) = CONST 
    0x500S0x57e: v500V57e(0xa0) = CONST 
    0x502S0x57e: v502V57e(0x10000000000000000000000000000000000000000) = SHL v500V57e(0xa0), v4feV57e(0x1)
    0x503S0x57e: v503V57e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502V57e(0x10000000000000000000000000000000000000000), v4fcV57e(0x1)
    0x504S0x57e: v504V57e = AND v503V57e(0xffffffffffffffffffffffffffffffffffffffff), v4fbV57e
    0x505S0x57e: v505V57e = CALLER 
    0x506S0x57e: v506V57e = EQ v505V57e, v504V57e
    0x508S0x57e: JUMP v57f(0x586)

    Begin block 0x586
    prev=[0x4f8B0x57e], succ=[0x58b, 0x5c5]
    =================================
    0x587: v587(0x5c5) = CONST 
    0x58a: JUMPI v587(0x5c5), v506V57e

    Begin block 0x58b
    prev=[0x586], succ=[]
    =================================
    0x58b: v58b(0x40) = CONST 
    0x58e: v58e = MLOAD v58b(0x40)
    0x58f: v58f(0x461bcd) = CONST 
    0x593: v593(0xe5) = CONST 
    0x595: v595(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v593(0xe5), v58f(0x461bcd)
    0x597: MSTORE v58e, v595(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x598: v598(0x20) = CONST 
    0x59a: v59a(0x4) = CONST 
    0x59d: v59d = ADD v58e, v59a(0x4)
    0x5a0: MSTORE v59d, v598(0x20)
    0x5a1: v5a1(0x24) = CONST 
    0x5a4: v5a4 = ADD v58e, v5a1(0x24)
    0x5a5: MSTORE v5a4, v598(0x20)
    0x5a6: v5a6(0x0) = CONST 
    0x5a9: v5a9 = MLOAD v5a6(0x0)
    0x5aa: v5aa(0x20) = CONST 
    0x5ac: v5ac(0x95c) = CONST 
    0x5b4: MSTORE v5a6(0x0), v5a9
    0x5b5: v5b5(0x44) = CONST 
    0x5b8: v5b8 = ADD v58e, v5b5(0x44)
    0x5b9: MSTORE v5b8, vd06(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x5bb: v5bb = MLOAD v58b(0x40)
    0x5bf: v5bf(0x0) = SUB v58e, v5bb
    0x5c0: v5c0(0x64) = CONST 
    0x5c2: v5c2(0x64) = ADD v5c0(0x64), v5bf(0x0)
    0x5c4: REVERT v5bb, v5c2(0x64)
    0xd06: vd06(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x5c5
    prev=[0x586], succ=[0x83a]
    =================================
    0x5c6: v5c6(0x5ce) = CONST 
    0x5ca: v5ca(0x83a) = CONST 
    0x5cd: JUMP v5ca(0x83a)

    Begin block 0x83a
    prev=[0x5c5], succ=[0x849, 0x87f]
    =================================
    0x83b: v83b(0x1) = CONST 
    0x83d: v83d(0x1) = CONST 
    0x83f: v83f(0xa0) = CONST 
    0x841: v841(0x10000000000000000000000000000000000000000) = SHL v83f(0xa0), v83d(0x1)
    0x842: v842(0xffffffffffffffffffffffffffffffffffffffff) = SUB v841(0x10000000000000000000000000000000000000000), v83b(0x1)
    0x844: v844 = AND v2c0, v842(0xffffffffffffffffffffffffffffffffffffffff)
    0x845: v845(0x87f) = CONST 
    0x848: JUMPI v845(0x87f), v844

    Begin block 0x849
    prev=[0x83a], succ=[]
    =================================
    0x849: v849(0x40) = CONST 
    0x84b: v84b = MLOAD v849(0x40)
    0x84c: v84c(0x461bcd) = CONST 
    0x850: v850(0xe5) = CONST 
    0x852: v852(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v850(0xe5), v84c(0x461bcd)
    0x854: MSTORE v84b, v852(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x855: v855(0x4) = CONST 
    0x857: v857 = ADD v855(0x4), v84b
    0x85a: v85a(0x20) = CONST 
    0x85c: v85c = ADD v85a(0x20), v857
    0x85f: v85f(0x20) = SUB v85c, v857
    0x861: MSTORE v857, v85f(0x20)
    0x862: v862(0x26) = CONST 
    0x865: MSTORE v85c, v862(0x26)
    0x866: v866(0x20) = CONST 
    0x868: v868 = ADD v866(0x20), v85c
    0x86a: v86a(0x8e5) = CONST 
    0x86d: v86d(0x26) = CONST 
    0x870: CODECOPY v868, v86a(0x8e5), v86d(0x26)
    0x871: v871(0x40) = CONST 
    0x873: v873 = ADD v871(0x40), v868
    0x877: v877(0x40) = CONST 
    0x879: v879 = MLOAD v877(0x40)
    0x87c: v87c(0x84) = SUB v873, v879
    0x87e: REVERT v879, v87c(0x84)

    Begin block 0x87f
    prev=[0x83a], succ=[0x5ce]
    =================================
    0x880: v880(0x0) = CONST 
    0x883: v883 = SLOAD v880(0x0)
    0x884: v884(0x40) = CONST 
    0x886: v886 = MLOAD v884(0x40)
    0x887: v887(0x1) = CONST 
    0x889: v889(0x1) = CONST 
    0x88b: v88b(0xa0) = CONST 
    0x88d: v88d(0x10000000000000000000000000000000000000000) = SHL v88b(0xa0), v889(0x1)
    0x88e: v88e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v88d(0x10000000000000000000000000000000000000000), v887(0x1)
    0x891: v891 = AND v2c0, v88e(0xffffffffffffffffffffffffffffffffffffffff)
    0x894: v894 = AND v883, v88e(0xffffffffffffffffffffffffffffffffffffffff)
    0x896: v896(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x8b8: LOG3 v886, v880(0x0), v896(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v894, v891
    0x8b9: v8b9(0x0) = CONST 
    0x8bc: v8bc = SLOAD v8b9(0x0)
    0x8bd: v8bd(0x1) = CONST 
    0x8bf: v8bf(0x1) = CONST 
    0x8c1: v8c1(0xa0) = CONST 
    0x8c3: v8c3(0x10000000000000000000000000000000000000000) = SHL v8c1(0xa0), v8bf(0x1)
    0x8c4: v8c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8c3(0x10000000000000000000000000000000000000000), v8bd(0x1)
    0x8c5: v8c5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v8c4(0xffffffffffffffffffffffffffffffffffffffff)
    0x8c6: v8c6 = AND v8c5(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v8bc
    0x8c7: v8c7(0x1) = CONST 
    0x8c9: v8c9(0x1) = CONST 
    0x8cb: v8cb(0xa0) = CONST 
    0x8cd: v8cd(0x10000000000000000000000000000000000000000) = SHL v8cb(0xa0), v8c9(0x1)
    0x8ce: v8ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8cd(0x10000000000000000000000000000000000000000), v8c7(0x1)
    0x8d2: v8d2 = AND v8ce(0xffffffffffffffffffffffffffffffffffffffff), v2c0
    0x8d6: v8d6 = OR v8d2, v8c6
    0x8d8: SSTORE v8b9(0x0), v8d6
    0x8d9: JUMP v5c6(0x5ce)

    Begin block 0x5ce
    prev=[0x87f], succ=[0xc05]
    =================================
    0x5d0: JUMP v2a0(0xc05)

    Begin block 0xc05
    prev=[0x5ce], succ=[]
    =================================
    0xc06: STOP 

}

function setHalt(bool)() public {
    Begin block 0x2c5
    prev=[], succ=[0x2cd, 0x2d1]
    =================================
    0x2c6: v2c6 = CALLVALUE 
    0x2c8: v2c8 = ISZERO v2c6
    0x2c9: v2c9(0x2d1) = CONST 
    0x2cc: JUMPI v2c9(0x2d1), v2c8

    Begin block 0x2cd
    prev=[0x2c5], succ=[]
    =================================
    0x2cd: v2cd(0x0) = CONST 
    0x2d0: REVERT v2cd(0x0), v2cd(0x0)

    Begin block 0x2d1
    prev=[0x2c5], succ=[0x2e4, 0x2e8]
    =================================
    0x2d3: v2d3(0xc26) = CONST 
    0x2d6: v2d6(0x4) = CONST 
    0x2d9: v2d9 = CALLDATASIZE 
    0x2da: v2da = SUB v2d9, v2d6(0x4)
    0x2db: v2db(0x20) = CONST 
    0x2de: v2de = LT v2da, v2db(0x20)
    0x2df: v2df = ISZERO v2de
    0x2e0: v2e0(0x2e8) = CONST 
    0x2e3: JUMPI v2e0(0x2e8), v2df

    Begin block 0x2e4
    prev=[0x2d1], succ=[]
    =================================
    0x2e4: v2e4(0x0) = CONST 
    0x2e7: REVERT v2e4(0x0), v2e4(0x0)

    Begin block 0x2e8
    prev=[0x2d1], succ=[0x5d1]
    =================================
    0x2ea: v2ea = CALLDATALOAD v2d6(0x4)
    0x2eb: v2eb = ISZERO v2ea
    0x2ec: v2ec = ISZERO v2eb
    0x2ed: v2ed(0x5d1) = CONST 
    0x2f0: JUMP v2ed(0x5d1)

    Begin block 0x5d1
    prev=[0x2e8], succ=[0x4f8B0x5d1]
    =================================
    0x5d2: v5d2(0x5d9) = CONST 
    0x5d5: v5d5(0x4f8) = CONST 
    0x5d8: JUMP v5d5(0x4f8)

    Begin block 0x4f8B0x5d1
    prev=[0x5d1], succ=[0x5d9]
    =================================
    0x4f9S0x5d1: v4f9V5d1(0x0) = CONST 
    0x4fbS0x5d1: v4fbV5d1 = SLOAD v4f9V5d1(0x0)
    0x4fcS0x5d1: v4fcV5d1(0x1) = CONST 
    0x4feS0x5d1: v4feV5d1(0x1) = CONST 
    0x500S0x5d1: v500V5d1(0xa0) = CONST 
    0x502S0x5d1: v502V5d1(0x10000000000000000000000000000000000000000) = SHL v500V5d1(0xa0), v4feV5d1(0x1)
    0x503S0x5d1: v503V5d1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v502V5d1(0x10000000000000000000000000000000000000000), v4fcV5d1(0x1)
    0x504S0x5d1: v504V5d1 = AND v503V5d1(0xffffffffffffffffffffffffffffffffffffffff), v4fbV5d1
    0x505S0x5d1: v505V5d1 = CALLER 
    0x506S0x5d1: v506V5d1 = EQ v505V5d1, v504V5d1
    0x508S0x5d1: JUMP v5d2(0x5d9)

    Begin block 0x5d9
    prev=[0x4f8B0x5d1], succ=[0x5de, 0x618]
    =================================
    0x5da: v5da(0x618) = CONST 
    0x5dd: JUMPI v5da(0x618), v506V5d1

    Begin block 0x5de
    prev=[0x5d9], succ=[]
    =================================
    0x5de: v5de(0x40) = CONST 
    0x5e1: v5e1 = MLOAD v5de(0x40)
    0x5e2: v5e2(0x461bcd) = CONST 
    0x5e6: v5e6(0xe5) = CONST 
    0x5e8: v5e8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5e6(0xe5), v5e2(0x461bcd)
    0x5ea: MSTORE v5e1, v5e8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x5eb: v5eb(0x20) = CONST 
    0x5ed: v5ed(0x4) = CONST 
    0x5f0: v5f0 = ADD v5e1, v5ed(0x4)
    0x5f3: MSTORE v5f0, v5eb(0x20)
    0x5f4: v5f4(0x24) = CONST 
    0x5f7: v5f7 = ADD v5e1, v5f4(0x24)
    0x5f8: MSTORE v5f7, v5eb(0x20)
    0x5f9: v5f9(0x0) = CONST 
    0x5fc: v5fc = MLOAD v5f9(0x0)
    0x5fd: v5fd(0x20) = CONST 
    0x5ff: v5ff(0x95c) = CONST 
    0x607: MSTORE v5f9(0x0), v5fc
    0x608: v608(0x44) = CONST 
    0x60b: v60b = ADD v5e1, v608(0x44)
    0x60c: MSTORE v60b, vd0b(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x60e: v60e = MLOAD v5de(0x40)
    0x612: v612(0x0) = SUB v5e1, v60e
    0x613: v613(0x64) = CONST 
    0x615: v615(0x64) = ADD v613(0x64), v612(0x0)
    0x617: REVERT v60e, v615(0x64)
    0xd0b: vd0b(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 

    Begin block 0x618
    prev=[0x5d9], succ=[0xc26]
    =================================
    0x619: v619(0x2) = CONST 
    0x61c: v61c = SLOAD v619(0x2)
    0x61d: v61d(0xff) = CONST 
    0x61f: v61f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v61d(0xff)
    0x620: v620 = AND v61f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v61c
    0x622: v622 = ISZERO v2ec
    0x623: v623 = ISZERO v622
    0x627: v627 = OR v623, v620
    0x629: SSTORE v619(0x2), v627
    0x62a: JUMP v2d3(0xc26)

    Begin block 0xc26
    prev=[0x618], succ=[]
    =================================
    0xc27: STOP 

}

function fallback()() public {
    Begin block 0xc2
    prev=[], succ=[0x2f1]
    =================================
    0xc3: vc3(0xa5a) = CONST 
    0xc6: vc6(0x2f1) = CONST 
    0xc9: JUMP vc6(0x2f1)

    Begin block 0x2f1
    prev=[0xc2], succ=[0xc47B0x2f1]
    =================================
    0x2f2: v2f2(0x2f9) = CONST 
    0x2f5: v2f5(0xc47) = CONST 
    0x2f8: JUMP v2f5(0xc47), v2f2(0x2f9)

    Begin block 0xc47B0x2f1
    prev=[0x2f1], succ=[0x2f9]
    =================================
    0xc48S0x2f1: JUMP v2f2(0x2f9)

    Begin block 0x2f9
    prev=[0xc47B0x2f1], succ=[0x62bB0x2f9]
    =================================
    0x2fa: v2fa(0xc68) = CONST 
    0x2fd: v2fd(0x304) = CONST 
    0x300: v300(0x62b) = CONST 
    0x303: JUMP v300(0x62b)

    Begin block 0x62bB0x2f9
    prev=[0x2f9], succ=[0x304]
    =================================
    0x62cS0x2f9: v62cV2f9(0x0) = CONST 
    0x62fS0x2f9: v62fV2f9(0x40) = CONST 
    0x631S0x2f9: v631V2f9 = MLOAD v62fV2f9(0x40)
    0x634S0x2f9: v634V2f9(0x97c) = CONST 
    0x637S0x2f9: v637V2f9(0x23) = CONST 
    0x63aS0x2f9: CODECOPY v631V2f9, v634V2f9(0x97c), v637V2f9(0x23)
    0x63bS0x2f9: v63bV2f9(0x40) = CONST 
    0x63dS0x2f9: v63dV2f9 = MLOAD v63bV2f9(0x40)
    0x641S0x2f9: v641V2f9(0x0) = SUB v631V2f9, v63dV2f9
    0x642S0x2f9: v642V2f9(0x23) = CONST 
    0x644S0x2f9: v644V2f9(0x23) = ADD v642V2f9(0x23), v641V2f9(0x0)
    0x646S0x2f9: v646V2f9 = SHA3 v63dV2f9, v644V2f9(0x23)
    0x647S0x2f9: v647V2f9 = SLOAD v646V2f9
    0x64dS0x2f9: JUMP v2fd(0x304)

    Begin block 0x304
    prev=[0x62bB0x2f9], succ=[0x64e]
    =================================
    0x305: v305(0x64e) = CONST 
    0x308: JUMP v305(0x64e)

    Begin block 0x64e
    prev=[0x304], succ=[0x669, 0x66d]
    =================================
    0x64f: v64f = CALLDATASIZE 
    0x650: v650(0x0) = CONST 
    0x653: CALLDATACOPY v650(0x0), v650(0x0), v64f
    0x654: v654(0x0) = CONST 
    0x657: v657 = CALLDATASIZE 
    0x658: v658(0x0) = CONST 
    0x65b: v65b = GAS 
    0x65c: v65c = DELEGATECALL v65b, v647V2f9, v658(0x0), v657, v654(0x0), v654(0x0)
    0x65d: v65d = RETURNDATASIZE 
    0x65e: v65e(0x0) = CONST 
    0x661: RETURNDATACOPY v65e(0x0), v65e(0x0), v65d
    0x664: v664 = ISZERO v65c
    0x665: v665(0x66d) = CONST 
    0x668: JUMPI v665(0x66d), v664

    Begin block 0x669
    prev=[0x64e], succ=[]
    =================================
    0x669: v669 = RETURNDATASIZE 
    0x66a: v66a(0x0) = CONST 
    0x66c: RETURN v66a(0x0), v669

    Begin block 0x66d
    prev=[0x64e], succ=[]
    =================================
    0x66e: v66e = RETURNDATASIZE 
    0x66f: v66f(0x0) = CONST 
    0x671: REVERT v66f(0x0), v66e

}

function getOperator(uint256)() public {
    Begin block 0xcc
    prev=[], succ=[0xd4, 0xd8]
    =================================
    0xcd: vcd = CALLVALUE 
    0xcf: vcf = ISZERO vcd
    0xd0: vd0(0xd8) = CONST 
    0xd3: JUMPI vd0(0xd8), vcf

    Begin block 0xd4
    prev=[0xcc], succ=[]
    =================================
    0xd4: vd4(0x0) = CONST 
    0xd7: REVERT vd4(0x0), vd4(0x0)

    Begin block 0xd8
    prev=[0xcc], succ=[0xeb, 0xef]
    =================================
    0xda: vda(0xa7b) = CONST 
    0xdd: vdd(0x4) = CONST 
    0xe0: ve0 = CALLDATASIZE 
    0xe1: ve1 = SUB ve0, vdd(0x4)
    0xe2: ve2(0x20) = CONST 
    0xe5: ve5 = LT ve1, ve2(0x20)
    0xe6: ve6 = ISZERO ve5
    0xe7: ve7(0xef) = CONST 
    0xea: JUMPI ve7(0xef), ve6

    Begin block 0xeb
    prev=[0xd8], succ=[]
    =================================
    0xeb: veb(0x0) = CONST 
    0xee: REVERT veb(0x0), veb(0x0)

    Begin block 0xef
    prev=[0xd8], succ=[0x30b]
    =================================
    0xf1: vf1 = CALLDATALOAD vdd(0x4)
    0xf2: vf2(0x30b) = CONST 
    0xf5: JUMP vf2(0x30b)

    Begin block 0x30b
    prev=[0xef], succ=[0xa7b]
    =================================
    0x30c: v30c(0x0) = CONST 
    0x310: MSTORE v30c(0x0), vf1
    0x311: v311(0x1) = CONST 
    0x313: v313(0x20) = CONST 
    0x315: MSTORE v313(0x20), v311(0x1)
    0x316: v316(0x40) = CONST 
    0x319: v319 = SHA3 v30c(0x0), v316(0x40)
    0x31a: v31a = SLOAD v319
    0x31b: v31b(0x1) = CONST 
    0x31d: v31d(0x1) = CONST 
    0x31f: v31f(0xa0) = CONST 
    0x321: v321(0x10000000000000000000000000000000000000000) = SHL v31f(0xa0), v31d(0x1)
    0x322: v322(0xffffffffffffffffffffffffffffffffffffffff) = SUB v321(0x10000000000000000000000000000000000000000), v31b(0x1)
    0x323: v323 = AND v322(0xffffffffffffffffffffffffffffffffffffffff), v31a
    0x325: JUMP vda(0xa7b)

    Begin block 0xa7b
    prev=[0x30b], succ=[]
    =================================
    0xa7c: va7c(0x40) = CONST 
    0xa7f: va7f = MLOAD va7c(0x40)
    0xa80: va80(0x1) = CONST 
    0xa82: va82(0x1) = CONST 
    0xa84: va84(0xa0) = CONST 
    0xa86: va86(0x10000000000000000000000000000000000000000) = SHL va84(0xa0), va82(0x1)
    0xa87: va87(0xffffffffffffffffffffffffffffffffffffffff) = SUB va86(0x10000000000000000000000000000000000000000), va80(0x1)
    0xa8a: va8a = AND v323, va87(0xffffffffffffffffffffffffffffffffffffffff)
    0xa8c: MSTORE va7f, va8a
    0xa8d: va8d = MLOAD va7c(0x40)
    0xa91: va91(0x0) = SUB va7f, va8d
    0xa92: va92(0x20) = CONST 
    0xa94: va94(0x20) = ADD va92(0x20), va91(0x0)
    0xa96: RETURN va8d, va94(0x20)

}

