function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xe1]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26: v26(0x3b) = CONST 
    0x28: v28(0x0) = CONST 
    0x2a: v2a(0x100) = CONST 
    0x2d: v2d(0x1) = EXP v2a(0x100), v28(0x0)
    0x2f: v2f = SLOAD v26(0x3b)
    0x31: v31(0xffffffffffffffffffffffffffffffff) = CONST 
    0x42: v42(0xffffffffffffffffffffffffffffffff) = MUL v31(0xffffffffffffffffffffffffffffffff), v2d(0x1)
    0x43: v43(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) = NOT v42(0xffffffffffffffffffffffffffffffff)
    0x44: v44 = AND v43(0xffffffffffffffffffffffffffffffff00000000000000000000000000000000), v2f
    0x47: v47(0xf) = CONST 
    0x49: v49 = SIGNEXTEND v47(0xf), v5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x4a: v4a(0xffffffffffffffffffffffffffffffff) = CONST 
    0x5b: v5b = AND v4a(0xffffffffffffffffffffffffffffffff), v49
    0x5c: v5c = MUL v5b, v2d(0x1)
    0x5d: v5d = OR v5c, v44
    0x5f: SSTORE v26(0x3b), v5d
    0x61: v61(0x71) = CONST 
    0x65: v65 = CALLER 
    0x66: v66(0xe1) = CONST 
    0x6a: v6a(0x20) = CONST 
    0x6c: v6c(0xe100000000) = SHL v6a(0x20), v66(0xe1)
    0x6d: v6d(0x20) = CONST 
    0x6f: v6f(0xe1) = SHR v6d(0x20), v6c(0xe100000000)
    0x70: JUMP v6f(0xe1)

    Begin block 0xe1
    prev=[0x0], succ=[0x71]
    =================================
    0xe2: ve2(0x0) = CONST 
    0xe4: ve4(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x105: v105(0x0) = CONST 
    0x107: v107(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL v105(0x0), ve4(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x10c: SSTORE v107(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v65
    0x10f: JUMP v61(0x71)

    Begin block 0x71
    prev=[0xe1], succ=[0x110]
    =================================
    0x72: v72(0x81) = CONST 
    0x76: v76(0x110) = CONST 
    0x7a: v7a(0x20) = CONST 
    0x7c: v7c(0x11000000000) = SHL v7a(0x20), v76(0x110)
    0x7d: v7d(0x20) = CONST 
    0x7f: v7f(0x110) = SHR v7d(0x20), v7c(0x11000000000)
    0x80: JUMP v7f(0x110)

    Begin block 0x110
    prev=[0x71], succ=[0x81]
    =================================
    0x111: v111(0x0) = CONST 
    0x114: v114(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x135: v135(0x0) = CONST 
    0x137: v137(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = SHL v135(0x0), v114(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x13b: v13b = SLOAD v137(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x140: JUMP v72(0x81)

    Begin block 0x81
    prev=[0x110], succ=[0x141]
    =================================
    0x82: v82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x97: v97 = AND v82(0xffffffffffffffffffffffffffffffffffffffff), v13b
    0x98: v98(0x0) = CONST 
    0x9a: v9a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf: vaf(0x0) = AND v9a(0xffffffffffffffffffffffffffffffffffffffff), v98(0x0)
    0xb0: vb0(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0xd1: vd1(0x40) = CONST 
    0xd3: vd3 = MLOAD vd1(0x40)
    0xd4: vd4(0x40) = CONST 
    0xd6: vd6 = MLOAD vd4(0x40)
    0xd9: vd9(0x0) = SUB vd3, vd6
    0xdb: LOG3 vd6, vd9(0x0), vb0(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), vaf(0x0), v97
    0xdc: vdc(0x141) = CONST 
    0xe0: JUMP vdc(0x141)

    Begin block 0x141
    prev=[0x81], succ=[]
    =================================
    0x142: v142(0x3f52) = CONST 
    0x146: v146(0x151) = CONST 
    0x14a: v14a(0x0) = CONST 
    0x14c: CODECOPY v14a(0x0), v146(0x151), v142(0x3f52)
    0x14d: v14d(0x0) = CONST 
    0x14f: RETURN v14d(0x0), v142(0x3f52)

}

