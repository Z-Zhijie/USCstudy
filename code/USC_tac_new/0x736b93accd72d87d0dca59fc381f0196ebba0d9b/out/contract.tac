function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0xd, 0x82e]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0x4) = CONST 
    0x7: v7 = CALLDATASIZE 
    0x8: v8 = LT v7, v5(0x4)
    0x822: v822(0x82e) = CONST 
    0x823: JUMPI v822(0x82e), v8

    Begin block 0xd
    prev=[0x0], succ=[0x831, 0x1e]
    =================================
    0xd: vd(0x0) = CONST 
    0xf: vf = CALLDATALOAD vd(0x0)
    0x10: v10(0xe0) = CONST 
    0x12: v12 = SHR v10(0xe0), vf
    0x14: v14(0x3659cfe6) = CONST 
    0x19: v19 = EQ v14(0x3659cfe6), v12
    0x824: v824(0x831) = CONST 
    0x825: JUMPI v824(0x831), v19

    Begin block 0x831
    prev=[0xd], succ=[]
    =================================
    0x832: v832(0x59) = CONST 
    0x833: CALLPRIVATE v832(0x59)

    Begin block 0x1e
    prev=[0xd], succ=[0x834, 0x29]
    =================================
    0x1f: v1f(0x4f1ef286) = CONST 
    0x24: v24 = EQ v1f(0x4f1ef286), v12
    0x826: v826(0x834) = CONST 
    0x827: JUMPI v826(0x834), v24

    Begin block 0x834
    prev=[0x1e], succ=[]
    =================================
    0x835: v835(0xaa) = CONST 
    0x836: CALLPRIVATE v835(0xaa)

    Begin block 0x29
    prev=[0x1e], succ=[0x837, 0x34]
    =================================
    0x2a: v2a(0x5c60da1b) = CONST 
    0x2f: v2f = EQ v2a(0x5c60da1b), v12
    0x828: v828(0x837) = CONST 
    0x829: JUMPI v828(0x837), v2f

    Begin block 0x837
    prev=[0x29], succ=[]
    =================================
    0x838: v838(0x143) = CONST 
    0x839: CALLPRIVATE v838(0x143)

    Begin block 0x34
    prev=[0x29], succ=[0x3f, 0x83a]
    =================================
    0x35: v35(0x8f283970) = CONST 
    0x3a: v3a = EQ v35(0x8f283970), v12
    0x82a: v82a(0x83a) = CONST 
    0x82b: JUMPI v82a(0x83a), v3a

    Begin block 0x3f
    prev=[0x34], succ=[0x4a, 0x83d]
    =================================
    0x40: v40(0xf851a440) = CONST 
    0x45: v45 = EQ v40(0xf851a440), v12
    0x82c: v82c(0x83d) = CONST 
    0x82d: JUMPI v82c(0x83d), v45

    Begin block 0x4a
    prev=[0x3f], succ=[0x4f0x0]
    =================================
    0x4a: v4a(0x4f) = CONST 
    0x4d: JUMP v4a(0x4f)

    Begin block 0x4f0x0
    prev=[0x4a], succ=[0x2160x0]
    =================================
    0x500x0: v050(0x57) = CONST 
    0x530x0: v053(0x216) = CONST 
    0x560x0: JUMP v053(0x216)

    Begin block 0x2160x0
    prev=[0x4f0x0], succ=[0x21e0x0]
    =================================
    0x2170x0: v0217(0x21e) = CONST 
    0x21a0x0: v021a(0x514) = CONST 
    0x21d0x0: CALLPRIVATE v021a(0x514), v0217(0x21e)

    Begin block 0x21e0x0
    prev=[0x2160x0], succ=[0x5aaB0x21e0x0]
    =================================
    0x21f0x0: v021f(0x22e) = CONST 
    0x2220x0: v0222(0x229) = CONST 
    0x2250x0: v0225(0x5aa) = CONST 
    0x2280x0: JUMP v0225(0x5aa)

    Begin block 0x5aaB0x21e0x0
    prev=[0x21e0x0], succ=[0x2290x0]
    =================================
    0x5abS0x21e0x0: v5abV21e0(0x0) = CONST 
    0x5aeS0x21e0x0: v5aeV21e0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x21e0x0: v5cfV21e0(0x0) = CONST 
    0x5d1S0x21e0x0: v5d1V21e0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV21e0(0x0), v5aeV21e0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x21e0x0: v5d5V21e0 = SLOAD v5d1V21e0(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x21e0x0: JUMP v0222(0x229)

    Begin block 0x2290x0
    prev=[0x5aaB0x21e0x0], succ=[0x5db0x0]
    =================================
    0x22a0x0: v022a(0x5db) = CONST 
    0x22d0x0: JUMP v022a(0x5db)

    Begin block 0x5db0x0
    prev=[0x2290x0], succ=[0x5f80x0, 0x5fc0x0]
    =================================
    0x5dc0x0: v05dc = CALLDATASIZE 
    0x5dd0x0: v05dd(0x0) = CONST 
    0x5e00x0: CALLDATACOPY v05dd(0x0), v05dd(0x0), v05dc
    0x5e10x0: v05e1(0x0) = CONST 
    0x5e40x0: v05e4 = CALLDATASIZE 
    0x5e50x0: v05e5(0x0) = CONST 
    0x5e80x0: v05e8 = GAS 
    0x5e90x0: v05e9 = DELEGATECALL v05e8, v5d5V21e0, v05e5(0x0), v05e4, v05e1(0x0), v05e1(0x0)
    0x5ea0x0: v05ea = RETURNDATASIZE 
    0x5eb0x0: v05eb(0x0) = CONST 
    0x5ee0x0: RETURNDATACOPY v05eb(0x0), v05eb(0x0), v05ea
    0x5f00x0: v05f0(0x0) = CONST 
    0x5f30x0: v05f3 = EQ v05e9, v05f0(0x0)
    0x5f40x0: v05f4(0x5fc) = CONST 
    0x5f70x0: JUMPI v05f4(0x5fc), v05f3

    Begin block 0x5f80x0
    prev=[0x5db0x0], succ=[]
    =================================
    0x5f80x0: v05f8 = RETURNDATASIZE 
    0x5f90x0: v05f9(0x0) = CONST 
    0x5fb0x0: RETURN v05f9(0x0), v05f8

    Begin block 0x5fc0x0
    prev=[0x5db0x0], succ=[]
    =================================
    0x5fd0x0: v05fd = RETURNDATASIZE 
    0x5fe0x0: v05fe(0x0) = CONST 
    0x6000x0: REVERT v05fe(0x0), v05fd

    Begin block 0x83d
    prev=[0x3f], succ=[]
    =================================
    0x83e: v83e(0x1d5) = CONST 
    0x83f: CALLPRIVATE v83e(0x1d5)

    Begin block 0x83a
    prev=[0x34], succ=[]
    =================================
    0x83b: v83b(0x184) = CONST 
    0x83c: CALLPRIVATE v83b(0x184)

    Begin block 0x82e
    prev=[0x0], succ=[]
    =================================
    0x82f: v82f(0x4e) = CONST 
    0x830: CALLPRIVATE v82f(0x4e)

}

