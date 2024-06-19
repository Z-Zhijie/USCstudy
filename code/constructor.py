import pandas as pd
import json
import os

with open('../proxy2impl.json', 'r') as f:
    proxy2impl = json.load(f)


def readfrom(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()
    return [x[:-1] for x in lines]


def readSstore(stmt):
    loc = '0'
    inter = stmt[stmt.find('SSTORE') + 6:]
    inter = inter[:inter.find(',')].strip()
    if inter[-1] == ')':
        loc = inter[inter.find('(') + 1:inter.find(')')]
    return loc

def readSload(stmt):
    loc = '0'
    inter = stmt[stmt.find('SLOAD') + 6:]
    loc = inter[inter.find('(') + 1:inter.find(')')]
    return loc

def getSstore(df):
    Sloc = set()
    for i, row in df.iterrows():
        Sloc.add(readSstore(row['3IR']))
    return Sloc

def getSload(df):
    Sloc = set()
    for i, row in df.iterrows():
        Sloc.add(readSload(row['3IR']))
    return Sloc


no_exist = readfrom('../noexist.txt')
constructor = {}

for proxy in proxy2impl.keys():
    # if proxy.lower() != "13a246e429ff8e7cf7d371133b511e601bfeb824":
    #     continue
    # if proxy in no_exist:
    #     continue
    impls = proxy2impl[proxy]
    path = '../USC_3IR_new/0x' + proxy.lower() + '.csv'
    path1 = '../USC_3IR_creation/0x' + proxy.lower() + '.csv'
    if (not os.path.exists(path)) or (not os.path.exists(path1)):
        print("1")
        continue
    proxy_creation_df = pd.read_csv(path1)
    proxy_creation_SSTORE = proxy_creation_df[proxy_creation_df['option'] == 'SSTORE']
    proxy_creation_SSTORE_loc = getSstore(proxy_creation_SSTORE)
    all_proxy_creation_Sstore = set()
    all_proxy_creation_Sstore = all_proxy_creation_Sstore.union(proxy_creation_SSTORE_loc)
    
    proxydf = pd.read_csv(path)
    proxySLOAD = proxydf[proxydf['option'] == 'SLOAD']
    proxy_SLOAD_loc = getSload(proxySLOAD)
    all_proxy_Sload = set()
    all_proxy_Sload = all_proxy_Sload.union(proxy_SLOAD_loc)
    # print(all_proxy_Sloc)
    proxySSTORE = proxydf[proxydf['option'] == 'SSTORE']
    proxy_SSTORE_loc = getSstore(proxySSTORE)
    all_proxy_Sstore = all_proxy_creation_Sstore.union(proxy_SSTORE_loc)
    proxy_coll = {}
    for impl in impls:
        # if impl in no_exist:
        #     continue
        path2 = '../USC_3IR_creation/' + impl.lower() + '.csv'
        if not os.path.exists(path2):
            continue
        impldf = pd.read_csv(path2)
        implSSTORE = impldf[impldf['option'] == 'SSTORE']
        impl_Sloc = getSstore(implSSTORE)
        all_impl_Sloc = set()
        all_impl_Sloc = all_impl_Sloc.union(impl_Sloc)
        # print(all_impl_Sloc)
        # set(implSSTORE['constant'])
        flag = 0
        impl_coll = []
        print(all_proxy_Sstore)
        print(all_proxy_Sload)
        print(all_impl_Sloc)

        for loc in all_impl_Sloc:
            # if loc in all_proxy_Sload and loc not in all_proxy_Sstore:
            if loc in all_proxy_Sload and loc not in all_proxy_creation_Sstore:
            # if loc not in all_proxy_creation_Sstore:
                # print(proxy,loc)
                flag = 1
                impl_coll.append(loc)
        if flag:
            proxy_coll[impl] = impl_coll
    if proxy_coll:
        constructor[proxy] = proxy_coll

# print('f',all_proxy_Sloc)
with open('output/constructor.json', 'w') as f:
    json.dump(constructor, f, indent=True)
