import pandas as pd
import json
import os
import re


sameop = ['AND', 'OR', 'DIV', 'MUL']

def samepropa(target, rowloc, vars, sameop):
    target = target[target.index > rowloc]
    for i, stmt in target.iterrows():
        stmtRVs = stmt['rightvariable'].split(',')
        if not stmt['option'] in sameop:
            continue
        for stmtRV in stmtRVs:
            if stmtRV == '0': continue
            if stmtRV in vars:
                vars.append(stmt['leftvariable'])
    return vars

def findPC(df):
    candi = set(df['functionname'])
    functions = []
    PC = []
    for f in candi:
        # print('function',f)
        dfF = df[df['functionname']==f]
        # 排除非public
        if dfF.iloc[0]['functiontype'] != 'public':
            continue
        # if sum(dfF['option']=='REVERT')+sum(dfF['option']=='STOP') <2:
        #     continue

        # 与caller有关的变量
        callervars = list(dfF[dfF['callersource']]['leftvariable'])

        # CALLPRIVATE 函数中调用其他函数中的代码段
        callpri = dfF[dfF['option']=='CALLPRIVATE']
        # if 'CALLPRIVATE' in dfF['option']:

        # lastblock = '-1'

        # print(len(callerstmt))
        # 处理CALLPRIVATE即处理函数调用的其他函数
        if len(callpri) != 0:
            # print(callpri)
            for i,row in callpri.iterrows():
                ir = row['3IR']
                # if f == 'setMigrator':
                #     print(ir)
                #     print(ir[ir.find('(')+1:ir.find(')')])
                priname = ir[ir.find('(')+1:ir.find(')')]
                args = ir[ir.find(',')+2:].split(', ')
                # print(args)
                callerarg=[]
                index = 0
                for j in args:
                    if j.find('(') < 0 and j in callervars:
                        call = 'v'+ priname[2:] + 'arg' + str(index)
                        callerarg.append(call)
                    index += 1

                # print(priname)
                # 找到被public函数调用的非public函数
                prifunc = df[df['functionname']==priname]
                if len(prifunc) == 0:
                    continue
                if prifunc.iloc[0]['functiontype'] != 'public':
                    prifunc = df[df['functionname']==priname]
                    p = getPC(prifunc,f,callerarg)
                    if p != '':
                        PC.append(p)
                # # 函数中存在owner权限控制 SLOAD CALLER EQ
                # PCop = ['SLOAD','CALLER','EQ']
                # temp = prifunc[prifunc['option'].isin(PCop)]
                #
                # targetOp = temp['option']
                # # if priname == '0x23b7': print(list(targetOp))
                # if list(targetOp)[:3] == ['SLOAD','CALLER','EQ'] or list(targetOp)[:3] == ['CALLER','SLOAD','EQ'] :
                #     print('111')
                #     ir = temp[temp['option']=='SLOAD']['3IR'].iloc[0]
                #     Sloc = ir[ir.find('(')+1:ir.find(')')]
                #     PC.append(('owner',f,Sloc))

        p = getPC(dfF, f, '')
        if p != '':
            PC.append(p)
        # print(PC)

    return PC

