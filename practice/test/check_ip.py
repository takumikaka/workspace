# check ip?
str = '172.17.xxx.90'

def checkIp(str):
    check_list = str.split('.')

    if len(check_list) == 4:
        for num in check_list:
            if not num.isdigit() or not 0 <= int(num) <= 255:
                return False
        return True
    return False

def checkResult(Flag):
    if Flag:
        print('The str is IP address')
    else:
        print('The str is not IP address')

def main():
    Flag = checkIp(str)
    checkResult(Flag)

main()
