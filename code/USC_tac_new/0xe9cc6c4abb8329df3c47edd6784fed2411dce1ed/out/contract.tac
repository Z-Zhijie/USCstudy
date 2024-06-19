function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x27b]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x273: v273(0x27b) = CONST 
    0x274: JUMPI v273(0x27b), v8

    Begin block 0xd
    prev=[0x0], succ=[0x27e, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x25b22bc) = CONST 
    0x19: v19 = EQ v14(0x25b22bc), v12
    0x275: v275(0x27e) = CONST 
    0x276: JUMPI v275(0x27e), v19

    Begin block 0x27e
    prev=[0xd], succ=[]
    =================================
    0x27f: v27f(0x8c) = CONST 
    0x280: CALLPRIVATE v27f(0x8c)

    Begin block 0x1e
    prev=[0xd], succ=[0x281, 0x29]
    =================================
    0x1f: v1f(0xdbe671f) = CONST 
    0x24: v24 = EQ v1f(0xdbe671f), v12
    0x277: v277(0x281) = CONST 
    0x278: JUMPI v277(0x281), v24

    Begin block 0x281
    prev=[0x1e], succ=[]
    =================================
    0x282: v282(0xdd) = CONST 
    0x283: CALLPRIVATE v282(0xdd)

    Begin block 0x29
    prev=[0x1e], succ=[0x27b, 0x284]
    =================================
    0x2a: v2a(0x64806a93) = CONST 
    0x2f: v2f = EQ v2a(0x64806a93), v12
    0x279: v279(0x284) = CONST 
    0x27a: JUMPI v279(0x284), v2f

    Begin block 0x27b
    prev=[0x0, 0x29], succ=[]
    =================================
    0x27c: v27c(0x34) = CONST 
    0x27d: CALLPRIVATE v27c(0x34)

    Begin block 0x284
    prev=[0x29], succ=[]
    =================================
    0x285: v285(0x134) = CONST 
    0x286: CALLPRIVATE v285(0x134)

}

