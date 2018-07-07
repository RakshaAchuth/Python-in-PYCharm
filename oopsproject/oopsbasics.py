class Motorbike:
#     pass
     def __init__(self, speed):
         #print(speed)
         self.speed = speed
         #print('motor bike instance created')

     def increase_speed(self, how_much):
         self.speed += how_much


     def decrease_speed(self, how_much):
         if(self.speed-how_much>0):
              self.speed -= how_much
         else:
             print('get a life')

honda = Motorbike(50)
ducati = Motorbike(100)
ducati_1 = Motorbike(200)
#
# honda.speed =  50
# ducati.speed=250
#
#
#
#
print(honda)
print(ducati)
#
#
print(honda.speed)
print(ducati.speed)


honda.increase_speed(150)
ducati.increase_speed(250)

print(honda.speed)
print(ducati.speed)


honda.decrease_speed(150)
ducati.decrease_speed(250)

print(honda.speed)
print(ducati.speed)


honda.speed += 150

#
# honda.speed = 150
#
# print(honda.speed)










