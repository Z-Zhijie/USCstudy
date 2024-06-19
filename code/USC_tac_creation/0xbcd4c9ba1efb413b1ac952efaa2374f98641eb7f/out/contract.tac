function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x9a]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x6: MSTORE v2(0x40), v0(0x80)
    0x7: v7(0x6f72672e6d6f6e657468612e70726f78792e6f776e6572000000000000000000) = CONST 
    0x29: MSTORE v0(0x80), v7(0x6f72672e6d6f6e657468612e70726f78792e6f776e6572000000000000000000)
    0x2a: v2a(0x3b) = CONST 
    0x2d: v2d = CALLER 
    0x2e: v2e(0x100000000) = CONST 
    0x34: v34(0x9a) = CONST 
    0x38: v38(0x9a00000000) = MUL v2e(0x100000000), v34(0x9a)
    0x39: v39(0x9a) = DIV v38(0x9a00000000), v2e(0x100000000)
    0x3a: JUMP v39(0x9a)

    Begin block 0x9a
    prev=[0x0], succ=[0x3b]
    =================================
    0x9b: v9b(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22) = CONST 
    0xbc: SSTORE v9b(0x3ca57e4b51fc2e18497b219410298879868edada7e6fe5132c8feceb0a080d22), v2d
    0xbd: JUMP v2a(0x3b)

    Begin block 0x3b
    prev=[0x9a], succ=[0x94, 0x95]
    =================================
    0x3c: v3c(0x40) = CONST 
    0x3f: v3f = MLOAD v3c(0x40)
    0x40: v40(0x6f72672e6d6f6e657468612e70726f78792e70656e64696e674f776e65720000) = CONST 
    0x62: MSTORE v3f, v40(0x6f72672e6d6f6e657468612e70726f78792e70656e64696e674f776e65720000)
    0x64: v64 = MLOAD v3c(0x40)
    0x68: v68(0x0) = SUB v3f, v64
    0x69: v69(0x1e) = CONST 
    0x6b: v6b(0x1e) = ADD v69(0x1e), v68(0x0)
    0x6d: v6d = SHA3 v64, v6b(0x1e)
    0x6e: v6e(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52) = CONST 
    0x8f: v8f = EQ v6e(0xcfd0c6ea5352192d7d4c5d4e7a73c5da12c871730cb60ff57879cbe7b403bb52), v6d
    0x90: v90(0x95) = CONST 
    0x93: JUMPI v90(0x95), v8f

    Begin block 0x94
    prev=[0x3b], succ=[]
    =================================
    0x94: THROW 

    Begin block 0x95
    prev=[0x3b], succ=[0xbe]
    =================================
    0x96: v96(0xbe) = CONST 
    0x99: JUMP v96(0xbe)

    Begin block 0xbe
    prev=[0x95], succ=[]
    =================================
    0xbf: vbf(0x17c0) = CONST 
    0xc3: vc3(0xcd) = CONST 
    0xc6: vc6(0x0) = CONST 
    0xc8: CODECOPY vc6(0x0), vc3(0xcd), vbf(0x17c0)
    0xc9: vc9(0x0) = CONST 
    0xcb: RETURN vc9(0x0), vbf(0x17c0)

}

