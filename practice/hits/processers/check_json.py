# -*- coding: utf-8 -*-

import config

class checkJson(object):
    def __init__(self):
        self.JSON_1_1 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2016-09-19 11:59:59","type":"team","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","os":"ios","game_id":"","uid":"","role_id":"","eid":"1-1","status":"","device_info":{},"user_info":{},"event_info":{"child_eid":"13578","amount":"9","sex_ratio":"6:3","s_wait_time":"430","class1":"8","class2":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"},"ext":{}}}}
        self.JSON_1_5 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2016-09-19 11:59:59","type":"team","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","os":"ios","game_id":"","uid":"","role_id":"","eid":"1-5","status":"","device_info":{},"user_info":{},"event_info":{"child_eid":"13578","sex_ratio":"F:F","ptime":"430","class1":"8","class2":"1","room_str":"194294_1507592929184",},"ext":{}}}}
        self.JSON_2_2 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"2-2","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","ptime":"73","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_3 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"mm_lrs_xDKSGq","channel":"","server":"lite_game_001","uid":"","eid":"2-3","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","type":"1","status":"1","same_sex":"1","quit_step":"2","p_time":"321","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_4 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"2-4","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","win":"0","fail":"0","sex":"M","role":"-1"},"event_info":{"child_eid":"194294","class1":"8","class2":"","change_desk":"3","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_5 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"2-5","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","content":"老铁关注走一波","emoji":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_6 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":" nat_sjyx_AySSih ","channel":"","server":"lite_game_001","uid":"","eid":"2-6","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","win":"0","fail":"0","sex":"M","role":"-1"},"event_info":{"child_eid":"194294","ptime":"783","class1":"8","class2":"","type":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_7 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"mm_lrs_xDKSGq","channel":"","server":"lite_game_001","uid":"","eid":"2-7","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","type":"1","room_str":"194294_1507592929184","enter_type":"0","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_9 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"mm_lrs_xDKSGq","channel":"","server":"lite_game_001","uid":"","eid":"2-9","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","type":"1","step":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_2_15 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"mm_lrs_xDKSGq","channel":"","server":"lite_game_001","uid":"","eid":"2-15","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"194294","class1":"8","class2":"","room_str":"194294_1507592929184","enter_type":"0",}}}}
        self.JSON_3_1 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"3-1","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","win":"0","fail":"0","sex":"M","role":"-1"},"event_info":{"child_eid":"194294","class1":"8","class2":"","type":"DHdFJDFjDKFJD","count":"2","amount ":"200","from_to_sex":"1:1","is_start":"1","is_suc":"0","impression":"0","girl_first":"0","room":"18806","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_3_4 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"3-4","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","sex":"M"},"event_info":{"child_eid":"","class1":"8","class2":"","type":"1","invite_type":"1","ptime":"10","room":"18806","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.JSON_4_1 = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":"nat_sjyx_AySSih","channel":"","server":"lite_game_001","uid":"","eid":"4-1","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"烽沙承雨","win":"0","fail":"0","sex":"M","role":"-1"},"event_info":{"child_eid":"btn04827","class1":"8","class2":"","room":"18806","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}
        self.eid = config.EID

    def run(self):
        if self.eid == '1-1':
            return self.JSON_1_1
        elif self.eid == '1-5':
            return self.JSON_1_5
        elif self.eid == '2-2':
            return self.JSON_2_2
        elif self.eid == '2-3':
            return self.JSON_2_3
        elif self.eid == '2-4':
            return self.JSON_2_4
        elif self.eid == '2-5':
            return self.JSON_2_5
        elif self.eid == '2-6':
            return self.JSON_2_6
        elif self.eid == '2-7':
            return self.JSON_2_7
        elif self.eid == '2-9':
            return self.JSON_2_9
        elif self.eid == '2-15':
            return self.JSON_2_15
        elif self.eid == '3-1':
            return self.JSON_3_1
        elif self.eid == '3-4':
            return self.JSON_3_4
        elif self.eid == '4-1':
            return self.JSON_4_1
