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
        insertvalue('USDT',50000,'SELL','TinkoffNew', "B60",a)
       
        insertvalue('BTC',50000,'SELL','TinkoffNew', "C60",a)
       
        insertvalue('BUSD',50000,'SELL','TinkoffNew', "D60",a)
        
        insertvalue('BNB',50000,'SELL','TinkoffNew', "E60",a)
        insertvalue('ETH',50000,'SELL','TinkoffNew', "F60",a)
        insertvalue('RUB',50000,'SELL','TinkoffNew', "G60",a)
        insertvalue('SHIB',50000,'SELL','TinkoffNew', "H60",a)
        matrix.append(a)
        
        
        insertvalue('USDT',50000,'SELL','RosBankNew', "B61",b)
        insertvalue('BTC',50000,'SELL','RosBankNew', "C61",b)
        insertvalue('BUSD',50000,'SELL','RosBankNew', "D61",b)
        insertvalue('BNB',50000,'SELL','RosBankNew', "E61",b)
        insertvalue('ETH',50000,'SELL','RosBankNew', "F61",b)
        insertvalue('RUB',50000,'SELL','RosBankNew', "G61",b)
        insertvalue('SHIB',50000,'SELL','RosBankNew', "H61",b)
        matrix.append(b)
         
        
        insertvalue('USDT',50000,'SELL','QIWI', "B62",c)
        insertvalue('BTC',50000,'SELL','QIWI', "C62",c)
        insertvalue('BUSD',50000,'SELL','QIWI', "D62",c)
        insertvalue('BNB',50000,'SELL','QIWI', "E62",c)
        insertvalue('ETH',50000,'SELL','QIWI', "F62",c)
        insertvalue('RUB',50000,'SELL','QIWI', "G62",c)
        insertvalue('SHIB',50000,'SELL','QIWI', "H62",c)
        matrix.append(c)
        insertvalue('USDT',50000,'SELL','YandexMoneyNew', "B63",d)
        insertvalue('BTC',50000,'SELL','YandexMoneyNew', "C63",d)
        insertvalue('BUSD',50000,'SELL','YandexMoneyNew', "D631",d)
        insertvalue('BNB',50000,'SELL','YandexMoneyNew', "E63",d)
        insertvalue('ETH',50000,'SELL','YandexMoneyNew', "F63",d)
        insertvalue('RUB',50000,'SELL','YandexMoneyNew', "G63",d)
        insertvalue('SHIB',50000,'SELL','YandexMoneyNew', "H63",d)
        matrix.append(d)
        insertvalue('USDT',50000,'SELL','RaiffeisenBank', "B64",e)
        insertvalue('BTC',50000,'SELL','RaiffeisenBank', "C64",e)
        insertvalue('BUSD',50000,'SELL','RaiffeisenBank', "D64",e)
        insertvalue('BNB',50000,'SELL','RaiffeisenBank', "E64",e)
        insertvalue('ETH',50000,'SELL','RaiffeisenBank', "F64",e)
        insertvalue('RUB',50000,'SELL','RaiffeisenBank', "G64",e)
        insertvalue('SHIB',50000,'SELL','RaiffeisenBank', "H64",e)
        matrix.append(e)
        
        insertvalue('USDT',50000,'SELL','PostBankNew', "B65",f)
        insertvalue('BTC',50000,'SELL','PostBankNew', "C65",f)
        insertvalue('BUSD',50000,'SELL','PostBankNew', "D65",f)
        insertvalue('BNB',50000,'SELL','PostBankNew', "E65",f)
        insertvalue('ETH',50000,'SELL','PostBankNew', "F65",f)
        insertvalue('RUB',50000,'SELL','PostBankNew', "G65",f)
        insertvalue('SHIB',50000,'SELL','PostBankNew', "H65",f)
        matrix.append(f)
        
        
        insertvalue('USDT',50000,'SELL','MTSBank', "B66",g)
        insertvalue('BTC',50000,'SELL','MTSBank', "C66",g)
        insertvalue('BUSD',50000,'SELL','MTSBank', "D66",g)
        insertvalue('BNB',50000,'SELL','MTSBank', "E66",g)
        insertvalue('ETH',50000,'SELL','MTSBank', "F66",g)
        insertvalue('RUB',50000,'SELL','MTSBank', "G66",g)
        insertvalue('SHIB',50000,'SELL','MTSBank', "H66",g)
        matrix.append(g)
        
        insertvalue('USDT',50000,'SELL','HomeCreditBank', "B67",r)
        insertvalue('BTC',50000,'SELL','HomeCreditBank', "C67",r)
        insertvalue('BUSD',50000,'SELL','HomeCreditBank', "D67",r)
        insertvalue('BNB',50000,'SELL','HomeCreditBank', "E67",r)
        insertvalue('ETH',50000,'SELL','HomeCreditBank', "F67",r)
        insertvalue('RUB',50000,'SELL','HomeCreditBank', "G67",r)
        insertvalue('SHIB',50000,'SELL','HomeCreditBank', "H67",r)
        matrix.append(r)
        insertvalue('USDT',50000,'SELL','ABank', "B68",n)
        insertvalue('BTC',50000,'SELL','ABank', "C68",n)
        insertvalue('BUSD',50000,'SELL','ABank', "D68",n)
        insertvalue('BNB',50000,'SELL','ABank', "E68",n)
        insertvalue('ETH',50000,'SELL','ABank', "F68",n)
        insertvalue('RUB',50000,'SELL','ABank', "G68",n)
        insertvalue('SHIB',50000,'SELL','ABank', "H68",n)
        matrix.append(n)
        insertvalue('USDT',50000,'SELL','RUBfiatbalance', "B69",q)
        insertvalue('BTC',50000,'SELL','RUBfiatbalance', "C69",q)
        insertvalue('BUSD',50000,'SELL','RUBfiatbalance', "D69",q)
        insertvalue('BNB',50000,'SELL','RUBfiatbalance', "E69",q)
        insertvalue('ETH',50000,'SELL','RUBfiatbalance', "F69",q)
        insertvalue('RUB',50000,'SELL','RUBfiatbalance', "G69",q)
        insertvalue('SHIB',50000,'SELL','RUBfiatbalance', "H69",q)
        matrix.append(q)
        
        insertvalue('USDT',50000,'SELL','Payeer', "B70",l)
        insertvalue('BTC',50000,'SELL','Payeer', "C70",l)
        insertvalue('BUSD',50000,'SELL','Payeer', "D70",l)
        insertvalue('BNB',50000,'SELL','Payeer', "E70",l)
        insertvalue('ETH',50000,'SELL','Payeer', "F70",l)
        insertvalue('RUB',50000,'SELL','Payeer', "G70",l)
        insertvalue('SHIB',50000,'SELL','Payeer', "H70",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',50000,'SELL','Advcash', "B71",h)
        insertvalue('BTC',50000,'SELL','Advcash', "C71",h)
        insertvalue('BUSD',50000,'SELL','Advcash', "D71",h)
        insertvalue('BNB',50000,'SELL','Advcash', "E71",h)
        insertvalue('ETH',50000,'SELL','Advcash', "F71",h)
        insertvalue('RUB',50000,'SELL','Advcash', "G71",h)
        insertvalue('SHIB',50000,'SELL','Advcash', "H71",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('J60:P71', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass
        
        
        
        
        
   