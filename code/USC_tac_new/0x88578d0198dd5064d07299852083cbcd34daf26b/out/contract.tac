function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x42, 0x46]
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
    0x33: v33 = GAS 
    0x34: v34 = DELEGATECALL v33, v26, v30(0x0), v2f, v2c(0x0), v2c(0x0)
    0x35: v35 = RETURNDATASIZE 
    0x36: v36(0x0) = CONST 
    0x39: RETURNDATACOPY v36(0x0), v36(0x0), v35
    0x3b: v3b(0x0) = CONST 
    0x3e: v3e = EQ v34, v3b(0x0)
    0x3f: v3f(0x46) = CONST 
    0x41: JUMPI v3f(0x46), v3e

    Begin block 0x42
    prev=[0x0], succ=[]
    =================================
    0x42: v42 = RETURNDATASIZE 
    0x43: v43(0x0) = CONST 
    0x45: RETURN v43(0x0), v42

    Begin block 0x46
    prev=[0x0], succ=[]
    =================================
    0x47: v47 = RETURNDATASIZE 
    0x48: v48(0x0) = CONST 
    0x4a: REVERT v48(0x0), v47

}

