
#open file/resource
# just try and finally are allowed
# try eith except are allowed
#try eith else and finally are not allowed
# try is mandatory
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

except:
    print('other error')
    j = 5

else: #operation when next block does not throw exception
     print('Else')
finally:
     #close file here(else resource leakage will occure
     print('finally')

print(j)
print("End")