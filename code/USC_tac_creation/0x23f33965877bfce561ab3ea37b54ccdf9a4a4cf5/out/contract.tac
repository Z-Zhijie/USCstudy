function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x12]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xd) = CONST 
    0x8: v8 = CALLER 
    0x9: v9(0x12) = CONST 
    0xc: JUMP v9(0x12)

    Begin block 0x12
    prev=[0x0], succ=[0xd]
    =================================
    0x13: v13(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103) = CONST 
    0x34: SSTORE v13(0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103), v8
    0x35: JUMP v5(0xd)

    Begin block 0xd
    prev=[0x12], succ=[0x36]
    =================================
    0xe: ve(0x36) = CONST 
    0x11: JUMP ve(0x36)

    Begin block 0x36
    prev=[0xd], succ=[]
    =================================
    0x37: v37(0x856) = CONST 
    0x3b: v3b(0x45) = CONST 
    0x3e: v3e(0x0) = CONST 
    0x40: CODECOPY v3e(0x0), v3b(0x45), v37(0x856)
    0x41: v41(0x0) = CONST 
    0x43: RETURN v41(0x0), v37(0x856)

}

