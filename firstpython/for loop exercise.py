
#check is prime
# def is_prime(number):
#     if(number<2):
#         return False #guard check or boundary check
#     for divisor in range(2,number):
#         if number % divisor == 0:
#             return False
#     return True
#
# print (is_prime(7));

#sum of numbers up to n

# def sum_upto_n(number):
#     sum = 0
#     for i in range(1, number+1):
#         sum = sum + i
#     return sum
#
# print (sum_upto_n(6));
# print (sum_upto_n(10));


#sum of divisors
# def sumofdivisors(number):
#     if(number<2):
#          return 0 #guard check or boundary check
#     sum = 0
#     for divisor in range(1,number+1):
#          if number % divisor == 0:
#              sum = sum + divisor
#     return sum
#
# print (sumofdivisors(6));
# print (sumofdivisors(15))



#print a number triangle

def printtri(number):
    for j in range(1, number + 1):
        for i in range(1, j+1):
            print(i, end=' ')
        print()

printtri(6)