# -*- coding: utf-8 -*-

import os
import copy
import json
import sys
import time

class compareResources(object):

###########################################################
#获取pwd
    def __init__(self):
        self.list_one_image = []
        self.list_one_sheet = []
        self.list_two_image = []
        self.list_two_sheet = []
        self.new_list = []
        self.comp_list = []
        self.num_comb = 2


    # 获取工程路径
    def get_cwd(self):
        return os.getcwd()

    # 转为list
    def strTolist(self, str):
        return str.split('/')

    # list去空格及无用文件名
    def delUncode(self, lst):
        for i in lst:
            if '' == i or 'processers' == i:
                lst.remove(i)
        return lst

    def get_pwd(self):
        str_pwd = self.get_cwd()
        lst = self.strTolist(str_pwd)
        lst = self.delUncode(lst)
        pwd = '/' + '/'.join(lst) + '/'
        return pwd
###########################################################
#获取文件名列表
    def get_filelist(self):
        file_dir = self.get_pwd() + 'sources/files'
        for files in os.walk(file_dir):
            for file_list in files:
                pass
        file_list.remove('.DS_Store')
        return file_list
###########################################################
#将获取的文件名列表2，2组合
    def combine_list(self):
        n = 2     #代表两两组合
        one = [0] * self.num_comb
        def next_c(li = 0, ni = 0):
            if ni == self.num_comb:
                self.new_list.append(copy.copy(one))
                return
            for lj in range(li, len(self.get_filelist())):
                one[ni] = self.get_filelist()[lj]
                next_c(lj + 1, ni + 1)
        next_c()
        return self.new_list
#############################################################
#获取列表中每个子列表的第一和第二个数
    def get_childlist(self):
        for child_list in self.combine_list():
            #取得第一个文件json内容
            json_file_one = self.get_pwd() + 'sources/files/' + child_list[0]

            #读取json内容
            with open(json_file_one) as f:
                content = f.read()
                if content.startswith(u'\ufeff'):
                    content = content.encode('utf8')[3:].decode('utf8')
            data_one = json.loads(content)

            #从json数据中，获取resource资源
            for key in data_one:
                if key == 'resources':
                    value_resources_one = data_one['resources']

            #获取resources中指定内容image
            len_list = len(value_resources_one)
            for i in range(len_list):
                for key in value_resources_one[i]:
                    if key == 'type' and value_resources_one[i]['type'] == 'image':
                        self.list_one_image.append(value_resources_one[i]['name'])

            #获取resources中指定内容sheet
            for j in range(len_list):
                for key in value_resources_one[j]:
                    if 'subkeys' in value_resources_one[j]:
                        if key == 'type' and value_resources_one[j]['type'] == 'sheet':
                            self.list_one_sheet += value_resources_one[j]["subkeys"].split(',')

            #取得第二个文件json内容
            json_file_two = self.get_pwd() + 'sources/files/' + child_list[1]

            #读取json内容
            with open(json_file_two) as f:
                content = f.read()
                if content.startswith(u'\ufeff'):
                    content = content.encode('utf8')[3:].decode('utf8')
            data_two = json.loads(content)

            #从json数据中，获取resource资源
            for key in data_two:
                if key == 'resources':
                    value_resources_two = data_two['resources']

            #获取resources中指定内容image
            len_list = len(value_resources_two)
            for m in range(len_list):
                for key in value_resources_two[m]:
                    if key == 'type' and value_resources_two[m]['type'] == 'image':
                        self.list_two_image.append(value_resources_two[m]['name'])

            #获取resources中指定内容sheet
            for n in range(len_list):
                for key in value_resources_two[n]:
                    if 'subkeys' in value_resources_two[n]:
                        if key == 'type' and value_resources_two[n]['type'] == 'sheet':
                            self.list_two_sheet += value_resources_two[n]['subkeys'].split(',')


####################################################################################
#比较两个列中中共同的元素
            list_one = self.list_one_image + self.list_one_sheet
            list_two = self.list_two_image + self.list_two_sheet
            print("开始对比文件:{0}和{1}".format(child_list[0], child_list[1]))
            time.sleep(0.5)
            for list_i in list_one:
                for list_j in list_two:
                    if list_i == list_j:
                        self.comp_list.append(list_i)

###################################################################################
#保存文件
            file_name = self.get_pwd() + 'sources/txt/' + '[file1]' + child_list[0].split('.')[0] + '_' + '[file2]' + child_list[1].split('.')[0] + '.txt'
            with open(file_name,'a') as f:
                print('共有资源共: {0}个'.format(len(self.comp_list)))
                f.write(str(self.comp_list) + '\n')
                print('文件写入中....{0}和{1}'.format(child_list[0].split('.')[0], child_list[1].split('.')[0]))
                f.close()
                print('文件写入完毕...')
#####################################################################################
#写入完毕，列表重置
            self.list_one_image = []
            self.list_one_sheet = []
            self.list_two_image = []
            self.list_two_sheet = []
            self.comp_list = []

################################################################################################
def main():
    action = compareResources()
    action.get_childlist()

if __name__ == '__main__':
    main()
