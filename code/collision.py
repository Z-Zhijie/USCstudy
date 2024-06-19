import pandas as pd
import json
import os
from accesscontrol import samepropa,findPC,getPC
with open('../proxy2impl.json','r') as f:
    proxy2impl = json.load(f)
collision = {}


def readfrom(fp):
    with open(fp,'r') as f:
        lines = f.readlines()
    return [x[:-1] for x in lines]

def readSloc(stmt):
    loc = '0'
    inter = stmt[stmt.find('SSTORE')+6:]
    inter = inter[:inter.find(',')].strip()
    if inter[-1] == ')':
        loc = inter[inter.find('(')+1:inter.find(')')]
    return loc
    
def getSloc(df):
    Sloc = set()
    for i,row in df.iterrows():
        Sloc.add(readSloc(row['3IR']))
    return Sloc

no_exist = readfrom('../noexist.txt')

collision = {}
permission = {}
StorageOp = ['SSTORE']

for proxy in proxy2impl.keys():
    # if proxy in no_exist:
    #     continue
    impls = proxy2impl[proxy]
    path = '../USC_3IR_new/0x'+proxy.lower()+'.csv'
    if not os.path.exists(path):
        continue
    proxydf = pd.read_csv(path)
    # break
    proxySSTORE = proxydf[proxydf['option'].isin(StorageOp)]
    # print('hhh')
    # proxy_Sloc = set(proxySSTORE['constant'])
    proxy_Sloc = getSloc(proxySSTORE)
    all_proxy_Sloc = set()
    all_proxy_Sloc = all_proxy_Sloc.union(proxy_Sloc)
    if all_proxy_Sloc == '0':
        continue
    proxy_coll = []
    proxy_permission = {}
    for impl in impls:
        # if impl in no_exist:
        #     continue
        path2 = '../USC_3IR_new/'+impl.lower()+'.csv'
        if not os.path.exists(path2):
            continue
        impldf = pd.read_csv(path2)
        implfunc = set()
        for i, row in impldf.iterrows():
            implfunc.add(row['functionname'])
        flag = 1
        for i, row in proxydf.iterrows():
            if row['functionname'] not in implfunc:
                flag = 0
        if flag == 1:
            continue
        implSSTORE = impldf[impldf['option'].isin(StorageOp)]
        
        # impl_Sloc = getSloc(implSSTORE)
        # set(implSSTORE['constant'])
        # candi_coll = proxy_Sloc.intersection(impl_Sloc)
        # for loc in candi_coll:
        #     if loc != '0':
        #         # print(proxy,loc)
        #         proxy_coll.append(loc)
        impl_coll = []
        flag = 0
        print(impl)
        for i,row in implSSTORE.iterrows():
            sstorefuncdf = proxydf[proxydf['functionname'] == row['functionname']]
            loc = readSloc(row['3IR'])
            if loc == '0':
                continue
            print("proxy")
            print(all_proxy_Sloc)
            print("loc")
            print(loc)
            print("PC")
            print(findPC(sstorefuncdf))
            if loc in all_proxy_Sloc and loc in findPC(sstorefuncdf):
                flag = 1
                impl_coll.append(loc)
        if impl_coll:
            proxy_permission[impl] = impl_coll
    if proxy_permission:
        permission[proxy] = proxy_permission

    # if proxy_coll:
    #     # proxy_coll=impl
    #     collision[proxy] = proxy_coll
# print('f',all_proxy_Sloc)
# with open('output/collision_new.json','w') as f:
#     json.dump(collision,f,indent=True)
with open('output/collision_permission.json','w') as f:
    json.dump(permission,f,indent=True)
