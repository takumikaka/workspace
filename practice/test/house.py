# -*- coding: utf-8 -*-

'''
们假设，在南站区域，一套双钥匙的精装修公寓，月租金在4500元/月，租金每年上涨5%，
总价是100万，首付50万，十年贷款50万，是基准利率上浮5%。
那么这套房子的总成本=总价+契税+利息
即100万+3万+15万左右=118万
而前15年的租金，按照每年投入54000元（4500X12），复利计算15年，总和达到122万左右，
说明这套公寓可以在前十五年收回成本，还是比较适宜投资的。
'''

class House(object):
    def __init__(self):
        self.totalPrice = 820000
        self.downpayment = 420000
        self.bankloan = 400000
        self.monthrent = 2500
        self.payment = 4400
        self.rise = 0.02
        self.deedtax = 0.03
        self.year = input('输入想要查看的年限:')

    def month_rise(self):
        if int(self.year) >= 3 and int(self.year) < 4:
            month_rise = self.monthrent
        elif int(self.year) >= 4:
            month_rise = self.monthrent*((1+self.rise)**int(self.year))
        else:
            month_rise = 0
        return int(month_rise)

    def total_monthrent(self):
        sum_total_monthrent = 0
        for i in range(int(self.year)):
            if i+1 >=3:
                sum_total_monthrent = sum_total_monthrent + self.month_rise()*12
            else:
                pass
        return sum_total_monthrent


    def run(self):
        house_cost = self.totalPrice
        print('购买房屋投入[合同上所标识]:{0}万'.format(house_cost/10000))
        deedtax = self.deedtax * self.totalPrice
        print('契税开支[3%契税]:{0}万'.format(deedtax/10000))
        total_cost = self.downpayment + self.payment * 120
        print('10年总投入[首付+银行还款]:{0}万'.format(total_cost/10000))
        month_rise = self.month_rise()
        print('第{0}年的月租金为[租金每年上涨2%]:{1}'.format(self.year, month_rise))
        if int(self.year) <= 10:
            bank_loan = self.payment - self.month_rise()
            print('第{0}年的月银行还款为:{1}'.format(self.year, bank_loan))
        else:
            print('第{0}年已还完银行贷款'.format(self.year))
        sum_total_monthrent = self.total_monthrent()
        print('截止第{0}年的租金总收入为:{1}万'.format(self.year, int(sum_total_monthrent/10000)))
        del_monthrent = total_cost - sum_total_monthrent
        if del_monthrent > 0:
            print('截止第{0}年的实际投入为[总投入-租金收益]:{1}万'.format(self.year, int(del_monthrent/10000)))
        else:
            print('截止第{0}年的预计收益[已还清购房的总投资]:{1}万'.format(self.year, abs(int(del_monthrent/10000))))

def main():
    action = House()
    action.run()

if __name__ == '__main__':
    main()
