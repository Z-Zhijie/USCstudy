function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xc81]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xc6f: vc6f(0xc81) = CONST 
    0xc70: JUMPI vc6f(0xc81), v8

    Begin block 0xd
    prev=[0x0], succ=[0x4e, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x6a284837) = CONST 
    0x19: v19 = GT v14(0x6a284837), v12
    0x1a: v1a(0x4e) = CONST 
    0x1d: JUMPI v1a(0x4e), v19

    Begin block 0x4e
    prev=[0xd], succ=[0xc84, 0x5a]
    =================================
    0x50: v50(0x26782247) = CONST 
    0x55: v55 = EQ v50(0x26782247), v12
    0xc79: vc79(0xc84) = CONST 
    0xc7a: JUMPI vc79(0xc84), v55

    Begin block 0xc84
    prev=[0x4e], succ=[]
    =================================
    0xc85: vc85(0x85) = CONST 
    0xc86: CALLPRIVATE vc85(0x85)

    Begin block 0x5a
    prev=[0x4e], succ=[0xc87, 0x65]
    =================================
    0x5b: v5b(0x3659cfe6) = CONST 
    0x60: v60 = EQ v5b(0x3659cfe6), v12
    0xc7b: vc7b(0xc87) = CONST 
    0xc7c: JUMPI vc7b(0xc87), v60

    Begin block 0xc87
    prev=[0x5a], succ=[]
    =================================
    0xc88: vc88(0xb6) = CONST 
    0xc89: CALLPRIVATE vc88(0xb6)

    Begin block 0x65
    prev=[0x5a], succ=[0xc8a, 0x70]
    =================================
    0x66: v66(0x4f1ef286) = CONST 
    0x6b: v6b = EQ v66(0x4f1ef286), v12
    0xc7d: vc7d(0xc8a) = CONST 
    0xc7e: JUMPI vc7d(0xc8a), v6b

    Begin block 0xc8a
    prev=[0x65], succ=[]
    =================================
    0xc8b: vc8b(0xe9) = CONST 
    0xc8c: CALLPRIVATE vc8b(0xe9)

    Begin block 0x70
    prev=[0x65], succ=[0xc81, 0xc8d]
    =================================
    0x71: v71(0x5c60da1b) = CONST 
    0x76: v76 = EQ v71(0x5c60da1b), v12
    0xc7f: vc7f(0xc8d) = CONST 
    0xc80: JUMPI vc7f(0xc8d), v76

    Begin block 0xc81
    prev=[0x0, 0x70], succ=[]
    =================================
    0xc82: vc82(0x7b) = CONST 
    0xc83: CALLPRIVATE vc82(0x7b)

    Begin block 0xc8d
    prev=[0x70], succ=[]
    =================================
    0xc8e: vc8e(0x169) = CONST 
    0xc8f: CALLPRIVATE vc8e(0x169)

    Begin block 0x1e
    prev=[0xd], succ=[0xc90, 0x29]
    =================================
    0x1f: v1f(0x6a284837) = CONST 
    0x24: v24 = EQ v1f(0x6a284837), v12
    0xc71: vc71(0xc90) = CONST 
    0xc72: JUMPI vc71(0xc90), v24

    Begin block 0xc90
    prev=[0x1e], succ=[]
    =================================
    0xc91: vc91(0x17e) = CONST 
    0xc92: CALLPRIVATE vc91(0x17e)

    Begin block 0x29
    prev=[0x1e], succ=[0xc93, 0x34]
    =================================
    0x2a: v2a(0x8f283970) = CONST 
    0x2f: v2f = EQ v2a(0x8f283970), v12
    0xc73: vc73(0xc93) = CONST 
    0xc74: JUMPI vc73(0xc93), v2f

    Begin block 0xc93
    prev=[0x29], succ=[]
    =================================
    0xc94: vc94(0x193) = CONST 
    0xc95: CALLPRIVATE vc94(0x193)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xc96]
    =================================
    0x35: v35(0xd3b2f598) = CONST 
    0x3a: v3a = EQ v35(0xd3b2f598), v12
    0xc75: vc75(0xc96) = CONST 
    0xc76: JUMPI vc75(0xc96), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0xc99]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0xc77: vc77(0xc99) = CONST 
    0xc78: JUMPI vc77(0xc99), v45

    Begin block 0x4a
    prev=[0x3f], succ=[]
    =================================
    0x4a: v4a(0x7b) = CONST 
    0x4d: JUMP v4a(0x7b)

    Begin block 0xc99
    prev=[0x3f], succ=[]
    =================================
    0xc9a: vc9a(0x1db) = CONST 
    0xc9b: CALLPRIVATE vc9a(0x1db)

    Begin block 0xc96
    prev=[0x34], succ=[]
    =================================
    0xc97: vc97(0x1c6) = CONST 
    0xc98: CALLPRIVATE vc97(0x1c6)

}

function implementation()() public {
    Begin block 0x169
    prev=[], succ=[0x171, 0x175]
    =================================
    0x16a: v16a = CALLVALUE 
    0x16c: v16c = ISZERO v16a
    0x16d: v16d(0x175) = CONST 
    0x170: JUMPI v16d(0x175), v16c

    Begin block 0x171
    prev=[0x169], succ=[]
    =================================
    0x171: v171(0x0) = CONST 
    0x174: REVERT v171(0x0), v171(0x0)

    Begin block 0x175
    prev=[0x169], succ=[0xa46]
    =================================
    0x177: v177(0xa46) = CONST 
    0x17a: v17a(0x372) = CONST 
    0x17d: v17d_0 = CALLPRIVATE v17a(0x372), v177(0xa46)

    Begin block 0xa46
    prev=[0x175], succ=[]
    =================================
    0xa47: va47(0x40) = CONST 
    0xa4a: va4a = MLOAD va47(0x40)
    0xa4b: va4b(0x1) = CONST 
    0xa4d: va4d(0x1) = CONST 
    0xa4f: va4f(0xa0) = CONST 
    0xa51: va51(0x10000000000000000000000000000000000000000) = SHL va4f(0xa0), va4d(0x1)
    0xa52: va52(0xffffffffffffffffffffffffffffffffffffffff) = SUB va51(0x10000000000000000000000000000000000000000), va4b(0x1)
    0xa55: va55 = AND v17d_0, va52(0xffffffffffffffffffffffffffffffffffffffff)
    0xa57: MSTORE va4a, va55
    0xa58: va58 = MLOAD va47(0x40)
    0xa5c: va5c(0x0) = SUB va4a, va58
    0xa5d: va5d(0x20) = CONST 
    0xa5f: va5f(0x20) = ADD va5d(0x20), va5c(0x0)
    0xa61: RETURN va58, va5f(0x20)

}