function loadImplementation()() public {
    Begin block 0x134
    prev=[], succ=[0x13c, 0x140]
    =================================
    0x135: v135 = CALLVALUE 
    0x137: v137 = ISZERO v135
    0x138: v138(0x140) = CONST 
    0x13b: JUMPI v138(0x140), v137

    Begin block 0x13c
    prev=[0x134], succ=[]
    =================================
    0x13c: v13c(0x0) = CONST 
    0x13f: REVERT v13c(0x0), v13c(0x0)

    Begin block 0x140
    prev=[0x134], succ=[0x18bB0x140]
    =================================
    0x142: v142(0x149) = CONST 
    0x145: v145(0x18b) = CONST 
    0x148: JUMP v145(0x18b)

    Begin block 0x18bB0x140
    prev=[0x140], succ=[0x149]
    =================================
    0x18cS0x140: v18cV140(0x0) = CONST 
    0x18fS0x140: v18fV140(0x0) = CONST 
    0x192S0x140: v192V140 = SLOAD v18cV140(0x0)
    0x194S0x140: v194V140(0x100) = CONST 
    0x197S0x140: v197V140(0x1) = EXP v194V140(0x100), v18fV140(0x0)
    0x199S0x140: v199V140 = DIV v192V140, v197V140(0x1)
    0x19aS0x140: v19aV140(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1afS0x140: v1afV140 = AND v19aV140(0xffffffffffffffffffffffffffffffffffffffff), v199V140
    0x1b3S0x140: JUMP v142(0x149)

    Begin block 0x149
    prev=[0x18bB0x140], succ=[]
    =================================
    0x14a: v14a(0x40) = CONST 
    0x14c: v14c = MLOAD v14a(0x40)
    0x14f: v14f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x164: v164 = AND v14f(0xffffffffffffffffffffffffffffffffffffffff), v1afV140
    0x165: v165(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17a: v17a = AND v165(0xffffffffffffffffffffffffffffffffffffffff), v164
    0x17c: MSTORE v14c, v17a
    0x17d: v17d(0x20) = CONST 
    0x17f: v17f = ADD v17d(0x20), v14c
    0x183: v183(0x40) = CONST 
    0x185: v185 = MLOAD v183(0x40)
    0x188: v188(0x20) = SUB v17f, v185
    0x18a: RETURN v185, v188(0x20)

}

function fallback()() public {
    Begin block 0x34
    prev=[], succ=[0x18bB0x34]
    =================================
    0x35: v35(0x8a) = CONST 
    0x38: v38(0x3f) = CONST 
    0x3b: v3b(0x18b) = CONST 
    0x3e: JUMP v3b(0x18b)

    Begin block 0x18bB0x34
    prev=[0x34], succ=[0x3f]
    =================================
    0x18cS0x34: v18cV34(0x0) = CONST 
    0x18fS0x34: v18fV34(0x0) = CONST 
    0x192S0x34: v192V34 = SLOAD v18cV34(0x0)
    0x194S0x34: v194V34(0x100) = CONST 
    0x197S0x34: v197V34(0x1) = EXP v194V34(0x100), v18fV34(0x0)
    0x199S0x34: v199V34 = DIV v192V34, v197V34(0x1)
    0x19aS0x34: v19aV34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1afS0x34: v1afV34 = AND v19aV34(0xffffffffffffffffffffffffffffffffffffffff), v199V34
    0x1b3S0x34: JUMP v38(0x3f)

    Begin block 0x3f
    prev=[0x18bB0x34], succ=[0x1b4]
    =================================
    0x40: v40(0x0) = CONST 
    0x42: v42 = CALLDATASIZE 
    0x45: v45(0x1f) = CONST 
    0x47: v47 = ADD v45(0x1f), v42
    0x48: v48(0x20) = CONST 
    0x4c: v4c = DIV v47, v48(0x20)
    0x4d: v4d = MUL v4c, v48(0x20)
    0x4e: v4e(0x20) = CONST 
    0x50: v50 = ADD v4e(0x20), v4d
    0x51: v51(0x40) = CONST 
    0x53: v53 = MLOAD v51(0x40)
    0x56: v56 = ADD v53, v50
    0x57: v57(0x40) = CONST 
    0x59: MSTORE v57(0x40), v56
    0x61: MSTORE v53, v42
    0x62: v62(0x20) = CONST 
    0x64: v64 = ADD v62(0x20), v53
    0x6a: CALLDATACOPY v64, v40(0x0), v42
    0x6b: v6b(0x0) = CONST 
    0x6f: v6f = ADD v64, v42
    0x70: MSTORE v6f, v6b(0x0)
    0x71: v71(0x1f) = CONST 
    0x73: v73(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v71(0x1f)
    0x74: v74(0x1f) = CONST 
    0x77: v77 = ADD v42, v74(0x1f)
    0x78: v78 = AND v77, v73(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x7d: v7d = ADD v64, v78
    0x86: v86(0x1b4) = CONST 
    0x89: JUMP v86(0x1b4)

    Begin block 0x1b4
    prev=[0x3f], succ=[0x1da, 0x1d7]
    =================================
    0x1b5: v1b5(0x0) = CONST 
    0x1b9: v1b9 = MLOAD v53
    0x1ba: v1ba(0x20) = CONST 
    0x1bd: v1bd = ADD v53, v1ba(0x20)
    0x1bf: v1bf(0x2710) = CONST 
    0x1c2: v1c2 = GAS 
    0x1c3: v1c3 = SUB v1c2, v1bf(0x2710)
    0x1c4: v1c4 = DELEGATECALL v1c3, v1afV34, v1bd, v1b9, v1b5(0x0), v1b5(0x0)
    0x1c5: v1c5 = RETURNDATASIZE 
    0x1c6: v1c6(0x40) = CONST 
    0x1c8: v1c8 = MLOAD v1c6(0x40)
    0x1ca: v1ca(0x0) = CONST 
    0x1cd: RETURNDATACOPY v1c8, v1ca(0x0), v1c5
    0x1cf: v1cf(0x0) = CONST 
    0x1d2: v1d2 = EQ v1c4, v1cf(0x0)
    0x1d3: v1d3(0x1da) = CONST 
    0x1d6: JUMPI v1d3(0x1da), v1d2

    Begin block 0x1da
    prev=[0x1b4], succ=[]
    =================================
    0x1dd: REVERT v1c8, v1c5

    Begin block 0x1d7
    prev=[0x1b4], succ=[]
    =================================
    0x1d9: RETURN v1c8, v1c5

}

function updateImplementation(address)() public {
    Begin block 0x8c
    prev=[], succ=[0x94, 0x98]
    =================================
    0x8d: v8d = CALLVALUE 
    0x8f: v8f = ISZERO v8d
    0x90: v90(0x98) = CONST 
    0x93: JUMPI v90(0x98), v8f

    Begin block 0x94
    prev=[0x8c], succ=[]
    =================================
    0x94: v94(0x0) = CONST 
    0x97: REVERT v94(0x0), v94(0x0)

    Begin block 0x98
    prev=[0x8c], succ=[0xab, 0xaf]
    =================================
    0x9a: v9a(0xdb) = CONST 
    0x9d: v9d(0x4) = CONST 
    0xa0: va0 = CALLDATASIZE 
    0xa1: va1 = SUB va0, v9d(0x4)
    0xa2: va2(0x20) = CONST 
    0xa5: va5 = LT va1, va2(0x20)
    0xa6: va6 = ISZERO va5
    0xa7: va7(0xaf) = CONST 
    0xaa: JUMPI va7(0xaf), va6

    Begin block 0xab
    prev=[0x98], succ=[]
    =================================
    0xab: vab(0x0) = CONST 
    0xae: REVERT vab(0x0), vab(0x0)

    Begin block 0xaf
    prev=[0x98], succ=[0x1de]
    =================================
    0xb1: vb1 = ADD v9d(0x4), va1
    0xb5: vb5 = CALLDATALOAD v9d(0x4)
    0xb6: vb6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcb: vcb = AND vb6(0xffffffffffffffffffffffffffffffffffffffff), vb5
    0xcd: vcd(0x20) = CONST 
    0xcf: vcf(0x24) = ADD vcd(0x20), v9d(0x4)
    0xd7: vd7(0x1de) = CONST 
    0xda: JUMP vd7(0x1de)

    Begin block 0x1de
    prev=[0xaf], succ=[0xdb]
    =================================
    0x1e0: v1e0(0x0) = CONST 
    0x1e3: v1e3(0x100) = CONST 
    0x1e6: v1e6(0x1) = EXP v1e3(0x100), v1e0(0x0)
    0x1e8: v1e8 = SLOAD v1e0(0x0)
    0x1ea: v1ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ff: v1ff(0xffffffffffffffffffffffffffffffffffffffff) = MUL v1ea(0xffffffffffffffffffffffffffffffffffffffff), v1e6(0x1)
    0x200: v200(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x201: v201 = AND v200(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1e8
    0x204: v204(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x219: v219 = AND v204(0xffffffffffffffffffffffffffffffffffffffff), vcb
    0x21a: v21a = MUL v219, v1e6(0x1)
    0x21b: v21b = OR v21a, v201
    0x21d: SSTORE v1e0(0x0), v21b
    0x220: JUMP v9a(0xdb)

    Begin block 0xdb
    prev=[0x1de], succ=[]
    =================================
    0xdc: STOP 

}

function a()() public {
    Begin block 0xdd
    prev=[], succ=[0xe5, 0xe9]
    =================================
    0xde: vde = CALLVALUE 
    0xe0: ve0 = ISZERO vde
    0xe1: ve1(0xe9) = CONST 
    0xe4: JUMPI ve1(0xe9), ve0

    Begin block 0xe5
    prev=[0xdd], succ=[]
    =================================
    0xe5: ve5(0x0) = CONST 
    0xe8: REVERT ve5(0x0), ve5(0x0)

    Begin block 0xe9
    prev=[0xdd], succ=[0x221]
    =================================
    0xeb: veb(0xf2) = CONST 
    0xee: vee(0x221) = CONST 
    0xf1: JUMP vee(0x221)

    Begin block 0x221
    prev=[0xe9], succ=[0xf2]
    =================================
    0x222: v222(0x0) = CONST 
    0x226: v226 = SLOAD v222(0x0)
    0x228: v228(0x100) = CONST 
    0x22b: v22b(0x1) = EXP v228(0x100), v222(0x0)
    0x22d: v22d = DIV v226, v22b(0x1)
    0x22e: v22e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x243: v243 = AND v22e(0xffffffffffffffffffffffffffffffffffffffff), v22d
    0x245: JUMP veb(0xf2)

    Begin block 0xf2
    prev=[0x221], succ=[]
    =================================
    0xf3: vf3(0x40) = CONST 
    0xf5: vf5 = MLOAD vf3(0x40)
    0xf8: vf8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10d: v10d = AND vf8(0xffffffffffffffffffffffffffffffffffffffff), v243
    0x10e: v10e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x123: v123 = AND v10e(0xffffffffffffffffffffffffffffffffffffffff), v10d
    0x125: MSTORE vf5, v123
    0x126: v126(0x20) = CONST 
    0x128: v128 = ADD v126(0x20), vf5
    0x12c: v12c(0x40) = CONST 
    0x12e: v12e = MLOAD v12c(0x40)
    0x131: v131(0x20) = SUB v128, v12e
    0x133: RETURN v12e, v131(0x20)

}

