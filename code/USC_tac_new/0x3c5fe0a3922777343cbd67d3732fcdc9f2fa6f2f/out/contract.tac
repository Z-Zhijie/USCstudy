function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0xbe4]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0xbd0: vbd0(0xbe4) = CONST 
    0xbd1: JUMPI vbd0(0xbe4), v8

    Begin block 0xd
    prev=[0x0], succ=[0x59, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x5d36b190) = CONST 
    0x19: v19 = GT v14(0x5d36b190), v12
    0x1a: v1a(0x59) = CONST 
    0x1d: JUMPI v1a(0x59), v19

    Begin block 0x59
    prev=[0xd], succ=[0xbe7, 0x65]
    =================================
    0x5b: v5b(0xc340a24) = CONST 
    0x60: v60 = EQ v5b(0xc340a24), v12
    0xbdc: vbdc(0xbe7) = CONST 
    0xbdd: JUMPI vbdc(0xbe7), v60

    Begin block 0xbe7
    prev=[0x59, 0x4a], succ=[]
    =================================
    0xbe8: vbe8(0x90) = CONST 
    0xbe9: CALLPRIVATE vbe8(0x90)

    Begin block 0x65
    prev=[0x59], succ=[0xbea, 0x70]
    =================================
    0x66: v66(0x3659cfe6) = CONST 
    0x6b: v6b = EQ v66(0x3659cfe6), v12
    0xbde: vbde(0xbea) = CONST 
    0xbdf: JUMPI vbde(0xbea), v6b

    Begin block 0xbea
    prev=[0x65], succ=[]
    =================================
    0xbeb: vbeb(0xc1) = CONST 
    0xbec: CALLPRIVATE vbeb(0xc1)

    Begin block 0x70
    prev=[0x65], succ=[0xbed, 0x7b]
    =================================
    0x71: v71(0x4f1ef286) = CONST 
    0x76: v76 = EQ v71(0x4f1ef286), v12
    0xbe0: vbe0(0xbed) = CONST 
    0xbe1: JUMPI vbe0(0xbed), v76

    Begin block 0xbed
    prev=[0x70], succ=[]
    =================================
    0xbee: vbee(0xf4) = CONST 
    0xbef: CALLPRIVATE vbee(0xf4)

    Begin block 0x7b
    prev=[0x70], succ=[0xbe4, 0xbf0]
    =================================
    0x7c: v7c(0x5c60da1b) = CONST 
    0x81: v81 = EQ v7c(0x5c60da1b), v12
    0xbe2: vbe2(0xbf0) = CONST 
    0xbe3: JUMPI vbe2(0xbf0), v81

    Begin block 0xbe4
    prev=[0x0, 0x7b], succ=[]
    =================================
    0xbe5: vbe5(0x86) = CONST 
    0xbe6: CALLPRIVATE vbe5(0x86)

    Begin block 0xbf0
    prev=[0x7b], succ=[]
    =================================
    0xbf1: vbf1(0x174) = CONST 
    0xbf2: CALLPRIVATE vbf1(0x174)

    Begin block 0x1e
    prev=[0xd], succ=[0xbf3, 0x29]
    =================================
    0x1f: v1f(0x5d36b190) = CONST 
    0x24: v24 = EQ v1f(0x5d36b190), v12
    0xbd2: vbd2(0xbf3) = CONST 
    0xbd3: JUMPI vbd2(0xbf3), v24

    Begin block 0xbf3
    prev=[0x1e], succ=[]
    =================================
    0xbf4: vbf4(0x189) = CONST 
    0xbf5: CALLPRIVATE vbf4(0x189)

    Begin block 0x29
    prev=[0x1e], succ=[0xbf6, 0x34]
    =================================
    0x2a: v2a(0xc7af3352) = CONST 
    0x2f: v2f = EQ v2a(0xc7af3352), v12
    0xbd4: vbd4(0xbf6) = CONST 
    0xbd5: JUMPI vbd4(0xbf6), v2f

    Begin block 0xbf6
    prev=[0x29], succ=[]
    =================================
    0xbf7: vbf7(0x19e) = CONST 
    0xbf8: CALLPRIVATE vbf7(0x19e)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0xbf9]
    =================================
    0x35: v35(0xcf7a1d77) = CONST 
    0x3a: v3a = EQ v35(0xcf7a1d77), v12
    0xbd6: vbd6(0xbf9) = CONST 
    0xbd7: JUMPI vbd6(0xbf9), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0xbfc, 0x4a]
    =================================
    0x40: v40(0xd38bfff4) = CONST 
    0x45: v45 = EQ v40(0xd38bfff4), v12
    0xbd8: vbd8(0xbfc) = CONST 
    0xbd9: JUMPI vbd8(0xbfc), v45

    Begin block 0xbfc
    prev=[0x3f], succ=[]
    =================================
    0xbfd: vbfd(0x286) = CONST 
    0xbfe: CALLPRIVATE vbfd(0x286)

    Begin block 0x4a
    prev=[0x3f], succ=[0x55, 0xbe7]
    =================================
    0x4b: v4b(0xf851a440) = CONST 
    0x50: v50 = EQ v4b(0xf851a440), v12
    0xbda: vbda(0xbe7) = CONST 
    0xbdb: JUMPI vbda(0xbe7), v50

    Begin block 0x55
    prev=[0x4a], succ=[]
    =================================
    0x55: v55(0x86) = CONST 
    0x58: JUMP v55(0x86)

    Begin block 0xbf9
    prev=[0x34], succ=[]
    =================================
    0xbfa: vbfa(0x1c7) = CONST 
    0xbfb: CALLPRIVATE vbfa(0x1c7)

}

