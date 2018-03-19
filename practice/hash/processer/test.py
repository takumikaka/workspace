# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
from open_xls import openXls
from get_cwd import getCwd
#from open_xls import openXls

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

        img1 = Image.open(pwd+'a{0}.jpg'.format(1))
        img2 = Image.open(pwd+'b{0}.jpg'.format(1))

        image1 = img1.resize(self.size).convert('L')
        code1 = self.get_code(image1, self.size)

        image2 = img2.resize(self.size).convert('L')
        code2 = self.get_code(image2, self.size)

        num = self.comp_code(code1, code2)
        print(num)

        '''
        print(pwd)
        for i in range(0, len(data)):
            try:
                img1 = Image.open(pwd+'a{0}.jpg'.format(i+1))
                img2 = Image.open(pwd+'b{1}.jpg'.format(i+1))

                image1 = img1.resize(self.size).convert('L')
                code1 = self.get_code(image1, self.size)

                image2 = img2.resize(self.size).convert('L')
                code2 = self.get_code(image2, self.size)

                num = self.comp_code(code1, code2)
                print(num)
            except Exception as e:
                e = 'Error'
                print(e)
        '''

def main():
    action = class_dHash()
    action.run()

if __name__ == '__main__':
    main()
