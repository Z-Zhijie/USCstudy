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
    prev=[0x0], succ=[0x2f, 0x33]
    =================================
    0x12: v12(0x40) = CONST 
    0x14: v14 = MLOAD v12(0x40)
    0x15: v15(0x8f4) = CONST 
    0x18: v18 = CODESIZE 
    0x19: v19 = SUB v18, v15(0x8f4)
    0x1b: v1b(0x8f4) = CONST 
    0x1f: CODECOPY v14, v1b(0x8f4), v19
    0x22: v22 = ADD v19, v14
    0x23: v23(0x40) = CONST 
    0x25: MSTORE v23(0x40), v22
    0x26: v26(0x40) = CONST 
    0x29: v29 = LT v19, v26(0x40)
    0x2a: v2a = ISZERO v29
    0x2b: v2b(0x33) = CONST 
    0x2e: JUMPI v2b(0x33), v2a

    Begin block 0x2f
    prev=[0x10], succ=[]
    =================================
    0x2f: v2f(0x0) = CONST 
    0x32: REVERT v2f(0x0), v2f(0x0)

    Begin block 0x33
    prev=[0x10], succ=[0xa0, 0xa1]
    =================================
    0x36: v36 = MLOAD v14
    0x37: v37(0x20) = CONST 
    0x3b: v3b = ADD v37(0x20), v14
    0x3c: v3c = MLOAD v3b
    0x3d: v3d(0x40) = CONST 
    0x40: v40 = MLOAD v3d(0x40)
    0x43: v43 = ADD v40, v37(0x20)
    0x45: MSTORE v3d(0x40), v43
    0x46: v46(0x0) = CONST 
    0x49: MSTORE v40, v46(0x0)
    0x4b: v4b = MLOAD v3d(0x40)
    0x4c: v4c(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000) = CONST 
    0x6e: MSTORE v4b, v4c(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000)
    0x70: v70 = MLOAD v3d(0x40)
    0x74: v74(0x0) = SUB v4b, v70
    0x75: v75(0x1c) = CONST 
    0x77: v77(0x1c) = ADD v75(0x1c), v74(0x0)
    0x79: v79 = SHA3 v70, v77(0x1c)
    0x86: v86(0x0) = CONST 
    0x89: v89 = MLOAD v86(0x0)
    0x8a: v8a(0x20) = CONST 
    0x8c: v8c(0x899) = CONST 
    0x94: MSTORE v86(0x0), v89
    0x95: v95(0x0) = CONST 
    0x97: v97(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v95(0x0)
    0x9a: v9a = ADD v79, v97(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x9b: v9b = EQ v9a, v936(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x9c: v9c(0xa1) = CONST 
    0x9f: JUMPI v9c(0xa1), v9b
    0x936: v936(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 

    Begin block 0xa0
    prev=[0x33], succ=[]
    =================================
    0xa0: THROW 

    Begin block 0xa1
    prev=[0x33], succ=[0x1d7]
    =================================
    0xa2: va2(0xb3) = CONST 
    0xa6: va6(0x1) = CONST 
    0xa8: va8(0x1) = CONST 
    0xaa: vaa(0xe0) = CONST 
    0xac: vac(0x100000000000000000000000000000000000000000000000000000000) = SHL vaa(0xe0), va8(0x1)
    0xad: vad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB vac(0x100000000000000000000000000000000000000000000000000000000), va6(0x1)
    0xae: vae(0x1d7) = CONST 
    0xb1: vb1(0x1d7) = AND vae(0x1d7), vad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xb2: JUMP vb1(0x1d7)

    Begin block 0x1d7
    prev=[0xa1], succ=[0x249]
    =================================
    0x1d8: v1d8(0x1ea) = CONST 
    0x1dc: v1dc(0x249) = CONST 
    0x1df: v1df(0x20) = CONST 
    0x1e1: v1e1(0x24900000000) = SHL v1df(0x20), v1dc(0x249)
    0x1e2: v1e2(0x53d) = CONST 
    0x1e5: v1e5(0x2490000053d) = OR v1e2(0x53d), v1e1(0x24900000000)
    0x1e6: v1e6(0x20) = CONST 
    0x1e8: v1e8(0x249) = SHR v1e6(0x20), v1e5(0x2490000053d)
    0x1e9: JUMP v1e8(0x249)

    Begin block 0x249
    prev=[0x1d7], succ=[0x1ea]
    =================================
    0x24a: v24a = EXTCODESIZE v36
    0x24b: v24b = ISZERO v24a
    0x24c: v24c = ISZERO v24b
    0x24e: JUMP v1d8(0x1ea)

    Begin block 0x1ea
    prev=[0x249], succ=[0x1ef, 0x225]
    =================================
    0x1eb: v1eb(0x225) = CONST 
    0x1ee: JUMPI v1eb(0x225), v24c

    Begin block 0x1ef
    prev=[0x1ea], succ=[]
    =================================
    0x1ef: v1ef(0x40) = CONST 
    0x1f1: v1f1 = MLOAD v1ef(0x40)
    0x1f2: v1f2(0x461bcd) = CONST 
    0x1f6: v1f6(0xe5) = CONST 
    0x1f8: v1f8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1f6(0xe5), v1f2(0x461bcd)
    0x1fa: MSTORE v1f1, v1f8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1fb: v1fb(0x4) = CONST 
    0x1fd: v1fd = ADD v1fb(0x4), v1f1
    0x200: v200(0x20) = CONST 
    0x202: v202 = ADD v200(0x20), v1fd
    0x205: v205(0x20) = SUB v202, v1fd
    0x207: MSTORE v1fd, v205(0x20)
    0x208: v208(0x3b) = CONST 
    0x20b: MSTORE v202, v208(0x3b)
    0x20c: v20c(0x20) = CONST 
    0x20e: v20e = ADD v20c(0x20), v202
    0x210: v210(0x8b9) = CONST 
    0x213: v213(0x3b) = CONST 
    0x216: CODECOPY v20e, v210(0x8b9), v213(0x3b)
    0x217: v217(0x40) = CONST 
    0x219: v219 = ADD v217(0x40), v20e
    0x21d: v21d(0x40) = CONST 
    0x21f: v21f = MLOAD v21d(0x40)
    0x222: v222(0x84) = SUB v219, v21f
    0x224: REVERT v21f, v222(0x84)

    Begin block 0x225
    prev=[0x1ea], succ=[0xb3]
    =================================
    0x226: v226(0x0) = CONST 
    0x229: v229 = MLOAD v226(0x0)
    0x22a: v22a(0x20) = CONST 
    0x22c: v22c(0x899) = CONST 
    0x234: MSTORE v226(0x0), v229
    0x235: SSTORE v943(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v36
    0x236: JUMP va2(0xb3)
    0x943: v943(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 

    Begin block 0xb3
    prev=[0x225], succ=[0xbb]
    =================================
    0xb5: vb5(0x0) = MLOAD v40
    0xb6: vb6 = ISZERO vb5(0x0)
    0xb7: vb7(0x16b) = CONST 
    0xba: JUMPI vb7(0x16b), vb6

    Begin block 0xbb
    prev=[0xb3], succ=[0xd7]
    =================================
    0xbb: vbb(0x0) = CONST 
    0xbe: vbe(0x1) = CONST 
    0xc0: vc0(0x1) = CONST 
    0xc2: vc2(0xa0) = CONST 
    0xc4: vc4(0x10000000000000000000000000000000000000000) = SHL vc2(0xa0), vc0(0x1)
    0xc5: vc5(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc4(0x10000000000000000000000000000000000000000), vbe(0x1)
    0xc6: vc6 = AND vc5(0xffffffffffffffffffffffffffffffffffffffff), v36
    0xc8: vc8(0x40) = CONST 
    0xca: vca = MLOAD vc8(0x40)
    0xce: vce(0x0) = MLOAD v40
    0xd0: vd0(0x20) = CONST 
    0xd2: vd2 = ADD vd0(0x20), v40

    Begin block 0xd7
    prev=[0xbb, 0xe0], succ=[0xe0, 0xf6]
    =================================
    0xd7_0x2: vd7_2 = PHI vce(0x0), ve9
    0xd8: vd8(0x20) = CONST 
    0xdb: vdb = LT vd7_2, vd8(0x20)
    0xdc: vdc(0xf6) = CONST 
    0xdf: JUMPI vdc(0xf6), vdb

    Begin block 0xe0
    prev=[0xd7], succ=[0xd7]
    =================================
    0xe0_0x0: ve0_0 = PHI vd2, vf1
    0xe0_0x1: ve0_1 = PHI vca, vef
    0xe0_0x2: ve0_2 = PHI vce(0x0), ve9
    0xe1: ve1 = MLOAD ve0_0
    0xe3: MSTORE ve0_1, ve1
    0xe4: ve4(0x1f) = CONST 
    0xe6: ve6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT ve4(0x1f)
    0xe9: ve9 = ADD ve0_2, ve6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0xeb: veb(0x20) = CONST 
    0xef: vef = ADD veb(0x20), ve0_1
    0xf1: vf1 = ADD veb(0x20), ve0_0
    0xf2: vf2(0xd7) = CONST 
    0xf5: JUMP vf2(0xd7)

    Begin block 0xf6
    prev=[0xd7], succ=[0x135, 0x156]
    =================================
    0xf6_0x0: vf6_0 = PHI vd2, vf1
    0xf6_0x1: vf6_1 = PHI vca, vef
    0xf6_0x2: vf6_2 = PHI vce(0x0), ve9
    0xf7: vf7(0x1) = CONST 
    0xfa: vfa(0x20) = CONST 
    0xfc: vfc = SUB vfa(0x20), vf6_2
    0xfd: vfd(0x100) = CONST 
    0x100: v100 = EXP vfd(0x100), vfc
    0x101: v101 = SUB v100, vf7(0x1)
    0x103: v103 = NOT v101
    0x105: v105 = MLOAD vf6_0
    0x106: v106 = AND v105, v103
    0x109: v109 = MLOAD vf6_1
    0x10a: v10a = AND v109, v101
    0x10d: v10d = OR v106, v10a
    0x10f: MSTORE vf6_1, v10d
    0x118: v118 = ADD vce(0x0), vca
    0x11c: v11c(0x0) = CONST 
    0x11e: v11e(0x40) = CONST 
    0x120: v120 = MLOAD v11e(0x40)
    0x123: v123(0x0) = SUB v118, v120
    0x126: v126 = GAS 
    0x127: v127 = DELEGATECALL v126, vc6, v120, v123(0x0), v120, v11c(0x0)
    0x12b: v12b = RETURNDATASIZE 
    0x12d: v12d(0x0) = CONST 
    0x130: v130 = EQ v12b, v12d(0x0)
    0x131: v131(0x156) = CONST 
    0x134: JUMPI v131(0x156), v130

    Begin block 0x135
    prev=[0xf6], succ=[0x15b]
    =================================
    0x135: v135(0x40) = CONST 
    0x137: v137 = MLOAD v135(0x40)
    0x13a: v13a(0x1f) = CONST 
    0x13c: v13c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v13a(0x1f)
    0x13d: v13d(0x3f) = CONST 
    0x13f: v13f = RETURNDATASIZE 
    0x140: v140 = ADD v13f, v13d(0x3f)
    0x141: v141 = AND v140, v13c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x143: v143 = ADD v137, v141
    0x144: v144(0x40) = CONST 
    0x146: MSTORE v144(0x40), v143
    0x147: v147 = RETURNDATASIZE 
    0x149: MSTORE v137, v147
    0x14a: v14a = RETURNDATASIZE 
    0x14b: v14b(0x0) = CONST 
    0x14d: v14d(0x20) = CONST 
    0x150: v150 = ADD v137, v14d(0x20)
    0x151: RETURNDATACOPY v150, v14b(0x0), v14a
    0x152: v152(0x15b) = CONST 
    0x155: JUMP v152(0x15b)

    Begin block 0x15b
    prev=[0x135, 0x156], succ=[0x165, 0x169]
    =================================
    0x161: v161(0x169) = CONST 
    0x164: JUMPI v161(0x169), v127

    Begin block 0x165
    prev=[0x15b], succ=[]
    =================================
    0x165: v165(0x0) = CONST 
    0x168: REVERT v165(0x0), v165(0x0)

    Begin block 0x169
    prev=[0x15b], succ=[0x937]
    =================================

    Begin block 0x937
    prev=[0x169], succ=[]
    =================================
    0x938: v938(0x16b) = CONST 
    0x939: CALLPRIVATE v938(0x16b), v40, v36, v40, v3c, v36, v3c, v36

    Begin block 0x156
    prev=[0xf6], succ=[0x15b]
    =================================
    0x157: v157(0x60) = CONST 

}

function admin()(0x16barg0x0, 0x16barg0x1, 0x16barg0x2, 0x16barg0x3, 0x16barg0x4, 0x16barg0x5, 0x16barg0x6) public {
    Begin block 0x16b
    prev=[], succ=[0x1ba, 0x1bb]
    =================================
    0x16e: v16e(0x40) = CONST 
    0x171: v171 = MLOAD v16e(0x40)
    0x172: v172(0x656970313936372e70726f78792e61646d696e00000000000000000000000000) = CONST 
    0x194: MSTORE v171, v172(0x656970313936372e70726f78792e61646d696e00000000000000000000000000)
    0x196: v196 = MLOAD v16e(0x40)
    0x19a: v19a(0x0) = SUB v171, v196
    0x19b: v19b(0x13) = CONST 
    0x19d: v19d(0x13) = ADD v19b(0x13), v19a(0x0)
    0x19f: v19f = SHA3 v196, v19d(0x13)
    0x1a0: v1a0(0x0) = CONST 
    0x1a3: v1a3 = MLOAD v1a0(0x0)
    0x1a4: v1a4(0x20) = CONST 
    0x1a6: v1a6(0x879) = CONST 
    0x1ae: MSTORE v1a0(0x0), v1a3
    0x1af: v1af(0x0) = CONST 
    0x1b1: v1b1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1af(0x0)
    0x1b4: v1b4 = ADD v19f, v1b1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1b5: v1b5 = EQ v1b4, v93e(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103)
    0x1b6: v1b6(0x1bb) = CONST 
    0x1b9: JUMPI v1b6(0x1bb), v1b5
    0x93e: v93e(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 

    Begin block 0x1ba
    prev=[0x16b], succ=[]
    =================================
    0x1ba: THROW 

    Begin block 0x1bb
    prev=[0x16b], succ=[0x237]
    =================================
    0x1bc: v1bc(0x1cd) = CONST 
    0x1c0: v1c0(0x1) = CONST 
    0x1c2: v1c2(0x1) = CONST 
    0x1c4: v1c4(0xe0) = CONST 
    0x1c6: v1c6(0x100000000000000000000000000000000000000000000000000000000) = SHL v1c4(0xe0), v1c2(0x1)
    0x1c7: v1c7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1c6(0x100000000000000000000000000000000000000000000000000000000), v1c0(0x1)
    0x1c8: v1c8(0x237) = CONST 
    0x1cb: v1cb(0x237) = AND v1c8(0x237), v1c7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1cc: JUMP v1cb(0x237)

    Begin block 0x237
    prev=[0x1bb], succ=[0x1cd]
    =================================
    0x238: v238(0x0) = CONST 
    0x23b: v23b = MLOAD v238(0x0)
    0x23c: v23c(0x20) = CONST 
    0x23e: v23e(0x879) = CONST 
    0x246: MSTORE v238(0x0), v23b
    0x247: SSTORE v948(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v16barg3
    0x248: JUMP v1bc(0x1cd)
    0x948: v948(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 

    Begin block 0x1cd
    prev=[0x237], succ=[0x24f]
    =================================
    0x1d3: v1d3(0x24f) = CONST 
    0x1d6: JUMP v1d3(0x24f)

    Begin block 0x24f
    prev=[0x1cd], succ=[]
    =================================
    0x250: v250(0x61b) = CONST 
    0x254: v254(0x25e) = CONST 
    0x257: v257(0x0) = CONST 
    0x259: CODECOPY v257(0x0), v254(0x25e), v250(0x61b)
    0x25a: v25a(0x0) = CONST 
    0x25c: RETURN v25a(0x0), v250(0x61b)

}

