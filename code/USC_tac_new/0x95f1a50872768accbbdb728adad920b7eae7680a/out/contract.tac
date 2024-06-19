function __function_selector__() public {
    Begin block 0x0
    prev=[], succ=[0x40, 0x43]
    =================================
    0x0: v0(0x80) = CONST 
    0x2: v2(0x40) = CONST 
    0x4: MSTORE v2(0x40), v0(0x80)
    0x5: v5(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7) = CONST 
    0x26: v26 = SLOAD v5(0xc5f16f0fcc639fa48a6947836d9850f504798523bf8c9a3a87d5876cf622bcf7)
    0x27: v27(0x0) = CONST 
    0x29: v29 = CALLDATASIZE 
    0x2c: CALLDATACOPY v27(0x0), v27(0x0), v29
    0x2f: v2f = CALLDATASIZE 
    0x32: v32 = GAS 
    0x33: v33 = DELEGATECALL v32, v26, v27(0x0), v2f, v27(0x0), v27(0x0)
    0x36: v36 = RETURNDATASIZE 
    0x39: RETURNDATACOPY v27(0x0), v27(0x0), v36
    0x3c: v3c = ISZERO v33
    0x3d: v3d(0x43) = CONST 
    0x3f: JUMPI v3d(0x43), v3c

    Begin block 0x40
    prev=[0x0], succ=[]
    =================================
    0x40: v40 = RETURNDATASIZE 
    0x42: RETURN v27(0x0), v40

    Begin block 0x43
    prev=[0x0], succ=[]
    =================================
    0x44: v44 = RETURNDATASIZE 
    0x46: REVERT v27(0x0), v44

}

