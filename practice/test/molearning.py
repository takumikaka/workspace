# -*- coding: utf-8 -*-


import urllib
import urllib2
import time

for i in range(1, 10):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
            'Cookie': 'CNZZDATA5825297=cnzz_eid%3D1464184107-1519883585-null%26ntime%3D1519899799; UM_distinctid=161e0343b655fa-0ce6acbe4f15b18-1d451b27-fa000-161e0343b6656e; PHPSESSID=inh7hidn5lheh4qo51k3tvlcu5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-cn',
            }
    test_data = {"result":0,"learnTimeSec":59,"res":True,"msg":"成功"}
    #command_data = {"status":1,"message":"\u63d0\u4ea4\u6210\u529f","jumpUrl":"\/index.php?r=front\/plan\/show&pid=65"}

    test_data_urlencode = urllib.urlencode(test_data)

    req_url = 'http://molearning.eceibs20.com/index.php?r=front/learningTime/updateTime&type=studyLesson&tid=64&resId=5a31f00e1da45'
    #req_url = 'http://molearning.eceibs20.com/index.php?r=front/lessonComm/add'


    req = urllib2.Request(url = req_url, data = test_data_urlencode, headers = headers)

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print(i)
    print(res)
    print(req_url)
    time.sleep(5)
