# -*- coding: utf-8 -*-
import random

dict_data = [{'id': '955', 'type': '历史', 'des': '香港是哪一年回归祖国的？', 'option2': '1990', 'option3': '1998', 'option4': '2000', 'option1': '1997'}, {'id': '956', 'type': '文艺', 'des': '香港特别行政区的区花是？', 'option2': '月季花', 'option3': '玫瑰花', 'option4': '百合花', 'option1': '紫荆花'}, {'id': '957', 'type': '影视', 'des': '香港经典电影《胭脂扣》的导演是以下哪位？', 'option2': '吴宇森', 'option3': '陈凯歌', 'option4': '李安', 'option1': '关锦鹏'}, {'id': '958', 'type': '科技', 'des': '阿里巴巴集团成立探索人类科技未来的实验室的名字是？', 'option2': '太空站', 'option3': '未来空间', 'option4': '黑洞', 'option1': '达摩院'}, {'id': '959', 'type': '经济', 'des': '马云的投资人是谁？', 'option2': '马云老婆', 'option3': '红杉资本', 'option4': '林中华', 'option1': '孙正义'}, {'id': '960', 'type': '地理', 'des': '马六甲海峡属于哪个洲？', 'option2': '欧洲', 'option3': '美洲', 'option4': '非洲', 'option1': '亚洲'}, {'id': '961', 'type': '生活', 'des': '马卡龙是哪个国家的甜点？', 'option2': '英国', 'option3': '日本', 'option4': '中国', 'option1': '法国'}, {'id': '962', 'type': '历史', 'des': '马可波罗是在哪个朝代来到中国的？', 'option2': '明朝', 'option3': '汉朝', 'option4': '宋朝', 'option1': '元朝'}, {'id': '963', 'type': '文艺', 'des': '马头琴是我国哪个民族的拉弦乐器？', 'option2': '维吾尔族', 'option3': '壮族', 'option4': '回族', 'option1': '蒙古族'}, {'id': '964', 'type': '生活', 'des': '马奶酒是哪个民族的酒？', 'option2': '维吾尔族', 'option3': '壮族', 'option4': '回族', 'option1': '蒙古族'}, {'id': '965', 'type': '地理', 'des': '马来西亚的首都是？', 'option2': '新德里', 'option3': '曼谷', 'option4': '槟城', 'option1': '吉隆坡'}, {'id': '966', 'type': '生活', 'des': '马铃薯可供食用的部分是？', 'option2': '叶子', 'option3': '块根', 'option4': '球茎', 'option1': '块茎'}, {'id': '967', 'type': '体育', 'des': '高尔夫球比赛中，打一场完整比赛需要打满多少洞？', 'option2': '16洞', 'option3': '20洞', 'option4': '25洞', 'option1': '18洞'}, {'id': '968', 'type': '理化', 'des': '高猛酸钾加热生成的气体是？', 'option2': '氢气', 'option3': '氮气', 'option4': '氯气', 'option1': '氧气'}, {'id': '969', 'type': '游戏', 'des': '魔兽争霸3《冰封王座》中，阿尔萨斯使用的是什么武器？', 'option2': '冰之哀伤', 'option3': '火之哀伤', 'option4': '风之哀伤', 'option1': '霜之哀伤'}, {'id': '970', 'type': '生活', 'des': '鱼翅是哪种动物的鳍所制成的？', 'option2': '海豚', 'option3': '鲸鱼', 'option4': '剑鱼', 'option1': '鲨鱼'}, {'id': '971', 'type': '语文', 'des': '鲁迅原名叫什么?', 'option2': '周作人', 'option3': '周建人', 'option1': '周树人'}, {'id': '972', 'type': '语文', 'des': '鲁迅用什么动物比喻心甘情愿为人民服务，无私奉献的人？', 'option2': '马', 'option3': '蚂蚁', 'option4': '龙', 'option1': '牛'}, {'id': '973', 'type': '语文', 'des': '鲁迅的作品《药》中，华老栓为了给儿子治病给他带血的什么食物？', 'option2': '花卷', 'option3': '窝窝头', 'option4': '包子', 'option1': '馒头'}, {'id': '974', 'type': '生物', 'des': '鸟类「杜鹃」又名什么？', 'option2': '斑鸠', 'option3': '画眉', 'option4': '沉香', 'option1': '子规'}, {'id': '975', 'type': '理化', 'des': '鸡蛋壳遇到下列哪种物质会被腐蚀？', 'option2': '酱油', 'option3': '水', 'option4': '热水', 'option1': '醋'}, {'id': '976', 'type': '数学', 'des': '麦克斯韦方程组有几个？', 'option2': '3', 'option3': '2', 'option4': '1', 'option1': '4'}, {'id': '977', 'type': '娱乐', 'des': '鹿晗宣布与谁恋爱？', 'option2': '吴亦凡', 'option3': '范冰冰', 'option4': '唐艺昕', 'option1': '关晓彤'}, {'id': '978', 'type': '历史', 'des': '麻沸散是世界上最早的麻醉剂，他的发明者被后世尊称为「外科鼻祖」的是？', 'option2': '张仲景', 'option3': '李时珍', 'option4': '孙思邈', 'option1': '华佗'}, {'id': '979', 'type': '语文', 'des': '黄景仁《杂感》的诗句「百无一用是书生」的上一句是？', 'option2': '风蓬飘尽悲歌气', 'option3': '只知独夜不平鸣', 'option4': '仙佛茫茫两未成', 'option1': '十有九人堪白眼'}, {'id': '980', 'type': '历史', 'des': '黄梅戏发展壮大于哪里？', 'option2': '湖南', 'option3': '湖北', 'option1': '安徽'}, {'id': '981', 'type': '地理', 'des': '黄河一共流经我国几个省份？', 'option2': '8', 'option3': '7', 'option4': '10', 'option1': '9'}, {'id': '982', 'type': '地理', 'des': '黄河入海口附近所在的省级行政区是？', 'option2': '辽宁', 'option3': '吉林', 'option4': '浙江', 'option1': '山东'}, {'id': '983', 'type': '地理', 'des': '黄河注入了什么海？', 'option2': '黄海', 'option3': '南海', 'option4': '东海', 'option1': '渤海'}, {'id': '984', 'type': '地理', 'des': '黄鹤楼位于下列哪个城市？', 'option2': '西安', 'option3': '杭州', 'option4': '苏州', 'option1': '武汉'}, {'id': '985', 'type': '地理', 'des': '黑龙江哪个城市被称为「东方莫斯科」？', 'option2': '牡丹江市', 'option3': '齐齐哈尔', 'option4': '佳木斯', 'option1': '哈尔滨'}, {'id': '986', 'type': '地理', 'des': '龙泉青瓷产与哪个省?', 'option2': '安徽', 'option3': '江苏', 'option4': '四川', 'option1': '浙江'}, {'id': '987', 'type': '语文', 'des': '龚自珍是哪朝诗人？', 'option2': '明', 'option3': '唐', 'option4': '宋', 'option1': '清'}, {'id': '988', 'type': '文艺', 'des': '交响乐”通常有几个乐章？', 'option2': '三个', 'option3': '五个', 'option4': '六个', 'option1': '四个'}, {'id': '989', 'type': '文艺', 'des': '“电影”在哪一年诞生的？', 'option2': '1894年', 'option3': '1897年', 'option4': '1896年', 'option1': '1895年'}, {'id': '990', 'type': '地理', 'des': '世界上最大的群岛国家是？', 'option2': '马来西亚', 'option3': '芬兰', 'option1': '印度尼西亚'}, {'id': '991', 'type': '经济', 'des': '“沃尔沃”车原产地？', 'option2': '荷兰', 'option3': '德国', 'option4': '瑞士', 'option1': '瑞典'}, {'id': '992', 'type': '生物', 'des': '世界上眼睛最多的昆虫？', 'option2': '苍蝇', 'option3': '蚂蚁', 'option4': '蝴蝶', 'option1': '蜻蜓'}, {'id': '993', 'type': '文艺', 'des': '京剧起源于？', 'option2': '明朝', 'option3': '宋朝', 'option4': '唐朝', 'option1': '清朝'}, {'id': '994', 'type': '历史', 'des': '慈禧曾几次垂帘听政？', 'option2': '2', 'option3': '1', 'option4': '4', 'option1': '3'}, {'id': '995', 'type': '娱乐', 'des': '“愚人节”起源于？', 'option2': '英国', 'option3': '德国', 'option4': '美国', 'option1': '法国'}, {'id': '996', 'type': '体育', 'des': '羽毛球的羽毛材料？', 'option2': '鸡毛', 'option3': '鸭毛', 'option1': '鹅毛'}, {'id': '997', 'type': '科技', 'des': '电视机是谁发明的？', 'option2': '贝尔', 'option3': '爱迪生', 'option1': '贝尔德'}, {'id': '998', 'type': '娱乐', 'des': '“刘福荣“是谁的真名？', 'option2': '刘欢', 'option3': '刘德凯', 'option1': '刘德华'}, {'id': '999', 'type': '理化', 'des': '哪种糖纯度最高？', 'option2': '白糖', 'option3': '红糖', 'option4': '糖精', 'option1': '冰糖'}, {'id': '1000', 'type': '体育', 'des': '第一个举办奥运会的亚洲国家？', 'option2': '韩国', 'option3': '印度', 'option4': '马来西亚', 'option1': '日本'}]
len_dict = len(dict_data)
num = random.randint(955, 1000)
lst_one = ['A', 'B', 'C', 'D']
lst_two = ['A', 'B', 'C']
lst_answer_one = ['A', 'B', 'C', 'D']
lst_answer_two = ['A', 'B', 'C']
for i in range(len_dict):
    if dict_data[i]['id'] == str(num):
        print(dict_data[i]['des'])
        if len(dict_data[i]) == 6:
            lst_option = [dict_data[i]['option1'], dict_data[i]['option2'], dict_data[i]['option3']]
            random.shuffle(lst_option)
            dict_answer = {}
            for j in range(3):
                print("{0} : {1}".format(lst_two[j], lst_option[j]))
                dict_answer[lst_two[j]] = lst_option[j]
            print(dict_answer)
            input_num = input("输入你的选项: ")
            Flag = True
            while Flag:
                if input_num in lst_answer_two:
                    value_data = dict_answer[input_num]
                    for k, v in dict_data[i].items():
                        if v == value_data:
                            if k == 'option1':
                                print("真棒!")
                            else:
                                print("遗憾！错了")
                    Flag = False
                else:
                    input_num = input("输入你的选项: ")
                    Flag = True
        else:
            lst_option = [dict_data[i]['option1'], dict_data[i]['option2'], dict_data[i]['option3'], dict_data[i]['option4']]
            random.shuffle(lst_option)
            dict_answer = {}
            for j in range(4):
                print("{0} : {1}".format(lst_one[j], lst_option[j]))
                dict_answer[lst_one[j]] = lst_option[j]
            print(dict_answer)
            input_num = input("输入你的选项: ")
            Flag = True
            while Flag:
                if input_num in lst_answer_one:
                    value_data = dict_answer[input_num]
                    for k, v in dict_data[i].items():
                        if v == value_data:
                            if k == 'option1':
                                print("真棒!")
                            else:
                                print("遗憾！错了")
                    Flag = False
                else:
                    input_num = input("输入你的选项: ")
                    Flag = True
