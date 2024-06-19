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
    prev=[0x0], succ=[0x1a, 0x40f8]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x3ff7: v3ff7(0x40f8) = CONST 
    0x3ff8: JUMPI v3ff7(0x40f8), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x1bd, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x691be4d8) = CONST 
    0x26: v26 = GT v21(0x691be4d8), v1f
    0x27: v27(0x1bd) = CONST 
    0x2a: JUMPI v27(0x1bd), v26

    Begin block 0x1bd
    prev=[0x1a], succ=[0x28c, 0x1c9]
    =================================
    0x1bf: v1bf(0x2c56320f) = CONST 
    0x1c4: v1c4 = GT v1bf(0x2c56320f), v1f
    0x1c5: v1c5(0x28c) = CONST 
    0x1c8: JUMPI v1c5(0x28c), v1c4

    Begin block 0x28c
    prev=[0x1bd], succ=[0x2ee, 0x298]
    =================================
    0x28e: v28e(0x19cd47f9) = CONST 
    0x293: v293 = GT v28e(0x19cd47f9), v1f
    0x294: v294(0x2ee) = CONST 
    0x297: JUMPI v294(0x2ee), v293

    Begin block 0x2ee
    prev=[0x28c], succ=[0x31f, 0x2fa]
    =================================
    0x2f0: v2f0(0x158ef93e) = CONST 
    0x2f5: v2f5 = GT v2f0(0x158ef93e), v1f
    0x2f6: v2f6(0x31f) = CONST 
    0x2f9: JUMPI v2f6(0x31f), v2f5

    Begin block 0x31f
    prev=[0x2ee], succ=[0x405f, 0x32b]
    =================================
    0x321: v321(0x7284ce9) = CONST 
    0x326: v326 = EQ v321(0x7284ce9), v1f
    0x4059: v4059(0x405f) = CONST 
    0x405a: JUMPI v4059(0x405f), v326

    Begin block 0x405f
    prev=[0x31f], succ=[]
    =================================
    0x4060: v4060(0x346) = CONST 
    0x4061: CALLPRIVATE v4060(0x346)

    Begin block 0x32b
    prev=[0x31f], succ=[0x4062, 0x336]
    =================================
    0x32c: v32c(0x108b54b9) = CONST 
    0x331: v331 = EQ v32c(0x108b54b9), v1f
    0x405b: v405b(0x4062) = CONST 
    0x405c: JUMPI v405b(0x4062), v331

    Begin block 0x4062
    prev=[0x32b], succ=[]
    =================================
    0x4063: v4063(0x360) = CONST 
    0x4064: CALLPRIVATE v4063(0x360)

    Begin block 0x336
    prev=[0x32b], succ=[0x4065, 0x341]
    =================================
    0x337: v337(0x154ec2db) = CONST 
    0x33c: v33c = EQ v337(0x154ec2db), v1f
    0x405d: v405d(0x4065) = CONST 
    0x405e: JUMPI v405d(0x4065), v33c

    Begin block 0x4065
    prev=[0x336], succ=[]
    =================================
    0x4066: v4066(0x37f) = CONST 
    0x4067: CALLPRIVATE v4066(0x37f)

    Begin block 0x341
    prev=[0x336], succ=[]
    =================================
    0x342: v342(0x0) = CONST 
    0x345: REVERT v342(0x0), v342(0x0)

    Begin block 0x2fa
    prev=[0x2ee], succ=[0x4068, 0x305]
    =================================
    0x2fb: v2fb(0x158ef93e) = CONST 
    0x300: v300 = EQ v2fb(0x158ef93e), v1f
    0x4053: v4053(0x4068) = CONST 
    0x4054: JUMPI v4053(0x4068), v300

    Begin block 0x4068
    prev=[0x2fa], succ=[]
    =================================
    0x4069: v4069(0x39c) = CONST 
    0x406a: CALLPRIVATE v4069(0x39c)

    Begin block 0x305
    prev=[0x2fa], succ=[0x406b, 0x310]
    =================================
    0x306: v306(0x18160ddd) = CONST 
    0x30b: v30b = EQ v306(0x18160ddd), v1f
    0x4055: v4055(0x406b) = CONST 
    0x4056: JUMPI v4055(0x406b), v30b

    Begin block 0x406b
    prev=[0x305], succ=[]
    =================================
    0x406c: v406c(0x3b8) = CONST 
    0x406d: CALLPRIVATE v406c(0x3b8)

    Begin block 0x310
    prev=[0x305], succ=[0x31b, 0x406e]
    =================================
    0x311: v311(0x18a98bfb) = CONST 
    0x316: v316 = EQ v311(0x18a98bfb), v1f
    0x4057: v4057(0x406e) = CONST 
    0x4058: JUMPI v4057(0x406e), v316

    Begin block 0x31b
    prev=[0x310], succ=[0x353e]
    =================================
    0x31b: v31b(0x353e) = CONST 
    0x31e: JUMP v31b(0x353e)

    Begin block 0x353e
    prev=[0x31b], succ=[]
    =================================
    0x353f: v353f(0x0) = CONST 
    0x3542: REVERT v353f(0x0), v353f(0x0)

    Begin block 0x406e
    prev=[0x310], succ=[]
    =================================
    0x406f: v406f(0x3c0) = CONST 
    0x4070: CALLPRIVATE v406f(0x3c0)

    Begin block 0x298
    prev=[0x28c], succ=[0x2c8, 0x2a3]
    =================================
    0x299: v299(0x207395b1) = CONST 
    0x29e: v29e = GT v299(0x207395b1), v1f
    0x29f: v29f(0x2c8) = CONST 
    0x2a2: JUMPI v29f(0x2c8), v29e

    Begin block 0x2c8
    prev=[0x298], succ=[0x4071, 0x2d4]
    =================================
    0x2ca: v2ca(0x19cd47f9) = CONST 
    0x2cf: v2cf = EQ v2ca(0x19cd47f9), v1f
    0x404d: v404d(0x4071) = CONST 
    0x404e: JUMPI v404d(0x4071), v2cf

    Begin block 0x4071
    prev=[0x2c8], succ=[]
    =================================
    0x4072: v4072(0x3dd) = CONST 
    0x4073: CALLPRIVATE v4072(0x3dd)

    Begin block 0x2d4
    prev=[0x2c8], succ=[0x4074, 0x2df]
    =================================
    0x2d5: v2d5(0x1a5e2e54) = CONST 
    0x2da: v2da = EQ v2d5(0x1a5e2e54), v1f
    0x404f: v404f(0x4074) = CONST 
    0x4050: JUMPI v404f(0x4074), v2da

    Begin block 0x4074
    prev=[0x2d4], succ=[]
    =================================
    0x4075: v4075(0x3fa) = CONST 
    0x4076: CALLPRIVATE v4075(0x3fa)

    Begin block 0x2df
    prev=[0x2d4], succ=[0x2ea, 0x4077]
    =================================
    0x2e0: v2e0(0x1c9fde7a) = CONST 
    0x2e5: v2e5 = EQ v2e0(0x1c9fde7a), v1f
    0x4051: v4051(0x4077) = CONST 
    0x4052: JUMPI v4051(0x4077), v2e5

    Begin block 0x2ea
    prev=[0x2df], succ=[0x351a]
    =================================
    0x2ea: v2ea(0x351a) = CONST 
    0x2ed: JUMP v2ea(0x351a)

    Begin block 0x351a
    prev=[0x2ea], succ=[]
    =================================
    0x351b: v351b(0x0) = CONST 
    0x351e: REVERT v351b(0x0), v351b(0x0)

    Begin block 0x4077
    prev=[0x2df], succ=[]
    =================================
    0x4078: v4078(0x42d) = CONST 
    0x4079: CALLPRIVATE v4078(0x42d)

    Begin block 0x2a3
    prev=[0x298], succ=[0x407a, 0x2ae]
    =================================
    0x2a4: v2a4(0x207395b1) = CONST 
    0x2a9: v2a9 = EQ v2a4(0x207395b1), v1f
    0x4047: v4047(0x407a) = CONST 
    0x4048: JUMPI v4047(0x407a), v2a9

    Begin block 0x407a
    prev=[0x2a3], succ=[]
    =================================
    0x407b: v407b(0x466) = CONST 
    0x407c: CALLPRIVATE v407b(0x466)

    Begin block 0x2ae
    prev=[0x2a3], succ=[0x407d, 0x2b9]
    =================================
    0x2af: v2af(0x27aac633) = CONST 
    0x2b4: v2b4 = EQ v2af(0x27aac633), v1f
    0x4049: v4049(0x407d) = CONST 
    0x404a: JUMPI v4049(0x407d), v2b4

    Begin block 0x407d
    prev=[0x2ae], succ=[]
    =================================
    0x407e: v407e(0x539) = CONST 
    0x407f: CALLPRIVATE v407e(0x539)

    Begin block 0x2b9
    prev=[0x2ae], succ=[0x2c4, 0x4080]
    =================================
    0x2ba: v2ba(0x29ef1919) = CONST 
    0x2bf: v2bf = EQ v2ba(0x29ef1919), v1f
    0x404b: v404b(0x4080) = CONST 
    0x404c: JUMPI v404b(0x4080), v2bf

    Begin block 0x2c4
    prev=[0x2b9], succ=[0x34f6]
    =================================
    0x2c4: v2c4(0x34f6) = CONST 
    0x2c7: JUMP v2c4(0x34f6)

    Begin block 0x34f6
    prev=[0x2c4], succ=[]
    =================================
    0x34f7: v34f7(0x0) = CONST 
    0x34fa: REVERT v34f7(0x0), v34f7(0x0)

    Begin block 0x4080
    prev=[0x2b9], succ=[]
    =================================
    0x4081: v4081(0x541) = CONST 
    0x4082: CALLPRIVATE v4081(0x541)

    Begin block 0x1c9
    prev=[0x1bd], succ=[0x235, 0x1d4]
    =================================
    0x1ca: v1ca(0x3f53fbec) = CONST 
    0x1cf: v1cf = GT v1ca(0x3f53fbec), v1f
    0x1d0: v1d0(0x235) = CONST 
    0x1d3: JUMPI v1d0(0x235), v1cf

    Begin block 0x235
    prev=[0x1c9], succ=[0x266, 0x241]
    =================================
    0x237: v237(0x392e53cd) = CONST 
    0x23c: v23c = GT v237(0x392e53cd), v1f
    0x23d: v23d(0x266) = CONST 
    0x240: JUMPI v23d(0x266), v23c

    Begin block 0x266
    prev=[0x235], succ=[0x4083, 0x272]
    =================================
    0x268: v268(0x2c56320f) = CONST 
    0x26d: v26d = EQ v268(0x2c56320f), v1f
    0x4041: v4041(0x4083) = CONST 
    0x4042: JUMPI v4041(0x4083), v26d

    Begin block 0x4083
    prev=[0x266], succ=[]
    =================================
    0x4084: v4084(0x549) = CONST 
    0x4085: CALLPRIVATE v4084(0x549)

    Begin block 0x272
    prev=[0x266], succ=[0x4086, 0x27d]
    =================================
    0x273: v273(0x2cf06f1a) = CONST 
    0x278: v278 = EQ v273(0x2cf06f1a), v1f
    0x4043: v4043(0x4086) = CONST 
    0x4044: JUMPI v4043(0x4086), v278

    Begin block 0x4086
    prev=[0x272], succ=[]
    =================================
    0x4087: v4087(0x551) = CONST 
    0x4088: CALLPRIVATE v4087(0x551)

    Begin block 0x27d
    prev=[0x272], succ=[0x288, 0x4089]
    =================================
    0x27e: v27e(0x2e9c7b65) = CONST 
    0x283: v283 = EQ v27e(0x2e9c7b65), v1f
    0x4045: v4045(0x4089) = CONST 
    0x4046: JUMPI v4045(0x4089), v283

    Begin block 0x288
    prev=[0x27d], succ=[0x34d2]
    =================================
    0x288: v288(0x34d2) = CONST 
    0x28b: JUMP v288(0x34d2)

    Begin block 0x34d2
    prev=[0x288], succ=[]
    =================================
    0x34d3: v34d3(0x0) = CONST 
    0x34d6: REVERT v34d3(0x0), v34d3(0x0)

    Begin block 0x4089
    prev=[0x27d], succ=[]
    =================================
    0x408a: v408a(0x56e) = CONST 
    0x408b: CALLPRIVATE v408a(0x56e)

    Begin block 0x241
    prev=[0x235], succ=[0x408c, 0x24c]
    =================================
    0x242: v242(0x392e53cd) = CONST 
    0x247: v247 = EQ v242(0x392e53cd), v1f
    0x403b: v403b(0x408c) = CONST 
    0x403c: JUMPI v403b(0x408c), v247

    Begin block 0x408c
    prev=[0x241], succ=[]
    =================================
    0x408d: v408d(0x576) = CONST 
    0x408e: CALLPRIVATE v408d(0x576)

    Begin block 0x24c
    prev=[0x241], succ=[0x408f, 0x257]
    =================================
    0x24d: v24d(0x3cc3d23b) = CONST 
    0x252: v252 = EQ v24d(0x3cc3d23b), v1f
    0x403d: v403d(0x408f) = CONST 
    0x403e: JUMPI v403d(0x408f), v252

    Begin block 0x408f
    prev=[0x24c], succ=[]
    =================================
    0x4090: v4090(0x57e) = CONST 
    0x4091: CALLPRIVATE v4090(0x57e)

    Begin block 0x257
    prev=[0x24c], succ=[0x262, 0x4092]
    =================================
    0x258: v258(0x3e38fd00) = CONST 
    0x25d: v25d = EQ v258(0x3e38fd00), v1f
    0x403f: v403f(0x4092) = CONST 
    0x4040: JUMPI v403f(0x4092), v25d

    Begin block 0x262
    prev=[0x257], succ=[0x34ae]
    =================================
    0x262: v262(0x34ae) = CONST 
    0x265: JUMP v262(0x34ae)

    Begin block 0x34ae
    prev=[0x262], succ=[]
    =================================
    0x34af: v34af(0x0) = CONST 
    0x34b2: REVERT v34af(0x0), v34af(0x0)

    Begin block 0x4092
    prev=[0x257], succ=[]
    =================================
    0x4093: v4093(0x586) = CONST 
    0x4094: CALLPRIVATE v4093(0x586)

    Begin block 0x1d4
    prev=[0x1c9], succ=[0x20f, 0x1df]
    =================================
    0x1d5: v1d5(0x51adeb57) = CONST 
    0x1da: v1da = GT v1d5(0x51adeb57), v1f
    0x1db: v1db(0x20f) = CONST 
    0x1de: JUMPI v1db(0x20f), v1da

    Begin block 0x20f
    prev=[0x1d4], succ=[0x4095, 0x21b]
    =================================
    0x211: v211(0x3f53fbec) = CONST 
    0x216: v216 = EQ v211(0x3f53fbec), v1f
    0x4035: v4035(0x4095) = CONST 
    0x4036: JUMPI v4035(0x4095), v216

    Begin block 0x4095
    prev=[0x20f], succ=[]
    =================================
    0x4096: v4096(0x5bf) = CONST 
    0x4097: CALLPRIVATE v4096(0x5bf)

    Begin block 0x21b
    prev=[0x20f], succ=[0x4098, 0x226]
    =================================
    0x21c: v21c(0x40af7ba5) = CONST 
    0x221: v221 = EQ v21c(0x40af7ba5), v1f
    0x4037: v4037(0x4098) = CONST 
    0x4038: JUMPI v4037(0x4098), v221

    Begin block 0x4098
    prev=[0x21b], succ=[]
    =================================
    0x4099: v4099(0x5f2) = CONST 
    0x409a: CALLPRIVATE v4099(0x5f2)

    Begin block 0x226
    prev=[0x21b], succ=[0x231, 0x409b]
    =================================
    0x227: v227(0x451111b7) = CONST 
    0x22c: v22c = EQ v227(0x451111b7), v1f
    0x4039: v4039(0x409b) = CONST 
    0x403a: JUMPI v4039(0x409b), v22c

    Begin block 0x231
    prev=[0x226], succ=[0x348a]
    =================================
    0x231: v231(0x348a) = CONST 
    0x234: JUMP v231(0x348a)

    Begin block 0x348a
    prev=[0x231], succ=[]
    =================================
    0x348b: v348b(0x0) = CONST 
    0x348e: REVERT v348b(0x0), v348b(0x0)

    Begin block 0x409b
    prev=[0x226], succ=[]
    =================================
    0x409c: v409c(0x60f) = CONST 
    0x409d: CALLPRIVATE v409c(0x60f)

    Begin block 0x1df
    prev=[0x1d4], succ=[0x409e, 0x1ea]
    =================================
    0x1e0: v1e0(0x51adeb57) = CONST 
    0x1e5: v1e5 = EQ v1e0(0x51adeb57), v1f
    0x402d: v402d(0x409e) = CONST 
    0x402e: JUMPI v402d(0x409e), v1e5

    Begin block 0x409e
    prev=[0x1df], succ=[]
    =================================
    0x409f: v409f(0x640) = CONST 
    0x40a0: CALLPRIVATE v409f(0x640)

    Begin block 0x1ea
    prev=[0x1df], succ=[0x40a1, 0x1f5]
    =================================
    0x1eb: v1eb(0x54575af4) = CONST 
    0x1f0: v1f0 = EQ v1eb(0x54575af4), v1f
    0x402f: v402f(0x40a1) = CONST 
    0x4030: JUMPI v402f(0x40a1), v1f0

    Begin block 0x40a1
    prev=[0x1ea], succ=[]
    =================================
    0x40a2: v40a2(0x648) = CONST 
    0x40a3: CALLPRIVATE v40a2(0x648)

    Begin block 0x1f5
    prev=[0x1ea], succ=[0x40a4, 0x200]
    =================================
    0x1f6: v1f6(0x570ca735) = CONST 
    0x1fb: v1fb = EQ v1f6(0x570ca735), v1f
    0x4031: v4031(0x40a4) = CONST 
    0x4032: JUMPI v4031(0x40a4), v1fb

    Begin block 0x40a4
    prev=[0x1f5], succ=[]
    =================================
    0x40a5: v40a5(0x68b) = CONST 
    0x40a6: CALLPRIVATE v40a5(0x68b)

    Begin block 0x200
    prev=[0x1f5], succ=[0x20b, 0x40a7]
    =================================
    0x201: v201(0x61d027b3) = CONST 
    0x206: v206 = EQ v201(0x61d027b3), v1f
    0x4033: v4033(0x40a7) = CONST 
    0x4034: JUMPI v4033(0x40a7), v206

    Begin block 0x20b
    prev=[0x200], succ=[0x3466]
    =================================
    0x20b: v20b(0x3466) = CONST 
    0x20e: JUMP v20b(0x3466)

    Begin block 0x3466
    prev=[0x20b], succ=[]
    =================================
    0x3467: v3467(0x0) = CONST 
    0x346a: REVERT v3467(0x0), v3467(0x0)

    Begin block 0x40a7
    prev=[0x200], succ=[]
    =================================
    0x40a8: v40a8(0x693) = CONST 
    0x40a9: CALLPRIVATE v40a8(0x693)

    Begin block 0x2b
    prev=[0x1a], succ=[0xf9, 0x36]
    =================================
    0x2c: v2c(0xa688cfd7) = CONST 
    0x31: v31 = GT v2c(0xa688cfd7), v1f
    0x32: v32(0xf9) = CONST 
    0x35: JUMPI v32(0xf9), v31

    Begin block 0xf9
    prev=[0x2b], succ=[0x166, 0x105]
    =================================
    0xfb: vfb(0x900cf0cf) = CONST 
    0x100: v100 = GT vfb(0x900cf0cf), v1f
    0x101: v101(0x166) = CONST 
    0x104: JUMPI v101(0x166), v100

    Begin block 0x166
    prev=[0xf9], succ=[0x197, 0x172]
    =================================
    0x168: v168(0x71bc6a83) = CONST 
    0x16d: v16d = GT v168(0x71bc6a83), v1f
    0x16e: v16e(0x197) = CONST 
    0x171: JUMPI v16e(0x197), v16d

    Begin block 0x197
    prev=[0x166], succ=[0x40aa, 0x1a3]
    =================================
    0x199: v199(0x691be4d8) = CONST 
    0x19e: v19e = EQ v199(0x691be4d8), v1f
    0x4027: v4027(0x40aa) = CONST 
    0x4028: JUMPI v4027(0x40aa), v19e

    Begin block 0x40aa
    prev=[0x197], succ=[]
    =================================
    0x40ab: v40ab(0x69b) = CONST 
    0x40ac: CALLPRIVATE v40ab(0x69b)

    Begin block 0x1a3
    prev=[0x197], succ=[0x40ad, 0x1ae]
    =================================
    0x1a4: v1a4(0x6a1463c8) = CONST 
    0x1a9: v1a9 = EQ v1a4(0x6a1463c8), v1f
    0x4029: v4029(0x40ad) = CONST 
    0x402a: JUMPI v4029(0x40ad), v1a9

    Begin block 0x40ad
    prev=[0x1a3], succ=[]
    =================================
    0x40ae: v40ae(0x6d4) = CONST 
    0x40af: CALLPRIVATE v40ae(0x6d4)

    Begin block 0x1ae
    prev=[0x1a3], succ=[0x1b9, 0x40b0]
    =================================
    0x1af: v1af(0x70a08231) = CONST 
    0x1b4: v1b4 = EQ v1af(0x70a08231), v1f
    0x402b: v402b(0x40b0) = CONST 
    0x402c: JUMPI v402b(0x40b0), v1b4

    Begin block 0x1b9
    prev=[0x1ae], succ=[0x3442]
    =================================
    0x1b9: v1b9(0x3442) = CONST 
    0x1bc: JUMP v1b9(0x3442)

    Begin block 0x3442
    prev=[0x1b9], succ=[]
    =================================
    0x3443: v3443(0x0) = CONST 
    0x3446: REVERT v3443(0x0), v3443(0x0)

    Begin block 0x40b0
    prev=[0x1ae], succ=[]
    =================================
    0x40b1: v40b1(0x6f1) = CONST 
    0x40b2: CALLPRIVATE v40b1(0x6f1)

    Begin block 0x172
    prev=[0x166], succ=[0x40b3, 0x17d]
    =================================
    0x173: v173(0x71bc6a83) = CONST 
    0x178: v178 = EQ v173(0x71bc6a83), v1f
    0x4021: v4021(0x40b3) = CONST 
    0x4022: JUMPI v4021(0x40b3), v178

    Begin block 0x40b3
    prev=[0x172], succ=[]
    =================================
    0x40b4: v40b4(0x724) = CONST 
    0x40b5: CALLPRIVATE v40b4(0x724)

    Begin block 0x17d
    prev=[0x172], succ=[0x40b6, 0x188]
    =================================
    0x17e: v17e(0x8745e2e9) = CONST 
    0x183: v183 = EQ v17e(0x8745e2e9), v1f
    0x4023: v4023(0x40b6) = CONST 
    0x4024: JUMPI v4023(0x40b6), v183

    Begin block 0x40b6
    prev=[0x17d], succ=[]
    =================================
    0x40b7: v40b7(0x747) = CONST 
    0x40b8: CALLPRIVATE v40b7(0x747)

    Begin block 0x188
    prev=[0x17d], succ=[0x193, 0x40b9]
    =================================
    0x189: v189(0x8eda90ad) = CONST 
    0x18e: v18e = EQ v189(0x8eda90ad), v1f
    0x4025: v4025(0x40b9) = CONST 
    0x4026: JUMPI v4025(0x40b9), v18e

    Begin block 0x193
    prev=[0x188], succ=[0x341e]
    =================================
    0x193: v193(0x341e) = CONST 
    0x196: JUMP v193(0x341e)

    Begin block 0x341e
    prev=[0x193], succ=[]
    =================================
    0x341f: v341f(0x0) = CONST 
    0x3422: REVERT v341f(0x0), v341f(0x0)

    Begin block 0x40b9
    prev=[0x188], succ=[]
    =================================
    0x40ba: v40ba(0x74f) = CONST 
    0x40bb: CALLPRIVATE v40ba(0x74f)

    Begin block 0x105
    prev=[0xf9], succ=[0x140, 0x110]
    =================================
    0x106: v106(0x99f85b18) = CONST 
    0x10b: v10b = GT v106(0x99f85b18), v1f
    0x10c: v10c(0x140) = CONST 
    0x10f: JUMPI v10c(0x140), v10b

    Begin block 0x140
    prev=[0x105], succ=[0x40bc, 0x14c]
    =================================
    0x142: v142(0x900cf0cf) = CONST 
    0x147: v147 = EQ v142(0x900cf0cf), v1f
    0x401b: v401b(0x40bc) = CONST 
    0x401c: JUMPI v401b(0x40bc), v147

    Begin block 0x40bc
    prev=[0x140], succ=[]
    =================================
    0x40bd: v40bd(0x757) = CONST 
    0x40be: CALLPRIVATE v40bd(0x757)

    Begin block 0x14c
    prev=[0x140], succ=[0x40bf, 0x157]
    =================================
    0x14d: v14d(0x94bdf63e) = CONST 
    0x152: v152 = EQ v14d(0x94bdf63e), v1f
    0x401d: v401d(0x40bf) = CONST 
    0x401e: JUMPI v401d(0x40bf), v152

    Begin block 0x40bf
    prev=[0x14c], succ=[]
    =================================
    0x40c0: v40c0(0x75f) = CONST 
    0x40c1: CALLPRIVATE v40c0(0x75f)

    Begin block 0x157
    prev=[0x14c], succ=[0x162, 0x40c2]
    =================================
    0x158: v158(0x98b762a1) = CONST 
    0x15d: v15d = EQ v158(0x98b762a1), v1f
    0x401f: v401f(0x40c2) = CONST 
    0x4020: JUMPI v401f(0x40c2), v15d

    Begin block 0x162
    prev=[0x157], succ=[0x33fa]
    =================================
    0x162: v162(0x33fa) = CONST 
    0x165: JUMP v162(0x33fa)

    Begin block 0x33fa
    prev=[0x162], succ=[]
    =================================
    0x33fb: v33fb(0x0) = CONST 
    0x33fe: REVERT v33fb(0x0), v33fb(0x0)

    Begin block 0x40c2
    prev=[0x157], succ=[]
    =================================
    0x40c3: v40c3(0x767) = CONST 
    0x40c4: CALLPRIVATE v40c3(0x767)

    Begin block 0x110
    prev=[0x105], succ=[0x40c5, 0x11b]
    =================================
    0x111: v111(0x99f85b18) = CONST 
    0x116: v116 = EQ v111(0x99f85b18), v1f
    0x4013: v4013(0x40c5) = CONST 
    0x4014: JUMPI v4013(0x40c5), v116

    Begin block 0x40c5
    prev=[0x110], succ=[]
    =================================
    0x40c6: v40c6(0x784) = CONST 
    0x40c7: CALLPRIVATE v40c6(0x784)

    Begin block 0x11b
    prev=[0x110], succ=[0x40c8, 0x126]
    =================================
    0x11c: v11c(0x9bde100e) = CONST 
    0x121: v121 = EQ v11c(0x9bde100e), v1f
    0x4015: v4015(0x40c8) = CONST 
    0x4016: JUMPI v4015(0x40c8), v121

    Begin block 0x40c8
    prev=[0x11b], succ=[]
    =================================
    0x40c9: v40c9(0x78c) = CONST 
    0x40ca: CALLPRIVATE v40c9(0x78c)

    Begin block 0x126
    prev=[0x11b], succ=[0x40cb, 0x131]
    =================================
    0x127: v127(0xa204452b) = CONST 
    0x12c: v12c = EQ v127(0xa204452b), v1f
    0x4017: v4017(0x40cb) = CONST 
    0x4018: JUMPI v4017(0x40cb), v12c

    Begin block 0x40cb
    prev=[0x126], succ=[]
    =================================
    0x40cc: v40cc(0x794) = CONST 
    0x40cd: CALLPRIVATE v40cc(0x794)

    Begin block 0x131
    prev=[0x126], succ=[0x13c, 0x40ce]
    =================================
    0x132: v132(0xa43cb496) = CONST 
    0x137: v137 = EQ v132(0xa43cb496), v1f
    0x4019: v4019(0x40ce) = CONST 
    0x401a: JUMPI v4019(0x40ce), v137

    Begin block 0x13c
    prev=[0x131], succ=[0x33d6]
    =================================
    0x13c: v13c(0x33d6) = CONST 
    0x13f: JUMP v13c(0x33d6)

    Begin block 0x33d6
    prev=[0x13c], succ=[]
    =================================
    0x33d7: v33d7(0x0) = CONST 
    0x33da: REVERT v33d7(0x0), v33d7(0x0)

    Begin block 0x40ce
    prev=[0x131], succ=[]
    =================================
    0x40cf: v40cf(0x7b1) = CONST 
    0x40d0: CALLPRIVATE v40cf(0x7b1)

    Begin block 0x36
    prev=[0x2b], succ=[0xa2, 0x41]
    =================================
    0x37: v37(0xc0c53b8b) = CONST 
    0x3c: v3c = GT v37(0xc0c53b8b), v1f
    0x3d: v3d(0xa2) = CONST 
    0x40: JUMPI v3d(0xa2), v3c

    Begin block 0xa2
    prev=[0x36], succ=[0xd3, 0xae]
    =================================
    0xa4: va4(0xb3ab15fb) = CONST 
    0xa9: va9 = GT va4(0xb3ab15fb), v1f
    0xaa: vaa(0xd3) = CONST 
    0xad: JUMPI vaa(0xd3), va9

    Begin block 0xd3
    prev=[0xa2], succ=[0x40d1, 0xdf]
    =================================
    0xd5: vd5(0xa688cfd7) = CONST 
    0xda: vda = EQ vd5(0xa688cfd7), v1f
    0x400d: v400d(0x40d1) = CONST 
    0x400e: JUMPI v400d(0x40d1), vda

    Begin block 0x40d1
    prev=[0xd3], succ=[]
    =================================
    0x40d2: v40d2(0x7b9) = CONST 
    0x40d3: CALLPRIVATE v40d2(0x7b9)

    Begin block 0xdf
    prev=[0xd3], succ=[0x40d4, 0xea]
    =================================
    0xe0: ve0(0xa7566bcf) = CONST 
    0xe5: ve5 = EQ ve0(0xa7566bcf), v1f
    0x400f: v400f(0x40d4) = CONST 
    0x4010: JUMPI v400f(0x40d4), ve5

    Begin block 0x40d4
    prev=[0xdf], succ=[]
    =================================
    0x40d5: v40d5(0x7c1) = CONST 
    0x40d6: CALLPRIVATE v40d5(0x7c1)

    Begin block 0xea
    prev=[0xdf], succ=[0xf5, 0x40d7]
    =================================
    0xeb: veb(0xaaec5061) = CONST 
    0xf0: vf0 = EQ veb(0xaaec5061), v1f
    0x4011: v4011(0x40d7) = CONST 
    0x4012: JUMPI v4011(0x40d7), vf0

    Begin block 0xf5
    prev=[0xea], succ=[0x33b2]
    =================================
    0xf5: vf5(0x33b2) = CONST 
    0xf8: JUMP vf5(0x33b2)

    Begin block 0x33b2
    prev=[0xf5], succ=[]
    =================================
    0x33b3: v33b3(0x0) = CONST 
    0x33b6: REVERT v33b3(0x0), v33b3(0x0)

    Begin block 0x40d7
    prev=[0xea], succ=[]
    =================================
    0x40d8: v40d8(0x7c9) = CONST 
    0x40d9: CALLPRIVATE v40d8(0x7c9)

    Begin block 0xae
    prev=[0xa2], succ=[0x40da, 0xb9]
    =================================
    0xaf: vaf(0xb3ab15fb) = CONST 
    0xb4: vb4 = EQ vaf(0xb3ab15fb), v1f
    0x4007: v4007(0x40da) = CONST 
    0x4008: JUMPI v4007(0x40da), vb4

    Begin block 0x40da
    prev=[0xae], succ=[]
    =================================
    0x40db: v40db(0x7d1) = CONST 
    0x40dc: CALLPRIVATE v40db(0x7d1)

    Begin block 0xb9
    prev=[0xae], succ=[0x40dd, 0xc4]
    =================================
    0xba: vba(0xb8a878f9) = CONST 
    0xbf: vbf = EQ vba(0xb8a878f9), v1f
    0x4009: v4009(0x40dd) = CONST 
    0x400a: JUMPI v4009(0x40dd), vbf

    Begin block 0x40dd
    prev=[0xb9], succ=[]
    =================================
    0x40de: v40de(0x804) = CONST 
    0x40df: CALLPRIVATE v40de(0x804)

    Begin block 0xc4
    prev=[0xb9], succ=[0xcf, 0x40e0]
    =================================
    0xc5: vc5(0xbc0b1df6) = CONST 
    0xca: vca = EQ vc5(0xbc0b1df6), v1f
    0x400b: v400b(0x40e0) = CONST 
    0x400c: JUMPI v400b(0x40e0), vca

    Begin block 0xcf
    prev=[0xc4], succ=[0x338e]
    =================================
    0xcf: vcf(0x338e) = CONST 
    0xd2: JUMP vcf(0x338e)

    Begin block 0x338e
    prev=[0xcf], succ=[]
    =================================
    0x338f: v338f(0x0) = CONST 
    0x3392: REVERT v338f(0x0), v338f(0x0)

    Begin block 0x40e0
    prev=[0xc4], succ=[]
    =================================
    0x40e1: v40e1(0x80c) = CONST 
    0x40e2: CALLPRIVATE v40e1(0x80c)

    Begin block 0x41
    prev=[0x36], succ=[0x7c, 0x4c]
    =================================
    0x42: v42(0xc81982e8) = CONST 
    0x47: v47 = GT v42(0xc81982e8), v1f
    0x48: v48(0x7c) = CONST 
    0x4b: JUMPI v48(0x7c), v47

    Begin block 0x7c
    prev=[0x41], succ=[0x40e3, 0x88]
    =================================
    0x7e: v7e(0xc0c53b8b) = CONST 
    0x83: v83 = EQ v7e(0xc0c53b8b), v1f
    0x4001: v4001(0x40e3) = CONST 
    0x4002: JUMPI v4001(0x40e3), v83

    Begin block 0x40e3
    prev=[0x7c], succ=[]
    =================================
    0x40e4: v40e4(0x835) = CONST 
    0x40e5: CALLPRIVATE v40e4(0x835)

    Begin block 0x88
    prev=[0x7c], succ=[0x40e6, 0x93]
    =================================
    0x89: v89(0xc476dd27) = CONST 
    0x8e: v8e = EQ v89(0xc476dd27), v1f
    0x4003: v4003(0x40e6) = CONST 
    0x4004: JUMPI v4003(0x40e6), v8e

    Begin block 0x40e6
    prev=[0x88], succ=[]
    =================================
    0x40e7: v40e7(0x87a) = CONST 
    0x40e8: CALLPRIVATE v40e7(0x87a)

    Begin block 0x93
    prev=[0x88], succ=[0x9e, 0x40e9]
    =================================
    0x94: v94(0xc5967c26) = CONST 
    0x99: v99 = EQ v94(0xc5967c26), v1f
    0x4005: v4005(0x40e9) = CONST 
    0x4006: JUMPI v4005(0x40e9), v99

    Begin block 0x9e
    prev=[0x93], succ=[0x336a]
    =================================
    0x9e: v9e(0x336a) = CONST 
    0xa1: JUMP v9e(0x336a)

    Begin block 0x336a
    prev=[0x9e], succ=[]
    =================================
    0x336b: v336b(0x0) = CONST 
    0x336e: REVERT v336b(0x0), v336b(0x0)

    Begin block 0x40e9
    prev=[0x93], succ=[]
    =================================
    0x40ea: v40ea(0x882) = CONST 
    0x40eb: CALLPRIVATE v40ea(0x882)

    Begin block 0x4c
    prev=[0x41], succ=[0x40ec, 0x57]
    =================================
    0x4d: v4d(0xc81982e8) = CONST 
    0x52: v52 = EQ v4d(0xc81982e8), v1f
    0x3ff9: v3ff9(0x40ec) = CONST 
    0x3ffa: JUMPI v3ff9(0x40ec), v52

    Begin block 0x40ec
    prev=[0x4c], succ=[]
    =================================
    0x40ed: v40ed(0x88a) = CONST 
    0x40ee: CALLPRIVATE v40ed(0x88a)

    Begin block 0x57
    prev=[0x4c], succ=[0x40ef, 0x62]
    =================================
    0x58: v58(0xc8412d02) = CONST 
    0x5d: v5d = EQ v58(0xc8412d02), v1f
    0x3ffb: v3ffb(0x40ef) = CONST 
    0x3ffc: JUMPI v3ffb(0x40ef), v5d

    Begin block 0x40ef
    prev=[0x57], succ=[]
    =================================
    0x40f0: v40f0(0x892) = CONST 
    0x40f1: CALLPRIVATE v40f0(0x892)

    Begin block 0x62
    prev=[0x57], succ=[0x40f2, 0x6d]
    =================================
    0x63: v63(0xcac9aa9a) = CONST 
    0x68: v68 = EQ v63(0xcac9aa9a), v1f
    0x3ffd: v3ffd(0x40f2) = CONST 
    0x3ffe: JUMPI v3ffd(0x40f2), v68

    Begin block 0x40f2
    prev=[0x62], succ=[]
    =================================
    0x40f3: v40f3(0x89a) = CONST 
    0x40f4: CALLPRIVATE v40f3(0x89a)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x40f5]
    =================================
    0x6e: v6e(0xe1f095aa) = CONST 
    0x73: v73 = EQ v6e(0xe1f095aa), v1f
    0x3fff: v3fff(0x40f5) = CONST 
    0x4000: JUMPI v3fff(0x40f5), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x3346]
    =================================
    0x78: v78(0x3346) = CONST 
    0x7b: JUMP v78(0x3346)

    Begin block 0x3346
    prev=[0x78], succ=[]
    =================================
    0x3347: v3347(0x0) = CONST 
    0x334a: REVERT v3347(0x0), v3347(0x0)

    Begin block 0x40f5
    prev=[0x6d], succ=[]
    =================================
    0x40f6: v40f6(0x8a2) = CONST 
    0x40f7: CALLPRIVATE v40f6(0x8a2)

    Begin block 0x40f8
    prev=[0x10], succ=[]
    =================================
    0x40f9: v40f9(0x3322) = CONST 
    0x40fa: CALLPRIVATE v40f9(0x3322)

}

function 0x105e(0x105earg0x0) private {
    Begin block 0x105e
    prev=[], succ=[0x1069]
    =================================
    0x105f: v105f(0x0) = CONST 
    0x1062: v1062(0x1069) = CONST 
    0x1065: v1065(0x266f) = CONST 
    0x1068: v1068_0 = CALLPRIVATE v1065(0x266f), v1062(0x1069)

    Begin block 0x1069
    prev=[0x105e], succ=[0x107b, 0x3d67]
    =================================
    0x106c: v106c(0xde0b6b3a7640000) = CONST 
    0x1076: v1076 = LT v1068_0, v106c(0xde0b6b3a7640000)
    0x1077: v1077(0x3d67) = CONST 
    0x107a: JUMPI v1077(0x3d67), v1076

    Begin block 0x107b
    prev=[0x1069], succ=[0x1082, 0x1091]
    =================================
    0x107b: v107b(0xb) = CONST 
    0x107d: v107d = SLOAD v107b(0xb)
    0x107e: v107e(0x1091) = CONST 
    0x1081: JUMPI v107e(0x1091), v107d

    Begin block 0x1082
    prev=[0x107b], succ=[0x3d8a]
    =================================
    0x1082: v1082(0xde0b6b3a7640000) = CONST 
    0x108d: v108d(0x3d8a) = CONST 
    0x1090: JUMP v108d(0x3d8a)

    Begin block 0x3d8a
    prev=[0x1082], succ=[]
    =================================
    0x3d8d: RETURNPRIVATE v105earg0, v1082(0xde0b6b3a7640000)

    Begin block 0x1091
    prev=[0x107b], succ=[0x29b0B0x1091]
    =================================
    0x1092: v1092(0x0) = CONST 
    0x1094: v1094(0x10c6) = CONST 
    0x1097: v1097(0x2710) = CONST 
    0x109a: v109a(0x3dad) = CONST 
    0x109d: v109d(0xb) = CONST 
    0x109f: v109f = SLOAD v109d(0xb)
    0x10a0: v10a0(0x3dd2) = CONST 
    0x10a3: v10a3(0xde0b6b3a7640000) = CONST 
    0x10ad: v10ad(0x29b0) = CONST 
    0x10b3: v10b3(0xffffffff) = CONST 
    0x10b8: v10b8(0x29b0) = AND v10b3(0xffffffff), v10ad(0x29b0)
    0x10b9: JUMP v10b8(0x29b0)

    Begin block 0x29b0B0x1091
    prev=[0x1091], succ=[0x29a70x29b0B0x1091]
    =================================
    0x29b1S0x1091: v29b1V1091(0x0) = CONST 
    0x29b3S0x1091: v29b3V1091(0x29a7) = CONST 
    0x29b8S0x1091: v29b8V1091(0x40) = CONST 
    0x29baS0x1091: v29baV1091 = MLOAD v29b8V1091(0x40)
    0x29bcS0x1091: v29bcV1091(0x40) = CONST 
    0x29beS0x1091: v29beV1091 = ADD v29bcV1091(0x40), v29baV1091
    0x29bfS0x1091: v29bfV1091(0x40) = CONST 
    0x29c1S0x1091: MSTORE v29bfV1091(0x40), v29beV1091
    0x29c3S0x1091: v29c3V1091(0x1e) = CONST 
    0x29c6S0x1091: MSTORE v29baV1091, v29c3V1091(0x1e)
    0x29c7S0x1091: v29c7V1091(0x20) = CONST 
    0x29c9S0x1091: v29c9V1091 = ADD v29c7V1091(0x20), v29baV1091
    0x29caS0x1091: v29caV1091(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x1091: MSTORE v29c9V1091, v29caV1091(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x1091: v29eeV1091(0x2bef) = CONST 
    0x29f1S0x1091: v29f1_0V1091 = CALLPRIVATE v29eeV1091(0x2bef), v29baV1091, v10a3(0xde0b6b3a7640000), v1068_0, v29b3V1091(0x29a7)

    Begin block 0x29a70x29b0B0x1091
    prev=[0x29b0B0x1091], succ=[0x29aa0x29b0B0x1091]
    =================================

    Begin block 0x29aa0x29b0B0x1091
    prev=[0x29a70x29b0B0x1091], succ=[0x3dd2]
    =================================
    0x29af0x29b0S0x1091: JUMP v10a0(0x3dd2)

    Begin block 0x3dd2
    prev=[0x29aa0x29b0B0x1091], succ=[0x3dad]
    =================================
    0x3dd4: v3dd4(0x29f2) = CONST 
    0x3dd7: v3dd7_0 = CALLPRIVATE v3dd4(0x29f2), v109f, v29f1_0V1091, v109a(0x3dad)

    Begin block 0x3dad
    prev=[0x3dd2], succ=[0x10c6]
    =================================
    0x3daf: v3daf(0x2a65) = CONST 
    0x3db2: v3db2_0 = CALLPRIVATE v3daf(0x2a65), v1097(0x2710), v3dd7_0, v1094(0x10c6)

    Begin block 0x10c6
    prev=[0x3dad], succ=[0x10da]
    =================================
    0x10c9: v10c9(0x10da) = CONST 
    0x10cc: v10cc(0xde0b6b3a7640000) = CONST 
    0x10d6: v10d6(0x2933) = CONST 
    0x10d9: v10d9_0 = CALLPRIVATE v10d6(0x2933), v3db2_0, v10cc(0xde0b6b3a7640000), v10c9(0x10da)

    Begin block 0x10da
    prev=[0x10c6], succ=[0x10ee, 0x10ea]
    =================================
    0x10db: v10db(0xc) = CONST 
    0x10dd: v10dd = SLOAD v10db(0xc)
    0x10e2: v10e2 = ISZERO v10dd
    0x10e4: v10e4 = ISZERO v10e2
    0x10e6: v10e6(0x10ee) = CONST 
    0x10e9: JUMPI v10e6(0x10ee), v10e2

    Begin block 0x10ee
    prev=[0x10da, 0x10ea], succ=[0x10f7, 0x10f4]
    =================================
    0x10ee_0x0: v10ee_0 = PHI v10e4, v10ed
    0x10ef: v10ef = ISZERO v10ee_0
    0x10f0: v10f0(0x10f7) = CONST 
    0x10f3: JUMPI v10f0(0x10f7), v10ef

    Begin block 0x10f7
    prev=[0x10ee, 0x10f4], succ=[0x10fa]
    =================================

    Begin block 0x10fa
    prev=[0x10f7], succ=[]
    =================================
    0x10fa_0x1: v10fa_1 = PHI v10dd, v10d9_0
    0x10fd: RETURNPRIVATE v105earg0, v10fa_1

    Begin block 0x10f4
    prev=[0x10ee], succ=[0x10f7]
    =================================

    Begin block 0x10ea
    prev=[0x10da], succ=[0x10ee]
    =================================
    0x10ed: v10ed = GT v10d9_0, v10dd

    Begin block 0x3d67
    prev=[0x1069], succ=[]
    =================================
    0x3d6a: RETURNPRIVATE v105earg0, v105f(0x0)

}

function 0x1af0(0x1af0arg0x0) private {
    Begin block 0x1af0
    prev=[], succ=[0x1afb]
    =================================
    0x1af1: v1af1(0x0) = CONST 
    0x1af4: v1af4(0x1afb) = CONST 
    0x1af7: v1af7(0x282f) = CONST 
    0x1afa: v1afa_0 = CALLPRIVATE v1af7(0x282f), v1af4(0x1afb)

    Begin block 0x1afb
    prev=[0x1af0], succ=[0x1b0d, 0x3e40]
    =================================
    0x1afe: v1afe(0xde0b6b3a7640000) = CONST 
    0x1b08: v1b08 = LT v1afa_0, v1afe(0xde0b6b3a7640000)
    0x1b09: v1b09(0x3e40) = CONST 
    0x1b0c: JUMPI v1b09(0x3e40), v1b08

    Begin block 0x1b0d
    prev=[0x1afb], succ=[0x1b16]
    =================================
    0x1b0d: v1b0d(0x0) = CONST 
    0x1b0f: v1b0f(0x1b16) = CONST 
    0x1b12: v1b12(0x1c11) = CONST 
    0x1b15: v1b15_0 = CALLPRIVATE v1b12(0x1c11), v1b0f(0x1b16)

    Begin block 0x1b16
    prev=[0x1b0d], succ=[0x1b8a, 0x1b8e]
    =================================
    0x1b19: v1b19(0x0) = CONST 
    0x1b1b: v1b1b(0x1bc0) = CONST 
    0x1b1e: v1b1e(0x2710) = CONST 
    0x1b21: v1b21(0x3e63) = CONST 
    0x1b24: v1b24(0xd) = CONST 
    0x1b26: v1b26 = SLOAD v1b24(0xd)
    0x1b27: v1b27(0x2) = CONST 
    0x1b29: v1b29(0x0) = CONST 
    0x1b2c: v1b2c = SLOAD v1b27(0x2)
    0x1b2e: v1b2e(0x100) = CONST 
    0x1b31: v1b31(0x1) = EXP v1b2e(0x100), v1b29(0x0)
    0x1b33: v1b33 = DIV v1b2c, v1b31(0x1)
    0x1b34: v1b34(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b49: v1b49 = AND v1b34(0xffffffffffffffffffffffffffffffffffffffff), v1b33
    0x1b4a: v1b4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1b5f: v1b5f = AND v1b4a(0xffffffffffffffffffffffffffffffffffffffff), v1b49
    0x1b60: v1b60(0x18160ddd) = CONST 
    0x1b65: v1b65(0x40) = CONST 
    0x1b67: v1b67 = MLOAD v1b65(0x40)
    0x1b69: v1b69(0xffffffff) = CONST 
    0x1b6e: v1b6e(0x18160ddd) = AND v1b69(0xffffffff), v1b60(0x18160ddd)
    0x1b6f: v1b6f(0xe0) = CONST 
    0x1b71: v1b71(0x18160ddd00000000000000000000000000000000000000000000000000000000) = SHL v1b6f(0xe0), v1b6e(0x18160ddd)
    0x1b73: MSTORE v1b67, v1b71(0x18160ddd00000000000000000000000000000000000000000000000000000000)
    0x1b74: v1b74(0x4) = CONST 
    0x1b76: v1b76 = ADD v1b74(0x4), v1b67
    0x1b77: v1b77(0x20) = CONST 
    0x1b79: v1b79(0x40) = CONST 
    0x1b7b: v1b7b = MLOAD v1b79(0x40)
    0x1b7e: v1b7e(0x4) = SUB v1b76, v1b7b
    0x1b82: v1b82 = EXTCODESIZE v1b5f
    0x1b83: v1b83 = ISZERO v1b82
    0x1b85: v1b85 = ISZERO v1b83
    0x1b86: v1b86(0x1b8e) = CONST 
    0x1b89: JUMPI v1b86(0x1b8e), v1b85

    Begin block 0x1b8a
    prev=[0x1b16], succ=[]
    =================================
    0x1b8a: v1b8a(0x0) = CONST 
    0x1b8d: REVERT v1b8a(0x0), v1b8a(0x0)

    Begin block 0x1b8e
    prev=[0x1b16], succ=[0x1b99, 0x1ba2]
    =================================
    0x1b90: v1b90 = GAS 
    0x1b91: v1b91 = STATICCALL v1b90, v1b5f, v1b7b, v1b7e(0x4), v1b7b, v1b77(0x20)
    0x1b92: v1b92 = ISZERO v1b91
    0x1b94: v1b94 = ISZERO v1b92
    0x1b95: v1b95(0x1ba2) = CONST 
    0x1b98: JUMPI v1b95(0x1ba2), v1b94

    Begin block 0x1b99
    prev=[0x1b8e], succ=[]
    =================================
    0x1b99: v1b99 = RETURNDATASIZE 
    0x1b9a: v1b9a(0x0) = CONST 
    0x1b9d: RETURNDATACOPY v1b9a(0x0), v1b9a(0x0), v1b99
    0x1b9e: v1b9e = RETURNDATASIZE 
    0x1b9f: v1b9f(0x0) = CONST 
    0x1ba1: REVERT v1b9f(0x0), v1b9e

    Begin block 0x1ba2
    prev=[0x1b8e], succ=[0x1bb4, 0x1bb8]
    =================================
    0x1ba7: v1ba7(0x40) = CONST 
    0x1ba9: v1ba9 = MLOAD v1ba7(0x40)
    0x1baa: v1baa = RETURNDATASIZE 
    0x1bab: v1bab(0x20) = CONST 
    0x1bae: v1bae = LT v1baa, v1bab(0x20)
    0x1baf: v1baf = ISZERO v1bae
    0x1bb0: v1bb0(0x1bb8) = CONST 
    0x1bb3: JUMPI v1bb0(0x1bb8), v1baf

    Begin block 0x1bb4
    prev=[0x1ba2], succ=[]
    =================================
    0x1bb4: v1bb4(0x0) = CONST 
    0x1bb7: REVERT v1bb4(0x0), v1bb4(0x0)

    Begin block 0x1bb8
    prev=[0x1ba2], succ=[0x29f20x1af0]
    =================================
    0x1bba: v1bba = MLOAD v1ba9
    0x1bbc: v1bbc(0x29f2) = CONST 
    0x1bbf: JUMP v1bbc(0x29f2)

    Begin block 0x29f20x1af0
    prev=[0x1bb8], succ=[0x2a010x1af0, 0x29fa0x1af0]
    =================================
    0x29f30x1af0: v1af029f3(0x0) = CONST 
    0x29f60x1af0: v1af029f6(0x2a01) = CONST 
    0x29f90x1af0: JUMPI v1af029f6(0x2a01), v1bba

    Begin block 0x2a010x1af0
    prev=[0x29f20x1af0], succ=[0x2a0d0x1af0, 0x2a0e0x1af0]
    =================================
    0x2a040x1af0: v1af02a04 = MUL v1b26, v1bba
    0x2a090x1af0: v1af02a09(0x2a0e) = CONST 
    0x2a0c0x1af0: JUMPI v1af02a09(0x2a0e), v1bba

    Begin block 0x2a0d0x1af0
    prev=[0x2a010x1af0], succ=[]
    =================================
    0x2a0d0x1af0: THROW 

    Begin block 0x2a0e0x1af0
    prev=[0x2a010x1af0], succ=[0x2a150x1af0, 0x29a70x1af0]
    =================================
    0x2a0f0x1af0: v1af02a0f = DIV v1af02a04, v1bba
    0x2a100x1af0: v1af02a10 = EQ v1af02a0f, v1b26
    0x2a110x1af0: v1af02a11(0x29a7) = CONST 
    0x2a140x1af0: JUMPI v1af02a11(0x29a7), v1af02a10

    Begin block 0x2a150x1af0
    prev=[0x2a0e0x1af0], succ=[]
    =================================
    0x2a150x1af0: v1af02a15(0x40) = CONST 
    0x2a170x1af0: v1af02a17 = MLOAD v1af02a15(0x40)
    0x2a180x1af0: v1af02a18(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a3a0x1af0: MSTORE v1af02a17, v1af02a18(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a3b0x1af0: v1af02a3b(0x4) = CONST 
    0x2a3d0x1af0: v1af02a3d = ADD v1af02a3b(0x4), v1af02a17
    0x2a400x1af0: v1af02a40(0x20) = CONST 
    0x2a420x1af0: v1af02a42 = ADD v1af02a40(0x20), v1af02a3d
    0x2a450x1af0: v1af02a45(0x20) = SUB v1af02a42, v1af02a3d
    0x2a470x1af0: MSTORE v1af02a3d, v1af02a45(0x20)
    0x2a480x1af0: v1af02a48(0x21) = CONST 
    0x2a4b0x1af0: MSTORE v1af02a42, v1af02a48(0x21)
    0x2a4c0x1af0: v1af02a4c(0x20) = CONST 
    0x2a4e0x1af0: v1af02a4e = ADD v1af02a4c(0x20), v1af02a42
    0x2a500x1af0: v1af02a50(0x3202) = CONST 
    0x2a530x1af0: v1af02a53(0x21) = CONST 
    0x2a560x1af0: CODECOPY v1af02a4e, v1af02a50(0x3202), v1af02a53(0x21)
    0x2a570x1af0: v1af02a57(0x40) = CONST 
    0x2a590x1af0: v1af02a59 = ADD v1af02a57(0x40), v1af02a4e
    0x2a5d0x1af0: v1af02a5d(0x40) = CONST 
    0x2a5f0x1af0: v1af02a5f = MLOAD v1af02a5d(0x40)
    0x2a620x1af0: v1af02a62(0x84) = SUB v1af02a59, v1af02a5f
    0x2a640x1af0: REVERT v1af02a5f, v1af02a62(0x84)

    Begin block 0x29a70x1af0
    prev=[0x2a0e0x1af0, 0x2d1a0x1af0], succ=[0x29aa0x1af0]
    =================================

    Begin block 0x29aa0x1af0
    prev=[0x29fa0x1af0, 0x29a70x1af0], succ=[0x1bc0, 0x3e63]
    =================================
    0x29aa0x1af0_0x3: v29aa1af0_3 = PHI v1af1(0x0), v1b1b(0x1bc0), v1b21(0x3e63), v1b15_0
    0x29af0x1af0: JUMP v29aa1af0_3

    Begin block 0x1bc0
    prev=[0x29aa0x1af0], succ=[0x1bdb, 0x1be9]
    =================================
    0x1bc0_0x0: v1bc0_0 = PHI v1af02d1b, v1af02a04, v1af029fb(0x0)
    0x1bc0_0x2: v1bc0_2 = PHI v1af1(0x0), v1b1b(0x1bc0), v1b15_0
    0x1bc1: v1bc1(0x0) = CONST 
    0x1bc5: MSTORE v1bc1(0x0), v1bc0_2
    0x1bc6: v1bc6(0x10) = CONST 
    0x1bc8: v1bc8(0x20) = CONST 
    0x1bca: MSTORE v1bc8(0x20), v1bc6(0x10)
    0x1bcb: v1bcb(0x40) = CONST 
    0x1bce: v1bce = SHA3 v1bc1(0x0), v1bcb(0x40)
    0x1bcf: v1bcf = SLOAD v1bce
    0x1bd5: v1bd5 = GT v1bc0_0, v1bcf
    0x1bd6: v1bd6 = ISZERO v1bd5
    0x1bd7: v1bd7(0x1be9) = CONST 
    0x1bda: JUMPI v1bd7(0x1be9), v1bd6

    Begin block 0x1bdb
    prev=[0x1bc0], succ=[0x29b0B0x1bdb]
    =================================
    0x1bdb: v1bdb(0x1be4) = CONST 
    0x1bdb_0x1: v1bdb_1 = PHI v1af02d1b, v1af02a04, v1af029fb(0x0)
    0x1be0: v1be0(0x29b0) = CONST 
    0x1be3: JUMP v1be0(0x29b0)

    Begin block 0x29b0B0x1bdb
    prev=[0x1bdb], succ=[0x29a70x29b0B0x1bdb]
    =================================
    0x29b1S0x1bdb: v29b1V1bdb(0x0) = CONST 
    0x29b3S0x1bdb: v29b3V1bdb(0x29a7) = CONST 
    0x29b8S0x1bdb: v29b8V1bdb(0x40) = CONST 
    0x29baS0x1bdb: v29baV1bdb = MLOAD v29b8V1bdb(0x40)
    0x29bcS0x1bdb: v29bcV1bdb(0x40) = CONST 
    0x29beS0x1bdb: v29beV1bdb = ADD v29bcV1bdb(0x40), v29baV1bdb
    0x29bfS0x1bdb: v29bfV1bdb(0x40) = CONST 
    0x29c1S0x1bdb: MSTORE v29bfV1bdb(0x40), v29beV1bdb
    0x29c3S0x1bdb: v29c3V1bdb(0x1e) = CONST 
    0x29c6S0x1bdb: MSTORE v29baV1bdb, v29c3V1bdb(0x1e)
    0x29c7S0x1bdb: v29c7V1bdb(0x20) = CONST 
    0x29c9S0x1bdb: v29c9V1bdb = ADD v29c7V1bdb(0x20), v29baV1bdb
    0x29caS0x1bdb: v29caV1bdb(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x1bdb: MSTORE v29c9V1bdb, v29caV1bdb(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x1bdb: v29eeV1bdb(0x2bef) = CONST 
    0x29f1S0x1bdb: v29f1_0V1bdb = CALLPRIVATE v29eeV1bdb(0x2bef), v29baV1bdb, v1bcf, v1bdb_1, v29b3V1bdb(0x29a7)

    Begin block 0x29a70x29b0B0x1bdb
    prev=[0x29b0B0x1bdb], succ=[0x29aa0x29b0B0x1bdb]
    =================================

    Begin block 0x29aa0x29b0B0x1bdb
    prev=[0x29a70x29b0B0x1bdb], succ=[0x1be4]
    =================================
    0x29af0x29b0S0x1bdb: JUMP v1bdb(0x1be4)

    Begin block 0x1be4
    prev=[0x29aa0x29b0B0x1bdb], succ=[0x1bec]
    =================================
    0x1be5: v1be5(0x1bec) = CONST 
    0x1be8: JUMP v1be5(0x1bec)

    Begin block 0x1bec
    prev=[0x1be9, 0x1be4], succ=[]
    =================================
    0x1bec_0x0: v1bec_0 = PHI v1bea(0x0), v29f1_0V1bdb
    0x1bec_0x6: v1bec_6 = PHI v1afa_0, v1af0arg0
    0x1bf4: RETURNPRIVATE v1bec_6, v1bec_0

    Begin block 0x1be9
    prev=[0x1bc0], succ=[0x1bec]
    =================================
    0x1bea: v1bea(0x0) = CONST 

    Begin block 0x3e63
    prev=[0x29aa0x1af0], succ=[0x2a650x1af0]
    =================================
    0x3e65: v3e65(0x2a65) = CONST 
    0x3e68: JUMP v3e65(0x2a65)

    Begin block 0x2a650x1af0
    prev=[0x3e63], succ=[0x2ca50x1af0]
    =================================
    0x2a660x1af0: v1af02a66(0x0) = CONST 
    0x2a680x1af0: v1af02a68(0x29a7) = CONST 
    0x2a6d0x1af0: v1af02a6d(0x40) = CONST 
    0x2a6f0x1af0: v1af02a6f = MLOAD v1af02a6d(0x40)
    0x2a710x1af0: v1af02a71(0x40) = CONST 
    0x2a730x1af0: v1af02a73 = ADD v1af02a71(0x40), v1af02a6f
    0x2a740x1af0: v1af02a74(0x40) = CONST 
    0x2a760x1af0: MSTORE v1af02a74(0x40), v1af02a73
    0x2a780x1af0: v1af02a78(0x1a) = CONST 
    0x2a7b0x1af0: MSTORE v1af02a6f, v1af02a78(0x1a)
    0x2a7c0x1af0: v1af02a7c(0x20) = CONST 
    0x2a7e0x1af0: v1af02a7e = ADD v1af02a7c(0x20), v1af02a6f
    0x2a7f0x1af0: v1af02a7f(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x2aa10x1af0: MSTORE v1af02a7e, v1af02a7f(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x2aa30x1af0: v1af02aa3(0x2ca5) = CONST 
    0x2aa60x1af0: JUMP v1af02aa3(0x2ca5)

    Begin block 0x2ca50x1af0
    prev=[0x2a650x1af0], succ=[0x2cae0x1af0, 0x2d0e0x1af0]
    =================================
    0x2ca50x1af0_0x1: v2ca51af0_1 = PHI v1b19(0x0), v1b1e(0x2710), v1afa_0, v1af0arg0
    0x2ca60x1af0: v1af02ca6(0x0) = CONST 
    0x2caa0x1af0: v1af02caa(0x2d0e) = CONST 
    0x2cad0x1af0: JUMPI v1af02caa(0x2d0e), v2ca51af0_1

    Begin block 0x2cae0x1af0
    prev=[0x2ca50x1af0], succ=[0x2cff0x1af0, 0x2c5d0x1af0]
    =================================
    0x2cae0x1af0: v1af02cae(0x40) = CONST 
    0x2cb00x1af0: v1af02cb0 = MLOAD v1af02cae(0x40)
    0x2cb10x1af0: v1af02cb1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2cd30x1af0: MSTORE v1af02cb0, v1af02cb1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2cd40x1af0: v1af02cd4(0x20) = CONST 
    0x2cd60x1af0: v1af02cd6(0x4) = CONST 
    0x2cd90x1af0: v1af02cd9 = ADD v1af02cb0, v1af02cd6(0x4)
    0x2cdc0x1af0: MSTORE v1af02cd9, v1af02cd4(0x20)
    0x2cde0x1af0: v1af02cde(0x1a) = MLOAD v1af02a6f
    0x2cdf0x1af0: v1af02cdf(0x24) = CONST 
    0x2ce20x1af0: v1af02ce2 = ADD v1af02cb0, v1af02cdf(0x24)
    0x2ce30x1af0: MSTORE v1af02ce2, v1af02cde(0x1a)
    0x2ce50x1af0: v1af02ce5(0x1a) = MLOAD v1af02a6f
    0x2cea0x1af0: v1af02cea(0x44) = CONST 
    0x2cee0x1af0: v1af02cee = ADD v1af02cb0, v1af02cea(0x44)
    0x2cf20x1af0: v1af02cf2 = ADD v1af02a6f, v1af02cd4(0x20)
    0x2cf70x1af0: v1af02cf7(0x0) = CONST 
    0x2cfa0x1af0: v1af02cfa = ISZERO v1af02ce5(0x1a)
    0x2cfb0x1af0: v1af02cfb(0x2c5d) = CONST 
    0x2cfe0x1af0: JUMPI v1af02cfb(0x2c5d), v1af02cfa

    Begin block 0x2cff0x1af0
    prev=[0x2cae0x1af0], succ=[0x2c450x1af0]
    =================================
    0x2d010x1af0: v1af02d01 = ADD v1af02cf7(0x0), v1af02cf2
    0x2d020x1af0: v1af02d02 = MLOAD v1af02d01
    0x2d050x1af0: v1af02d05 = ADD v1af02cf7(0x0), v1af02cee
    0x2d060x1af0: MSTORE v1af02d05, v1af02d02
    0x2d070x1af0: v1af02d07(0x20) = CONST 
    0x2d090x1af0: v1af02d09(0x20) = ADD v1af02d07(0x20), v1af02cf7(0x0)
    0x2d0a0x1af0: v1af02d0a(0x2c45) = CONST 
    0x2d0d0x1af0: JUMP v1af02d0a(0x2c45)

    Begin block 0x2c450x1af0
    prev=[0x2cff0x1af0, 0x2c4e0x1af0], succ=[0x2c5d0x1af0, 0x2c4e0x1af0]
    =================================
    0x2c450x1af0_0x0: v2c451af0_0 = PHI v1af02d09(0x20), v1af02c58
    0x2c480x1af0: v1af02c48 = LT v2c451af0_0, v1af02ce5(0x1a)
    0x2c490x1af0: v1af02c49 = ISZERO v1af02c48
    0x2c4a0x1af0: v1af02c4a(0x2c5d) = CONST 
    0x2c4d0x1af0: JUMPI v1af02c4a(0x2c5d), v1af02c49

    Begin block 0x2c5d0x1af0
    prev=[0x2cae0x1af0, 0x2c450x1af0], succ=[0x2c8a0x1af0, 0x2c710x1af0]
    =================================
    0x2c660x1af0: v1af02c66 = ADD v1af02ce5(0x1a), v1af02cee
    0x2c680x1af0: v1af02c68(0x1f) = CONST 
    0x2c6a0x1af0: v1af02c6a(0x1a) = AND v1af02c68(0x1f), v1af02ce5(0x1a)
    0x2c6c0x1af0: v1af02c6c = ISZERO v1af02c6a(0x1a)
    0x2c6d0x1af0: v1af02c6d(0x2c8a) = CONST 
    0x2c700x1af0: JUMPI v1af02c6d(0x2c8a), v1af02c6c

    Begin block 0x2c8a0x1af0
    prev=[0x2c5d0x1af0, 0x2c710x1af0], succ=[]
    =================================
    0x2c8a0x1af0_0x1: v2c8a1af0_1 = PHI v1af02c87, v1af02c66
    0x2c900x1af0: v1af02c90(0x40) = CONST 
    0x2c920x1af0: v1af02c92 = MLOAD v1af02c90(0x40)
    0x2c950x1af0: v1af02c95 = SUB v2c8a1af0_1, v1af02c92
    0x2c970x1af0: REVERT v1af02c92, v1af02c95

    Begin block 0x2c710x1af0
    prev=[0x2c5d0x1af0], succ=[0x2c8a0x1af0]
    =================================
    0x2c730x1af0: v1af02c73 = SUB v1af02c66, v1af02c6a(0x1a)
    0x2c750x1af0: v1af02c75 = MLOAD v1af02c73
    0x2c760x1af0: v1af02c76(0x1) = CONST 
    0x2c790x1af0: v1af02c79(0x20) = CONST 
    0x2c7b0x1af0: v1af02c7b(0x6) = SUB v1af02c79(0x20), v1af02c6a(0x1a)
    0x2c7c0x1af0: v1af02c7c(0x100) = CONST 
    0x2c7f0x1af0: v1af02c7f(0x1000000000000) = EXP v1af02c7c(0x100), v1af02c7b(0x6)
    0x2c800x1af0: v1af02c80(0xffffffffffff) = SUB v1af02c7f(0x1000000000000), v1af02c76(0x1)
    0x2c810x1af0: v1af02c81 = NOT v1af02c80(0xffffffffffff)
    0x2c820x1af0: v1af02c82 = AND v1af02c81, v1af02c75
    0x2c840x1af0: MSTORE v1af02c73, v1af02c82
    0x2c850x1af0: v1af02c85(0x20) = CONST 
    0x2c870x1af0: v1af02c87 = ADD v1af02c85(0x20), v1af02c73

    Begin block 0x2c4e0x1af0
    prev=[0x2c450x1af0], succ=[0x2c450x1af0]
    =================================
    0x2c4e0x1af0_0x0: v2c4e1af0_0 = PHI v1af02d09(0x20), v1af02c58
    0x2c500x1af0: v1af02c50 = ADD v2c4e1af0_0, v1af02cf2
    0x2c510x1af0: v1af02c51 = MLOAD v1af02c50
    0x2c540x1af0: v1af02c54 = ADD v2c4e1af0_0, v1af02cee
    0x2c550x1af0: MSTORE v1af02c54, v1af02c51
    0x2c560x1af0: v1af02c56(0x20) = CONST 
    0x2c580x1af0: v1af02c58 = ADD v1af02c56(0x20), v2c4e1af0_0
    0x2c590x1af0: v1af02c59(0x2c45) = CONST 
    0x2c5c0x1af0: JUMP v1af02c59(0x2c45)

    Begin block 0x2d0e0x1af0
    prev=[0x2ca50x1af0], succ=[0x2d190x1af0, 0x2d1a0x1af0]
    =================================
    0x2d0e0x1af0_0x3: v2d0e1af0_3 = PHI v1b19(0x0), v1b1e(0x2710), v1afa_0, v1af0arg0
    0x2d100x1af0: v1af02d10(0x0) = CONST 
    0x2d150x1af0: v1af02d15(0x2d1a) = CONST 
    0x2d180x1af0: JUMPI v1af02d15(0x2d1a), v2d0e1af0_3

    Begin block 0x2d190x1af0
    prev=[0x2d0e0x1af0], succ=[]
    =================================
    0x2d190x1af0: THROW 

    Begin block 0x2d1a0x1af0
    prev=[0x2d0e0x1af0], succ=[0x29a70x1af0]
    =================================
    0x2d1a0x1af0_0x0: v2d1a1af0_0 = PHI v1af02d1b, v1af02a04, v1af029fb(0x0)
    0x2d1a0x1af0_0x1: v2d1a1af0_1 = PHI v1b19(0x0), v1b1e(0x2710), v1afa_0, v1af0arg0
    0x2d1b0x1af0: v1af02d1b = DIV v2d1a1af0_0, v2d1a1af0_1
    0x2d230x1af0: JUMP v1af02a68(0x29a7)

    Begin block 0x29fa0x1af0
    prev=[0x29f20x1af0], succ=[0x29aa0x1af0]
    =================================
    0x29fb0x1af0: v1af029fb(0x0) = CONST 
    0x29fd0x1af0: v1af029fd(0x29aa) = CONST 
    0x2a000x1af0: JUMP v1af029fd(0x29aa)

    Begin block 0x3e40
    prev=[0x1afb], succ=[]
    =================================
    0x3e43: RETURNPRIVATE v1af0arg0, v1af1(0x0)

}

function 0x1c11(0x1c11arg0x0) private {
    Begin block 0x1c11
    prev=[], succ=[0x1c78, 0x9150x1c11]
    =================================
    0x1c12: v1c12(0x3) = CONST 
    0x1c14: v1c14 = SLOAD v1c12(0x3)
    0x1c15: v1c15(0x40) = CONST 
    0x1c18: v1c18 = MLOAD v1c15(0x40)
    0x1c19: v1c19(0x900cf0cf00000000000000000000000000000000000000000000000000000000) = CONST 
    0x1c3b: MSTORE v1c18, v1c19(0x900cf0cf00000000000000000000000000000000000000000000000000000000)
    0x1c3d: v1c3d = MLOAD v1c15(0x40)
    0x1c3e: v1c3e(0x0) = CONST 
    0x1c41: v1c41(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c56: v1c56 = AND v1c41(0xffffffffffffffffffffffffffffffffffffffff), v1c14
    0x1c58: v1c58(0x900cf0cf) = CONST 
    0x1c5e: v1c5e(0x4) = CONST 
    0x1c62: v1c62 = ADD v1c18, v1c5e(0x4)
    0x1c64: v1c64(0x20) = CONST 
    0x1c6b: v1c6b(0x0) = SUB v1c18, v1c3d
    0x1c6c: v1c6c(0x4) = ADD v1c6b(0x0), v1c5e(0x4)
    0x1c70: v1c70 = EXTCODESIZE v1c56
    0x1c71: v1c71 = ISZERO v1c70
    0x1c73: v1c73 = ISZERO v1c71
    0x1c74: v1c74(0x915) = CONST 
    0x1c77: JUMPI v1c74(0x915), v1c73

    Begin block 0x1c78
    prev=[0x1c11], succ=[]
    =================================
    0x1c78: v1c78(0x0) = CONST 
    0x1c7b: REVERT v1c78(0x0), v1c78(0x0)

    Begin block 0x9150x1c11
    prev=[0x1c11], succ=[0x9200x1c11, 0x9290x1c11]
    =================================
    0x9170x1c11: v1c11917 = GAS 
    0x9180x1c11: v1c11918 = STATICCALL v1c11917, v1c56, v1c3d, v1c6c(0x4), v1c3d, v1c64(0x20)
    0x9190x1c11: v1c11919 = ISZERO v1c11918
    0x91b0x1c11: v1c1191b = ISZERO v1c11919
    0x91c0x1c11: v1c1191c(0x929) = CONST 
    0x91f0x1c11: JUMPI v1c1191c(0x929), v1c1191b

    Begin block 0x9200x1c11
    prev=[0x9150x1c11], succ=[]
    =================================
    0x9200x1c11: v1c11920 = RETURNDATASIZE 
    0x9210x1c11: v1c11921(0x0) = CONST 
    0x9240x1c11: RETURNDATACOPY v1c11921(0x0), v1c11921(0x0), v1c11920
    0x9250x1c11: v1c11925 = RETURNDATASIZE 
    0x9260x1c11: v1c11926(0x0) = CONST 
    0x9280x1c11: REVERT v1c11926(0x0), v1c11925

    Begin block 0x9290x1c11
    prev=[0x9150x1c11], succ=[0x93b0x1c11, 0x93f0x1c11]
    =================================
    0x92e0x1c11: v1c1192e(0x40) = CONST 
    0x9300x1c11: v1c11930 = MLOAD v1c1192e(0x40)
    0x9310x1c11: v1c11931 = RETURNDATASIZE 
    0x9320x1c11: v1c11932(0x20) = CONST 
    0x9350x1c11: v1c11935 = LT v1c11931, v1c11932(0x20)
    0x9360x1c11: v1c11936 = ISZERO v1c11935
    0x9370x1c11: v1c11937(0x93f) = CONST 
    0x93a0x1c11: JUMPI v1c11937(0x93f), v1c11936

    Begin block 0x93b0x1c11
    prev=[0x9290x1c11], succ=[]
    =================================
    0x93b0x1c11: v1c1193b(0x0) = CONST 
    0x93e0x1c11: REVERT v1c1193b(0x0), v1c1193b(0x0)

    Begin block 0x93f0x1c11
    prev=[0x9290x1c11], succ=[0x9440x1c11]
    =================================
    0x9410x1c11: v1c11941 = MLOAD v1c11930

    Begin block 0x9440x1c11
    prev=[0x93f0x1c11], succ=[]
    =================================
    0x9460x1c11: RETURNPRIVATE v1c11arg0, v1c11941

}

function 0x1cfd(0x1cfdarg0x0) private {
    Begin block 0x1cfd
    prev=[], succ=[0x1d08]
    =================================
    0x1cfe: v1cfe(0x0) = CONST 
    0x1d01: v1d01(0x1d08) = CONST 
    0x1d04: v1d04(0x282f) = CONST 
    0x1d07: v1d07_0 = CALLPRIVATE v1d04(0x282f), v1d01(0x1d08)

    Begin block 0x1d08
    prev=[0x1cfd], succ=[0x1d1b, 0x3e88]
    =================================
    0x1d0b: v1d0b(0xde0b6b3a7640000) = CONST 
    0x1d15: v1d15 = LT v1d07_0, v1d0b(0xde0b6b3a7640000)
    0x1d16: v1d16 = ISZERO v1d15
    0x1d17: v1d17(0x3e88) = CONST 
    0x1d1a: JUMPI v1d17(0x3e88), v1d16

    Begin block 0x1d1b
    prev=[0x1d08], succ=[0x1d25]
    =================================
    0x1d1b: v1d1b(0x1d3a) = CONST 
    0x1d1e: v1d1e(0x1d25) = CONST 
    0x1d21: v1d21(0x2780) = CONST 
    0x1d24: v1d24_0 = CALLPRIVATE v1d21(0x2780), v1d1e(0x1d25)

    Begin block 0x1d25
    prev=[0x1d1b], succ=[0x3eab]
    =================================
    0x1d26: v1d26(0x6) = CONST 
    0x1d28: v1d28 = SLOAD v1d26(0x6)
    0x1d29: v1d29(0x3eab) = CONST 
    0x1d2d: v1d2d(0xde0b6b3a7640000) = CONST 
    0x1d36: v1d36(0x29f2) = CONST 
    0x1d39: v1d39_0 = CALLPRIVATE v1d36(0x29f2), v1d2d(0xde0b6b3a7640000), v1d28, v1d29(0x3eab)

    Begin block 0x3eab
    prev=[0x1d25], succ=[0x1d3a0x1cfd]
    =================================
    0x3ead: v3ead(0x2a65) = CONST 
    0x3eb0: v3eb0_0 = CALLPRIVATE v3ead(0x2a65), v1d24_0, v1d39_0, v1d1b(0x1d3a)

    Begin block 0x1d3a0x1cfd
    prev=[0x3eab], succ=[]
    =================================
    0x1d3f0x1cfd: RETURNPRIVATE v1cfdarg0, v3eb0_0

    Begin block 0x3e88
    prev=[0x1d08], succ=[]
    =================================
    0x3e8b: RETURNPRIVATE v1cfdarg0, v1cfe(0x0)

}

function 0x266f(0x266farg0x0) private {
    Begin block 0x266f
    prev=[], succ=[0x26f5, 0x26f9]
    =================================
    0x2670: v2670(0x4) = CONST 
    0x2673: v2673 = SLOAD v2670(0x4)
    0x2674: v2674(0x5) = CONST 
    0x2676: v2676 = SLOAD v2674(0x5)
    0x2677: v2677(0x40) = CONST 
    0x267a: v267a = MLOAD v2677(0x40)
    0x267b: v267b(0xba54d3ec00000000000000000000000000000000000000000000000000000000) = CONST 
    0x269d: MSTORE v267a, v267b(0xba54d3ec00000000000000000000000000000000000000000000000000000000)
    0x269e: v269e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x26b5: v26b5 = AND v269e(0xffffffffffffffffffffffffffffffffffffffff), v2676
    0x26b8: v26b8 = ADD v267a, v2670(0x4)
    0x26bc: MSTORE v26b8, v26b5
    0x26bd: v26bd(0xde0b6b3a7640000) = CONST 
    0x26c6: v26c6(0x24) = CONST 
    0x26c9: v26c9 = ADD v267a, v26c6(0x24)
    0x26ca: MSTORE v26c9, v26bd(0xde0b6b3a7640000)
    0x26cb: v26cb = MLOAD v2677(0x40)
    0x26cc: v26cc(0x0) = CONST 
    0x26d2: v26d2 = AND v2673, v269e(0xffffffffffffffffffffffffffffffffffffffff)
    0x26d4: v26d4(0xba54d3ec) = CONST 
    0x26da: v26da(0x44) = CONST 
    0x26de: v26de = ADD v267a, v26da(0x44)
    0x26e0: v26e0(0x20) = CONST 
    0x26e8: v26e8(0x0) = SUB v267a, v26cb
    0x26e9: v26e9(0x44) = ADD v26e8(0x0), v26da(0x44)
    0x26ed: v26ed = EXTCODESIZE v26d2
    0x26ee: v26ee = ISZERO v26ed
    0x26f0: v26f0 = ISZERO v26ee
    0x26f1: v26f1(0x26f9) = CONST 
    0x26f4: JUMPI v26f1(0x26f9), v26f0

    Begin block 0x26f5
    prev=[0x266f], succ=[]
    =================================
    0x26f5: v26f5(0x0) = CONST 
    0x26f8: REVERT v26f5(0x0), v26f5(0x0)

    Begin block 0x26f9
    prev=[0x266f], succ=[0x271e, 0x2707]
    =================================
    0x26fb: v26fb = GAS 
    0x26fc: v26fc = STATICCALL v26fb, v26d2, v26cb, v26e9(0x44), v26cb, v26e0(0x20)
    0x2702: v2702 = ISZERO v26fc
    0x2703: v2703(0x271e) = CONST 
    0x2706: JUMPI v2703(0x271e), v2702

    Begin block 0x271e
    prev=[0x26f9, 0x2719], succ=[0x2723, 0x27730x266f]
    =================================
    0x271e_0x0: v271e_0 = PHI v26fc, v271c(0x1)
    0x271f: v271f(0x2773) = CONST 
    0x2722: JUMPI v271f(0x2773), v271e_0

    Begin block 0x2723
    prev=[0x271e], succ=[]
    =================================
    0x2723: v2723(0x40) = CONST 
    0x2725: v2725 = MLOAD v2723(0x40)
    0x2726: v2726(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2748: MSTORE v2725, v2726(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2749: v2749(0x4) = CONST 
    0x274b: v274b = ADD v2749(0x4), v2725
    0x274e: v274e(0x20) = CONST 
    0x2750: v2750 = ADD v274e(0x20), v274b
    0x2753: v2753(0x20) = SUB v2750, v274b
    0x2755: MSTORE v274b, v2753(0x20)
    0x2756: v2756(0x3d) = CONST 
    0x2759: MSTORE v2750, v2756(0x3d)
    0x275a: v275a(0x20) = CONST 
    0x275c: v275c = ADD v275a(0x20), v2750
    0x275e: v275e(0x3223) = CONST 
    0x2761: v2761(0x3d) = CONST 
    0x2764: CODECOPY v275c, v275e(0x3223), v2761(0x3d)
    0x2765: v2765(0x40) = CONST 
    0x2767: v2767 = ADD v2765(0x40), v275c
    0x276b: v276b(0x40) = CONST 
    0x276d: v276d = MLOAD v276b(0x40)
    0x2770: v2770(0x84) = SUB v2767, v276d
    0x2772: REVERT v276d, v2770(0x84)

    Begin block 0x27730x266f
    prev=[0x271e], succ=[0x9440x266f]
    =================================
    0x27760x266f: v266f2776(0x944) = CONST 
    0x27790x266f: JUMP v266f2776(0x944)

    Begin block 0x9440x266f
    prev=[0x27730x266f], succ=[]
    =================================
    0x9440x266f_0x0: v944266f_0 = PHI v26cc(0x0), v271b
    0x9460x266f: RETURNPRIVATE v266farg0, v944266f_0

    Begin block 0x2707
    prev=[0x26f9], succ=[0x2715, 0x2719]
    =================================
    0x2708: v2708(0x40) = CONST 
    0x270a: v270a = MLOAD v2708(0x40)
    0x270b: v270b = RETURNDATASIZE 
    0x270c: v270c(0x20) = CONST 
    0x270f: v270f = LT v270b, v270c(0x20)
    0x2710: v2710 = ISZERO v270f
    0x2711: v2711(0x2719) = CONST 
    0x2714: JUMPI v2711(0x2719), v2710

    Begin block 0x2715
    prev=[0x2707], succ=[]
    =================================
    0x2715: v2715(0x0) = CONST 
    0x2718: REVERT v2715(0x0), v2715(0x0)

    Begin block 0x2719
    prev=[0x2707], succ=[0x271e]
    =================================
    0x271b: v271b = MLOAD v270a
    0x271c: v271c(0x1) = CONST 

}

function 0x2780(0x2780arg0x0) private {
    Begin block 0x2780
    prev=[], succ=[0x278b]
    =================================
    0x2781: v2781(0x0) = CONST 
    0x2784: v2784(0x278b) = CONST 
    0x2787: v2787(0x266f) = CONST 
    0x278a: v278a_0 = CALLPRIVATE v2787(0x266f), v2784(0x278b)

    Begin block 0x278b
    prev=[0x2780], succ=[0x279e, 0x3ef5]
    =================================
    0x278e: v278e(0xde0b6b3a7640000) = CONST 
    0x2798: v2798 = LT v278a_0, v278e(0xde0b6b3a7640000)
    0x2799: v2799 = ISZERO v2798
    0x279a: v279a(0x3ef5) = CONST 
    0x279d: JUMPI v279a(0x3ef5), v2799

    Begin block 0x279e
    prev=[0x278b], succ=[0x27a5, 0x27b4]
    =================================
    0x279e: v279e(0x9) = CONST 
    0x27a0: v27a0 = SLOAD v279e(0x9)
    0x27a1: v27a1(0x27b4) = CONST 
    0x27a4: JUMPI v27a1(0x27b4), v27a0

    Begin block 0x27a5
    prev=[0x279e], succ=[0x3f18]
    =================================
    0x27a5: v27a5(0xde0b6b3a7640000) = CONST 
    0x27b0: v27b0(0x3f18) = CONST 
    0x27b3: JUMP v27b0(0x3f18)

    Begin block 0x3f18
    prev=[0x27a5], succ=[]
    =================================
    0x3f1b: RETURNPRIVATE v2780arg0, v27a5(0xde0b6b3a7640000)

    Begin block 0x27b4
    prev=[0x279e], succ=[0x3f3b]
    =================================
    0x27b5: v27b5(0x0) = CONST 
    0x27b7: v27b7(0x27cc) = CONST 
    0x27bb: v27bb(0x3f3b) = CONST 
    0x27be: v27be(0xde0b6b3a7640000) = CONST 
    0x27c8: v27c8(0x29f2) = CONST 
    0x27cb: v27cb_0 = CALLPRIVATE v27c8(0x29f2), v27be(0xde0b6b3a7640000), v27be(0xde0b6b3a7640000), v27bb(0x3f3b)

    Begin block 0x3f3b
    prev=[0x27b4], succ=[0x27cc]
    =================================
    0x3f3d: v3f3d(0x2a65) = CONST 
    0x3f40: v3f40_0 = CALLPRIVATE v3f3d(0x2a65), v278a_0, v27cb_0, v27b7(0x27cc)

    Begin block 0x27cc
    prev=[0x3f3b], succ=[0x29b0B0x27cc]
    =================================
    0x27cf: v27cf(0x0) = CONST 
    0x27d1: v27d1(0x27f7) = CONST 
    0x27d4: v27d4(0x2710) = CONST 
    0x27d7: v27d7(0x3f60) = CONST 
    0x27da: v27da(0x9) = CONST 
    0x27dc: v27dc = SLOAD v27da(0x9)
    0x27dd: v27dd(0x3f85) = CONST 
    0x27e0: v27e0(0xde0b6b3a7640000) = CONST 
    0x27ea: v27ea(0x29b0) = CONST 
    0x27f0: v27f0(0xffffffff) = CONST 
    0x27f5: v27f5(0x29b0) = AND v27f0(0xffffffff), v27ea(0x29b0)
    0x27f6: JUMP v27f5(0x29b0)

    Begin block 0x29b0B0x27cc
    prev=[0x27cc], succ=[0x29a70x29b0B0x27cc]
    =================================
    0x29b1S0x27cc: v29b1V27cc(0x0) = CONST 
    0x29b3S0x27cc: v29b3V27cc(0x29a7) = CONST 
    0x29b8S0x27cc: v29b8V27cc(0x40) = CONST 
    0x29baS0x27cc: v29baV27cc = MLOAD v29b8V27cc(0x40)
    0x29bcS0x27cc: v29bcV27cc(0x40) = CONST 
    0x29beS0x27cc: v29beV27cc = ADD v29bcV27cc(0x40), v29baV27cc
    0x29bfS0x27cc: v29bfV27cc(0x40) = CONST 
    0x29c1S0x27cc: MSTORE v29bfV27cc(0x40), v29beV27cc
    0x29c3S0x27cc: v29c3V27cc(0x1e) = CONST 
    0x29c6S0x27cc: MSTORE v29baV27cc, v29c3V27cc(0x1e)
    0x29c7S0x27cc: v29c7V27cc(0x20) = CONST 
    0x29c9S0x27cc: v29c9V27cc = ADD v29c7V27cc(0x20), v29baV27cc
    0x29caS0x27cc: v29caV27cc(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x27cc: MSTORE v29c9V27cc, v29caV27cc(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x27cc: v29eeV27cc(0x2bef) = CONST 
    0x29f1S0x27cc: v29f1_0V27cc = CALLPRIVATE v29eeV27cc(0x2bef), v29baV27cc, v27e0(0xde0b6b3a7640000), v3f40_0, v29b3V27cc(0x29a7)

    Begin block 0x29a70x29b0B0x27cc
    prev=[0x29b0B0x27cc], succ=[0x29aa0x29b0B0x27cc]
    =================================

    Begin block 0x29aa0x29b0B0x27cc
    prev=[0x29a70x29b0B0x27cc], succ=[0x3f85]
    =================================
    0x29af0x29b0S0x27cc: JUMP v27dd(0x3f85)

    Begin block 0x3f85
    prev=[0x29aa0x29b0B0x27cc], succ=[0x3f60]
    =================================
    0x3f87: v3f87(0x29f2) = CONST 
    0x3f8a: v3f8a_0 = CALLPRIVATE v3f87(0x29f2), v27dc, v29f1_0V27cc, v27d7(0x3f60)

    Begin block 0x3f60
    prev=[0x3f85], succ=[0x27f7]
    =================================
    0x3f62: v3f62(0x2a65) = CONST 
    0x3f65: v3f65_0 = CALLPRIVATE v3f62(0x2a65), v27d4(0x2710), v3f8a_0, v27d1(0x27f7)

    Begin block 0x27f7
    prev=[0x3f60], succ=[0x280b]
    =================================
    0x27fa: v27fa(0x280b) = CONST 
    0x27fd: v27fd(0xde0b6b3a7640000) = CONST 
    0x2807: v2807(0x2933) = CONST 
    0x280a: v280a_0 = CALLPRIVATE v2807(0x2933), v3f65_0, v27fd(0xde0b6b3a7640000), v27fa(0x280b)

    Begin block 0x280b
    prev=[0x27f7], succ=[0x281f, 0x281b]
    =================================
    0x280c: v280c(0xa) = CONST 
    0x280e: v280e = SLOAD v280c(0xa)
    0x2813: v2813 = ISZERO v280e
    0x2815: v2815 = ISZERO v2813
    0x2817: v2817(0x281f) = CONST 
    0x281a: JUMPI v2817(0x281f), v2813

    Begin block 0x281f
    prev=[0x280b, 0x281b], succ=[0x2828, 0x2825]
    =================================
    0x281f_0x0: v281f_0 = PHI v2815, v281e
    0x2820: v2820 = ISZERO v281f_0
    0x2821: v2821(0x2828) = CONST 
    0x2824: JUMPI v2821(0x2828), v2820

    Begin block 0x2828
    prev=[0x281f, 0x2825], succ=[]
    =================================
    0x2828_0x4: v2828_4 = PHI v280e, v280a_0
    0x282e: RETURNPRIVATE v2780arg0, v2828_4

    Begin block 0x2825
    prev=[0x281f], succ=[0x2828]
    =================================

    Begin block 0x281b
    prev=[0x280b], succ=[0x281f]
    =================================
    0x281e: v281e = GT v280a_0, v280e

    Begin block 0x3ef5
    prev=[0x278b], succ=[]
    =================================
    0x3ef8: RETURNPRIVATE v2780arg0, v2781(0x0)

}

function 0x282f(0x282farg0x0) private {
    Begin block 0x282f
    prev=[], succ=[0x28b5, 0x28b9]
    =================================
    0x2830: v2830(0x4) = CONST 
    0x2833: v2833 = SLOAD v2830(0x4)
    0x2834: v2834(0x5) = CONST 
    0x2836: v2836 = SLOAD v2834(0x5)
    0x2837: v2837(0x40) = CONST 
    0x283a: v283a = MLOAD v2837(0x40)
    0x283b: v283b(0x6bfb05f900000000000000000000000000000000000000000000000000000000) = CONST 
    0x285d: MSTORE v283a, v283b(0x6bfb05f900000000000000000000000000000000000000000000000000000000)
    0x285e: v285e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2875: v2875 = AND v285e(0xffffffffffffffffffffffffffffffffffffffff), v2836
    0x2878: v2878 = ADD v283a, v2830(0x4)
    0x287c: MSTORE v2878, v2875
    0x287d: v287d(0xde0b6b3a7640000) = CONST 
    0x2886: v2886(0x24) = CONST 
    0x2889: v2889 = ADD v283a, v2886(0x24)
    0x288a: MSTORE v2889, v287d(0xde0b6b3a7640000)
    0x288b: v288b = MLOAD v2837(0x40)
    0x288c: v288c(0x0) = CONST 
    0x2892: v2892 = AND v2833, v285e(0xffffffffffffffffffffffffffffffffffffffff)
    0x2894: v2894(0x6bfb05f9) = CONST 
    0x289a: v289a(0x44) = CONST 
    0x289e: v289e = ADD v283a, v289a(0x44)
    0x28a0: v28a0(0x20) = CONST 
    0x28a8: v28a8(0x0) = SUB v283a, v288b
    0x28a9: v28a9(0x44) = ADD v28a8(0x0), v289a(0x44)
    0x28ad: v28ad = EXTCODESIZE v2892
    0x28ae: v28ae = ISZERO v28ad
    0x28b0: v28b0 = ISZERO v28ae
    0x28b1: v28b1(0x28b9) = CONST 
    0x28b4: JUMPI v28b1(0x28b9), v28b0

    Begin block 0x28b5
    prev=[0x282f], succ=[]
    =================================
    0x28b5: v28b5(0x0) = CONST 
    0x28b8: REVERT v28b5(0x0), v28b5(0x0)

    Begin block 0x28b9
    prev=[0x282f], succ=[0x28de, 0x28c7]
    =================================
    0x28bb: v28bb = GAS 
    0x28bc: v28bc = STATICCALL v28bb, v2892, v288b, v28a9(0x44), v288b, v28a0(0x20)
    0x28c2: v28c2 = ISZERO v28bc
    0x28c3: v28c3(0x28de) = CONST 
    0x28c6: JUMPI v28c3(0x28de), v28c2

    Begin block 0x28de
    prev=[0x28b9, 0x28d9], succ=[0x28e3, 0x27730x282f]
    =================================
    0x28de_0x0: v28de_0 = PHI v28bc, v28dc(0x1)
    0x28df: v28df(0x2773) = CONST 
    0x28e2: JUMPI v28df(0x2773), v28de_0

    Begin block 0x28e3
    prev=[0x28de], succ=[]
    =================================
    0x28e3: v28e3(0x40) = CONST 
    0x28e5: v28e5 = MLOAD v28e3(0x40)
    0x28e6: v28e6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2908: MSTORE v28e5, v28e6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2909: v2909(0x4) = CONST 
    0x290b: v290b = ADD v2909(0x4), v28e5
    0x290e: v290e(0x20) = CONST 
    0x2910: v2910 = ADD v290e(0x20), v290b
    0x2913: v2913(0x20) = SUB v2910, v290b
    0x2915: MSTORE v290b, v2913(0x20)
    0x2916: v2916(0x3c) = CONST 
    0x2919: MSTORE v2910, v2916(0x3c)
    0x291a: v291a(0x20) = CONST 
    0x291c: v291c = ADD v291a(0x20), v2910
    0x291e: v291e(0x3087) = CONST 
    0x2921: v2921(0x3c) = CONST 
    0x2924: CODECOPY v291c, v291e(0x3087), v2921(0x3c)
    0x2925: v2925(0x40) = CONST 
    0x2927: v2927 = ADD v2925(0x40), v291c
    0x292b: v292b(0x40) = CONST 
    0x292d: v292d = MLOAD v292b(0x40)
    0x2930: v2930(0x84) = SUB v2927, v292d
    0x2932: REVERT v292d, v2930(0x84)

    Begin block 0x27730x282f
    prev=[0x28de], succ=[0x9440x282f]
    =================================
    0x27760x282f: v282f2776(0x944) = CONST 
    0x27790x282f: JUMP v282f2776(0x944)

    Begin block 0x9440x282f
    prev=[0x27730x282f], succ=[]
    =================================
    0x9440x282f_0x0: v944282f_0 = PHI v288c(0x0), v28db
    0x9460x282f: RETURNPRIVATE v282farg0, v944282f_0

    Begin block 0x28c7
    prev=[0x28b9], succ=[0x28d5, 0x28d9]
    =================================
    0x28c8: v28c8(0x40) = CONST 
    0x28ca: v28ca = MLOAD v28c8(0x40)
    0x28cb: v28cb = RETURNDATASIZE 
    0x28cc: v28cc(0x20) = CONST 
    0x28cf: v28cf = LT v28cb, v28cc(0x20)
    0x28d0: v28d0 = ISZERO v28cf
    0x28d1: v28d1(0x28d9) = CONST 
    0x28d4: JUMPI v28d1(0x28d9), v28d0

    Begin block 0x28d5
    prev=[0x28c7], succ=[]
    =================================
    0x28d5: v28d5(0x0) = CONST 
    0x28d8: REVERT v28d5(0x0), v28d5(0x0)

    Begin block 0x28d9
    prev=[0x28c7], succ=[0x28de]
    =================================
    0x28db: v28db = MLOAD v28ca
    0x28dc: v28dc(0x1) = CONST 

}

function 0x2933(0x2933arg0x0, 0x2933arg0x1, 0x2933arg0x2) private {
    Begin block 0x2933
    prev=[], succ=[0x2941, 0x29a70x2933]
    =================================
    0x2934: v2934(0x0) = CONST 
    0x2938: v2938 = ADD v2933arg0, v2933arg1
    0x293b: v293b = LT v2938, v2933arg1
    0x293c: v293c = ISZERO v293b
    0x293d: v293d(0x29a7) = CONST 
    0x2940: JUMPI v293d(0x29a7), v293c

    Begin block 0x2941
    prev=[0x2933], succ=[]
    =================================
    0x2941: v2941(0x40) = CONST 
    0x2944: v2944 = MLOAD v2941(0x40)
    0x2945: v2945(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2967: MSTORE v2944, v2945(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2968: v2968(0x20) = CONST 
    0x296a: v296a(0x4) = CONST 
    0x296d: v296d = ADD v2944, v296a(0x4)
    0x296e: MSTORE v296d, v2968(0x20)
    0x296f: v296f(0x1b) = CONST 
    0x2971: v2971(0x24) = CONST 
    0x2974: v2974 = ADD v2944, v2971(0x24)
    0x2975: MSTORE v2974, v296f(0x1b)
    0x2976: v2976(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000) = CONST 
    0x2997: v2997(0x44) = CONST 
    0x299a: v299a = ADD v2944, v2997(0x44)
    0x299b: MSTORE v299a, v2976(0x536166654d6174683a206164646974696f6e206f766572666c6f770000000000)
    0x299d: v299d = MLOAD v2941(0x40)
    0x29a1: v29a1(0x0) = SUB v2944, v299d
    0x29a2: v29a2(0x64) = CONST 
    0x29a4: v29a4(0x64) = ADD v29a2(0x64), v29a1(0x0)
    0x29a6: REVERT v299d, v29a4(0x64)

    Begin block 0x29a70x2933
    prev=[0x2933], succ=[0x29aa0x2933]
    =================================

    Begin block 0x29aa0x2933
    prev=[0x29a70x2933], succ=[]
    =================================
    0x29af0x2933: RETURNPRIVATE v2933arg2, v2938

}

function 0x29f2(0x29f2arg0x0, 0x29f2arg0x1, 0x29f2arg0x2) private {
    Begin block 0x29f2
    prev=[], succ=[0x2a010x29f2, 0x29fa0x29f2]
    =================================
    0x29f3: v29f3(0x0) = CONST 
    0x29f6: v29f6(0x2a01) = CONST 
    0x29f9: JUMPI v29f6(0x2a01), v29f2arg1

    Begin block 0x2a010x29f2
    prev=[0x29f2], succ=[0x2a0d0x29f2, 0x2a0e0x29f2]
    =================================
    0x2a040x29f2: v29f22a04 = MUL v29f2arg0, v29f2arg1
    0x2a090x29f2: v29f22a09(0x2a0e) = CONST 
    0x2a0c0x29f2: JUMPI v29f22a09(0x2a0e), v29f2arg1

    Begin block 0x2a0d0x29f2
    prev=[0x2a010x29f2], succ=[]
    =================================
    0x2a0d0x29f2: THROW 

    Begin block 0x2a0e0x29f2
    prev=[0x2a010x29f2], succ=[0x2a150x29f2, 0x29a70x29f2]
    =================================
    0x2a0f0x29f2: v29f22a0f = DIV v29f22a04, v29f2arg1
    0x2a100x29f2: v29f22a10 = EQ v29f22a0f, v29f2arg0
    0x2a110x29f2: v29f22a11(0x29a7) = CONST 
    0x2a140x29f2: JUMPI v29f22a11(0x29a7), v29f22a10

    Begin block 0x2a150x29f2
    prev=[0x2a0e0x29f2], succ=[]
    =================================
    0x2a150x29f2: v29f22a15(0x40) = CONST 
    0x2a170x29f2: v29f22a17 = MLOAD v29f22a15(0x40)
    0x2a180x29f2: v29f22a18(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2a3a0x29f2: MSTORE v29f22a17, v29f22a18(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2a3b0x29f2: v29f22a3b(0x4) = CONST 
    0x2a3d0x29f2: v29f22a3d = ADD v29f22a3b(0x4), v29f22a17
    0x2a400x29f2: v29f22a40(0x20) = CONST 
    0x2a420x29f2: v29f22a42 = ADD v29f22a40(0x20), v29f22a3d
    0x2a450x29f2: v29f22a45(0x20) = SUB v29f22a42, v29f22a3d
    0x2a470x29f2: MSTORE v29f22a3d, v29f22a45(0x20)
    0x2a480x29f2: v29f22a48(0x21) = CONST 
    0x2a4b0x29f2: MSTORE v29f22a42, v29f22a48(0x21)
    0x2a4c0x29f2: v29f22a4c(0x20) = CONST 
    0x2a4e0x29f2: v29f22a4e = ADD v29f22a4c(0x20), v29f22a42
    0x2a500x29f2: v29f22a50(0x3202) = CONST 
    0x2a530x29f2: v29f22a53(0x21) = CONST 
    0x2a560x29f2: CODECOPY v29f22a4e, v29f22a50(0x3202), v29f22a53(0x21)
    0x2a570x29f2: v29f22a57(0x40) = CONST 
    0x2a590x29f2: v29f22a59 = ADD v29f22a57(0x40), v29f22a4e
    0x2a5d0x29f2: v29f22a5d(0x40) = CONST 
    0x2a5f0x29f2: v29f22a5f = MLOAD v29f22a5d(0x40)
    0x2a620x29f2: v29f22a62(0x84) = SUB v29f22a59, v29f22a5f
    0x2a640x29f2: REVERT v29f22a5f, v29f22a62(0x84)

    Begin block 0x29a70x29f2
    prev=[0x2a0e0x29f2], succ=[0x29aa0x29f2]
    =================================

    Begin block 0x29aa0x29f2
    prev=[0x29fa0x29f2, 0x29a70x29f2], succ=[]
    =================================
    0x29aa0x29f2_0x0: v29aa29f2_0 = PHI v29f22a04, v29f229fb(0x0)
    0x29af0x29f2: RETURNPRIVATE v29f2arg2, v29aa29f2_0

    Begin block 0x29fa0x29f2
    prev=[0x29f2], succ=[0x29aa0x29f2]
    =================================
    0x29fb0x29f2: v29f229fb(0x0) = CONST 
    0x29fd0x29f2: v29f229fd(0x29aa) = CONST 
    0x2a000x29f2: JUMP v29f229fd(0x29aa)

}

function 0x2a65(0x2a65arg0x0, 0x2a65arg0x1, 0x2a65arg0x2) private {
    Begin block 0x2a65
    prev=[], succ=[0x2ca50x2a65]
    =================================
    0x2a66: v2a66(0x0) = CONST 
    0x2a68: v2a68(0x29a7) = CONST 
    0x2a6d: v2a6d(0x40) = CONST 
    0x2a6f: v2a6f = MLOAD v2a6d(0x40)
    0x2a71: v2a71(0x40) = CONST 
    0x2a73: v2a73 = ADD v2a71(0x40), v2a6f
    0x2a74: v2a74(0x40) = CONST 
    0x2a76: MSTORE v2a74(0x40), v2a73
    0x2a78: v2a78(0x1a) = CONST 
    0x2a7b: MSTORE v2a6f, v2a78(0x1a)
    0x2a7c: v2a7c(0x20) = CONST 
    0x2a7e: v2a7e = ADD v2a7c(0x20), v2a6f
    0x2a7f: v2a7f(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000) = CONST 
    0x2aa1: MSTORE v2a7e, v2a7f(0x536166654d6174683a206469766973696f6e206279207a65726f000000000000)
    0x2aa3: v2aa3(0x2ca5) = CONST 
    0x2aa6: JUMP v2aa3(0x2ca5)

    Begin block 0x2ca50x2a65
    prev=[0x2a65], succ=[0x2cae0x2a65, 0x2d0e0x2a65]
    =================================
    0x2ca60x2a65: v2a652ca6(0x0) = CONST 
    0x2caa0x2a65: v2a652caa(0x2d0e) = CONST 
    0x2cad0x2a65: JUMPI v2a652caa(0x2d0e), v2a65arg0

    Begin block 0x2cae0x2a65
    prev=[0x2ca50x2a65], succ=[0x2cff0x2a65, 0x2c5d0x2a65]
    =================================
    0x2cae0x2a65: v2a652cae(0x40) = CONST 
    0x2cb00x2a65: v2a652cb0 = MLOAD v2a652cae(0x40)
    0x2cb10x2a65: v2a652cb1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2cd30x2a65: MSTORE v2a652cb0, v2a652cb1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2cd40x2a65: v2a652cd4(0x20) = CONST 
    0x2cd60x2a65: v2a652cd6(0x4) = CONST 
    0x2cd90x2a65: v2a652cd9 = ADD v2a652cb0, v2a652cd6(0x4)
    0x2cdc0x2a65: MSTORE v2a652cd9, v2a652cd4(0x20)
    0x2cde0x2a65: v2a652cde(0x1a) = MLOAD v2a6f
    0x2cdf0x2a65: v2a652cdf(0x24) = CONST 
    0x2ce20x2a65: v2a652ce2 = ADD v2a652cb0, v2a652cdf(0x24)
    0x2ce30x2a65: MSTORE v2a652ce2, v2a652cde(0x1a)
    0x2ce50x2a65: v2a652ce5(0x1a) = MLOAD v2a6f
    0x2cea0x2a65: v2a652cea(0x44) = CONST 
    0x2cee0x2a65: v2a652cee = ADD v2a652cb0, v2a652cea(0x44)
    0x2cf20x2a65: v2a652cf2 = ADD v2a6f, v2a652cd4(0x20)
    0x2cf70x2a65: v2a652cf7(0x0) = CONST 
    0x2cfa0x2a65: v2a652cfa = ISZERO v2a652ce5(0x1a)
    0x2cfb0x2a65: v2a652cfb(0x2c5d) = CONST 
    0x2cfe0x2a65: JUMPI v2a652cfb(0x2c5d), v2a652cfa

    Begin block 0x2cff0x2a65
    prev=[0x2cae0x2a65], succ=[0x2c450x2a65]
    =================================
    0x2d010x2a65: v2a652d01 = ADD v2a652cf7(0x0), v2a652cf2
    0x2d020x2a65: v2a652d02 = MLOAD v2a652d01
    0x2d050x2a65: v2a652d05 = ADD v2a652cf7(0x0), v2a652cee
    0x2d060x2a65: MSTORE v2a652d05, v2a652d02
    0x2d070x2a65: v2a652d07(0x20) = CONST 
    0x2d090x2a65: v2a652d09(0x20) = ADD v2a652d07(0x20), v2a652cf7(0x0)
    0x2d0a0x2a65: v2a652d0a(0x2c45) = CONST 
    0x2d0d0x2a65: JUMP v2a652d0a(0x2c45)

    Begin block 0x2c450x2a65
    prev=[0x2cff0x2a65, 0x2c4e0x2a65], succ=[0x2c5d0x2a65, 0x2c4e0x2a65]
    =================================
    0x2c450x2a65_0x0: v2c452a65_0 = PHI v2a652d09(0x20), v2a652c58
    0x2c480x2a65: v2a652c48 = LT v2c452a65_0, v2a652ce5(0x1a)
    0x2c490x2a65: v2a652c49 = ISZERO v2a652c48
    0x2c4a0x2a65: v2a652c4a(0x2c5d) = CONST 
    0x2c4d0x2a65: JUMPI v2a652c4a(0x2c5d), v2a652c49

    Begin block 0x2c5d0x2a65
    prev=[0x2cae0x2a65, 0x2c450x2a65], succ=[0x2c8a0x2a65, 0x2c710x2a65]
    =================================
    0x2c660x2a65: v2a652c66 = ADD v2a652ce5(0x1a), v2a652cee
    0x2c680x2a65: v2a652c68(0x1f) = CONST 
    0x2c6a0x2a65: v2a652c6a(0x1a) = AND v2a652c68(0x1f), v2a652ce5(0x1a)
    0x2c6c0x2a65: v2a652c6c = ISZERO v2a652c6a(0x1a)
    0x2c6d0x2a65: v2a652c6d(0x2c8a) = CONST 
    0x2c700x2a65: JUMPI v2a652c6d(0x2c8a), v2a652c6c

    Begin block 0x2c8a0x2a65
    prev=[0x2c5d0x2a65, 0x2c710x2a65], succ=[]
    =================================
    0x2c8a0x2a65_0x1: v2c8a2a65_1 = PHI v2a652c87, v2a652c66
    0x2c900x2a65: v2a652c90(0x40) = CONST 
    0x2c920x2a65: v2a652c92 = MLOAD v2a652c90(0x40)
    0x2c950x2a65: v2a652c95 = SUB v2c8a2a65_1, v2a652c92
    0x2c970x2a65: REVERT v2a652c92, v2a652c95

    Begin block 0x2c710x2a65
    prev=[0x2c5d0x2a65], succ=[0x2c8a0x2a65]
    =================================
    0x2c730x2a65: v2a652c73 = SUB v2a652c66, v2a652c6a(0x1a)
    0x2c750x2a65: v2a652c75 = MLOAD v2a652c73
    0x2c760x2a65: v2a652c76(0x1) = CONST 
    0x2c790x2a65: v2a652c79(0x20) = CONST 
    0x2c7b0x2a65: v2a652c7b(0x6) = SUB v2a652c79(0x20), v2a652c6a(0x1a)
    0x2c7c0x2a65: v2a652c7c(0x100) = CONST 
    0x2c7f0x2a65: v2a652c7f(0x1000000000000) = EXP v2a652c7c(0x100), v2a652c7b(0x6)
    0x2c800x2a65: v2a652c80(0xffffffffffff) = SUB v2a652c7f(0x1000000000000), v2a652c76(0x1)
    0x2c810x2a65: v2a652c81 = NOT v2a652c80(0xffffffffffff)
    0x2c820x2a65: v2a652c82 = AND v2a652c81, v2a652c75
    0x2c840x2a65: MSTORE v2a652c73, v2a652c82
    0x2c850x2a65: v2a652c85(0x20) = CONST 
    0x2c870x2a65: v2a652c87 = ADD v2a652c85(0x20), v2a652c73

    Begin block 0x2c4e0x2a65
    prev=[0x2c450x2a65], succ=[0x2c450x2a65]
    =================================
    0x2c4e0x2a65_0x0: v2c4e2a65_0 = PHI v2a652d09(0x20), v2a652c58
    0x2c500x2a65: v2a652c50 = ADD v2c4e2a65_0, v2a652cf2
    0x2c510x2a65: v2a652c51 = MLOAD v2a652c50
    0x2c540x2a65: v2a652c54 = ADD v2c4e2a65_0, v2a652cee
    0x2c550x2a65: MSTORE v2a652c54, v2a652c51
    0x2c560x2a65: v2a652c56(0x20) = CONST 
    0x2c580x2a65: v2a652c58 = ADD v2a652c56(0x20), v2c4e2a65_0
    0x2c590x2a65: v2a652c59(0x2c45) = CONST 
    0x2c5c0x2a65: JUMP v2a652c59(0x2c45)

    Begin block 0x2d0e0x2a65
    prev=[0x2ca50x2a65], succ=[0x2d190x2a65, 0x2d1a0x2a65]
    =================================
    0x2d100x2a65: v2a652d10(0x0) = CONST 
    0x2d150x2a65: v2a652d15(0x2d1a) = CONST 
    0x2d180x2a65: JUMPI v2a652d15(0x2d1a), v2a65arg0

    Begin block 0x2d190x2a65
    prev=[0x2d0e0x2a65], succ=[]
    =================================
    0x2d190x2a65: THROW 

    Begin block 0x2d1a0x2a65
    prev=[0x2d0e0x2a65], succ=[0x29a70x2a65]
    =================================
    0x2d1b0x2a65: v2a652d1b = DIV v2a65arg1, v2a65arg0
    0x2d230x2a65: JUMP v2a68(0x29a7)

    Begin block 0x29a70x2a65
    prev=[0x2d1a0x2a65], succ=[0x29aa0x2a65]
    =================================

    Begin block 0x29aa0x2a65
    prev=[0x29a70x2a65], succ=[]
    =================================
    0x29af0x2a65: RETURNPRIVATE v2a65arg2, v2a652d1b

}

function 0x2b72(0x2b72arg0x0) private {
    Begin block 0x2b72
    prev=[], succ=[0x2bd7, 0x2bdb]
    =================================
    0x2b73: v2b73(0x4) = CONST 
    0x2b76: v2b76 = SLOAD v2b73(0x4)
    0x2b77: v2b77(0x40) = CONST 
    0x2b7a: v2b7a = MLOAD v2b77(0x40)
    0x2b7b: v2b7b(0xda303d9d00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2b9d: MSTORE v2b7a, v2b7b(0xda303d9d00000000000000000000000000000000000000000000000000000000)
    0x2b9f: v2b9f = MLOAD v2b77(0x40)
    0x2ba0: v2ba0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2bb7: v2bb7 = AND v2b76, v2ba0(0xffffffffffffffffffffffffffffffffffffffff)
    0x2bb9: v2bb9(0xda303d9d) = CONST 
    0x2bc1: v2bc1 = ADD v2b73(0x4), v2b7a
    0x2bc3: v2bc3(0x0) = CONST 
    0x2bc9: v2bc9(0x0) = SUB v2b7a, v2b9f
    0x2bca: v2bca(0x4) = ADD v2bc9(0x0), v2b73(0x4)
    0x2bcf: v2bcf = EXTCODESIZE v2bb7
    0x2bd0: v2bd0 = ISZERO v2bcf
    0x2bd2: v2bd2 = ISZERO v2bd0
    0x2bd3: v2bd3(0x2bdb) = CONST 
    0x2bd6: JUMPI v2bd3(0x2bdb), v2bd2

    Begin block 0x2bd7
    prev=[0x2b72], succ=[]
    =================================
    0x2bd7: v2bd7(0x0) = CONST 
    0x2bda: REVERT v2bd7(0x0), v2bd7(0x0)

    Begin block 0x2bdb
    prev=[0x2b72], succ=[0x2bec, 0x2be9]
    =================================
    0x2bdd: v2bdd = GAS 
    0x2bde: v2bde = CALL v2bdd, v2bb7, v2bc3(0x0), v2b9f, v2bca(0x4), v2b9f, v2bc3(0x0)
    0x2be4: v2be4 = ISZERO v2bde
    0x2be5: v2be5(0x2bec) = CONST 
    0x2be8: JUMPI v2be5(0x2bec), v2be4

    Begin block 0x2bec
    prev=[0x2bdb, 0x2be9], succ=[]
    =================================
    0x2bee: RETURNPRIVATE v2b72arg0

    Begin block 0x2be9
    prev=[0x2bdb], succ=[0x2bec]
    =================================
    0x2bea: v2bea(0x1) = CONST 

}

function 0x2bef(0x2befarg0x0, 0x2befarg0x1, 0x2befarg0x2, 0x2befarg0x3) private {
    Begin block 0x2bef
    prev=[], succ=[0x2bfb, 0x2c98]
    =================================
    0x2bf0: v2bf0(0x0) = CONST 
    0x2bf5: v2bf5 = GT v2befarg1, v2befarg2
    0x2bf6: v2bf6 = ISZERO v2bf5
    0x2bf7: v2bf7(0x2c98) = CONST 
    0x2bfa: JUMPI v2bf7(0x2c98), v2bf6

    Begin block 0x2bfb
    prev=[0x2bef], succ=[0x2c450x2bef]
    =================================
    0x2bfb: v2bfb(0x40) = CONST 
    0x2bfd: v2bfd = MLOAD v2bfb(0x40)
    0x2bfe: v2bfe(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2c20: MSTORE v2bfd, v2bfe(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2c21: v2c21(0x4) = CONST 
    0x2c23: v2c23 = ADD v2c21(0x4), v2bfd
    0x2c26: v2c26(0x20) = CONST 
    0x2c28: v2c28 = ADD v2c26(0x20), v2c23
    0x2c2b: v2c2b(0x20) = SUB v2c28, v2c23
    0x2c2d: MSTORE v2c23, v2c2b(0x20)
    0x2c31: v2c31 = MLOAD v2befarg0
    0x2c33: MSTORE v2c28, v2c31
    0x2c34: v2c34(0x20) = CONST 
    0x2c36: v2c36 = ADD v2c34(0x20), v2c28
    0x2c3a: v2c3a = MLOAD v2befarg0
    0x2c3c: v2c3c(0x20) = CONST 
    0x2c3e: v2c3e = ADD v2c3c(0x20), v2befarg0
    0x2c43: v2c43(0x0) = CONST 

    Begin block 0x2c450x2bef
    prev=[0x2bfb, 0x2c4e0x2bef], succ=[0x2c5d0x2bef, 0x2c4e0x2bef]
    =================================
    0x2c450x2bef_0x0: v2c452bef_0 = PHI v2c43(0x0), v2bef2c58
    0x2c480x2bef: v2bef2c48 = LT v2c452bef_0, v2c3a
    0x2c490x2bef: v2bef2c49 = ISZERO v2bef2c48
    0x2c4a0x2bef: v2bef2c4a(0x2c5d) = CONST 
    0x2c4d0x2bef: JUMPI v2bef2c4a(0x2c5d), v2bef2c49

    Begin block 0x2c5d0x2bef
    prev=[0x2c450x2bef], succ=[0x2c8a0x2bef, 0x2c710x2bef]
    =================================
    0x2c660x2bef: v2bef2c66 = ADD v2c3a, v2c36
    0x2c680x2bef: v2bef2c68(0x1f) = CONST 
    0x2c6a0x2bef: v2bef2c6a = AND v2bef2c68(0x1f), v2c3a
    0x2c6c0x2bef: v2bef2c6c = ISZERO v2bef2c6a
    0x2c6d0x2bef: v2bef2c6d(0x2c8a) = CONST 
    0x2c700x2bef: JUMPI v2bef2c6d(0x2c8a), v2bef2c6c

    Begin block 0x2c8a0x2bef
    prev=[0x2c5d0x2bef, 0x2c710x2bef], succ=[]
    =================================
    0x2c8a0x2bef_0x1: v2c8a2bef_1 = PHI v2bef2c87, v2bef2c66
    0x2c900x2bef: v2bef2c90(0x40) = CONST 
    0x2c920x2bef: v2bef2c92 = MLOAD v2bef2c90(0x40)
    0x2c950x2bef: v2bef2c95 = SUB v2c8a2bef_1, v2bef2c92
    0x2c970x2bef: REVERT v2bef2c92, v2bef2c95

    Begin block 0x2c710x2bef
    prev=[0x2c5d0x2bef], succ=[0x2c8a0x2bef]
    =================================
    0x2c730x2bef: v2bef2c73 = SUB v2bef2c66, v2bef2c6a
    0x2c750x2bef: v2bef2c75 = MLOAD v2bef2c73
    0x2c760x2bef: v2bef2c76(0x1) = CONST 
    0x2c790x2bef: v2bef2c79(0x20) = CONST 
    0x2c7b0x2bef: v2bef2c7b = SUB v2bef2c79(0x20), v2bef2c6a
    0x2c7c0x2bef: v2bef2c7c(0x100) = CONST 
    0x2c7f0x2bef: v2bef2c7f = EXP v2bef2c7c(0x100), v2bef2c7b
    0x2c800x2bef: v2bef2c80 = SUB v2bef2c7f, v2bef2c76(0x1)
    0x2c810x2bef: v2bef2c81 = NOT v2bef2c80
    0x2c820x2bef: v2bef2c82 = AND v2bef2c81, v2bef2c75
    0x2c840x2bef: MSTORE v2bef2c73, v2bef2c82
    0x2c850x2bef: v2bef2c85(0x20) = CONST 
    0x2c870x2bef: v2bef2c87 = ADD v2bef2c85(0x20), v2bef2c73

    Begin block 0x2c4e0x2bef
    prev=[0x2c450x2bef], succ=[0x2c450x2bef]
    =================================
    0x2c4e0x2bef_0x0: v2c4e2bef_0 = PHI v2c43(0x0), v2bef2c58
    0x2c500x2bef: v2bef2c50 = ADD v2c4e2bef_0, v2c3e
    0x2c510x2bef: v2bef2c51 = MLOAD v2bef2c50
    0x2c540x2bef: v2bef2c54 = ADD v2c4e2bef_0, v2c36
    0x2c550x2bef: MSTORE v2bef2c54, v2bef2c51
    0x2c560x2bef: v2bef2c56(0x20) = CONST 
    0x2c580x2bef: v2bef2c58 = ADD v2bef2c56(0x20), v2c4e2bef_0
    0x2c590x2bef: v2bef2c59(0x2c45) = CONST 
    0x2c5c0x2bef: JUMP v2bef2c59(0x2c45)

    Begin block 0x2c98
    prev=[0x2bef], succ=[0x2c9e0x2bef]
    =================================
    0x2c9d: v2c9d = SUB v2befarg2, v2befarg1

    Begin block 0x2c9e0x2bef
    prev=[0x2c98], succ=[]
    =================================
    0x2ca40x2bef: RETURNPRIVATE v2befarg3, v2c9d

}

function fallback()() public {
    Begin block 0x3322
    prev=[], succ=[]
    =================================
    0x3323: v3323(0x0) = CONST 
    0x3326: REVERT v3323(0x0), v3323(0x0)

}

function nextEpochLength()() public {
    Begin block 0x346
    prev=[], succ=[0x8aaB0x346]
    =================================
    0x347: v347(0x3562) = CONST 
    0x34a: v34a(0x8aa) = CONST 
    0x34d: JUMP v34a(0x8aa)

    Begin block 0x8aaB0x346
    prev=[0x346], succ=[0x911B0x346, 0x9150x8aaB0x346]
    =================================
    0x8abS0x346: v8abV346(0x3) = CONST 
    0x8adS0x346: v8adV346 = SLOAD v8abV346(0x3)
    0x8aeS0x346: v8aeV346(0x40) = CONST 
    0x8b1S0x346: v8b1V346 = MLOAD v8aeV346(0x40)
    0x8b2S0x346: v8b2V346(0x7284ce900000000000000000000000000000000000000000000000000000000) = CONST 
    0x8d4S0x346: MSTORE v8b1V346, v8b2V346(0x7284ce900000000000000000000000000000000000000000000000000000000)
    0x8d6S0x346: v8d6V346 = MLOAD v8aeV346(0x40)
    0x8d7S0x346: v8d7V346(0x0) = CONST 
    0x8daS0x346: v8daV346(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x8efS0x346: v8efV346 = AND v8daV346(0xffffffffffffffffffffffffffffffffffffffff), v8adV346
    0x8f1S0x346: v8f1V346(0x7284ce9) = CONST 
    0x8f7S0x346: v8f7V346(0x4) = CONST 
    0x8fbS0x346: v8fbV346 = ADD v8b1V346, v8f7V346(0x4)
    0x8fdS0x346: v8fdV346(0x20) = CONST 
    0x904S0x346: v904V346(0x0) = SUB v8b1V346, v8d6V346
    0x905S0x346: v905V346(0x4) = ADD v904V346(0x0), v8f7V346(0x4)
    0x909S0x346: v909V346 = EXTCODESIZE v8efV346
    0x90aS0x346: v90aV346 = ISZERO v909V346
    0x90cS0x346: v90cV346 = ISZERO v90aV346
    0x90dS0x346: v90dV346(0x915) = CONST 
    0x910S0x346: JUMPI v90dV346(0x915), v90cV346

    Begin block 0x911B0x346
    prev=[0x8aaB0x346], succ=[]
    =================================
    0x911S0x346: v911V346(0x0) = CONST 
    0x914S0x346: REVERT v911V346(0x0), v911V346(0x0)

    Begin block 0x9150x8aaB0x346
    prev=[0x8aaB0x346], succ=[0x9200x8aaB0x346, 0x9290x8aaB0x346]
    =================================
    0x9170x8aaS0x346: v8aa917V346 = GAS 
    0x9180x8aaS0x346: v8aa918V346 = STATICCALL v8aa917V346, v8efV346, v8d6V346, v905V346(0x4), v8d6V346, v8fdV346(0x20)
    0x9190x8aaS0x346: v8aa919V346 = ISZERO v8aa918V346
    0x91b0x8aaS0x346: v8aa91bV346 = ISZERO v8aa919V346
    0x91c0x8aaS0x346: v8aa91cV346(0x929) = CONST 
    0x91f0x8aaS0x346: JUMPI v8aa91cV346(0x929), v8aa91bV346

    Begin block 0x9200x8aaB0x346
    prev=[0x9150x8aaB0x346], succ=[]
    =================================
    0x9200x8aaS0x346: v8aa920V346 = RETURNDATASIZE 
    0x9210x8aaS0x346: v8aa921V346(0x0) = CONST 
    0x9240x8aaS0x346: RETURNDATACOPY v8aa921V346(0x0), v8aa921V346(0x0), v8aa920V346
    0x9250x8aaS0x346: v8aa925V346 = RETURNDATASIZE 
    0x9260x8aaS0x346: v8aa926V346(0x0) = CONST 
    0x9280x8aaS0x346: REVERT v8aa926V346(0x0), v8aa925V346

    Begin block 0x9290x8aaB0x346
    prev=[0x9150x8aaB0x346], succ=[0x93b0x8aaB0x346, 0x93f0x8aaB0x346]
    =================================
    0x92e0x8aaS0x346: v8aa92eV346(0x40) = CONST 
    0x9300x8aaS0x346: v8aa930V346 = MLOAD v8aa92eV346(0x40)
    0x9310x8aaS0x346: v8aa931V346 = RETURNDATASIZE 
    0x9320x8aaS0x346: v8aa932V346(0x20) = CONST 
    0x9350x8aaS0x346: v8aa935V346 = LT v8aa931V346, v8aa932V346(0x20)
    0x9360x8aaS0x346: v8aa936V346 = ISZERO v8aa935V346
    0x9370x8aaS0x346: v8aa937V346(0x93f) = CONST 
    0x93a0x8aaS0x346: JUMPI v8aa937V346(0x93f), v8aa936V346

    Begin block 0x93b0x8aaB0x346
    prev=[0x9290x8aaB0x346], succ=[]
    =================================
    0x93b0x8aaS0x346: v8aa93bV346(0x0) = CONST 
    0x93e0x8aaS0x346: REVERT v8aa93bV346(0x0), v8aa93bV346(0x0)

    Begin block 0x93f0x8aaB0x346
    prev=[0x9290x8aaB0x346], succ=[0x9440x8aaB0x346]
    =================================
    0x9410x8aaS0x346: v8aa941V346 = MLOAD v8aa930V346

    Begin block 0x9440x8aaB0x346
    prev=[0x93f0x8aaB0x346], succ=[0x3562]
    =================================
    0x9460x8aaS0x346: JUMP v347(0x3562)

    Begin block 0x3562
    prev=[0x9440x8aaB0x346], succ=[]
    =================================
    0x3563: v3563(0x40) = CONST 
    0x3566: v3566 = MLOAD v3563(0x40)
    0x3569: MSTORE v3566, v8aa941V346
    0x356a: v356a = MLOAD v3563(0x40)
    0x356e: v356e(0x0) = SUB v3566, v356a
    0x356f: v356f(0x20) = CONST 
    0x3571: v3571(0x20) = ADD v356f(0x20), v356e(0x0)
    0x3573: RETURN v356a, v3571(0x20)

}

function setMaxRedeemableCouponPercentPerEpoch(uint256)() public {
    Begin block 0x360
    prev=[], succ=[0x372, 0x376]
    =================================
    0x361: v361(0x3593) = CONST 
    0x364: v364(0x4) = CONST 
    0x367: v367 = CALLDATASIZE 
    0x368: v368 = SUB v367, v364(0x4)
    0x369: v369(0x20) = CONST 
    0x36c: v36c = LT v368, v369(0x20)
    0x36d: v36d = ISZERO v36c
    0x36e: v36e(0x376) = CONST 
    0x371: JUMPI v36e(0x376), v36d

    Begin block 0x372
    prev=[0x360], succ=[]
    =================================
    0x372: v372(0x0) = CONST 
    0x375: REVERT v372(0x0), v372(0x0)

    Begin block 0x376
    prev=[0x360], succ=[0x947]
    =================================
    0x378: v378 = CALLDATALOAD v364(0x4)
    0x379: v379(0x947) = CONST 
    0x37c: JUMP v379(0x947)

    Begin block 0x947
    prev=[0x376], succ=[0x967, 0x9b7]
    =================================
    0x948: v948(0x1) = CONST 
    0x94a: v94a = SLOAD v948(0x1)
    0x94b: v94b(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x960: v960 = AND v94b(0xffffffffffffffffffffffffffffffffffffffff), v94a
    0x961: v961 = CALLER 
    0x962: v962 = EQ v961, v960
    0x963: v963(0x9b7) = CONST 
    0x966: JUMPI v963(0x9b7), v962

    Begin block 0x967
    prev=[0x947], succ=[]
    =================================
    0x967: v967(0x40) = CONST 
    0x969: v969 = MLOAD v967(0x40)
    0x96a: v96a(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x98c: MSTORE v969, v96a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x98d: v98d(0x4) = CONST 
    0x98f: v98f = ADD v98d(0x4), v969
    0x992: v992(0x20) = CONST 
    0x994: v994 = ADD v992(0x20), v98f
    0x997: v997(0x20) = SUB v994, v98f
    0x999: MSTORE v98f, v997(0x20)
    0x99a: v99a(0x28) = CONST 
    0x99d: MSTORE v994, v99a(0x28)
    0x99e: v99e(0x20) = CONST 
    0x9a0: v9a0 = ADD v99e(0x20), v994
    0x9a2: v9a2(0x311d) = CONST 
    0x9a5: v9a5(0x28) = CONST 
    0x9a8: CODECOPY v9a0, v9a2(0x311d), v9a5(0x28)
    0x9a9: v9a9(0x40) = CONST 
    0x9ab: v9ab = ADD v9a9(0x40), v9a0
    0x9af: v9af(0x40) = CONST 
    0x9b1: v9b1 = MLOAD v9af(0x40)
    0x9b4: v9b4(0x84) = SUB v9ab, v9b1
    0x9b6: REVERT v9b1, v9b4(0x84)

    Begin block 0x9b7
    prev=[0x947], succ=[0x9c2, 0xa28]
    =================================
    0x9b8: v9b8(0x2710) = CONST 
    0x9bc: v9bc = GT v378, v9b8(0x2710)
    0x9bd: v9bd = ISZERO v9bc
    0x9be: v9be(0xa28) = CONST 
    0x9c1: JUMPI v9be(0xa28), v9bd

    Begin block 0x9c2
    prev=[0x9b7], succ=[]
    =================================
    0x9c2: v9c2(0x40) = CONST 
    0x9c5: v9c5 = MLOAD v9c2(0x40)
    0x9c6: v9c6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x9e8: MSTORE v9c5, v9c6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9e9: v9e9(0x20) = CONST 
    0x9eb: v9eb(0x4) = CONST 
    0x9ee: v9ee = ADD v9c5, v9eb(0x4)
    0x9ef: MSTORE v9ee, v9e9(0x20)
    0x9f0: v9f0(0x9) = CONST 
    0x9f2: v9f2(0x24) = CONST 
    0x9f5: v9f5 = ADD v9c5, v9f2(0x24)
    0x9f6: MSTORE v9f5, v9f0(0x9)
    0x9f7: v9f7(0x6f76657220313030250000000000000000000000000000000000000000000000) = CONST 
    0xa18: va18(0x44) = CONST 
    0xa1b: va1b = ADD v9c5, va18(0x44)
    0xa1c: MSTORE va1b, v9f7(0x6f76657220313030250000000000000000000000000000000000000000000000)
    0xa1e: va1e = MLOAD v9c2(0x40)
    0xa22: va22(0x0) = SUB v9c5, va1e
    0xa23: va23(0x64) = CONST 
    0xa25: va25(0x64) = ADD va23(0x64), va22(0x0)
    0xa27: REVERT va1e, va25(0x64)

    Begin block 0xa28
    prev=[0x9b7], succ=[0x3593]
    =================================
    0xa29: va29(0xd) = CONST 
    0xa2b: SSTORE va29(0xd), v378
    0xa2c: JUMP v361(0x3593)

    Begin block 0x3593
    prev=[0xa28], succ=[]
    =================================
    0x3594: STOP 

}

function setDiscountPercent(uint256)() public {
    Begin block 0x37f
    prev=[], succ=[0x391, 0x395]
    =================================
    0x380: v380(0x35b4) = CONST 
    0x383: v383(0x4) = CONST 
    0x386: v386 = CALLDATASIZE 
    0x387: v387 = SUB v386, v383(0x4)
    0x388: v388(0x20) = CONST 
    0x38b: v38b = LT v387, v388(0x20)
    0x38c: v38c = ISZERO v38b
    0x38d: v38d(0x395) = CONST 
    0x390: JUMPI v38d(0x395), v38c

    Begin block 0x391
    prev=[0x37f], succ=[]
    =================================
    0x391: v391(0x0) = CONST 
    0x394: REVERT v391(0x0), v391(0x0)

    Begin block 0x395
    prev=[0x37f], succ=[0xa2d]
    =================================
    0x397: v397 = CALLDATALOAD v383(0x4)
    0x398: v398(0xa2d) = CONST 
    0x39b: JUMP v398(0xa2d)

    Begin block 0xa2d
    prev=[0x395], succ=[0xa4d, 0xa9d]
    =================================
    0xa2e: va2e(0x1) = CONST 
    0xa30: va30 = SLOAD va2e(0x1)
    0xa31: va31(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xa46: va46 = AND va31(0xffffffffffffffffffffffffffffffffffffffff), va30
    0xa47: va47 = CALLER 
    0xa48: va48 = EQ va47, va46
    0xa49: va49(0xa9d) = CONST 
    0xa4c: JUMPI va49(0xa9d), va48

    Begin block 0xa4d
    prev=[0xa2d], succ=[]
    =================================
    0xa4d: va4d(0x40) = CONST 
    0xa4f: va4f = MLOAD va4d(0x40)
    0xa50: va50(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xa72: MSTORE va4f, va50(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xa73: va73(0x4) = CONST 
    0xa75: va75 = ADD va73(0x4), va4f
    0xa78: va78(0x20) = CONST 
    0xa7a: va7a = ADD va78(0x20), va75
    0xa7d: va7d(0x20) = SUB va7a, va75
    0xa7f: MSTORE va75, va7d(0x20)
    0xa80: va80(0x28) = CONST 
    0xa83: MSTORE va7a, va80(0x28)
    0xa84: va84(0x20) = CONST 
    0xa86: va86 = ADD va84(0x20), va7a
    0xa88: va88(0x311d) = CONST 
    0xa8b: va8b(0x28) = CONST 
    0xa8e: CODECOPY va86, va88(0x311d), va8b(0x28)
    0xa8f: va8f(0x40) = CONST 
    0xa91: va91 = ADD va8f(0x40), va86
    0xa95: va95(0x40) = CONST 
    0xa97: va97 = MLOAD va95(0x40)
    0xa9a: va9a(0x84) = SUB va91, va97
    0xa9c: REVERT va97, va9a(0x84)

    Begin block 0xa9d
    prev=[0xa2d], succ=[0xaa8, 0xb0e]
    =================================
    0xa9e: va9e(0x4e20) = CONST 
    0xaa2: vaa2 = GT v397, va9e(0x4e20)
    0xaa3: vaa3 = ISZERO vaa2
    0xaa4: vaa4(0xb0e) = CONST 
    0xaa7: JUMPI vaa4(0xb0e), vaa3

    Begin block 0xaa8
    prev=[0xa9d], succ=[]
    =================================
    0xaa8: vaa8(0x40) = CONST 
    0xaab: vaab = MLOAD vaa8(0x40)
    0xaac: vaac(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xace: MSTORE vaab, vaac(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xacf: vacf(0x20) = CONST 
    0xad1: vad1(0x4) = CONST 
    0xad4: vad4 = ADD vaab, vad1(0x4)
    0xad5: MSTORE vad4, vacf(0x20)
    0xad6: vad6(0x9) = CONST 
    0xad8: vad8(0x24) = CONST 
    0xadb: vadb = ADD vaab, vad8(0x24)
    0xadc: MSTORE vadb, vad6(0x9)
    0xadd: vadd(0x6f76657220323030250000000000000000000000000000000000000000000000) = CONST 
    0xafe: vafe(0x44) = CONST 
    0xb01: vb01 = ADD vaab, vafe(0x44)
    0xb02: MSTORE vb01, vadd(0x6f76657220323030250000000000000000000000000000000000000000000000)
    0xb04: vb04 = MLOAD vaa8(0x40)
    0xb08: vb08(0x0) = SUB vaab, vb04
    0xb09: vb09(0x64) = CONST 
    0xb0b: vb0b(0x64) = ADD vb09(0x64), vb08(0x0)
    0xb0d: REVERT vb04, vb0b(0x64)

    Begin block 0xb0e
    prev=[0xa9d], succ=[0x35b4]
    =================================
    0xb0f: vb0f(0x9) = CONST 
    0xb11: SSTORE vb0f(0x9), v397
    0xb12: JUMP v380(0x35b4)

    Begin block 0x35b4
    prev=[0xb0e], succ=[]
    =================================
    0x35b5: STOP 

}

function initialized()() public {
    Begin block 0x39c
    prev=[], succ=[0xb13]
    =================================
    0x39d: v39d(0x35d5) = CONST 
    0x3a0: v3a0(0xb13) = CONST 
    0x3a3: JUMP v3a0(0xb13)

    Begin block 0xb13
    prev=[0x39c], succ=[0x35d5]
    =================================
    0xb14: vb14(0x1) = CONST 
    0xb16: vb16 = SLOAD vb14(0x1)
    0xb17: vb17(0x10000000000000000000000000000000000000000) = CONST 
    0xb2e: vb2e = DIV vb16, vb17(0x10000000000000000000000000000000000000000)
    0xb2f: vb2f(0xff) = CONST 
    0xb31: vb31 = AND vb2f(0xff), vb2e
    0xb33: JUMP v39d(0x35d5)

    Begin block 0x35d5
    prev=[0xb13], succ=[]
    =================================
    0x35d6: v35d6(0x40) = CONST 
    0x35d9: v35d9 = MLOAD v35d6(0x40)
    0x35db: v35db = ISZERO vb31
    0x35dc: v35dc = ISZERO v35db
    0x35de: MSTORE v35d9, v35dc
    0x35df: v35df = MLOAD v35d6(0x40)
    0x35e3: v35e3(0x0) = SUB v35d9, v35df
    0x35e4: v35e4(0x20) = CONST 
    0x35e6: v35e6(0x20) = ADD v35e4(0x20), v35e3(0x0)
    0x35e8: RETURN v35df, v35e6(0x20)

}

function totalSupply()() public {
    Begin block 0x3b8
    prev=[], succ=[0xb34]
    =================================
    0x3b9: v3b9(0x3608) = CONST 
    0x3bc: v3bc(0xb34) = CONST 
    0x3bf: JUMP v3bc(0xb34)

    Begin block 0xb34
    prev=[0x3b8], succ=[0x3608]
    =================================
    0xb35: vb35(0x11) = CONST 
    0xb37: vb37 = SLOAD vb35(0x11)
    0xb39: JUMP v3b9(0x3608)

    Begin block 0x3608
    prev=[0xb34], succ=[]
    =================================
    0x3609: v3609(0x40) = CONST 
    0x360c: v360c = MLOAD v3609(0x40)
    0x360f: MSTORE v360c, vb37
    0x3610: v3610 = MLOAD v3609(0x40)
    0x3614: v3614(0x0) = SUB v360c, v3610
    0x3615: v3615(0x20) = CONST 
    0x3617: v3617(0x20) = ADD v3615(0x20), v3614(0x0)
    0x3619: RETURN v3610, v3617(0x20)

}

function setLpPoolIncentiveRate(uint256)() public {
    Begin block 0x3c0
    prev=[], succ=[0x3d2, 0x3d6]
    =================================
    0x3c1: v3c1(0x3639) = CONST 
    0x3c4: v3c4(0x4) = CONST 
    0x3c7: v3c7 = CALLDATASIZE 
    0x3c8: v3c8 = SUB v3c7, v3c4(0x4)
    0x3c9: v3c9(0x20) = CONST 
    0x3cc: v3cc = LT v3c8, v3c9(0x20)
    0x3cd: v3cd = ISZERO v3cc
    0x3ce: v3ce(0x3d6) = CONST 
    0x3d1: JUMPI v3ce(0x3d6), v3cd

    Begin block 0x3d2
    prev=[0x3c0], succ=[]
    =================================
    0x3d2: v3d2(0x0) = CONST 
    0x3d5: REVERT v3d2(0x0), v3d2(0x0)

    Begin block 0x3d6
    prev=[0x3c0], succ=[0xb3a]
    =================================
    0x3d8: v3d8 = CALLDATALOAD v3c4(0x4)
    0x3d9: v3d9(0xb3a) = CONST 
    0x3dc: JUMP v3d9(0xb3a)

    Begin block 0xb3a
    prev=[0x3d6], succ=[0xb5a, 0xbaa]
    =================================
    0xb3b: vb3b(0x1) = CONST 
    0xb3d: vb3d = SLOAD vb3b(0x1)
    0xb3e: vb3e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xb53: vb53 = AND vb3e(0xffffffffffffffffffffffffffffffffffffffff), vb3d
    0xb54: vb54 = CALLER 
    0xb55: vb55 = EQ vb54, vb53
    0xb56: vb56(0xbaa) = CONST 
    0xb59: JUMPI vb56(0xbaa), vb55

    Begin block 0xb5a
    prev=[0xb3a], succ=[]
    =================================
    0xb5a: vb5a(0x40) = CONST 
    0xb5c: vb5c = MLOAD vb5a(0x40)
    0xb5d: vb5d(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xb7f: MSTORE vb5c, vb5d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xb80: vb80(0x4) = CONST 
    0xb82: vb82 = ADD vb80(0x4), vb5c
    0xb85: vb85(0x20) = CONST 
    0xb87: vb87 = ADD vb85(0x20), vb82
    0xb8a: vb8a(0x20) = SUB vb87, vb82
    0xb8c: MSTORE vb82, vb8a(0x20)
    0xb8d: vb8d(0x28) = CONST 
    0xb90: MSTORE vb87, vb8d(0x28)
    0xb91: vb91(0x20) = CONST 
    0xb93: vb93 = ADD vb91(0x20), vb87
    0xb95: vb95(0x311d) = CONST 
    0xb98: vb98(0x28) = CONST 
    0xb9b: CODECOPY vb93, vb95(0x311d), vb98(0x28)
    0xb9c: vb9c(0x40) = CONST 
    0xb9e: vb9e = ADD vb9c(0x40), vb93
    0xba2: vba2(0x40) = CONST 
    0xba4: vba4 = MLOAD vba2(0x40)
    0xba7: vba7(0x84) = SUB vb9e, vba4
    0xba9: REVERT vba4, vba7(0x84)

    Begin block 0xbaa
    prev=[0xb3a], succ=[0xbb5, 0xc1b]
    =================================
    0xbab: vbab(0x7d0) = CONST 
    0xbaf: vbaf = GT v3d8, vbab(0x7d0)
    0xbb0: vbb0 = ISZERO vbaf
    0xbb1: vbb1(0xc1b) = CONST 
    0xbb4: JUMPI vbb1(0xc1b), vbb0

    Begin block 0xbb5
    prev=[0xbaa], succ=[]
    =================================
    0xbb5: vbb5(0x40) = CONST 
    0xbb8: vbb8 = MLOAD vbb5(0x40)
    0xbb9: vbb9(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xbdb: MSTORE vbb8, vbb9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xbdc: vbdc(0x20) = CONST 
    0xbde: vbde(0x4) = CONST 
    0xbe1: vbe1 = ADD vbb8, vbde(0x4)
    0xbe2: MSTORE vbe1, vbdc(0x20)
    0xbe3: vbe3(0x8) = CONST 
    0xbe5: vbe5(0x24) = CONST 
    0xbe8: vbe8 = ADD vbb8, vbe5(0x24)
    0xbe9: MSTORE vbe8, vbe3(0x8)
    0xbea: vbea(0x6f76657220323025000000000000000000000000000000000000000000000000) = CONST 
    0xc0b: vc0b(0x44) = CONST 
    0xc0e: vc0e = ADD vbb8, vc0b(0x44)
    0xc0f: MSTORE vc0e, vbea(0x6f76657220323025000000000000000000000000000000000000000000000000)
    0xc11: vc11 = MLOAD vbb5(0x40)
    0xc15: vc15(0x0) = SUB vbb8, vc11
    0xc16: vc16(0x64) = CONST 
    0xc18: vc18(0x64) = ADD vc16(0x64), vc15(0x0)
    0xc1a: REVERT vc11, vc18(0x64)

    Begin block 0xc1b
    prev=[0xbaa], succ=[0x3639]
    =================================
    0xc1c: vc1c(0x13) = CONST 
    0xc1e: SSTORE vc1c(0x13), v3d8
    0xc1f: JUMP v3c1(0x3639)

    Begin block 0x3639
    prev=[0xc1b], succ=[]
    =================================
    0x363a: STOP 

}

function redemptedCoupons(uint256)() public {
    Begin block 0x3dd
    prev=[], succ=[0x3ef, 0x3f3]
    =================================
    0x3de: v3de(0x365a) = CONST 
    0x3e1: v3e1(0x4) = CONST 
    0x3e4: v3e4 = CALLDATASIZE 
    0x3e5: v3e5 = SUB v3e4, v3e1(0x4)
    0x3e6: v3e6(0x20) = CONST 
    0x3e9: v3e9 = LT v3e5, v3e6(0x20)
    0x3ea: v3ea = ISZERO v3e9
    0x3eb: v3eb(0x3f3) = CONST 
    0x3ee: JUMPI v3eb(0x3f3), v3ea

    Begin block 0x3ef
    prev=[0x3dd], succ=[]
    =================================
    0x3ef: v3ef(0x0) = CONST 
    0x3f2: REVERT v3ef(0x0), v3ef(0x0)

    Begin block 0x3f3
    prev=[0x3dd], succ=[0xc20]
    =================================
    0x3f5: v3f5 = CALLDATALOAD v3e1(0x4)
    0x3f6: v3f6(0xc20) = CONST 
    0x3f9: JUMP v3f6(0xc20)

    Begin block 0xc20
    prev=[0x3f3], succ=[0x365a]
    =================================
    0xc21: vc21(0x10) = CONST 
    0xc23: vc23(0x20) = CONST 
    0xc25: MSTORE vc23(0x20), vc21(0x10)
    0xc26: vc26(0x0) = CONST 
    0xc2a: MSTORE vc26(0x0), v3f5
    0xc2b: vc2b(0x40) = CONST 
    0xc2e: vc2e = SHA3 vc26(0x0), vc2b(0x40)
    0xc2f: vc2f = SLOAD vc2e
    0xc31: JUMP v3de(0x365a)

    Begin block 0x365a
    prev=[0xc20], succ=[]
    =================================
    0x365b: v365b(0x40) = CONST 
    0x365e: v365e = MLOAD v365b(0x40)
    0x3661: MSTORE v365e, vc2f
    0x3662: v3662 = MLOAD v365b(0x40)
    0x3666: v3666(0x0) = SUB v365e, v3662
    0x3667: v3667(0x20) = CONST 
    0x3669: v3669(0x20) = ADD v3667(0x20), v3666(0x0)
    0x366b: RETURN v3662, v3669(0x20)

}

function setDollarOracle(address)() public {
    Begin block 0x3fa
    prev=[], succ=[0x40c, 0x410]
    =================================
    0x3fb: v3fb(0x368b) = CONST 
    0x3fe: v3fe(0x4) = CONST 
    0x401: v401 = CALLDATASIZE 
    0x402: v402 = SUB v401, v3fe(0x4)
    0x403: v403(0x20) = CONST 
    0x406: v406 = LT v402, v403(0x20)
    0x407: v407 = ISZERO v406
    0x408: v408(0x410) = CONST 
    0x40b: JUMPI v408(0x410), v407

    Begin block 0x40c
    prev=[0x3fa], succ=[]
    =================================
    0x40c: v40c(0x0) = CONST 
    0x40f: REVERT v40c(0x0), v40c(0x0)

    Begin block 0x410
    prev=[0x3fa], succ=[0xc32]
    =================================
    0x412: v412 = CALLDATALOAD v3fe(0x4)
    0x413: v413(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x428: v428 = AND v413(0xffffffffffffffffffffffffffffffffffffffff), v412
    0x429: v429(0xc32) = CONST 
    0x42c: JUMP v429(0xc32)

    Begin block 0xc32
    prev=[0x410], succ=[0xc52, 0xca2]
    =================================
    0xc33: vc33(0x1) = CONST 
    0xc35: vc35 = SLOAD vc33(0x1)
    0xc36: vc36(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xc4b: vc4b = AND vc36(0xffffffffffffffffffffffffffffffffffffffff), vc35
    0xc4c: vc4c = CALLER 
    0xc4d: vc4d = EQ vc4c, vc4b
    0xc4e: vc4e(0xca2) = CONST 
    0xc51: JUMPI vc4e(0xca2), vc4d

    Begin block 0xc52
    prev=[0xc32], succ=[]
    =================================
    0xc52: vc52(0x40) = CONST 
    0xc54: vc54 = MLOAD vc52(0x40)
    0xc55: vc55(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xc77: MSTORE vc54, vc55(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xc78: vc78(0x4) = CONST 
    0xc7a: vc7a = ADD vc78(0x4), vc54
    0xc7d: vc7d(0x20) = CONST 
    0xc7f: vc7f = ADD vc7d(0x20), vc7a
    0xc82: vc82(0x20) = SUB vc7f, vc7a
    0xc84: MSTORE vc7a, vc82(0x20)
    0xc85: vc85(0x28) = CONST 
    0xc88: MSTORE vc7f, vc85(0x28)
    0xc89: vc89(0x20) = CONST 
    0xc8b: vc8b = ADD vc89(0x20), vc7f
    0xc8d: vc8d(0x311d) = CONST 
    0xc90: vc90(0x28) = CONST 
    0xc93: CODECOPY vc8b, vc8d(0x311d), vc90(0x28)
    0xc94: vc94(0x40) = CONST 
    0xc96: vc96 = ADD vc94(0x40), vc8b
    0xc9a: vc9a(0x40) = CONST 
    0xc9c: vc9c = MLOAD vc9a(0x40)
    0xc9f: vc9f(0x84) = SUB vc96, vc9c
    0xca1: REVERT vc9c, vc9f(0x84)

    Begin block 0xca2
    prev=[0xc32], succ=[0x368b]
    =================================
    0xca3: vca3(0x4) = CONST 
    0xca6: vca6 = SLOAD vca3(0x4)
    0xca7: vca7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0xcc8: vcc8 = AND vca7(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), vca6
    0xcc9: vcc9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xce1: vce1 = AND vcc9(0xffffffffffffffffffffffffffffffffffffffff), v428
    0xce5: vce5 = OR vce1, vcc8
    0xce7: SSTORE vca3(0x4), vce5
    0xce8: JUMP v3fb(0x368b)

    Begin block 0x368b
    prev=[0xca2], succ=[]
    =================================
    0x368c: STOP 

}

function manuallyBalanceAdd(address,uint256)() public {
    Begin block 0x42d
    prev=[], succ=[0x43f, 0x443]
    =================================
    0x42e: v42e(0x36ac) = CONST 
    0x431: v431(0x4) = CONST 
    0x434: v434 = CALLDATASIZE 
    0x435: v435 = SUB v434, v431(0x4)
    0x436: v436(0x40) = CONST 
    0x439: v439 = LT v435, v436(0x40)
    0x43a: v43a = ISZERO v439
    0x43b: v43b(0x443) = CONST 
    0x43e: JUMPI v43b(0x443), v43a

    Begin block 0x43f
    prev=[0x42d], succ=[]
    =================================
    0x43f: v43f(0x0) = CONST 
    0x442: REVERT v43f(0x0), v43f(0x0)

    Begin block 0x443
    prev=[0x42d], succ=[0xce9]
    =================================
    0x445: v445(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x45b: v45b = CALLDATALOAD v431(0x4)
    0x45c: v45c = AND v45b, v445(0xffffffffffffffffffffffffffffffffffffffff)
    0x45e: v45e(0x20) = CONST 
    0x460: v460(0x24) = ADD v45e(0x20), v431(0x4)
    0x461: v461 = CALLDATALOAD v460(0x24)
    0x462: v462(0xce9) = CONST 
    0x465: JUMP v462(0xce9)

    Begin block 0xce9
    prev=[0x443], succ=[0xd09, 0xd59]
    =================================
    0xcea: vcea(0x1) = CONST 
    0xcec: vcec = SLOAD vcea(0x1)
    0xced: vced(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd02: vd02 = AND vced(0xffffffffffffffffffffffffffffffffffffffff), vcec
    0xd03: vd03 = CALLER 
    0xd04: vd04 = EQ vd03, vd02
    0xd05: vd05(0xd59) = CONST 
    0xd08: JUMPI vd05(0xd59), vd04

    Begin block 0xd09
    prev=[0xce9], succ=[]
    =================================
    0xd09: vd09(0x40) = CONST 
    0xd0b: vd0b = MLOAD vd09(0x40)
    0xd0c: vd0c(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xd2e: MSTORE vd0b, vd0c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xd2f: vd2f(0x4) = CONST 
    0xd31: vd31 = ADD vd2f(0x4), vd0b
    0xd34: vd34(0x20) = CONST 
    0xd36: vd36 = ADD vd34(0x20), vd31
    0xd39: vd39(0x20) = SUB vd36, vd31
    0xd3b: MSTORE vd31, vd39(0x20)
    0xd3c: vd3c(0x28) = CONST 
    0xd3f: MSTORE vd36, vd3c(0x28)
    0xd40: vd40(0x20) = CONST 
    0xd42: vd42 = ADD vd40(0x20), vd36
    0xd44: vd44(0x311d) = CONST 
    0xd47: vd47(0x28) = CONST 
    0xd4a: CODECOPY vd42, vd44(0x311d), vd47(0x28)
    0xd4b: vd4b(0x40) = CONST 
    0xd4d: vd4d = ADD vd4b(0x40), vd42
    0xd51: vd51(0x40) = CONST 
    0xd53: vd53 = MLOAD vd51(0x40)
    0xd56: vd56(0x84) = SUB vd4d, vd53
    0xd58: REVERT vd53, vd56(0x84)

    Begin block 0xd59
    prev=[0xce9], succ=[0xd89]
    =================================
    0xd5a: vd5a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xd70: vd70 = AND v45c, vd5a(0xffffffffffffffffffffffffffffffffffffffff)
    0xd71: vd71(0x0) = CONST 
    0xd75: MSTORE vd71(0x0), vd70
    0xd76: vd76(0x12) = CONST 
    0xd78: vd78(0x20) = CONST 
    0xd7a: MSTORE vd78(0x20), vd76(0x12)
    0xd7b: vd7b(0x40) = CONST 
    0xd7e: vd7e = SHA3 vd71(0x0), vd7b(0x40)
    0xd7f: vd7f = SLOAD vd7e
    0xd80: vd80(0xd89) = CONST 
    0xd85: vd85(0x2933) = CONST 
    0xd88: vd88_0 = CALLPRIVATE vd85(0x2933), v461, vd7f, vd80(0xd89)

    Begin block 0xd89
    prev=[0xd59], succ=[0xdbc]
    =================================
    0xd8a: vd8a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xda0: vda0 = AND v45c, vd8a(0xffffffffffffffffffffffffffffffffffffffff)
    0xda1: vda1(0x0) = CONST 
    0xda5: MSTORE vda1(0x0), vda0
    0xda6: vda6(0x12) = CONST 
    0xda8: vda8(0x20) = CONST 
    0xdaa: MSTORE vda8(0x20), vda6(0x12)
    0xdab: vdab(0x40) = CONST 
    0xdae: vdae = SHA3 vda1(0x0), vdab(0x40)
    0xdaf: SSTORE vdae, vd88_0
    0xdb0: vdb0(0x11) = CONST 
    0xdb2: vdb2 = SLOAD vdb0(0x11)
    0xdb3: vdb3(0xdbc) = CONST 
    0xdb8: vdb8(0x2933) = CONST 
    0xdbb: vdbb_0 = CALLPRIVATE vdb8(0x2933), v461, vdb2, vdb3(0xdbc)

    Begin block 0xdbc
    prev=[0xd89], succ=[0x36ac]
    =================================
    0xdbd: vdbd(0x11) = CONST 
    0xdbf: SSTORE vdbd(0x11), vdbb_0
    0xdc2: JUMP v42e(0x36ac)

    Begin block 0x36ac
    prev=[0xdbc], succ=[]
    =================================
    0x36ad: STOP 

}

function getPurchasedCouponHistory(address)() public {
    Begin block 0x466
    prev=[], succ=[0x478, 0x47c]
    =================================
    0x467: v467(0x499) = CONST 
    0x46a: v46a(0x4) = CONST 
    0x46d: v46d = CALLDATASIZE 
    0x46e: v46e = SUB v46d, v46a(0x4)
    0x46f: v46f(0x20) = CONST 
    0x472: v472 = LT v46e, v46f(0x20)
    0x473: v473 = ISZERO v472
    0x474: v474(0x47c) = CONST 
    0x477: JUMPI v474(0x47c), v473

    Begin block 0x478
    prev=[0x466], succ=[]
    =================================
    0x478: v478(0x0) = CONST 
    0x47b: REVERT v478(0x0), v478(0x0)

    Begin block 0x47c
    prev=[0x466], succ=[0xdc3]
    =================================
    0x47e: v47e = CALLDATALOAD v46a(0x4)
    0x47f: v47f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x494: v494 = AND v47f(0xffffffffffffffffffffffffffffffffffffffff), v47e
    0x495: v495(0xdc3) = CONST 
    0x498: JUMP v495(0xdc3)

    Begin block 0xdc3
    prev=[0x47c], succ=[0xe01, 0xe05]
    =================================
    0xdc4: vdc4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdda: vdda = AND v494, vdc4(0xffffffffffffffffffffffffffffffffffffffff)
    0xddb: vddb(0x0) = CONST 
    0xddf: MSTORE vddb(0x0), vdda
    0xde0: vde0(0xf) = CONST 
    0xde2: vde2(0x20) = CONST 
    0xde4: MSTORE vde2(0x20), vde0(0xf)
    0xde5: vde5(0x40) = CONST 
    0xde8: vde8 = SHA3 vddb(0x0), vde5(0x40)
    0xde9: vde9 = SLOAD vde8
    0xdea: vdea(0x60) = CONST 
    0xdf0: vdf0(0xffffffffffffffff) = CONST 
    0xdfa: vdfa = GT vde9, vdf0(0xffffffffffffffff)
    0xdfc: vdfc = ISZERO vdfa
    0xdfd: vdfd(0xe05) = CONST 
    0xe00: JUMPI vdfd(0xe05), vdfc

    Begin block 0xe01
    prev=[0xdc3], succ=[]
    =================================
    0xe01: ve01(0x0) = CONST 
    0xe04: REVERT ve01(0x0), ve01(0x0)

    Begin block 0xe05
    prev=[0xdc3], succ=[0xe2f, 0xe20]
    =================================
    0xe07: ve07(0x40) = CONST 
    0xe09: ve09 = MLOAD ve07(0x40)
    0xe0d: MSTORE ve09, vde9
    0xe0f: ve0f(0x20) = CONST 
    0xe11: ve11 = MUL ve0f(0x20), vde9
    0xe12: ve12(0x20) = CONST 
    0xe14: ve14 = ADD ve12(0x20), ve11
    0xe16: ve16 = ADD ve09, ve14
    0xe17: ve17(0x40) = CONST 
    0xe19: MSTORE ve17(0x40), ve16
    0xe1b: ve1b = ISZERO vde9
    0xe1c: ve1c(0xe2f) = CONST 
    0xe1f: JUMPI ve1c(0xe2f), ve1b

    Begin block 0xe2f
    prev=[0xe05, 0xe20], succ=[0xe45, 0xe49]
    =================================
    0xe34: ve34(0xffffffffffffffff) = CONST 
    0xe3e: ve3e = GT vde9, ve34(0xffffffffffffffff)
    0xe40: ve40 = ISZERO ve3e
    0xe41: ve41(0xe49) = CONST 
    0xe44: JUMPI ve41(0xe49), ve40

    Begin block 0xe45
    prev=[0xe2f], succ=[]
    =================================
    0xe45: ve45(0x0) = CONST 
    0xe48: REVERT ve45(0x0), ve45(0x0)

    Begin block 0xe49
    prev=[0xe2f], succ=[0xe73, 0xe64]
    =================================
    0xe4b: ve4b(0x40) = CONST 
    0xe4d: ve4d = MLOAD ve4b(0x40)
    0xe51: MSTORE ve4d, vde9
    0xe53: ve53(0x20) = CONST 
    0xe55: ve55 = MUL ve53(0x20), vde9
    0xe56: ve56(0x20) = CONST 
    0xe58: ve58 = ADD ve56(0x20), ve55
    0xe5a: ve5a = ADD ve4d, ve58
    0xe5b: ve5b(0x40) = CONST 
    0xe5d: MSTORE ve5b(0x40), ve5a
    0xe5f: ve5f = ISZERO vde9
    0xe60: ve60(0xe73) = CONST 
    0xe63: JUMPI ve60(0xe73), ve5f

    Begin block 0xe73
    prev=[0xe49, 0xe64], succ=[0xe79]
    =================================
    0xe77: ve77(0x0) = CONST 

    Begin block 0xe79
    prev=[0xe73, 0xf2d], succ=[0xe82, 0xf37]
    =================================
    0xe79_0x0: ve79_0 = PHI ve77(0x0), vf32
    0xe7c: ve7c = LT ve79_0, vde9
    0xe7d: ve7d = ISZERO ve7c
    0xe7e: ve7e(0xf37) = CONST 
    0xe81: JUMPI ve7e(0xf37), ve7d

    Begin block 0xe82
    prev=[0xe79], succ=[0xeb1, 0xeb2]
    =================================
    0xe82: ve82(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xe82_0x0: ve82_0 = PHI ve77(0x0), vf32
    0xe98: ve98 = AND v494, ve82(0xffffffffffffffffffffffffffffffffffffffff)
    0xe99: ve99(0x0) = CONST 
    0xe9d: MSTORE ve99(0x0), ve98
    0xe9e: ve9e(0xf) = CONST 
    0xea0: vea0(0x20) = CONST 
    0xea2: MSTORE vea0(0x20), ve9e(0xf)
    0xea3: vea3(0x40) = CONST 
    0xea6: vea6 = SHA3 ve99(0x0), vea3(0x40)
    0xea8: vea8 = SLOAD vea6
    0xeac: veac = LT ve82_0, vea8
    0xead: vead(0xeb2) = CONST 
    0xeb0: JUMPI vead(0xeb2), veac

    Begin block 0xeb1
    prev=[0xe82], succ=[]
    =================================
    0xeb1: THROW 

    Begin block 0xeb2
    prev=[0xe82], succ=[0xf2d, 0xef5]
    =================================
    0xeb2_0x0: veb2_0 = PHI ve77(0x0), vf32
    0xeb3: veb3(0x0) = CONST 
    0xeb7: MSTORE veb3(0x0), vea6
    0xeb8: veb8(0x20) = CONST 
    0xebc: vebc = SHA3 veb3(0x0), veb8(0x20)
    0xebf: vebf = ADD veb2_0, vebc
    0xec0: vec0 = SLOAD vebf
    0xec1: vec1(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xed7: ved7 = AND v494, vec1(0xffffffffffffffffffffffffffffffffffffffff)
    0xed9: MSTORE veb3(0x0), ved7
    0xeda: veda(0xe) = CONST 
    0xedd: MSTORE veb8(0x20), veda(0xe)
    0xede: vede(0x40) = CONST 
    0xee2: vee2 = SHA3 veb3(0x0), vede(0x40)
    0xee5: MSTORE veb3(0x0), vec0
    0xee8: MSTORE veb8(0x20), vee2
    0xeea: veea = SHA3 veb3(0x0), vede(0x40)
    0xeeb: veeb = SLOAD veea
    0xef0: vef0 = ISZERO veeb
    0xef1: vef1(0xf2d) = CONST 
    0xef4: JUMPI vef1(0xf2d), vef0

    Begin block 0xf2d
    prev=[0xeb2, 0xf1a], succ=[0xe79]
    =================================
    0xf2d_0x2: vf2d_2 = PHI ve77(0x0), vf32
    0xf30: vf30(0x1) = CONST 
    0xf32: vf32 = ADD vf30(0x1), vf2d_2
    0xf33: vf33(0xe79) = CONST 
    0xf36: JUMP vf33(0xe79)

    Begin block 0xef5
    prev=[0xeb2], succ=[0xf00, 0xf01]
    =================================
    0xef5_0x6: vef5_6 = PHI vddb(0x0), vf2a
    0xef9: vef9 = MLOAD ve09
    0xefb: vefb = LT vef5_6, vef9
    0xefc: vefc(0xf01) = CONST 
    0xeff: JUMPI vefc(0xf01), vefb

    Begin block 0xf00
    prev=[0xef5], succ=[]
    =================================
    0xf00: THROW 

    Begin block 0xf01
    prev=[0xef5], succ=[0xf19, 0xf1a]
    =================================
    0xf01_0x0: vf01_0 = PHI vddb(0x0), vf2a
    0xf01_0x9: vf01_9 = PHI vddb(0x0), vf2a
    0xf02: vf02(0x20) = CONST 
    0xf04: vf04 = MUL vf02(0x20), vf01_0
    0xf05: vf05(0x20) = CONST 
    0xf07: vf07 = ADD vf05(0x20), vf04
    0xf08: vf08 = ADD vf07, ve09
    0xf0b: MSTORE vf08, vec0
    0xf12: vf12 = MLOAD ve4d
    0xf14: vf14 = LT vf01_9, vf12
    0xf15: vf15(0xf1a) = CONST 
    0xf18: JUMPI vf15(0xf1a), vf14

    Begin block 0xf19
    prev=[0xf01], succ=[]
    =================================
    0xf19: THROW 

    Begin block 0xf1a
    prev=[0xf01], succ=[0xf2d]
    =================================
    0xf1a_0x0: vf1a_0 = PHI vddb(0x0), vf2a
    0xf1a_0x9: vf1a_9 = PHI vddb(0x0), vf2a
    0xf1b: vf1b(0x20) = CONST 
    0xf1d: vf1d = MUL vf1b(0x20), vf1a_0
    0xf1e: vf1e(0x20) = CONST 
    0xf20: vf20 = ADD vf1e(0x20), vf1d
    0xf21: vf21 = ADD vf20, ve4d
    0xf24: MSTORE vf21, veeb
    0xf28: vf28(0x1) = CONST 
    0xf2a: vf2a = ADD vf28(0x1), vf1a_9

    Begin block 0xf37
    prev=[0xe79], succ=[0x499]
    =================================
    0xf3f: JUMP v467(0x499)

    Begin block 0x499
    prev=[0xf37], succ=[0x4cb]
    =================================
    0x499_0x2: v499_2 = PHI vddb(0x0), vf2a
    0x49a: v49a(0x40) = CONST 
    0x49c: v49c = MLOAD v49a(0x40)
    0x4a0: MSTORE v49c, v499_2
    0x4a1: v4a1(0x20) = CONST 
    0x4a3: v4a3 = ADD v4a1(0x20), v49c
    0x4a5: v4a5(0x20) = CONST 
    0x4a7: v4a7 = ADD v4a5(0x20), v4a3
    0x4a9: v4a9(0x20) = CONST 
    0x4ab: v4ab = ADD v4a9(0x20), v4a7
    0x4ae: v4ae(0x60) = SUB v4ab, v49c
    0x4b0: MSTORE v4a3, v4ae(0x60)
    0x4b4: v4b4 = MLOAD ve09
    0x4b6: MSTORE v4ab, v4b4
    0x4b7: v4b7(0x20) = CONST 
    0x4b9: v4b9 = ADD v4b7(0x20), v4ab
    0x4bd: v4bd = MLOAD ve09
    0x4bf: v4bf(0x20) = CONST 
    0x4c1: v4c1 = ADD v4bf(0x20), ve09
    0x4c3: v4c3(0x20) = CONST 
    0x4c5: v4c5 = MUL v4c3(0x20), v4bd
    0x4c9: v4c9(0x0) = CONST 

    Begin block 0x4cb
    prev=[0x499, 0x4d4], succ=[0x4e3, 0x4d4]
    =================================
    0x4cb_0x0: v4cb_0 = PHI v4c9(0x0), v4de
    0x4ce: v4ce = LT v4cb_0, v4c5
    0x4cf: v4cf = ISZERO v4ce
    0x4d0: v4d0(0x4e3) = CONST 
    0x4d3: JUMPI v4d0(0x4e3), v4cf

    Begin block 0x4e3
    prev=[0x4cb], succ=[0x50a]
    =================================
    0x4ea: v4ea = ADD v4c5, v4b9
    0x4ed: v4ed = SUB v4ea, v49c
    0x4ef: MSTORE v4a7, v4ed
    0x4f3: v4f3 = MLOAD ve4d
    0x4f5: MSTORE v4ea, v4f3
    0x4f6: v4f6(0x20) = CONST 
    0x4f8: v4f8 = ADD v4f6(0x20), v4ea
    0x4fc: v4fc = MLOAD ve4d
    0x4fe: v4fe(0x20) = CONST 
    0x500: v500 = ADD v4fe(0x20), ve4d
    0x502: v502(0x20) = CONST 
    0x504: v504 = MUL v502(0x20), v4fc
    0x508: v508(0x0) = CONST 

    Begin block 0x50a
    prev=[0x4e3, 0x513], succ=[0x522, 0x513]
    =================================
    0x50a_0x0: v50a_0 = PHI v508(0x0), v51d
    0x50d: v50d = LT v50a_0, v504
    0x50e: v50e = ISZERO v50d
    0x50f: v50f(0x522) = CONST 
    0x512: JUMPI v50f(0x522), v50e

    Begin block 0x522
    prev=[0x50a], succ=[]
    =================================
    0x529: v529 = ADD v504, v4f8
    0x531: v531(0x40) = CONST 
    0x533: v533 = MLOAD v531(0x40)
    0x536: v536 = SUB v529, v533
    0x538: RETURN v533, v536

    Begin block 0x513
    prev=[0x50a], succ=[0x50a]
    =================================
    0x513_0x0: v513_0 = PHI v508(0x0), v51d
    0x515: v515 = ADD v513_0, v500
    0x516: v516 = MLOAD v515
    0x519: v519 = ADD v513_0, v4f8
    0x51a: MSTORE v519, v516
    0x51b: v51b(0x20) = CONST 
    0x51d: v51d = ADD v51b(0x20), v513_0
    0x51e: v51e(0x50a) = CONST 
    0x521: JUMP v51e(0x50a)

    Begin block 0x4d4
    prev=[0x4cb], succ=[0x4cb]
    =================================
    0x4d4_0x0: v4d4_0 = PHI v4c9(0x0), v4de
    0x4d6: v4d6 = ADD v4d4_0, v4c1
    0x4d7: v4d7 = MLOAD v4d6
    0x4da: v4da = ADD v4d4_0, v4b9
    0x4db: MSTORE v4da, v4d7
    0x4dc: v4dc(0x20) = CONST 
    0x4de: v4de = ADD v4dc(0x20), v4d4_0
    0x4df: v4df(0x4cb) = CONST 
    0x4e2: JUMP v4df(0x4cb)

    Begin block 0xe64
    prev=[0xe49], succ=[0xe73]
    =================================
    0xe65: ve65(0x20) = CONST 
    0xe67: ve67 = ADD ve65(0x20), ve4d
    0xe68: ve68(0x20) = CONST 
    0xe6b: ve6b = MUL vde9, ve68(0x20)
    0xe6d: ve6d = CALLDATASIZE 
    0xe6f: CALLDATACOPY ve67, ve6d, ve6b
    0xe70: ve70 = ADD ve6b, ve67

    Begin block 0xe20
    prev=[0xe05], succ=[0xe2f]
    =================================
    0xe21: ve21(0x20) = CONST 
    0xe23: ve23 = ADD ve21(0x20), ve09
    0xe24: ve24(0x20) = CONST 
    0xe27: ve27 = MUL vde9, ve24(0x20)
    0xe29: ve29 = CALLDATASIZE 
    0xe2b: CALLDATACOPY ve23, ve29, ve27
    0xe2c: ve2c = ADD ve27, ve23

}

function bondSupply()() public {
    Begin block 0x539
    prev=[], succ=[0xf40]
    =================================
    0x53a: v53a(0x36cd) = CONST 
    0x53d: v53d(0xf40) = CONST 
    0x540: JUMP v53d(0xf40)

    Begin block 0xf40
    prev=[0x539], succ=[0x36cd]
    =================================
    0xf41: vf41(0x6) = CONST 
    0xf43: vf43 = SLOAD vf41(0x6)
    0xf45: JUMP v53a(0x36cd)

    Begin block 0x36cd
    prev=[0xf40], succ=[]
    =================================
    0x36ce: v36ce(0x40) = CONST 
    0x36d1: v36d1 = MLOAD v36ce(0x40)
    0x36d4: MSTORE v36d1, vf43
    0x36d5: v36d5 = MLOAD v36ce(0x40)
    0x36d9: v36d9(0x0) = SUB v36d1, v36d5
    0x36da: v36da(0x20) = CONST 
    0x36dc: v36dc(0x20) = ADD v36da(0x20), v36d9(0x0)
    0x36de: RETURN v36d5, v36dc(0x20)

}

function discountPercent()() public {
    Begin block 0x541
    prev=[], succ=[0xf46]
    =================================
    0x542: v542(0x36fe) = CONST 
    0x545: v545(0xf46) = CONST 
    0x548: JUMP v545(0xf46)

    Begin block 0xf46
    prev=[0x541], succ=[0x36fe]
    =================================
    0xf47: vf47(0x9) = CONST 
    0xf49: vf49 = SLOAD vf47(0x9)
    0xf4b: JUMP v542(0x36fe)

    Begin block 0x36fe
    prev=[0xf46], succ=[]
    =================================
    0x36ff: v36ff(0x40) = CONST 
    0x3702: v3702 = MLOAD v36ff(0x40)
    0x3705: MSTORE v3702, vf49
    0x3706: v3706 = MLOAD v36ff(0x40)
    0x370a: v370a(0x0) = SUB v3702, v3706
    0x370b: v370b(0x20) = CONST 
    0x370d: v370d(0x20) = ADD v370b(0x20), v370a(0x0)
    0x370f: RETURN v3706, v370d(0x20)

}

function couponSupply()() public {
    Begin block 0x549
    prev=[], succ=[0xf4c]
    =================================
    0x54a: v54a(0x372f) = CONST 
    0x54d: v54d(0xf4c) = CONST 
    0x550: JUMP v54d(0xf4c)

    Begin block 0xf4c
    prev=[0x549], succ=[0x372f]
    =================================
    0xf4d: vf4d(0x6) = CONST 
    0xf4f: vf4f = SLOAD vf4d(0x6)
    0xf51: JUMP v54a(0x372f)

    Begin block 0x372f
    prev=[0xf4c], succ=[]
    =================================
    0x3730: v3730(0x40) = CONST 
    0x3733: v3733 = MLOAD v3730(0x40)
    0x3736: MSTORE v3733, vf4f
    0x3737: v3737 = MLOAD v3730(0x40)
    0x373b: v373b(0x0) = SUB v3733, v3737
    0x373c: v373c(0x20) = CONST 
    0x373e: v373e(0x20) = ADD v373c(0x20), v373b(0x0)
    0x3740: RETURN v3737, v373e(0x20)

}

function setExpiredCouponEpochs(uint256)() public {
    Begin block 0x551
    prev=[], succ=[0x563, 0x567]
    =================================
    0x552: v552(0x3760) = CONST 
    0x555: v555(0x4) = CONST 
    0x558: v558 = CALLDATASIZE 
    0x559: v559 = SUB v558, v555(0x4)
    0x55a: v55a(0x20) = CONST 
    0x55d: v55d = LT v559, v55a(0x20)
    0x55e: v55e = ISZERO v55d
    0x55f: v55f(0x567) = CONST 
    0x562: JUMPI v55f(0x567), v55e

    Begin block 0x563
    prev=[0x551], succ=[]
    =================================
    0x563: v563(0x0) = CONST 
    0x566: REVERT v563(0x0), v563(0x0)

    Begin block 0x567
    prev=[0x551], succ=[0xf52]
    =================================
    0x569: v569 = CALLDATALOAD v555(0x4)
    0x56a: v56a(0xf52) = CONST 
    0x56d: JUMP v56a(0xf52)

    Begin block 0xf52
    prev=[0x567], succ=[0xf72, 0xfc2]
    =================================
    0xf53: vf53(0x1) = CONST 
    0xf55: vf55 = SLOAD vf53(0x1)
    0xf56: vf56(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xf6b: vf6b = AND vf56(0xffffffffffffffffffffffffffffffffffffffff), vf55
    0xf6c: vf6c = CALLER 
    0xf6d: vf6d = EQ vf6c, vf6b
    0xf6e: vf6e(0xfc2) = CONST 
    0xf71: JUMPI vf6e(0xfc2), vf6d

    Begin block 0xf72
    prev=[0xf52], succ=[]
    =================================
    0xf72: vf72(0x40) = CONST 
    0xf74: vf74 = MLOAD vf72(0x40)
    0xf75: vf75(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xf97: MSTORE vf74, vf75(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xf98: vf98(0x4) = CONST 
    0xf9a: vf9a = ADD vf98(0x4), vf74
    0xf9d: vf9d(0x20) = CONST 
    0xf9f: vf9f = ADD vf9d(0x20), vf9a
    0xfa2: vfa2(0x20) = SUB vf9f, vf9a
    0xfa4: MSTORE vf9a, vfa2(0x20)
    0xfa5: vfa5(0x28) = CONST 
    0xfa8: MSTORE vf9f, vfa5(0x28)
    0xfa9: vfa9(0x20) = CONST 
    0xfab: vfab = ADD vfa9(0x20), vf9f
    0xfad: vfad(0x311d) = CONST 
    0xfb0: vfb0(0x28) = CONST 
    0xfb3: CODECOPY vfab, vfad(0x311d), vfb0(0x28)
    0xfb4: vfb4(0x40) = CONST 
    0xfb6: vfb6 = ADD vfb4(0x40), vfab
    0xfba: vfba(0x40) = CONST 
    0xfbc: vfbc = MLOAD vfba(0x40)
    0xfbf: vfbf(0x84) = SUB vfb6, vfbc
    0xfc1: REVERT vfbc, vfbf(0x84)

    Begin block 0xfc2
    prev=[0xf52], succ=[0xfcc, 0x1032]
    =================================
    0xfc3: vfc3(0xb4) = CONST 
    0xfc6: vfc6 = LT v569, vfc3(0xb4)
    0xfc7: vfc7 = ISZERO vfc6
    0xfc8: vfc8(0x1032) = CONST 
    0xfcb: JUMPI vfc8(0x1032), vfc7

    Begin block 0xfcc
    prev=[0xfc2], succ=[]
    =================================
    0xfcc: vfcc(0x40) = CONST 
    0xfcf: vfcf = MLOAD vfcc(0x40)
    0xfd0: vfd0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0xff2: MSTORE vfcf, vfd0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xff3: vff3(0x20) = CONST 
    0xff5: vff5(0x4) = CONST 
    0xff8: vff8 = ADD vfcf, vff5(0x4)
    0xff9: MSTORE vff8, vff3(0x20)
    0xffa: vffa(0x9) = CONST 
    0xffc: vffc(0x24) = CONST 
    0xfff: vfff = ADD vfcf, vffc(0x24)
    0x1000: MSTORE vfff, vffa(0x9)
    0x1001: v1001(0x746f6f2073686f72740000000000000000000000000000000000000000000000) = CONST 
    0x1022: v1022(0x44) = CONST 
    0x1025: v1025 = ADD vfcf, v1022(0x44)
    0x1026: MSTORE v1025, v1001(0x746f6f2073686f72740000000000000000000000000000000000000000000000)
    0x1028: v1028 = MLOAD vfcc(0x40)
    0x102c: v102c(0x0) = SUB vfcf, v1028
    0x102d: v102d(0x64) = CONST 
    0x102f: v102f(0x64) = ADD v102d(0x64), v102c(0x0)
    0x1031: REVERT v1028, v102f(0x64)

    Begin block 0x1032
    prev=[0xfc2], succ=[0x3760]
    =================================
    0x1033: v1033(0x14) = CONST 
    0x1035: SSTORE v1033(0x14), v569
    0x1036: JUMP v552(0x3760)

    Begin block 0x3760
    prev=[0x1032], succ=[]
    =================================
    0x3761: STOP 

}

function maxPremiumRate()() public {
    Begin block 0x56e
    prev=[], succ=[0x1037]
    =================================
    0x56f: v56f(0x3781) = CONST 
    0x572: v572(0x1037) = CONST 
    0x575: JUMP v572(0x1037)

    Begin block 0x1037
    prev=[0x56e], succ=[0x3781]
    =================================
    0x1038: v1038(0xc) = CONST 
    0x103a: v103a = SLOAD v1038(0xc)
    0x103c: JUMP v56f(0x3781)

    Begin block 0x3781
    prev=[0x1037], succ=[]
    =================================
    0x3782: v3782(0x40) = CONST 
    0x3785: v3785 = MLOAD v3782(0x40)
    0x3788: MSTORE v3785, v103a
    0x3789: v3789 = MLOAD v3782(0x40)
    0x378d: v378d(0x0) = SUB v3785, v3789
    0x378e: v378e(0x20) = CONST 
    0x3790: v3790(0x20) = ADD v378e(0x20), v378d(0x0)
    0x3792: RETURN v3789, v3790(0x20)

}

function isInitialized()() public {
    Begin block 0x576
    prev=[], succ=[0x103d]
    =================================
    0x577: v577(0x37b2) = CONST 
    0x57a: v57a(0x103d) = CONST 
    0x57d: JUMP v57a(0x103d)

    Begin block 0x103d
    prev=[0x576], succ=[0x37b2]
    =================================
    0x103e: v103e(0x1) = CONST 
    0x1040: v1040 = SLOAD v103e(0x1)
    0x1041: v1041(0x10000000000000000000000000000000000000000) = CONST 
    0x1058: v1058 = DIV v1040, v1041(0x10000000000000000000000000000000000000000)
    0x1059: v1059(0xff) = CONST 
    0x105b: v105b = AND v1059(0xff), v1058
    0x105d: JUMP v577(0x37b2)

    Begin block 0x37b2
    prev=[0x103d], succ=[]
    =================================
    0x37b3: v37b3(0x40) = CONST 
    0x37b6: v37b6 = MLOAD v37b3(0x40)
    0x37b8: v37b8 = ISZERO v105b
    0x37b9: v37b9 = ISZERO v37b8
    0x37bb: MSTORE v37b6, v37b9
    0x37bc: v37bc = MLOAD v37b3(0x40)
    0x37c0: v37c0(0x0) = SUB v37b6, v37bc
    0x37c1: v37c1(0x20) = CONST 
    0x37c3: v37c3(0x20) = ADD v37c1(0x20), v37c0(0x0)
    0x37c5: RETURN v37bc, v37c3(0x20)

}

function getCouponPremiumRate()() public {
    Begin block 0x57e
    prev=[], succ=[0x34e0x57e]
    =================================
    0x57f: v57f(0x34e) = CONST 
    0x582: v582(0x105e) = CONST 
    0x585: v585_0 = CALLPRIVATE v582(0x105e), v57f(0x34e)

    Begin block 0x34e0x57e
    prev=[0x57e], succ=[]
    =================================
    0x34f0x57e: v57e34f(0x40) = CONST 
    0x3520x57e: v57e352 = MLOAD v57e34f(0x40)
    0x3550x57e: MSTORE v57e352, v585_0
    0x3560x57e: v57e356 = MLOAD v57e34f(0x40)
    0x35a0x57e: v57e35a(0x0) = SUB v57e352, v57e356
    0x35b0x57e: v57e35b(0x20) = CONST 
    0x35d0x57e: v57e35d(0x20) = ADD v57e35b(0x20), v57e35a(0x0)
    0x35f0x57e: RETURN v57e356, v57e35d(0x20)

}

function purchasedCoupons(address,uint256)() public {
    Begin block 0x586
    prev=[], succ=[0x598, 0x59c]
    =================================
    0x587: v587(0x37e5) = CONST 
    0x58a: v58a(0x4) = CONST 
    0x58d: v58d = CALLDATASIZE 
    0x58e: v58e = SUB v58d, v58a(0x4)
    0x58f: v58f(0x40) = CONST 
    0x592: v592 = LT v58e, v58f(0x40)
    0x593: v593 = ISZERO v592
    0x594: v594(0x59c) = CONST 
    0x597: JUMPI v594(0x59c), v593

    Begin block 0x598
    prev=[0x586], succ=[]
    =================================
    0x598: v598(0x0) = CONST 
    0x59b: REVERT v598(0x0), v598(0x0)

    Begin block 0x59c
    prev=[0x586], succ=[0x10fe]
    =================================
    0x59e: v59e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5b4: v5b4 = CALLDATALOAD v58a(0x4)
    0x5b5: v5b5 = AND v5b4, v59e(0xffffffffffffffffffffffffffffffffffffffff)
    0x5b7: v5b7(0x20) = CONST 
    0x5b9: v5b9(0x24) = ADD v5b7(0x20), v58a(0x4)
    0x5ba: v5ba = CALLDATALOAD v5b9(0x24)
    0x5bb: v5bb(0x10fe) = CONST 
    0x5be: JUMP v5bb(0x10fe)

    Begin block 0x10fe
    prev=[0x59c], succ=[0x37e5]
    =================================
    0x10ff: v10ff(0xe) = CONST 
    0x1101: v1101(0x20) = CONST 
    0x1105: MSTORE v1101(0x20), v10ff(0xe)
    0x1106: v1106(0x0) = CONST 
    0x110a: MSTORE v1106(0x0), v5b5
    0x110b: v110b(0x40) = CONST 
    0x110f: v110f = SHA3 v1106(0x0), v110b(0x40)
    0x1112: MSTORE v1101(0x20), v110f
    0x1115: MSTORE v1106(0x0), v5ba
    0x1117: v1117 = SHA3 v1106(0x0), v110b(0x40)
    0x1118: v1118 = SLOAD v1117
    0x111a: JUMP v587(0x37e5)

    Begin block 0x37e5
    prev=[0x10fe], succ=[]
    =================================
    0x37e6: v37e6(0x40) = CONST 
    0x37e9: v37e9 = MLOAD v37e6(0x40)
    0x37ec: MSTORE v37e9, v1118
    0x37ed: v37ed = MLOAD v37e6(0x40)
    0x37f1: v37f1(0x0) = SUB v37e9, v37ed
    0x37f2: v37f2(0x20) = CONST 
    0x37f4: v37f4(0x20) = ADD v37f2(0x20), v37f1(0x0)
    0x37f6: RETURN v37ed, v37f4(0x20)

}

function setSideToken(address)() public {
    Begin block 0x5bf
    prev=[], succ=[0x5d1, 0x5d5]
    =================================
    0x5c0: v5c0(0x3816) = CONST 
    0x5c3: v5c3(0x4) = CONST 
    0x5c6: v5c6 = CALLDATASIZE 
    0x5c7: v5c7 = SUB v5c6, v5c3(0x4)
    0x5c8: v5c8(0x20) = CONST 
    0x5cb: v5cb = LT v5c7, v5c8(0x20)
    0x5cc: v5cc = ISZERO v5cb
    0x5cd: v5cd(0x5d5) = CONST 
    0x5d0: JUMPI v5cd(0x5d5), v5cc

    Begin block 0x5d1
    prev=[0x5bf], succ=[]
    =================================
    0x5d1: v5d1(0x0) = CONST 
    0x5d4: REVERT v5d1(0x0), v5d1(0x0)

    Begin block 0x5d5
    prev=[0x5bf], succ=[0x111b]
    =================================
    0x5d7: v5d7 = CALLDATALOAD v5c3(0x4)
    0x5d8: v5d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5ed: v5ed = AND v5d8(0xffffffffffffffffffffffffffffffffffffffff), v5d7
    0x5ee: v5ee(0x111b) = CONST 
    0x5f1: JUMP v5ee(0x111b)

    Begin block 0x111b
    prev=[0x5d5], succ=[0x113b, 0x118b]
    =================================
    0x111c: v111c(0x1) = CONST 
    0x111e: v111e = SLOAD v111c(0x1)
    0x111f: v111f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1134: v1134 = AND v111f(0xffffffffffffffffffffffffffffffffffffffff), v111e
    0x1135: v1135 = CALLER 
    0x1136: v1136 = EQ v1135, v1134
    0x1137: v1137(0x118b) = CONST 
    0x113a: JUMPI v1137(0x118b), v1136

    Begin block 0x113b
    prev=[0x111b], succ=[]
    =================================
    0x113b: v113b(0x40) = CONST 
    0x113d: v113d = MLOAD v113b(0x40)
    0x113e: v113e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1160: MSTORE v113d, v113e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1161: v1161(0x4) = CONST 
    0x1163: v1163 = ADD v1161(0x4), v113d
    0x1166: v1166(0x20) = CONST 
    0x1168: v1168 = ADD v1166(0x20), v1163
    0x116b: v116b(0x20) = SUB v1168, v1163
    0x116d: MSTORE v1163, v116b(0x20)
    0x116e: v116e(0x28) = CONST 
    0x1171: MSTORE v1168, v116e(0x28)
    0x1172: v1172(0x20) = CONST 
    0x1174: v1174 = ADD v1172(0x20), v1168
    0x1176: v1176(0x311d) = CONST 
    0x1179: v1179(0x28) = CONST 
    0x117c: CODECOPY v1174, v1176(0x311d), v1179(0x28)
    0x117d: v117d(0x40) = CONST 
    0x117f: v117f = ADD v117d(0x40), v1174
    0x1183: v1183(0x40) = CONST 
    0x1185: v1185 = MLOAD v1183(0x40)
    0x1188: v1188(0x84) = SUB v117f, v1185
    0x118a: REVERT v1185, v1188(0x84)

    Begin block 0x118b
    prev=[0x111b], succ=[0x3816]
    =================================
    0x118c: v118c(0x5) = CONST 
    0x118f: v118f = SLOAD v118c(0x5)
    0x1190: v1190(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x11b1: v11b1 = AND v1190(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v118f
    0x11b2: v11b2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11ca: v11ca = AND v11b2(0xffffffffffffffffffffffffffffffffffffffff), v5ed
    0x11ce: v11ce = OR v11ca, v11b1
    0x11d0: SSTORE v118c(0x5), v11ce
    0x11d1: JUMP v5c0(0x3816)

    Begin block 0x3816
    prev=[0x118b], succ=[]
    =================================
    0x3817: STOP 

}

function setPremiumPercent(uint256)() public {
    Begin block 0x5f2
    prev=[], succ=[0x604, 0x608]
    =================================
    0x5f3: v5f3(0x3837) = CONST 
    0x5f6: v5f6(0x4) = CONST 
    0x5f9: v5f9 = CALLDATASIZE 
    0x5fa: v5fa = SUB v5f9, v5f6(0x4)
    0x5fb: v5fb(0x20) = CONST 
    0x5fe: v5fe = LT v5fa, v5fb(0x20)
    0x5ff: v5ff = ISZERO v5fe
    0x600: v600(0x608) = CONST 
    0x603: JUMPI v600(0x608), v5ff

    Begin block 0x604
    prev=[0x5f2], succ=[]
    =================================
    0x604: v604(0x0) = CONST 
    0x607: REVERT v604(0x0), v604(0x0)

    Begin block 0x608
    prev=[0x5f2], succ=[0x11d2]
    =================================
    0x60a: v60a = CALLDATALOAD v5f6(0x4)
    0x60b: v60b(0x11d2) = CONST 
    0x60e: JUMP v60b(0x11d2)

    Begin block 0x11d2
    prev=[0x608], succ=[0x11f2, 0x1242]
    =================================
    0x11d3: v11d3(0x1) = CONST 
    0x11d5: v11d5 = SLOAD v11d3(0x1)
    0x11d6: v11d6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x11eb: v11eb = AND v11d6(0xffffffffffffffffffffffffffffffffffffffff), v11d5
    0x11ec: v11ec = CALLER 
    0x11ed: v11ed = EQ v11ec, v11eb
    0x11ee: v11ee(0x1242) = CONST 
    0x11f1: JUMPI v11ee(0x1242), v11ed

    Begin block 0x11f2
    prev=[0x11d2], succ=[]
    =================================
    0x11f2: v11f2(0x40) = CONST 
    0x11f4: v11f4 = MLOAD v11f2(0x40)
    0x11f5: v11f5(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1217: MSTORE v11f4, v11f5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1218: v1218(0x4) = CONST 
    0x121a: v121a = ADD v1218(0x4), v11f4
    0x121d: v121d(0x20) = CONST 
    0x121f: v121f = ADD v121d(0x20), v121a
    0x1222: v1222(0x20) = SUB v121f, v121a
    0x1224: MSTORE v121a, v1222(0x20)
    0x1225: v1225(0x28) = CONST 
    0x1228: MSTORE v121f, v1225(0x28)
    0x1229: v1229(0x20) = CONST 
    0x122b: v122b = ADD v1229(0x20), v121f
    0x122d: v122d(0x311d) = CONST 
    0x1230: v1230(0x28) = CONST 
    0x1233: CODECOPY v122b, v122d(0x311d), v1230(0x28)
    0x1234: v1234(0x40) = CONST 
    0x1236: v1236 = ADD v1234(0x40), v122b
    0x123a: v123a(0x40) = CONST 
    0x123c: v123c = MLOAD v123a(0x40)
    0x123f: v123f(0x84) = SUB v1236, v123c
    0x1241: REVERT v123c, v123f(0x84)

    Begin block 0x1242
    prev=[0x11d2], succ=[0x124d, 0x12b3]
    =================================
    0x1243: v1243(0x4e20) = CONST 
    0x1247: v1247 = GT v60a, v1243(0x4e20)
    0x1248: v1248 = ISZERO v1247
    0x1249: v1249(0x12b3) = CONST 
    0x124c: JUMPI v1249(0x12b3), v1248

    Begin block 0x124d
    prev=[0x1242], succ=[]
    =================================
    0x124d: v124d(0x40) = CONST 
    0x1250: v1250 = MLOAD v124d(0x40)
    0x1251: v1251(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1273: MSTORE v1250, v1251(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1274: v1274(0x20) = CONST 
    0x1276: v1276(0x4) = CONST 
    0x1279: v1279 = ADD v1250, v1276(0x4)
    0x127a: MSTORE v1279, v1274(0x20)
    0x127b: v127b(0x9) = CONST 
    0x127d: v127d(0x24) = CONST 
    0x1280: v1280 = ADD v1250, v127d(0x24)
    0x1281: MSTORE v1280, v127b(0x9)
    0x1282: v1282(0x6f76657220323030250000000000000000000000000000000000000000000000) = CONST 
    0x12a3: v12a3(0x44) = CONST 
    0x12a6: v12a6 = ADD v1250, v12a3(0x44)
    0x12a7: MSTORE v12a6, v1282(0x6f76657220323030250000000000000000000000000000000000000000000000)
    0x12a9: v12a9 = MLOAD v124d(0x40)
    0x12ad: v12ad(0x0) = SUB v1250, v12a9
    0x12ae: v12ae(0x64) = CONST 
    0x12b0: v12b0(0x64) = ADD v12ae(0x64), v12ad(0x0)
    0x12b2: REVERT v12a9, v12b0(0x64)

    Begin block 0x12b3
    prev=[0x1242], succ=[0x3837]
    =================================
    0x12b4: v12b4(0xb) = CONST 
    0x12b6: SSTORE v12b4(0xb), v60a
    0x12b7: JUMP v5f3(0x3837)

    Begin block 0x3837
    prev=[0x12b3], succ=[]
    =================================
    0x3838: STOP 

}

function dollarOracle()() public {
    Begin block 0x60f
    prev=[], succ=[0x12b8]
    =================================
    0x610: v610(0x3858) = CONST 
    0x613: v613(0x12b8) = CONST 
    0x616: JUMP v613(0x12b8)

    Begin block 0x12b8
    prev=[0x60f], succ=[0x3858]
    =================================
    0x12b9: v12b9(0x4) = CONST 
    0x12bb: v12bb = SLOAD v12b9(0x4)
    0x12bc: v12bc(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12d1: v12d1 = AND v12bc(0xffffffffffffffffffffffffffffffffffffffff), v12bb
    0x12d3: JUMP v610(0x3858)

    Begin block 0x3858
    prev=[0x12b8], succ=[]
    =================================
    0x3859: v3859(0x40) = CONST 
    0x385c: v385c = MLOAD v3859(0x40)
    0x385d: v385d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3874: v3874 = AND v12d1, v385d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3876: MSTORE v385c, v3874
    0x3877: v3877 = MLOAD v3859(0x40)
    0x387b: v387b(0x0) = SUB v385c, v3877
    0x387c: v387c(0x20) = CONST 
    0x387e: v387e(0x20) = ADD v387c(0x20), v387b(0x0)
    0x3880: RETURN v3877, v387e(0x20)

}

function dollar()() public {
    Begin block 0x640
    prev=[], succ=[0x12d4]
    =================================
    0x641: v641(0x38a0) = CONST 
    0x644: v644(0x12d4) = CONST 
    0x647: JUMP v644(0x12d4)

    Begin block 0x12d4
    prev=[0x640], succ=[0x38a0]
    =================================
    0x12d5: v12d5(0x2) = CONST 
    0x12d7: v12d7 = SLOAD v12d5(0x2)
    0x12d8: v12d8(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x12ed: v12ed = AND v12d8(0xffffffffffffffffffffffffffffffffffffffff), v12d7
    0x12ef: JUMP v641(0x38a0)

    Begin block 0x38a0
    prev=[0x12d4], succ=[]
    =================================
    0x38a1: v38a1(0x40) = CONST 
    0x38a4: v38a4 = MLOAD v38a1(0x40)
    0x38a5: v38a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x38bc: v38bc = AND v12ed, v38a5(0xffffffffffffffffffffffffffffffffffffffff)
    0x38be: MSTORE v38a4, v38bc
    0x38bf: v38bf = MLOAD v38a1(0x40)
    0x38c3: v38c3(0x0) = SUB v38a4, v38bf
    0x38c4: v38c4(0x20) = CONST 
    0x38c6: v38c6(0x20) = ADD v38c4(0x20), v38c3(0x0)
    0x38c8: RETURN v38bf, v38c6(0x20)

}

function governanceRecoverUnsupported(address,uint256,address)() public {
    Begin block 0x648
    prev=[], succ=[0x65a, 0x65e]
    =================================
    0x649: v649(0x38e8) = CONST 
    0x64c: v64c(0x4) = CONST 
    0x64f: v64f = CALLDATASIZE 
    0x650: v650 = SUB v64f, v64c(0x4)
    0x651: v651(0x60) = CONST 
    0x654: v654 = LT v650, v651(0x60)
    0x655: v655 = ISZERO v654
    0x656: v656(0x65e) = CONST 
    0x659: JUMPI v656(0x65e), v655

    Begin block 0x65a
    prev=[0x648], succ=[]
    =================================
    0x65a: v65a(0x0) = CONST 
    0x65d: REVERT v65a(0x0), v65a(0x0)

    Begin block 0x65e
    prev=[0x648], succ=[0x12f0]
    =================================
    0x660: v660(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x676: v676 = CALLDATALOAD v64c(0x4)
    0x678: v678 = AND v660(0xffffffffffffffffffffffffffffffffffffffff), v676
    0x67a: v67a(0x20) = CONST 
    0x67d: v67d(0x24) = ADD v64c(0x4), v67a(0x20)
    0x67e: v67e = CALLDATALOAD v67d(0x24)
    0x680: v680(0x40) = CONST 
    0x684: v684(0x44) = ADD v64c(0x4), v680(0x40)
    0x685: v685 = CALLDATALOAD v684(0x44)
    0x686: v686 = AND v685, v660(0xffffffffffffffffffffffffffffffffffffffff)
    0x687: v687(0x12f0) = CONST 
    0x68a: JUMP v687(0x12f0)

    Begin block 0x12f0
    prev=[0x65e], succ=[0x1310, 0x1360]
    =================================
    0x12f1: v12f1(0x1) = CONST 
    0x12f3: v12f3 = SLOAD v12f1(0x1)
    0x12f4: v12f4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1309: v1309 = AND v12f4(0xffffffffffffffffffffffffffffffffffffffff), v12f3
    0x130a: v130a = CALLER 
    0x130b: v130b = EQ v130a, v1309
    0x130c: v130c(0x1360) = CONST 
    0x130f: JUMPI v130c(0x1360), v130b

    Begin block 0x1310
    prev=[0x12f0], succ=[]
    =================================
    0x1310: v1310(0x40) = CONST 
    0x1312: v1312 = MLOAD v1310(0x40)
    0x1313: v1313(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1335: MSTORE v1312, v1313(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1336: v1336(0x4) = CONST 
    0x1338: v1338 = ADD v1336(0x4), v1312
    0x133b: v133b(0x20) = CONST 
    0x133d: v133d = ADD v133b(0x20), v1338
    0x1340: v1340(0x20) = SUB v133d, v1338
    0x1342: MSTORE v1338, v1340(0x20)
    0x1343: v1343(0x28) = CONST 
    0x1346: MSTORE v133d, v1343(0x28)
    0x1347: v1347(0x20) = CONST 
    0x1349: v1349 = ADD v1347(0x20), v133d
    0x134b: v134b(0x311d) = CONST 
    0x134e: v134e(0x28) = CONST 
    0x1351: CODECOPY v1349, v134b(0x311d), v134e(0x28)
    0x1352: v1352(0x40) = CONST 
    0x1354: v1354 = ADD v1352(0x40), v1349
    0x1358: v1358(0x40) = CONST 
    0x135a: v135a = MLOAD v1358(0x40)
    0x135d: v135d(0x84) = SUB v1354, v135a
    0x135f: REVERT v135a, v135d(0x84)

    Begin block 0x1360
    prev=[0x12f0], succ=[0x2aa7B0x1360]
    =================================
    0x1361: v1361(0x3df7) = CONST 
    0x1364: v1364(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x137a: v137a = AND v678, v1364(0xffffffffffffffffffffffffffffffffffffffff)
    0x137d: v137d(0x2aa7) = CONST 
    0x1380: JUMP v137d(0x2aa7), v67e, v686, v137a, v1361(0x3df7)

    Begin block 0x2aa7B0x1360
    prev=[0x1360], succ=[0x2d24B0x2aa7B0x1360]
    =================================
    0x2aa8S0x1360: v2aa8V1360(0x40) = CONST 
    0x2aabS0x1360: v2aabV1360 = MLOAD v2aa8V1360(0x40)
    0x2aacS0x1360: v2aacV1360(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ac2S0x1360: v2ac2V1360 = AND v686, v2aacV1360(0xffffffffffffffffffffffffffffffffffffffff)
    0x2ac3S0x1360: v2ac3V1360(0x24) = CONST 
    0x2ac6S0x1360: v2ac6V1360 = ADD v2aabV1360, v2ac3V1360(0x24)
    0x2ac7S0x1360: MSTORE v2ac6V1360, v2ac2V1360
    0x2ac8S0x1360: v2ac8V1360(0x44) = CONST 
    0x2accS0x1360: v2accV1360 = ADD v2aabV1360, v2ac8V1360(0x44)
    0x2acfS0x1360: MSTORE v2accV1360, v67e
    0x2ad1S0x1360: v2ad1V1360 = MLOAD v2aa8V1360(0x40)
    0x2ad4S0x1360: v2ad4V1360(0x0) = SUB v2aabV1360, v2ad1V1360
    0x2ad7S0x1360: v2ad7V1360(0x44) = ADD v2ac8V1360(0x44), v2ad4V1360(0x0)
    0x2ad9S0x1360: MSTORE v2ad1V1360, v2ad7V1360(0x44)
    0x2adaS0x1360: v2adaV1360(0x64) = CONST 
    0x2adeS0x1360: v2adeV1360 = ADD v2aabV1360, v2adaV1360(0x64)
    0x2ae1S0x1360: MSTORE v2aa8V1360(0x40), v2adeV1360
    0x2ae2S0x1360: v2ae2V1360(0x20) = CONST 
    0x2ae5S0x1360: v2ae5V1360 = ADD v2ad1V1360, v2ae2V1360(0x20)
    0x2ae7S0x1360: v2ae7V1360 = MLOAD v2ae5V1360
    0x2ae8S0x1360: v2ae8V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2b05S0x1360: v2b05V1360 = AND v2ae8V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff), v2ae7V1360
    0x2b06S0x1360: v2b06V1360(0xa9059cbb00000000000000000000000000000000000000000000000000000000) = CONST 
    0x2b27S0x1360: v2b27V1360 = OR v2b06V1360(0xa9059cbb00000000000000000000000000000000000000000000000000000000), v2b05V1360
    0x2b29S0x1360: MSTORE v2ae5V1360, v2b27V1360
    0x2b2aS0x1360: v2b2aV1360(0x3faa) = CONST 
    0x2b30S0x1360: v2b30V1360(0x2d24) = CONST 
    0x2b33S0x1360: JUMP v2b30V1360(0x2d24), v2ad1V1360, v137a, v2b2aV1360(0x3faa)

    Begin block 0x2d24B0x2aa7B0x1360
    prev=[0x2aa7B0x1360], succ=[0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2d25S0x2aa7S0x1360: v2d25V2aa7V1360(0x60) = CONST 
    0x2d27S0x2aa7S0x1360: v2d27V2aa7V1360(0x2d86) = CONST 
    0x2d2bS0x2aa7S0x1360: v2d2bV2aa7V1360(0x40) = CONST 
    0x2d2dS0x2aa7S0x1360: v2d2dV2aa7V1360 = MLOAD v2d2bV2aa7V1360(0x40)
    0x2d2fS0x2aa7S0x1360: v2d2fV2aa7V1360(0x40) = CONST 
    0x2d31S0x2aa7S0x1360: v2d31V2aa7V1360 = ADD v2d2fV2aa7V1360(0x40), v2d2dV2aa7V1360
    0x2d32S0x2aa7S0x1360: v2d32V2aa7V1360(0x40) = CONST 
    0x2d34S0x2aa7S0x1360: MSTORE v2d32V2aa7V1360(0x40), v2d31V2aa7V1360
    0x2d36S0x2aa7S0x1360: v2d36V2aa7V1360(0x20) = CONST 
    0x2d39S0x2aa7S0x1360: MSTORE v2d2dV2aa7V1360, v2d36V2aa7V1360(0x20)
    0x2d3aS0x2aa7S0x1360: v2d3aV2aa7V1360(0x20) = CONST 
    0x2d3cS0x2aa7S0x1360: v2d3cV2aa7V1360 = ADD v2d3aV2aa7V1360(0x20), v2d2dV2aa7V1360
    0x2d3dS0x2aa7S0x1360: v2d3dV2aa7V1360(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564) = CONST 
    0x2d5fS0x2aa7S0x1360: MSTORE v2d3cV2aa7V1360, v2d3dV2aa7V1360(0x5361666545524332303a206c6f772d6c6576656c2063616c6c206661696c6564)
    0x2d62S0x2aa7S0x1360: v2d62V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d77S0x2aa7S0x1360: v2d77V2aa7V1360 = AND v2d62V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffff), v137a
    0x2d78S0x2aa7S0x1360: v2d78V2aa7V1360(0x2dfc) = CONST 
    0x2d7fS0x2aa7S0x1360: v2d7fV2aa7V1360(0xffffffff) = CONST 
    0x2d84S0x2aa7S0x1360: v2d84V2aa7V1360(0x2dfc) = AND v2d7fV2aa7V1360(0xffffffff), v2d78V2aa7V1360(0x2dfc)
    0x2d85S0x2aa7S0x1360: JUMP v2d84V2aa7V1360(0x2dfc)

    Begin block 0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2d24B0x2aa7B0x1360], succ=[0x2e13B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2dfdS0x2d24S0x2aa7S0x1360: v2dfdV2d24V2aa7V1360(0x60) = CONST 
    0x2dffS0x2d24S0x2aa7S0x1360: v2dffV2d24V2aa7V1360(0x2e0b) = CONST 
    0x2e04S0x2d24S0x2aa7S0x1360: v2e04V2d24V2aa7V1360(0x0) = CONST 
    0x2e07S0x2d24S0x2aa7S0x1360: v2e07V2d24V2aa7V1360(0x2e13) = CONST 
    0x2e0aS0x2d24S0x2aa7S0x1360: JUMP v2e07V2d24V2aa7V1360(0x2e13)

    Begin block 0x2e13B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2e1eB0x2dfcB0x2d24B0x2aa7B0x1360, 0x2e6eB0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2e14S0x2dfcS0x2d24S0x2aa7S0x1360: v2e14V2dfcV2d24V2aa7V1360(0x60) = CONST 
    0x2e17S0x2dfcS0x2d24S0x2aa7S0x1360: v2e17V2dfcV2d24V2aa7V1360 = SELFBALANCE 
    0x2e18S0x2dfcS0x2d24S0x2aa7S0x1360: v2e18V2dfcV2d24V2aa7V1360 = LT v2e17V2dfcV2d24V2aa7V1360, v2e04V2d24V2aa7V1360(0x0)
    0x2e19S0x2dfcS0x2d24S0x2aa7S0x1360: v2e19V2dfcV2d24V2aa7V1360 = ISZERO v2e18V2dfcV2d24V2aa7V1360
    0x2e1aS0x2dfcS0x2d24S0x2aa7S0x1360: v2e1aV2dfcV2d24V2aa7V1360(0x2e6e) = CONST 
    0x2e1dS0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2e1aV2dfcV2d24V2aa7V1360(0x2e6e), v2e19V2dfcV2d24V2aa7V1360

    Begin block 0x2e1eB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2e13B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[]
    =================================
    0x2e1eS0x2dfcS0x2d24S0x2aa7S0x1360: v2e1eV2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2e20S0x2dfcS0x2d24S0x2aa7S0x1360: v2e20V2dfcV2d24V2aa7V1360 = MLOAD v2e1eV2dfcV2d24V2aa7V1360(0x40)
    0x2e21S0x2dfcS0x2d24S0x2aa7S0x1360: v2e21V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2e43S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2e20V2dfcV2d24V2aa7V1360, v2e21V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2e44S0x2dfcS0x2d24S0x2aa7S0x1360: v2e44V2dfcV2d24V2aa7V1360(0x4) = CONST 
    0x2e46S0x2dfcS0x2d24S0x2aa7S0x1360: v2e46V2dfcV2d24V2aa7V1360 = ADD v2e44V2dfcV2d24V2aa7V1360(0x4), v2e20V2dfcV2d24V2aa7V1360
    0x2e49S0x2dfcS0x2d24S0x2aa7S0x1360: v2e49V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2e4bS0x2dfcS0x2d24S0x2aa7S0x1360: v2e4bV2dfcV2d24V2aa7V1360 = ADD v2e49V2dfcV2d24V2aa7V1360(0x20), v2e46V2dfcV2d24V2aa7V1360
    0x2e4eS0x2dfcS0x2d24S0x2aa7S0x1360: v2e4eV2dfcV2d24V2aa7V1360(0x20) = SUB v2e4bV2dfcV2d24V2aa7V1360, v2e46V2dfcV2d24V2aa7V1360
    0x2e50S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2e46V2dfcV2d24V2aa7V1360, v2e4eV2dfcV2d24V2aa7V1360(0x20)
    0x2e51S0x2dfcS0x2d24S0x2aa7S0x1360: v2e51V2dfcV2d24V2aa7V1360(0x26) = CONST 
    0x2e54S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2e4bV2dfcV2d24V2aa7V1360, v2e51V2dfcV2d24V2aa7V1360(0x26)
    0x2e55S0x2dfcS0x2d24S0x2aa7S0x1360: v2e55V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2e57S0x2dfcS0x2d24S0x2aa7S0x1360: v2e57V2dfcV2d24V2aa7V1360 = ADD v2e55V2dfcV2d24V2aa7V1360(0x20), v2e4bV2dfcV2d24V2aa7V1360
    0x2e59S0x2dfcS0x2d24S0x2aa7S0x1360: v2e59V2dfcV2d24V2aa7V1360(0x30c3) = CONST 
    0x2e5cS0x2dfcS0x2d24S0x2aa7S0x1360: v2e5cV2dfcV2d24V2aa7V1360(0x26) = CONST 
    0x2e5fS0x2dfcS0x2d24S0x2aa7S0x1360: CODECOPY v2e57V2dfcV2d24V2aa7V1360, v2e59V2dfcV2d24V2aa7V1360(0x30c3), v2e5cV2dfcV2d24V2aa7V1360(0x26)
    0x2e60S0x2dfcS0x2d24S0x2aa7S0x1360: v2e60V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2e62S0x2dfcS0x2d24S0x2aa7S0x1360: v2e62V2dfcV2d24V2aa7V1360 = ADD v2e60V2dfcV2d24V2aa7V1360(0x40), v2e57V2dfcV2d24V2aa7V1360
    0x2e66S0x2dfcS0x2d24S0x2aa7S0x1360: v2e66V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2e68S0x2dfcS0x2d24S0x2aa7S0x1360: v2e68V2dfcV2d24V2aa7V1360 = MLOAD v2e66V2dfcV2d24V2aa7V1360(0x40)
    0x2e6bS0x2dfcS0x2d24S0x2aa7S0x1360: v2e6bV2dfcV2d24V2aa7V1360(0x84) = SUB v2e62V2dfcV2d24V2aa7V1360, v2e68V2dfcV2d24V2aa7V1360
    0x2e6dS0x2dfcS0x2d24S0x2aa7S0x1360: REVERT v2e68V2dfcV2d24V2aa7V1360, v2e6bV2dfcV2d24V2aa7V1360(0x84)

    Begin block 0x2e6eB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2e13B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fceB0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2e6fS0x2dfcS0x2d24S0x2aa7S0x1360: v2e6fV2dfcV2d24V2aa7V1360(0x2e77) = CONST 
    0x2e73S0x2dfcS0x2d24S0x2aa7S0x1360: v2e73V2dfcV2d24V2aa7V1360(0x2fce) = CONST 
    0x2e76S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2e73V2dfcV2d24V2aa7V1360(0x2fce)

    Begin block 0x2fceB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2e6eB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2e77B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fcfS0x2dfcS0x2d24S0x2aa7S0x1360: v2fcfV2dfcV2d24V2aa7V1360 = EXTCODESIZE v2d77V2aa7V1360
    0x2fd0S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd0V2dfcV2d24V2aa7V1360 = ISZERO v2fcfV2dfcV2d24V2aa7V1360
    0x2fd1S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd1V2dfcV2d24V2aa7V1360 = ISZERO v2fd0V2dfcV2d24V2aa7V1360
    0x2fd3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2e6fV2dfcV2d24V2aa7V1360(0x2e77)

    Begin block 0x2e77B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fceB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2e7cB0x2dfcB0x2d24B0x2aa7B0x1360, 0x2ee2B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2e78S0x2dfcS0x2d24S0x2aa7S0x1360: v2e78V2dfcV2d24V2aa7V1360(0x2ee2) = CONST 
    0x2e7bS0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2e78V2dfcV2d24V2aa7V1360(0x2ee2), v2fd1V2dfcV2d24V2aa7V1360

    Begin block 0x2e7cB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2e77B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[]
    =================================
    0x2e7cS0x2dfcS0x2d24S0x2aa7S0x1360: v2e7cV2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2e7fS0x2dfcS0x2d24S0x2aa7S0x1360: v2e7fV2dfcV2d24V2aa7V1360 = MLOAD v2e7cV2dfcV2d24V2aa7V1360(0x40)
    0x2e80S0x2dfcS0x2d24S0x2aa7S0x1360: v2e80V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2ea2S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2e7fV2dfcV2d24V2aa7V1360, v2e80V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2ea3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ea3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2ea5S0x2dfcS0x2d24S0x2aa7S0x1360: v2ea5V2dfcV2d24V2aa7V1360(0x4) = CONST 
    0x2ea8S0x2dfcS0x2d24S0x2aa7S0x1360: v2ea8V2dfcV2d24V2aa7V1360 = ADD v2e7fV2dfcV2d24V2aa7V1360, v2ea5V2dfcV2d24V2aa7V1360(0x4)
    0x2ea9S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2ea8V2dfcV2d24V2aa7V1360, v2ea3V2dfcV2d24V2aa7V1360(0x20)
    0x2eaaS0x2dfcS0x2d24S0x2aa7S0x1360: v2eaaV2dfcV2d24V2aa7V1360(0x1d) = CONST 
    0x2eacS0x2dfcS0x2d24S0x2aa7S0x1360: v2eacV2dfcV2d24V2aa7V1360(0x24) = CONST 
    0x2eafS0x2dfcS0x2d24S0x2aa7S0x1360: v2eafV2dfcV2d24V2aa7V1360 = ADD v2e7fV2dfcV2d24V2aa7V1360, v2eacV2dfcV2d24V2aa7V1360(0x24)
    0x2eb0S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2eafV2dfcV2d24V2aa7V1360, v2eaaV2dfcV2d24V2aa7V1360(0x1d)
    0x2eb1S0x2dfcS0x2d24S0x2aa7S0x1360: v2eb1V2dfcV2d24V2aa7V1360(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000) = CONST 
    0x2ed2S0x2dfcS0x2d24S0x2aa7S0x1360: v2ed2V2dfcV2d24V2aa7V1360(0x44) = CONST 
    0x2ed5S0x2dfcS0x2d24S0x2aa7S0x1360: v2ed5V2dfcV2d24V2aa7V1360 = ADD v2e7fV2dfcV2d24V2aa7V1360, v2ed2V2dfcV2d24V2aa7V1360(0x44)
    0x2ed6S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2ed5V2dfcV2d24V2aa7V1360, v2eb1V2dfcV2d24V2aa7V1360(0x416464726573733a2063616c6c20746f206e6f6e2d636f6e7472616374000000)
    0x2ed8S0x2dfcS0x2d24S0x2aa7S0x1360: v2ed8V2dfcV2d24V2aa7V1360 = MLOAD v2e7cV2dfcV2d24V2aa7V1360(0x40)
    0x2edcS0x2dfcS0x2d24S0x2aa7S0x1360: v2edcV2dfcV2d24V2aa7V1360(0x0) = SUB v2e7fV2dfcV2d24V2aa7V1360, v2ed8V2dfcV2d24V2aa7V1360
    0x2eddS0x2dfcS0x2d24S0x2aa7S0x1360: v2eddV2dfcV2d24V2aa7V1360(0x64) = CONST 
    0x2edfS0x2dfcS0x2d24S0x2aa7S0x1360: v2edfV2dfcV2d24V2aa7V1360(0x64) = ADD v2eddV2dfcV2d24V2aa7V1360(0x64), v2edcV2dfcV2d24V2aa7V1360(0x0)
    0x2ee1S0x2dfcS0x2d24S0x2aa7S0x1360: REVERT v2ed8V2dfcV2d24V2aa7V1360, v2edfV2dfcV2d24V2aa7V1360(0x64)

    Begin block 0x2ee2B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2e77B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2f0fB0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2ee3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ee3V2dfcV2d24V2aa7V1360(0x0) = CONST 
    0x2ee5S0x2dfcS0x2d24S0x2aa7S0x1360: v2ee5V2dfcV2d24V2aa7V1360(0x60) = CONST 
    0x2ee8S0x2dfcS0x2d24S0x2aa7S0x1360: v2ee8V2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2efdS0x2dfcS0x2d24S0x2aa7S0x1360: v2efdV2dfcV2d24V2aa7V1360 = AND v2ee8V2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffff), v2d77V2aa7V1360
    0x2f00S0x2dfcS0x2d24S0x2aa7S0x1360: v2f00V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2f02S0x2dfcS0x2d24S0x2aa7S0x1360: v2f02V2dfcV2d24V2aa7V1360 = MLOAD v2f00V2dfcV2d24V2aa7V1360(0x40)
    0x2f06S0x2dfcS0x2d24S0x2aa7S0x1360: v2f06V2dfcV2d24V2aa7V1360(0x44) = MLOAD v2ad1V1360
    0x2f08S0x2dfcS0x2d24S0x2aa7S0x1360: v2f08V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2f0aS0x2dfcS0x2d24S0x2aa7S0x1360: v2f0aV2dfcV2d24V2aa7V1360 = ADD v2f08V2dfcV2d24V2aa7V1360(0x20), v2ad1V1360

    Begin block 0x2f0fB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2ee2B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2f18B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2f4cB0x2dfcB0x2d24B0x2aa7B0x1360, 0x2f18B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2f0f_0x2S0x2dfcS0x2d24S0x2aa7S0x1360: v2f0f_2V2dfcV2d24V2aa7V1360 = PHI v2f06V2dfcV2d24V2aa7V1360(0x44), v2f3fV2dfcV2d24V2aa7V1360
    0x2f10S0x2dfcS0x2d24S0x2aa7S0x1360: v2f10V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2f13S0x2dfcS0x2d24S0x2aa7S0x1360: v2f13V2dfcV2d24V2aa7V1360 = LT v2f0f_2V2dfcV2d24V2aa7V1360, v2f10V2dfcV2d24V2aa7V1360(0x20)
    0x2f14S0x2dfcS0x2d24S0x2aa7S0x1360: v2f14V2dfcV2d24V2aa7V1360(0x2f4c) = CONST 
    0x2f17S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2f14V2dfcV2d24V2aa7V1360(0x2f4c), v2f13V2dfcV2d24V2aa7V1360

    Begin block 0x2f4cB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2f0fB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2f8dB0x2dfcB0x2d24B0x2aa7B0x1360, 0x2faeB0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2f4c_0x0S0x2dfcS0x2d24S0x2aa7S0x1360: v2f4c_0V2dfcV2d24V2aa7V1360 = PHI v2f0aV2dfcV2d24V2aa7V1360, v2f47V2dfcV2d24V2aa7V1360
    0x2f4c_0x1S0x2dfcS0x2d24S0x2aa7S0x1360: v2f4c_1V2dfcV2d24V2aa7V1360 = PHI v2f02V2dfcV2d24V2aa7V1360, v2f45V2dfcV2d24V2aa7V1360
    0x2f4c_0x2S0x2dfcS0x2d24S0x2aa7S0x1360: v2f4c_2V2dfcV2d24V2aa7V1360 = PHI v2f06V2dfcV2d24V2aa7V1360(0x44), v2f3fV2dfcV2d24V2aa7V1360
    0x2f4dS0x2dfcS0x2d24S0x2aa7S0x1360: v2f4dV2dfcV2d24V2aa7V1360(0x1) = CONST 
    0x2f50S0x2dfcS0x2d24S0x2aa7S0x1360: v2f50V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2f52S0x2dfcS0x2d24S0x2aa7S0x1360: v2f52V2dfcV2d24V2aa7V1360 = SUB v2f50V2dfcV2d24V2aa7V1360(0x20), v2f4c_2V2dfcV2d24V2aa7V1360
    0x2f53S0x2dfcS0x2d24S0x2aa7S0x1360: v2f53V2dfcV2d24V2aa7V1360(0x100) = CONST 
    0x2f56S0x2dfcS0x2d24S0x2aa7S0x1360: v2f56V2dfcV2d24V2aa7V1360 = EXP v2f53V2dfcV2d24V2aa7V1360(0x100), v2f52V2dfcV2d24V2aa7V1360
    0x2f57S0x2dfcS0x2d24S0x2aa7S0x1360: v2f57V2dfcV2d24V2aa7V1360 = SUB v2f56V2dfcV2d24V2aa7V1360, v2f4dV2dfcV2d24V2aa7V1360(0x1)
    0x2f59S0x2dfcS0x2d24S0x2aa7S0x1360: v2f59V2dfcV2d24V2aa7V1360 = NOT v2f57V2dfcV2d24V2aa7V1360
    0x2f5bS0x2dfcS0x2d24S0x2aa7S0x1360: v2f5bV2dfcV2d24V2aa7V1360 = MLOAD v2f4c_0V2dfcV2d24V2aa7V1360
    0x2f5cS0x2dfcS0x2d24S0x2aa7S0x1360: v2f5cV2dfcV2d24V2aa7V1360 = AND v2f5bV2dfcV2d24V2aa7V1360, v2f59V2dfcV2d24V2aa7V1360
    0x2f5fS0x2dfcS0x2d24S0x2aa7S0x1360: v2f5fV2dfcV2d24V2aa7V1360 = MLOAD v2f4c_1V2dfcV2d24V2aa7V1360
    0x2f60S0x2dfcS0x2d24S0x2aa7S0x1360: v2f60V2dfcV2d24V2aa7V1360 = AND v2f5fV2dfcV2d24V2aa7V1360, v2f57V2dfcV2d24V2aa7V1360
    0x2f63S0x2dfcS0x2d24S0x2aa7S0x1360: v2f63V2dfcV2d24V2aa7V1360 = OR v2f5cV2dfcV2d24V2aa7V1360, v2f60V2dfcV2d24V2aa7V1360
    0x2f65S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2f4c_1V2dfcV2d24V2aa7V1360, v2f63V2dfcV2d24V2aa7V1360
    0x2f6eS0x2dfcS0x2d24S0x2aa7S0x1360: v2f6eV2dfcV2d24V2aa7V1360 = ADD v2f06V2dfcV2d24V2aa7V1360(0x44), v2f02V2dfcV2d24V2aa7V1360
    0x2f72S0x2dfcS0x2d24S0x2aa7S0x1360: v2f72V2dfcV2d24V2aa7V1360(0x0) = CONST 
    0x2f74S0x2dfcS0x2d24S0x2aa7S0x1360: v2f74V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2f76S0x2dfcS0x2d24S0x2aa7S0x1360: v2f76V2dfcV2d24V2aa7V1360 = MLOAD v2f74V2dfcV2d24V2aa7V1360(0x40)
    0x2f79S0x2dfcS0x2d24S0x2aa7S0x1360: v2f79V2dfcV2d24V2aa7V1360(0x44) = SUB v2f6eV2dfcV2d24V2aa7V1360, v2f76V2dfcV2d24V2aa7V1360
    0x2f7dS0x2dfcS0x2d24S0x2aa7S0x1360: v2f7dV2dfcV2d24V2aa7V1360 = GAS 
    0x2f7eS0x2dfcS0x2d24S0x2aa7S0x1360: v2f7eV2dfcV2d24V2aa7V1360 = CALL v2f7dV2dfcV2d24V2aa7V1360, v2efdV2dfcV2d24V2aa7V1360, v2e04V2d24V2aa7V1360(0x0), v2f76V2dfcV2d24V2aa7V1360, v2f79V2dfcV2d24V2aa7V1360(0x44), v2f76V2dfcV2d24V2aa7V1360, v2f72V2dfcV2d24V2aa7V1360(0x0)
    0x2f83S0x2dfcS0x2d24S0x2aa7S0x1360: v2f83V2dfcV2d24V2aa7V1360 = RETURNDATASIZE 
    0x2f85S0x2dfcS0x2d24S0x2aa7S0x1360: v2f85V2dfcV2d24V2aa7V1360(0x0) = CONST 
    0x2f88S0x2dfcS0x2d24S0x2aa7S0x1360: v2f88V2dfcV2d24V2aa7V1360 = EQ v2f83V2dfcV2d24V2aa7V1360, v2f85V2dfcV2d24V2aa7V1360(0x0)
    0x2f89S0x2dfcS0x2d24S0x2aa7S0x1360: v2f89V2dfcV2d24V2aa7V1360(0x2fae) = CONST 
    0x2f8cS0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2f89V2dfcV2d24V2aa7V1360(0x2fae), v2f88V2dfcV2d24V2aa7V1360

    Begin block 0x2f8dB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2f4cB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2f8dS0x2dfcS0x2d24S0x2aa7S0x1360: v2f8dV2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2f8fS0x2dfcS0x2d24S0x2aa7S0x1360: v2f8fV2dfcV2d24V2aa7V1360 = MLOAD v2f8dV2dfcV2d24V2aa7V1360(0x40)
    0x2f92S0x2dfcS0x2d24S0x2aa7S0x1360: v2f92V2dfcV2d24V2aa7V1360(0x1f) = CONST 
    0x2f94S0x2dfcS0x2d24S0x2aa7S0x1360: v2f94V2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2f92V2dfcV2d24V2aa7V1360(0x1f)
    0x2f95S0x2dfcS0x2d24S0x2aa7S0x1360: v2f95V2dfcV2d24V2aa7V1360(0x3f) = CONST 
    0x2f97S0x2dfcS0x2d24S0x2aa7S0x1360: v2f97V2dfcV2d24V2aa7V1360 = RETURNDATASIZE 
    0x2f98S0x2dfcS0x2d24S0x2aa7S0x1360: v2f98V2dfcV2d24V2aa7V1360 = ADD v2f97V2dfcV2d24V2aa7V1360, v2f95V2dfcV2d24V2aa7V1360(0x3f)
    0x2f99S0x2dfcS0x2d24S0x2aa7S0x1360: v2f99V2dfcV2d24V2aa7V1360 = AND v2f98V2dfcV2d24V2aa7V1360, v2f94V2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2f9bS0x2dfcS0x2d24S0x2aa7S0x1360: v2f9bV2dfcV2d24V2aa7V1360 = ADD v2f8fV2dfcV2d24V2aa7V1360, v2f99V2dfcV2d24V2aa7V1360
    0x2f9cS0x2dfcS0x2d24S0x2aa7S0x1360: v2f9cV2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2f9eS0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2f9cV2dfcV2d24V2aa7V1360(0x40), v2f9bV2dfcV2d24V2aa7V1360
    0x2f9fS0x2dfcS0x2d24S0x2aa7S0x1360: v2f9fV2dfcV2d24V2aa7V1360 = RETURNDATASIZE 
    0x2fa1S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2f8fV2dfcV2d24V2aa7V1360, v2f9fV2dfcV2d24V2aa7V1360
    0x2fa2S0x2dfcS0x2d24S0x2aa7S0x1360: v2fa2V2dfcV2d24V2aa7V1360 = RETURNDATASIZE 
    0x2fa3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fa3V2dfcV2d24V2aa7V1360(0x0) = CONST 
    0x2fa5S0x2dfcS0x2d24S0x2aa7S0x1360: v2fa5V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2fa8S0x2dfcS0x2d24S0x2aa7S0x1360: v2fa8V2dfcV2d24V2aa7V1360 = ADD v2f8fV2dfcV2d24V2aa7V1360, v2fa5V2dfcV2d24V2aa7V1360(0x20)
    0x2fa9S0x2dfcS0x2d24S0x2aa7S0x1360: RETURNDATACOPY v2fa8V2dfcV2d24V2aa7V1360, v2fa3V2dfcV2d24V2aa7V1360(0x0), v2fa2V2dfcV2d24V2aa7V1360
    0x2faaS0x2dfcS0x2d24S0x2aa7S0x1360: v2faaV2dfcV2d24V2aa7V1360(0x2fb3) = CONST 
    0x2fadS0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2faaV2dfcV2d24V2aa7V1360(0x2fb3)

    Begin block 0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2f8dB0x2dfcB0x2d24B0x2aa7B0x1360, 0x2faeB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fb3_0x1S0x2dfcS0x2d24S0x2aa7S0x1360: v2fb3_1V2dfcV2d24V2aa7V1360 = PHI v2f8fV2dfcV2d24V2aa7V1360, v2fafV2dfcV2d24V2aa7V1360(0x60)
    0x2fb9S0x2dfcS0x2d24S0x2aa7S0x1360: v2fb9V2dfcV2d24V2aa7V1360(0x2fc3) = CONST 
    0x2fbfS0x2dfcS0x2d24S0x2aa7S0x1360: v2fbfV2dfcV2d24V2aa7V1360(0x2fd4) = CONST 
    0x2fc2S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2fbfV2dfcV2d24V2aa7V1360(0x2fd4)

    Begin block 0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fe3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2fddB0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fd5S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd5V2fb3V2dfcV2d24V2aa7V1360(0x60) = CONST 
    0x2fd8S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd8V2fb3V2dfcV2d24V2aa7V1360 = ISZERO v2f7eV2dfcV2d24V2aa7V1360
    0x2fd9S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd9V2fb3V2dfcV2d24V2aa7V1360(0x2fe3) = CONST 
    0x2fdcS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2fd9V2fb3V2dfcV2d24V2aa7V1360(0x2fe3), v2fd8V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2fe3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2ff3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2febB0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fe5S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fe5V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2fb3_1V2dfcV2d24V2aa7V1360
    0x2fe6S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fe6V2fb3V2dfcV2d24V2aa7V1360 = ISZERO v2fe5V2fb3V2dfcV2d24V2aa7V1360
    0x2fe7S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fe7V2fb3V2dfcV2d24V2aa7V1360(0x2ff3) = CONST 
    0x2feaS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2fe7V2fb3V2dfcV2d24V2aa7V1360(0x2ff3), v2fe6V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2ff3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fe3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x3045B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c5d0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2ff4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ff4V2fb3V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2ff6S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ff6V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2ff4V2fb3V2dfcV2d24V2aa7V1360(0x40)
    0x2ff7S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ff7V2fb3V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x3019S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2ff6V2fb3V2dfcV2d24V2aa7V1360, v2ff7V2fb3V2dfcV2d24V2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x301aS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v301aV2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x301cS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v301cV2fb3V2dfcV2d24V2aa7V1360(0x4) = CONST 
    0x301fS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v301fV2fb3V2dfcV2d24V2aa7V1360 = ADD v2ff6V2fb3V2dfcV2d24V2aa7V1360, v301cV2fb3V2dfcV2d24V2aa7V1360(0x4)
    0x3022S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v301fV2fb3V2dfcV2d24V2aa7V1360, v301aV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x3024S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3024V2fb3V2dfcV2d24V2aa7V1360(0x20) = MLOAD v2d2dV2aa7V1360
    0x3025S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3025V2fb3V2dfcV2d24V2aa7V1360(0x24) = CONST 
    0x3028S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3028V2fb3V2dfcV2d24V2aa7V1360 = ADD v2ff6V2fb3V2dfcV2d24V2aa7V1360, v3025V2fb3V2dfcV2d24V2aa7V1360(0x24)
    0x3029S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v3028V2fb3V2dfcV2d24V2aa7V1360, v3024V2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x302bS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v302bV2fb3V2dfcV2d24V2aa7V1360(0x20) = MLOAD v2d2dV2aa7V1360
    0x3032S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3032V2fb3V2dfcV2d24V2aa7V1360(0x44) = CONST 
    0x3034S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3034V2fb3V2dfcV2d24V2aa7V1360 = ADD v3032V2fb3V2dfcV2d24V2aa7V1360(0x44), v2ff6V2fb3V2dfcV2d24V2aa7V1360
    0x3038S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3038V2fb3V2dfcV2d24V2aa7V1360 = ADD v2d2dV2aa7V1360, v301aV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x303dS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v303dV2fb3V2dfcV2d24V2aa7V1360(0x0) = CONST 
    0x3040S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3040V2fb3V2dfcV2d24V2aa7V1360 = ISZERO v302bV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x3041S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3041V2fb3V2dfcV2d24V2aa7V1360(0x2c5d) = CONST 
    0x3044S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v3041V2fb3V2dfcV2d24V2aa7V1360(0x2c5d), v3040V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x3045B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2ff3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c450x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x3047S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3047V2fb3V2dfcV2d24V2aa7V1360 = ADD v303dV2fb3V2dfcV2d24V2aa7V1360(0x0), v3038V2fb3V2dfcV2d24V2aa7V1360
    0x3048S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3048V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v3047V2fb3V2dfcV2d24V2aa7V1360
    0x304bS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v304bV2fb3V2dfcV2d24V2aa7V1360 = ADD v303dV2fb3V2dfcV2d24V2aa7V1360(0x0), v3034V2fb3V2dfcV2d24V2aa7V1360
    0x304cS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v304bV2fb3V2dfcV2d24V2aa7V1360, v3048V2fb3V2dfcV2d24V2aa7V1360
    0x304dS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v304dV2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x304fS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v304fV2fb3V2dfcV2d24V2aa7V1360(0x20) = ADD v304dV2fb3V2dfcV2d24V2aa7V1360(0x20), v303dV2fb3V2dfcV2d24V2aa7V1360(0x0)
    0x3050S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v3050V2fb3V2dfcV2d24V2aa7V1360(0x2c45) = CONST 
    0x3053S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v3050V2fb3V2dfcV2d24V2aa7V1360(0x2c45)

    Begin block 0x2c450x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x3045B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c4e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c4e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c5d0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2c450x2fd4_0x0S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2c452fd4_0V2fb3V2dfcV2d24V2aa7V1360 = PHI v304fV2fb3V2dfcV2d24V2aa7V1360(0x20), v2fd42c58V2fb3V2dfcV2d24V2aa7V1360
    0x2c480x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c48V2fb3V2dfcV2d24V2aa7V1360 = LT v2c452fd4_0V2fb3V2dfcV2d24V2aa7V1360, v302bV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x2c490x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c49V2fb3V2dfcV2d24V2aa7V1360 = ISZERO v2fd42c48V2fb3V2dfcV2d24V2aa7V1360
    0x2c4a0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c4aV2fb3V2dfcV2d24V2aa7V1360(0x2c5d) = CONST 
    0x2c4d0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2fd42c4aV2fb3V2dfcV2d24V2aa7V1360(0x2c5d), v2fd42c49V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2c4e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2c450x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c450x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2c4e0x2fd4_0x0S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2c4e2fd4_0V2fb3V2dfcV2d24V2aa7V1360 = PHI v304fV2fb3V2dfcV2d24V2aa7V1360(0x20), v2fd42c58V2fb3V2dfcV2d24V2aa7V1360
    0x2c500x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c50V2fb3V2dfcV2d24V2aa7V1360 = ADD v2c4e2fd4_0V2fb3V2dfcV2d24V2aa7V1360, v3038V2fb3V2dfcV2d24V2aa7V1360
    0x2c510x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c51V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2fd42c50V2fb3V2dfcV2d24V2aa7V1360
    0x2c540x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c54V2fb3V2dfcV2d24V2aa7V1360 = ADD v2c4e2fd4_0V2fb3V2dfcV2d24V2aa7V1360, v3034V2fb3V2dfcV2d24V2aa7V1360
    0x2c550x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2fd42c54V2fb3V2dfcV2d24V2aa7V1360, v2fd42c51V2fb3V2dfcV2d24V2aa7V1360
    0x2c560x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c56V2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2c580x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c58V2fb3V2dfcV2d24V2aa7V1360 = ADD v2fd42c56V2fb3V2dfcV2d24V2aa7V1360(0x20), v2c4e2fd4_0V2fb3V2dfcV2d24V2aa7V1360
    0x2c590x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c59V2fb3V2dfcV2d24V2aa7V1360(0x2c45) = CONST 
    0x2c5c0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2fd42c59V2fb3V2dfcV2d24V2aa7V1360(0x2c45)

    Begin block 0x2c5d0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2ff3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c450x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c710x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c8a0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2c660x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c66V2fb3V2dfcV2d24V2aa7V1360 = ADD v302bV2fb3V2dfcV2d24V2aa7V1360(0x20), v3034V2fb3V2dfcV2d24V2aa7V1360
    0x2c680x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c68V2fb3V2dfcV2d24V2aa7V1360(0x1f) = CONST 
    0x2c6a0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c6aV2fb3V2dfcV2d24V2aa7V1360(0x0) = AND v2fd42c68V2fb3V2dfcV2d24V2aa7V1360(0x1f), v302bV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x2c6c0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c6cV2fb3V2dfcV2d24V2aa7V1360 = ISZERO v2fd42c6aV2fb3V2dfcV2d24V2aa7V1360(0x0)
    0x2c6d0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c6dV2fb3V2dfcV2d24V2aa7V1360(0x2c8a) = CONST 
    0x2c700x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMPI v2fd42c6dV2fb3V2dfcV2d24V2aa7V1360(0x2c8a), v2fd42c6cV2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2c710x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2c5d0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c8a0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2c730x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c73V2fb3V2dfcV2d24V2aa7V1360 = SUB v2fd42c66V2fb3V2dfcV2d24V2aa7V1360, v2fd42c6aV2fb3V2dfcV2d24V2aa7V1360(0x0)
    0x2c750x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c75V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2fd42c73V2fb3V2dfcV2d24V2aa7V1360
    0x2c760x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c76V2fb3V2dfcV2d24V2aa7V1360(0x1) = CONST 
    0x2c790x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c79V2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2c7b0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c7bV2fb3V2dfcV2d24V2aa7V1360(0x20) = SUB v2fd42c79V2fb3V2dfcV2d24V2aa7V1360(0x20), v2fd42c6aV2fb3V2dfcV2d24V2aa7V1360(0x0)
    0x2c7c0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c7cV2fb3V2dfcV2d24V2aa7V1360(0x100) = CONST 
    0x2c7f0x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c7fV2fb3V2dfcV2d24V2aa7V1360(0x1) = EXP v2fd42c7cV2fb3V2dfcV2d24V2aa7V1360(0x100), v2fd42c7bV2fb3V2dfcV2d24V2aa7V1360(0x20)
    0x2c800x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c80V2fb3V2dfcV2d24V2aa7V1360(0x0) = SUB v2fd42c7fV2fb3V2dfcV2d24V2aa7V1360(0x1), v2fd42c76V2fb3V2dfcV2d24V2aa7V1360(0x1)
    0x2c810x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c81V2fb3V2dfcV2d24V2aa7V1360 = NOT v2fd42c80V2fb3V2dfcV2d24V2aa7V1360(0x0)
    0x2c820x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c82V2fb3V2dfcV2d24V2aa7V1360 = AND v2fd42c81V2fb3V2dfcV2d24V2aa7V1360, v2fd42c75V2fb3V2dfcV2d24V2aa7V1360
    0x2c840x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2fd42c73V2fb3V2dfcV2d24V2aa7V1360, v2fd42c82V2fb3V2dfcV2d24V2aa7V1360
    0x2c850x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c85V2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2c870x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c87V2fb3V2dfcV2d24V2aa7V1360 = ADD v2fd42c85V2fb3V2dfcV2d24V2aa7V1360(0x20), v2fd42c73V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2c8a0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2c5d0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360, 0x2c710x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[]
    =================================
    0x2c8a0x2fd4_0x1S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2c8a2fd4_1V2fb3V2dfcV2d24V2aa7V1360 = PHI v2fd42c66V2fb3V2dfcV2d24V2aa7V1360, v2fd42c87V2fb3V2dfcV2d24V2aa7V1360
    0x2c900x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c90V2fb3V2dfcV2d24V2aa7V1360(0x40) = CONST 
    0x2c920x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c92V2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2fd42c90V2fb3V2dfcV2d24V2aa7V1360(0x40)
    0x2c950x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fd42c95V2fb3V2dfcV2d24V2aa7V1360 = SUB v2c8a2fd4_1V2fb3V2dfcV2d24V2aa7V1360, v2fd42c92V2fb3V2dfcV2d24V2aa7V1360
    0x2c970x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: REVERT v2fd42c92V2fb3V2dfcV2d24V2aa7V1360, v2fd42c95V2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2febB0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fe3B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[]
    =================================
    0x2fecS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fecV2fb3V2dfcV2d24V2aa7V1360 = MLOAD v2fb3_1V2dfcV2d24V2aa7V1360
    0x2fefS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fefV2fb3V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2ff1S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2ff1V2fb3V2dfcV2d24V2aa7V1360 = ADD v2fefV2fb3V2dfcV2d24V2aa7V1360(0x20), v2fb3_1V2dfcV2d24V2aa7V1360
    0x2ff2S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: REVERT v2ff1V2fb3V2dfcV2d24V2aa7V1360, v2fecV2fb3V2dfcV2d24V2aa7V1360

    Begin block 0x2fddB0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2c9e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fdfS0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: v2fdfV2fb3V2dfcV2d24V2aa7V1360(0x2c9e) = CONST 
    0x2fe2S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2fdfV2fb3V2dfcV2d24V2aa7V1360(0x2c9e)

    Begin block 0x2c9e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2fddB0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fc3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2ca40x2fd4S0x2fb3S0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2fb9V2dfcV2d24V2aa7V1360(0x2fc3)

    Begin block 0x2fc3B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2c9e0x2fd4B0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2e0bB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fcdS0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2dffV2d24V2aa7V1360(0x2e0b)

    Begin block 0x2e0bB0x2d24B0x2aa7B0x1360
    prev=[0x2fc3B0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2d86B0x2aa7B0x1360]
    =================================
    0x2e12S0x2d24S0x2aa7S0x1360: JUMP v2d27V2aa7V1360(0x2d86)

    Begin block 0x2d86B0x2aa7B0x1360
    prev=[0x2e0bB0x2d24B0x2aa7B0x1360], succ=[0x3fceB0x2aa7B0x1360, 0x2d91B0x2aa7B0x1360]
    =================================
    0x2d88S0x2aa7S0x1360: v2d88V2aa7V1360 = MLOAD v2fb3_1V2dfcV2d24V2aa7V1360
    0x2d8cS0x2aa7S0x1360: v2d8cV2aa7V1360 = ISZERO v2d88V2aa7V1360
    0x2d8dS0x2aa7S0x1360: v2d8dV2aa7V1360(0x3fce) = CONST 
    0x2d90S0x2aa7S0x1360: JUMPI v2d8dV2aa7V1360(0x3fce), v2d8cV2aa7V1360

    Begin block 0x3fceB0x2aa7B0x1360
    prev=[0x2d86B0x2aa7B0x1360], succ=[0x3faaB0x1360]
    =================================
    0x3fd2S0x2aa7S0x1360: JUMP v2b2aV1360(0x3faa)

    Begin block 0x3faaB0x1360
    prev=[0x3fceB0x2aa7B0x1360, 0x3ff2B0x2aa7B0x1360], succ=[0x3df7]
    =================================
    0x3faeS0x1360: JUMP v1361(0x3df7)

    Begin block 0x3df7
    prev=[0x3faaB0x1360], succ=[0x38e8]
    =================================
    0x3dfb: JUMP v649(0x38e8)

    Begin block 0x38e8
    prev=[0x3df7], succ=[]
    =================================
    0x38e9: STOP 

    Begin block 0x2d91B0x2aa7B0x1360
    prev=[0x2d86B0x2aa7B0x1360], succ=[0x2da1B0x2aa7B0x1360, 0x2da5B0x2aa7B0x1360]
    =================================
    0x2d93S0x2aa7S0x1360: v2d93V2aa7V1360(0x20) = CONST 
    0x2d95S0x2aa7S0x1360: v2d95V2aa7V1360 = ADD v2d93V2aa7V1360(0x20), v2fb3_1V2dfcV2d24V2aa7V1360
    0x2d97S0x2aa7S0x1360: v2d97V2aa7V1360 = MLOAD v2fb3_1V2dfcV2d24V2aa7V1360
    0x2d98S0x2aa7S0x1360: v2d98V2aa7V1360(0x20) = CONST 
    0x2d9bS0x2aa7S0x1360: v2d9bV2aa7V1360 = LT v2d97V2aa7V1360, v2d98V2aa7V1360(0x20)
    0x2d9cS0x2aa7S0x1360: v2d9cV2aa7V1360 = ISZERO v2d9bV2aa7V1360
    0x2d9dS0x2aa7S0x1360: v2d9dV2aa7V1360(0x2da5) = CONST 
    0x2da0S0x2aa7S0x1360: JUMPI v2d9dV2aa7V1360(0x2da5), v2d9cV2aa7V1360

    Begin block 0x2da1B0x2aa7B0x1360
    prev=[0x2d91B0x2aa7B0x1360], succ=[]
    =================================
    0x2da1S0x2aa7S0x1360: v2da1V2aa7V1360(0x0) = CONST 
    0x2da4S0x2aa7S0x1360: REVERT v2da1V2aa7V1360(0x0), v2da1V2aa7V1360(0x0)

    Begin block 0x2da5B0x2aa7B0x1360
    prev=[0x2d91B0x2aa7B0x1360], succ=[0x2dacB0x2aa7B0x1360, 0x3ff2B0x2aa7B0x1360]
    =================================
    0x2da7S0x2aa7S0x1360: v2da7V2aa7V1360 = MLOAD v2d95V2aa7V1360
    0x2da8S0x2aa7S0x1360: v2da8V2aa7V1360(0x3ff2) = CONST 
    0x2dabS0x2aa7S0x1360: JUMPI v2da8V2aa7V1360(0x3ff2), v2da7V2aa7V1360

    Begin block 0x2dacB0x2aa7B0x1360
    prev=[0x2da5B0x2aa7B0x1360], succ=[]
    =================================
    0x2dacS0x2aa7S0x1360: v2dacV2aa7V1360(0x40) = CONST 
    0x2daeS0x2aa7S0x1360: v2daeV2aa7V1360 = MLOAD v2dacV2aa7V1360(0x40)
    0x2dafS0x2aa7S0x1360: v2dafV2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2dd1S0x2aa7S0x1360: MSTORE v2daeV2aa7V1360, v2dafV2aa7V1360(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2dd2S0x2aa7S0x1360: v2dd2V2aa7V1360(0x4) = CONST 
    0x2dd4S0x2aa7S0x1360: v2dd4V2aa7V1360 = ADD v2dd2V2aa7V1360(0x4), v2daeV2aa7V1360
    0x2dd7S0x2aa7S0x1360: v2dd7V2aa7V1360(0x20) = CONST 
    0x2dd9S0x2aa7S0x1360: v2dd9V2aa7V1360 = ADD v2dd7V2aa7V1360(0x20), v2dd4V2aa7V1360
    0x2ddcS0x2aa7S0x1360: v2ddcV2aa7V1360(0x20) = SUB v2dd9V2aa7V1360, v2dd4V2aa7V1360
    0x2ddeS0x2aa7S0x1360: MSTORE v2dd4V2aa7V1360, v2ddcV2aa7V1360(0x20)
    0x2ddfS0x2aa7S0x1360: v2ddfV2aa7V1360(0x2a) = CONST 
    0x2de2S0x2aa7S0x1360: MSTORE v2dd9V2aa7V1360, v2ddfV2aa7V1360(0x2a)
    0x2de3S0x2aa7S0x1360: v2de3V2aa7V1360(0x20) = CONST 
    0x2de5S0x2aa7S0x1360: v2de5V2aa7V1360 = ADD v2de3V2aa7V1360(0x20), v2dd9V2aa7V1360
    0x2de7S0x2aa7S0x1360: v2de7V2aa7V1360(0x328e) = CONST 
    0x2deaS0x2aa7S0x1360: v2deaV2aa7V1360(0x2a) = CONST 
    0x2dedS0x2aa7S0x1360: CODECOPY v2de5V2aa7V1360, v2de7V2aa7V1360(0x328e), v2deaV2aa7V1360(0x2a)
    0x2deeS0x2aa7S0x1360: v2deeV2aa7V1360(0x40) = CONST 
    0x2df0S0x2aa7S0x1360: v2df0V2aa7V1360 = ADD v2deeV2aa7V1360(0x40), v2de5V2aa7V1360
    0x2df4S0x2aa7S0x1360: v2df4V2aa7V1360(0x40) = CONST 
    0x2df6S0x2aa7S0x1360: v2df6V2aa7V1360 = MLOAD v2df4V2aa7V1360(0x40)
    0x2df9S0x2aa7S0x1360: v2df9V2aa7V1360(0x84) = SUB v2df0V2aa7V1360, v2df6V2aa7V1360
    0x2dfbS0x2aa7S0x1360: REVERT v2df6V2aa7V1360, v2df9V2aa7V1360(0x84)

    Begin block 0x3ff2B0x2aa7B0x1360
    prev=[0x2da5B0x2aa7B0x1360], succ=[0x3faaB0x1360]
    =================================
    0x3ff6S0x2aa7S0x1360: JUMP v2b2aV1360(0x3faa)

    Begin block 0x2faeB0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2f4cB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2fb3B0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2fafS0x2dfcS0x2d24S0x2aa7S0x1360: v2fafV2dfcV2d24V2aa7V1360(0x60) = CONST 

    Begin block 0x2f18B0x2dfcB0x2d24B0x2aa7B0x1360
    prev=[0x2f0fB0x2dfcB0x2d24B0x2aa7B0x1360], succ=[0x2f0fB0x2dfcB0x2d24B0x2aa7B0x1360]
    =================================
    0x2f18_0x0S0x2dfcS0x2d24S0x2aa7S0x1360: v2f18_0V2dfcV2d24V2aa7V1360 = PHI v2f0aV2dfcV2d24V2aa7V1360, v2f47V2dfcV2d24V2aa7V1360
    0x2f18_0x1S0x2dfcS0x2d24S0x2aa7S0x1360: v2f18_1V2dfcV2d24V2aa7V1360 = PHI v2f02V2dfcV2d24V2aa7V1360, v2f45V2dfcV2d24V2aa7V1360
    0x2f18_0x2S0x2dfcS0x2d24S0x2aa7S0x1360: v2f18_2V2dfcV2d24V2aa7V1360 = PHI v2f06V2dfcV2d24V2aa7V1360(0x44), v2f3fV2dfcV2d24V2aa7V1360
    0x2f19S0x2dfcS0x2d24S0x2aa7S0x1360: v2f19V2dfcV2d24V2aa7V1360 = MLOAD v2f18_0V2dfcV2d24V2aa7V1360
    0x2f1bS0x2dfcS0x2d24S0x2aa7S0x1360: MSTORE v2f18_1V2dfcV2d24V2aa7V1360, v2f19V2dfcV2d24V2aa7V1360
    0x2f1cS0x2dfcS0x2d24S0x2aa7S0x1360: v2f1cV2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = CONST 
    0x2f3fS0x2dfcS0x2d24S0x2aa7S0x1360: v2f3fV2dfcV2d24V2aa7V1360 = ADD v2f18_2V2dfcV2d24V2aa7V1360, v2f1cV2dfcV2d24V2aa7V1360(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2f41S0x2dfcS0x2d24S0x2aa7S0x1360: v2f41V2dfcV2d24V2aa7V1360(0x20) = CONST 
    0x2f45S0x2dfcS0x2d24S0x2aa7S0x1360: v2f45V2dfcV2d24V2aa7V1360 = ADD v2f41V2dfcV2d24V2aa7V1360(0x20), v2f18_1V2dfcV2d24V2aa7V1360
    0x2f47S0x2dfcS0x2d24S0x2aa7S0x1360: v2f47V2dfcV2d24V2aa7V1360 = ADD v2f41V2dfcV2d24V2aa7V1360(0x20), v2f18_0V2dfcV2d24V2aa7V1360
    0x2f48S0x2dfcS0x2d24S0x2aa7S0x1360: v2f48V2dfcV2d24V2aa7V1360(0x2f0f) = CONST 
    0x2f4bS0x2dfcS0x2d24S0x2aa7S0x1360: JUMP v2f48V2dfcV2d24V2aa7V1360(0x2f0f)

}

function operator()() public {
    Begin block 0x68b
    prev=[], succ=[0x1386]
    =================================
    0x68c: v68c(0x3909) = CONST 
    0x68f: v68f(0x1386) = CONST 
    0x692: JUMP v68f(0x1386)

    Begin block 0x1386
    prev=[0x68b], succ=[0x3909]
    =================================
    0x1387: v1387(0x1) = CONST 
    0x1389: v1389 = SLOAD v1387(0x1)
    0x138a: v138a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x139f: v139f = AND v138a(0xffffffffffffffffffffffffffffffffffffffff), v1389
    0x13a1: JUMP v68c(0x3909)

    Begin block 0x3909
    prev=[0x1386], succ=[]
    =================================
    0x390a: v390a(0x40) = CONST 
    0x390d: v390d = MLOAD v390a(0x40)
    0x390e: v390e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3925: v3925 = AND v139f, v390e(0xffffffffffffffffffffffffffffffffffffffff)
    0x3927: MSTORE v390d, v3925
    0x3928: v3928 = MLOAD v390a(0x40)
    0x392c: v392c(0x0) = SUB v390d, v3928
    0x392d: v392d(0x20) = CONST 
    0x392f: v392f(0x20) = ADD v392d(0x20), v392c(0x0)
    0x3931: RETURN v3928, v392f(0x20)

}

function treasury()() public {
    Begin block 0x693
    prev=[], succ=[0x13a2]
    =================================
    0x694: v694(0x3951) = CONST 
    0x697: v697(0x13a2) = CONST 
    0x69a: JUMP v697(0x13a2)

    Begin block 0x13a2
    prev=[0x693], succ=[0x3951]
    =================================
    0x13a3: v13a3(0x3) = CONST 
    0x13a5: v13a5 = SLOAD v13a3(0x3)
    0x13a6: v13a6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x13bb: v13bb = AND v13a6(0xffffffffffffffffffffffffffffffffffffffff), v13a5
    0x13bd: JUMP v694(0x3951)

    Begin block 0x3951
    prev=[0x13a2], succ=[]
    =================================
    0x3952: v3952(0x40) = CONST 
    0x3955: v3955 = MLOAD v3952(0x40)
    0x3956: v3956(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x396d: v396d = AND v13bb, v3956(0xffffffffffffffffffffffffffffffffffffffff)
    0x396f: MSTORE v3955, v396d
    0x3970: v3970 = MLOAD v3952(0x40)
    0x3974: v3974(0x0) = SUB v3955, v3970
    0x3975: v3975(0x20) = CONST 
    0x3977: v3977(0x20) = ADD v3975(0x20), v3974(0x0)
    0x3979: RETURN v3970, v3977(0x20)

}

function purchasedEpochs(address,uint256)() public {
    Begin block 0x69b
    prev=[], succ=[0x6ad, 0x6b1]
    =================================
    0x69c: v69c(0x3999) = CONST 
    0x69f: v69f(0x4) = CONST 
    0x6a2: v6a2 = CALLDATASIZE 
    0x6a3: v6a3 = SUB v6a2, v69f(0x4)
    0x6a4: v6a4(0x40) = CONST 
    0x6a7: v6a7 = LT v6a3, v6a4(0x40)
    0x6a8: v6a8 = ISZERO v6a7
    0x6a9: v6a9(0x6b1) = CONST 
    0x6ac: JUMPI v6a9(0x6b1), v6a8

    Begin block 0x6ad
    prev=[0x69b], succ=[]
    =================================
    0x6ad: v6ad(0x0) = CONST 
    0x6b0: REVERT v6ad(0x0), v6ad(0x0)

    Begin block 0x6b1
    prev=[0x69b], succ=[0x13be]
    =================================
    0x6b3: v6b3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x6c9: v6c9 = CALLDATALOAD v69f(0x4)
    0x6ca: v6ca = AND v6c9, v6b3(0xffffffffffffffffffffffffffffffffffffffff)
    0x6cc: v6cc(0x20) = CONST 
    0x6ce: v6ce(0x24) = ADD v6cc(0x20), v69f(0x4)
    0x6cf: v6cf = CALLDATALOAD v6ce(0x24)
    0x6d0: v6d0(0x13be) = CONST 
    0x6d3: JUMP v6d0(0x13be)

    Begin block 0x13be
    prev=[0x6b1], succ=[0x13d6, 0x13d7]
    =================================
    0x13bf: v13bf(0xf) = CONST 
    0x13c1: v13c1(0x20) = CONST 
    0x13c3: MSTORE v13c1(0x20), v13bf(0xf)
    0x13c5: v13c5(0x0) = CONST 
    0x13c7: MSTORE v13c5(0x0), v6ca
    0x13c8: v13c8(0x40) = CONST 
    0x13ca: v13ca(0x0) = CONST 
    0x13cc: v13cc = SHA3 v13ca(0x0), v13c8(0x40)
    0x13cf: v13cf = SLOAD v13cc
    0x13d1: v13d1 = LT v6cf, v13cf
    0x13d2: v13d2(0x13d7) = CONST 
    0x13d5: JUMPI v13d2(0x13d7), v13d1

    Begin block 0x13d6
    prev=[0x13be], succ=[]
    =================================
    0x13d6: THROW 

    Begin block 0x13d7
    prev=[0x13be], succ=[0x3999]
    =================================
    0x13d9: v13d9(0x0) = CONST 
    0x13db: MSTORE v13d9(0x0), v13cc
    0x13dc: v13dc(0x20) = CONST 
    0x13de: v13de(0x0) = CONST 
    0x13e0: v13e0 = SHA3 v13de(0x0), v13dc(0x20)
    0x13e1: v13e1 = ADD v13e0, v6cf
    0x13e2: v13e2(0x0) = CONST 
    0x13e9: v13e9 = SLOAD v13e1
    0x13eb: JUMP v69c(0x3999)

    Begin block 0x3999
    prev=[0x13d7], succ=[]
    =================================
    0x399a: v399a(0x40) = CONST 
    0x399d: v399d = MLOAD v399a(0x40)
    0x39a0: MSTORE v399d, v13e9
    0x39a1: v39a1 = MLOAD v399a(0x40)
    0x39a5: v39a5(0x0) = SUB v399d, v39a1
    0x39a6: v39a6(0x20) = CONST 
    0x39a8: v39a8(0x20) = ADD v39a6(0x20), v39a5(0x0)
    0x39aa: RETURN v39a1, v39a8(0x20)

}

function issueNewBond(uint256)() public {
    Begin block 0x6d4
    prev=[], succ=[0x6e6, 0x6ea]
    =================================
    0x6d5: v6d5(0x39ca) = CONST 
    0x6d8: v6d8(0x4) = CONST 
    0x6db: v6db = CALLDATASIZE 
    0x6dc: v6dc = SUB v6db, v6d8(0x4)
    0x6dd: v6dd(0x20) = CONST 
    0x6e0: v6e0 = LT v6dc, v6dd(0x20)
    0x6e1: v6e1 = ISZERO v6e0
    0x6e2: v6e2(0x6ea) = CONST 
    0x6e5: JUMPI v6e2(0x6ea), v6e1

    Begin block 0x6e6
    prev=[0x6d4], succ=[]
    =================================
    0x6e6: v6e6(0x0) = CONST 
    0x6e9: REVERT v6e6(0x0), v6e6(0x0)

    Begin block 0x6ea
    prev=[0x6d4], succ=[0x13ec]
    =================================
    0x6ec: v6ec = CALLDATALOAD v6d8(0x4)
    0x6ed: v6ed(0x13ec) = CONST 
    0x6f0: JUMP v6ed(0x13ec)

    Begin block 0x13ec
    prev=[0x6ea], succ=[0x1429, 0x140d]
    =================================
    0x13ed: v13ed(0x3) = CONST 
    0x13ef: v13ef = SLOAD v13ed(0x3)
    0x13f0: v13f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1405: v1405 = AND v13f0(0xffffffffffffffffffffffffffffffffffffffff), v13ef
    0x1406: v1406 = CALLER 
    0x1407: v1407 = EQ v1406, v1405
    0x1409: v1409(0x1429) = CONST 
    0x140c: JUMPI v1409(0x1429), v1407

    Begin block 0x1429
    prev=[0x13ec, 0x140d], succ=[0x142e, 0x147e]
    =================================
    0x1429_0x0: v1429_0 = PHI v1407, v1428
    0x142a: v142a(0x147e) = CONST 
    0x142d: JUMPI v142a(0x147e), v1429_0

    Begin block 0x142e
    prev=[0x1429], succ=[]
    =================================
    0x142e: v142e(0x40) = CONST 
    0x1430: v1430 = MLOAD v142e(0x40)
    0x1431: v1431(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1453: MSTORE v1430, v1431(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1454: v1454(0x4) = CONST 
    0x1456: v1456 = ADD v1454(0x4), v1430
    0x1459: v1459(0x20) = CONST 
    0x145b: v145b = ADD v1459(0x20), v1456
    0x145e: v145e(0x20) = SUB v145b, v1456
    0x1460: MSTORE v1456, v145e(0x20)
    0x1461: v1461(0x33) = CONST 
    0x1464: MSTORE v145b, v1461(0x33)
    0x1465: v1465(0x20) = CONST 
    0x1467: v1467 = ADD v1465(0x20), v145b
    0x1469: v1469(0x31cf) = CONST 
    0x146c: v146c(0x33) = CONST 
    0x146f: CODECOPY v1467, v1469(0x31cf), v146c(0x33)
    0x1470: v1470(0x40) = CONST 
    0x1472: v1472 = ADD v1470(0x40), v1467
    0x1476: v1476(0x40) = CONST 
    0x1478: v1478 = MLOAD v1476(0x40)
    0x147b: v147b(0x84) = SUB v1472, v1478
    0x147d: REVERT v1478, v147b(0x84)

    Begin block 0x147e
    prev=[0x1429], succ=[0x148b]
    =================================
    0x147f: v147f(0x6) = CONST 
    0x1481: v1481 = SLOAD v147f(0x6)
    0x1482: v1482(0x148b) = CONST 
    0x1487: v1487(0x2933) = CONST 
    0x148a: v148a_0 = CALLPRIVATE v1487(0x2933), v6ec, v1481, v1482(0x148b)

    Begin block 0x148b
    prev=[0x147e], succ=[0x39ca]
    =================================
    0x148c: v148c(0x6) = CONST 
    0x148e: SSTORE v148c(0x6), v148a_0
    0x1490: JUMP v6d5(0x39ca)

    Begin block 0x39ca
    prev=[0x148b], succ=[]
    =================================
    0x39cb: STOP 

    Begin block 0x140d
    prev=[0x13ec], succ=[0x1429]
    =================================
    0x140e: v140e(0x1) = CONST 
    0x1410: v1410 = SLOAD v140e(0x1)
    0x1411: v1411(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1426: v1426 = AND v1411(0xffffffffffffffffffffffffffffffffffffffff), v1410
    0x1427: v1427 = CALLER 
    0x1428: v1428 = EQ v1427, v1426

}

function balanceOf(address)() public {
    Begin block 0x6f1
    prev=[], succ=[0x703, 0x707]
    =================================
    0x6f2: v6f2(0x39eb) = CONST 
    0x6f5: v6f5(0x4) = CONST 
    0x6f8: v6f8 = CALLDATASIZE 
    0x6f9: v6f9 = SUB v6f8, v6f5(0x4)
    0x6fa: v6fa(0x20) = CONST 
    0x6fd: v6fd = LT v6f9, v6fa(0x20)
    0x6fe: v6fe = ISZERO v6fd
    0x6ff: v6ff(0x707) = CONST 
    0x702: JUMPI v6ff(0x707), v6fe

    Begin block 0x703
    prev=[0x6f1], succ=[]
    =================================
    0x703: v703(0x0) = CONST 
    0x706: REVERT v703(0x0), v703(0x0)

    Begin block 0x707
    prev=[0x6f1], succ=[0x1491]
    =================================
    0x709: v709 = CALLDATALOAD v6f5(0x4)
    0x70a: v70a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x71f: v71f = AND v70a(0xffffffffffffffffffffffffffffffffffffffff), v709
    0x720: v720(0x1491) = CONST 
    0x723: JUMP v720(0x1491)

    Begin block 0x1491
    prev=[0x707], succ=[0x39eb]
    =================================
    0x1492: v1492(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x14a7: v14a7 = AND v1492(0xffffffffffffffffffffffffffffffffffffffff), v71f
    0x14a8: v14a8(0x0) = CONST 
    0x14ac: MSTORE v14a8(0x0), v14a7
    0x14ad: v14ad(0x12) = CONST 
    0x14af: v14af(0x20) = CONST 
    0x14b1: MSTORE v14af(0x20), v14ad(0x12)
    0x14b2: v14b2(0x40) = CONST 
    0x14b5: v14b5 = SHA3 v14a8(0x0), v14b2(0x40)
    0x14b6: v14b6 = SLOAD v14b5
    0x14b8: JUMP v6f2(0x39eb)

    Begin block 0x39eb
    prev=[0x1491], succ=[]
    =================================
    0x39ec: v39ec(0x40) = CONST 
    0x39ef: v39ef = MLOAD v39ec(0x40)
    0x39f2: MSTORE v39ef, v14b6
    0x39f3: v39f3 = MLOAD v39ec(0x40)
    0x39f7: v39f7(0x0) = SUB v39ef, v39f3
    0x39f8: v39f8(0x20) = CONST 
    0x39fa: v39fa(0x20) = ADD v39f8(0x20), v39f7(0x0)
    0x39fc: RETURN v39f3, v39fa(0x20)

}

function buyCoupons(uint256,uint256)() public {
    Begin block 0x724
    prev=[], succ=[0x736, 0x73a]
    =================================
    0x725: v725(0x37d) = CONST 
    0x728: v728(0x4) = CONST 
    0x72b: v72b = CALLDATASIZE 
    0x72c: v72c = SUB v72b, v728(0x4)
    0x72d: v72d(0x40) = CONST 
    0x730: v730 = LT v72c, v72d(0x40)
    0x731: v731 = ISZERO v730
    0x732: v732(0x73a) = CONST 
    0x735: JUMPI v732(0x73a), v731

    Begin block 0x736
    prev=[0x724], succ=[]
    =================================
    0x736: v736(0x0) = CONST 
    0x739: REVERT v736(0x0), v736(0x0)

    Begin block 0x73a
    prev=[0x724], succ=[0x14b9]
    =================================
    0x73d: v73d = CALLDATALOAD v728(0x4)
    0x73f: v73f(0x20) = CONST 
    0x741: v741(0x24) = ADD v73f(0x20), v728(0x4)
    0x742: v742 = CALLDATALOAD v741(0x24)
    0x743: v743(0x14b9) = CONST 
    0x746: JUMP v743(0x14b9)

    Begin block 0x14b9
    prev=[0x73a], succ=[0x2b34B0x14b9]
    =================================
    0x14ba: v14ba(0x14c1) = CONST 
    0x14bd: v14bd(0x2b34) = CONST 
    0x14c0: JUMP v14bd(0x2b34)

    Begin block 0x2b34B0x14b9
    prev=[0x14b9], succ=[0x14c1]
    =================================
    0x2b35S0x14b9: v2b35V14b9 = NUMBER 
    0x2b36S0x14b9: v2b36V14b9(0x0) = CONST 
    0x2b3aS0x14b9: MSTORE v2b36V14b9(0x0), v2b35V14b9
    0x2b3bS0x14b9: v2b3bV14b9(0x20) = CONST 
    0x2b3fS0x14b9: MSTORE v2b3bV14b9(0x20), v2b36V14b9(0x0)
    0x2b40S0x14b9: v2b40V14b9(0x40) = CONST 
    0x2b44S0x14b9: v2b44V14b9 = SHA3 v2b36V14b9(0x0), v2b40V14b9(0x40)
    0x2b45S0x14b9: v2b45V14b9 = ORIGIN 
    0x2b47S0x14b9: MSTORE v2b36V14b9(0x0), v2b45V14b9
    0x2b4aS0x14b9: MSTORE v2b3bV14b9(0x20), v2b44V14b9
    0x2b4cS0x14b9: v2b4cV14b9 = SHA3 v2b36V14b9(0x0), v2b40V14b9(0x40)
    0x2b4dS0x14b9: v2b4dV14b9 = SLOAD v2b4cV14b9
    0x2b4eS0x14b9: v2b4eV14b9(0xff) = CONST 
    0x2b50S0x14b9: v2b50V14b9 = AND v2b4eV14b9(0xff), v2b4dV14b9
    0x2b52S0x14b9: JUMP v14ba(0x14c1)

    Begin block 0x14c1
    prev=[0x2b34B0x14b9], succ=[0x14c7, 0x1517]
    =================================
    0x14c2: v14c2 = ISZERO v2b50V14b9
    0x14c3: v14c3(0x1517) = CONST 
    0x14c6: JUMPI v14c3(0x1517), v14c2

    Begin block 0x14c7
    prev=[0x14c1], succ=[]
    =================================
    0x14c7: v14c7(0x40) = CONST 
    0x14c9: v14c9 = MLOAD v14c7(0x40)
    0x14ca: v14ca(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x14ec: MSTORE v14c9, v14ca(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x14ed: v14ed(0x4) = CONST 
    0x14ef: v14ef = ADD v14ed(0x4), v14c9
    0x14f2: v14f2(0x20) = CONST 
    0x14f4: v14f4 = ADD v14f2(0x20), v14ef
    0x14f7: v14f7(0x20) = SUB v14f4, v14ef
    0x14f9: MSTORE v14ef, v14f7(0x20)
    0x14fa: v14fa(0x26) = CONST 
    0x14fd: MSTORE v14f4, v14fa(0x26)
    0x14fe: v14fe(0x20) = CONST 
    0x1500: v1500 = ADD v14fe(0x20), v14f4
    0x1502: v1502(0x32b8) = CONST 
    0x1505: v1505(0x26) = CONST 
    0x1508: CODECOPY v1500, v1502(0x32b8), v1505(0x26)
    0x1509: v1509(0x40) = CONST 
    0x150b: v150b = ADD v1509(0x40), v1500
    0x150f: v150f(0x40) = CONST 
    0x1511: v1511 = MLOAD v150f(0x40)
    0x1514: v1514(0x84) = SUB v150b, v1511
    0x1516: REVERT v1511, v1514(0x84)

    Begin block 0x1517
    prev=[0x14c1], succ=[0x2b53B0x1517]
    =================================
    0x1518: v1518(0x151f) = CONST 
    0x151b: v151b(0x2b53) = CONST 
    0x151e: JUMP v151b(0x2b53)

    Begin block 0x2b53B0x1517
    prev=[0x1517], succ=[0x151f]
    =================================
    0x2b54S0x1517: v2b54V1517 = NUMBER 
    0x2b55S0x1517: v2b55V1517(0x0) = CONST 
    0x2b59S0x1517: MSTORE v2b55V1517(0x0), v2b54V1517
    0x2b5aS0x1517: v2b5aV1517(0x20) = CONST 
    0x2b5eS0x1517: MSTORE v2b5aV1517(0x20), v2b55V1517(0x0)
    0x2b5fS0x1517: v2b5fV1517(0x40) = CONST 
    0x2b63S0x1517: v2b63V1517 = SHA3 v2b55V1517(0x0), v2b5fV1517(0x40)
    0x2b64S0x1517: v2b64V1517 = CALLER 
    0x2b66S0x1517: MSTORE v2b55V1517(0x0), v2b64V1517
    0x2b69S0x1517: MSTORE v2b5aV1517(0x20), v2b63V1517
    0x2b6bS0x1517: v2b6bV1517 = SHA3 v2b55V1517(0x0), v2b5fV1517(0x40)
    0x2b6cS0x1517: v2b6cV1517 = SLOAD v2b6bV1517
    0x2b6dS0x1517: v2b6dV1517(0xff) = CONST 
    0x2b6fS0x1517: v2b6fV1517 = AND v2b6dV1517(0xff), v2b6cV1517
    0x2b71S0x1517: JUMP v1518(0x151f)

    Begin block 0x151f
    prev=[0x2b53B0x1517], succ=[0x1525, 0x1575]
    =================================
    0x1520: v1520 = ISZERO v2b6fV1517
    0x1521: v1521(0x1575) = CONST 
    0x1524: JUMPI v1521(0x1575), v1520

    Begin block 0x1525
    prev=[0x151f], succ=[]
    =================================
    0x1525: v1525(0x40) = CONST 
    0x1527: v1527 = MLOAD v1525(0x40)
    0x1528: v1528(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x154a: MSTORE v1527, v1528(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x154b: v154b(0x4) = CONST 
    0x154d: v154d = ADD v154b(0x4), v1527
    0x1550: v1550(0x20) = CONST 
    0x1552: v1552 = ADD v1550(0x20), v154d
    0x1555: v1555(0x20) = SUB v1552, v154d
    0x1557: MSTORE v154d, v1555(0x20)
    0x1558: v1558(0x26) = CONST 
    0x155b: MSTORE v1552, v1558(0x26)
    0x155c: v155c(0x20) = CONST 
    0x155e: v155e = ADD v155c(0x20), v1552
    0x1560: v1560(0x32b8) = CONST 
    0x1563: v1563(0x26) = CONST 
    0x1566: CODECOPY v155e, v1560(0x32b8), v1563(0x26)
    0x1567: v1567(0x40) = CONST 
    0x1569: v1569 = ADD v1567(0x40), v155e
    0x156d: v156d(0x40) = CONST 
    0x156f: v156f = MLOAD v156d(0x40)
    0x1572: v1572(0x84) = SUB v1569, v156f
    0x1574: REVERT v156f, v1572(0x84)

    Begin block 0x1575
    prev=[0x151f], succ=[0x157e, 0x15ce]
    =================================
    0x1576: v1576(0x0) = CONST 
    0x1579: v1579 = GT v73d, v1576(0x0)
    0x157a: v157a(0x15ce) = CONST 
    0x157d: JUMPI v157a(0x15ce), v1579

    Begin block 0x157e
    prev=[0x1575], succ=[]
    =================================
    0x157e: v157e(0x40) = CONST 
    0x1580: v1580 = MLOAD v157e(0x40)
    0x1581: v1581(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x15a3: MSTORE v1580, v1581(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x15a4: v15a4(0x4) = CONST 
    0x15a6: v15a6 = ADD v15a4(0x4), v1580
    0x15a9: v15a9(0x20) = CONST 
    0x15ab: v15ab = ADD v15a9(0x20), v15a6
    0x15ae: v15ae(0x20) = SUB v15ab, v15a6
    0x15b0: MSTORE v15a6, v15ae(0x20)
    0x15b1: v15b1(0x34) = CONST 
    0x15b4: MSTORE v15ab, v15b1(0x34)
    0x15b5: v15b5(0x20) = CONST 
    0x15b7: v15b7 = ADD v15b5(0x20), v15ab
    0x15b9: v15b9(0x30e9) = CONST 
    0x15bc: v15bc(0x34) = CONST 
    0x15bf: CODECOPY v15b7, v15b9(0x30e9), v15bc(0x34)
    0x15c0: v15c0(0x40) = CONST 
    0x15c2: v15c2 = ADD v15c0(0x40), v15b7
    0x15c6: v15c6(0x40) = CONST 
    0x15c8: v15c8 = MLOAD v15c6(0x40)
    0x15cb: v15cb(0x84) = SUB v15c2, v15c8
    0x15cd: REVERT v15c8, v15cb(0x84)

    Begin block 0x15ce
    prev=[0x1575], succ=[0x15d8]
    =================================
    0x15cf: v15cf(0x0) = CONST 
    0x15d1: v15d1(0x15d8) = CONST 
    0x15d4: v15d4(0x266f) = CONST 
    0x15d7: v15d7_0 = CALLPRIVATE v15d4(0x266f), v15d1(0x15d8)

    Begin block 0x15d8
    prev=[0x15ce], succ=[0x15e2, 0x1648]
    =================================
    0x15dd: v15dd = EQ v15d7_0, v742
    0x15de: v15de(0x1648) = CONST 
    0x15e1: JUMPI v15de(0x1648), v15dd

    Begin block 0x15e2
    prev=[0x15d8], succ=[]
    =================================
    0x15e2: v15e2(0x40) = CONST 
    0x15e5: v15e5 = MLOAD v15e2(0x40)
    0x15e6: v15e6(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1608: MSTORE v15e5, v15e6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1609: v1609(0x20) = CONST 
    0x160b: v160b(0x4) = CONST 
    0x160e: v160e = ADD v15e5, v160b(0x4)
    0x160f: MSTORE v160e, v1609(0x20)
    0x1610: v1610(0x1e) = CONST 
    0x1612: v1612(0x24) = CONST 
    0x1615: v1615 = ADD v15e5, v1612(0x24)
    0x1616: MSTORE v1615, v1610(0x1e)
    0x1617: v1617(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000) = CONST 
    0x1638: v1638(0x44) = CONST 
    0x163b: v163b = ADD v15e5, v1638(0x44)
    0x163c: MSTORE v163b, v1617(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000)
    0x163e: v163e = MLOAD v15e2(0x40)
    0x1642: v1642(0x0) = SUB v15e5, v163e
    0x1643: v1643(0x64) = CONST 
    0x1645: v1645(0x64) = ADD v1643(0x64), v1642(0x0)
    0x1647: REVERT v163e, v1645(0x64)

    Begin block 0x1648
    prev=[0x15d8], succ=[0x1658, 0x16a8]
    =================================
    0x1649: v1649(0xde0b6b3a7640000) = CONST 
    0x1653: v1653 = LT v15d7_0, v1649(0xde0b6b3a7640000)
    0x1654: v1654(0x16a8) = CONST 
    0x1657: JUMPI v1654(0x16a8), v1653

    Begin block 0x1658
    prev=[0x1648], succ=[]
    =================================
    0x1658: v1658(0x40) = CONST 
    0x165a: v165a = MLOAD v1658(0x40)
    0x165b: v165b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x167d: MSTORE v165a, v165b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x167e: v167e(0x4) = CONST 
    0x1680: v1680 = ADD v167e(0x4), v165a
    0x1683: v1683(0x20) = CONST 
    0x1685: v1685 = ADD v1683(0x20), v1680
    0x1688: v1688(0x20) = SUB v1685, v1680
    0x168a: MSTORE v1680, v1688(0x20)
    0x168b: v168b(0x38) = CONST 
    0x168e: MSTORE v1685, v168b(0x38)
    0x168f: v168f(0x20) = CONST 
    0x1691: v1691 = ADD v168f(0x20), v1685
    0x1693: v1693(0x3145) = CONST 
    0x1696: v1696(0x38) = CONST 
    0x1699: CODECOPY v1691, v1693(0x3145), v1696(0x38)
    0x169a: v169a(0x40) = CONST 
    0x169c: v169c = ADD v169a(0x40), v1691
    0x16a0: v16a0(0x40) = CONST 
    0x16a2: v16a2 = MLOAD v16a0(0x40)
    0x16a5: v16a5(0x84) = SUB v169c, v16a2
    0x16a7: REVERT v16a2, v16a5(0x84)

    Begin block 0x16a8
    prev=[0x1648], succ=[0x16b2]
    =================================
    0x16a9: v16a9(0x0) = CONST 
    0x16ab: v16ab(0x16b2) = CONST 
    0x16ae: v16ae(0x1cfd) = CONST 
    0x16b1: v16b1_0 = CALLPRIVATE v16ae(0x1cfd), v16ab(0x16b2)

    Begin block 0x16b2
    prev=[0x16a8], succ=[0x16bd, 0x170d]
    =================================
    0x16b7: v16b7 = GT v73d, v16b1_0
    0x16b8: v16b8 = ISZERO v16b7
    0x16b9: v16b9(0x170d) = CONST 
    0x16bc: JUMPI v16b9(0x170d), v16b8

    Begin block 0x16bd
    prev=[0x16b2], succ=[]
    =================================
    0x16bd: v16bd(0x40) = CONST 
    0x16bf: v16bf = MLOAD v16bd(0x40)
    0x16c0: v16c0(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x16e2: MSTORE v16bf, v16c0(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x16e3: v16e3(0x4) = CONST 
    0x16e5: v16e5 = ADD v16e3(0x4), v16bf
    0x16e8: v16e8(0x20) = CONST 
    0x16ea: v16ea = ADD v16e8(0x20), v16e5
    0x16ed: v16ed(0x20) = SUB v16ea, v16e5
    0x16ef: MSTORE v16e5, v16ed(0x20)
    0x16f0: v16f0(0x2e) = CONST 
    0x16f3: MSTORE v16ea, v16f0(0x2e)
    0x16f4: v16f4(0x20) = CONST 
    0x16f6: v16f6 = ADD v16f4(0x20), v16ea
    0x16f8: v16f8(0x3260) = CONST 
    0x16fb: v16fb(0x2e) = CONST 
    0x16fe: CODECOPY v16f6, v16f8(0x3260), v16fb(0x2e)
    0x16ff: v16ff(0x40) = CONST 
    0x1701: v1701 = ADD v16ff(0x40), v16f6
    0x1705: v1705(0x40) = CONST 
    0x1707: v1707 = MLOAD v1705(0x40)
    0x170a: v170a(0x84) = SUB v1701, v1707
    0x170c: REVERT v1707, v170a(0x84)

    Begin block 0x170d
    prev=[0x16b2], succ=[0x1717]
    =================================
    0x170e: v170e(0x0) = CONST 
    0x1710: v1710(0x1717) = CONST 
    0x1713: v1713(0x2780) = CONST 
    0x1716: v1716_0 = CALLPRIVATE v1713(0x2780), v1710(0x1717)

    Begin block 0x1717
    prev=[0x170d], succ=[0x1722, 0x1788]
    =================================
    0x171a: v171a(0x0) = CONST 
    0x171d: v171d = GT v1716_0, v171a(0x0)
    0x171e: v171e(0x1788) = CONST 
    0x1721: JUMPI v171e(0x1788), v171d

    Begin block 0x1722
    prev=[0x1717], succ=[]
    =================================
    0x1722: v1722(0x40) = CONST 
    0x1725: v1725 = MLOAD v1722(0x40)
    0x1726: v1726(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1748: MSTORE v1725, v1726(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1749: v1749(0x20) = CONST 
    0x174b: v174b(0x4) = CONST 
    0x174e: v174e = ADD v1725, v174b(0x4)
    0x174f: MSTORE v174e, v1749(0x20)
    0x1750: v1750(0x1f) = CONST 
    0x1752: v1752(0x24) = CONST 
    0x1755: v1755 = ADD v1725, v1752(0x24)
    0x1756: MSTORE v1755, v1750(0x1f)
    0x1757: v1757(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500) = CONST 
    0x1778: v1778(0x44) = CONST 
    0x177b: v177b = ADD v1725, v1778(0x44)
    0x177c: MSTORE v177b, v1757(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500)
    0x177e: v177e = MLOAD v1722(0x40)
    0x1782: v1782(0x0) = SUB v1725, v177e
    0x1783: v1783(0x64) = CONST 
    0x1785: v1785(0x64) = ADD v1783(0x64), v1782(0x0)
    0x1787: REVERT v177e, v1785(0x64)

    Begin block 0x1788
    prev=[0x1717], succ=[0x3e1b]
    =================================
    0x1789: v1789(0x0) = CONST 
    0x178b: v178b(0x17a0) = CONST 
    0x178e: v178e(0xde0b6b3a7640000) = CONST 
    0x1797: v1797(0x3e1b) = CONST 
    0x179c: v179c(0x29f2) = CONST 
    0x179f: v179f_0 = CALLPRIVATE v179c(0x29f2), v1716_0, v73d, v1797(0x3e1b)

    Begin block 0x3e1b
    prev=[0x1788], succ=[0x17a0]
    =================================
    0x3e1d: v3e1d(0x2a65) = CONST 
    0x3e20: v3e20_0 = CALLPRIVATE v3e1d(0x2a65), v178e(0xde0b6b3a7640000), v179f_0, v178b(0x17a0)

    Begin block 0x17a0
    prev=[0x3e1b], succ=[0x29b0B0x17a0]
    =================================
    0x17a1: v17a1(0x6) = CONST 
    0x17a3: v17a3 = SLOAD v17a1(0x6)
    0x17a7: v17a7(0x17b0) = CONST 
    0x17ac: v17ac(0x29b0) = CONST 
    0x17af: JUMP v17ac(0x29b0)

    Begin block 0x29b0B0x17a0
    prev=[0x17a0], succ=[0x29a70x29b0B0x17a0]
    =================================
    0x29b1S0x17a0: v29b1V17a0(0x0) = CONST 
    0x29b3S0x17a0: v29b3V17a0(0x29a7) = CONST 
    0x29b8S0x17a0: v29b8V17a0(0x40) = CONST 
    0x29baS0x17a0: v29baV17a0 = MLOAD v29b8V17a0(0x40)
    0x29bcS0x17a0: v29bcV17a0(0x40) = CONST 
    0x29beS0x17a0: v29beV17a0 = ADD v29bcV17a0(0x40), v29baV17a0
    0x29bfS0x17a0: v29bfV17a0(0x40) = CONST 
    0x29c1S0x17a0: MSTORE v29bfV17a0(0x40), v29beV17a0
    0x29c3S0x17a0: v29c3V17a0(0x1e) = CONST 
    0x29c6S0x17a0: MSTORE v29baV17a0, v29c3V17a0(0x1e)
    0x29c7S0x17a0: v29c7V17a0(0x20) = CONST 
    0x29c9S0x17a0: v29c9V17a0 = ADD v29c7V17a0(0x20), v29baV17a0
    0x29caS0x17a0: v29caV17a0(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x17a0: MSTORE v29c9V17a0, v29caV17a0(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x17a0: v29eeV17a0(0x2bef) = CONST 
    0x29f1S0x17a0: v29f1_0V17a0 = CALLPRIVATE v29eeV17a0(0x2bef), v29baV17a0, v3e20_0, v17a3, v29b3V17a0(0x29a7)

    Begin block 0x29a70x29b0B0x17a0
    prev=[0x29b0B0x17a0], succ=[0x29aa0x29b0B0x17a0]
    =================================

    Begin block 0x29aa0x29b0B0x17a0
    prev=[0x29a70x29b0B0x17a0], succ=[0x17b0]
    =================================
    0x29af0x29b0S0x17a0: JUMP v17a7(0x17b0)

    Begin block 0x17b0
    prev=[0x29aa0x29b0B0x17a0], succ=[0x17c0]
    =================================
    0x17b1: v17b1(0x6) = CONST 
    0x17b3: SSTORE v17b1(0x6), v29f1_0V17a0
    0x17b4: v17b4(0x7) = CONST 
    0x17b6: v17b6 = SLOAD v17b4(0x7)
    0x17b7: v17b7(0x17c0) = CONST 
    0x17bc: v17bc(0x2933) = CONST 
    0x17bf: v17bf_0 = CALLPRIVATE v17bc(0x2933), v3e20_0, v17b6, v17b7(0x17c0)

    Begin block 0x17c0
    prev=[0x17b0], succ=[0x17cd]
    =================================
    0x17c1: v17c1(0x7) = CONST 
    0x17c3: SSTORE v17c1(0x7), v17bf_0
    0x17c4: v17c4(0x0) = CONST 
    0x17c6: v17c6(0x17cd) = CONST 
    0x17c9: v17c9(0x1c11) = CONST 
    0x17cc: v17cc_0 = CALLPRIVATE v17c9(0x1c11), v17c6(0x17cd)

    Begin block 0x17cd
    prev=[0x17c0], succ=[0x1846, 0x184a]
    =================================
    0x17ce: v17ce(0x2) = CONST 
    0x17d0: v17d0 = SLOAD v17ce(0x2)
    0x17d1: v17d1(0x40) = CONST 
    0x17d4: v17d4 = MLOAD v17d1(0x40)
    0x17d5: v17d5(0x79cc679000000000000000000000000000000000000000000000000000000000) = CONST 
    0x17f7: MSTORE v17d4, v17d5(0x79cc679000000000000000000000000000000000000000000000000000000000)
    0x17f8: v17f8 = CALLER 
    0x17f9: v17f9(0x4) = CONST 
    0x17fc: v17fc = ADD v17d4, v17f9(0x4)
    0x17fd: MSTORE v17fc, v17f8
    0x17fe: v17fe(0x24) = CONST 
    0x1801: v1801 = ADD v17d4, v17fe(0x24)
    0x1804: MSTORE v1801, v73d
    0x1806: v1806 = MLOAD v17d1(0x40)
    0x180a: v180a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1821: v1821 = AND v17d0, v180a(0xffffffffffffffffffffffffffffffffffffffff)
    0x1825: v1825(0x79cc6790) = CONST 
    0x182b: v182b(0x44) = CONST 
    0x182f: v182f = ADD v17d4, v182b(0x44)
    0x1831: v1831(0x0) = CONST 
    0x1838: v1838(0x0) = SUB v17d4, v1806
    0x1839: v1839(0x44) = ADD v1838(0x0), v182b(0x44)
    0x183e: v183e = EXTCODESIZE v1821
    0x183f: v183f = ISZERO v183e
    0x1841: v1841 = ISZERO v183f
    0x1842: v1842(0x184a) = CONST 
    0x1845: JUMPI v1842(0x184a), v1841

    Begin block 0x1846
    prev=[0x17cd], succ=[]
    =================================
    0x1846: v1846(0x0) = CONST 
    0x1849: REVERT v1846(0x0), v1846(0x0)

    Begin block 0x184a
    prev=[0x17cd], succ=[0x1855, 0x185e]
    =================================
    0x184c: v184c = GAS 
    0x184d: v184d = CALL v184c, v1821, v1831(0x0), v1806, v1839(0x44), v1806, v1831(0x0)
    0x184e: v184e = ISZERO v184d
    0x1850: v1850 = ISZERO v184e
    0x1851: v1851(0x185e) = CONST 
    0x1854: JUMPI v1851(0x185e), v1850

    Begin block 0x1855
    prev=[0x184a], succ=[]
    =================================
    0x1855: v1855 = RETURNDATASIZE 
    0x1856: v1856(0x0) = CONST 
    0x1859: RETURNDATACOPY v1856(0x0), v1856(0x0), v1855
    0x185a: v185a = RETURNDATASIZE 
    0x185b: v185b(0x0) = CONST 
    0x185d: REVERT v185b(0x0), v185a

    Begin block 0x185e
    prev=[0x184a], succ=[0x1888]
    =================================
    0x1861: v1861 = CALLER 
    0x1862: v1862(0x0) = CONST 
    0x1866: MSTORE v1862(0x0), v1861
    0x1867: v1867(0xe) = CONST 
    0x1869: v1869(0x20) = CONST 
    0x186d: MSTORE v1869(0x20), v1867(0xe)
    0x186e: v186e(0x40) = CONST 
    0x1872: v1872 = SHA3 v1862(0x0), v186e(0x40)
    0x1875: MSTORE v1862(0x0), v17cc_0
    0x1878: MSTORE v1869(0x20), v1872
    0x187a: v187a = SHA3 v1862(0x0), v186e(0x40)
    0x187b: v187b = SLOAD v187a
    0x187c: v187c(0x1888) = CONST 
    0x1884: v1884(0x2933) = CONST 
    0x1887: v1887_0 = CALLPRIVATE v1884(0x2933), v3e20_0, v187b, v187c(0x1888)

    Begin block 0x1888
    prev=[0x185e], succ=[0x18ba]
    =================================
    0x1889: v1889 = CALLER 
    0x188a: v188a(0x0) = CONST 
    0x188e: MSTORE v188a(0x0), v1889
    0x188f: v188f(0xe) = CONST 
    0x1891: v1891(0x20) = CONST 
    0x1895: MSTORE v1891(0x20), v188f(0xe)
    0x1896: v1896(0x40) = CONST 
    0x189a: v189a = SHA3 v188a(0x0), v1896(0x40)
    0x189d: MSTORE v188a(0x0), v17cc_0
    0x189f: MSTORE v1891(0x20), v189a
    0x18a2: v18a2 = SHA3 v188a(0x0), v1896(0x40)
    0x18a6: SSTORE v18a2, v1887_0
    0x18a9: MSTORE v188a(0x0), v1889
    0x18aa: v18aa(0x12) = CONST 
    0x18ae: MSTORE v1891(0x20), v18aa(0x12)
    0x18af: v18af = SHA3 v188a(0x0), v1896(0x40)
    0x18b0: v18b0 = SLOAD v18af
    0x18b1: v18b1(0x18ba) = CONST 
    0x18b6: v18b6(0x2933) = CONST 
    0x18b9: v18b9_0 = CALLPRIVATE v18b6(0x2933), v3e20_0, v18b0, v18b1(0x18ba)

    Begin block 0x18ba
    prev=[0x1888], succ=[0x18d7]
    =================================
    0x18bb: v18bb = CALLER 
    0x18bc: v18bc(0x0) = CONST 
    0x18c0: MSTORE v18bc(0x0), v18bb
    0x18c1: v18c1(0x12) = CONST 
    0x18c3: v18c3(0x20) = CONST 
    0x18c5: MSTORE v18c3(0x20), v18c1(0x12)
    0x18c6: v18c6(0x40) = CONST 
    0x18c9: v18c9 = SHA3 v18bc(0x0), v18c6(0x40)
    0x18ca: SSTORE v18c9, v18b9_0
    0x18cb: v18cb(0x11) = CONST 
    0x18cd: v18cd = SLOAD v18cb(0x11)
    0x18ce: v18ce(0x18d7) = CONST 
    0x18d3: v18d3(0x2933) = CONST 
    0x18d6: v18d6_0 = CALLPRIVATE v18d3(0x2933), v3e20_0, v18cd, v18ce(0x18d7)

    Begin block 0x18d7
    prev=[0x18ba], succ=[0x18e3, 0x19a2]
    =================================
    0x18d8: v18d8(0x11) = CONST 
    0x18da: SSTORE v18d8(0x11), v18d6_0
    0x18db: v18db(0x13) = CONST 
    0x18dd: v18dd = SLOAD v18db(0x13)
    0x18de: v18de = ISZERO v18dd
    0x18df: v18df(0x19a2) = CONST 
    0x18e2: JUMPI v18df(0x19a2), v18de

    Begin block 0x18e3
    prev=[0x18d7], succ=[0x18f2, 0x18f3]
    =================================
    0x18e3: v18e3(0x0) = CONST 
    0x18e5: v18e5(0x2710) = CONST 
    0x18e8: v18e8(0x13) = CONST 
    0x18ea: v18ea = SLOAD v18e8(0x13)
    0x18ec: v18ec = MUL v73d, v18ea
    0x18ee: v18ee(0x18f3) = CONST 
    0x18f1: JUMPI v18ee(0x18f3), v18e5(0x2710)

    Begin block 0x18f2
    prev=[0x18e3], succ=[]
    =================================
    0x18f2: THROW 

    Begin block 0x18f3
    prev=[0x18e3], succ=[0x1970, 0x1974]
    =================================
    0x18f4: v18f4(0x3) = CONST 
    0x18f6: v18f6 = SLOAD v18f4(0x3)
    0x18f7: v18f7(0x40) = CONST 
    0x18fa: v18fa = MLOAD v18f7(0x40)
    0x18fb: v18fb(0x40c10f1900000000000000000000000000000000000000000000000000000000) = CONST 
    0x191d: MSTORE v18fa, v18fb(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0x191e: v191e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1935: v1935 = AND v191e(0xffffffffffffffffffffffffffffffffffffffff), v18f6
    0x1936: v1936(0x4) = CONST 
    0x1939: v1939 = ADD v18fa, v1936(0x4)
    0x193a: MSTORE v1939, v1935
    0x193e: v193e = DIV v18ec, v18e5(0x2710)
    0x193f: v193f(0x24) = CONST 
    0x1942: v1942 = ADD v18fa, v193f(0x24)
    0x1945: MSTORE v1942, v193e
    0x1947: v1947 = MLOAD v18f7(0x40)
    0x194c: v194c = AND v1821, v191e(0xffffffffffffffffffffffffffffffffffffffff)
    0x194e: v194e(0x40c10f19) = CONST 
    0x1954: v1954(0x44) = CONST 
    0x1958: v1958 = ADD v18fa, v1954(0x44)
    0x195a: v195a(0x20) = CONST 
    0x1961: v1961(0x0) = SUB v18fa, v1947
    0x1962: v1962(0x44) = ADD v1961(0x0), v1954(0x44)
    0x1964: v1964(0x0) = CONST 
    0x1968: v1968 = EXTCODESIZE v194c
    0x1969: v1969 = ISZERO v1968
    0x196b: v196b = ISZERO v1969
    0x196c: v196c(0x1974) = CONST 
    0x196f: JUMPI v196c(0x1974), v196b

    Begin block 0x1970
    prev=[0x18f3], succ=[]
    =================================
    0x1970: v1970(0x0) = CONST 
    0x1973: REVERT v1970(0x0), v1970(0x0)

    Begin block 0x1974
    prev=[0x18f3], succ=[0x197f, 0x1988]
    =================================
    0x1976: v1976 = GAS 
    0x1977: v1977 = CALL v1976, v194c, v1964(0x0), v1947, v1962(0x44), v1947, v195a(0x20)
    0x1978: v1978 = ISZERO v1977
    0x197a: v197a = ISZERO v1978
    0x197b: v197b(0x1988) = CONST 
    0x197e: JUMPI v197b(0x1988), v197a

    Begin block 0x197f
    prev=[0x1974], succ=[]
    =================================
    0x197f: v197f = RETURNDATASIZE 
    0x1980: v1980(0x0) = CONST 
    0x1983: RETURNDATACOPY v1980(0x0), v1980(0x0), v197f
    0x1984: v1984 = RETURNDATASIZE 
    0x1985: v1985(0x0) = CONST 
    0x1987: REVERT v1985(0x0), v1984

    Begin block 0x1988
    prev=[0x1974], succ=[0x199a, 0x199e]
    =================================
    0x198d: v198d(0x40) = CONST 
    0x198f: v198f = MLOAD v198d(0x40)
    0x1990: v1990 = RETURNDATASIZE 
    0x1991: v1991(0x20) = CONST 
    0x1994: v1994 = LT v1990, v1991(0x20)
    0x1995: v1995 = ISZERO v1994
    0x1996: v1996(0x199e) = CONST 
    0x1999: JUMPI v1996(0x199e), v1995

    Begin block 0x199a
    prev=[0x1988], succ=[]
    =================================
    0x199a: v199a(0x0) = CONST 
    0x199d: REVERT v199a(0x0), v199a(0x0)

    Begin block 0x199e
    prev=[0x1988], succ=[0x19a2]
    =================================

    Begin block 0x19a2
    prev=[0x18d7, 0x199e], succ=[0x1a07, 0x19ba]
    =================================
    0x19a3: v19a3 = CALLER 
    0x19a4: v19a4(0x0) = CONST 
    0x19a8: MSTORE v19a4(0x0), v19a3
    0x19a9: v19a9(0xf) = CONST 
    0x19ab: v19ab(0x20) = CONST 
    0x19ad: MSTORE v19ab(0x20), v19a9(0xf)
    0x19ae: v19ae(0x40) = CONST 
    0x19b1: v19b1 = SHA3 v19a4(0x0), v19ae(0x40)
    0x19b2: v19b2 = SLOAD v19b1
    0x19b4: v19b4 = ISZERO v19b2
    0x19b6: v19b6(0x1a07) = CONST 
    0x19b9: JUMPI v19b6(0x1a07), v19b4

    Begin block 0x1a07
    prev=[0x19a2, 0x19fa], succ=[0x1a0d, 0x1a2f]
    =================================
    0x1a07_0x0: v1a07_0 = PHI v19b4, v1a06
    0x1a08: v1a08 = ISZERO v1a07_0
    0x1a09: v1a09(0x1a2f) = CONST 
    0x1a0c: JUMPI v1a09(0x1a2f), v1a08

    Begin block 0x1a0d
    prev=[0x1a07], succ=[0x1a2f]
    =================================
    0x1a0d: v1a0d = CALLER 
    0x1a0e: v1a0e(0x0) = CONST 
    0x1a12: MSTORE v1a0e(0x0), v1a0d
    0x1a13: v1a13(0xf) = CONST 
    0x1a15: v1a15(0x20) = CONST 
    0x1a19: MSTORE v1a15(0x20), v1a13(0xf)
    0x1a1a: v1a1a(0x40) = CONST 
    0x1a1d: v1a1d = SHA3 v1a0e(0x0), v1a1a(0x40)
    0x1a1f: v1a1f = SLOAD v1a1d
    0x1a20: v1a20(0x1) = CONST 
    0x1a23: v1a23 = ADD v1a1f, v1a20(0x1)
    0x1a25: SSTORE v1a1d, v1a23
    0x1a28: MSTORE v1a0e(0x0), v1a1d
    0x1a2a: v1a2a = SHA3 v1a0e(0x0), v1a15(0x20)
    0x1a2b: v1a2b = ADD v1a2a, v1a1f
    0x1a2e: SSTORE v1a2b, v17cc_0

    Begin block 0x1a2f
    prev=[0x1a0d, 0x1a07], succ=[0x1a37]
    =================================
    0x1a30: v1a30(0x1a37) = CONST 
    0x1a33: v1a33(0x2b72) = CONST 
    0x1a36: CALLPRIVATE v1a33(0x2b72), v1a30(0x1a37)

    Begin block 0x1a37
    prev=[0x1a2f], succ=[0x37d0x724]
    =================================
    0x1a38: v1a38 = CALLER 
    0x1a39: v1a39(0x0) = CONST 
    0x1a3d: MSTORE v1a39(0x0), v1a38
    0x1a3e: v1a3e(0xe) = CONST 
    0x1a40: v1a40(0x20) = CONST 
    0x1a44: MSTORE v1a40(0x20), v1a3e(0xe)
    0x1a45: v1a45(0x40) = CONST 
    0x1a49: v1a49 = SHA3 v1a39(0x0), v1a45(0x40)
    0x1a4c: MSTORE v1a39(0x0), v17cc_0
    0x1a4e: MSTORE v1a40(0x20), v1a49
    0x1a52: v1a52 = SHA3 v1a39(0x0), v1a45(0x40)
    0x1a53: v1a53 = SLOAD v1a52
    0x1a55: v1a55 = MLOAD v1a45(0x40)
    0x1a58: MSTORE v1a55, v17cc_0
    0x1a5b: v1a5b = ADD v1a55, v1a40(0x20)
    0x1a5e: MSTORE v1a5b, v73d
    0x1a61: v1a61 = ADD v1a45(0x40), v1a55
    0x1a62: MSTORE v1a61, v1a53
    0x1a64: v1a64 = MLOAD v1a45(0x40)
    0x1a65: v1a65(0x523040e57210c2af3b7a61d17ba47d377066ed7c71d1847477197fae677b9814) = CONST 
    0x1a89: v1a89(0x0) = SUB v1a55, v1a64
    0x1a8a: v1a8a(0x60) = CONST 
    0x1a8c: v1a8c(0x60) = ADD v1a8a(0x60), v1a89(0x0)
    0x1a8e: LOG2 v1a64, v1a8c(0x60), v1a65(0x523040e57210c2af3b7a61d17ba47d377066ed7c71d1847477197fae677b9814), v1a38
    0x1a91: v1a91 = NUMBER 
    0x1a92: v1a92(0x0) = CONST 
    0x1a96: MSTORE v1a92(0x0), v1a91
    0x1a97: v1a97(0x20) = CONST 
    0x1a9b: MSTORE v1a97(0x20), v1a92(0x0)
    0x1a9c: v1a9c(0x40) = CONST 
    0x1aa0: v1aa0 = SHA3 v1a92(0x0), v1a9c(0x40)
    0x1aa1: v1aa1 = ORIGIN 
    0x1aa3: MSTORE v1a92(0x0), v1aa1
    0x1aa6: MSTORE v1a97(0x20), v1aa0
    0x1aa9: v1aa9 = SHA3 v1a92(0x0), v1a9c(0x40)
    0x1aab: v1aab = SLOAD v1aa9
    0x1aac: v1aac(0x1) = CONST 
    0x1aae: v1aae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x1ad1: v1ad1 = AND v1aae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1aab
    0x1ad3: v1ad3 = OR v1aac(0x1), v1ad1
    0x1ad6: SSTORE v1aa9, v1ad3
    0x1ad7: v1ad7 = CALLER 
    0x1ad9: MSTORE v1a92(0x0), v1ad7
    0x1add: v1add = SHA3 v1a92(0x0), v1a9c(0x40)
    0x1adf: v1adf = SLOAD v1add
    0x1ae2: v1ae2 = AND v1aae(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1adf
    0x1ae5: v1ae5 = OR v1aac(0x1), v1ae2
    0x1ae7: SSTORE v1add, v1ae5
    0x1aef: JUMP v725(0x37d)

    Begin block 0x37d0x724
    prev=[0x1a37], succ=[]
    =================================
    0x37e0x724: STOP 

    Begin block 0x19ba
    prev=[0x19a2], succ=[0x19f9, 0x19fa]
    =================================
    0x19bb: v19bb = CALLER 
    0x19bc: v19bc(0x0) = CONST 
    0x19c0: MSTORE v19bc(0x0), v19bb
    0x19c1: v19c1(0xf) = CONST 
    0x19c3: v19c3(0x20) = CONST 
    0x19c5: MSTORE v19c3(0x20), v19c1(0xf)
    0x19c6: v19c6(0x40) = CONST 
    0x19c9: v19c9 = SHA3 v19bc(0x0), v19c6(0x40)
    0x19cb: v19cb = SLOAD v19c9
    0x19cf: v19cf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19f1: v19f1 = ADD v19b2, v19cf(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x19f4: v19f4 = LT v19f1, v19cb
    0x19f5: v19f5(0x19fa) = CONST 
    0x19f8: JUMPI v19f5(0x19fa), v19f4

    Begin block 0x19f9
    prev=[0x19ba], succ=[]
    =================================
    0x19f9: THROW 

    Begin block 0x19fa
    prev=[0x19ba], succ=[0x1a07]
    =================================
    0x19fc: v19fc(0x0) = CONST 
    0x19fe: MSTORE v19fc(0x0), v19c9
    0x19ff: v19ff(0x20) = CONST 
    0x1a01: v1a01(0x0) = CONST 
    0x1a03: v1a03 = SHA3 v1a01(0x0), v19ff(0x20)
    0x1a04: v1a04 = ADD v1a03, v19f1
    0x1a05: v1a05 = SLOAD v1a04
    0x1a06: v1a06 = LT v1a05, v17cc_0

}

function getRedeemableCoupons()() public {
    Begin block 0x747
    prev=[], succ=[0x34e0x747]
    =================================
    0x748: v748(0x34e) = CONST 
    0x74b: v74b(0x1af0) = CONST 
    0x74e: v74e_0 = CALLPRIVATE v74b(0x1af0), v748(0x34e)

    Begin block 0x34e0x747
    prev=[0x747], succ=[]
    =================================
    0x34f0x747: v74734f(0x40) = CONST 
    0x3520x747: v747352 = MLOAD v74734f(0x40)
    0x3550x747: MSTORE v747352, v74e_0
    0x3560x747: v747356 = MLOAD v74734f(0x40)
    0x35a0x747: v74735a(0x0) = SUB v747352, v747356
    0x35b0x747: v74735b(0x20) = CONST 
    0x35d0x747: v74735d(0x20) = ADD v74735b(0x20), v74735a(0x0)
    0x35f0x747: RETURN v747356, v74735d(0x20)

}

function sideToken()() public {
    Begin block 0x74f
    prev=[], succ=[0x1bf5]
    =================================
    0x750: v750(0x3a1c) = CONST 
    0x753: v753(0x1bf5) = CONST 
    0x756: JUMP v753(0x1bf5)

    Begin block 0x1bf5
    prev=[0x74f], succ=[0x3a1c]
    =================================
    0x1bf6: v1bf6(0x5) = CONST 
    0x1bf8: v1bf8 = SLOAD v1bf6(0x5)
    0x1bf9: v1bf9(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c0e: v1c0e = AND v1bf9(0xffffffffffffffffffffffffffffffffffffffff), v1bf8
    0x1c10: JUMP v750(0x3a1c)

    Begin block 0x3a1c
    prev=[0x1bf5], succ=[]
    =================================
    0x3a1d: v3a1d(0x40) = CONST 
    0x3a20: v3a20 = MLOAD v3a1d(0x40)
    0x3a21: v3a21(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a38: v3a38 = AND v1c0e, v3a21(0xffffffffffffffffffffffffffffffffffffffff)
    0x3a3a: MSTORE v3a20, v3a38
    0x3a3b: v3a3b = MLOAD v3a1d(0x40)
    0x3a3f: v3a3f(0x0) = SUB v3a20, v3a3b
    0x3a40: v3a40(0x20) = CONST 
    0x3a42: v3a42(0x20) = ADD v3a40(0x20), v3a3f(0x0)
    0x3a44: RETURN v3a3b, v3a42(0x20)

}

function epoch()() public {
    Begin block 0x757
    prev=[], succ=[0x3a64]
    =================================
    0x758: v758(0x3a64) = CONST 
    0x75b: v75b(0x1c11) = CONST 
    0x75e: v75e_0 = CALLPRIVATE v75b(0x1c11), v758(0x3a64)

    Begin block 0x3a64
    prev=[0x757], succ=[]
    =================================
    0x3a65: v3a65(0x40) = CONST 
    0x3a68: v3a68 = MLOAD v3a65(0x40)
    0x3a6b: MSTORE v3a68, v75e_0
    0x3a6c: v3a6c = MLOAD v3a65(0x40)
    0x3a70: v3a70(0x0) = SUB v3a68, v3a6c
    0x3a71: v3a71(0x20) = CONST 
    0x3a73: v3a73(0x20) = ADD v3a71(0x20), v3a70(0x0)
    0x3a75: RETURN v3a6c, v3a73(0x20)

}

function dollarPriceOne()() public {
    Begin block 0x75f
    prev=[], succ=[0x1c7c]
    =================================
    0x760: v760(0x3a95) = CONST 
    0x763: v763(0x1c7c) = CONST 
    0x766: JUMP v763(0x1c7c)

    Begin block 0x1c7c
    prev=[0x75f], succ=[0x3a95]
    =================================
    0x1c7d: v1c7d(0xde0b6b3a7640000) = CONST 
    0x1c87: JUMP v760(0x3a95)

    Begin block 0x3a95
    prev=[0x1c7c], succ=[]
    =================================
    0x3a96: v3a96(0x40) = CONST 
    0x3a99: v3a99 = MLOAD v3a96(0x40)
    0x3a9c: MSTORE v3a99, v1c7d(0xde0b6b3a7640000)
    0x3a9d: v3a9d = MLOAD v3a96(0x40)
    0x3aa1: v3aa1(0x0) = SUB v3a99, v3a9d
    0x3aa2: v3aa2(0x20) = CONST 
    0x3aa4: v3aa4(0x20) = ADD v3aa2(0x20), v3aa1(0x0)
    0x3aa6: RETURN v3a9d, v3aa4(0x20)

}

function setMaxDiscountRate(uint256)() public {
    Begin block 0x767
    prev=[], succ=[0x779, 0x77d]
    =================================
    0x768: v768(0x3ac6) = CONST 
    0x76b: v76b(0x4) = CONST 
    0x76e: v76e = CALLDATASIZE 
    0x76f: v76f = SUB v76e, v76b(0x4)
    0x770: v770(0x20) = CONST 
    0x773: v773 = LT v76f, v770(0x20)
    0x774: v774 = ISZERO v773
    0x775: v775(0x77d) = CONST 
    0x778: JUMPI v775(0x77d), v774

    Begin block 0x779
    prev=[0x767], succ=[]
    =================================
    0x779: v779(0x0) = CONST 
    0x77c: REVERT v779(0x0), v779(0x0)

    Begin block 0x77d
    prev=[0x767], succ=[0x1c88]
    =================================
    0x77f: v77f = CALLDATALOAD v76b(0x4)
    0x780: v780(0x1c88) = CONST 
    0x783: JUMP v780(0x1c88)

    Begin block 0x1c88
    prev=[0x77d], succ=[0x1ca8, 0x1cf8]
    =================================
    0x1c89: v1c89(0x1) = CONST 
    0x1c8b: v1c8b = SLOAD v1c89(0x1)
    0x1c8c: v1c8c(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1ca1: v1ca1 = AND v1c8c(0xffffffffffffffffffffffffffffffffffffffff), v1c8b
    0x1ca2: v1ca2 = CALLER 
    0x1ca3: v1ca3 = EQ v1ca2, v1ca1
    0x1ca4: v1ca4(0x1cf8) = CONST 
    0x1ca7: JUMPI v1ca4(0x1cf8), v1ca3

    Begin block 0x1ca8
    prev=[0x1c88], succ=[]
    =================================
    0x1ca8: v1ca8(0x40) = CONST 
    0x1caa: v1caa = MLOAD v1ca8(0x40)
    0x1cab: v1cab(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1ccd: MSTORE v1caa, v1cab(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1cce: v1cce(0x4) = CONST 
    0x1cd0: v1cd0 = ADD v1cce(0x4), v1caa
    0x1cd3: v1cd3(0x20) = CONST 
    0x1cd5: v1cd5 = ADD v1cd3(0x20), v1cd0
    0x1cd8: v1cd8(0x20) = SUB v1cd5, v1cd0
    0x1cda: MSTORE v1cd0, v1cd8(0x20)
    0x1cdb: v1cdb(0x28) = CONST 
    0x1cde: MSTORE v1cd5, v1cdb(0x28)
    0x1cdf: v1cdf(0x20) = CONST 
    0x1ce1: v1ce1 = ADD v1cdf(0x20), v1cd5
    0x1ce3: v1ce3(0x311d) = CONST 
    0x1ce6: v1ce6(0x28) = CONST 
    0x1ce9: CODECOPY v1ce1, v1ce3(0x311d), v1ce6(0x28)
    0x1cea: v1cea(0x40) = CONST 
    0x1cec: v1cec = ADD v1cea(0x40), v1ce1
    0x1cf0: v1cf0(0x40) = CONST 
    0x1cf2: v1cf2 = MLOAD v1cf0(0x40)
    0x1cf5: v1cf5(0x84) = SUB v1cec, v1cf2
    0x1cf7: REVERT v1cf2, v1cf5(0x84)

    Begin block 0x1cf8
    prev=[0x1c88], succ=[0x3ac6]
    =================================
    0x1cf9: v1cf9(0xa) = CONST 
    0x1cfb: SSTORE v1cf9(0xa), v77f
    0x1cfc: JUMP v768(0x3ac6)

    Begin block 0x3ac6
    prev=[0x1cf8], succ=[]
    =================================
    0x3ac7: STOP 

}

function getBurnableDollarLeft()() public {
    Begin block 0x784
    prev=[], succ=[0x34e0x784]
    =================================
    0x785: v785(0x34e) = CONST 
    0x788: v788(0x1cfd) = CONST 
    0x78b: v78b_0 = CALLPRIVATE v788(0x1cfd), v785(0x34e)

    Begin block 0x34e0x784
    prev=[0x784], succ=[]
    =================================
    0x34f0x784: v78434f(0x40) = CONST 
    0x3520x784: v784352 = MLOAD v78434f(0x40)
    0x3550x784: MSTORE v784352, v78b_0
    0x3560x784: v784356 = MLOAD v78434f(0x40)
    0x35a0x784: v78435a(0x0) = SUB v784352, v784356
    0x35b0x784: v78435b(0x20) = CONST 
    0x35d0x784: v78435d(0x20) = ADD v78435b(0x20), v78435a(0x0)
    0x35f0x784: RETURN v784356, v78435d(0x20)

}

function expiredCouponEpochs()() public {
    Begin block 0x78c
    prev=[], succ=[0x1d40]
    =================================
    0x78d: v78d(0x3ae7) = CONST 
    0x790: v790(0x1d40) = CONST 
    0x793: JUMP v790(0x1d40)

    Begin block 0x1d40
    prev=[0x78c], succ=[0x3ae7]
    =================================
    0x1d41: v1d41(0x14) = CONST 
    0x1d43: v1d43 = SLOAD v1d41(0x14)
    0x1d45: JUMP v78d(0x3ae7)

    Begin block 0x3ae7
    prev=[0x1d40], succ=[]
    =================================
    0x3ae8: v3ae8(0x40) = CONST 
    0x3aeb: v3aeb = MLOAD v3ae8(0x40)
    0x3aee: MSTORE v3aeb, v1d43
    0x3aef: v3aef = MLOAD v3ae8(0x40)
    0x3af3: v3af3(0x0) = SUB v3aeb, v3aef
    0x3af4: v3af4(0x20) = CONST 
    0x3af6: v3af6(0x20) = ADD v3af4(0x20), v3af3(0x0)
    0x3af8: RETURN v3aef, v3af6(0x20)

}

function setMaxPremiumRate(uint256)() public {
    Begin block 0x794
    prev=[], succ=[0x7a6, 0x7aa]
    =================================
    0x795: v795(0x3b18) = CONST 
    0x798: v798(0x4) = CONST 
    0x79b: v79b = CALLDATASIZE 
    0x79c: v79c = SUB v79b, v798(0x4)
    0x79d: v79d(0x20) = CONST 
    0x7a0: v7a0 = LT v79c, v79d(0x20)
    0x7a1: v7a1 = ISZERO v7a0
    0x7a2: v7a2(0x7aa) = CONST 
    0x7a5: JUMPI v7a2(0x7aa), v7a1

    Begin block 0x7a6
    prev=[0x794], succ=[]
    =================================
    0x7a6: v7a6(0x0) = CONST 
    0x7a9: REVERT v7a6(0x0), v7a6(0x0)

    Begin block 0x7aa
    prev=[0x794], succ=[0x1d46]
    =================================
    0x7ac: v7ac = CALLDATALOAD v798(0x4)
    0x7ad: v7ad(0x1d46) = CONST 
    0x7b0: JUMP v7ad(0x1d46)

    Begin block 0x1d46
    prev=[0x7aa], succ=[0x1d66, 0x1db6]
    =================================
    0x1d47: v1d47(0x1) = CONST 
    0x1d49: v1d49 = SLOAD v1d47(0x1)
    0x1d4a: v1d4a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1d5f: v1d5f = AND v1d4a(0xffffffffffffffffffffffffffffffffffffffff), v1d49
    0x1d60: v1d60 = CALLER 
    0x1d61: v1d61 = EQ v1d60, v1d5f
    0x1d62: v1d62(0x1db6) = CONST 
    0x1d65: JUMPI v1d62(0x1db6), v1d61

    Begin block 0x1d66
    prev=[0x1d46], succ=[]
    =================================
    0x1d66: v1d66(0x40) = CONST 
    0x1d68: v1d68 = MLOAD v1d66(0x40)
    0x1d69: v1d69(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1d8b: MSTORE v1d68, v1d69(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d8c: v1d8c(0x4) = CONST 
    0x1d8e: v1d8e = ADD v1d8c(0x4), v1d68
    0x1d91: v1d91(0x20) = CONST 
    0x1d93: v1d93 = ADD v1d91(0x20), v1d8e
    0x1d96: v1d96(0x20) = SUB v1d93, v1d8e
    0x1d98: MSTORE v1d8e, v1d96(0x20)
    0x1d99: v1d99(0x28) = CONST 
    0x1d9c: MSTORE v1d93, v1d99(0x28)
    0x1d9d: v1d9d(0x20) = CONST 
    0x1d9f: v1d9f = ADD v1d9d(0x20), v1d93
    0x1da1: v1da1(0x311d) = CONST 
    0x1da4: v1da4(0x28) = CONST 
    0x1da7: CODECOPY v1d9f, v1da1(0x311d), v1da4(0x28)
    0x1da8: v1da8(0x40) = CONST 
    0x1daa: v1daa = ADD v1da8(0x40), v1d9f
    0x1dae: v1dae(0x40) = CONST 
    0x1db0: v1db0 = MLOAD v1dae(0x40)
    0x1db3: v1db3(0x84) = SUB v1daa, v1db0
    0x1db5: REVERT v1db0, v1db3(0x84)

    Begin block 0x1db6
    prev=[0x1d46], succ=[0x3b18]
    =================================
    0x1db7: v1db7(0xc) = CONST 
    0x1db9: SSTORE v1db7(0xc), v7ac
    0x1dba: JUMP v795(0x3b18)

    Begin block 0x3b18
    prev=[0x1db6], succ=[]
    =================================
    0x3b19: STOP 

}

function lpPoolIncentiveRate()() public {
    Begin block 0x7b1
    prev=[], succ=[0x1dbb]
    =================================
    0x7b2: v7b2(0x3b39) = CONST 
    0x7b5: v7b5(0x1dbb) = CONST 
    0x7b8: JUMP v7b5(0x1dbb)

    Begin block 0x1dbb
    prev=[0x7b1], succ=[0x3b39]
    =================================
    0x1dbc: v1dbc(0x13) = CONST 
    0x1dbe: v1dbe = SLOAD v1dbc(0x13)
    0x1dc0: JUMP v7b2(0x3b39)

    Begin block 0x3b39
    prev=[0x1dbb], succ=[]
    =================================
    0x3b3a: v3b3a(0x40) = CONST 
    0x3b3d: v3b3d = MLOAD v3b3a(0x40)
    0x3b40: MSTORE v3b3d, v1dbe
    0x3b41: v3b41 = MLOAD v3b3a(0x40)
    0x3b45: v3b45(0x0) = SUB v3b3d, v3b41
    0x3b46: v3b46(0x20) = CONST 
    0x3b48: v3b48(0x20) = ADD v3b46(0x20), v3b45(0x0)
    0x3b4a: RETURN v3b41, v3b48(0x20)

}

function maxRedeemableCouponPercentPerEpoch()() public {
    Begin block 0x7b9
    prev=[], succ=[0x1dc1]
    =================================
    0x7ba: v7ba(0x3b6a) = CONST 
    0x7bd: v7bd(0x1dc1) = CONST 
    0x7c0: JUMP v7bd(0x1dc1)

    Begin block 0x1dc1
    prev=[0x7b9], succ=[0x3b6a]
    =================================
    0x1dc2: v1dc2(0xd) = CONST 
    0x1dc4: v1dc4 = SLOAD v1dc2(0xd)
    0x1dc6: JUMP v7ba(0x3b6a)

    Begin block 0x3b6a
    prev=[0x1dc1], succ=[]
    =================================
    0x3b6b: v3b6b(0x40) = CONST 
    0x3b6e: v3b6e = MLOAD v3b6b(0x40)
    0x3b71: MSTORE v3b6e, v1dc4
    0x3b72: v3b72 = MLOAD v3b6b(0x40)
    0x3b76: v3b76(0x0) = SUB v3b6e, v3b72
    0x3b77: v3b77(0x20) = CONST 
    0x3b79: v3b79(0x20) = ADD v3b77(0x20), v3b76(0x0)
    0x3b7b: RETURN v3b72, v3b79(0x20)

}

function couponClaimed()() public {
    Begin block 0x7c1
    prev=[], succ=[0x1dc7]
    =================================
    0x7c2: v7c2(0x3b9b) = CONST 
    0x7c5: v7c5(0x1dc7) = CONST 
    0x7c8: JUMP v7c5(0x1dc7)

    Begin block 0x1dc7
    prev=[0x7c1], succ=[0x3b9b]
    =================================
    0x1dc8: v1dc8(0x8) = CONST 
    0x1dca: v1dca = SLOAD v1dc8(0x8)
    0x1dcc: JUMP v7c2(0x3b9b)

    Begin block 0x3b9b
    prev=[0x1dc7], succ=[]
    =================================
    0x3b9c: v3b9c(0x40) = CONST 
    0x3b9f: v3b9f = MLOAD v3b9c(0x40)
    0x3ba2: MSTORE v3b9f, v1dca
    0x3ba3: v3ba3 = MLOAD v3b9c(0x40)
    0x3ba7: v3ba7(0x0) = SUB v3b9f, v3ba3
    0x3ba8: v3ba8(0x20) = CONST 
    0x3baa: v3baa(0x20) = ADD v3ba8(0x20), v3ba7(0x0)
    0x3bac: RETURN v3ba3, v3baa(0x20)

}

function isDebtPhase()() public {
    Begin block 0x7c9
    prev=[], succ=[0x1dcd]
    =================================
    0x7ca: v7ca(0x3bcc) = CONST 
    0x7cd: v7cd(0x1dcd) = CONST 
    0x7d0: JUMP v7cd(0x1dcd)

    Begin block 0x1dcd
    prev=[0x7c9], succ=[0x1de0]
    =================================
    0x1dce: v1dce(0x0) = CONST 
    0x1dd0: v1dd0(0xde0b6b3a7640000) = CONST 
    0x1dd9: v1dd9(0x1de0) = CONST 
    0x1ddc: v1ddc(0x266f) = CONST 
    0x1ddf: v1ddf_0 = CALLPRIVATE v1ddc(0x266f), v1dd9(0x1de0)

    Begin block 0x1de0
    prev=[0x1dcd], succ=[0x3bcc]
    =================================
    0x1de1: v1de1 = LT v1ddf_0, v1dd0(0xde0b6b3a7640000)
    0x1de5: JUMP v7ca(0x3bcc)

    Begin block 0x3bcc
    prev=[0x1de0], succ=[]
    =================================
    0x3bcd: v3bcd(0x40) = CONST 
    0x3bd0: v3bd0 = MLOAD v3bcd(0x40)
    0x3bd2: v3bd2 = ISZERO v1de1
    0x3bd3: v3bd3 = ISZERO v3bd2
    0x3bd5: MSTORE v3bd0, v3bd3
    0x3bd6: v3bd6 = MLOAD v3bcd(0x40)
    0x3bda: v3bda(0x0) = SUB v3bd0, v3bd6
    0x3bdb: v3bdb(0x20) = CONST 
    0x3bdd: v3bdd(0x20) = ADD v3bdb(0x20), v3bda(0x0)
    0x3bdf: RETURN v3bd6, v3bdd(0x20)

}

function setOperator(address)() public {
    Begin block 0x7d1
    prev=[], succ=[0x7e3, 0x7e7]
    =================================
    0x7d2: v7d2(0x3bff) = CONST 
    0x7d5: v7d5(0x4) = CONST 
    0x7d8: v7d8 = CALLDATASIZE 
    0x7d9: v7d9 = SUB v7d8, v7d5(0x4)
    0x7da: v7da(0x20) = CONST 
    0x7dd: v7dd = LT v7d9, v7da(0x20)
    0x7de: v7de = ISZERO v7dd
    0x7df: v7df(0x7e7) = CONST 
    0x7e2: JUMPI v7df(0x7e7), v7de

    Begin block 0x7e3
    prev=[0x7d1], succ=[]
    =================================
    0x7e3: v7e3(0x0) = CONST 
    0x7e6: REVERT v7e3(0x0), v7e3(0x0)

    Begin block 0x7e7
    prev=[0x7d1], succ=[0x1de6]
    =================================
    0x7e9: v7e9 = CALLDATALOAD v7d5(0x4)
    0x7ea: v7ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x7ff: v7ff = AND v7ea(0xffffffffffffffffffffffffffffffffffffffff), v7e9
    0x800: v800(0x1de6) = CONST 
    0x803: JUMP v800(0x1de6)

    Begin block 0x1de6
    prev=[0x7e7], succ=[0x1e06, 0x1e56]
    =================================
    0x1de7: v1de7(0x1) = CONST 
    0x1de9: v1de9 = SLOAD v1de7(0x1)
    0x1dea: v1dea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1dff: v1dff = AND v1dea(0xffffffffffffffffffffffffffffffffffffffff), v1de9
    0x1e00: v1e00 = CALLER 
    0x1e01: v1e01 = EQ v1e00, v1dff
    0x1e02: v1e02(0x1e56) = CONST 
    0x1e05: JUMPI v1e02(0x1e56), v1e01

    Begin block 0x1e06
    prev=[0x1de6], succ=[]
    =================================
    0x1e06: v1e06(0x40) = CONST 
    0x1e08: v1e08 = MLOAD v1e06(0x40)
    0x1e09: v1e09(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1e2b: MSTORE v1e08, v1e09(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e2c: v1e2c(0x4) = CONST 
    0x1e2e: v1e2e = ADD v1e2c(0x4), v1e08
    0x1e31: v1e31(0x20) = CONST 
    0x1e33: v1e33 = ADD v1e31(0x20), v1e2e
    0x1e36: v1e36(0x20) = SUB v1e33, v1e2e
    0x1e38: MSTORE v1e2e, v1e36(0x20)
    0x1e39: v1e39(0x28) = CONST 
    0x1e3c: MSTORE v1e33, v1e39(0x28)
    0x1e3d: v1e3d(0x20) = CONST 
    0x1e3f: v1e3f = ADD v1e3d(0x20), v1e33
    0x1e41: v1e41(0x311d) = CONST 
    0x1e44: v1e44(0x28) = CONST 
    0x1e47: CODECOPY v1e3f, v1e41(0x311d), v1e44(0x28)
    0x1e48: v1e48(0x40) = CONST 
    0x1e4a: v1e4a = ADD v1e48(0x40), v1e3f
    0x1e4e: v1e4e(0x40) = CONST 
    0x1e50: v1e50 = MLOAD v1e4e(0x40)
    0x1e53: v1e53(0x84) = SUB v1e4a, v1e50
    0x1e55: REVERT v1e50, v1e53(0x84)

    Begin block 0x1e56
    prev=[0x1de6], succ=[0x3bff]
    =================================
    0x1e57: v1e57(0x1) = CONST 
    0x1e5a: v1e5a = SLOAD v1e57(0x1)
    0x1e5b: v1e5b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x1e7c: v1e7c = AND v1e5b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1e5a
    0x1e7d: v1e7d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1e95: v1e95 = AND v1e7d(0xffffffffffffffffffffffffffffffffffffffff), v7ff
    0x1e99: v1e99 = OR v1e95, v1e7c
    0x1e9b: SSTORE v1e57(0x1), v1e99
    0x1e9c: JUMP v7d2(0x3bff)

    Begin block 0x3bff
    prev=[0x1e56], succ=[]
    =================================
    0x3c00: STOP 

}

function maxDiscountRate()() public {
    Begin block 0x804
    prev=[], succ=[0x1e9d]
    =================================
    0x805: v805(0x3c20) = CONST 
    0x808: v808(0x1e9d) = CONST 
    0x80b: JUMP v808(0x1e9d)

    Begin block 0x1e9d
    prev=[0x804], succ=[0x3c20]
    =================================
    0x1e9e: v1e9e(0xa) = CONST 
    0x1ea0: v1ea0 = SLOAD v1e9e(0xa)
    0x1ea2: JUMP v805(0x3c20)

    Begin block 0x3c20
    prev=[0x1e9d], succ=[]
    =================================
    0x3c21: v3c21(0x40) = CONST 
    0x3c24: v3c24 = MLOAD v3c21(0x40)
    0x3c27: MSTORE v3c24, v1ea0
    0x3c28: v3c28 = MLOAD v3c21(0x40)
    0x3c2c: v3c2c(0x0) = SUB v3c24, v3c28
    0x3c2d: v3c2d(0x20) = CONST 
    0x3c2f: v3c2f(0x20) = ADD v3c2d(0x20), v3c2c(0x0)
    0x3c31: RETURN v3c28, v3c2f(0x20)

}

function redeemCoupons(uint256,uint256,uint256)() public {
    Begin block 0x80c
    prev=[], succ=[0x81e, 0x822]
    =================================
    0x80d: v80d(0x37d) = CONST 
    0x810: v810(0x4) = CONST 
    0x813: v813 = CALLDATASIZE 
    0x814: v814 = SUB v813, v810(0x4)
    0x815: v815(0x60) = CONST 
    0x818: v818 = LT v814, v815(0x60)
    0x819: v819 = ISZERO v818
    0x81a: v81a(0x822) = CONST 
    0x81d: JUMPI v81a(0x822), v819

    Begin block 0x81e
    prev=[0x80c], succ=[]
    =================================
    0x81e: v81e(0x0) = CONST 
    0x821: REVERT v81e(0x0), v81e(0x0)

    Begin block 0x822
    prev=[0x80c], succ=[0x1ea3]
    =================================
    0x825: v825 = CALLDATALOAD v810(0x4)
    0x827: v827(0x20) = CONST 
    0x82a: v82a(0x24) = ADD v810(0x4), v827(0x20)
    0x82b: v82b = CALLDATALOAD v82a(0x24)
    0x82d: v82d(0x40) = CONST 
    0x82f: v82f(0x44) = ADD v82d(0x40), v810(0x4)
    0x830: v830 = CALLDATALOAD v82f(0x44)
    0x831: v831(0x1ea3) = CONST 
    0x834: JUMP v831(0x1ea3)

    Begin block 0x1ea3
    prev=[0x822], succ=[0x2b34B0x1ea3]
    =================================
    0x1ea4: v1ea4(0x1eab) = CONST 
    0x1ea7: v1ea7(0x2b34) = CONST 
    0x1eaa: JUMP v1ea7(0x2b34)

    Begin block 0x2b34B0x1ea3
    prev=[0x1ea3], succ=[0x1eab]
    =================================
    0x2b35S0x1ea3: v2b35V1ea3 = NUMBER 
    0x2b36S0x1ea3: v2b36V1ea3(0x0) = CONST 
    0x2b3aS0x1ea3: MSTORE v2b36V1ea3(0x0), v2b35V1ea3
    0x2b3bS0x1ea3: v2b3bV1ea3(0x20) = CONST 
    0x2b3fS0x1ea3: MSTORE v2b3bV1ea3(0x20), v2b36V1ea3(0x0)
    0x2b40S0x1ea3: v2b40V1ea3(0x40) = CONST 
    0x2b44S0x1ea3: v2b44V1ea3 = SHA3 v2b36V1ea3(0x0), v2b40V1ea3(0x40)
    0x2b45S0x1ea3: v2b45V1ea3 = ORIGIN 
    0x2b47S0x1ea3: MSTORE v2b36V1ea3(0x0), v2b45V1ea3
    0x2b4aS0x1ea3: MSTORE v2b3bV1ea3(0x20), v2b44V1ea3
    0x2b4cS0x1ea3: v2b4cV1ea3 = SHA3 v2b36V1ea3(0x0), v2b40V1ea3(0x40)
    0x2b4dS0x1ea3: v2b4dV1ea3 = SLOAD v2b4cV1ea3
    0x2b4eS0x1ea3: v2b4eV1ea3(0xff) = CONST 
    0x2b50S0x1ea3: v2b50V1ea3 = AND v2b4eV1ea3(0xff), v2b4dV1ea3
    0x2b52S0x1ea3: JUMP v1ea4(0x1eab)

    Begin block 0x1eab
    prev=[0x2b34B0x1ea3], succ=[0x1eb1, 0x1f01]
    =================================
    0x1eac: v1eac = ISZERO v2b50V1ea3
    0x1ead: v1ead(0x1f01) = CONST 
    0x1eb0: JUMPI v1ead(0x1f01), v1eac

    Begin block 0x1eb1
    prev=[0x1eab], succ=[]
    =================================
    0x1eb1: v1eb1(0x40) = CONST 
    0x1eb3: v1eb3 = MLOAD v1eb1(0x40)
    0x1eb4: v1eb4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1ed6: MSTORE v1eb3, v1eb4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1ed7: v1ed7(0x4) = CONST 
    0x1ed9: v1ed9 = ADD v1ed7(0x4), v1eb3
    0x1edc: v1edc(0x20) = CONST 
    0x1ede: v1ede = ADD v1edc(0x20), v1ed9
    0x1ee1: v1ee1(0x20) = SUB v1ede, v1ed9
    0x1ee3: MSTORE v1ed9, v1ee1(0x20)
    0x1ee4: v1ee4(0x26) = CONST 
    0x1ee7: MSTORE v1ede, v1ee4(0x26)
    0x1ee8: v1ee8(0x20) = CONST 
    0x1eea: v1eea = ADD v1ee8(0x20), v1ede
    0x1eec: v1eec(0x32b8) = CONST 
    0x1eef: v1eef(0x26) = CONST 
    0x1ef2: CODECOPY v1eea, v1eec(0x32b8), v1eef(0x26)
    0x1ef3: v1ef3(0x40) = CONST 
    0x1ef5: v1ef5 = ADD v1ef3(0x40), v1eea
    0x1ef9: v1ef9(0x40) = CONST 
    0x1efb: v1efb = MLOAD v1ef9(0x40)
    0x1efe: v1efe(0x84) = SUB v1ef5, v1efb
    0x1f00: REVERT v1efb, v1efe(0x84)

    Begin block 0x1f01
    prev=[0x1eab], succ=[0x2b53B0x1f01]
    =================================
    0x1f02: v1f02(0x1f09) = CONST 
    0x1f05: v1f05(0x2b53) = CONST 
    0x1f08: JUMP v1f05(0x2b53)

    Begin block 0x2b53B0x1f01
    prev=[0x1f01], succ=[0x1f09]
    =================================
    0x2b54S0x1f01: v2b54V1f01 = NUMBER 
    0x2b55S0x1f01: v2b55V1f01(0x0) = CONST 
    0x2b59S0x1f01: MSTORE v2b55V1f01(0x0), v2b54V1f01
    0x2b5aS0x1f01: v2b5aV1f01(0x20) = CONST 
    0x2b5eS0x1f01: MSTORE v2b5aV1f01(0x20), v2b55V1f01(0x0)
    0x2b5fS0x1f01: v2b5fV1f01(0x40) = CONST 
    0x2b63S0x1f01: v2b63V1f01 = SHA3 v2b55V1f01(0x0), v2b5fV1f01(0x40)
    0x2b64S0x1f01: v2b64V1f01 = CALLER 
    0x2b66S0x1f01: MSTORE v2b55V1f01(0x0), v2b64V1f01
    0x2b69S0x1f01: MSTORE v2b5aV1f01(0x20), v2b63V1f01
    0x2b6bS0x1f01: v2b6bV1f01 = SHA3 v2b55V1f01(0x0), v2b5fV1f01(0x40)
    0x2b6cS0x1f01: v2b6cV1f01 = SLOAD v2b6bV1f01
    0x2b6dS0x1f01: v2b6dV1f01(0xff) = CONST 
    0x2b6fS0x1f01: v2b6fV1f01 = AND v2b6dV1f01(0xff), v2b6cV1f01
    0x2b71S0x1f01: JUMP v1f02(0x1f09)

    Begin block 0x1f09
    prev=[0x2b53B0x1f01], succ=[0x1f0f, 0x1f5f]
    =================================
    0x1f0a: v1f0a = ISZERO v2b6fV1f01
    0x1f0b: v1f0b(0x1f5f) = CONST 
    0x1f0e: JUMPI v1f0b(0x1f5f), v1f0a

    Begin block 0x1f0f
    prev=[0x1f09], succ=[]
    =================================
    0x1f0f: v1f0f(0x40) = CONST 
    0x1f11: v1f11 = MLOAD v1f0f(0x40)
    0x1f12: v1f12(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f34: MSTORE v1f11, v1f12(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f35: v1f35(0x4) = CONST 
    0x1f37: v1f37 = ADD v1f35(0x4), v1f11
    0x1f3a: v1f3a(0x20) = CONST 
    0x1f3c: v1f3c = ADD v1f3a(0x20), v1f37
    0x1f3f: v1f3f(0x20) = SUB v1f3c, v1f37
    0x1f41: MSTORE v1f37, v1f3f(0x20)
    0x1f42: v1f42(0x26) = CONST 
    0x1f45: MSTORE v1f3c, v1f42(0x26)
    0x1f46: v1f46(0x20) = CONST 
    0x1f48: v1f48 = ADD v1f46(0x20), v1f3c
    0x1f4a: v1f4a(0x32b8) = CONST 
    0x1f4d: v1f4d(0x26) = CONST 
    0x1f50: CODECOPY v1f48, v1f4a(0x32b8), v1f4d(0x26)
    0x1f51: v1f51(0x40) = CONST 
    0x1f53: v1f53 = ADD v1f51(0x40), v1f48
    0x1f57: v1f57(0x40) = CONST 
    0x1f59: v1f59 = MLOAD v1f57(0x40)
    0x1f5c: v1f5c(0x84) = SUB v1f53, v1f59
    0x1f5e: REVERT v1f59, v1f5c(0x84)

    Begin block 0x1f5f
    prev=[0x1f09], succ=[0x1f68, 0x1fb8]
    =================================
    0x1f60: v1f60(0x0) = CONST 
    0x1f63: v1f63 = GT v82b, v1f60(0x0)
    0x1f64: v1f64(0x1fb8) = CONST 
    0x1f67: JUMPI v1f64(0x1fb8), v1f63

    Begin block 0x1f68
    prev=[0x1f5f], succ=[]
    =================================
    0x1f68: v1f68(0x40) = CONST 
    0x1f6a: v1f6a = MLOAD v1f68(0x40)
    0x1f6b: v1f6b(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x1f8d: MSTORE v1f6a, v1f6b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1f8e: v1f8e(0x4) = CONST 
    0x1f90: v1f90 = ADD v1f8e(0x4), v1f6a
    0x1f93: v1f93(0x20) = CONST 
    0x1f95: v1f95 = ADD v1f93(0x20), v1f90
    0x1f98: v1f98(0x20) = SUB v1f95, v1f90
    0x1f9a: MSTORE v1f90, v1f98(0x20)
    0x1f9b: v1f9b(0x32) = CONST 
    0x1f9e: MSTORE v1f95, v1f9b(0x32)
    0x1f9f: v1f9f(0x20) = CONST 
    0x1fa1: v1fa1 = ADD v1f9f(0x20), v1f95
    0x1fa3: v1fa3(0x3055) = CONST 
    0x1fa6: v1fa6(0x32) = CONST 
    0x1fa9: CODECOPY v1fa1, v1fa3(0x3055), v1fa6(0x32)
    0x1faa: v1faa(0x40) = CONST 
    0x1fac: v1fac = ADD v1faa(0x40), v1fa1
    0x1fb0: v1fb0(0x40) = CONST 
    0x1fb2: v1fb2 = MLOAD v1fb0(0x40)
    0x1fb5: v1fb5(0x84) = SUB v1fac, v1fb2
    0x1fb7: REVERT v1fb2, v1fb5(0x84)

    Begin block 0x1fb8
    prev=[0x1f5f], succ=[0x1fc2]
    =================================
    0x1fb9: v1fb9(0x0) = CONST 
    0x1fbb: v1fbb(0x1fc2) = CONST 
    0x1fbe: v1fbe(0x1c11) = CONST 
    0x1fc1: v1fc1_0 = CALLPRIVATE v1fbe(0x1c11), v1fbb(0x1fc2)

    Begin block 0x1fc2
    prev=[0x1fb8], succ=[0x2046, 0x1fcf]
    =================================
    0x1fc3: v1fc3(0x14) = CONST 
    0x1fc5: v1fc5 = SLOAD v1fc3(0x14)
    0x1fca: v1fca = ISZERO v1fc5
    0x1fcb: v1fcb(0x2046) = CONST 
    0x1fce: JUMPI v1fcb(0x2046), v1fca

    Begin block 0x2046
    prev=[0x1fc2, 0x1fd9], succ=[0x2050]
    =================================
    0x2047: v2047(0x0) = CONST 
    0x2049: v2049(0x2050) = CONST 
    0x204c: v204c(0x266f) = CONST 
    0x204f: v204f_0 = CALLPRIVATE v204c(0x266f), v2049(0x2050)

    Begin block 0x2050
    prev=[0x2046], succ=[0x205a, 0x20c0]
    =================================
    0x2055: v2055 = EQ v204f_0, v830
    0x2056: v2056(0x20c0) = CONST 
    0x2059: JUMPI v2056(0x20c0), v2055

    Begin block 0x205a
    prev=[0x2050], succ=[]
    =================================
    0x205a: v205a(0x40) = CONST 
    0x205d: v205d = MLOAD v205a(0x40)
    0x205e: v205e(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2080: MSTORE v205d, v205e(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2081: v2081(0x20) = CONST 
    0x2083: v2083(0x4) = CONST 
    0x2086: v2086 = ADD v205d, v2083(0x4)
    0x2087: MSTORE v2086, v2081(0x20)
    0x2088: v2088(0x1e) = CONST 
    0x208a: v208a(0x24) = CONST 
    0x208d: v208d = ADD v205d, v208a(0x24)
    0x208e: MSTORE v208d, v2088(0x1e)
    0x208f: v208f(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000) = CONST 
    0x20b0: v20b0(0x44) = CONST 
    0x20b3: v20b3 = ADD v205d, v20b0(0x44)
    0x20b4: MSTORE v20b3, v208f(0x426f6e644d61726b65743a20646f6c6c6172207072696365206d6f7665640000)
    0x20b6: v20b6 = MLOAD v205a(0x40)
    0x20ba: v20ba(0x0) = SUB v205d, v20b6
    0x20bb: v20bb(0x64) = CONST 
    0x20bd: v20bd(0x64) = ADD v20bb(0x64), v20ba(0x0)
    0x20bf: REVERT v20b6, v20bd(0x64)

    Begin block 0x20c0
    prev=[0x2050], succ=[0x20d1, 0x2121]
    =================================
    0x20c1: v20c1(0xde0b6b3a7640000) = CONST 
    0x20cb: v20cb = LT v204f_0, v20c1(0xde0b6b3a7640000)
    0x20cc: v20cc = ISZERO v20cb
    0x20cd: v20cd(0x2121) = CONST 
    0x20d0: JUMPI v20cd(0x2121), v20cc

    Begin block 0x20d1
    prev=[0x20c0], succ=[]
    =================================
    0x20d1: v20d1(0x40) = CONST 
    0x20d3: v20d3 = MLOAD v20d1(0x40)
    0x20d4: v20d4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x20f6: MSTORE v20d3, v20d4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x20f7: v20f7(0x4) = CONST 
    0x20f9: v20f9 = ADD v20f7(0x4), v20d3
    0x20fc: v20fc(0x20) = CONST 
    0x20fe: v20fe = ADD v20fc(0x20), v20f9
    0x2101: v2101(0x20) = SUB v20fe, v20f9
    0x2103: MSTORE v20f9, v2101(0x20)
    0x2104: v2104(0x38) = CONST 
    0x2107: MSTORE v20fe, v2104(0x38)
    0x2108: v2108(0x20) = CONST 
    0x210a: v210a = ADD v2108(0x20), v20fe
    0x210c: v210c(0x3145) = CONST 
    0x210f: v210f(0x38) = CONST 
    0x2112: CODECOPY v210a, v210c(0x3145), v210f(0x38)
    0x2113: v2113(0x40) = CONST 
    0x2115: v2115 = ADD v2113(0x40), v210a
    0x2119: v2119(0x40) = CONST 
    0x211b: v211b = MLOAD v2119(0x40)
    0x211e: v211e(0x84) = SUB v2115, v211b
    0x2120: REVERT v211b, v211e(0x84)

    Begin block 0x2121
    prev=[0x20c0], succ=[0x212b]
    =================================
    0x2122: v2122(0x0) = CONST 
    0x2124: v2124(0x212b) = CONST 
    0x2127: v2127(0x1af0) = CONST 
    0x212a: v212a_0 = CALLPRIVATE v2127(0x1af0), v2124(0x212b)

    Begin block 0x212b
    prev=[0x2121], succ=[0x2136, 0x2186]
    =================================
    0x2130: v2130 = GT v82b, v212a_0
    0x2131: v2131 = ISZERO v2130
    0x2132: v2132(0x2186) = CONST 
    0x2135: JUMPI v2132(0x2186), v2131

    Begin block 0x2136
    prev=[0x212b], succ=[]
    =================================
    0x2136: v2136(0x40) = CONST 
    0x2138: v2138 = MLOAD v2136(0x40)
    0x2139: v2139(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x215b: MSTORE v2138, v2139(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x215c: v215c(0x4) = CONST 
    0x215e: v215e = ADD v215c(0x4), v2138
    0x2161: v2161(0x20) = CONST 
    0x2163: v2163 = ADD v2161(0x20), v215e
    0x2166: v2166(0x20) = SUB v2163, v215e
    0x2168: MSTORE v215e, v2166(0x20)
    0x2169: v2169(0x31) = CONST 
    0x216c: MSTORE v2163, v2169(0x31)
    0x216d: v216d(0x20) = CONST 
    0x216f: v216f = ADD v216d(0x20), v2163
    0x2171: v2171(0x317d) = CONST 
    0x2174: v2174(0x31) = CONST 
    0x2177: CODECOPY v216f, v2171(0x317d), v2174(0x31)
    0x2178: v2178(0x40) = CONST 
    0x217a: v217a = ADD v2178(0x40), v216f
    0x217e: v217e(0x40) = CONST 
    0x2180: v2180 = MLOAD v217e(0x40)
    0x2183: v2183(0x84) = SUB v217a, v2180
    0x2185: REVERT v2180, v2183(0x84)

    Begin block 0x2186
    prev=[0x212b], succ=[0x2190]
    =================================
    0x2187: v2187(0x0) = CONST 
    0x2189: v2189(0x2190) = CONST 
    0x218c: v218c(0x105e) = CONST 
    0x218f: v218f_0 = CALLPRIVATE v218c(0x105e), v2189(0x2190)

    Begin block 0x2190
    prev=[0x2186], succ=[0x219b, 0x2201]
    =================================
    0x2193: v2193(0x0) = CONST 
    0x2196: v2196 = GT v218f_0, v2193(0x0)
    0x2197: v2197(0x2201) = CONST 
    0x219a: JUMPI v2197(0x2201), v2196

    Begin block 0x219b
    prev=[0x2190], succ=[]
    =================================
    0x219b: v219b(0x40) = CONST 
    0x219e: v219e = MLOAD v219b(0x40)
    0x219f: v219f(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x21c1: MSTORE v219e, v219f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x21c2: v21c2(0x20) = CONST 
    0x21c4: v21c4(0x4) = CONST 
    0x21c7: v21c7 = ADD v219e, v21c4(0x4)
    0x21c8: MSTORE v21c7, v21c2(0x20)
    0x21c9: v21c9(0x1f) = CONST 
    0x21cb: v21cb(0x24) = CONST 
    0x21ce: v21ce = ADD v219e, v21cb(0x24)
    0x21cf: MSTORE v21ce, v21c9(0x1f)
    0x21d0: v21d0(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500) = CONST 
    0x21f1: v21f1(0x44) = CONST 
    0x21f4: v21f4 = ADD v219e, v21f1(0x44)
    0x21f5: MSTORE v21f4, v21d0(0x426f6e644d61726b65743a20696e76616c696420636f75706f6e207261746500)
    0x21f7: v21f7 = MLOAD v219b(0x40)
    0x21fb: v21fb(0x0) = SUB v219e, v21f7
    0x21fc: v21fc(0x64) = CONST 
    0x21fe: v21fe(0x64) = ADD v21fc(0x64), v21fb(0x0)
    0x2200: REVERT v21f7, v21fe(0x64)

    Begin block 0x2201
    prev=[0x2190], succ=[0x3ed0]
    =================================
    0x2202: v2202(0x0) = CONST 
    0x2204: v2204(0x2219) = CONST 
    0x2207: v2207(0xde0b6b3a7640000) = CONST 
    0x2210: v2210(0x3ed0) = CONST 
    0x2215: v2215(0x29f2) = CONST 
    0x2218: v2218_0 = CALLPRIVATE v2215(0x29f2), v218f_0, v82b, v2210(0x3ed0)

    Begin block 0x3ed0
    prev=[0x2201], succ=[0x2219]
    =================================
    0x3ed2: v3ed2(0x2a65) = CONST 
    0x3ed5: v3ed5_0 = CALLPRIVATE v3ed2(0x2a65), v2207(0xde0b6b3a7640000), v2218_0, v2204(0x2219)

    Begin block 0x2219
    prev=[0x3ed0], succ=[0x2292, 0x2296]
    =================================
    0x221a: v221a(0x2) = CONST 
    0x221c: v221c = SLOAD v221a(0x2)
    0x221d: v221d(0x40) = CONST 
    0x2220: v2220 = MLOAD v221d(0x40)
    0x2221: v2221(0x40c10f1900000000000000000000000000000000000000000000000000000000) = CONST 
    0x2243: MSTORE v2220, v2221(0x40c10f1900000000000000000000000000000000000000000000000000000000)
    0x2244: v2244 = CALLER 
    0x2245: v2245(0x4) = CONST 
    0x2248: v2248 = ADD v2220, v2245(0x4)
    0x2249: MSTORE v2248, v2244
    0x224a: v224a(0x24) = CONST 
    0x224d: v224d = ADD v2220, v224a(0x24)
    0x2250: MSTORE v224d, v3ed5_0
    0x2252: v2252 = MLOAD v221d(0x40)
    0x2256: v2256(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x226d: v226d = AND v221c, v2256(0xffffffffffffffffffffffffffffffffffffffff)
    0x226f: v226f(0x40c10f19) = CONST 
    0x2275: v2275(0x44) = CONST 
    0x2279: v2279 = ADD v2220, v2275(0x44)
    0x227b: v227b(0x20) = CONST 
    0x2283: v2283(0x0) = SUB v2220, v2252
    0x2284: v2284(0x44) = ADD v2283(0x0), v2275(0x44)
    0x2286: v2286(0x0) = CONST 
    0x228a: v228a = EXTCODESIZE v226d
    0x228b: v228b = ISZERO v228a
    0x228d: v228d = ISZERO v228b
    0x228e: v228e(0x2296) = CONST 
    0x2291: JUMPI v228e(0x2296), v228d

    Begin block 0x2292
    prev=[0x2219], succ=[]
    =================================
    0x2292: v2292(0x0) = CONST 
    0x2295: REVERT v2292(0x0), v2292(0x0)

    Begin block 0x2296
    prev=[0x2219], succ=[0x22a1, 0x22aa]
    =================================
    0x2298: v2298 = GAS 
    0x2299: v2299 = CALL v2298, v226d, v2286(0x0), v2252, v2284(0x44), v2252, v227b(0x20)
    0x229a: v229a = ISZERO v2299
    0x229c: v229c = ISZERO v229a
    0x229d: v229d(0x22aa) = CONST 
    0x22a0: JUMPI v229d(0x22aa), v229c

    Begin block 0x22a1
    prev=[0x2296], succ=[]
    =================================
    0x22a1: v22a1 = RETURNDATASIZE 
    0x22a2: v22a2(0x0) = CONST 
    0x22a5: RETURNDATACOPY v22a2(0x0), v22a2(0x0), v22a1
    0x22a6: v22a6 = RETURNDATASIZE 
    0x22a7: v22a7(0x0) = CONST 
    0x22a9: REVERT v22a7(0x0), v22a6

    Begin block 0x22aa
    prev=[0x2296], succ=[0x22bc, 0x22c0]
    =================================
    0x22af: v22af(0x40) = CONST 
    0x22b1: v22b1 = MLOAD v22af(0x40)
    0x22b2: v22b2 = RETURNDATASIZE 
    0x22b3: v22b3(0x20) = CONST 
    0x22b6: v22b6 = LT v22b2, v22b3(0x20)
    0x22b7: v22b7 = ISZERO v22b6
    0x22b8: v22b8(0x22c0) = CONST 
    0x22bb: JUMPI v22b8(0x22c0), v22b7

    Begin block 0x22bc
    prev=[0x22aa], succ=[]
    =================================
    0x22bc: v22bc(0x0) = CONST 
    0x22bf: REVERT v22bc(0x0), v22bc(0x0)

    Begin block 0x22c0
    prev=[0x22aa], succ=[0x231c]
    =================================
    0x22c3: v22c3(0x40) = CONST 
    0x22c6: v22c6 = MLOAD v22c3(0x40)
    0x22c9: v22c9 = ADD v22c3(0x40), v22c6
    0x22cb: MSTORE v22c3(0x40), v22c9
    0x22cc: v22cc(0xb) = CONST 
    0x22cf: MSTORE v22c6, v22cc(0xb)
    0x22d0: v22d0(0x6f7665722072656465656d000000000000000000000000000000000000000000) = CONST 
    0x22f1: v22f1(0x20) = CONST 
    0x22f5: v22f5 = ADD v22f1(0x20), v22c6
    0x22f9: MSTORE v22f5, v22d0(0x6f7665722072656465656d000000000000000000000000000000000000000000)
    0x22fa: v22fa = CALLER 
    0x22fb: v22fb(0x0) = CONST 
    0x22ff: MSTORE v22fb(0x0), v22fa
    0x2300: v2300(0xe) = CONST 
    0x2303: MSTORE v22f1(0x20), v2300(0xe)
    0x2306: v2306 = SHA3 v22fb(0x0), v22c3(0x40)
    0x2309: MSTORE v22fb(0x0), v825
    0x230c: MSTORE v22f1(0x20), v2306
    0x2310: v2310 = SHA3 v22fb(0x0), v22c3(0x40)
    0x2311: v2311 = SLOAD v2310
    0x2312: v2312(0x231c) = CONST 
    0x2318: v2318(0x2bef) = CONST 
    0x231b: v231b_0 = CALLPRIVATE v2318(0x2bef), v22c6, v82b, v2311, v2312(0x231c)

    Begin block 0x231c
    prev=[0x22c0], succ=[0x29b0B0x231c]
    =================================
    0x231d: v231d = CALLER 
    0x231e: v231e(0x0) = CONST 
    0x2322: MSTORE v231e(0x0), v231d
    0x2323: v2323(0xe) = CONST 
    0x2325: v2325(0x20) = CONST 
    0x2329: MSTORE v2325(0x20), v2323(0xe)
    0x232a: v232a(0x40) = CONST 
    0x232e: v232e = SHA3 v231e(0x0), v232a(0x40)
    0x2331: MSTORE v231e(0x0), v825
    0x2333: MSTORE v2325(0x20), v232e
    0x2336: v2336 = SHA3 v231e(0x0), v232a(0x40)
    0x233a: SSTORE v2336, v231b_0
    0x233d: MSTORE v231e(0x0), v231d
    0x233e: v233e(0x12) = CONST 
    0x2342: MSTORE v2325(0x20), v233e(0x12)
    0x2343: v2343 = SHA3 v231e(0x0), v232a(0x40)
    0x2344: v2344 = SLOAD v2343
    0x2345: v2345(0x234e) = CONST 
    0x234a: v234a(0x29b0) = CONST 
    0x234d: JUMP v234a(0x29b0)

    Begin block 0x29b0B0x231c
    prev=[0x231c], succ=[0x29a70x29b0B0x231c]
    =================================
    0x29b1S0x231c: v29b1V231c(0x0) = CONST 
    0x29b3S0x231c: v29b3V231c(0x29a7) = CONST 
    0x29b8S0x231c: v29b8V231c(0x40) = CONST 
    0x29baS0x231c: v29baV231c = MLOAD v29b8V231c(0x40)
    0x29bcS0x231c: v29bcV231c(0x40) = CONST 
    0x29beS0x231c: v29beV231c = ADD v29bcV231c(0x40), v29baV231c
    0x29bfS0x231c: v29bfV231c(0x40) = CONST 
    0x29c1S0x231c: MSTORE v29bfV231c(0x40), v29beV231c
    0x29c3S0x231c: v29c3V231c(0x1e) = CONST 
    0x29c6S0x231c: MSTORE v29baV231c, v29c3V231c(0x1e)
    0x29c7S0x231c: v29c7V231c(0x20) = CONST 
    0x29c9S0x231c: v29c9V231c = ADD v29c7V231c(0x20), v29baV231c
    0x29caS0x231c: v29caV231c(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x231c: MSTORE v29c9V231c, v29caV231c(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x231c: v29eeV231c(0x2bef) = CONST 
    0x29f1S0x231c: v29f1_0V231c = CALLPRIVATE v29eeV231c(0x2bef), v29baV231c, v82b, v2344, v29b3V231c(0x29a7)

    Begin block 0x29a70x29b0B0x231c
    prev=[0x29b0B0x231c], succ=[0x29aa0x29b0B0x231c]
    =================================

    Begin block 0x29aa0x29b0B0x231c
    prev=[0x29a70x29b0B0x231c], succ=[0x234e]
    =================================
    0x29af0x29b0S0x231c: JUMP v2345(0x234e)

    Begin block 0x234e
    prev=[0x29aa0x29b0B0x231c], succ=[0x29b0B0x234e]
    =================================
    0x234f: v234f = CALLER 
    0x2350: v2350(0x0) = CONST 
    0x2354: MSTORE v2350(0x0), v234f
    0x2355: v2355(0x12) = CONST 
    0x2357: v2357(0x20) = CONST 
    0x2359: MSTORE v2357(0x20), v2355(0x12)
    0x235a: v235a(0x40) = CONST 
    0x235d: v235d = SHA3 v2350(0x0), v235a(0x40)
    0x235e: SSTORE v235d, v29f1_0V231c
    0x235f: v235f(0x11) = CONST 
    0x2361: v2361 = SLOAD v235f(0x11)
    0x2362: v2362(0x236b) = CONST 
    0x2367: v2367(0x29b0) = CONST 
    0x236a: JUMP v2367(0x29b0)

    Begin block 0x29b0B0x234e
    prev=[0x234e], succ=[0x29a70x29b0B0x234e]
    =================================
    0x29b1S0x234e: v29b1V234e(0x0) = CONST 
    0x29b3S0x234e: v29b3V234e(0x29a7) = CONST 
    0x29b8S0x234e: v29b8V234e(0x40) = CONST 
    0x29baS0x234e: v29baV234e = MLOAD v29b8V234e(0x40)
    0x29bcS0x234e: v29bcV234e(0x40) = CONST 
    0x29beS0x234e: v29beV234e = ADD v29bcV234e(0x40), v29baV234e
    0x29bfS0x234e: v29bfV234e(0x40) = CONST 
    0x29c1S0x234e: MSTORE v29bfV234e(0x40), v29beV234e
    0x29c3S0x234e: v29c3V234e(0x1e) = CONST 
    0x29c6S0x234e: MSTORE v29baV234e, v29c3V234e(0x1e)
    0x29c7S0x234e: v29c7V234e(0x20) = CONST 
    0x29c9S0x234e: v29c9V234e = ADD v29c7V234e(0x20), v29baV234e
    0x29caS0x234e: v29caV234e(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000) = CONST 
    0x29ecS0x234e: MSTORE v29c9V234e, v29caV234e(0x536166654d6174683a207375627472616374696f6e206f766572666c6f770000)
    0x29eeS0x234e: v29eeV234e(0x2bef) = CONST 
    0x29f1S0x234e: v29f1_0V234e = CALLPRIVATE v29eeV234e(0x2bef), v29baV234e, v82b, v2361, v29b3V234e(0x29a7)

    Begin block 0x29a70x29b0B0x234e
    prev=[0x29b0B0x234e], succ=[0x29aa0x29b0B0x234e]
    =================================

    Begin block 0x29aa0x29b0B0x234e
    prev=[0x29a70x29b0B0x234e], succ=[0x236b]
    =================================
    0x29af0x29b0S0x234e: JUMP v2362(0x236b)

    Begin block 0x236b
    prev=[0x29aa0x29b0B0x234e], succ=[0x237b]
    =================================
    0x236c: v236c(0x11) = CONST 
    0x236e: SSTORE v236c(0x11), v29f1_0V234e
    0x236f: v236f(0x8) = CONST 
    0x2371: v2371 = SLOAD v236f(0x8)
    0x2372: v2372(0x237b) = CONST 
    0x2377: v2377(0x2933) = CONST 
    0x237a: v237a_0 = CALLPRIVATE v2377(0x2933), v82b, v2371, v2372(0x237b)

    Begin block 0x237b
    prev=[0x236b], succ=[0x2397]
    =================================
    0x237c: v237c(0x8) = CONST 
    0x237e: SSTORE v237c(0x8), v237a_0
    0x237f: v237f(0x0) = CONST 
    0x2383: MSTORE v237f(0x0), v1fc1_0
    0x2384: v2384(0x10) = CONST 
    0x2386: v2386(0x20) = CONST 
    0x2388: MSTORE v2386(0x20), v2384(0x10)
    0x2389: v2389(0x40) = CONST 
    0x238c: v238c = SHA3 v237f(0x0), v2389(0x40)
    0x238d: v238d = SLOAD v238c
    0x238e: v238e(0x2397) = CONST 
    0x2393: v2393(0x2933) = CONST 
    0x2396: v2396_0 = CALLPRIVATE v2393(0x2933), v82b, v238d, v238e(0x2397)

    Begin block 0x2397
    prev=[0x237b], succ=[0x23ae]
    =================================
    0x2398: v2398(0x0) = CONST 
    0x239c: MSTORE v2398(0x0), v1fc1_0
    0x239d: v239d(0x10) = CONST 
    0x239f: v239f(0x20) = CONST 
    0x23a1: MSTORE v239f(0x20), v239d(0x10)
    0x23a2: v23a2(0x40) = CONST 
    0x23a5: v23a5 = SHA3 v2398(0x0), v23a2(0x40)
    0x23a6: SSTORE v23a5, v2396_0
    0x23a7: v23a7(0x23ae) = CONST 
    0x23aa: v23aa(0x2b72) = CONST 
    0x23ad: CALLPRIVATE v23aa(0x2b72), v23a7(0x23ae)

    Begin block 0x23ae
    prev=[0x2397], succ=[0x37d0x80c]
    =================================
    0x23af: v23af(0x40) = CONST 
    0x23b2: v23b2 = MLOAD v23af(0x40)
    0x23b5: MSTORE v23b2, v1fc1_0
    0x23b6: v23b6(0x20) = CONST 
    0x23b9: v23b9 = ADD v23b2, v23b6(0x20)
    0x23bc: MSTORE v23b9, v825
    0x23bf: v23bf = ADD v23af(0x40), v23b2
    0x23c2: MSTORE v23bf, v3ed5_0
    0x23c3: v23c3(0x60) = CONST 
    0x23c6: v23c6 = ADD v23b2, v23c3(0x60)
    0x23c9: MSTORE v23c6, v82b
    0x23cb: v23cb = MLOAD v23af(0x40)
    0x23cc: v23cc = CALLER 
    0x23ce: v23ce(0xb5e7fa60bdf74ffc7e542c61b550354c38e19b153814e6089dbaf3bbd7ae59b) = CONST 
    0x23f3: v23f3(0x0) = SUB v23b2, v23cb
    0x23f4: v23f4(0x80) = CONST 
    0x23f6: v23f6(0x80) = ADD v23f4(0x80), v23f3(0x0)
    0x23f8: LOG2 v23cb, v23f6(0x80), v23ce(0xb5e7fa60bdf74ffc7e542c61b550354c38e19b153814e6089dbaf3bbd7ae59b), v23cc
    0x23fb: v23fb = NUMBER 
    0x23fc: v23fc(0x0) = CONST 
    0x2400: MSTORE v23fc(0x0), v23fb
    0x2401: v2401(0x20) = CONST 
    0x2405: MSTORE v2401(0x20), v23fc(0x0)
    0x2406: v2406(0x40) = CONST 
    0x240a: v240a = SHA3 v23fc(0x0), v2406(0x40)
    0x240b: v240b = ORIGIN 
    0x240d: MSTORE v23fc(0x0), v240b
    0x2410: MSTORE v2401(0x20), v240a
    0x2413: v2413 = SHA3 v23fc(0x0), v2406(0x40)
    0x2415: v2415 = SLOAD v2413
    0x2416: v2416(0x1) = CONST 
    0x2418: v2418(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = CONST 
    0x243b: v243b = AND v2418(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2415
    0x243d: v243d = OR v2416(0x1), v243b
    0x2440: SSTORE v2413, v243d
    0x2441: v2441 = CALLER 
    0x2443: MSTORE v23fc(0x0), v2441
    0x2447: v2447 = SHA3 v23fc(0x0), v2406(0x40)
    0x2449: v2449 = SLOAD v2447
    0x244c: v244c = AND v2418(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v2449
    0x244f: v244f = OR v2416(0x1), v244c
    0x2451: SSTORE v2447, v244f
    0x2459: JUMP v80d(0x37d)

    Begin block 0x37d0x80c
    prev=[0x23ae], succ=[]
    =================================
    0x37e0x80c: STOP 

    Begin block 0x1fcf
    prev=[0x1fc2], succ=[0x1fd9]
    =================================
    0x1fd0: v1fd0(0x1fd9) = CONST 
    0x1fd5: v1fd5(0x2933) = CONST 
    0x1fd8: v1fd8_0 = CALLPRIVATE v1fd5(0x2933), v1fc5, v825, v1fd0(0x1fd9)

    Begin block 0x1fd9
    prev=[0x1fcf], succ=[0x1fe0, 0x2046]
    =================================
    0x1fda: v1fda = LT v1fd8_0, v1fc1_0
    0x1fdb: v1fdb = ISZERO v1fda
    0x1fdc: v1fdc(0x2046) = CONST 
    0x1fdf: JUMPI v1fdc(0x2046), v1fdb

    Begin block 0x1fe0
    prev=[0x1fd9], succ=[]
    =================================
    0x1fe0: v1fe0(0x40) = CONST 
    0x1fe3: v1fe3 = MLOAD v1fe0(0x40)
    0x1fe4: v1fe4(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x2006: MSTORE v1fe3, v1fe4(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2007: v2007(0x20) = CONST 
    0x2009: v2009(0x4) = CONST 
    0x200c: v200c = ADD v1fe3, v2009(0x4)
    0x200d: MSTORE v200c, v2007(0x20)
    0x200e: v200e(0x1b) = CONST 
    0x2010: v2010(0x24) = CONST 
    0x2013: v2013 = ADD v1fe3, v2010(0x24)
    0x2014: MSTORE v2013, v200e(0x1b)
    0x2015: v2015(0x426f6e644d61726b65743a20636f75706f6e7320657870697265640000000000) = CONST 
    0x2036: v2036(0x44) = CONST 
    0x2039: v2039 = ADD v1fe3, v2036(0x44)
    0x203a: MSTORE v2039, v2015(0x426f6e644d61726b65743a20636f75706f6e7320657870697265640000000000)
    0x203c: v203c = MLOAD v1fe0(0x40)
    0x2040: v2040(0x0) = SUB v1fe3, v203c
    0x2041: v2041(0x64) = CONST 
    0x2043: v2043(0x64) = ADD v2041(0x64), v2040(0x0)
    0x2045: REVERT v203c, v2043(0x64)

}

function initialize(address,address,address)() public {
    Begin block 0x835
    prev=[], succ=[0x847, 0x84b]
    =================================
    0x836: v836(0x3c51) = CONST 
    0x839: v839(0x4) = CONST 
    0x83c: v83c = CALLDATASIZE 
    0x83d: v83d = SUB v83c, v839(0x4)
    0x83e: v83e(0x60) = CONST 
    0x841: v841 = LT v83d, v83e(0x60)
    0x842: v842 = ISZERO v841
    0x843: v843(0x84b) = CONST 
    0x846: JUMPI v843(0x84b), v842

    Begin block 0x847
    prev=[0x835], succ=[]
    =================================
    0x847: v847(0x0) = CONST 
    0x84a: REVERT v847(0x0), v847(0x0)

    Begin block 0x84b
    prev=[0x835], succ=[0x245a]
    =================================
    0x84d: v84d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x863: v863 = CALLDATALOAD v839(0x4)
    0x865: v865 = AND v84d(0xffffffffffffffffffffffffffffffffffffffff), v863
    0x867: v867(0x20) = CONST 
    0x86a: v86a(0x24) = ADD v839(0x4), v867(0x20)
    0x86b: v86b = CALLDATALOAD v86a(0x24)
    0x86d: v86d = AND v84d(0xffffffffffffffffffffffffffffffffffffffff), v86b
    0x86f: v86f(0x40) = CONST 
    0x873: v873(0x44) = ADD v839(0x4), v86f(0x40)
    0x874: v874 = CALLDATALOAD v873(0x44)
    0x875: v875 = AND v874, v84d(0xffffffffffffffffffffffffffffffffffffffff)
    0x876: v876(0x245a) = CONST 
    0x879: JUMP v876(0x245a)

    Begin block 0x245a
    prev=[0x84b], succ=[0x247e, 0x24ce]
    =================================
    0x245b: v245b(0x1) = CONST 
    0x245d: v245d = SLOAD v245b(0x1)
    0x245e: v245e(0x10000000000000000000000000000000000000000) = CONST 
    0x2475: v2475 = DIV v245d, v245e(0x10000000000000000000000000000000000000000)
    0x2476: v2476(0xff) = CONST 
    0x2478: v2478 = AND v2476(0xff), v2475
    0x2479: v2479 = ISZERO v2478
    0x247a: v247a(0x24ce) = CONST 
    0x247d: JUMPI v247a(0x24ce), v2479

    Begin block 0x247e
    prev=[0x245a], succ=[]
    =================================
    0x247e: v247e(0x40) = CONST 
    0x2480: v2480 = MLOAD v247e(0x40)
    0x2481: v2481(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x24a3: MSTORE v2480, v2481(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x24a4: v24a4(0x4) = CONST 
    0x24a6: v24a6 = ADD v24a4(0x4), v2480
    0x24a9: v24a9(0x20) = CONST 
    0x24ab: v24ab = ADD v24a9(0x20), v24a6
    0x24ae: v24ae(0x20) = SUB v24ab, v24a6
    0x24b0: MSTORE v24a6, v24ae(0x20)
    0x24b1: v24b1(0x21) = CONST 
    0x24b4: MSTORE v24ab, v24b1(0x21)
    0x24b5: v24b5(0x20) = CONST 
    0x24b7: v24b7 = ADD v24b5(0x20), v24ab
    0x24b9: v24b9(0x31ae) = CONST 
    0x24bc: v24bc(0x21) = CONST 
    0x24bf: CODECOPY v24b7, v24b9(0x31ae), v24bc(0x21)
    0x24c0: v24c0(0x40) = CONST 
    0x24c2: v24c2 = ADD v24c0(0x40), v24b7
    0x24c6: v24c6(0x40) = CONST 
    0x24c8: v24c8 = MLOAD v24c6(0x40)
    0x24cb: v24cb(0x84) = SUB v24c2, v24c8
    0x24cd: REVERT v24c8, v24cb(0x84)

    Begin block 0x24ce
    prev=[0x245a], succ=[0x3c51]
    =================================
    0x24cf: v24cf(0x2) = CONST 
    0x24d2: v24d2 = SLOAD v24cf(0x2)
    0x24d3: v24d3(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24ea: v24ea = AND v865, v24d3(0xffffffffffffffffffffffffffffffffffffffff)
    0x24eb: v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = CONST 
    0x250e: v250e = AND v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v24d2
    0x250f: v250f = OR v250e, v24ea
    0x2512: SSTORE v24cf(0x2), v250f
    0x2513: v2513(0x3) = CONST 
    0x2516: v2516 = SLOAD v2513(0x3)
    0x2519: v2519 = AND v24d3(0xffffffffffffffffffffffffffffffffffffffff), v86d
    0x251c: v251c = AND v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2516
    0x251d: v251d = OR v251c, v2519
    0x251f: SSTORE v2513(0x3), v251d
    0x2520: v2520(0x4) = CONST 
    0x2523: v2523 = SLOAD v2520(0x4)
    0x2526: v2526 = AND v875, v24d3(0xffffffffffffffffffffffffffffffffffffffff)
    0x2529: v2529 = AND v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2523
    0x252d: v252d = OR v2529, v2526
    0x2530: SSTORE v2520(0x4), v252d
    0x2531: v2531(0x5) = CONST 
    0x2534: v2534 = SLOAD v2531(0x5)
    0x2536: v2536 = AND v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v2534
    0x2537: v2537(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) = CONST 
    0x254c: v254c = OR v2537(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2), v2536
    0x254e: SSTORE v2531(0x5), v254c
    0x254f: v254f(0x0) = CONST 
    0x2551: v2551(0x6) = CONST 
    0x2555: SSTORE v2551(0x6), v254f(0x0)
    0x2556: v2556(0x7) = CONST 
    0x255a: SSTORE v2556(0x7), v254f(0x0)
    0x255b: v255b(0x8) = CONST 
    0x255d: SSTORE v255b(0x8), v254f(0x0)
    0x255e: v255e(0x120a871cc0020000) = CONST 
    0x2567: v2567(0xa) = CONST 
    0x256b: SSTORE v2567(0xa), v255e(0x120a871cc0020000)
    0x256c: v256c(0xc) = CONST 
    0x256e: SSTORE v256c(0xc), v255e(0x120a871cc0020000)
    0x256f: v256f(0xbb8) = CONST 
    0x2572: v2572(0x9) = CONST 
    0x2576: SSTORE v2572(0x9), v256f(0xbb8)
    0x2577: v2577(0xb) = CONST 
    0x2579: SSTORE v2577(0xb), v256f(0xbb8)
    0x257a: v257a(0x12c) = CONST 
    0x257d: v257d(0xd) = CONST 
    0x257f: SSTORE v257d(0xd), v257a(0x12c)
    0x2580: v2580(0x1) = CONST 
    0x2583: v2583 = SLOAD v2580(0x1)
    0x2584: v2584(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x25a5: v25a5 = AND v2584(0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff), v2583
    0x25a6: v25a6(0x10000000000000000000000000000000000000000) = CONST 
    0x25bc: v25bc = OR v25a6(0x10000000000000000000000000000000000000000), v25a5
    0x25bf: v25bf = AND v24eb(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v25bc
    0x25c0: v25c0 = CALLER 
    0x25c3: v25c3 = OR v25c0, v25bf
    0x25c6: SSTORE v2580(0x1), v25c3
    0x25c7: v25c7(0x40) = CONST 
    0x25ca: v25ca = MLOAD v25c7(0x40)
    0x25cb: v25cb = NUMBER 
    0x25cd: MSTORE v25ca, v25cb
    0x25cf: v25cf = MLOAD v25c7(0x40)
    0x25d0: v25d0(0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79) = CONST 
    0x25f4: v25f4(0x0) = SUB v25ca, v25cf
    0x25f5: v25f5(0x20) = CONST 
    0x25f7: v25f7(0x20) = ADD v25f5(0x20), v25f4(0x0)
    0x25f9: LOG2 v25cf, v25f7(0x20), v25d0(0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79), v25c0
    0x25fd: JUMP v836(0x3c51)

    Begin block 0x3c51
    prev=[0x24ce], succ=[]
    =================================
    0x3c52: STOP 

}

function couponIssued()() public {
    Begin block 0x87a
    prev=[], succ=[0x25fe]
    =================================
    0x87b: v87b(0x3c72) = CONST 
    0x87e: v87e(0x25fe) = CONST 
    0x881: JUMP v87e(0x25fe)

    Begin block 0x25fe
    prev=[0x87a], succ=[0x3c72]
    =================================
    0x25ff: v25ff(0x7) = CONST 
    0x2601: v2601 = SLOAD v25ff(0x7)
    0x2603: JUMP v87b(0x3c72)

    Begin block 0x3c72
    prev=[0x25fe], succ=[]
    =================================
    0x3c73: v3c73(0x40) = CONST 
    0x3c76: v3c76 = MLOAD v3c73(0x40)
    0x3c79: MSTORE v3c76, v2601
    0x3c7a: v3c7a = MLOAD v3c73(0x40)
    0x3c7e: v3c7e(0x0) = SUB v3c76, v3c7a
    0x3c7f: v3c7f(0x20) = CONST 
    0x3c81: v3c81(0x20) = ADD v3c7f(0x20), v3c7e(0x0)
    0x3c83: RETURN v3c7a, v3c81(0x20)

}

function nextEpochPoint()() public {
    Begin block 0x882
    prev=[], succ=[0x2604B0x882]
    =================================
    0x883: v883(0x3ca3) = CONST 
    0x886: v886(0x2604) = CONST 
    0x889: JUMP v886(0x2604)

    Begin block 0x2604B0x882
    prev=[0x882], succ=[0x266bB0x882, 0x9150x2604B0x882]
    =================================
    0x2605S0x882: v2605V882(0x3) = CONST 
    0x2607S0x882: v2607V882 = SLOAD v2605V882(0x3)
    0x2608S0x882: v2608V882(0x40) = CONST 
    0x260bS0x882: v260bV882 = MLOAD v2608V882(0x40)
    0x260cS0x882: v260cV882(0xc5967c2600000000000000000000000000000000000000000000000000000000) = CONST 
    0x262eS0x882: MSTORE v260bV882, v260cV882(0xc5967c2600000000000000000000000000000000000000000000000000000000)
    0x2630S0x882: v2630V882 = MLOAD v2608V882(0x40)
    0x2631S0x882: v2631V882(0x0) = CONST 
    0x2634S0x882: v2634V882(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2649S0x882: v2649V882 = AND v2634V882(0xffffffffffffffffffffffffffffffffffffffff), v2607V882
    0x264bS0x882: v264bV882(0xc5967c26) = CONST 
    0x2651S0x882: v2651V882(0x4) = CONST 
    0x2655S0x882: v2655V882 = ADD v260bV882, v2651V882(0x4)
    0x2657S0x882: v2657V882(0x20) = CONST 
    0x265eS0x882: v265eV882(0x0) = SUB v260bV882, v2630V882
    0x265fS0x882: v265fV882(0x4) = ADD v265eV882(0x0), v2651V882(0x4)
    0x2663S0x882: v2663V882 = EXTCODESIZE v2649V882
    0x2664S0x882: v2664V882 = ISZERO v2663V882
    0x2666S0x882: v2666V882 = ISZERO v2664V882
    0x2667S0x882: v2667V882(0x915) = CONST 
    0x266aS0x882: JUMPI v2667V882(0x915), v2666V882

    Begin block 0x266bB0x882
    prev=[0x2604B0x882], succ=[]
    =================================
    0x266bS0x882: v266bV882(0x0) = CONST 
    0x266eS0x882: REVERT v266bV882(0x0), v266bV882(0x0)

    Begin block 0x9150x2604B0x882
    prev=[0x2604B0x882], succ=[0x9200x2604B0x882, 0x9290x2604B0x882]
    =================================
    0x9170x2604S0x882: v2604917V882 = GAS 
    0x9180x2604S0x882: v2604918V882 = STATICCALL v2604917V882, v2649V882, v2630V882, v265fV882(0x4), v2630V882, v2657V882(0x20)
    0x9190x2604S0x882: v2604919V882 = ISZERO v2604918V882
    0x91b0x2604S0x882: v260491bV882 = ISZERO v2604919V882
    0x91c0x2604S0x882: v260491cV882(0x929) = CONST 
    0x91f0x2604S0x882: JUMPI v260491cV882(0x929), v260491bV882

    Begin block 0x9200x2604B0x882
    prev=[0x9150x2604B0x882], succ=[]
    =================================
    0x9200x2604S0x882: v2604920V882 = RETURNDATASIZE 
    0x9210x2604S0x882: v2604921V882(0x0) = CONST 
    0x9240x2604S0x882: RETURNDATACOPY v2604921V882(0x0), v2604921V882(0x0), v2604920V882
    0x9250x2604S0x882: v2604925V882 = RETURNDATASIZE 
    0x9260x2604S0x882: v2604926V882(0x0) = CONST 
    0x9280x2604S0x882: REVERT v2604926V882(0x0), v2604925V882

    Begin block 0x9290x2604B0x882
    prev=[0x9150x2604B0x882], succ=[0x93b0x2604B0x882, 0x93f0x2604B0x882]
    =================================
    0x92e0x2604S0x882: v260492eV882(0x40) = CONST 
    0x9300x2604S0x882: v2604930V882 = MLOAD v260492eV882(0x40)
    0x9310x2604S0x882: v2604931V882 = RETURNDATASIZE 
    0x9320x2604S0x882: v2604932V882(0x20) = CONST 
    0x9350x2604S0x882: v2604935V882 = LT v2604931V882, v2604932V882(0x20)
    0x9360x2604S0x882: v2604936V882 = ISZERO v2604935V882
    0x9370x2604S0x882: v2604937V882(0x93f) = CONST 
    0x93a0x2604S0x882: JUMPI v2604937V882(0x93f), v2604936V882

    Begin block 0x93b0x2604B0x882
    prev=[0x9290x2604B0x882], succ=[]
    =================================
    0x93b0x2604S0x882: v260493bV882(0x0) = CONST 
    0x93e0x2604S0x882: REVERT v260493bV882(0x0), v260493bV882(0x0)

    Begin block 0x93f0x2604B0x882
    prev=[0x9290x2604B0x882], succ=[0x9440x2604B0x882]
    =================================
    0x9410x2604S0x882: v2604941V882 = MLOAD v2604930V882

    Begin block 0x9440x2604B0x882
    prev=[0x93f0x2604B0x882], succ=[0x3ca3]
    =================================
    0x9460x2604S0x882: JUMP v883(0x3ca3)

    Begin block 0x3ca3
    prev=[0x9440x2604B0x882], succ=[]
    =================================
    0x3ca4: v3ca4(0x40) = CONST 
    0x3ca7: v3ca7 = MLOAD v3ca4(0x40)
    0x3caa: MSTORE v3ca7, v2604941V882
    0x3cab: v3cab = MLOAD v3ca4(0x40)
    0x3caf: v3caf(0x0) = SUB v3ca7, v3cab
    0x3cb0: v3cb0(0x20) = CONST 
    0x3cb2: v3cb2(0x20) = ADD v3cb0(0x20), v3caf(0x0)
    0x3cb4: RETURN v3cab, v3cb2(0x20)

}

function getDollarUpdatedPrice()() public {
    Begin block 0x88a
    prev=[], succ=[0x3cd4]
    =================================
    0x88b: v88b(0x3cd4) = CONST 
    0x88e: v88e(0x266f) = CONST 
    0x891: v891_0 = CALLPRIVATE v88e(0x266f), v88b(0x3cd4)

    Begin block 0x3cd4
    prev=[0x88a], succ=[]
    =================================
    0x3cd5: v3cd5(0x40) = CONST 
    0x3cd8: v3cd8 = MLOAD v3cd5(0x40)
    0x3cdb: MSTORE v3cd8, v891_0
    0x3cdc: v3cdc = MLOAD v3cd5(0x40)
    0x3ce0: v3ce0(0x0) = SUB v3cd8, v3cdc
    0x3ce1: v3ce1(0x20) = CONST 
    0x3ce3: v3ce3(0x20) = ADD v3ce1(0x20), v3ce0(0x0)
    0x3ce5: RETURN v3cdc, v3ce3(0x20)

}

function premiumPercent()() public {
    Begin block 0x892
    prev=[], succ=[0x277a]
    =================================
    0x893: v893(0x3d05) = CONST 
    0x896: v896(0x277a) = CONST 
    0x899: JUMP v896(0x277a)

    Begin block 0x277a
    prev=[0x892], succ=[0x3d05]
    =================================
    0x277b: v277b(0xb) = CONST 
    0x277d: v277d = SLOAD v277b(0xb)
    0x277f: JUMP v893(0x3d05)

    Begin block 0x3d05
    prev=[0x277a], succ=[]
    =================================
    0x3d06: v3d06(0x40) = CONST 
    0x3d09: v3d09 = MLOAD v3d06(0x40)
    0x3d0c: MSTORE v3d09, v277d
    0x3d0d: v3d0d = MLOAD v3d06(0x40)
    0x3d11: v3d11(0x0) = SUB v3d09, v3d0d
    0x3d12: v3d12(0x20) = CONST 
    0x3d14: v3d14(0x20) = ADD v3d12(0x20), v3d11(0x0)
    0x3d16: RETURN v3d0d, v3d14(0x20)

}

function getCouponDiscountRate()() public {
    Begin block 0x89a
    prev=[], succ=[0x34e0x89a]
    =================================
    0x89b: v89b(0x34e) = CONST 
    0x89e: v89e(0x2780) = CONST 
    0x8a1: v8a1_0 = CALLPRIVATE v89e(0x2780), v89b(0x34e)

    Begin block 0x34e0x89a
    prev=[0x89a], succ=[]
    =================================
    0x34f0x89a: v89a34f(0x40) = CONST 
    0x3520x89a: v89a352 = MLOAD v89a34f(0x40)
    0x3550x89a: MSTORE v89a352, v8a1_0
    0x3560x89a: v89a356 = MLOAD v89a34f(0x40)
    0x35a0x89a: v89a35a(0x0) = SUB v89a352, v89a356
    0x35b0x89a: v89a35b(0x20) = CONST 
    0x35d0x89a: v89a35d(0x20) = ADD v89a35b(0x20), v89a35a(0x0)
    0x35f0x89a: RETURN v89a356, v89a35d(0x20)

}

function getDollarPrice()() public {
    Begin block 0x8a2
    prev=[], succ=[0x3d36]
    =================================
    0x8a3: v8a3(0x3d36) = CONST 
    0x8a6: v8a6(0x282f) = CONST 
    0x8a9: v8a9_0 = CALLPRIVATE v8a6(0x282f), v8a3(0x3d36)

    Begin block 0x3d36
    prev=[0x8a2], succ=[]
    =================================
    0x3d37: v3d37(0x40) = CONST 
    0x3d3a: v3d3a = MLOAD v3d37(0x40)
    0x3d3d: MSTORE v3d3a, v8a9_0
    0x3d3e: v3d3e = MLOAD v3d37(0x40)
    0x3d42: v3d42(0x0) = SUB v3d3a, v3d3e
    0x3d43: v3d43(0x20) = CONST 
    0x3d45: v3d45(0x20) = ADD v3d43(0x20), v3d42(0x0)
    0x3d47: RETURN v3d3e, v3d45(0x20)

}

