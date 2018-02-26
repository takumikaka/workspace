# -*- coding: utf-8 -*-

# Practice one
# 写一个函数，输入 lst = [1, 1, 3, 4, 4, 1]，返回值为[1,3,4,1]
# 需求是：如果后一个数字与前一个数字相同，则只保留一个数

'''
lst = [1, 1, 3, 4, 4, 1]
new_lst = []
print('原始列表:', lst)
for i in range(len(lst)-1):
    a = lst.pop(0)
    print('移除pop(0)....a={0}, lst={1}'.format(a, lst))
    if a == lst[0]:
        if a in new_lst:
            print('元素已在new_lst中，删除...')
        else:
            print('如果移除数同第一位相同...a={0}, lst={1}'.format(a, lst))
            new_lst.append(a)
            print('插入new_lst中的元素及new_lst...a={0}, new_lst={1}'.format(a, new_lst))
    else:
        new_lst.append(lst[0])
        print('如果移除数同第一位不同...lst[0]={0}, new_lst={1}'.format(lst[0], new_lst))
print(new_lst)


# Practice two
# 有一个json文件：
# {"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]}, "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}}
# 现在要写一个函数search，当给search函数传入‘金字塔’的 时候，函数打印出奴隶社会.非洲.古埃及文明.金字塔，当给search函数传入美洲的时候，打印出“不存在的关键字：美洲“

dit = {"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]},
        "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"],
        "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}}
print('原始字典为:', dit)
input_str = input('Input String:')
lst_key = []
lst_value = []
for key, value in dit.items():
    #print('字典中的key:', key)
    for key_i, value_i in dit[key].items():
        #print('value中的key:{0}\nvalue中的value:{1}'.format(key_i, value_i))
        lst_key.append(key_i)
        for key_j, value_j in dit[key][key_i].items():
            #print('子value中的key:{0}\n子value中的value:{1}'.format(key_j, value_j))
            #print(value_j[0])
            for i in range(len(value_j)):
                lst_value.append(value_j[i])
                if input_str == str(value_j[i]):
                    print('{0}.{1}.{2}.{3}'.format(key, key_i, key_j, value_j[i]))
                else:
                    pass
if input_str in lst_key or input_str in lst_value:
    pass
else:
    print('不存在的关键字:{0}'.format(input_str))


# 第三题：返回乒乓序列的第n个元素
# 乒乓序列从1开始计数，始终向上计数或倒数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和第28个要素。
# 1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
# 实现一个返回乒乓序列第n个元素的函数乒乓。

#input_num = int(input('输入任意整数:'))
def pingpong(n):
    changeone = 1
    outnum = 0
    for i in range(1, n + 1):
        outnum = outnum + changeone
        if i % 7 ==0 or i % 10 == 7 :
            changeone = changeone * -1
        print(outnum)

a = pingpong(20)

'''

def foo():
    print('foo')

def bar(func):
    func()

bar(foo)
