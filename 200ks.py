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
        insertvalue('USDT',200000,'SELL','TinkoffNew', "B102",a)
       
        insertvalue('BTC',200000,'SELL','TinkoffNew', "C102",a)
       
        insertvalue('BUSD',200000,'SELL','TinkoffNew', "D102",a)
        
        insertvalue('BNB',200000,'SELL','TinkoffNew', "E102",a)
        insertvalue('ETH',200000,'SELL','TinkoffNew', "F102",a)
        insertvalue('RUB',200000,'SELL','TinkoffNew', "G102",a)
        insertvalue('SHIB',200000,'SELL','TinkoffNew', "H102",a)
        matrix.append(a)
        
        
        insertvalue('USDT',200000,'SELL','RosBankNew', "B103",b)
        insertvalue('BTC',200000,'SELL','RosBankNew', "C103",b)
        insertvalue('BUSD',200000,'SELL','RosBankNew', "D103",b)
        insertvalue('BNB',200000,'SELL','RosBankNew', "E103",b)
        insertvalue('ETH',200000,'SELL','RosBankNew', "F103",b)
        insertvalue('RUB',200000,'SELL','RosBankNew', "G103",b)
        insertvalue('SHIB',200000,'SELL','RosBankNew', "H103",b)
        matrix.append(b)
         
        
        insertvalue('USDT',200000,'SELL','QIWI', "B104",c)
        insertvalue('BTC',200000,'SELL','QIWI', "C104",c)
        insertvalue('BUSD',200000,'SELL','QIWI', "D104",c)
        insertvalue('BNB',200000,'SELL','QIWI', "E104",c)
        insertvalue('ETH',200000,'SELL','QIWI', "F104",c)
        insertvalue('RUB',200000,'SELL','QIWI', "G104",c)
        insertvalue('SHIB',200000,'SELL','QIWI', "H104",c)
        matrix.append(c)
        insertvalue('USDT',200000,'SELL','YandexMoneyNew', "B105",d)
        insertvalue('BTC',200000,'SELL','YandexMoneyNew', "C105",d)
        insertvalue('BUSD',200000,'SELL','YandexMoneyNew', "D1051",d)
        insertvalue('BNB',200000,'SELL','YandexMoneyNew', "E105",d)
        insertvalue('ETH',200000,'SELL','YandexMoneyNew', "F105",d)
        insertvalue('RUB',200000,'SELL','YandexMoneyNew', "G105",d)
        insertvalue('SHIB',200000,'SELL','YandexMoneyNew', "H105",d)
        matrix.append(d)
        insertvalue('USDT',200000,'SELL','RaiffeisenBank', "B106",e)
        insertvalue('BTC',200000,'SELL','RaiffeisenBank', "C106",e)
        insertvalue('BUSD',200000,'SELL','RaiffeisenBank', "D106",e)
        insertvalue('BNB',200000,'SELL','RaiffeisenBank', "E106",e)
        insertvalue('ETH',200000,'SELL','RaiffeisenBank', "F106",e)
        insertvalue('RUB',200000,'SELL','RaiffeisenBank', "G106",e)
        insertvalue('SHIB',200000,'SELL','RaiffeisenBank', "H106",e)
        matrix.append(e)
        
        insertvalue('USDT',200000,'SELL','PostBankNew', "B107",f)
        insertvalue('BTC',200000,'SELL','PostBankNew', "C107",f)
        insertvalue('BUSD',200000,'SELL','PostBankNew', "D107",f)
        insertvalue('BNB',200000,'SELL','PostBankNew', "E107",f)
        insertvalue('ETH',200000,'SELL','PostBankNew', "F107",f)
        insertvalue('RUB',200000,'SELL','PostBankNew', "G107",f)
        insertvalue('SHIB',200000,'SELL','PostBankNew', "H107",f)
        matrix.append(f)
        
        
        insertvalue('USDT',200000,'SELL','MTSBank', "B108",g)
        insertvalue('BTC',200000,'SELL','MTSBank', "C108",g)
        insertvalue('BUSD',200000,'SELL','MTSBank', "D108",g)
        insertvalue('BNB',200000,'SELL','MTSBank', "E108",g)
        insertvalue('ETH',200000,'SELL','MTSBank', "F108",g)
        insertvalue('RUB',200000,'SELL','MTSBank', "G108",g)
        insertvalue('SHIB',200000,'SELL','MTSBank', "H108",g)
        matrix.append(g)
        
        insertvalue('USDT',200000,'SELL','HomeCreditBank', "B109",r)
        insertvalue('BTC',200000,'SELL','HomeCreditBank', "C109",r)
        insertvalue('BUSD',200000,'SELL','HomeCreditBank', "D109",r)
        insertvalue('BNB',200000,'SELL','HomeCreditBank', "E109",r)
        insertvalue('ETH',200000,'SELL','HomeCreditBank', "F109",r)
        insertvalue('RUB',200000,'SELL','HomeCreditBank', "G109",r)
        insertvalue('SHIB',200000,'SELL','HomeCreditBank', "H109",r)
        matrix.append(r)
        insertvalue('USDT',200000,'SELL','ABank', "B110",n)
        insertvalue('BTC',200000,'SELL','ABank', "C110",n)
        insertvalue('BUSD',200000,'SELL','ABank', "D110",n)
        insertvalue('BNB',200000,'SELL','ABank', "E110",n)
        insertvalue('ETH',200000,'SELL','ABank', "F110",n)
        insertvalue('RUB',200000,'SELL','ABank', "G110",n)
        insertvalue('SHIB',200000,'SELL','ABank', "H110",n)
        matrix.append(n)
        insertvalue('USDT',200000,'SELL','RUBfiatbalance', "B111",q)
        insertvalue('BTC',200000,'SELL','RUBfiatbalance', "C111",q)
        insertvalue('BUSD',200000,'SELL','RUBfiatbalance', "D111",q)
        insertvalue('BNB',200000,'SELL','RUBfiatbalance', "E111",q)
        insertvalue('ETH',200000,'SELL','RUBfiatbalance', "F111",q)
        insertvalue('RUB',200000,'SELL','RUBfiatbalance', "G111",q)
        insertvalue('SHIB',200000,'SELL','RUBfiatbalance', "H111",q)
        matrix.append(q)
        
        insertvalue('USDT',200000,'SELL','Payeer', "B112",l)
        insertvalue('BTC',200000,'SELL','Payeer', "C112",l)
        insertvalue('BUSD',200000,'SELL','Payeer', "D112",l)
        insertvalue('BNB',200000,'SELL','Payeer', "E112",l)
        insertvalue('ETH',200000,'SELL','Payeer', "F112",l)
        insertvalue('RUB',200000,'SELL','Payeer', "G112",l)
        insertvalue('SHIB',200000,'SELL','Payeer', "H112",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',200000,'SELL','Advcash', "B113",h)
        insertvalue('BTC',200000,'SELL','Advcash', "C113",h)
        insertvalue('BUSD',200000,'SELL','Advcash', "D113",h)
        insertvalue('BNB',200000,'SELL','Advcash', "E113",h)
        insertvalue('ETH',200000,'SELL','Advcash', "F113",h)
        insertvalue('RUB',200000,'SELL','Advcash', "G113",h)
        insertvalue('SHIB',200000,'SELL','Advcash', "H113",h)
        matrix.append(h)
        
        
        
        
        wks1.update_values('J102:P113', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(10)
    pass