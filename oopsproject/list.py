class Student:
      def __init__(self, name, marks):
           self.name = name
           self.marks = marks

      def get_number_ofmarks(self):
           return len(self.marks)

      def get_total_sum_of_marks(self):
           return sum(self.marks)

      def determine_average(self):
           return self.get_total_sum_of_marks()/self.get_number_ofmarks()

      def determine_min(self):
           return min(self.marks)

      def determine_max(self):
           return max(self.marks)

      def add_new_mark(self, new_mark):
           self.marks.append(new_mark)

      def remove_mark_at_index(self, index):
           del self.marks[index] # deletes marks at specific index



student = Student ("Raksha", [45,23,14,51])
number = student.get_number_ofmarks()


sumofmarks = student.get_total_sum_of_marks()
maximark = student.determine_max()
minmark = student.determine_min()
avgmark = student.determine_average()

student.add_new_mark(35)
student.remove_mark_at_index(2)


print(student.marks)
#print (f"""Student[num of marks - {number}]")
