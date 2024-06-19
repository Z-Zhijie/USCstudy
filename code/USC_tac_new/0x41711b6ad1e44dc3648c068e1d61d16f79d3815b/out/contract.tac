function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x8fc]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x8f0: v8f0(0x8fc) = CONST 
    0x8f1: JUMPI v8f0(0x8fc), v8

    Begin block 0xd
    prev=[0x0], succ=[0x8ff, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x3659cfe6) = CONST 
    0x3c: v3c = EQ v37(0x3659cfe6), v35
    0x8f2: v8f2(0x8ff) = CONST 
    0x8f3: JUMPI v8f2(0x8ff), v3c

    Begin block 0x8ff
    prev=[0xd], succ=[]
    =================================
    0x900: v900(0x77) = CONST 
    0x901: CALLPRIVATE v900(0x77)

    Begin block 0x41
    prev=[0xd], succ=[0x902, 0x4c]
    =================================
    0x42: v42(0x4f1ef286) = CONST 
    0x47: v47 = EQ v42(0x4f1ef286), v35
    0x8f4: v8f4(0x902) = CONST 
    0x8f5: JUMPI v8f4(0x902), v47

    Begin block 0x902
    prev=[0x41], succ=[]
    =================================
    0x903: v903(0xc8) = CONST 
    0x904: CALLPRIVATE v903(0xc8)

    Begin block 0x4c
    prev=[0x41], succ=[0x905, 0x57]
    =================================
    0x4d: v4d(0x5c60da1b) = CONST 
    0x52: v52 = EQ v4d(0x5c60da1b), v35
    0x8f6: v8f6(0x905) = CONST 
    0x8f7: JUMPI v8f6(0x905), v52

    Begin block 0x905
    prev=[0x4c], succ=[]
    =================================
    0x906: v906(0x161) = CONST 
    0x907: CALLPRIVATE v906(0x161)

    Begin block 0x57
    prev=[0x4c], succ=[0x908, 0x62]
    =================================
    0x58: v58(0x8f283970) = CONST 
    0x5d: v5d = EQ v58(0x8f283970), v35
    0x8f8: v8f8(0x908) = CONST 
    0x8f9: JUMPI v8f8(0x908), v5d

    Begin block 0x908
    prev=[0x57], succ=[]
    =================================
    0x909: v909(0x1b8) = CONST 
    0x90a: CALLPRIVATE v909(0x1b8)

    Begin block 0x62
    prev=[0x57], succ=[0x8fc, 0x90b]
    =================================
    0x63: v63(0xf851a440) = CONST 
    0x68: v68 = EQ v63(0xf851a440), v35
    0x8fa: v8fa(0x90b) = CONST 
    0x8fb: JUMPI v8fa(0x90b), v68

    Begin block 0x8fc
    prev=[0x0, 0x62], succ=[]
    =================================
    0x8fd: v8fd(0x6d) = CONST 
    0x8fe: CALLPRIVATE v8fd(0x6d)

    Begin block 0x90b
    prev=[0x62], succ=[]
    =================================
    0x90c: v90c(0x209) = CONST 
    0x90d: CALLPRIVATE v90c(0x209)

}

