# -*- coding: utf-8 -*-


from wxpy import *
from processer.tuling import Tuling

class Robot(Bot):
    def __init__(self):
        Bot.__init__(self, True)
        self.tuling = Tuling()

    def friend_msg_process(self, msg, tuling = True):
        msg_rec = msg.text

        if tuling:
            return self.tuling.get_msg(msg.text)

    def send_msg_process(self):
        @self.register()
        def send_msg(msg):
            return self.friend_msg_process(msg)
