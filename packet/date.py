from sys import argv

def _leap(num):
    check = False
    if (num[2] % 4 == 0 and num[2] % 100 != 0) or num[2] % 400 == 0:
        check = True
        return check
    return check
        

def year(date):
    month_max = [1,3,5,7,8,10,12]
    num = list(map(int, (date.split('.'))))
    check = _leap(num)
    if num[0] > 31 or num[0] < 0 or num[1] > 12 or num[1] < 1 or num[2] > 9999 or num[2] < 1:
        return False
    elif (num[1] == 2 and num[0] > 29) or (num[1] == 2 and num[0] > 28 and check == False):
        return False
    elif num[1] not in month_max and num[0] > 30:
        return False
    return True
    