function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x687]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x67b: v67b(0x687) = CONST 
    0x67c: JUMPI v67b(0x687), v8

    Begin block 0xd
    prev=[0x0], succ=[0x68a, 0x41]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0x100000000000000000000000000000000000000000000000000000000) = CONST 
    0x2f: v2f = DIV vf, v10(0x100000000000000000000000000000000000000000000000000000000)
    0x30: v30(0xffffffff) = CONST 
    0x35: v35 = AND v30(0xffffffff), v2f
    0x37: v37(0x3659cfe6) = CONST 
    0x3c: v3c = EQ v37(0x3659cfe6), v35
    0x67d: v67d(0x68a) = CONST 
    0x67e: JUMPI v67d(0x68a), v3c

    Begin block 0x68a
    prev=[0xd], succ=[]
    =================================
    0x68b: v68b(0x113) = CONST 
    0x68c: CALLPRIVATE v68b(0x113)

    Begin block 0x41
    prev=[0xd], succ=[0x68d, 0x4c]
    =================================
    0x42: v42(0x5c60da1b) = CONST 
    0x47: v47 = EQ v42(0x5c60da1b), v35
    0x67f: v67f(0x68d) = CONST 
    0x680: JUMPI v67f(0x68d), v47

    Begin block 0x68d
    prev=[0x41], succ=[]
    =================================
    0x68e: v68e(0x156) = CONST 
    0x68f: CALLPRIVATE v68e(0x156)

    Begin block 0x4c
    prev=[0x41], succ=[0x690, 0x57]
    =================================
    0x4d: v4d(0x715018a6) = CONST 
    0x52: v52 = EQ v4d(0x715018a6), v35
    0x681: v681(0x690) = CONST 
    0x682: JUMPI v681(0x690), v52

    Begin block 0x690
    prev=[0x4c], succ=[]
    =================================
    0x691: v691(0x1ad) = CONST 
    0x692: CALLPRIVATE v691(0x1ad)

    Begin block 0x57
    prev=[0x4c], succ=[0x693, 0x62]
    =================================
    0x58: v58(0x8da5cb5b) = CONST 
    0x5d: v5d = EQ v58(0x8da5cb5b), v35
    0x683: v683(0x693) = CONST 
    0x684: JUMPI v683(0x693), v5d

    Begin block 0x693
    prev=[0x57], succ=[]
    =================================
    0x694: v694(0x1c4) = CONST 
    0x695: CALLPRIVATE v694(0x1c4)

    Begin block 0x62
    prev=[0x57], succ=[0x687, 0x696]
    =================================
    0x63: v63(0xf2fde38b) = CONST 
    0x68: v68 = EQ v63(0xf2fde38b), v35
    0x685: v685(0x696) = CONST 
    0x686: JUMPI v685(0x696), v68

    Begin block 0x687
    prev=[0x0, 0x62], succ=[]
    =================================
    0x688: v688(0x6d) = CONST 
    0x689: CALLPRIVATE v688(0x6d)

    Begin block 0x696
    prev=[0x62], succ=[]
    =================================
    0x697: v697(0x21b) = CONST 
    0x698: CALLPRIVATE v697(0x21b)

}

