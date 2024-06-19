function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8cd]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x8c1: v8c1(0x8cd) = CONST 
    0x8c2: JUMPI v8c1(0x8cd), v8

    Begin block 0xd
    prev=[0x0], succ=[0x8d0, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x3659cfe6) = CONST 
    0x19: v19 = EQ v14(0x3659cfe6), v12
    0x8c3: v8c3(0x8d0) = CONST 
    0x8c4: JUMPI v8c3(0x8d0), v19

    Begin block 0x8d0
    prev=[0xd], succ=[]
    =================================
    0x8d1: v8d1(0x54) = CONST 
    0x8d2: CALLPRIVATE v8d1(0x54)

    Begin block 0x1e
    prev=[0xd], succ=[0x8d3, 0x29]
    =================================
    0x1f: v1f(0x4f1ef286) = CONST 
    0x24: v24 = EQ v1f(0x4f1ef286), v12
    0x8c5: v8c5(0x8d3) = CONST 
    0x8c6: JUMPI v8c5(0x8d3), v24

    Begin block 0x8d3
    prev=[0x1e], succ=[]
    =================================
    0x8d4: v8d4(0xa5) = CONST 
    0x8d5: CALLPRIVATE v8d4(0xa5)

    Begin block 0x29
    prev=[0x1e], succ=[0x8d6, 0x34]
    =================================
    0x2a: v2a(0x5c60da1b) = CONST 
    0x2f: v2f = EQ v2a(0x5c60da1b), v12
    0x8c7: v8c7(0x8d6) = CONST 
    0x8c8: JUMPI v8c7(0x8d6), v2f

    Begin block 0x8d6
    prev=[0x29], succ=[]
    =================================
    0x8d7: v8d7(0x13e) = CONST 
    0x8d8: CALLPRIVATE v8d7(0x13e)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x8d9]
    =================================
    0x35: v35(0x8f283970) = CONST 
    0x3a: v3a = EQ v35(0x8f283970), v12
    0x8c9: v8c9(0x8d9) = CONST 
    0x8ca: JUMPI v8c9(0x8d9), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x8cd, 0x8dc]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x8cb: v8cb(0x8dc) = CONST 
    0x8cc: JUMPI v8cb(0x8dc), v45

    Begin block 0x8cd
    prev=[0x0, 0x3f], succ=[]
    =================================
    0x8ce: v8ce(0x4a) = CONST 
    0x8cf: CALLPRIVATE v8ce(0x4a)

    Begin block 0x8dc
    prev=[0x3f], succ=[]
    =================================
    0x8dd: v8dd(0x1e6) = CONST 
    0x8de: CALLPRIVATE v8dd(0x1e6)

    Begin block 0x8d9
    prev=[0x34], succ=[]
    =================================
    0x8da: v8da(0x195) = CONST 
    0x8db: CALLPRIVATE v8da(0x195)

}

