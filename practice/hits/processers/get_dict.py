# -*- coding: utf-8 -*-


from processers.get_value import getValue
import config

########################################################################

class getDict(object):
    def __init__(self):
        self.get_value = getValue()
        self.json_2_6 = config.JSON_2_6
        self.uid = config.UID
        self.eid= config.EID
        self.user_info = config.USER_INFO
        self.event_info = config.EVENT_INFO
        self.os = config.OS
        self.appid = config.APPID
        self.time = config.TIME
        self.type = config.TYPE
        self.channel = config.CHANNEL
        self.server = config.SERVER
        self.ext = config.EXT
        self.status = config.STATUS
        self.device_info = config.DEVICE_INFO
        self.game_id = config.GAME_ID
        self.role_id = config.ROLE_ID
        self.timestamp = config.TIMESTAMP
        self.log_type = config.LOG_TYPE

    def get_default(self, value):
        return value.get('default', {})

    def get_payload(self, value):
        return value.get('payload', {})

    def get_key(self, value, key):
        return value.get(key)

    def merg_dict(self, dict1, dict2):
        dictMerged = dict1.copy()
        dictMerged.update(dict2)
        return dictMerged

    def get_dict_html(self):
        dit_html = {}
        value = self.get_value.run()
        value = self.get_default(value)
        dit_html[self.uid] = self.get_key(value, self.uid)
        dit_html[self.os] = self.get_key(value, self.os)
        dit_html[self.role_id] = self.get_key(value, self.role_id)
        dit_html[self.status] = self.get_key(value, self.status)
        dit_html[self.appid] = self.get_key(value, self.appid)
        dit_html[self.eid] = self.get_key(value, self.eid)
        dit_html[self.device_info] = self.get_key(value, self.device_info)
        dit_html[self.ext] = self.get_key(value, self.ext)
        dit_html[self.timestamp] = self.get_key(value, self.timestamp)
        dit_html[self.time] = self.get_key(value, self.time)
        dit_html[self.game_id] = self.get_key(value, self.game_id)
        dit_html[self.server] = self.get_key(value, self.server)
        dit_html[self.channel] = self.get_key(value, self.channel)
        dit_html[self.log_type] = self.get_key(value, self.log_type)
        user_info = self.get_key(value, self.user_info)
        event_info = self.get_key(value, self.event_info)
        dit_html = self.merg_dict(dit_html, user_info)
        dit_html = self.merg_dict(dit_html, event_info)
        print(dit_html)
        return dit_html

    def get_dict_json(self):
        dit_json = {}
        value = self.json_2_6
        value_payload = self.get_payload(value)
        value_payload_ag = self.get_payload(value_payload)

        dit_json[self.appid] = self.get_key(value, self.appid)
        dit_json[self.time] = self.get_key(value_payload, self.time)
        dit_json[self.type] = self.get_key(value_payload, self.type)
        dit_json[self.channel] = self.get_key(value_payload_ag, self.channel)
        dit_json[self.server] = self.get_key(value_payload_ag, self.server)
        dit_json[self.uid] = self.get_key(value_payload_ag, self.uid)
        dit_json[self.eid] = self.get_key(value_payload_ag, self.eid)
        dit_json[self.ext] = self.get_key(value_payload_ag, self.ext)
        dit_json[self.status] = self.get_key(value_payload_ag, self.status)
        dit_json[self.os] = self.get_key(value_payload_ag, self.os)
        dit_json[self.device_info] = self.get_key(value_payload_ag, self.device_info)
        dit_json[self.game_id] = self.get_key(value_payload_ag, self.game_id)
        dit_json[self.role_id] = self.get_key(value_payload_ag, self.role_id)
        user_info = self.get_key(value_payload_ag, self.user_info)
        event_info = self.get_key(value_payload_ag, self.event_info)
        dit_json = self.merg_dict(dit_json, user_info)
        dit_json = self.merg_dict(dit_json, event_info)
        print(dit_json)
        return dit_json
