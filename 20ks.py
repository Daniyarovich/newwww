import pygsheets
import numpy as np
import requests
import sys 
import time
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('ТЗ на таблицу')
wks1 = sh.worksheet_by_title("Binance-RUB")
def newmain():
    a= []
    b= []
    c= []
    d= []
    e= []
    f= []
    g= []
    r=[]
    n=[]
    q=[]
    l=[]
    h=[]
    
    # update the sheet with array
    matrix = [] 
    # share the sheet with your friend

    def insertvalue(asset, amount, tradetype, bank, row, sde):
        e = ''
        try:

            headers = {
            "Accept": "*/*",

            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com"
            }
            data = {
            "page": 1,
            "rows":1,
            "asset":asset,
            "tradeType":tradetype,
            "fiat":"RUB",
            "payTypes":[bank],
            "transAmount":amount
            }
            r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            sp = r.text
            allinfo = sp.split('"price"');
            someinfo = allinfo[1].split('"');
            line = someinfo[1].replace('.', ',')
            
            sde.append(line)
                 
        except:
            sde.append("Пусто")

    def SELLUAH():
        insertvalue('USDT',20000,'SELL','TinkoffNew', "B46",a)
       
        insertvalue('BTC',20000,'SELL','TinkoffNew', "C46",a)
       
        insertvalue('BUSD',20000,'SELL','TinkoffNew', "D46",a)
        
        insertvalue('BNB',20000,'SELL','TinkoffNew', "E46",a)
        insertvalue('ETH',20000,'SELL','TinkoffNew', "F46",a)
        insertvalue('RUB',20000,'SELL','TinkoffNew', "G46",a)
        insertvalue('SHIB',20000,'SELL','TinkoffNew', "H46",a)
        matrix.append(a)
        
        
        insertvalue('USDT',20000,'SELL','RosBankNew', "B47",b)
        insertvalue('BTC',20000,'SELL','RosBankNew', "C47",b)
        insertvalue('BUSD',20000,'SELL','RosBankNew', "D47",b)
        insertvalue('BNB',20000,'SELL','RosBankNew', "E47",b)
        insertvalue('ETH',20000,'SELL','RosBankNew', "F47",b)
        insertvalue('RUB',20000,'SELL','RosBankNew', "G47",b)
        insertvalue('SHIB',20000,'SELL','RosBankNew', "H47",b)
        matrix.append(b)
         
        
        insertvalue('USDT',20000,'SELL','QIWI', "B48",c)
        insertvalue('BTC',20000,'SELL','QIWI', "C48",c)
        insertvalue('BUSD',20000,'SELL','QIWI', "D48",c)
        insertvalue('BNB',20000,'SELL','QIWI', "E48",c)
        insertvalue('ETH',20000,'SELL','QIWI', "F48",c)
        insertvalue('RUB',20000,'SELL','QIWI', "G48",c)
        insertvalue('SHIB',20000,'SELL','QIWI', "H48",c)
        matrix.append(c)
        insertvalue('USDT',20000,'SELL','YandexMoneyNew', "B49",d)
        insertvalue('BTC',20000,'SELL','YandexMoneyNew', "C49",d)
        insertvalue('BUSD',20000,'SELL','YandexMoneyNew', "D491",d)
        insertvalue('BNB',20000,'SELL','YandexMoneyNew', "E49",d)
        insertvalue('ETH',20000,'SELL','YandexMoneyNew', "F49",d)
        insertvalue('RUB',20000,'SELL','YandexMoneyNew', "G49",d)
        insertvalue('SHIB',20000,'SELL','YandexMoneyNew', "H49",d)
        matrix.append(d)
        insertvalue('USDT',20000,'SELL','RaiffeisenBank', "B50",e)
        insertvalue('BTC',20000,'SELL','RaiffeisenBank', "C50",e)
        insertvalue('BUSD',20000,'SELL','RaiffeisenBank', "D50",e)
        insertvalue('BNB',20000,'SELL','RaiffeisenBank', "E50",e)
        insertvalue('ETH',20000,'SELL','RaiffeisenBank', "F50",e)
        insertvalue('RUB',20000,'SELL','RaiffeisenBank', "G50",e)
        insertvalue('SHIB',20000,'SELL','RaiffeisenBank', "H50",e)
        matrix.append(e)
        
        insertvalue('USDT',20000,'SELL','PostBankNew', "B51",f)
        insertvalue('BTC',20000,'SELL','PostBankNew', "C51",f)
        insertvalue('BUSD',20000,'SELL','PostBankNew', "D51",f)
        insertvalue('BNB',20000,'SELL','PostBankNew', "E51",f)
        insertvalue('ETH',20000,'SELL','PostBankNew', "F51",f)
        insertvalue('RUB',20000,'SELL','PostBankNew', "G51",f)
        insertvalue('SHIB',20000,'SELL','PostBankNew', "H51",f)
        matrix.append(f)
        
        
        insertvalue('USDT',20000,'SELL','MTSBank', "B52",g)
        insertvalue('BTC',20000,'SELL','MTSBank', "C52",g)
        insertvalue('BUSD',20000,'SELL','MTSBank', "D52",g)
        insertvalue('BNB',20000,'SELL','MTSBank', "E52",g)
        insertvalue('ETH',20000,'SELL','MTSBank', "F52",g)
        insertvalue('RUB',20000,'SELL','MTSBank', "G52",g)
        insertvalue('SHIB',20000,'SELL','MTSBank', "H52",g)
        matrix.append(g)
        
        insertvalue('USDT',20000,'SELL','HomeCreditBank', "B53",r)
        insertvalue('BTC',20000,'SELL','HomeCreditBank', "C53",r)
        insertvalue('BUSD',20000,'SELL','HomeCreditBank', "D53",r)
        insertvalue('BNB',20000,'SELL','HomeCreditBank', "E53",r)
        insertvalue('ETH',20000,'SELL','HomeCreditBank', "F53",r)
        insertvalue('RUB',20000,'SELL','HomeCreditBank', "G53",r)
        insertvalue('SHIB',20000,'SELL','HomeCreditBank', "H53",r)
        matrix.append(r)
        insertvalue('USDT',20000,'SELL','ABank', "B54",n)
        insertvalue('BTC',20000,'SELL','ABank', "C54",n)
        insertvalue('BUSD',20000,'SELL','ABank', "D54",n)
        insertvalue('BNB',20000,'SELL','ABank', "E54",n)
        insertvalue('ETH',20000,'SELL','ABank', "F54",n)
        insertvalue('RUB',20000,'SELL','ABank', "G54",n)
        insertvalue('SHIB',20000,'SELL','ABank', "H54",n)
        matrix.append(n)
        insertvalue('USDT',20000,'SELL','RUBfiatbalance', "B55",q)
        insertvalue('BTC',20000,'SELL','RUBfiatbalance', "C55",q)
        insertvalue('BUSD',20000,'SELL','RUBfiatbalance', "D55",q)
        insertvalue('BNB',20000,'SELL','RUBfiatbalance', "E55",q)
        insertvalue('ETH',20000,'SELL','RUBfiatbalance', "F55",q)
        insertvalue('RUB',20000,'SELL','RUBfiatbalance', "G55",q)
        insertvalue('SHIB',20000,'SELL','RUBfiatbalance', "H55",q)
        matrix.append(q)
        
        insertvalue('USDT',20000,'SELL','Payeer', "B56",l)
        insertvalue('BTC',20000,'SELL','Payeer', "C56",l)
        insertvalue('BUSD',20000,'SELL','Payeer', "D56",l)
        insertvalue('BNB',20000,'SELL','Payeer', "E56",l)
        insertvalue('ETH',20000,'SELL','Payeer', "F56",l)
        insertvalue('RUB',20000,'SELL','Payeer', "G56",l)
        insertvalue('SHIB',20000,'SELL','Payeer', "H56",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',20000,'SELL','Advcash', "B57",h)
        insertvalue('BTC',20000,'SELL','Advcash', "C57",h)
        insertvalue('BUSD',20000,'SELL','Advcash', "D57",h)
        insertvalue('BNB',20000,'SELL','Advcash', "E57",h)
        insertvalue('ETH',20000,'SELL','Advcash', "F57",h)
        insertvalue('RUB',20000,'SELL','Advcash', "G57",h)
        insertvalue('SHIB',20000,'SELL','Advcash', "H57",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('J46:P57', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass 