
#open file/resource
try:
     #try business logic to read
     i = 1 #input from user
     j = 10/i
     values = [1, '2']
     sum(values)
except TypeError:
     print('TypeError')
     j = 10

except ZeroDivisionError:
     print('ZeroDivisionError')
     j = 0
else: #operation when next block does not throw exception
     print('Else')
finally:
     #close file here(else resource leakage will occure
     print('finally')

print(j)
print("End")