def getPC(dfF,f,callerarg):
    # print(f)
    # print(callerarg)
    lastblock = '-1'
    callerargs = callerarg
    # callersource不为零的行即与CALLER有关
    callerstmt = dfF[dfF['callersource']]
    calldatavars = list(dfF[dfF['option'] == 'CALLDATALOAD']['leftvariable'])

    if callerarg != '':
        for i,row in dfF.iterrows():
            for j in callerargs:
                if j in row['rightvariable'] and (row['option'] == 'AND' or row['option'] == 'OR'):
                    callerargs.append(row['leftvariable'])
                    callerstmt = pd.merge(callerstmt, dfF[dfF['leftvariable'] == row['leftvariable']], how='outer') # 合并

    # print(callerargs)
    if len(callerstmt) != 0:
        for i, row in callerstmt.iterrows():
            # if row['blockname'] == '0x88aB0x198':
            # print(lastblock)
            if row['blockname'] == lastblock:
                continue
            lastblock = row['blockname']
            # caller = row['leftvariable']
            targetblock = dfF[dfF['blockname'] == row['blockname']]

            # 与caller有关的变量
            if callerargs != '':
                callervars = list(targetblock[targetblock['callersource']]['leftvariable']) + callerargs
            else:
                callervars = list(targetblock[targetblock['callersource']]['leftvariable'])

            # callervars = list(targetblock[targetblock['callersource']]['leftvariable'])



            # PCop = ['MSTORE','SLOAD','CALLER','SHA3','EQ','ISZERO']
            PCop = ['MSTORE', 'SLOAD', 'CALLER', 'SHA3', 'EQ', 'GT', 'LT', 'SLT', 'SGT', 'JUMPI']
            targetOp = []
            # targetOp = targetblock[targetblock['option'].isin(PCop)]['option']
            for i, row in targetblock.iterrows():
                # MSTORE 的变量与CALLER相关
                if row['option'] == 'MSTORE' and (row['rightvariable'].split(',')[2] in callervars):
                    if targetOp.count('CALLER') == 0:
                        # print('!!!')
                        targetOp.append('CALLER')
                if row['leftvariable'] in callerargs:
                    if targetOp.count('CALLER') == 0:
                        # print('!!!')
                        targetOp.append('CALLER')
                if row['option'] in PCop:
                    targetOp.append(row['option'])


            # add pattern
            if list(targetOp) == ['CALLER', 'EQ', 'JUMPI']:
                targetfuncdf = dfF[dfF['functionname'] == row['functionname']]
                sloaddf = targetfuncdf[targetfuncdf['option'] == 'SLOAD']
                if sloaddf.empty:
                    continue
                eq = targetblock[targetblock['option'] == 'EQ']
                flag = 0
                for k in range(len(eq)):
                    eqRV = eq.iloc[k]['rightvariable'].split(',')
                    for caller in callervars:
                        if caller in eqRV:
                            flag = 1
                if flag == 0:
                    continue
                return '1'



            # PC 1 #

            # if list(targetOp) == ['SLOAD', 'CALLER', 'EQ', 'JUMPI'] or \
            #         list(targetOp) == ['CALLER', 'SLOAD', 'EQ', 'JUMPI'] or \
            #             list(targetOp) == ['CALLER', 'SLOAD', 'EQ'] or \
            #                 list(targetOp) == ['SLOAD', 'CALLER', 'EQ']:
            if 'SLOAD' in list(targetOp) and 'EQ' in list(targetOp):
                # print(row['blockname'])
                # ir = targetblock[targetblock['option']=='SLOAD']['3IR'].iloc[0]
                # Sloc = ir[ir.find('(')+1:ir.find(')')]
                # PC.append(('owner',f,Sloc))
                # if row['blockname'] == '0x2249B0xa5b': print(list(targetOp)[:3])
                sload = targetblock[targetblock['option'] == 'SLOAD']
                eq = targetblock[targetblock['option'] == 'EQ']

                Ssplit = re.split(r'(?:[, : \s])', sload.iloc[0]['3IR'])
                ltemp = Ssplit[9].find('(')
                if ltemp > -1:
                    Sloc = Ssplit[9][Ssplit[9].find('(') + 1:Ssplit[9].find(')')]

                    sloadvar = []
                    for k in range(len(sload)):
                        sloadvar.append(sload.iloc[k]['leftvariable'])
                    # SLOAD后进行的数值计算
                    sloadvars = samepropa(targetblock, sload.iloc[0].name, sloadvar, sameop)
                    # print(sloadvars)
                    for k in range(len(eq)):
                        eqRV = eq.iloc[k]['rightvariable'].split(',')

                        flag = False
                        # print('111')
                        for caller in callervars:
                            if caller in eqRV:
                                # print('CALLER:', callervars)
                                for x in eqRV:
                                    # print(x)
                                    if x != caller and x != '0':
                                        flag = True
                                        eqRV1 = x
                                        break
                            else:
                                continue
                            # print(eqRV1)
                        if flag:
                            if eqRV1 in sloadvars:
                                # print('333')
                                # print(('owner',f,Sloc))
                                # Perm = eq.iloc[0]['leftvariable']
                                # PC.append(('owner', f, Sloc))
                                return Sloc
            # PC 2/3
            # if list(targetOp) == ['CALLER', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'EQ'] or \
            #     list(targetOp) == ['CALLER', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'ISZERO','ISZERO'] or \
            if list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'EQ', 'JUMPI'] or \
                list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'CALLER', 'EQ', 'JUMPI']:
                # or list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'EQ']:
                # list (targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD'] or \
                # print(targetblock[targetblock['option'] == 'MSTORE'])
                flag = 0
                eq = targetblock[targetblock['option'] == 'EQ'].iloc[0]
                eqsplit = re.split(r'(?:[, : \s])', eq['3IR'])
                eqRV = eq['rightvariable'].split(',')
                eq0 = eqsplit[9].find('(')
                eqnumber = ''
                if eq0 > -1:
                    eqnumber = eqsplit[9][eqsplit[9].find('(') + 1:eqsplit[9].find(')')]
                else:
                    eqnumber = eqsplit[11][eqsplit[11].find('(') + 1:eqsplit[11].find(')')]
                eq0 = 0
                if eqnumber == '0x00' or eqnumber == '0x0':
                    eq0 = 1
                mstore0 = targetblock[targetblock['option'] == 'MSTORE'].iloc[0]
                Msplit0 = re.split(r'(?:[, : \s])', mstore0['3IR'])
                ltemp0 = Msplit0[9].find('(')  # MSTORE 第二项

                if ltemp0 < 0:
                    Mloc0 = Msplit0[9]
                    # MSTORE 与 CALLER 有关 且 EQ 是与 0 比较
                    if eq0 == 1 and Mloc0 in callervars:
                        flag = 1
                    # EQ 项与 CALLER 有关
                    if (Mloc0 not in callervars) and (eqRV[0] in callervars or eqRV[1] in callervars):
                        flag = 1
                if flag == 1:
                    mstore1 = targetblock[targetblock['option'] == 'MSTORE'].iloc[1]
                    Msplit1 = re.split(r'(?:[, : \s])', mstore1['3IR'])
                    ltemp1 = Msplit1[9].find('(')
                    if ltemp1 > -1:
                        # print(Msplit[9])
                        Mloc1 = Msplit1[9][Msplit1[9].find('(') + 1:Msplit1[9].find(')')]
                        Pdv = 'SHA3(msg.sender,' + Mloc1 + ')'
                        # PC.append(('whitelist', f, Pdv))
                        return Mloc1

            # PC4
            if list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'JUMPI']:

                rolemstore = targetblock[targetblock['option'] == 'MSTORE'].iloc[0]
                Msplit = re.split(r'(?:[, : \s])', rolemstore['3IR'])
                ltemp = Msplit[9].find('(')
                if ltemp > -1:
                    rolename = Msplit[9][Msplit[9].find('(') + 1:Msplit[9].find(')')]
                    mstore = targetblock[targetblock['option'] == 'MSTORE'].iloc[1]
                    Msplit = re.split(r'(?:[, : \s])', mstore['3IR'])
                    ltemp = Msplit[9].find('(')
                    if ltemp > -1:
                        Mloc = Msplit[9][Msplit[9].find('(') + 1:Msplit[9].find(')')]
                        temp = 'SHA3(rolename,' + Mloc + ')'
                        Pdv = 'SHA3(msg.sender,' + temp + ')'
                        # PC.append(('Rolebased', f, Pdv))
                        return Mloc1

            # PC5
            if list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'GT', 'JUMPI'] or \
                    list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'LT', 'JUMPI'] or \
                    list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'SGT', 'JUMPI'] or \
                    list(targetOp) == ['CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'SLT', 'JUMPI']:
                mstore0 = targetblock[targetblock['option'] == 'MSTORE'].iloc[0]
                Msplit0 = re.split(r'(?:[, : \s])', mstore0['3IR'])
                ltemp0 = Msplit0[9].find('(')  # MSTORE 第二项

                if ltemp0 < 0:
                    Mloc0 = Msplit0[9]
                    # MSTORE 与 CALLER 有关 (另一项应为CALLDATALOAD)
                    if Mloc0 in callervars:
                        mstore1 = targetblock[targetblock['option'] == 'MSTORE'].iloc[1]
                        Msplit1 = re.split(r'(?:[, : \s])', mstore1['3IR'])
                        ltemp1 = Msplit1[9].find('(')
                        if 'GT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'GT']
                        if 'LT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'LT']
                        if 'SGT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'SGT']
                        if 'SLT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'SLT']

                        sload = targetblock[targetblock['option'] == 'SLOAD']

                        if ltemp1 > -1:
                            # print(Msplit[9])

                            sloadvar = sload.iloc[0]['leftvariable']
                            # SLOAD后进行的数值计算
                            sloadvars = samepropa(targetblock, sload.iloc[0].name, [sloadvar], sameop)
                            # print(sloadvars)

                            eqRV = eq.iloc[0]['rightvariable'].split(',')

                            flag = False

                            for calldata in calldatavars:
                                if calldata in eqRV:
                                    for x in eqRV:
                                        # print(x)
                                        if x != calldata and x != '0':
                                            flag = True
                                            eqRV1 = x
                                            break
                                else:
                                    continue

                            if flag:
                                if eqRV1 in sloadvars:
                                    Mloc1 = Msplit1[9][Msplit1[9].find('(') + 1:Msplit1[9].find(')')]
                                    Pdv = 'SHA3(msg.sender,' + Mloc1 + ')'
                                    # PC.append(('whitelist', f, Pdv))
                                    return Mloc1

            # PC5
            if list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'GT', 'JUMPI'] or \
                list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'LT', 'JUMPI'] or \
                list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'SGT', 'JUMPI'] or \
                list(targetOp) == ['MSTORE', 'MSTORE', 'SHA3', 'CALLER', 'MSTORE', 'MSTORE', 'SHA3', 'SLOAD', 'SLT', 'JUMPI']:
                mstore0 = targetblock[targetblock['option'] == 'MSTORE'].iloc[2]
                Msplit0 = re.split(r'(?:[, : \s])', mstore0['3IR'])
                ltemp0 = Msplit0[9].find('(')  # MSTORE 第二项

                if ltemp0 < 0:
                    Mloc0 = Msplit0[9]
                    # MSTORE 与 CALLER 有关 (另一项应为CALLDATALOAD)
                    if Mloc0 in callervars:
                        mstore1 = targetblock[targetblock['option'] == 'MSTORE'].iloc[1]
                        Msplit1 = re.split(r'(?:[, : \s])', mstore1['3IR'])
                        ltemp1 = Msplit1[9].find('(')
                        if 'GT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'GT']
                        if 'LT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'LT']
                        if 'SGT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'SGT']
                        if 'SLT' in targetOp:
                            eq = targetblock[targetblock['option'] == 'SLT']

                        sload = targetblock[targetblock['option'] == 'SLOAD']

                        if ltemp1 > -1:
                            # print(Msplit[9])
                            sloadvar = sload.iloc[0]['leftvariable']
                            # SLOAD后进行的数值计算
                            sloadvars = samepropa(targetblock, sload.iloc[0].name, [sloadvar], sameop)
                            # print(sloadvars)

                            eqRV = eq.iloc[0]['rightvariable'].split(',')

                            flag = False

                            for calldata in calldatavars:
                                if calldata in eqRV:
                                    for x in eqRV:
                                        # print(x)
                                        if x != calldata and x != '0':
                                            flag = True
                                            eqRV1 = x
                                            break
                                else:
                                    continue
                            if flag:
                                if eqRV1 in sloadvars:
                                    Mloc1 = Msplit1[9][Msplit1[9].find('(') + 1:Msplit1[9].find(')')]
                                    Pdv = 'SHA3(msg.sender,' + Mloc1 + ')'
                                    # PC.append(('whitelist', f, Pdv))
                                    return Mloc1

    return ''


