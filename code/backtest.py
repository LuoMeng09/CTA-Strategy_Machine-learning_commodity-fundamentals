def BackTest(pred,p0,p1,c0,code,n,z=1,k=0,lev=1,alpha=1):
    '''
    Backtesting Functions:
    p0:open price
    P1: Settle Price_uses to calculate the rollover return
    c0: close price_calculates the daily floating profit and loss
    code: the code of the contract
    n: window time
    z: the number of days before the rollover
    lev: leverage
    alpha: stop loss
    '''
    m=len(pred) 
    capital=p0[0]/lev
    pricesB=np.full(m,np.nan)
    pricesS=np.full(m,np.nan)
    net=np.full((n),capital)         
    pos=0
    count=0
  
    for i in range(n,m):
        if count == 0: 
            p=p0
            c=c0
        if pos==1: 
            if pred[i]==1:                  
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]):
                    pos=1 
                    count=z 
                    capital=capital-pricesB[np.max(np.where(~np.isnan(pricesB)))]+(1-k)*p[i]
                    pricesB[i]=p[i]
                    capital=capital-k*pricesB[i] 
                    net=np.append(net,(capital-pricesB[i]+c[i]))
                else:                                       
                    if (pricesB[np.max(np.where(~np.isnan(pricesB)))]-c[i])>alpha*(pricesB[np.max(np.where(~np.isnan(pricesB)))]):
                        capital=capital-alpha*(pricesB[np.max(np.where(~np.isnan(pricesB)))])
                        net=np.append(net,capital)
                        pos=0                     
                    else:
                        net=np.append(net,(capital-pricesB[np.max(np.where(~np.isnan(pricesB)))]+c[i]))
                        pos=1
            elif pred[i]==0:               
                capital=capital-pricesB[np.max(np.where(~np.isnan(pricesB)))]+(1-k)*p[i]
                pos=0
                net=np.append(net,capital)
            elif pred[i]==-1:
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]):
                    pos=-1 
                    p=p1
                    count=z
                    capital=capital-pricesB[np.max(np.where(~np.isnan(pricesB)))]+(1-k)*p[i]
                    pricesS[i]=p[i]
                    capital=capital-k*pricesS[i]
                    net=np.append(net,capital+pricesS[i]-c[i])
                else:      
                    capital=capital-pricesB[np.max(np.where(~np.isnan(pricesB)))]+(1-k)*p[i]
                    pricesS[i]=p[i] 
                    capital=capital-k*pricesS[i]
                    if (-pricesS[i]+c[i])>alpha*pricesS[i]:
                        capital=capital-alpha*pricesS[i]
                        net=np.append(net,capital)
                        pos=0
                    else:
                        pos=-1
                        net=np.append(net,capital+pricesS[i]-c[i])
                    
        elif pos==-1:          
            if pred[i]==-1:                 
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]):
                    pos=-1
                    p=p1
                    count=z 
                    capital=capital+pricesS[np.max(np.where(~np.isnan(pricesS)))]-(1+k)*p[i]
                    pricesS[i]=p[i]
                    capital=capital-k*pricesS[i]
                    net=np.append(net,capital+pricesS[i]-c[i])
                else:                                      
                    if (-pricesS[np.max(np.where(~np.isnan(pricesS)))]+c[i])>alpha*(pricesS[np.max(np.where(~np.isnan(pricesS)))]):
                        capital=capital-alpha*(pricesS[np.max(np.where(~np.isnan(pricesS)))])
                        net=np.append(net,capital)
                        pos=0
                    else :
                        pos=-1
                        net=np.append(net,(capital+pricesS[np.max(np.where(~np.isnan(pricesS)))]-c[i]))
            elif pred[i]==0:               
                capital=capital+pricesS[np.max(np.where(~np.isnan(pricesS)))]-(1+k)*p[i]
                pos=0
                net=np.append(net,capital)
            elif pred[i]==1:
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]):
                    pos=1
                    p=p1
                    count=z
                    capital=capital+pricesS[np.max(np.where(~np.isnan(pricesS)))]-(1+k)*p[i]
                    pricesB[i]=p[i]
                    capital=capital-k*pricesB[i]
                    net=np.append(net,capital-pricesB[i]+c[i])
                else:                    
                    capital=capital+pricesS[np.max(np.where(~np.isnan(pricesS)))]-(1+k)*p[i]
                    pricesB[i]=p[i]
                    capital=capital-k*pricesB[i]
                    if (pricesB[i]-c[i])>alpha*pricesB[i]:
                        capital=capital-alpha*pricesB[i]
                        net=np.append(net,capital)
                        pos=0
                    else:
                        pos=1
                        net=np.append(net,capital-pricesB[i]+c[i])
        elif pos==0:          
            if pred[i]==1:      
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]):
                    pos=1
                    p=p1
                    count=z 
                    pricesB[i]=p[i]
                    capital=capital-k*pricesB[i]
                    net=np.append(net,capital-pricesB[i]+c[i])
                else: 
                    pricesB[i]=p[i]
                    capital=capital-k*pricesB[i]
                    if (pricesB[i]-c[i])>alpha*pricesB[i]:
                        capital=capital-alpha*pricesB[i]
                        net=np.append(net,capital)
                        pos=0
                    else:
                        pos=1
                        net=np.append(net,capital-pricesB[i]+c[i])
            elif pred[i]==-1:      
                if (count==0) and (i<=m-z-1) and (code[i]!=code[i+z]): 
                    pos=-1
                    p=p1
                    count=z                
                    pricesS[i]=p[i]
                    capital=capital-k*pricesS[i]
                    net=np.append(net,capital+pricesS[i]-c[i])
                else:                   
                    pricesS[i]=p[i]
                    capital=capital-k*pricesS[i]
                    if (-pricesS[i]+c[i])>alpha*pricesS[i]:
                        capital=capital-alpha*pricesS[i]
                        net=np.append(net,capital)
                        pos=0
                    else:
                        pos=-1
                        net=np.append(net,capital+pricesS[i]-c[i])
            else:
                net=np.append(net,capital)
        if count>0:count=count-1
    return net/net[0]