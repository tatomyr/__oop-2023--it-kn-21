mystring = "hi"
myfloat = 19.9
myint = 123

if mystring == "hi":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 19.9:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 123:
    print("Integer: %d" % myint)