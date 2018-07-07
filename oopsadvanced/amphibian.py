class landani:
      def __init__(self):
          super().__init__()
          self.walking_speed = 5

      def increase_walking_speed(self, how_much):
           self.walking_speed += how_much


class waterani:
      def __init__(self):
          super().__init__()
          self.swimming_speed = 10

      def increase_swimming_speed(self, how_much):
           self.swimming_speed += how_much


class amphibian(waterani,landani) :
      def __init__(self):
           super().__init__()


amphi = amphibian()
amphi.increase_swimming_speed(25)
amphi.increase_walking_speed(15)
print(amphi.swimming_speed)
print(amphi.walking_speed)