function upgradeTo(address)() public {
    Begin block 0x113
    prev=[], succ=[0x11b, 0x11f]
    =================================
    0x114: v114 = CALLVALUE 
    0x116: v116 = ISZERO v114
    0x117: v117(0x11f) = CONST 
    0x11a: JUMPI v117(0x11f), v116

    Begin block 0x11b
    prev=[0x113], succ=[]
    =================================
    0x11b: v11b(0x0) = CONST 
    0x11e: REVERT v11b(0x0), v11b(0x0)

    Begin block 0x11f
    prev=[0x113], succ=[0x288]
    =================================
    0x121: v121(0x154) = CONST 
    0x124: v124(0x4) = CONST 
    0x127: v127 = CALLDATASIZE 
    0x128: v128 = SUB v127, v124(0x4)
    0x12a: v12a = ADD v124(0x4), v128
    0x12e: v12e = CALLDATALOAD v124(0x4)
    0x12f: v12f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x144: v144 = AND v12f(0xffffffffffffffffffffffffffffffffffffffff), v12e
    0x146: v146(0x20) = CONST 
    0x148: v148(0x24) = ADD v146(0x20), v124(0x4)
    0x150: v150(0x288) = CONST 
    0x153: JUMP v150(0x288)

    Begin block 0x288
    prev=[0x11f], succ=[0x2df, 0x2e3]
    =================================
    0x289: v289(0x0) = CONST 
    0x28d: v28d = SLOAD v289(0x0)
    0x28f: v28f(0x100) = CONST 
    0x292: v292(0x1) = EXP v28f(0x100), v289(0x0)
    0x294: v294 = DIV v28d, v292(0x1)
    0x295: v295(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2aa: v2aa = AND v295(0xffffffffffffffffffffffffffffffffffffffff), v294
    0x2ab: v2ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2c0: v2c0 = AND v2ab(0xffffffffffffffffffffffffffffffffffffffff), v2aa
    0x2c1: v2c1 = CALLER 
    0x2c2: v2c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2d7: v2d7 = AND v2c2(0xffffffffffffffffffffffffffffffffffffffff), v2c1
    0x2d8: v2d8 = EQ v2d7, v2c0
    0x2d9: v2d9 = ISZERO v2d8
    0x2da: v2da = ISZERO v2d9
    0x2db: v2db(0x2e3) = CONST 
    0x2de: JUMPI v2db(0x2e3), v2da

    Begin block 0x2df
    prev=[0x288], succ=[]
    =================================
    0x2df: v2df(0x0) = CONST 
    0x2e2: REVERT v2df(0x0), v2df(0x0)

    Begin block 0x2e3
    prev=[0x288], succ=[0x33c, 0x340]
    =================================
    0x2e5: v2e5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2fa: v2fa = AND v2e5(0xffffffffffffffffffffffffffffffffffffffff), v144
    0x2fb: v2fb(0x1) = CONST 
    0x2fd: v2fd(0x0) = CONST 
    0x300: v300 = SLOAD v2fb(0x1)
    0x302: v302(0x100) = CONST 
    0x305: v305(0x1) = EXP v302(0x100), v2fd(0x0)
    0x307: v307 = DIV v300, v305(0x1)
    0x308: v308(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x31d: v31d = AND v308(0xffffffffffffffffffffffffffffffffffffffff), v307
    0x31e: v31e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x333: v333 = AND v31e(0xffffffffffffffffffffffffffffffffffffffff), v31d
    0x334: v334 = EQ v333, v2fa
    0x335: v335 = ISZERO v334
    0x336: v336 = ISZERO v335
    0x337: v337 = ISZERO v336
    0x338: v338(0x340) = CONST 
    0x33b: JUMPI v338(0x340), v337

    Begin block 0x33c
    prev=[0x2e3], succ=[]
    =================================
    0x33c: v33c(0x0) = CONST 
    0x33f: REVERT v33c(0x0), v33c(0x0)

    Begin block 0x340
    prev=[0x2e3], succ=[0x154]
    =================================
    0x342: v342(0x1) = CONST 
    0x344: v344(0x0) = CONST 
    0x346: v346(0x100) = CONST 
    0x349: v349(0x1) = EXP v346(0x100), v344(0x0)
    0x34b: v34b = SLOAD v342(0x1)
    0x34d: v34d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x362: v362(0xffffffffffffffffffffffffffffffffffffffff) = MUL v34d(0xffffffffffffffffffffffffffffffffffffffff), v349(0x1)
    0x363: v363(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v362(0xffffffffffffffffffffffffffffffffffffffff)
    0x364: v364 = AND v363(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v34b
    0x367: v367(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x37c: v37c = AND v367(0xffffffffffffffffffffffffffffffffffffffff), v144
    0x37d: v37d = MUL v37c, v349(0x1)
    0x37e: v37e = OR v37d, v364
    0x380: SSTORE v342(0x1), v37e
    0x383: v383(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x398: v398 = AND v383(0xffffffffffffffffffffffffffffffffffffffff), v144
    0x399: v399(0x1466d4e2c17718222b4ada7f7cbc8907912d6083fdaf34382703d6a9602eef55) = CONST 
    0x3ba: v3ba(0x40) = CONST 
    0x3bc: v3bc = MLOAD v3ba(0x40)
    0x3bd: v3bd(0x40) = CONST 
    0x3bf: v3bf = MLOAD v3bd(0x40)
    0x3c2: v3c2(0x0) = SUB v3bc, v3bf
    0x3c4: LOG2 v3bf, v3c2(0x0), v399(0x1466d4e2c17718222b4ada7f7cbc8907912d6083fdaf34382703d6a9602eef55), v398
    0x3c6: JUMP v121(0x154)

    Begin block 0x154
    prev=[0x340], succ=[]
    =================================
    0x155: STOP 

}

function implementation()() public {
    Begin block 0x156
    prev=[], succ=[0x15e, 0x162]
    =================================
    0x157: v157 = CALLVALUE 
    0x159: v159 = ISZERO v157
    0x15a: v15a(0x162) = CONST 
    0x15d: JUMPI v15a(0x162), v159

    Begin block 0x15e
    prev=[0x156], succ=[]
    =================================
    0x15e: v15e(0x0) = CONST 
    0x161: REVERT v15e(0x0), v15e(0x0)

    Begin block 0x162
    prev=[0x156], succ=[0x25eB0x162]
    =================================
    0x164: v164(0x16b) = CONST 
    0x167: v167(0x25e) = CONST 
    0x16a: JUMP v167(0x25e)

    Begin block 0x25eB0x162
    prev=[0x162], succ=[0x16b]
    =================================
    0x25fS0x162: v25fV162(0x0) = CONST 
    0x261S0x162: v261V162(0x1) = CONST 
    0x263S0x162: v263V162(0x0) = CONST 
    0x266S0x162: v266V162 = SLOAD v261V162(0x1)
    0x268S0x162: v268V162(0x100) = CONST 
    0x26bS0x162: v26bV162(0x1) = EXP v268V162(0x100), v263V162(0x0)
    0x26dS0x162: v26dV162 = DIV v266V162, v26bV162(0x1)
    0x26eS0x162: v26eV162(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x283S0x162: v283V162 = AND v26eV162(0xffffffffffffffffffffffffffffffffffffffff), v26dV162
    0x287S0x162: JUMP v164(0x16b)

    Begin block 0x16b
    prev=[0x25eB0x162], succ=[]
    =================================
    0x16c: v16c(0x40) = CONST 
    0x16e: v16e = MLOAD v16c(0x40)
    0x171: v171(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x186: v186 = AND v171(0xffffffffffffffffffffffffffffffffffffffff), v283V162
    0x187: v187(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x19c: v19c = AND v187(0xffffffffffffffffffffffffffffffffffffffff), v186
    0x19e: MSTORE v16e, v19c
    0x19f: v19f(0x20) = CONST 
    0x1a1: v1a1 = ADD v19f(0x20), v16e
    0x1a5: v1a5(0x40) = CONST 
    0x1a7: v1a7 = MLOAD v1a5(0x40)
    0x1aa: v1aa(0x20) = SUB v1a1, v1a7
    0x1ac: RETURN v1a7, v1aa(0x20)

}

function renounceOwnership()() public {
    Begin block 0x1ad
    prev=[], succ=[0x1b5, 0x1b9]
    =================================
    0x1ae: v1ae = CALLVALUE 
    0x1b0: v1b0 = ISZERO v1ae
    0x1b1: v1b1(0x1b9) = CONST 
    0x1b4: JUMPI v1b1(0x1b9), v1b0

    Begin block 0x1b5
    prev=[0x1ad], succ=[]
    =================================
    0x1b5: v1b5(0x0) = CONST 
    0x1b8: REVERT v1b5(0x0), v1b5(0x0)

    Begin block 0x1b9
    prev=[0x1ad], succ=[0x3c7]
    =================================
    0x1bb: v1bb(0x1c2) = CONST 
    0x1be: v1be(0x3c7) = CONST 
    0x1c1: JUMP v1be(0x3c7)

    Begin block 0x3c7
    prev=[0x1b9], succ=[0x41e, 0x422]
    =================================
    0x3c8: v3c8(0x0) = CONST 
    0x3cc: v3cc = SLOAD v3c8(0x0)
    0x3ce: v3ce(0x100) = CONST 
    0x3d1: v3d1(0x1) = EXP v3ce(0x100), v3c8(0x0)
    0x3d3: v3d3 = DIV v3cc, v3d1(0x1)
    0x3d4: v3d4(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3e9: v3e9 = AND v3d4(0xffffffffffffffffffffffffffffffffffffffff), v3d3
    0x3ea: v3ea(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3ff: v3ff = AND v3ea(0xffffffffffffffffffffffffffffffffffffffff), v3e9
    0x400: v400 = CALLER 
    0x401: v401(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x416: v416 = AND v401(0xffffffffffffffffffffffffffffffffffffffff), v400
    0x417: v417 = EQ v416, v3ff
    0x418: v418 = ISZERO v417
    0x419: v419 = ISZERO v418
    0x41a: v41a(0x422) = CONST 
    0x41d: JUMPI v41a(0x422), v419

    Begin block 0x41e
    prev=[0x3c7], succ=[]
    =================================
    0x41e: v41e(0x0) = CONST 
    0x421: REVERT v41e(0x0), v41e(0x0)

    Begin block 0x422
    prev=[0x3c7], succ=[0x1c2]
    =================================
    0x423: v423(0x0) = CONST 
    0x427: v427 = SLOAD v423(0x0)
    0x429: v429(0x100) = CONST 
    0x42c: v42c(0x1) = EXP v429(0x100), v423(0x0)
    0x42e: v42e = DIV v427, v42c(0x1)
    0x42f: v42f(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x444: v444 = AND v42f(0xffffffffffffffffffffffffffffffffffffffff), v42e
    0x445: v445(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x45a: v45a = AND v445(0xffffffffffffffffffffffffffffffffffffffff), v444
    0x45b: v45b(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820) = CONST 
    0x47c: v47c(0x40) = CONST 
    0x47e: v47e = MLOAD v47c(0x40)
    0x47f: v47f(0x40) = CONST 
    0x481: v481 = MLOAD v47f(0x40)
    0x484: v484(0x0) = SUB v47e, v481
    0x486: LOG2 v481, v484(0x0), v45b(0xf8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c64820), v45a
    0x487: v487(0x0) = CONST 
    0x48a: v48a(0x0) = CONST 
    0x48c: v48c(0x100) = CONST 
    0x48f: v48f(0x1) = EXP v48c(0x100), v48a(0x0)
    0x491: v491 = SLOAD v487(0x0)
    0x493: v493(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4a8: v4a8(0xffffffffffffffffffffffffffffffffffffffff) = MUL v493(0xffffffffffffffffffffffffffffffffffffffff), v48f(0x1)
    0x4a9: v4a9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v4a8(0xffffffffffffffffffffffffffffffffffffffff)
    0x4aa: v4aa = AND v4a9(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v491
    0x4ad: v4ad(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4c2: v4c2(0x0) = AND v4ad(0xffffffffffffffffffffffffffffffffffffffff), v487(0x0)
    0x4c3: v4c3(0x0) = MUL v4c2(0x0), v48f(0x1)
    0x4c4: v4c4 = OR v4c3(0x0), v4aa
    0x4c6: SSTORE v487(0x0), v4c4
    0x4c8: JUMP v1bb(0x1c2)

    Begin block 0x1c2
    prev=[0x422], succ=[]
    =================================
    0x1c3: STOP 

}

function owner()() public {
    Begin block 0x1c4
    prev=[], succ=[0x1cc, 0x1d0]
    =================================
    0x1c5: v1c5 = CALLVALUE 
    0x1c7: v1c7 = ISZERO v1c5
    0x1c8: v1c8(0x1d0) = CONST 
    0x1cb: JUMPI v1c8(0x1d0), v1c7

    Begin block 0x1cc
    prev=[0x1c4], succ=[]
    =================================
    0x1cc: v1cc(0x0) = CONST 
    0x1cf: REVERT v1cc(0x0), v1cc(0x0)

    Begin block 0x1d0
    prev=[0x1c4], succ=[0x4c9]
    =================================
    0x1d2: v1d2(0x1d9) = CONST 
    0x1d5: v1d5(0x4c9) = CONST 
    0x1d8: JUMP v1d5(0x4c9)

    Begin block 0x4c9
    prev=[0x1d0], succ=[0x1d9]
    =================================
    0x4ca: v4ca(0x0) = CONST 
    0x4ce: v4ce = SLOAD v4ca(0x0)
    0x4d0: v4d0(0x100) = CONST 
    0x4d3: v4d3(0x1) = EXP v4d0(0x100), v4ca(0x0)
    0x4d5: v4d5 = DIV v4ce, v4d3(0x1)
    0x4d6: v4d6(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x4eb: v4eb = AND v4d6(0xffffffffffffffffffffffffffffffffffffffff), v4d5
    0x4ed: JUMP v1d2(0x1d9)

    Begin block 0x1d9
    prev=[0x4c9], succ=[]
    =================================
    0x1da: v1da(0x40) = CONST 
    0x1dc: v1dc = MLOAD v1da(0x40)
    0x1df: v1df(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1f4: v1f4 = AND v1df(0xffffffffffffffffffffffffffffffffffffffff), v4eb
    0x1f5: v1f5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x20a: v20a = AND v1f5(0xffffffffffffffffffffffffffffffffffffffff), v1f4
    0x20c: MSTORE v1dc, v20a
    0x20d: v20d(0x20) = CONST 
    0x20f: v20f = ADD v20d(0x20), v1dc
    0x213: v213(0x40) = CONST 
    0x215: v215 = MLOAD v213(0x40)
    0x218: v218(0x20) = SUB v20f, v215
    0x21a: RETURN v215, v218(0x20)

}

function transferOwnership(address)() public {
    Begin block 0x21b
    prev=[], succ=[0x223, 0x227]
    =================================
    0x21c: v21c = CALLVALUE 
    0x21e: v21e = ISZERO v21c
    0x21f: v21f(0x227) = CONST 
    0x222: JUMPI v21f(0x227), v21e

    Begin block 0x223
    prev=[0x21b], succ=[]
    =================================
    0x223: v223(0x0) = CONST 
    0x226: REVERT v223(0x0), v223(0x0)

    Begin block 0x227
    prev=[0x21b], succ=[0x4eeB0x227]
    =================================
    0x229: v229(0x25c) = CONST 
    0x22c: v22c(0x4) = CONST 
    0x22f: v22f = CALLDATASIZE 
    0x230: v230 = SUB v22f, v22c(0x4)
    0x232: v232 = ADD v22c(0x4), v230
    0x236: v236 = CALLDATALOAD v22c(0x4)
    0x237: v237(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24c: v24c = AND v237(0xffffffffffffffffffffffffffffffffffffffff), v236
    0x24e: v24e(0x20) = CONST 
    0x250: v250(0x24) = ADD v24e(0x20), v22c(0x4)
    0x258: v258(0x4ee) = CONST 
    0x25b: JUMP v258(0x4ee), v24c, v229(0x25c)

    Begin block 0x4eeB0x227
    prev=[0x227], succ=[0x545B0x227, 0x549B0x227]
    =================================
    0x4efS0x227: v4efV227(0x0) = CONST 
    0x4f3S0x227: v4f3V227 = SLOAD v4efV227(0x0)
    0x4f5S0x227: v4f5V227(0x100) = CONST 
    0x4f8S0x227: v4f8V227(0x1) = EXP v4f5V227(0x100), v4efV227(0x0)
    0x4faS0x227: v4faV227 = DIV v4f3V227, v4f8V227(0x1)
    0x4fbS0x227: v4fbV227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x510S0x227: v510V227 = AND v4fbV227(0xffffffffffffffffffffffffffffffffffffffff), v4faV227
    0x511S0x227: v511V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x526S0x227: v526V227 = AND v511V227(0xffffffffffffffffffffffffffffffffffffffff), v510V227
    0x527S0x227: v527V227 = CALLER 
    0x528S0x227: v528V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x53dS0x227: v53dV227 = AND v528V227(0xffffffffffffffffffffffffffffffffffffffff), v527V227
    0x53eS0x227: v53eV227 = EQ v53dV227, v526V227
    0x53fS0x227: v53fV227 = ISZERO v53eV227
    0x540S0x227: v540V227 = ISZERO v53fV227
    0x541S0x227: v541V227(0x549) = CONST 
    0x544S0x227: JUMPI v541V227(0x549), v540V227

    Begin block 0x545B0x227
    prev=[0x4eeB0x227], succ=[]
    =================================
    0x545S0x227: v545V227(0x0) = CONST 
    0x548S0x227: REVERT v545V227(0x0), v545V227(0x0)

    Begin block 0x549B0x227
    prev=[0x4eeB0x227], succ=[0x555B0x227]
    =================================
    0x54aS0x227: v54aV227(0x552) = CONST 
    0x54eS0x227: v54eV227(0x555) = CONST 
    0x551S0x227: JUMP v54eV227(0x555)

    Begin block 0x555B0x227
    prev=[0x549B0x227], succ=[0x58dB0x227, 0x591B0x227]
    =================================
    0x556S0x227: v556V227(0x0) = CONST 
    0x558S0x227: v558V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x56dS0x227: v56dV227(0x0) = AND v558V227(0xffffffffffffffffffffffffffffffffffffffff), v556V227(0x0)
    0x56fS0x227: v56fV227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x584S0x227: v584V227 = AND v56fV227(0xffffffffffffffffffffffffffffffffffffffff), v24c
    0x585S0x227: v585V227 = EQ v584V227, v56dV227(0x0)
    0x586S0x227: v586V227 = ISZERO v585V227
    0x587S0x227: v587V227 = ISZERO v586V227
    0x588S0x227: v588V227 = ISZERO v587V227
    0x589S0x227: v589V227(0x591) = CONST 
    0x58cS0x227: JUMPI v589V227(0x591), v588V227

    Begin block 0x58dB0x227
    prev=[0x555B0x227], succ=[]
    =================================
    0x58dS0x227: v58dV227(0x0) = CONST 
    0x590S0x227: REVERT v58dV227(0x0), v58dV227(0x0)

    Begin block 0x591B0x227
    prev=[0x555B0x227], succ=[0x552B0x227]
    =================================
    0x593S0x227: v593V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5a8S0x227: v5a8V227 = AND v593V227(0xffffffffffffffffffffffffffffffffffffffff), v24c
    0x5a9S0x227: v5a9V227(0x0) = CONST 
    0x5adS0x227: v5adV227 = SLOAD v5a9V227(0x0)
    0x5afS0x227: v5afV227(0x100) = CONST 
    0x5b2S0x227: v5b2V227(0x1) = EXP v5afV227(0x100), v5a9V227(0x0)
    0x5b4S0x227: v5b4V227 = DIV v5adV227, v5b2V227(0x1)
    0x5b5S0x227: v5b5V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5caS0x227: v5caV227 = AND v5b5V227(0xffffffffffffffffffffffffffffffffffffffff), v5b4V227
    0x5cbS0x227: v5cbV227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x5e0S0x227: v5e0V227 = AND v5cbV227(0xffffffffffffffffffffffffffffffffffffffff), v5caV227
    0x5e1S0x227: v5e1V227(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0) = CONST 
    0x602S0x227: v602V227(0x40) = CONST 
    0x604S0x227: v604V227 = MLOAD v602V227(0x40)
    0x605S0x227: v605V227(0x40) = CONST 
    0x607S0x227: v607V227 = MLOAD v605V227(0x40)
    0x60aS0x227: v60aV227(0x0) = SUB v604V227, v607V227
    0x60cS0x227: LOG3 v607V227, v60aV227(0x0), v5e1V227(0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0), v5e0V227, v5a8V227
    0x60eS0x227: v60eV227(0x0) = CONST 
    0x611S0x227: v611V227(0x100) = CONST 
    0x614S0x227: v614V227(0x1) = EXP v611V227(0x100), v60eV227(0x0)
    0x616S0x227: v616V227 = SLOAD v60eV227(0x0)
    0x618S0x227: v618V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x62dS0x227: v62dV227(0xffffffffffffffffffffffffffffffffffffffff) = MUL v618V227(0xffffffffffffffffffffffffffffffffffffffff), v614V227(0x1)
    0x62eS0x227: v62eV227(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v62dV227(0xffffffffffffffffffffffffffffffffffffffff)
    0x62fS0x227: v62fV227 = AND v62eV227(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v616V227
    0x632S0x227: v632V227(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x647S0x227: v647V227 = AND v632V227(0xffffffffffffffffffffffffffffffffffffffff), v24c
    0x648S0x227: v648V227 = MUL v647V227, v614V227(0x1)
    0x649S0x227: v649V227 = OR v648V227, v62fV227
    0x64bS0x227: SSTORE v60eV227(0x0), v649V227
    0x64eS0x227: JUMP v54aV227(0x552)

    Begin block 0x552B0x227
    prev=[0x591B0x227], succ=[0x25c]
    =================================
    0x554S0x227: JUMP v229(0x25c)

    Begin block 0x25c
    prev=[0x552B0x227], succ=[]
    =================================
    0x25d: STOP 

}

function fallback()() public {
    Begin block 0x6d
    prev=[], succ=[0x25eB0x6d]
    =================================
    0x6e: v6e(0x0) = CONST 
    0x70: v70(0x60) = CONST 
    0x72: v72(0x79) = CONST 
    0x75: v75(0x25e) = CONST 
    0x78: JUMP v75(0x25e)

    Begin block 0x25eB0x6d
    prev=[0x6d], succ=[0x79]
    =================================
    0x25fS0x6d: v25fV6d(0x0) = CONST 
    0x261S0x6d: v261V6d(0x1) = CONST 
    0x263S0x6d: v263V6d(0x0) = CONST 
    0x266S0x6d: v266V6d = SLOAD v261V6d(0x1)
    0x268S0x6d: v268V6d(0x100) = CONST 
    0x26bS0x6d: v26bV6d(0x1) = EXP v268V6d(0x100), v263V6d(0x0)
    0x26dS0x6d: v26dV6d = DIV v266V6d, v26bV6d(0x1)
    0x26eS0x6d: v26eV6d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x283S0x6d: v283V6d = AND v26eV6d(0xffffffffffffffffffffffffffffffffffffffff), v26dV6d
    0x287S0x6d: JUMP v72(0x79)

    Begin block 0x79
    prev=[0x25eB0x6d], succ=[0xb3, 0xb7]
    =================================
    0x7c: v7c(0x0) = CONST 
    0x7e: v7e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x93: v93(0x0) = AND v7e(0xffffffffffffffffffffffffffffffffffffffff), v7c(0x0)
    0x95: v95(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xaa: vaa = AND v95(0xffffffffffffffffffffffffffffffffffffffff), v283V6d
    0xab: vab = EQ vaa, v93(0x0)
    0xac: vac = ISZERO vab
    0xad: vad = ISZERO vac
    0xae: vae = ISZERO vad
    0xaf: vaf(0xb7) = CONST 
    0xb2: JUMPI vaf(0xb7), vae

    Begin block 0xb3
    prev=[0x79], succ=[]
    =================================
    0xb3: vb3(0x0) = CONST 
    0xb6: REVERT vb3(0x0), vb3(0x0)

    Begin block 0xb7
    prev=[0x79], succ=[0x10f, 0x10c]
    =================================
    0xb8: vb8(0x0) = CONST 
    0xba: vba = CALLDATASIZE 
    0xbd: vbd(0x1f) = CONST 
    0xbf: vbf = ADD vbd(0x1f), vba
    0xc0: vc0(0x20) = CONST 
    0xc4: vc4 = DIV vbf, vc0(0x20)
    0xc5: vc5 = MUL vc4, vc0(0x20)
    0xc6: vc6(0x20) = CONST 
    0xc8: vc8 = ADD vc6(0x20), vc5
    0xc9: vc9(0x40) = CONST 
    0xcb: vcb = MLOAD vc9(0x40)
    0xce: vce = ADD vcb, vc8
    0xcf: vcf(0x40) = CONST 
    0xd1: MSTORE vcf(0x40), vce
    0xd9: MSTORE vcb, vba
    0xda: vda(0x20) = CONST 
    0xdc: vdc = ADD vda(0x20), vcb
    0xe2: CALLDATACOPY vdc, vb8(0x0), vba
    0xe4: ve4 = ADD vdc, vba
    0xee: vee(0x0) = CONST 
    0xf2: vf2 = MLOAD vcb
    0xf3: vf3(0x20) = CONST 
    0xf6: vf6 = ADD vcb, vf3(0x20)
    0xf8: vf8 = GAS 
    0xf9: vf9 = DELEGATECALL vf8, v283V6d, vf6, vf2, vee(0x0), vee(0x0)
    0xfa: vfa = RETURNDATASIZE 
    0xfb: vfb(0x40) = CONST 
    0xfd: vfd = MLOAD vfb(0x40)
    0xff: vff(0x0) = CONST 
    0x102: RETURNDATACOPY vfd, vff(0x0), vfa
    0x104: v104(0x0) = CONST 
    0x107: v107 = EQ vf9, v104(0x0)
    0x108: v108(0x10f) = CONST 
    0x10b: JUMPI v108(0x10f), v107

    Begin block 0x10f
    prev=[0xb7], succ=[]
    =================================
    0x112: REVERT vfd, vfa

    Begin block 0x10c
    prev=[0xb7], succ=[]
    =================================
    0x10e: RETURN vfd, vfa

}

