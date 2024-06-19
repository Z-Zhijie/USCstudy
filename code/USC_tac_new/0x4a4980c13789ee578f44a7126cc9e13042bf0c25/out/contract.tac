function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xe, 0x1ab]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x9: v9(0x1ab) = CONST 
    0xd: JUMPI v9(0x1ab), v8

    Begin block 0xe
    prev=[0x0], succ=[0x20, 0xe5]
    =================================
    0xe: ve(0x0) = CONST 
    0x10: v10 = CALLDATALOAD ve(0x0)
    0x11: v11(0xe0) = CONST 
    0x13: v13 = SHR v11(0xe0), v10
    0x15: v15(0x8da5cb5b) = CONST 
    0x1a: v1a = GT v15(0x8da5cb5b), v13
    0x1b: v1b(0xe5) = CONST 
    0x1f: JUMPI v1b(0xe5), v1a

    Begin block 0x20
    prev=[0xe], succ=[0x97, 0x2c]
    =================================
    0x21: v21(0xcbe25197) = CONST 
    0x26: v26 = GT v21(0xcbe25197), v13
    0x27: v27(0x97) = CONST 
    0x2b: JUMPI v27(0x97), v26

    Begin block 0x97
    prev=[0x20], succ=[0xa4, 0x41f4]
    =================================
    0x99: v99(0x8da5cb5b) = CONST 
    0x9e: v9e = EQ v99(0x8da5cb5b), v13
    0x41a4: v41a4(0x41f4) = CONST 
    0x41a5: JUMPI v41a4(0x41f4), v9e

    Begin block 0xa4
    prev=[0x97], succ=[0x41f7, 0xb0]
    =================================
    0xa5: va5(0x953612b5) = CONST 
    0xaa: vaa = EQ va5(0x953612b5), v13
    0x41a6: v41a6(0x41f7) = CONST 
    0x41a7: JUMPI v41a6(0x41f7), vaa

    Begin block 0x41f7
    prev=[0xa4], succ=[]
    =================================
    0x41f8: v41f8(0x426) = CONST 
    0x41f9: CALLPRIVATE v41f8(0x426)

    Begin block 0xb0
    prev=[0xa4], succ=[0x41fa, 0xbc]
    =================================
    0xb1: vb1(0xac4afa38) = CONST 
    0xb6: vb6 = EQ vb1(0xac4afa38), v13
    0x41a8: v41a8(0x41fa) = CONST 
    0x41a9: JUMPI v41a8(0x41fa), vb6

    Begin block 0x41fa
    prev=[0xb0], succ=[]
    =================================
    0x41fb: v41fb(0x4d2) = CONST 
    0x41fc: CALLPRIVATE v41fb(0x4d2)

    Begin block 0xbc
    prev=[0xb0], succ=[0x41fd, 0xc8]
    =================================
    0xbd: vbd(0xaf1c0db0) = CONST 
    0xc2: vc2 = EQ vbd(0xaf1c0db0), v13
    0x41aa: v41aa(0x41fd) = CONST 
    0x41ab: JUMPI v41aa(0x41fd), vc2

    Begin block 0x41fd
    prev=[0xbc], succ=[]
    =================================
    0x41fe: v41fe(0x500) = CONST 
    0x41ff: CALLPRIVATE v41fe(0x500)

    Begin block 0xc8
    prev=[0xbc], succ=[0x4200, 0xd4]
    =================================
    0xc9: vc9(0xb39e12cf) = CONST 
    0xce: vce = EQ vc9(0xb39e12cf), v13
    0x41ac: v41ac(0x4200) = CONST 
    0x41ad: JUMPI v41ac(0x4200), vce

    Begin block 0x4200
    prev=[0xc8], succ=[]
    =================================
    0x4201: v4201(0x53f) = CONST 
    0x4202: CALLPRIVATE v4201(0x53f)

    Begin block 0xd4
    prev=[0xc8], succ=[0xe0, 0x4203]
    =================================
    0xd5: vd5(0xbd097e21) = CONST 
    0xda: vda = EQ vd5(0xbd097e21), v13
    0x41ae: v41ae(0x4203) = CONST 
    0x41af: JUMPI v41ae(0x4203), vda

    Begin block 0xe0
    prev=[0xd4], succ=[0x3891]
    =================================
    0xe0: ve0(0x3891) = CONST 
    0xe4: JUMP ve0(0x3891)

    Begin block 0x3891
    prev=[0xe0], succ=[]
    =================================
    0x3892: v3892(0x0) = CONST 
    0x3895: REVERT v3892(0x0), v3892(0x0)

    Begin block 0x4203
    prev=[0xd4], succ=[]
    =================================
    0x4204: v4204(0x557) = CONST 
    0x4205: CALLPRIVATE v4204(0x557)

    Begin block 0x41f4
    prev=[0x97], succ=[]
    =================================
    0x41f5: v41f5(0x40e) = CONST 
    0x41f6: CALLPRIVATE v41f5(0x40e)

    Begin block 0x2c
    prev=[0x20], succ=[0x6d, 0x38]
    =================================
    0x2d: v2d(0xde260f37) = CONST 
    0x32: v32 = GT v2d(0xde260f37), v13
    0x33: v33(0x6d) = CONST 
    0x37: JUMPI v33(0x6d), v32

    Begin block 0x6d
    prev=[0x2c], succ=[0x4206, 0x7a]
    =================================
    0x6f: v6f(0xcbe25197) = CONST 
    0x74: v74 = EQ v6f(0xcbe25197), v13
    0x419e: v419e(0x4206) = CONST 
    0x419f: JUMPI v419e(0x4206), v74

    Begin block 0x4206
    prev=[0x6d], succ=[]
    =================================
    0x4207: v4207(0x56f) = CONST 
    0x4208: CALLPRIVATE v4207(0x56f)

    Begin block 0x7a
    prev=[0x6d], succ=[0x4209, 0x86]
    =================================
    0x7b: v7b(0xcfad00b8) = CONST 
    0x80: v80 = EQ v7b(0xcfad00b8), v13
    0x41a0: v41a0(0x4209) = CONST 
    0x41a1: JUMPI v41a0(0x4209), v80

    Begin block 0x4209
    prev=[0x7a], succ=[]
    =================================
    0x420a: v420a(0x5a6) = CONST 
    0x420b: CALLPRIVATE v420a(0x5a6)

    Begin block 0x86
    prev=[0x7a], succ=[0x92, 0x420c]
    =================================
    0x87: v87(0xdbdd2989) = CONST 
    0x8c: v8c = EQ v87(0xdbdd2989), v13
    0x41a2: v41a2(0x420c) = CONST 
    0x41a3: JUMPI v41a2(0x420c), v8c

    Begin block 0x92
    prev=[0x86], succ=[0x386d]
    =================================
    0x92: v92(0x386d) = CONST 
    0x96: JUMP v92(0x386d)

    Begin block 0x386d
    prev=[0x92], succ=[]
    =================================
    0x386e: v386e(0x0) = CONST 
    0x3871: REVERT v386e(0x0), v386e(0x0)

    Begin block 0x420c
    prev=[0x86], succ=[]
    =================================
    0x420d: v420d(0x5dd) = CONST 
    0x420e: CALLPRIVATE v420d(0x5dd)

    Begin block 0x38
    prev=[0x2c], succ=[0x44, 0x420f]
    =================================
    0x39: v39(0xde260f37) = CONST 
    0x3e: v3e = EQ v39(0xde260f37), v13
    0x4196: v4196(0x420f) = CONST 
    0x4197: JUMPI v4196(0x420f), v3e

    Begin block 0x44
    prev=[0x38], succ=[0x4212, 0x50]
    =================================
    0x45: v45(0xe3fedc51) = CONST 
    0x4a: v4a = EQ v45(0xe3fedc51), v13
    0x4198: v4198(0x4212) = CONST 
    0x4199: JUMPI v4198(0x4212), v4a

    Begin block 0x4212
    prev=[0x44], succ=[]
    =================================
    0x4213: v4213(0x653) = CONST 
    0x4214: CALLPRIVATE v4213(0x653)

    Begin block 0x50
    prev=[0x44], succ=[0x4215, 0x5c]
    =================================
    0x51: v51(0xeb7e3a5c) = CONST 
    0x56: v56 = EQ v51(0xeb7e3a5c), v13
    0x419a: v419a(0x4215) = CONST 
    0x419b: JUMPI v419a(0x4215), v56

    Begin block 0x4215
    prev=[0x50], succ=[]
    =================================
    0x4216: v4216(0x740) = CONST 
    0x4217: CALLPRIVATE v4216(0x740)

    Begin block 0x5c
    prev=[0x50], succ=[0x68, 0x4218]
    =================================
    0x5d: v5d(0xf3bc96ea) = CONST 
    0x62: v62 = EQ v5d(0xf3bc96ea), v13
    0x419c: v419c(0x4218) = CONST 
    0x419d: JUMPI v419c(0x4218), v62

    Begin block 0x68
    prev=[0x5c], succ=[0x3849]
    =================================
    0x68: v68(0x3849) = CONST 
    0x6c: JUMP v68(0x3849)

    Begin block 0x3849
    prev=[0x68], succ=[]
    =================================
    0x384a: v384a(0x0) = CONST 
    0x384d: REVERT v384a(0x0), v384a(0x0)

    Begin block 0x4218
    prev=[0x5c], succ=[]
    =================================
    0x4219: v4219(0x783) = CONST 
    0x421a: CALLPRIVATE v4219(0x783)

    Begin block 0x420f
    prev=[0x38], succ=[]
    =================================
    0x4210: v4210(0x61c) = CONST 
    0x4211: CALLPRIVATE v4210(0x61c)

    Begin block 0xe5
    prev=[0xe], succ=[0x15d, 0xf2]
    =================================
    0xe7: ve7(0x30bc3daa) = CONST 
    0xec: vec = GT ve7(0x30bc3daa), v13
    0xed: ved(0x15d) = CONST 
    0xf1: JUMPI ved(0x15d), vec

    Begin block 0x15d
    prev=[0xe5], succ=[0x41cd, 0x16a]
    =================================
    0x15f: v15f(0xfd6240e) = CONST 
    0x164: v164 = EQ v15f(0xfd6240e), v13
    0x41be: v41be(0x41cd) = CONST 
    0x41bf: JUMPI v41be(0x41cd), v164

    Begin block 0x41cd
    prev=[0x15d], succ=[]
    =================================
    0x41ce: v41ce(0x1b8) = CONST 
    0x41cf: CALLPRIVATE v41ce(0x1b8)

    Begin block 0x16a
    prev=[0x15d], succ=[0x41d0, 0x176]
    =================================
    0x16b: v16b(0x158ef93e) = CONST 
    0x170: v170 = EQ v16b(0x158ef93e), v13
    0x41c0: v41c0(0x41d0) = CONST 
    0x41c1: JUMPI v41c0(0x41d0), v170

    Begin block 0x41d0
    prev=[0x16a], succ=[]
    =================================
    0x41d1: v41d1(0x1ec) = CONST 
    0x41d2: CALLPRIVATE v41d1(0x1ec)

    Begin block 0x176
    prev=[0x16a], succ=[0x41d3, 0x182]
    =================================
    0x177: v177(0x1ebeef89) = CONST 
    0x17c: v17c = EQ v177(0x1ebeef89), v13
    0x41c2: v41c2(0x41d3) = CONST 
    0x41c3: JUMPI v41c2(0x41d3), v17c

    Begin block 0x41d3
    prev=[0x176], succ=[]
    =================================
    0x41d4: v41d4(0x218) = CONST 
    0x41d5: CALLPRIVATE v41d4(0x218)

    Begin block 0x182
    prev=[0x176], succ=[0x41d6, 0x18e]
    =================================
    0x183: v183(0x21dadb75) = CONST 
    0x188: v188 = EQ v183(0x21dadb75), v13
    0x41c4: v41c4(0x41d6) = CONST 
    0x41c5: JUMPI v41c4(0x41d6), v188

    Begin block 0x41d6
    prev=[0x182], succ=[]
    =================================
    0x41d7: v41d7(0x230) = CONST 
    0x41d8: CALLPRIVATE v41d7(0x230)

    Begin block 0x18e
    prev=[0x182], succ=[0x41d9, 0x19a]
    =================================
    0x18f: v18f(0x220cce97) = CONST 
    0x194: v194 = EQ v18f(0x220cce97), v13
    0x41c6: v41c6(0x41d9) = CONST 
    0x41c7: JUMPI v41c6(0x41d9), v194

    Begin block 0x41d9
    prev=[0x18e], succ=[]
    =================================
    0x41da: v41da(0x248) = CONST 
    0x41db: CALLPRIVATE v41da(0x248)

    Begin block 0x19a
    prev=[0x18e], succ=[0x1a6, 0x41dc]
    =================================
    0x19b: v19b(0x2ff55e87) = CONST 
    0x1a0: v1a0 = EQ v19b(0x2ff55e87), v13
    0x41c8: v41c8(0x41dc) = CONST 
    0x41c9: JUMPI v41c8(0x41dc), v1a0

    Begin block 0x1a6
    prev=[0x19a], succ=[0x38fd]
    =================================
    0x1a6: v1a6(0x38fd) = CONST 
    0x1aa: JUMP v1a6(0x38fd)

    Begin block 0x38fd
    prev=[0x1a6], succ=[]
    =================================
    0x38fe: v38fe(0x0) = CONST 
    0x3901: REVERT v38fe(0x0), v38fe(0x0)

    Begin block 0x41dc
    prev=[0x19a], succ=[]
    =================================
    0x41dd: v41dd(0x260) = CONST 
    0x41de: CALLPRIVATE v41dd(0x260)

    Begin block 0xf2
    prev=[0xe5], succ=[0x133, 0xfe]
    =================================
    0xf3: vf3(0x5a2e2f47) = CONST 
    0xf8: vf8 = GT vf3(0x5a2e2f47), v13
    0xf9: vf9(0x133) = CONST 
    0xfd: JUMPI vf9(0x133), vf8

    Begin block 0x133
    prev=[0xf2], succ=[0x41df, 0x140]
    =================================
    0x135: v135(0x30bc3daa) = CONST 
    0x13a: v13a = EQ v135(0x30bc3daa), v13
    0x41b8: v41b8(0x41df) = CONST 
    0x41b9: JUMPI v41b8(0x41df), v13a

    Begin block 0x41df
    prev=[0x133], succ=[]
    =================================
    0x41e0: v41e0(0x2a9) = CONST 
    0x41e1: CALLPRIVATE v41e0(0x2a9)

    Begin block 0x140
    prev=[0x133], succ=[0x41e2, 0x14c]
    =================================
    0x141: v141(0x46951954) = CONST 
    0x146: v146 = EQ v141(0x46951954), v13
    0x41ba: v41ba(0x41e2) = CONST 
    0x41bb: JUMPI v41ba(0x41e2), v146

    Begin block 0x41e2
    prev=[0x140], succ=[]
    =================================
    0x41e3: v41e3(0x302) = CONST 
    0x41e4: CALLPRIVATE v41e3(0x302)

    Begin block 0x14c
    prev=[0x140], succ=[0x158, 0x41e5]
    =================================
    0x14d: v14d(0x52d1902d) = CONST 
    0x152: v152 = EQ v14d(0x52d1902d), v13
    0x41bc: v41bc(0x41e5) = CONST 
    0x41bd: JUMPI v41bc(0x41e5), v152

    Begin block 0x158
    prev=[0x14c], succ=[0x38d9]
    =================================
    0x158: v158(0x38d9) = CONST 
    0x15c: JUMP v158(0x38d9)

    Begin block 0x38d9
    prev=[0x158], succ=[]
    =================================
    0x38da: v38da(0x0) = CONST 
    0x38dd: REVERT v38da(0x0), v38da(0x0)

    Begin block 0x41e5
    prev=[0x14c], succ=[]
    =================================
    0x41e6: v41e6(0x339) = CONST 
    0x41e7: CALLPRIVATE v41e6(0x339)

    Begin block 0xfe
    prev=[0xf2], succ=[0x41e8, 0x10a]
    =================================
    0xff: vff(0x5a2e2f47) = CONST 
    0x104: v104 = EQ vff(0x5a2e2f47), v13
    0x41b0: v41b0(0x41e8) = CONST 
    0x41b1: JUMPI v41b0(0x41e8), v104

    Begin block 0x41e8
    prev=[0xfe], succ=[]
    =================================
    0x41e9: v41e9(0x351) = CONST 
    0x41ea: CALLPRIVATE v41e9(0x351)

    Begin block 0x10a
    prev=[0xfe], succ=[0x41eb, 0x116]
    =================================
    0x10b: v10b(0x5b55c1b1) = CONST 
    0x110: v110 = EQ v10b(0x5b55c1b1), v13
    0x41b2: v41b2(0x41eb) = CONST 
    0x41b3: JUMPI v41b2(0x41eb), v110

    Begin block 0x41eb
    prev=[0x10a], succ=[]
    =================================
    0x41ec: v41ec(0x388) = CONST 
    0x41ed: CALLPRIVATE v41ec(0x388)

    Begin block 0x116
    prev=[0x10a], succ=[0x41ee, 0x122]
    =================================
    0x117: v117(0x7b103999) = CONST 
    0x11c: v11c = EQ v117(0x7b103999), v13
    0x41b4: v41b4(0x41ee) = CONST 
    0x41b5: JUMPI v41b4(0x41ee), v11c

    Begin block 0x41ee
    prev=[0x116], succ=[]
    =================================
    0x41ef: v41ef(0x3c5) = CONST 
    0x41f0: CALLPRIVATE v41ef(0x3c5)

    Begin block 0x122
    prev=[0x116], succ=[0x12e, 0x41f1]
    =================================
    0x123: v123(0x8463dd84) = CONST 
    0x128: v128 = EQ v123(0x8463dd84), v13
    0x41b6: v41b6(0x41f1) = CONST 
    0x41b7: JUMPI v41b6(0x41f1), v128

    Begin block 0x12e
    prev=[0x122], succ=[0x38b5]
    =================================
    0x12e: v12e(0x38b5) = CONST 
    0x132: JUMP v12e(0x38b5)

    Begin block 0x38b5
    prev=[0x12e], succ=[]
    =================================
    0x38b6: v38b6(0x0) = CONST 
    0x38b9: REVERT v38b6(0x0), v38b6(0x0)

    Begin block 0x41f1
    prev=[0x122], succ=[]
    =================================
    0x41f2: v41f2(0x3dd) = CONST 
    0x41f3: CALLPRIVATE v41f2(0x3dd)

    Begin block 0x1ab
    prev=[0x0], succ=[0x41ca, 0x3921]
    =================================
    0x1ac: v1ac = CALLDATASIZE 
    0x1ad: v1ad(0x3921) = CONST 
    0x1b1: JUMPI v1ad(0x3921), v1ac

    Begin block 0x41ca
    prev=[0x1ab], succ=[]
    =================================
    0x41ca: v41ca(0x41cc) = CONST 
    0x41cb: CALLPRIVATE v41ca(0x41cc)

    Begin block 0x3921
    prev=[0x1ab], succ=[]
    =================================
    0x3922: v3922(0x0) = CONST 
    0x3925: REVERT v3922(0x0), v3922(0x0)

}

function devContract()() public {
    Begin block 0x1b8
    prev=[], succ=[0x1c1, 0x1c5]
    =================================
    0x1b9: v1b9 = CALLVALUE 
    0x1bb: v1bb = ISZERO v1b9
    0x1bc: v1bc(0x1c5) = CONST 
    0x1c0: JUMPI v1bc(0x1c5), v1bb

    Begin block 0x1c1
    prev=[0x1b8], succ=[]
    =================================
    0x1c1: v1c1(0x0) = CONST 
    0x1c4: REVERT v1c1(0x0), v1c1(0x0)

    Begin block 0x1c5
    prev=[0x1b8], succ=[0x79b]
    =================================
    0x1c7: v1c7(0x3945) = CONST 
    0x1cb: v1cb(0x79b) = CONST 
    0x1cf: JUMP v1cb(0x79b)

    Begin block 0x79b
    prev=[0x1c5], succ=[0x3945]
    =================================
    0x79c: v79c(0x9) = CONST 
    0x79e: v79e = SLOAD v79c(0x9)
    0x79f: v79f(0x1) = CONST 
    0x7a1: v7a1(0x1) = CONST 
    0x7a3: v7a3(0xa0) = CONST 
    0x7a5: v7a5(0x10000000000000000000000000000000000000000) = SHL v7a3(0xa0), v7a1(0x1)
    0x7a6: v7a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7a5(0x10000000000000000000000000000000000000000), v79f(0x1)
    0x7a7: v7a7 = AND v7a6(0xffffffffffffffffffffffffffffffffffffffff), v79e
    0x7a9: JUMP v1c7(0x3945)

    Begin block 0x3945
    prev=[0x79b], succ=[]
    =================================
    0x3946: v3946(0x40) = CONST 
    0x3949: v3949 = MLOAD v3946(0x40)
    0x394a: v394a(0x1) = CONST 
    0x394c: v394c(0x1) = CONST 
    0x394e: v394e(0xa0) = CONST 
    0x3950: v3950(0x10000000000000000000000000000000000000000) = SHL v394e(0xa0), v394c(0x1)
    0x3951: v3951(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3950(0x10000000000000000000000000000000000000000), v394a(0x1)
    0x3954: v3954 = AND v7a7, v3951(0xffffffffffffffffffffffffffffffffffffffff)
    0x3956: MSTORE v3949, v3954
    0x3957: v3957 = MLOAD v3946(0x40)
    0x395b: v395b(0x0) = SUB v3949, v3957
    0x395c: v395c(0x20) = CONST 
    0x395e: v395e(0x20) = ADD v395c(0x20), v395b(0x0)
    0x3960: RETURN v3957, v395e(0x20)

}

function 0x1e23(0x1e23arg0x0, 0x1e23arg0x1, 0x1e23arg0x2) private {
    Begin block 0x1e23
    prev=[], succ=[0x1e340x1e23, 0x1e2c0x1e23]
    =================================
    0x1e24: v1e24(0x0) = CONST 
    0x1e27: v1e27(0x1e34) = CONST 
    0x1e2b: JUMPI v1e27(0x1e34), v1e23arg1

    Begin block 0x1e340x1e23
    prev=[0x1e23], succ=[0x1e410x1e23, 0x1e420x1e23]
    =================================
    0x1e370x1e23: v1e231e37 = MUL v1e23arg0, v1e23arg1
    0x1e3c0x1e23: v1e231e3c(0x1e42) = CONST 
    0x1e400x1e23: JUMPI v1e231e3c(0x1e42), v1e23arg1

    Begin block 0x1e410x1e23
    prev=[0x1e340x1e23], succ=[]
    =================================
    0x1e410x1e23: THROW 

    Begin block 0x1e420x1e23
    prev=[0x1e340x1e23], succ=[0x1e4a0x1e23, 0x40110x1e23]
    =================================
    0x1e430x1e23: v1e231e43 = DIV v1e231e37, v1e23arg1
    0x1e440x1e23: v1e231e44 = EQ v1e231e43, v1e23arg0
    0x1e450x1e23: v1e231e45(0x4011) = CONST 
    0x1e490x1e23: JUMPI v1e231e45(0x4011), v1e231e44

    Begin block 0x1e4a0x1e23
    prev=[0x1e420x1e23], succ=[]
    =================================
    0x1e4a0x1e23: v1e231e4a(0x40) = CONST 
    0x1e4c0x1e23: v1e231e4c = MLOAD v1e231e4a(0x40)
    0x1e4d0x1e23: v1e231e4d(0x461bcd) = CONST 
    0x1e510x1e23: v1e231e51(0xe5) = CONST 
    0x1e530x1e23: v1e231e53(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e231e51(0xe5), v1e231e4d(0x461bcd)
    0x1e550x1e23: MSTORE v1e231e4c, v1e231e53(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e560x1e23: v1e231e56(0x4) = CONST 
    0x1e580x1e23: v1e231e58 = ADD v1e231e56(0x4), v1e231e4c
    0x1e5b0x1e23: v1e231e5b(0x20) = CONST 
    0x1e5d0x1e23: v1e231e5d = ADD v1e231e5b(0x20), v1e231e58
    0x1e600x1e23: v1e231e60(0x20) = SUB v1e231e5d, v1e231e58
    0x1e620x1e23: MSTORE v1e231e58, v1e231e60(0x20)
    0x1e630x1e23: v1e231e63(0x21) = CONST 
    0x1e660x1e23: MSTORE v1e231e5d, v1e231e63(0x21)
    0x1e670x1e23: v1e231e67(0x20) = CONST 
    0x1e690x1e23: v1e231e69 = ADD v1e231e67(0x20), v1e231e5d
    0x1e6b0x1e23: v1e231e6b(0x378a) = CONST 
    0x1e6f0x1e23: v1e231e6f(0x21) = CONST 
    0x1e720x1e23: CODECOPY v1e231e69, v1e231e6b(0x378a), v1e231e6f(0x21)
    0x1e730x1e23: v1e231e73(0x40) = CONST 
    0x1e750x1e23: v1e231e75 = ADD v1e231e73(0x40), v1e231e69
    0x1e790x1e23: v1e231e79(0x40) = CONST 
    0x1e7b0x1e23: v1e231e7b = MLOAD v1e231e79(0x40)
    0x1e7e0x1e23: v1e231e7e(0x84) = SUB v1e231e75, v1e231e7b
    0x1e800x1e23: REVERT v1e231e7b, v1e231e7e(0x84)

    Begin block 0x40110x1e23
    prev=[0x1e420x1e23], succ=[]
    =================================
    0x40170x1e23: RETURNPRIVATE v1e23arg2, v1e231e37

    Begin block 0x1e2c0x1e23
    prev=[0x1e23], succ=[0xf450x1e23]
    =================================
    0x1e2d0x1e23: v1e231e2d(0x0) = CONST 
    0x1e2f0x1e23: v1e231e2f(0xf45) = CONST 
    0x1e330x1e23: JUMP v1e231e2f(0xf45)

    Begin block 0xf450x1e23
    prev=[0x1e2c0x1e23], succ=[]
    =================================
    0xf4a0x1e23: RETURNPRIVATE v1e23arg2, v1e231e2d(0x0)

}

function 0x1e81(0x1e81arg0x0, 0x1e81arg0x1, 0x1e81arg0x2) private {
    Begin block 0x1e81
    prev=[], succ=[0x21200x1e81]
    =================================
    0x1e82: v1e82(0x0) = CONST 
    0x1e84: v1e84(0x4037) = CONST 
    0x1e8a: v1e8a(0x40) = CONST 
    0x1e8c: v1e8c = MLOAD v1e8a(0x40)
    0x1e8e: v1e8e(0x40) = CONST 
    0x1e90: v1e90 = ADD v1e8e(0x40), v1e8c
    0x1e91: v1e91(0x40) = CONST 
    0x1e93: MSTORE v1e91(0x40), v1e90
    0x1e95: v1e95(0x1a) = CONST 
    0x1e98: MSTORE v1e8c, v1e95(0x1a)
    0x1e99: v1e99(0x20) = CONST 
    0x1e9b: v1e9b = ADD v1e99(0x20), v1e8c
    0x1e9c: v1e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1ebe: MSTORE v1e9b, v1e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1ec0: v1ec0(0x2120) = CONST 
    0x1ec4: JUMP v1ec0(0x2120)

    Begin block 0x21200x1e81
    prev=[0x1e81], succ=[0x212a0x1e81, 0x21b00x1e81]
    =================================
    0x21210x1e81: v1e812121(0x0) = CONST 
    0x21250x1e81: v1e812125(0x21b0) = CONST 
    0x21290x1e81: JUMPI v1e812125(0x21b0), v1e81arg0

    Begin block 0x212a0x1e81
    prev=[0x21200x1e81], succ=[0x215a0x1e81]
    =================================
    0x212a0x1e81: v1e81212a(0x40) = CONST 
    0x212c0x1e81: v1e81212c = MLOAD v1e81212a(0x40)
    0x212d0x1e81: v1e81212d(0x461bcd) = CONST 
    0x21310x1e81: v1e812131(0xe5) = CONST 
    0x21330x1e81: v1e812133(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e812131(0xe5), v1e81212d(0x461bcd)
    0x21350x1e81: MSTORE v1e81212c, v1e812133(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21360x1e81: v1e812136(0x4) = CONST 
    0x21380x1e81: v1e812138 = ADD v1e812136(0x4), v1e81212c
    0x213b0x1e81: v1e81213b(0x20) = CONST 
    0x213d0x1e81: v1e81213d = ADD v1e81213b(0x20), v1e812138
    0x21400x1e81: v1e812140(0x20) = SUB v1e81213d, v1e812138
    0x21420x1e81: MSTORE v1e812138, v1e812140(0x20)
    0x21460x1e81: v1e812146(0x1a) = MLOAD v1e8c
    0x21480x1e81: MSTORE v1e81213d, v1e812146(0x1a)
    0x21490x1e81: v1e812149(0x20) = CONST 
    0x214b0x1e81: v1e81214b = ADD v1e812149(0x20), v1e81213d
    0x214f0x1e81: v1e81214f(0x1a) = MLOAD v1e8c
    0x21510x1e81: v1e812151(0x20) = CONST 
    0x21530x1e81: v1e812153 = ADD v1e812151(0x20), v1e8c
    0x21580x1e81: v1e812158(0x0) = CONST 

    Begin block 0x215a0x1e81
    prev=[0x212a0x1e81, 0x21640x1e81], succ=[0x21740x1e81, 0x21640x1e81]
    =================================
    0x215a0x1e81_0x0: v215a1e81_0 = PHI v1e81216e, v1e812158(0x0)
    0x215d0x1e81: v1e81215d = LT v215a1e81_0, v1e81214f(0x1a)
    0x215e0x1e81: v1e81215e = ISZERO v1e81215d
    0x215f0x1e81: v1e81215f(0x2174) = CONST 
    0x21630x1e81: JUMPI v1e81215f(0x2174), v1e81215e

    Begin block 0x21740x1e81
    prev=[0x215a0x1e81], succ=[0x21a20x1e81, 0x21890x1e81]
    =================================
    0x217d0x1e81: v1e81217d = ADD v1e81214f(0x1a), v1e81214b
    0x217f0x1e81: v1e81217f(0x1f) = CONST 
    0x21810x1e81: v1e812181(0x1a) = AND v1e81217f(0x1f), v1e81214f(0x1a)
    0x21830x1e81: v1e812183 = ISZERO v1e812181(0x1a)
    0x21840x1e81: v1e812184(0x21a2) = CONST 
    0x21880x1e81: JUMPI v1e812184(0x21a2), v1e812183

    Begin block 0x21a20x1e81
    prev=[0x21740x1e81, 0x21890x1e81], succ=[]
    =================================
    0x21a20x1e81_0x1: v21a21e81_1 = PHI v1e81219f, v1e81217d
    0x21a80x1e81: v1e8121a8(0x40) = CONST 
    0x21aa0x1e81: v1e8121aa = MLOAD v1e8121a8(0x40)
    0x21ad0x1e81: v1e8121ad = SUB v21a21e81_1, v1e8121aa
    0x21af0x1e81: REVERT v1e8121aa, v1e8121ad

    Begin block 0x21890x1e81
    prev=[0x21740x1e81], succ=[0x21a20x1e81]
    =================================
    0x218b0x1e81: v1e81218b = SUB v1e81217d, v1e812181(0x1a)
    0x218d0x1e81: v1e81218d = MLOAD v1e81218b
    0x218e0x1e81: v1e81218e(0x1) = CONST 
    0x21910x1e81: v1e812191(0x20) = CONST 
    0x21930x1e81: v1e812193(0x6) = SUB v1e812191(0x20), v1e812181(0x1a)
    0x21940x1e81: v1e812194(0x100) = CONST 
    0x21970x1e81: v1e812197(0x1000000000000) = EXP v1e812194(0x100), v1e812193(0x6)
    0x21980x1e81: v1e812198(0xffffffffffff) = SUB v1e812197(0x1000000000000), v1e81218e(0x1)
    0x21990x1e81: v1e812199 = NOT v1e812198(0xffffffffffff)
    0x219a0x1e81: v1e81219a = AND v1e812199, v1e81218d
    0x219c0x1e81: MSTORE v1e81218b, v1e81219a
    0x219d0x1e81: v1e81219d(0x20) = CONST 
    0x219f0x1e81: v1e81219f = ADD v1e81219d(0x20), v1e81218b

    Begin block 0x21640x1e81
    prev=[0x215a0x1e81], succ=[0x215a0x1e81]
    =================================
    0x21640x1e81_0x0: v21641e81_0 = PHI v1e81216e, v1e812158(0x0)
    0x21660x1e81: v1e812166 = ADD v21641e81_0, v1e812153
    0x21670x1e81: v1e812167 = MLOAD v1e812166
    0x216a0x1e81: v1e81216a = ADD v21641e81_0, v1e81214b
    0x216b0x1e81: MSTORE v1e81216a, v1e812167
    0x216c0x1e81: v1e81216c(0x20) = CONST 
    0x216e0x1e81: v1e81216e = ADD v1e81216c(0x20), v21641e81_0
    0x216f0x1e81: v1e81216f(0x215a) = CONST 
    0x21730x1e81: JUMP v1e81216f(0x215a)

    Begin block 0x21b00x1e81
    prev=[0x21200x1e81], succ=[0x21bc0x1e81, 0x21bd0x1e81]
    =================================
    0x21b20x1e81: v1e8121b2(0x0) = CONST 
    0x21b70x1e81: v1e8121b7(0x21bd) = CONST 
    0x21bb0x1e81: JUMPI v1e8121b7(0x21bd), v1e81arg0

    Begin block 0x21bc0x1e81
    prev=[0x21b00x1e81], succ=[]
    =================================
    0x21bc0x1e81: THROW 

    Begin block 0x21bd0x1e81
    prev=[0x21b00x1e81], succ=[0x40370x1e81]
    =================================
    0x21be0x1e81: v1e8121be = DIV v1e81arg1, v1e81arg0
    0x21c60x1e81: JUMP v1e84(0x4037)

    Begin block 0x40370x1e81
    prev=[0x21bd0x1e81], succ=[]
    =================================
    0x403d0x1e81: RETURNPRIVATE v1e81arg2, v1e8121be

}

function initialized()() public {
    Begin block 0x1ec
    prev=[], succ=[0x1f5, 0x1f9]
    =================================
    0x1ed: v1ed = CALLVALUE 
    0x1ef: v1ef = ISZERO v1ed
    0x1f0: v1f0(0x1f9) = CONST 
    0x1f4: JUMPI v1f0(0x1f9), v1ef

    Begin block 0x1f5
    prev=[0x1ec], succ=[]
    =================================
    0x1f5: v1f5(0x0) = CONST 
    0x1f8: REVERT v1f5(0x0), v1f5(0x0)

    Begin block 0x1f9
    prev=[0x1ec], succ=[0x7aa]
    =================================
    0x1fb: v1fb(0x3980) = CONST 
    0x1ff: v1ff(0x7aa) = CONST 
    0x203: JUMP v1ff(0x7aa)

    Begin block 0x7aa
    prev=[0x1f9], succ=[0x3980]
    =================================
    0x7ab: v7ab(0x0) = CONST 
    0x7ad: v7ad = SLOAD v7ab(0x0)
    0x7ae: v7ae(0xff) = CONST 
    0x7b0: v7b0 = AND v7ae(0xff), v7ad
    0x7b2: JUMP v1fb(0x3980)

    Begin block 0x3980
    prev=[0x7aa], succ=[]
    =================================
    0x3981: v3981(0x40) = CONST 
    0x3984: v3984 = MLOAD v3981(0x40)
    0x3986: v3986 = ISZERO v7b0
    0x3987: v3987 = ISZERO v3986
    0x3989: MSTORE v3984, v3987
    0x398a: v398a = MLOAD v3981(0x40)
    0x398e: v398e(0x0) = SUB v3984, v398a
    0x398f: v398f(0x20) = CONST 
    0x3991: v3991(0x20) = ADD v398f(0x20), v398e(0x0)
    0x3993: RETURN v398a, v3991(0x20)

}

function 0x1ec5(0x1ec5arg0x0, 0x1ec5arg0x1, 0x1ec5arg0x2) private {
    Begin block 0x1ec5
    prev=[], succ=[0x21c7]
    =================================
    0x1ec6: v1ec6(0x0) = CONST 
    0x1ec8: v1ec8(0x405d) = CONST 
    0x1ece: v1ece(0x40) = CONST 
    0x1ed0: v1ed0 = MLOAD v1ece(0x40)
    0x1ed2: v1ed2(0x40) = CONST 
    0x1ed4: v1ed4 = ADD v1ed2(0x40), v1ed0
    0x1ed5: v1ed5(0x40) = CONST 
    0x1ed7: MSTORE v1ed5(0x40), v1ed4
    0x1ed9: v1ed9(0x1e) = CONST 
    0x1edc: MSTORE v1ed0, v1ed9(0x1e)
    0x1edd: v1edd(0x20) = CONST 
    0x1edf: v1edf = ADD v1edd(0x20), v1ed0
    0x1ee0: v1ee0(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x1f02: MSTORE v1edf, v1ee0(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x1f04: v1f04(0x21c7) = CONST 
    0x1f08: JUMP v1f04(0x21c7)

    Begin block 0x21c7
    prev=[0x1ec5], succ=[0x21d4, 0x221c]
    =================================
    0x21c8: v21c8(0x0) = CONST 
    0x21cd: v21cd = GT v1ec5arg0, v1ec5arg1
    0x21ce: v21ce = ISZERO v21cd
    0x21cf: v21cf(0x221c) = CONST 
    0x21d3: JUMPI v21cf(0x221c), v21ce

    Begin block 0x21d4
    prev=[0x21c7], succ=[0x220c, 0x21740x1ec5]
    =================================
    0x21d4: v21d4(0x40) = CONST 
    0x21d6: v21d6 = MLOAD v21d4(0x40)
    0x21d7: v21d7(0x461bcd) = CONST 
    0x21db: v21db(0xe5) = CONST 
    0x21dd: v21dd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v21db(0xe5), v21d7(0x461bcd)
    0x21df: MSTORE v21d6, v21dd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21e0: v21e0(0x20) = CONST 
    0x21e2: v21e2(0x4) = CONST 
    0x21e5: v21e5 = ADD v21d6, v21e2(0x4)
    0x21e8: MSTORE v21e5, v21e0(0x20)
    0x21ea: v21ea(0x1e) = MLOAD v1ed0
    0x21eb: v21eb(0x24) = CONST 
    0x21ee: v21ee = ADD v21d6, v21eb(0x24)
    0x21ef: MSTORE v21ee, v21ea(0x1e)
    0x21f1: v21f1(0x1e) = MLOAD v1ed0
    0x21f6: v21f6(0x44) = CONST 
    0x21fa: v21fa = ADD v21d6, v21f6(0x44)
    0x21fe: v21fe = ADD v1ed0, v21e0(0x20)
    0x2203: v2203(0x0) = CONST 
    0x2206: v2206 = ISZERO v21f1(0x1e)
    0x2207: v2207(0x2174) = CONST 
    0x220b: JUMPI v2207(0x2174), v2206

    Begin block 0x220c
    prev=[0x21d4], succ=[0x215a0x1ec5]
    =================================
    0x220e: v220e = ADD v2203(0x0), v21fe
    0x220f: v220f = MLOAD v220e
    0x2212: v2212 = ADD v2203(0x0), v21fa
    0x2213: MSTORE v2212, v220f
    0x2214: v2214(0x20) = CONST 
    0x2216: v2216(0x20) = ADD v2214(0x20), v2203(0x0)
    0x2217: v2217(0x215a) = CONST 
    0x221b: JUMP v2217(0x215a)

    Begin block 0x215a0x1ec5
    prev=[0x220c, 0x21640x1ec5], succ=[0x21740x1ec5, 0x21640x1ec5]
    =================================
    0x215a0x1ec5_0x0: v215a1ec5_0 = PHI v2216(0x20), v1ec5216e
    0x215d0x1ec5: v1ec5215d = LT v215a1ec5_0, v21f1(0x1e)
    0x215e0x1ec5: v1ec5215e = ISZERO v1ec5215d
    0x215f0x1ec5: v1ec5215f(0x2174) = CONST 
    0x21630x1ec5: JUMPI v1ec5215f(0x2174), v1ec5215e

    Begin block 0x21740x1ec5
    prev=[0x21d4, 0x215a0x1ec5], succ=[0x21a20x1ec5, 0x21890x1ec5]
    =================================
    0x217d0x1ec5: v1ec5217d = ADD v21f1(0x1e), v21fa
    0x217f0x1ec5: v1ec5217f(0x1f) = CONST 
    0x21810x1ec5: v1ec52181(0x1e) = AND v1ec5217f(0x1f), v21f1(0x1e)
    0x21830x1ec5: v1ec52183 = ISZERO v1ec52181(0x1e)
    0x21840x1ec5: v1ec52184(0x21a2) = CONST 
    0x21880x1ec5: JUMPI v1ec52184(0x21a2), v1ec52183

    Begin block 0x21a20x1ec5
    prev=[0x21740x1ec5, 0x21890x1ec5], succ=[]
    =================================
    0x21a20x1ec5_0x1: v21a21ec5_1 = PHI v1ec5219f, v1ec5217d
    0x21a80x1ec5: v1ec521a8(0x40) = CONST 
    0x21aa0x1ec5: v1ec521aa = MLOAD v1ec521a8(0x40)
    0x21ad0x1ec5: v1ec521ad = SUB v21a21ec5_1, v1ec521aa
    0x21af0x1ec5: REVERT v1ec521aa, v1ec521ad

    Begin block 0x21890x1ec5
    prev=[0x21740x1ec5], succ=[0x21a20x1ec5]
    =================================
    0x218b0x1ec5: v1ec5218b = SUB v1ec5217d, v1ec52181(0x1e)
    0x218d0x1ec5: v1ec5218d = MLOAD v1ec5218b
    0x218e0x1ec5: v1ec5218e(0x1) = CONST 
    0x21910x1ec5: v1ec52191(0x20) = CONST 
    0x21930x1ec5: v1ec52193(0x2) = SUB v1ec52191(0x20), v1ec52181(0x1e)
    0x21940x1ec5: v1ec52194(0x100) = CONST 
    0x21970x1ec5: v1ec52197(0x10000) = EXP v1ec52194(0x100), v1ec52193(0x2)
    0x21980x1ec5: v1ec52198(0xffff) = SUB v1ec52197(0x10000), v1ec5218e(0x1)
    0x21990x1ec5: v1ec52199 = NOT v1ec52198(0xffff)
    0x219a0x1ec5: v1ec5219a = AND v1ec52199, v1ec5218d
    0x219c0x1ec5: MSTORE v1ec5218b, v1ec5219a
    0x219d0x1ec5: v1ec5219d(0x20) = CONST 
    0x219f0x1ec5: v1ec5219f = ADD v1ec5219d(0x20), v1ec5218b

    Begin block 0x21640x1ec5
    prev=[0x215a0x1ec5], succ=[0x215a0x1ec5]
    =================================
    0x21640x1ec5_0x0: v21641ec5_0 = PHI v2216(0x20), v1ec5216e
    0x21660x1ec5: v1ec52166 = ADD v21641ec5_0, v21fe
    0x21670x1ec5: v1ec52167 = MLOAD v1ec52166
    0x216a0x1ec5: v1ec5216a = ADD v21641ec5_0, v21fa
    0x216b0x1ec5: MSTORE v1ec5216a, v1ec52167
    0x216c0x1ec5: v1ec5216c(0x20) = CONST 
    0x216e0x1ec5: v1ec5216e = ADD v1ec5216c(0x20), v21641ec5_0
    0x216f0x1ec5: v1ec5216f(0x215a) = CONST 
    0x21730x1ec5: JUMP v1ec5216f(0x215a)

    Begin block 0x221c
    prev=[0x21c7], succ=[0x405d]
    =================================
    0x2221: v2221 = SUB v1ec5arg1, v1ec5arg0
    0x2223: JUMP v1ec8(0x405d)

    Begin block 0x405d
    prev=[0x221c], succ=[]
    =================================
    0x4063: RETURNPRIVATE v1ec5arg2, v2221

}

function nyanManager()() public {
    Begin block 0x218
    prev=[], succ=[0x221, 0x225]
    =================================
    0x219: v219 = CALLVALUE 
    0x21b: v21b = ISZERO v219
    0x21c: v21c(0x225) = CONST 
    0x220: JUMPI v21c(0x225), v21b

    Begin block 0x221
    prev=[0x218], succ=[]
    =================================
    0x221: v221(0x0) = CONST 
    0x224: REVERT v221(0x0), v221(0x0)

    Begin block 0x225
    prev=[0x218], succ=[0x7b3]
    =================================
    0x227: v227(0x39b3) = CONST 
    0x22b: v22b(0x7b3) = CONST 
    0x22f: JUMP v22b(0x7b3)

    Begin block 0x7b3
    prev=[0x225], succ=[0x39b3]
    =================================
    0x7b4: v7b4(0xa) = CONST 
    0x7b6: v7b6 = SLOAD v7b4(0xa)
    0x7b7: v7b7(0x1) = CONST 
    0x7b9: v7b9(0x1) = CONST 
    0x7bb: v7bb(0xa0) = CONST 
    0x7bd: v7bd(0x10000000000000000000000000000000000000000) = SHL v7bb(0xa0), v7b9(0x1)
    0x7be: v7be(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7bd(0x10000000000000000000000000000000000000000), v7b7(0x1)
    0x7bf: v7bf = AND v7be(0xffffffffffffffffffffffffffffffffffffffff), v7b6
    0x7c1: JUMP v227(0x39b3)

    Begin block 0x39b3
    prev=[0x7b3], succ=[]
    =================================
    0x39b4: v39b4(0x40) = CONST 
    0x39b7: v39b7 = MLOAD v39b4(0x40)
    0x39b8: v39b8(0x1) = CONST 
    0x39ba: v39ba(0x1) = CONST 
    0x39bc: v39bc(0xa0) = CONST 
    0x39be: v39be(0x10000000000000000000000000000000000000000) = SHL v39bc(0xa0), v39ba(0x1)
    0x39bf: v39bf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39be(0x10000000000000000000000000000000000000000), v39b8(0x1)
    0x39c2: v39c2 = AND v7bf, v39bf(0xffffffffffffffffffffffffffffffffffffffff)
    0x39c4: MSTORE v39b7, v39c2
    0x39c5: v39c5 = MLOAD v39b4(0x40)
    0x39c9: v39c9(0x0) = SUB v39b7, v39c5
    0x39ca: v39ca(0x20) = CONST 
    0x39cc: v39cc(0x20) = ADD v39ca(0x20), v39c9(0x0)
    0x39ce: RETURN v39c5, v39cc(0x20)

}

function nyanVoting()() public {
    Begin block 0x230
    prev=[], succ=[0x239, 0x23d]
    =================================
    0x231: v231 = CALLVALUE 
    0x233: v233 = ISZERO v231
    0x234: v234(0x23d) = CONST 
    0x238: JUMPI v234(0x23d), v233

    Begin block 0x239
    prev=[0x230], succ=[]
    =================================
    0x239: v239(0x0) = CONST 
    0x23c: REVERT v239(0x0), v239(0x0)

    Begin block 0x23d
    prev=[0x230], succ=[0x7c2]
    =================================
    0x23f: v23f(0x39ee) = CONST 
    0x243: v243(0x7c2) = CONST 
    0x247: JUMP v243(0x7c2)

    Begin block 0x7c2
    prev=[0x23d], succ=[0x39ee]
    =================================
    0x7c3: v7c3(0x1) = CONST 
    0x7c5: v7c5 = SLOAD v7c3(0x1)
    0x7c6: v7c6(0x1) = CONST 
    0x7c8: v7c8(0x1) = CONST 
    0x7ca: v7ca(0xa0) = CONST 
    0x7cc: v7cc(0x10000000000000000000000000000000000000000) = SHL v7ca(0xa0), v7c8(0x1)
    0x7cd: v7cd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7cc(0x10000000000000000000000000000000000000000), v7c6(0x1)
    0x7ce: v7ce = AND v7cd(0xffffffffffffffffffffffffffffffffffffffff), v7c5
    0x7d0: JUMP v23f(0x39ee)

    Begin block 0x39ee
    prev=[0x7c2], succ=[]
    =================================
    0x39ef: v39ef(0x40) = CONST 
    0x39f2: v39f2 = MLOAD v39ef(0x40)
    0x39f3: v39f3(0x1) = CONST 
    0x39f5: v39f5(0x1) = CONST 
    0x39f7: v39f7(0xa0) = CONST 
    0x39f9: v39f9(0x10000000000000000000000000000000000000000) = SHL v39f7(0xa0), v39f5(0x1)
    0x39fa: v39fa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v39f9(0x10000000000000000000000000000000000000000), v39f3(0x1)
    0x39fd: v39fd = AND v7ce, v39fa(0xffffffffffffffffffffffffffffffffffffffff)
    0x39ff: MSTORE v39f2, v39fd
    0x3a00: v3a00 = MLOAD v39ef(0x40)
    0x3a04: v3a04(0x0) = SUB v39f2, v3a00
    0x3a05: v3a05(0x20) = CONST 
    0x3a07: v3a07(0x20) = ADD v3a05(0x20), v3a04(0x0)
    0x3a09: RETURN v3a00, v3a07(0x20)

}

function rewardsContract()() public {
    Begin block 0x248
    prev=[], succ=[0x251, 0x255]
    =================================
    0x249: v249 = CALLVALUE 
    0x24b: v24b = ISZERO v249
    0x24c: v24c(0x255) = CONST 
    0x250: JUMPI v24c(0x255), v24b

    Begin block 0x251
    prev=[0x248], succ=[]
    =================================
    0x251: v251(0x0) = CONST 
    0x254: REVERT v251(0x0), v251(0x0)

    Begin block 0x255
    prev=[0x248], succ=[0x7d1]
    =================================
    0x257: v257(0x3a29) = CONST 
    0x25b: v25b(0x7d1) = CONST 
    0x25f: JUMP v25b(0x7d1)

    Begin block 0x7d1
    prev=[0x255], succ=[0x3a29]
    =================================
    0x7d2: v7d2(0x8) = CONST 
    0x7d4: v7d4 = SLOAD v7d2(0x8)
    0x7d5: v7d5(0x1) = CONST 
    0x7d7: v7d7(0x1) = CONST 
    0x7d9: v7d9(0xa0) = CONST 
    0x7db: v7db(0x10000000000000000000000000000000000000000) = SHL v7d9(0xa0), v7d7(0x1)
    0x7dc: v7dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7db(0x10000000000000000000000000000000000000000), v7d5(0x1)
    0x7dd: v7dd = AND v7dc(0xffffffffffffffffffffffffffffffffffffffff), v7d4
    0x7df: JUMP v257(0x3a29)

    Begin block 0x3a29
    prev=[0x7d1], succ=[]
    =================================
    0x3a2a: v3a2a(0x40) = CONST 
    0x3a2d: v3a2d = MLOAD v3a2a(0x40)
    0x3a2e: v3a2e(0x1) = CONST 
    0x3a30: v3a30(0x1) = CONST 
    0x3a32: v3a32(0xa0) = CONST 
    0x3a34: v3a34(0x10000000000000000000000000000000000000000) = SHL v3a32(0xa0), v3a30(0x1)
    0x3a35: v3a35(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3a34(0x10000000000000000000000000000000000000000), v3a2e(0x1)
    0x3a38: v3a38 = AND v7dd, v3a35(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a3a: MSTORE v3a2d, v3a38
    0x3a3b: v3a3b = MLOAD v3a2a(0x40)
    0x3a3f: v3a3f(0x0) = SUB v3a2d, v3a3b
    0x3a40: v3a40(0x20) = CONST 
    0x3a42: v3a42(0x20) = ADD v3a40(0x20), v3a3f(0x0)
    0x3a44: RETURN v3a3b, v3a42(0x20)

}

function tokensForETH(address,address,uint256)() public {
    Begin block 0x260
    prev=[], succ=[0x269, 0x26d]
    =================================
    0x261: v261 = CALLVALUE 
    0x263: v263 = ISZERO v261
    0x264: v264(0x26d) = CONST 
    0x268: JUMPI v264(0x26d), v263

    Begin block 0x269
    prev=[0x260], succ=[]
    =================================
    0x269: v269(0x0) = CONST 
    0x26c: REVERT v269(0x0), v269(0x0)

    Begin block 0x26d
    prev=[0x260], succ=[0x282, 0x286]
    =================================
    0x26f: v26f(0x3a64) = CONST 
    0x273: v273(0x4) = CONST 
    0x276: v276 = CALLDATASIZE 
    0x277: v277 = SUB v276, v273(0x4)
    0x278: v278(0x60) = CONST 
    0x27b: v27b = LT v277, v278(0x60)
    0x27c: v27c = ISZERO v27b
    0x27d: v27d(0x286) = CONST 
    0x281: JUMPI v27d(0x286), v27c

    Begin block 0x282
    prev=[0x26d], succ=[]
    =================================
    0x282: v282(0x0) = CONST 
    0x285: REVERT v282(0x0), v282(0x0)

    Begin block 0x286
    prev=[0x26d], succ=[0x7e0]
    =================================
    0x288: v288(0x1) = CONST 
    0x28a: v28a(0x1) = CONST 
    0x28c: v28c(0xa0) = CONST 
    0x28e: v28e(0x10000000000000000000000000000000000000000) = SHL v28c(0xa0), v28a(0x1)
    0x28f: v28f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v28e(0x10000000000000000000000000000000000000000), v288(0x1)
    0x291: v291 = CALLDATALOAD v273(0x4)
    0x293: v293 = AND v28f(0xffffffffffffffffffffffffffffffffffffffff), v291
    0x295: v295(0x20) = CONST 
    0x298: v298(0x24) = ADD v273(0x4), v295(0x20)
    0x299: v299 = CALLDATALOAD v298(0x24)
    0x29c: v29c = AND v28f(0xffffffffffffffffffffffffffffffffffffffff), v299
    0x29e: v29e(0x40) = CONST 
    0x2a0: v2a0(0x44) = ADD v29e(0x40), v273(0x4)
    0x2a1: v2a1 = CALLDATALOAD v2a0(0x44)
    0x2a2: v2a2(0x7e0) = CONST 
    0x2a6: JUMP v2a2(0x7e0)

    Begin block 0x7e0
    prev=[0x286], succ=[0x7f1, 0x828]
    =================================
    0x7e1: v7e1(0x0) = CONST 
    0x7e3: v7e3 = SLOAD v7e1(0x0)
    0x7e4: v7e4(0xff) = CONST 
    0x7e6: v7e6 = AND v7e4(0xff), v7e3
    0x7e7: v7e7 = ISZERO v7e6
    0x7e8: v7e8 = ISZERO v7e7
    0x7e9: v7e9(0x1) = CONST 
    0x7eb: v7eb = EQ v7e9(0x1), v7e8
    0x7ec: v7ec(0x828) = CONST 
    0x7f0: JUMPI v7ec(0x828), v7eb

    Begin block 0x7f1
    prev=[0x7e0], succ=[]
    =================================
    0x7f1: v7f1(0x40) = CONST 
    0x7f3: v7f3 = MLOAD v7f1(0x40)
    0x7f4: v7f4(0x461bcd) = CONST 
    0x7f8: v7f8(0xe5) = CONST 
    0x7fa: v7fa(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7f8(0xe5), v7f4(0x461bcd)
    0x7fc: MSTORE v7f3, v7fa(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7fd: v7fd(0x4) = CONST 
    0x7ff: v7ff = ADD v7fd(0x4), v7f3
    0x802: v802(0x20) = CONST 
    0x804: v804 = ADD v802(0x20), v7ff
    0x807: v807(0x20) = SUB v804, v7ff
    0x809: MSTORE v7ff, v807(0x20)
    0x80a: v80a(0x32) = CONST 
    0x80d: MSTORE v804, v80a(0x32)
    0x80e: v80e(0x20) = CONST 
    0x810: v810 = ADD v80e(0x20), v804
    0x812: v812(0x37d5) = CONST 
    0x816: v816(0x32) = CONST 
    0x819: CODECOPY v810, v812(0x37d5), v816(0x32)
    0x81a: v81a(0x40) = CONST 
    0x81c: v81c = ADD v81a(0x40), v810
    0x820: v820(0x40) = CONST 
    0x822: v822 = MLOAD v820(0x40)
    0x825: v825(0x84) = SUB v81c, v822
    0x827: REVERT v822, v825(0x84)

    Begin block 0x828
    prev=[0x7e0], succ=[0x851, 0x855]
    =================================
    0x829: v829(0x1) = CONST 
    0x82b: v82b(0x1) = CONST 
    0x82d: v82d(0xa0) = CONST 
    0x82f: v82f(0x10000000000000000000000000000000000000000) = SHL v82d(0xa0), v82b(0x1)
    0x830: v830(0xffffffffffffffffffffffffffffffffffffffff) = SUB v82f(0x10000000000000000000000000000000000000000), v829(0x1)
    0x833: v833 = AND v830(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x834: v834(0x0) = CONST 
    0x838: MSTORE v834(0x0), v833
    0x839: v839(0x3) = CONST 
    0x83b: v83b(0x20) = CONST 
    0x83d: MSTORE v83b(0x20), v839(0x3)
    0x83e: v83e(0x40) = CONST 
    0x841: v841 = SHA3 v834(0x0), v83e(0x40)
    0x842: v842(0x9) = CONST 
    0x844: v844 = ADD v842(0x9), v841
    0x845: v845 = SLOAD v844
    0x847: v847 = AND v830(0xffffffffffffffffffffffffffffffffffffffff), v845
    0x84a: v84a = AND v29c, v830(0xffffffffffffffffffffffffffffffffffffffff)
    0x84b: v84b = EQ v84a, v847
    0x84c: v84c(0x855) = CONST 
    0x850: JUMPI v84c(0x855), v84b

    Begin block 0x851
    prev=[0x828], succ=[]
    =================================
    0x851: v851(0x0) = CONST 
    0x854: REVERT v851(0x0), v851(0x0)

    Begin block 0x855
    prev=[0x828], succ=[0x1dc1B0x855]
    =================================
    0x856: v856(0x86c) = CONST 
    0x85a: v85a(0x1) = CONST 
    0x85c: v85c(0x1) = CONST 
    0x85e: v85e(0xa0) = CONST 
    0x860: v860(0x10000000000000000000000000000000000000000) = SHL v85e(0xa0), v85c(0x1)
    0x861: v861(0xffffffffffffffffffffffffffffffffffffffff) = SUB v860(0x10000000000000000000000000000000000000000), v85a(0x1)
    0x863: v863 = AND v29c, v861(0xffffffffffffffffffffffffffffffffffffffff)
    0x864: v864 = CALLER 
    0x865: v865 = ADDRESS 
    0x867: v867(0x1dc1) = CONST 
    0x86b: JUMP v867(0x1dc1), v2a1, v865, v864, v863, v856(0x86c)

    Begin block 0x1dc1B0x855
    prev=[0x855], succ=[0x2064B0x1dc1B0x855]
    =================================
    0x1dc2S0x855: v1dc2V855(0x40) = CONST 
    0x1dc5S0x855: v1dc5V855 = MLOAD v1dc2V855(0x40)
    0x1dc6S0x855: v1dc6V855(0x1) = CONST 
    0x1dc8S0x855: v1dc8V855(0x1) = CONST 
    0x1dcaS0x855: v1dcaV855(0xa0) = CONST 
    0x1dccS0x855: v1dccV855(0x10000000000000000000000000000000000000000) = SHL v1dcaV855(0xa0), v1dc8V855(0x1)
    0x1dcdS0x855: v1dcdV855(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1dccV855(0x10000000000000000000000000000000000000000), v1dc6V855(0x1)
    0x1dd0S0x855: v1dd0V855 = AND v864, v1dcdV855(0xffffffffffffffffffffffffffffffffffffffff)
    0x1dd1S0x855: v1dd1V855(0x24) = CONST 
    0x1dd4S0x855: v1dd4V855 = ADD v1dc5V855, v1dd1V855(0x24)
    0x1dd5S0x855: MSTORE v1dd4V855, v1dd0V855
    0x1dd7S0x855: v1dd7V855 = AND v865, v1dcdV855(0xffffffffffffffffffffffffffffffffffffffff)
    0x1dd8S0x855: v1dd8V855(0x44) = CONST 
    0x1ddbS0x855: v1ddbV855 = ADD v1dc5V855, v1dd8V855(0x44)
    0x1ddcS0x855: MSTORE v1ddbV855, v1dd7V855
    0x1dddS0x855: v1dddV855(0x64) = CONST 
    0x1de1S0x855: v1de1V855 = ADD v1dc5V855, v1dddV855(0x64)
    0x1de4S0x855: MSTORE v1de1V855, v2a1
    0x1de6S0x855: v1de6V855 = MLOAD v1dc2V855(0x40)
    0x1de9S0x855: v1de9V855(0x0) = SUB v1dc5V855, v1de6V855
    0x1decS0x855: v1decV855(0x64) = ADD v1dddV855(0x64), v1de9V855(0x0)
    0x1deeS0x855: MSTORE v1de6V855, v1decV855(0x64)
    0x1defS0x855: v1defV855(0x84) = CONST 
    0x1df3S0x855: v1df3V855 = ADD v1dc5V855, v1defV855(0x84)
    0x1df6S0x855: MSTORE v1dc2V855(0x40), v1df3V855
    0x1df7S0x855: v1df7V855(0x20) = CONST 
    0x1dfaS0x855: v1dfaV855 = ADD v1de6V855, v1df7V855(0x20)
    0x1dfcS0x855: v1dfcV855 = MLOAD v1dfaV855
    0x1dfdS0x855: v1dfdV855(0x1) = CONST 
    0x1dffS0x855: v1dffV855(0x1) = CONST 
    0x1e01S0x855: v1e01V855(0xe0) = CONST 
    0x1e03S0x855: v1e03V855(0x100000000000000000000000000000000000000000000000000000000) = SHL v1e01V855(0xe0), v1dffV855(0x1)
    0x1e04S0x855: v1e04V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1e03V855(0x100000000000000000000000000000000000000000000000000000000), v1dfdV855(0x1)
    0x1e05S0x855: v1e05V855 = AND v1e04V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1dfcV855
    0x1e06S0x855: v1e06V855(0x23b872dd) = CONST 
    0x1e0bS0x855: v1e0bV855(0xe0) = CONST 
    0x1e0dS0x855: v1e0dV855(0x23b872dd00000000000000000000000000000000000000000000000000000000) = SHL v1e0bV855(0xe0), v1e06V855(0x23b872dd)
    0x1e0eS0x855: v1e0eV855 = OR v1e0dV855(0x23b872dd00000000000000000000000000000000000000000000000000000000), v1e05V855
    0x1e10S0x855: MSTORE v1dfaV855, v1e0eV855
    0x1e11S0x855: v1e11V855(0x1e1d) = CONST 
    0x1e18S0x855: v1e18V855(0x2064) = CONST 
    0x1e1cS0x855: JUMP v1e18V855(0x2064), v1de6V855, v863, v1e11V855(0x1e1d)

    Begin block 0x2064B0x1dc1B0x855
    prev=[0x1dc1B0x855], succ=[0x2224B0x2064B0x1dc1B0x855]
    =================================
    0x2065S0x1dc1S0x855: v2065V1dc1V855(0x60) = CONST 
    0x2067S0x1dc1S0x855: v2067V1dc1V855(0x20bb) = CONST 
    0x206cS0x1dc1S0x855: v206cV1dc1V855(0x40) = CONST 
    0x206eS0x1dc1S0x855: v206eV1dc1V855 = MLOAD v206cV1dc1V855(0x40)
    0x2070S0x1dc1S0x855: v2070V1dc1V855(0x40) = CONST 
    0x2072S0x1dc1S0x855: v2072V1dc1V855 = ADD v2070V1dc1V855(0x40), v206eV1dc1V855
    0x2073S0x1dc1S0x855: v2073V1dc1V855(0x40) = CONST 
    0x2075S0x1dc1S0x855: MSTORE v2073V1dc1V855(0x40), v2072V1dc1V855
    0x2077S0x1dc1S0x855: v2077V1dc1V855(0x20) = CONST 
    0x207aS0x1dc1S0x855: MSTORE v206eV1dc1V855, v2077V1dc1V855(0x20)
    0x207bS0x1dc1S0x855: v207bV1dc1V855(0x20) = CONST 
    0x207dS0x1dc1S0x855: v207dV1dc1V855 = ADD v207bV1dc1V855(0x20), v206eV1dc1V855
    0x207eS0x1dc1S0x855: v207eV1dc1V855(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564) = CONST 
    0x20a0S0x1dc1S0x855: MSTORE v207dV1dc1V855, v207eV1dc1V855(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564)
    0x20a3S0x1dc1S0x855: v20a3V1dc1V855(0x1) = CONST 
    0x20a5S0x1dc1S0x855: v20a5V1dc1V855(0x1) = CONST 
    0x20a7S0x1dc1S0x855: v20a7V1dc1V855(0xa0) = CONST 
    0x20a9S0x1dc1S0x855: v20a9V1dc1V855(0x10000000000000000000000000000000000000000) = SHL v20a7V1dc1V855(0xa0), v20a5V1dc1V855(0x1)
    0x20aaS0x1dc1S0x855: v20aaV1dc1V855(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20a9V1dc1V855(0x10000000000000000000000000000000000000000), v20a3V1dc1V855(0x1)
    0x20abS0x1dc1S0x855: v20abV1dc1V855 = AND v20aaV1dc1V855(0xffffffffffffffffffffffffffffffffffffffff), v863
    0x20acS0x1dc1S0x855: v20acV1dc1V855(0x2224) = CONST 
    0x20b4S0x1dc1S0x855: v20b4V1dc1V855(0xffffffff) = CONST 
    0x20b9S0x1dc1S0x855: v20b9V1dc1V855(0x2224) = AND v20b4V1dc1V855(0xffffffff), v20acV1dc1V855(0x2224)
    0x20baS0x1dc1S0x855: JUMP v20b9V1dc1V855(0x2224)

    Begin block 0x2224B0x2064B0x1dc1B0x855
    prev=[0x2064B0x1dc1B0x855], succ=[0x2354B0x2064B0x1dc1B0x855]
    =================================
    0x2225S0x2064S0x1dc1S0x855: v2225V2064V1dc1V855(0x60) = CONST 
    0x2227S0x2064S0x1dc1S0x855: v2227V2064V1dc1V855(0x40f1) = CONST 
    0x222dS0x2064S0x1dc1S0x855: v222dV2064V1dc1V855(0x0) = CONST 
    0x2231S0x2064S0x1dc1S0x855: v2231V2064V1dc1V855(0x223b) = CONST 
    0x2236S0x2064S0x1dc1S0x855: v2236V2064V1dc1V855(0x2354) = CONST 
    0x223aS0x2064S0x1dc1S0x855: JUMP v2236V2064V1dc1V855(0x2354)

    Begin block 0x2354B0x2064B0x1dc1B0x855
    prev=[0x2224B0x2064B0x1dc1B0x855], succ=[0x223bB0x2064B0x1dc1B0x855]
    =================================
    0x2355S0x2064S0x1dc1S0x855: v2355V2064V1dc1V855 = EXTCODESIZE v20abV1dc1V855
    0x2356S0x2064S0x1dc1S0x855: v2356V2064V1dc1V855 = ISZERO v2355V2064V1dc1V855
    0x2357S0x2064S0x1dc1S0x855: v2357V2064V1dc1V855 = ISZERO v2356V2064V1dc1V855
    0x2359S0x2064S0x1dc1S0x855: JUMP v2231V2064V1dc1V855(0x223b)

    Begin block 0x223bB0x2064B0x1dc1B0x855
    prev=[0x2354B0x2064B0x1dc1B0x855], succ=[0x2241B0x2064B0x1dc1B0x855, 0x228dB0x2064B0x1dc1B0x855]
    =================================
    0x223cS0x2064S0x1dc1S0x855: v223cV2064V1dc1V855(0x228d) = CONST 
    0x2240S0x2064S0x1dc1S0x855: JUMPI v223cV2064V1dc1V855(0x228d), v2357V2064V1dc1V855

    Begin block 0x2241B0x2064B0x1dc1B0x855
    prev=[0x223bB0x2064B0x1dc1B0x855], succ=[]
    =================================
    0x2241S0x2064S0x1dc1S0x855: v2241V2064V1dc1V855(0x40) = CONST 
    0x2244S0x2064S0x1dc1S0x855: v2244V2064V1dc1V855 = MLOAD v2241V2064V1dc1V855(0x40)
    0x2245S0x2064S0x1dc1S0x855: v2245V2064V1dc1V855(0x461bcd) = CONST 
    0x2249S0x2064S0x1dc1S0x855: v2249V2064V1dc1V855(0xe5) = CONST 
    0x224bS0x2064S0x1dc1S0x855: v224bV2064V1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2249V2064V1dc1V855(0xe5), v2245V2064V1dc1V855(0x461bcd)
    0x224dS0x2064S0x1dc1S0x855: MSTORE v2244V2064V1dc1V855, v224bV2064V1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x224eS0x2064S0x1dc1S0x855: v224eV2064V1dc1V855(0x20) = CONST 
    0x2250S0x2064S0x1dc1S0x855: v2250V2064V1dc1V855(0x4) = CONST 
    0x2253S0x2064S0x1dc1S0x855: v2253V2064V1dc1V855 = ADD v2244V2064V1dc1V855, v2250V2064V1dc1V855(0x4)
    0x2254S0x2064S0x1dc1S0x855: MSTORE v2253V2064V1dc1V855, v224eV2064V1dc1V855(0x20)
    0x2255S0x2064S0x1dc1S0x855: v2255V2064V1dc1V855(0x1d) = CONST 
    0x2257S0x2064S0x1dc1S0x855: v2257V2064V1dc1V855(0x24) = CONST 
    0x225aS0x2064S0x1dc1S0x855: v225aV2064V1dc1V855 = ADD v2244V2064V1dc1V855, v2257V2064V1dc1V855(0x24)
    0x225bS0x2064S0x1dc1S0x855: MSTORE v225aV2064V1dc1V855, v2255V2064V1dc1V855(0x1d)
    0x225cS0x2064S0x1dc1S0x855: v225cV2064V1dc1V855(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000) = CONST 
    0x227dS0x2064S0x1dc1S0x855: v227dV2064V1dc1V855(0x44) = CONST 
    0x2280S0x2064S0x1dc1S0x855: v2280V2064V1dc1V855 = ADD v2244V2064V1dc1V855, v227dV2064V1dc1V855(0x44)
    0x2281S0x2064S0x1dc1S0x855: MSTORE v2280V2064V1dc1V855, v225cV2064V1dc1V855(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000)
    0x2283S0x2064S0x1dc1S0x855: v2283V2064V1dc1V855 = MLOAD v2241V2064V1dc1V855(0x40)
    0x2287S0x2064S0x1dc1S0x855: v2287V2064V1dc1V855(0x0) = SUB v2244V2064V1dc1V855, v2283V2064V1dc1V855
    0x2288S0x2064S0x1dc1S0x855: v2288V2064V1dc1V855(0x64) = CONST 
    0x228aS0x2064S0x1dc1S0x855: v228aV2064V1dc1V855(0x64) = ADD v2288V2064V1dc1V855(0x64), v2287V2064V1dc1V855(0x0)
    0x228cS0x2064S0x1dc1S0x855: REVERT v2283V2064V1dc1V855, v228aV2064V1dc1V855(0x64)

    Begin block 0x228dB0x2064B0x1dc1B0x855
    prev=[0x223bB0x2064B0x1dc1B0x855], succ=[0x22adB0x2064B0x1dc1B0x855]
    =================================
    0x228eS0x2064S0x1dc1S0x855: v228eV2064V1dc1V855(0x0) = CONST 
    0x2290S0x2064S0x1dc1S0x855: v2290V2064V1dc1V855(0x60) = CONST 
    0x2293S0x2064S0x1dc1S0x855: v2293V2064V1dc1V855(0x1) = CONST 
    0x2295S0x2064S0x1dc1S0x855: v2295V2064V1dc1V855(0x1) = CONST 
    0x2297S0x2064S0x1dc1S0x855: v2297V2064V1dc1V855(0xa0) = CONST 
    0x2299S0x2064S0x1dc1S0x855: v2299V2064V1dc1V855(0x10000000000000000000000000000000000000000) = SHL v2297V2064V1dc1V855(0xa0), v2295V2064V1dc1V855(0x1)
    0x229aS0x2064S0x1dc1S0x855: v229aV2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2299V2064V1dc1V855(0x10000000000000000000000000000000000000000), v2293V2064V1dc1V855(0x1)
    0x229bS0x2064S0x1dc1S0x855: v229bV2064V1dc1V855 = AND v229aV2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffff), v20abV1dc1V855
    0x229eS0x2064S0x1dc1S0x855: v229eV2064V1dc1V855(0x40) = CONST 
    0x22a0S0x2064S0x1dc1S0x855: v22a0V2064V1dc1V855 = MLOAD v229eV2064V1dc1V855(0x40)
    0x22a4S0x2064S0x1dc1S0x855: v22a4V2064V1dc1V855(0x64) = MLOAD v1de6V855
    0x22a6S0x2064S0x1dc1S0x855: v22a6V2064V1dc1V855(0x20) = CONST 
    0x22a8S0x2064S0x1dc1S0x855: v22a8V2064V1dc1V855 = ADD v22a6V2064V1dc1V855(0x20), v1de6V855

    Begin block 0x22adB0x2064B0x1dc1B0x855
    prev=[0x228dB0x2064B0x1dc1B0x855, 0x22b7B0x2064B0x1dc1B0x855], succ=[0x22ceB0x2064B0x1dc1B0x855, 0x22b7B0x2064B0x1dc1B0x855]
    =================================
    0x22ad_0x2S0x2064S0x1dc1S0x855: v22ad_2V2064V1dc1V855 = PHI v22a4V2064V1dc1V855(0x64), v22c0V2064V1dc1V855
    0x22aeS0x2064S0x1dc1S0x855: v22aeV2064V1dc1V855(0x20) = CONST 
    0x22b1S0x2064S0x1dc1S0x855: v22b1V2064V1dc1V855 = LT v22ad_2V2064V1dc1V855, v22aeV2064V1dc1V855(0x20)
    0x22b2S0x2064S0x1dc1S0x855: v22b2V2064V1dc1V855(0x22ce) = CONST 
    0x22b6S0x2064S0x1dc1S0x855: JUMPI v22b2V2064V1dc1V855(0x22ce), v22b1V2064V1dc1V855

    Begin block 0x22ceB0x2064B0x1dc1B0x855
    prev=[0x22adB0x2064B0x1dc1B0x855], succ=[0x2310B0x2064B0x1dc1B0x855, 0x2332B0x2064B0x1dc1B0x855]
    =================================
    0x22ce_0x0S0x2064S0x1dc1S0x855: v22ce_0V2064V1dc1V855 = PHI v22a8V2064V1dc1V855, v22c8V2064V1dc1V855
    0x22ce_0x1S0x2064S0x1dc1S0x855: v22ce_1V2064V1dc1V855 = PHI v22a0V2064V1dc1V855, v22c6V2064V1dc1V855
    0x22ce_0x2S0x2064S0x1dc1S0x855: v22ce_2V2064V1dc1V855 = PHI v22a4V2064V1dc1V855(0x64), v22c0V2064V1dc1V855
    0x22cfS0x2064S0x1dc1S0x855: v22cfV2064V1dc1V855(0x1) = CONST 
    0x22d2S0x2064S0x1dc1S0x855: v22d2V2064V1dc1V855(0x20) = CONST 
    0x22d4S0x2064S0x1dc1S0x855: v22d4V2064V1dc1V855 = SUB v22d2V2064V1dc1V855(0x20), v22ce_2V2064V1dc1V855
    0x22d5S0x2064S0x1dc1S0x855: v22d5V2064V1dc1V855(0x100) = CONST 
    0x22d8S0x2064S0x1dc1S0x855: v22d8V2064V1dc1V855 = EXP v22d5V2064V1dc1V855(0x100), v22d4V2064V1dc1V855
    0x22d9S0x2064S0x1dc1S0x855: v22d9V2064V1dc1V855 = SUB v22d8V2064V1dc1V855, v22cfV2064V1dc1V855(0x1)
    0x22dbS0x2064S0x1dc1S0x855: v22dbV2064V1dc1V855 = NOT v22d9V2064V1dc1V855
    0x22ddS0x2064S0x1dc1S0x855: v22ddV2064V1dc1V855 = MLOAD v22ce_0V2064V1dc1V855
    0x22deS0x2064S0x1dc1S0x855: v22deV2064V1dc1V855 = AND v22ddV2064V1dc1V855, v22dbV2064V1dc1V855
    0x22e1S0x2064S0x1dc1S0x855: v22e1V2064V1dc1V855 = MLOAD v22ce_1V2064V1dc1V855
    0x22e2S0x2064S0x1dc1S0x855: v22e2V2064V1dc1V855 = AND v22e1V2064V1dc1V855, v22d9V2064V1dc1V855
    0x22e5S0x2064S0x1dc1S0x855: v22e5V2064V1dc1V855 = OR v22deV2064V1dc1V855, v22e2V2064V1dc1V855
    0x22e7S0x2064S0x1dc1S0x855: MSTORE v22ce_1V2064V1dc1V855, v22e5V2064V1dc1V855
    0x22f0S0x2064S0x1dc1S0x855: v22f0V2064V1dc1V855 = ADD v22a4V2064V1dc1V855(0x64), v22a0V2064V1dc1V855
    0x22f4S0x2064S0x1dc1S0x855: v22f4V2064V1dc1V855(0x0) = CONST 
    0x22f6S0x2064S0x1dc1S0x855: v22f6V2064V1dc1V855(0x40) = CONST 
    0x22f8S0x2064S0x1dc1S0x855: v22f8V2064V1dc1V855 = MLOAD v22f6V2064V1dc1V855(0x40)
    0x22fbS0x2064S0x1dc1S0x855: v22fbV2064V1dc1V855(0x64) = SUB v22f0V2064V1dc1V855, v22f8V2064V1dc1V855
    0x22ffS0x2064S0x1dc1S0x855: v22ffV2064V1dc1V855 = GAS 
    0x2300S0x2064S0x1dc1S0x855: v2300V2064V1dc1V855 = CALL v22ffV2064V1dc1V855, v229bV2064V1dc1V855, v222dV2064V1dc1V855(0x0), v22f8V2064V1dc1V855, v22fbV2064V1dc1V855(0x64), v22f8V2064V1dc1V855, v22f4V2064V1dc1V855(0x0)
    0x2305S0x2064S0x1dc1S0x855: v2305V2064V1dc1V855 = RETURNDATASIZE 
    0x2307S0x2064S0x1dc1S0x855: v2307V2064V1dc1V855(0x0) = CONST 
    0x230aS0x2064S0x1dc1S0x855: v230aV2064V1dc1V855 = EQ v2305V2064V1dc1V855, v2307V2064V1dc1V855(0x0)
    0x230bS0x2064S0x1dc1S0x855: v230bV2064V1dc1V855(0x2332) = CONST 
    0x230fS0x2064S0x1dc1S0x855: JUMPI v230bV2064V1dc1V855(0x2332), v230aV2064V1dc1V855

    Begin block 0x2310B0x2064B0x1dc1B0x855
    prev=[0x22ceB0x2064B0x1dc1B0x855], succ=[0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x2310S0x2064S0x1dc1S0x855: v2310V2064V1dc1V855(0x40) = CONST 
    0x2312S0x2064S0x1dc1S0x855: v2312V2064V1dc1V855 = MLOAD v2310V2064V1dc1V855(0x40)
    0x2315S0x2064S0x1dc1S0x855: v2315V2064V1dc1V855(0x1f) = CONST 
    0x2317S0x2064S0x1dc1S0x855: v2317V2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2315V2064V1dc1V855(0x1f)
    0x2318S0x2064S0x1dc1S0x855: v2318V2064V1dc1V855(0x3f) = CONST 
    0x231aS0x2064S0x1dc1S0x855: v231aV2064V1dc1V855 = RETURNDATASIZE 
    0x231bS0x2064S0x1dc1S0x855: v231bV2064V1dc1V855 = ADD v231aV2064V1dc1V855, v2318V2064V1dc1V855(0x3f)
    0x231cS0x2064S0x1dc1S0x855: v231cV2064V1dc1V855 = AND v231bV2064V1dc1V855, v2317V2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x231eS0x2064S0x1dc1S0x855: v231eV2064V1dc1V855 = ADD v2312V2064V1dc1V855, v231cV2064V1dc1V855
    0x231fS0x2064S0x1dc1S0x855: v231fV2064V1dc1V855(0x40) = CONST 
    0x2321S0x2064S0x1dc1S0x855: MSTORE v231fV2064V1dc1V855(0x40), v231eV2064V1dc1V855
    0x2322S0x2064S0x1dc1S0x855: v2322V2064V1dc1V855 = RETURNDATASIZE 
    0x2324S0x2064S0x1dc1S0x855: MSTORE v2312V2064V1dc1V855, v2322V2064V1dc1V855
    0x2325S0x2064S0x1dc1S0x855: v2325V2064V1dc1V855 = RETURNDATASIZE 
    0x2326S0x2064S0x1dc1S0x855: v2326V2064V1dc1V855(0x0) = CONST 
    0x2328S0x2064S0x1dc1S0x855: v2328V2064V1dc1V855(0x20) = CONST 
    0x232bS0x2064S0x1dc1S0x855: v232bV2064V1dc1V855 = ADD v2312V2064V1dc1V855, v2328V2064V1dc1V855(0x20)
    0x232cS0x2064S0x1dc1S0x855: RETURNDATACOPY v232bV2064V1dc1V855, v2326V2064V1dc1V855(0x0), v2325V2064V1dc1V855
    0x232dS0x2064S0x1dc1S0x855: v232dV2064V1dc1V855(0x2337) = CONST 
    0x2331S0x2064S0x1dc1S0x855: JUMP v232dV2064V1dc1V855(0x2337)

    Begin block 0x2337B0x2064B0x1dc1B0x855
    prev=[0x2310B0x2064B0x1dc1B0x855, 0x2332B0x2064B0x1dc1B0x855], succ=[0x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x2337_0x1S0x2064S0x1dc1S0x855: v2337_1V2064V1dc1V855 = PHI v2312V2064V1dc1V855, v2333V2064V1dc1V855(0x60)
    0x233dS0x2064S0x1dc1S0x855: v233dV2064V1dc1V855(0x2349) = CONST 
    0x2344S0x2064S0x1dc1S0x855: v2344V2064V1dc1V855(0x235a) = CONST 
    0x2348S0x2064S0x1dc1S0x855: JUMP v2344V2064V1dc1V855(0x235a)

    Begin block 0x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x2337B0x2064B0x1dc1B0x855], succ=[0x236bB0x2337B0x2064B0x1dc1B0x855, 0x2364B0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x235bS0x2337S0x2064S0x1dc1S0x855: v235bV2337V2064V1dc1V855(0x60) = CONST 
    0x235eS0x2337S0x2064S0x1dc1S0x855: v235eV2337V2064V1dc1V855 = ISZERO v2300V2064V1dc1V855
    0x235fS0x2337S0x2064S0x1dc1S0x855: v235fV2337V2064V1dc1V855(0x236b) = CONST 
    0x2363S0x2337S0x2064S0x1dc1S0x855: JUMPI v235fV2337V2064V1dc1V855(0x236b), v235eV2337V2064V1dc1V855

    Begin block 0x236bB0x2337B0x2064B0x1dc1B0x855
    prev=[0x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x237cB0x2337B0x2064B0x1dc1B0x855, 0x2374B0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x236dS0x2337S0x2064S0x1dc1S0x855: v236dV2337V2064V1dc1V855 = MLOAD v2337_1V2064V1dc1V855
    0x236eS0x2337S0x2064S0x1dc1S0x855: v236eV2337V2064V1dc1V855 = ISZERO v236dV2337V2064V1dc1V855
    0x236fS0x2337S0x2064S0x1dc1S0x855: v236fV2337V2064V1dc1V855(0x237c) = CONST 
    0x2373S0x2337S0x2064S0x1dc1S0x855: JUMPI v236fV2337V2064V1dc1V855(0x237c), v236eV2337V2064V1dc1V855

    Begin block 0x237cB0x2337B0x2064B0x1dc1B0x855
    prev=[0x236bB0x2337B0x2064B0x1dc1B0x855], succ=[0x23b5B0x2337B0x2064B0x1dc1B0x855, 0x21740x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x237dS0x2337S0x2064S0x1dc1S0x855: v237dV2337V2064V1dc1V855(0x40) = CONST 
    0x237fS0x2337S0x2064S0x1dc1S0x855: v237fV2337V2064V1dc1V855 = MLOAD v237dV2337V2064V1dc1V855(0x40)
    0x2380S0x2337S0x2064S0x1dc1S0x855: v2380V2337V2064V1dc1V855(0x461bcd) = CONST 
    0x2384S0x2337S0x2064S0x1dc1S0x855: v2384V2337V2064V1dc1V855(0xe5) = CONST 
    0x2386S0x2337S0x2064S0x1dc1S0x855: v2386V2337V2064V1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2384V2337V2064V1dc1V855(0xe5), v2380V2337V2064V1dc1V855(0x461bcd)
    0x2388S0x2337S0x2064S0x1dc1S0x855: MSTORE v237fV2337V2064V1dc1V855, v2386V2337V2064V1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2389S0x2337S0x2064S0x1dc1S0x855: v2389V2337V2064V1dc1V855(0x20) = CONST 
    0x238bS0x2337S0x2064S0x1dc1S0x855: v238bV2337V2064V1dc1V855(0x4) = CONST 
    0x238eS0x2337S0x2064S0x1dc1S0x855: v238eV2337V2064V1dc1V855 = ADD v237fV2337V2064V1dc1V855, v238bV2337V2064V1dc1V855(0x4)
    0x2391S0x2337S0x2064S0x1dc1S0x855: MSTORE v238eV2337V2064V1dc1V855, v2389V2337V2064V1dc1V855(0x20)
    0x2393S0x2337S0x2064S0x1dc1S0x855: v2393V2337V2064V1dc1V855(0x20) = MLOAD v206eV1dc1V855
    0x2394S0x2337S0x2064S0x1dc1S0x855: v2394V2337V2064V1dc1V855(0x24) = CONST 
    0x2397S0x2337S0x2064S0x1dc1S0x855: v2397V2337V2064V1dc1V855 = ADD v237fV2337V2064V1dc1V855, v2394V2337V2064V1dc1V855(0x24)
    0x2398S0x2337S0x2064S0x1dc1S0x855: MSTORE v2397V2337V2064V1dc1V855, v2393V2337V2064V1dc1V855(0x20)
    0x239aS0x2337S0x2064S0x1dc1S0x855: v239aV2337V2064V1dc1V855(0x20) = MLOAD v206eV1dc1V855
    0x23a1S0x2337S0x2064S0x1dc1S0x855: v23a1V2337V2064V1dc1V855(0x44) = CONST 
    0x23a3S0x2337S0x2064S0x1dc1S0x855: v23a3V2337V2064V1dc1V855 = ADD v23a1V2337V2064V1dc1V855(0x44), v237fV2337V2064V1dc1V855
    0x23a7S0x2337S0x2064S0x1dc1S0x855: v23a7V2337V2064V1dc1V855 = ADD v206eV1dc1V855, v2389V2337V2064V1dc1V855(0x20)
    0x23acS0x2337S0x2064S0x1dc1S0x855: v23acV2337V2064V1dc1V855(0x0) = CONST 
    0x23afS0x2337S0x2064S0x1dc1S0x855: v23afV2337V2064V1dc1V855 = ISZERO v239aV2337V2064V1dc1V855(0x20)
    0x23b0S0x2337S0x2064S0x1dc1S0x855: v23b0V2337V2064V1dc1V855(0x2174) = CONST 
    0x23b4S0x2337S0x2064S0x1dc1S0x855: JUMPI v23b0V2337V2064V1dc1V855(0x2174), v23afV2337V2064V1dc1V855

    Begin block 0x23b5B0x2337B0x2064B0x1dc1B0x855
    prev=[0x237cB0x2337B0x2064B0x1dc1B0x855], succ=[0x215a0x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x23b7S0x2337S0x2064S0x1dc1S0x855: v23b7V2337V2064V1dc1V855 = ADD v23acV2337V2064V1dc1V855(0x0), v23a7V2337V2064V1dc1V855
    0x23b8S0x2337S0x2064S0x1dc1S0x855: v23b8V2337V2064V1dc1V855 = MLOAD v23b7V2337V2064V1dc1V855
    0x23bbS0x2337S0x2064S0x1dc1S0x855: v23bbV2337V2064V1dc1V855 = ADD v23acV2337V2064V1dc1V855(0x0), v23a3V2337V2064V1dc1V855
    0x23bcS0x2337S0x2064S0x1dc1S0x855: MSTORE v23bbV2337V2064V1dc1V855, v23b8V2337V2064V1dc1V855
    0x23bdS0x2337S0x2064S0x1dc1S0x855: v23bdV2337V2064V1dc1V855(0x20) = CONST 
    0x23bfS0x2337S0x2064S0x1dc1S0x855: v23bfV2337V2064V1dc1V855(0x20) = ADD v23bdV2337V2064V1dc1V855(0x20), v23acV2337V2064V1dc1V855(0x0)
    0x23c0S0x2337S0x2064S0x1dc1S0x855: v23c0V2337V2064V1dc1V855(0x215a) = CONST 
    0x23c4S0x2337S0x2064S0x1dc1S0x855: JUMP v23c0V2337V2064V1dc1V855(0x215a)

    Begin block 0x215a0x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x23b5B0x2337B0x2064B0x1dc1B0x855, 0x21640x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x21640x235aB0x2337B0x2064B0x1dc1B0x855, 0x21740x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x215a0x235a_0x0S0x2337S0x2064S0x1dc1S0x855: v215a235a_0V2337V2064V1dc1V855 = PHI v23bfV2337V2064V1dc1V855(0x20), v235a216eV2337V2064V1dc1V855
    0x215d0x235aS0x2337S0x2064S0x1dc1S0x855: v235a215dV2337V2064V1dc1V855 = LT v215a235a_0V2337V2064V1dc1V855, v239aV2337V2064V1dc1V855(0x20)
    0x215e0x235aS0x2337S0x2064S0x1dc1S0x855: v235a215eV2337V2064V1dc1V855 = ISZERO v235a215dV2337V2064V1dc1V855
    0x215f0x235aS0x2337S0x2064S0x1dc1S0x855: v235a215fV2337V2064V1dc1V855(0x2174) = CONST 
    0x21630x235aS0x2337S0x2064S0x1dc1S0x855: JUMPI v235a215fV2337V2064V1dc1V855(0x2174), v235a215eV2337V2064V1dc1V855

    Begin block 0x21640x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x215a0x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x215a0x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x21640x235a_0x0S0x2337S0x2064S0x1dc1S0x855: v2164235a_0V2337V2064V1dc1V855 = PHI v23bfV2337V2064V1dc1V855(0x20), v235a216eV2337V2064V1dc1V855
    0x21660x235aS0x2337S0x2064S0x1dc1S0x855: v235a2166V2337V2064V1dc1V855 = ADD v2164235a_0V2337V2064V1dc1V855, v23a7V2337V2064V1dc1V855
    0x21670x235aS0x2337S0x2064S0x1dc1S0x855: v235a2167V2337V2064V1dc1V855 = MLOAD v235a2166V2337V2064V1dc1V855
    0x216a0x235aS0x2337S0x2064S0x1dc1S0x855: v235a216aV2337V2064V1dc1V855 = ADD v2164235a_0V2337V2064V1dc1V855, v23a3V2337V2064V1dc1V855
    0x216b0x235aS0x2337S0x2064S0x1dc1S0x855: MSTORE v235a216aV2337V2064V1dc1V855, v235a2167V2337V2064V1dc1V855
    0x216c0x235aS0x2337S0x2064S0x1dc1S0x855: v235a216cV2337V2064V1dc1V855(0x20) = CONST 
    0x216e0x235aS0x2337S0x2064S0x1dc1S0x855: v235a216eV2337V2064V1dc1V855 = ADD v235a216cV2337V2064V1dc1V855(0x20), v2164235a_0V2337V2064V1dc1V855
    0x216f0x235aS0x2337S0x2064S0x1dc1S0x855: v235a216fV2337V2064V1dc1V855(0x215a) = CONST 
    0x21730x235aS0x2337S0x2064S0x1dc1S0x855: JUMP v235a216fV2337V2064V1dc1V855(0x215a)

    Begin block 0x21740x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x237cB0x2337B0x2064B0x1dc1B0x855, 0x215a0x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x21890x235aB0x2337B0x2064B0x1dc1B0x855, 0x21a20x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x217d0x235aS0x2337S0x2064S0x1dc1S0x855: v235a217dV2337V2064V1dc1V855 = ADD v239aV2337V2064V1dc1V855(0x20), v23a3V2337V2064V1dc1V855
    0x217f0x235aS0x2337S0x2064S0x1dc1S0x855: v235a217fV2337V2064V1dc1V855(0x1f) = CONST 
    0x21810x235aS0x2337S0x2064S0x1dc1S0x855: v235a2181V2337V2064V1dc1V855(0x0) = AND v235a217fV2337V2064V1dc1V855(0x1f), v239aV2337V2064V1dc1V855(0x20)
    0x21830x235aS0x2337S0x2064S0x1dc1S0x855: v235a2183V2337V2064V1dc1V855 = ISZERO v235a2181V2337V2064V1dc1V855(0x0)
    0x21840x235aS0x2337S0x2064S0x1dc1S0x855: v235a2184V2337V2064V1dc1V855(0x21a2) = CONST 
    0x21880x235aS0x2337S0x2064S0x1dc1S0x855: JUMPI v235a2184V2337V2064V1dc1V855(0x21a2), v235a2183V2337V2064V1dc1V855

    Begin block 0x21890x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x21740x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x21a20x235aB0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x218b0x235aS0x2337S0x2064S0x1dc1S0x855: v235a218bV2337V2064V1dc1V855 = SUB v235a217dV2337V2064V1dc1V855, v235a2181V2337V2064V1dc1V855(0x0)
    0x218d0x235aS0x2337S0x2064S0x1dc1S0x855: v235a218dV2337V2064V1dc1V855 = MLOAD v235a218bV2337V2064V1dc1V855
    0x218e0x235aS0x2337S0x2064S0x1dc1S0x855: v235a218eV2337V2064V1dc1V855(0x1) = CONST 
    0x21910x235aS0x2337S0x2064S0x1dc1S0x855: v235a2191V2337V2064V1dc1V855(0x20) = CONST 
    0x21930x235aS0x2337S0x2064S0x1dc1S0x855: v235a2193V2337V2064V1dc1V855(0x20) = SUB v235a2191V2337V2064V1dc1V855(0x20), v235a2181V2337V2064V1dc1V855(0x0)
    0x21940x235aS0x2337S0x2064S0x1dc1S0x855: v235a2194V2337V2064V1dc1V855(0x100) = CONST 
    0x21970x235aS0x2337S0x2064S0x1dc1S0x855: v235a2197V2337V2064V1dc1V855(0x1) = EXP v235a2194V2337V2064V1dc1V855(0x100), v235a2193V2337V2064V1dc1V855(0x20)
    0x21980x235aS0x2337S0x2064S0x1dc1S0x855: v235a2198V2337V2064V1dc1V855(0x0) = SUB v235a2197V2337V2064V1dc1V855(0x1), v235a218eV2337V2064V1dc1V855(0x1)
    0x21990x235aS0x2337S0x2064S0x1dc1S0x855: v235a2199V2337V2064V1dc1V855 = NOT v235a2198V2337V2064V1dc1V855(0x0)
    0x219a0x235aS0x2337S0x2064S0x1dc1S0x855: v235a219aV2337V2064V1dc1V855 = AND v235a2199V2337V2064V1dc1V855, v235a218dV2337V2064V1dc1V855
    0x219c0x235aS0x2337S0x2064S0x1dc1S0x855: MSTORE v235a218bV2337V2064V1dc1V855, v235a219aV2337V2064V1dc1V855
    0x219d0x235aS0x2337S0x2064S0x1dc1S0x855: v235a219dV2337V2064V1dc1V855(0x20) = CONST 
    0x219f0x235aS0x2337S0x2064S0x1dc1S0x855: v235a219fV2337V2064V1dc1V855 = ADD v235a219dV2337V2064V1dc1V855(0x20), v235a218bV2337V2064V1dc1V855

    Begin block 0x21a20x235aB0x2337B0x2064B0x1dc1B0x855
    prev=[0x21740x235aB0x2337B0x2064B0x1dc1B0x855, 0x21890x235aB0x2337B0x2064B0x1dc1B0x855], succ=[]
    =================================
    0x21a20x235a_0x1S0x2337S0x2064S0x1dc1S0x855: v21a2235a_1V2337V2064V1dc1V855 = PHI v235a217dV2337V2064V1dc1V855, v235a219fV2337V2064V1dc1V855
    0x21a80x235aS0x2337S0x2064S0x1dc1S0x855: v235a21a8V2337V2064V1dc1V855(0x40) = CONST 
    0x21aa0x235aS0x2337S0x2064S0x1dc1S0x855: v235a21aaV2337V2064V1dc1V855 = MLOAD v235a21a8V2337V2064V1dc1V855(0x40)
    0x21ad0x235aS0x2337S0x2064S0x1dc1S0x855: v235a21adV2337V2064V1dc1V855 = SUB v21a2235a_1V2337V2064V1dc1V855, v235a21aaV2337V2064V1dc1V855
    0x21af0x235aS0x2337S0x2064S0x1dc1S0x855: REVERT v235a21aaV2337V2064V1dc1V855, v235a21adV2337V2064V1dc1V855

    Begin block 0x2374B0x2337B0x2064B0x1dc1B0x855
    prev=[0x236bB0x2337B0x2064B0x1dc1B0x855], succ=[]
    =================================
    0x2375S0x2337S0x2064S0x1dc1S0x855: v2375V2337V2064V1dc1V855 = MLOAD v2337_1V2064V1dc1V855
    0x2378S0x2337S0x2064S0x1dc1S0x855: v2378V2337V2064V1dc1V855(0x20) = CONST 
    0x237aS0x2337S0x2064S0x1dc1S0x855: v237aV2337V2064V1dc1V855 = ADD v2378V2337V2064V1dc1V855(0x20), v2337_1V2064V1dc1V855
    0x237bS0x2337S0x2064S0x1dc1S0x855: REVERT v237aV2337V2064V1dc1V855, v2375V2337V2064V1dc1V855

    Begin block 0x2364B0x2337B0x2064B0x1dc1B0x855
    prev=[0x235aB0x2337B0x2064B0x1dc1B0x855], succ=[0x4118B0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x2366S0x2337S0x2064S0x1dc1S0x855: v2366V2337V2064V1dc1V855(0x4118) = CONST 
    0x236aS0x2337S0x2064S0x1dc1S0x855: JUMP v2366V2337V2064V1dc1V855(0x4118)

    Begin block 0x4118B0x2337B0x2064B0x1dc1B0x855
    prev=[0x2364B0x2337B0x2064B0x1dc1B0x855], succ=[0x2349B0x2064B0x1dc1B0x855]
    =================================
    0x411eS0x2337S0x2064S0x1dc1S0x855: JUMP v233dV2064V1dc1V855(0x2349)

    Begin block 0x2349B0x2064B0x1dc1B0x855
    prev=[0x4118B0x2337B0x2064B0x1dc1B0x855], succ=[0x40f1B0x2064B0x1dc1B0x855]
    =================================
    0x2353S0x2064S0x1dc1S0x855: JUMP v2227V2064V1dc1V855(0x40f1)

    Begin block 0x40f1B0x2064B0x1dc1B0x855
    prev=[0x2349B0x2064B0x1dc1B0x855], succ=[0x20bbB0x1dc1B0x855]
    =================================
    0x40f8S0x2064S0x1dc1S0x855: JUMP v2067V1dc1V855(0x20bb)

    Begin block 0x20bbB0x1dc1B0x855
    prev=[0x40f1B0x2064B0x1dc1B0x855], succ=[0x20c7B0x1dc1B0x855, 0x40a9B0x1dc1B0x855]
    =================================
    0x20bdS0x1dc1S0x855: v20bdV1dc1V855 = MLOAD v2337_1V2064V1dc1V855
    0x20c1S0x1dc1S0x855: v20c1V1dc1V855 = ISZERO v20bdV1dc1V855
    0x20c2S0x1dc1S0x855: v20c2V1dc1V855(0x40a9) = CONST 
    0x20c6S0x1dc1S0x855: JUMPI v20c2V1dc1V855(0x40a9), v20c1V1dc1V855

    Begin block 0x20c7B0x1dc1B0x855
    prev=[0x20bbB0x1dc1B0x855], succ=[0x20d8B0x1dc1B0x855, 0x20dcB0x1dc1B0x855]
    =================================
    0x20c9S0x1dc1S0x855: v20c9V1dc1V855(0x20) = CONST 
    0x20cbS0x1dc1S0x855: v20cbV1dc1V855 = ADD v20c9V1dc1V855(0x20), v2337_1V2064V1dc1V855
    0x20cdS0x1dc1S0x855: v20cdV1dc1V855 = MLOAD v2337_1V2064V1dc1V855
    0x20ceS0x1dc1S0x855: v20ceV1dc1V855(0x20) = CONST 
    0x20d1S0x1dc1S0x855: v20d1V1dc1V855 = LT v20cdV1dc1V855, v20ceV1dc1V855(0x20)
    0x20d2S0x1dc1S0x855: v20d2V1dc1V855 = ISZERO v20d1V1dc1V855
    0x20d3S0x1dc1S0x855: v20d3V1dc1V855(0x20dc) = CONST 
    0x20d7S0x1dc1S0x855: JUMPI v20d3V1dc1V855(0x20dc), v20d2V1dc1V855

    Begin block 0x20d8B0x1dc1B0x855
    prev=[0x20c7B0x1dc1B0x855], succ=[]
    =================================
    0x20d8S0x1dc1S0x855: v20d8V1dc1V855(0x0) = CONST 
    0x20dbS0x1dc1S0x855: REVERT v20d8V1dc1V855(0x0), v20d8V1dc1V855(0x0)

    Begin block 0x20dcB0x1dc1B0x855
    prev=[0x20c7B0x1dc1B0x855], succ=[0x20e4B0x1dc1B0x855, 0x40cdB0x1dc1B0x855]
    =================================
    0x20deS0x1dc1S0x855: v20deV1dc1V855 = MLOAD v20cbV1dc1V855
    0x20dfS0x1dc1S0x855: v20dfV1dc1V855(0x40cd) = CONST 
    0x20e3S0x1dc1S0x855: JUMPI v20dfV1dc1V855(0x40cd), v20deV1dc1V855

    Begin block 0x20e4B0x1dc1B0x855
    prev=[0x20dcB0x1dc1B0x855], succ=[]
    =================================
    0x20e4S0x1dc1S0x855: v20e4V1dc1V855(0x40) = CONST 
    0x20e6S0x1dc1S0x855: v20e6V1dc1V855 = MLOAD v20e4V1dc1V855(0x40)
    0x20e7S0x1dc1S0x855: v20e7V1dc1V855(0x461bcd) = CONST 
    0x20ebS0x1dc1S0x855: v20ebV1dc1V855(0xe5) = CONST 
    0x20edS0x1dc1S0x855: v20edV1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v20ebV1dc1V855(0xe5), v20e7V1dc1V855(0x461bcd)
    0x20efS0x1dc1S0x855: MSTORE v20e6V1dc1V855, v20edV1dc1V855(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x20f0S0x1dc1S0x855: v20f0V1dc1V855(0x4) = CONST 
    0x20f2S0x1dc1S0x855: v20f2V1dc1V855 = ADD v20f0V1dc1V855(0x4), v20e6V1dc1V855
    0x20f5S0x1dc1S0x855: v20f5V1dc1V855(0x20) = CONST 
    0x20f7S0x1dc1S0x855: v20f7V1dc1V855 = ADD v20f5V1dc1V855(0x20), v20f2V1dc1V855
    0x20faS0x1dc1S0x855: v20faV1dc1V855(0x20) = SUB v20f7V1dc1V855, v20f2V1dc1V855
    0x20fcS0x1dc1S0x855: MSTORE v20f2V1dc1V855, v20faV1dc1V855(0x20)
    0x20fdS0x1dc1S0x855: v20fdV1dc1V855(0x2a) = CONST 
    0x2100S0x1dc1S0x855: MSTORE v20f7V1dc1V855, v20fdV1dc1V855(0x2a)
    0x2101S0x1dc1S0x855: v2101V1dc1V855(0x20) = CONST 
    0x2103S0x1dc1S0x855: v2103V1dc1V855 = ADD v2101V1dc1V855(0x20), v20f7V1dc1V855
    0x2105S0x1dc1S0x855: v2105V1dc1V855(0x37ab) = CONST 
    0x2109S0x1dc1S0x855: v2109V1dc1V855(0x2a) = CONST 
    0x210cS0x1dc1S0x855: CODECOPY v2103V1dc1V855, v2105V1dc1V855(0x37ab), v2109V1dc1V855(0x2a)
    0x210dS0x1dc1S0x855: v210dV1dc1V855(0x40) = CONST 
    0x210fS0x1dc1S0x855: v210fV1dc1V855 = ADD v210dV1dc1V855(0x40), v2103V1dc1V855
    0x2113S0x1dc1S0x855: v2113V1dc1V855(0x40) = CONST 
    0x2115S0x1dc1S0x855: v2115V1dc1V855 = MLOAD v2113V1dc1V855(0x40)
    0x2118S0x1dc1S0x855: v2118V1dc1V855(0x84) = SUB v210fV1dc1V855, v2115V1dc1V855
    0x211aS0x1dc1S0x855: REVERT v2115V1dc1V855, v2118V1dc1V855(0x84)

    Begin block 0x40cdB0x1dc1B0x855
    prev=[0x20dcB0x1dc1B0x855], succ=[0x1e1dB0x855]
    =================================
    0x40d1S0x1dc1S0x855: JUMP v1e11V855(0x1e1d)

    Begin block 0x1e1dB0x855
    prev=[0x40a9B0x1dc1B0x855, 0x40cdB0x1dc1B0x855], succ=[0x86c]
    =================================
    0x1e22S0x855: JUMP v856(0x86c)

    Begin block 0x86c
    prev=[0x1e1dB0x855], succ=[0x8a8, 0x8ac]
    =================================
    0x86d: v86d(0x0) = CONST 
    0x86f: v86f(0x906) = CONST 
    0x874: v874(0x1) = CONST 
    0x876: v876(0x1) = CONST 
    0x878: v878(0xa0) = CONST 
    0x87a: v87a(0x10000000000000000000000000000000000000000) = SHL v878(0xa0), v876(0x1)
    0x87b: v87b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v87a(0x10000000000000000000000000000000000000000), v874(0x1)
    0x87c: v87c = AND v87b(0xffffffffffffffffffffffffffffffffffffffff), v29c
    0x87d: v87d(0x18160ddd) = CONST 
    0x882: v882(0x40) = CONST 
    0x884: v884 = MLOAD v882(0x40)
    0x886: v886(0xffffffff) = CONST 
    0x88b: v88b(0x18160ddd) = AND v886(0xffffffff), v87d(0x18160ddd)
    0x88c: v88c(0xe0) = CONST 
    0x88e: v88e(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL v88c(0xe0), v88b(0x18160ddd)
    0x890: MSTORE v884, v88e(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x891: v891(0x4) = CONST 
    0x893: v893 = ADD v891(0x4), v884
    0x894: v894(0x20) = CONST 
    0x896: v896(0x40) = CONST 
    0x898: v898 = MLOAD v896(0x40)
    0x89b: v89b(0x4) = SUB v893, v898
    0x89f: v89f = EXTCODESIZE v87c
    0x8a0: v8a0 = ISZERO v89f
    0x8a2: v8a2 = ISZERO v8a0
    0x8a3: v8a3(0x8ac) = CONST 
    0x8a7: JUMPI v8a3(0x8ac), v8a2

    Begin block 0x8a8
    prev=[0x86c], succ=[]
    =================================
    0x8a8: v8a8(0x0) = CONST 
    0x8ab: REVERT v8a8(0x0), v8a8(0x0)

    Begin block 0x8ac
    prev=[0x86c], succ=[0x8b8, 0x8c1]
    =================================
    0x8ae: v8ae = GAS 
    0x8af: v8af = STATICCALL v8ae, v87c, v898, v89b(0x4), v898, v894(0x20)
    0x8b0: v8b0 = ISZERO v8af
    0x8b2: v8b2 = ISZERO v8b0
    0x8b3: v8b3(0x8c1) = CONST 
    0x8b7: JUMPI v8b3(0x8c1), v8b2

    Begin block 0x8b8
    prev=[0x8ac], succ=[]
    =================================
    0x8b8: v8b8 = RETURNDATASIZE 
    0x8b9: v8b9(0x0) = CONST 
    0x8bc: RETURNDATACOPY v8b9(0x0), v8b9(0x0), v8b8
    0x8bd: v8bd = RETURNDATASIZE 
    0x8be: v8be(0x0) = CONST 
    0x8c0: REVERT v8be(0x0), v8bd

    Begin block 0x8c1
    prev=[0x8ac], succ=[0x8d4, 0x8d8]
    =================================
    0x8c6: v8c6(0x40) = CONST 
    0x8c8: v8c8 = MLOAD v8c6(0x40)
    0x8c9: v8c9 = RETURNDATASIZE 
    0x8ca: v8ca(0x20) = CONST 
    0x8cd: v8cd = LT v8c9, v8ca(0x20)
    0x8ce: v8ce = ISZERO v8cd
    0x8cf: v8cf(0x8d8) = CONST 
    0x8d3: JUMPI v8cf(0x8d8), v8ce

    Begin block 0x8d4
    prev=[0x8c1], succ=[]
    =================================
    0x8d4: v8d4(0x0) = CONST 
    0x8d7: REVERT v8d4(0x0), v8d4(0x0)

    Begin block 0x8d8
    prev=[0x8c1], succ=[0x3dfa]
    =================================
    0x8da: v8da = MLOAD v8c8
    0x8db: v8db(0x1) = CONST 
    0x8dd: v8dd(0x1) = CONST 
    0x8df: v8df(0xa0) = CONST 
    0x8e1: v8e1(0x10000000000000000000000000000000000000000) = SHL v8df(0xa0), v8dd(0x1)
    0x8e2: v8e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v8e1(0x10000000000000000000000000000000000000000), v8db(0x1)
    0x8e4: v8e4 = AND v293, v8e2(0xffffffffffffffffffffffffffffffffffffffff)
    0x8e5: v8e5(0x0) = CONST 
    0x8e9: MSTORE v8e5(0x0), v8e4
    0x8ea: v8ea(0x3) = CONST 
    0x8ec: v8ec(0x20) = CONST 
    0x8ee: MSTORE v8ec(0x20), v8ea(0x3)
    0x8ef: v8ef(0x40) = CONST 
    0x8f2: v8f2 = SHA3 v8e5(0x0), v8ef(0x40)
    0x8f3: v8f3 = SLOAD v8f2
    0x8f4: v8f4(0x3dfa) = CONST 
    0x8fa: v8fa(0x1e23) = CONST 
    0x8fe: v8fe_0 = CALLPRIVATE v8fa(0x1e23), v2a1, v8f3, v8f4(0x3dfa)

    Begin block 0x3dfa
    prev=[0x8d8], succ=[0x1e810x260]
    =================================
    0x3dfc: v3dfc(0x1e81) = CONST 
    0x3e00: JUMP v3dfc(0x1e81)

    Begin block 0x1e810x260
    prev=[0x3dfa], succ=[0x21200x260]
    =================================
    0x1e820x260: v2601e82(0x0) = CONST 
    0x1e840x260: v2601e84(0x4037) = CONST 
    0x1e8a0x260: v2601e8a(0x40) = CONST 
    0x1e8c0x260: v2601e8c = MLOAD v2601e8a(0x40)
    0x1e8e0x260: v2601e8e(0x40) = CONST 
    0x1e900x260: v2601e90 = ADD v2601e8e(0x40), v2601e8c
    0x1e910x260: v2601e91(0x40) = CONST 
    0x1e930x260: MSTORE v2601e91(0x40), v2601e90
    0x1e950x260: v2601e95(0x1a) = CONST 
    0x1e980x260: MSTORE v2601e8c, v2601e95(0x1a)
    0x1e990x260: v2601e99(0x20) = CONST 
    0x1e9b0x260: v2601e9b = ADD v2601e99(0x20), v2601e8c
    0x1e9c0x260: v2601e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1ebe0x260: MSTORE v2601e9b, v2601e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1ec00x260: v2601ec0(0x2120) = CONST 
    0x1ec40x260: JUMP v2601ec0(0x2120)

    Begin block 0x21200x260
    prev=[0x1e810x260], succ=[0x212a0x260, 0x21b00x260]
    =================================
    0x21210x260: v2602121(0x0) = CONST 
    0x21250x260: v2602125(0x21b0) = CONST 
    0x21290x260: JUMPI v2602125(0x21b0), v8da

    Begin block 0x212a0x260
    prev=[0x21200x260], succ=[0x215a0x260]
    =================================
    0x212a0x260: v260212a(0x40) = CONST 
    0x212c0x260: v260212c = MLOAD v260212a(0x40)
    0x212d0x260: v260212d(0x461bcd) = CONST 
    0x21310x260: v2602131(0xe5) = CONST 
    0x21330x260: v2602133(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2602131(0xe5), v260212d(0x461bcd)
    0x21350x260: MSTORE v260212c, v2602133(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21360x260: v2602136(0x4) = CONST 
    0x21380x260: v2602138 = ADD v2602136(0x4), v260212c
    0x213b0x260: v260213b(0x20) = CONST 
    0x213d0x260: v260213d = ADD v260213b(0x20), v2602138
    0x21400x260: v2602140(0x20) = SUB v260213d, v2602138
    0x21420x260: MSTORE v2602138, v2602140(0x20)
    0x21460x260: v2602146(0x1a) = MLOAD v2601e8c
    0x21480x260: MSTORE v260213d, v2602146(0x1a)
    0x21490x260: v2602149(0x20) = CONST 
    0x214b0x260: v260214b = ADD v2602149(0x20), v260213d
    0x214f0x260: v260214f(0x1a) = MLOAD v2601e8c
    0x21510x260: v2602151(0x20) = CONST 
    0x21530x260: v2602153 = ADD v2602151(0x20), v2601e8c
    0x21580x260: v2602158(0x0) = CONST 

    Begin block 0x215a0x260
    prev=[0x212a0x260, 0x21640x260], succ=[0x21740x260, 0x21640x260]
    =================================
    0x215a0x260_0x0: v215a260_0 = PHI v260216e, v2602158(0x0)
    0x215d0x260: v260215d = LT v215a260_0, v260214f(0x1a)
    0x215e0x260: v260215e = ISZERO v260215d
    0x215f0x260: v260215f(0x2174) = CONST 
    0x21630x260: JUMPI v260215f(0x2174), v260215e

    Begin block 0x21740x260
    prev=[0x215a0x260], succ=[0x21a20x260, 0x21890x260]
    =================================
    0x217d0x260: v260217d = ADD v260214f(0x1a), v260214b
    0x217f0x260: v260217f(0x1f) = CONST 
    0x21810x260: v2602181(0x1a) = AND v260217f(0x1f), v260214f(0x1a)
    0x21830x260: v2602183 = ISZERO v2602181(0x1a)
    0x21840x260: v2602184(0x21a2) = CONST 
    0x21880x260: JUMPI v2602184(0x21a2), v2602183

    Begin block 0x21a20x260
    prev=[0x21740x260, 0x21890x260], succ=[]
    =================================
    0x21a20x260_0x1: v21a2260_1 = PHI v260219f, v260217d
    0x21a80x260: v26021a8(0x40) = CONST 
    0x21aa0x260: v26021aa = MLOAD v26021a8(0x40)
    0x21ad0x260: v26021ad = SUB v21a2260_1, v26021aa
    0x21af0x260: REVERT v26021aa, v26021ad

    Begin block 0x21890x260
    prev=[0x21740x260], succ=[0x21a20x260]
    =================================
    0x218b0x260: v260218b = SUB v260217d, v2602181(0x1a)
    0x218d0x260: v260218d = MLOAD v260218b
    0x218e0x260: v260218e(0x1) = CONST 
    0x21910x260: v2602191(0x20) = CONST 
    0x21930x260: v2602193(0x6) = SUB v2602191(0x20), v2602181(0x1a)
    0x21940x260: v2602194(0x100) = CONST 
    0x21970x260: v2602197(0x1000000000000) = EXP v2602194(0x100), v2602193(0x6)
    0x21980x260: v2602198(0xffffffffffff) = SUB v2602197(0x1000000000000), v260218e(0x1)
    0x21990x260: v2602199 = NOT v2602198(0xffffffffffff)
    0x219a0x260: v260219a = AND v2602199, v260218d
    0x219c0x260: MSTORE v260218b, v260219a
    0x219d0x260: v260219d(0x20) = CONST 
    0x219f0x260: v260219f = ADD v260219d(0x20), v260218b

    Begin block 0x21640x260
    prev=[0x215a0x260], succ=[0x215a0x260]
    =================================
    0x21640x260_0x0: v2164260_0 = PHI v260216e, v2602158(0x0)
    0x21660x260: v2602166 = ADD v2164260_0, v2602153
    0x21670x260: v2602167 = MLOAD v2602166
    0x216a0x260: v260216a = ADD v2164260_0, v260214b
    0x216b0x260: MSTORE v260216a, v2602167
    0x216c0x260: v260216c(0x20) = CONST 
    0x216e0x260: v260216e = ADD v260216c(0x20), v2164260_0
    0x216f0x260: v260216f(0x215a) = CONST 
    0x21730x260: JUMP v260216f(0x215a)

    Begin block 0x21b00x260
    prev=[0x21200x260], succ=[0x21bc0x260, 0x21bd0x260]
    =================================
    0x21b20x260: v26021b2(0x0) = CONST 
    0x21b70x260: v26021b7(0x21bd) = CONST 
    0x21bb0x260: JUMPI v26021b7(0x21bd), v8da

    Begin block 0x21bc0x260
    prev=[0x21b00x260], succ=[]
    =================================
    0x21bc0x260: THROW 

    Begin block 0x21bd0x260
    prev=[0x21b00x260], succ=[0x40370x260]
    =================================
    0x21be0x260: v26021be = DIV v8fe_0, v8da
    0x21c60x260: JUMP v2601e84(0x4037)

    Begin block 0x40370x260
    prev=[0x21bd0x260], succ=[0x906]
    =================================
    0x403d0x260: JUMP v86f(0x906)

    Begin block 0x906
    prev=[0x40370x260], succ=[0x959, 0x95d]
    =================================
    0x907: v907(0x6) = CONST 
    0x909: v909 = SLOAD v907(0x6)
    0x90a: v90a(0x40) = CONST 
    0x90d: v90d = MLOAD v90a(0x40)
    0x90e: v90e(0x7dc5bcc9) = CONST 
    0x913: v913(0xe1) = CONST 
    0x915: v915(0xfb8b799200000000000000000000000000000000000000000000000000000000) = SHL v913(0xe1), v90e(0x7dc5bcc9)
    0x917: MSTORE v90d, v915(0xfb8b799200000000000000000000000000000000000000000000000000000000)
    0x918: v918(0x4) = CONST 
    0x91b: v91b = ADD v90d, v918(0x4)
    0x91e: MSTORE v91b, v26021be
    0x91f: v91f = CALLER 
    0x920: v920(0x24) = CONST 
    0x923: v923 = ADD v90d, v920(0x24)
    0x924: MSTORE v923, v91f
    0x926: v926 = MLOAD v90a(0x40)
    0x92a: v92a(0x1) = CONST 
    0x92c: v92c(0x1) = CONST 
    0x92e: v92e(0xa0) = CONST 
    0x930: v930(0x10000000000000000000000000000000000000000) = SHL v92e(0xa0), v92c(0x1)
    0x931: v931(0xffffffffffffffffffffffffffffffffffffffff) = SUB v930(0x10000000000000000000000000000000000000000), v92a(0x1)
    0x934: v934 = AND v909, v931(0xffffffffffffffffffffffffffffffffffffffff)
    0x936: v936(0xfb8b7992) = CONST 
    0x93c: v93c(0x44) = CONST 
    0x940: v940 = ADD v90d, v93c(0x44)
    0x942: v942(0x0) = CONST 
    0x94a: v94a(0x0) = SUB v90d, v926
    0x94b: v94b(0x44) = ADD v94a(0x0), v93c(0x44)
    0x950: v950 = EXTCODESIZE v934
    0x951: v951 = ISZERO v950
    0x953: v953 = ISZERO v951
    0x954: v954(0x95d) = CONST 
    0x958: JUMPI v954(0x95d), v953

    Begin block 0x959
    prev=[0x906], succ=[]
    =================================
    0x959: v959(0x0) = CONST 
    0x95c: REVERT v959(0x0), v959(0x0)

    Begin block 0x95d
    prev=[0x906], succ=[0x969, 0x972]
    =================================
    0x95f: v95f = GAS 
    0x960: v960 = CALL v95f, v934, v942(0x0), v926, v94b(0x44), v926, v942(0x0)
    0x961: v961 = ISZERO v960
    0x963: v963 = ISZERO v961
    0x964: v964(0x972) = CONST 
    0x968: JUMPI v964(0x972), v963

    Begin block 0x969
    prev=[0x95d], succ=[]
    =================================
    0x969: v969 = RETURNDATASIZE 
    0x96a: v96a(0x0) = CONST 
    0x96d: RETURNDATACOPY v96a(0x0), v96a(0x0), v969
    0x96e: v96e = RETURNDATASIZE 
    0x96f: v96f(0x0) = CONST 
    0x971: REVERT v96f(0x0), v96e

    Begin block 0x972
    prev=[0x95d], succ=[0x9ec, 0x9f0]
    =================================
    0x975: v975(0x5) = CONST 
    0x977: v977 = SLOAD v975(0x5)
    0x978: v978(0x40) = CONST 
    0x97b: v97b = MLOAD v978(0x40)
    0x97c: v97c(0x75b04b15) = CONST 
    0x981: v981(0xe1) = CONST 
    0x983: v983(0xeb60962a00000000000000000000000000000000000000000000000000000000) = SHL v981(0xe1), v97c(0x75b04b15)
    0x985: MSTORE v97b, v983(0xeb60962a00000000000000000000000000000000000000000000000000000000)
    0x986: v986(0x1) = CONST 
    0x988: v988(0x1) = CONST 
    0x98a: v98a(0xa0) = CONST 
    0x98c: v98c(0x10000000000000000000000000000000000000000) = SHL v98a(0xa0), v988(0x1)
    0x98d: v98d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v98c(0x10000000000000000000000000000000000000000), v986(0x1)
    0x990: v990 = AND v98d(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x991: v991(0x4) = CONST 
    0x994: v994 = ADD v97b, v991(0x4)
    0x995: MSTORE v994, v990
    0x996: v996 = CALLER 
    0x997: v997(0x44) = CONST 
    0x99a: v99a = ADD v97b, v997(0x44)
    0x99b: MSTORE v99a, v996
    0x99c: v99c(0x60) = CONST 
    0x99e: v99e(0x24) = CONST 
    0x9a1: v9a1 = ADD v97b, v99e(0x24)
    0x9a2: MSTORE v9a1, v99c(0x60)
    0x9a3: v9a3(0xe) = CONST 
    0x9a5: v9a5(0x64) = CONST 
    0x9a8: v9a8 = ADD v97b, v9a5(0x64)
    0x9a9: MSTORE v9a8, v9a3(0xe)
    0x9aa: v9aa(0x115512081dda5d1a191c985dd85b) = CONST 
    0x9b9: v9b9(0x92) = CONST 
    0x9bb: v9bb(0x455448207769746864726177616c000000000000000000000000000000000000) = SHL v9b9(0x92), v9aa(0x115512081dda5d1a191c985dd85b)
    0x9bc: v9bc(0x84) = CONST 
    0x9bf: v9bf = ADD v97b, v9bc(0x84)
    0x9c0: MSTORE v9bf, v9bb(0x455448207769746864726177616c000000000000000000000000000000000000)
    0x9c2: v9c2 = MLOAD v978(0x40)
    0x9c6: v9c6 = AND v977, v98d(0xffffffffffffffffffffffffffffffffffffffff)
    0x9c9: v9c9(0xeb60962a) = CONST 
    0x9d0: v9d0(0xa4) = CONST 
    0x9d4: v9d4 = ADD v97b, v9d0(0xa4)
    0x9d6: v9d6(0x0) = CONST 
    0x9dd: v9dd(0x0) = SUB v97b, v9c2
    0x9de: v9de(0xa4) = ADD v9dd(0x0), v9d0(0xa4)
    0x9e3: v9e3 = EXTCODESIZE v9c6
    0x9e4: v9e4 = ISZERO v9e3
    0x9e6: v9e6 = ISZERO v9e4
    0x9e7: v9e7(0x9f0) = CONST 
    0x9eb: JUMPI v9e7(0x9f0), v9e6

    Begin block 0x9ec
    prev=[0x972], succ=[]
    =================================
    0x9ec: v9ec(0x0) = CONST 
    0x9ef: REVERT v9ec(0x0), v9ec(0x0)

    Begin block 0x9f0
    prev=[0x972], succ=[0x9fc, 0xa05]
    =================================
    0x9f2: v9f2 = GAS 
    0x9f3: v9f3 = CALL v9f2, v9c6, v9d6(0x0), v9c2, v9de(0xa4), v9c2, v9d6(0x0)
    0x9f4: v9f4 = ISZERO v9f3
    0x9f6: v9f6 = ISZERO v9f4
    0x9f7: v9f7(0xa05) = CONST 
    0x9fb: JUMPI v9f7(0xa05), v9f6

    Begin block 0x9fc
    prev=[0x9f0], succ=[]
    =================================
    0x9fc: v9fc = RETURNDATASIZE 
    0x9fd: v9fd(0x0) = CONST 
    0xa00: RETURNDATACOPY v9fd(0x0), v9fd(0x0), v9fc
    0xa01: va01 = RETURNDATASIZE 
    0xa02: va02(0x0) = CONST 
    0xa04: REVERT va02(0x0), va01

    Begin block 0xa05
    prev=[0x9f0], succ=[0xa2e]
    =================================
    0xa09: va09(0x1) = CONST 
    0xa0b: va0b(0x1) = CONST 
    0xa0d: va0d(0xa0) = CONST 
    0xa0f: va0f(0x10000000000000000000000000000000000000000) = SHL va0d(0xa0), va0b(0x1)
    0xa10: va10(0xffffffffffffffffffffffffffffffffffffffff) = SUB va0f(0x10000000000000000000000000000000000000000), va09(0x1)
    0xa12: va12 = AND v293, va10(0xffffffffffffffffffffffffffffffffffffffff)
    0xa13: va13(0x0) = CONST 
    0xa17: MSTORE va13(0x0), va12
    0xa18: va18(0x3) = CONST 
    0xa1a: va1a(0x20) = CONST 
    0xa1c: MSTORE va1a(0x20), va18(0x3)
    0xa1d: va1d(0x40) = CONST 
    0xa20: va20 = SHA3 va13(0x0), va1d(0x40)
    0xa21: va21 = SLOAD va20
    0xa22: va22(0xa2e) = CONST 
    0xa29: va29(0x1ec5) = CONST 
    0xa2d: va2d_0 = CALLPRIVATE va29(0x1ec5), v26021be, va21, va22(0xa2e)

    Begin block 0xa2e
    prev=[0xa05], succ=[0xaa2, 0xaa6]
    =================================
    0xa2f: va2f(0x1) = CONST 
    0xa31: va31(0x1) = CONST 
    0xa33: va33(0xa0) = CONST 
    0xa35: va35(0x10000000000000000000000000000000000000000) = SHL va33(0xa0), va31(0x1)
    0xa36: va36(0xffffffffffffffffffffffffffffffffffffffff) = SUB va35(0x10000000000000000000000000000000000000000), va2f(0x1)
    0xa39: va39 = AND v293, va36(0xffffffffffffffffffffffffffffffffffffffff)
    0xa3a: va3a(0x0) = CONST 
    0xa3e: MSTORE va3a(0x0), va39
    0xa3f: va3f(0x3) = CONST 
    0xa41: va41(0x20) = CONST 
    0xa45: MSTORE va41(0x20), va3f(0x3)
    0xa46: va46(0x40) = CONST 
    0xa4a: va4a = SHA3 va3a(0x0), va46(0x40)
    0xa4d: SSTORE va4a, va2d_0
    0xa4e: va4e(0x7) = CONST 
    0xa50: va50 = ADD va4e(0x7), va4a
    0xa52: va52 = SLOAD va50
    0xa53: va53(0x1) = CONST 
    0xa56: va56 = ADD va52, va53(0x1)
    0xa58: SSTORE va50, va56
    0xa5b: MSTORE va3a(0x0), va50
    0xa5e: va5e = SHA3 va3a(0x0), va41(0x20)
    0xa5f: va5f = ADD va5e, va52
    0xa63: SSTORE va5f, va2d_0
    0xa65: va65 = MLOAD va46(0x40)
    0xa66: va66(0x95ea7b3) = CONST 
    0xa6b: va6b(0xe0) = CONST 
    0xa6d: va6d(0x95ea7b300000000000000000000000000000000000000000000000000000000) = SHL va6b(0xe0), va66(0x95ea7b3)
    0xa6f: MSTORE va65, va6d(0x95ea7b300000000000000000000000000000000000000000000000000000000)
    0xa72: va72 = AND v29c, va36(0xffffffffffffffffffffffffffffffffffffffff)
    0xa73: va73(0x4) = CONST 
    0xa76: va76 = ADD va65, va73(0x4)
    0xa79: MSTORE va76, va72
    0xa7a: va7a(0x24) = CONST 
    0xa7d: va7d = ADD va65, va7a(0x24)
    0xa80: MSTORE va7d, v2a1
    0xa82: va82 = MLOAD va46(0x40)
    0xa83: va83(0x95ea7b3) = CONST 
    0xa89: va89(0x44) = CONST 
    0xa8d: va8d = ADD va65, va89(0x44)
    0xa92: va92(0x0) = SUB va65, va82
    0xa93: va93(0x44) = ADD va92(0x0), va89(0x44)
    0xa99: va99 = EXTCODESIZE va72
    0xa9a: va9a = ISZERO va99
    0xa9c: va9c = ISZERO va9a
    0xa9d: va9d(0xaa6) = CONST 
    0xaa1: JUMPI va9d(0xaa6), va9c

    Begin block 0xaa2
    prev=[0xa2e], succ=[]
    =================================
    0xaa2: vaa2(0x0) = CONST 
    0xaa5: REVERT vaa2(0x0), vaa2(0x0)

    Begin block 0xaa6
    prev=[0xa2e], succ=[0xab2, 0xabb]
    =================================
    0xaa8: vaa8 = GAS 
    0xaa9: vaa9 = CALL vaa8, va72, va3a(0x0), va82, va93(0x44), va82, va41(0x20)
    0xaaa: vaaa = ISZERO vaa9
    0xaac: vaac = ISZERO vaaa
    0xaad: vaad(0xabb) = CONST 
    0xab1: JUMPI vaad(0xabb), vaac

    Begin block 0xab2
    prev=[0xaa6], succ=[]
    =================================
    0xab2: vab2 = RETURNDATASIZE 
    0xab3: vab3(0x0) = CONST 
    0xab6: RETURNDATACOPY vab3(0x0), vab3(0x0), vab2
    0xab7: vab7 = RETURNDATASIZE 
    0xab8: vab8(0x0) = CONST 
    0xaba: REVERT vab8(0x0), vab7

    Begin block 0xabb
    prev=[0xaa6], succ=[0xace, 0xad2]
    =================================
    0xac0: vac0(0x40) = CONST 
    0xac2: vac2 = MLOAD vac0(0x40)
    0xac3: vac3 = RETURNDATASIZE 
    0xac4: vac4(0x20) = CONST 
    0xac7: vac7 = LT vac3, vac4(0x20)
    0xac8: vac8 = ISZERO vac7
    0xac9: vac9(0xad2) = CONST 
    0xacd: JUMPI vac9(0xad2), vac8

    Begin block 0xace
    prev=[0xabb], succ=[]
    =================================
    0xace: vace(0x0) = CONST 
    0xad1: REVERT vace(0x0), vace(0x0)

    Begin block 0xad2
    prev=[0xabb], succ=[0xb19, 0xb1d]
    =================================
    0xad5: vad5(0x40) = CONST 
    0xad8: vad8 = MLOAD vad5(0x40)
    0xad9: vad9(0x6d1b229d) = CONST 
    0xade: vade(0xe0) = CONST 
    0xae0: vae0(0x6d1b229d00000000000000000000000000000000000000000000000000000000) = SHL vade(0xe0), vad9(0x6d1b229d)
    0xae2: MSTORE vad8, vae0(0x6d1b229d00000000000000000000000000000000000000000000000000000000)
    0xae3: vae3(0x4) = CONST 
    0xae6: vae6 = ADD vad8, vae3(0x4)
    0xae9: MSTORE vae6, v2a1
    0xaeb: vaeb = MLOAD vad5(0x40)
    0xaec: vaec(0x1) = CONST 
    0xaee: vaee(0x1) = CONST 
    0xaf0: vaf0(0xa0) = CONST 
    0xaf2: vaf2(0x10000000000000000000000000000000000000000) = SHL vaf0(0xa0), vaee(0x1)
    0xaf3: vaf3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaf2(0x10000000000000000000000000000000000000000), vaec(0x1)
    0xaf5: vaf5 = AND v29c, vaf3(0xffffffffffffffffffffffffffffffffffffffff)
    0xaf7: vaf7(0x6d1b229d) = CONST 
    0xafd: vafd(0x24) = CONST 
    0xb01: vb01 = ADD vad8, vafd(0x24)
    0xb03: vb03(0x0) = CONST 
    0xb0a: vb0a(0x0) = SUB vad8, vaeb
    0xb0b: vb0b(0x24) = ADD vb0a(0x0), vafd(0x24)
    0xb10: vb10 = EXTCODESIZE vaf5
    0xb11: vb11 = ISZERO vb10
    0xb13: vb13 = ISZERO vb11
    0xb14: vb14(0xb1d) = CONST 
    0xb18: JUMPI vb14(0xb1d), vb13

    Begin block 0xb19
    prev=[0xad2], succ=[]
    =================================
    0xb19: vb19(0x0) = CONST 
    0xb1c: REVERT vb19(0x0), vb19(0x0)

    Begin block 0xb1d
    prev=[0xad2], succ=[0xb29, 0xb32]
    =================================
    0xb1f: vb1f = GAS 
    0xb20: vb20 = CALL vb1f, vaf5, vb03(0x0), vaeb, vb0b(0x24), vaeb, vb03(0x0)
    0xb21: vb21 = ISZERO vb20
    0xb23: vb23 = ISZERO vb21
    0xb24: vb24(0xb32) = CONST 
    0xb28: JUMPI vb24(0xb32), vb23

    Begin block 0xb29
    prev=[0xb1d], succ=[]
    =================================
    0xb29: vb29 = RETURNDATASIZE 
    0xb2a: vb2a(0x0) = CONST 
    0xb2d: RETURNDATACOPY vb2a(0x0), vb2a(0x0), vb29
    0xb2e: vb2e = RETURNDATASIZE 
    0xb2f: vb2f(0x0) = CONST 
    0xb31: REVERT vb2f(0x0), vb2e

    Begin block 0xb32
    prev=[0xb1d], succ=[0x3a64]
    =================================
    0xb35: vb35(0x40) = CONST 
    0xb38: vb38 = MLOAD vb35(0x40)
    0xb39: vb39 = CALLER 
    0xb3b: MSTORE vb38, vb39
    0xb3c: vb3c(0x1) = CONST 
    0xb3e: vb3e(0x1) = CONST 
    0xb40: vb40(0xa0) = CONST 
    0xb42: vb42(0x10000000000000000000000000000000000000000) = SHL vb40(0xa0), vb3e(0x1)
    0xb43: vb43(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb42(0x10000000000000000000000000000000000000000), vb3c(0x1)
    0xb46: vb46 = AND v293, vb43(0xffffffffffffffffffffffffffffffffffffffff)
    0xb47: vb47(0x20) = CONST 
    0xb4a: vb4a = ADD vb38, vb47(0x20)
    0xb4b: MSTORE vb4a, vb46
    0xb4d: vb4d = AND v29c, vb43(0xffffffffffffffffffffffffffffffffffffffff)
    0xb50: vb50 = ADD vb35(0x40), vb38
    0xb51: MSTORE vb50, vb4d
    0xb52: vb52(0x60) = CONST 
    0xb55: vb55 = ADD vb38, vb52(0x60)
    0xb58: MSTORE vb55, v26021be
    0xb5a: vb5a = MLOAD vb35(0x40)
    0xb5b: vb5b(0xf5fc7ed3de5c91430804f8cdf35dce35b7bbc4ab8de63895df80cf4e80a41053) = CONST 
    0xb81: vb81(0x0) = SUB vb38, vb5a
    0xb82: vb82(0x80) = CONST 
    0xb84: vb84(0x80) = ADD vb82(0x80), vb81(0x0)
    0xb87: LOG1 vb5a, vb84(0x80), vb5b(0xf5fc7ed3de5c91430804f8cdf35dce35b7bbc4ab8de63895df80cf4e80a41053)
    0xb8c: JUMP v26f(0x3a64)

    Begin block 0x3a64
    prev=[0xb32], succ=[]
    =================================
    0x3a65: STOP 

    Begin block 0x40a9B0x1dc1B0x855
    prev=[0x20bbB0x1dc1B0x855], succ=[0x1e1dB0x855]
    =================================
    0x40adS0x1dc1S0x855: JUMP v1e11V855(0x1e1d)

    Begin block 0x2332B0x2064B0x1dc1B0x855
    prev=[0x22ceB0x2064B0x1dc1B0x855], succ=[0x2337B0x2064B0x1dc1B0x855]
    =================================
    0x2333S0x2064S0x1dc1S0x855: v2333V2064V1dc1V855(0x60) = CONST 

    Begin block 0x22b7B0x2064B0x1dc1B0x855
    prev=[0x22adB0x2064B0x1dc1B0x855], succ=[0x22adB0x2064B0x1dc1B0x855]
    =================================
    0x22b7_0x0S0x2064S0x1dc1S0x855: v22b7_0V2064V1dc1V855 = PHI v22a8V2064V1dc1V855, v22c8V2064V1dc1V855
    0x22b7_0x1S0x2064S0x1dc1S0x855: v22b7_1V2064V1dc1V855 = PHI v22a0V2064V1dc1V855, v22c6V2064V1dc1V855
    0x22b7_0x2S0x2064S0x1dc1S0x855: v22b7_2V2064V1dc1V855 = PHI v22a4V2064V1dc1V855(0x64), v22c0V2064V1dc1V855
    0x22b8S0x2064S0x1dc1S0x855: v22b8V2064V1dc1V855 = MLOAD v22b7_0V2064V1dc1V855
    0x22baS0x2064S0x1dc1S0x855: MSTORE v22b7_1V2064V1dc1V855, v22b8V2064V1dc1V855
    0x22bbS0x2064S0x1dc1S0x855: v22bbV2064V1dc1V855(0x1f) = CONST 
    0x22bdS0x2064S0x1dc1S0x855: v22bdV2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v22bbV2064V1dc1V855(0x1f)
    0x22c0S0x2064S0x1dc1S0x855: v22c0V2064V1dc1V855 = ADD v22b7_2V2064V1dc1V855, v22bdV2064V1dc1V855(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x22c2S0x2064S0x1dc1S0x855: v22c2V2064V1dc1V855(0x20) = CONST 
    0x22c6S0x2064S0x1dc1S0x855: v22c6V2064V1dc1V855 = ADD v22c2V2064V1dc1V855(0x20), v22b7_1V2064V1dc1V855
    0x22c8S0x2064S0x1dc1S0x855: v22c8V2064V1dc1V855 = ADD v22c2V2064V1dc1V855(0x20), v22b7_0V2064V1dc1V855
    0x22c9S0x2064S0x1dc1S0x855: v22c9V2064V1dc1V855(0x22ad) = CONST 
    0x22cdS0x2064S0x1dc1S0x855: JUMP v22c9V2064V1dc1V855(0x22ad)

}

function estimateTokensForETH(address,address,uint256)() public {
    Begin block 0x2a9
    prev=[], succ=[0x2b2, 0x2b6]
    =================================
    0x2aa: v2aa = CALLVALUE 
    0x2ac: v2ac = ISZERO v2aa
    0x2ad: v2ad(0x2b6) = CONST 
    0x2b1: JUMPI v2ad(0x2b6), v2ac

    Begin block 0x2b2
    prev=[0x2a9], succ=[]
    =================================
    0x2b2: v2b2(0x0) = CONST 
    0x2b5: REVERT v2b2(0x0), v2b2(0x0)

    Begin block 0x2b6
    prev=[0x2a9], succ=[0x2cb, 0x2cf]
    =================================
    0x2b8: v2b8(0x3a85) = CONST 
    0x2bc: v2bc(0x4) = CONST 
    0x2bf: v2bf = CALLDATASIZE 
    0x2c0: v2c0 = SUB v2bf, v2bc(0x4)
    0x2c1: v2c1(0x60) = CONST 
    0x2c4: v2c4 = LT v2c0, v2c1(0x60)
    0x2c5: v2c5 = ISZERO v2c4
    0x2c6: v2c6(0x2cf) = CONST 
    0x2ca: JUMPI v2c6(0x2cf), v2c5

    Begin block 0x2cb
    prev=[0x2b6], succ=[]
    =================================
    0x2cb: v2cb(0x0) = CONST 
    0x2ce: REVERT v2cb(0x0), v2cb(0x0)

    Begin block 0x2cf
    prev=[0x2b6], succ=[0xb8d]
    =================================
    0x2d1: v2d1(0x1) = CONST 
    0x2d3: v2d3(0x1) = CONST 
    0x2d5: v2d5(0xa0) = CONST 
    0x2d7: v2d7(0x10000000000000000000000000000000000000000) = SHL v2d5(0xa0), v2d3(0x1)
    0x2d8: v2d8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2d7(0x10000000000000000000000000000000000000000), v2d1(0x1)
    0x2da: v2da = CALLDATALOAD v2bc(0x4)
    0x2dc: v2dc = AND v2d8(0xffffffffffffffffffffffffffffffffffffffff), v2da
    0x2de: v2de(0x20) = CONST 
    0x2e1: v2e1(0x24) = ADD v2bc(0x4), v2de(0x20)
    0x2e2: v2e2 = CALLDATALOAD v2e1(0x24)
    0x2e5: v2e5 = AND v2d8(0xffffffffffffffffffffffffffffffffffffffff), v2e2
    0x2e7: v2e7(0x40) = CONST 
    0x2e9: v2e9(0x44) = ADD v2e7(0x40), v2bc(0x4)
    0x2ea: v2ea = CALLDATALOAD v2e9(0x44)
    0x2eb: v2eb(0xb8d) = CONST 
    0x2ef: JUMP v2eb(0xb8d)

    Begin block 0xb8d
    prev=[0x2cf], succ=[0xbb8, 0xbbc]
    =================================
    0xb8e: vb8e(0x1) = CONST 
    0xb90: vb90(0x1) = CONST 
    0xb92: vb92(0xa0) = CONST 
    0xb94: vb94(0x10000000000000000000000000000000000000000) = SHL vb92(0xa0), vb90(0x1)
    0xb95: vb95(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb94(0x10000000000000000000000000000000000000000), vb8e(0x1)
    0xb98: vb98 = AND vb95(0xffffffffffffffffffffffffffffffffffffffff), v2dc
    0xb99: vb99(0x0) = CONST 
    0xb9d: MSTORE vb99(0x0), vb98
    0xb9e: vb9e(0x3) = CONST 
    0xba0: vba0(0x20) = CONST 
    0xba2: MSTORE vba0(0x20), vb9e(0x3)
    0xba3: vba3(0x40) = CONST 
    0xba6: vba6 = SHA3 vb99(0x0), vba3(0x40)
    0xba7: vba7(0x9) = CONST 
    0xba9: vba9 = ADD vba7(0x9), vba6
    0xbaa: vbaa = SLOAD vba9
    0xbaf: vbaf = AND vb95(0xffffffffffffffffffffffffffffffffffffffff), v2e5
    0xbb1: vbb1 = AND vbaa, vb95(0xffffffffffffffffffffffffffffffffffffffff)
    0xbb2: vbb2 = EQ vbb1, vbaf
    0xbb3: vbb3(0xbbc) = CONST 
    0xbb7: JUMPI vbb3(0xbbc), vbb2

    Begin block 0xbb8
    prev=[0xb8d], succ=[]
    =================================
    0xbb8: vbb8(0x0) = CONST 
    0xbbb: REVERT vbb8(0x0), vbb8(0x0)

    Begin block 0xbbc
    prev=[0xb8d], succ=[0xbf8, 0xbfc]
    =================================
    0xbbd: vbbd(0x0) = CONST 
    0xbbf: vbbf(0xc4f) = CONST 
    0xbc4: vbc4(0x1) = CONST 
    0xbc6: vbc6(0x1) = CONST 
    0xbc8: vbc8(0xa0) = CONST 
    0xbca: vbca(0x10000000000000000000000000000000000000000) = SHL vbc8(0xa0), vbc6(0x1)
    0xbcb: vbcb(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbca(0x10000000000000000000000000000000000000000), vbc4(0x1)
    0xbcc: vbcc = AND vbcb(0xffffffffffffffffffffffffffffffffffffffff), v2e5
    0xbcd: vbcd(0x18160ddd) = CONST 
    0xbd2: vbd2(0x40) = CONST 
    0xbd4: vbd4 = MLOAD vbd2(0x40)
    0xbd6: vbd6(0xffffffff) = CONST 
    0xbdb: vbdb(0x18160ddd) = AND vbd6(0xffffffff), vbcd(0x18160ddd)
    0xbdc: vbdc(0xe0) = CONST 
    0xbde: vbde(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL vbdc(0xe0), vbdb(0x18160ddd)
    0xbe0: MSTORE vbd4, vbde(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0xbe1: vbe1(0x4) = CONST 
    0xbe3: vbe3 = ADD vbe1(0x4), vbd4
    0xbe4: vbe4(0x20) = CONST 
    0xbe6: vbe6(0x40) = CONST 
    0xbe8: vbe8 = MLOAD vbe6(0x40)
    0xbeb: vbeb(0x4) = SUB vbe3, vbe8
    0xbef: vbef = EXTCODESIZE vbcc
    0xbf0: vbf0 = ISZERO vbef
    0xbf2: vbf2 = ISZERO vbf0
    0xbf3: vbf3(0xbfc) = CONST 
    0xbf7: JUMPI vbf3(0xbfc), vbf2

    Begin block 0xbf8
    prev=[0xbbc], succ=[]
    =================================
    0xbf8: vbf8(0x0) = CONST 
    0xbfb: REVERT vbf8(0x0), vbf8(0x0)

    Begin block 0xbfc
    prev=[0xbbc], succ=[0xc08, 0xc11]
    =================================
    0xbfe: vbfe = GAS 
    0xbff: vbff = STATICCALL vbfe, vbcc, vbe8, vbeb(0x4), vbe8, vbe4(0x20)
    0xc00: vc00 = ISZERO vbff
    0xc02: vc02 = ISZERO vc00
    0xc03: vc03(0xc11) = CONST 
    0xc07: JUMPI vc03(0xc11), vc02

    Begin block 0xc08
    prev=[0xbfc], succ=[]
    =================================
    0xc08: vc08 = RETURNDATASIZE 
    0xc09: vc09(0x0) = CONST 
    0xc0c: RETURNDATACOPY vc09(0x0), vc09(0x0), vc08
    0xc0d: vc0d = RETURNDATASIZE 
    0xc0e: vc0e(0x0) = CONST 
    0xc10: REVERT vc0e(0x0), vc0d

    Begin block 0xc11
    prev=[0xbfc], succ=[0xc24, 0xc28]
    =================================
    0xc16: vc16(0x40) = CONST 
    0xc18: vc18 = MLOAD vc16(0x40)
    0xc19: vc19 = RETURNDATASIZE 
    0xc1a: vc1a(0x20) = CONST 
    0xc1d: vc1d = LT vc19, vc1a(0x20)
    0xc1e: vc1e = ISZERO vc1d
    0xc1f: vc1f(0xc28) = CONST 
    0xc23: JUMPI vc1f(0xc28), vc1e

    Begin block 0xc24
    prev=[0xc11], succ=[]
    =================================
    0xc24: vc24(0x0) = CONST 
    0xc27: REVERT vc24(0x0), vc24(0x0)

    Begin block 0xc28
    prev=[0xc11], succ=[0x3e20]
    =================================
    0xc2a: vc2a = MLOAD vc18
    0xc2b: vc2b(0x1) = CONST 
    0xc2d: vc2d(0x1) = CONST 
    0xc2f: vc2f(0xa0) = CONST 
    0xc31: vc31(0x10000000000000000000000000000000000000000) = SHL vc2f(0xa0), vc2d(0x1)
    0xc32: vc32(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc31(0x10000000000000000000000000000000000000000), vc2b(0x1)
    0xc34: vc34 = AND v2dc, vc32(0xffffffffffffffffffffffffffffffffffffffff)
    0xc35: vc35(0x0) = CONST 
    0xc39: MSTORE vc35(0x0), vc34
    0xc3a: vc3a(0x3) = CONST 
    0xc3c: vc3c(0x20) = CONST 
    0xc3e: MSTORE vc3c(0x20), vc3a(0x3)
    0xc3f: vc3f(0x40) = CONST 
    0xc42: vc42 = SHA3 vc35(0x0), vc3f(0x40)
    0xc43: vc43 = SLOAD vc42
    0xc44: vc44(0x3e20) = CONST 
    0xc4a: vc4a(0x1e23) = CONST 
    0xc4e: vc4e_0 = CALLPRIVATE vc4a(0x1e23), v2ea, vc43, vc44(0x3e20)

    Begin block 0x3e20
    prev=[0xc28], succ=[0x1e810x2a9]
    =================================
    0x3e22: v3e22(0x1e81) = CONST 
    0x3e26: JUMP v3e22(0x1e81)

    Begin block 0x1e810x2a9
    prev=[0x3e20], succ=[0x21200x2a9]
    =================================
    0x1e820x2a9: v2a91e82(0x0) = CONST 
    0x1e840x2a9: v2a91e84(0x4037) = CONST 
    0x1e8a0x2a9: v2a91e8a(0x40) = CONST 
    0x1e8c0x2a9: v2a91e8c = MLOAD v2a91e8a(0x40)
    0x1e8e0x2a9: v2a91e8e(0x40) = CONST 
    0x1e900x2a9: v2a91e90 = ADD v2a91e8e(0x40), v2a91e8c
    0x1e910x2a9: v2a91e91(0x40) = CONST 
    0x1e930x2a9: MSTORE v2a91e91(0x40), v2a91e90
    0x1e950x2a9: v2a91e95(0x1a) = CONST 
    0x1e980x2a9: MSTORE v2a91e8c, v2a91e95(0x1a)
    0x1e990x2a9: v2a91e99(0x20) = CONST 
    0x1e9b0x2a9: v2a91e9b = ADD v2a91e99(0x20), v2a91e8c
    0x1e9c0x2a9: v2a91e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1ebe0x2a9: MSTORE v2a91e9b, v2a91e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1ec00x2a9: v2a91ec0(0x2120) = CONST 
    0x1ec40x2a9: JUMP v2a91ec0(0x2120)

    Begin block 0x21200x2a9
    prev=[0x1e810x2a9], succ=[0x212a0x2a9, 0x21b00x2a9]
    =================================
    0x21210x2a9: v2a92121(0x0) = CONST 
    0x21250x2a9: v2a92125(0x21b0) = CONST 
    0x21290x2a9: JUMPI v2a92125(0x21b0), vc2a

    Begin block 0x212a0x2a9
    prev=[0x21200x2a9], succ=[0x215a0x2a9]
    =================================
    0x212a0x2a9: v2a9212a(0x40) = CONST 
    0x212c0x2a9: v2a9212c = MLOAD v2a9212a(0x40)
    0x212d0x2a9: v2a9212d(0x461bcd) = CONST 
    0x21310x2a9: v2a92131(0xe5) = CONST 
    0x21330x2a9: v2a92133(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2a92131(0xe5), v2a9212d(0x461bcd)
    0x21350x2a9: MSTORE v2a9212c, v2a92133(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21360x2a9: v2a92136(0x4) = CONST 
    0x21380x2a9: v2a92138 = ADD v2a92136(0x4), v2a9212c
    0x213b0x2a9: v2a9213b(0x20) = CONST 
    0x213d0x2a9: v2a9213d = ADD v2a9213b(0x20), v2a92138
    0x21400x2a9: v2a92140(0x20) = SUB v2a9213d, v2a92138
    0x21420x2a9: MSTORE v2a92138, v2a92140(0x20)
    0x21460x2a9: v2a92146(0x1a) = MLOAD v2a91e8c
    0x21480x2a9: MSTORE v2a9213d, v2a92146(0x1a)
    0x21490x2a9: v2a92149(0x20) = CONST 
    0x214b0x2a9: v2a9214b = ADD v2a92149(0x20), v2a9213d
    0x214f0x2a9: v2a9214f(0x1a) = MLOAD v2a91e8c
    0x21510x2a9: v2a92151(0x20) = CONST 
    0x21530x2a9: v2a92153 = ADD v2a92151(0x20), v2a91e8c
    0x21580x2a9: v2a92158(0x0) = CONST 

    Begin block 0x215a0x2a9
    prev=[0x212a0x2a9, 0x21640x2a9], succ=[0x21740x2a9, 0x21640x2a9]
    =================================
    0x215a0x2a9_0x0: v215a2a9_0 = PHI v2a9216e, v2a92158(0x0)
    0x215d0x2a9: v2a9215d = LT v215a2a9_0, v2a9214f(0x1a)
    0x215e0x2a9: v2a9215e = ISZERO v2a9215d
    0x215f0x2a9: v2a9215f(0x2174) = CONST 
    0x21630x2a9: JUMPI v2a9215f(0x2174), v2a9215e

    Begin block 0x21740x2a9
    prev=[0x215a0x2a9], succ=[0x21a20x2a9, 0x21890x2a9]
    =================================
    0x217d0x2a9: v2a9217d = ADD v2a9214f(0x1a), v2a9214b
    0x217f0x2a9: v2a9217f(0x1f) = CONST 
    0x21810x2a9: v2a92181(0x1a) = AND v2a9217f(0x1f), v2a9214f(0x1a)
    0x21830x2a9: v2a92183 = ISZERO v2a92181(0x1a)
    0x21840x2a9: v2a92184(0x21a2) = CONST 
    0x21880x2a9: JUMPI v2a92184(0x21a2), v2a92183

    Begin block 0x21a20x2a9
    prev=[0x21740x2a9, 0x21890x2a9], succ=[]
    =================================
    0x21a20x2a9_0x1: v21a22a9_1 = PHI v2a9219f, v2a9217d
    0x21a80x2a9: v2a921a8(0x40) = CONST 
    0x21aa0x2a9: v2a921aa = MLOAD v2a921a8(0x40)
    0x21ad0x2a9: v2a921ad = SUB v21a22a9_1, v2a921aa
    0x21af0x2a9: REVERT v2a921aa, v2a921ad

    Begin block 0x21890x2a9
    prev=[0x21740x2a9], succ=[0x21a20x2a9]
    =================================
    0x218b0x2a9: v2a9218b = SUB v2a9217d, v2a92181(0x1a)
    0x218d0x2a9: v2a9218d = MLOAD v2a9218b
    0x218e0x2a9: v2a9218e(0x1) = CONST 
    0x21910x2a9: v2a92191(0x20) = CONST 
    0x21930x2a9: v2a92193(0x6) = SUB v2a92191(0x20), v2a92181(0x1a)
    0x21940x2a9: v2a92194(0x100) = CONST 
    0x21970x2a9: v2a92197(0x1000000000000) = EXP v2a92194(0x100), v2a92193(0x6)
    0x21980x2a9: v2a92198(0xffffffffffff) = SUB v2a92197(0x1000000000000), v2a9218e(0x1)
    0x21990x2a9: v2a92199 = NOT v2a92198(0xffffffffffff)
    0x219a0x2a9: v2a9219a = AND v2a92199, v2a9218d
    0x219c0x2a9: MSTORE v2a9218b, v2a9219a
    0x219d0x2a9: v2a9219d(0x20) = CONST 
    0x219f0x2a9: v2a9219f = ADD v2a9219d(0x20), v2a9218b

    Begin block 0x21640x2a9
    prev=[0x215a0x2a9], succ=[0x215a0x2a9]
    =================================
    0x21640x2a9_0x0: v21642a9_0 = PHI v2a9216e, v2a92158(0x0)
    0x21660x2a9: v2a92166 = ADD v21642a9_0, v2a92153
    0x21670x2a9: v2a92167 = MLOAD v2a92166
    0x216a0x2a9: v2a9216a = ADD v21642a9_0, v2a9214b
    0x216b0x2a9: MSTORE v2a9216a, v2a92167
    0x216c0x2a9: v2a9216c(0x20) = CONST 
    0x216e0x2a9: v2a9216e = ADD v2a9216c(0x20), v21642a9_0
    0x216f0x2a9: v2a9216f(0x215a) = CONST 
    0x21730x2a9: JUMP v2a9216f(0x215a)

    Begin block 0x21b00x2a9
    prev=[0x21200x2a9], succ=[0x21bc0x2a9, 0x21bd0x2a9]
    =================================
    0x21b20x2a9: v2a921b2(0x0) = CONST 
    0x21b70x2a9: v2a921b7(0x21bd) = CONST 
    0x21bb0x2a9: JUMPI v2a921b7(0x21bd), vc2a

    Begin block 0x21bc0x2a9
    prev=[0x21b00x2a9], succ=[]
    =================================
    0x21bc0x2a9: THROW 

    Begin block 0x21bd0x2a9
    prev=[0x21b00x2a9], succ=[0x40370x2a9]
    =================================
    0x21be0x2a9: v2a921be = DIV vc4e_0, vc2a
    0x21c60x2a9: JUMP v2a91e84(0x4037)

    Begin block 0x40370x2a9
    prev=[0x21bd0x2a9], succ=[0xc4f]
    =================================
    0x403d0x2a9: JUMP vbbf(0xc4f)

    Begin block 0xc4f
    prev=[0x40370x2a9], succ=[0xc53]
    =================================

    Begin block 0xc53
    prev=[0xc4f], succ=[0x3a85]
    =================================
    0xc59: JUMP v2b8(0x3a85)

    Begin block 0x3a85
    prev=[0xc53], succ=[]
    =================================
    0x3a86: v3a86(0x40) = CONST 
    0x3a89: v3a89 = MLOAD v3a86(0x40)
    0x3a8c: MSTORE v3a89, v2a921be
    0x3a8d: v3a8d = MLOAD v3a86(0x40)
    0x3a91: v3a91(0x0) = SUB v3a89, v3a8d
    0x3a92: v3a92(0x20) = CONST 
    0x3a94: v3a94(0x20) = ADD v3a92(0x20), v3a91(0x0)
    0x3a96: RETURN v3a8d, v3a94(0x20)

}

function updateCode(address)() public {
    Begin block 0x302
    prev=[], succ=[0x30b, 0x30f]
    =================================
    0x303: v303 = CALLVALUE 
    0x305: v305 = ISZERO v303
    0x306: v306(0x30f) = CONST 
    0x30a: JUMPI v306(0x30f), v305

    Begin block 0x30b
    prev=[0x302], succ=[]
    =================================
    0x30b: v30b(0x0) = CONST 
    0x30e: REVERT v30b(0x0), v30b(0x0)

    Begin block 0x30f
    prev=[0x302], succ=[0x324, 0x328]
    =================================
    0x311: v311(0x3ab6) = CONST 
    0x315: v315(0x4) = CONST 
    0x318: v318 = CALLDATASIZE 
    0x319: v319 = SUB v318, v315(0x4)
    0x31a: v31a(0x20) = CONST 
    0x31d: v31d = LT v319, v31a(0x20)
    0x31e: v31e = ISZERO v31d
    0x31f: v31f(0x328) = CONST 
    0x323: JUMPI v31f(0x328), v31e

    Begin block 0x324
    prev=[0x30f], succ=[]
    =================================
    0x324: v324(0x0) = CONST 
    0x327: REVERT v324(0x0), v324(0x0)

    Begin block 0x328
    prev=[0x30f], succ=[0xc5a]
    =================================
    0x32a: v32a = CALLDATALOAD v315(0x4)
    0x32b: v32b(0x1) = CONST 
    0x32d: v32d(0x1) = CONST 
    0x32f: v32f(0xa0) = CONST 
    0x331: v331(0x10000000000000000000000000000000000000000) = SHL v32f(0xa0), v32d(0x1)
    0x332: v332(0xffffffffffffffffffffffffffffffffffffffff) = SUB v331(0x10000000000000000000000000000000000000000), v32b(0x1)
    0x333: v333 = AND v332(0xffffffffffffffffffffffffffffffffffffffff), v32a
    0x334: v334(0xc5a) = CONST 
    0x338: JUMP v334(0xc5a)

    Begin block 0xc5a
    prev=[0x328], succ=[0xc6b, 0xca2]
    =================================
    0xc5b: vc5b(0x0) = CONST 
    0xc5d: vc5d = SLOAD vc5b(0x0)
    0xc5e: vc5e(0xff) = CONST 
    0xc60: vc60 = AND vc5e(0xff), vc5d
    0xc61: vc61 = ISZERO vc60
    0xc62: vc62 = ISZERO vc61
    0xc63: vc63(0x1) = CONST 
    0xc65: vc65 = EQ vc63(0x1), vc62
    0xc66: vc66(0xca2) = CONST 
    0xc6a: JUMPI vc66(0xca2), vc65

    Begin block 0xc6b
    prev=[0xc5a], succ=[]
    =================================
    0xc6b: vc6b(0x40) = CONST 
    0xc6d: vc6d = MLOAD vc6b(0x40)
    0xc6e: vc6e(0x461bcd) = CONST 
    0xc72: vc72(0xe5) = CONST 
    0xc74: vc74(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vc72(0xe5), vc6e(0x461bcd)
    0xc76: MSTORE vc6d, vc74(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc77: vc77(0x4) = CONST 
    0xc79: vc79 = ADD vc77(0x4), vc6d
    0xc7c: vc7c(0x20) = CONST 
    0xc7e: vc7e = ADD vc7c(0x20), vc79
    0xc81: vc81(0x20) = SUB vc7e, vc79
    0xc83: MSTORE vc79, vc81(0x20)
    0xc84: vc84(0x32) = CONST 
    0xc87: MSTORE vc7e, vc84(0x32)
    0xc88: vc88(0x20) = CONST 
    0xc8a: vc8a = ADD vc88(0x20), vc7e
    0xc8c: vc8c(0x37d5) = CONST 
    0xc90: vc90(0x32) = CONST 
    0xc93: CODECOPY vc8a, vc8c(0x37d5), vc90(0x32)
    0xc94: vc94(0x40) = CONST 
    0xc96: vc96 = ADD vc94(0x40), vc8a
    0xc9a: vc9a(0x40) = CONST 
    0xc9c: vc9c = MLOAD vc9a(0x40)
    0xc9f: vc9f(0x84) = SUB vc96, vc9c
    0xca1: REVERT vc9c, vc9f(0x84)

    Begin block 0xca2
    prev=[0xc5a], succ=[0xcb9, 0xcd6]
    =================================
    0xca3: vca3(0x0) = CONST 
    0xca5: vca5 = SLOAD vca3(0x0)
    0xca6: vca6(0x100) = CONST 
    0xcaa: vcaa = DIV vca5, vca6(0x100)
    0xcab: vcab(0x1) = CONST 
    0xcad: vcad(0x1) = CONST 
    0xcaf: vcaf(0xa0) = CONST 
    0xcb1: vcb1(0x10000000000000000000000000000000000000000) = SHL vcaf(0xa0), vcad(0x1)
    0xcb2: vcb2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcb1(0x10000000000000000000000000000000000000000), vcab(0x1)
    0xcb3: vcb3 = AND vcb2(0xffffffffffffffffffffffffffffffffffffffff), vcaa
    0xcb4: vcb4(0xcd6) = CONST 
    0xcb8: JUMPI vcb4(0xcd6), vcb3

    Begin block 0xcb9
    prev=[0xca2], succ=[0xccc, 0xcd0]
    =================================
    0xcb9: vcb9(0xb) = CONST 
    0xcbb: vcbb = SLOAD vcb9(0xb)
    0xcbc: vcbc(0x1) = CONST 
    0xcbe: vcbe(0x1) = CONST 
    0xcc0: vcc0(0xa0) = CONST 
    0xcc2: vcc2(0x10000000000000000000000000000000000000000) = SHL vcc0(0xa0), vcbe(0x1)
    0xcc3: vcc3(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcc2(0x10000000000000000000000000000000000000000), vcbc(0x1)
    0xcc4: vcc4 = AND vcc3(0xffffffffffffffffffffffffffffffffffffffff), vcbb
    0xcc5: vcc5 = CALLER 
    0xcc6: vcc6 = EQ vcc5, vcc4
    0xcc7: vcc7(0xcd0) = CONST 
    0xccb: JUMPI vcc7(0xcd0), vcc6

    Begin block 0xccc
    prev=[0xcb9], succ=[]
    =================================
    0xccc: vccc(0x0) = CONST 
    0xccf: REVERT vccc(0x0), vccc(0x0)

    Begin block 0xcd0
    prev=[0xcb9], succ=[0xcf3]
    =================================
    0xcd1: vcd1(0xcf3) = CONST 
    0xcd5: JUMP vcd1(0xcf3)

    Begin block 0xcf3
    prev=[0xcd6, 0xcd0], succ=[0x1f09]
    =================================
    0xcf4: vcf4(0x3e46) = CONST 
    0xcf9: vcf9(0x1f09) = CONST 
    0xcfd: JUMP vcf9(0x1f09)

    Begin block 0x1f09
    prev=[0xcf3], succ=[0x1f3f, 0x1f43]
    =================================
    0x1f0b: v1f0b(0x1) = CONST 
    0x1f0d: v1f0d(0x1) = CONST 
    0x1f0f: v1f0f(0xa0) = CONST 
    0x1f11: v1f11(0x10000000000000000000000000000000000000000) = SHL v1f0f(0xa0), v1f0d(0x1)
    0x1f12: v1f12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f11(0x10000000000000000000000000000000000000000), v1f0b(0x1)
    0x1f13: v1f13 = AND v1f12(0xffffffffffffffffffffffffffffffffffffffff), v333
    0x1f14: v1f14(0x52d1902d) = CONST 
    0x1f19: v1f19(0x40) = CONST 
    0x1f1b: v1f1b = MLOAD v1f19(0x40)
    0x1f1d: v1f1d(0xffffffff) = CONST 
    0x1f22: v1f22(0x52d1902d) = AND v1f1d(0xffffffff), v1f14(0x52d1902d)
    0x1f23: v1f23(0xe0) = CONST 
    0x1f25: v1f25(0x52d1902d00000000000000000000000000000000000000000000000000000000) = SHL v1f23(0xe0), v1f22(0x52d1902d)
    0x1f27: MSTORE v1f1b, v1f25(0x52d1902d00000000000000000000000000000000000000000000000000000000)
    0x1f28: v1f28(0x4) = CONST 
    0x1f2a: v1f2a = ADD v1f28(0x4), v1f1b
    0x1f2b: v1f2b(0x20) = CONST 
    0x1f2d: v1f2d(0x40) = CONST 
    0x1f2f: v1f2f = MLOAD v1f2d(0x40)
    0x1f32: v1f32(0x4) = SUB v1f2a, v1f2f
    0x1f36: v1f36 = EXTCODESIZE v1f13
    0x1f37: v1f37 = ISZERO v1f36
    0x1f39: v1f39 = ISZERO v1f37
    0x1f3a: v1f3a(0x1f43) = CONST 
    0x1f3e: JUMPI v1f3a(0x1f43), v1f39

    Begin block 0x1f3f
    prev=[0x1f09], succ=[]
    =================================
    0x1f3f: v1f3f(0x0) = CONST 
    0x1f42: REVERT v1f3f(0x0), v1f3f(0x0)

    Begin block 0x1f43
    prev=[0x1f09], succ=[0x1f4f, 0x1f58]
    =================================
    0x1f45: v1f45 = GAS 
    0x1f46: v1f46 = STATICCALL v1f45, v1f13, v1f2f, v1f32(0x4), v1f2f, v1f2b(0x20)
    0x1f47: v1f47 = ISZERO v1f46
    0x1f49: v1f49 = ISZERO v1f47
    0x1f4a: v1f4a(0x1f58) = CONST 
    0x1f4e: JUMPI v1f4a(0x1f58), v1f49

    Begin block 0x1f4f
    prev=[0x1f43], succ=[]
    =================================
    0x1f4f: v1f4f = RETURNDATASIZE 
    0x1f50: v1f50(0x0) = CONST 
    0x1f53: RETURNDATACOPY v1f50(0x0), v1f50(0x0), v1f4f
    0x1f54: v1f54 = RETURNDATASIZE 
    0x1f55: v1f55(0x0) = CONST 
    0x1f57: REVERT v1f55(0x0), v1f54

    Begin block 0x1f58
    prev=[0x1f43], succ=[0x1f6b, 0x1f6f]
    =================================
    0x1f5d: v1f5d(0x40) = CONST 
    0x1f5f: v1f5f = MLOAD v1f5d(0x40)
    0x1f60: v1f60 = RETURNDATASIZE 
    0x1f61: v1f61(0x20) = CONST 
    0x1f64: v1f64 = LT v1f60, v1f61(0x20)
    0x1f65: v1f65 = ISZERO v1f64
    0x1f66: v1f66(0x1f6f) = CONST 
    0x1f6a: JUMPI v1f66(0x1f6f), v1f65

    Begin block 0x1f6b
    prev=[0x1f58], succ=[]
    =================================
    0x1f6b: v1f6b(0x0) = CONST 
    0x1f6e: REVERT v1f6b(0x0), v1f6b(0x0)

    Begin block 0x1f6f
    prev=[0x1f58], succ=[0x1f99, 0x1fd6]
    =================================
    0x1f71: v1f71 = MLOAD v1f5f
    0x1f72: v1f72(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x1f93: v1f93 = EQ v1f72(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7), v1f71
    0x1f94: v1f94(0x1fd6) = CONST 
    0x1f98: JUMPI v1f94(0x1fd6), v1f93

    Begin block 0x1f99
    prev=[0x1f6f], succ=[]
    =================================
    0x1f99: v1f99(0x40) = CONST 
    0x1f9c: v1f9c = MLOAD v1f99(0x40)
    0x1f9d: v1f9d(0x461bcd) = CONST 
    0x1fa1: v1fa1(0xe5) = CONST 
    0x1fa3: v1fa3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1fa1(0xe5), v1f9d(0x461bcd)
    0x1fa5: MSTORE v1f9c, v1fa3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1fa6: v1fa6(0x20) = CONST 
    0x1fa8: v1fa8(0x4) = CONST 
    0x1fab: v1fab = ADD v1f9c, v1fa8(0x4)
    0x1fac: MSTORE v1fab, v1fa6(0x20)
    0x1fad: v1fad(0xe) = CONST 
    0x1faf: v1faf(0x24) = CONST 
    0x1fb2: v1fb2 = ADD v1f9c, v1faf(0x24)
    0x1fb3: MSTORE v1fb2, v1fad(0xe)
    0x1fb4: v1fb4(0x4e6f7420636f6d70617469626c65) = CONST 
    0x1fc3: v1fc3(0x90) = CONST 
    0x1fc5: v1fc5(0x4e6f7420636f6d70617469626c65000000000000000000000000000000000000) = SHL v1fc3(0x90), v1fb4(0x4e6f7420636f6d70617469626c65)
    0x1fc6: v1fc6(0x44) = CONST 
    0x1fc9: v1fc9 = ADD v1f9c, v1fc6(0x44)
    0x1fca: MSTORE v1fc9, v1fc5(0x4e6f7420636f6d70617469626c65000000000000000000000000000000000000)
    0x1fcc: v1fcc = MLOAD v1f99(0x40)
    0x1fd0: v1fd0(0x0) = SUB v1f9c, v1fcc
    0x1fd1: v1fd1(0x64) = CONST 
    0x1fd3: v1fd3(0x64) = ADD v1fd1(0x64), v1fd0(0x0)
    0x1fd5: REVERT v1fcc, v1fd3(0x64)

    Begin block 0x1fd6
    prev=[0x1f6f], succ=[0x3e46]
    =================================
    0x1fd7: v1fd7(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x1ff8: SSTORE v1fd7(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7), v333
    0x1ff9: JUMP vcf4(0x3e46)

    Begin block 0x3e46
    prev=[0x1fd6], succ=[0x3ab6]
    =================================
    0x3e48: JUMP v311(0x3ab6)

    Begin block 0x3ab6
    prev=[0x3e46], succ=[]
    =================================
    0x3ab7: STOP 

    Begin block 0xcd6
    prev=[0xca2], succ=[0xcef, 0xcf3]
    =================================
    0xcd7: vcd7(0x0) = CONST 
    0xcd9: vcd9 = SLOAD vcd7(0x0)
    0xcda: vcda(0x100) = CONST 
    0xcde: vcde = DIV vcd9, vcda(0x100)
    0xcdf: vcdf(0x1) = CONST 
    0xce1: vce1(0x1) = CONST 
    0xce3: vce3(0xa0) = CONST 
    0xce5: vce5(0x10000000000000000000000000000000000000000) = SHL vce3(0xa0), vce1(0x1)
    0xce6: vce6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vce5(0x10000000000000000000000000000000000000000), vcdf(0x1)
    0xce7: vce7 = AND vce6(0xffffffffffffffffffffffffffffffffffffffff), vcde
    0xce8: vce8 = CALLER 
    0xce9: vce9 = EQ vce8, vce7
    0xcea: vcea(0xcf3) = CONST 
    0xcee: JUMPI vcea(0xcf3), vce9

    Begin block 0xcef
    prev=[0xcd6], succ=[]
    =================================
    0xcef: vcef(0x0) = CONST 
    0xcf2: REVERT vcef(0x0), vcef(0x0)

}

function proxiableUUID()() public {
    Begin block 0x339
    prev=[], succ=[0x342, 0x346]
    =================================
    0x33a: v33a = CALLVALUE 
    0x33c: v33c = ISZERO v33a
    0x33d: v33d(0x346) = CONST 
    0x341: JUMPI v33d(0x346), v33c

    Begin block 0x342
    prev=[0x339], succ=[]
    =================================
    0x342: v342(0x0) = CONST 
    0x345: REVERT v342(0x0), v342(0x0)

    Begin block 0x346
    prev=[0x339], succ=[0xd01]
    =================================
    0x348: v348(0x3ad7) = CONST 
    0x34c: v34c(0xd01) = CONST 
    0x350: JUMP v34c(0xd01)

    Begin block 0xd01
    prev=[0x346], succ=[0x3ad7]
    =================================
    0xd02: vd02(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0xd24: JUMP v348(0x3ad7)

    Begin block 0x3ad7
    prev=[0xd01], succ=[]
    =================================
    0x3ad8: v3ad8(0x40) = CONST 
    0x3adb: v3adb = MLOAD v3ad8(0x40)
    0x3ade: MSTORE v3adb, vd02(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x3adf: v3adf = MLOAD v3ad8(0x40)
    0x3ae3: v3ae3(0x0) = SUB v3adb, v3adf
    0x3ae4: v3ae4(0x20) = CONST 
    0x3ae6: v3ae6(0x20) = ADD v3ae4(0x20), v3ae3(0x0)
    0x3ae8: RETURN v3adf, v3ae6(0x20)

}

function setContracts(address)() public {
    Begin block 0x351
    prev=[], succ=[0x35a, 0x35e]
    =================================
    0x352: v352 = CALLVALUE 
    0x354: v354 = ISZERO v352
    0x355: v355(0x35e) = CONST 
    0x359: JUMPI v355(0x35e), v354

    Begin block 0x35a
    prev=[0x351], succ=[]
    =================================
    0x35a: v35a(0x0) = CONST 
    0x35d: REVERT v35a(0x0), v35a(0x0)

    Begin block 0x35e
    prev=[0x351], succ=[0x373, 0x377]
    =================================
    0x360: v360(0x3b08) = CONST 
    0x364: v364(0x4) = CONST 
    0x367: v367 = CALLDATASIZE 
    0x368: v368 = SUB v367, v364(0x4)
    0x369: v369(0x20) = CONST 
    0x36c: v36c = LT v368, v369(0x20)
    0x36d: v36d = ISZERO v36c
    0x36e: v36e(0x377) = CONST 
    0x372: JUMPI v36e(0x377), v36d

    Begin block 0x373
    prev=[0x35e], succ=[]
    =================================
    0x373: v373(0x0) = CONST 
    0x376: REVERT v373(0x0), v373(0x0)

    Begin block 0x377
    prev=[0x35e], succ=[0xd25]
    =================================
    0x379: v379 = CALLDATALOAD v364(0x4)
    0x37a: v37a(0x1) = CONST 
    0x37c: v37c(0x1) = CONST 
    0x37e: v37e(0xa0) = CONST 
    0x380: v380(0x10000000000000000000000000000000000000000) = SHL v37e(0xa0), v37c(0x1)
    0x381: v381(0xffffffffffffffffffffffffffffffffffffffff) = SUB v380(0x10000000000000000000000000000000000000000), v37a(0x1)
    0x382: v382 = AND v381(0xffffffffffffffffffffffffffffffffffffffff), v379
    0x383: v383(0xd25) = CONST 
    0x387: JUMP v383(0xd25)

    Begin block 0xd25
    prev=[0x377], succ=[0xd36, 0xd6d]
    =================================
    0xd26: vd26(0x0) = CONST 
    0xd28: vd28 = SLOAD vd26(0x0)
    0xd29: vd29(0xff) = CONST 
    0xd2b: vd2b = AND vd29(0xff), vd28
    0xd2c: vd2c = ISZERO vd2b
    0xd2d: vd2d = ISZERO vd2c
    0xd2e: vd2e(0x1) = CONST 
    0xd30: vd30 = EQ vd2e(0x1), vd2d
    0xd31: vd31(0xd6d) = CONST 
    0xd35: JUMPI vd31(0xd6d), vd30

    Begin block 0xd36
    prev=[0xd25], succ=[]
    =================================
    0xd36: vd36(0x40) = CONST 
    0xd38: vd38 = MLOAD vd36(0x40)
    0xd39: vd39(0x461bcd) = CONST 
    0xd3d: vd3d(0xe5) = CONST 
    0xd3f: vd3f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vd3d(0xe5), vd39(0x461bcd)
    0xd41: MSTORE vd38, vd3f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd42: vd42(0x4) = CONST 
    0xd44: vd44 = ADD vd42(0x4), vd38
    0xd47: vd47(0x20) = CONST 
    0xd49: vd49 = ADD vd47(0x20), vd44
    0xd4c: vd4c(0x20) = SUB vd49, vd44
    0xd4e: MSTORE vd44, vd4c(0x20)
    0xd4f: vd4f(0x32) = CONST 
    0xd52: MSTORE vd49, vd4f(0x32)
    0xd53: vd53(0x20) = CONST 
    0xd55: vd55 = ADD vd53(0x20), vd49
    0xd57: vd57(0x37d5) = CONST 
    0xd5b: vd5b(0x32) = CONST 
    0xd5e: CODECOPY vd55, vd57(0x37d5), vd5b(0x32)
    0xd5f: vd5f(0x40) = CONST 
    0xd61: vd61 = ADD vd5f(0x40), vd55
    0xd65: vd65(0x40) = CONST 
    0xd67: vd67 = MLOAD vd65(0x40)
    0xd6a: vd6a(0x84) = SUB vd61, vd67
    0xd6c: REVERT vd67, vd6a(0x84)

    Begin block 0xd6d
    prev=[0xd25], succ=[0xd86, 0xd8a]
    =================================
    0xd6e: vd6e(0x0) = CONST 
    0xd70: vd70 = SLOAD vd6e(0x0)
    0xd71: vd71(0x100) = CONST 
    0xd75: vd75 = DIV vd70, vd71(0x100)
    0xd76: vd76(0x1) = CONST 
    0xd78: vd78(0x1) = CONST 
    0xd7a: vd7a(0xa0) = CONST 
    0xd7c: vd7c(0x10000000000000000000000000000000000000000) = SHL vd7a(0xa0), vd78(0x1)
    0xd7d: vd7d(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd7c(0x10000000000000000000000000000000000000000), vd76(0x1)
    0xd7e: vd7e = AND vd7d(0xffffffffffffffffffffffffffffffffffffffff), vd75
    0xd7f: vd7f = CALLER 
    0xd80: vd80 = EQ vd7f, vd7e
    0xd81: vd81(0xd8a) = CONST 
    0xd85: JUMPI vd81(0xd8a), vd80

    Begin block 0xd86
    prev=[0xd6d], succ=[]
    =================================
    0xd86: vd86(0x0) = CONST 
    0xd89: REVERT vd86(0x0), vd86(0x0)

    Begin block 0xd8a
    prev=[0xd6d], succ=[0x3b08]
    =================================
    0xd8b: vd8b(0xb) = CONST 
    0xd8e: vd8e = SLOAD vd8b(0xb)
    0xd8f: vd8f(0x1) = CONST 
    0xd91: vd91(0x1) = CONST 
    0xd93: vd93(0xa0) = CONST 
    0xd95: vd95(0x10000000000000000000000000000000000000000) = SHL vd93(0xa0), vd91(0x1)
    0xd96: vd96(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd95(0x10000000000000000000000000000000000000000), vd8f(0x1)
    0xd99: vd99 = AND v382, vd96(0xffffffffffffffffffffffffffffffffffffffff)
    0xd9a: vd9a(0x1) = CONST 
    0xd9c: vd9c(0x1) = CONST 
    0xd9e: vd9e(0xa0) = CONST 
    0xda0: vda0(0x10000000000000000000000000000000000000000) = SHL vd9e(0xa0), vd9c(0x1)
    0xda1: vda1(0xffffffffffffffffffffffffffffffffffffffff) = SUB vda0(0x10000000000000000000000000000000000000000), vd9a(0x1)
    0xda2: vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT vda1(0xffffffffffffffffffffffffffffffffffffffff)
    0xda5: vda5 = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vd8e
    0xda6: vda6 = OR vda5, vd99
    0xda8: SSTORE vd8b(0xb), vda6
    0xda9: vda9(0x5) = CONST 
    0xdac: vdac = SLOAD vda9(0x5)
    0xdae: vdae = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdac
    0xdaf: vdaf(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac5) = CONST 
    0xdc4: vdc4 = OR vdaf(0x2c9728ad35c1cfb16e3c1b5045bc9ba30f37fac5), vdae
    0xdc6: SSTORE vda9(0x5), vdc4
    0xdc7: vdc7(0x6) = CONST 
    0xdca: vdca = SLOAD vdc7(0x6)
    0xdcc: vdcc = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdca
    0xdcd: vdcd(0x60d70df1c783b1e5489721c443465684e2756555) = CONST 
    0xde2: vde2 = OR vdcd(0x60d70df1c783b1e5489721c443465684e2756555), vdcc
    0xde4: SSTORE vdc7(0x6), vde2
    0xde5: vde5(0x7) = CONST 
    0xde8: vde8 = SLOAD vde5(0x7)
    0xdea: vdea = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vde8
    0xdeb: vdeb(0x66bfd3ed6618d9c62dcf1ef706d9aacd5fdbccd6) = CONST 
    0xe00: ve00 = OR vdeb(0x66bfd3ed6618d9c62dcf1ef706d9aacd5fdbccd6), vdea
    0xe02: SSTORE vde5(0x7), ve00
    0xe03: ve03(0x8) = CONST 
    0xe06: ve06 = SLOAD ve03(0x8)
    0xe08: ve08 = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), ve06
    0xe09: ve09(0x868f7622f57b62330db8b282044d7eaf067facfe) = CONST 
    0xe1e: ve1e = OR ve09(0x868f7622f57b62330db8b282044d7eaf067facfe), ve08
    0xe20: SSTORE ve03(0x8), ve1e
    0xe21: ve21(0x9) = CONST 
    0xe24: ve24 = SLOAD ve21(0x9)
    0xe26: ve26 = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), ve24
    0xe27: ve27(0xd66a9d2b706e225204f475c9e70a4c09eea62199) = CONST 
    0xe3c: ve3c = OR ve27(0xd66a9d2b706e225204f475c9e70a4c09eea62199), ve26
    0xe3e: SSTORE ve21(0x9), ve3c
    0xe3f: ve3f(0xa) = CONST 
    0xe42: ve42 = SLOAD ve3f(0xa)
    0xe45: ve45 = AND vda2(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), ve42
    0xe46: ve46(0x74a9ec513bc45bd04769fdf7a502e9c2a39e2d0e) = CONST 
    0xe5b: ve5b = OR ve46(0x74a9ec513bc45bd04769fdf7a502e9c2a39e2d0e), ve45
    0xe5d: SSTORE ve3f(0xa), ve5b
    0xe5e: JUMP v360(0x3b08)

    Begin block 0x3b08
    prev=[0xd8a], succ=[]
    =================================
    0x3b09: STOP 

}

function checkManagerAllowance(address,uint256)() public {
    Begin block 0x388
    prev=[], succ=[0x391, 0x395]
    =================================
    0x389: v389 = CALLVALUE 
    0x38b: v38b = ISZERO v389
    0x38c: v38c(0x395) = CONST 
    0x390: JUMPI v38c(0x395), v38b

    Begin block 0x391
    prev=[0x388], succ=[]
    =================================
    0x391: v391(0x0) = CONST 
    0x394: REVERT v391(0x0), v391(0x0)

    Begin block 0x395
    prev=[0x388], succ=[0x3aa, 0x3ae]
    =================================
    0x397: v397(0x3b29) = CONST 
    0x39b: v39b(0x4) = CONST 
    0x39e: v39e = CALLDATASIZE 
    0x39f: v39f = SUB v39e, v39b(0x4)
    0x3a0: v3a0(0x40) = CONST 
    0x3a3: v3a3 = LT v39f, v3a0(0x40)
    0x3a4: v3a4 = ISZERO v3a3
    0x3a5: v3a5(0x3ae) = CONST 
    0x3a9: JUMPI v3a5(0x3ae), v3a4

    Begin block 0x3aa
    prev=[0x395], succ=[]
    =================================
    0x3aa: v3aa(0x0) = CONST 
    0x3ad: REVERT v3aa(0x0), v3aa(0x0)

    Begin block 0x3ae
    prev=[0x395], succ=[0xe5f]
    =================================
    0x3b0: v3b0(0x1) = CONST 
    0x3b2: v3b2(0x1) = CONST 
    0x3b4: v3b4(0xa0) = CONST 
    0x3b6: v3b6(0x10000000000000000000000000000000000000000) = SHL v3b4(0xa0), v3b2(0x1)
    0x3b7: v3b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b6(0x10000000000000000000000000000000000000000), v3b0(0x1)
    0x3b9: v3b9 = CALLDATALOAD v39b(0x4)
    0x3ba: v3ba = AND v3b9, v3b7(0xffffffffffffffffffffffffffffffffffffffff)
    0x3bc: v3bc(0x20) = CONST 
    0x3be: v3be(0x24) = ADD v3bc(0x20), v39b(0x4)
    0x3bf: v3bf = CALLDATALOAD v3be(0x24)
    0x3c0: v3c0(0xe5f) = CONST 
    0x3c4: JUMP v3c0(0xe5f)

    Begin block 0xe5f
    prev=[0x3ae], succ=[0xe76, 0xe7a]
    =================================
    0xe60: ve60(0x7) = CONST 
    0xe62: ve62 = SLOAD ve60(0x7)
    0xe63: ve63(0x0) = CONST 
    0xe66: ve66(0x1) = CONST 
    0xe68: ve68(0x1) = CONST 
    0xe6a: ve6a(0xa0) = CONST 
    0xe6c: ve6c(0x10000000000000000000000000000000000000000) = SHL ve6a(0xa0), ve68(0x1)
    0xe6d: ve6d(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve6c(0x10000000000000000000000000000000000000000), ve66(0x1)
    0xe6e: ve6e = AND ve6d(0xffffffffffffffffffffffffffffffffffffffff), ve62
    0xe6f: ve6f = CALLER 
    0xe70: ve70 = EQ ve6f, ve6e
    0xe71: ve71(0xe7a) = CONST 
    0xe75: JUMPI ve71(0xe7a), ve70

    Begin block 0xe76
    prev=[0xe5f], succ=[]
    =================================
    0xe76: ve76(0x0) = CONST 
    0xe79: REVERT ve76(0x0), ve76(0x0)

    Begin block 0xe7a
    prev=[0xe5f], succ=[0xe9c, 0xee8]
    =================================
    0xe7b: ve7b(0x1) = CONST 
    0xe7d: ve7d(0x1) = CONST 
    0xe7f: ve7f(0xa0) = CONST 
    0xe81: ve81(0x10000000000000000000000000000000000000000) = SHL ve7f(0xa0), ve7d(0x1)
    0xe82: ve82(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve81(0x10000000000000000000000000000000000000000), ve7b(0x1)
    0xe84: ve84 = AND v3ba, ve82(0xffffffffffffffffffffffffffffffffffffffff)
    0xe85: ve85(0x0) = CONST 
    0xe89: MSTORE ve85(0x0), ve84
    0xe8a: ve8a(0x3) = CONST 
    0xe8c: ve8c(0x20) = CONST 
    0xe8e: MSTORE ve8c(0x20), ve8a(0x3)
    0xe8f: ve8f(0x40) = CONST 
    0xe92: ve92 = SHA3 ve85(0x0), ve8f(0x40)
    0xe93: ve93 = SLOAD ve92
    0xe95: ve95 = GT v3bf, ve93
    0xe96: ve96 = ISZERO ve95
    0xe97: ve97(0xee8) = CONST 
    0xe9b: JUMPI ve97(0xee8), ve96

    Begin block 0xe9c
    prev=[0xe7a], succ=[]
    =================================
    0xe9c: ve9c(0x40) = CONST 
    0xe9f: ve9f = MLOAD ve9c(0x40)
    0xea0: vea0(0x461bcd) = CONST 
    0xea4: vea4(0xe5) = CONST 
    0xea6: vea6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vea4(0xe5), vea0(0x461bcd)
    0xea8: MSTORE ve9f, vea6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xea9: vea9(0x20) = CONST 
    0xeab: veab(0x4) = CONST 
    0xeae: veae = ADD ve9f, veab(0x4)
    0xeaf: MSTORE veae, vea9(0x20)
    0xeb0: veb0(0x1e) = CONST 
    0xeb2: veb2(0x24) = CONST 
    0xeb5: veb5 = ADD ve9f, veb2(0x24)
    0xeb6: MSTORE veb5, veb0(0x1e)
    0xeb7: veb7(0x4d616e616765723a20496e73756666696369656e7420686f6c64696e67730000) = CONST 
    0xed8: ved8(0x44) = CONST 
    0xedb: vedb = ADD ve9f, ved8(0x44)
    0xedc: MSTORE vedb, veb7(0x4d616e616765723a20496e73756666696369656e7420686f6c64696e67730000)
    0xede: vede = MLOAD ve9c(0x40)
    0xee2: vee2(0x0) = SUB ve9f, vede
    0xee3: vee3(0x64) = CONST 
    0xee5: vee5(0x64) = ADD vee3(0x64), vee2(0x0)
    0xee7: REVERT vede, vee5(0x64)

    Begin block 0xee8
    prev=[0xe7a], succ=[0xf0d]
    =================================
    0xee9: vee9(0x1) = CONST 
    0xeeb: veeb(0x1) = CONST 
    0xeed: veed(0xa0) = CONST 
    0xeef: veef(0x10000000000000000000000000000000000000000) = SHL veed(0xa0), veeb(0x1)
    0xef0: vef0(0xffffffffffffffffffffffffffffffffffffffff) = SUB veef(0x10000000000000000000000000000000000000000), vee9(0x1)
    0xef2: vef2 = AND v3ba, vef0(0xffffffffffffffffffffffffffffffffffffffff)
    0xef3: vef3(0x0) = CONST 
    0xef7: MSTORE vef3(0x0), vef2
    0xef8: vef8(0x3) = CONST 
    0xefa: vefa(0x20) = CONST 
    0xefc: MSTORE vefa(0x20), vef8(0x3)
    0xefd: vefd(0x40) = CONST 
    0xf00: vf00 = SHA3 vef3(0x0), vefd(0x40)
    0xf01: vf01 = SLOAD vf00
    0xf02: vf02(0xf0d) = CONST 
    0xf08: vf08(0x1ec5) = CONST 
    0xf0c: vf0c_0 = CALLPRIVATE vf08(0x1ec5), v3bf, vf01, vf02(0xf0d)

    Begin block 0xf0d
    prev=[0xee8], succ=[0xf450x388]
    =================================
    0xf0e: vf0e(0x1) = CONST 
    0xf10: vf10(0x1) = CONST 
    0xf12: vf12(0xa0) = CONST 
    0xf14: vf14(0x10000000000000000000000000000000000000000) = SHL vf12(0xa0), vf10(0x1)
    0xf15: vf15(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf14(0x10000000000000000000000000000000000000000), vf0e(0x1)
    0xf17: vf17 = AND v3ba, vf15(0xffffffffffffffffffffffffffffffffffffffff)
    0xf18: vf18(0x0) = CONST 
    0xf1c: MSTORE vf18(0x0), vf17
    0xf1d: vf1d(0x3) = CONST 
    0xf1f: vf1f(0x20) = CONST 
    0xf23: MSTORE vf1f(0x20), vf1d(0x3)
    0xf24: vf24(0x40) = CONST 
    0xf27: vf27 = SHA3 vf18(0x0), vf24(0x40)
    0xf2a: SSTORE vf27, vf0c_0
    0xf2b: vf2b(0x7) = CONST 
    0xf2d: vf2d = ADD vf2b(0x7), vf27
    0xf2f: vf2f = SLOAD vf2d
    0xf30: vf30(0x1) = CONST 
    0xf34: vf34 = ADD vf30(0x1), vf2f
    0xf36: SSTORE vf2d, vf34
    0xf39: MSTORE vf18(0x0), vf2d
    0xf3d: vf3d = SHA3 vf18(0x0), vf1f(0x20)
    0xf3e: vf3e = ADD vf3d, vf2f
    0xf42: SSTORE vf3e, vf0c_0

    Begin block 0xf450x388
    prev=[0xf0d], succ=[0x3b29]
    =================================
    0xf4a0x388: JUMP v397(0x3b29)

    Begin block 0x3b29
    prev=[0xf450x388], succ=[]
    =================================
    0x3b2a: v3b2a(0x40) = CONST 
    0x3b2d: v3b2d = MLOAD v3b2a(0x40)
    0x3b2f: v3b2f = ISZERO vf30(0x1)
    0x3b30: v3b30 = ISZERO v3b2f
    0x3b32: MSTORE v3b2d, v3b30
    0x3b33: v3b33 = MLOAD v3b2a(0x40)
    0x3b37: v3b37(0x0) = SUB v3b2d, v3b33
    0x3b38: v3b38(0x20) = CONST 
    0x3b3a: v3b3a(0x20) = ADD v3b38(0x20), v3b37(0x0)
    0x3b3c: RETURN v3b33, v3b3a(0x20)

}

function registry()() public {
    Begin block 0x3c5
    prev=[], succ=[0x3ce, 0x3d2]
    =================================
    0x3c6: v3c6 = CALLVALUE 
    0x3c8: v3c8 = ISZERO v3c6
    0x3c9: v3c9(0x3d2) = CONST 
    0x3cd: JUMPI v3c9(0x3d2), v3c8

    Begin block 0x3ce
    prev=[0x3c5], succ=[]
    =================================
    0x3ce: v3ce(0x0) = CONST 
    0x3d1: REVERT v3ce(0x0), v3ce(0x0)

    Begin block 0x3d2
    prev=[0x3c5], succ=[0xf4b]
    =================================
    0x3d4: v3d4(0x3b5c) = CONST 
    0x3d8: v3d8(0xf4b) = CONST 
    0x3dc: JUMP v3d8(0xf4b)

    Begin block 0xf4b
    prev=[0x3d2], succ=[0x3b5c]
    =================================
    0xf4c: vf4c(0x7) = CONST 
    0xf4e: vf4e = SLOAD vf4c(0x7)
    0xf4f: vf4f(0x1) = CONST 
    0xf51: vf51(0x1) = CONST 
    0xf53: vf53(0xa0) = CONST 
    0xf55: vf55(0x10000000000000000000000000000000000000000) = SHL vf53(0xa0), vf51(0x1)
    0xf56: vf56(0xffffffffffffffffffffffffffffffffffffffff) = SUB vf55(0x10000000000000000000000000000000000000000), vf4f(0x1)
    0xf57: vf57 = AND vf56(0xffffffffffffffffffffffffffffffffffffffff), vf4e
    0xf59: JUMP v3d4(0x3b5c)

    Begin block 0x3b5c
    prev=[0xf4b], succ=[]
    =================================
    0x3b5d: v3b5d(0x40) = CONST 
    0x3b60: v3b60 = MLOAD v3b5d(0x40)
    0x3b61: v3b61(0x1) = CONST 
    0x3b63: v3b63(0x1) = CONST 
    0x3b65: v3b65(0xa0) = CONST 
    0x3b67: v3b67(0x10000000000000000000000000000000000000000) = SHL v3b65(0xa0), v3b63(0x1)
    0x3b68: v3b68(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3b67(0x10000000000000000000000000000000000000000), v3b61(0x1)
    0x3b6b: v3b6b = AND vf57, v3b68(0xffffffffffffffffffffffffffffffffffffffff)
    0x3b6d: MSTORE v3b60, v3b6b
    0x3b6e: v3b6e = MLOAD v3b5d(0x40)
    0x3b72: v3b72(0x0) = SUB v3b60, v3b6e
    0x3b73: v3b73(0x20) = CONST 
    0x3b75: v3b75(0x20) = ADD v3b73(0x20), v3b72(0x0)
    0x3b77: RETURN v3b6e, v3b75(0x20)

}

function ETHForTokens(address,address)() public {
    Begin block 0x3dd
    prev=[], succ=[0x3f1, 0x3f5]
    =================================
    0x3de: v3de(0x3b97) = CONST 
    0x3e2: v3e2(0x4) = CONST 
    0x3e5: v3e5 = CALLDATASIZE 
    0x3e6: v3e6 = SUB v3e5, v3e2(0x4)
    0x3e7: v3e7(0x40) = CONST 
    0x3ea: v3ea = LT v3e6, v3e7(0x40)
    0x3eb: v3eb = ISZERO v3ea
    0x3ec: v3ec(0x3f5) = CONST 
    0x3f0: JUMPI v3ec(0x3f5), v3eb

    Begin block 0x3f1
    prev=[0x3dd], succ=[]
    =================================
    0x3f1: v3f1(0x0) = CONST 
    0x3f4: REVERT v3f1(0x0), v3f1(0x0)

    Begin block 0x3f5
    prev=[0x3dd], succ=[0xf5a]
    =================================
    0x3f7: v3f7(0x1) = CONST 
    0x3f9: v3f9(0x1) = CONST 
    0x3fb: v3fb(0xa0) = CONST 
    0x3fd: v3fd(0x10000000000000000000000000000000000000000) = SHL v3fb(0xa0), v3f9(0x1)
    0x3fe: v3fe(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fd(0x10000000000000000000000000000000000000000), v3f7(0x1)
    0x400: v400 = CALLDATALOAD v3e2(0x4)
    0x402: v402 = AND v3fe(0xffffffffffffffffffffffffffffffffffffffff), v400
    0x404: v404(0x20) = CONST 
    0x406: v406(0x24) = ADD v404(0x20), v3e2(0x4)
    0x407: v407 = CALLDATALOAD v406(0x24)
    0x408: v408 = AND v407, v3fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x409: v409(0xf5a) = CONST 
    0x40d: JUMP v409(0xf5a)

    Begin block 0xf5a
    prev=[0x3f5], succ=[0xf6b, 0xfa2]
    =================================
    0xf5b: vf5b(0x0) = CONST 
    0xf5d: vf5d = SLOAD vf5b(0x0)
    0xf5e: vf5e(0xff) = CONST 
    0xf60: vf60 = AND vf5e(0xff), vf5d
    0xf61: vf61 = ISZERO vf60
    0xf62: vf62 = ISZERO vf61
    0xf63: vf63(0x1) = CONST 
    0xf65: vf65 = EQ vf63(0x1), vf62
    0xf66: vf66(0xfa2) = CONST 
    0xf6a: JUMPI vf66(0xfa2), vf65

    Begin block 0xf6b
    prev=[0xf5a], succ=[]
    =================================
    0xf6b: vf6b(0x40) = CONST 
    0xf6d: vf6d = MLOAD vf6b(0x40)
    0xf6e: vf6e(0x461bcd) = CONST 
    0xf72: vf72(0xe5) = CONST 
    0xf74: vf74(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vf72(0xe5), vf6e(0x461bcd)
    0xf76: MSTORE vf6d, vf74(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf77: vf77(0x4) = CONST 
    0xf79: vf79 = ADD vf77(0x4), vf6d
    0xf7c: vf7c(0x20) = CONST 
    0xf7e: vf7e = ADD vf7c(0x20), vf79
    0xf81: vf81(0x20) = SUB vf7e, vf79
    0xf83: MSTORE vf79, vf81(0x20)
    0xf84: vf84(0x32) = CONST 
    0xf87: MSTORE vf7e, vf84(0x32)
    0xf88: vf88(0x20) = CONST 
    0xf8a: vf8a = ADD vf88(0x20), vf7e
    0xf8c: vf8c(0x37d5) = CONST 
    0xf90: vf90(0x32) = CONST 
    0xf93: CODECOPY vf8a, vf8c(0x37d5), vf90(0x32)
    0xf94: vf94(0x40) = CONST 
    0xf96: vf96 = ADD vf94(0x40), vf8a
    0xf9a: vf9a(0x40) = CONST 
    0xf9c: vf9c = MLOAD vf9a(0x40)
    0xf9f: vf9f(0x84) = SUB vf96, vf9c
    0xfa1: REVERT vf9c, vf9f(0x84)

    Begin block 0xfa2
    prev=[0xf5a], succ=[0xfcb, 0xfcf]
    =================================
    0xfa3: vfa3(0x1) = CONST 
    0xfa5: vfa5(0x1) = CONST 
    0xfa7: vfa7(0xa0) = CONST 
    0xfa9: vfa9(0x10000000000000000000000000000000000000000) = SHL vfa7(0xa0), vfa5(0x1)
    0xfaa: vfaa(0xffffffffffffffffffffffffffffffffffffffff) = SUB vfa9(0x10000000000000000000000000000000000000000), vfa3(0x1)
    0xfad: vfad = AND vfaa(0xffffffffffffffffffffffffffffffffffffffff), v402
    0xfae: vfae(0x0) = CONST 
    0xfb2: MSTORE vfae(0x0), vfad
    0xfb3: vfb3(0x3) = CONST 
    0xfb5: vfb5(0x20) = CONST 
    0xfb7: MSTORE vfb5(0x20), vfb3(0x3)
    0xfb8: vfb8(0x40) = CONST 
    0xfbb: vfbb = SHA3 vfae(0x0), vfb8(0x40)
    0xfbc: vfbc(0x9) = CONST 
    0xfbe: vfbe = ADD vfbc(0x9), vfbb
    0xfbf: vfbf = SLOAD vfbe
    0xfc1: vfc1 = AND vfaa(0xffffffffffffffffffffffffffffffffffffffff), vfbf
    0xfc4: vfc4 = AND v408, vfaa(0xffffffffffffffffffffffffffffffffffffffff)
    0xfc5: vfc5 = EQ vfc4, vfc1
    0xfc6: vfc6(0xfcf) = CONST 
    0xfca: JUMPI vfc6(0xfcf), vfc5

    Begin block 0xfcb
    prev=[0xfa2], succ=[]
    =================================
    0xfcb: vfcb(0x0) = CONST 
    0xfce: REVERT vfcb(0x0), vfcb(0x0)

    Begin block 0xfcf
    prev=[0xfa2], succ=[0x3e68]
    =================================
    0xfd0: vfd0(0x0) = CONST 
    0xfd2: vfd2(0xfe4) = CONST 
    0xfd6: vfd6(0x64) = CONST 
    0xfd8: vfd8(0x3e68) = CONST 
    0xfdc: vfdc = CALLVALUE 
    0xfdd: vfdd(0x1) = CONST 
    0xfdf: vfdf(0x1e23) = CONST 
    0xfe3: vfe3_0 = CALLPRIVATE vfdf(0x1e23), vfdd(0x1), vfdc, vfd8(0x3e68)

    Begin block 0x3e68
    prev=[0xfcf], succ=[0xfe4]
    =================================
    0x3e6a: v3e6a(0x1e81) = CONST 
    0x3e6e: v3e6e_0 = CALLPRIVATE v3e6a(0x1e81), vfd6(0x64), vfe3_0, vfd2(0xfe4)

    Begin block 0xfe4
    prev=[0x3e68], succ=[0x1000]
    =================================
    0xfe5: vfe5(0x9) = CONST 
    0xfe7: vfe7 = SLOAD vfe5(0x9)
    0xfeb: vfeb(0x1) = CONST 
    0xfed: vfed(0x1) = CONST 
    0xfef: vfef(0xa0) = CONST 
    0xff1: vff1(0x10000000000000000000000000000000000000000) = SHL vfef(0xa0), vfed(0x1)
    0xff2: vff2(0xffffffffffffffffffffffffffffffffffffffff) = SUB vff1(0x10000000000000000000000000000000000000000), vfeb(0x1)
    0xff3: vff3 = AND vff2(0xffffffffffffffffffffffffffffffffffffffff), vfe7
    0xff4: vff4(0x1000) = CONST 
    0xff9: vff9(0xa) = CONST 
    0xffb: vffb(0x1e81) = CONST 
    0xfff: vfff_0 = CALLPRIVATE vffb(0x1e81), vff9(0xa), v3e6e_0, vff4(0x1000)

    Begin block 0x1000
    prev=[0xfe4], succ=[0x101c, 0x103e]
    =================================
    0x1001: v1001(0x40) = CONST 
    0x1003: v1003 = MLOAD v1001(0x40)
    0x1004: v1004(0x0) = CONST 
    0x100b: v100b = GAS 
    0x100c: v100c = CALL v100b, vff3, vfff_0, v1003, v1004(0x0), v1003, v1004(0x0)
    0x1011: v1011 = RETURNDATASIZE 
    0x1013: v1013(0x0) = CONST 
    0x1016: v1016 = EQ v1011, v1013(0x0)
    0x1017: v1017(0x103e) = CONST 
    0x101b: JUMPI v1017(0x103e), v1016

    Begin block 0x101c
    prev=[0x1000], succ=[0x1043]
    =================================
    0x101c: v101c(0x40) = CONST 
    0x101e: v101e = MLOAD v101c(0x40)
    0x1021: v1021(0x1f) = CONST 
    0x1023: v1023(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1021(0x1f)
    0x1024: v1024(0x3f) = CONST 
    0x1026: v1026 = RETURNDATASIZE 
    0x1027: v1027 = ADD v1026, v1024(0x3f)
    0x1028: v1028 = AND v1027, v1023(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x102a: v102a = ADD v101e, v1028
    0x102b: v102b(0x40) = CONST 
    0x102d: MSTORE v102b(0x40), v102a
    0x102e: v102e = RETURNDATASIZE 
    0x1030: MSTORE v101e, v102e
    0x1031: v1031 = RETURNDATASIZE 
    0x1032: v1032(0x0) = CONST 
    0x1034: v1034(0x20) = CONST 
    0x1037: v1037 = ADD v101e, v1034(0x20)
    0x1038: RETURNDATACOPY v1037, v1032(0x0), v1031
    0x1039: v1039(0x1043) = CONST 
    0x103d: JUMP v1039(0x1043)

    Begin block 0x1043
    prev=[0x101c, 0x103e], succ=[0x1064]
    =================================
    0x1046: v1046(0x8) = CONST 
    0x1048: v1048 = SLOAD v1046(0x8)
    0x1049: v1049(0x1) = CONST 
    0x104b: v104b(0x1) = CONST 
    0x104d: v104d(0xa0) = CONST 
    0x104f: v104f(0x10000000000000000000000000000000000000000) = SHL v104d(0xa0), v104b(0x1)
    0x1050: v1050(0xffffffffffffffffffffffffffffffffffffffff) = SUB v104f(0x10000000000000000000000000000000000000000), v1049(0x1)
    0x1051: v1051 = AND v1050(0xffffffffffffffffffffffffffffffffffffffff), v1048
    0x1054: v1054(0x106c) = CONST 
    0x1058: v1058(0x1064) = CONST 
    0x105d: v105d(0xa) = CONST 
    0x105f: v105f(0x1e81) = CONST 
    0x1063: v1063_0 = CALLPRIVATE v105f(0x1e81), v105d(0xa), v3e6e_0, v1058(0x1064)

    Begin block 0x1064
    prev=[0x1043], succ=[0x106c]
    =================================
    0x1067: v1067(0x1ec5) = CONST 
    0x106b: v106b_0 = CALLPRIVATE v1067(0x1ec5), v1063_0, v3e6e_0, v1054(0x106c)

    Begin block 0x106c
    prev=[0x1064], succ=[0x1088, 0x10aa]
    =================================
    0x106d: v106d(0x40) = CONST 
    0x106f: v106f = MLOAD v106d(0x40)
    0x1070: v1070(0x0) = CONST 
    0x1077: v1077 = GAS 
    0x1078: v1078 = CALL v1077, v1051, v106b_0, v106f, v1070(0x0), v106f, v1070(0x0)
    0x107d: v107d = RETURNDATASIZE 
    0x107f: v107f(0x0) = CONST 
    0x1082: v1082 = EQ v107d, v107f(0x0)
    0x1083: v1083(0x10aa) = CONST 
    0x1087: JUMPI v1083(0x10aa), v1082

    Begin block 0x1088
    prev=[0x106c], succ=[0x10af]
    =================================
    0x1088: v1088(0x40) = CONST 
    0x108a: v108a = MLOAD v1088(0x40)
    0x108d: v108d(0x1f) = CONST 
    0x108f: v108f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v108d(0x1f)
    0x1090: v1090(0x3f) = CONST 
    0x1092: v1092 = RETURNDATASIZE 
    0x1093: v1093 = ADD v1092, v1090(0x3f)
    0x1094: v1094 = AND v1093, v108f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x1096: v1096 = ADD v108a, v1094
    0x1097: v1097(0x40) = CONST 
    0x1099: MSTORE v1097(0x40), v1096
    0x109a: v109a = RETURNDATASIZE 
    0x109c: MSTORE v108a, v109a
    0x109d: v109d = RETURNDATASIZE 
    0x109e: v109e(0x0) = CONST 
    0x10a0: v10a0(0x20) = CONST 
    0x10a3: v10a3 = ADD v108a, v10a0(0x20)
    0x10a4: RETURNDATACOPY v10a3, v109e(0x0), v109d
    0x10a5: v10a5(0x10af) = CONST 
    0x10a9: JUMP v10a5(0x10af)

    Begin block 0x10af
    prev=[0x1088, 0x10aa], succ=[0x10cb]
    =================================
    0x10b2: v10b2(0x5) = CONST 
    0x10b4: v10b4 = SLOAD v10b2(0x5)
    0x10b5: v10b5(0x1) = CONST 
    0x10b7: v10b7(0x1) = CONST 
    0x10b9: v10b9(0xa0) = CONST 
    0x10bb: v10bb(0x10000000000000000000000000000000000000000) = SHL v10b9(0xa0), v10b7(0x1)
    0x10bc: v10bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10bb(0x10000000000000000000000000000000000000000), v10b5(0x1)
    0x10bd: v10bd = AND v10bc(0xffffffffffffffffffffffffffffffffffffffff), v10b4
    0x10c0: v10c0(0x10cb) = CONST 
    0x10c4: v10c4 = CALLVALUE 
    0x10c6: v10c6(0x1ec5) = CONST 
    0x10ca: v10ca_0 = CALLPRIVATE v10c6(0x1ec5), v3e6e_0, v10c4, v10c0(0x10cb)

    Begin block 0x10cb
    prev=[0x10af], succ=[0x10e7, 0x1109]
    =================================
    0x10cc: v10cc(0x40) = CONST 
    0x10ce: v10ce = MLOAD v10cc(0x40)
    0x10cf: v10cf(0x0) = CONST 
    0x10d6: v10d6 = GAS 
    0x10d7: v10d7 = CALL v10d6, v10bd, v10ca_0, v10ce, v10cf(0x0), v10ce, v10cf(0x0)
    0x10dc: v10dc = RETURNDATASIZE 
    0x10de: v10de(0x0) = CONST 
    0x10e1: v10e1 = EQ v10dc, v10de(0x0)
    0x10e2: v10e2(0x1109) = CONST 
    0x10e6: JUMPI v10e2(0x1109), v10e1

    Begin block 0x10e7
    prev=[0x10cb], succ=[0x110e]
    =================================
    0x10e7: v10e7(0x40) = CONST 
    0x10e9: v10e9 = MLOAD v10e7(0x40)
    0x10ec: v10ec(0x1f) = CONST 
    0x10ee: v10ee(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v10ec(0x1f)
    0x10ef: v10ef(0x3f) = CONST 
    0x10f1: v10f1 = RETURNDATASIZE 
    0x10f2: v10f2 = ADD v10f1, v10ef(0x3f)
    0x10f3: v10f3 = AND v10f2, v10ee(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x10f5: v10f5 = ADD v10e9, v10f3
    0x10f6: v10f6(0x40) = CONST 
    0x10f8: MSTORE v10f6(0x40), v10f5
    0x10f9: v10f9 = RETURNDATASIZE 
    0x10fb: MSTORE v10e9, v10f9
    0x10fc: v10fc = RETURNDATASIZE 
    0x10fd: v10fd(0x0) = CONST 
    0x10ff: v10ff(0x20) = CONST 
    0x1102: v1102 = ADD v10e9, v10ff(0x20)
    0x1103: RETURNDATACOPY v1102, v10fd(0x0), v10fc
    0x1104: v1104(0x110e) = CONST 
    0x1108: JUMP v1104(0x110e)

    Begin block 0x110e
    prev=[0x10e7, 0x1109], succ=[0x118d, 0x1191]
    =================================
    0x1111: v1111(0x5) = CONST 
    0x1113: v1113 = SLOAD v1111(0x5)
    0x1114: v1114(0x40) = CONST 
    0x1117: v1117 = MLOAD v1114(0x40)
    0x1118: v1118(0x75b04b15) = CONST 
    0x111d: v111d(0xe1) = CONST 
    0x111f: v111f(0xeb60962a00000000000000000000000000000000000000000000000000000000) = SHL v111d(0xe1), v1118(0x75b04b15)
    0x1121: MSTORE v1117, v111f(0xeb60962a00000000000000000000000000000000000000000000000000000000)
    0x1122: v1122(0x1) = CONST 
    0x1124: v1124(0x1) = CONST 
    0x1126: v1126(0xa0) = CONST 
    0x1128: v1128(0x10000000000000000000000000000000000000000) = SHL v1126(0xa0), v1124(0x1)
    0x1129: v1129(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1128(0x10000000000000000000000000000000000000000), v1122(0x1)
    0x112c: v112c = AND v1129(0xffffffffffffffffffffffffffffffffffffffff), v402
    0x112d: v112d(0x4) = CONST 
    0x1130: v1130 = ADD v1117, v112d(0x4)
    0x1131: MSTORE v1130, v112c
    0x1134: v1134 = AND v1113, v1129(0xffffffffffffffffffffffffffffffffffffffff)
    0x1135: v1135(0x44) = CONST 
    0x1138: v1138 = ADD v1117, v1135(0x44)
    0x113b: MSTORE v1138, v1134
    0x113c: v113c(0x60) = CONST 
    0x113e: v113e(0x24) = CONST 
    0x1141: v1141 = ADD v1117, v113e(0x24)
    0x1142: MSTORE v1141, v113c(0x60)
    0x1143: v1143(0x12) = CONST 
    0x1145: v1145(0x64) = CONST 
    0x1148: v1148 = ADD v1117, v1145(0x64)
    0x1149: MSTORE v1148, v1143(0x12)
    0x114a: v114a(0x19dbdd08185b881155120819195c1bdcda5d) = CONST 
    0x115d: v115d(0x72) = CONST 
    0x115f: v115f(0x676f7420616e20455448206465706f7369740000000000000000000000000000) = SHL v115d(0x72), v114a(0x19dbdd08185b881155120819195c1bdcda5d)
    0x1160: v1160(0x84) = CONST 
    0x1163: v1163 = ADD v1117, v1160(0x84)
    0x1164: MSTORE v1163, v115f(0x676f7420616e20455448206465706f7369740000000000000000000000000000)
    0x1166: v1166 = MLOAD v1114(0x40)
    0x116a: v116a(0xeb60962a) = CONST 
    0x1170: v1170(0xa4) = CONST 
    0x1174: v1174 = ADD v1117, v1170(0xa4)
    0x1176: v1176(0x0) = CONST 
    0x117e: v117e(0x0) = SUB v1117, v1166
    0x117f: v117f(0xa4) = ADD v117e(0x0), v1170(0xa4)
    0x1184: v1184 = EXTCODESIZE v1134
    0x1185: v1185 = ISZERO v1184
    0x1187: v1187 = ISZERO v1185
    0x1188: v1188(0x1191) = CONST 
    0x118c: JUMPI v1188(0x1191), v1187

    Begin block 0x118d
    prev=[0x110e], succ=[]
    =================================
    0x118d: v118d(0x0) = CONST 
    0x1190: REVERT v118d(0x0), v118d(0x0)

    Begin block 0x1191
    prev=[0x110e], succ=[0x119d, 0x11a6]
    =================================
    0x1193: v1193 = GAS 
    0x1194: v1194 = CALL v1193, v1134, v1176(0x0), v1166, v117f(0xa4), v1166, v1176(0x0)
    0x1195: v1195 = ISZERO v1194
    0x1197: v1197 = ISZERO v1195
    0x1198: v1198(0x11a6) = CONST 
    0x119c: JUMPI v1198(0x11a6), v1197

    Begin block 0x119d
    prev=[0x1191], succ=[]
    =================================
    0x119d: v119d = RETURNDATASIZE 
    0x119e: v119e(0x0) = CONST 
    0x11a1: RETURNDATACOPY v119e(0x0), v119e(0x0), v119d
    0x11a2: v11a2 = RETURNDATASIZE 
    0x11a3: v11a3(0x0) = CONST 
    0x11a5: REVERT v11a3(0x0), v11a2

    Begin block 0x11a6
    prev=[0x1191], succ=[0x3e8e]
    =================================
    0x11ab: v11ab(0x11e3) = CONST 
    0x11af: v11af(0x3e8e) = CONST 
    0x11b4: v11b4 = CALLVALUE 
    0x11b5: v11b5(0x1ec5) = CONST 
    0x11bc: v11bc(0xffffffff) = CONST 
    0x11c1: v11c1(0x1ec5) = AND v11bc(0xffffffff), v11b5(0x1ec5)
    0x11c2: v11c2_0 = CALLPRIVATE v11c1(0x1ec5), v3e6e_0, v11b4, v11af(0x3e8e)

    Begin block 0x3e8e
    prev=[0x11a6], succ=[0x1ffaB0x3e8e]
    =================================
    0x3e8f: v3e8f(0x1) = CONST 
    0x3e91: v3e91(0x1) = CONST 
    0x3e93: v3e93(0xa0) = CONST 
    0x3e95: v3e95(0x10000000000000000000000000000000000000000) = SHL v3e93(0xa0), v3e91(0x1)
    0x3e96: v3e96(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3e95(0x10000000000000000000000000000000000000000), v3e8f(0x1)
    0x3e98: v3e98 = AND v402, v3e96(0xffffffffffffffffffffffffffffffffffffffff)
    0x3e99: v3e99(0x0) = CONST 
    0x3e9d: MSTORE v3e99(0x0), v3e98
    0x3e9e: v3e9e(0x3) = CONST 
    0x3ea0: v3ea0(0x20) = CONST 
    0x3ea2: MSTORE v3ea0(0x20), v3e9e(0x3)
    0x3ea3: v3ea3(0x40) = CONST 
    0x3ea6: v3ea6 = SHA3 v3e99(0x0), v3ea3(0x40)
    0x3ea7: v3ea7 = SLOAD v3ea6
    0x3ea9: v3ea9(0x1ffa) = CONST 
    0x3ead: JUMP v3ea9(0x1ffa)

    Begin block 0x1ffaB0x3e8e
    prev=[0x3e8e], succ=[0x2009B0x3e8e, 0x4083B0x3e8e]
    =================================
    0x1ffbS0x3e8e: v1ffbV3e8e(0x0) = CONST 
    0x1fffS0x3e8e: v1fffV3e8e = ADD v11c2_0, v3ea7
    0x2002S0x3e8e: v2002V3e8e = LT v1fffV3e8e, v3ea7
    0x2003S0x3e8e: v2003V3e8e = ISZERO v2002V3e8e
    0x2004S0x3e8e: v2004V3e8e(0x4083) = CONST 
    0x2008S0x3e8e: JUMPI v2004V3e8e(0x4083), v2003V3e8e

    Begin block 0x2009B0x3e8e
    prev=[0x1ffaB0x3e8e], succ=[]
    =================================
    0x2009S0x3e8e: v2009V3e8e(0x40) = CONST 
    0x200cS0x3e8e: v200cV3e8e = MLOAD v2009V3e8e(0x40)
    0x200dS0x3e8e: v200dV3e8e(0x461bcd) = CONST 
    0x2011S0x3e8e: v2011V3e8e(0xe5) = CONST 
    0x2013S0x3e8e: v2013V3e8e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2011V3e8e(0xe5), v200dV3e8e(0x461bcd)
    0x2015S0x3e8e: MSTORE v200cV3e8e, v2013V3e8e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2016S0x3e8e: v2016V3e8e(0x20) = CONST 
    0x2018S0x3e8e: v2018V3e8e(0x4) = CONST 
    0x201bS0x3e8e: v201bV3e8e = ADD v200cV3e8e, v2018V3e8e(0x4)
    0x201cS0x3e8e: MSTORE v201bV3e8e, v2016V3e8e(0x20)
    0x201dS0x3e8e: v201dV3e8e(0x1b) = CONST 
    0x201fS0x3e8e: v201fV3e8e(0x24) = CONST 
    0x2022S0x3e8e: v2022V3e8e = ADD v200cV3e8e, v201fV3e8e(0x24)
    0x2023S0x3e8e: MSTORE v2022V3e8e, v201dV3e8e(0x1b)
    0x2024S0x3e8e: v2024V3e8e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2045S0x3e8e: v2045V3e8e(0x44) = CONST 
    0x2048S0x3e8e: v2048V3e8e = ADD v200cV3e8e, v2045V3e8e(0x44)
    0x2049S0x3e8e: MSTORE v2048V3e8e, v2024V3e8e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x204bS0x3e8e: v204bV3e8e = MLOAD v2009V3e8e(0x40)
    0x204fS0x3e8e: v204fV3e8e(0x0) = SUB v200cV3e8e, v204bV3e8e
    0x2050S0x3e8e: v2050V3e8e(0x64) = CONST 
    0x2052S0x3e8e: v2052V3e8e(0x64) = ADD v2050V3e8e(0x64), v204fV3e8e(0x0)
    0x2054S0x3e8e: REVERT v204bV3e8e, v2052V3e8e(0x64)

    Begin block 0x4083B0x3e8e
    prev=[0x1ffaB0x3e8e], succ=[0x11e3]
    =================================
    0x4089S0x3e8e: JUMP v11ab(0x11e3)

    Begin block 0x11e3
    prev=[0x4083B0x3e8e], succ=[0x122a]
    =================================
    0x11e4: v11e4(0x1) = CONST 
    0x11e6: v11e6(0x1) = CONST 
    0x11e8: v11e8(0xa0) = CONST 
    0x11ea: v11ea(0x10000000000000000000000000000000000000000) = SHL v11e8(0xa0), v11e6(0x1)
    0x11eb: v11eb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11ea(0x10000000000000000000000000000000000000000), v11e4(0x1)
    0x11ee: v11ee = AND v402, v11eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x11ef: v11ef(0x0) = CONST 
    0x11f3: MSTORE v11ef(0x0), v11ee
    0x11f4: v11f4(0x3) = CONST 
    0x11f6: v11f6(0x20) = CONST 
    0x11fa: MSTORE v11f6(0x20), v11f4(0x3)
    0x11fb: v11fb(0x40) = CONST 
    0x11fe: v11fe = SHA3 v11ef(0x0), v11fb(0x40)
    0x1201: SSTORE v11fe, v1fffV3e8e
    0x1202: v1202(0x7) = CONST 
    0x1204: v1204 = ADD v1202(0x7), v11fe
    0x1206: v1206 = SLOAD v1204
    0x1207: v1207(0x1) = CONST 
    0x120a: v120a = ADD v1206, v1207(0x1)
    0x120c: SSTORE v1204, v120a
    0x120f: MSTORE v11ef(0x0), v1204
    0x1211: v1211 = SHA3 v11ef(0x0), v11f6(0x20)
    0x1212: v1212 = ADD v1211, v1206
    0x1216: SSTORE v1212, v1fffV3e8e
    0x1218: v1218 = AND v408, v11eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x1219: v1219(0xf0dda65c) = CONST 
    0x121e: v121e = CALLER 
    0x121f: v121f(0x122a) = CONST 
    0x1223: v1223 = CALLVALUE 
    0x1225: v1225(0x1ec5) = CONST 
    0x1229: v1229_0 = CALLPRIVATE v1225(0x1ec5), v3e6e_0, v1223, v121f(0x122a)

    Begin block 0x122a
    prev=[0x11e3], succ=[0x126d, 0x1271]
    =================================
    0x122b: v122b(0x40) = CONST 
    0x122d: v122d = MLOAD v122b(0x40)
    0x122f: v122f(0xffffffff) = CONST 
    0x1234: v1234(0xf0dda65c) = AND v122f(0xffffffff), v1219(0xf0dda65c)
    0x1235: v1235(0xe0) = CONST 
    0x1237: v1237(0xf0dda65c00000000000000000000000000000000000000000000000000000000) = SHL v1235(0xe0), v1234(0xf0dda65c)
    0x1239: MSTORE v122d, v1237(0xf0dda65c00000000000000000000000000000000000000000000000000000000)
    0x123a: v123a(0x4) = CONST 
    0x123c: v123c = ADD v123a(0x4), v122d
    0x123f: v123f(0x1) = CONST 
    0x1241: v1241(0x1) = CONST 
    0x1243: v1243(0xa0) = CONST 
    0x1245: v1245(0x10000000000000000000000000000000000000000) = SHL v1243(0xa0), v1241(0x1)
    0x1246: v1246(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1245(0x10000000000000000000000000000000000000000), v123f(0x1)
    0x1247: v1247 = AND v1246(0xffffffffffffffffffffffffffffffffffffffff), v121e
    0x1249: MSTORE v123c, v1247
    0x124a: v124a(0x20) = CONST 
    0x124c: v124c = ADD v124a(0x20), v123c
    0x124f: MSTORE v124c, v1229_0
    0x1250: v1250(0x20) = CONST 
    0x1252: v1252 = ADD v1250(0x20), v124c
    0x1257: v1257(0x0) = CONST 
    0x1259: v1259(0x40) = CONST 
    0x125b: v125b = MLOAD v1259(0x40)
    0x125e: v125e(0x44) = SUB v1252, v125b
    0x1260: v1260(0x0) = CONST 
    0x1264: v1264 = EXTCODESIZE v1218
    0x1265: v1265 = ISZERO v1264
    0x1267: v1267 = ISZERO v1265
    0x1268: v1268(0x1271) = CONST 
    0x126c: JUMPI v1268(0x1271), v1267

    Begin block 0x126d
    prev=[0x122a], succ=[]
    =================================
    0x126d: v126d(0x0) = CONST 
    0x1270: REVERT v126d(0x0), v126d(0x0)

    Begin block 0x1271
    prev=[0x122a], succ=[0x127d, 0x1286]
    =================================
    0x1273: v1273 = GAS 
    0x1274: v1274 = CALL v1273, v1218, v1260(0x0), v125b, v125e(0x44), v125b, v1257(0x0)
    0x1275: v1275 = ISZERO v1274
    0x1277: v1277 = ISZERO v1275
    0x1278: v1278(0x1286) = CONST 
    0x127c: JUMPI v1278(0x1286), v1277

    Begin block 0x127d
    prev=[0x1271], succ=[]
    =================================
    0x127d: v127d = RETURNDATASIZE 
    0x127e: v127e(0x0) = CONST 
    0x1281: RETURNDATACOPY v127e(0x0), v127e(0x0), v127d
    0x1282: v1282 = RETURNDATASIZE 
    0x1283: v1283(0x0) = CONST 
    0x1285: REVERT v1283(0x0), v1282

    Begin block 0x1286
    prev=[0x1271], succ=[0x3b97]
    =================================
    0x1289: v1289(0x40) = CONST 
    0x128c: v128c = MLOAD v1289(0x40)
    0x128d: v128d = CALLER 
    0x128f: MSTORE v128c, v128d
    0x1290: v1290(0x1) = CONST 
    0x1292: v1292(0x1) = CONST 
    0x1294: v1294(0xa0) = CONST 
    0x1296: v1296(0x10000000000000000000000000000000000000000) = SHL v1294(0xa0), v1292(0x1)
    0x1297: v1297(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1296(0x10000000000000000000000000000000000000000), v1290(0x1)
    0x129a: v129a = AND v402, v1297(0xffffffffffffffffffffffffffffffffffffffff)
    0x129b: v129b(0x20) = CONST 
    0x129e: v129e = ADD v128c, v129b(0x20)
    0x129f: MSTORE v129e, v129a
    0x12a1: v12a1 = AND v408, v1297(0xffffffffffffffffffffffffffffffffffffffff)
    0x12a4: v12a4 = ADD v1289(0x40), v128c
    0x12a5: MSTORE v12a4, v12a1
    0x12a6: v12a6 = CALLVALUE 
    0x12a7: v12a7(0x60) = CONST 
    0x12aa: v12aa = ADD v128c, v12a7(0x60)
    0x12ab: MSTORE v12aa, v12a6
    0x12ad: v12ad = MLOAD v1289(0x40)
    0x12ae: v12ae(0x25488d774d4c9d96b2af48b21c141656a113646833485d2b376e0ba6b1f160f5) = CONST 
    0x12d4: v12d4(0x0) = SUB v128c, v12ad
    0x12d5: v12d5(0x80) = CONST 
    0x12d7: v12d7(0x80) = ADD v12d5(0x80), v12d4(0x0)
    0x12da: LOG1 v12ad, v12d7(0x80), v12ae(0x25488d774d4c9d96b2af48b21c141656a113646833485d2b376e0ba6b1f160f5)
    0x12de: JUMP v3de(0x3b97)

    Begin block 0x3b97
    prev=[0x1286], succ=[]
    =================================
    0x3b98: STOP 

    Begin block 0x1109
    prev=[0x10cb], succ=[0x110e]
    =================================
    0x110a: v110a(0x60) = CONST 

    Begin block 0x10aa
    prev=[0x106c], succ=[0x10af]
    =================================
    0x10ab: v10ab(0x60) = CONST 

    Begin block 0x103e
    prev=[0x1000], succ=[0x1043]
    =================================
    0x103f: v103f(0x60) = CONST 

}

function owner()() public {
    Begin block 0x40e
    prev=[], succ=[0x417, 0x41b]
    =================================
    0x40f: v40f = CALLVALUE 
    0x411: v411 = ISZERO v40f
    0x412: v412(0x41b) = CONST 
    0x416: JUMPI v412(0x41b), v411

    Begin block 0x417
    prev=[0x40e], succ=[]
    =================================
    0x417: v417(0x0) = CONST 
    0x41a: REVERT v417(0x0), v417(0x0)

    Begin block 0x41b
    prev=[0x40e], succ=[0x12df]
    =================================
    0x41d: v41d(0x3bb8) = CONST 
    0x421: v421(0x12df) = CONST 
    0x425: JUMP v421(0x12df)

    Begin block 0x12df
    prev=[0x41b], succ=[0x3bb8]
    =================================
    0x12e0: v12e0(0x0) = CONST 
    0x12e2: v12e2 = SLOAD v12e0(0x0)
    0x12e3: v12e3(0x100) = CONST 
    0x12e7: v12e7 = DIV v12e2, v12e3(0x100)
    0x12e8: v12e8(0x1) = CONST 
    0x12ea: v12ea(0x1) = CONST 
    0x12ec: v12ec(0xa0) = CONST 
    0x12ee: v12ee(0x10000000000000000000000000000000000000000) = SHL v12ec(0xa0), v12ea(0x1)
    0x12ef: v12ef(0xffffffffffffffffffffffffffffffffffffffff) = SUB v12ee(0x10000000000000000000000000000000000000000), v12e8(0x1)
    0x12f0: v12f0 = AND v12ef(0xffffffffffffffffffffffffffffffffffffffff), v12e7
    0x12f2: JUMP v41d(0x3bb8)

    Begin block 0x3bb8
    prev=[0x12df], succ=[]
    =================================
    0x3bb9: v3bb9(0x40) = CONST 
    0x3bbc: v3bbc = MLOAD v3bb9(0x40)
    0x3bbd: v3bbd(0x1) = CONST 
    0x3bbf: v3bbf(0x1) = CONST 
    0x3bc1: v3bc1(0xa0) = CONST 
    0x3bc3: v3bc3(0x10000000000000000000000000000000000000000) = SHL v3bc1(0xa0), v3bbf(0x1)
    0x3bc4: v3bc4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3bc3(0x10000000000000000000000000000000000000000), v3bbd(0x1)
    0x3bc7: v3bc7 = AND v12f0, v3bc4(0xffffffffffffffffffffffffffffffffffffffff)
    0x3bc9: MSTORE v3bbc, v3bc7
    0x3bca: v3bca = MLOAD v3bb9(0x40)
    0x3bce: v3bce(0x0) = SUB v3bbc, v3bca
    0x3bcf: v3bcf(0x20) = CONST 
    0x3bd1: v3bd1(0x20) = ADD v3bcf(0x20), v3bce(0x0)
    0x3bd3: RETURN v3bca, v3bd1(0x20)

}

function fallback()() public {
    Begin block 0x41cc
    prev=[], succ=[]
    =================================
    0x1b2: STOP 

}

function openPool(string)() public {
    Begin block 0x426
    prev=[], succ=[0x43a, 0x43e]
    =================================
    0x427: v427(0x3bf3) = CONST 
    0x42b: v42b(0x4) = CONST 
    0x42e: v42e = CALLDATASIZE 
    0x42f: v42f = SUB v42e, v42b(0x4)
    0x430: v430(0x20) = CONST 
    0x433: v433 = LT v42f, v430(0x20)
    0x434: v434 = ISZERO v433
    0x435: v435(0x43e) = CONST 
    0x439: JUMPI v435(0x43e), v434

    Begin block 0x43a
    prev=[0x426], succ=[]
    =================================
    0x43a: v43a(0x0) = CONST 
    0x43d: REVERT v43a(0x0), v43a(0x0)

    Begin block 0x43e
    prev=[0x426], succ=[0x456, 0x45a]
    =================================
    0x440: v440 = ADD v42b(0x4), v42f
    0x442: v442(0x20) = CONST 
    0x445: v445(0x24) = ADD v42b(0x4), v442(0x20)
    0x447: v447 = CALLDATALOAD v42b(0x4)
    0x448: v448(0x100000000) = CONST 
    0x44f: v44f = GT v447, v448(0x100000000)
    0x450: v450 = ISZERO v44f
    0x451: v451(0x45a) = CONST 
    0x455: JUMPI v451(0x45a), v450

    Begin block 0x456
    prev=[0x43e], succ=[]
    =================================
    0x456: v456(0x0) = CONST 
    0x459: REVERT v456(0x0), v456(0x0)

    Begin block 0x45a
    prev=[0x43e], succ=[0x469, 0x46d]
    =================================
    0x45c: v45c = ADD v42b(0x4), v447
    0x45e: v45e(0x20) = CONST 
    0x461: v461 = ADD v45c, v45e(0x20)
    0x462: v462 = GT v461, v440
    0x463: v463 = ISZERO v462
    0x464: v464(0x46d) = CONST 
    0x468: JUMPI v464(0x46d), v463

    Begin block 0x469
    prev=[0x45a], succ=[]
    =================================
    0x469: v469(0x0) = CONST 
    0x46c: REVERT v469(0x0), v469(0x0)

    Begin block 0x46d
    prev=[0x45a], succ=[0x48c, 0x490]
    =================================
    0x46f: v46f = CALLDATALOAD v45c
    0x471: v471(0x20) = CONST 
    0x473: v473 = ADD v471(0x20), v45c
    0x476: v476(0x1) = CONST 
    0x479: v479 = MUL v46f, v476(0x1)
    0x47b: v47b = ADD v473, v479
    0x47c: v47c = GT v47b, v440
    0x47d: v47d(0x100000000) = CONST 
    0x484: v484 = GT v46f, v47d(0x100000000)
    0x485: v485 = OR v484, v47c
    0x486: v486 = ISZERO v485
    0x487: v487(0x490) = CONST 
    0x48b: JUMPI v487(0x490), v486

    Begin block 0x48c
    prev=[0x46d], succ=[]
    =================================
    0x48c: v48c(0x0) = CONST 
    0x48f: REVERT v48c(0x0), v48c(0x0)

    Begin block 0x490
    prev=[0x46d], succ=[0x12f3]
    =================================
    0x495: v495(0x1f) = CONST 
    0x497: v497 = ADD v495(0x1f), v46f
    0x498: v498(0x20) = CONST 
    0x49c: v49c = DIV v497, v498(0x20)
    0x49d: v49d = MUL v49c, v498(0x20)
    0x49e: v49e(0x20) = CONST 
    0x4a0: v4a0 = ADD v49e(0x20), v49d
    0x4a1: v4a1(0x40) = CONST 
    0x4a3: v4a3 = MLOAD v4a1(0x40)
    0x4a6: v4a6 = ADD v4a3, v4a0
    0x4a7: v4a7(0x40) = CONST 
    0x4a9: MSTORE v4a7(0x40), v4a6
    0x4b1: MSTORE v4a3, v46f
    0x4b2: v4b2(0x20) = CONST 
    0x4b4: v4b4 = ADD v4b2(0x20), v4a3
    0x4ba: CALLDATACOPY v4b4, v473, v46f
    0x4bb: v4bb(0x0) = CONST 
    0x4be: v4be = ADD v4b4, v46f
    0x4c2: MSTORE v4be, v4bb(0x0)
    0x4c7: v4c7(0x12f3) = CONST 
    0x4d1: JUMP v4c7(0x12f3)

    Begin block 0x12f3
    prev=[0x490], succ=[0x1304, 0x133b]
    =================================
    0x12f4: v12f4(0x0) = CONST 
    0x12f6: v12f6 = SLOAD v12f4(0x0)
    0x12f7: v12f7(0xff) = CONST 
    0x12f9: v12f9 = AND v12f7(0xff), v12f6
    0x12fa: v12fa = ISZERO v12f9
    0x12fb: v12fb = ISZERO v12fa
    0x12fc: v12fc(0x1) = CONST 
    0x12fe: v12fe = EQ v12fc(0x1), v12fb
    0x12ff: v12ff(0x133b) = CONST 
    0x1303: JUMPI v12ff(0x133b), v12fe

    Begin block 0x1304
    prev=[0x12f3], succ=[]
    =================================
    0x1304: v1304(0x40) = CONST 
    0x1306: v1306 = MLOAD v1304(0x40)
    0x1307: v1307(0x461bcd) = CONST 
    0x130b: v130b(0xe5) = CONST 
    0x130d: v130d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v130b(0xe5), v1307(0x461bcd)
    0x130f: MSTORE v1306, v130d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1310: v1310(0x4) = CONST 
    0x1312: v1312 = ADD v1310(0x4), v1306
    0x1315: v1315(0x20) = CONST 
    0x1317: v1317 = ADD v1315(0x20), v1312
    0x131a: v131a(0x20) = SUB v1317, v1312
    0x131c: MSTORE v1312, v131a(0x20)
    0x131d: v131d(0x32) = CONST 
    0x1320: MSTORE v1317, v131d(0x32)
    0x1321: v1321(0x20) = CONST 
    0x1323: v1323 = ADD v1321(0x20), v1317
    0x1325: v1325(0x37d5) = CONST 
    0x1329: v1329(0x32) = CONST 
    0x132c: CODECOPY v1323, v1325(0x37d5), v1329(0x32)
    0x132d: v132d(0x40) = CONST 
    0x132f: v132f = ADD v132d(0x40), v1323
    0x1333: v1333(0x40) = CONST 
    0x1335: v1335 = MLOAD v1333(0x40)
    0x1338: v1338(0x84) = SUB v132f, v1335
    0x133a: REVERT v1335, v1338(0x84)

    Begin block 0x133b
    prev=[0x12f3], succ=[0x134c, 0x1350]
    =================================
    0x133c: v133c(0xb1a2bc2ec50000) = CONST 
    0x1344: v1344 = CALLVALUE 
    0x1345: v1345 = LT v1344, v133c(0xb1a2bc2ec50000)
    0x1346: v1346 = ISZERO v1345
    0x1347: v1347(0x1350) = CONST 
    0x134b: JUMPI v1347(0x1350), v1346

    Begin block 0x134c
    prev=[0x133b], succ=[]
    =================================
    0x134c: v134c(0x0) = CONST 
    0x134f: REVERT v134c(0x0), v134c(0x0)

    Begin block 0x1350
    prev=[0x133b], succ=[0x1398, 0x139c]
    =================================
    0x1351: v1351(0xa) = CONST 
    0x1353: v1353 = SLOAD v1351(0xa)
    0x1354: v1354(0x40) = CONST 
    0x1357: v1357 = MLOAD v1354(0x40)
    0x1358: v1358(0xdd6d77a7) = CONST 
    0x135d: v135d(0xe0) = CONST 
    0x135f: v135f(0xdd6d77a700000000000000000000000000000000000000000000000000000000) = SHL v135d(0xe0), v1358(0xdd6d77a7)
    0x1361: MSTORE v1357, v135f(0xdd6d77a700000000000000000000000000000000000000000000000000000000)
    0x1362: v1362 = CALLER 
    0x1363: v1363(0x4) = CONST 
    0x1366: v1366 = ADD v1357, v1363(0x4)
    0x1367: MSTORE v1366, v1362
    0x1369: v1369 = MLOAD v1354(0x40)
    0x136a: v136a(0x1) = CONST 
    0x136c: v136c(0x1) = CONST 
    0x136e: v136e(0xa0) = CONST 
    0x1370: v1370(0x10000000000000000000000000000000000000000) = SHL v136e(0xa0), v136c(0x1)
    0x1371: v1371(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1370(0x10000000000000000000000000000000000000000), v136a(0x1)
    0x1374: v1374 = AND v1353, v1371(0xffffffffffffffffffffffffffffffffffffffff)
    0x1376: v1376(0xdd6d77a7) = CONST 
    0x137c: v137c(0x24) = CONST 
    0x1380: v1380 = ADD v1357, v137c(0x24)
    0x1382: v1382(0x20) = CONST 
    0x138a: v138a(0x0) = SUB v1357, v1369
    0x138b: v138b(0x24) = ADD v138a(0x0), v137c(0x24)
    0x138f: v138f = EXTCODESIZE v1374
    0x1390: v1390 = ISZERO v138f
    0x1392: v1392 = ISZERO v1390
    0x1393: v1393(0x139c) = CONST 
    0x1397: JUMPI v1393(0x139c), v1392

    Begin block 0x1398
    prev=[0x1350], succ=[]
    =================================
    0x1398: v1398(0x0) = CONST 
    0x139b: REVERT v1398(0x0), v1398(0x0)

    Begin block 0x139c
    prev=[0x1350], succ=[0x13a8, 0x13b1]
    =================================
    0x139e: v139e = GAS 
    0x139f: v139f = STATICCALL v139e, v1374, v1369, v138b(0x24), v1369, v1382(0x20)
    0x13a0: v13a0 = ISZERO v139f
    0x13a2: v13a2 = ISZERO v13a0
    0x13a3: v13a3(0x13b1) = CONST 
    0x13a7: JUMPI v13a3(0x13b1), v13a2

    Begin block 0x13a8
    prev=[0x139c], succ=[]
    =================================
    0x13a8: v13a8 = RETURNDATASIZE 
    0x13a9: v13a9(0x0) = CONST 
    0x13ac: RETURNDATACOPY v13a9(0x0), v13a9(0x0), v13a8
    0x13ad: v13ad = RETURNDATASIZE 
    0x13ae: v13ae(0x0) = CONST 
    0x13b0: REVERT v13ae(0x0), v13ad

    Begin block 0x13b1
    prev=[0x139c], succ=[0x13c4, 0x13c8]
    =================================
    0x13b6: v13b6(0x40) = CONST 
    0x13b8: v13b8 = MLOAD v13b6(0x40)
    0x13b9: v13b9 = RETURNDATASIZE 
    0x13ba: v13ba(0x20) = CONST 
    0x13bd: v13bd = LT v13b9, v13ba(0x20)
    0x13be: v13be = ISZERO v13bd
    0x13bf: v13bf(0x13c8) = CONST 
    0x13c3: JUMPI v13bf(0x13c8), v13be

    Begin block 0x13c4
    prev=[0x13b1], succ=[]
    =================================
    0x13c4: v13c4(0x0) = CONST 
    0x13c7: REVERT v13c4(0x0), v13c4(0x0)

    Begin block 0x13c8
    prev=[0x13b1], succ=[0x13d1, 0x1408]
    =================================
    0x13ca: v13ca = MLOAD v13b8
    0x13cb: v13cb = ISZERO v13ca
    0x13cc: v13cc(0x1408) = CONST 
    0x13d0: JUMPI v13cc(0x1408), v13cb

    Begin block 0x13d1
    prev=[0x13c8], succ=[]
    =================================
    0x13d1: v13d1(0x40) = CONST 
    0x13d3: v13d3 = MLOAD v13d1(0x40)
    0x13d4: v13d4(0x461bcd) = CONST 
    0x13d8: v13d8(0xe5) = CONST 
    0x13da: v13da(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13d8(0xe5), v13d4(0x461bcd)
    0x13dc: MSTORE v13d3, v13da(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13dd: v13dd(0x4) = CONST 
    0x13df: v13df = ADD v13dd(0x4), v13d3
    0x13e2: v13e2(0x20) = CONST 
    0x13e4: v13e4 = ADD v13e2(0x20), v13df
    0x13e7: v13e7(0x20) = SUB v13e4, v13df
    0x13e9: MSTORE v13df, v13e7(0x20)
    0x13ea: v13ea(0x27) = CONST 
    0x13ed: MSTORE v13e4, v13ea(0x27)
    0x13ee: v13ee(0x20) = CONST 
    0x13f0: v13f0 = ADD v13ee(0x20), v13e4
    0x13f2: v13f2(0x3763) = CONST 
    0x13f6: v13f6(0x27) = CONST 
    0x13f9: CODECOPY v13f0, v13f2(0x3763), v13f6(0x27)
    0x13fa: v13fa(0x40) = CONST 
    0x13fc: v13fc = ADD v13fa(0x40), v13f0
    0x1400: v1400(0x40) = CONST 
    0x1402: v1402 = MLOAD v1400(0x40)
    0x1405: v1405(0x84) = SUB v13fc, v1402
    0x1407: REVERT v1402, v1405(0x84)

    Begin block 0x1408
    prev=[0x13c8], succ=[0x23c5]
    =================================
    0x1409: v1409(0x0) = CONST 
    0x140b: v140b = ADDRESS 
    0x140c: v140c(0x40) = CONST 
    0x140e: v140e = MLOAD v140c(0x40)
    0x140f: v140f(0x1419) = CONST 
    0x1414: v1414(0x23c5) = CONST 
    0x1418: JUMP v1414(0x23c5)

    Begin block 0x23c5
    prev=[0x1408], succ=[0x1419]
    =================================
    0x23c6: v23c6(0x12f3) = CONST 
    0x23ca: v23ca(0x2470) = CONST 
    0x23cf: CODECOPY v140e, v23ca(0x2470), v23c6(0x12f3)
    0x23d0: v23d0 = ADD v23c6(0x12f3), v140e
    0x23d2: JUMP v140f(0x1419)

    Begin block 0x1419
    prev=[0x23c5], succ=[0x143e, 0x1447]
    =================================
    0x141a: v141a(0x1) = CONST 
    0x141c: v141c(0x1) = CONST 
    0x141e: v141e(0xa0) = CONST 
    0x1420: v1420(0x10000000000000000000000000000000000000000) = SHL v141e(0xa0), v141c(0x1)
    0x1421: v1421(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1420(0x10000000000000000000000000000000000000000), v141a(0x1)
    0x1424: v1424 = AND v140b, v1421(0xffffffffffffffffffffffffffffffffffffffff)
    0x1426: MSTORE v23d0, v1424
    0x1427: v1427(0x40) = CONST 
    0x1429: v1429 = MLOAD v1427(0x40)
    0x142d: v142d(0x12f3) = SUB v23d0, v1429
    0x142e: v142e(0x20) = CONST 
    0x1430: v1430(0x1313) = ADD v142e(0x20), v142d(0x12f3)
    0x1432: v1432(0x0) = CONST 
    0x1434: v1434 = CREATE v1432(0x0), v1429, v1430(0x1313)
    0x1436: v1436 = ISZERO v1434
    0x1438: v1438 = ISZERO v1436
    0x1439: v1439(0x1447) = CONST 
    0x143d: JUMPI v1439(0x1447), v1438

    Begin block 0x143e
    prev=[0x1419], succ=[]
    =================================
    0x143e: v143e = RETURNDATASIZE 
    0x143f: v143f(0x0) = CONST 
    0x1442: RETURNDATACOPY v143f(0x0), v143f(0x0), v143e
    0x1443: v1443 = RETURNDATASIZE 
    0x1444: v1444(0x0) = CONST 
    0x1446: REVERT v1444(0x0), v1443

    Begin block 0x1447
    prev=[0x1419], succ=[0x23d3B0x1447]
    =================================
    0x1449: v1449(0x2) = CONST 
    0x144c: v144c = SLOAD v1449(0x2)
    0x144d: v144d(0x1) = CONST 
    0x1450: v1450 = ADD v144c, v144d(0x1)
    0x1453: SSTORE v1449(0x2), v1450
    0x1454: v1454(0x405787fa12a823e0f2b7631cc41b3ba8828b3321ca811111fa75cd3aa3bb5ace) = CONST 
    0x1475: v1475 = ADD v1454(0x405787fa12a823e0f2b7631cc41b3ba8828b3321ca811111fa75cd3aa3bb5ace), v144c
    0x1477: v1477 = SLOAD v1475
    0x1478: v1478(0x1) = CONST 
    0x147a: v147a(0x1) = CONST 
    0x147c: v147c(0xa0) = CONST 
    0x147e: v147e(0x10000000000000000000000000000000000000000) = SHL v147c(0xa0), v147a(0x1)
    0x147f: v147f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v147e(0x10000000000000000000000000000000000000000), v1478(0x1)
    0x1481: v1481 = AND v1434, v147f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1482: v1482(0x1) = CONST 
    0x1484: v1484(0x1) = CONST 
    0x1486: v1486(0xa0) = CONST 
    0x1488: v1488(0x10000000000000000000000000000000000000000) = SHL v1486(0xa0), v1484(0x1)
    0x1489: v1489(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1488(0x10000000000000000000000000000000000000000), v1482(0x1)
    0x148a: v148a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1489(0xffffffffffffffffffffffffffffffffffffffff)
    0x148d: v148d = AND v148a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1477
    0x148f: v148f = OR v1481, v148d
    0x1492: SSTORE v1475, v148f
    0x1493: v1493 = CALLER 
    0x1494: v1494(0x0) = CONST 
    0x1498: MSTORE v1494(0x0), v1493
    0x1499: v1499(0x3) = CONST 
    0x149b: v149b(0x20) = CONST 
    0x149f: MSTORE v149b(0x20), v1499(0x3)
    0x14a0: v14a0(0x40) = CONST 
    0x14a4: v14a4 = SHA3 v1494(0x0), v14a0(0x40)
    0x14a5: v14a5(0x9) = CONST 
    0x14a8: v14a8 = ADD v14a4, v14a5(0x9)
    0x14aa: v14aa = SLOAD v14a8
    0x14ad: v14ad = AND v148a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v14aa
    0x14b0: v14b0 = OR v1481, v14ad
    0x14b3: SSTORE v14a8, v14b0
    0x14b5: v14b5 = MLOAD v4a3
    0x14b9: v14b9(0x14cd) = CONST 
    0x14be: v14be(0x6) = CONST 
    0x14c2: v14c2 = ADD v14a4, v14be(0x6)
    0x14c6: v14c6 = ADD v4a3, v149b(0x20)
    0x14c8: v14c8(0x23d3) = CONST 
    0x14cc: JUMP v14c8(0x23d3)

    Begin block 0x23d3B0x1447
    prev=[0x1447], succ=[0x2416B0x1447, 0x2405B0x1447]
    =================================
    0x23d6S0x1447: v23d6V1447 = SLOAD v14c2
    0x23d7S0x1447: v23d7V1447(0x1) = CONST 
    0x23daS0x1447: v23daV1447(0x1) = CONST 
    0x23dcS0x1447: v23dcV1447 = AND v23daV1447(0x1), v23d6V1447
    0x23ddS0x1447: v23ddV1447 = ISZERO v23dcV1447
    0x23deS0x1447: v23deV1447(0x100) = CONST 
    0x23e1S0x1447: v23e1V1447 = MUL v23deV1447(0x100), v23ddV1447
    0x23e2S0x1447: v23e2V1447 = SUB v23e1V1447, v23d7V1447(0x1)
    0x23e3S0x1447: v23e3V1447 = AND v23e2V1447, v23d6V1447
    0x23e4S0x1447: v23e4V1447(0x2) = CONST 
    0x23e7S0x1447: v23e7V1447 = DIV v23e3V1447, v23e4V1447(0x2)
    0x23e9S0x1447: v23e9V1447(0x0) = CONST 
    0x23ebS0x1447: MSTORE v23e9V1447(0x0), v14c2
    0x23ecS0x1447: v23ecV1447(0x20) = CONST 
    0x23eeS0x1447: v23eeV1447(0x0) = CONST 
    0x23f0S0x1447: v23f0V1447 = SHA3 v23eeV1447(0x0), v23ecV1447(0x20)
    0x23f2S0x1447: v23f2V1447(0x1f) = CONST 
    0x23f4S0x1447: v23f4V1447 = ADD v23f2V1447(0x1f), v23e7V1447
    0x23f5S0x1447: v23f5V1447(0x20) = CONST 
    0x23f8S0x1447: v23f8V1447 = DIV v23f4V1447, v23f5V1447(0x20)
    0x23faS0x1447: v23faV1447 = ADD v23f0V1447, v23f8V1447
    0x23fdS0x1447: v23fdV1447(0x1f) = CONST 
    0x23ffS0x1447: v23ffV1447 = LT v23fdV1447(0x1f), v14b5
    0x2400S0x1447: v2400V1447(0x2416) = CONST 
    0x2404S0x1447: JUMPI v2400V1447(0x2416), v23ffV1447

    Begin block 0x2416B0x1447
    prev=[0x23d3B0x1447], succ=[0x2446B0x1447, 0x2426B0x1447]
    =================================
    0x2419S0x1447: v2419V1447 = ADD v14b5, v14b5
    0x241aS0x1447: v241aV1447(0x1) = CONST 
    0x241cS0x1447: v241cV1447 = ADD v241aV1447(0x1), v2419V1447
    0x241eS0x1447: SSTORE v14c2, v241cV1447
    0x2420S0x1447: v2420V1447 = ISZERO v14b5
    0x2421S0x1447: v2421V1447(0x2446) = CONST 
    0x2425S0x1447: JUMPI v2421V1447(0x2446), v2420V1447

    Begin block 0x2446B0x1447
    prev=[0x2416B0x1447, 0x2429B0x1447, 0x2405B0x1447], succ=[0x2458B0x2446B0x1447]
    =================================
    0x2446_0x1S0x1447: v2446_1V1447 = PHI v23f0V1447, v243fV1447
    0x2448S0x1447: v2448V1447(0x413e) = CONST 
    0x244fS0x1447: v244fV1447(0x2458) = CONST 
    0x2453S0x1447: JUMP v244fV1447(0x2458)

    Begin block 0x2458B0x2446B0x1447
    prev=[0x2446B0x1447], succ=[0x2459B0x2446B0x1447]
    =================================

    Begin block 0x2459B0x2446B0x1447
    prev=[0x2463B0x2446B0x1447, 0x2458B0x2446B0x1447], succ=[0x2463B0x2446B0x1447, 0x4161B0x2446B0x1447]
    =================================
    0x2459_0x0S0x2446S0x1447: v2459_0V2446V1447 = PHI v2446_1V1447, v2469V2446V1447
    0x245cS0x2446S0x1447: v245cV2446V1447 = GT v23faV1447, v2459_0V2446V1447
    0x245dS0x2446S0x1447: v245dV2446V1447 = ISZERO v245cV2446V1447
    0x245eS0x2446S0x1447: v245eV2446V1447(0x4161) = CONST 
    0x2462S0x2446S0x1447: JUMPI v245eV2446V1447(0x4161), v245dV2446V1447

    Begin block 0x2463B0x2446B0x1447
    prev=[0x2459B0x2446B0x1447], succ=[0x2459B0x2446B0x1447]
    =================================
    0x2463S0x2446S0x1447: v2463V2446V1447(0x0) = CONST 
    0x2463_0x0S0x2446S0x1447: v2463_0V2446V1447 = PHI v2446_1V1447, v2469V2446V1447
    0x2466S0x2446S0x1447: SSTORE v2463_0V2446V1447, v2463V2446V1447(0x0)
    0x2467S0x2446S0x1447: v2467V2446V1447(0x1) = CONST 
    0x2469S0x2446S0x1447: v2469V2446V1447 = ADD v2467V2446V1447(0x1), v2463_0V2446V1447
    0x246aS0x2446S0x1447: v246aV2446V1447(0x2459) = CONST 
    0x246eS0x2446S0x1447: JUMP v246aV2446V1447(0x2459)

    Begin block 0x4161B0x2446B0x1447
    prev=[0x2459B0x2446B0x1447], succ=[0x413eB0x1447]
    =================================
    0x4164S0x2446S0x1447: JUMP v2448V1447(0x413e)

    Begin block 0x413eB0x1447
    prev=[0x4161B0x2446B0x1447], succ=[0x14cd]
    =================================
    0x4141S0x1447: JUMP v14b9(0x14cd)

    Begin block 0x14cd
    prev=[0x413eB0x1447], succ=[0x14e7]
    =================================
    0x14cf: v14cf(0x9) = CONST 
    0x14d1: v14d1 = SLOAD v14cf(0x9)
    0x14d2: v14d2(0x1) = CONST 
    0x14d4: v14d4(0x1) = CONST 
    0x14d6: v14d6(0xa0) = CONST 
    0x14d8: v14d8(0x10000000000000000000000000000000000000000) = SHL v14d6(0xa0), v14d4(0x1)
    0x14d9: v14d9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14d8(0x10000000000000000000000000000000000000000), v14d2(0x1)
    0x14da: v14da = AND v14d9(0xffffffffffffffffffffffffffffffffffffffff), v14d1
    0x14db: v14db(0x14e7) = CONST 
    0x14df: v14df = CALLVALUE 
    0x14e0: v14e0(0xa) = CONST 
    0x14e2: v14e2(0x1e81) = CONST 
    0x14e6: v14e6_0 = CALLPRIVATE v14e2(0x1e81), v14e0(0xa), v14df, v14db(0x14e7)

    Begin block 0x14e7
    prev=[0x14cd], succ=[0x1503, 0x1525]
    =================================
    0x14e8: v14e8(0x40) = CONST 
    0x14ea: v14ea = MLOAD v14e8(0x40)
    0x14eb: v14eb(0x0) = CONST 
    0x14f2: v14f2 = GAS 
    0x14f3: v14f3 = CALL v14f2, v14da, v14e6_0, v14ea, v14eb(0x0), v14ea, v14eb(0x0)
    0x14f8: v14f8 = RETURNDATASIZE 
    0x14fa: v14fa(0x0) = CONST 
    0x14fd: v14fd = EQ v14f8, v14fa(0x0)
    0x14fe: v14fe(0x1525) = CONST 
    0x1502: JUMPI v14fe(0x1525), v14fd

    Begin block 0x1503
    prev=[0x14e7], succ=[0x152a]
    =================================
    0x1503: v1503(0x40) = CONST 
    0x1505: v1505 = MLOAD v1503(0x40)
    0x1508: v1508(0x1f) = CONST 
    0x150a: v150a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1508(0x1f)
    0x150b: v150b(0x3f) = CONST 
    0x150d: v150d = RETURNDATASIZE 
    0x150e: v150e = ADD v150d, v150b(0x3f)
    0x150f: v150f = AND v150e, v150a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x1511: v1511 = ADD v1505, v150f
    0x1512: v1512(0x40) = CONST 
    0x1514: MSTORE v1512(0x40), v1511
    0x1515: v1515 = RETURNDATASIZE 
    0x1517: MSTORE v1505, v1515
    0x1518: v1518 = RETURNDATASIZE 
    0x1519: v1519(0x0) = CONST 
    0x151b: v151b(0x20) = CONST 
    0x151e: v151e = ADD v1505, v151b(0x20)
    0x151f: RETURNDATACOPY v151e, v1519(0x0), v1518
    0x1520: v1520(0x152a) = CONST 
    0x1524: JUMP v1520(0x152a)

    Begin block 0x152a
    prev=[0x1503, 0x1525], succ=[0x154b]
    =================================
    0x152d: v152d(0x8) = CONST 
    0x152f: v152f = SLOAD v152d(0x8)
    0x1530: v1530(0x1) = CONST 
    0x1532: v1532(0x1) = CONST 
    0x1534: v1534(0xa0) = CONST 
    0x1536: v1536(0x10000000000000000000000000000000000000000) = SHL v1534(0xa0), v1532(0x1)
    0x1537: v1537(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1536(0x10000000000000000000000000000000000000000), v1530(0x1)
    0x1538: v1538 = AND v1537(0xffffffffffffffffffffffffffffffffffffffff), v152f
    0x153b: v153b(0x1553) = CONST 
    0x153f: v153f(0x154b) = CONST 
    0x1543: v1543 = CALLVALUE 
    0x1544: v1544(0xa) = CONST 
    0x1546: v1546(0x1e81) = CONST 
    0x154a: v154a_0 = CALLPRIVATE v1546(0x1e81), v1544(0xa), v1543, v153f(0x154b)

    Begin block 0x154b
    prev=[0x152a], succ=[0x1553]
    =================================
    0x154c: v154c = CALLVALUE 
    0x154e: v154e(0x1ec5) = CONST 
    0x1552: v1552_0 = CALLPRIVATE v154e(0x1ec5), v154a_0, v154c, v153b(0x1553)

    Begin block 0x1553
    prev=[0x154b], succ=[0x156f, 0x1591]
    =================================
    0x1554: v1554(0x40) = CONST 
    0x1556: v1556 = MLOAD v1554(0x40)
    0x1557: v1557(0x0) = CONST 
    0x155e: v155e = GAS 
    0x155f: v155f = CALL v155e, v1538, v1552_0, v1556, v1557(0x0), v1556, v1557(0x0)
    0x1564: v1564 = RETURNDATASIZE 
    0x1566: v1566(0x0) = CONST 
    0x1569: v1569 = EQ v1564, v1566(0x0)
    0x156a: v156a(0x1591) = CONST 
    0x156e: JUMPI v156a(0x1591), v1569

    Begin block 0x156f
    prev=[0x1553], succ=[0x1596]
    =================================
    0x156f: v156f(0x40) = CONST 
    0x1571: v1571 = MLOAD v156f(0x40)
    0x1574: v1574(0x1f) = CONST 
    0x1576: v1576(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v1574(0x1f)
    0x1577: v1577(0x3f) = CONST 
    0x1579: v1579 = RETURNDATASIZE 
    0x157a: v157a = ADD v1579, v1577(0x3f)
    0x157b: v157b = AND v157a, v1576(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x157d: v157d = ADD v1571, v157b
    0x157e: v157e(0x40) = CONST 
    0x1580: MSTORE v157e(0x40), v157d
    0x1581: v1581 = RETURNDATASIZE 
    0x1583: MSTORE v1571, v1581
    0x1584: v1584 = RETURNDATASIZE 
    0x1585: v1585(0x0) = CONST 
    0x1587: v1587(0x20) = CONST 
    0x158a: v158a = ADD v1571, v1587(0x20)
    0x158b: RETURNDATACOPY v158a, v1585(0x0), v1584
    0x158c: v158c(0x1596) = CONST 
    0x1590: JUMP v158c(0x1596)

    Begin block 0x1596
    prev=[0x156f, 0x1591], succ=[0x3bf3]
    =================================
    0x1599: v1599(0x40) = CONST 
    0x159c: v159c = MLOAD v1599(0x40)
    0x159d: v159d = CALLER 
    0x159f: MSTORE v159c, v159d
    0x15a0: v15a0(0x1) = CONST 
    0x15a2: v15a2(0x1) = CONST 
    0x15a4: v15a4(0xa0) = CONST 
    0x15a6: v15a6(0x10000000000000000000000000000000000000000) = SHL v15a4(0xa0), v15a2(0x1)
    0x15a7: v15a7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v15a6(0x10000000000000000000000000000000000000000), v15a0(0x1)
    0x15a9: v15a9 = AND v1434, v15a7(0xffffffffffffffffffffffffffffffffffffffff)
    0x15aa: v15aa(0x20) = CONST 
    0x15ad: v15ad = ADD v159c, v15aa(0x20)
    0x15ae: MSTORE v15ad, v15a9
    0x15b0: v15b0 = MLOAD v1599(0x40)
    0x15b1: v15b1(0x72ed24c6d9a9d33d5e42445130c1eea41c91327f01c5b876b26ecdeb7eb437c4) = CONST 
    0x15d7: v15d7(0x0) = SUB v159c, v15b0
    0x15da: v15da(0x40) = ADD v1599(0x40), v15d7(0x0)
    0x15dc: LOG1 v15b0, v15da(0x40), v15b1(0x72ed24c6d9a9d33d5e42445130c1eea41c91327f01c5b876b26ecdeb7eb437c4)
    0x15df: JUMP v427(0x3bf3)

    Begin block 0x3bf3
    prev=[0x1596], succ=[]
    =================================
    0x3bf4: STOP 

    Begin block 0x1591
    prev=[0x1553], succ=[0x1596]
    =================================
    0x1592: v1592(0x60) = CONST 

    Begin block 0x1525
    prev=[0x14e7], succ=[0x152a]
    =================================
    0x1526: v1526(0x60) = CONST 

    Begin block 0x2426B0x1447
    prev=[0x2416B0x1447], succ=[0x2429B0x1447]
    =================================
    0x2428S0x1447: v2428V1447 = ADD v14c6, v14b5

    Begin block 0x2429B0x1447
    prev=[0x2426B0x1447, 0x2433B0x1447], succ=[0x2446B0x1447, 0x2433B0x1447]
    =================================
    0x2429_0x2S0x1447: v2429_2V1447 = PHI v14c6, v243aV1447
    0x242cS0x1447: v242cV1447 = GT v2428V1447, v2429_2V1447
    0x242dS0x1447: v242dV1447 = ISZERO v242cV1447
    0x242eS0x1447: v242eV1447(0x2446) = CONST 
    0x2432S0x1447: JUMPI v242eV1447(0x2446), v242dV1447

    Begin block 0x2433B0x1447
    prev=[0x2429B0x1447], succ=[0x2429B0x1447]
    =================================
    0x2433_0x1S0x1447: v2433_1V1447 = PHI v23f0V1447, v243fV1447
    0x2433_0x2S0x1447: v2433_2V1447 = PHI v14c6, v243aV1447
    0x2434S0x1447: v2434V1447 = MLOAD v2433_2V1447
    0x2436S0x1447: SSTORE v2433_1V1447, v2434V1447
    0x2438S0x1447: v2438V1447(0x20) = CONST 
    0x243aS0x1447: v243aV1447 = ADD v2438V1447(0x20), v2433_2V1447
    0x243dS0x1447: v243dV1447(0x1) = CONST 
    0x243fS0x1447: v243fV1447 = ADD v243dV1447(0x1), v2433_1V1447
    0x2441S0x1447: v2441V1447(0x2429) = CONST 
    0x2445S0x1447: JUMP v2441V1447(0x2429)

    Begin block 0x2405B0x1447
    prev=[0x23d3B0x1447], succ=[0x2446B0x1447]
    =================================
    0x2406S0x1447: v2406V1447 = MLOAD v14c6
    0x2407S0x1447: v2407V1447(0xff) = CONST 
    0x2409S0x1447: v2409V1447(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2407V1447(0xff)
    0x240aS0x1447: v240aV1447 = AND v2409V1447(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2406V1447
    0x240dS0x1447: v240dV1447 = ADD v14b5, v14b5
    0x240eS0x1447: v240eV1447 = OR v240dV1447, v240aV1447
    0x2410S0x1447: SSTORE v14c2, v240eV1447
    0x2411S0x1447: v2411V1447(0x2446) = CONST 
    0x2415S0x1447: JUMP v2411V1447(0x2446)

}

function pools(uint256)() public {
    Begin block 0x4d2
    prev=[], succ=[0x4db, 0x4df]
    =================================
    0x4d3: v4d3 = CALLVALUE 
    0x4d5: v4d5 = ISZERO v4d3
    0x4d6: v4d6(0x4df) = CONST 
    0x4da: JUMPI v4d6(0x4df), v4d5

    Begin block 0x4db
    prev=[0x4d2], succ=[]
    =================================
    0x4db: v4db(0x0) = CONST 
    0x4de: REVERT v4db(0x0), v4db(0x0)

    Begin block 0x4df
    prev=[0x4d2], succ=[0x4f4, 0x4f8]
    =================================
    0x4e1: v4e1(0x3c14) = CONST 
    0x4e5: v4e5(0x4) = CONST 
    0x4e8: v4e8 = CALLDATASIZE 
    0x4e9: v4e9 = SUB v4e8, v4e5(0x4)
    0x4ea: v4ea(0x20) = CONST 
    0x4ed: v4ed = LT v4e9, v4ea(0x20)
    0x4ee: v4ee = ISZERO v4ed
    0x4ef: v4ef(0x4f8) = CONST 
    0x4f3: JUMPI v4ef(0x4f8), v4ee

    Begin block 0x4f4
    prev=[0x4df], succ=[]
    =================================
    0x4f4: v4f4(0x0) = CONST 
    0x4f7: REVERT v4f4(0x0), v4f4(0x0)

    Begin block 0x4f8
    prev=[0x4df], succ=[0x15e0]
    =================================
    0x4fa: v4fa = CALLDATALOAD v4e5(0x4)
    0x4fb: v4fb(0x15e0) = CONST 
    0x4ff: JUMP v4fb(0x15e0)

    Begin block 0x15e0
    prev=[0x4f8], succ=[0x15ed, 0x15ee]
    =================================
    0x15e1: v15e1(0x2) = CONST 
    0x15e5: v15e5 = SLOAD v15e1(0x2)
    0x15e7: v15e7 = LT v4fa, v15e5
    0x15e8: v15e8(0x15ee) = CONST 
    0x15ec: JUMPI v15e8(0x15ee), v15e7

    Begin block 0x15ed
    prev=[0x15e0], succ=[]
    =================================
    0x15ed: THROW 

    Begin block 0x15ee
    prev=[0x15e0], succ=[0x3c14]
    =================================
    0x15ef: v15ef(0x0) = CONST 
    0x15f3: MSTORE v15ef(0x0), v15e1(0x2)
    0x15f4: v15f4(0x20) = CONST 
    0x15f8: v15f8 = SHA3 v15ef(0x0), v15f4(0x20)
    0x15f9: v15f9 = ADD v15f8, v4fa
    0x15fa: v15fa = SLOAD v15f9
    0x15fb: v15fb(0x1) = CONST 
    0x15fd: v15fd(0x1) = CONST 
    0x15ff: v15ff(0xa0) = CONST 
    0x1601: v1601(0x10000000000000000000000000000000000000000) = SHL v15ff(0xa0), v15fd(0x1)
    0x1602: v1602(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1601(0x10000000000000000000000000000000000000000), v15fb(0x1)
    0x1603: v1603 = AND v1602(0xffffffffffffffffffffffffffffffffffffffff), v15fa
    0x1607: JUMP v4e1(0x3c14)

    Begin block 0x3c14
    prev=[0x15ee], succ=[]
    =================================
    0x3c15: v3c15(0x40) = CONST 
    0x3c18: v3c18 = MLOAD v3c15(0x40)
    0x3c19: v3c19(0x1) = CONST 
    0x3c1b: v3c1b(0x1) = CONST 
    0x3c1d: v3c1d(0xa0) = CONST 
    0x3c1f: v3c1f(0x10000000000000000000000000000000000000000) = SHL v3c1d(0xa0), v3c1b(0x1)
    0x3c20: v3c20(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c1f(0x10000000000000000000000000000000000000000), v3c19(0x1)
    0x3c23: v3c23 = AND v1603, v3c20(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c25: MSTORE v3c18, v3c23
    0x3c26: v3c26 = MLOAD v3c15(0x40)
    0x3c2a: v3c2a(0x0) = SUB v3c18, v3c26
    0x3c2b: v3c2b(0x20) = CONST 
    0x3c2d: v3c2d(0x20) = ADD v3c2b(0x20), v3c2a(0x0)
    0x3c2f: RETURN v3c26, v3c2d(0x20)

}

function estimatedProfit(address,address)() public {
    Begin block 0x500
    prev=[], succ=[0x509, 0x50d]
    =================================
    0x501: v501 = CALLVALUE 
    0x503: v503 = ISZERO v501
    0x504: v504(0x50d) = CONST 
    0x508: JUMPI v504(0x50d), v503

    Begin block 0x509
    prev=[0x500], succ=[]
    =================================
    0x509: v509(0x0) = CONST 
    0x50c: REVERT v509(0x0), v509(0x0)

    Begin block 0x50d
    prev=[0x500], succ=[0x522, 0x526]
    =================================
    0x50f: v50f(0x3c4f) = CONST 
    0x513: v513(0x4) = CONST 
    0x516: v516 = CALLDATASIZE 
    0x517: v517 = SUB v516, v513(0x4)
    0x518: v518(0x40) = CONST 
    0x51b: v51b = LT v517, v518(0x40)
    0x51c: v51c = ISZERO v51b
    0x51d: v51d(0x526) = CONST 
    0x521: JUMPI v51d(0x526), v51c

    Begin block 0x522
    prev=[0x50d], succ=[]
    =================================
    0x522: v522(0x0) = CONST 
    0x525: REVERT v522(0x0), v522(0x0)

    Begin block 0x526
    prev=[0x50d], succ=[0x1608]
    =================================
    0x528: v528(0x1) = CONST 
    0x52a: v52a(0x1) = CONST 
    0x52c: v52c(0xa0) = CONST 
    0x52e: v52e(0x10000000000000000000000000000000000000000) = SHL v52c(0xa0), v52a(0x1)
    0x52f: v52f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v52e(0x10000000000000000000000000000000000000000), v528(0x1)
    0x531: v531 = CALLDATALOAD v513(0x4)
    0x533: v533 = AND v52f(0xffffffffffffffffffffffffffffffffffffffff), v531
    0x535: v535(0x20) = CONST 
    0x537: v537(0x24) = ADD v535(0x20), v513(0x4)
    0x538: v538 = CALLDATALOAD v537(0x24)
    0x539: v539 = AND v538, v52f(0xffffffffffffffffffffffffffffffffffffffff)
    0x53a: v53a(0x1608) = CONST 
    0x53e: JUMP v53a(0x1608)

    Begin block 0x1608
    prev=[0x526], succ=[0x1633, 0x1637]
    =================================
    0x1609: v1609(0x1) = CONST 
    0x160b: v160b(0x1) = CONST 
    0x160d: v160d(0xa0) = CONST 
    0x160f: v160f(0x10000000000000000000000000000000000000000) = SHL v160d(0xa0), v160b(0x1)
    0x1610: v1610(0xffffffffffffffffffffffffffffffffffffffff) = SUB v160f(0x10000000000000000000000000000000000000000), v1609(0x1)
    0x1613: v1613 = AND v1610(0xffffffffffffffffffffffffffffffffffffffff), v533
    0x1614: v1614(0x0) = CONST 
    0x1618: MSTORE v1614(0x0), v1613
    0x1619: v1619(0x3) = CONST 
    0x161b: v161b(0x20) = CONST 
    0x161d: MSTORE v161b(0x20), v1619(0x3)
    0x161e: v161e(0x40) = CONST 
    0x1621: v1621 = SHA3 v1614(0x0), v161e(0x40)
    0x1622: v1622(0x9) = CONST 
    0x1624: v1624 = ADD v1622(0x9), v1621
    0x1625: v1625 = SLOAD v1624
    0x162a: v162a = AND v1610(0xffffffffffffffffffffffffffffffffffffffff), v539
    0x162c: v162c = AND v1625, v1610(0xffffffffffffffffffffffffffffffffffffffff)
    0x162d: v162d = EQ v162c, v162a
    0x162e: v162e(0x1637) = CONST 
    0x1632: JUMPI v162e(0x1637), v162d

    Begin block 0x1633
    prev=[0x1608], succ=[]
    =================================
    0x1633: v1633(0x0) = CONST 
    0x1636: REVERT v1633(0x0), v1633(0x0)

    Begin block 0x1637
    prev=[0x1608], succ=[0x165c, 0x1660]
    =================================
    0x1638: v1638(0x1) = CONST 
    0x163a: v163a(0x1) = CONST 
    0x163c: v163c(0xa0) = CONST 
    0x163e: v163e(0x10000000000000000000000000000000000000000) = SHL v163c(0xa0), v163a(0x1)
    0x163f: v163f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v163e(0x10000000000000000000000000000000000000000), v1638(0x1)
    0x1641: v1641 = AND v533, v163f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1642: v1642(0x0) = CONST 
    0x1646: MSTORE v1642(0x0), v1641
    0x1647: v1647(0x3) = CONST 
    0x1649: v1649(0x20) = CONST 
    0x164b: MSTORE v1649(0x20), v1647(0x3)
    0x164c: v164c(0x40) = CONST 
    0x164f: v164f = SHA3 v1642(0x0), v164c(0x40)
    0x1650: v1650(0x1) = CONST 
    0x1652: v1652 = ADD v1650(0x1), v164f
    0x1653: v1653 = SLOAD v1652
    0x1654: v1654(0x64) = CONST 
    0x1656: v1656 = LT v1654(0x64), v1653
    0x1657: v1657(0x1660) = CONST 
    0x165b: JUMPI v1657(0x1660), v1656

    Begin block 0x165c
    prev=[0x1637], succ=[]
    =================================
    0x165c: v165c(0x0) = CONST 
    0x165f: REVERT v165c(0x0), v165c(0x0)

    Begin block 0x1660
    prev=[0x1637], succ=[0x169c, 0x16a0]
    =================================
    0x1661: v1661(0x0) = CONST 
    0x1663: v1663(0x3ecd) = CONST 
    0x1668: v1668(0x1) = CONST 
    0x166a: v166a(0x1) = CONST 
    0x166c: v166c(0xa0) = CONST 
    0x166e: v166e(0x10000000000000000000000000000000000000000) = SHL v166c(0xa0), v166a(0x1)
    0x166f: v166f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v166e(0x10000000000000000000000000000000000000000), v1668(0x1)
    0x1670: v1670 = AND v166f(0xffffffffffffffffffffffffffffffffffffffff), v539
    0x1671: v1671(0x18160ddd) = CONST 
    0x1676: v1676(0x40) = CONST 
    0x1678: v1678 = MLOAD v1676(0x40)
    0x167a: v167a(0xffffffff) = CONST 
    0x167f: v167f(0x18160ddd) = AND v167a(0xffffffff), v1671(0x18160ddd)
    0x1680: v1680(0xe0) = CONST 
    0x1682: v1682(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL v1680(0xe0), v167f(0x18160ddd)
    0x1684: MSTORE v1678, v1682(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x1685: v1685(0x4) = CONST 
    0x1687: v1687 = ADD v1685(0x4), v1678
    0x1688: v1688(0x20) = CONST 
    0x168a: v168a(0x40) = CONST 
    0x168c: v168c = MLOAD v168a(0x40)
    0x168f: v168f(0x4) = SUB v1687, v168c
    0x1693: v1693 = EXTCODESIZE v1670
    0x1694: v1694 = ISZERO v1693
    0x1696: v1696 = ISZERO v1694
    0x1697: v1697(0x16a0) = CONST 
    0x169b: JUMPI v1697(0x16a0), v1696

    Begin block 0x169c
    prev=[0x1660], succ=[]
    =================================
    0x169c: v169c(0x0) = CONST 
    0x169f: REVERT v169c(0x0), v169c(0x0)

    Begin block 0x16a0
    prev=[0x1660], succ=[0x16ac, 0x16b5]
    =================================
    0x16a2: v16a2 = GAS 
    0x16a3: v16a3 = STATICCALL v16a2, v1670, v168c, v168f(0x4), v168c, v1688(0x20)
    0x16a4: v16a4 = ISZERO v16a3
    0x16a6: v16a6 = ISZERO v16a4
    0x16a7: v16a7(0x16b5) = CONST 
    0x16ab: JUMPI v16a7(0x16b5), v16a6

    Begin block 0x16ac
    prev=[0x16a0], succ=[]
    =================================
    0x16ac: v16ac = RETURNDATASIZE 
    0x16ad: v16ad(0x0) = CONST 
    0x16b0: RETURNDATACOPY v16ad(0x0), v16ad(0x0), v16ac
    0x16b1: v16b1 = RETURNDATASIZE 
    0x16b2: v16b2(0x0) = CONST 
    0x16b4: REVERT v16b2(0x0), v16b1

    Begin block 0x16b5
    prev=[0x16a0], succ=[0x16c8, 0x16cc]
    =================================
    0x16ba: v16ba(0x40) = CONST 
    0x16bc: v16bc = MLOAD v16ba(0x40)
    0x16bd: v16bd = RETURNDATASIZE 
    0x16be: v16be(0x20) = CONST 
    0x16c1: v16c1 = LT v16bd, v16be(0x20)
    0x16c2: v16c2 = ISZERO v16c1
    0x16c3: v16c3(0x16cc) = CONST 
    0x16c7: JUMPI v16c3(0x16cc), v16c2

    Begin block 0x16c8
    prev=[0x16b5], succ=[]
    =================================
    0x16c8: v16c8(0x0) = CONST 
    0x16cb: REVERT v16c8(0x0), v16c8(0x0)

    Begin block 0x16cc
    prev=[0x16b5], succ=[0x172c, 0x17300x500]
    =================================
    0x16ce: v16ce = MLOAD v16bc
    0x16cf: v16cf(0x1) = CONST 
    0x16d1: v16d1(0x1) = CONST 
    0x16d3: v16d3(0xa0) = CONST 
    0x16d5: v16d5(0x10000000000000000000000000000000000000000) = SHL v16d3(0xa0), v16d1(0x1)
    0x16d6: v16d6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16d5(0x10000000000000000000000000000000000000000), v16cf(0x1)
    0x16d9: v16d9 = AND v533, v16d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x16da: v16da(0x0) = CONST 
    0x16de: MSTORE v16da(0x0), v16d9
    0x16df: v16df(0x3) = CONST 
    0x16e1: v16e1(0x20) = CONST 
    0x16e5: MSTORE v16e1(0x20), v16df(0x3)
    0x16e6: v16e6(0x40) = CONST 
    0x16eb: v16eb = SHA3 v16da(0x0), v16e6(0x40)
    0x16ec: v16ec(0x1) = CONST 
    0x16ee: v16ee = ADD v16ec(0x1), v16eb
    0x16ef: v16ef = SLOAD v16ee
    0x16f1: v16f1 = MLOAD v16e6(0x40)
    0x16f2: v16f2(0x70a08231) = CONST 
    0x16f7: v16f7(0xe0) = CONST 
    0x16f9: v16f9(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v16f7(0xe0), v16f2(0x70a08231)
    0x16fb: MSTORE v16f1, v16f9(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x16fc: v16fc = CALLER 
    0x16fd: v16fd(0x4) = CONST 
    0x1700: v1700 = ADD v16f1, v16fd(0x4)
    0x1701: MSTORE v1700, v16fc
    0x1703: v1703 = MLOAD v16e6(0x40)
    0x1704: v1704(0x3ef4) = CONST 
    0x170d: v170d = AND v539, v16d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x170f: v170f(0x70a08231) = CONST 
    0x1715: v1715(0x24) = CONST 
    0x1719: v1719 = ADD v16f1, v1715(0x24)
    0x171e: v171e(0x0) = SUB v16f1, v1703
    0x171f: v171f(0x24) = ADD v171e(0x0), v1715(0x24)
    0x1723: v1723 = EXTCODESIZE v170d
    0x1724: v1724 = ISZERO v1723
    0x1726: v1726 = ISZERO v1724
    0x1727: v1727(0x1730) = CONST 
    0x172b: JUMPI v1727(0x1730), v1726

    Begin block 0x172c
    prev=[0x16cc], succ=[]
    =================================
    0x172c: v172c(0x0) = CONST 
    0x172f: REVERT v172c(0x0), v172c(0x0)

    Begin block 0x17300x500
    prev=[0x16cc], succ=[0x173c0x500, 0x17450x500]
    =================================
    0x17320x500: v5001732 = GAS 
    0x17330x500: v5001733 = STATICCALL v5001732, v170d, v1703, v171f(0x24), v1703, v16e1(0x20)
    0x17340x500: v5001734 = ISZERO v5001733
    0x17360x500: v5001736 = ISZERO v5001734
    0x17370x500: v5001737(0x1745) = CONST 
    0x173b0x500: JUMPI v5001737(0x1745), v5001736

    Begin block 0x173c0x500
    prev=[0x17300x500], succ=[]
    =================================
    0x173c0x500: v500173c = RETURNDATASIZE 
    0x173d0x500: v500173d(0x0) = CONST 
    0x17400x500: RETURNDATACOPY v500173d(0x0), v500173d(0x0), v500173c
    0x17410x500: v5001741 = RETURNDATASIZE 
    0x17420x500: v5001742(0x0) = CONST 
    0x17440x500: REVERT v5001742(0x0), v5001741

    Begin block 0x17450x500
    prev=[0x17300x500], succ=[0x17580x500, 0x175c0x500]
    =================================
    0x174a0x500: v500174a(0x40) = CONST 
    0x174c0x500: v500174c = MLOAD v500174a(0x40)
    0x174d0x500: v500174d = RETURNDATASIZE 
    0x174e0x500: v500174e(0x20) = CONST 
    0x17510x500: v5001751 = LT v500174d, v500174e(0x20)
    0x17520x500: v5001752 = ISZERO v5001751
    0x17530x500: v5001753(0x175c) = CONST 
    0x17570x500: JUMPI v5001753(0x175c), v5001752

    Begin block 0x17580x500
    prev=[0x17450x500], succ=[]
    =================================
    0x17580x500: v5001758(0x0) = CONST 
    0x175b0x500: REVERT v5001758(0x0), v5001758(0x0)

    Begin block 0x175c0x500
    prev=[0x17450x500], succ=[0x1e230x500]
    =================================
    0x175e0x500: v500175e = MLOAD v500174c
    0x17600x500: v5001760(0x1e23) = CONST 
    0x17640x500: JUMP v5001760(0x1e23)

    Begin block 0x1e230x500
    prev=[0x175c0x500], succ=[0x1e340x500, 0x1e2c0x500]
    =================================
    0x1e240x500: v5001e24(0x0) = CONST 
    0x1e270x500: v5001e27(0x1e34) = CONST 
    0x1e2b0x500: JUMPI v5001e27(0x1e34), v500175e

    Begin block 0x1e340x500
    prev=[0x1e230x500], succ=[0x1e410x500, 0x1e420x500]
    =================================
    0x1e370x500: v5001e37 = MUL v16ef, v500175e
    0x1e3c0x500: v5001e3c(0x1e42) = CONST 
    0x1e400x500: JUMPI v5001e3c(0x1e42), v500175e

    Begin block 0x1e410x500
    prev=[0x1e340x500], succ=[]
    =================================
    0x1e410x500: THROW 

    Begin block 0x1e420x500
    prev=[0x1e340x500], succ=[0x1e4a0x500, 0x40110x500]
    =================================
    0x1e430x500: v5001e43 = DIV v5001e37, v500175e
    0x1e440x500: v5001e44 = EQ v5001e43, v16ef
    0x1e450x500: v5001e45(0x4011) = CONST 
    0x1e490x500: JUMPI v5001e45(0x4011), v5001e44

    Begin block 0x1e4a0x500
    prev=[0x1e420x500], succ=[]
    =================================
    0x1e4a0x500: v5001e4a(0x40) = CONST 
    0x1e4c0x500: v5001e4c = MLOAD v5001e4a(0x40)
    0x1e4d0x500: v5001e4d(0x461bcd) = CONST 
    0x1e510x500: v5001e51(0xe5) = CONST 
    0x1e530x500: v5001e53(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5001e51(0xe5), v5001e4d(0x461bcd)
    0x1e550x500: MSTORE v5001e4c, v5001e53(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e560x500: v5001e56(0x4) = CONST 
    0x1e580x500: v5001e58 = ADD v5001e56(0x4), v5001e4c
    0x1e5b0x500: v5001e5b(0x20) = CONST 
    0x1e5d0x500: v5001e5d = ADD v5001e5b(0x20), v5001e58
    0x1e600x500: v5001e60(0x20) = SUB v5001e5d, v5001e58
    0x1e620x500: MSTORE v5001e58, v5001e60(0x20)
    0x1e630x500: v5001e63(0x21) = CONST 
    0x1e660x500: MSTORE v5001e5d, v5001e63(0x21)
    0x1e670x500: v5001e67(0x20) = CONST 
    0x1e690x500: v5001e69 = ADD v5001e67(0x20), v5001e5d
    0x1e6b0x500: v5001e6b(0x378a) = CONST 
    0x1e6f0x500: v5001e6f(0x21) = CONST 
    0x1e720x500: CODECOPY v5001e69, v5001e6b(0x378a), v5001e6f(0x21)
    0x1e730x500: v5001e73(0x40) = CONST 
    0x1e750x500: v5001e75 = ADD v5001e73(0x40), v5001e69
    0x1e790x500: v5001e79(0x40) = CONST 
    0x1e7b0x500: v5001e7b = MLOAD v5001e79(0x40)
    0x1e7e0x500: v5001e7e(0x84) = SUB v5001e75, v5001e7b
    0x1e800x500: REVERT v5001e7b, v5001e7e(0x84)

    Begin block 0x40110x500
    prev=[0x1e420x500], succ=[0x3ef4]
    =================================
    0x40170x500: JUMP v1704(0x3ef4)

    Begin block 0x3ef4
    prev=[0xf450x500, 0x40110x500], succ=[0x1e810x500]
    =================================
    0x3ef6: v3ef6(0x1e81) = CONST 
    0x3efa: JUMP v3ef6(0x1e81)

    Begin block 0x1e810x500
    prev=[0x3ef4], succ=[0x21200x500]
    =================================
    0x1e820x500: v5001e82(0x0) = CONST 
    0x1e840x500: v5001e84(0x4037) = CONST 
    0x1e8a0x500: v5001e8a(0x40) = CONST 
    0x1e8c0x500: v5001e8c = MLOAD v5001e8a(0x40)
    0x1e8e0x500: v5001e8e(0x40) = CONST 
    0x1e900x500: v5001e90 = ADD v5001e8e(0x40), v5001e8c
    0x1e910x500: v5001e91(0x40) = CONST 
    0x1e930x500: MSTORE v5001e91(0x40), v5001e90
    0x1e950x500: v5001e95(0x1a) = CONST 
    0x1e980x500: MSTORE v5001e8c, v5001e95(0x1a)
    0x1e990x500: v5001e99(0x20) = CONST 
    0x1e9b0x500: v5001e9b = ADD v5001e99(0x20), v5001e8c
    0x1e9c0x500: v5001e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1ebe0x500: MSTORE v5001e9b, v5001e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1ec00x500: v5001ec0(0x2120) = CONST 
    0x1ec40x500: JUMP v5001ec0(0x2120)

    Begin block 0x21200x500
    prev=[0x1e810x500], succ=[0x212a0x500, 0x21b00x500]
    =================================
    0x21210x500: v5002121(0x0) = CONST 
    0x21250x500: v5002125(0x21b0) = CONST 
    0x21290x500: JUMPI v5002125(0x21b0), v16ce

    Begin block 0x212a0x500
    prev=[0x21200x500], succ=[0x215a0x500]
    =================================
    0x212a0x500: v500212a(0x40) = CONST 
    0x212c0x500: v500212c = MLOAD v500212a(0x40)
    0x212d0x500: v500212d(0x461bcd) = CONST 
    0x21310x500: v5002131(0xe5) = CONST 
    0x21330x500: v5002133(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5002131(0xe5), v500212d(0x461bcd)
    0x21350x500: MSTORE v500212c, v5002133(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21360x500: v5002136(0x4) = CONST 
    0x21380x500: v5002138 = ADD v5002136(0x4), v500212c
    0x213b0x500: v500213b(0x20) = CONST 
    0x213d0x500: v500213d = ADD v500213b(0x20), v5002138
    0x21400x500: v5002140(0x20) = SUB v500213d, v5002138
    0x21420x500: MSTORE v5002138, v5002140(0x20)
    0x21460x500: v5002146(0x1a) = MLOAD v5001e8c
    0x21480x500: MSTORE v500213d, v5002146(0x1a)
    0x21490x500: v5002149(0x20) = CONST 
    0x214b0x500: v500214b = ADD v5002149(0x20), v500213d
    0x214f0x500: v500214f(0x1a) = MLOAD v5001e8c
    0x21510x500: v5002151(0x20) = CONST 
    0x21530x500: v5002153 = ADD v5002151(0x20), v5001e8c
    0x21580x500: v5002158(0x0) = CONST 

    Begin block 0x215a0x500
    prev=[0x212a0x500, 0x21640x500], succ=[0x21740x500, 0x21640x500]
    =================================
    0x215a0x500_0x0: v215a500_0 = PHI v500216e, v5002158(0x0)
    0x215d0x500: v500215d = LT v215a500_0, v500214f(0x1a)
    0x215e0x500: v500215e = ISZERO v500215d
    0x215f0x500: v500215f(0x2174) = CONST 
    0x21630x500: JUMPI v500215f(0x2174), v500215e

    Begin block 0x21740x500
    prev=[0x215a0x500], succ=[0x21a20x500, 0x21890x500]
    =================================
    0x217d0x500: v500217d = ADD v500214f(0x1a), v500214b
    0x217f0x500: v500217f(0x1f) = CONST 
    0x21810x500: v5002181(0x1a) = AND v500217f(0x1f), v500214f(0x1a)
    0x21830x500: v5002183 = ISZERO v5002181(0x1a)
    0x21840x500: v5002184(0x21a2) = CONST 
    0x21880x500: JUMPI v5002184(0x21a2), v5002183

    Begin block 0x21a20x500
    prev=[0x21740x500, 0x21890x500], succ=[]
    =================================
    0x21a20x500_0x1: v21a2500_1 = PHI v500219f, v500217d
    0x21a80x500: v50021a8(0x40) = CONST 
    0x21aa0x500: v50021aa = MLOAD v50021a8(0x40)
    0x21ad0x500: v50021ad = SUB v21a2500_1, v50021aa
    0x21af0x500: REVERT v50021aa, v50021ad

    Begin block 0x21890x500
    prev=[0x21740x500], succ=[0x21a20x500]
    =================================
    0x218b0x500: v500218b = SUB v500217d, v5002181(0x1a)
    0x218d0x500: v500218d = MLOAD v500218b
    0x218e0x500: v500218e(0x1) = CONST 
    0x21910x500: v5002191(0x20) = CONST 
    0x21930x500: v5002193(0x6) = SUB v5002191(0x20), v5002181(0x1a)
    0x21940x500: v5002194(0x100) = CONST 
    0x21970x500: v5002197(0x1000000000000) = EXP v5002194(0x100), v5002193(0x6)
    0x21980x500: v5002198(0xffffffffffff) = SUB v5002197(0x1000000000000), v500218e(0x1)
    0x21990x500: v5002199 = NOT v5002198(0xffffffffffff)
    0x219a0x500: v500219a = AND v5002199, v500218d
    0x219c0x500: MSTORE v500218b, v500219a
    0x219d0x500: v500219d(0x20) = CONST 
    0x219f0x500: v500219f = ADD v500219d(0x20), v500218b

    Begin block 0x21640x500
    prev=[0x215a0x500], succ=[0x215a0x500]
    =================================
    0x21640x500_0x0: v2164500_0 = PHI v500216e, v5002158(0x0)
    0x21660x500: v5002166 = ADD v2164500_0, v5002153
    0x21670x500: v5002167 = MLOAD v5002166
    0x216a0x500: v500216a = ADD v2164500_0, v500214b
    0x216b0x500: MSTORE v500216a, v5002167
    0x216c0x500: v500216c(0x20) = CONST 
    0x216e0x500: v500216e = ADD v500216c(0x20), v2164500_0
    0x216f0x500: v500216f(0x215a) = CONST 
    0x21730x500: JUMP v500216f(0x215a)

    Begin block 0x21b00x500
    prev=[0x21200x500], succ=[0x21bc0x500, 0x21bd0x500]
    =================================
    0x21b20x500: v50021b2(0x0) = CONST 
    0x21b70x500: v50021b7(0x21bd) = CONST 
    0x21bb0x500: JUMPI v50021b7(0x21bd), v16ce

    Begin block 0x21bc0x500
    prev=[0x21b00x500], succ=[]
    =================================
    0x21bc0x500: THROW 

    Begin block 0x21bd0x500
    prev=[0x21b00x500], succ=[0x40370x500]
    =================================
    0x21bd0x500_0x0: v21bd500_0 = PHI v5001e37, v5001e2d(0x0)
    0x21be0x500: v50021be = DIV v21bd500_0, v16ce
    0x21c60x500: JUMP v5001e84(0x4037)

    Begin block 0x40370x500
    prev=[0x21bd0x500], succ=[0x3ecd]
    =================================
    0x403d0x500: JUMP v1663(0x3ecd)

    Begin block 0x3ecd
    prev=[0x40370x500], succ=[0x3c4f]
    =================================
    0x3ed4: JUMP v50f(0x3c4f)

    Begin block 0x3c4f
    prev=[0x3ecd], succ=[]
    =================================
    0x3c50: v3c50(0x40) = CONST 
    0x3c53: v3c53 = MLOAD v3c50(0x40)
    0x3c56: MSTORE v3c53, v50021be
    0x3c57: v3c57 = MLOAD v3c50(0x40)
    0x3c5b: v3c5b(0x0) = SUB v3c53, v3c57
    0x3c5c: v3c5c(0x20) = CONST 
    0x3c5e: v3c5e(0x20) = ADD v3c5c(0x20), v3c5b(0x0)
    0x3c60: RETURN v3c57, v3c5e(0x20)

    Begin block 0x1e2c0x500
    prev=[0x1e230x500], succ=[0xf450x500]
    =================================
    0x1e2d0x500: v5001e2d(0x0) = CONST 
    0x1e2f0x500: v5001e2f(0xf45) = CONST 
    0x1e330x500: JUMP v5001e2f(0xf45)

    Begin block 0xf450x500
    prev=[0x1e2c0x500], succ=[0x3ef4]
    =================================
    0xf4a0x500: JUMP v1704(0x3ef4)

}

function contractManager()() public {
    Begin block 0x53f
    prev=[], succ=[0x548, 0x54c]
    =================================
    0x540: v540 = CALLVALUE 
    0x542: v542 = ISZERO v540
    0x543: v543(0x54c) = CONST 
    0x547: JUMPI v543(0x54c), v542

    Begin block 0x548
    prev=[0x53f], succ=[]
    =================================
    0x548: v548(0x0) = CONST 
    0x54b: REVERT v548(0x0), v548(0x0)

    Begin block 0x54c
    prev=[0x53f], succ=[0x176d]
    =================================
    0x54e: v54e(0x3c80) = CONST 
    0x552: v552(0x176d) = CONST 
    0x556: JUMP v552(0x176d)

    Begin block 0x176d
    prev=[0x54c], succ=[0x3c80]
    =================================
    0x176e: v176e(0xb) = CONST 
    0x1770: v1770 = SLOAD v176e(0xb)
    0x1771: v1771(0x1) = CONST 
    0x1773: v1773(0x1) = CONST 
    0x1775: v1775(0xa0) = CONST 
    0x1777: v1777(0x10000000000000000000000000000000000000000) = SHL v1775(0xa0), v1773(0x1)
    0x1778: v1778(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1777(0x10000000000000000000000000000000000000000), v1771(0x1)
    0x1779: v1779 = AND v1778(0xffffffffffffffffffffffffffffffffffffffff), v1770
    0x177b: JUMP v54e(0x3c80)

    Begin block 0x3c80
    prev=[0x176d], succ=[]
    =================================
    0x3c81: v3c81(0x40) = CONST 
    0x3c84: v3c84 = MLOAD v3c81(0x40)
    0x3c85: v3c85(0x1) = CONST 
    0x3c87: v3c87(0x1) = CONST 
    0x3c89: v3c89(0xa0) = CONST 
    0x3c8b: v3c8b(0x10000000000000000000000000000000000000000) = SHL v3c89(0xa0), v3c87(0x1)
    0x3c8c: v3c8c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c8b(0x10000000000000000000000000000000000000000), v3c85(0x1)
    0x3c8f: v3c8f = AND v1779, v3c8c(0xffffffffffffffffffffffffffffffffffffffff)
    0x3c91: MSTORE v3c84, v3c8f
    0x3c92: v3c92 = MLOAD v3c81(0x40)
    0x3c96: v3c96(0x0) = SUB v3c84, v3c92
    0x3c97: v3c97(0x20) = CONST 
    0x3c99: v3c99(0x20) = ADD v3c97(0x20), v3c96(0x0)
    0x3c9b: RETURN v3c92, v3c99(0x20)

}

function fundContract()() public {
    Begin block 0x557
    prev=[], succ=[0x560, 0x564]
    =================================
    0x558: v558 = CALLVALUE 
    0x55a: v55a = ISZERO v558
    0x55b: v55b(0x564) = CONST 
    0x55f: JUMPI v55b(0x564), v55a

    Begin block 0x560
    prev=[0x557], succ=[]
    =================================
    0x560: v560(0x0) = CONST 
    0x563: REVERT v560(0x0), v560(0x0)

    Begin block 0x564
    prev=[0x557], succ=[0x177c]
    =================================
    0x566: v566(0x3cbb) = CONST 
    0x56a: v56a(0x177c) = CONST 
    0x56e: JUMP v56a(0x177c)

    Begin block 0x177c
    prev=[0x564], succ=[0x3cbb]
    =================================
    0x177d: v177d(0x5) = CONST 
    0x177f: v177f = SLOAD v177d(0x5)
    0x1780: v1780(0x1) = CONST 
    0x1782: v1782(0x1) = CONST 
    0x1784: v1784(0xa0) = CONST 
    0x1786: v1786(0x10000000000000000000000000000000000000000) = SHL v1784(0xa0), v1782(0x1)
    0x1787: v1787(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1786(0x10000000000000000000000000000000000000000), v1780(0x1)
    0x1788: v1788 = AND v1787(0xffffffffffffffffffffffffffffffffffffffff), v177f
    0x178a: JUMP v566(0x3cbb)

    Begin block 0x3cbb
    prev=[0x177c], succ=[]
    =================================
    0x3cbc: v3cbc(0x40) = CONST 
    0x3cbf: v3cbf = MLOAD v3cbc(0x40)
    0x3cc0: v3cc0(0x1) = CONST 
    0x3cc2: v3cc2(0x1) = CONST 
    0x3cc4: v3cc4(0xa0) = CONST 
    0x3cc6: v3cc6(0x10000000000000000000000000000000000000000) = SHL v3cc4(0xa0), v3cc2(0x1)
    0x3cc7: v3cc7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3cc6(0x10000000000000000000000000000000000000000), v3cc0(0x1)
    0x3cca: v3cca = AND v1788, v3cc7(0xffffffffffffffffffffffffffffffffffffffff)
    0x3ccc: MSTORE v3cbf, v3cca
    0x3ccd: v3ccd = MLOAD v3cbc(0x40)
    0x3cd1: v3cd1(0x0) = SUB v3cbf, v3ccd
    0x3cd2: v3cd2(0x20) = CONST 
    0x3cd4: v3cd4(0x20) = ADD v3cd2(0x20), v3cd1(0x0)
    0x3cd6: RETURN v3ccd, v3cd4(0x20)

}

function managerInit(address)() public {
    Begin block 0x56f
    prev=[], succ=[0x578, 0x57c]
    =================================
    0x570: v570 = CALLVALUE 
    0x572: v572 = ISZERO v570
    0x573: v573(0x57c) = CONST 
    0x577: JUMPI v573(0x57c), v572

    Begin block 0x578
    prev=[0x56f], succ=[]
    =================================
    0x578: v578(0x0) = CONST 
    0x57b: REVERT v578(0x0), v578(0x0)

    Begin block 0x57c
    prev=[0x56f], succ=[0x591, 0x595]
    =================================
    0x57e: v57e(0x3cf6) = CONST 
    0x582: v582(0x4) = CONST 
    0x585: v585 = CALLDATASIZE 
    0x586: v586 = SUB v585, v582(0x4)
    0x587: v587(0x20) = CONST 
    0x58a: v58a = LT v586, v587(0x20)
    0x58b: v58b = ISZERO v58a
    0x58c: v58c(0x595) = CONST 
    0x590: JUMPI v58c(0x595), v58b

    Begin block 0x591
    prev=[0x57c], succ=[]
    =================================
    0x591: v591(0x0) = CONST 
    0x594: REVERT v591(0x0), v591(0x0)

    Begin block 0x595
    prev=[0x57c], succ=[0x178b]
    =================================
    0x597: v597 = CALLDATALOAD v582(0x4)
    0x598: v598(0x1) = CONST 
    0x59a: v59a(0x1) = CONST 
    0x59c: v59c(0xa0) = CONST 
    0x59e: v59e(0x10000000000000000000000000000000000000000) = SHL v59c(0xa0), v59a(0x1)
    0x59f: v59f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v59e(0x10000000000000000000000000000000000000000), v598(0x1)
    0x5a0: v5a0 = AND v59f(0xffffffffffffffffffffffffffffffffffffffff), v597
    0x5a1: v5a1(0x178b) = CONST 
    0x5a5: JUMP v5a1(0x178b)

    Begin block 0x178b
    prev=[0x595], succ=[0x1798, 0x179c]
    =================================
    0x178c: v178c(0x0) = CONST 
    0x178e: v178e = SLOAD v178c(0x0)
    0x178f: v178f(0xff) = CONST 
    0x1791: v1791 = AND v178f(0xff), v178e
    0x1792: v1792 = ISZERO v1791
    0x1793: v1793(0x179c) = CONST 
    0x1797: JUMPI v1793(0x179c), v1792

    Begin block 0x1798
    prev=[0x178b], succ=[]
    =================================
    0x1798: v1798(0x0) = CONST 
    0x179b: REVERT v1798(0x0), v1798(0x0)

    Begin block 0x179c
    prev=[0x178b], succ=[0x2055]
    =================================
    0x179d: v179d(0x0) = CONST 
    0x17a0: v17a0 = SLOAD v179d(0x0)
    0x17a1: v17a1(0x100) = CONST 
    0x17a4: v17a4(0x1) = CONST 
    0x17a6: v17a6(0xa8) = CONST 
    0x17a8: v17a8(0x1000000000000000000000000000000000000000000) = SHL v17a6(0xa8), v17a4(0x1)
    0x17a9: v17a9(0xffffffffffffffffffffffffffffffffffffffff00) = SUB v17a8(0x1000000000000000000000000000000000000000000), v17a1(0x100)
    0x17aa: v17aa(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff) = NOT v17a9(0xffffffffffffffffffffffffffffffffffffffff00)
    0x17ab: v17ab = AND v17aa(0xffffffffffffffffffffff0000000000000000000000000000000000000000ff), v17a0
    0x17ac: v17ac(0x100) = CONST 
    0x17af: v17af(0x1) = CONST 
    0x17b1: v17b1(0x1) = CONST 
    0x17b3: v17b3(0xa0) = CONST 
    0x17b5: v17b5(0x10000000000000000000000000000000000000000) = SHL v17b3(0xa0), v17b1(0x1)
    0x17b6: v17b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17b5(0x10000000000000000000000000000000000000000), v17af(0x1)
    0x17b8: v17b8 = AND v5a0, v17b6(0xffffffffffffffffffffffffffffffffffffffff)
    0x17b9: v17b9 = MUL v17b8, v17ac(0x100)
    0x17ba: v17ba = OR v17b9, v17ab
    0x17bc: SSTORE v179d(0x0), v17ba
    0x17bd: v17bd(0x3f1a) = CONST 
    0x17c1: v17c1(0x2055) = CONST 
    0x17c5: JUMP v17c1(0x2055)

    Begin block 0x2055
    prev=[0x179c], succ=[0x3f1a]
    =================================
    0x2056: v2056(0x0) = CONST 
    0x2059: v2059 = SLOAD v2056(0x0)
    0x205a: v205a(0xff) = CONST 
    0x205c: v205c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v205a(0xff)
    0x205d: v205d = AND v205c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2059
    0x205e: v205e(0x1) = CONST 
    0x2060: v2060 = OR v205e(0x1), v205d
    0x2062: SSTORE v2056(0x0), v2060
    0x2063: JUMP v17bd(0x3f1a)

    Begin block 0x3f1a
    prev=[0x2055], succ=[0x3cf6]
    =================================
    0x3f1c: JUMP v57e(0x3cf6)

    Begin block 0x3cf6
    prev=[0x3f1a], succ=[]
    =================================
    0x3cf7: STOP 

}

function isSelfManager(address)() public {
    Begin block 0x5a6
    prev=[], succ=[0x5af, 0x5b3]
    =================================
    0x5a7: v5a7 = CALLVALUE 
    0x5a9: v5a9 = ISZERO v5a7
    0x5aa: v5aa(0x5b3) = CONST 
    0x5ae: JUMPI v5aa(0x5b3), v5a9

    Begin block 0x5af
    prev=[0x5a6], succ=[]
    =================================
    0x5af: v5af(0x0) = CONST 
    0x5b2: REVERT v5af(0x0), v5af(0x0)

    Begin block 0x5b3
    prev=[0x5a6], succ=[0x5c8, 0x5cc]
    =================================
    0x5b5: v5b5(0x3d17) = CONST 
    0x5b9: v5b9(0x4) = CONST 
    0x5bc: v5bc = CALLDATASIZE 
    0x5bd: v5bd = SUB v5bc, v5b9(0x4)
    0x5be: v5be(0x20) = CONST 
    0x5c1: v5c1 = LT v5bd, v5be(0x20)
    0x5c2: v5c2 = ISZERO v5c1
    0x5c3: v5c3(0x5cc) = CONST 
    0x5c7: JUMPI v5c3(0x5cc), v5c2

    Begin block 0x5c8
    prev=[0x5b3], succ=[]
    =================================
    0x5c8: v5c8(0x0) = CONST 
    0x5cb: REVERT v5c8(0x0), v5c8(0x0)

    Begin block 0x5cc
    prev=[0x5b3], succ=[0x17c6]
    =================================
    0x5ce: v5ce = CALLDATALOAD v5b9(0x4)
    0x5cf: v5cf(0x1) = CONST 
    0x5d1: v5d1(0x1) = CONST 
    0x5d3: v5d3(0xa0) = CONST 
    0x5d5: v5d5(0x10000000000000000000000000000000000000000) = SHL v5d3(0xa0), v5d1(0x1)
    0x5d6: v5d6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5d5(0x10000000000000000000000000000000000000000), v5cf(0x1)
    0x5d7: v5d7 = AND v5d6(0xffffffffffffffffffffffffffffffffffffffff), v5ce
    0x5d8: v5d8(0x17c6) = CONST 
    0x5dc: JUMP v5d8(0x17c6)

    Begin block 0x17c6
    prev=[0x5cc], succ=[0x17f4, 0x17ec]
    =================================
    0x17c7: v17c7(0x1) = CONST 
    0x17c9: v17c9(0x1) = CONST 
    0x17cb: v17cb(0xa0) = CONST 
    0x17cd: v17cd(0x10000000000000000000000000000000000000000) = SHL v17cb(0xa0), v17c9(0x1)
    0x17ce: v17ce(0xffffffffffffffffffffffffffffffffffffffff) = SUB v17cd(0x10000000000000000000000000000000000000000), v17c7(0x1)
    0x17d1: v17d1 = AND v17ce(0xffffffffffffffffffffffffffffffffffffffff), v5d7
    0x17d2: v17d2(0x0) = CONST 
    0x17d6: MSTORE v17d2(0x0), v17d1
    0x17d7: v17d7(0x3) = CONST 
    0x17d9: v17d9(0x20) = CONST 
    0x17db: MSTORE v17d9(0x20), v17d7(0x3)
    0x17dc: v17dc(0x40) = CONST 
    0x17df: v17df = SHA3 v17d2(0x0), v17dc(0x40)
    0x17e0: v17e0(0x9) = CONST 
    0x17e2: v17e2 = ADD v17e0(0x9), v17df
    0x17e3: v17e3 = SLOAD v17e2
    0x17e6: v17e6 = AND v17ce(0xffffffffffffffffffffffffffffffffffffffff), v17e3
    0x17e7: v17e7(0x17f4) = CONST 
    0x17eb: JUMPI v17e7(0x17f4), v17e6

    Begin block 0x17f4
    prev=[0x17c6], succ=[0x17f8]
    =================================
    0x17f6: v17f6(0x1) = CONST 

    Begin block 0x17f8
    prev=[0x17f4, 0x17ec], succ=[0x3d17]
    =================================
    0x17fc: JUMP v5b5(0x3d17)

    Begin block 0x3d17
    prev=[0x17f8], succ=[]
    =================================
    0x3d17_0x0: v3d17_0 = PHI v17ed(0x0), v17f6(0x1)
    0x3d18: v3d18(0x40) = CONST 
    0x3d1b: v3d1b = MLOAD v3d18(0x40)
    0x3d1d: v3d1d = ISZERO v3d17_0
    0x3d1e: v3d1e = ISZERO v3d1d
    0x3d20: MSTORE v3d1b, v3d1e
    0x3d21: v3d21 = MLOAD v3d18(0x40)
    0x3d25: v3d25(0x0) = SUB v3d1b, v3d21
    0x3d26: v3d26(0x20) = CONST 
    0x3d28: v3d28(0x20) = ADD v3d26(0x20), v3d25(0x0)
    0x3d2a: RETURN v3d21, v3d28(0x20)

    Begin block 0x17ec
    prev=[0x17c6], succ=[0x17f8]
    =================================
    0x17ed: v17ed(0x0) = CONST 
    0x17ef: v17ef(0x17f8) = CONST 
    0x17f3: JUMP v17ef(0x17f8)

}

function claimProfit(address,address)() public {
    Begin block 0x5dd
    prev=[], succ=[0x5e6, 0x5ea]
    =================================
    0x5de: v5de = CALLVALUE 
    0x5e0: v5e0 = ISZERO v5de
    0x5e1: v5e1(0x5ea) = CONST 
    0x5e5: JUMPI v5e1(0x5ea), v5e0

    Begin block 0x5e6
    prev=[0x5dd], succ=[]
    =================================
    0x5e6: v5e6(0x0) = CONST 
    0x5e9: REVERT v5e6(0x0), v5e6(0x0)

    Begin block 0x5ea
    prev=[0x5dd], succ=[0x5ff, 0x603]
    =================================
    0x5ec: v5ec(0x3d4a) = CONST 
    0x5f0: v5f0(0x4) = CONST 
    0x5f3: v5f3 = CALLDATASIZE 
    0x5f4: v5f4 = SUB v5f3, v5f0(0x4)
    0x5f5: v5f5(0x40) = CONST 
    0x5f8: v5f8 = LT v5f4, v5f5(0x40)
    0x5f9: v5f9 = ISZERO v5f8
    0x5fa: v5fa(0x603) = CONST 
    0x5fe: JUMPI v5fa(0x603), v5f9

    Begin block 0x5ff
    prev=[0x5ea], succ=[]
    =================================
    0x5ff: v5ff(0x0) = CONST 
    0x602: REVERT v5ff(0x0), v5ff(0x0)

    Begin block 0x603
    prev=[0x5ea], succ=[0x17fd]
    =================================
    0x605: v605(0x1) = CONST 
    0x607: v607(0x1) = CONST 
    0x609: v609(0xa0) = CONST 
    0x60b: v60b(0x10000000000000000000000000000000000000000) = SHL v609(0xa0), v607(0x1)
    0x60c: v60c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v60b(0x10000000000000000000000000000000000000000), v605(0x1)
    0x60e: v60e = CALLDATALOAD v5f0(0x4)
    0x610: v610 = AND v60c(0xffffffffffffffffffffffffffffffffffffffff), v60e
    0x612: v612(0x20) = CONST 
    0x614: v614(0x24) = ADD v612(0x20), v5f0(0x4)
    0x615: v615 = CALLDATALOAD v614(0x24)
    0x616: v616 = AND v615, v60c(0xffffffffffffffffffffffffffffffffffffffff)
    0x617: v617(0x17fd) = CONST 
    0x61b: JUMP v617(0x17fd)

    Begin block 0x17fd
    prev=[0x603], succ=[0x180e, 0x1845]
    =================================
    0x17fe: v17fe(0x0) = CONST 
    0x1800: v1800 = SLOAD v17fe(0x0)
    0x1801: v1801(0xff) = CONST 
    0x1803: v1803 = AND v1801(0xff), v1800
    0x1804: v1804 = ISZERO v1803
    0x1805: v1805 = ISZERO v1804
    0x1806: v1806(0x1) = CONST 
    0x1808: v1808 = EQ v1806(0x1), v1805
    0x1809: v1809(0x1845) = CONST 
    0x180d: JUMPI v1809(0x1845), v1808

    Begin block 0x180e
    prev=[0x17fd], succ=[]
    =================================
    0x180e: v180e(0x40) = CONST 
    0x1810: v1810 = MLOAD v180e(0x40)
    0x1811: v1811(0x461bcd) = CONST 
    0x1815: v1815(0xe5) = CONST 
    0x1817: v1817(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1815(0xe5), v1811(0x461bcd)
    0x1819: MSTORE v1810, v1817(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x181a: v181a(0x4) = CONST 
    0x181c: v181c = ADD v181a(0x4), v1810
    0x181f: v181f(0x20) = CONST 
    0x1821: v1821 = ADD v181f(0x20), v181c
    0x1824: v1824(0x20) = SUB v1821, v181c
    0x1826: MSTORE v181c, v1824(0x20)
    0x1827: v1827(0x32) = CONST 
    0x182a: MSTORE v1821, v1827(0x32)
    0x182b: v182b(0x20) = CONST 
    0x182d: v182d = ADD v182b(0x20), v1821
    0x182f: v182f(0x37d5) = CONST 
    0x1833: v1833(0x32) = CONST 
    0x1836: CODECOPY v182d, v182f(0x37d5), v1833(0x32)
    0x1837: v1837(0x40) = CONST 
    0x1839: v1839 = ADD v1837(0x40), v182d
    0x183d: v183d(0x40) = CONST 
    0x183f: v183f = MLOAD v183d(0x40)
    0x1842: v1842(0x84) = SUB v1839, v183f
    0x1844: REVERT v183f, v1842(0x84)

    Begin block 0x1845
    prev=[0x17fd], succ=[0x186e, 0x1872]
    =================================
    0x1846: v1846(0x1) = CONST 
    0x1848: v1848(0x1) = CONST 
    0x184a: v184a(0xa0) = CONST 
    0x184c: v184c(0x10000000000000000000000000000000000000000) = SHL v184a(0xa0), v1848(0x1)
    0x184d: v184d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v184c(0x10000000000000000000000000000000000000000), v1846(0x1)
    0x1850: v1850 = AND v184d(0xffffffffffffffffffffffffffffffffffffffff), v610
    0x1851: v1851(0x0) = CONST 
    0x1855: MSTORE v1851(0x0), v1850
    0x1856: v1856(0x3) = CONST 
    0x1858: v1858(0x20) = CONST 
    0x185a: MSTORE v1858(0x20), v1856(0x3)
    0x185b: v185b(0x40) = CONST 
    0x185e: v185e = SHA3 v1851(0x0), v185b(0x40)
    0x185f: v185f(0x9) = CONST 
    0x1861: v1861 = ADD v185f(0x9), v185e
    0x1862: v1862 = SLOAD v1861
    0x1864: v1864 = AND v184d(0xffffffffffffffffffffffffffffffffffffffff), v1862
    0x1867: v1867 = AND v616, v184d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1868: v1868 = EQ v1867, v1864
    0x1869: v1869(0x1872) = CONST 
    0x186d: JUMPI v1869(0x1872), v1868

    Begin block 0x186e
    prev=[0x1845], succ=[]
    =================================
    0x186e: v186e(0x0) = CONST 
    0x1871: REVERT v186e(0x0), v186e(0x0)

    Begin block 0x1872
    prev=[0x1845], succ=[0x18b7, 0x18bb]
    =================================
    0x1873: v1873(0x40) = CONST 
    0x1876: v1876 = MLOAD v1873(0x40)
    0x1877: v1877(0xc9df977) = CONST 
    0x187c: v187c(0xe1) = CONST 
    0x187e: v187e(0x193bf2ee00000000000000000000000000000000000000000000000000000000) = SHL v187c(0xe1), v1877(0xc9df977)
    0x1880: MSTORE v1876, v187e(0x193bf2ee00000000000000000000000000000000000000000000000000000000)
    0x1881: v1881 = CALLER 
    0x1882: v1882(0x4) = CONST 
    0x1885: v1885 = ADD v1876, v1882(0x4)
    0x1886: MSTORE v1885, v1881
    0x1888: v1888 = MLOAD v1873(0x40)
    0x1889: v1889(0x1) = CONST 
    0x188b: v188b(0x1) = CONST 
    0x188d: v188d(0xa0) = CONST 
    0x188f: v188f(0x10000000000000000000000000000000000000000) = SHL v188d(0xa0), v188b(0x1)
    0x1890: v1890(0xffffffffffffffffffffffffffffffffffffffff) = SUB v188f(0x10000000000000000000000000000000000000000), v1889(0x1)
    0x1892: v1892 = AND v616, v1890(0xffffffffffffffffffffffffffffffffffffffff)
    0x1894: v1894(0x193bf2ee) = CONST 
    0x189a: v189a(0x24) = CONST 
    0x189e: v189e = ADD v1876, v189a(0x24)
    0x18a0: v18a0(0x20) = CONST 
    0x18a7: v18a7(0x0) = SUB v1876, v1888
    0x18a8: v18a8(0x24) = ADD v18a7(0x0), v189a(0x24)
    0x18aa: v18aa(0x0) = CONST 
    0x18ae: v18ae = EXTCODESIZE v1892
    0x18af: v18af = ISZERO v18ae
    0x18b1: v18b1 = ISZERO v18af
    0x18b2: v18b2(0x18bb) = CONST 
    0x18b6: JUMPI v18b2(0x18bb), v18b1

    Begin block 0x18b7
    prev=[0x1872], succ=[]
    =================================
    0x18b7: v18b7(0x0) = CONST 
    0x18ba: REVERT v18b7(0x0), v18b7(0x0)

    Begin block 0x18bb
    prev=[0x1872], succ=[0x18c7, 0x18d0]
    =================================
    0x18bd: v18bd = GAS 
    0x18be: v18be = CALL v18bd, v1892, v18aa(0x0), v1888, v18a8(0x24), v1888, v18a0(0x20)
    0x18bf: v18bf = ISZERO v18be
    0x18c1: v18c1 = ISZERO v18bf
    0x18c2: v18c2(0x18d0) = CONST 
    0x18c6: JUMPI v18c2(0x18d0), v18c1

    Begin block 0x18c7
    prev=[0x18bb], succ=[]
    =================================
    0x18c7: v18c7 = RETURNDATASIZE 
    0x18c8: v18c8(0x0) = CONST 
    0x18cb: RETURNDATACOPY v18c8(0x0), v18c8(0x0), v18c7
    0x18cc: v18cc = RETURNDATASIZE 
    0x18cd: v18cd(0x0) = CONST 
    0x18cf: REVERT v18cd(0x0), v18cc

    Begin block 0x18d0
    prev=[0x18bb], succ=[0x18e3, 0x18e7]
    =================================
    0x18d5: v18d5(0x40) = CONST 
    0x18d7: v18d7 = MLOAD v18d5(0x40)
    0x18d8: v18d8 = RETURNDATASIZE 
    0x18d9: v18d9(0x20) = CONST 
    0x18dc: v18dc = LT v18d8, v18d9(0x20)
    0x18dd: v18dd = ISZERO v18dc
    0x18de: v18de(0x18e7) = CONST 
    0x18e2: JUMPI v18de(0x18e7), v18dd

    Begin block 0x18e3
    prev=[0x18d0], succ=[]
    =================================
    0x18e3: v18e3(0x0) = CONST 
    0x18e6: REVERT v18e3(0x0), v18e3(0x0)

    Begin block 0x18e7
    prev=[0x18d0], succ=[0x18ef, 0x193b]
    =================================
    0x18e9: v18e9 = MLOAD v18d7
    0x18ea: v18ea(0x193b) = CONST 
    0x18ee: JUMPI v18ea(0x193b), v18e9

    Begin block 0x18ef
    prev=[0x18e7], succ=[]
    =================================
    0x18ef: v18ef(0x40) = CONST 
    0x18f2: v18f2 = MLOAD v18ef(0x40)
    0x18f3: v18f3(0x461bcd) = CONST 
    0x18f7: v18f7(0xe5) = CONST 
    0x18f9: v18f9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v18f7(0xe5), v18f3(0x461bcd)
    0x18fb: MSTORE v18f2, v18f9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x18fc: v18fc(0x20) = CONST 
    0x18fe: v18fe(0x4) = CONST 
    0x1901: v1901 = ADD v18f2, v18fe(0x4)
    0x1902: MSTORE v1901, v18fc(0x20)
    0x1903: v1903(0x17) = CONST 
    0x1905: v1905(0x24) = CONST 
    0x1908: v1908 = ADD v18f2, v1905(0x24)
    0x1909: MSTORE v1908, v1903(0x17)
    0x190a: v190a(0x416c726561647920636c61696d656420666f72206e6f77000000000000000000) = CONST 
    0x192b: v192b(0x44) = CONST 
    0x192e: v192e = ADD v18f2, v192b(0x44)
    0x192f: MSTORE v192e, v190a(0x416c726561647920636c61696d656420666f72206e6f77000000000000000000)
    0x1931: v1931 = MLOAD v18ef(0x40)
    0x1935: v1935(0x0) = SUB v18f2, v1931
    0x1936: v1936(0x64) = CONST 
    0x1938: v1938(0x64) = ADD v1936(0x64), v1935(0x0)
    0x193a: REVERT v1931, v1938(0x64)

    Begin block 0x193b
    prev=[0x18e7], succ=[0x1960, 0x1964]
    =================================
    0x193c: v193c(0x1) = CONST 
    0x193e: v193e(0x1) = CONST 
    0x1940: v1940(0xa0) = CONST 
    0x1942: v1942(0x10000000000000000000000000000000000000000) = SHL v1940(0xa0), v193e(0x1)
    0x1943: v1943(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1942(0x10000000000000000000000000000000000000000), v193c(0x1)
    0x1945: v1945 = AND v610, v1943(0xffffffffffffffffffffffffffffffffffffffff)
    0x1946: v1946(0x0) = CONST 
    0x194a: MSTORE v1946(0x0), v1945
    0x194b: v194b(0x3) = CONST 
    0x194d: v194d(0x20) = CONST 
    0x194f: MSTORE v194d(0x20), v194b(0x3)
    0x1950: v1950(0x40) = CONST 
    0x1953: v1953 = SHA3 v1946(0x0), v1950(0x40)
    0x1954: v1954(0x1) = CONST 
    0x1956: v1956 = ADD v1954(0x1), v1953
    0x1957: v1957 = SLOAD v1956
    0x1958: v1958(0x64) = CONST 
    0x195a: v195a = LT v1958(0x64), v1957
    0x195b: v195b(0x1964) = CONST 
    0x195f: JUMPI v195b(0x1964), v195a

    Begin block 0x1960
    prev=[0x193b], succ=[]
    =================================
    0x1960: v1960(0x0) = CONST 
    0x1963: REVERT v1960(0x0), v1960(0x0)

    Begin block 0x1964
    prev=[0x193b], succ=[0x19a0, 0x19a4]
    =================================
    0x1965: v1965(0x0) = CONST 
    0x1967: v1967(0x1a34) = CONST 
    0x196c: v196c(0x1) = CONST 
    0x196e: v196e(0x1) = CONST 
    0x1970: v1970(0xa0) = CONST 
    0x1972: v1972(0x10000000000000000000000000000000000000000) = SHL v1970(0xa0), v196e(0x1)
    0x1973: v1973(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1972(0x10000000000000000000000000000000000000000), v196c(0x1)
    0x1974: v1974 = AND v1973(0xffffffffffffffffffffffffffffffffffffffff), v616
    0x1975: v1975(0x18160ddd) = CONST 
    0x197a: v197a(0x40) = CONST 
    0x197c: v197c = MLOAD v197a(0x40)
    0x197e: v197e(0xffffffff) = CONST 
    0x1983: v1983(0x18160ddd) = AND v197e(0xffffffff), v1975(0x18160ddd)
    0x1984: v1984(0xe0) = CONST 
    0x1986: v1986(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL v1984(0xe0), v1983(0x18160ddd)
    0x1988: MSTORE v197c, v1986(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x1989: v1989(0x4) = CONST 
    0x198b: v198b = ADD v1989(0x4), v197c
    0x198c: v198c(0x20) = CONST 
    0x198e: v198e(0x40) = CONST 
    0x1990: v1990 = MLOAD v198e(0x40)
    0x1993: v1993(0x4) = SUB v198b, v1990
    0x1997: v1997 = EXTCODESIZE v1974
    0x1998: v1998 = ISZERO v1997
    0x199a: v199a = ISZERO v1998
    0x199b: v199b(0x19a4) = CONST 
    0x199f: JUMPI v199b(0x19a4), v199a

    Begin block 0x19a0
    prev=[0x1964], succ=[]
    =================================
    0x19a0: v19a0(0x0) = CONST 
    0x19a3: REVERT v19a0(0x0), v19a0(0x0)

    Begin block 0x19a4
    prev=[0x1964], succ=[0x19b0, 0x19b9]
    =================================
    0x19a6: v19a6 = GAS 
    0x19a7: v19a7 = STATICCALL v19a6, v1974, v1990, v1993(0x4), v1990, v198c(0x20)
    0x19a8: v19a8 = ISZERO v19a7
    0x19aa: v19aa = ISZERO v19a8
    0x19ab: v19ab(0x19b9) = CONST 
    0x19af: JUMPI v19ab(0x19b9), v19aa

    Begin block 0x19b0
    prev=[0x19a4], succ=[]
    =================================
    0x19b0: v19b0 = RETURNDATASIZE 
    0x19b1: v19b1(0x0) = CONST 
    0x19b4: RETURNDATACOPY v19b1(0x0), v19b1(0x0), v19b0
    0x19b5: v19b5 = RETURNDATASIZE 
    0x19b6: v19b6(0x0) = CONST 
    0x19b8: REVERT v19b6(0x0), v19b5

    Begin block 0x19b9
    prev=[0x19a4], succ=[0x19cc, 0x19d0]
    =================================
    0x19be: v19be(0x40) = CONST 
    0x19c0: v19c0 = MLOAD v19be(0x40)
    0x19c1: v19c1 = RETURNDATASIZE 
    0x19c2: v19c2(0x20) = CONST 
    0x19c5: v19c5 = LT v19c1, v19c2(0x20)
    0x19c6: v19c6 = ISZERO v19c5
    0x19c7: v19c7(0x19d0) = CONST 
    0x19cb: JUMPI v19c7(0x19d0), v19c6

    Begin block 0x19cc
    prev=[0x19b9], succ=[]
    =================================
    0x19cc: v19cc(0x0) = CONST 
    0x19cf: REVERT v19cc(0x0), v19cc(0x0)

    Begin block 0x19d0
    prev=[0x19b9], succ=[0x1a30, 0x17300x5dd]
    =================================
    0x19d2: v19d2 = MLOAD v19c0
    0x19d3: v19d3(0x1) = CONST 
    0x19d5: v19d5(0x1) = CONST 
    0x19d7: v19d7(0xa0) = CONST 
    0x19d9: v19d9(0x10000000000000000000000000000000000000000) = SHL v19d7(0xa0), v19d5(0x1)
    0x19da: v19da(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19d9(0x10000000000000000000000000000000000000000), v19d3(0x1)
    0x19dd: v19dd = AND v610, v19da(0xffffffffffffffffffffffffffffffffffffffff)
    0x19de: v19de(0x0) = CONST 
    0x19e2: MSTORE v19de(0x0), v19dd
    0x19e3: v19e3(0x3) = CONST 
    0x19e5: v19e5(0x20) = CONST 
    0x19e9: MSTORE v19e5(0x20), v19e3(0x3)
    0x19ea: v19ea(0x40) = CONST 
    0x19ef: v19ef = SHA3 v19de(0x0), v19ea(0x40)
    0x19f0: v19f0(0x1) = CONST 
    0x19f2: v19f2 = ADD v19f0(0x1), v19ef
    0x19f3: v19f3 = SLOAD v19f2
    0x19f5: v19f5 = MLOAD v19ea(0x40)
    0x19f6: v19f6(0x70a08231) = CONST 
    0x19fb: v19fb(0xe0) = CONST 
    0x19fd: v19fd(0x70a0823100000000000000000000000000000000000000000000000000000000) = SHL v19fb(0xe0), v19f6(0x70a08231)
    0x19ff: MSTORE v19f5, v19fd(0x70a0823100000000000000000000000000000000000000000000000000000000)
    0x1a00: v1a00 = CALLER 
    0x1a01: v1a01(0x4) = CONST 
    0x1a04: v1a04 = ADD v19f5, v1a01(0x4)
    0x1a05: MSTORE v1a04, v1a00
    0x1a07: v1a07 = MLOAD v19ea(0x40)
    0x1a08: v1a08(0x3f3c) = CONST 
    0x1a11: v1a11 = AND v616, v19da(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a13: v1a13(0x70a08231) = CONST 
    0x1a19: v1a19(0x24) = CONST 
    0x1a1d: v1a1d = ADD v19f5, v1a19(0x24)
    0x1a22: v1a22(0x0) = SUB v19f5, v1a07
    0x1a23: v1a23(0x24) = ADD v1a22(0x0), v1a19(0x24)
    0x1a27: v1a27 = EXTCODESIZE v1a11
    0x1a28: v1a28 = ISZERO v1a27
    0x1a2a: v1a2a = ISZERO v1a28
    0x1a2b: v1a2b(0x1730) = CONST 
    0x1a2f: JUMPI v1a2b(0x1730), v1a2a

    Begin block 0x1a30
    prev=[0x19d0], succ=[]
    =================================
    0x1a30: v1a30(0x0) = CONST 
    0x1a33: REVERT v1a30(0x0), v1a30(0x0)

    Begin block 0x17300x5dd
    prev=[0x19d0], succ=[0x173c0x5dd, 0x17450x5dd]
    =================================
    0x17320x5dd: v5dd1732 = GAS 
    0x17330x5dd: v5dd1733 = STATICCALL v5dd1732, v1a11, v1a07, v1a23(0x24), v1a07, v19e5(0x20)
    0x17340x5dd: v5dd1734 = ISZERO v5dd1733
    0x17360x5dd: v5dd1736 = ISZERO v5dd1734
    0x17370x5dd: v5dd1737(0x1745) = CONST 
    0x173b0x5dd: JUMPI v5dd1737(0x1745), v5dd1736

    Begin block 0x173c0x5dd
    prev=[0x17300x5dd], succ=[]
    =================================
    0x173c0x5dd: v5dd173c = RETURNDATASIZE 
    0x173d0x5dd: v5dd173d(0x0) = CONST 
    0x17400x5dd: RETURNDATACOPY v5dd173d(0x0), v5dd173d(0x0), v5dd173c
    0x17410x5dd: v5dd1741 = RETURNDATASIZE 
    0x17420x5dd: v5dd1742(0x0) = CONST 
    0x17440x5dd: REVERT v5dd1742(0x0), v5dd1741

    Begin block 0x17450x5dd
    prev=[0x17300x5dd], succ=[0x17580x5dd, 0x175c0x5dd]
    =================================
    0x174a0x5dd: v5dd174a(0x40) = CONST 
    0x174c0x5dd: v5dd174c = MLOAD v5dd174a(0x40)
    0x174d0x5dd: v5dd174d = RETURNDATASIZE 
    0x174e0x5dd: v5dd174e(0x20) = CONST 
    0x17510x5dd: v5dd1751 = LT v5dd174d, v5dd174e(0x20)
    0x17520x5dd: v5dd1752 = ISZERO v5dd1751
    0x17530x5dd: v5dd1753(0x175c) = CONST 
    0x17570x5dd: JUMPI v5dd1753(0x175c), v5dd1752

    Begin block 0x17580x5dd
    prev=[0x17450x5dd], succ=[]
    =================================
    0x17580x5dd: v5dd1758(0x0) = CONST 
    0x175b0x5dd: REVERT v5dd1758(0x0), v5dd1758(0x0)

    Begin block 0x175c0x5dd
    prev=[0x17450x5dd], succ=[0x1e230x5dd]
    =================================
    0x175e0x5dd: v5dd175e = MLOAD v5dd174c
    0x17600x5dd: v5dd1760(0x1e23) = CONST 
    0x17640x5dd: JUMP v5dd1760(0x1e23)

    Begin block 0x1e230x5dd
    prev=[0x175c0x5dd], succ=[0x1e340x5dd, 0x1e2c0x5dd]
    =================================
    0x1e240x5dd: v5dd1e24(0x0) = CONST 
    0x1e270x5dd: v5dd1e27(0x1e34) = CONST 
    0x1e2b0x5dd: JUMPI v5dd1e27(0x1e34), v5dd175e

    Begin block 0x1e340x5dd
    prev=[0x1e230x5dd], succ=[0x1e410x5dd, 0x1e420x5dd]
    =================================
    0x1e370x5dd: v5dd1e37 = MUL v19f3, v5dd175e
    0x1e3c0x5dd: v5dd1e3c(0x1e42) = CONST 
    0x1e400x5dd: JUMPI v5dd1e3c(0x1e42), v5dd175e

    Begin block 0x1e410x5dd
    prev=[0x1e340x5dd], succ=[]
    =================================
    0x1e410x5dd: THROW 

    Begin block 0x1e420x5dd
    prev=[0x1e340x5dd], succ=[0x1e4a0x5dd, 0x40110x5dd]
    =================================
    0x1e430x5dd: v5dd1e43 = DIV v5dd1e37, v5dd175e
    0x1e440x5dd: v5dd1e44 = EQ v5dd1e43, v19f3
    0x1e450x5dd: v5dd1e45(0x4011) = CONST 
    0x1e490x5dd: JUMPI v5dd1e45(0x4011), v5dd1e44

    Begin block 0x1e4a0x5dd
    prev=[0x1e420x5dd], succ=[]
    =================================
    0x1e4a0x5dd: v5dd1e4a(0x40) = CONST 
    0x1e4c0x5dd: v5dd1e4c = MLOAD v5dd1e4a(0x40)
    0x1e4d0x5dd: v5dd1e4d(0x461bcd) = CONST 
    0x1e510x5dd: v5dd1e51(0xe5) = CONST 
    0x1e530x5dd: v5dd1e53(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5dd1e51(0xe5), v5dd1e4d(0x461bcd)
    0x1e550x5dd: MSTORE v5dd1e4c, v5dd1e53(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e560x5dd: v5dd1e56(0x4) = CONST 
    0x1e580x5dd: v5dd1e58 = ADD v5dd1e56(0x4), v5dd1e4c
    0x1e5b0x5dd: v5dd1e5b(0x20) = CONST 
    0x1e5d0x5dd: v5dd1e5d = ADD v5dd1e5b(0x20), v5dd1e58
    0x1e600x5dd: v5dd1e60(0x20) = SUB v5dd1e5d, v5dd1e58
    0x1e620x5dd: MSTORE v5dd1e58, v5dd1e60(0x20)
    0x1e630x5dd: v5dd1e63(0x21) = CONST 
    0x1e660x5dd: MSTORE v5dd1e5d, v5dd1e63(0x21)
    0x1e670x5dd: v5dd1e67(0x20) = CONST 
    0x1e690x5dd: v5dd1e69 = ADD v5dd1e67(0x20), v5dd1e5d
    0x1e6b0x5dd: v5dd1e6b(0x378a) = CONST 
    0x1e6f0x5dd: v5dd1e6f(0x21) = CONST 
    0x1e720x5dd: CODECOPY v5dd1e69, v5dd1e6b(0x378a), v5dd1e6f(0x21)
    0x1e730x5dd: v5dd1e73(0x40) = CONST 
    0x1e750x5dd: v5dd1e75 = ADD v5dd1e73(0x40), v5dd1e69
    0x1e790x5dd: v5dd1e79(0x40) = CONST 
    0x1e7b0x5dd: v5dd1e7b = MLOAD v5dd1e79(0x40)
    0x1e7e0x5dd: v5dd1e7e(0x84) = SUB v5dd1e75, v5dd1e7b
    0x1e800x5dd: REVERT v5dd1e7b, v5dd1e7e(0x84)

    Begin block 0x40110x5dd
    prev=[0x1e420x5dd], succ=[0x3f3c]
    =================================
    0x40170x5dd: JUMP v1a08(0x3f3c)

    Begin block 0x3f3c
    prev=[0xf450x5dd, 0x40110x5dd], succ=[0x1e810x5dd]
    =================================
    0x3f3e: v3f3e(0x1e81) = CONST 
    0x3f42: JUMP v3f3e(0x1e81)

    Begin block 0x1e810x5dd
    prev=[0x3f3c], succ=[0x21200x5dd]
    =================================
    0x1e820x5dd: v5dd1e82(0x0) = CONST 
    0x1e840x5dd: v5dd1e84(0x4037) = CONST 
    0x1e8a0x5dd: v5dd1e8a(0x40) = CONST 
    0x1e8c0x5dd: v5dd1e8c = MLOAD v5dd1e8a(0x40)
    0x1e8e0x5dd: v5dd1e8e(0x40) = CONST 
    0x1e900x5dd: v5dd1e90 = ADD v5dd1e8e(0x40), v5dd1e8c
    0x1e910x5dd: v5dd1e91(0x40) = CONST 
    0x1e930x5dd: MSTORE v5dd1e91(0x40), v5dd1e90
    0x1e950x5dd: v5dd1e95(0x1a) = CONST 
    0x1e980x5dd: MSTORE v5dd1e8c, v5dd1e95(0x1a)
    0x1e990x5dd: v5dd1e99(0x20) = CONST 
    0x1e9b0x5dd: v5dd1e9b = ADD v5dd1e99(0x20), v5dd1e8c
    0x1e9c0x5dd: v5dd1e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x1ebe0x5dd: MSTORE v5dd1e9b, v5dd1e9c(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x1ec00x5dd: v5dd1ec0(0x2120) = CONST 
    0x1ec40x5dd: JUMP v5dd1ec0(0x2120)

    Begin block 0x21200x5dd
    prev=[0x1e810x5dd], succ=[0x212a0x5dd, 0x21b00x5dd]
    =================================
    0x21210x5dd: v5dd2121(0x0) = CONST 
    0x21250x5dd: v5dd2125(0x21b0) = CONST 
    0x21290x5dd: JUMPI v5dd2125(0x21b0), v19d2

    Begin block 0x212a0x5dd
    prev=[0x21200x5dd], succ=[0x215a0x5dd]
    =================================
    0x212a0x5dd: v5dd212a(0x40) = CONST 
    0x212c0x5dd: v5dd212c = MLOAD v5dd212a(0x40)
    0x212d0x5dd: v5dd212d(0x461bcd) = CONST 
    0x21310x5dd: v5dd2131(0xe5) = CONST 
    0x21330x5dd: v5dd2133(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v5dd2131(0xe5), v5dd212d(0x461bcd)
    0x21350x5dd: MSTORE v5dd212c, v5dd2133(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21360x5dd: v5dd2136(0x4) = CONST 
    0x21380x5dd: v5dd2138 = ADD v5dd2136(0x4), v5dd212c
    0x213b0x5dd: v5dd213b(0x20) = CONST 
    0x213d0x5dd: v5dd213d = ADD v5dd213b(0x20), v5dd2138
    0x21400x5dd: v5dd2140(0x20) = SUB v5dd213d, v5dd2138
    0x21420x5dd: MSTORE v5dd2138, v5dd2140(0x20)
    0x21460x5dd: v5dd2146(0x1a) = MLOAD v5dd1e8c
    0x21480x5dd: MSTORE v5dd213d, v5dd2146(0x1a)
    0x21490x5dd: v5dd2149(0x20) = CONST 
    0x214b0x5dd: v5dd214b = ADD v5dd2149(0x20), v5dd213d
    0x214f0x5dd: v5dd214f(0x1a) = MLOAD v5dd1e8c
    0x21510x5dd: v5dd2151(0x20) = CONST 
    0x21530x5dd: v5dd2153 = ADD v5dd2151(0x20), v5dd1e8c
    0x21580x5dd: v5dd2158(0x0) = CONST 

    Begin block 0x215a0x5dd
    prev=[0x212a0x5dd, 0x21640x5dd], succ=[0x21740x5dd, 0x21640x5dd]
    =================================
    0x215a0x5dd_0x0: v215a5dd_0 = PHI v5dd216e, v5dd2158(0x0)
    0x215d0x5dd: v5dd215d = LT v215a5dd_0, v5dd214f(0x1a)
    0x215e0x5dd: v5dd215e = ISZERO v5dd215d
    0x215f0x5dd: v5dd215f(0x2174) = CONST 
    0x21630x5dd: JUMPI v5dd215f(0x2174), v5dd215e

    Begin block 0x21740x5dd
    prev=[0x215a0x5dd], succ=[0x21a20x5dd, 0x21890x5dd]
    =================================
    0x217d0x5dd: v5dd217d = ADD v5dd214f(0x1a), v5dd214b
    0x217f0x5dd: v5dd217f(0x1f) = CONST 
    0x21810x5dd: v5dd2181(0x1a) = AND v5dd217f(0x1f), v5dd214f(0x1a)
    0x21830x5dd: v5dd2183 = ISZERO v5dd2181(0x1a)
    0x21840x5dd: v5dd2184(0x21a2) = CONST 
    0x21880x5dd: JUMPI v5dd2184(0x21a2), v5dd2183

    Begin block 0x21a20x5dd
    prev=[0x21740x5dd, 0x21890x5dd], succ=[]
    =================================
    0x21a20x5dd_0x1: v21a25dd_1 = PHI v5dd219f, v5dd217d
    0x21a80x5dd: v5dd21a8(0x40) = CONST 
    0x21aa0x5dd: v5dd21aa = MLOAD v5dd21a8(0x40)
    0x21ad0x5dd: v5dd21ad = SUB v21a25dd_1, v5dd21aa
    0x21af0x5dd: REVERT v5dd21aa, v5dd21ad

    Begin block 0x21890x5dd
    prev=[0x21740x5dd], succ=[0x21a20x5dd]
    =================================
    0x218b0x5dd: v5dd218b = SUB v5dd217d, v5dd2181(0x1a)
    0x218d0x5dd: v5dd218d = MLOAD v5dd218b
    0x218e0x5dd: v5dd218e(0x1) = CONST 
    0x21910x5dd: v5dd2191(0x20) = CONST 
    0x21930x5dd: v5dd2193(0x6) = SUB v5dd2191(0x20), v5dd2181(0x1a)
    0x21940x5dd: v5dd2194(0x100) = CONST 
    0x21970x5dd: v5dd2197(0x1000000000000) = EXP v5dd2194(0x100), v5dd2193(0x6)
    0x21980x5dd: v5dd2198(0xffffffffffff) = SUB v5dd2197(0x1000000000000), v5dd218e(0x1)
    0x21990x5dd: v5dd2199 = NOT v5dd2198(0xffffffffffff)
    0x219a0x5dd: v5dd219a = AND v5dd2199, v5dd218d
    0x219c0x5dd: MSTORE v5dd218b, v5dd219a
    0x219d0x5dd: v5dd219d(0x20) = CONST 
    0x219f0x5dd: v5dd219f = ADD v5dd219d(0x20), v5dd218b

    Begin block 0x21640x5dd
    prev=[0x215a0x5dd], succ=[0x215a0x5dd]
    =================================
    0x21640x5dd_0x0: v21645dd_0 = PHI v5dd216e, v5dd2158(0x0)
    0x21660x5dd: v5dd2166 = ADD v21645dd_0, v5dd2153
    0x21670x5dd: v5dd2167 = MLOAD v5dd2166
    0x216a0x5dd: v5dd216a = ADD v21645dd_0, v5dd214b
    0x216b0x5dd: MSTORE v5dd216a, v5dd2167
    0x216c0x5dd: v5dd216c(0x20) = CONST 
    0x216e0x5dd: v5dd216e = ADD v5dd216c(0x20), v21645dd_0
    0x216f0x5dd: v5dd216f(0x215a) = CONST 
    0x21730x5dd: JUMP v5dd216f(0x215a)

    Begin block 0x21b00x5dd
    prev=[0x21200x5dd], succ=[0x21bc0x5dd, 0x21bd0x5dd]
    =================================
    0x21b20x5dd: v5dd21b2(0x0) = CONST 
    0x21b70x5dd: v5dd21b7(0x21bd) = CONST 
    0x21bb0x5dd: JUMPI v5dd21b7(0x21bd), v19d2

    Begin block 0x21bc0x5dd
    prev=[0x21b00x5dd], succ=[]
    =================================
    0x21bc0x5dd: THROW 

    Begin block 0x21bd0x5dd
    prev=[0x21b00x5dd], succ=[0x40370x5dd]
    =================================
    0x21bd0x5dd_0x0: v21bd5dd_0 = PHI v5dd1e37, v5dd1e2d(0x0)
    0x21be0x5dd: v5dd21be = DIV v21bd5dd_0, v19d2
    0x21c60x5dd: JUMP v5dd1e84(0x4037)

    Begin block 0x40370x5dd
    prev=[0x21bd0x5dd], succ=[0x1a34]
    =================================
    0x403d0x5dd: JUMP v1967(0x1a34)

    Begin block 0x1a34
    prev=[0x40370x5dd], succ=[0x1a5f]
    =================================
    0x1a35: v1a35(0x1) = CONST 
    0x1a37: v1a37(0x1) = CONST 
    0x1a39: v1a39(0xa0) = CONST 
    0x1a3b: v1a3b(0x10000000000000000000000000000000000000000) = SHL v1a39(0xa0), v1a37(0x1)
    0x1a3c: v1a3c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a3b(0x10000000000000000000000000000000000000000), v1a35(0x1)
    0x1a3e: v1a3e = AND v610, v1a3c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a3f: v1a3f(0x0) = CONST 
    0x1a43: MSTORE v1a3f(0x0), v1a3e
    0x1a44: v1a44(0x3) = CONST 
    0x1a46: v1a46(0x20) = CONST 
    0x1a48: MSTORE v1a46(0x20), v1a44(0x3)
    0x1a49: v1a49(0x40) = CONST 
    0x1a4c: v1a4c = SHA3 v1a3f(0x0), v1a49(0x40)
    0x1a4d: v1a4d(0x1) = CONST 
    0x1a4f: v1a4f = ADD v1a4d(0x1), v1a4c
    0x1a50: v1a50 = SLOAD v1a4f
    0x1a54: v1a54(0x1a5f) = CONST 
    0x1a5a: v1a5a(0x1ec5) = CONST 
    0x1a5e: v1a5e_0 = CALLPRIVATE v1a5a(0x1ec5), v5dd21be, v1a50, v1a54(0x1a5f)

    Begin block 0x1a5f
    prev=[0x1a34], succ=[0x1ac0, 0x1ac4]
    =================================
    0x1a60: v1a60(0x1) = CONST 
    0x1a62: v1a62(0x1) = CONST 
    0x1a64: v1a64(0xa0) = CONST 
    0x1a66: v1a66(0x10000000000000000000000000000000000000000) = SHL v1a64(0xa0), v1a62(0x1)
    0x1a67: v1a67(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a66(0x10000000000000000000000000000000000000000), v1a60(0x1)
    0x1a6a: v1a6a = AND v610, v1a67(0xffffffffffffffffffffffffffffffffffffffff)
    0x1a6b: v1a6b(0x0) = CONST 
    0x1a6f: MSTORE v1a6b(0x0), v1a6a
    0x1a70: v1a70(0x3) = CONST 
    0x1a72: v1a72(0x20) = CONST 
    0x1a74: MSTORE v1a72(0x20), v1a70(0x3)
    0x1a75: v1a75(0x40) = CONST 
    0x1a79: v1a79 = SHA3 v1a6b(0x0), v1a75(0x40)
    0x1a7a: v1a7a(0x1) = CONST 
    0x1a7c: v1a7c = ADD v1a7a(0x1), v1a79
    0x1a80: SSTORE v1a7c, v1a5e_0
    0x1a81: v1a81(0x6) = CONST 
    0x1a83: v1a83 = SLOAD v1a81(0x6)
    0x1a85: v1a85 = MLOAD v1a75(0x40)
    0x1a86: v1a86(0x7dc5bcc9) = CONST 
    0x1a8b: v1a8b(0xe1) = CONST 
    0x1a8d: v1a8d(0xfb8b799200000000000000000000000000000000000000000000000000000000) = SHL v1a8b(0xe1), v1a86(0x7dc5bcc9)
    0x1a8f: MSTORE v1a85, v1a8d(0xfb8b799200000000000000000000000000000000000000000000000000000000)
    0x1a90: v1a90(0x4) = CONST 
    0x1a93: v1a93 = ADD v1a85, v1a90(0x4)
    0x1a96: MSTORE v1a93, v5dd21be
    0x1a97: v1a97 = CALLER 
    0x1a98: v1a98(0x24) = CONST 
    0x1a9b: v1a9b = ADD v1a85, v1a98(0x24)
    0x1a9c: MSTORE v1a9b, v1a97
    0x1a9e: v1a9e = MLOAD v1a75(0x40)
    0x1aa0: v1aa0 = AND v1a67(0xffffffffffffffffffffffffffffffffffffffff), v1a83
    0x1aa2: v1aa2(0xfb8b7992) = CONST 
    0x1aa8: v1aa8(0x44) = CONST 
    0x1aac: v1aac = ADD v1a85, v1aa8(0x44)
    0x1ab1: v1ab1(0x0) = SUB v1a85, v1a9e
    0x1ab2: v1ab2(0x44) = ADD v1ab1(0x0), v1aa8(0x44)
    0x1ab7: v1ab7 = EXTCODESIZE v1aa0
    0x1ab8: v1ab8 = ISZERO v1ab7
    0x1aba: v1aba = ISZERO v1ab8
    0x1abb: v1abb(0x1ac4) = CONST 
    0x1abf: JUMPI v1abb(0x1ac4), v1aba

    Begin block 0x1ac0
    prev=[0x1a5f], succ=[]
    =================================
    0x1ac0: v1ac0(0x0) = CONST 
    0x1ac3: REVERT v1ac0(0x0), v1ac0(0x0)

    Begin block 0x1ac4
    prev=[0x1a5f], succ=[0x1ad0, 0x1ad9]
    =================================
    0x1ac6: v1ac6 = GAS 
    0x1ac7: v1ac7 = CALL v1ac6, v1aa0, v1a6b(0x0), v1a9e, v1ab2(0x44), v1a9e, v1a6b(0x0)
    0x1ac8: v1ac8 = ISZERO v1ac7
    0x1aca: v1aca = ISZERO v1ac8
    0x1acb: v1acb(0x1ad9) = CONST 
    0x1acf: JUMPI v1acb(0x1ad9), v1aca

    Begin block 0x1ad0
    prev=[0x1ac4], succ=[]
    =================================
    0x1ad0: v1ad0 = RETURNDATASIZE 
    0x1ad1: v1ad1(0x0) = CONST 
    0x1ad4: RETURNDATACOPY v1ad1(0x0), v1ad1(0x0), v1ad0
    0x1ad5: v1ad5 = RETURNDATASIZE 
    0x1ad6: v1ad6(0x0) = CONST 
    0x1ad8: REVERT v1ad6(0x0), v1ad5

    Begin block 0x1ad9
    prev=[0x1ac4], succ=[0x1b5a, 0x1b5e]
    =================================
    0x1adc: v1adc(0x6) = CONST 
    0x1ade: v1ade = SLOAD v1adc(0x6)
    0x1adf: v1adf(0x40) = CONST 
    0x1ae2: v1ae2 = MLOAD v1adf(0x40)
    0x1ae3: v1ae3(0x75b04b15) = CONST 
    0x1ae8: v1ae8(0xe1) = CONST 
    0x1aea: v1aea(0xeb60962a00000000000000000000000000000000000000000000000000000000) = SHL v1ae8(0xe1), v1ae3(0x75b04b15)
    0x1aec: MSTORE v1ae2, v1aea(0xeb60962a00000000000000000000000000000000000000000000000000000000)
    0x1aed: v1aed(0x1) = CONST 
    0x1aef: v1aef(0x1) = CONST 
    0x1af1: v1af1(0xa0) = CONST 
    0x1af3: v1af3(0x10000000000000000000000000000000000000000) = SHL v1af1(0xa0), v1aef(0x1)
    0x1af4: v1af4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1af3(0x10000000000000000000000000000000000000000), v1aed(0x1)
    0x1af7: v1af7 = AND v1af4(0xffffffffffffffffffffffffffffffffffffffff), v610
    0x1af8: v1af8(0x4) = CONST 
    0x1afb: v1afb = ADD v1ae2, v1af8(0x4)
    0x1afc: MSTORE v1afb, v1af7
    0x1afd: v1afd = CALLER 
    0x1afe: v1afe(0x44) = CONST 
    0x1b01: v1b01 = ADD v1ae2, v1afe(0x44)
    0x1b02: MSTORE v1b01, v1afd
    0x1b03: v1b03(0x60) = CONST 
    0x1b05: v1b05(0x24) = CONST 
    0x1b08: v1b08 = ADD v1ae2, v1b05(0x24)
    0x1b09: MSTORE v1b08, v1b03(0x60)
    0x1b0a: v1b0a(0x15) = CONST 
    0x1b0c: v1b0c(0x64) = CONST 
    0x1b0f: v1b0f = ADD v1ae2, v1b0c(0x64)
    0x1b10: MSTORE v1b0f, v1b0a(0x15)
    0x1b11: v1b11(0x115512081c1c9bd99a5d081dda5d1a191c985dd85b) = CONST 
    0x1b27: v1b27(0x5a) = CONST 
    0x1b29: v1b29(0x4554482070726f666974207769746864726177616c0000000000000000000000) = SHL v1b27(0x5a), v1b11(0x115512081c1c9bd99a5d081dda5d1a191c985dd85b)
    0x1b2a: v1b2a(0x84) = CONST 
    0x1b2d: v1b2d = ADD v1ae2, v1b2a(0x84)
    0x1b2e: MSTORE v1b2d, v1b29(0x4554482070726f666974207769746864726177616c0000000000000000000000)
    0x1b30: v1b30 = MLOAD v1adf(0x40)
    0x1b34: v1b34 = AND v1ade, v1af4(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b37: v1b37(0xeb60962a) = CONST 
    0x1b3e: v1b3e(0xa4) = CONST 
    0x1b42: v1b42 = ADD v1ae2, v1b3e(0xa4)
    0x1b44: v1b44(0x0) = CONST 
    0x1b4b: v1b4b(0x0) = SUB v1ae2, v1b30
    0x1b4c: v1b4c(0xa4) = ADD v1b4b(0x0), v1b3e(0xa4)
    0x1b51: v1b51 = EXTCODESIZE v1b34
    0x1b52: v1b52 = ISZERO v1b51
    0x1b54: v1b54 = ISZERO v1b52
    0x1b55: v1b55(0x1b5e) = CONST 
    0x1b59: JUMPI v1b55(0x1b5e), v1b54

    Begin block 0x1b5a
    prev=[0x1ad9], succ=[]
    =================================
    0x1b5a: v1b5a(0x0) = CONST 
    0x1b5d: REVERT v1b5a(0x0), v1b5a(0x0)

    Begin block 0x1b5e
    prev=[0x1ad9], succ=[0x1b6a, 0x1b73]
    =================================
    0x1b60: v1b60 = GAS 
    0x1b61: v1b61 = CALL v1b60, v1b34, v1b44(0x0), v1b30, v1b4c(0xa4), v1b30, v1b44(0x0)
    0x1b62: v1b62 = ISZERO v1b61
    0x1b64: v1b64 = ISZERO v1b62
    0x1b65: v1b65(0x1b73) = CONST 
    0x1b69: JUMPI v1b65(0x1b73), v1b64

    Begin block 0x1b6a
    prev=[0x1b5e], succ=[]
    =================================
    0x1b6a: v1b6a = RETURNDATASIZE 
    0x1b6b: v1b6b(0x0) = CONST 
    0x1b6e: RETURNDATACOPY v1b6b(0x0), v1b6b(0x0), v1b6a
    0x1b6f: v1b6f = RETURNDATASIZE 
    0x1b70: v1b70(0x0) = CONST 
    0x1b72: REVERT v1b70(0x0), v1b6f

    Begin block 0x1b73
    prev=[0x1b5e], succ=[0x3d4a]
    =================================
    0x1b76: v1b76(0x40) = CONST 
    0x1b79: v1b79 = MLOAD v1b76(0x40)
    0x1b7a: v1b7a = CALLER 
    0x1b7c: MSTORE v1b79, v1b7a
    0x1b7d: v1b7d(0x1) = CONST 
    0x1b7f: v1b7f(0x1) = CONST 
    0x1b81: v1b81(0xa0) = CONST 
    0x1b83: v1b83(0x10000000000000000000000000000000000000000) = SHL v1b81(0xa0), v1b7f(0x1)
    0x1b84: v1b84(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b83(0x10000000000000000000000000000000000000000), v1b7d(0x1)
    0x1b87: v1b87 = AND v610, v1b84(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b88: v1b88(0x20) = CONST 
    0x1b8b: v1b8b = ADD v1b79, v1b88(0x20)
    0x1b8c: MSTORE v1b8b, v1b87
    0x1b8e: v1b8e = AND v616, v1b84(0xffffffffffffffffffffffffffffffffffffffff)
    0x1b91: v1b91 = ADD v1b76(0x40), v1b79
    0x1b92: MSTORE v1b91, v1b8e
    0x1b93: v1b93(0x60) = CONST 
    0x1b96: v1b96 = ADD v1b79, v1b93(0x60)
    0x1b99: MSTORE v1b96, v5dd21be
    0x1b9b: v1b9b = MLOAD v1b76(0x40)
    0x1b9c: v1b9c(0xa1e7118e976e6ee7f9d9199320d3260a1030b9a74f0396620ff70a4d308f18dc) = CONST 
    0x1bc2: v1bc2(0x0) = SUB v1b79, v1b9b
    0x1bc3: v1bc3(0x80) = CONST 
    0x1bc5: v1bc5(0x80) = ADD v1bc3(0x80), v1bc2(0x0)
    0x1bc8: LOG1 v1b9b, v1bc5(0x80), v1b9c(0xa1e7118e976e6ee7f9d9199320d3260a1030b9a74f0396620ff70a4d308f18dc)
    0x1bcc: JUMP v5ec(0x3d4a)

    Begin block 0x3d4a
    prev=[0x1b73], succ=[]
    =================================
    0x3d4b: STOP 

    Begin block 0x1e2c0x5dd
    prev=[0x1e230x5dd], succ=[0xf450x5dd]
    =================================
    0x1e2d0x5dd: v5dd1e2d(0x0) = CONST 
    0x1e2f0x5dd: v5dd1e2f(0xf45) = CONST 
    0x1e330x5dd: JUMP v5dd1e2f(0xf45)

    Begin block 0xf450x5dd
    prev=[0x1e2c0x5dd], succ=[0x3f3c]
    =================================
    0xf4a0x5dd: JUMP v1a08(0x3f3c)

}

function isPoolToken(address)() public {
    Begin block 0x61c
    prev=[], succ=[0x625, 0x629]
    =================================
    0x61d: v61d = CALLVALUE 
    0x61f: v61f = ISZERO v61d
    0x620: v620(0x629) = CONST 
    0x624: JUMPI v620(0x629), v61f

    Begin block 0x625
    prev=[0x61c], succ=[]
    =================================
    0x625: v625(0x0) = CONST 
    0x628: REVERT v625(0x0), v625(0x0)

    Begin block 0x629
    prev=[0x61c], succ=[0x63e, 0x642]
    =================================
    0x62b: v62b(0x3d6b) = CONST 
    0x62f: v62f(0x4) = CONST 
    0x632: v632 = CALLDATASIZE 
    0x633: v633 = SUB v632, v62f(0x4)
    0x634: v634(0x20) = CONST 
    0x637: v637 = LT v633, v634(0x20)
    0x638: v638 = ISZERO v637
    0x639: v639(0x642) = CONST 
    0x63d: JUMPI v639(0x642), v638

    Begin block 0x63e
    prev=[0x629], succ=[]
    =================================
    0x63e: v63e(0x0) = CONST 
    0x641: REVERT v63e(0x0), v63e(0x0)

    Begin block 0x642
    prev=[0x629], succ=[0x1bcd]
    =================================
    0x644: v644 = CALLDATALOAD v62f(0x4)
    0x645: v645(0x1) = CONST 
    0x647: v647(0x1) = CONST 
    0x649: v649(0xa0) = CONST 
    0x64b: v64b(0x10000000000000000000000000000000000000000) = SHL v649(0xa0), v647(0x1)
    0x64c: v64c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v64b(0x10000000000000000000000000000000000000000), v645(0x1)
    0x64d: v64d = AND v64c(0xffffffffffffffffffffffffffffffffffffffff), v644
    0x64e: v64e(0x1bcd) = CONST 
    0x652: JUMP v64e(0x1bcd)

    Begin block 0x1bcd
    prev=[0x642], succ=[0x3d6b]
    =================================
    0x1bce: v1bce(0x4) = CONST 
    0x1bd0: v1bd0(0x20) = CONST 
    0x1bd2: MSTORE v1bd0(0x20), v1bce(0x4)
    0x1bd3: v1bd3(0x0) = CONST 
    0x1bd7: MSTORE v1bd3(0x0), v64d
    0x1bd8: v1bd8(0x40) = CONST 
    0x1bdb: v1bdb = SHA3 v1bd3(0x0), v1bd8(0x40)
    0x1bdc: v1bdc = SLOAD v1bdb
    0x1bdd: v1bdd(0xff) = CONST 
    0x1bdf: v1bdf = AND v1bdd(0xff), v1bdc
    0x1be1: JUMP v62b(0x3d6b)

    Begin block 0x3d6b
    prev=[0x1bcd], succ=[]
    =================================
    0x3d6c: v3d6c(0x40) = CONST 
    0x3d6f: v3d6f = MLOAD v3d6c(0x40)
    0x3d71: v3d71 = ISZERO v1bdf
    0x3d72: v3d72 = ISZERO v3d71
    0x3d74: MSTORE v3d6f, v3d72
    0x3d75: v3d75 = MLOAD v3d6c(0x40)
    0x3d79: v3d79(0x0) = SUB v3d6f, v3d75
    0x3d7a: v3d7a(0x20) = CONST 
    0x3d7c: v3d7c(0x20) = ADD v3d7a(0x20), v3d79(0x0)
    0x3d7e: RETURN v3d75, v3d7c(0x20)

}

function managerStruct(address)() public {
    Begin block 0x653
    prev=[], succ=[0x65c, 0x660]
    =================================
    0x654: v654 = CALLVALUE 
    0x656: v656 = ISZERO v654
    0x657: v657(0x660) = CONST 
    0x65b: JUMPI v657(0x660), v656

    Begin block 0x65c
    prev=[0x653], succ=[]
    =================================
    0x65c: v65c(0x0) = CONST 
    0x65f: REVERT v65c(0x0), v65c(0x0)

    Begin block 0x660
    prev=[0x653], succ=[0x675, 0x679]
    =================================
    0x662: v662(0x68a) = CONST 
    0x666: v666(0x4) = CONST 
    0x669: v669 = CALLDATASIZE 
    0x66a: v66a = SUB v669, v666(0x4)
    0x66b: v66b(0x20) = CONST 
    0x66e: v66e = LT v66a, v66b(0x20)
    0x66f: v66f = ISZERO v66e
    0x670: v670(0x679) = CONST 
    0x674: JUMPI v670(0x679), v66f

    Begin block 0x675
    prev=[0x660], succ=[]
    =================================
    0x675: v675(0x0) = CONST 
    0x678: REVERT v675(0x0), v675(0x0)

    Begin block 0x679
    prev=[0x660], succ=[0x1be2]
    =================================
    0x67b: v67b = CALLDATALOAD v666(0x4)
    0x67c: v67c(0x1) = CONST 
    0x67e: v67e(0x1) = CONST 
    0x680: v680(0xa0) = CONST 
    0x682: v682(0x10000000000000000000000000000000000000000) = SHL v680(0xa0), v67e(0x1)
    0x683: v683(0xffffffffffffffffffffffffffffffffffffffff) = SUB v682(0x10000000000000000000000000000000000000000), v67c(0x1)
    0x684: v684 = AND v683(0xffffffffffffffffffffffffffffffffffffffff), v67b
    0x685: v685(0x1be2) = CONST 
    0x689: JUMP v685(0x1be2)

    Begin block 0x1be2
    prev=[0x679], succ=[0x3f62, 0x1c5c]
    =================================
    0x1be3: v1be3(0x3) = CONST 
    0x1be5: v1be5(0x20) = CONST 
    0x1be9: MSTORE v1be5(0x20), v1be3(0x3)
    0x1bea: v1bea(0x0) = CONST 
    0x1bee: MSTORE v1bea(0x0), v684
    0x1bef: v1bef(0x40) = CONST 
    0x1bf4: v1bf4 = SHA3 v1bea(0x0), v1bef(0x40)
    0x1bf6: v1bf6 = SLOAD v1bf4
    0x1bf7: v1bf7(0x1) = CONST 
    0x1bfb: v1bfb = ADD v1bf4, v1bf7(0x1)
    0x1bfc: v1bfc = SLOAD v1bfb
    0x1bfd: v1bfd(0x2) = CONST 
    0x1c01: v1c01 = ADD v1bf4, v1bfd(0x2)
    0x1c02: v1c02 = SLOAD v1c01
    0x1c05: v1c05 = ADD v1bf4, v1be3(0x3)
    0x1c06: v1c06 = SLOAD v1c05
    0x1c07: v1c07(0x4) = CONST 
    0x1c0a: v1c0a = ADD v1bf4, v1c07(0x4)
    0x1c0b: v1c0b = SLOAD v1c0a
    0x1c0c: v1c0c(0x6) = CONST 
    0x1c0f: v1c0f = ADD v1bf4, v1c0c(0x6)
    0x1c11: v1c11 = SLOAD v1c0f
    0x1c13: v1c13 = MLOAD v1bef(0x40)
    0x1c14: v1c14(0x100) = CONST 
    0x1c19: v1c19 = AND v1c11, v1bf7(0x1)
    0x1c1a: v1c1a = ISZERO v1c19
    0x1c1e: v1c1e = MUL v1c1a, v1c14(0x100)
    0x1c1f: v1c1f(0x0) = CONST 
    0x1c21: v1c21(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v1c1f(0x0)
    0x1c22: v1c22 = ADD v1c21(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1c1e
    0x1c23: v1c23 = AND v1c22, v1c11
    0x1c27: v1c27 = DIV v1c23, v1bfd(0x2)
    0x1c28: v1c28(0x1f) = CONST 
    0x1c2b: v1c2b = ADD v1c27, v1c28(0x1f)
    0x1c2e: v1c2e = DIV v1c2b, v1be5(0x20)
    0x1c30: v1c30 = MUL v1be5(0x20), v1c2e
    0x1c32: v1c32 = ADD v1c13, v1c30
    0x1c34: v1c34 = ADD v1be5(0x20), v1c32
    0x1c37: MSTORE v1bef(0x40), v1c34
    0x1c3a: MSTORE v1c13, v1c27
    0x1c3f: v1c3f(0xffffffff) = CONST 
    0x1c44: v1c44 = AND v1c3f(0xffffffff), v1c02
    0x1c48: v1c48(0xff) = CONST 
    0x1c4c: v1c4c = AND v1c0b, v1c48(0xff)
    0x1c52: v1c52 = ADD v1c13, v1be5(0x20)
    0x1c56: v1c56 = ISZERO v1c27
    0x1c57: v1c57(0x3f62) = CONST 
    0x1c5b: JUMPI v1c57(0x3f62), v1c56

    Begin block 0x3f62
    prev=[0x1be2], succ=[0x68a]
    =================================
    0x3f66: v3f66(0x9) = CONST 
    0x3f6a: v3f6a = ADD v1bf4, v3f66(0x9)
    0x3f6b: v3f6b = SLOAD v3f6a
    0x3f70: v3f70(0x1) = CONST 
    0x3f72: v3f72(0x1) = CONST 
    0x3f74: v3f74(0xa0) = CONST 
    0x3f76: v3f76(0x10000000000000000000000000000000000000000) = SHL v3f74(0xa0), v3f72(0x1)
    0x3f77: v3f77(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3f76(0x10000000000000000000000000000000000000000), v3f70(0x1)
    0x3f78: v3f78 = AND v3f77(0xffffffffffffffffffffffffffffffffffffffff), v3f6b
    0x3f7a: JUMP v662(0x68a)

    Begin block 0x68a
    prev=[0x3f62, 0x3f9a, 0x1ca5], succ=[0x6e4]
    =================================
    0x68a_0x0: v68a_0 = PHI v1cbb, v3f78, v3fb0
    0x68b: v68b(0x40) = CONST 
    0x68d: v68d = MLOAD v68b(0x40)
    0x691: MSTORE v68d, v1bf6
    0x692: v692(0x20) = CONST 
    0x694: v694 = ADD v692(0x20), v68d
    0x697: MSTORE v694, v1bfc
    0x698: v698(0x20) = CONST 
    0x69a: v69a = ADD v698(0x20), v694
    0x69c: v69c(0xffffffff) = CONST 
    0x6a1: v6a1 = AND v69c(0xffffffff), v1c44
    0x6a3: MSTORE v69a, v6a1
    0x6a4: v6a4(0x20) = CONST 
    0x6a6: v6a6 = ADD v6a4(0x20), v69a
    0x6a9: MSTORE v6a6, v1c06
    0x6aa: v6aa(0x20) = CONST 
    0x6ac: v6ac = ADD v6aa(0x20), v6a6
    0x6ae: v6ae = ISZERO v1c4c
    0x6af: v6af = ISZERO v6ae
    0x6b1: MSTORE v6ac, v6af
    0x6b2: v6b2(0x20) = CONST 
    0x6b4: v6b4 = ADD v6b2(0x20), v6ac
    0x6b6: v6b6(0x20) = CONST 
    0x6b8: v6b8 = ADD v6b6(0x20), v6b4
    0x6ba: v6ba(0x1) = CONST 
    0x6bc: v6bc(0x1) = CONST 
    0x6be: v6be(0xa0) = CONST 
    0x6c0: v6c0(0x10000000000000000000000000000000000000000) = SHL v6be(0xa0), v6bc(0x1)
    0x6c1: v6c1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6c0(0x10000000000000000000000000000000000000000), v6ba(0x1)
    0x6c2: v6c2 = AND v6c1(0xffffffffffffffffffffffffffffffffffffffff), v68a_0
    0x6c4: MSTORE v6b8, v6c2
    0x6c5: v6c5(0x20) = CONST 
    0x6c7: v6c7 = ADD v6c5(0x20), v6b8
    0x6ca: v6ca(0xe0) = SUB v6c7, v68d
    0x6cc: MSTORE v6b4, v6ca(0xe0)
    0x6d0: v6d0 = MLOAD v1c13
    0x6d2: MSTORE v6c7, v6d0
    0x6d3: v6d3(0x20) = CONST 
    0x6d5: v6d5 = ADD v6d3(0x20), v6c7
    0x6d9: v6d9 = MLOAD v1c13
    0x6db: v6db(0x20) = CONST 
    0x6dd: v6dd = ADD v6db(0x20), v1c13
    0x6e2: v6e2(0x0) = CONST 

    Begin block 0x6e4
    prev=[0x68a, 0x6ee], succ=[0x6fe, 0x6ee]
    =================================
    0x6e4_0x0: v6e4_0 = PHI v6e2(0x0), v6f8
    0x6e7: v6e7 = LT v6e4_0, v6d9
    0x6e8: v6e8 = ISZERO v6e7
    0x6e9: v6e9(0x6fe) = CONST 
    0x6ed: JUMPI v6e9(0x6fe), v6e8

    Begin block 0x6fe
    prev=[0x6e4], succ=[0x72c, 0x713]
    =================================
    0x707: v707 = ADD v6d9, v6d5
    0x709: v709(0x1f) = CONST 
    0x70b: v70b = AND v709(0x1f), v6d9
    0x70d: v70d = ISZERO v70b
    0x70e: v70e(0x72c) = CONST 
    0x712: JUMPI v70e(0x72c), v70d

    Begin block 0x72c
    prev=[0x6fe, 0x713], succ=[]
    =================================
    0x72c_0x1: v72c_1 = PHI v707, v729
    0x738: v738(0x40) = CONST 
    0x73a: v73a = MLOAD v738(0x40)
    0x73d: v73d = SUB v72c_1, v73a
    0x73f: RETURN v73a, v73d

    Begin block 0x713
    prev=[0x6fe], succ=[0x72c]
    =================================
    0x715: v715 = SUB v707, v70b
    0x717: v717 = MLOAD v715
    0x718: v718(0x1) = CONST 
    0x71b: v71b(0x20) = CONST 
    0x71d: v71d = SUB v71b(0x20), v70b
    0x71e: v71e(0x100) = CONST 
    0x721: v721 = EXP v71e(0x100), v71d
    0x722: v722 = SUB v721, v718(0x1)
    0x723: v723 = NOT v722
    0x724: v724 = AND v723, v717
    0x726: MSTORE v715, v724
    0x727: v727(0x20) = CONST 
    0x729: v729 = ADD v727(0x20), v715

    Begin block 0x6ee
    prev=[0x6e4], succ=[0x6e4]
    =================================
    0x6ee_0x0: v6ee_0 = PHI v6e2(0x0), v6f8
    0x6f0: v6f0 = ADD v6ee_0, v6dd
    0x6f1: v6f1 = MLOAD v6f0
    0x6f4: v6f4 = ADD v6ee_0, v6d5
    0x6f5: MSTORE v6f4, v6f1
    0x6f6: v6f6(0x20) = CONST 
    0x6f8: v6f8 = ADD v6f6(0x20), v6ee_0
    0x6f9: v6f9(0x6e4) = CONST 
    0x6fd: JUMP v6f9(0x6e4)

    Begin block 0x1c5c
    prev=[0x1be2], succ=[0x1c65, 0x1c79]
    =================================
    0x1c5d: v1c5d(0x1f) = CONST 
    0x1c5f: v1c5f = LT v1c5d(0x1f), v1c27
    0x1c60: v1c60(0x1c79) = CONST 
    0x1c64: JUMPI v1c60(0x1c79), v1c5f

    Begin block 0x1c65
    prev=[0x1c5c], succ=[0x3f9a]
    =================================
    0x1c65: v1c65(0x100) = CONST 
    0x1c6a: v1c6a = SLOAD v1c0f
    0x1c6b: v1c6b = DIV v1c6a, v1c65(0x100)
    0x1c6c: v1c6c = MUL v1c6b, v1c65(0x100)
    0x1c6e: MSTORE v1c52, v1c6c
    0x1c70: v1c70(0x20) = CONST 
    0x1c72: v1c72 = ADD v1c70(0x20), v1c52
    0x1c74: v1c74(0x3f9a) = CONST 
    0x1c78: JUMP v1c74(0x3f9a)

    Begin block 0x3f9a
    prev=[0x1c65], succ=[0x68a]
    =================================
    0x3f9e: v3f9e(0x9) = CONST 
    0x3fa2: v3fa2 = ADD v1bf4, v3f9e(0x9)
    0x3fa3: v3fa3 = SLOAD v3fa2
    0x3fa8: v3fa8(0x1) = CONST 
    0x3faa: v3faa(0x1) = CONST 
    0x3fac: v3fac(0xa0) = CONST 
    0x3fae: v3fae(0x10000000000000000000000000000000000000000) = SHL v3fac(0xa0), v3faa(0x1)
    0x3faf: v3faf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fae(0x10000000000000000000000000000000000000000), v3fa8(0x1)
    0x3fb0: v3fb0 = AND v3faf(0xffffffffffffffffffffffffffffffffffffffff), v3fa3
    0x3fb2: JUMP v662(0x68a)

    Begin block 0x1c79
    prev=[0x1c5c], succ=[0x1c87]
    =================================
    0x1c7b: v1c7b = ADD v1c52, v1c27
    0x1c7e: v1c7e(0x0) = CONST 
    0x1c80: MSTORE v1c7e(0x0), v1c0f
    0x1c81: v1c81(0x20) = CONST 
    0x1c83: v1c83(0x0) = CONST 
    0x1c85: v1c85 = SHA3 v1c83(0x0), v1c81(0x20)

    Begin block 0x1c87
    prev=[0x1c79, 0x1c87], succ=[0x1c87, 0x1c9c]
    =================================
    0x1c87_0x0: v1c87_0 = PHI v1c52, v1c93
    0x1c87_0x1: v1c87_1 = PHI v1c85, v1c8f
    0x1c89: v1c89 = SLOAD v1c87_1
    0x1c8b: MSTORE v1c87_0, v1c89
    0x1c8d: v1c8d(0x1) = CONST 
    0x1c8f: v1c8f = ADD v1c8d(0x1), v1c87_1
    0x1c91: v1c91(0x20) = CONST 
    0x1c93: v1c93 = ADD v1c91(0x20), v1c87_0
    0x1c96: v1c96 = GT v1c7b, v1c93
    0x1c97: v1c97(0x1c87) = CONST 
    0x1c9b: JUMPI v1c97(0x1c87), v1c96

    Begin block 0x1c9c
    prev=[0x1c87], succ=[0x1ca5]
    =================================
    0x1c9e: v1c9e = SUB v1c93, v1c7b
    0x1c9f: v1c9f(0x1f) = CONST 
    0x1ca1: v1ca1 = AND v1c9f(0x1f), v1c9e
    0x1ca3: v1ca3 = ADD v1c7b, v1ca1

    Begin block 0x1ca5
    prev=[0x1c9c], succ=[0x68a]
    =================================
    0x1ca9: v1ca9(0x9) = CONST 
    0x1cad: v1cad = ADD v1bf4, v1ca9(0x9)
    0x1cae: v1cae = SLOAD v1cad
    0x1cb3: v1cb3(0x1) = CONST 
    0x1cb5: v1cb5(0x1) = CONST 
    0x1cb7: v1cb7(0xa0) = CONST 
    0x1cb9: v1cb9(0x10000000000000000000000000000000000000000) = SHL v1cb7(0xa0), v1cb5(0x1)
    0x1cba: v1cba(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cb9(0x10000000000000000000000000000000000000000), v1cb3(0x1)
    0x1cbb: v1cbb = AND v1cba(0xffffffffffffffffffffffffffffffffffffffff), v1cae
    0x1cbd: JUMP v662(0x68a)

}

function adjustManagerAllowance(address,uint256,uint256)() public {
    Begin block 0x740
    prev=[], succ=[0x749, 0x74d]
    =================================
    0x741: v741 = CALLVALUE 
    0x743: v743 = ISZERO v741
    0x744: v744(0x74d) = CONST 
    0x748: JUMPI v744(0x74d), v743

    Begin block 0x749
    prev=[0x740], succ=[]
    =================================
    0x749: v749(0x0) = CONST 
    0x74c: REVERT v749(0x0), v749(0x0)

    Begin block 0x74d
    prev=[0x740], succ=[0x762, 0x766]
    =================================
    0x74f: v74f(0x3d9e) = CONST 
    0x753: v753(0x4) = CONST 
    0x756: v756 = CALLDATASIZE 
    0x757: v757 = SUB v756, v753(0x4)
    0x758: v758(0x60) = CONST 
    0x75b: v75b = LT v757, v758(0x60)
    0x75c: v75c = ISZERO v75b
    0x75d: v75d(0x766) = CONST 
    0x761: JUMPI v75d(0x766), v75c

    Begin block 0x762
    prev=[0x74d], succ=[]
    =================================
    0x762: v762(0x0) = CONST 
    0x765: REVERT v762(0x0), v762(0x0)

    Begin block 0x766
    prev=[0x74d], succ=[0x1cbe]
    =================================
    0x768: v768(0x1) = CONST 
    0x76a: v76a(0x1) = CONST 
    0x76c: v76c(0xa0) = CONST 
    0x76e: v76e(0x10000000000000000000000000000000000000000) = SHL v76c(0xa0), v76a(0x1)
    0x76f: v76f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v76e(0x10000000000000000000000000000000000000000), v768(0x1)
    0x771: v771 = CALLDATALOAD v753(0x4)
    0x772: v772 = AND v771, v76f(0xffffffffffffffffffffffffffffffffffffffff)
    0x774: v774(0x20) = CONST 
    0x777: v777(0x24) = ADD v753(0x4), v774(0x20)
    0x778: v778 = CALLDATALOAD v777(0x24)
    0x77a: v77a(0x40) = CONST 
    0x77c: v77c(0x44) = ADD v77a(0x40), v753(0x4)
    0x77d: v77d = CALLDATALOAD v77c(0x44)
    0x77e: v77e(0x1cbe) = CONST 
    0x782: JUMP v77e(0x1cbe)

    Begin block 0x1cbe
    prev=[0x766], succ=[0x1ccf, 0x1d06]
    =================================
    0x1cbf: v1cbf(0x0) = CONST 
    0x1cc1: v1cc1 = SLOAD v1cbf(0x0)
    0x1cc2: v1cc2(0xff) = CONST 
    0x1cc4: v1cc4 = AND v1cc2(0xff), v1cc1
    0x1cc5: v1cc5 = ISZERO v1cc4
    0x1cc6: v1cc6 = ISZERO v1cc5
    0x1cc7: v1cc7(0x1) = CONST 
    0x1cc9: v1cc9 = EQ v1cc7(0x1), v1cc6
    0x1cca: v1cca(0x1d06) = CONST 
    0x1cce: JUMPI v1cca(0x1d06), v1cc9

    Begin block 0x1ccf
    prev=[0x1cbe], succ=[]
    =================================
    0x1ccf: v1ccf(0x40) = CONST 
    0x1cd1: v1cd1 = MLOAD v1ccf(0x40)
    0x1cd2: v1cd2(0x461bcd) = CONST 
    0x1cd6: v1cd6(0xe5) = CONST 
    0x1cd8: v1cd8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1cd6(0xe5), v1cd2(0x461bcd)
    0x1cda: MSTORE v1cd1, v1cd8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cdb: v1cdb(0x4) = CONST 
    0x1cdd: v1cdd = ADD v1cdb(0x4), v1cd1
    0x1ce0: v1ce0(0x20) = CONST 
    0x1ce2: v1ce2 = ADD v1ce0(0x20), v1cdd
    0x1ce5: v1ce5(0x20) = SUB v1ce2, v1cdd
    0x1ce7: MSTORE v1cdd, v1ce5(0x20)
    0x1ce8: v1ce8(0x32) = CONST 
    0x1ceb: MSTORE v1ce2, v1ce8(0x32)
    0x1cec: v1cec(0x20) = CONST 
    0x1cee: v1cee = ADD v1cec(0x20), v1ce2
    0x1cf0: v1cf0(0x37d5) = CONST 
    0x1cf4: v1cf4(0x32) = CONST 
    0x1cf7: CODECOPY v1cee, v1cf0(0x37d5), v1cf4(0x32)
    0x1cf8: v1cf8(0x40) = CONST 
    0x1cfa: v1cfa = ADD v1cf8(0x40), v1cee
    0x1cfe: v1cfe(0x40) = CONST 
    0x1d00: v1d00 = MLOAD v1cfe(0x40)
    0x1d03: v1d03(0x84) = SUB v1cfa, v1d00
    0x1d05: REVERT v1d00, v1d03(0x84)

    Begin block 0x1d06
    prev=[0x1cbe], succ=[0x1d1a, 0x1d1e]
    =================================
    0x1d07: v1d07(0x7) = CONST 
    0x1d09: v1d09 = SLOAD v1d07(0x7)
    0x1d0a: v1d0a(0x1) = CONST 
    0x1d0c: v1d0c(0x1) = CONST 
    0x1d0e: v1d0e(0xa0) = CONST 
    0x1d10: v1d10(0x10000000000000000000000000000000000000000) = SHL v1d0e(0xa0), v1d0c(0x1)
    0x1d11: v1d11(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d10(0x10000000000000000000000000000000000000000), v1d0a(0x1)
    0x1d12: v1d12 = AND v1d11(0xffffffffffffffffffffffffffffffffffffffff), v1d09
    0x1d13: v1d13 = CALLER 
    0x1d14: v1d14 = EQ v1d13, v1d12
    0x1d15: v1d15(0x1d1e) = CONST 
    0x1d19: JUMPI v1d15(0x1d1e), v1d14

    Begin block 0x1d1a
    prev=[0x1d06], succ=[]
    =================================
    0x1d1a: v1d1a(0x0) = CONST 
    0x1d1d: REVERT v1d1a(0x0), v1d1a(0x0)

    Begin block 0x1d1e
    prev=[0x1d06], succ=[0x3fd2]
    =================================
    0x1d1f: v1d1f(0x1d2e) = CONST 
    0x1d23: v1d23(0x3fd2) = CONST 
    0x1d29: v1d29(0x1ec5) = CONST 
    0x1d2d: v1d2d_0 = CALLPRIVATE v1d29(0x1ec5), v77d, v778, v1d23(0x3fd2)

    Begin block 0x3fd2
    prev=[0x1d1e], succ=[0x1ffaB0x3fd2]
    =================================
    0x3fd3: v3fd3(0x1) = CONST 
    0x3fd5: v3fd5(0x1) = CONST 
    0x3fd7: v3fd7(0xa0) = CONST 
    0x3fd9: v3fd9(0x10000000000000000000000000000000000000000) = SHL v3fd7(0xa0), v3fd5(0x1)
    0x3fda: v3fda(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3fd9(0x10000000000000000000000000000000000000000), v3fd3(0x1)
    0x3fdc: v3fdc = AND v772, v3fda(0xffffffffffffffffffffffffffffffffffffffff)
    0x3fdd: v3fdd(0x0) = CONST 
    0x3fe1: MSTORE v3fdd(0x0), v3fdc
    0x3fe2: v3fe2(0x3) = CONST 
    0x3fe4: v3fe4(0x20) = CONST 
    0x3fe6: MSTORE v3fe4(0x20), v3fe2(0x3)
    0x3fe7: v3fe7(0x40) = CONST 
    0x3fea: v3fea = SHA3 v3fdd(0x0), v3fe7(0x40)
    0x3feb: v3feb = SLOAD v3fea
    0x3fed: v3fed(0x1ffa) = CONST 
    0x3ff1: JUMP v3fed(0x1ffa)

    Begin block 0x1ffaB0x3fd2
    prev=[0x3fd2], succ=[0x2009B0x3fd2, 0x4083B0x3fd2]
    =================================
    0x1ffbS0x3fd2: v1ffbV3fd2(0x0) = CONST 
    0x1fffS0x3fd2: v1fffV3fd2 = ADD v1d2d_0, v3feb
    0x2002S0x3fd2: v2002V3fd2 = LT v1fffV3fd2, v3feb
    0x2003S0x3fd2: v2003V3fd2 = ISZERO v2002V3fd2
    0x2004S0x3fd2: v2004V3fd2(0x4083) = CONST 
    0x2008S0x3fd2: JUMPI v2004V3fd2(0x4083), v2003V3fd2

    Begin block 0x2009B0x3fd2
    prev=[0x1ffaB0x3fd2], succ=[]
    =================================
    0x2009S0x3fd2: v2009V3fd2(0x40) = CONST 
    0x200cS0x3fd2: v200cV3fd2 = MLOAD v2009V3fd2(0x40)
    0x200dS0x3fd2: v200dV3fd2(0x461bcd) = CONST 
    0x2011S0x3fd2: v2011V3fd2(0xe5) = CONST 
    0x2013S0x3fd2: v2013V3fd2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2011V3fd2(0xe5), v200dV3fd2(0x461bcd)
    0x2015S0x3fd2: MSTORE v200cV3fd2, v2013V3fd2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2016S0x3fd2: v2016V3fd2(0x20) = CONST 
    0x2018S0x3fd2: v2018V3fd2(0x4) = CONST 
    0x201bS0x3fd2: v201bV3fd2 = ADD v200cV3fd2, v2018V3fd2(0x4)
    0x201cS0x3fd2: MSTORE v201bV3fd2, v2016V3fd2(0x20)
    0x201dS0x3fd2: v201dV3fd2(0x1b) = CONST 
    0x201fS0x3fd2: v201fV3fd2(0x24) = CONST 
    0x2022S0x3fd2: v2022V3fd2 = ADD v200cV3fd2, v201fV3fd2(0x24)
    0x2023S0x3fd2: MSTORE v2022V3fd2, v201dV3fd2(0x1b)
    0x2024S0x3fd2: v2024V3fd2(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2045S0x3fd2: v2045V3fd2(0x44) = CONST 
    0x2048S0x3fd2: v2048V3fd2 = ADD v200cV3fd2, v2045V3fd2(0x44)
    0x2049S0x3fd2: MSTORE v2048V3fd2, v2024V3fd2(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x204bS0x3fd2: v204bV3fd2 = MLOAD v2009V3fd2(0x40)
    0x204fS0x3fd2: v204fV3fd2(0x0) = SUB v200cV3fd2, v204bV3fd2
    0x2050S0x3fd2: v2050V3fd2(0x64) = CONST 
    0x2052S0x3fd2: v2052V3fd2(0x64) = ADD v2050V3fd2(0x64), v204fV3fd2(0x0)
    0x2054S0x3fd2: REVERT v204bV3fd2, v2052V3fd2(0x64)

    Begin block 0x4083B0x3fd2
    prev=[0x1ffaB0x3fd2], succ=[0x1d2e]
    =================================
    0x4089S0x3fd2: JUMP v1d1f(0x1d2e)

    Begin block 0x1d2e
    prev=[0x4083B0x3fd2], succ=[0x1ffaB0x1d2e]
    =================================
    0x1d2f: v1d2f(0x1) = CONST 
    0x1d31: v1d31(0x1) = CONST 
    0x1d33: v1d33(0xa0) = CONST 
    0x1d35: v1d35(0x10000000000000000000000000000000000000000) = SHL v1d33(0xa0), v1d31(0x1)
    0x1d36: v1d36(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d35(0x10000000000000000000000000000000000000000), v1d2f(0x1)
    0x1d38: v1d38 = AND v772, v1d36(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d39: v1d39(0x0) = CONST 
    0x1d3d: MSTORE v1d39(0x0), v1d38
    0x1d3e: v1d3e(0x3) = CONST 
    0x1d40: v1d40(0x20) = CONST 
    0x1d44: MSTORE v1d40(0x20), v1d3e(0x3)
    0x1d45: v1d45(0x40) = CONST 
    0x1d48: v1d48 = SHA3 v1d39(0x0), v1d45(0x40)
    0x1d4b: SSTORE v1d48, v1fffV3fd2
    0x1d4c: v1d4c(0x7) = CONST 
    0x1d4f: v1d4f = ADD v1d48, v1d4c(0x7)
    0x1d51: v1d51 = SLOAD v1d4f
    0x1d52: v1d52(0x1) = CONST 
    0x1d56: v1d56 = ADD v1d52(0x1), v1d51
    0x1d58: SSTORE v1d4f, v1d56
    0x1d5b: MSTORE v1d39(0x0), v1d4f
    0x1d5e: v1d5e = SHA3 v1d39(0x0), v1d40(0x20)
    0x1d61: v1d61 = ADD v1d51, v1d5e
    0x1d65: SSTORE v1d61, v1fffV3fd2
    0x1d68: MSTORE v1d39(0x0), v1d38
    0x1d69: v1d69 = ADD v1d52(0x1), v1d48
    0x1d6a: v1d6a = SLOAD v1d69
    0x1d6b: v1d6b(0x1d76) = CONST 
    0x1d71: v1d71(0x1ffa) = CONST 
    0x1d75: JUMP v1d71(0x1ffa)

    Begin block 0x1ffaB0x1d2e
    prev=[0x1d2e], succ=[0x2009B0x1d2e, 0x4083B0x1d2e]
    =================================
    0x1ffbS0x1d2e: v1ffbV1d2e(0x0) = CONST 
    0x1fffS0x1d2e: v1fffV1d2e = ADD v77d, v1d6a
    0x2002S0x1d2e: v2002V1d2e = LT v1fffV1d2e, v1d6a
    0x2003S0x1d2e: v2003V1d2e = ISZERO v2002V1d2e
    0x2004S0x1d2e: v2004V1d2e(0x4083) = CONST 
    0x2008S0x1d2e: JUMPI v2004V1d2e(0x4083), v2003V1d2e

    Begin block 0x2009B0x1d2e
    prev=[0x1ffaB0x1d2e], succ=[]
    =================================
    0x2009S0x1d2e: v2009V1d2e(0x40) = CONST 
    0x200cS0x1d2e: v200cV1d2e = MLOAD v2009V1d2e(0x40)
    0x200dS0x1d2e: v200dV1d2e(0x461bcd) = CONST 
    0x2011S0x1d2e: v2011V1d2e(0xe5) = CONST 
    0x2013S0x1d2e: v2013V1d2e(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2011V1d2e(0xe5), v200dV1d2e(0x461bcd)
    0x2015S0x1d2e: MSTORE v200cV1d2e, v2013V1d2e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2016S0x1d2e: v2016V1d2e(0x20) = CONST 
    0x2018S0x1d2e: v2018V1d2e(0x4) = CONST 
    0x201bS0x1d2e: v201bV1d2e = ADD v200cV1d2e, v2018V1d2e(0x4)
    0x201cS0x1d2e: MSTORE v201bV1d2e, v2016V1d2e(0x20)
    0x201dS0x1d2e: v201dV1d2e(0x1b) = CONST 
    0x201fS0x1d2e: v201fV1d2e(0x24) = CONST 
    0x2022S0x1d2e: v2022V1d2e = ADD v200cV1d2e, v201fV1d2e(0x24)
    0x2023S0x1d2e: MSTORE v2022V1d2e, v201dV1d2e(0x1b)
    0x2024S0x1d2e: v2024V1d2e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2045S0x1d2e: v2045V1d2e(0x44) = CONST 
    0x2048S0x1d2e: v2048V1d2e = ADD v200cV1d2e, v2045V1d2e(0x44)
    0x2049S0x1d2e: MSTORE v2048V1d2e, v2024V1d2e(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x204bS0x1d2e: v204bV1d2e = MLOAD v2009V1d2e(0x40)
    0x204fS0x1d2e: v204fV1d2e(0x0) = SUB v200cV1d2e, v204bV1d2e
    0x2050S0x1d2e: v2050V1d2e(0x64) = CONST 
    0x2052S0x1d2e: v2052V1d2e(0x64) = ADD v2050V1d2e(0x64), v204fV1d2e(0x0)
    0x2054S0x1d2e: REVERT v204bV1d2e, v2052V1d2e(0x64)

    Begin block 0x4083B0x1d2e
    prev=[0x1ffaB0x1d2e], succ=[0x1d76]
    =================================
    0x4089S0x1d2e: JUMP v1d6b(0x1d76)

    Begin block 0x1d76
    prev=[0x4083B0x1d2e], succ=[0x3d9e]
    =================================
    0x1d77: v1d77(0x1) = CONST 
    0x1d79: v1d79(0x1) = CONST 
    0x1d7b: v1d7b(0xa0) = CONST 
    0x1d7d: v1d7d(0x10000000000000000000000000000000000000000) = SHL v1d7b(0xa0), v1d79(0x1)
    0x1d7e: v1d7e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1d7d(0x10000000000000000000000000000000000000000), v1d77(0x1)
    0x1d81: v1d81 = AND v772, v1d7e(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d82: v1d82(0x0) = CONST 
    0x1d86: MSTORE v1d82(0x0), v1d81
    0x1d87: v1d87(0x3) = CONST 
    0x1d89: v1d89(0x20) = CONST 
    0x1d8d: MSTORE v1d89(0x20), v1d87(0x3)
    0x1d8e: v1d8e(0x40) = CONST 
    0x1d91: v1d91 = SHA3 v1d82(0x0), v1d8e(0x40)
    0x1d92: v1d92(0x1) = CONST 
    0x1d96: v1d96 = ADD v1d91, v1d92(0x1)
    0x1d99: SSTORE v1d96, v1fffV1d2e
    0x1d9a: v1d9a(0x8) = CONST 
    0x1d9e: v1d9e = ADD v1d91, v1d9a(0x8)
    0x1da0: v1da0 = SLOAD v1d9e
    0x1da3: v1da3 = ADD v1da0, v1d92(0x1)
    0x1da5: SSTORE v1d9e, v1da3
    0x1da7: MSTORE v1d82(0x0), v1d9e
    0x1da9: v1da9 = SHA3 v1d82(0x0), v1d89(0x20)
    0x1daa: v1daa = ADD v1da9, v1da0
    0x1dae: SSTORE v1daa, v1fffV1d2e
    0x1db1: JUMP v74f(0x3d9e)

    Begin block 0x3d9e
    prev=[0x1d76], succ=[]
    =================================
    0x3d9f: STOP 

}

function connectorContract()() public {
    Begin block 0x783
    prev=[], succ=[0x78c, 0x790]
    =================================
    0x784: v784 = CALLVALUE 
    0x786: v786 = ISZERO v784
    0x787: v787(0x790) = CONST 
    0x78b: JUMPI v787(0x790), v786

    Begin block 0x78c
    prev=[0x783], succ=[]
    =================================
    0x78c: v78c(0x0) = CONST 
    0x78f: REVERT v78c(0x0), v78c(0x0)

    Begin block 0x790
    prev=[0x783], succ=[0x1db2]
    =================================
    0x792: v792(0x3dbf) = CONST 
    0x796: v796(0x1db2) = CONST 
    0x79a: JUMP v796(0x1db2)

    Begin block 0x1db2
    prev=[0x790], succ=[0x3dbf]
    =================================
    0x1db3: v1db3(0x6) = CONST 
    0x1db5: v1db5 = SLOAD v1db3(0x6)
    0x1db6: v1db6(0x1) = CONST 
    0x1db8: v1db8(0x1) = CONST 
    0x1dba: v1dba(0xa0) = CONST 
    0x1dbc: v1dbc(0x10000000000000000000000000000000000000000) = SHL v1dba(0xa0), v1db8(0x1)
    0x1dbd: v1dbd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1dbc(0x10000000000000000000000000000000000000000), v1db6(0x1)
    0x1dbe: v1dbe = AND v1dbd(0xffffffffffffffffffffffffffffffffffffffff), v1db5
    0x1dc0: JUMP v792(0x3dbf)

    Begin block 0x3dbf
    prev=[0x1db2], succ=[]
    =================================
    0x3dc0: v3dc0(0x40) = CONST 
    0x3dc3: v3dc3 = MLOAD v3dc0(0x40)
    0x3dc4: v3dc4(0x1) = CONST 
    0x3dc6: v3dc6(0x1) = CONST 
    0x3dc8: v3dc8(0xa0) = CONST 
    0x3dca: v3dca(0x10000000000000000000000000000000000000000) = SHL v3dc8(0xa0), v3dc6(0x1)
    0x3dcb: v3dcb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3dca(0x10000000000000000000000000000000000000000), v3dc4(0x1)
    0x3dce: v3dce = AND v1dbe, v3dcb(0xffffffffffffffffffffffffffffffffffffffff)
    0x3dd0: MSTORE v3dc3, v3dce
    0x3dd1: v3dd1 = MLOAD v3dc0(0x40)
    0x3dd5: v3dd5(0x0) = SUB v3dc3, v3dd1
    0x3dd6: v3dd6(0x20) = CONST 
    0x3dd8: v3dd8(0x20) = ADD v3dd6(0x20), v3dd5(0x0)
    0x3dda: RETURN v3dd1, v3dd8(0x20)

}

