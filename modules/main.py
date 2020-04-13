import module_1
from module_1 import variable_1, list_1
from module_1 import variable_1 as vv, list_1 as ll
# from module_1 import *

if __name__ == "__main__":
    module_1.func()
    module_1.variable_1 = 101
    variable_1 = 1000
    ll.append(11)
    ll.append(12)
    import module_2
        
    print(module_1.__dict__)
    module_1.__dict__['variable_1'] = 88
    print(list(module_1.__dict__.keys()))

    #import my_package_1
    #my_package_1.sub_module1.kek()
    #my_package_1.module1.kek()
    #print(__file__)
    