function implementation()() public {
    Begin block 0x174
    prev=[], succ=[0x17c, 0x180]
    =================================
    0x175: v175 = CALLVALUE 
    0x177: v177 = ISZERO v175
    0x178: v178(0x180) = CONST 
    0x17b: JUMPI v178(0x180), v177

    Begin block 0x17c
    prev=[0x174], succ=[]
    =================================
    0x17c: v17c(0x0) = CONST 
    0x17f: REVERT v17c(0x0), v17c(0x0)

    Begin block 0x180
    prev=[0x174], succ=[0x419B0x180]
    =================================
    0x182: v182(0xa62) = CONST 
    0x185: v185(0x419) = CONST 
    0x188: JUMP v185(0x419)

    Begin block 0x419B0x180
    prev=[0x180], succ=[0x6dcB0x419B0x180]
    =================================
    0x41aS0x180: v41aV180(0x0) = CONST 
    0x41cS0x180: v41cV180(0xb88) = CONST 
    0x41fS0x180: v41fV180(0x6dc) = CONST 
    0x422S0x180: JUMP v41fV180(0x6dc)

    Begin block 0x6dcB0x419B0x180
    prev=[0x419B0x180], succ=[0xb88B0x180]
    =================================
    0x6ddS0x419S0x180: v6ddV419V180(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x6feS0x419S0x180: v6feV419V180 = SLOAD v6ddV419V180(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x700S0x419S0x180: JUMP v41cV180(0xb88)

    Begin block 0xb88B0x180
    prev=[0x6dcB0x419B0x180], succ=[0xa62]
    =================================
    0xb8cS0x180: JUMP v182(0xa62)

    Begin block 0xa62
    prev=[0xb88B0x180], succ=[]
    =================================
    0xa63: va63(0x40) = CONST 
    0xa66: va66 = MLOAD va63(0x40)
    0xa67: va67(0x1) = CONST 
    0xa69: va69(0x1) = CONST 
    0xa6b: va6b(0xa0) = CONST 
    0xa6d: va6d(0x10000000000000000000000000000000000000000) = SHL va6b(0xa0), va69(0x1)
    0xa6e: va6e(0xffffffffffffffffffffffffffffffffffffffff) = SUB va6d(0x10000000000000000000000000000000000000000), va67(0x1)
    0xa71: va71 = AND v6feV419V180, va6e(0xffffffffffffffffffffffffffffffffffffffff)
    0xa73: MSTORE va66, va71
    0xa74: va74 = MLOAD va63(0x40)
    0xa78: va78(0x0) = SUB va66, va74
    0xa79: va79(0x20) = CONST 
    0xa7b: va7b(0x20) = ADD va79(0x20), va78(0x0)
    0xa7d: RETURN va74, va7b(0x20)

}

function claimGovernance()() public {
    Begin block 0x189
    prev=[], succ=[0x191, 0x195]
    =================================
    0x18a: v18a = CALLVALUE 
    0x18c: v18c = ISZERO v18a
    0x18d: v18d(0x195) = CONST 
    0x190: JUMPI v18d(0x195), v18c

    Begin block 0x191
    prev=[0x189], succ=[]
    =================================
    0x191: v191(0x0) = CONST 
    0x194: REVERT v191(0x0), v191(0x0)

    Begin block 0x195
    prev=[0x189], succ=[0x423B0x195]
    =================================
    0x197: v197(0xa9d) = CONST 
    0x19a: v19a(0x423) = CONST 
    0x19d: JUMP v19a(0x423), v197(0xa9d)

    Begin block 0x423B0x195
    prev=[0x195], succ=[0x78aB0x195]
    =================================
    0x424S0x195: v424V195(0x42b) = CONST 
    0x427S0x195: v427V195(0x78a) = CONST 
    0x42aS0x195: JUMP v427V195(0x78a)

    Begin block 0x78aB0x195
    prev=[0x423B0x195], succ=[0x42bB0x195]
    =================================
    0x78bS0x195: v78bV195(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = CONST 
    0x7acS0x195: v7acV195 = SLOAD v78bV195(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db)
    0x7aeS0x195: JUMP v424V195(0x42b)

    Begin block 0x42bB0x195
    prev=[0x78aB0x195], succ=[0x444B0x195, 0x47aB0x195]
    =================================
    0x42cS0x195: v42cV195(0x1) = CONST 
    0x42eS0x195: v42eV195(0x1) = CONST 
    0x430S0x195: v430V195(0xa0) = CONST 
    0x432S0x195: v432V195(0x10000000000000000000000000000000000000000) = SHL v430V195(0xa0), v42eV195(0x1)
    0x433S0x195: v433V195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v432V195(0x10000000000000000000000000000000000000000), v42cV195(0x1)
    0x434S0x195: v434V195 = AND v433V195(0xffffffffffffffffffffffffffffffffffffffff), v7acV195
    0x435S0x195: v435V195 = CALLER 
    0x436S0x195: v436V195(0x1) = CONST 
    0x438S0x195: v438V195(0x1) = CONST 
    0x43aS0x195: v43aV195(0xa0) = CONST 
    0x43cS0x195: v43cV195(0x10000000000000000000000000000000000000000) = SHL v43aV195(0xa0), v438V195(0x1)
    0x43dS0x195: v43dV195(0xffffffffffffffffffffffffffffffffffffffff) = SUB v43cV195(0x10000000000000000000000000000000000000000), v436V195(0x1)
    0x43eS0x195: v43eV195 = AND v43dV195(0xffffffffffffffffffffffffffffffffffffffff), v435V195
    0x43fS0x195: v43fV195 = EQ v43eV195, v434V195
    0x440S0x195: v440V195(0x47a) = CONST 
    0x443S0x195: JUMPI v440V195(0x47a), v43fV195

    Begin block 0x444B0x195
    prev=[0x42bB0x195], succ=[]
    =================================
    0x444S0x195: v444V195(0x40) = CONST 
    0x446S0x195: v446V195 = MLOAD v444V195(0x40)
    0x447S0x195: v447V195(0x461bcd) = CONST 
    0x44bS0x195: v44bV195(0xe5) = CONST 
    0x44dS0x195: v44dV195(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v44bV195(0xe5), v447V195(0x461bcd)
    0x44fS0x195: MSTORE v446V195, v44dV195(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x450S0x195: v450V195(0x4) = CONST 
    0x452S0x195: v452V195 = ADD v450V195(0x4), v446V195
    0x455S0x195: v455V195(0x20) = CONST 
    0x457S0x195: v457V195 = ADD v455V195(0x20), v452V195
    0x45aS0x195: v45aV195(0x20) = SUB v457V195, v452V195
    0x45cS0x195: MSTORE v452V195, v45aV195(0x20)
    0x45dS0x195: v45dV195(0x30) = CONST 
    0x460S0x195: MSTORE v457V195, v45dV195(0x30)
    0x461S0x195: v461V195(0x20) = CONST 
    0x463S0x195: v463V195 = ADD v461V195(0x20), v457V195
    0x465S0x195: v465V195(0x94c) = CONST 
    0x468S0x195: v468V195(0x30) = CONST 
    0x46bS0x195: CODECOPY v463V195, v465V195(0x94c), v468V195(0x30)
    0x46cS0x195: v46cV195(0x40) = CONST 
    0x46eS0x195: v46eV195 = ADD v46cV195(0x40), v463V195
    0x472S0x195: v472V195(0x40) = CONST 
    0x474S0x195: v474V195 = MLOAD v472V195(0x40)
    0x477S0x195: v477V195(0x84) = SUB v46eV195, v474V195
    0x479S0x195: REVERT v474V195, v477V195(0x84)

    Begin block 0x47aB0x195
    prev=[0x42bB0x195], succ=[0xbacB0x195]
    =================================
    0x47bS0x195: v47bV195(0xbac) = CONST 
    0x47eS0x195: v47eV195 = CALLER 
    0x47fS0x195: v47fV195(0x7af) = CONST 
    0x482S0x195: CALLPRIVATE v47fV195(0x7af), v47eV195, v47bV195(0xbac)

    Begin block 0xbacB0x195
    prev=[0x47aB0x195], succ=[0xa9d]
    =================================
    0xbadS0x195: JUMP v197(0xa9d)

    Begin block 0xa9d
    prev=[0xbacB0x195], succ=[]
    =================================
    0xa9e: STOP 

}

function isGovernor()() public {
    Begin block 0x19e
    prev=[], succ=[0x1a6, 0x1aa]
    =================================
    0x19f: v19f = CALLVALUE 
    0x1a1: v1a1 = ISZERO v19f
    0x1a2: v1a2(0x1aa) = CONST 
    0x1a5: JUMPI v1a2(0x1aa), v1a1

    Begin block 0x1a6
    prev=[0x19e], succ=[]
    =================================
    0x1a6: v1a6(0x0) = CONST 
    0x1a9: REVERT v1a6(0x0), v1a6(0x0)

    Begin block 0x1aa
    prev=[0x19e], succ=[0x483B0x1aa]
    =================================
    0x1ac: v1ac(0x1b3) = CONST 
    0x1af: v1af(0x483) = CONST 
    0x1b2: JUMP v1af(0x483)

    Begin block 0x483B0x1aa
    prev=[0x1aa], succ=[0x725B0x483B0x1aa]
    =================================
    0x484S0x1aa: v484V1aa(0x0) = CONST 
    0x486S0x1aa: v486V1aa(0x48d) = CONST 
    0x489S0x1aa: v489V1aa(0x725) = CONST 
    0x48cS0x1aa: JUMP v489V1aa(0x725)

    Begin block 0x725B0x483B0x1aa
    prev=[0x483B0x1aa], succ=[0x48dB0x1aa]
    =================================
    0x726S0x483S0x1aa: v726V483V1aa(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x483S0x1aa: v747V483V1aa = SLOAD v726V483V1aa(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x483S0x1aa: JUMP v486V1aa(0x48d)

    Begin block 0x48dB0x1aa
    prev=[0x725B0x483B0x1aa], succ=[0x1b3]
    =================================
    0x48eS0x1aa: v48eV1aa(0x1) = CONST 
    0x490S0x1aa: v490V1aa(0x1) = CONST 
    0x492S0x1aa: v492V1aa(0xa0) = CONST 
    0x494S0x1aa: v494V1aa(0x10000000000000000000000000000000000000000) = SHL v492V1aa(0xa0), v490V1aa(0x1)
    0x495S0x1aa: v495V1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494V1aa(0x10000000000000000000000000000000000000000), v48eV1aa(0x1)
    0x496S0x1aa: v496V1aa = AND v495V1aa(0xffffffffffffffffffffffffffffffffffffffff), v747V483V1aa
    0x497S0x1aa: v497V1aa = CALLER 
    0x498S0x1aa: v498V1aa(0x1) = CONST 
    0x49aS0x1aa: v49aV1aa(0x1) = CONST 
    0x49cS0x1aa: v49cV1aa(0xa0) = CONST 
    0x49eS0x1aa: v49eV1aa(0x10000000000000000000000000000000000000000) = SHL v49cV1aa(0xa0), v49aV1aa(0x1)
    0x49fS0x1aa: v49fV1aa(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49eV1aa(0x10000000000000000000000000000000000000000), v498V1aa(0x1)
    0x4a0S0x1aa: v4a0V1aa = AND v49fV1aa(0xffffffffffffffffffffffffffffffffffffffff), v497V1aa
    0x4a1S0x1aa: v4a1V1aa = EQ v4a0V1aa, v496V1aa
    0x4a5S0x1aa: JUMP v1ac(0x1b3)

    Begin block 0x1b3
    prev=[0x48dB0x1aa], succ=[]
    =================================
    0x1b4: v1b4(0x40) = CONST 
    0x1b7: v1b7 = MLOAD v1b4(0x40)
    0x1b9: v1b9 = ISZERO v4a1V1aa
    0x1ba: v1ba = ISZERO v1b9
    0x1bc: MSTORE v1b7, v1ba
    0x1bd: v1bd = MLOAD v1b4(0x40)
    0x1c1: v1c1(0x0) = SUB v1b7, v1bd
    0x1c2: v1c2(0x20) = CONST 
    0x1c4: v1c4(0x20) = ADD v1c2(0x20), v1c1(0x0)
    0x1c6: RETURN v1bd, v1c4(0x20)

}

function initialize(address,address,bytes)() public {
    Begin block 0x1c7
    prev=[], succ=[0x1d9, 0x1dd]
    =================================
    0x1c8: v1c8(0xabe) = CONST 
    0x1cb: v1cb(0x4) = CONST 
    0x1ce: v1ce = CALLDATASIZE 
    0x1cf: v1cf = SUB v1ce, v1cb(0x4)
    0x1d0: v1d0(0x60) = CONST 
    0x1d3: v1d3 = LT v1cf, v1d0(0x60)
    0x1d4: v1d4 = ISZERO v1d3
    0x1d5: v1d5(0x1dd) = CONST 
    0x1d8: JUMPI v1d5(0x1dd), v1d4

    Begin block 0x1d9
    prev=[0x1c7], succ=[]
    =================================
    0x1d9: v1d9(0x0) = CONST 
    0x1dc: REVERT v1d9(0x0), v1d9(0x0)

    Begin block 0x1dd
    prev=[0x1c7], succ=[0x20d, 0x211]
    =================================
    0x1de: v1de(0x1) = CONST 
    0x1e0: v1e0(0x1) = CONST 
    0x1e2: v1e2(0xa0) = CONST 
    0x1e4: v1e4(0x10000000000000000000000000000000000000000) = SHL v1e2(0xa0), v1e0(0x1)
    0x1e5: v1e5(0xffffffffffffffffffffffffffffffffffffffff) = SUB v1e4(0x10000000000000000000000000000000000000000), v1de(0x1)
    0x1e7: v1e7 = CALLDATALOAD v1cb(0x4)
    0x1e9: v1e9 = AND v1e5(0xffffffffffffffffffffffffffffffffffffffff), v1e7
    0x1eb: v1eb(0x20) = CONST 
    0x1ee: v1ee(0x24) = ADD v1cb(0x4), v1eb(0x20)
    0x1ef: v1ef = CALLDATALOAD v1ee(0x24)
    0x1f2: v1f2 = AND v1e5(0xffffffffffffffffffffffffffffffffffffffff), v1ef
    0x1f5: v1f5 = ADD v1cb(0x4), v1cf
    0x1f7: v1f7(0x60) = CONST 
    0x1fa: v1fa(0x64) = ADD v1cb(0x4), v1f7(0x60)
    0x1fb: v1fb(0x40) = CONST 
    0x1fe: v1fe(0x44) = ADD v1cb(0x4), v1fb(0x40)
    0x1ff: v1ff = CALLDATALOAD v1fe(0x44)
    0x200: v200(0x100000000) = CONST 
    0x207: v207 = GT v1ff, v200(0x100000000)
    0x208: v208 = ISZERO v207
    0x209: v209(0x211) = CONST 
    0x20c: JUMPI v209(0x211), v208

    Begin block 0x20d
    prev=[0x1dd], succ=[]
    =================================
    0x20d: v20d(0x0) = CONST 
    0x210: REVERT v20d(0x0), v20d(0x0)

    Begin block 0x211
    prev=[0x1dd], succ=[0x21f, 0x223]
    =================================
    0x213: v213 = ADD v1cb(0x4), v1ff
    0x215: v215(0x20) = CONST 
    0x218: v218 = ADD v213, v215(0x20)
    0x219: v219 = GT v218, v1f5
    0x21a: v21a = ISZERO v219
    0x21b: v21b(0x223) = CONST 
    0x21e: JUMPI v21b(0x223), v21a

    Begin block 0x21f
    prev=[0x211], succ=[]
    =================================
    0x21f: v21f(0x0) = CONST 
    0x222: REVERT v21f(0x0), v21f(0x0)

    Begin block 0x223
    prev=[0x211], succ=[0x241, 0x245]
    =================================
    0x225: v225 = CALLDATALOAD v213
    0x227: v227(0x20) = CONST 
    0x229: v229 = ADD v227(0x20), v213
    0x22c: v22c(0x1) = CONST 
    0x22f: v22f = MUL v225, v22c(0x1)
    0x231: v231 = ADD v229, v22f
    0x232: v232 = GT v231, v1f5
    0x233: v233(0x100000000) = CONST 
    0x23a: v23a = GT v225, v233(0x100000000)
    0x23b: v23b = OR v23a, v232
    0x23c: v23c = ISZERO v23b
    0x23d: v23d(0x245) = CONST 
    0x240: JUMPI v23d(0x245), v23c

    Begin block 0x241
    prev=[0x223], succ=[]
    =================================
    0x241: v241(0x0) = CONST 
    0x244: REVERT v241(0x0), v241(0x0)

    Begin block 0x245
    prev=[0x223], succ=[0x4a6]
    =================================
    0x24a: v24a(0x1f) = CONST 
    0x24c: v24c = ADD v24a(0x1f), v225
    0x24d: v24d(0x20) = CONST 
    0x251: v251 = DIV v24c, v24d(0x20)
    0x252: v252 = MUL v251, v24d(0x20)
    0x253: v253(0x20) = CONST 
    0x255: v255 = ADD v253(0x20), v252
    0x256: v256(0x40) = CONST 
    0x258: v258 = MLOAD v256(0x40)
    0x25b: v25b = ADD v258, v255
    0x25c: v25c(0x40) = CONST 
    0x25e: MSTORE v25c(0x40), v25b
    0x266: MSTORE v258, v225
    0x267: v267(0x20) = CONST 
    0x269: v269 = ADD v267(0x20), v258
    0x26f: CALLDATACOPY v269, v229, v225
    0x270: v270(0x0) = CONST 
    0x273: v273 = ADD v269, v225
    0x277: MSTORE v273, v270(0x0)
    0x27c: v27c(0x4a6) = CONST 
    0x285: JUMP v27c(0x4a6)

    Begin block 0x4a6
    prev=[0x245], succ=[0x483B0x4a6]
    =================================
    0x4a7: v4a7(0x4ae) = CONST 
    0x4aa: v4aa(0x483) = CONST 
    0x4ad: JUMP v4aa(0x483)

    Begin block 0x483B0x4a6
    prev=[0x4a6], succ=[0x725B0x483B0x4a6]
    =================================
    0x484S0x4a6: v484V4a6(0x0) = CONST 
    0x486S0x4a6: v486V4a6(0x48d) = CONST 
    0x489S0x4a6: v489V4a6(0x725) = CONST 
    0x48cS0x4a6: JUMP v489V4a6(0x725)

    Begin block 0x725B0x483B0x4a6
    prev=[0x483B0x4a6], succ=[0x48dB0x4a6]
    =================================
    0x726S0x483S0x4a6: v726V483V4a6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x483S0x4a6: v747V483V4a6 = SLOAD v726V483V4a6(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x483S0x4a6: JUMP v486V4a6(0x48d)

    Begin block 0x48dB0x4a6
    prev=[0x725B0x483B0x4a6], succ=[0x4ae]
    =================================
    0x48eS0x4a6: v48eV4a6(0x1) = CONST 
    0x490S0x4a6: v490V4a6(0x1) = CONST 
    0x492S0x4a6: v492V4a6(0xa0) = CONST 
    0x494S0x4a6: v494V4a6(0x10000000000000000000000000000000000000000) = SHL v492V4a6(0xa0), v490V4a6(0x1)
    0x495S0x4a6: v495V4a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494V4a6(0x10000000000000000000000000000000000000000), v48eV4a6(0x1)
    0x496S0x4a6: v496V4a6 = AND v495V4a6(0xffffffffffffffffffffffffffffffffffffffff), v747V483V4a6
    0x497S0x4a6: v497V4a6 = CALLER 
    0x498S0x4a6: v498V4a6(0x1) = CONST 
    0x49aS0x4a6: v49aV4a6(0x1) = CONST 
    0x49cS0x4a6: v49cV4a6(0xa0) = CONST 
    0x49eS0x4a6: v49eV4a6(0x10000000000000000000000000000000000000000) = SHL v49cV4a6(0xa0), v49aV4a6(0x1)
    0x49fS0x4a6: v49fV4a6(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49eV4a6(0x10000000000000000000000000000000000000000), v498V4a6(0x1)
    0x4a0S0x4a6: v4a0V4a6 = AND v49fV4a6(0xffffffffffffffffffffffffffffffffffffffff), v497V4a6
    0x4a1S0x4a6: v4a1V4a6 = EQ v4a0V4a6, v496V4a6
    0x4a5S0x4a6: JUMP v4a7(0x4ae)

    Begin block 0x4ae
    prev=[0x48dB0x4a6], succ=[0x4b3, 0x4fc]
    =================================
    0x4af: v4af(0x4fc) = CONST 
    0x4b2: JUMPI v4af(0x4fc), v4a1V4a6

    Begin block 0x4b3
    prev=[0x4ae], succ=[]
    =================================
    0x4b3: v4b3(0x40) = CONST 
    0x4b6: v4b6 = MLOAD v4b3(0x40)
    0x4b7: v4b7(0x461bcd) = CONST 
    0x4bb: v4bb(0xe5) = CONST 
    0x4bd: v4bd(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v4bb(0xe5), v4b7(0x461bcd)
    0x4bf: MSTORE v4b6, v4bd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x4c0: v4c0(0x20) = CONST 
    0x4c2: v4c2(0x4) = CONST 
    0x4c5: v4c5 = ADD v4b6, v4c2(0x4)
    0x4c6: MSTORE v4c5, v4c0(0x20)
    0x4c7: v4c7(0x1a) = CONST 
    0x4c9: v4c9(0x24) = CONST 
    0x4cc: v4cc = ADD v4b6, v4c9(0x24)
    0x4cd: MSTORE v4cc, v4c7(0x1a)
    0x4ce: v4ce(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9) = CONST 
    0x4e9: v4e9(0x31) = CONST 
    0x4eb: v4eb(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = SHL v4e9(0x31), v4ce(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9)
    0x4ec: v4ec(0x44) = CONST 
    0x4ef: v4ef = ADD v4b6, v4ec(0x44)
    0x4f0: MSTORE v4ef, v4eb(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x4f2: v4f2 = MLOAD v4b3(0x40)
    0x4f6: v4f6(0x0) = SUB v4b6, v4f2
    0x4f7: v4f7(0x64) = CONST 
    0x4f9: v4f9(0x64) = ADD v4f7(0x64), v4f6(0x0)
    0x4fb: REVERT v4f2, v4f9(0x64)

    Begin block 0x4fc
    prev=[0x4ae], succ=[0x6dcB0x4fc]
    =================================
    0x4fd: v4fd(0x0) = CONST 
    0x4ff: v4ff(0x506) = CONST 
    0x502: v502(0x6dc) = CONST 
    0x505: JUMP v502(0x6dc)

    Begin block 0x6dcB0x4fc
    prev=[0x4fc], succ=[0x506]
    =================================
    0x6ddS0x4fc: v6ddV4fc(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x6feS0x4fc: v6feV4fc = SLOAD v6ddV4fc(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x700S0x4fc: JUMP v4ff(0x506)

    Begin block 0x506
    prev=[0x6dcB0x4fc], succ=[0x515, 0x519]
    =================================
    0x507: v507(0x1) = CONST 
    0x509: v509(0x1) = CONST 
    0x50b: v50b(0xa0) = CONST 
    0x50d: v50d(0x10000000000000000000000000000000000000000) = SHL v50b(0xa0), v509(0x1)
    0x50e: v50e(0xffffffffffffffffffffffffffffffffffffffff) = SUB v50d(0x10000000000000000000000000000000000000000), v507(0x1)
    0x50f: v50f = AND v50e(0xffffffffffffffffffffffffffffffffffffffff), v6feV4fc
    0x510: v510 = EQ v50f, v4fd(0x0)
    0x511: v511(0x519) = CONST 
    0x514: JUMPI v511(0x519), v510

    Begin block 0x515
    prev=[0x506], succ=[]
    =================================
    0x515: v515(0x0) = CONST 
    0x518: REVERT v515(0x0), v515(0x0)

    Begin block 0x519
    prev=[0x506], succ=[0x578, 0x579]
    =================================
    0x51a: v51a(0x40) = CONST 
    0x51d: v51d = MLOAD v51a(0x40)
    0x51e: v51e(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000) = CONST 
    0x540: MSTORE v51d, v51e(0x656970313936372e70726f78792e696d706c656d656e746174696f6e00000000)
    0x542: v542 = MLOAD v51a(0x40)
    0x546: v546(0x0) = SUB v51d, v542
    0x547: v547(0x1c) = CONST 
    0x549: v549(0x1c) = ADD v547(0x1c), v546(0x0)
    0x54b: v54b = SHA3 v542, v549(0x1c)
    0x54c: v54c(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x56d: v56d(0x0) = CONST 
    0x56f: v56f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) = NOT v56d(0x0)
    0x572: v572 = ADD v54b, v56f(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
    0x573: v573 = EQ v572, v54c(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x574: v574(0x579) = CONST 
    0x577: JUMPI v574(0x579), v573

    Begin block 0x578
    prev=[0x519], succ=[]
    =================================
    0x578: THROW 

    Begin block 0x579
    prev=[0x519], succ=[0x582]
    =================================
    0x57a: v57a(0x582) = CONST 
    0x57e: v57e(0x7af) = CONST 
    0x581: CALLPRIVATE v57e(0x7af), v1f2, v57a(0x582)

    Begin block 0x582
    prev=[0x579], succ=[0x58b]
    =================================
    0x583: v583(0x58b) = CONST 
    0x587: v587(0x85a) = CONST 
    0x58a: CALLPRIVATE v587(0x85a), v1e9, v583(0x58b)

    Begin block 0x58b
    prev=[0x582], succ=[0x593, 0x62e]
    =================================
    0x58d: v58d = MLOAD v258
    0x58e: v58e = ISZERO v58d
    0x58f: v58f(0x62e) = CONST 
    0x592: JUMPI v58f(0x62e), v58e

    Begin block 0x593
    prev=[0x58b], succ=[0x5af]
    =================================
    0x593: v593(0x0) = CONST 
    0x596: v596(0x1) = CONST 
    0x598: v598(0x1) = CONST 
    0x59a: v59a(0xa0) = CONST 
    0x59c: v59c(0x10000000000000000000000000000000000000000) = SHL v59a(0xa0), v598(0x1)
    0x59d: v59d(0xffffffffffffffffffffffffffffffffffffffff) = SUB v59c(0x10000000000000000000000000000000000000000), v596(0x1)
    0x59e: v59e = AND v59d(0xffffffffffffffffffffffffffffffffffffffff), v1e9
    0x5a0: v5a0(0x40) = CONST 
    0x5a2: v5a2 = MLOAD v5a0(0x40)
    0x5a6: v5a6 = MLOAD v258
    0x5a8: v5a8(0x20) = CONST 
    0x5aa: v5aa = ADD v5a8(0x20), v258

    Begin block 0x5af
    prev=[0x593, 0x5b8], succ=[0x5ce, 0x5b8]
    =================================
    0x5af_0x2: v5af_2 = PHI v5a6, v5c1
    0x5b0: v5b0(0x20) = CONST 
    0x5b3: v5b3 = LT v5af_2, v5b0(0x20)
    0x5b4: v5b4(0x5ce) = CONST 
    0x5b7: JUMPI v5b4(0x5ce), v5b3

    Begin block 0x5ce
    prev=[0x5af], succ=[0x60d, 0x4000x1c7]
    =================================
    0x5ce_0x0: v5ce_0 = PHI v5aa, v5c9
    0x5ce_0x1: v5ce_1 = PHI v5a2, v5c7
    0x5ce_0x2: v5ce_2 = PHI v5a6, v5c1
    0x5cf: v5cf(0x1) = CONST 
    0x5d2: v5d2(0x20) = CONST 
    0x5d4: v5d4 = SUB v5d2(0x20), v5ce_2
    0x5d5: v5d5(0x100) = CONST 
    0x5d8: v5d8 = EXP v5d5(0x100), v5d4
    0x5d9: v5d9 = SUB v5d8, v5cf(0x1)
    0x5db: v5db = NOT v5d9
    0x5dd: v5dd = MLOAD v5ce_0
    0x5de: v5de = AND v5dd, v5db
    0x5e1: v5e1 = MLOAD v5ce_1
    0x5e2: v5e2 = AND v5e1, v5d9
    0x5e5: v5e5 = OR v5de, v5e2
    0x5e7: MSTORE v5ce_1, v5e5
    0x5f0: v5f0 = ADD v5a6, v5a2
    0x5f4: v5f4(0x0) = CONST 
    0x5f6: v5f6(0x40) = CONST 
    0x5f8: v5f8 = MLOAD v5f6(0x40)
    0x5fb: v5fb = SUB v5f0, v5f8
    0x5fe: v5fe = GAS 
    0x5ff: v5ff = DELEGATECALL v5fe, v59e, v5f8, v5fb, v5f8, v5f4(0x0)
    0x603: v603 = RETURNDATASIZE 
    0x605: v605(0x0) = CONST 
    0x608: v608 = EQ v603, v605(0x0)
    0x609: v609(0x400) = CONST 
    0x60c: JUMPI v609(0x400), v608

    Begin block 0x60d
    prev=[0x5ce], succ=[0x4050x1c7]
    =================================
    0x60d: v60d(0x40) = CONST 
    0x60f: v60f = MLOAD v60d(0x40)
    0x612: v612(0x1f) = CONST 
    0x614: v614(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v612(0x1f)
    0x615: v615(0x3f) = CONST 
    0x617: v617 = RETURNDATASIZE 
    0x618: v618 = ADD v617, v615(0x3f)
    0x619: v619 = AND v618, v614(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x61b: v61b = ADD v60f, v619
    0x61c: v61c(0x40) = CONST 
    0x61e: MSTORE v61c(0x40), v61b
    0x61f: v61f = RETURNDATASIZE 
    0x621: MSTORE v60f, v61f
    0x622: v622 = RETURNDATASIZE 
    0x623: v623(0x0) = CONST 
    0x625: v625(0x20) = CONST 
    0x628: v628 = ADD v60f, v625(0x20)
    0x629: RETURNDATACOPY v628, v623(0x0), v622
    0x62a: v62a(0x405) = CONST 
    0x62d: JUMP v62a(0x405)

    Begin block 0x4050x1c7
    prev=[0x60d, 0x4000x1c7], succ=[0x40f0x1c7, 0x4130x1c7]
    =================================
    0x40b0x1c7: v1c740b(0x413) = CONST 
    0x40e0x1c7: JUMPI v1c740b(0x413), v5ff

    Begin block 0x40f0x1c7
    prev=[0x4050x1c7], succ=[]
    =================================
    0x40f0x1c7: v1c740f(0x0) = CONST 
    0x4120x1c7: REVERT v1c740f(0x0), v1c740f(0x0)

    Begin block 0x4130x1c7
    prev=[0x4050x1c7], succ=[0xabe]
    =================================
    0x4180x1c7: JUMP v1c8(0xabe)

    Begin block 0xabe
    prev=[0x62e, 0x4130x1c7], succ=[]
    =================================
    0xabf: STOP 

    Begin block 0x4000x1c7
    prev=[0x5ce], succ=[0x4050x1c7]
    =================================
    0x4010x1c7: v1c7401(0x60) = CONST 

    Begin block 0x5b8
    prev=[0x5af], succ=[0x5af]
    =================================
    0x5b8_0x0: v5b8_0 = PHI v5aa, v5c9
    0x5b8_0x1: v5b8_1 = PHI v5a2, v5c7
    0x5b8_0x2: v5b8_2 = PHI v5a6, v5c1
    0x5b9: v5b9 = MLOAD v5b8_0
    0x5bb: MSTORE v5b8_1, v5b9
    0x5bc: v5bc(0x1f) = CONST 
    0x5be: v5be(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v5bc(0x1f)
    0x5c1: v5c1 = ADD v5b8_2, v5be(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x5c3: v5c3(0x20) = CONST 
    0x5c7: v5c7 = ADD v5c3(0x20), v5b8_1
    0x5c9: v5c9 = ADD v5c3(0x20), v5b8_0
    0x5ca: v5ca(0x5af) = CONST 
    0x5cd: JUMP v5ca(0x5af)

    Begin block 0x62e
    prev=[0x58b], succ=[0xabe]
    =================================
    0x632: JUMP v1c8(0xabe)

}

function transferGovernance(address)() public {
    Begin block 0x286
    prev=[], succ=[0x28e, 0x292]
    =================================
    0x287: v287 = CALLVALUE 
    0x289: v289 = ISZERO v287
    0x28a: v28a(0x292) = CONST 
    0x28d: JUMPI v28a(0x292), v289

    Begin block 0x28e
    prev=[0x286], succ=[]
    =================================
    0x28e: v28e(0x0) = CONST 
    0x291: REVERT v28e(0x0), v28e(0x0)

    Begin block 0x292
    prev=[0x286], succ=[0x2a5, 0x2a9]
    =================================
    0x294: v294(0xadf) = CONST 
    0x297: v297(0x4) = CONST 
    0x29a: v29a = CALLDATASIZE 
    0x29b: v29b = SUB v29a, v297(0x4)
    0x29c: v29c(0x20) = CONST 
    0x29f: v29f = LT v29b, v29c(0x20)
    0x2a0: v2a0 = ISZERO v29f
    0x2a1: v2a1(0x2a9) = CONST 
    0x2a4: JUMPI v2a1(0x2a9), v2a0

    Begin block 0x2a5
    prev=[0x292], succ=[]
    =================================
    0x2a5: v2a5(0x0) = CONST 
    0x2a8: REVERT v2a5(0x0), v2a5(0x0)

    Begin block 0x2a9
    prev=[0x292], succ=[0x633]
    =================================
    0x2ab: v2ab = CALLDATALOAD v297(0x4)
    0x2ac: v2ac(0x1) = CONST 
    0x2ae: v2ae(0x1) = CONST 
    0x2b0: v2b0(0xa0) = CONST 
    0x2b2: v2b2(0x10000000000000000000000000000000000000000) = SHL v2b0(0xa0), v2ae(0x1)
    0x2b3: v2b3(0xffffffffffffffffffffffffffffffffffffffff) = SUB v2b2(0x10000000000000000000000000000000000000000), v2ac(0x1)
    0x2b4: v2b4 = AND v2b3(0xffffffffffffffffffffffffffffffffffffffff), v2ab
    0x2b5: v2b5(0x633) = CONST 
    0x2b8: JUMP v2b5(0x633)

    Begin block 0x633
    prev=[0x2a9], succ=[0x483B0x633]
    =================================
    0x634: v634(0x63b) = CONST 
    0x637: v637(0x483) = CONST 
    0x63a: JUMP v637(0x483)

    Begin block 0x483B0x633
    prev=[0x633], succ=[0x725B0x483B0x633]
    =================================
    0x484S0x633: v484V633(0x0) = CONST 
    0x486S0x633: v486V633(0x48d) = CONST 
    0x489S0x633: v489V633(0x725) = CONST 
    0x48cS0x633: JUMP v489V633(0x725)

    Begin block 0x725B0x483B0x633
    prev=[0x483B0x633], succ=[0x48dB0x633]
    =================================
    0x726S0x483S0x633: v726V483V633(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x483S0x633: v747V483V633 = SLOAD v726V483V633(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x483S0x633: JUMP v486V633(0x48d)

    Begin block 0x48dB0x633
    prev=[0x725B0x483B0x633], succ=[0x63b]
    =================================
    0x48eS0x633: v48eV633(0x1) = CONST 
    0x490S0x633: v490V633(0x1) = CONST 
    0x492S0x633: v492V633(0xa0) = CONST 
    0x494S0x633: v494V633(0x10000000000000000000000000000000000000000) = SHL v492V633(0xa0), v490V633(0x1)
    0x495S0x633: v495V633(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494V633(0x10000000000000000000000000000000000000000), v48eV633(0x1)
    0x496S0x633: v496V633 = AND v495V633(0xffffffffffffffffffffffffffffffffffffffff), v747V483V633
    0x497S0x633: v497V633 = CALLER 
    0x498S0x633: v498V633(0x1) = CONST 
    0x49aS0x633: v49aV633(0x1) = CONST 
    0x49cS0x633: v49cV633(0xa0) = CONST 
    0x49eS0x633: v49eV633(0x10000000000000000000000000000000000000000) = SHL v49cV633(0xa0), v49aV633(0x1)
    0x49fS0x633: v49fV633(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49eV633(0x10000000000000000000000000000000000000000), v498V633(0x1)
    0x4a0S0x633: v4a0V633 = AND v49fV633(0xffffffffffffffffffffffffffffffffffffffff), v497V633
    0x4a1S0x633: v4a1V633 = EQ v4a0V633, v496V633
    0x4a5S0x633: JUMP v634(0x63b)

    Begin block 0x63b
    prev=[0x48dB0x633], succ=[0x640, 0x689]
    =================================
    0x63c: v63c(0x689) = CONST 
    0x63f: JUMPI v63c(0x689), v4a1V633

    Begin block 0x640
    prev=[0x63b], succ=[]
    =================================
    0x640: v640(0x40) = CONST 
    0x643: v643 = MLOAD v640(0x40)
    0x644: v644(0x461bcd) = CONST 
    0x648: v648(0xe5) = CONST 
    0x64a: v64a(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v648(0xe5), v644(0x461bcd)
    0x64c: MSTORE v643, v64a(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x64d: v64d(0x20) = CONST 
    0x64f: v64f(0x4) = CONST 
    0x652: v652 = ADD v643, v64f(0x4)
    0x653: MSTORE v652, v64d(0x20)
    0x654: v654(0x1a) = CONST 
    0x656: v656(0x24) = CONST 
    0x659: v659 = ADD v643, v656(0x24)
    0x65a: MSTORE v659, v654(0x1a)
    0x65b: v65b(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9) = CONST 
    0x676: v676(0x31) = CONST 
    0x678: v678(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = SHL v676(0x31), v65b(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9)
    0x679: v679(0x44) = CONST 
    0x67c: v67c = ADD v643, v679(0x44)
    0x67d: MSTORE v67c, v678(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x67f: v67f = MLOAD v640(0x40)
    0x683: v683(0x0) = SUB v643, v67f
    0x684: v684(0x64) = CONST 
    0x686: v686(0x64) = ADD v684(0x64), v683(0x0)
    0x688: REVERT v67f, v686(0x64)

    Begin block 0x689
    prev=[0x63b], succ=[0x8c2]
    =================================
    0x68a: v68a(0x692) = CONST 
    0x68e: v68e(0x8c2) = CONST 
    0x691: JUMP v68e(0x8c2)

    Begin block 0x8c2
    prev=[0x689], succ=[0x692]
    =================================
    0x8c3: v8c3(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db) = CONST 
    0x8e4: SSTORE v8c3(0x44c4d30b2eaad5130ad70c3ba6972730566f3e6359ab83e800d905c61b1c51db), v2b4
    0x8e5: JUMP v68a(0x692)

    Begin block 0x692
    prev=[0x8c2], succ=[0x725B0x692]
    =================================
    0x694: v694(0x1) = CONST 
    0x696: v696(0x1) = CONST 
    0x698: v698(0xa0) = CONST 
    0x69a: v69a(0x10000000000000000000000000000000000000000) = SHL v698(0xa0), v696(0x1)
    0x69b: v69b(0xffffffffffffffffffffffffffffffffffffffff) = SUB v69a(0x10000000000000000000000000000000000000000), v694(0x1)
    0x69c: v69c = AND v69b(0xffffffffffffffffffffffffffffffffffffffff), v2b4
    0x69d: v69d(0x6a4) = CONST 
    0x6a0: v6a0(0x725) = CONST 
    0x6a3: JUMP v6a0(0x725)

    Begin block 0x725B0x692
    prev=[0x692], succ=[0x6a4]
    =================================
    0x726S0x692: v726V692(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x692: v747V692 = SLOAD v726V692(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x692: JUMP v69d(0x6a4)

    Begin block 0x6a4
    prev=[0x725B0x692], succ=[0xadf]
    =================================
    0x6a5: v6a5(0x1) = CONST 
    0x6a7: v6a7(0x1) = CONST 
    0x6a9: v6a9(0xa0) = CONST 
    0x6ab: v6ab(0x10000000000000000000000000000000000000000) = SHL v6a9(0xa0), v6a7(0x1)
    0x6ac: v6ac(0xffffffffffffffffffffffffffffffffffffffff) = SUB v6ab(0x10000000000000000000000000000000000000000), v6a5(0x1)
    0x6ad: v6ad = AND v6ac(0xffffffffffffffffffffffffffffffffffffffff), v747V692
    0x6ae: v6ae(0xa39cc5eb22d0f34d8beaefee8a3f17cc229c1a1d1ef87a5ad47313487b1c4f0d) = CONST 
    0x6cf: v6cf(0x40) = CONST 
    0x6d1: v6d1 = MLOAD v6cf(0x40)
    0x6d2: v6d2(0x40) = CONST 
    0x6d4: v6d4 = MLOAD v6d2(0x40)
    0x6d7: v6d7(0x0) = SUB v6d1, v6d4
    0x6d9: LOG3 v6d4, v6d7(0x0), v6ae(0xa39cc5eb22d0f34d8beaefee8a3f17cc229c1a1d1ef87a5ad47313487b1c4f0d), v6ad, v69c
    0x6db: JUMP v294(0xadf)

    Begin block 0xadf
    prev=[0x6a4], succ=[]
    =================================
    0xae0: STOP 

}

function 0x7af(0x7afarg0x0, 0x7afarg0x1) private {
    Begin block 0x7af
    prev=[], succ=[0x7be, 0x80a]
    =================================
    0x7b0: v7b0(0x1) = CONST 
    0x7b2: v7b2(0x1) = CONST 
    0x7b4: v7b4(0xa0) = CONST 
    0x7b6: v7b6(0x10000000000000000000000000000000000000000) = SHL v7b4(0xa0), v7b2(0x1)
    0x7b7: v7b7(0xffffffffffffffffffffffffffffffffffffffff) = SUB v7b6(0x10000000000000000000000000000000000000000), v7b0(0x1)
    0x7b9: v7b9 = AND v7afarg0, v7b7(0xffffffffffffffffffffffffffffffffffffffff)
    0x7ba: v7ba(0x80a) = CONST 
    0x7bd: JUMPI v7ba(0x80a), v7b9

    Begin block 0x7be
    prev=[0x7af], succ=[]
    =================================
    0x7be: v7be(0x40) = CONST 
    0x7c1: v7c1 = MLOAD v7be(0x40)
    0x7c2: v7c2(0x461bcd) = CONST 
    0x7c6: v7c6(0xe5) = CONST 
    0x7c8: v7c8(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v7c6(0xe5), v7c2(0x461bcd)
    0x7ca: MSTORE v7c1, v7c8(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x7cb: v7cb(0x20) = CONST 
    0x7cd: v7cd(0x4) = CONST 
    0x7d0: v7d0 = ADD v7c1, v7cd(0x4)
    0x7d1: MSTORE v7d0, v7cb(0x20)
    0x7d2: v7d2(0x1a) = CONST 
    0x7d4: v7d4(0x24) = CONST 
    0x7d7: v7d7 = ADD v7c1, v7d4(0x24)
    0x7d8: MSTORE v7d7, v7d2(0x1a)
    0x7d9: v7d9(0x4e657720476f7665726e6f722069732061646472657373283029000000000000) = CONST 
    0x7fa: v7fa(0x44) = CONST 
    0x7fd: v7fd = ADD v7c1, v7fa(0x44)
    0x7fe: MSTORE v7fd, v7d9(0x4e657720476f7665726e6f722069732061646472657373283029000000000000)
    0x800: v800 = MLOAD v7be(0x40)
    0x804: v804(0x0) = SUB v7c1, v800
    0x805: v805(0x64) = CONST 
    0x807: v807(0x64) = ADD v805(0x64), v804(0x0)
    0x809: REVERT v800, v807(0x64)

    Begin block 0x80a
    prev=[0x7af], succ=[0x725B0x80a]
    =================================
    0x80c: v80c(0x1) = CONST 
    0x80e: v80e(0x1) = CONST 
    0x810: v810(0xa0) = CONST 
    0x812: v812(0x10000000000000000000000000000000000000000) = SHL v810(0xa0), v80e(0x1)
    0x813: v813(0xffffffffffffffffffffffffffffffffffffffff) = SUB v812(0x10000000000000000000000000000000000000000), v80c(0x1)
    0x814: v814 = AND v813(0xffffffffffffffffffffffffffffffffffffffff), v7afarg0
    0x815: v815(0x81c) = CONST 
    0x818: v818(0x725) = CONST 
    0x81b: JUMP v818(0x725)

    Begin block 0x725B0x80a
    prev=[0x80a], succ=[0x81c]
    =================================
    0x726S0x80a: v726V80a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x80a: v747V80a = SLOAD v726V80a(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x80a: JUMP v815(0x81c)

    Begin block 0x81c
    prev=[0x725B0x80a], succ=[0x8e6]
    =================================
    0x81d: v81d(0x1) = CONST 
    0x81f: v81f(0x1) = CONST 
    0x821: v821(0xa0) = CONST 
    0x823: v823(0x10000000000000000000000000000000000000000) = SHL v821(0xa0), v81f(0x1)
    0x824: v824(0xffffffffffffffffffffffffffffffffffffffff) = SUB v823(0x10000000000000000000000000000000000000000), v81d(0x1)
    0x825: v825 = AND v824(0xffffffffffffffffffffffffffffffffffffffff), v747V80a
    0x826: v826(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a) = CONST 
    0x847: v847(0x40) = CONST 
    0x849: v849 = MLOAD v847(0x40)
    0x84a: v84a(0x40) = CONST 
    0x84c: v84c = MLOAD v84a(0x40)
    0x84f: v84f(0x0) = SUB v849, v84c
    0x851: LOG3 v84c, v84f(0x0), v826(0xc7c0c772add429241571afb3805861fb3cfa2af374534088b76cdb4325a87e9a), v825, v814
    0x852: v852(0xbcd) = CONST 
    0x856: v856(0x8e6) = CONST 
    0x859: JUMP v856(0x8e6)

    Begin block 0x8e6
    prev=[0x81c], succ=[0xbcd]
    =================================
    0x8e7: v8e7(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x908: SSTORE v8e7(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a), v7afarg0
    0x909: JUMP v852(0xbcd)

    Begin block 0xbcd
    prev=[0x8e6], succ=[]
    =================================
    0xbcf: RETURNPRIVATE v7afarg1

}

function 0x85a(0x85aarg0x0, 0x85aarg0x1) private {
    Begin block 0x85a
    prev=[], succ=[0x90a]
    =================================
    0x85b: v85b(0x863) = CONST 
    0x85f: v85f(0x90a) = CONST 
    0x862: JUMP v85f(0x90a)

    Begin block 0x90a
    prev=[0x85a], succ=[0x863]
    =================================
    0x90b: v90b = EXTCODESIZE v85aarg0
    0x90c: v90c = ISZERO v90b
    0x90d: v90d = ISZERO v90c
    0x90f: JUMP v85b(0x863)

    Begin block 0x863
    prev=[0x90a], succ=[0x868, 0x89e]
    =================================
    0x864: v864(0x89e) = CONST 
    0x867: JUMPI v864(0x89e), v90d

    Begin block 0x868
    prev=[0x863], succ=[]
    =================================
    0x868: v868(0x40) = CONST 
    0x86a: v86a = MLOAD v868(0x40)
    0x86b: v86b(0x461bcd) = CONST 
    0x86f: v86f(0xe5) = CONST 
    0x871: v871(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v86f(0xe5), v86b(0x461bcd)
    0x873: MSTORE v86a, v871(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x874: v874(0x4) = CONST 
    0x876: v876 = ADD v874(0x4), v86a
    0x879: v879(0x20) = CONST 
    0x87b: v87b = ADD v879(0x20), v876
    0x87e: v87e(0x20) = SUB v87b, v876
    0x880: MSTORE v876, v87e(0x20)
    0x881: v881(0x3b) = CONST 
    0x884: MSTORE v87b, v881(0x3b)
    0x885: v885(0x20) = CONST 
    0x887: v887 = ADD v885(0x20), v87b
    0x889: v889(0x911) = CONST 
    0x88c: v88c(0x3b) = CONST 
    0x88f: CODECOPY v887, v889(0x911), v88c(0x3b)
    0x890: v890(0x40) = CONST 
    0x892: v892 = ADD v890(0x40), v887
    0x896: v896(0x40) = CONST 
    0x898: v898 = MLOAD v896(0x40)
    0x89b: v89b(0x84) = SUB v892, v898
    0x89d: REVERT v898, v89b(0x84)

    Begin block 0x89e
    prev=[0x863], succ=[]
    =================================
    0x89f: v89f(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x8c0: SSTORE v89f(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc), v85aarg0
    0x8c1: RETURNPRIVATE v85aarg1

}

function fallback()() public {
    Begin block 0x86
    prev=[], succ=[0x2b9]
    =================================
    0x87: v87(0x9c4) = CONST 
    0x8a: v8a(0x2b9) = CONST 
    0x8d: JUMP v8a(0x2b9)

    Begin block 0x2b9
    prev=[0x86], succ=[0xb00B0x2b9]
    =================================
    0x2ba: v2ba(0x2c1) = CONST 
    0x2bd: v2bd(0xb00) = CONST 
    0x2c0: JUMP v2bd(0xb00), v2ba(0x2c1)

    Begin block 0xb00B0x2b9
    prev=[0x2b9], succ=[0x2c1]
    =================================
    0xb01S0x2b9: JUMP v2ba(0x2c1)

    Begin block 0x2c1
    prev=[0xb00B0x2b9], succ=[0x6dcB0x2c1]
    =================================
    0x2c2: v2c2(0xb21) = CONST 
    0x2c5: v2c5(0x2cc) = CONST 
    0x2c8: v2c8(0x6dc) = CONST 
    0x2cb: JUMP v2c8(0x6dc)

    Begin block 0x6dcB0x2c1
    prev=[0x2c1], succ=[0x2cc]
    =================================
    0x6ddS0x2c1: v6ddV2c1(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc) = CONST 
    0x6feS0x2c1: v6feV2c1 = SLOAD v6ddV2c1(0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    0x700S0x2c1: JUMP v2c5(0x2cc)

    Begin block 0x2cc
    prev=[0x6dcB0x2c1], succ=[0x701]
    =================================
    0x2cd: v2cd(0x701) = CONST 
    0x2d0: JUMP v2cd(0x701)

    Begin block 0x701
    prev=[0x2cc], succ=[0x71c, 0x720]
    =================================
    0x702: v702 = CALLDATASIZE 
    0x703: v703(0x0) = CONST 
    0x706: CALLDATACOPY v703(0x0), v703(0x0), v702
    0x707: v707(0x0) = CONST 
    0x70a: v70a = CALLDATASIZE 
    0x70b: v70b(0x0) = CONST 
    0x70e: v70e = GAS 
    0x70f: v70f = DELEGATECALL v70e, v6feV2c1, v70b(0x0), v70a, v707(0x0), v707(0x0)
    0x710: v710 = RETURNDATASIZE 
    0x711: v711(0x0) = CONST 
    0x714: RETURNDATACOPY v711(0x0), v711(0x0), v710
    0x717: v717 = ISZERO v70f
    0x718: v718(0x720) = CONST 
    0x71b: JUMPI v718(0x720), v717

    Begin block 0x71c
    prev=[0x701], succ=[]
    =================================
    0x71c: v71c = RETURNDATASIZE 
    0x71d: v71d(0x0) = CONST 
    0x71f: RETURN v71d(0x0), v71c

    Begin block 0x720
    prev=[0x701], succ=[]
    =================================
    0x721: v721 = RETURNDATASIZE 
    0x722: v722(0x0) = CONST 
    0x724: REVERT v722(0x0), v721

}

function admin()() public {
    Begin block 0x90
    prev=[], succ=[0x98, 0x9c]
    =================================
    0x91: v91 = CALLVALUE 
    0x93: v93 = ISZERO v91
    0x94: v94(0x9c) = CONST 
    0x97: JUMPI v94(0x9c), v93

    Begin block 0x98
    prev=[0x90], succ=[]
    =================================
    0x98: v98(0x0) = CONST 
    0x9b: REVERT v98(0x0), v98(0x0)

    Begin block 0x9c
    prev=[0x90], succ=[0x2d3B0x9c]
    =================================
    0x9e: v9e(0x9e5) = CONST 
    0xa1: va1(0x2d3) = CONST 
    0xa4: JUMP va1(0x2d3)

    Begin block 0x2d3B0x9c
    prev=[0x9c], succ=[0x725B0x2d3B0x9c]
    =================================
    0x2d4S0x9c: v2d4V9c(0x0) = CONST 
    0x2d6S0x9c: v2d6V9c(0xb42) = CONST 
    0x2d9S0x9c: v2d9V9c(0x725) = CONST 
    0x2dcS0x9c: JUMP v2d9V9c(0x725)

    Begin block 0x725B0x2d3B0x9c
    prev=[0x2d3B0x9c], succ=[0xb42B0x9c]
    =================================
    0x726S0x2d3S0x9c: v726V2d3V9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x2d3S0x9c: v747V2d3V9c = SLOAD v726V2d3V9c(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x2d3S0x9c: JUMP v2d6V9c(0xb42)

    Begin block 0xb42B0x9c
    prev=[0x725B0x2d3B0x9c], succ=[0x9e5]
    =================================
    0xb46S0x9c: JUMP v9e(0x9e5)

    Begin block 0x9e5
    prev=[0xb42B0x9c], succ=[]
    =================================
    0x9e6: v9e6(0x40) = CONST 
    0x9e9: v9e9 = MLOAD v9e6(0x40)
    0x9ea: v9ea(0x1) = CONST 
    0x9ec: v9ec(0x1) = CONST 
    0x9ee: v9ee(0xa0) = CONST 
    0x9f0: v9f0(0x10000000000000000000000000000000000000000) = SHL v9ee(0xa0), v9ec(0x1)
    0x9f1: v9f1(0xffffffffffffffffffffffffffffffffffffffff) = SUB v9f0(0x10000000000000000000000000000000000000000), v9ea(0x1)
    0x9f4: v9f4 = AND v747V2d3V9c, v9f1(0xffffffffffffffffffffffffffffffffffffffff)
    0x9f6: MSTORE v9e9, v9f4
    0x9f7: v9f7 = MLOAD v9e6(0x40)
    0x9fb: v9fb(0x0) = SUB v9e9, v9f7
    0x9fc: v9fc(0x20) = CONST 
    0x9fe: v9fe(0x20) = ADD v9fc(0x20), v9fb(0x0)
    0xa00: RETURN v9f7, v9fe(0x20)

}

function upgradeTo(address)() public {
    Begin block 0xc1
    prev=[], succ=[0xc9, 0xcd]
    =================================
    0xc2: vc2 = CALLVALUE 
    0xc4: vc4 = ISZERO vc2
    0xc5: vc5(0xcd) = CONST 
    0xc8: JUMPI vc5(0xcd), vc4

    Begin block 0xc9
    prev=[0xc1], succ=[]
    =================================
    0xc9: vc9(0x0) = CONST 
    0xcc: REVERT vc9(0x0), vc9(0x0)

    Begin block 0xcd
    prev=[0xc1], succ=[0xe0, 0xe4]
    =================================
    0xcf: vcf(0xa20) = CONST 
    0xd2: vd2(0x4) = CONST 
    0xd5: vd5 = CALLDATASIZE 
    0xd6: vd6 = SUB vd5, vd2(0x4)
    0xd7: vd7(0x20) = CONST 
    0xda: vda = LT vd6, vd7(0x20)
    0xdb: vdb = ISZERO vda
    0xdc: vdc(0xe4) = CONST 
    0xdf: JUMPI vdc(0xe4), vdb

    Begin block 0xe0
    prev=[0xcd], succ=[]
    =================================
    0xe0: ve0(0x0) = CONST 
    0xe3: REVERT ve0(0x0), ve0(0x0)

    Begin block 0xe4
    prev=[0xcd], succ=[0x2e2]
    =================================
    0xe6: ve6 = CALLDATALOAD vd2(0x4)
    0xe7: ve7(0x1) = CONST 
    0xe9: ve9(0x1) = CONST 
    0xeb: veb(0xa0) = CONST 
    0xed: ved(0x10000000000000000000000000000000000000000) = SHL veb(0xa0), ve9(0x1)
    0xee: vee(0xffffffffffffffffffffffffffffffffffffffff) = SUB ved(0x10000000000000000000000000000000000000000), ve7(0x1)
    0xef: vef = AND vee(0xffffffffffffffffffffffffffffffffffffffff), ve6
    0xf0: vf0(0x2e2) = CONST 
    0xf3: JUMP vf0(0x2e2)

    Begin block 0x2e2
    prev=[0xe4], succ=[0x483B0x2e2]
    =================================
    0x2e3: v2e3(0x2ea) = CONST 
    0x2e6: v2e6(0x483) = CONST 
    0x2e9: JUMP v2e6(0x483)

    Begin block 0x483B0x2e2
    prev=[0x2e2], succ=[0x725B0x483B0x2e2]
    =================================
    0x484S0x2e2: v484V2e2(0x0) = CONST 
    0x486S0x2e2: v486V2e2(0x48d) = CONST 
    0x489S0x2e2: v489V2e2(0x725) = CONST 
    0x48cS0x2e2: JUMP v489V2e2(0x725)

    Begin block 0x725B0x483B0x2e2
    prev=[0x483B0x2e2], succ=[0x48dB0x2e2]
    =================================
    0x726S0x483S0x2e2: v726V483V2e2(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x483S0x2e2: v747V483V2e2 = SLOAD v726V483V2e2(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x483S0x2e2: JUMP v486V2e2(0x48d)

    Begin block 0x48dB0x2e2
    prev=[0x725B0x483B0x2e2], succ=[0x2ea]
    =================================
    0x48eS0x2e2: v48eV2e2(0x1) = CONST 
    0x490S0x2e2: v490V2e2(0x1) = CONST 
    0x492S0x2e2: v492V2e2(0xa0) = CONST 
    0x494S0x2e2: v494V2e2(0x10000000000000000000000000000000000000000) = SHL v492V2e2(0xa0), v490V2e2(0x1)
    0x495S0x2e2: v495V2e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494V2e2(0x10000000000000000000000000000000000000000), v48eV2e2(0x1)
    0x496S0x2e2: v496V2e2 = AND v495V2e2(0xffffffffffffffffffffffffffffffffffffffff), v747V483V2e2
    0x497S0x2e2: v497V2e2 = CALLER 
    0x498S0x2e2: v498V2e2(0x1) = CONST 
    0x49aS0x2e2: v49aV2e2(0x1) = CONST 
    0x49cS0x2e2: v49cV2e2(0xa0) = CONST 
    0x49eS0x2e2: v49eV2e2(0x10000000000000000000000000000000000000000) = SHL v49cV2e2(0xa0), v49aV2e2(0x1)
    0x49fS0x2e2: v49fV2e2(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49eV2e2(0x10000000000000000000000000000000000000000), v498V2e2(0x1)
    0x4a0S0x2e2: v4a0V2e2 = AND v49fV2e2(0xffffffffffffffffffffffffffffffffffffffff), v497V2e2
    0x4a1S0x2e2: v4a1V2e2 = EQ v4a0V2e2, v496V2e2
    0x4a5S0x2e2: JUMP v2e3(0x2ea)

    Begin block 0x2ea
    prev=[0x48dB0x2e2], succ=[0x2ef, 0x338]
    =================================
    0x2eb: v2eb(0x338) = CONST 
    0x2ee: JUMPI v2eb(0x338), v4a1V2e2

    Begin block 0x2ef
    prev=[0x2ea], succ=[]
    =================================
    0x2ef: v2ef(0x40) = CONST 
    0x2f2: v2f2 = MLOAD v2ef(0x40)
    0x2f3: v2f3(0x461bcd) = CONST 
    0x2f7: v2f7(0xe5) = CONST 
    0x2f9: v2f9(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v2f7(0xe5), v2f3(0x461bcd)
    0x2fb: MSTORE v2f2, v2f9(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x2fc: v2fc(0x20) = CONST 
    0x2fe: v2fe(0x4) = CONST 
    0x301: v301 = ADD v2f2, v2fe(0x4)
    0x302: MSTORE v301, v2fc(0x20)
    0x303: v303(0x1a) = CONST 
    0x305: v305(0x24) = CONST 
    0x308: v308 = ADD v2f2, v305(0x24)
    0x309: MSTORE v308, v303(0x1a)
    0x30a: v30a(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9) = CONST 
    0x325: v325(0x31) = CONST 
    0x327: v327(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = SHL v325(0x31), v30a(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9)
    0x328: v328(0x44) = CONST 
    0x32b: v32b = ADD v2f2, v328(0x44)
    0x32c: MSTORE v32b, v327(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x32e: v32e = MLOAD v2ef(0x40)
    0x332: v332(0x0) = SUB v2f2, v32e
    0x333: v333(0x64) = CONST 
    0x335: v335(0x64) = ADD v333(0x64), v332(0x0)
    0x337: REVERT v32e, v335(0x64)

    Begin block 0x338
    prev=[0x2ea], succ=[0x74aB0x338]
    =================================
    0x339: v339(0xb66) = CONST 
    0x33d: v33d(0x74a) = CONST 
    0x340: JUMP v33d(0x74a), vef, v339(0xb66)

    Begin block 0x74aB0x338
    prev=[0x338], succ=[0x753B0x338]
    =================================
    0x74bS0x338: v74bV338(0x753) = CONST 
    0x74fS0x338: v74fV338(0x85a) = CONST 
    0x752S0x338: CALLPRIVATE v74fV338(0x85a), vef, v74bV338(0x753)

    Begin block 0x753B0x338
    prev=[0x74aB0x338], succ=[0xb66]
    =================================
    0x754S0x338: v754V338(0x40) = CONST 
    0x756S0x338: v756V338 = MLOAD v754V338(0x40)
    0x757S0x338: v757V338(0x1) = CONST 
    0x759S0x338: v759V338(0x1) = CONST 
    0x75bS0x338: v75bV338(0xa0) = CONST 
    0x75dS0x338: v75dV338(0x10000000000000000000000000000000000000000) = SHL v75bV338(0xa0), v759V338(0x1)
    0x75eS0x338: v75eV338(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75dV338(0x10000000000000000000000000000000000000000), v757V338(0x1)
    0x760S0x338: v760V338 = AND vef, v75eV338(0xffffffffffffffffffffffffffffffffffffffff)
    0x762S0x338: v762V338(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x784S0x338: v784V338(0x0) = CONST 
    0x787S0x338: LOG2 v756V338, v784V338(0x0), v762V338(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v760V338
    0x789S0x338: JUMP v339(0xb66)

    Begin block 0xb66
    prev=[0x753B0x338], succ=[0xa20]
    =================================
    0xb68: JUMP vcf(0xa20)

    Begin block 0xa20
    prev=[0xb66], succ=[]
    =================================
    0xa21: STOP 

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xf4
    prev=[], succ=[0x106, 0x10a]
    =================================
    0xf5: vf5(0xa41) = CONST 
    0xf8: vf8(0x4) = CONST 
    0xfb: vfb = CALLDATASIZE 
    0xfc: vfc = SUB vfb, vf8(0x4)
    0xfd: vfd(0x40) = CONST 
    0x100: v100 = LT vfc, vfd(0x40)
    0x101: v101 = ISZERO v100
    0x102: v102(0x10a) = CONST 
    0x105: JUMPI v102(0x10a), v101

    Begin block 0x106
    prev=[0xf4], succ=[]
    =================================
    0x106: v106(0x0) = CONST 
    0x109: REVERT v106(0x0), v106(0x0)

    Begin block 0x10a
    prev=[0xf4], succ=[0x131, 0x135]
    =================================
    0x10b: v10b(0x1) = CONST 
    0x10d: v10d(0x1) = CONST 
    0x10f: v10f(0xa0) = CONST 
    0x111: v111(0x10000000000000000000000000000000000000000) = SHL v10f(0xa0), v10d(0x1)
    0x112: v112(0xffffffffffffffffffffffffffffffffffffffff) = SUB v111(0x10000000000000000000000000000000000000000), v10b(0x1)
    0x114: v114 = CALLDATALOAD vf8(0x4)
    0x115: v115 = AND v114, v112(0xffffffffffffffffffffffffffffffffffffffff)
    0x119: v119 = ADD vf8(0x4), vfc
    0x11b: v11b(0x40) = CONST 
    0x11e: v11e(0x44) = ADD vf8(0x4), v11b(0x40)
    0x11f: v11f(0x20) = CONST 
    0x122: v122(0x24) = ADD vf8(0x4), v11f(0x20)
    0x123: v123 = CALLDATALOAD v122(0x24)
    0x124: v124(0x100000000) = CONST 
    0x12b: v12b = GT v123, v124(0x100000000)
    0x12c: v12c = ISZERO v12b
    0x12d: v12d(0x135) = CONST 
    0x130: JUMPI v12d(0x135), v12c

    Begin block 0x131
    prev=[0x10a], succ=[]
    =================================
    0x131: v131(0x0) = CONST 
    0x134: REVERT v131(0x0), v131(0x0)

    Begin block 0x135
    prev=[0x10a], succ=[0x143, 0x147]
    =================================
    0x137: v137 = ADD vf8(0x4), v123
    0x139: v139(0x20) = CONST 
    0x13c: v13c = ADD v137, v139(0x20)
    0x13d: v13d = GT v13c, v119
    0x13e: v13e = ISZERO v13d
    0x13f: v13f(0x147) = CONST 
    0x142: JUMPI v13f(0x147), v13e

    Begin block 0x143
    prev=[0x135], succ=[]
    =================================
    0x143: v143(0x0) = CONST 
    0x146: REVERT v143(0x0), v143(0x0)

    Begin block 0x147
    prev=[0x135], succ=[0x165, 0x169]
    =================================
    0x149: v149 = CALLDATALOAD v137
    0x14b: v14b(0x20) = CONST 
    0x14d: v14d = ADD v14b(0x20), v137
    0x150: v150(0x1) = CONST 
    0x153: v153 = MUL v149, v150(0x1)
    0x155: v155 = ADD v14d, v153
    0x156: v156 = GT v155, v119
    0x157: v157(0x100000000) = CONST 
    0x15e: v15e = GT v149, v157(0x100000000)
    0x15f: v15f = OR v15e, v156
    0x160: v160 = ISZERO v15f
    0x161: v161(0x169) = CONST 
    0x164: JUMPI v161(0x169), v160

    Begin block 0x165
    prev=[0x147], succ=[]
    =================================
    0x165: v165(0x0) = CONST 
    0x168: REVERT v165(0x0), v165(0x0)

    Begin block 0x169
    prev=[0x147], succ=[0x344]
    =================================
    0x170: v170(0x344) = CONST 
    0x173: JUMP v170(0x344)

    Begin block 0x344
    prev=[0x169], succ=[0x483B0x344]
    =================================
    0x345: v345(0x34c) = CONST 
    0x348: v348(0x483) = CONST 
    0x34b: JUMP v348(0x483)

    Begin block 0x483B0x344
    prev=[0x344], succ=[0x725B0x483B0x344]
    =================================
    0x484S0x344: v484V344(0x0) = CONST 
    0x486S0x344: v486V344(0x48d) = CONST 
    0x489S0x344: v489V344(0x725) = CONST 
    0x48cS0x344: JUMP v489V344(0x725)

    Begin block 0x725B0x483B0x344
    prev=[0x483B0x344], succ=[0x48dB0x344]
    =================================
    0x726S0x483S0x344: v726V483V344(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a) = CONST 
    0x747S0x483S0x344: v747V483V344 = SLOAD v726V483V344(0x7bea13895fa79d2831e0a9e28edede30099005a50d652d8957cf8a607ee6ca4a)
    0x749S0x483S0x344: JUMP v486V344(0x48d)

    Begin block 0x48dB0x344
    prev=[0x725B0x483B0x344], succ=[0x34c]
    =================================
    0x48eS0x344: v48eV344(0x1) = CONST 
    0x490S0x344: v490V344(0x1) = CONST 
    0x492S0x344: v492V344(0xa0) = CONST 
    0x494S0x344: v494V344(0x10000000000000000000000000000000000000000) = SHL v492V344(0xa0), v490V344(0x1)
    0x495S0x344: v495V344(0xffffffffffffffffffffffffffffffffffffffff) = SUB v494V344(0x10000000000000000000000000000000000000000), v48eV344(0x1)
    0x496S0x344: v496V344 = AND v495V344(0xffffffffffffffffffffffffffffffffffffffff), v747V483V344
    0x497S0x344: v497V344 = CALLER 
    0x498S0x344: v498V344(0x1) = CONST 
    0x49aS0x344: v49aV344(0x1) = CONST 
    0x49cS0x344: v49cV344(0xa0) = CONST 
    0x49eS0x344: v49eV344(0x10000000000000000000000000000000000000000) = SHL v49cV344(0xa0), v49aV344(0x1)
    0x49fS0x344: v49fV344(0xffffffffffffffffffffffffffffffffffffffff) = SUB v49eV344(0x10000000000000000000000000000000000000000), v498V344(0x1)
    0x4a0S0x344: v4a0V344 = AND v49fV344(0xffffffffffffffffffffffffffffffffffffffff), v497V344
    0x4a1S0x344: v4a1V344 = EQ v4a0V344, v496V344
    0x4a5S0x344: JUMP v345(0x34c)

    Begin block 0x34c
    prev=[0x48dB0x344], succ=[0x351, 0x39a]
    =================================
    0x34d: v34d(0x39a) = CONST 
    0x350: JUMPI v34d(0x39a), v4a1V344

    Begin block 0x351
    prev=[0x34c], succ=[]
    =================================
    0x351: v351(0x40) = CONST 
    0x354: v354 = MLOAD v351(0x40)
    0x355: v355(0x461bcd) = CONST 
    0x359: v359(0xe5) = CONST 
    0x35b: v35b(0x8c379a000000000000000000000000000000000000000000000000000000000) = SHL v359(0xe5), v355(0x461bcd)
    0x35d: MSTORE v354, v35b(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x35e: v35e(0x20) = CONST 
    0x360: v360(0x4) = CONST 
    0x363: v363 = ADD v354, v360(0x4)
    0x364: MSTORE v363, v35e(0x20)
    0x365: v365(0x1a) = CONST 
    0x367: v367(0x24) = CONST 
    0x36a: v36a = ADD v354, v367(0x24)
    0x36b: MSTORE v36a, v365(0x1a)
    0x36c: v36c(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9) = CONST 
    0x387: v387(0x31) = CONST 
    0x389: v389(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000) = SHL v387(0x31), v36c(0x21b0b63632b91034b9903737ba103a34329023b7bb32b93737b9)
    0x38a: v38a(0x44) = CONST 
    0x38d: v38d = ADD v354, v38a(0x44)
    0x38e: MSTORE v38d, v389(0x43616c6c6572206973206e6f742074686520476f7665726e6f72000000000000)
    0x390: v390 = MLOAD v351(0x40)
    0x394: v394(0x0) = SUB v354, v390
    0x395: v395(0x64) = CONST 
    0x397: v397(0x64) = ADD v395(0x64), v394(0x0)
    0x399: REVERT v390, v397(0x64)

    Begin block 0x39a
    prev=[0x34c], succ=[0x74aB0x39a]
    =================================
    0x39b: v39b(0x3a3) = CONST 
    0x39f: v39f(0x74a) = CONST 
    0x3a2: JUMP v39f(0x74a), v115, v39b(0x3a3)

    Begin block 0x74aB0x39a
    prev=[0x39a], succ=[0x753B0x39a]
    =================================
    0x74bS0x39a: v74bV39a(0x753) = CONST 
    0x74fS0x39a: v74fV39a(0x85a) = CONST 
    0x752S0x39a: CALLPRIVATE v74fV39a(0x85a), v115, v74bV39a(0x753)

    Begin block 0x753B0x39a
    prev=[0x74aB0x39a], succ=[0x3a3]
    =================================
    0x754S0x39a: v754V39a(0x40) = CONST 
    0x756S0x39a: v756V39a = MLOAD v754V39a(0x40)
    0x757S0x39a: v757V39a(0x1) = CONST 
    0x759S0x39a: v759V39a(0x1) = CONST 
    0x75bS0x39a: v75bV39a(0xa0) = CONST 
    0x75dS0x39a: v75dV39a(0x10000000000000000000000000000000000000000) = SHL v75bV39a(0xa0), v759V39a(0x1)
    0x75eS0x39a: v75eV39a(0xffffffffffffffffffffffffffffffffffffffff) = SUB v75dV39a(0x10000000000000000000000000000000000000000), v757V39a(0x1)
    0x760S0x39a: v760V39a = AND v115, v75eV39a(0xffffffffffffffffffffffffffffffffffffffff)
    0x762S0x39a: v762V39a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x784S0x39a: v784V39a(0x0) = CONST 
    0x787S0x39a: LOG2 v756V39a, v784V39a(0x0), v762V39a(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b), v760V39a
    0x789S0x39a: JUMP v39b(0x3a3)

    Begin block 0x3a3
    prev=[0x753B0x39a], succ=[0x3df, 0x4000xf4]
    =================================
    0x3a4: v3a4(0x0) = CONST 
    0x3a7: v3a7(0x1) = CONST 
    0x3a9: v3a9(0x1) = CONST 
    0x3ab: v3ab(0xa0) = CONST 
    0x3ad: v3ad(0x10000000000000000000000000000000000000000) = SHL v3ab(0xa0), v3a9(0x1)
    0x3ae: v3ae(0xffffffffffffffffffffffffffffffffffffffff) = SUB v3ad(0x10000000000000000000000000000000000000000), v3a7(0x1)
    0x3af: v3af = AND v3ae(0xffffffffffffffffffffffffffffffffffffffff), v115
    0x3b2: v3b2(0x40) = CONST 
    0x3b4: v3b4 = MLOAD v3b2(0x40)
    0x3bb: CALLDATACOPY v3b4, v14d, v149
    0x3bc: v3bc(0x40) = CONST 
    0x3be: v3be = MLOAD v3bc(0x40)
    0x3c0: v3c0 = ADD v3b4, v149
    0x3c3: v3c3(0x0) = CONST 
    0x3cd: v3cd = SUB v3c0, v3be
    0x3d0: v3d0 = GAS 
    0x3d1: v3d1 = DELEGATECALL v3d0, v3af, v3be, v3cd, v3be, v3c3(0x0)
    0x3d5: v3d5 = RETURNDATASIZE 
    0x3d7: v3d7(0x0) = CONST 
    0x3da: v3da = EQ v3d5, v3d7(0x0)
    0x3db: v3db(0x400) = CONST 
    0x3de: JUMPI v3db(0x400), v3da

    Begin block 0x3df
    prev=[0x3a3], succ=[0x4050xf4]
    =================================
    0x3df: v3df(0x40) = CONST 
    0x3e1: v3e1 = MLOAD v3df(0x40)
    0x3e4: v3e4(0x1f) = CONST 
    0x3e6: v3e6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v3e4(0x1f)
    0x3e7: v3e7(0x3f) = CONST 
    0x3e9: v3e9 = RETURNDATASIZE 
    0x3ea: v3ea = ADD v3e9, v3e7(0x3f)
    0x3eb: v3eb = AND v3ea, v3e6(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x3ed: v3ed = ADD v3e1, v3eb
    0x3ee: v3ee(0x40) = CONST 
    0x3f0: MSTORE v3ee(0x40), v3ed
    0x3f1: v3f1 = RETURNDATASIZE 
    0x3f3: MSTORE v3e1, v3f1
    0x3f4: v3f4 = RETURNDATASIZE 
    0x3f5: v3f5(0x0) = CONST 
    0x3f7: v3f7(0x20) = CONST 
    0x3fa: v3fa = ADD v3e1, v3f7(0x20)
    0x3fb: RETURNDATACOPY v3fa, v3f5(0x0), v3f4
    0x3fc: v3fc(0x405) = CONST 
    0x3ff: JUMP v3fc(0x405)

    Begin block 0x4050xf4
    prev=[0x3df, 0x4000xf4], succ=[0x40f0xf4, 0x4130xf4]
    =================================
    0x40b0xf4: vf440b(0x413) = CONST 
    0x40e0xf4: JUMPI vf440b(0x413), v3d1

    Begin block 0x40f0xf4
    prev=[0x4050xf4], succ=[]
    =================================
    0x40f0xf4: vf440f(0x0) = CONST 
    0x4120xf4: REVERT vf440f(0x0), vf440f(0x0)

    Begin block 0x4130xf4
    prev=[0x4050xf4], succ=[0xa41]
    =================================
    0x4180xf4: JUMP vf5(0xa41)

    Begin block 0xa41
    prev=[0x4130xf4], succ=[]
    =================================
    0xa42: STOP 

    Begin block 0x4000xf4
    prev=[0x3a3], succ=[0x4050xf4]
    =================================
    0x4010xf4: vf4401(0x60) = CONST 

}