function implementation()() public {
    Begin block 0x161
    prev=[], succ=[0x169, 0x16d]
    =================================
    0x162: v162 = CALLVALUE 
    0x164: v164 = ISZERO v162
    0x165: v165(0x16d) = CONST 
    0x168: JUMPI v165(0x16d), v164

    Begin block 0x169
    prev=[0x161], succ=[]
    =================================
    0x169: v169(0x0) = CONST 
    0x16c: REVERT v169(0x0), v169(0x0)

    Begin block 0x16d
    prev=[0x161], succ=[0x176]
    =================================
    0x16f: v16f(0x176) = CONST 
    0x172: v172(0x3a7) = CONST 
    0x175: v175_0 = CALLPRIVATE v172(0x3a7), v16f(0x176)

    Begin block 0x176
    prev=[0x16d], succ=[]
    =================================
    0x177: v177(0x40) = CONST 
    0x179: v179 = MLOAD v177(0x40)
    0x17c: v17c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x191: v191 = AND v17c(0xffffffffffffffffffffffffffffffffffffffff), v175_0
    0x192: v192(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1a7: v1a7 = AND v192(0xffffffffffffffffffffffffffffffffffffffff), v191
    0x1a9: MSTORE v179, v1a7
    0x1aa: v1aa(0x20) = CONST 
    0x1ac: v1ac = ADD v1aa(0x20), v179
    0x1b0: v1b0(0x40) = CONST 
    0x1b2: v1b2 = MLOAD v1b0(0x40)
    0x1b5: v1b5(0x20) = SUB v1ac, v1b2
    0x1b7: RETURN v1b2, v1b5(0x20)

}

function changeAdmin(address)() public {
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
    prev=[0x1b8], succ=[0x1d7, 0x1db]
    =================================
    0x1c6: v1c6(0x207) = CONST 
    0x1c9: v1c9(0x4) = CONST 
    0x1cc: v1cc = CALLDATASIZE 
    0x1cd: v1cd = SUB v1cc, v1c9(0x4)
    0x1ce: v1ce(0x20) = CONST 
    0x1d1: v1d1 = LT v1cd, v1ce(0x20)
    0x1d2: v1d2 = ISZERO v1d1
    0x1d3: v1d3(0x1db) = CONST 
    0x1d6: JUMPI v1d3(0x1db), v1d2

    Begin block 0x1d7
    prev=[0x1c4], succ=[]
    =================================
    0x1d7: v1d7(0x0) = CONST 
    0x1da: REVERT v1d7(0x0), v1d7(0x0)

    Begin block 0x1db
    prev=[0x1c4], succ=[0x3ff]
    =================================
    0x1dd: v1dd = ADD v1c9(0x4), v1cd
    0x1e1: v1e1 = CALLDATALOAD v1c9(0x4)
    0x1e2: v1e2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f7: v1f7 = AND v1e2(0xffffffffffffffffffffffffffffffffffffffff), v1e1
    0x1f9: v1f9(0x20) = CONST 
    0x1fb: v1fb(0x24) = ADD v1f9(0x20), v1c9(0x4)
    0x203: v203(0x3ff) = CONST 
    0x206: JUMP v203(0x3ff)

    Begin block 0x3ff
    prev=[0x1db], succ=[0x747B0x3ff]
    =================================
    0x400: v400(0x407) = CONST 
    0x403: v403(0x747) = CONST 
    0x406: JUMP v403(0x747)

    Begin block 0x747B0x3ff
    prev=[0x3ff], succ=[0x407]
    =================================
    0x748S0x3ff: v748V3ff(0x0) = CONST 
    0x74bS0x3ff: v74bV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x3ff: v76cV3ff(0x1) = CONST 
    0x76eS0x3ff: v76eV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV3ff(0x1), v74bV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x3ff: v772V3ff = SLOAD v76eV3ff(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x3ff: JUMP v400(0x407)

    Begin block 0x407
    prev=[0x747B0x3ff], succ=[0x43b, 0x5b1]
    =================================
    0x408: v408(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x41d: v41d = AND v408(0xffffffffffffffffffffffffffffffffffffffff), v772V3ff
    0x41e: v41e = CALLER 
    0x41f: v41f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x434: v434 = AND v41f(0xffffffffffffffffffffffffffffffffffffffff), v41e
    0x435: v435 = EQ v434, v41d
    0x436: v436 = ISZERO v435
    0x437: v437(0x5b1) = CONST 
    0x43a: JUMPI v437(0x5b1), v436

    Begin block 0x43b
    prev=[0x407], succ=[0x472, 0x505]
    =================================
    0x43b: v43b(0x0) = CONST 
    0x43d: v43d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x452: v452(0x0) = AND v43d(0xffffffffffffffffffffffffffffffffffffffff), v43b(0x0)
    0x454: v454(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x469: v469 = AND v454(0xffffffffffffffffffffffffffffffffffffffff), v1f7
    0x46a: v46a = EQ v469, v452(0x0)
    0x46b: v46b = ISZERO v46a
    0x46c: v46c = ISZERO v46b
    0x46d: v46d = ISZERO v46c
    0x46e: v46e(0x505) = CONST 
    0x471: JUMPI v46e(0x505), v46d

    Begin block 0x472
    prev=[0x43b], succ=[]
    =================================
    0x472: v472(0x40) = CONST 
    0x474: v474 = MLOAD v472(0x40)
    0x475: v475(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x497: MSTORE v474, v475(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x498: v498(0x4) = CONST 
    0x49a: v49a = ADD v498(0x4), v474
    0x49d: v49d(0x20) = CONST 
    0x49f: v49f = ADD v49d(0x20), v49a
    0x4a2: v4a2(0x20) = SUB v49f, v49a
    0x4a4: MSTORE v49a, v4a2(0x20)
    0x4a5: v4a5(0x36) = CONST 
    0x4a8: MSTORE v49f, v4a5(0x36)
    0x4a9: v4a9(0x20) = CONST 
    0x4ab: v4ab = ADD v4a9(0x20), v49f
    0x4ad: v4ad(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f) = CONST 
    0x4cf: MSTORE v4ab, v4ad(0x43616e6e6f74206368616e6765207468652061646d696e206f6620612070726f)
    0x4d0: v4d0(0x20) = CONST 
    0x4d2: v4d2 = ADD v4d0(0x20), v4ab
    0x4d3: v4d3(0x787920746f20746865207a65726f206164647265737300000000000000000000) = CONST 
    0x4f5: MSTORE v4d2, v4d3(0x787920746f20746865207a65726f206164647265737300000000000000000000)
    0x4f7: v4f7(0x40) = CONST 
    0x4f9: v4f9 = ADD v4f7(0x40), v4ab
    0x4fd: v4fd(0x40) = CONST 
    0x4ff: v4ff = MLOAD v4fd(0x40)
    0x502: v502(0x84) = SUB v4f9, v4ff
    0x504: REVERT v4ff, v502(0x84)

    Begin block 0x505
    prev=[0x43b], succ=[0x747B0x505]
    =================================
    0x506: v506(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x527: v527(0x52e) = CONST 
    0x52a: v52a(0x747) = CONST 
    0x52d: JUMP v52a(0x747)

    Begin block 0x747B0x505
    prev=[0x505], succ=[0x52e]
    =================================
    0x748S0x505: v748V505(0x0) = CONST 
    0x74bS0x505: v74bV505(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x505: v76cV505(0x1) = CONST 
    0x76eS0x505: v76eV505(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV505(0x1), v74bV505(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x505: v772V505 = SLOAD v76eV505(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x505: JUMP v527(0x52e)

    Begin block 0x52e
    prev=[0x747B0x505], succ=[0x7c7]
    =================================
    0x530: v530(0x40) = CONST 
    0x532: v532 = MLOAD v530(0x40)
    0x535: v535(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x54a: v54a = AND v535(0xffffffffffffffffffffffffffffffffffffffff), v772V505
    0x54b: v54b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x560: v560 = AND v54b(0xffffffffffffffffffffffffffffffffffffffff), v54a
    0x562: MSTORE v532, v560
    0x563: v563(0x20) = CONST 
    0x565: v565 = ADD v563(0x20), v532
    0x567: v567(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x57c: v57c = AND v567(0xffffffffffffffffffffffffffffffffffffffff), v1f7
    0x57d: v57d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x592: v592 = AND v57d(0xffffffffffffffffffffffffffffffffffffffff), v57c
    0x594: MSTORE v565, v592
    0x595: v595(0x20) = CONST 
    0x597: v597 = ADD v595(0x20), v565
    0x59c: v59c(0x40) = CONST 
    0x59e: v59e = MLOAD v59c(0x40)
    0x5a1: v5a1(0x40) = SUB v597, v59e
    0x5a3: LOG1 v59e, v5a1(0x40), v506(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x5a4: v5a4(0x5ac) = CONST 
    0x5a8: v5a8(0x7c7) = CONST 
    0x5ab: JUMP v5a8(0x7c7)

    Begin block 0x7c7
    prev=[0x52e], succ=[0x5ac]
    =================================
    0x7c8: v7c8(0x0) = CONST 
    0x7ca: v7ca(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x7eb: v7eb(0x1) = CONST 
    0x7ed: v7ed(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v7eb(0x1), v7ca(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x7f2: SSTORE v7ed(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v1f7
    0x7f5: JUMP v5a4(0x5ac)

    Begin block 0x5ac
    prev=[0x7c7], succ=[0x5ba]
    =================================
    0x5ad: v5ad(0x5ba) = CONST 
    0x5b0: JUMP v5ad(0x5ba)

    Begin block 0x5ba
    prev=[0x5ac], succ=[0x207]
    =================================
    0x5bc: JUMP v1c6(0x207)

    Begin block 0x207
    prev=[0x5ba], succ=[]
    =================================
    0x208: STOP 

    Begin block 0x5b1
    prev=[0x407], succ=[0x2600x1b8]
    =================================
    0x5b2: v5b2(0x5b9) = CONST 
    0x5b5: v5b5(0x260) = CONST 
    0x5b8: JUMP v5b5(0x260)

    Begin block 0x2600x1b8
    prev=[0x5b1], succ=[0x2680x1b8]
    =================================
    0x2610x1b8: v1b8261(0x268) = CONST 
    0x2640x1b8: v1b8264(0x615) = CONST 
    0x2670x1b8: CALLPRIVATE v1b8264(0x615), v1b8261(0x268)

    Begin block 0x2680x1b8
    prev=[0x2600x1b8], succ=[0x6f0B0x2680x1b8]
    =================================
    0x2690x1b8: v1b8269(0x278) = CONST 
    0x26c0x1b8: v1b826c(0x273) = CONST 
    0x26f0x1b8: v1b826f(0x6f0) = CONST 
    0x2720x1b8: JUMP v1b826f(0x6f0)

    Begin block 0x6f0B0x2680x1b8
    prev=[0x2680x1b8], succ=[0x2730x1b8]
    =================================
    0x6f1S0x2680x1b8: v6f1V2681b8(0x0) = CONST 
    0x6f4S0x2680x1b8: v6f4V2681b8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680x1b8: v715V2681b8(0x1) = CONST 
    0x717S0x2680x1b8: v717V2681b8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V2681b8(0x1), v6f4V2681b8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680x1b8: v71bV2681b8 = SLOAD v717V2681b8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680x1b8: JUMP v1b826c(0x273)

    Begin block 0x2730x1b8
    prev=[0x6f0B0x2680x1b8], succ=[0x7210x1b8]
    =================================
    0x2740x1b8: v1b8274(0x721) = CONST 
    0x2770x1b8: JUMP v1b8274(0x721)

    Begin block 0x7210x1b8
    prev=[0x2730x1b8], succ=[0x73e0x1b8, 0x7420x1b8]
    =================================
    0x7220x1b8: v1b8722 = CALLDATASIZE 
    0x7230x1b8: v1b8723(0x0) = CONST 
    0x7260x1b8: CALLDATACOPY v1b8723(0x0), v1b8723(0x0), v1b8722
    0x7270x1b8: v1b8727(0x0) = CONST 
    0x72a0x1b8: v1b872a = CALLDATASIZE 
    0x72b0x1b8: v1b872b(0x0) = CONST 
    0x72e0x1b8: v1b872e = GAS 
    0x72f0x1b8: v1b872f = DELEGATECALL v1b872e, v71bV2681b8, v1b872b(0x0), v1b872a, v1b8727(0x0), v1b8727(0x0)
    0x7300x1b8: v1b8730 = RETURNDATASIZE 
    0x7310x1b8: v1b8731(0x0) = CONST 
    0x7340x1b8: RETURNDATACOPY v1b8731(0x0), v1b8731(0x0), v1b8730
    0x7360x1b8: v1b8736(0x0) = CONST 
    0x7390x1b8: v1b8739 = EQ v1b872f, v1b8736(0x0)
    0x73a0x1b8: v1b873a(0x742) = CONST 
    0x73d0x1b8: JUMPI v1b873a(0x742), v1b8739

    Begin block 0x73e0x1b8
    prev=[0x7210x1b8], succ=[]
    =================================
    0x73e0x1b8: v1b873e = RETURNDATASIZE 
    0x73f0x1b8: v1b873f(0x0) = CONST 
    0x7410x1b8: RETURN v1b873f(0x0), v1b873e

    Begin block 0x7420x1b8
    prev=[0x7210x1b8], succ=[]
    =================================
    0x7430x1b8: v1b8743 = RETURNDATASIZE 
    0x7440x1b8: v1b8744(0x0) = CONST 
    0x7460x1b8: REVERT v1b8744(0x0), v1b8743

}

function admin()() public {
    Begin block 0x209
    prev=[], succ=[0x211, 0x215]
    =================================
    0x20a: v20a = CALLVALUE 
    0x20c: v20c = ISZERO v20a
    0x20d: v20d(0x215) = CONST 
    0x210: JUMPI v20d(0x215), v20c

    Begin block 0x211
    prev=[0x209], succ=[]
    =================================
    0x211: v211(0x0) = CONST 
    0x214: REVERT v211(0x0), v211(0x0)

    Begin block 0x215
    prev=[0x209], succ=[0x21e]
    =================================
    0x217: v217(0x21e) = CONST 
    0x21a: v21a(0x5bd) = CONST 
    0x21d: v21d_0 = CALLPRIVATE v21a(0x5bd), v217(0x21e)

    Begin block 0x21e
    prev=[0x215], succ=[]
    =================================
    0x21f: v21f(0x40) = CONST 
    0x221: v221 = MLOAD v21f(0x40)
    0x224: v224(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x239: v239 = AND v224(0xffffffffffffffffffffffffffffffffffffffff), v21d_0
    0x23a: v23a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24f: v24f = AND v23a(0xffffffffffffffffffffffffffffffffffffffff), v239
    0x251: MSTORE v221, v24f
    0x252: v252(0x20) = CONST 
    0x254: v254 = ADD v252(0x20), v221
    0x258: v258(0x40) = CONST 
    0x25a: v25a = MLOAD v258(0x40)
    0x25d: v25d(0x20) = SUB v254, v25a
    0x25f: RETURN v25a, v25d(0x20)

}

function 0x3a7(0x3a7arg0x0) private {
    Begin block 0x3a7
    prev=[], succ=[0x747B0x3a7]
    =================================
    0x3a8: v3a8(0x0) = CONST 
    0x3aa: v3aa(0x3b1) = CONST 
    0x3ad: v3ad(0x747) = CONST 
    0x3b0: JUMP v3ad(0x747)

    Begin block 0x747B0x3a7
    prev=[0x3a7], succ=[0x3b1]
    =================================
    0x748S0x3a7: v748V3a7(0x0) = CONST 
    0x74bS0x3a7: v74bV3a7(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x3a7: v76cV3a7(0x1) = CONST 
    0x76eS0x3a7: v76eV3a7(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV3a7(0x1), v74bV3a7(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x3a7: v772V3a7 = SLOAD v76eV3a7(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x3a7: JUMP v3aa(0x3b1)

    Begin block 0x3b1
    prev=[0x747B0x3a7], succ=[0x3e5, 0x3f3]
    =================================
    0x3b2: v3b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c7: v3c7 = AND v3b2(0xffffffffffffffffffffffffffffffffffffffff), v772V3a7
    0x3c8: v3c8 = CALLER 
    0x3c9: v3c9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3de: v3de = AND v3c9(0xffffffffffffffffffffffffffffffffffffffff), v3c8
    0x3df: v3df = EQ v3de, v3c7
    0x3e0: v3e0 = ISZERO v3df
    0x3e1: v3e1(0x3f3) = CONST 
    0x3e4: JUMPI v3e1(0x3f3), v3e0

    Begin block 0x3e5
    prev=[0x3b1], succ=[0x6f0B0x3e5]
    =================================
    0x3e5: v3e5(0x3ec) = CONST 
    0x3e8: v3e8(0x6f0) = CONST 
    0x3eb: JUMP v3e8(0x6f0)

    Begin block 0x6f0B0x3e5
    prev=[0x3e5], succ=[0x3ec]
    =================================
    0x6f1S0x3e5: v6f1V3e5(0x0) = CONST 
    0x6f4S0x3e5: v6f4V3e5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x3e5: v715V3e5(0x1) = CONST 
    0x717S0x3e5: v717V3e5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V3e5(0x1), v6f4V3e5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x3e5: v71bV3e5 = SLOAD v717V3e5(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x3e5: JUMP v3e5(0x3ec)

    Begin block 0x3ec
    prev=[0x6f0B0x3e5], succ=[0x3fc]
    =================================
    0x3ef: v3ef(0x3fc) = CONST 
    0x3f2: JUMP v3ef(0x3fc)

    Begin block 0x3fc
    prev=[0x3ec], succ=[]
    =================================
    0x3fe: RETURNPRIVATE v3a7arg0, v71bV3e5

    Begin block 0x3f3
    prev=[0x3b1], succ=[0x2600x3a7]
    =================================
    0x3f4: v3f4(0x3fb) = CONST 
    0x3f7: v3f7(0x260) = CONST 
    0x3fa: JUMP v3f7(0x260)

    Begin block 0x2600x3a7
    prev=[0x3f3], succ=[0x2680x3a7]
    =================================
    0x2610x3a7: v3a7261(0x268) = CONST 
    0x2640x3a7: v3a7264(0x615) = CONST 
    0x2670x3a7: CALLPRIVATE v3a7264(0x615), v3a7261(0x268)

    Begin block 0x2680x3a7
    prev=[0x2600x3a7], succ=[0x6f0B0x2680x3a7]
    =================================
    0x2690x3a7: v3a7269(0x278) = CONST 
    0x26c0x3a7: v3a726c(0x273) = CONST 
    0x26f0x3a7: v3a726f(0x6f0) = CONST 
    0x2720x3a7: JUMP v3a726f(0x6f0)

    Begin block 0x6f0B0x2680x3a7
    prev=[0x2680x3a7], succ=[0x2730x3a7]
    =================================
    0x6f1S0x2680x3a7: v6f1V2683a7(0x0) = CONST 
    0x6f4S0x2680x3a7: v6f4V2683a7(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680x3a7: v715V2683a7(0x1) = CONST 
    0x717S0x2680x3a7: v717V2683a7(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V2683a7(0x1), v6f4V2683a7(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680x3a7: v71bV2683a7 = SLOAD v717V2683a7(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680x3a7: JUMP v3a726c(0x273)

    Begin block 0x2730x3a7
    prev=[0x6f0B0x2680x3a7], succ=[0x7210x3a7]
    =================================
    0x2740x3a7: v3a7274(0x721) = CONST 
    0x2770x3a7: JUMP v3a7274(0x721)

    Begin block 0x7210x3a7
    prev=[0x2730x3a7], succ=[0x73e0x3a7, 0x7420x3a7]
    =================================
    0x7220x3a7: v3a7722 = CALLDATASIZE 
    0x7230x3a7: v3a7723(0x0) = CONST 
    0x7260x3a7: CALLDATACOPY v3a7723(0x0), v3a7723(0x0), v3a7722
    0x7270x3a7: v3a7727(0x0) = CONST 
    0x72a0x3a7: v3a772a = CALLDATASIZE 
    0x72b0x3a7: v3a772b(0x0) = CONST 
    0x72e0x3a7: v3a772e = GAS 
    0x72f0x3a7: v3a772f = DELEGATECALL v3a772e, v71bV2683a7, v3a772b(0x0), v3a772a, v3a7727(0x0), v3a7727(0x0)
    0x7300x3a7: v3a7730 = RETURNDATASIZE 
    0x7310x3a7: v3a7731(0x0) = CONST 
    0x7340x3a7: RETURNDATACOPY v3a7731(0x0), v3a7731(0x0), v3a7730
    0x7360x3a7: v3a7736(0x0) = CONST 
    0x7390x3a7: v3a7739 = EQ v3a772f, v3a7736(0x0)
    0x73a0x3a7: v3a773a(0x742) = CONST 
    0x73d0x3a7: JUMPI v3a773a(0x742), v3a7739

    Begin block 0x73e0x3a7
    prev=[0x7210x3a7], succ=[]
    =================================
    0x73e0x3a7: v3a773e = RETURNDATASIZE 
    0x73f0x3a7: v3a773f(0x0) = CONST 
    0x7410x3a7: RETURN v3a773f(0x0), v3a773e

    Begin block 0x7420x3a7
    prev=[0x7210x3a7], succ=[]
    =================================
    0x7430x3a7: v3a7743 = RETURNDATASIZE 
    0x7440x3a7: v3a7744(0x0) = CONST 
    0x7460x3a7: REVERT v3a7744(0x0), v3a7743

}

function 0x5bd(0x5bdarg0x0) private {
    Begin block 0x5bd
    prev=[], succ=[0x747B0x5bd]
    =================================
    0x5be: v5be(0x0) = CONST 
    0x5c0: v5c0(0x5c7) = CONST 
    0x5c3: v5c3(0x747) = CONST 
    0x5c6: JUMP v5c3(0x747)

    Begin block 0x747B0x5bd
    prev=[0x5bd], succ=[0x5c7]
    =================================
    0x748S0x5bd: v748V5bd(0x0) = CONST 
    0x74bS0x5bd: v74bV5bd(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x5bd: v76cV5bd(0x1) = CONST 
    0x76eS0x5bd: v76eV5bd(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV5bd(0x1), v74bV5bd(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x5bd: v772V5bd = SLOAD v76eV5bd(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x5bd: JUMP v5c0(0x5c7)

    Begin block 0x5c7
    prev=[0x747B0x5bd], succ=[0x5fb, 0x609]
    =================================
    0x5c8: v5c8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5dd: v5dd = AND v5c8(0xffffffffffffffffffffffffffffffffffffffff), v772V5bd
    0x5de: v5de = CALLER 
    0x5df: v5df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5f4: v5f4 = AND v5df(0xffffffffffffffffffffffffffffffffffffffff), v5de
    0x5f5: v5f5 = EQ v5f4, v5dd
    0x5f6: v5f6 = ISZERO v5f5
    0x5f7: v5f7(0x609) = CONST 
    0x5fa: JUMPI v5f7(0x609), v5f6

    Begin block 0x5fb
    prev=[0x5c7], succ=[0x747B0x5fb]
    =================================
    0x5fb: v5fb(0x602) = CONST 
    0x5fe: v5fe(0x747) = CONST 
    0x601: JUMP v5fe(0x747)

    Begin block 0x747B0x5fb
    prev=[0x5fb], succ=[0x602]
    =================================
    0x748S0x5fb: v748V5fb(0x0) = CONST 
    0x74bS0x5fb: v74bV5fb(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x5fb: v76cV5fb(0x1) = CONST 
    0x76eS0x5fb: v76eV5fb(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV5fb(0x1), v74bV5fb(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x5fb: v772V5fb = SLOAD v76eV5fb(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x5fb: JUMP v5fb(0x602)

    Begin block 0x602
    prev=[0x747B0x5fb], succ=[0x612]
    =================================
    0x605: v605(0x612) = CONST 
    0x608: JUMP v605(0x612)

    Begin block 0x612
    prev=[0x602], succ=[]
    =================================
    0x614: RETURNPRIVATE v5bdarg0, v772V5fb

    Begin block 0x609
    prev=[0x5c7], succ=[0x2600x5bd]
    =================================
    0x60a: v60a(0x611) = CONST 
    0x60d: v60d(0x260) = CONST 
    0x610: JUMP v60d(0x260)

    Begin block 0x2600x5bd
    prev=[0x609], succ=[0x2680x5bd]
    =================================
    0x2610x5bd: v5bd261(0x268) = CONST 
    0x2640x5bd: v5bd264(0x615) = CONST 
    0x2670x5bd: CALLPRIVATE v5bd264(0x615), v5bd261(0x268)

    Begin block 0x2680x5bd
    prev=[0x2600x5bd], succ=[0x6f0B0x2680x5bd]
    =================================
    0x2690x5bd: v5bd269(0x278) = CONST 
    0x26c0x5bd: v5bd26c(0x273) = CONST 
    0x26f0x5bd: v5bd26f(0x6f0) = CONST 
    0x2720x5bd: JUMP v5bd26f(0x6f0)

    Begin block 0x6f0B0x2680x5bd
    prev=[0x2680x5bd], succ=[0x2730x5bd]
    =================================
    0x6f1S0x2680x5bd: v6f1V2685bd(0x0) = CONST 
    0x6f4S0x2680x5bd: v6f4V2685bd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680x5bd: v715V2685bd(0x1) = CONST 
    0x717S0x2680x5bd: v717V2685bd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V2685bd(0x1), v6f4V2685bd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680x5bd: v71bV2685bd = SLOAD v717V2685bd(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680x5bd: JUMP v5bd26c(0x273)

    Begin block 0x2730x5bd
    prev=[0x6f0B0x2680x5bd], succ=[0x7210x5bd]
    =================================
    0x2740x5bd: v5bd274(0x721) = CONST 
    0x2770x5bd: JUMP v5bd274(0x721)

    Begin block 0x7210x5bd
    prev=[0x2730x5bd], succ=[0x73e0x5bd, 0x7420x5bd]
    =================================
    0x7220x5bd: v5bd722 = CALLDATASIZE 
    0x7230x5bd: v5bd723(0x0) = CONST 
    0x7260x5bd: CALLDATACOPY v5bd723(0x0), v5bd723(0x0), v5bd722
    0x7270x5bd: v5bd727(0x0) = CONST 
    0x72a0x5bd: v5bd72a = CALLDATASIZE 
    0x72b0x5bd: v5bd72b(0x0) = CONST 
    0x72e0x5bd: v5bd72e = GAS 
    0x72f0x5bd: v5bd72f = DELEGATECALL v5bd72e, v71bV2685bd, v5bd72b(0x0), v5bd72a, v5bd727(0x0), v5bd727(0x0)
    0x7300x5bd: v5bd730 = RETURNDATASIZE 
    0x7310x5bd: v5bd731(0x0) = CONST 
    0x7340x5bd: RETURNDATACOPY v5bd731(0x0), v5bd731(0x0), v5bd730
    0x7360x5bd: v5bd736(0x0) = CONST 
    0x7390x5bd: v5bd739 = EQ v5bd72f, v5bd736(0x0)
    0x73a0x5bd: v5bd73a(0x742) = CONST 
    0x73d0x5bd: JUMPI v5bd73a(0x742), v5bd739

    Begin block 0x73e0x5bd
    prev=[0x7210x5bd], succ=[]
    =================================
    0x73e0x5bd: v5bd73e = RETURNDATASIZE 
    0x73f0x5bd: v5bd73f(0x0) = CONST 
    0x7410x5bd: RETURN v5bd73f(0x0), v5bd73e

    Begin block 0x7420x5bd
    prev=[0x7210x5bd], succ=[]
    =================================
    0x7430x5bd: v5bd743 = RETURNDATASIZE 
    0x7440x5bd: v5bd744(0x0) = CONST 
    0x7460x5bd: REVERT v5bd744(0x0), v5bd743

}

function 0x615(0x615arg0x0) private {
    Begin block 0x615
    prev=[], succ=[0x747B0x615]
    =================================
    0x616: v616(0x61d) = CONST 
    0x619: v619(0x747) = CONST 
    0x61c: JUMP v619(0x747)

    Begin block 0x747B0x615
    prev=[0x615], succ=[0x61d]
    =================================
    0x748S0x615: v748V615(0x0) = CONST 
    0x74bS0x615: v74bV615(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x615: v76cV615(0x1) = CONST 
    0x76eS0x615: v76eV615(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV615(0x1), v74bV615(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x615: v772V615 = SLOAD v76eV615(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x615: JUMP v616(0x61d)

    Begin block 0x61d
    prev=[0x747B0x615], succ=[0x653, 0x6e6]
    =================================
    0x61e: v61e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x633: v633 = AND v61e(0xffffffffffffffffffffffffffffffffffffffff), v772V615
    0x634: v634 = CALLER 
    0x635: v635(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x64a: v64a = AND v635(0xffffffffffffffffffffffffffffffffffffffff), v634
    0x64b: v64b = EQ v64a, v633
    0x64c: v64c = ISZERO v64b
    0x64d: v64d = ISZERO v64c
    0x64e: v64e = ISZERO v64d
    0x64f: v64f(0x6e6) = CONST 
    0x652: JUMPI v64f(0x6e6), v64e

    Begin block 0x653
    prev=[0x61d], succ=[]
    =================================
    0x653: v653(0x40) = CONST 
    0x655: v655 = MLOAD v653(0x40)
    0x656: v656(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x678: MSTORE v655, v656(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x679: v679(0x4) = CONST 
    0x67b: v67b = ADD v679(0x4), v655
    0x67e: v67e(0x20) = CONST 
    0x680: v680 = ADD v67e(0x20), v67b
    0x683: v683(0x20) = SUB v680, v67b
    0x685: MSTORE v67b, v683(0x20)
    0x686: v686(0x32) = CONST 
    0x689: MSTORE v680, v686(0x32)
    0x68a: v68a(0x20) = CONST 
    0x68c: v68c = ADD v68a(0x20), v680
    0x68e: v68e(0x43616e6e6f742063616c6c2066616c6c6261636b2066756e6374696f6e206672) = CONST 
    0x6b0: MSTORE v68c, v68e(0x43616e6e6f742063616c6c2066616c6c6261636b2066756e6374696f6e206672)
    0x6b1: v6b1(0x20) = CONST 
    0x6b3: v6b3 = ADD v6b1(0x20), v68c
    0x6b4: v6b4(0x6f6d207468652070726f78792061646d696e0000000000000000000000000000) = CONST 
    0x6d6: MSTORE v6b3, v6b4(0x6f6d207468652070726f78792061646d696e0000000000000000000000000000)
    0x6d8: v6d8(0x40) = CONST 
    0x6da: v6da = ADD v6d8(0x40), v68c
    0x6de: v6de(0x40) = CONST 
    0x6e0: v6e0 = MLOAD v6de(0x40)
    0x6e3: v6e3(0x84) = SUB v6da, v6e0
    0x6e5: REVERT v6e0, v6e3(0x84)

    Begin block 0x6e6
    prev=[0x61d], succ=[0x7f6B0x6e6]
    =================================
    0x6e7: v6e7(0x6ee) = CONST 
    0x6ea: v6ea(0x7f6) = CONST 
    0x6ed: JUMP v6ea(0x7f6), v6e7(0x6ee)

    Begin block 0x7f6B0x6e6
    prev=[0x6e6], succ=[0x6ee]
    =================================
    0x7f7S0x6e6: JUMP v6e7(0x6ee)

    Begin block 0x6ee
    prev=[0x7f6B0x6e6], succ=[]
    =================================
    0x6ef: RETURNPRIVATE v615arg0

}

function fallback()() public {
    Begin block 0x6d
    prev=[], succ=[0x2600x6d]
    =================================
    0x6e: v6e(0x75) = CONST 
    0x71: v71(0x260) = CONST 
    0x74: JUMP v71(0x260)

    Begin block 0x2600x6d
    prev=[0x6d], succ=[0x2680x6d]
    =================================
    0x2610x6d: v6d261(0x268) = CONST 
    0x2640x6d: v6d264(0x615) = CONST 
    0x2670x6d: CALLPRIVATE v6d264(0x615), v6d261(0x268)

    Begin block 0x2680x6d
    prev=[0x2600x6d], succ=[0x6f0B0x2680x6d]
    =================================
    0x2690x6d: v6d269(0x278) = CONST 
    0x26c0x6d: v6d26c(0x273) = CONST 
    0x26f0x6d: v6d26f(0x6f0) = CONST 
    0x2720x6d: JUMP v6d26f(0x6f0)

    Begin block 0x6f0B0x2680x6d
    prev=[0x2680x6d], succ=[0x2730x6d]
    =================================
    0x6f1S0x2680x6d: v6f1V2686d(0x0) = CONST 
    0x6f4S0x2680x6d: v6f4V2686d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680x6d: v715V2686d(0x1) = CONST 
    0x717S0x2680x6d: v717V2686d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V2686d(0x1), v6f4V2686d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680x6d: v71bV2686d = SLOAD v717V2686d(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680x6d: JUMP v6d26c(0x273)

    Begin block 0x2730x6d
    prev=[0x6f0B0x2680x6d], succ=[0x7210x6d]
    =================================
    0x2740x6d: v6d274(0x721) = CONST 
    0x2770x6d: JUMP v6d274(0x721)

    Begin block 0x7210x6d
    prev=[0x2730x6d], succ=[0x73e0x6d, 0x7420x6d]
    =================================
    0x7220x6d: v6d722 = CALLDATASIZE 
    0x7230x6d: v6d723(0x0) = CONST 
    0x7260x6d: CALLDATACOPY v6d723(0x0), v6d723(0x0), v6d722
    0x7270x6d: v6d727(0x0) = CONST 
    0x72a0x6d: v6d72a = CALLDATASIZE 
    0x72b0x6d: v6d72b(0x0) = CONST 
    0x72e0x6d: v6d72e = GAS 
    0x72f0x6d: v6d72f = DELEGATECALL v6d72e, v71bV2686d, v6d72b(0x0), v6d72a, v6d727(0x0), v6d727(0x0)
    0x7300x6d: v6d730 = RETURNDATASIZE 
    0x7310x6d: v6d731(0x0) = CONST 
    0x7340x6d: RETURNDATACOPY v6d731(0x0), v6d731(0x0), v6d730
    0x7360x6d: v6d736(0x0) = CONST 
    0x7390x6d: v6d739 = EQ v6d72f, v6d736(0x0)
    0x73a0x6d: v6d73a(0x742) = CONST 
    0x73d0x6d: JUMPI v6d73a(0x742), v6d739

    Begin block 0x73e0x6d
    prev=[0x7210x6d], succ=[]
    =================================
    0x73e0x6d: v6d73e = RETURNDATASIZE 
    0x73f0x6d: v6d73f(0x0) = CONST 
    0x7410x6d: RETURN v6d73f(0x0), v6d73e

    Begin block 0x7420x6d
    prev=[0x7210x6d], succ=[]
    =================================
    0x7430x6d: v6d743 = RETURNDATASIZE 
    0x7440x6d: v6d744(0x0) = CONST 
    0x7460x6d: REVERT v6d744(0x0), v6d743

}

function upgradeTo(address)() public {
    Begin block 0x77
    prev=[], succ=[0x7f, 0x83]
    =================================
    0x78: v78 = CALLVALUE 
    0x7a: v7a = ISZERO v78
    0x7b: v7b(0x83) = CONST 
    0x7e: JUMPI v7b(0x83), v7a

    Begin block 0x7f
    prev=[0x77], succ=[]
    =================================
    0x7f: v7f(0x0) = CONST 
    0x82: REVERT v7f(0x0), v7f(0x0)

    Begin block 0x83
    prev=[0x77], succ=[0x96, 0x9a]
    =================================
    0x85: v85(0xc6) = CONST 
    0x88: v88(0x4) = CONST 
    0x8b: v8b = CALLDATASIZE 
    0x8c: v8c = SUB v8b, v88(0x4)
    0x8d: v8d(0x20) = CONST 
    0x90: v90 = LT v8c, v8d(0x20)
    0x91: v91 = ISZERO v90
    0x92: v92(0x9a) = CONST 
    0x95: JUMPI v92(0x9a), v91

    Begin block 0x96
    prev=[0x83], succ=[]
    =================================
    0x96: v96(0x0) = CONST 
    0x99: REVERT v96(0x0), v96(0x0)

    Begin block 0x9a
    prev=[0x83], succ=[0x27a]
    =================================
    0x9c: v9c = ADD v88(0x4), v8c
    0xa0: va0 = CALLDATALOAD v88(0x4)
    0xa1: va1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb6: vb6 = AND va1(0xffffffffffffffffffffffffffffffffffffffff), va0
    0xb8: vb8(0x20) = CONST 
    0xba: vba(0x24) = ADD vb8(0x20), v88(0x4)
    0xc2: vc2(0x27a) = CONST 
    0xc5: JUMP vc2(0x27a)

    Begin block 0x27a
    prev=[0x9a], succ=[0x747B0x27a]
    =================================
    0x27b: v27b(0x282) = CONST 
    0x27e: v27e(0x747) = CONST 
    0x281: JUMP v27e(0x747)

    Begin block 0x747B0x27a
    prev=[0x27a], succ=[0x282]
    =================================
    0x748S0x27a: v748V27a(0x0) = CONST 
    0x74bS0x27a: v74bV27a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x27a: v76cV27a(0x1) = CONST 
    0x76eS0x27a: v76eV27a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV27a(0x1), v74bV27a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x27a: v772V27a = SLOAD v76eV27a(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x27a: JUMP v27b(0x282)

    Begin block 0x282
    prev=[0x747B0x27a], succ=[0x2b6, 0x2c3]
    =================================
    0x283: v283(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x298: v298 = AND v283(0xffffffffffffffffffffffffffffffffffffffff), v772V27a
    0x299: v299 = CALLER 
    0x29a: v29a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2af: v2af = AND v29a(0xffffffffffffffffffffffffffffffffffffffff), v299
    0x2b0: v2b0 = EQ v2af, v298
    0x2b1: v2b1 = ISZERO v2b0
    0x2b2: v2b2(0x2c3) = CONST 
    0x2b5: JUMPI v2b2(0x2c3), v2b1

    Begin block 0x2b6
    prev=[0x282], succ=[0x2be]
    =================================
    0x2b6: v2b6(0x2be) = CONST 
    0x2ba: v2ba(0x778) = CONST 
    0x2bd: CALLPRIVATE v2ba(0x778), vb6, v2b6(0x2be)

    Begin block 0x2be
    prev=[0x2b6], succ=[0x2cc]
    =================================
    0x2bf: v2bf(0x2cc) = CONST 
    0x2c2: JUMP v2bf(0x2cc)

    Begin block 0x2cc
    prev=[0x2be], succ=[0xc6]
    =================================
    0x2ce: JUMP v85(0xc6)

    Begin block 0xc6
    prev=[0x2cc], succ=[]
    =================================
    0xc7: STOP 

    Begin block 0x2c3
    prev=[0x282], succ=[0x2600x77]
    =================================
    0x2c4: v2c4(0x2cb) = CONST 
    0x2c7: v2c7(0x260) = CONST 
    0x2ca: JUMP v2c7(0x260)

    Begin block 0x2600x77
    prev=[0x2c3], succ=[0x2680x77]
    =================================
    0x2610x77: v77261(0x268) = CONST 
    0x2640x77: v77264(0x615) = CONST 
    0x2670x77: CALLPRIVATE v77264(0x615), v77261(0x268)

    Begin block 0x2680x77
    prev=[0x2600x77], succ=[0x6f0B0x2680x77]
    =================================
    0x2690x77: v77269(0x278) = CONST 
    0x26c0x77: v7726c(0x273) = CONST 
    0x26f0x77: v7726f(0x6f0) = CONST 
    0x2720x77: JUMP v7726f(0x6f0)

    Begin block 0x6f0B0x2680x77
    prev=[0x2680x77], succ=[0x2730x77]
    =================================
    0x6f1S0x2680x77: v6f1V26877(0x0) = CONST 
    0x6f4S0x2680x77: v6f4V26877(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680x77: v715V26877(0x1) = CONST 
    0x717S0x2680x77: v717V26877(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V26877(0x1), v6f4V26877(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680x77: v71bV26877 = SLOAD v717V26877(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680x77: JUMP v7726c(0x273)

    Begin block 0x2730x77
    prev=[0x6f0B0x2680x77], succ=[0x7210x77]
    =================================
    0x2740x77: v77274(0x721) = CONST 
    0x2770x77: JUMP v77274(0x721)

    Begin block 0x7210x77
    prev=[0x2730x77], succ=[0x73e0x77, 0x7420x77]
    =================================
    0x7220x77: v77722 = CALLDATASIZE 
    0x7230x77: v77723(0x0) = CONST 
    0x7260x77: CALLDATACOPY v77723(0x0), v77723(0x0), v77722
    0x7270x77: v77727(0x0) = CONST 
    0x72a0x77: v7772a = CALLDATASIZE 
    0x72b0x77: v7772b(0x0) = CONST 
    0x72e0x77: v7772e = GAS 
    0x72f0x77: v7772f = DELEGATECALL v7772e, v71bV26877, v7772b(0x0), v7772a, v77727(0x0), v77727(0x0)
    0x7300x77: v77730 = RETURNDATASIZE 
    0x7310x77: v77731(0x0) = CONST 
    0x7340x77: RETURNDATACOPY v77731(0x0), v77731(0x0), v77730
    0x7360x77: v77736(0x0) = CONST 
    0x7390x77: v77739 = EQ v7772f, v77736(0x0)
    0x73a0x77: v7773a(0x742) = CONST 
    0x73d0x77: JUMPI v7773a(0x742), v77739

    Begin block 0x73e0x77
    prev=[0x7210x77], succ=[]
    =================================
    0x73e0x77: v7773e = RETURNDATASIZE 
    0x73f0x77: v7773f(0x0) = CONST 
    0x7410x77: RETURN v7773f(0x0), v7773e

    Begin block 0x7420x77
    prev=[0x7210x77], succ=[]
    =================================
    0x7430x77: v77743 = RETURNDATASIZE 
    0x7440x77: v77744(0x0) = CONST 
    0x7460x77: REVERT v77744(0x0), v77743

}

function 0x778(0x778arg0x0, 0x778arg0x1) private {
    Begin block 0x778
    prev=[], succ=[0x7f8]
    =================================
    0x779: v779(0x781) = CONST 
    0x77d: v77d(0x7f8) = CONST 
    0x780: JUMP v77d(0x7f8)

    Begin block 0x7f8
    prev=[0x778], succ=[0x8ca]
    =================================
    0x7f9: v7f9(0x801) = CONST 
    0x7fd: v7fd(0x8ca) = CONST 
    0x800: JUMP v7fd(0x8ca)

    Begin block 0x8ca
    prev=[0x7f8], succ=[0x801]
    =================================
    0x8cb: v8cb(0x0) = CONST 
    0x8cf: v8cf = EXTCODESIZE v778arg0
    0x8d2: v8d2(0x0) = CONST 
    0x8d5: v8d5 = GT v8cf, v8d2(0x0)
    0x8dc: JUMP v7f9(0x801)

    Begin block 0x801
    prev=[0x8ca], succ=[0x808, 0x89b]
    =================================
    0x802: v802 = ISZERO v8d5
    0x803: v803 = ISZERO v802
    0x804: v804(0x89b) = CONST 
    0x807: JUMPI v804(0x89b), v803

    Begin block 0x808
    prev=[0x801], succ=[]
    =================================
    0x808: v808(0x40) = CONST 
    0x80a: v80a = MLOAD v808(0x40)
    0x80b: v80b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x82d: MSTORE v80a, v80b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x82e: v82e(0x4) = CONST 
    0x830: v830 = ADD v82e(0x4), v80a
    0x833: v833(0x20) = CONST 
    0x835: v835 = ADD v833(0x20), v830
    0x838: v838(0x20) = SUB v835, v830
    0x83a: MSTORE v830, v838(0x20)
    0x83b: v83b(0x3b) = CONST 
    0x83e: MSTORE v835, v83b(0x3b)
    0x83f: v83f(0x20) = CONST 
    0x841: v841 = ADD v83f(0x20), v835
    0x843: v843(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f) = CONST 
    0x865: MSTORE v841, v843(0x43616e6e6f742073657420612070726f787920696d706c656d656e746174696f)
    0x866: v866(0x20) = CONST 
    0x868: v868 = ADD v866(0x20), v841
    0x869: v869(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000) = CONST 
    0x88b: MSTORE v868, v869(0x6e20746f2061206e6f6e2d636f6e747261637420616464726573730000000000)
    0x88d: v88d(0x40) = CONST 
    0x88f: v88f = ADD v88d(0x40), v841
    0x893: v893(0x40) = CONST 
    0x895: v895 = MLOAD v893(0x40)
    0x898: v898(0x84) = SUB v88f, v895
    0x89a: REVERT v895, v898(0x84)

    Begin block 0x89b
    prev=[0x801], succ=[0x781]
    =================================
    0x89c: v89c(0x0) = CONST 
    0x89e: v89e(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x8bf: v8bf(0x1) = CONST 
    0x8c1: v8c1(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v8bf(0x1), v89e(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x8c6: SSTORE v8c1(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v778arg0
    0x8c9: JUMP v779(0x781)

    Begin block 0x781
    prev=[0x89b], succ=[]
    =================================
    0x783: v783(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x798: v798 = AND v783(0xffffffffffffffffffffffffffffffffffffffff), v778arg0
    0x799: v799(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x7ba: v7ba(0x40) = CONST 
    0x7bc: v7bc = MLOAD v7ba(0x40)
    0x7bd: v7bd(0x40) = CONST 
    0x7bf: v7bf = MLOAD v7bd(0x40)
    0x7c2: v7c2(0x0) = SUB v7bc, v7bf
    0x7c4: LOG2 v7bf, v7c2(0x0), v799(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v798
    0x7c6: RETURNPRIVATE v778arg1

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xc8
    prev=[], succ=[0xda, 0xde]
    =================================
    0xc9: vc9(0x15f) = CONST 
    0xcc: vcc(0x4) = CONST 
    0xcf: vcf = CALLDATASIZE 
    0xd0: vd0 = SUB vcf, vcc(0x4)
    0xd1: vd1(0x40) = CONST 
    0xd4: vd4 = LT vd0, vd1(0x40)
    0xd5: vd5 = ISZERO vd4
    0xd6: vd6(0xde) = CONST 
    0xd9: JUMPI vd6(0xde), vd5

    Begin block 0xda
    prev=[0xc8], succ=[]
    =================================
    0xda: vda(0x0) = CONST 
    0xdd: REVERT vda(0x0), vda(0x0)

    Begin block 0xde
    prev=[0xc8], succ=[0x117, 0x11b]
    =================================
    0xe0: ve0 = ADD vcc(0x4), vd0
    0xe4: ve4 = CALLDATALOAD vcc(0x4)
    0xe5: ve5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfa: vfa = AND ve5(0xffffffffffffffffffffffffffffffffffffffff), ve4
    0xfc: vfc(0x20) = CONST 
    0xfe: vfe(0x24) = ADD vfc(0x20), vcc(0x4)
    0x104: v104 = CALLDATALOAD vfe(0x24)
    0x106: v106(0x20) = CONST 
    0x108: v108(0x44) = ADD v106(0x20), vfe(0x24)
    0x10a: v10a(0x100000000) = CONST 
    0x111: v111 = GT v104, v10a(0x100000000)
    0x112: v112 = ISZERO v111
    0x113: v113(0x11b) = CONST 
    0x116: JUMPI v113(0x11b), v112

    Begin block 0x117
    prev=[0xde], succ=[]
    =================================
    0x117: v117(0x0) = CONST 
    0x11a: REVERT v117(0x0), v117(0x0)

    Begin block 0x11b
    prev=[0xde], succ=[0x129, 0x12d]
    =================================
    0x11d: v11d = ADD vcc(0x4), v104
    0x11f: v11f(0x20) = CONST 
    0x122: v122 = ADD v11d, v11f(0x20)
    0x123: v123 = GT v122, ve0
    0x124: v124 = ISZERO v123
    0x125: v125(0x12d) = CONST 
    0x128: JUMPI v125(0x12d), v124

    Begin block 0x129
    prev=[0x11b], succ=[]
    =================================
    0x129: v129(0x0) = CONST 
    0x12c: REVERT v129(0x0), v129(0x0)

    Begin block 0x12d
    prev=[0x11b], succ=[0x14b, 0x14f]
    =================================
    0x12f: v12f = CALLDATALOAD v11d
    0x131: v131(0x20) = CONST 
    0x133: v133 = ADD v131(0x20), v11d
    0x136: v136(0x1) = CONST 
    0x139: v139 = MUL v12f, v136(0x1)
    0x13b: v13b = ADD v133, v139
    0x13c: v13c = GT v13b, ve0
    0x13d: v13d(0x100000000) = CONST 
    0x144: v144 = GT v12f, v13d(0x100000000)
    0x145: v145 = OR v144, v13c
    0x146: v146 = ISZERO v145
    0x147: v147(0x14f) = CONST 
    0x14a: JUMPI v147(0x14f), v146

    Begin block 0x14b
    prev=[0x12d], succ=[]
    =================================
    0x14b: v14b(0x0) = CONST 
    0x14e: REVERT v14b(0x0), v14b(0x0)

    Begin block 0x14f
    prev=[0x12d], succ=[0x2cf]
    =================================
    0x15b: v15b(0x2cf) = CONST 
    0x15e: JUMP v15b(0x2cf)

    Begin block 0x2cf
    prev=[0x14f], succ=[0x747B0x2cf]
    =================================
    0x2d0: v2d0(0x2d7) = CONST 
    0x2d3: v2d3(0x747) = CONST 
    0x2d6: JUMP v2d3(0x747)

    Begin block 0x747B0x2cf
    prev=[0x2cf], succ=[0x2d7]
    =================================
    0x748S0x2cf: v748V2cf(0x0) = CONST 
    0x74bS0x2cf: v74bV2cf(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x76cS0x2cf: v76cV2cf(0x1) = CONST 
    0x76eS0x2cf: v76eV2cf(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = MUL v76cV2cf(0x1), v74bV2cf(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x772S0x2cf: v772V2cf = SLOAD v76eV2cf(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x777S0x2cf: JUMP v2d0(0x2d7)

    Begin block 0x2d7
    prev=[0x747B0x2cf], succ=[0x30b, 0x399]
    =================================
    0x2d8: v2d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ed: v2ed = AND v2d8(0xffffffffffffffffffffffffffffffffffffffff), v772V2cf
    0x2ee: v2ee = CALLER 
    0x2ef: v2ef(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x304: v304 = AND v2ef(0xffffffffffffffffffffffffffffffffffffffff), v2ee
    0x305: v305 = EQ v304, v2ed
    0x306: v306 = ISZERO v305
    0x307: v307(0x399) = CONST 
    0x30a: JUMPI v307(0x399), v306

    Begin block 0x30b
    prev=[0x2d7], succ=[0x313]
    =================================
    0x30b: v30b(0x313) = CONST 
    0x30f: v30f(0x778) = CONST 
    0x312: CALLPRIVATE v30f(0x778), vfa, v30b(0x313)

    Begin block 0x313
    prev=[0x30b], succ=[0x35d, 0x37e]
    =================================
    0x314: v314(0x0) = CONST 
    0x317: v317(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x32c: v32c = AND v317(0xffffffffffffffffffffffffffffffffffffffff), vfa
    0x32f: v32f(0x40) = CONST 
    0x331: v331 = MLOAD v32f(0x40)
    0x338: CALLDATACOPY v331, v133, v12f
    0x33b: v33b = ADD v331, v12f
    0x344: v344(0x0) = CONST 
    0x346: v346(0x40) = CONST 
    0x348: v348 = MLOAD v346(0x40)
    0x34b: v34b = SUB v33b, v348
    0x34e: v34e = GAS 
    0x34f: v34f = DELEGATECALL v34e, v32c, v348, v34b, v348, v344(0x0)
    0x353: v353 = RETURNDATASIZE 
    0x355: v355(0x0) = CONST 
    0x358: v358 = EQ v353, v355(0x0)
    0x359: v359(0x37e) = CONST 
    0x35c: JUMPI v359(0x37e), v358

    Begin block 0x35d
    prev=[0x313], succ=[0x383]
    =================================
    0x35d: v35d(0x40) = CONST 
    0x35f: v35f = MLOAD v35d(0x40)
    0x362: v362(0x1f) = CONST 
    0x364: v364(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v362(0x1f)
    0x365: v365(0x3f) = CONST 
    0x367: v367 = RETURNDATASIZE 
    0x368: v368 = ADD v367, v365(0x3f)
    0x369: v369 = AND v368, v364(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x36b: v36b = ADD v35f, v369
    0x36c: v36c(0x40) = CONST 
    0x36e: MSTORE v36c(0x40), v36b
    0x36f: v36f = RETURNDATASIZE 
    0x371: MSTORE v35f, v36f
    0x372: v372 = RETURNDATASIZE 
    0x373: v373(0x0) = CONST 
    0x375: v375(0x20) = CONST 
    0x378: v378 = ADD v35f, v375(0x20)
    0x379: RETURNDATACOPY v378, v373(0x0), v372
    0x37a: v37a(0x383) = CONST 
    0x37d: JUMP v37a(0x383)

    Begin block 0x383
    prev=[0x35d, 0x37e], succ=[0x38f, 0x393]
    =================================
    0x389: v389 = ISZERO v34f
    0x38a: v38a = ISZERO v389
    0x38b: v38b(0x393) = CONST 
    0x38e: JUMPI v38b(0x393), v38a

    Begin block 0x38f
    prev=[0x383], succ=[]
    =================================
    0x38f: v38f(0x0) = CONST 
    0x392: REVERT v38f(0x0), v38f(0x0)

    Begin block 0x393
    prev=[0x383], succ=[0x3a2]
    =================================
    0x395: v395(0x3a2) = CONST 
    0x398: JUMP v395(0x3a2)

    Begin block 0x3a2
    prev=[0x393], succ=[0x15f]
    =================================
    0x3a6: JUMP vc9(0x15f)

    Begin block 0x15f
    prev=[0x3a2], succ=[]
    =================================
    0x160: STOP 

    Begin block 0x37e
    prev=[0x313], succ=[0x383]
    =================================
    0x37f: v37f(0x60) = CONST 

    Begin block 0x399
    prev=[0x2d7], succ=[0x2600xc8]
    =================================
    0x39a: v39a(0x3a1) = CONST 
    0x39d: v39d(0x260) = CONST 
    0x3a0: JUMP v39d(0x260)

    Begin block 0x2600xc8
    prev=[0x399], succ=[0x2680xc8]
    =================================
    0x2610xc8: vc8261(0x268) = CONST 
    0x2640xc8: vc8264(0x615) = CONST 
    0x2670xc8: CALLPRIVATE vc8264(0x615), vc8261(0x268)

    Begin block 0x2680xc8
    prev=[0x2600xc8], succ=[0x6f0B0x2680xc8]
    =================================
    0x2690xc8: vc8269(0x278) = CONST 
    0x26c0xc8: vc826c(0x273) = CONST 
    0x26f0xc8: vc826f(0x6f0) = CONST 
    0x2720xc8: JUMP vc826f(0x6f0)

    Begin block 0x6f0B0x2680xc8
    prev=[0x2680xc8], succ=[0x2730xc8]
    =================================
    0x6f1S0x2680xc8: v6f1V268c8(0x0) = CONST 
    0x6f4S0x2680xc8: v6f4V268c8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x715S0x2680xc8: v715V268c8(0x1) = CONST 
    0x717S0x2680xc8: v717V268c8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = MUL v715V268c8(0x1), v6f4V268c8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x71bS0x2680xc8: v71bV268c8 = SLOAD v717V268c8(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x720S0x2680xc8: JUMP vc826c(0x273)

    Begin block 0x2730xc8
    prev=[0x6f0B0x2680xc8], succ=[0x7210xc8]
    =================================
    0x2740xc8: vc8274(0x721) = CONST 
    0x2770xc8: JUMP vc8274(0x721)

    Begin block 0x7210xc8
    prev=[0x2730xc8], succ=[0x73e0xc8, 0x7420xc8]
    =================================
    0x7220xc8: vc8722 = CALLDATASIZE 
    0x7230xc8: vc8723(0x0) = CONST 
    0x7260xc8: CALLDATACOPY vc8723(0x0), vc8723(0x0), vc8722
    0x7270xc8: vc8727(0x0) = CONST 
    0x72a0xc8: vc872a = CALLDATASIZE 
    0x72b0xc8: vc872b(0x0) = CONST 
    0x72e0xc8: vc872e = GAS 
    0x72f0xc8: vc872f = DELEGATECALL vc872e, v71bV268c8, vc872b(0x0), vc872a, vc8727(0x0), vc8727(0x0)
    0x7300xc8: vc8730 = RETURNDATASIZE 
    0x7310xc8: vc8731(0x0) = CONST 
    0x7340xc8: RETURNDATACOPY vc8731(0x0), vc8731(0x0), vc8730
    0x7360xc8: vc8736(0x0) = CONST 
    0x7390xc8: vc8739 = EQ vc872f, vc8736(0x0)
    0x73a0xc8: vc873a(0x742) = CONST 
    0x73d0xc8: JUMPI vc873a(0x742), vc8739

    Begin block 0x73e0xc8
    prev=[0x7210xc8], succ=[]
    =================================
    0x73e0xc8: vc873e = RETURNDATASIZE 
    0x73f0xc8: vc873f(0x0) = CONST 
    0x7410xc8: RETURN vc873f(0x0), vc873e

    Begin block 0x7420xc8
    prev=[0x7210xc8], succ=[]
    =================================
    0x7430xc8: vc8743 = RETURNDATASIZE 
    0x7440xc8: vc8744(0x0) = CONST 
    0x7460xc8: REVERT vc8744(0x0), vc8743

}

