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
        insertvalue('USDT',0,'SELL','TinkoffNew', "B4",a)
       
        insertvalue('BTC',0,'SELL','TinkoffNew', "C4",a)
       
        insertvalue('BUSD',0,'SELL','TinkoffNew', "D4",a)
        
        insertvalue('BNB',0,'SELL','TinkoffNew', "E4",a)
        insertvalue('ETH',0,'SELL','TinkoffNew', "F4",a)
        insertvalue('RUB',0,'SELL','TinkoffNew', "G4",a)
        insertvalue('SHIB',0,'SELL','TinkoffNew', "H4",a)
        matrix.append(a)
        
        
        insertvalue('USDT',0,'SELL','RosBankNew', "B5",b)
        insertvalue('BTC',0,'SELL','RosBankNew', "C5",b)
        insertvalue('BUSD',0,'SELL','RosBankNew', "D5",b)
        insertvalue('BNB',0,'SELL','RosBankNew', "E5",b)
        insertvalue('ETH',0,'SELL','RosBankNew', "F5",b)
        insertvalue('RUB',0,'SELL','RosBankNew', "G5",b)
        insertvalue('SHIB',0,'SELL','RosBankNew', "H5",b)
        matrix.append(b)
         
        
        insertvalue('USDT',0,'SELL','QIWI', "B6",c)
        insertvalue('BTC',0,'SELL','QIWI', "C6",c)
        insertvalue('BUSD',0,'SELL','QIWI', "D6",c)
        insertvalue('BNB',0,'SELL','QIWI', "E6",c)
        insertvalue('ETH',0,'SELL','QIWI', "F6",c)
        insertvalue('RUB',0,'SELL','QIWI', "G6",c)
        insertvalue('SHIB',0,'SELL','QIWI', "H6",c)
        matrix.append(c)
        insertvalue('USDT',0,'SELL','YandexMoneyNew', "B7",d)
        insertvalue('BTC',0,'SELL','YandexMoneyNew', "C7",d)
        insertvalue('BUSD',0,'SELL','YandexMoneyNew', "D7",d)
        insertvalue('BNB',0,'SELL','YandexMoneyNew', "E7",d)
        insertvalue('ETH',0,'SELL','YandexMoneyNew', "F7",d)
        insertvalue('RUB',0,'SELL','YandexMoneyNew', "G7",d)
        insertvalue('SHIB',0,'SELL','YandexMoneyNew', "H7",d)
        matrix.append(d)
        insertvalue('USDT',0,'SELL','RaiffeisenBank', "B8",e)
        insertvalue('BTC',0,'SELL','RaiffeisenBank', "C8",e)
        insertvalue('BUSD',0,'SELL','RaiffeisenBank', "D8",e)
        insertvalue('BNB',0,'SELL','RaiffeisenBank', "E8",e)
        insertvalue('ETH',0,'SELL','RaiffeisenBank', "F8",e)
        insertvalue('RUB',0,'SELL','RaiffeisenBank', "G8",e)
        insertvalue('SHIB',0,'SELL','RaiffeisenBank', "H8",e)
        matrix.append(e)
        
        insertvalue('USDT',0,'SELL','PostBankNew', "B9",f)
        insertvalue('BTC',0,'SELL','PostBankNew', "C9",f)
        insertvalue('BUSD',0,'SELL','PostBankNew', "D9",f)
        insertvalue('BNB',0,'SELL','PostBankNew', "E9",f)
        insertvalue('ETH',0,'SELL','PostBankNew', "F9",f)
        insertvalue('RUB',0,'SELL','PostBankNew', "G9",f)
        insertvalue('SHIB',0,'SELL','PostBankNew', "H9",f)
        matrix.append(f)
        
        
        insertvalue('USDT',0,'SELL','MTSBank', "B10",g)
        insertvalue('BTC',0,'SELL','MTSBank', "C10",g)
        insertvalue('BUSD',0,'SELL','MTSBank', "D10",g)
        insertvalue('BNB',0,'SELL','MTSBank', "E10",g)
        insertvalue('ETH',0,'SELL','MTSBank', "F10",g)
        insertvalue('RUB',0,'SELL','MTSBank', "G10",g)
        insertvalue('SHIB',0,'SELL','MTSBank', "H10",g)
        matrix.append(g)
        
        insertvalue('USDT',0,'SELL','HomeCreditBank', "B11",r)
        insertvalue('BTC',0,'SELL','HomeCreditBank', "C11",r)
        insertvalue('BUSD',0,'SELL','HomeCreditBank', "D11",r)
        insertvalue('BNB',0,'SELL','HomeCreditBank', "E11",r)
        insertvalue('ETH',0,'SELL','HomeCreditBank', "F11",r)
        insertvalue('RUB',0,'SELL','HomeCreditBank', "G11",r)
        insertvalue('SHIB',0,'SELL','HomeCreditBank', "H11",r)
        matrix.append(r)
        insertvalue('USDT',0,'SELL','ABank', "B12",n)
        insertvalue('BTC',0,'SELL','ABank', "C12",n)
        insertvalue('BUSD',0,'SELL','ABank', "D12",n)
        insertvalue('BNB',0,'SELL','ABank', "E12",n)
        insertvalue('ETH',0,'SELL','ABank', "F12",n)
        insertvalue('RUB',0,'SELL','ABank', "G12",n)
        insertvalue('SHIB',0,'SELL','ABank', "H12",n)
        matrix.append(n)
        insertvalue('USDT',0,'SELL','RUBfiatbalance', "B13",q)
        insertvalue('BTC',0,'SELL','RUBfiatbalance', "C13",q)
        insertvalue('BUSD',0,'SELL','RUBfiatbalance', "D13",q)
        insertvalue('BNB',0,'SELL','RUBfiatbalance', "E13",q)
        insertvalue('ETH',0,'SELL','RUBfiatbalance', "F13",q)
        insertvalue('RUB',0,'SELL','RUBfiatbalance', "G13",q)
        insertvalue('SHIB',0,'SELL','RUBfiatbalance', "H13",q)
        matrix.append(q)
        
        insertvalue('USDT',0,'SELL','Payeer', "B14",l)
        insertvalue('BTC',0,'SELL','Payeer', "C14",l)
        insertvalue('BUSD',0,'SELL','Payeer', "D14",l)
        insertvalue('BNB',0,'SELL','Payeer', "E14",l)
        insertvalue('ETH',0,'SELL','Payeer', "F14",l)
        insertvalue('RUB',0,'SELL','Payeer', "G14",l)
        insertvalue('SHIB',0,'SELL','Payeer', "H14",l)
        matrix.append(l)
        
        
        
        insertvalue('USDT',0,'SELL','Advcash', "B15",h)
        insertvalue('BTC',0,'SELL','Advcash', "C15",h)
        insertvalue('BUSD',0,'SELL','Advcash', "D15",h)
        insertvalue('BNB',0,'SELL','Advcash', "E15",h)
        insertvalue('ETH',0,'SELL','Advcash', "F15",h)
        insertvalue('RUB',0,'SELL','Advcash', "G15",h)
        insertvalue('SHIB',0,'SELL','Advcash', "H15",h)
        matrix.append(h)
        
        
        
        
        
        wks1.update_values('J4:P15', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(10)
    pass