val_1 = 1
val_2 = 2

if True:
    print('True')
if False:
    print('True')


if val_1 > val_2:
    print("if")
else:
    print("else")

    
if val_1 > val_2:
    print("val_1 > val_2")
elif val_1 < val_2:
    print("val_1 < val_2")
elif val_1 == val_2:
    print("val_1 == val_2")
else:
    print("else")

# is 
# not    
val_1 = 'asd'
if type(val_1) is int:
    print("int")
elif type(val_1) is not str:
    print("str")
elif type(val_1)  is not None:
    print("None")

#and  or
if val_1 == 1 and val_2 != 2:
    print("val_1 == 1 and val_2 != 2")

if val_1 == 1 or val_2 != 2:
    print("val_1 == 1 and val_2 != 2")

if ((val_1 < 1 or val_1 > 20) and
   (val_2 == 1 or val_2 != 2)):
   print("!")