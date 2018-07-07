# for i in range(1,11,2):
#     print(i, end=' ')


# for i in range(11,0,-1):
#     print(i, end=' ')



# i=5
# while i*i < 10:
#     print(i)
# print('done')


# for i in range(1,11):
#     if i==5:
#         break
#     print(i, end=' ')
# print('done')


# for i in range(1,11):
#     if i%2==0: #any non zero number is considered to be false
#         break
#     print(i, end=' ')
# print('done')

#
# for i in range(1,11):
#     if i%2==0: #any non zero number is considered to be false
#         continue
#     print(i, end=' ')
# print('done')


for i in range(1,11):
    if i%2!=0: #any non zero number is considered to be false
        continue
    print(i, end=' ')
print('done')