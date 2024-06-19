function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8c5]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x8b9: v8b9(0x8c5) = CONST 
    0x8ba: JUMPI v8b9(0x8c5), v8

    Begin block 0xd
    prev=[0x0], succ=[0x8c8, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x3659cfe6) = CONST 
    0x19: v19 = EQ v14(0x3659cfe6), v12
    0x8bb: v8bb(0x8c8) = CONST 
    0x8bc: JUMPI v8bb(0x8c8), v19

    Begin block 0x8c8
    prev=[0xd], succ=[]
    =================================
    0x8c9: v8c9(0x54) = CONST 
    0x8ca: CALLPRIVATE v8c9(0x54)

    Begin block 0x1e
    prev=[0xd], succ=[0x8cb, 0x29]
    =================================
    0x1f: v1f(0x4f1ef286) = CONST 
    0x24: v24 = EQ v1f(0x4f1ef286), v12
    0x8bd: v8bd(0x8cb) = CONST 
    0x8be: JUMPI v8bd(0x8cb), v24

    Begin block 0x8cb
    prev=[0x1e], succ=[]
    =================================
    0x8cc: v8cc(0xa5) = CONST 
    0x8cd: CALLPRIVATE v8cc(0xa5)

    Begin block 0x29
    prev=[0x1e], succ=[0x8ce, 0x34]
    =================================
    0x2a: v2a(0x5c60da1b) = CONST 
    0x2f: v2f = EQ v2a(0x5c60da1b), v12
    0x8bf: v8bf(0x8ce) = CONST 
    0x8c0: JUMPI v8bf(0x8ce), v2f

    Begin block 0x8ce
    prev=[0x29], succ=[]
    =================================
    0x8cf: v8cf(0x13e) = CONST 
    0x8d0: CALLPRIVATE v8cf(0x13e)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x8d1]
    =================================
    0x35: v35(0x8f283970) = CONST 
    0x3a: v3a = EQ v35(0x8f283970), v12
    0x8c1: v8c1(0x8d1) = CONST 
    0x8c2: JUMPI v8c1(0x8d1), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x8c5, 0x8d4]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x8c3: v8c3(0x8d4) = CONST 
    0x8c4: JUMPI v8c3(0x8d4), v45

    Begin block 0x8c5
    prev=[0x0, 0x3f], succ=[]
    =================================
    0x8c6: v8c6(0x4a) = CONST 
    0x8c7: CALLPRIVATE v8c6(0x4a)

    Begin block 0x8d4
    prev=[0x3f], succ=[]
    =================================
    0x8d5: v8d5(0x1e6) = CONST 
    0x8d6: CALLPRIVATE v8d5(0x1e6)

    Begin block 0x8d1
    prev=[0x34], succ=[]
    =================================
    0x8d2: v8d2(0x195) = CONST 
    0x8d3: CALLPRIVATE v8d2(0x195)

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
    0x14f: v14f(0x384) = CONST 
    0x152: v152_0 = CALLPRIVATE v14f(0x384), v14c(0x153)

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
    prev=[0x1a1], succ=[0x3dc]
    =================================
    0x1ba: v1ba = ADD v1a6(0x4), v1aa
    0x1be: v1be = CALLDATALOAD v1a6(0x4)
    0x1bf: v1bf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d4: v1d4 = AND v1bf(0xffffffffffffffffffffffffffffffffffffffff), v1be
    0x1d6: v1d6(0x20) = CONST 
    0x1d8: v1d8(0x24) = ADD v1d6(0x20), v1a6(0x4)
    0x1e0: v1e0(0x3dc) = CONST 
    0x1e3: JUMP v1e0(0x3dc)

    Begin block 0x3dc
    prev=[0x1b8], succ=[0x69eB0x3dc]
    =================================
    0x3dd: v3dd(0x3e4) = CONST 
    0x3e0: v3e0(0x69e) = CONST 
    0x3e3: JUMP v3e0(0x69e)

    Begin block 0x69eB0x3dc
    prev=[0x3dc], succ=[0x3e4]
    =================================
    0x69fS0x3dc: v69fV3dc(0x0) = CONST 
    0x6a2S0x3dc: v6a2V3dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x3dc: v6c3V3dc(0x0) = CONST 
    0x6c5S0x3dc: v6c5V3dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V3dc(0x0), v6a2V3dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x3dc: v6c9V3dc = SLOAD v6c5V3dc(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x3dc: JUMP v3dd(0x3e4)

    Begin block 0x3e4
    prev=[0x69eB0x3dc], succ=[0x418, 0x54b]
    =================================
    0x3e5: v3e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3fa: v3fa = AND v3e5(0xffffffffffffffffffffffffffffffffffffffff), v6c9V3dc
    0x3fb: v3fb = CALLER 
    0x3fc: v3fc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x411: v411 = AND v3fc(0xffffffffffffffffffffffffffffffffffffffff), v3fb
    0x412: v412 = EQ v411, v3fa
    0x413: v413 = ISZERO v412
    0x414: v414(0x54b) = CONST 
    0x417: JUMPI v414(0x54b), v413

    Begin block 0x418
    prev=[0x3e4], succ=[0x44f, 0x49f]
    =================================
    0x418: v418(0x0) = CONST 
    0x41a: v41a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x42f: v42f(0x0) = AND v41a(0xffffffffffffffffffffffffffffffffffffffff), v418(0x0)
    0x431: v431(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x446: v446 = AND v431(0xffffffffffffffffffffffffffffffffffffffff), v1d4
    0x447: v447 = EQ v446, v42f(0x0)
    0x448: v448 = ISZERO v447
    0x449: v449 = ISZERO v448
    0x44a: v44a = ISZERO v449
    0x44b: v44b(0x49f) = CONST 
    0x44e: JUMPI v44b(0x49f), v44a

    Begin block 0x44f
    prev=[0x418], succ=[]
    =================================
    0x44f: v44f(0x40) = CONST 
    0x451: v451 = MLOAD v44f(0x40)
    0x452: v452(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x474: MSTORE v451, v452(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x475: v475(0x4) = CONST 
    0x477: v477 = ADD v475(0x4), v451
    0x47a: v47a(0x20) = CONST 
    0x47c: v47c = ADD v47a(0x20), v477
    0x47f: v47f(0x20) = SUB v47c, v477
    0x481: MSTORE v477, v47f(0x20)
    0x482: v482(0x36) = CONST 
    0x485: MSTORE v47c, v482(0x36)
    0x486: v486(0x20) = CONST 
    0x488: v488 = ADD v486(0x20), v47c
    0x48a: v48a(0x824) = CONST 
    0x48d: v48d(0x36) = CONST 
    0x490: CODECOPY v488, v48a(0x824), v48d(0x36)
    0x491: v491(0x40) = CONST 
    0x493: v493 = ADD v491(0x40), v488
    0x497: v497(0x40) = CONST 
    0x499: v499 = MLOAD v497(0x40)
    0x49c: v49c(0x84) = SUB v493, v499
    0x49e: REVERT v499, v49c(0x84)

    Begin block 0x49f
    prev=[0x418], succ=[0x69eB0x49f]
    =================================
    0x4a0: v4a0(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x4c1: v4c1(0x4c8) = CONST 
    0x4c4: v4c4(0x69e) = CONST 
    0x4c7: JUMP v4c4(0x69e)

    Begin block 0x69eB0x49f
    prev=[0x49f], succ=[0x4c8]
    =================================
    0x69fS0x49f: v69fV49f(0x0) = CONST 
    0x6a2S0x49f: v6a2V49f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x49f: v6c3V49f(0x0) = CONST 
    0x6c5S0x49f: v6c5V49f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V49f(0x0), v6a2V49f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x49f: v6c9V49f = SLOAD v6c5V49f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x49f: JUMP v4c1(0x4c8)

    Begin block 0x4c8
    prev=[0x69eB0x49f], succ=[0x71e]
    =================================
    0x4ca: v4ca(0x40) = CONST 
    0x4cc: v4cc = MLOAD v4ca(0x40)
    0x4cf: v4cf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4e4: v4e4 = AND v4cf(0xffffffffffffffffffffffffffffffffffffffff), v6c9V49f
    0x4e5: v4e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4fa: v4fa = AND v4e5(0xffffffffffffffffffffffffffffffffffffffff), v4e4
    0x4fc: MSTORE v4cc, v4fa
    0x4fd: v4fd(0x20) = CONST 
    0x4ff: v4ff = ADD v4fd(0x20), v4cc
    0x501: v501(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x516: v516 = AND v501(0xffffffffffffffffffffffffffffffffffffffff), v1d4
    0x517: v517(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x52c: v52c = AND v517(0xffffffffffffffffffffffffffffffffffffffff), v516
    0x52e: MSTORE v4ff, v52c
    0x52f: v52f(0x20) = CONST 
    0x531: v531 = ADD v52f(0x20), v4ff
    0x536: v536(0x40) = CONST 
    0x538: v538 = MLOAD v536(0x40)
    0x53b: v53b(0x40) = SUB v531, v538
    0x53d: LOG1 v538, v53b(0x40), v4a0(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x53e: v53e(0x546) = CONST 
    0x542: v542(0x71e) = CONST 
    0x545: JUMP v542(0x71e)

    Begin block 0x71e
    prev=[0x4c8], succ=[0x546]
    =================================
    0x71f: v71f(0x0) = CONST 
    0x721: v721(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x742: v742(0x0) = CONST 
    0x744: v744(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v742(0x0), v721(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x749: SSTORE v744(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v1d4
    0x74c: JUMP v53e(0x546)

    Begin block 0x546
    prev=[0x71e], succ=[0x554]
    =================================
    0x547: v547(0x554) = CONST 
    0x54a: JUMP v547(0x554)

    Begin block 0x554
    prev=[0x546], succ=[0x1e4]
    =================================
    0x556: JUMP v1a3(0x1e4)

    Begin block 0x1e4
    prev=[0x554], succ=[]
    =================================
    0x1e5: STOP 

    Begin block 0x54b
    prev=[0x3e4], succ=[0x23d0x195]
    =================================
    0x54c: v54c(0x553) = CONST 
    0x54f: v54f(0x23d) = CONST 
    0x552: JUMP v54f(0x23d)

    Begin block 0x23d0x195
    prev=[0x54b], succ=[0x2450x195]
    =================================
    0x23e0x195: v19523e(0x245) = CONST 
    0x2410x195: v195241(0x5af) = CONST 
    0x2440x195: CALLPRIVATE v195241(0x5af), v19523e(0x245)

    Begin block 0x2450x195
    prev=[0x23d0x195], succ=[0x647B0x2450x195]
    =================================
    0x2460x195: v195246(0x255) = CONST 
    0x2490x195: v195249(0x250) = CONST 
    0x24c0x195: v19524c(0x647) = CONST 
    0x24f0x195: JUMP v19524c(0x647)

    Begin block 0x647B0x2450x195
    prev=[0x2450x195], succ=[0x2500x195]
    =================================
    0x648S0x2450x195: v648V245195(0x0) = CONST 
    0x64bS0x2450x195: v64bV245195(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450x195: v66cV245195(0x0) = CONST 
    0x66eS0x2450x195: v66eV245195(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV245195(0x0), v64bV245195(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450x195: v672V245195 = SLOAD v66eV245195(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450x195: JUMP v195249(0x250)

    Begin block 0x2500x195
    prev=[0x647B0x2450x195], succ=[0x6780x195]
    =================================
    0x2510x195: v195251(0x678) = CONST 
    0x2540x195: JUMP v195251(0x678)

    Begin block 0x6780x195
    prev=[0x2500x195], succ=[0x6950x195, 0x6990x195]
    =================================
    0x6790x195: v195679 = CALLDATASIZE 
    0x67a0x195: v19567a(0x0) = CONST 
    0x67d0x195: CALLDATACOPY v19567a(0x0), v19567a(0x0), v195679
    0x67e0x195: v19567e(0x0) = CONST 
    0x6810x195: v195681 = CALLDATASIZE 
    0x6820x195: v195682(0x0) = CONST 
    0x6850x195: v195685 = GAS 
    0x6860x195: v195686 = DELEGATECALL v195685, v672V245195, v195682(0x0), v195681, v19567e(0x0), v19567e(0x0)
    0x6870x195: v195687 = RETURNDATASIZE 
    0x6880x195: v195688(0x0) = CONST 
    0x68b0x195: RETURNDATACOPY v195688(0x0), v195688(0x0), v195687
    0x68d0x195: v19568d(0x0) = CONST 
    0x6900x195: v195690 = EQ v195686, v19568d(0x0)
    0x6910x195: v195691(0x699) = CONST 
    0x6940x195: JUMPI v195691(0x699), v195690

    Begin block 0x6950x195
    prev=[0x6780x195], succ=[]
    =================================
    0x6950x195: v195695 = RETURNDATASIZE 
    0x6960x195: v195696(0x0) = CONST 
    0x6980x195: RETURN v195696(0x0), v195695

    Begin block 0x6990x195
    prev=[0x6780x195], succ=[]
    =================================
    0x69a0x195: v19569a = RETURNDATASIZE 
    0x69b0x195: v19569b(0x0) = CONST 
    0x69d0x195: REVERT v19569b(0x0), v19569a

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
    0x1f7: v1f7(0x557) = CONST 
    0x1fa: v1fa_0 = CALLPRIVATE v1f7(0x557), v1f4(0x1fb)

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

function 0x384(0x384arg0x0) private {
    Begin block 0x384
    prev=[], succ=[0x69eB0x384]
    =================================
    0x385: v385(0x0) = CONST 
    0x387: v387(0x38e) = CONST 
    0x38a: v38a(0x69e) = CONST 
    0x38d: JUMP v38a(0x69e)

    Begin block 0x69eB0x384
    prev=[0x384], succ=[0x38e]
    =================================
    0x69fS0x384: v69fV384(0x0) = CONST 
    0x6a2S0x384: v6a2V384(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x384: v6c3V384(0x0) = CONST 
    0x6c5S0x384: v6c5V384(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V384(0x0), v6a2V384(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x384: v6c9V384 = SLOAD v6c5V384(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x384: JUMP v387(0x38e)

    Begin block 0x38e
    prev=[0x69eB0x384], succ=[0x3c2, 0x3d0]
    =================================
    0x38f: v38f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a4: v3a4 = AND v38f(0xffffffffffffffffffffffffffffffffffffffff), v6c9V384
    0x3a5: v3a5 = CALLER 
    0x3a6: v3a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3bb: v3bb = AND v3a6(0xffffffffffffffffffffffffffffffffffffffff), v3a5
    0x3bc: v3bc = EQ v3bb, v3a4
    0x3bd: v3bd = ISZERO v3bc
    0x3be: v3be(0x3d0) = CONST 
    0x3c1: JUMPI v3be(0x3d0), v3bd

    Begin block 0x3c2
    prev=[0x38e], succ=[0x647B0x3c2]
    =================================
    0x3c2: v3c2(0x3c9) = CONST 
    0x3c5: v3c5(0x647) = CONST 
    0x3c8: JUMP v3c5(0x647)

    Begin block 0x647B0x3c2
    prev=[0x3c2], succ=[0x3c9]
    =================================
    0x648S0x3c2: v648V3c2(0x0) = CONST 
    0x64bS0x3c2: v64bV3c2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x3c2: v66cV3c2(0x0) = CONST 
    0x66eS0x3c2: v66eV3c2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV3c2(0x0), v64bV3c2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x3c2: v672V3c2 = SLOAD v66eV3c2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x3c2: JUMP v3c2(0x3c9)

    Begin block 0x3c9
    prev=[0x647B0x3c2], succ=[0x3d9]
    =================================
    0x3cc: v3cc(0x3d9) = CONST 
    0x3cf: JUMP v3cc(0x3d9)

    Begin block 0x3d9
    prev=[0x3c9], succ=[]
    =================================
    0x3db: RETURNPRIVATE v384arg0, v672V3c2

    Begin block 0x3d0
    prev=[0x38e], succ=[0x23d0x384]
    =================================
    0x3d1: v3d1(0x3d8) = CONST 
    0x3d4: v3d4(0x23d) = CONST 
    0x3d7: JUMP v3d4(0x23d)

    Begin block 0x23d0x384
    prev=[0x3d0], succ=[0x2450x384]
    =================================
    0x23e0x384: v38423e(0x245) = CONST 
    0x2410x384: v384241(0x5af) = CONST 
    0x2440x384: CALLPRIVATE v384241(0x5af), v38423e(0x245)

    Begin block 0x2450x384
    prev=[0x23d0x384], succ=[0x647B0x2450x384]
    =================================
    0x2460x384: v384246(0x255) = CONST 
    0x2490x384: v384249(0x250) = CONST 
    0x24c0x384: v38424c(0x647) = CONST 
    0x24f0x384: JUMP v38424c(0x647)

    Begin block 0x647B0x2450x384
    prev=[0x2450x384], succ=[0x2500x384]
    =================================
    0x648S0x2450x384: v648V245384(0x0) = CONST 
    0x64bS0x2450x384: v64bV245384(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450x384: v66cV245384(0x0) = CONST 
    0x66eS0x2450x384: v66eV245384(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV245384(0x0), v64bV245384(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450x384: v672V245384 = SLOAD v66eV245384(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450x384: JUMP v384249(0x250)

    Begin block 0x2500x384
    prev=[0x647B0x2450x384], succ=[0x6780x384]
    =================================
    0x2510x384: v384251(0x678) = CONST 
    0x2540x384: JUMP v384251(0x678)

    Begin block 0x6780x384
    prev=[0x2500x384], succ=[0x6950x384, 0x6990x384]
    =================================
    0x6790x384: v384679 = CALLDATASIZE 
    0x67a0x384: v38467a(0x0) = CONST 
    0x67d0x384: CALLDATACOPY v38467a(0x0), v38467a(0x0), v384679
    0x67e0x384: v38467e(0x0) = CONST 
    0x6810x384: v384681 = CALLDATASIZE 
    0x6820x384: v384682(0x0) = CONST 
    0x6850x384: v384685 = GAS 
    0x6860x384: v384686 = DELEGATECALL v384685, v672V245384, v384682(0x0), v384681, v38467e(0x0), v38467e(0x0)
    0x6870x384: v384687 = RETURNDATASIZE 
    0x6880x384: v384688(0x0) = CONST 
    0x68b0x384: RETURNDATACOPY v384688(0x0), v384688(0x0), v384687
    0x68d0x384: v38468d(0x0) = CONST 
    0x6900x384: v384690 = EQ v384686, v38468d(0x0)
    0x6910x384: v384691(0x699) = CONST 
    0x6940x384: JUMPI v384691(0x699), v384690

    Begin block 0x6950x384
    prev=[0x6780x384], succ=[]
    =================================
    0x6950x384: v384695 = RETURNDATASIZE 
    0x6960x384: v384696(0x0) = CONST 
    0x6980x384: RETURN v384696(0x0), v384695

    Begin block 0x6990x384
    prev=[0x6780x384], succ=[]
    =================================
    0x69a0x384: v38469a = RETURNDATASIZE 
    0x69b0x384: v38469b(0x0) = CONST 
    0x69d0x384: REVERT v38469b(0x0), v38469a

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
    0x2410x4a: v4a241(0x5af) = CONST 
    0x2440x4a: CALLPRIVATE v4a241(0x5af), v4a23e(0x245)

    Begin block 0x2450x4a
    prev=[0x23d0x4a], succ=[0x647B0x2450x4a]
    =================================
    0x2460x4a: v4a246(0x255) = CONST 
    0x2490x4a: v4a249(0x250) = CONST 
    0x24c0x4a: v4a24c(0x647) = CONST 
    0x24f0x4a: JUMP v4a24c(0x647)

    Begin block 0x647B0x2450x4a
    prev=[0x2450x4a], succ=[0x2500x4a]
    =================================
    0x648S0x2450x4a: v648V2454a(0x0) = CONST 
    0x64bS0x2450x4a: v64bV2454a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450x4a: v66cV2454a(0x0) = CONST 
    0x66eS0x2450x4a: v66eV2454a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV2454a(0x0), v64bV2454a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450x4a: v672V2454a = SLOAD v66eV2454a(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450x4a: JUMP v4a249(0x250)

    Begin block 0x2500x4a
    prev=[0x647B0x2450x4a], succ=[0x6780x4a]
    =================================
    0x2510x4a: v4a251(0x678) = CONST 
    0x2540x4a: JUMP v4a251(0x678)

    Begin block 0x6780x4a
    prev=[0x2500x4a], succ=[0x6950x4a, 0x6990x4a]
    =================================
    0x6790x4a: v4a679 = CALLDATASIZE 
    0x67a0x4a: v4a67a(0x0) = CONST 
    0x67d0x4a: CALLDATACOPY v4a67a(0x0), v4a67a(0x0), v4a679
    0x67e0x4a: v4a67e(0x0) = CONST 
    0x6810x4a: v4a681 = CALLDATASIZE 
    0x6820x4a: v4a682(0x0) = CONST 
    0x6850x4a: v4a685 = GAS 
    0x6860x4a: v4a686 = DELEGATECALL v4a685, v672V2454a, v4a682(0x0), v4a681, v4a67e(0x0), v4a67e(0x0)
    0x6870x4a: v4a687 = RETURNDATASIZE 
    0x6880x4a: v4a688(0x0) = CONST 
    0x68b0x4a: RETURNDATACOPY v4a688(0x0), v4a688(0x0), v4a687
    0x68d0x4a: v4a68d(0x0) = CONST 
    0x6900x4a: v4a690 = EQ v4a686, v4a68d(0x0)
    0x6910x4a: v4a691(0x699) = CONST 
    0x6940x4a: JUMPI v4a691(0x699), v4a690

    Begin block 0x6950x4a
    prev=[0x6780x4a], succ=[]
    =================================
    0x6950x4a: v4a695 = RETURNDATASIZE 
    0x6960x4a: v4a696(0x0) = CONST 
    0x6980x4a: RETURN v4a696(0x0), v4a695

    Begin block 0x6990x4a
    prev=[0x6780x4a], succ=[]
    =================================
    0x69a0x4a: v4a69a = RETURNDATASIZE 
    0x69b0x4a: v4a69b(0x0) = CONST 
    0x69d0x4a: REVERT v4a69b(0x0), v4a69a

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
    prev=[0x77], succ=[0x69eB0x257]
    =================================
    0x258: v258(0x25f) = CONST 
    0x25b: v25b(0x69e) = CONST 
    0x25e: JUMP v25b(0x69e)

    Begin block 0x69eB0x257
    prev=[0x257], succ=[0x25f]
    =================================
    0x69fS0x257: v69fV257(0x0) = CONST 
    0x6a2S0x257: v6a2V257(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x257: v6c3V257(0x0) = CONST 
    0x6c5S0x257: v6c5V257(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V257(0x0), v6a2V257(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x257: v6c9V257 = SLOAD v6c5V257(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x257: JUMP v258(0x25f)

    Begin block 0x25f
    prev=[0x69eB0x257], succ=[0x293, 0x2a0]
    =================================
    0x260: v260(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x275: v275 = AND v260(0xffffffffffffffffffffffffffffffffffffffff), v6c9V257
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
    0x297: v297(0x6cf) = CONST 
    0x29a: CALLPRIVATE v297(0x6cf), v93, v293(0x29b)

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
    0x2410x54: v54241(0x5af) = CONST 
    0x2440x54: CALLPRIVATE v54241(0x5af), v5423e(0x245)

    Begin block 0x2450x54
    prev=[0x23d0x54], succ=[0x647B0x2450x54]
    =================================
    0x2460x54: v54246(0x255) = CONST 
    0x2490x54: v54249(0x250) = CONST 
    0x24c0x54: v5424c(0x647) = CONST 
    0x24f0x54: JUMP v5424c(0x647)

    Begin block 0x647B0x2450x54
    prev=[0x2450x54], succ=[0x2500x54]
    =================================
    0x648S0x2450x54: v648V24554(0x0) = CONST 
    0x64bS0x2450x54: v64bV24554(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450x54: v66cV24554(0x0) = CONST 
    0x66eS0x2450x54: v66eV24554(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV24554(0x0), v64bV24554(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450x54: v672V24554 = SLOAD v66eV24554(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450x54: JUMP v54249(0x250)

    Begin block 0x2500x54
    prev=[0x647B0x2450x54], succ=[0x6780x54]
    =================================
    0x2510x54: v54251(0x678) = CONST 
    0x2540x54: JUMP v54251(0x678)

    Begin block 0x6780x54
    prev=[0x2500x54], succ=[0x6950x54, 0x6990x54]
    =================================
    0x6790x54: v54679 = CALLDATASIZE 
    0x67a0x54: v5467a(0x0) = CONST 
    0x67d0x54: CALLDATACOPY v5467a(0x0), v5467a(0x0), v54679
    0x67e0x54: v5467e(0x0) = CONST 
    0x6810x54: v54681 = CALLDATASIZE 
    0x6820x54: v54682(0x0) = CONST 
    0x6850x54: v54685 = GAS 
    0x6860x54: v54686 = DELEGATECALL v54685, v672V24554, v54682(0x0), v54681, v5467e(0x0), v5467e(0x0)
    0x6870x54: v54687 = RETURNDATASIZE 
    0x6880x54: v54688(0x0) = CONST 
    0x68b0x54: RETURNDATACOPY v54688(0x0), v54688(0x0), v54687
    0x68d0x54: v5468d(0x0) = CONST 
    0x6900x54: v54690 = EQ v54686, v5468d(0x0)
    0x6910x54: v54691(0x699) = CONST 
    0x6940x54: JUMPI v54691(0x699), v54690

    Begin block 0x6950x54
    prev=[0x6780x54], succ=[]
    =================================
    0x6950x54: v54695 = RETURNDATASIZE 
    0x6960x54: v54696(0x0) = CONST 
    0x6980x54: RETURN v54696(0x0), v54695

    Begin block 0x6990x54
    prev=[0x6780x54], succ=[]
    =================================
    0x69a0x54: v5469a = RETURNDATASIZE 
    0x69b0x54: v5469b(0x0) = CONST 
    0x69d0x54: REVERT v5469b(0x0), v5469a

    Begin block 0x5c
    prev=[0x54], succ=[]
    =================================
    0x5c: v5c(0x0) = CONST 
    0x5f: REVERT v5c(0x0), v5c(0x0)

}

function 0x557(0x557arg0x0) private {
    Begin block 0x557
    prev=[], succ=[0x69eB0x557]
    =================================
    0x558: v558(0x0) = CONST 
    0x55a: v55a(0x561) = CONST 
    0x55d: v55d(0x69e) = CONST 
    0x560: JUMP v55d(0x69e)

    Begin block 0x69eB0x557
    prev=[0x557], succ=[0x561]
    =================================
    0x69fS0x557: v69fV557(0x0) = CONST 
    0x6a2S0x557: v6a2V557(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x557: v6c3V557(0x0) = CONST 
    0x6c5S0x557: v6c5V557(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V557(0x0), v6a2V557(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x557: v6c9V557 = SLOAD v6c5V557(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x557: JUMP v55a(0x561)

    Begin block 0x561
    prev=[0x69eB0x557], succ=[0x595, 0x5a3]
    =================================
    0x562: v562(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x577: v577 = AND v562(0xffffffffffffffffffffffffffffffffffffffff), v6c9V557
    0x578: v578 = CALLER 
    0x579: v579(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x58e: v58e = AND v579(0xffffffffffffffffffffffffffffffffffffffff), v578
    0x58f: v58f = EQ v58e, v577
    0x590: v590 = ISZERO v58f
    0x591: v591(0x5a3) = CONST 
    0x594: JUMPI v591(0x5a3), v590

    Begin block 0x595
    prev=[0x561], succ=[0x69eB0x595]
    =================================
    0x595: v595(0x59c) = CONST 
    0x598: v598(0x69e) = CONST 
    0x59b: JUMP v598(0x69e)

    Begin block 0x69eB0x595
    prev=[0x595], succ=[0x59c]
    =================================
    0x69fS0x595: v69fV595(0x0) = CONST 
    0x6a2S0x595: v6a2V595(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x595: v6c3V595(0x0) = CONST 
    0x6c5S0x595: v6c5V595(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V595(0x0), v6a2V595(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x595: v6c9V595 = SLOAD v6c5V595(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x595: JUMP v595(0x59c)

    Begin block 0x59c
    prev=[0x69eB0x595], succ=[0x5ac]
    =================================
    0x59f: v59f(0x5ac) = CONST 
    0x5a2: JUMP v59f(0x5ac)

    Begin block 0x5ac
    prev=[0x59c], succ=[]
    =================================
    0x5ae: RETURNPRIVATE v557arg0, v6c9V595

    Begin block 0x5a3
    prev=[0x561], succ=[0x23d0x557]
    =================================
    0x5a4: v5a4(0x5ab) = CONST 
    0x5a7: v5a7(0x23d) = CONST 
    0x5aa: JUMP v5a7(0x23d)

    Begin block 0x23d0x557
    prev=[0x5a3], succ=[0x2450x557]
    =================================
    0x23e0x557: v55723e(0x245) = CONST 
    0x2410x557: v557241(0x5af) = CONST 
    0x2440x557: CALLPRIVATE v557241(0x5af), v55723e(0x245)

    Begin block 0x2450x557
    prev=[0x23d0x557], succ=[0x647B0x2450x557]
    =================================
    0x2460x557: v557246(0x255) = CONST 
    0x2490x557: v557249(0x250) = CONST 
    0x24c0x557: v55724c(0x647) = CONST 
    0x24f0x557: JUMP v55724c(0x647)

    Begin block 0x647B0x2450x557
    prev=[0x2450x557], succ=[0x2500x557]
    =================================
    0x648S0x2450x557: v648V245557(0x0) = CONST 
    0x64bS0x2450x557: v64bV245557(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450x557: v66cV245557(0x0) = CONST 
    0x66eS0x2450x557: v66eV245557(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV245557(0x0), v64bV245557(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450x557: v672V245557 = SLOAD v66eV245557(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450x557: JUMP v557249(0x250)

    Begin block 0x2500x557
    prev=[0x647B0x2450x557], succ=[0x6780x557]
    =================================
    0x2510x557: v557251(0x678) = CONST 
    0x2540x557: JUMP v557251(0x678)

    Begin block 0x6780x557
    prev=[0x2500x557], succ=[0x6950x557, 0x6990x557]
    =================================
    0x6790x557: v557679 = CALLDATASIZE 
    0x67a0x557: v55767a(0x0) = CONST 
    0x67d0x557: CALLDATACOPY v55767a(0x0), v55767a(0x0), v557679
    0x67e0x557: v55767e(0x0) = CONST 
    0x6810x557: v557681 = CALLDATASIZE 
    0x6820x557: v557682(0x0) = CONST 
    0x6850x557: v557685 = GAS 
    0x6860x557: v557686 = DELEGATECALL v557685, v672V245557, v557682(0x0), v557681, v55767e(0x0), v55767e(0x0)
    0x6870x557: v557687 = RETURNDATASIZE 
    0x6880x557: v557688(0x0) = CONST 
    0x68b0x557: RETURNDATACOPY v557688(0x0), v557688(0x0), v557687
    0x68d0x557: v55768d(0x0) = CONST 
    0x6900x557: v557690 = EQ v557686, v55768d(0x0)
    0x6910x557: v557691(0x699) = CONST 
    0x6940x557: JUMPI v557691(0x699), v557690

    Begin block 0x6950x557
    prev=[0x6780x557], succ=[]
    =================================
    0x6950x557: v557695 = RETURNDATASIZE 
    0x6960x557: v557696(0x0) = CONST 
    0x6980x557: RETURN v557696(0x0), v557695

    Begin block 0x6990x557
    prev=[0x6780x557], succ=[]
    =================================
    0x69a0x557: v55769a = RETURNDATASIZE 
    0x69b0x557: v55769b(0x0) = CONST 
    0x69d0x557: REVERT v55769b(0x0), v55769a

}

function 0x5af(0x5afarg0x0) private {
    Begin block 0x5af
    prev=[], succ=[0x69eB0x5af]
    =================================
    0x5b0: v5b0(0x5b7) = CONST 
    0x5b3: v5b3(0x69e) = CONST 
    0x5b6: JUMP v5b3(0x69e)

    Begin block 0x69eB0x5af
    prev=[0x5af], succ=[0x5b7]
    =================================
    0x69fS0x5af: v69fV5af(0x0) = CONST 
    0x6a2S0x5af: v6a2V5af(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x5af: v6c3V5af(0x0) = CONST 
    0x6c5S0x5af: v6c5V5af(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V5af(0x0), v6a2V5af(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x5af: v6c9V5af = SLOAD v6c5V5af(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x5af: JUMP v5b0(0x5b7)

    Begin block 0x5b7
    prev=[0x69eB0x5af], succ=[0x5ed, 0x63d]
    =================================
    0x5b8: v5b8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5cd: v5cd = AND v5b8(0xffffffffffffffffffffffffffffffffffffffff), v6c9V5af
    0x5ce: v5ce = CALLER 
    0x5cf: v5cf(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5e4: v5e4 = AND v5cf(0xffffffffffffffffffffffffffffffffffffffff), v5ce
    0x5e5: v5e5 = EQ v5e4, v5cd
    0x5e6: v5e6 = ISZERO v5e5
    0x5e7: v5e7 = ISZERO v5e6
    0x5e8: v5e8 = ISZERO v5e7
    0x5e9: v5e9(0x63d) = CONST 
    0x5ec: JUMPI v5e9(0x63d), v5e8

    Begin block 0x5ed
    prev=[0x5b7], succ=[]
    =================================
    0x5ed: v5ed(0x40) = CONST 
    0x5ef: v5ef = MLOAD v5ed(0x40)
    0x5f0: v5f0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x612: MSTORE v5ef, v5f0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x613: v613(0x4) = CONST 
    0x615: v615 = ADD v613(0x4), v5ef
    0x618: v618(0x20) = CONST 
    0x61a: v61a = ADD v618(0x20), v615
    0x61d: v61d(0x20) = SUB v61a, v615
    0x61f: MSTORE v615, v61d(0x20)
    0x620: v620(0x32) = CONST 
    0x623: MSTORE v61a, v620(0x32)
    0x624: v624(0x20) = CONST 
    0x626: v626 = ADD v624(0x20), v61a
    0x628: v628(0x7f2) = CONST 
    0x62b: v62b(0x32) = CONST 
    0x62e: CODECOPY v626, v628(0x7f2), v62b(0x32)
    0x62f: v62f(0x40) = CONST 
    0x631: v631 = ADD v62f(0x40), v626
    0x635: v635(0x40) = CONST 
    0x637: v637 = MLOAD v635(0x40)
    0x63a: v63a(0x84) = SUB v631, v637
    0x63c: REVERT v637, v63a(0x84)

    Begin block 0x63d
    prev=[0x5b7], succ=[0x74dB0x63d]
    =================================
    0x63e: v63e(0x645) = CONST 
    0x641: v641(0x74d) = CONST 
    0x644: JUMP v641(0x74d), v63e(0x645)

    Begin block 0x74dB0x63d
    prev=[0x63d], succ=[0x645]
    =================================
    0x74eS0x63d: JUMP v63e(0x645)

    Begin block 0x645
    prev=[0x74dB0x63d], succ=[]
    =================================
    0x646: RETURNPRIVATE v5afarg0

}

function 0x6cf(0x6cfarg0x0, 0x6cfarg0x1) private {
    Begin block 0x6cf
    prev=[], succ=[0x74f]
    =================================
    0x6d0: v6d0(0x6d8) = CONST 
    0x6d4: v6d4(0x74f) = CONST 
    0x6d7: JUMP v6d4(0x74f)

    Begin block 0x74f
    prev=[0x6cf], succ=[0x7de]
    =================================
    0x750: v750(0x758) = CONST 
    0x754: v754(0x7de) = CONST 
    0x757: JUMP v754(0x7de)

    Begin block 0x7de
    prev=[0x74f], succ=[0x758]
    =================================
    0x7df: v7df(0x0) = CONST 
    0x7e3: v7e3 = EXTCODESIZE v6cfarg0
    0x7e6: v7e6(0x0) = CONST 
    0x7e9: v7e9 = GT v7e3, v7e6(0x0)
    0x7f0: JUMP v750(0x758)

    Begin block 0x758
    prev=[0x7de], succ=[0x75f, 0x7af]
    =================================
    0x759: v759 = ISZERO v7e9
    0x75a: v75a = ISZERO v759
    0x75b: v75b(0x7af) = CONST 
    0x75e: JUMPI v75b(0x7af), v75a

    Begin block 0x75f
    prev=[0x758], succ=[]
    =================================
    0x75f: v75f(0x40) = CONST 
    0x761: v761 = MLOAD v75f(0x40)
    0x762: v762(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x784: MSTORE v761, v762(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x785: v785(0x4) = CONST 
    0x787: v787 = ADD v785(0x4), v761
    0x78a: v78a(0x20) = CONST 
    0x78c: v78c = ADD v78a(0x20), v787
    0x78f: v78f(0x20) = SUB v78c, v787
    0x791: MSTORE v787, v78f(0x20)
    0x792: v792(0x3b) = CONST 
    0x795: MSTORE v78c, v792(0x3b)
    0x796: v796(0x20) = CONST 
    0x798: v798 = ADD v796(0x20), v78c
    0x79a: v79a(0x85a) = CONST 
    0x79d: v79d(0x3b) = CONST 
    0x7a0: CODECOPY v798, v79a(0x85a), v79d(0x3b)
    0x7a1: v7a1(0x40) = CONST 
    0x7a3: v7a3 = ADD v7a1(0x40), v798
    0x7a7: v7a7(0x40) = CONST 
    0x7a9: v7a9 = MLOAD v7a7(0x40)
    0x7ac: v7ac(0x84) = SUB v7a3, v7a9
    0x7ae: REVERT v7a9, v7ac(0x84)

    Begin block 0x7af
    prev=[0x758], succ=[0x6d8]
    =================================
    0x7b0: v7b0(0x0) = CONST 
    0x7b2: v7b2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x7d3: v7d3(0x0) = CONST 
    0x7d5: v7d5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v7d3(0x0), v7b2(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x7da: SSTORE v7d5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v6cfarg0
    0x7dd: JUMP v6d0(0x6d8)

    Begin block 0x6d8
    prev=[0x7af], succ=[]
    =================================
    0x6da: v6da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6ef: v6ef = AND v6da(0xffffffffffffffffffffffffffffffffffffffff), v6cfarg0
    0x6f0: v6f0(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x711: v711(0x40) = CONST 
    0x713: v713 = MLOAD v711(0x40)
    0x714: v714(0x40) = CONST 
    0x716: v716 = MLOAD v714(0x40)
    0x719: v719(0x0) = SUB v713, v716
    0x71b: LOG2 v716, v719(0x0), v6f0(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v6ef
    0x71d: RETURNPRIVATE v6cfarg1

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
    prev=[0x12c], succ=[0x69eB0x2ac]
    =================================
    0x2ad: v2ad(0x2b4) = CONST 
    0x2b0: v2b0(0x69e) = CONST 
    0x2b3: JUMP v2b0(0x69e)

    Begin block 0x69eB0x2ac
    prev=[0x2ac], succ=[0x2b4]
    =================================
    0x69fS0x2ac: v69fV2ac(0x0) = CONST 
    0x6a2S0x2ac: v6a2V2ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x6c3S0x2ac: v6c3V2ac(0x0) = CONST 
    0x6c5S0x2ac: v6c5V2ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v6c3V2ac(0x0), v6a2V2ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6c9S0x2ac: v6c9V2ac = SLOAD v6c5V2ac(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x6ceS0x2ac: JUMP v2ad(0x2b4)

    Begin block 0x2b4
    prev=[0x69eB0x2ac], succ=[0x2e8, 0x376]
    =================================
    0x2b5: v2b5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ca: v2ca = AND v2b5(0xffffffffffffffffffffffffffffffffffffffff), v6c9V2ac
    0x2cb: v2cb = CALLER 
    0x2cc: v2cc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e1: v2e1 = AND v2cc(0xffffffffffffffffffffffffffffffffffffffff), v2cb
    0x2e2: v2e2 = EQ v2e1, v2ca
    0x2e3: v2e3 = ISZERO v2e2
    0x2e4: v2e4(0x376) = CONST 
    0x2e7: JUMPI v2e4(0x376), v2e3

    Begin block 0x2e8
    prev=[0x2b4], succ=[0x2f0]
    =================================
    0x2e8: v2e8(0x2f0) = CONST 
    0x2ec: v2ec(0x6cf) = CONST 
    0x2ef: CALLPRIVATE v2ec(0x6cf), vd7, v2e8(0x2f0)

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
    prev=[0x33a, 0x35b], succ=[0x36c, 0x370]
    =================================
    0x366: v366 = ISZERO v32c
    0x367: v367 = ISZERO v366
    0x368: v368(0x370) = CONST 
    0x36b: JUMPI v368(0x370), v367

    Begin block 0x36c
    prev=[0x360], succ=[]
    =================================
    0x36c: v36c(0x0) = CONST 
    0x36f: REVERT v36c(0x0), v36c(0x0)

    Begin block 0x370
    prev=[0x360], succ=[0x37f]
    =================================
    0x372: v372(0x37f) = CONST 
    0x375: JUMP v372(0x37f)

    Begin block 0x37f
    prev=[0x370], succ=[0x13c]
    =================================
    0x383: JUMP va6(0x13c)

    Begin block 0x13c
    prev=[0x37f], succ=[]
    =================================
    0x13d: STOP 

    Begin block 0x35b
    prev=[0x2f0], succ=[0x360]
    =================================
    0x35c: v35c(0x60) = CONST 

    Begin block 0x376
    prev=[0x2b4], succ=[0x23d0xa5]
    =================================
    0x377: v377(0x37e) = CONST 
    0x37a: v37a(0x23d) = CONST 
    0x37d: JUMP v37a(0x23d)

    Begin block 0x23d0xa5
    prev=[0x376], succ=[0x2450xa5]
    =================================
    0x23e0xa5: va523e(0x245) = CONST 
    0x2410xa5: va5241(0x5af) = CONST 
    0x2440xa5: CALLPRIVATE va5241(0x5af), va523e(0x245)

    Begin block 0x2450xa5
    prev=[0x23d0xa5], succ=[0x647B0x2450xa5]
    =================================
    0x2460xa5: va5246(0x255) = CONST 
    0x2490xa5: va5249(0x250) = CONST 
    0x24c0xa5: va524c(0x647) = CONST 
    0x24f0xa5: JUMP va524c(0x647)

    Begin block 0x647B0x2450xa5
    prev=[0x2450xa5], succ=[0x2500xa5]
    =================================
    0x648S0x2450xa5: v648V245a5(0x0) = CONST 
    0x64bS0x2450xa5: v64bV245a5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x66cS0x2450xa5: v66cV245a5(0x0) = CONST 
    0x66eS0x2450xa5: v66eV245a5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v66cV245a5(0x0), v64bV245a5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x672S0x2450xa5: v672V245a5 = SLOAD v66eV245a5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x677S0x2450xa5: JUMP va5249(0x250)

    Begin block 0x2500xa5
    prev=[0x647B0x2450xa5], succ=[0x6780xa5]
    =================================
    0x2510xa5: va5251(0x678) = CONST 
    0x2540xa5: JUMP va5251(0x678)

    Begin block 0x6780xa5
    prev=[0x2500xa5], succ=[0x6950xa5, 0x6990xa5]
    =================================
    0x6790xa5: va5679 = CALLDATASIZE 
    0x67a0xa5: va567a(0x0) = CONST 
    0x67d0xa5: CALLDATACOPY va567a(0x0), va567a(0x0), va5679
    0x67e0xa5: va567e(0x0) = CONST 
    0x6810xa5: va5681 = CALLDATASIZE 
    0x6820xa5: va5682(0x0) = CONST 
    0x6850xa5: va5685 = GAS 
    0x6860xa5: va5686 = DELEGATECALL va5685, v672V245a5, va5682(0x0), va5681, va567e(0x0), va567e(0x0)
    0x6870xa5: va5687 = RETURNDATASIZE 
    0x6880xa5: va5688(0x0) = CONST 
    0x68b0xa5: RETURNDATACOPY va5688(0x0), va5688(0x0), va5687
    0x68d0xa5: va568d(0x0) = CONST 
    0x6900xa5: va5690 = EQ va5686, va568d(0x0)
    0x6910xa5: va5691(0x699) = CONST 
    0x6940xa5: JUMPI va5691(0x699), va5690

    Begin block 0x6950xa5
    prev=[0x6780xa5], succ=[]
    =================================
    0x6950xa5: va5695 = RETURNDATASIZE 
    0x6960xa5: va5696(0x0) = CONST 
    0x6980xa5: RETURN va5696(0x0), va5695

    Begin block 0x6990xa5
    prev=[0x6780xa5], succ=[]
    =================================
    0x69a0xa5: va569a = RETURNDATASIZE 
    0x69b0xa5: va569b(0x0) = CONST 
    0x69d0xa5: REVERT va569b(0x0), va569a

}

