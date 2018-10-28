#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 15:40:03
# @Author  : KlausQiu
# @QQ      : 375235513
# @github  : https://github.com/KlausQIU

from huobi.api.huobiServiceApi import *

if __name__ == '__main__':
    
    response=get_symbols()
    symbols=jsonpath.jsonpath(response,'$..symbol') 
    symbol='btcusdt'
    pool=0
    mysymbol=['btcusdt']
    activesymbol=[]
    while True:
        try:
            params = {"symbol": symbol}
            url = MARKET_URL + '/market/tickers'
            resp=http_get_request(url,params)
        except Exception as e:
            print (e)    
            time.sleep(20)
            continue

        tickers=resp['data']
        for ticker in tickers:
            if ticker['vol'] <4000:
                if ticker['vol'] not in activesymbol and ticker['vol'] in mysymbol:
                    mysymbol.remove(ticker['vol'])
                continue

            print (ticker['symbol']+' '+str(ticker['vol']))
            mysymbol.append(ticker['symbol'])

        mysymbol.append(activesymbol)
        sblist=[i for i in mysymbol]
        for symbol in sblist:
            try:
                resp=get_kline(symbol,'5min',size=150)
            except:
                print ('get kline error')
                continue
    
            response=json.dumps(resp)
            closeList=jsonpath.jsonpath(resp,'$..close')
            idList=jsonpath.jsonpath(resp,'$..id')
            now=closeList[1]
            prev=closeList[2]
            a=sum(closeList[1:11])/10
            b=sum(closeList[1:31])/30
            c=sum(closeList)/150
            print(str(now)+' '+str(a)[0:8]+' '+str(b)[0:8]+'   '+str(c)[0:8])
            print(closeList[0:10])
            num=0.0006

            if now>a and pool<2 and now>prev:
                try:
                    buy_result=send_order(1,'api',symbol,'buy-market',0)
                    pool = pool +1
                    print ('buy In '+buy_result['status'])
                    activesymbol.append(symbol)
                except:
                    print ('buy In error')

            elif now<a and symbol in activesymbol:
            
                try:
                    sell_result=send_order(num,'api',symbol,'sell-market',0)
                    while num>0 and sell_result['status'] != 'ok':
                        print (sell_result)
            
                        num = num -0.0001
                        numx,numy=str(num).split('.')
                        num=float(numx+'.'+numy[0:4])
                        sell_result=send_order(num,'api',symbol,'sell-market',0)
                    pool = 0
                    print ('sell out '+str(num))
                except:
                    print ('sell error'+sell_result['err-msg'])
                    if sell_result['err-code']=='account-frozen-balance-insufficient-error':
                            tmp=sell_result['err-msg'].spilt('`')
                            print (tmp)

            time.sleep(10)
        