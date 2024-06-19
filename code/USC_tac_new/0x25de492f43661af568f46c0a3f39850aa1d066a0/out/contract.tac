function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x4b, 0x47]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x26: v26 = SLOAD v5(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x27: v27 = CALLDATASIZE 
    0x28: v28(0x0) = CONST 
    0x2b: CALLDATACOPY v28(0x0), v28(0x0), v27
    0x2c: v2c(0x0) = CONST 
    0x2f: v2f = CALLDATASIZE 
    0x30: v30(0x0) = CONST 
    0x33: v33(0x2710) = CONST 
    0x36: v36 = GAS 
    0x37: v37 = SUB v36, v33(0x2710)
    0x38: v38 = DELEGATECALL v37, v26, v30(0x0), v2f, v2c(0x0), v2c(0x0)
    0x39: v39 = RETURNDATASIZE 
    0x3b: v3b(0x0) = CONST 
    0x3e: RETURNDATACOPY v3b(0x0), v3b(0x0), v39
    0x40: v40(0x0) = CONST 
    0x43: v43 = EQ v38, v40(0x0)
    0x44: v44(0x4b) = CONST 
    0x46: JUMPI v44(0x4b), v43

    Begin block 0x4b
    prev=[0x0], succ=[]
    =================================
    0x4d: v4d(0x0) = CONST 
    0x4f: REVERT v4d(0x0), v39

    Begin block 0x47
    prev=[0x0], succ=[]
    =================================
    0x48: v48(0x0) = CONST 
    0x4a: RETURN v48(0x0), v39

}

