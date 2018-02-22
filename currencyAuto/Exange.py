
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlite3
from datetime import datetime 
df = pd.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
currency = df[0]
currency = currency.iloc[:,0:5] #取前5攔
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出'] #存成unicode

#將currency裡只取USD
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
currency['Date'] = datetime.now().strftime('%Y-%m-%d')
currency['Date'] = pd.to_datetime(currency['Date'])

with sqlite3.connect('C:\\Users\\Leo\\SQLITE\\currency.sqlite') as db: 
    currency.to_sql('currency', con = db, if_exists='append')   #將資料currency存入db裡,若資料表已經存在則將資料附加到最後

