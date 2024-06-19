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
    prev=[0x0], succ=[0x1a, 0x39c9]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x392c: v392c(0x39c9) = CONST 
    0x392d: JUMPI v392c(0x39c9), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x10f, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x70a08231) = CONST 
    0x26: v26 = GT v21(0x70a08231), v1f
    0x27: v27(0x10f) = CONST 
    0x2a: JUMPI v27(0x10f), v26

    Begin block 0x10f
    prev=[0x1a], succ=[0x187, 0x11b]
    =================================
    0x111: v111(0x3357162b) = CONST 
    0x116: v116 = GT v111(0x3357162b), v1f
    0x117: v117(0x187) = CONST 
    0x11a: JUMPI v117(0x187), v116

    Begin block 0x187
    prev=[0x10f], succ=[0x1c3, 0x193]
    =================================
    0x189: v189(0x1a895266) = CONST 
    0x18e: v18e = GT v189(0x1a895266), v1f
    0x18f: v18f(0x1c3) = CONST 
    0x192: JUMPI v18f(0x1c3), v18e

    Begin block 0x1c3
    prev=[0x187], succ=[0x396c, 0x1cf]
    =================================
    0x1c5: v1c5(0x6fdde03) = CONST 
    0x1ca: v1ca = EQ v1c5(0x6fdde03), v1f
    0x3966: v3966(0x396c) = CONST 
    0x3967: JUMPI v3966(0x396c), v1ca

    Begin block 0x396c
    prev=[0x1c3], succ=[]
    =================================
    0x396d: v396d(0x1ea) = CONST 
    0x396e: CALLPRIVATE v396d(0x1ea)

    Begin block 0x1cf
    prev=[0x1c3], succ=[0x396f, 0x1da]
    =================================
    0x1d0: v1d0(0x95ea7b3) = CONST 
    0x1d5: v1d5 = EQ v1d0(0x95ea7b3), v1f
    0x3968: v3968(0x396f) = CONST 
    0x3969: JUMPI v3968(0x396f), v1d5

    Begin block 0x396f
    prev=[0x1cf], succ=[]
    =================================
    0x3970: v3970(0x267) = CONST 
    0x3971: CALLPRIVATE v3970(0x267)

    Begin block 0x1da
    prev=[0x1cf], succ=[0x3972, 0x1e5]
    =================================
    0x1db: v1db(0x18160ddd) = CONST 
    0x1e0: v1e0 = EQ v1db(0x18160ddd), v1f
    0x396a: v396a(0x3972) = CONST 
    0x396b: JUMPI v396a(0x3972), v1e0

    Begin block 0x3972
    prev=[0x1da], succ=[]
    =================================
    0x3973: v3973(0x2b4) = CONST 
    0x3974: CALLPRIVATE v3973(0x2b4)

    Begin block 0x1e5
    prev=[0x1da], succ=[]
    =================================
    0x1e6: v1e6(0x0) = CONST 
    0x1e9: REVERT v1e6(0x0), v1e6(0x0)

    Begin block 0x193
    prev=[0x187], succ=[0x3975, 0x19e]
    =================================
    0x194: v194(0x1a895266) = CONST 
    0x199: v199 = EQ v194(0x1a895266), v1f
    0x395e: v395e(0x3975) = CONST 
    0x395f: JUMPI v395e(0x3975), v199

    Begin block 0x3975
    prev=[0x193], succ=[]
    =================================
    0x3976: v3976(0x2ce) = CONST 
    0x3977: CALLPRIVATE v3976(0x2ce)

    Begin block 0x19e
    prev=[0x193], succ=[0x3978, 0x1a9]
    =================================
    0x19f: v19f(0x23b872dd) = CONST 
    0x1a4: v1a4 = EQ v19f(0x23b872dd), v1f
    0x3960: v3960(0x3978) = CONST 
    0x3961: JUMPI v3960(0x3978), v1a4

    Begin block 0x3978
    prev=[0x19e], succ=[]
    =================================
    0x3979: v3979(0x303) = CONST 
    0x397a: CALLPRIVATE v3979(0x303)

    Begin block 0x1a9
    prev=[0x19e], succ=[0x397b, 0x1b4]
    =================================
    0x1aa: v1aa(0x3092afd5) = CONST 
    0x1af: v1af = EQ v1aa(0x3092afd5), v1f
    0x3962: v3962(0x397b) = CONST 
    0x3963: JUMPI v3962(0x397b), v1af

    Begin block 0x397b
    prev=[0x1a9], succ=[]
    =================================
    0x397c: v397c(0x346) = CONST 
    0x397d: CALLPRIVATE v397c(0x346)

    Begin block 0x1b4
    prev=[0x1a9], succ=[0x1bf, 0x397e]
    =================================
    0x1b5: v1b5(0x313ce567) = CONST 
    0x1ba: v1ba = EQ v1b5(0x313ce567), v1f
    0x3964: v3964(0x397e) = CONST 
    0x3965: JUMPI v3964(0x397e), v1ba

    Begin block 0x1bf
    prev=[0x1b4], succ=[0x325e]
    =================================
    0x1bf: v1bf(0x325e) = CONST 
    0x1c2: JUMP v1bf(0x325e)

    Begin block 0x325e
    prev=[0x1bf], succ=[]
    =================================
    0x325f: v325f(0x0) = CONST 
    0x3262: REVERT v325f(0x0), v325f(0x0)

    Begin block 0x397e
    prev=[0x1b4], succ=[]
    =================================
    0x397f: v397f(0x379) = CONST 
    0x3980: CALLPRIVATE v397f(0x379)

    Begin block 0x11b
    prev=[0x10f], succ=[0x156, 0x126]
    =================================
    0x11c: v11c(0x42966c68) = CONST 
    0x121: v121 = GT v11c(0x42966c68), v1f
    0x122: v122(0x156) = CONST 
    0x125: JUMPI v122(0x156), v121

    Begin block 0x156
    prev=[0x11b], succ=[0x3981, 0x162]
    =================================
    0x158: v158(0x3357162b) = CONST 
    0x15d: v15d = EQ v158(0x3357162b), v1f
    0x3956: v3956(0x3981) = CONST 
    0x3957: JUMPI v3956(0x3981), v15d

    Begin block 0x3981
    prev=[0x156], succ=[]
    =================================
    0x3982: v3982(0x397) = CONST 
    0x3983: CALLPRIVATE v3982(0x397)

    Begin block 0x162
    prev=[0x156], succ=[0x3984, 0x16d]
    =================================
    0x163: v163(0x35d99f35) = CONST 
    0x168: v168 = EQ v163(0x35d99f35), v1f
    0x3958: v3958(0x3984) = CONST 
    0x3959: JUMPI v3958(0x3984), v168

    Begin block 0x3984
    prev=[0x162], succ=[]
    =================================
    0x3985: v3985(0x583) = CONST 
    0x3986: CALLPRIVATE v3985(0x583)

    Begin block 0x16d
    prev=[0x162], succ=[0x3987, 0x178]
    =================================
    0x16e: v16e(0x3f4ba83a) = CONST 
    0x173: v173 = EQ v16e(0x3f4ba83a), v1f
    0x395a: v395a(0x3987) = CONST 
    0x395b: JUMPI v395a(0x3987), v173

    Begin block 0x3987
    prev=[0x16d], succ=[]
    =================================
    0x3988: v3988(0x5b4) = CONST 
    0x3989: CALLPRIVATE v3988(0x5b4)

    Begin block 0x178
    prev=[0x16d], succ=[0x183, 0x398a]
    =================================
    0x179: v179(0x40c10f19) = CONST 
    0x17e: v17e = EQ v179(0x40c10f19), v1f
    0x395c: v395c(0x398a) = CONST 
    0x395d: JUMPI v395c(0x398a), v17e

    Begin block 0x183
    prev=[0x178], succ=[0x323a]
    =================================
    0x183: v183(0x323a) = CONST 
    0x186: JUMP v183(0x323a)

    Begin block 0x323a
    prev=[0x183], succ=[]
    =================================
    0x323b: v323b(0x0) = CONST 
    0x323e: REVERT v323b(0x0), v323b(0x0)

    Begin block 0x398a
    prev=[0x178], succ=[]
    =================================
    0x398b: v398b(0x5bc) = CONST 
    0x398c: CALLPRIVATE v398b(0x5bc)

    Begin block 0x126
    prev=[0x11b], succ=[0x398d, 0x131]
    =================================
    0x127: v127(0x42966c68) = CONST 
    0x12c: v12c = EQ v127(0x42966c68), v1f
    0x394e: v394e(0x398d) = CONST 
    0x394f: JUMPI v394e(0x398d), v12c

    Begin block 0x398d
    prev=[0x126], succ=[]
    =================================
    0x398e: v398e(0x5f5) = CONST 
    0x398f: CALLPRIVATE v398e(0x5f5)

    Begin block 0x131
    prev=[0x126], succ=[0x3990, 0x13c]
    =================================
    0x132: v132(0x4e44d956) = CONST 
    0x137: v137 = EQ v132(0x4e44d956), v1f
    0x3950: v3950(0x3990) = CONST 
    0x3951: JUMPI v3950(0x3990), v137

    Begin block 0x3990
    prev=[0x131], succ=[]
    =================================
    0x3991: v3991(0x612) = CONST 
    0x3992: CALLPRIVATE v3991(0x612)

    Begin block 0x13c
    prev=[0x131], succ=[0x3993, 0x147]
    =================================
    0x13d: v13d(0x554bab3c) = CONST 
    0x142: v142 = EQ v13d(0x554bab3c), v1f
    0x3952: v3952(0x3993) = CONST 
    0x3953: JUMPI v3952(0x3993), v142

    Begin block 0x3993
    prev=[0x13c], succ=[]
    =================================
    0x3994: v3994(0x64b) = CONST 
    0x3995: CALLPRIVATE v3994(0x64b)

    Begin block 0x147
    prev=[0x13c], succ=[0x152, 0x3996]
    =================================
    0x148: v148(0x5c975abb) = CONST 
    0x14d: v14d = EQ v148(0x5c975abb), v1f
    0x3954: v3954(0x3996) = CONST 
    0x3955: JUMPI v3954(0x3996), v14d

    Begin block 0x152
    prev=[0x147], succ=[0x3216]
    =================================
    0x152: v152(0x3216) = CONST 
    0x155: JUMP v152(0x3216)

    Begin block 0x3216
    prev=[0x152], succ=[]
    =================================
    0x3217: v3217(0x0) = CONST 
    0x321a: REVERT v3217(0x0), v3217(0x0)

    Begin block 0x3996
    prev=[0x147], succ=[]
    =================================
    0x3997: v3997(0x67e) = CONST 
    0x3998: CALLPRIVATE v3997(0x67e)

    Begin block 0x2b
    prev=[0x1a], succ=[0xa2, 0x36]
    =================================
    0x2c: v2c(0xaa271e1a) = CONST 
    0x31: v31 = GT v2c(0xaa271e1a), v1f
    0x32: v32(0xa2) = CONST 
    0x35: JUMPI v32(0xa2), v31

    Begin block 0xa2
    prev=[0x2b], succ=[0xde, 0xae]
    =================================
    0xa4: va4(0x95d89b41) = CONST 
    0xa9: va9 = GT va4(0x95d89b41), v1f
    0xaa: vaa(0xde) = CONST 
    0xad: JUMPI vaa(0xde), va9

    Begin block 0xde
    prev=[0xa2], succ=[0x3999, 0xea]
    =================================
    0xe0: ve0(0x70a08231) = CONST 
    0xe5: ve5 = EQ ve0(0x70a08231), v1f
    0x3946: v3946(0x3999) = CONST 
    0x3947: JUMPI v3946(0x3999), ve5

    Begin block 0x3999
    prev=[0xde], succ=[]
    =================================
    0x399a: v399a(0x686) = CONST 
    0x399b: CALLPRIVATE v399a(0x686)

    Begin block 0xea
    prev=[0xde], succ=[0x399c, 0xf5]
    =================================
    0xeb: veb(0x8456cb59) = CONST 
    0xf0: vf0 = EQ veb(0x8456cb59), v1f
    0x3948: v3948(0x399c) = CONST 
    0x3949: JUMPI v3948(0x399c), vf0

    Begin block 0x399c
    prev=[0xea], succ=[]
    =================================
    0x399d: v399d(0x6b9) = CONST 
    0x399e: CALLPRIVATE v399d(0x6b9)

    Begin block 0xf5
    prev=[0xea], succ=[0x100, 0x399f]
    =================================
    0xf6: vf6(0x8a6db9c3) = CONST 
    0xfb: vfb = EQ vf6(0x8a6db9c3), v1f
    0x394a: v394a(0x399f) = CONST 
    0x394b: JUMPI v394a(0x399f), vfb

    Begin block 0x100
    prev=[0xf5], succ=[0x10b, 0x39a2]
    =================================
    0x101: v101(0x8da5cb5b) = CONST 
    0x106: v106 = EQ v101(0x8da5cb5b), v1f
    0x394c: v394c(0x39a2) = CONST 
    0x394d: JUMPI v394c(0x39a2), v106

    Begin block 0x10b
    prev=[0x100], succ=[0x31f2]
    =================================
    0x10b: v10b(0x31f2) = CONST 
    0x10e: JUMP v10b(0x31f2)

    Begin block 0x31f2
    prev=[0x10b], succ=[]
    =================================
    0x31f3: v31f3(0x0) = CONST 
    0x31f6: REVERT v31f3(0x0), v31f3(0x0)

    Begin block 0x39a2
    prev=[0x100], succ=[]
    =================================
    0x39a3: v39a3(0x6f4) = CONST 
    0x39a4: CALLPRIVATE v39a3(0x6f4)

    Begin block 0x399f
    prev=[0xf5], succ=[]
    =================================
    0x39a0: v39a0(0x6c1) = CONST 
    0x39a1: CALLPRIVATE v39a0(0x6c1)

    Begin block 0xae
    prev=[0xa2], succ=[0x39a5, 0xb9]
    =================================
    0xaf: vaf(0x95d89b41) = CONST 
    0xb4: vb4 = EQ vaf(0x95d89b41), v1f
    0x393e: v393e(0x39a5) = CONST 
    0x393f: JUMPI v393e(0x39a5), vb4

    Begin block 0x39a5
    prev=[0xae], succ=[]
    =================================
    0x39a6: v39a6(0x6fc) = CONST 
    0x39a7: CALLPRIVATE v39a6(0x6fc)

    Begin block 0xb9
    prev=[0xae], succ=[0xc4, 0x39a8]
    =================================
    0xba: vba(0x9fd0506d) = CONST 
    0xbf: vbf = EQ vba(0x9fd0506d), v1f
    0x3940: v3940(0x39a8) = CONST 
    0x3941: JUMPI v3940(0x39a8), vbf

    Begin block 0xc4
    prev=[0xb9], succ=[0x39ab, 0xcf]
    =================================
    0xc5: vc5(0xa9059cbb) = CONST 
    0xca: vca = EQ vc5(0xa9059cbb), v1f
    0x3942: v3942(0x39ab) = CONST 
    0x3943: JUMPI v3942(0x39ab), vca

    Begin block 0x39ab
    prev=[0xc4], succ=[]
    =================================
    0x39ac: v39ac(0x70c) = CONST 
    0x39ad: CALLPRIVATE v39ac(0x70c)

    Begin block 0xcf
    prev=[0xc4], succ=[0xda, 0x39ae]
    =================================
    0xd0: vd0(0xaa20e1e4) = CONST 
    0xd5: vd5 = EQ vd0(0xaa20e1e4), v1f
    0x3944: v3944(0x39ae) = CONST 
    0x3945: JUMPI v3944(0x39ae), vd5

    Begin block 0xda
    prev=[0xcf], succ=[0x31ce]
    =================================
    0xda: vda(0x31ce) = CONST 
    0xdd: JUMP vda(0x31ce)

    Begin block 0x31ce
    prev=[0xda], succ=[]
    =================================
    0x31cf: v31cf(0x0) = CONST 
    0x31d2: REVERT v31cf(0x0), v31cf(0x0)

    Begin block 0x39ae
    prev=[0xcf], succ=[]
    =================================
    0x39af: v39af(0x745) = CONST 
    0x39b0: CALLPRIVATE v39af(0x745)

    Begin block 0x39a8
    prev=[0xb9], succ=[]
    =================================
    0x39a9: v39a9(0x704) = CONST 
    0x39aa: CALLPRIVATE v39a9(0x704)

    Begin block 0x36
    prev=[0x2b], succ=[0x71, 0x41]
    =================================
    0x37: v37(0xe5a6b10f) = CONST 
    0x3c: v3c = GT v37(0xe5a6b10f), v1f
    0x3d: v3d(0x71) = CONST 
    0x40: JUMPI v3d(0x71), v3c

    Begin block 0x71
    prev=[0x36], succ=[0x39b1, 0x7d]
    =================================
    0x73: v73(0xaa271e1a) = CONST 
    0x78: v78 = EQ v73(0xaa271e1a), v1f
    0x3936: v3936(0x39b1) = CONST 
    0x3937: JUMPI v3936(0x39b1), v78

    Begin block 0x39b1
    prev=[0x71], succ=[]
    =================================
    0x39b2: v39b2(0x778) = CONST 
    0x39b3: CALLPRIVATE v39b2(0x778)

    Begin block 0x7d
    prev=[0x71], succ=[0x39b4, 0x88]
    =================================
    0x7e: v7e(0xad38bf22) = CONST 
    0x83: v83 = EQ v7e(0xad38bf22), v1f
    0x3938: v3938(0x39b4) = CONST 
    0x3939: JUMPI v3938(0x39b4), v83

    Begin block 0x39b4
    prev=[0x7d], succ=[]
    =================================
    0x39b5: v39b5(0x7ab) = CONST 
    0x39b6: CALLPRIVATE v39b5(0x7ab)

    Begin block 0x88
    prev=[0x7d], succ=[0x39b7, 0x93]
    =================================
    0x89: v89(0xbd102430) = CONST 
    0x8e: v8e = EQ v89(0xbd102430), v1f
    0x393a: v393a(0x39b7) = CONST 
    0x393b: JUMPI v393a(0x39b7), v8e

    Begin block 0x39b7
    prev=[0x88], succ=[]
    =================================
    0x39b8: v39b8(0x7de) = CONST 
    0x39b9: CALLPRIVATE v39b8(0x7de)

    Begin block 0x93
    prev=[0x88], succ=[0x9e, 0x39ba]
    =================================
    0x94: v94(0xdd62ed3e) = CONST 
    0x99: v99 = EQ v94(0xdd62ed3e), v1f
    0x393c: v393c(0x39ba) = CONST 
    0x393d: JUMPI v393c(0x39ba), v99

    Begin block 0x9e
    prev=[0x93], succ=[0x31aa]
    =================================
    0x9e: v9e(0x31aa) = CONST 
    0xa1: JUMP v9e(0x31aa)

    Begin block 0x31aa
    prev=[0x9e], succ=[]
    =================================
    0x31ab: v31ab(0x0) = CONST 
    0x31ae: REVERT v31ab(0x0), v31ab(0x0)

    Begin block 0x39ba
    prev=[0x93], succ=[]
    =================================
    0x39bb: v39bb(0x7e6) = CONST 
    0x39bc: CALLPRIVATE v39bb(0x7e6)

    Begin block 0x41
    prev=[0x36], succ=[0x39bd, 0x4c]
    =================================
    0x42: v42(0xe5a6b10f) = CONST 
    0x47: v47 = EQ v42(0xe5a6b10f), v1f
    0x392e: v392e(0x39bd) = CONST 
    0x392f: JUMPI v392e(0x39bd), v47

    Begin block 0x39bd
    prev=[0x41], succ=[]
    =================================
    0x39be: v39be(0x821) = CONST 
    0x39bf: CALLPRIVATE v39be(0x821)

    Begin block 0x4c
    prev=[0x41], succ=[0x39c0, 0x57]
    =================================
    0x4d: v4d(0xf2fde38b) = CONST 
    0x52: v52 = EQ v4d(0xf2fde38b), v1f
    0x3930: v3930(0x39c0) = CONST 
    0x3931: JUMPI v3930(0x39c0), v52

    Begin block 0x39c0
    prev=[0x4c], succ=[]
    =================================
    0x39c1: v39c1(0x829) = CONST 
    0x39c2: CALLPRIVATE v39c1(0x829)

    Begin block 0x57
    prev=[0x4c], succ=[0x39c3, 0x62]
    =================================
    0x58: v58(0xf9f92be4) = CONST 
    0x5d: v5d = EQ v58(0xf9f92be4), v1f
    0x3932: v3932(0x39c3) = CONST 
    0x3933: JUMPI v3932(0x39c3), v5d

    Begin block 0x39c3
    prev=[0x57], succ=[]
    =================================
    0x39c4: v39c4(0x85c) = CONST 
    0x39c5: CALLPRIVATE v39c4(0x85c)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0x39c6]
    =================================
    0x63: v63(0xfe575a87) = CONST 
    0x68: v68 = EQ v63(0xfe575a87), v1f
    0x3934: v3934(0x39c6) = CONST 
    0x3935: JUMPI v3934(0x39c6), v68

    Begin block 0x6d
    prev=[0x62], succ=[0x3186]
    =================================
    0x6d: v6d(0x3186) = CONST 
    0x70: JUMP v6d(0x3186)

    Begin block 0x3186
    prev=[0x6d], succ=[]
    =================================
    0x3187: v3187(0x0) = CONST 
    0x318a: REVERT v3187(0x0), v3187(0x0)

    Begin block 0x39c6
    prev=[0x62], succ=[]
    =================================
    0x39c7: v39c7(0x88f) = CONST 
    0x39c8: CALLPRIVATE v39c7(0x88f)

    Begin block 0x39c9
    prev=[0x10], succ=[]
    =================================
    0x39ca: v39ca(0x3162) = CONST 
    0x39cb: CALLPRIVATE v39ca(0x3162)

}

function name()() public {
    Begin block 0x1ea
    prev=[], succ=[0x1f20x1ea]
    =================================
    0x1eb: v1eb(0x1f2) = CONST 
    0x1ee: v1ee(0x8c2) = CONST 
    0x1f1: v1f1_0, v1f1_1 = CALLPRIVATE v1ee(0x8c2), v1eb(0x1f2)

    Begin block 0x1f20x1ea
    prev=[0x1ea], succ=[0x2140x1ea]
    =================================
    0x1f30x1ea: v1ea1f3(0x40) = CONST 
    0x1f60x1ea: v1ea1f6 = MLOAD v1ea1f3(0x40)
    0x1f70x1ea: v1ea1f7(0x20) = CONST 
    0x1fb0x1ea: MSTORE v1ea1f6, v1ea1f7(0x20)
    0x1fd0x1ea: v1ea1fd = MLOAD v1f1_0
    0x2000x1ea: v1ea200 = ADD v1ea1f6, v1ea1f7(0x20)
    0x2010x1ea: MSTORE v1ea200, v1ea1fd
    0x2030x1ea: v1ea203 = MLOAD v1f1_0
    0x20a0x1ea: v1ea20a = ADD v1ea1f6, v1ea1f3(0x40)
    0x20d0x1ea: v1ea20d = ADD v1f1_0, v1ea1f7(0x20)
    0x2120x1ea: v1ea212(0x0) = CONST 

    Begin block 0x2140x1ea
    prev=[0x21d0x1ea, 0x1f20x1ea], succ=[0x22c0x1ea, 0x21d0x1ea]
    =================================
    0x2140x1ea_0x0: v2141ea_0 = PHI v1ea227, v1ea212(0x0)
    0x2170x1ea: v1ea217 = LT v2141ea_0, v1ea203
    0x2180x1ea: v1ea218 = ISZERO v1ea217
    0x2190x1ea: v1ea219(0x22c) = CONST 
    0x21c0x1ea: JUMPI v1ea219(0x22c), v1ea218

    Begin block 0x22c0x1ea
    prev=[0x2140x1ea], succ=[0x2590x1ea, 0x2400x1ea]
    =================================
    0x2350x1ea: v1ea235 = ADD v1ea203, v1ea20a
    0x2370x1ea: v1ea237(0x1f) = CONST 
    0x2390x1ea: v1ea239 = AND v1ea237(0x1f), v1ea203
    0x23b0x1ea: v1ea23b = ISZERO v1ea239
    0x23c0x1ea: v1ea23c(0x259) = CONST 
    0x23f0x1ea: JUMPI v1ea23c(0x259), v1ea23b

    Begin block 0x2590x1ea
    prev=[0x22c0x1ea, 0x2400x1ea], succ=[]
    =================================
    0x2590x1ea_0x1: v2591ea_1 = PHI v1ea256, v1ea235
    0x25f0x1ea: v1ea25f(0x40) = CONST 
    0x2610x1ea: v1ea261 = MLOAD v1ea25f(0x40)
    0x2640x1ea: v1ea264 = SUB v2591ea_1, v1ea261
    0x2660x1ea: RETURN v1ea261, v1ea264

    Begin block 0x2400x1ea
    prev=[0x22c0x1ea], succ=[0x2590x1ea]
    =================================
    0x2420x1ea: v1ea242 = SUB v1ea235, v1ea239
    0x2440x1ea: v1ea244 = MLOAD v1ea242
    0x2450x1ea: v1ea245(0x1) = CONST 
    0x2480x1ea: v1ea248(0x20) = CONST 
    0x24a0x1ea: v1ea24a = SUB v1ea248(0x20), v1ea239
    0x24b0x1ea: v1ea24b(0x100) = CONST 
    0x24e0x1ea: v1ea24e = EXP v1ea24b(0x100), v1ea24a
    0x24f0x1ea: v1ea24f = SUB v1ea24e, v1ea245(0x1)
    0x2500x1ea: v1ea250 = NOT v1ea24f
    0x2510x1ea: v1ea251 = AND v1ea250, v1ea244
    0x2530x1ea: MSTORE v1ea242, v1ea251
    0x2540x1ea: v1ea254(0x20) = CONST 
    0x2560x1ea: v1ea256 = ADD v1ea254(0x20), v1ea242

    Begin block 0x21d0x1ea
    prev=[0x2140x1ea], succ=[0x2140x1ea]
    =================================
    0x21d0x1ea_0x0: v21d1ea_0 = PHI v1ea227, v1ea212(0x0)
    0x21f0x1ea: v1ea21f = ADD v21d1ea_0, v1ea20d
    0x2200x1ea: v1ea220 = MLOAD v1ea21f
    0x2230x1ea: v1ea223 = ADD v21d1ea_0, v1ea20a
    0x2240x1ea: MSTORE v1ea223, v1ea220
    0x2250x1ea: v1ea225(0x20) = CONST 
    0x2270x1ea: v1ea227 = ADD v1ea225(0x20), v21d1ea_0
    0x2280x1ea: v1ea228(0x214) = CONST 
    0x22b0x1ea: JUMP v1ea228(0x214)

}

function 0x1f5e(0x1f5earg0x0) private {
    Begin block 0x1f5e
    prev=[], succ=[0x37f3, 0x1fbc]
    =================================
    0x1f5f: v1f5f(0x5) = CONST 
    0x1f62: v1f62 = SLOAD v1f5f(0x5)
    0x1f63: v1f63(0x40) = CONST 
    0x1f66: v1f66 = MLOAD v1f63(0x40)
    0x1f67: v1f67(0x20) = CONST 
    0x1f69: v1f69(0x2) = CONST 
    0x1f6b: v1f6b(0x1) = CONST 
    0x1f6e: v1f6e = AND v1f62, v1f6b(0x1)
    0x1f6f: v1f6f = ISZERO v1f6e
    0x1f70: v1f70(0x100) = CONST 
    0x1f73: v1f73 = MUL v1f70(0x100), v1f6f
    0x1f74: v1f74(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f95: v1f95 = ADD v1f74(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v1f73
    0x1f98: v1f98 = AND v1f62, v1f95
    0x1f9c: v1f9c = DIV v1f98, v1f69(0x2)
    0x1f9d: v1f9d(0x1f) = CONST 
    0x1fa0: v1fa0 = ADD v1f9c, v1f9d(0x1f)
    0x1fa3: v1fa3 = DIV v1fa0, v1f67(0x20)
    0x1fa5: v1fa5 = MUL v1f67(0x20), v1fa3
    0x1fa7: v1fa7 = ADD v1f66, v1fa5
    0x1fa9: v1fa9 = ADD v1f67(0x20), v1fa7
    0x1fac: MSTORE v1f63(0x40), v1fa9
    0x1faf: MSTORE v1f66, v1f9c
    0x1fb3: v1fb3 = ADD v1f66, v1f67(0x20)
    0x1fb7: v1fb7 = ISZERO v1f9c
    0x1fb8: v1fb8(0x37f3) = CONST 
    0x1fbb: JUMPI v1fb8(0x37f3), v1fb7

    Begin block 0x37f3
    prev=[0x1f5e], succ=[]
    =================================
    0x37fa: RETURNPRIVATE v1f5earg0, v1f66, v1f5earg0

    Begin block 0x1fbc
    prev=[0x1f5e], succ=[0x1fc4, 0x93b0x1f5e]
    =================================
    0x1fbd: v1fbd(0x1f) = CONST 
    0x1fbf: v1fbf = LT v1fbd(0x1f), v1f9c
    0x1fc0: v1fc0(0x93b) = CONST 
    0x1fc3: JUMPI v1fc0(0x93b), v1fbf

    Begin block 0x1fc4
    prev=[0x1fbc], succ=[0x381a]
    =================================
    0x1fc4: v1fc4(0x100) = CONST 
    0x1fc9: v1fc9 = SLOAD v1f5f(0x5)
    0x1fca: v1fca = DIV v1fc9, v1fc4(0x100)
    0x1fcb: v1fcb = MUL v1fca, v1fc4(0x100)
    0x1fcd: MSTORE v1fb3, v1fcb
    0x1fcf: v1fcf(0x20) = CONST 
    0x1fd1: v1fd1 = ADD v1fcf(0x20), v1fb3
    0x1fd3: v1fd3(0x381a) = CONST 
    0x1fd6: JUMP v1fd3(0x381a)

    Begin block 0x381a
    prev=[0x1fc4], succ=[]
    =================================
    0x3821: RETURNPRIVATE v1f5earg0, v1f66, v1f5earg0

    Begin block 0x93b0x1f5e
    prev=[0x1fbc], succ=[0x9490x1f5e]
    =================================
    0x93d0x1f5e: v1f5e93d = ADD v1fb3, v1f9c
    0x9400x1f5e: v1f5e940(0x0) = CONST 
    0x9420x1f5e: MSTORE v1f5e940(0x0), v1f5f(0x5)
    0x9430x1f5e: v1f5e943(0x20) = CONST 
    0x9450x1f5e: v1f5e945(0x0) = CONST 
    0x9470x1f5e: v1f5e947 = SHA3 v1f5e945(0x0), v1f5e943(0x20)

    Begin block 0x9490x1f5e
    prev=[0x9490x1f5e, 0x93b0x1f5e], succ=[0x9490x1f5e, 0x95d0x1f5e]
    =================================
    0x9490x1f5e_0x0: v9491f5e_0 = PHI v1fb3, v1f5e955
    0x9490x1f5e_0x1: v9491f5e_1 = PHI v1f5e951, v1f5e947
    0x94b0x1f5e: v1f5e94b = SLOAD v9491f5e_1
    0x94d0x1f5e: MSTORE v9491f5e_0, v1f5e94b
    0x94f0x1f5e: v1f5e94f(0x1) = CONST 
    0x9510x1f5e: v1f5e951 = ADD v1f5e94f(0x1), v9491f5e_1
    0x9530x1f5e: v1f5e953(0x20) = CONST 
    0x9550x1f5e: v1f5e955 = ADD v1f5e953(0x20), v9491f5e_0
    0x9580x1f5e: v1f5e958 = GT v1f5e93d, v1f5e955
    0x9590x1f5e: v1f5e959(0x949) = CONST 
    0x95c0x1f5e: JUMPI v1f5e959(0x949), v1f5e958

    Begin block 0x95d0x1f5e
    prev=[0x9490x1f5e], succ=[0x9660x1f5e]
    =================================
    0x95f0x1f5e: v1f5e95f = SUB v1f5e955, v1f5e93d
    0x9600x1f5e: v1f5e960(0x1f) = CONST 
    0x9620x1f5e: v1f5e962 = AND v1f5e960(0x1f), v1f5e95f
    0x9640x1f5e: v1f5e964 = ADD v1f5e93d, v1f5e962

    Begin block 0x9660x1f5e
    prev=[0x95d0x1f5e], succ=[]
    =================================
    0x96d0x1f5e: RETURNPRIVATE v1f5earg0, v1f66, v1f5earg0

}

function 0x24c2(0x24c2arg0x0) private {
    Begin block 0x24c2
    prev=[], succ=[0x386b, 0x2520]
    =================================
    0x24c3: v24c3(0x7) = CONST 
    0x24c6: v24c6 = SLOAD v24c3(0x7)
    0x24c7: v24c7(0x40) = CONST 
    0x24ca: v24ca = MLOAD v24c7(0x40)
    0x24cb: v24cb(0x20) = CONST 
    0x24cd: v24cd(0x2) = CONST 
    0x24cf: v24cf(0x1) = CONST 
    0x24d2: v24d2 = AND v24c6, v24cf(0x1)
    0x24d3: v24d3 = ISZERO v24d2
    0x24d4: v24d4(0x100) = CONST 
    0x24d7: v24d7 = MUL v24d4(0x100), v24d3
    0x24d8: v24d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24f9: v24f9 = ADD v24d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v24d7
    0x24fc: v24fc = AND v24c6, v24f9
    0x2500: v2500 = DIV v24fc, v24cd(0x2)
    0x2501: v2501(0x1f) = CONST 
    0x2504: v2504 = ADD v2500, v2501(0x1f)
    0x2507: v2507 = DIV v2504, v24cb(0x20)
    0x2509: v2509 = MUL v24cb(0x20), v2507
    0x250b: v250b = ADD v24ca, v2509
    0x250d: v250d = ADD v24cb(0x20), v250b
    0x2510: MSTORE v24c7(0x40), v250d
    0x2513: MSTORE v24ca, v2500
    0x2517: v2517 = ADD v24ca, v24cb(0x20)
    0x251b: v251b = ISZERO v2500
    0x251c: v251c(0x386b) = CONST 
    0x251f: JUMPI v251c(0x386b), v251b

    Begin block 0x386b
    prev=[0x24c2], succ=[]
    =================================
    0x3872: RETURNPRIVATE v24c2arg0, v24ca, v24c2arg0

    Begin block 0x2520
    prev=[0x24c2], succ=[0x2528, 0x93b0x24c2]
    =================================
    0x2521: v2521(0x1f) = CONST 
    0x2523: v2523 = LT v2521(0x1f), v2500
    0x2524: v2524(0x93b) = CONST 
    0x2527: JUMPI v2524(0x93b), v2523

    Begin block 0x2528
    prev=[0x2520], succ=[0x3892]
    =================================
    0x2528: v2528(0x100) = CONST 
    0x252d: v252d = SLOAD v24c3(0x7)
    0x252e: v252e = DIV v252d, v2528(0x100)
    0x252f: v252f = MUL v252e, v2528(0x100)
    0x2531: MSTORE v2517, v252f
    0x2533: v2533(0x20) = CONST 
    0x2535: v2535 = ADD v2533(0x20), v2517
    0x2537: v2537(0x3892) = CONST 
    0x253a: JUMP v2537(0x3892)

    Begin block 0x3892
    prev=[0x2528], succ=[]
    =================================
    0x3899: RETURNPRIVATE v24c2arg0, v24ca, v24c2arg0

    Begin block 0x93b0x24c2
    prev=[0x2520], succ=[0x9490x24c2]
    =================================
    0x93d0x24c2: v24c293d = ADD v2517, v2500
    0x9400x24c2: v24c2940(0x0) = CONST 
    0x9420x24c2: MSTORE v24c2940(0x0), v24c3(0x7)
    0x9430x24c2: v24c2943(0x20) = CONST 
    0x9450x24c2: v24c2945(0x0) = CONST 
    0x9470x24c2: v24c2947 = SHA3 v24c2945(0x0), v24c2943(0x20)

    Begin block 0x9490x24c2
    prev=[0x9490x24c2, 0x93b0x24c2], succ=[0x9490x24c2, 0x95d0x24c2]
    =================================
    0x9490x24c2_0x0: v94924c2_0 = PHI v2517, v24c2955
    0x9490x24c2_0x1: v94924c2_1 = PHI v24c2951, v24c2947
    0x94b0x24c2: v24c294b = SLOAD v94924c2_1
    0x94d0x24c2: MSTORE v94924c2_0, v24c294b
    0x94f0x24c2: v24c294f(0x1) = CONST 
    0x9510x24c2: v24c2951 = ADD v24c294f(0x1), v94924c2_1
    0x9530x24c2: v24c2953(0x20) = CONST 
    0x9550x24c2: v24c2955 = ADD v24c2953(0x20), v94924c2_0
    0x9580x24c2: v24c2958 = GT v24c293d, v24c2955
    0x9590x24c2: v24c2959(0x949) = CONST 
    0x95c0x24c2: JUMPI v24c2959(0x949), v24c2958

    Begin block 0x95d0x24c2
    prev=[0x9490x24c2], succ=[0x9660x24c2]
    =================================
    0x95f0x24c2: v24c295f = SUB v24c2955, v24c293d
    0x9600x24c2: v24c2960(0x1f) = CONST 
    0x9620x24c2: v24c2962 = AND v24c2960(0x1f), v24c295f
    0x9640x24c2: v24c2964 = ADD v24c293d, v24c2962

    Begin block 0x9660x24c2
    prev=[0x95d0x24c2], succ=[]
    =================================
    0x96d0x24c2: RETURNPRIVATE v24c2arg0, v24ca, v24c2arg0

}

function approve(address,uint256)() public {
    Begin block 0x267
    prev=[], succ=[0x279, 0x27d]
    =================================
    0x268: v268(0x3282) = CONST 
    0x26b: v26b(0x4) = CONST 
    0x26e: v26e = CALLDATASIZE 
    0x26f: v26f = SUB v26e, v26b(0x4)
    0x270: v270(0x40) = CONST 
    0x273: v273 = LT v26f, v270(0x40)
    0x274: v274 = ISZERO v273
    0x275: v275(0x27d) = CONST 
    0x278: JUMPI v275(0x27d), v274

    Begin block 0x279
    prev=[0x267], succ=[]
    =================================
    0x279: v279(0x0) = CONST 
    0x27c: REVERT v279(0x0), v279(0x0)

    Begin block 0x27d
    prev=[0x267], succ=[0x96e]
    =================================
    0x27f: v27f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x295: v295 = CALLDATALOAD v26b(0x4)
    0x296: v296 = AND v295, v27f(0xffffffffffffffffffffffffffffffffffffffff)
    0x298: v298(0x20) = CONST 
    0x29a: v29a(0x24) = ADD v298(0x20), v26b(0x4)
    0x29b: v29b = CALLDATALOAD v29a(0x24)
    0x29c: v29c(0x96e) = CONST 
    0x29f: JUMP v29c(0x96e)

    Begin block 0x96e
    prev=[0x27d], succ=[0x995, 0x9fb]
    =================================
    0x96f: v96f(0x1) = CONST 
    0x971: v971 = SLOAD v96f(0x1)
    0x972: v972(0x0) = CONST 
    0x975: v975(0x10000000000000000000000000000000000000000) = CONST 
    0x98c: v98c = DIV v971, v975(0x10000000000000000000000000000000000000000)
    0x98d: v98d(0xff) = CONST 
    0x98f: v98f = AND v98d(0xff), v98c
    0x990: v990 = ISZERO v98f
    0x991: v991(0x9fb) = CONST 
    0x994: JUMPI v991(0x9fb), v990

    Begin block 0x995
    prev=[0x96e], succ=[]
    =================================
    0x995: v995(0x40) = CONST 
    0x998: v998 = MLOAD v995(0x40)
    0x999: v999(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9bb: MSTORE v998, v999(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9bc: v9bc(0x20) = CONST 
    0x9be: v9be(0x4) = CONST 
    0x9c1: v9c1 = ADD v998, v9be(0x4)
    0x9c2: MSTORE v9c1, v9bc(0x20)
    0x9c3: v9c3(0x10) = CONST 
    0x9c5: v9c5(0x24) = CONST 
    0x9c8: v9c8 = ADD v998, v9c5(0x24)
    0x9c9: MSTORE v9c8, v9c3(0x10)
    0x9ca: v9ca(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0x9eb: v9eb(0x44) = CONST 
    0x9ee: v9ee = ADD v998, v9eb(0x44)
    0x9ef: MSTORE v9ee, v9ca(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x9f1: v9f1 = MLOAD v995(0x40)
    0x9f5: v9f5(0x0) = SUB v998, v9f1
    0x9f6: v9f6(0x64) = CONST 
    0x9f8: v9f8(0x64) = ADD v9f6(0x64), v9f5(0x0)
    0x9fa: REVERT v9f1, v9f8(0x64)

    Begin block 0x9fb
    prev=[0x96e], succ=[0xa14, 0xa64]
    =================================
    0x9fc: v9fc = CALLER 
    0x9fd: v9fd(0x0) = CONST 
    0xa01: MSTORE v9fd(0x0), v9fc
    0xa02: va02(0x3) = CONST 
    0xa04: va04(0x20) = CONST 
    0xa06: MSTORE va04(0x20), va02(0x3)
    0xa07: va07(0x40) = CONST 
    0xa0a: va0a = SHA3 v9fd(0x0), va07(0x40)
    0xa0b: va0b = SLOAD va0a
    0xa0c: va0c(0xff) = CONST 
    0xa0e: va0e = AND va0c(0xff), va0b
    0xa0f: va0f = ISZERO va0e
    0xa10: va10(0xa64) = CONST 
    0xa13: JUMPI va10(0xa64), va0f

    Begin block 0xa14
    prev=[0x9fb], succ=[]
    =================================
    0xa14: va14(0x40) = CONST 
    0xa16: va16 = MLOAD va14(0x40)
    0xa17: va17(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa39: MSTORE va16, va17(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa3a: va3a(0x4) = CONST 
    0xa3c: va3c = ADD va3a(0x4), va16
    0xa3f: va3f(0x20) = CONST 
    0xa41: va41 = ADD va3f(0x20), va3c
    0xa44: va44(0x20) = SUB va41, va3c
    0xa46: MSTORE va3c, va44(0x20)
    0xa47: va47(0x25) = CONST 
    0xa4a: MSTORE va41, va47(0x25)
    0xa4b: va4b(0x20) = CONST 
    0xa4d: va4d = ADD va4b(0x20), va41
    0xa4f: va4f(0x30f0) = CONST 
    0xa52: va52(0x25) = CONST 
    0xa55: CODECOPY va4d, va4f(0x30f0), va52(0x25)
    0xa56: va56(0x40) = CONST 
    0xa58: va58 = ADD va56(0x40), va4d
    0xa5c: va5c(0x40) = CONST 
    0xa5e: va5e = MLOAD va5c(0x40)
    0xa61: va61(0x84) = SUB va58, va5e
    0xa63: REVERT va5e, va61(0x84)

    Begin block 0xa64
    prev=[0x9fb], succ=[0xa95, 0xae5]
    =================================
    0xa65: va65(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa7b: va7b = AND v296, va65(0xffffffffffffffffffffffffffffffffffffffff)
    0xa7c: va7c(0x0) = CONST 
    0xa80: MSTORE va7c(0x0), va7b
    0xa81: va81(0x3) = CONST 
    0xa83: va83(0x20) = CONST 
    0xa85: MSTORE va83(0x20), va81(0x3)
    0xa86: va86(0x40) = CONST 
    0xa89: va89 = SHA3 va7c(0x0), va86(0x40)
    0xa8a: va8a = SLOAD va89
    0xa8d: va8d(0xff) = CONST 
    0xa8f: va8f = AND va8d(0xff), va8a
    0xa90: va90 = ISZERO va8f
    0xa91: va91(0xae5) = CONST 
    0xa94: JUMPI va91(0xae5), va90

    Begin block 0xa95
    prev=[0xa64], succ=[]
    =================================
    0xa95: va95(0x40) = CONST 
    0xa97: va97 = MLOAD va95(0x40)
    0xa98: va98(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xaba: MSTORE va97, va98(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xabb: vabb(0x4) = CONST 
    0xabd: vabd = ADD vabb(0x4), va97
    0xac0: vac0(0x20) = CONST 
    0xac2: vac2 = ADD vac0(0x20), vabd
    0xac5: vac5(0x20) = SUB vac2, vabd
    0xac7: MSTORE vabd, vac5(0x20)
    0xac8: vac8(0x25) = CONST 
    0xacb: MSTORE vac2, vac8(0x25)
    0xacc: vacc(0x20) = CONST 
    0xace: vace = ADD vacc(0x20), vac2
    0xad0: vad0(0x30f0) = CONST 
    0xad3: vad3(0x25) = CONST 
    0xad6: CODECOPY vace, vad0(0x30f0), vad3(0x25)
    0xad7: vad7(0x40) = CONST 
    0xad9: vad9 = ADD vad7(0x40), vace
    0xadd: vadd(0x40) = CONST 
    0xadf: vadf = MLOAD vadd(0x40)
    0xae2: vae2(0x84) = SUB vad9, vadf
    0xae4: REVERT vadf, vae2(0x84)

    Begin block 0xae5
    prev=[0xa64], succ=[0x27a0]
    =================================
    0xae6: vae6(0x37c9) = CONST 
    0xae9: vae9 = CALLER 
    0xaec: vaec(0x27a0) = CONST 
    0xaef: JUMP vaec(0x27a0)

    Begin block 0x27a0
    prev=[0xae5], succ=[0x27bc, 0x280c]
    =================================
    0x27a1: v27a1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27b7: v27b7 = AND vae9, v27a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x27b8: v27b8(0x280c) = CONST 
    0x27bb: JUMPI v27b8(0x280c), v27b7

    Begin block 0x27bc
    prev=[0x27a0], succ=[]
    =================================
    0x27bc: v27bc(0x40) = CONST 
    0x27be: v27be = MLOAD v27bc(0x40)
    0x27bf: v27bf(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x27e1: MSTORE v27be, v27bf(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x27e2: v27e2(0x4) = CONST 
    0x27e4: v27e4 = ADD v27e2(0x4), v27be
    0x27e7: v27e7(0x20) = CONST 
    0x27e9: v27e9 = ADD v27e7(0x20), v27e4
    0x27ec: v27ec(0x20) = SUB v27e9, v27e4
    0x27ee: MSTORE v27e4, v27ec(0x20)
    0x27ef: v27ef(0x24) = CONST 
    0x27f2: MSTORE v27e9, v27ef(0x24)
    0x27f3: v27f3(0x20) = CONST 
    0x27f5: v27f5 = ADD v27f3(0x20), v27e9
    0x27f7: v27f7(0x3022) = CONST 
    0x27fa: v27fa(0x24) = CONST 
    0x27fd: CODECOPY v27f5, v27f7(0x3022), v27fa(0x24)
    0x27fe: v27fe(0x40) = CONST 
    0x2800: v2800 = ADD v27fe(0x40), v27f5
    0x2804: v2804(0x40) = CONST 
    0x2806: v2806 = MLOAD v2804(0x40)
    0x2809: v2809(0x84) = SUB v2800, v2806
    0x280b: REVERT v2806, v2809(0x84)

    Begin block 0x280c
    prev=[0x27a0], succ=[0x2828, 0x2878]
    =================================
    0x280d: v280d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2823: v2823 = AND v296, v280d(0xffffffffffffffffffffffffffffffffffffffff)
    0x2824: v2824(0x2878) = CONST 
    0x2827: JUMPI v2824(0x2878), v2823

    Begin block 0x2828
    prev=[0x280c], succ=[]
    =================================
    0x2828: v2828(0x40) = CONST 
    0x282a: v282a = MLOAD v2828(0x40)
    0x282b: v282b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x284d: MSTORE v282a, v282b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x284e: v284e(0x4) = CONST 
    0x2850: v2850 = ADD v284e(0x4), v282a
    0x2853: v2853(0x20) = CONST 
    0x2855: v2855 = ADD v2853(0x20), v2850
    0x2858: v2858(0x20) = SUB v2855, v2850
    0x285a: MSTORE v2850, v2858(0x20)
    0x285b: v285b(0x22) = CONST 
    0x285e: MSTORE v2855, v285b(0x22)
    0x285f: v285f(0x20) = CONST 
    0x2861: v2861 = ADD v285f(0x20), v2855
    0x2863: v2863(0x2e18) = CONST 
    0x2866: v2866(0x22) = CONST 
    0x2869: CODECOPY v2861, v2863(0x2e18), v2866(0x22)
    0x286a: v286a(0x40) = CONST 
    0x286c: v286c = ADD v286a(0x40), v2861
    0x2870: v2870(0x40) = CONST 
    0x2872: v2872 = MLOAD v2870(0x40)
    0x2875: v2875(0x84) = SUB v286c, v2872
    0x2877: REVERT v2872, v2875(0x84)

    Begin block 0x2878
    prev=[0x280c], succ=[0x37c9]
    =================================
    0x2879: v2879(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2890: v2890 = AND vae9, v2879(0xffffffffffffffffffffffffffffffffffffffff)
    0x2891: v2891(0x0) = CONST 
    0x2895: MSTORE v2891(0x0), v2890
    0x2896: v2896(0xa) = CONST 
    0x2898: v2898(0x20) = CONST 
    0x289c: MSTORE v2898(0x20), v2896(0xa)
    0x289d: v289d(0x40) = CONST 
    0x28a1: v28a1 = SHA3 v2891(0x0), v289d(0x40)
    0x28a4: v28a4 = AND v296, v2879(0xffffffffffffffffffffffffffffffffffffffff)
    0x28a7: MSTORE v2891(0x0), v28a4
    0x28aa: MSTORE v2898(0x20), v28a1
    0x28ae: v28ae = SHA3 v2891(0x0), v289d(0x40)
    0x28b1: SSTORE v28ae, v29b
    0x28b3: v28b3 = MLOAD v289d(0x40)
    0x28b6: MSTORE v28b3, v29b
    0x28b8: v28b8 = MLOAD v289d(0x40)
    0x28b9: v28b9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925) = CONST 
    0x28dd: v28dd(0x0) = SUB v28b3, v28b8
    0x28e0: v28e0(0x20) = ADD v2898(0x20), v28dd(0x0)
    0x28e2: LOG3 v28b8, v28e0(0x20), v28b9(0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925), v2890, v28a4
    0x28e6: JUMP vae6(0x37c9)

    Begin block 0x37c9
    prev=[0x2878], succ=[0x3282]
    =================================
    0x37cb: v37cb(0x1) = CONST 
    0x37d3: JUMP v268(0x3282)

    Begin block 0x3282
    prev=[0x37c9], succ=[]
    =================================
    0x3283: v3283(0x40) = CONST 
    0x3286: v3286 = MLOAD v3283(0x40)
    0x3288: v3288 = ISZERO v37cb(0x1)
    0x3289: v3289 = ISZERO v3288
    0x328b: MSTORE v3286, v3289
    0x328c: v328c = MLOAD v3283(0x40)
    0x3290: v3290(0x0) = SUB v3286, v328c
    0x3291: v3291(0x20) = CONST 
    0x3293: v3293(0x20) = ADD v3291(0x20), v3290(0x0)
    0x3295: RETURN v328c, v3293(0x20)

}

function 0x28e7(0x28e7arg0x0, 0x28e7arg0x1, 0x28e7arg0x2, 0x28e7arg0x3) private {
    Begin block 0x28e7
    prev=[], succ=[0x2903, 0x2953]
    =================================
    0x28e8: v28e8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x28fe: v28fe = AND v28e7arg2, v28e8(0xffffffffffffffffffffffffffffffffffffffff)
    0x28ff: v28ff(0x2953) = CONST 
    0x2902: JUMPI v28ff(0x2953), v28fe

    Begin block 0x2903
    prev=[0x28e7], succ=[]
    =================================
    0x2903: v2903(0x40) = CONST 
    0x2905: v2905 = MLOAD v2903(0x40)
    0x2906: v2906(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2928: MSTORE v2905, v2906(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2929: v2929(0x4) = CONST 
    0x292b: v292b = ADD v2929(0x4), v2905
    0x292e: v292e(0x20) = CONST 
    0x2930: v2930 = ADD v292e(0x20), v292b
    0x2933: v2933(0x20) = SUB v2930, v292b
    0x2935: MSTORE v292b, v2933(0x20)
    0x2936: v2936(0x25) = CONST 
    0x2939: MSTORE v2930, v2936(0x25)
    0x293a: v293a(0x20) = CONST 
    0x293c: v293c = ADD v293a(0x20), v2930
    0x293e: v293e(0x2ffd) = CONST 
    0x2941: v2941(0x25) = CONST 
    0x2944: CODECOPY v293c, v293e(0x2ffd), v2941(0x25)
    0x2945: v2945(0x40) = CONST 
    0x2947: v2947 = ADD v2945(0x40), v293c
    0x294b: v294b(0x40) = CONST 
    0x294d: v294d = MLOAD v294b(0x40)
    0x2950: v2950(0x84) = SUB v2947, v294d
    0x2952: REVERT v294d, v2950(0x84)

    Begin block 0x2953
    prev=[0x28e7], succ=[0x296f, 0x29bf]
    =================================
    0x2954: v2954(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x296a: v296a = AND v28e7arg1, v2954(0xffffffffffffffffffffffffffffffffffffffff)
    0x296b: v296b(0x29bf) = CONST 
    0x296e: JUMPI v296b(0x29bf), v296a

    Begin block 0x296f
    prev=[0x2953], succ=[]
    =================================
    0x296f: v296f(0x40) = CONST 
    0x2971: v2971 = MLOAD v296f(0x40)
    0x2972: v2972(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2994: MSTORE v2971, v2972(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2995: v2995(0x4) = CONST 
    0x2997: v2997 = ADD v2995(0x4), v2971
    0x299a: v299a(0x20) = CONST 
    0x299c: v299c = ADD v299a(0x20), v2997
    0x299f: v299f(0x20) = SUB v299c, v2997
    0x29a1: MSTORE v2997, v299f(0x20)
    0x29a2: v29a2(0x23) = CONST 
    0x29a5: MSTORE v299c, v29a2(0x23)
    0x29a6: v29a6(0x20) = CONST 
    0x29a8: v29a8 = ADD v29a6(0x20), v299c
    0x29aa: v29aa(0x2d5b) = CONST 
    0x29ad: v29ad(0x23) = CONST 
    0x29b0: CODECOPY v29a8, v29aa(0x2d5b), v29ad(0x23)
    0x29b1: v29b1(0x40) = CONST 
    0x29b3: v29b3 = ADD v29b1(0x40), v29a8
    0x29b7: v29b7(0x40) = CONST 
    0x29b9: v29b9 = MLOAD v29b7(0x40)
    0x29bc: v29bc(0x84) = SUB v29b3, v29b9
    0x29be: REVERT v29b9, v29bc(0x84)

    Begin block 0x29bf
    prev=[0x2953], succ=[0x29ed, 0x2a3d]
    =================================
    0x29c0: v29c0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x29d6: v29d6 = AND v28e7arg2, v29c0(0xffffffffffffffffffffffffffffffffffffffff)
    0x29d7: v29d7(0x0) = CONST 
    0x29db: MSTORE v29d7(0x0), v29d6
    0x29dc: v29dc(0x9) = CONST 
    0x29de: v29de(0x20) = CONST 
    0x29e0: MSTORE v29de(0x20), v29dc(0x9)
    0x29e1: v29e1(0x40) = CONST 
    0x29e4: v29e4 = SHA3 v29d7(0x0), v29e1(0x40)
    0x29e5: v29e5 = SLOAD v29e4
    0x29e7: v29e7 = GT v28e7arg0, v29e5
    0x29e8: v29e8 = ISZERO v29e7
    0x29e9: v29e9(0x2a3d) = CONST 
    0x29ec: JUMPI v29e9(0x2a3d), v29e8

    Begin block 0x29ed
    prev=[0x29bf], succ=[]
    =================================
    0x29ed: v29ed(0x40) = CONST 
    0x29ef: v29ef = MLOAD v29ed(0x40)
    0x29f0: v29f0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a12: MSTORE v29ef, v29f0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a13: v2a13(0x4) = CONST 
    0x2a15: v2a15 = ADD v2a13(0x4), v29ef
    0x2a18: v2a18(0x20) = CONST 
    0x2a1a: v2a1a = ADD v2a18(0x20), v2a15
    0x2a1d: v2a1d(0x20) = SUB v2a1a, v2a15
    0x2a1f: MSTORE v2a15, v2a1d(0x20)
    0x2a20: v2a20(0x26) = CONST 
    0x2a23: MSTORE v2a1a, v2a20(0x26)
    0x2a24: v2a24(0x20) = CONST 
    0x2a26: v2a26 = ADD v2a24(0x20), v2a1a
    0x2a28: v2a28(0x2e8c) = CONST 
    0x2a2b: v2a2b(0x26) = CONST 
    0x2a2e: CODECOPY v2a26, v2a28(0x2e8c), v2a2b(0x26)
    0x2a2f: v2a2f(0x40) = CONST 
    0x2a31: v2a31 = ADD v2a2f(0x40), v2a26
    0x2a35: v2a35(0x40) = CONST 
    0x2a37: v2a37 = MLOAD v2a35(0x40)
    0x2a3a: v2a3a(0x84) = SUB v2a31, v2a37
    0x2a3c: REVERT v2a37, v2a3a(0x84)

    Begin block 0x2a3d
    prev=[0x29bf], succ=[0x2a6d]
    =================================
    0x2a3e: v2a3e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a54: v2a54 = AND v28e7arg2, v2a3e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a55: v2a55(0x0) = CONST 
    0x2a59: MSTORE v2a55(0x0), v2a54
    0x2a5a: v2a5a(0x9) = CONST 
    0x2a5c: v2a5c(0x20) = CONST 
    0x2a5e: MSTORE v2a5c(0x20), v2a5a(0x9)
    0x2a5f: v2a5f(0x40) = CONST 
    0x2a62: v2a62 = SHA3 v2a55(0x0), v2a5f(0x40)
    0x2a63: v2a63 = SLOAD v2a62
    0x2a64: v2a64(0x2a6d) = CONST 
    0x2a69: v2a69(0x2b12) = CONST 
    0x2a6c: v2a6c_0 = CALLPRIVATE v2a69(0x2b12), v28e7arg0, v2a63, v2a64(0x2a6d)

    Begin block 0x2a6d
    prev=[0x2a3d], succ=[0x2ba2B0x2a6d]
    =================================
    0x2a6e: v2a6e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a85: v2a85 = AND v28e7arg2, v2a6e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a86: v2a86(0x0) = CONST 
    0x2a8a: MSTORE v2a86(0x0), v2a85
    0x2a8b: v2a8b(0x9) = CONST 
    0x2a8d: v2a8d(0x20) = CONST 
    0x2a8f: MSTORE v2a8d(0x20), v2a8b(0x9)
    0x2a90: v2a90(0x40) = CONST 
    0x2a94: v2a94 = SHA3 v2a86(0x0), v2a90(0x40)
    0x2a98: SSTORE v2a94, v2a6c_0
    0x2a9b: v2a9b = AND v28e7arg1, v2a6e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a9d: MSTORE v2a86(0x0), v2a9b
    0x2a9e: v2a9e = SHA3 v2a86(0x0), v2a90(0x40)
    0x2a9f: v2a9f = SLOAD v2a9e
    0x2aa0: v2aa0(0x2aa9) = CONST 
    0x2aa5: v2aa5(0x2ba2) = CONST 
    0x2aa8: JUMP v2aa5(0x2ba2)

    Begin block 0x2ba2B0x2a6d
    prev=[0x2a6d], succ=[0x2bb0B0x2a6d, 0x38dfB0x2a6d]
    =================================
    0x2ba3S0x2a6d: v2ba3V2a6d(0x0) = CONST 
    0x2ba7S0x2a6d: v2ba7V2a6d = ADD v28e7arg0, v2a9f
    0x2baaS0x2a6d: v2baaV2a6d = LT v2ba7V2a6d, v2a9f
    0x2babS0x2a6d: v2babV2a6d = ISZERO v2baaV2a6d
    0x2bacS0x2a6d: v2bacV2a6d(0x38df) = CONST 
    0x2bafS0x2a6d: JUMPI v2bacV2a6d(0x38df), v2babV2a6d

    Begin block 0x2bb0B0x2a6d
    prev=[0x2ba2B0x2a6d], succ=[]
    =================================
    0x2bb0S0x2a6d: v2bb0V2a6d(0x40) = CONST 
    0x2bb3S0x2a6d: v2bb3V2a6d = MLOAD v2bb0V2a6d(0x40)
    0x2bb4S0x2a6d: v2bb4V2a6d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2bd6S0x2a6d: MSTORE v2bb3V2a6d, v2bb4V2a6d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2bd7S0x2a6d: v2bd7V2a6d(0x20) = CONST 
    0x2bd9S0x2a6d: v2bd9V2a6d(0x4) = CONST 
    0x2bdcS0x2a6d: v2bdcV2a6d = ADD v2bb3V2a6d, v2bd9V2a6d(0x4)
    0x2bddS0x2a6d: MSTORE v2bdcV2a6d, v2bd7V2a6d(0x20)
    0x2bdeS0x2a6d: v2bdeV2a6d(0x1b) = CONST 
    0x2be0S0x2a6d: v2be0V2a6d(0x24) = CONST 
    0x2be3S0x2a6d: v2be3V2a6d = ADD v2bb3V2a6d, v2be0V2a6d(0x24)
    0x2be4S0x2a6d: MSTORE v2be3V2a6d, v2bdeV2a6d(0x1b)
    0x2be5S0x2a6d: v2be5V2a6d(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2c06S0x2a6d: v2c06V2a6d(0x44) = CONST 
    0x2c09S0x2a6d: v2c09V2a6d = ADD v2bb3V2a6d, v2c06V2a6d(0x44)
    0x2c0aS0x2a6d: MSTORE v2c09V2a6d, v2be5V2a6d(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2c0cS0x2a6d: v2c0cV2a6d = MLOAD v2bb0V2a6d(0x40)
    0x2c10S0x2a6d: v2c10V2a6d(0x0) = SUB v2bb3V2a6d, v2c0cV2a6d
    0x2c11S0x2a6d: v2c11V2a6d(0x64) = CONST 
    0x2c13S0x2a6d: v2c13V2a6d(0x64) = ADD v2c11V2a6d(0x64), v2c10V2a6d(0x0)
    0x2c15S0x2a6d: REVERT v2c0cV2a6d, v2c13V2a6d(0x64)

    Begin block 0x38dfB0x2a6d
    prev=[0x2ba2B0x2a6d], succ=[0x2aa9]
    =================================
    0x38e5S0x2a6d: JUMP v2aa0(0x2aa9)

    Begin block 0x2aa9
    prev=[0x38dfB0x2a6d], succ=[]
    =================================
    0x2aaa: v2aaa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ac1: v2ac1 = AND v28e7arg1, v2aaa(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ac2: v2ac2(0x0) = CONST 
    0x2ac6: MSTORE v2ac2(0x0), v2ac1
    0x2ac7: v2ac7(0x9) = CONST 
    0x2ac9: v2ac9(0x20) = CONST 
    0x2acd: MSTORE v2ac9(0x20), v2ac7(0x9)
    0x2ace: v2ace(0x40) = CONST 
    0x2ad3: v2ad3 = SHA3 v2ac2(0x0), v2ace(0x40)
    0x2ad7: SSTORE v2ad3, v2ba7V2a6d
    0x2ad9: v2ad9 = MLOAD v2ace(0x40)
    0x2adc: MSTORE v2ad9, v28e7arg0
    0x2ade: v2ade = MLOAD v2ace(0x40)
    0x2ae3: v2ae3 = AND v28e7arg2, v2aaa(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ae5: v2ae5(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x2b0a: v2b0a(0x0) = SUB v2ad9, v2ade
    0x2b0b: v2b0b(0x20) = ADD v2b0a(0x0), v2ac9(0x20)
    0x2b0d: LOG3 v2ade, v2b0b(0x20), v2ae5(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v2ae3, v2ac1
    0x2b11: RETURNPRIVATE v28e7arg3

}

function 0x2b12(0x2b12arg0x0, 0x2b12arg0x1, 0x2b12arg0x2) private {
    Begin block 0x2b12
    prev=[], succ=[0x2c16]
    =================================
    0x2b13: v2b13(0x0) = CONST 
    0x2b15: v2b15(0x38b9) = CONST 
    0x2b1a: v2b1a(0x40) = CONST 
    0x2b1c: v2b1c = MLOAD v2b1a(0x40)
    0x2b1e: v2b1e(0x40) = CONST 
    0x2b20: v2b20 = ADD v2b1e(0x40), v2b1c
    0x2b21: v2b21(0x40) = CONST 
    0x2b23: MSTORE v2b21(0x40), v2b20
    0x2b25: v2b25(0x1e) = CONST 
    0x2b28: MSTORE v2b1c, v2b25(0x1e)
    0x2b29: v2b29(0x20) = CONST 
    0x2b2b: v2b2b = ADD v2b29(0x20), v2b1c
    0x2b2c: v2b2c(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x2b4e: MSTORE v2b2b, v2b2c(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x2b50: v2b50(0x2c16) = CONST 
    0x2b53: JUMP v2b50(0x2c16)

    Begin block 0x2c16
    prev=[0x2b12], succ=[0x2c22, 0x2cbf]
    =================================
    0x2c17: v2c17(0x0) = CONST 
    0x2c1c: v2c1c = GT v2b12arg0, v2b12arg1
    0x2c1d: v2c1d = ISZERO v2c1c
    0x2c1e: v2c1e(0x2cbf) = CONST 
    0x2c21: JUMPI v2c1e(0x2cbf), v2c1d

    Begin block 0x2c22
    prev=[0x2c16], succ=[0x2c6c]
    =================================
    0x2c22: v2c22(0x40) = CONST 
    0x2c24: v2c24 = MLOAD v2c22(0x40)
    0x2c25: v2c25(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2c47: MSTORE v2c24, v2c25(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2c48: v2c48(0x4) = CONST 
    0x2c4a: v2c4a = ADD v2c48(0x4), v2c24
    0x2c4d: v2c4d(0x20) = CONST 
    0x2c4f: v2c4f = ADD v2c4d(0x20), v2c4a
    0x2c52: v2c52(0x20) = SUB v2c4f, v2c4a
    0x2c54: MSTORE v2c4a, v2c52(0x20)
    0x2c58: v2c58(0x1e) = MLOAD v2b1c
    0x2c5a: MSTORE v2c4f, v2c58(0x1e)
    0x2c5b: v2c5b(0x20) = CONST 
    0x2c5d: v2c5d = ADD v2c5b(0x20), v2c4f
    0x2c61: v2c61(0x1e) = MLOAD v2b1c
    0x2c63: v2c63(0x20) = CONST 
    0x2c65: v2c65 = ADD v2c63(0x20), v2b1c
    0x2c6a: v2c6a(0x0) = CONST 

    Begin block 0x2c6c
    prev=[0x2c22, 0x2c75], succ=[0x2c84, 0x2c75]
    =================================
    0x2c6c_0x0: v2c6c_0 = PHI v2c6a(0x0), v2c7f
    0x2c6f: v2c6f = LT v2c6c_0, v2c61(0x1e)
    0x2c70: v2c70 = ISZERO v2c6f
    0x2c71: v2c71(0x2c84) = CONST 
    0x2c74: JUMPI v2c71(0x2c84), v2c70

    Begin block 0x2c84
    prev=[0x2c6c], succ=[0x2cb1, 0x2c98]
    =================================
    0x2c8d: v2c8d = ADD v2c61(0x1e), v2c5d
    0x2c8f: v2c8f(0x1f) = CONST 
    0x2c91: v2c91(0x1e) = AND v2c8f(0x1f), v2c61(0x1e)
    0x2c93: v2c93 = ISZERO v2c91(0x1e)
    0x2c94: v2c94(0x2cb1) = CONST 
    0x2c97: JUMPI v2c94(0x2cb1), v2c93

    Begin block 0x2cb1
    prev=[0x2c84, 0x2c98], succ=[]
    =================================
    0x2cb1_0x1: v2cb1_1 = PHI v2c8d, v2cae
    0x2cb7: v2cb7(0x40) = CONST 
    0x2cb9: v2cb9 = MLOAD v2cb7(0x40)
    0x2cbc: v2cbc = SUB v2cb1_1, v2cb9
    0x2cbe: REVERT v2cb9, v2cbc

    Begin block 0x2c98
    prev=[0x2c84], succ=[0x2cb1]
    =================================
    0x2c9a: v2c9a = SUB v2c8d, v2c91(0x1e)
    0x2c9c: v2c9c = MLOAD v2c9a
    0x2c9d: v2c9d(0x1) = CONST 
    0x2ca0: v2ca0(0x20) = CONST 
    0x2ca2: v2ca2(0x2) = SUB v2ca0(0x20), v2c91(0x1e)
    0x2ca3: v2ca3(0x100) = CONST 
    0x2ca6: v2ca6(0x10000) = EXP v2ca3(0x100), v2ca2(0x2)
    0x2ca7: v2ca7(0xffff) = SUB v2ca6(0x10000), v2c9d(0x1)
    0x2ca8: v2ca8 = NOT v2ca7(0xffff)
    0x2ca9: v2ca9 = AND v2ca8, v2c9c
    0x2cab: MSTORE v2c9a, v2ca9
    0x2cac: v2cac(0x20) = CONST 
    0x2cae: v2cae = ADD v2cac(0x20), v2c9a

    Begin block 0x2c75
    prev=[0x2c6c], succ=[0x2c6c]
    =================================
    0x2c75_0x0: v2c75_0 = PHI v2c6a(0x0), v2c7f
    0x2c77: v2c77 = ADD v2c75_0, v2c65
    0x2c78: v2c78 = MLOAD v2c77
    0x2c7b: v2c7b = ADD v2c75_0, v2c5d
    0x2c7c: MSTORE v2c7b, v2c78
    0x2c7d: v2c7d(0x20) = CONST 
    0x2c7f: v2c7f = ADD v2c7d(0x20), v2c75_0
    0x2c80: v2c80(0x2c6c) = CONST 
    0x2c83: JUMP v2c80(0x2c6c)

    Begin block 0x2cbf
    prev=[0x2c16], succ=[0x38b9]
    =================================
    0x2cc4: v2cc4 = SUB v2b12arg1, v2b12arg0
    0x2cc6: JUMP v2b15(0x38b9)

    Begin block 0x38b9
    prev=[0x2cbf], succ=[]
    =================================
    0x38bf: RETURNPRIVATE v2b12arg2, v2cc4

}

function totalSupply()() public {
    Begin block 0x2b4
    prev=[], succ=[0xafb]
    =================================
    0x2b5: v2b5(0x32b5) = CONST 
    0x2b8: v2b8(0xafb) = CONST 
    0x2bb: JUMP v2b8(0xafb)

    Begin block 0xafb
    prev=[0x2b4], succ=[0x32b5]
    =================================
    0xafc: vafc(0xb) = CONST 
    0xafe: vafe = SLOAD vafc(0xb)
    0xb00: JUMP v2b5(0x32b5)

    Begin block 0x32b5
    prev=[0xafb], succ=[]
    =================================
    0x32b6: v32b6(0x40) = CONST 
    0x32b9: v32b9 = MLOAD v32b6(0x40)
    0x32bc: MSTORE v32b9, vafe
    0x32bd: v32bd = MLOAD v32b6(0x40)
    0x32c1: v32c1(0x0) = SUB v32b9, v32bd
    0x32c2: v32c2(0x20) = CONST 
    0x32c4: v32c4(0x20) = ADD v32c2(0x20), v32c1(0x0)
    0x32c6: RETURN v32bd, v32c4(0x20)

}

function unBlacklist(address)() public {
    Begin block 0x2ce
    prev=[], succ=[0x2e0, 0x2e4]
    =================================
    0x2cf: v2cf(0x32e6) = CONST 
    0x2d2: v2d2(0x4) = CONST 
    0x2d5: v2d5 = CALLDATASIZE 
    0x2d6: v2d6 = SUB v2d5, v2d2(0x4)
    0x2d7: v2d7(0x20) = CONST 
    0x2da: v2da = LT v2d6, v2d7(0x20)
    0x2db: v2db = ISZERO v2da
    0x2dc: v2dc(0x2e4) = CONST 
    0x2df: JUMPI v2dc(0x2e4), v2db

    Begin block 0x2e0
    prev=[0x2ce], succ=[]
    =================================
    0x2e0: v2e0(0x0) = CONST 
    0x2e3: REVERT v2e0(0x0), v2e0(0x0)

    Begin block 0x2e4
    prev=[0x2ce], succ=[0xb01]
    =================================
    0x2e6: v2e6 = CALLDATALOAD v2d2(0x4)
    0x2e7: v2e7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fc: v2fc = AND v2e7(0xffffffffffffffffffffffffffffffffffffffff), v2e6
    0x2fd: v2fd(0xb01) = CONST 
    0x300: JUMP v2fd(0xb01)

    Begin block 0xb01
    prev=[0x2e4], succ=[0xb21, 0xb71]
    =================================
    0xb02: vb02(0x2) = CONST 
    0xb04: vb04 = SLOAD vb02(0x2)
    0xb05: vb05(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb1a: vb1a = AND vb05(0xffffffffffffffffffffffffffffffffffffffff), vb04
    0xb1b: vb1b = CALLER 
    0xb1c: vb1c = EQ vb1b, vb1a
    0xb1d: vb1d(0xb71) = CONST 
    0xb20: JUMPI vb1d(0xb71), vb1c

    Begin block 0xb21
    prev=[0xb01], succ=[]
    =================================
    0xb21: vb21(0x40) = CONST 
    0xb23: vb23 = MLOAD vb21(0x40)
    0xb24: vb24(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xb46: MSTORE vb23, vb24(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb47: vb47(0x4) = CONST 
    0xb49: vb49 = ADD vb47(0x4), vb23
    0xb4c: vb4c(0x20) = CONST 
    0xb4e: vb4e = ADD vb4c(0x20), vb49
    0xb51: vb51(0x20) = SUB vb4e, vb49
    0xb53: MSTORE vb49, vb51(0x20)
    0xb54: vb54(0x2c) = CONST 
    0xb57: MSTORE vb4e, vb54(0x2c)
    0xb58: vb58(0x20) = CONST 
    0xb5a: vb5a = ADD vb58(0x20), vb4e
    0xb5c: vb5c(0x2edb) = CONST 
    0xb5f: vb5f(0x2c) = CONST 
    0xb62: CODECOPY vb5a, vb5c(0x2edb), vb5f(0x2c)
    0xb63: vb63(0x40) = CONST 
    0xb65: vb65 = ADD vb63(0x40), vb5a
    0xb69: vb69(0x40) = CONST 
    0xb6b: vb6b = MLOAD vb69(0x40)
    0xb6e: vb6e(0x84) = SUB vb65, vb6b
    0xb70: REVERT vb6b, vb6e(0x84)

    Begin block 0xb71
    prev=[0xb01], succ=[0x32e6]
    =================================
    0xb72: vb72(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb88: vb88 = AND v2fc, vb72(0xffffffffffffffffffffffffffffffffffffffff)
    0xb89: vb89(0x0) = CONST 
    0xb8d: MSTORE vb89(0x0), vb88
    0xb8e: vb8e(0x3) = CONST 
    0xb90: vb90(0x20) = CONST 
    0xb92: MSTORE vb90(0x20), vb8e(0x3)
    0xb93: vb93(0x40) = CONST 
    0xb97: vb97 = SHA3 vb89(0x0), vb93(0x40)
    0xb99: vb99 = SLOAD vb97
    0xb9a: vb9a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0xbbb: vbbb = AND vb9a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vb99
    0xbbd: SSTORE vb97, vbbb
    0xbbe: vbbe = MLOAD vb93(0x40)
    0xbbf: vbbf(0x117e3210bb9aa7d9baff172026820255c6f6c30ba8999d1c2fd88e2848137c4e) = CONST 
    0xbe2: LOG2 vbbe, vb89(0x0), vbbf(0x117e3210bb9aa7d9baff172026820255c6f6c30ba8999d1c2fd88e2848137c4e), vb88
    0xbe4: JUMP v2cf(0x32e6)

    Begin block 0x32e6
    prev=[0xb71], succ=[]
    =================================
    0x32e7: STOP 

}

function transferFrom(address,address,uint256)() public {
    Begin block 0x303
    prev=[], succ=[0x315, 0x319]
    =================================
    0x304: v304(0x3307) = CONST 
    0x307: v307(0x4) = CONST 
    0x30a: v30a = CALLDATASIZE 
    0x30b: v30b = SUB v30a, v307(0x4)
    0x30c: v30c(0x60) = CONST 
    0x30f: v30f = LT v30b, v30c(0x60)
    0x310: v310 = ISZERO v30f
    0x311: v311(0x319) = CONST 
    0x314: JUMPI v311(0x319), v310

    Begin block 0x315
    prev=[0x303], succ=[]
    =================================
    0x315: v315(0x0) = CONST 
    0x318: REVERT v315(0x0), v315(0x0)

    Begin block 0x319
    prev=[0x303], succ=[0xbe5]
    =================================
    0x31b: v31b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x331: v331 = CALLDATALOAD v307(0x4)
    0x333: v333 = AND v31b(0xffffffffffffffffffffffffffffffffffffffff), v331
    0x335: v335(0x20) = CONST 
    0x338: v338(0x24) = ADD v307(0x4), v335(0x20)
    0x339: v339 = CALLDATALOAD v338(0x24)
    0x33c: v33c = AND v31b(0xffffffffffffffffffffffffffffffffffffffff), v339
    0x33e: v33e(0x40) = CONST 
    0x340: v340(0x44) = ADD v33e(0x40), v307(0x4)
    0x341: v341 = CALLDATALOAD v340(0x44)
    0x342: v342(0xbe5) = CONST 
    0x345: JUMP v342(0xbe5)

    Begin block 0xbe5
    prev=[0x319], succ=[0xc0c, 0xc72]
    =================================
    0xbe6: vbe6(0x1) = CONST 
    0xbe8: vbe8 = SLOAD vbe6(0x1)
    0xbe9: vbe9(0x0) = CONST 
    0xbec: vbec(0x10000000000000000000000000000000000000000) = CONST 
    0xc03: vc03 = DIV vbe8, vbec(0x10000000000000000000000000000000000000000)
    0xc04: vc04(0xff) = CONST 
    0xc06: vc06 = AND vc04(0xff), vc03
    0xc07: vc07 = ISZERO vc06
    0xc08: vc08(0xc72) = CONST 
    0xc0b: JUMPI vc08(0xc72), vc07

    Begin block 0xc0c
    prev=[0xbe5], succ=[]
    =================================
    0xc0c: vc0c(0x40) = CONST 
    0xc0f: vc0f = MLOAD vc0c(0x40)
    0xc10: vc10(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xc32: MSTORE vc0f, vc10(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc33: vc33(0x20) = CONST 
    0xc35: vc35(0x4) = CONST 
    0xc38: vc38 = ADD vc0f, vc35(0x4)
    0xc39: MSTORE vc38, vc33(0x20)
    0xc3a: vc3a(0x10) = CONST 
    0xc3c: vc3c(0x24) = CONST 
    0xc3f: vc3f = ADD vc0f, vc3c(0x24)
    0xc40: MSTORE vc3f, vc3a(0x10)
    0xc41: vc41(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0xc62: vc62(0x44) = CONST 
    0xc65: vc65 = ADD vc0f, vc62(0x44)
    0xc66: MSTORE vc65, vc41(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0xc68: vc68 = MLOAD vc0c(0x40)
    0xc6c: vc6c(0x0) = SUB vc0f, vc68
    0xc6d: vc6d(0x64) = CONST 
    0xc6f: vc6f(0x64) = ADD vc6d(0x64), vc6c(0x0)
    0xc71: REVERT vc68, vc6f(0x64)

    Begin block 0xc72
    prev=[0xbe5], succ=[0xc8b, 0xcdb]
    =================================
    0xc73: vc73 = CALLER 
    0xc74: vc74(0x0) = CONST 
    0xc78: MSTORE vc74(0x0), vc73
    0xc79: vc79(0x3) = CONST 
    0xc7b: vc7b(0x20) = CONST 
    0xc7d: MSTORE vc7b(0x20), vc79(0x3)
    0xc7e: vc7e(0x40) = CONST 
    0xc81: vc81 = SHA3 vc74(0x0), vc7e(0x40)
    0xc82: vc82 = SLOAD vc81
    0xc83: vc83(0xff) = CONST 
    0xc85: vc85 = AND vc83(0xff), vc82
    0xc86: vc86 = ISZERO vc85
    0xc87: vc87(0xcdb) = CONST 
    0xc8a: JUMPI vc87(0xcdb), vc86

    Begin block 0xc8b
    prev=[0xc72], succ=[]
    =================================
    0xc8b: vc8b(0x40) = CONST 
    0xc8d: vc8d = MLOAD vc8b(0x40)
    0xc8e: vc8e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xcb0: MSTORE vc8d, vc8e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xcb1: vcb1(0x4) = CONST 
    0xcb3: vcb3 = ADD vcb1(0x4), vc8d
    0xcb6: vcb6(0x20) = CONST 
    0xcb8: vcb8 = ADD vcb6(0x20), vcb3
    0xcbb: vcbb(0x20) = SUB vcb8, vcb3
    0xcbd: MSTORE vcb3, vcbb(0x20)
    0xcbe: vcbe(0x25) = CONST 
    0xcc1: MSTORE vcb8, vcbe(0x25)
    0xcc2: vcc2(0x20) = CONST 
    0xcc4: vcc4 = ADD vcc2(0x20), vcb8
    0xcc6: vcc6(0x30f0) = CONST 
    0xcc9: vcc9(0x25) = CONST 
    0xccc: CODECOPY vcc4, vcc6(0x30f0), vcc9(0x25)
    0xccd: vccd(0x40) = CONST 
    0xccf: vccf = ADD vccd(0x40), vcc4
    0xcd3: vcd3(0x40) = CONST 
    0xcd5: vcd5 = MLOAD vcd3(0x40)
    0xcd8: vcd8(0x84) = SUB vccf, vcd5
    0xcda: REVERT vcd5, vcd8(0x84)

    Begin block 0xcdb
    prev=[0xc72], succ=[0xd0c, 0xd5c]
    =================================
    0xcdc: vcdc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xcf2: vcf2 = AND v333, vcdc(0xffffffffffffffffffffffffffffffffffffffff)
    0xcf3: vcf3(0x0) = CONST 
    0xcf7: MSTORE vcf3(0x0), vcf2
    0xcf8: vcf8(0x3) = CONST 
    0xcfa: vcfa(0x20) = CONST 
    0xcfc: MSTORE vcfa(0x20), vcf8(0x3)
    0xcfd: vcfd(0x40) = CONST 
    0xd00: vd00 = SHA3 vcf3(0x0), vcfd(0x40)
    0xd01: vd01 = SLOAD vd00
    0xd04: vd04(0xff) = CONST 
    0xd06: vd06 = AND vd04(0xff), vd01
    0xd07: vd07 = ISZERO vd06
    0xd08: vd08(0xd5c) = CONST 
    0xd0b: JUMPI vd08(0xd5c), vd07

    Begin block 0xd0c
    prev=[0xcdb], succ=[]
    =================================
    0xd0c: vd0c(0x40) = CONST 
    0xd0e: vd0e = MLOAD vd0c(0x40)
    0xd0f: vd0f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xd31: MSTORE vd0e, vd0f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd32: vd32(0x4) = CONST 
    0xd34: vd34 = ADD vd32(0x4), vd0e
    0xd37: vd37(0x20) = CONST 
    0xd39: vd39 = ADD vd37(0x20), vd34
    0xd3c: vd3c(0x20) = SUB vd39, vd34
    0xd3e: MSTORE vd34, vd3c(0x20)
    0xd3f: vd3f(0x25) = CONST 
    0xd42: MSTORE vd39, vd3f(0x25)
    0xd43: vd43(0x20) = CONST 
    0xd45: vd45 = ADD vd43(0x20), vd39
    0xd47: vd47(0x30f0) = CONST 
    0xd4a: vd4a(0x25) = CONST 
    0xd4d: CODECOPY vd45, vd47(0x30f0), vd4a(0x25)
    0xd4e: vd4e(0x40) = CONST 
    0xd50: vd50 = ADD vd4e(0x40), vd45
    0xd54: vd54(0x40) = CONST 
    0xd56: vd56 = MLOAD vd54(0x40)
    0xd59: vd59(0x84) = SUB vd50, vd56
    0xd5b: REVERT vd56, vd59(0x84)

    Begin block 0xd5c
    prev=[0xcdb], succ=[0xd8d, 0xddd]
    =================================
    0xd5d: vd5d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd73: vd73 = AND v33c, vd5d(0xffffffffffffffffffffffffffffffffffffffff)
    0xd74: vd74(0x0) = CONST 
    0xd78: MSTORE vd74(0x0), vd73
    0xd79: vd79(0x3) = CONST 
    0xd7b: vd7b(0x20) = CONST 
    0xd7d: MSTORE vd7b(0x20), vd79(0x3)
    0xd7e: vd7e(0x40) = CONST 
    0xd81: vd81 = SHA3 vd74(0x0), vd7e(0x40)
    0xd82: vd82 = SLOAD vd81
    0xd85: vd85(0xff) = CONST 
    0xd87: vd87 = AND vd85(0xff), vd82
    0xd88: vd88 = ISZERO vd87
    0xd89: vd89(0xddd) = CONST 
    0xd8c: JUMPI vd89(0xddd), vd88

    Begin block 0xd8d
    prev=[0xd5c], succ=[]
    =================================
    0xd8d: vd8d(0x40) = CONST 
    0xd8f: vd8f = MLOAD vd8d(0x40)
    0xd90: vd90(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xdb2: MSTORE vd8f, vd90(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xdb3: vdb3(0x4) = CONST 
    0xdb5: vdb5 = ADD vdb3(0x4), vd8f
    0xdb8: vdb8(0x20) = CONST 
    0xdba: vdba = ADD vdb8(0x20), vdb5
    0xdbd: vdbd(0x20) = SUB vdba, vdb5
    0xdbf: MSTORE vdb5, vdbd(0x20)
    0xdc0: vdc0(0x25) = CONST 
    0xdc3: MSTORE vdba, vdc0(0x25)
    0xdc4: vdc4(0x20) = CONST 
    0xdc6: vdc6 = ADD vdc4(0x20), vdba
    0xdc8: vdc8(0x30f0) = CONST 
    0xdcb: vdcb(0x25) = CONST 
    0xdce: CODECOPY vdc6, vdc8(0x30f0), vdcb(0x25)
    0xdcf: vdcf(0x40) = CONST 
    0xdd1: vdd1 = ADD vdcf(0x40), vdc6
    0xdd5: vdd5(0x40) = CONST 
    0xdd7: vdd7 = MLOAD vdd5(0x40)
    0xdda: vdda(0x84) = SUB vdd1, vdd7
    0xddc: REVERT vdd7, vdda(0x84)

    Begin block 0xddd
    prev=[0xd5c], succ=[0xe16, 0xe66]
    =================================
    0xdde: vdde(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdf4: vdf4 = AND v333, vdde(0xffffffffffffffffffffffffffffffffffffffff)
    0xdf5: vdf5(0x0) = CONST 
    0xdf9: MSTORE vdf5(0x0), vdf4
    0xdfa: vdfa(0xa) = CONST 
    0xdfc: vdfc(0x20) = CONST 
    0xe00: MSTORE vdfc(0x20), vdfa(0xa)
    0xe01: ve01(0x40) = CONST 
    0xe05: ve05 = SHA3 vdf5(0x0), ve01(0x40)
    0xe06: ve06 = CALLER 
    0xe08: MSTORE vdf5(0x0), ve06
    0xe0b: MSTORE vdfc(0x20), ve05
    0xe0d: ve0d = SHA3 vdf5(0x0), ve01(0x40)
    0xe0e: ve0e = SLOAD ve0d
    0xe10: ve10 = GT v341, ve0e
    0xe11: ve11 = ISZERO ve10
    0xe12: ve12(0xe66) = CONST 
    0xe15: JUMPI ve12(0xe66), ve11

    Begin block 0xe16
    prev=[0xddd], succ=[]
    =================================
    0xe16: ve16(0x40) = CONST 
    0xe18: ve18 = MLOAD ve16(0x40)
    0xe19: ve19(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xe3b: MSTORE ve18, ve19(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe3c: ve3c(0x4) = CONST 
    0xe3e: ve3e = ADD ve3c(0x4), ve18
    0xe41: ve41(0x20) = CONST 
    0xe43: ve43 = ADD ve41(0x20), ve3e
    0xe46: ve46(0x20) = SUB ve43, ve3e
    0xe48: MSTORE ve3e, ve46(0x20)
    0xe49: ve49(0x28) = CONST 
    0xe4c: MSTORE ve43, ve49(0x28)
    0xe4d: ve4d(0x20) = CONST 
    0xe4f: ve4f = ADD ve4d(0x20), ve43
    0xe51: ve51(0x2f7d) = CONST 
    0xe54: ve54(0x28) = CONST 
    0xe57: CODECOPY ve4f, ve51(0x2f7d), ve54(0x28)
    0xe58: ve58(0x40) = CONST 
    0xe5a: ve5a = ADD ve58(0x40), ve4f
    0xe5e: ve5e(0x40) = CONST 
    0xe60: ve60 = MLOAD ve5e(0x40)
    0xe63: ve63(0x84) = SUB ve5a, ve60
    0xe65: REVERT ve60, ve63(0x84)

    Begin block 0xe66
    prev=[0xddd], succ=[0xe71]
    =================================
    0xe67: ve67(0xe71) = CONST 
    0xe6d: ve6d(0x28e7) = CONST 
    0xe70: CALLPRIVATE ve6d(0x28e7), v341, v33c, v333, ve67(0xe71)

    Begin block 0xe71
    prev=[0xe66], succ=[0xeac]
    =================================
    0xe72: ve72(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe88: ve88 = AND v333, ve72(0xffffffffffffffffffffffffffffffffffffffff)
    0xe89: ve89(0x0) = CONST 
    0xe8d: MSTORE ve89(0x0), ve88
    0xe8e: ve8e(0xa) = CONST 
    0xe90: ve90(0x20) = CONST 
    0xe94: MSTORE ve90(0x20), ve8e(0xa)
    0xe95: ve95(0x40) = CONST 
    0xe99: ve99 = SHA3 ve89(0x0), ve95(0x40)
    0xe9a: ve9a = CALLER 
    0xe9c: MSTORE ve89(0x0), ve9a
    0xe9f: MSTORE ve90(0x20), ve99
    0xea1: vea1 = SHA3 ve89(0x0), ve95(0x40)
    0xea2: vea2 = SLOAD vea1
    0xea3: vea3(0xeac) = CONST 
    0xea8: vea8(0x2b12) = CONST 
    0xeab: veab_0 = CALLPRIVATE vea8(0x2b12), v341, vea2, vea3(0xeac)

    Begin block 0xeac
    prev=[0xe71], succ=[0x3307]
    =================================
    0xead: vead(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xec3: vec3 = AND v333, vead(0xffffffffffffffffffffffffffffffffffffffff)
    0xec4: vec4(0x0) = CONST 
    0xec8: MSTORE vec4(0x0), vec3
    0xec9: vec9(0xa) = CONST 
    0xecb: vecb(0x20) = CONST 
    0xecf: MSTORE vecb(0x20), vec9(0xa)
    0xed0: ved0(0x40) = CONST 
    0xed4: ved4 = SHA3 vec4(0x0), ved0(0x40)
    0xed5: ved5 = CALLER 
    0xed7: MSTORE vec4(0x0), ved5
    0xeda: MSTORE vecb(0x20), ved4
    0xedc: vedc = SHA3 vec4(0x0), ved0(0x40)
    0xedd: SSTORE vedc, veab_0
    0xede: vede(0x1) = CONST 
    0xeea: JUMP v304(0x3307)

    Begin block 0x3307
    prev=[0xeac], succ=[]
    =================================
    0x3308: v3308(0x40) = CONST 
    0x330b: v330b = MLOAD v3308(0x40)
    0x330d: v330d = ISZERO vede(0x1)
    0x330e: v330e = ISZERO v330d
    0x3310: MSTORE v330b, v330e
    0x3311: v3311 = MLOAD v3308(0x40)
    0x3315: v3315(0x0) = SUB v330b, v3311
    0x3316: v3316(0x20) = CONST 
    0x3318: v3318(0x20) = ADD v3316(0x20), v3315(0x0)
    0x331a: RETURN v3311, v3318(0x20)

}

function fallback()() public {
    Begin block 0x3162
    prev=[], succ=[]
    =================================
    0x3163: v3163(0x0) = CONST 
    0x3166: REVERT v3163(0x0), v3163(0x0)

}

function removeMinter(address)() public {
    Begin block 0x346
    prev=[], succ=[0x358, 0x35c]
    =================================
    0x347: v347(0x333a) = CONST 
    0x34a: v34a(0x4) = CONST 
    0x34d: v34d = CALLDATASIZE 
    0x34e: v34e = SUB v34d, v34a(0x4)
    0x34f: v34f(0x20) = CONST 
    0x352: v352 = LT v34e, v34f(0x20)
    0x353: v353 = ISZERO v352
    0x354: v354(0x35c) = CONST 
    0x357: JUMPI v354(0x35c), v353

    Begin block 0x358
    prev=[0x346], succ=[]
    =================================
    0x358: v358(0x0) = CONST 
    0x35b: REVERT v358(0x0), v358(0x0)

    Begin block 0x35c
    prev=[0x346], succ=[0xeeb]
    =================================
    0x35e: v35e = CALLDATALOAD v34a(0x4)
    0x35f: v35f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x374: v374 = AND v35f(0xffffffffffffffffffffffffffffffffffffffff), v35e
    0x375: v375(0xeeb) = CONST 
    0x378: JUMP v375(0xeeb)

    Begin block 0xeeb
    prev=[0x35c], succ=[0xf0e, 0xf5e]
    =================================
    0xeec: veec(0x8) = CONST 
    0xeee: veee = SLOAD veec(0x8)
    0xeef: veef(0x0) = CONST 
    0xef2: vef2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf07: vf07 = AND vef2(0xffffffffffffffffffffffffffffffffffffffff), veee
    0xf08: vf08 = CALLER 
    0xf09: vf09 = EQ vf08, vf07
    0xf0a: vf0a(0xf5e) = CONST 
    0xf0d: JUMPI vf0a(0xf5e), vf09

    Begin block 0xf0e
    prev=[0xeeb], succ=[]
    =================================
    0xf0e: vf0e(0x40) = CONST 
    0xf10: vf10 = MLOAD vf0e(0x40)
    0xf11: vf11(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf33: MSTORE vf10, vf11(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf34: vf34(0x4) = CONST 
    0xf36: vf36 = ADD vf34(0x4), vf10
    0xf39: vf39(0x20) = CONST 
    0xf3b: vf3b = ADD vf39(0x20), vf36
    0xf3e: vf3e(0x20) = SUB vf3b, vf36
    0xf40: MSTORE vf36, vf3e(0x20)
    0xf41: vf41(0x29) = CONST 
    0xf44: MSTORE vf3b, vf41(0x29)
    0xf45: vf45(0x20) = CONST 
    0xf47: vf47 = ADD vf45(0x20), vf3b
    0xf49: vf49(0x2eb2) = CONST 
    0xf4c: vf4c(0x29) = CONST 
    0xf4f: CODECOPY vf47, vf49(0x2eb2), vf4c(0x29)
    0xf50: vf50(0x40) = CONST 
    0xf52: vf52 = ADD vf50(0x40), vf47
    0xf56: vf56(0x40) = CONST 
    0xf58: vf58 = MLOAD vf56(0x40)
    0xf5b: vf5b(0x84) = SUB vf52, vf58
    0xf5d: REVERT vf58, vf5b(0x84)

    Begin block 0xf5e
    prev=[0xeeb], succ=[0x333a]
    =================================
    0xf5f: vf5f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf75: vf75 = AND v374, vf5f(0xffffffffffffffffffffffffffffffffffffffff)
    0xf76: vf76(0x0) = CONST 
    0xf7a: MSTORE vf76(0x0), vf75
    0xf7b: vf7b(0xc) = CONST 
    0xf7d: vf7d(0x20) = CONST 
    0xf81: MSTORE vf7d(0x20), vf7b(0xc)
    0xf82: vf82(0x40) = CONST 
    0xf86: vf86 = SHA3 vf76(0x0), vf82(0x40)
    0xf88: vf88 = SLOAD vf86
    0xf89: vf89(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0xfaa: vfaa = AND vf89(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), vf88
    0xfac: SSTORE vf86, vfaa
    0xfad: vfad(0xd) = CONST 
    0xfb1: MSTORE vf7d(0x20), vfad(0xd)
    0xfb4: vfb4 = SHA3 vf76(0x0), vf82(0x40)
    0xfb7: SSTORE vfb4, vf76(0x0)
    0xfb8: vfb8 = MLOAD vf82(0x40)
    0xfb9: vfb9(0xe94479a9f7e1952cc78f2d6baab678adc1b772d936c6583def489e524cb66692) = CONST 
    0xfdc: LOG2 vfb8, vf76(0x0), vfb9(0xe94479a9f7e1952cc78f2d6baab678adc1b772d936c6583def489e524cb66692), vf75
    0xfde: vfde(0x1) = CONST 
    0xfe3: JUMP v347(0x333a)

    Begin block 0x333a
    prev=[0xf5e], succ=[]
    =================================
    0x333b: v333b(0x40) = CONST 
    0x333e: v333e = MLOAD v333b(0x40)
    0x3340: v3340 = ISZERO vfde(0x1)
    0x3341: v3341 = ISZERO v3340
    0x3343: MSTORE v333e, v3341
    0x3344: v3344 = MLOAD v333b(0x40)
    0x3348: v3348(0x0) = SUB v333e, v3344
    0x3349: v3349(0x20) = CONST 
    0x334b: v334b(0x20) = ADD v3349(0x20), v3348(0x0)
    0x334d: RETURN v3344, v334b(0x20)

}

function decimals()() public {
    Begin block 0x379
    prev=[], succ=[0xfe4]
    =================================
    0x37a: v37a(0x381) = CONST 
    0x37d: v37d(0xfe4) = CONST 
    0x380: JUMP v37d(0xfe4)

    Begin block 0xfe4
    prev=[0x379], succ=[0x381]
    =================================
    0xfe5: vfe5(0x6) = CONST 
    0xfe7: vfe7 = SLOAD vfe5(0x6)
    0xfe8: vfe8(0xff) = CONST 
    0xfea: vfea = AND vfe8(0xff), vfe7
    0xfec: JUMP v37a(0x381)

    Begin block 0x381
    prev=[0xfe4], succ=[]
    =================================
    0x382: v382(0x40) = CONST 
    0x385: v385 = MLOAD v382(0x40)
    0x386: v386(0xff) = CONST 
    0x38a: v38a = AND vfea, v386(0xff)
    0x38c: MSTORE v385, v38a
    0x38d: v38d = MLOAD v382(0x40)
    0x391: v391(0x0) = SUB v385, v38d
    0x392: v392(0x20) = CONST 
    0x394: v394(0x20) = ADD v392(0x20), v391(0x0)
    0x396: RETURN v38d, v394(0x20)

}

function initialize(string,string,string,uint8,address,address,address,address)() public {
    Begin block 0x397
    prev=[], succ=[0x3aa, 0x3ae]
    =================================
    0x398: v398(0x336d) = CONST 
    0x39b: v39b(0x4) = CONST 
    0x39e: v39e = CALLDATASIZE 
    0x39f: v39f = SUB v39e, v39b(0x4)
    0x3a0: v3a0(0x100) = CONST 
    0x3a4: v3a4 = LT v39f, v3a0(0x100)
    0x3a5: v3a5 = ISZERO v3a4
    0x3a6: v3a6(0x3ae) = CONST 
    0x3a9: JUMPI v3a6(0x3ae), v3a5

    Begin block 0x3aa
    prev=[0x397], succ=[]
    =================================
    0x3aa: v3aa(0x0) = CONST 
    0x3ad: REVERT v3aa(0x0), v3aa(0x0)

    Begin block 0x3ae
    prev=[0x397], succ=[0x3c5, 0x3c9]
    =================================
    0x3b0: v3b0 = ADD v39b(0x4), v39f
    0x3b2: v3b2(0x20) = CONST 
    0x3b5: v3b5(0x24) = ADD v39b(0x4), v3b2(0x20)
    0x3b7: v3b7 = CALLDATALOAD v39b(0x4)
    0x3b8: v3b8(0x100000000) = CONST 
    0x3bf: v3bf = GT v3b7, v3b8(0x100000000)
    0x3c0: v3c0 = ISZERO v3bf
    0x3c1: v3c1(0x3c9) = CONST 
    0x3c4: JUMPI v3c1(0x3c9), v3c0

    Begin block 0x3c5
    prev=[0x3ae], succ=[]
    =================================
    0x3c5: v3c5(0x0) = CONST 
    0x3c8: REVERT v3c5(0x0), v3c5(0x0)

    Begin block 0x3c9
    prev=[0x3ae], succ=[0x3d7, 0x3db]
    =================================
    0x3cb: v3cb = ADD v39b(0x4), v3b7
    0x3cd: v3cd(0x20) = CONST 
    0x3d0: v3d0 = ADD v3cb, v3cd(0x20)
    0x3d1: v3d1 = GT v3d0, v3b0
    0x3d2: v3d2 = ISZERO v3d1
    0x3d3: v3d3(0x3db) = CONST 
    0x3d6: JUMPI v3d3(0x3db), v3d2

    Begin block 0x3d7
    prev=[0x3c9], succ=[]
    =================================
    0x3d7: v3d7(0x0) = CONST 
    0x3da: REVERT v3d7(0x0), v3d7(0x0)

    Begin block 0x3db
    prev=[0x3c9], succ=[0x3f9, 0x3fd]
    =================================
    0x3dd: v3dd = CALLDATALOAD v3cb
    0x3df: v3df(0x20) = CONST 
    0x3e1: v3e1 = ADD v3df(0x20), v3cb
    0x3e4: v3e4(0x1) = CONST 
    0x3e7: v3e7 = MUL v3dd, v3e4(0x1)
    0x3e9: v3e9 = ADD v3e1, v3e7
    0x3ea: v3ea = GT v3e9, v3b0
    0x3eb: v3eb(0x100000000) = CONST 
    0x3f2: v3f2 = GT v3dd, v3eb(0x100000000)
    0x3f3: v3f3 = OR v3f2, v3ea
    0x3f4: v3f4 = ISZERO v3f3
    0x3f5: v3f5(0x3fd) = CONST 
    0x3f8: JUMPI v3f5(0x3fd), v3f4

    Begin block 0x3f9
    prev=[0x3db], succ=[]
    =================================
    0x3f9: v3f9(0x0) = CONST 
    0x3fc: REVERT v3f9(0x0), v3f9(0x0)

    Begin block 0x3fd
    prev=[0x3db], succ=[0x44c, 0x450]
    =================================
    0x402: v402(0x1f) = CONST 
    0x404: v404 = ADD v402(0x1f), v3dd
    0x405: v405(0x20) = CONST 
    0x409: v409 = DIV v404, v405(0x20)
    0x40a: v40a = MUL v409, v405(0x20)
    0x40b: v40b(0x20) = CONST 
    0x40d: v40d = ADD v40b(0x20), v40a
    0x40e: v40e(0x40) = CONST 
    0x410: v410 = MLOAD v40e(0x40)
    0x413: v413 = ADD v410, v40d
    0x414: v414(0x40) = CONST 
    0x416: MSTORE v414(0x40), v413
    0x41e: MSTORE v410, v3dd
    0x41f: v41f(0x20) = CONST 
    0x421: v421 = ADD v41f(0x20), v410
    0x427: CALLDATACOPY v421, v3e1, v3dd
    0x428: v428(0x0) = CONST 
    0x42b: v42b = ADD v421, v3dd
    0x42f: MSTORE v42b, v428(0x0)
    0x435: v435(0x20) = CONST 
    0x438: v438(0x44) = ADD v3b5(0x24), v435(0x20)
    0x43b: v43b = CALLDATALOAD v3b5(0x24)
    0x43f: v43f(0x100000000) = CONST 
    0x446: v446 = GT v43b, v43f(0x100000000)
    0x447: v447 = ISZERO v446
    0x448: v448(0x450) = CONST 
    0x44b: JUMPI v448(0x450), v447

    Begin block 0x44c
    prev=[0x3fd], succ=[]
    =================================
    0x44c: v44c(0x0) = CONST 
    0x44f: REVERT v44c(0x0), v44c(0x0)

    Begin block 0x450
    prev=[0x3fd], succ=[0x45e, 0x462]
    =================================
    0x452: v452 = ADD v39b(0x4), v43b
    0x454: v454(0x20) = CONST 
    0x457: v457 = ADD v452, v454(0x20)
    0x458: v458 = GT v457, v3b0
    0x459: v459 = ISZERO v458
    0x45a: v45a(0x462) = CONST 
    0x45d: JUMPI v45a(0x462), v459

    Begin block 0x45e
    prev=[0x450], succ=[]
    =================================
    0x45e: v45e(0x0) = CONST 
    0x461: REVERT v45e(0x0), v45e(0x0)

    Begin block 0x462
    prev=[0x450], succ=[0x480, 0x484]
    =================================
    0x464: v464 = CALLDATALOAD v452
    0x466: v466(0x20) = CONST 
    0x468: v468 = ADD v466(0x20), v452
    0x46b: v46b(0x1) = CONST 
    0x46e: v46e = MUL v464, v46b(0x1)
    0x470: v470 = ADD v468, v46e
    0x471: v471 = GT v470, v3b0
    0x472: v472(0x100000000) = CONST 
    0x479: v479 = GT v464, v472(0x100000000)
    0x47a: v47a = OR v479, v471
    0x47b: v47b = ISZERO v47a
    0x47c: v47c(0x484) = CONST 
    0x47f: JUMPI v47c(0x484), v47b

    Begin block 0x480
    prev=[0x462], succ=[]
    =================================
    0x480: v480(0x0) = CONST 
    0x483: REVERT v480(0x0), v480(0x0)

    Begin block 0x484
    prev=[0x462], succ=[0x4d3, 0x4d7]
    =================================
    0x489: v489(0x1f) = CONST 
    0x48b: v48b = ADD v489(0x1f), v464
    0x48c: v48c(0x20) = CONST 
    0x490: v490 = DIV v48b, v48c(0x20)
    0x491: v491 = MUL v490, v48c(0x20)
    0x492: v492(0x20) = CONST 
    0x494: v494 = ADD v492(0x20), v491
    0x495: v495(0x40) = CONST 
    0x497: v497 = MLOAD v495(0x40)
    0x49a: v49a = ADD v497, v494
    0x49b: v49b(0x40) = CONST 
    0x49d: MSTORE v49b(0x40), v49a
    0x4a5: MSTORE v497, v464
    0x4a6: v4a6(0x20) = CONST 
    0x4a8: v4a8 = ADD v4a6(0x20), v497
    0x4ae: CALLDATACOPY v4a8, v468, v464
    0x4af: v4af(0x0) = CONST 
    0x4b2: v4b2 = ADD v4a8, v464
    0x4b6: MSTORE v4b2, v4af(0x0)
    0x4bc: v4bc(0x20) = CONST 
    0x4bf: v4bf(0x64) = ADD v438(0x44), v4bc(0x20)
    0x4c2: v4c2 = CALLDATALOAD v438(0x44)
    0x4c6: v4c6(0x100000000) = CONST 
    0x4cd: v4cd = GT v4c2, v4c6(0x100000000)
    0x4ce: v4ce = ISZERO v4cd
    0x4cf: v4cf(0x4d7) = CONST 
    0x4d2: JUMPI v4cf(0x4d7), v4ce

    Begin block 0x4d3
    prev=[0x484], succ=[]
    =================================
    0x4d3: v4d3(0x0) = CONST 
    0x4d6: REVERT v4d3(0x0), v4d3(0x0)

    Begin block 0x4d7
    prev=[0x484], succ=[0x4e5, 0x4e9]
    =================================
    0x4d9: v4d9 = ADD v39b(0x4), v4c2
    0x4db: v4db(0x20) = CONST 
    0x4de: v4de = ADD v4d9, v4db(0x20)
    0x4df: v4df = GT v4de, v3b0
    0x4e0: v4e0 = ISZERO v4df
    0x4e1: v4e1(0x4e9) = CONST 
    0x4e4: JUMPI v4e1(0x4e9), v4e0

    Begin block 0x4e5
    prev=[0x4d7], succ=[]
    =================================
    0x4e5: v4e5(0x0) = CONST 
    0x4e8: REVERT v4e5(0x0), v4e5(0x0)

    Begin block 0x4e9
    prev=[0x4d7], succ=[0x507, 0x50b]
    =================================
    0x4eb: v4eb = CALLDATALOAD v4d9
    0x4ed: v4ed(0x20) = CONST 
    0x4ef: v4ef = ADD v4ed(0x20), v4d9
    0x4f2: v4f2(0x1) = CONST 
    0x4f5: v4f5 = MUL v4eb, v4f2(0x1)
    0x4f7: v4f7 = ADD v4ef, v4f5
    0x4f8: v4f8 = GT v4f7, v3b0
    0x4f9: v4f9(0x100000000) = CONST 
    0x500: v500 = GT v4eb, v4f9(0x100000000)
    0x501: v501 = OR v500, v4f8
    0x502: v502 = ISZERO v501
    0x503: v503(0x50b) = CONST 
    0x506: JUMPI v503(0x50b), v502

    Begin block 0x507
    prev=[0x4e9], succ=[]
    =================================
    0x507: v507(0x0) = CONST 
    0x50a: REVERT v507(0x0), v507(0x0)

    Begin block 0x50b
    prev=[0x4e9], succ=[0xfed]
    =================================
    0x510: v510(0x1f) = CONST 
    0x512: v512 = ADD v510(0x1f), v4eb
    0x513: v513(0x20) = CONST 
    0x517: v517 = DIV v512, v513(0x20)
    0x518: v518 = MUL v517, v513(0x20)
    0x519: v519(0x20) = CONST 
    0x51b: v51b = ADD v519(0x20), v518
    0x51c: v51c(0x40) = CONST 
    0x51e: v51e = MLOAD v51c(0x40)
    0x521: v521 = ADD v51e, v51b
    0x522: v522(0x40) = CONST 
    0x524: MSTORE v522(0x40), v521
    0x52c: MSTORE v51e, v4eb
    0x52d: v52d(0x20) = CONST 
    0x52f: v52f = ADD v52d(0x20), v51e
    0x535: CALLDATACOPY v52f, v4ef, v4eb
    0x536: v536(0x0) = CONST 
    0x539: v539 = ADD v52f, v4eb
    0x53d: MSTORE v539, v536(0x0)
    0x545: v545 = CALLDATALOAD v4bf(0x64)
    0x546: v546(0xff) = CONST 
    0x548: v548 = AND v546(0xff), v545
    0x54c: v54c(0x20) = CONST 
    0x54f: v54f(0x84) = ADD v4bf(0x64), v54c(0x20)
    0x550: v550 = CALLDATALOAD v54f(0x84)
    0x551: v551(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x568: v568 = AND v551(0xffffffffffffffffffffffffffffffffffffffff), v550
    0x56a: v56a(0x40) = CONST 
    0x56d: v56d(0xa4) = ADD v4bf(0x64), v56a(0x40)
    0x56e: v56e = CALLDATALOAD v56d(0xa4)
    0x570: v570 = AND v551(0xffffffffffffffffffffffffffffffffffffffff), v56e
    0x572: v572(0x60) = CONST 
    0x575: v575(0xc4) = ADD v4bf(0x64), v572(0x60)
    0x576: v576 = CALLDATALOAD v575(0xc4)
    0x578: v578 = AND v551(0xffffffffffffffffffffffffffffffffffffffff), v576
    0x57a: v57a(0x80) = CONST 
    0x57c: v57c(0xe4) = ADD v57a(0x80), v4bf(0x64)
    0x57d: v57d = CALLDATALOAD v57c(0xe4)
    0x57e: v57e = AND v57d, v551(0xffffffffffffffffffffffffffffffffffffffff)
    0x57f: v57f(0xfed) = CONST 
    0x582: JUMP v57f(0xfed)

    Begin block 0xfed
    prev=[0x50b], succ=[0x1011, 0x1061]
    =================================
    0xfee: vfee(0x8) = CONST 
    0xff0: vff0 = SLOAD vfee(0x8)
    0xff1: vff1(0x10000000000000000000000000000000000000000) = CONST 
    0x1008: v1008 = DIV vff0, vff1(0x10000000000000000000000000000000000000000)
    0x1009: v1009(0xff) = CONST 
    0x100b: v100b = AND v1009(0xff), v1008
    0x100c: v100c = ISZERO v100b
    0x100d: v100d(0x1061) = CONST 
    0x1010: JUMPI v100d(0x1061), v100c

    Begin block 0x1011
    prev=[0xfed], succ=[]
    =================================
    0x1011: v1011(0x40) = CONST 
    0x1013: v1013 = MLOAD v1011(0x40)
    0x1014: v1014(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1036: MSTORE v1013, v1014(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1037: v1037(0x4) = CONST 
    0x1039: v1039 = ADD v1037(0x4), v1013
    0x103c: v103c(0x20) = CONST 
    0x103e: v103e = ADD v103c(0x20), v1039
    0x1041: v1041(0x20) = SUB v103e, v1039
    0x1043: MSTORE v1039, v1041(0x20)
    0x1044: v1044(0x2a) = CONST 
    0x1047: MSTORE v103e, v1044(0x2a)
    0x1048: v1048(0x20) = CONST 
    0x104a: v104a = ADD v1048(0x20), v103e
    0x104c: v104c(0x2fd3) = CONST 
    0x104f: v104f(0x2a) = CONST 
    0x1052: CODECOPY v104a, v104c(0x2fd3), v104f(0x2a)
    0x1053: v1053(0x40) = CONST 
    0x1055: v1055 = ADD v1053(0x40), v104a
    0x1059: v1059(0x40) = CONST 
    0x105b: v105b = MLOAD v1059(0x40)
    0x105e: v105e(0x84) = SUB v1055, v105b
    0x1060: REVERT v105b, v105e(0x84)

    Begin block 0x1061
    prev=[0xfed], succ=[0x107d, 0x10cd]
    =================================
    0x1062: v1062(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1078: v1078 = AND v568, v1062(0xffffffffffffffffffffffffffffffffffffffff)
    0x1079: v1079(0x10cd) = CONST 
    0x107c: JUMPI v1079(0x10cd), v1078

    Begin block 0x107d
    prev=[0x1061], succ=[]
    =================================
    0x107d: v107d(0x40) = CONST 
    0x107f: v107f = MLOAD v107d(0x40)
    0x1080: v1080(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x10a2: MSTORE v107f, v1080(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10a3: v10a3(0x4) = CONST 
    0x10a5: v10a5 = ADD v10a3(0x4), v107f
    0x10a8: v10a8(0x20) = CONST 
    0x10aa: v10aa = ADD v10a8(0x20), v10a5
    0x10ad: v10ad(0x20) = SUB v10aa, v10a5
    0x10af: MSTORE v10a5, v10ad(0x20)
    0x10b0: v10b0(0x2f) = CONST 
    0x10b3: MSTORE v10aa, v10b0(0x2f)
    0x10b4: v10b4(0x20) = CONST 
    0x10b6: v10b6 = ADD v10b4(0x20), v10aa
    0x10b8: v10b8(0x2f4e) = CONST 
    0x10bb: v10bb(0x2f) = CONST 
    0x10be: CODECOPY v10b6, v10b8(0x2f4e), v10bb(0x2f)
    0x10bf: v10bf(0x40) = CONST 
    0x10c1: v10c1 = ADD v10bf(0x40), v10b6
    0x10c5: v10c5(0x40) = CONST 
    0x10c7: v10c7 = MLOAD v10c5(0x40)
    0x10ca: v10ca(0x84) = SUB v10c1, v10c7
    0x10cc: REVERT v10c7, v10ca(0x84)

    Begin block 0x10cd
    prev=[0x1061], succ=[0x10e9, 0x1139]
    =================================
    0x10ce: v10ce(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x10e4: v10e4 = AND v570, v10ce(0xffffffffffffffffffffffffffffffffffffffff)
    0x10e5: v10e5(0x1139) = CONST 
    0x10e8: JUMPI v10e5(0x1139), v10e4

    Begin block 0x10e9
    prev=[0x10cd], succ=[]
    =================================
    0x10e9: v10e9(0x40) = CONST 
    0x10eb: v10eb = MLOAD v10e9(0x40)
    0x10ec: v10ec(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x110e: MSTORE v10eb, v10ec(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x110f: v110f(0x4) = CONST 
    0x1111: v1111 = ADD v110f(0x4), v10eb
    0x1114: v1114(0x20) = CONST 
    0x1116: v1116 = ADD v1114(0x20), v1111
    0x1119: v1119(0x20) = SUB v1116, v1111
    0x111b: MSTORE v1111, v1119(0x20)
    0x111c: v111c(0x29) = CONST 
    0x111f: MSTORE v1116, v111c(0x29)
    0x1120: v1120(0x20) = CONST 
    0x1122: v1122 = ADD v1120(0x20), v1116
    0x1124: v1124(0x2e3a) = CONST 
    0x1127: v1127(0x29) = CONST 
    0x112a: CODECOPY v1122, v1124(0x2e3a), v1127(0x29)
    0x112b: v112b(0x40) = CONST 
    0x112d: v112d = ADD v112b(0x40), v1122
    0x1131: v1131(0x40) = CONST 
    0x1133: v1133 = MLOAD v1131(0x40)
    0x1136: v1136(0x84) = SUB v112d, v1133
    0x1138: REVERT v1133, v1136(0x84)

    Begin block 0x1139
    prev=[0x10cd], succ=[0x1155, 0x11a5]
    =================================
    0x113a: v113a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1150: v1150 = AND v578, v113a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1151: v1151(0x11a5) = CONST 
    0x1154: JUMPI v1151(0x11a5), v1150

    Begin block 0x1155
    prev=[0x1139], succ=[]
    =================================
    0x1155: v1155(0x40) = CONST 
    0x1157: v1157 = MLOAD v1155(0x40)
    0x1158: v1158(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x117a: MSTORE v1157, v1158(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x117b: v117b(0x4) = CONST 
    0x117d: v117d = ADD v117b(0x4), v1157
    0x1180: v1180(0x20) = CONST 
    0x1182: v1182 = ADD v1180(0x20), v117d
    0x1185: v1185(0x20) = SUB v1182, v117d
    0x1187: MSTORE v117d, v1185(0x20)
    0x1188: v1188(0x2e) = CONST 
    0x118b: MSTORE v1182, v1188(0x2e)
    0x118c: v118c(0x20) = CONST 
    0x118e: v118e = ADD v118c(0x20), v1182
    0x1190: v1190(0x2fa5) = CONST 
    0x1193: v1193(0x2e) = CONST 
    0x1196: CODECOPY v118e, v1190(0x2fa5), v1193(0x2e)
    0x1197: v1197(0x40) = CONST 
    0x1199: v1199 = ADD v1197(0x40), v118e
    0x119d: v119d(0x40) = CONST 
    0x119f: v119f = MLOAD v119d(0x40)
    0x11a2: v11a2(0x84) = SUB v1199, v119f
    0x11a4: REVERT v119f, v11a2(0x84)

    Begin block 0x11a5
    prev=[0x1139], succ=[0x11c1, 0x1211]
    =================================
    0x11a6: v11a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11bc: v11bc = AND v57e, v11a6(0xffffffffffffffffffffffffffffffffffffffff)
    0x11bd: v11bd(0x1211) = CONST 
    0x11c0: JUMPI v11bd(0x1211), v11bc

    Begin block 0x11c1
    prev=[0x11a5], succ=[]
    =================================
    0x11c1: v11c1(0x40) = CONST 
    0x11c3: v11c3 = MLOAD v11c1(0x40)
    0x11c4: v11c4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11e6: MSTORE v11c3, v11c4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11e7: v11e7(0x4) = CONST 
    0x11e9: v11e9 = ADD v11e7(0x4), v11c3
    0x11ec: v11ec(0x20) = CONST 
    0x11ee: v11ee = ADD v11ec(0x20), v11e9
    0x11f1: v11f1(0x20) = SUB v11ee, v11e9
    0x11f3: MSTORE v11e9, v11f1(0x20)
    0x11f4: v11f4(0x28) = CONST 
    0x11f7: MSTORE v11ee, v11f4(0x28)
    0x11f8: v11f8(0x20) = CONST 
    0x11fa: v11fa = ADD v11f8(0x20), v11ee
    0x11fc: v11fc(0x3096) = CONST 
    0x11ff: v11ff(0x28) = CONST 
    0x1202: CODECOPY v11fa, v11fc(0x3096), v11ff(0x28)
    0x1203: v1203(0x40) = CONST 
    0x1205: v1205 = ADD v1203(0x40), v11fa
    0x1209: v1209(0x40) = CONST 
    0x120b: v120b = MLOAD v1209(0x40)
    0x120e: v120e(0x84) = SUB v1205, v120b
    0x1210: REVERT v120b, v120e(0x84)

    Begin block 0x1211
    prev=[0x11a5], succ=[0x2cc7B0x1211]
    =================================
    0x1213: v1213 = MLOAD v410
    0x1214: v1214(0x1224) = CONST 
    0x1218: v1218(0x4) = CONST 
    0x121b: v121b(0x20) = CONST 
    0x121e: v121e = ADD v410, v121b(0x20)
    0x1220: v1220(0x2cc7) = CONST 
    0x1223: JUMP v1220(0x2cc7)

    Begin block 0x2cc7B0x1211
    prev=[0x1211], succ=[0x2d08B0x1211, 0x2cf8B0x1211]
    =================================
    0x2ccaS0x1211: v2ccaV1211 = SLOAD v1218(0x4)
    0x2ccbS0x1211: v2ccbV1211(0x1) = CONST 
    0x2cceS0x1211: v2cceV1211(0x1) = CONST 
    0x2cd0S0x1211: v2cd0V1211 = AND v2cceV1211(0x1), v2ccaV1211
    0x2cd1S0x1211: v2cd1V1211 = ISZERO v2cd0V1211
    0x2cd2S0x1211: v2cd2V1211(0x100) = CONST 
    0x2cd5S0x1211: v2cd5V1211 = MUL v2cd2V1211(0x100), v2cd1V1211
    0x2cd6S0x1211: v2cd6V1211 = SUB v2cd5V1211, v2ccbV1211(0x1)
    0x2cd7S0x1211: v2cd7V1211 = AND v2cd6V1211, v2ccaV1211
    0x2cd8S0x1211: v2cd8V1211(0x2) = CONST 
    0x2cdbS0x1211: v2cdbV1211 = DIV v2cd7V1211, v2cd8V1211(0x2)
    0x2cddS0x1211: v2cddV1211(0x0) = CONST 
    0x2cdfS0x1211: MSTORE v2cddV1211(0x0), v1218(0x4)
    0x2ce0S0x1211: v2ce0V1211(0x20) = CONST 
    0x2ce2S0x1211: v2ce2V1211(0x0) = CONST 
    0x2ce4S0x1211: v2ce4V1211 = SHA3 v2ce2V1211(0x0), v2ce0V1211(0x20)
    0x2ce6S0x1211: v2ce6V1211(0x1f) = CONST 
    0x2ce8S0x1211: v2ce8V1211 = ADD v2ce6V1211(0x1f), v2cdbV1211
    0x2ce9S0x1211: v2ce9V1211(0x20) = CONST 
    0x2cecS0x1211: v2cecV1211 = DIV v2ce8V1211, v2ce9V1211(0x20)
    0x2ceeS0x1211: v2ceeV1211 = ADD v2ce4V1211, v2cecV1211
    0x2cf1S0x1211: v2cf1V1211(0x1f) = CONST 
    0x2cf3S0x1211: v2cf3V1211 = LT v2cf1V1211(0x1f), v1213
    0x2cf4S0x1211: v2cf4V1211(0x2d08) = CONST 
    0x2cf7S0x1211: JUMPI v2cf4V1211(0x2d08), v2cf3V1211

    Begin block 0x2d08B0x1211
    prev=[0x2cc7B0x1211], succ=[0x2d35B0x1211, 0x2d17B0x1211]
    =================================
    0x2d0bS0x1211: v2d0bV1211 = ADD v1213, v1213
    0x2d0cS0x1211: v2d0cV1211(0x1) = CONST 
    0x2d0eS0x1211: v2d0eV1211 = ADD v2d0cV1211(0x1), v2d0bV1211
    0x2d10S0x1211: SSTORE v1218(0x4), v2d0eV1211
    0x2d12S0x1211: v2d12V1211 = ISZERO v1213
    0x2d13S0x1211: v2d13V1211(0x2d35) = CONST 
    0x2d16S0x1211: JUMPI v2d13V1211(0x2d35), v2d12V1211

    Begin block 0x2d35B0x1211
    prev=[0x2d08B0x1211, 0x2d1aB0x1211, 0x2cf8B0x1211], succ=[0x2d45B0x2d35B0x1211]
    =================================
    0x2d35_0x1S0x1211: v2d35_1V1211 = PHI v2ce4V1211, v2d2fV1211
    0x2d37S0x1211: v2d37V1211(0x3905) = CONST 
    0x2d3dS0x1211: v2d3dV1211(0x2d45) = CONST 
    0x2d40S0x1211: JUMP v2d3dV1211(0x2d45)

    Begin block 0x2d45B0x2d35B0x1211
    prev=[0x2d35B0x1211], succ=[0x2d46B0x2d35B0x1211]
    =================================

    Begin block 0x2d46B0x2d35B0x1211
    prev=[0x2d4fB0x2d35B0x1211, 0x2d45B0x2d35B0x1211], succ=[0x2d4fB0x2d35B0x1211, 0x3928B0x2d35B0x1211]
    =================================
    0x2d46_0x0S0x2d35S0x1211: v2d46_0V2d35V1211 = PHI v2d35_1V1211, v2d55V2d35V1211
    0x2d49S0x2d35S0x1211: v2d49V2d35V1211 = GT v2ceeV1211, v2d46_0V2d35V1211
    0x2d4aS0x2d35S0x1211: v2d4aV2d35V1211 = ISZERO v2d49V2d35V1211
    0x2d4bS0x2d35S0x1211: v2d4bV2d35V1211(0x3928) = CONST 
    0x2d4eS0x2d35S0x1211: JUMPI v2d4bV2d35V1211(0x3928), v2d4aV2d35V1211

    Begin block 0x2d4fB0x2d35B0x1211
    prev=[0x2d46B0x2d35B0x1211], succ=[0x2d46B0x2d35B0x1211]
    =================================
    0x2d4fS0x2d35S0x1211: v2d4fV2d35V1211(0x0) = CONST 
    0x2d4f_0x0S0x2d35S0x1211: v2d4f_0V2d35V1211 = PHI v2d35_1V1211, v2d55V2d35V1211
    0x2d52S0x2d35S0x1211: SSTORE v2d4f_0V2d35V1211, v2d4fV2d35V1211(0x0)
    0x2d53S0x2d35S0x1211: v2d53V2d35V1211(0x1) = CONST 
    0x2d55S0x2d35S0x1211: v2d55V2d35V1211 = ADD v2d53V2d35V1211(0x1), v2d4f_0V2d35V1211
    0x2d56S0x2d35S0x1211: v2d56V2d35V1211(0x2d46) = CONST 
    0x2d59S0x2d35S0x1211: JUMP v2d56V2d35V1211(0x2d46)

    Begin block 0x3928B0x2d35B0x1211
    prev=[0x2d46B0x2d35B0x1211], succ=[0x3905B0x1211]
    =================================
    0x392bS0x2d35S0x1211: JUMP v2d37V1211(0x3905)

    Begin block 0x3905B0x1211
    prev=[0x3928B0x2d35B0x1211], succ=[0x1224]
    =================================
    0x3908S0x1211: JUMP v1214(0x1224)

    Begin block 0x1224
    prev=[0x3905B0x1211], succ=[0x2cc7B0x1224]
    =================================
    0x1227: v1227 = MLOAD v497
    0x1228: v1228(0x1238) = CONST 
    0x122c: v122c(0x5) = CONST 
    0x122f: v122f(0x20) = CONST 
    0x1232: v1232 = ADD v497, v122f(0x20)
    0x1234: v1234(0x2cc7) = CONST 
    0x1237: JUMP v1234(0x2cc7)

    Begin block 0x2cc7B0x1224
    prev=[0x1224], succ=[0x2d08B0x1224, 0x2cf8B0x1224]
    =================================
    0x2ccaS0x1224: v2ccaV1224 = SLOAD v122c(0x5)
    0x2ccbS0x1224: v2ccbV1224(0x1) = CONST 
    0x2cceS0x1224: v2cceV1224(0x1) = CONST 
    0x2cd0S0x1224: v2cd0V1224 = AND v2cceV1224(0x1), v2ccaV1224
    0x2cd1S0x1224: v2cd1V1224 = ISZERO v2cd0V1224
    0x2cd2S0x1224: v2cd2V1224(0x100) = CONST 
    0x2cd5S0x1224: v2cd5V1224 = MUL v2cd2V1224(0x100), v2cd1V1224
    0x2cd6S0x1224: v2cd6V1224 = SUB v2cd5V1224, v2ccbV1224(0x1)
    0x2cd7S0x1224: v2cd7V1224 = AND v2cd6V1224, v2ccaV1224
    0x2cd8S0x1224: v2cd8V1224(0x2) = CONST 
    0x2cdbS0x1224: v2cdbV1224 = DIV v2cd7V1224, v2cd8V1224(0x2)
    0x2cddS0x1224: v2cddV1224(0x0) = CONST 
    0x2cdfS0x1224: MSTORE v2cddV1224(0x0), v122c(0x5)
    0x2ce0S0x1224: v2ce0V1224(0x20) = CONST 
    0x2ce2S0x1224: v2ce2V1224(0x0) = CONST 
    0x2ce4S0x1224: v2ce4V1224 = SHA3 v2ce2V1224(0x0), v2ce0V1224(0x20)
    0x2ce6S0x1224: v2ce6V1224(0x1f) = CONST 
    0x2ce8S0x1224: v2ce8V1224 = ADD v2ce6V1224(0x1f), v2cdbV1224
    0x2ce9S0x1224: v2ce9V1224(0x20) = CONST 
    0x2cecS0x1224: v2cecV1224 = DIV v2ce8V1224, v2ce9V1224(0x20)
    0x2ceeS0x1224: v2ceeV1224 = ADD v2ce4V1224, v2cecV1224
    0x2cf1S0x1224: v2cf1V1224(0x1f) = CONST 
    0x2cf3S0x1224: v2cf3V1224 = LT v2cf1V1224(0x1f), v1227
    0x2cf4S0x1224: v2cf4V1224(0x2d08) = CONST 
    0x2cf7S0x1224: JUMPI v2cf4V1224(0x2d08), v2cf3V1224

    Begin block 0x2d08B0x1224
    prev=[0x2cc7B0x1224], succ=[0x2d35B0x1224, 0x2d17B0x1224]
    =================================
    0x2d0bS0x1224: v2d0bV1224 = ADD v1227, v1227
    0x2d0cS0x1224: v2d0cV1224(0x1) = CONST 
    0x2d0eS0x1224: v2d0eV1224 = ADD v2d0cV1224(0x1), v2d0bV1224
    0x2d10S0x1224: SSTORE v122c(0x5), v2d0eV1224
    0x2d12S0x1224: v2d12V1224 = ISZERO v1227
    0x2d13S0x1224: v2d13V1224(0x2d35) = CONST 
    0x2d16S0x1224: JUMPI v2d13V1224(0x2d35), v2d12V1224

    Begin block 0x2d35B0x1224
    prev=[0x2d08B0x1224, 0x2d1aB0x1224, 0x2cf8B0x1224], succ=[0x2d45B0x2d35B0x1224]
    =================================
    0x2d35_0x1S0x1224: v2d35_1V1224 = PHI v2ce4V1224, v2d2fV1224
    0x2d37S0x1224: v2d37V1224(0x3905) = CONST 
    0x2d3dS0x1224: v2d3dV1224(0x2d45) = CONST 
    0x2d40S0x1224: JUMP v2d3dV1224(0x2d45)

    Begin block 0x2d45B0x2d35B0x1224
    prev=[0x2d35B0x1224], succ=[0x2d46B0x2d35B0x1224]
    =================================

    Begin block 0x2d46B0x2d35B0x1224
    prev=[0x2d4fB0x2d35B0x1224, 0x2d45B0x2d35B0x1224], succ=[0x2d4fB0x2d35B0x1224, 0x3928B0x2d35B0x1224]
    =================================
    0x2d46_0x0S0x2d35S0x1224: v2d46_0V2d35V1224 = PHI v2d35_1V1224, v2d55V2d35V1224
    0x2d49S0x2d35S0x1224: v2d49V2d35V1224 = GT v2ceeV1224, v2d46_0V2d35V1224
    0x2d4aS0x2d35S0x1224: v2d4aV2d35V1224 = ISZERO v2d49V2d35V1224
    0x2d4bS0x2d35S0x1224: v2d4bV2d35V1224(0x3928) = CONST 
    0x2d4eS0x2d35S0x1224: JUMPI v2d4bV2d35V1224(0x3928), v2d4aV2d35V1224

    Begin block 0x2d4fB0x2d35B0x1224
    prev=[0x2d46B0x2d35B0x1224], succ=[0x2d46B0x2d35B0x1224]
    =================================
    0x2d4fS0x2d35S0x1224: v2d4fV2d35V1224(0x0) = CONST 
    0x2d4f_0x0S0x2d35S0x1224: v2d4f_0V2d35V1224 = PHI v2d35_1V1224, v2d55V2d35V1224
    0x2d52S0x2d35S0x1224: SSTORE v2d4f_0V2d35V1224, v2d4fV2d35V1224(0x0)
    0x2d53S0x2d35S0x1224: v2d53V2d35V1224(0x1) = CONST 
    0x2d55S0x2d35S0x1224: v2d55V2d35V1224 = ADD v2d53V2d35V1224(0x1), v2d4f_0V2d35V1224
    0x2d56S0x2d35S0x1224: v2d56V2d35V1224(0x2d46) = CONST 
    0x2d59S0x2d35S0x1224: JUMP v2d56V2d35V1224(0x2d46)

    Begin block 0x3928B0x2d35B0x1224
    prev=[0x2d46B0x2d35B0x1224], succ=[0x3905B0x1224]
    =================================
    0x392bS0x2d35S0x1224: JUMP v2d37V1224(0x3905)

    Begin block 0x3905B0x1224
    prev=[0x3928B0x2d35B0x1224], succ=[0x1238]
    =================================
    0x3908S0x1224: JUMP v1228(0x1238)

    Begin block 0x1238
    prev=[0x3905B0x1224], succ=[0x2cc7B0x1238]
    =================================
    0x123b: v123b = MLOAD v51e
    0x123c: v123c(0x124c) = CONST 
    0x1240: v1240(0x7) = CONST 
    0x1243: v1243(0x20) = CONST 
    0x1246: v1246 = ADD v51e, v1243(0x20)
    0x1248: v1248(0x2cc7) = CONST 
    0x124b: JUMP v1248(0x2cc7)

    Begin block 0x2cc7B0x1238
    prev=[0x1238], succ=[0x2d08B0x1238, 0x2cf8B0x1238]
    =================================
    0x2ccaS0x1238: v2ccaV1238 = SLOAD v1240(0x7)
    0x2ccbS0x1238: v2ccbV1238(0x1) = CONST 
    0x2cceS0x1238: v2cceV1238(0x1) = CONST 
    0x2cd0S0x1238: v2cd0V1238 = AND v2cceV1238(0x1), v2ccaV1238
    0x2cd1S0x1238: v2cd1V1238 = ISZERO v2cd0V1238
    0x2cd2S0x1238: v2cd2V1238(0x100) = CONST 
    0x2cd5S0x1238: v2cd5V1238 = MUL v2cd2V1238(0x100), v2cd1V1238
    0x2cd6S0x1238: v2cd6V1238 = SUB v2cd5V1238, v2ccbV1238(0x1)
    0x2cd7S0x1238: v2cd7V1238 = AND v2cd6V1238, v2ccaV1238
    0x2cd8S0x1238: v2cd8V1238(0x2) = CONST 
    0x2cdbS0x1238: v2cdbV1238 = DIV v2cd7V1238, v2cd8V1238(0x2)
    0x2cddS0x1238: v2cddV1238(0x0) = CONST 
    0x2cdfS0x1238: MSTORE v2cddV1238(0x0), v1240(0x7)
    0x2ce0S0x1238: v2ce0V1238(0x20) = CONST 
    0x2ce2S0x1238: v2ce2V1238(0x0) = CONST 
    0x2ce4S0x1238: v2ce4V1238 = SHA3 v2ce2V1238(0x0), v2ce0V1238(0x20)
    0x2ce6S0x1238: v2ce6V1238(0x1f) = CONST 
    0x2ce8S0x1238: v2ce8V1238 = ADD v2ce6V1238(0x1f), v2cdbV1238
    0x2ce9S0x1238: v2ce9V1238(0x20) = CONST 
    0x2cecS0x1238: v2cecV1238 = DIV v2ce8V1238, v2ce9V1238(0x20)
    0x2ceeS0x1238: v2ceeV1238 = ADD v2ce4V1238, v2cecV1238
    0x2cf1S0x1238: v2cf1V1238(0x1f) = CONST 
    0x2cf3S0x1238: v2cf3V1238 = LT v2cf1V1238(0x1f), v123b
    0x2cf4S0x1238: v2cf4V1238(0x2d08) = CONST 
    0x2cf7S0x1238: JUMPI v2cf4V1238(0x2d08), v2cf3V1238

    Begin block 0x2d08B0x1238
    prev=[0x2cc7B0x1238], succ=[0x2d35B0x1238, 0x2d17B0x1238]
    =================================
    0x2d0bS0x1238: v2d0bV1238 = ADD v123b, v123b
    0x2d0cS0x1238: v2d0cV1238(0x1) = CONST 
    0x2d0eS0x1238: v2d0eV1238 = ADD v2d0cV1238(0x1), v2d0bV1238
    0x2d10S0x1238: SSTORE v1240(0x7), v2d0eV1238
    0x2d12S0x1238: v2d12V1238 = ISZERO v123b
    0x2d13S0x1238: v2d13V1238(0x2d35) = CONST 
    0x2d16S0x1238: JUMPI v2d13V1238(0x2d35), v2d12V1238

    Begin block 0x2d35B0x1238
    prev=[0x2d08B0x1238, 0x2d1aB0x1238, 0x2cf8B0x1238], succ=[0x2d45B0x2d35B0x1238]
    =================================
    0x2d35_0x1S0x1238: v2d35_1V1238 = PHI v2ce4V1238, v2d2fV1238
    0x2d37S0x1238: v2d37V1238(0x3905) = CONST 
    0x2d3dS0x1238: v2d3dV1238(0x2d45) = CONST 
    0x2d40S0x1238: JUMP v2d3dV1238(0x2d45)

    Begin block 0x2d45B0x2d35B0x1238
    prev=[0x2d35B0x1238], succ=[0x2d46B0x2d35B0x1238]
    =================================

    Begin block 0x2d46B0x2d35B0x1238
    prev=[0x2d4fB0x2d35B0x1238, 0x2d45B0x2d35B0x1238], succ=[0x2d4fB0x2d35B0x1238, 0x3928B0x2d35B0x1238]
    =================================
    0x2d46_0x0S0x2d35S0x1238: v2d46_0V2d35V1238 = PHI v2d35_1V1238, v2d55V2d35V1238
    0x2d49S0x2d35S0x1238: v2d49V2d35V1238 = GT v2ceeV1238, v2d46_0V2d35V1238
    0x2d4aS0x2d35S0x1238: v2d4aV2d35V1238 = ISZERO v2d49V2d35V1238
    0x2d4bS0x2d35S0x1238: v2d4bV2d35V1238(0x3928) = CONST 
    0x2d4eS0x2d35S0x1238: JUMPI v2d4bV2d35V1238(0x3928), v2d4aV2d35V1238

    Begin block 0x2d4fB0x2d35B0x1238
    prev=[0x2d46B0x2d35B0x1238], succ=[0x2d46B0x2d35B0x1238]
    =================================
    0x2d4fS0x2d35S0x1238: v2d4fV2d35V1238(0x0) = CONST 
    0x2d4f_0x0S0x2d35S0x1238: v2d4f_0V2d35V1238 = PHI v2d35_1V1238, v2d55V2d35V1238
    0x2d52S0x2d35S0x1238: SSTORE v2d4f_0V2d35V1238, v2d4fV2d35V1238(0x0)
    0x2d53S0x2d35S0x1238: v2d53V2d35V1238(0x1) = CONST 
    0x2d55S0x2d35S0x1238: v2d55V2d35V1238 = ADD v2d53V2d35V1238(0x1), v2d4f_0V2d35V1238
    0x2d56S0x2d35S0x1238: v2d56V2d35V1238(0x2d46) = CONST 
    0x2d59S0x2d35S0x1238: JUMP v2d56V2d35V1238(0x2d46)

    Begin block 0x3928B0x2d35B0x1238
    prev=[0x2d46B0x2d35B0x1238], succ=[0x3905B0x1238]
    =================================
    0x392bS0x2d35S0x1238: JUMP v2d37V1238(0x3905)

    Begin block 0x3905B0x1238
    prev=[0x3928B0x2d35B0x1238], succ=[0x124c]
    =================================
    0x3908S0x1238: JUMP v123c(0x124c)

    Begin block 0x124c
    prev=[0x3905B0x1238], succ=[0x2b5bB0x124c]
    =================================
    0x124e: v124e(0x6) = CONST 
    0x1251: v1251 = SLOAD v124e(0x6)
    0x1252: v1252(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x1273: v1273 = AND v1252(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1251
    0x1274: v1274(0xff) = CONST 
    0x1277: v1277 = AND v548, v1274(0xff)
    0x1278: v1278 = OR v1277, v1273
    0x127a: SSTORE v124e(0x6), v1278
    0x127b: v127b(0x8) = CONST 
    0x127e: v127e = SLOAD v127b(0x8)
    0x127f: v127f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x12a2: v12a2 = AND v127f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v127e
    0x12a3: v12a3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12ba: v12ba = AND v12a3(0xffffffffffffffffffffffffffffffffffffffff), v568
    0x12be: v12be = OR v12ba, v12a2
    0x12c1: SSTORE v127b(0x8), v12be
    0x12c2: v12c2(0x1) = CONST 
    0x12c5: v12c5 = SLOAD v12c2(0x1)
    0x12c7: v12c7 = AND v127f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12c5
    0x12ca: v12ca = AND v12a3(0xffffffffffffffffffffffffffffffffffffffff), v570
    0x12cb: v12cb = OR v12ca, v12c7
    0x12cd: SSTORE v12c2(0x1), v12cb
    0x12ce: v12ce(0x2) = CONST 
    0x12d1: v12d1 = SLOAD v12ce(0x2)
    0x12d4: v12d4 = AND v127f(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v12d1
    0x12d7: v12d7 = AND v578, v12a3(0xffffffffffffffffffffffffffffffffffffffff)
    0x12db: v12db = OR v12d7, v12d4
    0x12dd: SSTORE v12ce(0x2), v12db
    0x12de: v12de(0x12e6) = CONST 
    0x12e2: v12e2(0x2b5b) = CONST 
    0x12e5: JUMP v12e2(0x2b5b), v57e, v12de(0x12e6)

    Begin block 0x2b5bB0x124c
    prev=[0x124c], succ=[0x12e6]
    =================================
    0x2b5cS0x124c: v2b5cV124c(0x0) = CONST 
    0x2b5fS0x124c: v2b5fV124c = SLOAD v2b5cV124c(0x0)
    0x2b60S0x124c: v2b60V124c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x2b81S0x124c: v2b81V124c = AND v2b60V124c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2b5fV124c
    0x2b82S0x124c: v2b82V124c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b9aS0x124c: v2b9aV124c = AND v2b82V124c(0xffffffffffffffffffffffffffffffffffffffff), v57e
    0x2b9eS0x124c: v2b9eV124c = OR v2b9aV124c, v2b81V124c
    0x2ba0S0x124c: SSTORE v2b5cV124c(0x0), v2b9eV124c
    0x2ba1S0x124c: JUMP v12de(0x12e6)

    Begin block 0x12e6
    prev=[0x2b5bB0x124c], succ=[0x336d]
    =================================
    0x12e9: v12e9(0x8) = CONST 
    0x12ec: v12ec = SLOAD v12e9(0x8)
    0x12ed: v12ed(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x130e: v130e = AND v12ed(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v12ec
    0x130f: v130f(0x10000000000000000000000000000000000000000) = CONST 
    0x1325: v1325 = OR v130f(0x10000000000000000000000000000000000000000), v130e
    0x1327: SSTORE v12e9(0x8), v1325
    0x132e: JUMP v398(0x336d)

    Begin block 0x336d
    prev=[0x12e6], succ=[]
    =================================
    0x336e: STOP 

    Begin block 0x2d17B0x1238
    prev=[0x2d08B0x1238], succ=[0x2d1aB0x1238]
    =================================
    0x2d19S0x1238: v2d19V1238 = ADD v1246, v123b

    Begin block 0x2d1aB0x1238
    prev=[0x2d17B0x1238, 0x2d23B0x1238], succ=[0x2d35B0x1238, 0x2d23B0x1238]
    =================================
    0x2d1a_0x2S0x1238: v2d1a_2V1238 = PHI v1246, v2d2aV1238
    0x2d1dS0x1238: v2d1dV1238 = GT v2d19V1238, v2d1a_2V1238
    0x2d1eS0x1238: v2d1eV1238 = ISZERO v2d1dV1238
    0x2d1fS0x1238: v2d1fV1238(0x2d35) = CONST 
    0x2d22S0x1238: JUMPI v2d1fV1238(0x2d35), v2d1eV1238

    Begin block 0x2d23B0x1238
    prev=[0x2d1aB0x1238], succ=[0x2d1aB0x1238]
    =================================
    0x2d23_0x1S0x1238: v2d23_1V1238 = PHI v2ce4V1238, v2d2fV1238
    0x2d23_0x2S0x1238: v2d23_2V1238 = PHI v1246, v2d2aV1238
    0x2d24S0x1238: v2d24V1238 = MLOAD v2d23_2V1238
    0x2d26S0x1238: SSTORE v2d23_1V1238, v2d24V1238
    0x2d28S0x1238: v2d28V1238(0x20) = CONST 
    0x2d2aS0x1238: v2d2aV1238 = ADD v2d28V1238(0x20), v2d23_2V1238
    0x2d2dS0x1238: v2d2dV1238(0x1) = CONST 
    0x2d2fS0x1238: v2d2fV1238 = ADD v2d2dV1238(0x1), v2d23_1V1238
    0x2d31S0x1238: v2d31V1238(0x2d1a) = CONST 
    0x2d34S0x1238: JUMP v2d31V1238(0x2d1a)

    Begin block 0x2cf8B0x1238
    prev=[0x2cc7B0x1238], succ=[0x2d35B0x1238]
    =================================
    0x2cf9S0x1238: v2cf9V1238 = MLOAD v1246
    0x2cfaS0x1238: v2cfaV1238(0xff) = CONST 
    0x2cfcS0x1238: v2cfcV1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2cfaV1238(0xff)
    0x2cfdS0x1238: v2cfdV1238 = AND v2cfcV1238(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2cf9V1238
    0x2d00S0x1238: v2d00V1238 = ADD v123b, v123b
    0x2d01S0x1238: v2d01V1238 = OR v2d00V1238, v2cfdV1238
    0x2d03S0x1238: SSTORE v1240(0x7), v2d01V1238
    0x2d04S0x1238: v2d04V1238(0x2d35) = CONST 
    0x2d07S0x1238: JUMP v2d04V1238(0x2d35)

    Begin block 0x2d17B0x1224
    prev=[0x2d08B0x1224], succ=[0x2d1aB0x1224]
    =================================
    0x2d19S0x1224: v2d19V1224 = ADD v1232, v1227

    Begin block 0x2d1aB0x1224
    prev=[0x2d17B0x1224, 0x2d23B0x1224], succ=[0x2d35B0x1224, 0x2d23B0x1224]
    =================================
    0x2d1a_0x2S0x1224: v2d1a_2V1224 = PHI v1232, v2d2aV1224
    0x2d1dS0x1224: v2d1dV1224 = GT v2d19V1224, v2d1a_2V1224
    0x2d1eS0x1224: v2d1eV1224 = ISZERO v2d1dV1224
    0x2d1fS0x1224: v2d1fV1224(0x2d35) = CONST 
    0x2d22S0x1224: JUMPI v2d1fV1224(0x2d35), v2d1eV1224

    Begin block 0x2d23B0x1224
    prev=[0x2d1aB0x1224], succ=[0x2d1aB0x1224]
    =================================
    0x2d23_0x1S0x1224: v2d23_1V1224 = PHI v2ce4V1224, v2d2fV1224
    0x2d23_0x2S0x1224: v2d23_2V1224 = PHI v1232, v2d2aV1224
    0x2d24S0x1224: v2d24V1224 = MLOAD v2d23_2V1224
    0x2d26S0x1224: SSTORE v2d23_1V1224, v2d24V1224
    0x2d28S0x1224: v2d28V1224(0x20) = CONST 
    0x2d2aS0x1224: v2d2aV1224 = ADD v2d28V1224(0x20), v2d23_2V1224
    0x2d2dS0x1224: v2d2dV1224(0x1) = CONST 
    0x2d2fS0x1224: v2d2fV1224 = ADD v2d2dV1224(0x1), v2d23_1V1224
    0x2d31S0x1224: v2d31V1224(0x2d1a) = CONST 
    0x2d34S0x1224: JUMP v2d31V1224(0x2d1a)

    Begin block 0x2cf8B0x1224
    prev=[0x2cc7B0x1224], succ=[0x2d35B0x1224]
    =================================
    0x2cf9S0x1224: v2cf9V1224 = MLOAD v1232
    0x2cfaS0x1224: v2cfaV1224(0xff) = CONST 
    0x2cfcS0x1224: v2cfcV1224(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2cfaV1224(0xff)
    0x2cfdS0x1224: v2cfdV1224 = AND v2cfcV1224(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2cf9V1224
    0x2d00S0x1224: v2d00V1224 = ADD v1227, v1227
    0x2d01S0x1224: v2d01V1224 = OR v2d00V1224, v2cfdV1224
    0x2d03S0x1224: SSTORE v122c(0x5), v2d01V1224
    0x2d04S0x1224: v2d04V1224(0x2d35) = CONST 
    0x2d07S0x1224: JUMP v2d04V1224(0x2d35)

    Begin block 0x2d17B0x1211
    prev=[0x2d08B0x1211], succ=[0x2d1aB0x1211]
    =================================
    0x2d19S0x1211: v2d19V1211 = ADD v121e, v1213

    Begin block 0x2d1aB0x1211
    prev=[0x2d17B0x1211, 0x2d23B0x1211], succ=[0x2d35B0x1211, 0x2d23B0x1211]
    =================================
    0x2d1a_0x2S0x1211: v2d1a_2V1211 = PHI v121e, v2d2aV1211
    0x2d1dS0x1211: v2d1dV1211 = GT v2d19V1211, v2d1a_2V1211
    0x2d1eS0x1211: v2d1eV1211 = ISZERO v2d1dV1211
    0x2d1fS0x1211: v2d1fV1211(0x2d35) = CONST 
    0x2d22S0x1211: JUMPI v2d1fV1211(0x2d35), v2d1eV1211

    Begin block 0x2d23B0x1211
    prev=[0x2d1aB0x1211], succ=[0x2d1aB0x1211]
    =================================
    0x2d23_0x1S0x1211: v2d23_1V1211 = PHI v2ce4V1211, v2d2fV1211
    0x2d23_0x2S0x1211: v2d23_2V1211 = PHI v121e, v2d2aV1211
    0x2d24S0x1211: v2d24V1211 = MLOAD v2d23_2V1211
    0x2d26S0x1211: SSTORE v2d23_1V1211, v2d24V1211
    0x2d28S0x1211: v2d28V1211(0x20) = CONST 
    0x2d2aS0x1211: v2d2aV1211 = ADD v2d28V1211(0x20), v2d23_2V1211
    0x2d2dS0x1211: v2d2dV1211(0x1) = CONST 
    0x2d2fS0x1211: v2d2fV1211 = ADD v2d2dV1211(0x1), v2d23_1V1211
    0x2d31S0x1211: v2d31V1211(0x2d1a) = CONST 
    0x2d34S0x1211: JUMP v2d31V1211(0x2d1a)

    Begin block 0x2cf8B0x1211
    prev=[0x2cc7B0x1211], succ=[0x2d35B0x1211]
    =================================
    0x2cf9S0x1211: v2cf9V1211 = MLOAD v121e
    0x2cfaS0x1211: v2cfaV1211(0xff) = CONST 
    0x2cfcS0x1211: v2cfcV1211(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v2cfaV1211(0xff)
    0x2cfdS0x1211: v2cfdV1211 = AND v2cfcV1211(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2cf9V1211
    0x2d00S0x1211: v2d00V1211 = ADD v1213, v1213
    0x2d01S0x1211: v2d01V1211 = OR v2d00V1211, v2cfdV1211
    0x2d03S0x1211: SSTORE v1218(0x4), v2d01V1211
    0x2d04S0x1211: v2d04V1211(0x2d35) = CONST 
    0x2d07S0x1211: JUMP v2d04V1211(0x2d35)

}

function masterMinter()() public {
    Begin block 0x583
    prev=[], succ=[0x132f]
    =================================
    0x584: v584(0x338e) = CONST 
    0x587: v587(0x132f) = CONST 
    0x58a: JUMP v587(0x132f)

    Begin block 0x132f
    prev=[0x583], succ=[0x338e]
    =================================
    0x1330: v1330(0x8) = CONST 
    0x1332: v1332 = SLOAD v1330(0x8)
    0x1333: v1333(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1348: v1348 = AND v1333(0xffffffffffffffffffffffffffffffffffffffff), v1332
    0x134a: JUMP v584(0x338e)

    Begin block 0x338e
    prev=[0x132f], succ=[]
    =================================
    0x338f: v338f(0x40) = CONST 
    0x3392: v3392 = MLOAD v338f(0x40)
    0x3393: v3393(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33aa: v33aa = AND v1348, v3393(0xffffffffffffffffffffffffffffffffffffffff)
    0x33ac: MSTORE v3392, v33aa
    0x33ad: v33ad = MLOAD v338f(0x40)
    0x33b1: v33b1(0x0) = SUB v3392, v33ad
    0x33b2: v33b2(0x20) = CONST 
    0x33b4: v33b4(0x20) = ADD v33b2(0x20), v33b1(0x0)
    0x33b6: RETURN v33ad, v33b4(0x20)

}

function unpause()() public {
    Begin block 0x5b4
    prev=[], succ=[0x134b]
    =================================
    0x5b5: v5b5(0x33d6) = CONST 
    0x5b8: v5b8(0x134b) = CONST 
    0x5bb: JUMP v5b8(0x134b)

    Begin block 0x134b
    prev=[0x5b4], succ=[0x136b, 0x13bb]
    =================================
    0x134c: v134c(0x1) = CONST 
    0x134e: v134e = SLOAD v134c(0x1)
    0x134f: v134f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1364: v1364 = AND v134f(0xffffffffffffffffffffffffffffffffffffffff), v134e
    0x1365: v1365 = CALLER 
    0x1366: v1366 = EQ v1365, v1364
    0x1367: v1367(0x13bb) = CONST 
    0x136a: JUMPI v1367(0x13bb), v1366

    Begin block 0x136b
    prev=[0x134b], succ=[]
    =================================
    0x136b: v136b(0x40) = CONST 
    0x136d: v136d = MLOAD v136b(0x40)
    0x136e: v136e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1390: MSTORE v136d, v136e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1391: v1391(0x4) = CONST 
    0x1393: v1393 = ADD v1391(0x4), v136d
    0x1396: v1396(0x20) = CONST 
    0x1398: v1398 = ADD v1396(0x20), v1393
    0x139b: v139b(0x20) = SUB v1398, v1393
    0x139d: MSTORE v1393, v139b(0x20)
    0x139e: v139e(0x22) = CONST 
    0x13a1: MSTORE v1398, v139e(0x22)
    0x13a2: v13a2(0x20) = CONST 
    0x13a4: v13a4 = ADD v13a2(0x20), v1398
    0x13a6: v13a6(0x3074) = CONST 
    0x13a9: v13a9(0x22) = CONST 
    0x13ac: CODECOPY v13a4, v13a6(0x3074), v13a9(0x22)
    0x13ad: v13ad(0x40) = CONST 
    0x13af: v13af = ADD v13ad(0x40), v13a4
    0x13b3: v13b3(0x40) = CONST 
    0x13b5: v13b5 = MLOAD v13b3(0x40)
    0x13b8: v13b8(0x84) = SUB v13af, v13b5
    0x13ba: REVERT v13b5, v13b8(0x84)

    Begin block 0x13bb
    prev=[0x134b], succ=[0x33d6]
    =================================
    0x13bc: v13bc(0x1) = CONST 
    0x13bf: v13bf = SLOAD v13bc(0x1)
    0x13c0: v13c0(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13e1: v13e1 = AND v13c0(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v13bf
    0x13e3: SSTORE v13bc(0x1), v13e1
    0x13e4: v13e4(0x40) = CONST 
    0x13e6: v13e6 = MLOAD v13e4(0x40)
    0x13e7: v13e7(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33) = CONST 
    0x1409: v1409(0x0) = CONST 
    0x140c: LOG1 v13e6, v1409(0x0), v13e7(0x7805862f689e2f13df9f062ff482ad3ad112aca9e0847911ed832e158c525b33)
    0x140d: JUMP v5b5(0x33d6)

    Begin block 0x33d6
    prev=[0x13bb], succ=[]
    =================================
    0x33d7: STOP 

}

function mint(address,uint256)() public {
    Begin block 0x5bc
    prev=[], succ=[0x5ce, 0x5d2]
    =================================
    0x5bd: v5bd(0x33f7) = CONST 
    0x5c0: v5c0(0x4) = CONST 
    0x5c3: v5c3 = CALLDATASIZE 
    0x5c4: v5c4 = SUB v5c3, v5c0(0x4)
    0x5c5: v5c5(0x40) = CONST 
    0x5c8: v5c8 = LT v5c4, v5c5(0x40)
    0x5c9: v5c9 = ISZERO v5c8
    0x5ca: v5ca(0x5d2) = CONST 
    0x5cd: JUMPI v5ca(0x5d2), v5c9

    Begin block 0x5ce
    prev=[0x5bc], succ=[]
    =================================
    0x5ce: v5ce(0x0) = CONST 
    0x5d1: REVERT v5ce(0x0), v5ce(0x0)

    Begin block 0x5d2
    prev=[0x5bc], succ=[0x140e]
    =================================
    0x5d4: v5d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ea: v5ea = CALLDATALOAD v5c0(0x4)
    0x5eb: v5eb = AND v5ea, v5d4(0xffffffffffffffffffffffffffffffffffffffff)
    0x5ed: v5ed(0x20) = CONST 
    0x5ef: v5ef(0x24) = ADD v5ed(0x20), v5c0(0x4)
    0x5f0: v5f0 = CALLDATALOAD v5ef(0x24)
    0x5f1: v5f1(0x140e) = CONST 
    0x5f4: JUMP v5f1(0x140e)

    Begin block 0x140e
    prev=[0x5d2], succ=[0x1435, 0x149b]
    =================================
    0x140f: v140f(0x1) = CONST 
    0x1411: v1411 = SLOAD v140f(0x1)
    0x1412: v1412(0x0) = CONST 
    0x1415: v1415(0x10000000000000000000000000000000000000000) = CONST 
    0x142c: v142c = DIV v1411, v1415(0x10000000000000000000000000000000000000000)
    0x142d: v142d(0xff) = CONST 
    0x142f: v142f = AND v142d(0xff), v142c
    0x1430: v1430 = ISZERO v142f
    0x1431: v1431(0x149b) = CONST 
    0x1434: JUMPI v1431(0x149b), v1430

    Begin block 0x1435
    prev=[0x140e], succ=[]
    =================================
    0x1435: v1435(0x40) = CONST 
    0x1438: v1438 = MLOAD v1435(0x40)
    0x1439: v1439(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x145b: MSTORE v1438, v1439(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x145c: v145c(0x20) = CONST 
    0x145e: v145e(0x4) = CONST 
    0x1461: v1461 = ADD v1438, v145e(0x4)
    0x1462: MSTORE v1461, v145c(0x20)
    0x1463: v1463(0x10) = CONST 
    0x1465: v1465(0x24) = CONST 
    0x1468: v1468 = ADD v1438, v1465(0x24)
    0x1469: MSTORE v1468, v1463(0x10)
    0x146a: v146a(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0x148b: v148b(0x44) = CONST 
    0x148e: v148e = ADD v1438, v148b(0x44)
    0x148f: MSTORE v148e, v146a(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x1491: v1491 = MLOAD v1435(0x40)
    0x1495: v1495(0x0) = SUB v1438, v1491
    0x1496: v1496(0x64) = CONST 
    0x1498: v1498(0x64) = ADD v1496(0x64), v1495(0x0)
    0x149a: REVERT v1491, v1498(0x64)

    Begin block 0x149b
    prev=[0x140e], succ=[0x14b3, 0x1503]
    =================================
    0x149c: v149c = CALLER 
    0x149d: v149d(0x0) = CONST 
    0x14a1: MSTORE v149d(0x0), v149c
    0x14a2: v14a2(0xc) = CONST 
    0x14a4: v14a4(0x20) = CONST 
    0x14a6: MSTORE v14a4(0x20), v14a2(0xc)
    0x14a7: v14a7(0x40) = CONST 
    0x14aa: v14aa = SHA3 v149d(0x0), v14a7(0x40)
    0x14ab: v14ab = SLOAD v14aa
    0x14ac: v14ac(0xff) = CONST 
    0x14ae: v14ae = AND v14ac(0xff), v14ab
    0x14af: v14af(0x1503) = CONST 
    0x14b2: JUMPI v14af(0x1503), v14ae

    Begin block 0x14b3
    prev=[0x149b], succ=[]
    =================================
    0x14b3: v14b3(0x40) = CONST 
    0x14b5: v14b5 = MLOAD v14b3(0x40)
    0x14b6: v14b6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x14d8: MSTORE v14b5, v14b6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14d9: v14d9(0x4) = CONST 
    0x14db: v14db = ADD v14d9(0x4), v14b5
    0x14de: v14de(0x20) = CONST 
    0x14e0: v14e0 = ADD v14de(0x20), v14db
    0x14e3: v14e3(0x20) = SUB v14e0, v14db
    0x14e5: MSTORE v14db, v14e3(0x20)
    0x14e6: v14e6(0x21) = CONST 
    0x14e9: MSTORE v14e0, v14e6(0x21)
    0x14ea: v14ea(0x20) = CONST 
    0x14ec: v14ec = ADD v14ea(0x20), v14e0
    0x14ee: v14ee(0x2f2d) = CONST 
    0x14f1: v14f1(0x21) = CONST 
    0x14f4: CODECOPY v14ec, v14ee(0x2f2d), v14f1(0x21)
    0x14f5: v14f5(0x40) = CONST 
    0x14f7: v14f7 = ADD v14f5(0x40), v14ec
    0x14fb: v14fb(0x40) = CONST 
    0x14fd: v14fd = MLOAD v14fb(0x40)
    0x1500: v1500(0x84) = SUB v14f7, v14fd
    0x1502: REVERT v14fd, v1500(0x84)

    Begin block 0x1503
    prev=[0x149b], succ=[0x151c, 0x156c]
    =================================
    0x1504: v1504 = CALLER 
    0x1505: v1505(0x0) = CONST 
    0x1509: MSTORE v1505(0x0), v1504
    0x150a: v150a(0x3) = CONST 
    0x150c: v150c(0x20) = CONST 
    0x150e: MSTORE v150c(0x20), v150a(0x3)
    0x150f: v150f(0x40) = CONST 
    0x1512: v1512 = SHA3 v1505(0x0), v150f(0x40)
    0x1513: v1513 = SLOAD v1512
    0x1514: v1514(0xff) = CONST 
    0x1516: v1516 = AND v1514(0xff), v1513
    0x1517: v1517 = ISZERO v1516
    0x1518: v1518(0x156c) = CONST 
    0x151b: JUMPI v1518(0x156c), v1517

    Begin block 0x151c
    prev=[0x1503], succ=[]
    =================================
    0x151c: v151c(0x40) = CONST 
    0x151e: v151e = MLOAD v151c(0x40)
    0x151f: v151f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1541: MSTORE v151e, v151f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1542: v1542(0x4) = CONST 
    0x1544: v1544 = ADD v1542(0x4), v151e
    0x1547: v1547(0x20) = CONST 
    0x1549: v1549 = ADD v1547(0x20), v1544
    0x154c: v154c(0x20) = SUB v1549, v1544
    0x154e: MSTORE v1544, v154c(0x20)
    0x154f: v154f(0x25) = CONST 
    0x1552: MSTORE v1549, v154f(0x25)
    0x1553: v1553(0x20) = CONST 
    0x1555: v1555 = ADD v1553(0x20), v1549
    0x1557: v1557(0x30f0) = CONST 
    0x155a: v155a(0x25) = CONST 
    0x155d: CODECOPY v1555, v1557(0x30f0), v155a(0x25)
    0x155e: v155e(0x40) = CONST 
    0x1560: v1560 = ADD v155e(0x40), v1555
    0x1564: v1564(0x40) = CONST 
    0x1566: v1566 = MLOAD v1564(0x40)
    0x1569: v1569(0x84) = SUB v1560, v1566
    0x156b: REVERT v1566, v1569(0x84)

    Begin block 0x156c
    prev=[0x1503], succ=[0x159d, 0x15ed]
    =================================
    0x156d: v156d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1583: v1583 = AND v5eb, v156d(0xffffffffffffffffffffffffffffffffffffffff)
    0x1584: v1584(0x0) = CONST 
    0x1588: MSTORE v1584(0x0), v1583
    0x1589: v1589(0x3) = CONST 
    0x158b: v158b(0x20) = CONST 
    0x158d: MSTORE v158b(0x20), v1589(0x3)
    0x158e: v158e(0x40) = CONST 
    0x1591: v1591 = SHA3 v1584(0x0), v158e(0x40)
    0x1592: v1592 = SLOAD v1591
    0x1595: v1595(0xff) = CONST 
    0x1597: v1597 = AND v1595(0xff), v1592
    0x1598: v1598 = ISZERO v1597
    0x1599: v1599(0x15ed) = CONST 
    0x159c: JUMPI v1599(0x15ed), v1598

    Begin block 0x159d
    prev=[0x156c], succ=[]
    =================================
    0x159d: v159d(0x40) = CONST 
    0x159f: v159f = MLOAD v159d(0x40)
    0x15a0: v15a0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x15c2: MSTORE v159f, v15a0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15c3: v15c3(0x4) = CONST 
    0x15c5: v15c5 = ADD v15c3(0x4), v159f
    0x15c8: v15c8(0x20) = CONST 
    0x15ca: v15ca = ADD v15c8(0x20), v15c5
    0x15cd: v15cd(0x20) = SUB v15ca, v15c5
    0x15cf: MSTORE v15c5, v15cd(0x20)
    0x15d0: v15d0(0x25) = CONST 
    0x15d3: MSTORE v15ca, v15d0(0x25)
    0x15d4: v15d4(0x20) = CONST 
    0x15d6: v15d6 = ADD v15d4(0x20), v15ca
    0x15d8: v15d8(0x30f0) = CONST 
    0x15db: v15db(0x25) = CONST 
    0x15de: CODECOPY v15d6, v15d8(0x30f0), v15db(0x25)
    0x15df: v15df(0x40) = CONST 
    0x15e1: v15e1 = ADD v15df(0x40), v15d6
    0x15e5: v15e5(0x40) = CONST 
    0x15e7: v15e7 = MLOAD v15e5(0x40)
    0x15ea: v15ea(0x84) = SUB v15e1, v15e7
    0x15ec: REVERT v15e7, v15ea(0x84)

    Begin block 0x15ed
    prev=[0x156c], succ=[0x1609, 0x1659]
    =================================
    0x15ee: v15ee(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1604: v1604 = AND v5eb, v15ee(0xffffffffffffffffffffffffffffffffffffffff)
    0x1605: v1605(0x1659) = CONST 
    0x1608: JUMPI v1605(0x1659), v1604

    Begin block 0x1609
    prev=[0x15ed], succ=[]
    =================================
    0x1609: v1609(0x40) = CONST 
    0x160b: v160b = MLOAD v1609(0x40)
    0x160c: v160c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x162e: MSTORE v160b, v160c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x162f: v162f(0x4) = CONST 
    0x1631: v1631 = ADD v162f(0x4), v160b
    0x1634: v1634(0x20) = CONST 
    0x1636: v1636 = ADD v1634(0x20), v1631
    0x1639: v1639(0x20) = SUB v1636, v1631
    0x163b: MSTORE v1631, v1639(0x20)
    0x163c: v163c(0x23) = CONST 
    0x163f: MSTORE v1636, v163c(0x23)
    0x1640: v1640(0x20) = CONST 
    0x1642: v1642 = ADD v1640(0x20), v1636
    0x1644: v1644(0x2dcf) = CONST 
    0x1647: v1647(0x23) = CONST 
    0x164a: CODECOPY v1642, v1644(0x2dcf), v1647(0x23)
    0x164b: v164b(0x40) = CONST 
    0x164d: v164d = ADD v164b(0x40), v1642
    0x1651: v1651(0x40) = CONST 
    0x1653: v1653 = MLOAD v1651(0x40)
    0x1656: v1656(0x84) = SUB v164d, v1653
    0x1658: REVERT v1653, v1656(0x84)

    Begin block 0x1659
    prev=[0x15ed], succ=[0x1662, 0x16b2]
    =================================
    0x165a: v165a(0x0) = CONST 
    0x165d: v165d = GT v5f0, v165a(0x0)
    0x165e: v165e(0x16b2) = CONST 
    0x1661: JUMPI v165e(0x16b2), v165d

    Begin block 0x1662
    prev=[0x1659], succ=[]
    =================================
    0x1662: v1662(0x40) = CONST 
    0x1664: v1664 = MLOAD v1662(0x40)
    0x1665: v1665(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1687: MSTORE v1664, v1665(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1688: v1688(0x4) = CONST 
    0x168a: v168a = ADD v1688(0x4), v1664
    0x168d: v168d(0x20) = CONST 
    0x168f: v168f = ADD v168d(0x20), v168a
    0x1692: v1692(0x20) = SUB v168f, v168a
    0x1694: MSTORE v168a, v1692(0x20)
    0x1695: v1695(0x29) = CONST 
    0x1698: MSTORE v168f, v1695(0x29)
    0x1699: v1699(0x20) = CONST 
    0x169b: v169b = ADD v1699(0x20), v168f
    0x169d: v169d(0x2e63) = CONST 
    0x16a0: v16a0(0x29) = CONST 
    0x16a3: CODECOPY v169b, v169d(0x2e63), v16a0(0x29)
    0x16a4: v16a4(0x40) = CONST 
    0x16a6: v16a6 = ADD v16a4(0x40), v169b
    0x16aa: v16aa(0x40) = CONST 
    0x16ac: v16ac = MLOAD v16aa(0x40)
    0x16af: v16af(0x84) = SUB v16a6, v16ac
    0x16b1: REVERT v16ac, v16af(0x84)

    Begin block 0x16b2
    prev=[0x1659], succ=[0x16cb, 0x171b]
    =================================
    0x16b3: v16b3 = CALLER 
    0x16b4: v16b4(0x0) = CONST 
    0x16b8: MSTORE v16b4(0x0), v16b3
    0x16b9: v16b9(0xd) = CONST 
    0x16bb: v16bb(0x20) = CONST 
    0x16bd: MSTORE v16bb(0x20), v16b9(0xd)
    0x16be: v16be(0x40) = CONST 
    0x16c1: v16c1 = SHA3 v16b4(0x0), v16be(0x40)
    0x16c2: v16c2 = SLOAD v16c1
    0x16c5: v16c5 = GT v5f0, v16c2
    0x16c6: v16c6 = ISZERO v16c5
    0x16c7: v16c7(0x171b) = CONST 
    0x16ca: JUMPI v16c7(0x171b), v16c6

    Begin block 0x16cb
    prev=[0x16b2], succ=[]
    =================================
    0x16cb: v16cb(0x40) = CONST 
    0x16cd: v16cd = MLOAD v16cb(0x40)
    0x16ce: v16ce(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x16f0: MSTORE v16cd, v16ce(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x16f1: v16f1(0x4) = CONST 
    0x16f3: v16f3 = ADD v16f1(0x4), v16cd
    0x16f6: v16f6(0x20) = CONST 
    0x16f8: v16f8 = ADD v16f6(0x20), v16f3
    0x16fb: v16fb(0x20) = SUB v16f8, v16f3
    0x16fd: MSTORE v16f3, v16fb(0x20)
    0x16fe: v16fe(0x2e) = CONST 
    0x1701: MSTORE v16f8, v16fe(0x2e)
    0x1702: v1702(0x20) = CONST 
    0x1704: v1704 = ADD v1702(0x20), v16f8
    0x1706: v1706(0x3046) = CONST 
    0x1709: v1709(0x2e) = CONST 
    0x170c: CODECOPY v1704, v1706(0x3046), v1709(0x2e)
    0x170d: v170d(0x40) = CONST 
    0x170f: v170f = ADD v170d(0x40), v1704
    0x1713: v1713(0x40) = CONST 
    0x1715: v1715 = MLOAD v1713(0x40)
    0x1718: v1718(0x84) = SUB v170f, v1715
    0x171a: REVERT v1715, v1718(0x84)

    Begin block 0x171b
    prev=[0x16b2], succ=[0x2ba2B0x171b]
    =================================
    0x171c: v171c(0xb) = CONST 
    0x171e: v171e = SLOAD v171c(0xb)
    0x171f: v171f(0x1728) = CONST 
    0x1724: v1724(0x2ba2) = CONST 
    0x1727: JUMP v1724(0x2ba2)

    Begin block 0x2ba2B0x171b
    prev=[0x171b], succ=[0x2bb0B0x171b, 0x38dfB0x171b]
    =================================
    0x2ba3S0x171b: v2ba3V171b(0x0) = CONST 
    0x2ba7S0x171b: v2ba7V171b = ADD v5f0, v171e
    0x2baaS0x171b: v2baaV171b = LT v2ba7V171b, v171e
    0x2babS0x171b: v2babV171b = ISZERO v2baaV171b
    0x2bacS0x171b: v2bacV171b(0x38df) = CONST 
    0x2bafS0x171b: JUMPI v2bacV171b(0x38df), v2babV171b

    Begin block 0x2bb0B0x171b
    prev=[0x2ba2B0x171b], succ=[]
    =================================
    0x2bb0S0x171b: v2bb0V171b(0x40) = CONST 
    0x2bb3S0x171b: v2bb3V171b = MLOAD v2bb0V171b(0x40)
    0x2bb4S0x171b: v2bb4V171b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2bd6S0x171b: MSTORE v2bb3V171b, v2bb4V171b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2bd7S0x171b: v2bd7V171b(0x20) = CONST 
    0x2bd9S0x171b: v2bd9V171b(0x4) = CONST 
    0x2bdcS0x171b: v2bdcV171b = ADD v2bb3V171b, v2bd9V171b(0x4)
    0x2bddS0x171b: MSTORE v2bdcV171b, v2bd7V171b(0x20)
    0x2bdeS0x171b: v2bdeV171b(0x1b) = CONST 
    0x2be0S0x171b: v2be0V171b(0x24) = CONST 
    0x2be3S0x171b: v2be3V171b = ADD v2bb3V171b, v2be0V171b(0x24)
    0x2be4S0x171b: MSTORE v2be3V171b, v2bdeV171b(0x1b)
    0x2be5S0x171b: v2be5V171b(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2c06S0x171b: v2c06V171b(0x44) = CONST 
    0x2c09S0x171b: v2c09V171b = ADD v2bb3V171b, v2c06V171b(0x44)
    0x2c0aS0x171b: MSTORE v2c09V171b, v2be5V171b(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2c0cS0x171b: v2c0cV171b = MLOAD v2bb0V171b(0x40)
    0x2c10S0x171b: v2c10V171b(0x0) = SUB v2bb3V171b, v2c0cV171b
    0x2c11S0x171b: v2c11V171b(0x64) = CONST 
    0x2c13S0x171b: v2c13V171b(0x64) = ADD v2c11V171b(0x64), v2c10V171b(0x0)
    0x2c15S0x171b: REVERT v2c0cV171b, v2c13V171b(0x64)

    Begin block 0x38dfB0x171b
    prev=[0x2ba2B0x171b], succ=[0x1728]
    =================================
    0x38e5S0x171b: JUMP v171f(0x1728)

    Begin block 0x1728
    prev=[0x38dfB0x171b], succ=[0x2ba2B0x1728]
    =================================
    0x1729: v1729(0xb) = CONST 
    0x172b: SSTORE v1729(0xb), v2ba7V171b
    0x172c: v172c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1742: v1742 = AND v5eb, v172c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1743: v1743(0x0) = CONST 
    0x1747: MSTORE v1743(0x0), v1742
    0x1748: v1748(0x9) = CONST 
    0x174a: v174a(0x20) = CONST 
    0x174c: MSTORE v174a(0x20), v1748(0x9)
    0x174d: v174d(0x40) = CONST 
    0x1750: v1750 = SHA3 v1743(0x0), v174d(0x40)
    0x1751: v1751 = SLOAD v1750
    0x1752: v1752(0x175b) = CONST 
    0x1757: v1757(0x2ba2) = CONST 
    0x175a: JUMP v1757(0x2ba2)

    Begin block 0x2ba2B0x1728
    prev=[0x1728], succ=[0x2bb0B0x1728, 0x38dfB0x1728]
    =================================
    0x2ba3S0x1728: v2ba3V1728(0x0) = CONST 
    0x2ba7S0x1728: v2ba7V1728 = ADD v5f0, v1751
    0x2baaS0x1728: v2baaV1728 = LT v2ba7V1728, v1751
    0x2babS0x1728: v2babV1728 = ISZERO v2baaV1728
    0x2bacS0x1728: v2bacV1728(0x38df) = CONST 
    0x2bafS0x1728: JUMPI v2bacV1728(0x38df), v2babV1728

    Begin block 0x2bb0B0x1728
    prev=[0x2ba2B0x1728], succ=[]
    =================================
    0x2bb0S0x1728: v2bb0V1728(0x40) = CONST 
    0x2bb3S0x1728: v2bb3V1728 = MLOAD v2bb0V1728(0x40)
    0x2bb4S0x1728: v2bb4V1728(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2bd6S0x1728: MSTORE v2bb3V1728, v2bb4V1728(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2bd7S0x1728: v2bd7V1728(0x20) = CONST 
    0x2bd9S0x1728: v2bd9V1728(0x4) = CONST 
    0x2bdcS0x1728: v2bdcV1728 = ADD v2bb3V1728, v2bd9V1728(0x4)
    0x2bddS0x1728: MSTORE v2bdcV1728, v2bd7V1728(0x20)
    0x2bdeS0x1728: v2bdeV1728(0x1b) = CONST 
    0x2be0S0x1728: v2be0V1728(0x24) = CONST 
    0x2be3S0x1728: v2be3V1728 = ADD v2bb3V1728, v2be0V1728(0x24)
    0x2be4S0x1728: MSTORE v2be3V1728, v2bdeV1728(0x1b)
    0x2be5S0x1728: v2be5V1728(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2c06S0x1728: v2c06V1728(0x44) = CONST 
    0x2c09S0x1728: v2c09V1728 = ADD v2bb3V1728, v2c06V1728(0x44)
    0x2c0aS0x1728: MSTORE v2c09V1728, v2be5V1728(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x2c0cS0x1728: v2c0cV1728 = MLOAD v2bb0V1728(0x40)
    0x2c10S0x1728: v2c10V1728(0x0) = SUB v2bb3V1728, v2c0cV1728
    0x2c11S0x1728: v2c11V1728(0x64) = CONST 
    0x2c13S0x1728: v2c13V1728(0x64) = ADD v2c11V1728(0x64), v2c10V1728(0x0)
    0x2c15S0x1728: REVERT v2c0cV1728, v2c13V1728(0x64)

    Begin block 0x38dfB0x1728
    prev=[0x2ba2B0x1728], succ=[0x175b]
    =================================
    0x38e5S0x1728: JUMP v1752(0x175b)

    Begin block 0x175b
    prev=[0x38dfB0x1728], succ=[0x178b]
    =================================
    0x175c: v175c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1772: v1772 = AND v5eb, v175c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1773: v1773(0x0) = CONST 
    0x1777: MSTORE v1773(0x0), v1772
    0x1778: v1778(0x9) = CONST 
    0x177a: v177a(0x20) = CONST 
    0x177c: MSTORE v177a(0x20), v1778(0x9)
    0x177d: v177d(0x40) = CONST 
    0x1780: v1780 = SHA3 v1773(0x0), v177d(0x40)
    0x1781: SSTORE v1780, v2ba7V1728
    0x1782: v1782(0x178b) = CONST 
    0x1787: v1787(0x2b12) = CONST 
    0x178a: v178a_0 = CALLPRIVATE v1787(0x2b12), v5f0, v16c2, v1782(0x178b)

    Begin block 0x178b
    prev=[0x175b], succ=[0x33f7]
    =================================
    0x178c: v178c = CALLER 
    0x178d: v178d(0x0) = CONST 
    0x1791: MSTORE v178d(0x0), v178c
    0x1792: v1792(0xd) = CONST 
    0x1794: v1794(0x20) = CONST 
    0x1798: MSTORE v1794(0x20), v1792(0xd)
    0x1799: v1799(0x40) = CONST 
    0x179e: v179e = SHA3 v178d(0x0), v1799(0x40)
    0x17a2: SSTORE v179e, v178a_0
    0x17a4: v17a4 = MLOAD v1799(0x40)
    0x17a7: MSTORE v17a4, v5f0
    0x17a9: v17a9 = MLOAD v1799(0x40)
    0x17aa: v17aa(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17c0: v17c0 = AND v5eb, v17aa(0xffffffffffffffffffffffffffffffffffffffff)
    0x17c2: v17c2(0xab8530f87dc9b59234c4623bf917212bb2536d647574c8e7e5da92c2ede0c9f8) = CONST 
    0x17e6: v17e6(0x0) = SUB v17a4, v17a9
    0x17e7: v17e7(0x20) = ADD v17e6(0x0), v1794(0x20)
    0x17e9: LOG3 v17a9, v17e7(0x20), v17c2(0xab8530f87dc9b59234c4623bf917212bb2536d647574c8e7e5da92c2ede0c9f8), v178c, v17c0
    0x17ea: v17ea(0x40) = CONST 
    0x17ed: v17ed = MLOAD v17ea(0x40)
    0x17f0: MSTORE v17ed, v5f0
    0x17f2: v17f2 = MLOAD v17ea(0x40)
    0x17f3: v17f3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1809: v1809 = AND v5eb, v17f3(0xffffffffffffffffffffffffffffffffffffffff)
    0x180b: v180b(0x0) = CONST 
    0x180e: v180e(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1832: v1832(0x0) = SUB v17ed, v17f2
    0x1833: v1833(0x20) = CONST 
    0x1835: v1835(0x20) = ADD v1833(0x20), v1832(0x0)
    0x1837: LOG3 v17f2, v1835(0x20), v180e(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v180b(0x0), v1809
    0x1839: v1839(0x1) = CONST 
    0x1842: JUMP v5bd(0x33f7)

    Begin block 0x33f7
    prev=[0x178b], succ=[]
    =================================
    0x33f8: v33f8(0x40) = CONST 
    0x33fb: v33fb = MLOAD v33f8(0x40)
    0x33fd: v33fd = ISZERO v1839(0x1)
    0x33fe: v33fe = ISZERO v33fd
    0x3400: MSTORE v33fb, v33fe
    0x3401: v3401 = MLOAD v33f8(0x40)
    0x3405: v3405(0x0) = SUB v33fb, v3401
    0x3406: v3406(0x20) = CONST 
    0x3408: v3408(0x20) = ADD v3406(0x20), v3405(0x0)
    0x340a: RETURN v3401, v3408(0x20)

}

function burn(uint256)() public {
    Begin block 0x5f5
    prev=[], succ=[0x607, 0x60b]
    =================================
    0x5f6: v5f6(0x342a) = CONST 
    0x5f9: v5f9(0x4) = CONST 
    0x5fc: v5fc = CALLDATASIZE 
    0x5fd: v5fd = SUB v5fc, v5f9(0x4)
    0x5fe: v5fe(0x20) = CONST 
    0x601: v601 = LT v5fd, v5fe(0x20)
    0x602: v602 = ISZERO v601
    0x603: v603(0x60b) = CONST 
    0x606: JUMPI v603(0x60b), v602

    Begin block 0x607
    prev=[0x5f5], succ=[]
    =================================
    0x607: v607(0x0) = CONST 
    0x60a: REVERT v607(0x0), v607(0x0)

    Begin block 0x60b
    prev=[0x5f5], succ=[0x1843]
    =================================
    0x60d: v60d = CALLDATALOAD v5f9(0x4)
    0x60e: v60e(0x1843) = CONST 
    0x611: JUMP v60e(0x1843)

    Begin block 0x1843
    prev=[0x60b], succ=[0x1867, 0x18cd]
    =================================
    0x1844: v1844(0x1) = CONST 
    0x1846: v1846 = SLOAD v1844(0x1)
    0x1847: v1847(0x10000000000000000000000000000000000000000) = CONST 
    0x185e: v185e = DIV v1846, v1847(0x10000000000000000000000000000000000000000)
    0x185f: v185f(0xff) = CONST 
    0x1861: v1861 = AND v185f(0xff), v185e
    0x1862: v1862 = ISZERO v1861
    0x1863: v1863(0x18cd) = CONST 
    0x1866: JUMPI v1863(0x18cd), v1862

    Begin block 0x1867
    prev=[0x1843], succ=[]
    =================================
    0x1867: v1867(0x40) = CONST 
    0x186a: v186a = MLOAD v1867(0x40)
    0x186b: v186b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x188d: MSTORE v186a, v186b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x188e: v188e(0x20) = CONST 
    0x1890: v1890(0x4) = CONST 
    0x1893: v1893 = ADD v186a, v1890(0x4)
    0x1894: MSTORE v1893, v188e(0x20)
    0x1895: v1895(0x10) = CONST 
    0x1897: v1897(0x24) = CONST 
    0x189a: v189a = ADD v186a, v1897(0x24)
    0x189b: MSTORE v189a, v1895(0x10)
    0x189c: v189c(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0x18bd: v18bd(0x44) = CONST 
    0x18c0: v18c0 = ADD v186a, v18bd(0x44)
    0x18c1: MSTORE v18c0, v189c(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x18c3: v18c3 = MLOAD v1867(0x40)
    0x18c7: v18c7(0x0) = SUB v186a, v18c3
    0x18c8: v18c8(0x64) = CONST 
    0x18ca: v18ca(0x64) = ADD v18c8(0x64), v18c7(0x0)
    0x18cc: REVERT v18c3, v18ca(0x64)

    Begin block 0x18cd
    prev=[0x1843], succ=[0x18e5, 0x1935]
    =================================
    0x18ce: v18ce = CALLER 
    0x18cf: v18cf(0x0) = CONST 
    0x18d3: MSTORE v18cf(0x0), v18ce
    0x18d4: v18d4(0xc) = CONST 
    0x18d6: v18d6(0x20) = CONST 
    0x18d8: MSTORE v18d6(0x20), v18d4(0xc)
    0x18d9: v18d9(0x40) = CONST 
    0x18dc: v18dc = SHA3 v18cf(0x0), v18d9(0x40)
    0x18dd: v18dd = SLOAD v18dc
    0x18de: v18de(0xff) = CONST 
    0x18e0: v18e0 = AND v18de(0xff), v18dd
    0x18e1: v18e1(0x1935) = CONST 
    0x18e4: JUMPI v18e1(0x1935), v18e0

    Begin block 0x18e5
    prev=[0x18cd], succ=[]
    =================================
    0x18e5: v18e5(0x40) = CONST 
    0x18e7: v18e7 = MLOAD v18e5(0x40)
    0x18e8: v18e8(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x190a: MSTORE v18e7, v18e8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x190b: v190b(0x4) = CONST 
    0x190d: v190d = ADD v190b(0x4), v18e7
    0x1910: v1910(0x20) = CONST 
    0x1912: v1912 = ADD v1910(0x20), v190d
    0x1915: v1915(0x20) = SUB v1912, v190d
    0x1917: MSTORE v190d, v1915(0x20)
    0x1918: v1918(0x21) = CONST 
    0x191b: MSTORE v1912, v1918(0x21)
    0x191c: v191c(0x20) = CONST 
    0x191e: v191e = ADD v191c(0x20), v1912
    0x1920: v1920(0x2f2d) = CONST 
    0x1923: v1923(0x21) = CONST 
    0x1926: CODECOPY v191e, v1920(0x2f2d), v1923(0x21)
    0x1927: v1927(0x40) = CONST 
    0x1929: v1929 = ADD v1927(0x40), v191e
    0x192d: v192d(0x40) = CONST 
    0x192f: v192f = MLOAD v192d(0x40)
    0x1932: v1932(0x84) = SUB v1929, v192f
    0x1934: REVERT v192f, v1932(0x84)

    Begin block 0x1935
    prev=[0x18cd], succ=[0x194e, 0x199e]
    =================================
    0x1936: v1936 = CALLER 
    0x1937: v1937(0x0) = CONST 
    0x193b: MSTORE v1937(0x0), v1936
    0x193c: v193c(0x3) = CONST 
    0x193e: v193e(0x20) = CONST 
    0x1940: MSTORE v193e(0x20), v193c(0x3)
    0x1941: v1941(0x40) = CONST 
    0x1944: v1944 = SHA3 v1937(0x0), v1941(0x40)
    0x1945: v1945 = SLOAD v1944
    0x1946: v1946(0xff) = CONST 
    0x1948: v1948 = AND v1946(0xff), v1945
    0x1949: v1949 = ISZERO v1948
    0x194a: v194a(0x199e) = CONST 
    0x194d: JUMPI v194a(0x199e), v1949

    Begin block 0x194e
    prev=[0x1935], succ=[]
    =================================
    0x194e: v194e(0x40) = CONST 
    0x1950: v1950 = MLOAD v194e(0x40)
    0x1951: v1951(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1973: MSTORE v1950, v1951(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1974: v1974(0x4) = CONST 
    0x1976: v1976 = ADD v1974(0x4), v1950
    0x1979: v1979(0x20) = CONST 
    0x197b: v197b = ADD v1979(0x20), v1976
    0x197e: v197e(0x20) = SUB v197b, v1976
    0x1980: MSTORE v1976, v197e(0x20)
    0x1981: v1981(0x25) = CONST 
    0x1984: MSTORE v197b, v1981(0x25)
    0x1985: v1985(0x20) = CONST 
    0x1987: v1987 = ADD v1985(0x20), v197b
    0x1989: v1989(0x30f0) = CONST 
    0x198c: v198c(0x25) = CONST 
    0x198f: CODECOPY v1987, v1989(0x30f0), v198c(0x25)
    0x1990: v1990(0x40) = CONST 
    0x1992: v1992 = ADD v1990(0x40), v1987
    0x1996: v1996(0x40) = CONST 
    0x1998: v1998 = MLOAD v1996(0x40)
    0x199b: v199b(0x84) = SUB v1992, v1998
    0x199d: REVERT v1998, v199b(0x84)

    Begin block 0x199e
    prev=[0x1935], succ=[0x19b4, 0x1a04]
    =================================
    0x199f: v199f = CALLER 
    0x19a0: v19a0(0x0) = CONST 
    0x19a4: MSTORE v19a0(0x0), v199f
    0x19a5: v19a5(0x9) = CONST 
    0x19a7: v19a7(0x20) = CONST 
    0x19a9: MSTORE v19a7(0x20), v19a5(0x9)
    0x19aa: v19aa(0x40) = CONST 
    0x19ad: v19ad = SHA3 v19a0(0x0), v19aa(0x40)
    0x19ae: v19ae = SLOAD v19ad
    0x19b0: v19b0(0x1a04) = CONST 
    0x19b3: JUMPI v19b0(0x1a04), v60d

    Begin block 0x19b4
    prev=[0x199e], succ=[]
    =================================
    0x19b4: v19b4(0x40) = CONST 
    0x19b6: v19b6 = MLOAD v19b4(0x40)
    0x19b7: v19b7(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x19d9: MSTORE v19b6, v19b7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19da: v19da(0x4) = CONST 
    0x19dc: v19dc = ADD v19da(0x4), v19b6
    0x19df: v19df(0x20) = CONST 
    0x19e1: v19e1 = ADD v19df(0x20), v19dc
    0x19e4: v19e4(0x20) = SUB v19e1, v19dc
    0x19e6: MSTORE v19dc, v19e4(0x20)
    0x19e7: v19e7(0x29) = CONST 
    0x19ea: MSTORE v19e1, v19e7(0x29)
    0x19eb: v19eb(0x20) = CONST 
    0x19ed: v19ed = ADD v19eb(0x20), v19e1
    0x19ef: v19ef(0x2da6) = CONST 
    0x19f2: v19f2(0x29) = CONST 
    0x19f5: CODECOPY v19ed, v19ef(0x2da6), v19f2(0x29)
    0x19f6: v19f6(0x40) = CONST 
    0x19f8: v19f8 = ADD v19f6(0x40), v19ed
    0x19fc: v19fc(0x40) = CONST 
    0x19fe: v19fe = MLOAD v19fc(0x40)
    0x1a01: v1a01(0x84) = SUB v19f8, v19fe
    0x1a03: REVERT v19fe, v1a01(0x84)

    Begin block 0x1a04
    prev=[0x199e], succ=[0x1a0d, 0x1a5d]
    =================================
    0x1a07: v1a07 = LT v19ae, v60d
    0x1a08: v1a08 = ISZERO v1a07
    0x1a09: v1a09(0x1a5d) = CONST 
    0x1a0c: JUMPI v1a09(0x1a5d), v1a08

    Begin block 0x1a0d
    prev=[0x1a04], succ=[]
    =================================
    0x1a0d: v1a0d(0x40) = CONST 
    0x1a0f: v1a0f = MLOAD v1a0d(0x40)
    0x1a10: v1a10(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1a32: MSTORE v1a0f, v1a10(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a33: v1a33(0x4) = CONST 
    0x1a35: v1a35 = ADD v1a33(0x4), v1a0f
    0x1a38: v1a38(0x20) = CONST 
    0x1a3a: v1a3a = ADD v1a38(0x20), v1a35
    0x1a3d: v1a3d(0x20) = SUB v1a3a, v1a35
    0x1a3f: MSTORE v1a35, v1a3d(0x20)
    0x1a40: v1a40(0x26) = CONST 
    0x1a43: MSTORE v1a3a, v1a40(0x26)
    0x1a44: v1a44(0x20) = CONST 
    0x1a46: v1a46 = ADD v1a44(0x20), v1a3a
    0x1a48: v1a48(0x2f07) = CONST 
    0x1a4b: v1a4b(0x26) = CONST 
    0x1a4e: CODECOPY v1a46, v1a48(0x2f07), v1a4b(0x26)
    0x1a4f: v1a4f(0x40) = CONST 
    0x1a51: v1a51 = ADD v1a4f(0x40), v1a46
    0x1a55: v1a55(0x40) = CONST 
    0x1a57: v1a57 = MLOAD v1a55(0x40)
    0x1a5a: v1a5a(0x84) = SUB v1a51, v1a57
    0x1a5c: REVERT v1a57, v1a5a(0x84)

    Begin block 0x1a5d
    prev=[0x1a04], succ=[0x1a6a]
    =================================
    0x1a5e: v1a5e(0xb) = CONST 
    0x1a60: v1a60 = SLOAD v1a5e(0xb)
    0x1a61: v1a61(0x1a6a) = CONST 
    0x1a66: v1a66(0x2b12) = CONST 
    0x1a69: v1a69_0 = CALLPRIVATE v1a66(0x2b12), v60d, v1a60, v1a61(0x1a6a)

    Begin block 0x1a6a
    prev=[0x1a5d], succ=[0x1a77]
    =================================
    0x1a6b: v1a6b(0xb) = CONST 
    0x1a6d: SSTORE v1a6b(0xb), v1a69_0
    0x1a6e: v1a6e(0x1a77) = CONST 
    0x1a73: v1a73(0x2b12) = CONST 
    0x1a76: v1a76_0 = CALLPRIVATE v1a73(0x2b12), v60d, v19ae, v1a6e(0x1a77)

    Begin block 0x1a77
    prev=[0x1a6a], succ=[0x342a]
    =================================
    0x1a78: v1a78 = CALLER 
    0x1a79: v1a79(0x0) = CONST 
    0x1a7d: MSTORE v1a79(0x0), v1a78
    0x1a7e: v1a7e(0x9) = CONST 
    0x1a80: v1a80(0x20) = CONST 
    0x1a84: MSTORE v1a80(0x20), v1a7e(0x9)
    0x1a85: v1a85(0x40) = CONST 
    0x1a8a: v1a8a = SHA3 v1a79(0x0), v1a85(0x40)
    0x1a8e: SSTORE v1a8a, v1a76_0
    0x1a90: v1a90 = MLOAD v1a85(0x40)
    0x1a93: MSTORE v1a90, v60d
    0x1a95: v1a95 = MLOAD v1a85(0x40)
    0x1a98: v1a98(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5) = CONST 
    0x1abd: v1abd(0x0) = SUB v1a90, v1a95
    0x1abe: v1abe(0x20) = ADD v1abd(0x0), v1a80(0x20)
    0x1ac0: LOG2 v1a95, v1abe(0x20), v1a98(0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5), v1a78
    0x1ac1: v1ac1(0x40) = CONST 
    0x1ac4: v1ac4 = MLOAD v1ac1(0x40)
    0x1ac7: MSTORE v1ac4, v60d
    0x1ac9: v1ac9 = MLOAD v1ac1(0x40)
    0x1aca: v1aca(0x0) = CONST 
    0x1acd: v1acd = CALLER 
    0x1acf: v1acf(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef) = CONST 
    0x1af3: v1af3(0x0) = SUB v1ac4, v1ac9
    0x1af4: v1af4(0x20) = CONST 
    0x1af6: v1af6(0x20) = ADD v1af4(0x20), v1af3(0x0)
    0x1af8: LOG3 v1ac9, v1af6(0x20), v1acf(0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef), v1acd, v1aca(0x0)
    0x1afc: JUMP v5f6(0x342a)

    Begin block 0x342a
    prev=[0x1a77], succ=[]
    =================================
    0x342b: STOP 

}

function configureMinter(address,uint256)() public {
    Begin block 0x612
    prev=[], succ=[0x624, 0x628]
    =================================
    0x613: v613(0x344b) = CONST 
    0x616: v616(0x4) = CONST 
    0x619: v619 = CALLDATASIZE 
    0x61a: v61a = SUB v619, v616(0x4)
    0x61b: v61b(0x40) = CONST 
    0x61e: v61e = LT v61a, v61b(0x40)
    0x61f: v61f = ISZERO v61e
    0x620: v620(0x628) = CONST 
    0x623: JUMPI v620(0x628), v61f

    Begin block 0x624
    prev=[0x612], succ=[]
    =================================
    0x624: v624(0x0) = CONST 
    0x627: REVERT v624(0x0), v624(0x0)

    Begin block 0x628
    prev=[0x612], succ=[0x1afd]
    =================================
    0x62a: v62a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x640: v640 = CALLDATALOAD v616(0x4)
    0x641: v641 = AND v640, v62a(0xffffffffffffffffffffffffffffffffffffffff)
    0x643: v643(0x20) = CONST 
    0x645: v645(0x24) = ADD v643(0x20), v616(0x4)
    0x646: v646 = CALLDATALOAD v645(0x24)
    0x647: v647(0x1afd) = CONST 
    0x64a: JUMP v647(0x1afd)

    Begin block 0x1afd
    prev=[0x628], succ=[0x1b24, 0x1b8a]
    =================================
    0x1afe: v1afe(0x1) = CONST 
    0x1b00: v1b00 = SLOAD v1afe(0x1)
    0x1b01: v1b01(0x0) = CONST 
    0x1b04: v1b04(0x10000000000000000000000000000000000000000) = CONST 
    0x1b1b: v1b1b = DIV v1b00, v1b04(0x10000000000000000000000000000000000000000)
    0x1b1c: v1b1c(0xff) = CONST 
    0x1b1e: v1b1e = AND v1b1c(0xff), v1b1b
    0x1b1f: v1b1f = ISZERO v1b1e
    0x1b20: v1b20(0x1b8a) = CONST 
    0x1b23: JUMPI v1b20(0x1b8a), v1b1f

    Begin block 0x1b24
    prev=[0x1afd], succ=[]
    =================================
    0x1b24: v1b24(0x40) = CONST 
    0x1b27: v1b27 = MLOAD v1b24(0x40)
    0x1b28: v1b28(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1b4a: MSTORE v1b27, v1b28(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b4b: v1b4b(0x20) = CONST 
    0x1b4d: v1b4d(0x4) = CONST 
    0x1b50: v1b50 = ADD v1b27, v1b4d(0x4)
    0x1b51: MSTORE v1b50, v1b4b(0x20)
    0x1b52: v1b52(0x10) = CONST 
    0x1b54: v1b54(0x24) = CONST 
    0x1b57: v1b57 = ADD v1b27, v1b54(0x24)
    0x1b58: MSTORE v1b57, v1b52(0x10)
    0x1b59: v1b59(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0x1b7a: v1b7a(0x44) = CONST 
    0x1b7d: v1b7d = ADD v1b27, v1b7a(0x44)
    0x1b7e: MSTORE v1b7d, v1b59(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x1b80: v1b80 = MLOAD v1b24(0x40)
    0x1b84: v1b84(0x0) = SUB v1b27, v1b80
    0x1b85: v1b85(0x64) = CONST 
    0x1b87: v1b87(0x64) = ADD v1b85(0x64), v1b84(0x0)
    0x1b89: REVERT v1b80, v1b87(0x64)

    Begin block 0x1b8a
    prev=[0x1afd], succ=[0x1baa, 0x1bfa]
    =================================
    0x1b8b: v1b8b(0x8) = CONST 
    0x1b8d: v1b8d = SLOAD v1b8b(0x8)
    0x1b8e: v1b8e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ba3: v1ba3 = AND v1b8e(0xffffffffffffffffffffffffffffffffffffffff), v1b8d
    0x1ba4: v1ba4 = CALLER 
    0x1ba5: v1ba5 = EQ v1ba4, v1ba3
    0x1ba6: v1ba6(0x1bfa) = CONST 
    0x1ba9: JUMPI v1ba6(0x1bfa), v1ba5

    Begin block 0x1baa
    prev=[0x1b8a], succ=[]
    =================================
    0x1baa: v1baa(0x40) = CONST 
    0x1bac: v1bac = MLOAD v1baa(0x40)
    0x1bad: v1bad(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1bcf: MSTORE v1bac, v1bad(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1bd0: v1bd0(0x4) = CONST 
    0x1bd2: v1bd2 = ADD v1bd0(0x4), v1bac
    0x1bd5: v1bd5(0x20) = CONST 
    0x1bd7: v1bd7 = ADD v1bd5(0x20), v1bd2
    0x1bda: v1bda(0x20) = SUB v1bd7, v1bd2
    0x1bdc: MSTORE v1bd2, v1bda(0x20)
    0x1bdd: v1bdd(0x29) = CONST 
    0x1be0: MSTORE v1bd7, v1bdd(0x29)
    0x1be1: v1be1(0x20) = CONST 
    0x1be3: v1be3 = ADD v1be1(0x20), v1bd7
    0x1be5: v1be5(0x2eb2) = CONST 
    0x1be8: v1be8(0x29) = CONST 
    0x1beb: CODECOPY v1be3, v1be5(0x2eb2), v1be8(0x29)
    0x1bec: v1bec(0x40) = CONST 
    0x1bee: v1bee = ADD v1bec(0x40), v1be3
    0x1bf2: v1bf2(0x40) = CONST 
    0x1bf4: v1bf4 = MLOAD v1bf2(0x40)
    0x1bf7: v1bf7(0x84) = SUB v1bee, v1bf4
    0x1bf9: REVERT v1bf4, v1bf7(0x84)

    Begin block 0x1bfa
    prev=[0x1b8a], succ=[0x344b]
    =================================
    0x1bfb: v1bfb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c11: v1c11 = AND v641, v1bfb(0xffffffffffffffffffffffffffffffffffffffff)
    0x1c12: v1c12(0x0) = CONST 
    0x1c16: MSTORE v1c12(0x0), v1c11
    0x1c17: v1c17(0xc) = CONST 
    0x1c19: v1c19(0x20) = CONST 
    0x1c1d: MSTORE v1c19(0x20), v1c17(0xc)
    0x1c1e: v1c1e(0x40) = CONST 
    0x1c22: v1c22 = SHA3 v1c12(0x0), v1c1e(0x40)
    0x1c24: v1c24 = SLOAD v1c22
    0x1c25: v1c25(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x1c46: v1c46 = AND v1c25(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1c24
    0x1c47: v1c47(0x1) = CONST 
    0x1c49: v1c49 = OR v1c47(0x1), v1c46
    0x1c4b: SSTORE v1c22, v1c49
    0x1c4c: v1c4c(0xd) = CONST 
    0x1c4f: MSTORE v1c19(0x20), v1c4c(0xd)
    0x1c53: v1c53 = SHA3 v1c12(0x0), v1c1e(0x40)
    0x1c56: SSTORE v1c53, v646
    0x1c58: v1c58 = MLOAD v1c1e(0x40)
    0x1c5b: MSTORE v1c58, v646
    0x1c5d: v1c5d = MLOAD v1c1e(0x40)
    0x1c5e: v1c5e(0x46980fca912ef9bcdbd36877427b6b90e860769f604e89c0e67720cece530d20) = CONST 
    0x1c82: v1c82(0x0) = SUB v1c58, v1c5d
    0x1c85: v1c85(0x20) = ADD v1c19(0x20), v1c82(0x0)
    0x1c87: LOG2 v1c5d, v1c85(0x20), v1c5e(0x46980fca912ef9bcdbd36877427b6b90e860769f604e89c0e67720cece530d20), v1c11
    0x1c89: v1c89(0x1) = CONST 
    0x1c8f: JUMP v613(0x344b)

    Begin block 0x344b
    prev=[0x1bfa], succ=[]
    =================================
    0x344c: v344c(0x40) = CONST 
    0x344f: v344f = MLOAD v344c(0x40)
    0x3451: v3451 = ISZERO v1c89(0x1)
    0x3452: v3452 = ISZERO v3451
    0x3454: MSTORE v344f, v3452
    0x3455: v3455 = MLOAD v344c(0x40)
    0x3459: v3459(0x0) = SUB v344f, v3455
    0x345a: v345a(0x20) = CONST 
    0x345c: v345c(0x20) = ADD v345a(0x20), v3459(0x0)
    0x345e: RETURN v3455, v345c(0x20)

}

function updatePauser(address)() public {
    Begin block 0x64b
    prev=[], succ=[0x65d, 0x661]
    =================================
    0x64c: v64c(0x347e) = CONST 
    0x64f: v64f(0x4) = CONST 
    0x652: v652 = CALLDATASIZE 
    0x653: v653 = SUB v652, v64f(0x4)
    0x654: v654(0x20) = CONST 
    0x657: v657 = LT v653, v654(0x20)
    0x658: v658 = ISZERO v657
    0x659: v659(0x661) = CONST 
    0x65c: JUMPI v659(0x661), v658

    Begin block 0x65d
    prev=[0x64b], succ=[]
    =================================
    0x65d: v65d(0x0) = CONST 
    0x660: REVERT v65d(0x0), v65d(0x0)

    Begin block 0x661
    prev=[0x64b], succ=[0x1c90]
    =================================
    0x663: v663 = CALLDATALOAD v64f(0x4)
    0x664: v664(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x679: v679 = AND v664(0xffffffffffffffffffffffffffffffffffffffff), v663
    0x67a: v67a(0x1c90) = CONST 
    0x67d: JUMP v67a(0x1c90)

    Begin block 0x1c90
    prev=[0x661], succ=[0x1cb0, 0x1d16]
    =================================
    0x1c91: v1c91(0x0) = CONST 
    0x1c93: v1c93 = SLOAD v1c91(0x0)
    0x1c94: v1c94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ca9: v1ca9 = AND v1c94(0xffffffffffffffffffffffffffffffffffffffff), v1c93
    0x1caa: v1caa = CALLER 
    0x1cab: v1cab = EQ v1caa, v1ca9
    0x1cac: v1cac(0x1d16) = CONST 
    0x1caf: JUMPI v1cac(0x1d16), v1cab

    Begin block 0x1cb0
    prev=[0x1c90], succ=[]
    =================================
    0x1cb0: v1cb0(0x40) = CONST 
    0x1cb3: v1cb3 = MLOAD v1cb0(0x40)
    0x1cb4: v1cb4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1cd6: MSTORE v1cb3, v1cb4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cd7: v1cd7(0x20) = CONST 
    0x1cd9: v1cd9(0x4) = CONST 
    0x1cdc: v1cdc = ADD v1cb3, v1cd9(0x4)
    0x1cdf: MSTORE v1cdc, v1cd7(0x20)
    0x1ce0: v1ce0(0x24) = CONST 
    0x1ce3: v1ce3 = ADD v1cb3, v1ce0(0x24)
    0x1ce4: MSTORE v1ce3, v1cd7(0x20)
    0x1ce5: v1ce5(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x1d06: v1d06(0x44) = CONST 
    0x1d09: v1d09 = ADD v1cb3, v1d06(0x44)
    0x1d0a: MSTORE v1d09, v1ce5(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x1d0c: v1d0c = MLOAD v1cb0(0x40)
    0x1d10: v1d10(0x0) = SUB v1cb3, v1d0c
    0x1d11: v1d11(0x64) = CONST 
    0x1d13: v1d13(0x64) = ADD v1d11(0x64), v1d10(0x0)
    0x1d15: REVERT v1d0c, v1d13(0x64)

    Begin block 0x1d16
    prev=[0x1c90], succ=[0x1d32, 0x1d82]
    =================================
    0x1d17: v1d17(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d2d: v1d2d = AND v679, v1d17(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d2e: v1d2e(0x1d82) = CONST 
    0x1d31: JUMPI v1d2e(0x1d82), v1d2d

    Begin block 0x1d32
    prev=[0x1d16], succ=[]
    =================================
    0x1d32: v1d32(0x40) = CONST 
    0x1d34: v1d34 = MLOAD v1d32(0x40)
    0x1d35: v1d35(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d57: MSTORE v1d34, v1d35(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d58: v1d58(0x4) = CONST 
    0x1d5a: v1d5a = ADD v1d58(0x4), v1d34
    0x1d5d: v1d5d(0x20) = CONST 
    0x1d5f: v1d5f = ADD v1d5d(0x20), v1d5a
    0x1d62: v1d62(0x20) = SUB v1d5f, v1d5a
    0x1d64: MSTORE v1d5a, v1d62(0x20)
    0x1d65: v1d65(0x28) = CONST 
    0x1d68: MSTORE v1d5f, v1d65(0x28)
    0x1d69: v1d69(0x20) = CONST 
    0x1d6b: v1d6b = ADD v1d69(0x20), v1d5f
    0x1d6d: v1d6d(0x2d7e) = CONST 
    0x1d70: v1d70(0x28) = CONST 
    0x1d73: CODECOPY v1d6b, v1d6d(0x2d7e), v1d70(0x28)
    0x1d74: v1d74(0x40) = CONST 
    0x1d76: v1d76 = ADD v1d74(0x40), v1d6b
    0x1d7a: v1d7a(0x40) = CONST 
    0x1d7c: v1d7c = MLOAD v1d7a(0x40)
    0x1d7f: v1d7f(0x84) = SUB v1d76, v1d7c
    0x1d81: REVERT v1d7c, v1d7f(0x84)

    Begin block 0x1d82
    prev=[0x1d16], succ=[0x347e]
    =================================
    0x1d83: v1d83(0x1) = CONST 
    0x1d86: v1d86 = SLOAD v1d83(0x1)
    0x1d87: v1d87(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1da8: v1da8 = AND v1d87(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1d86
    0x1da9: v1da9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dc0: v1dc0 = AND v1da9(0xffffffffffffffffffffffffffffffffffffffff), v679
    0x1dc4: v1dc4 = OR v1dc0, v1da8
    0x1dc8: SSTORE v1d83(0x1), v1dc4
    0x1dc9: v1dc9(0x40) = CONST 
    0x1dcb: v1dcb = MLOAD v1dc9(0x40)
    0x1dcd: v1dcd = AND v1dc4, v1da9(0xffffffffffffffffffffffffffffffffffffffff)
    0x1dcf: v1dcf(0xb80482a293ca2e013eda8683c9bd7fc8347cfdaeea5ede58cba46df502c2a604) = CONST 
    0x1df1: v1df1(0x0) = CONST 
    0x1df4: LOG2 v1dcb, v1df1(0x0), v1dcf(0xb80482a293ca2e013eda8683c9bd7fc8347cfdaeea5ede58cba46df502c2a604), v1dcd
    0x1df6: JUMP v64c(0x347e)

    Begin block 0x347e
    prev=[0x1d82], succ=[]
    =================================
    0x347f: STOP 

}

function paused()() public {
    Begin block 0x67e
    prev=[], succ=[0x1df7]
    =================================
    0x67f: v67f(0x349f) = CONST 
    0x682: v682(0x1df7) = CONST 
    0x685: JUMP v682(0x1df7)

    Begin block 0x1df7
    prev=[0x67e], succ=[0x349f]
    =================================
    0x1df8: v1df8(0x1) = CONST 
    0x1dfa: v1dfa = SLOAD v1df8(0x1)
    0x1dfb: v1dfb(0x10000000000000000000000000000000000000000) = CONST 
    0x1e12: v1e12 = DIV v1dfa, v1dfb(0x10000000000000000000000000000000000000000)
    0x1e13: v1e13(0xff) = CONST 
    0x1e15: v1e15 = AND v1e13(0xff), v1e12
    0x1e17: JUMP v67f(0x349f)

    Begin block 0x349f
    prev=[0x1df7], succ=[]
    =================================
    0x34a0: v34a0(0x40) = CONST 
    0x34a3: v34a3 = MLOAD v34a0(0x40)
    0x34a5: v34a5 = ISZERO v1e15
    0x34a6: v34a6 = ISZERO v34a5
    0x34a8: MSTORE v34a3, v34a6
    0x34a9: v34a9 = MLOAD v34a0(0x40)
    0x34ad: v34ad(0x0) = SUB v34a3, v34a9
    0x34ae: v34ae(0x20) = CONST 
    0x34b0: v34b0(0x20) = ADD v34ae(0x20), v34ad(0x0)
    0x34b2: RETURN v34a9, v34b0(0x20)

}

function balanceOf(address)() public {
    Begin block 0x686
    prev=[], succ=[0x698, 0x69c]
    =================================
    0x687: v687(0x34d2) = CONST 
    0x68a: v68a(0x4) = CONST 
    0x68d: v68d = CALLDATASIZE 
    0x68e: v68e = SUB v68d, v68a(0x4)
    0x68f: v68f(0x20) = CONST 
    0x692: v692 = LT v68e, v68f(0x20)
    0x693: v693 = ISZERO v692
    0x694: v694(0x69c) = CONST 
    0x697: JUMPI v694(0x69c), v693

    Begin block 0x698
    prev=[0x686], succ=[]
    =================================
    0x698: v698(0x0) = CONST 
    0x69b: REVERT v698(0x0), v698(0x0)

    Begin block 0x69c
    prev=[0x686], succ=[0x1e18]
    =================================
    0x69e: v69e = CALLDATALOAD v68a(0x4)
    0x69f: v69f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6b4: v6b4 = AND v69f(0xffffffffffffffffffffffffffffffffffffffff), v69e
    0x6b5: v6b5(0x1e18) = CONST 
    0x6b8: JUMP v6b5(0x1e18)

    Begin block 0x1e18
    prev=[0x69c], succ=[0x34d2]
    =================================
    0x1e19: v1e19(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e2e: v1e2e = AND v1e19(0xffffffffffffffffffffffffffffffffffffffff), v6b4
    0x1e2f: v1e2f(0x0) = CONST 
    0x1e33: MSTORE v1e2f(0x0), v1e2e
    0x1e34: v1e34(0x9) = CONST 
    0x1e36: v1e36(0x20) = CONST 
    0x1e38: MSTORE v1e36(0x20), v1e34(0x9)
    0x1e39: v1e39(0x40) = CONST 
    0x1e3c: v1e3c = SHA3 v1e2f(0x0), v1e39(0x40)
    0x1e3d: v1e3d = SLOAD v1e3c
    0x1e3f: JUMP v687(0x34d2)

    Begin block 0x34d2
    prev=[0x1e18], succ=[]
    =================================
    0x34d3: v34d3(0x40) = CONST 
    0x34d6: v34d6 = MLOAD v34d3(0x40)
    0x34d9: MSTORE v34d6, v1e3d
    0x34da: v34da = MLOAD v34d3(0x40)
    0x34de: v34de(0x0) = SUB v34d6, v34da
    0x34df: v34df(0x20) = CONST 
    0x34e1: v34e1(0x20) = ADD v34df(0x20), v34de(0x0)
    0x34e3: RETURN v34da, v34e1(0x20)

}

function pause()() public {
    Begin block 0x6b9
    prev=[], succ=[0x1e40]
    =================================
    0x6ba: v6ba(0x3503) = CONST 
    0x6bd: v6bd(0x1e40) = CONST 
    0x6c0: JUMP v6bd(0x1e40)

    Begin block 0x1e40
    prev=[0x6b9], succ=[0x1e60, 0x1eb0]
    =================================
    0x1e41: v1e41(0x1) = CONST 
    0x1e43: v1e43 = SLOAD v1e41(0x1)
    0x1e44: v1e44(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e59: v1e59 = AND v1e44(0xffffffffffffffffffffffffffffffffffffffff), v1e43
    0x1e5a: v1e5a = CALLER 
    0x1e5b: v1e5b = EQ v1e5a, v1e59
    0x1e5c: v1e5c(0x1eb0) = CONST 
    0x1e5f: JUMPI v1e5c(0x1eb0), v1e5b

    Begin block 0x1e60
    prev=[0x1e40], succ=[]
    =================================
    0x1e60: v1e60(0x40) = CONST 
    0x1e62: v1e62 = MLOAD v1e60(0x40)
    0x1e63: v1e63(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e85: MSTORE v1e62, v1e63(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e86: v1e86(0x4) = CONST 
    0x1e88: v1e88 = ADD v1e86(0x4), v1e62
    0x1e8b: v1e8b(0x20) = CONST 
    0x1e8d: v1e8d = ADD v1e8b(0x20), v1e88
    0x1e90: v1e90(0x20) = SUB v1e8d, v1e88
    0x1e92: MSTORE v1e88, v1e90(0x20)
    0x1e93: v1e93(0x22) = CONST 
    0x1e96: MSTORE v1e8d, v1e93(0x22)
    0x1e97: v1e97(0x20) = CONST 
    0x1e99: v1e99 = ADD v1e97(0x20), v1e8d
    0x1e9b: v1e9b(0x3074) = CONST 
    0x1e9e: v1e9e(0x22) = CONST 
    0x1ea1: CODECOPY v1e99, v1e9b(0x3074), v1e9e(0x22)
    0x1ea2: v1ea2(0x40) = CONST 
    0x1ea4: v1ea4 = ADD v1ea2(0x40), v1e99
    0x1ea8: v1ea8(0x40) = CONST 
    0x1eaa: v1eaa = MLOAD v1ea8(0x40)
    0x1ead: v1ead(0x84) = SUB v1ea4, v1eaa
    0x1eaf: REVERT v1eaa, v1ead(0x84)

    Begin block 0x1eb0
    prev=[0x1e40], succ=[0x3503]
    =================================
    0x1eb1: v1eb1(0x1) = CONST 
    0x1eb4: v1eb4 = SLOAD v1eb1(0x1)
    0x1eb5: v1eb5(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ed6: v1ed6 = AND v1eb5(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1eb4
    0x1ed7: v1ed7(0x10000000000000000000000000000000000000000) = CONST 
    0x1eed: v1eed = OR v1ed7(0x10000000000000000000000000000000000000000), v1ed6
    0x1eef: SSTORE v1eb1(0x1), v1eed
    0x1ef0: v1ef0(0x40) = CONST 
    0x1ef2: v1ef2 = MLOAD v1ef0(0x40)
    0x1ef3: v1ef3(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625) = CONST 
    0x1f15: v1f15(0x0) = CONST 
    0x1f18: LOG1 v1ef2, v1f15(0x0), v1ef3(0x6985a02210a168e66602d3235cb6db0e70f92b3ba4d376a33c0f3d9434bff625)
    0x1f19: JUMP v6ba(0x3503)

    Begin block 0x3503
    prev=[0x1eb0], succ=[]
    =================================
    0x3504: STOP 

}

function minterAllowance(address)() public {
    Begin block 0x6c1
    prev=[], succ=[0x6d3, 0x6d7]
    =================================
    0x6c2: v6c2(0x3524) = CONST 
    0x6c5: v6c5(0x4) = CONST 
    0x6c8: v6c8 = CALLDATASIZE 
    0x6c9: v6c9 = SUB v6c8, v6c5(0x4)
    0x6ca: v6ca(0x20) = CONST 
    0x6cd: v6cd = LT v6c9, v6ca(0x20)
    0x6ce: v6ce = ISZERO v6cd
    0x6cf: v6cf(0x6d7) = CONST 
    0x6d2: JUMPI v6cf(0x6d7), v6ce

    Begin block 0x6d3
    prev=[0x6c1], succ=[]
    =================================
    0x6d3: v6d3(0x0) = CONST 
    0x6d6: REVERT v6d3(0x0), v6d3(0x0)

    Begin block 0x6d7
    prev=[0x6c1], succ=[0x1f1a]
    =================================
    0x6d9: v6d9 = CALLDATALOAD v6c5(0x4)
    0x6da: v6da(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6ef: v6ef = AND v6da(0xffffffffffffffffffffffffffffffffffffffff), v6d9
    0x6f0: v6f0(0x1f1a) = CONST 
    0x6f3: JUMP v6f0(0x1f1a)

    Begin block 0x1f1a
    prev=[0x6d7], succ=[0x3524]
    =================================
    0x1f1b: v1f1b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f30: v1f30 = AND v1f1b(0xffffffffffffffffffffffffffffffffffffffff), v6ef
    0x1f31: v1f31(0x0) = CONST 
    0x1f35: MSTORE v1f31(0x0), v1f30
    0x1f36: v1f36(0xd) = CONST 
    0x1f38: v1f38(0x20) = CONST 
    0x1f3a: MSTORE v1f38(0x20), v1f36(0xd)
    0x1f3b: v1f3b(0x40) = CONST 
    0x1f3e: v1f3e = SHA3 v1f31(0x0), v1f3b(0x40)
    0x1f3f: v1f3f = SLOAD v1f3e
    0x1f41: JUMP v6c2(0x3524)

    Begin block 0x3524
    prev=[0x1f1a], succ=[]
    =================================
    0x3525: v3525(0x40) = CONST 
    0x3528: v3528 = MLOAD v3525(0x40)
    0x352b: MSTORE v3528, v1f3f
    0x352c: v352c = MLOAD v3525(0x40)
    0x3530: v3530(0x0) = SUB v3528, v352c
    0x3531: v3531(0x20) = CONST 
    0x3533: v3533(0x20) = ADD v3531(0x20), v3530(0x0)
    0x3535: RETURN v352c, v3533(0x20)

}

function owner()() public {
    Begin block 0x6f4
    prev=[], succ=[0x1f42]
    =================================
    0x6f5: v6f5(0x3555) = CONST 
    0x6f8: v6f8(0x1f42) = CONST 
    0x6fb: JUMP v6f8(0x1f42)

    Begin block 0x1f42
    prev=[0x6f4], succ=[0x3555]
    =================================
    0x1f43: v1f43(0x0) = CONST 
    0x1f45: v1f45 = SLOAD v1f43(0x0)
    0x1f46: v1f46(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f5b: v1f5b = AND v1f46(0xffffffffffffffffffffffffffffffffffffffff), v1f45
    0x1f5d: JUMP v6f5(0x3555)

    Begin block 0x3555
    prev=[0x1f42], succ=[]
    =================================
    0x3556: v3556(0x40) = CONST 
    0x3559: v3559 = MLOAD v3556(0x40)
    0x355a: v355a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3571: v3571 = AND v1f5b, v355a(0xffffffffffffffffffffffffffffffffffffffff)
    0x3573: MSTORE v3559, v3571
    0x3574: v3574 = MLOAD v3556(0x40)
    0x3578: v3578(0x0) = SUB v3559, v3574
    0x3579: v3579(0x20) = CONST 
    0x357b: v357b(0x20) = ADD v3579(0x20), v3578(0x0)
    0x357d: RETURN v3574, v357b(0x20)

}

function symbol()() public {
    Begin block 0x6fc
    prev=[], succ=[0x1f20x6fc]
    =================================
    0x6fd: v6fd(0x1f2) = CONST 
    0x700: v700(0x1f5e) = CONST 
    0x703: v703_0, v703_1 = CALLPRIVATE v700(0x1f5e), v6fd(0x1f2)

    Begin block 0x1f20x6fc
    prev=[0x6fc], succ=[0x2140x6fc]
    =================================
    0x1f30x6fc: v6fc1f3(0x40) = CONST 
    0x1f60x6fc: v6fc1f6 = MLOAD v6fc1f3(0x40)
    0x1f70x6fc: v6fc1f7(0x20) = CONST 
    0x1fb0x6fc: MSTORE v6fc1f6, v6fc1f7(0x20)
    0x1fd0x6fc: v6fc1fd = MLOAD v703_0
    0x2000x6fc: v6fc200 = ADD v6fc1f6, v6fc1f7(0x20)
    0x2010x6fc: MSTORE v6fc200, v6fc1fd
    0x2030x6fc: v6fc203 = MLOAD v703_0
    0x20a0x6fc: v6fc20a = ADD v6fc1f6, v6fc1f3(0x40)
    0x20d0x6fc: v6fc20d = ADD v703_0, v6fc1f7(0x20)
    0x2120x6fc: v6fc212(0x0) = CONST 

    Begin block 0x2140x6fc
    prev=[0x21d0x6fc, 0x1f20x6fc], succ=[0x22c0x6fc, 0x21d0x6fc]
    =================================
    0x2140x6fc_0x0: v2146fc_0 = PHI v6fc227, v6fc212(0x0)
    0x2170x6fc: v6fc217 = LT v2146fc_0, v6fc203
    0x2180x6fc: v6fc218 = ISZERO v6fc217
    0x2190x6fc: v6fc219(0x22c) = CONST 
    0x21c0x6fc: JUMPI v6fc219(0x22c), v6fc218

    Begin block 0x22c0x6fc
    prev=[0x2140x6fc], succ=[0x2590x6fc, 0x2400x6fc]
    =================================
    0x2350x6fc: v6fc235 = ADD v6fc203, v6fc20a
    0x2370x6fc: v6fc237(0x1f) = CONST 
    0x2390x6fc: v6fc239 = AND v6fc237(0x1f), v6fc203
    0x23b0x6fc: v6fc23b = ISZERO v6fc239
    0x23c0x6fc: v6fc23c(0x259) = CONST 
    0x23f0x6fc: JUMPI v6fc23c(0x259), v6fc23b

    Begin block 0x2590x6fc
    prev=[0x22c0x6fc, 0x2400x6fc], succ=[]
    =================================
    0x2590x6fc_0x1: v2596fc_1 = PHI v6fc256, v6fc235
    0x25f0x6fc: v6fc25f(0x40) = CONST 
    0x2610x6fc: v6fc261 = MLOAD v6fc25f(0x40)
    0x2640x6fc: v6fc264 = SUB v2596fc_1, v6fc261
    0x2660x6fc: RETURN v6fc261, v6fc264

    Begin block 0x2400x6fc
    prev=[0x22c0x6fc], succ=[0x2590x6fc]
    =================================
    0x2420x6fc: v6fc242 = SUB v6fc235, v6fc239
    0x2440x6fc: v6fc244 = MLOAD v6fc242
    0x2450x6fc: v6fc245(0x1) = CONST 
    0x2480x6fc: v6fc248(0x20) = CONST 
    0x24a0x6fc: v6fc24a = SUB v6fc248(0x20), v6fc239
    0x24b0x6fc: v6fc24b(0x100) = CONST 
    0x24e0x6fc: v6fc24e = EXP v6fc24b(0x100), v6fc24a
    0x24f0x6fc: v6fc24f = SUB v6fc24e, v6fc245(0x1)
    0x2500x6fc: v6fc250 = NOT v6fc24f
    0x2510x6fc: v6fc251 = AND v6fc250, v6fc244
    0x2530x6fc: MSTORE v6fc242, v6fc251
    0x2540x6fc: v6fc254(0x20) = CONST 
    0x2560x6fc: v6fc256 = ADD v6fc254(0x20), v6fc242

    Begin block 0x21d0x6fc
    prev=[0x2140x6fc], succ=[0x2140x6fc]
    =================================
    0x21d0x6fc_0x0: v21d6fc_0 = PHI v6fc227, v6fc212(0x0)
    0x21f0x6fc: v6fc21f = ADD v21d6fc_0, v6fc20d
    0x2200x6fc: v6fc220 = MLOAD v6fc21f
    0x2230x6fc: v6fc223 = ADD v21d6fc_0, v6fc20a
    0x2240x6fc: MSTORE v6fc223, v6fc220
    0x2250x6fc: v6fc225(0x20) = CONST 
    0x2270x6fc: v6fc227 = ADD v6fc225(0x20), v21d6fc_0
    0x2280x6fc: v6fc228(0x214) = CONST 
    0x22b0x6fc: JUMP v6fc228(0x214)

}

function pauser()() public {
    Begin block 0x704
    prev=[], succ=[0x1fd7]
    =================================
    0x705: v705(0x359d) = CONST 
    0x708: v708(0x1fd7) = CONST 
    0x70b: JUMP v708(0x1fd7)

    Begin block 0x1fd7
    prev=[0x704], succ=[0x359d]
    =================================
    0x1fd8: v1fd8(0x1) = CONST 
    0x1fda: v1fda = SLOAD v1fd8(0x1)
    0x1fdb: v1fdb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ff0: v1ff0 = AND v1fdb(0xffffffffffffffffffffffffffffffffffffffff), v1fda
    0x1ff2: JUMP v705(0x359d)

    Begin block 0x359d
    prev=[0x1fd7], succ=[]
    =================================
    0x359e: v359e(0x40) = CONST 
    0x35a1: v35a1 = MLOAD v359e(0x40)
    0x35a2: v35a2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x35b9: v35b9 = AND v1ff0, v35a2(0xffffffffffffffffffffffffffffffffffffffff)
    0x35bb: MSTORE v35a1, v35b9
    0x35bc: v35bc = MLOAD v359e(0x40)
    0x35c0: v35c0(0x0) = SUB v35a1, v35bc
    0x35c1: v35c1(0x20) = CONST 
    0x35c3: v35c3(0x20) = ADD v35c1(0x20), v35c0(0x0)
    0x35c5: RETURN v35bc, v35c3(0x20)

}

function transfer(address,uint256)() public {
    Begin block 0x70c
    prev=[], succ=[0x71e, 0x722]
    =================================
    0x70d: v70d(0x35e5) = CONST 
    0x710: v710(0x4) = CONST 
    0x713: v713 = CALLDATASIZE 
    0x714: v714 = SUB v713, v710(0x4)
    0x715: v715(0x40) = CONST 
    0x718: v718 = LT v714, v715(0x40)
    0x719: v719 = ISZERO v718
    0x71a: v71a(0x722) = CONST 
    0x71d: JUMPI v71a(0x722), v719

    Begin block 0x71e
    prev=[0x70c], succ=[]
    =================================
    0x71e: v71e(0x0) = CONST 
    0x721: REVERT v71e(0x0), v71e(0x0)

    Begin block 0x722
    prev=[0x70c], succ=[0x1ff3]
    =================================
    0x724: v724(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x73a: v73a = CALLDATALOAD v710(0x4)
    0x73b: v73b = AND v73a, v724(0xffffffffffffffffffffffffffffffffffffffff)
    0x73d: v73d(0x20) = CONST 
    0x73f: v73f(0x24) = ADD v73d(0x20), v710(0x4)
    0x740: v740 = CALLDATALOAD v73f(0x24)
    0x741: v741(0x1ff3) = CONST 
    0x744: JUMP v741(0x1ff3)

    Begin block 0x1ff3
    prev=[0x722], succ=[0x201a, 0x2080]
    =================================
    0x1ff4: v1ff4(0x1) = CONST 
    0x1ff6: v1ff6 = SLOAD v1ff4(0x1)
    0x1ff7: v1ff7(0x0) = CONST 
    0x1ffa: v1ffa(0x10000000000000000000000000000000000000000) = CONST 
    0x2011: v2011 = DIV v1ff6, v1ffa(0x10000000000000000000000000000000000000000)
    0x2012: v2012(0xff) = CONST 
    0x2014: v2014 = AND v2012(0xff), v2011
    0x2015: v2015 = ISZERO v2014
    0x2016: v2016(0x2080) = CONST 
    0x2019: JUMPI v2016(0x2080), v2015

    Begin block 0x201a
    prev=[0x1ff3], succ=[]
    =================================
    0x201a: v201a(0x40) = CONST 
    0x201d: v201d = MLOAD v201a(0x40)
    0x201e: v201e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2040: MSTORE v201d, v201e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2041: v2041(0x20) = CONST 
    0x2043: v2043(0x4) = CONST 
    0x2046: v2046 = ADD v201d, v2043(0x4)
    0x2047: MSTORE v2046, v2041(0x20)
    0x2048: v2048(0x10) = CONST 
    0x204a: v204a(0x24) = CONST 
    0x204d: v204d = ADD v201d, v204a(0x24)
    0x204e: MSTORE v204d, v2048(0x10)
    0x204f: v204f(0x5061757361626c653a2070617573656400000000000000000000000000000000) = CONST 
    0x2070: v2070(0x44) = CONST 
    0x2073: v2073 = ADD v201d, v2070(0x44)
    0x2074: MSTORE v2073, v204f(0x5061757361626c653a2070617573656400000000000000000000000000000000)
    0x2076: v2076 = MLOAD v201a(0x40)
    0x207a: v207a(0x0) = SUB v201d, v2076
    0x207b: v207b(0x64) = CONST 
    0x207d: v207d(0x64) = ADD v207b(0x64), v207a(0x0)
    0x207f: REVERT v2076, v207d(0x64)

    Begin block 0x2080
    prev=[0x1ff3], succ=[0x2099, 0x20e9]
    =================================
    0x2081: v2081 = CALLER 
    0x2082: v2082(0x0) = CONST 
    0x2086: MSTORE v2082(0x0), v2081
    0x2087: v2087(0x3) = CONST 
    0x2089: v2089(0x20) = CONST 
    0x208b: MSTORE v2089(0x20), v2087(0x3)
    0x208c: v208c(0x40) = CONST 
    0x208f: v208f = SHA3 v2082(0x0), v208c(0x40)
    0x2090: v2090 = SLOAD v208f
    0x2091: v2091(0xff) = CONST 
    0x2093: v2093 = AND v2091(0xff), v2090
    0x2094: v2094 = ISZERO v2093
    0x2095: v2095(0x20e9) = CONST 
    0x2098: JUMPI v2095(0x20e9), v2094

    Begin block 0x2099
    prev=[0x2080], succ=[]
    =================================
    0x2099: v2099(0x40) = CONST 
    0x209b: v209b = MLOAD v2099(0x40)
    0x209c: v209c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x20be: MSTORE v209b, v209c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x20bf: v20bf(0x4) = CONST 
    0x20c1: v20c1 = ADD v20bf(0x4), v209b
    0x20c4: v20c4(0x20) = CONST 
    0x20c6: v20c6 = ADD v20c4(0x20), v20c1
    0x20c9: v20c9(0x20) = SUB v20c6, v20c1
    0x20cb: MSTORE v20c1, v20c9(0x20)
    0x20cc: v20cc(0x25) = CONST 
    0x20cf: MSTORE v20c6, v20cc(0x25)
    0x20d0: v20d0(0x20) = CONST 
    0x20d2: v20d2 = ADD v20d0(0x20), v20c6
    0x20d4: v20d4(0x30f0) = CONST 
    0x20d7: v20d7(0x25) = CONST 
    0x20da: CODECOPY v20d2, v20d4(0x30f0), v20d7(0x25)
    0x20db: v20db(0x40) = CONST 
    0x20dd: v20dd = ADD v20db(0x40), v20d2
    0x20e1: v20e1(0x40) = CONST 
    0x20e3: v20e3 = MLOAD v20e1(0x40)
    0x20e6: v20e6(0x84) = SUB v20dd, v20e3
    0x20e8: REVERT v20e3, v20e6(0x84)

    Begin block 0x20e9
    prev=[0x2080], succ=[0x211a, 0x216a]
    =================================
    0x20ea: v20ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2100: v2100 = AND v73b, v20ea(0xffffffffffffffffffffffffffffffffffffffff)
    0x2101: v2101(0x0) = CONST 
    0x2105: MSTORE v2101(0x0), v2100
    0x2106: v2106(0x3) = CONST 
    0x2108: v2108(0x20) = CONST 
    0x210a: MSTORE v2108(0x20), v2106(0x3)
    0x210b: v210b(0x40) = CONST 
    0x210e: v210e = SHA3 v2101(0x0), v210b(0x40)
    0x210f: v210f = SLOAD v210e
    0x2112: v2112(0xff) = CONST 
    0x2114: v2114 = AND v2112(0xff), v210f
    0x2115: v2115 = ISZERO v2114
    0x2116: v2116(0x216a) = CONST 
    0x2119: JUMPI v2116(0x216a), v2115

    Begin block 0x211a
    prev=[0x20e9], succ=[]
    =================================
    0x211a: v211a(0x40) = CONST 
    0x211c: v211c = MLOAD v211a(0x40)
    0x211d: v211d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x213f: MSTORE v211c, v211d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2140: v2140(0x4) = CONST 
    0x2142: v2142 = ADD v2140(0x4), v211c
    0x2145: v2145(0x20) = CONST 
    0x2147: v2147 = ADD v2145(0x20), v2142
    0x214a: v214a(0x20) = SUB v2147, v2142
    0x214c: MSTORE v2142, v214a(0x20)
    0x214d: v214d(0x25) = CONST 
    0x2150: MSTORE v2147, v214d(0x25)
    0x2151: v2151(0x20) = CONST 
    0x2153: v2153 = ADD v2151(0x20), v2147
    0x2155: v2155(0x30f0) = CONST 
    0x2158: v2158(0x25) = CONST 
    0x215b: CODECOPY v2153, v2155(0x30f0), v2158(0x25)
    0x215c: v215c(0x40) = CONST 
    0x215e: v215e = ADD v215c(0x40), v2153
    0x2162: v2162(0x40) = CONST 
    0x2164: v2164 = MLOAD v2162(0x40)
    0x2167: v2167(0x84) = SUB v215e, v2164
    0x2169: REVERT v2164, v2167(0x84)

    Begin block 0x216a
    prev=[0x20e9], succ=[0x3841]
    =================================
    0x216b: v216b(0x3841) = CONST 
    0x216e: v216e = CALLER 
    0x2171: v2171(0x28e7) = CONST 
    0x2174: CALLPRIVATE v2171(0x28e7), v740, v73b, v216e, v216b(0x3841)

    Begin block 0x3841
    prev=[0x216a], succ=[0x35e5]
    =================================
    0x3843: v3843(0x1) = CONST 
    0x384b: JUMP v70d(0x35e5)

    Begin block 0x35e5
    prev=[0x3841], succ=[]
    =================================
    0x35e6: v35e6(0x40) = CONST 
    0x35e9: v35e9 = MLOAD v35e6(0x40)
    0x35eb: v35eb = ISZERO v3843(0x1)
    0x35ec: v35ec = ISZERO v35eb
    0x35ee: MSTORE v35e9, v35ec
    0x35ef: v35ef = MLOAD v35e6(0x40)
    0x35f3: v35f3(0x0) = SUB v35e9, v35ef
    0x35f4: v35f4(0x20) = CONST 
    0x35f6: v35f6(0x20) = ADD v35f4(0x20), v35f3(0x0)
    0x35f8: RETURN v35ef, v35f6(0x20)

}

function updateMasterMinter(address)() public {
    Begin block 0x745
    prev=[], succ=[0x757, 0x75b]
    =================================
    0x746: v746(0x3618) = CONST 
    0x749: v749(0x4) = CONST 
    0x74c: v74c = CALLDATASIZE 
    0x74d: v74d = SUB v74c, v749(0x4)
    0x74e: v74e(0x20) = CONST 
    0x751: v751 = LT v74d, v74e(0x20)
    0x752: v752 = ISZERO v751
    0x753: v753(0x75b) = CONST 
    0x756: JUMPI v753(0x75b), v752

    Begin block 0x757
    prev=[0x745], succ=[]
    =================================
    0x757: v757(0x0) = CONST 
    0x75a: REVERT v757(0x0), v757(0x0)

    Begin block 0x75b
    prev=[0x745], succ=[0x2175]
    =================================
    0x75d: v75d = CALLDATALOAD v749(0x4)
    0x75e: v75e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x773: v773 = AND v75e(0xffffffffffffffffffffffffffffffffffffffff), v75d
    0x774: v774(0x2175) = CONST 
    0x777: JUMP v774(0x2175)

    Begin block 0x2175
    prev=[0x75b], succ=[0x2195, 0x21fb]
    =================================
    0x2176: v2176(0x0) = CONST 
    0x2178: v2178 = SLOAD v2176(0x0)
    0x2179: v2179(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x218e: v218e = AND v2179(0xffffffffffffffffffffffffffffffffffffffff), v2178
    0x218f: v218f = CALLER 
    0x2190: v2190 = EQ v218f, v218e
    0x2191: v2191(0x21fb) = CONST 
    0x2194: JUMPI v2191(0x21fb), v2190

    Begin block 0x2195
    prev=[0x2175], succ=[]
    =================================
    0x2195: v2195(0x40) = CONST 
    0x2198: v2198 = MLOAD v2195(0x40)
    0x2199: v2199(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x21bb: MSTORE v2198, v2199(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21bc: v21bc(0x20) = CONST 
    0x21be: v21be(0x4) = CONST 
    0x21c1: v21c1 = ADD v2198, v21be(0x4)
    0x21c4: MSTORE v21c1, v21bc(0x20)
    0x21c5: v21c5(0x24) = CONST 
    0x21c8: v21c8 = ADD v2198, v21c5(0x24)
    0x21c9: MSTORE v21c8, v21bc(0x20)
    0x21ca: v21ca(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x21eb: v21eb(0x44) = CONST 
    0x21ee: v21ee = ADD v2198, v21eb(0x44)
    0x21ef: MSTORE v21ee, v21ca(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x21f1: v21f1 = MLOAD v2195(0x40)
    0x21f5: v21f5(0x0) = SUB v2198, v21f1
    0x21f6: v21f6(0x64) = CONST 
    0x21f8: v21f8(0x64) = ADD v21f6(0x64), v21f5(0x0)
    0x21fa: REVERT v21f1, v21f8(0x64)

    Begin block 0x21fb
    prev=[0x2175], succ=[0x2217, 0x2267]
    =================================
    0x21fc: v21fc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2212: v2212 = AND v773, v21fc(0xffffffffffffffffffffffffffffffffffffffff)
    0x2213: v2213(0x2267) = CONST 
    0x2216: JUMPI v2213(0x2267), v2212

    Begin block 0x2217
    prev=[0x21fb], succ=[]
    =================================
    0x2217: v2217(0x40) = CONST 
    0x2219: v2219 = MLOAD v2217(0x40)
    0x221a: v221a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x223c: MSTORE v2219, v221a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x223d: v223d(0x4) = CONST 
    0x223f: v223f = ADD v223d(0x4), v2219
    0x2242: v2242(0x20) = CONST 
    0x2244: v2244 = ADD v2242(0x20), v223f
    0x2247: v2247(0x20) = SUB v2244, v223f
    0x2249: MSTORE v223f, v2247(0x20)
    0x224a: v224a(0x2f) = CONST 
    0x224d: MSTORE v2244, v224a(0x2f)
    0x224e: v224e(0x20) = CONST 
    0x2250: v2250 = ADD v224e(0x20), v2244
    0x2252: v2252(0x2f4e) = CONST 
    0x2255: v2255(0x2f) = CONST 
    0x2258: CODECOPY v2250, v2252(0x2f4e), v2255(0x2f)
    0x2259: v2259(0x40) = CONST 
    0x225b: v225b = ADD v2259(0x40), v2250
    0x225f: v225f(0x40) = CONST 
    0x2261: v2261 = MLOAD v225f(0x40)
    0x2264: v2264(0x84) = SUB v225b, v2261
    0x2266: REVERT v2261, v2264(0x84)

    Begin block 0x2267
    prev=[0x21fb], succ=[0x3618]
    =================================
    0x2268: v2268(0x8) = CONST 
    0x226b: v226b = SLOAD v2268(0x8)
    0x226c: v226c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x228d: v228d = AND v226c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v226b
    0x228e: v228e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22a5: v22a5 = AND v228e(0xffffffffffffffffffffffffffffffffffffffff), v773
    0x22a9: v22a9 = OR v22a5, v228d
    0x22ad: SSTORE v2268(0x8), v22a9
    0x22ae: v22ae(0x40) = CONST 
    0x22b0: v22b0 = MLOAD v22ae(0x40)
    0x22b2: v22b2 = AND v22a9, v228e(0xffffffffffffffffffffffffffffffffffffffff)
    0x22b4: v22b4(0xdb66dfa9c6b8f5226fe9aac7e51897ae8ee94ac31dc70bb6c9900b2574b707e6) = CONST 
    0x22d6: v22d6(0x0) = CONST 
    0x22d9: LOG2 v22b0, v22d6(0x0), v22b4(0xdb66dfa9c6b8f5226fe9aac7e51897ae8ee94ac31dc70bb6c9900b2574b707e6), v22b2
    0x22db: JUMP v746(0x3618)

    Begin block 0x3618
    prev=[0x2267], succ=[]
    =================================
    0x3619: STOP 

}

function isMinter(address)() public {
    Begin block 0x778
    prev=[], succ=[0x78a, 0x78e]
    =================================
    0x779: v779(0x3639) = CONST 
    0x77c: v77c(0x4) = CONST 
    0x77f: v77f = CALLDATASIZE 
    0x780: v780 = SUB v77f, v77c(0x4)
    0x781: v781(0x20) = CONST 
    0x784: v784 = LT v780, v781(0x20)
    0x785: v785 = ISZERO v784
    0x786: v786(0x78e) = CONST 
    0x789: JUMPI v786(0x78e), v785

    Begin block 0x78a
    prev=[0x778], succ=[]
    =================================
    0x78a: v78a(0x0) = CONST 
    0x78d: REVERT v78a(0x0), v78a(0x0)

    Begin block 0x78e
    prev=[0x778], succ=[0x22dc]
    =================================
    0x790: v790 = CALLDATALOAD v77c(0x4)
    0x791: v791(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7a6: v7a6 = AND v791(0xffffffffffffffffffffffffffffffffffffffff), v790
    0x7a7: v7a7(0x22dc) = CONST 
    0x7aa: JUMP v7a7(0x22dc)

    Begin block 0x22dc
    prev=[0x78e], succ=[0x3639]
    =================================
    0x22dd: v22dd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22f2: v22f2 = AND v22dd(0xffffffffffffffffffffffffffffffffffffffff), v7a6
    0x22f3: v22f3(0x0) = CONST 
    0x22f7: MSTORE v22f3(0x0), v22f2
    0x22f8: v22f8(0xc) = CONST 
    0x22fa: v22fa(0x20) = CONST 
    0x22fc: MSTORE v22fa(0x20), v22f8(0xc)
    0x22fd: v22fd(0x40) = CONST 
    0x2300: v2300 = SHA3 v22f3(0x0), v22fd(0x40)
    0x2301: v2301 = SLOAD v2300
    0x2302: v2302(0xff) = CONST 
    0x2304: v2304 = AND v2302(0xff), v2301
    0x2306: JUMP v779(0x3639)

    Begin block 0x3639
    prev=[0x22dc], succ=[]
    =================================
    0x363a: v363a(0x40) = CONST 
    0x363d: v363d = MLOAD v363a(0x40)
    0x363f: v363f = ISZERO v2304
    0x3640: v3640 = ISZERO v363f
    0x3642: MSTORE v363d, v3640
    0x3643: v3643 = MLOAD v363a(0x40)
    0x3647: v3647(0x0) = SUB v363d, v3643
    0x3648: v3648(0x20) = CONST 
    0x364a: v364a(0x20) = ADD v3648(0x20), v3647(0x0)
    0x364c: RETURN v3643, v364a(0x20)

}

function updateBlacklister(address)() public {
    Begin block 0x7ab
    prev=[], succ=[0x7bd, 0x7c1]
    =================================
    0x7ac: v7ac(0x366c) = CONST 
    0x7af: v7af(0x4) = CONST 
    0x7b2: v7b2 = CALLDATASIZE 
    0x7b3: v7b3 = SUB v7b2, v7af(0x4)
    0x7b4: v7b4(0x20) = CONST 
    0x7b7: v7b7 = LT v7b3, v7b4(0x20)
    0x7b8: v7b8 = ISZERO v7b7
    0x7b9: v7b9(0x7c1) = CONST 
    0x7bc: JUMPI v7b9(0x7c1), v7b8

    Begin block 0x7bd
    prev=[0x7ab], succ=[]
    =================================
    0x7bd: v7bd(0x0) = CONST 
    0x7c0: REVERT v7bd(0x0), v7bd(0x0)

    Begin block 0x7c1
    prev=[0x7ab], succ=[0x2307]
    =================================
    0x7c3: v7c3 = CALLDATALOAD v7af(0x4)
    0x7c4: v7c4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7d9: v7d9 = AND v7c4(0xffffffffffffffffffffffffffffffffffffffff), v7c3
    0x7da: v7da(0x2307) = CONST 
    0x7dd: JUMP v7da(0x2307)

    Begin block 0x2307
    prev=[0x7c1], succ=[0x2327, 0x238d]
    =================================
    0x2308: v2308(0x0) = CONST 
    0x230a: v230a = SLOAD v2308(0x0)
    0x230b: v230b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2320: v2320 = AND v230b(0xffffffffffffffffffffffffffffffffffffffff), v230a
    0x2321: v2321 = CALLER 
    0x2322: v2322 = EQ v2321, v2320
    0x2323: v2323(0x238d) = CONST 
    0x2326: JUMPI v2323(0x238d), v2322

    Begin block 0x2327
    prev=[0x2307], succ=[]
    =================================
    0x2327: v2327(0x40) = CONST 
    0x232a: v232a = MLOAD v2327(0x40)
    0x232b: v232b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x234d: MSTORE v232a, v232b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x234e: v234e(0x20) = CONST 
    0x2350: v2350(0x4) = CONST 
    0x2353: v2353 = ADD v232a, v2350(0x4)
    0x2356: MSTORE v2353, v234e(0x20)
    0x2357: v2357(0x24) = CONST 
    0x235a: v235a = ADD v232a, v2357(0x24)
    0x235b: MSTORE v235a, v234e(0x20)
    0x235c: v235c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x237d: v237d(0x44) = CONST 
    0x2380: v2380 = ADD v232a, v237d(0x44)
    0x2381: MSTORE v2380, v235c(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x2383: v2383 = MLOAD v2327(0x40)
    0x2387: v2387(0x0) = SUB v232a, v2383
    0x2388: v2388(0x64) = CONST 
    0x238a: v238a(0x64) = ADD v2388(0x64), v2387(0x0)
    0x238c: REVERT v2383, v238a(0x64)

    Begin block 0x238d
    prev=[0x2307], succ=[0x23a9, 0x23f9]
    =================================
    0x238e: v238e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x23a4: v23a4 = AND v7d9, v238e(0xffffffffffffffffffffffffffffffffffffffff)
    0x23a5: v23a5(0x23f9) = CONST 
    0x23a8: JUMPI v23a5(0x23f9), v23a4

    Begin block 0x23a9
    prev=[0x238d], succ=[]
    =================================
    0x23a9: v23a9(0x40) = CONST 
    0x23ab: v23ab = MLOAD v23a9(0x40)
    0x23ac: v23ac(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x23ce: MSTORE v23ab, v23ac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x23cf: v23cf(0x4) = CONST 
    0x23d1: v23d1 = ADD v23cf(0x4), v23ab
    0x23d4: v23d4(0x20) = CONST 
    0x23d6: v23d6 = ADD v23d4(0x20), v23d1
    0x23d9: v23d9(0x20) = SUB v23d6, v23d1
    0x23db: MSTORE v23d1, v23d9(0x20)
    0x23dc: v23dc(0x32) = CONST 
    0x23df: MSTORE v23d6, v23dc(0x32)
    0x23e0: v23e0(0x20) = CONST 
    0x23e2: v23e2 = ADD v23e0(0x20), v23d6
    0x23e4: v23e4(0x30be) = CONST 
    0x23e7: v23e7(0x32) = CONST 
    0x23ea: CODECOPY v23e2, v23e4(0x30be), v23e7(0x32)
    0x23eb: v23eb(0x40) = CONST 
    0x23ed: v23ed = ADD v23eb(0x40), v23e2
    0x23f1: v23f1(0x40) = CONST 
    0x23f3: v23f3 = MLOAD v23f1(0x40)
    0x23f6: v23f6(0x84) = SUB v23ed, v23f3
    0x23f8: REVERT v23f3, v23f6(0x84)

    Begin block 0x23f9
    prev=[0x238d], succ=[0x366c]
    =================================
    0x23fa: v23fa(0x2) = CONST 
    0x23fd: v23fd = SLOAD v23fa(0x2)
    0x23fe: v23fe(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x241f: v241f = AND v23fe(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v23fd
    0x2420: v2420(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2437: v2437 = AND v2420(0xffffffffffffffffffffffffffffffffffffffff), v7d9
    0x243b: v243b = OR v2437, v241f
    0x243f: SSTORE v23fa(0x2), v243b
    0x2440: v2440(0x40) = CONST 
    0x2442: v2442 = MLOAD v2440(0x40)
    0x2444: v2444 = AND v243b, v2420(0xffffffffffffffffffffffffffffffffffffffff)
    0x2446: v2446(0xc67398012c111ce95ecb7429b933096c977380ee6c421175a71a4a4c6c88c06e) = CONST 
    0x2468: v2468(0x0) = CONST 
    0x246b: LOG2 v2442, v2468(0x0), v2446(0xc67398012c111ce95ecb7429b933096c977380ee6c421175a71a4a4c6c88c06e), v2444
    0x246d: JUMP v7ac(0x366c)

    Begin block 0x366c
    prev=[0x23f9], succ=[]
    =================================
    0x366d: STOP 

}

function blacklister()() public {
    Begin block 0x7de
    prev=[], succ=[0x246e]
    =================================
    0x7df: v7df(0x368d) = CONST 
    0x7e2: v7e2(0x246e) = CONST 
    0x7e5: JUMP v7e2(0x246e)

    Begin block 0x246e
    prev=[0x7de], succ=[0x368d]
    =================================
    0x246f: v246f(0x2) = CONST 
    0x2471: v2471 = SLOAD v246f(0x2)
    0x2472: v2472(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2487: v2487 = AND v2472(0xffffffffffffffffffffffffffffffffffffffff), v2471
    0x2489: JUMP v7df(0x368d)

    Begin block 0x368d
    prev=[0x246e], succ=[]
    =================================
    0x368e: v368e(0x40) = CONST 
    0x3691: v3691 = MLOAD v368e(0x40)
    0x3692: v3692(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x36a9: v36a9 = AND v2487, v3692(0xffffffffffffffffffffffffffffffffffffffff)
    0x36ab: MSTORE v3691, v36a9
    0x36ac: v36ac = MLOAD v368e(0x40)
    0x36b0: v36b0(0x0) = SUB v3691, v36ac
    0x36b1: v36b1(0x20) = CONST 
    0x36b3: v36b3(0x20) = ADD v36b1(0x20), v36b0(0x0)
    0x36b5: RETURN v36ac, v36b3(0x20)

}

function allowance(address,address)() public {
    Begin block 0x7e6
    prev=[], succ=[0x7f8, 0x7fc]
    =================================
    0x7e7: v7e7(0x36d5) = CONST 
    0x7ea: v7ea(0x4) = CONST 
    0x7ed: v7ed = CALLDATASIZE 
    0x7ee: v7ee = SUB v7ed, v7ea(0x4)
    0x7ef: v7ef(0x40) = CONST 
    0x7f2: v7f2 = LT v7ee, v7ef(0x40)
    0x7f3: v7f3 = ISZERO v7f2
    0x7f4: v7f4(0x7fc) = CONST 
    0x7f7: JUMPI v7f4(0x7fc), v7f3

    Begin block 0x7f8
    prev=[0x7e6], succ=[]
    =================================
    0x7f8: v7f8(0x0) = CONST 
    0x7fb: REVERT v7f8(0x0), v7f8(0x0)

    Begin block 0x7fc
    prev=[0x7e6], succ=[0x248a]
    =================================
    0x7fe: v7fe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x814: v814 = CALLDATALOAD v7ea(0x4)
    0x816: v816 = AND v7fe(0xffffffffffffffffffffffffffffffffffffffff), v814
    0x818: v818(0x20) = CONST 
    0x81a: v81a(0x24) = ADD v818(0x20), v7ea(0x4)
    0x81b: v81b = CALLDATALOAD v81a(0x24)
    0x81c: v81c = AND v81b, v7fe(0xffffffffffffffffffffffffffffffffffffffff)
    0x81d: v81d(0x248a) = CONST 
    0x820: JUMP v81d(0x248a)

    Begin block 0x248a
    prev=[0x7fc], succ=[0x36d5]
    =================================
    0x248b: v248b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24a2: v24a2 = AND v248b(0xffffffffffffffffffffffffffffffffffffffff), v816
    0x24a3: v24a3(0x0) = CONST 
    0x24a7: MSTORE v24a3(0x0), v24a2
    0x24a8: v24a8(0xa) = CONST 
    0x24aa: v24aa(0x20) = CONST 
    0x24ae: MSTORE v24aa(0x20), v24a8(0xa)
    0x24af: v24af(0x40) = CONST 
    0x24b3: v24b3 = SHA3 v24a3(0x0), v24af(0x40)
    0x24b7: v24b7 = AND v248b(0xffffffffffffffffffffffffffffffffffffffff), v81c
    0x24b9: MSTORE v24a3(0x0), v24b7
    0x24bd: MSTORE v24aa(0x20), v24b3
    0x24be: v24be = SHA3 v24a3(0x0), v24af(0x40)
    0x24bf: v24bf = SLOAD v24be
    0x24c1: JUMP v7e7(0x36d5)

    Begin block 0x36d5
    prev=[0x248a], succ=[]
    =================================
    0x36d6: v36d6(0x40) = CONST 
    0x36d9: v36d9 = MLOAD v36d6(0x40)
    0x36dc: MSTORE v36d9, v24bf
    0x36dd: v36dd = MLOAD v36d6(0x40)
    0x36e1: v36e1(0x0) = SUB v36d9, v36dd
    0x36e2: v36e2(0x20) = CONST 
    0x36e4: v36e4(0x20) = ADD v36e2(0x20), v36e1(0x0)
    0x36e6: RETURN v36dd, v36e4(0x20)

}

function currency()() public {
    Begin block 0x821
    prev=[], succ=[0x1f20x821]
    =================================
    0x822: v822(0x1f2) = CONST 
    0x825: v825(0x24c2) = CONST 
    0x828: v828_0, v828_1 = CALLPRIVATE v825(0x24c2), v822(0x1f2)

    Begin block 0x1f20x821
    prev=[0x821], succ=[0x2140x821]
    =================================
    0x1f30x821: v8211f3(0x40) = CONST 
    0x1f60x821: v8211f6 = MLOAD v8211f3(0x40)
    0x1f70x821: v8211f7(0x20) = CONST 
    0x1fb0x821: MSTORE v8211f6, v8211f7(0x20)
    0x1fd0x821: v8211fd = MLOAD v828_0
    0x2000x821: v821200 = ADD v8211f6, v8211f7(0x20)
    0x2010x821: MSTORE v821200, v8211fd
    0x2030x821: v821203 = MLOAD v828_0
    0x20a0x821: v82120a = ADD v8211f6, v8211f3(0x40)
    0x20d0x821: v82120d = ADD v828_0, v8211f7(0x20)
    0x2120x821: v821212(0x0) = CONST 

    Begin block 0x2140x821
    prev=[0x21d0x821, 0x1f20x821], succ=[0x22c0x821, 0x21d0x821]
    =================================
    0x2140x821_0x0: v214821_0 = PHI v821227, v821212(0x0)
    0x2170x821: v821217 = LT v214821_0, v821203
    0x2180x821: v821218 = ISZERO v821217
    0x2190x821: v821219(0x22c) = CONST 
    0x21c0x821: JUMPI v821219(0x22c), v821218

    Begin block 0x22c0x821
    prev=[0x2140x821], succ=[0x2590x821, 0x2400x821]
    =================================
    0x2350x821: v821235 = ADD v821203, v82120a
    0x2370x821: v821237(0x1f) = CONST 
    0x2390x821: v821239 = AND v821237(0x1f), v821203
    0x23b0x821: v82123b = ISZERO v821239
    0x23c0x821: v82123c(0x259) = CONST 
    0x23f0x821: JUMPI v82123c(0x259), v82123b

    Begin block 0x2590x821
    prev=[0x22c0x821, 0x2400x821], succ=[]
    =================================
    0x2590x821_0x1: v259821_1 = PHI v821256, v821235
    0x25f0x821: v82125f(0x40) = CONST 
    0x2610x821: v821261 = MLOAD v82125f(0x40)
    0x2640x821: v821264 = SUB v259821_1, v821261
    0x2660x821: RETURN v821261, v821264

    Begin block 0x2400x821
    prev=[0x22c0x821], succ=[0x2590x821]
    =================================
    0x2420x821: v821242 = SUB v821235, v821239
    0x2440x821: v821244 = MLOAD v821242
    0x2450x821: v821245(0x1) = CONST 
    0x2480x821: v821248(0x20) = CONST 
    0x24a0x821: v82124a = SUB v821248(0x20), v821239
    0x24b0x821: v82124b(0x100) = CONST 
    0x24e0x821: v82124e = EXP v82124b(0x100), v82124a
    0x24f0x821: v82124f = SUB v82124e, v821245(0x1)
    0x2500x821: v821250 = NOT v82124f
    0x2510x821: v821251 = AND v821250, v821244
    0x2530x821: MSTORE v821242, v821251
    0x2540x821: v821254(0x20) = CONST 
    0x2560x821: v821256 = ADD v821254(0x20), v821242

    Begin block 0x21d0x821
    prev=[0x2140x821], succ=[0x2140x821]
    =================================
    0x21d0x821_0x0: v21d821_0 = PHI v821227, v821212(0x0)
    0x21f0x821: v82121f = ADD v21d821_0, v82120d
    0x2200x821: v821220 = MLOAD v82121f
    0x2230x821: v821223 = ADD v21d821_0, v82120a
    0x2240x821: MSTORE v821223, v821220
    0x2250x821: v821225(0x20) = CONST 
    0x2270x821: v821227 = ADD v821225(0x20), v21d821_0
    0x2280x821: v821228(0x214) = CONST 
    0x22b0x821: JUMP v821228(0x214)

}

function transferOwnership(address)() public {
    Begin block 0x829
    prev=[], succ=[0x83b, 0x83f]
    =================================
    0x82a: v82a(0x3706) = CONST 
    0x82d: v82d(0x4) = CONST 
    0x830: v830 = CALLDATASIZE 
    0x831: v831 = SUB v830, v82d(0x4)
    0x832: v832(0x20) = CONST 
    0x835: v835 = LT v831, v832(0x20)
    0x836: v836 = ISZERO v835
    0x837: v837(0x83f) = CONST 
    0x83a: JUMPI v837(0x83f), v836

    Begin block 0x83b
    prev=[0x829], succ=[]
    =================================
    0x83b: v83b(0x0) = CONST 
    0x83e: REVERT v83b(0x0), v83b(0x0)

    Begin block 0x83f
    prev=[0x829], succ=[0x253b]
    =================================
    0x841: v841 = CALLDATALOAD v82d(0x4)
    0x842: v842(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x857: v857 = AND v842(0xffffffffffffffffffffffffffffffffffffffff), v841
    0x858: v858(0x253b) = CONST 
    0x85b: JUMP v858(0x253b)

    Begin block 0x253b
    prev=[0x83f], succ=[0x255b, 0x25c1]
    =================================
    0x253c: v253c(0x0) = CONST 
    0x253e: v253e = SLOAD v253c(0x0)
    0x253f: v253f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2554: v2554 = AND v253f(0xffffffffffffffffffffffffffffffffffffffff), v253e
    0x2555: v2555 = CALLER 
    0x2556: v2556 = EQ v2555, v2554
    0x2557: v2557(0x25c1) = CONST 
    0x255a: JUMPI v2557(0x25c1), v2556

    Begin block 0x255b
    prev=[0x253b], succ=[]
    =================================
    0x255b: v255b(0x40) = CONST 
    0x255e: v255e = MLOAD v255b(0x40)
    0x255f: v255f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2581: MSTORE v255e, v255f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2582: v2582(0x20) = CONST 
    0x2584: v2584(0x4) = CONST 
    0x2587: v2587 = ADD v255e, v2584(0x4)
    0x258a: MSTORE v2587, v2582(0x20)
    0x258b: v258b(0x24) = CONST 
    0x258e: v258e = ADD v255e, v258b(0x24)
    0x258f: MSTORE v258e, v2582(0x20)
    0x2590: v2590(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572) = CONST 
    0x25b1: v25b1(0x44) = CONST 
    0x25b4: v25b4 = ADD v255e, v25b1(0x44)
    0x25b5: MSTORE v25b4, v2590(0x4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572)
    0x25b7: v25b7 = MLOAD v255b(0x40)
    0x25bb: v25bb(0x0) = SUB v255e, v25b7
    0x25bc: v25bc(0x64) = CONST 
    0x25be: v25be(0x64) = ADD v25bc(0x64), v25bb(0x0)
    0x25c0: REVERT v25b7, v25be(0x64)

    Begin block 0x25c1
    prev=[0x253b], succ=[0x25dd, 0x262d]
    =================================
    0x25c2: v25c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25d8: v25d8 = AND v857, v25c2(0xffffffffffffffffffffffffffffffffffffffff)
    0x25d9: v25d9(0x262d) = CONST 
    0x25dc: JUMPI v25d9(0x262d), v25d8

    Begin block 0x25dd
    prev=[0x25c1], succ=[]
    =================================
    0x25dd: v25dd(0x40) = CONST 
    0x25df: v25df = MLOAD v25dd(0x40)
    0x25e0: v25e0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2602: MSTORE v25df, v25e0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2603: v2603(0x4) = CONST 
    0x2605: v2605 = ADD v2603(0x4), v25df
    0x2608: v2608(0x20) = CONST 
    0x260a: v260a = ADD v2608(0x20), v2605
    0x260d: v260d(0x20) = SUB v260a, v2605
    0x260f: MSTORE v2605, v260d(0x20)
    0x2610: v2610(0x26) = CONST 
    0x2613: MSTORE v260a, v2610(0x26)
    0x2614: v2614(0x20) = CONST 
    0x2616: v2616 = ADD v2614(0x20), v260a
    0x2618: v2618(0x2df2) = CONST 
    0x261b: v261b(0x26) = CONST 
    0x261e: CODECOPY v2616, v2618(0x2df2), v261b(0x26)
    0x261f: v261f(0x40) = CONST 
    0x2621: v2621 = ADD v261f(0x40), v2616
    0x2625: v2625(0x40) = CONST 
    0x2627: v2627 = MLOAD v2625(0x40)
    0x262a: v262a(0x84) = SUB v2621, v2627
    0x262c: REVERT v2627, v262a(0x84)

    Begin block 0x262d
    prev=[0x25c1], succ=[0x2b5bB0x262d]
    =================================
    0x262e: v262e(0x0) = CONST 
    0x2630: v2630 = SLOAD v262e(0x0)
    0x2631: v2631(0x40) = CONST 
    0x2634: v2634 = MLOAD v2631(0x40)
    0x2635: v2635(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x264c: v264c = AND v2635(0xffffffffffffffffffffffffffffffffffffffff), v2630
    0x264e: MSTORE v2634, v264c
    0x2651: v2651 = AND v857, v2635(0xffffffffffffffffffffffffffffffffffffffff)
    0x2652: v2652(0x20) = CONST 
    0x2655: v2655 = ADD v2634, v2652(0x20)
    0x2656: MSTORE v2655, v2651
    0x2658: v2658 = MLOAD v2631(0x40)
    0x2659: v2659(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x267d: v267d(0x0) = SUB v2634, v2658
    0x2680: v2680(0x40) = ADD v2631(0x40), v267d(0x0)
    0x2682: LOG1 v2658, v2680(0x40), v2659(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0)
    0x2683: v2683(0x268b) = CONST 
    0x2687: v2687(0x2b5b) = CONST 
    0x268a: JUMP v2687(0x2b5b), v857, v2683(0x268b)

    Begin block 0x2b5bB0x262d
    prev=[0x262d], succ=[0x268b]
    =================================
    0x2b5cS0x262d: v2b5cV262d(0x0) = CONST 
    0x2b5fS0x262d: v2b5fV262d = SLOAD v2b5cV262d(0x0)
    0x2b60S0x262d: v2b60V262d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x2b81S0x262d: v2b81V262d = AND v2b60V262d(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2b5fV262d
    0x2b82S0x262d: v2b82V262d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b9aS0x262d: v2b9aV262d = AND v2b82V262d(0xffffffffffffffffffffffffffffffffffffffff), v857
    0x2b9eS0x262d: v2b9eV262d = OR v2b9aV262d, v2b81V262d
    0x2ba0S0x262d: SSTORE v2b5cV262d(0x0), v2b9eV262d
    0x2ba1S0x262d: JUMP v2683(0x268b)

    Begin block 0x268b
    prev=[0x2b5bB0x262d], succ=[0x3706]
    =================================
    0x268d: JUMP v82a(0x3706)

    Begin block 0x3706
    prev=[0x268b], succ=[]
    =================================
    0x3707: STOP 

}

function blacklist(address)() public {
    Begin block 0x85c
    prev=[], succ=[0x86e, 0x872]
    =================================
    0x85d: v85d(0x3727) = CONST 
    0x860: v860(0x4) = CONST 
    0x863: v863 = CALLDATASIZE 
    0x864: v864 = SUB v863, v860(0x4)
    0x865: v865(0x20) = CONST 
    0x868: v868 = LT v864, v865(0x20)
    0x869: v869 = ISZERO v868
    0x86a: v86a(0x872) = CONST 
    0x86d: JUMPI v86a(0x872), v869

    Begin block 0x86e
    prev=[0x85c], succ=[]
    =================================
    0x86e: v86e(0x0) = CONST 
    0x871: REVERT v86e(0x0), v86e(0x0)

    Begin block 0x872
    prev=[0x85c], succ=[0x268e]
    =================================
    0x874: v874 = CALLDATALOAD v860(0x4)
    0x875: v875(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x88a: v88a = AND v875(0xffffffffffffffffffffffffffffffffffffffff), v874
    0x88b: v88b(0x268e) = CONST 
    0x88e: JUMP v88b(0x268e)

    Begin block 0x268e
    prev=[0x872], succ=[0x26ae, 0x26fe]
    =================================
    0x268f: v268f(0x2) = CONST 
    0x2691: v2691 = SLOAD v268f(0x2)
    0x2692: v2692(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26a7: v26a7 = AND v2692(0xffffffffffffffffffffffffffffffffffffffff), v2691
    0x26a8: v26a8 = CALLER 
    0x26a9: v26a9 = EQ v26a8, v26a7
    0x26aa: v26aa(0x26fe) = CONST 
    0x26ad: JUMPI v26aa(0x26fe), v26a9

    Begin block 0x26ae
    prev=[0x268e], succ=[]
    =================================
    0x26ae: v26ae(0x40) = CONST 
    0x26b0: v26b0 = MLOAD v26ae(0x40)
    0x26b1: v26b1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x26d3: MSTORE v26b0, v26b1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x26d4: v26d4(0x4) = CONST 
    0x26d6: v26d6 = ADD v26d4(0x4), v26b0
    0x26d9: v26d9(0x20) = CONST 
    0x26db: v26db = ADD v26d9(0x20), v26d6
    0x26de: v26de(0x20) = SUB v26db, v26d6
    0x26e0: MSTORE v26d6, v26de(0x20)
    0x26e1: v26e1(0x2c) = CONST 
    0x26e4: MSTORE v26db, v26e1(0x2c)
    0x26e5: v26e5(0x20) = CONST 
    0x26e7: v26e7 = ADD v26e5(0x20), v26db
    0x26e9: v26e9(0x2edb) = CONST 
    0x26ec: v26ec(0x2c) = CONST 
    0x26ef: CODECOPY v26e7, v26e9(0x2edb), v26ec(0x2c)
    0x26f0: v26f0(0x40) = CONST 
    0x26f2: v26f2 = ADD v26f0(0x40), v26e7
    0x26f6: v26f6(0x40) = CONST 
    0x26f8: v26f8 = MLOAD v26f6(0x40)
    0x26fb: v26fb(0x84) = SUB v26f2, v26f8
    0x26fd: REVERT v26f8, v26fb(0x84)

    Begin block 0x26fe
    prev=[0x268e], succ=[0x3727]
    =================================
    0x26ff: v26ff(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2715: v2715 = AND v88a, v26ff(0xffffffffffffffffffffffffffffffffffffffff)
    0x2716: v2716(0x0) = CONST 
    0x271a: MSTORE v2716(0x0), v2715
    0x271b: v271b(0x3) = CONST 
    0x271d: v271d(0x20) = CONST 
    0x271f: MSTORE v271d(0x20), v271b(0x3)
    0x2720: v2720(0x40) = CONST 
    0x2724: v2724 = SHA3 v2716(0x0), v2720(0x40)
    0x2726: v2726 = SLOAD v2724
    0x2727: v2727(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x2748: v2748 = AND v2727(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2726
    0x2749: v2749(0x1) = CONST 
    0x274b: v274b = OR v2749(0x1), v2748
    0x274d: SSTORE v2724, v274b
    0x274e: v274e = MLOAD v2720(0x40)
    0x274f: v274f(0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855) = CONST 
    0x2772: LOG2 v274e, v2716(0x0), v274f(0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855), v2715
    0x2774: JUMP v85d(0x3727)

    Begin block 0x3727
    prev=[0x26fe], succ=[]
    =================================
    0x3728: STOP 

}

function isBlacklisted(address)() public {
    Begin block 0x88f
    prev=[], succ=[0x8a1, 0x8a5]
    =================================
    0x890: v890(0x3748) = CONST 
    0x893: v893(0x4) = CONST 
    0x896: v896 = CALLDATASIZE 
    0x897: v897 = SUB v896, v893(0x4)
    0x898: v898(0x20) = CONST 
    0x89b: v89b = LT v897, v898(0x20)
    0x89c: v89c = ISZERO v89b
    0x89d: v89d(0x8a5) = CONST 
    0x8a0: JUMPI v89d(0x8a5), v89c

    Begin block 0x8a1
    prev=[0x88f], succ=[]
    =================================
    0x8a1: v8a1(0x0) = CONST 
    0x8a4: REVERT v8a1(0x0), v8a1(0x0)

    Begin block 0x8a5
    prev=[0x88f], succ=[0x2775]
    =================================
    0x8a7: v8a7 = CALLDATALOAD v893(0x4)
    0x8a8: v8a8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8bd: v8bd = AND v8a8(0xffffffffffffffffffffffffffffffffffffffff), v8a7
    0x8be: v8be(0x2775) = CONST 
    0x8c1: JUMP v8be(0x2775)

    Begin block 0x2775
    prev=[0x8a5], succ=[0x3748]
    =================================
    0x2776: v2776(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x278b: v278b = AND v2776(0xffffffffffffffffffffffffffffffffffffffff), v8bd
    0x278c: v278c(0x0) = CONST 
    0x2790: MSTORE v278c(0x0), v278b
    0x2791: v2791(0x3) = CONST 
    0x2793: v2793(0x20) = CONST 
    0x2795: MSTORE v2793(0x20), v2791(0x3)
    0x2796: v2796(0x40) = CONST 
    0x2799: v2799 = SHA3 v278c(0x0), v2796(0x40)
    0x279a: v279a = SLOAD v2799
    0x279b: v279b(0xff) = CONST 
    0x279d: v279d = AND v279b(0xff), v279a
    0x279f: JUMP v890(0x3748)

    Begin block 0x3748
    prev=[0x2775], succ=[]
    =================================
    0x3749: v3749(0x40) = CONST 
    0x374c: v374c = MLOAD v3749(0x40)
    0x374e: v374e = ISZERO v279d
    0x374f: v374f = ISZERO v374e
    0x3751: MSTORE v374c, v374f
    0x3752: v3752 = MLOAD v3749(0x40)
    0x3756: v3756(0x0) = SUB v374c, v3752
    0x3757: v3757(0x20) = CONST 
    0x3759: v3759(0x20) = ADD v3757(0x20), v3756(0x0)
    0x375b: RETURN v3752, v3759(0x20)

}

function 0x8c2(0x8c2arg0x0) private {
    Begin block 0x8c2
    prev=[], succ=[0x377b, 0x920]
    =================================
    0x8c3: v8c3(0x4) = CONST 
    0x8c6: v8c6 = SLOAD v8c3(0x4)
    0x8c7: v8c7(0x40) = CONST 
    0x8ca: v8ca = MLOAD v8c7(0x40)
    0x8cb: v8cb(0x20) = CONST 
    0x8cd: v8cd(0x2) = CONST 
    0x8cf: v8cf(0x1) = CONST 
    0x8d2: v8d2 = AND v8c6, v8cf(0x1)
    0x8d3: v8d3 = ISZERO v8d2
    0x8d4: v8d4(0x100) = CONST 
    0x8d7: v8d7 = MUL v8d4(0x100), v8d3
    0x8d8: v8d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8f9: v8f9 = ADD v8d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v8d7
    0x8fc: v8fc = AND v8c6, v8f9
    0x900: v900 = DIV v8fc, v8cd(0x2)
    0x901: v901(0x1f) = CONST 
    0x904: v904 = ADD v900, v901(0x1f)
    0x907: v907 = DIV v904, v8cb(0x20)
    0x909: v909 = MUL v8cb(0x20), v907
    0x90b: v90b = ADD v8ca, v909
    0x90d: v90d = ADD v8cb(0x20), v90b
    0x910: MSTORE v8c7(0x40), v90d
    0x913: MSTORE v8ca, v900
    0x917: v917 = ADD v8ca, v8cb(0x20)
    0x91b: v91b = ISZERO v900
    0x91c: v91c(0x377b) = CONST 
    0x91f: JUMPI v91c(0x377b), v91b

    Begin block 0x377b
    prev=[0x8c2], succ=[]
    =================================
    0x3782: RETURNPRIVATE v8c2arg0, v8ca, v8c2arg0

    Begin block 0x920
    prev=[0x8c2], succ=[0x928, 0x93b0x8c2]
    =================================
    0x921: v921(0x1f) = CONST 
    0x923: v923 = LT v921(0x1f), v900
    0x924: v924(0x93b) = CONST 
    0x927: JUMPI v924(0x93b), v923

    Begin block 0x928
    prev=[0x920], succ=[0x37a2]
    =================================
    0x928: v928(0x100) = CONST 
    0x92d: v92d = SLOAD v8c3(0x4)
    0x92e: v92e = DIV v92d, v928(0x100)
    0x92f: v92f = MUL v92e, v928(0x100)
    0x931: MSTORE v917, v92f
    0x933: v933(0x20) = CONST 
    0x935: v935 = ADD v933(0x20), v917
    0x937: v937(0x37a2) = CONST 
    0x93a: JUMP v937(0x37a2)

    Begin block 0x37a2
    prev=[0x928], succ=[]
    =================================
    0x37a9: RETURNPRIVATE v8c2arg0, v8ca, v8c2arg0

    Begin block 0x93b0x8c2
    prev=[0x920], succ=[0x9490x8c2]
    =================================
    0x93d0x8c2: v8c293d = ADD v917, v900
    0x9400x8c2: v8c2940(0x0) = CONST 
    0x9420x8c2: MSTORE v8c2940(0x0), v8c3(0x4)
    0x9430x8c2: v8c2943(0x20) = CONST 
    0x9450x8c2: v8c2945(0x0) = CONST 
    0x9470x8c2: v8c2947 = SHA3 v8c2945(0x0), v8c2943(0x20)

    Begin block 0x9490x8c2
    prev=[0x9490x8c2, 0x93b0x8c2], succ=[0x9490x8c2, 0x95d0x8c2]
    =================================
    0x9490x8c2_0x0: v9498c2_0 = PHI v917, v8c2955
    0x9490x8c2_0x1: v9498c2_1 = PHI v8c2951, v8c2947
    0x94b0x8c2: v8c294b = SLOAD v9498c2_1
    0x94d0x8c2: MSTORE v9498c2_0, v8c294b
    0x94f0x8c2: v8c294f(0x1) = CONST 
    0x9510x8c2: v8c2951 = ADD v8c294f(0x1), v9498c2_1
    0x9530x8c2: v8c2953(0x20) = CONST 
    0x9550x8c2: v8c2955 = ADD v8c2953(0x20), v9498c2_0
    0x9580x8c2: v8c2958 = GT v8c293d, v8c2955
    0x9590x8c2: v8c2959(0x949) = CONST 
    0x95c0x8c2: JUMPI v8c2959(0x949), v8c2958

    Begin block 0x95d0x8c2
    prev=[0x9490x8c2], succ=[0x9660x8c2]
    =================================
    0x95f0x8c2: v8c295f = SUB v8c2955, v8c293d
    0x9600x8c2: v8c2960(0x1f) = CONST 
    0x9620x8c2: v8c2962 = AND v8c2960(0x1f), v8c295f
    0x9640x8c2: v8c2964 = ADD v8c293d, v8c2962

    Begin block 0x9660x8c2
    prev=[0x95d0x8c2], succ=[]
    =================================
    0x96d0x8c2: RETURNPRIVATE v8c2arg0, v8ca, v8c2arg0

}

