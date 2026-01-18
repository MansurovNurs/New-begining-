# def check_password(password):
#
#         if len(password) <= 6:
#             print('wrong password! try again')
#             return False
#
#         if (any(i.isdigit() for i in password)
#             and any(not i.isalnum() for i in password)
#             and password[0].isupper()):
#             print('WELLCOME')
#             return False
#         else:
#             print('(Примеры надежного пароля: $PassW/12,\'3gT*5?O, k2-iR!49;'
#                   'Примеры недопустимого пароля: 12345, password, ???!!!)')
#             return True
#
# passw = check_password(input('Enter the password:'))
#

def nearest_number(numbers, target=0):
    nearest_num = numbers[0]
    for number in numbers:
        if abs(nearest_num - target) > abs(number - target):
            nearest_num = number
    return nearest_num
print('Enter the number:', end= ' ')
num = nearest_number([1, 2, 3, 67, 23, 34, 65, 33],
      int(input()))
print(num)