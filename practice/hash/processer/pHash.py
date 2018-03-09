# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import math

###################################################################

# 1.图片尺寸重定义
# 2.转为灰度图
# 3.计算灰度后，每个像素点的平均值‘
# 4.比较像素灰度值，遍历图片每一个像素，大于平均值记1，否则记0
# 5.得到信息指纹
# 6.根据汉明距离判断相似度

####################################################################

class pHash(object):
    def __init__(self):

        self.image1 = Image.open('./3.jpg')
        self.image2 = Image.open('./4.jpg')
        self.size = (32, 32)
        self.part_size = (8, 8)

    def get_code(self, List, middle):

        result = []
        for index in range(0, len(List)):
            if List[index] > middle:
                result.append('1')
            else:
                result.append('0')
        return result

    def comp_code(self, code1, code2):
        num = 0
        for index in range(0, len(code1)):
            if str(code1[index]) != str(code2[index]):
                num += 1
        return num

    def get_matrix(self, image):

        matrix = []
        size = image.size
        for height in range(0, size[1]):
            pixel = []
            for width in range(0, size[0]):
                pixel_value = image.getpixel((width, height))
                pixel.append(pixel_value)
            matrix.append(pixel)

        return matrix

    def get_coefficient(self, n):

        matrix = []
        PI = math.pi
        sqr = math.sqrt(1/n)
        value = []
        for i in range(0, n):
            value.append(sqr)
        matrix.append(value)

        for i in range(1, n):
            value = []
            for j in range(0, n):
                data = math.sqrt(2.0/n) * math.cos(i*PI*(j+0.5)/n)
                value.append(data)
            matrix.append(value)

        return matrix

    def get_transposing(self, matrix):

        new_matrix = []

        for i in range(0, len(matrix)):
            value_list = []
            for j in range(0, len(matrix[i])):
                value_list.append(matrix[i][j])
            new_matrix.append(value_list)

        return new_matrix

    def get_middle(self, List):
        li = List.copy()
        li.sort()
        value = 0
        if len(li)%2 == 0:
            index = int((len(li)/2)) - 1
            value = li[index]
        else:
            index = int((len(li)/2))
            value = (li[index]+li[index - 1])/2
        return value

    def get_mult(self, matrix1, matrix2):
        new_matrix = []

        for i in range(0, len(matrix1)):
            value_list = []
            for j in range(0, len(matrix1)):
                t = 0.0
                for k in range(0, len(matrix1)):
                    t += matrix1[i][k] * matrix2[k][j]
                value_list.append(t)
            new_matrix.append(value_list)

        return new_matrix

    def sub_matrix_to_list(self, DCT_matrix, part_size):

        w, h = part_size
        List = []
        for i in range(0, h):
            for j in range(0, w):
                List.append(DCT_matrix[i][j])

        return List

    def DCT(self, double_matrix):
        n = len(double_matrix)
        A = self.get_coefficient(n)
        AT = self.get_transposing(A)

        temp = self.get_mult(double_matrix, A)
        DCT_matrix = self.get_mult(temp, AT)

        return DCT_matrix

    def run(self):

        assert self.size[0] == self.size[1], "Size error..."
        assert self.part_size[0] == self.part_size[1], "Part_size error..."

        image1 = self.image1.resize(self.size).convert('L').filter(ImageFilter.BLUR)
        image1 = ImageOps.equalize(image1)
        matrix = self.get_matrix(image1)
        DCT_matrix = self.DCT(matrix)
        List = self.sub_matrix_to_list(DCT_matrix, self.part_size)
        middle = self.get_middle(List)
        code1 = self.get_code(List, middle)

        image2 = self.image2.resize(self.size).convert('L').filter(ImageFilter.BLUR)
        image2 = ImageOps.equalize(image2)
        matrix = self.get_matrix(image2)
        DCT_matrix = self.DCT(matrix)
        List = self.sub_matrix_to_list(DCT_matrix, self.part_size)
        middle = self.get_middle(List)
        code2 = self.get_code(List, middle)

        print(self.comp_code(code1, code2))



####################################################################

def main():
    action = pHash()
    action.run()

if __name__=='__main__':
    main()
