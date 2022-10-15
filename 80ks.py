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
        insertvalue('USDT',80000,'SELL','TinkoffNew', "B74",a)
       
        insertvalue('BTC',80000,'SELL','TinkoffNew', "C74",a)
       
        insertvalue('BUSD',80000,'SELL','TinkoffNew', "D74",a)
        
        insertvalue('BNB',80000,'SELL','TinkoffNew', "E74",a)
        insertvalue('ETH',80000,'SELL','TinkoffNew', "F74",a)
        insertvalue('RUB',80000,'SELL','TinkoffNew', "G74",a)
        insertvalue('SHIB',80000,'SELL','TinkoffNew', "H74",a)
        matrix.append(a)
        
        
        insertvalue('USDT',80000,'SELL','RosBankNew', "B75",b)
        insertvalue('BTC',80000,'SELL','RosBankNew', "C75",b)
        insertvalue('BUSD',80000,'SELL','RosBankNew', "D75",b)
        insertvalue('BNB',80000,'SELL','RosBankNew', "E75",b)
        insertvalue('ETH',80000,'SELL','RosBankNew', "F75",b)
        insertvalue('RUB',80000,'SELL','RosBankNew', "G75",b)
        insertvalue('SHIB',80000,'SELL','RosBankNew', "H75",b)
        matrix.append(b)
         
        
        insertvalue('USDT',80000,'SELL','QIWI', "B76",c)
        insertvalue('BTC',80000,'SELL','QIWI', "C76",c)
        insertvalue('BUSD',80000,'SELL','QIWI', "D76",c)
        insertvalue('BNB',80000,'SELL','QIWI', "E76",c)
        insertvalue('ETH',80000,'SELL','QIWI', "F76",c)
        insertvalue('RUB',80000,'SELL','QIWI', "G76",c)
        insertvalue('SHIB',80000,'SELL','QIWI', "H76",c)
        matrix.append(c)
        insertvalue('USDT',80000,'SELL','YandexMoneyNew', "B77",d)
        insertvalue('BTC',80000,'SELL','YandexMoneyNew', "C77",d)
        insertvalue('BUSD',80000,'SELL','YandexMoneyNew', "D771",d)
        insertvalue('BNB',80000,'SELL','YandexMoneyNew', "E77",d)
        insertvalue('ETH',80000,'SELL','YandexMoneyNew', "F77",d)
        insertvalue('RUB',80000,'SELL','YandexMoneyNew', "G77",d)
        insertvalue('SHIB',80000,'SELL','YandexMoneyNew', "H77",d)
        matrix.append(d)
        insertvalue('USDT',80000,'SELL','RaiffeisenBank', "B78",e)
        insertvalue('BTC',80000,'SELL','RaiffeisenBank', "C78",e)
        insertvalue('BUSD',80000,'SELL','RaiffeisenBank', "D78",e)
        insertvalue('BNB',80000,'SELL','RaiffeisenBank', "E78",e)
        insertvalue('ETH',80000,'SELL','RaiffeisenBank', "F78",e)
        insertvalue('RUB',80000,'SELL','RaiffeisenBank', "G78",e)
        insertvalue('SHIB',80000,'SELL','RaiffeisenBank', "H78",e)
        matrix.append(e)
        
        insertvalue('USDT',80000,'SELL','PostBankNew', "B79",f)
        insertvalue('BTC',80000,'SELL','PostBankNew', "C79",f)
        insertvalue('BUSD',80000,'SELL','PostBankNew', "D79",f)
        insertvalue('BNB',80000,'SELL','PostBankNew', "E79",f)
        insertvalue('ETH',80000,'SELL','PostBankNew', "F79",f)
        insertvalue('RUB',80000,'SELL','PostBankNew', "G79",f)
        insertvalue('SHIB',80000,'SELL','PostBankNew', "H79",f)
        matrix.append(f)
        
        
        insertvalue('USDT',80000,'SELL','MTSBank', "B80",g)
        insertvalue('BTC',80000,'SELL','MTSBank', "C80",g)
        insertvalue('BUSD',80000,'SELL','MTSBank', "D80",g)
        insertvalue('BNB',80000,'SELL','MTSBank', "E80",g)
        insertvalue('ETH',80000,'SELL','MTSBank', "F80",g)
        insertvalue('RUB',80000,'SELL','MTSBank', "G80",g)
        insertvalue('SHIB',80000,'SELL','MTSBank', "H80",g)
        matrix.append(g)
        
        insertvalue('USDT',80000,'SELL','HomeCreditBank', "B81",r)
        insertvalue('BTC',80000,'SELL','HomeCreditBank', "C81",r)
        insertvalue('BUSD',80000,'SELL','HomeCreditBank', "D81",r)
        insertvalue('BNB',80000,'SELL','HomeCreditBank', "E81",r)
        insertvalue('ETH',80000,'SELL','HomeCreditBank', "F81",r)
        insertvalue('RUB',80000,'SELL','HomeCreditBank', "G81",r)
        insertvalue('SHIB',80000,'SELL','HomeCreditBank', "H81",r)
        matrix.append(r)
        insertvalue('USDT',80000,'SELL','ABank', "B82",n)
        insertvalue('BTC',80000,'SELL','ABank', "C82",n)
        insertvalue('BUSD',80000,'SELL','ABank', "D82",n)
        insertvalue('BNB',80000,'SELL','ABank', "E82",n)
        insertvalue('ETH',80000,'SELL','ABank', "F82",n)
        insertvalue('RUB',80000,'SELL','ABank', "G82",n)
        insertvalue('SHIB',80000,'SELL','ABank', "H82",n)
        matrix.append(n)
        insertvalue('USDT',80000,'SELL','RUBfiatbalance', "B83",q)
        insertvalue('BTC',80000,'SELL','RUBfiatbalance', "C83",q)
        insertvalue('BUSD',80000,'SELL','RUBfiatbalance', "D83",q)
        insertvalue('BNB',80000,'SELL','RUBfiatbalance', "E83",q)
        insertvalue('ETH',80000,'SELL','RUBfiatbalance', "F83",q)
        insertvalue('RUB',80000,'SELL','RUBfiatbalance', "G83",q)
        insertvalue('SHIB',80000,'SELL','RUBfiatbalance', "H83",q)
        matrix.append(q)
        
        insertvalue('USDT',80000,'SELL','Payeer', "B84",l)
        insertvalue('BTC',80000,'SELL','Payeer', "C84",l)
        insertvalue('BUSD',80000,'SELL','Payeer', "D84",l)
        insertvalue('BNB',80000,'SELL','Payeer', "E84",l)
        insertvalue('ETH',80000,'SELL','Payeer', "F84",l)
        insertvalue('RUB',80000,'SELL','Payeer', "G84",l)
        insertvalue('SHIB',80000,'SELL','Payeer', "H84",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',80000,'SELL','Advcash', "B85",h)
        insertvalue('BTC',80000,'SELL','Advcash', "C85",h)
        insertvalue('BUSD',80000,'SELL','Advcash', "D85",h)
        insertvalue('BNB',80000,'SELL','Advcash', "E85",h)
        insertvalue('ETH',80000,'SELL','Advcash', "F85",h)
        insertvalue('RUB',80000,'SELL','Advcash', "G85",h)
        insertvalue('SHIB',80000,'SELL','Advcash', "H85",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('J74:P85', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass