#python can contain multiple classes
def method1():
    print('method')

class ClassA:
    def class_method_1(self):
        print('class_method_1 method_1')

#print(__name__)
if __name__ == '__main__':
     method1()
     ClassA().class_method_1()