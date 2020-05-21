# my_list_1 = [1,1,1,2,2,2,3,4]
# print(type(my_list_1))
# my_list_2 = [2,3,4]
# my_list_1 = set (my_list_1)
# my_list_2 = set (my_list_2)
# print(list(my_list_1-my_list_2))
# #######################
# my_list_final =[]
# for element in my_list_2:
#     if element not in my_list_1:
#         my_list_final.append (element)
# print(my_list_final)
##-------------------------
raw_date=(input('введите дату в формате dd.mm.yyyy: '))
#print(raw_date)
day=int(raw_date[:2])
month=int(raw_date[3:5])
year=raw_date[6:]
# print(day)
# print(month)
# print(year)
day_digits=['нулевятое','первое','второе','третье','четвертое','пятое','шестое','седьмое','восьмое','девятое','десятое','одиннадцатое','двенадцатое','тринадцатое','четырнадцатое','пятнадцатое','шестнадцатое','семнадцатое','весемнадцатое','девятнадцатое','двадцатое','двадцать первое','двадцать второе','двадцать третье','двадцать четвертое','двадцать пятое','двадцать шестое','двадцать седьмое','двадцать восьмое','двадцать девятое','тридцатое','тридцать первое']
month_digits=['ээбрь','января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
if day>0 and day<=31:
   day_word = day_digits [day]
   if month > 0 and month <= 12:
       month_word = month_digits[month]
       print('{} {} {} года'.format(day_word, month_word, year))
   else:
       print('не корректное значение месяца')
else:
    print('не корректное значение числа')
##-------------------------
my_list_1 = [2,19, 2, 5, 188,19,19, 12, 8, 3, 2, 12]
my_list_fin= []
# my_list_1 = list(set(my_list_1))
for element in my_list_1:
    if my_list_1.count(element) ==1:
        my_list_fin.append (element)



print(my_list_fin)


