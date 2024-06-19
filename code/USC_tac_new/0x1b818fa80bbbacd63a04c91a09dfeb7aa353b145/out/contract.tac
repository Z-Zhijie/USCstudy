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
    prev=[0x0], succ=[0x1a, 0x3432]
    =================================
    0x12: v12(0x4) = CONST 
    0x14: v14 = CALLDATASIZE 
    0x15: v15 = LT v14, v12(0x4)
    0x32af: v32af(0x3432) = CONST 
    0x32b0: JUMPI v32af(0x3432), v15

    Begin block 0x1a
    prev=[0x10], succ=[0x1de, 0x2b]
    =================================
    0x1a: v1a(0x0) = CONST 
    0x1c: v1c = CALLDATALOAD v1a(0x0)
    0x1d: v1d(0xe0) = CONST 
    0x1f: v1f = SHR v1d(0xe0), v1c
    0x21: v21(0x7bc2aaf1) = CONST 
    0x26: v26 = GT v21(0x7bc2aaf1), v1f
    0x27: v27(0x1de) = CONST 
    0x2a: JUMPI v27(0x1de), v26

    Begin block 0x1de
    prev=[0x1a], succ=[0x2c3, 0x1ea]
    =================================
    0x1e0: v1e0(0x3b1fa43c) = CONST 
    0x1e5: v1e5 = GT v1e0(0x3b1fa43c), v1f
    0x1e6: v1e6(0x2c3) = CONST 
    0x1e9: JUMPI v1e6(0x2c3), v1e5

    Begin block 0x2c3
    prev=[0x1de], succ=[0x330, 0x2cf]
    =================================
    0x2c5: v2c5(0x2133bbcf) = CONST 
    0x2ca: v2ca = GT v2c5(0x2133bbcf), v1f
    0x2cb: v2cb(0x330) = CONST 
    0x2ce: JUMPI v2cb(0x330), v2ca

    Begin block 0x330
    prev=[0x2c3], succ=[0x36c, 0x33c]
    =================================
    0x332: v332(0x13af4035) = CONST 
    0x337: v337 = GT v332(0x13af4035), v1f
    0x338: v338(0x36c) = CONST 
    0x33b: JUMPI v338(0x36c), v337

    Begin block 0x36c
    prev=[0x330], succ=[0x3325, 0x377]
    =================================
    0x36e: v36e(0x7e922d) = CONST 
    0x372: v372 = EQ v36e(0x7e922d), v1f
    0x331f: v331f(0x3325) = CONST 
    0x3320: JUMPI v331f(0x3325), v372

    Begin block 0x3325
    prev=[0x36c], succ=[]
    =================================
    0x3326: v3326(0x392) = CONST 
    0x3327: CALLPRIVATE v3326(0x392)

    Begin block 0x377
    prev=[0x36c], succ=[0x3328, 0x382]
    =================================
    0x378: v378(0x3a74dc2) = CONST 
    0x37d: v37d = EQ v378(0x3a74dc2), v1f
    0x3321: v3321(0x3328) = CONST 
    0x3322: JUMPI v3321(0x3328), v37d

    Begin block 0x3328
    prev=[0x377], succ=[]
    =================================
    0x3329: v3329(0x3ac) = CONST 
    0x332a: CALLPRIVATE v3329(0x3ac)

    Begin block 0x382
    prev=[0x377], succ=[0x332b, 0x38d]
    =================================
    0x383: v383(0x4707715) = CONST 
    0x388: v388 = EQ v383(0x4707715), v1f
    0x3323: v3323(0x332b) = CONST 
    0x3324: JUMPI v3323(0x332b), v388

    Begin block 0x332b
    prev=[0x382], succ=[]
    =================================
    0x332c: v332c(0x3b4) = CONST 
    0x332d: CALLPRIVATE v332c(0x3b4)

    Begin block 0x38d
    prev=[0x382], succ=[]
    =================================
    0x38e: v38e(0x0) = CONST 
    0x391: REVERT v38e(0x0), v38e(0x0)

    Begin block 0x33c
    prev=[0x330], succ=[0x332e, 0x347]
    =================================
    0x33d: v33d(0x13af4035) = CONST 
    0x342: v342 = EQ v33d(0x13af4035), v1f
    0x3317: v3317(0x332e) = CONST 
    0x3318: JUMPI v3317(0x332e), v342

    Begin block 0x332e
    prev=[0x33c], succ=[]
    =================================
    0x332f: v332f(0x3bc) = CONST 
    0x3330: CALLPRIVATE v332f(0x3bc)

    Begin block 0x347
    prev=[0x33c], succ=[0x3331, 0x352]
    =================================
    0x348: v348(0x1affbd97) = CONST 
    0x34d: v34d = EQ v348(0x1affbd97), v1f
    0x3319: v3319(0x3331) = CONST 
    0x331a: JUMPI v3319(0x3331), v34d

    Begin block 0x3331
    prev=[0x347], succ=[]
    =================================
    0x3332: v3332(0x3e4) = CONST 
    0x3333: CALLPRIVATE v3332(0x3e4)

    Begin block 0x352
    prev=[0x347], succ=[0x3334, 0x35d]
    =================================
    0x353: v353(0x1b31f54a) = CONST 
    0x358: v358 = EQ v353(0x1b31f54a), v1f
    0x331b: v331b(0x3334) = CONST 
    0x331c: JUMPI v331b(0x3334), v358

    Begin block 0x3334
    prev=[0x352], succ=[]
    =================================
    0x3335: v3335(0x40b) = CONST 
    0x3336: CALLPRIVATE v3335(0x40b)

    Begin block 0x35d
    prev=[0x352], succ=[0x368, 0x3337]
    =================================
    0x35e: v35e(0x1bb25390) = CONST 
    0x363: v363 = EQ v35e(0x1bb25390), v1f
    0x331d: v331d(0x3337) = CONST 
    0x331e: JUMPI v331d(0x3337), v363

    Begin block 0x368
    prev=[0x35d], succ=[0x2686]
    =================================
    0x368: v368(0x2686) = CONST 
    0x36b: JUMP v368(0x2686)

    Begin block 0x2686
    prev=[0x368], succ=[]
    =================================
    0x2687: v2687(0x0) = CONST 
    0x268a: REVERT v2687(0x0), v2687(0x0)

    Begin block 0x3337
    prev=[0x35d], succ=[]
    =================================
    0x3338: v3338(0x413) = CONST 
    0x3339: CALLPRIVATE v3338(0x413)

    Begin block 0x2cf
    prev=[0x2c3], succ=[0x30a, 0x2da]
    =================================
    0x2d0: v2d0(0x30ec03d3) = CONST 
    0x2d5: v2d5 = GT v2d0(0x30ec03d3), v1f
    0x2d6: v2d6(0x30a) = CONST 
    0x2d9: JUMPI v2d6(0x30a), v2d5

    Begin block 0x30a
    prev=[0x2cf], succ=[0x333a, 0x316]
    =================================
    0x30c: v30c(0x2133bbcf) = CONST 
    0x311: v311 = EQ v30c(0x2133bbcf), v1f
    0x3311: v3311(0x333a) = CONST 
    0x3312: JUMPI v3311(0x333a), v311

    Begin block 0x333a
    prev=[0x30a], succ=[]
    =================================
    0x333b: v333b(0x450) = CONST 
    0x333c: CALLPRIVATE v333b(0x450)

    Begin block 0x316
    prev=[0x30a], succ=[0x333d, 0x321]
    =================================
    0x317: v317(0x230b7adc) = CONST 
    0x31c: v31c = EQ v317(0x230b7adc), v1f
    0x3313: v3313(0x333d) = CONST 
    0x3314: JUMPI v3313(0x333d), v31c

    Begin block 0x333d
    prev=[0x316], succ=[]
    =================================
    0x333e: v333e(0x458) = CONST 
    0x333f: CALLPRIVATE v333e(0x458)

    Begin block 0x321
    prev=[0x316], succ=[0x32c, 0x3340]
    =================================
    0x322: v322(0x2b3ba681) = CONST 
    0x327: v327 = EQ v322(0x2b3ba681), v1f
    0x3315: v3315(0x3340) = CONST 
    0x3316: JUMPI v3315(0x3340), v327

    Begin block 0x32c
    prev=[0x321], succ=[0x2662]
    =================================
    0x32c: v32c(0x2662) = CONST 
    0x32f: JUMP v32c(0x2662)

    Begin block 0x2662
    prev=[0x32c], succ=[]
    =================================
    0x2663: v2663(0x0) = CONST 
    0x2666: REVERT v2663(0x0), v2663(0x0)

    Begin block 0x3340
    prev=[0x321], succ=[]
    =================================
    0x3341: v3341(0x460) = CONST 
    0x3342: CALLPRIVATE v3341(0x460)

    Begin block 0x2da
    prev=[0x2cf], succ=[0x3343, 0x2e5]
    =================================
    0x2db: v2db(0x30ec03d3) = CONST 
    0x2e0: v2e0 = EQ v2db(0x30ec03d3), v1f
    0x3309: v3309(0x3343) = CONST 
    0x330a: JUMPI v3309(0x3343), v2e0

    Begin block 0x3343
    prev=[0x2da], succ=[]
    =================================
    0x3344: v3344(0x48d) = CONST 
    0x3345: CALLPRIVATE v3344(0x48d)

    Begin block 0x2e5
    prev=[0x2da], succ=[0x3346, 0x2f0]
    =================================
    0x2e6: v2e6(0x3133f084) = CONST 
    0x2eb: v2eb = EQ v2e6(0x3133f084), v1f
    0x330b: v330b(0x3346) = CONST 
    0x330c: JUMPI v330b(0x3346), v2eb

    Begin block 0x3346
    prev=[0x2e5], succ=[]
    =================================
    0x3347: v3347(0x4bd) = CONST 
    0x3348: CALLPRIVATE v3347(0x4bd)

    Begin block 0x2f0
    prev=[0x2e5], succ=[0x3349, 0x2fb]
    =================================
    0x2f1: v2f1(0x33281815) = CONST 
    0x2f6: v2f6 = EQ v2f1(0x33281815), v1f
    0x330d: v330d(0x3349) = CONST 
    0x330e: JUMPI v330d(0x3349), v2f6

    Begin block 0x3349
    prev=[0x2f0], succ=[]
    =================================
    0x334a: v334a(0x4c5) = CONST 
    0x334b: CALLPRIVATE v334a(0x4c5)

    Begin block 0x2fb
    prev=[0x2f0], succ=[0x306, 0x334c]
    =================================
    0x2fc: v2fc(0x341f5fc9) = CONST 
    0x301: v301 = EQ v2fc(0x341f5fc9), v1f
    0x330f: v330f(0x334c) = CONST 
    0x3310: JUMPI v330f(0x334c), v301

    Begin block 0x306
    prev=[0x2fb], succ=[0x263e]
    =================================
    0x306: v306(0x263e) = CONST 
    0x309: JUMP v306(0x263e)

    Begin block 0x263e
    prev=[0x306], succ=[]
    =================================
    0x263f: v263f(0x0) = CONST 
    0x2642: REVERT v263f(0x0), v263f(0x0)

    Begin block 0x334c
    prev=[0x2fb], succ=[]
    =================================
    0x334d: v334d(0x4f7) = CONST 
    0x334e: CALLPRIVATE v334d(0x4f7)

    Begin block 0x1ea
    prev=[0x1de], succ=[0x261, 0x1f5]
    =================================
    0x1eb: v1eb(0x607b6858) = CONST 
    0x1f0: v1f0 = GT v1eb(0x607b6858), v1f
    0x1f1: v1f1(0x261) = CONST 
    0x1f4: JUMPI v1f1(0x261), v1f0

    Begin block 0x261
    prev=[0x1ea], succ=[0x29d, 0x26d]
    =================================
    0x263: v263(0x572e3543) = CONST 
    0x268: v268 = GT v263(0x572e3543), v1f
    0x269: v269(0x29d) = CONST 
    0x26c: JUMPI v269(0x29d), v268

    Begin block 0x29d
    prev=[0x261], succ=[0x334f, 0x2a9]
    =================================
    0x29f: v29f(0x3b1fa43c) = CONST 
    0x2a4: v2a4 = EQ v29f(0x3b1fa43c), v1f
    0x3303: v3303(0x334f) = CONST 
    0x3304: JUMPI v3303(0x334f), v2a4

    Begin block 0x334f
    prev=[0x29d], succ=[]
    =================================
    0x3350: v3350(0x4ff) = CONST 
    0x3351: CALLPRIVATE v3350(0x4ff)

    Begin block 0x2a9
    prev=[0x29d], succ=[0x3352, 0x2b4]
    =================================
    0x2aa: v2aa(0x3bf31254) = CONST 
    0x2af: v2af = EQ v2aa(0x3bf31254), v1f
    0x3305: v3305(0x3352) = CONST 
    0x3306: JUMPI v3305(0x3352), v2af

    Begin block 0x3352
    prev=[0x2a9], succ=[]
    =================================
    0x3353: v3353(0x507) = CONST 
    0x3354: CALLPRIVATE v3353(0x507)

    Begin block 0x2b4
    prev=[0x2a9], succ=[0x2bf, 0x3355]
    =================================
    0x2b5: v2b5(0x474a74a9) = CONST 
    0x2ba: v2ba = EQ v2b5(0x474a74a9), v1f
    0x3307: v3307(0x3355) = CONST 
    0x3308: JUMPI v3307(0x3355), v2ba

    Begin block 0x2bf
    prev=[0x2b4], succ=[0x261a]
    =================================
    0x2bf: v2bf(0x261a) = CONST 
    0x2c2: JUMP v2bf(0x261a)

    Begin block 0x261a
    prev=[0x2bf], succ=[]
    =================================
    0x261b: v261b(0x0) = CONST 
    0x261e: REVERT v261b(0x0), v261b(0x0)

    Begin block 0x3355
    prev=[0x2b4], succ=[]
    =================================
    0x3356: v3356(0x50f) = CONST 
    0x3357: CALLPRIVATE v3356(0x50f)

    Begin block 0x26d
    prev=[0x261], succ=[0x3358, 0x278]
    =================================
    0x26e: v26e(0x572e3543) = CONST 
    0x273: v273 = EQ v26e(0x572e3543), v1f
    0x32fb: v32fb(0x3358) = CONST 
    0x32fc: JUMPI v32fb(0x3358), v273

    Begin block 0x3358
    prev=[0x26d], succ=[]
    =================================
    0x3359: v3359(0x52d) = CONST 
    0x335a: CALLPRIVATE v3359(0x52d)

    Begin block 0x278
    prev=[0x26d], succ=[0x335b, 0x283]
    =================================
    0x279: v279(0x57933f9d) = CONST 
    0x27e: v27e = EQ v279(0x57933f9d), v1f
    0x32fd: v32fd(0x335b) = CONST 
    0x32fe: JUMPI v32fd(0x335b), v27e

    Begin block 0x335b
    prev=[0x278], succ=[]
    =================================
    0x335c: v335c(0x535) = CONST 
    0x335d: CALLPRIVATE v335c(0x535)

    Begin block 0x283
    prev=[0x278], succ=[0x335e, 0x28e]
    =================================
    0x284: v284(0x5d4a2f92) = CONST 
    0x289: v289 = EQ v284(0x5d4a2f92), v1f
    0x32ff: v32ff(0x335e) = CONST 
    0x3300: JUMPI v32ff(0x335e), v289

    Begin block 0x335e
    prev=[0x283], succ=[]
    =================================
    0x335f: v335f(0x53d) = CONST 
    0x3360: CALLPRIVATE v335f(0x53d)

    Begin block 0x28e
    prev=[0x283], succ=[0x299, 0x3361]
    =================================
    0x28f: v28f(0x5fb1900b) = CONST 
    0x294: v294 = EQ v28f(0x5fb1900b), v1f
    0x3301: v3301(0x3361) = CONST 
    0x3302: JUMPI v3301(0x3361), v294

    Begin block 0x299
    prev=[0x28e], succ=[0x25f6]
    =================================
    0x299: v299(0x25f6) = CONST 
    0x29c: JUMP v299(0x25f6)

    Begin block 0x25f6
    prev=[0x299], succ=[]
    =================================
    0x25f7: v25f7(0x0) = CONST 
    0x25fa: REVERT v25f7(0x0), v25f7(0x0)

    Begin block 0x3361
    prev=[0x28e], succ=[]
    =================================
    0x3362: v3362(0x545) = CONST 
    0x3363: CALLPRIVATE v3362(0x545)

    Begin block 0x1f5
    prev=[0x1ea], succ=[0x230, 0x200]
    =================================
    0x1f6: v1f6(0x6de0cd8b) = CONST 
    0x1fb: v1fb = GT v1f6(0x6de0cd8b), v1f
    0x1fc: v1fc(0x230) = CONST 
    0x1ff: JUMPI v1fc(0x230), v1fb

    Begin block 0x230
    prev=[0x1f5], succ=[0x3364, 0x23c]
    =================================
    0x232: v232(0x607b6858) = CONST 
    0x237: v237 = EQ v232(0x607b6858), v1f
    0x32f3: v32f3(0x3364) = CONST 
    0x32f4: JUMPI v32f3(0x3364), v237

    Begin block 0x3364
    prev=[0x230], succ=[]
    =================================
    0x3365: v3365(0x54d) = CONST 
    0x3366: CALLPRIVATE v3365(0x54d)

    Begin block 0x23c
    prev=[0x230], succ=[0x3367, 0x247]
    =================================
    0x23d: v23d(0x61b39d48) = CONST 
    0x242: v242 = EQ v23d(0x61b39d48), v1f
    0x32f5: v32f5(0x3367) = CONST 
    0x32f6: JUMPI v32f5(0x3367), v242

    Begin block 0x3367
    prev=[0x23c], succ=[]
    =================================
    0x3368: v3368(0x555) = CONST 
    0x3369: CALLPRIVATE v3368(0x555)

    Begin block 0x247
    prev=[0x23c], succ=[0x336a, 0x252]
    =================================
    0x248: v248(0x65a11acb) = CONST 
    0x24d: v24d = EQ v248(0x65a11acb), v1f
    0x32f7: v32f7(0x336a) = CONST 
    0x32f8: JUMPI v32f7(0x336a), v24d

    Begin block 0x336a
    prev=[0x247], succ=[]
    =================================
    0x336b: v336b(0x55d) = CONST 
    0x336c: CALLPRIVATE v336b(0x55d)

    Begin block 0x252
    prev=[0x247], succ=[0x25d, 0x336d]
    =================================
    0x253: v253(0x6bf79fd1) = CONST 
    0x258: v258 = EQ v253(0x6bf79fd1), v1f
    0x32f9: v32f9(0x336d) = CONST 
    0x32fa: JUMPI v32f9(0x336d), v258

    Begin block 0x25d
    prev=[0x252], succ=[0x25d2]
    =================================
    0x25d: v25d(0x25d2) = CONST 
    0x260: JUMP v25d(0x25d2)

    Begin block 0x25d2
    prev=[0x25d], succ=[]
    =================================
    0x25d3: v25d3(0x0) = CONST 
    0x25d6: REVERT v25d3(0x0), v25d3(0x0)

    Begin block 0x336d
    prev=[0x252], succ=[]
    =================================
    0x336e: v336e(0x584) = CONST 
    0x336f: CALLPRIVATE v336e(0x584)

    Begin block 0x200
    prev=[0x1f5], succ=[0x3370, 0x20b]
    =================================
    0x201: v201(0x6de0cd8b) = CONST 
    0x206: v206 = EQ v201(0x6de0cd8b), v1f
    0x32eb: v32eb(0x3370) = CONST 
    0x32ec: JUMPI v32eb(0x3370), v206

    Begin block 0x3370
    prev=[0x200], succ=[]
    =================================
    0x3371: v3371(0x58c) = CONST 
    0x3372: CALLPRIVATE v3371(0x58c)

    Begin block 0x20b
    prev=[0x200], succ=[0x3373, 0x216]
    =================================
    0x20c: v20c(0x75e5826e) = CONST 
    0x211: v211 = EQ v20c(0x75e5826e), v1f
    0x32ed: v32ed(0x3373) = CONST 
    0x32ee: JUMPI v32ed(0x3373), v211

    Begin block 0x3373
    prev=[0x20b], succ=[]
    =================================
    0x3374: v3374(0x5b8) = CONST 
    0x3375: CALLPRIVATE v3374(0x5b8)

    Begin block 0x216
    prev=[0x20b], succ=[0x3376, 0x221]
    =================================
    0x217: v217(0x7a9e5e4b) = CONST 
    0x21c: v21c = EQ v217(0x7a9e5e4b), v1f
    0x32ef: v32ef(0x3376) = CONST 
    0x32f0: JUMPI v32ef(0x3376), v21c

    Begin block 0x3376
    prev=[0x216], succ=[]
    =================================
    0x3377: v3377(0x5c0) = CONST 
    0x3378: CALLPRIVATE v3377(0x5c0)

    Begin block 0x221
    prev=[0x216], succ=[0x22c, 0x3379]
    =================================
    0x222: v222(0x7b103999) = CONST 
    0x227: v227 = EQ v222(0x7b103999), v1f
    0x32f1: v32f1(0x3379) = CONST 
    0x32f2: JUMPI v32f1(0x3379), v227

    Begin block 0x22c
    prev=[0x221], succ=[0x25ae]
    =================================
    0x22c: v22c(0x25ae) = CONST 
    0x22f: JUMP v22c(0x25ae)

    Begin block 0x25ae
    prev=[0x22c], succ=[]
    =================================
    0x25af: v25af(0x0) = CONST 
    0x25b2: REVERT v25af(0x0), v25af(0x0)

    Begin block 0x3379
    prev=[0x221], succ=[]
    =================================
    0x337a: v337a(0x5e6) = CONST 
    0x337b: CALLPRIVATE v337a(0x5e6)

    Begin block 0x2b
    prev=[0x1a], succ=[0x10f, 0x36]
    =================================
    0x2c: v2c(0xa91346b6) = CONST 
    0x31: v31 = GT v2c(0xa91346b6), v1f
    0x32: v32(0x10f) = CONST 
    0x35: JUMPI v32(0x10f), v31

    Begin block 0x10f
    prev=[0x2b], succ=[0x17c, 0x11b]
    =================================
    0x111: v111(0x88525548) = CONST 
    0x116: v116 = GT v111(0x88525548), v1f
    0x117: v117(0x17c) = CONST 
    0x11a: JUMPI v117(0x17c), v116

    Begin block 0x17c
    prev=[0x10f], succ=[0x1b8, 0x188]
    =================================
    0x17e: v17e(0x8134d30d) = CONST 
    0x183: v183 = GT v17e(0x8134d30d), v1f
    0x184: v184(0x1b8) = CONST 
    0x187: JUMPI v184(0x1b8), v183

    Begin block 0x1b8
    prev=[0x17c], succ=[0x337c, 0x1c4]
    =================================
    0x1ba: v1ba(0x7bc2aaf1) = CONST 
    0x1bf: v1bf = EQ v1ba(0x7bc2aaf1), v1f
    0x32e5: v32e5(0x337c) = CONST 
    0x32e6: JUMPI v32e5(0x337c), v1bf

    Begin block 0x337c
    prev=[0x1b8], succ=[]
    =================================
    0x337d: v337d(0x60a) = CONST 
    0x337e: CALLPRIVATE v337d(0x60a)

    Begin block 0x1c4
    prev=[0x1b8], succ=[0x337f, 0x1cf]
    =================================
    0x1c5: v1c5(0x7fb2c9d9) = CONST 
    0x1ca: v1ca = EQ v1c5(0x7fb2c9d9), v1f
    0x32e7: v32e7(0x337f) = CONST 
    0x32e8: JUMPI v32e7(0x337f), v1ca

    Begin block 0x337f
    prev=[0x1c4], succ=[]
    =================================
    0x3380: v3380(0x612) = CONST 
    0x3381: CALLPRIVATE v3380(0x612)

    Begin block 0x1cf
    prev=[0x1c4], succ=[0x1da, 0x3382]
    =================================
    0x1d0: v1d0(0x7ff0a3a6) = CONST 
    0x1d5: v1d5 = EQ v1d0(0x7ff0a3a6), v1f
    0x32e9: v32e9(0x3382) = CONST 
    0x32ea: JUMPI v32e9(0x3382), v1d5

    Begin block 0x1da
    prev=[0x1cf], succ=[0x258a]
    =================================
    0x1da: v1da(0x258a) = CONST 
    0x1dd: JUMP v1da(0x258a)

    Begin block 0x258a
    prev=[0x1da], succ=[]
    =================================
    0x258b: v258b(0x0) = CONST 
    0x258e: REVERT v258b(0x0), v258b(0x0)

    Begin block 0x3382
    prev=[0x1cf], succ=[]
    =================================
    0x3383: v3383(0x61a) = CONST 
    0x3384: CALLPRIVATE v3383(0x61a)

    Begin block 0x188
    prev=[0x17c], succ=[0x3385, 0x193]
    =================================
    0x189: v189(0x8134d30d) = CONST 
    0x18e: v18e = EQ v189(0x8134d30d), v1f
    0x32dd: v32dd(0x3385) = CONST 
    0x32de: JUMPI v32dd(0x3385), v18e

    Begin block 0x3385
    prev=[0x188], succ=[]
    =================================
    0x3386: v3386(0x622) = CONST 
    0x3387: CALLPRIVATE v3386(0x622)

    Begin block 0x193
    prev=[0x188], succ=[0x3388, 0x19e]
    =================================
    0x194: v194(0x840ee967) = CONST 
    0x199: v199 = EQ v194(0x840ee967), v1f
    0x32df: v32df(0x3388) = CONST 
    0x32e0: JUMPI v32df(0x3388), v199

    Begin block 0x3388
    prev=[0x193], succ=[]
    =================================
    0x3389: v3389(0x657) = CONST 
    0x338a: CALLPRIVATE v3389(0x657)

    Begin block 0x19e
    prev=[0x193], succ=[0x338b, 0x1a9]
    =================================
    0x19f: v19f(0x84f37a3d) = CONST 
    0x1a4: v1a4 = EQ v19f(0x84f37a3d), v1f
    0x32e1: v32e1(0x338b) = CONST 
    0x32e2: JUMPI v32e1(0x338b), v1a4

    Begin block 0x338b
    prev=[0x19e], succ=[]
    =================================
    0x338c: v338c(0x683) = CONST 
    0x338d: CALLPRIVATE v338c(0x683)

    Begin block 0x1a9
    prev=[0x19e], succ=[0x1b4, 0x338e]
    =================================
    0x1aa: v1aa(0x8847037d) = CONST 
    0x1af: v1af = EQ v1aa(0x8847037d), v1f
    0x32e3: v32e3(0x338e) = CONST 
    0x32e4: JUMPI v32e3(0x338e), v1af

    Begin block 0x1b4
    prev=[0x1a9], succ=[0x2566]
    =================================
    0x1b4: v1b4(0x2566) = CONST 
    0x1b7: JUMP v1b4(0x2566)

    Begin block 0x2566
    prev=[0x1b4], succ=[]
    =================================
    0x2567: v2567(0x0) = CONST 
    0x256a: REVERT v2567(0x0), v2567(0x0)

    Begin block 0x338e
    prev=[0x1a9], succ=[]
    =================================
    0x338f: v338f(0x68b) = CONST 
    0x3390: CALLPRIVATE v338f(0x68b)

    Begin block 0x11b
    prev=[0x10f], succ=[0x156, 0x126]
    =================================
    0x11c: v11c(0x8da5cb5b) = CONST 
    0x121: v121 = GT v11c(0x8da5cb5b), v1f
    0x122: v122(0x156) = CONST 
    0x125: JUMPI v122(0x156), v121

    Begin block 0x156
    prev=[0x11b], succ=[0x3391, 0x162]
    =================================
    0x158: v158(0x88525548) = CONST 
    0x15d: v15d = EQ v158(0x88525548), v1f
    0x32d7: v32d7(0x3391) = CONST 
    0x32d8: JUMPI v32d7(0x3391), v15d

    Begin block 0x3391
    prev=[0x156], succ=[]
    =================================
    0x3392: v3392(0x693) = CONST 
    0x3393: CALLPRIVATE v3392(0x693)

    Begin block 0x162
    prev=[0x156], succ=[0x3394, 0x16d]
    =================================
    0x163: v163(0x8aecbc17) = CONST 
    0x168: v168 = EQ v163(0x8aecbc17), v1f
    0x32d9: v32d9(0x3394) = CONST 
    0x32da: JUMPI v32d9(0x3394), v168

    Begin block 0x3394
    prev=[0x162], succ=[]
    =================================
    0x3395: v3395(0x69b) = CONST 
    0x3396: CALLPRIVATE v3395(0x69b)

    Begin block 0x16d
    prev=[0x162], succ=[0x178, 0x3397]
    =================================
    0x16e: v16e(0x8b7ee7e4) = CONST 
    0x173: v173 = EQ v16e(0x8b7ee7e4), v1f
    0x32db: v32db(0x3397) = CONST 
    0x32dc: JUMPI v32db(0x3397), v173

    Begin block 0x178
    prev=[0x16d], succ=[0x2542]
    =================================
    0x178: v178(0x2542) = CONST 
    0x17b: JUMP v178(0x2542)

    Begin block 0x2542
    prev=[0x178], succ=[]
    =================================
    0x2543: v2543(0x0) = CONST 
    0x2546: REVERT v2543(0x0), v2543(0x0)

    Begin block 0x3397
    prev=[0x16d], succ=[]
    =================================
    0x3398: v3398(0x6b8) = CONST 
    0x3399: CALLPRIVATE v3398(0x6b8)

    Begin block 0x126
    prev=[0x11b], succ=[0x339a, 0x131]
    =================================
    0x127: v127(0x8da5cb5b) = CONST 
    0x12c: v12c = EQ v127(0x8da5cb5b), v1f
    0x32cf: v32cf(0x339a) = CONST 
    0x32d0: JUMPI v32cf(0x339a), v12c

    Begin block 0x339a
    prev=[0x126], succ=[]
    =================================
    0x339b: v339b(0x6c0) = CONST 
    0x339c: CALLPRIVATE v339b(0x6c0)

    Begin block 0x131
    prev=[0x126], succ=[0x339d, 0x13c]
    =================================
    0x132: v132(0x9434a4fa) = CONST 
    0x137: v137 = EQ v132(0x9434a4fa), v1f
    0x32d1: v32d1(0x339d) = CONST 
    0x32d2: JUMPI v32d1(0x339d), v137

    Begin block 0x339d
    prev=[0x131], succ=[]
    =================================
    0x339e: v339e(0x6c8) = CONST 
    0x339f: CALLPRIVATE v339e(0x6c8)

    Begin block 0x13c
    prev=[0x131], succ=[0x33a0, 0x147]
    =================================
    0x13d: v13d(0x9edaab7f) = CONST 
    0x142: v142 = EQ v13d(0x9edaab7f), v1f
    0x32d3: v32d3(0x33a0) = CONST 
    0x32d4: JUMPI v32d3(0x33a0), v142

    Begin block 0x33a0
    prev=[0x13c], succ=[]
    =================================
    0x33a1: v33a1(0x6ef) = CONST 
    0x33a2: CALLPRIVATE v33a1(0x6ef)

    Begin block 0x147
    prev=[0x13c], succ=[0x152, 0x33a3]
    =================================
    0x148: v148(0xa22709e4) = CONST 
    0x14d: v14d = EQ v148(0xa22709e4), v1f
    0x32d5: v32d5(0x33a3) = CONST 
    0x32d6: JUMPI v32d5(0x33a3), v14d

    Begin block 0x152
    prev=[0x147], succ=[0x251e]
    =================================
    0x152: v152(0x251e) = CONST 
    0x155: JUMP v152(0x251e)

    Begin block 0x251e
    prev=[0x152], succ=[]
    =================================
    0x251f: v251f(0x0) = CONST 
    0x2522: REVERT v251f(0x0), v251f(0x0)

    Begin block 0x33a3
    prev=[0x147], succ=[]
    =================================
    0x33a4: v33a4(0x6f7) = CONST 
    0x33a5: CALLPRIVATE v33a4(0x6f7)

    Begin block 0x36
    prev=[0x2b], succ=[0xad, 0x41]
    =================================
    0x37: v37(0xbf7e214f) = CONST 
    0x3c: v3c = GT v37(0xbf7e214f), v1f
    0x3d: v3d(0xad) = CONST 
    0x40: JUMPI v3d(0xad), v3c

    Begin block 0xad
    prev=[0x36], succ=[0xe9, 0xb9]
    =================================
    0xaf: vaf(0xb15762e8) = CONST 
    0xb4: vb4 = GT vaf(0xb15762e8), v1f
    0xb5: vb5(0xe9) = CONST 
    0xb8: JUMPI vb5(0xe9), vb4

    Begin block 0xe9
    prev=[0xad], succ=[0x33a6, 0xf5]
    =================================
    0xeb: veb(0xa91346b6) = CONST 
    0xf0: vf0 = EQ veb(0xa91346b6), v1f
    0x32c9: v32c9(0x33a6) = CONST 
    0x32ca: JUMPI v32c9(0x33a6), vf0

    Begin block 0x33a6
    prev=[0xe9], succ=[]
    =================================
    0x33a7: v33a7(0x6ff) = CONST 
    0x33a8: CALLPRIVATE v33a7(0x6ff)

    Begin block 0xf5
    prev=[0xe9], succ=[0x100, 0x33a9]
    =================================
    0xf6: vf6(0xaa62a812) = CONST 
    0xfb: vfb = EQ vf6(0xaa62a812), v1f
    0x32cb: v32cb(0x33a9) = CONST 
    0x32cc: JUMPI v32cb(0x33a9), vfb

    Begin block 0x100
    prev=[0xf5], succ=[0x10b, 0x33ac]
    =================================
    0x101: v101(0xb0f899dd) = CONST 
    0x106: v106 = EQ v101(0xb0f899dd), v1f
    0x32cd: v32cd(0x33ac) = CONST 
    0x32ce: JUMPI v32cd(0x33ac), v106

    Begin block 0x10b
    prev=[0x100], succ=[0x24fa]
    =================================
    0x10b: v10b(0x24fa) = CONST 
    0x10e: JUMP v10b(0x24fa)

    Begin block 0x24fa
    prev=[0x10b], succ=[]
    =================================
    0x24fb: v24fb(0x0) = CONST 
    0x24fe: REVERT v24fb(0x0), v24fb(0x0)

    Begin block 0x33ac
    prev=[0x100], succ=[]
    =================================
    0x33ad: v33ad(0x70f) = CONST 
    0x33ae: CALLPRIVATE v33ad(0x70f)

    Begin block 0x33a9
    prev=[0xf5], succ=[]
    =================================
    0x33aa: v33aa(0x707) = CONST 
    0x33ab: CALLPRIVATE v33aa(0x707)

    Begin block 0xb9
    prev=[0xad], succ=[0x33af, 0xc4]
    =================================
    0xba: vba(0xb15762e8) = CONST 
    0xbf: vbf = EQ vba(0xb15762e8), v1f
    0x32c1: v32c1(0x33af) = CONST 
    0x32c2: JUMPI v32c1(0x33af), vbf

    Begin block 0x33af
    prev=[0xb9], succ=[]
    =================================
    0x33b0: v33b0(0x717) = CONST 
    0x33b1: CALLPRIVATE v33b0(0x717)

    Begin block 0xc4
    prev=[0xb9], succ=[0x33b2, 0xcf]
    =================================
    0xc5: vc5(0xb71dce2a) = CONST 
    0xca: vca = EQ vc5(0xb71dce2a), v1f
    0x32c3: v32c3(0x33b2) = CONST 
    0x32c4: JUMPI v32c3(0x33b2), vca

    Begin block 0x33b2
    prev=[0xc4], succ=[]
    =================================
    0x33b3: v33b3(0x743) = CONST 
    0x33b4: CALLPRIVATE v33b3(0x743)

    Begin block 0xcf
    prev=[0xc4], succ=[0x33b5, 0xda]
    =================================
    0xd0: vd0(0xb88c6661) = CONST 
    0xd5: vd5 = EQ vd0(0xb88c6661), v1f
    0x32c5: v32c5(0x33b5) = CONST 
    0x32c6: JUMPI v32c5(0x33b5), vd5

    Begin block 0x33b5
    prev=[0xcf], succ=[]
    =================================
    0x33b6: v33b6(0x74b) = CONST 
    0x33b7: CALLPRIVATE v33b6(0x74b)

    Begin block 0xda
    prev=[0xcf], succ=[0xe5, 0x33b8]
    =================================
    0xdb: vdb(0xbba38b85) = CONST 
    0xe0: ve0 = EQ vdb(0xbba38b85), v1f
    0x32c7: v32c7(0x33b8) = CONST 
    0x32c8: JUMPI v32c7(0x33b8), ve0

    Begin block 0xe5
    prev=[0xda], succ=[0x24d6]
    =================================
    0xe5: ve5(0x24d6) = CONST 
    0xe8: JUMP ve5(0x24d6)

    Begin block 0x24d6
    prev=[0xe5], succ=[]
    =================================
    0x24d7: v24d7(0x0) = CONST 
    0x24da: REVERT v24d7(0x0), v24d7(0x0)

    Begin block 0x33b8
    prev=[0xda], succ=[]
    =================================
    0x33b9: v33b9(0x753) = CONST 
    0x33ba: CALLPRIVATE v33b9(0x753)

    Begin block 0x41
    prev=[0x36], succ=[0x7c, 0x4c]
    =================================
    0x42: v42(0xe4a24016) = CONST 
    0x47: v47 = GT v42(0xe4a24016), v1f
    0x48: v48(0x7c) = CONST 
    0x4b: JUMPI v48(0x7c), v47

    Begin block 0x7c
    prev=[0x41], succ=[0x33bb, 0x88]
    =================================
    0x7e: v7e(0xbf7e214f) = CONST 
    0x83: v83 = EQ v7e(0xbf7e214f), v1f
    0x32b9: v32b9(0x33bb) = CONST 
    0x32ba: JUMPI v32b9(0x33bb), v83

    Begin block 0x33bb
    prev=[0x7c], succ=[]
    =================================
    0x33bc: v33bc(0x779) = CONST 
    0x33bd: CALLPRIVATE v33bc(0x779)

    Begin block 0x88
    prev=[0x7c], succ=[0x33be, 0x93]
    =================================
    0x89: v89(0xc102fe25) = CONST 
    0x8e: v8e = EQ v89(0xc102fe25), v1f
    0x32bb: v32bb(0x33be) = CONST 
    0x32bc: JUMPI v32bb(0x33be), v8e

    Begin block 0x33be
    prev=[0x88], succ=[]
    =================================
    0x33bf: v33bf(0x781) = CONST 
    0x33c0: CALLPRIVATE v33bf(0x781)

    Begin block 0x93
    prev=[0x88], succ=[0x33c1, 0x9e]
    =================================
    0x94: v94(0xc4d66de8) = CONST 
    0x99: v99 = EQ v94(0xc4d66de8), v1f
    0x32bd: v32bd(0x33c1) = CONST 
    0x32be: JUMPI v32bd(0x33c1), v99

    Begin block 0x33c1
    prev=[0x93], succ=[]
    =================================
    0x33c2: v33c2(0x789) = CONST 
    0x33c3: CALLPRIVATE v33c2(0x789)

    Begin block 0x9e
    prev=[0x93], succ=[0xa9, 0x33c4]
    =================================
    0x9f: v9f(0xdd5e3720) = CONST 
    0xa4: va4 = EQ v9f(0xdd5e3720), v1f
    0x32bf: v32bf(0x33c4) = CONST 
    0x32c0: JUMPI v32bf(0x33c4), va4

    Begin block 0xa9
    prev=[0x9e], succ=[0x24b2]
    =================================
    0xa9: va9(0x24b2) = CONST 
    0xac: JUMP va9(0x24b2)

    Begin block 0x24b2
    prev=[0xa9], succ=[]
    =================================
    0x24b3: v24b3(0x0) = CONST 
    0x24b6: REVERT v24b3(0x0), v24b3(0x0)

    Begin block 0x33c4
    prev=[0x9e], succ=[]
    =================================
    0x33c5: v33c5(0x7af) = CONST 
    0x33c6: CALLPRIVATE v33c5(0x7af)

    Begin block 0x4c
    prev=[0x41], succ=[0x33c7, 0x57]
    =================================
    0x4d: v4d(0xe4a24016) = CONST 
    0x52: v52 = EQ v4d(0xe4a24016), v1f
    0x32b1: v32b1(0x33c7) = CONST 
    0x32b2: JUMPI v32b1(0x33c7), v52

    Begin block 0x33c7
    prev=[0x4c], succ=[]
    =================================
    0x33c8: v33c8(0x7d5) = CONST 
    0x33c9: CALLPRIVATE v33c8(0x7d5)

    Begin block 0x57
    prev=[0x4c], succ=[0x33ca, 0x62]
    =================================
    0x58: v58(0xf02e371a) = CONST 
    0x5d: v5d = EQ v58(0xf02e371a), v1f
    0x32b3: v32b3(0x33ca) = CONST 
    0x32b4: JUMPI v32b3(0x33ca), v5d

    Begin block 0x33ca
    prev=[0x57], succ=[]
    =================================
    0x33cb: v33cb(0x815) = CONST 
    0x33cc: CALLPRIVATE v33cb(0x815)

    Begin block 0x62
    prev=[0x57], succ=[0x33cd, 0x6d]
    =================================
    0x63: v63(0xf666196d) = CONST 
    0x68: v68 = EQ v63(0xf666196d), v1f
    0x32b5: v32b5(0x33cd) = CONST 
    0x32b6: JUMPI v32b5(0x33cd), v68

    Begin block 0x33cd
    prev=[0x62], succ=[]
    =================================
    0x33ce: v33ce(0x81d) = CONST 
    0x33cf: CALLPRIVATE v33ce(0x81d)

    Begin block 0x6d
    prev=[0x62], succ=[0x78, 0x33d0]
    =================================
    0x6e: v6e(0xfcb4aaee) = CONST 
    0x73: v73 = EQ v6e(0xfcb4aaee), v1f
    0x32b7: v32b7(0x33d0) = CONST 
    0x32b8: JUMPI v32b7(0x33d0), v73

    Begin block 0x78
    prev=[0x6d], succ=[0x248e]
    =================================
    0x78: v78(0x248e) = CONST 
    0x7b: JUMP v78(0x248e)

    Begin block 0x248e
    prev=[0x78], succ=[]
    =================================
    0x248f: v248f(0x0) = CONST 
    0x2492: REVERT v248f(0x0), v248f(0x0)

    Begin block 0x33d0
    prev=[0x6d], succ=[]
    =================================
    0x33d1: v33d1(0x86f) = CONST 
    0x33d2: CALLPRIVATE v33d1(0x86f)

    Begin block 0x3432
    prev=[0x10], succ=[]
    =================================
    0x3433: v3433(0x246a) = CONST 
    0x3434: CALLPRIVATE v3433(0x246a)

}

function 0x22d3(0x22d3arg0x0, 0x22d3arg0x1, 0x22d3arg0x2) private {
    Begin block 0x22d3
    prev=[], succ=[0x22ee, 0x22e7]
    =================================
    0x22d4: v22d4(0x0) = CONST 
    0x22d6: v22d6(0x1) = CONST 
    0x22d8: v22d8(0x1) = CONST 
    0x22da: v22da(0xa0) = CONST 
    0x22dc: v22dc(0x10000000000000000000000000000000000000000) = SHL v22da(0xa0), v22d8(0x1)
    0x22dd: v22dd(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22dc(0x10000000000000000000000000000000000000000), v22d6(0x1)
    0x22df: v22df = AND v22d3arg1, v22dd(0xffffffffffffffffffffffffffffffffffffffff)
    0x22e0: v22e0 = ADDRESS 
    0x22e1: v22e1 = EQ v22e0, v22df
    0x22e2: v22e2 = ISZERO v22e1
    0x22e3: v22e3(0x22ee) = CONST 
    0x22e6: JUMPI v22e3(0x22ee), v22e2

    Begin block 0x22ee
    prev=[0x22d3], succ=[0x230c, 0x2305]
    =================================
    0x22ef: v22ef(0x1) = CONST 
    0x22f1: v22f1 = SLOAD v22ef(0x1)
    0x22f2: v22f2(0x1) = CONST 
    0x22f4: v22f4(0x1) = CONST 
    0x22f6: v22f6(0xa0) = CONST 
    0x22f8: v22f8(0x10000000000000000000000000000000000000000) = SHL v22f6(0xa0), v22f4(0x1)
    0x22f9: v22f9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v22f8(0x10000000000000000000000000000000000000000), v22f2(0x1)
    0x22fc: v22fc = AND v22f9(0xffffffffffffffffffffffffffffffffffffffff), v22d3arg1
    0x22fe: v22fe = AND v22f1, v22f9(0xffffffffffffffffffffffffffffffffffffffff)
    0x22ff: v22ff = EQ v22fe, v22fc
    0x2300: v2300 = ISZERO v22ff
    0x2301: v2301(0x230c) = CONST 
    0x2304: JUMPI v2301(0x230c), v2300

    Begin block 0x230c
    prev=[0x22ee], succ=[0x232a, 0x2323]
    =================================
    0x230d: v230d(0x0) = CONST 
    0x230f: v230f = SLOAD v230d(0x0)
    0x2310: v2310(0x10000) = CONST 
    0x2315: v2315 = DIV v230f, v2310(0x10000)
    0x2316: v2316(0x1) = CONST 
    0x2318: v2318(0x1) = CONST 
    0x231a: v231a(0xa0) = CONST 
    0x231c: v231c(0x10000000000000000000000000000000000000000) = SHL v231a(0xa0), v2318(0x1)
    0x231d: v231d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v231c(0x10000000000000000000000000000000000000000), v2316(0x1)
    0x231e: v231e = AND v231d(0xffffffffffffffffffffffffffffffffffffffff), v2315
    0x231f: v231f(0x232a) = CONST 
    0x2322: JUMPI v231f(0x232a), v231e

    Begin block 0x232a
    prev=[0x230c], succ=[0x2390, 0x10ef0x22d3]
    =================================
    0x232b: v232b(0x0) = CONST 
    0x232d: v232d = SLOAD v232b(0x0)
    0x232e: v232e(0x40) = CONST 
    0x2331: v2331 = MLOAD v232e(0x40)
    0x2332: v2332(0xb7009613) = CONST 
    0x2337: v2337(0xe0) = CONST 
    0x2339: v2339(0xb700961300000000000000000000000000000000000000000000000000000000) = SHL v2337(0xe0), v2332(0xb7009613)
    0x233b: MSTORE v2331, v2339(0xb700961300000000000000000000000000000000000000000000000000000000)
    0x233c: v233c(0x1) = CONST 
    0x233e: v233e(0x1) = CONST 
    0x2340: v2340(0xa0) = CONST 
    0x2342: v2342(0x10000000000000000000000000000000000000000) = SHL v2340(0xa0), v233e(0x1)
    0x2343: v2343(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2342(0x10000000000000000000000000000000000000000), v233c(0x1)
    0x2346: v2346 = AND v2343(0xffffffffffffffffffffffffffffffffffffffff), v22d3arg1
    0x2347: v2347(0x4) = CONST 
    0x234a: v234a = ADD v2331, v2347(0x4)
    0x234b: MSTORE v234a, v2346
    0x234c: v234c = ADDRESS 
    0x234d: v234d(0x24) = CONST 
    0x2350: v2350 = ADD v2331, v234d(0x24)
    0x2351: MSTORE v2350, v234c
    0x2352: v2352(0x1) = CONST 
    0x2354: v2354(0x1) = CONST 
    0x2356: v2356(0xe0) = CONST 
    0x2358: v2358(0x100000000000000000000000000000000000000000000000000000000) = SHL v2356(0xe0), v2354(0x1)
    0x2359: v2359(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v2358(0x100000000000000000000000000000000000000000000000000000000), v2352(0x1)
    0x235a: v235a(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v2359(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x235c: v235c = AND v22d3arg0, v235a(0xffffffff00000000000000000000000000000000000000000000000000000000)
    0x235d: v235d(0x44) = CONST 
    0x2360: v2360 = ADD v2331, v235d(0x44)
    0x2361: MSTORE v2360, v235c
    0x2363: v2363 = MLOAD v232e(0x40)
    0x2364: v2364(0x10000) = CONST 
    0x236a: v236a = DIV v232d, v2364(0x10000)
    0x236d: v236d = AND v2343(0xffffffffffffffffffffffffffffffffffffffff), v236a
    0x236f: v236f(0xb7009613) = CONST 
    0x2375: v2375(0x64) = CONST 
    0x2379: v2379 = ADD v2331, v2375(0x64)
    0x237b: v237b(0x20) = CONST 
    0x2383: v2383(0x0) = SUB v2331, v2363
    0x2384: v2384(0x64) = ADD v2383(0x0), v2375(0x64)
    0x2388: v2388 = EXTCODESIZE v236d
    0x2389: v2389 = ISZERO v2388
    0x238b: v238b = ISZERO v2389
    0x238c: v238c(0x10ef) = CONST 
    0x238f: JUMPI v238c(0x10ef), v238b

    Begin block 0x2390
    prev=[0x232a], succ=[]
    =================================
    0x2390: v2390(0x0) = CONST 
    0x2393: REVERT v2390(0x0), v2390(0x0)

    Begin block 0x10ef0x22d3
    prev=[0x232a], succ=[0x10fa0x22d3, 0x11030x22d3]
    =================================
    0x10f10x22d3: v22d310f1 = GAS 
    0x10f20x22d3: v22d310f2 = STATICCALL v22d310f1, v236d, v2363, v2384(0x64), v2363, v237b(0x20)
    0x10f30x22d3: v22d310f3 = ISZERO v22d310f2
    0x10f50x22d3: v22d310f5 = ISZERO v22d310f3
    0x10f60x22d3: v22d310f6(0x1103) = CONST 
    0x10f90x22d3: JUMPI v22d310f6(0x1103), v22d310f5

    Begin block 0x10fa0x22d3
    prev=[0x10ef0x22d3], succ=[]
    =================================
    0x10fa0x22d3: v22d310fa = RETURNDATASIZE 
    0x10fb0x22d3: v22d310fb(0x0) = CONST 
    0x10fe0x22d3: RETURNDATACOPY v22d310fb(0x0), v22d310fb(0x0), v22d310fa
    0x10ff0x22d3: v22d310ff = RETURNDATASIZE 
    0x11000x22d3: v22d31100(0x0) = CONST 
    0x11020x22d3: REVERT v22d31100(0x0), v22d310ff

    Begin block 0x11030x22d3
    prev=[0x10ef0x22d3], succ=[0x11150x22d3, 0x11190x22d3]
    =================================
    0x11080x22d3: v22d31108(0x40) = CONST 
    0x110a0x22d3: v22d3110a = MLOAD v22d31108(0x40)
    0x110b0x22d3: v22d3110b = RETURNDATASIZE 
    0x110c0x22d3: v22d3110c(0x20) = CONST 
    0x110f0x22d3: v22d3110f = LT v22d3110b, v22d3110c(0x20)
    0x11100x22d3: v22d31110 = ISZERO v22d3110f
    0x11110x22d3: v22d31111(0x1119) = CONST 
    0x11140x22d3: JUMPI v22d31111(0x1119), v22d31110

    Begin block 0x11150x22d3
    prev=[0x11030x22d3], succ=[]
    =================================
    0x11150x22d3: v22d31115(0x0) = CONST 
    0x11180x22d3: REVERT v22d31115(0x0), v22d31115(0x0)

    Begin block 0x11190x22d3
    prev=[0x11030x22d3], succ=[0x31c90x22d3]
    =================================
    0x111b0x22d3: v22d3111b = MLOAD v22d3110a
    0x111e0x22d3: v22d3111e(0x31c9) = CONST 
    0x11210x22d3: JUMP v22d3111e(0x31c9)

    Begin block 0x31c90x22d3
    prev=[0x11190x22d3], succ=[]
    =================================
    0x31ce0x22d3: RETURNPRIVATE v22d3arg2, v22d3111b

    Begin block 0x2323
    prev=[0x230c], succ=[0x32a9]
    =================================
    0x2324: v2324(0x0) = CONST 
    0x2326: v2326(0x32a9) = CONST 
    0x2329: JUMP v2326(0x32a9)

    Begin block 0x32a9
    prev=[0x2323], succ=[]
    =================================
    0x32ae: RETURNPRIVATE v22d3arg2, v2324(0x0)

    Begin block 0x2305
    prev=[0x22ee], succ=[0x3284]
    =================================
    0x2306: v2306(0x1) = CONST 
    0x2308: v2308(0x3284) = CONST 
    0x230b: JUMP v2308(0x3284)

    Begin block 0x3284
    prev=[0x2305], succ=[]
    =================================
    0x3289: RETURNPRIVATE v22d3arg2, v2306(0x1)

    Begin block 0x22e7
    prev=[0x22d3], succ=[0x325f]
    =================================
    0x22e8: v22e8(0x1) = CONST 
    0x22ea: v22ea(0x325f) = CONST 
    0x22ed: JUMP v22ea(0x325f)

    Begin block 0x325f
    prev=[0x22e7], succ=[]
    =================================
    0x3264: RETURNPRIVATE v22d3arg2, v22e8(0x1)

}

function fallback()() public {
    Begin block 0x246a
    prev=[], succ=[]
    =================================
    0x246b: v246b(0x0) = CONST 
    0x246e: REVERT v246b(0x0), v246b(0x0)

}

function CONTRACT_LP_ELEMENT_TOKEN()() public {
    Begin block 0x392
    prev=[], succ=[0x89c]
    =================================
    0x393: v393(0x26aa) = CONST 
    0x396: v396(0x89c) = CONST 
    0x399: JUMP v396(0x89c)

    Begin block 0x89c
    prev=[0x392], succ=[0x26aa]
    =================================
    0x89d: v89d(0x0) = CONST 
    0x8a0: v8a0 = MLOAD v89d(0x0)
    0x8a1: v8a1(0x20) = CONST 
    0x8a3: v8a3(0x23e9) = CONST 
    0x8ab: MSTORE v89d(0x0), v8a0
    0x8ad: JUMP v393(0x26aa)
    0x33d7: v33d7(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 

    Begin block 0x26aa
    prev=[0x89c], succ=[]
    =================================
    0x26ab: v26ab(0x40) = CONST 
    0x26ae: v26ae = MLOAD v26ab(0x40)
    0x26b1: MSTORE v26ae, v33d7(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x26b2: v26b2 = MLOAD v26ab(0x40)
    0x26b6: v26b6(0x0) = SUB v26ae, v26b2
    0x26b7: v26b7(0x20) = CONST 
    0x26b9: v26b9(0x20) = ADD v26b7(0x20), v26b6(0x0)
    0x26bb: RETURN v26b2, v26b9(0x20)

}

function PREFER_FIRE()() public {
    Begin block 0x3ac
    prev=[], succ=[0x8ae]
    =================================
    0x3ad: v3ad(0x26db) = CONST 
    0x3b0: v3b0(0x8ae) = CONST 
    0x3b3: JUMP v3b0(0x8ae)

    Begin block 0x8ae
    prev=[0x3ac], succ=[0x26db]
    =================================
    0x8af: v8af(0x10) = CONST 
    0x8b2: JUMP v3ad(0x26db)

    Begin block 0x26db
    prev=[0x8ae], succ=[]
    =================================
    0x26dc: v26dc(0x40) = CONST 
    0x26df: v26df = MLOAD v26dc(0x40)
    0x26e2: MSTORE v26df, v8af(0x10)
    0x26e3: v26e3 = MLOAD v26dc(0x40)
    0x26e7: v26e7(0x0) = SUB v26df, v26e3
    0x26e8: v26e8(0x20) = CONST 
    0x26ea: v26ea(0x20) = ADD v26e8(0x20), v26e7(0x0)
    0x26ec: RETURN v26e3, v26ea(0x20)

}

function CONTRACT_LP_SOIL_ERC20_TOKEN()() public {
    Begin block 0x3b4
    prev=[], succ=[0x8b3]
    =================================
    0x3b5: v3b5(0x270c) = CONST 
    0x3b8: v3b8(0x8b3) = CONST 
    0x3bb: JUMP v3b8(0x8b3)

    Begin block 0x8b3
    prev=[0x3b4], succ=[0x270c]
    =================================
    0x8b4: v8b4(0x434f4e54524143545f4c505f534f494c5f45524332305f544f4b454e00000000) = CONST 
    0x8d6: JUMP v3b5(0x270c)

    Begin block 0x270c
    prev=[0x8b3], succ=[]
    =================================
    0x270d: v270d(0x40) = CONST 
    0x2710: v2710 = MLOAD v270d(0x40)
    0x2713: MSTORE v2710, v8b4(0x434f4e54524143545f4c505f534f494c5f45524332305f544f4b454e00000000)
    0x2714: v2714 = MLOAD v270d(0x40)
    0x2718: v2718(0x0) = SUB v2710, v2714
    0x2719: v2719(0x20) = CONST 
    0x271b: v271b(0x20) = ADD v2719(0x20), v2718(0x0)
    0x271d: RETURN v2714, v271b(0x20)

}

function setOwner(address)() public {
    Begin block 0x3bc
    prev=[], succ=[0x3ce, 0x3d2]
    =================================
    0x3bd: v3bd(0x273d) = CONST 
    0x3c0: v3c0(0x4) = CONST 
    0x3c3: v3c3 = CALLDATASIZE 
    0x3c4: v3c4 = SUB v3c3, v3c0(0x4)
    0x3c5: v3c5(0x20) = CONST 
    0x3c8: v3c8 = LT v3c4, v3c5(0x20)
    0x3c9: v3c9 = ISZERO v3c8
    0x3ca: v3ca(0x3d2) = CONST 
    0x3cd: JUMPI v3ca(0x3d2), v3c9

    Begin block 0x3ce
    prev=[0x3bc], succ=[]
    =================================
    0x3ce: v3ce(0x0) = CONST 
    0x3d1: REVERT v3ce(0x0), v3ce(0x0)

    Begin block 0x3d2
    prev=[0x3bc], succ=[0x8d7]
    =================================
    0x3d4: v3d4 = CALLDATALOAD v3c0(0x4)
    0x3d5: v3d5(0x1) = CONST 
    0x3d7: v3d7(0x1) = CONST 
    0x3d9: v3d9(0xa0) = CONST 
    0x3db: v3db(0x10000000000000000000000000000000000000000) = SHL v3d9(0xa0), v3d7(0x1)
    0x3dc: v3dc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3db(0x10000000000000000000000000000000000000000), v3d5(0x1)
    0x3dd: v3dd = AND v3dc(0xffffffffffffffffffffffffffffffffffffffff), v3d4
    0x3de: v3de(0x8d7) = CONST 
    0x3e1: JUMP v3de(0x8d7)

    Begin block 0x8d7
    prev=[0x3d2], succ=[0x8ed]
    =================================
    0x8d8: v8d8(0x8ed) = CONST 
    0x8db: v8db = CALLER 
    0x8dc: v8dc(0x0) = CONST 
    0x8de: v8de = CALLDATALOAD v8dc(0x0)
    0x8df: v8df(0x1) = CONST 
    0x8e1: v8e1(0x1) = CONST 
    0x8e3: v8e3(0xe0) = CONST 
    0x8e5: v8e5(0x100000000000000000000000000000000000000000000000000000000) = SHL v8e3(0xe0), v8e1(0x1)
    0x8e6: v8e6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v8e5(0x100000000000000000000000000000000000000000000000000000000), v8df(0x1)
    0x8e7: v8e7(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v8e6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x8e8: v8e8 = AND v8e7(0xffffffff00000000000000000000000000000000000000000000000000000000), v8de
    0x8e9: v8e9(0x22d3) = CONST 
    0x8ec: v8ec_0 = CALLPRIVATE v8e9(0x22d3), v8e8, v8db, v8d8(0x8ed)

    Begin block 0x8ed
    prev=[0x8d7], succ=[0x8f2, 0x92c]
    =================================
    0x8ee: v8ee(0x92c) = CONST 
    0x8f1: JUMPI v8ee(0x92c), v8ec_0

    Begin block 0x8f2
    prev=[0x8ed], succ=[]
    =================================
    0x8f2: v8f2(0x40) = CONST 
    0x8f5: v8f5 = MLOAD v8f2(0x40)
    0x8f6: v8f6(0x461bcd) = CONST 
    0x8fa: v8fa(0xe5) = CONST 
    0x8fc: v8fc(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v8fa(0xe5), v8f6(0x461bcd)
    0x8fe: MSTORE v8f5, v8fc(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x8ff: v8ff(0x20) = CONST 
    0x901: v901(0x4) = CONST 
    0x904: v904 = ADD v8f5, v901(0x4)
    0x905: MSTORE v904, v8ff(0x20)
    0x906: v906(0x14) = CONST 
    0x908: v908(0x24) = CONST 
    0x90b: v90b = ADD v8f5, v908(0x24)
    0x90c: MSTORE v90b, v906(0x14)
    0x90d: v90d(0x0) = CONST 
    0x910: v910 = MLOAD v90d(0x0)
    0x911: v911(0x20) = CONST 
    0x913: v913(0x2409) = CONST 
    0x91b: MSTORE v90d(0x0), v910
    0x91c: v91c(0x44) = CONST 
    0x91f: v91f = ADD v8f5, v91c(0x44)
    0x920: MSTORE v91f, v33dc(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x922: v922 = MLOAD v8f2(0x40)
    0x926: v926(0x0) = SUB v8f5, v922
    0x927: v927(0x64) = CONST 
    0x929: v929(0x64) = ADD v927(0x64), v926(0x0)
    0x92b: REVERT v922, v929(0x64)
    0x33dc: v33dc(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x92c
    prev=[0x8ed], succ=[0x273d]
    =================================
    0x92d: v92d(0x1) = CONST 
    0x930: v930 = SLOAD v92d(0x1)
    0x931: v931(0x1) = CONST 
    0x933: v933(0x1) = CONST 
    0x935: v935(0xa0) = CONST 
    0x937: v937(0x10000000000000000000000000000000000000000) = SHL v935(0xa0), v933(0x1)
    0x938: v938(0xffffffffffffffffffffffffffffffffffffffff) = SUB v937(0x10000000000000000000000000000000000000000), v931(0x1)
    0x939: v939(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v938(0xffffffffffffffffffffffffffffffffffffffff)
    0x93a: v93a = AND v939(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v930
    0x93b: v93b(0x1) = CONST 
    0x93d: v93d(0x1) = CONST 
    0x93f: v93f(0xa0) = CONST 
    0x941: v941(0x10000000000000000000000000000000000000000) = SHL v93f(0xa0), v93d(0x1)
    0x942: v942(0xffffffffffffffffffffffffffffffffffffffff) = SUB v941(0x10000000000000000000000000000000000000000), v93b(0x1)
    0x945: v945 = AND v942(0xffffffffffffffffffffffffffffffffffffffff), v3dd
    0x949: v949 = OR v945, v93a
    0x94d: SSTORE v92d(0x1), v949
    0x94e: v94e(0x40) = CONST 
    0x950: v950 = MLOAD v94e(0x40)
    0x952: v952 = AND v949, v942(0xffffffffffffffffffffffffffffffffffffffff)
    0x954: v954(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94) = CONST 
    0x976: v976(0x0) = CONST 
    0x979: LOG2 v950, v976(0x0), v954(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94), v952
    0x97b: JUMP v3bd(0x273d)

    Begin block 0x273d
    prev=[0x92c], succ=[]
    =================================
    0x273e: STOP 

}

function removeInternalTokenMeta(bytes32,uint16)() public {
    Begin block 0x3e4
    prev=[], succ=[0x3f6, 0x3fa]
    =================================
    0x3e5: v3e5(0x275e) = CONST 
    0x3e8: v3e8(0x4) = CONST 
    0x3eb: v3eb = CALLDATASIZE 
    0x3ec: v3ec = SUB v3eb, v3e8(0x4)
    0x3ed: v3ed(0x40) = CONST 
    0x3f0: v3f0 = LT v3ec, v3ed(0x40)
    0x3f1: v3f1 = ISZERO v3f0
    0x3f2: v3f2(0x3fa) = CONST 
    0x3f5: JUMPI v3f2(0x3fa), v3f1

    Begin block 0x3f6
    prev=[0x3e4], succ=[]
    =================================
    0x3f6: v3f6(0x0) = CONST 
    0x3f9: REVERT v3f6(0x0), v3f6(0x0)

    Begin block 0x3fa
    prev=[0x3e4], succ=[0x97c]
    =================================
    0x3fd: v3fd = CALLDATALOAD v3e8(0x4)
    0x3ff: v3ff(0x20) = CONST 
    0x401: v401(0x24) = ADD v3ff(0x20), v3e8(0x4)
    0x402: v402 = CALLDATALOAD v401(0x24)
    0x403: v403(0xffff) = CONST 
    0x406: v406 = AND v403(0xffff), v402
    0x407: v407(0x97c) = CONST 
    0x40a: JUMP v407(0x97c)

    Begin block 0x97c
    prev=[0x3fa], succ=[0x992]
    =================================
    0x97d: v97d(0x992) = CONST 
    0x980: v980 = CALLER 
    0x981: v981(0x0) = CONST 
    0x983: v983 = CALLDATALOAD v981(0x0)
    0x984: v984(0x1) = CONST 
    0x986: v986(0x1) = CONST 
    0x988: v988(0xe0) = CONST 
    0x98a: v98a(0x100000000000000000000000000000000000000000000000000000000) = SHL v988(0xe0), v986(0x1)
    0x98b: v98b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v98a(0x100000000000000000000000000000000000000000000000000000000), v984(0x1)
    0x98c: v98c(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v98b(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x98d: v98d = AND v98c(0xffffffff00000000000000000000000000000000000000000000000000000000), v983
    0x98e: v98e(0x22d3) = CONST 
    0x991: v991_0 = CALLPRIVATE v98e(0x22d3), v98d, v980, v97d(0x992)

    Begin block 0x992
    prev=[0x97c], succ=[0x997, 0x9d1]
    =================================
    0x993: v993(0x9d1) = CONST 
    0x996: JUMPI v993(0x9d1), v991_0

    Begin block 0x997
    prev=[0x992], succ=[]
    =================================
    0x997: v997(0x40) = CONST 
    0x99a: v99a = MLOAD v997(0x40)
    0x99b: v99b(0x461bcd) = CONST 
    0x99f: v99f(0xe5) = CONST 
    0x9a1: v9a1(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v99f(0xe5), v99b(0x461bcd)
    0x9a3: MSTORE v99a, v9a1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x9a4: v9a4(0x20) = CONST 
    0x9a6: v9a6(0x4) = CONST 
    0x9a9: v9a9 = ADD v99a, v9a6(0x4)
    0x9aa: MSTORE v9a9, v9a4(0x20)
    0x9ab: v9ab(0x14) = CONST 
    0x9ad: v9ad(0x24) = CONST 
    0x9b0: v9b0 = ADD v99a, v9ad(0x24)
    0x9b1: MSTORE v9b0, v9ab(0x14)
    0x9b2: v9b2(0x0) = CONST 
    0x9b5: v9b5 = MLOAD v9b2(0x0)
    0x9b6: v9b6(0x20) = CONST 
    0x9b8: v9b8(0x2409) = CONST 
    0x9c0: MSTORE v9b2(0x0), v9b5
    0x9c1: v9c1(0x44) = CONST 
    0x9c4: v9c4 = ADD v99a, v9c1(0x44)
    0x9c5: MSTORE v9c4, v33e1(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x9c7: v9c7 = MLOAD v997(0x40)
    0x9cb: v9cb(0x0) = SUB v99a, v9c7
    0x9cc: v9cc(0x64) = CONST 
    0x9ce: v9ce(0x64) = ADD v9cc(0x64), v9cb(0x0)
    0x9d0: REVERT v9c7, v9ce(0x64)
    0x33e1: v33e1(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x9d1
    prev=[0x992], succ=[0x275e]
    =================================
    0x9d2: v9d2(0x0) = CONST 
    0x9d6: MSTORE v9d2(0x0), v3fd
    0x9d7: v9d7(0x5) = CONST 
    0x9d9: v9d9(0x20) = CONST 
    0x9dd: MSTORE v9d9(0x20), v9d7(0x5)
    0x9de: v9de(0x40) = CONST 
    0x9e2: v9e2 = SHA3 v9d2(0x0), v9de(0x40)
    0x9e3: v9e3(0xffff) = CONST 
    0x9e7: v9e7 = AND v406, v9e3(0xffff)
    0x9ea: MSTORE v9d2(0x0), v9e7
    0x9ed: MSTORE v9d9(0x20), v9e2
    0x9f0: v9f0 = SHA3 v9d2(0x0), v9de(0x40)
    0x9f4: SSTORE v9f0, v9d2(0x0)
    0x9f6: v9f6 = MLOAD v9de(0x40)
    0x9f9: MSTORE v9f6, v9e7
    0x9fa: v9fa = MLOAD v9de(0x40)
    0x9fd: v9fd(0x6099bd94321aaa3f84f9d0a2aed109a4898fe63080ad546f37ac3a0b3e96c396) = CONST 
    0xa22: va22(0x0) = SUB v9f6, v9fa
    0xa23: va23(0x20) = ADD va22(0x0), v9d9(0x20)
    0xa25: LOG2 v9fa, va23(0x20), v9fd(0x6099bd94321aaa3f84f9d0a2aed109a4898fe63080ad546f37ac3a0b3e96c396), v3fd
    0xa28: JUMP v3e5(0x275e)

    Begin block 0x275e
    prev=[0x9d1], succ=[]
    =================================
    0x275f: STOP 

}

function CONTRACT_FORMULA()() public {
    Begin block 0x40b
    prev=[], succ=[0xa29]
    =================================
    0x40c: v40c(0x277f) = CONST 
    0x40f: v40f(0xa29) = CONST 
    0x412: JUMP v40f(0xa29)

    Begin block 0xa29
    prev=[0x40b], succ=[0x277f]
    =================================
    0xa2a: va2a(0x434f4e54524143545f464f524d554c41) = CONST 
    0xa3b: va3b(0x80) = CONST 
    0xa3d: va3d(0x434f4e54524143545f464f524d554c4100000000000000000000000000000000) = SHL va3b(0x80), va2a(0x434f4e54524143545f464f524d554c41)
    0xa3f: JUMP v40c(0x277f)

    Begin block 0x277f
    prev=[0xa29], succ=[]
    =================================
    0x2780: v2780(0x40) = CONST 
    0x2783: v2783 = MLOAD v2780(0x40)
    0x2786: MSTORE v2783, va3d(0x434f4e54524143545f464f524d554c4100000000000000000000000000000000)
    0x2787: v2787 = MLOAD v2780(0x40)
    0x278b: v278b(0x0) = SUB v2783, v2787
    0x278c: v278c(0x20) = CONST 
    0x278e: v278e(0x20) = ADD v278c(0x20), v278b(0x0)
    0x2790: RETURN v2787, v278e(0x20)

}

function externalToken2Meta(address)() public {
    Begin block 0x413
    prev=[], succ=[0x425, 0x429]
    =================================
    0x414: v414(0x27b0) = CONST 
    0x417: v417(0x4) = CONST 
    0x41a: v41a = CALLDATASIZE 
    0x41b: v41b = SUB v41a, v417(0x4)
    0x41c: v41c(0x20) = CONST 
    0x41f: v41f = LT v41b, v41c(0x20)
    0x420: v420 = ISZERO v41f
    0x421: v421(0x429) = CONST 
    0x424: JUMPI v421(0x429), v420

    Begin block 0x425
    prev=[0x413], succ=[]
    =================================
    0x425: v425(0x0) = CONST 
    0x428: REVERT v425(0x0), v425(0x0)

    Begin block 0x429
    prev=[0x413], succ=[0xa40]
    =================================
    0x42b: v42b = CALLDATALOAD v417(0x4)
    0x42c: v42c(0x1) = CONST 
    0x42e: v42e(0x1) = CONST 
    0x430: v430(0xa0) = CONST 
    0x432: v432(0x10000000000000000000000000000000000000000) = SHL v430(0xa0), v42e(0x1)
    0x433: v433(0xffffffffffffffffffffffffffffffffffffffff) = SUB v432(0x10000000000000000000000000000000000000000), v42c(0x1)
    0x434: v434 = AND v433(0xffffffffffffffffffffffffffffffffffffffff), v42b
    0x435: v435(0xa40) = CONST 
    0x438: JUMP v435(0xa40)

    Begin block 0xa40
    prev=[0x429], succ=[0x27b0]
    =================================
    0xa41: va41(0x4) = CONST 
    0xa43: va43(0x20) = CONST 
    0xa45: MSTORE va43(0x20), va41(0x4)
    0xa46: va46(0x0) = CONST 
    0xa4a: MSTORE va46(0x0), v434
    0xa4b: va4b(0x40) = CONST 
    0xa4e: va4e = SHA3 va46(0x0), va4b(0x40)
    0xa4f: va4f = SLOAD va4e
    0xa50: va50(0xffff) = CONST 
    0xa53: va53 = AND va50(0xffff), va4f
    0xa55: JUMP v414(0x27b0)

    Begin block 0x27b0
    prev=[0xa40], succ=[]
    =================================
    0x27b1: v27b1(0x40) = CONST 
    0x27b4: v27b4 = MLOAD v27b1(0x40)
    0x27b5: v27b5(0xffff) = CONST 
    0x27ba: v27ba = AND va53, v27b5(0xffff)
    0x27bc: MSTORE v27b4, v27ba
    0x27bd: v27bd = MLOAD v27b1(0x40)
    0x27c1: v27c1(0x0) = SUB v27b4, v27bd
    0x27c2: v27c2(0x20) = CONST 
    0x27c4: v27c4(0x20) = ADD v27c2(0x20), v27c1(0x0)
    0x27c6: RETURN v27bd, v27c4(0x20)

}

function CONTRACT_WATER_ERC20_TOKEN()() public {
    Begin block 0x450
    prev=[], succ=[0xa56]
    =================================
    0x451: v451(0x27e6) = CONST 
    0x454: v454(0xa56) = CONST 
    0x457: JUMP v454(0xa56)

    Begin block 0xa56
    prev=[0x450], succ=[0x27e6]
    =================================
    0xa57: va57(0x434f4e54524143545f57415445525f45524332305f544f4b454e000000000000) = CONST 
    0xa79: JUMP v451(0x27e6)

    Begin block 0x27e6
    prev=[0xa56], succ=[]
    =================================
    0x27e7: v27e7(0x40) = CONST 
    0x27ea: v27ea = MLOAD v27e7(0x40)
    0x27ed: MSTORE v27ea, va57(0x434f4e54524143545f57415445525f45524332305f544f4b454e000000000000)
    0x27ee: v27ee = MLOAD v27e7(0x40)
    0x27f2: v27f2(0x0) = SUB v27ea, v27ee
    0x27f3: v27f3(0x20) = CONST 
    0x27f5: v27f5(0x20) = ADD v27f3(0x20), v27f2(0x0)
    0x27f7: RETURN v27ee, v27f5(0x20)

}

function CONTRACT_GOLD_ERC20_TOKEN()() public {
    Begin block 0x458
    prev=[], succ=[0xa7a]
    =================================
    0x459: v459(0x2817) = CONST 
    0x45c: v45c(0xa7a) = CONST 
    0x45f: JUMP v45c(0xa7a)

    Begin block 0xa7a
    prev=[0x458], succ=[0x2817]
    =================================
    0xa7b: va7b(0x434f4e54524143545f474f4c445f45524332305f544f4b454e00000000000000) = CONST 
    0xa9d: JUMP v459(0x2817)

    Begin block 0x2817
    prev=[0xa7a], succ=[]
    =================================
    0x2818: v2818(0x40) = CONST 
    0x281b: v281b = MLOAD v2818(0x40)
    0x281e: MSTORE v281b, va7b(0x434f4e54524143545f474f4c445f45524332305f544f4b454e00000000000000)
    0x281f: v281f = MLOAD v2818(0x40)
    0x2823: v2823(0x0) = SUB v281b, v281f
    0x2824: v2824(0x20) = CONST 
    0x2826: v2826(0x20) = ADD v2824(0x20), v2823(0x0)
    0x2828: RETURN v281f, v2826(0x20)

}

function RATE_PRECISION()() public {
    Begin block 0x460
    prev=[], succ=[0xa9e]
    =================================
    0x461: v461(0x468) = CONST 
    0x464: v464(0xa9e) = CONST 
    0x467: JUMP v464(0xa9e)

    Begin block 0xa9e
    prev=[0x460], succ=[0x468]
    =================================
    0xa9f: va9f(0x5f5e100) = CONST 
    0xaa5: JUMP v461(0x468)

    Begin block 0x468
    prev=[0xa9e], succ=[]
    =================================
    0x469: v469(0x40) = CONST 
    0x46c: v46c = MLOAD v469(0x40)
    0x46d: v46d(0xffffffffffffffffffffffffffffffff) = CONST 
    0x480: v480(0x5f5e100) = AND va9f(0x5f5e100), v46d(0xffffffffffffffffffffffffffffffff)
    0x482: MSTORE v46c, v480(0x5f5e100)
    0x483: v483 = MLOAD v469(0x40)
    0x487: v487(0x0) = SUB v46c, v483
    0x488: v488(0x20) = CONST 
    0x48a: v48a(0x20) = ADD v488(0x20), v487(0x0)
    0x48c: RETURN v483, v48a(0x20)

}

function getExternalStrengthRate(address,uint16)() public {
    Begin block 0x48d
    prev=[], succ=[0x49f, 0x4a3]
    =================================
    0x48e: v48e(0x2848) = CONST 
    0x491: v491(0x4) = CONST 
    0x494: v494 = CALLDATASIZE 
    0x495: v495 = SUB v494, v491(0x4)
    0x496: v496(0x40) = CONST 
    0x499: v499 = LT v495, v496(0x40)
    0x49a: v49a = ISZERO v499
    0x49b: v49b(0x4a3) = CONST 
    0x49e: JUMPI v49b(0x4a3), v49a

    Begin block 0x49f
    prev=[0x48d], succ=[]
    =================================
    0x49f: v49f(0x0) = CONST 
    0x4a2: REVERT v49f(0x0), v49f(0x0)

    Begin block 0x4a3
    prev=[0x48d], succ=[0xaa60x48d]
    =================================
    0x4a6: v4a6 = CALLDATALOAD v491(0x4)
    0x4a7: v4a7(0x1) = CONST 
    0x4a9: v4a9(0x1) = CONST 
    0x4ab: v4ab(0xa0) = CONST 
    0x4ad: v4ad(0x10000000000000000000000000000000000000000) = SHL v4ab(0xa0), v4a9(0x1)
    0x4ae: v4ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ad(0x10000000000000000000000000000000000000000), v4a7(0x1)
    0x4af: v4af = AND v4ae(0xffffffffffffffffffffffffffffffffffffffff), v4a6
    0x4b1: v4b1(0x20) = CONST 
    0x4b3: v4b3(0x24) = ADD v4b1(0x20), v491(0x4)
    0x4b4: v4b4 = CALLDATALOAD v4b3(0x24)
    0x4b5: v4b5(0xffff) = CONST 
    0x4b8: v4b8 = AND v4b5(0xffff), v4b4
    0x4b9: v4b9(0xaa6) = CONST 
    0x4bc: JUMP v4b9(0xaa6)

    Begin block 0xaa60x48d
    prev=[0x4a3], succ=[0xac80x48d, 0xb0b0x48d]
    =================================
    0xaa70x48d: v48daa7(0x1) = CONST 
    0xaa90x48d: v48daa9(0x1) = CONST 
    0xaab0x48d: v48daab(0xa0) = CONST 
    0xaad0x48d: v48daad(0x10000000000000000000000000000000000000000) = SHL v48daab(0xa0), v48daa9(0x1)
    0xaae0x48d: v48daae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48daad(0x10000000000000000000000000000000000000000), v48daa7(0x1)
    0xab00x48d: v48dab0 = AND v4af, v48daae(0xffffffffffffffffffffffffffffffffffffffff)
    0xab10x48d: v48dab1(0x0) = CONST 
    0xab50x48d: MSTORE v48dab1(0x0), v48dab0
    0xab60x48d: v48dab6(0x4) = CONST 
    0xab80x48d: v48dab8(0x20) = CONST 
    0xaba0x48d: MSTORE v48dab8(0x20), v48dab6(0x4)
    0xabb0x48d: v48dabb(0x40) = CONST 
    0xabe0x48d: v48dabe = SHA3 v48dab1(0x0), v48dabb(0x40)
    0xabf0x48d: v48dabf = SLOAD v48dabe
    0xac00x48d: v48dac0(0xffff) = CONST 
    0xac30x48d: v48dac3 = AND v48dac0(0xffff), v48dabf
    0xac40x48d: v48dac4(0xb0b) = CONST 
    0xac70x48d: JUMPI v48dac4(0xb0b), v48dac3

    Begin block 0xac80x48d
    prev=[0xaa60x48d], succ=[]
    =================================
    0xac80x48d: v48dac8(0x40) = CONST 
    0xacb0x48d: v48dacb = MLOAD v48dac8(0x40)
    0xacc0x48d: v48dacc(0x461bcd) = CONST 
    0xad00x48d: v48dad0(0xe5) = CONST 
    0xad20x48d: v48dad2(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v48dad0(0xe5), v48dacc(0x461bcd)
    0xad40x48d: MSTORE v48dacb, v48dad2(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xad50x48d: v48dad5(0x20) = CONST 
    0xad70x48d: v48dad7(0x4) = CONST 
    0xada0x48d: v48dada = ADD v48dacb, v48dad7(0x4)
    0xadb0x48d: MSTORE v48dada, v48dad5(0x20)
    0xadc0x48d: v48dadc(0x14) = CONST 
    0xade0x48d: v48dade(0x24) = CONST 
    0xae10x48d: v48dae1 = ADD v48dacb, v48dade(0x24)
    0xae20x48d: MSTORE v48dae1, v48dadc(0x14)
    0xae30x48d: v48dae3(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0xaf80x48d: v48daf8(0x62) = CONST 
    0xafa0x48d: v48dafa(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL v48daf8(0x62), v48dae3(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0xafb0x48d: v48dafb(0x44) = CONST 
    0xafe0x48d: v48dafe = ADD v48dacb, v48dafb(0x44)
    0xaff0x48d: MSTORE v48dafe, v48dafa(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0xb010x48d: v48db01 = MLOAD v48dac8(0x40)
    0xb050x48d: v48db05(0x0) = SUB v48dacb, v48db01
    0xb060x48d: v48db06(0x64) = CONST 
    0xb080x48d: v48db08(0x64) = ADD v48db06(0x64), v48db05(0x0)
    0xb0a0x48d: REVERT v48db01, v48db08(0x64)

    Begin block 0xb0b0x48d
    prev=[0xaa60x48d], succ=[0xb380x48d]
    =================================
    0xb0d0x48d: v48db0d(0x1) = CONST 
    0xb0f0x48d: v48db0f(0x1) = CONST 
    0xb110x48d: v48db11(0xa0) = CONST 
    0xb130x48d: v48db13(0x10000000000000000000000000000000000000000) = SHL v48db11(0xa0), v48db0f(0x1)
    0xb140x48d: v48db14(0xffffffffffffffffffffffffffffffffffffffff) = SUB v48db13(0x10000000000000000000000000000000000000000), v48db0d(0x1)
    0xb160x48d: v48db16 = AND v4af, v48db14(0xffffffffffffffffffffffffffffffffffffffff)
    0xb170x48d: v48db17(0x0) = CONST 
    0xb1b0x48d: MSTORE v48db17(0x0), v48db16
    0xb1c0x48d: v48db1c(0x4) = CONST 
    0xb1e0x48d: v48db1e(0x20) = CONST 
    0xb220x48d: MSTORE v48db1e(0x20), v48db1c(0x4)
    0xb230x48d: v48db23(0x40) = CONST 
    0xb270x48d: v48db27 = SHA3 v48db17(0x0), v48db23(0x40)
    0xb280x48d: v48db28(0xffff) = CONST 
    0xb2c0x48d: v48db2c = AND v4b8, v48db28(0xffff)
    0xb2e0x48d: MSTORE v48db17(0x0), v48db2c
    0xb2f0x48d: v48db2f(0x1) = CONST 
    0xb310x48d: v48db31 = ADD v48db2f(0x1), v48db27
    0xb340x48d: MSTORE v48db1e(0x20), v48db31
    0xb360x48d: v48db36 = SHA3 v48db17(0x0), v48db23(0x40)
    0xb370x48d: v48db37 = SLOAD v48db36

    Begin block 0xb380x48d
    prev=[0xb0b0x48d], succ=[0x2848]
    =================================
    0xb3d0x48d: JUMP v48e(0x2848)

    Begin block 0x2848
    prev=[0xb380x48d], succ=[]
    =================================
    0x2849: v2849(0x40) = CONST 
    0x284c: v284c = MLOAD v2849(0x40)
    0x284f: MSTORE v284c, v48db37
    0x2850: v2850 = MLOAD v2849(0x40)
    0x2854: v2854(0x0) = SUB v284c, v2850
    0x2855: v2855(0x20) = CONST 
    0x2857: v2857(0x20) = ADD v2855(0x20), v2854(0x0)
    0x2859: RETURN v2850, v2857(0x20)

}

function CONTRACT_RING_ERC20_TOKEN()() public {
    Begin block 0x4bd
    prev=[], succ=[0xb3e]
    =================================
    0x4be: v4be(0x2879) = CONST 
    0x4c1: v4c1(0xb3e) = CONST 
    0x4c4: JUMP v4c1(0xb3e)

    Begin block 0xb3e
    prev=[0x4bd], succ=[0x2879]
    =================================
    0xb3f: vb3f(0x434f4e54524143545f52494e475f45524332305f544f4b454e00000000000000) = CONST 
    0xb61: JUMP v4be(0x2879)

    Begin block 0x2879
    prev=[0xb3e], succ=[]
    =================================
    0x287a: v287a(0x40) = CONST 
    0x287d: v287d = MLOAD v287a(0x40)
    0x2880: MSTORE v287d, vb3f(0x434f4e54524143545f52494e475f45524332305f544f4b454e00000000000000)
    0x2881: v2881 = MLOAD v287a(0x40)
    0x2885: v2885(0x0) = SUB v287d, v2881
    0x2886: v2886(0x20) = CONST 
    0x2888: v2888(0x20) = ADD v2886(0x20), v2885(0x0)
    0x288a: RETURN v2881, v2888(0x20)

}

function getRate(address,uint256,uint256)() public {
    Begin block 0x4c5
    prev=[], succ=[0x4d7, 0x4db]
    =================================
    0x4c6: v4c6(0x28aa) = CONST 
    0x4c9: v4c9(0x4) = CONST 
    0x4cc: v4cc = CALLDATASIZE 
    0x4cd: v4cd = SUB v4cc, v4c9(0x4)
    0x4ce: v4ce(0x60) = CONST 
    0x4d1: v4d1 = LT v4cd, v4ce(0x60)
    0x4d2: v4d2 = ISZERO v4d1
    0x4d3: v4d3(0x4db) = CONST 
    0x4d6: JUMPI v4d3(0x4db), v4d2

    Begin block 0x4d7
    prev=[0x4c5], succ=[]
    =================================
    0x4d7: v4d7(0x0) = CONST 
    0x4da: REVERT v4d7(0x0), v4d7(0x0)

    Begin block 0x4db
    prev=[0x4c5], succ=[0xb62]
    =================================
    0x4dd: v4dd(0x1) = CONST 
    0x4df: v4df(0x1) = CONST 
    0x4e1: v4e1(0xa0) = CONST 
    0x4e3: v4e3(0x10000000000000000000000000000000000000000) = SHL v4e1(0xa0), v4df(0x1)
    0x4e4: v4e4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4e3(0x10000000000000000000000000000000000000000), v4dd(0x1)
    0x4e6: v4e6 = CALLDATALOAD v4c9(0x4)
    0x4e7: v4e7 = AND v4e6, v4e4(0xffffffffffffffffffffffffffffffffffffffff)
    0x4e9: v4e9(0x20) = CONST 
    0x4ec: v4ec(0x24) = ADD v4c9(0x4), v4e9(0x20)
    0x4ed: v4ed = CALLDATALOAD v4ec(0x24)
    0x4ef: v4ef(0x40) = CONST 
    0x4f1: v4f1(0x44) = ADD v4ef(0x40), v4c9(0x4)
    0x4f2: v4f2 = CALLDATALOAD v4f1(0x44)
    0x4f3: v4f3(0xb62) = CONST 
    0x4f6: JUMP v4f3(0xb62)

    Begin block 0xb62
    prev=[0x4db], succ=[0xb7a, 0xb73]
    =================================
    0xb63: vb63(0x0) = CONST 
    0xb65: vb65(0x1) = CONST 
    0xb67: vb67(0x1) = CONST 
    0xb69: vb69(0xa0) = CONST 
    0xb6b: vb6b(0x10000000000000000000000000000000000000000) = SHL vb69(0xa0), vb67(0x1)
    0xb6c: vb6c(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb6b(0x10000000000000000000000000000000000000000), vb65(0x1)
    0xb6e: vb6e = AND v4e7, vb6c(0xffffffffffffffffffffffffffffffffffffffff)
    0xb6f: vb6f(0xb7a) = CONST 
    0xb72: JUMPI vb6f(0xb7a), vb6e

    Begin block 0xb7a
    prev=[0xb62], succ=[0xbdd, 0xbe1]
    =================================
    0xb7b: vb7b(0x2) = CONST 
    0xb7d: vb7d = SLOAD vb7b(0x2)
    0xb7e: vb7e(0x40) = CONST 
    0xb81: vb81 = MLOAD vb7e(0x40)
    0xb82: vb82(0x2ecd14d3) = CONST 
    0xb87: vb87(0xe2) = CONST 
    0xb89: vb89(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL vb87(0xe2), vb82(0x2ecd14d3)
    0xb8b: MSTORE vb81, vb89(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0xb8c: vb8c(0x434f4e54524143545f4f424a4543545f4f574e45525348495) = CONST 
    0xba6: vba6(0x3c) = CONST 
    0xba8: vba8(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000) = SHL vba6(0x3c), vb8c(0x434f4e54524143545f4f424a4543545f4f574e45525348495)
    0xba9: vba9(0x4) = CONST 
    0xbac: vbac = ADD vb81, vba9(0x4)
    0xbad: MSTORE vbac, vba8(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000)
    0xbaf: vbaf = MLOAD vb7e(0x40)
    0xbb0: vbb0(0x1) = CONST 
    0xbb2: vbb2(0x1) = CONST 
    0xbb4: vbb4(0xa0) = CONST 
    0xbb6: vbb6(0x10000000000000000000000000000000000000000) = SHL vbb4(0xa0), vbb2(0x1)
    0xbb7: vbb7(0xffffffffffffffffffffffffffffffffffffffff) = SUB vbb6(0x10000000000000000000000000000000000000000), vbb0(0x1)
    0xbba: vbba = AND vb7d, vbb7(0xffffffffffffffffffffffffffffffffffffffff)
    0xbbc: vbbc(0xbb34534c) = CONST 
    0xbc2: vbc2(0x24) = CONST 
    0xbc6: vbc6 = ADD vb81, vbc2(0x24)
    0xbc8: vbc8(0x20) = CONST 
    0xbd0: vbd0(0x0) = SUB vb81, vbaf
    0xbd1: vbd1(0x24) = ADD vbd0(0x0), vbc2(0x24)
    0xbd5: vbd5 = EXTCODESIZE vbba
    0xbd6: vbd6 = ISZERO vbd5
    0xbd8: vbd8 = ISZERO vbd6
    0xbd9: vbd9(0xbe1) = CONST 
    0xbdc: JUMPI vbd9(0xbe1), vbd8

    Begin block 0xbdd
    prev=[0xb7a], succ=[]
    =================================
    0xbdd: vbdd(0x0) = CONST 
    0xbe0: REVERT vbdd(0x0), vbdd(0x0)

    Begin block 0xbe1
    prev=[0xb7a], succ=[0xbec, 0xbf5]
    =================================
    0xbe3: vbe3 = GAS 
    0xbe4: vbe4 = STATICCALL vbe3, vbba, vbaf, vbd1(0x24), vbaf, vbc8(0x20)
    0xbe5: vbe5 = ISZERO vbe4
    0xbe7: vbe7 = ISZERO vbe5
    0xbe8: vbe8(0xbf5) = CONST 
    0xbeb: JUMPI vbe8(0xbf5), vbe7

    Begin block 0xbec
    prev=[0xbe1], succ=[]
    =================================
    0xbec: vbec = RETURNDATASIZE 
    0xbed: vbed(0x0) = CONST 
    0xbf0: RETURNDATACOPY vbed(0x0), vbed(0x0), vbec
    0xbf1: vbf1 = RETURNDATASIZE 
    0xbf2: vbf2(0x0) = CONST 
    0xbf4: REVERT vbf2(0x0), vbf1

    Begin block 0xbf5
    prev=[0xbe1], succ=[0xc07, 0xc0b]
    =================================
    0xbfa: vbfa(0x40) = CONST 
    0xbfc: vbfc = MLOAD vbfa(0x40)
    0xbfd: vbfd = RETURNDATASIZE 
    0xbfe: vbfe(0x20) = CONST 
    0xc01: vc01 = LT vbfd, vbfe(0x20)
    0xc02: vc02 = ISZERO vc01
    0xc03: vc03(0xc0b) = CONST 
    0xc06: JUMPI vc03(0xc0b), vc02

    Begin block 0xc07
    prev=[0xbf5], succ=[]
    =================================
    0xc07: vc07(0x0) = CONST 
    0xc0a: REVERT vc07(0x0), vc07(0x0)

    Begin block 0xc0b
    prev=[0xbf5], succ=[0xc21, 0xe8f]
    =================================
    0xc0d: vc0d = MLOAD vbfc
    0xc0e: vc0e(0x1) = CONST 
    0xc10: vc10(0x1) = CONST 
    0xc12: vc12(0xa0) = CONST 
    0xc14: vc14(0x10000000000000000000000000000000000000000) = SHL vc12(0xa0), vc10(0x1)
    0xc15: vc15(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc14(0x10000000000000000000000000000000000000000), vc0e(0x1)
    0xc18: vc18 = AND vc15(0xffffffffffffffffffffffffffffffffffffffff), v4e7
    0xc1a: vc1a = AND vc0d, vc15(0xffffffffffffffffffffffffffffffffffffffff)
    0xc1b: vc1b = EQ vc1a, vc18
    0xc1c: vc1c = ISZERO vc1b
    0xc1d: vc1d(0xe8f) = CONST 
    0xc20: JUMPI vc1d(0xe8f), vc1c

    Begin block 0xc21
    prev=[0xc0b], succ=[0xc87, 0xc8b]
    =================================
    0xc21: vc21(0x2) = CONST 
    0xc23: vc23 = SLOAD vc21(0x2)
    0xc24: vc24(0x40) = CONST 
    0xc27: vc27 = MLOAD vc24(0x40)
    0xc28: vc28(0x2ecd14d3) = CONST 
    0xc2d: vc2d(0xe2) = CONST 
    0xc2f: vc2f(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL vc2d(0xe2), vc28(0x2ecd14d3)
    0xc31: MSTORE vc27, vc2f(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0xc32: vc32(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000) = CONST 
    0xc53: vc53(0x4) = CONST 
    0xc56: vc56 = ADD vc27, vc53(0x4)
    0xc57: MSTORE vc56, vc32(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000)
    0xc59: vc59 = MLOAD vc24(0x40)
    0xc5a: vc5a(0x0) = CONST 
    0xc5d: vc5d(0x1) = CONST 
    0xc5f: vc5f(0x1) = CONST 
    0xc61: vc61(0xa0) = CONST 
    0xc63: vc63(0x10000000000000000000000000000000000000000) = SHL vc61(0xa0), vc5f(0x1)
    0xc64: vc64(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc63(0x10000000000000000000000000000000000000000), vc5d(0x1)
    0xc65: vc65 = AND vc64(0xffffffffffffffffffffffffffffffffffffffff), vc23
    0xc67: vc67(0xbb34534c) = CONST 
    0xc6d: vc6d(0x24) = CONST 
    0xc71: vc71 = ADD vc27, vc6d(0x24)
    0xc73: vc73(0x20) = CONST 
    0xc7a: vc7a(0x0) = SUB vc27, vc59
    0xc7b: vc7b(0x24) = ADD vc7a(0x0), vc6d(0x24)
    0xc7f: vc7f = EXTCODESIZE vc65
    0xc80: vc80 = ISZERO vc7f
    0xc82: vc82 = ISZERO vc80
    0xc83: vc83(0xc8b) = CONST 
    0xc86: JUMPI vc83(0xc8b), vc82

    Begin block 0xc87
    prev=[0xc21], succ=[]
    =================================
    0xc87: vc87(0x0) = CONST 
    0xc8a: REVERT vc87(0x0), vc87(0x0)

    Begin block 0xc8b
    prev=[0xc21], succ=[0xc96, 0xc9f]
    =================================
    0xc8d: vc8d = GAS 
    0xc8e: vc8e = STATICCALL vc8d, vc65, vc59, vc7b(0x24), vc59, vc73(0x20)
    0xc8f: vc8f = ISZERO vc8e
    0xc91: vc91 = ISZERO vc8f
    0xc92: vc92(0xc9f) = CONST 
    0xc95: JUMPI vc92(0xc9f), vc91

    Begin block 0xc96
    prev=[0xc8b], succ=[]
    =================================
    0xc96: vc96 = RETURNDATASIZE 
    0xc97: vc97(0x0) = CONST 
    0xc9a: RETURNDATACOPY vc97(0x0), vc97(0x0), vc96
    0xc9b: vc9b = RETURNDATASIZE 
    0xc9c: vc9c(0x0) = CONST 
    0xc9e: REVERT vc9c(0x0), vc9b

    Begin block 0xc9f
    prev=[0xc8b], succ=[0xcb1, 0xcb5]
    =================================
    0xca4: vca4(0x40) = CONST 
    0xca6: vca6 = MLOAD vca4(0x40)
    0xca7: vca7 = RETURNDATASIZE 
    0xca8: vca8(0x20) = CONST 
    0xcab: vcab = LT vca7, vca8(0x20)
    0xcac: vcac = ISZERO vcab
    0xcad: vcad(0xcb5) = CONST 
    0xcb0: JUMPI vcad(0xcb5), vcac

    Begin block 0xcb1
    prev=[0xc9f], succ=[]
    =================================
    0xcb1: vcb1(0x0) = CONST 
    0xcb4: REVERT vcb1(0x0), vcb1(0x0)

    Begin block 0xcb5
    prev=[0xc9f], succ=[0xcfc, 0xd00]
    =================================
    0xcb7: vcb7 = MLOAD vca6
    0xcb8: vcb8(0x40) = CONST 
    0xcbb: vcbb = MLOAD vcb8(0x40)
    0xcbc: vcbc(0xf44a67e1) = CONST 
    0xcc1: vcc1(0xe0) = CONST 
    0xcc3: vcc3(0xf44a67e100000000000000000000000000000000000000000000000000000000) = SHL vcc1(0xe0), vcbc(0xf44a67e1)
    0xcc5: MSTORE vcbb, vcc3(0xf44a67e100000000000000000000000000000000000000000000000000000000)
    0xcc6: vcc6(0x4) = CONST 
    0xcc9: vcc9 = ADD vcbb, vcc6(0x4)
    0xccc: MSTORE vcc9, v4ed
    0xcce: vcce = MLOAD vcb8(0x40)
    0xccf: vccf(0x1) = CONST 
    0xcd1: vcd1(0x1) = CONST 
    0xcd3: vcd3(0xa0) = CONST 
    0xcd5: vcd5(0x10000000000000000000000000000000000000000) = SHL vcd3(0xa0), vcd1(0x1)
    0xcd6: vcd6(0xffffffffffffffffffffffffffffffffffffffff) = SUB vcd5(0x10000000000000000000000000000000000000000), vccf(0x1)
    0xcd9: vcd9 = AND vcb7, vcd6(0xffffffffffffffffffffffffffffffffffffffff)
    0xcdb: vcdb(0xf44a67e1) = CONST 
    0xce1: vce1(0x24) = CONST 
    0xce5: vce5 = ADD vcbb, vce1(0x24)
    0xce7: vce7(0x20) = CONST 
    0xcef: vcef(0x0) = SUB vcbb, vcce
    0xcf0: vcf0(0x24) = ADD vcef(0x0), vce1(0x24)
    0xcf4: vcf4 = EXTCODESIZE vcd9
    0xcf5: vcf5 = ISZERO vcf4
    0xcf7: vcf7 = ISZERO vcf5
    0xcf8: vcf8(0xd00) = CONST 
    0xcfb: JUMPI vcf8(0xd00), vcf7

    Begin block 0xcfc
    prev=[0xcb5], succ=[]
    =================================
    0xcfc: vcfc(0x0) = CONST 
    0xcff: REVERT vcfc(0x0), vcfc(0x0)

    Begin block 0xd00
    prev=[0xcb5], succ=[0xd0b, 0xd14]
    =================================
    0xd02: vd02 = GAS 
    0xd03: vd03 = STATICCALL vd02, vcd9, vcce, vcf0(0x24), vcce, vce7(0x20)
    0xd04: vd04 = ISZERO vd03
    0xd06: vd06 = ISZERO vd04
    0xd07: vd07(0xd14) = CONST 
    0xd0a: JUMPI vd07(0xd14), vd06

    Begin block 0xd0b
    prev=[0xd00], succ=[]
    =================================
    0xd0b: vd0b = RETURNDATASIZE 
    0xd0c: vd0c(0x0) = CONST 
    0xd0f: RETURNDATACOPY vd0c(0x0), vd0c(0x0), vd0b
    0xd10: vd10 = RETURNDATASIZE 
    0xd11: vd11(0x0) = CONST 
    0xd13: REVERT vd11(0x0), vd10

    Begin block 0xd14
    prev=[0xd00], succ=[0xd26, 0xd2a]
    =================================
    0xd19: vd19(0x40) = CONST 
    0xd1b: vd1b = MLOAD vd19(0x40)
    0xd1c: vd1c = RETURNDATASIZE 
    0xd1d: vd1d(0x20) = CONST 
    0xd20: vd20 = LT vd1c, vd1d(0x20)
    0xd21: vd21 = ISZERO vd20
    0xd22: vd22(0xd2a) = CONST 
    0xd25: JUMPI vd22(0xd2a), vd21

    Begin block 0xd26
    prev=[0xd14], succ=[]
    =================================
    0xd26: vd26(0x0) = CONST 
    0xd29: REVERT vd26(0x0), vd26(0x0)

    Begin block 0xd2a
    prev=[0xd14], succ=[0xd3b, 0xe4b]
    =================================
    0xd2c: vd2c = MLOAD vd1b
    0xd2f: vd2f(0xff) = CONST 
    0xd32: vd32 = AND vd2c, vd2f(0xff)
    0xd33: vd33(0x5) = CONST 
    0xd35: vd35 = EQ vd33(0x5), vd32
    0xd36: vd36 = ISZERO vd35
    0xd37: vd37(0xe4b) = CONST 
    0xd3a: JUMPI vd37(0xe4b), vd36

    Begin block 0xd3b
    prev=[0xd2a], succ=[0xd96, 0xd9a]
    =================================
    0xd3b: vd3b(0x2) = CONST 
    0xd3d: vd3d = SLOAD vd3b(0x2)
    0xd3e: vd3e(0x40) = CONST 
    0xd41: vd41 = MLOAD vd3e(0x40)
    0xd42: vd42(0x2ecd14d3) = CONST 
    0xd47: vd47(0xe2) = CONST 
    0xd49: vd49(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL vd47(0xe2), vd42(0x2ecd14d3)
    0xd4b: MSTORE vd41, vd49(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0xd4c: vd4c(0x434f4e54524143545f4954454d5f42415345) = CONST 
    0xd5f: vd5f(0x70) = CONST 
    0xd61: vd61(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000) = SHL vd5f(0x70), vd4c(0x434f4e54524143545f4954454d5f42415345)
    0xd62: vd62(0x4) = CONST 
    0xd65: vd65 = ADD vd41, vd62(0x4)
    0xd66: MSTORE vd65, vd61(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000)
    0xd68: vd68 = MLOAD vd3e(0x40)
    0xd69: vd69(0x1) = CONST 
    0xd6b: vd6b(0x1) = CONST 
    0xd6d: vd6d(0xa0) = CONST 
    0xd6f: vd6f(0x10000000000000000000000000000000000000000) = SHL vd6d(0xa0), vd6b(0x1)
    0xd70: vd70(0xffffffffffffffffffffffffffffffffffffffff) = SUB vd6f(0x10000000000000000000000000000000000000000), vd69(0x1)
    0xd73: vd73 = AND vd3d, vd70(0xffffffffffffffffffffffffffffffffffffffff)
    0xd75: vd75(0xbb34534c) = CONST 
    0xd7b: vd7b(0x24) = CONST 
    0xd7f: vd7f = ADD vd41, vd7b(0x24)
    0xd81: vd81(0x20) = CONST 
    0xd89: vd89(0x0) = SUB vd41, vd68
    0xd8a: vd8a(0x24) = ADD vd89(0x0), vd7b(0x24)
    0xd8e: vd8e = EXTCODESIZE vd73
    0xd8f: vd8f = ISZERO vd8e
    0xd91: vd91 = ISZERO vd8f
    0xd92: vd92(0xd9a) = CONST 
    0xd95: JUMPI vd92(0xd9a), vd91

    Begin block 0xd96
    prev=[0xd3b], succ=[]
    =================================
    0xd96: vd96(0x0) = CONST 
    0xd99: REVERT vd96(0x0), vd96(0x0)

    Begin block 0xd9a
    prev=[0xd3b], succ=[0xda5, 0xdae]
    =================================
    0xd9c: vd9c = GAS 
    0xd9d: vd9d = STATICCALL vd9c, vd73, vd68, vd8a(0x24), vd68, vd81(0x20)
    0xd9e: vd9e = ISZERO vd9d
    0xda0: vda0 = ISZERO vd9e
    0xda1: vda1(0xdae) = CONST 
    0xda4: JUMPI vda1(0xdae), vda0

    Begin block 0xda5
    prev=[0xd9a], succ=[]
    =================================
    0xda5: vda5 = RETURNDATASIZE 
    0xda6: vda6(0x0) = CONST 
    0xda9: RETURNDATACOPY vda6(0x0), vda6(0x0), vda5
    0xdaa: vdaa = RETURNDATASIZE 
    0xdab: vdab(0x0) = CONST 
    0xdad: REVERT vdab(0x0), vdaa

    Begin block 0xdae
    prev=[0xd9a], succ=[0xdc0, 0xdc4]
    =================================
    0xdb3: vdb3(0x40) = CONST 
    0xdb5: vdb5 = MLOAD vdb3(0x40)
    0xdb6: vdb6 = RETURNDATASIZE 
    0xdb7: vdb7(0x20) = CONST 
    0xdba: vdba = LT vdb6, vdb7(0x20)
    0xdbb: vdbb = ISZERO vdba
    0xdbc: vdbc(0xdc4) = CONST 
    0xdbf: JUMPI vdbc(0xdc4), vdbb

    Begin block 0xdc0
    prev=[0xdae], succ=[]
    =================================
    0xdc0: vdc0(0x0) = CONST 
    0xdc3: REVERT vdc0(0x0), vdc0(0x0)

    Begin block 0xdc4
    prev=[0xdae], succ=[0xe12, 0xe16]
    =================================
    0xdc6: vdc6 = MLOAD vdb5
    0xdc7: vdc7(0x40) = CONST 
    0xdca: vdca = MLOAD vdc7(0x40)
    0xdcb: vdcb(0xd70e7e3) = CONST 
    0xdd0: vdd0(0xe0) = CONST 
    0xdd2: vdd2(0xd70e7e300000000000000000000000000000000000000000000000000000000) = SHL vdd0(0xe0), vdcb(0xd70e7e3)
    0xdd4: MSTORE vdca, vdd2(0xd70e7e300000000000000000000000000000000000000000000000000000000)
    0xdd5: vdd5(0x4) = CONST 
    0xdd8: vdd8 = ADD vdca, vdd5(0x4)
    0xddb: MSTORE vdd8, v4ed
    0xddc: vddc(0x24) = CONST 
    0xddf: vddf = ADD vdca, vddc(0x24)
    0xde2: MSTORE vddf, v4f2
    0xde4: vde4 = MLOAD vdc7(0x40)
    0xde5: vde5(0x1) = CONST 
    0xde7: vde7(0x1) = CONST 
    0xde9: vde9(0xa0) = CONST 
    0xdeb: vdeb(0x10000000000000000000000000000000000000000) = SHL vde9(0xa0), vde7(0x1)
    0xdec: vdec(0xffffffffffffffffffffffffffffffffffffffff) = SUB vdeb(0x10000000000000000000000000000000000000000), vde5(0x1)
    0xdef: vdef = AND vdc6, vdec(0xffffffffffffffffffffffffffffffffffffffff)
    0xdf1: vdf1(0xd70e7e3) = CONST 
    0xdf7: vdf7(0x44) = CONST 
    0xdfb: vdfb = ADD vdca, vdf7(0x44)
    0xdfd: vdfd(0x20) = CONST 
    0xe05: ve05(0x0) = SUB vdca, vde4
    0xe06: ve06(0x44) = ADD ve05(0x0), vdf7(0x44)
    0xe0a: ve0a = EXTCODESIZE vdef
    0xe0b: ve0b = ISZERO ve0a
    0xe0d: ve0d = ISZERO ve0b
    0xe0e: ve0e(0xe16) = CONST 
    0xe11: JUMPI ve0e(0xe16), ve0d

    Begin block 0xe12
    prev=[0xdc4], succ=[]
    =================================
    0xe12: ve12(0x0) = CONST 
    0xe15: REVERT ve12(0x0), ve12(0x0)

    Begin block 0xe16
    prev=[0xdc4], succ=[0xe21, 0xe2a]
    =================================
    0xe18: ve18 = GAS 
    0xe19: ve19 = STATICCALL ve18, vdef, vde4, ve06(0x44), vde4, vdfd(0x20)
    0xe1a: ve1a = ISZERO ve19
    0xe1c: ve1c = ISZERO ve1a
    0xe1d: ve1d(0xe2a) = CONST 
    0xe20: JUMPI ve1d(0xe2a), ve1c

    Begin block 0xe21
    prev=[0xe16], succ=[]
    =================================
    0xe21: ve21 = RETURNDATASIZE 
    0xe22: ve22(0x0) = CONST 
    0xe25: RETURNDATACOPY ve22(0x0), ve22(0x0), ve21
    0xe26: ve26 = RETURNDATASIZE 
    0xe27: ve27(0x0) = CONST 
    0xe29: REVERT ve27(0x0), ve26

    Begin block 0xe2a
    prev=[0xe16], succ=[0xe3c, 0xe40]
    =================================
    0xe2f: ve2f(0x40) = CONST 
    0xe31: ve31 = MLOAD ve2f(0x40)
    0xe32: ve32 = RETURNDATASIZE 
    0xe33: ve33(0x20) = CONST 
    0xe36: ve36 = LT ve32, ve33(0x20)
    0xe37: ve37 = ISZERO ve36
    0xe38: ve38(0xe40) = CONST 
    0xe3b: JUMPI ve38(0xe40), ve37

    Begin block 0xe3c
    prev=[0xe2a], succ=[]
    =================================
    0xe3c: ve3c(0x0) = CONST 
    0xe3f: REVERT ve3c(0x0), ve3c(0x0)

    Begin block 0xe40
    prev=[0xe2a], succ=[0x317d]
    =================================
    0xe42: ve42 = MLOAD ve31
    0xe45: ve45(0x317d) = CONST 
    0xe4a: JUMP ve45(0x317d)

    Begin block 0x317d
    prev=[0xe40], succ=[0x28aa]
    =================================
    0x3183: JUMP v4c6(0x28aa)

    Begin block 0x28aa
    prev=[0x3157, 0x317d, 0x31a3, 0xe9d], succ=[]
    =================================
    0x28aa_0x0: v28aa_0 = PHI vb74(0x0), ve42, v4c515b6, vaa6b37Ve8f
    0x28ab: v28ab(0x40) = CONST 
    0x28ae: v28ae = MLOAD v28ab(0x40)
    0x28b1: MSTORE v28ae, v28aa_0
    0x28b2: v28b2 = MLOAD v28ab(0x40)
    0x28b6: v28b6(0x0) = SUB v28ae, v28b2
    0x28b7: v28b7(0x20) = CONST 
    0x28b9: v28b9(0x20) = ADD v28b7(0x20), v28b6(0x0)
    0x28bb: RETURN v28b2, v28b9(0x20)

    Begin block 0xe4b
    prev=[0xd2a], succ=[0xe58, 0xe8d]
    =================================
    0xe4c: ve4c(0xff) = CONST 
    0xe4f: ve4f = AND vd2c, ve4c(0xff)
    0xe50: ve50(0x4) = CONST 
    0xe52: ve52 = EQ ve50(0x4), ve4f
    0xe53: ve53 = ISZERO ve52
    0xe54: ve54(0xe8d) = CONST 
    0xe57: JUMPI ve54(0xe8d), ve53

    Begin block 0xe58
    prev=[0xe4b], succ=[0x14f2B0xe58]
    =================================
    0xe58: ve58(0x0) = CONST 
    0xe5a: ve5a(0xe62) = CONST 
    0xe5e: ve5e(0x14f2) = CONST 
    0xe61: JUMP ve5e(0x14f2)

    Begin block 0x14f2B0xe58
    prev=[0xe58], succ=[0xe62]
    =================================
    0x14f3S0xe58: v14f3Ve58(0x70) = CONST 
    0x14f5S0xe58: v14f5Ve58 = SHR v14f3Ve58(0x70), v4ed
    0x14f6S0xe58: v14f6Ve58(0xffff) = CONST 
    0x14f9S0xe58: v14f9Ve58 = AND v14f6Ve58(0xffff), v14f5Ve58
    0x14fbS0xe58: JUMP ve5a(0xe62)

    Begin block 0xe62
    prev=[0x14f2B0xe58], succ=[0x152f0x4c5]
    =================================
    0xe65: ve65(0xe84) = CONST 
    0xe68: ve68(0x434f4e54524143545f4452494c4c5f42415345) = CONST 
    0xe7c: ve7c(0x68) = CONST 
    0xe7e: ve7e(0x434f4e54524143545f4452494c4c5f4241534500000000000000000000000000) = SHL ve7c(0x68), ve68(0x434f4e54524143545f4452494c4c5f42415345)
    0xe80: ve80(0x152f) = CONST 
    0xe83: JUMP ve80(0x152f)

    Begin block 0x152f0x4c5
    prev=[0xe62], succ=[0x15520x4c5, 0x15950x4c5]
    =================================
    0x15300x4c5: v4c51530(0x0) = CONST 
    0x15340x4c5: MSTORE v4c51530(0x0), ve7e(0x434f4e54524143545f4452494c4c5f4241534500000000000000000000000000)
    0x15350x4c5: v4c51535(0x5) = CONST 
    0x15370x4c5: v4c51537(0x20) = CONST 
    0x153b0x4c5: MSTORE v4c51537(0x20), v4c51535(0x5)
    0x153c0x4c5: v4c5153c(0x40) = CONST 
    0x15400x4c5: v4c51540 = SHA3 v4c51530(0x0), v4c5153c(0x40)
    0x15410x4c5: v4c51541(0xffff) = CONST 
    0x15450x4c5: v4c51545 = AND v14f9Ve58, v4c51541(0xffff)
    0x15470x4c5: MSTORE v4c51530(0x0), v4c51545
    0x154a0x4c5: MSTORE v4c51537(0x20), v4c51540
    0x154c0x4c5: v4c5154c = SHA3 v4c51530(0x0), v4c5153c(0x40)
    0x154d0x4c5: v4c5154d = SLOAD v4c5154c
    0x154e0x4c5: v4c5154e(0x1595) = CONST 
    0x15510x4c5: JUMPI v4c5154e(0x1595), v4c5154d

    Begin block 0x15520x4c5
    prev=[0x152f0x4c5], succ=[]
    =================================
    0x15520x4c5: v4c51552(0x40) = CONST 
    0x15550x4c5: v4c51555 = MLOAD v4c51552(0x40)
    0x15560x4c5: v4c51556(0x461bcd) = CONST 
    0x155a0x4c5: v4c5155a(0xe5) = CONST 
    0x155c0x4c5: v4c5155c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v4c5155a(0xe5), v4c51556(0x461bcd)
    0x155e0x4c5: MSTORE v4c51555, v4c5155c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x155f0x4c5: v4c5155f(0x20) = CONST 
    0x15610x4c5: v4c51561(0x4) = CONST 
    0x15640x4c5: v4c51564 = ADD v4c51555, v4c51561(0x4)
    0x15650x4c5: MSTORE v4c51564, v4c5155f(0x20)
    0x15660x4c5: v4c51566(0x14) = CONST 
    0x15680x4c5: v4c51568(0x24) = CONST 
    0x156b0x4c5: v4c5156b = ADD v4c51555, v4c51568(0x24)
    0x156c0x4c5: MSTORE v4c5156b, v4c51566(0x14)
    0x156d0x4c5: v4c5156d(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0x15820x4c5: v4c51582(0x62) = CONST 
    0x15840x4c5: v4c51584(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL v4c51582(0x62), v4c5156d(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0x15850x4c5: v4c51585(0x44) = CONST 
    0x15880x4c5: v4c51588 = ADD v4c51555, v4c51585(0x44)
    0x15890x4c5: MSTORE v4c51588, v4c51584(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0x158b0x4c5: v4c5158b = MLOAD v4c51552(0x40)
    0x158f0x4c5: v4c5158f(0x0) = SUB v4c51555, v4c5158b
    0x15900x4c5: v4c51590(0x64) = CONST 
    0x15920x4c5: v4c51592(0x64) = ADD v4c51590(0x64), v4c5158f(0x0)
    0x15940x4c5: REVERT v4c5158b, v4c51592(0x64)

    Begin block 0x15950x4c5
    prev=[0x152f0x4c5], succ=[0xe84]
    =================================
    0x15970x4c5: v4c51597(0x0) = CONST 
    0x159b0x4c5: MSTORE v4c51597(0x0), ve7e(0x434f4e54524143545f4452494c4c5f4241534500000000000000000000000000)
    0x159c0x4c5: v4c5159c(0x5) = CONST 
    0x159e0x4c5: v4c5159e(0x20) = CONST 
    0x15a20x4c5: MSTORE v4c5159e(0x20), v4c5159c(0x5)
    0x15a30x4c5: v4c515a3(0x40) = CONST 
    0x15a70x4c5: v4c515a7 = SHA3 v4c51597(0x0), v4c515a3(0x40)
    0x15a80x4c5: v4c515a8(0xffff) = CONST 
    0x15ae0x4c5: v4c515ae = AND v4c515a8(0xffff), v14f9Ve58
    0x15b00x4c5: MSTORE v4c51597(0x0), v4c515ae
    0x15b30x4c5: MSTORE v4c5159e(0x20), v4c515a7
    0x15b50x4c5: v4c515b5 = SHA3 v4c51597(0x0), v4c515a3(0x40)
    0x15b60x4c5: v4c515b6 = SLOAD v4c515b5
    0x15b80x4c5: JUMP ve65(0xe84)

    Begin block 0xe84
    prev=[0x15950x4c5], succ=[0x31a3]
    =================================
    0xe89: ve89(0x31a3) = CONST 
    0xe8c: JUMP ve89(0x31a3)

    Begin block 0x31a3
    prev=[0xe84], succ=[0x28aa]
    =================================
    0x31a9: JUMP v4c6(0x28aa)

    Begin block 0xe8d
    prev=[0xe4b], succ=[0xe8f]
    =================================

    Begin block 0xe8f
    prev=[0xc0b, 0xe8d], succ=[0xaa6B0xe8f]
    =================================
    0xe90: ve90(0xe9a) = CONST 
    0xe94: ve94(0x1) = CONST 
    0xe96: ve96(0xaa6) = CONST 
    0xe99: JUMP ve96(0xaa6)

    Begin block 0xaa6B0xe8f
    prev=[0xe8f], succ=[0xac80xaa6B0xe8f, 0xb0b0xaa6B0xe8f]
    =================================
    0xaa7S0xe8f: vaa7Ve8f(0x1) = CONST 
    0xaa9S0xe8f: vaa9Ve8f(0x1) = CONST 
    0xaabS0xe8f: vaabVe8f(0xa0) = CONST 
    0xaadS0xe8f: vaadVe8f(0x10000000000000000000000000000000000000000) = SHL vaabVe8f(0xa0), vaa9Ve8f(0x1)
    0xaaeS0xe8f: vaaeVe8f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaadVe8f(0x10000000000000000000000000000000000000000), vaa7Ve8f(0x1)
    0xab0S0xe8f: vab0Ve8f = AND v4e7, vaaeVe8f(0xffffffffffffffffffffffffffffffffffffffff)
    0xab1S0xe8f: vab1Ve8f(0x0) = CONST 
    0xab5S0xe8f: MSTORE vab1Ve8f(0x0), vab0Ve8f
    0xab6S0xe8f: vab6Ve8f(0x4) = CONST 
    0xab8S0xe8f: vab8Ve8f(0x20) = CONST 
    0xabaS0xe8f: MSTORE vab8Ve8f(0x20), vab6Ve8f(0x4)
    0xabbS0xe8f: vabbVe8f(0x40) = CONST 
    0xabeS0xe8f: vabeVe8f = SHA3 vab1Ve8f(0x0), vabbVe8f(0x40)
    0xabfS0xe8f: vabfVe8f = SLOAD vabeVe8f
    0xac0S0xe8f: vac0Ve8f(0xffff) = CONST 
    0xac3S0xe8f: vac3Ve8f = AND vac0Ve8f(0xffff), vabfVe8f
    0xac4S0xe8f: vac4Ve8f(0xb0b) = CONST 
    0xac7S0xe8f: JUMPI vac4Ve8f(0xb0b), vac3Ve8f

    Begin block 0xac80xaa6B0xe8f
    prev=[0xaa6B0xe8f], succ=[]
    =================================
    0xac80xaa6S0xe8f: vaa6ac8Ve8f(0x40) = CONST 
    0xacb0xaa6S0xe8f: vaa6acbVe8f = MLOAD vaa6ac8Ve8f(0x40)
    0xacc0xaa6S0xe8f: vaa6accVe8f(0x461bcd) = CONST 
    0xad00xaa6S0xe8f: vaa6ad0Ve8f(0xe5) = CONST 
    0xad20xaa6S0xe8f: vaa6ad2Ve8f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL vaa6ad0Ve8f(0xe5), vaa6accVe8f(0x461bcd)
    0xad40xaa6S0xe8f: MSTORE vaa6acbVe8f, vaa6ad2Ve8f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0xad50xaa6S0xe8f: vaa6ad5Ve8f(0x20) = CONST 
    0xad70xaa6S0xe8f: vaa6ad7Ve8f(0x4) = CONST 
    0xada0xaa6S0xe8f: vaa6adaVe8f = ADD vaa6acbVe8f, vaa6ad7Ve8f(0x4)
    0xadb0xaa6S0xe8f: MSTORE vaa6adaVe8f, vaa6ad5Ve8f(0x20)
    0xadc0xaa6S0xe8f: vaa6adcVe8f(0x14) = CONST 
    0xade0xaa6S0xe8f: vaa6adeVe8f(0x24) = CONST 
    0xae10xaa6S0xe8f: vaa6ae1Ve8f = ADD vaa6acbVe8f, vaa6adeVe8f(0x24)
    0xae20xaa6S0xe8f: MSTORE vaa6ae1Ve8f, vaa6adcVe8f(0x14)
    0xae30xaa6S0xe8f: vaa6ae3Ve8f(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0xaf80xaa6S0xe8f: vaa6af8Ve8f(0x62) = CONST 
    0xafa0xaa6S0xe8f: vaa6afaVe8f(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL vaa6af8Ve8f(0x62), vaa6ae3Ve8f(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0xafb0xaa6S0xe8f: vaa6afbVe8f(0x44) = CONST 
    0xafe0xaa6S0xe8f: vaa6afeVe8f = ADD vaa6acbVe8f, vaa6afbVe8f(0x44)
    0xaff0xaa6S0xe8f: MSTORE vaa6afeVe8f, vaa6afaVe8f(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0xb010xaa6S0xe8f: vaa6b01Ve8f = MLOAD vaa6ac8Ve8f(0x40)
    0xb050xaa6S0xe8f: vaa6b05Ve8f(0x0) = SUB vaa6acbVe8f, vaa6b01Ve8f
    0xb060xaa6S0xe8f: vaa6b06Ve8f(0x64) = CONST 
    0xb080xaa6S0xe8f: vaa6b08Ve8f(0x64) = ADD vaa6b06Ve8f(0x64), vaa6b05Ve8f(0x0)
    0xb0a0xaa6S0xe8f: REVERT vaa6b01Ve8f, vaa6b08Ve8f(0x64)

    Begin block 0xb0b0xaa6B0xe8f
    prev=[0xaa6B0xe8f], succ=[0xb380xaa6B0xe8f]
    =================================
    0xb0d0xaa6S0xe8f: vaa6b0dVe8f(0x1) = CONST 
    0xb0f0xaa6S0xe8f: vaa6b0fVe8f(0x1) = CONST 
    0xb110xaa6S0xe8f: vaa6b11Ve8f(0xa0) = CONST 
    0xb130xaa6S0xe8f: vaa6b13Ve8f(0x10000000000000000000000000000000000000000) = SHL vaa6b11Ve8f(0xa0), vaa6b0fVe8f(0x1)
    0xb140xaa6S0xe8f: vaa6b14Ve8f(0xffffffffffffffffffffffffffffffffffffffff) = SUB vaa6b13Ve8f(0x10000000000000000000000000000000000000000), vaa6b0dVe8f(0x1)
    0xb160xaa6S0xe8f: vaa6b16Ve8f = AND v4e7, vaa6b14Ve8f(0xffffffffffffffffffffffffffffffffffffffff)
    0xb170xaa6S0xe8f: vaa6b17Ve8f(0x0) = CONST 
    0xb1b0xaa6S0xe8f: MSTORE vaa6b17Ve8f(0x0), vaa6b16Ve8f
    0xb1c0xaa6S0xe8f: vaa6b1cVe8f(0x4) = CONST 
    0xb1e0xaa6S0xe8f: vaa6b1eVe8f(0x20) = CONST 
    0xb220xaa6S0xe8f: MSTORE vaa6b1eVe8f(0x20), vaa6b1cVe8f(0x4)
    0xb230xaa6S0xe8f: vaa6b23Ve8f(0x40) = CONST 
    0xb270xaa6S0xe8f: vaa6b27Ve8f = SHA3 vaa6b17Ve8f(0x0), vaa6b23Ve8f(0x40)
    0xb280xaa6S0xe8f: vaa6b28Ve8f(0xffff) = CONST 
    0xb2c0xaa6S0xe8f: vaa6b2cVe8f(0x1) = AND ve94(0x1), vaa6b28Ve8f(0xffff)
    0xb2e0xaa6S0xe8f: MSTORE vaa6b17Ve8f(0x0), vaa6b2cVe8f(0x1)
    0xb2f0xaa6S0xe8f: vaa6b2fVe8f(0x1) = CONST 
    0xb310xaa6S0xe8f: vaa6b31Ve8f = ADD vaa6b2fVe8f(0x1), vaa6b27Ve8f
    0xb340xaa6S0xe8f: MSTORE vaa6b1eVe8f(0x20), vaa6b31Ve8f
    0xb360xaa6S0xe8f: vaa6b36Ve8f = SHA3 vaa6b17Ve8f(0x0), vaa6b23Ve8f(0x40)
    0xb370xaa6S0xe8f: vaa6b37Ve8f = SLOAD vaa6b36Ve8f

    Begin block 0xb380xaa6B0xe8f
    prev=[0xb0b0xaa6B0xe8f], succ=[0xe9a]
    =================================
    0xb3d0xaa6S0xe8f: JUMP ve90(0xe9a)

    Begin block 0xe9a
    prev=[0xb380xaa6B0xe8f], succ=[0xe9d]
    =================================

    Begin block 0xe9d
    prev=[0xe9a], succ=[0x28aa]
    =================================
    0xea3: JUMP v4c6(0x28aa)

    Begin block 0xb73
    prev=[0xb62], succ=[0x3157]
    =================================
    0xb74: vb74(0x0) = CONST 
    0xb76: vb76(0x3157) = CONST 
    0xb79: JUMP vb76(0x3157)

    Begin block 0x3157
    prev=[0xb73], succ=[0x28aa]
    =================================
    0x315d: JUMP v4c6(0x28aa)

}

function CONTRACT_LAND_ITEM_BAR()() public {
    Begin block 0x4f7
    prev=[], succ=[0xea4]
    =================================
    0x4f8: v4f8(0x28db) = CONST 
    0x4fb: v4fb(0xea4) = CONST 
    0x4fe: JUMP v4fb(0xea4)

    Begin block 0xea4
    prev=[0x4f7], succ=[0x28db]
    =================================
    0xea5: vea5(0x21a7a72a2920a1aa2fa620a7222fa4aa22a6afa120a9) = CONST 
    0xebc: vebc(0x51) = CONST 
    0xebe: vebe(0x434f4e54524143545f4c414e445f4954454d5f42415200000000000000000000) = SHL vebc(0x51), vea5(0x21a7a72a2920a1aa2fa620a7222fa4aa22a6afa120a9)
    0xec0: JUMP v4f8(0x28db)

    Begin block 0x28db
    prev=[0xea4], succ=[]
    =================================
    0x28dc: v28dc(0x40) = CONST 
    0x28df: v28df = MLOAD v28dc(0x40)
    0x28e2: MSTORE v28df, vebe(0x434f4e54524143545f4c414e445f4954454d5f42415200000000000000000000)
    0x28e3: v28e3 = MLOAD v28dc(0x40)
    0x28e7: v28e7(0x0) = SUB v28df, v28e3
    0x28e8: v28e8(0x20) = CONST 
    0x28ea: v28ea(0x20) = ADD v28e8(0x20), v28e7(0x0)
    0x28ec: RETURN v28e3, v28ea(0x20)

}

function CONTRACT_LP_WOOD_ERC20_TOKEN()() public {
    Begin block 0x4ff
    prev=[], succ=[0xec1]
    =================================
    0x500: v500(0x290c) = CONST 
    0x503: v503(0xec1) = CONST 
    0x506: JUMP v503(0xec1)

    Begin block 0xec1
    prev=[0x4ff], succ=[0x290c]
    =================================
    0xec2: vec2(0x434f4e54524143545f4c505f574f4f445f45524332305f544f4b454e00000000) = CONST 
    0xee4: JUMP v500(0x290c)

    Begin block 0x290c
    prev=[0xec1], succ=[]
    =================================
    0x290d: v290d(0x40) = CONST 
    0x2910: v2910 = MLOAD v290d(0x40)
    0x2913: MSTORE v2910, vec2(0x434f4e54524143545f4c505f574f4f445f45524332305f544f4b454e00000000)
    0x2914: v2914 = MLOAD v290d(0x40)
    0x2918: v2918(0x0) = SUB v2910, v2914
    0x2919: v2919(0x20) = CONST 
    0x291b: v291b(0x20) = ADD v2919(0x20), v2918(0x0)
    0x291d: RETURN v2914, v291b(0x20)

}

function CONTRACT_ERC721_GEGO()() public {
    Begin block 0x507
    prev=[], succ=[0xee5]
    =================================
    0x508: v508(0x293d) = CONST 
    0x50b: v50b(0xee5) = CONST 
    0x50e: JUMP v50b(0xee5)

    Begin block 0xee5
    prev=[0x507], succ=[0x293d]
    =================================
    0xee6: vee6(0x434f4e54524143545f4552433732315f4745474f) = CONST 
    0xefb: vefb(0x60) = CONST 
    0xefd: vefd(0x434f4e54524143545f4552433732315f4745474f000000000000000000000000) = SHL vefb(0x60), vee6(0x434f4e54524143545f4552433732315f4745474f)
    0xeff: JUMP v508(0x293d)

    Begin block 0x293d
    prev=[0xee5], succ=[]
    =================================
    0x293e: v293e(0x40) = CONST 
    0x2941: v2941 = MLOAD v293e(0x40)
    0x2944: MSTORE v2941, vefd(0x434f4e54524143545f4552433732315f4745474f000000000000000000000000)
    0x2945: v2945 = MLOAD v293e(0x40)
    0x2949: v2949(0x0) = SUB v2941, v2945
    0x294a: v294a(0x20) = CONST 
    0x294c: v294c(0x20) = ADD v294a(0x20), v2949(0x0)
    0x294e: RETURN v2945, v294c(0x20)

}

function DRILL_OBJECT_CLASS()() public {
    Begin block 0x50f
    prev=[], succ=[0x29a3]
    =================================
    0x510: v510(0x296e) = CONST 
    0x513: v513(0x29a3) = CONST 
    0x516: JUMP v513(0x29a3)

    Begin block 0x29a3
    prev=[0x50f], succ=[0x296e]
    =================================
    0x29a4: v29a4(0x4) = CONST 
    0x29a7: JUMP v510(0x296e)

    Begin block 0x296e
    prev=[0x29a3], succ=[]
    =================================
    0x296f: v296f(0x40) = CONST 
    0x2972: v2972 = MLOAD v296f(0x40)
    0x2973: v2973(0xff) = CONST 
    0x2977: v2977(0x4) = AND v29a4(0x4), v2973(0xff)
    0x2979: MSTORE v2972, v2977(0x4)
    0x297a: v297a = MLOAD v296f(0x40)
    0x297e: v297e(0x0) = SUB v2972, v297a
    0x297f: v297f(0x20) = CONST 
    0x2981: v2981(0x20) = ADD v297f(0x20), v297e(0x0)
    0x2983: RETURN v297a, v2981(0x20)

}

function CONTRACT_KTON_ERC20_TOKEN()() public {
    Begin block 0x52d
    prev=[], succ=[0xf05]
    =================================
    0x52e: v52e(0x29c7) = CONST 
    0x531: v531(0xf05) = CONST 
    0x534: JUMP v531(0xf05)

    Begin block 0xf05
    prev=[0x52d], succ=[0x29c7]
    =================================
    0xf06: vf06(0x434f4e54524143545f4b544f4e5f45524332305f544f4b454e00000000000000) = CONST 
    0xf28: JUMP v52e(0x29c7)

    Begin block 0x29c7
    prev=[0xf05], succ=[]
    =================================
    0x29c8: v29c8(0x40) = CONST 
    0x29cb: v29cb = MLOAD v29c8(0x40)
    0x29ce: MSTORE v29cb, vf06(0x434f4e54524143545f4b544f4e5f45524332305f544f4b454e00000000000000)
    0x29cf: v29cf = MLOAD v29c8(0x40)
    0x29d3: v29d3(0x0) = SUB v29cb, v29cf
    0x29d4: v29d4(0x20) = CONST 
    0x29d6: v29d6(0x20) = ADD v29d4(0x20), v29d3(0x0)
    0x29d8: RETURN v29cf, v29d6(0x20)

}

function FURNACE_APP()() public {
    Begin block 0x535
    prev=[], succ=[0xf29]
    =================================
    0x536: v536(0x29f8) = CONST 
    0x539: v539(0xf29) = CONST 
    0x53c: JUMP v539(0xf29)

    Begin block 0xf29
    prev=[0x535], succ=[0x29f8]
    =================================
    0xf2a: vf2a(0x4655524e4143455f41505) = CONST 
    0xf36: vf36(0xac) = CONST 
    0xf38: vf38(0x4655524e4143455f415050000000000000000000000000000000000000000000) = SHL vf36(0xac), vf2a(0x4655524e4143455f41505)
    0xf3a: JUMP v536(0x29f8)

    Begin block 0x29f8
    prev=[0xf29], succ=[]
    =================================
    0x29f9: v29f9(0x40) = CONST 
    0x29fc: v29fc = MLOAD v29f9(0x40)
    0x29ff: MSTORE v29fc, vf38(0x4655524e4143455f415050000000000000000000000000000000000000000000)
    0x2a00: v2a00 = MLOAD v29f9(0x40)
    0x2a04: v2a04(0x0) = SUB v29fc, v2a00
    0x2a05: v2a05(0x20) = CONST 
    0x2a07: v2a07(0x20) = ADD v2a05(0x20), v2a04(0x0)
    0x2a09: RETURN v2a00, v2a07(0x20)

}

function CONTRACT_WOOD_ERC20_TOKEN()() public {
    Begin block 0x53d
    prev=[], succ=[0xf3b]
    =================================
    0x53e: v53e(0x2a29) = CONST 
    0x541: v541(0xf3b) = CONST 
    0x544: JUMP v541(0xf3b)

    Begin block 0xf3b
    prev=[0x53d], succ=[0x2a29]
    =================================
    0xf3c: vf3c(0x434f4e54524143545f574f4f445f45524332305f544f4b454e00000000000000) = CONST 
    0xf5e: JUMP v53e(0x2a29)

    Begin block 0x2a29
    prev=[0xf3b], succ=[]
    =================================
    0x2a2a: v2a2a(0x40) = CONST 
    0x2a2d: v2a2d = MLOAD v2a2a(0x40)
    0x2a30: MSTORE v2a2d, vf3c(0x434f4e54524143545f574f4f445f45524332305f544f4b454e00000000000000)
    0x2a31: v2a31 = MLOAD v2a2a(0x40)
    0x2a35: v2a35(0x0) = SUB v2a2d, v2a31
    0x2a36: v2a36(0x20) = CONST 
    0x2a38: v2a38(0x20) = ADD v2a36(0x20), v2a35(0x0)
    0x2a3a: RETURN v2a31, v2a38(0x20)

}

function CONTRACT_FIRE_ERC20_TOKEN()() public {
    Begin block 0x545
    prev=[], succ=[0xf5f]
    =================================
    0x546: v546(0x2a5a) = CONST 
    0x549: v549(0xf5f) = CONST 
    0x54c: JUMP v549(0xf5f)

    Begin block 0xf5f
    prev=[0x545], succ=[0x2a5a]
    =================================
    0xf60: vf60(0x434f4e54524143545f464952455f45524332305f544f4b454e00000000000000) = CONST 
    0xf82: JUMP v546(0x2a5a)

    Begin block 0x2a5a
    prev=[0xf5f], succ=[]
    =================================
    0x2a5b: v2a5b(0x40) = CONST 
    0x2a5e: v2a5e = MLOAD v2a5b(0x40)
    0x2a61: MSTORE v2a5e, vf60(0x434f4e54524143545f464952455f45524332305f544f4b454e00000000000000)
    0x2a62: v2a62 = MLOAD v2a5b(0x40)
    0x2a66: v2a66(0x0) = SUB v2a5e, v2a62
    0x2a67: v2a67(0x20) = CONST 
    0x2a69: v2a69(0x20) = ADD v2a67(0x20), v2a66(0x0)
    0x2a6b: RETURN v2a62, v2a69(0x20)

}

function CONTRACT_ITEM_BASE()() public {
    Begin block 0x54d
    prev=[], succ=[0xf83]
    =================================
    0x54e: v54e(0x2a8b) = CONST 
    0x551: v551(0xf83) = CONST 
    0x554: JUMP v551(0xf83)

    Begin block 0xf83
    prev=[0x54d], succ=[0x2a8b]
    =================================
    0xf84: vf84(0x434f4e54524143545f4954454d5f42415345) = CONST 
    0xf97: vf97(0x70) = CONST 
    0xf99: vf99(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000) = SHL vf97(0x70), vf84(0x434f4e54524143545f4954454d5f42415345)
    0xf9b: JUMP v54e(0x2a8b)

    Begin block 0x2a8b
    prev=[0xf83], succ=[]
    =================================
    0x2a8c: v2a8c(0x40) = CONST 
    0x2a8f: v2a8f = MLOAD v2a8c(0x40)
    0x2a92: MSTORE v2a8f, vf99(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000)
    0x2a93: v2a93 = MLOAD v2a8c(0x40)
    0x2a97: v2a97(0x0) = SUB v2a8f, v2a93
    0x2a98: v2a98(0x20) = CONST 
    0x2a9a: v2a9a(0x20) = ADD v2a98(0x20), v2a97(0x0)
    0x2a9c: RETURN v2a93, v2a9a(0x20)

}

function CONTRACT_LP_GOLD_ERC20_TOKEN()() public {
    Begin block 0x555
    prev=[], succ=[0xf9c]
    =================================
    0x556: v556(0x2abc) = CONST 
    0x559: v559(0xf9c) = CONST 
    0x55c: JUMP v559(0xf9c)

    Begin block 0xf9c
    prev=[0x555], succ=[0x2abc]
    =================================
    0xf9d: vf9d(0x434f4e54524143545f4c505f474f4c445f45524332305f544f4b454e00000000) = CONST 
    0xfbf: JUMP v556(0x2abc)

    Begin block 0x2abc
    prev=[0xf9c], succ=[]
    =================================
    0x2abd: v2abd(0x40) = CONST 
    0x2ac0: v2ac0 = MLOAD v2abd(0x40)
    0x2ac3: MSTORE v2ac0, vf9d(0x434f4e54524143545f4c505f474f4c445f45524332305f544f4b454e00000000)
    0x2ac4: v2ac4 = MLOAD v2abd(0x40)
    0x2ac8: v2ac8(0x0) = SUB v2ac0, v2ac4
    0x2ac9: v2ac9(0x20) = CONST 
    0x2acb: v2acb(0x20) = ADD v2ac9(0x20), v2ac8(0x0)
    0x2acd: RETURN v2ac4, v2acb(0x20)

}

function internalToken2Meta(bytes32,uint16)() public {
    Begin block 0x55d
    prev=[], succ=[0x56f, 0x573]
    =================================
    0x55e: v55e(0x2aed) = CONST 
    0x561: v561(0x4) = CONST 
    0x564: v564 = CALLDATASIZE 
    0x565: v565 = SUB v564, v561(0x4)
    0x566: v566(0x40) = CONST 
    0x569: v569 = LT v565, v566(0x40)
    0x56a: v56a = ISZERO v569
    0x56b: v56b(0x573) = CONST 
    0x56e: JUMPI v56b(0x573), v56a

    Begin block 0x56f
    prev=[0x55d], succ=[]
    =================================
    0x56f: v56f(0x0) = CONST 
    0x572: REVERT v56f(0x0), v56f(0x0)

    Begin block 0x573
    prev=[0x55d], succ=[0xfc0]
    =================================
    0x576: v576 = CALLDATALOAD v561(0x4)
    0x578: v578(0x20) = CONST 
    0x57a: v57a(0x24) = ADD v578(0x20), v561(0x4)
    0x57b: v57b = CALLDATALOAD v57a(0x24)
    0x57c: v57c(0xffff) = CONST 
    0x57f: v57f = AND v57c(0xffff), v57b
    0x580: v580(0xfc0) = CONST 
    0x583: JUMP v580(0xfc0)

    Begin block 0xfc0
    prev=[0x573], succ=[0x2aed]
    =================================
    0xfc1: vfc1(0x5) = CONST 
    0xfc3: vfc3(0x20) = CONST 
    0xfc7: MSTORE vfc3(0x20), vfc1(0x5)
    0xfc8: vfc8(0x0) = CONST 
    0xfcc: MSTORE vfc8(0x0), v576
    0xfcd: vfcd(0x40) = CONST 
    0xfd1: vfd1 = SHA3 vfc8(0x0), vfcd(0x40)
    0xfd4: MSTORE vfc3(0x20), vfd1
    0xfd7: MSTORE vfc8(0x0), v57f
    0xfd9: vfd9 = SHA3 vfc8(0x0), vfcd(0x40)
    0xfda: vfda = SLOAD vfd9
    0xfdc: JUMP v55e(0x2aed)

    Begin block 0x2aed
    prev=[0xfc0], succ=[]
    =================================
    0x2aee: v2aee(0x40) = CONST 
    0x2af1: v2af1 = MLOAD v2aee(0x40)
    0x2af4: MSTORE v2af1, vfda
    0x2af5: v2af5 = MLOAD v2aee(0x40)
    0x2af9: v2af9(0x0) = SUB v2af1, v2af5
    0x2afa: v2afa(0x20) = CONST 
    0x2afc: v2afc(0x20) = ADD v2afa(0x20), v2af9(0x0)
    0x2afe: RETURN v2af5, v2afc(0x20)

}

function CONTRACT_LAND_BASE()() public {
    Begin block 0x584
    prev=[], succ=[0xfdd]
    =================================
    0x585: v585(0x2b1e) = CONST 
    0x588: v588(0xfdd) = CONST 
    0x58b: JUMP v588(0xfdd)

    Begin block 0xfdd
    prev=[0x584], succ=[0x2b1e]
    =================================
    0xfde: vfde(0x434f4e54524143545f4c414e445f42415345) = CONST 
    0xff1: vff1(0x70) = CONST 
    0xff3: vff3(0x434f4e54524143545f4c414e445f424153450000000000000000000000000000) = SHL vff1(0x70), vfde(0x434f4e54524143545f4c414e445f42415345)
    0xff5: JUMP v585(0x2b1e)

    Begin block 0x2b1e
    prev=[0xfdd], succ=[]
    =================================
    0x2b1f: v2b1f(0x40) = CONST 
    0x2b22: v2b22 = MLOAD v2b1f(0x40)
    0x2b25: MSTORE v2b22, vff3(0x434f4e54524143545f4c414e445f424153450000000000000000000000000000)
    0x2b26: v2b26 = MLOAD v2b1f(0x40)
    0x2b2a: v2b2a(0x0) = SUB v2b22, v2b26
    0x2b2b: v2b2b(0x20) = CONST 
    0x2b2d: v2b2d(0x20) = ADD v2b2b(0x20), v2b2a(0x0)
    0x2b2f: RETURN v2b26, v2b2d(0x20)

}

function getPrefer(bytes32,address)() public {
    Begin block 0x58c
    prev=[], succ=[0x59e, 0x5a2]
    =================================
    0x58d: v58d(0x2b4f) = CONST 
    0x590: v590(0x4) = CONST 
    0x593: v593 = CALLDATASIZE 
    0x594: v594 = SUB v593, v590(0x4)
    0x595: v595(0x40) = CONST 
    0x598: v598 = LT v594, v595(0x40)
    0x599: v599 = ISZERO v598
    0x59a: v59a(0x5a2) = CONST 
    0x59d: JUMPI v59a(0x5a2), v599

    Begin block 0x59e
    prev=[0x58c], succ=[]
    =================================
    0x59e: v59e(0x0) = CONST 
    0x5a1: REVERT v59e(0x0), v59e(0x0)

    Begin block 0x5a2
    prev=[0x58c], succ=[0xff6]
    =================================
    0x5a5: v5a5 = CALLDATALOAD v590(0x4)
    0x5a7: v5a7(0x20) = CONST 
    0x5a9: v5a9(0x24) = ADD v5a7(0x20), v590(0x4)
    0x5aa: v5aa = CALLDATALOAD v5a9(0x24)
    0x5ab: v5ab(0x1) = CONST 
    0x5ad: v5ad(0x1) = CONST 
    0x5af: v5af(0xa0) = CONST 
    0x5b1: v5b1(0x10000000000000000000000000000000000000000) = SHL v5af(0xa0), v5ad(0x1)
    0x5b2: v5b2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5b1(0x10000000000000000000000000000000000000000), v5ab(0x1)
    0x5b3: v5b3 = AND v5b2(0xffffffffffffffffffffffffffffffffffffffff), v5aa
    0x5b4: v5b4(0xff6) = CONST 
    0x5b7: JUMP v5b4(0xff6)

    Begin block 0xff6
    prev=[0x5a2], succ=[0x101a, 0x1122]
    =================================
    0xff7: vff7(0x0) = CONST 
    0xff9: vff9(0x21a7a72a2920a1aa2fa2a622a6a2a72a2faa27a5a2a7) = CONST 
    0x1010: v1010(0x51) = CONST 
    0x1012: v1012(0x434f4e54524143545f454c454d454e545f544f4b454e00000000000000000000) = SHL v1010(0x51), vff9(0x21a7a72a2920a1aa2fa2a622a6a2a72a2faa27a5a2a7)
    0x1014: v1014 = EQ v5a5, v1012(0x434f4e54524143545f454c454d454e545f544f4b454e00000000000000000000)
    0x1015: v1015 = ISZERO v1014
    0x1016: v1016(0x1122) = CONST 
    0x1019: JUMPI v1016(0x1122), v1015

    Begin block 0x101a
    prev=[0xff6], succ=[0x1075, 0x1079]
    =================================
    0x101a: v101a(0x2) = CONST 
    0x101c: v101c = SLOAD v101a(0x2)
    0x101d: v101d(0x40) = CONST 
    0x1020: v1020 = MLOAD v101d(0x40)
    0x1021: v1021(0x2ecd14d3) = CONST 
    0x1026: v1026(0xe2) = CONST 
    0x1028: v1028(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1026(0xe2), v1021(0x2ecd14d3)
    0x102a: MSTORE v1020, v1028(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x102b: v102b(0x434f4e54524143545f4c414e445f42415345) = CONST 
    0x103e: v103e(0x70) = CONST 
    0x1040: v1040(0x434f4e54524143545f4c414e445f424153450000000000000000000000000000) = SHL v103e(0x70), v102b(0x434f4e54524143545f4c414e445f42415345)
    0x1041: v1041(0x4) = CONST 
    0x1044: v1044 = ADD v1020, v1041(0x4)
    0x1045: MSTORE v1044, v1040(0x434f4e54524143545f4c414e445f424153450000000000000000000000000000)
    0x1047: v1047 = MLOAD v101d(0x40)
    0x1048: v1048(0x1) = CONST 
    0x104a: v104a(0x1) = CONST 
    0x104c: v104c(0xa0) = CONST 
    0x104e: v104e(0x10000000000000000000000000000000000000000) = SHL v104c(0xa0), v104a(0x1)
    0x104f: v104f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v104e(0x10000000000000000000000000000000000000000), v1048(0x1)
    0x1052: v1052 = AND v101c, v104f(0xffffffffffffffffffffffffffffffffffffffff)
    0x1054: v1054(0xbb34534c) = CONST 
    0x105a: v105a(0x24) = CONST 
    0x105e: v105e = ADD v1020, v105a(0x24)
    0x1060: v1060(0x20) = CONST 
    0x1068: v1068(0x0) = SUB v1020, v1047
    0x1069: v1069(0x24) = ADD v1068(0x0), v105a(0x24)
    0x106d: v106d = EXTCODESIZE v1052
    0x106e: v106e = ISZERO v106d
    0x1070: v1070 = ISZERO v106e
    0x1071: v1071(0x1079) = CONST 
    0x1074: JUMPI v1071(0x1079), v1070

    Begin block 0x1075
    prev=[0x101a], succ=[]
    =================================
    0x1075: v1075(0x0) = CONST 
    0x1078: REVERT v1075(0x0), v1075(0x0)

    Begin block 0x1079
    prev=[0x101a], succ=[0x1084, 0x108d]
    =================================
    0x107b: v107b = GAS 
    0x107c: v107c = STATICCALL v107b, v1052, v1047, v1069(0x24), v1047, v1060(0x20)
    0x107d: v107d = ISZERO v107c
    0x107f: v107f = ISZERO v107d
    0x1080: v1080(0x108d) = CONST 
    0x1083: JUMPI v1080(0x108d), v107f

    Begin block 0x1084
    prev=[0x1079], succ=[]
    =================================
    0x1084: v1084 = RETURNDATASIZE 
    0x1085: v1085(0x0) = CONST 
    0x1088: RETURNDATACOPY v1085(0x0), v1085(0x0), v1084
    0x1089: v1089 = RETURNDATASIZE 
    0x108a: v108a(0x0) = CONST 
    0x108c: REVERT v108a(0x0), v1089

    Begin block 0x108d
    prev=[0x1079], succ=[0x109f, 0x10a3]
    =================================
    0x1092: v1092(0x40) = CONST 
    0x1094: v1094 = MLOAD v1092(0x40)
    0x1095: v1095 = RETURNDATASIZE 
    0x1096: v1096(0x20) = CONST 
    0x1099: v1099 = LT v1095, v1096(0x20)
    0x109a: v109a = ISZERO v1099
    0x109b: v109b(0x10a3) = CONST 
    0x109e: JUMPI v109b(0x10a3), v109a

    Begin block 0x109f
    prev=[0x108d], succ=[]
    =================================
    0x109f: v109f(0x0) = CONST 
    0x10a2: REVERT v109f(0x0), v109f(0x0)

    Begin block 0x10a3
    prev=[0x108d], succ=[0x10eb, 0x10ef0x58c]
    =================================
    0x10a5: v10a5 = MLOAD v1094
    0x10a6: v10a6(0x40) = CONST 
    0x10a9: v10a9 = MLOAD v10a6(0x40)
    0x10aa: v10aa(0xa2de1409) = CONST 
    0x10af: v10af(0xe0) = CONST 
    0x10b1: v10b1(0xa2de140900000000000000000000000000000000000000000000000000000000) = SHL v10af(0xe0), v10aa(0xa2de1409)
    0x10b3: MSTORE v10a9, v10b1(0xa2de140900000000000000000000000000000000000000000000000000000000)
    0x10b4: v10b4(0x1) = CONST 
    0x10b6: v10b6(0x1) = CONST 
    0x10b8: v10b8(0xa0) = CONST 
    0x10ba: v10ba(0x10000000000000000000000000000000000000000) = SHL v10b8(0xa0), v10b6(0x1)
    0x10bb: v10bb(0xffffffffffffffffffffffffffffffffffffffff) = SUB v10ba(0x10000000000000000000000000000000000000000), v10b4(0x1)
    0x10be: v10be = AND v10bb(0xffffffffffffffffffffffffffffffffffffffff), v5b3
    0x10bf: v10bf(0x4) = CONST 
    0x10c2: v10c2 = ADD v10a9, v10bf(0x4)
    0x10c3: MSTORE v10c2, v10be
    0x10c5: v10c5 = MLOAD v10a6(0x40)
    0x10c9: v10c9 = AND v10a5, v10bb(0xffffffffffffffffffffffffffffffffffffffff)
    0x10cb: v10cb(0xa2de1409) = CONST 
    0x10d1: v10d1(0x24) = CONST 
    0x10d5: v10d5 = ADD v10a9, v10d1(0x24)
    0x10d7: v10d7(0x20) = CONST 
    0x10de: v10de(0x0) = SUB v10a9, v10c5
    0x10df: v10df(0x24) = ADD v10de(0x0), v10d1(0x24)
    0x10e3: v10e3 = EXTCODESIZE v10c9
    0x10e4: v10e4 = ISZERO v10e3
    0x10e6: v10e6 = ISZERO v10e4
    0x10e7: v10e7(0x10ef) = CONST 
    0x10ea: JUMPI v10e7(0x10ef), v10e6

    Begin block 0x10eb
    prev=[0x10a3], succ=[]
    =================================
    0x10eb: v10eb(0x0) = CONST 
    0x10ee: REVERT v10eb(0x0), v10eb(0x0)

    Begin block 0x10ef0x58c
    prev=[0x10a3], succ=[0x10fa0x58c, 0x11030x58c]
    =================================
    0x10f10x58c: v58c10f1 = GAS 
    0x10f20x58c: v58c10f2 = STATICCALL v58c10f1, v10c9, v10c5, v10df(0x24), v10c5, v10d7(0x20)
    0x10f30x58c: v58c10f3 = ISZERO v58c10f2
    0x10f50x58c: v58c10f5 = ISZERO v58c10f3
    0x10f60x58c: v58c10f6(0x1103) = CONST 
    0x10f90x58c: JUMPI v58c10f6(0x1103), v58c10f5

    Begin block 0x10fa0x58c
    prev=[0x10ef0x58c], succ=[]
    =================================
    0x10fa0x58c: v58c10fa = RETURNDATASIZE 
    0x10fb0x58c: v58c10fb(0x0) = CONST 
    0x10fe0x58c: RETURNDATACOPY v58c10fb(0x0), v58c10fb(0x0), v58c10fa
    0x10ff0x58c: v58c10ff = RETURNDATASIZE 
    0x11000x58c: v58c1100(0x0) = CONST 
    0x11020x58c: REVERT v58c1100(0x0), v58c10ff

    Begin block 0x11030x58c
    prev=[0x10ef0x58c], succ=[0x11150x58c, 0x11190x58c]
    =================================
    0x11080x58c: v58c1108(0x40) = CONST 
    0x110a0x58c: v58c110a = MLOAD v58c1108(0x40)
    0x110b0x58c: v58c110b = RETURNDATASIZE 
    0x110c0x58c: v58c110c(0x20) = CONST 
    0x110f0x58c: v58c110f = LT v58c110b, v58c110c(0x20)
    0x11100x58c: v58c1110 = ISZERO v58c110f
    0x11110x58c: v58c1111(0x1119) = CONST 
    0x11140x58c: JUMPI v58c1111(0x1119), v58c1110

    Begin block 0x11150x58c
    prev=[0x11030x58c], succ=[]
    =================================
    0x11150x58c: v58c1115(0x0) = CONST 
    0x11180x58c: REVERT v58c1115(0x0), v58c1115(0x0)

    Begin block 0x11190x58c
    prev=[0x11030x58c], succ=[0x31c90x58c]
    =================================
    0x111b0x58c: v58c111b = MLOAD v58c110a
    0x111e0x58c: v58c111e(0x31c9) = CONST 
    0x11210x58c: JUMP v58c111e(0x31c9)

    Begin block 0x31c90x58c
    prev=[0x11190x58c], succ=[0x2b4f]
    =================================
    0x31ce0x58c: JUMP v58d(0x2b4f)

    Begin block 0x2b4f
    prev=[0x31ee, 0x31c90x58c], succ=[]
    =================================
    0x2b4f_0x0: v2b4f_0 = PHI v1149, v58c111b
    0x2b50: v2b50(0x40) = CONST 
    0x2b53: v2b53 = MLOAD v2b50(0x40)
    0x2b56: MSTORE v2b53, v2b4f_0
    0x2b57: v2b57 = MLOAD v2b50(0x40)
    0x2b5b: v2b5b(0x0) = SUB v2b53, v2b57
    0x2b5c: v2b5c(0x20) = CONST 
    0x2b5e: v2b5e(0x20) = ADD v2b5c(0x20), v2b5b(0x0)
    0x2b60: RETURN v2b57, v2b5e(0x20)

    Begin block 0x1122
    prev=[0xff6], succ=[0x31ee]
    =================================
    0x1124: v1124(0x0) = CONST 
    0x1128: MSTORE v1124(0x0), v5a5
    0x1129: v1129(0x3) = CONST 
    0x112b: v112b(0x20) = CONST 
    0x112f: MSTORE v112b(0x20), v1129(0x3)
    0x1130: v1130(0x40) = CONST 
    0x1134: v1134 = SHA3 v1124(0x0), v1130(0x40)
    0x1135: v1135(0x1) = CONST 
    0x1137: v1137(0x1) = CONST 
    0x1139: v1139(0xa0) = CONST 
    0x113b: v113b(0x10000000000000000000000000000000000000000) = SHL v1139(0xa0), v1137(0x1)
    0x113c: v113c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v113b(0x10000000000000000000000000000000000000000), v1135(0x1)
    0x113e: v113e = AND v5b3, v113c(0xffffffffffffffffffffffffffffffffffffffff)
    0x1140: MSTORE v1124(0x0), v113e
    0x1143: MSTORE v112b(0x20), v1134
    0x1145: v1145 = SHA3 v1124(0x0), v1130(0x40)
    0x1146: v1146 = SLOAD v1145
    0x1147: v1147(0xff) = CONST 
    0x1149: v1149 = AND v1147(0xff), v1146
    0x114a: v114a(0x31ee) = CONST 
    0x114d: JUMP v114a(0x31ee)

    Begin block 0x31ee
    prev=[0x1122], succ=[0x2b4f]
    =================================
    0x31f3: JUMP v58d(0x2b4f)

}

function PREFER_SOIL()() public {
    Begin block 0x5b8
    prev=[], succ=[0x114e]
    =================================
    0x5b9: v5b9(0x2b80) = CONST 
    0x5bc: v5bc(0x114e) = CONST 
    0x5bf: JUMP v5bc(0x114e)

    Begin block 0x114e
    prev=[0x5b8], succ=[0x2b80]
    =================================
    0x114f: v114f(0x20) = CONST 
    0x1152: JUMP v5b9(0x2b80)

    Begin block 0x2b80
    prev=[0x114e], succ=[]
    =================================
    0x2b81: v2b81(0x40) = CONST 
    0x2b84: v2b84 = MLOAD v2b81(0x40)
    0x2b87: MSTORE v2b84, v114f(0x20)
    0x2b88: v2b88 = MLOAD v2b81(0x40)
    0x2b8c: v2b8c(0x0) = SUB v2b84, v2b88
    0x2b8d: v2b8d(0x20) = CONST 
    0x2b8f: v2b8f(0x20) = ADD v2b8d(0x20), v2b8c(0x0)
    0x2b91: RETURN v2b88, v2b8f(0x20)

}

function setAuthority(address)() public {
    Begin block 0x5c0
    prev=[], succ=[0x5d2, 0x5d6]
    =================================
    0x5c1: v5c1(0x2bb1) = CONST 
    0x5c4: v5c4(0x4) = CONST 
    0x5c7: v5c7 = CALLDATASIZE 
    0x5c8: v5c8 = SUB v5c7, v5c4(0x4)
    0x5c9: v5c9(0x20) = CONST 
    0x5cc: v5cc = LT v5c8, v5c9(0x20)
    0x5cd: v5cd = ISZERO v5cc
    0x5ce: v5ce(0x5d6) = CONST 
    0x5d1: JUMPI v5ce(0x5d6), v5cd

    Begin block 0x5d2
    prev=[0x5c0], succ=[]
    =================================
    0x5d2: v5d2(0x0) = CONST 
    0x5d5: REVERT v5d2(0x0), v5d2(0x0)

    Begin block 0x5d6
    prev=[0x5c0], succ=[0x1153]
    =================================
    0x5d8: v5d8 = CALLDATALOAD v5c4(0x4)
    0x5d9: v5d9(0x1) = CONST 
    0x5db: v5db(0x1) = CONST 
    0x5dd: v5dd(0xa0) = CONST 
    0x5df: v5df(0x10000000000000000000000000000000000000000) = SHL v5dd(0xa0), v5db(0x1)
    0x5e0: v5e0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5df(0x10000000000000000000000000000000000000000), v5d9(0x1)
    0x5e1: v5e1 = AND v5e0(0xffffffffffffffffffffffffffffffffffffffff), v5d8
    0x5e2: v5e2(0x1153) = CONST 
    0x5e5: JUMP v5e2(0x1153)

    Begin block 0x1153
    prev=[0x5d6], succ=[0x1169]
    =================================
    0x1154: v1154(0x1169) = CONST 
    0x1157: v1157 = CALLER 
    0x1158: v1158(0x0) = CONST 
    0x115a: v115a = CALLDATALOAD v1158(0x0)
    0x115b: v115b(0x1) = CONST 
    0x115d: v115d(0x1) = CONST 
    0x115f: v115f(0xe0) = CONST 
    0x1161: v1161(0x100000000000000000000000000000000000000000000000000000000) = SHL v115f(0xe0), v115d(0x1)
    0x1162: v1162(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1161(0x100000000000000000000000000000000000000000000000000000000), v115b(0x1)
    0x1163: v1163(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1162(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1164: v1164 = AND v1163(0xffffffff00000000000000000000000000000000000000000000000000000000), v115a
    0x1165: v1165(0x22d3) = CONST 
    0x1168: v1168_0 = CALLPRIVATE v1165(0x22d3), v1164, v1157, v1154(0x1169)

    Begin block 0x1169
    prev=[0x1153], succ=[0x116e, 0x11a8]
    =================================
    0x116a: v116a(0x11a8) = CONST 
    0x116d: JUMPI v116a(0x11a8), v1168_0

    Begin block 0x116e
    prev=[0x1169], succ=[]
    =================================
    0x116e: v116e(0x40) = CONST 
    0x1171: v1171 = MLOAD v116e(0x40)
    0x1172: v1172(0x461bcd) = CONST 
    0x1176: v1176(0xe5) = CONST 
    0x1178: v1178(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1176(0xe5), v1172(0x461bcd)
    0x117a: MSTORE v1171, v1178(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x117b: v117b(0x20) = CONST 
    0x117d: v117d(0x4) = CONST 
    0x1180: v1180 = ADD v1171, v117d(0x4)
    0x1181: MSTORE v1180, v117b(0x20)
    0x1182: v1182(0x14) = CONST 
    0x1184: v1184(0x24) = CONST 
    0x1187: v1187 = ADD v1171, v1184(0x24)
    0x1188: MSTORE v1187, v1182(0x14)
    0x1189: v1189(0x0) = CONST 
    0x118c: v118c = MLOAD v1189(0x0)
    0x118d: v118d(0x20) = CONST 
    0x118f: v118f(0x2409) = CONST 
    0x1197: MSTORE v1189(0x0), v118c
    0x1198: v1198(0x44) = CONST 
    0x119b: v119b = ADD v1171, v1198(0x44)
    0x119c: MSTORE v119b, v33e6(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x119e: v119e = MLOAD v116e(0x40)
    0x11a2: v11a2(0x0) = SUB v1171, v119e
    0x11a3: v11a3(0x64) = CONST 
    0x11a5: v11a5(0x64) = ADD v11a3(0x64), v11a2(0x0)
    0x11a7: REVERT v119e, v11a5(0x64)
    0x33e6: v33e6(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x11a8
    prev=[0x1169], succ=[0x2bb1]
    =================================
    0x11a9: v11a9(0x0) = CONST 
    0x11ac: v11ac = SLOAD v11a9(0x0)
    0x11ad: v11ad(0x10000) = CONST 
    0x11b1: v11b1(0x1) = CONST 
    0x11b3: v11b3(0xb0) = CONST 
    0x11b5: v11b5(0x100000000000000000000000000000000000000000000) = SHL v11b3(0xb0), v11b1(0x1)
    0x11b6: v11b6(0xffffffffffffffffffffffffffffffffffffffff0000) = SUB v11b5(0x100000000000000000000000000000000000000000000), v11ad(0x10000)
    0x11b7: v11b7(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff) = NOT v11b6(0xffffffffffffffffffffffffffffffffffffffff0000)
    0x11b8: v11b8 = AND v11b7(0xffffffffffffffffffff0000000000000000000000000000000000000000ffff), v11ac
    0x11b9: v11b9(0x10000) = CONST 
    0x11bd: v11bd(0x1) = CONST 
    0x11bf: v11bf(0x1) = CONST 
    0x11c1: v11c1(0xa0) = CONST 
    0x11c3: v11c3(0x10000000000000000000000000000000000000000) = SHL v11c1(0xa0), v11bf(0x1)
    0x11c4: v11c4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v11c3(0x10000000000000000000000000000000000000000), v11bd(0x1)
    0x11c7: v11c7 = AND v11c4(0xffffffffffffffffffffffffffffffffffffffff), v5e1
    0x11c9: v11c9 = MUL v11b9(0x10000), v11c7
    0x11cd: v11cd = OR v11c9, v11b8
    0x11d0: SSTORE v11a9(0x0), v11cd
    0x11d1: v11d1(0x40) = CONST 
    0x11d3: v11d3 = MLOAD v11d1(0x40)
    0x11d6: v11d6 = DIV v11cd, v11b9(0x10000)
    0x11d9: v11d9 = AND v11c4(0xffffffffffffffffffffffffffffffffffffffff), v11d6
    0x11db: v11db(0x1abebea81bfa2637f28358c371278fb15ede7ea8dd28d2e03b112ff6d936ada4) = CONST 
    0x11fd: LOG2 v11d3, v11a9(0x0), v11db(0x1abebea81bfa2637f28358c371278fb15ede7ea8dd28d2e03b112ff6d936ada4), v11d9
    0x11ff: JUMP v5c1(0x2bb1)

    Begin block 0x2bb1
    prev=[0x11a8], succ=[]
    =================================
    0x2bb2: STOP 

}

function registry()() public {
    Begin block 0x5e6
    prev=[], succ=[0x1200]
    =================================
    0x5e7: v5e7(0x2bd2) = CONST 
    0x5ea: v5ea(0x1200) = CONST 
    0x5ed: JUMP v5ea(0x1200)

    Begin block 0x1200
    prev=[0x5e6], succ=[0x2bd2]
    =================================
    0x1201: v1201(0x2) = CONST 
    0x1203: v1203 = SLOAD v1201(0x2)
    0x1204: v1204(0x1) = CONST 
    0x1206: v1206(0x1) = CONST 
    0x1208: v1208(0xa0) = CONST 
    0x120a: v120a(0x10000000000000000000000000000000000000000) = SHL v1208(0xa0), v1206(0x1)
    0x120b: v120b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v120a(0x10000000000000000000000000000000000000000), v1204(0x1)
    0x120c: v120c = AND v120b(0xffffffffffffffffffffffffffffffffffffffff), v1203
    0x120e: JUMP v5e7(0x2bd2)

    Begin block 0x2bd2
    prev=[0x1200], succ=[]
    =================================
    0x2bd3: v2bd3(0x40) = CONST 
    0x2bd6: v2bd6 = MLOAD v2bd3(0x40)
    0x2bd7: v2bd7(0x1) = CONST 
    0x2bd9: v2bd9(0x1) = CONST 
    0x2bdb: v2bdb(0xa0) = CONST 
    0x2bdd: v2bdd(0x10000000000000000000000000000000000000000) = SHL v2bdb(0xa0), v2bd9(0x1)
    0x2bde: v2bde(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2bdd(0x10000000000000000000000000000000000000000), v2bd7(0x1)
    0x2be1: v2be1 = AND v120c, v2bde(0xffffffffffffffffffffffffffffffffffffffff)
    0x2be3: MSTORE v2bd6, v2be1
    0x2be4: v2be4 = MLOAD v2bd3(0x40)
    0x2be8: v2be8(0x0) = SUB v2bd6, v2be4
    0x2be9: v2be9(0x20) = CONST 
    0x2beb: v2beb(0x20) = ADD v2be9(0x20), v2be8(0x0)
    0x2bed: RETURN v2be4, v2beb(0x20)

}

function FURNACE_ITEM_MINE_FEE()() public {
    Begin block 0x60a
    prev=[], succ=[0x120f]
    =================================
    0x60b: v60b(0x2c0d) = CONST 
    0x60e: v60e(0x120f) = CONST 
    0x611: JUMP v60e(0x120f)

    Begin block 0x120f
    prev=[0x60a], succ=[0x2c0d]
    =================================
    0x1210: v1210(0x4655524e4143455f4954454d5f4d494e455f464545) = CONST 
    0x1226: v1226(0x58) = CONST 
    0x1228: v1228(0x4655524e4143455f4954454d5f4d494e455f4645450000000000000000000000) = SHL v1226(0x58), v1210(0x4655524e4143455f4954454d5f4d494e455f464545)
    0x122a: JUMP v60b(0x2c0d)

    Begin block 0x2c0d
    prev=[0x120f], succ=[]
    =================================
    0x2c0e: v2c0e(0x40) = CONST 
    0x2c11: v2c11 = MLOAD v2c0e(0x40)
    0x2c14: MSTORE v2c11, v1228(0x4655524e4143455f4954454d5f4d494e455f4645450000000000000000000000)
    0x2c15: v2c15 = MLOAD v2c0e(0x40)
    0x2c19: v2c19(0x0) = SUB v2c11, v2c15
    0x2c1a: v2c1a(0x20) = CONST 
    0x2c1c: v2c1c(0x20) = ADD v2c1a(0x20), v2c19(0x0)
    0x2c1e: RETURN v2c15, v2c1c(0x20)

}

function CONTRACT_INTERSTELLAR_ENCODER()() public {
    Begin block 0x612
    prev=[], succ=[0x122b]
    =================================
    0x613: v613(0x2c3e) = CONST 
    0x616: v616(0x122b) = CONST 
    0x619: JUMP v616(0x122b)

    Begin block 0x122b
    prev=[0x612], succ=[0x2c3e]
    =================================
    0x122c: v122c(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000) = CONST 
    0x124e: JUMP v613(0x2c3e)

    Begin block 0x2c3e
    prev=[0x122b], succ=[]
    =================================
    0x2c3f: v2c3f(0x40) = CONST 
    0x2c42: v2c42 = MLOAD v2c3f(0x40)
    0x2c45: MSTORE v2c42, v122c(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000)
    0x2c46: v2c46 = MLOAD v2c3f(0x40)
    0x2c4a: v2c4a(0x0) = SUB v2c42, v2c46
    0x2c4b: v2c4b(0x20) = CONST 
    0x2c4d: v2c4d(0x20) = ADD v2c4b(0x20), v2c4a(0x0)
    0x2c4f: RETURN v2c46, v2c4d(0x20)

}

function ITEM_OBJECT_CLASS()() public {
    Begin block 0x61a
    prev=[], succ=[0x124f]
    =================================
    0x61b: v61b(0x2c6f) = CONST 
    0x61e: v61e(0x124f) = CONST 
    0x621: JUMP v61e(0x124f)

    Begin block 0x124f
    prev=[0x61a], succ=[0x2c6f]
    =================================
    0x1250: v1250(0x5) = CONST 
    0x1253: JUMP v61b(0x2c6f)

    Begin block 0x2c6f
    prev=[0x124f], succ=[]
    =================================
    0x2c70: v2c70(0x40) = CONST 
    0x2c73: v2c73 = MLOAD v2c70(0x40)
    0x2c74: v2c74(0xff) = CONST 
    0x2c78: v2c78(0x5) = AND v1250(0x5), v2c74(0xff)
    0x2c7a: MSTORE v2c73, v2c78(0x5)
    0x2c7b: v2c7b = MLOAD v2c70(0x40)
    0x2c7f: v2c7f(0x0) = SUB v2c73, v2c7b
    0x2c80: v2c80(0x20) = CONST 
    0x2c82: v2c82(0x20) = ADD v2c80(0x20), v2c7f(0x0)
    0x2c84: RETURN v2c7b, v2c82(0x20)

}

function addLPToken(bytes32,address,uint8)() public {
    Begin block 0x622
    prev=[], succ=[0x634, 0x638]
    =================================
    0x623: v623(0x2ca4) = CONST 
    0x626: v626(0x4) = CONST 
    0x629: v629 = CALLDATASIZE 
    0x62a: v62a = SUB v629, v626(0x4)
    0x62b: v62b(0x60) = CONST 
    0x62e: v62e = LT v62a, v62b(0x60)
    0x62f: v62f = ISZERO v62e
    0x630: v630(0x638) = CONST 
    0x633: JUMPI v630(0x638), v62f

    Begin block 0x634
    prev=[0x622], succ=[]
    =================================
    0x634: v634(0x0) = CONST 
    0x637: REVERT v634(0x0), v634(0x0)

    Begin block 0x638
    prev=[0x622], succ=[0x1254]
    =================================
    0x63b: v63b = CALLDATALOAD v626(0x4)
    0x63d: v63d(0x20) = CONST 
    0x640: v640(0x24) = ADD v626(0x4), v63d(0x20)
    0x641: v641 = CALLDATALOAD v640(0x24)
    0x642: v642(0x1) = CONST 
    0x644: v644(0x1) = CONST 
    0x646: v646(0xa0) = CONST 
    0x648: v648(0x10000000000000000000000000000000000000000) = SHL v646(0xa0), v644(0x1)
    0x649: v649(0xffffffffffffffffffffffffffffffffffffffff) = SUB v648(0x10000000000000000000000000000000000000000), v642(0x1)
    0x64a: v64a = AND v649(0xffffffffffffffffffffffffffffffffffffffff), v641
    0x64c: v64c(0x40) = CONST 
    0x64e: v64e(0x44) = ADD v64c(0x40), v626(0x4)
    0x64f: v64f = CALLDATALOAD v64e(0x44)
    0x650: v650(0xff) = CONST 
    0x652: v652 = AND v650(0xff), v64f
    0x653: v653(0x1254) = CONST 
    0x656: JUMP v653(0x1254)

    Begin block 0x1254
    prev=[0x638], succ=[0x126a]
    =================================
    0x1255: v1255(0x126a) = CONST 
    0x1258: v1258 = CALLER 
    0x1259: v1259(0x0) = CONST 
    0x125b: v125b = CALLDATALOAD v1259(0x0)
    0x125c: v125c(0x1) = CONST 
    0x125e: v125e(0x1) = CONST 
    0x1260: v1260(0xe0) = CONST 
    0x1262: v1262(0x100000000000000000000000000000000000000000000000000000000) = SHL v1260(0xe0), v125e(0x1)
    0x1263: v1263(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1262(0x100000000000000000000000000000000000000000000000000000000), v125c(0x1)
    0x1264: v1264(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1263(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1265: v1265 = AND v1264(0xffffffff00000000000000000000000000000000000000000000000000000000), v125b
    0x1266: v1266(0x22d3) = CONST 
    0x1269: v1269_0 = CALLPRIVATE v1266(0x22d3), v1265, v1258, v1255(0x126a)

    Begin block 0x126a
    prev=[0x1254], succ=[0x126f, 0x12a9]
    =================================
    0x126b: v126b(0x12a9) = CONST 
    0x126e: JUMPI v126b(0x12a9), v1269_0

    Begin block 0x126f
    prev=[0x126a], succ=[]
    =================================
    0x126f: v126f(0x40) = CONST 
    0x1272: v1272 = MLOAD v126f(0x40)
    0x1273: v1273(0x461bcd) = CONST 
    0x1277: v1277(0xe5) = CONST 
    0x1279: v1279(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1277(0xe5), v1273(0x461bcd)
    0x127b: MSTORE v1272, v1279(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x127c: v127c(0x20) = CONST 
    0x127e: v127e(0x4) = CONST 
    0x1281: v1281 = ADD v1272, v127e(0x4)
    0x1282: MSTORE v1281, v127c(0x20)
    0x1283: v1283(0x14) = CONST 
    0x1285: v1285(0x24) = CONST 
    0x1288: v1288 = ADD v1272, v1285(0x24)
    0x1289: MSTORE v1288, v1283(0x14)
    0x128a: v128a(0x0) = CONST 
    0x128d: v128d = MLOAD v128a(0x0)
    0x128e: v128e(0x20) = CONST 
    0x1290: v1290(0x2409) = CONST 
    0x1298: MSTORE v128a(0x0), v128d
    0x1299: v1299(0x44) = CONST 
    0x129c: v129c = ADD v1272, v1299(0x44)
    0x129d: MSTORE v129c, v33eb(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x129f: v129f = MLOAD v126f(0x40)
    0x12a3: v12a3(0x0) = SUB v1272, v129f
    0x12a4: v12a4(0x64) = CONST 
    0x12a6: v12a6(0x64) = ADD v12a4(0x64), v12a3(0x0)
    0x12a8: REVERT v129f, v12a6(0x64)
    0x33eb: v33eb(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x12a9
    prev=[0x126a], succ=[0x12bf, 0x12b7]
    =================================
    0x12aa: v12aa(0x0) = CONST 
    0x12ad: v12ad(0xff) = CONST 
    0x12af: v12af = AND v12ad(0xff), v652
    0x12b0: v12b0 = GT v12af, v12aa(0x0)
    0x12b2: v12b2 = ISZERO v12b0
    0x12b3: v12b3(0x12bf) = CONST 
    0x12b6: JUMPI v12b3(0x12bf), v12b2

    Begin block 0x12bf
    prev=[0x12a9, 0x12b7], succ=[0x12c4, 0x1310]
    =================================
    0x12bf_0x0: v12bf_0 = PHI v12b0, v12be
    0x12c0: v12c0(0x1310) = CONST 
    0x12c3: JUMPI v12c0(0x1310), v12bf_0

    Begin block 0x12c4
    prev=[0x12bf], succ=[]
    =================================
    0x12c4: v12c4(0x40) = CONST 
    0x12c7: v12c7 = MLOAD v12c4(0x40)
    0x12c8: v12c8(0x461bcd) = CONST 
    0x12cc: v12cc(0xe5) = CONST 
    0x12ce: v12ce(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v12cc(0xe5), v12c8(0x461bcd)
    0x12d0: MSTORE v12c7, v12ce(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x12d1: v12d1(0x20) = CONST 
    0x12d3: v12d3(0x4) = CONST 
    0x12d6: v12d6 = ADD v12c7, v12d3(0x4)
    0x12d7: MSTORE v12d6, v12d1(0x20)
    0x12d8: v12d8(0x1b) = CONST 
    0x12da: v12da(0x24) = CONST 
    0x12dd: v12dd = ADD v12c7, v12da(0x24)
    0x12de: MSTORE v12dd, v12d8(0x1b)
    0x12df: v12df(0x4675726e6163653a20494e56414c49445f5245534f5552434549440000000000) = CONST 
    0x1300: v1300(0x44) = CONST 
    0x1303: v1303 = ADD v12c7, v1300(0x44)
    0x1304: MSTORE v1303, v12df(0x4675726e6163653a20494e56414c49445f5245534f5552434549440000000000)
    0x1306: v1306 = MLOAD v12c4(0x40)
    0x130a: v130a(0x0) = SUB v12c7, v1306
    0x130b: v130b(0x64) = CONST 
    0x130d: v130d(0x64) = ADD v130b(0x64), v130a(0x0)
    0x130f: REVERT v1306, v130d(0x64)

    Begin block 0x1310
    prev=[0x12bf], succ=[0x2ca4]
    =================================
    0x1311: v1311(0x0) = CONST 
    0x1315: MSTORE v1311(0x0), v63b
    0x1316: v1316(0x3) = CONST 
    0x1318: v1318(0x20) = CONST 
    0x131c: MSTORE v1318(0x20), v1316(0x3)
    0x131d: v131d(0x40) = CONST 
    0x1321: v1321 = SHA3 v1311(0x0), v131d(0x40)
    0x1322: v1322(0x1) = CONST 
    0x1324: v1324(0x1) = CONST 
    0x1326: v1326(0xa0) = CONST 
    0x1328: v1328(0x10000000000000000000000000000000000000000) = SHL v1326(0xa0), v1324(0x1)
    0x1329: v1329(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1328(0x10000000000000000000000000000000000000000), v1322(0x1)
    0x132b: v132b = AND v64a, v1329(0xffffffffffffffffffffffffffffffffffffffff)
    0x132e: MSTORE v1311(0x0), v132b
    0x1331: MSTORE v1318(0x20), v1321
    0x1335: v1335 = SHA3 v1311(0x0), v131d(0x40)
    0x1337: v1337 = SLOAD v1335
    0x1338: v1338(0xff) = CONST 
    0x133b: v133b = AND v652, v1338(0xff)
    0x133c: v133c(0xff) = CONST 
    0x133e: v133e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v133c(0xff)
    0x1341: v1341 = AND v1337, v133e(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x1343: v1343 = OR v133b, v1341
    0x1346: SSTORE v1335, v1343
    0x1348: v1348 = MLOAD v131d(0x40)
    0x134b: MSTORE v1348, v63b
    0x134e: v134e = ADD v1348, v1318(0x20)
    0x1352: MSTORE v134e, v132b
    0x1355: v1355 = ADD v131d(0x40), v1348
    0x1359: MSTORE v1355, v133b
    0x135b: v135b = MLOAD v131d(0x40)
    0x135c: v135c(0x4afee0e249c1335f985452b7cb4168fd5c71db2b554fcbda0802a4293bf6f79e) = CONST 
    0x1380: v1380(0x0) = SUB v1348, v135b
    0x1381: v1381(0x60) = CONST 
    0x1383: v1383(0x60) = ADD v1381(0x60), v1380(0x0)
    0x1385: LOG1 v135b, v1383(0x60), v135c(0x4afee0e249c1335f985452b7cb4168fd5c71db2b554fcbda0802a4293bf6f79e)
    0x1389: JUMP v623(0x2ca4)

    Begin block 0x2ca4
    prev=[0x1310], succ=[]
    =================================
    0x2ca5: STOP 

    Begin block 0x12b7
    prev=[0x12a9], succ=[0x12bf]
    =================================
    0x12b8: v12b8(0x6) = CONST 
    0x12bb: v12bb(0xff) = CONST 
    0x12bd: v12bd = AND v12bb(0xff), v652
    0x12be: v12be = LT v12bd, v12b8(0x6)

}

function removeLPToken(bytes32,address)() public {
    Begin block 0x657
    prev=[], succ=[0x669, 0x66d]
    =================================
    0x658: v658(0x2cc5) = CONST 
    0x65b: v65b(0x4) = CONST 
    0x65e: v65e = CALLDATASIZE 
    0x65f: v65f = SUB v65e, v65b(0x4)
    0x660: v660(0x40) = CONST 
    0x663: v663 = LT v65f, v660(0x40)
    0x664: v664 = ISZERO v663
    0x665: v665(0x66d) = CONST 
    0x668: JUMPI v665(0x66d), v664

    Begin block 0x669
    prev=[0x657], succ=[]
    =================================
    0x669: v669(0x0) = CONST 
    0x66c: REVERT v669(0x0), v669(0x0)

    Begin block 0x66d
    prev=[0x657], succ=[0x138a]
    =================================
    0x670: v670 = CALLDATALOAD v65b(0x4)
    0x672: v672(0x20) = CONST 
    0x674: v674(0x24) = ADD v672(0x20), v65b(0x4)
    0x675: v675 = CALLDATALOAD v674(0x24)
    0x676: v676(0x1) = CONST 
    0x678: v678(0x1) = CONST 
    0x67a: v67a(0xa0) = CONST 
    0x67c: v67c(0x10000000000000000000000000000000000000000) = SHL v67a(0xa0), v678(0x1)
    0x67d: v67d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v67c(0x10000000000000000000000000000000000000000), v676(0x1)
    0x67e: v67e = AND v67d(0xffffffffffffffffffffffffffffffffffffffff), v675
    0x67f: v67f(0x138a) = CONST 
    0x682: JUMP v67f(0x138a)

    Begin block 0x138a
    prev=[0x66d], succ=[0x13a0]
    =================================
    0x138b: v138b(0x13a0) = CONST 
    0x138e: v138e = CALLER 
    0x138f: v138f(0x0) = CONST 
    0x1391: v1391 = CALLDATALOAD v138f(0x0)
    0x1392: v1392(0x1) = CONST 
    0x1394: v1394(0x1) = CONST 
    0x1396: v1396(0xe0) = CONST 
    0x1398: v1398(0x100000000000000000000000000000000000000000000000000000000) = SHL v1396(0xe0), v1394(0x1)
    0x1399: v1399(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1398(0x100000000000000000000000000000000000000000000000000000000), v1392(0x1)
    0x139a: v139a(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1399(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x139b: v139b = AND v139a(0xffffffff00000000000000000000000000000000000000000000000000000000), v1391
    0x139c: v139c(0x22d3) = CONST 
    0x139f: v139f_0 = CALLPRIVATE v139c(0x22d3), v139b, v138e, v138b(0x13a0)

    Begin block 0x13a0
    prev=[0x138a], succ=[0x13a5, 0x13df]
    =================================
    0x13a1: v13a1(0x13df) = CONST 
    0x13a4: JUMPI v13a1(0x13df), v139f_0

    Begin block 0x13a5
    prev=[0x13a0], succ=[]
    =================================
    0x13a5: v13a5(0x40) = CONST 
    0x13a8: v13a8 = MLOAD v13a5(0x40)
    0x13a9: v13a9(0x461bcd) = CONST 
    0x13ad: v13ad(0xe5) = CONST 
    0x13af: v13af(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v13ad(0xe5), v13a9(0x461bcd)
    0x13b1: MSTORE v13a8, v13af(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x13b2: v13b2(0x20) = CONST 
    0x13b4: v13b4(0x4) = CONST 
    0x13b7: v13b7 = ADD v13a8, v13b4(0x4)
    0x13b8: MSTORE v13b7, v13b2(0x20)
    0x13b9: v13b9(0x14) = CONST 
    0x13bb: v13bb(0x24) = CONST 
    0x13be: v13be = ADD v13a8, v13bb(0x24)
    0x13bf: MSTORE v13be, v13b9(0x14)
    0x13c0: v13c0(0x0) = CONST 
    0x13c3: v13c3 = MLOAD v13c0(0x0)
    0x13c4: v13c4(0x20) = CONST 
    0x13c6: v13c6(0x2409) = CONST 
    0x13ce: MSTORE v13c0(0x0), v13c3
    0x13cf: v13cf(0x44) = CONST 
    0x13d2: v13d2 = ADD v13a8, v13cf(0x44)
    0x13d3: MSTORE v13d2, v33f0(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x13d5: v13d5 = MLOAD v13a5(0x40)
    0x13d9: v13d9(0x0) = SUB v13a8, v13d5
    0x13da: v13da(0x64) = CONST 
    0x13dc: v13dc(0x64) = ADD v13da(0x64), v13d9(0x0)
    0x13de: REVERT v13d5, v13dc(0x64)
    0x33f0: v33f0(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x13df
    prev=[0x13a0], succ=[0x140a, 0x1447]
    =================================
    0x13e0: v13e0(0x0) = CONST 
    0x13e4: MSTORE v13e0(0x0), v670
    0x13e5: v13e5(0x3) = CONST 
    0x13e7: v13e7(0x20) = CONST 
    0x13eb: MSTORE v13e7(0x20), v13e5(0x3)
    0x13ec: v13ec(0x40) = CONST 
    0x13f0: v13f0 = SHA3 v13e0(0x0), v13ec(0x40)
    0x13f1: v13f1(0x1) = CONST 
    0x13f3: v13f3(0x1) = CONST 
    0x13f5: v13f5(0xa0) = CONST 
    0x13f7: v13f7(0x10000000000000000000000000000000000000000) = SHL v13f5(0xa0), v13f3(0x1)
    0x13f8: v13f8(0xffffffffffffffffffffffffffffffffffffffff) = SUB v13f7(0x10000000000000000000000000000000000000000), v13f1(0x1)
    0x13fa: v13fa = AND v67e, v13f8(0xffffffffffffffffffffffffffffffffffffffff)
    0x13fc: MSTORE v13e0(0x0), v13fa
    0x13ff: MSTORE v13e7(0x20), v13f0
    0x1401: v1401 = SHA3 v13e0(0x0), v13ec(0x40)
    0x1402: v1402 = SLOAD v1401
    0x1403: v1403(0xff) = CONST 
    0x1405: v1405 = AND v1403(0xff), v1402
    0x1406: v1406(0x1447) = CONST 
    0x1409: JUMPI v1406(0x1447), v1405

    Begin block 0x140a
    prev=[0x13df], succ=[]
    =================================
    0x140a: v140a(0x40) = CONST 
    0x140d: v140d = MLOAD v140a(0x40)
    0x140e: v140e(0x461bcd) = CONST 
    0x1412: v1412(0xe5) = CONST 
    0x1414: v1414(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1412(0xe5), v140e(0x461bcd)
    0x1416: MSTORE v140d, v1414(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1417: v1417(0x20) = CONST 
    0x1419: v1419(0x4) = CONST 
    0x141c: v141c = ADD v140d, v1419(0x4)
    0x141d: MSTORE v141c, v1417(0x20)
    0x141e: v141e(0xe) = CONST 
    0x1420: v1420(0x24) = CONST 
    0x1423: v1423 = ADD v140d, v1420(0x24)
    0x1424: MSTORE v1423, v141e(0xe)
    0x1425: v1425(0x4675726e6163653a20454d505459) = CONST 
    0x1434: v1434(0x90) = CONST 
    0x1436: v1436(0x4675726e6163653a20454d505459000000000000000000000000000000000000) = SHL v1434(0x90), v1425(0x4675726e6163653a20454d505459)
    0x1437: v1437(0x44) = CONST 
    0x143a: v143a = ADD v140d, v1437(0x44)
    0x143b: MSTORE v143a, v1436(0x4675726e6163653a20454d505459000000000000000000000000000000000000)
    0x143d: v143d = MLOAD v140a(0x40)
    0x1441: v1441(0x0) = SUB v140d, v143d
    0x1442: v1442(0x64) = CONST 
    0x1444: v1444(0x64) = ADD v1442(0x64), v1441(0x0)
    0x1446: REVERT v143d, v1444(0x64)

    Begin block 0x1447
    prev=[0x13df], succ=[0x2cc5]
    =================================
    0x1448: v1448(0x0) = CONST 
    0x144c: MSTORE v1448(0x0), v670
    0x144d: v144d(0x3) = CONST 
    0x144f: v144f(0x20) = CONST 
    0x1453: MSTORE v144f(0x20), v144d(0x3)
    0x1454: v1454(0x40) = CONST 
    0x1458: v1458 = SHA3 v1448(0x0), v1454(0x40)
    0x1459: v1459(0x1) = CONST 
    0x145b: v145b(0x1) = CONST 
    0x145d: v145d(0xa0) = CONST 
    0x145f: v145f(0x10000000000000000000000000000000000000000) = SHL v145d(0xa0), v145b(0x1)
    0x1460: v1460(0xffffffffffffffffffffffffffffffffffffffff) = SUB v145f(0x10000000000000000000000000000000000000000), v1459(0x1)
    0x1462: v1462 = AND v67e, v1460(0xffffffffffffffffffffffffffffffffffffffff)
    0x1465: MSTORE v1448(0x0), v1462
    0x1468: MSTORE v144f(0x20), v1458
    0x146c: v146c = SHA3 v1448(0x0), v1454(0x40)
    0x146e: v146e = SLOAD v146c
    0x146f: v146f(0xff) = CONST 
    0x1471: v1471(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v146f(0xff)
    0x1472: v1472 = AND v1471(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v146e
    0x1474: SSTORE v146c, v1472
    0x1476: v1476 = MLOAD v1454(0x40)
    0x1479: MSTORE v1476, v670
    0x147c: v147c = ADD v1476, v144f(0x20)
    0x1480: MSTORE v147c, v1462
    0x1482: v1482 = MLOAD v1454(0x40)
    0x1483: v1483(0x927a120242c178e436f17248a76d573b08959e380cf6c18e79a7abcb8fa1c39d) = CONST 
    0x14a8: v14a8(0x0) = SUB v1476, v1482
    0x14ab: v14ab(0x40) = ADD v1454(0x40), v14a8(0x0)
    0x14ad: LOG1 v1482, v14ab(0x40), v1483(0x927a120242c178e436f17248a76d573b08959e380cf6c18e79a7abcb8fa1c39d)
    0x14b0: JUMP v658(0x2cc5)

    Begin block 0x2cc5
    prev=[0x1447], succ=[]
    =================================
    0x2cc6: STOP 

}

function CONTRACT_DARWINIA_ITO_BASE()() public {
    Begin block 0x683
    prev=[], succ=[0x14b1]
    =================================
    0x684: v684(0x2ce6) = CONST 
    0x687: v687(0x14b1) = CONST 
    0x68a: JUMP v687(0x14b1)

    Begin block 0x14b1
    prev=[0x683], succ=[0x2ce6]
    =================================
    0x14b2: v14b2(0x434f4e54524143545f44415257494e49415f49544f5f42415345000000000000) = CONST 
    0x14d4: JUMP v684(0x2ce6)

    Begin block 0x2ce6
    prev=[0x14b1], succ=[]
    =================================
    0x2ce7: v2ce7(0x40) = CONST 
    0x2cea: v2cea = MLOAD v2ce7(0x40)
    0x2ced: MSTORE v2cea, v14b2(0x434f4e54524143545f44415257494e49415f49544f5f42415345000000000000)
    0x2cee: v2cee = MLOAD v2ce7(0x40)
    0x2cf2: v2cf2(0x0) = SUB v2cea, v2cee
    0x2cf3: v2cf3(0x20) = CONST 
    0x2cf5: v2cf5(0x20) = ADD v2cf3(0x20), v2cf2(0x0)
    0x2cf7: RETURN v2cee, v2cf5(0x20)

}

function PREFER_WOOD()() public {
    Begin block 0x68b
    prev=[], succ=[0x2d48]
    =================================
    0x68c: v68c(0x2d17) = CONST 
    0x68f: v68f(0x2d48) = CONST 
    0x692: JUMP v68f(0x2d48)

    Begin block 0x2d48
    prev=[0x68b], succ=[0x2d17]
    =================================
    0x2d49: v2d49(0x4) = CONST 
    0x2d4c: JUMP v68c(0x2d17)

    Begin block 0x2d17
    prev=[0x2d48], succ=[]
    =================================
    0x2d18: v2d18(0x40) = CONST 
    0x2d1b: v2d1b = MLOAD v2d18(0x40)
    0x2d1e: MSTORE v2d1b, v2d49(0x4)
    0x2d1f: v2d1f = MLOAD v2d18(0x40)
    0x2d23: v2d23(0x0) = SUB v2d1b, v2d1f
    0x2d24: v2d24(0x20) = CONST 
    0x2d26: v2d26(0x20) = ADD v2d24(0x20), v2d23(0x0)
    0x2d28: RETURN v2d1f, v2d26(0x20)

}

function CONTRACT_ELEMENT_TOKEN()() public {
    Begin block 0x693
    prev=[], succ=[0x14d5]
    =================================
    0x694: v694(0x2d6c) = CONST 
    0x697: v697(0x14d5) = CONST 
    0x69a: JUMP v697(0x14d5)

    Begin block 0x14d5
    prev=[0x693], succ=[0x2d6c]
    =================================
    0x14d6: v14d6(0x21a7a72a2920a1aa2fa2a622a6a2a72a2faa27a5a2a7) = CONST 
    0x14ed: v14ed(0x51) = CONST 
    0x14ef: v14ef(0x434f4e54524143545f454c454d454e545f544f4b454e00000000000000000000) = SHL v14ed(0x51), v14d6(0x21a7a72a2920a1aa2fa2a622a6a2a72a2faa27a5a2a7)
    0x14f1: JUMP v694(0x2d6c)

    Begin block 0x2d6c
    prev=[0x14d5], succ=[]
    =================================
    0x2d6d: v2d6d(0x40) = CONST 
    0x2d70: v2d70 = MLOAD v2d6d(0x40)
    0x2d73: MSTORE v2d70, v14ef(0x434f4e54524143545f454c454d454e545f544f4b454e00000000000000000000)
    0x2d74: v2d74 = MLOAD v2d6d(0x40)
    0x2d78: v2d78(0x0) = SUB v2d70, v2d74
    0x2d79: v2d79(0x20) = CONST 
    0x2d7b: v2d7b(0x20) = ADD v2d79(0x20), v2d78(0x0)
    0x2d7d: RETURN v2d74, v2d7b(0x20)

}

function getDrillGrade(uint256)() public {
    Begin block 0x69b
    prev=[], succ=[0x6ad, 0x6b1]
    =================================
    0x69c: v69c(0x2d9d) = CONST 
    0x69f: v69f(0x4) = CONST 
    0x6a2: v6a2 = CALLDATASIZE 
    0x6a3: v6a3 = SUB v6a2, v69f(0x4)
    0x6a4: v6a4(0x20) = CONST 
    0x6a7: v6a7 = LT v6a3, v6a4(0x20)
    0x6a8: v6a8 = ISZERO v6a7
    0x6a9: v6a9(0x6b1) = CONST 
    0x6ac: JUMPI v6a9(0x6b1), v6a8

    Begin block 0x6ad
    prev=[0x69b], succ=[]
    =================================
    0x6ad: v6ad(0x0) = CONST 
    0x6b0: REVERT v6ad(0x0), v6ad(0x0)

    Begin block 0x6b1
    prev=[0x69b], succ=[0x14f20x69b]
    =================================
    0x6b3: v6b3 = CALLDATALOAD v69f(0x4)
    0x6b4: v6b4(0x14f2) = CONST 
    0x6b7: JUMP v6b4(0x14f2)

    Begin block 0x14f20x69b
    prev=[0x6b1], succ=[0x2d9d]
    =================================
    0x14f30x69b: v69b14f3(0x70) = CONST 
    0x14f50x69b: v69b14f5 = SHR v69b14f3(0x70), v6b3
    0x14f60x69b: v69b14f6(0xffff) = CONST 
    0x14f90x69b: v69b14f9 = AND v69b14f6(0xffff), v69b14f5
    0x14fb0x69b: JUMP v69c(0x2d9d)

    Begin block 0x2d9d
    prev=[0x14f20x69b], succ=[]
    =================================
    0x2d9e: v2d9e(0x40) = CONST 
    0x2da1: v2da1 = MLOAD v2d9e(0x40)
    0x2da2: v2da2(0xffff) = CONST 
    0x2da7: v2da7 = AND v69b14f9, v2da2(0xffff)
    0x2da9: MSTORE v2da1, v2da7
    0x2daa: v2daa = MLOAD v2d9e(0x40)
    0x2dae: v2dae(0x0) = SUB v2da1, v2daa
    0x2daf: v2daf(0x20) = CONST 
    0x2db1: v2db1(0x20) = ADD v2daf(0x20), v2dae(0x0)
    0x2db3: RETURN v2daa, v2db1(0x20)

}

function CONTRACT_SOIL_ERC20_TOKEN()() public {
    Begin block 0x6b8
    prev=[], succ=[0x14fc]
    =================================
    0x6b9: v6b9(0x2dd3) = CONST 
    0x6bc: v6bc(0x14fc) = CONST 
    0x6bf: JUMP v6bc(0x14fc)

    Begin block 0x14fc
    prev=[0x6b8], succ=[0x2dd3]
    =================================
    0x14fd: v14fd(0x434f4e54524143545f534f494c5f45524332305f544f4b454e00000000000000) = CONST 
    0x151f: JUMP v6b9(0x2dd3)

    Begin block 0x2dd3
    prev=[0x14fc], succ=[]
    =================================
    0x2dd4: v2dd4(0x40) = CONST 
    0x2dd7: v2dd7 = MLOAD v2dd4(0x40)
    0x2dda: MSTORE v2dd7, v14fd(0x434f4e54524143545f534f494c5f45524332305f544f4b454e00000000000000)
    0x2ddb: v2ddb = MLOAD v2dd4(0x40)
    0x2ddf: v2ddf(0x0) = SUB v2dd7, v2ddb
    0x2de0: v2de0(0x20) = CONST 
    0x2de2: v2de2(0x20) = ADD v2de0(0x20), v2ddf(0x0)
    0x2de4: RETURN v2ddb, v2de2(0x20)

}

function owner()() public {
    Begin block 0x6c0
    prev=[], succ=[0x1520]
    =================================
    0x6c1: v6c1(0x2e04) = CONST 
    0x6c4: v6c4(0x1520) = CONST 
    0x6c7: JUMP v6c4(0x1520)

    Begin block 0x1520
    prev=[0x6c0], succ=[0x2e04]
    =================================
    0x1521: v1521(0x1) = CONST 
    0x1523: v1523 = SLOAD v1521(0x1)
    0x1524: v1524(0x1) = CONST 
    0x1526: v1526(0x1) = CONST 
    0x1528: v1528(0xa0) = CONST 
    0x152a: v152a(0x10000000000000000000000000000000000000000) = SHL v1528(0xa0), v1526(0x1)
    0x152b: v152b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v152a(0x10000000000000000000000000000000000000000), v1524(0x1)
    0x152c: v152c = AND v152b(0xffffffffffffffffffffffffffffffffffffffff), v1523
    0x152e: JUMP v6c1(0x2e04)

    Begin block 0x2e04
    prev=[0x1520], succ=[]
    =================================
    0x2e05: v2e05(0x40) = CONST 
    0x2e08: v2e08 = MLOAD v2e05(0x40)
    0x2e09: v2e09(0x1) = CONST 
    0x2e0b: v2e0b(0x1) = CONST 
    0x2e0d: v2e0d(0xa0) = CONST 
    0x2e0f: v2e0f(0x10000000000000000000000000000000000000000) = SHL v2e0d(0xa0), v2e0b(0x1)
    0x2e10: v2e10(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2e0f(0x10000000000000000000000000000000000000000), v2e09(0x1)
    0x2e13: v2e13 = AND v152c, v2e10(0xffffffffffffffffffffffffffffffffffffffff)
    0x2e15: MSTORE v2e08, v2e13
    0x2e16: v2e16 = MLOAD v2e05(0x40)
    0x2e1a: v2e1a(0x0) = SUB v2e08, v2e16
    0x2e1b: v2e1b(0x20) = CONST 
    0x2e1d: v2e1d(0x20) = ADD v2e1b(0x20), v2e1a(0x0)
    0x2e1f: RETURN v2e16, v2e1d(0x20)

}

function getInternalStrengthRate(bytes32,uint16)() public {
    Begin block 0x6c8
    prev=[], succ=[0x6da, 0x6de]
    =================================
    0x6c9: v6c9(0x2e3f) = CONST 
    0x6cc: v6cc(0x4) = CONST 
    0x6cf: v6cf = CALLDATASIZE 
    0x6d0: v6d0 = SUB v6cf, v6cc(0x4)
    0x6d1: v6d1(0x40) = CONST 
    0x6d4: v6d4 = LT v6d0, v6d1(0x40)
    0x6d5: v6d5 = ISZERO v6d4
    0x6d6: v6d6(0x6de) = CONST 
    0x6d9: JUMPI v6d6(0x6de), v6d5

    Begin block 0x6da
    prev=[0x6c8], succ=[]
    =================================
    0x6da: v6da(0x0) = CONST 
    0x6dd: REVERT v6da(0x0), v6da(0x0)

    Begin block 0x6de
    prev=[0x6c8], succ=[0x152f0x6c8]
    =================================
    0x6e1: v6e1 = CALLDATALOAD v6cc(0x4)
    0x6e3: v6e3(0x20) = CONST 
    0x6e5: v6e5(0x24) = ADD v6e3(0x20), v6cc(0x4)
    0x6e6: v6e6 = CALLDATALOAD v6e5(0x24)
    0x6e7: v6e7(0xffff) = CONST 
    0x6ea: v6ea = AND v6e7(0xffff), v6e6
    0x6eb: v6eb(0x152f) = CONST 
    0x6ee: JUMP v6eb(0x152f)

    Begin block 0x152f0x6c8
    prev=[0x6de], succ=[0x15520x6c8, 0x15950x6c8]
    =================================
    0x15300x6c8: v6c81530(0x0) = CONST 
    0x15340x6c8: MSTORE v6c81530(0x0), v6e1
    0x15350x6c8: v6c81535(0x5) = CONST 
    0x15370x6c8: v6c81537(0x20) = CONST 
    0x153b0x6c8: MSTORE v6c81537(0x20), v6c81535(0x5)
    0x153c0x6c8: v6c8153c(0x40) = CONST 
    0x15400x6c8: v6c81540 = SHA3 v6c81530(0x0), v6c8153c(0x40)
    0x15410x6c8: v6c81541(0xffff) = CONST 
    0x15450x6c8: v6c81545 = AND v6ea, v6c81541(0xffff)
    0x15470x6c8: MSTORE v6c81530(0x0), v6c81545
    0x154a0x6c8: MSTORE v6c81537(0x20), v6c81540
    0x154c0x6c8: v6c8154c = SHA3 v6c81530(0x0), v6c8153c(0x40)
    0x154d0x6c8: v6c8154d = SLOAD v6c8154c
    0x154e0x6c8: v6c8154e(0x1595) = CONST 
    0x15510x6c8: JUMPI v6c8154e(0x1595), v6c8154d

    Begin block 0x15520x6c8
    prev=[0x152f0x6c8], succ=[]
    =================================
    0x15520x6c8: v6c81552(0x40) = CONST 
    0x15550x6c8: v6c81555 = MLOAD v6c81552(0x40)
    0x15560x6c8: v6c81556(0x461bcd) = CONST 
    0x155a0x6c8: v6c8155a(0xe5) = CONST 
    0x155c0x6c8: v6c8155c(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v6c8155a(0xe5), v6c81556(0x461bcd)
    0x155e0x6c8: MSTORE v6c81555, v6c8155c(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x155f0x6c8: v6c8155f(0x20) = CONST 
    0x15610x6c8: v6c81561(0x4) = CONST 
    0x15640x6c8: v6c81564 = ADD v6c81555, v6c81561(0x4)
    0x15650x6c8: MSTORE v6c81564, v6c8155f(0x20)
    0x15660x6c8: v6c81566(0x14) = CONST 
    0x15680x6c8: v6c81568(0x24) = CONST 
    0x156b0x6c8: v6c8156b = ADD v6c81555, v6c81568(0x24)
    0x156c0x6c8: MSTORE v6c8156b, v6c81566(0x14)
    0x156d0x6c8: v6c8156d(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0x15820x6c8: v6c81582(0x62) = CONST 
    0x15840x6c8: v6c81584(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL v6c81582(0x62), v6c8156d(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0x15850x6c8: v6c81585(0x44) = CONST 
    0x15880x6c8: v6c81588 = ADD v6c81555, v6c81585(0x44)
    0x15890x6c8: MSTORE v6c81588, v6c81584(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0x158b0x6c8: v6c8158b = MLOAD v6c81552(0x40)
    0x158f0x6c8: v6c8158f(0x0) = SUB v6c81555, v6c8158b
    0x15900x6c8: v6c81590(0x64) = CONST 
    0x15920x6c8: v6c81592(0x64) = ADD v6c81590(0x64), v6c8158f(0x0)
    0x15940x6c8: REVERT v6c8158b, v6c81592(0x64)

    Begin block 0x15950x6c8
    prev=[0x152f0x6c8], succ=[0x2e3f]
    =================================
    0x15970x6c8: v6c81597(0x0) = CONST 
    0x159b0x6c8: MSTORE v6c81597(0x0), v6e1
    0x159c0x6c8: v6c8159c(0x5) = CONST 
    0x159e0x6c8: v6c8159e(0x20) = CONST 
    0x15a20x6c8: MSTORE v6c8159e(0x20), v6c8159c(0x5)
    0x15a30x6c8: v6c815a3(0x40) = CONST 
    0x15a70x6c8: v6c815a7 = SHA3 v6c81597(0x0), v6c815a3(0x40)
    0x15a80x6c8: v6c815a8(0xffff) = CONST 
    0x15ae0x6c8: v6c815ae = AND v6c815a8(0xffff), v6ea
    0x15b00x6c8: MSTORE v6c81597(0x0), v6c815ae
    0x15b30x6c8: MSTORE v6c8159e(0x20), v6c815a7
    0x15b50x6c8: v6c815b5 = SHA3 v6c81597(0x0), v6c815a3(0x40)
    0x15b60x6c8: v6c815b6 = SLOAD v6c815b5
    0x15b80x6c8: JUMP v6c9(0x2e3f)

    Begin block 0x2e3f
    prev=[0x15950x6c8], succ=[]
    =================================
    0x2e40: v2e40(0x40) = CONST 
    0x2e43: v2e43 = MLOAD v2e40(0x40)
    0x2e46: MSTORE v2e43, v6c815b6
    0x2e47: v2e47 = MLOAD v2e40(0x40)
    0x2e4b: v2e4b(0x0) = SUB v2e43, v2e47
    0x2e4c: v2e4c(0x20) = CONST 
    0x2e4e: v2e4e(0x20) = ADD v2e4c(0x20), v2e4b(0x0)
    0x2e50: RETURN v2e47, v2e4e(0x20)

}

function CONTRACT_DRILL_BASE()() public {
    Begin block 0x6ef
    prev=[], succ=[0x15b9]
    =================================
    0x6f0: v6f0(0x2e70) = CONST 
    0x6f3: v6f3(0x15b9) = CONST 
    0x6f6: JUMP v6f3(0x15b9)

    Begin block 0x15b9
    prev=[0x6ef], succ=[0x2e70]
    =================================
    0x15ba: v15ba(0x434f4e54524143545f4452494c4c5f42415345) = CONST 
    0x15ce: v15ce(0x68) = CONST 
    0x15d0: v15d0(0x434f4e54524143545f4452494c4c5f4241534500000000000000000000000000) = SHL v15ce(0x68), v15ba(0x434f4e54524143545f4452494c4c5f42415345)
    0x15d2: JUMP v6f0(0x2e70)

    Begin block 0x2e70
    prev=[0x15b9], succ=[]
    =================================
    0x2e71: v2e71(0x40) = CONST 
    0x2e74: v2e74 = MLOAD v2e71(0x40)
    0x2e77: MSTORE v2e74, v15d0(0x434f4e54524143545f4452494c4c5f4241534500000000000000000000000000)
    0x2e78: v2e78 = MLOAD v2e71(0x40)
    0x2e7c: v2e7c(0x0) = SUB v2e74, v2e78
    0x2e7d: v2e7d(0x20) = CONST 
    0x2e7f: v2e7f(0x20) = ADD v2e7d(0x20), v2e7c(0x0)
    0x2e81: RETURN v2e78, v2e7f(0x20)

}

function CONTRACT_OBJECT_OWNERSHIP()() public {
    Begin block 0x6f7
    prev=[], succ=[0x15d3]
    =================================
    0x6f8: v6f8(0x2ea1) = CONST 
    0x6fb: v6fb(0x15d3) = CONST 
    0x6fe: JUMP v6fb(0x15d3)

    Begin block 0x15d3
    prev=[0x6f7], succ=[0x2ea1]
    =================================
    0x15d4: v15d4(0x434f4e54524143545f4f424a4543545f4f574e45525348495) = CONST 
    0x15ee: v15ee(0x3c) = CONST 
    0x15f0: v15f0(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000) = SHL v15ee(0x3c), v15d4(0x434f4e54524143545f4f424a4543545f4f574e45525348495)
    0x15f2: JUMP v6f8(0x2ea1)

    Begin block 0x2ea1
    prev=[0x15d3], succ=[]
    =================================
    0x2ea2: v2ea2(0x40) = CONST 
    0x2ea5: v2ea5 = MLOAD v2ea2(0x40)
    0x2ea8: MSTORE v2ea5, v15f0(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000)
    0x2ea9: v2ea9 = MLOAD v2ea2(0x40)
    0x2ead: v2ead(0x0) = SUB v2ea5, v2ea9
    0x2eae: v2eae(0x20) = CONST 
    0x2eb0: v2eb0(0x20) = ADD v2eae(0x20), v2ead(0x0)
    0x2eb2: RETURN v2ea9, v2eb0(0x20)

}

function DARWINIA_OBJECT_CLASS()() public {
    Begin block 0x6ff
    prev=[], succ=[0x15f3]
    =================================
    0x700: v700(0x2ed2) = CONST 
    0x703: v703(0x15f3) = CONST 
    0x706: JUMP v703(0x15f3)

    Begin block 0x15f3
    prev=[0x6ff], succ=[0x2ed2]
    =================================
    0x15f4: v15f4(0xfe) = CONST 
    0x15f7: JUMP v700(0x2ed2)

    Begin block 0x2ed2
    prev=[0x15f3], succ=[]
    =================================
    0x2ed3: v2ed3(0x40) = CONST 
    0x2ed6: v2ed6 = MLOAD v2ed3(0x40)
    0x2ed7: v2ed7(0xff) = CONST 
    0x2edb: v2edb(0xfe) = AND v15f4(0xfe), v2ed7(0xff)
    0x2edd: MSTORE v2ed6, v2edb(0xfe)
    0x2ede: v2ede = MLOAD v2ed3(0x40)
    0x2ee2: v2ee2(0x0) = SUB v2ed6, v2ede
    0x2ee3: v2ee3(0x20) = CONST 
    0x2ee5: v2ee5(0x20) = ADD v2ee3(0x20), v2ee2(0x0)
    0x2ee7: RETURN v2ede, v2ee5(0x20)

}

function CONTRACT_METADATA_TELLER()() public {
    Begin block 0x707
    prev=[], succ=[0x15f8]
    =================================
    0x708: v708(0x2f07) = CONST 
    0x70b: v70b(0x15f8) = CONST 
    0x70e: JUMP v70b(0x15f8)

    Begin block 0x15f8
    prev=[0x707], succ=[0x2f07]
    =================================
    0x15f9: v15f9(0x434f4e54524143545f4d455441444154415f54454c4c45520000000000000000) = CONST 
    0x161b: JUMP v708(0x2f07)

    Begin block 0x2f07
    prev=[0x15f8], succ=[]
    =================================
    0x2f08: v2f08(0x40) = CONST 
    0x2f0b: v2f0b = MLOAD v2f08(0x40)
    0x2f0e: MSTORE v2f0b, v15f9(0x434f4e54524143545f4d455441444154415f54454c4c45520000000000000000)
    0x2f0f: v2f0f = MLOAD v2f08(0x40)
    0x2f13: v2f13(0x0) = SUB v2f0b, v2f0f
    0x2f14: v2f14(0x20) = CONST 
    0x2f16: v2f16(0x20) = ADD v2f14(0x20), v2f13(0x0)
    0x2f18: RETURN v2f0f, v2f16(0x20)

}

function CONTRACT_APOSTLE_ITEM_BAR()() public {
    Begin block 0x70f
    prev=[], succ=[0x161c]
    =================================
    0x710: v710(0x2f38) = CONST 
    0x713: v713(0x161c) = CONST 
    0x716: JUMP v713(0x161c)

    Begin block 0x161c
    prev=[0x70f], succ=[0x2f38]
    =================================
    0x161d: v161d(0x434f4e54524143545f41504f53544c455f4954454d5f42415200000000000000) = CONST 
    0x163f: JUMP v710(0x2f38)

    Begin block 0x2f38
    prev=[0x161c], succ=[]
    =================================
    0x2f39: v2f39(0x40) = CONST 
    0x2f3c: v2f3c = MLOAD v2f39(0x40)
    0x2f3f: MSTORE v2f3c, v161d(0x434f4e54524143545f41504f53544c455f4954454d5f42415200000000000000)
    0x2f40: v2f40 = MLOAD v2f39(0x40)
    0x2f44: v2f44(0x0) = SUB v2f3c, v2f40
    0x2f45: v2f45(0x20) = CONST 
    0x2f47: v2f47(0x20) = ADD v2f45(0x20), v2f44(0x0)
    0x2f49: RETURN v2f40, v2f47(0x20)

}

function resourceLPToken2RateAttrId(bytes32,address)() public {
    Begin block 0x717
    prev=[], succ=[0x729, 0x72d]
    =================================
    0x718: v718(0x2f69) = CONST 
    0x71b: v71b(0x4) = CONST 
    0x71e: v71e = CALLDATASIZE 
    0x71f: v71f = SUB v71e, v71b(0x4)
    0x720: v720(0x40) = CONST 
    0x723: v723 = LT v71f, v720(0x40)
    0x724: v724 = ISZERO v723
    0x725: v725(0x72d) = CONST 
    0x728: JUMPI v725(0x72d), v724

    Begin block 0x729
    prev=[0x717], succ=[]
    =================================
    0x729: v729(0x0) = CONST 
    0x72c: REVERT v729(0x0), v729(0x0)

    Begin block 0x72d
    prev=[0x717], succ=[0x1640]
    =================================
    0x730: v730 = CALLDATALOAD v71b(0x4)
    0x732: v732(0x20) = CONST 
    0x734: v734(0x24) = ADD v732(0x20), v71b(0x4)
    0x735: v735 = CALLDATALOAD v734(0x24)
    0x736: v736(0x1) = CONST 
    0x738: v738(0x1) = CONST 
    0x73a: v73a(0xa0) = CONST 
    0x73c: v73c(0x10000000000000000000000000000000000000000) = SHL v73a(0xa0), v738(0x1)
    0x73d: v73d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v73c(0x10000000000000000000000000000000000000000), v736(0x1)
    0x73e: v73e = AND v73d(0xffffffffffffffffffffffffffffffffffffffff), v735
    0x73f: v73f(0x1640) = CONST 
    0x742: JUMP v73f(0x1640)

    Begin block 0x1640
    prev=[0x72d], succ=[0x2f69]
    =================================
    0x1641: v1641(0x3) = CONST 
    0x1643: v1643(0x20) = CONST 
    0x1647: MSTORE v1643(0x20), v1641(0x3)
    0x1648: v1648(0x0) = CONST 
    0x164c: MSTORE v1648(0x0), v730
    0x164d: v164d(0x40) = CONST 
    0x1651: v1651 = SHA3 v1648(0x0), v164d(0x40)
    0x1654: MSTORE v1643(0x20), v1651
    0x1657: MSTORE v1648(0x0), v73e
    0x1659: v1659 = SHA3 v1648(0x0), v164d(0x40)
    0x165a: v165a = SLOAD v1659
    0x165b: v165b(0xff) = CONST 
    0x165d: v165d = AND v165b(0xff), v165a
    0x165f: JUMP v718(0x2f69)

    Begin block 0x2f69
    prev=[0x1640], succ=[]
    =================================
    0x2f6a: v2f6a(0x40) = CONST 
    0x2f6d: v2f6d = MLOAD v2f6a(0x40)
    0x2f6e: v2f6e(0xff) = CONST 
    0x2f72: v2f72 = AND v165d, v2f6e(0xff)
    0x2f74: MSTORE v2f6d, v2f72
    0x2f75: v2f75 = MLOAD v2f6a(0x40)
    0x2f79: v2f79(0x0) = SUB v2f6d, v2f75
    0x2f7a: v2f7a(0x20) = CONST 
    0x2f7c: v2f7c(0x20) = ADD v2f7a(0x20), v2f79(0x0)
    0x2f7e: RETURN v2f75, v2f7c(0x20)

}

function CONTRACT_LP_FIRE_ERC20_TOKEN()() public {
    Begin block 0x743
    prev=[], succ=[0x1660]
    =================================
    0x744: v744(0x2f9e) = CONST 
    0x747: v747(0x1660) = CONST 
    0x74a: JUMP v747(0x1660)

    Begin block 0x1660
    prev=[0x743], succ=[0x2f9e]
    =================================
    0x1661: v1661(0x434f4e54524143545f4c505f464952455f45524332305f544f4b454e00000000) = CONST 
    0x1683: JUMP v744(0x2f9e)

    Begin block 0x2f9e
    prev=[0x1660], succ=[]
    =================================
    0x2f9f: v2f9f(0x40) = CONST 
    0x2fa2: v2fa2 = MLOAD v2f9f(0x40)
    0x2fa5: MSTORE v2fa2, v1661(0x434f4e54524143545f4c505f464952455f45524332305f544f4b454e00000000)
    0x2fa6: v2fa6 = MLOAD v2f9f(0x40)
    0x2faa: v2faa(0x0) = SUB v2fa2, v2fa6
    0x2fab: v2fab(0x20) = CONST 
    0x2fad: v2fad(0x20) = ADD v2fab(0x20), v2faa(0x0)
    0x2faf: RETURN v2fa6, v2fad(0x20)

}

function PREFER_WATER()() public {
    Begin block 0x74b
    prev=[], succ=[0x1684]
    =================================
    0x74c: v74c(0x2fcf) = CONST 
    0x74f: v74f(0x1684) = CONST 
    0x752: JUMP v74f(0x1684)

    Begin block 0x1684
    prev=[0x74b], succ=[0x2fcf]
    =================================
    0x1685: v1685(0x8) = CONST 
    0x1688: JUMP v74c(0x2fcf)

    Begin block 0x2fcf
    prev=[0x1684], succ=[]
    =================================
    0x2fd0: v2fd0(0x40) = CONST 
    0x2fd3: v2fd3 = MLOAD v2fd0(0x40)
    0x2fd6: MSTORE v2fd3, v1685(0x8)
    0x2fd7: v2fd7 = MLOAD v2fd0(0x40)
    0x2fdb: v2fdb(0x0) = SUB v2fd3, v2fd7
    0x2fdc: v2fdc(0x20) = CONST 
    0x2fde: v2fde(0x20) = ADD v2fdc(0x20), v2fdb(0x0)
    0x2fe0: RETURN v2fd7, v2fde(0x20)

}

function removeExternalTokenMeta(address)() public {
    Begin block 0x753
    prev=[], succ=[0x765, 0x769]
    =================================
    0x754: v754(0x3000) = CONST 
    0x757: v757(0x4) = CONST 
    0x75a: v75a = CALLDATASIZE 
    0x75b: v75b = SUB v75a, v757(0x4)
    0x75c: v75c(0x20) = CONST 
    0x75f: v75f = LT v75b, v75c(0x20)
    0x760: v760 = ISZERO v75f
    0x761: v761(0x769) = CONST 
    0x764: JUMPI v761(0x769), v760

    Begin block 0x765
    prev=[0x753], succ=[]
    =================================
    0x765: v765(0x0) = CONST 
    0x768: REVERT v765(0x0), v765(0x0)

    Begin block 0x769
    prev=[0x753], succ=[0x1689]
    =================================
    0x76b: v76b = CALLDATALOAD v757(0x4)
    0x76c: v76c(0x1) = CONST 
    0x76e: v76e(0x1) = CONST 
    0x770: v770(0xa0) = CONST 
    0x772: v772(0x10000000000000000000000000000000000000000) = SHL v770(0xa0), v76e(0x1)
    0x773: v773(0xffffffffffffffffffffffffffffffffffffffff) = SUB v772(0x10000000000000000000000000000000000000000), v76c(0x1)
    0x774: v774 = AND v773(0xffffffffffffffffffffffffffffffffffffffff), v76b
    0x775: v775(0x1689) = CONST 
    0x778: JUMP v775(0x1689)

    Begin block 0x1689
    prev=[0x769], succ=[0x169f]
    =================================
    0x168a: v168a(0x169f) = CONST 
    0x168d: v168d = CALLER 
    0x168e: v168e(0x0) = CONST 
    0x1690: v1690 = CALLDATALOAD v168e(0x0)
    0x1691: v1691(0x1) = CONST 
    0x1693: v1693(0x1) = CONST 
    0x1695: v1695(0xe0) = CONST 
    0x1697: v1697(0x100000000000000000000000000000000000000000000000000000000) = SHL v1695(0xe0), v1693(0x1)
    0x1698: v1698(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1697(0x100000000000000000000000000000000000000000000000000000000), v1691(0x1)
    0x1699: v1699(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1698(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x169a: v169a = AND v1699(0xffffffff00000000000000000000000000000000000000000000000000000000), v1690
    0x169b: v169b(0x22d3) = CONST 
    0x169e: v169e_0 = CALLPRIVATE v169b(0x22d3), v169a, v168d, v168a(0x169f)

    Begin block 0x169f
    prev=[0x1689], succ=[0x16a4, 0x16de]
    =================================
    0x16a0: v16a0(0x16de) = CONST 
    0x16a3: JUMPI v16a0(0x16de), v169e_0

    Begin block 0x16a4
    prev=[0x169f], succ=[]
    =================================
    0x16a4: v16a4(0x40) = CONST 
    0x16a7: v16a7 = MLOAD v16a4(0x40)
    0x16a8: v16a8(0x461bcd) = CONST 
    0x16ac: v16ac(0xe5) = CONST 
    0x16ae: v16ae(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v16ac(0xe5), v16a8(0x461bcd)
    0x16b0: MSTORE v16a7, v16ae(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x16b1: v16b1(0x20) = CONST 
    0x16b3: v16b3(0x4) = CONST 
    0x16b6: v16b6 = ADD v16a7, v16b3(0x4)
    0x16b7: MSTORE v16b6, v16b1(0x20)
    0x16b8: v16b8(0x14) = CONST 
    0x16ba: v16ba(0x24) = CONST 
    0x16bd: v16bd = ADD v16a7, v16ba(0x24)
    0x16be: MSTORE v16bd, v16b8(0x14)
    0x16bf: v16bf(0x0) = CONST 
    0x16c2: v16c2 = MLOAD v16bf(0x0)
    0x16c3: v16c3(0x20) = CONST 
    0x16c5: v16c5(0x2409) = CONST 
    0x16cd: MSTORE v16bf(0x0), v16c2
    0x16ce: v16ce(0x44) = CONST 
    0x16d1: v16d1 = ADD v16a7, v16ce(0x44)
    0x16d2: MSTORE v16d1, v33f5(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x16d4: v16d4 = MLOAD v16a4(0x40)
    0x16d8: v16d8(0x0) = SUB v16a7, v16d4
    0x16d9: v16d9(0x64) = CONST 
    0x16db: v16db(0x64) = ADD v16d9(0x64), v16d8(0x0)
    0x16dd: REVERT v16d4, v16db(0x64)
    0x33f5: v33f5(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x16de
    prev=[0x169f], succ=[0x1700, 0x173d]
    =================================
    0x16df: v16df(0x1) = CONST 
    0x16e1: v16e1(0x1) = CONST 
    0x16e3: v16e3(0xa0) = CONST 
    0x16e5: v16e5(0x10000000000000000000000000000000000000000) = SHL v16e3(0xa0), v16e1(0x1)
    0x16e6: v16e6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v16e5(0x10000000000000000000000000000000000000000), v16df(0x1)
    0x16e8: v16e8 = AND v774, v16e6(0xffffffffffffffffffffffffffffffffffffffff)
    0x16e9: v16e9(0x0) = CONST 
    0x16ed: MSTORE v16e9(0x0), v16e8
    0x16ee: v16ee(0x4) = CONST 
    0x16f0: v16f0(0x20) = CONST 
    0x16f2: MSTORE v16f0(0x20), v16ee(0x4)
    0x16f3: v16f3(0x40) = CONST 
    0x16f6: v16f6 = SHA3 v16e9(0x0), v16f3(0x40)
    0x16f7: v16f7 = SLOAD v16f6
    0x16f8: v16f8(0xffff) = CONST 
    0x16fb: v16fb = AND v16f8(0xffff), v16f7
    0x16fc: v16fc(0x173d) = CONST 
    0x16ff: JUMPI v16fc(0x173d), v16fb

    Begin block 0x1700
    prev=[0x16de], succ=[]
    =================================
    0x1700: v1700(0x40) = CONST 
    0x1703: v1703 = MLOAD v1700(0x40)
    0x1704: v1704(0x461bcd) = CONST 
    0x1708: v1708(0xe5) = CONST 
    0x170a: v170a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1708(0xe5), v1704(0x461bcd)
    0x170c: MSTORE v1703, v170a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x170d: v170d(0x20) = CONST 
    0x170f: v170f(0x4) = CONST 
    0x1712: v1712 = ADD v1703, v170f(0x4)
    0x1713: MSTORE v1712, v170d(0x20)
    0x1714: v1714(0xe) = CONST 
    0x1716: v1716(0x24) = CONST 
    0x1719: v1719 = ADD v1703, v1716(0x24)
    0x171a: MSTORE v1719, v1714(0xe)
    0x171b: v171b(0x4675726e6163653a20454d505459) = CONST 
    0x172a: v172a(0x90) = CONST 
    0x172c: v172c(0x4675726e6163653a20454d505459000000000000000000000000000000000000) = SHL v172a(0x90), v171b(0x4675726e6163653a20454d505459)
    0x172d: v172d(0x44) = CONST 
    0x1730: v1730 = ADD v1703, v172d(0x44)
    0x1731: MSTORE v1730, v172c(0x4675726e6163653a20454d505459000000000000000000000000000000000000)
    0x1733: v1733 = MLOAD v1700(0x40)
    0x1737: v1737(0x0) = SUB v1703, v1733
    0x1738: v1738(0x64) = CONST 
    0x173a: v173a(0x64) = ADD v1738(0x64), v1737(0x0)
    0x173c: REVERT v1733, v173a(0x64)

    Begin block 0x173d
    prev=[0x16de], succ=[0x3000]
    =================================
    0x173e: v173e(0x1) = CONST 
    0x1740: v1740(0x1) = CONST 
    0x1742: v1742(0xa0) = CONST 
    0x1744: v1744(0x10000000000000000000000000000000000000000) = SHL v1742(0xa0), v1740(0x1)
    0x1745: v1745(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1744(0x10000000000000000000000000000000000000000), v173e(0x1)
    0x1747: v1747 = AND v774, v1745(0xffffffffffffffffffffffffffffffffffffffff)
    0x1748: v1748(0x0) = CONST 
    0x174c: MSTORE v1748(0x0), v1747
    0x174d: v174d(0x4) = CONST 
    0x174f: v174f(0x20) = CONST 
    0x1751: MSTORE v174f(0x20), v174d(0x4)
    0x1752: v1752(0x40) = CONST 
    0x1756: v1756 = SHA3 v1748(0x0), v1752(0x40)
    0x1758: v1758 = SLOAD v1756
    0x1759: v1759(0xffff) = CONST 
    0x175c: v175c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT v1759(0xffff)
    0x175d: v175d = AND v175c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000), v1758
    0x175f: SSTORE v1756, v175d
    0x1760: v1760 = MLOAD v1752(0x40)
    0x1761: v1761(0x40d3a28bfc35eb505cbed026b5858d1b1a934c3143bacd0196a14bc7c9aae142) = CONST 
    0x1784: LOG2 v1760, v1748(0x0), v1761(0x40d3a28bfc35eb505cbed026b5858d1b1a934c3143bacd0196a14bc7c9aae142), v1747
    0x1786: JUMP v754(0x3000)

    Begin block 0x3000
    prev=[0x173d], succ=[]
    =================================
    0x3001: STOP 

}

function authority()() public {
    Begin block 0x779
    prev=[], succ=[0x1787]
    =================================
    0x77a: v77a(0x3021) = CONST 
    0x77d: v77d(0x1787) = CONST 
    0x780: JUMP v77d(0x1787)

    Begin block 0x1787
    prev=[0x779], succ=[0x3021]
    =================================
    0x1788: v1788(0x0) = CONST 
    0x178a: v178a = SLOAD v1788(0x0)
    0x178b: v178b(0x10000) = CONST 
    0x1790: v1790 = DIV v178a, v178b(0x10000)
    0x1791: v1791(0x1) = CONST 
    0x1793: v1793(0x1) = CONST 
    0x1795: v1795(0xa0) = CONST 
    0x1797: v1797(0x10000000000000000000000000000000000000000) = SHL v1795(0xa0), v1793(0x1)
    0x1798: v1798(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1797(0x10000000000000000000000000000000000000000), v1791(0x1)
    0x1799: v1799 = AND v1798(0xffffffffffffffffffffffffffffffffffffffff), v1790
    0x179b: JUMP v77a(0x3021)

    Begin block 0x3021
    prev=[0x1787], succ=[]
    =================================
    0x3022: v3022(0x40) = CONST 
    0x3025: v3025 = MLOAD v3022(0x40)
    0x3026: v3026(0x1) = CONST 
    0x3028: v3028(0x1) = CONST 
    0x302a: v302a(0xa0) = CONST 
    0x302c: v302c(0x10000000000000000000000000000000000000000) = SHL v302a(0xa0), v3028(0x1)
    0x302d: v302d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v302c(0x10000000000000000000000000000000000000000), v3026(0x1)
    0x3030: v3030 = AND v1799, v302d(0xffffffffffffffffffffffffffffffffffffffff)
    0x3032: MSTORE v3025, v3030
    0x3033: v3033 = MLOAD v3022(0x40)
    0x3037: v3037(0x0) = SUB v3025, v3033
    0x3038: v3038(0x20) = CONST 
    0x303a: v303a(0x20) = ADD v3038(0x20), v3037(0x0)
    0x303c: RETURN v3033, v303a(0x20)

}

function PREFER_GOLD()() public {
    Begin block 0x781
    prev=[], succ=[0x179c]
    =================================
    0x782: v782(0x305c) = CONST 
    0x785: v785(0x179c) = CONST 
    0x788: JUMP v785(0x179c)

    Begin block 0x179c
    prev=[0x781], succ=[0x305c]
    =================================
    0x179d: v179d(0x2) = CONST 
    0x17a0: JUMP v782(0x305c)

    Begin block 0x305c
    prev=[0x179c], succ=[]
    =================================
    0x305d: v305d(0x40) = CONST 
    0x3060: v3060 = MLOAD v305d(0x40)
    0x3063: MSTORE v3060, v179d(0x2)
    0x3064: v3064 = MLOAD v305d(0x40)
    0x3068: v3068(0x0) = SUB v3060, v3064
    0x3069: v3069(0x20) = CONST 
    0x306b: v306b(0x20) = ADD v3069(0x20), v3068(0x0)
    0x306d: RETURN v3064, v306b(0x20)

}

function initialize(address)() public {
    Begin block 0x789
    prev=[], succ=[0x79b, 0x79f]
    =================================
    0x78a: v78a(0x308d) = CONST 
    0x78d: v78d(0x4) = CONST 
    0x790: v790 = CALLDATASIZE 
    0x791: v791 = SUB v790, v78d(0x4)
    0x792: v792(0x20) = CONST 
    0x795: v795 = LT v791, v792(0x20)
    0x796: v796 = ISZERO v795
    0x797: v797(0x79f) = CONST 
    0x79a: JUMPI v797(0x79f), v796

    Begin block 0x79b
    prev=[0x789], succ=[]
    =================================
    0x79b: v79b(0x0) = CONST 
    0x79e: REVERT v79b(0x0), v79b(0x0)

    Begin block 0x79f
    prev=[0x789], succ=[0x17a1]
    =================================
    0x7a1: v7a1 = CALLDATALOAD v78d(0x4)
    0x7a2: v7a2(0x1) = CONST 
    0x7a4: v7a4(0x1) = CONST 
    0x7a6: v7a6(0xa0) = CONST 
    0x7a8: v7a8(0x10000000000000000000000000000000000000000) = SHL v7a6(0xa0), v7a4(0x1)
    0x7a9: v7a9(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7a8(0x10000000000000000000000000000000000000000), v7a2(0x1)
    0x7aa: v7aa = AND v7a9(0xffffffffffffffffffffffffffffffffffffffff), v7a1
    0x7ab: v7ab(0x17a1) = CONST 
    0x7ae: JUMP v7ab(0x17a1)

    Begin block 0x17a1
    prev=[0x79f], succ=[0x17ba, 0x17b2]
    =================================
    0x17a2: v17a2(0x0) = CONST 
    0x17a4: v17a4 = SLOAD v17a2(0x0)
    0x17a5: v17a5(0x100) = CONST 
    0x17a9: v17a9 = DIV v17a4, v17a5(0x100)
    0x17aa: v17aa(0xff) = CONST 
    0x17ac: v17ac = AND v17aa(0xff), v17a9
    0x17ae: v17ae(0x17ba) = CONST 
    0x17b1: JUMPI v17ae(0x17ba), v17ac

    Begin block 0x17ba
    prev=[0x17a1, 0x2394], succ=[0x17c8, 0x17c0]
    =================================
    0x17ba_0x0: v17ba_0 = PHI v17ac, v2397
    0x17bc: v17bc(0x17c8) = CONST 
    0x17bf: JUMPI v17bc(0x17c8), v17ba_0

    Begin block 0x17c8
    prev=[0x17ba, 0x17c0], succ=[0x17cd, 0x1803]
    =================================
    0x17c8_0x0: v17c8_0 = PHI v17ac, v17c7, v2397
    0x17c9: v17c9(0x1803) = CONST 
    0x17cc: JUMPI v17c9(0x1803), v17c8_0

    Begin block 0x17cd
    prev=[0x17c8], succ=[]
    =================================
    0x17cd: v17cd(0x40) = CONST 
    0x17cf: v17cf = MLOAD v17cd(0x40)
    0x17d0: v17d0(0x461bcd) = CONST 
    0x17d4: v17d4(0xe5) = CONST 
    0x17d6: v17d6(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v17d4(0xe5), v17d0(0x461bcd)
    0x17d8: MSTORE v17cf, v17d6(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x17d9: v17d9(0x4) = CONST 
    0x17db: v17db = ADD v17d9(0x4), v17cf
    0x17de: v17de(0x20) = CONST 
    0x17e0: v17e0 = ADD v17de(0x20), v17db
    0x17e3: v17e3(0x20) = SUB v17e0, v17db
    0x17e5: MSTORE v17db, v17e3(0x20)
    0x17e6: v17e6(0x2e) = CONST 
    0x17e9: MSTORE v17e0, v17e6(0x2e)
    0x17ea: v17ea(0x20) = CONST 
    0x17ec: v17ec = ADD v17ea(0x20), v17e0
    0x17ee: v17ee(0x239b) = CONST 
    0x17f1: v17f1(0x2e) = CONST 
    0x17f4: CODECOPY v17ec, v17ee(0x239b), v17f1(0x2e)
    0x17f5: v17f5(0x40) = CONST 
    0x17f7: v17f7 = ADD v17f5(0x40), v17ec
    0x17fb: v17fb(0x40) = CONST 
    0x17fd: v17fd = MLOAD v17fb(0x40)
    0x1800: v1800(0x84) = SUB v17f7, v17fd
    0x1802: REVERT v17fd, v1800(0x84)

    Begin block 0x1803
    prev=[0x17c8], succ=[0x1816, 0x182e]
    =================================
    0x1804: v1804(0x0) = CONST 
    0x1806: v1806 = SLOAD v1804(0x0)
    0x1807: v1807(0x100) = CONST 
    0x180b: v180b = DIV v1806, v1807(0x100)
    0x180c: v180c(0xff) = CONST 
    0x180e: v180e = AND v180c(0xff), v180b
    0x180f: v180f = ISZERO v180e
    0x1811: v1811 = ISZERO v180f
    0x1812: v1812(0x182e) = CONST 
    0x1815: JUMPI v1812(0x182e), v1811

    Begin block 0x1816
    prev=[0x1803], succ=[0x182e]
    =================================
    0x1816: v1816(0x0) = CONST 
    0x1819: v1819 = SLOAD v1816(0x0)
    0x181a: v181a(0xff) = CONST 
    0x181c: v181c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v181a(0xff)
    0x181d: v181d(0xff00) = CONST 
    0x1820: v1820(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v181d(0xff00)
    0x1823: v1823 = AND v1819, v1820(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff)
    0x1824: v1824(0x100) = CONST 
    0x1827: v1827 = OR v1824(0x100), v1823
    0x1828: v1828 = AND v1827, v181c(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00)
    0x1829: v1829(0x1) = CONST 
    0x182b: v182b = OR v1829(0x1), v1828
    0x182d: SSTORE v1816(0x0), v182b

    Begin block 0x182e
    prev=[0x1816, 0x1803], succ=[0x1910, 0x1914]
    =================================
    0x182f: v182f(0x1) = CONST 
    0x1832: v1832 = SLOAD v182f(0x1)
    0x1833: v1833(0x1) = CONST 
    0x1835: v1835(0x1) = CONST 
    0x1837: v1837(0xa0) = CONST 
    0x1839: v1839(0x10000000000000000000000000000000000000000) = SHL v1837(0xa0), v1835(0x1)
    0x183a: v183a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1839(0x10000000000000000000000000000000000000000), v1833(0x1)
    0x183b: v183b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v183a(0xffffffffffffffffffffffffffffffffffffffff)
    0x183c: v183c = AND v183b(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1832
    0x183d: v183d = CALLER 
    0x1840: v1840 = OR v183d, v183c
    0x1843: SSTORE v182f(0x1), v1840
    0x1844: v1844(0x40) = CONST 
    0x1846: v1846 = MLOAD v1844(0x40)
    0x1847: v1847(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94) = CONST 
    0x1869: v1869(0x0) = CONST 
    0x186c: LOG2 v1846, v1869(0x0), v1847(0xce241d7ca1f669fee44b6fc00b8eba2df3bb514eed0f6f668f8f89096e81ed94), v183d
    0x186d: v186d(0x2) = CONST 
    0x1870: v1870 = SLOAD v186d(0x2)
    0x1871: v1871(0x1) = CONST 
    0x1873: v1873(0x1) = CONST 
    0x1875: v1875(0xa0) = CONST 
    0x1877: v1877(0x10000000000000000000000000000000000000000) = SHL v1875(0xa0), v1873(0x1)
    0x1878: v1878(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1877(0x10000000000000000000000000000000000000000), v1871(0x1)
    0x1879: v1879(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v1878(0xffffffffffffffffffffffffffffffffffffffff)
    0x187a: v187a = AND v1879(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v1870
    0x187b: v187b(0x1) = CONST 
    0x187d: v187d(0x1) = CONST 
    0x187f: v187f(0xa0) = CONST 
    0x1881: v1881(0x10000000000000000000000000000000000000000) = SHL v187f(0xa0), v187d(0x1)
    0x1882: v1882(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1881(0x10000000000000000000000000000000000000000), v187b(0x1)
    0x1885: v1885 = AND v1882(0xffffffffffffffffffffffffffffffffffffffff), v7aa
    0x1889: v1889 = OR v1885, v187a
    0x188d: SSTORE v186d(0x2), v1889
    0x188e: v188e(0x0) = CONST 
    0x1891: v1891 = MLOAD v188e(0x0)
    0x1892: v1892(0x20) = CONST 
    0x1894: v1894(0x23e9) = CONST 
    0x189c: MSTORE v188e(0x0), v1891
    0x189d: v189d(0x0) = CONST 
    0x18a1: MSTORE v189d(0x0), v33fa(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x18a2: v18a2(0x3) = CONST 
    0x18a4: v18a4(0x20) = CONST 
    0x18a8: MSTORE v18a4(0x20), v18a2(0x3)
    0x18a9: v18a9(0x40) = CONST 
    0x18ac: v18ac = MLOAD v18a9(0x40)
    0x18ad: v18ad(0x2ecd14d3) = CONST 
    0x18b2: v18b2(0xe2) = CONST 
    0x18b4: v18b4(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v18b2(0xe2), v18ad(0x2ecd14d3)
    0x18b6: MSTORE v18ac, v18b4(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x18b7: v18b7(0x434f4e54524143545f4c505f474f4c445f45524332305f544f4b454e00000000) = CONST 
    0x18d8: v18d8(0x4) = CONST 
    0x18db: v18db = ADD v18ac, v18d8(0x4)
    0x18dc: MSTORE v18db, v18b7(0x434f4e54524143545f4c505f474f4c445f45524332305f544f4b454e00000000)
    0x18de: v18de = MLOAD v18a9(0x40)
    0x18df: v18df(0x1) = CONST 
    0x18e2: v18e2(0x0) = CONST 
    0x18e5: v18e5 = MLOAD v18e2(0x0)
    0x18e6: v18e6(0x20) = CONST 
    0x18e8: v18e8(0x23c9) = CONST 
    0x18f0: MSTORE v18e2(0x0), v18e5
    0x18f2: v18f2 = AND v1882(0xffffffffffffffffffffffffffffffffffffffff), v1889
    0x18f4: v18f4(0xbb34534c) = CONST 
    0x18fa: v18fa(0x24) = CONST 
    0x18fe: v18fe = ADD v18ac, v18fa(0x24)
    0x1903: v1903(0x0) = SUB v18ac, v18de
    0x1904: v1904(0x24) = ADD v1903(0x0), v18fa(0x24)
    0x1908: v1908 = EXTCODESIZE v18f2
    0x1909: v1909 = ISZERO v1908
    0x190b: v190b = ISZERO v1909
    0x190c: v190c(0x1914) = CONST 
    0x190f: JUMPI v190c(0x1914), v190b
    0x33fa: v33fa(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 
    0x33ff: v33ff(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01) = CONST 

    Begin block 0x1910
    prev=[0x182e], succ=[]
    =================================
    0x1910: v1910(0x0) = CONST 
    0x1913: REVERT v1910(0x0), v1910(0x0)

    Begin block 0x1914
    prev=[0x182e], succ=[0x191f, 0x1928]
    =================================
    0x1916: v1916 = GAS 
    0x1917: v1917 = STATICCALL v1916, v18f2, v18de, v1904(0x24), v18de, v18a4(0x20)
    0x1918: v1918 = ISZERO v1917
    0x191a: v191a = ISZERO v1918
    0x191b: v191b(0x1928) = CONST 
    0x191e: JUMPI v191b(0x1928), v191a

    Begin block 0x191f
    prev=[0x1914], succ=[]
    =================================
    0x191f: v191f = RETURNDATASIZE 
    0x1920: v1920(0x0) = CONST 
    0x1923: RETURNDATACOPY v1920(0x0), v1920(0x0), v191f
    0x1924: v1924 = RETURNDATASIZE 
    0x1925: v1925(0x0) = CONST 
    0x1927: REVERT v1925(0x0), v1924

    Begin block 0x1928
    prev=[0x1914], succ=[0x193a, 0x193e]
    =================================
    0x192d: v192d(0x40) = CONST 
    0x192f: v192f = MLOAD v192d(0x40)
    0x1930: v1930 = RETURNDATASIZE 
    0x1931: v1931(0x20) = CONST 
    0x1934: v1934 = LT v1930, v1931(0x20)
    0x1935: v1935 = ISZERO v1934
    0x1936: v1936(0x193e) = CONST 
    0x1939: JUMPI v1936(0x193e), v1935

    Begin block 0x193a
    prev=[0x1928], succ=[]
    =================================
    0x193a: v193a(0x0) = CONST 
    0x193d: REVERT v193a(0x0), v193a(0x0)

    Begin block 0x193e
    prev=[0x1928], succ=[0x19f5, 0x19f9]
    =================================
    0x1940: v1940 = MLOAD v192f
    0x1941: v1941(0x1) = CONST 
    0x1943: v1943(0x1) = CONST 
    0x1945: v1945(0xa0) = CONST 
    0x1947: v1947(0x10000000000000000000000000000000000000000) = SHL v1945(0xa0), v1943(0x1)
    0x1948: v1948(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1947(0x10000000000000000000000000000000000000000), v1941(0x1)
    0x194b: v194b = AND v1948(0xffffffffffffffffffffffffffffffffffffffff), v1940
    0x194d: MSTORE v189d(0x0), v194b
    0x194e: v194e(0x20) = CONST 
    0x1952: v1952(0x20) = ADD v189d(0x0), v194e(0x20)
    0x1956: MSTORE v1952(0x20), v33ff(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01)
    0x1957: v1957(0x40) = CONST 
    0x195b: v195b(0x40) = ADD v1957(0x40), v189d(0x0)
    0x195c: v195c(0x0) = CONST 
    0x1960: v1960 = SHA3 v195c(0x0), v195b(0x40)
    0x1962: v1962 = SLOAD v1960
    0x1963: v1963(0xff) = CONST 
    0x1965: v1965(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1963(0xff)
    0x1966: v1966 = AND v1965(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1962
    0x1967: v1967(0xff) = CONST 
    0x196c: v196c(0x1) = AND v1967(0xff), v18df(0x1)
    0x1970: v1970 = OR v196c(0x1), v1966
    0x1973: SSTORE v1960, v1970
    0x1974: v1974(0x0) = CONST 
    0x1977: v1977 = MLOAD v1974(0x0)
    0x1978: v1978(0x20) = CONST 
    0x197a: v197a(0x23e9) = CONST 
    0x1982: MSTORE v1974(0x0), v1977
    0x1984: MSTORE v195c(0x0), v3404(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x1985: v1985(0x3) = CONST 
    0x1988: MSTORE v194e(0x20), v1985(0x3)
    0x1989: v1989(0x2) = CONST 
    0x198c: v198c = SLOAD v1989(0x2)
    0x198e: v198e = MLOAD v1957(0x40)
    0x198f: v198f(0x2ecd14d3) = CONST 
    0x1994: v1994(0xe2) = CONST 
    0x1996: v1996(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1994(0xe2), v198f(0x2ecd14d3)
    0x1998: MSTORE v198e, v1996(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1999: v1999(0x434f4e54524143545f4c505f574f4f445f45524332305f544f4b454e00000000) = CONST 
    0x19ba: v19ba(0x4) = CONST 
    0x19bd: v19bd = ADD v198e, v19ba(0x4)
    0x19be: MSTORE v19bd, v1999(0x434f4e54524143545f4c505f574f4f445f45524332305f544f4b454e00000000)
    0x19c0: v19c0 = MLOAD v1957(0x40)
    0x19c3: v19c3(0x0) = CONST 
    0x19c6: v19c6 = MLOAD v19c3(0x0)
    0x19c7: v19c7(0x20) = CONST 
    0x19c9: v19c9(0x23c9) = CONST 
    0x19d1: MSTORE v19c3(0x0), v19c6
    0x19d8: v19d8 = AND v1948(0xffffffffffffffffffffffffffffffffffffffff), v198c
    0x19da: v19da(0xbb34534c) = CONST 
    0x19e0: v19e0(0x24) = CONST 
    0x19e4: v19e4 = ADD v198e, v19e0(0x24)
    0x19e8: v19e8(0x0) = SUB v198e, v19c0
    0x19e9: v19e9(0x24) = ADD v19e8(0x0), v19e0(0x24)
    0x19ed: v19ed = EXTCODESIZE v19d8
    0x19ee: v19ee = ISZERO v19ed
    0x19f0: v19f0 = ISZERO v19ee
    0x19f1: v19f1(0x19f9) = CONST 
    0x19f4: JUMPI v19f1(0x19f9), v19f0
    0x3404: v3404(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 
    0x3409: v3409(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01) = CONST 

    Begin block 0x19f5
    prev=[0x193e], succ=[]
    =================================
    0x19f5: v19f5(0x0) = CONST 
    0x19f8: REVERT v19f5(0x0), v19f5(0x0)

    Begin block 0x19f9
    prev=[0x193e], succ=[0x1a04, 0x1a0d]
    =================================
    0x19fb: v19fb = GAS 
    0x19fc: v19fc = STATICCALL v19fb, v19d8, v19c0, v19e9(0x24), v19c0, v194e(0x20)
    0x19fd: v19fd = ISZERO v19fc
    0x19ff: v19ff = ISZERO v19fd
    0x1a00: v1a00(0x1a0d) = CONST 
    0x1a03: JUMPI v1a00(0x1a0d), v19ff

    Begin block 0x1a04
    prev=[0x19f9], succ=[]
    =================================
    0x1a04: v1a04 = RETURNDATASIZE 
    0x1a05: v1a05(0x0) = CONST 
    0x1a08: RETURNDATACOPY v1a05(0x0), v1a05(0x0), v1a04
    0x1a09: v1a09 = RETURNDATASIZE 
    0x1a0a: v1a0a(0x0) = CONST 
    0x1a0c: REVERT v1a0a(0x0), v1a09

    Begin block 0x1a0d
    prev=[0x19f9], succ=[0x1a1f, 0x1a23]
    =================================
    0x1a12: v1a12(0x40) = CONST 
    0x1a14: v1a14 = MLOAD v1a12(0x40)
    0x1a15: v1a15 = RETURNDATASIZE 
    0x1a16: v1a16(0x20) = CONST 
    0x1a19: v1a19 = LT v1a15, v1a16(0x20)
    0x1a1a: v1a1a = ISZERO v1a19
    0x1a1b: v1a1b(0x1a23) = CONST 
    0x1a1e: JUMPI v1a1b(0x1a23), v1a1a

    Begin block 0x1a1f
    prev=[0x1a0d], succ=[]
    =================================
    0x1a1f: v1a1f(0x0) = CONST 
    0x1a22: REVERT v1a1f(0x0), v1a1f(0x0)

    Begin block 0x1a23
    prev=[0x1a0d], succ=[0x1ada, 0x1ade]
    =================================
    0x1a25: v1a25 = MLOAD v1a14
    0x1a26: v1a26(0x1) = CONST 
    0x1a28: v1a28(0x1) = CONST 
    0x1a2a: v1a2a(0xa0) = CONST 
    0x1a2c: v1a2c(0x10000000000000000000000000000000000000000) = SHL v1a2a(0xa0), v1a28(0x1)
    0x1a2d: v1a2d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1a2c(0x10000000000000000000000000000000000000000), v1a26(0x1)
    0x1a30: v1a30 = AND v1a2d(0xffffffffffffffffffffffffffffffffffffffff), v1a25
    0x1a32: MSTORE v195c(0x0), v1a30
    0x1a33: v1a33(0x20) = CONST 
    0x1a37: v1a37(0x20) = ADD v195c(0x0), v1a33(0x20)
    0x1a3b: MSTORE v1a37(0x20), v3409(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01)
    0x1a3c: v1a3c(0x40) = CONST 
    0x1a40: v1a40(0x40) = ADD v1a3c(0x40), v195c(0x0)
    0x1a41: v1a41(0x0) = CONST 
    0x1a45: v1a45 = SHA3 v1a41(0x0), v1a40(0x40)
    0x1a47: v1a47 = SLOAD v1a45
    0x1a48: v1a48(0xff) = CONST 
    0x1a4a: v1a4a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1a48(0xff)
    0x1a4b: v1a4b = AND v1a4a(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1a47
    0x1a4c: v1a4c(0xff) = CONST 
    0x1a51: v1a51(0x2) = AND v1a4c(0xff), v1989(0x2)
    0x1a55: v1a55 = OR v1a51(0x2), v1a4b
    0x1a58: SSTORE v1a45, v1a55
    0x1a59: v1a59(0x0) = CONST 
    0x1a5c: v1a5c = MLOAD v1a59(0x0)
    0x1a5d: v1a5d(0x20) = CONST 
    0x1a5f: v1a5f(0x23e9) = CONST 
    0x1a67: MSTORE v1a59(0x0), v1a5c
    0x1a69: MSTORE v1a41(0x0), v340e(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x1a6a: v1a6a(0x3) = CONST 
    0x1a6e: MSTORE v1a33(0x20), v1a6a(0x3)
    0x1a6f: v1a6f(0x2) = CONST 
    0x1a71: v1a71 = SLOAD v1a6f(0x2)
    0x1a73: v1a73 = MLOAD v1a3c(0x40)
    0x1a74: v1a74(0x2ecd14d3) = CONST 
    0x1a79: v1a79(0xe2) = CONST 
    0x1a7b: v1a7b(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1a79(0xe2), v1a74(0x2ecd14d3)
    0x1a7d: MSTORE v1a73, v1a7b(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1a7e: v1a7e(0x434f4e54524143545f4c505f57415445525f45524332305f544f4b454e000000) = CONST 
    0x1a9f: v1a9f(0x4) = CONST 
    0x1aa2: v1aa2 = ADD v1a73, v1a9f(0x4)
    0x1aa3: MSTORE v1aa2, v1a7e(0x434f4e54524143545f4c505f57415445525f45524332305f544f4b454e000000)
    0x1aa5: v1aa5 = MLOAD v1a3c(0x40)
    0x1aa8: v1aa8(0x0) = CONST 
    0x1aab: v1aab = MLOAD v1aa8(0x0)
    0x1aac: v1aac(0x20) = CONST 
    0x1aae: v1aae(0x23c9) = CONST 
    0x1ab6: MSTORE v1aa8(0x0), v1aab
    0x1abd: v1abd = AND v1a2d(0xffffffffffffffffffffffffffffffffffffffff), v1a71
    0x1abf: v1abf(0xbb34534c) = CONST 
    0x1ac5: v1ac5(0x24) = CONST 
    0x1ac9: v1ac9 = ADD v1a73, v1ac5(0x24)
    0x1acd: v1acd(0x0) = SUB v1a73, v1aa5
    0x1ace: v1ace(0x24) = ADD v1acd(0x0), v1ac5(0x24)
    0x1ad2: v1ad2 = EXTCODESIZE v1abd
    0x1ad3: v1ad3 = ISZERO v1ad2
    0x1ad5: v1ad5 = ISZERO v1ad3
    0x1ad6: v1ad6(0x1ade) = CONST 
    0x1ad9: JUMPI v1ad6(0x1ade), v1ad5
    0x340e: v340e(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 
    0x3413: v3413(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01) = CONST 

    Begin block 0x1ada
    prev=[0x1a23], succ=[]
    =================================
    0x1ada: v1ada(0x0) = CONST 
    0x1add: REVERT v1ada(0x0), v1ada(0x0)

    Begin block 0x1ade
    prev=[0x1a23], succ=[0x1ae9, 0x1af2]
    =================================
    0x1ae0: v1ae0 = GAS 
    0x1ae1: v1ae1 = STATICCALL v1ae0, v1abd, v1aa5, v1ace(0x24), v1aa5, v1a33(0x20)
    0x1ae2: v1ae2 = ISZERO v1ae1
    0x1ae4: v1ae4 = ISZERO v1ae2
    0x1ae5: v1ae5(0x1af2) = CONST 
    0x1ae8: JUMPI v1ae5(0x1af2), v1ae4

    Begin block 0x1ae9
    prev=[0x1ade], succ=[]
    =================================
    0x1ae9: v1ae9 = RETURNDATASIZE 
    0x1aea: v1aea(0x0) = CONST 
    0x1aed: RETURNDATACOPY v1aea(0x0), v1aea(0x0), v1ae9
    0x1aee: v1aee = RETURNDATASIZE 
    0x1aef: v1aef(0x0) = CONST 
    0x1af1: REVERT v1aef(0x0), v1aee

    Begin block 0x1af2
    prev=[0x1ade], succ=[0x1b04, 0x1b08]
    =================================
    0x1af7: v1af7(0x40) = CONST 
    0x1af9: v1af9 = MLOAD v1af7(0x40)
    0x1afa: v1afa = RETURNDATASIZE 
    0x1afb: v1afb(0x20) = CONST 
    0x1afe: v1afe = LT v1afa, v1afb(0x20)
    0x1aff: v1aff = ISZERO v1afe
    0x1b00: v1b00(0x1b08) = CONST 
    0x1b03: JUMPI v1b00(0x1b08), v1aff

    Begin block 0x1b04
    prev=[0x1af2], succ=[]
    =================================
    0x1b04: v1b04(0x0) = CONST 
    0x1b07: REVERT v1b04(0x0), v1b04(0x0)

    Begin block 0x1b08
    prev=[0x1af2], succ=[0x1bc2, 0x1bc6]
    =================================
    0x1b0a: v1b0a = MLOAD v1af9
    0x1b0b: v1b0b(0x1) = CONST 
    0x1b0d: v1b0d(0x1) = CONST 
    0x1b0f: v1b0f(0xa0) = CONST 
    0x1b11: v1b11(0x10000000000000000000000000000000000000000) = SHL v1b0f(0xa0), v1b0d(0x1)
    0x1b12: v1b12(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1b11(0x10000000000000000000000000000000000000000), v1b0b(0x1)
    0x1b15: v1b15 = AND v1b12(0xffffffffffffffffffffffffffffffffffffffff), v1b0a
    0x1b17: MSTORE v1a41(0x0), v1b15
    0x1b18: v1b18(0x20) = CONST 
    0x1b1c: v1b1c(0x20) = ADD v1a41(0x0), v1b18(0x20)
    0x1b20: MSTORE v1b1c(0x20), v3413(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01)
    0x1b21: v1b21(0x40) = CONST 
    0x1b25: v1b25(0x40) = ADD v1b21(0x40), v1a41(0x0)
    0x1b26: v1b26(0x0) = CONST 
    0x1b2a: v1b2a = SHA3 v1b26(0x0), v1b25(0x40)
    0x1b2c: v1b2c = SLOAD v1b2a
    0x1b2d: v1b2d(0xff) = CONST 
    0x1b2f: v1b2f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1b2d(0xff)
    0x1b30: v1b30 = AND v1b2f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1b2c
    0x1b31: v1b31(0xff) = CONST 
    0x1b36: v1b36(0x3) = AND v1b31(0xff), v1a6a(0x3)
    0x1b3a: v1b3a = OR v1b36(0x3), v1b30
    0x1b3d: SSTORE v1b2a, v1b3a
    0x1b3e: v1b3e(0x0) = CONST 
    0x1b41: v1b41 = MLOAD v1b3e(0x0)
    0x1b42: v1b42(0x20) = CONST 
    0x1b44: v1b44(0x23e9) = CONST 
    0x1b4c: MSTORE v1b3e(0x0), v1b41
    0x1b4e: MSTORE v1b26(0x0), v3418(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x1b4f: v1b4f(0x3) = CONST 
    0x1b52: MSTORE v1b18(0x20), v1b4f(0x3)
    0x1b53: v1b53(0x2) = CONST 
    0x1b55: v1b55 = SLOAD v1b53(0x2)
    0x1b57: v1b57 = MLOAD v1b21(0x40)
    0x1b58: v1b58(0x2ecd14d3) = CONST 
    0x1b5d: v1b5d(0xe2) = CONST 
    0x1b5f: v1b5f(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1b5d(0xe2), v1b58(0x2ecd14d3)
    0x1b61: MSTORE v1b57, v1b5f(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1b62: v1b62(0x434f4e54524143545f4c505f464952455f45524332305f544f4b454e00000000) = CONST 
    0x1b83: v1b83(0x4) = CONST 
    0x1b87: v1b87 = ADD v1b57, v1b83(0x4)
    0x1b8b: MSTORE v1b87, v1b62(0x434f4e54524143545f4c505f464952455f45524332305f544f4b454e00000000)
    0x1b8d: v1b8d = MLOAD v1b21(0x40)
    0x1b90: v1b90(0x0) = CONST 
    0x1b93: v1b93 = MLOAD v1b90(0x0)
    0x1b94: v1b94(0x20) = CONST 
    0x1b96: v1b96(0x23c9) = CONST 
    0x1b9e: MSTORE v1b90(0x0), v1b93
    0x1ba5: v1ba5 = AND v1b12(0xffffffffffffffffffffffffffffffffffffffff), v1b55
    0x1ba7: v1ba7(0xbb34534c) = CONST 
    0x1bad: v1bad(0x24) = CONST 
    0x1bb1: v1bb1 = ADD v1b57, v1bad(0x24)
    0x1bb5: v1bb5(0x0) = SUB v1b57, v1b8d
    0x1bb6: v1bb6(0x24) = ADD v1bb5(0x0), v1bad(0x24)
    0x1bba: v1bba = EXTCODESIZE v1ba5
    0x1bbb: v1bbb = ISZERO v1bba
    0x1bbd: v1bbd = ISZERO v1bbb
    0x1bbe: v1bbe(0x1bc6) = CONST 
    0x1bc1: JUMPI v1bbe(0x1bc6), v1bbd
    0x3418: v3418(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 
    0x341d: v341d(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01) = CONST 

    Begin block 0x1bc2
    prev=[0x1b08], succ=[]
    =================================
    0x1bc2: v1bc2(0x0) = CONST 
    0x1bc5: REVERT v1bc2(0x0), v1bc2(0x0)

    Begin block 0x1bc6
    prev=[0x1b08], succ=[0x1bd1, 0x1bda]
    =================================
    0x1bc8: v1bc8 = GAS 
    0x1bc9: v1bc9 = STATICCALL v1bc8, v1ba5, v1b8d, v1bb6(0x24), v1b8d, v1b18(0x20)
    0x1bca: v1bca = ISZERO v1bc9
    0x1bcc: v1bcc = ISZERO v1bca
    0x1bcd: v1bcd(0x1bda) = CONST 
    0x1bd0: JUMPI v1bcd(0x1bda), v1bcc

    Begin block 0x1bd1
    prev=[0x1bc6], succ=[]
    =================================
    0x1bd1: v1bd1 = RETURNDATASIZE 
    0x1bd2: v1bd2(0x0) = CONST 
    0x1bd5: RETURNDATACOPY v1bd2(0x0), v1bd2(0x0), v1bd1
    0x1bd6: v1bd6 = RETURNDATASIZE 
    0x1bd7: v1bd7(0x0) = CONST 
    0x1bd9: REVERT v1bd7(0x0), v1bd6

    Begin block 0x1bda
    prev=[0x1bc6], succ=[0x1bec, 0x1bf0]
    =================================
    0x1bdf: v1bdf(0x40) = CONST 
    0x1be1: v1be1 = MLOAD v1bdf(0x40)
    0x1be2: v1be2 = RETURNDATASIZE 
    0x1be3: v1be3(0x20) = CONST 
    0x1be6: v1be6 = LT v1be2, v1be3(0x20)
    0x1be7: v1be7 = ISZERO v1be6
    0x1be8: v1be8(0x1bf0) = CONST 
    0x1beb: JUMPI v1be8(0x1bf0), v1be7

    Begin block 0x1bec
    prev=[0x1bda], succ=[]
    =================================
    0x1bec: v1bec(0x0) = CONST 
    0x1bef: REVERT v1bec(0x0), v1bec(0x0)

    Begin block 0x1bf0
    prev=[0x1bda], succ=[0x1ca8, 0x1cac]
    =================================
    0x1bf2: v1bf2 = MLOAD v1be1
    0x1bf3: v1bf3(0x1) = CONST 
    0x1bf5: v1bf5(0x1) = CONST 
    0x1bf7: v1bf7(0xa0) = CONST 
    0x1bf9: v1bf9(0x10000000000000000000000000000000000000000) = SHL v1bf7(0xa0), v1bf5(0x1)
    0x1bfa: v1bfa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1bf9(0x10000000000000000000000000000000000000000), v1bf3(0x1)
    0x1bfd: v1bfd = AND v1bfa(0xffffffffffffffffffffffffffffffffffffffff), v1bf2
    0x1bff: MSTORE v1b26(0x0), v1bfd
    0x1c00: v1c00(0x20) = CONST 
    0x1c04: v1c04(0x20) = ADD v1b26(0x0), v1c00(0x20)
    0x1c08: MSTORE v1c04(0x20), v341d(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01)
    0x1c09: v1c09(0x40) = CONST 
    0x1c0d: v1c0d(0x40) = ADD v1c09(0x40), v1b26(0x0)
    0x1c0e: v1c0e(0x0) = CONST 
    0x1c12: v1c12 = SHA3 v1c0e(0x0), v1c0d(0x40)
    0x1c14: v1c14 = SLOAD v1c12
    0x1c15: v1c15(0xff) = CONST 
    0x1c17: v1c17(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1c15(0xff)
    0x1c18: v1c18 = AND v1c17(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1c14
    0x1c19: v1c19(0xff) = CONST 
    0x1c1e: v1c1e(0x4) = AND v1c19(0xff), v1b83(0x4)
    0x1c22: v1c22 = OR v1c1e(0x4), v1c18
    0x1c25: SSTORE v1c12, v1c22
    0x1c26: v1c26(0x0) = CONST 
    0x1c29: v1c29 = MLOAD v1c26(0x0)
    0x1c2a: v1c2a(0x20) = CONST 
    0x1c2c: v1c2c(0x23e9) = CONST 
    0x1c34: MSTORE v1c26(0x0), v1c29
    0x1c36: MSTORE v1c0e(0x0), v3422(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000)
    0x1c37: v1c37(0x3) = CONST 
    0x1c3a: MSTORE v1c00(0x20), v1c37(0x3)
    0x1c3b: v1c3b(0x2) = CONST 
    0x1c3d: v1c3d = SLOAD v1c3b(0x2)
    0x1c3f: v1c3f = MLOAD v1c09(0x40)
    0x1c40: v1c40(0x2ecd14d3) = CONST 
    0x1c45: v1c45(0xe2) = CONST 
    0x1c47: v1c47(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1c45(0xe2), v1c40(0x2ecd14d3)
    0x1c49: MSTORE v1c3f, v1c47(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1c4a: v1c4a(0x434f4e54524143545f4c505f534f494c5f45524332305f544f4b454e00000000) = CONST 
    0x1c6b: v1c6b(0x4) = CONST 
    0x1c6e: v1c6e = ADD v1c3f, v1c6b(0x4)
    0x1c6f: MSTORE v1c6e, v1c4a(0x434f4e54524143545f4c505f534f494c5f45524332305f544f4b454e00000000)
    0x1c71: v1c71 = MLOAD v1c09(0x40)
    0x1c72: v1c72(0x5) = CONST 
    0x1c75: v1c75(0x0) = CONST 
    0x1c78: v1c78 = MLOAD v1c75(0x0)
    0x1c79: v1c79(0x20) = CONST 
    0x1c7b: v1c7b(0x23c9) = CONST 
    0x1c83: MSTORE v1c75(0x0), v1c78
    0x1c8a: v1c8a = AND v1bfa(0xffffffffffffffffffffffffffffffffffffffff), v1c3d
    0x1c8c: v1c8c(0xbb34534c) = CONST 
    0x1c92: v1c92(0x24) = CONST 
    0x1c96: v1c96 = ADD v1c3f, v1c92(0x24)
    0x1c9b: v1c9b(0x0) = SUB v1c3f, v1c71
    0x1c9c: v1c9c(0x24) = ADD v1c9b(0x0), v1c92(0x24)
    0x1ca0: v1ca0 = EXTCODESIZE v1c8a
    0x1ca1: v1ca1 = ISZERO v1ca0
    0x1ca3: v1ca3 = ISZERO v1ca1
    0x1ca4: v1ca4(0x1cac) = CONST 
    0x1ca7: JUMPI v1ca4(0x1cac), v1ca3
    0x3422: v3422(0x434f4e54524143545f4c505f454c454d454e545f544f4b454e00000000000000) = CONST 
    0x3427: v3427(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01) = CONST 

    Begin block 0x1ca8
    prev=[0x1bf0], succ=[]
    =================================
    0x1ca8: v1ca8(0x0) = CONST 
    0x1cab: REVERT v1ca8(0x0), v1ca8(0x0)

    Begin block 0x1cac
    prev=[0x1bf0], succ=[0x1cb7, 0x1cc0]
    =================================
    0x1cae: v1cae = GAS 
    0x1caf: v1caf = STATICCALL v1cae, v1c8a, v1c71, v1c9c(0x24), v1c71, v1c00(0x20)
    0x1cb0: v1cb0 = ISZERO v1caf
    0x1cb2: v1cb2 = ISZERO v1cb0
    0x1cb3: v1cb3(0x1cc0) = CONST 
    0x1cb6: JUMPI v1cb3(0x1cc0), v1cb2

    Begin block 0x1cb7
    prev=[0x1cac], succ=[]
    =================================
    0x1cb7: v1cb7 = RETURNDATASIZE 
    0x1cb8: v1cb8(0x0) = CONST 
    0x1cbb: RETURNDATACOPY v1cb8(0x0), v1cb8(0x0), v1cb7
    0x1cbc: v1cbc = RETURNDATASIZE 
    0x1cbd: v1cbd(0x0) = CONST 
    0x1cbf: REVERT v1cbd(0x0), v1cbc

    Begin block 0x1cc0
    prev=[0x1cac], succ=[0x1cd2, 0x1cd6]
    =================================
    0x1cc5: v1cc5(0x40) = CONST 
    0x1cc7: v1cc7 = MLOAD v1cc5(0x40)
    0x1cc8: v1cc8 = RETURNDATASIZE 
    0x1cc9: v1cc9(0x20) = CONST 
    0x1ccc: v1ccc = LT v1cc8, v1cc9(0x20)
    0x1ccd: v1ccd = ISZERO v1ccc
    0x1cce: v1cce(0x1cd6) = CONST 
    0x1cd1: JUMPI v1cce(0x1cd6), v1ccd

    Begin block 0x1cd2
    prev=[0x1cc0], succ=[]
    =================================
    0x1cd2: v1cd2(0x0) = CONST 
    0x1cd5: REVERT v1cd2(0x0), v1cd2(0x0)

    Begin block 0x1cd6
    prev=[0x1cc0], succ=[0x1d0a, 0x1d15]
    =================================
    0x1cd8: v1cd8 = MLOAD v1cc7
    0x1cd9: v1cd9(0x1) = CONST 
    0x1cdb: v1cdb(0x1) = CONST 
    0x1cdd: v1cdd(0xa0) = CONST 
    0x1cdf: v1cdf(0x10000000000000000000000000000000000000000) = SHL v1cdd(0xa0), v1cdb(0x1)
    0x1ce0: v1ce0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1cdf(0x10000000000000000000000000000000000000000), v1cd9(0x1)
    0x1ce1: v1ce1 = AND v1ce0(0xffffffffffffffffffffffffffffffffffffffff), v1cd8
    0x1ce3: MSTORE v1c0e(0x0), v1ce1
    0x1ce4: v1ce4(0x20) = CONST 
    0x1ce7: v1ce7(0x20) = ADD v1c0e(0x0), v1ce4(0x20)
    0x1ceb: MSTORE v1ce7(0x20), v3427(0x60255b8336c17e13e8fe52140e54aa919e7e1180fbd9cce43d47bfecd2649c01)
    0x1cec: v1cec(0x40) = CONST 
    0x1cee: v1cee(0x40) = ADD v1cec(0x40), v1c0e(0x0)
    0x1cef: v1cef(0x0) = CONST 
    0x1cf1: v1cf1 = SHA3 v1cef(0x0), v1cee(0x40)
    0x1cf3: v1cf3 = SLOAD v1cf1
    0x1cf4: v1cf4(0xff) = CONST 
    0x1cf6: v1cf6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00) = NOT v1cf4(0xff)
    0x1cf7: v1cf7 = AND v1cf6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00), v1cf3
    0x1cf8: v1cf8(0xff) = CONST 
    0x1cfd: v1cfd(0x5) = AND v1cf8(0xff), v1c72(0x5)
    0x1d01: v1d01 = OR v1cfd(0x5), v1cf7
    0x1d03: SSTORE v1cf1, v1d01
    0x1d05: v1d05 = ISZERO v180f
    0x1d06: v1d06(0x1d15) = CONST 
    0x1d09: JUMPI v1d06(0x1d15), v1d05

    Begin block 0x1d0a
    prev=[0x1cd6], succ=[0x1d15]
    =================================
    0x1d0a: v1d0a(0x0) = CONST 
    0x1d0d: v1d0d = SLOAD v1d0a(0x0)
    0x1d0e: v1d0e(0xff00) = CONST 
    0x1d11: v1d11(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff) = NOT v1d0e(0xff00)
    0x1d12: v1d12 = AND v1d11(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00ff), v1d0d
    0x1d14: SSTORE v1d0a(0x0), v1d12

    Begin block 0x1d15
    prev=[0x1d0a, 0x1cd6], succ=[0x308d]
    =================================
    0x1d18: JUMP v78a(0x308d)

    Begin block 0x308d
    prev=[0x1d15], succ=[]
    =================================
    0x308e: STOP 

    Begin block 0x17c0
    prev=[0x17ba], succ=[0x17c8]
    =================================
    0x17c1: v17c1(0x0) = CONST 
    0x17c3: v17c3 = SLOAD v17c1(0x0)
    0x17c4: v17c4(0xff) = CONST 
    0x17c6: v17c6 = AND v17c4(0xff), v17c3
    0x17c7: v17c7 = ISZERO v17c6

    Begin block 0x17b2
    prev=[0x17a1], succ=[0x2394]
    =================================
    0x17b3: v17b3(0x17ba) = CONST 
    0x17b6: v17b6(0x2394) = CONST 
    0x17b9: JUMP v17b6(0x2394)

    Begin block 0x2394
    prev=[0x17b2], succ=[0x17ba]
    =================================
    0x2395: v2395 = ADDRESS 
    0x2396: v2396 = EXTCODESIZE v2395
    0x2397: v2397 = ISZERO v2396
    0x2399: JUMP v17b3(0x17ba)

}

function getExternalObjectClassExt(address)() public {
    Begin block 0x7af
    prev=[], succ=[0x7c1, 0x7c5]
    =================================
    0x7b0: v7b0(0x30ae) = CONST 
    0x7b3: v7b3(0x4) = CONST 
    0x7b6: v7b6 = CALLDATASIZE 
    0x7b7: v7b7 = SUB v7b6, v7b3(0x4)
    0x7b8: v7b8(0x20) = CONST 
    0x7bb: v7bb = LT v7b7, v7b8(0x20)
    0x7bc: v7bc = ISZERO v7bb
    0x7bd: v7bd(0x7c5) = CONST 
    0x7c0: JUMPI v7bd(0x7c5), v7bc

    Begin block 0x7c1
    prev=[0x7af], succ=[]
    =================================
    0x7c1: v7c1(0x0) = CONST 
    0x7c4: REVERT v7c1(0x0), v7c1(0x0)

    Begin block 0x7c5
    prev=[0x7af], succ=[0x1d190x7af]
    =================================
    0x7c7: v7c7 = CALLDATALOAD v7b3(0x4)
    0x7c8: v7c8(0x1) = CONST 
    0x7ca: v7ca(0x1) = CONST 
    0x7cc: v7cc(0xa0) = CONST 
    0x7ce: v7ce(0x10000000000000000000000000000000000000000) = SHL v7cc(0xa0), v7ca(0x1)
    0x7cf: v7cf(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7ce(0x10000000000000000000000000000000000000000), v7c8(0x1)
    0x7d0: v7d0 = AND v7cf(0xffffffffffffffffffffffffffffffffffffffff), v7c7
    0x7d1: v7d1(0x1d19) = CONST 
    0x7d4: JUMP v7d1(0x1d19)

    Begin block 0x1d190x7af
    prev=[0x7c5], succ=[0x1d3b0x7af, 0x1d7e0x7af]
    =================================
    0x1d1a0x7af: v7af1d1a(0x1) = CONST 
    0x1d1c0x7af: v7af1d1c(0x1) = CONST 
    0x1d1e0x7af: v7af1d1e(0xa0) = CONST 
    0x1d200x7af: v7af1d20(0x10000000000000000000000000000000000000000) = SHL v7af1d1e(0xa0), v7af1d1c(0x1)
    0x1d210x7af: v7af1d21(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7af1d20(0x10000000000000000000000000000000000000000), v7af1d1a(0x1)
    0x1d230x7af: v7af1d23 = AND v7d0, v7af1d21(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d240x7af: v7af1d24(0x0) = CONST 
    0x1d280x7af: MSTORE v7af1d24(0x0), v7af1d23
    0x1d290x7af: v7af1d29(0x4) = CONST 
    0x1d2b0x7af: v7af1d2b(0x20) = CONST 
    0x1d2d0x7af: MSTORE v7af1d2b(0x20), v7af1d29(0x4)
    0x1d2e0x7af: v7af1d2e(0x40) = CONST 
    0x1d310x7af: v7af1d31 = SHA3 v7af1d24(0x0), v7af1d2e(0x40)
    0x1d320x7af: v7af1d32 = SLOAD v7af1d31
    0x1d330x7af: v7af1d33(0xffff) = CONST 
    0x1d360x7af: v7af1d36 = AND v7af1d33(0xffff), v7af1d32
    0x1d370x7af: v7af1d37(0x1d7e) = CONST 
    0x1d3a0x7af: JUMPI v7af1d37(0x1d7e), v7af1d36

    Begin block 0x1d3b0x7af
    prev=[0x1d190x7af], succ=[]
    =================================
    0x1d3b0x7af: v7af1d3b(0x40) = CONST 
    0x1d3e0x7af: v7af1d3e = MLOAD v7af1d3b(0x40)
    0x1d3f0x7af: v7af1d3f(0x461bcd) = CONST 
    0x1d430x7af: v7af1d43(0xe5) = CONST 
    0x1d450x7af: v7af1d45(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7af1d43(0xe5), v7af1d3f(0x461bcd)
    0x1d470x7af: MSTORE v7af1d3e, v7af1d45(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d480x7af: v7af1d48(0x20) = CONST 
    0x1d4a0x7af: v7af1d4a(0x4) = CONST 
    0x1d4d0x7af: v7af1d4d = ADD v7af1d3e, v7af1d4a(0x4)
    0x1d4e0x7af: MSTORE v7af1d4d, v7af1d48(0x20)
    0x1d4f0x7af: v7af1d4f(0x14) = CONST 
    0x1d510x7af: v7af1d51(0x24) = CONST 
    0x1d540x7af: v7af1d54 = ADD v7af1d3e, v7af1d51(0x24)
    0x1d550x7af: MSTORE v7af1d54, v7af1d4f(0x14)
    0x1d560x7af: v7af1d56(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0x1d6b0x7af: v7af1d6b(0x62) = CONST 
    0x1d6d0x7af: v7af1d6d(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL v7af1d6b(0x62), v7af1d56(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0x1d6e0x7af: v7af1d6e(0x44) = CONST 
    0x1d710x7af: v7af1d71 = ADD v7af1d3e, v7af1d6e(0x44)
    0x1d720x7af: MSTORE v7af1d71, v7af1d6d(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0x1d740x7af: v7af1d74 = MLOAD v7af1d3b(0x40)
    0x1d780x7af: v7af1d78(0x0) = SUB v7af1d3e, v7af1d74
    0x1d790x7af: v7af1d79(0x64) = CONST 
    0x1d7b0x7af: v7af1d7b(0x64) = ADD v7af1d79(0x64), v7af1d78(0x0)
    0x1d7d0x7af: REVERT v7af1d74, v7af1d7b(0x64)

    Begin block 0x1d7e0x7af
    prev=[0x1d190x7af], succ=[0x30ae]
    =================================
    0x1d800x7af: v7af1d80(0x1) = CONST 
    0x1d820x7af: v7af1d82(0x1) = CONST 
    0x1d840x7af: v7af1d84(0xa0) = CONST 
    0x1d860x7af: v7af1d86(0x10000000000000000000000000000000000000000) = SHL v7af1d84(0xa0), v7af1d82(0x1)
    0x1d870x7af: v7af1d87(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7af1d86(0x10000000000000000000000000000000000000000), v7af1d80(0x1)
    0x1d880x7af: v7af1d88 = AND v7af1d87(0xffffffffffffffffffffffffffffffffffffffff), v7d0
    0x1d890x7af: v7af1d89(0x0) = CONST 
    0x1d8d0x7af: MSTORE v7af1d89(0x0), v7af1d88
    0x1d8e0x7af: v7af1d8e(0x4) = CONST 
    0x1d900x7af: v7af1d90(0x20) = CONST 
    0x1d920x7af: MSTORE v7af1d90(0x20), v7af1d8e(0x4)
    0x1d930x7af: v7af1d93(0x40) = CONST 
    0x1d960x7af: v7af1d96 = SHA3 v7af1d89(0x0), v7af1d93(0x40)
    0x1d970x7af: v7af1d97 = SLOAD v7af1d96
    0x1d980x7af: v7af1d98(0xffff) = CONST 
    0x1d9b0x7af: v7af1d9b = AND v7af1d98(0xffff), v7af1d97
    0x1d9d0x7af: JUMP v7b0(0x30ae)

    Begin block 0x30ae
    prev=[0x1d7e0x7af], succ=[]
    =================================
    0x30af: v30af(0x40) = CONST 
    0x30b2: v30b2 = MLOAD v30af(0x40)
    0x30b3: v30b3(0xffff) = CONST 
    0x30b8: v30b8 = AND v7af1d9b, v30b3(0xffff)
    0x30ba: MSTORE v30b2, v30b8
    0x30bb: v30bb = MLOAD v30af(0x40)
    0x30bf: v30bf(0x0) = SUB v30b2, v30bb
    0x30c0: v30c0(0x20) = CONST 
    0x30c2: v30c2(0x20) = ADD v30c0(0x20), v30bf(0x0)
    0x30c4: RETURN v30bb, v30c2(0x20)

}

function addExternalTokenMeta(address,uint16,uint16,uint256)() public {
    Begin block 0x7d5
    prev=[], succ=[0x7e7, 0x7eb]
    =================================
    0x7d6: v7d6(0x30e4) = CONST 
    0x7d9: v7d9(0x4) = CONST 
    0x7dc: v7dc = CALLDATASIZE 
    0x7dd: v7dd = SUB v7dc, v7d9(0x4)
    0x7de: v7de(0x80) = CONST 
    0x7e1: v7e1 = LT v7dd, v7de(0x80)
    0x7e2: v7e2 = ISZERO v7e1
    0x7e3: v7e3(0x7eb) = CONST 
    0x7e6: JUMPI v7e3(0x7eb), v7e2

    Begin block 0x7e7
    prev=[0x7d5], succ=[]
    =================================
    0x7e7: v7e7(0x0) = CONST 
    0x7ea: REVERT v7e7(0x0), v7e7(0x0)

    Begin block 0x7eb
    prev=[0x7d5], succ=[0x1d9e]
    =================================
    0x7ed: v7ed(0x1) = CONST 
    0x7ef: v7ef(0x1) = CONST 
    0x7f1: v7f1(0xa0) = CONST 
    0x7f3: v7f3(0x10000000000000000000000000000000000000000) = SHL v7f1(0xa0), v7ef(0x1)
    0x7f4: v7f4(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7f3(0x10000000000000000000000000000000000000000), v7ed(0x1)
    0x7f6: v7f6 = CALLDATALOAD v7d9(0x4)
    0x7f7: v7f7 = AND v7f6, v7f4(0xffffffffffffffffffffffffffffffffffffffff)
    0x7f9: v7f9(0xffff) = CONST 
    0x7fc: v7fc(0x20) = CONST 
    0x7ff: v7ff(0x24) = ADD v7d9(0x4), v7fc(0x20)
    0x800: v800 = CALLDATALOAD v7ff(0x24)
    0x802: v802 = AND v7f9(0xffff), v800
    0x804: v804(0x40) = CONST 
    0x807: v807(0x44) = ADD v7d9(0x4), v804(0x40)
    0x808: v808 = CALLDATALOAD v807(0x44)
    0x80b: v80b = AND v7f9(0xffff), v808
    0x80d: v80d(0x60) = CONST 
    0x80f: v80f(0x64) = ADD v80d(0x60), v7d9(0x4)
    0x810: v810 = CALLDATALOAD v80f(0x64)
    0x811: v811(0x1d9e) = CONST 
    0x814: JUMP v811(0x1d9e)

    Begin block 0x1d9e
    prev=[0x7eb], succ=[0x1db4]
    =================================
    0x1d9f: v1d9f(0x1db4) = CONST 
    0x1da2: v1da2 = CALLER 
    0x1da3: v1da3(0x0) = CONST 
    0x1da5: v1da5 = CALLDATALOAD v1da3(0x0)
    0x1da6: v1da6(0x1) = CONST 
    0x1da8: v1da8(0x1) = CONST 
    0x1daa: v1daa(0xe0) = CONST 
    0x1dac: v1dac(0x100000000000000000000000000000000000000000000000000000000) = SHL v1daa(0xe0), v1da8(0x1)
    0x1dad: v1dad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v1dac(0x100000000000000000000000000000000000000000000000000000000), v1da6(0x1)
    0x1dae: v1dae(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v1dad(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x1daf: v1daf = AND v1dae(0xffffffff00000000000000000000000000000000000000000000000000000000), v1da5
    0x1db0: v1db0(0x22d3) = CONST 
    0x1db3: v1db3_0 = CALLPRIVATE v1db0(0x22d3), v1daf, v1da2, v1d9f(0x1db4)

    Begin block 0x1db4
    prev=[0x1d9e], succ=[0x1db9, 0x1df3]
    =================================
    0x1db5: v1db5(0x1df3) = CONST 
    0x1db8: JUMPI v1db5(0x1df3), v1db3_0

    Begin block 0x1db9
    prev=[0x1db4], succ=[]
    =================================
    0x1db9: v1db9(0x40) = CONST 
    0x1dbc: v1dbc = MLOAD v1db9(0x40)
    0x1dbd: v1dbd(0x461bcd) = CONST 
    0x1dc1: v1dc1(0xe5) = CONST 
    0x1dc3: v1dc3(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1dc1(0xe5), v1dbd(0x461bcd)
    0x1dc5: MSTORE v1dbc, v1dc3(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1dc6: v1dc6(0x20) = CONST 
    0x1dc8: v1dc8(0x4) = CONST 
    0x1dcb: v1dcb = ADD v1dbc, v1dc8(0x4)
    0x1dcc: MSTORE v1dcb, v1dc6(0x20)
    0x1dcd: v1dcd(0x14) = CONST 
    0x1dcf: v1dcf(0x24) = CONST 
    0x1dd2: v1dd2 = ADD v1dbc, v1dcf(0x24)
    0x1dd3: MSTORE v1dd2, v1dcd(0x14)
    0x1dd4: v1dd4(0x0) = CONST 
    0x1dd7: v1dd7 = MLOAD v1dd4(0x0)
    0x1dd8: v1dd8(0x20) = CONST 
    0x1dda: v1dda(0x2409) = CONST 
    0x1de2: MSTORE v1dd4(0x0), v1dd7
    0x1de3: v1de3(0x44) = CONST 
    0x1de6: v1de6 = ADD v1dbc, v1de3(0x44)
    0x1de7: MSTORE v1de6, v342c(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x1de9: v1de9 = MLOAD v1db9(0x40)
    0x1ded: v1ded(0x0) = SUB v1dbc, v1de9
    0x1dee: v1dee(0x64) = CONST 
    0x1df0: v1df0(0x64) = ADD v1dee(0x64), v1ded(0x0)
    0x1df2: REVERT v1de9, v1df0(0x64)
    0x342c: v342c(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x1df3
    prev=[0x1db4], succ=[0x1e00, 0x1e4c]
    =================================
    0x1df4: v1df4(0x0) = CONST 
    0x1df7: v1df7(0xffff) = CONST 
    0x1dfa: v1dfa = AND v1df7(0xffff), v802
    0x1dfb: v1dfb = GT v1dfa, v1df4(0x0)
    0x1dfc: v1dfc(0x1e4c) = CONST 
    0x1dff: JUMPI v1dfc(0x1e4c), v1dfb

    Begin block 0x1e00
    prev=[0x1df3], succ=[]
    =================================
    0x1e00: v1e00(0x40) = CONST 
    0x1e03: v1e03 = MLOAD v1e00(0x40)
    0x1e04: v1e04(0x461bcd) = CONST 
    0x1e08: v1e08(0xe5) = CONST 
    0x1e0a: v1e0a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v1e08(0xe5), v1e04(0x461bcd)
    0x1e0c: MSTORE v1e03, v1e0a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1e0d: v1e0d(0x20) = CONST 
    0x1e0f: v1e0f(0x4) = CONST 
    0x1e12: v1e12 = ADD v1e03, v1e0f(0x4)
    0x1e13: MSTORE v1e12, v1e0d(0x20)
    0x1e14: v1e14(0x1c) = CONST 
    0x1e16: v1e16(0x24) = CONST 
    0x1e19: v1e19 = ADD v1e03, v1e16(0x24)
    0x1e1a: MSTORE v1e19, v1e14(0x1c)
    0x1e1b: v1e1b(0x4675726e6163653a20494e56414c49445f4f424a434c41535345585400000000) = CONST 
    0x1e3c: v1e3c(0x44) = CONST 
    0x1e3f: v1e3f = ADD v1e03, v1e3c(0x44)
    0x1e40: MSTORE v1e3f, v1e1b(0x4675726e6163653a20494e56414c49445f4f424a434c41535345585400000000)
    0x1e42: v1e42 = MLOAD v1e00(0x40)
    0x1e46: v1e46(0x0) = SUB v1e03, v1e42
    0x1e47: v1e47(0x64) = CONST 
    0x1e49: v1e49(0x64) = ADD v1e47(0x64), v1e46(0x0)
    0x1e4b: REVERT v1e42, v1e49(0x64)

    Begin block 0x1e4c
    prev=[0x1df3], succ=[0x30e4]
    =================================
    0x1e4d: v1e4d(0x1) = CONST 
    0x1e4f: v1e4f(0x1) = CONST 
    0x1e51: v1e51(0xa0) = CONST 
    0x1e53: v1e53(0x10000000000000000000000000000000000000000) = SHL v1e51(0xa0), v1e4f(0x1)
    0x1e54: v1e54(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e53(0x10000000000000000000000000000000000000000), v1e4d(0x1)
    0x1e56: v1e56 = AND v7f7, v1e54(0xffffffffffffffffffffffffffffffffffffffff)
    0x1e57: v1e57(0x0) = CONST 
    0x1e5b: MSTORE v1e57(0x0), v1e56
    0x1e5c: v1e5c(0x4) = CONST 
    0x1e5e: v1e5e(0x20) = CONST 
    0x1e62: MSTORE v1e5e(0x20), v1e5c(0x4)
    0x1e63: v1e63(0x40) = CONST 
    0x1e67: v1e67 = SHA3 v1e57(0x0), v1e63(0x40)
    0x1e69: v1e69 = SLOAD v1e67
    0x1e6a: v1e6a(0xffff) = CONST 
    0x1e6f: v1e6f = AND v802, v1e6a(0xffff)
    0x1e70: v1e70(0xffff) = CONST 
    0x1e73: v1e73(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000) = NOT v1e70(0xffff)
    0x1e76: v1e76 = AND v1e69, v1e73(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000)
    0x1e78: v1e78 = OR v1e6f, v1e76
    0x1e7a: SSTORE v1e67, v1e78
    0x1e7c: v1e7c = AND v80b, v1e6a(0xffff)
    0x1e7f: MSTORE v1e57(0x0), v1e7c
    0x1e80: v1e80(0x1) = CONST 
    0x1e84: v1e84 = ADD v1e67, v1e80(0x1)
    0x1e86: MSTORE v1e5e(0x20), v1e84
    0x1e8a: v1e8a = SHA3 v1e57(0x0), v1e63(0x40)
    0x1e8d: SSTORE v1e8a, v810
    0x1e8f: v1e8f = MLOAD v1e63(0x40)
    0x1e92: MSTORE v1e8f, v1e6f
    0x1e95: v1e95 = ADD v1e8f, v1e5e(0x20)
    0x1e99: MSTORE v1e95, v1e7c
    0x1e9c: v1e9c = ADD v1e63(0x40), v1e8f
    0x1e9f: MSTORE v1e9c, v810
    0x1ea0: v1ea0 = MLOAD v1e63(0x40)
    0x1ea1: v1ea1(0xcabffb94c7e376e4e5646720b0f0f101bb0608b93a8c21f186ea49b081c6bf9) = CONST 
    0x1ec5: v1ec5(0x0) = SUB v1e8f, v1ea0
    0x1ec6: v1ec6(0x60) = CONST 
    0x1ec8: v1ec8(0x60) = ADD v1ec6(0x60), v1ec5(0x0)
    0x1eca: LOG2 v1ea0, v1ec8(0x60), v1ea1(0xcabffb94c7e376e4e5646720b0f0f101bb0608b93a8c21f186ea49b081c6bf9), v1e56
    0x1ecf: JUMP v7d6(0x30e4)

    Begin block 0x30e4
    prev=[0x1e4c], succ=[]
    =================================
    0x30e5: STOP 

}

function CONTRACT_LP_WATER_ERC20_TOKEN()() public {
    Begin block 0x815
    prev=[], succ=[0x1ed0]
    =================================
    0x816: v816(0x3105) = CONST 
    0x819: v819(0x1ed0) = CONST 
    0x81c: JUMP v819(0x1ed0)

    Begin block 0x1ed0
    prev=[0x815], succ=[0x3105]
    =================================
    0x1ed1: v1ed1(0x434f4e54524143545f4c505f57415445525f45524332305f544f4b454e000000) = CONST 
    0x1ef3: JUMP v816(0x3105)

    Begin block 0x3105
    prev=[0x1ed0], succ=[]
    =================================
    0x3106: v3106(0x40) = CONST 
    0x3109: v3109 = MLOAD v3106(0x40)
    0x310c: MSTORE v3109, v1ed1(0x434f4e54524143545f4c505f57415445525f45524332305f544f4b454e000000)
    0x310d: v310d = MLOAD v3106(0x40)
    0x3111: v3111(0x0) = SUB v3109, v310d
    0x3112: v3112(0x20) = CONST 
    0x3114: v3114(0x20) = ADD v3112(0x20), v3111(0x0)
    0x3116: RETURN v310d, v3114(0x20)

}

function getMetaData(address,uint256)() public {
    Begin block 0x81d
    prev=[], succ=[0x82f, 0x833]
    =================================
    0x81e: v81e(0x849) = CONST 
    0x821: v821(0x4) = CONST 
    0x824: v824 = CALLDATASIZE 
    0x825: v825 = SUB v824, v821(0x4)
    0x826: v826(0x40) = CONST 
    0x829: v829 = LT v825, v826(0x40)
    0x82a: v82a = ISZERO v829
    0x82b: v82b(0x833) = CONST 
    0x82e: JUMPI v82b(0x833), v82a

    Begin block 0x82f
    prev=[0x81d], succ=[]
    =================================
    0x82f: v82f(0x0) = CONST 
    0x832: REVERT v82f(0x0), v82f(0x0)

    Begin block 0x833
    prev=[0x81d], succ=[0x1ef4]
    =================================
    0x835: v835(0x1) = CONST 
    0x837: v837(0x1) = CONST 
    0x839: v839(0xa0) = CONST 
    0x83b: v83b(0x10000000000000000000000000000000000000000) = SHL v839(0xa0), v837(0x1)
    0x83c: v83c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v83b(0x10000000000000000000000000000000000000000), v835(0x1)
    0x83e: v83e = CALLDATALOAD v821(0x4)
    0x83f: v83f = AND v83e, v83c(0xffffffffffffffffffffffffffffffffffffffff)
    0x841: v841(0x20) = CONST 
    0x843: v843(0x24) = ADD v841(0x20), v821(0x4)
    0x844: v844 = CALLDATALOAD v843(0x24)
    0x845: v845(0x1ef4) = CONST 
    0x848: JUMP v845(0x1ef4)

    Begin block 0x1ef4
    prev=[0x833], succ=[0x1f5e, 0x1f62]
    =================================
    0x1ef5: v1ef5(0x2) = CONST 
    0x1ef7: v1ef7 = SLOAD v1ef5(0x2)
    0x1ef8: v1ef8(0x40) = CONST 
    0x1efb: v1efb = MLOAD v1ef8(0x40)
    0x1efc: v1efc(0x2ecd14d3) = CONST 
    0x1f01: v1f01(0xe2) = CONST 
    0x1f03: v1f03(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1f01(0xe2), v1efc(0x2ecd14d3)
    0x1f05: MSTORE v1efb, v1f03(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1f06: v1f06(0x434f4e54524143545f4f424a4543545f4f574e45525348495) = CONST 
    0x1f20: v1f20(0x3c) = CONST 
    0x1f22: v1f22(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000) = SHL v1f20(0x3c), v1f06(0x434f4e54524143545f4f424a4543545f4f574e45525348495)
    0x1f23: v1f23(0x4) = CONST 
    0x1f26: v1f26 = ADD v1efb, v1f23(0x4)
    0x1f27: MSTORE v1f26, v1f22(0x434f4e54524143545f4f424a4543545f4f574e45525348495000000000000000)
    0x1f29: v1f29 = MLOAD v1ef8(0x40)
    0x1f2a: v1f2a(0x0) = CONST 
    0x1f31: v1f31(0x1) = CONST 
    0x1f33: v1f33(0x1) = CONST 
    0x1f35: v1f35(0xa0) = CONST 
    0x1f37: v1f37(0x10000000000000000000000000000000000000000) = SHL v1f35(0xa0), v1f33(0x1)
    0x1f38: v1f38(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f37(0x10000000000000000000000000000000000000000), v1f31(0x1)
    0x1f3b: v1f3b = AND v1ef7, v1f38(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f3d: v1f3d(0xbb34534c) = CONST 
    0x1f43: v1f43(0x24) = CONST 
    0x1f47: v1f47 = ADD v1efb, v1f43(0x24)
    0x1f49: v1f49(0x20) = CONST 
    0x1f51: v1f51(0x0) = SUB v1efb, v1f29
    0x1f52: v1f52(0x24) = ADD v1f51(0x0), v1f43(0x24)
    0x1f56: v1f56 = EXTCODESIZE v1f3b
    0x1f57: v1f57 = ISZERO v1f56
    0x1f59: v1f59 = ISZERO v1f57
    0x1f5a: v1f5a(0x1f62) = CONST 
    0x1f5d: JUMPI v1f5a(0x1f62), v1f59

    Begin block 0x1f5e
    prev=[0x1ef4], succ=[]
    =================================
    0x1f5e: v1f5e(0x0) = CONST 
    0x1f61: REVERT v1f5e(0x0), v1f5e(0x0)

    Begin block 0x1f62
    prev=[0x1ef4], succ=[0x1f6d, 0x1f76]
    =================================
    0x1f64: v1f64 = GAS 
    0x1f65: v1f65 = STATICCALL v1f64, v1f3b, v1f29, v1f52(0x24), v1f29, v1f49(0x20)
    0x1f66: v1f66 = ISZERO v1f65
    0x1f68: v1f68 = ISZERO v1f66
    0x1f69: v1f69(0x1f76) = CONST 
    0x1f6c: JUMPI v1f69(0x1f76), v1f68

    Begin block 0x1f6d
    prev=[0x1f62], succ=[]
    =================================
    0x1f6d: v1f6d = RETURNDATASIZE 
    0x1f6e: v1f6e(0x0) = CONST 
    0x1f71: RETURNDATACOPY v1f6e(0x0), v1f6e(0x0), v1f6d
    0x1f72: v1f72 = RETURNDATASIZE 
    0x1f73: v1f73(0x0) = CONST 
    0x1f75: REVERT v1f73(0x0), v1f72

    Begin block 0x1f76
    prev=[0x1f62], succ=[0x1f88, 0x1f8c]
    =================================
    0x1f7b: v1f7b(0x40) = CONST 
    0x1f7d: v1f7d = MLOAD v1f7b(0x40)
    0x1f7e: v1f7e = RETURNDATASIZE 
    0x1f7f: v1f7f(0x20) = CONST 
    0x1f82: v1f82 = LT v1f7e, v1f7f(0x20)
    0x1f83: v1f83 = ISZERO v1f82
    0x1f84: v1f84(0x1f8c) = CONST 
    0x1f87: JUMPI v1f84(0x1f8c), v1f83

    Begin block 0x1f88
    prev=[0x1f76], succ=[]
    =================================
    0x1f88: v1f88(0x0) = CONST 
    0x1f8b: REVERT v1f88(0x0), v1f88(0x0)

    Begin block 0x1f8c
    prev=[0x1f76], succ=[0x1fa2, 0x2203]
    =================================
    0x1f8e: v1f8e = MLOAD v1f7d
    0x1f8f: v1f8f(0x1) = CONST 
    0x1f91: v1f91(0x1) = CONST 
    0x1f93: v1f93(0xa0) = CONST 
    0x1f95: v1f95(0x10000000000000000000000000000000000000000) = SHL v1f93(0xa0), v1f91(0x1)
    0x1f96: v1f96(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1f95(0x10000000000000000000000000000000000000000), v1f8f(0x1)
    0x1f99: v1f99 = AND v1f96(0xffffffffffffffffffffffffffffffffffffffff), v83f
    0x1f9b: v1f9b = AND v1f8e, v1f96(0xffffffffffffffffffffffffffffffffffffffff)
    0x1f9c: v1f9c = EQ v1f9b, v1f99
    0x1f9d: v1f9d = ISZERO v1f9c
    0x1f9e: v1f9e(0x2203) = CONST 
    0x1fa1: JUMPI v1f9e(0x2203), v1f9d

    Begin block 0x1fa2
    prev=[0x1f8c], succ=[0x2008, 0x200c]
    =================================
    0x1fa2: v1fa2(0x2) = CONST 
    0x1fa4: v1fa4 = SLOAD v1fa2(0x2)
    0x1fa5: v1fa5(0x40) = CONST 
    0x1fa8: v1fa8 = MLOAD v1fa5(0x40)
    0x1fa9: v1fa9(0x2ecd14d3) = CONST 
    0x1fae: v1fae(0xe2) = CONST 
    0x1fb0: v1fb0(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v1fae(0xe2), v1fa9(0x2ecd14d3)
    0x1fb2: MSTORE v1fa8, v1fb0(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x1fb3: v1fb3(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000) = CONST 
    0x1fd4: v1fd4(0x4) = CONST 
    0x1fd7: v1fd7 = ADD v1fa8, v1fd4(0x4)
    0x1fd8: MSTORE v1fd7, v1fb3(0x434f4e54524143545f494e5445525354454c4c41525f454e434f444552000000)
    0x1fda: v1fda = MLOAD v1fa5(0x40)
    0x1fdb: v1fdb(0x0) = CONST 
    0x1fde: v1fde(0x1) = CONST 
    0x1fe0: v1fe0(0x1) = CONST 
    0x1fe2: v1fe2(0xa0) = CONST 
    0x1fe4: v1fe4(0x10000000000000000000000000000000000000000) = SHL v1fe2(0xa0), v1fe0(0x1)
    0x1fe5: v1fe5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fe4(0x10000000000000000000000000000000000000000), v1fde(0x1)
    0x1fe6: v1fe6 = AND v1fe5(0xffffffffffffffffffffffffffffffffffffffff), v1fa4
    0x1fe8: v1fe8(0xbb34534c) = CONST 
    0x1fee: v1fee(0x24) = CONST 
    0x1ff2: v1ff2 = ADD v1fa8, v1fee(0x24)
    0x1ff4: v1ff4(0x20) = CONST 
    0x1ffb: v1ffb(0x0) = SUB v1fa8, v1fda
    0x1ffc: v1ffc(0x24) = ADD v1ffb(0x0), v1fee(0x24)
    0x2000: v2000 = EXTCODESIZE v1fe6
    0x2001: v2001 = ISZERO v2000
    0x2003: v2003 = ISZERO v2001
    0x2004: v2004(0x200c) = CONST 
    0x2007: JUMPI v2004(0x200c), v2003

    Begin block 0x2008
    prev=[0x1fa2], succ=[]
    =================================
    0x2008: v2008(0x0) = CONST 
    0x200b: REVERT v2008(0x0), v2008(0x0)

    Begin block 0x200c
    prev=[0x1fa2], succ=[0x2017, 0x2020]
    =================================
    0x200e: v200e = GAS 
    0x200f: v200f = STATICCALL v200e, v1fe6, v1fda, v1ffc(0x24), v1fda, v1ff4(0x20)
    0x2010: v2010 = ISZERO v200f
    0x2012: v2012 = ISZERO v2010
    0x2013: v2013(0x2020) = CONST 
    0x2016: JUMPI v2013(0x2020), v2012

    Begin block 0x2017
    prev=[0x200c], succ=[]
    =================================
    0x2017: v2017 = RETURNDATASIZE 
    0x2018: v2018(0x0) = CONST 
    0x201b: RETURNDATACOPY v2018(0x0), v2018(0x0), v2017
    0x201c: v201c = RETURNDATASIZE 
    0x201d: v201d(0x0) = CONST 
    0x201f: REVERT v201d(0x0), v201c

    Begin block 0x2020
    prev=[0x200c], succ=[0x2032, 0x2036]
    =================================
    0x2025: v2025(0x40) = CONST 
    0x2027: v2027 = MLOAD v2025(0x40)
    0x2028: v2028 = RETURNDATASIZE 
    0x2029: v2029(0x20) = CONST 
    0x202c: v202c = LT v2028, v2029(0x20)
    0x202d: v202d = ISZERO v202c
    0x202e: v202e(0x2036) = CONST 
    0x2031: JUMPI v202e(0x2036), v202d

    Begin block 0x2032
    prev=[0x2020], succ=[]
    =================================
    0x2032: v2032(0x0) = CONST 
    0x2035: REVERT v2032(0x0), v2032(0x0)

    Begin block 0x2036
    prev=[0x2020], succ=[0x207d, 0x2081]
    =================================
    0x2038: v2038 = MLOAD v2027
    0x2039: v2039(0x40) = CONST 
    0x203c: v203c = MLOAD v2039(0x40)
    0x203d: v203d(0xf44a67e1) = CONST 
    0x2042: v2042(0xe0) = CONST 
    0x2044: v2044(0xf44a67e100000000000000000000000000000000000000000000000000000000) = SHL v2042(0xe0), v203d(0xf44a67e1)
    0x2046: MSTORE v203c, v2044(0xf44a67e100000000000000000000000000000000000000000000000000000000)
    0x2047: v2047(0x4) = CONST 
    0x204a: v204a = ADD v203c, v2047(0x4)
    0x204d: MSTORE v204a, v844
    0x204f: v204f = MLOAD v2039(0x40)
    0x2050: v2050(0x1) = CONST 
    0x2052: v2052(0x1) = CONST 
    0x2054: v2054(0xa0) = CONST 
    0x2056: v2056(0x10000000000000000000000000000000000000000) = SHL v2054(0xa0), v2052(0x1)
    0x2057: v2057(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2056(0x10000000000000000000000000000000000000000), v2050(0x1)
    0x205a: v205a = AND v2038, v2057(0xffffffffffffffffffffffffffffffffffffffff)
    0x205c: v205c(0xf44a67e1) = CONST 
    0x2062: v2062(0x24) = CONST 
    0x2066: v2066 = ADD v203c, v2062(0x24)
    0x2068: v2068(0x20) = CONST 
    0x2070: v2070(0x0) = SUB v203c, v204f
    0x2071: v2071(0x24) = ADD v2070(0x0), v2062(0x24)
    0x2075: v2075 = EXTCODESIZE v205a
    0x2076: v2076 = ISZERO v2075
    0x2078: v2078 = ISZERO v2076
    0x2079: v2079(0x2081) = CONST 
    0x207c: JUMPI v2079(0x2081), v2078

    Begin block 0x207d
    prev=[0x2036], succ=[]
    =================================
    0x207d: v207d(0x0) = CONST 
    0x2080: REVERT v207d(0x0), v207d(0x0)

    Begin block 0x2081
    prev=[0x2036], succ=[0x208c, 0x2095]
    =================================
    0x2083: v2083 = GAS 
    0x2084: v2084 = STATICCALL v2083, v205a, v204f, v2071(0x24), v204f, v2068(0x20)
    0x2085: v2085 = ISZERO v2084
    0x2087: v2087 = ISZERO v2085
    0x2088: v2088(0x2095) = CONST 
    0x208b: JUMPI v2088(0x2095), v2087

    Begin block 0x208c
    prev=[0x2081], succ=[]
    =================================
    0x208c: v208c = RETURNDATASIZE 
    0x208d: v208d(0x0) = CONST 
    0x2090: RETURNDATACOPY v208d(0x0), v208d(0x0), v208c
    0x2091: v2091 = RETURNDATASIZE 
    0x2092: v2092(0x0) = CONST 
    0x2094: REVERT v2092(0x0), v2091

    Begin block 0x2095
    prev=[0x2081], succ=[0x20a7, 0x20ab]
    =================================
    0x209a: v209a(0x40) = CONST 
    0x209c: v209c = MLOAD v209a(0x40)
    0x209d: v209d = RETURNDATASIZE 
    0x209e: v209e(0x20) = CONST 
    0x20a1: v20a1 = LT v209d, v209e(0x20)
    0x20a2: v20a2 = ISZERO v20a1
    0x20a3: v20a3(0x20ab) = CONST 
    0x20a6: JUMPI v20a3(0x20ab), v20a2

    Begin block 0x20a7
    prev=[0x2095], succ=[]
    =================================
    0x20a7: v20a7(0x0) = CONST 
    0x20aa: REVERT v20a7(0x0), v20a7(0x0)

    Begin block 0x20ab
    prev=[0x2095], succ=[0x20bc, 0x21d7]
    =================================
    0x20ad: v20ad = MLOAD v209c
    0x20b0: v20b0(0xff) = CONST 
    0x20b3: v20b3 = AND v20ad, v20b0(0xff)
    0x20b4: v20b4(0x5) = CONST 
    0x20b6: v20b6 = EQ v20b4(0x5), v20b3
    0x20b7: v20b7 = ISZERO v20b6
    0x20b8: v20b8(0x21d7) = CONST 
    0x20bb: JUMPI v20b8(0x21d7), v20b7

    Begin block 0x20bc
    prev=[0x20ab], succ=[0x2117, 0x211b]
    =================================
    0x20bc: v20bc(0x2) = CONST 
    0x20be: v20be = SLOAD v20bc(0x2)
    0x20bf: v20bf(0x40) = CONST 
    0x20c2: v20c2 = MLOAD v20bf(0x40)
    0x20c3: v20c3(0x2ecd14d3) = CONST 
    0x20c8: v20c8(0xe2) = CONST 
    0x20ca: v20ca(0xbb34534c00000000000000000000000000000000000000000000000000000000) = SHL v20c8(0xe2), v20c3(0x2ecd14d3)
    0x20cc: MSTORE v20c2, v20ca(0xbb34534c00000000000000000000000000000000000000000000000000000000)
    0x20cd: v20cd(0x434f4e54524143545f4954454d5f42415345) = CONST 
    0x20e0: v20e0(0x70) = CONST 
    0x20e2: v20e2(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000) = SHL v20e0(0x70), v20cd(0x434f4e54524143545f4954454d5f42415345)
    0x20e3: v20e3(0x4) = CONST 
    0x20e6: v20e6 = ADD v20c2, v20e3(0x4)
    0x20e7: MSTORE v20e6, v20e2(0x434f4e54524143545f4954454d5f424153450000000000000000000000000000)
    0x20e9: v20e9 = MLOAD v20bf(0x40)
    0x20ea: v20ea(0x1) = CONST 
    0x20ec: v20ec(0x1) = CONST 
    0x20ee: v20ee(0xa0) = CONST 
    0x20f0: v20f0(0x10000000000000000000000000000000000000000) = SHL v20ee(0xa0), v20ec(0x1)
    0x20f1: v20f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v20f0(0x10000000000000000000000000000000000000000), v20ea(0x1)
    0x20f4: v20f4 = AND v20be, v20f1(0xffffffffffffffffffffffffffffffffffffffff)
    0x20f6: v20f6(0xbb34534c) = CONST 
    0x20fc: v20fc(0x24) = CONST 
    0x2100: v2100 = ADD v20c2, v20fc(0x24)
    0x2102: v2102(0x20) = CONST 
    0x210a: v210a(0x0) = SUB v20c2, v20e9
    0x210b: v210b(0x24) = ADD v210a(0x0), v20fc(0x24)
    0x210f: v210f = EXTCODESIZE v20f4
    0x2110: v2110 = ISZERO v210f
    0x2112: v2112 = ISZERO v2110
    0x2113: v2113(0x211b) = CONST 
    0x2116: JUMPI v2113(0x211b), v2112

    Begin block 0x2117
    prev=[0x20bc], succ=[]
    =================================
    0x2117: v2117(0x0) = CONST 
    0x211a: REVERT v2117(0x0), v2117(0x0)

    Begin block 0x211b
    prev=[0x20bc], succ=[0x2126, 0x212f]
    =================================
    0x211d: v211d = GAS 
    0x211e: v211e = STATICCALL v211d, v20f4, v20e9, v210b(0x24), v20e9, v2102(0x20)
    0x211f: v211f = ISZERO v211e
    0x2121: v2121 = ISZERO v211f
    0x2122: v2122(0x212f) = CONST 
    0x2125: JUMPI v2122(0x212f), v2121

    Begin block 0x2126
    prev=[0x211b], succ=[]
    =================================
    0x2126: v2126 = RETURNDATASIZE 
    0x2127: v2127(0x0) = CONST 
    0x212a: RETURNDATACOPY v2127(0x0), v2127(0x0), v2126
    0x212b: v212b = RETURNDATASIZE 
    0x212c: v212c(0x0) = CONST 
    0x212e: REVERT v212c(0x0), v212b

    Begin block 0x212f
    prev=[0x211b], succ=[0x2141, 0x2145]
    =================================
    0x2134: v2134(0x40) = CONST 
    0x2136: v2136 = MLOAD v2134(0x40)
    0x2137: v2137 = RETURNDATASIZE 
    0x2138: v2138(0x20) = CONST 
    0x213b: v213b = LT v2137, v2138(0x20)
    0x213c: v213c = ISZERO v213b
    0x213d: v213d(0x2145) = CONST 
    0x2140: JUMPI v213d(0x2145), v213c

    Begin block 0x2141
    prev=[0x212f], succ=[]
    =================================
    0x2141: v2141(0x0) = CONST 
    0x2144: REVERT v2141(0x0), v2141(0x0)

    Begin block 0x2145
    prev=[0x212f], succ=[0x218c, 0x2190]
    =================================
    0x2147: v2147 = MLOAD v2136
    0x2148: v2148(0x40) = CONST 
    0x214b: v214b = MLOAD v2148(0x40)
    0x214c: v214c(0xaf68dd3f) = CONST 
    0x2151: v2151(0xe0) = CONST 
    0x2153: v2153(0xaf68dd3f00000000000000000000000000000000000000000000000000000000) = SHL v2151(0xe0), v214c(0xaf68dd3f)
    0x2155: MSTORE v214b, v2153(0xaf68dd3f00000000000000000000000000000000000000000000000000000000)
    0x2156: v2156(0x4) = CONST 
    0x2159: v2159 = ADD v214b, v2156(0x4)
    0x215c: MSTORE v2159, v844
    0x215e: v215e = MLOAD v2148(0x40)
    0x215f: v215f(0x1) = CONST 
    0x2161: v2161(0x1) = CONST 
    0x2163: v2163(0xa0) = CONST 
    0x2165: v2165(0x10000000000000000000000000000000000000000) = SHL v2163(0xa0), v2161(0x1)
    0x2166: v2166(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2165(0x10000000000000000000000000000000000000000), v215f(0x1)
    0x2169: v2169 = AND v2147, v2166(0xffffffffffffffffffffffffffffffffffffffff)
    0x216b: v216b(0xaf68dd3f) = CONST 
    0x2171: v2171(0x24) = CONST 
    0x2175: v2175 = ADD v214b, v2171(0x24)
    0x2177: v2177(0x60) = CONST 
    0x217f: v217f(0x0) = SUB v214b, v215e
    0x2180: v2180(0x24) = ADD v217f(0x0), v2171(0x24)
    0x2184: v2184 = EXTCODESIZE v2169
    0x2185: v2185 = ISZERO v2184
    0x2187: v2187 = ISZERO v2185
    0x2188: v2188(0x2190) = CONST 
    0x218b: JUMPI v2188(0x2190), v2187

    Begin block 0x218c
    prev=[0x2145], succ=[]
    =================================
    0x218c: v218c(0x0) = CONST 
    0x218f: REVERT v218c(0x0), v218c(0x0)

    Begin block 0x2190
    prev=[0x2145], succ=[0x219b, 0x21a4]
    =================================
    0x2192: v2192 = GAS 
    0x2193: v2193 = STATICCALL v2192, v2169, v215e, v2180(0x24), v215e, v2177(0x60)
    0x2194: v2194 = ISZERO v2193
    0x2196: v2196 = ISZERO v2194
    0x2197: v2197(0x21a4) = CONST 
    0x219a: JUMPI v2197(0x21a4), v2196

    Begin block 0x219b
    prev=[0x2190], succ=[]
    =================================
    0x219b: v219b = RETURNDATASIZE 
    0x219c: v219c(0x0) = CONST 
    0x219f: RETURNDATACOPY v219c(0x0), v219c(0x0), v219b
    0x21a0: v21a0 = RETURNDATASIZE 
    0x21a1: v21a1(0x0) = CONST 
    0x21a3: REVERT v21a1(0x0), v21a0

    Begin block 0x21a4
    prev=[0x2190], succ=[0x21b6, 0x21ba]
    =================================
    0x21a9: v21a9(0x40) = CONST 
    0x21ab: v21ab = MLOAD v21a9(0x40)
    0x21ac: v21ac = RETURNDATASIZE 
    0x21ad: v21ad(0x60) = CONST 
    0x21b0: v21b0 = LT v21ac, v21ad(0x60)
    0x21b1: v21b1 = ISZERO v21b0
    0x21b2: v21b2(0x21ba) = CONST 
    0x21b5: JUMPI v21b2(0x21ba), v21b1

    Begin block 0x21b6
    prev=[0x21a4], succ=[]
    =================================
    0x21b6: v21b6(0x0) = CONST 
    0x21b9: REVERT v21b6(0x0), v21b6(0x0)

    Begin block 0x21ba
    prev=[0x21a4], succ=[0x3213]
    =================================
    0x21bd: v21bd = MLOAD v21ab
    0x21be: v21be(0x20) = CONST 
    0x21c1: v21c1 = ADD v21ab, v21be(0x20)
    0x21c2: v21c2 = MLOAD v21c1
    0x21c3: v21c3(0x40) = CONST 
    0x21c7: v21c7 = ADD v21ab, v21c3(0x40)
    0x21c8: v21c8 = MLOAD v21c7
    0x21d1: v21d1(0x3213) = CONST 
    0x21d6: JUMP v21d1(0x3213)

    Begin block 0x3213
    prev=[0x21ba], succ=[0x849]
    =================================
    0x3219: JUMP v81e(0x849)

    Begin block 0x849
    prev=[0x3213, 0x3239, 0x2217], succ=[]
    =================================
    0x849_0x0: v849_0 = PHI v21c8, v220f(0x1), v14f9V21e4
    0x849_0x1: v849_1 = PHI v21c2, v21e5(0x0), v220d(0x0)
    0x849_0x2: v849_2 = PHI v21bd, v21f3, v81d1d9b
    0x84a: v84a(0x40) = CONST 
    0x84d: v84d = MLOAD v84a(0x40)
    0x84e: v84e(0xffff) = CONST 
    0x853: v853 = AND v84e(0xffff), v849_2
    0x855: MSTORE v84d, v853
    0x858: v858 = AND v84e(0xffff), v849_1
    0x859: v859(0x20) = CONST 
    0x85c: v85c = ADD v84d, v859(0x20)
    0x85d: MSTORE v85c, v858
    0x85f: v85f = AND v84e(0xffff), v849_0
    0x862: v862 = ADD v84a(0x40), v84d
    0x863: MSTORE v862, v85f
    0x865: v865 = MLOAD v84a(0x40)
    0x869: v869(0x0) = SUB v84d, v865
    0x86a: v86a(0x60) = CONST 
    0x86c: v86c(0x60) = ADD v86a(0x60), v869(0x0)
    0x86e: RETURN v865, v86c(0x60)

    Begin block 0x21d7
    prev=[0x20ab], succ=[0x2201, 0x21e4]
    =================================
    0x21d8: v21d8(0xff) = CONST 
    0x21db: v21db = AND v20ad, v21d8(0xff)
    0x21dc: v21dc(0x4) = CONST 
    0x21de: v21de = EQ v21dc(0x4), v21db
    0x21df: v21df = ISZERO v21de
    0x21e0: v21e0(0x2201) = CONST 
    0x21e3: JUMPI v21e0(0x2201), v21df

    Begin block 0x2201
    prev=[0x21d7], succ=[0x2203]
    =================================

    Begin block 0x2203
    prev=[0x1f8c, 0x2201], succ=[0x1d190x81d]
    =================================
    0x2204: v2204(0x220c) = CONST 
    0x2208: v2208(0x1d19) = CONST 
    0x220b: JUMP v2208(0x1d19)

    Begin block 0x1d190x81d
    prev=[0x2203], succ=[0x1d3b0x81d, 0x1d7e0x81d]
    =================================
    0x1d1a0x81d: v81d1d1a(0x1) = CONST 
    0x1d1c0x81d: v81d1d1c(0x1) = CONST 
    0x1d1e0x81d: v81d1d1e(0xa0) = CONST 
    0x1d200x81d: v81d1d20(0x10000000000000000000000000000000000000000) = SHL v81d1d1e(0xa0), v81d1d1c(0x1)
    0x1d210x81d: v81d1d21(0xffffffffffffffffffffffffffffffffffffffff) = SUB v81d1d20(0x10000000000000000000000000000000000000000), v81d1d1a(0x1)
    0x1d230x81d: v81d1d23 = AND v83f, v81d1d21(0xffffffffffffffffffffffffffffffffffffffff)
    0x1d240x81d: v81d1d24(0x0) = CONST 
    0x1d280x81d: MSTORE v81d1d24(0x0), v81d1d23
    0x1d290x81d: v81d1d29(0x4) = CONST 
    0x1d2b0x81d: v81d1d2b(0x20) = CONST 
    0x1d2d0x81d: MSTORE v81d1d2b(0x20), v81d1d29(0x4)
    0x1d2e0x81d: v81d1d2e(0x40) = CONST 
    0x1d310x81d: v81d1d31 = SHA3 v81d1d24(0x0), v81d1d2e(0x40)
    0x1d320x81d: v81d1d32 = SLOAD v81d1d31
    0x1d330x81d: v81d1d33(0xffff) = CONST 
    0x1d360x81d: v81d1d36 = AND v81d1d33(0xffff), v81d1d32
    0x1d370x81d: v81d1d37(0x1d7e) = CONST 
    0x1d3a0x81d: JUMPI v81d1d37(0x1d7e), v81d1d36

    Begin block 0x1d3b0x81d
    prev=[0x1d190x81d], succ=[]
    =================================
    0x1d3b0x81d: v81d1d3b(0x40) = CONST 
    0x1d3e0x81d: v81d1d3e = MLOAD v81d1d3b(0x40)
    0x1d3f0x81d: v81d1d3f(0x461bcd) = CONST 
    0x1d430x81d: v81d1d43(0xe5) = CONST 
    0x1d450x81d: v81d1d45(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v81d1d43(0xe5), v81d1d3f(0x461bcd)
    0x1d470x81d: MSTORE v81d1d3e, v81d1d45(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x1d480x81d: v81d1d48(0x20) = CONST 
    0x1d4a0x81d: v81d1d4a(0x4) = CONST 
    0x1d4d0x81d: v81d1d4d = ADD v81d1d3e, v81d1d4a(0x4)
    0x1d4e0x81d: MSTORE v81d1d4d, v81d1d48(0x20)
    0x1d4f0x81d: v81d1d4f(0x14) = CONST 
    0x1d510x81d: v81d1d51(0x24) = CONST 
    0x1d540x81d: v81d1d54 = ADD v81d1d3e, v81d1d51(0x24)
    0x1d550x81d: MSTORE v81d1d54, v81d1d4f(0x14)
    0x1d560x81d: v81d1d56(0x119d5c9b9858d94e881393d517d4d5541413d495) = CONST 
    0x1d6b0x81d: v81d1d6b(0x62) = CONST 
    0x1d6d0x81d: v81d1d6d(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000) = SHL v81d1d6b(0x62), v81d1d56(0x119d5c9b9858d94e881393d517d4d5541413d495)
    0x1d6e0x81d: v81d1d6e(0x44) = CONST 
    0x1d710x81d: v81d1d71 = ADD v81d1d3e, v81d1d6e(0x44)
    0x1d720x81d: MSTORE v81d1d71, v81d1d6d(0x4675726e6163653a204e4f545f535550504f5254000000000000000000000000)
    0x1d740x81d: v81d1d74 = MLOAD v81d1d3b(0x40)
    0x1d780x81d: v81d1d78(0x0) = SUB v81d1d3e, v81d1d74
    0x1d790x81d: v81d1d79(0x64) = CONST 
    0x1d7b0x81d: v81d1d7b(0x64) = ADD v81d1d79(0x64), v81d1d78(0x0)
    0x1d7d0x81d: REVERT v81d1d74, v81d1d7b(0x64)

    Begin block 0x1d7e0x81d
    prev=[0x1d190x81d], succ=[0x220c]
    =================================
    0x1d800x81d: v81d1d80(0x1) = CONST 
    0x1d820x81d: v81d1d82(0x1) = CONST 
    0x1d840x81d: v81d1d84(0xa0) = CONST 
    0x1d860x81d: v81d1d86(0x10000000000000000000000000000000000000000) = SHL v81d1d84(0xa0), v81d1d82(0x1)
    0x1d870x81d: v81d1d87(0xffffffffffffffffffffffffffffffffffffffff) = SUB v81d1d86(0x10000000000000000000000000000000000000000), v81d1d80(0x1)
    0x1d880x81d: v81d1d88 = AND v81d1d87(0xffffffffffffffffffffffffffffffffffffffff), v83f
    0x1d890x81d: v81d1d89(0x0) = CONST 
    0x1d8d0x81d: MSTORE v81d1d89(0x0), v81d1d88
    0x1d8e0x81d: v81d1d8e(0x4) = CONST 
    0x1d900x81d: v81d1d90(0x20) = CONST 
    0x1d920x81d: MSTORE v81d1d90(0x20), v81d1d8e(0x4)
    0x1d930x81d: v81d1d93(0x40) = CONST 
    0x1d960x81d: v81d1d96 = SHA3 v81d1d89(0x0), v81d1d93(0x40)
    0x1d970x81d: v81d1d97 = SLOAD v81d1d96
    0x1d980x81d: v81d1d98(0xffff) = CONST 
    0x1d9b0x81d: v81d1d9b = AND v81d1d98(0xffff), v81d1d97
    0x1d9d0x81d: JUMP v2204(0x220c)

    Begin block 0x220c
    prev=[0x1d7e0x81d], succ=[0x2217]
    =================================
    0x220d: v220d(0x0) = CONST 
    0x220f: v220f(0x1) = CONST 

    Begin block 0x2217
    prev=[0x220c], succ=[0x849]
    =================================
    0x221d: JUMP v81e(0x849)

    Begin block 0x21e4
    prev=[0x21d7], succ=[0x14f2B0x21e4]
    =================================
    0x21e5: v21e5(0x0) = CONST 
    0x21e7: v21e7(0x21ef) = CONST 
    0x21eb: v21eb(0x14f2) = CONST 
    0x21ee: JUMP v21eb(0x14f2)

    Begin block 0x14f2B0x21e4
    prev=[0x21e4], succ=[0x21ef]
    =================================
    0x14f3S0x21e4: v14f3V21e4(0x70) = CONST 
    0x14f5S0x21e4: v14f5V21e4 = SHR v14f3V21e4(0x70), v844
    0x14f6S0x21e4: v14f6V21e4(0xffff) = CONST 
    0x14f9S0x21e4: v14f9V21e4 = AND v14f6V21e4(0xffff), v14f5V21e4
    0x14fbS0x21e4: JUMP v21e7(0x21ef)

    Begin block 0x21ef
    prev=[0x14f2B0x21e4], succ=[0x3239]
    =================================
    0x21f1: v21f1(0xff) = CONST 
    0x21f3: v21f3 = AND v21f1(0xff), v20ad
    0x21fd: v21fd(0x3239) = CONST 
    0x2200: JUMP v21fd(0x3239)

    Begin block 0x3239
    prev=[0x21ef], succ=[0x849]
    =================================
    0x323f: JUMP v81e(0x849)

}

function addInternalTokenMeta(bytes32,uint16,uint256)() public {
    Begin block 0x86f
    prev=[], succ=[0x881, 0x885]
    =================================
    0x870: v870(0x3136) = CONST 
    0x873: v873(0x4) = CONST 
    0x876: v876 = CALLDATASIZE 
    0x877: v877 = SUB v876, v873(0x4)
    0x878: v878(0x60) = CONST 
    0x87b: v87b = LT v877, v878(0x60)
    0x87c: v87c = ISZERO v87b
    0x87d: v87d(0x885) = CONST 
    0x880: JUMPI v87d(0x885), v87c

    Begin block 0x881
    prev=[0x86f], succ=[]
    =================================
    0x881: v881(0x0) = CONST 
    0x884: REVERT v881(0x0), v881(0x0)

    Begin block 0x885
    prev=[0x86f], succ=[0x221e]
    =================================
    0x888: v888 = CALLDATALOAD v873(0x4)
    0x88a: v88a(0xffff) = CONST 
    0x88d: v88d(0x20) = CONST 
    0x890: v890(0x24) = ADD v873(0x4), v88d(0x20)
    0x891: v891 = CALLDATALOAD v890(0x24)
    0x892: v892 = AND v891, v88a(0xffff)
    0x894: v894(0x40) = CONST 
    0x896: v896(0x44) = ADD v894(0x40), v873(0x4)
    0x897: v897 = CALLDATALOAD v896(0x44)
    0x898: v898(0x221e) = CONST 
    0x89b: JUMP v898(0x221e)

    Begin block 0x221e
    prev=[0x885], succ=[0x2234]
    =================================
    0x221f: v221f(0x2234) = CONST 
    0x2222: v2222 = CALLER 
    0x2223: v2223(0x0) = CONST 
    0x2225: v2225 = CALLDATALOAD v2223(0x0)
    0x2226: v2226(0x1) = CONST 
    0x2228: v2228(0x1) = CONST 
    0x222a: v222a(0xe0) = CONST 
    0x222c: v222c(0x100000000000000000000000000000000000000000000000000000000) = SHL v222a(0xe0), v2228(0x1)
    0x222d: v222d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = SUB v222c(0x100000000000000000000000000000000000000000000000000000000), v2226(0x1)
    0x222e: v222e(0xffffffff00000000000000000000000000000000000000000000000000000000) = NOT v222d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x222f: v222f = AND v222e(0xffffffff00000000000000000000000000000000000000000000000000000000), v2225
    0x2230: v2230(0x22d3) = CONST 
    0x2233: v2233_0 = CALLPRIVATE v2230(0x22d3), v222f, v2222, v221f(0x2234)

    Begin block 0x2234
    prev=[0x221e], succ=[0x2239, 0x2273]
    =================================
    0x2235: v2235(0x2273) = CONST 
    0x2238: JUMPI v2235(0x2273), v2233_0

    Begin block 0x2239
    prev=[0x2234], succ=[]
    =================================
    0x2239: v2239(0x40) = CONST 
    0x223c: v223c = MLOAD v2239(0x40)
    0x223d: v223d(0x461bcd) = CONST 
    0x2241: v2241(0xe5) = CONST 
    0x2243: v2243(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2241(0xe5), v223d(0x461bcd)
    0x2245: MSTORE v223c, v2243(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2246: v2246(0x20) = CONST 
    0x2248: v2248(0x4) = CONST 
    0x224b: v224b = ADD v223c, v2248(0x4)
    0x224c: MSTORE v224b, v2246(0x20)
    0x224d: v224d(0x14) = CONST 
    0x224f: v224f(0x24) = CONST 
    0x2252: v2252 = ADD v223c, v224f(0x24)
    0x2253: MSTORE v2252, v224d(0x14)
    0x2254: v2254(0x0) = CONST 
    0x2257: v2257 = MLOAD v2254(0x0)
    0x2258: v2258(0x20) = CONST 
    0x225a: v225a(0x2409) = CONST 
    0x2262: MSTORE v2254(0x0), v2257
    0x2263: v2263(0x44) = CONST 
    0x2266: v2266 = ADD v223c, v2263(0x44)
    0x2267: MSTORE v2266, v3431(0x64732d617574682d756e617574686f72697a6564000000000000000000000000)
    0x2269: v2269 = MLOAD v2239(0x40)
    0x226d: v226d(0x0) = SUB v223c, v2269
    0x226e: v226e(0x64) = CONST 
    0x2270: v2270(0x64) = ADD v226e(0x64), v226d(0x0)
    0x2272: REVERT v2269, v2270(0x64)
    0x3431: v3431(0x64732d617574682d756e617574686f72697a6564000000000000000000000000) = CONST 

    Begin block 0x2273
    prev=[0x2234], succ=[0x3136]
    =================================
    0x2274: v2274(0x0) = CONST 
    0x2278: MSTORE v2274(0x0), v888
    0x2279: v2279(0x5) = CONST 
    0x227b: v227b(0x20) = CONST 
    0x227f: MSTORE v227b(0x20), v2279(0x5)
    0x2280: v2280(0x40) = CONST 
    0x2284: v2284 = SHA3 v2274(0x0), v2280(0x40)
    0x2285: v2285(0xffff) = CONST 
    0x2289: v2289 = AND v892, v2285(0xffff)
    0x228c: MSTORE v2274(0x0), v2289
    0x228f: MSTORE v227b(0x20), v2284
    0x2293: v2293 = SHA3 v2274(0x0), v2280(0x40)
    0x2296: SSTORE v2293, v897
    0x2298: v2298 = MLOAD v2280(0x40)
    0x229b: MSTORE v2298, v2289
    0x229e: v229e = ADD v2298, v227b(0x20)
    0x22a1: MSTORE v229e, v897
    0x22a3: v22a3 = MLOAD v2280(0x40)
    0x22a6: v22a6(0xd429d1334d25faabd932782487baaddc69097651c9a519499dedc8cab8c1e6b1) = CONST 
    0x22cb: v22cb(0x0) = SUB v2298, v22a3
    0x22cc: v22cc(0x40) = ADD v22cb(0x0), v2280(0x40)
    0x22ce: LOG2 v22a3, v22cc(0x40), v22a6(0xd429d1334d25faabd932782487baaddc69097651c9a519499dedc8cab8c1e6b1), v888
    0x22d2: JUMP v870(0x3136)

    Begin block 0x3136
    prev=[0x2273], succ=[]
    =================================
    0x3137: STOP 

}

