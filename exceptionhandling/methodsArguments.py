def example_method(mandatory_parameter, default_parameter = 'default',
                   *args, **kwargs):
   #keyword argument is called 'kwargs' (key - value pairs)
   # *args allows to pass any number of arguments
   # f format ddoesnt work
    print(f"""mandatpara = {mandatory_parameter}
              deaf = {default_parameter}
                args = {args}
                kwargs = {kwargs}""")

#example_method(mandatory_parameter=15)
#example_method(25, 'some string')
#example_method(25, 'string_one', 'string 2', 'string 3')
#example_method(25, 'string_one', 'string 2', 'string 3', 'string 4')
#example_method(25, 'string_one', 'string 2', 'string 3',
               key1 = 'a', key2 = 'b')
example_list = [1,2,3]
#example_method(example_list[0],example_list[1],example_list[2])
#instead of above one
#example_method(*example_list)
example_dict = {'a':'1', 'b':'2'}
example_method(*example_list, **example_dict)