function implementation()() public {
    Begin block 0x143
    prev=[], succ=[0x14b, 0x14f]
    =================================
    0x144: v144 = CALLVALUE 
    0x146: v146 = ISZERO v144
    0x147: v147(0x14f) = CONST 
    0x14a: JUMPI v147(0x14f), v146

    Begin block 0x14b
    prev=[0x143], succ=[]
    =================================
    0x14b: v14b(0x0) = CONST 
    0x14e: REVERT v14b(0x0), v14b(0x0)

    Begin block 0x14f
    prev=[0x143], succ=[0x35eB0x14f]
    =================================
    0x151: v151(0x158) = CONST 
    0x154: v154(0x35e) = CONST 
    0x157: JUMP v154(0x35e)

    Begin block 0x35eB0x14f
    prev=[0x14f], succ=[0x5aaB0x35eB0x14f]
    =================================
    0x35fS0x14f: v35fV14f(0x0) = CONST 
    0x361S0x14f: v361V14f(0x368) = CONST 
    0x364S0x14f: v364V14f(0x5aa) = CONST 
    0x367S0x14f: JUMP v364V14f(0x5aa)

    Begin block 0x5aaB0x35eB0x14f
    prev=[0x35eB0x14f], succ=[0x368B0x14f]
    =================================
    0x5abS0x35eS0x14f: v5abV35eV14f(0x0) = CONST 
    0x5aeS0x35eS0x14f: v5aeV35eV14f(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x35eS0x14f: v5cfV35eV14f(0x0) = CONST 
    0x5d1S0x35eS0x14f: v5d1V35eV14f(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV35eV14f(0x0), v5aeV35eV14f(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x35eS0x14f: v5d5V35eV14f = SLOAD v5d1V35eV14f(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x35eS0x14f: JUMP v361V14f(0x368)

    Begin block 0x368B0x14f
    prev=[0x5aaB0x35eB0x14f], succ=[0x158]
    =================================
    0x36cS0x14f: JUMP v151(0x158)

    Begin block 0x158
    prev=[0x368B0x14f], succ=[]
    =================================
    0x159: v159(0x40) = CONST 
    0x15b: v15b = MLOAD v159(0x40)
    0x15e: v15e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x173: v173 = AND v15e(0xffffffffffffffffffffffffffffffffffffffff), v5d5V35eV14f
    0x175: MSTORE v15b, v173
    0x176: v176(0x20) = CONST 
    0x178: v178 = ADD v176(0x20), v15b
    0x17c: v17c(0x40) = CONST 
    0x17e: v17e = MLOAD v17c(0x40)
    0x181: v181(0x20) = SUB v178, v17e
    0x183: RETURN v17e, v181(0x20)

}

function changeAdmin(address)() public {
    Begin block 0x184
    prev=[], succ=[0x18c, 0x190]
    =================================
    0x185: v185 = CALLVALUE 
    0x187: v187 = ISZERO v185
    0x188: v188(0x190) = CONST 
    0x18b: JUMPI v188(0x190), v187

    Begin block 0x18c
    prev=[0x184], succ=[]
    =================================
    0x18c: v18c(0x0) = CONST 
    0x18f: REVERT v18c(0x0), v18c(0x0)

    Begin block 0x190
    prev=[0x184], succ=[0x1a3, 0x1a7]
    =================================
    0x192: v192(0x1d3) = CONST 
    0x195: v195(0x4) = CONST 
    0x198: v198 = CALLDATASIZE 
    0x199: v199 = SUB v198, v195(0x4)
    0x19a: v19a(0x20) = CONST 
    0x19d: v19d = LT v199, v19a(0x20)
    0x19e: v19e = ISZERO v19d
    0x19f: v19f(0x1a7) = CONST 
    0x1a2: JUMPI v19f(0x1a7), v19e

    Begin block 0x1a3
    prev=[0x190], succ=[]
    =================================
    0x1a3: v1a3(0x0) = CONST 
    0x1a6: REVERT v1a3(0x0), v1a3(0x0)

    Begin block 0x1a7
    prev=[0x190], succ=[0x36d]
    =================================
    0x1a9: v1a9 = ADD v195(0x4), v199
    0x1ad: v1ad = CALLDATALOAD v195(0x4)
    0x1ae: v1ae(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x1c3: v1c3 = AND v1ae(0xffffffffffffffffffffffffffffffffffffffff), v1ad
    0x1c5: v1c5(0x20) = CONST 
    0x1c7: v1c7(0x24) = ADD v1c5(0x20), v195(0x4)
    0x1cf: v1cf(0x36d) = CONST 
    0x1d2: JUMP v1cf(0x36d)

    Begin block 0x36d
    prev=[0x1a7], succ=[0x601B0x36d]
    =================================
    0x36e: v36e(0x375) = CONST 
    0x371: v371(0x601) = CONST 
    0x374: JUMP v371(0x601)

    Begin block 0x601B0x36d
    prev=[0x36d], succ=[0x375]
    =================================
    0x602S0x36d: v602V36d(0x0) = CONST 
    0x605S0x36d: v605V36d(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x36d: v626V36d(0x0) = CONST 
    0x628S0x36d: v628V36d(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V36d(0x0), v605V36d(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x36d: v62cV36d = SLOAD v628V36d(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x36d: JUMP v36e(0x375)

    Begin block 0x375
    prev=[0x601B0x36d], succ=[0x3a9, 0x4ae]
    =================================
    0x376: v376(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x38b: v38b = AND v376(0xffffffffffffffffffffffffffffffffffffffff), v62cV36d
    0x38c: v38c = CALLER 
    0x38d: v38d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3a2: v3a2 = AND v38d(0xffffffffffffffffffffffffffffffffffffffff), v38c
    0x3a3: v3a3 = EQ v3a2, v38b
    0x3a4: v3a4 = ISZERO v3a3
    0x3a5: v3a5(0x4ae) = CONST 
    0x3a8: JUMPI v3a5(0x4ae), v3a4

    Begin block 0x3a9
    prev=[0x375], succ=[0x3de, 0x42e]
    =================================
    0x3a9: v3a9(0x0) = CONST 
    0x3ab: v3ab(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3c0: v3c0(0x0) = AND v3ab(0xffffffffffffffffffffffffffffffffffffffff), v3a9(0x0)
    0x3c2: v3c2(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x3d7: v3d7 = AND v3c2(0xffffffffffffffffffffffffffffffffffffffff), v1c3
    0x3d8: v3d8 = EQ v3d7, v3c0(0x0)
    0x3d9: v3d9 = ISZERO v3d8
    0x3da: v3da(0x42e) = CONST 
    0x3dd: JUMPI v3da(0x42e), v3d9

    Begin block 0x3de
    prev=[0x3a9], succ=[]
    =================================
    0x3de: v3de(0x40) = CONST 
    0x3e0: v3e0 = MLOAD v3de(0x40)
    0x3e1: v3e1(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x403: MSTORE v3e0, v3e1(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x404: v404(0x4) = CONST 
    0x406: v406 = ADD v404(0x4), v3e0
    0x409: v409(0x20) = CONST 
    0x40b: v40b = ADD v409(0x20), v406
    0x40e: v40e(0x20) = SUB v40b, v406
    0x410: MSTORE v406, v40e(0x20)
    0x411: v411(0x36) = CONST 
    0x414: MSTORE v40b, v411(0x36)
    0x415: v415(0x20) = CONST 
    0x417: v417 = ADD v415(0x20), v40b
    0x419: v419(0x77c) = CONST 
    0x41c: v41c(0x36) = CONST 
    0x41f: CODECOPY v417, v419(0x77c), v41c(0x36)
    0x420: v420(0x40) = CONST 
    0x422: v422 = ADD v420(0x40), v417
    0x426: v426(0x40) = CONST 
    0x428: v428 = MLOAD v426(0x40)
    0x42b: v42b(0x84) = SUB v422, v428
    0x42d: REVERT v428, v42b(0x84)

    Begin block 0x42e
    prev=[0x3a9], succ=[0x601B0x42e]
    =================================
    0x42f: v42f(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f) = CONST 
    0x450: v450(0x457) = CONST 
    0x453: v453(0x601) = CONST 
    0x456: JUMP v453(0x601)

    Begin block 0x601B0x42e
    prev=[0x42e], succ=[0x457]
    =================================
    0x602S0x42e: v602V42e(0x0) = CONST 
    0x605S0x42e: v605V42e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x42e: v626V42e(0x0) = CONST 
    0x628S0x42e: v628V42e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V42e(0x0), v605V42e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x42e: v62cV42e = SLOAD v628V42e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x42e: JUMP v450(0x457)

    Begin block 0x457
    prev=[0x601B0x42e], succ=[0x68b]
    =================================
    0x459: v459(0x40) = CONST 
    0x45b: v45b = MLOAD v459(0x40)
    0x45e: v45e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x473: v473 = AND v45e(0xffffffffffffffffffffffffffffffffffffffff), v62cV42e
    0x475: MSTORE v45b, v473
    0x476: v476(0x20) = CONST 
    0x478: v478 = ADD v476(0x20), v45b
    0x47a: v47a(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x48f: v48f = AND v47a(0xffffffffffffffffffffffffffffffffffffffff), v1c3
    0x491: MSTORE v478, v48f
    0x492: v492(0x20) = CONST 
    0x494: v494 = ADD v492(0x20), v478
    0x499: v499(0x40) = CONST 
    0x49b: v49b = MLOAD v499(0x40)
    0x49e: v49e(0x40) = SUB v494, v49b
    0x4a0: LOG1 v49b, v49e(0x40), v42f(0x7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f)
    0x4a1: v4a1(0x4a9) = CONST 
    0x4a5: v4a5(0x68b) = CONST 
    0x4a8: JUMP v4a5(0x68b)

    Begin block 0x68b
    prev=[0x457], succ=[0x4a9]
    =================================
    0x68c: v68c(0x0) = CONST 
    0x68e: v68e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x6af: v6af(0x0) = CONST 
    0x6b1: v6b1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v6af(0x0), v68e(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x6b6: SSTORE v6b1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b), v1c3
    0x6b9: JUMP v4a1(0x4a9)

    Begin block 0x4a9
    prev=[0x68b], succ=[0x4b7]
    =================================
    0x4aa: v4aa(0x4b7) = CONST 
    0x4ad: JUMP v4aa(0x4b7)

    Begin block 0x4b7
    prev=[0x4a9], succ=[0x1d3]
    =================================
    0x4b9: JUMP v192(0x1d3)

    Begin block 0x1d3
    prev=[0x4b7], succ=[]
    =================================
    0x1d4: STOP 

    Begin block 0x4ae
    prev=[0x375], succ=[0x2160x184]
    =================================
    0x4af: v4af(0x4b6) = CONST 
    0x4b2: v4b2(0x216) = CONST 
    0x4b5: JUMP v4b2(0x216)

    Begin block 0x2160x184
    prev=[0x4ae], succ=[0x21e0x184]
    =================================
    0x2170x184: v184217(0x21e) = CONST 
    0x21a0x184: v18421a(0x514) = CONST 
    0x21d0x184: CALLPRIVATE v18421a(0x514), v184217(0x21e)

    Begin block 0x21e0x184
    prev=[0x2160x184], succ=[0x5aaB0x21e0x184]
    =================================
    0x21f0x184: v18421f(0x22e) = CONST 
    0x2220x184: v184222(0x229) = CONST 
    0x2250x184: v184225(0x5aa) = CONST 
    0x2280x184: JUMP v184225(0x5aa)

    Begin block 0x5aaB0x21e0x184
    prev=[0x21e0x184], succ=[0x2290x184]
    =================================
    0x5abS0x21e0x184: v5abV21e184(0x0) = CONST 
    0x5aeS0x21e0x184: v5aeV21e184(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x21e0x184: v5cfV21e184(0x0) = CONST 
    0x5d1S0x21e0x184: v5d1V21e184(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV21e184(0x0), v5aeV21e184(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x21e0x184: v5d5V21e184 = SLOAD v5d1V21e184(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x21e0x184: JUMP v184222(0x229)

    Begin block 0x2290x184
    prev=[0x5aaB0x21e0x184], succ=[0x5db0x184]
    =================================
    0x22a0x184: v18422a(0x5db) = CONST 
    0x22d0x184: JUMP v18422a(0x5db)

    Begin block 0x5db0x184
    prev=[0x2290x184], succ=[0x5f80x184, 0x5fc0x184]
    =================================
    0x5dc0x184: v1845dc = CALLDATASIZE 
    0x5dd0x184: v1845dd(0x0) = CONST 
    0x5e00x184: CALLDATACOPY v1845dd(0x0), v1845dd(0x0), v1845dc
    0x5e10x184: v1845e1(0x0) = CONST 
    0x5e40x184: v1845e4 = CALLDATASIZE 
    0x5e50x184: v1845e5(0x0) = CONST 
    0x5e80x184: v1845e8 = GAS 
    0x5e90x184: v1845e9 = DELEGATECALL v1845e8, v5d5V21e184, v1845e5(0x0), v1845e4, v1845e1(0x0), v1845e1(0x0)
    0x5ea0x184: v1845ea = RETURNDATASIZE 
    0x5eb0x184: v1845eb(0x0) = CONST 
    0x5ee0x184: RETURNDATACOPY v1845eb(0x0), v1845eb(0x0), v1845ea
    0x5f00x184: v1845f0(0x0) = CONST 
    0x5f30x184: v1845f3 = EQ v1845e9, v1845f0(0x0)
    0x5f40x184: v1845f4(0x5fc) = CONST 
    0x5f70x184: JUMPI v1845f4(0x5fc), v1845f3

    Begin block 0x5f80x184
    prev=[0x5db0x184], succ=[]
    =================================
    0x5f80x184: v1845f8 = RETURNDATASIZE 
    0x5f90x184: v1845f9(0x0) = CONST 
    0x5fb0x184: RETURN v1845f9(0x0), v1845f8

    Begin block 0x5fc0x184
    prev=[0x5db0x184], succ=[]
    =================================
    0x5fd0x184: v1845fd = RETURNDATASIZE 
    0x5fe0x184: v1845fe(0x0) = CONST 
    0x6000x184: REVERT v1845fe(0x0), v1845fd

}

function admin()() public {
    Begin block 0x1d5
    prev=[], succ=[0x1dd, 0x1e1]
    =================================
    0x1d6: v1d6 = CALLVALUE 
    0x1d8: v1d8 = ISZERO v1d6
    0x1d9: v1d9(0x1e1) = CONST 
    0x1dc: JUMPI v1d9(0x1e1), v1d8

    Begin block 0x1dd
    prev=[0x1d5], succ=[]
    =================================
    0x1dd: v1dd(0x0) = CONST 
    0x1e0: REVERT v1dd(0x0), v1dd(0x0)

    Begin block 0x1e1
    prev=[0x1d5], succ=[0x4baB0x1e1]
    =================================
    0x1e3: v1e3(0x1ea) = CONST 
    0x1e6: v1e6(0x4ba) = CONST 
    0x1e9: JUMP v1e6(0x4ba)

    Begin block 0x4baB0x1e1
    prev=[0x1e1], succ=[0x601B0x4baB0x1e1]
    =================================
    0x4bbS0x1e1: v4bbV1e1(0x0) = CONST 
    0x4bdS0x1e1: v4bdV1e1(0x4c4) = CONST 
    0x4c0S0x1e1: v4c0V1e1(0x601) = CONST 
    0x4c3S0x1e1: JUMP v4c0V1e1(0x601)

    Begin block 0x601B0x4baB0x1e1
    prev=[0x4baB0x1e1], succ=[0x4c4B0x1e1]
    =================================
    0x602S0x4baS0x1e1: v602V4baV1e1(0x0) = CONST 
    0x605S0x4baS0x1e1: v605V4baV1e1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x4baS0x1e1: v626V4baV1e1(0x0) = CONST 
    0x628S0x4baS0x1e1: v628V4baV1e1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V4baV1e1(0x0), v605V4baV1e1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x4baS0x1e1: v62cV4baV1e1 = SLOAD v628V4baV1e1(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x4baS0x1e1: JUMP v4bdV1e1(0x4c4)

    Begin block 0x4c4B0x1e1
    prev=[0x601B0x4baB0x1e1], succ=[0x1ea]
    =================================
    0x4c8S0x1e1: JUMP v1e3(0x1ea)

    Begin block 0x1ea
    prev=[0x4c4B0x1e1], succ=[]
    =================================
    0x1eb: v1eb(0x40) = CONST 
    0x1ed: v1ed = MLOAD v1eb(0x40)
    0x1f0: v1f0(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x205: v205 = AND v1f0(0xffffffffffffffffffffffffffffffffffffffff), v62cV4baV1e1
    0x207: MSTORE v1ed, v205
    0x208: v208(0x20) = CONST 
    0x20a: v20a = ADD v208(0x20), v1ed
    0x20e: v20e(0x40) = CONST 
    0x210: v210 = MLOAD v20e(0x40)
    0x213: v213(0x20) = SUB v20a, v210
    0x215: RETURN v210, v213(0x20)

}

function fallback()() public {
    Begin block 0x4e
    prev=[], succ=[0x4f0x4e]
    =================================

    Begin block 0x4f0x4e
    prev=[0x4e], succ=[0x2160x4e]
    =================================
    0x500x4e: v4e50(0x57) = CONST 
    0x530x4e: v4e53(0x216) = CONST 
    0x560x4e: JUMP v4e53(0x216)

    Begin block 0x2160x4e
    prev=[0x4f0x4e], succ=[0x21e0x4e]
    =================================
    0x2170x4e: v4e217(0x21e) = CONST 
    0x21a0x4e: v4e21a(0x514) = CONST 
    0x21d0x4e: CALLPRIVATE v4e21a(0x514), v4e217(0x21e)

    Begin block 0x21e0x4e
    prev=[0x2160x4e], succ=[0x5aaB0x21e0x4e]
    =================================
    0x21f0x4e: v4e21f(0x22e) = CONST 
    0x2220x4e: v4e222(0x229) = CONST 
    0x2250x4e: v4e225(0x5aa) = CONST 
    0x2280x4e: JUMP v4e225(0x5aa)

    Begin block 0x5aaB0x21e0x4e
    prev=[0x21e0x4e], succ=[0x2290x4e]
    =================================
    0x5abS0x21e0x4e: v5abV21e4e(0x0) = CONST 
    0x5aeS0x21e0x4e: v5aeV21e4e(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x21e0x4e: v5cfV21e4e(0x0) = CONST 
    0x5d1S0x21e0x4e: v5d1V21e4e(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV21e4e(0x0), v5aeV21e4e(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x21e0x4e: v5d5V21e4e = SLOAD v5d1V21e4e(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x21e0x4e: JUMP v4e222(0x229)

    Begin block 0x2290x4e
    prev=[0x5aaB0x21e0x4e], succ=[0x5db0x4e]
    =================================
    0x22a0x4e: v4e22a(0x5db) = CONST 
    0x22d0x4e: JUMP v4e22a(0x5db)

    Begin block 0x5db0x4e
    prev=[0x2290x4e], succ=[0x5f80x4e, 0x5fc0x4e]
    =================================
    0x5dc0x4e: v4e5dc = CALLDATASIZE 
    0x5dd0x4e: v4e5dd(0x0) = CONST 
    0x5e00x4e: CALLDATACOPY v4e5dd(0x0), v4e5dd(0x0), v4e5dc
    0x5e10x4e: v4e5e1(0x0) = CONST 
    0x5e40x4e: v4e5e4 = CALLDATASIZE 
    0x5e50x4e: v4e5e5(0x0) = CONST 
    0x5e80x4e: v4e5e8 = GAS 
    0x5e90x4e: v4e5e9 = DELEGATECALL v4e5e8, v5d5V21e4e, v4e5e5(0x0), v4e5e4, v4e5e1(0x0), v4e5e1(0x0)
    0x5ea0x4e: v4e5ea = RETURNDATASIZE 
    0x5eb0x4e: v4e5eb(0x0) = CONST 
    0x5ee0x4e: RETURNDATACOPY v4e5eb(0x0), v4e5eb(0x0), v4e5ea
    0x5f00x4e: v4e5f0(0x0) = CONST 
    0x5f30x4e: v4e5f3 = EQ v4e5e9, v4e5f0(0x0)
    0x5f40x4e: v4e5f4(0x5fc) = CONST 
    0x5f70x4e: JUMPI v4e5f4(0x5fc), v4e5f3

    Begin block 0x5f80x4e
    prev=[0x5db0x4e], succ=[]
    =================================
    0x5f80x4e: v4e5f8 = RETURNDATASIZE 
    0x5f90x4e: v4e5f9(0x0) = CONST 
    0x5fb0x4e: RETURN v4e5f9(0x0), v4e5f8

    Begin block 0x5fc0x4e
    prev=[0x5db0x4e], succ=[]
    =================================
    0x5fd0x4e: v4e5fd = RETURNDATASIZE 
    0x5fe0x4e: v4e5fe(0x0) = CONST 
    0x6000x4e: REVERT v4e5fe(0x0), v4e5fd

}

function 0x514(0x514arg0x0) private {
    Begin block 0x514
    prev=[], succ=[0x601B0x514]
    =================================
    0x515: v515(0x51c) = CONST 
    0x518: v518(0x601) = CONST 
    0x51b: JUMP v518(0x601)

    Begin block 0x601B0x514
    prev=[0x514], succ=[0x51c]
    =================================
    0x602S0x514: v602V514(0x0) = CONST 
    0x605S0x514: v605V514(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x514: v626V514(0x0) = CONST 
    0x628S0x514: v628V514(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V514(0x0), v605V514(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x514: v62cV514 = SLOAD v628V514(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x514: JUMP v515(0x51c)

    Begin block 0x51c
    prev=[0x601B0x514], succ=[0x550, 0x5a0]
    =================================
    0x51d: v51d(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x532: v532 = AND v51d(0xffffffffffffffffffffffffffffffffffffffff), v62cV514
    0x533: v533 = CALLER 
    0x534: v534(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x549: v549 = AND v534(0xffffffffffffffffffffffffffffffffffffffff), v533
    0x54a: v54a = EQ v549, v532
    0x54b: v54b = ISZERO v54a
    0x54c: v54c(0x5a0) = CONST 
    0x54f: JUMPI v54c(0x5a0), v54b

    Begin block 0x550
    prev=[0x51c], succ=[]
    =================================
    0x550: v550(0x40) = CONST 
    0x552: v552 = MLOAD v550(0x40)
    0x553: v553(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x575: MSTORE v552, v553(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x576: v576(0x4) = CONST 
    0x578: v578 = ADD v576(0x4), v552
    0x57b: v57b(0x20) = CONST 
    0x57d: v57d = ADD v57b(0x20), v578
    0x580: v580(0x20) = SUB v57d, v578
    0x582: MSTORE v578, v580(0x20)
    0x583: v583(0x32) = CONST 
    0x586: MSTORE v57d, v583(0x32)
    0x587: v587(0x20) = CONST 
    0x589: v589 = ADD v587(0x20), v57d
    0x58b: v58b(0x74a) = CONST 
    0x58e: v58e(0x32) = CONST 
    0x591: CODECOPY v589, v58b(0x74a), v58e(0x32)
    0x592: v592(0x40) = CONST 
    0x594: v594 = ADD v592(0x40), v589
    0x598: v598(0x40) = CONST 
    0x59a: v59a = MLOAD v598(0x40)
    0x59d: v59d(0x84) = SUB v594, v59a
    0x59f: REVERT v59a, v59d(0x84)

    Begin block 0x5a0
    prev=[0x51c], succ=[0x6baB0x5a0]
    =================================
    0x5a1: v5a1(0x5a8) = CONST 
    0x5a4: v5a4(0x6ba) = CONST 
    0x5a7: JUMP v5a4(0x6ba), v5a1(0x5a8)

    Begin block 0x6baB0x5a0
    prev=[0x5a0], succ=[0x5a8]
    =================================
    0x6bbS0x5a0: JUMP v5a1(0x5a8)

    Begin block 0x5a8
    prev=[0x6baB0x5a0], succ=[]
    =================================
    0x5a9: RETURNPRIVATE v514arg0

}

function upgradeTo(address)() public {
    Begin block 0x59
    prev=[], succ=[0x61, 0x65]
    =================================
    0x5a: v5a = CALLVALUE 
    0x5c: v5c = ISZERO v5a
    0x5d: v5d(0x65) = CONST 
    0x60: JUMPI v5d(0x65), v5c

    Begin block 0x61
    prev=[0x59], succ=[]
    =================================
    0x61: v61(0x0) = CONST 
    0x64: REVERT v61(0x0), v61(0x0)

    Begin block 0x65
    prev=[0x59], succ=[0x78, 0x7c]
    =================================
    0x67: v67(0xa8) = CONST 
    0x6a: v6a(0x4) = CONST 
    0x6d: v6d = CALLDATASIZE 
    0x6e: v6e = SUB v6d, v6a(0x4)
    0x6f: v6f(0x20) = CONST 
    0x72: v72 = LT v6e, v6f(0x20)
    0x73: v73 = ISZERO v72
    0x74: v74(0x7c) = CONST 
    0x77: JUMPI v74(0x7c), v73

    Begin block 0x78
    prev=[0x65], succ=[]
    =================================
    0x78: v78(0x0) = CONST 
    0x7b: REVERT v78(0x0), v78(0x0)

    Begin block 0x7c
    prev=[0x65], succ=[0x230]
    =================================
    0x7e: v7e = ADD v6a(0x4), v6e
    0x82: v82 = CALLDATALOAD v6a(0x4)
    0x83: v83(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x98: v98 = AND v83(0xffffffffffffffffffffffffffffffffffffffff), v82
    0x9a: v9a(0x20) = CONST 
    0x9c: v9c(0x24) = ADD v9a(0x20), v6a(0x4)
    0xa4: va4(0x230) = CONST 
    0xa7: JUMP va4(0x230)

    Begin block 0x230
    prev=[0x7c], succ=[0x601B0x230]
    =================================
    0x231: v231(0x238) = CONST 
    0x234: v234(0x601) = CONST 
    0x237: JUMP v234(0x601)

    Begin block 0x601B0x230
    prev=[0x230], succ=[0x238]
    =================================
    0x602S0x230: v602V230(0x0) = CONST 
    0x605S0x230: v605V230(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x230: v626V230(0x0) = CONST 
    0x628S0x230: v628V230(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V230(0x0), v605V230(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x230: v62cV230 = SLOAD v628V230(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x230: JUMP v231(0x238)

    Begin block 0x238
    prev=[0x601B0x230], succ=[0x26c, 0x279]
    =================================
    0x239: v239(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x24e: v24e = AND v239(0xffffffffffffffffffffffffffffffffffffffff), v62cV230
    0x24f: v24f = CALLER 
    0x250: v250(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x265: v265 = AND v250(0xffffffffffffffffffffffffffffffffffffffff), v24f
    0x266: v266 = EQ v265, v24e
    0x267: v267 = ISZERO v266
    0x268: v268(0x279) = CONST 
    0x26b: JUMPI v268(0x279), v267

    Begin block 0x26c
    prev=[0x238], succ=[0x274]
    =================================
    0x26c: v26c(0x274) = CONST 
    0x270: v270(0x632) = CONST 
    0x273: CALLPRIVATE v270(0x632), v98, v26c(0x274)

    Begin block 0x274
    prev=[0x26c], succ=[0x282]
    =================================
    0x275: v275(0x282) = CONST 
    0x278: JUMP v275(0x282)

    Begin block 0x282
    prev=[0x274], succ=[0xa8]
    =================================
    0x284: JUMP v67(0xa8)

    Begin block 0xa8
    prev=[0x282], succ=[]
    =================================
    0xa9: STOP 

    Begin block 0x279
    prev=[0x238], succ=[0x2160x59]
    =================================
    0x27a: v27a(0x281) = CONST 
    0x27d: v27d(0x216) = CONST 
    0x280: JUMP v27d(0x216)

    Begin block 0x2160x59
    prev=[0x279], succ=[0x21e0x59]
    =================================
    0x2170x59: v59217(0x21e) = CONST 
    0x21a0x59: v5921a(0x514) = CONST 
    0x21d0x59: CALLPRIVATE v5921a(0x514), v59217(0x21e)

    Begin block 0x21e0x59
    prev=[0x2160x59], succ=[0x5aaB0x21e0x59]
    =================================
    0x21f0x59: v5921f(0x22e) = CONST 
    0x2220x59: v59222(0x229) = CONST 
    0x2250x59: v59225(0x5aa) = CONST 
    0x2280x59: JUMP v59225(0x5aa)

    Begin block 0x5aaB0x21e0x59
    prev=[0x21e0x59], succ=[0x2290x59]
    =================================
    0x5abS0x21e0x59: v5abV21e59(0x0) = CONST 
    0x5aeS0x21e0x59: v5aeV21e59(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x21e0x59: v5cfV21e59(0x0) = CONST 
    0x5d1S0x21e0x59: v5d1V21e59(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV21e59(0x0), v5aeV21e59(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x21e0x59: v5d5V21e59 = SLOAD v5d1V21e59(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x21e0x59: JUMP v59222(0x229)

    Begin block 0x2290x59
    prev=[0x5aaB0x21e0x59], succ=[0x5db0x59]
    =================================
    0x22a0x59: v5922a(0x5db) = CONST 
    0x22d0x59: JUMP v5922a(0x5db)

    Begin block 0x5db0x59
    prev=[0x2290x59], succ=[0x5f80x59, 0x5fc0x59]
    =================================
    0x5dc0x59: v595dc = CALLDATASIZE 
    0x5dd0x59: v595dd(0x0) = CONST 
    0x5e00x59: CALLDATACOPY v595dd(0x0), v595dd(0x0), v595dc
    0x5e10x59: v595e1(0x0) = CONST 
    0x5e40x59: v595e4 = CALLDATASIZE 
    0x5e50x59: v595e5(0x0) = CONST 
    0x5e80x59: v595e8 = GAS 
    0x5e90x59: v595e9 = DELEGATECALL v595e8, v5d5V21e59, v595e5(0x0), v595e4, v595e1(0x0), v595e1(0x0)
    0x5ea0x59: v595ea = RETURNDATASIZE 
    0x5eb0x59: v595eb(0x0) = CONST 
    0x5ee0x59: RETURNDATACOPY v595eb(0x0), v595eb(0x0), v595ea
    0x5f00x59: v595f0(0x0) = CONST 
    0x5f30x59: v595f3 = EQ v595e9, v595f0(0x0)
    0x5f40x59: v595f4(0x5fc) = CONST 
    0x5f70x59: JUMPI v595f4(0x5fc), v595f3

    Begin block 0x5f80x59
    prev=[0x5db0x59], succ=[]
    =================================
    0x5f80x59: v595f8 = RETURNDATASIZE 
    0x5f90x59: v595f9(0x0) = CONST 
    0x5fb0x59: RETURN v595f9(0x0), v595f8

    Begin block 0x5fc0x59
    prev=[0x5db0x59], succ=[]
    =================================
    0x5fd0x59: v595fd = RETURNDATASIZE 
    0x5fe0x59: v595fe(0x0) = CONST 
    0x6000x59: REVERT v595fe(0x0), v595fd

}

function 0x632(0x632arg0x0, 0x632arg0x1) private {
    Begin block 0x632
    prev=[], succ=[0x6bc]
    =================================
    0x633: v633(0x63b) = CONST 
    0x637: v637(0x6bc) = CONST 
    0x63a: JUMP v637(0x6bc)

    Begin block 0x6bc
    prev=[0x632], succ=[0x4c9B0x6bc]
    =================================
    0x6bd: v6bd(0x6c5) = CONST 
    0x6c1: v6c1(0x4c9) = CONST 
    0x6c4: JUMP v6c1(0x4c9)

    Begin block 0x4c9B0x6bc
    prev=[0x6bc], succ=[0x50bB0x6bc, 0x503B0x6bc]
    =================================
    0x4caS0x6bc: v4caV6bc(0x0) = CONST 
    0x4cdS0x6bc: v4cdV6bc(0x0) = CONST 
    0x4cfS0x6bc: v4cfV6bc(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = CONST 
    0x4f0S0x6bc: v4f0V6bc(0x0) = CONST 
    0x4f2S0x6bc: v4f2V6bc(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470) = SHL v4f0V6bc(0x0), v4cfV6bc(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470)
    0x4f6S0x6bc: v4f6V6bc = EXTCODEHASH v632arg0
    0x4fbS0x6bc: v4fbV6bc = EQ v4f6V6bc, v4f2V6bc(0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470)
    0x4fcS0x6bc: v4fcV6bc = ISZERO v4fbV6bc
    0x4feS0x6bc: v4feV6bc = ISZERO v4fcV6bc
    0x4ffS0x6bc: v4ffV6bc(0x50b) = CONST 
    0x502S0x6bc: JUMPI v4ffV6bc(0x50b), v4feV6bc

    Begin block 0x50bB0x6bc
    prev=[0x4c9B0x6bc, 0x503B0x6bc], succ=[0x6c5]
    =================================
    0x50b_0x0S0x6bc: v50b_0V6bc = PHI v4fcV6bc, v50aV6bc
    0x513S0x6bc: JUMP v6bd(0x6c5)

    Begin block 0x6c5
    prev=[0x50bB0x6bc], succ=[0x6ca, 0x71a]
    =================================
    0x6c6: v6c6(0x71a) = CONST 
    0x6c9: JUMPI v6c6(0x71a), v50b_0V6bc

    Begin block 0x6ca
    prev=[0x6c5], succ=[]
    =================================
    0x6ca: v6ca(0x40) = CONST 
    0x6cc: v6cc = MLOAD v6ca(0x40)
    0x6cd: v6cd(0x8c379a000000000000000000000000000000000000000000000000000000000) = CONST 
    0x6ef: MSTORE v6cc, v6cd(0x8c379a000000000000000000000000000000000000000000000000000000000)
    0x6f0: v6f0(0x4) = CONST 
    0x6f2: v6f2 = ADD v6f0(0x4), v6cc
    0x6f5: v6f5(0x20) = CONST 
    0x6f7: v6f7 = ADD v6f5(0x20), v6f2
    0x6fa: v6fa(0x20) = SUB v6f7, v6f2
    0x6fc: MSTORE v6f2, v6fa(0x20)
    0x6fd: v6fd(0x3b) = CONST 
    0x700: MSTORE v6f7, v6fd(0x3b)
    0x701: v701(0x20) = CONST 
    0x703: v703 = ADD v701(0x20), v6f7
    0x705: v705(0x7b2) = CONST 
    0x708: v708(0x3b) = CONST 
    0x70b: CODECOPY v703, v705(0x7b2), v708(0x3b)
    0x70c: v70c(0x40) = CONST 
    0x70e: v70e = ADD v70c(0x40), v703
    0x712: v712(0x40) = CONST 
    0x714: v714 = MLOAD v712(0x40)
    0x717: v717(0x84) = SUB v70e, v714
    0x719: REVERT v714, v717(0x84)

    Begin block 0x71a
    prev=[0x6c5], succ=[0x63b]
    =================================
    0x71b: v71b(0x0) = CONST 
    0x71d: v71d(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x73e: v73e(0x0) = CONST 
    0x740: v740(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v73e(0x0), v71d(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x745: SSTORE v740(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3), v632arg0
    0x748: JUMP v633(0x63b)

    Begin block 0x63b
    prev=[0x71a], succ=[]
    =================================
    0x63c: v63c(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b) = CONST 
    0x65e: v65e(0x40) = CONST 
    0x660: v660 = MLOAD v65e(0x40)
    0x663: v663(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x678: v678 = AND v663(0xffffffffffffffffffffffffffffffffffffffff), v632arg0
    0x67a: MSTORE v660, v678
    0x67b: v67b(0x20) = CONST 
    0x67d: v67d = ADD v67b(0x20), v660
    0x681: v681(0x40) = CONST 
    0x683: v683 = MLOAD v681(0x40)
    0x686: v686(0x20) = SUB v67d, v683
    0x688: LOG1 v683, v686(0x20), v63c(0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b)
    0x68a: RETURNPRIVATE v632arg1

    Begin block 0x503B0x6bc
    prev=[0x4c9B0x6bc], succ=[0x50bB0x6bc]
    =================================
    0x504S0x6bc: v504V6bc(0x0) = CONST 
    0x507S0x6bc: v507V6bc(0x0) = SHL v504V6bc(0x0), v504V6bc(0x0)
    0x509S0x6bc: v509V6bc = EQ v4f6V6bc, v507V6bc(0x0)
    0x50aS0x6bc: v50aV6bc = ISZERO v509V6bc

}

function upgradeToAndCall(address,bytes)() public {
    Begin block 0xaa
    prev=[], succ=[0xbc, 0xc0]
    =================================
    0xab: vab(0x141) = CONST 
    0xae: vae(0x4) = CONST 
    0xb1: vb1 = CALLDATASIZE 
    0xb2: vb2 = SUB vb1, vae(0x4)
    0xb3: vb3(0x40) = CONST 
    0xb6: vb6 = LT vb2, vb3(0x40)
    0xb7: vb7 = ISZERO vb6
    0xb8: vb8(0xc0) = CONST 
    0xbb: JUMPI vb8(0xc0), vb7

    Begin block 0xbc
    prev=[0xaa], succ=[]
    =================================
    0xbc: vbc(0x0) = CONST 
    0xbf: REVERT vbc(0x0), vbc(0x0)

    Begin block 0xc0
    prev=[0xaa], succ=[0xf9, 0xfd]
    =================================
    0xc2: vc2 = ADD vae(0x4), vb2
    0xc6: vc6 = CALLDATALOAD vae(0x4)
    0xc7: vc7(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0xdc: vdc = AND vc7(0xffffffffffffffffffffffffffffffffffffffff), vc6
    0xde: vde(0x20) = CONST 
    0xe0: ve0(0x24) = ADD vde(0x20), vae(0x4)
    0xe6: ve6 = CALLDATALOAD ve0(0x24)
    0xe8: ve8(0x20) = CONST 
    0xea: vea(0x44) = ADD ve8(0x20), ve0(0x24)
    0xec: vec(0x100000000) = CONST 
    0xf3: vf3 = GT ve6, vec(0x100000000)
    0xf4: vf4 = ISZERO vf3
    0xf5: vf5(0xfd) = CONST 
    0xf8: JUMPI vf5(0xfd), vf4

    Begin block 0xf9
    prev=[0xc0], succ=[]
    =================================
    0xf9: vf9(0x0) = CONST 
    0xfc: REVERT vf9(0x0), vf9(0x0)

    Begin block 0xfd
    prev=[0xc0], succ=[0x10b, 0x10f]
    =================================
    0xff: vff = ADD vae(0x4), ve6
    0x101: v101(0x20) = CONST 
    0x104: v104 = ADD vff, v101(0x20)
    0x105: v105 = GT v104, vc2
    0x106: v106 = ISZERO v105
    0x107: v107(0x10f) = CONST 
    0x10a: JUMPI v107(0x10f), v106

    Begin block 0x10b
    prev=[0xfd], succ=[]
    =================================
    0x10b: v10b(0x0) = CONST 
    0x10e: REVERT v10b(0x0), v10b(0x0)

    Begin block 0x10f
    prev=[0xfd], succ=[0x12d, 0x131]
    =================================
    0x111: v111 = CALLDATALOAD vff
    0x113: v113(0x20) = CONST 
    0x115: v115 = ADD v113(0x20), vff
    0x118: v118(0x1) = CONST 
    0x11b: v11b = MUL v111, v118(0x1)
    0x11d: v11d = ADD v115, v11b
    0x11e: v11e = GT v11d, vc2
    0x11f: v11f(0x100000000) = CONST 
    0x126: v126 = GT v111, v11f(0x100000000)
    0x127: v127 = OR v126, v11e
    0x128: v128 = ISZERO v127
    0x129: v129(0x131) = CONST 
    0x12c: JUMPI v129(0x131), v128

    Begin block 0x12d
    prev=[0x10f], succ=[]
    =================================
    0x12d: v12d(0x0) = CONST 
    0x130: REVERT v12d(0x0), v12d(0x0)

    Begin block 0x131
    prev=[0x10f], succ=[0x285]
    =================================
    0x13d: v13d(0x285) = CONST 
    0x140: JUMP v13d(0x285)

    Begin block 0x285
    prev=[0x131], succ=[0x601B0x285]
    =================================
    0x286: v286(0x28d) = CONST 
    0x289: v289(0x601) = CONST 
    0x28c: JUMP v289(0x601)

    Begin block 0x601B0x285
    prev=[0x285], succ=[0x28d]
    =================================
    0x602S0x285: v602V285(0x0) = CONST 
    0x605S0x285: v605V285(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = CONST 
    0x626S0x285: v626V285(0x0) = CONST 
    0x628S0x285: v628V285(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b) = SHL v626V285(0x0), v605V285(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x62cS0x285: v62cV285 = SLOAD v628V285(0x10d6a54a4754c8869d6886b5f5d7fbfa5b4522237ea5c60d11bc4e7a1ff9390b)
    0x631S0x285: JUMP v286(0x28d)

    Begin block 0x28d
    prev=[0x601B0x285], succ=[0x2c1, 0x350]
    =================================
    0x28e: v28e(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2a3: v2a3 = AND v28e(0xffffffffffffffffffffffffffffffffffffffff), v62cV285
    0x2a4: v2a4 = CALLER 
    0x2a5: v2a5(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2ba: v2ba = AND v2a5(0xffffffffffffffffffffffffffffffffffffffff), v2a4
    0x2bb: v2bb = EQ v2ba, v2a3
    0x2bc: v2bc = ISZERO v2bb
    0x2bd: v2bd(0x350) = CONST 
    0x2c0: JUMPI v2bd(0x350), v2bc

    Begin block 0x2c1
    prev=[0x28d], succ=[0x2c9]
    =================================
    0x2c1: v2c1(0x2c9) = CONST 
    0x2c5: v2c5(0x632) = CONST 
    0x2c8: CALLPRIVATE v2c5(0x632), vdc, v2c1(0x2c9)

    Begin block 0x2c9
    prev=[0x2c1], succ=[0x316, 0x337]
    =================================
    0x2ca: v2ca(0x0) = CONST 
    0x2cc: v2cc = ADDRESS 
    0x2cd: v2cd(0xffffffffffffffffffffffffffffffffffffffff) = CONST 
    0x2e2: v2e2 = AND v2cd(0xffffffffffffffffffffffffffffffffffffffff), v2cc
    0x2e3: v2e3 = CALLVALUE 
    0x2e6: v2e6(0x40) = CONST 
    0x2e8: v2e8 = MLOAD v2e6(0x40)
    0x2ef: CALLDATACOPY v2e8, v115, v111
    0x2f2: v2f2 = ADD v2e8, v111
    0x2fb: v2fb(0x0) = CONST 
    0x2fd: v2fd(0x40) = CONST 
    0x2ff: v2ff = MLOAD v2fd(0x40)
    0x302: v302 = SUB v2f2, v2ff
    0x306: v306 = GAS 
    0x307: v307 = CALL v306, v2e2, v2e3, v2ff, v302, v2ff, v2fb(0x0)
    0x30c: v30c = RETURNDATASIZE 
    0x30e: v30e(0x0) = CONST 
    0x311: v311 = EQ v30c, v30e(0x0)
    0x312: v312(0x337) = CONST 
    0x315: JUMPI v312(0x337), v311

    Begin block 0x316
    prev=[0x2c9], succ=[0x33c]
    =================================
    0x316: v316(0x40) = CONST 
    0x318: v318 = MLOAD v316(0x40)
    0x31b: v31b(0x1f) = CONST 
    0x31d: v31d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0) = NOT v31b(0x1f)
    0x31e: v31e(0x3f) = CONST 
    0x320: v320 = RETURNDATASIZE 
    0x321: v321 = ADD v320, v31e(0x3f)
    0x322: v322 = AND v321, v31d(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe0)
    0x324: v324 = ADD v318, v322
    0x325: v325(0x40) = CONST 
    0x327: MSTORE v325(0x40), v324
    0x328: v328 = RETURNDATASIZE 
    0x32a: MSTORE v318, v328
    0x32b: v32b = RETURNDATASIZE 
    0x32c: v32c(0x0) = CONST 
    0x32e: v32e(0x20) = CONST 
    0x331: v331 = ADD v318, v32e(0x20)
    0x332: RETURNDATACOPY v331, v32c(0x0), v32b
    0x333: v333(0x33c) = CONST 
    0x336: JUMP v333(0x33c)

    Begin block 0x33c
    prev=[0x316, 0x337], succ=[0x346, 0x34a]
    =================================
    0x342: v342(0x34a) = CONST 
    0x345: JUMPI v342(0x34a), v307

    Begin block 0x346
    prev=[0x33c], succ=[]
    =================================
    0x346: v346(0x0) = CONST 
    0x349: REVERT v346(0x0), v346(0x0)

    Begin block 0x34a
    prev=[0x33c], succ=[0x359]
    =================================
    0x34c: v34c(0x359) = CONST 
    0x34f: JUMP v34c(0x359)

    Begin block 0x359
    prev=[0x34a], succ=[0x141]
    =================================
    0x35d: JUMP vab(0x141)

    Begin block 0x141
    prev=[0x359], succ=[]
    =================================
    0x142: STOP 

    Begin block 0x337
    prev=[0x2c9], succ=[0x33c]
    =================================
    0x338: v338(0x60) = CONST 

    Begin block 0x350
    prev=[0x28d], succ=[0x2160xaa]
    =================================
    0x351: v351(0x358) = CONST 
    0x354: v354(0x216) = CONST 
    0x357: JUMP v354(0x216)

    Begin block 0x2160xaa
    prev=[0x350], succ=[0x21e0xaa]
    =================================
    0x2170xaa: vaa217(0x21e) = CONST 
    0x21a0xaa: vaa21a(0x514) = CONST 
    0x21d0xaa: CALLPRIVATE vaa21a(0x514), vaa217(0x21e)

    Begin block 0x21e0xaa
    prev=[0x2160xaa], succ=[0x5aaB0x21e0xaa]
    =================================
    0x21f0xaa: vaa21f(0x22e) = CONST 
    0x2220xaa: vaa222(0x229) = CONST 
    0x2250xaa: vaa225(0x5aa) = CONST 
    0x2280xaa: JUMP vaa225(0x5aa)

    Begin block 0x5aaB0x21e0xaa
    prev=[0x21e0xaa], succ=[0x2290xaa]
    =================================
    0x5abS0x21e0xaa: v5abV21eaa(0x0) = CONST 
    0x5aeS0x21e0xaa: v5aeV21eaa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = CONST 
    0x5cfS0x21e0xaa: v5cfV21eaa(0x0) = CONST 
    0x5d1S0x21e0xaa: v5d1V21eaa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3) = SHL v5cfV21eaa(0x0), v5aeV21eaa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5d5S0x21e0xaa: v5d5V21eaa = SLOAD v5d1V21eaa(0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3)
    0x5daS0x21e0xaa: JUMP vaa222(0x229)

    Begin block 0x2290xaa
    prev=[0x5aaB0x21e0xaa], succ=[0x5db0xaa]
    =================================
    0x22a0xaa: vaa22a(0x5db) = CONST 
    0x22d0xaa: JUMP vaa22a(0x5db)

    Begin block 0x5db0xaa
    prev=[0x2290xaa], succ=[0x5f80xaa, 0x5fc0xaa]
    =================================
    0x5dc0xaa: vaa5dc = CALLDATASIZE 
    0x5dd0xaa: vaa5dd(0x0) = CONST 
    0x5e00xaa: CALLDATACOPY vaa5dd(0x0), vaa5dd(0x0), vaa5dc
    0x5e10xaa: vaa5e1(0x0) = CONST 
    0x5e40xaa: vaa5e4 = CALLDATASIZE 
    0x5e50xaa: vaa5e5(0x0) = CONST 
    0x5e80xaa: vaa5e8 = GAS 
    0x5e90xaa: vaa5e9 = DELEGATECALL vaa5e8, v5d5V21eaa, vaa5e5(0x0), vaa5e4, vaa5e1(0x0), vaa5e1(0x0)
    0x5ea0xaa: vaa5ea = RETURNDATASIZE 
    0x5eb0xaa: vaa5eb(0x0) = CONST 
    0x5ee0xaa: RETURNDATACOPY vaa5eb(0x0), vaa5eb(0x0), vaa5ea
    0x5f00xaa: vaa5f0(0x0) = CONST 
    0x5f30xaa: vaa5f3 = EQ vaa5e9, vaa5f0(0x0)
    0x5f40xaa: vaa5f4(0x5fc) = CONST 
    0x5f70xaa: JUMPI vaa5f4(0x5fc), vaa5f3

    Begin block 0x5f80xaa
    prev=[0x5db0xaa], succ=[]
    =================================
    0x5f80xaa: vaa5f8 = RETURNDATASIZE 
    0x5f90xaa: vaa5f9(0x0) = CONST 
    0x5fb0xaa: RETURN vaa5f9(0x0), vaa5f8

    Begin block 0x5fc0xaa
    prev=[0x5db0xaa], succ=[]
    =================================
    0x5fd0xaa: vaa5fd = RETURNDATASIZE 
    0x5fe0xaa: vaa5fe(0x0) = CONST 
    0x6000xaa: REVERT vaa5fe(0x0), vaa5fd

}