function implementation()() public {
    Begin block 0x13e
    prev=[], succ=[0x146, 0x14a]
    =================================
    0x13f: v13f = CALLVALUE 
    0x141: v141 = ISZERO v13f
    0x142: v142(0x14a) = CONST 
    0x145: JUMPI v142(0x14a), v141

    Begin block 0x146
    prev=[0x13e], succ=[]
    =================================
    0x146: v146(0x0) = CONST 
    0x149: REVERT v146(0x0), v146(0x0)

    Begin block 0x14a
    prev=[0x13e], succ=[0x153]
    =================================
    0x14c: v14c(0x153) = CONST 
    0x14f: v14f(0x382) = CONST 
    0x152: v152_0 = CALLPRIVATE v14f(0x382), v14c(0x153)

    Begin block 0x153
    prev=[0x14a], succ=[]
    =================================
    0x154: v154(0x40) = CONST 
    0x156: v156 = MLOAD v154(0x40)
    0x159: v159(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x16e: v16e = AND v159(0xffffffffffffffffffffffffffffffffffffffff), v152_0
    0x16f: v16f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x184: v184 = AND v16f(0xffffffffffffffffffffffffffffffffffffffff), v16e
    0x186: MSTORE v156, v184
    0x187: v187(0x20) = CONST 
    0x189: v189 = ADD v187(0x20), v156
    0x18d: v18d(0x40) = CONST 
    0x18f: v18f = MLOAD v18d(0x40)
    0x192: v192(0x20) = SUB v189, v18f
    0x194: RETURN v18f, v192(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x195
    prev=[], succ=[0x19d, 0x1a1]
    =================================
    0x196: v196 = CALLVALUE 
    0x198: v198 = ISZERO v196
    0x199: v199(0x1a1) = CONST 
    0x19c: JUMPI v199(0x1a1), v198

    Begin block 0x19d
    prev=[0x195], succ=[]
    =================================
    0x19d: v19d(0x0) = CONST 
    0x1a0: REVERT v19d(0x0), v19d(0x0)

    Begin block 0x1a1
    prev=[0x195], succ=[0x1b4, 0x1b8]
    =================================
    0x1a3: v1a3(0x1e4) = CONST 
    0x1a6: v1a6(0x4) = CONST 
    0x1a9: v1a9 = CALLDATASIZE 
    0x1aa: v1aa = SUB v1a9, v1a6(0x4)
    0x1ab: v1ab(0x20) = CONST 
    0x1ae: v1ae = LT v1aa, v1ab(0x20)
    0x1af: v1af = ISZERO v1ae
    0x1b0: v1b0(0x1b8) = CONST 
    0x1b3: JUMPI v1b0(0x1b8), v1af

    Begin block 0x1b4
    prev=[0x1a1], succ=[]
    =================================
    0x1b4: v1b4(0x0) = CONST 
    0x1b7: REVERT v1b4(0x0), v1b4(0x0)

    Begin block 0x1b8
    prev=[0x1a1], succ=[0x3da]
    =================================
    0x1ba: v1ba = ADD v1a6(0x4), v1aa
    0x1be: v1be = CALLDATALOAD v1a6(0x4)
    0x1bf: v1bf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d4: v1d4 = AND v1bf(0xffffffffffffffffffffffffffffffffffffffff), v1be
    0x1d6: v1d6(0x20) = CONST 
    0x1d8: v1d8(0x24) = ADD v1d6(0x20), v1a6(0x4)
    0x1e0: v1e0(0x3da) = CONST 
    0x1e3: JUMP v1e0(0x3da)

    Begin block 0x3da
    prev=[0x1b8], succ=[0x698B0x3da]
    =================================
    0x3db: v3db(0x3e2) = CONST 
    0x3de: v3de(0x698) = CONST 
    0x3e1: JUMP v3de(0x698)

    Begin block 0x698B0x3da
    prev=[0x3da], succ=[0x3e2]
    =================================
    0x699S0x3da: v699V3da(0x0) = CONST 
    0x69cS0x3da: v69cV3da(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x3da: v6bdV3da(0x0) = CONST 
    0x6bfS0x3da: v6bfV3da(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV3da(0x0), v69cV3da(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x3da: v6c3V3da = SLOAD v6bfV3da(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x3da: JUMP v3db(0x3e2)

    Begin block 0x3e2
    prev=[0x698B0x3da], succ=[0x416, 0x547]
    =================================
    0x3e3: v3e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3f8: v3f8 = AND v3e3(0xffffffffffffffffffffffffffffffffffffffff), v6c3V3da
    0x3f9: v3f9 = CALLER 
    0x3fa: v3fa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x40f: v40f = AND v3fa(0xffffffffffffffffffffffffffffffffffffffff), v3f9
    0x410: v410 = EQ v40f, v3f8
    0x411: v411 = ISZERO v410
    0x412: v412(0x547) = CONST 
    0x415: JUMPI v412(0x547), v411

    Begin block 0x416
    prev=[0x3e2], succ=[0x44b, 0x49b]
    =================================
    0x416: v416(0x0) = CONST 
    0x418: v418(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42d: v42d(0x0) = AND v418(0xffffffffffffffffffffffffffffffffffffffff), v416(0x0)
    0x42f: v42f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x444: v444 = AND v42f(0xffffffffffffffffffffffffffffffffffffffff), v1d4
    0x445: v445 = EQ v444, v42d(0x0)
    0x446: v446 = ISZERO v445
    0x447: v447(0x49b) = CONST 
    0x44a: JUMPI v447(0x49b), v446

    Begin block 0x44b
    prev=[0x416], succ=[]
    =================================
    0x44b: v44b(0x40) = CONST 
    0x44d: v44d = MLOAD v44b(0x40)
    0x44e: v44e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x470: MSTORE v44d, v44e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x471: v471(0x4) = CONST 
    0x473: v473 = ADD v471(0x4), v44d
    0x476: v476(0x20) = CONST 
    0x478: v478 = ADD v476(0x20), v473
    0x47b: v47b(0x20) = SUB v478, v473
    0x47d: MSTORE v473, v47b(0x20)
    0x47e: v47e(0x36) = CONST 
    0x481: MSTORE v478, v47e(0x36)
    0x482: v482(0x20) = CONST 
    0x484: v484 = ADD v482(0x20), v478
    0x486: v486(0x81c) = CONST 
    0x489: v489(0x36) = CONST 
    0x48c: CODECOPY v484, v486(0x81c), v489(0x36)
    0x48d: v48d(0x40) = CONST 
    0x48f: v48f = ADD v48d(0x40), v484
    0x493: v493(0x40) = CONST 
    0x495: v495 = MLOAD v493(0x40)
    0x498: v498(0x84) = SUB v48f, v495
    0x49a: REVERT v495, v498(0x84)

    Begin block 0x49b
    prev=[0x416], succ=[0x698B0x49b]
    =================================
    0x49c: v49c(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x4bd: v4bd(0x4c4) = CONST 
    0x4c0: v4c0(0x698) = CONST 
    0x4c3: JUMP v4c0(0x698)

    Begin block 0x698B0x49b
    prev=[0x49b], succ=[0x4c4]
    =================================
    0x699S0x49b: v699V49b(0x0) = CONST 
    0x69cS0x49b: v69cV49b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x49b: v6bdV49b(0x0) = CONST 
    0x6bfS0x49b: v6bfV49b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV49b(0x0), v69cV49b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x49b: v6c3V49b = SLOAD v6bfV49b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x49b: JUMP v4bd(0x4c4)

    Begin block 0x4c4
    prev=[0x698B0x49b], succ=[0x718]
    =================================
    0x4c6: v4c6(0x40) = CONST 
    0x4c8: v4c8 = MLOAD v4c6(0x40)
    0x4cb: v4cb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4e0: v4e0 = AND v4cb(0xffffffffffffffffffffffffffffffffffffffff), v6c3V49b
    0x4e1: v4e1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4f6: v4f6 = AND v4e1(0xffffffffffffffffffffffffffffffffffffffff), v4e0
    0x4f8: MSTORE v4c8, v4f6
    0x4f9: v4f9(0x20) = CONST 
    0x4fb: v4fb = ADD v4f9(0x20), v4c8
    0x4fd: v4fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x512: v512 = AND v4fd(0xffffffffffffffffffffffffffffffffffffffff), v1d4
    0x513: v513(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x528: v528 = AND v513(0xffffffffffffffffffffffffffffffffffffffff), v512
    0x52a: MSTORE v4fb, v528
    0x52b: v52b(0x20) = CONST 
    0x52d: v52d = ADD v52b(0x20), v4fb
    0x532: v532(0x40) = CONST 
    0x534: v534 = MLOAD v532(0x40)
    0x537: v537(0x40) = SUB v52d, v534
    0x539: LOG1 v534, v537(0x40), v49c(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x53a: v53a(0x542) = CONST 
    0x53e: v53e(0x718) = CONST 
    0x541: JUMP v53e(0x718)

    Begin block 0x718
    prev=[0x4c4], succ=[0x542]
    =================================
    0x719: v719(0x0) = CONST 
    0x71b: v71b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x73c: v73c(0x0) = CONST 
    0x73e: v73e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v73c(0x0), v71b(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x743: SSTORE v73e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b), v1d4
    0x746: JUMP v53a(0x542)

    Begin block 0x542
    prev=[0x718], succ=[0x550]
    =================================
    0x543: v543(0x550) = CONST 
    0x546: JUMP v543(0x550)

    Begin block 0x550
    prev=[0x542], succ=[0x1e4]
    =================================
    0x552: JUMP v1a3(0x1e4)

    Begin block 0x1e4
    prev=[0x550], succ=[]
    =================================
    0x1e5: STOP 

    Begin block 0x547
    prev=[0x3e2], succ=[0x23d0x195]
    =================================
    0x548: v548(0x54f) = CONST 
    0x54b: v54b(0x23d) = CONST 
    0x54e: JUMP v54b(0x23d)

    Begin block 0x23d0x195
    prev=[0x547], succ=[0x2450x195]
    =================================
    0x23e0x195: v19523e(0x245) = CONST 
    0x2410x195: v195241(0x5ab) = CONST 
    0x2440x195: CALLPRIVATE v195241(0x5ab), v19523e(0x245)

    Begin block 0x2450x195
    prev=[0x23d0x195], succ=[0x641B0x2450x195]
    =================================
    0x2460x195: v195246(0x255) = CONST 
    0x2490x195: v195249(0x250) = CONST 
    0x24c0x195: v19524c(0x641) = CONST 
    0x24f0x195: JUMP v19524c(0x641)

    Begin block 0x641B0x2450x195
    prev=[0x2450x195], succ=[0x2500x195]
    =================================
    0x642S0x2450x195: v642V245195(0x0) = CONST 
    0x645S0x2450x195: v645V245195(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450x195: v666V245195(0x0) = CONST 
    0x668S0x2450x195: v668V245195(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V245195(0x0), v645V245195(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450x195: v66cV245195 = SLOAD v668V245195(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450x195: JUMP v195249(0x250)

    Begin block 0x2500x195
    prev=[0x641B0x2450x195], succ=[0x6720x195]
    =================================
    0x2510x195: v195251(0x672) = CONST 
    0x2540x195: JUMP v195251(0x672)

    Begin block 0x6720x195
    prev=[0x2500x195], succ=[0x68f0x195, 0x6930x195]
    =================================
    0x6730x195: v195673 = CALLDATASIZE 
    0x6740x195: v195674(0x0) = CONST 
    0x6770x195: CALLDATACOPY v195674(0x0), v195674(0x0), v195673
    0x6780x195: v195678(0x0) = CONST 
    0x67b0x195: v19567b = CALLDATASIZE 
    0x67c0x195: v19567c(0x0) = CONST 
    0x67f0x195: v19567f = GAS 
    0x6800x195: v195680 = DELEGATECALL v19567f, v66cV245195, v19567c(0x0), v19567b, v195678(0x0), v195678(0x0)
    0x6810x195: v195681 = RETURNDATASIZE 
    0x6820x195: v195682(0x0) = CONST 
    0x6850x195: RETURNDATACOPY v195682(0x0), v195682(0x0), v195681
    0x6870x195: v195687(0x0) = CONST 
    0x68a0x195: v19568a = EQ v195680, v195687(0x0)
    0x68b0x195: v19568b(0x693) = CONST 
    0x68e0x195: JUMPI v19568b(0x693), v19568a

    Begin block 0x68f0x195
    prev=[0x6720x195], succ=[]
    =================================
    0x68f0x195: v19568f = RETURNDATASIZE 
    0x6900x195: v195690(0x0) = CONST 
    0x6920x195: RETURN v195690(0x0), v19568f

    Begin block 0x6930x195
    prev=[0x6720x195], succ=[]
    =================================
    0x6940x195: v195694 = RETURNDATASIZE 
    0x6950x195: v195695(0x0) = CONST 
    0x6970x195: REVERT v195695(0x0), v195694

}

function admin()() public {
    Begin block 0x1e6
    prev=[], succ=[0x1ee, 0x1f2]
    =================================
    0x1e7: v1e7 = CALLVALUE 
    0x1e9: v1e9 = ISZERO v1e7
    0x1ea: v1ea(0x1f2) = CONST 
    0x1ed: JUMPI v1ea(0x1f2), v1e9

    Begin block 0x1ee
    prev=[0x1e6], succ=[]
    =================================
    0x1ee: v1ee(0x0) = CONST 
    0x1f1: REVERT v1ee(0x0), v1ee(0x0)

    Begin block 0x1f2
    prev=[0x1e6], succ=[0x1fb]
    =================================
    0x1f4: v1f4(0x1fb) = CONST 
    0x1f7: v1f7(0x553) = CONST 
    0x1fa: v1fa_0 = CALLPRIVATE v1f7(0x553), v1f4(0x1fb)

    Begin block 0x1fb
    prev=[0x1f2], succ=[]
    =================================
    0x1fc: v1fc(0x40) = CONST 
    0x1fe: v1fe = MLOAD v1fc(0x40)
    0x201: v201(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x216: v216 = AND v201(0xffffffffffffffffffffffffffffffffffffffff), v1fa_0
    0x217: v217(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22c: v22c = AND v217(0xffffffffffffffffffffffffffffffffffffffff), v216
    0x22e: MSTORE v1fe, v22c
    0x22f: v22f(0x20) = CONST 
    0x231: v231 = ADD v22f(0x20), v1fe
    0x235: v235(0x40) = CONST 
    0x237: v237 = MLOAD v235(0x40)
    0x23a: v23a(0x20) = SUB v231, v237
    0x23c: RETURN v237, v23a(0x20)

}

function 0x382(0x382arg0x0) private {
    Begin block 0x382
    prev=[], succ=[0x698B0x382]
    =================================
    0x383: v383(0x0) = CONST 
    0x385: v385(0x38c) = CONST 
    0x388: v388(0x698) = CONST 
    0x38b: JUMP v388(0x698)

    Begin block 0x698B0x382
    prev=[0x382], succ=[0x38c]
    =================================
    0x699S0x382: v699V382(0x0) = CONST 
    0x69cS0x382: v69cV382(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x382: v6bdV382(0x0) = CONST 
    0x6bfS0x382: v6bfV382(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV382(0x0), v69cV382(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x382: v6c3V382 = SLOAD v6bfV382(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x382: JUMP v385(0x38c)

    Begin block 0x38c
    prev=[0x698B0x382], succ=[0x3c0, 0x3ce]
    =================================
    0x38d: v38d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a2: v3a2 = AND v38d(0xffffffffffffffffffffffffffffffffffffffff), v6c3V382
    0x3a3: v3a3 = CALLER 
    0x3a4: v3a4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b9: v3b9 = AND v3a4(0xffffffffffffffffffffffffffffffffffffffff), v3a3
    0x3ba: v3ba = EQ v3b9, v3a2
    0x3bb: v3bb = ISZERO v3ba
    0x3bc: v3bc(0x3ce) = CONST 
    0x3bf: JUMPI v3bc(0x3ce), v3bb

    Begin block 0x3c0
    prev=[0x38c], succ=[0x641B0x3c0]
    =================================
    0x3c0: v3c0(0x3c7) = CONST 
    0x3c3: v3c3(0x641) = CONST 
    0x3c6: JUMP v3c3(0x641)

    Begin block 0x641B0x3c0
    prev=[0x3c0], succ=[0x3c7]
    =================================
    0x642S0x3c0: v642V3c0(0x0) = CONST 
    0x645S0x3c0: v645V3c0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x3c0: v666V3c0(0x0) = CONST 
    0x668S0x3c0: v668V3c0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V3c0(0x0), v645V3c0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x3c0: v66cV3c0 = SLOAD v668V3c0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x3c0: JUMP v3c0(0x3c7)

    Begin block 0x3c7
    prev=[0x641B0x3c0], succ=[0x3d7]
    =================================
    0x3ca: v3ca(0x3d7) = CONST 
    0x3cd: JUMP v3ca(0x3d7)

    Begin block 0x3d7
    prev=[0x3c7], succ=[]
    =================================
    0x3d9: RETURNPRIVATE v382arg0, v66cV3c0

    Begin block 0x3ce
    prev=[0x38c], succ=[0x23d0x382]
    =================================
    0x3cf: v3cf(0x3d6) = CONST 
    0x3d2: v3d2(0x23d) = CONST 
    0x3d5: JUMP v3d2(0x23d)

    Begin block 0x23d0x382
    prev=[0x3ce], succ=[0x2450x382]
    =================================
    0x23e0x382: v38223e(0x245) = CONST 
    0x2410x382: v382241(0x5ab) = CONST 
    0x2440x382: CALLPRIVATE v382241(0x5ab), v38223e(0x245)

    Begin block 0x2450x382
    prev=[0x23d0x382], succ=[0x641B0x2450x382]
    =================================
    0x2460x382: v382246(0x255) = CONST 
    0x2490x382: v382249(0x250) = CONST 
    0x24c0x382: v38224c(0x641) = CONST 
    0x24f0x382: JUMP v38224c(0x641)

    Begin block 0x641B0x2450x382
    prev=[0x2450x382], succ=[0x2500x382]
    =================================
    0x642S0x2450x382: v642V245382(0x0) = CONST 
    0x645S0x2450x382: v645V245382(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450x382: v666V245382(0x0) = CONST 
    0x668S0x2450x382: v668V245382(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V245382(0x0), v645V245382(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450x382: v66cV245382 = SLOAD v668V245382(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450x382: JUMP v382249(0x250)

    Begin block 0x2500x382
    prev=[0x641B0x2450x382], succ=[0x6720x382]
    =================================
    0x2510x382: v382251(0x672) = CONST 
    0x2540x382: JUMP v382251(0x672)

    Begin block 0x6720x382
    prev=[0x2500x382], succ=[0x68f0x382, 0x6930x382]
    =================================
    0x6730x382: v382673 = CALLDATASIZE 
    0x6740x382: v382674(0x0) = CONST 
    0x6770x382: CALLDATACOPY v382674(0x0), v382674(0x0), v382673
    0x6780x382: v382678(0x0) = CONST 
    0x67b0x382: v38267b = CALLDATASIZE 
    0x67c0x382: v38267c(0x0) = CONST 
    0x67f0x382: v38267f = GAS 
    0x6800x382: v382680 = DELEGATECALL v38267f, v66cV245382, v38267c(0x0), v38267b, v382678(0x0), v382678(0x0)
    0x6810x382: v382681 = RETURNDATASIZE 
    0x6820x382: v382682(0x0) = CONST 
    0x6850x382: RETURNDATACOPY v382682(0x0), v382682(0x0), v382681
    0x6870x382: v382687(0x0) = CONST 
    0x68a0x382: v38268a = EQ v382680, v382687(0x0)
    0x68b0x382: v38268b(0x693) = CONST 
    0x68e0x382: JUMPI v38268b(0x693), v38268a

    Begin block 0x68f0x382
    prev=[0x6720x382], succ=[]
    =================================
    0x68f0x382: v38268f = RETURNDATASIZE 
    0x6900x382: v382690(0x0) = CONST 
    0x6920x382: RETURN v382690(0x0), v38268f

    Begin block 0x6930x382
    prev=[0x6720x382], succ=[]
    =================================
    0x6940x382: v382694 = RETURNDATASIZE 
    0x6950x382: v382695(0x0) = CONST 
    0x6970x382: REVERT v382695(0x0), v382694

}

function fallback()() public {
    Begin block 0x4a
    prev=[], succ=[0x23d0x4a]
    =================================
    0x4b: v4b(0x52) = CONST 
    0x4e: v4e(0x23d) = CONST 
    0x51: JUMP v4e(0x23d)

    Begin block 0x23d0x4a
    prev=[0x4a], succ=[0x2450x4a]
    =================================
    0x23e0x4a: v4a23e(0x245) = CONST 
    0x2410x4a: v4a241(0x5ab) = CONST 
    0x2440x4a: CALLPRIVATE v4a241(0x5ab), v4a23e(0x245)

    Begin block 0x2450x4a
    prev=[0x23d0x4a], succ=[0x641B0x2450x4a]
    =================================
    0x2460x4a: v4a246(0x255) = CONST 
    0x2490x4a: v4a249(0x250) = CONST 
    0x24c0x4a: v4a24c(0x641) = CONST 
    0x24f0x4a: JUMP v4a24c(0x641)

    Begin block 0x641B0x2450x4a
    prev=[0x2450x4a], succ=[0x2500x4a]
    =================================
    0x642S0x2450x4a: v642V2454a(0x0) = CONST 
    0x645S0x2450x4a: v645V2454a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450x4a: v666V2454a(0x0) = CONST 
    0x668S0x2450x4a: v668V2454a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V2454a(0x0), v645V2454a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450x4a: v66cV2454a = SLOAD v668V2454a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450x4a: JUMP v4a249(0x250)

    Begin block 0x2500x4a
    prev=[0x641B0x2450x4a], succ=[0x6720x4a]
    =================================
    0x2510x4a: v4a251(0x672) = CONST 
    0x2540x4a: JUMP v4a251(0x672)

    Begin block 0x6720x4a
    prev=[0x2500x4a], succ=[0x68f0x4a, 0x6930x4a]
    =================================
    0x6730x4a: v4a673 = CALLDATASIZE 
    0x6740x4a: v4a674(0x0) = CONST 
    0x6770x4a: CALLDATACOPY v4a674(0x0), v4a674(0x0), v4a673
    0x6780x4a: v4a678(0x0) = CONST 
    0x67b0x4a: v4a67b = CALLDATASIZE 
    0x67c0x4a: v4a67c(0x0) = CONST 
    0x67f0x4a: v4a67f = GAS 
    0x6800x4a: v4a680 = DELEGATECALL v4a67f, v66cV2454a, v4a67c(0x0), v4a67b, v4a678(0x0), v4a678(0x0)
    0x6810x4a: v4a681 = RETURNDATASIZE 
    0x6820x4a: v4a682(0x0) = CONST 
    0x6850x4a: RETURNDATACOPY v4a682(0x0), v4a682(0x0), v4a681
    0x6870x4a: v4a687(0x0) = CONST 
    0x68a0x4a: v4a68a = EQ v4a680, v4a687(0x0)
    0x68b0x4a: v4a68b(0x693) = CONST 
    0x68e0x4a: JUMPI v4a68b(0x693), v4a68a

    Begin block 0x68f0x4a
    prev=[0x6720x4a], succ=[]
    =================================
    0x68f0x4a: v4a68f = RETURNDATASIZE 
    0x6900x4a: v4a690(0x0) = CONST 
    0x6920x4a: RETURN v4a690(0x0), v4a68f

    Begin block 0x6930x4a
    prev=[0x6720x4a], succ=[]
    =================================
    0x6940x4a: v4a694 = RETURNDATASIZE 
    0x6950x4a: v4a695(0x0) = CONST 
    0x6970x4a: REVERT v4a695(0x0), v4a694

}

function upgradeTo(address)() public {
    Begin block 0x54
    prev=[], succ=[0x60, 0x5c]
    =================================
    0x55: v55 = CALLVALUE 
    0x57: v57 = ISZERO v55
    0x58: v58(0x60) = CONST 
    0x5b: JUMPI v58(0x60), v57

    Begin block 0x60
    prev=[0x54], succ=[0x73, 0x77]
    =================================
    0x62: v62(0xa3) = CONST 
    0x65: v65(0x4) = CONST 
    0x68: v68 = CALLDATASIZE 
    0x69: v69 = SUB v68, v65(0x4)
    0x6a: v6a(0x20) = CONST 
    0x6d: v6d = LT v69, v6a(0x20)
    0x6e: v6e = ISZERO v6d
    0x6f: v6f(0x77) = CONST 
    0x72: JUMPI v6f(0x77), v6e

    Begin block 0x73
    prev=[0x60], succ=[]
    =================================
    0x73: v73(0x0) = CONST 
    0x76: REVERT v73(0x0), v73(0x0)

    Begin block 0x77
    prev=[0x60], succ=[0x257]
    =================================
    0x79: v79 = ADD v65(0x4), v69
    0x7d: v7d = CALLDATALOAD v65(0x4)
    0x7e: v7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x93: v93 = AND v7e(0xffffffffffffffffffffffffffffffffffffffff), v7d
    0x95: v95(0x20) = CONST 
    0x97: v97(0x24) = ADD v95(0x20), v65(0x4)
    0x9f: v9f(0x257) = CONST 
    0xa2: JUMP v9f(0x257)

    Begin block 0x257
    prev=[0x77], succ=[0x698B0x257]
    =================================
    0x258: v258(0x25f) = CONST 
    0x25b: v25b(0x698) = CONST 
    0x25e: JUMP v25b(0x698)

    Begin block 0x698B0x257
    prev=[0x257], succ=[0x25f]
    =================================
    0x699S0x257: v699V257(0x0) = CONST 
    0x69cS0x257: v69cV257(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x257: v6bdV257(0x0) = CONST 
    0x6bfS0x257: v6bfV257(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV257(0x0), v69cV257(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x257: v6c3V257 = SLOAD v6bfV257(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x257: JUMP v258(0x25f)

    Begin block 0x25f
    prev=[0x698B0x257], succ=[0x293, 0x2a0]
    =================================
    0x260: v260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x275: v275 = AND v260(0xffffffffffffffffffffffffffffffffffffffff), v6c3V257
    0x276: v276 = CALLER 
    0x277: v277(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28c: v28c = AND v277(0xffffffffffffffffffffffffffffffffffffffff), v276
    0x28d: v28d = EQ v28c, v275
    0x28e: v28e = ISZERO v28d
    0x28f: v28f(0x2a0) = CONST 
    0x292: JUMPI v28f(0x2a0), v28e

    Begin block 0x293
    prev=[0x25f], succ=[0x29b]
    =================================
    0x293: v293(0x29b) = CONST 
    0x297: v297(0x6c9) = CONST 
    0x29a: CALLPRIVATE v297(0x6c9), v93, v293(0x29b)

    Begin block 0x29b
    prev=[0x293], succ=[0x2a9]
    =================================
    0x29c: v29c(0x2a9) = CONST 
    0x29f: JUMP v29c(0x2a9)

    Begin block 0x2a9
    prev=[0x29b], succ=[0xa3]
    =================================
    0x2ab: JUMP v62(0xa3)

    Begin block 0xa3
    prev=[0x2a9], succ=[]
    =================================
    0xa4: STOP 

    Begin block 0x2a0
    prev=[0x25f], succ=[0x23d0x54]
    =================================
    0x2a1: v2a1(0x2a8) = CONST 
    0x2a4: v2a4(0x23d) = CONST 
    0x2a7: JUMP v2a4(0x23d)

    Begin block 0x23d0x54
    prev=[0x2a0], succ=[0x2450x54]
    =================================
    0x23e0x54: v5423e(0x245) = CONST 
    0x2410x54: v54241(0x5ab) = CONST 
    0x2440x54: CALLPRIVATE v54241(0x5ab), v5423e(0x245)

    Begin block 0x2450x54
    prev=[0x23d0x54], succ=[0x641B0x2450x54]
    =================================
    0x2460x54: v54246(0x255) = CONST 
    0x2490x54: v54249(0x250) = CONST 
    0x24c0x54: v5424c(0x641) = CONST 
    0x24f0x54: JUMP v5424c(0x641)

    Begin block 0x641B0x2450x54
    prev=[0x2450x54], succ=[0x2500x54]
    =================================
    0x642S0x2450x54: v642V24554(0x0) = CONST 
    0x645S0x2450x54: v645V24554(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450x54: v666V24554(0x0) = CONST 
    0x668S0x2450x54: v668V24554(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V24554(0x0), v645V24554(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450x54: v66cV24554 = SLOAD v668V24554(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450x54: JUMP v54249(0x250)

    Begin block 0x2500x54
    prev=[0x641B0x2450x54], succ=[0x6720x54]
    =================================
    0x2510x54: v54251(0x672) = CONST 
    0x2540x54: JUMP v54251(0x672)

    Begin block 0x6720x54
    prev=[0x2500x54], succ=[0x68f0x54, 0x6930x54]
    =================================
    0x6730x54: v54673 = CALLDATASIZE 
    0x6740x54: v54674(0x0) = CONST 
    0x6770x54: CALLDATACOPY v54674(0x0), v54674(0x0), v54673
    0x6780x54: v54678(0x0) = CONST 
    0x67b0x54: v5467b = CALLDATASIZE 
    0x67c0x54: v5467c(0x0) = CONST 
    0x67f0x54: v5467f = GAS 
    0x6800x54: v54680 = DELEGATECALL v5467f, v66cV24554, v5467c(0x0), v5467b, v54678(0x0), v54678(0x0)
    0x6810x54: v54681 = RETURNDATASIZE 
    0x6820x54: v54682(0x0) = CONST 
    0x6850x54: RETURNDATACOPY v54682(0x0), v54682(0x0), v54681
    0x6870x54: v54687(0x0) = CONST 
    0x68a0x54: v5468a = EQ v54680, v54687(0x0)
    0x68b0x54: v5468b(0x693) = CONST 
    0x68e0x54: JUMPI v5468b(0x693), v5468a

    Begin block 0x68f0x54
    prev=[0x6720x54], succ=[]
    =================================
    0x68f0x54: v5468f = RETURNDATASIZE 
    0x6900x54: v54690(0x0) = CONST 
    0x6920x54: RETURN v54690(0x0), v5468f

    Begin block 0x6930x54
    prev=[0x6720x54], succ=[]
    =================================
    0x6940x54: v54694 = RETURNDATASIZE 
    0x6950x54: v54695(0x0) = CONST 
    0x6970x54: REVERT v54695(0x0), v54694

    Begin block 0x5c
    prev=[0x54], succ=[]
    =================================
    0x5c: v5c(0x0) = CONST 
    0x5f: REVERT v5c(0x0), v5c(0x0)

}

function 0x553(0x553arg0x0) private {
    Begin block 0x553
    prev=[], succ=[0x698B0x553]
    =================================
    0x554: v554(0x0) = CONST 
    0x556: v556(0x55d) = CONST 
    0x559: v559(0x698) = CONST 
    0x55c: JUMP v559(0x698)

    Begin block 0x698B0x553
    prev=[0x553], succ=[0x55d]
    =================================
    0x699S0x553: v699V553(0x0) = CONST 
    0x69cS0x553: v69cV553(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x553: v6bdV553(0x0) = CONST 
    0x6bfS0x553: v6bfV553(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV553(0x0), v69cV553(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x553: v6c3V553 = SLOAD v6bfV553(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x553: JUMP v556(0x55d)

    Begin block 0x55d
    prev=[0x698B0x553], succ=[0x591, 0x59f]
    =================================
    0x55e: v55e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x573: v573 = AND v55e(0xffffffffffffffffffffffffffffffffffffffff), v6c3V553
    0x574: v574 = CALLER 
    0x575: v575(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x58a: v58a = AND v575(0xffffffffffffffffffffffffffffffffffffffff), v574
    0x58b: v58b = EQ v58a, v573
    0x58c: v58c = ISZERO v58b
    0x58d: v58d(0x59f) = CONST 
    0x590: JUMPI v58d(0x59f), v58c

    Begin block 0x591
    prev=[0x55d], succ=[0x698B0x591]
    =================================
    0x591: v591(0x598) = CONST 
    0x594: v594(0x698) = CONST 
    0x597: JUMP v594(0x698)

    Begin block 0x698B0x591
    prev=[0x591], succ=[0x598]
    =================================
    0x699S0x591: v699V591(0x0) = CONST 
    0x69cS0x591: v69cV591(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x591: v6bdV591(0x0) = CONST 
    0x6bfS0x591: v6bfV591(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV591(0x0), v69cV591(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x591: v6c3V591 = SLOAD v6bfV591(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x591: JUMP v591(0x598)

    Begin block 0x598
    prev=[0x698B0x591], succ=[0x5a8]
    =================================
    0x59b: v59b(0x5a8) = CONST 
    0x59e: JUMP v59b(0x5a8)

    Begin block 0x5a8
    prev=[0x598], succ=[]
    =================================
    0x5aa: RETURNPRIVATE v553arg0, v6c3V591

    Begin block 0x59f
    prev=[0x55d], succ=[0x23d0x553]
    =================================
    0x5a0: v5a0(0x5a7) = CONST 
    0x5a3: v5a3(0x23d) = CONST 
    0x5a6: JUMP v5a3(0x23d)

    Begin block 0x23d0x553
    prev=[0x59f], succ=[0x2450x553]
    =================================
    0x23e0x553: v55323e(0x245) = CONST 
    0x2410x553: v553241(0x5ab) = CONST 
    0x2440x553: CALLPRIVATE v553241(0x5ab), v55323e(0x245)

    Begin block 0x2450x553
    prev=[0x23d0x553], succ=[0x641B0x2450x553]
    =================================
    0x2460x553: v553246(0x255) = CONST 
    0x2490x553: v553249(0x250) = CONST 
    0x24c0x553: v55324c(0x641) = CONST 
    0x24f0x553: JUMP v55324c(0x641)

    Begin block 0x641B0x2450x553
    prev=[0x2450x553], succ=[0x2500x553]
    =================================
    0x642S0x2450x553: v642V245553(0x0) = CONST 
    0x645S0x2450x553: v645V245553(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450x553: v666V245553(0x0) = CONST 
    0x668S0x2450x553: v668V245553(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V245553(0x0), v645V245553(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450x553: v66cV245553 = SLOAD v668V245553(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450x553: JUMP v553249(0x250)

    Begin block 0x2500x553
    prev=[0x641B0x2450x553], succ=[0x6720x553]
    =================================
    0x2510x553: v553251(0x672) = CONST 
    0x2540x553: JUMP v553251(0x672)

    Begin block 0x6720x553
    prev=[0x2500x553], succ=[0x68f0x553, 0x6930x553]
    =================================
    0x6730x553: v553673 = CALLDATASIZE 
    0x6740x553: v553674(0x0) = CONST 
    0x6770x553: CALLDATACOPY v553674(0x0), v553674(0x0), v553673
    0x6780x553: v553678(0x0) = CONST 
    0x67b0x553: v55367b = CALLDATASIZE 
    0x67c0x553: v55367c(0x0) = CONST 
    0x67f0x553: v55367f = GAS 
    0x6800x553: v553680 = DELEGATECALL v55367f, v66cV245553, v55367c(0x0), v55367b, v553678(0x0), v553678(0x0)
    0x6810x553: v553681 = RETURNDATASIZE 
    0x6820x553: v553682(0x0) = CONST 
    0x6850x553: RETURNDATACOPY v553682(0x0), v553682(0x0), v553681
    0x6870x553: v553687(0x0) = CONST 
    0x68a0x553: v55368a = EQ v553680, v553687(0x0)
    0x68b0x553: v55368b(0x693) = CONST 
    0x68e0x553: JUMPI v55368b(0x693), v55368a

    Begin block 0x68f0x553
    prev=[0x6720x553], succ=[]
    =================================
    0x68f0x553: v55368f = RETURNDATASIZE 
    0x6900x553: v553690(0x0) = CONST 
    0x6920x553: RETURN v553690(0x0), v55368f

    Begin block 0x6930x553
    prev=[0x6720x553], succ=[]
    =================================
    0x6940x553: v553694 = RETURNDATASIZE 
    0x6950x553: v553695(0x0) = CONST 
    0x6970x553: REVERT v553695(0x0), v553694

}

function 0x5ab(0x5abarg0x0) private {
    Begin block 0x5ab
    prev=[], succ=[0x698B0x5ab]
    =================================
    0x5ac: v5ac(0x5b3) = CONST 
    0x5af: v5af(0x698) = CONST 
    0x5b2: JUMP v5af(0x698)

    Begin block 0x698B0x5ab
    prev=[0x5ab], succ=[0x5b3]
    =================================
    0x699S0x5ab: v699V5ab(0x0) = CONST 
    0x69cS0x5ab: v69cV5ab(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x5ab: v6bdV5ab(0x0) = CONST 
    0x6bfS0x5ab: v6bfV5ab(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV5ab(0x0), v69cV5ab(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x5ab: v6c3V5ab = SLOAD v6bfV5ab(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x5ab: JUMP v5ac(0x5b3)

    Begin block 0x5b3
    prev=[0x698B0x5ab], succ=[0x5e7, 0x637]
    =================================
    0x5b4: v5b4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5c9: v5c9 = AND v5b4(0xffffffffffffffffffffffffffffffffffffffff), v6c3V5ab
    0x5ca: v5ca = CALLER 
    0x5cb: v5cb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5e0: v5e0 = AND v5cb(0xffffffffffffffffffffffffffffffffffffffff), v5ca
    0x5e1: v5e1 = EQ v5e0, v5c9
    0x5e2: v5e2 = ISZERO v5e1
    0x5e3: v5e3(0x637) = CONST 
    0x5e6: JUMPI v5e3(0x637), v5e2

    Begin block 0x5e7
    prev=[0x5b3], succ=[]
    =================================
    0x5e7: v5e7(0x40) = CONST 
    0x5e9: v5e9 = MLOAD v5e7(0x40)
    0x5ea: v5ea(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x60c: MSTORE v5e9, v5ea(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x60d: v60d(0x4) = CONST 
    0x60f: v60f = ADD v60d(0x4), v5e9
    0x612: v612(0x20) = CONST 
    0x614: v614 = ADD v612(0x20), v60f
    0x617: v617(0x20) = SUB v614, v60f
    0x619: MSTORE v60f, v617(0x20)
    0x61a: v61a(0x32) = CONST 
    0x61d: MSTORE v614, v61a(0x32)
    0x61e: v61e(0x20) = CONST 
    0x620: v620 = ADD v61e(0x20), v614
    0x622: v622(0x7ea) = CONST 
    0x625: v625(0x32) = CONST 
    0x628: CODECOPY v620, v622(0x7ea), v625(0x32)
    0x629: v629(0x40) = CONST 
    0x62b: v62b = ADD v629(0x40), v620
    0x62f: v62f(0x40) = CONST 
    0x631: v631 = MLOAD v62f(0x40)
    0x634: v634(0x84) = SUB v62b, v631
    0x636: REVERT v631, v634(0x84)

    Begin block 0x637
    prev=[0x5b3], succ=[0x747B0x637]
    =================================
    0x638: v638(0x63f) = CONST 
    0x63b: v63b(0x747) = CONST 
    0x63e: JUMP v63b(0x747), v638(0x63f)

    Begin block 0x747B0x637
    prev=[0x637], succ=[0x63f]
    =================================
    0x748S0x637: JUMP v638(0x63f)

    Begin block 0x63f
    prev=[0x747B0x637], succ=[]
    =================================
    0x640: RETURNPRIVATE v5abarg0

}

function 0x6c9(0x6c9arg0x0, 0x6c9arg0x1) private {
    Begin block 0x6c9
    prev=[], succ=[0x749]
    =================================
    0x6ca: v6ca(0x6d2) = CONST 
    0x6ce: v6ce(0x749) = CONST 
    0x6d1: JUMP v6ce(0x749)

    Begin block 0x749
    prev=[0x6c9], succ=[0x7d6]
    =================================
    0x74a: v74a(0x752) = CONST 
    0x74e: v74e(0x7d6) = CONST 
    0x751: JUMP v74e(0x7d6)

    Begin block 0x7d6
    prev=[0x749], succ=[0x752]
    =================================
    0x7d7: v7d7(0x0) = CONST 
    0x7db: v7db = EXTCODESIZE v6c9arg0
    0x7de: v7de(0x0) = CONST 
    0x7e1: v7e1 = GT v7db, v7de(0x0)
    0x7e8: JUMP v74a(0x752)

    Begin block 0x752
    prev=[0x7d6], succ=[0x757, 0x7a7]
    =================================
    0x753: v753(0x7a7) = CONST 
    0x756: JUMPI v753(0x7a7), v7e1

    Begin block 0x757
    prev=[0x752], succ=[]
    =================================
    0x757: v757(0x40) = CONST 
    0x759: v759 = MLOAD v757(0x40)
    0x75a: v75a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x77c: MSTORE v759, v75a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x77d: v77d(0x4) = CONST 
    0x77f: v77f = ADD v77d(0x4), v759
    0x782: v782(0x20) = CONST 
    0x784: v784 = ADD v782(0x20), v77f
    0x787: v787(0x20) = SUB v784, v77f
    0x789: MSTORE v77f, v787(0x20)
    0x78a: v78a(0x3b) = CONST 
    0x78d: MSTORE v784, v78a(0x3b)
    0x78e: v78e(0x20) = CONST 
    0x790: v790 = ADD v78e(0x20), v784
    0x792: v792(0x852) = CONST 
    0x795: v795(0x3b) = CONST 
    0x798: CODECOPY v790, v792(0x852), v795(0x3b)
    0x799: v799(0x40) = CONST 
    0x79b: v79b = ADD v799(0x40), v790
    0x79f: v79f(0x40) = CONST 
    0x7a1: v7a1 = MLOAD v79f(0x40)
    0x7a4: v7a4(0x84) = SUB v79b, v7a1
    0x7a6: REVERT v7a1, v7a4(0x84)

    Begin block 0x7a7
    prev=[0x752], succ=[0x6d2]
    =================================
    0x7a8: v7a8(0x0) = CONST 
    0x7aa: v7aa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x7cb: v7cb(0x0) = CONST 
    0x7cd: v7cd(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v7cb(0x0), v7aa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x7d2: SSTORE v7cd(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), v6c9arg0
    0x7d5: JUMP v6ca(0x6d2)

    Begin block 0x6d2
    prev=[0x7a7], succ=[]
    =================================
    0x6d4: v6d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6e9: v6e9 = AND v6d4(0xffffffffffffffffffffffffffffffffffffffff), v6c9arg0
    0x6ea: v6ea(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x70b: v70b(0x40) = CONST 
    0x70d: v70d = MLOAD v70b(0x40)
    0x70e: v70e(0x40) = CONST 
    0x710: v710 = MLOAD v70e(0x40)
    0x713: v713(0x0) = SUB v70d, v710
    0x715: LOG2 v710, v713(0x0), v6ea(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v6e9
    0x717: RETURNPRIVATE v6c9arg1

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xa5
    prev=[], succ=[0xb7, 0xbb]
    =================================
    0xa6: va6(0x13c) = CONST 
    0xa9: va9(0x4) = CONST 
    0xac: vac = CALLDATASIZE 
    0xad: vad = SUB vac, va9(0x4)
    0xae: vae(0x40) = CONST 
    0xb1: vb1 = LT vad, vae(0x40)
    0xb2: vb2 = ISZERO vb1
    0xb3: vb3(0xbb) = CONST 
    0xb6: JUMPI vb3(0xbb), vb2

    Begin block 0xb7
    prev=[0xa5], succ=[]
    =================================
    0xb7: vb7(0x0) = CONST 
    0xba: REVERT vb7(0x0), vb7(0x0)

    Begin block 0xbb
    prev=[0xa5], succ=[0xf4, 0xf8]
    =================================
    0xbd: vbd = ADD va9(0x4), vad
    0xc1: vc1 = CALLDATALOAD va9(0x4)
    0xc2: vc2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd7: vd7 = AND vc2(0xffffffffffffffffffffffffffffffffffffffff), vc1
    0xd9: vd9(0x20) = CONST 
    0xdb: vdb(0x24) = ADD vd9(0x20), va9(0x4)
    0xe1: ve1 = CALLDATALOAD vdb(0x24)
    0xe3: ve3(0x20) = CONST 
    0xe5: ve5(0x44) = ADD ve3(0x20), vdb(0x24)
    0xe7: ve7(0x100000000) = CONST 
    0xee: vee = GT ve1, ve7(0x100000000)
    0xef: vef = ISZERO vee
    0xf0: vf0(0xf8) = CONST 
    0xf3: JUMPI vf0(0xf8), vef

    Begin block 0xf4
    prev=[0xbb], succ=[]
    =================================
    0xf4: vf4(0x0) = CONST 
    0xf7: REVERT vf4(0x0), vf4(0x0)

    Begin block 0xf8
    prev=[0xbb], succ=[0x106, 0x10a]
    =================================
    0xfa: vfa = ADD va9(0x4), ve1
    0xfc: vfc(0x20) = CONST 
    0xff: vff = ADD vfa, vfc(0x20)
    0x100: v100 = GT vff, vbd
    0x101: v101 = ISZERO v100
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xf8], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xf8], succ=[0x128, 0x12c]
    =================================
    0x10c: v10c = CALLDATALOAD vfa
    0x10e: v10e(0x20) = CONST 
    0x110: v110 = ADD v10e(0x20), vfa
    0x113: v113(0x1) = CONST 
    0x116: v116 = MUL v10c, v113(0x1)
    0x118: v118 = ADD v110, v116
    0x119: v119 = GT v118, vbd
    0x11a: v11a(0x100000000) = CONST 
    0x121: v121 = GT v10c, v11a(0x100000000)
    0x122: v122 = OR v121, v119
    0x123: v123 = ISZERO v122
    0x124: v124(0x12c) = CONST 
    0x127: JUMPI v124(0x12c), v123

    Begin block 0x128
    prev=[0x10a], succ=[]
    =================================
    0x128: v128(0x0) = CONST 
    0x12b: REVERT v128(0x0), v128(0x0)

    Begin block 0x12c
    prev=[0x10a], succ=[0x2ac]
    =================================
    0x138: v138(0x2ac) = CONST 
    0x13b: JUMP v138(0x2ac)

    Begin block 0x2ac
    prev=[0x12c], succ=[0x698B0x2ac]
    =================================
    0x2ad: v2ad(0x2b4) = CONST 
    0x2b0: v2b0(0x698) = CONST 
    0x2b3: JUMP v2b0(0x698)

    Begin block 0x698B0x2ac
    prev=[0x2ac], succ=[0x2b4]
    =================================
    0x699S0x2ac: v699V2ac(0x0) = CONST 
    0x69cS0x2ac: v69cV2ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6bdS0x2ac: v6bdV2ac(0x0) = CONST 
    0x6bfS0x2ac: v6bfV2ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6bdV2ac(0x0), v69cV2ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c3S0x2ac: v6c3V2ac = SLOAD v6bfV2ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6c8S0x2ac: JUMP v2ad(0x2b4)

    Begin block 0x2b4
    prev=[0x698B0x2ac], succ=[0x2e8, 0x374]
    =================================
    0x2b5: v2b5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ca: v2ca = AND v2b5(0xffffffffffffffffffffffffffffffffffffffff), v6c3V2ac
    0x2cb: v2cb = CALLER 
    0x2cc: v2cc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e1: v2e1 = AND v2cc(0xffffffffffffffffffffffffffffffffffffffff), v2cb
    0x2e2: v2e2 = EQ v2e1, v2ca
    0x2e3: v2e3 = ISZERO v2e2
    0x2e4: v2e4(0x374) = CONST 
    0x2e7: JUMPI v2e4(0x374), v2e3

    Begin block 0x2e8
    prev=[0x2b4], succ=[0x2f0]
    =================================
    0x2e8: v2e8(0x2f0) = CONST 
    0x2ec: v2ec(0x6c9) = CONST 
    0x2ef: CALLPRIVATE v2ec(0x6c9), vd7, v2e8(0x2f0)

    Begin block 0x2f0
    prev=[0x2e8], succ=[0x33a, 0x35b]
    =================================
    0x2f1: v2f1(0x0) = CONST 
    0x2f4: v2f4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x309: v309 = AND v2f4(0xffffffffffffffffffffffffffffffffffffffff), vd7
    0x30c: v30c(0x40) = CONST 
    0x30e: v30e = MLOAD v30c(0x40)
    0x315: CALLDATACOPY v30e, v110, v10c
    0x318: v318 = ADD v30e, v10c
    0x321: v321(0x0) = CONST 
    0x323: v323(0x40) = CONST 
    0x325: v325 = MLOAD v323(0x40)
    0x328: v328 = SUB v318, v325
    0x32b: v32b = GAS 
    0x32c: v32c = DELEGATECALL v32b, v309, v325, v328, v325, v321(0x0)
    0x330: v330 = RETURNDATASIZE 
    0x332: v332(0x0) = CONST 
    0x335: v335 = EQ v330, v332(0x0)
    0x336: v336(0x35b) = CONST 
    0x339: JUMPI v336(0x35b), v335

    Begin block 0x33a
    prev=[0x2f0], succ=[0x360]
    =================================
    0x33a: v33a(0x40) = CONST 
    0x33c: v33c = MLOAD v33a(0x40)
    0x33f: v33f(0x1f) = CONST 
    0x341: v341(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v33f(0x1f)
    0x342: v342(0x3f) = CONST 
    0x344: v344 = RETURNDATASIZE 
    0x345: v345 = ADD v344, v342(0x3f)
    0x346: v346 = AND v345, v341(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x348: v348 = ADD v33c, v346
    0x349: v349(0x40) = CONST 
    0x34b: MSTORE v349(0x40), v348
    0x34c: v34c = RETURNDATASIZE 
    0x34e: MSTORE v33c, v34c
    0x34f: v34f = RETURNDATASIZE 
    0x350: v350(0x0) = CONST 
    0x352: v352(0x20) = CONST 
    0x355: v355 = ADD v33c, v352(0x20)
    0x356: RETURNDATACOPY v355, v350(0x0), v34f
    0x357: v357(0x360) = CONST 
    0x35a: JUMP v357(0x360)

    Begin block 0x360
    prev=[0x33a, 0x35b], succ=[0x36a, 0x36e]
    =================================
    0x366: v366(0x36e) = CONST 
    0x369: JUMPI v366(0x36e), v32c

    Begin block 0x36a
    prev=[0x360], succ=[]
    =================================
    0x36a: v36a(0x0) = CONST 
    0x36d: REVERT v36a(0x0), v36a(0x0)

    Begin block 0x36e
    prev=[0x360], succ=[0x37d]
    =================================
    0x370: v370(0x37d) = CONST 
    0x373: JUMP v370(0x37d)

    Begin block 0x37d
    prev=[0x36e], succ=[0x13c]
    =================================
    0x381: JUMP va6(0x13c)

    Begin block 0x13c
    prev=[0x37d], succ=[]
    =================================
    0x13d: STOP 

    Begin block 0x35b
    prev=[0x2f0], succ=[0x360]
    =================================
    0x35c: v35c(0x60) = CONST 

    Begin block 0x374
    prev=[0x2b4], succ=[0x23d0xa5]
    =================================
    0x375: v375(0x37c) = CONST 
    0x378: v378(0x23d) = CONST 
    0x37b: JUMP v378(0x23d)

    Begin block 0x23d0xa5
    prev=[0x374], succ=[0x2450xa5]
    =================================
    0x23e0xa5: va523e(0x245) = CONST 
    0x2410xa5: va5241(0x5ab) = CONST 
    0x2440xa5: CALLPRIVATE va5241(0x5ab), va523e(0x245)

    Begin block 0x2450xa5
    prev=[0x23d0xa5], succ=[0x641B0x2450xa5]
    =================================
    0x2460xa5: va5246(0x255) = CONST 
    0x2490xa5: va5249(0x250) = CONST 
    0x24c0xa5: va524c(0x641) = CONST 
    0x24f0xa5: JUMP va524c(0x641)

    Begin block 0x641B0x2450xa5
    prev=[0x2450xa5], succ=[0x2500xa5]
    =================================
    0x642S0x2450xa5: v642V245a5(0x0) = CONST 
    0x645S0x2450xa5: v645V245a5(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x666S0x2450xa5: v666V245a5(0x0) = CONST 
    0x668S0x2450xa5: v668V245a5(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v666V245a5(0x0), v645V245a5(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x66cS0x2450xa5: v66cV245a5 = SLOAD v668V245a5(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x671S0x2450xa5: JUMP va5249(0x250)

    Begin block 0x2500xa5
    prev=[0x641B0x2450xa5], succ=[0x6720xa5]
    =================================
    0x2510xa5: va5251(0x672) = CONST 
    0x2540xa5: JUMP va5251(0x672)

    Begin block 0x6720xa5
    prev=[0x2500xa5], succ=[0x68f0xa5, 0x6930xa5]
    =================================
    0x6730xa5: va5673 = CALLDATASIZE 
    0x6740xa5: va5674(0x0) = CONST 
    0x6770xa5: CALLDATACOPY va5674(0x0), va5674(0x0), va5673
    0x6780xa5: va5678(0x0) = CONST 
    0x67b0xa5: va567b = CALLDATASIZE 
    0x67c0xa5: va567c(0x0) = CONST 
    0x67f0xa5: va567f = GAS 
    0x6800xa5: va5680 = DELEGATECALL va567f, v66cV245a5, va567c(0x0), va567b, va5678(0x0), va5678(0x0)
    0x6810xa5: va5681 = RETURNDATASIZE 
    0x6820xa5: va5682(0x0) = CONST 
    0x6850xa5: RETURNDATACOPY va5682(0x0), va5682(0x0), va5681
    0x6870xa5: va5687(0x0) = CONST 
    0x68a0xa5: va568a = EQ va5680, va5687(0x0)
    0x68b0xa5: va568b(0x693) = CONST 
    0x68e0xa5: JUMPI va568b(0x693), va568a

    Begin block 0x68f0xa5
    prev=[0x6720xa5], succ=[]
    =================================
    0x68f0xa5: va568f = RETURNDATASIZE 
    0x6900xa5: va5690(0x0) = CONST 
    0x6920xa5: RETURN va5690(0x0), va568f

    Begin block 0x6930xa5
    prev=[0x6720xa5], succ=[]
    =================================
    0x6940xa5: va5694 = RETURNDATASIZE 
    0x6950xa5: va5695(0x0) = CONST 
    0x6970xa5: REVERT va5695(0x0), va5694

}

