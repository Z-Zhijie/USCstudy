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
    prev=[0x0], succ=[0x7b, 0x7c]
    =================================
    0x12: v12(0x40) = CONST 
    0x14: v14 = MLOAD v12(0x40)
    0x17: v17(0x6376632e70726f78792e696d706c656d656e746174696f6e0000000000000000) = CONST 
    0x39: MSTORE v14, v17(0x6376632e70726f78792e696d706c656d656e746174696f6e0000000000000000)
    0x3b: v3b(0x18) = CONST 
    0x3d: v3d = ADD v3b(0x18), v14
    0x40: v40(0x40) = CONST 
    0x42: v42 = MLOAD v40(0x40)
    0x45: v45(0x18) = SUB v3d, v42
    0x47: v47 = SHA3 v42, v45(0x18)
    0x48: v48(0x0) = CONST 
    0x4a: v4a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v48(0x0)
    0x4b: v4b = AND v4a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v47
    0x4c: v4c(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb) = CONST 
    0x6d: v6d(0x1) = CONST 
    0x6f: v6f(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb) = MUL v6d(0x1), v4c(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb)
    0x70: v70(0x0) = CONST 
    0x72: v72(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v70(0x0)
    0x73: v73(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb) = AND v72(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v6f(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb)
    0x74: v74 = EQ v73(0xa490aab0d89837371982f93f57ffd20c47991f88066ef92475bc8233036969bb), v4b
    0x75: v75 = ISZERO v74
    0x76: v76 = ISZERO v75
    0x77: v77(0x7c) = CONST 
    0x7a: JUMPI v77(0x7c), v76

    Begin block 0x7b
    prev=[0x10], succ=[]
    =================================
    0x7b: THROW 

    Begin block 0x7c
    prev=[0x10], succ=[0xe6, 0xe7]
    =================================
    0x7d: v7d(0x40) = CONST 
    0x7f: v7f = MLOAD v7d(0x40)
    0x82: v82(0x6376632e70726f78792e61646d696e0000000000000000000000000000000000) = CONST 
    0xa4: MSTORE v7f, v82(0x6376632e70726f78792e61646d696e0000000000000000000000000000000000)
    0xa6: va6(0xf) = CONST 
    0xa8: va8 = ADD va6(0xf), v7f
    0xab: vab(0x40) = CONST 
    0xad: vad = MLOAD vab(0x40)
    0xb0: vb0(0xf) = SUB va8, vad
    0xb2: vb2 = SHA3 vad, vb0(0xf)
    0xb3: vb3(0x0) = CONST 
    0xb5: vb5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vb3(0x0)
    0xb6: vb6 = AND vb5(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vb2
    0xb7: vb7(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433) = CONST 
    0xd8: vd8(0x1) = CONST 
    0xda: vda(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433) = MUL vd8(0x1), vb7(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433)
    0xdb: vdb(0x0) = CONST 
    0xdd: vdd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT vdb(0x0)
    0xde: vde(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433) = AND vdd(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), vda(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433)
    0xdf: vdf = EQ vde(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433), vb6
    0xe0: ve0 = ISZERO vdf
    0xe1: ve1 = ISZERO ve0
    0xe2: ve2(0xe7) = CONST 
    0xe5: JUMPI ve2(0xe7), ve1

    Begin block 0xe6
    prev=[0x7c], succ=[]
    =================================
    0xe6: THROW 

    Begin block 0xe7
    prev=[0x7c], succ=[0x104]
    =================================
    0xe8: ve8(0xff) = CONST 
    0xeb: veb = CALLER 
    0xec: vec(0x104) = CONST 
    0xef: vef(0x100000000) = CONST 
    0xf5: vf5(0x10400000000) = MUL vef(0x100000000), vec(0x104)
    0xf6: vf6(0x100000000) = CONST 
    0xfd: vfd(0x104) = DIV vf5(0x10400000000), vf6(0x100000000)
    0xfe: JUMP vfd(0x104)

    Begin block 0x104
    prev=[0xe7], succ=[0xff]
    =================================
    0x105: v105(0x0) = CONST 
    0x107: v107(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433) = CONST 
    0x128: v128(0x1) = CONST 
    0x12a: v12a(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433) = MUL v128(0x1), v107(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433)
    0x12f: SSTORE v12a(0x2bbac3e52eee27be250d682577104e2abe776c40160cd3167b24633933100433), veb
    0x132: JUMP ve8(0xff)

    Begin block 0xff
    prev=[0x104], succ=[0x133]
    =================================
    0x100: v100(0x133) = CONST 
    0x103: JUMP v100(0x133)

    Begin block 0x133
    prev=[0xff], succ=[]
    =================================
    0x134: v134(0x9e6) = CONST 
    0x138: v138(0x142) = CONST 
    0x13b: v13b(0x0) = CONST 
    0x13d: CODECOPY v13b(0x0), v138(0x142), v134(0x9e6)
    0x13e: v13e(0x0) = CONST 
    0x140: RETURN v13e(0x0), v134(0x9e6)

}

