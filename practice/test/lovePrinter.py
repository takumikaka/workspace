import time
words = raw_input("Please input the words you want to say!:")
for item in words.split():
    print(''.join('.'.join(item[x-y])))
