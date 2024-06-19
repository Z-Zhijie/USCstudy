function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x38, 0x3c]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x21e19e0c9bab2400000) = CONST 
    0x10: v10(0xd) = CONST 
    0x12: SSTORE v10(0xd), v5(0x21e19e0c9bab2400000)
    0x13: v13(0x69780) = CONST 
    0x17: v17(0xe) = CONST 
    0x19: SSTORE v17(0xe), v13(0x69780)
    0x1a: v1a(0x93a80) = CONST 
    0x1e: v1e(0xf) = CONST 
    0x20: SSTORE v1e(0xf), v1a(0x93a80)
    0x21: v21(0x5) = CONST 
    0x23: v23(0x10) = CONST 
    0x25: SSTORE v23(0x10), v21(0x5)
    0x26: v26(0x5) = CONST 
    0x28: v28(0x11) = CONST 
    0x2a: SSTORE v28(0x11), v26(0x5)
    0x2b: v2b(0x14) = CONST 
    0x2d: v2d(0x12) = CONST 
    0x2f: SSTORE v2d(0x12), v2b(0x14)
    0x30: v30 = CALLVALUE 
    0x32: v32 = ISZERO v30
    0x33: v33(0x3c) = CONST 
    0x37: JUMPI v33(0x3c), v32

    Begin block 0x38
    prev=[0x0], succ=[]
    =================================
    0x38: v38(0x0) = CONST 
    0x3b: REVERT v38(0x0), v38(0x0)

    Begin block 0x3c
    prev=[0x0], succ=[0x4f]
    =================================
    0x3e: v3e(0x4f) = CONST 
    0x42: v42(0x1ffc9a7) = CONST 
    0x47: v47(0xe0) = CONST 
    0x49: v49(0x1ffc9a700000000000000000000000000000000000000000000000000000000) = SHL v47(0xe0), v42(0x1ffc9a7)
    0x4a: v4a(0x67) = CONST 
    0x4e: CALLPRIVATE v4a(0x67), v49(0x1ffc9a700000000000000000000000000000000000000000000000000000000), v3e(0x4f)

    Begin block 0x4f
    prev=[0x3c], succ=[0x61]
    =================================
    0x50: v50(0x61) = CONST 
    0x54: v54(0x2711897) = CONST 
    0x59: v59(0xe5) = CONST 
    0x5b: v5b(0x4e2312e000000000000000000000000000000000000000000000000000000000) = SHL v59(0xe5), v54(0x2711897)
    0x5c: v5c(0x67) = CONST 
    0x60: CALLPRIVATE v5c(0x67), v5b(0x4e2312e000000000000000000000000000000000000000000000000000000000), v50(0x61)

    Begin block 0x61
    prev=[0x4f], succ=[0xf9]
    =================================
    0x62: v62(0xf9) = CONST 
    0x66: JUMP v62(0xf9)

    Begin block 0xf9
    prev=[0x61], succ=[]
    =================================
    0xfa: vfa(0x5561) = CONST 
    0xfe: vfe(0x109) = CONST 
    0x102: v102(0x0) = CONST 
    0x104: CODECOPY v102(0x0), vfe(0x109), vfa(0x5561)
    0x105: v105(0x0) = CONST 
    0x107: RETURN v105(0x0), vfa(0x5561)

}

function 0x67(0x67arg0x0, 0x67arg0x1) private {
    Begin block 0x67
    prev=[], succ=[0x7b, 0x9d]
    =================================
    0x68: v68(0x1) = CONST 
    0x6a: v6a(0x1) = CONST 
    0x6c: v6c(0xe0) = CONST 
    0x6e: v6e(0x100000000000000000000000000000000000000000000000000000000) = SHL v6c(0xe0), v6a(0x1)
    0x6f: v6f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v6e(0x100000000000000000000000000000000000000000000000000000000), v68(0x1)
    0x70: v70(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v6f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x73: v73 = AND v67arg0, v70(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x74: v74 = EQ v73, v70(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x75: v75 = ISZERO v74
    0x76: v76(0x9d) = CONST 
    0x7a: JUMPI v76(0x9d), v75

    Begin block 0x7b
    prev=[0x67], succ=[0xc2]
    =================================
    0x7b: v7b(0x40) = CONST 
    0x7d: v7d = MLOAD v7b(0x40)
    0x7e: v7e(0x461bcd) = CONST 
    0x82: v82(0xe5) = CONST 
    0x84: v84(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v82(0xe5), v7e(0x461bcd)
    0x86: MSTORE v7d, v84(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x87: v87(0x4) = CONST 
    0x89: v89 = ADD v87(0x4), v7d
    0x8a: v8a(0x94) = CONST 
    0x8f: v8f(0xc2) = CONST 
    0x93: JUMP v8f(0xc2)

    Begin block 0xc2
    prev=[0x7b], succ=[0x94]
    =================================
    0xc3: vc3(0x20) = CONST 
    0xc7: MSTORE v89, vc3(0x20)
    0xc8: vc8(0x1c) = CONST 
    0xcc: vcc = ADD v89, vc3(0x20)
    0xcd: MSTORE vcc, vc8(0x1c)
    0xce: vce(0x4552433136353a20696e76616c696420696e7465726661636520696400000000) = CONST 
    0xef: vef(0x40) = CONST 
    0xf2: vf2 = ADD v89, vef(0x40)
    0xf3: MSTORE vf2, vce(0x4552433136353a20696e76616c696420696e7465726661636520696400000000)
    0xf4: vf4(0x60) = CONST 
    0xf6: vf6 = ADD vf4(0x60), v89
    0xf8: JUMP v8a(0x94)

    Begin block 0x94
    prev=[0xc2], succ=[]
    =================================
    0x95: v95(0x40) = CONST 
    0x97: v97 = MLOAD v95(0x40)
    0x9a: v9a(0x64) = SUB vf6, v97
    0x9c: REVERT v97, v9a(0x64)

    Begin block 0x9d
    prev=[0x67], succ=[]
    =================================
    0x9e: v9e(0x1) = CONST 
    0xa0: va0(0x1) = CONST 
    0xa2: va2(0xe0) = CONST 
    0xa4: va4(0x100000000000000000000000000000000000000000000000000000000) = SHL va2(0xe0), va0(0x1)
    0xa5: va5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB va4(0x100000000000000000000000000000000000000000000000000000000), v9e(0x1)
    0xa6: va6(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT va5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0xa7: va7 = AND va6(0xffffffff00000000000000000000000000000000000000000000000000000000), v67arg0
    0xa8: va8(0x0) = CONST 
    0xac: MSTORE va8(0x0), va7
    0xad: vad(0x1a) = CONST 
    0xaf: vaf(0x20) = CONST 
    0xb1: MSTORE vaf(0x20), vad(0x1a)
    0xb2: vb2(0x40) = CONST 
    0xb5: vb5 = SHA3 va8(0x0), vb2(0x40)
    0xb7: vb7 = SLOAD vb5
    0xb8: vb8(0xff) = CONST 
    0xba: vba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT vb8(0xff)
    0xbb: vbb = AND vba(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vb7
    0xbc: vbc(0x1) = CONST 
    0xbe: vbe = OR vbc(0x1), vbb
    0xc0: SSTORE vb5, vbe
    0xc1: RETURNPRIVATE v67arg1

}

