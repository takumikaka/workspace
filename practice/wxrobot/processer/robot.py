# -*- coding: utf-8 -*-


from wxpy import *
from processer.tuling import Tuling
import config
import random
from processer.restaurant import Restaurant
import time, datetime
import threading
import linecache

class Robot(Bot):
    def __init__(self):
        # 方便服务器二维码扫描
        #Bot.__init__(self, cache_path=True, console_qr=-2)
        # 调试使用，直接生成图片
        Bot.__init__(self, cache_path=True)
        self.enable_puid('./cache/admin_puid.pkl')
        self.admin = self.get_admin()
        self.tuling = Tuling()
        self.restaurant = Restaurant()

        self.wr = False

        # 获取笑话文件
        self.file_count = len(open('./files/laugh.txt', 'rU').readline())

        # 指定用户对象并尝试发送信息
        my_friend = self.friends().search(config.ADMIN_NAME)[0]
        self.logger = get_wechat_logger(my_friend)

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
                                    'joke': self.get_joke,
                                    # 以下是admin命令
                                    'wrk': self.set_wrk,
                                    'wrg': self.set_wrg,
                                    'st': self.get_status,
        }

        self.FUNC_CODE_PARAM = {
                                'logout': self.ai_logout,
        }

        # 指令分为有参数，无参数，有参数like，无参数like
        self.friend_no_param = set(['lunch', 'joke', ])
        self.friend_param = set([])

        self.admin_no_param = self.friend_no_param | set(['wrk', 'wrg', 'st', ])
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

    def get_status(self):
        ans = u'勿扰模式: ' + (u'开' if self.wr else u'关')
        ans += u'\n聊天程序: ' + (u'开' if self.tuling.get_swith() else u'关')
        return ans

    # 设置lunch
    def get_lunch(self):
        try:
            lst_lunch = self.restaurant.run()
            return random.choice(lst_lunch)
        except Exception as e:
            print(e)

    def get_joke(self):
        # 勿扰模式
        if self.wr:
            return config.WR_MSG

        at_msg = random.randrange(1, self.file_count, 1)
        msg = linecache.getline('./files/laugh.txt', at_msg).strip()
        return msg

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

        # 开关聊天程序
        if msg_rec in ['tlk', 'tlg']:
            return self.tuling.set_swith(True if msg_rec == 'tlk' else False)

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

    # 设置吃饭提醒时间
    def corn_lunch(self):
        SECONDS_PER_DAY = 24 * 60 * 60
        curTime = datetime.datetime.now()
        desTime = curTime.replace(hour=21, minute=43, second=1, microsecond=0)
        delta = (desTime - curTime).total_seconds()
        skipSeconds = (SECONDS_PER_DAY + delta) if delta < 0 else delta
        time.sleep(skipSeconds)
        self.logger.warning(random.choice(config.LUNCH_WARN))

    # 设定线程控制吃饭时间提醒
    def threads(self):
        t_lunch = threading.Thread(target=self.corn_lunch)
        t_lunch.setDaemon(True)
        t_lunch.start()
