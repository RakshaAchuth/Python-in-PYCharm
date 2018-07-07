#Error Handling Puzzles

#
# try:
#     i = 1 #input from user
#     j = 10/i
#     values = [1, '2']
#     sum(values)
# except TypeError:
#     print('TypeError')
#     j = 10
#
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#     j = 0
#
# print(j)
# print("End")

#
# try:
#     10/0
# except object:
#     print('TypeError')
#
# except ZeroDivisionError:
#     print('ZeroDivisionError')

#
# try:
#     10/0
# except BaseException:
#     print('BaseException')
#
# #except ZeroDivisionError:
#     print('End')


# try:
#     10/0
# except OverflowError:
#     print('OverflowError')
#
# #except ZeroDivisionError:
#     print('End')
#

# try:
#    # 10/0
#     sum([1,'1'])
# except (ZeroDivisionError, TypeError):
#     print('EXception')
#
# #except ZeroDivisionError:
#     print('End')


try:
   # 10/0
    sum([1,'1'])
except TypeError as error:
    print(error)

#except ZeroDivisionError:
    print('End')