function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x488]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x47a: v47a(0x488) = CONST 
    0x47b: JUMPI v47a(0x488), v8

    Begin block 0xd
    prev=[0x0], succ=[0x48b, 0x27]
    =================================
    0xd: vd(0xffffffff) = CONST 
    0x12: v12(0xe0) = CONST 
    0x14: v14(0x2) = CONST 
    0x16: v16(0x100000000000000000000000000000000000000000000000000000000) = EXP v14(0x2), v12(0xe0)
    0x17: v17(0x0) = CONST 
    0x19: v19 = CALLDATALOAD v17(0x0)
    0x1a: v1a = DIV v19, v16(0x100000000000000000000000000000000000000000000000000000000)
    0x1b: v1b = AND v1a, vd(0xffffffff)
    0x1c: v1c(0x3ad06d16) = CONST 
    0x22: v22 = EQ v1b, v1c(0x3ad06d16)
    0x47c: v47c(0x48b) = CONST 
    0x47d: JUMPI v47c(0x48b), v22

    Begin block 0x48b
    prev=[0xd], succ=[]
    =================================
    0x48c: v48c(0xa9) = CONST 
    0x48d: CALLPRIVATE v48c(0xa9)

    Begin block 0x27
    prev=[0xd], succ=[0x48e, 0x32]
    =================================
    0x28: v28(0x54fd4d50) = CONST 
    0x2d: v2d = EQ v28(0x54fd4d50), v1b
    0x47e: v47e(0x48e) = CONST 
    0x47f: JUMPI v47e(0x48e), v2d

    Begin block 0x48e
    prev=[0x27], succ=[]
    =================================
    0x48f: v48f(0xcf) = CONST 
    0x490: CALLPRIVATE v48f(0xcf)

    Begin block 0x32
    prev=[0x27], succ=[0x491, 0x3d]
    =================================
    0x33: v33(0x5c60da1b) = CONST 
    0x38: v38 = EQ v33(0x5c60da1b), v1b
    0x480: v480(0x491) = CONST 
    0x481: JUMPI v480(0x491), v38

    Begin block 0x491
    prev=[0x32], succ=[]
    =================================
    0x492: v492(0xf6) = CONST 
    0x493: CALLPRIVATE v492(0xf6)

    Begin block 0x3d
    prev=[0x32], succ=[0x494, 0x48]
    =================================
    0x3e: v3e(0x6fde8202) = CONST 
    0x43: v43 = EQ v3e(0x6fde8202), v1b
    0x482: v482(0x494) = CONST 
    0x483: JUMPI v482(0x494), v43

    Begin block 0x494
    prev=[0x3d], succ=[]
    =================================
    0x495: v495(0x127) = CONST 
    0x496: CALLPRIVATE v495(0x127)

    Begin block 0x48
    prev=[0x3d], succ=[0x497, 0x53]
    =================================
    0x49: v49(0xa9c45fcb) = CONST 
    0x4e: v4e = EQ v49(0xa9c45fcb), v1b
    0x484: v484(0x497) = CONST 
    0x485: JUMPI v484(0x497), v4e

    Begin block 0x497
    prev=[0x48], succ=[]
    =================================
    0x498: v498(0x13c) = CONST 
    0x499: CALLPRIVATE v498(0x13c)

    Begin block 0x53
    prev=[0x48], succ=[0x488, 0x49a]
    =================================
    0x54: v54(0xf1739cae) = CONST 
    0x59: v59 = EQ v54(0xf1739cae), v1b
    0x486: v486(0x49a) = CONST 
    0x487: JUMPI v486(0x49a), v59

    Begin block 0x488
    prev=[0x0, 0x53], succ=[]
    =================================
    0x489: v489(0x5e) = CONST 
    0x48a: CALLPRIVATE v489(0x5e)

    Begin block 0x49a
    prev=[0x53], succ=[]
    =================================
    0x49b: v49b(0x160) = CONST 
    0x49c: CALLPRIVATE v49b(0x160)

}

