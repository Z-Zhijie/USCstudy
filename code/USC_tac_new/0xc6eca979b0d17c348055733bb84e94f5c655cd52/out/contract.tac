function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x460]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x458: v458(0x460) = CONST 
    0x459: JUMPI v458(0x460), v8

    Begin block 0xd
    prev=[0x0], succ=[0x463, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x900f010) = CONST 
    0x19: v19 = EQ v14(0x900f010), v12
    0x45a: v45a(0x463) = CONST 
    0x45b: JUMPI v45a(0x463), v19

    Begin block 0x463
    prev=[0xd], succ=[]
    =================================
    0x464: v464(0x6b) = CONST 
    0x465: CALLPRIVATE v464(0x6b)

    Begin block 0x1e
    prev=[0xd], succ=[0x466, 0x29]
    =================================
    0x1f: v1f(0x5c60da1b) = CONST 
    0x24: v24 = EQ v1f(0x5c60da1b), v12
    0x45c: v45c(0x466) = CONST 
    0x45d: JUMPI v45c(0x466), v24

    Begin block 0x466
    prev=[0x1e], succ=[]
    =================================
    0x467: v467(0xfc) = CONST 
    0x468: CALLPRIVATE v467(0xfc)

    Begin block 0x29
    prev=[0x1e], succ=[0x34, 0x469]
    =================================
    0x2a: v2a(0xb996c170) = CONST 
    0x2f: v2f = EQ v2a(0xb996c170), v12
    0x45e: v45e(0x469) = CONST 
    0x45f: JUMPI v45e(0x469), v2f

    Begin block 0x34
    prev=[0x29], succ=[0x390x0]
    =================================
    0x34: v34(0x39) = CONST 
    0x37: JUMP v34(0x39)

    Begin block 0x390x0
    prev=[0x34], succ=[0x1aaB0x390x0]
    =================================
    0x3a0x0: v03a(0x0) = CONST 
    0x3c0x0: v03c(0x43) = CONST 
    0x3f0x0: v03f(0x1aa) = CONST 
    0x420x0: JUMP v03f(0x1aa)

    Begin block 0x1aaB0x390x0
    prev=[0x390x0], succ=[0x430x0]
    =================================
    0x1abS0x390x0: v1abV390(0x0) = CONST 
    0x1aeS0x390x0: v1aeV390(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cfS0x390x0: v1cfV390(0x0) = CONST 
    0x1d1S0x390x0: v1d1V390(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v1cfV390(0x0), v1aeV390(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1d5S0x390x0: v1d5V390 = SLOAD v1d1V390(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1daS0x390x0: JUMP v03c(0x43)

    Begin block 0x430x0
    prev=[0x1aaB0x390x0], succ=[0x620x0, 0x660x0]
    =================================
    0x460x0: v046 = CALLDATASIZE 
    0x470x0: v047(0x0) = CONST 
    0x4a0x0: CALLDATACOPY v047(0x0), v047(0x0), v046
    0x4b0x0: v04b(0x0) = CONST 
    0x4e0x0: v04e = CALLDATASIZE 
    0x4f0x0: v04f(0x0) = CONST 
    0x520x0: v052 = GAS 
    0x530x0: v053 = DELEGATECALL v052, v1d5V390, v04f(0x0), v04e, v04b(0x0), v04b(0x0)
    0x540x0: v054 = RETURNDATASIZE 
    0x550x0: v055(0x0) = CONST 
    0x580x0: RETURNDATACOPY v055(0x0), v055(0x0), v054
    0x5a0x0: v05a(0x0) = CONST 
    0x5d0x0: v05d = EQ v053, v05a(0x0)
    0x5e0x0: v05e(0x66) = CONST 
    0x610x0: JUMPI v05e(0x66), v05d

    Begin block 0x620x0
    prev=[0x430x0], succ=[]
    =================================
    0x620x0: v062 = RETURNDATASIZE 
    0x630x0: v063(0x0) = CONST 
    0x650x0: RETURN v063(0x0), v062

    Begin block 0x660x0
    prev=[0x430x0], succ=[]
    =================================
    0x670x0: v067 = RETURNDATASIZE 
    0x680x0: v068(0x0) = CONST 
    0x6a0x0: REVERT v068(0x0), v067

    Begin block 0x469
    prev=[0x29], succ=[]
    =================================
    0x46a: v46a(0x153) = CONST 
    0x46b: CALLPRIVATE v46a(0x153)

    Begin block 0x460
    prev=[0x0], succ=[]
    =================================
    0x461: v461(0x38) = CONST 
    0x462: CALLPRIVATE v461(0x38)

}

function authentication()() public {
    Begin block 0x153
    prev=[], succ=[0x15b, 0x15f]
    =================================
    0x154: v154 = CALLVALUE 
    0x156: v156 = ISZERO v154
    0x157: v157(0x15f) = CONST 
    0x15a: JUMPI v157(0x15f), v156

    Begin block 0x15b
    prev=[0x153], succ=[]
    =================================
    0x15b: v15b(0x0) = CONST 
    0x15e: REVERT v15b(0x0), v15b(0x0)

    Begin block 0x15f
    prev=[0x153], succ=[0x3afB0x15f]
    =================================
    0x161: v161(0x168) = CONST 
    0x164: v164(0x3af) = CONST 
    0x167: JUMP v164(0x3af)

    Begin block 0x3afB0x15f
    prev=[0x15f], succ=[0x168]
    =================================
    0x3b0S0x15f: v3b0V15f(0x0) = CONST 
    0x3b3S0x15f: v3b3V15f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x3d4S0x15f: v3d4V15f(0x0) = CONST 
    0x3d6S0x15f: v3d6V15f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v3d4V15f(0x0), v3b3V15f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x3daS0x15f: v3daV15f = SLOAD v3d6V15f(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x3dfS0x15f: JUMP v161(0x168)

    Begin block 0x168
    prev=[0x3afB0x15f], succ=[]
    =================================
    0x169: v169(0x40) = CONST 
    0x16b: v16b = MLOAD v169(0x40)
    0x16e: v16e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x183: v183 = AND v16e(0xffffffffffffffffffffffffffffffffffffffff), v3daV15f
    0x184: v184(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x199: v199 = AND v184(0xffffffffffffffffffffffffffffffffffffffff), v183
    0x19b: MSTORE v16b, v199
    0x19c: v19c(0x20) = CONST 
    0x19e: v19e = ADD v19c(0x20), v16b
    0x1a2: v1a2(0x40) = CONST 
    0x1a4: v1a4 = MLOAD v1a2(0x40)
    0x1a7: v1a7(0x20) = SUB v19e, v1a4
    0x1a9: RETURN v1a4, v1a7(0x20)

}

function fallback()() public {
    Begin block 0x38
    prev=[], succ=[0x390x38]
    =================================

    Begin block 0x390x38
    prev=[0x38], succ=[0x1aaB0x390x38]
    =================================
    0x3a0x38: v383a(0x0) = CONST 
    0x3c0x38: v383c(0x43) = CONST 
    0x3f0x38: v383f(0x1aa) = CONST 
    0x420x38: JUMP v383f(0x1aa)

    Begin block 0x1aaB0x390x38
    prev=[0x390x38], succ=[0x430x38]
    =================================
    0x1abS0x390x38: v1abV3938(0x0) = CONST 
    0x1aeS0x390x38: v1aeV3938(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cfS0x390x38: v1cfV3938(0x0) = CONST 
    0x1d1S0x390x38: v1d1V3938(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v1cfV3938(0x0), v1aeV3938(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1d5S0x390x38: v1d5V3938 = SLOAD v1d1V3938(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1daS0x390x38: JUMP v383c(0x43)

    Begin block 0x430x38
    prev=[0x1aaB0x390x38], succ=[0x620x38, 0x660x38]
    =================================
    0x460x38: v3846 = CALLDATASIZE 
    0x470x38: v3847(0x0) = CONST 
    0x4a0x38: CALLDATACOPY v3847(0x0), v3847(0x0), v3846
    0x4b0x38: v384b(0x0) = CONST 
    0x4e0x38: v384e = CALLDATASIZE 
    0x4f0x38: v384f(0x0) = CONST 
    0x520x38: v3852 = GAS 
    0x530x38: v3853 = DELEGATECALL v3852, v1d5V3938, v384f(0x0), v384e, v384b(0x0), v384b(0x0)
    0x540x38: v3854 = RETURNDATASIZE 
    0x550x38: v3855(0x0) = CONST 
    0x580x38: RETURNDATACOPY v3855(0x0), v3855(0x0), v3854
    0x5a0x38: v385a(0x0) = CONST 
    0x5d0x38: v385d = EQ v3853, v385a(0x0)
    0x5e0x38: v385e(0x66) = CONST 
    0x610x38: JUMPI v385e(0x66), v385d

    Begin block 0x620x38
    prev=[0x430x38], succ=[]
    =================================
    0x620x38: v3862 = RETURNDATASIZE 
    0x630x38: v3863(0x0) = CONST 
    0x650x38: RETURN v3863(0x0), v3862

    Begin block 0x660x38
    prev=[0x430x38], succ=[]
    =================================
    0x670x38: v3867 = RETURNDATASIZE 
    0x680x38: v3868(0x0) = CONST 
    0x6a0x38: REVERT v3868(0x0), v3867

}

function upgrade(address)() public {
    Begin block 0x6b
    prev=[], succ=[0x73, 0x77]
    =================================
    0x6c: v6c = CALLVALUE 
    0x6e: v6e = ISZERO v6c
    0x6f: v6f(0x77) = CONST 
    0x72: JUMPI v6f(0x77), v6e

    Begin block 0x73
    prev=[0x6b], succ=[]
    =================================
    0x73: v73(0x0) = CONST 
    0x76: REVERT v73(0x0), v73(0x0)

    Begin block 0x77
    prev=[0x6b], succ=[0x8a, 0x8e]
    =================================
    0x79: v79(0xba) = CONST 
    0x7c: v7c(0x4) = CONST 
    0x7f: v7f = CALLDATASIZE 
    0x80: v80 = SUB v7f, v7c(0x4)
    0x81: v81(0x20) = CONST 
    0x84: v84 = LT v80, v81(0x20)
    0x85: v85 = ISZERO v84
    0x86: v86(0x8e) = CONST 
    0x89: JUMPI v86(0x8e), v85

    Begin block 0x8a
    prev=[0x77], succ=[]
    =================================
    0x8a: v8a(0x0) = CONST 
    0x8d: REVERT v8a(0x0), v8a(0x0)

    Begin block 0x8e
    prev=[0x77], succ=[0x1db]
    =================================
    0x90: v90 = ADD v7c(0x4), v80
    0x94: v94 = CALLDATALOAD v7c(0x4)
    0x95: v95(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaa: vaa = AND v95(0xffffffffffffffffffffffffffffffffffffffff), v94
    0xac: vac(0x20) = CONST 
    0xae: vae(0x24) = ADD vac(0x20), v7c(0x4)
    0xb6: vb6(0x1db) = CONST 
    0xb9: JUMP vb6(0x1db)

    Begin block 0x1db
    prev=[0x8e], succ=[0x3afB0x1db]
    =================================
    0x1dc: v1dc(0x0) = CONST 
    0x1de: v1de(0x1e5) = CONST 
    0x1e1: v1e1(0x3af) = CONST 
    0x1e4: JUMP v1e1(0x3af)

    Begin block 0x3afB0x1db
    prev=[0x1db], succ=[0x1e5]
    =================================
    0x3b0S0x1db: v3b0V1db(0x0) = CONST 
    0x3b3S0x1db: v3b3V1db(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x3d4S0x1db: v3d4V1db(0x0) = CONST 
    0x3d6S0x1db: v3d6V1db(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = SHL v3d4V1db(0x0), v3b3V1db(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x3daS0x1db: v3daV1db = SLOAD v3d6V1db(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x3dfS0x1db: JUMP v1de(0x1e5)

    Begin block 0x1e5
    prev=[0x3afB0x1db], succ=[0x218, 0x285]
    =================================
    0x1e6: v1e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1fb: v1fb = AND v1e6(0xffffffffffffffffffffffffffffffffffffffff), v3daV1db
    0x1fc: v1fc = CALLER 
    0x1fd: v1fd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x212: v212 = AND v1fd(0xffffffffffffffffffffffffffffffffffffffff), v1fc
    0x213: v213 = EQ v212, v1fb
    0x214: v214(0x285) = CONST 
    0x217: JUMPI v214(0x285), v213

    Begin block 0x218
    prev=[0x1e5], succ=[]
    =================================
    0x218: v218(0x40) = CONST 
    0x21a: v21a = MLOAD v218(0x40)
    0x21b: v21b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x23d: MSTORE v21a, v21b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x23e: v23e(0x4) = CONST 
    0x240: v240 = ADD v23e(0x4), v21a
    0x243: v243(0x20) = CONST 
    0x245: v245 = ADD v243(0x20), v240
    0x248: v248(0x20) = SUB v245, v240
    0x24a: MSTORE v240, v248(0x20)
    0x24b: v24b(0x19) = CONST 
    0x24e: MSTORE v245, v24b(0x19)
    0x24f: v24f(0x20) = CONST 
    0x251: v251 = ADD v24f(0x20), v245
    0x253: v253(0x5570677261646561626c652e617574682e454944303030303100000000000000) = CONST 
    0x275: MSTORE v251, v253(0x5570677261646561626c652e617574682e454944303030303100000000000000)
    0x277: v277(0x20) = CONST 
    0x279: v279 = ADD v277(0x20), v251
    0x27d: v27d(0x40) = CONST 
    0x27f: v27f = MLOAD v27d(0x40)
    0x282: v282(0x64) = SUB v279, v27f
    0x284: REVERT v27f, v282(0x64)

    Begin block 0x285
    prev=[0x1e5], succ=[0x2bb, 0x328]
    =================================
    0x286: v286(0x0) = CONST 
    0x288: v288(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29d: v29d(0x0) = AND v288(0xffffffffffffffffffffffffffffffffffffffff), v286(0x0)
    0x29f: v29f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b4: v2b4 = AND v29f(0xffffffffffffffffffffffffffffffffffffffff), vaa
    0x2b5: v2b5 = EQ v2b4, v29d(0x0)
    0x2b6: v2b6 = ISZERO v2b5
    0x2b7: v2b7(0x328) = CONST 
    0x2ba: JUMPI v2b7(0x328), v2b6

    Begin block 0x2bb
    prev=[0x285], succ=[]
    =================================
    0x2bb: v2bb(0x40) = CONST 
    0x2bd: v2bd = MLOAD v2bb(0x40)
    0x2be: v2be(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2e0: MSTORE v2bd, v2be(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2e1: v2e1(0x4) = CONST 
    0x2e3: v2e3 = ADD v2e1(0x4), v2bd
    0x2e6: v2e6(0x20) = CONST 
    0x2e8: v2e8 = ADD v2e6(0x20), v2e3
    0x2eb: v2eb(0x20) = SUB v2e8, v2e3
    0x2ed: MSTORE v2e3, v2eb(0x20)
    0x2ee: v2ee(0x1c) = CONST 
    0x2f1: MSTORE v2e8, v2ee(0x1c)
    0x2f2: v2f2(0x20) = CONST 
    0x2f4: v2f4 = ADD v2f2(0x20), v2e8
    0x2f6: v2f6(0x5570677261646561626c652e757067726164652e454944303030393000000000) = CONST 
    0x318: MSTORE v2f4, v2f6(0x5570677261646561626c652e757067726164652e454944303030393000000000)
    0x31a: v31a(0x20) = CONST 
    0x31c: v31c = ADD v31a(0x20), v2f4
    0x320: v320(0x40) = CONST 
    0x322: v322 = MLOAD v320(0x40)
    0x325: v325(0x64) = SUB v31c, v322
    0x327: REVERT v322, v325(0x64)

    Begin block 0x328
    prev=[0x285], succ=[0x3e0]
    =================================
    0x329: v329(0x0) = CONST 
    0x32b: v32b(0x333) = CONST 
    0x32f: v32f(0x3e0) = CONST 
    0x332: JUMP v32f(0x3e0)

    Begin block 0x3e0
    prev=[0x328], succ=[0x1aaB0x3e0]
    =================================
    0x3e1: v3e1(0x0) = CONST 
    0x3e4: v3e4(0x3eb) = CONST 
    0x3e7: v3e7(0x1aa) = CONST 
    0x3ea: JUMP v3e7(0x1aa)

    Begin block 0x1aaB0x3e0
    prev=[0x3e0], succ=[0x3eb]
    =================================
    0x1abS0x3e0: v1abV3e0(0x0) = CONST 
    0x1aeS0x3e0: v1aeV3e0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cfS0x3e0: v1cfV3e0(0x0) = CONST 
    0x1d1S0x3e0: v1d1V3e0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v1cfV3e0(0x0), v1aeV3e0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1d5S0x3e0: v1d5V3e0 = SLOAD v1d1V3e0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1daS0x3e0: JUMP v3e4(0x3eb)

    Begin block 0x3eb
    prev=[0x1aaB0x3e0], succ=[0x333]
    =================================
    0x3ee: v3ee(0x0) = CONST 
    0x3f0: v3f0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x411: v411(0x0) = CONST 
    0x413: v413(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v411(0x0), v3f0(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x418: SSTORE v413(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), vaa
    0x421: JUMP v32b(0x333)

    Begin block 0x333
    prev=[0x3eb], succ=[0xba]
    =================================
    0x337: v337(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x34c: v34c = AND v337(0xffffffffffffffffffffffffffffffffffffffff), vaa
    0x34e: v34e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x363: v363 = AND v34e(0xffffffffffffffffffffffffffffffffffffffff), v1d5V3e0
    0x364: v364 = CALLER 
    0x365: v365(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x37a: v37a = AND v365(0xffffffffffffffffffffffffffffffffffffffff), v364
    0x37b: v37b(0x8c78349fc44add47ae711ddc6e926b7845597c57473e587420693d8d0547845a) = CONST 
    0x39c: v39c(0x40) = CONST 
    0x39e: v39e = MLOAD v39c(0x40)
    0x39f: v39f(0x40) = CONST 
    0x3a1: v3a1 = MLOAD v39f(0x40)
    0x3a4: v3a4(0x0) = SUB v39e, v3a1
    0x3a6: LOG4 v3a1, v3a4(0x0), v37b(0x8c78349fc44add47ae711ddc6e926b7845597c57473e587420693d8d0547845a), v37a, v363, v34c
    0x3ae: JUMP v79(0xba)

    Begin block 0xba
    prev=[0x333], succ=[]
    =================================
    0xbb: vbb(0x40) = CONST 
    0xbd: vbd = MLOAD vbb(0x40)
    0xc0: vc0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd5: vd5 = AND vc0(0xffffffffffffffffffffffffffffffffffffffff), v1d5V3e0
    0xd6: vd6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xeb: veb = AND vd6(0xffffffffffffffffffffffffffffffffffffffff), vd5
    0xed: MSTORE vbd, veb
    0xee: vee(0x20) = CONST 
    0xf0: vf0 = ADD vee(0x20), vbd
    0xf4: vf4(0x40) = CONST 
    0xf6: vf6 = MLOAD vf4(0x40)
    0xf9: vf9(0x20) = SUB vf0, vf6
    0xfb: RETURN vf6, vf9(0x20)

}

function implementation()() public {
    Begin block 0xfc
    prev=[], succ=[0x104, 0x108]
    =================================
    0xfd: vfd = CALLVALUE 
    0xff: vff = ISZERO vfd
    0x100: v100(0x108) = CONST 
    0x103: JUMPI v100(0x108), vff

    Begin block 0x104
    prev=[0xfc], succ=[]
    =================================
    0x104: v104(0x0) = CONST 
    0x107: REVERT v104(0x0), v104(0x0)

    Begin block 0x108
    prev=[0xfc], succ=[0x1aaB0x108]
    =================================
    0x10a: v10a(0x111) = CONST 
    0x10d: v10d(0x1aa) = CONST 
    0x110: JUMP v10d(0x1aa)

    Begin block 0x1aaB0x108
    prev=[0x108], succ=[0x111]
    =================================
    0x1abS0x108: v1abV108(0x0) = CONST 
    0x1aeS0x108: v1aeV108(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x1cfS0x108: v1cfV108(0x0) = CONST 
    0x1d1S0x108: v1d1V108(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = SHL v1cfV108(0x0), v1aeV108(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1d5S0x108: v1d5V108 = SLOAD v1d1V108(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x1daS0x108: JUMP v10a(0x111)

    Begin block 0x111
    prev=[0x1aaB0x108], succ=[]
    =================================
    0x112: v112(0x40) = CONST 
    0x114: v114 = MLOAD v112(0x40)
    0x117: v117(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12c: v12c = AND v117(0xffffffffffffffffffffffffffffffffffffffff), v1d5V108
    0x12d: v12d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x142: v142 = AND v12d(0xffffffffffffffffffffffffffffffffffffffff), v12c
    0x144: MSTORE v114, v142
    0x145: v145(0x20) = CONST 
    0x147: v147 = ADD v145(0x20), v114
    0x14b: v14b(0x40) = CONST 
    0x14d: v14d = MLOAD v14b(0x40)
    0x150: v150(0x20) = SUB v147, v14d
    0x152: RETURN v14d, v150(0x20)

}

