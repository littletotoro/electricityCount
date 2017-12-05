import urllib.parse;


import requests;

logUrl = 'http://172.27.2.95:8899/query/Default.aspx'
request = requests.session()
parms = {
    'submitDirectEventConfig':'{"config":{"extraParams":{"rid":"17310"}}}',
    'hid_bui_id':'015',
    'hid_bui_name':'15幢',
    'hid_floor_id':'003',
    'hid_floor_name':'第3层',
    'hid_r_id':'17310',
    'hid_room_name':'325房间',
    '__EVENTTARGET':'ct104',
    '__EVENTARGUMENT':'-|public|RoomQuery'
}
headers = {
    #'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5',
    #'Connection':'keep-alive',
    #'Content-Length':'302',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #'DNT':'1',
    #'Host':'172.27.2.95:8899',
    #'Origin':'http://172.27.2.95:8899',
    #'Referer':'http://172.27.2.95:8899/query/Default.aspx',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    #'X-Ext-Net':'delta=true',
    'X-Requested-With':'XMLHttpRequest'
}
request.headers.update(headers)
str1 = 'submitDirectEventConfig=%7B%22config%22%3A%7B%22extraParams%22%3A%7B%22rid%22%3A%2217310%22%7D%7D%7D&hid_bui_id=015&hid_bui_name=15%E5%B9%A2&hid_floor_id=003&hid_floor_name=%E7%AC%AC3%E5%B1%82&hid_r_id=17310&hid_room_name=325%E6%88%BF%E9%97%B4&__EVENTTARGET=ctl04&__EVENTARGUMENT=-%7Cpublic%7CRoomQuery'
req = request.post(logUrl,data=urllib.parse.urlencode(parms),headers=headers)
print(req.status_code)
print(req.content.decode('utf-8'))
print(req.history)
#print(req.text)
#print(urllib.parse.urlencode(parms))