function dTokenImplementation()() public {
    Begin block 0x17e
    prev=[], succ=[0x186, 0x18a]
    =================================
    0x17f: v17f = CALLVALUE 
    0x181: v181 = ISZERO v17f
    0x182: v182(0x18a) = CONST 
    0x185: JUMPI v182(0x18a), v181

    Begin block 0x186
    prev=[0x17e], succ=[]
    =================================
    0x186: v186(0x0) = CONST 
    0x189: REVERT v186(0x0), v186(0x0)

    Begin block 0x18a
    prev=[0x17e], succ=[0x39dB0x18a]
    =================================
    0x18c: v18c(0xa81) = CONST 
    0x18f: v18f(0x39d) = CONST 
    0x192: JUMP v18f(0x39d)

    Begin block 0x39dB0x18a
    prev=[0x18a], succ=[0x690B0x39dB0x18a]
    =================================
    0x39eS0x18a: v39eV18a(0x0) = CONST 
    0x3a0S0x18a: v3a0V18a(0x3a7) = CONST 
    0x3a3S0x18a: v3a3V18a(0x690) = CONST 
    0x3a6S0x18a: JUMP v3a3V18a(0x690)

    Begin block 0x690B0x39dB0x18a
    prev=[0x39dB0x18a], succ=[0x3a7B0x18a]
    =================================
    0x691S0x39dS0x18a: v691V39dV18a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x39dS0x18a: v6b2V39dV18a = SLOAD v691V39dV18a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x39dS0x18a: JUMP v3a0V18a(0x3a7)

    Begin block 0x3a7B0x18a
    prev=[0x690B0x39dB0x18a], succ=[0xa81]
    =================================
    0x3abS0x18a: JUMP v18c(0xa81)

    Begin block 0xa81
    prev=[0x3a7B0x18a], succ=[]
    =================================
    0xa82: va82(0x40) = CONST 
    0xa85: va85 = MLOAD va82(0x40)
    0xa86: va86(0x1) = CONST 
    0xa88: va88(0x1) = CONST 
    0xa8a: va8a(0xa0) = CONST 
    0xa8c: va8c(0x10000000000000000000000000000000000000000) = SHL va8a(0xa0), va88(0x1)
    0xa8d: va8d(0xffffffffffffffffffffffffffffffffffffffff) = SUB va8c(0x10000000000000000000000000000000000000000), va86(0x1)
    0xa90: va90 = AND v6b2V39dV18a, va8d(0xffffffffffffffffffffffffffffffffffffffff)
    0xa92: MSTORE va85, va90
    0xa93: va93 = MLOAD va82(0x40)
    0xa97: va97(0x0) = SUB va85, va93
    0xa98: va98(0x20) = CONST 
    0xa9a: va9a(0x20) = ADD va98(0x20), va97(0x0)
    0xa9c: RETURN va93, va9a(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x193
    prev=[], succ=[0x19b, 0x19f]
    =================================
    0x194: v194 = CALLVALUE 
    0x196: v196 = ISZERO v194
    0x197: v197(0x19f) = CONST 
    0x19a: JUMPI v197(0x19f), v196

    Begin block 0x19b
    prev=[0x193], succ=[]
    =================================
    0x19b: v19b(0x0) = CONST 
    0x19e: REVERT v19b(0x0), v19b(0x0)

    Begin block 0x19f
    prev=[0x193], succ=[0x1b2, 0x1b6]
    =================================
    0x1a1: v1a1(0xabc) = CONST 
    0x1a4: v1a4(0x4) = CONST 
    0x1a7: v1a7 = CALLDATASIZE 
    0x1a8: v1a8 = SUB v1a7, v1a4(0x4)
    0x1a9: v1a9(0x20) = CONST 
    0x1ac: v1ac = LT v1a8, v1a9(0x20)
    0x1ad: v1ad = ISZERO v1ac
    0x1ae: v1ae(0x1b6) = CONST 
    0x1b1: JUMPI v1ae(0x1b6), v1ad

    Begin block 0x1b2
    prev=[0x19f], succ=[]
    =================================
    0x1b2: v1b2(0x0) = CONST 
    0x1b5: REVERT v1b2(0x0), v1b2(0x0)

    Begin block 0x1b6
    prev=[0x19f], succ=[0x3ac]
    =================================
    0x1b8: v1b8 = CALLDATALOAD v1a4(0x4)
    0x1b9: v1b9(0x1) = CONST 
    0x1bb: v1bb(0x1) = CONST 
    0x1bd: v1bd(0xa0) = CONST 
    0x1bf: v1bf(0x10000000000000000000000000000000000000000) = SHL v1bd(0xa0), v1bb(0x1)
    0x1c0: v1c0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1bf(0x10000000000000000000000000000000000000000), v1b9(0x1)
    0x1c1: v1c1 = AND v1c0(0xffffffffffffffffffffffffffffffffffffffff), v1b8
    0x1c2: v1c2(0x3ac) = CONST 
    0x1c5: JUMP v1c2(0x3ac)

    Begin block 0x3ac
    prev=[0x1b6], succ=[0x6d9B0x3ac]
    =================================
    0x3ad: v3ad(0x3b4) = CONST 
    0x3b0: v3b0(0x6d9) = CONST 
    0x3b3: JUMP v3b0(0x6d9)

    Begin block 0x6d9B0x3ac
    prev=[0x3ac], succ=[0x3b4]
    =================================
    0x6daS0x3ac: v6daV3ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x3ac: v6fbV3ac = SLOAD v6daV3ac(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x3ac: JUMP v3ad(0x3b4)

    Begin block 0x3b4
    prev=[0x6d9B0x3ac], succ=[0x3ce, 0x2760x193]
    =================================
    0x3b5: v3b5(0x1) = CONST 
    0x3b7: v3b7(0x1) = CONST 
    0x3b9: v3b9(0xa0) = CONST 
    0x3bb: v3bb(0x10000000000000000000000000000000000000000) = SHL v3b9(0xa0), v3b7(0x1)
    0x3bc: v3bc(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3bb(0x10000000000000000000000000000000000000000), v3b5(0x1)
    0x3bd: v3bd = AND v3bc(0xffffffffffffffffffffffffffffffffffffffff), v6fbV3ac
    0x3be: v3be = CALLER 
    0x3bf: v3bf(0x1) = CONST 
    0x3c1: v3c1(0x1) = CONST 
    0x3c3: v3c3(0xa0) = CONST 
    0x3c5: v3c5(0x10000000000000000000000000000000000000000) = SHL v3c3(0xa0), v3c1(0x1)
    0x3c6: v3c6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3c5(0x10000000000000000000000000000000000000000), v3bf(0x1)
    0x3c7: v3c7 = AND v3c6(0xffffffffffffffffffffffffffffffffffffffff), v3be
    0x3c8: v3c8 = EQ v3c7, v3bd
    0x3c9: v3c9 = ISZERO v3c8
    0x3ca: v3ca(0x276) = CONST 
    0x3cd: JUMPI v3ca(0x276), v3c9

    Begin block 0x3ce
    prev=[0x3b4], succ=[0x3dc, 0x412]
    =================================
    0x3ce: v3ce(0x1) = CONST 
    0x3d0: v3d0(0x1) = CONST 
    0x3d2: v3d2(0xa0) = CONST 
    0x3d4: v3d4(0x10000000000000000000000000000000000000000) = SHL v3d2(0xa0), v3d0(0x1)
    0x3d5: v3d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3d4(0x10000000000000000000000000000000000000000), v3ce(0x1)
    0x3d7: v3d7 = AND v1c1, v3d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x3d8: v3d8(0x412) = CONST 
    0x3db: JUMPI v3d8(0x412), v3d7

    Begin block 0x3dc
    prev=[0x3ce], succ=[]
    =================================
    0x3dc: v3dc(0x40) = CONST 
    0x3de: v3de = MLOAD v3dc(0x40)
    0x3df: v3df(0x461bcd) = CONST 
    0x3e3: v3e3(0xe5) = CONST 
    0x3e5: v3e5(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v3e3(0xe5), v3df(0x461bcd)
    0x3e7: MSTORE v3de, v3e5(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x3e8: v3e8(0x4) = CONST 
    0x3ea: v3ea = ADD v3e8(0x4), v3de
    0x3ed: v3ed(0x20) = CONST 
    0x3ef: v3ef = ADD v3ed(0x20), v3ea
    0x3f2: v3f2(0x20) = SUB v3ef, v3ea
    0x3f4: MSTORE v3ea, v3f2(0x20)
    0x3f5: v3f5(0x36) = CONST 
    0x3f8: MSTORE v3ef, v3f5(0x36)
    0x3f9: v3f9(0x20) = CONST 
    0x3fb: v3fb = ADD v3f9(0x20), v3ef
    0x3fd: v3fd(0x87e) = CONST 
    0x400: v400(0x36) = CONST 
    0x403: CODECOPY v3fb, v3fd(0x87e), v400(0x36)
    0x404: v404(0x40) = CONST 
    0x406: v406 = ADD v404(0x40), v3fb
    0x40a: v40a(0x40) = CONST 
    0x40c: v40c = MLOAD v40a(0x40)
    0x40f: v40f(0x84) = SUB v406, v40c
    0x411: REVERT v40c, v40f(0x84)

    Begin block 0x412
    prev=[0x3ce], succ=[0x6d9B0x412]
    =================================
    0x413: v413(0x41a) = CONST 
    0x416: v416(0x6d9) = CONST 
    0x419: JUMP v416(0x6d9)

    Begin block 0x6d9B0x412
    prev=[0x412], succ=[0x41a]
    =================================
    0x6daS0x412: v6daV412(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x412: v6fbV412 = SLOAD v6daV412(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x412: JUMP v413(0x41a)

    Begin block 0x41a
    prev=[0x6d9B0x412], succ=[0x434, 0x46a]
    =================================
    0x41b: v41b(0x1) = CONST 
    0x41d: v41d(0x1) = CONST 
    0x41f: v41f(0xa0) = CONST 
    0x421: v421(0x10000000000000000000000000000000000000000) = SHL v41f(0xa0), v41d(0x1)
    0x422: v422(0xffffffffffffffffffffffffffffffffffffffff) = SUB v421(0x10000000000000000000000000000000000000000), v41b(0x1)
    0x423: v423 = AND v422(0xffffffffffffffffffffffffffffffffffffffff), v6fbV412
    0x425: v425(0x1) = CONST 
    0x427: v427(0x1) = CONST 
    0x429: v429(0xa0) = CONST 
    0x42b: v42b(0x10000000000000000000000000000000000000000) = SHL v429(0xa0), v427(0x1)
    0x42c: v42c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v42b(0x10000000000000000000000000000000000000000), v425(0x1)
    0x42d: v42d = AND v42c(0xffffffffffffffffffffffffffffffffffffffff), v1c1
    0x42e: v42e = EQ v42d, v423
    0x42f: v42f = ISZERO v42e
    0x430: v430(0x46a) = CONST 
    0x433: JUMPI v430(0x46a), v42f

    Begin block 0x434
    prev=[0x41a], succ=[]
    =================================
    0x434: v434(0x40) = CONST 
    0x436: v436 = MLOAD v434(0x40)
    0x437: v437(0x461bcd) = CONST 
    0x43b: v43b(0xe5) = CONST 
    0x43d: v43d(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v43b(0xe5), v437(0x461bcd)
    0x43f: MSTORE v436, v43d(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x440: v440(0x4) = CONST 
    0x442: v442 = ADD v440(0x4), v436
    0x445: v445(0x20) = CONST 
    0x447: v447 = ADD v445(0x20), v442
    0x44a: v44a(0x20) = SUB v447, v442
    0x44c: MSTORE v442, v44a(0x20)
    0x44d: v44d(0x2e) = CONST 
    0x450: MSTORE v447, v44d(0x2e)
    0x451: v451(0x20) = CONST 
    0x453: v453 = ADD v451(0x20), v447
    0x455: v455(0x8ef) = CONST 
    0x458: v458(0x2e) = CONST 
    0x45b: CODECOPY v453, v455(0x8ef), v458(0x2e)
    0x45c: v45c(0x40) = CONST 
    0x45e: v45e = ADD v45c(0x40), v453
    0x462: v462(0x40) = CONST 
    0x464: v464 = MLOAD v462(0x40)
    0x467: v467(0x84) = SUB v45e, v464
    0x469: REVERT v464, v467(0x84)

    Begin block 0x46a
    prev=[0x41a], succ=[0x6feB0x46a]
    =================================
    0x46b: v46b(0x472) = CONST 
    0x46e: v46e(0x6fe) = CONST 
    0x471: JUMP v46e(0x6fe)

    Begin block 0x6feB0x46a
    prev=[0x46a], succ=[0x472]
    =================================
    0x6ffS0x46a: v6ffV46a(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x720S0x46a: v720V46a = SLOAD v6ffV46a(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x722S0x46a: JUMP v46b(0x472)

    Begin block 0x472
    prev=[0x6feB0x46a], succ=[0x48c, 0x4c2]
    =================================
    0x473: v473(0x1) = CONST 
    0x475: v475(0x1) = CONST 
    0x477: v477(0xa0) = CONST 
    0x479: v479(0x10000000000000000000000000000000000000000) = SHL v477(0xa0), v475(0x1)
    0x47a: v47a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v479(0x10000000000000000000000000000000000000000), v473(0x1)
    0x47b: v47b = AND v47a(0xffffffffffffffffffffffffffffffffffffffff), v720V46a
    0x47d: v47d(0x1) = CONST 
    0x47f: v47f(0x1) = CONST 
    0x481: v481(0xa0) = CONST 
    0x483: v483(0x10000000000000000000000000000000000000000) = SHL v481(0xa0), v47f(0x1)
    0x484: v484(0xffffffffffffffffffffffffffffffffffffffff) = SUB v483(0x10000000000000000000000000000000000000000), v47d(0x1)
    0x485: v485 = AND v484(0xffffffffffffffffffffffffffffffffffffffff), v1c1
    0x486: v486 = EQ v485, v47b
    0x487: v487 = ISZERO v486
    0x488: v488(0x4c2) = CONST 
    0x48b: JUMPI v488(0x4c2), v487

    Begin block 0x48c
    prev=[0x472], succ=[]
    =================================
    0x48c: v48c(0x40) = CONST 
    0x48e: v48e = MLOAD v48c(0x40)
    0x48f: v48f(0x461bcd) = CONST 
    0x493: v493(0xe5) = CONST 
    0x495: v495(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v493(0xe5), v48f(0x461bcd)
    0x497: MSTORE v48e, v495(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x498: v498(0x4) = CONST 
    0x49a: v49a = ADD v498(0x4), v48e
    0x49d: v49d(0x20) = CONST 
    0x49f: v49f = ADD v49d(0x20), v49a
    0x4a2: v4a2(0x20) = SUB v49f, v49a
    0x4a4: MSTORE v49a, v4a2(0x20)
    0x4a5: v4a5(0x38) = CONST 
    0x4a8: MSTORE v49f, v4a5(0x38)
    0x4a9: v4a9(0x20) = CONST 
    0x4ab: v4ab = ADD v4a9(0x20), v49f
    0x4ad: v4ad(0x91d) = CONST 
    0x4b0: v4b0(0x38) = CONST 
    0x4b3: CODECOPY v4ab, v4ad(0x91d), v4b0(0x38)
    0x4b4: v4b4(0x40) = CONST 
    0x4b6: v4b6 = ADD v4b4(0x40), v4ab
    0x4ba: v4ba(0x40) = CONST 
    0x4bc: v4bc = MLOAD v4ba(0x40)
    0x4bf: v4bf(0x84) = SUB v4b6, v4bc
    0x4c1: REVERT v4bc, v4bf(0x84)

    Begin block 0x4c2
    prev=[0x472], succ=[0x76bB0x4c2]
    =================================
    0x4c3: v4c3(0x4cb) = CONST 
    0x4c7: v4c7(0x76b) = CONST 
    0x4ca: JUMP v4c7(0x76b), v1c1, v4c3(0x4cb)

    Begin block 0x76bB0x4c2
    prev=[0x4c2], succ=[0x4cb]
    =================================
    0x76cS0x4c2: v76cV4c2(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x78dS0x4c2: SSTORE v76cV4c2(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c), v1c1
    0x78eS0x4c2: JUMP v4c3(0x4cb)

    Begin block 0x4cb
    prev=[0x76bB0x4c2], succ=[0x6d9B0x4cb]
    =================================
    0x4cc: v4cc(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x4ed: v4ed(0x4f4) = CONST 
    0x4f0: v4f0(0x6d9) = CONST 
    0x4f3: JUMP v4f0(0x6d9)

    Begin block 0x6d9B0x4cb
    prev=[0x4cb], succ=[0x4f4]
    =================================
    0x6daS0x4cb: v6daV4cb(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x4cb: v6fbV4cb = SLOAD v6daV4cb(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x4cb: JUMP v4ed(0x4f4)

    Begin block 0x4f4
    prev=[0x6d9B0x4cb], succ=[0xc2a]
    =================================
    0x4f5: v4f5(0x40) = CONST 
    0x4f8: v4f8 = MLOAD v4f5(0x40)
    0x4f9: v4f9(0x1) = CONST 
    0x4fb: v4fb(0x1) = CONST 
    0x4fd: v4fd(0xa0) = CONST 
    0x4ff: v4ff(0x10000000000000000000000000000000000000000) = SHL v4fd(0xa0), v4fb(0x1)
    0x500: v500(0xffffffffffffffffffffffffffffffffffffffff) = SUB v4ff(0x10000000000000000000000000000000000000000), v4f9(0x1)
    0x503: v503 = AND v500(0xffffffffffffffffffffffffffffffffffffffff), v6fbV4cb
    0x505: MSTORE v4f8, v503
    0x508: v508 = AND v1c1, v500(0xffffffffffffffffffffffffffffffffffffffff)
    0x509: v509(0x20) = CONST 
    0x50c: v50c = ADD v4f8, v509(0x20)
    0x50d: MSTORE v50c, v508
    0x50f: v50f = MLOAD v4f5(0x40)
    0x513: v513(0x0) = SUB v4f8, v50f
    0x514: v514(0x40) = ADD v513(0x0), v4f5(0x40)
    0x516: LOG1 v50f, v514(0x40), v4cc(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x517: v517(0xc2a) = CONST 
    0x51a: JUMP v517(0xc2a)

    Begin block 0xc2a
    prev=[0x4f4], succ=[0xabc]
    =================================
    0xc2c: JUMP v1a1(0xabc)

    Begin block 0xabc
    prev=[0xc2a], succ=[]
    =================================
    0xabd: STOP 

    Begin block 0x2760x193
    prev=[0x3b4], succ=[0x1f00x193]
    =================================
    0x2770x193: v193277(0xbc0) = CONST 
    0x27a0x193: v19327a(0x1f0) = CONST 
    0x27d0x193: JUMP v19327a(0x1f0)

    Begin block 0x1f00x193
    prev=[0x2760x193], succ=[0x1f80x193]
    =================================
    0x1f10x193: v1931f1(0x1f8) = CONST 
    0x1f40x193: v1931f4(0x630) = CONST 
    0x1f70x193: CALLPRIVATE v1931f4(0x630), v1931f1(0x1f8)

    Begin block 0x1f80x193
    prev=[0x1f00x193], succ=[0x690B0x1f80x193]
    =================================
    0x1f90x193: v1931f9(0xb39) = CONST 
    0x1fc0x193: v1931fc(0x203) = CONST 
    0x1ff0x193: v1931ff(0x690) = CONST 
    0x2020x193: JUMP v1931ff(0x690)

    Begin block 0x690B0x1f80x193
    prev=[0x1f80x193], succ=[0x2030x193]
    =================================
    0x691S0x1f80x193: v691V1f8193(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80x193: v6b2V1f8193 = SLOAD v691V1f8193(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80x193: JUMP v1931fc(0x203)

    Begin block 0x2030x193
    prev=[0x690B0x1f80x193], succ=[0x6b50x193]
    =================================
    0x2040x193: v193204(0x6b5) = CONST 
    0x2070x193: JUMP v193204(0x6b5)

    Begin block 0x6b50x193
    prev=[0x2030x193], succ=[0x6d00x193, 0x6d40x193]
    =================================
    0x6b60x193: v1936b6 = CALLDATASIZE 
    0x6b70x193: v1936b7(0x0) = CONST 
    0x6ba0x193: CALLDATACOPY v1936b7(0x0), v1936b7(0x0), v1936b6
    0x6bb0x193: v1936bb(0x0) = CONST 
    0x6be0x193: v1936be = CALLDATASIZE 
    0x6bf0x193: v1936bf(0x0) = CONST 
    0x6c20x193: v1936c2 = GAS 
    0x6c30x193: v1936c3 = DELEGATECALL v1936c2, v6b2V1f8193, v1936bf(0x0), v1936be, v1936bb(0x0), v1936bb(0x0)
    0x6c40x193: v1936c4 = RETURNDATASIZE 
    0x6c50x193: v1936c5(0x0) = CONST 
    0x6c80x193: RETURNDATACOPY v1936c5(0x0), v1936c5(0x0), v1936c4
    0x6cb0x193: v1936cb = ISZERO v1936c3
    0x6cc0x193: v1936cc(0x6d4) = CONST 
    0x6cf0x193: JUMPI v1936cc(0x6d4), v1936cb

    Begin block 0x6d00x193
    prev=[0x6b50x193], succ=[]
    =================================
    0x6d00x193: v1936d0 = RETURNDATASIZE 
    0x6d10x193: v1936d1(0x0) = CONST 
    0x6d30x193: RETURN v1936d1(0x0), v1936d0

    Begin block 0x6d40x193
    prev=[0x6b50x193], succ=[]
    =================================
    0x6d50x193: v1936d5 = RETURNDATASIZE 
    0x6d60x193: v1936d6(0x0) = CONST 
    0x6d80x193: REVERT v1936d6(0x0), v1936d5

}

function updateAdmin()() public {
    Begin block 0x1c6
    prev=[], succ=[0x1ce, 0x1d2]
    =================================
    0x1c7: v1c7 = CALLVALUE 
    0x1c9: v1c9 = ISZERO v1c7
    0x1ca: v1ca(0x1d2) = CONST 
    0x1cd: JUMPI v1ca(0x1d2), v1c9

    Begin block 0x1ce
    prev=[0x1c6], succ=[]
    =================================
    0x1ce: v1ce(0x0) = CONST 
    0x1d1: REVERT v1ce(0x0), v1ce(0x0)

    Begin block 0x1d2
    prev=[0x1c6], succ=[0x51b]
    =================================
    0x1d4: v1d4(0xadd) = CONST 
    0x1d7: v1d7(0x51b) = CONST 
    0x1da: JUMP v1d7(0x51b)

    Begin block 0x51b
    prev=[0x1d2], succ=[0x6feB0x51b]
    =================================
    0x51c: v51c(0x0) = CONST 
    0x51e: v51e(0x525) = CONST 
    0x521: v521(0x6fe) = CONST 
    0x524: JUMP v521(0x6fe)

    Begin block 0x6feB0x51b
    prev=[0x51b], succ=[0x525]
    =================================
    0x6ffS0x51b: v6ffV51b(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x720S0x51b: v720V51b = SLOAD v6ffV51b(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x722S0x51b: JUMP v51e(0x525)

    Begin block 0x525
    prev=[0x6feB0x51b], succ=[0x536, 0x56c]
    =================================
    0x528: v528(0x1) = CONST 
    0x52a: v52a(0x1) = CONST 
    0x52c: v52c(0xa0) = CONST 
    0x52e: v52e(0x10000000000000000000000000000000000000000) = SHL v52c(0xa0), v52a(0x1)
    0x52f: v52f(0xffffffffffffffffffffffffffffffffffffffff) = SUB v52e(0x10000000000000000000000000000000000000000), v528(0x1)
    0x531: v531 = AND v720V51b, v52f(0xffffffffffffffffffffffffffffffffffffffff)
    0x532: v532(0x56c) = CONST 
    0x535: JUMPI v532(0x56c), v531

    Begin block 0x536
    prev=[0x525], succ=[]
    =================================
    0x536: v536(0x40) = CONST 
    0x538: v538 = MLOAD v536(0x40)
    0x539: v539(0x461bcd) = CONST 
    0x53d: v53d(0xe5) = CONST 
    0x53f: v53f(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v53d(0xe5), v539(0x461bcd)
    0x541: MSTORE v538, v53f(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x542: v542(0x4) = CONST 
    0x544: v544 = ADD v542(0x4), v538
    0x547: v547(0x20) = CONST 
    0x549: v549 = ADD v547(0x20), v544
    0x54c: v54c(0x20) = SUB v549, v544
    0x54e: MSTORE v544, v54c(0x20)
    0x54f: v54f(0x36) = CONST 
    0x552: MSTORE v549, v54f(0x36)
    0x553: v553(0x20) = CONST 
    0x555: v555 = ADD v553(0x20), v549
    0x557: v557(0x87e) = CONST 
    0x55a: v55a(0x36) = CONST 
    0x55d: CODECOPY v555, v557(0x87e), v55a(0x36)
    0x55e: v55e(0x40) = CONST 
    0x560: v560 = ADD v55e(0x40), v555
    0x564: v564(0x40) = CONST 
    0x566: v566 = MLOAD v564(0x40)
    0x569: v569(0x84) = SUB v560, v566
    0x56b: REVERT v566, v569(0x84)

    Begin block 0x56c
    prev=[0x525], succ=[0x57d, 0x5b3]
    =================================
    0x56d: v56d = CALLER 
    0x56e: v56e(0x1) = CONST 
    0x570: v570(0x1) = CONST 
    0x572: v572(0xa0) = CONST 
    0x574: v574(0x10000000000000000000000000000000000000000) = SHL v572(0xa0), v570(0x1)
    0x575: v575(0xffffffffffffffffffffffffffffffffffffffff) = SUB v574(0x10000000000000000000000000000000000000000), v56e(0x1)
    0x577: v577 = AND v720V51b, v575(0xffffffffffffffffffffffffffffffffffffffff)
    0x578: v578 = EQ v577, v56d
    0x579: v579(0x5b3) = CONST 
    0x57c: JUMPI v579(0x5b3), v578

    Begin block 0x57d
    prev=[0x56c], succ=[]
    =================================
    0x57d: v57d(0x40) = CONST 
    0x57f: v57f = MLOAD v57d(0x40)
    0x580: v580(0x461bcd) = CONST 
    0x584: v584(0xe5) = CONST 
    0x586: v586(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v584(0xe5), v580(0x461bcd)
    0x588: MSTORE v57f, v586(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x589: v589(0x4) = CONST 
    0x58b: v58b = ADD v589(0x4), v57f
    0x58e: v58e(0x20) = CONST 
    0x590: v590 = ADD v58e(0x20), v58b
    0x593: v593(0x20) = SUB v590, v58b
    0x595: MSTORE v58b, v593(0x20)
    0x596: v596(0x2a) = CONST 
    0x599: MSTORE v590, v596(0x2a)
    0x59a: v59a(0x20) = CONST 
    0x59c: v59c = ADD v59a(0x20), v590
    0x59e: v59e(0x822) = CONST 
    0x5a1: v5a1(0x2a) = CONST 
    0x5a4: CODECOPY v59c, v59e(0x822), v5a1(0x2a)
    0x5a5: v5a5(0x40) = CONST 
    0x5a7: v5a7 = ADD v5a5(0x40), v59c
    0x5ab: v5ab(0x40) = CONST 
    0x5ad: v5ad = MLOAD v5ab(0x40)
    0x5b0: v5b0(0x84) = SUB v5a7, v5ad
    0x5b2: REVERT v5ad, v5b0(0x84)

    Begin block 0x5b3
    prev=[0x56c], succ=[0x78f]
    =================================
    0x5b4: v5b4(0x5bc) = CONST 
    0x5b8: v5b8(0x78f) = CONST 
    0x5bb: JUMP v5b8(0x78f)

    Begin block 0x78f
    prev=[0x5b3], succ=[0x5bc]
    =================================
    0x790: v790(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x7b1: SSTORE v790(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b), v720V51b
    0x7b2: JUMP v5b4(0x5bc)

    Begin block 0x5bc
    prev=[0x78f], succ=[0x76bB0x5bc]
    =================================
    0x5bd: v5bd(0x5c6) = CONST 
    0x5c0: v5c0(0x0) = CONST 
    0x5c2: v5c2(0x76b) = CONST 
    0x5c5: JUMP v5c2(0x76b), v5c0(0x0), v5bd(0x5c6)

    Begin block 0x76bB0x5bc
    prev=[0x5bc], succ=[0x5c6]
    =================================
    0x76cS0x5bc: v76cV5bc(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x78dS0x5bc: SSTORE v76cV5bc(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c), v5c0(0x0)
    0x78eS0x5bc: JUMP v5bd(0x5c6)

    Begin block 0x5c6
    prev=[0x76bB0x5bc], succ=[0xadd]
    =================================
    0x5c7: v5c7(0x40) = CONST 
    0x5ca: v5ca = MLOAD v5c7(0x40)
    0x5cb: v5cb(0x1) = CONST 
    0x5cd: v5cd(0x1) = CONST 
    0x5cf: v5cf(0xa0) = CONST 
    0x5d1: v5d1(0x10000000000000000000000000000000000000000) = SHL v5cf(0xa0), v5cd(0x1)
    0x5d2: v5d2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v5d1(0x10000000000000000000000000000000000000000), v5cb(0x1)
    0x5d4: v5d4 = AND v720V51b, v5d2(0xffffffffffffffffffffffffffffffffffffffff)
    0x5d6: MSTORE v5ca, v5d4
    0x5d8: v5d8 = MLOAD v5c7(0x40)
    0x5d9: v5d9(0x54e4612788f90384e6843298d7854436f3a585b2c3831ab66abf1de63bfa6c2d) = CONST 
    0x5fd: v5fd(0x0) = SUB v5ca, v5d8
    0x5fe: v5fe(0x20) = CONST 
    0x600: v600(0x20) = ADD v5fe(0x20), v5fd(0x0)
    0x602: LOG1 v5d8, v600(0x20), v5d9(0x54e4612788f90384e6843298d7854436f3a585b2c3831ab66abf1de63bfa6c2d)
    0x604: JUMP v1d4(0xadd)

    Begin block 0xadd
    prev=[0x5c6], succ=[]
    =================================
    0xade: STOP 

}

function admin()() public {
    Begin block 0x1db
    prev=[], succ=[0x1e3, 0x1e7]
    =================================
    0x1dc: v1dc = CALLVALUE 
    0x1de: v1de = ISZERO v1dc
    0x1df: v1df(0x1e7) = CONST 
    0x1e2: JUMPI v1df(0x1e7), v1de

    Begin block 0x1e3
    prev=[0x1db], succ=[]
    =================================
    0x1e3: v1e3(0x0) = CONST 
    0x1e6: REVERT v1e3(0x0), v1e3(0x0)

    Begin block 0x1e7
    prev=[0x1db], succ=[0xafe]
    =================================
    0x1e9: v1e9(0xafe) = CONST 
    0x1ec: v1ec(0x605) = CONST 
    0x1ef: v1ef_0 = CALLPRIVATE v1ec(0x605), v1e9(0xafe)

    Begin block 0xafe
    prev=[0x1e7], succ=[]
    =================================
    0xaff: vaff(0x40) = CONST 
    0xb02: vb02 = MLOAD vaff(0x40)
    0xb03: vb03(0x1) = CONST 
    0xb05: vb05(0x1) = CONST 
    0xb07: vb07(0xa0) = CONST 
    0xb09: vb09(0x10000000000000000000000000000000000000000) = SHL vb07(0xa0), vb05(0x1)
    0xb0a: vb0a(0xffffffffffffffffffffffffffffffffffffffff) = SUB vb09(0x10000000000000000000000000000000000000000), vb03(0x1)
    0xb0d: vb0d = AND v1ef_0, vb0a(0xffffffffffffffffffffffffffffffffffffffff)
    0xb0f: MSTORE vb02, vb0d
    0xb10: vb10 = MLOAD vaff(0x40)
    0xb14: vb14(0x0) = SUB vb02, vb10
    0xb15: vb15(0x20) = CONST 
    0xb17: vb17(0x20) = ADD vb15(0x20), vb14(0x0)
    0xb19: RETURN vb10, vb17(0x20)

}

function 0x20a(0x20aarg0x0) private {
    Begin block 0x20a
    prev=[], succ=[0x6d9B0x20a]
    =================================
    0x20b: v20b(0x0) = CONST 
    0x20d: v20d(0x214) = CONST 
    0x210: v210(0x6d9) = CONST 
    0x213: JUMP v210(0x6d9)

    Begin block 0x6d9B0x20a
    prev=[0x20a], succ=[0x214]
    =================================
    0x6daS0x20a: v6daV20a(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x20a: v6fbV20a = SLOAD v6daV20a(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x20a: JUMP v20d(0x214)

    Begin block 0x214
    prev=[0x6d9B0x20a], succ=[0x22e, 0x23c0x20a]
    =================================
    0x215: v215(0x1) = CONST 
    0x217: v217(0x1) = CONST 
    0x219: v219(0xa0) = CONST 
    0x21b: v21b(0x10000000000000000000000000000000000000000) = SHL v219(0xa0), v217(0x1)
    0x21c: v21c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v21b(0x10000000000000000000000000000000000000000), v215(0x1)
    0x21d: v21d = AND v21c(0xffffffffffffffffffffffffffffffffffffffff), v6fbV20a
    0x21e: v21e = CALLER 
    0x21f: v21f(0x1) = CONST 
    0x221: v221(0x1) = CONST 
    0x223: v223(0xa0) = CONST 
    0x225: v225(0x10000000000000000000000000000000000000000) = SHL v223(0xa0), v221(0x1)
    0x226: v226(0xffffffffffffffffffffffffffffffffffffffff) = SUB v225(0x10000000000000000000000000000000000000000), v21f(0x1)
    0x227: v227 = AND v226(0xffffffffffffffffffffffffffffffffffffffff), v21e
    0x228: v228 = EQ v227, v21d
    0x229: v229 = ISZERO v228
    0x22a: v22a(0x23c) = CONST 
    0x22d: JUMPI v22a(0x23c), v229

    Begin block 0x22e
    prev=[0x214], succ=[0x6feB0x22e]
    =================================
    0x22e: v22e(0x235) = CONST 
    0x231: v231(0x6fe) = CONST 
    0x234: JUMP v231(0x6fe)

    Begin block 0x6feB0x22e
    prev=[0x22e], succ=[0x2350x20a]
    =================================
    0x6ffS0x22e: v6ffV22e(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c) = CONST 
    0x720S0x22e: v720V22e = SLOAD v6ffV22e(0x54ac2bd5363dfe95a011c5b5a153968d77d153d212e900afce8624fdad74525c)
    0x722S0x22e: JUMP v22e(0x235)

    Begin block 0x2350x20a
    prev=[0x6feB0x22e], succ=[0xb5a0x20a]
    =================================
    0x2380x20a: v20a238(0xb5a) = CONST 
    0x23b0x20a: JUMP v20a238(0xb5a)

    Begin block 0xb5a0x20a
    prev=[0x2350x20a], succ=[]
    =================================
    0xb5c0x20a: RETURNPRIVATE v20aarg0, v720V22e

    Begin block 0x23c0x20a
    prev=[0x214], succ=[0x1f00x20a]
    =================================
    0x23d0x20a: v20a23d(0xb7c) = CONST 
    0x2400x20a: v20a240(0x1f0) = CONST 
    0x2430x20a: JUMP v20a240(0x1f0)

    Begin block 0x1f00x20a
    prev=[0x23c0x20a], succ=[0x1f80x20a]
    =================================
    0x1f10x20a: v20a1f1(0x1f8) = CONST 
    0x1f40x20a: v20a1f4(0x630) = CONST 
    0x1f70x20a: CALLPRIVATE v20a1f4(0x630), v20a1f1(0x1f8)

    Begin block 0x1f80x20a
    prev=[0x1f00x20a], succ=[0x690B0x1f80x20a]
    =================================
    0x1f90x20a: v20a1f9(0xb39) = CONST 
    0x1fc0x20a: v20a1fc(0x203) = CONST 
    0x1ff0x20a: v20a1ff(0x690) = CONST 
    0x2020x20a: JUMP v20a1ff(0x690)

    Begin block 0x690B0x1f80x20a
    prev=[0x1f80x20a], succ=[0x2030x20a]
    =================================
    0x691S0x1f80x20a: v691V1f820a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80x20a: v6b2V1f820a = SLOAD v691V1f820a(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80x20a: JUMP v20a1fc(0x203)

    Begin block 0x2030x20a
    prev=[0x690B0x1f80x20a], succ=[0x6b50x20a]
    =================================
    0x2040x20a: v20a204(0x6b5) = CONST 
    0x2070x20a: JUMP v20a204(0x6b5)

    Begin block 0x6b50x20a
    prev=[0x2030x20a], succ=[0x6d00x20a, 0x6d40x20a]
    =================================
    0x6b60x20a: v20a6b6 = CALLDATASIZE 
    0x6b70x20a: v20a6b7(0x0) = CONST 
    0x6ba0x20a: CALLDATACOPY v20a6b7(0x0), v20a6b7(0x0), v20a6b6
    0x6bb0x20a: v20a6bb(0x0) = CONST 
    0x6be0x20a: v20a6be = CALLDATASIZE 
    0x6bf0x20a: v20a6bf(0x0) = CONST 
    0x6c20x20a: v20a6c2 = GAS 
    0x6c30x20a: v20a6c3 = DELEGATECALL v20a6c2, v6b2V1f820a, v20a6bf(0x0), v20a6be, v20a6bb(0x0), v20a6bb(0x0)
    0x6c40x20a: v20a6c4 = RETURNDATASIZE 
    0x6c50x20a: v20a6c5(0x0) = CONST 
    0x6c80x20a: RETURNDATACOPY v20a6c5(0x0), v20a6c5(0x0), v20a6c4
    0x6cb0x20a: v20a6cb = ISZERO v20a6c3
    0x6cc0x20a: v20a6cc(0x6d4) = CONST 
    0x6cf0x20a: JUMPI v20a6cc(0x6d4), v20a6cb

    Begin block 0x6d00x20a
    prev=[0x6b50x20a], succ=[]
    =================================
    0x6d00x20a: v20a6d0 = RETURNDATASIZE 
    0x6d10x20a: v20a6d1(0x0) = CONST 
    0x6d30x20a: RETURN v20a6d1(0x0), v20a6d0

    Begin block 0x6d40x20a
    prev=[0x6b50x20a], succ=[]
    =================================
    0x6d50x20a: v20a6d5 = RETURNDATASIZE 
    0x6d60x20a: v20a6d6(0x0) = CONST 
    0x6d80x20a: REVERT v20a6d6(0x0), v20a6d5

}

function 0x372(0x372arg0x0) private {
    Begin block 0x372
    prev=[], succ=[0x6d9B0x372]
    =================================
    0x373: v373(0x0) = CONST 
    0x375: v375(0x37c) = CONST 
    0x378: v378(0x6d9) = CONST 
    0x37b: JUMP v378(0x6d9)

    Begin block 0x6d9B0x372
    prev=[0x372], succ=[0x37c]
    =================================
    0x6daS0x372: v6daV372(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x372: v6fbV372 = SLOAD v6daV372(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x372: JUMP v375(0x37c)

    Begin block 0x37c
    prev=[0x6d9B0x372], succ=[0x396, 0x23c0x372]
    =================================
    0x37d: v37d(0x1) = CONST 
    0x37f: v37f(0x1) = CONST 
    0x381: v381(0xa0) = CONST 
    0x383: v383(0x10000000000000000000000000000000000000000) = SHL v381(0xa0), v37f(0x1)
    0x384: v384(0xffffffffffffffffffffffffffffffffffffffff) = SUB v383(0x10000000000000000000000000000000000000000), v37d(0x1)
    0x385: v385 = AND v384(0xffffffffffffffffffffffffffffffffffffffff), v6fbV372
    0x386: v386 = CALLER 
    0x387: v387(0x1) = CONST 
    0x389: v389(0x1) = CONST 
    0x38b: v38b(0xa0) = CONST 
    0x38d: v38d(0x10000000000000000000000000000000000000000) = SHL v38b(0xa0), v389(0x1)
    0x38e: v38e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v38d(0x10000000000000000000000000000000000000000), v387(0x1)
    0x38f: v38f = AND v38e(0xffffffffffffffffffffffffffffffffffffffff), v386
    0x390: v390 = EQ v38f, v385
    0x391: v391 = ISZERO v390
    0x392: v392(0x23c) = CONST 
    0x395: JUMPI v392(0x23c), v391

    Begin block 0x396
    prev=[0x37c], succ=[0x690B0x396]
    =================================
    0x396: v396(0x235) = CONST 
    0x399: v399(0x690) = CONST 
    0x39c: JUMP v399(0x690)

    Begin block 0x690B0x396
    prev=[0x396], succ=[0x2350x372]
    =================================
    0x691S0x396: v691V396(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x396: v6b2V396 = SLOAD v691V396(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x396: JUMP v396(0x235)

    Begin block 0x2350x372
    prev=[0x690B0x396], succ=[0xb5a0x372]
    =================================
    0x2380x372: v372238(0xb5a) = CONST 
    0x23b0x372: JUMP v372238(0xb5a)

    Begin block 0xb5a0x372
    prev=[0x2350x372], succ=[]
    =================================
    0xb5c0x372: RETURNPRIVATE v372arg0, v6b2V396

    Begin block 0x23c0x372
    prev=[0x37c], succ=[0x1f00x372]
    =================================
    0x23d0x372: v37223d(0xb7c) = CONST 
    0x2400x372: v372240(0x1f0) = CONST 
    0x2430x372: JUMP v372240(0x1f0)

    Begin block 0x1f00x372
    prev=[0x23c0x372], succ=[0x1f80x372]
    =================================
    0x1f10x372: v3721f1(0x1f8) = CONST 
    0x1f40x372: v3721f4(0x630) = CONST 
    0x1f70x372: CALLPRIVATE v3721f4(0x630), v3721f1(0x1f8)

    Begin block 0x1f80x372
    prev=[0x1f00x372], succ=[0x690B0x1f80x372]
    =================================
    0x1f90x372: v3721f9(0xb39) = CONST 
    0x1fc0x372: v3721fc(0x203) = CONST 
    0x1ff0x372: v3721ff(0x690) = CONST 
    0x2020x372: JUMP v3721ff(0x690)

    Begin block 0x690B0x1f80x372
    prev=[0x1f80x372], succ=[0x2030x372]
    =================================
    0x691S0x1f80x372: v691V1f8372(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80x372: v6b2V1f8372 = SLOAD v691V1f8372(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80x372: JUMP v3721fc(0x203)

    Begin block 0x2030x372
    prev=[0x690B0x1f80x372], succ=[0x6b50x372]
    =================================
    0x2040x372: v372204(0x6b5) = CONST 
    0x2070x372: JUMP v372204(0x6b5)

    Begin block 0x6b50x372
    prev=[0x2030x372], succ=[0x6d00x372, 0x6d40x372]
    =================================
    0x6b60x372: v3726b6 = CALLDATASIZE 
    0x6b70x372: v3726b7(0x0) = CONST 
    0x6ba0x372: CALLDATACOPY v3726b7(0x0), v3726b7(0x0), v3726b6
    0x6bb0x372: v3726bb(0x0) = CONST 
    0x6be0x372: v3726be = CALLDATASIZE 
    0x6bf0x372: v3726bf(0x0) = CONST 
    0x6c20x372: v3726c2 = GAS 
    0x6c30x372: v3726c3 = DELEGATECALL v3726c2, v6b2V1f8372, v3726bf(0x0), v3726be, v3726bb(0x0), v3726bb(0x0)
    0x6c40x372: v3726c4 = RETURNDATASIZE 
    0x6c50x372: v3726c5(0x0) = CONST 
    0x6c80x372: RETURNDATACOPY v3726c5(0x0), v3726c5(0x0), v3726c4
    0x6cb0x372: v3726cb = ISZERO v3726c3
    0x6cc0x372: v3726cc(0x6d4) = CONST 
    0x6cf0x372: JUMPI v3726cc(0x6d4), v3726cb

    Begin block 0x6d00x372
    prev=[0x6b50x372], succ=[]
    =================================
    0x6d00x372: v3726d0 = RETURNDATASIZE 
    0x6d10x372: v3726d1(0x0) = CONST 
    0x6d30x372: RETURN v3726d1(0x0), v3726d0

    Begin block 0x6d40x372
    prev=[0x6b50x372], succ=[]
    =================================
    0x6d50x372: v3726d5 = RETURNDATASIZE 
    0x6d60x372: v3726d6(0x0) = CONST 
    0x6d80x372: REVERT v3726d6(0x0), v3726d5

}

function 0x605(0x605arg0x0) private {
    Begin block 0x605
    prev=[], succ=[0x6d9B0x605]
    =================================
    0x606: v606(0x0) = CONST 
    0x608: v608(0x60f) = CONST 
    0x60b: v60b(0x6d9) = CONST 
    0x60e: JUMP v60b(0x6d9)

    Begin block 0x6d9B0x605
    prev=[0x605], succ=[0x60f]
    =================================
    0x6daS0x605: v6daV605(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x605: v6fbV605 = SLOAD v6daV605(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x605: JUMP v608(0x60f)

    Begin block 0x60f
    prev=[0x6d9B0x605], succ=[0x629, 0x23c0x605]
    =================================
    0x610: v610(0x1) = CONST 
    0x612: v612(0x1) = CONST 
    0x614: v614(0xa0) = CONST 
    0x616: v616(0x10000000000000000000000000000000000000000) = SHL v614(0xa0), v612(0x1)
    0x617: v617(0xffffffffffffffffffffffffffffffffffffffff) = SUB v616(0x10000000000000000000000000000000000000000), v610(0x1)
    0x618: v618 = AND v617(0xffffffffffffffffffffffffffffffffffffffff), v6fbV605
    0x619: v619 = CALLER 
    0x61a: v61a(0x1) = CONST 
    0x61c: v61c(0x1) = CONST 
    0x61e: v61e(0xa0) = CONST 
    0x620: v620(0x10000000000000000000000000000000000000000) = SHL v61e(0xa0), v61c(0x1)
    0x621: v621(0xffffffffffffffffffffffffffffffffffffffff) = SUB v620(0x10000000000000000000000000000000000000000), v61a(0x1)
    0x622: v622 = AND v621(0xffffffffffffffffffffffffffffffffffffffff), v619
    0x623: v623 = EQ v622, v618
    0x624: v624 = ISZERO v623
    0x625: v625(0x23c) = CONST 
    0x628: JUMPI v625(0x23c), v624

    Begin block 0x629
    prev=[0x60f], succ=[0x6d9B0x629]
    =================================
    0x629: v629(0x235) = CONST 
    0x62c: v62c(0x6d9) = CONST 
    0x62f: JUMP v62c(0x6d9)

    Begin block 0x6d9B0x629
    prev=[0x629], succ=[0x2350x605]
    =================================
    0x6daS0x629: v6daV629(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x629: v6fbV629 = SLOAD v6daV629(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x629: JUMP v629(0x235)

    Begin block 0x2350x605
    prev=[0x6d9B0x629], succ=[0xb5a0x605]
    =================================
    0x2380x605: v605238(0xb5a) = CONST 
    0x23b0x605: JUMP v605238(0xb5a)

    Begin block 0xb5a0x605
    prev=[0x2350x605], succ=[]
    =================================
    0xb5c0x605: RETURNPRIVATE v605arg0, v6fbV629

    Begin block 0x23c0x605
    prev=[0x60f], succ=[0x1f00x605]
    =================================
    0x23d0x605: v60523d(0xb7c) = CONST 
    0x2400x605: v605240(0x1f0) = CONST 
    0x2430x605: JUMP v605240(0x1f0)

    Begin block 0x1f00x605
    prev=[0x23c0x605], succ=[0x1f80x605]
    =================================
    0x1f10x605: v6051f1(0x1f8) = CONST 
    0x1f40x605: v6051f4(0x630) = CONST 
    0x1f70x605: CALLPRIVATE v6051f4(0x630), v6051f1(0x1f8)

    Begin block 0x1f80x605
    prev=[0x1f00x605], succ=[0x690B0x1f80x605]
    =================================
    0x1f90x605: v6051f9(0xb39) = CONST 
    0x1fc0x605: v6051fc(0x203) = CONST 
    0x1ff0x605: v6051ff(0x690) = CONST 
    0x2020x605: JUMP v6051ff(0x690)

    Begin block 0x690B0x1f80x605
    prev=[0x1f80x605], succ=[0x2030x605]
    =================================
    0x691S0x1f80x605: v691V1f8605(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80x605: v6b2V1f8605 = SLOAD v691V1f8605(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80x605: JUMP v6051fc(0x203)

    Begin block 0x2030x605
    prev=[0x690B0x1f80x605], succ=[0x6b50x605]
    =================================
    0x2040x605: v605204(0x6b5) = CONST 
    0x2070x605: JUMP v605204(0x6b5)

    Begin block 0x6b50x605
    prev=[0x2030x605], succ=[0x6d00x605, 0x6d40x605]
    =================================
    0x6b60x605: v6056b6 = CALLDATASIZE 
    0x6b70x605: v6056b7(0x0) = CONST 
    0x6ba0x605: CALLDATACOPY v6056b7(0x0), v6056b7(0x0), v6056b6
    0x6bb0x605: v6056bb(0x0) = CONST 
    0x6be0x605: v6056be = CALLDATASIZE 
    0x6bf0x605: v6056bf(0x0) = CONST 
    0x6c20x605: v6056c2 = GAS 
    0x6c30x605: v6056c3 = DELEGATECALL v6056c2, v6b2V1f8605, v6056bf(0x0), v6056be, v6056bb(0x0), v6056bb(0x0)
    0x6c40x605: v6056c4 = RETURNDATASIZE 
    0x6c50x605: v6056c5(0x0) = CONST 
    0x6c80x605: RETURNDATACOPY v6056c5(0x0), v6056c5(0x0), v6056c4
    0x6cb0x605: v6056cb = ISZERO v6056c3
    0x6cc0x605: v6056cc(0x6d4) = CONST 
    0x6cf0x605: JUMPI v6056cc(0x6d4), v6056cb

    Begin block 0x6d00x605
    prev=[0x6b50x605], succ=[]
    =================================
    0x6d00x605: v6056d0 = RETURNDATASIZE 
    0x6d10x605: v6056d1(0x0) = CONST 
    0x6d30x605: RETURN v6056d1(0x0), v6056d0

    Begin block 0x6d40x605
    prev=[0x6b50x605], succ=[]
    =================================
    0x6d50x605: v6056d5 = RETURNDATASIZE 
    0x6d60x605: v6056d6(0x0) = CONST 
    0x6d80x605: REVERT v6056d6(0x0), v6056d5

}

function 0x630(0x630arg0x0) private {
    Begin block 0x630
    prev=[], succ=[0x6d9B0x630]
    =================================
    0x631: v631(0x638) = CONST 
    0x634: v634(0x6d9) = CONST 
    0x637: JUMP v634(0x6d9)

    Begin block 0x6d9B0x630
    prev=[0x630], succ=[0x638]
    =================================
    0x6daS0x630: v6daV630(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x630: v6fbV630 = SLOAD v6daV630(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x630: JUMP v631(0x638)

    Begin block 0x638
    prev=[0x6d9B0x630], succ=[0x652, 0x688]
    =================================
    0x639: v639(0x1) = CONST 
    0x63b: v63b(0x1) = CONST 
    0x63d: v63d(0xa0) = CONST 
    0x63f: v63f(0x10000000000000000000000000000000000000000) = SHL v63d(0xa0), v63b(0x1)
    0x640: v640(0xffffffffffffffffffffffffffffffffffffffff) = SUB v63f(0x10000000000000000000000000000000000000000), v639(0x1)
    0x641: v641 = AND v640(0xffffffffffffffffffffffffffffffffffffffff), v6fbV630
    0x642: v642 = CALLER 
    0x643: v643(0x1) = CONST 
    0x645: v645(0x1) = CONST 
    0x647: v647(0xa0) = CONST 
    0x649: v649(0x10000000000000000000000000000000000000000) = SHL v647(0xa0), v645(0x1)
    0x64a: v64a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v649(0x10000000000000000000000000000000000000000), v643(0x1)
    0x64b: v64b = AND v64a(0xffffffffffffffffffffffffffffffffffffffff), v642
    0x64c: v64c = EQ v64b, v641
    0x64d: v64d = ISZERO v64c
    0x64e: v64e(0x688) = CONST 
    0x651: JUMPI v64e(0x688), v64d

    Begin block 0x652
    prev=[0x638], succ=[]
    =================================
    0x652: v652(0x40) = CONST 
    0x654: v654 = MLOAD v652(0x40)
    0x655: v655(0x461bcd) = CONST 
    0x659: v659(0xe5) = CONST 
    0x65b: v65b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v659(0xe5), v655(0x461bcd)
    0x65d: MSTORE v654, v65b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x65e: v65e(0x4) = CONST 
    0x660: v660 = ADD v65e(0x4), v654
    0x663: v663(0x20) = CONST 
    0x665: v665 = ADD v663(0x20), v660
    0x668: v668(0x20) = SUB v665, v660
    0x66a: MSTORE v660, v668(0x20)
    0x66b: v66b(0x32) = CONST 
    0x66e: MSTORE v665, v66b(0x32)
    0x66f: v66f(0x20) = CONST 
    0x671: v671 = ADD v66f(0x20), v665
    0x673: v673(0x84c) = CONST 
    0x676: v676(0x32) = CONST 
    0x679: CODECOPY v671, v673(0x84c), v676(0x32)
    0x67a: v67a(0x40) = CONST 
    0x67c: v67c = ADD v67a(0x40), v671
    0x680: v680(0x40) = CONST 
    0x682: v682 = MLOAD v680(0x40)
    0x685: v685(0x84) = SUB v67c, v682
    0x687: REVERT v682, v685(0x84)

    Begin block 0x688
    prev=[0x638], succ=[0xc6dB0x688]
    =================================
    0x689: v689(0xc4c) = CONST 
    0x68c: v68c(0xc6d) = CONST 
    0x68f: JUMP v68c(0xc6d), v689(0xc4c)

    Begin block 0xc6dB0x688
    prev=[0x688], succ=[0xc4c]
    =================================
    0xc6eS0x688: JUMP v689(0xc4c)

    Begin block 0xc4c
    prev=[0xc6dB0x688], succ=[]
    =================================
    0xc4d: RETURNPRIVATE v630arg0

}

function 0x723(0x723arg0x0, 0x723arg0x1) private {
    Begin block 0x723
    prev=[], succ=[0x7b3]
    =================================
    0x724: v724(0x72c) = CONST 
    0x728: v728(0x7b3) = CONST 
    0x72b: JUMP v728(0x7b3)

    Begin block 0x7b3
    prev=[0x723], succ=[0x81b]
    =================================
    0x7b4: v7b4(0x7bc) = CONST 
    0x7b8: v7b8(0x81b) = CONST 
    0x7bb: JUMP v7b8(0x81b)

    Begin block 0x81b
    prev=[0x7b3], succ=[0x7bc]
    =================================
    0x81c: v81c = EXTCODESIZE v723arg0
    0x81d: v81d = ISZERO v81c
    0x81e: v81e = ISZERO v81d
    0x820: JUMP v7b4(0x7bc)

    Begin block 0x7bc
    prev=[0x81b], succ=[0x7c1, 0x7f7]
    =================================
    0x7bd: v7bd(0x7f7) = CONST 
    0x7c0: JUMPI v7bd(0x7f7), v81e

    Begin block 0x7c1
    prev=[0x7bc], succ=[]
    =================================
    0x7c1: v7c1(0x40) = CONST 
    0x7c3: v7c3 = MLOAD v7c1(0x40)
    0x7c4: v7c4(0x461bcd) = CONST 
    0x7c8: v7c8(0xe5) = CONST 
    0x7ca: v7ca(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7c8(0xe5), v7c4(0x461bcd)
    0x7cc: MSTORE v7c3, v7ca(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7cd: v7cd(0x4) = CONST 
    0x7cf: v7cf = ADD v7cd(0x4), v7c3
    0x7d2: v7d2(0x20) = CONST 
    0x7d4: v7d4 = ADD v7d2(0x20), v7cf
    0x7d7: v7d7(0x20) = SUB v7d4, v7cf
    0x7d9: MSTORE v7cf, v7d7(0x20)
    0x7da: v7da(0x3b) = CONST 
    0x7dd: MSTORE v7d4, v7da(0x3b)
    0x7de: v7de(0x20) = CONST 
    0x7e0: v7e0 = ADD v7de(0x20), v7d4
    0x7e2: v7e2(0x8b4) = CONST 
    0x7e5: v7e5(0x3b) = CONST 
    0x7e8: CODECOPY v7e0, v7e2(0x8b4), v7e5(0x3b)
    0x7e9: v7e9(0x40) = CONST 
    0x7eb: v7eb = ADD v7e9(0x40), v7e0
    0x7ef: v7ef(0x40) = CONST 
    0x7f1: v7f1 = MLOAD v7ef(0x40)
    0x7f4: v7f4(0x84) = SUB v7eb, v7f1
    0x7f6: REVERT v7f1, v7f4(0x84)

    Begin block 0x7f7
    prev=[0x7bc], succ=[0x72c]
    =================================
    0x7f8: v7f8(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x819: SSTORE v7f8(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), v723arg0
    0x81a: JUMP v724(0x72c)

    Begin block 0x72c
    prev=[0x7f7], succ=[]
    =================================
    0x72d: v72d(0x40) = CONST 
    0x730: v730 = MLOAD v72d(0x40)
    0x731: v731(0x1) = CONST 
    0x733: v733(0x1) = CONST 
    0x735: v735(0xa0) = CONST 
    0x737: v737(0x10000000000000000000000000000000000000000) = SHL v735(0xa0), v733(0x1)
    0x738: v738(0xffffffffffffffffffffffffffffffffffffffff) = SUB v737(0x10000000000000000000000000000000000000000), v731(0x1)
    0x73a: v73a = AND v723arg0, v738(0xffffffffffffffffffffffffffffffffffffffff)
    0x73c: MSTORE v730, v73a
    0x73e: v73e = MLOAD v72d(0x40)
    0x73f: v73f(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x763: v763(0x0) = SUB v730, v73e
    0x764: v764(0x20) = CONST 
    0x766: v766(0x20) = ADD v764(0x20), v763(0x0)
    0x768: LOG1 v73e, v766(0x20), v73f(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b)
    0x76a: RETURNPRIVATE v723arg1

}

function fallback()() public {
    Begin block 0x7b
    prev=[], succ=[0x1f00x7b]
    =================================
    0x7c: v7c(0x9a8) = CONST 
    0x7f: v7f(0x1f0) = CONST 
    0x82: JUMP v7f(0x1f0)

    Begin block 0x1f00x7b
    prev=[0x7b], succ=[0x1f80x7b]
    =================================
    0x1f10x7b: v7b1f1(0x1f8) = CONST 
    0x1f40x7b: v7b1f4(0x630) = CONST 
    0x1f70x7b: CALLPRIVATE v7b1f4(0x630), v7b1f1(0x1f8)

    Begin block 0x1f80x7b
    prev=[0x1f00x7b], succ=[0x690B0x1f80x7b]
    =================================
    0x1f90x7b: v7b1f9(0xb39) = CONST 
    0x1fc0x7b: v7b1fc(0x203) = CONST 
    0x1ff0x7b: v7b1ff(0x690) = CONST 
    0x2020x7b: JUMP v7b1ff(0x690)

    Begin block 0x690B0x1f80x7b
    prev=[0x1f80x7b], succ=[0x2030x7b]
    =================================
    0x691S0x1f80x7b: v691V1f87b(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80x7b: v6b2V1f87b = SLOAD v691V1f87b(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80x7b: JUMP v7b1fc(0x203)

    Begin block 0x2030x7b
    prev=[0x690B0x1f80x7b], succ=[0x6b50x7b]
    =================================
    0x2040x7b: v7b204(0x6b5) = CONST 
    0x2070x7b: JUMP v7b204(0x6b5)

    Begin block 0x6b50x7b
    prev=[0x2030x7b], succ=[0x6d00x7b, 0x6d40x7b]
    =================================
    0x6b60x7b: v7b6b6 = CALLDATASIZE 
    0x6b70x7b: v7b6b7(0x0) = CONST 
    0x6ba0x7b: CALLDATACOPY v7b6b7(0x0), v7b6b7(0x0), v7b6b6
    0x6bb0x7b: v7b6bb(0x0) = CONST 
    0x6be0x7b: v7b6be = CALLDATASIZE 
    0x6bf0x7b: v7b6bf(0x0) = CONST 
    0x6c20x7b: v7b6c2 = GAS 
    0x6c30x7b: v7b6c3 = DELEGATECALL v7b6c2, v6b2V1f87b, v7b6bf(0x0), v7b6be, v7b6bb(0x0), v7b6bb(0x0)
    0x6c40x7b: v7b6c4 = RETURNDATASIZE 
    0x6c50x7b: v7b6c5(0x0) = CONST 
    0x6c80x7b: RETURNDATACOPY v7b6c5(0x0), v7b6c5(0x0), v7b6c4
    0x6cb0x7b: v7b6cb = ISZERO v7b6c3
    0x6cc0x7b: v7b6cc(0x6d4) = CONST 
    0x6cf0x7b: JUMPI v7b6cc(0x6d4), v7b6cb

    Begin block 0x6d00x7b
    prev=[0x6b50x7b], succ=[]
    =================================
    0x6d00x7b: v7b6d0 = RETURNDATASIZE 
    0x6d10x7b: v7b6d1(0x0) = CONST 
    0x6d30x7b: RETURN v7b6d1(0x0), v7b6d0

    Begin block 0x6d40x7b
    prev=[0x6b50x7b], succ=[]
    =================================
    0x6d50x7b: v7b6d5 = RETURNDATASIZE 
    0x6d60x7b: v7b6d6(0x0) = CONST 
    0x6d80x7b: REVERT v7b6d6(0x0), v7b6d5

}

function pendingAdmin()() public {
    Begin block 0x85
    prev=[], succ=[0x8d, 0x91]
    =================================
    0x86: v86 = CALLVALUE 
    0x88: v88 = ISZERO v86
    0x89: v89(0x91) = CONST 
    0x8c: JUMPI v89(0x91), v88

    Begin block 0x8d
    prev=[0x85], succ=[]
    =================================
    0x8d: v8d(0x0) = CONST 
    0x90: REVERT v8d(0x0), v8d(0x0)

    Begin block 0x91
    prev=[0x85], succ=[0x9c9]
    =================================
    0x93: v93(0x9c9) = CONST 
    0x96: v96(0x20a) = CONST 
    0x99: v99_0 = CALLPRIVATE v96(0x20a), v93(0x9c9)

    Begin block 0x9c9
    prev=[0x91], succ=[]
    =================================
    0x9ca: v9ca(0x40) = CONST 
    0x9cd: v9cd = MLOAD v9ca(0x40)
    0x9ce: v9ce(0x1) = CONST 
    0x9d0: v9d0(0x1) = CONST 
    0x9d2: v9d2(0xa0) = CONST 
    0x9d4: v9d4(0x10000000000000000000000000000000000000000) = SHL v9d2(0xa0), v9d0(0x1)
    0x9d5: v9d5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9d4(0x10000000000000000000000000000000000000000), v9ce(0x1)
    0x9d8: v9d8 = AND v99_0, v9d5(0xffffffffffffffffffffffffffffffffffffffff)
    0x9da: MSTORE v9cd, v9d8
    0x9db: v9db = MLOAD v9ca(0x40)
    0x9df: v9df(0x0) = SUB v9cd, v9db
    0x9e0: v9e0(0x20) = CONST 
    0x9e2: v9e2(0x20) = ADD v9e0(0x20), v9df(0x0)
    0x9e4: RETURN v9db, v9e2(0x20)

}

function upgradeTo(address)() public {
    Begin block 0xb6
    prev=[], succ=[0xbe, 0xc2]
    =================================
    0xb7: vb7 = CALLVALUE 
    0xb9: vb9 = ISZERO vb7
    0xba: vba(0xc2) = CONST 
    0xbd: JUMPI vba(0xc2), vb9

    Begin block 0xbe
    prev=[0xb6], succ=[]
    =================================
    0xbe: vbe(0x0) = CONST 
    0xc1: REVERT vbe(0x0), vbe(0x0)

    Begin block 0xc2
    prev=[0xb6], succ=[0xd5, 0xd9]
    =================================
    0xc4: vc4(0xa04) = CONST 
    0xc7: vc7(0x4) = CONST 
    0xca: vca = CALLDATASIZE 
    0xcb: vcb = SUB vca, vc7(0x4)
    0xcc: vcc(0x20) = CONST 
    0xcf: vcf = LT vcb, vcc(0x20)
    0xd0: vd0 = ISZERO vcf
    0xd1: vd1(0xd9) = CONST 
    0xd4: JUMPI vd1(0xd9), vd0

    Begin block 0xd5
    prev=[0xc2], succ=[]
    =================================
    0xd5: vd5(0x0) = CONST 
    0xd8: REVERT vd5(0x0), vd5(0x0)

    Begin block 0xd9
    prev=[0xc2], succ=[0x247]
    =================================
    0xdb: vdb = CALLDATALOAD vc7(0x4)
    0xdc: vdc(0x1) = CONST 
    0xde: vde(0x1) = CONST 
    0xe0: ve0(0xa0) = CONST 
    0xe2: ve2(0x10000000000000000000000000000000000000000) = SHL ve0(0xa0), vde(0x1)
    0xe3: ve3(0xffffffffffffffffffffffffffffffffffffffff) = SUB ve2(0x10000000000000000000000000000000000000000), vdc(0x1)
    0xe4: ve4 = AND ve3(0xffffffffffffffffffffffffffffffffffffffff), vdb
    0xe5: ve5(0x247) = CONST 
    0xe8: JUMP ve5(0x247)

    Begin block 0x247
    prev=[0xd9], succ=[0x6d9B0x247]
    =================================
    0x248: v248(0x24f) = CONST 
    0x24b: v24b(0x6d9) = CONST 
    0x24e: JUMP v24b(0x6d9)

    Begin block 0x6d9B0x247
    prev=[0x247], succ=[0x24f]
    =================================
    0x6daS0x247: v6daV247(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x247: v6fbV247 = SLOAD v6daV247(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x247: JUMP v248(0x24f)

    Begin block 0x24f
    prev=[0x6d9B0x247], succ=[0x269, 0x2760xb6]
    =================================
    0x250: v250(0x1) = CONST 
    0x252: v252(0x1) = CONST 
    0x254: v254(0xa0) = CONST 
    0x256: v256(0x10000000000000000000000000000000000000000) = SHL v254(0xa0), v252(0x1)
    0x257: v257(0xffffffffffffffffffffffffffffffffffffffff) = SUB v256(0x10000000000000000000000000000000000000000), v250(0x1)
    0x258: v258 = AND v257(0xffffffffffffffffffffffffffffffffffffffff), v6fbV247
    0x259: v259 = CALLER 
    0x25a: v25a(0x1) = CONST 
    0x25c: v25c(0x1) = CONST 
    0x25e: v25e(0xa0) = CONST 
    0x260: v260(0x10000000000000000000000000000000000000000) = SHL v25e(0xa0), v25c(0x1)
    0x261: v261(0xffffffffffffffffffffffffffffffffffffffff) = SUB v260(0x10000000000000000000000000000000000000000), v25a(0x1)
    0x262: v262 = AND v261(0xffffffffffffffffffffffffffffffffffffffff), v259
    0x263: v263 = EQ v262, v258
    0x264: v264 = ISZERO v263
    0x265: v265(0x276) = CONST 
    0x268: JUMPI v265(0x276), v264

    Begin block 0x269
    prev=[0x24f], succ=[0x271]
    =================================
    0x269: v269(0x271) = CONST 
    0x26d: v26d(0x723) = CONST 
    0x270: CALLPRIVATE v26d(0x723), ve4, v269(0x271)

    Begin block 0x271
    prev=[0x269], succ=[0xb9e]
    =================================
    0x272: v272(0xb9e) = CONST 
    0x275: JUMP v272(0xb9e)

    Begin block 0xb9e
    prev=[0x271], succ=[0xa04]
    =================================
    0xba0: JUMP vc4(0xa04)

    Begin block 0xa04
    prev=[0xb9e], succ=[]
    =================================
    0xa05: STOP 

    Begin block 0x2760xb6
    prev=[0x24f], succ=[0x1f00xb6]
    =================================
    0x2770xb6: vb6277(0xbc0) = CONST 
    0x27a0xb6: vb627a(0x1f0) = CONST 
    0x27d0xb6: JUMP vb627a(0x1f0)

    Begin block 0x1f00xb6
    prev=[0x2760xb6], succ=[0x1f80xb6]
    =================================
    0x1f10xb6: vb61f1(0x1f8) = CONST 
    0x1f40xb6: vb61f4(0x630) = CONST 
    0x1f70xb6: CALLPRIVATE vb61f4(0x630), vb61f1(0x1f8)

    Begin block 0x1f80xb6
    prev=[0x1f00xb6], succ=[0x690B0x1f80xb6]
    =================================
    0x1f90xb6: vb61f9(0xb39) = CONST 
    0x1fc0xb6: vb61fc(0x203) = CONST 
    0x1ff0xb6: vb61ff(0x690) = CONST 
    0x2020xb6: JUMP vb61ff(0x690)

    Begin block 0x690B0x1f80xb6
    prev=[0x1f80xb6], succ=[0x2030xb6]
    =================================
    0x691S0x1f80xb6: v691V1f8b6(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80xb6: v6b2V1f8b6 = SLOAD v691V1f8b6(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80xb6: JUMP vb61fc(0x203)

    Begin block 0x2030xb6
    prev=[0x690B0x1f80xb6], succ=[0x6b50xb6]
    =================================
    0x2040xb6: vb6204(0x6b5) = CONST 
    0x2070xb6: JUMP vb6204(0x6b5)

    Begin block 0x6b50xb6
    prev=[0x2030xb6], succ=[0x6d00xb6, 0x6d40xb6]
    =================================
    0x6b60xb6: vb66b6 = CALLDATASIZE 
    0x6b70xb6: vb66b7(0x0) = CONST 
    0x6ba0xb6: CALLDATACOPY vb66b7(0x0), vb66b7(0x0), vb66b6
    0x6bb0xb6: vb66bb(0x0) = CONST 
    0x6be0xb6: vb66be = CALLDATASIZE 
    0x6bf0xb6: vb66bf(0x0) = CONST 
    0x6c20xb6: vb66c2 = GAS 
    0x6c30xb6: vb66c3 = DELEGATECALL vb66c2, v6b2V1f8b6, vb66bf(0x0), vb66be, vb66bb(0x0), vb66bb(0x0)
    0x6c40xb6: vb66c4 = RETURNDATASIZE 
    0x6c50xb6: vb66c5(0x0) = CONST 
    0x6c80xb6: RETURNDATACOPY vb66c5(0x0), vb66c5(0x0), vb66c4
    0x6cb0xb6: vb66cb = ISZERO vb66c3
    0x6cc0xb6: vb66cc(0x6d4) = CONST 
    0x6cf0xb6: JUMPI vb66cc(0x6d4), vb66cb

    Begin block 0x6d00xb6
    prev=[0x6b50xb6], succ=[]
    =================================
    0x6d00xb6: vb66d0 = RETURNDATASIZE 
    0x6d10xb6: vb66d1(0x0) = CONST 
    0x6d30xb6: RETURN vb66d1(0x0), vb66d0

    Begin block 0x6d40xb6
    prev=[0x6b50xb6], succ=[]
    =================================
    0x6d50xb6: vb66d5 = RETURNDATASIZE 
    0x6d60xb6: vb66d6(0x0) = CONST 
    0x6d80xb6: REVERT vb66d6(0x0), vb66d5

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xe9
    prev=[], succ=[0xfb, 0xff]
    =================================
    0xea: vea(0xa25) = CONST 
    0xed: ved(0x4) = CONST 
    0xf0: vf0 = CALLDATASIZE 
    0xf1: vf1 = SUB vf0, ved(0x4)
    0xf2: vf2(0x40) = CONST 
    0xf5: vf5 = LT vf1, vf2(0x40)
    0xf6: vf6 = ISZERO vf5
    0xf7: vf7(0xff) = CONST 
    0xfa: JUMPI vf7(0xff), vf6

    Begin block 0xfb
    prev=[0xe9], succ=[]
    =================================
    0xfb: vfb(0x0) = CONST 
    0xfe: REVERT vfb(0x0), vfb(0x0)

    Begin block 0xff
    prev=[0xe9], succ=[0x126, 0x12a]
    =================================
    0x100: v100(0x1) = CONST 
    0x102: v102(0x1) = CONST 
    0x104: v104(0xa0) = CONST 
    0x106: v106(0x10000000000000000000000000000000000000000) = SHL v104(0xa0), v102(0x1)
    0x107: v107(0xffffffffffffffffffffffffffffffffffffffff) = SUB v106(0x10000000000000000000000000000000000000000), v100(0x1)
    0x109: v109 = CALLDATALOAD ved(0x4)
    0x10a: v10a = AND v109, v107(0xffffffffffffffffffffffffffffffffffffffff)
    0x10e: v10e = ADD ved(0x4), vf1
    0x110: v110(0x40) = CONST 
    0x113: v113(0x44) = ADD ved(0x4), v110(0x40)
    0x114: v114(0x20) = CONST 
    0x117: v117(0x24) = ADD ved(0x4), v114(0x20)
    0x118: v118 = CALLDATALOAD v117(0x24)
    0x119: v119(0x100000000) = CONST 
    0x120: v120 = GT v118, v119(0x100000000)
    0x121: v121 = ISZERO v120
    0x122: v122(0x12a) = CONST 
    0x125: JUMPI v122(0x12a), v121

    Begin block 0x126
    prev=[0xff], succ=[]
    =================================
    0x126: v126(0x0) = CONST 
    0x129: REVERT v126(0x0), v126(0x0)

    Begin block 0x12a
    prev=[0xff], succ=[0x138, 0x13c]
    =================================
    0x12c: v12c = ADD ved(0x4), v118
    0x12e: v12e(0x20) = CONST 
    0x131: v131 = ADD v12c, v12e(0x20)
    0x132: v132 = GT v131, v10e
    0x133: v133 = ISZERO v132
    0x134: v134(0x13c) = CONST 
    0x137: JUMPI v134(0x13c), v133

    Begin block 0x138
    prev=[0x12a], succ=[]
    =================================
    0x138: v138(0x0) = CONST 
    0x13b: REVERT v138(0x0), v138(0x0)

    Begin block 0x13c
    prev=[0x12a], succ=[0x15a, 0x15e]
    =================================
    0x13e: v13e = CALLDATALOAD v12c
    0x140: v140(0x20) = CONST 
    0x142: v142 = ADD v140(0x20), v12c
    0x145: v145(0x1) = CONST 
    0x148: v148 = MUL v13e, v145(0x1)
    0x14a: v14a = ADD v142, v148
    0x14b: v14b = GT v14a, v10e
    0x14c: v14c(0x100000000) = CONST 
    0x153: v153 = GT v13e, v14c(0x100000000)
    0x154: v154 = OR v153, v14b
    0x155: v155 = ISZERO v154
    0x156: v156(0x15e) = CONST 
    0x159: JUMPI v156(0x15e), v155

    Begin block 0x15a
    prev=[0x13c], succ=[]
    =================================
    0x15a: v15a(0x0) = CONST 
    0x15d: REVERT v15a(0x0), v15a(0x0)

    Begin block 0x15e
    prev=[0x13c], succ=[0x281]
    =================================
    0x165: v165(0x281) = CONST 
    0x168: JUMP v165(0x281)

    Begin block 0x281
    prev=[0x15e], succ=[0x6d9B0x281]
    =================================
    0x282: v282(0x289) = CONST 
    0x285: v285(0x6d9) = CONST 
    0x288: JUMP v285(0x6d9)

    Begin block 0x6d9B0x281
    prev=[0x281], succ=[0x289]
    =================================
    0x6daS0x281: v6daV281(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6fbS0x281: v6fbV281 = SLOAD v6daV281(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6fdS0x281: JUMP v282(0x289)

    Begin block 0x289
    prev=[0x6d9B0x281], succ=[0x2a3, 0x365]
    =================================
    0x28a: v28a(0x1) = CONST 
    0x28c: v28c(0x1) = CONST 
    0x28e: v28e(0xa0) = CONST 
    0x290: v290(0x10000000000000000000000000000000000000000) = SHL v28e(0xa0), v28c(0x1)
    0x291: v291(0xffffffffffffffffffffffffffffffffffffffff) = SUB v290(0x10000000000000000000000000000000000000000), v28a(0x1)
    0x292: v292 = AND v291(0xffffffffffffffffffffffffffffffffffffffff), v6fbV281
    0x293: v293 = CALLER 
    0x294: v294(0x1) = CONST 
    0x296: v296(0x1) = CONST 
    0x298: v298(0xa0) = CONST 
    0x29a: v29a(0x10000000000000000000000000000000000000000) = SHL v298(0xa0), v296(0x1)
    0x29b: v29b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29a(0x10000000000000000000000000000000000000000), v294(0x1)
    0x29c: v29c = AND v29b(0xffffffffffffffffffffffffffffffffffffffff), v293
    0x29d: v29d = EQ v29c, v292
    0x29e: v29e = ISZERO v29d
    0x29f: v29f(0x365) = CONST 
    0x2a2: JUMPI v29f(0x365), v29e

    Begin block 0x2a3
    prev=[0x289], succ=[0x2ab]
    =================================
    0x2a3: v2a3(0x2ab) = CONST 
    0x2a7: v2a7(0x723) = CONST 
    0x2aa: CALLPRIVATE v2a7(0x723), v10a, v2a3(0x2ab)

    Begin block 0x2ab
    prev=[0x2a3], succ=[0x2ea, 0x30b]
    =================================
    0x2ac: v2ac(0x0) = CONST 
    0x2ae: v2ae = ADDRESS 
    0x2af: v2af(0x1) = CONST 
    0x2b1: v2b1(0x1) = CONST 
    0x2b3: v2b3(0xa0) = CONST 
    0x2b5: v2b5(0x10000000000000000000000000000000000000000) = SHL v2b3(0xa0), v2b1(0x1)
    0x2b6: v2b6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b5(0x10000000000000000000000000000000000000000), v2af(0x1)
    0x2b7: v2b7 = AND v2b6(0xffffffffffffffffffffffffffffffffffffffff), v2ae
    0x2b8: v2b8 = CALLVALUE 
    0x2bb: v2bb(0x40) = CONST 
    0x2bd: v2bd = MLOAD v2bb(0x40)
    0x2c4: CALLDATACOPY v2bd, v142, v13e
    0x2c5: v2c5(0x40) = CONST 
    0x2c7: v2c7 = MLOAD v2c5(0x40)
    0x2c9: v2c9 = ADD v2bd, v13e
    0x2cc: v2cc(0x0) = CONST 
    0x2d6: v2d6 = SUB v2c9, v2c7
    0x2da: v2da = GAS 
    0x2db: v2db = CALL v2da, v2b7, v2b8, v2c7, v2d6, v2c7, v2cc(0x0)
    0x2e0: v2e0 = RETURNDATASIZE 
    0x2e2: v2e2(0x0) = CONST 
    0x2e5: v2e5 = EQ v2e0, v2e2(0x0)
    0x2e6: v2e6(0x30b) = CONST 
    0x2e9: JUMPI v2e6(0x30b), v2e5

    Begin block 0x2ea
    prev=[0x2ab], succ=[0x310]
    =================================
    0x2ea: v2ea(0x40) = CONST 
    0x2ec: v2ec = MLOAD v2ea(0x40)
    0x2ef: v2ef(0x1f) = CONST 
    0x2f1: v2f1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v2ef(0x1f)
    0x2f2: v2f2(0x3f) = CONST 
    0x2f4: v2f4 = RETURNDATASIZE 
    0x2f5: v2f5 = ADD v2f4, v2f2(0x3f)
    0x2f6: v2f6 = AND v2f5, v2f1(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x2f8: v2f8 = ADD v2ec, v2f6
    0x2f9: v2f9(0x40) = CONST 
    0x2fb: MSTORE v2f9(0x40), v2f8
    0x2fc: v2fc = RETURNDATASIZE 
    0x2fe: MSTORE v2ec, v2fc
    0x2ff: v2ff = RETURNDATASIZE 
    0x300: v300(0x0) = CONST 
    0x302: v302(0x20) = CONST 
    0x305: v305 = ADD v2ec, v302(0x20)
    0x306: RETURNDATACOPY v305, v300(0x0), v2ff
    0x307: v307(0x310) = CONST 
    0x30a: JUMP v307(0x310)

    Begin block 0x310
    prev=[0x2ea, 0x30b], succ=[0x31a, 0x35f]
    =================================
    0x316: v316(0x35f) = CONST 
    0x319: JUMPI v316(0x35f), v2db

    Begin block 0x31a
    prev=[0x310], succ=[]
    =================================
    0x31a: v31a(0x40) = CONST 
    0x31d: v31d = MLOAD v31a(0x40)
    0x31e: v31e(0x461bcd) = CONST 
    0x322: v322(0xe5) = CONST 
    0x324: v324(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v322(0xe5), v31e(0x461bcd)
    0x326: MSTORE v31d, v324(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x327: v327(0x20) = CONST 
    0x329: v329(0x4) = CONST 
    0x32c: v32c = ADD v31d, v329(0x4)
    0x32d: MSTORE v32c, v327(0x20)
    0x32e: v32e(0x16) = CONST 
    0x330: v330(0x24) = CONST 
    0x333: v333 = ADD v31d, v330(0x24)
    0x334: MSTORE v333, v32e(0x16)
    0x335: v335(0x3ab833b930b232aa37a0b73221b0b63616b2b93937b9) = CONST 
    0x34c: v34c(0x51) = CONST 
    0x34e: v34e(0x75706772616465546f416e6443616c6c2d6572726f7200000000000000000000) = SHL v34c(0x51), v335(0x3ab833b930b232aa37a0b73221b0b63616b2b93937b9)
    0x34f: v34f(0x44) = CONST 
    0x352: v352 = ADD v31d, v34f(0x44)
    0x353: MSTORE v352, v34e(0x75706772616465546f416e6443616c6c2d6572726f7200000000000000000000)
    0x355: v355 = MLOAD v31a(0x40)
    0x359: v359(0x0) = SUB v31d, v355
    0x35a: v35a(0x64) = CONST 
    0x35c: v35c(0x64) = ADD v35a(0x64), v359(0x0)
    0x35e: REVERT v355, v35c(0x64)

    Begin block 0x35f
    prev=[0x310], succ=[0xbe2]
    =================================
    0x361: v361(0xbe2) = CONST 
    0x364: JUMP v361(0xbe2)

    Begin block 0xbe2
    prev=[0x35f], succ=[0xa25]
    =================================
    0xbe6: JUMP vea(0xa25)

    Begin block 0xa25
    prev=[0xbe2], succ=[]
    =================================
    0xa26: STOP 

    Begin block 0x30b
    prev=[0x2ab], succ=[0x310]
    =================================
    0x30c: v30c(0x60) = CONST 

    Begin block 0x365
    prev=[0x289], succ=[0x1f00xe9]
    =================================
    0x366: v366(0xc06) = CONST 
    0x369: v369(0x1f0) = CONST 
    0x36c: JUMP v369(0x1f0)

    Begin block 0x1f00xe9
    prev=[0x365], succ=[0x1f80xe9]
    =================================
    0x1f10xe9: ve91f1(0x1f8) = CONST 
    0x1f40xe9: ve91f4(0x630) = CONST 
    0x1f70xe9: CALLPRIVATE ve91f4(0x630), ve91f1(0x1f8)

    Begin block 0x1f80xe9
    prev=[0x1f00xe9], succ=[0x690B0x1f80xe9]
    =================================
    0x1f90xe9: ve91f9(0xb39) = CONST 
    0x1fc0xe9: ve91fc(0x203) = CONST 
    0x1ff0xe9: ve91ff(0x690) = CONST 
    0x2020xe9: JUMP ve91ff(0x690)

    Begin block 0x690B0x1f80xe9
    prev=[0x1f80xe9], succ=[0x2030xe9]
    =================================
    0x691S0x1f80xe9: v691V1f8e9(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x6b2S0x1f80xe9: v6b2V1f8e9 = SLOAD v691V1f8e9(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x6b4S0x1f80xe9: JUMP ve91fc(0x203)

    Begin block 0x2030xe9
    prev=[0x690B0x1f80xe9], succ=[0x6b50xe9]
    =================================
    0x2040xe9: ve9204(0x6b5) = CONST 
    0x2070xe9: JUMP ve9204(0x6b5)

    Begin block 0x6b50xe9
    prev=[0x2030xe9], succ=[0x6d00xe9, 0x6d40xe9]
    =================================
    0x6b60xe9: ve96b6 = CALLDATASIZE 
    0x6b70xe9: ve96b7(0x0) = CONST 
    0x6ba0xe9: CALLDATACOPY ve96b7(0x0), ve96b7(0x0), ve96b6
    0x6bb0xe9: ve96bb(0x0) = CONST 
    0x6be0xe9: ve96be = CALLDATASIZE 
    0x6bf0xe9: ve96bf(0x0) = CONST 
    0x6c20xe9: ve96c2 = GAS 
    0x6c30xe9: ve96c3 = DELEGATECALL ve96c2, v6b2V1f8e9, ve96bf(0x0), ve96be, ve96bb(0x0), ve96bb(0x0)
    0x6c40xe9: ve96c4 = RETURNDATASIZE 
    0x6c50xe9: ve96c5(0x0) = CONST 
    0x6c80xe9: RETURNDATACOPY ve96c5(0x0), ve96c5(0x0), ve96c4
    0x6cb0xe9: ve96cb = ISZERO ve96c3
    0x6cc0xe9: ve96cc(0x6d4) = CONST 
    0x6cf0xe9: JUMPI ve96cc(0x6d4), ve96cb

    Begin block 0x6d00xe9
    prev=[0x6b50xe9], succ=[]
    =================================
    0x6d00xe9: ve96d0 = RETURNDATASIZE 
    0x6d10xe9: ve96d1(0x0) = CONST 
    0x6d30xe9: RETURN ve96d1(0x0), ve96d0

    Begin block 0x6d40xe9
    prev=[0x6b50xe9], succ=[]
    =================================
    0x6d50xe9: ve96d5 = RETURNDATASIZE 
    0x6d60xe9: ve96d6(0x0) = CONST 
    0x6d80xe9: REVERT ve96d6(0x0), ve96d5

}

