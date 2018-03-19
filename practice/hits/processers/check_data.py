# -*- coding: utf-8 -*-

import config

class checkData(object):
    def __init__(self):
        self.DATA_1_1 = '{"query":{"bool":{"must":[{"term":{"default.eid":"1-1"}},{"term":{"default.server":"game_node_localqa"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_1_5 = '{"query":{"bool":{"must":[{"term":{"default.eid":"1-5"}},{"term":{"default.server":"game_node_localqa"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_2_2 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-2"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"aggs":{}}'
        self.DATA_2_3 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-3"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":250,"sort":[],"aggs":{}}'
        self.DATA_2_4 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-4"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}} '
        self.DATA_2_5 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-5"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_2_6 = '{"query":{"bool":{"must":[{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_2_7 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-7"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_2_9 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-9"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"aggs":{}}'
        self.DATA_2_15 = '{"query":{"bool":{"must":[{"term":{"default.eid":"2-15"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_3_1 = '{"query":{"bool":{"must":[{"term":{"default.eid":"3-1"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_3_4 = '{"query":{"bool":{"must":[{"term":{"default.eid":"3-4"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.DATA_4_1 = '{"query":{"bool":{"must":[{"term":{"default.eid":"4-1"}},{"term":{"default.user_info.nickname":"001"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'
        self.eid = config.EID
        self.lst = config.LST

    def run(self):
        if self.eid in self.lst:
            if self.eid == '1-1':
                return self.DATA_1_1
            elif self.eid == '1-5':
                return self.DATA_1_5
            elif self.eid == '2-2':
                return self.DATA_2_2
            elif self.eid == '2-3':
                return self.DATA_2_3
            elif self.eid == '2-4':
                return self.DATA_2_4
            elif self.eid == '2-5':
                return self.DATA_2_5
            elif self.eid == '2-6':
                return self.DATA_2_6
            elif self.eid == '2-7':
                return self.DATA_2_7
            elif self.eid == '2-9':
                return self.DATA_2_9
            elif self.eid == '2-15':
                return self.DATA_2_15
            elif self.eid == '3-1':
                return self.DATA_3_1
            elif self.eid == '3-4':
                return self.DATA_3_4
            elif self.eid == '4-1':
                return self.DATA_4_1
        else:
            print('输入EID错误，请重试\n正确EID为:{0}'.format(self.lst))
            exit()
