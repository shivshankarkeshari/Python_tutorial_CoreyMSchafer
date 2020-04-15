class Asd:
    count = 0
    '''Hello Here is doc of this class
        --> self represent class instance variable and cls_var represent class variable
        --> regular method, static method and class method
            regular method in a class automatically take the instance as the first argument(self)
            turn a regular method into a class method by adding decorator to the top @classmethod 
        --> static method don't pass anything automatically, they don't pass instance or cls, they behave
            just like regular function except we include them in our classes coz they have some logical 
            connection with the class
    '''
    cls_var = 1.04

    def __init__(self, name):
        self.name = name

        Asd.count += 1

    # regular method
    def change_to_unique_name(self):
        self.name = 'ok'

    @classmethod
    def cha(cls, val):
        cls.cls_var = val
        # Asd.cls_var = val
    # Asd.cha(23)

    def __call__(self, *args, **kwargs):
        print("ok")
        print("ok")

        self.func(self)


'''
b = Asd('shankar')
print(Asd.cls_var, b.name, b.cls_var)

# this will change cls var value for all data
Asd.cls_var = 3.4
print(Asd.cls_var)


# This will change only object variable value
b.cls_var = 3.3

a = Asd('shiv')
print(a.name, a.cls_var, b.cls_var)
'''

'''
b = Asd('shankar')
b.change_to_unique_name()
print(b.name)
print(b.__dict__)
print(b.__dir__)
print(Asd.__dict__)
# To print doc of class
print(Asd.__doc__)
print(Asd.__dir__)



'''