def readfrom(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()
    return [x[:-1] for x in lines]

# with open('../proxy2impl.json', 'r') as f:
#     proxy2impl = json.load(f)


no_exist = readfrom('../noexist.txt')
all_proxy_Sloc = set()
permission = []
nosstore = []
CallOp = ['DELEGATECALL']
cnt = 0

with open('../address.txt', 'r') as f:
    lines = f.readlines()
# for proxy in proxy2impl.keys():
for proxy in lines:
    # if proxy in no_exist:
    #     continue
    # impls = proxy2impl[proxy]
    path = '../USC_3IR_new/0x' + proxy.strip().lower() + '.csv'
    if not os.path.exists(path):
        continue
    # if not proxy.strip().lower() == "0062bb52986ebeae585898e63667d9d760ff75a0":
    #     continue
    proxydf = pd.read_csv(path)
    proxycall = proxydf[proxydf['option'].isin(CallOp)]
    if proxycall.empty:
        # nosstore.append(proxy.strip())
        continue
    imploc = ''
    for k in range(len(proxycall)):
        callvars = proxycall.iloc[k]['rightvariable'].split(',')
        callvar = callvars[2]
        # print(callvar)
        proxystorage = proxydf[proxydf['leftvariable'] == callvar].iloc[0]
        # storagevars = proxystorage['rightvariable'].split(',')
        # print(storagevars)
        storagedf = proxydf[proxydf['functionname'] == proxystorage['functionname']]
        sloadloc = storagedf[storagedf['option'] == 'SLOAD']
        if sloadloc.empty:
            # if proxy.strip() not in permission:
                # nosstore.append(proxy.strip())
            continue
        for i, row in sloadloc.iterrows():
            Msplit = re.split(r'(?:[, : \s])', row['3IR'])
            loc = Msplit[9][Msplit[9].find('(') + 1:Msplit[9].find(')')]
            # print(loc)
            sloadleft = row['leftvariable']
            sloadvars = []
            sloadvars.append(sloadleft)
            while 1:
                if callvar in sloadvars:
                    imploc = loc
                    break
                flag = 0
                for i, row in storagedf.iterrows():
                    if set(row['rightvariable'].split(',')) & set(sloadvars) and row['option'] in sameop and row['leftvariable'] not in sloadvars:
                        sloadvars.append(row['leftvariable'])
                        flag = 1
                if flag == 0:
                    break
            if imploc != '':
                break
            # if sloadleft == callvar or sloadleft in storagevars:
            #     imploc = loc
            #     break
        # 逻辑合约地址插槽
        # print(imploc)
        if imploc != '':
            break

    if imploc == '':
        nosstore.append(proxy.strip())
        continue
    flag = 0
    sstoredf = proxydf[proxydf['option'] == 'SSTORE']
    for i, row in sstoredf.iterrows():
        Msplit = re.split(r'(?:[, : \s])', row['3IR'])
        sstoreloc = Msplit[7][Msplit[7].find('(') + 1:Msplit[7].find(')')]
        # print(row['functionname'])
        funcs = set()
        funcs.add(row['functionname'])
        # 处理callprivate
        if row['functionname'][0] == '0':
            funcallpath = '../USC_tac_new/0x' + proxy.strip().lower() + '/out/IRFunctionCall.csv'
            funcalldf = pd.read_csv(funcallpath, header=None, delimiter='\t')
            funcalldf.columns = ['blockname', 'privatename']
            blockname = set(funcalldf[funcalldf['privatename'] == row['functionname']]['blockname'])
            # print(blockname)
            privatefuncs = set(proxydf[proxydf['blockname'].isin(blockname)]['functionname'])
            # print(privatefuncs)
            funcs = funcs.union(privatefuncs)
        # 排除fallback
        if 'fallback' in funcs:
            funcs.discard('fallback')
        # print(funcs)
        # print(sstoreloc)
        if sstoreloc == imploc:
            # flag = 1
            # permission.append(proxy.strip())
            # break
            # SSTORE 所在函数是否有access control
            sstorefuncdf = proxydf[proxydf['functionname'].isin(funcs)]
            cnt+=1
            # print(findPC(sstoredf))
            if findPC(sstorefuncdf) == []:
                permission.append(proxy.strip().lower())
                print(proxy.strip().lower())
                print(funcs)
                break
    # if flag == 0:
    #     nosstore.append(proxy.strip())

print(cnt)
with open('output/permission.txt', 'w') as f:
    json.dump(permission, f, indent=True)

with open('output/nosstore.txt', 'w') as f:
    json.dump(nosstore, f, indent=True)