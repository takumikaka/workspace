# -*- coding: utf-8 -*-

#dit = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":" nat_sjyx_AySSih ","channel":"","server":"lite_game_001","uid":"","eid":"2-6","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","user_info":{"nickname":"001","win":"0","fail":"0","sex":"M","role":"-1"},"event_info":{"child_eid":"194294","ptime":"783","class1":"8","class2":"","type":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"}}}}

#dit = {"appid":"nat_sjyx_AySSih","payload":{"time":"2017-10-10 10:59:58","type":"behavior","payload":{"appid":" nat_sjyx_AySSih ","channel":"","server":"lite_game_001","uid":"","eid":"2-6","status":"","ext":{},"device_info":{},"os":"ANDROID","game_id":"549908695","role_id":"549908695","event_info":{"child_eid":"194294","ptime":"783","class1":"8","class2":"","type":"1","room_str":"194294_1507592929184","game_str":"194294_1507592929184_1507604207167"},"user_info":{"nickname":"001","win":"0","fail":"0","sex":"M","role":"-1"}}}}

#dit = {'user_info': {'nickname': '001', 'win': '0', 'fail': '0', 'sex': 'M', 'role': '-1'}}

class testValue(object):
    def __init__(self):
        self.dit = {'uid': '','test': {}, 'user_info': {'nickname': '001', 'win': '0', 'fail': '0', 'sex': 'M', 'role': '-1'}, 'event_info': {'child_eid': '991075', 'ptime': '211', 'class1': '199', 'class2': '', 'type': '1', 'room_str': '991075_1520584565779', 'game_str': '991075_1520584565779_1520584565779'}, 'os': 'ANDROID', 'role_id': '9999001', 'status': '', 'appid': 'nat_sjyx_AySSih', 'eid': '2-6', 'device_info': {}, 'ext': {}, 'timestamp': 1520584776000, 'time': '2018-03-09 16:39:36', 'game_id': '9999001', 'server': 'game_node_localqa', 'channel': '', 'log_type': 'behavior'}
        self.dic = {}

    def json_text(self, dit):
        dic = self.dic
        if isinstance(dit, dict):
            for key in dit:
                if isinstance(dit[key], dict):
                    #print('{0}:{1}'.format(key, dit[key]))
                    self.json_text(dit[key])
                    #dic[key] = dit[key]
                else:
                    dic[key] = dit[key]
                    #print('{0}:{1}'.format(key, dit[key]))
        else:
            print('数据不是字典类型...', dit)
            #dic[key] = dic_json[key]

        return dic

    def run(self):
        dic = self.json_text(self.dit)
        return dic


def main():
    action = testValue()
    action.run()

if __name__ == '__main__':
    main()
