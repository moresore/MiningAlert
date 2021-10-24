import json
from urllib.request import urlopen
import requests
import time

def Line(msg,token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    r = requests.post(url, headers=headers, data = {'message':msg})

while(1):

    with open("config.txt", "r") as file:
        tokenL = file.readline(100)
        tokenL = tokenL[0:-1]
        TimDel = file.readline(100)


    url = "http://127.0.0.1:4067/summary"
    response = urlopen(url)
    data_json = json.loads(response.read())
    gpu = data_json['gpu_total']

    # find hashrate
    f = data_json["hashrate"]/1000000
    s = str(f) + " MH/s"

    # find worker name's
    pairs = data_json.items()
    for key, value in pairs:
        wks = str.find(str(value),"'worker':")
        if wks != -1 :
            wkf = str.find(str(value), "'}")
            wkc = str(value)[wks+11:wkf]

    msg = wkc + " running with " + str(gpu) + " GPUs " + s
    Line(msg,tokenL)
    print(msg)
    print("Waiting for next " + TimDel + " seconds")
    time.sleep(float(TimDel))

