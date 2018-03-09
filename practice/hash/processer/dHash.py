# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
from processer.open_xls import openXls
from processer.get_cwd import getCwd
#from open_xls import openXls

###########################################################################

# 缩小图片：收缩到9*8的大小，以便它有72的像素点
# 转化为灰度图：把缩放后的图片转化为256阶的灰度图
# 计算差异值：dHash算法工作在相邻像素之间，这样每行9个像素之间产生了8个不同的差异，一共8行，则产生了64个差异值
# 获得指纹：如果左边的像素比右边的更亮，则记录为1，否则为0
# 最后比对两张图片的指纹，获得汉明距离即可

###########################################################################

class class_dHash(object):

    def __init__(self):
        self.open_xls = openXls()
        self.get_cwd = getCwd()
        self.size = (9,8)
        self.part_pwd_two = 'resource/images/'

    def get_code(self, image, size):

        result = []
        x_size = size[0] - 1
        y_size = size[1]
        for x in range(0, x_size):
            for y in range(0, y_size):
                now_value = image.getpixel((x, y))
                next_value = image.getpixel((x+1, y))

                if next_value < now_value:
                    result.append(1)
                else:
                    result.append(0)

        return result

    def comp_code(self, code1, code2):

        num = 0
        for index in range(0, len(code1)):
            if code1[index] != code2[index]:
                num += 1
        return num


    def run(self):
        data = self.open_xls.run()
        part_pwd_one = self.get_cwd.run()
        pwd = part_pwd_one + self.part_pwd_two
        lst = []
        for i in range(0, len(data)):
            try:
                img1 = Image.open(pwd+'a{0}.jpg'.format(i+1))
                img2 = Image.open(pwd+'b{0}.jpg'.format(i+1))

                image1 = img1.resize(self.size).convert('L')
                code1 = self.get_code(image1, self.size)

                image2 = img2.resize(self.size).convert('L')
                code2 = self.get_code(image2, self.size)

                num = self.comp_code(code1, code2)
                print('第{0}个数:'.format(i+1), num)
                lst.append(num)
            except Exception as e:
                print(e)
        return lst

def main():
    action = class_dHash()
    action.run()

if __name__ == '__main__':
    main()
