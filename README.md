โปรแกรมแจ้งเตือนสำหรับขุดด้วย Trex บน Windows ครับ
1. Download file จาก https://github.com/moresore/MiningAlert/ แตก File บน windows ที่เปิด Trex ขุดอยู่
2. ขอ Line notify จาก https://notify-bot.line.me/th/
3. คัดลอก Line notify token ไปวางทับ คำว่า Line token บรรทัดแรก ใน config.txt
4. แก้ความถี่ในการแจ้งเตือนว่า Trex ยังทำงานอยู่ ค่าเติมตั้งไว้ 300 วินาที แล้ว Save
5. เปิดโปรแกรม MiningAlert จะมีข้อความเข้า Line ทันที แล้วเว้นระยะตามที่ตั้งค่าไว้ข้อ 4
6. ทำ shortcut วางใน start up
เป้าหมายโปรแกรมคือ คอยแจ้งว่า Trex ยังขุดอยู่ หากไฟดับหรือไม่ขุดก็จะไม่มีข้อความแจ้งเตือน อันนี้ยังไม่ได้ลอง ไม่อยากปิดเครื่องเพราะขุดอยู่ครับ
โปรแกรมพัฒนาด้วย Python 3 เขียนแยบเรียบง่าย อยากนำไปพัฒนาต่อ "ยินดีมากๆ" ครับ
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
ปล. ไว้มีโอกาสจะพัฒนาต่อนะครับ คงไม่ถึงขั้นแบบ HiveOS