function upgradeabilityOwner()() public {
    Begin block 0x127
    prev=[], succ=[0x12f, 0x133]
    =================================
    0x128: v128 = CALLVALUE 
    0x12a: v12a = ISZERO v128
    0x12b: v12b(0x133) = CONST 
    0x12e: JUMPI v12b(0x133), v12a

    Begin block 0x12f
    prev=[0x127], succ=[]
    =================================
    0x12f: v12f(0x0) = CONST 
    0x132: REVERT v12f(0x0), v12f(0x0)

    Begin block 0x133
    prev=[0x127], succ=[0x1c0B0x133]
    =================================
    0x135: v135(0x41c) = CONST 
    0x138: v138(0x1c0) = CONST 
    0x13b: JUMP v138(0x1c0)

    Begin block 0x1c0B0x133
    prev=[0x133], succ=[0x41c]
    =================================
    0x1c1S0x133: v1c1V133(0x6) = CONST 
    0x1c3S0x133: v1c3V133 = SLOAD v1c1V133(0x6)
    0x1c4S0x133: v1c4V133(0x1) = CONST 
    0x1c6S0x133: v1c6V133(0xa0) = CONST 
    0x1c8S0x133: v1c8V133(0x2) = CONST 
    0x1caS0x133: v1caV133(0x10000000000000000000000000000000000000000) = EXP v1c8V133(0x2), v1c6V133(0xa0)
    0x1cbS0x133: v1cbV133(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1caV133(0x10000000000000000000000000000000000000000), v1c4V133(0x1)
    0x1ccS0x133: v1ccV133 = AND v1cbV133(0xffffffffffffffffffffffffffffffffffffffff), v1c3V133
    0x1ceS0x133: JUMP v135(0x41c)

    Begin block 0x41c
    prev=[0x1c0B0x133], succ=[]
    =================================
    0x41d: v41d(0x40) = CONST 
    0x420: v420 = MLOAD v41d(0x40)
    0x421: v421(0x1) = CONST 
    0x423: v423(0xa0) = CONST 
    0x425: v425(0x2) = CONST 
    0x427: v427(0x10000000000000000000000000000000000000000) = EXP v425(0x2), v423(0xa0)
    0x428: v428(0xffffffffffffffffffffffffffffffffffffffff) = SUB v427(0x10000000000000000000000000000000000000000), v421(0x1)
    0x42b: v42b = AND v1ccV133, v428(0xffffffffffffffffffffffffffffffffffffffff)
    0x42d: MSTORE v420, v42b
    0x42e: v42e = MLOAD v41d(0x40)
    0x432: v432(0x0) = SUB v420, v42e
    0x433: v433(0x20) = CONST 
    0x435: v435(0x20) = ADD v433(0x20), v432(0x0)
    0x437: RETURN v42e, v435(0x20)

}

function upgradeToAndCall(uint256,address,bytes)() public {
    Begin block 0x13c
    prev=[], succ=[0x1cfB0x13c]
    =================================
    0x13d: v13d(0x457) = CONST 
    0x140: v140(0x4) = CONST 
    0x143: v143 = CALLDATALOAD v140(0x4)
    0x145: v145(0x24) = CONST 
    0x148: v148 = CALLDATALOAD v145(0x24)
    0x149: v149(0x1) = CONST 
    0x14b: v14b(0xa0) = CONST 
    0x14d: v14d(0x2) = CONST 
    0x14f: v14f(0x10000000000000000000000000000000000000000) = EXP v14d(0x2), v14b(0xa0)
    0x150: v150(0xffffffffffffffffffffffffffffffffffffffff) = SUB v14f(0x10000000000000000000000000000000000000000), v149(0x1)
    0x151: v151 = AND v150(0xffffffffffffffffffffffffffffffffffffffff), v148
    0x153: v153(0x44) = CONST 
    0x155: v155 = CALLDATALOAD v153(0x44)
    0x158: v158 = ADD v155, v145(0x24)
    0x15a: v15a = ADD v155, v140(0x4)
    0x15b: v15b = CALLDATALOAD v15a
    0x15c: v15c(0x1cf) = CONST 
    0x15f: JUMP v15c(0x1cf), v15b, v158, v151, v143, v13d(0x457)

    Begin block 0x1cfB0x13c
    prev=[0x13c], succ=[0x1c0B0x1cfB0x13c]
    =================================
    0x1d0S0x13c: v1d0V13c(0x1d7) = CONST 
    0x1d3S0x13c: v1d3V13c(0x1c0) = CONST 
    0x1d6S0x13c: JUMP v1d3V13c(0x1c0)

    Begin block 0x1c0B0x1cfB0x13c
    prev=[0x1cfB0x13c], succ=[0x1d7B0x13c]
    =================================
    0x1c1S0x1cfS0x13c: v1c1V1cfV13c(0x6) = CONST 
    0x1c3S0x1cfS0x13c: v1c3V1cfV13c = SLOAD v1c1V1cfV13c(0x6)
    0x1c4S0x1cfS0x13c: v1c4V1cfV13c(0x1) = CONST 
    0x1c6S0x1cfS0x13c: v1c6V1cfV13c(0xa0) = CONST 
    0x1c8S0x1cfS0x13c: v1c8V1cfV13c(0x2) = CONST 
    0x1caS0x1cfS0x13c: v1caV1cfV13c(0x10000000000000000000000000000000000000000) = EXP v1c8V1cfV13c(0x2), v1c6V1cfV13c(0xa0)
    0x1cbS0x1cfS0x13c: v1cbV1cfV13c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1caV1cfV13c(0x10000000000000000000000000000000000000000), v1c4V1cfV13c(0x1)
    0x1ccS0x1cfS0x13c: v1ccV1cfV13c = AND v1cbV1cfV13c(0xffffffffffffffffffffffffffffffffffffffff), v1c3V1cfV13c
    0x1ceS0x1cfS0x13c: JUMP v1d0V13c(0x1d7)

    Begin block 0x1d7B0x13c
    prev=[0x1c0B0x1cfB0x13c], succ=[0x1e7B0x13c, 0x1ebB0x13c]
    =================================
    0x1d8S0x13c: v1d8V13c(0x1) = CONST 
    0x1daS0x13c: v1daV13c(0xa0) = CONST 
    0x1dcS0x13c: v1dcV13c(0x2) = CONST 
    0x1deS0x13c: v1deV13c(0x10000000000000000000000000000000000000000) = EXP v1dcV13c(0x2), v1daV13c(0xa0)
    0x1dfS0x13c: v1dfV13c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1deV13c(0x10000000000000000000000000000000000000000), v1d8V13c(0x1)
    0x1e0S0x13c: v1e0V13c = AND v1dfV13c(0xffffffffffffffffffffffffffffffffffffffff), v1ccV1cfV13c
    0x1e1S0x13c: v1e1V13c = CALLER 
    0x1e2S0x13c: v1e2V13c = EQ v1e1V13c, v1e0V13c
    0x1e3S0x13c: v1e3V13c(0x1eb) = CONST 
    0x1e6S0x13c: JUMPI v1e3V13c(0x1eb), v1e2V13c

    Begin block 0x1e7B0x13c
    prev=[0x1d7B0x13c], succ=[]
    =================================
    0x1e7S0x13c: v1e7V13c(0x0) = CONST 
    0x1eaS0x13c: REVERT v1e7V13c(0x0), v1e7V13c(0x0)

    Begin block 0x1ebB0x13c
    prev=[0x1d7B0x13c], succ=[0x1f5B0x13c]
    =================================
    0x1ecS0x13c: v1ecV13c(0x1f5) = CONST 
    0x1f1S0x13c: v1f1V13c(0x190) = CONST 
    0x1f4S0x13c: CALLPRIVATE v1f1V13c(0x190), v151, v143, v1ecV13c(0x1f5)

    Begin block 0x1f5B0x13c
    prev=[0x1ebB0x13c], succ=[0x22dB0x13c, 0x231B0x13c]
    =================================
    0x1f6S0x13c: v1f6V13c = ADDRESS 
    0x1f7S0x13c: v1f7V13c(0x1) = CONST 
    0x1f9S0x13c: v1f9V13c(0xa0) = CONST 
    0x1fbS0x13c: v1fbV13c(0x2) = CONST 
    0x1fdS0x13c: v1fdV13c(0x10000000000000000000000000000000000000000) = EXP v1fbV13c(0x2), v1f9V13c(0xa0)
    0x1feS0x13c: v1feV13c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1fdV13c(0x10000000000000000000000000000000000000000), v1f7V13c(0x1)
    0x1ffS0x13c: v1ffV13c = AND v1feV13c(0xffffffffffffffffffffffffffffffffffffffff), v1f6V13c
    0x200S0x13c: v200V13c = CALLVALUE 
    0x203S0x13c: v203V13c(0x40) = CONST 
    0x205S0x13c: v205V13c = MLOAD v203V13c(0x40)
    0x20cS0x13c: CALLDATACOPY v205V13c, v158, v15b
    0x20eS0x13c: v20eV13c = ADD v205V13c, v15b
    0x216S0x13c: v216V13c(0x0) = CONST 
    0x218S0x13c: v218V13c(0x40) = CONST 
    0x21aS0x13c: v21aV13c = MLOAD v218V13c(0x40)
    0x21dS0x13c: v21dV13c = SUB v20eV13c, v21aV13c
    0x221S0x13c: v221V13c = GAS 
    0x222S0x13c: v222V13c = CALL v221V13c, v1ffV13c, v200V13c, v21aV13c, v21dV13c, v21aV13c, v216V13c(0x0)
    0x227S0x13c: v227V13c = ISZERO v222V13c
    0x228S0x13c: v228V13c = ISZERO v227V13c
    0x229S0x13c: v229V13c(0x231) = CONST 
    0x22cS0x13c: JUMPI v229V13c(0x231), v228V13c

    Begin block 0x22dB0x13c
    prev=[0x1f5B0x13c], succ=[]
    =================================
    0x22dS0x13c: v22dV13c(0x0) = CONST 
    0x230S0x13c: REVERT v22dV13c(0x0), v22dV13c(0x0)

    Begin block 0x231B0x13c
    prev=[0x1f5B0x13c], succ=[0x457]
    =================================
    0x236S0x13c: JUMP v13d(0x457)

    Begin block 0x457
    prev=[0x231B0x13c], succ=[]
    =================================
    0x458: STOP 

}

function transferProxyOwnership(address)() public {
    Begin block 0x160
    prev=[], succ=[0x168, 0x16c]
    =================================
    0x161: v161 = CALLVALUE 
    0x163: v163 = ISZERO v161
    0x164: v164(0x16c) = CONST 
    0x167: JUMPI v164(0x16c), v163

    Begin block 0x168
    prev=[0x160], succ=[]
    =================================
    0x168: v168(0x0) = CONST 
    0x16b: REVERT v168(0x0), v168(0x0)

    Begin block 0x16c
    prev=[0x160], succ=[0x237B0x16c]
    =================================
    0x16e: v16e(0x478) = CONST 
    0x171: v171(0x1) = CONST 
    0x173: v173(0xa0) = CONST 
    0x175: v175(0x2) = CONST 
    0x177: v177(0x10000000000000000000000000000000000000000) = EXP v175(0x2), v173(0xa0)
    0x178: v178(0xffffffffffffffffffffffffffffffffffffffff) = SUB v177(0x10000000000000000000000000000000000000000), v171(0x1)
    0x179: v179(0x4) = CONST 
    0x17b: v17b = CALLDATALOAD v179(0x4)
    0x17c: v17c = AND v17b, v178(0xffffffffffffffffffffffffffffffffffffffff)
    0x17d: v17d(0x237) = CONST 
    0x180: JUMP v17d(0x237), v17c, v16e(0x478)

    Begin block 0x237B0x16c
    prev=[0x16c], succ=[0x1c0B0x237B0x16c]
    =================================
    0x238S0x16c: v238V16c(0x23f) = CONST 
    0x23bS0x16c: v23bV16c(0x1c0) = CONST 
    0x23eS0x16c: JUMP v23bV16c(0x1c0)

    Begin block 0x1c0B0x237B0x16c
    prev=[0x237B0x16c], succ=[0x23fB0x16c]
    =================================
    0x1c1S0x237S0x16c: v1c1V237V16c(0x6) = CONST 
    0x1c3S0x237S0x16c: v1c3V237V16c = SLOAD v1c1V237V16c(0x6)
    0x1c4S0x237S0x16c: v1c4V237V16c(0x1) = CONST 
    0x1c6S0x237S0x16c: v1c6V237V16c(0xa0) = CONST 
    0x1c8S0x237S0x16c: v1c8V237V16c(0x2) = CONST 
    0x1caS0x237S0x16c: v1caV237V16c(0x10000000000000000000000000000000000000000) = EXP v1c8V237V16c(0x2), v1c6V237V16c(0xa0)
    0x1cbS0x237S0x16c: v1cbV237V16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1caV237V16c(0x10000000000000000000000000000000000000000), v1c4V237V16c(0x1)
    0x1ccS0x237S0x16c: v1ccV237V16c = AND v1cbV237V16c(0xffffffffffffffffffffffffffffffffffffffff), v1c3V237V16c
    0x1ceS0x237S0x16c: JUMP v238V16c(0x23f)

    Begin block 0x23fB0x16c
    prev=[0x1c0B0x237B0x16c], succ=[0x24fB0x16c, 0x253B0x16c]
    =================================
    0x240S0x16c: v240V16c(0x1) = CONST 
    0x242S0x16c: v242V16c(0xa0) = CONST 
    0x244S0x16c: v244V16c(0x2) = CONST 
    0x246S0x16c: v246V16c(0x10000000000000000000000000000000000000000) = EXP v244V16c(0x2), v242V16c(0xa0)
    0x247S0x16c: v247V16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v246V16c(0x10000000000000000000000000000000000000000), v240V16c(0x1)
    0x248S0x16c: v248V16c = AND v247V16c(0xffffffffffffffffffffffffffffffffffffffff), v1ccV237V16c
    0x249S0x16c: v249V16c = CALLER 
    0x24aS0x16c: v24aV16c = EQ v249V16c, v248V16c
    0x24bS0x16c: v24bV16c(0x253) = CONST 
    0x24eS0x16c: JUMPI v24bV16c(0x253), v24aV16c

    Begin block 0x24fB0x16c
    prev=[0x23fB0x16c], succ=[]
    =================================
    0x24fS0x16c: v24fV16c(0x0) = CONST 
    0x252S0x16c: REVERT v24fV16c(0x0), v24fV16c(0x0)

    Begin block 0x253B0x16c
    prev=[0x23fB0x16c], succ=[0x264B0x16c, 0x268B0x16c]
    =================================
    0x254S0x16c: v254V16c(0x1) = CONST 
    0x256S0x16c: v256V16c(0xa0) = CONST 
    0x258S0x16c: v258V16c(0x2) = CONST 
    0x25aS0x16c: v25aV16c(0x10000000000000000000000000000000000000000) = EXP v258V16c(0x2), v256V16c(0xa0)
    0x25bS0x16c: v25bV16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v25aV16c(0x10000000000000000000000000000000000000000), v254V16c(0x1)
    0x25dS0x16c: v25dV16c = AND v17c, v25bV16c(0xffffffffffffffffffffffffffffffffffffffff)
    0x25eS0x16c: v25eV16c = ISZERO v25dV16c
    0x25fS0x16c: v25fV16c = ISZERO v25eV16c
    0x260S0x16c: v260V16c(0x268) = CONST 
    0x263S0x16c: JUMPI v260V16c(0x268), v25fV16c

    Begin block 0x264B0x16c
    prev=[0x253B0x16c], succ=[]
    =================================
    0x264S0x16c: v264V16c(0x0) = CONST 
    0x267S0x16c: REVERT v264V16c(0x0), v264V16c(0x0)

    Begin block 0x268B0x16c
    prev=[0x253B0x16c], succ=[0x1c0B0x268B0x16c]
    =================================
    0x269S0x16c: v269V16c(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9) = CONST 
    0x28aS0x16c: v28aV16c(0x291) = CONST 
    0x28dS0x16c: v28dV16c(0x1c0) = CONST 
    0x290S0x16c: JUMP v28dV16c(0x1c0)

    Begin block 0x1c0B0x268B0x16c
    prev=[0x268B0x16c], succ=[0x291B0x16c]
    =================================
    0x1c1S0x268S0x16c: v1c1V268V16c(0x6) = CONST 
    0x1c3S0x268S0x16c: v1c3V268V16c = SLOAD v1c1V268V16c(0x6)
    0x1c4S0x268S0x16c: v1c4V268V16c(0x1) = CONST 
    0x1c6S0x268S0x16c: v1c6V268V16c(0xa0) = CONST 
    0x1c8S0x268S0x16c: v1c8V268V16c(0x2) = CONST 
    0x1caS0x268S0x16c: v1caV268V16c(0x10000000000000000000000000000000000000000) = EXP v1c8V268V16c(0x2), v1c6V268V16c(0xa0)
    0x1cbS0x268S0x16c: v1cbV268V16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1caV268V16c(0x10000000000000000000000000000000000000000), v1c4V268V16c(0x1)
    0x1ccS0x268S0x16c: v1ccV268V16c = AND v1cbV268V16c(0xffffffffffffffffffffffffffffffffffffffff), v1c3V268V16c
    0x1ceS0x268S0x16c: JUMP v28aV16c(0x291)

    Begin block 0x291B0x16c
    prev=[0x1c0B0x268B0x16c], succ=[0x357B0x16c]
    =================================
    0x292S0x16c: v292V16c(0x40) = CONST 
    0x295S0x16c: v295V16c = MLOAD v292V16c(0x40)
    0x296S0x16c: v296V16c(0x1) = CONST 
    0x298S0x16c: v298V16c(0xa0) = CONST 
    0x29aS0x16c: v29aV16c(0x2) = CONST 
    0x29cS0x16c: v29cV16c(0x10000000000000000000000000000000000000000) = EXP v29aV16c(0x2), v298V16c(0xa0)
    0x29dS0x16c: v29dV16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v29cV16c(0x10000000000000000000000000000000000000000), v296V16c(0x1)
    0x2a0S0x16c: v2a0V16c = AND v29dV16c(0xffffffffffffffffffffffffffffffffffffffff), v1ccV268V16c
    0x2a2S0x16c: MSTORE v295V16c, v2a0V16c
    0x2a5S0x16c: v2a5V16c = AND v17c, v29dV16c(0xffffffffffffffffffffffffffffffffffffffff)
    0x2a6S0x16c: v2a6V16c(0x20) = CONST 
    0x2a9S0x16c: v2a9V16c = ADD v295V16c, v2a6V16c(0x20)
    0x2aaS0x16c: MSTORE v2a9V16c, v2a5V16c
    0x2acS0x16c: v2acV16c = MLOAD v292V16c(0x40)
    0x2b0S0x16c: v2b0V16c(0x0) = SUB v295V16c, v2acV16c
    0x2b1S0x16c: v2b1V16c(0x40) = ADD v2b0V16c(0x0), v292V16c(0x40)
    0x2b3S0x16c: LOG1 v2acV16c, v2b1V16c(0x40), v269V16c(0x5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9)
    0x2b4S0x16c: v2b4V16c(0x2bc) = CONST 
    0x2b8S0x16c: v2b8V16c(0x357) = CONST 
    0x2bbS0x16c: JUMP v2b8V16c(0x357)

    Begin block 0x357B0x16c
    prev=[0x291B0x16c], succ=[0x2bcB0x16c]
    =================================
    0x358S0x16c: v358V16c(0x6) = CONST 
    0x35bS0x16c: v35bV16c = SLOAD v358V16c(0x6)
    0x35cS0x16c: v35cV16c(0x1) = CONST 
    0x35eS0x16c: v35eV16c(0xa0) = CONST 
    0x360S0x16c: v360V16c(0x2) = CONST 
    0x362S0x16c: v362V16c(0x10000000000000000000000000000000000000000) = EXP v360V16c(0x2), v35eV16c(0xa0)
    0x363S0x16c: v363V16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v362V16c(0x10000000000000000000000000000000000000000), v35cV16c(0x1)
    0x364S0x16c: v364V16c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v363V16c(0xffffffffffffffffffffffffffffffffffffffff)
    0x365S0x16c: v365V16c = AND v364V16c(0xffffffffffffffffffffffff0000000000000000000000000000000000000000), v35bV16c
    0x366S0x16c: v366V16c(0x1) = CONST 
    0x368S0x16c: v368V16c(0xa0) = CONST 
    0x36aS0x16c: v36aV16c(0x2) = CONST 
    0x36cS0x16c: v36cV16c(0x10000000000000000000000000000000000000000) = EXP v36aV16c(0x2), v368V16c(0xa0)
    0x36dS0x16c: v36dV16c(0xffffffffffffffffffffffffffffffffffffffff) = SUB v36cV16c(0x10000000000000000000000000000000000000000), v366V16c(0x1)
    0x371S0x16c: v371V16c = AND v36dV16c(0xffffffffffffffffffffffffffffffffffffffff), v17c
    0x375S0x16c: v375V16c = OR v371V16c, v365V16c
    0x377S0x16c: SSTORE v358V16c(0x6), v375V16c
    0x378S0x16c: JUMP v2b4V16c(0x2bc)

    Begin block 0x2bcB0x16c
    prev=[0x357B0x16c], succ=[0x478]
    =================================
    0x2beS0x16c: JUMP v16e(0x478)

    Begin block 0x478
    prev=[0x2bcB0x16c], succ=[]
    =================================
    0x479: STOP 

}

function 0x190(0x190arg0x0, 0x190arg0x1, 0x190arg0x2) private {
    Begin block 0x190
    prev=[], succ=[0x1c0B0x190]
    =================================
    0x191: v191(0x198) = CONST 
    0x194: v194(0x1c0) = CONST 
    0x197: JUMP v194(0x1c0)

    Begin block 0x1c0B0x190
    prev=[0x190], succ=[0x198]
    =================================
    0x1c1S0x190: v1c1V190(0x6) = CONST 
    0x1c3S0x190: v1c3V190 = SLOAD v1c1V190(0x6)
    0x1c4S0x190: v1c4V190(0x1) = CONST 
    0x1c6S0x190: v1c6V190(0xa0) = CONST 
    0x1c8S0x190: v1c8V190(0x2) = CONST 
    0x1caS0x190: v1caV190(0x10000000000000000000000000000000000000000) = EXP v1c8V190(0x2), v1c6V190(0xa0)
    0x1cbS0x190: v1cbV190(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1caV190(0x10000000000000000000000000000000000000000), v1c4V190(0x1)
    0x1ccS0x190: v1ccV190 = AND v1cbV190(0xffffffffffffffffffffffffffffffffffffffff), v1c3V190
    0x1ceS0x190: JUMP v191(0x198)

    Begin block 0x198
    prev=[0x1c0B0x190], succ=[0x1a8, 0x1ac]
    =================================
    0x199: v199(0x1) = CONST 
    0x19b: v19b(0xa0) = CONST 
    0x19d: v19d(0x2) = CONST 
    0x19f: v19f(0x10000000000000000000000000000000000000000) = EXP v19d(0x2), v19b(0xa0)
    0x1a0: v1a0(0xffffffffffffffffffffffffffffffffffffffff) = SUB v19f(0x10000000000000000000000000000000000000000), v199(0x1)
    0x1a1: v1a1 = AND v1a0(0xffffffffffffffffffffffffffffffffffffffff), v1ccV190
    0x1a2: v1a2 = CALLER 
    0x1a3: v1a3 = EQ v1a2, v1a1
    0x1a4: v1a4(0x1ac) = CONST 
    0x1a7: JUMPI v1a4(0x1ac), v1a3

    Begin block 0x1a8
    prev=[0x198], succ=[]
    =================================
    0x1a8: v1a8(0x0) = CONST 
    0x1ab: REVERT v1a8(0x0), v1a8(0x0)

    Begin block 0x1ac
    prev=[0x198], succ=[0x2bf]
    =================================
    0x1ad: v1ad(0x1b6) = CONST 
    0x1b2: v1b2(0x2bf) = CONST 
    0x1b5: JUMP v1b2(0x2bf)

    Begin block 0x2bf
    prev=[0x1ac], succ=[0x2d6, 0x2da]
    =================================
    0x2c0: v2c0(0x8) = CONST 
    0x2c2: v2c2 = SLOAD v2c0(0x8)
    0x2c3: v2c3(0x1) = CONST 
    0x2c5: v2c5(0xa0) = CONST 
    0x2c7: v2c7(0x2) = CONST 
    0x2c9: v2c9(0x10000000000000000000000000000000000000000) = EXP v2c7(0x2), v2c5(0xa0)
    0x2ca: v2ca(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2c9(0x10000000000000000000000000000000000000000), v2c3(0x1)
    0x2cd: v2cd = AND v2ca(0xffffffffffffffffffffffffffffffffffffffff), v190arg0
    0x2cf: v2cf = AND v2c2, v2ca(0xffffffffffffffffffffffffffffffffffffffff)
    0x2d0: v2d0 = EQ v2cf, v2cd
    0x2d1: v2d1 = ISZERO v2d0
    0x2d2: v2d2(0x2da) = CONST 
    0x2d5: JUMPI v2d2(0x2da), v2d1

    Begin block 0x2d6
    prev=[0x2bf], succ=[]
    =================================
    0x2d6: v2d6(0x0) = CONST 
    0x2d9: REVERT v2d6(0x0), v2d6(0x0)

    Begin block 0x2da
    prev=[0x2bf], succ=[0x379]
    =================================
    0x2db: v2db(0x2e3) = CONST 
    0x2df: v2df(0x379) = CONST 
    0x2e2: JUMP v2df(0x379)

    Begin block 0x379
    prev=[0x2da], succ=[0x2e3]
    =================================
    0x37a: v37a(0x0) = CONST 
    0x37d: v37d = EXTCODESIZE v190arg0
    0x37e: v37e = GT v37d, v37a(0x0)
    0x380: JUMP v2db(0x2e3)

    Begin block 0x2e3
    prev=[0x379], succ=[0x2ea, 0x2ee]
    =================================
    0x2e4: v2e4 = ISZERO v37e
    0x2e5: v2e5 = ISZERO v2e4
    0x2e6: v2e6(0x2ee) = CONST 
    0x2e9: JUMPI v2e6(0x2ee), v2e5

    Begin block 0x2ea
    prev=[0x2e3], succ=[]
    =================================
    0x2ea: v2ea(0x0) = CONST 
    0x2ed: REVERT v2ea(0x0), v2ea(0x0)

    Begin block 0x2ee
    prev=[0x2e3], succ=[0x2f8, 0x2fc]
    =================================
    0x2ef: v2ef(0x7) = CONST 
    0x2f1: v2f1 = SLOAD v2ef(0x7)
    0x2f3: v2f3 = GT v190arg1, v2f1
    0x2f4: v2f4(0x2fc) = CONST 
    0x2f7: JUMPI v2f4(0x2fc), v2f3

    Begin block 0x2f8
    prev=[0x2ee], succ=[]
    =================================
    0x2f8: v2f8(0x0) = CONST 
    0x2fb: REVERT v2f8(0x0), v2f8(0x0)

    Begin block 0x2fc
    prev=[0x2ee], succ=[0x1b6]
    =================================
    0x2fd: v2fd(0x7) = CONST 
    0x301: SSTORE v2fd(0x7), v190arg1
    0x302: v302(0x8) = CONST 
    0x305: v305 = SLOAD v302(0x8)
    0x306: v306(0x1) = CONST 
    0x308: v308(0xa0) = CONST 
    0x30a: v30a(0x2) = CONST 
    0x30c: v30c(0x10000000000000000000000000000000000000000) = EXP v30a(0x2), v308(0xa0)
    0x30d: v30d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v30c(0x10000000000000000000000000000000000000000), v306(0x1)
    0x30f: v30f = AND v190arg0, v30d(0xffffffffffffffffffffffffffffffffffffffff)
    0x310: v310(0x1) = CONST 
    0x312: v312(0xa0) = CONST 
    0x314: v314(0x2) = CONST 
    0x316: v316(0x10000000000000000000000000000000000000000) = EXP v314(0x2), v312(0xa0)
    0x317: v317(0xffffffffffffffffffffffffffffffffffffffff) = SUB v316(0x10000000000000000000000000000000000000000), v310(0x1)
    0x318: v318(0xffffffffffffffffffffffff0000000000000000000000000000000000000000) = NOT v317(0xffffffffffffffffffffffffffffffffffffffff)
    0x31b: v31b = AND v305, v318(0xffffffffffffffffffffffff0000000000000000000000000000000000000000)
    0x31d: v31d = OR v30f, v31b
    0x320: SSTORE v302(0x8), v31d
    0x321: v321(0x40) = CONST 
    0x324: v324 = MLOAD v321(0x40)
    0x327: MSTORE v324, v190arg1
    0x329: v329 = MLOAD v321(0x40)
    0x32a: v32a(0x4289d6195cf3c2d2174adf98d0e19d4d2d08887995b99cb7b100e7ffe795820e) = CONST 
    0x34e: v34e(0x0) = SUB v324, v329
    0x34f: v34f(0x20) = CONST 
    0x351: v351(0x20) = ADD v34f(0x20), v34e(0x0)
    0x353: LOG2 v329, v351(0x20), v32a(0x4289d6195cf3c2d2174adf98d0e19d4d2d08887995b99cb7b100e7ffe795820e), v30f
    0x356: JUMP v1ad(0x1b6)

    Begin block 0x1b6
    prev=[0x2fc], succ=[]
    =================================
    0x1b9: RETURNPRIVATE v190arg2

}

function fallback()() public {
    Begin block 0x5e
    prev=[], succ=[0x181B0x5e]
    =================================
    0x5f: v5f(0x0) = CONST 
    0x61: v61(0x68) = CONST 
    0x64: v64(0x181) = CONST 
    0x67: JUMP v64(0x181)

    Begin block 0x181B0x5e
    prev=[0x5e], succ=[0x68]
    =================================
    0x182S0x5e: v182V5e(0x8) = CONST 
    0x184S0x5e: v184V5e = SLOAD v182V5e(0x8)
    0x185S0x5e: v185V5e(0x1) = CONST 
    0x187S0x5e: v187V5e(0xa0) = CONST 
    0x189S0x5e: v189V5e(0x2) = CONST 
    0x18bS0x5e: v18bV5e(0x10000000000000000000000000000000000000000) = EXP v189V5e(0x2), v187V5e(0xa0)
    0x18cS0x5e: v18cV5e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18bV5e(0x10000000000000000000000000000000000000000), v185V5e(0x1)
    0x18dS0x5e: v18dV5e = AND v18cV5e(0xffffffffffffffffffffffffffffffffffffffff), v184V5e
    0x18fS0x5e: JUMP v61(0x68)

    Begin block 0x68
    prev=[0x181B0x5e], succ=[0x7b, 0x7f]
    =================================
    0x6b: v6b(0x1) = CONST 
    0x6d: v6d(0xa0) = CONST 
    0x6f: v6f(0x2) = CONST 
    0x71: v71(0x10000000000000000000000000000000000000000) = EXP v6f(0x2), v6d(0xa0)
    0x72: v72(0xffffffffffffffffffffffffffffffffffffffff) = SUB v71(0x10000000000000000000000000000000000000000), v6b(0x1)
    0x74: v74 = AND v18dV5e, v72(0xffffffffffffffffffffffffffffffffffffffff)
    0x75: v75 = ISZERO v74
    0x76: v76 = ISZERO v75
    0x77: v77(0x7f) = CONST 
    0x7a: JUMPI v77(0x7f), v76

    Begin block 0x7b
    prev=[0x68], succ=[]
    =================================
    0x7b: v7b(0x0) = CONST 
    0x7e: REVERT v7b(0x0), v7b(0x0)

    Begin block 0x7f
    prev=[0x68], succ=[0xa2, 0xa5]
    =================================
    0x80: v80(0x40) = CONST 
    0x82: v82 = MLOAD v80(0x40)
    0x83: v83 = CALLDATASIZE 
    0x84: v84(0x0) = CONST 
    0x87: CALLDATACOPY v82, v84(0x0), v83
    0x88: v88(0x0) = CONST 
    0x8b: v8b = CALLDATASIZE 
    0x8e: v8e = GAS 
    0x8f: v8f = DELEGATECALL v8e, v18dV5e, v82, v8b, v88(0x0), v88(0x0)
    0x90: v90 = RETURNDATASIZE 
    0x92: v92 = ADD v82, v90
    0x93: v93(0x40) = CONST 
    0x95: MSTORE v93(0x40), v92
    0x96: v96 = RETURNDATASIZE 
    0x97: v97(0x0) = CONST 
    0x9a: RETURNDATACOPY v82, v97(0x0), v96
    0x9d: v9d = ISZERO v8f
    0x9e: v9e(0xa5) = CONST 
    0xa1: JUMPI v9e(0xa5), v9d

    Begin block 0xa2
    prev=[0x7f], succ=[]
    =================================
    0xa2: va2 = RETURNDATASIZE 
    0xa4: RETURN v82, va2

    Begin block 0xa5
    prev=[0x7f], succ=[]
    =================================
    0xa6: va6 = RETURNDATASIZE 
    0xa8: REVERT v82, va6

}

function upgradeTo(uint256,address)() public {
    Begin block 0xa9
    prev=[], succ=[0xb1, 0xb5]
    =================================
    0xaa: vaa = CALLVALUE 
    0xac: vac = ISZERO vaa
    0xad: vad(0xb5) = CONST 
    0xb0: JUMPI vad(0xb5), vac

    Begin block 0xb1
    prev=[0xa9], succ=[]
    =================================
    0xb1: vb1(0x0) = CONST 
    0xb4: REVERT vb1(0x0), vb1(0x0)

    Begin block 0xb5
    prev=[0xa9], succ=[0x3c0]
    =================================
    0xb7: vb7(0x3c0) = CONST 
    0xba: vba(0x4) = CONST 
    0xbc: vbc = CALLDATALOAD vba(0x4)
    0xbd: vbd(0x1) = CONST 
    0xbf: vbf(0xa0) = CONST 
    0xc1: vc1(0x2) = CONST 
    0xc3: vc3(0x10000000000000000000000000000000000000000) = EXP vc1(0x2), vbf(0xa0)
    0xc4: vc4(0xffffffffffffffffffffffffffffffffffffffff) = SUB vc3(0x10000000000000000000000000000000000000000), vbd(0x1)
    0xc5: vc5(0x24) = CONST 
    0xc7: vc7 = CALLDATALOAD vc5(0x24)
    0xc8: vc8 = AND vc7, vc4(0xffffffffffffffffffffffffffffffffffffffff)
    0xc9: vc9(0x190) = CONST 
    0xcc: CALLPRIVATE vc9(0x190), vc8, vbc, vb7(0x3c0)

    Begin block 0x3c0
    prev=[0xb5], succ=[]
    =================================
    0x3c1: STOP 

}

function version()() public {
    Begin block 0xcf
    prev=[], succ=[0xd7, 0xdb]
    =================================
    0xd0: vd0 = CALLVALUE 
    0xd2: vd2 = ISZERO vd0
    0xd3: vd3(0xdb) = CONST 
    0xd6: JUMPI vd3(0xdb), vd2

    Begin block 0xd7
    prev=[0xcf], succ=[]
    =================================
    0xd7: vd7(0x0) = CONST 
    0xda: REVERT vd7(0x0), vd7(0x0)

    Begin block 0xdb
    prev=[0xcf], succ=[0x1ba]
    =================================
    0xdd: vdd(0xe4) = CONST 
    0xe0: ve0(0x1ba) = CONST 
    0xe3: JUMP ve0(0x1ba)

    Begin block 0x1ba
    prev=[0xdb], succ=[0xe4]
    =================================
    0x1bb: v1bb(0x7) = CONST 
    0x1bd: v1bd = SLOAD v1bb(0x7)
    0x1bf: JUMP vdd(0xe4)

    Begin block 0xe4
    prev=[0x1ba], succ=[]
    =================================
    0xe5: ve5(0x40) = CONST 
    0xe8: ve8 = MLOAD ve5(0x40)
    0xeb: MSTORE ve8, v1bd
    0xec: vec = MLOAD ve5(0x40)
    0xf0: vf0(0x0) = SUB ve8, vec
    0xf1: vf1(0x20) = CONST 
    0xf3: vf3(0x20) = ADD vf1(0x20), vf0(0x0)
    0xf5: RETURN vec, vf3(0x20)

}

function implementation()() public {
    Begin block 0xf6
    prev=[], succ=[0xfe, 0x102]
    =================================
    0xf7: vf7 = CALLVALUE 
    0xf9: vf9 = ISZERO vf7
    0xfa: vfa(0x102) = CONST 
    0xfd: JUMPI vfa(0x102), vf9

    Begin block 0xfe
    prev=[0xf6], succ=[]
    =================================
    0xfe: vfe(0x0) = CONST 
    0x101: REVERT vfe(0x0), vfe(0x0)

    Begin block 0x102
    prev=[0xf6], succ=[0x181B0x102]
    =================================
    0x104: v104(0x3e1) = CONST 
    0x107: v107(0x181) = CONST 
    0x10a: JUMP v107(0x181)

    Begin block 0x181B0x102
    prev=[0x102], succ=[0x3e1]
    =================================
    0x182S0x102: v182V102(0x8) = CONST 
    0x184S0x102: v184V102 = SLOAD v182V102(0x8)
    0x185S0x102: v185V102(0x1) = CONST 
    0x187S0x102: v187V102(0xa0) = CONST 
    0x189S0x102: v189V102(0x2) = CONST 
    0x18bS0x102: v18bV102(0x10000000000000000000000000000000000000000) = EXP v189V102(0x2), v187V102(0xa0)
    0x18cS0x102: v18cV102(0xffffffffffffffffffffffffffffffffffffffff) = SUB v18bV102(0x10000000000000000000000000000000000000000), v185V102(0x1)
    0x18dS0x102: v18dV102 = AND v18cV102(0xffffffffffffffffffffffffffffffffffffffff), v184V102
    0x18fS0x102: JUMP v104(0x3e1)

    Begin block 0x3e1
    prev=[0x181B0x102], succ=[]
    =================================
    0x3e2: v3e2(0x40) = CONST 
    0x3e5: v3e5 = MLOAD v3e2(0x40)
    0x3e6: v3e6(0x1) = CONST 
    0x3e8: v3e8(0xa0) = CONST 
    0x3ea: v3ea(0x2) = CONST 
    0x3ec: v3ec(0x10000000000000000000000000000000000000000) = EXP v3ea(0x2), v3e8(0xa0)
    0x3ed: v3ed(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ec(0x10000000000000000000000000000000000000000), v3e6(0x1)
    0x3f0: v3f0 = AND v18dV102, v3ed(0xffffffffffffffffffffffffffffffffffffffff)
    0x3f2: MSTORE v3e5, v3f0
    0x3f3: v3f3 = MLOAD v3e2(0x40)
    0x3f7: v3f7(0x0) = SUB v3e5, v3f3
    0x3f8: v3f8(0x20) = CONST 
    0x3fa: v3fa(0x20) = ADD v3f8(0x20), v3f7(0x0)
    0x3fc: RETURN v3f3, v3fa(0x20)

}

