# -*- coding: utf-8 -*-


from wxpy import *
from processer.tuling import Tuling
import config
import random

class Robot(Bot):
    def __init__(self):
        # 方便服务器二维码扫描
        #Bot.__init__(self, cache_path=True, console_qr=-2)
        # 调试使用，直接生成图片
        Bot.__init__(self, cache_path=True)
        self.enable_puid('./cache/admin_puid.pkl')
        self.admin = self.get_admin()
        self.tuling = Tuling()

        self.wr = False

        self.lunch = ['面', '米线', '套餐']

        # 纯文本信息
        self.FRIEND_TEXT = {
                            '指令': "\n".join(config.USER_CODE),
        }

        self.ADMIN_TEXT = {
                            '权限': "\n".join(config.ADMIN_CODE),
        }

        # 函数信息
        self.FUNC_CODE_NO_PARAM = {
                                    'lunch': self.get_lunch,
                                    'wrk': self.set_wrk,
                                    'wrg': self.set_wrg,
        }

        self.FUNC_CODE_PARAM = {
                                'logout': self.ai_logout,
        }

        # 指令分为有参数，无参数，有参数like，无参数like
        self.friend_no_param = set(['lunch', ])
        self.friend_param = set([])

        self.admin_no_param = self.friend_no_param | set(['wrk', 'wrg',])
        self.admin_param = self.friend_param | set(['logout'])

    def get_admin(self):
        users = self.search(config.ADMIN_NAME)
        puid = self.friends().search(config.ADMIN_NAME)[0].puid
        admin = None
        for v in users:
            if v.puid == puid:
                admin = v
        return admin

    # 将文字信息函数分离出来，这样可以通过指令集合来区分不同的人，避免拟合

    # 设置lunch
    def get_lunch(self):
        return random.choice(self.lunch)

    def set_wrk(self):
        self.wr = True
        return '开启勿扰模式...'

    def set_wrg(self):
        self.wr = False
        return '关闭勿扰模式...'

    def ai_logout(self, msg):
        msg.reply_msg('AI Logout...')
        self.logout()

    # 文本信息，处理函数
    def friend_msg_process(self, msg, tuling = True):
        msg_rec = msg.text

        # 判定文本信息指令
        # dict.get() 获取key
        if self.FRIEND_TEXT.get(msg_rec) is not None:
            return self.FRIEND_TEXT.get(msg_rec)

        if msg_rec in self.friend_no_param:
            return self.FUNC_CODE_NO_PARAM.get(msg_rec)()

        if tuling:
            return self.tuling.get_msg(msg.text)

    def admin_msg_process(self, msg, tuling = True):
        msg_rec = msg.text

        # dict.get() 获取key
        if self.FRIEND_TEXT.get(msg_rec) is not None:
            return self.FRIEND_TEXT.get(msg_rec)

        if self.ADMIN_TEXT.get(msg_rec) is not None:
            return self.ADMIN_TEXT.get(msg_rec)

        # 判断是否是无参数指令命令
        if msg_rec in self.admin_no_param:
            return self.FUNC_CODE_NO_PARAM.get(msg_rec)()

        # 判断是否是有参数指令命令
        if msg_rec in self.admin_param:
            return self.FUNC_CODE_PARAM.get(msg_rec)(msg)

        if self.wr:
            return config.WR_MSG

        # 调用图灵
        if tuling:
            return self.tuling.get_msg(msg.text)

    # 后注册的配置具有更高的优先级
    def member_fun(self):

        @self.register(Friend, TEXT)
        def text_processer(msg):

            if msg.sender == self.admin:
                ans = self.admin_msg_process(msg)
                if ans is not None:
                    return ans

            if self.wr:
                return config.WR_MSG
            else:
                return self.friend_msg_process(msg)
