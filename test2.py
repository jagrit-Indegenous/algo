import requests
import logging
import shutil

import http.client
http.client.HTTPConnection.debuglevel = 1

import datetime as dt

dt_India = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')

UTC_time = dt.datetime.utcnow().strftime('%d-%b-%y %H:%M:%S')

max_len = len(max(['UTC Time', 'Indian Time'], key=len))

print(f"{'UTC Time'   :<{max_len}} - {UTC_time}")
print(f"{'Indian Time':<{max_len}} - {Indian_time}")

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
headers = {
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'accept-encoding' : 'gzip, deflate, br',
'accept-language' : 'en-US,en;q=0.9'
}
    # response = requests.get(url, headers=headers).    

response = requests.get("https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY",headers=headers).content
print(response)
import datetime,pytz


for i in range (100000):
    if i%10 ==0:
        with open('nse_data.txt', 'w') as out_file:
            out_file.write(response.text)
            # shutil.copyfileobj(response.raw, out_file)

            print(f'The file was saved successfully {Indian_time}')