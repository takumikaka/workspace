# -*- coding: utf-8 -*-

'''
元音字母 有：a，e，i，o，u五个， 写一个函数，交换字符串的元音字符位置。
假设，一个字符串中只有二个不同的元音字符。
二个测试用例：
输入 apple 输出 eppla
输入machin 输出 michan
'''

list_vowel = ['a', 'e', 'i', 'o', 'u']
string = input("Input string:")
list_str = list(string)
list_pos = []
for i in range(len(list_vowel)):
    for j in range(len(list_str)):
        if list_vowel[i] == list_str[j]:
            list_pos.append(j)
print(list_pos)
list_str[list_pos[0]], list_str[list_pos[1]] = list_str[list_pos[1]], list_str[list_pos[0]]
print(list_str)
