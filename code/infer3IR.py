import os
import pandas as pd
import re
import networkx as nx
import time
from multiprocessing import Pool
# from taint_utils import findPC,findSink,findSinkbypass,findSource, block_propagate, block_propagate_bypass, edge_propagate

def infer(file):
    item = file
    error = False
    path = '../USC_tac_creation/'+item+'/out'
    # DataFrame二维表格
    if not os.path.exists(path + '/contract.tac'):
        print('no exist: ', item)
        with open('../noexist.txt','a') as f:
            f.write(item+'\n')
        return
    df = pd.read_table(path + '/contract.tac')

    df.columns = ["3IR"]
    df['blockname']='0'
    df['leftvariable']='0'
    df['rightvariable']='0'
    df['option']='0'
    df['functionname']='0' # 5
    df['functiontype'] = '0'
    df['callersource'] = False  # 是否与CALLER有关
    df['constant'] = '0'  # 内存位置
    df['memloc'] = '0'  # 变量所在的内存地址
    df['succ'] = ''  # 后续block

    #已定义的内存地址
    memlocvar = {}
    #未定义的内存地址
    unlocmemvar = []
    # taint_col = ['function','block','var']
    # taint_source = pd.DataFrame([],columns=taint_col)
    # 调用者列表
    callerVars = []

    ###################  3IR parsing ########################
    for i in range(0,len(df)):
        blockindex=df.iloc[i,0].find('block')
        # 取blockname
        if blockindex>0:
            # .iloc 是按整数位置选择数据
            k=df.iloc[i,0][(blockindex+6):]
            df.iloc[i,1]=k
            #print (b.iloc[i,0][(blockindex+6):])
        df.iloc[i,1]=k

        # 分割
        bsplit=re.split(r'(?:[, : \s ( )])',df.iloc[i,0])
        #print(bsplit)

        # 处理含=的行的操作符与变量
        if (bsplit.count('=')>0):
            eindex=bsplit.index('=')
            # = 后一位为操作符
            df.iloc[i,4]=bsplit[eindex+1]
            #print (bsplit[eindex])
            for p in range(0,eindex):
                findvar=bsplit[p]
                # 左变量
                if (findvar.find('v')>-1):
                    df.iloc[i,2]= findvar
                    if p != (eindex-1):
                        df.iloc[i,8] = bsplit[p+1]

            # 右变量 可能不唯一
            for p in range(eindex,len(bsplit)):
                if (bsplit[p].find('v')>-1):
                    df.iloc[i,3]=df.iloc[i,3]+','+ bsplit[p]
        
        else:
            # 注意行前有空格

            # 处理succ
            if(df.iloc[i,0].find('succ') > -1):
                succindex = df.iloc[i,0].find('succ')
                df.iloc[i,10] = df.iloc[i,0][succindex+6:-1]
                # print(df.iloc[i,10])
            # 跳转指令如 JUMP JUMPI REVERT STOP THROW RETURN
            # MSTORE SSTORE CALLDATACOPY CALLPRIVATE
            if(len(bsplit)>7 and df.iloc[i,0].find('succ')<0):
                op = bsplit[6]
                df.iloc[i, 4] = op
                for p in range(0, len(bsplit)):
                    if(bsplit[p].find('v') > -1):
                        df.iloc[i, 3] = df.iloc[i, 3] + ',' + bsplit[p]

            # if(len(bsplit)>7 and df.iloc[i,0].find('succ')<0):
            #     df.iloc[i,4]=bsplit[6]
            #
            #     for p in range(0,len(bsplit)):
            #         if (bsplit[p].find('v')>-1):
            #             df.iloc[i,3]=df.iloc[i,3]+','+ bsplit[p]

        # 处理function名和类型
        if (bsplit[0]=='function'):
            df.iloc[i,5]=bsplit[1]
            df.iloc[i,6] = bsplit[-2] # 倒数第二
        else:
            df.iloc[i,5]=df.iloc[i-1,5]
            df.iloc[i,6] = df.iloc[i-1,6]

        # succ
        if (df.iloc[i, 10] == ''):
            df.iloc[i, 10] = df.iloc[i - 1, 10]

        # MLOAD
        # ？还需考虑SLOAD，CALLVALUE，CALLER
        if df.iloc[i,4] == 'MLOAD':
            if df.iloc[i,0].find('(')>-1:
                df.iloc[i,9] = df.iloc[i,5]+'&m'+df.iloc[i,0][df.iloc[i,0].find('(')+1:df.iloc[i,0].find(')')]
                memlocvar[df.iloc[i,2]] = df.iloc[i,9]
        # ADD
        if df.iloc[i,4] == 'ADD':
            para = df.iloc[i,3].split(',')
            row = df.iloc[i]
            # 如果ADD中的变量包含MLOAD调用
            # 内存地址 + 值 ？
            if len(para) != 3:
                # errors.add(item)
                print('error: ', item)
                error = True
                # print(para)
                continue
            
            
            if para[1] in memlocvar.keys() or para[2] in memlocvar.keys():
                if df.iloc[i,0].find('(')>-1:
                    const = row['3IR'][row['3IR'].find('(')+1:row['3IR'].find(')')]
                    if para[1] in memlocvar.keys():
                        memloc = memlocvar[para[1]]
                        newmemloc = memloc +'+'+const
                        memlocvar[row['leftvariable']]= newmemloc
                    if para[2] in memlocvar.keys():
                        memloc = memlocvar[para[2]]
                        newmemloc = memloc +'+'+const
                        memlocvar[row['leftvariable']]= newmemloc
                    df.iloc[i,9] = newmemloc
                else:
                    unlocmemvar.append(row['leftvariable'])
        # SUB
        if df.iloc[i,4] == 'SUB':
            para = df.iloc[i,3].split(',')
            row = df.iloc[i]
            if para[1] in memlocvar.keys(): 
                if df.iloc[i,0].find('(')>-1:
                    const = row['3IR'][row['3IR'].find('(')+1:row['3IR'].find(')')]
                    memloc = memlocvar[para[1]]
                    newmemloc = memloc +'-'+const
                    memlocvar[row['leftvariable']]= newmemloc
                    df.iloc[i,9] = newmemloc
                else:
                    unlocmemvar.append(row['leftvariable'])


        stmtOp = df.iloc[i]['option']
        # CALLER
        if stmtOp == 'CALLER':
            callerVars.append(df.iloc[i,2])
            df.iloc[i,7] = True
        # AND OR CALLER后续做的数值计算
        if stmtOp == 'AND' or stmtOp == 'OR':
            stmtRVs = df.iloc[i,3].split(',')
            for stmtRV in stmtRVs:
                if stmtRV == '0':
                    continue
                if stmtRV in callerVars:
                    callerVars.append(df.iloc[i,2])
                    # df.iloc[i,2] == 'CALLER'
                    df.iloc[i,7] = True
                    break


    # MSTORE
    mstores = df[df['option']=="MSTORE"]
    for i,row in mstores.iterrows():
        paras = row['rightvariable'].split(',')
        if paras[1] in memlocvar.keys():
            df.iloc[row.name,2] = memlocvar[paras[1]]
            df.iloc[row.name,9] = memlocvar[paras[1]]

    # function signature blockname
    for i,row in df.iterrows():
        if row['3IR'][:8] == 'function':
            df.iloc[i,1] = df.iloc[i+1]['blockname']
    # df.to_csv(targetPath+testcsv,index=False)
    
    # with open('../../smartbugs_3IR/'+item+'.csv','w') as f:
    if not error:
        df.to_csv('../USC_3IR_creation/'+item+'.csv',index=False)
    else:
        with open('./error.txt','a') as f:
            f.write(item+'\n')
            

# folder that saves tac
toAnalysis = os.listdir('../USC_tac_creation')
# folder that saves 3IR
# analyzed = os.listdir('../USC_3IR')
# analyzed = [x[:-4] for x in analyzed]
# toAnalysis = list(set(toAnalysis) - set(analyzed))

print(len(toAnalysis))
pool = Pool(40)
pool.map(infer, toAnalysis)
# for cnt, item in enumerate(toAnalysis):
#     if item in analyzed:
#         continue
#     pool.apply_async(infer, item)
#     if cnt%1000 == 0:
#         print(cnt)
