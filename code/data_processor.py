def Nameprocessing(data,direct='index'):
    '''name processing'''
    if direct=='index':
        name = []
        for i in data.index:
            name.append(i)
        name = list(map(lambda x: re.sub(u"\\(.*?\\)|\\:|\\（.*?\\）|" "|.1|.2","", \
                                     name[x]), [x for x in range(len(name))]))
        data.index = name
    else :
        name = []
        for i in data.columns:
            name.append(i)
        name = list(map(lambda x: re.sub(u"\\(.*?\\)|\\:|\\（.*?\\）|" "|.1|.2","", \
                                     name[x]), [x for x in range(len(name))]))
        data.columns = name
    return data


def ComparePercent(a, b, x):
    if x >= a:
        x = 1
    elif x <= b:
        x = -1
    else:
        x = 0
    return x

def DateSame(factor1,factor2):
    factor1 = factor1.loc[factor1.index.isin(factor2.index),:]
    factor2 = factor2.loc[factor2.index.isin(factor1.index),:]
    factor1 = factor1.loc[factor1.index.isin(factor2.index),:]
    factor2 = factor2.loc[factor2.index.isin(factor1.index),:]
    return factor1,factor2