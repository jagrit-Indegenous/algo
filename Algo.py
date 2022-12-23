#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


Charting_Link = "https://chartink.com/screener/"
Charting_url= "https://chartink.com/screener/process"


# In[3]:


condition= '( {cash} ( monthly rsi( 14 ) > 60 and weekly rsi( 14 ) > 60 and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 and latest volume > 100000 ) ) '


# In[4]:


def Send_high():
    import requests
    import json

    url = "https://api.telegram.org/bot5820846301%3AAAHYbFAlHnqDfzbHFPZHdO1O1u6Y21UJzVg/sendMessage"

    payload = {
        "text": "Count is more than 40",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": "-1001691472772"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


# In[5]:


def Send_low():
    import requests
    import json

    url = "https://api.telegram.org/bot5921643018:AAHmiFfQudRMNZNl3sG19zafMZD0OdfWGgA/sendMessage"

    payload = {
        "text": "Count is less than 10",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": "-1001691472772"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


# In[6]:


import requests



# In[7]:
from datetime import datetime
import pytz

UTC = pytz.utc

IST = pytz.timezone('Asia/Kolkata')

datetime_ist = datetime.now(IST)

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# data = {
#   'scan_clause': '( {cash} ( monthly rsi( 14 ) > 60 and weekly rsi( 14 ) > 60 and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 and latest volume > 100000 ) ) '
# }
interval= 1

def periodic_work(interval):
    counter = 0
    while True:
        try:
            data = {
                  'scan_clause': '( {33492} ( [0] 15 minute close > latest vwap ) )'
                }

            with requests.Session() as s:
                r = s.get('https://chartink.com/screener/n-b-27')
                soup = bs(r.content, 'lxml')
                s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
                r = s.post('https://chartink.com/screener/process', data=data).json()
                #print(r.json())
                df = pd.DataFrame(r['data'])
#                 print(df)

                column = df["sr"]

                print("len",len(column))
                counter = counter + 1
                print(counter)
                datetime_ist = datetime.now(IST)
                print(datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))


                if(len(column)<=40):
    
                    Send_high()
                    interval= 1
                    print(df)
                if(len(column)>=10):

                    Send_low()
                    interval= 1
                    print(df)
                else:
                    interval=1

                #interval should be an integer, the number of seconds to wait


            time.sleep(interval)
        except Exception as e:
            print("ERROR : "+str(e))
        

periodic_work(1)  

        

