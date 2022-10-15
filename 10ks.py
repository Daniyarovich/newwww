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
        insertvalue('USDT',10000,'SELL','TinkoffNew', "B32",a)
       
        insertvalue('BTC',10000,'SELL','TinkoffNew', "C32",a)
       
        insertvalue('BUSD',10000,'SELL','TinkoffNew', "D32",a)
        
        insertvalue('BNB',10000,'SELL','TinkoffNew', "E32",a)
        insertvalue('ETH',10000,'SELL','TinkoffNew', "F32",a)
        insertvalue('RUB',10000,'SELL','TinkoffNew', "G32",a)
        insertvalue('SHIB',10000,'SELL','TinkoffNew', "H32",a)
        matrix.append(a)
        
        
        insertvalue('USDT',10000,'SELL','RosBankNew', "B33",b)
        insertvalue('BTC',10000,'SELL','RosBankNew', "C33",b)
        insertvalue('BUSD',10000,'SELL','RosBankNew', "D33",b)
        insertvalue('BNB',10000,'SELL','RosBankNew', "E33",b)
        insertvalue('ETH',10000,'SELL','RosBankNew', "F33",b)
        insertvalue('RUB',10000,'SELL','RosBankNew', "G33",b)
        insertvalue('SHIB',10000,'SELL','RosBankNew', "H33",b)
        matrix.append(b)
         
        
        insertvalue('USDT',10000,'SELL','QIWI', "B34",c)
        insertvalue('BTC',10000,'SELL','QIWI', "C34",c)
        insertvalue('BUSD',10000,'SELL','QIWI', "D34",c)
        insertvalue('BNB',10000,'SELL','QIWI', "E34",c)
        insertvalue('ETH',10000,'SELL','QIWI', "F34",c)
        insertvalue('RUB',10000,'SELL','QIWI', "G34",c)
        insertvalue('SHIB',10000,'SELL','QIWI', "H34",c)
        matrix.append(c)
        insertvalue('USDT',10000,'SELL','YandexMoneyNew', "B35",d)
        insertvalue('BTC',10000,'SELL','YandexMoneyNew', "C35",d)
        insertvalue('BUSD',10000,'SELL','YandexMoneyNew', "D351",d)
        insertvalue('BNB',10000,'SELL','YandexMoneyNew', "E35",d)
        insertvalue('ETH',10000,'SELL','YandexMoneyNew', "F35",d)
        insertvalue('RUB',10000,'SELL','YandexMoneyNew', "G35",d)
        insertvalue('SHIB',10000,'SELL','YandexMoneyNew', "H35",d)
        matrix.append(d)
        insertvalue('USDT',10000,'SELL','RaiffeisenBank', "B36",e)
        insertvalue('BTC',10000,'SELL','RaiffeisenBank', "C36",e)
        insertvalue('BUSD',10000,'SELL','RaiffeisenBank', "D36",e)
        insertvalue('BNB',10000,'SELL','RaiffeisenBank', "E36",e)
        insertvalue('ETH',10000,'SELL','RaiffeisenBank', "F36",e)
        insertvalue('RUB',10000,'SELL','RaiffeisenBank', "G36",e)
        insertvalue('SHIB',10000,'SELL','RaiffeisenBank', "H36",e)
        matrix.append(e)
        
        insertvalue('USDT',10000,'SELL','PostBankNew', "B37",f)
        insertvalue('BTC',10000,'SELL','PostBankNew', "C37",f)
        insertvalue('BUSD',10000,'SELL','PostBankNew', "D37",f)
        insertvalue('BNB',10000,'SELL','PostBankNew', "E37",f)
        insertvalue('ETH',10000,'SELL','PostBankNew', "F37",f)
        insertvalue('RUB',10000,'SELL','PostBankNew', "G37",f)
        insertvalue('SHIB',10000,'SELL','PostBankNew', "H37",f)
        matrix.append(f)
        
        
        insertvalue('USDT',10000,'SELL','MTSBank', "B38",g)
        insertvalue('BTC',10000,'SELL','MTSBank', "C38",g)
        insertvalue('BUSD',10000,'SELL','MTSBank', "D38",g)
        insertvalue('BNB',10000,'SELL','MTSBank', "E38",g)
        insertvalue('ETH',10000,'SELL','MTSBank', "F38",g)
        insertvalue('RUB',10000,'SELL','MTSBank', "G38",g)
        insertvalue('SHIB',10000,'SELL','MTSBank', "H38",g)
        matrix.append(g)
        
        insertvalue('USDT',10000,'SELL','HomeCreditBank', "B39",r)
        insertvalue('BTC',10000,'SELL','HomeCreditBank', "C39",r)
        insertvalue('BUSD',10000,'SELL','HomeCreditBank', "D39",r)
        insertvalue('BNB',10000,'SELL','HomeCreditBank', "E39",r)
        insertvalue('ETH',10000,'SELL','HomeCreditBank', "F39",r)
        insertvalue('RUB',10000,'SELL','HomeCreditBank', "G39",r)
        insertvalue('SHIB',10000,'SELL','HomeCreditBank', "H39",r)
        matrix.append(r)
        insertvalue('USDT',10000,'SELL','ABank', "B40",n)
        insertvalue('BTC',10000,'SELL','ABank', "C40",n)
        insertvalue('BUSD',10000,'SELL','ABank', "D40",n)
        insertvalue('BNB',10000,'SELL','ABank', "E40",n)
        insertvalue('ETH',10000,'SELL','ABank', "F40",n)
        insertvalue('RUB',10000,'SELL','ABank', "G40",n)
        insertvalue('SHIB',10000,'SELL','ABank', "H40",n)
        matrix.append(n)
        insertvalue('USDT',10000,'SELL','RUBfiatbalance', "B41",q)
        insertvalue('BTC',10000,'SELL','RUBfiatbalance', "C41",q)
        insertvalue('BUSD',10000,'SELL','RUBfiatbalance', "D41",q)
        insertvalue('BNB',10000,'SELL','RUBfiatbalance', "E41",q)
        insertvalue('ETH',10000,'SELL','RUBfiatbalance', "F41",q)
        insertvalue('RUB',10000,'SELL','RUBfiatbalance', "G41",q)
        insertvalue('SHIB',10000,'SELL','RUBfiatbalance', "H41",q)
        matrix.append(q)
        
        insertvalue('USDT',10000,'SELL','Payeer', "B42",l)
        insertvalue('BTC',10000,'SELL','Payeer', "C42",l)
        insertvalue('BUSD',10000,'SELL','Payeer', "D42",l)
        insertvalue('BNB',10000,'SELL','Payeer', "E42",l)
        insertvalue('ETH',10000,'SELL','Payeer', "F42",l)
        insertvalue('RUB',10000,'SELL','Payeer', "G42",l)
        insertvalue('SHIB',10000,'SELL','Payeer', "H42",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',10000,'SELL','Advcash', "B43",h)
        insertvalue('BTC',10000,'SELL','Advcash', "C43",h)
        insertvalue('BUSD',10000,'SELL','Advcash', "D43",h)
        insertvalue('BNB',10000,'SELL','Advcash', "E43",h)
        insertvalue('ETH',10000,'SELL','Advcash', "F43",h)
        insertvalue('RUB',10000,'SELL','Advcash', "G43",h)
        insertvalue('SHIB',10000,'SELL','Advcash', "H43",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('J32:P43', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass