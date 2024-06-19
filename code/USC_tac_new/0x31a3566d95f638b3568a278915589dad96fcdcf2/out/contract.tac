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
    prev=[0x0], succ=[0x1a, 0x3a1f]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x3941: v3941(0x3a1f) = CONST 
    0x3942: JUMPI v3941(0x3a1f), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x191, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x6a1463c8) = CONST 
    0x26: v26 = GT v21(0x6a1463c8), v1f
    0x27: v27(0x191) = CONST 
    0x2a: JUMPI v27(0x191), v26

    Begin block 0x191
    prev=[0x1a], succ=[0x24a, 0x19d]
    =================================
    0x193: v193(0x392e53cd) = CONST 
    0x198: v198 = GT v193(0x392e53cd), v1f
    0x199: v199(0x24a) = CONST 
    0x19c: JUMPI v199(0x24a), v198

    Begin block 0x24a
    prev=[0x191], succ=[0x2ac, 0x256]
    =================================
    0x24c: v24c(0x1a5e2e54) = CONST 
    0x251: v251 = GT v24c(0x1a5e2e54), v1f
    0x252: v252(0x2ac) = CONST 
    0x255: JUMPI v252(0x2ac), v251

    Begin block 0x2ac
    prev=[0x24a], succ=[0x2dd, 0x2b8]
    =================================
    0x2ae: v2ae(0x154ec2db) = CONST 
    0x2b3: v2b3 = GT v2ae(0x154ec2db), v1f
    0x2b4: v2b4(0x2dd) = CONST 
    0x2b7: JUMPI v2b4(0x2dd), v2b3

    Begin block 0x2dd
    prev=[0x2ac], succ=[0x399b, 0x2e9]
    =================================
    0x2df: v2df(0x7284ce9) = CONST 
    0x2e4: v2e4 = EQ v2df(0x7284ce9), v1f
    0x3997: v3997(0x399b) = CONST 
    0x3998: JUMPI v3997(0x399b), v2e4

    Begin block 0x399b
    prev=[0x2dd], succ=[]
    =================================
    0x399c: v399c(0x2f9) = CONST 
    0x399d: CALLPRIVATE v399c(0x2f9)

    Begin block 0x2e9
    prev=[0x2dd], succ=[0x399e, 0x2f4]
    =================================
    0x2ea: v2ea(0x108b54b9) = CONST 
    0x2ef: v2ef = EQ v2ea(0x108b54b9), v1f
    0x3999: v3999(0x399e) = CONST 
    0x399a: JUMPI v3999(0x399e), v2ef

    Begin block 0x399e
    prev=[0x2e9], succ=[]
    =================================
    0x399f: v399f(0x313) = CONST 
    0x39a0: CALLPRIVATE v399f(0x313)

    Begin block 0x2f4
    prev=[0x2e9], succ=[]
    =================================
    0x2f5: v2f5(0x0) = CONST 
    0x2f8: REVERT v2f5(0x0), v2f5(0x0)

    Begin block 0x2b8
    prev=[0x2ac], succ=[0x39a1, 0x2c3]
    =================================
    0x2b9: v2b9(0x154ec2db) = CONST 
    0x2be: v2be = EQ v2b9(0x154ec2db), v1f
    0x3991: v3991(0x39a1) = CONST 
    0x3992: JUMPI v3991(0x39a1), v2be

    Begin block 0x39a1
    prev=[0x2b8], succ=[]
    =================================
    0x39a2: v39a2(0x332) = CONST 
    0x39a3: CALLPRIVATE v39a2(0x332)

    Begin block 0x2c3
    prev=[0x2b8], succ=[0x39a4, 0x2ce]
    =================================
    0x2c4: v2c4(0x158ef93e) = CONST 
    0x2c9: v2c9 = EQ v2c4(0x158ef93e), v1f
    0x3993: v3993(0x39a4) = CONST 
    0x3994: JUMPI v3993(0x39a4), v2c9

    Begin block 0x39a4
    prev=[0x2c3], succ=[]
    =================================
    0x39a5: v39a5(0x34f) = CONST 
    0x39a6: CALLPRIVATE v39a5(0x34f)

    Begin block 0x2ce
    prev=[0x2c3], succ=[0x2d9, 0x39a7]
    =================================
    0x2cf: v2cf(0x19cd47f9) = CONST 
    0x2d4: v2d4 = EQ v2cf(0x19cd47f9), v1f
    0x3995: v3995(0x39a7) = CONST 
    0x3996: JUMPI v3995(0x39a7), v2d4

    Begin block 0x2d9
    prev=[0x2ce], succ=[0x2faf]
    =================================
    0x2d9: v2d9(0x2faf) = CONST 
    0x2dc: JUMP v2d9(0x2faf)

    Begin block 0x2faf
    prev=[0x2d9], succ=[]
    =================================
    0x2fb0: v2fb0(0x0) = CONST 
    0x2fb3: REVERT v2fb0(0x0), v2fb0(0x0)

    Begin block 0x39a7
    prev=[0x2ce], succ=[]
    =================================
    0x39a8: v39a8(0x36b) = CONST 
    0x39a9: CALLPRIVATE v39a8(0x36b)

    Begin block 0x256
    prev=[0x24a], succ=[0x286, 0x261]
    =================================
    0x257: v257(0x29ef1919) = CONST 
    0x25c: v25c = GT v257(0x29ef1919), v1f
    0x25d: v25d(0x286) = CONST 
    0x260: JUMPI v25d(0x286), v25c

    Begin block 0x286
    prev=[0x256], succ=[0x39aa, 0x292]
    =================================
    0x288: v288(0x1a5e2e54) = CONST 
    0x28d: v28d = EQ v288(0x1a5e2e54), v1f
    0x398b: v398b(0x39aa) = CONST 
    0x398c: JUMPI v398b(0x39aa), v28d

    Begin block 0x39aa
    prev=[0x286], succ=[]
    =================================
    0x39ab: v39ab(0x388) = CONST 
    0x39ac: CALLPRIVATE v39ab(0x388)

    Begin block 0x292
    prev=[0x286], succ=[0x39ad, 0x29d]
    =================================
    0x293: v293(0x207395b1) = CONST 
    0x298: v298 = EQ v293(0x207395b1), v1f
    0x398d: v398d(0x39ad) = CONST 
    0x398e: JUMPI v398d(0x39ad), v298

    Begin block 0x39ad
    prev=[0x292], succ=[]
    =================================
    0x39ae: v39ae(0x3bb) = CONST 
    0x39af: CALLPRIVATE v39ae(0x3bb)

    Begin block 0x29d
    prev=[0x292], succ=[0x2a8, 0x39b0]
    =================================
    0x29e: v29e(0x27aac633) = CONST 
    0x2a3: v2a3 = EQ v29e(0x27aac633), v1f
    0x398f: v398f(0x39b0) = CONST 
    0x3990: JUMPI v398f(0x39b0), v2a3

    Begin block 0x2a8
    prev=[0x29d], succ=[0x2f8b]
    =================================
    0x2a8: v2a8(0x2f8b) = CONST 
    0x2ab: JUMP v2a8(0x2f8b)

    Begin block 0x2f8b
    prev=[0x2a8], succ=[]
    =================================
    0x2f8c: v2f8c(0x0) = CONST 
    0x2f8f: REVERT v2f8c(0x0), v2f8c(0x0)

    Begin block 0x39b0
    prev=[0x29d], succ=[]
    =================================
    0x39b1: v39b1(0x48e) = CONST 
    0x39b2: CALLPRIVATE v39b1(0x48e)

    Begin block 0x261
    prev=[0x256], succ=[0x39b3, 0x26c]
    =================================
    0x262: v262(0x29ef1919) = CONST 
    0x267: v267 = EQ v262(0x29ef1919), v1f
    0x3985: v3985(0x39b3) = CONST 
    0x3986: JUMPI v3985(0x39b3), v267

    Begin block 0x39b3
    prev=[0x261], succ=[]
    =================================
    0x39b4: v39b4(0x496) = CONST 
    0x39b5: CALLPRIVATE v39b4(0x496)

    Begin block 0x26c
    prev=[0x261], succ=[0x39b6, 0x277]
    =================================
    0x26d: v26d(0x2c56320f) = CONST 
    0x272: v272 = EQ v26d(0x2c56320f), v1f
    0x3987: v3987(0x39b6) = CONST 
    0x3988: JUMPI v3987(0x39b6), v272

    Begin block 0x39b6
    prev=[0x26c], succ=[]
    =================================
    0x39b7: v39b7(0x49e) = CONST 
    0x39b8: CALLPRIVATE v39b7(0x49e)

    Begin block 0x277
    prev=[0x26c], succ=[0x282, 0x39b9]
    =================================
    0x278: v278(0x2e9c7b65) = CONST 
    0x27d: v27d = EQ v278(0x2e9c7b65), v1f
    0x3989: v3989(0x39b9) = CONST 
    0x398a: JUMPI v3989(0x39b9), v27d

    Begin block 0x282
    prev=[0x277], succ=[0x2f67]
    =================================
    0x282: v282(0x2f67) = CONST 
    0x285: JUMP v282(0x2f67)

    Begin block 0x2f67
    prev=[0x282], succ=[]
    =================================
    0x2f68: v2f68(0x0) = CONST 
    0x2f6b: REVERT v2f68(0x0), v2f68(0x0)

    Begin block 0x39b9
    prev=[0x277], succ=[]
    =================================
    0x39ba: v39ba(0x4a6) = CONST 
    0x39bb: CALLPRIVATE v39ba(0x4a6)

    Begin block 0x19d
    prev=[0x191], succ=[0x1fe, 0x1a8]
    =================================
    0x19e: v19e(0x451111b7) = CONST 
    0x1a3: v1a3 = GT v19e(0x451111b7), v1f
    0x1a4: v1a4(0x1fe) = CONST 
    0x1a7: JUMPI v1a4(0x1fe), v1a3

    Begin block 0x1fe
    prev=[0x19d], succ=[0x22f, 0x20a]
    =================================
    0x200: v200(0x3e38fd00) = CONST 
    0x205: v205 = GT v200(0x3e38fd00), v1f
    0x206: v206(0x22f) = CONST 
    0x209: JUMPI v206(0x22f), v205

    Begin block 0x22f
    prev=[0x1fe], succ=[0x39bc, 0x23b]
    =================================
    0x231: v231(0x392e53cd) = CONST 
    0x236: v236 = EQ v231(0x392e53cd), v1f
    0x3981: v3981(0x39bc) = CONST 
    0x3982: JUMPI v3981(0x39bc), v236

    Begin block 0x39bc
    prev=[0x22f], succ=[]
    =================================
    0x39bd: v39bd(0x4ae) = CONST 
    0x39be: CALLPRIVATE v39bd(0x4ae)

    Begin block 0x23b
    prev=[0x22f], succ=[0x246, 0x39bf]
    =================================
    0x23c: v23c(0x3cc3d23b) = CONST 
    0x241: v241 = EQ v23c(0x3cc3d23b), v1f
    0x3983: v3983(0x39bf) = CONST 
    0x3984: JUMPI v3983(0x39bf), v241

    Begin block 0x246
    prev=[0x23b], succ=[0x2f43]
    =================================
    0x246: v246(0x2f43) = CONST 
    0x249: JUMP v246(0x2f43)

    Begin block 0x2f43
    prev=[0x246], succ=[]
    =================================
    0x2f44: v2f44(0x0) = CONST 
    0x2f47: REVERT v2f44(0x0), v2f44(0x0)

    Begin block 0x39bf
    prev=[0x23b], succ=[]
    =================================
    0x39c0: v39c0(0x4b6) = CONST 
    0x39c1: CALLPRIVATE v39c0(0x4b6)

    Begin block 0x20a
    prev=[0x1fe], succ=[0x39c2, 0x215]
    =================================
    0x20b: v20b(0x3e38fd00) = CONST 
    0x210: v210 = EQ v20b(0x3e38fd00), v1f
    0x397b: v397b(0x39c2) = CONST 
    0x397c: JUMPI v397b(0x39c2), v210

    Begin block 0x39c2
    prev=[0x20a], succ=[]
    =================================
    0x39c3: v39c3(0x4be) = CONST 
    0x39c4: CALLPRIVATE v39c3(0x4be)

    Begin block 0x215
    prev=[0x20a], succ=[0x39c5, 0x220]
    =================================
    0x216: v216(0x3f53fbec) = CONST 
    0x21b: v21b = EQ v216(0x3f53fbec), v1f
    0x397d: v397d(0x39c5) = CONST 
    0x397e: JUMPI v397d(0x39c5), v21b

    Begin block 0x39c5
    prev=[0x215], succ=[]
    =================================
    0x39c6: v39c6(0x4f7) = CONST 
    0x39c7: CALLPRIVATE v39c6(0x4f7)

    Begin block 0x220
    prev=[0x215], succ=[0x22b, 0x39c8]
    =================================
    0x221: v221(0x40af7ba5) = CONST 
    0x226: v226 = EQ v221(0x40af7ba5), v1f
    0x397f: v397f(0x39c8) = CONST 
    0x3980: JUMPI v397f(0x39c8), v226

    Begin block 0x22b
    prev=[0x220], succ=[0x2f1f]
    =================================
    0x22b: v22b(0x2f1f) = CONST 
    0x22e: JUMP v22b(0x2f1f)

    Begin block 0x2f1f
    prev=[0x22b], succ=[]
    =================================
    0x2f20: v2f20(0x0) = CONST 
    0x2f23: REVERT v2f20(0x0), v2f20(0x0)

    Begin block 0x39c8
    prev=[0x220], succ=[]
    =================================
    0x39c9: v39c9(0x52a) = CONST 
    0x39ca: CALLPRIVATE v39c9(0x52a)

    Begin block 0x1a8
    prev=[0x19d], succ=[0x1d8, 0x1b3]
    =================================
    0x1a9: v1a9(0x570ca735) = CONST 
    0x1ae: v1ae = GT v1a9(0x570ca735), v1f
    0x1af: v1af(0x1d8) = CONST 
    0x1b2: JUMPI v1af(0x1d8), v1ae

    Begin block 0x1d8
    prev=[0x1a8], succ=[0x39cb, 0x1e4]
    =================================
    0x1da: v1da(0x451111b7) = CONST 
    0x1df: v1df = EQ v1da(0x451111b7), v1f
    0x3975: v3975(0x39cb) = CONST 
    0x3976: JUMPI v3975(0x39cb), v1df

    Begin block 0x39cb
    prev=[0x1d8], succ=[]
    =================================
    0x39cc: v39cc(0x547) = CONST 
    0x39cd: CALLPRIVATE v39cc(0x547)

    Begin block 0x1e4
    prev=[0x1d8], succ=[0x39ce, 0x1ef]
    =================================
    0x1e5: v1e5(0x51adeb57) = CONST 
    0x1ea: v1ea = EQ v1e5(0x51adeb57), v1f
    0x3977: v3977(0x39ce) = CONST 
    0x3978: JUMPI v3977(0x39ce), v1ea

    Begin block 0x39ce
    prev=[0x1e4], succ=[]
    =================================
    0x39cf: v39cf(0x578) = CONST 
    0x39d0: CALLPRIVATE v39cf(0x578)

    Begin block 0x1ef
    prev=[0x1e4], succ=[0x1fa, 0x39d1]
    =================================
    0x1f0: v1f0(0x54575af4) = CONST 
    0x1f5: v1f5 = EQ v1f0(0x54575af4), v1f
    0x3979: v3979(0x39d1) = CONST 
    0x397a: JUMPI v3979(0x39d1), v1f5

    Begin block 0x1fa
    prev=[0x1ef], succ=[0x2efb]
    =================================
    0x1fa: v1fa(0x2efb) = CONST 
    0x1fd: JUMP v1fa(0x2efb)

    Begin block 0x2efb
    prev=[0x1fa], succ=[]
    =================================
    0x2efc: v2efc(0x0) = CONST 
    0x2eff: REVERT v2efc(0x0), v2efc(0x0)

    Begin block 0x39d1
    prev=[0x1ef], succ=[]
    =================================
    0x39d2: v39d2(0x580) = CONST 
    0x39d3: CALLPRIVATE v39d2(0x580)

    Begin block 0x1b3
    prev=[0x1a8], succ=[0x39d4, 0x1be]
    =================================
    0x1b4: v1b4(0x570ca735) = CONST 
    0x1b9: v1b9 = EQ v1b4(0x570ca735), v1f
    0x396f: v396f(0x39d4) = CONST 
    0x3970: JUMPI v396f(0x39d4), v1b9

    Begin block 0x39d4
    prev=[0x1b3], succ=[]
    =================================
    0x39d5: v39d5(0x5c3) = CONST 
    0x39d6: CALLPRIVATE v39d5(0x5c3)

    Begin block 0x1be
    prev=[0x1b3], succ=[0x39d7, 0x1c9]
    =================================
    0x1bf: v1bf(0x61d027b3) = CONST 
    0x1c4: v1c4 = EQ v1bf(0x61d027b3), v1f
    0x3971: v3971(0x39d7) = CONST 
    0x3972: JUMPI v3971(0x39d7), v1c4

    Begin block 0x39d7
    prev=[0x1be], succ=[]
    =================================
    0x39d8: v39d8(0x5cb) = CONST 
    0x39d9: CALLPRIVATE v39d8(0x5cb)

    Begin block 0x1c9
    prev=[0x1be], succ=[0x1d4, 0x39da]
    =================================
    0x1ca: v1ca(0x691be4d8) = CONST 
    0x1cf: v1cf = EQ v1ca(0x691be4d8), v1f
    0x3973: v3973(0x39da) = CONST 
    0x3974: JUMPI v3973(0x39da), v1cf

    Begin block 0x1d4
    prev=[0x1c9], succ=[0x2ed7]
    =================================
    0x1d4: v1d4(0x2ed7) = CONST 
    0x1d7: JUMP v1d4(0x2ed7)

    Begin block 0x2ed7
    prev=[0x1d4], succ=[]
    =================================
    0x2ed8: v2ed8(0x0) = CONST 
    0x2edb: REVERT v2ed8(0x0), v2ed8(0x0)

    Begin block 0x39da
    prev=[0x1c9], succ=[]
    =================================
    0x39db: v39db(0x5d3) = CONST 
    0x39dc: CALLPRIVATE v39db(0x5d3)

    Begin block 0x2b
    prev=[0x1a], succ=[0xe3, 0x36]
    =================================
    0x2c: v2c(0xaaec5061) = CONST 
    0x31: v31 = GT v2c(0xaaec5061), v1f
    0x32: v32(0xe3) = CONST 
    0x35: JUMPI v32(0xe3), v31

    Begin block 0xe3
    prev=[0x2b], succ=[0x145, 0xef]
    =================================
    0xe5: ve5(0x94bdf63e) = CONST 
    0xea: vea = GT ve5(0x94bdf63e), v1f
    0xeb: veb(0x145) = CONST 
    0xee: JUMPI veb(0x145), vea

    Begin block 0x145
    prev=[0xe3], succ=[0x176, 0x151]
    =================================
    0x147: v147(0x8745e2e9) = CONST 
    0x14c: v14c = GT v147(0x8745e2e9), v1f
    0x14d: v14d(0x176) = CONST 
    0x150: JUMPI v14d(0x176), v14c

    Begin block 0x176
    prev=[0x145], succ=[0x39dd, 0x182]
    =================================
    0x178: v178(0x6a1463c8) = CONST 
    0x17d: v17d = EQ v178(0x6a1463c8), v1f
    0x396b: v396b(0x39dd) = CONST 
    0x396c: JUMPI v396b(0x39dd), v17d

    Begin block 0x39dd
    prev=[0x176], succ=[]
    =================================
    0x39de: v39de(0x60c) = CONST 
    0x39df: CALLPRIVATE v39de(0x60c)

    Begin block 0x182
    prev=[0x176], succ=[0x18d, 0x39e0]
    =================================
    0x183: v183(0x71bc6a83) = CONST 
    0x188: v188 = EQ v183(0x71bc6a83), v1f
    0x396d: v396d(0x39e0) = CONST 
    0x396e: JUMPI v396d(0x39e0), v188

    Begin block 0x18d
    prev=[0x182], succ=[0x2eb3]
    =================================
    0x18d: v18d(0x2eb3) = CONST 
    0x190: JUMP v18d(0x2eb3)

    Begin block 0x2eb3
    prev=[0x18d], succ=[]
    =================================
    0x2eb4: v2eb4(0x0) = CONST 
    0x2eb7: REVERT v2eb4(0x0), v2eb4(0x0)

    Begin block 0x39e0
    prev=[0x182], succ=[]
    =================================
    0x39e1: v39e1(0x629) = CONST 
    0x39e2: CALLPRIVATE v39e1(0x629)

    Begin block 0x151
    prev=[0x145], succ=[0x39e3, 0x15c]
    =================================
    0x152: v152(0x8745e2e9) = CONST 
    0x157: v157 = EQ v152(0x8745e2e9), v1f
    0x3965: v3965(0x39e3) = CONST 
    0x3966: JUMPI v3965(0x39e3), v157

    Begin block 0x39e3
    prev=[0x151], succ=[]
    =================================
    0x39e4: v39e4(0x64c) = CONST 
    0x39e5: CALLPRIVATE v39e4(0x64c)

    Begin block 0x15c
    prev=[0x151], succ=[0x39e6, 0x167]
    =================================
    0x15d: v15d(0x8eda90ad) = CONST 
    0x162: v162 = EQ v15d(0x8eda90ad), v1f
    0x3967: v3967(0x39e6) = CONST 
    0x3968: JUMPI v3967(0x39e6), v162

    Begin block 0x39e6
    prev=[0x15c], succ=[]
    =================================
    0x39e7: v39e7(0x654) = CONST 
    0x39e8: CALLPRIVATE v39e7(0x654)

    Begin block 0x167
    prev=[0x15c], succ=[0x172, 0x39e9]
    =================================
    0x168: v168(0x900cf0cf) = CONST 
    0x16d: v16d = EQ v168(0x900cf0cf), v1f
    0x3969: v3969(0x39e9) = CONST 
    0x396a: JUMPI v3969(0x39e9), v16d

    Begin block 0x172
    prev=[0x167], succ=[0x2e8f]
    =================================
    0x172: v172(0x2e8f) = CONST 
    0x175: JUMP v172(0x2e8f)

    Begin block 0x2e8f
    prev=[0x172], succ=[]
    =================================
    0x2e90: v2e90(0x0) = CONST 
    0x2e93: REVERT v2e90(0x0), v2e90(0x0)

    Begin block 0x39e9
    prev=[0x167], succ=[]
    =================================
    0x39ea: v39ea(0x65c) = CONST 
    0x39eb: CALLPRIVATE v39ea(0x65c)

    Begin block 0xef
    prev=[0xe3], succ=[0x11f, 0xfa]
    =================================
    0xf0: vf0(0xa204452b) = CONST 
    0xf5: vf5 = GT vf0(0xa204452b), v1f
    0xf6: vf6(0x11f) = CONST 
    0xf9: JUMPI vf6(0x11f), vf5

    Begin block 0x11f
    prev=[0xef], succ=[0x39ec, 0x12b]
    =================================
    0x121: v121(0x94bdf63e) = CONST 
    0x126: v126 = EQ v121(0x94bdf63e), v1f
    0x395f: v395f(0x39ec) = CONST 
    0x3960: JUMPI v395f(0x39ec), v126

    Begin block 0x39ec
    prev=[0x11f], succ=[]
    =================================
    0x39ed: v39ed(0x664) = CONST 
    0x39ee: CALLPRIVATE v39ed(0x664)

    Begin block 0x12b
    prev=[0x11f], succ=[0x39ef, 0x136]
    =================================
    0x12c: v12c(0x98b762a1) = CONST 
    0x131: v131 = EQ v12c(0x98b762a1), v1f
    0x3961: v3961(0x39ef) = CONST 
    0x3962: JUMPI v3961(0x39ef), v131

    Begin block 0x39ef
    prev=[0x12b], succ=[]
    =================================
    0x39f0: v39f0(0x66c) = CONST 
    0x39f1: CALLPRIVATE v39f0(0x66c)

    Begin block 0x136
    prev=[0x12b], succ=[0x141, 0x39f2]
    =================================
    0x137: v137(0x99f85b18) = CONST 
    0x13c: v13c = EQ v137(0x99f85b18), v1f
    0x3963: v3963(0x39f2) = CONST 
    0x3964: JUMPI v3963(0x39f2), v13c

    Begin block 0x141
    prev=[0x136], succ=[0x2e6b]
    =================================
    0x141: v141(0x2e6b) = CONST 
    0x144: JUMP v141(0x2e6b)

    Begin block 0x2e6b
    prev=[0x141], succ=[]
    =================================
    0x2e6c: v2e6c(0x0) = CONST 
    0x2e6f: REVERT v2e6c(0x0), v2e6c(0x0)

    Begin block 0x39f2
    prev=[0x136], succ=[]
    =================================
    0x39f3: v39f3(0x689) = CONST 
    0x39f4: CALLPRIVATE v39f3(0x689)

    Begin block 0xfa
    prev=[0xef], succ=[0x39f5, 0x105]
    =================================
    0xfb: vfb(0xa204452b) = CONST 
    0x100: v100 = EQ vfb(0xa204452b), v1f
    0x3959: v3959(0x39f5) = CONST 
    0x395a: JUMPI v3959(0x39f5), v100

    Begin block 0x39f5
    prev=[0xfa], succ=[]
    =================================
    0x39f6: v39f6(0x691) = CONST 
    0x39f7: CALLPRIVATE v39f6(0x691)

    Begin block 0x105
    prev=[0xfa], succ=[0x39f8, 0x110]
    =================================
    0x106: v106(0xa688cfd7) = CONST 
    0x10b: v10b = EQ v106(0xa688cfd7), v1f
    0x395b: v395b(0x39f8) = CONST 
    0x395c: JUMPI v395b(0x39f8), v10b

    Begin block 0x39f8
    prev=[0x105], succ=[]
    =================================
    0x39f9: v39f9(0x6ae) = CONST 
    0x39fa: CALLPRIVATE v39f9(0x6ae)

    Begin block 0x110
    prev=[0x105], succ=[0x11b, 0x39fb]
    =================================
    0x111: v111(0xa7566bcf) = CONST 
    0x116: v116 = EQ v111(0xa7566bcf), v1f
    0x395d: v395d(0x39fb) = CONST 
    0x395e: JUMPI v395d(0x39fb), v116

    Begin block 0x11b
    prev=[0x110], succ=[0x2e47]
    =================================
    0x11b: v11b(0x2e47) = CONST 
    0x11e: JUMP v11b(0x2e47)

    Begin block 0x2e47
    prev=[0x11b], succ=[]
    =================================
    0x2e48: v2e48(0x0) = CONST 
    0x2e4b: REVERT v2e48(0x0), v2e48(0x0)

    Begin block 0x39fb
    prev=[0x110], succ=[]
    =================================
    0x39fc: v39fc(0x6b6) = CONST 
    0x39fd: CALLPRIVATE v39fc(0x6b6)

    Begin block 0x36
    prev=[0x2b], succ=[0x97, 0x41]
    =================================
    0x37: v37(0xc476dd27) = CONST 
    0x3c: v3c = GT v37(0xc476dd27), v1f
    0x3d: v3d(0x97) = CONST 
    0x40: JUMPI v3d(0x97), v3c

    Begin block 0x97
    prev=[0x36], succ=[0xc8, 0xa3]
    =================================
    0x99: v99(0xb8a878f9) = CONST 
    0x9e: v9e = GT v99(0xb8a878f9), v1f
    0x9f: v9f(0xc8) = CONST 
    0xa2: JUMPI v9f(0xc8), v9e

    Begin block 0xc8
    prev=[0x97], succ=[0x39fe, 0xd4]
    =================================
    0xca: vca(0xaaec5061) = CONST 
    0xcf: vcf = EQ vca(0xaaec5061), v1f
    0x3955: v3955(0x39fe) = CONST 
    0x3956: JUMPI v3955(0x39fe), vcf

    Begin block 0x39fe
    prev=[0xc8], succ=[]
    =================================
    0x39ff: v39ff(0x6be) = CONST 
    0x3a00: CALLPRIVATE v39ff(0x6be)

    Begin block 0xd4
    prev=[0xc8], succ=[0xdf, 0x3a01]
    =================================
    0xd5: vd5(0xb3ab15fb) = CONST 
    0xda: vda = EQ vd5(0xb3ab15fb), v1f
    0x3957: v3957(0x3a01) = CONST 
    0x3958: JUMPI v3957(0x3a01), vda

    Begin block 0xdf
    prev=[0xd4], succ=[0x2e23]
    =================================
    0xdf: vdf(0x2e23) = CONST 
    0xe2: JUMP vdf(0x2e23)

    Begin block 0x2e23
    prev=[0xdf], succ=[]
    =================================
    0x2e24: v2e24(0x0) = CONST 
    0x2e27: REVERT v2e24(0x0), v2e24(0x0)

    Begin block 0x3a01
    prev=[0xd4], succ=[]
    =================================
    0x3a02: v3a02(0x6c6) = CONST 
    0x3a03: CALLPRIVATE v3a02(0x6c6)

    Begin block 0xa3
    prev=[0x97], succ=[0x3a04, 0xae]
    =================================
    0xa4: va4(0xb8a878f9) = CONST 
    0xa9: va9 = EQ va4(0xb8a878f9), v1f
    0x394f: v394f(0x3a04) = CONST 
    0x3950: JUMPI v394f(0x3a04), va9

    Begin block 0x3a04
    prev=[0xa3], succ=[]
    =================================
    0x3a05: v3a05(0x6f9) = CONST 
    0x3a06: CALLPRIVATE v3a05(0x6f9)

    Begin block 0xae
    prev=[0xa3], succ=[0x3a07, 0xb9]
    =================================
    0xaf: vaf(0xbc0b1df6) = CONST 
    0xb4: vb4 = EQ vaf(0xbc0b1df6), v1f
    0x3951: v3951(0x3a07) = CONST 
    0x3952: JUMPI v3951(0x3a07), vb4

    Begin block 0x3a07
    prev=[0xae], succ=[]
    =================================
    0x3a08: v3a08(0x701) = CONST 
    0x3a09: CALLPRIVATE v3a08(0x701)

    Begin block 0xb9
    prev=[0xae], succ=[0xc4, 0x3a0a]
    =================================
    0xba: vba(0xc0c53b8b) = CONST 
    0xbf: vbf = EQ vba(0xc0c53b8b), v1f
    0x3953: v3953(0x3a0a) = CONST 
    0x3954: JUMPI v3953(0x3a0a), vbf

    Begin block 0xc4
    prev=[0xb9], succ=[0x2dff]
    =================================
    0xc4: vc4(0x2dff) = CONST 
    0xc7: JUMP vc4(0x2dff)

    Begin block 0x2dff
    prev=[0xc4], succ=[]
    =================================
    0x2e00: v2e00(0x0) = CONST 
    0x2e03: REVERT v2e00(0x0), v2e00(0x0)

    Begin block 0x3a0a
    prev=[0xb9], succ=[]
    =================================
    0x3a0b: v3a0b(0x72a) = CONST 
    0x3a0c: CALLPRIVATE v3a0b(0x72a)

    Begin block 0x41
    prev=[0x36], succ=[0x71, 0x4c]
    =================================
    0x42: v42(0xc8412d02) = CONST 
    0x47: v47 = GT v42(0xc8412d02), v1f
    0x48: v48(0x71) = CONST 
    0x4b: JUMPI v48(0x71), v47

    Begin block 0x71
    prev=[0x41], succ=[0x3a0d, 0x7d]
    =================================
    0x73: v73(0xc476dd27) = CONST 
    0x78: v78 = EQ v73(0xc476dd27), v1f
    0x3949: v3949(0x3a0d) = CONST 
    0x394a: JUMPI v3949(0x3a0d), v78

    Begin block 0x3a0d
    prev=[0x71], succ=[]
    =================================
    0x3a0e: v3a0e(0x76f) = CONST 
    0x3a0f: CALLPRIVATE v3a0e(0x76f)

    Begin block 0x7d
    prev=[0x71], succ=[0x3a10, 0x88]
    =================================
    0x7e: v7e(0xc5967c26) = CONST 
    0x83: v83 = EQ v7e(0xc5967c26), v1f
    0x394b: v394b(0x3a10) = CONST 
    0x394c: JUMPI v394b(0x3a10), v83

    Begin block 0x3a10
    prev=[0x7d], succ=[]
    =================================
    0x3a11: v3a11(0x777) = CONST 
    0x3a12: CALLPRIVATE v3a11(0x777)

    Begin block 0x88
    prev=[0x7d], succ=[0x93, 0x3a13]
    =================================
    0x89: v89(0xc81982e8) = CONST 
    0x8e: v8e = EQ v89(0xc81982e8), v1f
    0x394d: v394d(0x3a13) = CONST 
    0x394e: JUMPI v394d(0x3a13), v8e

    Begin block 0x93
    prev=[0x88], succ=[0x2ddb]
    =================================
    0x93: v93(0x2ddb) = CONST 
    0x96: JUMP v93(0x2ddb)

    Begin block 0x2ddb
    prev=[0x93], succ=[]
    =================================
    0x2ddc: v2ddc(0x0) = CONST 
    0x2ddf: REVERT v2ddc(0x0), v2ddc(0x0)

    Begin block 0x3a13
    prev=[0x88], succ=[]
    =================================
    0x3a14: v3a14(0x77f) = CONST 
    0x3a15: CALLPRIVATE v3a14(0x77f)

    Begin block 0x4c
    prev=[0x41], succ=[0x3a16, 0x57]
    =================================
    0x4d: v4d(0xc8412d02) = CONST 
    0x52: v52 = EQ v4d(0xc8412d02), v1f
    0x3943: v3943(0x3a16) = CONST 
    0x3944: JUMPI v3943(0x3a16), v52

    Begin block 0x3a16
    prev=[0x4c], succ=[]
    =================================
    0x3a17: v3a17(0x787) = CONST 
    0x3a18: CALLPRIVATE v3a17(0x787)

    Begin block 0x57
    prev=[0x4c], succ=[0x3a19, 0x62]
    =================================
    0x58: v58(0xcac9aa9a) = CONST 
    0x5d: v5d = EQ v58(0xcac9aa9a), v1f
    0x3945: v3945(0x3a19) = CONST 
    0x3946: JUMPI v3945(0x3a19), v5d

    Begin block 0x3a19
    prev=[0x57], succ=[]
    =================================
    0x3a1a: v3a1a(0x78f) = CONST 
    0x3a1b: CALLPRIVATE v3a1a(0x78f)

    Begin block 0x62
    prev=[0x57], succ=[0x6d, 0x3a1c]
    =================================
    0x63: v63(0xe1f095aa) = CONST 
    0x68: v68 = EQ v63(0xe1f095aa), v1f
    0x3947: v3947(0x3a1c) = CONST 
    0x3948: JUMPI v3947(0x3a1c), v68

    Begin block 0x6d
    prev=[0x62], succ=[0x2db7]
    =================================
    0x6d: v6d(0x2db7) = CONST 
    0x70: JUMP v6d(0x2db7)

    Begin block 0x2db7
    prev=[0x6d], succ=[]
    =================================
    0x2db8: v2db8(0x0) = CONST 
    0x2dbb: REVERT v2db8(0x0), v2db8(0x0)

    Begin block 0x3a1c
    prev=[0x62], succ=[]
    =================================
    0x3a1d: v3a1d(0x797) = CONST 
    0x3a1e: CALLPRIVATE v3a1d(0x797)

    Begin block 0x3a1f
    prev=[0x10], succ=[]
    =================================
    0x3a20: v3a20(0x2d93) = CONST 
    0x3a21: CALLPRIVATE v3a20(0x2d93)

}

function 0x15f8(0x15f8arg0x0) private {
    Begin block 0x15f8
    prev=[], succ=[0x1603]
    =================================
    0x15f9: v15f9(0x0) = CONST 
    0x15fc: v15fc(0x1603) = CONST 
    0x15ff: v15ff(0x2272) = CONST 
    0x1602: v1602_0 = CALLPRIVATE v15ff(0x2272), v15fc(0x1603)

    Begin block 0x1603
    prev=[0x15f8], succ=[0x1615, 0x378a]
    =================================
    0x1606: v1606(0xde0b6b3a7640000) = CONST 
    0x1610: v1610 = LT v1602_0, v1606(0xde0b6b3a7640000)
    0x1611: v1611(0x378a) = CONST 
    0x1614: JUMPI v1611(0x378a), v1610

    Begin block 0x1615
    prev=[0x1603], succ=[0x161e]
    =================================
    0x1615: v1615(0x0) = CONST 
    0x1617: v1617(0x161e) = CONST 
    0x161a: v161a(0x1719) = CONST 
    0x161d: v161d_0 = CALLPRIVATE v161a(0x1719), v1617(0x161e)

    Begin block 0x161e
    prev=[0x1615], succ=[0x1692, 0x1696]
    =================================
    0x1621: v1621(0x0) = CONST 
    0x1623: v1623(0x16c8) = CONST 
    0x1626: v1626(0x2710) = CONST 
    0x1629: v1629(0x37ad) = CONST 
    0x162c: v162c(0xd) = CONST 
    0x162e: v162e = SLOAD v162c(0xd)
    0x162f: v162f(0x2) = CONST 
    0x1631: v1631(0x0) = CONST 
    0x1634: v1634 = SLOAD v162f(0x2)
    0x1636: v1636(0x100) = CONST 
    0x1639: v1639(0x1) = EXP v1636(0x100), v1631(0x0)
    0x163b: v163b = DIV v1634, v1639(0x1)
    0x163c: v163c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1651: v1651 = AND v163c(0xffffffffffffffffffffffffffffffffffffffff), v163b
    0x1652: v1652(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1667: v1667 = AND v1652(0xffffffffffffffffffffffffffffffffffffffff), v1651
    0x1668: v1668(0x18160ddd) = CONST 
    0x166d: v166d(0x40) = CONST 
    0x166f: v166f = MLOAD v166d(0x40)
    0x1671: v1671(0xffffffff) = CONST 
    0x1676: v1676(0x18160ddd) = AND v1671(0xffffffff), v1668(0x18160ddd)
    0x1677: v1677(0xe0) = CONST 
    0x1679: v1679(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL v1677(0xe0), v1676(0x18160ddd)
    0x167b: MSTORE v166f, v1679(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x167c: v167c(0x4) = CONST 
    0x167e: v167e = ADD v167c(0x4), v166f
    0x167f: v167f(0x20) = CONST 
    0x1681: v1681(0x40) = CONST 
    0x1683: v1683 = MLOAD v1681(0x40)
    0x1686: v1686(0x4) = SUB v167e, v1683
    0x168a: v168a = EXTCODESIZE v1667
    0x168b: v168b = ISZERO v168a
    0x168d: v168d = ISZERO v168b
    0x168e: v168e(0x1696) = CONST 
    0x1691: JUMPI v168e(0x1696), v168d

    Begin block 0x1692
    prev=[0x161e], succ=[]
    =================================
    0x1692: v1692(0x0) = CONST 
    0x1695: REVERT v1692(0x0), v1692(0x0)

    Begin block 0x1696
    prev=[0x161e], succ=[0x16a1, 0x16aa]
    =================================
    0x1698: v1698 = GAS 
    0x1699: v1699 = STATICCALL v1698, v1667, v1683, v1686(0x4), v1683, v167f(0x20)
    0x169a: v169a = ISZERO v1699
    0x169c: v169c = ISZERO v169a
    0x169d: v169d(0x16aa) = CONST 
    0x16a0: JUMPI v169d(0x16aa), v169c

    Begin block 0x16a1
    prev=[0x1696], succ=[]
    =================================
    0x16a1: v16a1 = RETURNDATASIZE 
    0x16a2: v16a2(0x0) = CONST 
    0x16a5: RETURNDATACOPY v16a2(0x0), v16a2(0x0), v16a1
    0x16a6: v16a6 = RETURNDATASIZE 
    0x16a7: v16a7(0x0) = CONST 
    0x16a9: REVERT v16a7(0x0), v16a6

    Begin block 0x16aa
    prev=[0x1696], succ=[0x16bc, 0x16c0]
    =================================
    0x16af: v16af(0x40) = CONST 
    0x16b1: v16b1 = MLOAD v16af(0x40)
    0x16b2: v16b2 = RETURNDATASIZE 
    0x16b3: v16b3(0x20) = CONST 
    0x16b6: v16b6 = LT v16b2, v16b3(0x20)
    0x16b7: v16b7 = ISZERO v16b6
    0x16b8: v16b8(0x16c0) = CONST 
    0x16bb: JUMPI v16b8(0x16c0), v16b7

    Begin block 0x16bc
    prev=[0x16aa], succ=[]
    =================================
    0x16bc: v16bc(0x0) = CONST 
    0x16bf: REVERT v16bc(0x0), v16bc(0x0)

    Begin block 0x16c0
    prev=[0x16aa], succ=[0x23c10x15f8]
    =================================
    0x16c2: v16c2 = MLOAD v16b1
    0x16c4: v16c4(0x23c1) = CONST 
    0x16c7: JUMP v16c4(0x23c1)

    Begin block 0x23c10x15f8
    prev=[0x16c0], succ=[0x23d00x15f8, 0x23c90x15f8]
    =================================
    0x23c20x15f8: v15f823c2(0x0) = CONST 
    0x23c50x15f8: v15f823c5(0x23d0) = CONST 
    0x23c80x15f8: JUMPI v15f823c5(0x23d0), v16c2

    Begin block 0x23d00x15f8
    prev=[0x23c10x15f8], succ=[0x23dc0x15f8, 0x23dd0x15f8]
    =================================
    0x23d30x15f8: v15f823d3 = MUL v162e, v16c2
    0x23d80x15f8: v15f823d8(0x23dd) = CONST 
    0x23db0x15f8: JUMPI v15f823d8(0x23dd), v16c2

    Begin block 0x23dc0x15f8
    prev=[0x23d00x15f8], succ=[]
    =================================
    0x23dc0x15f8: THROW 

    Begin block 0x23dd0x15f8
    prev=[0x23d00x15f8], succ=[0x23e40x15f8, 0x23b80x15f8]
    =================================
    0x23de0x15f8: v15f823de = DIV v15f823d3, v16c2
    0x23df0x15f8: v15f823df = EQ v15f823de, v162e
    0x23e00x15f8: v15f823e0(0x23b8) = CONST 
    0x23e30x15f8: JUMPI v15f823e0(0x23b8), v15f823df

    Begin block 0x23e40x15f8
    prev=[0x23dd0x15f8], succ=[]
    =================================
    0x23e40x15f8: v15f823e4(0x40) = CONST 
    0x23e60x15f8: v15f823e6 = MLOAD v15f823e4(0x40)
    0x23e70x15f8: v15f823e7(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x24090x15f8: MSTORE v15f823e6, v15f823e7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x240a0x15f8: v15f8240a(0x4) = CONST 
    0x240c0x15f8: v15f8240c = ADD v15f8240a(0x4), v15f823e6
    0x240f0x15f8: v15f8240f(0x20) = CONST 
    0x24110x15f8: v15f82411 = ADD v15f8240f(0x20), v15f8240c
    0x24140x15f8: v15f82414(0x20) = SUB v15f82411, v15f8240c
    0x24160x15f8: MSTORE v15f8240c, v15f82414(0x20)
    0x24170x15f8: v15f82417(0x21) = CONST 
    0x241a0x15f8: MSTORE v15f82411, v15f82417(0x21)
    0x241b0x15f8: v15f8241b(0x20) = CONST 
    0x241d0x15f8: v15f8241d = ADD v15f8241b(0x20), v15f82411
    0x241f0x15f8: v15f8241f(0x2c75) = CONST 
    0x24220x15f8: v15f82422(0x21) = CONST 
    0x24250x15f8: CODECOPY v15f8241d, v15f8241f(0x2c75), v15f82422(0x21)
    0x24260x15f8: v15f82426(0x40) = CONST 
    0x24280x15f8: v15f82428 = ADD v15f82426(0x40), v15f8241d
    0x242c0x15f8: v15f8242c(0x40) = CONST 
    0x242e0x15f8: v15f8242e = MLOAD v15f8242c(0x40)
    0x24310x15f8: v15f82431(0x84) = SUB v15f82428, v15f8242e
    0x24330x15f8: REVERT v15f8242e, v15f82431(0x84)

    Begin block 0x23b80x15f8
    prev=[0x23dd0x15f8, 0x275d0x15f8], succ=[0x23bb0x15f8]
    =================================

    Begin block 0x23bb0x15f8
    prev=[0x23c90x15f8, 0x23b80x15f8], succ=[0x16c8, 0x37ad]
    =================================
    0x23bb0x15f8_0x3: v23bb15f8_3 = PHI v15f9(0x0), v1623(0x16c8), v1629(0x37ad), v161d_0
    0x23c00x15f8: JUMP v23bb15f8_3

    Begin block 0x16c8
    prev=[0x23bb0x15f8], succ=[0x16e3, 0x16f1]
    =================================
    0x16c8_0x0: v16c8_0 = PHI v15f8275e, v15f823d3, v15f823ca(0x0)
    0x16c8_0x2: v16c8_2 = PHI v15f9(0x0), v1623(0x16c8), v161d_0
    0x16c9: v16c9(0x0) = CONST 
    0x16cd: MSTORE v16c9(0x0), v16c8_2
    0x16ce: v16ce(0x10) = CONST 
    0x16d0: v16d0(0x20) = CONST 
    0x16d2: MSTORE v16d0(0x20), v16ce(0x10)
    0x16d3: v16d3(0x40) = CONST 
    0x16d6: v16d6 = SHA3 v16c9(0x0), v16d3(0x40)
    0x16d7: v16d7 = SLOAD v16d6
    0x16dd: v16dd = GT v16c8_0, v16d7
    0x16de: v16de = ISZERO v16dd
    0x16df: v16df(0x16f1) = CONST 
    0x16e2: JUMPI v16df(0x16f1), v16de

    Begin block 0x16e3
    prev=[0x16c8], succ=[0x2376B0x16e3]
    =================================
    0x16e3: v16e3(0x16ec) = CONST 
    0x16e3_0x1: v16e3_1 = PHI v15f8275e, v15f823d3, v15f823ca(0x0)
    0x16e8: v16e8(0x2376) = CONST 
    0x16eb: JUMP v16e8(0x2376)

    Begin block 0x2376B0x16e3
    prev=[0x16e3], succ=[0x23b80x2376B0x16e3]
    =================================
    0x2377S0x16e3: v2377V16e3(0x0) = CONST 
    0x2379S0x16e3: v2379V16e3(0x23b8) = CONST 
    0x237eS0x16e3: v237eV16e3(0x40) = CONST 
    0x2380S0x16e3: v2380V16e3 = MLOAD v237eV16e3(0x40)
    0x2382S0x16e3: v2382V16e3(0x40) = CONST 
    0x2384S0x16e3: v2384V16e3 = ADD v2382V16e3(0x40), v2380V16e3
    0x2385S0x16e3: v2385V16e3(0x40) = CONST 
    0x2387S0x16e3: MSTORE v2385V16e3(0x40), v2384V16e3
    0x2389S0x16e3: v2389V16e3(0x1e) = CONST 
    0x238cS0x16e3: MSTORE v2380V16e3, v2389V16e3(0x1e)
    0x238dS0x16e3: v238dV16e3(0x20) = CONST 
    0x238fS0x16e3: v238fV16e3 = ADD v238dV16e3(0x20), v2380V16e3
    0x2390S0x16e3: v2390V16e3(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x23b2S0x16e3: MSTORE v238fV16e3, v2390V16e3(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x23b4S0x16e3: v23b4V16e3(0x2632) = CONST 
    0x23b7S0x16e3: v23b7_0V16e3 = CALLPRIVATE v23b4V16e3(0x2632), v2380V16e3, v16d7, v16e3_1, v2379V16e3(0x23b8)

    Begin block 0x23b80x2376B0x16e3
    prev=[0x2376B0x16e3], succ=[0x23bb0x2376B0x16e3]
    =================================

    Begin block 0x23bb0x2376B0x16e3
    prev=[0x23b80x2376B0x16e3], succ=[0x16ec]
    =================================
    0x23c00x2376S0x16e3: JUMP v16e3(0x16ec)

    Begin block 0x16ec
    prev=[0x23bb0x2376B0x16e3], succ=[0x16f4]
    =================================
    0x16ed: v16ed(0x16f4) = CONST 
    0x16f0: JUMP v16ed(0x16f4)

    Begin block 0x16f4
    prev=[0x16f1, 0x16ec], succ=[]
    =================================
    0x16f4_0x0: v16f4_0 = PHI v16f2(0x0), v23b7_0V16e3
    0x16f4_0x6: v16f4_6 = PHI v1602_0, v15f8arg0
    0x16fc: RETURNPRIVATE v16f4_6, v16f4_0

    Begin block 0x16f1
    prev=[0x16c8], succ=[0x16f4]
    =================================
    0x16f2: v16f2(0x0) = CONST 

    Begin block 0x37ad
    prev=[0x23bb0x15f8], succ=[0x24340x15f8]
    =================================
    0x37af: v37af(0x2434) = CONST 
    0x37b2: JUMP v37af(0x2434)

    Begin block 0x24340x15f8
    prev=[0x37ad], succ=[0x26e80x15f8]
    =================================
    0x24350x15f8: v15f82435(0x0) = CONST 
    0x24370x15f8: v15f82437(0x23b8) = CONST 
    0x243c0x15f8: v15f8243c(0x40) = CONST 
    0x243e0x15f8: v15f8243e = MLOAD v15f8243c(0x40)
    0x24400x15f8: v15f82440(0x40) = CONST 
    0x24420x15f8: v15f82442 = ADD v15f82440(0x40), v15f8243e
    0x24430x15f8: v15f82443(0x40) = CONST 
    0x24450x15f8: MSTORE v15f82443(0x40), v15f82442
    0x24470x15f8: v15f82447(0x1a) = CONST 
    0x244a0x15f8: MSTORE v15f8243e, v15f82447(0x1a)
    0x244b0x15f8: v15f8244b(0x20) = CONST 
    0x244d0x15f8: v15f8244d = ADD v15f8244b(0x20), v15f8243e
    0x244e0x15f8: v15f8244e(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x24700x15f8: MSTORE v15f8244d, v15f8244e(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x24720x15f8: v15f82472(0x26e8) = CONST 
    0x24750x15f8: JUMP v15f82472(0x26e8)

    Begin block 0x26e80x15f8
    prev=[0x24340x15f8], succ=[0x26f10x15f8, 0x27510x15f8]
    =================================
    0x26e80x15f8_0x1: v26e815f8_1 = PHI v1621(0x0), v1626(0x2710), v1602_0, v15f8arg0
    0x26e90x15f8: v15f826e9(0x0) = CONST 
    0x26ed0x15f8: v15f826ed(0x2751) = CONST 
    0x26f00x15f8: JUMPI v15f826ed(0x2751), v26e815f8_1

    Begin block 0x26f10x15f8
    prev=[0x26e80x15f8], succ=[0x27420x15f8, 0x26a00x15f8]
    =================================
    0x26f10x15f8: v15f826f1(0x40) = CONST 
    0x26f30x15f8: v15f826f3 = MLOAD v15f826f1(0x40)
    0x26f40x15f8: v15f826f4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x27160x15f8: MSTORE v15f826f3, v15f826f4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x27170x15f8: v15f82717(0x20) = CONST 
    0x27190x15f8: v15f82719(0x4) = CONST 
    0x271c0x15f8: v15f8271c = ADD v15f826f3, v15f82719(0x4)
    0x271f0x15f8: MSTORE v15f8271c, v15f82717(0x20)
    0x27210x15f8: v15f82721(0x1a) = MLOAD v15f8243e
    0x27220x15f8: v15f82722(0x24) = CONST 
    0x27250x15f8: v15f82725 = ADD v15f826f3, v15f82722(0x24)
    0x27260x15f8: MSTORE v15f82725, v15f82721(0x1a)
    0x27280x15f8: v15f82728(0x1a) = MLOAD v15f8243e
    0x272d0x15f8: v15f8272d(0x44) = CONST 
    0x27310x15f8: v15f82731 = ADD v15f826f3, v15f8272d(0x44)
    0x27350x15f8: v15f82735 = ADD v15f8243e, v15f82717(0x20)
    0x273a0x15f8: v15f8273a(0x0) = CONST 
    0x273d0x15f8: v15f8273d = ISZERO v15f82728(0x1a)
    0x273e0x15f8: v15f8273e(0x26a0) = CONST 
    0x27410x15f8: JUMPI v15f8273e(0x26a0), v15f8273d

    Begin block 0x27420x15f8
    prev=[0x26f10x15f8], succ=[0x26880x15f8]
    =================================
    0x27440x15f8: v15f82744 = ADD v15f8273a(0x0), v15f82735
    0x27450x15f8: v15f82745 = MLOAD v15f82744
    0x27480x15f8: v15f82748 = ADD v15f8273a(0x0), v15f82731
    0x27490x15f8: MSTORE v15f82748, v15f82745
    0x274a0x15f8: v15f8274a(0x20) = CONST 
    0x274c0x15f8: v15f8274c(0x20) = ADD v15f8274a(0x20), v15f8273a(0x0)
    0x274d0x15f8: v15f8274d(0x2688) = CONST 
    0x27500x15f8: JUMP v15f8274d(0x2688)

    Begin block 0x26880x15f8
    prev=[0x27420x15f8, 0x26910x15f8], succ=[0x26a00x15f8, 0x26910x15f8]
    =================================
    0x26880x15f8_0x0: v268815f8_0 = PHI v15f8274c(0x20), v15f8269b
    0x268b0x15f8: v15f8268b = LT v268815f8_0, v15f82728(0x1a)
    0x268c0x15f8: v15f8268c = ISZERO v15f8268b
    0x268d0x15f8: v15f8268d(0x26a0) = CONST 
    0x26900x15f8: JUMPI v15f8268d(0x26a0), v15f8268c

    Begin block 0x26a00x15f8
    prev=[0x26f10x15f8, 0x26880x15f8], succ=[0x26cd0x15f8, 0x26b40x15f8]
    =================================
    0x26a90x15f8: v15f826a9 = ADD v15f82728(0x1a), v15f82731
    0x26ab0x15f8: v15f826ab(0x1f) = CONST 
    0x26ad0x15f8: v15f826ad(0x1a) = AND v15f826ab(0x1f), v15f82728(0x1a)
    0x26af0x15f8: v15f826af = ISZERO v15f826ad(0x1a)
    0x26b00x15f8: v15f826b0(0x26cd) = CONST 
    0x26b30x15f8: JUMPI v15f826b0(0x26cd), v15f826af

    Begin block 0x26cd0x15f8
    prev=[0x26a00x15f8, 0x26b40x15f8], succ=[]
    =================================
    0x26cd0x15f8_0x1: v26cd15f8_1 = PHI v15f826ca, v15f826a9
    0x26d30x15f8: v15f826d3(0x40) = CONST 
    0x26d50x15f8: v15f826d5 = MLOAD v15f826d3(0x40)
    0x26d80x15f8: v15f826d8 = SUB v26cd15f8_1, v15f826d5
    0x26da0x15f8: REVERT v15f826d5, v15f826d8

    Begin block 0x26b40x15f8
    prev=[0x26a00x15f8], succ=[0x26cd0x15f8]
    =================================
    0x26b60x15f8: v15f826b6 = SUB v15f826a9, v15f826ad(0x1a)
    0x26b80x15f8: v15f826b8 = MLOAD v15f826b6
    0x26b90x15f8: v15f826b9(0x1) = CONST 
    0x26bc0x15f8: v15f826bc(0x20) = CONST 
    0x26be0x15f8: v15f826be(0x6) = SUB v15f826bc(0x20), v15f826ad(0x1a)
    0x26bf0x15f8: v15f826bf(0x100) = CONST 
    0x26c20x15f8: v15f826c2(0x1000000000000) = EXP v15f826bf(0x100), v15f826be(0x6)
    0x26c30x15f8: v15f826c3(0xffffffffffff) = SUB v15f826c2(0x1000000000000), v15f826b9(0x1)
    0x26c40x15f8: v15f826c4 = NOT v15f826c3(0xffffffffffff)
    0x26c50x15f8: v15f826c5 = AND v15f826c4, v15f826b8
    0x26c70x15f8: MSTORE v15f826b6, v15f826c5
    0x26c80x15f8: v15f826c8(0x20) = CONST 
    0x26ca0x15f8: v15f826ca = ADD v15f826c8(0x20), v15f826b6

    Begin block 0x26910x15f8
    prev=[0x26880x15f8], succ=[0x26880x15f8]
    =================================
    0x26910x15f8_0x0: v269115f8_0 = PHI v15f8274c(0x20), v15f8269b
    0x26930x15f8: v15f82693 = ADD v269115f8_0, v15f82735
    0x26940x15f8: v15f82694 = MLOAD v15f82693
    0x26970x15f8: v15f82697 = ADD v269115f8_0, v15f82731
    0x26980x15f8: MSTORE v15f82697, v15f82694
    0x26990x15f8: v15f82699(0x20) = CONST 
    0x269b0x15f8: v15f8269b = ADD v15f82699(0x20), v269115f8_0
    0x269c0x15f8: v15f8269c(0x2688) = CONST 
    0x269f0x15f8: JUMP v15f8269c(0x2688)

    Begin block 0x27510x15f8
    prev=[0x26e80x15f8], succ=[0x275c0x15f8, 0x275d0x15f8]
    =================================
    0x27510x15f8_0x3: v275115f8_3 = PHI v1621(0x0), v1626(0x2710), v1602_0, v15f8arg0
    0x27530x15f8: v15f82753(0x0) = CONST 
    0x27580x15f8: v15f82758(0x275d) = CONST 
    0x275b0x15f8: JUMPI v15f82758(0x275d), v275115f8_3

    Begin block 0x275c0x15f8
    prev=[0x27510x15f8], succ=[]
    =================================
    0x275c0x15f8: THROW 

    Begin block 0x275d0x15f8
    prev=[0x27510x15f8], succ=[0x23b80x15f8]
    =================================
    0x275d0x15f8_0x0: v275d15f8_0 = PHI v15f8275e, v15f823d3, v15f823ca(0x0)
    0x275d0x15f8_0x1: v275d15f8_1 = PHI v1621(0x0), v1626(0x2710), v1602_0, v15f8arg0
    0x275e0x15f8: v15f8275e = DIV v275d15f8_0, v275d15f8_1
    0x27660x15f8: JUMP v15f82437(0x23b8)

    Begin block 0x23c90x15f8
    prev=[0x23c10x15f8], succ=[0x23bb0x15f8]
    =================================
    0x23ca0x15f8: v15f823ca(0x0) = CONST 
    0x23cc0x15f8: v15f823cc(0x23bb) = CONST 
    0x23cf0x15f8: JUMP v15f823cc(0x23bb)

    Begin block 0x378a
    prev=[0x1603], succ=[]
    =================================
    0x378d: RETURNPRIVATE v15f8arg0, v15f9(0x0)

}

function 0x1719(0x1719arg0x0) private {
    Begin block 0x1719
    prev=[], succ=[0x1780, 0x80a0x1719]
    =================================
    0x171a: v171a(0x3) = CONST 
    0x171c: v171c = SLOAD v171a(0x3)
    0x171d: v171d(0x40) = CONST 
    0x1720: v1720 = MLOAD v171d(0x40)
    0x1721: v1721(0x900cf0cf00000000000000000000000000000000000000000000000000000000) = CONST 
    0x1743: MSTORE v1720, v1721(0x900cf0cf00000000000000000000000000000000000000000000000000000000)
    0x1745: v1745 = MLOAD v171d(0x40)
    0x1746: v1746(0x0) = CONST 
    0x1749: v1749(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x175e: v175e = AND v1749(0xffffffffffffffffffffffffffffffffffffffff), v171c
    0x1760: v1760(0x900cf0cf) = CONST 
    0x1766: v1766(0x4) = CONST 
    0x176a: v176a = ADD v1720, v1766(0x4)
    0x176c: v176c(0x20) = CONST 
    0x1773: v1773(0x0) = SUB v1720, v1745
    0x1774: v1774(0x4) = ADD v1773(0x0), v1766(0x4)
    0x1778: v1778 = EXTCODESIZE v175e
    0x1779: v1779 = ISZERO v1778
    0x177b: v177b = ISZERO v1779
    0x177c: v177c(0x80a) = CONST 
    0x177f: JUMPI v177c(0x80a), v177b

    Begin block 0x1780
    prev=[0x1719], succ=[]
    =================================
    0x1780: v1780(0x0) = CONST 
    0x1783: REVERT v1780(0x0), v1780(0x0)

    Begin block 0x80a0x1719
    prev=[0x1719], succ=[0x8150x1719, 0x81e0x1719]
    =================================
    0x80c0x1719: v171980c = GAS 
    0x80d0x1719: v171980d = STATICCALL v171980c, v175e, v1745, v1774(0x4), v1745, v176c(0x20)
    0x80e0x1719: v171980e = ISZERO v171980d
    0x8100x1719: v1719810 = ISZERO v171980e
    0x8110x1719: v1719811(0x81e) = CONST 
    0x8140x1719: JUMPI v1719811(0x81e), v1719810

    Begin block 0x8150x1719
    prev=[0x80a0x1719], succ=[]
    =================================
    0x8150x1719: v1719815 = RETURNDATASIZE 
    0x8160x1719: v1719816(0x0) = CONST 
    0x8190x1719: RETURNDATACOPY v1719816(0x0), v1719816(0x0), v1719815
    0x81a0x1719: v171981a = RETURNDATASIZE 
    0x81b0x1719: v171981b(0x0) = CONST 
    0x81d0x1719: REVERT v171981b(0x0), v171981a

    Begin block 0x81e0x1719
    prev=[0x80a0x1719], succ=[0x8300x1719, 0x8340x1719]
    =================================
    0x8230x1719: v1719823(0x40) = CONST 
    0x8250x1719: v1719825 = MLOAD v1719823(0x40)
    0x8260x1719: v1719826 = RETURNDATASIZE 
    0x8270x1719: v1719827(0x20) = CONST 
    0x82a0x1719: v171982a = LT v1719826, v1719827(0x20)
    0x82b0x1719: v171982b = ISZERO v171982a
    0x82c0x1719: v171982c(0x834) = CONST 
    0x82f0x1719: JUMPI v171982c(0x834), v171982b

    Begin block 0x8300x1719
    prev=[0x81e0x1719], succ=[]
    =================================
    0x8300x1719: v1719830(0x0) = CONST 
    0x8330x1719: REVERT v1719830(0x0), v1719830(0x0)

    Begin block 0x8340x1719
    prev=[0x81e0x1719], succ=[0x8390x1719]
    =================================
    0x8360x1719: v1719836 = MLOAD v1719825

    Begin block 0x8390x1719
    prev=[0x8340x1719], succ=[]
    =================================
    0x83b0x1719: RETURNPRIVATE v1719arg0, v1719836

}

function 0x1805(0x1805arg0x0) private {
    Begin block 0x1805
    prev=[], succ=[0x1810]
    =================================
    0x1806: v1806(0x0) = CONST 
    0x1809: v1809(0x1810) = CONST 
    0x180c: v180c(0x2272) = CONST 
    0x180f: v180f_0 = CALLPRIVATE v180c(0x2272), v1809(0x1810)

    Begin block 0x1810
    prev=[0x1805], succ=[0x1823, 0x37d2]
    =================================
    0x1813: v1813(0xde0b6b3a7640000) = CONST 
    0x181d: v181d = LT v180f_0, v1813(0xde0b6b3a7640000)
    0x181e: v181e = ISZERO v181d
    0x181f: v181f(0x37d2) = CONST 
    0x1822: JUMPI v181f(0x37d2), v181e

    Begin block 0x1823
    prev=[0x1810], succ=[0x182d]
    =================================
    0x1823: v1823(0x1842) = CONST 
    0x1826: v1826(0x182d) = CONST 
    0x1829: v1829(0x21c3) = CONST 
    0x182c: v182c_0 = CALLPRIVATE v1829(0x21c3), v1826(0x182d)

    Begin block 0x182d
    prev=[0x1823], succ=[0x37f5]
    =================================
    0x182e: v182e(0x6) = CONST 
    0x1830: v1830 = SLOAD v182e(0x6)
    0x1831: v1831(0x37f5) = CONST 
    0x1835: v1835(0xde0b6b3a7640000) = CONST 
    0x183e: v183e(0x23c1) = CONST 
    0x1841: v1841_0 = CALLPRIVATE v183e(0x23c1), v1835(0xde0b6b3a7640000), v1830, v1831(0x37f5)

    Begin block 0x37f5
    prev=[0x182d], succ=[0x18420x1805]
    =================================
    0x37f7: v37f7(0x2434) = CONST 
    0x37fa: v37fa_0 = CALLPRIVATE v37f7(0x2434), v182c_0, v1841_0, v1823(0x1842)

    Begin block 0x18420x1805
    prev=[0x37f5], succ=[]
    =================================
    0x18470x1805: RETURNPRIVATE v1805arg0, v37fa_0

    Begin block 0x37d2
    prev=[0x1810], succ=[]
    =================================
    0x37d5: RETURNPRIVATE v1805arg0, v1806(0x0)

}

function 0x20b2(0x20b2arg0x0) private {
    Begin block 0x20b2
    prev=[], succ=[0x2138, 0x213c]
    =================================
    0x20b3: v20b3(0x4) = CONST 
    0x20b6: v20b6 = SLOAD v20b3(0x4)
    0x20b7: v20b7(0x5) = CONST 
    0x20b9: v20b9 = SLOAD v20b7(0x5)
    0x20ba: v20ba(0x40) = CONST 
    0x20bd: v20bd = MLOAD v20ba(0x40)
    0x20be: v20be(0xba54d3ec00000000000000000000000000000000000000000000000000000000) = CONST 
    0x20e0: MSTORE v20bd, v20be(0xba54d3ec00000000000000000000000000000000000000000000000000000000)
    0x20e1: v20e1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20f8: v20f8 = AND v20e1(0xffffffffffffffffffffffffffffffffffffffff), v20b9
    0x20fb: v20fb = ADD v20bd, v20b3(0x4)
    0x20ff: MSTORE v20fb, v20f8
    0x2100: v2100(0xde0b6b3a7640000) = CONST 
    0x2109: v2109(0x24) = CONST 
    0x210c: v210c = ADD v20bd, v2109(0x24)
    0x210d: MSTORE v210c, v2100(0xde0b6b3a7640000)
    0x210e: v210e = MLOAD v20ba(0x40)
    0x210f: v210f(0x0) = CONST 
    0x2115: v2115 = AND v20b6, v20e1(0xffffffffffffffffffffffffffffffffffffffff)
    0x2117: v2117(0xba54d3ec) = CONST 
    0x211d: v211d(0x44) = CONST 
    0x2121: v2121 = ADD v20bd, v211d(0x44)
    0x2123: v2123(0x20) = CONST 
    0x212b: v212b(0x0) = SUB v20bd, v210e
    0x212c: v212c(0x44) = ADD v212b(0x0), v211d(0x44)
    0x2130: v2130 = EXTCODESIZE v2115
    0x2131: v2131 = ISZERO v2130
    0x2133: v2133 = ISZERO v2131
    0x2134: v2134(0x213c) = CONST 
    0x2137: JUMPI v2134(0x213c), v2133

    Begin block 0x2138
    prev=[0x20b2], succ=[]
    =================================
    0x2138: v2138(0x0) = CONST 
    0x213b: REVERT v2138(0x0), v2138(0x0)

    Begin block 0x213c
    prev=[0x20b2], succ=[0x2161, 0x214a]
    =================================
    0x213e: v213e = GAS 
    0x213f: v213f = STATICCALL v213e, v2115, v210e, v212c(0x44), v210e, v2123(0x20)
    0x2145: v2145 = ISZERO v213f
    0x2146: v2146(0x2161) = CONST 
    0x2149: JUMPI v2146(0x2161), v2145

    Begin block 0x2161
    prev=[0x213c, 0x215c], succ=[0x2166, 0x21b60x20b2]
    =================================
    0x2161_0x0: v2161_0 = PHI v213f, v215f(0x1)
    0x2162: v2162(0x21b6) = CONST 
    0x2165: JUMPI v2162(0x21b6), v2161_0

    Begin block 0x2166
    prev=[0x2161], succ=[]
    =================================
    0x2166: v2166(0x40) = CONST 
    0x2168: v2168 = MLOAD v2166(0x40)
    0x2169: v2169(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x218b: MSTORE v2168, v2169(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x218c: v218c(0x4) = CONST 
    0x218e: v218e = ADD v218c(0x4), v2168
    0x2191: v2191(0x20) = CONST 
    0x2193: v2193 = ADD v2191(0x20), v218e
    0x2196: v2196(0x20) = SUB v2193, v218e
    0x2198: MSTORE v218e, v2196(0x20)
    0x2199: v2199(0x3d) = CONST 
    0x219c: MSTORE v2193, v2199(0x3d)
    0x219d: v219d(0x20) = CONST 
    0x219f: v219f = ADD v219d(0x20), v2193
    0x21a1: v21a1(0x2c96) = CONST 
    0x21a4: v21a4(0x3d) = CONST 
    0x21a7: CODECOPY v219f, v21a1(0x2c96), v21a4(0x3d)
    0x21a8: v21a8(0x40) = CONST 
    0x21aa: v21aa = ADD v21a8(0x40), v219f
    0x21ae: v21ae(0x40) = CONST 
    0x21b0: v21b0 = MLOAD v21ae(0x40)
    0x21b3: v21b3(0x84) = SUB v21aa, v21b0
    0x21b5: REVERT v21b0, v21b3(0x84)

    Begin block 0x21b60x20b2
    prev=[0x2161], succ=[0x8390x20b2]
    =================================
    0x21b90x20b2: v20b221b9(0x839) = CONST 
    0x21bc0x20b2: JUMP v20b221b9(0x839)

    Begin block 0x8390x20b2
    prev=[0x21b60x20b2], succ=[]
    =================================
    0x8390x20b2_0x0: v83920b2_0 = PHI v210f(0x0), v215e
    0x83b0x20b2: RETURNPRIVATE v20b2arg0, v83920b2_0

    Begin block 0x214a
    prev=[0x213c], succ=[0x2158, 0x215c]
    =================================
    0x214b: v214b(0x40) = CONST 
    0x214d: v214d = MLOAD v214b(0x40)
    0x214e: v214e = RETURNDATASIZE 
    0x214f: v214f(0x20) = CONST 
    0x2152: v2152 = LT v214e, v214f(0x20)
    0x2153: v2153 = ISZERO v2152
    0x2154: v2154(0x215c) = CONST 
    0x2157: JUMPI v2154(0x215c), v2153

    Begin block 0x2158
    prev=[0x214a], succ=[]
    =================================
    0x2158: v2158(0x0) = CONST 
    0x215b: REVERT v2158(0x0), v2158(0x0)

    Begin block 0x215c
    prev=[0x214a], succ=[0x2161]
    =================================
    0x215e: v215e = MLOAD v214d
    0x215f: v215f(0x1) = CONST 

}

function 0x21c3(0x21c3arg0x0) private {
    Begin block 0x21c3
    prev=[], succ=[0x21ce]
    =================================
    0x21c4: v21c4(0x0) = CONST 
    0x21c7: v21c7(0x21ce) = CONST 
    0x21ca: v21ca(0x20b2) = CONST 
    0x21cd: v21cd_0 = CALLPRIVATE v21ca(0x20b2), v21c7(0x21ce)

    Begin block 0x21ce
    prev=[0x21c3], succ=[0x21e1, 0x383f]
    =================================
    0x21d1: v21d1(0xde0b6b3a7640000) = CONST 
    0x21db: v21db = LT v21cd_0, v21d1(0xde0b6b3a7640000)
    0x21dc: v21dc = ISZERO v21db
    0x21dd: v21dd(0x383f) = CONST 
    0x21e0: JUMPI v21dd(0x383f), v21dc

    Begin block 0x21e1
    prev=[0x21ce], succ=[0x21e8, 0x21f7]
    =================================
    0x21e1: v21e1(0x9) = CONST 
    0x21e3: v21e3 = SLOAD v21e1(0x9)
    0x21e4: v21e4(0x21f7) = CONST 
    0x21e7: JUMPI v21e4(0x21f7), v21e3

    Begin block 0x21e8
    prev=[0x21e1], succ=[0x3862]
    =================================
    0x21e8: v21e8(0xde0b6b3a7640000) = CONST 
    0x21f3: v21f3(0x3862) = CONST 
    0x21f6: JUMP v21f3(0x3862)

    Begin block 0x3862
    prev=[0x21e8], succ=[]
    =================================
    0x3865: RETURNPRIVATE v21c3arg0, v21e8(0xde0b6b3a7640000)

    Begin block 0x21f7
    prev=[0x21e1], succ=[0x3885]
    =================================
    0x21f8: v21f8(0x0) = CONST 
    0x21fa: v21fa(0x220f) = CONST 
    0x21fe: v21fe(0x3885) = CONST 
    0x2201: v2201(0xde0b6b3a7640000) = CONST 
    0x220b: v220b(0x23c1) = CONST 
    0x220e: v220e_0 = CALLPRIVATE v220b(0x23c1), v2201(0xde0b6b3a7640000), v2201(0xde0b6b3a7640000), v21fe(0x3885)

    Begin block 0x3885
    prev=[0x21f7], succ=[0x220f]
    =================================
    0x3887: v3887(0x2434) = CONST 
    0x388a: v388a_0 = CALLPRIVATE v3887(0x2434), v21cd_0, v220e_0, v21fa(0x220f)

    Begin block 0x220f
    prev=[0x3885], succ=[0x2376B0x220f]
    =================================
    0x2212: v2212(0x0) = CONST 
    0x2214: v2214(0x223a) = CONST 
    0x2217: v2217(0x2710) = CONST 
    0x221a: v221a(0x38aa) = CONST 
    0x221d: v221d(0x9) = CONST 
    0x221f: v221f = SLOAD v221d(0x9)
    0x2220: v2220(0x38cf) = CONST 
    0x2223: v2223(0xde0b6b3a7640000) = CONST 
    0x222d: v222d(0x2376) = CONST 
    0x2233: v2233(0xffffffff) = CONST 
    0x2238: v2238(0x2376) = AND v2233(0xffffffff), v222d(0x2376)
    0x2239: JUMP v2238(0x2376)

    Begin block 0x2376B0x220f
    prev=[0x220f], succ=[0x23b80x2376B0x220f]
    =================================
    0x2377S0x220f: v2377V220f(0x0) = CONST 
    0x2379S0x220f: v2379V220f(0x23b8) = CONST 
    0x237eS0x220f: v237eV220f(0x40) = CONST 
    0x2380S0x220f: v2380V220f = MLOAD v237eV220f(0x40)
    0x2382S0x220f: v2382V220f(0x40) = CONST 
    0x2384S0x220f: v2384V220f = ADD v2382V220f(0x40), v2380V220f
    0x2385S0x220f: v2385V220f(0x40) = CONST 
    0x2387S0x220f: MSTORE v2385V220f(0x40), v2384V220f
    0x2389S0x220f: v2389V220f(0x1e) = CONST 
    0x238cS0x220f: MSTORE v2380V220f, v2389V220f(0x1e)
    0x238dS0x220f: v238dV220f(0x20) = CONST 
    0x238fS0x220f: v238fV220f = ADD v238dV220f(0x20), v2380V220f
    0x2390S0x220f: v2390V220f(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x23b2S0x220f: MSTORE v238fV220f, v2390V220f(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x23b4S0x220f: v23b4V220f(0x2632) = CONST 
    0x23b7S0x220f: v23b7_0V220f = CALLPRIVATE v23b4V220f(0x2632), v2380V220f, v2223(0xde0b6b3a7640000), v388a_0, v2379V220f(0x23b8)

    Begin block 0x23b80x2376B0x220f
    prev=[0x2376B0x220f], succ=[0x23bb0x2376B0x220f]
    =================================

    Begin block 0x23bb0x2376B0x220f
    prev=[0x23b80x2376B0x220f], succ=[0x38cf]
    =================================
    0x23c00x2376S0x220f: JUMP v2220(0x38cf)

    Begin block 0x38cf
    prev=[0x23bb0x2376B0x220f], succ=[0x38aa]
    =================================
    0x38d1: v38d1(0x23c1) = CONST 
    0x38d4: v38d4_0 = CALLPRIVATE v38d1(0x23c1), v221f, v23b7_0V220f, v221a(0x38aa)

    Begin block 0x38aa
    prev=[0x38cf], succ=[0x223a]
    =================================
    0x38ac: v38ac(0x2434) = CONST 
    0x38af: v38af_0 = CALLPRIVATE v38ac(0x2434), v2217(0x2710), v38d4_0, v2214(0x223a)

    Begin block 0x223a
    prev=[0x38aa], succ=[0x224e]
    =================================
    0x223d: v223d(0x224e) = CONST 
    0x2240: v2240(0xde0b6b3a7640000) = CONST 
    0x224a: v224a(0x2476) = CONST 
    0x224d: v224d_0 = CALLPRIVATE v224a(0x2476), v38af_0, v2240(0xde0b6b3a7640000), v223d(0x224e)

    Begin block 0x224e
    prev=[0x223a], succ=[0x2262, 0x225e]
    =================================
    0x224f: v224f(0xa) = CONST 
    0x2251: v2251 = SLOAD v224f(0xa)
    0x2256: v2256 = ISZERO v2251
    0x2258: v2258 = ISZERO v2256
    0x225a: v225a(0x2262) = CONST 
    0x225d: JUMPI v225a(0x2262), v2256

    Begin block 0x2262
    prev=[0x224e, 0x225e], succ=[0x226b, 0x2268]
    =================================
    0x2262_0x0: v2262_0 = PHI v2258, v2261
    0x2263: v2263 = ISZERO v2262_0
    0x2264: v2264(0x226b) = CONST 
    0x2267: JUMPI v2264(0x226b), v2263

    Begin block 0x226b
    prev=[0x2262, 0x2268], succ=[]
    =================================
    0x226b_0x4: v226b_4 = PHI v2251, v224d_0
    0x2271: RETURNPRIVATE v21c3arg0, v226b_4

    Begin block 0x2268
    prev=[0x2262], succ=[0x226b]
    =================================

    Begin block 0x225e
    prev=[0x224e], succ=[0x2262]
    =================================
    0x2261: v2261 = GT v224d_0, v2251

    Begin block 0x383f
    prev=[0x21ce], succ=[]
    =================================
    0x3842: RETURNPRIVATE v21c3arg0, v21c4(0x0)

}

function 0x2272(0x2272arg0x0) private {
    Begin block 0x2272
    prev=[], succ=[0x22f8, 0x22fc]
    =================================
    0x2273: v2273(0x4) = CONST 
    0x2276: v2276 = SLOAD v2273(0x4)
    0x2277: v2277(0x5) = CONST 
    0x2279: v2279 = SLOAD v2277(0x5)
    0x227a: v227a(0x40) = CONST 
    0x227d: v227d = MLOAD v227a(0x40)
    0x227e: v227e(0x6bfb05f900000000000000000000000000000000000000000000000000000000) = CONST 
    0x22a0: MSTORE v227d, v227e(0x6bfb05f900000000000000000000000000000000000000000000000000000000)
    0x22a1: v22a1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x22b8: v22b8 = AND v22a1(0xffffffffffffffffffffffffffffffffffffffff), v2279
    0x22bb: v22bb = ADD v227d, v2273(0x4)
    0x22bf: MSTORE v22bb, v22b8
    0x22c0: v22c0(0xde0b6b3a7640000) = CONST 
    0x22c9: v22c9(0x24) = CONST 
    0x22cc: v22cc = ADD v227d, v22c9(0x24)
    0x22cd: MSTORE v22cc, v22c0(0xde0b6b3a7640000)
    0x22ce: v22ce = MLOAD v227a(0x40)
    0x22cf: v22cf(0x0) = CONST 
    0x22d5: v22d5 = AND v2276, v22a1(0xffffffffffffffffffffffffffffffffffffffff)
    0x22d7: v22d7(0x6bfb05f9) = CONST 
    0x22dd: v22dd(0x44) = CONST 
    0x22e1: v22e1 = ADD v227d, v22dd(0x44)
    0x22e3: v22e3(0x20) = CONST 
    0x22eb: v22eb(0x0) = SUB v227d, v22ce
    0x22ec: v22ec(0x44) = ADD v22eb(0x0), v22dd(0x44)
    0x22f0: v22f0 = EXTCODESIZE v22d5
    0x22f1: v22f1 = ISZERO v22f0
    0x22f3: v22f3 = ISZERO v22f1
    0x22f4: v22f4(0x22fc) = CONST 
    0x22f7: JUMPI v22f4(0x22fc), v22f3

    Begin block 0x22f8
    prev=[0x2272], succ=[]
    =================================
    0x22f8: v22f8(0x0) = CONST 
    0x22fb: REVERT v22f8(0x0), v22f8(0x0)

    Begin block 0x22fc
    prev=[0x2272], succ=[0x2321, 0x230a]
    =================================
    0x22fe: v22fe = GAS 
    0x22ff: v22ff = STATICCALL v22fe, v22d5, v22ce, v22ec(0x44), v22ce, v22e3(0x20)
    0x2305: v2305 = ISZERO v22ff
    0x2306: v2306(0x2321) = CONST 
    0x2309: JUMPI v2306(0x2321), v2305

    Begin block 0x2321
    prev=[0x22fc, 0x231c], succ=[0x2326, 0x21b60x2272]
    =================================
    0x2321_0x0: v2321_0 = PHI v22ff, v231f(0x1)
    0x2322: v2322(0x21b6) = CONST 
    0x2325: JUMPI v2322(0x21b6), v2321_0

    Begin block 0x2326
    prev=[0x2321], succ=[]
    =================================
    0x2326: v2326(0x40) = CONST 
    0x2328: v2328 = MLOAD v2326(0x40)
    0x2329: v2329(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x234b: MSTORE v2328, v2329(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x234c: v234c(0x4) = CONST 
    0x234e: v234e = ADD v234c(0x4), v2328
    0x2351: v2351(0x20) = CONST 
    0x2353: v2353 = ADD v2351(0x20), v234e
    0x2356: v2356(0x20) = SUB v2353, v234e
    0x2358: MSTORE v234e, v2356(0x20)
    0x2359: v2359(0x3c) = CONST 
    0x235c: MSTORE v2353, v2359(0x3c)
    0x235d: v235d(0x20) = CONST 
    0x235f: v235f = ADD v235d(0x20), v2353
    0x2361: v2361(0x2aca) = CONST 
    0x2364: v2364(0x3c) = CONST 
    0x2367: CODECOPY v235f, v2361(0x2aca), v2364(0x3c)
    0x2368: v2368(0x40) = CONST 
    0x236a: v236a = ADD v2368(0x40), v235f
    0x236e: v236e(0x40) = CONST 
    0x2370: v2370 = MLOAD v236e(0x40)
    0x2373: v2373(0x84) = SUB v236a, v2370
    0x2375: REVERT v2370, v2373(0x84)

    Begin block 0x21b60x2272
    prev=[0x2321], succ=[0x8390x2272]
    =================================
    0x21b90x2272: v227221b9(0x839) = CONST 
    0x21bc0x2272: JUMP v227221b9(0x839)

    Begin block 0x8390x2272
    prev=[0x21b60x2272], succ=[]
    =================================
    0x8390x2272_0x0: v8392272_0 = PHI v22cf(0x0), v231e
    0x83b0x2272: RETURNPRIVATE v2272arg0, v8392272_0

    Begin block 0x230a
    prev=[0x22fc], succ=[0x2318, 0x231c]
    =================================
    0x230b: v230b(0x40) = CONST 
    0x230d: v230d = MLOAD v230b(0x40)
    0x230e: v230e = RETURNDATASIZE 
    0x230f: v230f(0x20) = CONST 
    0x2312: v2312 = LT v230e, v230f(0x20)
    0x2313: v2313 = ISZERO v2312
    0x2314: v2314(0x231c) = CONST 
    0x2317: JUMPI v2314(0x231c), v2313

    Begin block 0x2318
    prev=[0x230a], succ=[]
    =================================
    0x2318: v2318(0x0) = CONST 
    0x231b: REVERT v2318(0x0), v2318(0x0)

    Begin block 0x231c
    prev=[0x230a], succ=[0x2321]
    =================================
    0x231e: v231e = MLOAD v230d
    0x231f: v231f(0x1) = CONST 

}

function 0x23c1(0x23c1arg0x0, 0x23c1arg0x1, 0x23c1arg0x2) private {
    Begin block 0x23c1
    prev=[], succ=[0x23d00x23c1, 0x23c90x23c1]
    =================================
    0x23c2: v23c2(0x0) = CONST 
    0x23c5: v23c5(0x23d0) = CONST 
    0x23c8: JUMPI v23c5(0x23d0), v23c1arg1

    Begin block 0x23d00x23c1
    prev=[0x23c1], succ=[0x23dc0x23c1, 0x23dd0x23c1]
    =================================
    0x23d30x23c1: v23c123d3 = MUL v23c1arg0, v23c1arg1
    0x23d80x23c1: v23c123d8(0x23dd) = CONST 
    0x23db0x23c1: JUMPI v23c123d8(0x23dd), v23c1arg1

    Begin block 0x23dc0x23c1
    prev=[0x23d00x23c1], succ=[]
    =================================
    0x23dc0x23c1: THROW 

    Begin block 0x23dd0x23c1
    prev=[0x23d00x23c1], succ=[0x23e40x23c1, 0x23b80x23c1]
    =================================
    0x23de0x23c1: v23c123de = DIV v23c123d3, v23c1arg1
    0x23df0x23c1: v23c123df = EQ v23c123de, v23c1arg0
    0x23e00x23c1: v23c123e0(0x23b8) = CONST 
    0x23e30x23c1: JUMPI v23c123e0(0x23b8), v23c123df

    Begin block 0x23e40x23c1
    prev=[0x23dd0x23c1], succ=[]
    =================================
    0x23e40x23c1: v23c123e4(0x40) = CONST 
    0x23e60x23c1: v23c123e6 = MLOAD v23c123e4(0x40)
    0x23e70x23c1: v23c123e7(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x24090x23c1: MSTORE v23c123e6, v23c123e7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x240a0x23c1: v23c1240a(0x4) = CONST 
    0x240c0x23c1: v23c1240c = ADD v23c1240a(0x4), v23c123e6
    0x240f0x23c1: v23c1240f(0x20) = CONST 
    0x24110x23c1: v23c12411 = ADD v23c1240f(0x20), v23c1240c
    0x24140x23c1: v23c12414(0x20) = SUB v23c12411, v23c1240c
    0x24160x23c1: MSTORE v23c1240c, v23c12414(0x20)
    0x24170x23c1: v23c12417(0x21) = CONST 
    0x241a0x23c1: MSTORE v23c12411, v23c12417(0x21)
    0x241b0x23c1: v23c1241b(0x20) = CONST 
    0x241d0x23c1: v23c1241d = ADD v23c1241b(0x20), v23c12411
    0x241f0x23c1: v23c1241f(0x2c75) = CONST 
    0x24220x23c1: v23c12422(0x21) = CONST 
    0x24250x23c1: CODECOPY v23c1241d, v23c1241f(0x2c75), v23c12422(0x21)
    0x24260x23c1: v23c12426(0x40) = CONST 
    0x24280x23c1: v23c12428 = ADD v23c12426(0x40), v23c1241d
    0x242c0x23c1: v23c1242c(0x40) = CONST 
    0x242e0x23c1: v23c1242e = MLOAD v23c1242c(0x40)
    0x24310x23c1: v23c12431(0x84) = SUB v23c12428, v23c1242e
    0x24330x23c1: REVERT v23c1242e, v23c12431(0x84)

    Begin block 0x23b80x23c1
    prev=[0x23dd0x23c1], succ=[0x23bb0x23c1]
    =================================

    Begin block 0x23bb0x23c1
    prev=[0x23c90x23c1, 0x23b80x23c1], succ=[]
    =================================
    0x23bb0x23c1_0x0: v23bb23c1_0 = PHI v23c123d3, v23c123ca(0x0)
    0x23c00x23c1: RETURNPRIVATE v23c1arg2, v23bb23c1_0

    Begin block 0x23c90x23c1
    prev=[0x23c1], succ=[0x23bb0x23c1]
    =================================
    0x23ca0x23c1: v23c123ca(0x0) = CONST 
    0x23cc0x23c1: v23c123cc(0x23bb) = CONST 
    0x23cf0x23c1: JUMP v23c123cc(0x23bb)

}

function 0x2434(0x2434arg0x0, 0x2434arg0x1, 0x2434arg0x2) private {
    Begin block 0x2434
    prev=[], succ=[0x26e80x2434]
    =================================
    0x2435: v2435(0x0) = CONST 
    0x2437: v2437(0x23b8) = CONST 
    0x243c: v243c(0x40) = CONST 
    0x243e: v243e = MLOAD v243c(0x40)
    0x2440: v2440(0x40) = CONST 
    0x2442: v2442 = ADD v2440(0x40), v243e
    0x2443: v2443(0x40) = CONST 
    0x2445: MSTORE v2443(0x40), v2442
    0x2447: v2447(0x1a) = CONST 
    0x244a: MSTORE v243e, v2447(0x1a)
    0x244b: v244b(0x20) = CONST 
    0x244d: v244d = ADD v244b(0x20), v243e
    0x244e: v244e(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x2470: MSTORE v244d, v244e(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x2472: v2472(0x26e8) = CONST 
    0x2475: JUMP v2472(0x26e8)

    Begin block 0x26e80x2434
    prev=[0x2434], succ=[0x26f10x2434, 0x27510x2434]
    =================================
    0x26e90x2434: v243426e9(0x0) = CONST 
    0x26ed0x2434: v243426ed(0x2751) = CONST 
    0x26f00x2434: JUMPI v243426ed(0x2751), v2434arg0

    Begin block 0x26f10x2434
    prev=[0x26e80x2434], succ=[0x27420x2434, 0x26a00x2434]
    =================================
    0x26f10x2434: v243426f1(0x40) = CONST 
    0x26f30x2434: v243426f3 = MLOAD v243426f1(0x40)
    0x26f40x2434: v243426f4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x27160x2434: MSTORE v243426f3, v243426f4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x27170x2434: v24342717(0x20) = CONST 
    0x27190x2434: v24342719(0x4) = CONST 
    0x271c0x2434: v2434271c = ADD v243426f3, v24342719(0x4)
    0x271f0x2434: MSTORE v2434271c, v24342717(0x20)
    0x27210x2434: v24342721(0x1a) = MLOAD v243e
    0x27220x2434: v24342722(0x24) = CONST 
    0x27250x2434: v24342725 = ADD v243426f3, v24342722(0x24)
    0x27260x2434: MSTORE v24342725, v24342721(0x1a)
    0x27280x2434: v24342728(0x1a) = MLOAD v243e
    0x272d0x2434: v2434272d(0x44) = CONST 
    0x27310x2434: v24342731 = ADD v243426f3, v2434272d(0x44)
    0x27350x2434: v24342735 = ADD v243e, v24342717(0x20)
    0x273a0x2434: v2434273a(0x0) = CONST 
    0x273d0x2434: v2434273d = ISZERO v24342728(0x1a)
    0x273e0x2434: v2434273e(0x26a0) = CONST 
    0x27410x2434: JUMPI v2434273e(0x26a0), v2434273d

    Begin block 0x27420x2434
    prev=[0x26f10x2434], succ=[0x26880x2434]
    =================================
    0x27440x2434: v24342744 = ADD v2434273a(0x0), v24342735
    0x27450x2434: v24342745 = MLOAD v24342744
    0x27480x2434: v24342748 = ADD v2434273a(0x0), v24342731
    0x27490x2434: MSTORE v24342748, v24342745
    0x274a0x2434: v2434274a(0x20) = CONST 
    0x274c0x2434: v2434274c(0x20) = ADD v2434274a(0x20), v2434273a(0x0)
    0x274d0x2434: v2434274d(0x2688) = CONST 
    0x27500x2434: JUMP v2434274d(0x2688)

    Begin block 0x26880x2434
    prev=[0x27420x2434, 0x26910x2434], succ=[0x26a00x2434, 0x26910x2434]
    =================================
    0x26880x2434_0x0: v26882434_0 = PHI v2434274c(0x20), v2434269b
    0x268b0x2434: v2434268b = LT v26882434_0, v24342728(0x1a)
    0x268c0x2434: v2434268c = ISZERO v2434268b
    0x268d0x2434: v2434268d(0x26a0) = CONST 
    0x26900x2434: JUMPI v2434268d(0x26a0), v2434268c

    Begin block 0x26a00x2434
    prev=[0x26f10x2434, 0x26880x2434], succ=[0x26cd0x2434, 0x26b40x2434]
    =================================
    0x26a90x2434: v243426a9 = ADD v24342728(0x1a), v24342731
    0x26ab0x2434: v243426ab(0x1f) = CONST 
    0x26ad0x2434: v243426ad(0x1a) = AND v243426ab(0x1f), v24342728(0x1a)
    0x26af0x2434: v243426af = ISZERO v243426ad(0x1a)
    0x26b00x2434: v243426b0(0x26cd) = CONST 
    0x26b30x2434: JUMPI v243426b0(0x26cd), v243426af

    Begin block 0x26cd0x2434
    prev=[0x26a00x2434, 0x26b40x2434], succ=[]
    =================================
    0x26cd0x2434_0x1: v26cd2434_1 = PHI v243426ca, v243426a9
    0x26d30x2434: v243426d3(0x40) = CONST 
    0x26d50x2434: v243426d5 = MLOAD v243426d3(0x40)
    0x26d80x2434: v243426d8 = SUB v26cd2434_1, v243426d5
    0x26da0x2434: REVERT v243426d5, v243426d8

    Begin block 0x26b40x2434
    prev=[0x26a00x2434], succ=[0x26cd0x2434]
    =================================
    0x26b60x2434: v243426b6 = SUB v243426a9, v243426ad(0x1a)
    0x26b80x2434: v243426b8 = MLOAD v243426b6
    0x26b90x2434: v243426b9(0x1) = CONST 
    0x26bc0x2434: v243426bc(0x20) = CONST 
    0x26be0x2434: v243426be(0x6) = SUB v243426bc(0x20), v243426ad(0x1a)
    0x26bf0x2434: v243426bf(0x100) = CONST 
    0x26c20x2434: v243426c2(0x1000000000000) = EXP v243426bf(0x100), v243426be(0x6)
    0x26c30x2434: v243426c3(0xffffffffffff) = SUB v243426c2(0x1000000000000), v243426b9(0x1)
    0x26c40x2434: v243426c4 = NOT v243426c3(0xffffffffffff)
    0x26c50x2434: v243426c5 = AND v243426c4, v243426b8
    0x26c70x2434: MSTORE v243426b6, v243426c5
    0x26c80x2434: v243426c8(0x20) = CONST 
    0x26ca0x2434: v243426ca = ADD v243426c8(0x20), v243426b6

    Begin block 0x26910x2434
    prev=[0x26880x2434], succ=[0x26880x2434]
    =================================
    0x26910x2434_0x0: v26912434_0 = PHI v2434274c(0x20), v2434269b
    0x26930x2434: v24342693 = ADD v26912434_0, v24342735
    0x26940x2434: v24342694 = MLOAD v24342693
    0x26970x2434: v24342697 = ADD v26912434_0, v24342731
    0x26980x2434: MSTORE v24342697, v24342694
    0x26990x2434: v24342699(0x20) = CONST 
    0x269b0x2434: v2434269b = ADD v24342699(0x20), v26912434_0
    0x269c0x2434: v2434269c(0x2688) = CONST 
    0x269f0x2434: JUMP v2434269c(0x2688)

    Begin block 0x27510x2434
    prev=[0x26e80x2434], succ=[0x275c0x2434, 0x275d0x2434]
    =================================
    0x27530x2434: v24342753(0x0) = CONST 
    0x27580x2434: v24342758(0x275d) = CONST 
    0x275b0x2434: JUMPI v24342758(0x275d), v2434arg0

    Begin block 0x275c0x2434
    prev=[0x27510x2434], succ=[]
    =================================
    0x275c0x2434: THROW 

    Begin block 0x275d0x2434
    prev=[0x27510x2434], succ=[0x23b80x2434]
    =================================
    0x275e0x2434: v2434275e = DIV v2434arg1, v2434arg0
    0x27660x2434: JUMP v2437(0x23b8)

    Begin block 0x23b80x2434
    prev=[0x275d0x2434], succ=[0x23bb0x2434]
    =================================

    Begin block 0x23bb0x2434
    prev=[0x23b80x2434], succ=[]
    =================================
    0x23c00x2434: RETURNPRIVATE v2434arg2, v2434275e

}

function 0x2476(0x2476arg0x0, 0x2476arg0x1, 0x2476arg0x2) private {
    Begin block 0x2476
    prev=[], succ=[0x2484, 0x23b80x2476]
    =================================
    0x2477: v2477(0x0) = CONST 
    0x247b: v247b = ADD v2476arg0, v2476arg1
    0x247e: v247e = LT v247b, v2476arg1
    0x247f: v247f = ISZERO v247e
    0x2480: v2480(0x23b8) = CONST 
    0x2483: JUMPI v2480(0x23b8), v247f

    Begin block 0x2484
    prev=[0x2476], succ=[]
    =================================
    0x2484: v2484(0x40) = CONST 
    0x2487: v2487 = MLOAD v2484(0x40)
    0x2488: v2488(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x24aa: MSTORE v2487, v2488(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x24ab: v24ab(0x20) = CONST 
    0x24ad: v24ad(0x4) = CONST 
    0x24b0: v24b0 = ADD v2487, v24ad(0x4)
    0x24b1: MSTORE v24b0, v24ab(0x20)
    0x24b2: v24b2(0x1b) = CONST 
    0x24b4: v24b4(0x24) = CONST 
    0x24b7: v24b7 = ADD v2487, v24b4(0x24)
    0x24b8: MSTORE v24b7, v24b2(0x1b)
    0x24b9: v24b9(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x24da: v24da(0x44) = CONST 
    0x24dd: v24dd = ADD v2487, v24da(0x44)
    0x24de: MSTORE v24dd, v24b9(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x24e0: v24e0 = MLOAD v2484(0x40)
    0x24e4: v24e4(0x0) = SUB v2487, v24e0
    0x24e5: v24e5(0x64) = CONST 
    0x24e7: v24e7(0x64) = ADD v24e5(0x64), v24e4(0x0)
    0x24e9: REVERT v24e0, v24e7(0x64)

    Begin block 0x23b80x2476
    prev=[0x2476], succ=[0x23bb0x2476]
    =================================

    Begin block 0x23bb0x2476
    prev=[0x23b80x2476], succ=[]
    =================================
    0x23c00x2476: RETURNPRIVATE v2476arg2, v247b

}

function 0x25b5(0x25b5arg0x0) private {
    Begin block 0x25b5
    prev=[], succ=[0x261a, 0x261e]
    =================================
    0x25b6: v25b6(0x4) = CONST 
    0x25b9: v25b9 = SLOAD v25b6(0x4)
    0x25ba: v25ba(0x40) = CONST 
    0x25bd: v25bd = MLOAD v25ba(0x40)
    0x25be: v25be(0xda303d9d00000000000000000000000000000000000000000000000000000000) = CONST 
    0x25e0: MSTORE v25bd, v25be(0xda303d9d00000000000000000000000000000000000000000000000000000000)
    0x25e2: v25e2 = MLOAD v25ba(0x40)
    0x25e3: v25e3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25fa: v25fa = AND v25b9, v25e3(0xffffffffffffffffffffffffffffffffffffffff)
    0x25fc: v25fc(0xda303d9d) = CONST 
    0x2604: v2604 = ADD v25b6(0x4), v25bd
    0x2606: v2606(0x0) = CONST 
    0x260c: v260c(0x0) = SUB v25bd, v25e2
    0x260d: v260d(0x4) = ADD v260c(0x0), v25b6(0x4)
    0x2612: v2612 = EXTCODESIZE v25fa
    0x2613: v2613 = ISZERO v2612
    0x2615: v2615 = ISZERO v2613
    0x2616: v2616(0x261e) = CONST 
    0x2619: JUMPI v2616(0x261e), v2615

    Begin block 0x261a
    prev=[0x25b5], succ=[]
    =================================
    0x261a: v261a(0x0) = CONST 
    0x261d: REVERT v261a(0x0), v261a(0x0)

    Begin block 0x261e
    prev=[0x25b5], succ=[0x262f, 0x262c]
    =================================
    0x2620: v2620 = GAS 
    0x2621: v2621 = CALL v2620, v25fa, v2606(0x0), v25e2, v260d(0x4), v25e2, v2606(0x0)
    0x2627: v2627 = ISZERO v2621
    0x2628: v2628(0x262f) = CONST 
    0x262b: JUMPI v2628(0x262f), v2627

    Begin block 0x262f
    prev=[0x261e, 0x262c], succ=[]
    =================================
    0x2631: RETURNPRIVATE v25b5arg0

    Begin block 0x262c
    prev=[0x261e], succ=[0x262f]
    =================================
    0x262d: v262d(0x1) = CONST 

}

function 0x2632(0x2632arg0x0, 0x2632arg0x1, 0x2632arg0x2, 0x2632arg0x3) private {
    Begin block 0x2632
    prev=[], succ=[0x263e, 0x26db]
    =================================
    0x2633: v2633(0x0) = CONST 
    0x2638: v2638 = GT v2632arg1, v2632arg2
    0x2639: v2639 = ISZERO v2638
    0x263a: v263a(0x26db) = CONST 
    0x263d: JUMPI v263a(0x26db), v2639

    Begin block 0x263e
    prev=[0x2632], succ=[0x26880x2632]
    =================================
    0x263e: v263e(0x40) = CONST 
    0x2640: v2640 = MLOAD v263e(0x40)
    0x2641: v2641(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2663: MSTORE v2640, v2641(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2664: v2664(0x4) = CONST 
    0x2666: v2666 = ADD v2664(0x4), v2640
    0x2669: v2669(0x20) = CONST 
    0x266b: v266b = ADD v2669(0x20), v2666
    0x266e: v266e(0x20) = SUB v266b, v2666
    0x2670: MSTORE v2666, v266e(0x20)
    0x2674: v2674 = MLOAD v2632arg0
    0x2676: MSTORE v266b, v2674
    0x2677: v2677(0x20) = CONST 
    0x2679: v2679 = ADD v2677(0x20), v266b
    0x267d: v267d = MLOAD v2632arg0
    0x267f: v267f(0x20) = CONST 
    0x2681: v2681 = ADD v267f(0x20), v2632arg0
    0x2686: v2686(0x0) = CONST 

    Begin block 0x26880x2632
    prev=[0x263e, 0x26910x2632], succ=[0x26a00x2632, 0x26910x2632]
    =================================
    0x26880x2632_0x0: v26882632_0 = PHI v2686(0x0), v2632269b
    0x268b0x2632: v2632268b = LT v26882632_0, v267d
    0x268c0x2632: v2632268c = ISZERO v2632268b
    0x268d0x2632: v2632268d(0x26a0) = CONST 
    0x26900x2632: JUMPI v2632268d(0x26a0), v2632268c

    Begin block 0x26a00x2632
    prev=[0x26880x2632], succ=[0x26cd0x2632, 0x26b40x2632]
    =================================
    0x26a90x2632: v263226a9 = ADD v267d, v2679
    0x26ab0x2632: v263226ab(0x1f) = CONST 
    0x26ad0x2632: v263226ad = AND v263226ab(0x1f), v267d
    0x26af0x2632: v263226af = ISZERO v263226ad
    0x26b00x2632: v263226b0(0x26cd) = CONST 
    0x26b30x2632: JUMPI v263226b0(0x26cd), v263226af

    Begin block 0x26cd0x2632
    prev=[0x26a00x2632, 0x26b40x2632], succ=[]
    =================================
    0x26cd0x2632_0x1: v26cd2632_1 = PHI v263226ca, v263226a9
    0x26d30x2632: v263226d3(0x40) = CONST 
    0x26d50x2632: v263226d5 = MLOAD v263226d3(0x40)
    0x26d80x2632: v263226d8 = SUB v26cd2632_1, v263226d5
    0x26da0x2632: REVERT v263226d5, v263226d8

    Begin block 0x26b40x2632
    prev=[0x26a00x2632], succ=[0x26cd0x2632]
    =================================
    0x26b60x2632: v263226b6 = SUB v263226a9, v263226ad
    0x26b80x2632: v263226b8 = MLOAD v263226b6
    0x26b90x2632: v263226b9(0x1) = CONST 
    0x26bc0x2632: v263226bc(0x20) = CONST 
    0x26be0x2632: v263226be = SUB v263226bc(0x20), v263226ad
    0x26bf0x2632: v263226bf(0x100) = CONST 
    0x26c20x2632: v263226c2 = EXP v263226bf(0x100), v263226be
    0x26c30x2632: v263226c3 = SUB v263226c2, v263226b9(0x1)
    0x26c40x2632: v263226c4 = NOT v263226c3
    0x26c50x2632: v263226c5 = AND v263226c4, v263226b8
    0x26c70x2632: MSTORE v263226b6, v263226c5
    0x26c80x2632: v263226c8(0x20) = CONST 
    0x26ca0x2632: v263226ca = ADD v263226c8(0x20), v263226b6

    Begin block 0x26910x2632
    prev=[0x26880x2632], succ=[0x26880x2632]
    =================================
    0x26910x2632_0x0: v26912632_0 = PHI v2686(0x0), v2632269b
    0x26930x2632: v26322693 = ADD v26912632_0, v2681
    0x26940x2632: v26322694 = MLOAD v26322693
    0x26970x2632: v26322697 = ADD v26912632_0, v2679
    0x26980x2632: MSTORE v26322697, v26322694
    0x26990x2632: v26322699(0x20) = CONST 
    0x269b0x2632: v2632269b = ADD v26322699(0x20), v26912632_0
    0x269c0x2632: v2632269c(0x2688) = CONST 
    0x269f0x2632: JUMP v2632269c(0x2688)

    Begin block 0x26db
    prev=[0x2632], succ=[0x26e10x2632]
    =================================
    0x26e0: v26e0 = SUB v2632arg2, v2632arg1

    Begin block 0x26e10x2632
    prev=[0x26db], succ=[]
    =================================
    0x26e70x2632: RETURNPRIVATE v2632arg3, v26e0

}

function fallback()() public {
    Begin block 0x2d93
    prev=[], succ=[]
    =================================
    0x2d94: v2d94(0x0) = CONST 
    0x2d97: REVERT v2d94(0x0), v2d94(0x0)

}

function nextEpochLength()() public {
    Begin block 0x2f9
    prev=[], succ=[0x79fB0x2f9]
    =================================
    0x2fa: v2fa(0x2fd3) = CONST 
    0x2fd: v2fd(0x79f) = CONST 
    0x300: JUMP v2fd(0x79f)

    Begin block 0x79fB0x2f9
    prev=[0x2f9], succ=[0x806B0x2f9, 0x80a0x79fB0x2f9]
    =================================
    0x7a0S0x2f9: v7a0V2f9(0x3) = CONST 
    0x7a2S0x2f9: v7a2V2f9 = SLOAD v7a0V2f9(0x3)
    0x7a3S0x2f9: v7a3V2f9(0x40) = CONST 
    0x7a6S0x2f9: v7a6V2f9 = MLOAD v7a3V2f9(0x40)
    0x7a7S0x2f9: v7a7V2f9(0x7284ce900000000000000000000000000000000000000000000000000000000) = CONST 
    0x7c9S0x2f9: MSTORE v7a6V2f9, v7a7V2f9(0x7284ce900000000000000000000000000000000000000000000000000000000)
    0x7cbS0x2f9: v7cbV2f9 = MLOAD v7a3V2f9(0x40)
    0x7ccS0x2f9: v7ccV2f9(0x0) = CONST 
    0x7cfS0x2f9: v7cfV2f9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7e4S0x2f9: v7e4V2f9 = AND v7cfV2f9(0xffffffffffffffffffffffffffffffffffffffff), v7a2V2f9
    0x7e6S0x2f9: v7e6V2f9(0x7284ce9) = CONST 
    0x7ecS0x2f9: v7ecV2f9(0x4) = CONST 
    0x7f0S0x2f9: v7f0V2f9 = ADD v7a6V2f9, v7ecV2f9(0x4)
    0x7f2S0x2f9: v7f2V2f9(0x20) = CONST 
    0x7f9S0x2f9: v7f9V2f9(0x0) = SUB v7a6V2f9, v7cbV2f9
    0x7faS0x2f9: v7faV2f9(0x4) = ADD v7f9V2f9(0x0), v7ecV2f9(0x4)
    0x7feS0x2f9: v7feV2f9 = EXTCODESIZE v7e4V2f9
    0x7ffS0x2f9: v7ffV2f9 = ISZERO v7feV2f9
    0x801S0x2f9: v801V2f9 = ISZERO v7ffV2f9
    0x802S0x2f9: v802V2f9(0x80a) = CONST 
    0x805S0x2f9: JUMPI v802V2f9(0x80a), v801V2f9

    Begin block 0x806B0x2f9
    prev=[0x79fB0x2f9], succ=[]
    =================================
    0x806S0x2f9: v806V2f9(0x0) = CONST 
    0x809S0x2f9: REVERT v806V2f9(0x0), v806V2f9(0x0)

    Begin block 0x80a0x79fB0x2f9
    prev=[0x79fB0x2f9], succ=[0x8150x79fB0x2f9, 0x81e0x79fB0x2f9]
    =================================
    0x80c0x79fS0x2f9: v79f80cV2f9 = GAS 
    0x80d0x79fS0x2f9: v79f80dV2f9 = STATICCALL v79f80cV2f9, v7e4V2f9, v7cbV2f9, v7faV2f9(0x4), v7cbV2f9, v7f2V2f9(0x20)
    0x80e0x79fS0x2f9: v79f80eV2f9 = ISZERO v79f80dV2f9
    0x8100x79fS0x2f9: v79f810V2f9 = ISZERO v79f80eV2f9
    0x8110x79fS0x2f9: v79f811V2f9(0x81e) = CONST 
    0x8140x79fS0x2f9: JUMPI v79f811V2f9(0x81e), v79f810V2f9

    Begin block 0x8150x79fB0x2f9
    prev=[0x80a0x79fB0x2f9], succ=[]
    =================================
    0x8150x79fS0x2f9: v79f815V2f9 = RETURNDATASIZE 
    0x8160x79fS0x2f9: v79f816V2f9(0x0) = CONST 
    0x8190x79fS0x2f9: RETURNDATACOPY v79f816V2f9(0x0), v79f816V2f9(0x0), v79f815V2f9
    0x81a0x79fS0x2f9: v79f81aV2f9 = RETURNDATASIZE 
    0x81b0x79fS0x2f9: v79f81bV2f9(0x0) = CONST 
    0x81d0x79fS0x2f9: REVERT v79f81bV2f9(0x0), v79f81aV2f9

    Begin block 0x81e0x79fB0x2f9
    prev=[0x80a0x79fB0x2f9], succ=[0x8300x79fB0x2f9, 0x8340x79fB0x2f9]
    =================================
    0x8230x79fS0x2f9: v79f823V2f9(0x40) = CONST 
    0x8250x79fS0x2f9: v79f825V2f9 = MLOAD v79f823V2f9(0x40)
    0x8260x79fS0x2f9: v79f826V2f9 = RETURNDATASIZE 
    0x8270x79fS0x2f9: v79f827V2f9(0x20) = CONST 
    0x82a0x79fS0x2f9: v79f82aV2f9 = LT v79f826V2f9, v79f827V2f9(0x20)
    0x82b0x79fS0x2f9: v79f82bV2f9 = ISZERO v79f82aV2f9
    0x82c0x79fS0x2f9: v79f82cV2f9(0x834) = CONST 
    0x82f0x79fS0x2f9: JUMPI v79f82cV2f9(0x834), v79f82bV2f9

    Begin block 0x8300x79fB0x2f9
    prev=[0x81e0x79fB0x2f9], succ=[]
    =================================
    0x8300x79fS0x2f9: v79f830V2f9(0x0) = CONST 
    0x8330x79fS0x2f9: REVERT v79f830V2f9(0x0), v79f830V2f9(0x0)

    Begin block 0x8340x79fB0x2f9
    prev=[0x81e0x79fB0x2f9], succ=[0x8390x79fB0x2f9]
    =================================
    0x8360x79fS0x2f9: v79f836V2f9 = MLOAD v79f825V2f9

    Begin block 0x8390x79fB0x2f9
    prev=[0x8340x79fB0x2f9], succ=[0x2fd3]
    =================================
    0x83b0x79fS0x2f9: JUMP v2fa(0x2fd3)

    Begin block 0x2fd3
    prev=[0x8390x79fB0x2f9], succ=[]
    =================================
    0x2fd4: v2fd4(0x40) = CONST 
    0x2fd7: v2fd7 = MLOAD v2fd4(0x40)
    0x2fda: MSTORE v2fd7, v79f836V2f9
    0x2fdb: v2fdb = MLOAD v2fd4(0x40)
    0x2fdf: v2fdf(0x0) = SUB v2fd7, v2fdb
    0x2fe0: v2fe0(0x20) = CONST 
    0x2fe2: v2fe2(0x20) = ADD v2fe0(0x20), v2fdf(0x0)
    0x2fe4: RETURN v2fdb, v2fe2(0x20)

}

function setMaxRedeemableCouponPercentPerEpoch(uint256)() public {
    Begin block 0x313
    prev=[], succ=[0x325, 0x329]
    =================================
    0x314: v314(0x3004) = CONST 
    0x317: v317(0x4) = CONST 
    0x31a: v31a = CALLDATASIZE 
    0x31b: v31b = SUB v31a, v317(0x4)
    0x31c: v31c(0x20) = CONST 
    0x31f: v31f = LT v31b, v31c(0x20)
    0x320: v320 = ISZERO v31f
    0x321: v321(0x329) = CONST 
    0x324: JUMPI v321(0x329), v320

    Begin block 0x325
    prev=[0x313], succ=[]
    =================================
    0x325: v325(0x0) = CONST 
    0x328: REVERT v325(0x0), v325(0x0)

    Begin block 0x329
    prev=[0x313], succ=[0x83c]
    =================================
    0x32b: v32b = CALLDATALOAD v317(0x4)
    0x32c: v32c(0x83c) = CONST 
    0x32f: JUMP v32c(0x83c)

    Begin block 0x83c
    prev=[0x329], succ=[0x85c, 0x8ac]
    =================================
    0x83d: v83d(0x1) = CONST 
    0x83f: v83f = SLOAD v83d(0x1)
    0x840: v840(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x855: v855 = AND v840(0xffffffffffffffffffffffffffffffffffffffff), v83f
    0x856: v856 = CALLER 
    0x857: v857 = EQ v856, v855
    0x858: v858(0x8ac) = CONST 
    0x85b: JUMPI v858(0x8ac), v857

    Begin block 0x85c
    prev=[0x83c], succ=[]
    =================================
    0x85c: v85c(0x40) = CONST 
    0x85e: v85e = MLOAD v85c(0x40)
    0x85f: v85f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x881: MSTORE v85e, v85f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x882: v882(0x4) = CONST 
    0x884: v884 = ADD v882(0x4), v85e
    0x887: v887(0x20) = CONST 
    0x889: v889 = ADD v887(0x20), v884
    0x88c: v88c(0x20) = SUB v889, v884
    0x88e: MSTORE v884, v88c(0x20)
    0x88f: v88f(0x28) = CONST 
    0x892: MSTORE v889, v88f(0x28)
    0x893: v893(0x20) = CONST 
    0x895: v895 = ADD v893(0x20), v889
    0x897: v897(0x2b90) = CONST 
    0x89a: v89a(0x28) = CONST 
    0x89d: CODECOPY v895, v897(0x2b90), v89a(0x28)
    0x89e: v89e(0x40) = CONST 
    0x8a0: v8a0 = ADD v89e(0x40), v895
    0x8a4: v8a4(0x40) = CONST 
    0x8a6: v8a6 = MLOAD v8a4(0x40)
    0x8a9: v8a9(0x84) = SUB v8a0, v8a6
    0x8ab: REVERT v8a6, v8a9(0x84)

    Begin block 0x8ac
    prev=[0x83c], succ=[0x8b7, 0x907]
    =================================
    0x8ad: v8ad(0x2710) = CONST 
    0x8b1: v8b1 = GT v32b, v8ad(0x2710)
    0x8b2: v8b2 = ISZERO v8b1
    0x8b3: v8b3(0x907) = CONST 
    0x8b6: JUMPI v8b3(0x907), v8b2

    Begin block 0x8b7
    prev=[0x8ac], succ=[]
    =================================
    0x8b7: v8b7(0x40) = CONST 
    0x8b9: v8b9 = MLOAD v8b7(0x40)
    0x8ba: v8ba(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x8dc: MSTORE v8b9, v8ba(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8dd: v8dd(0x4) = CONST 
    0x8df: v8df = ADD v8dd(0x4), v8b9
    0x8e2: v8e2(0x20) = CONST 
    0x8e4: v8e4 = ADD v8e2(0x20), v8df
    0x8e7: v8e7(0x20) = SUB v8e4, v8df
    0x8e9: MSTORE v8df, v8e7(0x20)
    0x8ea: v8ea(0x30) = CONST 
    0x8ed: MSTORE v8e4, v8ea(0x30)
    0x8ee: v8ee(0x20) = CONST 
    0x8f0: v8f0 = ADD v8ee(0x20), v8e4
    0x8f2: v8f2(0x2b2c) = CONST 
    0x8f5: v8f5(0x30) = CONST 
    0x8f8: CODECOPY v8f0, v8f2(0x2b2c), v8f5(0x30)
    0x8f9: v8f9(0x40) = CONST 
    0x8fb: v8fb = ADD v8f9(0x40), v8f0
    0x8ff: v8ff(0x40) = CONST 
    0x901: v901 = MLOAD v8ff(0x40)
    0x904: v904(0x84) = SUB v8fb, v901
    0x906: REVERT v901, v904(0x84)

    Begin block 0x907
    prev=[0x8ac], succ=[0x3004]
    =================================
    0x908: v908(0xd) = CONST 
    0x90a: SSTORE v908(0xd), v32b
    0x90b: JUMP v314(0x3004)

    Begin block 0x3004
    prev=[0x907], succ=[]
    =================================
    0x3005: STOP 

}

function setDiscountPercent(uint256)() public {
    Begin block 0x332
    prev=[], succ=[0x344, 0x348]
    =================================
    0x333: v333(0x3025) = CONST 
    0x336: v336(0x4) = CONST 
    0x339: v339 = CALLDATASIZE 
    0x33a: v33a = SUB v339, v336(0x4)
    0x33b: v33b(0x20) = CONST 
    0x33e: v33e = LT v33a, v33b(0x20)
    0x33f: v33f = ISZERO v33e
    0x340: v340(0x348) = CONST 
    0x343: JUMPI v340(0x348), v33f

    Begin block 0x344
    prev=[0x332], succ=[]
    =================================
    0x344: v344(0x0) = CONST 
    0x347: REVERT v344(0x0), v344(0x0)

    Begin block 0x348
    prev=[0x332], succ=[0x90c]
    =================================
    0x34a: v34a = CALLDATALOAD v336(0x4)
    0x34b: v34b(0x90c) = CONST 
    0x34e: JUMP v34b(0x90c)

    Begin block 0x90c
    prev=[0x348], succ=[0x92c, 0x97c]
    =================================
    0x90d: v90d(0x1) = CONST 
    0x90f: v90f = SLOAD v90d(0x1)
    0x910: v910(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x925: v925 = AND v910(0xffffffffffffffffffffffffffffffffffffffff), v90f
    0x926: v926 = CALLER 
    0x927: v927 = EQ v926, v925
    0x928: v928(0x97c) = CONST 
    0x92b: JUMPI v928(0x97c), v927

    Begin block 0x92c
    prev=[0x90c], succ=[]
    =================================
    0x92c: v92c(0x40) = CONST 
    0x92e: v92e = MLOAD v92c(0x40)
    0x92f: v92f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x951: MSTORE v92e, v92f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x952: v952(0x4) = CONST 
    0x954: v954 = ADD v952(0x4), v92e
    0x957: v957(0x20) = CONST 
    0x959: v959 = ADD v957(0x20), v954
    0x95c: v95c(0x20) = SUB v959, v954
    0x95e: MSTORE v954, v95c(0x20)
    0x95f: v95f(0x28) = CONST 
    0x962: MSTORE v959, v95f(0x28)
    0x963: v963(0x20) = CONST 
    0x965: v965 = ADD v963(0x20), v959
    0x967: v967(0x2b90) = CONST 
    0x96a: v96a(0x28) = CONST 
    0x96d: CODECOPY v965, v967(0x2b90), v96a(0x28)
    0x96e: v96e(0x40) = CONST 
    0x970: v970 = ADD v96e(0x40), v965
    0x974: v974(0x40) = CONST 
    0x976: v976 = MLOAD v974(0x40)
    0x979: v979(0x84) = SUB v970, v976
    0x97b: REVERT v976, v979(0x84)

    Begin block 0x97c
    prev=[0x90c], succ=[0x987, 0x9ed]
    =================================
    0x97d: v97d(0x4e20) = CONST 
    0x981: v981 = GT v34a, v97d(0x4e20)
    0x982: v982 = ISZERO v981
    0x983: v983(0x9ed) = CONST 
    0x986: JUMPI v983(0x9ed), v982

    Begin block 0x987
    prev=[0x97c], succ=[]
    =================================
    0x987: v987(0x40) = CONST 
    0x98a: v98a = MLOAD v987(0x40)
    0x98b: v98b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9ad: MSTORE v98a, v98b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9ae: v9ae(0x20) = CONST 
    0x9b0: v9b0(0x4) = CONST 
    0x9b3: v9b3 = ADD v98a, v9b0(0x4)
    0x9b4: MSTORE v9b3, v9ae(0x20)
    0x9b5: v9b5(0x1d) = CONST 
    0x9b7: v9b7(0x24) = CONST 
    0x9ba: v9ba = ADD v98a, v9b7(0x24)
    0x9bb: MSTORE v9ba, v9b5(0x1d)
    0x9bc: v9bc(0x5f646973636f756e7450657263656e74206973206f7665722032303025000000) = CONST 
    0x9dd: v9dd(0x44) = CONST 
    0x9e0: v9e0 = ADD v98a, v9dd(0x44)
    0x9e1: MSTORE v9e0, v9bc(0x5f646973636f756e7450657263656e74206973206f7665722032303025000000)
    0x9e3: v9e3 = MLOAD v987(0x40)
    0x9e7: v9e7(0x0) = SUB v98a, v9e3
    0x9e8: v9e8(0x64) = CONST 
    0x9ea: v9ea(0x64) = ADD v9e8(0x64), v9e7(0x0)
    0x9ec: REVERT v9e3, v9ea(0x64)

    Begin block 0x9ed
    prev=[0x97c], succ=[0x3025]
    =================================
    0x9ee: v9ee(0x9) = CONST 
    0x9f0: SSTORE v9ee(0x9), v34a
    0x9f1: JUMP v333(0x3025)

    Begin block 0x3025
    prev=[0x9ed], succ=[]
    =================================
    0x3026: STOP 

}

function initialized()() public {
    Begin block 0x34f
    prev=[], succ=[0x9f2]
    =================================
    0x350: v350(0x3046) = CONST 
    0x353: v353(0x9f2) = CONST 
    0x356: JUMP v353(0x9f2)

    Begin block 0x9f2
    prev=[0x34f], succ=[0x3046]
    =================================
    0x9f3: v9f3(0x1) = CONST 
    0x9f5: v9f5 = SLOAD v9f3(0x1)
    0x9f6: v9f6(0x10000000000000000000000000000000000000000) = CONST 
    0xa0d: va0d = DIV v9f5, v9f6(0x10000000000000000000000000000000000000000)
    0xa0e: va0e(0xff) = CONST 
    0xa10: va10 = AND va0e(0xff), va0d
    0xa12: JUMP v350(0x3046)

    Begin block 0x3046
    prev=[0x9f2], succ=[]
    =================================
    0x3047: v3047(0x40) = CONST 
    0x304a: v304a = MLOAD v3047(0x40)
    0x304c: v304c = ISZERO va10
    0x304d: v304d = ISZERO v304c
    0x304f: MSTORE v304a, v304d
    0x3050: v3050 = MLOAD v3047(0x40)
    0x3054: v3054(0x0) = SUB v304a, v3050
    0x3055: v3055(0x20) = CONST 
    0x3057: v3057(0x20) = ADD v3055(0x20), v3054(0x0)
    0x3059: RETURN v3050, v3057(0x20)

}

function redemptedCoupons(uint256)() public {
    Begin block 0x36b
    prev=[], succ=[0x37d, 0x381]
    =================================
    0x36c: v36c(0x3079) = CONST 
    0x36f: v36f(0x4) = CONST 
    0x372: v372 = CALLDATASIZE 
    0x373: v373 = SUB v372, v36f(0x4)
    0x374: v374(0x20) = CONST 
    0x377: v377 = LT v373, v374(0x20)
    0x378: v378 = ISZERO v377
    0x379: v379(0x381) = CONST 
    0x37c: JUMPI v379(0x381), v378

    Begin block 0x37d
    prev=[0x36b], succ=[]
    =================================
    0x37d: v37d(0x0) = CONST 
    0x380: REVERT v37d(0x0), v37d(0x0)

    Begin block 0x381
    prev=[0x36b], succ=[0xa13]
    =================================
    0x383: v383 = CALLDATALOAD v36f(0x4)
    0x384: v384(0xa13) = CONST 
    0x387: JUMP v384(0xa13)

    Begin block 0xa13
    prev=[0x381], succ=[0x3079]
    =================================
    0xa14: va14(0x10) = CONST 
    0xa16: va16(0x20) = CONST 
    0xa18: MSTORE va16(0x20), va14(0x10)
    0xa19: va19(0x0) = CONST 
    0xa1d: MSTORE va19(0x0), v383
    0xa1e: va1e(0x40) = CONST 
    0xa21: va21 = SHA3 va19(0x0), va1e(0x40)
    0xa22: va22 = SLOAD va21
    0xa24: JUMP v36c(0x3079)

    Begin block 0x3079
    prev=[0xa13], succ=[]
    =================================
    0x307a: v307a(0x40) = CONST 
    0x307d: v307d = MLOAD v307a(0x40)
    0x3080: MSTORE v307d, va22
    0x3081: v3081 = MLOAD v307a(0x40)
    0x3085: v3085(0x0) = SUB v307d, v3081
    0x3086: v3086(0x20) = CONST 
    0x3088: v3088(0x20) = ADD v3086(0x20), v3085(0x0)
    0x308a: RETURN v3081, v3088(0x20)

}

function setDollarOracle(address)() public {
    Begin block 0x388
    prev=[], succ=[0x39a, 0x39e]
    =================================
    0x389: v389(0x30aa) = CONST 
    0x38c: v38c(0x4) = CONST 
    0x38f: v38f = CALLDATASIZE 
    0x390: v390 = SUB v38f, v38c(0x4)
    0x391: v391(0x20) = CONST 
    0x394: v394 = LT v390, v391(0x20)
    0x395: v395 = ISZERO v394
    0x396: v396(0x39e) = CONST 
    0x399: JUMPI v396(0x39e), v395

    Begin block 0x39a
    prev=[0x388], succ=[]
    =================================
    0x39a: v39a(0x0) = CONST 
    0x39d: REVERT v39a(0x0), v39a(0x0)

    Begin block 0x39e
    prev=[0x388], succ=[0xa25]
    =================================
    0x3a0: v3a0 = CALLDATALOAD v38c(0x4)
    0x3a1: v3a1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3b6: v3b6 = AND v3a1(0xffffffffffffffffffffffffffffffffffffffff), v3a0
    0x3b7: v3b7(0xa25) = CONST 
    0x3ba: JUMP v3b7(0xa25)

    Begin block 0xa25
    prev=[0x39e], succ=[0xa45, 0xa95]
    =================================
    0xa26: va26(0x1) = CONST 
    0xa28: va28 = SLOAD va26(0x1)
    0xa29: va29(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa3e: va3e = AND va29(0xffffffffffffffffffffffffffffffffffffffff), va28
    0xa3f: va3f = CALLER 
    0xa40: va40 = EQ va3f, va3e
    0xa41: va41(0xa95) = CONST 
    0xa44: JUMPI va41(0xa95), va40

    Begin block 0xa45
    prev=[0xa25], succ=[]
    =================================
    0xa45: va45(0x40) = CONST 
    0xa47: va47 = MLOAD va45(0x40)
    0xa48: va48(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa6a: MSTORE va47, va48(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa6b: va6b(0x4) = CONST 
    0xa6d: va6d = ADD va6b(0x4), va47
    0xa70: va70(0x20) = CONST 
    0xa72: va72 = ADD va70(0x20), va6d
    0xa75: va75(0x20) = SUB va72, va6d
    0xa77: MSTORE va6d, va75(0x20)
    0xa78: va78(0x28) = CONST 
    0xa7b: MSTORE va72, va78(0x28)
    0xa7c: va7c(0x20) = CONST 
    0xa7e: va7e = ADD va7c(0x20), va72
    0xa80: va80(0x2b90) = CONST 
    0xa83: va83(0x28) = CONST 
    0xa86: CODECOPY va7e, va80(0x2b90), va83(0x28)
    0xa87: va87(0x40) = CONST 
    0xa89: va89 = ADD va87(0x40), va7e
    0xa8d: va8d(0x40) = CONST 
    0xa8f: va8f = MLOAD va8d(0x40)
    0xa92: va92(0x84) = SUB va89, va8f
    0xa94: REVERT va8f, va92(0x84)

    Begin block 0xa95
    prev=[0xa25], succ=[0x30aa]
    =================================
    0xa96: va96(0x4) = CONST 
    0xa99: va99 = SLOAD va96(0x4)
    0xa9a: va9a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xabb: vabb = AND va9a(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), va99
    0xabc: vabc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xad4: vad4 = AND vabc(0xffffffffffffffffffffffffffffffffffffffff), v3b6
    0xad8: vad8 = OR vad4, vabb
    0xada: SSTORE va96(0x4), vad8
    0xadb: JUMP v389(0x30aa)

    Begin block 0x30aa
    prev=[0xa95], succ=[]
    =================================
    0x30ab: STOP 

}

function getPurchasedCouponHistory(address)() public {
    Begin block 0x3bb
    prev=[], succ=[0x3cd, 0x3d1]
    =================================
    0x3bc: v3bc(0x3ee) = CONST 
    0x3bf: v3bf(0x4) = CONST 
    0x3c2: v3c2 = CALLDATASIZE 
    0x3c3: v3c3 = SUB v3c2, v3bf(0x4)
    0x3c4: v3c4(0x20) = CONST 
    0x3c7: v3c7 = LT v3c3, v3c4(0x20)
    0x3c8: v3c8 = ISZERO v3c7
    0x3c9: v3c9(0x3d1) = CONST 
    0x3cc: JUMPI v3c9(0x3d1), v3c8

    Begin block 0x3cd
    prev=[0x3bb], succ=[]
    =================================
    0x3cd: v3cd(0x0) = CONST 
    0x3d0: REVERT v3cd(0x0), v3cd(0x0)

    Begin block 0x3d1
    prev=[0x3bb], succ=[0xadc]
    =================================
    0x3d3: v3d3 = CALLDATALOAD v3bf(0x4)
    0x3d4: v3d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3e9: v3e9 = AND v3d4(0xffffffffffffffffffffffffffffffffffffffff), v3d3
    0x3ea: v3ea(0xadc) = CONST 
    0x3ed: JUMP v3ea(0xadc)

    Begin block 0xadc
    prev=[0x3d1], succ=[0xb1a, 0xb1e]
    =================================
    0xadd: vadd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaf3: vaf3 = AND v3e9, vadd(0xffffffffffffffffffffffffffffffffffffffff)
    0xaf4: vaf4(0x0) = CONST 
    0xaf8: MSTORE vaf4(0x0), vaf3
    0xaf9: vaf9(0xf) = CONST 
    0xafb: vafb(0x20) = CONST 
    0xafd: MSTORE vafb(0x20), vaf9(0xf)
    0xafe: vafe(0x40) = CONST 
    0xb01: vb01 = SHA3 vaf4(0x0), vafe(0x40)
    0xb02: vb02 = SLOAD vb01
    0xb03: vb03(0x60) = CONST 
    0xb09: vb09(0xffffffffffffffff) = CONST 
    0xb13: vb13 = GT vb02, vb09(0xffffffffffffffff)
    0xb15: vb15 = ISZERO vb13
    0xb16: vb16(0xb1e) = CONST 
    0xb19: JUMPI vb16(0xb1e), vb15

    Begin block 0xb1a
    prev=[0xadc], succ=[]
    =================================
    0xb1a: vb1a(0x0) = CONST 
    0xb1d: REVERT vb1a(0x0), vb1a(0x0)

    Begin block 0xb1e
    prev=[0xadc], succ=[0xb48, 0xb39]
    =================================
    0xb20: vb20(0x40) = CONST 
    0xb22: vb22 = MLOAD vb20(0x40)
    0xb26: MSTORE vb22, vb02
    0xb28: vb28(0x20) = CONST 
    0xb2a: vb2a = MUL vb28(0x20), vb02
    0xb2b: vb2b(0x20) = CONST 
    0xb2d: vb2d = ADD vb2b(0x20), vb2a
    0xb2f: vb2f = ADD vb22, vb2d
    0xb30: vb30(0x40) = CONST 
    0xb32: MSTORE vb30(0x40), vb2f
    0xb34: vb34 = ISZERO vb02
    0xb35: vb35(0xb48) = CONST 
    0xb38: JUMPI vb35(0xb48), vb34

    Begin block 0xb48
    prev=[0xb1e, 0xb39], succ=[0xb5e, 0xb62]
    =================================
    0xb4d: vb4d(0xffffffffffffffff) = CONST 
    0xb57: vb57 = GT vb02, vb4d(0xffffffffffffffff)
    0xb59: vb59 = ISZERO vb57
    0xb5a: vb5a(0xb62) = CONST 
    0xb5d: JUMPI vb5a(0xb62), vb59

    Begin block 0xb5e
    prev=[0xb48], succ=[]
    =================================
    0xb5e: vb5e(0x0) = CONST 
    0xb61: REVERT vb5e(0x0), vb5e(0x0)

    Begin block 0xb62
    prev=[0xb48], succ=[0xb8c, 0xb7d]
    =================================
    0xb64: vb64(0x40) = CONST 
    0xb66: vb66 = MLOAD vb64(0x40)
    0xb6a: MSTORE vb66, vb02
    0xb6c: vb6c(0x20) = CONST 
    0xb6e: vb6e = MUL vb6c(0x20), vb02
    0xb6f: vb6f(0x20) = CONST 
    0xb71: vb71 = ADD vb6f(0x20), vb6e
    0xb73: vb73 = ADD vb66, vb71
    0xb74: vb74(0x40) = CONST 
    0xb76: MSTORE vb74(0x40), vb73
    0xb78: vb78 = ISZERO vb02
    0xb79: vb79(0xb8c) = CONST 
    0xb7c: JUMPI vb79(0xb8c), vb78

    Begin block 0xb8c
    prev=[0xb62, 0xb7d], succ=[0xb92]
    =================================
    0xb90: vb90(0x0) = CONST 

    Begin block 0xb92
    prev=[0xb8c, 0xc46], succ=[0xb9b, 0xc50]
    =================================
    0xb92_0x0: vb92_0 = PHI vb90(0x0), vc4b
    0xb95: vb95 = LT vb92_0, vb02
    0xb96: vb96 = ISZERO vb95
    0xb97: vb97(0xc50) = CONST 
    0xb9a: JUMPI vb97(0xc50), vb96

    Begin block 0xb9b
    prev=[0xb92], succ=[0xbca, 0xbcb]
    =================================
    0xb9b: vb9b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb9b_0x0: vb9b_0 = PHI vb90(0x0), vc4b
    0xbb1: vbb1 = AND v3e9, vb9b(0xffffffffffffffffffffffffffffffffffffffff)
    0xbb2: vbb2(0x0) = CONST 
    0xbb6: MSTORE vbb2(0x0), vbb1
    0xbb7: vbb7(0xf) = CONST 
    0xbb9: vbb9(0x20) = CONST 
    0xbbb: MSTORE vbb9(0x20), vbb7(0xf)
    0xbbc: vbbc(0x40) = CONST 
    0xbbf: vbbf = SHA3 vbb2(0x0), vbbc(0x40)
    0xbc1: vbc1 = SLOAD vbbf
    0xbc5: vbc5 = LT vb9b_0, vbc1
    0xbc6: vbc6(0xbcb) = CONST 
    0xbc9: JUMPI vbc6(0xbcb), vbc5

    Begin block 0xbca
    prev=[0xb9b], succ=[]
    =================================
    0xbca: THROW 

    Begin block 0xbcb
    prev=[0xb9b], succ=[0xc46, 0xc0e]
    =================================
    0xbcb_0x0: vbcb_0 = PHI vb90(0x0), vc4b
    0xbcc: vbcc(0x0) = CONST 
    0xbd0: MSTORE vbcc(0x0), vbbf
    0xbd1: vbd1(0x20) = CONST 
    0xbd5: vbd5 = SHA3 vbcc(0x0), vbd1(0x20)
    0xbd8: vbd8 = ADD vbcb_0, vbd5
    0xbd9: vbd9 = SLOAD vbd8
    0xbda: vbda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xbf0: vbf0 = AND v3e9, vbda(0xffffffffffffffffffffffffffffffffffffffff)
    0xbf2: MSTORE vbcc(0x0), vbf0
    0xbf3: vbf3(0xe) = CONST 
    0xbf6: MSTORE vbd1(0x20), vbf3(0xe)
    0xbf7: vbf7(0x40) = CONST 
    0xbfb: vbfb = SHA3 vbcc(0x0), vbf7(0x40)
    0xbfe: MSTORE vbcc(0x0), vbd9
    0xc01: MSTORE vbd1(0x20), vbfb
    0xc03: vc03 = SHA3 vbcc(0x0), vbf7(0x40)
    0xc04: vc04 = SLOAD vc03
    0xc09: vc09 = ISZERO vc04
    0xc0a: vc0a(0xc46) = CONST 
    0xc0d: JUMPI vc0a(0xc46), vc09

    Begin block 0xc46
    prev=[0xbcb, 0xc33], succ=[0xb92]
    =================================
    0xc46_0x2: vc46_2 = PHI vb90(0x0), vc4b
    0xc49: vc49(0x1) = CONST 
    0xc4b: vc4b = ADD vc49(0x1), vc46_2
    0xc4c: vc4c(0xb92) = CONST 
    0xc4f: JUMP vc4c(0xb92)

    Begin block 0xc0e
    prev=[0xbcb], succ=[0xc19, 0xc1a]
    =================================
    0xc0e_0x6: vc0e_6 = PHI vaf4(0x0), vc43
    0xc12: vc12 = MLOAD vb22
    0xc14: vc14 = LT vc0e_6, vc12
    0xc15: vc15(0xc1a) = CONST 
    0xc18: JUMPI vc15(0xc1a), vc14

    Begin block 0xc19
    prev=[0xc0e], succ=[]
    =================================
    0xc19: THROW 

    Begin block 0xc1a
    prev=[0xc0e], succ=[0xc32, 0xc33]
    =================================
    0xc1a_0x0: vc1a_0 = PHI vaf4(0x0), vc43
    0xc1a_0x9: vc1a_9 = PHI vaf4(0x0), vc43
    0xc1b: vc1b(0x20) = CONST 
    0xc1d: vc1d = MUL vc1b(0x20), vc1a_0
    0xc1e: vc1e(0x20) = CONST 
    0xc20: vc20 = ADD vc1e(0x20), vc1d
    0xc21: vc21 = ADD vc20, vb22
    0xc24: MSTORE vc21, vbd9
    0xc2b: vc2b = MLOAD vb66
    0xc2d: vc2d = LT vc1a_9, vc2b
    0xc2e: vc2e(0xc33) = CONST 
    0xc31: JUMPI vc2e(0xc33), vc2d

    Begin block 0xc32
    prev=[0xc1a], succ=[]
    =================================
    0xc32: THROW 

    Begin block 0xc33
    prev=[0xc1a], succ=[0xc46]
    =================================
    0xc33_0x0: vc33_0 = PHI vaf4(0x0), vc43
    0xc33_0x9: vc33_9 = PHI vaf4(0x0), vc43
    0xc34: vc34(0x20) = CONST 
    0xc36: vc36 = MUL vc34(0x20), vc33_0
    0xc37: vc37(0x20) = CONST 
    0xc39: vc39 = ADD vc37(0x20), vc36
    0xc3a: vc3a = ADD vc39, vb66
    0xc3d: MSTORE vc3a, vc04
    0xc41: vc41(0x1) = CONST 
    0xc43: vc43 = ADD vc41(0x1), vc33_9

    Begin block 0xc50
    prev=[0xb92], succ=[0x3ee]
    =================================
    0xc58: JUMP v3bc(0x3ee)

    Begin block 0x3ee
    prev=[0xc50], succ=[0x420]
    =================================
    0x3ee_0x2: v3ee_2 = PHI vaf4(0x0), vc43
    0x3ef: v3ef(0x40) = CONST 
    0x3f1: v3f1 = MLOAD v3ef(0x40)
    0x3f5: MSTORE v3f1, v3ee_2
    0x3f6: v3f6(0x20) = CONST 
    0x3f8: v3f8 = ADD v3f6(0x20), v3f1
    0x3fa: v3fa(0x20) = CONST 
    0x3fc: v3fc = ADD v3fa(0x20), v3f8
    0x3fe: v3fe(0x20) = CONST 
    0x400: v400 = ADD v3fe(0x20), v3fc
    0x403: v403(0x60) = SUB v400, v3f1
    0x405: MSTORE v3f8, v403(0x60)
    0x409: v409 = MLOAD vb22
    0x40b: MSTORE v400, v409
    0x40c: v40c(0x20) = CONST 
    0x40e: v40e = ADD v40c(0x20), v400
    0x412: v412 = MLOAD vb22
    0x414: v414(0x20) = CONST 
    0x416: v416 = ADD v414(0x20), vb22
    0x418: v418(0x20) = CONST 
    0x41a: v41a = MUL v418(0x20), v412
    0x41e: v41e(0x0) = CONST 

    Begin block 0x420
    prev=[0x3ee, 0x429], succ=[0x438, 0x429]
    =================================
    0x420_0x0: v420_0 = PHI v41e(0x0), v433
    0x423: v423 = LT v420_0, v41a
    0x424: v424 = ISZERO v423
    0x425: v425(0x438) = CONST 
    0x428: JUMPI v425(0x438), v424

    Begin block 0x438
    prev=[0x420], succ=[0x45f]
    =================================
    0x43f: v43f = ADD v41a, v40e
    0x442: v442 = SUB v43f, v3f1
    0x444: MSTORE v3fc, v442
    0x448: v448 = MLOAD vb66
    0x44a: MSTORE v43f, v448
    0x44b: v44b(0x20) = CONST 
    0x44d: v44d = ADD v44b(0x20), v43f
    0x451: v451 = MLOAD vb66
    0x453: v453(0x20) = CONST 
    0x455: v455 = ADD v453(0x20), vb66
    0x457: v457(0x20) = CONST 
    0x459: v459 = MUL v457(0x20), v451
    0x45d: v45d(0x0) = CONST 

    Begin block 0x45f
    prev=[0x438, 0x468], succ=[0x477, 0x468]
    =================================
    0x45f_0x0: v45f_0 = PHI v45d(0x0), v472
    0x462: v462 = LT v45f_0, v459
    0x463: v463 = ISZERO v462
    0x464: v464(0x477) = CONST 
    0x467: JUMPI v464(0x477), v463

    Begin block 0x477
    prev=[0x45f], succ=[]
    =================================
    0x47e: v47e = ADD v459, v44d
    0x486: v486(0x40) = CONST 
    0x488: v488 = MLOAD v486(0x40)
    0x48b: v48b = SUB v47e, v488
    0x48d: RETURN v488, v48b

    Begin block 0x468
    prev=[0x45f], succ=[0x45f]
    =================================
    0x468_0x0: v468_0 = PHI v45d(0x0), v472
    0x46a: v46a = ADD v468_0, v455
    0x46b: v46b = MLOAD v46a
    0x46e: v46e = ADD v468_0, v44d
    0x46f: MSTORE v46e, v46b
    0x470: v470(0x20) = CONST 
    0x472: v472 = ADD v470(0x20), v468_0
    0x473: v473(0x45f) = CONST 
    0x476: JUMP v473(0x45f)

    Begin block 0x429
    prev=[0x420], succ=[0x420]
    =================================
    0x429_0x0: v429_0 = PHI v41e(0x0), v433
    0x42b: v42b = ADD v429_0, v416
    0x42c: v42c = MLOAD v42b
    0x42f: v42f = ADD v429_0, v40e
    0x430: MSTORE v42f, v42c
    0x431: v431(0x20) = CONST 
    0x433: v433 = ADD v431(0x20), v429_0
    0x434: v434(0x420) = CONST 
    0x437: JUMP v434(0x420)

    Begin block 0xb7d
    prev=[0xb62], succ=[0xb8c]
    =================================
    0xb7e: vb7e(0x20) = CONST 
    0xb80: vb80 = ADD vb7e(0x20), vb66
    0xb81: vb81(0x20) = CONST 
    0xb84: vb84 = MUL vb02, vb81(0x20)
    0xb86: vb86 = CALLDATASIZE 
    0xb88: CALLDATACOPY vb80, vb86, vb84
    0xb89: vb89 = ADD vb84, vb80

    Begin block 0xb39
    prev=[0xb1e], succ=[0xb48]
    =================================
    0xb3a: vb3a(0x20) = CONST 
    0xb3c: vb3c = ADD vb3a(0x20), vb22
    0xb3d: vb3d(0x20) = CONST 
    0xb40: vb40 = MUL vb02, vb3d(0x20)
    0xb42: vb42 = CALLDATASIZE 
    0xb44: CALLDATACOPY vb3c, vb42, vb40
    0xb45: vb45 = ADD vb40, vb3c

}

function bondSupply()() public {
    Begin block 0x48e
    prev=[], succ=[0xc59]
    =================================
    0x48f: v48f(0x30cb) = CONST 
    0x492: v492(0xc59) = CONST 
    0x495: JUMP v492(0xc59)

    Begin block 0xc59
    prev=[0x48e], succ=[0x30cb]
    =================================
    0xc5a: vc5a(0x6) = CONST 
    0xc5c: vc5c = SLOAD vc5a(0x6)
    0xc5e: JUMP v48f(0x30cb)

    Begin block 0x30cb
    prev=[0xc59], succ=[]
    =================================
    0x30cc: v30cc(0x40) = CONST 
    0x30cf: v30cf = MLOAD v30cc(0x40)
    0x30d2: MSTORE v30cf, vc5c
    0x30d3: v30d3 = MLOAD v30cc(0x40)
    0x30d7: v30d7(0x0) = SUB v30cf, v30d3
    0x30d8: v30d8(0x20) = CONST 
    0x30da: v30da(0x20) = ADD v30d8(0x20), v30d7(0x0)
    0x30dc: RETURN v30d3, v30da(0x20)

}

function discountPercent()() public {
    Begin block 0x496
    prev=[], succ=[0xc5f]
    =================================
    0x497: v497(0x30fc) = CONST 
    0x49a: v49a(0xc5f) = CONST 
    0x49d: JUMP v49a(0xc5f)

    Begin block 0xc5f
    prev=[0x496], succ=[0x30fc]
    =================================
    0xc60: vc60(0x9) = CONST 
    0xc62: vc62 = SLOAD vc60(0x9)
    0xc64: JUMP v497(0x30fc)

    Begin block 0x30fc
    prev=[0xc5f], succ=[]
    =================================
    0x30fd: v30fd(0x40) = CONST 
    0x3100: v3100 = MLOAD v30fd(0x40)
    0x3103: MSTORE v3100, vc62
    0x3104: v3104 = MLOAD v30fd(0x40)
    0x3108: v3108(0x0) = SUB v3100, v3104
    0x3109: v3109(0x20) = CONST 
    0x310b: v310b(0x20) = ADD v3109(0x20), v3108(0x0)
    0x310d: RETURN v3104, v310b(0x20)

}

function couponSupply()() public {
    Begin block 0x49e
    prev=[], succ=[0xc65]
    =================================
    0x49f: v49f(0x312d) = CONST 
    0x4a2: v4a2(0xc65) = CONST 
    0x4a5: JUMP v4a2(0xc65)

    Begin block 0xc65
    prev=[0x49e], succ=[0x312d]
    =================================
    0xc66: vc66(0x6) = CONST 
    0xc68: vc68 = SLOAD vc66(0x6)
    0xc6a: JUMP v49f(0x312d)

    Begin block 0x312d
    prev=[0xc65], succ=[]
    =================================
    0x312e: v312e(0x40) = CONST 
    0x3131: v3131 = MLOAD v312e(0x40)
    0x3134: MSTORE v3131, vc68
    0x3135: v3135 = MLOAD v312e(0x40)
    0x3139: v3139(0x0) = SUB v3131, v3135
    0x313a: v313a(0x20) = CONST 
    0x313c: v313c(0x20) = ADD v313a(0x20), v3139(0x0)
    0x313e: RETURN v3135, v313c(0x20)

}

function maxPremiumRate()() public {
    Begin block 0x4a6
    prev=[], succ=[0xc6b]
    =================================
    0x4a7: v4a7(0x315e) = CONST 
    0x4aa: v4aa(0xc6b) = CONST 
    0x4ad: JUMP v4aa(0xc6b)

    Begin block 0xc6b
    prev=[0x4a6], succ=[0x315e]
    =================================
    0xc6c: vc6c(0xc) = CONST 
    0xc6e: vc6e = SLOAD vc6c(0xc)
    0xc70: JUMP v4a7(0x315e)

    Begin block 0x315e
    prev=[0xc6b], succ=[]
    =================================
    0x315f: v315f(0x40) = CONST 
    0x3162: v3162 = MLOAD v315f(0x40)
    0x3165: MSTORE v3162, vc6e
    0x3166: v3166 = MLOAD v315f(0x40)
    0x316a: v316a(0x0) = SUB v3162, v3166
    0x316b: v316b(0x20) = CONST 
    0x316d: v316d(0x20) = ADD v316b(0x20), v316a(0x0)
    0x316f: RETURN v3166, v316d(0x20)

}

function isInitialized()() public {
    Begin block 0x4ae
    prev=[], succ=[0xc71]
    =================================
    0x4af: v4af(0x318f) = CONST 
    0x4b2: v4b2(0xc71) = CONST 
    0x4b5: JUMP v4b2(0xc71)

    Begin block 0xc71
    prev=[0x4ae], succ=[0x318f]
    =================================
    0xc72: vc72(0x1) = CONST 
    0xc74: vc74 = SLOAD vc72(0x1)
    0xc75: vc75(0x10000000000000000000000000000000000000000) = CONST 
    0xc8c: vc8c = DIV vc74, vc75(0x10000000000000000000000000000000000000000)
    0xc8d: vc8d(0xff) = CONST 
    0xc8f: vc8f = AND vc8d(0xff), vc8c
    0xc91: JUMP v4af(0x318f)

    Begin block 0x318f
    prev=[0xc71], succ=[]
    =================================
    0x3190: v3190(0x40) = CONST 
    0x3193: v3193 = MLOAD v3190(0x40)
    0x3195: v3195 = ISZERO vc8f
    0x3196: v3196 = ISZERO v3195
    0x3198: MSTORE v3193, v3196
    0x3199: v3199 = MLOAD v3190(0x40)
    0x319d: v319d(0x0) = SUB v3193, v3199
    0x319e: v319e(0x20) = CONST 
    0x31a0: v31a0(0x20) = ADD v319e(0x20), v319d(0x0)
    0x31a2: RETURN v3199, v31a0(0x20)

}

function getCouponPremiumRate()() public {
    Begin block 0x4b6
    prev=[], succ=[0x3010x4b6]
    =================================
    0x4b7: v4b7(0x301) = CONST 
    0x4ba: v4ba(0xc92) = CONST 
    0x4bd: v4bd_0 = CALLPRIVATE v4ba(0xc92), v4b7(0x301)

    Begin block 0x3010x4b6
    prev=[0x4b6], succ=[]
    =================================
    0x3020x4b6: v4b6302(0x40) = CONST 
    0x3050x4b6: v4b6305 = MLOAD v4b6302(0x40)
    0x3080x4b6: MSTORE v4b6305, v4bd_0
    0x3090x4b6: v4b6309 = MLOAD v4b6302(0x40)
    0x30d0x4b6: v4b630d(0x0) = SUB v4b6305, v4b6309
    0x30e0x4b6: v4b630e(0x20) = CONST 
    0x3100x4b6: v4b6310(0x20) = ADD v4b630e(0x20), v4b630d(0x0)
    0x3120x4b6: RETURN v4b6309, v4b6310(0x20)

}

function purchasedCoupons(address,uint256)() public {
    Begin block 0x4be
    prev=[], succ=[0x4d0, 0x4d4]
    =================================
    0x4bf: v4bf(0x31c2) = CONST 
    0x4c2: v4c2(0x4) = CONST 
    0x4c5: v4c5 = CALLDATASIZE 
    0x4c6: v4c6 = SUB v4c5, v4c2(0x4)
    0x4c7: v4c7(0x40) = CONST 
    0x4ca: v4ca = LT v4c6, v4c7(0x40)
    0x4cb: v4cb = ISZERO v4ca
    0x4cc: v4cc(0x4d4) = CONST 
    0x4cf: JUMPI v4cc(0x4d4), v4cb

    Begin block 0x4d0
    prev=[0x4be], succ=[]
    =================================
    0x4d0: v4d0(0x0) = CONST 
    0x4d3: REVERT v4d0(0x0), v4d0(0x0)

    Begin block 0x4d4
    prev=[0x4be], succ=[0xd32]
    =================================
    0x4d6: v4d6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4ec: v4ec = CALLDATALOAD v4c2(0x4)
    0x4ed: v4ed = AND v4ec, v4d6(0xffffffffffffffffffffffffffffffffffffffff)
    0x4ef: v4ef(0x20) = CONST 
    0x4f1: v4f1(0x24) = ADD v4ef(0x20), v4c2(0x4)
    0x4f2: v4f2 = CALLDATALOAD v4f1(0x24)
    0x4f3: v4f3(0xd32) = CONST 
    0x4f6: JUMP v4f3(0xd32)

    Begin block 0xd32
    prev=[0x4d4], succ=[0x31c2]
    =================================
    0xd33: vd33(0xe) = CONST 
    0xd35: vd35(0x20) = CONST 
    0xd39: MSTORE vd35(0x20), vd33(0xe)
    0xd3a: vd3a(0x0) = CONST 
    0xd3e: MSTORE vd3a(0x0), v4ed
    0xd3f: vd3f(0x40) = CONST 
    0xd43: vd43 = SHA3 vd3a(0x0), vd3f(0x40)
    0xd46: MSTORE vd35(0x20), vd43
    0xd49: MSTORE vd3a(0x0), v4f2
    0xd4b: vd4b = SHA3 vd3a(0x0), vd3f(0x40)
    0xd4c: vd4c = SLOAD vd4b
    0xd4e: JUMP v4bf(0x31c2)

    Begin block 0x31c2
    prev=[0xd32], succ=[]
    =================================
    0x31c3: v31c3(0x40) = CONST 
    0x31c6: v31c6 = MLOAD v31c3(0x40)
    0x31c9: MSTORE v31c6, vd4c
    0x31ca: v31ca = MLOAD v31c3(0x40)
    0x31ce: v31ce(0x0) = SUB v31c6, v31ca
    0x31cf: v31cf(0x20) = CONST 
    0x31d1: v31d1(0x20) = ADD v31cf(0x20), v31ce(0x0)
    0x31d3: RETURN v31ca, v31d1(0x20)

}

function setSideToken(address)() public {
    Begin block 0x4f7
    prev=[], succ=[0x509, 0x50d]
    =================================
    0x4f8: v4f8(0x31f3) = CONST 
    0x4fb: v4fb(0x4) = CONST 
    0x4fe: v4fe = CALLDATASIZE 
    0x4ff: v4ff = SUB v4fe, v4fb(0x4)
    0x500: v500(0x20) = CONST 
    0x503: v503 = LT v4ff, v500(0x20)
    0x504: v504 = ISZERO v503
    0x505: v505(0x50d) = CONST 
    0x508: JUMPI v505(0x50d), v504

    Begin block 0x509
    prev=[0x4f7], succ=[]
    =================================
    0x509: v509(0x0) = CONST 
    0x50c: REVERT v509(0x0), v509(0x0)

    Begin block 0x50d
    prev=[0x4f7], succ=[0xd4f]
    =================================
    0x50f: v50f = CALLDATALOAD v4fb(0x4)
    0x510: v510(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x525: v525 = AND v510(0xffffffffffffffffffffffffffffffffffffffff), v50f
    0x526: v526(0xd4f) = CONST 
    0x529: JUMP v526(0xd4f)

    Begin block 0xd4f
    prev=[0x50d], succ=[0xd6f, 0xdbf]
    =================================
    0xd50: vd50(0x1) = CONST 
    0xd52: vd52 = SLOAD vd50(0x1)
    0xd53: vd53(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd68: vd68 = AND vd53(0xffffffffffffffffffffffffffffffffffffffff), vd52
    0xd69: vd69 = CALLER 
    0xd6a: vd6a = EQ vd69, vd68
    0xd6b: vd6b(0xdbf) = CONST 
    0xd6e: JUMPI vd6b(0xdbf), vd6a

    Begin block 0xd6f
    prev=[0xd4f], succ=[]
    =================================
    0xd6f: vd6f(0x40) = CONST 
    0xd71: vd71 = MLOAD vd6f(0x40)
    0xd72: vd72(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xd94: MSTORE vd71, vd72(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd95: vd95(0x4) = CONST 
    0xd97: vd97 = ADD vd95(0x4), vd71
    0xd9a: vd9a(0x20) = CONST 
    0xd9c: vd9c = ADD vd9a(0x20), vd97
    0xd9f: vd9f(0x20) = SUB vd9c, vd97
    0xda1: MSTORE vd97, vd9f(0x20)
    0xda2: vda2(0x28) = CONST 
    0xda5: MSTORE vd9c, vda2(0x28)
    0xda6: vda6(0x20) = CONST 
    0xda8: vda8 = ADD vda6(0x20), vd9c
    0xdaa: vdaa(0x2b90) = CONST 
    0xdad: vdad(0x28) = CONST 
    0xdb0: CODECOPY vda8, vdaa(0x2b90), vdad(0x28)
    0xdb1: vdb1(0x40) = CONST 
    0xdb3: vdb3 = ADD vdb1(0x40), vda8
    0xdb7: vdb7(0x40) = CONST 
    0xdb9: vdb9 = MLOAD vdb7(0x40)
    0xdbc: vdbc(0x84) = SUB vdb3, vdb9
    0xdbe: REVERT vdb9, vdbc(0x84)

    Begin block 0xdbf
    prev=[0xd4f], succ=[0x31f3]
    =================================
    0xdc0: vdc0(0x5) = CONST 
    0xdc3: vdc3 = SLOAD vdc0(0x5)
    0xdc4: vdc4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xde5: vde5 = AND vdc4(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vdc3
    0xde6: vde6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdfe: vdfe = AND vde6(0xffffffffffffffffffffffffffffffffffffffff), v525
    0xe02: ve02 = OR vdfe, vde5
    0xe04: SSTORE vdc0(0x5), ve02
    0xe05: JUMP v4f8(0x31f3)

    Begin block 0x31f3
    prev=[0xdbf], succ=[]
    =================================
    0x31f4: STOP 

}

function setPremiumPercent(uint256)() public {
    Begin block 0x52a
    prev=[], succ=[0x53c, 0x540]
    =================================
    0x52b: v52b(0x3214) = CONST 
    0x52e: v52e(0x4) = CONST 
    0x531: v531 = CALLDATASIZE 
    0x532: v532 = SUB v531, v52e(0x4)
    0x533: v533(0x20) = CONST 
    0x536: v536 = LT v532, v533(0x20)
    0x537: v537 = ISZERO v536
    0x538: v538(0x540) = CONST 
    0x53b: JUMPI v538(0x540), v537

    Begin block 0x53c
    prev=[0x52a], succ=[]
    =================================
    0x53c: v53c(0x0) = CONST 
    0x53f: REVERT v53c(0x0), v53c(0x0)

    Begin block 0x540
    prev=[0x52a], succ=[0xe06]
    =================================
    0x542: v542 = CALLDATALOAD v52e(0x4)
    0x543: v543(0xe06) = CONST 
    0x546: JUMP v543(0xe06)

    Begin block 0xe06
    prev=[0x540], succ=[0xe26, 0xe76]
    =================================
    0xe07: ve07(0x1) = CONST 
    0xe09: ve09 = SLOAD ve07(0x1)
    0xe0a: ve0a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe1f: ve1f = AND ve0a(0xffffffffffffffffffffffffffffffffffffffff), ve09
    0xe20: ve20 = CALLER 
    0xe21: ve21 = EQ ve20, ve1f
    0xe22: ve22(0xe76) = CONST 
    0xe25: JUMPI ve22(0xe76), ve21

    Begin block 0xe26
    prev=[0xe06], succ=[]
    =================================
    0xe26: ve26(0x40) = CONST 
    0xe28: ve28 = MLOAD ve26(0x40)
    0xe29: ve29(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xe4b: MSTORE ve28, ve29(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xe4c: ve4c(0x4) = CONST 
    0xe4e: ve4e = ADD ve4c(0x4), ve28
    0xe51: ve51(0x20) = CONST 
    0xe53: ve53 = ADD ve51(0x20), ve4e
    0xe56: ve56(0x20) = SUB ve53, ve4e
    0xe58: MSTORE ve4e, ve56(0x20)
    0xe59: ve59(0x28) = CONST 
    0xe5c: MSTORE ve53, ve59(0x28)
    0xe5d: ve5d(0x20) = CONST 
    0xe5f: ve5f = ADD ve5d(0x20), ve53
    0xe61: ve61(0x2b90) = CONST 
    0xe64: ve64(0x28) = CONST 
    0xe67: CODECOPY ve5f, ve61(0x2b90), ve64(0x28)
    0xe68: ve68(0x40) = CONST 
    0xe6a: ve6a = ADD ve68(0x40), ve5f
    0xe6e: ve6e(0x40) = CONST 
    0xe70: ve70 = MLOAD ve6e(0x40)
    0xe73: ve73(0x84) = SUB ve6a, ve70
    0xe75: REVERT ve70, ve73(0x84)

    Begin block 0xe76
    prev=[0xe06], succ=[0xe81, 0xee7]
    =================================
    0xe77: ve77(0x4e20) = CONST 
    0xe7b: ve7b = GT v542, ve77(0x4e20)
    0xe7c: ve7c = ISZERO ve7b
    0xe7d: ve7d(0xee7) = CONST 
    0xe80: JUMPI ve7d(0xee7), ve7c

    Begin block 0xe81
    prev=[0xe76], succ=[]
    =================================
    0xe81: ve81(0x40) = CONST 
    0xe84: ve84 = MLOAD ve81(0x40)
    0xe85: ve85(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xea7: MSTORE ve84, ve85(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xea8: vea8(0x20) = CONST 
    0xeaa: veaa(0x4) = CONST 
    0xead: vead = ADD ve84, veaa(0x4)
    0xeae: MSTORE vead, vea8(0x20)
    0xeaf: veaf(0x1c) = CONST 
    0xeb1: veb1(0x24) = CONST 
    0xeb4: veb4 = ADD ve84, veb1(0x24)
    0xeb5: MSTORE veb4, veaf(0x1c)
    0xeb6: veb6(0x5f7072656d69756d50657263656e74206973206f766572203230302500000000) = CONST 
    0xed7: ved7(0x44) = CONST 
    0xeda: veda = ADD ve84, ved7(0x44)
    0xedb: MSTORE veda, veb6(0x5f7072656d69756d50657263656e74206973206f766572203230302500000000)
    0xedd: vedd = MLOAD ve81(0x40)
    0xee1: vee1(0x0) = SUB ve84, vedd
    0xee2: vee2(0x64) = CONST 
    0xee4: vee4(0x64) = ADD vee2(0x64), vee1(0x0)
    0xee6: REVERT vedd, vee4(0x64)

    Begin block 0xee7
    prev=[0xe76], succ=[0x3214]
    =================================
    0xee8: vee8(0xb) = CONST 
    0xeea: SSTORE vee8(0xb), v542
    0xeeb: JUMP v52b(0x3214)

    Begin block 0x3214
    prev=[0xee7], succ=[]
    =================================
    0x3215: STOP 

}

function dollarOracle()() public {
    Begin block 0x547
    prev=[], succ=[0xeec]
    =================================
    0x548: v548(0x3235) = CONST 
    0x54b: v54b(0xeec) = CONST 
    0x54e: JUMP v54b(0xeec)

    Begin block 0xeec
    prev=[0x547], succ=[0x3235]
    =================================
    0xeed: veed(0x4) = CONST 
    0xeef: veef = SLOAD veed(0x4)
    0xef0: vef0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf05: vf05 = AND vef0(0xffffffffffffffffffffffffffffffffffffffff), veef
    0xf07: JUMP v548(0x3235)

    Begin block 0x3235
    prev=[0xeec], succ=[]
    =================================
    0x3236: v3236(0x40) = CONST 
    0x3239: v3239 = MLOAD v3236(0x40)
    0x323a: v323a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3251: v3251 = AND vf05, v323a(0xffffffffffffffffffffffffffffffffffffffff)
    0x3253: MSTORE v3239, v3251
    0x3254: v3254 = MLOAD v3236(0x40)
    0x3258: v3258(0x0) = SUB v3239, v3254
    0x3259: v3259(0x20) = CONST 
    0x325b: v325b(0x20) = ADD v3259(0x20), v3258(0x0)
    0x325d: RETURN v3254, v325b(0x20)

}

function dollar()() public {
    Begin block 0x578
    prev=[], succ=[0xf08]
    =================================
    0x579: v579(0x327d) = CONST 
    0x57c: v57c(0xf08) = CONST 
    0x57f: JUMP v57c(0xf08)

    Begin block 0xf08
    prev=[0x578], succ=[0x327d]
    =================================
    0xf09: vf09(0x2) = CONST 
    0xf0b: vf0b = SLOAD vf09(0x2)
    0xf0c: vf0c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf21: vf21 = AND vf0c(0xffffffffffffffffffffffffffffffffffffffff), vf0b
    0xf23: JUMP v579(0x327d)

    Begin block 0x327d
    prev=[0xf08], succ=[]
    =================================
    0x327e: v327e(0x40) = CONST 
    0x3281: v3281 = MLOAD v327e(0x40)
    0x3282: v3282(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3299: v3299 = AND vf21, v3282(0xffffffffffffffffffffffffffffffffffffffff)
    0x329b: MSTORE v3281, v3299
    0x329c: v329c = MLOAD v327e(0x40)
    0x32a0: v32a0(0x0) = SUB v3281, v329c
    0x32a1: v32a1(0x20) = CONST 
    0x32a3: v32a3(0x20) = ADD v32a1(0x20), v32a0(0x0)
    0x32a5: RETURN v329c, v32a3(0x20)

}

function governanceRecoverUnsupported(address,uint256,address)() public {
    Begin block 0x580
    prev=[], succ=[0x592, 0x596]
    =================================
    0x581: v581(0x32c5) = CONST 
    0x584: v584(0x4) = CONST 
    0x587: v587 = CALLDATASIZE 
    0x588: v588 = SUB v587, v584(0x4)
    0x589: v589(0x60) = CONST 
    0x58c: v58c = LT v588, v589(0x60)
    0x58d: v58d = ISZERO v58c
    0x58e: v58e(0x596) = CONST 
    0x591: JUMPI v58e(0x596), v58d

    Begin block 0x592
    prev=[0x580], succ=[]
    =================================
    0x592: v592(0x0) = CONST 
    0x595: REVERT v592(0x0), v592(0x0)

    Begin block 0x596
    prev=[0x580], succ=[0xf24]
    =================================
    0x598: v598(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ae: v5ae = CALLDATALOAD v584(0x4)
    0x5b0: v5b0 = AND v598(0xffffffffffffffffffffffffffffffffffffffff), v5ae
    0x5b2: v5b2(0x20) = CONST 
    0x5b5: v5b5(0x24) = ADD v584(0x4), v5b2(0x20)
    0x5b6: v5b6 = CALLDATALOAD v5b5(0x24)
    0x5b8: v5b8(0x40) = CONST 
    0x5bc: v5bc(0x44) = ADD v584(0x4), v5b8(0x40)
    0x5bd: v5bd = CALLDATALOAD v5bc(0x44)
    0x5be: v5be = AND v5bd, v598(0xffffffffffffffffffffffffffffffffffffffff)
    0x5bf: v5bf(0xf24) = CONST 
    0x5c2: JUMP v5bf(0xf24)

    Begin block 0xf24
    prev=[0x596], succ=[0xf44, 0xf94]
    =================================
    0xf25: vf25(0x1) = CONST 
    0xf27: vf27 = SLOAD vf25(0x1)
    0xf28: vf28(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf3d: vf3d = AND vf28(0xffffffffffffffffffffffffffffffffffffffff), vf27
    0xf3e: vf3e = CALLER 
    0xf3f: vf3f = EQ vf3e, vf3d
    0xf40: vf40(0xf94) = CONST 
    0xf43: JUMPI vf40(0xf94), vf3f

    Begin block 0xf44
    prev=[0xf24], succ=[]
    =================================
    0xf44: vf44(0x40) = CONST 
    0xf46: vf46 = MLOAD vf44(0x40)
    0xf47: vf47(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf69: MSTORE vf46, vf47(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf6a: vf6a(0x4) = CONST 
    0xf6c: vf6c = ADD vf6a(0x4), vf46
    0xf6f: vf6f(0x20) = CONST 
    0xf71: vf71 = ADD vf6f(0x20), vf6c
    0xf74: vf74(0x20) = SUB vf71, vf6c
    0xf76: MSTORE vf6c, vf74(0x20)
    0xf77: vf77(0x28) = CONST 
    0xf7a: MSTORE vf71, vf77(0x28)
    0xf7b: vf7b(0x20) = CONST 
    0xf7d: vf7d = ADD vf7b(0x20), vf71
    0xf7f: vf7f(0x2b90) = CONST 
    0xf82: vf82(0x28) = CONST 
    0xf85: CODECOPY vf7d, vf7f(0x2b90), vf82(0x28)
    0xf86: vf86(0x40) = CONST 
    0xf88: vf88 = ADD vf86(0x40), vf7d
    0xf8c: vf8c(0x40) = CONST 
    0xf8e: vf8e = MLOAD vf8c(0x40)
    0xf91: vf91(0x84) = SUB vf88, vf8e
    0xf93: REVERT vf8e, vf91(0x84)

    Begin block 0xf94
    prev=[0xf24], succ=[0x24eaB0xf94]
    =================================
    0xf95: vf95(0x3741) = CONST 
    0xf98: vf98(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfae: vfae = AND v5b0, vf98(0xffffffffffffffffffffffffffffffffffffffff)
    0xfb1: vfb1(0x24ea) = CONST 
    0xfb4: JUMP vfb1(0x24ea), v5b6, v5be, vfae, vf95(0x3741)

    Begin block 0x24eaB0xf94
    prev=[0xf94], succ=[0x2767B0x24eaB0xf94]
    =================================
    0x24ebS0xf94: v24ebVf94(0x40) = CONST 
    0x24eeS0xf94: v24eeVf94 = MLOAD v24ebVf94(0x40)
    0x24efS0xf94: v24efVf94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2505S0xf94: v2505Vf94 = AND v5be, v24efVf94(0xffffffffffffffffffffffffffffffffffffffff)
    0x2506S0xf94: v2506Vf94(0x24) = CONST 
    0x2509S0xf94: v2509Vf94 = ADD v24eeVf94, v2506Vf94(0x24)
    0x250aS0xf94: MSTORE v2509Vf94, v2505Vf94
    0x250bS0xf94: v250bVf94(0x44) = CONST 
    0x250fS0xf94: v250fVf94 = ADD v24eeVf94, v250bVf94(0x44)
    0x2512S0xf94: MSTORE v250fVf94, v5b6
    0x2514S0xf94: v2514Vf94 = MLOAD v24ebVf94(0x40)
    0x2517S0xf94: v2517Vf94(0x0) = SUB v24eeVf94, v2514Vf94
    0x251aS0xf94: v251aVf94(0x44) = ADD v250bVf94(0x44), v2517Vf94(0x0)
    0x251cS0xf94: MSTORE v2514Vf94, v251aVf94(0x44)
    0x251dS0xf94: v251dVf94(0x64) = CONST 
    0x2521S0xf94: v2521Vf94 = ADD v24eeVf94, v251dVf94(0x64)
    0x2524S0xf94: MSTORE v24ebVf94(0x40), v2521Vf94
    0x2525S0xf94: v2525Vf94(0x20) = CONST 
    0x2528S0xf94: v2528Vf94 = ADD v2514Vf94, v2525Vf94(0x20)
    0x252aS0xf94: v252aVf94 = MLOAD v2528Vf94
    0x252bS0xf94: v252bVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2548S0xf94: v2548Vf94 = AND v252bVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v252aVf94
    0x2549S0xf94: v2549Vf94(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = CONST 
    0x256aS0xf94: v256aVf94 = OR v2549Vf94(0xa9059cbb00000000000000000000000000000000000000000000000000000000), v2548Vf94
    0x256cS0xf94: MSTORE v2528Vf94, v256aVf94
    0x256dS0xf94: v256dVf94(0x38f4) = CONST 
    0x2573S0xf94: v2573Vf94(0x2767) = CONST 
    0x2576S0xf94: JUMP v2573Vf94(0x2767), v2514Vf94, vfae, v256dVf94(0x38f4)

    Begin block 0x2767B0x24eaB0xf94
    prev=[0x24eaB0xf94], succ=[0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2768S0x24eaS0xf94: v2768V24eaVf94(0x60) = CONST 
    0x276aS0x24eaS0xf94: v276aV24eaVf94(0x27c9) = CONST 
    0x276eS0x24eaS0xf94: v276eV24eaVf94(0x40) = CONST 
    0x2770S0x24eaS0xf94: v2770V24eaVf94 = MLOAD v276eV24eaVf94(0x40)
    0x2772S0x24eaS0xf94: v2772V24eaVf94(0x40) = CONST 
    0x2774S0x24eaS0xf94: v2774V24eaVf94 = ADD v2772V24eaVf94(0x40), v2770V24eaVf94
    0x2775S0x24eaS0xf94: v2775V24eaVf94(0x40) = CONST 
    0x2777S0x24eaS0xf94: MSTORE v2775V24eaVf94(0x40), v2774V24eaVf94
    0x2779S0x24eaS0xf94: v2779V24eaVf94(0x20) = CONST 
    0x277cS0x24eaS0xf94: MSTORE v2770V24eaVf94, v2779V24eaVf94(0x20)
    0x277dS0x24eaS0xf94: v277dV24eaVf94(0x20) = CONST 
    0x277fS0x24eaS0xf94: v277fV24eaVf94 = ADD v277dV24eaVf94(0x20), v2770V24eaVf94
    0x2780S0x24eaS0xf94: v2780V24eaVf94(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564) = CONST 
    0x27a2S0x24eaS0xf94: MSTORE v277fV24eaVf94, v2780V24eaVf94(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564)
    0x27a5S0x24eaS0xf94: v27a5V24eaVf94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x27baS0x24eaS0xf94: v27baV24eaVf94 = AND v27a5V24eaVf94(0xffffffffffffffffffffffffffffffffffffffff), vfae
    0x27bbS0x24eaS0xf94: v27bbV24eaVf94(0x283f) = CONST 
    0x27c2S0x24eaS0xf94: v27c2V24eaVf94(0xffffffff) = CONST 
    0x27c7S0x24eaS0xf94: v27c7V24eaVf94(0x283f) = AND v27c2V24eaVf94(0xffffffff), v27bbV24eaVf94(0x283f)
    0x27c8S0x24eaS0xf94: JUMP v27c7V24eaVf94(0x283f)

    Begin block 0x283fB0x2767B0x24eaB0xf94
    prev=[0x2767B0x24eaB0xf94], succ=[0x2856B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2840S0x2767S0x24eaS0xf94: v2840V2767V24eaVf94(0x60) = CONST 
    0x2842S0x2767S0x24eaS0xf94: v2842V2767V24eaVf94(0x284e) = CONST 
    0x2847S0x2767S0x24eaS0xf94: v2847V2767V24eaVf94(0x0) = CONST 
    0x284aS0x2767S0x24eaS0xf94: v284aV2767V24eaVf94(0x2856) = CONST 
    0x284dS0x2767S0x24eaS0xf94: JUMP v284aV2767V24eaVf94(0x2856)

    Begin block 0x2856B0x283fB0x2767B0x24eaB0xf94
    prev=[0x283fB0x2767B0x24eaB0xf94], succ=[0x2861B0x283fB0x2767B0x24eaB0xf94, 0x28b1B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2857S0x283fS0x2767S0x24eaS0xf94: v2857V283fV2767V24eaVf94(0x60) = CONST 
    0x285aS0x283fS0x2767S0x24eaS0xf94: v285aV283fV2767V24eaVf94 = SELFBALANCE 
    0x285bS0x283fS0x2767S0x24eaS0xf94: v285bV283fV2767V24eaVf94 = LT v285aV283fV2767V24eaVf94, v2847V2767V24eaVf94(0x0)
    0x285cS0x283fS0x2767S0x24eaS0xf94: v285cV283fV2767V24eaVf94 = ISZERO v285bV283fV2767V24eaVf94
    0x285dS0x283fS0x2767S0x24eaS0xf94: v285dV283fV2767V24eaVf94(0x28b1) = CONST 
    0x2860S0x283fS0x2767S0x24eaS0xf94: JUMPI v285dV283fV2767V24eaVf94(0x28b1), v285cV283fV2767V24eaVf94

    Begin block 0x2861B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2856B0x283fB0x2767B0x24eaB0xf94], succ=[]
    =================================
    0x2861S0x283fS0x2767S0x24eaS0xf94: v2861V283fV2767V24eaVf94(0x40) = CONST 
    0x2863S0x283fS0x2767S0x24eaS0xf94: v2863V283fV2767V24eaVf94 = MLOAD v2861V283fV2767V24eaVf94(0x40)
    0x2864S0x283fS0x2767S0x24eaS0xf94: v2864V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2886S0x283fS0x2767S0x24eaS0xf94: MSTORE v2863V283fV2767V24eaVf94, v2864V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2887S0x283fS0x2767S0x24eaS0xf94: v2887V283fV2767V24eaVf94(0x4) = CONST 
    0x2889S0x283fS0x2767S0x24eaS0xf94: v2889V283fV2767V24eaVf94 = ADD v2887V283fV2767V24eaVf94(0x4), v2863V283fV2767V24eaVf94
    0x288cS0x283fS0x2767S0x24eaS0xf94: v288cV283fV2767V24eaVf94(0x20) = CONST 
    0x288eS0x283fS0x2767S0x24eaS0xf94: v288eV283fV2767V24eaVf94 = ADD v288cV283fV2767V24eaVf94(0x20), v2889V283fV2767V24eaVf94
    0x2891S0x283fS0x2767S0x24eaS0xf94: v2891V283fV2767V24eaVf94(0x20) = SUB v288eV283fV2767V24eaVf94, v2889V283fV2767V24eaVf94
    0x2893S0x283fS0x2767S0x24eaS0xf94: MSTORE v2889V283fV2767V24eaVf94, v2891V283fV2767V24eaVf94(0x20)
    0x2894S0x283fS0x2767S0x24eaS0xf94: v2894V283fV2767V24eaVf94(0x26) = CONST 
    0x2897S0x283fS0x2767S0x24eaS0xf94: MSTORE v288eV283fV2767V24eaVf94, v2894V283fV2767V24eaVf94(0x26)
    0x2898S0x283fS0x2767S0x24eaS0xf94: v2898V283fV2767V24eaVf94(0x20) = CONST 
    0x289aS0x283fS0x2767S0x24eaS0xf94: v289aV283fV2767V24eaVf94 = ADD v2898V283fV2767V24eaVf94(0x20), v288eV283fV2767V24eaVf94
    0x289cS0x283fS0x2767S0x24eaS0xf94: v289cV283fV2767V24eaVf94(0x2b06) = CONST 
    0x289fS0x283fS0x2767S0x24eaS0xf94: v289fV283fV2767V24eaVf94(0x26) = CONST 
    0x28a2S0x283fS0x2767S0x24eaS0xf94: CODECOPY v289aV283fV2767V24eaVf94, v289cV283fV2767V24eaVf94(0x2b06), v289fV283fV2767V24eaVf94(0x26)
    0x28a3S0x283fS0x2767S0x24eaS0xf94: v28a3V283fV2767V24eaVf94(0x40) = CONST 
    0x28a5S0x283fS0x2767S0x24eaS0xf94: v28a5V283fV2767V24eaVf94 = ADD v28a3V283fV2767V24eaVf94(0x40), v289aV283fV2767V24eaVf94
    0x28a9S0x283fS0x2767S0x24eaS0xf94: v28a9V283fV2767V24eaVf94(0x40) = CONST 
    0x28abS0x283fS0x2767S0x24eaS0xf94: v28abV283fV2767V24eaVf94 = MLOAD v28a9V283fV2767V24eaVf94(0x40)
    0x28aeS0x283fS0x2767S0x24eaS0xf94: v28aeV283fV2767V24eaVf94(0x84) = SUB v28a5V283fV2767V24eaVf94, v28abV283fV2767V24eaVf94
    0x28b0S0x283fS0x2767S0x24eaS0xf94: REVERT v28abV283fV2767V24eaVf94, v28aeV283fV2767V24eaVf94(0x84)

    Begin block 0x28b1B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2856B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a11B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x28b2S0x283fS0x2767S0x24eaS0xf94: v28b2V283fV2767V24eaVf94(0x28ba) = CONST 
    0x28b6S0x283fS0x2767S0x24eaS0xf94: v28b6V283fV2767V24eaVf94(0x2a11) = CONST 
    0x28b9S0x283fS0x2767S0x24eaS0xf94: JUMP v28b6V283fV2767V24eaVf94(0x2a11)

    Begin block 0x2a11B0x283fB0x2767B0x24eaB0xf94
    prev=[0x28b1B0x283fB0x2767B0x24eaB0xf94], succ=[0x28baB0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a12S0x283fS0x2767S0x24eaS0xf94: v2a12V283fV2767V24eaVf94 = EXTCODESIZE v27baV24eaVf94
    0x2a13S0x283fS0x2767S0x24eaS0xf94: v2a13V283fV2767V24eaVf94 = ISZERO v2a12V283fV2767V24eaVf94
    0x2a14S0x283fS0x2767S0x24eaS0xf94: v2a14V283fV2767V24eaVf94 = ISZERO v2a13V283fV2767V24eaVf94
    0x2a16S0x283fS0x2767S0x24eaS0xf94: JUMP v28b2V283fV2767V24eaVf94(0x28ba)

    Begin block 0x28baB0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a11B0x283fB0x2767B0x24eaB0xf94], succ=[0x28bfB0x283fB0x2767B0x24eaB0xf94, 0x2925B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x28bbS0x283fS0x2767S0x24eaS0xf94: v28bbV283fV2767V24eaVf94(0x2925) = CONST 
    0x28beS0x283fS0x2767S0x24eaS0xf94: JUMPI v28bbV283fV2767V24eaVf94(0x2925), v2a14V283fV2767V24eaVf94

    Begin block 0x28bfB0x283fB0x2767B0x24eaB0xf94
    prev=[0x28baB0x283fB0x2767B0x24eaB0xf94], succ=[]
    =================================
    0x28bfS0x283fS0x2767S0x24eaS0xf94: v28bfV283fV2767V24eaVf94(0x40) = CONST 
    0x28c2S0x283fS0x2767S0x24eaS0xf94: v28c2V283fV2767V24eaVf94 = MLOAD v28bfV283fV2767V24eaVf94(0x40)
    0x28c3S0x283fS0x2767S0x24eaS0xf94: v28c3V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x28e5S0x283fS0x2767S0x24eaS0xf94: MSTORE v28c2V283fV2767V24eaVf94, v28c3V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x28e6S0x283fS0x2767S0x24eaS0xf94: v28e6V283fV2767V24eaVf94(0x20) = CONST 
    0x28e8S0x283fS0x2767S0x24eaS0xf94: v28e8V283fV2767V24eaVf94(0x4) = CONST 
    0x28ebS0x283fS0x2767S0x24eaS0xf94: v28ebV283fV2767V24eaVf94 = ADD v28c2V283fV2767V24eaVf94, v28e8V283fV2767V24eaVf94(0x4)
    0x28ecS0x283fS0x2767S0x24eaS0xf94: MSTORE v28ebV283fV2767V24eaVf94, v28e6V283fV2767V24eaVf94(0x20)
    0x28edS0x283fS0x2767S0x24eaS0xf94: v28edV283fV2767V24eaVf94(0x1d) = CONST 
    0x28efS0x283fS0x2767S0x24eaS0xf94: v28efV283fV2767V24eaVf94(0x24) = CONST 
    0x28f2S0x283fS0x2767S0x24eaS0xf94: v28f2V283fV2767V24eaVf94 = ADD v28c2V283fV2767V24eaVf94, v28efV283fV2767V24eaVf94(0x24)
    0x28f3S0x283fS0x2767S0x24eaS0xf94: MSTORE v28f2V283fV2767V24eaVf94, v28edV283fV2767V24eaVf94(0x1d)
    0x28f4S0x283fS0x2767S0x24eaS0xf94: v28f4V283fV2767V24eaVf94(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000) = CONST 
    0x2915S0x283fS0x2767S0x24eaS0xf94: v2915V283fV2767V24eaVf94(0x44) = CONST 
    0x2918S0x283fS0x2767S0x24eaS0xf94: v2918V283fV2767V24eaVf94 = ADD v28c2V283fV2767V24eaVf94, v2915V283fV2767V24eaVf94(0x44)
    0x2919S0x283fS0x2767S0x24eaS0xf94: MSTORE v2918V283fV2767V24eaVf94, v28f4V283fV2767V24eaVf94(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000)
    0x291bS0x283fS0x2767S0x24eaS0xf94: v291bV283fV2767V24eaVf94 = MLOAD v28bfV283fV2767V24eaVf94(0x40)
    0x291fS0x283fS0x2767S0x24eaS0xf94: v291fV283fV2767V24eaVf94(0x0) = SUB v28c2V283fV2767V24eaVf94, v291bV283fV2767V24eaVf94
    0x2920S0x283fS0x2767S0x24eaS0xf94: v2920V283fV2767V24eaVf94(0x64) = CONST 
    0x2922S0x283fS0x2767S0x24eaS0xf94: v2922V283fV2767V24eaVf94(0x64) = ADD v2920V283fV2767V24eaVf94(0x64), v291fV283fV2767V24eaVf94(0x0)
    0x2924S0x283fS0x2767S0x24eaS0xf94: REVERT v291bV283fV2767V24eaVf94, v2922V283fV2767V24eaVf94(0x64)

    Begin block 0x2925B0x283fB0x2767B0x24eaB0xf94
    prev=[0x28baB0x283fB0x2767B0x24eaB0xf94], succ=[0x2952B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2926S0x283fS0x2767S0x24eaS0xf94: v2926V283fV2767V24eaVf94(0x0) = CONST 
    0x2928S0x283fS0x2767S0x24eaS0xf94: v2928V283fV2767V24eaVf94(0x60) = CONST 
    0x292bS0x283fS0x2767S0x24eaS0xf94: v292bV283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2940S0x283fS0x2767S0x24eaS0xf94: v2940V283fV2767V24eaVf94 = AND v292bV283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffff), v27baV24eaVf94
    0x2943S0x283fS0x2767S0x24eaS0xf94: v2943V283fV2767V24eaVf94(0x40) = CONST 
    0x2945S0x283fS0x2767S0x24eaS0xf94: v2945V283fV2767V24eaVf94 = MLOAD v2943V283fV2767V24eaVf94(0x40)
    0x2949S0x283fS0x2767S0x24eaS0xf94: v2949V283fV2767V24eaVf94(0x44) = MLOAD v2514Vf94
    0x294bS0x283fS0x2767S0x24eaS0xf94: v294bV283fV2767V24eaVf94(0x20) = CONST 
    0x294dS0x283fS0x2767S0x24eaS0xf94: v294dV283fV2767V24eaVf94 = ADD v294bV283fV2767V24eaVf94(0x20), v2514Vf94

    Begin block 0x2952B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2925B0x283fB0x2767B0x24eaB0xf94, 0x295bB0x283fB0x2767B0x24eaB0xf94], succ=[0x298fB0x283fB0x2767B0x24eaB0xf94, 0x295bB0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2952_0x2S0x283fS0x2767S0x24eaS0xf94: v2952_2V283fV2767V24eaVf94 = PHI v2949V283fV2767V24eaVf94(0x44), v2982V283fV2767V24eaVf94
    0x2953S0x283fS0x2767S0x24eaS0xf94: v2953V283fV2767V24eaVf94(0x20) = CONST 
    0x2956S0x283fS0x2767S0x24eaS0xf94: v2956V283fV2767V24eaVf94 = LT v2952_2V283fV2767V24eaVf94, v2953V283fV2767V24eaVf94(0x20)
    0x2957S0x283fS0x2767S0x24eaS0xf94: v2957V283fV2767V24eaVf94(0x298f) = CONST 
    0x295aS0x283fS0x2767S0x24eaS0xf94: JUMPI v2957V283fV2767V24eaVf94(0x298f), v2956V283fV2767V24eaVf94

    Begin block 0x298fB0x283fB0x2767B0x24eaB0xf94
    prev=[0x2952B0x283fB0x2767B0x24eaB0xf94], succ=[0x29d0B0x283fB0x2767B0x24eaB0xf94, 0x29f1B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x298f_0x0S0x283fS0x2767S0x24eaS0xf94: v298f_0V283fV2767V24eaVf94 = PHI v294dV283fV2767V24eaVf94, v298aV283fV2767V24eaVf94
    0x298f_0x1S0x283fS0x2767S0x24eaS0xf94: v298f_1V283fV2767V24eaVf94 = PHI v2945V283fV2767V24eaVf94, v2988V283fV2767V24eaVf94
    0x298f_0x2S0x283fS0x2767S0x24eaS0xf94: v298f_2V283fV2767V24eaVf94 = PHI v2949V283fV2767V24eaVf94(0x44), v2982V283fV2767V24eaVf94
    0x2990S0x283fS0x2767S0x24eaS0xf94: v2990V283fV2767V24eaVf94(0x1) = CONST 
    0x2993S0x283fS0x2767S0x24eaS0xf94: v2993V283fV2767V24eaVf94(0x20) = CONST 
    0x2995S0x283fS0x2767S0x24eaS0xf94: v2995V283fV2767V24eaVf94 = SUB v2993V283fV2767V24eaVf94(0x20), v298f_2V283fV2767V24eaVf94
    0x2996S0x283fS0x2767S0x24eaS0xf94: v2996V283fV2767V24eaVf94(0x100) = CONST 
    0x2999S0x283fS0x2767S0x24eaS0xf94: v2999V283fV2767V24eaVf94 = EXP v2996V283fV2767V24eaVf94(0x100), v2995V283fV2767V24eaVf94
    0x299aS0x283fS0x2767S0x24eaS0xf94: v299aV283fV2767V24eaVf94 = SUB v2999V283fV2767V24eaVf94, v2990V283fV2767V24eaVf94(0x1)
    0x299cS0x283fS0x2767S0x24eaS0xf94: v299cV283fV2767V24eaVf94 = NOT v299aV283fV2767V24eaVf94
    0x299eS0x283fS0x2767S0x24eaS0xf94: v299eV283fV2767V24eaVf94 = MLOAD v298f_0V283fV2767V24eaVf94
    0x299fS0x283fS0x2767S0x24eaS0xf94: v299fV283fV2767V24eaVf94 = AND v299eV283fV2767V24eaVf94, v299cV283fV2767V24eaVf94
    0x29a2S0x283fS0x2767S0x24eaS0xf94: v29a2V283fV2767V24eaVf94 = MLOAD v298f_1V283fV2767V24eaVf94
    0x29a3S0x283fS0x2767S0x24eaS0xf94: v29a3V283fV2767V24eaVf94 = AND v29a2V283fV2767V24eaVf94, v299aV283fV2767V24eaVf94
    0x29a6S0x283fS0x2767S0x24eaS0xf94: v29a6V283fV2767V24eaVf94 = OR v299fV283fV2767V24eaVf94, v29a3V283fV2767V24eaVf94
    0x29a8S0x283fS0x2767S0x24eaS0xf94: MSTORE v298f_1V283fV2767V24eaVf94, v29a6V283fV2767V24eaVf94
    0x29b1S0x283fS0x2767S0x24eaS0xf94: v29b1V283fV2767V24eaVf94 = ADD v2949V283fV2767V24eaVf94(0x44), v2945V283fV2767V24eaVf94
    0x29b5S0x283fS0x2767S0x24eaS0xf94: v29b5V283fV2767V24eaVf94(0x0) = CONST 
    0x29b7S0x283fS0x2767S0x24eaS0xf94: v29b7V283fV2767V24eaVf94(0x40) = CONST 
    0x29b9S0x283fS0x2767S0x24eaS0xf94: v29b9V283fV2767V24eaVf94 = MLOAD v29b7V283fV2767V24eaVf94(0x40)
    0x29bcS0x283fS0x2767S0x24eaS0xf94: v29bcV283fV2767V24eaVf94(0x44) = SUB v29b1V283fV2767V24eaVf94, v29b9V283fV2767V24eaVf94
    0x29c0S0x283fS0x2767S0x24eaS0xf94: v29c0V283fV2767V24eaVf94 = GAS 
    0x29c1S0x283fS0x2767S0x24eaS0xf94: v29c1V283fV2767V24eaVf94 = CALL v29c0V283fV2767V24eaVf94, v2940V283fV2767V24eaVf94, v2847V2767V24eaVf94(0x0), v29b9V283fV2767V24eaVf94, v29bcV283fV2767V24eaVf94(0x44), v29b9V283fV2767V24eaVf94, v29b5V283fV2767V24eaVf94(0x0)
    0x29c6S0x283fS0x2767S0x24eaS0xf94: v29c6V283fV2767V24eaVf94 = RETURNDATASIZE 
    0x29c8S0x283fS0x2767S0x24eaS0xf94: v29c8V283fV2767V24eaVf94(0x0) = CONST 
    0x29cbS0x283fS0x2767S0x24eaS0xf94: v29cbV283fV2767V24eaVf94 = EQ v29c6V283fV2767V24eaVf94, v29c8V283fV2767V24eaVf94(0x0)
    0x29ccS0x283fS0x2767S0x24eaS0xf94: v29ccV283fV2767V24eaVf94(0x29f1) = CONST 
    0x29cfS0x283fS0x2767S0x24eaS0xf94: JUMPI v29ccV283fV2767V24eaVf94(0x29f1), v29cbV283fV2767V24eaVf94

    Begin block 0x29d0B0x283fB0x2767B0x24eaB0xf94
    prev=[0x298fB0x283fB0x2767B0x24eaB0xf94], succ=[0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x29d0S0x283fS0x2767S0x24eaS0xf94: v29d0V283fV2767V24eaVf94(0x40) = CONST 
    0x29d2S0x283fS0x2767S0x24eaS0xf94: v29d2V283fV2767V24eaVf94 = MLOAD v29d0V283fV2767V24eaVf94(0x40)
    0x29d5S0x283fS0x2767S0x24eaS0xf94: v29d5V283fV2767V24eaVf94(0x1f) = CONST 
    0x29d7S0x283fS0x2767S0x24eaS0xf94: v29d7V283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v29d5V283fV2767V24eaVf94(0x1f)
    0x29d8S0x283fS0x2767S0x24eaS0xf94: v29d8V283fV2767V24eaVf94(0x3f) = CONST 
    0x29daS0x283fS0x2767S0x24eaS0xf94: v29daV283fV2767V24eaVf94 = RETURNDATASIZE 
    0x29dbS0x283fS0x2767S0x24eaS0xf94: v29dbV283fV2767V24eaVf94 = ADD v29daV283fV2767V24eaVf94, v29d8V283fV2767V24eaVf94(0x3f)
    0x29dcS0x283fS0x2767S0x24eaS0xf94: v29dcV283fV2767V24eaVf94 = AND v29dbV283fV2767V24eaVf94, v29d7V283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x29deS0x283fS0x2767S0x24eaS0xf94: v29deV283fV2767V24eaVf94 = ADD v29d2V283fV2767V24eaVf94, v29dcV283fV2767V24eaVf94
    0x29dfS0x283fS0x2767S0x24eaS0xf94: v29dfV283fV2767V24eaVf94(0x40) = CONST 
    0x29e1S0x283fS0x2767S0x24eaS0xf94: MSTORE v29dfV283fV2767V24eaVf94(0x40), v29deV283fV2767V24eaVf94
    0x29e2S0x283fS0x2767S0x24eaS0xf94: v29e2V283fV2767V24eaVf94 = RETURNDATASIZE 
    0x29e4S0x283fS0x2767S0x24eaS0xf94: MSTORE v29d2V283fV2767V24eaVf94, v29e2V283fV2767V24eaVf94
    0x29e5S0x283fS0x2767S0x24eaS0xf94: v29e5V283fV2767V24eaVf94 = RETURNDATASIZE 
    0x29e6S0x283fS0x2767S0x24eaS0xf94: v29e6V283fV2767V24eaVf94(0x0) = CONST 
    0x29e8S0x283fS0x2767S0x24eaS0xf94: v29e8V283fV2767V24eaVf94(0x20) = CONST 
    0x29ebS0x283fS0x2767S0x24eaS0xf94: v29ebV283fV2767V24eaVf94 = ADD v29d2V283fV2767V24eaVf94, v29e8V283fV2767V24eaVf94(0x20)
    0x29ecS0x283fS0x2767S0x24eaS0xf94: RETURNDATACOPY v29ebV283fV2767V24eaVf94, v29e6V283fV2767V24eaVf94(0x0), v29e5V283fV2767V24eaVf94
    0x29edS0x283fS0x2767S0x24eaS0xf94: v29edV283fV2767V24eaVf94(0x29f6) = CONST 
    0x29f0S0x283fS0x2767S0x24eaS0xf94: JUMP v29edV283fV2767V24eaVf94(0x29f6)

    Begin block 0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x29d0B0x283fB0x2767B0x24eaB0xf94, 0x29f1B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x29f6_0x1S0x283fS0x2767S0x24eaS0xf94: v29f6_1V283fV2767V24eaVf94 = PHI v29d2V283fV2767V24eaVf94, v29f2V283fV2767V24eaVf94(0x60)
    0x29fcS0x283fS0x2767S0x24eaS0xf94: v29fcV283fV2767V24eaVf94(0x2a06) = CONST 
    0x2a02S0x283fS0x2767S0x24eaS0xf94: v2a02V283fV2767V24eaVf94(0x2a17) = CONST 
    0x2a05S0x283fS0x2767S0x24eaS0xf94: JUMP v2a02V283fV2767V24eaVf94(0x2a17)

    Begin block 0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a26B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x2a20B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a18S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a18V29f6V283fV2767V24eaVf94(0x60) = CONST 
    0x2a1bS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1bV29f6V283fV2767V24eaVf94 = ISZERO v29c1V283fV2767V24eaVf94
    0x2a1cS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1cV29f6V283fV2767V24eaVf94(0x2a26) = CONST 
    0x2a1fS0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMPI v2a1cV29f6V283fV2767V24eaVf94(0x2a26), v2a1bV29f6V283fV2767V24eaVf94

    Begin block 0x2a26B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a36B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x2a2eB0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a28S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a28V29f6V283fV2767V24eaVf94 = MLOAD v29f6_1V283fV2767V24eaVf94
    0x2a29S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a29V29f6V283fV2767V24eaVf94 = ISZERO v2a28V29f6V283fV2767V24eaVf94
    0x2a2aS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a2aV29f6V283fV2767V24eaVf94(0x2a36) = CONST 
    0x2a2dS0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMPI v2a2aV29f6V283fV2767V24eaVf94(0x2a36), v2a29V29f6V283fV2767V24eaVf94

    Begin block 0x2a36B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a26B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a88B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26a00x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a37S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a37V29f6V283fV2767V24eaVf94(0x40) = CONST 
    0x2a39S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a39V29f6V283fV2767V24eaVf94 = MLOAD v2a37V29f6V283fV2767V24eaVf94(0x40)
    0x2a3aS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a3aV29f6V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a5cS0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a39V29f6V283fV2767V24eaVf94, v2a3aV29f6V283fV2767V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a5dS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a5dV29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x2a5fS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a5fV29f6V283fV2767V24eaVf94(0x4) = CONST 
    0x2a62S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a62V29f6V283fV2767V24eaVf94 = ADD v2a39V29f6V283fV2767V24eaVf94, v2a5fV29f6V283fV2767V24eaVf94(0x4)
    0x2a65S0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a62V29f6V283fV2767V24eaVf94, v2a5dV29f6V283fV2767V24eaVf94(0x20)
    0x2a67S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a67V29f6V283fV2767V24eaVf94(0x20) = MLOAD v2770V24eaVf94
    0x2a68S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a68V29f6V283fV2767V24eaVf94(0x24) = CONST 
    0x2a6bS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a6bV29f6V283fV2767V24eaVf94 = ADD v2a39V29f6V283fV2767V24eaVf94, v2a68V29f6V283fV2767V24eaVf94(0x24)
    0x2a6cS0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a6bV29f6V283fV2767V24eaVf94, v2a67V29f6V283fV2767V24eaVf94(0x20)
    0x2a6eS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a6eV29f6V283fV2767V24eaVf94(0x20) = MLOAD v2770V24eaVf94
    0x2a75S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a75V29f6V283fV2767V24eaVf94(0x44) = CONST 
    0x2a77S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a77V29f6V283fV2767V24eaVf94 = ADD v2a75V29f6V283fV2767V24eaVf94(0x44), v2a39V29f6V283fV2767V24eaVf94
    0x2a7bS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a7bV29f6V283fV2767V24eaVf94 = ADD v2770V24eaVf94, v2a5dV29f6V283fV2767V24eaVf94(0x20)
    0x2a80S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a80V29f6V283fV2767V24eaVf94(0x0) = CONST 
    0x2a83S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a83V29f6V283fV2767V24eaVf94 = ISZERO v2a6eV29f6V283fV2767V24eaVf94(0x20)
    0x2a84S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a84V29f6V283fV2767V24eaVf94(0x26a0) = CONST 
    0x2a87S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMPI v2a84V29f6V283fV2767V24eaVf94(0x26a0), v2a83V29f6V283fV2767V24eaVf94

    Begin block 0x2a88B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a36B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26880x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a8aS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a8aV29f6V283fV2767V24eaVf94 = ADD v2a80V29f6V283fV2767V24eaVf94(0x0), v2a7bV29f6V283fV2767V24eaVf94
    0x2a8bS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a8bV29f6V283fV2767V24eaVf94 = MLOAD v2a8aV29f6V283fV2767V24eaVf94
    0x2a8eS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a8eV29f6V283fV2767V24eaVf94 = ADD v2a80V29f6V283fV2767V24eaVf94(0x0), v2a77V29f6V283fV2767V24eaVf94
    0x2a8fS0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a8eV29f6V283fV2767V24eaVf94, v2a8bV29f6V283fV2767V24eaVf94
    0x2a90S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a90V29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x2a92S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a92V29f6V283fV2767V24eaVf94(0x20) = ADD v2a90V29f6V283fV2767V24eaVf94(0x20), v2a80V29f6V283fV2767V24eaVf94(0x0)
    0x2a93S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a93V29f6V283fV2767V24eaVf94(0x2688) = CONST 
    0x2a96S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMP v2a93V29f6V283fV2767V24eaVf94(0x2688)

    Begin block 0x26880x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a88B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26910x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26910x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26a00x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x26880x2a17_0x0S0x29f6S0x283fS0x2767S0x24eaS0xf94: v26882a17_0V29f6V283fV2767V24eaVf94 = PHI v2a92V29f6V283fV2767V24eaVf94(0x20), v2a17269bV29f6V283fV2767V24eaVf94
    0x268b0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a17268bV29f6V283fV2767V24eaVf94 = LT v26882a17_0V29f6V283fV2767V24eaVf94, v2a6eV29f6V283fV2767V24eaVf94(0x20)
    0x268c0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a17268cV29f6V283fV2767V24eaVf94 = ISZERO v2a17268bV29f6V283fV2767V24eaVf94
    0x268d0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a17268dV29f6V283fV2767V24eaVf94(0x26a0) = CONST 
    0x26900x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMPI v2a17268dV29f6V283fV2767V24eaVf94(0x26a0), v2a17268cV29f6V283fV2767V24eaVf94

    Begin block 0x26910x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x26880x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26880x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x26910x2a17_0x0S0x29f6S0x283fS0x2767S0x24eaS0xf94: v26912a17_0V29f6V283fV2767V24eaVf94 = PHI v2a92V29f6V283fV2767V24eaVf94(0x20), v2a17269bV29f6V283fV2767V24eaVf94
    0x26930x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a172693V29f6V283fV2767V24eaVf94 = ADD v26912a17_0V29f6V283fV2767V24eaVf94, v2a7bV29f6V283fV2767V24eaVf94
    0x26940x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a172694V29f6V283fV2767V24eaVf94 = MLOAD v2a172693V29f6V283fV2767V24eaVf94
    0x26970x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a172697V29f6V283fV2767V24eaVf94 = ADD v26912a17_0V29f6V283fV2767V24eaVf94, v2a77V29f6V283fV2767V24eaVf94
    0x26980x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a172697V29f6V283fV2767V24eaVf94, v2a172694V29f6V283fV2767V24eaVf94
    0x26990x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a172699V29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x269b0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a17269bV29f6V283fV2767V24eaVf94 = ADD v2a172699V29f6V283fV2767V24eaVf94(0x20), v26912a17_0V29f6V283fV2767V24eaVf94
    0x269c0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a17269cV29f6V283fV2767V24eaVf94(0x2688) = CONST 
    0x269f0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMP v2a17269cV29f6V283fV2767V24eaVf94(0x2688)

    Begin block 0x26a00x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a36B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26880x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26b40x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26cd0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x26a90x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726a9V29f6V283fV2767V24eaVf94 = ADD v2a6eV29f6V283fV2767V24eaVf94(0x20), v2a77V29f6V283fV2767V24eaVf94
    0x26ab0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726abV29f6V283fV2767V24eaVf94(0x1f) = CONST 
    0x26ad0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726adV29f6V283fV2767V24eaVf94(0x0) = AND v2a1726abV29f6V283fV2767V24eaVf94(0x1f), v2a6eV29f6V283fV2767V24eaVf94(0x20)
    0x26af0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726afV29f6V283fV2767V24eaVf94 = ISZERO v2a1726adV29f6V283fV2767V24eaVf94(0x0)
    0x26b00x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726b0V29f6V283fV2767V24eaVf94(0x26cd) = CONST 
    0x26b30x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMPI v2a1726b0V29f6V283fV2767V24eaVf94(0x26cd), v2a1726afV29f6V283fV2767V24eaVf94

    Begin block 0x26b40x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x26a00x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26cd0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x26b60x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726b6V29f6V283fV2767V24eaVf94 = SUB v2a1726a9V29f6V283fV2767V24eaVf94, v2a1726adV29f6V283fV2767V24eaVf94(0x0)
    0x26b80x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726b8V29f6V283fV2767V24eaVf94 = MLOAD v2a1726b6V29f6V283fV2767V24eaVf94
    0x26b90x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726b9V29f6V283fV2767V24eaVf94(0x1) = CONST 
    0x26bc0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726bcV29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x26be0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726beV29f6V283fV2767V24eaVf94(0x20) = SUB v2a1726bcV29f6V283fV2767V24eaVf94(0x20), v2a1726adV29f6V283fV2767V24eaVf94(0x0)
    0x26bf0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726bfV29f6V283fV2767V24eaVf94(0x100) = CONST 
    0x26c20x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726c2V29f6V283fV2767V24eaVf94(0x1) = EXP v2a1726bfV29f6V283fV2767V24eaVf94(0x100), v2a1726beV29f6V283fV2767V24eaVf94(0x20)
    0x26c30x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726c3V29f6V283fV2767V24eaVf94(0x0) = SUB v2a1726c2V29f6V283fV2767V24eaVf94(0x1), v2a1726b9V29f6V283fV2767V24eaVf94(0x1)
    0x26c40x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726c4V29f6V283fV2767V24eaVf94 = NOT v2a1726c3V29f6V283fV2767V24eaVf94(0x0)
    0x26c50x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726c5V29f6V283fV2767V24eaVf94 = AND v2a1726c4V29f6V283fV2767V24eaVf94, v2a1726b8V29f6V283fV2767V24eaVf94
    0x26c70x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: MSTORE v2a1726b6V29f6V283fV2767V24eaVf94, v2a1726c5V29f6V283fV2767V24eaVf94
    0x26c80x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726c8V29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x26ca0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726caV29f6V283fV2767V24eaVf94 = ADD v2a1726c8V29f6V283fV2767V24eaVf94(0x20), v2a1726b6V29f6V283fV2767V24eaVf94

    Begin block 0x26cd0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x26a00x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94, 0x26b40x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[]
    =================================
    0x26cd0x2a17_0x1S0x29f6S0x283fS0x2767S0x24eaS0xf94: v26cd2a17_1V29f6V283fV2767V24eaVf94 = PHI v2a1726a9V29f6V283fV2767V24eaVf94, v2a1726caV29f6V283fV2767V24eaVf94
    0x26d30x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726d3V29f6V283fV2767V24eaVf94(0x40) = CONST 
    0x26d50x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726d5V29f6V283fV2767V24eaVf94 = MLOAD v2a1726d3V29f6V283fV2767V24eaVf94(0x40)
    0x26d80x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a1726d8V29f6V283fV2767V24eaVf94 = SUB v26cd2a17_1V29f6V283fV2767V24eaVf94, v2a1726d5V29f6V283fV2767V24eaVf94
    0x26da0x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: REVERT v2a1726d5V29f6V283fV2767V24eaVf94, v2a1726d8V29f6V283fV2767V24eaVf94

    Begin block 0x2a2eB0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a26B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[]
    =================================
    0x2a2fS0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a2fV29f6V283fV2767V24eaVf94 = MLOAD v29f6_1V283fV2767V24eaVf94
    0x2a32S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a32V29f6V283fV2767V24eaVf94(0x20) = CONST 
    0x2a34S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a34V29f6V283fV2767V24eaVf94 = ADD v2a32V29f6V283fV2767V24eaVf94(0x20), v29f6_1V283fV2767V24eaVf94
    0x2a35S0x29f6S0x283fS0x2767S0x24eaS0xf94: REVERT v2a34V29f6V283fV2767V24eaVf94, v2a2fV29f6V283fV2767V24eaVf94

    Begin block 0x2a20B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x26e10x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x2a22S0x29f6S0x283fS0x2767S0x24eaS0xf94: v2a22V29f6V283fV2767V24eaVf94(0x26e1) = CONST 
    0x2a25S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMP v2a22V29f6V283fV2767V24eaVf94(0x26e1)

    Begin block 0x26e10x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94
    prev=[0x2a20B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x2a06B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x26e70x2a17S0x29f6S0x283fS0x2767S0x24eaS0xf94: JUMP v29fcV283fV2767V24eaVf94(0x2a06)

    Begin block 0x2a06B0x283fB0x2767B0x24eaB0xf94
    prev=[0x26e10x2a17B0x29f6B0x283fB0x2767B0x24eaB0xf94], succ=[0x284eB0x2767B0x24eaB0xf94]
    =================================
    0x2a10S0x283fS0x2767S0x24eaS0xf94: JUMP v2842V2767V24eaVf94(0x284e)

    Begin block 0x284eB0x2767B0x24eaB0xf94
    prev=[0x2a06B0x283fB0x2767B0x24eaB0xf94], succ=[0x27c9B0x24eaB0xf94]
    =================================
    0x2855S0x2767S0x24eaS0xf94: JUMP v276aV24eaVf94(0x27c9)

    Begin block 0x27c9B0x24eaB0xf94
    prev=[0x284eB0x2767B0x24eaB0xf94], succ=[0x3918B0x24eaB0xf94, 0x27d4B0x24eaB0xf94]
    =================================
    0x27cbS0x24eaS0xf94: v27cbV24eaVf94 = MLOAD v29f6_1V283fV2767V24eaVf94
    0x27cfS0x24eaS0xf94: v27cfV24eaVf94 = ISZERO v27cbV24eaVf94
    0x27d0S0x24eaS0xf94: v27d0V24eaVf94(0x3918) = CONST 
    0x27d3S0x24eaS0xf94: JUMPI v27d0V24eaVf94(0x3918), v27cfV24eaVf94

    Begin block 0x3918B0x24eaB0xf94
    prev=[0x27c9B0x24eaB0xf94], succ=[0x38f4B0xf94]
    =================================
    0x391cS0x24eaS0xf94: JUMP v256dVf94(0x38f4)

    Begin block 0x38f4B0xf94
    prev=[0x3918B0x24eaB0xf94, 0x393cB0x24eaB0xf94], succ=[0x3741]
    =================================
    0x38f8S0xf94: JUMP vf95(0x3741)

    Begin block 0x3741
    prev=[0x38f4B0xf94], succ=[0x32c5]
    =================================
    0x3745: JUMP v581(0x32c5)

    Begin block 0x32c5
    prev=[0x3741], succ=[]
    =================================
    0x32c6: STOP 

    Begin block 0x27d4B0x24eaB0xf94
    prev=[0x27c9B0x24eaB0xf94], succ=[0x27e4B0x24eaB0xf94, 0x27e8B0x24eaB0xf94]
    =================================
    0x27d6S0x24eaS0xf94: v27d6V24eaVf94(0x20) = CONST 
    0x27d8S0x24eaS0xf94: v27d8V24eaVf94 = ADD v27d6V24eaVf94(0x20), v29f6_1V283fV2767V24eaVf94
    0x27daS0x24eaS0xf94: v27daV24eaVf94 = MLOAD v29f6_1V283fV2767V24eaVf94
    0x27dbS0x24eaS0xf94: v27dbV24eaVf94(0x20) = CONST 
    0x27deS0x24eaS0xf94: v27deV24eaVf94 = LT v27daV24eaVf94, v27dbV24eaVf94(0x20)
    0x27dfS0x24eaS0xf94: v27dfV24eaVf94 = ISZERO v27deV24eaVf94
    0x27e0S0x24eaS0xf94: v27e0V24eaVf94(0x27e8) = CONST 
    0x27e3S0x24eaS0xf94: JUMPI v27e0V24eaVf94(0x27e8), v27dfV24eaVf94

    Begin block 0x27e4B0x24eaB0xf94
    prev=[0x27d4B0x24eaB0xf94], succ=[]
    =================================
    0x27e4S0x24eaS0xf94: v27e4V24eaVf94(0x0) = CONST 
    0x27e7S0x24eaS0xf94: REVERT v27e4V24eaVf94(0x0), v27e4V24eaVf94(0x0)

    Begin block 0x27e8B0x24eaB0xf94
    prev=[0x27d4B0x24eaB0xf94], succ=[0x27efB0x24eaB0xf94, 0x393cB0x24eaB0xf94]
    =================================
    0x27eaS0x24eaS0xf94: v27eaV24eaVf94 = MLOAD v27d8V24eaVf94
    0x27ebS0x24eaS0xf94: v27ebV24eaVf94(0x393c) = CONST 
    0x27eeS0x24eaS0xf94: JUMPI v27ebV24eaVf94(0x393c), v27eaV24eaVf94

    Begin block 0x27efB0x24eaB0xf94
    prev=[0x27e8B0x24eaB0xf94], succ=[]
    =================================
    0x27efS0x24eaS0xf94: v27efV24eaVf94(0x40) = CONST 
    0x27f1S0x24eaS0xf94: v27f1V24eaVf94 = MLOAD v27efV24eaVf94(0x40)
    0x27f2S0x24eaS0xf94: v27f2V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2814S0x24eaS0xf94: MSTORE v27f1V24eaVf94, v27f2V24eaVf94(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2815S0x24eaS0xf94: v2815V24eaVf94(0x4) = CONST 
    0x2817S0x24eaS0xf94: v2817V24eaVf94 = ADD v2815V24eaVf94(0x4), v27f1V24eaVf94
    0x281aS0x24eaS0xf94: v281aV24eaVf94(0x20) = CONST 
    0x281cS0x24eaS0xf94: v281cV24eaVf94 = ADD v281aV24eaVf94(0x20), v2817V24eaVf94
    0x281fS0x24eaS0xf94: v281fV24eaVf94(0x20) = SUB v281cV24eaVf94, v2817V24eaVf94
    0x2821S0x24eaS0xf94: MSTORE v2817V24eaVf94, v281fV24eaVf94(0x20)
    0x2822S0x24eaS0xf94: v2822V24eaVf94(0x2a) = CONST 
    0x2825S0x24eaS0xf94: MSTORE v281cV24eaVf94, v2822V24eaVf94(0x2a)
    0x2826S0x24eaS0xf94: v2826V24eaVf94(0x20) = CONST 
    0x2828S0x24eaS0xf94: v2828V24eaVf94 = ADD v2826V24eaVf94(0x20), v281cV24eaVf94
    0x282aS0x24eaS0xf94: v282aV24eaVf94(0x2d01) = CONST 
    0x282dS0x24eaS0xf94: v282dV24eaVf94(0x2a) = CONST 
    0x2830S0x24eaS0xf94: CODECOPY v2828V24eaVf94, v282aV24eaVf94(0x2d01), v282dV24eaVf94(0x2a)
    0x2831S0x24eaS0xf94: v2831V24eaVf94(0x40) = CONST 
    0x2833S0x24eaS0xf94: v2833V24eaVf94 = ADD v2831V24eaVf94(0x40), v2828V24eaVf94
    0x2837S0x24eaS0xf94: v2837V24eaVf94(0x40) = CONST 
    0x2839S0x24eaS0xf94: v2839V24eaVf94 = MLOAD v2837V24eaVf94(0x40)
    0x283cS0x24eaS0xf94: v283cV24eaVf94(0x84) = SUB v2833V24eaVf94, v2839V24eaVf94
    0x283eS0x24eaS0xf94: REVERT v2839V24eaVf94, v283cV24eaVf94(0x84)

    Begin block 0x393cB0x24eaB0xf94
    prev=[0x27e8B0x24eaB0xf94], succ=[0x38f4B0xf94]
    =================================
    0x3940S0x24eaS0xf94: JUMP v256dVf94(0x38f4)

    Begin block 0x29f1B0x283fB0x2767B0x24eaB0xf94
    prev=[0x298fB0x283fB0x2767B0x24eaB0xf94], succ=[0x29f6B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x29f2S0x283fS0x2767S0x24eaS0xf94: v29f2V283fV2767V24eaVf94(0x60) = CONST 

    Begin block 0x295bB0x283fB0x2767B0x24eaB0xf94
    prev=[0x2952B0x283fB0x2767B0x24eaB0xf94], succ=[0x2952B0x283fB0x2767B0x24eaB0xf94]
    =================================
    0x295b_0x0S0x283fS0x2767S0x24eaS0xf94: v295b_0V283fV2767V24eaVf94 = PHI v294dV283fV2767V24eaVf94, v298aV283fV2767V24eaVf94
    0x295b_0x1S0x283fS0x2767S0x24eaS0xf94: v295b_1V283fV2767V24eaVf94 = PHI v2945V283fV2767V24eaVf94, v2988V283fV2767V24eaVf94
    0x295b_0x2S0x283fS0x2767S0x24eaS0xf94: v295b_2V283fV2767V24eaVf94 = PHI v2949V283fV2767V24eaVf94(0x44), v2982V283fV2767V24eaVf94
    0x295cS0x283fS0x2767S0x24eaS0xf94: v295cV283fV2767V24eaVf94 = MLOAD v295b_0V283fV2767V24eaVf94
    0x295eS0x283fS0x2767S0x24eaS0xf94: MSTORE v295b_1V283fV2767V24eaVf94, v295cV283fV2767V24eaVf94
    0x295fS0x283fS0x2767S0x24eaS0xf94: v295fV283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = CONST 
    0x2982S0x283fS0x2767S0x24eaS0xf94: v2982V283fV2767V24eaVf94 = ADD v295b_2V283fV2767V24eaVf94, v295fV283fV2767V24eaVf94(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2984S0x283fS0x2767S0x24eaS0xf94: v2984V283fV2767V24eaVf94(0x20) = CONST 
    0x2988S0x283fS0x2767S0x24eaS0xf94: v2988V283fV2767V24eaVf94 = ADD v2984V283fV2767V24eaVf94(0x20), v295b_1V283fV2767V24eaVf94
    0x298aS0x283fS0x2767S0x24eaS0xf94: v298aV283fV2767V24eaVf94 = ADD v2984V283fV2767V24eaVf94(0x20), v295b_0V283fV2767V24eaVf94
    0x298bS0x283fS0x2767S0x24eaS0xf94: v298bV283fV2767V24eaVf94(0x2952) = CONST 
    0x298eS0x283fS0x2767S0x24eaS0xf94: JUMP v298bV283fV2767V24eaVf94(0x2952)

}

function operator()() public {
    Begin block 0x5c3
    prev=[], succ=[0xfba]
    =================================
    0x5c4: v5c4(0x32e6) = CONST 
    0x5c7: v5c7(0xfba) = CONST 
    0x5ca: JUMP v5c7(0xfba)

    Begin block 0xfba
    prev=[0x5c3], succ=[0x32e6]
    =================================
    0xfbb: vfbb(0x1) = CONST 
    0xfbd: vfbd = SLOAD vfbb(0x1)
    0xfbe: vfbe(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfd3: vfd3 = AND vfbe(0xffffffffffffffffffffffffffffffffffffffff), vfbd
    0xfd5: JUMP v5c4(0x32e6)

    Begin block 0x32e6
    prev=[0xfba], succ=[]
    =================================
    0x32e7: v32e7(0x40) = CONST 
    0x32ea: v32ea = MLOAD v32e7(0x40)
    0x32eb: v32eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3302: v3302 = AND vfd3, v32eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x3304: MSTORE v32ea, v3302
    0x3305: v3305 = MLOAD v32e7(0x40)
    0x3309: v3309(0x0) = SUB v32ea, v3305
    0x330a: v330a(0x20) = CONST 
    0x330c: v330c(0x20) = ADD v330a(0x20), v3309(0x0)
    0x330e: RETURN v3305, v330c(0x20)

}

function treasury()() public {
    Begin block 0x5cb
    prev=[], succ=[0xfd6]
    =================================
    0x5cc: v5cc(0x332e) = CONST 
    0x5cf: v5cf(0xfd6) = CONST 
    0x5d2: JUMP v5cf(0xfd6)

    Begin block 0xfd6
    prev=[0x5cb], succ=[0x332e]
    =================================
    0xfd7: vfd7(0x3) = CONST 
    0xfd9: vfd9 = SLOAD vfd7(0x3)
    0xfda: vfda(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xfef: vfef = AND vfda(0xffffffffffffffffffffffffffffffffffffffff), vfd9
    0xff1: JUMP v5cc(0x332e)

    Begin block 0x332e
    prev=[0xfd6], succ=[]
    =================================
    0x332f: v332f(0x40) = CONST 
    0x3332: v3332 = MLOAD v332f(0x40)
    0x3333: v3333(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x334a: v334a = AND vfef, v3333(0xffffffffffffffffffffffffffffffffffffffff)
    0x334c: MSTORE v3332, v334a
    0x334d: v334d = MLOAD v332f(0x40)
    0x3351: v3351(0x0) = SUB v3332, v334d
    0x3352: v3352(0x20) = CONST 
    0x3354: v3354(0x20) = ADD v3352(0x20), v3351(0x0)
    0x3356: RETURN v334d, v3354(0x20)

}

function purchasedEpochs(address,uint256)() public {
    Begin block 0x5d3
    prev=[], succ=[0x5e5, 0x5e9]
    =================================
    0x5d4: v5d4(0x3376) = CONST 
    0x5d7: v5d7(0x4) = CONST 
    0x5da: v5da = CALLDATASIZE 
    0x5db: v5db = SUB v5da, v5d7(0x4)
    0x5dc: v5dc(0x40) = CONST 
    0x5df: v5df = LT v5db, v5dc(0x40)
    0x5e0: v5e0 = ISZERO v5df
    0x5e1: v5e1(0x5e9) = CONST 
    0x5e4: JUMPI v5e1(0x5e9), v5e0

    Begin block 0x5e5
    prev=[0x5d3], succ=[]
    =================================
    0x5e5: v5e5(0x0) = CONST 
    0x5e8: REVERT v5e5(0x0), v5e5(0x0)

    Begin block 0x5e9
    prev=[0x5d3], succ=[0xff2]
    =================================
    0x5eb: v5eb(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x601: v601 = CALLDATALOAD v5d7(0x4)
    0x602: v602 = AND v601, v5eb(0xffffffffffffffffffffffffffffffffffffffff)
    0x604: v604(0x20) = CONST 
    0x606: v606(0x24) = ADD v604(0x20), v5d7(0x4)
    0x607: v607 = CALLDATALOAD v606(0x24)
    0x608: v608(0xff2) = CONST 
    0x60b: JUMP v608(0xff2)

    Begin block 0xff2
    prev=[0x5e9], succ=[0x100a, 0x100b]
    =================================
    0xff3: vff3(0xf) = CONST 
    0xff5: vff5(0x20) = CONST 
    0xff7: MSTORE vff5(0x20), vff3(0xf)
    0xff9: vff9(0x0) = CONST 
    0xffb: MSTORE vff9(0x0), v602
    0xffc: vffc(0x40) = CONST 
    0xffe: vffe(0x0) = CONST 
    0x1000: v1000 = SHA3 vffe(0x0), vffc(0x40)
    0x1003: v1003 = SLOAD v1000
    0x1005: v1005 = LT v607, v1003
    0x1006: v1006(0x100b) = CONST 
    0x1009: JUMPI v1006(0x100b), v1005

    Begin block 0x100a
    prev=[0xff2], succ=[]
    =================================
    0x100a: THROW 

    Begin block 0x100b
    prev=[0xff2], succ=[0x3376]
    =================================
    0x100d: v100d(0x0) = CONST 
    0x100f: MSTORE v100d(0x0), v1000
    0x1010: v1010(0x20) = CONST 
    0x1012: v1012(0x0) = CONST 
    0x1014: v1014 = SHA3 v1012(0x0), v1010(0x20)
    0x1015: v1015 = ADD v1014, v607
    0x1016: v1016(0x0) = CONST 
    0x101d: v101d = SLOAD v1015
    0x101f: JUMP v5d4(0x3376)

    Begin block 0x3376
    prev=[0x100b], succ=[]
    =================================
    0x3377: v3377(0x40) = CONST 
    0x337a: v337a = MLOAD v3377(0x40)
    0x337d: MSTORE v337a, v101d
    0x337e: v337e = MLOAD v3377(0x40)
    0x3382: v3382(0x0) = SUB v337a, v337e
    0x3383: v3383(0x20) = CONST 
    0x3385: v3385(0x20) = ADD v3383(0x20), v3382(0x0)
    0x3387: RETURN v337e, v3385(0x20)

}

function issueNewBond(uint256)() public {
    Begin block 0x60c
    prev=[], succ=[0x61e, 0x622]
    =================================
    0x60d: v60d(0x33a7) = CONST 
    0x610: v610(0x4) = CONST 
    0x613: v613 = CALLDATASIZE 
    0x614: v614 = SUB v613, v610(0x4)
    0x615: v615(0x20) = CONST 
    0x618: v618 = LT v614, v615(0x20)
    0x619: v619 = ISZERO v618
    0x61a: v61a(0x622) = CONST 
    0x61d: JUMPI v61a(0x622), v619

    Begin block 0x61e
    prev=[0x60c], succ=[]
    =================================
    0x61e: v61e(0x0) = CONST 
    0x621: REVERT v61e(0x0), v61e(0x0)

    Begin block 0x622
    prev=[0x60c], succ=[0x1020]
    =================================
    0x624: v624 = CALLDATALOAD v610(0x4)
    0x625: v625(0x1020) = CONST 
    0x628: JUMP v625(0x1020)

    Begin block 0x1020
    prev=[0x622], succ=[0x105d, 0x1041]
    =================================
    0x1021: v1021(0x3) = CONST 
    0x1023: v1023 = SLOAD v1021(0x3)
    0x1024: v1024(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1039: v1039 = AND v1024(0xffffffffffffffffffffffffffffffffffffffff), v1023
    0x103a: v103a = CALLER 
    0x103b: v103b = EQ v103a, v1039
    0x103d: v103d(0x105d) = CONST 
    0x1040: JUMPI v103d(0x105d), v103b

    Begin block 0x105d
    prev=[0x1020, 0x1041], succ=[0x1062, 0x10b2]
    =================================
    0x105d_0x0: v105d_0 = PHI v103b, v105c
    0x105e: v105e(0x10b2) = CONST 
    0x1061: JUMPI v105e(0x10b2), v105d_0

    Begin block 0x1062
    prev=[0x105d], succ=[]
    =================================
    0x1062: v1062(0x40) = CONST 
    0x1064: v1064 = MLOAD v1062(0x40)
    0x1065: v1065(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1087: MSTORE v1064, v1065(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1088: v1088(0x4) = CONST 
    0x108a: v108a = ADD v1088(0x4), v1064
    0x108d: v108d(0x20) = CONST 
    0x108f: v108f = ADD v108d(0x20), v108a
    0x1092: v1092(0x20) = SUB v108f, v108a
    0x1094: MSTORE v108a, v1092(0x20)
    0x1095: v1095(0x33) = CONST 
    0x1098: MSTORE v108f, v1095(0x33)
    0x1099: v1099(0x20) = CONST 
    0x109b: v109b = ADD v1099(0x20), v108f
    0x109d: v109d(0x2c42) = CONST 
    0x10a0: v10a0(0x33) = CONST 
    0x10a3: CODECOPY v109b, v109d(0x2c42), v10a0(0x33)
    0x10a4: v10a4(0x40) = CONST 
    0x10a6: v10a6 = ADD v10a4(0x40), v109b
    0x10aa: v10aa(0x40) = CONST 
    0x10ac: v10ac = MLOAD v10aa(0x40)
    0x10af: v10af(0x84) = SUB v10a6, v10ac
    0x10b1: REVERT v10ac, v10af(0x84)

    Begin block 0x10b2
    prev=[0x105d], succ=[0x10bf]
    =================================
    0x10b3: v10b3(0x6) = CONST 
    0x10b5: v10b5 = SLOAD v10b3(0x6)
    0x10b6: v10b6(0x10bf) = CONST 
    0x10bb: v10bb(0x2476) = CONST 
    0x10be: v10be_0 = CALLPRIVATE v10bb(0x2476), v624, v10b5, v10b6(0x10bf)

    Begin block 0x10bf
    prev=[0x10b2], succ=[0x33a7]
    =================================
    0x10c0: v10c0(0x6) = CONST 
    0x10c2: SSTORE v10c0(0x6), v10be_0
    0x10c4: JUMP v60d(0x33a7)

    Begin block 0x33a7
    prev=[0x10bf], succ=[]
    =================================
    0x33a8: STOP 

    Begin block 0x1041
    prev=[0x1020], succ=[0x105d]
    =================================
    0x1042: v1042(0x1) = CONST 
    0x1044: v1044 = SLOAD v1042(0x1)
    0x1045: v1045(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x105a: v105a = AND v1045(0xffffffffffffffffffffffffffffffffffffffff), v1044
    0x105b: v105b = CALLER 
    0x105c: v105c = EQ v105b, v105a

}

function buyCoupons(uint256,uint256)() public {
    Begin block 0x629
    prev=[], succ=[0x63b, 0x63f]
    =================================
    0x62a: v62a(0x330) = CONST 
    0x62d: v62d(0x4) = CONST 
    0x630: v630 = CALLDATASIZE 
    0x631: v631 = SUB v630, v62d(0x4)
    0x632: v632(0x40) = CONST 
    0x635: v635 = LT v631, v632(0x40)
    0x636: v636 = ISZERO v635
    0x637: v637(0x63f) = CONST 
    0x63a: JUMPI v637(0x63f), v636

    Begin block 0x63b
    prev=[0x629], succ=[]
    =================================
    0x63b: v63b(0x0) = CONST 
    0x63e: REVERT v63b(0x0), v63b(0x0)

    Begin block 0x63f
    prev=[0x629], succ=[0x10c5]
    =================================
    0x642: v642 = CALLDATALOAD v62d(0x4)
    0x644: v644(0x20) = CONST 
    0x646: v646(0x24) = ADD v644(0x20), v62d(0x4)
    0x647: v647 = CALLDATALOAD v646(0x24)
    0x648: v648(0x10c5) = CONST 
    0x64b: JUMP v648(0x10c5)

    Begin block 0x10c5
    prev=[0x63f], succ=[0x2577B0x10c5]
    =================================
    0x10c6: v10c6(0x10cd) = CONST 
    0x10c9: v10c9(0x2577) = CONST 
    0x10cc: JUMP v10c9(0x2577)

    Begin block 0x2577B0x10c5
    prev=[0x10c5], succ=[0x10cd]
    =================================
    0x2578S0x10c5: v2578V10c5 = NUMBER 
    0x2579S0x10c5: v2579V10c5(0x0) = CONST 
    0x257dS0x10c5: MSTORE v2579V10c5(0x0), v2578V10c5
    0x257eS0x10c5: v257eV10c5(0x20) = CONST 
    0x2582S0x10c5: MSTORE v257eV10c5(0x20), v2579V10c5(0x0)
    0x2583S0x10c5: v2583V10c5(0x40) = CONST 
    0x2587S0x10c5: v2587V10c5 = SHA3 v2579V10c5(0x0), v2583V10c5(0x40)
    0x2588S0x10c5: v2588V10c5 = ORIGIN 
    0x258aS0x10c5: MSTORE v2579V10c5(0x0), v2588V10c5
    0x258dS0x10c5: MSTORE v257eV10c5(0x20), v2587V10c5
    0x258fS0x10c5: v258fV10c5 = SHA3 v2579V10c5(0x0), v2583V10c5(0x40)
    0x2590S0x10c5: v2590V10c5 = SLOAD v258fV10c5
    0x2591S0x10c5: v2591V10c5(0xff) = CONST 
    0x2593S0x10c5: v2593V10c5 = AND v2591V10c5(0xff), v2590V10c5
    0x2595S0x10c5: JUMP v10c6(0x10cd)

    Begin block 0x10cd
    prev=[0x2577B0x10c5], succ=[0x10d3, 0x1123]
    =================================
    0x10ce: v10ce = ISZERO v2593V10c5
    0x10cf: v10cf(0x1123) = CONST 
    0x10d2: JUMPI v10cf(0x1123), v10ce

    Begin block 0x10d3
    prev=[0x10cd], succ=[]
    =================================
    0x10d3: v10d3(0x40) = CONST 
    0x10d5: v10d5 = MLOAD v10d3(0x40)
    0x10d6: v10d6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x10f8: MSTORE v10d5, v10d6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x10f9: v10f9(0x4) = CONST 
    0x10fb: v10fb = ADD v10f9(0x4), v10d5
    0x10fe: v10fe(0x20) = CONST 
    0x1100: v1100 = ADD v10fe(0x20), v10fb
    0x1103: v1103(0x20) = SUB v1100, v10fb
    0x1105: MSTORE v10fb, v1103(0x20)
    0x1106: v1106(0x26) = CONST 
    0x1109: MSTORE v1100, v1106(0x26)
    0x110a: v110a(0x20) = CONST 
    0x110c: v110c = ADD v110a(0x20), v1100
    0x110e: v110e(0x2d2b) = CONST 
    0x1111: v1111(0x26) = CONST 
    0x1114: CODECOPY v110c, v110e(0x2d2b), v1111(0x26)
    0x1115: v1115(0x40) = CONST 
    0x1117: v1117 = ADD v1115(0x40), v110c
    0x111b: v111b(0x40) = CONST 
    0x111d: v111d = MLOAD v111b(0x40)
    0x1120: v1120(0x84) = SUB v1117, v111d
    0x1122: REVERT v111d, v1120(0x84)

    Begin block 0x1123
    prev=[0x10cd], succ=[0x2596B0x1123]
    =================================
    0x1124: v1124(0x112b) = CONST 
    0x1127: v1127(0x2596) = CONST 
    0x112a: JUMP v1127(0x2596)

    Begin block 0x2596B0x1123
    prev=[0x1123], succ=[0x112b]
    =================================
    0x2597S0x1123: v2597V1123 = NUMBER 
    0x2598S0x1123: v2598V1123(0x0) = CONST 
    0x259cS0x1123: MSTORE v2598V1123(0x0), v2597V1123
    0x259dS0x1123: v259dV1123(0x20) = CONST 
    0x25a1S0x1123: MSTORE v259dV1123(0x20), v2598V1123(0x0)
    0x25a2S0x1123: v25a2V1123(0x40) = CONST 
    0x25a6S0x1123: v25a6V1123 = SHA3 v2598V1123(0x0), v25a2V1123(0x40)
    0x25a7S0x1123: v25a7V1123 = CALLER 
    0x25a9S0x1123: MSTORE v2598V1123(0x0), v25a7V1123
    0x25acS0x1123: MSTORE v259dV1123(0x20), v25a6V1123
    0x25aeS0x1123: v25aeV1123 = SHA3 v2598V1123(0x0), v25a2V1123(0x40)
    0x25afS0x1123: v25afV1123 = SLOAD v25aeV1123
    0x25b0S0x1123: v25b0V1123(0xff) = CONST 
    0x25b2S0x1123: v25b2V1123 = AND v25b0V1123(0xff), v25afV1123
    0x25b4S0x1123: JUMP v1124(0x112b)

    Begin block 0x112b
    prev=[0x2596B0x1123], succ=[0x1131, 0x1181]
    =================================
    0x112c: v112c = ISZERO v25b2V1123
    0x112d: v112d(0x1181) = CONST 
    0x1130: JUMPI v112d(0x1181), v112c

    Begin block 0x1131
    prev=[0x112b], succ=[]
    =================================
    0x1131: v1131(0x40) = CONST 
    0x1133: v1133 = MLOAD v1131(0x40)
    0x1134: v1134(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1156: MSTORE v1133, v1134(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1157: v1157(0x4) = CONST 
    0x1159: v1159 = ADD v1157(0x4), v1133
    0x115c: v115c(0x20) = CONST 
    0x115e: v115e = ADD v115c(0x20), v1159
    0x1161: v1161(0x20) = SUB v115e, v1159
    0x1163: MSTORE v1159, v1161(0x20)
    0x1164: v1164(0x26) = CONST 
    0x1167: MSTORE v115e, v1164(0x26)
    0x1168: v1168(0x20) = CONST 
    0x116a: v116a = ADD v1168(0x20), v115e
    0x116c: v116c(0x2d2b) = CONST 
    0x116f: v116f(0x26) = CONST 
    0x1172: CODECOPY v116a, v116c(0x2d2b), v116f(0x26)
    0x1173: v1173(0x40) = CONST 
    0x1175: v1175 = ADD v1173(0x40), v116a
    0x1179: v1179(0x40) = CONST 
    0x117b: v117b = MLOAD v1179(0x40)
    0x117e: v117e(0x84) = SUB v1175, v117b
    0x1180: REVERT v117b, v117e(0x84)

    Begin block 0x1181
    prev=[0x112b], succ=[0x118a, 0x11da]
    =================================
    0x1182: v1182(0x0) = CONST 
    0x1185: v1185 = GT v642, v1182(0x0)
    0x1186: v1186(0x11da) = CONST 
    0x1189: JUMPI v1186(0x11da), v1185

    Begin block 0x118a
    prev=[0x1181], succ=[]
    =================================
    0x118a: v118a(0x40) = CONST 
    0x118c: v118c = MLOAD v118a(0x40)
    0x118d: v118d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x11af: MSTORE v118c, v118d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x11b0: v11b0(0x4) = CONST 
    0x11b2: v11b2 = ADD v11b0(0x4), v118c
    0x11b5: v11b5(0x20) = CONST 
    0x11b7: v11b7 = ADD v11b5(0x20), v11b2
    0x11ba: v11ba(0x20) = SUB v11b7, v11b2
    0x11bc: MSTORE v11b2, v11ba(0x20)
    0x11bd: v11bd(0x34) = CONST 
    0x11c0: MSTORE v11b7, v11bd(0x34)
    0x11c1: v11c1(0x20) = CONST 
    0x11c3: v11c3 = ADD v11c1(0x20), v11b7
    0x11c5: v11c5(0x2b5c) = CONST 
    0x11c8: v11c8(0x34) = CONST 
    0x11cb: CODECOPY v11c3, v11c5(0x2b5c), v11c8(0x34)
    0x11cc: v11cc(0x40) = CONST 
    0x11ce: v11ce = ADD v11cc(0x40), v11c3
    0x11d2: v11d2(0x40) = CONST 
    0x11d4: v11d4 = MLOAD v11d2(0x40)
    0x11d7: v11d7(0x84) = SUB v11ce, v11d4
    0x11d9: REVERT v11d4, v11d7(0x84)

    Begin block 0x11da
    prev=[0x1181], succ=[0x11e4]
    =================================
    0x11db: v11db(0x0) = CONST 
    0x11dd: v11dd(0x11e4) = CONST 
    0x11e0: v11e0(0x20b2) = CONST 
    0x11e3: v11e3_0 = CALLPRIVATE v11e0(0x20b2), v11dd(0x11e4)

    Begin block 0x11e4
    prev=[0x11da], succ=[0x11ee, 0x1254]
    =================================
    0x11e9: v11e9 = EQ v11e3_0, v647
    0x11ea: v11ea(0x1254) = CONST 
    0x11ed: JUMPI v11ea(0x1254), v11e9

    Begin block 0x11ee
    prev=[0x11e4], succ=[]
    =================================
    0x11ee: v11ee(0x40) = CONST 
    0x11f1: v11f1 = MLOAD v11ee(0x40)
    0x11f2: v11f2(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1214: MSTORE v11f1, v11f2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1215: v1215(0x20) = CONST 
    0x1217: v1217(0x4) = CONST 
    0x121a: v121a = ADD v11f1, v1217(0x4)
    0x121b: MSTORE v121a, v1215(0x20)
    0x121c: v121c(0x1e) = CONST 
    0x121e: v121e(0x24) = CONST 
    0x1221: v1221 = ADD v11f1, v121e(0x24)
    0x1222: MSTORE v1221, v121c(0x1e)
    0x1223: v1223(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000) = CONST 
    0x1244: v1244(0x44) = CONST 
    0x1247: v1247 = ADD v11f1, v1244(0x44)
    0x1248: MSTORE v1247, v1223(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000)
    0x124a: v124a = MLOAD v11ee(0x40)
    0x124e: v124e(0x0) = SUB v11f1, v124a
    0x124f: v124f(0x64) = CONST 
    0x1251: v1251(0x64) = ADD v124f(0x64), v124e(0x0)
    0x1253: REVERT v124a, v1251(0x64)

    Begin block 0x1254
    prev=[0x11e4], succ=[0x1264, 0x12b4]
    =================================
    0x1255: v1255(0xde0b6b3a7640000) = CONST 
    0x125f: v125f = LT v11e3_0, v1255(0xde0b6b3a7640000)
    0x1260: v1260(0x12b4) = CONST 
    0x1263: JUMPI v1260(0x12b4), v125f

    Begin block 0x1264
    prev=[0x1254], succ=[]
    =================================
    0x1264: v1264(0x40) = CONST 
    0x1266: v1266 = MLOAD v1264(0x40)
    0x1267: v1267(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1289: MSTORE v1266, v1267(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x128a: v128a(0x4) = CONST 
    0x128c: v128c = ADD v128a(0x4), v1266
    0x128f: v128f(0x20) = CONST 
    0x1291: v1291 = ADD v128f(0x20), v128c
    0x1294: v1294(0x20) = SUB v1291, v128c
    0x1296: MSTORE v128c, v1294(0x20)
    0x1297: v1297(0x38) = CONST 
    0x129a: MSTORE v1291, v1297(0x38)
    0x129b: v129b(0x20) = CONST 
    0x129d: v129d = ADD v129b(0x20), v1291
    0x129f: v129f(0x2bb8) = CONST 
    0x12a2: v12a2(0x38) = CONST 
    0x12a5: CODECOPY v129d, v129f(0x2bb8), v12a2(0x38)
    0x12a6: v12a6(0x40) = CONST 
    0x12a8: v12a8 = ADD v12a6(0x40), v129d
    0x12ac: v12ac(0x40) = CONST 
    0x12ae: v12ae = MLOAD v12ac(0x40)
    0x12b1: v12b1(0x84) = SUB v12a8, v12ae
    0x12b3: REVERT v12ae, v12b1(0x84)

    Begin block 0x12b4
    prev=[0x1254], succ=[0x12be]
    =================================
    0x12b5: v12b5(0x0) = CONST 
    0x12b7: v12b7(0x12be) = CONST 
    0x12ba: v12ba(0x1805) = CONST 
    0x12bd: v12bd_0 = CALLPRIVATE v12ba(0x1805), v12b7(0x12be)

    Begin block 0x12be
    prev=[0x12b4], succ=[0x12c9, 0x1319]
    =================================
    0x12c3: v12c3 = GT v642, v12bd_0
    0x12c4: v12c4 = ISZERO v12c3
    0x12c5: v12c5(0x1319) = CONST 
    0x12c8: JUMPI v12c5(0x1319), v12c4

    Begin block 0x12c9
    prev=[0x12be], succ=[]
    =================================
    0x12c9: v12c9(0x40) = CONST 
    0x12cb: v12cb = MLOAD v12c9(0x40)
    0x12cc: v12cc(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x12ee: MSTORE v12cb, v12cc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12ef: v12ef(0x4) = CONST 
    0x12f1: v12f1 = ADD v12ef(0x4), v12cb
    0x12f4: v12f4(0x20) = CONST 
    0x12f6: v12f6 = ADD v12f4(0x20), v12f1
    0x12f9: v12f9(0x20) = SUB v12f6, v12f1
    0x12fb: MSTORE v12f1, v12f9(0x20)
    0x12fc: v12fc(0x2e) = CONST 
    0x12ff: MSTORE v12f6, v12fc(0x2e)
    0x1300: v1300(0x20) = CONST 
    0x1302: v1302 = ADD v1300(0x20), v12f6
    0x1304: v1304(0x2cd3) = CONST 
    0x1307: v1307(0x2e) = CONST 
    0x130a: CODECOPY v1302, v1304(0x2cd3), v1307(0x2e)
    0x130b: v130b(0x40) = CONST 
    0x130d: v130d = ADD v130b(0x40), v1302
    0x1311: v1311(0x40) = CONST 
    0x1313: v1313 = MLOAD v1311(0x40)
    0x1316: v1316(0x84) = SUB v130d, v1313
    0x1318: REVERT v1313, v1316(0x84)

    Begin block 0x1319
    prev=[0x12be], succ=[0x1323]
    =================================
    0x131a: v131a(0x0) = CONST 
    0x131c: v131c(0x1323) = CONST 
    0x131f: v131f(0x21c3) = CONST 
    0x1322: v1322_0 = CALLPRIVATE v131f(0x21c3), v131c(0x1323)

    Begin block 0x1323
    prev=[0x1319], succ=[0x132e, 0x1394]
    =================================
    0x1326: v1326(0x0) = CONST 
    0x1329: v1329 = GT v1322_0, v1326(0x0)
    0x132a: v132a(0x1394) = CONST 
    0x132d: JUMPI v132a(0x1394), v1329

    Begin block 0x132e
    prev=[0x1323], succ=[]
    =================================
    0x132e: v132e(0x40) = CONST 
    0x1331: v1331 = MLOAD v132e(0x40)
    0x1332: v1332(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1354: MSTORE v1331, v1332(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1355: v1355(0x20) = CONST 
    0x1357: v1357(0x4) = CONST 
    0x135a: v135a = ADD v1331, v1357(0x4)
    0x135b: MSTORE v135a, v1355(0x20)
    0x135c: v135c(0x1f) = CONST 
    0x135e: v135e(0x24) = CONST 
    0x1361: v1361 = ADD v1331, v135e(0x24)
    0x1362: MSTORE v1361, v135c(0x1f)
    0x1363: v1363(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500) = CONST 
    0x1384: v1384(0x44) = CONST 
    0x1387: v1387 = ADD v1331, v1384(0x44)
    0x1388: MSTORE v1387, v1363(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500)
    0x138a: v138a = MLOAD v132e(0x40)
    0x138e: v138e(0x0) = SUB v1331, v138a
    0x138f: v138f(0x64) = CONST 
    0x1391: v1391(0x64) = ADD v138f(0x64), v138e(0x0)
    0x1393: REVERT v138a, v1391(0x64)

    Begin block 0x1394
    prev=[0x1323], succ=[0x3765]
    =================================
    0x1395: v1395(0x0) = CONST 
    0x1397: v1397(0x13ac) = CONST 
    0x139a: v139a(0xde0b6b3a7640000) = CONST 
    0x13a3: v13a3(0x3765) = CONST 
    0x13a8: v13a8(0x23c1) = CONST 
    0x13ab: v13ab_0 = CALLPRIVATE v13a8(0x23c1), v1322_0, v642, v13a3(0x3765)

    Begin block 0x3765
    prev=[0x1394], succ=[0x13ac]
    =================================
    0x3767: v3767(0x2434) = CONST 
    0x376a: v376a_0 = CALLPRIVATE v3767(0x2434), v139a(0xde0b6b3a7640000), v13ab_0, v1397(0x13ac)

    Begin block 0x13ac
    prev=[0x3765], succ=[0x2376B0x13ac]
    =================================
    0x13ad: v13ad(0x6) = CONST 
    0x13af: v13af = SLOAD v13ad(0x6)
    0x13b3: v13b3(0x13bc) = CONST 
    0x13b8: v13b8(0x2376) = CONST 
    0x13bb: JUMP v13b8(0x2376)

    Begin block 0x2376B0x13ac
    prev=[0x13ac], succ=[0x23b80x2376B0x13ac]
    =================================
    0x2377S0x13ac: v2377V13ac(0x0) = CONST 
    0x2379S0x13ac: v2379V13ac(0x23b8) = CONST 
    0x237eS0x13ac: v237eV13ac(0x40) = CONST 
    0x2380S0x13ac: v2380V13ac = MLOAD v237eV13ac(0x40)
    0x2382S0x13ac: v2382V13ac(0x40) = CONST 
    0x2384S0x13ac: v2384V13ac = ADD v2382V13ac(0x40), v2380V13ac
    0x2385S0x13ac: v2385V13ac(0x40) = CONST 
    0x2387S0x13ac: MSTORE v2385V13ac(0x40), v2384V13ac
    0x2389S0x13ac: v2389V13ac(0x1e) = CONST 
    0x238cS0x13ac: MSTORE v2380V13ac, v2389V13ac(0x1e)
    0x238dS0x13ac: v238dV13ac(0x20) = CONST 
    0x238fS0x13ac: v238fV13ac = ADD v238dV13ac(0x20), v2380V13ac
    0x2390S0x13ac: v2390V13ac(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x23b2S0x13ac: MSTORE v238fV13ac, v2390V13ac(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x23b4S0x13ac: v23b4V13ac(0x2632) = CONST 
    0x23b7S0x13ac: v23b7_0V13ac = CALLPRIVATE v23b4V13ac(0x2632), v2380V13ac, v376a_0, v13af, v2379V13ac(0x23b8)

    Begin block 0x23b80x2376B0x13ac
    prev=[0x2376B0x13ac], succ=[0x23bb0x2376B0x13ac]
    =================================

    Begin block 0x23bb0x2376B0x13ac
    prev=[0x23b80x2376B0x13ac], succ=[0x13bc]
    =================================
    0x23c00x2376S0x13ac: JUMP v13b3(0x13bc)

    Begin block 0x13bc
    prev=[0x23bb0x2376B0x13ac], succ=[0x13cc]
    =================================
    0x13bd: v13bd(0x6) = CONST 
    0x13bf: SSTORE v13bd(0x6), v23b7_0V13ac
    0x13c0: v13c0(0x7) = CONST 
    0x13c2: v13c2 = SLOAD v13c0(0x7)
    0x13c3: v13c3(0x13cc) = CONST 
    0x13c8: v13c8(0x2476) = CONST 
    0x13cb: v13cb_0 = CALLPRIVATE v13c8(0x2476), v376a_0, v13c2, v13c3(0x13cc)

    Begin block 0x13cc
    prev=[0x13bc], succ=[0x13d9]
    =================================
    0x13cd: v13cd(0x7) = CONST 
    0x13cf: SSTORE v13cd(0x7), v13cb_0
    0x13d0: v13d0(0x0) = CONST 
    0x13d2: v13d2(0x13d9) = CONST 
    0x13d5: v13d5(0x1719) = CONST 
    0x13d8: v13d8_0 = CALLPRIVATE v13d5(0x1719), v13d2(0x13d9)

    Begin block 0x13d9
    prev=[0x13cc], succ=[0x1451, 0x1455]
    =================================
    0x13da: v13da(0x2) = CONST 
    0x13dc: v13dc = SLOAD v13da(0x2)
    0x13dd: v13dd(0x40) = CONST 
    0x13e0: v13e0 = MLOAD v13dd(0x40)
    0x13e1: v13e1(0x79cc679000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1403: MSTORE v13e0, v13e1(0x79cc679000000000000000000000000000000000000000000000000000000000)
    0x1404: v1404 = CALLER 
    0x1405: v1405(0x4) = CONST 
    0x1408: v1408 = ADD v13e0, v1405(0x4)
    0x1409: MSTORE v1408, v1404
    0x140a: v140a(0x24) = CONST 
    0x140d: v140d = ADD v13e0, v140a(0x24)
    0x1410: MSTORE v140d, v642
    0x1412: v1412 = MLOAD v13dd(0x40)
    0x1416: v1416(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x142d: v142d = AND v13dc, v1416(0xffffffffffffffffffffffffffffffffffffffff)
    0x142f: v142f(0x79cc6790) = CONST 
    0x1435: v1435(0x44) = CONST 
    0x1439: v1439 = ADD v13e0, v1435(0x44)
    0x143b: v143b(0x0) = CONST 
    0x1443: v1443(0x0) = SUB v13e0, v1412
    0x1444: v1444(0x44) = ADD v1443(0x0), v1435(0x44)
    0x1449: v1449 = EXTCODESIZE v142d
    0x144a: v144a = ISZERO v1449
    0x144c: v144c = ISZERO v144a
    0x144d: v144d(0x1455) = CONST 
    0x1450: JUMPI v144d(0x1455), v144c

    Begin block 0x1451
    prev=[0x13d9], succ=[]
    =================================
    0x1451: v1451(0x0) = CONST 
    0x1454: REVERT v1451(0x0), v1451(0x0)

    Begin block 0x1455
    prev=[0x13d9], succ=[0x1460, 0x1469]
    =================================
    0x1457: v1457 = GAS 
    0x1458: v1458 = CALL v1457, v142d, v143b(0x0), v1412, v1444(0x44), v1412, v143b(0x0)
    0x1459: v1459 = ISZERO v1458
    0x145b: v145b = ISZERO v1459
    0x145c: v145c(0x1469) = CONST 
    0x145f: JUMPI v145c(0x1469), v145b

    Begin block 0x1460
    prev=[0x1455], succ=[]
    =================================
    0x1460: v1460 = RETURNDATASIZE 
    0x1461: v1461(0x0) = CONST 
    0x1464: RETURNDATACOPY v1461(0x0), v1461(0x0), v1460
    0x1465: v1465 = RETURNDATASIZE 
    0x1466: v1466(0x0) = CONST 
    0x1468: REVERT v1466(0x0), v1465

    Begin block 0x1469
    prev=[0x1455], succ=[0x1493]
    =================================
    0x146c: v146c = CALLER 
    0x146d: v146d(0x0) = CONST 
    0x1471: MSTORE v146d(0x0), v146c
    0x1472: v1472(0xe) = CONST 
    0x1474: v1474(0x20) = CONST 
    0x1478: MSTORE v1474(0x20), v1472(0xe)
    0x1479: v1479(0x40) = CONST 
    0x147d: v147d = SHA3 v146d(0x0), v1479(0x40)
    0x1480: MSTORE v146d(0x0), v13d8_0
    0x1483: MSTORE v1474(0x20), v147d
    0x1485: v1485 = SHA3 v146d(0x0), v1479(0x40)
    0x1486: v1486 = SLOAD v1485
    0x1487: v1487(0x1493) = CONST 
    0x148f: v148f(0x2476) = CONST 
    0x1492: v1492_0 = CALLPRIVATE v148f(0x2476), v376a_0, v1486, v1487(0x1493)

    Begin block 0x1493
    prev=[0x1469], succ=[0x1510, 0x14c3]
    =================================
    0x1494: v1494 = CALLER 
    0x1495: v1495(0x0) = CONST 
    0x1499: MSTORE v1495(0x0), v1494
    0x149a: v149a(0xe) = CONST 
    0x149c: v149c(0x20) = CONST 
    0x14a0: MSTORE v149c(0x20), v149a(0xe)
    0x14a1: v14a1(0x40) = CONST 
    0x14a5: v14a5 = SHA3 v1495(0x0), v14a1(0x40)
    0x14a8: MSTORE v1495(0x0), v13d8_0
    0x14aa: MSTORE v149c(0x20), v14a5
    0x14ad: v14ad = SHA3 v1495(0x0), v14a1(0x40)
    0x14b1: SSTORE v14ad, v1492_0
    0x14b4: MSTORE v1495(0x0), v1494
    0x14b5: v14b5(0xf) = CONST 
    0x14b9: MSTORE v149c(0x20), v14b5(0xf)
    0x14ba: v14ba = SHA3 v1495(0x0), v14a1(0x40)
    0x14bb: v14bb = SLOAD v14ba
    0x14bd: v14bd = ISZERO v14bb
    0x14bf: v14bf(0x1510) = CONST 
    0x14c2: JUMPI v14bf(0x1510), v14bd

    Begin block 0x1510
    prev=[0x1493, 0x1503], succ=[0x1516, 0x1538]
    =================================
    0x1510_0x0: v1510_0 = PHI v14bd, v150f
    0x1511: v1511 = ISZERO v1510_0
    0x1512: v1512(0x1538) = CONST 
    0x1515: JUMPI v1512(0x1538), v1511

    Begin block 0x1516
    prev=[0x1510], succ=[0x1538]
    =================================
    0x1516: v1516 = CALLER 
    0x1517: v1517(0x0) = CONST 
    0x151b: MSTORE v1517(0x0), v1516
    0x151c: v151c(0xf) = CONST 
    0x151e: v151e(0x20) = CONST 
    0x1522: MSTORE v151e(0x20), v151c(0xf)
    0x1523: v1523(0x40) = CONST 
    0x1526: v1526 = SHA3 v1517(0x0), v1523(0x40)
    0x1528: v1528 = SLOAD v1526
    0x1529: v1529(0x1) = CONST 
    0x152c: v152c = ADD v1528, v1529(0x1)
    0x152e: SSTORE v1526, v152c
    0x1531: MSTORE v1517(0x0), v1526
    0x1533: v1533 = SHA3 v1517(0x0), v151e(0x20)
    0x1534: v1534 = ADD v1533, v1528
    0x1537: SSTORE v1534, v13d8_0

    Begin block 0x1538
    prev=[0x1516, 0x1510], succ=[0x1540]
    =================================
    0x1539: v1539(0x1540) = CONST 
    0x153c: v153c(0x25b5) = CONST 
    0x153f: CALLPRIVATE v153c(0x25b5), v1539(0x1540)

    Begin block 0x1540
    prev=[0x1538], succ=[0x3300x629]
    =================================
    0x1541: v1541 = CALLER 
    0x1542: v1542(0x0) = CONST 
    0x1546: MSTORE v1542(0x0), v1541
    0x1547: v1547(0xe) = CONST 
    0x1549: v1549(0x20) = CONST 
    0x154d: MSTORE v1549(0x20), v1547(0xe)
    0x154e: v154e(0x40) = CONST 
    0x1552: v1552 = SHA3 v1542(0x0), v154e(0x40)
    0x1555: MSTORE v1542(0x0), v13d8_0
    0x1557: MSTORE v1549(0x20), v1552
    0x155b: v155b = SHA3 v1542(0x0), v154e(0x40)
    0x155c: v155c = SLOAD v155b
    0x155e: v155e = MLOAD v154e(0x40)
    0x1561: MSTORE v155e, v13d8_0
    0x1564: v1564 = ADD v155e, v1549(0x20)
    0x1567: MSTORE v1564, v642
    0x156a: v156a = ADD v154e(0x40), v155e
    0x156b: MSTORE v156a, v155c
    0x156d: v156d = MLOAD v154e(0x40)
    0x156e: v156e(0x523040e57210c2af3b7a61d17ba47d377066ed7c71d1847477197fae677b9814) = CONST 
    0x1592: v1592(0x0) = SUB v155e, v156d
    0x1593: v1593(0x60) = CONST 
    0x1595: v1595(0x60) = ADD v1593(0x60), v1592(0x0)
    0x1597: LOG2 v156d, v1595(0x60), v156e(0x523040e57210c2af3b7a61d17ba47d377066ed7c71d1847477197fae677b9814), v1541
    0x159a: v159a = NUMBER 
    0x159b: v159b(0x0) = CONST 
    0x159f: MSTORE v159b(0x0), v159a
    0x15a0: v15a0(0x20) = CONST 
    0x15a4: MSTORE v15a0(0x20), v159b(0x0)
    0x15a5: v15a5(0x40) = CONST 
    0x15a9: v15a9 = SHA3 v159b(0x0), v15a5(0x40)
    0x15aa: v15aa = ORIGIN 
    0x15ac: MSTORE v159b(0x0), v15aa
    0x15af: MSTORE v15a0(0x20), v15a9
    0x15b2: v15b2 = SHA3 v159b(0x0), v15a5(0x40)
    0x15b4: v15b4 = SLOAD v15b2
    0x15b5: v15b5(0x1) = CONST 
    0x15b7: v15b7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x15da: v15da = AND v15b7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v15b4
    0x15dc: v15dc = OR v15b5(0x1), v15da
    0x15df: SSTORE v15b2, v15dc
    0x15e0: v15e0 = CALLER 
    0x15e2: MSTORE v159b(0x0), v15e0
    0x15e6: v15e6 = SHA3 v159b(0x0), v15a5(0x40)
    0x15e8: v15e8 = SLOAD v15e6
    0x15eb: v15eb = AND v15b7(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v15e8
    0x15ee: v15ee = OR v15b5(0x1), v15eb
    0x15f0: SSTORE v15e6, v15ee
    0x15f7: JUMP v62a(0x330)

    Begin block 0x3300x629
    prev=[0x1540], succ=[]
    =================================
    0x3310x629: STOP 

    Begin block 0x14c3
    prev=[0x1493], succ=[0x1502, 0x1503]
    =================================
    0x14c4: v14c4 = CALLER 
    0x14c5: v14c5(0x0) = CONST 
    0x14c9: MSTORE v14c5(0x0), v14c4
    0x14ca: v14ca(0xf) = CONST 
    0x14cc: v14cc(0x20) = CONST 
    0x14ce: MSTORE v14cc(0x20), v14ca(0xf)
    0x14cf: v14cf(0x40) = CONST 
    0x14d2: v14d2 = SHA3 v14c5(0x0), v14cf(0x40)
    0x14d4: v14d4 = SLOAD v14d2
    0x14d8: v14d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14fa: v14fa = ADD v14bb, v14d8(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x14fd: v14fd = LT v14fa, v14d4
    0x14fe: v14fe(0x1503) = CONST 
    0x1501: JUMPI v14fe(0x1503), v14fd

    Begin block 0x1502
    prev=[0x14c3], succ=[]
    =================================
    0x1502: THROW 

    Begin block 0x1503
    prev=[0x14c3], succ=[0x1510]
    =================================
    0x1505: v1505(0x0) = CONST 
    0x1507: MSTORE v1505(0x0), v14d2
    0x1508: v1508(0x20) = CONST 
    0x150a: v150a(0x0) = CONST 
    0x150c: v150c = SHA3 v150a(0x0), v1508(0x20)
    0x150d: v150d = ADD v150c, v14fa
    0x150e: v150e = SLOAD v150d
    0x150f: v150f = LT v150e, v13d8_0

}

function getRedeemableCoupons()() public {
    Begin block 0x64c
    prev=[], succ=[0x3010x64c]
    =================================
    0x64d: v64d(0x301) = CONST 
    0x650: v650(0x15f8) = CONST 
    0x653: v653_0 = CALLPRIVATE v650(0x15f8), v64d(0x301)

    Begin block 0x3010x64c
    prev=[0x64c], succ=[]
    =================================
    0x3020x64c: v64c302(0x40) = CONST 
    0x3050x64c: v64c305 = MLOAD v64c302(0x40)
    0x3080x64c: MSTORE v64c305, v653_0
    0x3090x64c: v64c309 = MLOAD v64c302(0x40)
    0x30d0x64c: v64c30d(0x0) = SUB v64c305, v64c309
    0x30e0x64c: v64c30e(0x20) = CONST 
    0x3100x64c: v64c310(0x20) = ADD v64c30e(0x20), v64c30d(0x0)
    0x3120x64c: RETURN v64c309, v64c310(0x20)

}

function sideToken()() public {
    Begin block 0x654
    prev=[], succ=[0x16fd]
    =================================
    0x655: v655(0x33c8) = CONST 
    0x658: v658(0x16fd) = CONST 
    0x65b: JUMP v658(0x16fd)

    Begin block 0x16fd
    prev=[0x654], succ=[0x33c8]
    =================================
    0x16fe: v16fe(0x5) = CONST 
    0x1700: v1700 = SLOAD v16fe(0x5)
    0x1701: v1701(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1716: v1716 = AND v1701(0xffffffffffffffffffffffffffffffffffffffff), v1700
    0x1718: JUMP v655(0x33c8)

    Begin block 0x33c8
    prev=[0x16fd], succ=[]
    =================================
    0x33c9: v33c9(0x40) = CONST 
    0x33cc: v33cc = MLOAD v33c9(0x40)
    0x33cd: v33cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x33e4: v33e4 = AND v1716, v33cd(0xffffffffffffffffffffffffffffffffffffffff)
    0x33e6: MSTORE v33cc, v33e4
    0x33e7: v33e7 = MLOAD v33c9(0x40)
    0x33eb: v33eb(0x0) = SUB v33cc, v33e7
    0x33ec: v33ec(0x20) = CONST 
    0x33ee: v33ee(0x20) = ADD v33ec(0x20), v33eb(0x0)
    0x33f0: RETURN v33e7, v33ee(0x20)

}

function epoch()() public {
    Begin block 0x65c
    prev=[], succ=[0x3410]
    =================================
    0x65d: v65d(0x3410) = CONST 
    0x660: v660(0x1719) = CONST 
    0x663: v663_0 = CALLPRIVATE v660(0x1719), v65d(0x3410)

    Begin block 0x3410
    prev=[0x65c], succ=[]
    =================================
    0x3411: v3411(0x40) = CONST 
    0x3414: v3414 = MLOAD v3411(0x40)
    0x3417: MSTORE v3414, v663_0
    0x3418: v3418 = MLOAD v3411(0x40)
    0x341c: v341c(0x0) = SUB v3414, v3418
    0x341d: v341d(0x20) = CONST 
    0x341f: v341f(0x20) = ADD v341d(0x20), v341c(0x0)
    0x3421: RETURN v3418, v341f(0x20)

}

function dollarPriceOne()() public {
    Begin block 0x664
    prev=[], succ=[0x1784]
    =================================
    0x665: v665(0x3441) = CONST 
    0x668: v668(0x1784) = CONST 
    0x66b: JUMP v668(0x1784)

    Begin block 0x1784
    prev=[0x664], succ=[0x3441]
    =================================
    0x1785: v1785(0xde0b6b3a7640000) = CONST 
    0x178f: JUMP v665(0x3441)

    Begin block 0x3441
    prev=[0x1784], succ=[]
    =================================
    0x3442: v3442(0x40) = CONST 
    0x3445: v3445 = MLOAD v3442(0x40)
    0x3448: MSTORE v3445, v1785(0xde0b6b3a7640000)
    0x3449: v3449 = MLOAD v3442(0x40)
    0x344d: v344d(0x0) = SUB v3445, v3449
    0x344e: v344e(0x20) = CONST 
    0x3450: v3450(0x20) = ADD v344e(0x20), v344d(0x0)
    0x3452: RETURN v3449, v3450(0x20)

}

function setMaxDiscountRate(uint256)() public {
    Begin block 0x66c
    prev=[], succ=[0x67e, 0x682]
    =================================
    0x66d: v66d(0x3472) = CONST 
    0x670: v670(0x4) = CONST 
    0x673: v673 = CALLDATASIZE 
    0x674: v674 = SUB v673, v670(0x4)
    0x675: v675(0x20) = CONST 
    0x678: v678 = LT v674, v675(0x20)
    0x679: v679 = ISZERO v678
    0x67a: v67a(0x682) = CONST 
    0x67d: JUMPI v67a(0x682), v679

    Begin block 0x67e
    prev=[0x66c], succ=[]
    =================================
    0x67e: v67e(0x0) = CONST 
    0x681: REVERT v67e(0x0), v67e(0x0)

    Begin block 0x682
    prev=[0x66c], succ=[0x1790]
    =================================
    0x684: v684 = CALLDATALOAD v670(0x4)
    0x685: v685(0x1790) = CONST 
    0x688: JUMP v685(0x1790)

    Begin block 0x1790
    prev=[0x682], succ=[0x17b0, 0x1800]
    =================================
    0x1791: v1791(0x1) = CONST 
    0x1793: v1793 = SLOAD v1791(0x1)
    0x1794: v1794(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x17a9: v17a9 = AND v1794(0xffffffffffffffffffffffffffffffffffffffff), v1793
    0x17aa: v17aa = CALLER 
    0x17ab: v17ab = EQ v17aa, v17a9
    0x17ac: v17ac(0x1800) = CONST 
    0x17af: JUMPI v17ac(0x1800), v17ab

    Begin block 0x17b0
    prev=[0x1790], succ=[]
    =================================
    0x17b0: v17b0(0x40) = CONST 
    0x17b2: v17b2 = MLOAD v17b0(0x40)
    0x17b3: v17b3(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x17d5: MSTORE v17b2, v17b3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17d6: v17d6(0x4) = CONST 
    0x17d8: v17d8 = ADD v17d6(0x4), v17b2
    0x17db: v17db(0x20) = CONST 
    0x17dd: v17dd = ADD v17db(0x20), v17d8
    0x17e0: v17e0(0x20) = SUB v17dd, v17d8
    0x17e2: MSTORE v17d8, v17e0(0x20)
    0x17e3: v17e3(0x28) = CONST 
    0x17e6: MSTORE v17dd, v17e3(0x28)
    0x17e7: v17e7(0x20) = CONST 
    0x17e9: v17e9 = ADD v17e7(0x20), v17dd
    0x17eb: v17eb(0x2b90) = CONST 
    0x17ee: v17ee(0x28) = CONST 
    0x17f1: CODECOPY v17e9, v17eb(0x2b90), v17ee(0x28)
    0x17f2: v17f2(0x40) = CONST 
    0x17f4: v17f4 = ADD v17f2(0x40), v17e9
    0x17f8: v17f8(0x40) = CONST 
    0x17fa: v17fa = MLOAD v17f8(0x40)
    0x17fd: v17fd(0x84) = SUB v17f4, v17fa
    0x17ff: REVERT v17fa, v17fd(0x84)

    Begin block 0x1800
    prev=[0x1790], succ=[0x3472]
    =================================
    0x1801: v1801(0xa) = CONST 
    0x1803: SSTORE v1801(0xa), v684
    0x1804: JUMP v66d(0x3472)

    Begin block 0x3472
    prev=[0x1800], succ=[]
    =================================
    0x3473: STOP 

}

function getBurnableDollarLeft()() public {
    Begin block 0x689
    prev=[], succ=[0x3010x689]
    =================================
    0x68a: v68a(0x301) = CONST 
    0x68d: v68d(0x1805) = CONST 
    0x690: v690_0 = CALLPRIVATE v68d(0x1805), v68a(0x301)

    Begin block 0x3010x689
    prev=[0x689], succ=[]
    =================================
    0x3020x689: v689302(0x40) = CONST 
    0x3050x689: v689305 = MLOAD v689302(0x40)
    0x3080x689: MSTORE v689305, v690_0
    0x3090x689: v689309 = MLOAD v689302(0x40)
    0x30d0x689: v68930d(0x0) = SUB v689305, v689309
    0x30e0x689: v68930e(0x20) = CONST 
    0x3100x689: v689310(0x20) = ADD v68930e(0x20), v68930d(0x0)
    0x3120x689: RETURN v689309, v689310(0x20)

}

function setMaxPremiumRate(uint256)() public {
    Begin block 0x691
    prev=[], succ=[0x6a3, 0x6a7]
    =================================
    0x692: v692(0x3493) = CONST 
    0x695: v695(0x4) = CONST 
    0x698: v698 = CALLDATASIZE 
    0x699: v699 = SUB v698, v695(0x4)
    0x69a: v69a(0x20) = CONST 
    0x69d: v69d = LT v699, v69a(0x20)
    0x69e: v69e = ISZERO v69d
    0x69f: v69f(0x6a7) = CONST 
    0x6a2: JUMPI v69f(0x6a7), v69e

    Begin block 0x6a3
    prev=[0x691], succ=[]
    =================================
    0x6a3: v6a3(0x0) = CONST 
    0x6a6: REVERT v6a3(0x0), v6a3(0x0)

    Begin block 0x6a7
    prev=[0x691], succ=[0x1848]
    =================================
    0x6a9: v6a9 = CALLDATALOAD v695(0x4)
    0x6aa: v6aa(0x1848) = CONST 
    0x6ad: JUMP v6aa(0x1848)

    Begin block 0x1848
    prev=[0x6a7], succ=[0x1868, 0x18b8]
    =================================
    0x1849: v1849(0x1) = CONST 
    0x184b: v184b = SLOAD v1849(0x1)
    0x184c: v184c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1861: v1861 = AND v184c(0xffffffffffffffffffffffffffffffffffffffff), v184b
    0x1862: v1862 = CALLER 
    0x1863: v1863 = EQ v1862, v1861
    0x1864: v1864(0x18b8) = CONST 
    0x1867: JUMPI v1864(0x18b8), v1863

    Begin block 0x1868
    prev=[0x1848], succ=[]
    =================================
    0x1868: v1868(0x40) = CONST 
    0x186a: v186a = MLOAD v1868(0x40)
    0x186b: v186b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x188d: MSTORE v186a, v186b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x188e: v188e(0x4) = CONST 
    0x1890: v1890 = ADD v188e(0x4), v186a
    0x1893: v1893(0x20) = CONST 
    0x1895: v1895 = ADD v1893(0x20), v1890
    0x1898: v1898(0x20) = SUB v1895, v1890
    0x189a: MSTORE v1890, v1898(0x20)
    0x189b: v189b(0x28) = CONST 
    0x189e: MSTORE v1895, v189b(0x28)
    0x189f: v189f(0x20) = CONST 
    0x18a1: v18a1 = ADD v189f(0x20), v1895
    0x18a3: v18a3(0x2b90) = CONST 
    0x18a6: v18a6(0x28) = CONST 
    0x18a9: CODECOPY v18a1, v18a3(0x2b90), v18a6(0x28)
    0x18aa: v18aa(0x40) = CONST 
    0x18ac: v18ac = ADD v18aa(0x40), v18a1
    0x18b0: v18b0(0x40) = CONST 
    0x18b2: v18b2 = MLOAD v18b0(0x40)
    0x18b5: v18b5(0x84) = SUB v18ac, v18b2
    0x18b7: REVERT v18b2, v18b5(0x84)

    Begin block 0x18b8
    prev=[0x1848], succ=[0x3493]
    =================================
    0x18b9: v18b9(0xc) = CONST 
    0x18bb: SSTORE v18b9(0xc), v6a9
    0x18bc: JUMP v692(0x3493)

    Begin block 0x3493
    prev=[0x18b8], succ=[]
    =================================
    0x3494: STOP 

}

function maxRedeemableCouponPercentPerEpoch()() public {
    Begin block 0x6ae
    prev=[], succ=[0x18bd]
    =================================
    0x6af: v6af(0x34b4) = CONST 
    0x6b2: v6b2(0x18bd) = CONST 
    0x6b5: JUMP v6b2(0x18bd)

    Begin block 0x18bd
    prev=[0x6ae], succ=[0x34b4]
    =================================
    0x18be: v18be(0xd) = CONST 
    0x18c0: v18c0 = SLOAD v18be(0xd)
    0x18c2: JUMP v6af(0x34b4)

    Begin block 0x34b4
    prev=[0x18bd], succ=[]
    =================================
    0x34b5: v34b5(0x40) = CONST 
    0x34b8: v34b8 = MLOAD v34b5(0x40)
    0x34bb: MSTORE v34b8, v18c0
    0x34bc: v34bc = MLOAD v34b5(0x40)
    0x34c0: v34c0(0x0) = SUB v34b8, v34bc
    0x34c1: v34c1(0x20) = CONST 
    0x34c3: v34c3(0x20) = ADD v34c1(0x20), v34c0(0x0)
    0x34c5: RETURN v34bc, v34c3(0x20)

}

function couponClaimed()() public {
    Begin block 0x6b6
    prev=[], succ=[0x18c3]
    =================================
    0x6b7: v6b7(0x34e5) = CONST 
    0x6ba: v6ba(0x18c3) = CONST 
    0x6bd: JUMP v6ba(0x18c3)

    Begin block 0x18c3
    prev=[0x6b6], succ=[0x34e5]
    =================================
    0x18c4: v18c4(0x8) = CONST 
    0x18c6: v18c6 = SLOAD v18c4(0x8)
    0x18c8: JUMP v6b7(0x34e5)

    Begin block 0x34e5
    prev=[0x18c3], succ=[]
    =================================
    0x34e6: v34e6(0x40) = CONST 
    0x34e9: v34e9 = MLOAD v34e6(0x40)
    0x34ec: MSTORE v34e9, v18c6
    0x34ed: v34ed = MLOAD v34e6(0x40)
    0x34f1: v34f1(0x0) = SUB v34e9, v34ed
    0x34f2: v34f2(0x20) = CONST 
    0x34f4: v34f4(0x20) = ADD v34f2(0x20), v34f1(0x0)
    0x34f6: RETURN v34ed, v34f4(0x20)

}

function isDebtPhase()() public {
    Begin block 0x6be
    prev=[], succ=[0x18c9]
    =================================
    0x6bf: v6bf(0x3516) = CONST 
    0x6c2: v6c2(0x18c9) = CONST 
    0x6c5: JUMP v6c2(0x18c9)

    Begin block 0x18c9
    prev=[0x6be], succ=[0x18dc]
    =================================
    0x18ca: v18ca(0x0) = CONST 
    0x18cc: v18cc(0xde0b6b3a7640000) = CONST 
    0x18d5: v18d5(0x18dc) = CONST 
    0x18d8: v18d8(0x20b2) = CONST 
    0x18db: v18db_0 = CALLPRIVATE v18d8(0x20b2), v18d5(0x18dc)

    Begin block 0x18dc
    prev=[0x18c9], succ=[0x3516]
    =================================
    0x18dd: v18dd = LT v18db_0, v18cc(0xde0b6b3a7640000)
    0x18e1: JUMP v6bf(0x3516)

    Begin block 0x3516
    prev=[0x18dc], succ=[]
    =================================
    0x3517: v3517(0x40) = CONST 
    0x351a: v351a = MLOAD v3517(0x40)
    0x351c: v351c = ISZERO v18dd
    0x351d: v351d = ISZERO v351c
    0x351f: MSTORE v351a, v351d
    0x3520: v3520 = MLOAD v3517(0x40)
    0x3524: v3524(0x0) = SUB v351a, v3520
    0x3525: v3525(0x20) = CONST 
    0x3527: v3527(0x20) = ADD v3525(0x20), v3524(0x0)
    0x3529: RETURN v3520, v3527(0x20)

}

function setOperator(address)() public {
    Begin block 0x6c6
    prev=[], succ=[0x6d8, 0x6dc]
    =================================
    0x6c7: v6c7(0x3549) = CONST 
    0x6ca: v6ca(0x4) = CONST 
    0x6cd: v6cd = CALLDATASIZE 
    0x6ce: v6ce = SUB v6cd, v6ca(0x4)
    0x6cf: v6cf(0x20) = CONST 
    0x6d2: v6d2 = LT v6ce, v6cf(0x20)
    0x6d3: v6d3 = ISZERO v6d2
    0x6d4: v6d4(0x6dc) = CONST 
    0x6d7: JUMPI v6d4(0x6dc), v6d3

    Begin block 0x6d8
    prev=[0x6c6], succ=[]
    =================================
    0x6d8: v6d8(0x0) = CONST 
    0x6db: REVERT v6d8(0x0), v6d8(0x0)

    Begin block 0x6dc
    prev=[0x6c6], succ=[0x18e2]
    =================================
    0x6de: v6de = CALLDATALOAD v6ca(0x4)
    0x6df: v6df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6f4: v6f4 = AND v6df(0xffffffffffffffffffffffffffffffffffffffff), v6de
    0x6f5: v6f5(0x18e2) = CONST 
    0x6f8: JUMP v6f5(0x18e2)

    Begin block 0x18e2
    prev=[0x6dc], succ=[0x1902, 0x1952]
    =================================
    0x18e3: v18e3(0x1) = CONST 
    0x18e5: v18e5 = SLOAD v18e3(0x1)
    0x18e6: v18e6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x18fb: v18fb = AND v18e6(0xffffffffffffffffffffffffffffffffffffffff), v18e5
    0x18fc: v18fc = CALLER 
    0x18fd: v18fd = EQ v18fc, v18fb
    0x18fe: v18fe(0x1952) = CONST 
    0x1901: JUMPI v18fe(0x1952), v18fd

    Begin block 0x1902
    prev=[0x18e2], succ=[]
    =================================
    0x1902: v1902(0x40) = CONST 
    0x1904: v1904 = MLOAD v1902(0x40)
    0x1905: v1905(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1927: MSTORE v1904, v1905(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1928: v1928(0x4) = CONST 
    0x192a: v192a = ADD v1928(0x4), v1904
    0x192d: v192d(0x20) = CONST 
    0x192f: v192f = ADD v192d(0x20), v192a
    0x1932: v1932(0x20) = SUB v192f, v192a
    0x1934: MSTORE v192a, v1932(0x20)
    0x1935: v1935(0x28) = CONST 
    0x1938: MSTORE v192f, v1935(0x28)
    0x1939: v1939(0x20) = CONST 
    0x193b: v193b = ADD v1939(0x20), v192f
    0x193d: v193d(0x2b90) = CONST 
    0x1940: v1940(0x28) = CONST 
    0x1943: CODECOPY v193b, v193d(0x2b90), v1940(0x28)
    0x1944: v1944(0x40) = CONST 
    0x1946: v1946 = ADD v1944(0x40), v193b
    0x194a: v194a(0x40) = CONST 
    0x194c: v194c = MLOAD v194a(0x40)
    0x194f: v194f(0x84) = SUB v1946, v194c
    0x1951: REVERT v194c, v194f(0x84)

    Begin block 0x1952
    prev=[0x18e2], succ=[0x3549]
    =================================
    0x1953: v1953(0x1) = CONST 
    0x1956: v1956 = SLOAD v1953(0x1)
    0x1957: v1957(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1978: v1978 = AND v1957(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1956
    0x1979: v1979(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1991: v1991 = AND v1979(0xffffffffffffffffffffffffffffffffffffffff), v6f4
    0x1995: v1995 = OR v1991, v1978
    0x1997: SSTORE v1953(0x1), v1995
    0x1998: JUMP v6c7(0x3549)

    Begin block 0x3549
    prev=[0x1952], succ=[]
    =================================
    0x354a: STOP 

}

function maxDiscountRate()() public {
    Begin block 0x6f9
    prev=[], succ=[0x1999]
    =================================
    0x6fa: v6fa(0x356a) = CONST 
    0x6fd: v6fd(0x1999) = CONST 
    0x700: JUMP v6fd(0x1999)

    Begin block 0x1999
    prev=[0x6f9], succ=[0x356a]
    =================================
    0x199a: v199a(0xa) = CONST 
    0x199c: v199c = SLOAD v199a(0xa)
    0x199e: JUMP v6fa(0x356a)

    Begin block 0x356a
    prev=[0x1999], succ=[]
    =================================
    0x356b: v356b(0x40) = CONST 
    0x356e: v356e = MLOAD v356b(0x40)
    0x3571: MSTORE v356e, v199c
    0x3572: v3572 = MLOAD v356b(0x40)
    0x3576: v3576(0x0) = SUB v356e, v3572
    0x3577: v3577(0x20) = CONST 
    0x3579: v3579(0x20) = ADD v3577(0x20), v3576(0x0)
    0x357b: RETURN v3572, v3579(0x20)

}

function redeemCoupons(uint256,uint256,uint256)() public {
    Begin block 0x701
    prev=[], succ=[0x713, 0x717]
    =================================
    0x702: v702(0x330) = CONST 
    0x705: v705(0x4) = CONST 
    0x708: v708 = CALLDATASIZE 
    0x709: v709 = SUB v708, v705(0x4)
    0x70a: v70a(0x60) = CONST 
    0x70d: v70d = LT v709, v70a(0x60)
    0x70e: v70e = ISZERO v70d
    0x70f: v70f(0x717) = CONST 
    0x712: JUMPI v70f(0x717), v70e

    Begin block 0x713
    prev=[0x701], succ=[]
    =================================
    0x713: v713(0x0) = CONST 
    0x716: REVERT v713(0x0), v713(0x0)

    Begin block 0x717
    prev=[0x701], succ=[0x199f]
    =================================
    0x71a: v71a = CALLDATALOAD v705(0x4)
    0x71c: v71c(0x20) = CONST 
    0x71f: v71f(0x24) = ADD v705(0x4), v71c(0x20)
    0x720: v720 = CALLDATALOAD v71f(0x24)
    0x722: v722(0x40) = CONST 
    0x724: v724(0x44) = ADD v722(0x40), v705(0x4)
    0x725: v725 = CALLDATALOAD v724(0x44)
    0x726: v726(0x199f) = CONST 
    0x729: JUMP v726(0x199f)

    Begin block 0x199f
    prev=[0x717], succ=[0x2577B0x199f]
    =================================
    0x19a0: v19a0(0x19a7) = CONST 
    0x19a3: v19a3(0x2577) = CONST 
    0x19a6: JUMP v19a3(0x2577)

    Begin block 0x2577B0x199f
    prev=[0x199f], succ=[0x19a7]
    =================================
    0x2578S0x199f: v2578V199f = NUMBER 
    0x2579S0x199f: v2579V199f(0x0) = CONST 
    0x257dS0x199f: MSTORE v2579V199f(0x0), v2578V199f
    0x257eS0x199f: v257eV199f(0x20) = CONST 
    0x2582S0x199f: MSTORE v257eV199f(0x20), v2579V199f(0x0)
    0x2583S0x199f: v2583V199f(0x40) = CONST 
    0x2587S0x199f: v2587V199f = SHA3 v2579V199f(0x0), v2583V199f(0x40)
    0x2588S0x199f: v2588V199f = ORIGIN 
    0x258aS0x199f: MSTORE v2579V199f(0x0), v2588V199f
    0x258dS0x199f: MSTORE v257eV199f(0x20), v2587V199f
    0x258fS0x199f: v258fV199f = SHA3 v2579V199f(0x0), v2583V199f(0x40)
    0x2590S0x199f: v2590V199f = SLOAD v258fV199f
    0x2591S0x199f: v2591V199f(0xff) = CONST 
    0x2593S0x199f: v2593V199f = AND v2591V199f(0xff), v2590V199f
    0x2595S0x199f: JUMP v19a0(0x19a7)

    Begin block 0x19a7
    prev=[0x2577B0x199f], succ=[0x19ad, 0x19fd]
    =================================
    0x19a8: v19a8 = ISZERO v2593V199f
    0x19a9: v19a9(0x19fd) = CONST 
    0x19ac: JUMPI v19a9(0x19fd), v19a8

    Begin block 0x19ad
    prev=[0x19a7], succ=[]
    =================================
    0x19ad: v19ad(0x40) = CONST 
    0x19af: v19af = MLOAD v19ad(0x40)
    0x19b0: v19b0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x19d2: MSTORE v19af, v19b0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x19d3: v19d3(0x4) = CONST 
    0x19d5: v19d5 = ADD v19d3(0x4), v19af
    0x19d8: v19d8(0x20) = CONST 
    0x19da: v19da = ADD v19d8(0x20), v19d5
    0x19dd: v19dd(0x20) = SUB v19da, v19d5
    0x19df: MSTORE v19d5, v19dd(0x20)
    0x19e0: v19e0(0x26) = CONST 
    0x19e3: MSTORE v19da, v19e0(0x26)
    0x19e4: v19e4(0x20) = CONST 
    0x19e6: v19e6 = ADD v19e4(0x20), v19da
    0x19e8: v19e8(0x2d2b) = CONST 
    0x19eb: v19eb(0x26) = CONST 
    0x19ee: CODECOPY v19e6, v19e8(0x2d2b), v19eb(0x26)
    0x19ef: v19ef(0x40) = CONST 
    0x19f1: v19f1 = ADD v19ef(0x40), v19e6
    0x19f5: v19f5(0x40) = CONST 
    0x19f7: v19f7 = MLOAD v19f5(0x40)
    0x19fa: v19fa(0x84) = SUB v19f1, v19f7
    0x19fc: REVERT v19f7, v19fa(0x84)

    Begin block 0x19fd
    prev=[0x19a7], succ=[0x2596B0x19fd]
    =================================
    0x19fe: v19fe(0x1a05) = CONST 
    0x1a01: v1a01(0x2596) = CONST 
    0x1a04: JUMP v1a01(0x2596)

    Begin block 0x2596B0x19fd
    prev=[0x19fd], succ=[0x1a05]
    =================================
    0x2597S0x19fd: v2597V19fd = NUMBER 
    0x2598S0x19fd: v2598V19fd(0x0) = CONST 
    0x259cS0x19fd: MSTORE v2598V19fd(0x0), v2597V19fd
    0x259dS0x19fd: v259dV19fd(0x20) = CONST 
    0x25a1S0x19fd: MSTORE v259dV19fd(0x20), v2598V19fd(0x0)
    0x25a2S0x19fd: v25a2V19fd(0x40) = CONST 
    0x25a6S0x19fd: v25a6V19fd = SHA3 v2598V19fd(0x0), v25a2V19fd(0x40)
    0x25a7S0x19fd: v25a7V19fd = CALLER 
    0x25a9S0x19fd: MSTORE v2598V19fd(0x0), v25a7V19fd
    0x25acS0x19fd: MSTORE v259dV19fd(0x20), v25a6V19fd
    0x25aeS0x19fd: v25aeV19fd = SHA3 v2598V19fd(0x0), v25a2V19fd(0x40)
    0x25afS0x19fd: v25afV19fd = SLOAD v25aeV19fd
    0x25b0S0x19fd: v25b0V19fd(0xff) = CONST 
    0x25b2S0x19fd: v25b2V19fd = AND v25b0V19fd(0xff), v25afV19fd
    0x25b4S0x19fd: JUMP v19fe(0x1a05)

    Begin block 0x1a05
    prev=[0x2596B0x19fd], succ=[0x1a0b, 0x1a5b]
    =================================
    0x1a06: v1a06 = ISZERO v25b2V19fd
    0x1a07: v1a07(0x1a5b) = CONST 
    0x1a0a: JUMPI v1a07(0x1a5b), v1a06

    Begin block 0x1a0b
    prev=[0x1a05], succ=[]
    =================================
    0x1a0b: v1a0b(0x40) = CONST 
    0x1a0d: v1a0d = MLOAD v1a0b(0x40)
    0x1a0e: v1a0e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1a30: MSTORE v1a0d, v1a0e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a31: v1a31(0x4) = CONST 
    0x1a33: v1a33 = ADD v1a31(0x4), v1a0d
    0x1a36: v1a36(0x20) = CONST 
    0x1a38: v1a38 = ADD v1a36(0x20), v1a33
    0x1a3b: v1a3b(0x20) = SUB v1a38, v1a33
    0x1a3d: MSTORE v1a33, v1a3b(0x20)
    0x1a3e: v1a3e(0x26) = CONST 
    0x1a41: MSTORE v1a38, v1a3e(0x26)
    0x1a42: v1a42(0x20) = CONST 
    0x1a44: v1a44 = ADD v1a42(0x20), v1a38
    0x1a46: v1a46(0x2d2b) = CONST 
    0x1a49: v1a49(0x26) = CONST 
    0x1a4c: CODECOPY v1a44, v1a46(0x2d2b), v1a49(0x26)
    0x1a4d: v1a4d(0x40) = CONST 
    0x1a4f: v1a4f = ADD v1a4d(0x40), v1a44
    0x1a53: v1a53(0x40) = CONST 
    0x1a55: v1a55 = MLOAD v1a53(0x40)
    0x1a58: v1a58(0x84) = SUB v1a4f, v1a55
    0x1a5a: REVERT v1a55, v1a58(0x84)

    Begin block 0x1a5b
    prev=[0x1a05], succ=[0x1a64, 0x1ab4]
    =================================
    0x1a5c: v1a5c(0x0) = CONST 
    0x1a5f: v1a5f = GT v720, v1a5c(0x0)
    0x1a60: v1a60(0x1ab4) = CONST 
    0x1a63: JUMPI v1a60(0x1ab4), v1a5f

    Begin block 0x1a64
    prev=[0x1a5b], succ=[]
    =================================
    0x1a64: v1a64(0x40) = CONST 
    0x1a66: v1a66 = MLOAD v1a64(0x40)
    0x1a67: v1a67(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1a89: MSTORE v1a66, v1a67(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1a8a: v1a8a(0x4) = CONST 
    0x1a8c: v1a8c = ADD v1a8a(0x4), v1a66
    0x1a8f: v1a8f(0x20) = CONST 
    0x1a91: v1a91 = ADD v1a8f(0x20), v1a8c
    0x1a94: v1a94(0x20) = SUB v1a91, v1a8c
    0x1a96: MSTORE v1a8c, v1a94(0x20)
    0x1a97: v1a97(0x32) = CONST 
    0x1a9a: MSTORE v1a91, v1a97(0x32)
    0x1a9b: v1a9b(0x20) = CONST 
    0x1a9d: v1a9d = ADD v1a9b(0x20), v1a91
    0x1a9f: v1a9f(0x2a98) = CONST 
    0x1aa2: v1aa2(0x32) = CONST 
    0x1aa5: CODECOPY v1a9d, v1a9f(0x2a98), v1aa2(0x32)
    0x1aa6: v1aa6(0x40) = CONST 
    0x1aa8: v1aa8 = ADD v1aa6(0x40), v1a9d
    0x1aac: v1aac(0x40) = CONST 
    0x1aae: v1aae = MLOAD v1aac(0x40)
    0x1ab1: v1ab1(0x84) = SUB v1aa8, v1aae
    0x1ab3: REVERT v1aae, v1ab1(0x84)

    Begin block 0x1ab4
    prev=[0x1a5b], succ=[0x1abe]
    =================================
    0x1ab5: v1ab5(0x0) = CONST 
    0x1ab7: v1ab7(0x1abe) = CONST 
    0x1aba: v1aba(0x20b2) = CONST 
    0x1abd: v1abd_0 = CALLPRIVATE v1aba(0x20b2), v1ab7(0x1abe)

    Begin block 0x1abe
    prev=[0x1ab4], succ=[0x1ac8, 0x1b2e]
    =================================
    0x1ac3: v1ac3 = EQ v1abd_0, v725
    0x1ac4: v1ac4(0x1b2e) = CONST 
    0x1ac7: JUMPI v1ac4(0x1b2e), v1ac3

    Begin block 0x1ac8
    prev=[0x1abe], succ=[]
    =================================
    0x1ac8: v1ac8(0x40) = CONST 
    0x1acb: v1acb = MLOAD v1ac8(0x40)
    0x1acc: v1acc(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1aee: MSTORE v1acb, v1acc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1aef: v1aef(0x20) = CONST 
    0x1af1: v1af1(0x4) = CONST 
    0x1af4: v1af4 = ADD v1acb, v1af1(0x4)
    0x1af5: MSTORE v1af4, v1aef(0x20)
    0x1af6: v1af6(0x1e) = CONST 
    0x1af8: v1af8(0x24) = CONST 
    0x1afb: v1afb = ADD v1acb, v1af8(0x24)
    0x1afc: MSTORE v1afb, v1af6(0x1e)
    0x1afd: v1afd(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000) = CONST 
    0x1b1e: v1b1e(0x44) = CONST 
    0x1b21: v1b21 = ADD v1acb, v1b1e(0x44)
    0x1b22: MSTORE v1b21, v1afd(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000)
    0x1b24: v1b24 = MLOAD v1ac8(0x40)
    0x1b28: v1b28(0x0) = SUB v1acb, v1b24
    0x1b29: v1b29(0x64) = CONST 
    0x1b2b: v1b2b(0x64) = ADD v1b29(0x64), v1b28(0x0)
    0x1b2d: REVERT v1b24, v1b2b(0x64)

    Begin block 0x1b2e
    prev=[0x1abe], succ=[0x1b3f, 0x1b8f]
    =================================
    0x1b2f: v1b2f(0xde0b6b3a7640000) = CONST 
    0x1b39: v1b39 = LT v1abd_0, v1b2f(0xde0b6b3a7640000)
    0x1b3a: v1b3a = ISZERO v1b39
    0x1b3b: v1b3b(0x1b8f) = CONST 
    0x1b3e: JUMPI v1b3b(0x1b8f), v1b3a

    Begin block 0x1b3f
    prev=[0x1b2e], succ=[]
    =================================
    0x1b3f: v1b3f(0x40) = CONST 
    0x1b41: v1b41 = MLOAD v1b3f(0x40)
    0x1b42: v1b42(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1b64: MSTORE v1b41, v1b42(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1b65: v1b65(0x4) = CONST 
    0x1b67: v1b67 = ADD v1b65(0x4), v1b41
    0x1b6a: v1b6a(0x20) = CONST 
    0x1b6c: v1b6c = ADD v1b6a(0x20), v1b67
    0x1b6f: v1b6f(0x20) = SUB v1b6c, v1b67
    0x1b71: MSTORE v1b67, v1b6f(0x20)
    0x1b72: v1b72(0x38) = CONST 
    0x1b75: MSTORE v1b6c, v1b72(0x38)
    0x1b76: v1b76(0x20) = CONST 
    0x1b78: v1b78 = ADD v1b76(0x20), v1b6c
    0x1b7a: v1b7a(0x2bb8) = CONST 
    0x1b7d: v1b7d(0x38) = CONST 
    0x1b80: CODECOPY v1b78, v1b7a(0x2bb8), v1b7d(0x38)
    0x1b81: v1b81(0x40) = CONST 
    0x1b83: v1b83 = ADD v1b81(0x40), v1b78
    0x1b87: v1b87(0x40) = CONST 
    0x1b89: v1b89 = MLOAD v1b87(0x40)
    0x1b8c: v1b8c(0x84) = SUB v1b83, v1b89
    0x1b8e: REVERT v1b89, v1b8c(0x84)

    Begin block 0x1b8f
    prev=[0x1b2e], succ=[0x1b99]
    =================================
    0x1b90: v1b90(0x0) = CONST 
    0x1b92: v1b92(0x1b99) = CONST 
    0x1b95: v1b95(0x15f8) = CONST 
    0x1b98: v1b98_0 = CALLPRIVATE v1b95(0x15f8), v1b92(0x1b99)

    Begin block 0x1b99
    prev=[0x1b8f], succ=[0x1ba4, 0x1bf4]
    =================================
    0x1b9e: v1b9e = GT v720, v1b98_0
    0x1b9f: v1b9f = ISZERO v1b9e
    0x1ba0: v1ba0(0x1bf4) = CONST 
    0x1ba3: JUMPI v1ba0(0x1bf4), v1b9f

    Begin block 0x1ba4
    prev=[0x1b99], succ=[]
    =================================
    0x1ba4: v1ba4(0x40) = CONST 
    0x1ba6: v1ba6 = MLOAD v1ba4(0x40)
    0x1ba7: v1ba7(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1bc9: MSTORE v1ba6, v1ba7(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1bca: v1bca(0x4) = CONST 
    0x1bcc: v1bcc = ADD v1bca(0x4), v1ba6
    0x1bcf: v1bcf(0x20) = CONST 
    0x1bd1: v1bd1 = ADD v1bcf(0x20), v1bcc
    0x1bd4: v1bd4(0x20) = SUB v1bd1, v1bcc
    0x1bd6: MSTORE v1bcc, v1bd4(0x20)
    0x1bd7: v1bd7(0x31) = CONST 
    0x1bda: MSTORE v1bd1, v1bd7(0x31)
    0x1bdb: v1bdb(0x20) = CONST 
    0x1bdd: v1bdd = ADD v1bdb(0x20), v1bd1
    0x1bdf: v1bdf(0x2bf0) = CONST 
    0x1be2: v1be2(0x31) = CONST 
    0x1be5: CODECOPY v1bdd, v1bdf(0x2bf0), v1be2(0x31)
    0x1be6: v1be6(0x40) = CONST 
    0x1be8: v1be8 = ADD v1be6(0x40), v1bdd
    0x1bec: v1bec(0x40) = CONST 
    0x1bee: v1bee = MLOAD v1bec(0x40)
    0x1bf1: v1bf1(0x84) = SUB v1be8, v1bee
    0x1bf3: REVERT v1bee, v1bf1(0x84)

    Begin block 0x1bf4
    prev=[0x1b99], succ=[0x1bfe]
    =================================
    0x1bf5: v1bf5(0x0) = CONST 
    0x1bf7: v1bf7(0x1bfe) = CONST 
    0x1bfa: v1bfa(0xc92) = CONST 
    0x1bfd: v1bfd_0 = CALLPRIVATE v1bfa(0xc92), v1bf7(0x1bfe)

    Begin block 0x1bfe
    prev=[0x1bf4], succ=[0x1c09, 0x1c6f]
    =================================
    0x1c01: v1c01(0x0) = CONST 
    0x1c04: v1c04 = GT v1bfd_0, v1c01(0x0)
    0x1c05: v1c05(0x1c6f) = CONST 
    0x1c08: JUMPI v1c05(0x1c6f), v1c04

    Begin block 0x1c09
    prev=[0x1bfe], succ=[]
    =================================
    0x1c09: v1c09(0x40) = CONST 
    0x1c0c: v1c0c = MLOAD v1c09(0x40)
    0x1c0d: v1c0d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c2f: MSTORE v1c0c, v1c0d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1c30: v1c30(0x20) = CONST 
    0x1c32: v1c32(0x4) = CONST 
    0x1c35: v1c35 = ADD v1c0c, v1c32(0x4)
    0x1c36: MSTORE v1c35, v1c30(0x20)
    0x1c37: v1c37(0x1f) = CONST 
    0x1c39: v1c39(0x24) = CONST 
    0x1c3c: v1c3c = ADD v1c0c, v1c39(0x24)
    0x1c3d: MSTORE v1c3c, v1c37(0x1f)
    0x1c3e: v1c3e(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500) = CONST 
    0x1c5f: v1c5f(0x44) = CONST 
    0x1c62: v1c62 = ADD v1c0c, v1c5f(0x44)
    0x1c63: MSTORE v1c62, v1c3e(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500)
    0x1c65: v1c65 = MLOAD v1c09(0x40)
    0x1c69: v1c69(0x0) = SUB v1c0c, v1c65
    0x1c6a: v1c6a(0x64) = CONST 
    0x1c6c: v1c6c(0x64) = ADD v1c6a(0x64), v1c69(0x0)
    0x1c6e: REVERT v1c65, v1c6c(0x64)

    Begin block 0x1c6f
    prev=[0x1bfe], succ=[0x381a]
    =================================
    0x1c70: v1c70(0x0) = CONST 
    0x1c72: v1c72(0x1c87) = CONST 
    0x1c75: v1c75(0xde0b6b3a7640000) = CONST 
    0x1c7e: v1c7e(0x381a) = CONST 
    0x1c83: v1c83(0x23c1) = CONST 
    0x1c86: v1c86_0 = CALLPRIVATE v1c83(0x23c1), v1bfd_0, v720, v1c7e(0x381a)

    Begin block 0x381a
    prev=[0x1c6f], succ=[0x1c87]
    =================================
    0x381c: v381c(0x2434) = CONST 
    0x381f: v381f_0 = CALLPRIVATE v381c(0x2434), v1c75(0xde0b6b3a7640000), v1c86_0, v1c72(0x1c87)

    Begin block 0x1c87
    prev=[0x381a], succ=[0x1d00, 0x1d04]
    =================================
    0x1c88: v1c88(0x2) = CONST 
    0x1c8a: v1c8a = SLOAD v1c88(0x2)
    0x1c8b: v1c8b(0x40) = CONST 
    0x1c8e: v1c8e = MLOAD v1c8b(0x40)
    0x1c8f: v1c8f(0x40c10f1900000000000000000000000000000000000000000000000000000000) = CONST 
    0x1cb1: MSTORE v1c8e, v1c8f(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0x1cb2: v1cb2 = CALLER 
    0x1cb3: v1cb3(0x4) = CONST 
    0x1cb6: v1cb6 = ADD v1c8e, v1cb3(0x4)
    0x1cb7: MSTORE v1cb6, v1cb2
    0x1cb8: v1cb8(0x24) = CONST 
    0x1cbb: v1cbb = ADD v1c8e, v1cb8(0x24)
    0x1cbe: MSTORE v1cbb, v381f_0
    0x1cc0: v1cc0 = MLOAD v1c8b(0x40)
    0x1cc4: v1cc4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1cdb: v1cdb = AND v1c8a, v1cc4(0xffffffffffffffffffffffffffffffffffffffff)
    0x1cdd: v1cdd(0x40c10f19) = CONST 
    0x1ce3: v1ce3(0x44) = CONST 
    0x1ce7: v1ce7 = ADD v1c8e, v1ce3(0x44)
    0x1ce9: v1ce9(0x20) = CONST 
    0x1cf1: v1cf1(0x0) = SUB v1c8e, v1cc0
    0x1cf2: v1cf2(0x44) = ADD v1cf1(0x0), v1ce3(0x44)
    0x1cf4: v1cf4(0x0) = CONST 
    0x1cf8: v1cf8 = EXTCODESIZE v1cdb
    0x1cf9: v1cf9 = ISZERO v1cf8
    0x1cfb: v1cfb = ISZERO v1cf9
    0x1cfc: v1cfc(0x1d04) = CONST 
    0x1cff: JUMPI v1cfc(0x1d04), v1cfb

    Begin block 0x1d00
    prev=[0x1c87], succ=[]
    =================================
    0x1d00: v1d00(0x0) = CONST 
    0x1d03: REVERT v1d00(0x0), v1d00(0x0)

    Begin block 0x1d04
    prev=[0x1c87], succ=[0x1d0f, 0x1d18]
    =================================
    0x1d06: v1d06 = GAS 
    0x1d07: v1d07 = CALL v1d06, v1cdb, v1cf4(0x0), v1cc0, v1cf2(0x44), v1cc0, v1ce9(0x20)
    0x1d08: v1d08 = ISZERO v1d07
    0x1d0a: v1d0a = ISZERO v1d08
    0x1d0b: v1d0b(0x1d18) = CONST 
    0x1d0e: JUMPI v1d0b(0x1d18), v1d0a

    Begin block 0x1d0f
    prev=[0x1d04], succ=[]
    =================================
    0x1d0f: v1d0f = RETURNDATASIZE 
    0x1d10: v1d10(0x0) = CONST 
    0x1d13: RETURNDATACOPY v1d10(0x0), v1d10(0x0), v1d0f
    0x1d14: v1d14 = RETURNDATASIZE 
    0x1d15: v1d15(0x0) = CONST 
    0x1d17: REVERT v1d15(0x0), v1d14

    Begin block 0x1d18
    prev=[0x1d04], succ=[0x1d2a, 0x1d2e]
    =================================
    0x1d1d: v1d1d(0x40) = CONST 
    0x1d1f: v1d1f = MLOAD v1d1d(0x40)
    0x1d20: v1d20 = RETURNDATASIZE 
    0x1d21: v1d21(0x20) = CONST 
    0x1d24: v1d24 = LT v1d20, v1d21(0x20)
    0x1d25: v1d25 = ISZERO v1d24
    0x1d26: v1d26(0x1d2e) = CONST 
    0x1d29: JUMPI v1d26(0x1d2e), v1d25

    Begin block 0x1d2a
    prev=[0x1d18], succ=[]
    =================================
    0x1d2a: v1d2a(0x0) = CONST 
    0x1d2d: REVERT v1d2a(0x0), v1d2a(0x0)

    Begin block 0x1d2e
    prev=[0x1d18], succ=[0x1d8a]
    =================================
    0x1d31: v1d31(0x40) = CONST 
    0x1d34: v1d34 = MLOAD v1d31(0x40)
    0x1d37: v1d37 = ADD v1d31(0x40), v1d34
    0x1d39: MSTORE v1d31(0x40), v1d37
    0x1d3a: v1d3a(0xb) = CONST 
    0x1d3d: MSTORE v1d34, v1d3a(0xb)
    0x1d3e: v1d3e(0x6f7665722072656465656d000000000000000000000000000000000000000000) = CONST 
    0x1d5f: v1d5f(0x20) = CONST 
    0x1d63: v1d63 = ADD v1d5f(0x20), v1d34
    0x1d67: MSTORE v1d63, v1d3e(0x6f7665722072656465656d000000000000000000000000000000000000000000)
    0x1d68: v1d68 = CALLER 
    0x1d69: v1d69(0x0) = CONST 
    0x1d6d: MSTORE v1d69(0x0), v1d68
    0x1d6e: v1d6e(0xe) = CONST 
    0x1d71: MSTORE v1d5f(0x20), v1d6e(0xe)
    0x1d74: v1d74 = SHA3 v1d69(0x0), v1d31(0x40)
    0x1d77: MSTORE v1d69(0x0), v71a
    0x1d7a: MSTORE v1d5f(0x20), v1d74
    0x1d7e: v1d7e = SHA3 v1d69(0x0), v1d31(0x40)
    0x1d7f: v1d7f = SLOAD v1d7e
    0x1d80: v1d80(0x1d8a) = CONST 
    0x1d86: v1d86(0x2632) = CONST 
    0x1d89: v1d89_0 = CALLPRIVATE v1d86(0x2632), v1d34, v720, v1d7f, v1d80(0x1d8a)

    Begin block 0x1d8a
    prev=[0x1d2e], succ=[0x1db2]
    =================================
    0x1d8b: v1d8b = CALLER 
    0x1d8c: v1d8c(0x0) = CONST 
    0x1d90: MSTORE v1d8c(0x0), v1d8b
    0x1d91: v1d91(0xe) = CONST 
    0x1d93: v1d93(0x20) = CONST 
    0x1d97: MSTORE v1d93(0x20), v1d91(0xe)
    0x1d98: v1d98(0x40) = CONST 
    0x1d9c: v1d9c = SHA3 v1d8c(0x0), v1d98(0x40)
    0x1d9f: MSTORE v1d8c(0x0), v71a
    0x1da2: MSTORE v1d93(0x20), v1d9c
    0x1da4: v1da4 = SHA3 v1d8c(0x0), v1d98(0x40)
    0x1da5: SSTORE v1da4, v1d89_0
    0x1da6: v1da6(0x8) = CONST 
    0x1da8: v1da8 = SLOAD v1da6(0x8)
    0x1da9: v1da9(0x1db2) = CONST 
    0x1dae: v1dae(0x2476) = CONST 
    0x1db1: v1db1_0 = CALLPRIVATE v1dae(0x2476), v720, v1da8, v1da9(0x1db2)

    Begin block 0x1db2
    prev=[0x1d8a], succ=[0x1dbf]
    =================================
    0x1db3: v1db3(0x8) = CONST 
    0x1db5: SSTORE v1db3(0x8), v1db1_0
    0x1db6: v1db6(0x0) = CONST 
    0x1db8: v1db8(0x1dbf) = CONST 
    0x1dbb: v1dbb(0x1719) = CONST 
    0x1dbe: v1dbe_0 = CALLPRIVATE v1dbb(0x1719), v1db8(0x1dbf)

    Begin block 0x1dbf
    prev=[0x1db2], succ=[0x1ddb]
    =================================
    0x1dc0: v1dc0(0x0) = CONST 
    0x1dc4: MSTORE v1dc0(0x0), v1dbe_0
    0x1dc5: v1dc5(0x10) = CONST 
    0x1dc7: v1dc7(0x20) = CONST 
    0x1dc9: MSTORE v1dc7(0x20), v1dc5(0x10)
    0x1dca: v1dca(0x40) = CONST 
    0x1dcd: v1dcd = SHA3 v1dc0(0x0), v1dca(0x40)
    0x1dce: v1dce = SLOAD v1dcd
    0x1dd2: v1dd2(0x1ddb) = CONST 
    0x1dd7: v1dd7(0x2476) = CONST 
    0x1dda: v1dda_0 = CALLPRIVATE v1dd7(0x2476), v720, v1dce, v1dd2(0x1ddb)

    Begin block 0x1ddb
    prev=[0x1dbf], succ=[0x1df2]
    =================================
    0x1ddc: v1ddc(0x0) = CONST 
    0x1de0: MSTORE v1ddc(0x0), v1dbe_0
    0x1de1: v1de1(0x10) = CONST 
    0x1de3: v1de3(0x20) = CONST 
    0x1de5: MSTORE v1de3(0x20), v1de1(0x10)
    0x1de6: v1de6(0x40) = CONST 
    0x1de9: v1de9 = SHA3 v1ddc(0x0), v1de6(0x40)
    0x1dea: SSTORE v1de9, v1dda_0
    0x1deb: v1deb(0x1df2) = CONST 
    0x1dee: v1dee(0x25b5) = CONST 
    0x1df1: CALLPRIVATE v1dee(0x25b5), v1deb(0x1df2)

    Begin block 0x1df2
    prev=[0x1ddb], succ=[0x3300x701]
    =================================
    0x1df3: v1df3(0x40) = CONST 
    0x1df6: v1df6 = MLOAD v1df3(0x40)
    0x1df9: MSTORE v1df6, v1dbe_0
    0x1dfa: v1dfa(0x20) = CONST 
    0x1dfd: v1dfd = ADD v1df6, v1dfa(0x20)
    0x1e00: MSTORE v1dfd, v71a
    0x1e03: v1e03 = ADD v1df3(0x40), v1df6
    0x1e06: MSTORE v1e03, v381f_0
    0x1e07: v1e07(0x60) = CONST 
    0x1e0a: v1e0a = ADD v1df6, v1e07(0x60)
    0x1e0d: MSTORE v1e0a, v720
    0x1e0f: v1e0f = MLOAD v1df3(0x40)
    0x1e10: v1e10 = CALLER 
    0x1e12: v1e12(0xb5e7fa60bdf74ffc7e542c61b550354c38e19b153814e6089dbaf3bbd7ae59b) = CONST 
    0x1e37: v1e37(0x0) = SUB v1df6, v1e0f
    0x1e38: v1e38(0x80) = CONST 
    0x1e3a: v1e3a(0x80) = ADD v1e38(0x80), v1e37(0x0)
    0x1e3c: LOG2 v1e0f, v1e3a(0x80), v1e12(0xb5e7fa60bdf74ffc7e542c61b550354c38e19b153814e6089dbaf3bbd7ae59b), v1e10
    0x1e3f: v1e3f = NUMBER 
    0x1e40: v1e40(0x0) = CONST 
    0x1e44: MSTORE v1e40(0x0), v1e3f
    0x1e45: v1e45(0x20) = CONST 
    0x1e49: MSTORE v1e45(0x20), v1e40(0x0)
    0x1e4a: v1e4a(0x40) = CONST 
    0x1e4e: v1e4e = SHA3 v1e40(0x0), v1e4a(0x40)
    0x1e4f: v1e4f = ORIGIN 
    0x1e51: MSTORE v1e40(0x0), v1e4f
    0x1e54: MSTORE v1e45(0x20), v1e4e
    0x1e57: v1e57 = SHA3 v1e40(0x0), v1e4a(0x40)
    0x1e59: v1e59 = SLOAD v1e57
    0x1e5a: v1e5a(0x1) = CONST 
    0x1e5c: v1e5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x1e7f: v1e7f = AND v1e5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1e59
    0x1e81: v1e81 = OR v1e5a(0x1), v1e7f
    0x1e84: SSTORE v1e57, v1e81
    0x1e85: v1e85 = CALLER 
    0x1e87: MSTORE v1e40(0x0), v1e85
    0x1e8b: v1e8b = SHA3 v1e40(0x0), v1e4a(0x40)
    0x1e8d: v1e8d = SLOAD v1e8b
    0x1e90: v1e90 = AND v1e5c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1e8d
    0x1e93: v1e93 = OR v1e5a(0x1), v1e90
    0x1e95: SSTORE v1e8b, v1e93
    0x1e9c: JUMP v702(0x330)

    Begin block 0x3300x701
    prev=[0x1df2], succ=[]
    =================================
    0x3310x701: STOP 

}

function initialize(address,address,address)() public {
    Begin block 0x72a
    prev=[], succ=[0x73c, 0x740]
    =================================
    0x72b: v72b(0x359b) = CONST 
    0x72e: v72e(0x4) = CONST 
    0x731: v731 = CALLDATASIZE 
    0x732: v732 = SUB v731, v72e(0x4)
    0x733: v733(0x60) = CONST 
    0x736: v736 = LT v732, v733(0x60)
    0x737: v737 = ISZERO v736
    0x738: v738(0x740) = CONST 
    0x73b: JUMPI v738(0x740), v737

    Begin block 0x73c
    prev=[0x72a], succ=[]
    =================================
    0x73c: v73c(0x0) = CONST 
    0x73f: REVERT v73c(0x0), v73c(0x0)

    Begin block 0x740
    prev=[0x72a], succ=[0x1e9d]
    =================================
    0x742: v742(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x758: v758 = CALLDATALOAD v72e(0x4)
    0x75a: v75a = AND v742(0xffffffffffffffffffffffffffffffffffffffff), v758
    0x75c: v75c(0x20) = CONST 
    0x75f: v75f(0x24) = ADD v72e(0x4), v75c(0x20)
    0x760: v760 = CALLDATALOAD v75f(0x24)
    0x762: v762 = AND v742(0xffffffffffffffffffffffffffffffffffffffff), v760
    0x764: v764(0x40) = CONST 
    0x768: v768(0x44) = ADD v72e(0x4), v764(0x40)
    0x769: v769 = CALLDATALOAD v768(0x44)
    0x76a: v76a = AND v769, v742(0xffffffffffffffffffffffffffffffffffffffff)
    0x76b: v76b(0x1e9d) = CONST 
    0x76e: JUMP v76b(0x1e9d)

    Begin block 0x1e9d
    prev=[0x740], succ=[0x1ec1, 0x1f11]
    =================================
    0x1e9e: v1e9e(0x1) = CONST 
    0x1ea0: v1ea0 = SLOAD v1e9e(0x1)
    0x1ea1: v1ea1(0x10000000000000000000000000000000000000000) = CONST 
    0x1eb8: v1eb8 = DIV v1ea0, v1ea1(0x10000000000000000000000000000000000000000)
    0x1eb9: v1eb9(0xff) = CONST 
    0x1ebb: v1ebb = AND v1eb9(0xff), v1eb8
    0x1ebc: v1ebc = ISZERO v1ebb
    0x1ebd: v1ebd(0x1f11) = CONST 
    0x1ec0: JUMPI v1ebd(0x1f11), v1ebc

    Begin block 0x1ec1
    prev=[0x1e9d], succ=[]
    =================================
    0x1ec1: v1ec1(0x40) = CONST 
    0x1ec3: v1ec3 = MLOAD v1ec1(0x40)
    0x1ec4: v1ec4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1ee6: MSTORE v1ec3, v1ec4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ee7: v1ee7(0x4) = CONST 
    0x1ee9: v1ee9 = ADD v1ee7(0x4), v1ec3
    0x1eec: v1eec(0x20) = CONST 
    0x1eee: v1eee = ADD v1eec(0x20), v1ee9
    0x1ef1: v1ef1(0x20) = SUB v1eee, v1ee9
    0x1ef3: MSTORE v1ee9, v1ef1(0x20)
    0x1ef4: v1ef4(0x21) = CONST 
    0x1ef7: MSTORE v1eee, v1ef4(0x21)
    0x1ef8: v1ef8(0x20) = CONST 
    0x1efa: v1efa = ADD v1ef8(0x20), v1eee
    0x1efc: v1efc(0x2c21) = CONST 
    0x1eff: v1eff(0x21) = CONST 
    0x1f02: CODECOPY v1efa, v1efc(0x2c21), v1eff(0x21)
    0x1f03: v1f03(0x40) = CONST 
    0x1f05: v1f05 = ADD v1f03(0x40), v1efa
    0x1f09: v1f09(0x40) = CONST 
    0x1f0b: v1f0b = MLOAD v1f09(0x40)
    0x1f0e: v1f0e(0x84) = SUB v1f05, v1f0b
    0x1f10: REVERT v1f0b, v1f0e(0x84)

    Begin block 0x1f11
    prev=[0x1e9d], succ=[0x359b]
    =================================
    0x1f12: v1f12(0x2) = CONST 
    0x1f15: v1f15 = SLOAD v1f12(0x2)
    0x1f16: v1f16(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f2d: v1f2d = AND v75a, v1f16(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f2e: v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1f51: v1f51 = AND v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f15
    0x1f52: v1f52 = OR v1f51, v1f2d
    0x1f55: SSTORE v1f12(0x2), v1f52
    0x1f56: v1f56(0x3) = CONST 
    0x1f59: v1f59 = SLOAD v1f56(0x3)
    0x1f5c: v1f5c = AND v1f16(0xffffffffffffffffffffffffffffffffffffffff), v762
    0x1f5f: v1f5f = AND v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f59
    0x1f60: v1f60 = OR v1f5f, v1f5c
    0x1f62: SSTORE v1f56(0x3), v1f60
    0x1f63: v1f63(0x4) = CONST 
    0x1f66: v1f66 = SLOAD v1f63(0x4)
    0x1f69: v1f69 = AND v76a, v1f16(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f6c: v1f6c = AND v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f66
    0x1f70: v1f70 = OR v1f6c, v1f69
    0x1f73: SSTORE v1f63(0x4), v1f70
    0x1f74: v1f74(0x5) = CONST 
    0x1f77: v1f77 = SLOAD v1f74(0x5)
    0x1f79: v1f79 = AND v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1f77
    0x1f7a: v1f7a(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = CONST 
    0x1f8f: v1f8f = OR v1f7a(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2), v1f79
    0x1f91: SSTORE v1f74(0x5), v1f8f
    0x1f92: v1f92(0x0) = CONST 
    0x1f94: v1f94(0x6) = CONST 
    0x1f98: SSTORE v1f94(0x6), v1f92(0x0)
    0x1f99: v1f99(0x7) = CONST 
    0x1f9d: SSTORE v1f99(0x7), v1f92(0x0)
    0x1f9e: v1f9e(0x8) = CONST 
    0x1fa0: SSTORE v1f9e(0x8), v1f92(0x0)
    0x1fa1: v1fa1(0x120a871cc0020000) = CONST 
    0x1faa: v1faa(0xa) = CONST 
    0x1fae: SSTORE v1faa(0xa), v1fa1(0x120a871cc0020000)
    0x1faf: v1faf(0xc) = CONST 
    0x1fb1: SSTORE v1faf(0xc), v1fa1(0x120a871cc0020000)
    0x1fb2: v1fb2(0xbb8) = CONST 
    0x1fb5: v1fb5(0x9) = CONST 
    0x1fb9: SSTORE v1fb5(0x9), v1fb2(0xbb8)
    0x1fba: v1fba(0xb) = CONST 
    0x1fbc: SSTORE v1fba(0xb), v1fb2(0xbb8)
    0x1fbd: v1fbd(0x12c) = CONST 
    0x1fc0: v1fc0(0xd) = CONST 
    0x1fc2: SSTORE v1fc0(0xd), v1fbd(0x12c)
    0x1fc3: v1fc3(0x1) = CONST 
    0x1fc6: v1fc6 = SLOAD v1fc3(0x1)
    0x1fc7: v1fc7(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1fe8: v1fe8 = AND v1fc7(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v1fc6
    0x1fe9: v1fe9(0x10000000000000000000000000000000000000000) = CONST 
    0x1fff: v1fff = OR v1fe9(0x10000000000000000000000000000000000000000), v1fe8
    0x2002: v2002 = AND v1f2e(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1fff
    0x2003: v2003 = CALLER 
    0x2006: v2006 = OR v2003, v2002
    0x2009: SSTORE v1fc3(0x1), v2006
    0x200a: v200a(0x40) = CONST 
    0x200d: v200d = MLOAD v200a(0x40)
    0x200e: v200e = NUMBER 
    0x2010: MSTORE v200d, v200e
    0x2012: v2012 = MLOAD v200a(0x40)
    0x2013: v2013(0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79) = CONST 
    0x2037: v2037(0x0) = SUB v200d, v2012
    0x2038: v2038(0x20) = CONST 
    0x203a: v203a(0x20) = ADD v2038(0x20), v2037(0x0)
    0x203c: LOG2 v2012, v203a(0x20), v2013(0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79), v2003
    0x2040: JUMP v72b(0x359b)

    Begin block 0x359b
    prev=[0x1f11], succ=[]
    =================================
    0x359c: STOP 

}

function couponIssued()() public {
    Begin block 0x76f
    prev=[], succ=[0x2041]
    =================================
    0x770: v770(0x35bc) = CONST 
    0x773: v773(0x2041) = CONST 
    0x776: JUMP v773(0x2041)

    Begin block 0x2041
    prev=[0x76f], succ=[0x35bc]
    =================================
    0x2042: v2042(0x7) = CONST 
    0x2044: v2044 = SLOAD v2042(0x7)
    0x2046: JUMP v770(0x35bc)

    Begin block 0x35bc
    prev=[0x2041], succ=[]
    =================================
    0x35bd: v35bd(0x40) = CONST 
    0x35c0: v35c0 = MLOAD v35bd(0x40)
    0x35c3: MSTORE v35c0, v2044
    0x35c4: v35c4 = MLOAD v35bd(0x40)
    0x35c8: v35c8(0x0) = SUB v35c0, v35c4
    0x35c9: v35c9(0x20) = CONST 
    0x35cb: v35cb(0x20) = ADD v35c9(0x20), v35c8(0x0)
    0x35cd: RETURN v35c4, v35cb(0x20)

}

function nextEpochPoint()() public {
    Begin block 0x777
    prev=[], succ=[0x2047B0x777]
    =================================
    0x778: v778(0x35ed) = CONST 
    0x77b: v77b(0x2047) = CONST 
    0x77e: JUMP v77b(0x2047)

    Begin block 0x2047B0x777
    prev=[0x777], succ=[0x20aeB0x777, 0x80a0x2047B0x777]
    =================================
    0x2048S0x777: v2048V777(0x3) = CONST 
    0x204aS0x777: v204aV777 = SLOAD v2048V777(0x3)
    0x204bS0x777: v204bV777(0x40) = CONST 
    0x204eS0x777: v204eV777 = MLOAD v204bV777(0x40)
    0x204fS0x777: v204fV777(0xc5967c2600000000000000000000000000000000000000000000000000000000) = CONST 
    0x2071S0x777: MSTORE v204eV777, v204fV777(0xc5967c2600000000000000000000000000000000000000000000000000000000)
    0x2073S0x777: v2073V777 = MLOAD v204bV777(0x40)
    0x2074S0x777: v2074V777(0x0) = CONST 
    0x2077S0x777: v2077V777(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x208cS0x777: v208cV777 = AND v2077V777(0xffffffffffffffffffffffffffffffffffffffff), v204aV777
    0x208eS0x777: v208eV777(0xc5967c26) = CONST 
    0x2094S0x777: v2094V777(0x4) = CONST 
    0x2098S0x777: v2098V777 = ADD v204eV777, v2094V777(0x4)
    0x209aS0x777: v209aV777(0x20) = CONST 
    0x20a1S0x777: v20a1V777(0x0) = SUB v204eV777, v2073V777
    0x20a2S0x777: v20a2V777(0x4) = ADD v20a1V777(0x0), v2094V777(0x4)
    0x20a6S0x777: v20a6V777 = EXTCODESIZE v208cV777
    0x20a7S0x777: v20a7V777 = ISZERO v20a6V777
    0x20a9S0x777: v20a9V777 = ISZERO v20a7V777
    0x20aaS0x777: v20aaV777(0x80a) = CONST 
    0x20adS0x777: JUMPI v20aaV777(0x80a), v20a9V777

    Begin block 0x20aeB0x777
    prev=[0x2047B0x777], succ=[]
    =================================
    0x20aeS0x777: v20aeV777(0x0) = CONST 
    0x20b1S0x777: REVERT v20aeV777(0x0), v20aeV777(0x0)

    Begin block 0x80a0x2047B0x777
    prev=[0x2047B0x777], succ=[0x8150x2047B0x777, 0x81e0x2047B0x777]
    =================================
    0x80c0x2047S0x777: v204780cV777 = GAS 
    0x80d0x2047S0x777: v204780dV777 = STATICCALL v204780cV777, v208cV777, v2073V777, v20a2V777(0x4), v2073V777, v209aV777(0x20)
    0x80e0x2047S0x777: v204780eV777 = ISZERO v204780dV777
    0x8100x2047S0x777: v2047810V777 = ISZERO v204780eV777
    0x8110x2047S0x777: v2047811V777(0x81e) = CONST 
    0x8140x2047S0x777: JUMPI v2047811V777(0x81e), v2047810V777

    Begin block 0x8150x2047B0x777
    prev=[0x80a0x2047B0x777], succ=[]
    =================================
    0x8150x2047S0x777: v2047815V777 = RETURNDATASIZE 
    0x8160x2047S0x777: v2047816V777(0x0) = CONST 
    0x8190x2047S0x777: RETURNDATACOPY v2047816V777(0x0), v2047816V777(0x0), v2047815V777
    0x81a0x2047S0x777: v204781aV777 = RETURNDATASIZE 
    0x81b0x2047S0x777: v204781bV777(0x0) = CONST 
    0x81d0x2047S0x777: REVERT v204781bV777(0x0), v204781aV777

    Begin block 0x81e0x2047B0x777
    prev=[0x80a0x2047B0x777], succ=[0x8300x2047B0x777, 0x8340x2047B0x777]
    =================================
    0x8230x2047S0x777: v2047823V777(0x40) = CONST 
    0x8250x2047S0x777: v2047825V777 = MLOAD v2047823V777(0x40)
    0x8260x2047S0x777: v2047826V777 = RETURNDATASIZE 
    0x8270x2047S0x777: v2047827V777(0x20) = CONST 
    0x82a0x2047S0x777: v204782aV777 = LT v2047826V777, v2047827V777(0x20)
    0x82b0x2047S0x777: v204782bV777 = ISZERO v204782aV777
    0x82c0x2047S0x777: v204782cV777(0x834) = CONST 
    0x82f0x2047S0x777: JUMPI v204782cV777(0x834), v204782bV777

    Begin block 0x8300x2047B0x777
    prev=[0x81e0x2047B0x777], succ=[]
    =================================
    0x8300x2047S0x777: v2047830V777(0x0) = CONST 
    0x8330x2047S0x777: REVERT v2047830V777(0x0), v2047830V777(0x0)

    Begin block 0x8340x2047B0x777
    prev=[0x81e0x2047B0x777], succ=[0x8390x2047B0x777]
    =================================
    0x8360x2047S0x777: v2047836V777 = MLOAD v2047825V777

    Begin block 0x8390x2047B0x777
    prev=[0x8340x2047B0x777], succ=[0x35ed]
    =================================
    0x83b0x2047S0x777: JUMP v778(0x35ed)

    Begin block 0x35ed
    prev=[0x8390x2047B0x777], succ=[]
    =================================
    0x35ee: v35ee(0x40) = CONST 
    0x35f1: v35f1 = MLOAD v35ee(0x40)
    0x35f4: MSTORE v35f1, v2047836V777
    0x35f5: v35f5 = MLOAD v35ee(0x40)
    0x35f9: v35f9(0x0) = SUB v35f1, v35f5
    0x35fa: v35fa(0x20) = CONST 
    0x35fc: v35fc(0x20) = ADD v35fa(0x20), v35f9(0x0)
    0x35fe: RETURN v35f5, v35fc(0x20)

}

function getDollarUpdatedPrice()() public {
    Begin block 0x77f
    prev=[], succ=[0x361e]
    =================================
    0x780: v780(0x361e) = CONST 
    0x783: v783(0x20b2) = CONST 
    0x786: v786_0 = CALLPRIVATE v783(0x20b2), v780(0x361e)

    Begin block 0x361e
    prev=[0x77f], succ=[]
    =================================
    0x361f: v361f(0x40) = CONST 
    0x3622: v3622 = MLOAD v361f(0x40)
    0x3625: MSTORE v3622, v786_0
    0x3626: v3626 = MLOAD v361f(0x40)
    0x362a: v362a(0x0) = SUB v3622, v3626
    0x362b: v362b(0x20) = CONST 
    0x362d: v362d(0x20) = ADD v362b(0x20), v362a(0x0)
    0x362f: RETURN v3626, v362d(0x20)

}

function premiumPercent()() public {
    Begin block 0x787
    prev=[], succ=[0x21bd]
    =================================
    0x788: v788(0x364f) = CONST 
    0x78b: v78b(0x21bd) = CONST 
    0x78e: JUMP v78b(0x21bd)

    Begin block 0x21bd
    prev=[0x787], succ=[0x364f]
    =================================
    0x21be: v21be(0xb) = CONST 
    0x21c0: v21c0 = SLOAD v21be(0xb)
    0x21c2: JUMP v788(0x364f)

    Begin block 0x364f
    prev=[0x21bd], succ=[]
    =================================
    0x3650: v3650(0x40) = CONST 
    0x3653: v3653 = MLOAD v3650(0x40)
    0x3656: MSTORE v3653, v21c0
    0x3657: v3657 = MLOAD v3650(0x40)
    0x365b: v365b(0x0) = SUB v3653, v3657
    0x365c: v365c(0x20) = CONST 
    0x365e: v365e(0x20) = ADD v365c(0x20), v365b(0x0)
    0x3660: RETURN v3657, v365e(0x20)

}

function getCouponDiscountRate()() public {
    Begin block 0x78f
    prev=[], succ=[0x3010x78f]
    =================================
    0x790: v790(0x301) = CONST 
    0x793: v793(0x21c3) = CONST 
    0x796: v796_0 = CALLPRIVATE v793(0x21c3), v790(0x301)

    Begin block 0x3010x78f
    prev=[0x78f], succ=[]
    =================================
    0x3020x78f: v78f302(0x40) = CONST 
    0x3050x78f: v78f305 = MLOAD v78f302(0x40)
    0x3080x78f: MSTORE v78f305, v796_0
    0x3090x78f: v78f309 = MLOAD v78f302(0x40)
    0x30d0x78f: v78f30d(0x0) = SUB v78f305, v78f309
    0x30e0x78f: v78f30e(0x20) = CONST 
    0x3100x78f: v78f310(0x20) = ADD v78f30e(0x20), v78f30d(0x0)
    0x3120x78f: RETURN v78f309, v78f310(0x20)

}

function getDollarPrice()() public {
    Begin block 0x797
    prev=[], succ=[0x3680]
    =================================
    0x798: v798(0x3680) = CONST 
    0x79b: v79b(0x2272) = CONST 
    0x79e: v79e_0 = CALLPRIVATE v79b(0x2272), v798(0x3680)

    Begin block 0x3680
    prev=[0x797], succ=[]
    =================================
    0x3681: v3681(0x40) = CONST 
    0x3684: v3684 = MLOAD v3681(0x40)
    0x3687: MSTORE v3684, v79e_0
    0x3688: v3688 = MLOAD v3681(0x40)
    0x368c: v368c(0x0) = SUB v3684, v3688
    0x368d: v368d(0x20) = CONST 
    0x368f: v368f(0x20) = ADD v368d(0x20), v368c(0x0)
    0x3691: RETURN v3688, v368f(0x20)

}

function 0xc92(0xc92arg0x0) private {
    Begin block 0xc92
    prev=[], succ=[0xc9d]
    =================================
    0xc93: vc93(0x0) = CONST 
    0xc96: vc96(0xc9d) = CONST 
    0xc99: vc99(0x20b2) = CONST 
    0xc9c: vc9c_0 = CALLPRIVATE vc99(0x20b2), vc96(0xc9d)

    Begin block 0xc9d
    prev=[0xc92], succ=[0xcaf, 0x36b1]
    =================================
    0xca0: vca0(0xde0b6b3a7640000) = CONST 
    0xcaa: vcaa = LT vc9c_0, vca0(0xde0b6b3a7640000)
    0xcab: vcab(0x36b1) = CONST 
    0xcae: JUMPI vcab(0x36b1), vcaa

    Begin block 0xcaf
    prev=[0xc9d], succ=[0xcb6, 0xcc5]
    =================================
    0xcaf: vcaf(0xb) = CONST 
    0xcb1: vcb1 = SLOAD vcaf(0xb)
    0xcb2: vcb2(0xcc5) = CONST 
    0xcb5: JUMPI vcb2(0xcc5), vcb1

    Begin block 0xcb6
    prev=[0xcaf], succ=[0x36d4]
    =================================
    0xcb6: vcb6(0xde0b6b3a7640000) = CONST 
    0xcc1: vcc1(0x36d4) = CONST 
    0xcc4: JUMP vcc1(0x36d4)

    Begin block 0x36d4
    prev=[0xcb6], succ=[]
    =================================
    0x36d7: RETURNPRIVATE vc92arg0, vcb6(0xde0b6b3a7640000)

    Begin block 0xcc5
    prev=[0xcaf], succ=[0x2376B0xcc5]
    =================================
    0xcc6: vcc6(0x0) = CONST 
    0xcc8: vcc8(0xcfa) = CONST 
    0xccb: vccb(0x2710) = CONST 
    0xcce: vcce(0x36f7) = CONST 
    0xcd1: vcd1(0xb) = CONST 
    0xcd3: vcd3 = SLOAD vcd1(0xb)
    0xcd4: vcd4(0x371c) = CONST 
    0xcd7: vcd7(0xde0b6b3a7640000) = CONST 
    0xce1: vce1(0x2376) = CONST 
    0xce7: vce7(0xffffffff) = CONST 
    0xcec: vcec(0x2376) = AND vce7(0xffffffff), vce1(0x2376)
    0xced: JUMP vcec(0x2376)

    Begin block 0x2376B0xcc5
    prev=[0xcc5], succ=[0x23b80x2376B0xcc5]
    =================================
    0x2377S0xcc5: v2377Vcc5(0x0) = CONST 
    0x2379S0xcc5: v2379Vcc5(0x23b8) = CONST 
    0x237eS0xcc5: v237eVcc5(0x40) = CONST 
    0x2380S0xcc5: v2380Vcc5 = MLOAD v237eVcc5(0x40)
    0x2382S0xcc5: v2382Vcc5(0x40) = CONST 
    0x2384S0xcc5: v2384Vcc5 = ADD v2382Vcc5(0x40), v2380Vcc5
    0x2385S0xcc5: v2385Vcc5(0x40) = CONST 
    0x2387S0xcc5: MSTORE v2385Vcc5(0x40), v2384Vcc5
    0x2389S0xcc5: v2389Vcc5(0x1e) = CONST 
    0x238cS0xcc5: MSTORE v2380Vcc5, v2389Vcc5(0x1e)
    0x238dS0xcc5: v238dVcc5(0x20) = CONST 
    0x238fS0xcc5: v238fVcc5 = ADD v238dVcc5(0x20), v2380Vcc5
    0x2390S0xcc5: v2390Vcc5(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x23b2S0xcc5: MSTORE v238fVcc5, v2390Vcc5(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x23b4S0xcc5: v23b4Vcc5(0x2632) = CONST 
    0x23b7S0xcc5: v23b7_0Vcc5 = CALLPRIVATE v23b4Vcc5(0x2632), v2380Vcc5, vcd7(0xde0b6b3a7640000), vc9c_0, v2379Vcc5(0x23b8)

    Begin block 0x23b80x2376B0xcc5
    prev=[0x2376B0xcc5], succ=[0x23bb0x2376B0xcc5]
    =================================

    Begin block 0x23bb0x2376B0xcc5
    prev=[0x23b80x2376B0xcc5], succ=[0x371c]
    =================================
    0x23c00x2376S0xcc5: JUMP vcd4(0x371c)

    Begin block 0x371c
    prev=[0x23bb0x2376B0xcc5], succ=[0x36f7]
    =================================
    0x371e: v371e(0x23c1) = CONST 
    0x3721: v3721_0 = CALLPRIVATE v371e(0x23c1), vcd3, v23b7_0Vcc5, vcce(0x36f7)

    Begin block 0x36f7
    prev=[0x371c], succ=[0xcfa]
    =================================
    0x36f9: v36f9(0x2434) = CONST 
    0x36fc: v36fc_0 = CALLPRIVATE v36f9(0x2434), vccb(0x2710), v3721_0, vcc8(0xcfa)

    Begin block 0xcfa
    prev=[0x36f7], succ=[0xd0e]
    =================================
    0xcfd: vcfd(0xd0e) = CONST 
    0xd00: vd00(0xde0b6b3a7640000) = CONST 
    0xd0a: vd0a(0x2476) = CONST 
    0xd0d: vd0d_0 = CALLPRIVATE vd0a(0x2476), v36fc_0, vd00(0xde0b6b3a7640000), vcfd(0xd0e)

    Begin block 0xd0e
    prev=[0xcfa], succ=[0xd22, 0xd1e]
    =================================
    0xd0f: vd0f(0xc) = CONST 
    0xd11: vd11 = SLOAD vd0f(0xc)
    0xd16: vd16 = ISZERO vd11
    0xd18: vd18 = ISZERO vd16
    0xd1a: vd1a(0xd22) = CONST 
    0xd1d: JUMPI vd1a(0xd22), vd16

    Begin block 0xd22
    prev=[0xd0e, 0xd1e], succ=[0xd2b, 0xd28]
    =================================
    0xd22_0x0: vd22_0 = PHI vd18, vd21
    0xd23: vd23 = ISZERO vd22_0
    0xd24: vd24(0xd2b) = CONST 
    0xd27: JUMPI vd24(0xd2b), vd23

    Begin block 0xd2b
    prev=[0xd22, 0xd28], succ=[0xd2e]
    =================================

    Begin block 0xd2e
    prev=[0xd2b], succ=[]
    =================================
    0xd2e_0x1: vd2e_1 = PHI vd11, vd0d_0
    0xd31: RETURNPRIVATE vc92arg0, vd2e_1

    Begin block 0xd28
    prev=[0xd22], succ=[0xd2b]
    =================================

    Begin block 0xd1e
    prev=[0xd0e], succ=[0xd22]
    =================================
    0xd21: vd21 = GT vd0d_0, vd11

    Begin block 0x36b1
    prev=[0xc9d], succ=[]
    =================================
    0x36b4: RETURNPRIVATE vc92arg0, vc93(0x0)

}

